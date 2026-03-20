# Cursor Plugin Project — Cursor 插件管理

> 本目录收集和管理 Cursor IDE 的扩展插件，包括完整的插件清单、一键安装脚本和各插件的使用文档。
>
> 最后更新：2026-03-15

---

## 目录结构

```
09.CursorPluginProject/
├── README.md                        # 本文件 — 插件总览与清单
├── scripts/install-extensions/       # 安装脚本
│   └── install-all-extensions.sh
├── 推荐安装插件列表.md               # 根据习惯整理的推荐插件
├── backup-YYYYMMDD-HHMMSS/          # 日期备份（插件列表、plugins、extensions.json）
│   ├── extensions-list.txt
│   ├── extensions.json
│   ├── plugins/
│   └── 已安装插件清单.md
└── cursor-usage/                    # Cursor Usage 插件
    ├── cursor-usage-0.0.7-bq.vsix   # 插件安装包
    └── Cursor-Usage安装与使用指南.md  # 安装使用文档
```

---

## 文档索引

| 文档 | 说明 |
|------|------|
| 本 README | 插件总览、清单、安装脚本 |
| [推荐安装插件列表](推荐安装插件列表.md) | 按习惯整理的推荐插件（含 Marketplace 与 VSCode 扩展） |
| [插件使用指南-按触发方式](插件使用指南-按触发方式.md) | 主动/被动触发方式与使用说明 |
| [cursor-usage 安装指南](cursor-usage/Cursor-Usage安装与使用指南.md) | Cursor Usage 本地插件安装 |

---

## 已安装插件清单（37 个，2026-03-20 更新）

> 详细分类与功能介绍见 [Cursor-Extensions-扩展总览.md](Cursor-Extensions-扩展总览.md)
> 已清理 5 个冗余扩展（2 个 PDF + 3 个 Mermaid）

### Cursor 内置

| 插件 ID | 版本 | 说明 |
|---------|------|------|
| `anysphere.cursorpyright` | 1.0.10 | Cursor 内置 Python 类型检查 |

### C/C++ 开发

| 插件 ID | 版本 | 说明 |
|---------|------|------|
| `llvm-vs-code-extensions.vscode-clangd` | 0.4.0 | clangd 语言服务前端（代码跳转、补全、诊断） |

### 语言包

| 插件 ID | 版本 | 说明 |
|---------|------|------|
| `ms-ceintl.vscode-language-pack-zh-hans` | 1.105.0 | 简体中文语言包 |

### Python 开发

| 插件 ID | 版本 | 说明 |
|---------|------|------|
| `ms-python.python` | 2025.6.1 | Python 语言支持（IntelliSense、调试、格式化） |
| `ms-python.debugpy` | 2025.18.0 | Python 调试器 |
| `ms-python.vscode-python-envs` | 1.10.0 | Python 环境管理 |

### Java 开发

| 插件 ID | 版本 | 说明 |
|---------|------|------|
| `redhat.java` | 1.53.0 | Java 语言支持（Language Server） |
| `vscjava.vscode-java-pack` | 0.30.5 | Java 扩展包（一键安装全套） |
| `vscjava.vscode-java-debug` | 0.58.5 | Java 调试器 |
| `vscjava.vscode-java-dependency` | 0.27.0 | Java 依赖管理 |
| `vscjava.vscode-java-test` | 0.44.0 | Java 测试运行器 |
| `vscjava.vscode-maven` | 0.45.1 | Maven 项目支持 |
| `vscjava.vscode-gradle` | 3.17.2 | Gradle 项目支持 |
| `ms-dotnettools.vscode-dotnet-runtime` | 3.0.0 | .NET 运行时（Java 插件依赖） |

### Docker & 容器

| 插件 ID | 版本 | 说明 |
|---------|------|------|
| `ms-azuretools.vscode-docker` | 2.0.0 | Docker 文件编辑、镜像管理、容器操作 |
| `ms-azuretools.vscode-containers` | 2.4.1 | 容器管理增强 |

### Markdown

| 插件 ID | 版本 | 说明 |
|---------|------|------|
| `davidanson.vscode-markdownlint` | 0.61.1 | Markdown 语法检查 |
| `yzane.markdown-pdf` | 1.5.0 | Markdown 导出为 PDF/HTML/PNG |

