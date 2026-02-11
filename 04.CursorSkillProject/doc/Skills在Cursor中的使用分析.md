# Skills 在 Cursor 中的使用分析

本文档分析项目中两个 Skills 仓库在 Cursor 中的兼容性和使用方式。

---

## 一、总体结论

| 仓库 | 技能数 | Cursor 兼容性 | 说明 |
|------|--------|--------------|------|
| antigravity-awesome-skills | 715 | **完全兼容** | 明确支持 Cursor，提供专用安装命令 |
| anthropics-skills | 16 | **部分兼容** | 主要为 Claude 设计，但 SKILL.md 格式通用 |

---

## 二、antigravity-awesome-skills（715 个技能）

### Cursor 兼容性：完全兼容

该仓库明确标注支持以下工具：
- Claude Code
- Gemini CLI
- Codex CLI
- **Cursor**（AI-native IDE）
- GitHub Copilot
- Antigravity IDE
- OpenCode / AdaL

### 在 Cursor 中的使用方式

**方法一：使用安装脚本**

```bash
npx antigravity-awesome-skills --cursor
```

**方法二：手动克隆**

```bash
git clone https://github.com/sickn33/antigravity-awesome-skills.git ~/.cursor/skills
```

**方法三：选择性安装（推荐）**

将需要的技能文件夹复制到 `~/.cursor/skills/` 目录下：

```bash
# 只安装特定技能
mkdir -p ~/.cursor/skills
cp -r skills/antigravity-awesome-skills/skills/rag-engineer ~/.cursor/skills/
cp -r skills/antigravity-awesome-skills/skills/python-expert ~/.cursor/skills/
```

**使用方式**：在 Cursor Chat 中输入 `@skill-name` 即可调用。

### 全部 715 个技能均可在 Cursor 中使用

涵盖 9 大分类：

| 分类 | 数量 | 示例技能 |
|------|------|----------|
| 架构与设计 | 63 | angular, architecture, microservices, ddd, event-driven |
| 商业与营销 | 38 | seo, copywriting, pricing, product-manager-toolkit |
| 数据与 AI | 99 | rag-engineer, llm-prompt, ml-pipeline, data-analysis |
| 开发与实现 | 83 | python-expert, react, rust, flutter, fastapi, django |
| 通用与综合 | 131 | debugging, documentation, code-review, git-pushing |
| 基础设施与运维 | 83 | kubernetes, terraform, docker, aws, ci-cd, monitoring |
| 安全与合规 | 114 | penetration-testing, security-audit, vulnerability-scanner |
| 测试与质量 | 23 | tdd, e2e-testing, unit-testing, performance-profiling |
| 工作流与协作 | 81 | changelog-automation, github-automation, slack-automation |

---

## 三、anthropics-skills（16 个技能）

### Cursor 兼容性分析

Anthropic 官方技能主要为 Claude Code / Claude.ai / Claude API 设计，但由于采用通用的 `SKILL.md` 格式，**大部分技能也可在 Cursor 中使用**。

#### 兼容性逐项分析

