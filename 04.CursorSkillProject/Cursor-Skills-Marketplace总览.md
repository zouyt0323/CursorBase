# Cursor Skills / Marketplace 总览

> 更新时间：2026-03-20
> 已安装 Skills 总数：170 个（已清理 21 个冗余/无关 Skills）
> - `~/.cursor/skills/`（手动安装）：91 个
> - `~/.cursor/skills-cursor/`（Marketplace/ECC）：79 个（原 100，删除 21）
>
> 已删除：autonomous-loops、continuous-learning(v1)、8 个行业特定（供应链/物流/零售/能源）、3 个 Perl、4 个 Django、4 个 Swift/iOS

---

## 与 ThunderSoft Android/嵌入式工作的相关性说明

- **高度相关**：Kotlin/Android/KMP、Compose、Clean Architecture、协程/Flow、测试、Docker/CI、安全审查、通用前端、API/部署、Python/脚本自动化、文档与沟通类技能
- **弱相关或易闲置**：纯 Spring/Java 企业后端、Django、Perl、Swift/iOS 全家桶、大量 SaaS 营销/CRO/付费广告、供应链/零售/能源等行业包、签证材料、X/公众号重度运营

---

## 冗余与重叠分析

| 关系 | 技能 | 建议 |
|------|------|------|
| SEO 主从 | `seo` 统筹多子技能，与 `seo-audit`、`seo-page` 等有包含关系 | 保持现状（设计如此） |
| 竞品页 | `seo-competitor-pages` vs `competitor-alternatives` | 题材重叠，粒度不同，可保留 |
| 验证闭环 | `verification-before-completion` vs `verification-loop` vs 各栈 `*-verification` | 保留 `verification-before-completion`（通用） |
| 自主循环 | `continuous-agent-loop` 已取代 `autonomous-loops` | 可删除 `autonomous-loops` |
| 持续学习 | `continuous-learning`（v1）vs `continuous-learning-v2`（instinct） | 保留 v2，可删除 v1 |
| 技能编写 | `create-skill` vs `writing-skills` vs `skill-creator` | 三者侧重不同，可保留 |
| 幻灯片 | `pptx` / `baoyu-slide-deck` / `frontend-slides` | 三条路径互补 |
| X/Twitter | `baoyu-post-to-x` / `baoyu-danger-x-to-markdown` / `x-api` / `social-content` / `crosspost` / `content-engine` | 功能交叉较多 |
| 研究 | `deep-research` vs `market-research` vs `exa-search` | 层次不同，保留 |

---

## 按分类的技能清单

### 1. 元技能 / Cursor 与技能生态（11 个）

| 名称 | 来源 | 说明 |
|------|------|------|
| `create-skill` | Marketplace | 引导编写 Cursor Agent Skill 的结构与最佳实践 |
| `create-rule` | Marketplace | 在 `.cursor/rules/` 创建持久化规则与项目约定 |
| `migrate-to-skills` | Marketplace | 将 `.mdc` 规则迁移为 Skills 格式 |
| `create-subagent` | Marketplace | 配置 `.cursor/agents/` 专用子代理 |
| `update-cursor-settings` | Marketplace | 修改 Cursor/VSCode 的 settings.json |
| `shell` | Marketplace | 将后续文本当作终端命令执行 |
| `using-superpowers` | 手动安装 | 会话开始即加载技能使用规范 |
| `skill-creator` | 手动安装 | 创建/改进技能并做 eval 与基准优化 |
| `writing-skills` | 手动安装 | 编写与校验可部署的 Skill 文档 |
| `configure-ecc` | Marketplace | ECC 交互式安装向导 |
| `skill-stocktake` | Marketplace | 审计技能与命令质量的盘点流程 |

### 2. 开发流程 / 规划 / 协作（17 个）

