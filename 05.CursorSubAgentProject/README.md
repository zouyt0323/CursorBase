# Cursor SubAgent 资源

> Cursor 子代理（SubAgent）的概念、配置、学习路径与资源站整理。

---

## 文件清单

| 文件 | 说明 |
|------|------|
| [Cursor_SubAgent_学习内容整理.md](Cursor_SubAgent_学习内容整理.md) | 子代理概念、内置/自定义子代理、Skills/Rules/Agent 关系、学习路径 |
| [Cursor_SubAgent_Top50_网站整理.md](Cursor_SubAgent_Top50_网站整理.md) | Top 50 资源站：官方文档、MCP 目录、Rules/Skills/Agent 社区 |

## 核心概念速览

- **子代理**是由主 Agent 委派的独立 AI 助手，拥有独立上下文窗口
- **内置子代理**：Explore（代码探索）、Bash（命令执行）、Browser（浏览器自动化）
- **自定义子代理**：在 `.cursor/agents/` 中通过 `.md` 文件定义专属指令、工具和模型
- **运行模式**：前台（阻塞等待结果）和后台（并行执行长任务）

## 学习路径

1. 阅读 [学习内容整理](Cursor_SubAgent_学习内容整理.md) 了解子代理的基本概念
2. 参考 [01.CursorBaseProject/.cursor/agents/](../01.CursorBaseProject/.cursor/agents/) 中的配置示例
3. 通过 [Top 50 网站](Cursor_SubAgent_Top50_网站整理.md) 获取更多社区资源
