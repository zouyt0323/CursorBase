# MCP 收集网站与热门服务汇总

> 整理自各大 MCP 收集平台的数据，包含主要收集网站、使用率最高的 MCP 服务排行以及推荐安装的服务。
>
> 最后更新：2026-02-26

---

## 一、MCP 收集网站一览

目前主要的 MCP 服务收集/目录网站有以下几类：

### 1. 官方平台

| 网站 | 地址 | 说明 |
|------|------|------|
| **MCP Official Registry** | [registry.modelcontextprotocol.io](https://registry.modelcontextprotocol.io/) | Anthropic 官方 MCP 注册中心 |
| **MCP Reference Servers** | [github.com/modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) | 官方参考实现仓库 |

### 2. 社区收集平台（网站类）

| 网站 | 地址 | 收录数量 | 特点 |
|------|------|---------|------|
| **MCP.so** | [mcp.so](https://mcp.so/) | 17,500+ | 最大的 MCP 市场，有调用排行榜 |
| **Smithery.ai** | [smithery.ai/servers](https://smithery.ai/servers) | 3,500+ | 提供安装量统计 |
| **PulseMCP** | [pulsemcp.com/servers](https://www.pulsemcp.com/servers) | 6,000~7,900 | 每日更新，下载量估算，过滤低质量实现 |
| **Glama.ai** | [glama.ai/mcp/servers](https://glama.ai/mcp/servers) | 5,800+ | awesome-mcp-servers 配套网站 |
| **MCP Evals** | [mcpevals.io](https://www.mcpevals.io/) | — | MCP 质量评估与统计分析 |
| **MCP Server List** | [mcp-server-list.com](https://mcp-server-list.com/) | 650+ | 按类别分类 |
| **MCPServers.org** | [mcpservers.org](https://mcpservers.org/) | 大量 | 精选和官方分类 |
| **MCP Server Hub** | [mcpserverhub.net](https://mcpserverhub.net/zh/servers) | 大量 | 支持中文界面 |
| **MCPServer.space** | [mcpserver.space](https://mcpserver.space/) | 大量 | MCP 服务发现平台 |
| **MCP AIBase** | [mcp.aibase.com](https://mcp.aibase.com/) | 大量 | 中文 MCP 服务目录 |

### 3. GitHub 收集仓库

| 仓库 | Stars | 说明 |
|------|-------|------|
| **[punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)** | ⭐ 80,480 | 最权威的社区 MCP 收集仓库 |
| **[modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)** | ⭐ 大量 | 官方参考实现 |
| **[appcypher/awesome-mcp-servers](https://github.com/appcypher/awesome-mcp-servers)** | ⭐ 5,000+ | 另一个社区收集 |
| **[tolkonepiu/best-of-mcp-servers](https://github.com/tolkonepiu/best-of-mcp-servers)** | — | 410 个 MCP 服务器，每周自动更新质量排名 |

---

## 二、使用率最高的 MCP 服务排行

### TOP 20（按下载量/热度综合排序）

| 排名 | MCP 服务 | 类别 | 热度来源 | 说明 |
|------|---------|------|---------|------|
| 1 | **GitHub** | 开发工具 | PulseMCP 889k 下载 | GitHub 仓库、Issue、PR |
| 2 | **Fetch** | 网页获取 | PulseMCP 801k 下载 | Anthropic 官方，HTTP 获取网页 |
| 3 | **Context7** | 代码文档 | PulseMCP 590k 下载 / ⭐45.3k+ | 实时拉取最新库文档 |
| 4 | **Playwright** | 浏览器自动化 | PulseMCP 590k 下载 | Microsoft，AI 控制浏览器 |
| 5 | **Filesystem** | 文件系统 | PulseMCP 575k 下载 | Anthropic 官方，安全文件操作 |
| 6 | **Exa Search** | 搜索 | Smithery 10.66M 使用 | AI 智能搜索 |
| 7 | **Supabase** | 数据库 | Smithery 7.95k+ | 数据库管理 |
| 8 | **Figma (remote)** | 设计工具 | 全平台热门 | Figma 官方远程 MCP |
| 9 | **Notion** | 生产力 | PulseMCP 热门 | 搜索、创建 Notion 页面 |
| 10 | **Slack** | 通讯 | PulseMCP 热门 | 消息收发 |
| 11 | **Sequential Thinking** | 推理增强 | 官方实现 | 结构化思考 |
| 12 | **Memory** | 记忆 | 官方实现 | 持久化记忆 |
| 13 | **Obsidian** | 知识管理 | PulseMCP 热门 | 笔记库读写 |
| 14 | **Firecrawl** | 网页抓取 | 多平台推荐 | 深度抓取 |
| 15 | **Google Calendar** | 生产力 | Smithery 4.93k | 日程管理 |
| 16 | **Postgres** | 数据库 | PulseMCP 热门 | PostgreSQL 操作 |
| 17 | **Git** | 开发工具 | 官方实现 | Git 操作 |
| 18 | **Perplexity Ask** | 搜索 | PulseMCP 热门 | 实时网页搜索 |
| 19 | **Jira** | 项目管理 | PulseMCP 热门 | Issue 和项目管理 |
| 20 | **Linkup** | 搜索 | Smithery 16.45k | 带引用搜索 |

> **数据来源说明**：PulseMCP 下载量为综合估算（合并 npm 注册、社交信号、网站流量等多源数据），反映生态系统整体使用情况。

---

## 三、推荐新增安装的 MCP 服务

### 强烈推荐

| MCP 服务 | 安装方式 | 推荐理由 |
|---------|---------|----------|
| **Sequential Thinking** | npx | 官方推理增强 |
| **Memory** | npx | 跨会话记忆 |
| **Filesystem** | npx | 安全文件操作 |
| **Exa Search** | npx | 最热门搜索 MCP |
| **Fetch** | uvx | 轻量网页获取 |

### 按需推荐

| MCP 服务 | 适用场景 |
|---------|----------|
| **Notion** | 使用 Notion 管理知识/项目 |
| **Obsidian** | 使用 Obsidian 做笔记 |
| **Supabase** | 使用 Supabase 做后端 |
| **Google Calendar** | AI 管理日程 |
| **Slack** | 使用 Slack 团队沟通 |
| **Perplexity Ask** | 高质量实时搜索 |

---

## 四、MCP 生态数据概览

| 指标 | 数据 |
|------|------|
| PulseMCP 收录（每日更新，过滤低质量） | **6,000~7,900** |
| MCP.so 收录（含全部） | **17,500+** |
| Glama.ai 收录 | **5,800+** |
| MCP 客户端应用 | **300+**（含 Claude Desktop、VS Code、Cursor 等） |
| 主要开发语言 | Python > TypeScript > JavaScript |
| 头部 MCP 服务下载量 | GitHub 889k / Fetch 801k / Context7 590k / Playwright 590k |
| MCP 协议发布时间 | 2024 年 11 月（Anthropic 发布） |
| 最大社区收集仓库 | punkpeye/awesome-mcp-servers（⭐80,480+） |

---

## 五、快速导航

| 需求 | 推荐网站 |
|------|----------|
| 查找特定功能的 MCP | [mcp.so](https://mcp.so/) |
| 查看安装量/使用率排名 | [smithery.ai](https://smithery.ai/servers) |
| 查看综合热度排名 | [pulsemcp.com](https://www.pulsemcp.com/servers) |
| 浏览精选高质量 MCP | [mcpservers.org](https://mcpservers.org/) |
| 查看官方/认证 MCP | [registry.modelcontextprotocol.io](https://registry.modelcontextprotocol.io/) |
| 中文界面浏览 | [mcpserverhub.net/zh](https://mcpserverhub.net/zh/servers) |
| GitHub 精选列表 | [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) |