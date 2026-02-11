---
name: example-skill
description: 示例项目技能，演示 .cursor/skills 目录下技能的写法与用途。
---

# 示例技能（Example Skill）

本技能用于说明 **项目技能** 的目录与文件结构。

## 何时使用

当用户需要「按项目约定执行某类任务」时，可将步骤与约定写在此处，供 Agent 按 SKILL.md 执行。

## 技能目录结构

```
.cursor/skills/example-skill/
  SKILL.md       # 本文件，必选
  reference.md   # 可选：详细参考
  examples.md    # 可选：示例
  scripts/       # 可选：可执行脚本
```

## 可实现的技能示例

- 按团队规范做 Code Review
- 按指定格式生成 commit message
- 根据数据库/API 规范生成代码或文档
- 项目特有的构建、部署、检查流程

复制本目录并重命名即可创建新技能；同时可在《Cursor文件夹说明.md》中补充该技能的功能说明。
