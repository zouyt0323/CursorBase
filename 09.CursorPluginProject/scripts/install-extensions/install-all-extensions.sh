#!/bin/bash
# Cursor 插件一键安装脚本
# 用法: bash install-all-extensions.sh
# 说明: 安装所有已记录的 Cursor/VS Code 扩展插件

set -e

echo "=========================================="
echo "  Cursor 插件一键安装脚本"
echo "=========================================="
echo ""

CURSOR_CMD="cursor"
if ! command -v $CURSOR_CMD &> /dev/null; then
    echo "[ERROR] 未找到 cursor 命令，请确认 Cursor IDE 已安装并在 PATH 中"
    exit 1
fi

EXTENSIONS=(
    # ─── Cursor 内置 ───
    "anysphere.cursorpyright"

    # ─── 语言包 ───
    "ms-ceintl.vscode-language-pack-zh-hans"

    # ─── Python 开发 ───
    "ms-python.python"
    "ms-python.debugpy"
    "ms-python.vscode-python-envs"

    # ─── Java 开发 ───
    "redhat.java"
    "vscjava.vscode-java-pack"
    "vscjava.vscode-java-debug"
    "vscjava.vscode-java-dependency"
    "vscjava.vscode-java-test"
    "vscjava.vscode-maven"
    "vscjava.vscode-gradle"
    "ms-dotnettools.vscode-dotnet-runtime"

    # ─── C/C++ ───
    "llvm-vs-code-extensions.vscode-clangd"

    # ─── Docker ───
    "ms-azuretools.vscode-docker"
    "ms-azuretools.vscode-containers"

    # ─── Markdown ───
    "davidanson.vscode-markdownlint"
    "yzane.markdown-pdf"

    # ─── Mermaid 图表 ───
    "bierner.markdown-mermaid"
    "bpruitt-goddard.mermaid-markdown-syntax-highlighting"
    "mermaidchart.vscode-mermaid-chart"
    "tomoyukim.vscode-mermaid-editor"
    "vstirbu.vscode-mermaid-preview"

    # ─── HTML/CSS ───
    "ecmel.vscode-html-css"
    "htmlhint.vscode-htmlhint"
    "formulahendry.auto-rename-tag"

    # ─── PDF / Office ───
    "tomoki1207.pdf"
    "mathematic.vscode-pdf"
    "cweijan.vscode-office"

    # ─── Git ───
    "donjayamanne.githistory"

    # ─── 数据库 ───
    "qwtel.sqlite-viewer"
)

TOTAL=${#EXTENSIONS[@]}
INSTALLED=0
FAILED=0

echo "共 $TOTAL 个插件待安装"
echo ""

for ext in "${EXTENSIONS[@]}"; do
    echo -n "[$((INSTALLED + FAILED + 1))/$TOTAL] 安装 $ext ... "
    if $CURSOR_CMD --install-extension "$ext" --force 2>/dev/null; then
        echo "✅"
        ((INSTALLED++))
    else
        echo "❌"
        ((FAILED++))
    fi
done

echo ""
echo "=========================================="
echo "  安装完成"
echo "  成功: $INSTALLED / $TOTAL"
if [ $FAILED -gt 0 ]; then
    echo "  失败: $FAILED"
fi
echo "=========================================="
echo ""

# 安装本地 .vsix 插件
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VSIX_FILE="$SCRIPT_DIR/cursor-usage/cursor-usage-0.0.7-bq.vsix"
if [ -f "$VSIX_FILE" ]; then
    echo -n "安装本地插件 cursor-usage ... "
    if $CURSOR_CMD --install-extension "$VSIX_FILE" 2>/dev/null; then
        echo "✅"
    else
        echo "❌"
    fi
fi

echo ""
echo "请执行 Ctrl+Shift+P → Developer: Reload Window 重新加载窗口"
