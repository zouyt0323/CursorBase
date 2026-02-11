# Cursor Rules 整理目录

本目录包含 **Cursor Rules Top 50** 的分类索引、各分类规则列表，以及从 [awesome-cursorrules](https://github.com/PatrickJS/awesome-cursorrules) 拉取的示例规则正文，便于本地查阅与复用。

## 目录结构

| 文件 | 说明 |
|------|------|
| `00-Top50-索引.md` | Top 50 完整清单与收集网站列表（与项目根目录清单一致） |
| `01-meta-best-practices.md` | 元规则与最佳实践（5 条） |
| `02-frontend-frameworks.md` | 前端框架与 UI（10 条） |
| `03-typescript-state.md` | TypeScript/JS 与状态管理（7 条） |
| `04-backend-languages.md` | 后端语言（9 条） |
| `05-backend-frameworks-api.md` | 后端框架与 API（6 条） |
| `06-quality-testing-security.md` | 质量、测试与安全（8 条） |
| `07-devops-infrastructure.md` | DevOps 与基础设施（3 条） |
| `08-data-ai-ml.md` | 数据与 AI/ML（2 条） |
| `examples/` | 示例规则正文（可直接复制到 `.cursor/rules/` 或项目根 `.cursorrules`） |

## 如何使用

1. **按分类选规则**：打开 `01-` ～ `08-` 中对应场景的 md，查看包名与说明。
2. **安装 PRPM 规则**（需先安装 [prpm](https://prpm.dev)）：
   ```bash
   npm install -g prpm
   prpm install @lst97/react-pro
   prpm install @sanjeed5/django
   ```
3. **使用示例规则**：将 `examples/` 下 `.md` 内容复制到项目的 `.cursor/rules/` 中作为 Cursor 规则使用。
4. **从 awesome-cursorrules 获取更多**：<https://github.com/PatrickJS/awesome-cursorrules/tree/main/rules> 中每个子目录下的 `.cursorrules` 可直接复制使用。
5. **使用已下载的 awesome-cursorrules**：项目内已下载仓库 `../awesome-cursorrules/`，其中 **`awesome-cursorrules/规则清单-使用场景与安装方法.md`** 包含每一条规则的使用场景与安装方法；可直接从 `awesome-cursorrules/rules/<子目录>/` 复制 `.cursorrules` 到项目根或 `.cursor/rules/`。

## 收集网站速查

- **CursorList**: https://cursorlist.com/
- **extmc.com**: https://extmc.com/
- **awesome-cursorrules**: https://github.com/PatrickJS/awesome-cursorrules
- **Pro Cursor Rules**: https://www.procursorrules.com/
- **Cursor Directory**: https://cursor.directory/rules/popular
- **PRPM**: https://prpm.dev/
- **官方文档**: https://cursor.com/docs/context/rules
