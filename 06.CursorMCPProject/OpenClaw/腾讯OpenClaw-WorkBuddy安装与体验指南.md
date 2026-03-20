# 腾讯 OpenClaw & WorkBuddy 安装与体验指南

> 整理时间：2026-03-15  
> 状态：仅文档整理，未安装  
> 相关文件：`06.CursorMCPProject/doc/OpenClaw/` 目录下已有 OpenClaw 部署相关文档

---

## 一、产品概览

### 1.1 产品体系

腾讯围绕 OpenClaw 生态推出了三款产品：

| 产品 | 定位 | 部署方式 | 目标用户 |
|------|------|----------|----------|
| **OpenClaw** (原版) | 开源 AI 智能体框架 | 需自行安装 Node.js + npm + 配置 API Key | 开发者/技术用户 |
| **WorkBuddy** | 免部署版 AI 办公桌面工作台 | 下载安装包，双击即用 | 普通办公用户/企业员工 |
| **QClaw** | 微信版"小龙虾" | 内测中，关联个人微信操控电脑 | 普通消费者 |

### 1.2 核心关系

```
OpenClaw (开源框架，25万+ GitHub Star)
    ├── WorkBuddy (腾讯云 CodeBuddy 团队，免部署商业版)
    │    ├── 预集成腾讯混元大模型
    │    ├── 兼容 OpenClaw Skill 生态
    │    └── 腾讯级安全网关
    └── QClaw (腾讯电脑管家团队，微信版)
         ├── 关联个人微信远程操控
         ├── 内置国产大模型
         └── 邀请制内测中
```

---

## 二、OpenClaw 原版安装（开发者路线）

### 2.1 系统要求

| 项目 | 要求 |
|------|------|
| Node.js | v22+ (LTS 推荐) |
| npm | 随 Node.js 安装 |
| Git | 最新版 |
| 操作系统 | Windows 10/11、macOS 10.15+、Linux |
| 网络 | 稳定连接（需调用 LLM API） |

### 2.2 安装步骤

#### 步骤 1：安装 Node.js

```bash
# Ubuntu/Debian
curl -fsSL https://deb.nodesource.com/setup_22.x | sudo -E bash -
sudo apt-get install -y nodejs

# 验证
node -v   # 应显示 v22.x.x
npm -v    # 应显示 10.x.x
```

#### 步骤 2：安装 OpenClaw

```bash
# 使用国内镜像源安装
npm i -g openclaw --ignore-scripts --registry=https://registry.npmmirror.com

# 验证安装
openclaw --version
```

#### 步骤 3：首次配置

```bash
# 启动 OpenClaw（首次运行会引导配置）
openclaw

# 配置 API Key（以 Claude 为例）
# 在 Gateway 仪表盘中设置，默认端口 18789
# 浏览器访问：http://localhost:18789
```

### 2.3 API Key 配置

OpenClaw 支持多种大模型，需自行配置：

| 模型提供商 | 获取方式 | 说明 |
|-----------|----------|------|
| Anthropic (Claude) | console.anthropic.com | 官方推荐，效果最佳 |
| OpenAI (GPT) | platform.openai.com | 通用性强 |
| Google (Gemini) | aistudio.google.com | 免费额度较多 |
| DeepSeek | platform.deepseek.com | 国内模型，性价比高 |
| 腾讯混元 | 腾讯云控制台 | 国内用户推荐 |

### 2.4 技术架构

OpenClaw 采用五层模块化设计：

```
┌──────────────────────────────────────┐
│         渠道适配层 (Channel)          │  WhatsApp/Telegram/飞书/钉钉/企微/QQ...
├──────────────────────────────────────┤
│       Gateway 网关层 (中枢核心)       │  请求调度/异常处理/认证鉴权
├──────────────────────────────────────┤
│       核心业务层 (Core Business)      │  Agent 管理/任务编排/Skill 调度
├──────────────────────────────────────┤
│         模型适配层 (Model)            │  Claude/GPT/Gemini/DeepSeek/本地模型
├──────────────────────────────────────┤
│        数据存储层 (Storage)           │  本地文件系统/SQLite/记忆管理
└──────────────────────────────────────┘
```

