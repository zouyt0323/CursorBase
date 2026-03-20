# Google Gemini CLI 完整报告 — 对标 Claude Code 的终端 AI 编程助手

> 来源：今日头条 @互联眼界 (2026-03-13) + 官方文档
> 原始链接：https://www.toutiao.com/w/1859552170790987/
> 整理时间：2026-03-15

---

## 一、项目概览

| 项目 | 信息 |
|------|------|
| **名称** | Gemini CLI |
| **开发者** | Google (google-gemini) |
| **GitHub** | https://github.com/google-gemini/gemini-cli |
| **官网** | https://geminicli.com |
| **文档** | https://google-gemini.github.io/gemini-cli/docs/ |
| **许可证** | Apache-2.0 |
| **语言** | TypeScript (98.1%) |
| **GitHub Star** | 97,700+ |
| **贡献者** | 450+ |
| **最新版本** | v0.35.0-nightly (2026-03-14) |

### 核心定位

Gemini CLI 是 Google 推出的**开源终端 AI 编程助手**，直接对标 Anthropic 的 Claude Code。它将 Gemini 模型的能力带入终端，提供交互式 REPL (Read-Eval-Print Loop) 环境。

### 三大王牌

1. **免费使用**：个人用户完全免费
2. **100 万上下文窗口**：Gemini 2.5 Pro / Gemini 3 驱动
3. **完全开源**：Apache-2.0 许可证

---

## 二、安装方法

### 方式一：npx 即时运行（推荐）

```bash
npx @google/gemini-cli
```

### 方式二：全局安装

```bash
npm install -g @google/gemini-cli
```

### 方式三：Homebrew (macOS)

```bash
brew install gemini-cli
```

### 方式四：Anaconda

```bash
conda install -c conda-forge gemini-cli
```

### 认证

首次使用需要 Google 账号登录认证，也可以使用 Gemini API Key：

```bash
# 使用 Google 账号（交互式登录）
gemini

# 使用 API Key
export GEMINI_API_KEY=your-key-here
gemini
```

---

## 三、Gemini CLI vs Claude Code 对比

| 维度 | Gemini CLI | Claude Code |
|------|-----------|-------------|
| **模型** | Gemini 2.5 Pro / Gemini 3 | Claude Sonnet/Opus |
| **上下文窗口** | **100 万 token** | ~20 万 token |
| **价格** | **个人免费** (60次/分, 1000次/天) | $20/月起 |
| **多模态** | **支持图片/视频** | 支持图片 |
| **MCP 支持** | 支持 | 支持 |
| **开源** | **Apache-2.0** | 不开源 |
| **代码质量** | 不错（持续改善中） | **公认更强** |
| **工具生态** | 内置 + 扩展 | 内置 + MCP |
| **IDE 集成** | VS Code 扩展 | Cursor/VS Code |

**总结**：Gemini CLI 赢在**免费 + 长上下文 + 开源**，Claude Code 赢在**代码质量**。

---

## 四、核心功能与内置工具

### 内置工具列表

| 工具 | 功能 | 说明 |
|------|------|------|
| `read_file` | 读取文件 | 支持任意文件格式 |
| `write_file` | 写入文件 | 创建或覆盖文件 |
| `read_many_files` | 批量读取 | 一次读取多个文件 |
| `run_shell_command` | 执行 Shell 命令 | 运行终端命令 |
| `google_web_search` | 网页搜索 | Google Search grounding |
| `web_fetch` | 网页获取 | 抓取网页内容 |
| `save_memory` | 保存记忆 | 跨会话记忆存储 |

### 特色功能

- **Checkpointing**：自动保存进度，可恢复中断的任务
- **Token Caching**：令牌缓存优化，减少重复请求
- **Trusted Folders**：信任文件夹安全机制
- **Themes**：支持自定义主题
- **Extensions**：可扩展架构，支持社区扩展

---

## 五、MCP 集成

### 配置方式

在项目根目录或全局配置中添加 `settings.json`：

