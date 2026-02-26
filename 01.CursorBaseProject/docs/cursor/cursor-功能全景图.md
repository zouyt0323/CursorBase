# Cursor 功能全景图与知识索引

> 基于 [Cursor 官方文档](https://cursor.com/docs) 梳理的功能全景图，标注本工程中已覆盖和待补充的领域。

---

## 一、功能全景图

### 1. Agent 核心

| 功能 | 官方文档 | 本工程覆盖 | 说明 |
|------|----------|:----------:|------|
| **Agent 模式总览** | [agent/overview](https://cursor.com/docs/agent/overview) | 部分 | cursor-完整说明.md 提及 |
| **四大模式（Agent/Ask/Plan/Debug）** | [agent/modes](https://cursor.com/docs/agent/modes) | ✅ | 本文 + 功能全景图 |
| **AI Code Review** | [agent/review](https://cursor.com/docs/agent/review) | — | 编辑器内代码审查 |
| **终端与沙箱** | [agent/terminal](https://cursor.com/docs/agent/terminal) | ✅ | cursor-Hooks与终端沙箱.md |
| **浏览器控制** | [agent/browser](https://cursor.com/docs/agent/browser) | — | Agent 内置浏览器 |
| **安全模型** | [agent/security](https://cursor.com/docs/agent/security) | 部分 | 沙箱文档 |
| **Hooks** | [agent/hooks](https://cursor.com/docs/agent/hooks) | ✅ | cursor-Hooks与终端沙箱.md |

### 2. 上下文系统

| 功能 | 官方文档 | 本工程覆盖 | 说明 |
|------|----------|:----------:|------|
| **Rules 规则** | [context/rules](https://cursor.com/docs/context/rules) | ✅ 详细 | 02.CursorRuleProject |
| **Commands 命令** | [context/commands](https://cursor.com/docs/context/commands) | ✅ | 01 模板 |
| **Skills 技能** | [context/skills](https://cursor.com/docs/context/skills) | ✅ 详细 | 04.CursorSkillProject |
| **SubAgents 子代理** | [context/subagents](https://cursor.com/docs/context/subagents) | ✅ | 05.CursorSubAgentProject |
| **语义搜索** | [context/semantic-search](https://cursor.com/docs/context/semantic-search) | 部分 | cursor-完整说明.md 提及 |
| **@ Mentions** | [context/mentions](https://cursor.com/docs/context/mentions) | ✅ | cursor-完整说明.md |
| **MCP** | [context/mcp](https://cursor.com/docs/context/mcp) | ✅ 详细 | 06.CursorMCPProject |
| **Plugins** | [plugins](https://cursor.com/docs/plugins) | — | v2.5 新增插件市场 |

### 3. 独立功能

| 功能 | 官方文档 | 本工程覆盖 | 说明 |
|------|----------|:----------:|------|
| **Tab（AI 自动补全）** | [tab/overview](https://cursor.com/docs/tab/overview) | ✅ | cursor-实战Cookbook.md |
| **Cloud Agent（云端代理）** | [cloud-agent](https://cursor.com/docs/cloud-agent) | ✅ | 本文 + Cookbook |
| **CLI（命令行工具）** | [cli/overview](https://cursor.com/docs/cli/overview) | ✅ | 本文详解 |
| **Inline Edit（内联编辑）** | [inline-edit/overview](https://cursor.com/docs/inline-edit/overview) | — | 选中代码直接编辑 |
| **BugBot（PR 审查机器人）** | [bugbot](https://cursor.com/docs/bugbot) | ✅ | 本文 + Cookbook 规则模板 |
| **Shared Transcripts** | [shared-transcripts](https://cursor.com/docs/shared-transcripts) | — | 分享对话记录 |

### 4. 集成

| 功能 | 官方文档 | 本工程覆盖 | 说明 |
|------|----------|:----------:|------|
| **Slack 集成** | [integrations/slack](https://cursor.com/docs/integrations/slack) | — | 在 Slack 触发 Agent |
| **Linear 集成** | [integrations/linear](https://cursor.com/docs/integrations/linear) | — | Issue 关联 |
| **GitHub 集成** | [integrations/github](https://cursor.com/docs/integrations/github) | 部分 | MCP 已覆盖 |
| **Git 集成** | [integrations/git](https://cursor.com/docs/integrations/git) | — | 版本控制增强 |
| **GitLab 集成** | [integrations/gitlab](https://cursor.com/docs/integrations/gitlab) | — | GitLab PR/MR |
| **Cursor Blame** | [integrations/cursor-blame](https://cursor.com/docs/integrations/cursor-blame) | — | AI 增强的 git blame |

### 5. 配置

| 功能 | 官方文档 | 本工程覆盖 | 说明 |
|------|----------|:----------:|------|
| **Ignore Files** | [context/ignore-files](https://cursor.com/docs/context/ignore-files) | ✅ | cursor-完整说明.md |
| **Extensions** | [configuration/extensions](https://cursor.com/docs/configuration/extensions) | — | VS Code 扩展兼容 |
| **快捷键** | [configuration/kbd](https://cursor.com/docs/configuration/kbd) | 部分 | cursor-完整说明.md 提及 |
| **主题** | [configuration/themes](https://cursor.com/docs/configuration/themes) | — | 外观定制 |
| **Shell 配置** | [configuration/shell](https://cursor.com/docs/configuration/shell) | — | 终端 shell 设置 |
| **Worktrees** | [configuration/worktrees](https://cursor.com/docs/configuration/worktrees) | ✅ | cursor-实战Cookbook.md |
| **API Keys / BYOK** | [settings/api-keys](https://cursor.com/docs/settings/api-keys) | — | 自带 API Key |
| **语言配置** | [configuration/languages/*](https://cursor.com/docs/configuration/languages/python) | — | Python/JS/TS/Swift/Java |

### 6. Cookbook（最佳实践）

| 主题 | 官方文档 | 本工程覆盖 |
|------|----------|:----------:|
| Agent 工作流 | [cookbook/agent-workflows](https://cursor.com/docs/cookbook/agent-workflows) | ✅ | cursor-实战Cookbook.md |
| 构建 MCP 服务器 | [cookbook/building-mcp-server](https://cursor.com/docs/cookbook/building-mcp-server) | — |
| Web 开发 | [cookbook/web-development](https://cursor.com/docs/cookbook/web-development) | — |
| 数据科学 | [cookbook/data-science](https://cursor.com/docs/cookbook/data-science) | — |
| 大型代码库 | [cookbook/large-codebases](https://cursor.com/docs/cookbook/large-codebases) | — |
| Mermaid 图表 | [cookbook/mermaid-diagrams](https://cursor.com/docs/cookbook/mermaid-diagrams) | ✅ | cursor-实战Cookbook.md |
| BugBot 规则 | [cookbook/bugbot-rules](https://cursor.com/docs/cookbook/bugbot-rules) | ✅ | cursor-实战Cookbook.md |

---

## 二、Agent 四大模式详解

Cursor Agent 提供 4 种模式，各有适用场景。快捷键 `Cmd+.`（Mac）或 `Ctrl+.`（Linux/Win）快速切换。

| 模式 | 适用场景 | 能力 | 工具 |
|------|----------|------|------|
| **Agent** | 复杂功能、重构 | 自主探索、多文件编辑 | 全部工具 |
| **Ask** | 学习、提问、理解代码 | 只读探索，不做修改 | 仅搜索工具 |
| **Plan** | 需要规划的复杂任务 | 先制定方案，问澄清问题，再执行 | 全部工具 |
| **Debug** | 难以复现的 bug、回归 | 假设生成、日志插桩、运行时分析 | 全部 + Debug Server |

### Agent 模式（默认）

默认模式，自主探索代码库、编辑文件、执行命令、修复错误。

### Ask 模式

只读模式，搜索代码回答问题，不做任何改动。适合理解代码后再动手修改。

### Plan 模式

先调研代码库、问澄清问题、生成可审查的实施方案，确认后再构建。适合：
- 架构决策需要先评审方案
- 需求不明确需要先探索
- 涉及多文件/系统的大改动
- 有多种方案需要权衡

按 `Shift+Tab` 从聊天输入框切到 Plan 模式。方案默认保存在 home 目录，可点「Save to workspace」存到工作区。

### Debug 模式

帮你定位根因并修复棘手 bug。流程：
1. 探索相关文件，生成多个假设
2. 添加日志插桩，发送数据到本地 Debug Server
3. 要求你重现 bug
4. 分析日志，基于运行时证据定位根因
5. 做精准修复（通常只改几行）
6. 清理所有插桩代码

适合：回归问题、性能/内存泄漏、竞态条件、可复现但原因不明的 bug。

---

## 三、Cloud Agent（云端代理）详解

Cloud Agent（原 Background Agent）在云端隔离环境中运行，不占用本机资源。

### 核心优势

- 可**并行运行**多个 Agent
- 不需要本地机器保持在线
- 拥有自己的虚拟机，可构建、测试、控制浏览器

### 触发方式

| 入口 | 方式 |
|------|------|
| **Cursor Desktop** | 聊天下拉选 Cloud |
| **Cursor Web** | [cursor.com/agents](https://cursor.com/agents) |
| **CLI** | `agent -c "你的任务"` 或对话中输入 `& 你的任务` |
| **Slack** | @cursor 命令 |
| **GitHub** | 在 PR/Issue 中评论 `@cursor` |
| **Linear** | @cursor 命令 |
| **API** | 通过 API 接口 |

### 工作原理

1. 从 GitHub/GitLab 克隆仓库
2. 在独立分支上工作
3. 完成后推送变更供你审查

### 移动端使用

打开 [cursor.com/agents](https://cursor.com/agents)，iOS 通过 Safari「添加到主屏幕」，Android 通过 Chrome「安装应用」。

---

## 四、CLI（命令行工具）详解

Cursor CLI 让你在终端中直接与 Agent 交互。

### 安装

```bash
# macOS / Linux / WSL
curl https://cursor.com/install -fsS | bash

# Windows PowerShell
irm 'https://cursor.com/install?win32=true' | iex
```

### 使用模式

```bash
# 交互模式
agent
agent "重构认证模块为 JWT"

# 非交互模式（CI/脚本）
agent -p "查找并修复性能问题" --model "gpt-5.2"

# 切换到 Cloud Agent
agent -c "重构模块并添加测试"
```

### 模式切换

| 模式 | 切换方式 |
|------|----------|
| Agent（默认）| 无需参数 |
| Plan | `Shift+Tab` / `/plan` / `--plan` / `--mode=plan` |
| Ask | `/ask` / `--mode=ask` |

### 会话管理

```bash
agent ls          # 列出所有对话
agent resume      # 恢复最近对话
agent --continue  # 继续上一个会话
```

### CLI Cookbook

| 场景 | 命令 |
|------|------|
| 代码审查 | `agent -p "review these changes"` |
| 更新文档 | `agent -p "update docs for recent changes"` |
| 修复 CI | `agent -p "fix failing CI pipeline"` |
| 密钥审计 | `agent -p "audit for leaked secrets"` |
| 翻译键 | `agent -p "translate i18n keys"` |

---

## 五、BugBot（PR 审查机器人）详解

BugBot 自动审查 PR，识别 bug、安全问题和代码质量问题。

### 核心功能

- 分析 PR diff，留下带修复建议的评论
- 每次 PR 更新自动运行，也可手动触发（评论 `cursor review` 或 `bugbot run`）
- 读取已有的 PR 评论作为上下文，避免重复建议
- **Autofix**：自动生成 Cloud Agent 修复 bug

### 支持平台

- GitHub.com / GitHub Enterprise Server
- GitLab.com / GitLab Self-Hosted

### 配置规则（.cursor/BUGBOT.md）

在项目中创建 `.cursor/BUGBOT.md` 提供审查上下文。支持按目录嵌套：

```
project/
  .cursor/BUGBOT.md          # 项目级规则（始终包含）
  backend/
    .cursor/BUGBOT.md        # 审查后端文件时包含
  frontend/
    .cursor/BUGBOT.md        # 审查前端文件时包含
```

### 规则示例

**安全：禁止使用 eval/exec**
```text
If any changed file contains /\beval\s*\(|\bexec\s*\(/i, then:
- Add a blocking Bug "Dangerous dynamic execution"
- Apply label "security"
```

**质量：后端改动必须有测试**
```text
If the PR modifies files in {server/**, api/**, backend/**}
and there are no changes in {**/*.test.*, tests/**}, then:
- Add a blocking Bug "Missing tests for backend changes"
```

### 定价

- **免费版**：每用户每月有限次 PR 审查
- **Pro 版**：$40/月/用户，无限审查（最高 200 PR/月/许可证）

---

## 六、Hooks（Agent 事件钩子）

Hooks 让你在 Agent 执行特定动作时自动触发自定义脚本。

| 钩子类型 | 触发时机 |
|----------|----------|
| **pre-file-edit** | Agent 编辑文件之前 |
| **post-file-edit** | Agent 编辑文件之后 |
| **pre-command** | Agent 执行终端命令之前 |
| **post-command** | Agent 执行终端命令之后 |

用途：自动格式化、lint 检查、自动运行测试、通知等。

---

## 七、Plugins（插件市场）

v2.5 新增插件市场，提供预构建插件：

- AWS、Figma、Linear、Stripe 等官方插件
- 一键安装，无需手动配置 MCP
- 插件可提供工具、上下文、认证等能力

---

## 八、集成与工作流

### Slack 集成
在 Slack 中 @cursor 触发 Cloud Agent，无需打开编辑器即可创建 PR。

### Linear 集成
从 Linear Issue 直接关联 Cursor Agent 任务。

### GitHub 集成
- 在 PR/Issue 评论 `@cursor` 启动 Cloud Agent
- BugBot 自动审查 PR
- Cursor Blame 查看代码演化时间线

### Worktrees
多工作树并行开发，最多 8 个 Agent 同时运行，各自隔离文件系统。

### Cursor Blame
AI 增强的 git blame，展示代码演化时间线，关联到 Issue 和 PR。

---

## 九、待补充内容优先级

| 优先级 | 领域 | 状态 | 说明 |
|--------|------|:----:|------|
| ~~高~~ | ~~Cloud Agent 实战~~ | ✅ | cursor-功能全景图.md + cursor-实战Cookbook.md |
| ~~高~~ | ~~CLI 教程~~ | ✅ | cursor-功能全景图.md |
| 高 | Plugins 目录 | — | 跟进 v2.5 插件市场，整理可用插件 |
| ~~中~~ | ~~BugBot 规则模板~~ | ✅ | cursor-实战Cookbook.md + BUGBOT.md.example |
| ~~中~~ | ~~Hooks 实战~~ | ✅ | cursor-Hooks与终端沙箱.md + hooks.json.example |
| ~~中~~ | ~~Cookbook 翻译~~ | ✅ | cursor-实战Cookbook.md |
| ~~低~~ | ~~Tab 补全配置~~ | ✅ | cursor-实战Cookbook.md |
| 中 | 语言专项配置 | — | Python/JS/TS/Swift/Java 专项优化 |
| 中 | 构建 MCP 服务器 | — | 开发自定义 MCP 教程 |
| 低 | Web/数据科学 Cookbook | — | 官方 Web Dev/Data Science Cookbook 翻译 |
| 低 | Inline Edit 详解 | — | 内联编辑功能专项 |
| 低 | 集成（Slack/Linear/GitLab）| — | 详细配置指南 |

---

*基于 Cursor 官方文档（2026 年 2 月）整理，如有更新以官方文档为准。*