| 名称 | 来源 | 说明 |
|------|------|------|
| `brainstorming` | 手动安装 | 创意与功能改动前先澄清意图与需求 |
| `writing-plans` | 手动安装 | 多步骤任务动笔前先写实施计划 |
| `planning-with-files` | 手动安装 | 文件化规划与会话恢复 |
| `executing-plans` | 手动安装 | 按书面计划执行并设检查点 |
| `subagent-driven-development` | 手动安装 | 子代理驱动开发 |
| `dispatching-parallel-agents` | 手动安装 | 多任务并行分派 |
| `blueprint` | Marketplace | 一句话目标拆成跨会话建设蓝图 |
| `doc-coauthoring` | 手动安装 | 文档/规格/决策稿的共创流程 |
| `finishing-a-development-branch` | 手动安装 | 合并、PR、清理等结构化收尾 |
| `requesting-code-review` | 手动安装 | 发起代码审查 |
| `receiving-code-review` | 手动安装 | 评估评审意见 |
| `using-git-worktrees` | 手动安装 | 用 git worktree 隔离功能开发 |
| `search-first` | Marketplace | 先检索现有工具再写代码 |
| `strategic-compact` | Marketplace | 在任务边界建议压缩上下文 |
| `iterative-retrieval` | Marketplace | 渐进细化检索缓解上下文不足 |
| `dmux-workflows` | Marketplace | dmux/tmux 多窗格编排 AI 会话 |
| `project-guidelines-example` | Marketplace | 项目专属技能模板示例 |

### 3. 验证、测试与质量（17 个）

| 名称 | 来源 | 说明 |
|------|------|------|
| `verification-before-completion` | 手动安装 | 完成前必须跑命令拿证据 |
| `verification-loop` | Marketplace | 综合验证体系 |
| `systematic-debugging` | 手动安装 | 系统化诊断 bug |
| `tdd-workflow` | Marketplace | TDD 与高覆盖率门槛 |
| `e2e-testing` | Marketplace | Playwright E2E 与 CI |
| `eval-harness` | Marketplace | 正式评测框架 |
| `python-testing` | Marketplace | pytest 实践 |
| `golang-testing` | Marketplace | Go 表驱动测试 |
| `kotlin-testing` | Marketplace | Kotest/MockK 测试 |
| `cpp-testing` | Marketplace | GoogleTest/CTest |
| `perl-testing` | Marketplace | Test2/Test::More |
| `django-tdd` | Marketplace | pytest-django TDD |
| `django-verification` | Marketplace | Django 发布前检查 |
| `springboot-tdd` | Marketplace | JUnit5/Mockito TDD |
| `springboot-verification` | Marketplace | Spring Boot 验证闭环 |
| `plankton-code-quality` | Marketplace | 每次编辑时格式化/lint/AI 修复 |
| `content-hash-cache-pattern` | Marketplace | 内容哈希缓存模式 |

### 4. AI / Agent 与自动化（14 个）

| 名称 | 来源 | 说明 |
|------|------|------|
| `continuous-agent-loop` | Marketplace | 连续自主循环（canonical） |
| `autonomous-loops` | Marketplace | 自主循环（过渡期，指向上者） |
| `enterprise-agent-ops` | Marketplace | 长生命周期 agent 管理 |
| `agentic-engineering` | Marketplace | 评测优先的代理化工程 |
| `ai-first-engineering` | Marketplace | AI 产出占比高团队流程 |
| `agent-harness-construction` | Marketplace | 优化工具定义与动作空间 |
| `ralphinho-rfc-pipeline` | Marketplace | RFC 驱动多智能体 DAG |
| `continuous-learning` | Marketplace | 会话结束抽取模式（v1） |
| `continuous-learning-v2` | Marketplace | instinct 学习与项目隔离（v2） |
| `cost-aware-llm-pipeline` | Marketplace | 模型路由与成本控制 |
| `prompt-optimizer` | Marketplace | prompt 优化建议 |
| `regex-vs-llm-structured-text` | Marketplace | 结构化文本解析策略 |
| `nanoclaw-repl` | Marketplace | NanoClaw 零依赖会话 REPL |

### 5. 编程语言 — Kotlin / Android / KMP（6 个）

