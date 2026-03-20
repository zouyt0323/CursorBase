# Cursor 从编译到提交的打工日记

> 来源：[飞书文档](https://thundersoft.feishu.cn/wiki/RLsGwMehEiQnnYk5XfDcMwNZnWd)

---

"为AI而生-中科创达AI发烧友社区" 群应该有权限，直接进群就可以了。

## 前提

我的 cursor 已经基本学会了使用 jenkins、gerrit、adb 操作设备、AOSP 编译版本、ftp 下载、刷机等技能

## 背景

产测工具因为传感器有启动时间要求 UI 换位置。

需求很简单，代码就一下，过程很麻烦，可是我很懒，但是还得干，怎么干，让 cursor 干。
简单的任务正好可以用来帮 AI 捋顺 SKILL 流程。

## 概览

先看，任务完成总结：

1. **Gradle 编译** - 在 `mmi/code/mmi/` 下执行 `assembleDebug`，生成 `app-debug.apk`
2. **替换 APK** - 将新 APK 复制到 `mmi/app-debug.apk`
3. **Android 源码编译** - `source build/envsetup.sh && lunch qssi-userdebug && make mmi`，产物：`system_ext/app/mmi/mmi.apk`
4. **刷入 qssi 版本** - 使用 qssi15-dev #28156 的 FlatBuild 刷机（含 wipefirst 擦除）
5. **刷入产物 A** - `adb push mmi.apk /system_ext/app/mmi/mmi.apk`
6. **验证 UI** - 截图确认 HDMI 输入测试按钮已移到环境传感器之前
7. **提交 Gerrit** - Change #541100
8. **Jenkins 编译** - 已触发，在队列中等待执行

## 过程

忘记了 Mdep 到 Qssi 版本需要进行 erase all，进入 recovery 了，没办法手动进入下 EDL 模式。

## SKILL

总结了一份 Skill.md 可以做到同样的事。

---

```
---
name: panola-qssi-build-verify
description: Panola 项目 qssi 分支 APK 修改的完整构建验证流程。当用户需要编译 MMI APK、刷入 qssi 版本验证、提交 Gerrit 并触发 Jenkins 编译时使用。适用于 vendor/thundercomm/apps 仓库的 qssi15-dev 分支。
---
```

# Panola QSSI 分支 APK 构建与验证

## 项目信息

| 项目 | 值 |
|------|-----|
| 源码根目录 | `/home/tsdl/mdep-qssi/QCM6490_apps_qssi15/LINUX/android/` |
| APK 仓库 | `vendor/thundercomm/apps` |
| MMI 模块目录 | `vendor/thundercomm/apps/mmi/` |
| Gradle 项目 | `mmi/code/mmi/` |
| 预编译 APK | `mmi/app-debug.apk` |
| Android.mk 模块名 | `mmi` |
| 包名 | `com.thundersoft.factory.sensor` |
| 主 Activity | `.MainActivity` |
| Git remote | `caf` |
| 目标分支 | `Panola-qcm6490-la5.1-qssi15-dev` |
| 提交格式 | `[MDEP][Common][Feature]: 描述` |
| IssueID | `PANOLA-51` |

## FTP 信息

| 项目 | 值 |
|------|-----|
| FTP 子目录 | `Panola-qcm6490-la5.1-qssi15-dev` |
| FlatBuild 文件名模式 | `FlatBuild_Turbox-QCS5430_xx.xx_la5.1.V.userdebug.{日期}.{时间}_factory.zip` |

其他 FTP 信息参考 `panola-ftp-download` Skill。

## 完整流程

### 步骤 1：Gradle 编译生成 APK

```bash
cd vendor/thundercomm/apps/mmi/code/mmi/
./gradlew assembleDebug
```

产物：`app/build/outputs/apk/debug/app-debug.apk`

### 步骤 2：替换预编译 APK

```bash
cp mmi/code/mmi/app/build/outputs/apk/debug/app-debug.apk mmi/app-debug.apk
```

### 步骤 3：Android 源码编译 mmi 模块

```bash
cd /home/tsdl/mdep-qssi/QCM6490_apps_qssi15/LINUX/android/
bash -c 'source build/envsetup.sh && lunch qssi-userdebug && make mmi'
```

产物 A：`out/target/product/qssi/system_ext/app/mmi/mmi.apk`

### 步骤 4：刷入 qssi 基础版本

1. 从 FTP 下载最新 qssi15-dev FlatBuild（参考 `panola-ftp-download` Skill）
2. 解压 FlatBuild
3. 刷机（参考 `panola-flash-device` Skill）

**重要**：从 mdep 版本切换到 qssi 版本时，需要使用 `--wipefirst` 参数：

```bash
# QSaharaServer 成功后，fh_loader 需加 --wipefirst
{解压目录}/fh_loader \
  --port=/dev/ttyUSB0 \
  --sendxml=rawprogram_unsparse0.xml,rawprogram1.xml,...,patch5.xml \
  --search_path={解压目录}/ufs \
  --memoryname=UFS \
  --noprompt \
  --showpercentagecomplete \
  --wipefirst
```

**注意**：`--erase` 需要 `=` 号（如 `--erase=partition_name`），直接用 `--erase` 会报错。应使用 `--wipefirst` 或 `--erasefirst` 来擦除。

### 步骤 5：推送产物 A 到设备

```bash
adb root
adb remount
# 首次 remount 后需重启
adb reboot
# 等待设备重启后再次
adb root
adb remount
# 推送 APK
adb push out/target/product/qssi/system_ext/app/mmi/mmi.apk /system_ext/app/mmi/mmi.apk
adb reboot
```

### 步骤 6：验证 UI 修改

```bash
# 启动 MMI APP
adb shell am start -n com.thundersoft.factory.sensor/.MainActivity
# 截图验证
adb shell screencap -p /sdcard/screenshot.png
adb pull /sdcard/screenshot.png /tmp/mmi_screenshot.png
```

然后用 Read 工具查看截图，确认 UI 修改是否生效。

### 步骤 7：提交到 Gerrit

```bash
cd vendor/thundercomm/apps
git add mmi/app-debug.apk mmi/code/mmi/app/src/main/res/layout/activity_main.xml
# 提交信息文件方式（Cursor 会自动注入 --trailer，git 2.25.1 不支持，需用 -F）
git commit -F /tmp/commit_msg.txt
git push caf HEAD:refs/for/Panola-qcm6490-la5.1-qssi15-dev
```

**提交格式**：

```
[MDEP][Common][Feature]: 描述

详细说明

IssueID: PANOLA-51
```

**Cursor git 兼容性问题**：git 2.25.1 不支持 `--trailer` 选项，Cursor 自动注入 `--trailer 'Made-with: Cursor'` 会导致 `git commit -m` 和 `git commit -F` 失败。解决方案：使用 `-c trailer.ifexists=addIfDifferent` 参数，如：

```bash
/usr/bin/git -c trailer.ifexists=addIfDifferent commit -F /tmp/commit_msg.txt
```

### 步骤 8：触发 Jenkins 编译

Jenkins Job：`VerifyBuild_for_IOT_6490`

凭据从 memory 获取（搜索 `Jenkins Credentials`）。

**关键参数**（参考 qssi15-dev 构建）：

```
GERRITID_Qssi={gerrit_change_number}
GERRITID_Vendor=
GERRITID_MDEP=
Manifest_Branch=Turbox-QCM6490.LA.5.1
Manifest_Name=Panola-qcm6490-la5.1-qssi15-dev.xml
Manifest_Name2=Panola-qcm6490-la5.1-vendor-dev.xml
Manifest_Name3=NULL
CI_BUILD_VARIANT=userdebug
CI_BUILD_MODULE=ALL
Extra_Build_Options=--user-opt-1 qssi
PACK_FLAT=True
CI_CLEAN_CACHE=True
CI_BUILD_TYPE=V
ENTER_BP_CODE=True
COPY_TO_DL=True
SIGN_OPTION=True
TC_PRODUCT_DISTRICT=ROW
TC_PRODUCT_CUST_VERSION=QUALCOMM
delete_workspace=True
```

触发方式：

```bash
curl -s -X POST -u "{username}:{api_token}" \
  "https://jenkins.thundercomm.com/job/VerifyBuild_for_IOT_6490/buildWithParameters" \
  --data-urlencode "GERRITID_Qssi={change_number}" \
  --data-urlencode "Manifest_Branch=Turbox-QCM6490.LA.5.1" \
  ... (其余参数)
```

成功返回 HTTP 201。

## 注意事项

- Panola qssi 分支的 FTP 目录是 `Panola-qcm6490-la5.1-qssi15-dev`，与 vendor-dev 不同
- FlatBuild 文件名包含 `QCS5430`（不是 QCM6490）
- mdep → qssi 切换必须 wipefirst，否则可能无法启动
- 设备序列号：`5B91E648`
- APK 安装路径：`/system_ext/app/mmi/mmi.apk`
- `adb remount` 首次需要重启后才生效
