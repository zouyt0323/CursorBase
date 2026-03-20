---
description: "Git 工作流：约定式提交、PR 流程"
alwaysApply: false
---
# Git 工作流

## 提交信息格式

```
<type>: <description>

<可选正文>
```

类型：feat、fix、refactor、docs、test、chore、perf、ci

## Pull Request 流程

创建 PR 时：
1. 分析完整提交历史（不仅是最近一次）
2. 使用 `git diff [base-branch]...HEAD` 查看全部变更
3. 撰写完整的 PR 摘要
4. 包含带 TODO 的测试计划
5. 新分支推送时使用 `-u` 参数

> 关于规划、TDD、代码审查等完整开发流程，参见开发流程规则。
