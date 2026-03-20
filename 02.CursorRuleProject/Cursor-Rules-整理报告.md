# Cursor Rules 整理报告

> 整理时间：2026-03-18
> 整理前：49 个 Rules（工程级 40 + 全局级 9）
> 整理后：32 个 Rules（工程级 27 + 全局级 5）
> 删除/合并：17 个

---

## 一、最终 Rules 清单

### 全局级 Rules（~/.cursor/rules/）— 5 个

| 文件 | 功能分类 | alwaysApply | 说明 |
|------|----------|-------------|------|
| `global-mcp-feedback.mdc` | 交互反馈 | true | Qt 交互式反馈规则（心跳、降级、tab 管理） |
| `auto-memory.mdc` | 记忆管理 | true | Memory MCP 自动存取规则 |
| `python.mdc` | Python 开发 | false | **合并后**的 Python 综合规范（编码/安全/测试/性能） |
| `creating-cursor-rules.mdc` | 元规则 | false | 创建 Cursor Rules 的最佳实践 |
| `android-jni-navigation.mdc` | Android 开发 | false | JNI 跨语言导航辅助 |

### 工程级 Rules（.cursor/rules/）— 27 个

#### 通用规则（7 个）

| 文件 | 功能分类 | 说明 |
|------|----------|------|
| `ecc-common-coding-style.md` | 编码风格 | 不可变性、文件组织、错误处理、输入验证 |
| `ecc-common-development-workflow.md` | 开发工作流 | 计划→TDD→审查→提交 |
| `ecc-common-git-workflow.md` | Git 规范 | 约定式提交、PR 流程 |
| `ecc-common-patterns.md` | 设计模式 | 仓库模式、API 响应、骨架项目、依赖注入 |
| `ecc-common-performance.md` | 性能优化 | 上下文管理、构建排错、缓存、数据库优化 |
| `ecc-common-security.md` | 安全规范 | 必检清单、密钥管理、漏洞防护 |
| `ecc-common-testing.md` | 测试规范 | 80%覆盖率、TDD、测试类型、自动化 |

#### Go 语言（4 个）

| 文件 | 功能 |
|------|------|
| `ecc-golang-coding-style.md` | Go 编码风格（gofmt、接口设计） |
| `ecc-golang-patterns.md` | Go 模式（Functional Options、错误处理） |
| `ecc-golang-security.md` | Go 安全（密钥管理、输入验证） |
| `ecc-golang-testing.md` | Go 测试（table-driven、race detection） |

#### Kotlin 语言（4 个）

| 文件 | 功能 |
|------|------|
| `ecc-kotlin-coding-style.md` | Kotlin 编码风格（ktfmt、不可变性） |
| `ecc-kotlin-patterns.md` | Kotlin 模式（sealed class、coroutine） |
| `ecc-kotlin-security.md` | Kotlin 安全（密钥管理、序列化） |
| `ecc-kotlin-testing.md` | Kotlin 测试（Kotest、MockK） |

#### PHP 语言（4 个）

| 文件 | 功能 |
|------|------|
| `ecc-php-coding-style.md` | PHP 编码风格（PSR-12、strict_types） |
| `ecc-php-patterns.md` | PHP 模式（thin controller、DTO） |
| `ecc-php-security.md` | PHP 安全（prepared statements、CSRF） |
| `ecc-php-testing.md` | PHP 测试（PHPUnit/Pest、coverage） |

#### Swift 语言（4 个）

| 文件 | 功能 |
|------|------|
| `ecc-swift-coding-style.md` | Swift 编码风格（SwiftFormat、let 优先） |
| `ecc-swift-patterns.md` | Swift 模式（Protocol-Oriented、Actor） |
| `ecc-swift-security.md` | Swift 安全（Keychain、ATS） |
| `ecc-swift-testing.md` | Swift 测试（Swift Testing、@Test） |

#### TypeScript 语言（4 个）

| 文件 | 功能 |
|------|------|
| `ecc-typescript-coding-style.md` | TS 编码风格（immutable spread、strict mode） |
| `ecc-typescript-patterns.md` | TS 模式（API Response、泛型） |
| `ecc-typescript-security.md` | TS 安全（env vars、输入验证） |
| `ecc-typescript-testing.md` | TS 测试（Playwright E2E） |

---

## 二、合并/删除详情

### 合并操作

| 合并组 | 源文件 | 目标文件 | 操作 |
|--------|--------|----------|------|
| Python 规范 | `python.mdc`(全局) + `python-pro.mdc`(全局) + `ecc-python-*.md`(工程级×5) | `python.mdc`(全局) | 7→1，中文化 |
| 测试规范 | `test-automator.mdc`(全局) + `ecc-common-testing.md`(工程级) | `ecc-common-testing.md`(工程级) | 2→1，中文化 |

### 删除操作