### Mermaid 图表（2 个，已精简）

| 插件 ID | 版本 | 说明 |
|---------|------|------|
| `bierner.markdown-mermaid` | 1.32.0 | Markdown 预览中渲染 Mermaid 图表 |
| `bpruitt-goddard.mermaid-markdown-syntax-highlighting` | 1.8.0 | Mermaid 语法高亮 |

### HTML / CSS

| 插件 ID | 版本 | 说明 |
|---------|------|------|
| `ecmel.vscode-html-css` | 2.0.14 | HTML 中 CSS 类名智能提示 |
| `htmlhint.vscode-htmlhint` | 1.16.0 | HTML 语法检查 |
| `formulahendry.auto-rename-tag` | 0.1.10 | 自动重命名配对 HTML 标签 |

### PDF / Office 文件（已精简，统一由 vscode-office 提供）

| 插件 ID | 版本 | 说明 |
|---------|------|------|
| `cweijan.vscode-office` | 3.5.4 | Office 文件预览（Excel/Word/PPT/PDF/SVG） |

### Git

| 插件 ID | 版本 | 说明 |
|---------|------|------|
| `donjayamanne.githistory` | 0.6.20 | Git 历史记录查看 |

### 数据库

| 插件 ID | 版本 | 说明 |
|---------|------|------|
| `qwtel.sqlite-viewer` | 26.2.5 | SQLite 数据库查看器 |

### 本地/自定义插件

| 插件 ID | 版本 | 说明 | 文档 |
|---------|------|------|------|
| `local.cursor-usage` | 0.0.7-bq | Cursor Included-Request 用量实时监控 | [安装指南](./cursor-usage/Cursor-Usage安装与使用指南.md) |

---

## 一键安装

### 安装所有插件

```bash
bash scripts/install-extensions/install-all-extensions.sh
```

### 仅安装本地插件

```bash
cursor --install-extension cursor-usage/cursor-usage-0.0.7-bq.vsix
```

### 导出当前插件列表

```bash
cursor --list-extensions --show-versions > extensions-list.txt
```

### 从列表批量安装

```bash
# 从纯文本列表安装（每行一个插件 ID）
while read ext; do
    cursor --install-extension "$ext"
done < extensions-list.txt
```

---

## 插件分类统计

| 分类 | 数量 | 说明 |
|------|------|------|
| Python 开发 | 3 | 语言支持 + 调试 + 环境管理 |
| Java 开发 | 7 | 全套 Java 开发工具链 |
| Docker | 2 | 容器管理 |
| Markdown | 2 | 语法检查 + PDF 导出 |
| Mermaid 图表 | 2 | 语法高亮 + Markdown 内渲染 |
| HTML/CSS | 3 | 智能提示 + 语法检查 |
| PDF/Office | 1 | vscode-office 统一预览 |
| Git | 1 | 历史记录 |
| 数据库 | 1 | SQLite 查看 |
| 语言包 | 1 | 中文 |
| C/C++ 开发 | 1 | clangd 语言服务 |
| Cursor 内置 | 1 | 类型检查 |
| 本地自定义 | 1 | 用量监控 |
| **合计** | **37** | 含 GrapeCity Excel、GitLens、Error Lens 等新增 |

---

## 卸载插件

```bash
# 卸载单个插件
cursor --uninstall-extension <publisher>.<extension-name>

# 示例
cursor --uninstall-extension local.cursor-usage
```

---

## 插件配置（已自动应用）

工程根目录 `.vscode/settings.json` 已配置：

- **保存时自动格式化**（Prettier）
- **保存时 ESLint 自动修复**
- **Error Lens 行内错误显示**
- **Todo Tree 标签**：TODO、FIXME、XXX、HACK、NOTE
- **Code Spell Checker**：中英文拼写检查
- **各语言默认格式化器**：JS/TS/JSON/MD 用 Prettier，Python 用 Python 插件

`.vscode/extensions.json` 包含推荐插件列表，打开工程时会提示安装。

---

## License

各插件遵循其原有许可证。
