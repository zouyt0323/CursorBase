# 仅需40mins，即可拥有一个全能私人助理

> 来源：[飞书文档](https://thundersoft.feishu.cn/docx/QpAjdipjnoSFBhxipCOclV4Fnlh)
> 下载时间：2026-03-20

**OpenClaw + Cursor 的自动化配置手册**

> 💡 从零搭建 Cursor API Gateway（持久会话模式）、集成 OpenClaw 智能助手平台、配置飞书通道、安装 20 个 Agent Skills 的完整指南。
>
> 💡 部署完成后，你将拥有一个通过飞书即可与 Claude Opus 4.6 对话、执行编程任务、生成文档的 AI 助手。

---

## 资源下载

| 资源 | 链接 |
|------|------|
| 📄 本手册 Markdown 版本 | [setup-guide.md](setup-guide.md) |
| 📦 Linux 安装包 | [cursor-api-gateway-2.5.0-linux.tar.gz](cursor-api-gateway-2.5.0-linux.tar.gz) |
| 📦 macOS 安装包 | [cursor-api-gateway-2.5.0-macos.tar.gz](cursor-api-gateway-2.5.0-macos.tar.gz) |
| 📦 Windows 安装包 | [cursor-api-gateway-2.5.0-windows.zip](cursor-api-gateway-2.5.0-windows.zip) |

## 快速开始

1. 下载上方的 Markdown 版本手册和你系统对应的安装包
2. 完成第一部分的人工操作：申请 Cursor API Key 和创建飞书应用（约 15 分钟）
3. 打开 Cursor，将以下信息粘贴到对话框中，并附上下载的 md 手册文件：

```
请按照附件手册完成本机部署。以下是我已获取的信息：
- Cursor API Key: <粘贴你的 Key>
- 飞书 App ID: <粘贴你的 App ID>
- 飞书 App Secret: <粘贴你的 App Secret>
```

4. 等待 Cursor 自动完成剩余所有部署步骤（约 25 分钟），然后在飞书中找到你的 AI 机器人开始对话

---

## 第一部分：准备工作（人工操作）

在开始自动化部署之前，需要先完成以下人工操作，获取必要的账号和凭据。

### 1.1 申请 Cursor API Key

Cursor API Key 是网关调用 Cursor Agent CLI 的核心凭据。

**操作步骤：**

1. 访问 Cursor 官网，使用企业账号登录，确保当前账号为 Teams 账号
2. 进入 Dashboard → 点击顶部 Integrations 菜单（或直接访问 https://cursor.com/dashboard?tab=integrations）
3. 在 Integrations 页面中找到 API Keys 区域
4. 点击 **Generate New Key**
5. 复制生成的 API Key，格式类似：`key_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`

**注意事项：**
- API Key 生成后仅显示一次，请立即保存
- 必须使用 Teams 账号，个人免费账号不支持 Agent API
- 如果看不到 Integrations 菜单，请联系团队管理员确认权限

> 💡 记录下来 → 后续称为 `YOUR_CURSOR_API_KEY`

### 1.2 创建飞书应用

飞书应用用于让 OpenClaw 通过飞书机器人与用户交互。

**操作步骤：**

1. 访问 [飞书开放平台](https://open.feishu.cn)，登录开发者账号
2. 点击 **创建自建应用**
3. 填写应用名称（如「AI助手」）和描述，上传图标
4. 创建完成后，进入应用详情页，记录以下信息：
   - **App ID**：格式 `cli_xxxxxxxxxxxx`
   - **App Secret**：点击查看并复制

> 💡 记录下来 → 后续称为 `YOUR_FEISHU_APP_ID` 和 `YOUR_FEISHU_APP_SECRET`

### 1.3 配置飞书应用权限与能力

在飞书开发者后台，为应用添加必要的能力和权限。

**添加应用能力：**
1. 左侧菜单 → 添加应用能力 → 勾选 **机器人**

**配置事件订阅（长连接模式）：**
1. 左侧菜单 → 事件与回调
2. 订阅方式选择 → **使用长连接接收事件**（WebSocket 模式，无需公网 IP）
3. 添加事件 → 搜索并添加 `im.message.receive_v1`（接收消息）

**开通 API 权限：**
1. 左侧菜单 → 权限管理
2. 搜索并开通以下权限：

| 权限 | 用途 |
|------|------|
| `im:message:send_as_bot` | 机器人发消息 |
| `im:message` | 读写消息 |
| `im:message:readonly` | 读取消息 |
| `im:chat:readonly` | 读取群信息 |
| `im:resource` | 上传/下载资源 |

**发布应用：**
1. 左侧菜单 → 版本管理与发布
2. 创建新版本 → 填写更新说明 → 提交审核（自建应用通常自动通过）
3. 发布后，在飞书客户端中搜索应用名称，即可看到机器人

**获取群聊 ID（可选，用于群聊白名单）：**
1. 在飞书中创建或选择一个群
2. 将机器人添加到群中
3. 通过飞书 API 调试台发送请求获取 `chat_id`，格式 `oc_xxxxxxxxxxxx`

> 💡 记录下来 → 后续称为 `YOUR_FEISHU_CHAT_ID`

### 1.4 人工操作清单汇总

请确认以下信息已全部获取，后续步骤将基于这些输入：

| 编号 | 信息 | 来源 | 示例值 |
|------|------|------|--------|
| ① | Cursor API Key | Cursor 官网 | `csk_xxxx...` |
| ② | 飞书 App ID | 飞书开放平台 | `cli_xxxxxxxxxxxx` |
| ③ | 飞书 App Secret | 飞书开放平台 | `xxxxxxxxxxxx` |
| ④ | 飞书群聊 ID（可选） | 飞书 API | `oc_xxxxxxxxxxxx` |

---

## 第二部分：环境安装

### 2.1 安装 Python 3.10+

**Debian / Ubuntu：**

```bash
sudo apt update
sudo apt install -y python3 python3-pip python3-venv
python3 --version   # 确认 >= 3.10
```

如果系统 Python 版本低于 3.10：

```bash
sudo apt install -y software-properties-common
sudo add-apt-repository -y ppa:deadsnakes/ppa
sudo apt update
sudo apt install -y python3.11 python3.11-pip python3.11-venv
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.11 1
```

**macOS（使用 Homebrew）：**

```bash
brew install python@3.11
echo 'export PATH="/opt/homebrew/opt/python@3.11/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
python3 --version
```

**Windows：**
1. 下载 Python 3.11+
2. 安装时勾选 **Add Python to PATH**
3. 打开 PowerShell 验证：`python --version`

**安装 Python 依赖：**

```bash
pip3 install fastapi uvicorn sse-starlette pydantic httpx
```

### 2.2 安装 Node.js 18+

Node.js 是运行 OpenClaw 的必要环境。

**Debian / Ubuntu（推荐 NodeSource）：**

```bash
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt install -y nodejs
node --version    # 确认 >= 18
npm --version
```

**macOS：**

```bash
brew install node@20
echo 'export PATH="/opt/homebrew/opt/node@20/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

**Windows：**
1. 下载 Node.js LTS
2. 运行安装程序
3. 验证：`node --version && npm --version`

### 2.3 安装 Cursor Agent CLI

Cursor Agent CLI 是核心的 AI 编程工具，Gateway 通过它与 Claude 模型交互。

**macOS / Linux / WSL：**

```bash
curl https://cursor.com/install -fsS | bash
```

**Windows PowerShell：**

```powershell
irm 'https://cursor.com/install?win32=true' | iex
```

**验证安装：**

```bash
cursor-agent --version
```

> 💡 安装脚本会自动将 CLI 添加到 PATH，安装完成后可直接使用 `cursor-agent` 命令。

---

## 第三部分：Cursor API Gateway 部署

### 3.1 架构说明

```
飞书用户 ──→ 飞书Bot (WebSocket长连接)
                │
                ▼
         OpenClaw Gateway (:18789)
                │
                ▼
      Cursor API Gateway (:8080)    ← OpenAI 兼容 SSE 接口
                │
                ▼
         Cursor Agent CLI           ← 持久进程，多轮对话保持上下文
                │
                ▼
         Claude opus-4.6-thinking   ← Cursor 订阅模型
```

### 3.2 下载安装包

根据你的操作系统下载对应的安装包：

| 平台 | 安装包 | 大小 |
|------|--------|------|
| Linux | `cursor-api-gateway-2.5.0-linux.tar.gz` | ~21K |
| macOS | `cursor-api-gateway-2.5.0-macos.tar.gz` | ~20K |
| Windows | `cursor-api-gateway-2.5.0-windows.zip` | ~28K |

> 💡 安装包下载链接见文末附件

### 3.3 Linux 安装

```bash
# 解压
tar xzf cursor-api-gateway-2.5.0-linux.tar.gz
cd cursor-api-gateway

# 交互式安装（填入第一部分获取的信息）
sudo bash install.sh
# 提示输入：
#   端口号 → 8080
#   模型名 → opus-4.6-thinking
#   API Key → 填入 YOUR_CURSOR_API_KEY
#   最大并发 → 3
#   运行模式 → 2（持久模式）
```

或手动安装：

```bash
# 复制文件
sudo mkdir -p /opt/cursor-api-gateway
sudo cp -r . /opt/cursor-api-gateway/
sudo chmod +x /opt/cursor-api-gateway/run_gateway.sh

# 写入配置文件
sudo tee /etc/cursor-api-gateway.env << 'EOF'
CAG_PORT=8080
CAG_HOST=0.0.0.0
CAG_DEFAULT_MODEL=opus-4.6-thinking
CAG_MAX_CONCURRENT=3
CAG_WORKSPACE=/opt/cursor-api-gateway
CAG_WAIT_SCRIPT=/opt/cursor-api-gateway/wait_input.py
CAG_GATEWAY_SCRIPT=persistent_gateway.py
CAG_AGENT_CLI=/root/.local/bin/agent
CAG_OUTPUT_MODE=full
CURSOR_API_KEY=YOUR_CURSOR_API_KEY
EOF

# 安装 systemd 服务
sudo cp deployment/cursor-api-gateway.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable cursor-api-gateway
sudo systemctl start cursor-api-gateway
```

### 3.4 macOS 安装

```bash
tar xzf cursor-api-gateway-2.5.0-macos.tar.gz
cd cursor-api-gateway
bash install-mac.sh
# 服务通过 launchd 管理
# 配置: ~/.config/cursor-api-gateway.env
# 启动: launchctl load ~/Library/LaunchAgents/com.cursor.api-gateway.plist
```

### 3.5 Windows 安装

```powershell
# 解压 zip
Expand-Archive cursor-api-gateway-2.5.0-windows.zip -DestinationPath .
cd cursor-api-gateway
# 以管理员运行
.\install.ps1
# 服务通过 Task Scheduler 管理
# 配置: %APPDATA%\cursor-api-gateway\config.env
```

### 3.6 验证部署

```bash
# 健康检查
curl http://localhost:8080/health

# 查看活跃会话
curl http://localhost:8080/sessions

# 测试对话（替换 API Key）
curl http://localhost:8080/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_CURSOR_API_KEY" \
  -d '{
    "model": "opus-4.6-thinking",
    "messages": [{"role":"user","content":"你好，请自我介绍"}],
    "stream": true
  }'
```

### 3.7 核心配置参数

| 环境变量 | 默认值 | 说明 |
|----------|--------|------|
| `CAG_PORT` | 8080 | 监听端口 |
| `CAG_HOST` | 0.0.0.0 | 监听地址 |
| `CAG_DEFAULT_MODEL` | opus-4.6-thinking | 默认模型 |
| `CAG_MAX_CONCURRENT` | 3 | 最大并发会话 |
| `CAG_WORKSPACE` | 安装目录 | Agent 工作目录 |
| `CAG_OUTPUT_MODE` | full | 输出模式 full（全量）/ compact（精简） |
| `CAG_SESSION_IDLE_HOURS` | 10 | 会话空闲超时（小时） |
| `CURSOR_API_KEY` | 无 | 必填，第一步获取的 Key |

### 3.8 输出模式说明

| 模式 | 输出内容 | 适用场景 |
|------|----------|----------|
| full | thinking + tool_call + assistant 文本 | 调试、观察 AI 工作过程 |
| compact | 仅 assistant 文本 | 日常使用、飞书聊天 |

设置优先级：请求 Header `X-Output-Mode` > 环境变量 `CAG_OUTPUT_MODE` > 启动参数 `--output-mode`

---

## 第四部分：OpenClaw 安装与配置

### 4.1 安装 OpenClaw

```bash
npm install -g openclaw

# 验证
openclaw --version
```

### 4.2 初始化

```bash
openclaw onboard    # 交互式初始化，按提示操作
```

### 4.3 配置模型（指向 Cursor Gateway）

编辑 `/root/.openclaw/openclaw.json`，将 AI 模型指向本地 Gateway：

```json
{
  "models": {
    "mode": "merge",
    "providers": {
      "cursor": {
        "baseUrl": "http://127.0.0.1:8080/v1",
        "api": "openai-completions",
        "models": [{
          "id": "opus-4.6-thinking",
          "name": "Claude 4.6 Opus (Thinking)",
          "reasoning": true,
          "input": ["text"],
          "cost": { "input": 0, "output": 0, "cacheRead": 0, "cacheWrite": 0 },
          "contextWindow": 200000,
          "maxTokens": 65536
        }]
      }
    }
  },
  "agents": {
    "defaults": {
      "model": { "primary": "cursor/opus-4.6-thinking" },
      "models": { "cursor/opus-4.6-thinking": { "alias": "Opus" } }
    }
  }
}
```

同时编辑 `/root/.openclaw/agents/main/agent/models.json`，添加 API Key：

```json
{
  "providers": {
    "cursor": {
      "baseUrl": "http://127.0.0.1:8080/v1",
      "api": "openai-completions",
      "models": [{
        "id": "opus-4.6-thinking",
        "name": "Claude 4.6 Opus (Thinking)",
        "reasoning": true,
        "input": ["text"],
        "cost": { "input": 0, "output": 0, "cacheRead": 0, "cacheWrite": 0 },
        "contextWindow": 200000,
        "maxTokens": 65536
      }],
      "apiKey": "YOUR_CURSOR_API_KEY"
    }
  }
}
```

### 4.4 配置飞书通道

在 `openclaw.json` 中添加飞书通道配置（使用第一部分获取的信息）：

```json
{
  "channels": {
    "feishu": {
      "enabled": true,
      "appId": "YOUR_FEISHU_APP_ID",
      "appSecret": "YOUR_FEISHU_APP_SECRET",
      "domain": "feishu",
      "connectionMode": "websocket",
      "blockStreaming": true,
      "streamMode": "block"
    }
  },
  "plugins": {
    "entries": {
      "feishu": { "enabled": true }
    }
  }
}
```

### 4.5 配置实时流式推送

让飞书收到的回复逐段显示，而非等全部完成后一次性推送。在 `agents.defaults` 中添加：

```json
{
  "agents": {
    "defaults": {
      "blockStreamingDefault": "on",
      "blockStreamingBreak": "text_end",
      "blockStreamingChunk": {
        "minChars": 60,
        "maxChars": 2000,
        "breakPreference": "paragraph"
      },
      "blockStreamingCoalesce": {
        "minChars": 100,
        "maxChars": 3000,
        "idleMs": 2000
      },
      "typingMode": "instant"
    }
  }
}
```

| 参数 | 作用 |
|------|------|
| `blockStreamingDefault: "on"` | 启用分块流式推送 |
| `blockStreamingBreak: "text_end"` | 每个文本块结束时推送 |
| `blockStreamingChunk` | 每块 60~2000 字，按段落断行 |
| `blockStreamingCoalesce` | 合并过小的块，空闲 2 秒 flush |
| `typingMode: "instant"` | 收到消息立即显示"正在输入" |

### 4.6 启动 OpenClaw 服务

创建 systemd 用户服务：

```bash
mkdir -p ~/.config/systemd/user

cat > ~/.config/systemd/user/openclaw-gateway.service << 'EOF'
[Unit]
Description=OpenClaw Gateway
After=network-online.target

[Service]
ExecStart=/usr/bin/node /usr/lib/node_modules/openclaw/dist/index.js gateway --port 18789
Restart=always
RestartSec=5
KillMode=process
UnsetEnvironment=HTTP_PROXY HTTPS_PROXY http_proxy https_proxy ALL_PROXY all_proxy
Environment=no_proxy=*
Environment=NO_PROXY=*
Environment=HOME=/root

[Install]
WantedBy=default.target
EOF

systemctl --user daemon-reload
systemctl --user enable openclaw-gateway
systemctl --user start openclaw-gateway
```

> 💡 **重要提示**：如果系统设置了 HTTP 代理（如 `/etc/environment` 中有 `HTTP_PROXY`），必须在 service 文件中 `UnsetEnvironment`，否则飞书 API 会报 400 错误（"The plain HTTP request was sent to HTTPS port"）。

---

## 第五部分：安装 20 个 Agent Skills

Skills 是模块化的 AI 能力，让 Agent 具备文档处理、内容创作、SEO 分析等专业技能。

### 5.1 安装方法

```bash
mkdir -p ~/.cursor/skills
mkdir -p /opt/cursor-api-gateway/.cursor/skills

cd /tmp

# 克隆技能仓库
git clone --depth 1 https://github.com/anthropics/skills.git anthropics-skills
git clone --depth 1 https://github.com/JimLiu/baoyu-skills.git
git clone --depth 1 https://github.com/coreyhaines31/marketingskills.git
git clone --depth 1 https://github.com/AgriciDaniel/claude-seo.git
git clone --depth 1 https://github.com/PleasePrompto/notebooklm-skill.git
git clone --depth 1 https://github.com/kepano/obsidian-skills.git

# 安装 Anthropics 官方 Skills
for skill in pdf docx pptx xlsx doc-coauthoring frontend-design canvas-design \
  algorithmic-art theme-factory brand-guidelines web-artifacts-builder \
  skill-creator mcp-builder; do
  cp -r /tmp/anthropics-skills/skills/$skill ~/.cursor/skills/
done

# 安装宝玉 Skills
mkdir -p ~/.cursor/skills/baoyu-skills
cp -r /tmp/baoyu-skills/skills/* ~/.cursor/skills/baoyu-skills/

# 安装营销 Skills
cp -r /tmp/marketingskills/skills ~/.cursor/skills/marketingskills

# 安装其他
cp -r /tmp/claude-seo ~/.cursor/skills/claude-seo
cp -r /tmp/notebooklm-skill ~/.cursor/skills/notebooklm-skill
cp -r /tmp/obsidian-skills/skills ~/.cursor/skills/obsidian-skills

# 同步到 Gateway workspace
cp -r ~/.cursor/skills/* /opt/cursor-api-gateway/.cursor/skills/
```

### 5.2 Skills 分层总览

**第一层：文档处理（Anthropic 官方）**

| Skill | 功能 |
|-------|------|
| pdf | PDF 解析、合同条款提取、OCR |
| docx | Word 文档创建/编辑 |
| pptx | PPT 演示文稿生成 |
| xlsx | Excel 表格、公式、图表 |

**第二层：写作 / 设计 / 营销**

| Skill | 来源 | 功能 |
|-------|------|------|
| baoyu-skills | JimLiu | 宝玉自用 15 子技能（公众号发布、格式化、配图等） |
| doc-coauthoring | anthropics | 人机协作写作 |
| frontend-design | anthropics | 高质量前端 UI 设计 |
| canvas-design | anthropics | 海报、Banner、社交配图 |
| algorithmic-art | anthropics | 分形、几何、数学可视化 |
| theme-factory | anthropics | 批量配色主题生成 |
| marketingskills | coreyhaines31 | 29 个营销子技能（SEO/CRO/广告/邮件） |
| claude-seo | AgriciDaniel | URL 级 SEO 分析优化 |
| brand-guidelines | anthropics | 品牌规范应用 |

**第三层：学习与知识管理**

| Skill | 来源 | 功能 |
|-------|------|------|
| notebooklm-skill | PleasePrompto | NotebookLM 集成（闪卡/思维导图） |
| obsidian-skills | kepano | Obsidian 集成（自动标签/链接） |
| web-artifacts-builder | anthropics | 自然语言创建小工具 |

**第四层：元技能**

| Skill | 来源 | 功能 |
|-------|------|------|
| skill-creator | anthropics | 设计和生成新 Skill |
| mcp-builder | anthropics | 构建 MCP 服务器 |

---

## 第六部分：Gateway 技术细节

### 6.1 持久会话机制

Gateway 使用 `wait_input.py` 脚本实现 Agent 进程持久化，保持多轮对话上下文：

```
Agent 启动 → 执行指令 → 回复用户 → Shell 调用 wait_input.py（阻塞）
                                              ↓
              新请求到达 → 写入 input 文件 → wait_input.py 读取并返回
                                              ↓
              Agent 收到新指令 → 执行 → 回复 → 再次调用 wait_input.py → 循环
```

**文件机制：**

| 文件 | 路径 | 用途 |
|------|------|------|
| 输出 | `/tmp/cag_out_{session_id}.jsonl` | Agent JSONL 事件流 |
| 输入 | `/tmp/cag_input_{session_id}.txt` | 下一轮用户指令 |
| 标记 | `/tmp/cag_waiting_{session_id}.marker` | wait_input.py 就绪 |

### 6.2 事件类型与流式输出

Gateway 将 Agent CLI 的 JSONL 事件实时格式化为 SSE 流：

| Agent 事件 | 输出效果 |
|------------|----------|
| `assistant/` | 文本增量 → `delta.content` |
| `thinking/delta` | 思考过程 → `delta.reasoning_content` |
| `tool_call/started (shell)` | [执行命令] + 代码块 |
| `tool_call/completed (shell)` | 输出结果 + exit code |
| `tool_call/started (read)` | [读取文件] + 文件路径 |
| `tool_call/started (edit)` | [编辑文件] + 文件路径 |
| `keepalive (10s)` | SSE comment 心跳 |

### 6.3 版本演进

| 版本 | 核心变更 |
|------|----------|
| v1.0.0 | 初版 OpenAI 兼容服务器，单次调用 |
| v2.0.0 | 持久会话模式，wait_input 机制，多平台打包 |
| v2.1.0 | 自动 session 分配（按 IP+Key 哈希绑定） |
| v2.2.0 | 修复流式字符丢失（增量 delta vs 累积识别） |
| v2.3.0 | 并发打断安全（generation 计数 + drain + session.lock） |
| v2.3.1 | SSE Keepalive 心跳；修复 systemd 代理继承 |
| v2.4.0 | 全事件分段输出（tool_call 格式化）；修复多轮重复回答 |
| v2.5.0 | 精简/全量输出模式（compact / full） |

---

## 第七部分：运维手册

### 7.1 服务管理

```bash
# Cursor API Gateway
sudo systemctl start cursor-api-gateway
sudo systemctl stop cursor-api-gateway
sudo systemctl restart cursor-api-gateway
sudo systemctl status cursor-api-gateway

# OpenClaw
systemctl --user start openclaw-gateway
systemctl --user stop openclaw-gateway
systemctl --user restart openclaw-gateway
systemctl --user status openclaw-gateway
```

### 7.2 健康检查

```bash
curl http://localhost:8080/health              # Gateway 状态
curl http://localhost:8080/sessions            # 活跃会话列表
curl -X DELETE http://localhost:8080/sessions/{id}  # 终止会话
```

### 7.3 日志查看

```bash
tail -f /tmp/cursor-api-gateway.log                 # Gateway 日志
journalctl --user -u openclaw-gateway -f             # OpenClaw 日志
tail -f /tmp/cag_out_*.jsonl                         # Agent 原始输出
```

### 7.4 常见问题

**Q: 飞书消息不是实时返回，一口气返回一堆**
A: 在 `openclaw.json` 的 `agents.defaults` 中启用 `blockStreamingDefault: "on"`，详见第四部分。

**Q: 飞书报 400 错误（HTTP request sent to HTTPS port）**
A: openclaw 服务继承了系统代理变量，在 systemd service 中 `UnsetEnvironment` 代理变量。

**Q: 新消息发送后上一轮中断，显示 "no output"**
A: 升级至 Gateway v2.3.0+，已通过 generation 计数 + drain 机制修复。

**Q: 第二轮对话重复上一轮回答**
A: 升级至 Gateway v2.4.0+，已修复 read_pos 推进逻辑。

**Q: Agent 执行工具调用时客户端超时**
A: Gateway v2.3.1+ 每 10 秒发送 SSE keepalive 心跳保活。

**Q: 只想看最终文本，不想看 thinking 和工具过程**
A: 使用 compact 模式：启动时 `--output-mode compact` 或 Header `X-Output-Mode: compact`。

---

## 附件

- 📦 Linux 安装包：`cursor-api-gateway-2.5.0-linux.tar.gz`
- 📦 macOS 安装包：`cursor-api-gateway-2.5.0-macos.tar.gz`
- 📦 Windows 安装包：`cursor-api-gateway-2.5.0-windows.zip`
- 📄 手册 Markdown 版：`setup-guide.md`
