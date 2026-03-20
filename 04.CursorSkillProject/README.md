# Cursor Skills 资源

> Agent Skills 的分类文档、生成脚本与第三方技能仓库汇总，帮助快速发现和使用适合的 Skills。

---

## 目录结构

| 路径 | 说明 |
|------|------|
| `01-文档/` | Skills 分析文档与分类索引（排行、场景分析、评测、第三方索引、完整指南） |
| `02-脚本/` | Python 文档生成脚本（从技能仓库自动生成索引文档） |
| `03-第三方技能/` | 第三方技能仓库（anthropics、antigravity、everything-claude-code、ui-ux、vm0） |
| `04-备份/` | skills、rules 备份及整理报告 |
| `.cursor/skills/` | 项目内置技能（Android App 式样书生成） |

## 核心文档

| 文档 | 说明 |
|------|------|
| [热门Skills_TOP20.md](01-文档/01-排行与索引/热门Skills_TOP20.md) | 2026 年使用率最高的 20 个 Agent Skills 排行 |
| [Skills在Cursor中的使用分析.md](01-文档/01-排行与索引/Skills在Cursor中的使用分析.md) | Skills 的安装方式、工作原理与使用技巧 |
| [Android_开发相关_Skills.md](01-文档/02-场景分析/Android_开发相关_Skills.md) | Android 开发者适用的 Skills 推荐 |
| [Figma与Cursor_UI制作方案分析.md](01-文档/02-场景分析/Figma与Cursor_UI制作方案分析.md) | Figma + Cursor 的 UI 设计工作流 |
| [提示词生成Skills分析.md](01-文档/02-场景分析/提示词生成Skills分析.md) | 提示词工程相关的 Skills 分析 |

## 第三方技能仓库

以下仓库在 `.gitignore` 中排除，需单独克隆到 `03-第三方技能/` 目录下：

| 仓库 | 来源 | 技能数 |
|------|------|--------|
| `anthropics-skills` | [anthropics/skills](https://github.com/anthropics/skills) | 17 个技能（Claude API、前端设计、MCP 构建、文档处理等） |
| `antigravity-awesome-skills` | [antigravity-ai/awesome-agent-skills](https://github.com/antigravity-ai/awesome-agent-skills) | 1945+ 技能（开发、架构、测试、安全等） |
| `ui-ux-pro-max` | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | UI/UX 设计系统（v2.2.1） |
| `everything-claude-code` | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | 94 技能 + 39 规则 + 19 Agents + 50+ Commands（Anthropic 黑客马拉松获奖作品） |
| `vm0-skills` | [vm0-ai/vm0-skills](https://github.com/vm0-ai/vm0-skills) | 84 个技能（GitHub、Figma、Google、Vercel、X 等） |

各仓库的分类索引见 `01-文档/04-第三方技能索引/` 下对应子目录的 README.md。

### everything-claude-code 安装详情

该仓库已全部安装到 Cursor：

| 类型 | 数量 | 安装位置 |
|------|------|----------|
| Cursor Rules | 39 | `.cursor/rules/ecc-*.md`（工程级） |
| Cursor Skills | 94 | `~/.cursor/skills-cursor/ecc-*/`（全局） |
| Agents | 19 | 参考用，位于 `skills/everything-claude-code/agents/` |
| Commands | 50+ | 参考用，位于 `skills/everything-claude-code/commands/` |
| MCP 配置 | 17 | 参考用，位于 `skills/everything-claude-code/mcp-configs/` |

覆盖语言：Python / TypeScript / Go / Kotlin / Swift / PHP / Perl / C++

关键 Skills（按场景分类）：
- **编码规范**：coding-standards, python-patterns, golang-patterns, kotlin-patterns
- **安全**：security-review, security-scan
- **测试**：tdd-workflow, python-testing, golang-testing, e2e-testing
- **架构**：api-design, backend-patterns, frontend-patterns, deployment-patterns
- **AI/Agent**：agentic-engineering, autonomous-loops, continuous-learning, cost-aware-llm-pipeline
- **研究**：deep-research, market-research, exa-search
- **内容**：article-writing, content-engine, frontend-slides

## 生成脚本

`02-脚本/` 下的 Python 脚本用于从技能仓库自动解析 `SKILL.md` 并生成分类索引文档：

| 脚本 | 用途 |
|------|------|
| `gen_skills_doc.py` | 生成 antigravity-awesome-skills 文档 |
| `gen_anthropic_skills_doc.py` | 生成 anthropics-skills 文档 |
| `gen_uiux_doc.py` | 生成 ui-ux-pro-max 文档 |
| `gen_vm0_skills_doc.py` | 生成 vm0-skills 文档 |

运行方式（需先激活虚拟环境）：

```bash
cd 04.CursorSkillProject
source .venv/bin/activate
python 02-脚本/gen_skills_doc.py
```
