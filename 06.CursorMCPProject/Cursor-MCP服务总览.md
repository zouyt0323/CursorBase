# Cursor MCP 服务总览

> 本文整理了当前 Cursor 中已安装的全部 **19 个** MCP（Model Context Protocol）服务，包括安装方案、配置详情和使用方法。
>
> 配置文件路径：`~/.cursor/mcp.json`
>
> 最后更新：2026-03-17

---

## 目录

1. [drawio — Draw.io 图表控制](#1-drawio--drawio-图表控制)
2. [TalkToFigma — Figma 双向交互](#2-talktofigma--figma-双向交互)
3. [figma — Figma 设计数据读取](#3-figma--figma-设计数据读取)
4. [lark-mcp — 飞书/Lark 集成](#4-lark-mcp--飞书lark-集成)
5. [playwright — 浏览器自动化](#5-playwright--浏览器自动化)
6. [n8n-mcp — n8n 工作流文档](#6-n8n-mcp--n8n-工作流文档)
7. [Pdf Reader Mcp — PDF 读取](#7-pdf-reader-mcp--pdf-读取)
8. [interactive-feedback — Qt 交互式反馈](#8-interactive-feedback--qt-交互式反馈)
9. [openspec — 规范变更管理](#9-openspec--规范变更管理)
10. [cursor-mcp-installer — MCP 安装器](#10-cursor-mcp-installer--mcp-安装器)
11. [context7 — 实时代码文档](#11-context7--实时代码文档)
12. [github — GitHub 集成](#12-github--github-集成)
13. [figma-remote — Figma 官方远程 MCP](#13-figma-remote--figma-官方远程-mcp)
14. [android-mcp — Android 设备控制](#14-android-mcp--android-设备控制)
15. [sequential-thinking — 结构化逐步推理](#15-sequential-thinking--结构化逐步推理)
16. [memory — 持久化记忆](#16-memory--持久化记忆)
17. [fetch — 网页内容获取](#17-fetch--网页内容获取)
18. [exa — AI 智能搜索](#18-exa--ai-智能搜索)
19. [MCP Local RAG — 本地 RAG 语义搜索](#19-mcp-local-rag本地-rag-语义搜索)
20. [通用维护指南](#通用维护指南)

---

## 1. drawio — Draw.io 图表控制

| 项目 | 说明 |
|------|------|
| **GitHub** | [lgazo/drawio-mcp-server](https://github.com/lgazo/drawio-mcp-server) |
| **功能** | 通过 AI 在 Draw.io 中创建、编辑、管理图表元素和图层 |
| **运行时** | Node.js（全局安装） |
| **传输方式** | STDIO + WebSocket（端口 3334 连接浏览器扩展） |

### 安装方案

```bash
npm install -g drawio-mcp-server
```

```json
"drawio": {
  "command": "/home/tsdl/.nvm/versions/node/v24.13.0/bin/node",
  "args": [
    "/home/tsdl/.nvm/versions/node/v24.13.0/lib/node_modules/drawio-mcp-server/build/index.js",
    "--extension-port", "3334"
  ]
}
```

### 主要工具（19 个）

| 分类 | 工具 | 说明 |
|------|------|------|
| 查看 | `get-selected-cell` | 获取当前选中单元格属性 |
| 查看 | `list-paged-model` | 分页列出图中所有单元格 |
| 编辑 | `add-rectangle` / `add-cell-of-shape` / `add-edge` | 添加矩形/形状/连线 |
| 编辑 | `edit-cell` / `edit-edge` / `delete-cell-by-id` | 修改/删除元素 |
| 图层 | `list-layers` / `create-layer` / `move-cell-to-layer` | 图层管理 |

---

## 2. TalkToFigma — Figma 双向交互

| 项目 | 说明 |
|------|------|
| **GitHub** | [grab/cursor-talk-to-figma-mcp](https://github.com/grab/cursor-talk-to-figma-mcp) |
| **功能** | 在 Cursor 中双向控制 Figma：创建/编辑/删除节点、设置样式、管理布局 |
| **运行时** | Bun v1.3.8+（通过 bunx） |
| **传输方式** | STDIO → WebSocket (端口 3055) → Figma 插件 |

### 安装方案

```json
"TalkToFigma": {
  "command": "/home/tsdl/.bun/bin/bunx",
  "args": ["cursor-talk-to-figma-mcp@latest"]
}
```

### 主要工具（30+ 个）

包括连接、读取、创建、编辑、布局、导出、注释、导航等全方位 Figma 操作。

---

## 3. figma — Figma 设计数据读取

| 项目 | 说明 |
|------|------|
| **npm** | [figma-developer-mcp](https://www.npmjs.com/package/figma-developer-mcp) |
| **功能** | 只读方式获取 Figma 文件的布局、内容、视觉和组件信息 |

```json
"figma": {
  "command": "npx",
  "args": ["-y", "figma-developer-mcp@latest", "--stdio"],
  "env": { "FIGMA_API_KEY": "figd_xxxxx" }
}
```

---

## 4. lark-mcp — 飞书/Lark 集成（中科创达）

| 项目 | 说明 |
|------|------|
| **npm** | [@larksuiteoapi/lark-mcp](https://www.npmjs.com/package/@larksuiteoapi/lark-mcp) |
| **功能** | 通过 AI 操作飞书：发消息、管理文档/多维表格、搜索 Wiki、管理群组和联系人 |
| **认证** | App ID + App Secret + OAuth |
| **企业** | 中科创达（Thundersoft） |

```json
"lark-mcp": {
  "command": "/home/tsdl/.nvm/versions/node/v24.13.0/bin/node",
  "args": [
    "/home/tsdl/.nvm/versions/node/v24.13.0/lib/node_modules/@larksuiteoapi/lark-mcp/dist/index.js",
    "mcp", "-a", "cli_a9283b82fbf9dcc7", "-s", "iuU6m7zJWVCcbhzGg7tW8GIvqjFOreqZ", "--oauth"
  ]
}
```

> **注意**：使用 NVM 安装的 Node.js 完整路径启动，避免 Cursor 找不到正确的 Node 版本。

### 主要工具（19 个）

多维表格、文档、权限、消息、群组、联系人、Wiki 等全方位飞书操作。

---

## 5. playwright — 浏览器自动化

| 项目 | 说明 |
|------|------|
| **npm** | [@playwright/mcp](https://www.npmjs.com/package/@playwright/mcp) |
| **GitHub** | [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp) |
| **功能** | AI 控制浏览器：导航、点击、填表、截图、执行 JS、文件上传等 |

```json
"playwright": {
  "command": "npx",
  "args": ["@playwright/mcp@latest"]
}
```

### 主要工具（20+ 个）

导航、交互、查看、执行、等待、窗口管理等全方位浏览器自动化。

---

## 6. n8n-mcp — n8n 工作流文档

| 项目 | 说明 |
|------|------|
| **npm** | [n8n-mcp](https://www.npmjs.com/package/n8n-mcp) |
| **功能** | 查询 n8n 节点文档、验证工作流配置、搜索模板 |

### 主要工具（7 个）

`search_nodes` / `get_node` / `validate_node` / `search_templates` / `get_template` / `validate_workflow` / `tools_documentation`

---

## 7. Pdf Reader Mcp — PDF 读取

```json
"Pdf Reader Mcp": {
  "command": "npx",
  "type": "stdio",
  "args": ["-y", "@sylphx/pdf-reader-mcp@latest"]
}
```

---

## 8. interactive-feedback — Qt 交互式反馈

| 项目 | 说明 |
|------|------|
| **GitHub** | [rooney2020/qt-interactive-feedback-mcp](https://github.com/rooney2020/qt-interactive-feedback-mcp) |
| **功能** | 基于 PySide6 的原生 Qt 交互式反馈工具，支持多标签页、Markdown 渲染、中文输入 |
| **运行时** | Python 3.10+（uv 管理） |
| **本地路径** | `~/.cursor/Interactive-Feedback-MCP/` |

### 配置

```json
"interactive-feedback": {
  "command": "uv",
  "args": [
    "--directory",
    "/home/tsdl/.cursor/Interactive-Feedback-MCP",
    "run",
    "server.py"
  ],
  "timeout": 43200,
  "autoApprove": ["interactive_feedback"]
}
```

### 工具列表（1 个）

| 工具 | 说明 |
|------|------|
| `interactive_feedback` | 弹出 Qt 原生窗口收集用户反馈，支持文本输入和 Markdown 预览 |

### 特点

- 原生 Qt (PySide6) 界面，无需浏览器
- 多标签页管理（tab_id / tab_title）
- Markdown 渲染预览
- 中文输入法支持（ibus/fcitx）
- 心跳检测 + 超时重连
- 12 小时超长超时

---

## 9. openspec — 规范变更管理

```json
"openspec": {
  "command": "uvx",
  "args": ["openspec-mcp"],
  "env": { "OPENSPEC_DEBUG": "false" }
}
```

---

## 10. cursor-mcp-installer — MCP 安装器

```json
"cursor-mcp-installer": {
  "command": "npx",
  "type": "stdio",
  "args": ["cursor-mcp-installer-free@0.1.3", "index.mjs"]
}
```

---

## 11. context7 — 实时代码文档

| 项目 | 说明 |
|------|------|
| **GitHub** | [upstash/context7](https://github.com/upstash/context7)（⭐ 45.3k） |
| **功能** | 为 AI 提供最新的、版本特定的库/框架文档和代码示例 |

```json
"context7": {
  "url": "https://mcp.context7.com/mcp"
}
```

---

## 12. github — GitHub 集成

| 项目 | 说明 |
|------|------|
| **npm** | [@modelcontextprotocol/server-github](https://www.npmjs.com/package/@modelcontextprotocol/server-github) |
| **功能** | 通过 AI 全面操作 GitHub：仓库管理、Issue、PR、代码搜索、分支管理等 |

```json
"github": {
  "command": "npx",
  "args": ["-y", "@modelcontextprotocol/server-github"],
  "env": { "GITHUB_PERSONAL_ACCESS_TOKEN": "ghp_xxxxxxxx" }
}
```

### 全部工具（26 个）

仓库与文件操作、6个）、Issue 管理（5个）、PR 管理（8个）、搜索ﾈ4个）、分支和提交（3个）。

---

## 13. figma-remote — Figma 官方远程 MCP

| 项目 | 说明 |
|------|------|
| **官方文档** | [Figma MCP Server Guide](https://help.figma.com/hc/en-us/articles/32132100833559) |
| **功能** | Figma 官方托管的远程 MCP 服务，从设计稿生成代码、提取设计上下文 |

```json
"figma-remote": {
  "url": "https://mcp.figma.com/mcp"
}
```

---

## 14. android-mcp — Android 设备控制

| 项目 | 说明 |
|------|------|
| **GitHub** | [CursorTouch/Android-MCP](https://github.com/CursorTouch/Android-MCP)（420+ stars） |
| **功能** | 通过 ADB + uiautomator2 控制 Android 设备，支持点击、滑动、输入、截图、多设备切换等 |
| **运行时** | Python 3.13+ (uv) |
| **传输方式** | STDIO（FastMCP 2.14.0） |
| **前置依赖** | ADB + Android 10+ 设备或模拟器 |
| **本地源码** | `06.CursorMCPProject/android-mcp/`（从 GitHub 克隆，支持 `--device` 参数） |

### 安装方案

```bash
# 从 GitHub 克隆到本地（已完成）
cd 06.CursorMCPProject
git clone https://github.com/CursorTouch/Android-MCP.git android-mcp

# 安装依赖
cd android-mcp && uv sync

# 测试启动
uv run android-mcp --device <设备序列号>
```

### 配置

```json
"android-mcp": {
  "command": "uv",
  "args": [
    "--directory",
    "/home/tsdl/SSD/CursorProject/CursorBase/06.CursorMCPProject/android-mcp",
    "run",
    "android-mcp",
    "--device",
    "HQ64CD099E"
  ]
}
```

切换设备时修改 `--device` 后的序列号即可。省略 `--device` 参数时，若只有一台设备会自动连接。

### 工具列表（12 个）

| 工具 | 说明 |
|------|------|
| `ListDevices` | 列出所有已连接的 ADB 设备 |
| `ConnectDevice` | 按序列号连接指定设备 |
| `Snapshot` | 获取设备 UI 层级树，可选截图（支持标注/原图） |
| `Click` | 点击屏幕坐标 |
| `LongClick` | 长按屏幕坐标 |
| `Type` | 在指定位置输入文本 |
| `Swipe` | 从一点滑动到另一点 |
| `Drag` | 拖拽操作 |
| `Press` | 按键（返回、Home、音量等） |
| `Wait` | 暂停等待指定时间 |
| `Notification` | 打开通知栏 |

### 多设备说明

当前连接了 3 台设备：`DA27776A`、`E261001830`、`HQ64CD099E`。
默认连接 `HQ64CD099E`，也可通过 `ListDevices` + `ConnectDevice` 工具在运行时切换。

### 使用示例

在 Cursor Agent 对话中：

> 打开设置应用，截图给我看当前 Android 版本

---

## 15. sequential-thinking — 结构化逐步推理

| 项目 | 说明 |
|------|------|
| **npm** | [@modelcontextprotocol/server-sequential-thinking](https://www.npmjs.com/package/@modelcontextprotocol/server-sequential-thinking) |
| **GitHub** | [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers/tree/main/src/sequentialthinking) |
| **功能** | 结构化逐步推理：将复杂问题分解为可管理的步骤，支持修正、分支和动态调整 |
| **来源** | Anthropic 官方 |

### 配置

```json
"sequential-thinking": {
  "command": "npx",
  "args": ["-y", "@modelcontextprotocol/server-sequential-thinking"]
}
```

### 工具列表（1 个）

| 工具 | 说明 |
|------|------|
| `sequential_thinking` | 逐步思考工具：分解问题、修正推理、分支探索替代路径、动态调整步骤数 |

### 适用场景

- **规划**：需要制定实施计划的任务
- **分析**：需要中途修正方向的分析工作
- **复杂问题**：全貌不明确、需要逐步探索的问题
- **设计决策**：需要权衡多种方案的架构设计

### 使用方式

在 Cursor Agent 对话中，AI 会自动使用此工具进行结构化思考。也可以在提示词中明确要求：

> 请使用 sequential thinking 帮我分析这个系统的架构设计方案

---

## 16. memory — 持久化记忆

| 项目 | 说明 |
|------|------|
| **npm** | [@modelcontextprotocol/server-memory](https://www.npmjs.com/package/@modelcontextprotocol/server-memory) |
| **GitHub** | [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers/tree/main/src/memory) |
| **功能** | 基于知识图谱的持久化记忆系统，跨对话保存实体、关系和观察 |
| **来源** | Anthropic 官方 |

### 配置

```json
"memory": {
  "command": "npx",
  "args": ["-y", "@modelcontextprotocol/server-memory"]
}
```

### 工具列表（8 个）

| 工具 | 说明 |
|------|------|
| `create_entities` | 创建实体节点 |
| `delete_entities` | 删除实体节点 |
| `create_relations` | 创建关系边 |
| `delete_relations` | 删除关系边 |
| `add_observations` | 添加观察记录 |
| `delete_observations` | 删除观察记录 |
| `search_nodes` | 搜索知识图谱 |
| `read_graph` | 读取完整图谱 |

### 使用方式

```
> 记住我的项目使用 Python 3.12 和 FastAPI 框架
> 回忆一下我之前告诉你的项目技术栈
```

---

## 17. fetch — 网页内容获取

| 项目 | 说明 |
|------|------|
| **PyPI** | [mcp-server-fetch](https://pypi.org/project/mcp-server-fetch/) |
| **GitHub** | [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch) |
| **功能** | 获取网页内容并转换为 Markdown，帮助 AI 访问和处理网页信息 |
| **来源** | Anthropic 官方 |

### 配置

```json
"fetch": {
  "command": "uvx",
  "args": ["mcp-server-fetch"]
}
```

### 工具列表（1 个）

| 工具 | 说明 |
|------|------|
| `fetch` | 获取 URL 内容，转换为 Markdown/JSON/纯文本 |

### 特点

- 遵循 `robots.txt` 规则
- 自动 HTML 转 Markdown
- 支持自定义 User-Agent
- 可配置最大内容长度

---

## 18. exa — AI 智能搜索

| 项目 | 说明 |
|------|------|
| **npm** | [exa-mcp-server](https://www.npmjs.com/package/exa-mcp-server) |
| **GitHub** | [exa-labs/exa-mcp-server](https://github.com/exa-labs/exa-mcp-server) |
| **功能** | Exa AI 智能搜索引擎，支持网页搜索、代码搜索、公司研究、人物搜索 |
| **来源** | [Exa AI](https://exa.ai/) |

### 配置

```json
"exa": {
  "command": "npx",
  "args": ["-y", "exa-mcp-server"],
  "env": {
    "EXA_API_KEY": "your-api-key"
  }
}
```

### 工具列表

| 工具 | 说明 |
|------|------|
| `web_search` | 网页搜索 |
| `code_search` | 代码搜索 |
| `company_research` | 公司信息搜索 |
| `people_search` | 人物搜索 |
| `crawl` | 网页爬取 |

### API Key 获取

在 [Exa Dashboard](https://dashboard.exa.ai/api-keys) 注册并获取 API Key。

---

## 通用维护指南

### 配置文件位置

```
~/.cursor/mcp.json
```

### 各服务运行环境汇总

| MCP 服务 | 运行时 | 启动方式 | 需要外部连接 |
|----------|--------|----------|-------------|
| drawio | Node.js v24 (NVM) | 全局安装 + 完整路径 | 浏览器扩展 (端口 3334) |
| TalkToFigma | Bun v1.3.8+ | bunx + 本地 WebSocket 服务 | WebSocket (端口 3055) + Figma 插件 |
| figma | Node.js | npx | Figma API (Token) |
| lark-mcp | Node.js v24 (NVM) | 全局安装 + 完整路径 | 飞书 API (OAuth) |
| playwright | Node.js | npx | 自带浏览器 |
| n8n-mcp | Node.js v24 (NVM) | 全局安装 + 完整路径 | 无（离线文档） |
| Pdf Reader Mcp | Node.js | npx | 无 |
| interactive-feedback | Python (uv) | uv run | 无（本地 Qt 窗口） |
| openspec | Python (uvx) | uvx | 无 |
| cursor-mcp-installer | Node.js | npx | npm 仓库 |
| context7 | 无（远程服务） | HTTP URL 直连 | context7.com 云端 |
| github | Node.js | npx | GitHub API (Token) |
| figma-remote | 无（远程服务） | HTTP URL 直连 | mcp.figma.com（OAuth 认证） |
| android-mcp | Python 3.13+ (uv) | uv run（本地克隆） | ADB + Android 10+ |
| sequential-thinking | Node.js | npx | 无（本地推理） |
| memory | Node.js | npx | 无（本地知识图谱） |
| fetch | Python (uvx) | uvx | 互联网（获取网页） |
| exa | Node.js | npx | Exa AI API (API Key) |
| local-rag | Node.js | npx | 无（本地语义搜索） |

---

## 19. MCP Local RAG（本地 RAG 语义搜索）

**用途**：为 Cursor 提供本地代码和文档的语义搜索 + 关键词混合检索能力。

**安装方式**：npx 一键启动（零 Docker、零配置）

**配置**（`~/.cursor/mcp.json`）：

```json
"local-rag": {
  "command": "npx",
  "args": ["-y", "mcp-local-rag"],
  "env": {
    "BASE_DIR": "/home/tsdl/SSD/CursorProject"
  }
}
```

**提供的工具**：

| 工具 | 说明 |
|------|------|
| `ingest_file` | 索引单个文件 |
| `ingest_data` | 索引文本数据 |
| `query_documents` | 语义 + 关键词混合搜索 |
| `list_files` | 列出已索引文件 |
| `delete_file` | 删除索引 |
| `status` | 查看索引状态 |

**特性**：
- 语义搜索 + 关键词增强（精确匹配技术术语如 `useEffect`、错误码）
- 智能语义分块（按嵌入相似度而非固定字符数）
- 完全本地运行，零外部 API 调用
- 内置 all-MiniLM-L6-v2 嵌入模型

### 常见问题排查

#### 1. MCP 显示红色点（Error）

**关键经验**：系统自带 `/usr/bin/node` 可能太旧，Cursor 启动 MCP 子进程时不加载 NVM 环境，所以必须在 `mcp.json` 中使用 NVM node 的**完整路径**。

#### 2. npx 缓存损坏

```bash
rm -rf ~/.npm/_npx/*
```

#### 3. 更新 MCP 服务

| 安装方式 | 更新命令 |
|----------|----------|
| `npx xxx@latest` | 自动使用最新版（清理缓存：`npx clear-npx-cache`） |
| npm 全局安装 | `npm update -g drawio-mcp-server @larksuiteoapi/lark-mcp n8n-mcp` |
| uvx | `uvx openspec-mcp`（自动拉取最新） |
| uv run（本地克隆） | `cd <项目目录> && git pull && uv sync --upgrade` |
| 远程 URL | 无需更新，始终连接远程最新版 |

### 当前版本（2026-03-17 更新）

| MCP 服务 | 版本 | 更新方式 |
|----------|------|----------|
| drawio-mcp-server | 1.8.0 | npm 全局 |
| @larksuiteoapi/lark-mcp | 0.5.1 | npm 全局 |
| n8n-mcp | 2.37.3 | npm 全局 |
| interactive-feedback | git latest | uv run（本地克隆） |
| android-mcp | git latest (FastMCP 3.1.1) | uv run（本地克隆） |
| @playwright/mcp | 0.0.68 | npx @latest |
| figma-developer-mcp | 0.6.6 | npx @latest |
| cursor-mcp-installer-free | 0.1.3 | npx 固定版本 |
| @sylphx/pdf-reader-mcp | 2.3.0 | npx @latest |
| @modelcontextprotocol/server-github | 2025.4.8 | npx |
| @modelcontextprotocol/server-sequential-thinking | 2025.12.18 | npx |
| @modelcontextprotocol/server-memory | 2026.1.26 | npx |
| exa-mcp-server | 3.1.9 | npx |
| mcp-local-rag | 0.8.1 | npx |
| openspec-mcp | 0.2.0 | uvx |
| mcp-server-fetch | 2025.4.7 | uvx |
| context7 | 远程服务 | HTTP URL 直连 |
| figma-remote | 远程服务 | HTTP URL 直连 |


---

## 1M 上下文时代的 MCP/Agent 工作流优化（2026-03-15）

> 参考：[Claude 1M Context GA](https://claude.com/blog/1m-context-ga)

### 核心变化

Claude Opus 4.6 / Sonnet 4.6 的 1M 上下文窗口正式 GA，对 MCP 和 Agent 工作流带来以下影响：

| 变化 | 影响 |
|------|------|
| Compaction 减少 ~15% | Agent 长任务中保持更完整的工具调用历史 |
| 600 页 PDF/图片 | 单次请求可处理更多媒体文件 |
| 无长上下文溢价 | 大上下文请求成本不变 |

### Agent 工作流优化建议

#### 1. 减少 SubAgent 使用

1M 上下文下，主 Agent 可以在单个会话中完成更多工作，减少对 SubAgent 的依赖：

```
传统做法: 主 Agent → 启动 SubAgent 搜索 → 返回结果 → 主 Agent 继续
1M 做法:  主 Agent 直接搜索 + 分析 + 修复，全部在一个上下文中
```

**适用场景**：代码搜索、文件分析、多步骤调试

**仍需 SubAgent 的场景**：并行执行独立任务、浏览器自动化、长时间运行的命令

#### 2. MCP 工具调用链优化

1M 上下文可以保持完整的工具调用 trace，减少重复调用：

| MCP 服务 | 优化建议 |
|----------|----------|
| **Local RAG** | 小文档可直接加载到上下文，减少 RAG 检索 |
| **Memory MCP** | 单次会话内不需要频繁存取，跨会话仍需要 |
| **Lark MCP** | 一次性获取更多飞书文档内容 |
| **Playwright** | 浏览器截图可一次提交更多（600 张限制） |
| **Feedback MCP** | 长任务中减少中间确认，利用大上下文保持任务连贯性 |

#### 3. 长任务策略

```
短任务（< 50K token）: 正常使用，任何模型
中任务（50K-200K token）: 使用 Opus/Sonnet 4.6，注意 token 效率
长任务（200K-1M token）: 使用 Opus 4.6，减少不必要的上下文加载
```

#### 4. Token 效率监控

使用 **cursor-usage** 插件实时监控 token 消耗：
- 状态栏显示每次请求的 token 消耗
- 识别空请求（token=0 的浪费请求）
- 跟踪周期内总消耗，优化使用效率

---

## 备选 MCP（未安装，仅记录）

### Windows-MCP — Windows 桌面自动化

| 项目 | 说明 |
|------|------|
| **GitHub** | [CursorTouch/Windows-MCP](https://github.com/CursorTouch/Windows-MCP)（4.7k stars） |
| **PyPI** | `windows-mcp`（v0.6.9） |
| **作者** | CursorTouch（与 Android-MCP 同一团队） |
| **功能** | 通过 MCP 让 AI Agent 控制 Windows 操作系统：文件导航、应用控制、UI 交互、QA 测试等 |
| **运行时** | Python 3.13+ (uv/uvx) |
| **传输方式** | STDIO / SSE / Streamable HTTP |
| **平台** | Windows 7 / 8 / 10 / 11 |
| **许可证** | MIT |

#### 安装方式

```json
"windows-mcp": {
  "command": "uvx",
  "args": ["windows-mcp"]
}
```

从源码安装：

```bash
git clone https://github.com/CursorTouch/Windows-MCP.git
cd Windows-MCP
```

```json
"windows-mcp": {
  "command": "uv",
  "args": ["--directory", "<path>", "run", "windows-mcp"]
}
```

#### 工具列表（16 个）

| 工具 | 说明 |
|------|------|
| `Click` | 点击屏幕坐标 |
| `Type` | 在元素上输入文本 |
| `Scroll` | 垂直/水平滚动 |
| `Move` | 移动鼠标或拖拽 |
| `Shortcut` | 按键盘快捷键（Ctrl+C、Alt+Tab 等） |
| `Wait` | 暂停指定时间 |
| `Screenshot` | 快速截图 + 光标位置 + 活动窗口信息 |
| `Snapshot` | 完整桌面状态捕获（含 UI 元素 ID、可滚动区域、DOM 模式） |
| `App` | 启动/调整/切换应用 |
| `Shell` | 执行 PowerShell 命令 |
| `Scrape` | 抓取网页内容 |
| `MultiSelect` | 多选文件/文件夹/复选框 |
| `MultiEdit` | 批量输入多个文本框 |
| `Clipboard` | 读写 Windows 剪贴板 |
| `Process` | 列出/终止进程 |
| `Notification` | 发送 Windows Toast 通知 |
| `Registry` | 读写 Windows 注册表 |

#### 特点

- 不依赖计算机视觉或特定微调模型，任何 LLM 均可使用
- 操作延迟 0.2~0.9 秒
- DOM 模式（`use_dom=True`）专注网页内容自动化
- 支持远程模式（通过 windowsmcp.io 连接云端 Windows VM）
- 支持多显示器（`display=[0]` / `display=[0,1]`）
- 2M+ 用户（Claude Desktop Extensions）

#### 备注

当前工作环境为 Linux，此 MCP 仅适用于 Windows。记录备用，如需在 Windows 机器上使用 Cursor 时可直接安装。与已安装的 `android-mcp` 来自同一团队（CursorTouch）。
