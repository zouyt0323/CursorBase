# Cursor Plan Mode 完全指南

> 基于 Cursor 官方文档、博客、Changelog 及最佳实践整理，版本覆盖至 Cursor 2.5（2026.02）

---

## 一、什么是 Plan Mode？

Plan Mode 是 Cursor 的**计划模式**，让 AI Agent 在编写代码之前先创建详细的实施计划。它会研究你的代码库、询问澄清问题、生成可审查的计划，你确认后再执行——从根本上提升复杂任务的代码质量。

**官方原话：**
> *"Most new features at Cursor now begin with Agent writing a plan. We've seen this significantly improve the code generated."*

芝加哥大学的一项[研究](https://cursor.com/blog/productivity)发现，经验丰富的开发者更倾向于在生成代码之前先规划。规划迫使你对要构建的内容进行清晰的思考，并为 Agent 提供可操作的具体目标。

---

## 二、核心功能详解

### 2.1 代码库研究（Codebase Research）

进入 Plan Mode 后，Agent 会自动：
- 使用 `grep` 和语义搜索搜索代码库，查找相关文件
- 阅读现有代码、文档和配置
- 理解项目的架构模式和约定
- 查找规范示例作为参考

> **提示**：无需手动标记每个文件，Agent 的搜索工具能自动找到相关文件。只在你确切知道文件路径时才手动指定。

### 2.2 交互式澄清提问（Clarifying Questions）

Agent 会根据任务复杂度提出结构化的澄清问题：
- 通过**交互式 UI** 回答问题（v2.1 新增）
- 问题覆盖需求范围、技术选型、边界条件、设计约束等
- 回答质量直接影响最终计划和代码质量
- 你可以在回答中提供额外上下文和限制条件

### 2.3 计划生成（Plan Generation）

基于研究和问答，Agent 生成结构化的实施计划：

```markdown
# Notification Preferences

## Overview
Add a notification preferences page to user settings.
Users can toggle email, push, and in-app notifications per category.

## Approach
- Follow the existing settings page layout in src/pages/Settings.tsx
- Use the UserPreferences table with a JSONB column
- Reuse our existing Toggle component from the UI library

## Tasks
- [x] Add notification_preferences column to UserPreferences table
- [ ] Create NotificationPreferences component
- [ ] Add API route at app/api/user/notifications/route.ts
- [ ] Wire up optimistic updates using useOptimistic hook
- [ ] Add tests for preference toggling and API validation
```

**关键特点：**
- **Markdown 格式**：包含文件路径、代码引用
- **结构化里程碑**：每个步骤可独立验证
- **可编辑**：直接在聊天中或作为 Markdown 文件编辑
- **To-Do 列表**：可添加/删除/修改/重排序
- **搜索功能**：⌘+F 在计划中搜索（v2.1 新增）

### 2.4 Mermaid 图表支持（v2.2 新增）

计划中支持内联 Mermaid 图表，自动生成并实时渲染：

| 图表类型 | 用途 |
|----------|------|
| 流程图（Flowchart） | 业务逻辑、代码执行流程 |
| 序列图（Sequence Diagram） | 模块间交互、API 调用链 |
| 架构图（Architecture） | 系统设计、数据流 |
| 状态图（State Diagram） | 状态机、生命周期 |

支持标准 Mermaid 语法，可手动编辑调整。

**官方推荐用法**：
> *"Create a Mermaid diagram showing the data flow for our authentication system, including OAuth providers, session management, and token refresh."*

### 2.5 发送任务到新 Agent（v2.2 新增）

可以从计划中选择特定的 To-Do 任务并行执行：

- 右键选择 **"Send to New Agent"**
- 将任务分发给独立的 Agent 并行执行
- 每个 Agent 运行在独立的 Git Worktree 中，互不干扰
- 独立任务可获得约 **3.4x 速度提升**
- Cursor **自动评判**所有并行结果，推荐最佳方案

### 2.6 计划文件持久化（v2.2 新增）

- 计划**默认保存为文件**到磁盘（`~` 主目录）
- 点击 **"Save to workspace"** 可保存到 `.cursor/plans/` 目录
- 支持 Git 版本控制，跟踪计划变更历史
- 可用于团队分享、文档沉淀、中断恢复

> **官方建议**：将计划保存到 `.cursor/plans/` 目录。这样可以为团队创建文档，方便恢复中断的工作，并为未来处理同一功能的 Agent 提供上下文。

> **注意**：Plan Mode 本身没有写入 `.cursor/plans/` 的权限，需要手动点击聊天气泡右上角的 **"Save to workspace"** 按钮。如果需要更可靠的持久化方案，参见[第十五章：计划文件组织的社区最佳实践](#十五plan-mode-计划文件组织最佳实践)。

### 2.7 CLI Plan Mode（v2026.02 新增）

Cursor CLI 现在完整支持 Plan Mode：

| 功能 | 说明 |
|------|------|
| **持久决策菜单** | 计划生成后展示"本地构建"或"云端构建"选项 |
| **`/plan` 命令** | 快速返回当前计划及操作菜单 |
| **键盘导航** | 方向键选择选项，Enter 执行，Shift+Enter 快捷云端构建 |
| **ASCII Mermaid** | Mermaid 图表在终端中渲染为 ASCII 图形 |
| **Ctrl+O** | 切换渲染图与 Mermaid 源码视图 |

### 2.8 长时间运行的 Agent（v2026.02 新增）

Cursor 新增长时间自主运行的 Agent，与 Plan Mode 深度结合：

- Agent **先规划再执行**，自主完成更大更复杂的任务
- 无需人工干预即可产出完整 PR
- 适用于 Ultra、Teams 和 Enterprise 计划
- 在 [cursor.com/agents](https://cursor.com/agents) 启动

### 2.9 异步子 Agent（v2.5 新增）

从计划中拆分的任务现在支持**异步执行**：

- 子 Agent 在后台运行，**不阻塞**父 Agent
- 子 Agent 可以**嵌套生成**自己的子 Agent，形成协作树
- 支持更大规模的任务：多文件功能、大型重构、复杂 Bug 修复
- 更低延迟、更好的流式反馈、更灵敏的并行执行

---

## 三、使用方法

### 3.1 进入 Plan Mode

| 方式 | 操作 |
|------|------|
| **快捷键** | 在 Agent 输入框按 **Shift + Tab** 切换 |
| **快速切换** | **Cmd + .** 打开模式选择器 |
| **下拉菜单** | Agent 界面顶部模式选择下拉 |
| **自动触发** | 描述复杂任务时 Cursor 自动建议使用 |

### 3.2 完整工作流程

```
第1步：描述任务
    ↓
第2步：Agent 研究代码库（自动搜索、读取相关文件）
    ↓
第3步：Agent 提出澄清问题（交互式 UI）
    ↓
第4步：你回答问题，提供额外上下文
    ↓
第5步：Agent 生成详细计划（Markdown + Mermaid 图表 + To-Do 列表）
    ↓
第6步：你审查/编辑计划
    • 删除不必要的步骤
    • 调整实现方案
    • 添加 Agent 遗漏的上下文
    ↓
第7步：点击 "Build" 执行
    ↓
第8步：Agent 按计划逐步编码，每步可独立验证
    ↓
第9步：（可选）保存计划到 .cursor/plans/
```

### 3.3 编辑计划的方式

| 方式 | 说明 |
|------|------|
| **聊天中编辑** | 直接在对话中修改计划内容 |
| **Markdown 文件编辑** | 用编辑器打开计划文件 |
| **搜索** | ⌘+F 搜索计划中的特定内容 |
| **To-Do 勾选** | 标记已完成/跳过的步骤 |

---

## 四、适用场景

### 4.1 推荐使用 Plan Mode

| 场景 | 说明 | 示例 |
|------|------|------|
| **架构决策** | 需要先审查方案再实施 | "添加用户认证系统" |
| **需求不明确** | 需要探索后才能确定范围 | "让应用更快" |
| **多文件变更** | 涉及大量文件或多个系统 | "重构数据库层" |
| **多种方案** | 存在多个有效实现路径 | "添加缓存——Redis vs 内存 vs 文件" |
| **团队协作** | 需要将计划分享给团队评审 | 大型功能开发 |
| **新代码库** | 不熟悉的项目，需要先理解 | 接手他人项目 |

### 4.2 无需 Plan Mode

| 场景 | 建议 |
|------|------|
| 简单快速修改 | 直接使用 Agent Mode |
| 重复性任务 | 直接使用 Agent Mode |
| 代码理解/学习 | 使用 Ask Mode |
| Bug 调试 | 使用 Debug Mode |
| 已做过多次的任务 | 直接使用 Agent Mode |

---

## 五、最佳实践

### 5.1 从计划重新开始（Starting Over）

当 Agent 编码结果不符合预期时：

1. **回退变更**（Revert all changes）
2. **细化计划**，使其更精确、更具体
3. **重新执行**

> **官方建议**：这通常比通过追加提示修复更快，且产出更干净的代码。如果漏掉了关键的架构或系统设计注意事项，从计划重新开始是最佳选择。

### 5.2 写好提示词

| 差的提示 | 好的提示 |
|----------|----------|
| "给 auth.ts 加测试" | "为 auth.ts 编写测试用例，覆盖 logout 边界情况，使用 `__tests__/` 中的模式，避免 mock" |
| "添加缓存" | "在用户查询接口添加 Redis 缓存，TTL 5分钟，参考 `services/CacheService.ts` 的模式" |
| "修复 Bug" | "修复用户在 Safari 上提交表单时偶发的 500 错误，错误日志见 `logs/error.log` 第 238 行" |

### 5.3 测试驱动开发（TDD）与 Plan Mode

Agent 在有明确目标时表现最好。推荐的 TDD + Plan 工作流：

```
第1步：用 Plan Mode 规划功能
第2步：让 Agent 先写测试（明确说明在做 TDD）
第3步：提交测试，确认测试失败
第4步：让 Agent 编写通过测试的代码（不修改测试）
第5步：Agent 反复迭代直到所有测试通过
第6步：审查并提交代码
```

### 5.4 上下文管理

- **让 Agent 自己找上下文**：Agent 的搜索工具能找到大部分相关文件
- **不要包含无关文件**：会混淆 Agent 对重点的判断
- **使用 `@Branch`** 给 Agent 提供当前工作分支的上下文
- **使用 `@Past Chats`** 引用之前的对话，避免复制粘贴

### 5.5 何时开始新对话

| 开始新对话 | 继续当前对话 |
|-----------|-------------|
| 完成了一个逻辑单元的工作 | 正在调试刚刚构建的内容 |
| Agent 看起来困惑或重复犯错 | Agent 需要之前讨论的上下文 |
| 切换到不同的任务或功能 | 正在迭代同一个功能 |

> **提示**：长对话会导致 Agent 失去焦点。如果注意到 Agent 效率下降，是时候开始新对话了。

### 5.6 使用 Rules 配合 Plan Mode

在 `.cursor/rules/` 中配置规则，让 Plan Mode 生成的计划自动遵循团队规范：

```markdown
# Commands
- `npm run build`: Build the project
- `npm run typecheck`: Run the typechecker
- `npm run test`: Run tests

# Code style
- Use ES modules (import/export), not CommonJS
- See `components/Button.tsx` for canonical component structure

# Workflow
- Always typecheck after making a series of code changes
- API routes go in `app/api/` following existing patterns
```

> **官方建议**：只在 Agent 反复犯同样的错误时才添加规则。不要过度优化。

### 5.7 保存计划到工作区

将计划保存为项目文档的好处：
- 为团队创建技术决策记录
- 方便恢复中断的工作
- 为未来的 Agent 提供功能上下文
- 可通过 Git 追踪计划变更历史

---

## 六、高级技巧

### 6.1 多 Agent 并行 + 自动评判（v2.2）

Cursor 支持通过 Git Worktree 并行运行多个 Agent：

- 每个 Agent 在**独立的 Worktree** 中运行，互不干扰
- 可将同一任务同时发给**多个不同模型**
- Cursor **自动评估**所有并行结果
- 推荐最佳方案并附带**选择理由**

**特别适合：**
- 发现单个模型可能遗漏的边界情况
- 比较不同模型家族的代码质量
- 需要不同方法的困难问题

### 6.2 自定义 Slash 命令

创建自定义命令，标准化团队的 Plan 工作流。保存在 `.cursor/commands/` 中：

**示例 `/pr` 命令：**
```markdown
Create a pull request for the current changes.

1. Look at the staged and unstaged changes with `git diff`
2. Write a clear commit message based on what changed
3. Commit and push to the current branch
4. Use `gh pr create` to open a pull request with title/description
5. Return the PR URL when done
```

**其他推荐命令：**
| 命令 | 用途 |
|------|------|
| `/update-deps` | 逐个更新过期依赖，每次更新后运行测试 |
| `/review` | 运行 linter，检查常见问题 |
| `/fix-issue [number]` | 获取 issue 详情，找到相关代码，实现修复 |

### 6.3 设计稿转代码

Plan Mode 支持图片输入：
- 粘贴设计稿截图或 Figma 导出
- Agent 匹配布局、颜色、间距
- 配合 [Figma MCP](https://cursor.com/docs/context/mcp/directory) 拉取设计令牌和组件规格

### 6.4 Browser 集成——可视化验证

Cursor Browser 可直接在编辑器内验证 Plan 的执行结果：

| 能力 | 说明 |
|------|------|
| **页面导航** | 自动打开页面检查实现效果 |
| **表单测试** | 填写表单、点击按钮、执行用户流程 |
| **控制台检查** | 监控 console.log、错误、网络请求 |
| **截图** | Agent 自动截图验证 UI 变更 |
| **可视化编辑器** | 拖拽 DOM 元素、调整属性、颜色选择器 |
| **点击+描述** | 点击多个元素后用文字描述变更，启动 Agent 执行 |

**提示词示例：**
```
在浏览器中打开应用，检查登录页面的 console 是否有错误
截图当前页面，对比设计稿是否一致
测试用户注册 → 登录 → 修改个人资料的完整流程
```

### 6.5 MCP 工具集成——扩展 Plan 能力

通过 MCP（Model Context Protocol），Plan Mode 可连接外部工具：

| 类别 | 可用服务 |
|------|----------|
| **项目管理** | Linear、GitHub Issues、Jira |
| **设计** | Figma（官方 MCP）、Figma Dev Mode |
| **通信** | Slack、Notion |
| **部署** | Vercel、Netlify、Heroku |
| **测试** | Playwright、Postman、Sentry |
| **数据库** | MongoDB、Supabase、Prisma |
| **分析** | PostHog、Amplitude |
| **浏览器调试** | Chrome DevTools MCP |
| **文档** | Context7（库文档查询） |

**Web 开发编排示例（Linear + Figma + Browser）：**

```
第1步：从 Linear 获取 Issue 描述和需求
    ↓
第2步：从 Figma 获取设计稿、令牌、组件规格
    ↓
第3步：Plan Mode 生成实施计划
    ↓
第4步：Agent 编码实现
    ↓
第5步：Browser 自动测试和截图验证
    ↓
第6步：通过 Slack 通知团队
```

### 6.6 长时间运行的 Agent 循环

通过 Hooks 创建持续迭代的 Agent：

```json
{
  "version": 1,
  "hooks": {
    "stop": [{ "command": "bun run .cursor/hooks/grind.ts" }]
  }
}
```

适用于：
- 反复运行直到所有测试通过
- 迭代 UI 直到匹配设计稿
- 任何目标可验证的任务

### 6.7 云端 Agent

Plan Mode 生成的计划可交给云端 Agent 执行：
- 从 [cursor.com/agents](https://cursor.com/agents) 启动
- 在手机上检查进度
- Agent 在**独立 VM** 中运行，可构建、测试、控制桌面和浏览器
- 完成后自动开 PR，附带**视频、截图、日志**
- 支持通过 Slack `@Cursor`、GitHub `@cursor`、Linear `@cursor`、API 触发

### 6.8 插件市场（v2.5 新增）

通过 [Cursor Marketplace](https://cursor.com/marketplace) 安装插件扩展 Plan Mode 能力：

- 插件打包了 Skills、子 Agent、MCP 服务、Hooks、Rules
- 合作伙伴包括 Amplitude、AWS、Figma、Linear、Stripe 等
- 使用 `/add-plugin` 直接在编辑器中安装
- 覆盖设计、数据库、支付、分析、部署等工作流

---

## 七、Cursor 四种模式对比

| 模式 | 用途 | 能力 | 可用工具 | 快捷键 |
|------|------|------|----------|--------|
| **Agent** | 复杂功能、重构 | 自主探索、多文件编辑 | 全部工具 | 默认 |
| **Ask** | 学习、提问 | 只读探索、不做修改 | 搜索工具 | Shift+Tab |
| **Plan** | 复杂功能规划 | 创建详细计划、澄清问题 | 全部工具 | Shift+Tab |
| **Debug** | 疑难 Bug | 假设生成、日志插桩、运行时分析 | 全部工具 + Debug 服务器 | Shift+Tab |

> 使用 **Shift+Tab** 在模式间轮换，或 **Cmd+.** 快速选择。

---

## 八、版本演进

| 版本 | 日期 | Plan Mode 相关更新 |
|------|------|-------------------|
| 首次发布 | 2025.11 | Plan Mode 正式推出；代码库研究；计划生成；Markdown 编辑 |
| 2.1 | 2025.11.21 | 交互式澄清问题 UI；计划内搜索（⌘+F）；Instant Grep（Beta） |
| 2.2 | 2025.12.10 | 内联 Mermaid 图表；发送 To-Do 到新 Agent；计划文件默认持久化；多 Agent 自动评判；Debug Mode |
| - | 2026.02.12 | 长时间运行 Agent（先规划再执行，自主完成复杂任务） |
| CLI | 2026.02.18 | CLI Plan Mode（持久决策菜单、`/plan` 命令、ASCII Mermaid、云端/本地构建切换） |
| 2.5 | 2026.02.17 | 插件市场（Cursor Marketplace）；异步子 Agent；沙盒网络访问控制 |
| - | 2026.02.24 | Cloud Agent 升级（独立 VM、视频/截图/日志产出物、可测试自己构建的软件） |
| - | 2026.02.26 | Bugbot Autofix（自动修复 PR 问题，35%+ 合并率） |

---

## 九、避坑指南

| 常见问题 | 解决方案 |
|----------|----------|
| Agent 构建结果不符预期 | 回退变更，细化计划后重新执行（不要追加修复） |
| 计划太笼统 | 提供更多上下文、更具体的需求描述 |
| 对话太长导致效率下降 | 保存当前进度，开始新对话，用 @Past Chats 引用 |
| Agent 编辑了不该动的文件 | 在 Rules 中明确限制 Agent 的操作范围 |
| 并行 Agent 文件冲突 | 使用 Git Worktree 隔离，锁定关键文件 |
| 跳过验证导致隐性 Bug | 配置 linter、类型检查、测试，让 Agent 自动验证 |

---

## 十、Plan Mode 与云端 Agent（Cloud Agents）

Cloud Agents（原名 Background Agents）可在云端独立环境运行，与 Plan Mode 完美配合。

### 10.1 核心优势

| 特性 | 说明 |
|------|------|
| **并行运行** | 同时运行多个 Agent，不占用本地资源 |
| **离线执行** | 关闭电脑后 Agent 继续工作 |
| **完整环境** | 拥有虚拟机，可构建、测试、运行软件 |
| **多端访问** | 桌面端、Web、手机 PWA、Slack、GitHub、Linear、API |

### 10.2 与 Plan Mode 的结合

```
本地 Plan Mode → 生成详细计划
    ↓
将计划交给 Cloud Agent 执行
    ↓
Agent 在云端独立完成编码
    ↓
完成后自动开 PR
    ↓
你审查并合并
```

### 10.3 启动方式

| 入口 | 方法 |
|------|------|
| **Cursor Desktop** | Agent 输入框下拉选择 "Cloud" |
| **Cursor Web** | [cursor.com/agents](https://cursor.com/agents) 启动和管理 |
| **Slack** | `@Cursor` 触发 |
| **GitHub** | 在 PR/Issue 评论 `@cursor` |
| **Linear** | `@cursor` 命令 |
| **API** | 通过 API 编程触发 |
| **手机** | Safari/Chrome 安装 PWA，随时查看进度 |

### 10.4 适合交给云端 Agent 的任务

- 文档更新
- 为已有代码生成测试
- 近期代码变更的重构
- 在做其他事时发现的 Bug 修复
- 任何"待办清单"级别的任务

---

## 十一、Plan Mode 与 Hooks 系统

Hooks 让你观察、控制和扩展 Agent 循环，与 Plan Mode 配合可实现自动化工作流。

### 11.1 核心 Hook 事件

| 事件 | 触发时机 | 用途 |
|------|----------|------|
| `sessionStart` | 会话开始 | 注入上下文 |
| `beforeSubmitPrompt` | 提交提示前 | 验证提示 |
| `beforeReadFile` | 读取文件前 | 控制文件访问 |
| `afterFileEdit` | 文件编辑后 | 运行格式化、lint |
| `beforeShellExecution` | 执行命令前 | 拦截危险操作 |
| `beforeMCPExecution` | 调用 MCP 前 | 控制 MCP 使用 |
| `stop` | Agent 完成 | 检查结果、持续循环 |
| `subagentStart/Stop` | 子 Agent 生命周期 | 控制并行任务 |

### 11.2 实用 Hook 示例

**自动格式化（编辑文件后自动运行 Prettier）：**

```json
{
  "version": 1,
  "hooks": {
    "afterFileEdit": [{ "command": ".cursor/hooks/format.sh" }]
  }
}
```

**持续迭代直到测试通过：**

```json
{
  "version": 1,
  "hooks": {
    "stop": [{ "command": "bun run .cursor/hooks/grind.ts" }]
  }
}
```

**安全门控（拦截危险 SQL）：**

```json
{
  "version": 1,
  "hooks": {
    "beforeShellExecution": [{ "command": ".cursor/hooks/sql-guard.sh" }]
  }
}
```

### 11.3 配置位置

| 级别 | 路径 |
|------|------|
| 项目级 | `.cursor/hooks.json` |
| 全局级 | `~/.cursor/hooks.json` |

---

## 十二、Plan Mode 与 Rules/Skills/Commands 的协同

### 12.1 Rules（规则）—— 始终生效的上下文

| 规则类型 | 说明 |
|----------|------|
| **Always** | 每次对话都应用 |
| **Agent decides** | Agent 根据描述判断是否应用 |
| **Globs** | 匹配文件模式时应用（如 `*.tsx`） |
| **Manual** | 仅在 @-提及时应用 |

**配置位置：**
- 项目级：`.cursor/rules/`
- 全局级：`~/.cursor/rules/`

### 12.2 Skills（技能）—— 按需加载的能力

与 Rules 不同，Skills 只在 Agent 判断相关时才加载，保持上下文窗口干净：

- 存放于 `SKILL.md` 文件
- 包含领域知识、工作流指令、脚本
- 适合不常用但需要时很重要的能力

### 12.3 Commands（命令）—— 可复用的工作流

存放在 `.cursor/commands/` 中，通过 `/` 触发：

| 命令 | 用途 |
|------|------|
| `/plan-feature` | 标准化团队的功能规划流程 |
| `/pr` | 自动提交、推送、开 PR |
| `/review` | 运行 lint、检查问题 |
| `/fix-issue [n]` | 获取 issue 详情并修复 |
| `/update-deps` | 逐个更新依赖并测试 |

### 12.4 协同工作流

```
Rules（始终生效）     → 确保代码风格、命名规范一致
    +
Plan Mode（规划阶段） → 生成遵循 Rules 的结构化计划
    +
Commands（触发执行）  → 用 /plan-feature 启动标准化规划
    +
Skills（按需加载）    → 提供特定领域知识（如部署检查清单）
    +
Hooks（自动化控制）   → 编辑后自动格式化、测试后持续迭代
    +
Cloud Agents（云端）  → 将计划交给云端并行执行
```

---

## 十三、实战案例与数据

### 13.1 生产力数据

| 指标 | 改进 |
|------|------|
| 开发周期 | **缩短 34%** |
| 代码审查次数 | 从 3.2 次降至 **1.1 次** |
| 回滚率 | 从 17% 降至 **4%** |
| 部署信心时间 | 从 47 分钟降至 **12 分钟** |
| AI 生成技术债 | **减少 55%** |
| 合规流程时间 | 从 14 小时降至 **90 分钟** |
| 团队 ROI | **12:1**（结合代码库调优） |

### 13.2 典型使用场景

**场景一：功能开发（Engincan Veske 的实践）**

```
1. 引用 GitHub Issue 描述作为上下文
2. 用 Plan Mode 生成实施计划
3. 优先处理核心功能点
4. 按计划逐步编码并验证
```

**场景二：iOS 应用重构（Nasma 案例）**

```
1. 从"随意编码"转向 Plan Mode 驱动
2. 用 Plan 梳理数千活跃用户的习惯追踪应用
3. 生成重构计划，逐模块执行
4. 显著提升代码清晰度和可维护性
```

**场景三：Chrome 扩展开发（Rachel Cantor 的方法）**

```
1. 以可测试的交付物为中心构建计划
2. 识别并行和线性依赖
3. 按序执行：数据库 Schema → API → CORS → OAuth → UI
4. 每步验证后再进入下一步
```

---

## 十四、Plan Mode 完整生态图

```
┌──────────────────────────────────────────────────────────────┐
│                      Cursor 生态系统                          │
├──────────────┬───────────────────────────────────────────────┤
│              │                                               │
│   输入层     │  用户提示 / 图片 / 设计稿 / @引用             │
│              │  @Branch / @Past Chats / @文件                 │
│              │  Linear Issue / GitHub Issue / Figma 设计      │
│              │                                               │
├──────────────┼───────────────────────────────────────────────┤
│              │                                               │
│   配置层     │  Rules（.cursor/rules/）                       │
│              │  Skills（SKILL.md）                            │
│              │  Commands（.cursor/commands/）                 │
│              │  Plugins（Marketplace）                        │
│              │  MCP Servers（mcp.json）                       │
│              │                                               │
├──────────────┼───────────────────────────────────────────────┤
│              │                                               │
│   计划层     │  ★ Plan Mode ★                                │
│              │  代码库研究 → 澄清提问 → Mermaid 图表         │
│              │  生成计划 → 保存到 .cursor/plans/              │
│              │  CLI: /plan + 持久决策菜单                     │
│              │                                               │
├──────────────┼───────────────────────────────────────────────┤
│              │                                               │
│   执行层     │  Agent Mode（本地执行）                        │
│              │  Cloud Agents（云端 VM，多端触发）             │
│              │  长时间运行 Agent（自主复杂任务）              │
│              │  多 Agent 并行（Git Worktree + 异步子 Agent）  │
│              │                                               │
├──────────────┼───────────────────────────────────────────────┤
│              │                                               │
│   控制层     │  Hooks（自动格式化/安全门控/持续迭代）         │
│              │  Sandbox（沙盒 + 网络访问控制）                │
│              │  Linter / TypeCheck / Tests（自动验证）        │
│              │  Browser（可视化编辑 + 截图验证）              │
│              │                                               │
├──────────────┼───────────────────────────────────────────────┤
│              │                                               │
│   输出层     │  代码变更 / PR（附视频、截图、日志）           │
│              │  Bugbot + Autofix（自动审查+修复）             │
│              │  架构图 / 文档 / 计划文件                      │
│              │                                               │
└──────────────┴───────────────────────────────────────────────┘
```

---

## 十五、Plan Mode 计划文件组织最佳实践

### 15.1 官方推荐结构

```
.cursor/
└── plans/
    ├── feature-auth.md
    ├── refactor-database.md
    └── migration-v2.md
```

点击 "Save to workspace" 自动保存到此目录。

### 15.2 社区推荐的详细结构

对于大型项目，社区推荐更完整的文件组织：

```
doc/workdocs/<yyyy-mm-dd>-<feature-key>/
├── plan.md          # 确认的计划快照
├── todos.md         # 权威任务列表（使用稳定的 kebab-case ID）
├── decisions.md     # 架构决策记录（ADR）
├── log.md           # 里程碑日志（带时间戳）
└── handoff.md       # 完成时的交接说明 / 发布说明
```

**核心原则：**
- 以**工作区文件**为唯一事实来源，不依赖 Cursor 内部存储
- 使用稳定的 `kebab-case` 任务 ID 跟踪进度
- Cursor 内部 to-do 仅作为可选镜像，不作为权威来源
- 所有决策和变更都可通过 Git 追溯

### 15.3 计划文件模板

```markdown
# [功能名称] 实施计划

## 概述
[1-2 句话描述此功能的目的和价值]

## 背景
- 相关 Issue: #xxx
- 设计稿: [Figma 链接]
- 依赖系统: [列出影响的系统]

## 技术方案
### 方案选择
- [x] 方案 A: [描述] — 选择原因: ...
- [ ] 方案 B: [描述] — 未选原因: ...

### 架构图
[Mermaid 图表]

### 影响范围
| 文件/模块 | 变更类型 | 说明 |
|-----------|----------|------|
| `src/...` | 新增 | ... |

## 任务分解
- [ ] 1. [任务描述] — 预计影响: [文件列表]
- [ ] 2. [任务描述]
- [ ] 3. [任务描述]

## 验证标准
- [ ] 单元测试通过
- [ ] 类型检查通过
- [ ] Lint 通过
- [ ] 浏览器测试通过

## 风险与注意事项
- [潜在风险和缓解措施]
```

---

## 十六、Plan Mode 提示词模板库

### 16.1 功能开发

```text
我需要实现 [功能描述]。

背景信息：
- 参考 Issue: #xxx
- 相关文件: @src/components/xxx
- 设计稿已粘贴（或 Figma 链接）

请先研究代码库，然后生成详细的实施计划。
计划需要包含：
1. 架构图（Mermaid）
2. 分步任务列表
3. 每步涉及的文件
4. 验证标准
```

### 16.2 重构

```text
我需要重构 [模块/系统]。

当前问题：
- [问题1]
- [问题2]

约束条件：
- 不能破坏现有 API
- 需要保持向后兼容

请分析当前代码，生成安全的重构计划。
```

### 16.3 Bug 修复规划

```text
在 [场景] 下出现 [问题描述]。

复现步骤：
1. ...
2. ...

期望行为: [描述]
实际行为: [描述]

请分析可能的原因，生成修复计划。
```

### 16.4 性能优化

```text
应用在 [场景] 下性能不佳。

现象：
- [指标1]
- [指标2]

请分析代码库中可能的性能瓶颈，生成优化计划。
优化方案按优先级排列，每步包含预期提升幅度。
```

### 16.5 TDD 规划

```text
请为 [功能] 创建 TDD 实施计划。

功能需求：
- [需求1]
- [需求2]

请按以下顺序规划：
1. 先列出需要编写的测试用例
2. 每个测试的输入和期望输出
3. 实现代码的步骤
4. 引用 @__tests__/ 中的现有测试模式
```

### 16.6 数据库迁移

```text
需要对数据库进行以下变更：
- [变更描述]

请生成安全的迁移计划，包含：
1. 迁移脚本（上下）
2. 数据回填策略
3. 回滚方案
4. 停机时间评估
5. 测试验证步骤
```

---

## 十七、Plan Mode 与 Web 开发工作流

### 17.1 完整编排流程

```
     Linear                Figma              Cursor
    ┌──────┐            ┌──────┐          ┌──────────┐
    │Issue │──获取需求──→│设计稿│──获取规格──→│Plan Mode │
    │描述  │            │组件  │          │生成计划  │
    └──────┘            └──────┘          └────┬─────┘
                                               │
                                          ┌────▼─────┐
                                          │ Agent    │
                                          │ 编码实现  │
                                          └────┬─────┘
                                               │
    ┌──────┐            ┌──────┐          ┌────▼─────┐
    │Slack │←──通知────│Bugbot│←─代码审查──│ Browser  │
    │团队  │            │审查  │          │ 测试验证  │
    └──────┘            └──────┘          └──────────┘
```

### 17.2 UI 组件规则配合 Plan

创建 `.cursor/rules/ui-components.mdc` 确保 Plan 生成的代码复用现有组件：

```markdown
---
description: Implementing designs and building UI
---
- reuse existing UI components from `/src/components/ui`
- create new components by orchestrating ui components if existing ones don't solve the problem
- ask the human how they want to proceed when there are missing components
```

### 17.3 关键实践

| 实践 | 说明 |
|------|------|
| **声明式代码** | React/JSX 等声明式代码与 Plan Mode 配合效果最好 |
| **设计系统** | 通过 Rules 引导 Agent 发现和复用设计系统 |
| **组件库** | 随组件库增长持续更新 Rules |
| **紧密反馈循环** | 用 Browser 工具实时验证 UI 变更 |
| **运行时上下文** | 包含 console log、网络请求、UI 元素数据扩展模型上下文 |

---

## 参考链接

- [Cursor 官方 Plan Mode 博客](https://cursor.com/blog/plan-mode)
- [Cursor Modes 文档](https://cursor.com/docs/agent/planning)
- [Cursor 2.1 Changelog](https://cursor.com/changelog/2-1)
- [Cursor 2.2 Changelog](https://cursor.com/changelog/2-2)
- [Agent 最佳实践](https://cursor.com/blog/agent-best-practices)
- [开发功能指南](https://cursor.com/learn/creating-features)
- [Cloud Agents 文档](https://cursor.com/docs/background-agent)
- [Cloud Agents 博客](https://cursor.com/blog/cloud-agents)
- [Hooks 文档](https://cursor.com/docs/agent/hooks)
- [Rules/Commands/Skills/Hooks 完全指南](https://theodoroskokosioulis.com/blog/cursor-rules-commands-skills-hooks-guide/)
- [Plan Mode 实战案例](https://engincanveske.substack.com/p/how-i-use-cursor-plan-mode-for-real)
- [Plan Mode 成本效益分析](https://dredyson.com/how-cursors-new-plan-mode-delivers-34-faster-development-cycles-a-cost-benefit-analysis-for-engineering-leaders/)
- [Web 开发指南](https://cursor.com/docs/cookbook/web-development)
- [Cursor Marketplace](https://cursor.com/marketplace)
- [计划文件组织方案（社区）](https://forum.cursor.com/t/plan-mode-save-to-workspace-workaround/136968)
- [Cursor CLI Changelog](https://cursor.com/changelog/cli-feb-18-2026)
- [长时间运行 Agent](https://cursor.com/blog/long-running-agents)
- [Bugbot Autofix](https://cursor.com/blog/bugbot-autofix)
