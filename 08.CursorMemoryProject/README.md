# Cursor AI 记忆与知识库方案

> 跨设备持久化 AI 记忆解决方案——基于 NAS + Memory MCP + Qdrant 构建个人/团队 AI 知识库。
>
> 最后更新：2026-03-05

---

## 目标

让 Cursor AI 拥有**持久化记忆**，跨多台电脑保持一致的上下文认知：
- 记住用户偏好、项目技术栈、编码规范
- 记住历史决策及原因
- 支持语义搜索，快速检索相关知识
- 所有设备自动同步，无需手动传递

---

## 架构总览

```
┌────────────────────────────────────────────────────────┐
│                     NAS / 共享存储                       │
│                                                        │
│  ┌─────────────────┐    ┌──────────────────────────┐   │
│  │  memory.jsonl   │    │  Qdrant (Docker)         │   │
│  │  (文件级记忆)     │    │  (向量语义搜索)            │   │
│  └────────┬────────┘    └────────────┬─────────────┘   │
│           │                          │                  │
│  ┌────────┴────────┐    ┌────────────┴─────────────┐   │
│  │   Syncthing     │    │   HTTP API :6333         │   │
│  │  (P2P 文件同步)  │    │   (局域网/VPN 访问)       │   │
│  └────────┬────────┘    └────────────┬─────────────┘   │
└───────────┼──────────────────────────┼─────────────────┘
            │                          │
     ┌──────┴──────┐           ┌───────┴───────┐
     │  电脑 A      │           │  电脑 B        │
     │  Memory MCP  │           │  Memory MCP   │
     │  Qdrant MCP  │           │  Qdrant MCP   │
     │  Cursor IDE  │           │  Cursor IDE   │
     └─────────────┘           └───────────────┘
```

---

## 方案一：Memory MCP + 文件同步（基础方案）

适合场景：个人使用，记忆量不大（< 1 万条），不需要语义搜索。

### 原理

Memory MCP 将记忆存储在本地 `memory.jsonl` 文件中，通过文件同步工具在多台电脑间共享。

### 第一步：配置 Memory MCP 存储路径

编辑 `~/.cursor/mcp.json`：

```json
"memory": {
  "command": "npx",
  "args": ["-y", "@modelcontextprotocol/server-memory"],
  "env": {
    "MEMORY_FILE_PATH": "/path/to/shared/cursor-memory.jsonl"
  }
}
```

### 第二步：选择同步方式

#### 方式 A：NAS 直接挂载（最简单）

将 NAS 的共享目录挂载到本地，所有电脑指向同一路径：

```bash
# Linux（SMB 挂载）
sudo mount -t cifs //NAS_IP/CursorMemory /mnt/cursor-memory \
  -o username=YOUR_USER,password=YOUR_PASS,uid=$(id -u),gid=$(id -g)

# 开机自动挂载 (/etc/fstab)
//NAS_IP/CursorMemory /mnt/cursor-memory cifs credentials=/etc/nas-creds,uid=1000,gid=1000 0 0
```

然后配置 Memory MCP：
```json
"MEMORY_FILE_PATH": "/mnt/cursor-memory/memory.jsonl"
```

#### 方式 B：Syncthing P2P 同步（无 NAS 也可用）

Syncthing 是去中心化的文件同步工具，不依赖中心服务器：

```bash
# 安装 Syncthing
sudo apt install syncthing

# 启动（后台运行）
syncthing serve --no-browser &

# 访问 Web UI 配置同步目录
# http://localhost:8384
```

在每台电脑上：
1. 安装 Syncthing
2. 添加同步目录：`/home/USER/CursorMemory/`
3. 互相添加设备 ID
4. Memory MCP 指向该目录

#### 方式 C：rsync 定时同步（适合 NAS + cron）

```bash
# 每 5 分钟同步到 NAS
*/5 * * * * rsync -az /home/tsdl/HDD/CursorMemory/ NAS_IP:/volume1/CursorMemory/

# 从 NAS 同步回来
*/5 * * * * rsync -az NAS_IP:/volume1/CursorMemory/ /home/tsdl/HDD/CursorMemory/
```

### 注意事项

- **并发写入冲突**：如果两台电脑同时写入 `memory.jsonl`，可能产生冲突。建议同一时间只在一台电脑上使用 Memory MCP。
- **NAS 离线时**：Memory MCP 会在本地缓存，NAS 恢复后自动同步。
- **文件大小**：1 万条记忆约 5-10MB，同步压力很小。

---

## 方案二：Qdrant 向量数据库（进阶方案）

适合场景：需要语义搜索、大量知识存储、团队共享。

### 原理

Qdrant 是开源向量数据库，部署在 NAS 上作为中央知识库。所有电脑通过 Qdrant MCP 连接到同一个数据库实例。

### 第一步：在 NAS 上部署 Qdrant

#### Docker 部署（推荐）

```bash
# 在 NAS 上运行 Qdrant
docker run -d \
  --name qdrant \
  --restart always \
  -p 6333:6333 \
  -v /volume1/qdrant_storage:/qdrant/storage \
  qdrant/qdrant

# 验证
curl http://NAS_IP:6333/collections
```

