# CursorBase

> Cursor 生态一站式资源与模板聚合工程——涵盖 Rules、Prompts、Skills、SubAgent、MCP、Plan Mode、Memory、Plugin 八大核心领域，从入门到进阶。

---

## 项目定位

为 Cursor IDE 使用者提供「一站式」参考、模板和资源链接：

- **规则（Rules）**：Top 50 分类索引 + awesome-cursorrules 1235+ 规则 + Android RTL 适配指南
- **提示词（Prompts）**：工作流、Android、UI/UX 设计、视频制作等场景
- **技能（Skills）**：4 大开源技能仓库的文档索引 + 内置 Android 式样生成技能 + 生成脚本
- **子代理（SubAgent）**：概念、配置、学习路径与 50+ 资源站
- **MCP**：19 个已安装服务说明 + TOP 20 热门排行 + 安装指南
- **Plan Mode**：Plan Mode 完全指南、最佳实践、提示词模板、Cloud Agent、Hooks 集成
- **Memory & RAG**：AI 记忆系统、本地知识库（RAGFlow）、NAS 部署方案
- **Plugin**：Cursor 扩展插件管理（Cursor Usage 用量监控等）

---

## 目录结构

| 目录 | 说明 | 关键内容 |
|------|------|----------|
| [`01.CursorBaseProject`](01.CursorBaseProject/) | Cursor 基础项目模板 | `.cursor/` 规则·命令·技能·Agent 模板，完整说明 + 功能全景图 |
| [`02.CursorRuleProject`](02.CursorRuleProject/) | Rules 规则分类与整理 | Top 50 分 8 类索引，示例规则正文，awesome-cursorrules 仓库 |
| [`03.CursorPromptProjet`](03.CursorPromptProjet/) | 各类场景提示词集合 | AI 网站资源、Android 全栈、UI/UX 设计、工作流、视频制作 |
| [`04.CursorSkillProject`](04.CursorSkillProject/) | Skills 文档·脚本·技能仓库 | 4 大技能仓库的分类文档、TOP 20 排行、Python 生成脚本 |
| [`05.CursorSubAgentProject`](05.CursorSubAgentProject/) | SubAgent 学习与资源 | 子代理概念与配置、Top 50 资源网站 |
| [`06.CursorMCPProject`](06.CursorMCPProject/) | MCP 服务配置指南 | 19 个已安装 MCP 详解、TOP 20 热门排行、7 个推荐安装指南 |
| [`07.CursorPlanProject`](07.CursorPlanProject/) | Plan Mode 完全指南 | 核心功能、最佳实践、提示词模板、Cloud Agent、Hooks、版本演进 |
| [`08.CursorMemoryProject`](08.CursorMemoryProject/) | AI 记忆与知识库方案 | NAS 部署、Memory MCP、Qdrant 向量搜索、跨设备同步 |
| [`09.CursorPluginProject`](09.CursorPluginProject/) | Cursor 扩展插件管理 | Cursor Usage 用量监控插件、安装指南 |

---

## 快速开始：按角色选择阅读路径

### Cursor 新手

1. [`01.CursorBaseProject/docs/cursor/cursor-完整说明.md`](01.CursorBaseProject/docs/cursor/cursor-完整说明.md) — 了解 Cursor 项目结构与核心概念
2. [`01.CursorBaseProject/docs/cursor/cursor-功能全景图.md`](01.CursorBaseProject/docs/cursor/cursor-功能全景图.md) — Agent 模式、Cloud Agent、CLI、BugBot 等功能全景
3. [`02.CursorRuleProject/01-自研规则/README.md`](02.CursorRuleProject/01-自研规则/README.md) — 学会选择和使用 Rules
4. [`06.CursorMCPProject/推荐MCP安装与使用指南.md`](06.CursorMCPProject/推荐MCP安装与使用指南.md) — 安装常用 MCP 服务

### 进阶使用者

1. [`07.CursorPlanProject/README.md`](07.CursorPlanProject/README.md) — 掌握 Plan Mode，先规划再编码
2. [`04.CursorSkillProject/01-文档/01-排行与索引/热门Skills_TOP20.md`](04.CursorSkillProject/01-文档/01-排行与索引/热门Skills_TOP20.md) — 发现高效 Skills
3. [`05.CursorSubAgentProject/Cursor_SubAgent_学习内容整理.md`](05.CursorSubAgentProject/Cursor_SubAgent_学习内容整理.md) — 掌握子代理并行开发
4. [`03.CursorPromptProjet/工作流精选提示词集合.md`](03.CursorPromptProjet/工作流精选提示词集合.md) — 提升工作流效率

