# Cursor 扩展总览

> 更新时间：2026-03-20
> 已安装扩展：37 个（已清理 5 个冗余扩展）

---

## 一、已安装扩展（按功能分类）

### 1. 语言支持与开发工具

| 扩展 | 版本 | 功能 |
|------|------|------|
| `ms-python.python` | 2025.6.1 | Python 语言支持（IntelliSense、调试、格式化、Linting） |
| `ms-python.debugpy` | 2025.18.0 | Python 调试器（断点、变量查看、远程调试） |
| `ms-python.vscode-python-envs` | 1.10.0 | Python 虚拟环境管理（venv、conda 切换） |
| `anysphere.cursorpyright` | 1.0.10 | Cursor 定制版 Pyright（Python 类型检查） |
| `redhat.java` | 1.53.0 | Java 语言支持（Language Server Protocol） |
| `vscjava.vscode-java-pack` | 0.30.5 | Java 扩展包（集成调试、测试、依赖管理） |
| `vscjava.vscode-java-debug` | 0.58.5 | Java 调试器 |
| `vscjava.vscode-java-test` | 0.44.0 | Java 单元测试运行器（JUnit、TestNG） |
| `vscjava.vscode-java-dependency` | 0.27.0 | Java 依赖管理与项目视图 |
| `vscjava.vscode-maven` | 0.45.1 | Maven 项目支持（构建、依赖树） |
| `vscjava.vscode-gradle` | 3.17.2 | Gradle 项目支持（任务运行、依赖管理） |
| `ms-dotnettools.vscode-dotnet-runtime` | 3.0.0 | .NET 运行时安装（Java 扩展依赖） |
| `mathiasfrohlich.kotlin` | 1.7.1 | Kotlin 语言支持（语法高亮、代码片段） |
| `llvm-vs-code-extensions.vscode-clangd` | 0.4.0 | C/C++ 语言支持（clangd LSP，代码补全、导航） |

### 2. Web 前端开发

| 扩展 | 版本 | 功能 |
|------|------|------|
| `ecmel.vscode-html-css` | 2.0.14 | HTML/CSS 智能提示（class 名补全、CSS 属性） |
| `formulahendry.auto-rename-tag` | 0.1.10 | HTML 标签自动重命名（改开始标签自动改结束标签） |
| `htmlhint.vscode-htmlhint` | 1.16.0 | HTML 静态分析（代码规范检查） |
| `dbaeumer.vscode-eslint` | 3.0.24 | ESLint 集成（JavaScript/TypeScript 代码检查） |
| `esbenp.prettier-vscode` | 12.4.0 | Prettier 代码格式化（JS/TS/CSS/HTML/JSON/Markdown） |

### 3. Markdown 与文档

| 扩展 | 版本 | 功能 |
|------|------|------|
| `davidanson.vscode-markdownlint` | 0.61.1 | Markdown 语法检查（规范格式） |
| `yzane.markdown-pdf` | 1.5.0 | Markdown 导出为 PDF/HTML/PNG/JPEG |
| `bierner.markdown-mermaid` | 1.32.0 | Markdown 预览中渲染 Mermaid 图表 |
| `bpruitt-goddard.mermaid-markdown-syntax-highlighting` | 1.8.0 | Mermaid 代码块语法高亮 |

### 4. Mermaid 图表

> 已精简：删除了 `mermaidchart.vscode-mermaid-chart`、`tomoyukim.vscode-mermaid-editor`、`vstirbu.vscode-mermaid-preview`（功能重叠）

*Mermaid 渲染由 Markdown 扩展（`bierner.markdown-mermaid` + `bpruitt-goddard.mermaid-markdown-syntax-highlighting`）提供，见上方 Markdown 分类。*

### 5. 文件预览

| 扩展 | 版本 | 功能 |
|------|------|------|
| `cweijan.vscode-office` | 3.5.4 | Office 文件预览（docx/xlsx/pptx/pdf/svg 等） |
| `grapecity.gc-excelviewer` | 4.2.58 | Excel/CSV 表格预览（排序、筛选） |
> 已精简：删除了 `mathematic.vscode-pdf` 和 `tomoki1207.pdf`（PDF 预览由 `vscode-office` 统一提供）
| `qwtel.sqlite-viewer` | 26.2.5 | SQLite 数据库文件浏览器（表结构、数据查询） |
| `kisstkondoros.vscode-gutter-preview` | 0.32.2 | 图片预览（在代码行号旁显示图片缩略图） |

### 6. Git 与版本控制

| 扩展 | 版本 | 功能 |
|------|------|------|
| `eamodio.gitlens` | 17.11.1 | Git 增强（行级 blame、提交历史、分支对比、代码作者） |
| `donjayamanne.githistory` | 0.6.20 | Git 历史查看器（提交图、文件历史、分支对比） |

### 7. Docker 与容器

| 扩展 | 版本 | 功能 |
|------|------|------|
| `ms-azuretools.vscode-docker` | 2.0.0 | Docker 集成（镜像管理、容器操作、Dockerfile 支持） |
| `ms-azuretools.vscode-containers` | 2.4.1 | 容器管理（Dev Containers 支持） |

### 8. 代码质量与效率

