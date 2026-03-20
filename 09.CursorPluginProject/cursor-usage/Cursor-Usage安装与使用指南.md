# Cursor Usage 安装与使用指南

> Cursor Usage 是一个 Cursor IDE 扩展插件，在底部状态栏实时显示 Included-Request 使用量，帮助你随时掌握配额消耗情况。
>
> 版本：0.0.7-bq | 来源：内部工具（daiqingchen）

---

## 一、功能概览

### 状态栏显示

插件在 Cursor 底部状态栏右下角实时显示：

```
⦿ 已用/配额 | 最近Token消耗
```

例如：`⦿ 123/500 | 2.3万`

### 悬停 Tooltip 详情

鼠标悬停状态栏图标，显示：

- **进度条**：可视化使用百分比
- **已用 / 配额 / 剩余**：精确数值
- **重置日期**：下次配额重置时间
- **最近请求 Token**：最近一次请求的 Token 消耗量
- **Token 效率**：当前周期内平均每次请求的 Token 消耗
- **空请求统计**：Token 消耗为 0 的请求次数 / 总请求次数
- **快捷按钮**：Show History、Sync

### 颜色预警

| 使用率 | 颜色 | 含义 |
|--------|------|------|
| < 75% | 默认 | 正常 |
| ≥ 75% | 黄色 | 接近配额上限 |
| ≥ 90% | 红色 | 即将用尽 |

### 历史面板

通过 `Ctrl+Shift+P` → `Cursor Usage: Show History` 打开 WebView 面板，展示：

- **时间范围切换**：1 天 / 7 天 / 30 天
- **汇总统计**：总请求数、总 Token 数
- **详细记录表格**：时间、类型（Included/On-Demand/Errored）、模型名、Tokens、Requests

---

## 二、安装步骤

### 前置要求

- **Cursor** 编辑器（基于 VS Code），版本 ≥ 1.85
- 已登录 Cursor 账号
- Linux x64 / Windows x64 / macOS（插件内置 sqlite3 二进制）

### 方式一：命令行安装（推荐）

```bash
# Linux / macOS
cursor --install-extension /path/to/cursor-usage-0.0.7-bq.vsix

# Windows (PowerShell)
cursor --install-extension C:\path\to\cursor-usage-0.0.7-bq.vsix
```

### 方式二：Cursor 界面安装

1. 打开 Cursor
2. 按 `Ctrl+Shift+P`（macOS 为 `Cmd+Shift+P`）
3. 输入并选择 `Extensions: Install from VSIX...`
4. 选择 `cursor-usage-0.0.7-bq.vsix` 文件
5. 重新加载窗口：`Ctrl+Shift+P` → `Developer: Reload Window`

### 验证安装

```bash
cursor --list-extensions | grep cursor-usage
# 应输出: local.cursor-usage
```

安装成功后，底部状态栏右下角应显示用量信息。

---

## 三、使用方法

### 3.1 查看实时用量

安装后自动在状态栏显示，无需任何操作。

### 3.2 查看详细信息

鼠标悬停在状态栏的用量数字上，弹出 Tooltip 显示：

- 进度条和百分比
- 已用 / 配额 / 剩余
- 配额重置日期
- 最近请求 Token 消耗
- Token 效率（平均每请求 Token 数）
- 空请求统计

### 3.3 手动刷新

- **点击状态栏**：直接点击用量数字
- **命令面板**：`Ctrl+Shift+P` → `Cursor Usage: Refresh`

### 3.4 查看历史记录

- **命令面板**：`Ctrl+Shift+P` → `Cursor Usage: Show History`
- **Tooltip 按钮**：悬停后点击 `Show History`

历史面板支持切换 1 天 / 7 天 / 30 天视图，展示每次请求的详细信息。

---

## 四、配置项

打开 Cursor 设置（`Ctrl+,`），搜索 `cursorUsage`：

| 设置项 | 默认值 | 说明 |
|--------|--------|------|
| `cursorUsage.refreshInterval` | `300` | 定时刷新间隔（秒），最小 30 |
| `cursorUsage.realtimeMinInterval` | `15` | 实时事件触发最小间隔（秒），最小 5 |
| `cursorUsage.activityDebounceMs` | `1200` | 编辑活动防抖时间（毫秒），最小 300 |
| `cursorUsage.language` | `auto` | 界面语言：`auto` / `zh-CN` / `en` |