| 文件 | 位置 | 删除原因 |
|------|------|----------|
| `python-pro.mdc` | 全局 | 已合并到 python.mdc |
| `ecc-python-coding-style.md` | 工程级 | 已合并到 python.mdc |
| `ecc-python-hooks.md` | 工程级 | 已合并到 python.mdc |
| `ecc-python-patterns.md` | 工程级 | 已合并到 python.mdc |
| `ecc-python-security.md` | 工程级 | 已合并到 python.mdc |
| `ecc-python-testing.md` | 工程级 | 已合并到 python.mdc |
| `test-automator.mdc` | 全局 | 已合并到 ecc-common-testing.md |
| `code-reviewer.mdc` | 全局 | Claude Code agent 协议，Cursor 不适用 |
| `multi-agent-coordination.mdc` | 全局 | Claude Code 多 agent 协调，Cursor 不适用 |
| `creating-cursor-rules.mdc` | 工程级 | 与全局级完全重复 |
| `ecc-common-agents.md` | 工程级 | Claude Code 专属（~/.claude/agents/） |
| `ecc-common-hooks.md` | 工程级 | Claude Code hooks 系统（PostToolUse 等） |
| `ecc-golang-hooks.md` | 工程级 | Claude Code hooks 系统 |
| `ecc-kotlin-hooks.md` | 工程级 | Claude Code hooks 系统 |
| `ecc-php-hooks.md` | 工程级 | Claude Code hooks 系统 |
| `ecc-swift-hooks.md` | 工程级 | Claude Code hooks 系统 |
| `ecc-typescript-hooks.md` | 工程级 | Claude Code hooks 系统 |

---

## 三、冲突分析与解决

### 冲突 1：Python 规范（4 个来源）

| 来源 | 独特价值 | 处理 |
|------|----------|------|
| `python.mdc` | 最全面的基础框架（代码组织、设计模式、性能、安全、测试、陷阱） | 作为骨架 |
| `python-pro.mdc` | 核心哲学（迭代交付、TDD、质量门禁、简洁可读、SOLID） | 合并到开头 |
| `ecc-python-coding-style.md` | frozen dataclass、black/isort/ruff 工具链 | 补充到编码风格 |
| `ecc-python-patterns.md` | Protocol duck typing、Dataclass DTO | 补充到设计模式 |
| `ecc-python-security.md` | bandit 安全扫描 | 补充到安全规范 |
| `ecc-python-testing.md` | pytest.mark 分类 | 补充到测试规范 |

**解决**：合并为一个中文 `python.mdc`，保留所有独特内容，去除重复。

### 冲突 2：测试规范（3 个来源）

| 来源 | 独特价值 | 处理 |
|------|----------|------|
| `ecc-common-testing.md` | 80%覆盖率、TDD 工作流、测试类型 | 保留为基础 |
| `test-automator.mdc` | CI/CD 集成、自动化框架列表 | 合并 CI/CD 部分 |
| `python.mdc` 测试章节 | Python 特定测试 | 保留在 python.mdc 中 |

**解决**：通用测试规范保留在 `ecc-common-testing.md`，Python 特定测试在 `python.mdc` 中。

### 冲突 3：ECC 通用规则引用 Claude Code

**问题**：9 个 `ecc-common-*.md` 全部设置 `alwaysApply: true`，且引用了 `~/.claude/` 目录、planner agent 等 Claude Code 专属功能。

**解决**：
- 删除 2 个纯 Claude Code 文件（agents、hooks）
- 剩余 7 个改为 `alwaysApply: false`，翻译为中文，去除 Claude Code 引用

---

## 四、备份位置

```
02.CursorRuleProject/
├── rules-backup/
│   ├── global/          ← ~/.cursor/rules/ 的备份
│   │   ├── android-jni-navigation.mdc
│   │   ├── auto-memory.mdc
│   │   ├── creating-cursor-rules.mdc
│   │   ├── global-mcp-feedback.mdc
│   │   └── python.mdc
│   └── project/         ← .cursor/rules/ 的备份
│       ├── ecc-common-*.md (7 个)
│       ├── ecc-golang-*.md (4 个)
│       ├── ecc-kotlin-*.md (4 个)
│       ├── ecc-php-*.md (4 个)
│       ├── ecc-swift-*.md (4 个)
│       └── ecc-typescript-*.md (4 个)
├── Cursor-Rules-整理报告.md    ← 本文件
└── Cursor-Rules-Top50-分类清单.md
```

---

## 五、功能分类总览

| 分类 | Rules 数量 | 文件 |
|------|-----------|------|
| **交互反馈** | 1 | global-mcp-feedback.mdc |
| **记忆管理** | 1 | auto-memory.mdc |
| **元规则** | 1 | creating-cursor-rules.mdc |
| **Python 开发** | 1 | python.mdc |
| **Android 开发** | 1 | android-jni-navigation.mdc |
| **通用编码规范** | 7 | ecc-common-*.md |
| **Go 开发** | 4 | ecc-golang-*.md |
| **Kotlin 开发** | 4 | ecc-kotlin-*.md |
| **PHP 开发** | 4 | ecc-php-*.md |
| **Swift 开发** | 4 | ecc-swift-*.md |
| **TypeScript 开发** | 4 | ecc-typescript-*.md |
| **合计** | **32** | |
