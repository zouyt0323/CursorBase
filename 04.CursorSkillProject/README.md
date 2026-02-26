# Cursor Skills 资源

> Agent Skills 的分类文档、生成脚本与第三方技能仓库汇总，帮助快速发现和使用适合的 Skills。

---

## 目录结构

| 路径 | 说明 |
|------|------|
| `doc/` | Skills 分析文档与分类索引（约 30 篇） |
| `script/` | Python 文档生成脚本（从技能仓库自动生成索引文档） |
| `skills/` | 第三方技能仓库（独立 Git 仓库，需单独克隆） |
| `.cursor/skills/` | 项目内置技能（Android App 式样书生成） |

## 核心文档

| 文档 | 说明 |
|------|------|
| [热门Skills_TOP20.md](doc/热门Skills_TOP20.md) | 2026 年使用率最高的 20 个 Agent Skills 排行 |
| [Skills在Cursor中的使用分析.md](doc/Skills在Cursor中的使用分析.md) | Skills 的安装方式、工作原理与使用技巧 |
| [Android_开发相关_Skills.md](doc/Android_开发相关_Skills.md) | Android 开发者适用的 Skills 推荐 |
| [Figma与Cursor_UI制作方案分析.md](doc/Figma与Cursor_UI制作方案分析.md) | Figma + Cursor 的 UI 设计工作流 |
| [提示词生成Skills分析.md](doc/提示词生成Skills分析.md) | 提示词工程相关的 Skills 分析 |

## 第三方技能仓库

以下仓库在 `.gitignore` 中排除，需单独克隆到 `skills/` 目录下：

| 仓库 | 来源 | 技能数 |
|------|------|--------|
| `anthropics-skills` | [anthropics/skills](https://github.com/anthropics/skills) | 前端设计、MCP 构建、文档处理等 |
| `antigravity-awesome-skills` | [antigravity-ai/awesome-agent-skills](https://github.com/antigravity-ai/awesome-agent-skills) | 100+ 技能（开发、架构、测试、安全等） |
| `ui-ux-pro-max` | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | UI/UX 设计系统 |
| `vm0-skills` | 社区 | 80+ 技能（GitHub、Figma、Supabase 等） |

各仓库的分类索引见 `doc/` 下对应子目录的 README.md。

## 生成脚本

`script/` 下的 Python 脚本用于从技能仓库自动解析 `SKILL.md` 并生成分类索引文档：

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
python script/gen_skills_doc.py
```