```json
{
  "mcpServers": {
    "my-mcp-server": {
      "command": "npx",
      "args": ["-y", "@my/mcp-server"],
      "env": {
        "API_KEY": "your-key"
      }
    }
  }
}
```

### 支持的传输协议

- **Stdio**：标准输入输出
- **SSE**：Server-Sent Events
- **Streamable HTTP**：流式 HTTP

### MCP 配置优先级

命令行参数 → 环境变量 → 系统设置 → 项目设置 → 用户设置 → 系统默认 → 硬编码默认

---

## 六、100 万上下文的优势

### 一次读完整个项目
- 100 万 token ≈ **大约 75 万字**
- 一个中型项目的全部代码都能塞进上下文
- 不用手动选文件，直接说"帮我重构这个项目"

### 跨文件理解更准
- Claude Code 上下文有限，复杂项目经常忘记前面的代码
- Gemini CLI 能同时看到更多文件，跨文件引用更准确

### 实际使用示例

```bash
# 分析项目架构
$ gemini "分析整个 src 目录的架构，画出模块依赖图"

# 项目迁移
$ gemini "把这个 Express 项目迁移到 Fastify"

# 全局代码审查
$ gemini "检查整个项目的安全隐患，生成报告"

# 文档生成
$ gemini "为这个项目生成完整的 API 文档"
```

---

## 七、免费额度详情

| 用户类型 | 额度 | 费用 |
|---------|------|------|
| **个人用户** | 每分钟 60 次请求，每天 1000 次 | **免费** |
| **企业用户** | 按 API Key 计费，无限制 | 按量计费 |

### 价格对比

| 工具 | 月费用 |
|------|--------|
| Gemini CLI（个人） | **$0** |
| Claude Code | $20/月起 |
| Cursor Pro | $20/月 |

---

## 八、使用建议

### 选 Gemini CLI 的场景
- 预算有限，想零成本体验终端 AI 编程
- 项目很大，需要长上下文理解全局
- 需要多模态（图片/视频输入）
- 喜欢开源，想自己改造工具
- 需要 Google Search grounding

### 选 Claude Code 的场景
- 对代码质量要求极高
- 复杂重构和架构设计
- 需要更稳定的工具链和生态
- 已有 Anthropic 订阅

### 最佳方案
**两个都装，根据任务切换**：日常用 Gemini CLI（免费），关键任务用 Claude Code。

---

## 九、发布节奏

| 版本类型 | 频率 | 时间 |
|---------|------|------|
| **Nightly** | 每日 | 自动发布 |
| **Preview** | 每周 | 周二 23:59 UTC |
| **Stable** | 每周 | 周二 20:00 UTC |

---

## 十、与 Cursor 的关系

Gemini CLI 与 Cursor 并不冲突，可以互补使用：

| 场景 | 推荐工具 |
|------|---------|
| IDE 内辅助编码 | **Cursor**（GUI 更友好） |
| 终端批量操作 | **Gemini CLI**（终端原生） |
| 大项目全局分析 | **Gemini CLI**（100 万上下文） |
| 精细代码修改 | **Cursor**（即时预览） |
| CI/CD 集成 | **Gemini CLI**（命令行原生） |

---

## 附件

本目录包含原文的 6 张配图：

| 文件 | 内容 |
|------|------|
| img_01.jpg | 封面：Google 的回应来了，Gemini CLI 正式开源 |
| img_02.jpg | 和 Claude Code 正面对比表 |
| img_03.jpg | 100 万上下文能干啥？ |
| img_04.jpg | 免费额度够用吗？ |
| img_05.jpg | 我的使用建议 |
| img_06.jpg | 总结与安装命令 |

---

## 参考链接

- GitHub 仓库: https://github.com/google-gemini/gemini-cli
- 官方文档: https://google-gemini.github.io/gemini-cli/docs/
- 官网: https://geminicli.com
- MCP 集成指南: https://google-gemini.github.io/gemini-cli/docs/tools/mcp-server.html
- 配置指南: https://google-gemini.github.io/gemini-cli/docs/get-started/configuration.html
- 工具 API: https://google-gemini.github.io/gemini-cli/docs/core/tools-api.html