#### Docker Compose

```yaml
version: '3.8'
services:
  qdrant:
    image: qdrant/qdrant:latest
    container_name: qdrant
    restart: always
    ports:
      - "6333:6333"
      - "6334:6334"
    volumes:
      - /volume1/qdrant_storage:/qdrant/storage
    environment:
      - QDRANT__STORAGE__STORAGE_PATH=/qdrant/storage
```

### 第二步：配置 Qdrant MCP

在每台电脑的 `~/.cursor/mcp.json` 中添加：

```json
"qdrant": {
  "command": "uvx",
  "args": ["mcp-server-qdrant"],
  "env": {
    "QDRANT_URL": "http://NAS_IP:6333",
    "COLLECTION_NAME": "cursor-knowledge",
    "EMBEDDING_MODEL": "sentence-transformers/all-MiniLM-L6-v2"
  }
}
```

### 第三步：使用方式

```
> 将这个 API 设计方案存入知识库
> 搜索知识库中关于 "数据库分表" 的方案
> 存储：我们决定使用 PostgreSQL + TimescaleDB，原因是...
```

### Qdrant 工具

| 工具 | 说明 |
|------|------|
| `qdrant-store` | 存储信息（自动向量化 + 可选元数据） |
| `qdrant-find` | 语义搜索（根据含义匹配，不是关键词） |

### 优势

- **语义搜索**：不是关键词匹配，而是理解含义
- **大规模存储**：百万级向量记录
- **多用户**：团队成员共享同一知识库
- **数据安全**：完全私有化，数据在你的 NAS 上

---

## 方案三：双层架构（推荐的最终方案）

结合 Memory MCP（轻量快速）+ Qdrant（深度搜索），获得最佳体验：

```json
{
  "memory": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-memory"],
    "env": {
      "MEMORY_FILE_PATH": "/mnt/nas/CursorMemory/memory.jsonl"
    }
  },
  "qdrant": {
    "command": "uvx",
    "args": ["mcp-server-qdrant"],
    "env": {
      "QDRANT_URL": "http://NAS_IP:6333",
      "COLLECTION_NAME": "cursor-knowledge"
    }
  }
}
```

| 层级 | 工具 | 存储内容 | 使用频率 |
|------|------|----------|----------|
| **快速记忆** | Memory MCP | 偏好、习惯、常用配置 | 每次对话 |
| **深度知识** | Qdrant MCP | 技术方案、设计文档、历史决策 | 按需搜索 |

---

## NAS 购买建议

### 入门级（个人使用）

| 型号 | 价格 | CPU | 内存 | 盘位 | Docker |
|------|------|-----|------|------|--------|
| 群晖 DS224+ | ¥3,000 | Intel J4125 | 2GB | 2 | 支持 |
| 极空间 Z4S | ¥2,500 | Intel N5105 | 8GB | 4 | 支持 |
| 绿联 DXP2800 | ¥1,500 | Realtek RTD1619B | 2GB | 2 | 支持 |

### 性能要求

- **Memory MCP 文件同步**：任何 NAS 都够用（文件极小）
- **Qdrant Docker**：建议 4GB+ 内存，Intel CPU（ARM 也可以但性能较低）
- **网络**：千兆局域网即可，延迟 < 10ms

---

## 实施路线图

### 阶段一：现在（已完成）
- [x] Memory MCP 安装并配置本地存储路径
- [x] auto-memory.mdc 全局规则（自动读写记忆）
- [x] 存储目录：`/home/tsdl/HDD/CursorMemory/`

### 阶段二：购买 NAS 后
- [ ] NAS 初始化，创建共享目录
- [ ] 配置 SMB/NFS 挂载到所有电脑
- [ ] Memory MCP 存储路径改为 NAS 挂载目录
- [ ] 安装 Syncthing 作为备选同步方案

### 阶段三：进阶（可选）
- [ ] NAS 上 Docker 部署 Qdrant
- [ ] 配置 Qdrant MCP 连接
- [ ] 历史记忆迁移到 Qdrant
- [ ] 团队知识库共享

---

## 相关配置文件

| 文件 | 说明 |
|------|------|
| `~/.cursor/mcp.json` | MCP 服务配置（Memory、Qdrant） |
| `~/.cursor/rules/auto-memory.mdc` | 自动记忆管理规则 |
| `$MEMORY_FILE_PATH` | Memory MCP 数据文件 |

---

## 参考资源

| 资源 | 链接 |
|------|------|
| Memory MCP | [npm](https://www.npmjs.com/package/@modelcontextprotocol/server-memory) |
| Qdrant MCP | [GitHub](https://github.com/qdrant/mcp-server-qdrant) |
| Qdrant 文档 | [qdrant.tech/documentation](https://qdrant.tech/documentation/) |
| Syncthing | [syncthing.net](https://syncthing.net/) |
| Mem0（云端替代） | [mem0.ai](https://mem0.ai/) |