#### Gateway 核心配置

- 默认端口：`18789`
- 配置文件路径：`~/.openclaw/config/`
- 日志路径：`~/.openclaw/logs/`
- 启动命令：`openclaw` 或 `openclaw --gateway`
- 停止命令：`Ctrl+C` 或 `openclaw stop`

#### 常见故障排查

| 故障现象 | 原因 | 解决方案 |
|---------|------|---------|
| Port 18789 already in use | 端口被占用 | `lsof -i :18789` 查找并 kill 进程 |
| Node.js version is too low | Node.js 版本不够 | 升级到 v22+ |
| 远程访问失败 | 防火墙/绑定 localhost | 修改配置绑定 0.0.0.0，开放端口 |
| Skill 加载失败 | 路径或权限问题 | 检查 Skill 目录权限和 SKILL.md 格式 |

### 2.5 Skill 技能体系

Skill 是 OpenClaw 的功能扩展单元，每个 Skill 仅需一个 `SKILL.md` 文件。

#### Skill vs Plugin

| 特征 | Skill | Plugin |
|------|-------|--------|
| 触发方式 | LLM 智能决策调用 | 生命周期钩子自动运行 |
| 用户可见性 | 用户可在对话中看到调用 | 通常隐形运行 |
| 组成 | YAML 元数据 + Markdown 指令 | JSON 配置 + 代码逻辑 |
| 开发难度 | 低（只需写 Markdown） | 中（需要编程） |

#### 安装 Skill

```bash
# 方式 1：命令行安装
clawhub install <skill-name>

# 方式 2：Web 仪表盘安装
# 访问 http://localhost:18789 → Skill 市场

# 方式 3：对话安装
# 在聊天中发送 Skill 地址，OpenClaw 自动下载安装
```

#### 推荐 Skill（ClawHub 13700+ 技能）

| 类别 | Skill 名称 | 功能 |
|------|-----------|------|
| 文件处理 | pdf-processor | PDF 读写/合并/拆分 |
| 数据分析 | excel-analyzer | Excel 数据分析/图表 |
| 浏览器 | browser-automation | 网页自动化操作 |
| 编程 | codebuddy-cli | 腾讯 CodeBuddy 编程助手 |
| 记忆 | memoclaw-mcp | 跨会话持久化记忆 |
| MCP 桥接 | openclaw-mcp-bridge | 连接任意 MCP 服务器 |

---

## 三、WorkBuddy 安装（免部署路线）

### 3.1 系统要求

| 项目 | 要求 |
|------|------|
| 操作系统 | Windows 10/11 或 macOS 10.15+ |
| 存储空间 | 约 150-180 MB |
| 网络 | 稳定连接 |
| 账号 | 腾讯账号（企业微信/QQ/微信） |

### 3.2 下载地址

- **官网**：https://www.codebuddy.cn/work/
- **Windows 安装包**：`WorkBuddySetup.exe`（约 150-180 MB）
- **macOS 安装包**：`WorkBuddy.dmg`

### 3.3 安装步骤

#### Windows 安装

1. 下载 `WorkBuddySetup.exe`
2. 双击运行安装程序
3. 按照安装向导点击"下一步"完成安装
4. 安装完成后自动启动

#### macOS 安装

1. 下载 `WorkBuddy.dmg`
2. 双击挂载 DMG 文件
3. 将 WorkBuddy 拖拽到"应用程序"文件夹
4. 如提示"无法打开"，进入 **系统设置 → 安全性与隐私 → 允许**
5. 从"应用程序"中启动 WorkBuddy

### 3.4 首次配置

#### 步骤 1：登录账号

- 使用腾讯账号登录（推荐企业微信或 QQ）
- WorkBuddy 与 CodeBuddy 使用同一账号体系

