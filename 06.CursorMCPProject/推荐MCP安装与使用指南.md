# 推荐 MCP 服务安装与使用指南

> 基于各平台使用率排行，推荐新增安装的高价值 MCP 服务。
>
> 最后更新：2026-02-26

---

## 目录

1. [Sequential Thinking — AI 推理增强](#1-sequential-thinking--ai-推理增强)（强烈推荐）
2. [Memory — 持久化记忆](#2-memory--持久化记忆)（强烈推荐）
3. [Fetch — 网页内容获取](#3-fetch--网页内容获取)（强烈推荐）
4. [Filesystem — 文件系统操作](#4-filesystem--文件系统操作)（强烈推荐）
5. [Exa Search — AI 智能搜索](#5-exa-search--ai-智能搜索)（强烈推荐）
6. [GitHub MCP — GitHub 集成](#6-github-mcp--github-集成)（按需推荐）
7. [Notion — 知识管理](#7-notion--知识管理)（按需推荐）

---

## 1. Sequential Thinking — AI 推理增强

| 项目 | 说明 |
|------|------|
| **来源** | Anthropic 官方 MCP Reference Server |
| **npm** | [@modelcontextprotocol/server-sequential-thinking](https://www.npmjs.com/package/@modelcontextprotocol/server-sequential-thinking) |
| **功能** | 通过结构化的思考序列提升 AI 解决复杂问题的能力 |

### 安装配置

```json
"sequential-thinking": {
  "command": "npx",
  "args": ["-y", "@modelcontextprotocol/server-sequential-thinking"]
}
```

### 主要工具（1 个）

| 工具 | 说明 |
|------|------|
| `sequential_thinking` | 动态结构化思考：分步推理、修正、分支探索、假设验证 |

### 工具参数

| 参数 | 类型 | 说明 |
|------|------|------|
| `thought` | string | 当前思考步骤的内容 |
| `nextThoughtNeeded` | boolean | 是否还需要下一步思考 |
| `thoughtNumber` | number | 当前是第几步思考 |
| `totalThoughts` | number | 预计总思考步数（可动态调整） |
| `isRevision` | boolean | 是否是对前面步骤的修正 |
| `revisesThought` | number | 修正的是哪一步 |
| `branchFromThought` | number | 从哪一步分支探索 |
| `branchId` | string | 分支标识 |
| `needsMoreThoughts` | boolean | 是否需要追加更多思考步骤 |

### 适用场景

```
帮我设计一个分布式缓存系统的架构方案
分析这段代码的性能瓶颈并给出优化方案
帮我规划一个从单体应用迁移到微服务的方案
```

---

## 2. Memory — 持久化记忆

| 项目 | 说明 |
|------|------|
| **来源** | Anthropic 官方 MCP Reference Server |
| **npm** | [@modelcontextprotocol/server-memory](https://www.npmjs.com/package/@modelcontextprotocol/server-memory) |
| **功能** | 基于知识图谱的持久化记忆系统，让 AI 跨会话记住信息 |

### 安装配置

```json
"memory": {
  "command": "npx",
  "args": ["-y", "@modelcontextprotocol/server-memory"]
}
```

### 主要工具

| 工具 | 说明 |
|------|------|
| `create_entities` | 创建新的实体（人、项目、概念等） |
| `create_relations` | 创建实体之间的关系 |
| `add_observations` | 为已有实体添加观察/信息 |
| `delete_entities` | 删除实体 |
| `read_graph` | 读取整个知识图谱 |
| `search_nodes` | 搜索实体 |
| `open_nodes` | 打开特定实体查看详情 |

### 使用示例

```
记住：我的项目使用 React 19 + TypeScript + Tailwind CSS v4
记住：张三是前端负责人，李四负责后端
回忆一下我的项目技术栈是什么？
```

---

## 3. Fetch — 网页内容获取

| 项目 | 说明 |
|------|------|
| **来源** | Anthropic 官方 MCP Reference Server |
| **PyPI** | [mcp-server-fetch](https://pypi.org/project/mcp-server-fetch/) |
| **功能** | 获取网页内容并转换为 Markdown 格式 |

### 安装配置

```json
"fetch": {
  "command": "uvx",
  "args": ["mcp-server-fetch"]
}
```

### 主要工具（1 个）

| 工具 | 说明 |
|------|------|
| `fetch` | 获取 URL 内容，自动将 HTML 转换为 Markdown |

### 与 Playwright 的区别

| 对比 | Fetch | Playwright |
|------|-------|------------|
| 速度 | 快（直接 HTTP） | 慢（启动浏览器） |
| 功能 | 只读取内容 | 可交互 |
| JS 渲染 | 不支持 | 支持 |
| 适用场景 | 静态页面/文档 | 交互/动态页面 |

---

## 4. Filesystem — 文件系统操作

| 项目 | 说明 |
|------|------|
| **来源** | Anthropic 官方 MCP Reference Server |
| **npm** | [@modelcontextprotocol/server-filesystem](https://www.npmjs.com/package/@modelcontextprotocol/server-filesystem) |
| **功能** | 安全的文件系统读写操作，限制在指定目录内 |

### 安装配置

```json
"filesystem": {
  "command": "npx",
  "args": ["-y", "@modelcontextprotocol/server-filesystem", "/home/tsdl/SSD"]
}
```

### 主要工具（11 个）

| 工具 | 说明 |
|------|------|
| `read_file` | 读取文件完整内容 |
| `read_multiple_files` | 批量读取多个文件 |
| `write_file` | 创建或覆盖写入文件 |
| `edit_file` | 使用 diff 方式编辑文件 |
| `create_directory` | 创建目录 |
| `list_directory` | 列出目录内容 |
| `directory_tree` | 获取目录树结构 |
| `move_file` | 移动/重命名文件 |
| `search_files` | 搜索文件 |
| `get_file_info` | 获取文件元信息 |
| `list_allowed_directories` | 列出允许操作的目录 |

---

## 5. Exa Search — AI 智能搜索

| 项目 | 说明 |
|------|------|
| **官网** | [exa.ai](https://exa.ai/) |
| **npm** | [@exa/mcp-server](https://www.npmjs.com/package/@exa/mcp-server) |
| **功能** | AI 驱动的智能网页搜索 |
| **使用量** | Smithery 平台 1066 万次使用（排名第一） |

### 安装配置

```json
"exa": {
  "command": "npx",
  "args": ["-y", "@exa/mcp-server"],
  "env": {
    "EXA_API_KEY": "你的EXA_API_KEY"
  }
}
```

### 主要工具（3 个）

| 工具 | 说明 |
|------|------|
| `web_search` | 智能网页搜索 |
| `research` | 深度研究 |
| `get_page_contents` | 获取页面内容 |

---

## 6. GitHub MCP — GitHub 集成

| 项目 | 说明 |
|------|------|
| **npm** | [@modelcontextprotocol/server-github](https://www.npmjs.com/package/@modelcontextprotocol/server-github) |
| **功能** | 通过 AI 操作 GitHub：仓库管理、Issue、PR、代码搜索 |

### 安装配置

```json
"github": {
  "command": "npx",
  "args": ["-y", "@modelcontextprotocol/server-github"],
  "env": {
    "GITHUB_PERSONAL_ACCESS_TOKEN": "ghp_xxxxxxxxxx"
  }
}
```

### 前置条件

- GitHub Personal Access Token（repo, read:org 权限）

---

## 7. Notion — 知识管理

| 项目 | 说明 |
|------|------|
| **npm** | [@notionhq/notion-mcp-server](https://www.npmjs.com/package/@notionhq/notion-mcp-server) |
| **功能** | 通过 AI 操作 Notion：搜索、创建、更新页面和数据库 |

### 安装配置

```json
"notion": {
  "command": "npx",
  "args": ["-y", "@notionhq/notion-mcp-server"],
  "env": {
    "OPENAPI_MCP_HEADERS": "{\"Authorization\":\"Bearer ntn_xxxxxxxxxx\",\"Notion-Version\":\"2022-06-28\"}"
  }
}
```

### 前置条件

1. [notion.so/my-integrations](https://www.notion.so/my-integrations) 创建 Integration
2. 复制 Internal Integration Secret
3. 在 Notion 页面中邀请该 Integration

---

## 快速安装汇总

所有推荐服务的 `mcp.json` 配置片段：

```json
{
  "sequential-thinking": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-sequential-thinking"]
  },
  "memory": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-memory"]
  },
  "fetch": {
    "command": "uvx",
    "args": ["mcp-server-fetch"]
  },
  "filesystem": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-filesystem", "/home/tsdl/SSD"]
  },
  "exa": {
    "command": "npx",
    "args": ["-y", "@exa/mcp-server"],
    "env": {
      "EXA_API_KEY": "你的KEY"
    }
  },
  "github": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-github"],
    "env": {
      "GITHUB_PERSONAL_ACCESS_TOKEN": "ghp_xxx"
    }
  },
  "notion": {
    "command": "npx",
    "args": ["-y", "@notionhq/notion-mcp-server"],
    "env": {
      "OPENAPI_MCP_HEADERS": "{\"Authorization\":\"Bearer ntn_xxx\",\"Notion-Version\":\"2022-06-28\"}"
    }
  }
}
```

> 提醒：如果 npx 方式遇到红色点，参考之前的解决方案——全局安装 + NVM node 完整路径。