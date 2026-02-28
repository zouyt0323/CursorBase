# Cursor MCP 服务总览

> 本文整理了当前 Cursor 中已安装的全部 **15 个** MCP（Model Context Protocol）服务，包括安装方案、配置详情和使用方法。
>
> 配置文件路径：`~/.cursor/mcp.json`
>
> 最后更新：2026-02-28

---

## 目录

1. [drawio — Draw.io 图表控制](#1-drawio--drawio-图表控制)
2. [TalkToFigma — Figma 双向交互](#2-talktofigma--figma-双向交互)
3. [figma — Figma 设计数据读取](#3-figma--figma-设计数据读取)
4. [lark-mcp — 飞书/Lark 集成](#4-lark-mcp--飞书lark-集成)
5. [playwright — 浏览器自动化](#5-playwright--浏览器自动化)
6. [n8n-mcp — n8n 工作流文档](#6-n8n-mcp--n8n-工作流文档)
7. [Pdf Reader Mcp — PDF 读取](#7-pdf-reader-mcp--pdf-读取)
8. [interactive-feedback-mcp — 交互式反馈](#8-interactive-feedback-mcp--交互式反馈)
9. [openspec — 规范变更管理](#9-openspec--规范变更管理)
10. [cursor-mcp-installer — MCP 安装器](#10-cursor-mcp-installer--mcp-安装器)
11. [context7 — 实时代码文档](#11-context7--实时代码文档)
12. [github — GitHub 集成](#12-github--github-集成)
13. [figma-remote — Figma 官方远程 MCP](#13-figma-remote--figma-官方远程-mcp)
14. [lark-feedback — 飞书远程控制](#14-lark-feedback--飞书远程控制)
15. [android-mcp — Android 设备控制](#15-android-mcp--android-设备控制)
16. [通用维护指南](#通用维护指南)

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

### 主要工具（18 个）

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

## 4. lark-mcp — 飞书/Lark 集成

| 项目 | 说明 |
|------|------|
| **npm** | [@larksuiteoapi/lark-mcp](https://www.npmjs.com/package/@larksuiteoapi/lark-mcp) |
| **功能** | 通过 AI 操作飞书：发消息、管理文档/多维表格、搜索 Wiki、管理群组和联系人 |
| **认证** | App ID + App Secret + OAuth |

```json
"lark-mcp": {
  "command": "npx",
  "args": ["-y", "@larksuiteoapi/lark-mcp", "mcp", "-a", "cli_xxxxxxxx", "-s", "xxxxxxxx", "--oauth"]
}
```

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

## 8. interactive-feedback-mcp — 交互式反馈

| 项目 | 说明 |
|------|------|
| **GitHub** | [noopstudios/interactive-feedback-mcp](https://github.com/noopstudios/interactive-feedback-mcp) |
| **功能** | 在 AI 执行任务过程中向用户请求交互式反馈 |

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

## 14. lark-feedback — 飞书远程控制

| 项目 | 说明 |
|------|------|
| **功能** | 通过飞书手机端远程控制 Cursor IDE，实现移动办公 |
| **运行时** | Python 3.11+ (uv) |
| **传输方式** | STDIO |
| **源码位置** | `07.CursorLarkProject/lark-feedback-mcp/` |

### 安装方案

```bash
cp -r 07.CursorLarkProject/lark-feedback-mcp ~/lark-feedback-mcp
cd ~/lark-feedback-mcp && uv sync
uv run python setup.py   # 输入飞书邮箱，自动创建群聊和 config.json
```

### 配置

```json
"lark-feedback": {
  "command": "uv",
  "args": [
    "--directory",
    "/home/tsdl/lark-feedback-mcp",
    "run",
    "server.py"
  ],
  "timeout": 600,
  "autoApprove": [
    "send_to_lark",
    "wait_for_lark_input"
  ]
}
```

### 工具列表（2 个）

| 工具 | 说明 |
|------|------|
| `send_to_lark` | 向飞书群发送消息（汇报进度/结果） |
| `wait_for_lark_input` | 等待用户在飞书中回复指令 |

### 使用方式

在 Cursor 对话中输入「手机控制模式」启动，飞书手机端发送指令即可远程控制。

详见 [`07.CursorLarkProject/README.md`](../07.CursorLarkProject/README.md)。

---

## 15. android-mcp — Android 设备控制

| 项目 | 说明 |
|------|------|
| **GitHub** | [CursorTouch/Android-MCP](https://github.com/CursorTouch/Android-MCP)（420+ stars） |
| **功能** | 通过 ADB 和无障碍 API 控制 Android 设备，支持点击、滑动、输入、截图等 |
| **运行时** | Python 3.10+ (uvx) |
| **传输方式** | STDIO |
| **前置依赖** | ADB + Android 10+ 设备或模拟器 |

### 安装方案

```bash
# 确认 ADB 已安装
adb version

# 确认设备已连接
adb devices

# 无需手动安装，uvx 自动下载
uvx android-mcp --help
```

### 配置

```json
"android-mcp": {
  "command": "uvx",
  "args": [
    "android-mcp"
  ]
}
```

如使用模拟器，添加 `"--emulator"` 到 args。

### 工具列表（11 个）

| 工具 | 说明 |
|------|------|
| `State-Tool` | 获取设备状态和 UI 层级 |
| `Click-Tool` | 点击屏幕坐标 |
| `Long-Click-Tool` | 长按屏幕坐标 |
| `Type-Tool` | 在指定位置输入文本 |
| `Swipe-Tool` | 从一点滑动到另一点 |
| `Drag-Tool` | 拖拽操作 |
| `Press-Tool` | 按键（返回、音量等） |
| `Wait-Tool` | 暂停等待指定时间 |
| `Notification-Tool` | 读取设备通知 |
| `Shell-Tool` | 执行 adb shell 命令 |

### 使用示例

在 Cursor Agent 对话中：

> 打开设置应用，截图给我看当前 Android 版本

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
| lark-mcp | Node.js | npx | 飞书 API (OAuth) |
| playwright | Node.js | npx | 自带浏览器 |
| n8n-mcp | Node.js v24 (NVM) | 全局安装 + 完整路径 | 无（离线文档） |
| Pdf Reader Mcp | Node.js | npx | 无 |
| interactive-feedback-mcp | Python (uv) | uv run | 无 |
| openspec | Python (uvx) | uvx | 无 |
| cursor-mcp-installer | Node.js | npx | npm 仓库 |
| context7 | 无（远程服务） | HTTP URL 直连 | context7.com 云端 |
| github | Node.js | npx | GitHub API (Token) |
| figma-remote | 无（远程服务） | HTTP URL 直连 | mcp.figma.com（OAuth 认证） |
| lark-feedback | Python 3.11+ (uv) | uv run | 飞书 API (app_id + chat_id) |
| android-mcp | Python 3.10+ (uvx) | uvx | ADB + Android 10+ |

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
| `npx xxx@latest` | 自动使用最新版 |
| 全局安装 | `npm install -g drawio-mcp-server n8n-mcp` |
| uvx | `uvx openspec-mcp`（自动拉取最新） |
| 远程 URL | 无需更新，始终连接远程最新版 |