# Cursor MCP Feedback Enhanced 完整配置指南

> 本指南帮助你在 Cursor IDE 中配置 mcp-feedback-enhanced 工具，实现 AI 对话中的持续反馈交互机制，并包含断线降级策略。

## 目录

1. [概述](#1-概述)
2. [环境要求](#2-环境要求)
3. [安装 mcp-feedback-enhanced](#3-安装-mcp-feedback-enhanced)
4. [配置 MCP 服务器](#4-配置-mcp-服务器)
5. [配置 Cursor 规则](#5-配置-cursor-规则)
6. [配置 User Rule](#6-配置-user-rule)
7. [验证配置](#7-验证配置)
8. [常见问题与排查](#8-常见问题与排查)

---

## 1. 概述

### 什么是 mcp-feedback-enhanced？

`mcp-feedback-enhanced` 是一个 MCP（Model Context Protocol）服务器工具，提供 Web UI 界面让用户在 AI 辅助开发过程中与 AI 进行交互反馈。

### 核心价值

- **持续对话**：AI 完成任务后不会直接结束，而是通过反馈界面询问你是否满意
- **方案选择**：当有多个方案时，通过界面让你选择
- **降级保障**：当 MCP 连接断开时，自动降级到 Cursor 内置的 AskQuestion 工具维持对话

### 工具使用策略（请求消耗优化版）

```
中间交互过程：AskQuestion（不消耗额外请求）
    ↓
任务最终完成：interactive_feedback（体验最佳，仅调用一次）
    ↓ 如果断开
降级备选：AskQuestion（稳定，不依赖 MCP）
```

### Cursor MCP 超时限制

> **重要**：Cursor IDE 对 MCP 工具调用有硬编码超时限制（约 2 分钟），无法配置。
> 因此中间交互应优先使用 AskQuestion，仅在最终确认时使用 interactive_feedback。

---

## 2. 环境要求

| 项目 | 要求 |
|------|------|
| 操作系统 | Windows 10/11 |
| Cursor | 最新版本 |
| Python | 3.10+ （Windows 本地安装） |
| 网络 | 需要 pip 可访问 |

### 关于 WSL 的说明

> **重要**：不建议在 WSL 中运行 mcp-feedback-enhanced。
> 
> 原因：WSL 的 Windows 互操作（binfmt_misc WSLInterop）在启用 `systemd=true` 后可能失效，导致 WSL 内无法调用 `cmd.exe` 打开 Windows 浏览器，反馈页面无法自动弹出。
> 
> **推荐方案**：在 Windows 本地安装并运行 mcp-feedback-enhanced。

---

## 3. 安装 mcp-feedback-enhanced

### 3.1 创建 Windows 虚拟环境

```powershell
# 创建专用虚拟环境
python -m venv C:\Users\<你的用户名>\.mcp-feedback-venv-win
```

### 3.2 安装 mcp-feedback-enhanced

```powershell
# 使用国内源安装（推荐）
C:\Users\<你的用户名>\.mcp-feedback-venv-win\Scripts\pip install mcp-feedback-enhanced -i https://pypi.tuna.tsinghua.edu.cn/simple

# 或使用默认源
C:\Users\<你的用户名>\.mcp-feedback-venv-win\Scripts\pip install mcp-feedback-enhanced
```

### 3.3 验证安装

```powershell
# 确认安装成功
C:\Users\<你的用户名>\.mcp-feedback-venv-win\Scripts\pip show mcp-feedback-enhanced
```

确认输出中包含 `Name: mcp-feedback-enhanced` 和版本号。

---

## 4. 配置 MCP 服务器

### 4.1 编辑 mcp.json

文件路径：`C:\Users\<你的用户名>\.cursor\mcp.json`

在 `mcpServers` 中添加以下配置：

```json
{
  "mcpServers": {
    "mcp-feedback-enhanced": {
      "command": "C:\\Users\\<你的用户名>\\.mcp-feedback-venv-win\\Scripts\\mcp-feedback-enhanced.exe",
      "args": ["server"],
      "timeout": 86400,
      "autoApprove": ["interactive_feedback"]
    }
  }
}
```

### 配置说明

| 字段 | 说明 |
|------|------|
| `command` | mcp-feedback-enhanced 可执行文件的完整路径 |
| `args` | 启动参数，`["server"]` 表示以服务器模式运行 |
| `timeout` | MCP 连接超时时间（秒），设为 86400 = 24 小时 |
| `autoApprove` | 自动批准的工具列表，无需每次手动确认 |

### 4.2 重启 MCP 服务器

配置完成后，需要重启才能生效：

- **方法 1**（推荐）：按 `Ctrl+Shift+P` → 输入 `Reload Window` → 回车
- **方法 2**：关闭并重新打开 Cursor
- **方法 3**：打开 Cursor Settings → MCP → 找到 mcp-feedback-enhanced → 点击重启按钮

---

## 5. 配置 Cursor 规则

### 5.1 规则配置层级

Cursor 支持两个层级的规则：

| 层级 | 文件路径 | 作用范围 |
|------|----------|----------|
| **全局用户级** | `C:\Users\<用户名>\.cursor\rules\*.mdc` | 所有项目 |
| **项目级** | `<项目目录>\.cursor\rules\*.mdc` | 当前项目 |

### 5.2 创建全局用户级规则（推荐，所有项目自动生效）

文件路径：`C:\Users\<你的用户名>\.cursor\rules\global-mcp-feedback.mdc`

```markdown
---
description: 每次对话自动启用反馈交互机制，优先使用 AskQuestion 以节省请求消耗，仅在最终完成时使用 interactive_feedback
alwaysApply: true
---

# 反馈交互规则（请求消耗优化版）

## 核心原则

**每次对话都必须通过交互工具与用户保持持续沟通，禁止单方面结束对话。**

## 工具选择策略（请求消耗优化）

为减少 API 请求消耗，采用以下策略：

| 场景 | 使用工具 | 原因 |
|------|----------|------|
| 中间过程确认/选择 | **AskQuestion** | 内置工具，不产生额外请求 |
| 需要用户澄清/提问 | **AskQuestion** | 内置工具，不产生额外请求 |
| 方案选择 | **AskQuestion** | 内置工具，不产生额外请求 |
| 报告进度 | **AskQuestion** | 内置工具，不产生额外请求 |
| 任务最终完成确认 | **interactive_feedback** | 支持自由文本，体验最佳 |
| interactive_feedback 断开时 | **AskQuestion** | 降级备选 |

### 关键规则

1. **整个会话过程中，尽量使用 AskQuestion** 进行所有中间交互
2. **仅在用户明确说"完成"之前的最后一轮**调用 `interactive_feedback`
3. 如果 `interactive_feedback` 失败，降级到 `AskQuestion` 完成最终确认
4. 用户说"等一下"/"稍后"/"我先离开"时，**不要**调用 `interactive_feedback`（避免超时浪费请求）

## Cursor MCP 超时限制说明

> **重要**：Cursor IDE 对 MCP 工具调用有硬编码超时限制（约 2 分钟），无法通过配置延长。
> 如果 `interactive_feedback` 等待超过 2 分钟未收到用户回复，将自动超时断开并触发新的请求。
> 这就是为什么中间交互应优先使用 `AskQuestion`（不受此限制）。

## 必须调用交互工具的场景

- 任务完成（无论成功或失败）→ 优先 `interactive_feedback`，失败则 `AskQuestion`
- 给出多个方案供用户选择 → `AskQuestion`
- 需要用户澄清或提问 → `AskQuestion`
- 判断无需操作时，说明原因并确认 → `AskQuestion`
- 遇到错误需要用户决策 → `AskQuestion`

## 工作流程

### 正常流程

1. 执行用户请求的任务
2. 中间需要确认时 → 使用 `AskQuestion`
3. 任务全部完成时 → 调用 `interactive_feedback` 做最终确认
4. 根据反馈内容决定下一步：
   - 用户说"完成"/"可以了"/"结束" → 结束对话
   - 用户提出新需求 → 继续执行，中间用 `AskQuestion`，完成后再用 `interactive_feedback`

### 降级与恢复流程（双向切换）

**interactive_feedback 不可用时 → 降级到 AskQuestion：**
1. 直接使用 `AskQuestion` 完成确认
2. 在选项中提供「尝试重新连接 mcp-feedback-enhanced」选项
3. 如果用户选择重连，尝试再次调用 `interactive_feedback`

**AskQuestion 异常结束时 → 切换到 interactive_feedback：**
1. 当 `AskQuestion` 被跳过或异常返回后，AI 立即恢复控制
2. 立即尝试调用 `interactive_feedback` 继续交互
3. 如果 `interactive_feedback` 也失败，再次降级到 `AskQuestion`
4. 循环直到成功建立交互或用户手动发送消息

**双向切换链：**
```
AskQuestion（异常）→ interactive_feedback → 如果也失败 → AskQuestion → ...
interactive_feedback（超时）→ AskQuestion → 如果也异常 → interactive_feedback → ...
```

## 禁止行为

- **禁止**在会话中直接结束对话或输出最终结果后停止
- **禁止**在交互工具可用时直接在对话中提问等待回复
- **禁止**输出结果后不调用任何交互工具
- **禁止**擅自判断任务已完成而结束反馈循环
- **禁止**擅自开启新 Agent 会话
- **禁止**用户明确表示暂时离开时调用 interactive_feedback（会导致超时浪费请求）

## 重要提醒

- 必须实际调用工具，不能只是文字描述要调用
- 循环直到用户明确说"完成"/"可以了"/"结束"
- **中间交互用 AskQuestion，最终确认用 interactive_feedback**
- 优先级：`AskQuestion`（中间）→ `interactive_feedback`（最终）→ `AskQuestion`（降级）
```

### 5.3 创建项目级规则（可选，覆盖到特定项目）

文件路径：`<项目目录>\.cursor\rules\mcp-feedback-enhanced.mdc`

内容与 5.2 完全相同。如果已配置全局用户级规则，项目级规则可以省略。

---

## 6. 配置 User Rule

### 6.1 打开 User Rule 设置

1. 按 `Ctrl+Shift+J` 打开 Cursor Settings
2. 导航到 **General** → **Rules for AI**

### 6.2 推荐 User Rule 文本

将以下内容粘贴到 Rules for AI 输入框中：

```
Always respond in 中文，Always fix code automatically. 
任何时候执行python脚本都在虚拟环境下执行，如果执行pip命令安装依赖包，请使用国内源。
每次对话都必须使用交互工具与我保持沟通，不得单方面终止会话。
中间过程的确认、提问、方案选择一律使用 AskQuestion 工具（节省请求消耗）。
仅在任务最终完成时调用 mcp-feedback-enhanced 的 interactive_feedback 做最终确认。
如果 interactive_feedback 失败或断开，降级使用 AskQuestion 维持对话。
在完成任务后，通过交互工具询问我是否满意，我可能会给出新的要求，你需要根据反馈持续改进，直到我明确说"完成"为止。
```

> **注意**：User Rule 提供简短的全局指示，详细的规则由 .mdc 文件提供。两者配合使用，双重保障。
> 
> **请求消耗优化**：AskQuestion 是 Cursor 内置工具，不产生额外 API 请求；interactive_feedback 是 MCP 工具，超时会触发新请求。因此中间过程用 AskQuestion，最终确认用 interactive_feedback。

---

## 7. 验证配置

### 7.1 验证 MCP 服务器

1. 重启 Cursor（`Ctrl+Shift+P` → `Reload Window`）
2. 打开 Cursor Settings → MCP
3. 确认 `mcp-feedback-enhanced` 状态为 **Running**（绿色）

### 7.2 验证反馈功能

在 Cursor Agent 模式中发送任意指令，例如：

```
请使用 mcp-feedback-enhanced 测试反馈功能
```

预期结果：
- AI 执行任务后，浏览器自动弹出反馈 Web UI
- 你可以在 Web UI 中输入反馈或确认满意
- AI 根据你的反馈继续操作或结束

### 7.3 验证降级机制

如果 mcp-feedback-enhanced 连接断开：
- AI 应自动切换到 AskQuestion 工具（弹出多选题弹窗）
- 选项中包含「尝试重新连接 mcp-feedback-enhanced」
- 选择重连后，AI 尝试恢复 interactive_feedback

---

## 8. 常见问题与排查

### Q1: 反馈页面没有自动弹出

**可能原因**：
- MCP 服务器在 WSL 中运行，WSL 互操作不可用

**解决方案**：
- 改用 Windows 本地 Python 运行（参见第 3 节）

### Q2: MCP 服务器状态显示红色/未运行

**排查步骤**：
1. 检查 `mcp.json` 中的路径是否正确
2. 确认 `mcp-feedback-enhanced.exe` 文件存在
3. 在终端手动运行测试：
   ```powershell
   C:\Users\<用户名>\.mcp-feedback-venv-win\Scripts\mcp-feedback-enhanced.exe server
   ```
4. 重启 Cursor

### Q3: 对话中断、AI 直接结束不询问

**可能原因**：
- 规则文件未正确加载
- `alwaysApply: true` 未设置

**排查步骤**：
1. 确认 `.mdc` 文件存在且格式正确
2. 确认文件头部包含 `alwaysApply: true`
3. 重启 Cursor 重新加载规则

### Q4: AskQuestion 降级时只有选择题，无法输入自由文本

**这是预期行为**：
- `AskQuestion` 是 Cursor 内置工具，仅支持多选题
- 如果需要输入自由文本，请在选项中选择"继续，我有新的需求"，然后在聊天输入框中输入

### Q5: 如何升级 mcp-feedback-enhanced？

```powershell
C:\Users\<用户名>\.mcp-feedback-venv-win\Scripts\pip install --upgrade mcp-feedback-enhanced -i https://pypi.tuna.tsinghua.edu.cn/simple
```

升级后重启 Cursor 生效。

---

## 附录

### A. 配置文件清单

| 文件 | 路径 | 用途 |
|------|------|------|
| MCP 服务器配置 | `C:\Users\<用户名>\.cursor\mcp.json` | 定义 MCP 服务器连接 |
| 全局规则文件 | `C:\Users\<用户名>\.cursor\rules\global-mcp-feedback.mdc` | 全局 AI 行为规则 |
| 项目规则文件 | `<项目>\.cursor\rules\mcp-feedback-enhanced.mdc` | 项目级 AI 行为规则 |
| User Rule | Cursor Settings → General → Rules for AI | 全局简短指示 |
| 虚拟环境 | `C:\Users\<用户名>\.mcp-feedback-venv-win\` | Python 虚拟环境 |

### B. 关键版本信息

| 组件 | 推荐版本 |
|------|----------|
| mcp-feedback-enhanced | >= 2.6.0 |
| Python | >= 3.10 |
| Cursor | 最新稳定版 |
