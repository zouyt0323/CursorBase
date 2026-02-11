# Cursor Skills 中文说明文档

本目录包含对 **Cursor Skills** 的**分类索引**与**中文说明**，便于查找每个技能的功能与使用方法。
**未对 `skills` 文件夹做任何修改、新增或删除。**

## 文档结构

| 文件 | 说明 |
|------|------|
| [00_分类索引.md](00_分类索引.md) | 按 CATALOG 的 9 大分类总览，含各分类技能数量与链接 |
| skills_architecture.md | **架构与设计**（63 个） |
| skills_business.md | **商业与营销**（38 个） |
| skills_data-ai.md | **数据与 AI**（99 个） |
| skills_development.md | **开发与实现**（83 个） |
| skills_general.md | **通用与综合**（131 个） |
| skills_infrastructure.md | **基础设施与运维**（83 个） |
| skills_security.md | **安全与合规**（114 个） |
| skills_testing.md | **测试与质量**（23 个） |
| skills_workflow.md | **工作流与协作**（81 个） |
| [Android_开发相关_Skills.md](Android_开发相关_Skills.md) | **Android 开发**：适用于 Android 系统开发的技能汇总 |
| [如何使用_Skills.md](如何使用_Skills.md) | 手把手教程：如何安装与使用 Cursor Skills |

## 每个技能的说明格式

每个技能均包含：

- **中文名**：该技能的英文 ID 对应的中文名称，便于快速识别。
- **功能**：该技能能做什么，用中文详细解释其能力与侧重点；并保留**英文原文**（首句）便于对照。
- **使用领域**：该技能适用的技术/业务领域，并附相关标签。
- **使用场景**：具体应在何时使用——例如「当……时」、以及对话中出现哪些关键词时会触发。
- **英文描述（原文）**：折叠块中保留 CATALOG 原始英文描述，便于对照。

## 如何查找技能

1. 从 [00_分类索引.md](00_分类索引.md) 确定大致分类。
2. 打开对应 `skills_<分类>.md`，用编辑器搜索技能 ID（如 `angular`、`rag-engineer`）。
3. 或在整个 `doc` 目录下全文搜索关键词（如「RAG」「SEO」「测试」）。

## 数据来源与更新

- 分类与技能列表来自仓库内 `skills/antigravity-awesome-skills/CATALOG.md`（只读，未修改）。
- 中文「功能」「使用方法」由脚本根据 CATALOG 描述与触发词自动生成；若需最准确说明，请以各技能目录下的 `SKILL.md` 为准。
- 生成脚本：`gen_skills_doc.py`

## 统计

- **总技能数**：715
- **分类数**：9（architecture, business, data-ai, development, general, infrastructure, security, testing, workflow）