| 名称 | 来源 | 说明 |
|------|------|------|
| `kotlin-patterns` | Marketplace | Kotlin 惯用法、协程、空安全与 DSL |
| `kotlin-coroutines-flows` | Marketplace | Coroutines、Flow、StateFlow 与测试 |
| `kotlin-ktor-patterns` | Marketplace | Ktor 服务端路由与 WebSocket |
| `kotlin-exposed-patterns` | Marketplace | Exposed ORM 与仓储模式 |
| `compose-multiplatform-patterns` | Marketplace | Compose Multiplatform 状态与性能 |
| `android-clean-architecture` | Marketplace | Android/KMP Clean Architecture |

### 6. 编程语言 — 其他（22 个）

| 名称 | 来源 | 说明 |
|------|------|------|
| `coding-standards` | Marketplace | TS/JS/React/Node 通用规范 |
| `frontend-patterns` | Marketplace | React、Next.js 状态管理 |
| `java-coding-standards` | Marketplace | Spring Boot 向 Java 风格 |
| `springboot-patterns` | Marketplace | Spring Boot 分层与 REST |
| `jpa-patterns` | Marketplace | JPA/Hibernate 实体与查询 |
| `python-patterns` | Marketplace | PEP8 与 Pythonic 实践 |
| `django-patterns` | Marketplace | Django/DRF 架构 |
| `golang-patterns` | Marketplace | 惯用 Go 模式 |
| `cpp-coding-standards` | Marketplace | 现代 C++ 规范 |
| `perl-patterns` | Marketplace | Perl 5.36+ 现代写法 |
| `swiftui-patterns` | Marketplace | SwiftUI 架构与性能 |
| `swift-protocol-di-testing` | Marketplace | Swift 协议化 DI |
| `swift-concurrency-6-2` | Marketplace | Swift 6.2 并发模型 |
| `swift-actor-persistence` | Marketplace | Actor 持久化 |
| `liquid-glass-design` | Marketplace | iOS 26 Liquid Glass |
| `foundation-models-on-device` | Marketplace | Apple 端侧 AI |

### 7. 安全（5 个）

| 名称 | 来源 | 说明 |
|------|------|------|
| `security-review` | Marketplace | 通用安全清单与模式 |
| `security-scan` | Marketplace | AgentShield 配置扫描 |
| `django-security` | Marketplace | Django 安全配置 |
| `springboot-security` | Marketplace | Spring Security |
| `perl-security` | Marketplace | Perl Web 安全 |

### 8. 后端、API 与基础设施（8 个）

| 名称 | 来源 | 说明 |
|------|------|------|
| `api-design` | Marketplace | REST API 设计规范 |
| `backend-patterns` | Marketplace | Node/Express 分层模式 |
| `deployment-patterns` | Marketplace | CI/CD 与上线清单 |
| `docker-patterns` | Marketplace | Docker Compose 开发 |
| `database-migrations` | Marketplace | 数据库迁移策略 |
| `postgres-patterns` | Marketplace | PostgreSQL 优化 |
| `clickhouse-io` | Marketplace | ClickHouse OLAP |

### 9. 文档处理（7 个）

| 名称 | 来源 | 说明 |
|------|------|------|
| `pdf` | 手动安装 | PDF 全流程 |
| `docx` | 手动安装 | Word 创建编辑 |
| `pptx` | 手动安装 | 幻灯片读写 |
| `xlsx` | 手动安装 | 电子表格处理 |
| `nutrient-document-processing` | Marketplace | 商业 API 文档处理 |
| `visa-doc-translate` | Marketplace | 签证材料英译 |

### 10. 知识管理（6 个）

| 名称 | 来源 | 说明 |
|------|------|------|
| `obsidian-markdown` | 手动安装 | Obsidian 方言支持 |
| `obsidian-bases` | 手动安装 | Obsidian Bases 视图 |
| `json-canvas` | 手动安装 | JSON Canvas 画布 |
| `obsidian-cli` | 手动安装 | CLI 管理 Obsidian |
| `defuddle` | 手动安装 | 网页转 Markdown |
| `notebooklm` | 手动安装 | NotebookLM 集成 |