| 技能 | 中文名 | Cursor 可用 | 兼容度 | 说明 |
|------|--------|:-----------:|--------|------|
| **frontend-design** | 前端设计 | **是** | 高 | 纯指令型，提供 UI 设计最佳实践，Cursor 直接可用 |
| **mcp-builder** | MCP 服务器构建 | **是** | 高 | MCP 协议通用，Cursor 本身也支持 MCP |
| **skill-creator** | 技能创建器 | **是** | 高 | 指导创建 SKILL.md，格式通用 |
| **webapp-testing** | Web 应用测试 | **是** | 高 | Playwright 测试工具独立运行，与 AI 平台无关 |
| **doc-coauthoring** | 文档协作 | **是** | 高 | 纯工作流指导，Cursor 可直接使用 |
| **brand-guidelines** | 品牌规范 | **是** | 高 | 品牌色彩/字体参考，平台无关 |
| **internal-comms** | 内部沟通 | **是** | 高 | 沟通模板和指南，平台无关 |
| **algorithmic-art** | 算法艺术 | **是** | 中 | p5.js 代码生成可用，但 Cursor 不支持预览 |
| **canvas-design** | 画布设计 | **是** | 中 | 设计哲学可用，但 PDF/PNG 生成需额外工具 |
| **theme-factory** | 主题工厂 | **是** | 中 | 主题定义可用，但预览功能依赖 Claude |
| **slack-gif-creator** | Slack GIF 制作 | **是** | 中 | PIL/GIF 生成代码可用，需安装 Python 依赖 |
| **web-artifacts-builder** | Web 制品构建器 | **是** | 中 | React 构建可用，但 artifact 预览功能是 Claude 特有的 |
| **docx** | Word 文档处理 | **是** | 中 | Python 脚本可用，但需安装依赖（pandoc、LibreOffice 等） |
| **pdf** | PDF 文档处理 | **是** | 中 | pypdf 等 Python 库可用，需安装依赖 |
| **pptx** | PPT 演示文稿处理 | **是** | 中 | pptxgenjs/Python 脚本可用，需安装依赖 |
| **xlsx** | Excel 电子表格处理 | **是** | 中 | openpyxl 等库可用，需安装依赖 |

### 安装到 Cursor 的方法

```bash
# 将 Anthropic 技能复制到 Cursor 技能目录
mkdir -p ~/.cursor/skills

# 安装所有技能
for skill in skills/anthropics-skills/skills/*/; do
    cp -r "$skill" ~/.cursor/skills/
done

# 或选择性安装
cp -r skills/anthropics-skills/skills/frontend-design ~/.cursor/skills/
cp -r skills/anthropics-skills/skills/mcp-builder ~/.cursor/skills/
cp -r skills/anthropics-skills/skills/webapp-testing ~/.cursor/skills/
```

---

## 四、推荐使用策略

### 1. 在 Cursor 中优先使用 antigravity-awesome-skills

原因：
- 专门为 Cursor 等 AI 编码助手优化
- 715 个技能覆盖面广，几乎涵盖所有开发场景
- 带有 CATALOG 分类和触发词，AI 可自动匹配
- 社区活跃，持续更新

### 2. Anthropic Skills 作为补充

以下 Anthropic 技能在 antigravity-awesome-skills 中**没有对应项**或质量更高，推荐补充安装：

| 技能 | 推荐理由 |
|------|----------|
| **frontend-design** | Anthropic 出品，设计理念独特，强调避免「AI 风格」 |
| **mcp-builder** | 官方 MCP 开发指南，最权威 |
| **doc-coauthoring** | 结构化文档协作工作流，独特的三阶段流程 |
| **brand-guidelines** | Anthropic 品牌规范，制作相关文档时有用 |
| **docx/pdf/pptx/xlsx** | 文档处理能力强大，附带完整脚本和参考资料 |

### 3. 避免冲突

两个仓库中有同名技能，安装时需注意：
- `skill-creator` — 两边都有，Anthropic 版更简洁，antigravity 版功能更全
- `slack-gif-creator` — 两边都有，内容相似
- `webapp-testing` — 两边都有，Anthropic 版更聚焦

**建议**：同名技能只安装一个，优先选择 antigravity 版本（更适配 Cursor），文档处理类选 Anthropic 版本（更专业）。

---

## 五、注意事项

1. **不要安装全部 715 个技能**：会占用大量磁盘空间和增加 AI 上下文搜索时间。建议只安装当前项目需要的技能。
2. **Anthropic 文档处理技能的许可证**：docx、pdf、pptx、xlsx 为**专有软件**（Proprietary），仅供参考和学习，商业使用需注意许可限制。
3. **Python 依赖**：部分技能包含 Python 脚本，需要安装对应的 Python 包（如 pypdf、openpyxl、Playwright 等）。
4. **Cursor 版本要求**：确保使用支持 Skills 功能的 Cursor 版本。

---

*生成时间：2026-02-06*
*数据来源：antigravity-awesome-skills (715 技能) + anthropics-skills (16 技能)*
