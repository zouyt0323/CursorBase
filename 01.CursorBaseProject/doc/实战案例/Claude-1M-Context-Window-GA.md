# Claude 1M 上下文窗口正式发布（GA）

> 来源：[claude.com/blog/1m-context-ga](https://claude.com/blog/1m-context-ga)
>
> 日期：2026-03-13
>
> 适用模型：Claude Opus 4.6 / Sonnet 4.6

---

## 核心公告

Claude Opus 4.6 和 Sonnet 4.6 的 **1M（100 万 token）上下文窗口**现已正式 GA，标准定价适用于整个窗口，无长上下文溢价。

## GA 新特性


| 特性                 | 详情                            |
| ------------------ | ----------------------------- |
| **无需 beta header** | 超过 200K token 的请求自动生效，无需代码变更  |
| **6x 媒体限制**        | 每次请求最多 600 张图片或 PDF 页面（原 100） |
| **标准速率限制**         | 整个窗口适用标准账户吞吐量                 |
| **统一定价**           | 无长上下文溢价                       |


## 定价


| 模型         | 输入          | 输出           |
| ---------- | ----------- | ------------ |
| Opus 4.6   | $5/百万 token | $25/百万 token |
| Sonnet 4.6 | $3/百万 token | $15/百万 token |


900K token 请求与 9K token 请求的每 token 费率相同。

## Claude Code 集成

- Max、Team、Enterprise 用户的 Opus 4.6 默认使用 1M 上下文
- 更少的 compaction（上下文压缩）事件
- 更多对话内容保持完整

## 性能基准

- Opus 4.6 在 MRCR v2 上得分 **78.3%**，前沿模型中最高
- 在整个 1M 窗口内保持准确性
- 每代模型的长上下文检索能力持续提升

## 实际用例

### 代码工程

> Claude Code 可以消耗 100K+ token 搜索 Datadog、Braintrust、数据库和源代码。以前 compaction 会导致细节丢失，陷入调试循环。有了 1M 上下文，可以搜索、再搜索、聚合边缘情况并提出修复方案——全部在一个窗口内完成。
>
> — Anton Biryukov, Software Engineer

### 大型文档处理

> 以前用户加载大型 PDF、数据集或图片时，我们不得不压缩上下文，丢失了最重要工作的保真度。1M 上下文后，compaction 事件减少了 15%。Agent 可以保持所有内容并运行数小时，不会忘记第一页读到的内容。
>
> — Jon Bell, CPO

### 代码审查

> Opus 4.6 的 1M 上下文使我们的 Devin Review agent 显著更有效。大型 diff 无法放入 200K 上下文窗口，agent 不得不分块处理上下文，导致更多遍历和跨文件依赖丢失。有了 1M 上下文，我们可以提供完整 diff 并从更简单、更高效的架构中获得更高质量的审查。
>
> — Adhyyan Sekhsaria, Founding Engineer

### 效率提升

> 我们将 Opus 上下文窗口从 200K 提升到 500K，agent 运行更高效——实际上总体使用更少的 token。更少的开销，更多专注于手头目标。
>
> — Izzy Miller, AI Research Lead

## 可用平台

- Claude Platform（原生）
- Amazon Bedrock
- Google Cloud Vertex AI
- Microsoft Foundry
- Claude Code（Max/Team/Enterprise）

## 参考链接

- [上下文窗口文档](https://platform.claude.com/docs/en/build-with-claude/context-windows)
- [定价详情](https://platform.claude.com/docs/en/about-claude/pricing)

