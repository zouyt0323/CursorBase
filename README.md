# CursorBase

> Cursor 生态一站式资源与模板聚合工程——涵盖 Rules、Prompts、Skills、SubAgent、MCP、Lark 集成六大核心领域，从入门到进阶。

---

## 项目定位

为 Cursor IDE 使用者提供「一站式」参考、模板和资源链接：

- **规则（Rules）**：Top 50 分类索引 + awesome-cursorrules 1200+ 规则
- **提示词（Prompts）**：工作流、Android、UI/UX 设计、视频制作等场景
- **技能（Skills）**：4 大开源技能仓库的文档索引 + 内置 Android 式样生成技能 + 生成脚本
- **子代理（SubAgent）**：概念、配置、学习路径与 50+ 资源站
- **MCP**：13 个已安装服务说明 + TOP 20 热门排行 + 安装指南
- **飞书集成（Lark）**：MCP 集成、机器人开发、文档协作、自动化工作流

---

## 目录结构

| 目录 | 说明 | 关键内容 |
|------|------|----------|
| [`01.CursorBaseProject`](01.CursorBaseProject/) | Cursor 基础项目模板 | `.cursor/` 规则·命令·技能·Agent 模板，完整说明 + 功能全景图 |
| [`02.CursorRuleProject`](02.CursorRuleProject/) | Rules 规则分类与整理 | Top 50 分 8 类索引，示例规则正文，awesome-cursorrules 仓库 |
| [`03.CursorPromptProjet`](03.CursorPromptProjet/) | 各类场景提示词集合 | AI 网站资源、Android 全栈、UI/UX 设计、工作流、视频制作 |
| [`04.CursorSkillProject`](04.CursorSkillProject/) | Skills 文档·脚本·技能仓库 | 4 大技能仓库的分类文档、TOP 20 排行、Python 生成脚本 |
| [`05.CursorSubAgentProject`](05.CursorSubAgentProject/) | SubAgent 学习与资源 | 子代理概念与配置、Top 50 资源网站 |
| [`06.CursorMCPProject`](06.CursorMCPProject/) | MCP 服务配置指南 | 13 个已安装 MCP 详解、TOP 20 热门排行、7 个推荐安装指南 |
| [`07.CursorLarkProject`](07.CursorLarkProject/) | Cursor × 飞书集成方案 | MCP 集成、机器人开发、文档协作、自动化工作流 |

---

## 快速开始：按角色选择阅读路径

### Cursor 新手

1. [`01.CursorBaseProject/docs/cursor/cursor-完整说明.md`](01.CursorBaseProject/docs/cursor/cursor-完整说明.md) — 了解 Cursor 项目结构与核心概念
2. [`01.CursorBaseProject/docs/cursor/cursor-功能全景图.md`](01.CursorBaseProject/docs/cursor/cursor-功能全景图.md) — Agent 模式、Cloud Agent、CLI、BugBot 等功能全景
3. [`02.CursorRuleProject/rule/README.md`](02.CursorRuleProject/rule/README.md) — 学会选择和使用 Rules
4. [`06.CursorMCPProject/推荐MCP安装与使用指南.md`](06.CursorMCPProject/推荐MCP安装与使用指南.md) — 安装常用 MCP 服务

### 进阶使用者

1. [`04.CursorSkillProject/doc/热门Skills_TOP20.md`](04.CursorSkillProject/doc/热门Skills_TOP20.md) — 发现高效 Skills
2. [`05.CursorSubAgentProject/Cursor_SubAgent_学习内容整理.md`](05.CursorSubAgentProject/Cursor_SubAgent_学习内容整理.md) — 掌握子代理并行开发
3. [`03.CursorPromptProjet/工作流精选提示词集合.md`](03.CursorPromptProjet/工作流精选提示词集合.md) — 提升工作流效率

### Android / 移动端开发者

1. [`03.CursorPromptProjet/Android全栈开发精选提示词（按开发阶段+出处）.md`](03.CursorPromptProjet/Android全栈开发精选提示词（按开发阶段+出处）.md)
2. [`04.CursorSkillProject/doc/Android_开发相关_Skills.md`](04.CursorSkillProject/doc/Android_开发相关_Skills.md)
3. [`03.CursorPromptProjet/Android_iOS_UI_UX设计精选提示词集合.md`](03.CursorPromptProjet/Android_iOS_UI_UX设计精选提示词集合.md)

---

## 子仓库说明

以下目录为独立 Git 仓库，未包含在本仓库中。按需单独克隆：

| 子仓库路径 | 来源 | 克隆命令 |
|------------|------|----------|
| `02.CursorRuleProject/awesome-cursorrules` | [PatrickJS/awesome-cursorrules](https://github.com/PatrickJS/awesome-cursorrules) | `git clone https://github.com/PatrickJS/awesome-cursorrules.git 02.CursorRuleProject/awesome-cursorrules` |
| `04.CursorSkillProject/skills/anthropics-skills` | [anthropics/skills](https://github.com/anthropics/skills) | `git clone https://github.com/anthropics/skills.git 04.CursorSkillProject/skills/anthropics-skills` |
| `04.CursorSkillProject/skills/antigravity-awesome-skills` | [antigravity-ai/awesome-agent-skills](https://github.com/antigravity-ai/awesome-agent-skills) | `git clone https://github.com/antigravity-ai/awesome-agent-skills.git 04.CursorSkillProject/skills/antigravity-awesome-skills` |
| `04.CursorSkillProject/skills/ui-ux-pro-max` | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | `git clone https://github.com/nextlevelbuilder/ui-ux-pro-max-skill.git 04.CursorSkillProject/skills/ui-ux-pro-max` |
| `04.CursorSkillProject/skills/vm0-skills` | [anthropics/skills 或 vm0 社区](https://github.com/) | `git clone <url> 04.CursorSkillProject/skills/vm0-skills` |

---

## 相关资源速查

| 类别 | 推荐网站 |
|------|----------|
| Rules | [cursor.directory](https://cursor.directory/rules/popular) · [cursorlist.com](https://cursorlist.com/) · [prpm.dev](https://prpm.dev/) |
| Skills | [awesomeagentskills.com](https://awesomeagentskills.com/) · [awesomeskills.dev](https://awesomeskills.dev/) · [agent-skills.cc](https://agent-skills.cc/) |
| MCP | [mcp.so](https://mcp.so/) · [smithery.ai](https://smithery.ai/servers) · [pulsemcp.com](https://www.pulsemcp.com/servers) |
| 官方文档 | [cursor.com/docs](https://cursor.com/docs) |

---

## License

各子项目遵循其原有许可证。
