# Anthropic Skills 中文说明文档

本目录包含对 **Anthropic 官方 Claude Skills** 的**分类索引**与**中文说明**。
数据来源：[https://github.com/anthropics/skills](https://github.com/anthropics/skills)

**未对 `skills` 文件夹做任何修改、新增或删除。**

## 文档结构

| 文件 | 说明 |
|------|------|
| [00_分类索引.md](00_分类索引.md) | 按分类总览，含各分类技能数量与链接 |
| skills_creative-design.md | **创意与设计**（4 个） |
| skills_development-technical.md | **开发与技术**（5 个） |
| skills_document-skills.md | **文档处理**（4 个） |
| skills_enterprise-communication.md | **企业与沟通**（3 个） |

## 每个技能的说明格式

每个技能均包含：

- **中文名**：该技能的中文名称，便于快速识别。
- **功能**：该技能能做什么，用中文详细解释其能力与侧重点；并保留**英文原文**便于对照。
- **使用领域**：该技能适用的技术/业务领域。
- **使用场景**：具体应在何时使用。
- **许可证**：开源（Apache 2.0）或专有（Proprietary）。

## 关于 Anthropic Skills

Skills 是 Claude 动态加载的指令、脚本和资源文件夹，用于提升特定任务的执行质量。
技能教会 Claude 以可重复的方式完成特定任务，无论是创建符合品牌规范的文档、分析数据，还是自动化个人任务。

更多信息请参考：
- [什么是 Skills？](https://support.claude.com/en/articles/12512176-what-are-skills)
- [在 Claude 中使用 Skills](https://support.claude.com/en/articles/12512180-using-skills-in-claude)
- [如何创建自定义 Skills](https://support.claude.com/en/articles/12512198-creating-custom-skills)

## 统计

- **总技能数**：16
- **分类数**：4（creative-design, development-technical, document-skills, enterprise-communication）
- **来源**：Anthropic 官方 GitHub 仓库 anthropics/skills
- **生成脚本**：`script/gen_anthropic_skills_doc.py`
