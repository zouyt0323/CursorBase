# vm0-skills 中文说明文档

本目录包含对 **vm0-skills** 技能集合的中文详细分析。
数据来源：[https://github.com/vm0-ai/vm0-skills](https://github.com/vm0-ai/vm0-skills)

**未对 `skills` 文件夹做任何修改、新增或删除。**

## 技能集概要

| 项目 | 信息 |
|------|------|
| **名称** | vm0-skills |
| **中文名** | VM0 SaaS API 技能集 |
| **技能总数** | **75 个** |
| **设计理念** | 无 MCP、无 SDK、无 CLI，只用 curl |
| **许可证** | 开源 |
| **GitHub** | [vm0-ai/vm0-skills](https://github.com/vm0-ai/vm0-skills) |
| **规范** | 遵循 [Agent Skills 规范](https://agentskills.io/specification) |
| **Cursor 兼容** | 是（复制 SKILL.md 到 .cursor/skills/） |

## 核心原则

1. **专注 SaaS API 集成**：提供常见 SaaS API 的实用集成方案
2. **纯净零脚本**：代码简洁清晰，无冗余脚本，AI Agent 易于学习
3. **安全优先**：所有 API 调用记录在 SKILL.md 中，便于安全审计

## 全部 75 个技能分类

### 设计与创意（1 个）

| 技能 | 中文名 | 说明 |
|------|--------|------|
| **figma** | Figma API | Figma REST API 集成，读取设计文件、导出图片、管理评论、获取组件信息 |

### 开发与代码平台（7 个）

| 技能 | 中文名 | 说明 |
|------|--------|------|
| github | GitHub | GitHub API 集成 |
| github-copilot | GitHub Copilot | Copilot 技能 |
| gitlab | GitLab | GitLab API 集成 |
| supabase | Supabase | Supabase 数据库/认证 |
| sentry | Sentry | 错误监控与追踪 |
| qdrant | Qdrant | 向量数据库 |
| minio | MinIO | 对象存储 |

### 通信与消息（10 个）

| 技能 | 中文名 | 说明 |
|------|--------|------|
| slack | Slack | Slack API |
| slack-webhook | Slack Webhook | Slack 消息推送 |
| discord | Discord | Discord API |
| discord-webhook | Discord Webhook | Discord 消息推送 |
| gmail | Gmail | Gmail 邮件 |
| resend | Resend | 邮件发送 |
| zeptomail | ZeptoMail | 邮件服务 |
| agentmail | AgentMail | AI Agent 邮件 |
| mailsac | Mailsac | 临时邮箱 |
| pushinator | Pushinator | 推送通知 |

### 项目管理与协作（9 个）

| 技能 | 中文名 | 说明 |
|------|--------|------|
| notion | Notion | Notion API |
| jira | Jira | 项目管理 |
| linear | Linear | 任务追踪 |
| monday | Monday.com | 工作管理 |
| lark | Lark/飞书 | 飞书 API |
| intercom | Intercom | 客户通信 |
| chatwoot | Chatwoot | 客服平台 |
| zendesk | Zendesk | 客户支持 |
| twenty | Twenty | 开源 CRM |

### AI 与机器学习（5 个）

| 技能 | 中文名 | 说明 |
|------|--------|------|
| openai | OpenAI | OpenAI API |
| deepseek | DeepSeek | DeepSeek AI |
| perplexity | Perplexity | 搜索引擎 AI |
| minimax | MiniMax | MiniMax AI |
| fal.ai | fal.ai | AI 推理 |

### 媒体与内容（6 个）

| 技能 | 中文名 | 说明 |
|------|--------|------|
| youtube | YouTube | YouTube API |
| elevenlabs | ElevenLabs | AI 语音合成 |
| runway | Runway | AI 视频生成 |
| cloudinary | Cloudinary | 图片/视频管理 |
| htmlcsstoimage | HTML/CSS to Image | 网页转图片 |
| imgur | Imgur | 图片托管 |

### 搜索与数据（7 个）

| 技能 | 中文名 | 说明 |
|------|--------|------|
| brave-search | Brave 搜索 | 隐私搜索 |
| serpapi | SerpAPI | 搜索结果 API |
| tavily | Tavily | AI 搜索 |
| firecrawl | Firecrawl | 网页抓取 |
| scrapeninja | ScrapeNinja | 网页抓取 |
| bright-data | Bright Data | 数据采集 |
| supadata | Supadata | 数据服务 |

### 自动化与工作流（5 个）

| 技能 | 中文名 | 说明 |
|------|--------|------|
| apify | Apify | Web 自动化 |
| browserbase | Browserbase | 无头浏览器 |
| browserless | Browserless | 浏览器自动化 |
| cronlytic | Cronlytic | 定时任务 |
| workflow-migration | 工作流迁移 | 迁移工具 |

### 社交与内容发布（5 个）

| 技能 | 中文名 | 说明 |
|------|--------|------|
| instagram | Instagram | Instagram API |
| dev.to | Dev.to | 技术博客 |
| hackernews | Hacker News | HN API |
| qiita | Qiita | 日本技术博客 |
| podchaser | Podchaser | 播客平台 |

### 营销与 CRM（6 个）

| 技能 | 中文名 | 说明 |
|------|--------|------|
| streak | Streak | CRM（Gmail） |
| kommo | Kommo | CRM 平台 |
| instantly | Instantly | 邮件营销 |
| reportei | Reportei | 营销报表 |
| shortio | Short.io | 短链接 |
| bitrix | Bitrix24 | 企业通信 |

### 文档与电子签名（4 个）

| 技能 | 中文名 | 说明 |
|------|--------|------|
| pdf4me | PDF4me | PDF 处理 |
| pdfco | PDF.co | PDF API |
| pdforge | PDForge | PDF 生成 |
| zapsign | ZapSign | 电子签名 |

### 基础设施（3 个）

| 技能 | 中文名 | 说明 |
|------|--------|------|
| cloudflare-tunnel | Cloudflare Tunnel | 内网穿透 |
| plausible | Plausible | 隐私分析 |
| pikvm | PiKVM | 远程 KVM |

### 数据表格（2 个）

| 技能 | 中文名 | 说明 |
|------|--------|------|
| google-sheets | Google Sheets | 表格 API |
| axiom | Axiom | 日志分析 |

### RSS 与订阅（1 个）

| 技能 | 中文名 | 说明 |
|------|--------|------|
| rss-fetch | RSS 抓取 | RSS 订阅 |

### 金融与支付（1 个）

| 技能 | 中文名 | 说明 |
|------|--------|------|
| mercury | Mercury 银行 | 银行账户管理、转账、交易查询 |

### VM0 平台（3 个）

| 技能 | 中文名 | 说明 |
|------|--------|------|
| vm0 | VM0 平台 | VM0 核心 API |
| vm0-agent | VM0 Agent | Agent 管理 |
| vm0-cli | VM0 CLI | 命令行工具 |

## Figma 技能详情

vm0-skills 中的 `figma` 技能是基于 **Figma REST API** 的纯 curl 方案：

### 功能

- 读取设计文件并提取组件、样式、框架
- 导出图片（PNG/JPG/SVG/PDF，可调缩放）
- 获取文件版本历史
- 管理评论（读取/发布/删除）
- 列出项目和文件
- 访问设计令牌和样式
- 获取组件信息和组件集
- 团队成员管理

### 使用方式

```bash
# 设置 API Token
export FIGMA_API_TOKEN="figd_..."

# 获取文件信息
curl -s "https://api.figma.com/v1/files/<file-key>" -H "X-Figma-Token: $FIGMA_API_TOKEN"

# 导出节点为图片
curl -s "https://api.figma.com/v1/images/<file-key>?ids=<node-ids>&format=png&scale=2" -H "X-Figma-Token: $FIGMA_API_TOKEN"
```

### 与其他 Figma 方案的对比

| 特性 | vm0-skills/figma | Figma 官方 MCP | cursor-talk-to-figma-mcp |
|------|-----------------|---------------|-------------------------|
| 方式 | REST API（curl） | MCP Server | WebSocket + MCP |
| 读取设计 | 是 | 是 | 是 |
| 修改设计 | **否** | 否 | **是** |
| 导出图片 | 是 | 是 | 否 |
| 评论管理 | 是（可读写） | 否 | 否 |
| 依赖 | 仅 curl | Figma 桌面版 v127+ | npm + Figma 插件 |
| 适合场景 | 信息读取、自动化报告 | 设计稿转代码 | 双向操作设计 |

## 安装到 Cursor

```bash
# 安装 Figma 技能
mkdir -p ~/.cursor/skills/figma
cp skills/vm0-skills/figma/SKILL.md ~/.cursor/skills/figma/

# 安装其他感兴趣的技能
cp -r skills/vm0-skills/notion ~/.cursor/skills/
cp -r skills/vm0-skills/slack ~/.cursor/skills/
cp -r skills/vm0-skills/github ~/.cursor/skills/
```

---

*整理时间：2026-02-06*
*技能总数：75 个*
