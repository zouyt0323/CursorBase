# CursorBaseProject

本仓库是 **Cursor 项目结构与文档** 的模板与说明库，便于在 Cursor 中规范使用规则、命令、技能、子代理与 MCP。

---

## 文档清单与阅读顺序

**解释型文档**（说明 Cursor 用法与项目约定）已统一为 **`docs/cursor/`** 下的一份汇总文档；**功能性文档**（AGENTS.md、.cursor/commands、.cursor/skills、.cursor/agents）保持原有路径与命名。

| 文档 | 内容 |
|------|------|
| [**docs/cursor/cursor-完整说明.md**](docs/cursor/cursor-完整说明.md) | **汇总文档**：项目文件夹与文件说明、项目目录与资源约定、资源目录说明、Android 开发工具整理；含索引、按难易程度的阅读顺序、你可定义的内容与社区资源。 |

按**难易程度**的阅读顺序见 [文档总览与按难易程度的阅读顺序](docs/cursor/cursor-完整说明.md#文档总览与按难易程度的阅读顺序)。若想知道「自己能定义什么」和「别人写好的规则/MCP 去哪找」，见 [十、你可定义的内容与社区优质资源](docs/cursor/cursor-完整说明.md#十你可定义的内容与社区优质资源)。

---

## 当前结构概览

| 路径 | 说明 |
|------|------|
| `.cursor/` | 项目级配置：rules、commands、skills、agents（**功能性**，保持路径）。 |
| `AGENTS.md` | Agent 简易说明入口（**功能性**，保持根目录）。 |
| `docs/cursor/` | **解释型文档**：以 cursor- 开头的 .md 汇总。 |
| `assets/` | 资源目录：images、icons、audio、video。 |
| `README.md` | 本文件，仓库入口与文档索引。 |

详细说明与已创建文件列表见 [cursor-完整说明.md](docs/cursor/cursor-完整说明.md)。
