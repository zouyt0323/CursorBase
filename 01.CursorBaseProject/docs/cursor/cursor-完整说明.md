# Cursor 完整说明（汇总文档）

本文档由原 `docs/cursor/` 下多份 cursor- 开头的 .md 合并而成，包含：Cursor 项目文件夹与文件说明、项目目录与资源约定、资源目录说明、Android 开发工具整理。**功能性文档**（AGENTS.md、.cursor/commands、.cursor/skills、.cursor/agents）保持原有路径，未纳入本汇总。

---

## 文档索引（本页内跳转）

| 部分 | 标题 | 内容概要 |
|------|------|----------|
| [第一部分](#第一部分cursor-项目文件夹与文件说明) | Cursor 项目文件夹与文件说明 | .cursor 目录、AGENTS.md、规则/命令/技能/子代理、@ 引用、MCP、高阶攻略、你可定义的内容与社区资源 |
| [第二部分](#第二部分项目目录与资源约定) | 项目目录与资源约定 | 式样（样式/模板）放哪里、图片/图标/音频/视频资源放哪里 |
| [第三部分](#第三部分资源目录assets-说明) | 资源目录（assets）说明 | assets/ 及各子目录用途 |
| [第四部分](#第四部分android-开发工具整理) | Android 开发工具整理 | 提示词、规则、技能、MCP 及使用例子 |

---

## 第一部分：Cursor 项目文件夹与文件说明

根据 [Cursor 官方帮助文档](https://docs.cursor.com) 整理，说明项目中与 Cursor 相关的**所有文件夹与根文件**的作用，并配有使用例子、高阶攻略、你可定义的内容与社区资源索引。

### 文档总览与按难易程度的阅读顺序

**本文档内建议阅读顺序（由易到难）：**

| 难易 | 建议顺序 | 看哪几节 | 为什么这样读 |
|------|----------|----------|--------------|
| 最容易 | 1 | **五** → **六** | 先看清「项目里已经有什么」，建立直观认识。 |
| 容易 | 2 | **一** → **二** | 再弄清 .cursor 四个子目录 + 根目录 AGENTS/.cursorignore。 |
| 容易 | 3 | **四** → **三** | 规则类型；用户级目录对照。 |
| 中等 | 4 | **七** | 日常怎么用：@ 引用、.cursorignore、MCP、快捷键。 |
| 进阶 | 5 | **八** | 按场景组合功能。 |
| 扩展 | 6 | **九** → **十** → **十一** | 延伸阅读、你可定义与社区资源、参考链接。 |

若做 Android 开发，在读完「五、六、一、二」后，可跳至本文档 [第四部分](#第四部分android-开发工具整理)。

### 文档索引（第一部分内跳转）

| 序号 | 章节 | 内容概要 |
|------|------|----------|
| **一** | [项目级 .cursor 目录](#一项目级cursor-目录) | rules / commands / skills / agents |
| **二** | [项目根目录文件](#二项目根目录文件) | AGENTS.md、.cursorignore |
| **三** | [用户级目录（参考）](#三用户级目录参考不在项目内创建) | ~/.cursor 下各目录 |
| **四** | [规则类型总览](#四规则类型总览官方四种) | 四种规则对比 |
| **五** | [本项目已创建结构](#五本项目已创建的目录与文件结构) | 目录树与示例文件 |
| **六** | [已创建文件功能说明](#六本项目已创建文件的功能说明) | 各示例文件功能 |
| **七** | [其他有帮助的内容](#七其他对-cursor-使用有帮助的内容) | @ 引用、MCP、快捷键等 |
| **八** | [高阶使用攻略](#八高阶使用攻略功能组合与效果) | 场景与组合 |
| **九** | [延伸阅读](#九延伸阅读与可能遗漏的内容) | Changelog、Forum、Tab 等 |
| **十** | [你可定义的内容与社区优质资源](#十你可定义的内容与社区优质资源) | 可配置清单 + 规则/MCP 检索 |
| **十一** | [参考链接](#十一参考链接) | 官方文档链接 |

---

### 一、项目级：`.cursor/` 目录

项目根目录下的 **`.cursor/`** 是 Cursor 的**项目配置目录**，可纳入 Git，与团队共享。下面四个子目录分别负责：规则、命令、技能、子代理。

#### 1. `.cursor/rules/`（项目规则）

| 项目 | 说明 |
|------|------|
| **作用** | 存放**项目规则**（Project Rules），为 AI 提供持久、可复用的上下文与约束。 |
| **适用** | 代码规范、项目约定、技术栈说明、文件/目录级别的规则等。 |
| **文件格式** | 使用 **`.mdc`**（Markdown Configuration），支持 YAML 前置元数据。 |
| **应用方式** | 可配置为：始终应用、按文件匹配自动附加、由 Agent 按需读取、或手动 @ 引用。 |

**规则文件示例结构：**

```yaml
---
description: 项目 TypeScript 规范简述
globs: "**/*.ts"
alwaysApply: false
---

# 规则正文（Markdown）
```

- `description`：规则简述（会在规则选择器中显示）。
- `globs`：文件匹配模式，如 `**/*.ts`、`src/components/**/*.tsx`。
- `alwaysApply`：为 `true` 时每次对话都会附带该规则。

**使用例子**：你在 `.cursor/rules/` 里放了一个 `react.mdc`，`globs` 设为 `**/*.tsx`。之后只要你在 Chat 里打开或 @ 了某个 `.tsx` 文件，这条规则会自动带上，AI 生成代码时会按你在规则里写的「用函数组件、用 Hooks」等要求来写。

#### 2. `.cursor/commands/`（项目命令）

| 项目 | 说明 |
|------|------|
| **作用** | 存放**项目级自定义命令**（斜杠命令），用 Markdown 描述命令行为与步骤。 |
| **适用** | 如「生成提交信息」「按团队规范做 PR 检查」等可重复执行的流程。 |
| **文件格式** | 使用 **`.md`** 文件。 |
| **作用域** | 仅当前项目；用户级命令在 `~/.cursor/commands/`。 |

**使用例子**：你在 `.cursor/commands/` 下新建了 `commit.md`，里面写了「读 git 暂存区 → 归纳 type/scope → 输出一条 commit 文案」。在 Chat 里输入对应命令名后，AI 会按这个文件的步骤执行，给你一段可直接用的 commit message。

#### 3. `.cursor/skills/`（项目技能）

| 项目 | 说明 |
|------|------|
| **作用** | 存放**项目级技能**（Skills），教 Agent 完成特定任务或工作流。 |
| **适用** | 如：按团队标准做 Code Review、按指定格式写 commit、查库表结构等。 |
| **结构** | 每个技能是一个**子目录**，目录内必须有 **`SKILL.md`**；可选子目录见下文「[Skill 文件夹内可有的目录](#skill-文件夹内可有的目录)」。 |
| **作用域** | 项目内共享；个人技能在 `~/.cursor/skills/`。 |

**注意**：不要使用 `~/.cursor/skills-cursor/`，该目录为 Cursor 内置技能保留。

##### Skill 文件夹内可有的目录

（据 [Cursor 文档 - 技能](https://cursor.com/cn/docs/context/skills)）

| 目录 | 用途 |
|------|------|
| **`scripts/`** | Agent 可运行的可执行代码（如 `deploy.sh`、`validate.py`），在 SKILL.md 中用相对路径引用。 |
| **`references/`** | 按需加载的附加文档（如 `REFERENCE.md`），便于保持 SKILL.md 简洁、渐进加载。 |
| **`assets/`** | 静态资源：模板、图片、数据文件等（如 `config-template.json`）。 |

示例结构：`my-skill/` 下含 `SKILL.md`，可选 `scripts/`、`references/`、`assets/` 三个子目录。

**使用例子**：你建了一个技能 `android-code-review`，SKILL.md 里写「检查生命周期、内存泄漏、是否在主线程操作 UI」。当你在 Composer 里说「按团队规范给这段 Android 代码做一次审查」时，Agent 会去读这个技能并按里面的检查清单输出审查结果。

#### 4. `.cursor/agents/`（项目子代理）

| 项目 | 说明 |
|------|------|
| **作用** | 存放**项目级子代理**（Subagents）定义，用于多代理协作或专用角色。 |
| **适用** | 为当前代码库定制的专用 Agent（如「前端规范检查」「API 契约校验」）。 |
| **文件格式** | **`.md`** 文件，描述该子代理的职责与行为。 |
| **作用域** | 当前项目，适合团队共享；用户级子代理在 `~/.cursor/agents/`。 |

**使用例子**：你在 `.cursor/agents/` 下放了一个 `api-checker.md`，写「只做一件事：对照 OpenAPI 文档检查当前文件里的接口调用是否一致」。之后在适合的任务里，可以指定用这个子代理，让 AI 只做接口校验。

---

### 二、项目根目录文件

#### 1. `AGENTS.md`

| 项目 | 说明 |
|------|------|
| **作用** | Agent 的**简易说明入口**，用 Markdown 写通用指引。 |
| **与 rules 的关系** | 可视为 `.cursor/rules` 的轻量替代：单文件、无 glob/alwaysApply 等配置。 |
| **适用** | 项目级通用说明：技术栈、代码风格、命名与目录约定、注意事项等。 |

**使用例子**：你在 AGENTS.md 里写「本项目用 TypeScript，禁止 any，接口用 interface」。之后每次在 Chat 里让 AI 写新函数或改代码，它都会默认遵守这些说明。

#### 2. `.cursorignore`

| 项目 | 说明 |
|------|------|
| **作用** | **控制 Cursor 的上下文与索引**：此处列出的路径不会被 @ 引用或语义搜索索引。 |
| **语法** | 与 `.gitignore` 类似。 |
| **常见用途** | 排除 `node_modules/`、`__pycache__/`、`.venv/`、构建产物、大文件等。 |

**使用例子**：你在项目根建了 `.cursorignore`，里面写 `node_modules/` 和 `dist/`。之后用 @Codebase 或语义搜索时，AI 不会把这些目录里的内容算进去。

---

### 三、用户级目录（参考，不在项目内创建）

| 路径 | 作用 |
|------|------|
| `~/.cursor/rules` | 用户级规则，对所有项目生效。 |
| `~/.cursor/commands/` | 用户级自定义命令，所有项目可用。 |
| `~/.cursor/skills/` | 用户级技能，所有项目可用。 |
| `~/.cursor/agents/` | 用户级子代理，所有项目可用。 |
| `~/.cursor/skills-cursor/` | Cursor 内置技能，**请勿在此创建或修改**。 |
| `~/.cursor/worktrees/` | 工作区相关数据。 |
| `~/.cursor/projects/` | 各项目的会话、MCP 等元数据。 |
| `~/.cursor/mcp-servers/`、`mcp.json` | MCP 服务器配置与数据。 |

---

### 四、规则类型总览（官方四种）

| 类型 | 位置 | 作用域 |
|------|------|--------|
| **项目规则** | `.cursor/rules/*.mdc` | 当前代码库，可版本控制 |
| **用户规则** | Cursor 设置中的 User Rules | 全局，所有项目 |
| **团队规则** | Cursor 团队后台 | 团队/企业计划 |
| **AGENTS.md** | 项目根目录 | 当前项目，单文件简易说明 |

---

### 五、本项目已创建的目录与文件结构

```
CursorBaseProject/
├── .cursor/
│   ├── rules/          # project-standards.mdc, file-specific.mdc, design-system.mdc
│   ├── commands/      # example-commit.md
│   ├── skills/         # example-skill/SKILL.md
│   └── agents/         # example-agent.md
├── assets/
│   ├── images/  icons/  audio/  video/
│   └── README.md
├── docs/
│   └── cursor/
│       └── cursor-完整说明.md   # 本汇总文档（原多份 cursor-*.md 已合并为此一份）
├── AGENTS.md
├── .cursorignore       # 可选，需自行创建
└── README.md
```

---

### 六、本项目已创建文件的功能说明

| 路径 | 类型 | 功能说明 |
|------|------|----------|
| `.cursor/rules/project-standards.mdc` | 规则 | 通用项目规范示例；alwaysApply: true。 |
| `.cursor/rules/file-specific.mdc` | 规则 | 按文件类型生效的规则示例；globs: "**/*.ts"。 |
| `.cursor/rules/design-system.mdc` | 规则 | 设计/样式规范示例；globs: "**/*.tsx"。 |
| `.cursor/commands/example-commit.md` | 命令 | 示例：根据暂存区生成提交信息。 |
| `.cursor/skills/example-skill/SKILL.md` | 技能 | 示例技能目录结构。 |
| `.cursor/agents/example-agent.md` | 子代理 | 示例子代理用途与扩展方式。 |
| `AGENTS.md` | 根文件 | Agent 简易说明入口。 |
| `docs/cursor/cursor-完整说明.md` | 文档 | 本汇总文档。 |

---

### 七、其他对 Cursor 使用有帮助的内容

#### 7.1 @ 引用

| 引用类型 | 说明 |
|----------|------|
| **@Codebase** | 对整个代码库做语义搜索。 |
| **@File / @Folder** | 引用指定文件或文件夹内容。 |
| **@Web** | 引用网页内容（URL）。 |
| **@Docs** | 引用已配置的文档源。 |

**使用例子**：能限定目录时先用 @Folder `src/auth` 再提问，AI 只基于该目录回答，更快更准。

#### 7.2 .cursorignore 与 .gitignore

`.cursorignore` 控制 Cursor 的索引与 @ 上下文；`.gitignore` 仅影响 Git。若希望 Cursor 也不索引某路径，需同时在 `.cursorignore` 中列出。

#### 7.3 代码库索引与语义搜索

Cursor 会对工作区做语义索引；使用 @Codebase 或 Agent 自动检索时会用到。索引质量受 `.cursorignore` 影响。

#### 7.4 MCP

**作用**：让 Cursor 调用外部工具（数据库、GitHub、Notion 等）。**配置位置**：项目级 `.cursor/mcp.json`，用户级 `~/.cursor/mcp.json`。在 Cursor 设置 **Features → MCP** 也可添加服务器。

#### 7.5 常用入口与快捷键

**Command Palette**：`Ctrl+Shift+P`（Windows/Linux）或 `Cmd+Shift+P`（Mac）。**Composer / Agent**：多文件编辑、任务型对话。**Chat**：单轮或短对话。**规则选择器**：在 Chat/Composer 中手动选择要附加的项目规则。

#### 7.6 使用建议

规则优先写清「做什么、不做什么」，用 `globs` 和 `alwaysApply` 控制范围。AGENTS.md 与 .cursor/rules 可二选一或搭配使用。用 `.cursorignore` 排除依赖与构建产物。能指定文件/文件夹时尽量用 @File / @Folder。

#### 7.7 使用前自检（常见遗漏）

| 检查项 | 说明 |
|--------|------|
| **.cursorignore** | 新项目或大仓建议配置，排除 `node_modules/`、`dist/`、`.venv/`、`__pycache__/` 等，避免 @Codebase 与语义搜索拖慢或跑偏。 |
| **规则不重复** | AGENTS.md 与 .cursor/rules 分工明确：要么以 AGENTS 为主、规则只做按文件/场景补充，要么以规则为主、AGENTS 只写一句话总则，避免同一约束写两遍。 |
| **globs 语法** | 规则里的 `globs` 与 .gitignore 类似（如 `**/*.ts`、`src/components/**/*.tsx`），写错会导致规则从不生效。 |
| **MCP 生效** | 若使用 MCP，需在 Cursor 设置 **Features → MCP** 或项目/用户 `mcp.json` 中正确配置并重启；服务需本机可执行。 |
| **技能目录结构** | 项目技能必须在 `.cursor/skills/<技能名>/` 下且包含 **SKILL.md**；不要使用 `~/.cursor/skills-cursor/`（Cursor 内置保留）。 |

---

### 八、高阶使用攻略：功能组合与效果

| 你想达到的效果 | 建议用的功能组合 |
|----------------|------------------|
| 代码风格统一、少返工 | AGENTS.md 或 alwaysApply 规则 + 按语言/目录的 glob 规则 |
| 大库下精准问答 | .cursorignore + @Folder / @Codebase + 规则里「先定位再回答」 |
| 提交/PR/发布流程统一 | commands + skills，必要时 + MCP |
| 专用角色（审查、校验） | agents 子代理 + 规则中的清单 |
| 结合文档与网页写代码 | @Docs / @Web + 规则中「参考某文档」 |
| 代码 + 外部系统联动 | MCP + skills/commands 或子代理 |

---

### 九、延伸阅读与可能遗漏的内容

| 主题 | 官方入口 |
|------|----------|
| Changelog | [cursor.com/changelog](https://www.cursor.com/changelog) |
| Forum | [forum.cursor.com](https://forum.cursor.com) |
| Cursor Tab、Bugbot、Shared Transcripts、CLI、Inline Edit | [docs.cursor.com](https://docs.cursor.com) |
| Agent 模式与安全、Subagents | [docs.cursor.com/agent](https://docs.cursor.com/agent/overview) |
| 键盘快捷键、主题、Worktrees、BYOK、故障排查、集成、Cookbook | [docs.cursor.com](https://docs.cursor.com) |

---

### 十、你可定义的内容与社区优质资源

#### 10.1 你可以自己定义的内容（清单）

| 类型 | 项目级位置 | 用户级位置 |
|------|------------|------------|
| 规则 | `.cursor/rules/*.mdc` | Cursor 设置 → Rules for AI |
| 命令 | `.cursor/commands/*.md` | `~/.cursor/commands/*.md` |
| 技能 | `.cursor/skills/<技能名>/SKILL.md` | `~/.cursor/skills/<技能名>/SKILL.md` |
| 子代理 | `.cursor/agents/*.md` | `~/.cursor/agents/*.md` |
| Agent 总说明 | 项目根 `AGENTS.md` | - |
| 上下文忽略 | 项目根 `.cursorignore` | - |
| MCP 服务器 | `.cursor/mcp.json` | `~/.cursor/mcp.json` |

#### 10.2 别人写好的规则/MCP 去哪检索

**规则**： [cursor.directory/rules](https://cursor.directory/rules)、[awesome-cursorrules](https://github.com/PatrickJS/awesome-cursorrules)、[awesome-cursor-rules-mdc](https://github.com/sanjeed5/awesome-cursor-rules-mdc)、[cursorrules.org](https://www.cursorrules.org)。

**MCP**： [cursor.directory/mcp](https://cursor.directory/mcp)、[mcpservers.com](https://mcpservers.com)、[cursormcp.dev/all](https://cursormcp.dev/all)、[cursormcp.com](https://cursormcp.com)。

---

### 十一、参考链接

- [Cursor 官方 - Rules / Commands / Skills / @ Mentions / Ignore Files](https://docs.cursor.com/context/rules)
- [Cursor Directory - Rules](https://cursor.directory/rules) | [Cursor Directory - MCP](https://cursor.directory/mcp)

---

## 第二部分：项目目录与资源约定

说明**式样（样式/模板）** 和 **图片、图标、音频、视频等资源** 应放在项目中的哪个文件夹。

### 式样（样式规范 / 模板）放哪里？

**若是「样式」——设计规范、UI 风格**  
→ 放在 **`.cursor/rules/`** 的 `.mdc`（如 `design-system.mdc`）或 **`AGENTS.md`**。样式源码（.css、.scss）放在项目源码目录（如 `src/styles/`），不要放进 `.cursor/`。

**若是「式样/模板」——文档或代码格式**  
→ **`.cursor/rules/`** 的某个 .mdc（说明 + 示例）；或 **`.cursor/skills/`**（SKILL.md + examples.md）；或用「一条命令」触发时放在 **`.cursor/commands/`** 的 .md。

**小结**：设计/UI 规范 → `.cursor/rules/` 下 `design-system.mdc` 等；格式/模板说明 → `.cursor/rules/` 或 `.cursor/skills/`；命令触发式样 → `.cursor/commands/`。

### 图片、图标、音频、视频资源放哪里？

**推荐**：统一放在 **`assets/`**（或 `src/assets/`），下设 `images/`、`icons/`、`audio/`、`video/`。

| 资源类型 | 建议文件夹 |
|----------|------------|
| 图片资源 | `assets/images/` |
| 图标（icon）资源 | `assets/icons/` |
| 音频（audio）资源 | `assets/audio/` |
| 视频（video）资源 | `assets/video/` |

不同项目类型：前端常用 `public/assets/` 或 `src/assets/`；React/Vite 常用 `src/assets/`；Android 用 `res/drawable/`、`mipmap/`、`raw/`；iOS 用 `Assets.xcassets` 等。本仓库采用 `assets/` + 子文件夹即可。

---

## 第三部分：资源目录（assets）说明

项目根目录下的 **`assets/`** 存放项目静态资源，按类型分子文件夹：

| 子目录 | 用途 |
|--------|------|
| `images/` | 图片（jpg, png, webp, gif, svg 等） |
| `icons/` | 图标（.ico, .svg 或图标字体等） |
| `audio/` | 音频（mp3, wav, ogg 等） |
| `video/` | 视频（mp4, webm 等） |

资源文件请放入上述对应子目录；不要将静态资源放在 `.cursor/` 下。

---

## 第四部分：Android 开发工具整理

Cursor 里对 **Android 开发** 有帮助的**提示词、规则、技能、MCP 服务**及相关资源。

### 提示词与规则

**[Cursor Directory - Android / Kotlin](https://cursor.directory/rules/android)** 提供「Senior Kotlin + Android」规则，要点：角色为资深 Kotlin + Android 程序员；Kotlin 通用（英文代码、类型声明、PascalCase/camelCase/snake_case、函数短小、data class、SOLID、测试 AAA）；Android 专项（Clean Architecture、Repository、MVI、Navigation Component、ViewBinding、Flow/LiveData、XML + Fragment、Material 3、ConstraintLayout）。  
若用 **Jetpack Compose**：Clean Architecture + Hilt、ViewModel + UI State、`remember`/`derivedStateOf`、LazyColumn/LazyRow、状态提升、@Preview；协程与 Flow、Compose 测试。

**使用方式**：简单项目可把规则放进 **AGENTS.md** 或 `.cursor/rules/android-kotlin.mdc`（alwaysApply: true）；多模块用多个 .mdc 按 glob 区分（如 `**/*.kt`、`**/ui/**/*.kt`）。

### 规则文件（.cursor/rules）

建议：`android-kotlin.mdc`（globs: `**/*.kt`）、`android-compose.mdc`（globs: `**/ui/**/*.kt` 或 `**/compose/**/*.kt`）。规则正文可从 [cursor.directory/rules/android](https://cursor.directory/rules/android) 复制，注意 HTML 转义（如 `&#x27;` → `'`）。

### 技能（Skills）

可自建：`android-code-review`（审查清单）、`android-commit`（提交信息格式）、`android-test-gen`（单元测试骨架）、`compose-preview`（@Preview 配置）。每技能一个目录，内含 **SKILL.md**（必选）。

### MCP 服务

- **Android-MCP（CursorTouch）**：通过 ADB 与无障碍 API 控制真机/模拟器；需 Python 3.10+、ADB、Android 10+。配置示例：`"command": "uvx", "args": ["android-mcp"]`。  
- **Mobile MCP**：iOS/Android 通用自动化。入口：[Cursor Directory - Mobile MCP](https://cursor.directory/mcp/mobile-mcp-ios-android-automation-and-development)。  
- Android 源码浏览类 MCP：可查 [MCP 目录](https://cursor.directory/mcp)。

### 推荐组合与使用建议

日常写 Android 代码：加 Android/Kotlin 规则（AGENTS.md 或 .cursor/rules/*.mdc），视情况加 Compose 规则。自动化点机/跑流程：配置 Android-MCP 或 Mobile MCP。大仓/多模块：.cursorignore + @Folder 限定模块。统一提交/审查：.cursor/commands 或 .cursor/skills 定义「生成 Android 提交信息」「按清单 Code Review」。

### 参考链接（Android）

- [Cursor Directory - Android / Kotlin Rules](https://cursor.directory/rules/android)
- [cursorrules.org - Android Jetpack Compose](https://www.cursorrules.org/article/android-jetpack-compose-cursorrules-prompt-file)
- [Android-MCP (CursorTouch)](https://github.com/CursorTouch/Android-MCP) | [Mobile MCP](https://cursor.directory/mcp/mobile-mcp-ios-android-automation-and-development)
- [Cursor 官方 - Rules / Skills / MCP](https://docs.cursor.com/context/rules)

---

## 参考链接汇总

- [Cursor 官方文档](https://docs.cursor.com)（Rules、Commands、Skills、@ Mentions、Ignore Files）
- [Cursor Directory - Rules](https://cursor.directory/rules) | [Cursor Directory - MCP](https://cursor.directory/mcp)
- [cursorrules.org](https://www.cursorrules.org) | [awesome-cursorrules](https://github.com/PatrickJS/awesome-cursorrules)

---

---

## 延伸文档

本文档聚焦 Cursor 项目结构与基础用法。以下功能在专题文档中详细介绍：

| 文档 | 内容 |
|------|------|
| [cursor-功能全景图.md](cursor-功能全景图.md) | Agent 四大模式、Cloud Agent、CLI、BugBot、Hooks、Plugins、集成、知识覆盖度分析 |
| [cursor-实战Cookbook.md](cursor-实战Cookbook.md) | TDD 工作流、Git Commands、代码库理解、设计转代码、架构图、Agent 循环、Worktrees、BugBot 规则模板、Tab 优化 |
| [cursor-Hooks与终端沙箱.md](cursor-Hooks与终端沙箱.md) | Hooks 事件列表与配置、实用脚本模板、终端沙箱 sandbox.json 配置 |
| [cursor-最佳实践与技巧.md](cursor-最佳实践与技巧.md) | Agent 最佳实践、上下文管理、Rules 编写、高效提示词、大型代码库策略、Plugins 市场、版本更新、学习资源、快捷键速查 |

---

*本文档根据 Cursor 帮助网站与技能文档整理，如有更新以官方文档为准。*
