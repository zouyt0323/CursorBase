# Cursor 实战 Cookbook

> 基于 [Cursor 官方 Cookbook](https://cursor.com/docs/cookbook/agent-workflows) 整理的实战工作流、最佳实践与常用模式。

---

## 一、测试驱动开发（TDD）

Agent 在有明确目标时表现最佳，测试就是这样的目标——可验证的验收标准。

### TDD 工作流

1. 让 Agent 写测试（明确说做 TDD，不要写实现）
2. 让 Agent 运行测试，确认失败
3. 确认测试满意后提交
4. 让 Agent 写代码通过测试，不修改测试，自动迭代直到全部通过
5. 提交实现

### 示例提示词

**写测试：**
```text
Write tests for a function that validates email addresses.
Expected behavior:
- "user@example.com" returns true
- "invalid-email" returns false
- Empty string returns false
Use the testing patterns in `__tests__/`. Don't implement the function yet.
```

**写实现：**
```text
Now implement the validateEmail function to pass all tests.
Don't modify the tests. Keep iterating until all tests pass.
```

---

## 二、Git 工作流 Commands

在 `.cursor/commands/` 中创建命令，用 `/` 触发。

### PR 命令

创建 `.cursor/commands/pr/COMMAND.md`：

```markdown
Create a pull request for the current changes.

1. Look at the staged and unstaged changes with `git diff`
2. Write a clear commit message based on what changed
3. Commit and push to the current branch
4. Use `gh pr create` to open a pull request with title/description
5. Return the PR URL when done
```

在 Agent 中输入 `/pr` 即可自动提交、推送并创建 PR。

### Fix Issue 命令

创建 `.cursor/commands/fix-issue/COMMAND.md`：

```markdown
Fix the GitHub issue specified by the user.

1. Fetch issue details with `gh issue view <number>`
2. Search the codebase to find relevant code
3. Implement a fix following existing patterns
4. Write tests if appropriate
5. Open a PR referencing the issue
```

用法：`/fix-issue 123`

### 其他实用命令

| 命令 | 用途 |
|------|------|
| `/review` | 运行 linter，检查常见问题，总结待处理事项 |
| `/update-deps` | 检查过期依赖，逐一更新，每次更新后运行测试 |
| `/docs` | 为最近改动生成或更新文档 |

---

## 三、代码库理解

把 Agent 当作一个了解代码库的同事来提问。

### 常用问题模式

- "Walk me through what happens when a user submits the login form"
- "Why are we calling `setUser()` instead of `createUser()` on line 1738?"
- "What edge cases does `CustomerOnboardingFlow` handle?"
- "How do I add a new API endpoint?"
- "How does logging work in this project?"

### 渐进式理解

从宏观到微观：

1. "Give me a high-level overview of this codebase"
2. "How does the authentication system work?"
3. "Show me the token refresh flow specifically"
4. "Why does this function check for null here?"

---

## 四、设计转代码

Agent 可以直接处理图片。截图、拖入设计文件或引用图片路径。

### 工作流

1. 粘贴设计稿到 Agent 输入框
2. Agent 匹配布局、颜色、间距
3. 要求 Agent 实现组件
4. 用浏览器侧边栏预览并迭代

### 视觉调试

截图错误状态或异常 UI，粘贴到 Agent 中。通常比用文字描述问题更快。

---

## 五、架构图生成

```text
Create a Mermaid diagram showing the data flow for our authentication system,
including OAuth providers, session management, and token refresh.
```

Agent 分析代码库后生成 Mermaid 图，适合：PR 描述、新人文档、架构审查。

---

## 六、长时间 Agent 循环（Hooks）

通过 `stop` Hook 让 Agent 持续迭代直到达成目标。

### 配置 .cursor/hooks.json

```json
{
  "version": 1,
  "hooks": {
    "stop": [{ "command": ".cursor/hooks/grind.sh" }]
  }
}
```

### Hook 脚本（bash 版）

```bash
#!/bin/bash
INPUT=$(cat)
STATUS=$(echo "$INPUT" | jq -r '.status')
LOOP=$(echo "$INPUT" | jq -r '.loop_count')
MAX=5

if [ "$STATUS" != "completed" ] || [ "$LOOP" -ge "$MAX" ]; then
  echo '{}'; exit 0
fi

if grep -q "DONE" .cursor/scratchpad.md 2>/dev/null; then
  echo '{}'; exit 0
fi

echo "{\"followup_message\": \"[Iteration $((LOOP+1))/$MAX] Continue working. Update .cursor/scratchpad.md with DONE when complete.\"}"
```

适合：运行直到测试通过、UI 匹配设计稿、任何可验证目标。

---

## 七、Cloud Agent 委派

将「待办事项级别」的任务委派给 Cloud Agent：

- 更新文档
- 为现有代码生成测试
- 最近代码变更的重构
- 处理过程中发现的 bug

从 [cursor.com/agents](https://cursor.com/agents)、编辑器、CLI（`agent -c`）或 Slack（@Cursor）启动。

---

## 八、并行 Agent（Worktrees）

### 基本用法

1. Agent 在独立 worktree 中运行，不干扰主分支
2. 完成后点「Apply」将变更合并到本地分支

### Best-of-N：多模型比较

同一提示词发给多个模型，对比结果选最优。适合：
- 比较模型对特定代码库的效果
- 发现单一模型可能遗漏的边界情况
- 比较代码质量，选最佳方案

### 初始化脚本 `.cursor/worktrees.json`

```json
{
  "setup-worktree": [
    "npm ci",
    "cp $ROOT_WORKTREE_PATH/.env .env"
  ]
}
```

Python 项目：
```json
{
  "setup-worktree": [
    "python -m venv venv",
    "source venv/bin/activate && pip install -r requirements.txt",
    "cp $ROOT_WORKTREE_PATH/.env .env"
  ]
}
```

---

## 九、BugBot 规则模板

在 `.cursor/BUGBOT.md` 中提供审查指引：

### 安全审查
```text
If any changed file contains /\beval\s*\(|\bexec\s*\(/i, then:
- Add a blocking Bug "Dangerous dynamic execution"
- Apply label "security"
```

### 测试覆盖
```text
If the PR modifies files in {server/**, api/**, backend/**}
and there are no changes in {**/*.test.*, tests/**}, then:
- Add a blocking Bug "Missing tests for backend changes"
```

### TODO 清理
```text
If any changed file contains /(?:^|\s)(TODO|FIXME)(?:\s*:|\s+)/, then:
- Add a non-blocking Bug "TODO/FIXME comment found"
- If the TODO already references /#\d+|[A-Z]+-\d+/, mark resolved.
```

---

## 十、Tab 自动补全优化

### 核心功能

| 功能 | 说明 |
|------|------|
| 多行补全 | 基于最近编辑、linter 错误、已接受的建议 |
| 文件内跳转 | Tab 预测下一个编辑位置并建议跳转 |
| 跨文件跳转 | 底部弹出跨文件编辑建议 |
| 自动导入 | TypeScript/Python 自动补充缺失的 import |
| Peek 中使用 | 在 Go to Definition 窗口中编辑 |

### 操作方式

| 按键 | 行为 |
|------|------|
| `Tab` | 接受建议 |
| `Escape` | 拒绝建议 |
| `Cmd+→` | 逐词接受 |

### 推荐设置

- 关闭注释中的补全：`Cursor Settings → Tab → Trigger in comments` 取消勾选
- 关闭仅空白的建议：`Whitespace-Only Suggestions` 取消勾选
- 启用 Python 自动导入：`Auto Import for Python (beta)` 勾选

---

*基于 Cursor 官方 Cookbook 和文档（2026 年 2 月）整理。*
