# interactive-feedback-mcp 中文输入支持改造指南

## 背景

[interactive-feedback-mcp](https://github.com/noopstudios/interactive-feedback-mcp) 是 Cursor IDE 的一个 MCP 工具，用于在 AI 对话中向用户请求交互式反馈。原版使用 PySide6 (Qt6) 构建 UI，在 Linux 下使用 fcitx 系输入法（如搜狗输入法）时**无法输入中文**。

### 原因

- PySide6 (Qt6) 插件目录中没有 fcitx 输入法插件
- ibus 桥接不可用（ibus-daemon 未配置中文引擎）
- Qt6 对 XIM 协议支持大幅削减，回退方案也失效

### 解决方案

将 UI 从 PySide6 (Qt6) **改写为 PyGObject (GTK3)**。GTK3 应用通过 `fcitx-frontend-gtk3` 与 fcitx 直接通信，天然支持中文输入。

---

## 环境要求

| 项目 | 要求 |
|------|------|
| 操作系统 | Linux (Ubuntu 18.04+) |
| 输入法 | fcitx/fcitx5 + 搜狗/拼音等中文引擎 |
| 系统 Python | `/usr/bin/python3`，需要有 PyGObject |
| MCP 运行环境 | uv (用于运行 server.py) |

### 依赖安装

```bash
# PyGObject 和 GTK3 绑定
sudo apt install python3-gi gir1.2-gtk-3.0

# fcitx GTK3 前端（fcitx4 用户）
sudo apt install fcitx-frontend-gtk3

# 或 fcitx5 GTK3 前端（fcitx5 用户）
sudo apt install fcitx5-frontend-gtk3
```

验证依赖是否就绪：

```bash
# 验证 PyGObject
/usr/bin/python3 -c "import gi; gi.require_version('Gtk','3.0'); from gi.repository import Gtk; print('OK')"

# 验证 fcitx GTK3 前端
dpkg -l | grep fcitx-frontend-gtk3
```

---

## 改造步骤

### 第 1 步：修改 server.py

需要修改两处：

**1a. 用临时 JSON 文件传递 prompt（解决中文编码问题）**

```python
# Write prompt and options to a temp file to avoid command-line encoding issues
with tempfile.NamedTemporaryFile(suffix=".json", delete=False, mode='w', encoding='utf-8') as input_tmp:
    input_file = input_tmp.name
    json.dump({
        "prompt": summary,
        "predefined_options": predefinedOptions or []
    }, input_tmp, ensure_ascii=False)

# Run feedback_ui.py using system Python (has PyGObject/GTK3)
system_python = "/usr/bin/python3"
if not os.path.exists(system_python):
    system_python = sys.executable
args = [
    system_python, "-u", feedback_ui_path,
    "--input-file", input_file,
    "--output-file", output_file,
]
env = os.environ.copy()
env["PYTHONIOENCODING"] = "utf-8"
result = subprocess.run(args, check=False, shell=False,
    stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
    stdin=subprocess.DEVNULL, close_fds=True, env=env)
if os.path.exists(input_file):
    os.unlink(input_file)
```

**1b. 读取结果文件时指定 UTF-8 编码**

```python
with open(output_file, 'r', encoding='utf-8') as f:
    result = json.load(f)
```

### 第 2 步：替换 feedback_ui.py

将整个 `feedback_ui.py` 替换为 GTK3 版本（使用 PyGObject），包含：

- 深色主题 CSS
- 窗口位置/大小持久化
- 多选复选框 + 文本输入
- Ctrl+Enter 快捷提交
- 从 JSON 文件读取中文 prompt（避免命令行编码问题）

### 第 3 步：重启 MCP 服务器

在 Cursor 设置 → MCP 中重启 `interactive-feedback` 服务。

---

## 测试验证

```bash
/usr/bin/python3 /path/to/feedback_ui.py \
  --prompt "测试中文输入" \
  --predefined-options "选项A|||选项B|||选项C" \
  --output-file /tmp/test.json
```

---

## 工作原理

```
Cursor → MCP stdio → server.py (uv python, fastmcp)
                         ↓ subprocess (/usr/bin/python3)
                    feedback_ui.py (PyGObject/GTK3)
                         ↓ fcitx-frontend-gtk3
                    中文输入法正常工作
```

GTK3 应用通过 `fcitx-frontend-gtk3` 与 fcitx 直接通信，不需要额外插件。

---

## 故障排查

| 问题 | 解决方案 |
|------|----------|
| `No module named 'gi'` | `sudo apt install python3-gi gir1.2-gtk-3.0` |
| UI 打开但无法输入中文 | `sudo apt install fcitx-frontend-gtk3` 然后 `fcitx -r` |
| UI 无法启动 | 检查 `/usr/bin/python3` 是否存在 |
| 中文显示为乱码 | 确认系统 locale 支持 UTF-8 |

## 适用范围

| 输入法 | 支持情况 |
|--------|----------|
| 搜狗输入法 (fcitx4) | ✅ 需要 `fcitx-frontend-gtk3` |
| fcitx5 系列 | ✅ 需要 `fcitx5-frontend-gtk3` |
| ibus 系列 | ✅ GTK3 内置 ibus 支持 |
| macOS / Windows | ❌ 此方案针对 Linux |
| 纯终端 / SSH | ❌ 需要图形显示环境 |