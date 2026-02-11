# Cursor Subagent 学习内容整理

> 面向「想系统学 Cursor 子代理与相关能力」的整理：概念、配置、与 Skills/Rules/Agent 的关系，以及推荐学习路径。  
> 基于官方文档与社区资料整理。

---

## 一、核心概念：什么是 Subagent（子代理）

### 1.1 定义

- **子代理**是独立的 AI 助手，由主 Agent **委派**具体任务。
- 每个子代理有**独立上下文窗口**，完成任务后把结果返回给父 Agent。
- 用途：拆分复杂任务、**并行执行**、保持主对话上下文简洁。

### 1.2 关键特性

| 特性 | 说明 |
|------|------|
| **上下文隔离** | 子代理有独立 context，长调研/探索不会占满主对话。 |
| **并行执行** | 可同时启动多个子代理，同时处理代码库不同部分。 |
| **专业能力** | 可为子代理配置专属提示词、工具权限、模型。 |
| **可复用** | 自定义子代理可在项目间复用。 |

### 1.3 运行模式：Foreground vs Background

| 模式 | 行为 | 适用场景 |
|------|------|----------|
| **Foreground（前台）** | 阻塞直到子代理完成，直接返回结果。 | 需要立刻拿到输出的顺序任务。 |
| **Background（后台）** | 立即返回，子代理在后台独立运行。 | 长时间任务或并行多条线。 |

---

## 二、内置子代理（Built-in Subagents）

无需配置，Agent 在合适场景下**自动**使用。

| 子代理 | 用途 | 为何做成子代理 |
|--------|------|----------------|
| **Explore** | 搜索、分析代码库 | 探索会产生大量中间结果，易撑爆主上下文；可用更快模型做大量并行搜索。 |
| **Bash** | 执行一系列 shell 命令 | 命令输出冗长，隔离后主 Agent 只做决策不看日志。 |
| **Browser** | 通过 MCP 控制浏览器 | 浏览器产生大量 DOM/截图，子代理过滤成简洁结果再上报。 |

共同点：中间输出多、适合专用提示/工具、耗 context；用子代理可隔离上下文、选不同模型、控制成本。

---

## 三、自定义子代理（Custom Subagents）

### 3.1 存放位置

- **项目级**：`.cursor/agents/`
- **用户级**：`~/.cursor/agents/`

### 3.2 文件格式

每个子代理一个 **Markdown 文件**，含 **YAML frontmatter**（name、description）+ 正文提示。

示例（可让 Agent 帮你生成）：

```markdown
---
name: verifier
description: 验证已完成工作，检查实现是否可用、跑测试并汇报通过/未完成项。
---

# Verifier 子代理

本子代理负责：
- 验证已完成的工作
- 检查实现是否可运行
- 运行测试
- 汇报通过项与未完成项
```

### 3.3 如何创建

- **方式一**：在 Composer 里用自然语言让 Agent 创建，例如：  
  「在 `.cursor/agents/verifier.md` 创建一个验证者子代理，YAML 里写 name、description，正文写提示词：验证完成工作、跑测试、汇报通过/未完成。」
- **方式二**：自己在 `.cursor/agents/` 下新建 `.md` 文件并按上述格式填写。

### 3.4 查看已配置子代理

- 看项目里的 `.cursor/agents/` 目录即可；
- Agent 会把该目录下的自定义子代理当作可用工具。

---

## 四、何时用 Subagent，何时用 Skill

| 更适合用 **Subagent** 时 | 更适合用 **Skill** 时 |
|-------------------------|------------------------|
| 需要**上下文隔离**的长调研/多步推理 | 单一目的任务（如生成 changelog、整理 import） |
| **多条线并行**（多子代理同时跑） | 希望一个**快速、可重复**的操作 |
| 任务需要**多步、跨领域**的专业能力 | 任务**一步就能完成** |
| 需要**独立验证**（例如专门一个子代理做测试与汇报） | 不需要单独上下文窗口 |

简单、单步类任务（如「生成 changelog」「格式化 import」）优先考虑 **Skill**，不必上子代理。

---

## 五、性能与成本（必读）

| 收益 | 代价 |
|------|------|
| 上下文隔离 | 每个子代理有**启动与收集上下文**的开销 |
| 并行执行 | **Token 用量成倍**（多个上下文同时跑） |
| 专业聚焦 | 简单任务可能比主 Agent **更慢**（子代理从零开始） |

注意：

- 子代理**各自计 token**，开 5 个子代理大约相当于 5 倍 token。
- 适合：复杂、长时间、可并行的任务；简单任务直接用主 Agent 更省更快。

---

## 六、与 Agent Skills 的关系（建议一起学）

### 6.1 Skills 是什么

- **Agent Skills**：用 **SKILL.md** 定义的、可复用的「技能包」——包含说明 + 可选脚本。
- 存在 `.cursor/skills/<skill-name>/SKILL.md`（或用户目录 `~/.cursor/skills/`）。
- Agent 启动时自动发现技能，根据上下文**自动选用**，也可通过输入 `/技能名` **手动触发**。

### 6.2 Skills 与 Subagent 分工

- **Skill**：偏「单次、可重复的动作」或「固定流程」——如部署、生成文档、跑某脚本。
- **Subagent**：偏「需要独立上下文、多步推理或并行」的任务——如全库探索、多模块并行修改、独立验证。

