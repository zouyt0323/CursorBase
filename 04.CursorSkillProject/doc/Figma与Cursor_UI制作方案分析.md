# Figma 与 Cursor UI 制作方案分析

本文档分析在 Cursor 中结合 Figma 进行 UI 设计和代码生成的各种方案。

---

## 一、方案总览

| 方案 | 类型 | 推荐度 | GitHub Stars | 说明 |
|------|------|:------:|:------------|------|
| **Figma 官方 MCP Server** | MCP Server | 最推荐 | 官方 | Figma 设计稿 → 代码，最稳定 |
| **cursor-talk-to-figma-mcp** | MCP Server | 推荐 | 6,273+ | 社区热门，双向操作 Figma |
| **figma-automation** | Agent Skill | 已有 | — | antigravity-awesome-skills 中已包含 |
| **vm0-ai/figma** | Agent Skill | 可选 | — | REST API 方式（设计文件只读，评论可读写） |

---

## 二、方案详解

### 方案一：Figma 官方 MCP Server（最推荐）

**来源**：Figma 官方（v127+）
**文档**：[developers.figma.com/docs/figma-mcp-server](https://developers.figma.com/docs/figma-mcp-server/)

#### 功能

- 从 Figma 设计稿直接生成像素级精确的代码
- 提取设计上下文（变量、组件、布局数据、文本样式）
- 通过 Code Connect 复用实际设计系统组件
- 保持与设计系统的一致性
- 支持 Make 文件的资源检索

#### 安装步骤

1. **启用 Figma Dev Mode MCP Server**：
   - 打开 Figma 桌面版（v127+）
   - 进入 Preferences → Dev Mode
   - 启用 MCP Server

2. **在 Cursor 中配置**：
   - 打开 Cursor Settings → MCP
   - 添加新的 MCP Server：

```json
{
  "mcpServers": {
    "figma": {
      "url": "http://127.0.0.1:3845/mcp"
    }
  }
}
```

3. **使用**：
   - 在 Cursor Composer（Agent 模式）中
   - 粘贴 Figma 文件/框架/组件的链接
   - 让 Cursor 实现设计

#### 使用示例

```
请根据这个 Figma 设计实现页面：
https://www.figma.com/design/xxxxx/MyProject?node-id=1234

使用 React + Tailwind CSS，保持与设计稿一致。
```

---

### 方案二：cursor-talk-to-figma-mcp（社区 MCP）

**来源**：Grab 团队（开源）
**GitHub**：[grab/cursor-talk-to-figma-mcp](https://github.com/grab/cursor-talk-to-figma-mcp)
**Stars**：6,273+

#### 功能

- Cursor AI 与 Figma 双向实时通信（WebSocket）
- 创建框架、矩形、文本元素
- 克隆/移动/调整节点大小
- 批量文本替换
- 组件实例覆盖
- 调整布局和颜色
- 添加注释

#### 安装

```bash
# 克隆仓库
git clone https://github.com/grab/cursor-talk-to-figma-mcp.git

# 安装依赖
cd cursor-talk-to-figma-mcp
npm install

# 构建
npm run build
```

在 Cursor MCP 设置中添加：

```json
{
  "mcpServers": {
    "cursor-talk-to-figma": {
      "command": "node",
      "args": ["<path>/cursor-talk-to-figma-mcp/build/index.js"]
    }
  }
}
```

> 注意：还需在 Figma 中安装配套插件 "Cursor Talk To Figma"。

#### 适用场景

- 需要从 Cursor 中直接修改 Figma 设计
- 批量操作设计元素
- 实时同步代码变更到 Figma

---

### 方案三：figma-automation（已有）

**来源**：antigravity-awesome-skills（项目中已下载）
**位置**：`skills/antigravity-awesome-skills/skills/figma-automation/`

#### 功能

通过 Rube MCP（Composio）自动化 Figma 任务：
- 文件管理
- 组件操作
- 设计令牌管理
- 评论管理
- 导出操作

#### 使用

已包含在 antigravity-awesome-skills 中，安装该 Skill 后即可使用。

---

### 方案四：vm0-ai/figma（Agent Skill）

**来源**：VM0-AI
**GitHub**：[vm0-ai/vm0-skills](https://github.com/vm0-ai/vm0-skills)

#### 功能

基于 Figma REST API 的技能：
- 读取设计文件内容
- 导出图片
- 管理评论（可读写）
- 集成 Figma 工作区

> 注意：对设计文件本身为只读，评论、版本等为可读写。

#### 安装

```bash
# 方式一：手动复制
git clone --depth 1 https://github.com/vm0-ai/vm0-skills.git /tmp/vm0-skills
mkdir -p ~/.cursor/skills/figma
cp /tmp/vm0-skills/figma/SKILL.md ~/.cursor/skills/figma/
rm -rf /tmp/vm0-skills

# 方式二：Claude Code Marketplace（如可用）
/plugin marketplace add vm0-ai/vm0-skills
/plugin install figma@vm0-skills
```

---

## 三、最佳实践推荐

### 推荐组合：Figma 官方 MCP + ui-ux-pro-max Skill

| 工具 | 职责 |
|------|------|
| **Figma 官方 MCP Server** | 从 Figma 读取设计数据，提供真实的设计上下文 |
| **ui-ux-pro-max Skill** | 智能推荐配色/字体/风格，生成高质量代码，Pre-delivery 检查 |

**工作流**：

```
1. 设计师在 Figma 中完成设计
2. 开发者在 Cursor 中粘贴 Figma 链接
3. Figma MCP 提取设计数据（颜色、字体、布局、组件）
4. ui-ux-pro-max 验证设计决策并补充最佳实践
5. Cursor Agent 生成符合设计稿的像素级代码
6. Pre-delivery 检查确保无障碍、性能、响应式等标准
```

### 不同场景的推荐方案

| 场景 | 推荐方案 |
|------|----------|
| **设计稿 → 代码**（最常见） | Figma 官方 MCP Server |
| **AI 直接设计 UI** | cursor-talk-to-figma-mcp |
| **批量修改设计** | cursor-talk-to-figma-mcp |
| **自动化设计工作流** | figma-automation（已有） |
| **设计审查与优化** | ui-ux-pro-max Skill |

---

## 四、相关资源

| 资源 | 地址 |
|------|------|
| Figma MCP Server 官方文档 | [developers.figma.com/docs/figma-mcp-server](https://developers.figma.com/docs/figma-mcp-server/) |
| Figma MCP 使用指南 | [help.figma.com/hc/en-us/articles/32132100833559](https://help.figma.com/hc/en-us/articles/32132100833559) |
| Figma to Code with Cursor MCP | [cursorideguide.com/use-cases/figma-to-cursor-with-mcp](https://cursorideguide.com/use-cases/figma-to-cursor-with-mcp) |
| Design in Figma using Cursor Agent | [completeaitraining.com/ai-tools/design-in-figma-using-cursor-agent-mcp](https://completeaitraining.com/ai-tools/design-in-figma-using-cursor-agent-mcp/) |
| cursor-talk-to-figma-mcp | [github.com/grab/cursor-talk-to-figma-mcp](https://github.com/grab/cursor-talk-to-figma-mcp) |
| vm0-ai/figma 技能 | [github.com/vm0-ai/vm0-skills/tree/main/figma](https://github.com/vm0-ai/vm0-skills/tree/main/figma) |

---

*整理时间：2026-02-06*