#### 步骤 2：授权文件访问

- 建议授权：桌面、文档、下载 三个文件夹
- 注意：仅授权必要文件夹，避免敏感数据暴露

#### 步骤 3：选择模型

| 场景 | 推荐模型 | 原因 |
|------|---------|------|
| 日常办公 | 混元 | 响应速度快 |
| 复杂任务 | DeepSeek / GLM | 理解能力强 |
| 创意写作 | Kimi | 文本生成质量高 |
| 编程辅助 | Auto 模式 | 自动选择最优模型 |

#### 步骤 4：切换中文界面

- 点击右上角头像 → 切换语言为中文

### 3.5 配置远程控制（Claw 功能）

WorkBuddy 支持通过手机远程操控电脑：

1. 打开 WorkBuddy → 右上角"个人中心"
2. 点击 **Claw 设置**
3. 选择绑定工具：企业微信 / QQ / 飞书 / 钉钉
4. 按提示扫码或授权完成绑定
5. 在手机 IM 中发送指令即可远程操控

### 3.6 费用说明

| 版本 | 价格 | 说明 |
|------|------|------|
| 个人免费版 | 免费 | 500 Credits/月 |
| 专业版 | 58 元/月 | 更多 Credits 额度 |
| Code Plan | 7.9 元/月 | 编程专用 |
| 活动赠送 | 5,000 Credits | 限时（具体日期以官方为准） |

领取 Credits：https://www.codebuddy.cn/profile/usage

---

## 四、核心功能体验

### 4.1 三种交互模式

| 模式 | 说明 | 适用场景 |
|------|------|----------|
| **Craft** (创作) | 执行具体任务，生成交付物 | 文件处理、报告生成、数据分析 |
| **Plan** (计划) | 任务规划和方案设计 | 复杂项目拆解、工作流设计 |
| **Ask** (咨询) | 问答和信息查询 | 知识咨询、技术问题 |

### 4.2 典型使用场景

#### 文件批量处理

```
把桌面上所有PDF按月份分类，移动到对应文件夹
```

#### Excel 数据分析

```
把桌面"2026Q1销售数据"里所有Excel合并，生成柱状图+分析报告
```

#### 文档格式转换

```
把D盘"周报"文件夹里所有Word转PDF，并按日期重命名
```

#### PPT 自动生成

```
读取"业绩表.xlsx"，计算各部门环比，生成PPT并自动排版
```

#### 定时任务

```
每天9点自动导出昨日订单数据，发送到企业微信群
```

### 4.3 内置技能（默认）

WorkBuddy 开箱即内置以下能力：

- 项目管理：协调多个 Agent 并行工作
- 文件操作：读写/合并/转换 Office/PDF/图片
- 网络搜索：获取最新信息
- 浏览器自动化：网页操作和数据采集
- 代码执行：运行 Python/Shell 等脚本
- 定时任务：自动化重复性工作

### 4.4 指令技巧

- 路径要具体：明确文件/文件夹的完整路径
- 格式要指定：明确输出格式（PDF/Excel/PPT 等）
- 需求要清晰：描述具体需求（图表类型、分析维度等）
- 从简入深：先尝试简单任务，再逐步复杂化

---

## 五、WorkBuddy vs OpenClaw 对比

| 维度 | OpenClaw (原版) | WorkBuddy (腾讯版) |
|------|----------------|-------------------|
| **部署方式** | npm 安装 + 命令行配置 | 下载安装包，双击即用 |
| **技术门槛** | 需要 Node.js、npm 基础 | 零技术门槛 |
| **模型配置** | 自行购买并配置各家 API Key | 预集成，一站式 |
| **数据存储** | 完全本地，隐私性强 | 云端 SaaS + 本地混合 |
| **Skill 生态** | 完整开源生态（13700+ Skill） | 兼容 OpenClaw Skill 格式 |
| **远程控制** | 需手动配置 | 内置 Claw 功能，一键绑定 |
| **安全性** | 自行管理 | 腾讯级安全网关 |
| **价格** | 软件免费，API 自费 | 个人版免费，专业版 58 元/月 |
| **定制性** | 极高（代码级） | 中等（技能市场 + 对话配置） |
| **适合人群** | 开发者/技术用户 | 普通办公用户/企业团队 |