### Android / 移动端开发者

1. [`03.CursorPromptProjet/Android全栈开发精选提示词（按开发阶段+出处）.md`](03.CursorPromptProjet/Android全栈开发精选提示词（按开发阶段+出处）.md)
2. [`04.CursorSkillProject/01-文档/02-场景分析/Android_开发相关_Skills.md`](04.CursorSkillProject/01-文档/02-场景分析/Android_开发相关_Skills.md)
3. [`03.CursorPromptProjet/Android_iOS_UI_UX设计精选提示词集合.md`](03.CursorPromptProjet/Android_iOS_UI_UX设计精选提示词集合.md)

---

## 子仓库说明

以下目录为独立 Git 仓库，未包含在本仓库中。按需单独克隆：

| 子仓库路径 | 来源 | 克隆命令 |
|------------|------|----------|
| `02.CursorRuleProject/02-第三方规则/awesome-cursorrules` | [PatrickJS/awesome-cursorrules](https://github.com/PatrickJS/awesome-cursorrules) | `git clone ... 02.CursorRuleProject/02-第三方规则/awesome-cursorrules` |
| `04.CursorSkillProject/03-第三方技能/anthropics-skills` | [anthropics/skills](https://github.com/anthropics/skills) | `git clone ... 04.CursorSkillProject/03-第三方技能/anthropics-skills` |
| `04.CursorSkillProject/03-第三方技能/antigravity-awesome-skills` | [antigravity-ai/awesome-agent-skills](https://github.com/antigravity-ai/awesome-agent-skills) | `git clone ... 04.CursorSkillProject/03-第三方技能/antigravity-awesome-skills` |
| `04.CursorSkillProject/03-第三方技能/ui-ux-pro-max` | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | `git clone ... 04.CursorSkillProject/03-第三方技能/ui-ux-pro-max` |
| `04.CursorSkillProject/03-第三方技能/vm0-skills` | [vm0-ai/vm0-skills](https://github.com/vm0-ai/vm0-skills) | `git clone ... 04.CursorSkillProject/03-第三方技能/vm0-skills` |

---

## 相关资源速查

| 类别 | 推荐网站 |
|------|----------|
| Rules | [cursor.directory](https://cursor.directory/rules/popular) · [cursorlist.com](https://cursorlist.com/) · [prpm.dev](https://prpm.dev/) |
| Skills | [awesomeagentskills.com](https://awesomeagentskills.com/) · [awesomeskills.dev](https://awesomeskills.dev/) · [agent-skills.cc](https://agent-skills.cc/) |
| MCP | [mcp.so](https://mcp.so/) · [smithery.ai](https://smithery.ai/servers) · [pulsemcp.com](https://www.pulsemcp.com/servers) |
| 官方文档 | [cursor.com/docs](https://cursor.com/docs) |

---

## 文档维护指南

> 整理日期：2026-03-18，更新：2026-03-20

### 已消除的重复内容

| 原重复项 | 处理方式 |
|----------|----------|
| `04.CursorSkillProject` 中 antigravity 下的 Android Skills | 已删除，统一指向 `01-文档/02-场景分析/Android_开发相关_Skills.md` |
| `99.CursorOther` 中的扩展总览/Skills 总览/MCP 方案/OpenClaw 文档 | 已迁移到对应项目目录 |

### 文档索引（避免重复引用）

| 项目 | 关键文档位置 |
|------|-------------|
| 02.CursorRuleProject | 自研规则 `01-自研规则/`、第三方 `02-第三方规则/`、索引 `00-索引与清单/` |
| 04.CursorSkillProject | Android Skills 仅保留 `01-文档/02-场景分析/`、Skills 总览 `Cursor-Skills-Marketplace总览.md` |
| 09.CursorPluginProject | 扩展总览 `Cursor-Extensions-扩展总览.md`、推荐安装 `推荐安装插件列表.md` |
| 06.CursorMCPProject | OpenClaw 文档 `OpenClaw/`、MCP-Feedback 方案 `MCP-Feedback超时方案/` |

### 后续维护建议

1. **新增 Android 相关文档**：统一放在 `04/01-文档/02-场景分析/`，勿在 antigravity 索引下重复创建
2. **gen_skills_doc.py**：每次运行会覆盖 antigravity README，Android 链接已固化在脚本中指向场景分析
3. **插件文档**：推荐安装、使用指南、备份清单各司其职，避免内容交叉重复
4. **99.CursorOther**：仅存放不属于特定项目分类的资料，新文档应优先归入对应项目

---

## License

各子项目遵循其原有许可证。
