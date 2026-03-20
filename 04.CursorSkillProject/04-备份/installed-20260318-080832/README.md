# Cursor 已安装 Rules 与 Skills 备份

**备份时间：** 2026-03-18 08:08:32  
**备份内容：** 当前 Cursor 中已安装的 Rules 和 Skills 完整副本

## 目录结构

| 目录/文件 | 说明 |
|-----------|------|
| `rules/` | 工程级 Rules（来自 CursorBase/.cursor/rules/） |
| `skills/` | 用户级 Skills（来自 ~/.cursor/skills/） |
| `skills-cursor/` | Cursor 专属 Skills（来自 ~/.cursor/skills-cursor/） |
| `规则列表-20260318.md` | Rules 分类清单（28 个） |
| `技能列表-20260318.md` | Skills 分类清单（186 个） |
| `MCP列表-20260318.md` | MCP 清单（20 个，含新增 chrome-devtools） |

## 恢复方式

```bash
# 恢复 Rules 到工程
cp -r rules/* /path/to/CursorBase/.cursor/rules/

# 恢复 Skills 到用户目录
cp -r skills/* ~/.cursor/skills/
cp -r skills-cursor/* ~/.cursor/skills-cursor/
```
