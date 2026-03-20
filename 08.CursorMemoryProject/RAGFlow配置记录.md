# RAGFlow 配置记录

**日期**：2026-03-09
**目标**：http://localhost:80（RAGFlow v0.24.0）

---

## 最终配置状态

| 组件 | 值 | 状态 |
|------|-----|------|
| **Chat 模型** | qwen2.5:7b（OpenAI-API-Compatible） | ✅ |
| **Embedding 模型** | bge-m3（Ollama） | ✅ |
| **默认 LLM** | qwen2.5:7b | ✅ |
| **默认 Embedding** | bge-m3 | ✅ |
| **知识库** | CursorProject, Zoom, Teams, MDEP | ✅ |
| **助手** | CursorProject助手, Zoom助手, Teams助手, MDEP助手 | ✅ |
| **知识库关联** | 全部已关联 | ✅ |

---

## 配置详情

### 模型提供商

#### Ollama（嵌入模型）

| 项目 | 值 |
|------|-----|
| 提供商类型 | Ollama |
| Base URL | `http://host.docker.internal:11434` |
| 嵌入模型 | bge-m3 |
| 最大 token | 512 |
| 连接验证 | ✅ 成功 |

#### OpenAI-API-Compatible（对话模型）

| 项目 | 值 |
|------|-----|
| 提供商类型 | OpenAI-API-Compatible |
| Base URL | `http://host.docker.internal:11434/v1` |
| API Key | ollama |
| 对话模型 | qwen2.5:7b |
| 连接验证 | ⚠️ 验证失败但已保存可用 |

