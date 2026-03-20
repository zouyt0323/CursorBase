# 热门 Agent Skills TOP 20（2026 年）

基于多个主流 Skills 汇总网站（awesomeagentskills.com、awesomeskills.dev、agent-skills.cc、scriptbyai.com 等）的热度和推荐数据，综合排列出当前使用最多的前 20 个 Agent Skills。

---

## 排行榜

| 排名 | 技能名称 | 中文名 | 用途 | 来源 / GitHub | Cursor 可用 |
|:----:|----------|--------|------|--------------|:-----------:|
| 1 | **Superpowers** | 超级能力 | 规划优先的软件开发工作流：头脑风暴 → TDD → 系统调试 → 代码评审 | [obra/superpowers](https://github.com/obra/superpowers) | 是 |
| 2 | **ui-ux-pro-max** | UI/UX 专业设计 | 自动生成完整的设计系统（配色、字体、组件模式），支持 React/Vue/SwiftUI | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | 是 |
| 3 | **agent-skills (Vercel)** | Vercel 技能包 | React/Next.js 性能优化、无障碍审计、Vercel 部署 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | 是 |
| 4 | **planning-with-files** | 文件式规划 | 用持久化 Markdown 文件管理长任务的计划、发现和进度，防止上下文丢失 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | 是 |
| 5 | **context-engineering** | 上下文工程 | 构建自定义 Agent 系统、多智能体架构、上下文窗口优化 | [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) | 是 |
| 6 | **prompt-engineer** | 提示词工程师 | 优化和测试提示词效果，提升输出质量 60-80% | antigravity-awesome-skills | 是 |
| 7 | **rag-engineer** | RAG 检索增强 | 构建企业级 RAG 系统，向量数据库、文档检索与生成 | antigravity-awesome-skills | 是 |
| 8 | **claude-scientific-skills** | 科学研究技能包 | 140+ 技能覆盖生物信息、化学、医学，集成 PubMed/ChEMBL/RDKit | [K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills) | 是 |
| 9 | **dev-browser** | 开发者浏览器 | 让 AI 可控制浏览器：导航网站、点击元素、截图验证 UI | [SawyerHood/dev-browser](https://github.com/SawyerHood/dev-browser) | 是 |
| 10 | **humanizer** | 人性化写作 | 检测并移除 24 种 AI 写作特征，使文本更自然 | [blader/humanizer](https://github.com/blader/humanizer) | 是 |
| 11 | **obsidian-skills** | Obsidian 技能 | Obsidian 知识库集成，支持 wiki 链接、Callout、Canvas 等格式 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | 是 |
| 12 | **marketingskills** | 营销技能包 | CRO 转化优化、着陆页文案、SEO 审计、产品发布策略 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | 是 |
| 13 | **frontend-design (Anthropic)** | 前端设计 | 生产级前端界面设计，避免 AI 风格，强调独特性 | [anthropics/skills](https://github.com/anthropics/skills) | 是 |
| 14 | **mcp-builder (Anthropic)** | MCP 服务器构建 | 官方 MCP 服务器开发指南，支持 Python/Node.js | [anthropics/skills](https://github.com/anthropics/skills) | 是 |
| 15 | **test-driven-development** | 测试驱动开发 | 强制 Red-Green-Refactor 循环，先写测试再写实现 | [obra/superpowers](https://github.com/obra/superpowers) | 是 |
| 16 | **systematic-debugging** | 系统化调试 | 4 阶段根因分析流程，系统性定位和修复 Bug | [obra/superpowers](https://github.com/obra/superpowers) | 是 |
| 17 | **docx/pdf/pptx/xlsx (Anthropic)** | 文档处理四件套 | Word/PDF/PPT/Excel 全方位处理，附完整 Python 脚本 | [anthropics/skills](https://github.com/anthropics/skills) | 是 |
| 18 | **connect-apps** | 应用连接器 | 将 Claude 连接到 Gmail、Slack、GitHub 等外部服务 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | 是 |
| 19 | **Notion Skills** | Notion 技能 | Claude 与 Notion 工作区深度集成 | [notiondevs](https://www.notion.so/notiondevs/Notion-Skills-for-Claude-28da4445d27180c7af1df7d8615723d0) | 是 |
| 20 | **playwright-skill** | Playwright 测试 | 通用浏览器自动化工具，即时编写 Playwright 脚本 | [lackeyjb/playwright-skill](https://github.com/lackeyjb/playwright-skill) | 是 |

---

## 详细介绍

### 1. Superpowers（超级能力）

**热度**：最受推荐的 Agent Skill，多个排行榜排名第一

**功能**：完整的软件开发工作流，强制 AI Agent 在编码前先规划、再测试、再实现。包含 5 个子技能模块：
- **Brainstorming**：通过苏格拉底式提问细化需求
- **Test-Driven Development**：强制 Red-Green-Refactor 循环
- **Systematic Debugging**：4 阶段根因分析
- **Code Review**：预审检查清单 + 反馈处理
- **Subagent-Driven Development**：并行子任务分发

**为什么热门**：解决了 AI Agent 最大的痛点——跳过规划直接写代码导致的 Bug 和糟糕架构。

**安装**：
```bash
/plugin marketplace add obra/superpowers-marketplace
/plugin install superpowers@superpowers-marketplace
```

---

### 2. ui-ux-pro-max（UI/UX 专业设计）

**热度**：前端开发者首选设计技能

**功能**：
- 自动分析项目需求，生成完整设计系统（MASTER.md）
- 包含配色方案、字体组合、组件模式
- 内置行业特定推理规则（金融科技、医疗等）
- 支持 React、Vue、SwiftUI、Tailwind CSS

**为什么热门**：开发者不再需要纠结设计决策，一键生成专业级 UI。

---

### 3. agent-skills (Vercel Labs)

**热度**：React/Next.js 开发者标配

**功能**：
- React 组件性能审计（重渲染、包体积）
- 100+ 无障碍规则检查
- 直接从对话中部署到 Vercel
- React Native 平台特定模式

---

### 4. planning-with-files（文件式规划）

**热度**：长任务场景必备

**功能**：
- 用 `task_plan.md`、`findings.md`、`progress.md` 管理复杂任务
- 计划和发现写入磁盘，不占用上下文窗口
- 支持 `/clear` 后恢复工作进度

**为什么热门**：解决了 AI Agent 在长任务中的「目标漂移」和「遗忘」问题。

---

### 5. context-engineering（上下文工程）

**热度**：构建自定义 Agent 的开发者必备

**功能**：
- 设计编排器或对等多智能体架构
- 上下文窗口信息压缩策略
- LLM-as-a-Judge 评估框架
- 沙箱化后台编码 Agent

---

### 6. prompt-engineer（提示词工程师）

**热度**：AI 领域最受关注技能之一，agent-skills.cc 站 12,456 Stars

**功能**：
- 优化和测试提示词效果
- 多种提示词框架（Few-shot、Chain-of-Thought、ReAct 等）
- 提升输出质量 60-80%

---

### 7. rag-engineer（RAG 检索增强）

**热度**：企业 AI 应用核心技能，agent-skills.cc 站 10,234 Stars

**功能**：
- 构建检索增强生成（RAG）系统
- 向量数据库选型与集成
- 文档分块、嵌入、检索策略
- 企业知识库构建

---

### 8. claude-scientific-skills（科学研究技能包）

**热度**：科研领域最大的 Skills 集合

**功能**：140+ 技能覆盖：
- 药物发现：虚拟筛选、分子对接、ADMET 预测
- 基因组学：单细胞 RNA-seq 分析
- 文献检索：OpenAlex、PubMed 集成
- 数据可视化：出版级科学图表

---

### 9. dev-browser（开发者浏览器）

**热度**：让 AI「看见」自己构建的 UI

**功能**：
- 控制浏览器：导航、点击、填表、截图
- 持久会话（无需重复登录）
- 端到端测试验证
- Localhost 实时预览

---

### 10. humanizer（人性化写作）

**热度**：内容创作者必备

**功能**：
- 检测 24 种 AI 写作特征
- 移除「意义膨胀」「谄媚语气」「聊天机器人痕迹」
- 使文本通过维基百科「AI 写作标志」检测

---

## 数据来源

| 网站 | 地址 | 技能数量 |
|------|------|----------|
| Awesome Agent Skills | [awesomeagentskills.com](https://www.awesomeagentskills.com/) | 41,295+ |
| Agent Skills CC | [agent-skills.cc](https://www.agent-skills.cc/) | 63,000+ |
| Awesome Skills Dev | [awesomeskills.dev](https://www.awesomeskills.dev/) | 2,025 |
| ScriptByAI | [scriptbyai.com](https://www.scriptbyai.com/best-agent-skills/) | Top 10 评测 |
| Claude Code Marketplace | [claudecodemarketplace.net](https://claudecodemarketplace.net/) | 1,329 |

---

*整理时间：2026-02-06*
