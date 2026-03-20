# MCP Feedback 超时方案

> 来源：[飞书文档](https://thundersoft.feishu.cn/docx/CoshdCQAhoDzmpxME4McjIfznnb)
> 下载时间：2026-03-18

---

## Cursor MCP Feedback 插件 — 超时解决方案与安装指南

### 核心价值

解决 Cursor IDE 中 MCP 工具调用超时问题，将 `interactive_feedback` 的可用等待时间提升到**无限**，且几乎不污染上下文。

---

## 四层超时与解决方案

| 层级 | 位置 | 默认值 | 解决方案 |
|------|------|--------|----------|
| **L1** 服务端等待 | `interactive_feedback(timeout=)` | 600s | 规则强制传 86400（24h） |
| **L2** Cursor 连接超时 | `settings.json` `mcp.server.timeout` | 60-120s | 配置 86400000（24h） |
| **L3** Cursor 工具执行硬上限 | Cursor 内部不可配置 | ~3600s | 内置自动定时提交 + AI 自动重调 |
| **L4** 传输层空闲超时 | MCP SDK transport | ~3600s | 修改 feedback 源代码，添加 `report_progress` 心跳保活 |

---

## L3 解决方案：内置自动定时提交

Cursor 有不可配置的约 1 小时工具执行硬上限。利用 mcp-feedback-enhanced 内置的「自动定时提交」功能绕过：

### 一次性配置

1. 先让 Cursor 调用一次 MCP（提示词：调用一次 mcp-feedback-enhanced mcp 工具），然后在 MCP 画面上配置

2. 打开 Web UI 设置面板（齿轮图标）

   ![设置面板](img_01_settings_panel.jpg)

3. 在「自动定时提交」区域：
   - 启用自动提交开关
   - 设置倒计时为 **3000 秒**（50 分钟）
   - 创建自定义提示词，内容为 `[AUTO_RECALL]`

   ![自动提交配置](img_02_auto_submit_config.png)

4. 选择该提示词作为自动提交提示词

   ![选择提示词](img_03_select_prompt.png)

5. **只需配置一次**

### 工作原理

1. 用户未在 50 分钟内提交 → Web UI 自动提交 `[AUTO_RECALL]`
2. AI 识别后立即重新调用 `interactive_feedback`（规则已配置）
3. Web UI 保持运行，用户无感知
4. 循环重调直到用户提交实际反馈，等待时间无上限
5. 每次重调仅消耗约 **14 token**，上下文污染极低

---

## 安装步骤

### 1. 放置插件

将 `cursor-feedback-protocol/` 目录放入：`~/.cursor/plugins/local/`

### 2. 配置超时（L2）（重要）

按 `Ctrl+Shift+P` → `Open Settings (JSON)` → 添加：

```json
"mcp.server.timeout": 86400000,
"mcp.elicitation.timeout": 86400000
```

值为毫秒，86400000 = 24 小时。

### 3. 配置 User Rule

在 Cursor Settings → Rules, Skills, SubAgents 中添加核心交互协议（见插件 README）。

#### 核心交互协议 (Critical Interaction Protocol)

- 在每次对话结束前调用反馈工具。
- 执行完任务前必须调用 `AskQuestion` 工具交由用户判断是否需要结束对话。
- 如果需求或指令不清楚，请使用 `AskQuestion` 工具向用户提问以澄清问题，不要做假设。
- 尽可能通过 `AskQuestion` 工具为用户提供预定义选项（2~6个，中文，简洁明了），以便快速决策。
- 任务最终完成时，**MUST** 优先调用 `mcp-feedback-enhanced` 的 `interactive_feedback` 做最终确认；若失败或断开，立即降级到 `AskQuestion` 维持对话。
- 只有用户明确说出"结束"，才可以结束调用这个工具，否则必须再次调用工具。
- 禁止未调用交互工具就结束对话，禁止对不明确需求直接假设执行。

### 4. 重启 Cursor

`Ctrl+Shift+P` → `Reload Window`

### 5. 配置自动定时提交（可选，突破1小时限制）

见上方「L3 解决方案」章节。

---

## 测试验证结果

- **心跳保活**：`report_progress` 每 30 秒成功发送，零失败率
- **自动重调**：5 轮连续重调验证稳定，用户无感知
- **进度可视化**：Cursor UI 显示实时等待进度条

![进度条](img_04_progress_bar.png)

![测试结果](img_05_test_result.png)

---

## 插件附件

### 初始版本

- `cursor-feedback-protocol-windows.zip`
- `cursor-feedback-protocol-linux-macos.zip`

### 更新版本（添加 MCP 间歇性不可用重试机制）

> 规则中添加 MCP 间歇性不可用（Cursor 存在已知 bug：`CallMcpTool` 偶尔报 "Tool not found" 错误，通常 1-2 次重试即可恢复）的重试机制

- `cursor-feedback-protocol-linux-macos-20260320_164803.zip`
- `cursor-feedback-protocol-windows-20260320_164803.zip`