> **说明**：RAGFlow v0.24.0 对 Ollama Chat 模型的验证存在已知问题（[#5841](https://github.com/infiniflow/ragflow/issues/5841)），通过 OpenAI-API-Compatible 方式绕过。实际 API 调用正常。

### 知识库

| 项目 | 值 |
|------|-----|
| 名称 | CursorProject |
| 嵌入模型 | bge-m3 (Ollama) |
| 分块方法 | General |
| 创建时间 | 2026-03-09 |
| URL | `http://localhost/dataset/dataset/1d6a97261b9811f1b9ca8bdffa79853f` |

#### Zoom（2026-03-09 新增）

| 项目 | 值 |
|------|-----|
| 名称 | Zoom |
| 嵌入模型 | bge-m3 (Ollama) |
| 分块方法 | General |
| 创建时间 | 2026-03-09 |
| 文件数 | 15 个（1 个 .ods 不支持） |
| URL | `http://localhost/dataset/dataset/ccd53ce21ba311f1b9ca8bdffa79853f` |

### 助手（2026-03-09 更新）

| 助手名称 | 知识库 | LLM | 状态 |
|----------|--------|-----|------|
| CursorProject助手 | CursorProject | qwen2.5:7b | ✅ 已关联 |
| Zoom助手 | Zoom | qwen2.5:7b | ✅ 已关联 |
| Teams助手 | Teams | qwen2.5:7b | ✅ 已关联 |
| MDEP助手 | MDEP | qwen2.5:7b | ✅ 已关联 |

---

## 账号信息

| 项目 | 值 |
|------|-----|
| 邮箱 | admin@localhost.com |
| 密码 | Admin@123456 |

---

## Ollama 配置

### 已安装模型

| 模型 | 大小 | 用途 |
|------|------|------|
| bge-m3 | 1.2 GB | 嵌入（1024维，100+语言） |
| qwen2.5:7b | 4.7 GB | 对话（中文最佳） |

### 监听配置

Ollama 默认只监听 `127.0.0.1`，Docker 容器无法访问。已通过 systemd override 修改为监听所有接口：

```bash
# /etc/systemd/system/ollama.service.d/override.conf
[Service]
Environment="OLLAMA_HOST=0.0.0.0:11434"
```

```bash
# 应用配置
sudo systemctl daemon-reload
sudo systemctl restart ollama

# 验证
ss -tlnp | grep 11434
# 应显示 *:11434（而非 127.0.0.1:11434）
```

---

## Docker 容器

| 容器 | 端口 | 说明 |
|------|------|------|
| docker-ragflow-cpu-1 | 80, 443, 9380-9382 | RAGFlow 主服务 |
| docker-es01-1 | 1200 | Elasticsearch 全文检索 |
| docker-mysql-1 | 5455 | MySQL 元数据存储 |
| docker-minio-1 | 9000, 9001 | MinIO 对象存储 |
| docker-redis-1 | 6379 | Redis 缓存 |

### 管理命令

```bash
# 启动
cd /home/tsdl/SSD/ragflow/docker && docker compose up -d

# 停止
cd /home/tsdl/SSD/ragflow/docker && docker compose down

# 查看日志
docker logs docker-ragflow-cpu-1 --tail 50

# 查看状态
docker ps --format "table {{.Names}}\t{{.Status}}"
```

---

## 配置过程中遇到的问题

### 问题 1：Ollama 连接失败

**现象**：RAGFlow 容器内无法访问 `host.docker.internal:11434`

**原因**：Ollama 默认只监听 `127.0.0.1:11434`

**解决**：创建 systemd override 文件设置 `OLLAMA_HOST=0.0.0.0:11434`

### 问题 2：Chat 模型验证失败

**现象**：通过 Ollama 提供商添加 qwen2.5:7b 时，验证报错 "Fail to access model"

**原因**：RAGFlow v0.24.0 的 Ollama Chat 模型验证逻辑存在 bug（[#5841](https://github.com/infiniflow/ragflow/issues/5841)）

**解决**：改用 OpenAI-API-Compatible 提供商，Base URL 设为 `http://host.docker.internal:11434/v1`

### 问题 3：Docker Hub 拉取失败

**现象**：`connection reset by peer`

**解决**：配置国内 Docker 镜像源（`/etc/docker/daemon.json`）

---

## 待完成事项

- [x] ~~在助手设置中手动关联 CursorProject 知识库~~（已完成，4 个助手均已关联）
- [ ] 上传项目需求文档到知识库
- [ ] 上传 Android 源码文件
- [ ] 测试 RAG 问答效果

---

## 1M 上下文时代的 RAG 策略优化（2026-03-15）

> 参考：[Claude 1M Context GA](https://claude.com/blog/1m-context-ga)

Claude Opus 4.6 / Sonnet 4.6 的 1M 上下文窗口正式 GA 后，RAG 的使用策略需要相应调整。

### 何时仍需要 RAG

| 场景 | 是否需要 RAG | 原因 |
|------|-------------|------|
| 持续更新的外部知识（MDEP/Zoom/Teams 文档） | **需要** | 文档频繁更新，不适合手动加载 |
| 超大文档集（> 2000 页） | **需要** | 超出 1M 上下文容量 |
| 多用户共享知识库 | **需要** | RAGFlow 提供统一检索入口 |
| 精确引用溯源 | **需要** | RAG 可以返回具体文档和段落来源 |

### 何时可以直接使用上下文

| 场景 | 可直接加载 | 原因 |
|------|-----------|------|
| 项目内部代码（< 66K 行） | **可以** | 1M token ≈ 66K 行代码 |
| 单个文档分析（< 600 页 PDF） | **可以** | 新限制支持 600 页 |
| 当前会话的调试上下文 | **可以** | 减少 compaction，保持完整 trace |
| 小型知识库（< 500 页文档） | **可以** | 直接加载比 RAG 检索更完整 |

### 混合策略建议

```
小型/临时文档 → 直接 @file 加载到上下文
大型/持久知识库 → RAGFlow RAG 检索
跨会话记忆 → Memory MCP
实时信息 → Web Search / Exa MCP
```

### 对现有知识库的影响

| 知识库 | 文档量 | 建议 |
|--------|--------|------|
| CursorProject | 少量 | 可直接加载，RAG 作为备选 |
| MDEP | 15 个文档 | 小文档直接加载，大文档走 RAG |
| Zoom | 15 个文档 | 保持 RAG，文档持续更新 |
| Teams | 66 个文档 | 保持 RAG，文档量较大 |

### Embedding 资源优化

1M 上下文减少了对 RAG 的依赖，可以降低 Embedding 计算压力：
- 优先解析高频查询的文档
- 低频文档可延迟解析
- CPU 环境下减少并发 Embedding 任务，避免影响 Chat 推理
