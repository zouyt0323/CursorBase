# Cursor × 飞书集成方案

> Cursor IDE 与飞书/Lark 的集成方案——涵盖官方 Lark MCP 和手机远程控制两大核心能力。
>
> 最后更新：2026-02-28

---

## 项目定位

本项目包含两个独立的飞书集成 MCP 服务，可根据需求选择安装：

| 服务 | 用途 | 技术栈 |
|------|------|--------|
| **lark-mcp**（官方） | 通过 Cursor 读写飞书文档、多维表格、消息、日历等 | Node.js (npx) |
| **lark-feedback-mcp**（自研） | 通过飞书手机端远程控制 Cursor，实现移动办公 | Python (uv) |

---

## 文件清单

| 文件/目录 | 说明 |
|-----------|------|
| `README.md` | 本文件，安装配置完整手顺 |
| `lark-feedback-mcp/` | 自研 MCP 源码（server.py, lark_client.py, setup.py） |
| `phone-control.mdc` | 手机控制模式的 Cursor 规则文件 |

---

## 一、官方 Lark MCP 安装配置

> 飞书官方发布的 MCP 服务，支持文档读写、消息发送、多维表格操作等。
>
> 参考来源：[飞书 Wiki](https://thundersoft.feishu.cn/wiki/MmoBwPF47iai78klhcAcZ3UGn7f)

### 使用场景

- 让 Cursor 根据飞书文档要求进行编码和总结
- 根据代码信息更新飞书文档或整理新文档
- 对飞书文档、表格进行整理、计算，生成报告

### 前置依赖

- **Node.js**：[官网下载](https://nodejs.org/)
- 验证安装：

```bash
node -v
npm -v
```

### 安装步骤

**步骤 1：登录授权**

在终端执行以下命令，一分钟内点击输出的链接完成飞书授权：

```bash
npx -y @larksuiteoapi/lark-mcp login -a cli_a8fde940c6da9013 -s tcxHbJIjVPUYrS61L92hKePrsQRYHolA
```

**步骤 2：配置 Cursor MCP**

编辑 `~/.cursor/mcp.json`，在 `mcpServers` 中添加：

```json
"lark-mcp": {
    "command": "npx",
    "args": [
        "-y",
        "@larksuiteoapi/lark-mcp",
        "mcp",
        "-a",
        "cli_a8fde940c6da9013",
        "-s",
        "tcxHbJIjVPUYrS61L92hKePrsQRYHolA",
        "--oauth"
    ]
}
```

**步骤 3：验证**

重启 Cursor，在 Settings → MCP 页面看到 `lark-mcp` 状态为绿灯即配置成功。

### 使用示例

在 Cursor Agent 模式下输入：

> 帮我整理飞书上最近的会议记录中关于 AI 培训的信息，整理成 Action Item 清单，生成新文档发送给 xxx@thundersoft.com

---

## 二、Lark Feedback MCP 安装配置（手机远程控制）

> 自研 MCP 服务，通过飞书群聊实现手机远程控制 Cursor。离开电脑也能下达指令、接收结果。

### 使用场景

- 手机端通过飞书群消息控制 Cursor 执行任务
- 远程查看任务进度和结果
- 移动办公场景下的 AI 编程助手

### 前置依赖

| 依赖 | 版本 | 检查命令 | 安装方式 |
|------|------|----------|----------|
| Python | 3.11+ | `python3.11 -V` | 源码编译或 apt/deadsnakes PPA |
| uv | 最新 | `uv --version` | `curl -LsSf https://astral.sh/uv/install.sh \| sh` |
| Cursor | 支持 MCP | Settings → MCP 页面可见 | — |
| 飞书账号 | 企业/团队 | — | 个人版不支持自建应用 |

### 飞书应用权限要求

应用需在[飞书开放平台](https://open.feishu.cn) → 应用权限中开通以下权限：

| 权限 | 说明 |
|------|------|
| `im:message:send_as_bot` | 以机器人身份发送消息 |
| `im:message` | 读取群聊消息 |
| `im:chat` | 创建和管理群聊 |
| `contact:user.id:readonly` | 通过邮箱查找用户（setup.py 需要） |

应用需发布上线（至少发布到企业内部可用）。

### 安装步骤

**步骤 1：复制项目文件到工作目录**

```bash
mkdir -p ~/lark-feedback-mcp
cp -r 07.CursorLarkProject/lark-feedback-mcp/* ~/lark-feedback-mcp/
cd ~/lark-feedback-mcp
```

或直接使用仓库中的源码目录。

**步骤 2：安装依赖**

```bash
cd ~/lark-feedback-mcp
uv sync
```

**步骤 3：运行初始化脚本**

```bash
uv run python setup.py
```

脚本会提示输入飞书邮箱，然后自动完成：

1. 创建随机命名的飞书群（如 `Cursor-MCP-A3X7K2`）
2. 通过邮箱查找你的飞书账号
3. 把你邀请进群
4. 发送测试消息到群聊
5. 生成 `config.json`（含 chat_id）

**步骤 4：配置 Cursor MCP**

编辑 `~/.cursor/mcp.json`，在 `mcpServers` 中添加（将 `tsdl` 替换为你的用户名）：

```json
"lark-feedback": {
    "command": "uv",
    "args": [
        "--directory",
        "/home/tsdl/lark-feedback-mcp",
        "run",
        "server.py"
    ],
    "timeout": 600,
    "autoApprove": [
        "send_to_lark",
        "wait_for_lark_input"
    ]
}
```

> 用 `echo $HOME` 查看你的家目录路径。

**步骤 5：添加手机控制模式规则（可选）**

将 `phone-control.mdc` 复制到项目的 `.cursor/rules/` 目录下：

```bash
cp 07.CursorLarkProject/phone-control.mdc .cursor/rules/
```

**步骤 6：重启 Cursor 并验证**

重启 Cursor 后，在对话中输入「手机控制模式」即可开始。

### 备选方案（手动配置 config.json）

如果 `setup.py` 报错（如"未找到用户"），可手动配置：

1. 在飞书中新建群聊，把飞书机器人加入
2. 通过飞书 API 调试工具获取群的 `chat_id`
3. 手动创建 `~/lark-feedback-mcp/config.json`：

```json
{
    "app_id": "cli_a8fde940c6da9013",
    "app_secret": "tcxHbJIjVPUYrS61L92hKePrsQRYHolA",
    "chat_id": "你的群 chat_id"
}
```

---

## 三、多电脑使用注意事项

> 如果两台电脑要同时使用 lark-feedback-mcp，**必须使用不同的飞书群聊**（不同的 `chat_id`），否则两个 Cursor 会抢同一条消息导致混乱。

每台电脑运行一次 `setup.py` 会自动创建独立的飞书群。同一个飞书应用（`app_id`/`app_secret`）可以共用，只需不同的 `chat_id`。

---

## 四、FAQ

| 问题 | 解答 |
|------|------|
| 两台电脑可以用同一个飞书群吗？ | 不建议。每台电脑用独立飞书群，每次运行 setup.py 会创建新群。 |
| lark-feedback-mcp 需要 Node.js 吗？ | 不需要。纯 Python，只需 Python 3.11+ 和 uv。 |
| app_id / app_secret 可以共用吗？ | 可以。同一个飞书应用可发消息到不同群，只需不同 chat_id。 |
| setup.py 报「未找到邮箱对应的飞书用户」？ | 飞书应用缺少 `contact:user.id:readonly` 权限，或改用手动方式。 |
| TypeError: FastMCP() no longer accepts `log_level`？ | fastmcp 3.x 的 breaking change，确保 server.py 在 import 前设置了 `FASTMCP_LOG_LEVEL` 环境变量。 |
| DeprecationWarning: websockets.legacy？ | lark-oapi 依赖的版本提示，不影响功能，可忽略。 |

---

## 相关资源

| 资源 | 链接 |
|------|------|
| 飞书开放平台 | [open.feishu.cn](https://open.feishu.cn/) |
| Lark Developer | [open.larksuite.com](https://open.larksuite.com/) |
| 飞书 Wiki（内部） | [安装指南](https://thundersoft.feishu.cn/wiki/MmoBwPF47iai78klhcAcZ3UGn7f) |
| 中科创达 Lark MCP 安装指南 | [`06.CursorMCPProject/中科创达 Lark MCP安装指南.md`](../06.CursorMCPProject/中科创达%20Lark%20MCP安装指南.md) |

---

## License

MIT
