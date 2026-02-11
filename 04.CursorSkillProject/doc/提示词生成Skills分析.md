# 提示词生成（Prompt Engineering/Generation）相关 Skills 分析

## 概述

提示词生成类 Skills 是 AI Agent 技能生态中非常重要的一类，涵盖从**提示词工程方法论**到**AI 图像提示词自动生成**等多种用途。本文整理了目前主流的提示词相关 Skills，并分析其在 Cursor 中的可用性。

---

## 一、推荐 Skills 总览

| 排名 | 技能名称 | 作者 | GitHub Stars | 核心功能 | Cursor 兼容 |
|------|----------|------|-------------|----------|------------|
| 1 | **skill-prompt-generator** | huangserva | 1,000+⭐（仓库） | AI 图像提示词智能生成系统（12 个子技能） | 是 |
| 2 | **prompting** | danielmiessler | 6,700+⭐（仓库） | 提示词工程标准和上下文工程原则 | 是 |
| 3 | **prompt-engineer** | amo-tech-ai | — | Claude 4 专业提示词工程 | 是 |
| 4 | **prompt-engineer** | avimaybee | — | 将模糊需求转化为优化提示词 | 是 |

> **其他相关元技能**（用于创建 Skill 本身，非直接用于提示词生成）：
> - **skill-creator**（OpenAI）— 创建 SKILL.md 的指导技能
> - **skill-writer**（PyTorch）— 技能编写辅助

---

## 二、详细分析

### 1. skill-prompt-generator（⭐ 最推荐）

