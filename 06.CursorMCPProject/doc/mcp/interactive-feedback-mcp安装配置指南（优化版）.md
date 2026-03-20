# Interactive Feedback MCP 安装配置指南（优化版）

> 本指南基于 Windows 环境实际安装经验编写，涵盖了安装过程中常见的坑和解决方案，帮助你一次成功完成配置。

## 这是什么？

[Interactive Feedback MCP](https://github.com/poliva/interactive-feedback-mcp) 是一个 MCP 服务，为 Cursor / Cline / Windsurf 等 AI 辅助开发工具提供**人机交互反馈**能力。它让 AI 在执行任务过程中可以暂停并向你提问，而不是靠猜测盲目执行。

**核心优势：**
- **节省 API 调用次数** — 多轮反馈在一次请求内完成，不额外消耗配额
- **减少错误** — AI 不确定时先问你，而不是瞎猜
- **加快迭代** — 快速确认比事后 debug 高效得多

---

## 1. 前置环境准备

### 1.1 安装 Python 3.11+

确保系统已安装 **Python 3.11 或更高版本**。

**Windows 安装方式（任选其一）：**

- **方式一：通过 winget 安装（推荐）**
  ```powershell
  winget install Python.Python.3.12 --accept-package-agreements --accept-source-agreements
  ```

- **方式二：官网下载安装包**
  前往 https://www.python.org/downloads/ 下载并安装，安装时务必勾选 **"Add Python to PATH"**。

**验证安装：**
```powershell
python --version
# 输出示例：Python 3.12.10
```

### 1.2 安装 uv（Python 包管理器）

**各平台安装命令：**

| 平台 | 安装命令 |
|------|---------|
| Windows | `pip install uv` |
| Linux | `curl -LsSf https://astral.sh/uv/install.sh \| sh` |
| macOS | `brew install uv` |

> **备选方式（Windows）：** 也可以从 https://github.com/astral-sh/uv/releases 下载对应平台的压缩包，解压后将路径添加到系统环境变量中。

**验证安装：**
```powershell
uv --version
# 输出示例：uv 0.10.8
```

> **重要：记录 uv 的完整路径**，后续配置需要用到：
> ```powershell
> # Windows PowerShell
> (Get-Command uv).Source
> # 输出示例：C:\Users\你的用户名\AppData\Local\Programs\Python\Python312\Scripts\uv.exe
> ```

---

## 2. 下载项目代码

**GitHub 项目地址：** https://github.com/poliva/interactive-feedback-mcp

**方式一：Git Clone（推荐）**
```bash
git clone https://github.com/poliva/interactive-feedback-mcp.git D:\interactive-feedback-mcp
```

**方式二：直接下载 ZIP（未安装 Git 时使用）**
```powershell
# 下载
Invoke-WebRequest -Uri "https://github.com/poliva/interactive-feedback-mcp/archive/refs/heads/main.zip" -OutFile "D:\interactive-feedback-mcp.zip"
# 解压
Expand-Archive -Path "D:\interactive-feedback-mcp.zip" -DestinationPath "D:\" -Force
# 重命名文件夹
Rename-Item -Path "D:\interactive-feedback-mcp-main" -NewName "interactive-feedback-mcp"
# 清理 zip 文件
Remove-Item "D:\interactive-feedback-mcp.zip"
```

> 本指南以 `D:\interactive-feedback-mcp` 作为项目路径示例，你可以选择任意位置存放。

---

## 3. 修复兼容性问题（关键步骤）

项目依赖的 `fastmcp` 库已升级到 3.x 版本，原代码中 `FastMCP()` 构造函数的 `log_level` 参数已被移除，**必须修改 `server.py` 才能正常运行**。

打开 `D:\interactive-feedback-mcp\server.py`，找到第 16-17 行：

```python
# 修改前（会报错）
# The log_level is necessary for Cline to work: https://github.com/jlowin/fastmcp/issues/81
mcp = FastMCP("Interactive Feedback MCP", log_level="ERROR")
```

替换为：

```python
# 修改后（兼容 fastmcp 3.x）
os.environ.setdefault("FASTMCP_LOG_LEVEL", "ERROR")
mcp = FastMCP("Interactive Feedback MCP")
```

---

## 4. 配置 Cursor MCP

### 4.1 打开配置文件

在 Cursor 中：**File → Preferences → Cursor Settings → Tools & MCP**，点击 **New MCP Server** 打开配置 JSON 文件。

### 4.2 添加配置

在 `mcpServers` 中添加以下配置：

```json
{
  "mcpServers": {
    "interactive-feedback": {
      "command": "C:\\Users\\你的用户名\\AppData\\Local\\Programs\\Python\\Python312\\Scripts\\uv.exe",
      "args": [
        "--directory",
        "D:\\interactive-feedback-mcp",
        "run",
        "server.py"
      ],
      "timeout": 600,
      "env": {
        "UV_LINK_MODE": "copy"
      },
      "autoApprove": [
        "interactive_feedback"
      ]
    }
  }
}
```

### 4.3 配置说明

| 字段 | 说明 |
|------|------|
| `command` | **必须使用 uv.exe 的完整绝对路径**，Cursor 启动 MCP 时使用独立的 PATH 环境，无法识别简写的 `uv` |
| `args` 中的 `--directory` | 替换为你实际的项目下载路径 |
| `env.UV_LINK_MODE` | 设为 `copy` 以避免项目与 uv 缓存在不同磁盘时的硬链接失败警告 |
| `timeout` | 设为 600 秒，留足启动时间 |
| `autoApprove` | 自动批准 `interactive_feedback` 工具调用，避免每次手动确认 |

---

## 5. 验证安装

1. 在 Cursor 的 **Tools & MCP** 页面中，确认 `interactive-feedback` 显示为绿色（已加载）状态
2. 如果显示红色 Error，点击 **Show Output** 查看具体错误信息

### 常见问题排查

| 错误信息 | 原因 | 解决方案 |
|---------|------|---------|
| `spawn uv ENOENT` | Cursor 找不到 uv 命令 | `command` 字段改为 uv.exe 的**完整绝对路径** |
| `FastMCP() no longer accepts log_level` | fastmcp 3.x 移除了此参数 | 按第 3 步修改 `server.py` |
| `Failed to hardlink files` | 项目和 uv 缓存在不同磁盘 | 配置中添加 `"env": {"UV_LINK_MODE": "copy"}` |
| `Client closed for command` | server.py 启动后立即崩溃 | 手动运行 `uv --directory 项目路径 run server.py` 查看具体报错 |

---

## 6. 配置 Cursor User Rules（重要）

为了让 AI 主动使用 interactive-feedback 工具，需要在 Cursor 中添加自定义规则。

**路径：** File → Preferences → Cursor Settings → Rules → User Rules

在规则框中添加以下内容：

```
If requirements or instructions are unclear use the tool interactive_feedback to ask clarifying questions to the user before proceeding, do not make assumptions. Whenever possible, present the user with predefined options through the interactive_feedback MCP tool to facilitate quick decisions.

Whenever you're about to complete a user request, call the interactive_feedback tool to request user feedback before ending the process. If the feedback is empty you can end the request and don't call the tool in loop.
```

> 这段规则会指导 AI：在任务不明确时主动提问，在完成任务后询问用户反馈，避免盲目猜测。

---

## 附录 A：手动测试 MCP 服务

在配置 Cursor 前，可以先在命令行手动验证服务能否正常启动：

```powershell
$env:UV_LINK_MODE = "copy"
uv --directory "D:\interactive-feedback-mcp" run server.py
```

如果看到类似以下输出，说明服务正常：

```
+----------------------------------------------------------------------+
|                         FastMCP 3.x.x                                |
|               Server: Interactive Feedback MCP                       |
+----------------------------------------------------------------------+
Starting MCP server 'Interactive Feedback MCP' with transport 'stdio'
```

按 `Ctrl+C` 退出测试即可。

---

## 附录 B：Linux / macOS 用户注意事项

本指南以 Windows 为主，Linux / macOS 用户需注意以下差异：

| 差异项 | Windows | Linux / macOS |
|-------|---------|--------------|
| uv 路径查找 | `(Get-Command uv).Source` | `which uv` |
| command 字段 | `C:\\Users\\...\\uv.exe` | `/home/用户名/.local/bin/uv` 或 `/opt/homebrew/bin/uv` |
| 路径分隔符 | `\\` | `/` |
| UV_LINK_MODE | 跨盘时需要设为 copy | 通常不需要（同一文件系统） |
