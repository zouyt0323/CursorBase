# Android Camera App 式样生成 — 推荐 Skills 详细使用指南

> **结论**：全网 30 万+ Agent Skills 中无专用"App 式样生成"Skill，以下 5 个 Skill 组合使用可完整覆盖式样生成需求。

---

## 一、总览：5 个 Skill 的分工

```
Android Camera App 式样文档
├── 1. 产品概述与项目初始化 ──────── conductor-setup
├── 2. 需求细化与功能列表 ─────────── brainstorming (Superpowers)
├── 3. 用户画像与用户旅程 ─────────── c4-context
├── 4. UI/UX 设计规范 ──────────────── mobile-design
├── 5. 整体文档编排与输出 ─────────── doc-coauthoring
```

| 排名 | Skill ID | 中文名 | 来源仓库 | 匹配度 |
|:----:|----------|--------|---------|:------:|
| 1 | **doc-coauthoring** | 文档协作编写 | antigravity-awesome-skills | 70% |
| 2 | **brainstorming** | 头脑风暴设计 | [obra/superpowers](https://github.com/obra/superpowers) | 65% |
| 3 | **conductor-setup** | 项目初始化 | antigravity-awesome-skills | 60% |
| 4 | **c4-context** | C4 上下文文档 | antigravity-awesome-skills | 55% |
| 5 | **mobile-design** | 移动端设计 | antigravity-awesome-skills | 50% |

---

## 二、安装方法

### 2.1 antigravity-awesome-skills（含 4 个 Skill）

包含：`doc-coauthoring`、`conductor-setup`、`c4-context`、`mobile-design`

#### 方式 A：官方安装器（推荐，一键安装全部 715 个 Skill）

```bash
npx antigravity-awesome-skills --cursor
```

若报 404，可用：

```bash
npx github:sickn33/antigravity-awesome-skills --cursor
```

#### 方式 B：手动链接（仅安装需要的 Skill）

```bash
# 假设项目中已有 skills 目录
SKILLS_SRC="/home/tsdl/SSD/CursorProject/CursorBase/04.CursorSkillProject/skills/skills"

mkdir -p ~/.cursor/skills

# 链接 4 个目标 Skill
ln -sf "$SKILLS_SRC/doc-coauthoring"   ~/.cursor/skills/doc-coauthoring
ln -sf "$SKILLS_SRC/conductor-setup"   ~/.cursor/skills/conductor-setup
ln -sf "$SKILLS_SRC/c4-context"        ~/.cursor/skills/c4-context
ln -sf "$SKILLS_SRC/mobile-design"     ~/.cursor/skills/mobile-design
```

> **注意**：需先确认 `$SKILLS_SRC` 路径下这些目录存在。若不存在，用方式 A 安装。

### 2.2 Superpowers（含 brainstorming）

#### 方式 A：Claude Code 插件（推荐）

```bash
/plugin marketplace add obra/superpowers-marketplace
/plugin install superpowers@superpowers-marketplace
```

#### 方式 B：手动安装到 Cursor

```bash
git clone --depth 1 https://github.com/obra/superpowers.git /tmp/superpowers
mkdir -p ~/.cursor/skills/brainstorming
cp /tmp/superpowers/skills/brainstorming/SKILL.md ~/.cursor/skills/brainstorming/
rm -rf /tmp/superpowers
```

---

## 三、各 Skill 详细说明与使用方法

---

### 3.1 brainstorming（头脑风暴 → 需求设计）⭐ 核心

**来源**：[obra/superpowers](https://github.com/obra/superpowers)（49,930+ Stars，TOP1 热门 Skill）

**核心能力**：
- 通过**苏格拉底式一问一答**，将模糊想法细化为完整设计规格
- 自动探索 2-3 种备选方案并给出推荐
- 分段展示设计文档（每段 200-300 字），逐段确认
- 输出完整设计文档到 `docs/plans/YYYY-MM-DD-<name>-design.md`

**工作流程**：

```
1. 理解想法 → 逐个提问（优先选择题）
2. 探索方案 → 提出 2-3 种方案 + 推荐
3. 呈现设计 → 分段展示，逐段验证
4. 输出文档 → 保存到 docs/plans/ 并提交 git
```

**设计文档覆盖内容**：
- 架构（Architecture）
- 组件（Components）
- 数据流（Data Flow）
- 错误处理（Error Handling）
- 测试策略（Testing）

**在 Cursor 中使用**：

```
# 方式 1：@ 引用
@brainstorming 我要设计一个 Android Camera App，需要支持拍照、录像、滤镜功能，请帮我细化需求。

# 方式 2：自然语言（自动触发）
帮我设计一个 Android Camera App 的功能列表和架构方案。
```

**Camera App 式样中的角色**：生成功能需求清单、技术方案选型、架构设计

---

### 3.2 doc-coauthoring（文档协作编写）

**来源**：antigravity-awesome-skills（架构与设计分类）

**核心能力**：
- 提供**结构化工作流**协作编写文档
- 支持文档类型：技术规格（technical specs）、提案（proposals）、决策文档（decision documents）
- 引导式文档编排，确保覆盖所有必要章节

**英文描述**：
> Guide users through a structured workflow for co-authoring documentation. Use when user wants to write documentation, proposals, technical specs, decision documents...

**触发关键词**：doc, coauthoring, documentation, write, proposals, technical specs, decision

**在 Cursor 中使用**：

```
# 方式 1：@ 引用
@doc-coauthoring 请帮我编写一份 Android Camera App 的完整技术规格文档（式样书），
包含产品概述、功能需求、UI 设计、技术架构、非功能需求等章节。

# 方式 2：组合使用
@doc-coauthoring @brainstorming 基于之前的头脑风暴结果，
帮我编排成正式的式样文档格式。
```

**Camera App 式样中的角色**：整体文档结构编排、章节组织、格式规范化

---

### 3.3 conductor-setup（项目初始化与产品定义）

**来源**：antigravity-awesome-skills（商业与营销分类）

**核心能力**：
- 用 **Conductor 工件**初始化项目
- 生成产品定义（Product Definition）
- 确定技术栈（Tech Stack）
- 建立工作流（Workflow）
- 制定风格指南（Style Guides）

**英文描述**：
> Initialize project with Conductor artifacts (product definition, tech stack, workflow, style guides)

**触发关键词**：conductor, setup, initialize, artifacts, product, definition, tech, stack, style, guides

**在 Cursor 中使用**：

```
# 使用方式
@conductor-setup 请为一个 Android Camera App 项目初始化以下内容：
- 产品定义文档（核心价值、目标用户、差异化）
- 技术栈选型（Kotlin + CameraX + Jetpack Compose）
- 开发工作流
- 代码风格指南
```

**Camera App 式样中的角色**：产品概述、目标定义、技术栈选型

---

### 3.4 c4-context（系统上下文与用户旅程）

**来源**：antigravity-awesome-skills（架构与设计分类）

**核心能力**：
- 生成**高层级系统上下文图**
- 记录用户画像（Personas）
- 描述用户旅程（User Journeys）
- 梳理系统功能（System Features）
- 标识外部系统依赖

**英文描述**：
> Expert C4 Context-level documentation specialist. Creates high-level system context diagrams, documents personas, user journeys, system features, and external...

**触发关键词**：c4, context, documentation, personas, user, journeys, features

**在 Cursor 中使用**：

```
# 使用方式
@c4-context 请为 Android Camera App 创建以下文档：
1. 用户画像（摄影爱好者、日常用户、专业用户）
2. 核心用户旅程（拍照流程、录像流程、编辑流程）
3. 系统上下文图（Camera App 与 OS Camera API、存储、云服务等的关系）
4. 外部系统依赖清单
```

**Camera App 式样中的角色**：用户画像、用户旅程图、系统上下文、外部依赖

---

### 3.5 mobile-design（移动端设计规范）

**来源**：antigravity-awesome-skills（开发与实现分类）

**核心能力**：
- 面向 iOS 与 **Android** 的**移动优先设计**与工程规范
- 涵盖触控交互（Touch Interaction）
- 性能优化（Performance）
- 平台约定（Platform Conventions）
- 离线行为（Offline Behavior）
- 移动端最佳实践

**英文描述**：
> Mobile-first design and engineering doctrine for iOS and Android apps. Touch interaction patterns, performance targets, platform-specific conventions, offline behavior, and mobile best practices.

**触发关键词**：mobile, design, ios, android, touch, performance, platform, offline

**在 Cursor 中使用**：

```
# 使用方式
@mobile-design 请为 Android Camera App 设计以下内容：
1. 触控交互规范（拍照按钮、缩放手势、滑动切换模式）
2. 界面布局设计（取景器、功能栏、设置面板）
3. 性能目标（启动时间、帧率、内存占用）
4. Android Material Design 3 适配规范
5. 离线模式处理（无网络时的功能降级）
```

**Camera App 式样中的角色**：UI 布局、交互规范、性能目标、平台适配

---

## 四、推荐使用顺序

### 第 1 步：项目初始化（conductor-setup）

```
@conductor-setup 为 Android Camera App 项目创建产品定义和技术栈选型文档。
目标用户：普通用户和摄影爱好者
核心功能：拍照、录像、滤镜、美颜、HDR
技术栈倾向：Kotlin + CameraX + Jetpack Compose
```

### 第 2 步：需求细化（brainstorming）

```
@brainstorming 基于产品定义，深入细化 Android Camera App 的每个功能模块。
请逐个功能提问，帮我想清楚每个细节。
```

### 第 3 步：用户旅程（c4-context）

```
@c4-context 为 Android Camera App 创建用户画像和核心用户旅程图。
```

### 第 4 步：UI/UX 设计（mobile-design）

```
@mobile-design 为 Android Camera App 设计完整的 UI/UX 规范，
包括界面布局、交互流程、手势操作、性能目标。
```

### 第 5 步：整合输出（doc-coauthoring）

```
@doc-coauthoring 将以上所有内容整合成一份完整的 Android Camera App 技术式样文档。
请按照标准式样书格式编排章节。
```

---

## 五、补充 Skill（可选）

如果需要更深入的某个方面，可以额外使用：

| Skill ID | 用途 | 何时使用 |
|----------|------|---------|
| **ui-ux-pro-max** | 自动生成设计系统（配色/字体/组件），支持 Jetpack Compose | 需要具体的设计系统文件时 |
| **senior-architect** | 技术架构深度设计（CameraX vs Camera2 选型等） | 需要深度技术架构分析时 |
| **architecture** | 架构决策记录（ADR） | 需要记录技术选型理由时 |
| **mobile-developer** | 移动端开发架构（MVVM、Clean Architecture） | 需要具体代码架构时 |
| **mobile-security-coder** | 移动端安全（权限管理、存储安全） | 需要安全规范时 |

---

## 六、搜索记录

### 检索数据来源

| 来源 | 技能总量 | 结果 |
|------|---------|------|
| awesomeagentskills.com | 41,295+ | 无专用式样生成 Skill |
| agent-skills.cc | 63,000+ | 无专用式样生成 Skill |
| skillsmp.com | 175K+ | 无专用式样生成 Skill |
| claudeskills.xyz | 13,225+ | 无专用式样生成 Skill |
| awesomeskills.dev | 2,025 | 无专用式样生成 Skill |
| prpm.dev | 7,500+ | 无专用式样生成 Skill |
| GitHub 全站 | - | 无专用式样生成 Skill |
| 本地 ~/.cursor/ | 5 个内置 | 无相关 |
| 本地项目索引 | 715 个已收录 | 上述 5 个最接近 |

*整理时间：2026-02-12*
