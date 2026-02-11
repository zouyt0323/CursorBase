# 示例命令：生成提交信息

本文件展示 `.cursor/commands` 下命令文件的用法。在 Chat/Composer 中可通过对应命令名触发。

## 命令目的

根据当前暂存区变更，生成符合项目规范的 Git 提交信息（可约定格式如 type(scope): message）。

## 执行步骤（供 AI 参考）

1. 读取 `git diff --cached` 或等价信息。
2. 归纳变更类型（feat/fix/docs/style/refactor/test/chore）与影响范围。
3. 用中文或英文写一句简洁的 subject，必要时加 body。
4. 输出最终提交信息供用户复制使用。

可将本文件重命名或复制为其他命令（如 `pr-check.md`、`run-tests.md`），并在文档中说明各命令功能。