### 6.3 Skills 学习要点

1. **目录**：`.cursor/skills/<name>/`，内含 `SKILL.md`，可选 `scripts/`、`references/`、`assets/`。
2. **SKILL.md**：YAML 里至少写 `name`、`description`；正文写「何时用 + 步骤与规范」。
3. **脚本**：在 `SKILL.md` 里用相对路径引用 `scripts/` 下的可执行文件，Agent 会按说明执行。
4. **仅手动触发**：在 frontmatter 里设 `disable-model-invocation: true`，则只有输入 `/技能名` 时才会带上该技能。
5. **迁移**：Cursor 2.4 提供 `/migrate-to-skills`，可把「动态规则」和「斜杠命令」转成 Skills。

详细格式与示例见：[Agent Skills 官方文档](https://cursor.com/docs/context/skills)。

---

## 七、Agent 模式与 Subagent 的配合

- **Agent 模式**：可编辑代码、跑终端、用 MCP、**并可调度子代理与 Skills**。
- **Ask / Plan / Debug** 等模式：侧重不同任务类型，子代理主要在「Agent 模式」下被使用。
- **Terminal**：Agent（及 Bash 子代理）可执行 shell；**Browser**：由 Browser 子代理通过 MCP 控制浏览器。

理解「主 Agent → 选模式 → 必要时派发子代理 / 调用 Skill」即可。

---

## 八、推荐学习路径（按顺序）

1. **概念**  
   - 读本文「一、二」：Subagent 是什么、内置三个子代理做什么。  
   - 读官方：[Subagents](https://cursor.com/docs/context/subagents)。

2. **何时用**  
   - 读本文「四、五」：Subagent vs Skill、性能与成本。  
   - 再扫一眼 [Skills 文档](https://cursor.com/docs/context/skills) 的「What are skills」和「How skills work」。

3. **动手：自定义子代理**  
   - 在项目里建 `.cursor/agents/`，写一个简单的 `verifier.md`（或你需要的角色）；  
   - 在 Composer 里给一个「需要验证/检查」的任务，观察 Agent 是否调用该子代理。

4. **动手：Skills**  
   - 在 `.cursor/skills/` 下建一个带 `SKILL.md` 的技能（例如「生成 changelog」）；  
   - 用 `/技能名` 或自然语言触发，体会与子代理的差异。

5. **进阶**  
   - 看 [Agent Workflows](https://cursor.com/docs/cookbook/agent-workflows)、[Agent 概述](https://cursor.com/docs/agent/overview)；  
   - 按需看 [Terminal](https://cursor.com/docs/agent/terminal)、[Browser](https://cursor.com/docs/agent/browser)。

---

## 九、实践练习建议

| 练习 | 目标 |
|------|------|
| 在 `.cursor/agents/` 下新建一个「代码审查」子代理 | 熟悉 frontmatter + 提示词写法 |
| 给 Agent 一个「分析整个仓库并列出潜在问题」的任务 | 观察 Explore 等内置子代理是否被使用 |
| 创建一个「运行测试并汇总结果」的 Skill | 区分 Skill（单次流程）与 Subagent（独立上下文） |
| 用 `/migrate-to-skills` 迁移一条现有斜杠命令 | 理解从命令到 Skill 的迁移 |

---

## 十、官方与延伸阅读链接

| 主题 | 链接 |
|------|------|
| Subagents 官方文档 | https://cursor.com/docs/context/subagents |
| Agent Skills 官方文档 | https://cursor.com/docs/context/skills |
| Agent 概述 | https://cursor.com/docs/agent/overview |
| Agent 模式 | https://cursor.com/docs/agent/modes |
| Terminal | https://cursor.com/docs/agent/terminal |
| Browser | https://cursor.com/docs/agent/browser |
| Changelog 2.4（子代理 / Skills） | https://cursor.com/changelog、https://cursor.com/cn/changelog/2-4 |
| Agent Skills 开放标准 | https://agentskills.io |
| 社区 Skills 示例 | https://github.com/daniel-scrivner/cursor-skills |
| 中文 Agent Skills 教程 | https://cursor.zone/faq/cursor-agent-skills-guide.html |
| 中文子代理报道 | https://www.53ai.com/news/LargeLanguageModel/2026012303645.html |

---

## 十一、常见问题速查

- **内置子代理有哪些？**  
  Explore（代码库探索）、Bash（终端）、Browser（浏览器）。
- **子代理能再调子代理吗？**  
  以当前官方文档为准，一般建议以「主 Agent → 子代理」一层为主。
- **子代理失败会怎样？**  
  父 Agent 会收到失败或异常信息，可据此决定重试或改策略。
- **子代理里能用 MCP 吗？**  
  可以，子代理可配置工具访问权限（详见 Subagents 文档）。
- **为什么我这看不到子代理？**  
  若为按请求计费旧方案，需开启 **Max Mode**；按用量计费方案默认可用。

---

把「Subagent 学习」和「Skills + Agent 模式」一起看，更容易判断什么时候该用子代理、什么时候用 Skill 或主 Agent 就够了。若你希望针对某一块（例如只练自定义子代理或只练 Skills）再拆成更细的步骤，可以说明当前环境（是否已有 Cursor 2.4、是否在用 MCP），我可以按你的情况再写一版「最小可做清单」。
