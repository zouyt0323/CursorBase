#!/bin/bash
# CursorBase 每周整理与更新脚本
# 建议通过 cron 每周执行：0 9 * * 1 (每周一 9:00)
# 或 systemd timer / 其他调度器

set -e
BASE="/home/tsdl/SSD/CursorProject/CursorBase"
LOG="$BASE/scripts/weekly-update.log"

log() { echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*" | tee -a "$LOG"; }

log "========== 每周整理更新开始 =========="

# 1. 从 GitHub 更新子仓库
log "1. 更新 Git 子仓库..."
for repo in \
  "02.CursorRuleProject/02-第三方规则/awesome-cursorrules" \
  "04.CursorSkillProject/03-第三方技能/everything-claude-code" \
  "04.CursorSkillProject/03-第三方技能/antigravity-awesome-skills" \
  "04.CursorSkillProject/03-第三方技能/vm0-skills" \
  "04.CursorSkillProject/03-第三方技能/ui-ux-pro-max" \
  "04.CursorSkillProject/03-第三方技能/anthropics-skills" \
  "06.CursorMCPProject/android-mcp"
do
  dir="$BASE/$repo"
  if [ -d "$dir/.git" ]; then
    (cd "$dir" && git pull --rebase 2>&1) | tee -a "$LOG" || log "警告: $repo 更新失败"
  else
    log "跳过(非git): $repo"
  fi
done

# 2. 重新生成 Skills 索引文档
log "2. 重新生成 Skills 索引文档..."
cd "$BASE"
PYTHON="python3"
[ -d "04.CursorSkillProject/.venv" ] && . 04.CursorSkillProject/.venv/bin/activate && PYTHON="python" 2>/dev/null || true
for script in 04.CursorSkillProject/scripts/gen-skills-doc/gen_skills_doc.py 04.CursorSkillProject/scripts/gen-skills-doc/gen_anthropic_skills_doc.py 04.CursorSkillProject/scripts/gen-skills-doc/gen_uiux_doc.py 04.CursorSkillProject/scripts/gen-skills-doc/gen_vm0_skills_doc.py; do
  [ -f "$script" ] && $PYTHON "$script" 2>&1 | tee -a "$LOG" || true
done

# 3. 创建日期备份（Rules + Skills）
log "3. 创建日期备份..."
BACKUP_DIR="$BASE/04.CursorSkillProject/04-备份/installed-$(date +%Y%m%d-%H%M%S)"
mkdir -p "$BACKUP_DIR"
cp -r "$BASE/.cursor/rules" "$BACKUP_DIR/" 2>/dev/null || true
cp -r "$HOME/.cursor/skills" "$BACKUP_DIR/" 2>/dev/null || true
cp -r "$HOME/.cursor/skills-cursor" "$BACKUP_DIR/" 2>/dev/null || true
log "备份已保存至: $BACKUP_DIR"

# 4. 更新 npm 全局包（chrome-devtools-mcp 等）
log "4. 检查 npm 全局 MCP 包..."
npm update -g chrome-devtools-mcp 2>/dev/null || log "chrome-devtools-mcp 未全局安装，跳过"

log "========== 每周整理更新完成 =========="