### 11. MCP / 集成（5 个）

| 名称 | 来源 | 说明 |
|------|------|------|
| `mcp-builder` | 手动安装 | 构建 MCP 服务 |
| `claude-api` | Marketplace | Claude API 全功能 |
| `web-artifacts-builder` | 手动安装 | 构建 claude.ai 工件 |
| `exa-search` | Marketplace | Exa 神经搜索 |
| `deep-research` | Marketplace | 多源深度研究 |

### 12. 设计 / UI / 主题（6 个）

| 名称 | 来源 | 说明 |
|------|------|------|
| `frontend-design` | 手动安装 | 高完成度 Web 界面 |
| `canvas-design` | 手动安装 | 静态视觉作品 |
| `algorithmic-art` | 手动安装 | p5.js 生成艺术 |
| `theme-factory` | 手动安装 | 配色主题生成 |
| `brand-guidelines` | 手动安装 | Anthropic 品牌规范 |
| `frontend-slides` | Marketplace | HTML 演示幻灯片 |

### 13. 媒体生成（3 个）

| 名称 | 来源 | 说明 |
|------|------|------|
| `fal-ai-media` | Marketplace | fal.ai 文生图/视频/TTS |
| `video-editing` | Marketplace | AI 辅助剪辑 |
| `videodb` | Marketplace | 视频索引与编辑 |

### 14. 内容写作（2 个）

| 名称 | 来源 | 说明 |
|------|------|------|
| `humanizer` | 手动安装 | 去除 AI 写作痕迹 |
| `article-writing` | Marketplace | 长文博客/教程 |

### 15. Baoyu 中文内容（15 个）

| 名称 | 来源 | 说明 |
|------|------|------|
| `baoyu-article-illustrator` | 手动安装 | 文章配图生成 |
| `baoyu-comic` | 手动安装 | 教育/叙事漫画 |
| `baoyu-compress-image` | 手动安装 | 图片压缩转 WebP |
| `baoyu-cover-image` | 手动安装 | 文章封面图 |
| `baoyu-danger-gemini-web` | 手动安装 | Gemini 文图生成 |
| `baoyu-danger-x-to-markdown` | 手动安装 | X 推文转 Markdown |
| `baoyu-format-markdown` | 手动安装 | Markdown 规范化 |
| `baoyu-image-gen` | 手动安装 | 多厂商文生图 |
| `baoyu-infographic` | 手动安装 | 信息图生成 |
| `baoyu-markdown-to-html` | 手动安装 | 微信友好 HTML |
| `baoyu-post-to-wechat` | 手动安装 | 公众号发布 |
| `baoyu-post-to-x` | 手动安装 | X 发帖 |
| `baoyu-slide-deck` | 手动安装 | 幻灯片图片生成 |
| `baoyu-url-to-markdown` | 手动安装 | URL 转 Markdown |
| `baoyu-xhs-images` | 手动安装 | 小红书种草图 |

### 16. SEO（14 个）

| 名称 | 来源 | 说明 |
|------|------|------|
| `seo` | 手动安装 | SEO/GEO 总控 |
| `seo-audit` | 手动安装 | 全站 SEO 审计 |
| `seo-page` | 手动安装 | 单页深评 |
| `seo-technical` | 手动安装 | 技术 SEO |
| `seo-content` | 手动安装 | 内容 E-E-A-T 审计 |
| `seo-schema` | 手动安装 | Schema.org 校验 |
| `seo-sitemap` | 手动安装 | XML sitemap |
| `seo-images` | 手动安装 | 图片 SEO |
| `seo-hreflang` | 手动安装 | 多语言 hreflang |
| `seo-programmatic` | 手动安装 | 程序化页面 |
| `seo-competitor-pages` | 手动安装 | 竞品对比页 |
| `seo-geo` | 手动安装 | 生成式引擎优化 |
| `seo-plan` | 手动安装 | SEO 战略路线图 |
| `seo-dataforseo` | 手动安装 | DataForSEO 数据 |

