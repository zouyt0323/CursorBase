#!/bin/bash
# JNI 跨语言导航辅助脚本
# 用法:
#   jni-helper.sh find-native <Java类全限定名>     — 查找 Java native 方法对应的 C 实现
#   jni-helper.sh find-java   <JNI C函数名>        — 从 C 函数名反查 Java 类和方法
#   jni-helper.sh gen-header  <Java源文件> [输出目录] — 生成 JNI 头文件
#   jni-helper.sh scan        <目录>               — 扫描目录下所有 JNI 注册关系

set -euo pipefail

if command -v rg &>/dev/null; then
    SEARCH_CMD="rg"
else
    SEARCH_CMD="grep"
fi

search_c_cpp() {
    local pattern="$1"
    local dir="$2"
    if [ "$SEARCH_CMD" = "rg" ]; then
        rg --type c --type cpp "$pattern" "$dir" 2>/dev/null
    else
        grep -rn --include='*.c' --include='*.cpp' --include='*.cc' --include='*.h' --include='*.hpp' "$pattern" "$dir" 2>/dev/null
    fi
}

search_java() {
    local pattern="$1"
    local dir="$2"
    if [ "$SEARCH_CMD" = "rg" ]; then
        rg --type java "$pattern" "$dir" 2>/dev/null
    else
        grep -rn --include='*.java' "$pattern" "$dir" 2>/dev/null
    fi
}

search_c_cpp_only_match() {
    local pattern="$1"
    local dir="$2"
    if [ "$SEARCH_CMD" = "rg" ]; then
        rg --type c --type cpp -o "$pattern" "$dir" 2>/dev/null
    else
        grep -roh --include='*.c' --include='*.cpp' --include='*.cc' --include='*.h' --include='*.hpp' "$pattern" "$dir" 2>/dev/null
    fi
}

search_c_cpp_context() {
    local pattern="$1"
    local dir="$2"
    local before="${3:-2}"
    local after="${4:-5}"
    if [ "$SEARCH_CMD" = "rg" ]; then
        rg --type c --type cpp -B"$before" -A"$after" "$pattern" "$dir" 2>/dev/null
    else
        grep -rn --include='*.c' --include='*.cpp' --include='*.cc' --include='*.h' --include='*.hpp' -B"$before" -A"$after" "$pattern" "$dir" 2>/dev/null
    fi
}

usage() {
    echo "JNI 跨语言导航辅助脚本 (搜索引擎: $SEARCH_CMD)"
    echo ""
    echo "用法:"
    echo "  $0 find-native <Java类全限定名>           查找 native 方法的 C 实现"
    echo "  $0 find-java   <JNI_C函数名>              从 C 函数名反查 Java 类"
    echo "  $0 gen-header  <Java源文件> [输出目录]     生成 JNI 头文件"
    echo "  $0 scan        <目录>                     扫描目录下所有 JNI 映射"
    echo ""
    echo "示例:"
    echo "  $0 find-native com.android.server.SystemServer"
    echo "  $0 find-java Java_com_android_server_SystemServer_nativeInit"
    echo "  $0 gen-header frameworks/base/core/java/android/os/Binder.java"
    echo "  $0 scan frameworks/base/core/jni/"
    exit 1
}

jni_mangle_classname() {
    echo "$1" | sed 's/\./\//g' | sed 's/\//_/g'
}

find_native_impl() {
    local classname="$1"
    local mangled
    mangled=$(jni_mangle_classname "$classname")
    local search_dir="${2:-.}"

    echo "=== 查找 $classname 的 JNI 实现 ==="
    echo ""

    echo "--- 静态注册 (Java_包名_类名_方法名) ---"
    search_c_cpp "Java_${mangled}_" "$search_dir" || echo "  未找到静态注册的 JNI 函数"
    echo ""

    echo "--- 动态注册 (JNINativeMethod / RegisterNatives) ---"
    local short_class
    short_class=$(echo "$classname" | awk -F. '{print $NF}')
    local class_path="${classname//./\/}"
    search_c_cpp "$class_path" "$search_dir" || search_c_cpp "RegisterNatives.*${short_class}" "$search_dir" || echo "  未找到动态注册"
}

find_java_class() {
    local jni_func="$1"
    local search_dir="${2:-.}"

    if [[ "$jni_func" == Java_* ]]; then
        local parts
        parts=$(echo "$jni_func" | sed 's/^Java_//' | sed 's/_/./g')
        echo "=== JNI 函数: $jni_func ==="
        echo "可能对应的 Java 类: $parts"
        echo ""
        echo "--- 搜索 native 方法声明 ---"
        local method_name
        method_name=$(echo "$jni_func" | awk -F_ '{print $NF}')
        search_java "native.*${method_name}" "$search_dir" || echo "  未找到匹配的 native 声明"
    else
        echo "=== 搜索动态注册的函数: $jni_func ==="
        search_c_cpp "\"$jni_func\"" "$search_dir" || echo "  未找到"
        echo ""
        echo "--- 搜索 Java native 声明 ---"
        search_java "native.*${jni_func}" "$search_dir" || echo "  未找到"
    fi
}

gen_jni_header() {
    local java_file="$1"
    local output_dir="${2:-.}"

    if ! command -v javac &>/dev/null; then
        echo "[ERROR] javac 未找到，请确认 JDK 已安装"
        exit 1
    fi

    local classname
    classname=$(grep -oP 'package\s+\K[^;]+' "$java_file" 2>/dev/null || echo "")
    local file_basename
    file_basename=$(basename "$java_file" .java)

    if [ -n "$classname" ]; then
        classname="${classname}.${file_basename}"
    else
        classname="$file_basename"
    fi

    echo "=== 为 $classname 生成 JNI 头文件 ==="
    mkdir -p "$output_dir"
    javac -h "$output_dir" -d /tmp/jni_classes "$java_file" 2>&1 || {
        echo "[WARN] javac 编译失败，尝试仅提取 native 方法签名..."
        echo ""
        echo "--- $java_file 中的 native 方法 ---"
        grep -n "native" "$java_file" | grep -v "//"
    }

    echo ""
    local header_file="$output_dir/${classname//\./_}.h"
    if [ -f "$header_file" ]; then
        echo "已生成: $header_file"
        cat "$header_file"
    fi
}

scan_jni_mappings() {
    local search_dir="${1:-.}"

    echo "=== 扫描 JNI 映射关系: $search_dir ==="
    echo ""

    echo "--- 静态注册的 JNI 函数 ---"
    search_c_cpp_only_match 'Java_[A-Za-z0-9_]\+' "$search_dir" | sort -u || echo "  无"
    echo ""

    echo "--- 动态注册 (JNINativeMethod 数组) ---"
    search_c_cpp_context 'JNINativeMethod' "$search_dir" 2 5 | head -100 || echo "  无"
    echo ""

    echo "--- RegisterNatives 调用 ---"
    search_c_cpp 'RegisterNatives' "$search_dir" || echo "  无"
    echo ""

    echo "--- Java native 方法声明 ---"
    search_java '\bnative\b' "$search_dir" | grep -v '//' | head -50 || echo "  无"
}

[ $# -lt 1 ] && usage

case "$1" in
    find-native)
        [ $# -lt 2 ] && usage
        find_native_impl "$2" "${3:-.}"
        ;;
    find-java)
        [ $# -lt 2 ] && usage
        find_java_class "$2" "${3:-.}"
        ;;
    gen-header)
        [ $# -lt 2 ] && usage
        gen_jni_header "$2" "${3:-.}"
        ;;
    scan)
        scan_jni_mappings "${2:-.}"
        ;;
    *)
        usage
        ;;
esac
