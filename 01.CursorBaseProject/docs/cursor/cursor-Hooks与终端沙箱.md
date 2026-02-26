# Cursor Hooks 与终端沙箱配置

> 基于 [Cursor 官方文档](https://cursor.com/docs/agent/hooks) 整理的 Hooks 事件钩子和终端沙箱安全配置。

---

## 一、Hooks 事件钩子

Hooks 让你用自定义脚本观察、控制和扩展 Agent 循环。通过 stdin/stdout 的 JSON 通信。

### 能力总览

- 会话开始时注入上下文
- 控制子代理（Task tool）执行
- 拦截高风险操作（如 SQL 写入）
- 扫描 PII 或密钥泄露
- 添加事件分析
- 编辑后自动格式化

### Hook 事件列表

#### Agent 事件

| 事件 | 触发时机 |
|------|----------|
| `sessionStart` | Agent 会话开始 |
| `sessionEnd` | Agent 会话结束 |
| `beforeSubmitPrompt` | 提交提示词之前 |
| `afterAgentResponse` | Agent 返回响应后 |
| `afterAgentThought` | Agent 思考过程后 |
| `stop` | Agent 完成时（可返回 followup 继续循环） |
| `preCompact` | 上下文窗口压缩前 |

#### 文件操作事件

| 事件 | 触发时机 |
|------|----------|
| `beforeReadFile` | 读取文件之前 |
| `afterFileEdit` | 编辑文件之后 |

#### 终端事件

| 事件 | 触发时机 |
|------|----------|
| `beforeShellExecution` | 执行 shell 命令之前 |
| `afterShellExecution` | 执行 shell 命令之后 |

#### MCP 事件

| 事件 | 触发时机 |
|------|----------|
| `beforeMCPExecution` | 调用 MCP 工具之前 |
| `afterMCPExecution` | 调用 MCP 工具之后 |

#### 子代理事件

| 事件 | 触发时机 |
|------|----------|
| `subagentStart` | 子代理启动 |
| `subagentStop` | 子代理完成 |

#### 通用工具事件

| 事件 | 触发时机 |
|------|----------|
| `preToolUse` | 任何工具调用之前 |
| `postToolUse` | 任何工具调用之后 |
| `postToolUseFailure` | 工具调用失败后 |

#### Tab 专用事件

| 事件 | 触发时机 |
|------|----------|
| `beforeTabFileRead` | Tab 补全读取文件之前 |
| `afterTabFileEdit` | Tab 补全编辑文件之后 |

### 快速入门

#### 项目级 Hook

创建 `.cursor/hooks.json`：

```json
{
  "version": 1,
  "hooks": {
    "afterFileEdit": [{ "command": ".cursor/hooks/format.sh" }]
  }
}
```

创建 `.cursor/hooks/format.sh`：

```bash
#!/bin/bash
cat > /dev/null
exit 0
```

```bash
chmod +x .cursor/hooks/format.sh
```

重启 Cursor 后，每次文件编辑都会触发。

#### 用户级 Hook

创建 `~/.cursor/hooks.json`，脚本放在 `~/.cursor/hooks/`。

### Hook 类型

#### 命令型（默认）

```json
{
  "hooks": {
    "beforeShellExecution": [
      {
        "command": ".cursor/hooks/approve-network.sh",
        "timeout": 30,
        "matcher": "curl|wget|nc"
      }
    ]
  }
}
```

退出码含义：
- `0`：成功，使用 JSON 输出
- `2`：阻止操作（等同于 `permission: "deny"`）
- 其他：Hook 失败，操作继续（fail-open）

#### 提示词型（LLM 评估）

```json
{
  "hooks": {
    "beforeShellExecution": [
      {
        "type": "prompt",
        "prompt": "Does this command look safe to execute? Only allow read-only operations.",
        "timeout": 10
      }
    ]
  }
}
```

### 实用 Hook 示例

#### 编辑后自动格式化

```bash
#!/bin/bash
INPUT=$(cat)
FILE=$(echo "$INPUT" | jq -r '.path // empty')
[ -z "$FILE" ] && exit 0

case "$FILE" in
  *.py) black "$FILE" 2>/dev/null ;;
  *.ts|*.tsx|*.js|*.jsx) npx prettier --write "$FILE" 2>/dev/null ;;
  *.go) gofmt -w "$FILE" 2>/dev/null ;;
esac
exit 0
```

#### 阻止危险 Git 操作

```bash
#!/bin/bash
INPUT=$(cat)
CMD=$(echo "$INPUT" | jq -r '.command // empty')

if echo "$CMD" | grep -qE 'git (push --force|reset --hard|clean -fd)'; then
  echo '{"permission": "deny", "reason": "Dangerous git operation blocked"}'
  exit 2
fi
echo '{}'
exit 0
```

#### 会话开始注入上下文

```bash
#!/bin/bash
cat > /dev/null
echo "{\"context\": \"Project: $(basename $(pwd)). Branch: $(git branch --show-current 2>/dev/null || echo 'unknown')\"}"
exit 0
```

---

## 二、终端沙箱配置

Agent 默认在受限环境中运行终端命令，阻止未授权的文件访问和网络活动。

### 平台支持

| 平台 | 实现方式 | 要求 |
|------|----------|------|
| macOS | `sandbox-exec`（seatbelt） | macOS > v2.0 |
| Linux | Landlock v3 + seccomp + user namespaces | 内核 >= 6.2 |
| Windows | 需要 WSL2 | — |

### 沙箱权限

| 访问类型 | 说明 |
|----------|------|
| 文件读取 | 全文件系统可读 |
| 文件写入 | 仅工作区目录可写 |
| 网络访问 | 默认阻止，可配置 |
| 临时文件 | `/tmp/` 完全访问 |

### sandbox.json 配置

放在 `~/.cursor/sandbox.json`（全局）或 `<workspace>/.cursor/sandbox.json`（项目级，优先级更高）。

#### 仅允许特定域名

```json
{
  "networkPolicy": {
    "default": "deny",
    "allow": [
      "registry.npmjs.org",
      "pypi.org",
      "*.githubusercontent.com"
    ]
  }
}
```

#### 允许全部网络

```json
{
  "networkPolicy": {
    "default": "allow"
  }
}
```

#### 完整示例

```json
{
  "networkPolicy": {
    "default": "deny",
    "allow": [
      "registry.npmjs.org",
      "pypi.org",
      "files.pythonhosted.org",
      "*.docker.io",
      "ghcr.io",
      "*.googleapis.com"
    ],
    "deny": [
      "*.internal.corp.example.com"
    ]
  },
  "additionalReadwritePaths": [
    "/home/me/.docker"
  ],
  "additionalReadonlyPaths": [
    "/opt/shared/design-tokens"
  ],
  "enableSharedBuildCache": true
}
```

### Schema 字段说明

| 字段 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `type` | string | `"workspace_readwrite"` | `"workspace_readwrite"` / `"workspace_readonly"` / `"insecure_none"` |
| `additionalReadwritePaths` | string[] | `[]` | 额外可读写路径 |
| `additionalReadonlyPaths` | string[] | `[]` | 额外可读路径 |
| `disableTmpWrite` | boolean | `false` | 禁止 /tmp 写入 |
| `enableSharedBuildCache` | boolean | `false` | 共享 npm/cargo/pip 缓存 |

### 命令允许列表

当沙箱命令失败时，可选择：

| 选项 | 说明 |
|------|------|
| **Skip** | 取消命令，让 Agent 换方案 |
| **Run** | 不经沙箱执行这一次 |
| **Add to allowlist** | 以后都在沙箱外自动运行 |

### 受保护路径（始终写保护）

- `.cursor/*.json`、`.cursor/**/*.json`
- `.vscode/**`
- `.git/hooks/**`、`.git/config`
- `.cursorignore`

**允许写入**的 `.cursor` 子目录：`rules/`、`commands/`、`worktrees/`、`skills/`、`agents/`。

---

*基于 Cursor 官方文档（2026 年 2 月）整理。*