### 17. 营销 / CRO（30 个）

| 名称 | 来源 | 说明 |
|------|------|------|
| `product-marketing-context` | 手动安装 | 产品营销上下文 |
| `content-strategy` | 手动安装 | 内容策略 |
| `copywriting` | 手动安装 | 营销文案 |
| `copy-editing` | 手动安装 | 文案润色 |
| `page-cro` | 手动安装 | 页面转化率优化 |
| `form-cro` | 手动安装 | 表单优化 |
| `signup-flow-cro` | 手动安装 | 注册流程优化 |
| `onboarding-cro` | 手动安装 | 激活体验优化 |
| `popup-cro` | 手动安装 | 弹窗优化 |
| `paywall-upgrade-cro` | 手动安装 | 付费墙优化 |
| `ab-test-setup` | 手动安装 | A/B 测试设计 |
| `analytics-tracking` | 手动安装 | 埋点方案 |
| `paid-ads` | 手动安装 | 付费投放 |
| `ad-creative` | 手动安装 | 广告创意 |
| `cold-email` | 手动安装 | B2B 冷邮件 |
| `email-sequence` | 手动安装 | 自动化邮件流 |
| `social-content` | 手动安装 | 社交内容 |
| `launch-strategy` | 手动安装 | 产品发布策划 |
| `marketing-ideas` | 手动安装 | 139 条增长点子 |
| `marketing-psychology` | 手动安装 | 70+ 心理学模型 |
| `competitor-alternatives` | 手动安装 | 竞品对比页 |
| `referral-program` | 手动安装 | 推荐计划 |
| `pricing-strategy` | 手动安装 | 定价策略 |
| `churn-prevention` | 手动安装 | 流失挽回 |
| `free-tool-strategy` | 手动安装 | 免费工具获客 |
| `revops` | 手动安装 | 线索评分与路由 |
| `sales-enablement` | 手动安装 | 销售材料 |
| `site-architecture` | 手动安装 | 网站信息架构 |

### 18. 社交 / 内容分发（3 个）

| 名称 | 来源 | 说明 |
|------|------|------|
| `content-engine` | Marketplace | 一源多平台内容 |
| `crosspost` | Marketplace | 跨平台分发 |
| `x-api` | Marketplace | X API 发帖与分析 |

### 19. 市场研究 / 投融资（3 个）

| 名称 | 来源 | 说明 |
|------|------|------|
| `market-research` | Marketplace | 竞品与赛道研究 |
| `investor-materials` | Marketplace | 融资材料 |
| `investor-outreach` | Marketplace | 投资人邮件 |

### 20. 行业特定（8 个）

| 名称 | 来源 | 说明 |
|------|------|------|
| `carrier-relationship-management` | Marketplace | 承运商管理 |
| `customs-trade-compliance` | Marketplace | 关务合规 |
| `logistics-exception-management` | Marketplace | 物流异常处理 |
| `returns-reverse-logistics` | Marketplace | 退货逆向物流 |
| `inventory-demand-planning` | Marketplace | 需求预测 |
| `production-scheduling` | Marketplace | 制造排产 |
| `quality-nonconformance` | Marketplace | 质量不合格管理 |
| `energy-procurement` | Marketplace | 能源采购 |

---

## 统计摘要

| 分类 | 数量 |
|------|------|
| 营销/CRO | 30 |
| 编程语言（全部） | 28 |
| 开发流程/规划 | 17 |
| 验证/测试/质量 | 17 |
| Baoyu 中文内容 | 15 |
| SEO | 14 |
| AI/Agent 自动化 | 14 |
| 元技能 | 11 |
| 后端/API/基础设施 | 8 |
| 行业特定 | 8 |
| 文档处理 | 7 |
| 知识管理 | 6 |
| 设计/UI/主题 | 6 |
| 安全 | 5 |
| MCP/集成 | 5 |
| 媒体生成 | 3 |
| 社交/内容分发 | 3 |
| 市场研究/投融资 | 3 |
| 内容写作 | 2 |
| **合计** | **191** |
