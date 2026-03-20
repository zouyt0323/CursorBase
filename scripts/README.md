# CursorBase 全局脚本

> 此目录仅存放跨项目的全局脚本。各项目专属脚本在各自的 `scripts/` 目录中。

## 全局脚本

| 脚本 | 功能 |
|------|------|
| `每周整理更新.sh` | Git 子仓库更新、Skills 索引重生成、日期备份、npm 更新 |

## 各项目脚本索引

| 项目 | 脚本目录 | 内容 |
|------|----------|------|
| 02.CursorRuleProject | `scripts/jni-helper/` | JNI 开发辅助工具 |
| 04.CursorSkillProject | `scripts/gen-skills-doc/` | 4 个 Skills 索引文档生成脚本 |
| 09.CursorPluginProject | `scripts/install-extensions/` | 一键安装所有扩展插件 |

## 使用方法

```bash
cd /home/tsdl/SSD/CursorProject/CursorBase
./scripts/每周整理更新.sh
```

定时执行（cron，每周一 9:00）：

```bash
0 9 * * 1 /home/tsdl/SSD/CursorProject/CursorBase/scripts/每周整理更新.sh
```