---

## 五、刷新策略

插件采用 **"事件驱动 + 定时兜底"** 双层策略：

### 事件驱动（实时触发）

| 事件 | 触发时机 | 说明 |
|------|----------|------|
| 启动 | 扩展激活后 | 强制刷新 |
| 窗口聚焦 | 切回 Cursor 窗口 | 立即触发 |
| 切换编辑器 | 打开或切换文件 | 防抖后触发 |
| 文本变更 | 编辑文件内容 | 防抖后触发 |
| 文件保存 | 保存文件 | 防抖后触发 |
| 手动点击 | 点击状态栏 | 强制刷新 |
| 命令刷新 | Cursor Usage: Refresh | 强制刷新 |

### 定时兜底

默认每 5 分钟自动刷新一次。

### 节流保护

```
事件触发 → 防抖过滤(1200ms) → 节流过滤(15s) → API 请求
```

强制刷新（启动、手动点击、命令）不受节流限制。

---

## 六、技术原理

### 数据来源

插件通过以下步骤获取用量数据：

1. **读取本地凭证**：通过 sqlite3 从 Cursor 的 `state.vscdb` 数据库读取登录 Token
2. **调用 Cursor API**：使用 Token 请求 `https://cursor.com/api/usage` 获取用量
3. **获取历史事件**：请求 `https://cursor.com/api/dashboard/get-filtered-usage-events` 获取详细记录

### 数据库路径

| 系统 | 路径 |
|------|------|
| **Linux** | `~/.config/Cursor/User/globalStorage/state.vscdb` |
| **macOS** | `~/Library/Application Support/Cursor/User/globalStorage/state.vscdb` |
| **Windows** | `%APPDATA%\Cursor\User\globalStorage\state.vscdb` |

### sqlite3 查找优先级

1. 系统已安装的 sqlite3（PATH 中的 `sqlite3`）
2. 插件内嵌的 sqlite3（`bin/linux-x64/sqlite3` 或 `bin/win32-x64/sqlite3.exe`）

---

## 七、故障排查

### 状态栏显示 "Cursor: No Token"

1. 确认已登录 Cursor 账号
2. 鼠标悬停查看具体错误：
   - `未找到 state.vscdb` — 数据库路径不在候选列表中
   - `sqlite3 查询失败` — sqlite3 执行出错
   - `数据库中 cursorAuth/accessToken 为空` — Token 字段为空
   - `未找到 sqlite3` — 系统和内嵌的 sqlite3 都不可用
3. 查看诊断日志：`Ctrl+Shift+P` → `Output` → 下拉选择 `Cursor Usage`

### 状态栏显示 "Cursor: No Data"

- Cursor 的 usage API 返回格式可能变化，查看 Output 日志中的 API 响应

### 数据不更新

- 确认网络可以访问 `https://cursor.com`
- 点击状态栏手动刷新
- 执行 `Developer: Reload Window` 重载窗口

### 验证 sqlite3 可用性

```bash
# 检查系统 sqlite3
which sqlite3 && sqlite3 --version

# 检查数据库是否可读
sqlite3 ~/.config/Cursor/User/globalStorage/state.vscdb \
  "SELECT length(value) FROM ItemTable WHERE key = 'cursorAuth/accessToken' LIMIT 1;"
```

---

## 八、卸载

```bash
cursor --uninstall-extension local.cursor-usage
```

或在 Cursor 扩展面板中找到 **Cursor Usage** → 点击卸载。

---

## 九、版本历史

| 版本 | 日期 | 变更 |
|------|------|------|
| 0.0.7-bq | 2026-03-13 | 当前版本，支持 Token 效率统计、空请求统计、中英文切换 |

---

## 十、相关信息

| 项目 | 说明 |
|------|------|
| 插件 ID | `local.cursor-usage` |
| 发布者 | local |
| 引擎要求 | VS Code ≥ 1.85 |
| 激活方式 | 启动完成后自动激活 |
| 内部发布页 | http://10.8.136.229:3000/daiqingchen/cursor-usage-plugn/releases |
