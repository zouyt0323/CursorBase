# UI UX Pro Max 中文说明文档

本目录包含对 **UI UX Pro Max** 技能的中文详细分析文档。
数据来源：[https://github.com/nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)

**未对 `skills` 文件夹做任何修改、新增或删除。**

## 文档结构

| 文件 | 说明 |
|------|------|
| [README.md](README.md) | 本文件，概览与导航 |
| [功能详解.md](功能详解.md) | 功能、特性、数据资源的详细中文解释 |

## 技能概要

- **名称**：UI UX Pro Max
- **版本**：v2.0
- **许可证**：MIT 开源
- **GitHub**：[nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)
- **官网**：[uupm.cc](https://uupm.cc)

## 核心数据

| 资源 | 数量 | 说明 |
|------|------|------|
| UI 风格 | 67 种 | 从极简主义到赛博朋克，覆盖所有主流设计风格 |
| 配色方案 | 96 套 | 按行业分类（SaaS/电商/医疗/金融等） |
| 字体搭配 | 57 组 | 含 Google Fonts 导入链接 |
| UX 指南 | 99 条 | 无障碍、交互、性能、布局等最佳实践 |
| 图表类型 | 25 种 | 仪表板和数据分析推荐 |
| 推理规则 | 100 条 | 行业特定的设计系统生成规则 |
| 技术栈 | 13 个 | React/Next.js/Vue/Svelte/SwiftUI/Flutter 等 |

## Cursor 兼容性

**完全兼容**。支持以下安装方式：

```bash
# 方式一：CLI 安装（推荐）
npm install -g uipro-cli
cd /path/to/your/project
uipro init --ai cursor

# 方式二：手动安装
cp -r skills/ui-ux-pro-max/src/ui-ux-pro-max ~/.cursor/skills/ui-ux-pro-max
```

安装后在 Cursor 中自然对话即可触发，无需特殊命令。

## 生成脚本

`script/gen_uiux_doc.py` — 解析 ui-ux-pro-max 的 CSV 数据和 SKILL.md 并生成中文文档

## 统计

- **技能数**：1（单一综合技能）
- **数据文件**：18 个 CSV + 13 个技术栈 CSV
- **脚本文件**：3 个 Python 脚本（core.py、design_system.py、search.py）
- **平台支持**：15 个（Claude/Cursor/Windsurf/Copilot/Gemini/Codex 等）
