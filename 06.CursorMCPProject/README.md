# Cursor MCP 服务配置指南

> 本仓库整理了 Cursor IDE 中 MCP（Model Context Protocol）服务的完整配置方案、使用文档、热门服务排行和推荐安装指南。
>
> 最后更新：2026-02-28

## 仓库内容

| 文件 | 说明 |
|------|------|
| [Cursor-MCP服务总览.md](./Cursor-MCP服务总览.md) | 当前已安装的 **15 个** MCP 服务的详细文档（安装、配置、工具列表、使用示例、故障排查） |
| [MCP收集网站与热门服务.md](./MCP收集网站与热门服务.md) | **10 大** MCP 收集网站 + 使用率 **TOP 20** 热门服务排行 |
| [推荐MCP安装与使用指南.md](./推荐MCP安装与使用指南.md) | **7 个**推荐新增安装的 MCP 服务详细指南 |
| [interactive-feedback-mcp 中文支持](./interactive-feedback-mcp-chinese-support/) | interactive-feedback-mcp Linux 下中文输入支持改造方案 |

## 已安装的 MCP 服务（15 个）

| # | 服务 | 功能 | 来源 | 连接方式 |
|---|------|------|------|--------|
| 1 | drawio | Draw.io 图表控制 | 社区 | 本地 (Node.js) |
| 2 | TalkToFigma | Figma 双向交互 | 社区 | 本地 (Bun + WebSocket) |
| 3 | figma | Figma 设计数据读取 | 社区 | 本地 (npx + API Token) |
| 4 | lark-mcp | 飞书/Lark 集成 | 飞书官方 | 本地 (Node.js + OAuth) |
| 5 | playwright | 浏览器自动化 | Microsoft | 本地 (npx) |
| 6 | n8n-mcp | n8n 工作流文档 | 社区 | 本地 (Node.js) |
| 7 | Pdf Reader Mcp | PDF 读取 | 社区 | 本地 (npx) |
| 8 | interactive-feedback-mcp | 交互式反馈 | 社区 | 本地 (Python/uv) |
| 9 | openspec | 规范变更管理 | 社区 | 本地 (Python/uvx) |
| 10 | cursor-mcp-installer | MCP 安装器 | 社区 | 本地 (npx) |
| 11 | context7 | 实时代码文档 | Upstash | **远程** (HTTP URL) |
| 12 | github | GitHub 集成 | Anthropic 官方 | 本地 (npx + Token) |
| 13 | figma-remote | Figma 官方远程 MCP | Figma 官方 | **远程** (HTTP URL + OAuth) |
| 14 | **lark-feedback** | **飞书远程控制 Cursor** | **自研** | **本地 (Python/uv)** |
| 15 | **android-mcp** | **Android 设备控制** | **[CursorTouch](https://github.com/CursorTouch/Android-MCP)** | **本地 (Python/uvx)** |

## 热门 MCP 服务 TOP 5（按下载量）

| 排名 | 服务 | 下载量/热度 |
|------|------|------------|
| 1 | GitHub | PulseMCP 889k 下载 |
| 2 | Fetch | PulseMCP 801k 下载 |
| 3 | Context7 | PulseMCP 590k 下载 / ⭐45.3k+ |
| 4 | Playwright | PulseMCP 590k 下载 / Microsoft 官方 |
| 5 | Filesystem | PulseMCP 575k 下载 |

## MCP 收集网站

| 网站 | 收录量 |
|------|--------|
| [mcp.so](https://mcp.so/) | 17,500+ |
| [pulsemcp.com](https://www.pulsemcp.com/servers) | 6,000~7,900 |
| [glama.ai](https://glama.ai/mcp/servers) | 5,800+ |
| [smithery.ai](https://smithery.ai/servers) | 3,500+ |
| [官方 Registry](https://registry.modelcontextprotocol.io/) | 官方认证 |
| [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | ⭐80,480+ |

## 配置文件

所有 MCP 服务的配置位于 `~/.cursor/mcp.json`。详见 [Cursor-MCP服务总览.md](./Cursor-MCP服务总览.md) 中的通用维护指南。

## License

MIT