**仓库**: [huangserva/skill-prompt-generator](https://github.com/huangserva/skill-prompt-generator)

#### 基本信息

| 项目 | 信息 |
|------|------|
| 作者 | huangserva |
| Stars | 1,017⭐ |
| 许可证 | MIT |
| 版本 | v2.0 |
| 子技能数 | 12 个 |
| 元素库 | 1,246+ 个元素 |
| 依赖 | Python 3.8+, SQLite |

#### 核心能力

这是一个**完整的 AI 图像提示词生成系统**，通过 12 个专业领域 Skills 和 Universal Elements Library 智能组合生成高质量提示词。

##### 三种生成模式

| 模式 | 说明 | 元素数 |
|------|------|--------|
| **Portrait（人像）** | 纯人像摄影，使用 portrait domain | 502 个 |
| **Cross-Domain（跨域）** | 复杂场景，自动组合多个 domains | 995 个 |
| **Design（设计）** | 海报/卡片，SQLite 元素 + YAML 配色 | 20 万+ 组合 |

##### 12 个子技能

| 技能 | 功能 |
|------|------|
| intelligent-prompt-generator | 人像提示词专家 |
| art-master | 艺术风格专家 |
| design-master | 平面设计专家 |
| product-master | 产品摄影专家 |
| video-master | 视频生成专家 |
| universal-learner | 学习系统（从新提示词提取元素） |
| prompt-analyzer | 提示词分析 |
| prompt-extractor | 元素提取 |
| prompt-generator | 通用生成器 |
| prompt-master | 主控调度 |
| prompt-xray | X-Ray 分析 |
| domain-classifier | 领域分类 |

##### 支持领域

| 领域 | 元素数 | 说明 |
|------|--------|------|
| portrait（人像） | 502 | 人像摄影 |
| common（通用） | 205 | 通用摄影技术 |
| design（设计） | 155 | 平面设计，含 5 个完整模板 |
| product（产品） | 77 | 产品摄影 |
| art（艺术） | 51 | 艺术风格 |
| video（视频） | 49 | 视频生成 |
| interior（室内） | — | 室内设计 |

##### 智能能力

- **语义理解**：区分主体/风格/氛围
- **常识推理**：自动推断合理属性（如人种 → 眼睛颜色）
- **一致性检查**：自动检测并修正逻辑冲突
- **框架驱动**：基于 `prompt_framework.yaml` 结构化生成
- **跨域查询**：自动识别所需 domains 并智能组合
- **自动学习**：从新提示词中提取元素，持续扩展知识库

#### 在 Cursor 中使用

```bash
# 1. 克隆项目
git clone https://github.com/huangserva/skill-prompt-generator.git

# 2. 安装依赖
cd skill-prompt-generator
pip install -r requirements.txt

# 3. 复制 Skills 到 Cursor
cp -r .claude/skills/* ~/.cursor/skills/

# 4. 在 Cursor 中使用
# 直接对话：「生成电影级的亚洲女性，张艺谋电影风格」
# 或：「生成龙珠悟空打出龟派气功的提示词」
# 或：「生成温馨可爱风格的儿童教育海报」
```

---

### 2. prompting（Daniel Miessler）

**仓库**: [danielmiessler/Personal_AI_Infrastructure](https://github.com/danielmiessler/Personal_AI_Infrastructure)

#### 基本信息

| 项目 | 信息 |
|------|------|
| 作者 | danielmiessler（AI 安全专家） |
| Stars | 6,700+⭐（仓库 Personal_AI_Infrastructure） |
| 定位 | 提示词工程方法论 |
| 基于 | Anthropic 官方最佳实践 |

#### 核心内容

基于 Anthropic「Effective Context Engineering for AI Agents」的提示词工程标准：

##### 核心哲学

**上下文工程** = 在 LLM 推理期间策划最优令牌集合

##### 关键原则

1. **上下文是有限资源**
   - LLM 有限「注意力预算」
   - 性能随上下文增长而下降
   - 每个 token 消耗容量

2. **优化信噪比**
   - 清晰直接的语言 > 冗长解释
   - 移除冗余信息
   - 聚焦高价值 token

3. **渐进式发现**
   - 使用轻量级标识符 vs 完整数据转储
   - 按需动态加载详细信息
   - 即时信息加载

##### 写作风格指南

| 类型 | 好的做法 | 不好的做法 |
|------|----------|-----------|
| 清晰度 | "Validate input before processing" | "You should always make sure to validate..." |
| 直接性 | "Use calculate_tax tool with amount" | "You might want to consider using..." |
| 结构化 | 要点列表 | 段落式需求 |

##### 反模式

- 冗长解释
- 历史上下文倾倒
- 重叠工具定义
- 过早信息加载
- 模糊指令（"might", "could", "should"）

#### 在 Cursor 中使用

```bash
# 克隆仓库
git clone --depth 1 https://github.com/danielmiessler/Personal_AI_Infrastructure.git /tmp/pai

# 查找 prompting 技能（PAI 仓库结构可能更新）
find /tmp/pai -name "SKILL.md" -path "*prompting*" 2>/dev/null

# 复制到 Cursor（路径以实际查找结果为准）
mkdir -p ~/.cursor/skills/prompting
cp /tmp/pai/.claude/skills/prompting/SKILL.md ~/.cursor/skills/prompting/
rm -rf /tmp/pai
```

> 注意：PAI 仓库目录结构可能随版本更新而变化，建议克隆后先确认 SKILL.md 的实际路径。

---

### 3. prompt-engineer（amo-tech-ai）

**仓库**: [amo-tech-ai/medellin-spark](https://github.com/amo-tech-ai/medellin-spark)

#### 基本信息

| 项目 | 信息 |
|------|------|
| 作者 | amo-tech-ai |
| 定位 | Claude 4 专业提示词工程 |
| 大小 | SKILL.md 12KB + README 8.7KB |

#### 核心内容

专为 **Claude 4 模型（Sonnet 4.5）** 优化的提示词工程指南：

1. **核心原则**
   - 清晰、直接、详细
   - 添加上下文提升性能
   - 显式指令（Claude 4 精确遵循指令）
   - 谨慎使用示例

2. **思维链（CoT）技术**
   - 基础 CoT：`Think step-by-step`
   - 引导式 CoT：分步分析
   - 结构化 CoT：`<thinking>` + `<answer>` 标签

3. **扩展思维（Extended Thinking）**
   - 适合复杂研究任务
   - 多上下文窗口工作流
   - 状态管理（JSON + 文本笔记）

4. **高级技术**
   - 输出格式控制
   - 工具使用模式
   - 并行工具调用
   - 减少幻觉
   - 研究和信息收集

5. **生产模式**
   - Agentic 编码模式
   - 视觉/前端代码模式
   - 交流风格控制

#### 在 Cursor 中使用

```bash
git clone https://github.com/amo-tech-ai/medellin-spark.git
mkdir -p ~/.cursor/skills/prompt-engineer
cp medellin-spark/.claude/archive/skills/prompt-engineer/SKILL.md ~/.cursor/skills/prompt-engineer/
```

---

### 4. prompt-engineer（avimaybee）

**仓库**: [avimaybee/refinery](https://github.com/avimaybee/refinery)

#### 核心功能

将用户模糊的请求转化为优化的、详细的 AI 编码 Agent 提示词，强调效率和清晰度。

#### 在 Cursor 中使用

```bash
git clone --depth 1 https://github.com/avimaybee/refinery.git /tmp/refinery

# 查找 prompt-engineer 技能目录
find /tmp/refinery -name "SKILL.md" -path "*prompt*" 2>/dev/null

# 复制到 Cursor（路径以实际查找结果为准）
mkdir -p ~/.cursor/skills/prompt-engineer
cp /tmp/refinery/.skills/prompt-engineer/SKILL.md ~/.cursor/skills/prompt-engineer/ 2>/dev/null || \
cp /tmp/refinery/.claude/skills/prompt-engineer/SKILL.md ~/.cursor/skills/prompt-engineer/
rm -rf /tmp/refinery
```

---

## 三、技能对比

| 特性 | skill-prompt-generator | prompting | prompt-engineer (amo) |
|------|----------------------|-----------|----------------------|
| **类型** | 生成工具 | 方法论 | 方法论 |
| **用途** | AI 图像提示词生成 | 提示词工程标准 | Claude 4 提示词优化 |
| **包含子技能** | 12 个 | 1 个 | 1 个 |
| **数据库** | 1,246+ 元素 | 无 | 无 |
| **Python 依赖** | 是 | 否 | 否 |
| **适合场景** | 图像生成（Midjourney/SD等） | 所有 AI 交互 | Claude 模型交互 |
| **学习曲线** | 中等 | 低 | 低 |
| **Cursor 兼容** | 是 | 是 | 是 |

---

## 四、其他相关资源

### 提示词收集平台

| 平台 | 地址 | 说明 |
|------|------|------|
| **SkillsMP** | [skillsmp.com](https://skillsmp.com) | 175K+ Agent Skills 市场 |
| **Agent Skills Guide** | [agentskills.guide](https://agentskills.guide) | 技能目录与安装指南 |
| **PRPM** | [prpm.dev](https://prpm.dev) | 7,500+ Cursor Rules/Skills |
| **PromptFlow** | [github.com/saran-io/promptflow](https://github.com/saran-io/promptflow) | 生产级提示词合集 |
| **Claude Skills** | [claudeskills.xyz](https://www.claudeskills.xyz) | 13,225+ 验证技能 |

### Cursor Rules（非 SKILL.md 格式）

| 项目 | 地址 | 说明 |
|------|------|------|
| cursor-rules-and-prompts | [thehimel/cursor-rules-and-prompts](https://github.com/thehimel/cursor-rules-and-prompts) | 201⭐，编码标准规则 |
| cursor_prompts | [DVC2/cursor_prompts](https://github.com/DVC2/cursor_prompts) | 11 条 .mdc 规则 |
| cursor-skills | [daniel-scrivner/cursor-skills](https://github.com/daniel-scrivner/cursor-skills) | 自动化工作流 |

---

## 五、推荐安装方案

### 场景一：AI 图像提示词生成

```bash
# 安装 skill-prompt-generator（完整系统）
git clone https://github.com/huangserva/skill-prompt-generator.git ~/.cursor/skills/prompt-generator-system
cd ~/.cursor/skills/prompt-generator-system && pip install -r requirements.txt
```

### 场景二：提升日常 AI 交互质量

```bash
# 安装 prompting 方法论
git clone --depth 1 https://github.com/danielmiessler/Personal_AI_Infrastructure.git /tmp/pai
mkdir -p ~/.cursor/skills/prompting
cp /tmp/pai/.claude/skills/prompting/SKILL.md ~/.cursor/skills/prompting/
rm -rf /tmp/pai
```

### 场景三：Claude 模型专业优化

```bash
# 安装 prompt-engineer
git clone --depth 1 https://github.com/amo-tech-ai/medellin-spark.git /tmp/medellin
mkdir -p ~/.cursor/skills/prompt-engineer
cp /tmp/medellin/.claude/archive/skills/prompt-engineer/SKILL.md ~/.cursor/skills/prompt-engineer/
rm -rf /tmp/medellin
```

### 场景四：全面覆盖

```bash
# 1. 方法论（无依赖，轻量）
git clone --depth 1 https://github.com/danielmiessler/Personal_AI_Infrastructure.git /tmp/pai
mkdir -p ~/.cursor/skills/prompting
cp /tmp/pai/.claude/skills/prompting/SKILL.md ~/.cursor/skills/prompting/ 2>/dev/null
rm -rf /tmp/pai

# 2. 生成工具（需要 Python 3.8+）
git clone https://github.com/huangserva/skill-prompt-generator.git /tmp/spg
cd /tmp/spg && pip install -r requirements.txt
cp -r .claude/skills/* ~/.cursor/skills/
cd - && rm -rf /tmp/spg
```

---

## 六、总结

| 需求 | 推荐技能 | 理由 |
|------|----------|------|
| **AI 图像提示词生成** | skill-prompt-generator | 1,246+ 元素库，12 个子技能，三种模式 |
| **提示词工程方法论** | prompting (danielmiessler) | 基于 Anthropic 最佳实践，简洁实用 |
| **Claude 深度优化** | prompt-engineer (amo-tech-ai) | 详细的 Claude 4 专属技巧 |
| **模糊需求优化** | prompt-engineer (avimaybee) | 自动转化模糊描述 |

> **建议**：方法论类技能（prompting/prompt-engineer）轻量无依赖，建议直接安装。生成工具类（skill-prompt-generator）功能强大但需要 Python 环境，按需安装。

---

*整理时间：2026-02-06*
*数据来源：GitHub、SkillsMP、AgentSkills.guide、WebSearch*
