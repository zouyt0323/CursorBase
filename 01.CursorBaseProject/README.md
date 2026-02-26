# CursorBaseProject

本仓库是 **Cursor 项目结构与文档** 的模板与说明库，便于在 Cursor 中规范使用规则、命令、技能、子代理与 MCP。

---

## 文档清单与阅读顺序

**解释型文档**（说明 Cursor 用法与项目约定）已统一为 **`docs/cursor/`** 下的一份汇总文档；**功能性文档**（AGENTS.md、.cursor/commands、.cursor/skills、.cursor/agents）保持原有路径与命名。

| 文档 | 内容 |
|------|------|
| [**docs/cursor/cursor-完整说明.md**](docs/cursor/cursor-完整说明.md) | **汇总文档**：项目文件夹与文件说明、项目目录与资源约定、资源目录说明、Android 开发工具整理；含索引、按难易程度的阅读顺序、你可定义的内容与社区资源。 |
| [**docs/cursor/cursor-功能全景图.md**](docs/cursor/cursor-功能全景图.md) | **功能全景**：Agent 四大模式、Cloud Agent、CLI、BugBot、Hooks、Plugins、集成、知识覆盖度分析。 |
| [**docs/cursor/cursor-实战Cookbook.md**](docs/cursor/cursor-实战Cookbook.md) | **实战手册**：TDD、Git Commands、设计转代码、架构图、Agent 循环、Worktrees、BugBot 规则、Tab 优化。 |
| [**docs/cursor/cursor-Hooks与终端沙箱.md**](docs/cursor/cursor-Hooks与终端沙箱.md) | **Hooks 与沙箱**：事件钩子配置、实用脚本模板、sandbox.json 详解。 |
| [**docs/cursor/cursor-最佳实践与技巧.md**](docs/cursor/cursor-最佳实践与技巧.md) | **最佳实践**：上下文管理、Rules 编写、提示词技巧、Plugins 市场、版本更新、学习资源、快捷键。 |

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