| 扩展 | 版本 | 功能 |
|------|------|------|
| `aaron-bond.better-comments` | 3.0.2 | 注释增强（彩色分类：TODO/FIXME/NOTE/警告等） |
| `usernamehw.errorlens` | 3.26.0 | 错误内联显示（在代码行末直接显示错误/警告信息） |
| `streetsidesoftware.code-spell-checker` | 4.5.6 | 拼写检查（变量名、注释、字符串中的拼写错误） |
| `gruntfuggly.todo-tree` | 0.0.215 | TODO 树（汇总项目中所有 TODO/FIXME/HACK 标记） |

### 9. 本地化

| 扩展 | 版本 | 功能 |
|------|------|------|
| `ms-ceintl.vscode-language-pack-zh-hans` | 1.105.0 | 中文简体语言包 |

### 10. 自定义/本地扩展

| 扩展 | 版本 | 功能 |
|------|------|------|
| `local.cursor-usage` | 0.0.7-bq | Cursor 用量统计（自定义本地扩展） |

---

## 二、推荐安装的扩展（按场景）

### 场景 1：Android 开发增强

| 扩展 | ID | 功能 |
|------|-----|------|
| Android Full Support | `nicholasmata.android-full-support` | Android 项目支持（Gradle 同步、ADB 集成） |
| Logcat | `nicholasmata.logcat` | Android Logcat 日志查看器 |

### 场景 2：AI 辅助开发

| 扩展 | ID | 功能 |
|------|-----|------|
| Continue | `continue.continue` | 开源 AI 编程助手（支持多模型） |
| Codeium | `codeium.codeium` | AI 代码补全（免费） |

> 注：Cursor 本身已内置 AI 功能，这些扩展可作为补充。

### 场景 3：远程开发

| 扩展 | ID | 功能 |
|------|-----|------|
| Remote - SSH | `ms-vscode-remote.remote-ssh` | SSH 远程开发（连接远程服务器编辑代码） |
| Remote Explorer | `ms-vscode.remote-explorer` | 远程连接管理器 |

### 场景 4：数据库管理

| 扩展 | ID | 功能 |
|------|-----|------|
| Database Client | `cweijan.vscode-database-client2` | 数据库客户端（MySQL/PostgreSQL/SQLite/MongoDB） |
| Redis | `cweijan.vscode-redis-client` | Redis 客户端 |

### 场景 5：API 开发与测试

| 扩展 | ID | 功能 |
|------|-----|------|
| Thunder Client | `rangav.vscode-thunder-client` | REST API 客户端（类似 Postman） |
| REST Client | `humao.rest-client` | HTTP 请求发送器（在 .http 文件中发请求） |

### 场景 6：Shell 脚本开发

| 扩展 | ID | 功能 |
|------|-----|------|
| ShellCheck | `timonwong.shellcheck` | Shell 脚本静态分析（检查常见错误） |
| Bash IDE | `mads-hartmann.bash-ide-vscode` | Bash 语言支持（补全、跳转、重命名） |

### 场景 7：主题与美化

| 扩展 | ID | 功能 |
|------|-----|------|
| Material Icon Theme | `pkief.material-icon-theme` | 文件图标主题（美化文件树） |
| One Dark Pro | `zhuangtongfa.material-theme` | 热门暗色主题 |
| Indent Rainbow | `oderwat.indent-rainbow` | 缩进彩虹（不同层级不同颜色） |

### 场景 8：项目管理

| 扩展 | ID | 功能 |
|------|-----|------|
| Project Manager | `alefragnani.project-manager` | 项目切换器（快速在多个项目间切换） |
| Bookmarks | `alefragnani.bookmarks` | 代码书签（标记重要位置快速跳转） |

### 场景 9：Markdown 增强

| 扩展 | ID | 功能 |
|------|-----|------|
| Markdown All in One | `yzhang.markdown-all-in-one` | Markdown 全能工具（快捷键、TOC、列表编辑） |
| Markdown Preview Github Styling | `bierner.markdown-preview-github-styles` | GitHub 风格 Markdown 预览 |

---

## 三、扩展冗余分析

当前有以下功能重叠的扩展：

| 功能 | 重叠扩展 | 建议 |
|------|----------|------|
| PDF 预览 | `mathematic.vscode-pdf` + `tomoki1207.pdf` + `cweijan.vscode-office` | 保留 `vscode-office`（最全面），可卸载另外两个 |
| Excel 预览 | `grapecity.gc-excelviewer` + `cweijan.vscode-office` | `gc-excelviewer` 表格功能更强，建议保留两个 |
| Mermaid | 4 个 Mermaid 扩展 | `bierner.markdown-mermaid`（Markdown 内渲染）+ `tomoyukim.vscode-mermaid-editor`（编辑器）足够，可精简 |

---

## 四、统计摘要

| 分类 | 数量 |
|------|------|
| 语言支持与开发工具 | 14 |
| Web 前端开发 | 5 |
| Markdown 与文档（含 Mermaid） | 4 |
| 文件预览 | 4 |
| Git 与版本控制 | 2 |
| Docker 与容器 | 2 |
| 代码质量与效率 | 4 |
| 本地化 | 1 |
| 自定义扩展 | 1 |
| **合计** | **37** |
