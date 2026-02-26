# Cursor Agent 最佳实践与效率技巧

> 基于 [Cursor 官方 Best Practices](https://cursor.com/blog/agent-best-practices) 和社区经验整理，涵盖工作流优化、上下文管理、高效提示词等。

---

## 一、Agent 工作三要素

Agent 框架由三个组件构成：

| 组件 | 说明 |
|------|------|
| **用户消息** | 你的提示词和追问，指导工作方向 |
| **工具** | 文件编辑、代码搜索、终端执行等 |
| **指令** | 系统提示词和规则，引导 Agent 行为 |

Cursor 针对每个前沿模型调优了指令和工具调用方式，你只需专注于描述任务。

---

## 二、先规划再编码（Plan First）

芝加哥大学研究表明：有经验的开发者更倾向于先规划再生成代码，结果更干净。

### 使用 Plan 模式

按 `Shift+Tab` 切换到 Plan 模式，Agent 会：

1. 调研代码库，找到相关文件
2. 提出澄清问题
3. 生成详细实施方案（含文件路径和代码引用）
4. 等你批准后再构建

方案以 Markdown 打开，可直接编辑。点「Save to workspace」保存到 `.cursor/plans/`，方便团队共享和日后恢复。

### 何时直接跳过规划

- 快速小改动
- 已经做过很多次的任务
- 简单的 bug 修复

### 方案不满意时

不要通过追问来修补，而是：**撤销变更 → 修改方案 → 重新运行**。这通常比修补半成品更快、更干净。

---

## 三、上下文管理

### 让 Agent 自己找上下文

不需要手动标记每个文件。Cursor 的搜索工具（grep + 语义搜索）可以毫秒级检索代码库。

- 如果你知道确切文件，用 `@` 标记它
- 如果不确定，描述需求，Agent 会自己找到
- 包含无关文件反而会干扰 Agent 判断

### `@` 符号的 8 种高级用法

| 引用 | 说明 | 准确率提升 |
|------|------|:----------:|
| `@Codebase` | 搜索整个代码库 | — |
| `@File` | 引用指定文件 | — |
| `@Folder` | 引用整个目录 | — |
| `@Docs` | 引用已配置的文档源 | — |
| `@Web` | 搜索在线资源（Pro 功能） | — |
| `@Git` / `@Branch` | 引用 Git 变更 | — |
| `@symbol` | 跳转到函数/类定义 | — |
| `@Past Chats` | 引用过往对话 | — |

**技巧**：组合使用 `@` 可以将 AI 准确率从 62% 提升到 91%。

### 何时开新对话 vs 继续

**开新对话**：
- 完成了一个逻辑单元的工作
- Agent 似乎困惑或反复犯同样错误
- 切换到不同任务或功能

**继续对话**：
- 调试刚才构建的东西
- Agent 需要之前讨论的上下文
- 仍在迭代同一功能

长对话会导致 Agent 失去焦点。感觉效果下降时，果断开新对话。

---

## 四、Rules 最佳实践

### 写什么

```markdown
# Commands
- `npm run build`: Build the project
- `npm run test`: Run tests (prefer single test files)

# Code style
- Use ES modules, not CommonJS
- See `components/Button.tsx` for canonical structure

# Workflow
- Always typecheck after making code changes
- API routes go in `app/api/` following existing patterns
```

### 关键原则

- **聚焦核心**：只写命令、模式、典型示例的指向
- **引用文件而非复制内容**：保持规则简短，避免过时
- **从简开始**：只在 Agent 反复犯同样错误时才添加规则
- **提交到 Git**：让团队共享

### 避免什么

- 为极少出现的边界情况添加指令
- 记录所有可能的命令（Agent 认识常用工具）
- 复制完整风格指南（用 linter 代替）

---

## 五、代码审查策略

### 生成过程中

观察 Agent 工作，diff 视图实时显示变更。方向不对时按 `Escape` 中断并重新引导。

### Agent Review

完成后点 **Review → Find Issues**，Agent 逐行分析并标记潜在问题。

在 Source Control 标签页运行 **Agent Review**，对比主分支上所有本地变更。

### BugBot（PR 审查）

推送到版本控制，BugBot 在每个 PR 上自动运行高级分析。

---

## 六、编写高效提示词

### 差的提示词 vs 好的提示词

| 差 | 好 |
|-----|-----|
| "add tests for auth.ts" | "Write a test case for auth.ts covering the logout edge case, using the patterns in `__tests__/` and avoiding mocks." |
| "fix the bug" | "The login form throws 'undefined is not a function' when submitting empty fields. Fix it in `src/auth/login.tsx`." |
| "make it faster" | "Profile the `getProducts` API route. The `JOIN` on line 45 of `db/queries.ts` may be causing N+1 queries." |

### 提示词五要素

1. **具体**：指明文件、函数、行号
2. **有明确目标**：期望的输入/输出、通过/失败标准
3. **给出约束**：不要修改哪些文件、遵循什么模式
4. **提供上下文**：相关背景信息
5. **可验证**：Agent 能自行检查结果是否正确

---

## 七、高效开发者的特征

基于 Cursor 团队和社区的观察：

| 特征 | 说明 |
|------|------|
| **写具体的提示词** | 具体指令的成功率显著高于模糊描述 |
| **迭代优化配置** | 从简开始，逐步添加规则和命令 |
| **仔细审查** | AI 代码可能看起来对但实际有微妙错误，认真读 diff |
| **提供可验证目标** | 使用类型语言、配置 linter、编写测试 |
| **把 Agent 当合作者** | 要方案、要解释、对不喜欢的方案说不 |

---

## 八、大型代码库策略

### 索引优化

1. 在 `.cursorignore` 中排除 `node_modules/`、`dist/`、`.venv/`、`__pycache__/`
2. 对 Monorepo，用多根工作区打开特定 package，而非整个根目录
3. 在 Settings → Indexing and Docs 监控索引健康状态

### 精准提问

- 尽可能用 `@Folder` 限定目录再提问
- 先广后窄：从高层概览到具体细节
- 用 `@Branch` 让 Agent 了解当前工作内容

---

## 九、Plugins 插件市场（v2.5 新增）

### 什么是 Plugin

Plugin 将 Rules、Skills、Agents、Commands、MCP、Hooks 打包为可分发的捆绑包。

### 可用插件类别

| 类别 | 示例 |
|------|------|
| **设计** | Figma |
| **基础设施** | AWS、Cloudflare、Neon Postgres、Sentry、Vercel |
| **数据分析** | Amplitude、ClickHouse、Databricks、PostHog、Snowflake、Supabase |
| **支付** | Stripe |
| **协作** | Linear、Monday.com、Notion、Slack、Atlassian（Jira/Confluence） |
| **AI/ML** | Hugging Face |
| **开发工具** | Superpowers、Code Review、Frontend、iOS、Android |

### 安装方式

- 浏览器：[cursor.com/marketplace](https://cursor.com/marketplace)
- 编辑器内：`/add-plugin`
- 所有 Plugin 必须开源，经 Cursor 团队手动审核后上架

### 创建 Plugin

创建包含 `.cursor-plugin/plugin.json` 清单的目录，添加组件后提交给 Cursor 团队。详见 [Building Plugins](https://cursor.com/docs/plugins/building)。

---

## 十、版本更新要点（2026）

### v2.5（2026-02-17）

| 功能 | 说明 |
|------|------|
| **Plugins 市场** | 一键安装 Skills + MCP + Hooks + Rules 捆绑包 |
| **沙箱网络控制** | 精细化域名允许/拒绝列表 |
| **异步子代理** | 子代理后台运行，父 Agent 继续工作；子代理可嵌套子代理 |

### v2.4（2026-01-22）

| 功能 | 说明 |
|------|------|
| **SubAgents** | 独立子代理，自定义提示词/工具/模型 |
| **Skills** | SKILL.md 定义，动态上下文发现 |
| **Image Generation** | Agent 内生成图片（模型+文本描述） |
| **Cursor Blame** | AI 增强 git blame（企业版） |

---

## 十一、学习资源推荐

### 官方资源

| 资源 | 链接 |
|------|------|
| 官方文档 | [cursor.com/docs](https://cursor.com/docs) |
| 中文文档 | [cursor.com/cn/docs](https://cursor.com/cn/docs) |
| Changelog | [cursor.com/changelog](https://cursor.com/changelog) |
| Blog | [cursor.com/blog](https://cursor.com/blog) |
| Forum | [forum.cursor.com](https://forum.cursor.com) |
| Marketplace | [cursor.com/marketplace](https://cursor.com/marketplace) |

### 社区资源

| 资源 | 链接 | 说明 |
|------|------|------|
| Cursor Directory | [cursor.directory](https://cursor.directory) | 71.7k+ 成员社区中心 |
| Learn Cursor | [learn-cursor.com](https://learn-cursor.com) | 从初级到高级的系统学习 |
| Developer Toolkit | [developertoolkit.ai](https://developertoolkit.ai/en/cursor-ide/) | 112+ 技巧合集 |
| Cursor 101 | [github.com/biubiubiu35/cursor101](https://github.com/biubiubiu35/cursor101) | 中文入门教程 |
| cursorintro.com | [cursorintro.com](https://cursorintro.com) | 最佳实践指南 |

### 中文教程

| 教程 | 说明 |
|------|------|
| [Cursor AI 初学者教程](https://lilys.ai/zh/notes/cursor-ai-20251026/cursor-ai-tutorial-beginners) | 基础界面、文件浏览、终端 |
| [15分钟学会 Cursor 2.0](https://lilys.ai/notes/zh/cursor-20-20251106/cursor-two-beginner-guide) | Agent 视图、浏览器集成 |

---

## 十二、快捷键速查

| 快捷键 | 功能 |
|--------|------|
| `Cmd/Ctrl+I` | 打开 Composer（多文件编辑） |
| `Cmd/Ctrl+K` | 打开 Chat（单轮对话） |
| `Cmd/Ctrl+.` | 快速切换模式 |
| `Shift+Tab` | 切到 Plan 模式 |
| `Cmd/Ctrl+E` | Cloud Agent |
| `Tab` | 接受补全建议 |
| `Escape` | 拒绝建议 / 中断 Agent |
| `Cmd/Ctrl+→` | 逐词接受补全 |
| `Cmd/Ctrl+Shift+P` | Command Palette |
| `Cmd/Ctrl+Shift+J` | Cursor Settings |

---

*基于 Cursor 官方文档、Blog 和社区资料（2026 年 2 月）整理。*