### 选择建议

- **选 OpenClaw**：重视隐私、需要高度定制、有技术背景、预算有限
- **选 WorkBuddy**：追求开箱即用、非技术背景、需要远程控制、腾讯生态用户

---

## 六、QClaw（微信版，内测中）

### 6.1 概述

QClaw 由腾讯电脑管家团队开发，基于 OpenClaw 框架，通过个人微信远程操控电脑。

### 6.2 核心特点

- 微信直连：关联个人微信（非企业微信），零配置
- 本地部署：数据全部留在本地，隐私安全
- 5000+ Skills：兼容 ClawHub 生态
- 持续记忆：记住偏好和上下文，持续成长
- 双端支持：Mac & Windows

### 6.3 状态

- 当前：邀请制内测
- 下载：https://claw.guanjia.qq.com
- 申请内测：https://wj.qq.com/s2/25871229/abe7

---

## 七、与 Cursor 的关联

### 7.1 CodeBuddy 是桥梁

腾讯 CodeBuddy 同时提供：
- **CodeBuddy IDE 插件**：VSCode/Cursor 内编程助手
- **WorkBuddy 桌面端**：AI 办公桌面工作台
- 两者共享同一账号体系和 Credits 额度

### 7.2 MCP 互通

OpenClaw 通过 `openclaw-mcp-bridge` 可接入任意 MCP 服务器，与 Cursor 的 MCP 生态互通：

```bash
# 安装 MCP 桥接插件
openclaw plugins install @aiwerk/openclaw-mcp-bridge
```

支持接入：Todoist、GitHub、Notion、Stripe、RAGFlow 等 MCP 服务。

### 7.3 互补使用场景

| 场景 | 推荐工具 |
|------|---------|
| 代码编写/调试 | Cursor |
| 文件批量处理/办公自动化 | WorkBuddy |
| 代码审查 + 文档生成 | CodeBuddy + WorkBuddy |
| 远程操控电脑执行任务 | WorkBuddy (Claw) |
| 知识库检索 + 编程 | Cursor (RAGFlow MCP) |

---

## 八、官方资源汇总

| 资源 | 地址 |
|------|------|
| WorkBuddy 官网 | https://www.codebuddy.cn/work/ |
| WorkBuddy 文档 | https://www.codebuddy.cn/docs/workbuddy/Overview |
| Claw 远程文档 | https://www.codebuddy.cn/docs/workbuddy/Claw |
| CodeBuddy 插件系统 | https://www.codebuddy.cn/docs/zh/cli/plugins |
| OpenClaw GitHub | https://github.com/openclaw/openclaw |
| ClawHub 技能市场 | https://openclawdir.com |
| QClaw 下载 | https://claw.guanjia.qq.com |
| QClaw 内测申请 | https://wj.qq.com/s2/25871229/abe7 |
| Credits 管理 | https://www.codebuddy.cn/profile/usage |
| 腾讯云开发者社区 | https://cloud.tencent.com/developer |

---

## 九、注意事项

### 安全建议

1. 仅授权必要的文件夹访问权限
2. 避免处理敏感/机密数据
3. 定期检查执行日志
4. 使用沙箱机制执行任务

### 性能优化

1. 根据任务复杂度选择合适的模型
2. 批量处理任务建议分批执行
3. 复杂任务消耗 Credits 较多，注意额度

### Linux 用户说明

- WorkBuddy 目前仅支持 Windows/macOS，**不支持 Linux**
- Linux 用户建议使用 OpenClaw 原版（npm 安装）
- 当前系统（Ubuntu 20.04）适合安装 OpenClaw 原版
