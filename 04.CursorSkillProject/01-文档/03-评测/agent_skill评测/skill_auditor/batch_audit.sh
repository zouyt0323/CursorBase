#!/bin/bash
# 批量评测所有 Skill
# 用法: ./batch_audit.sh [skills_root_dir] [output_dir]

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
AUDITOR="$SCRIPT_DIR/skill_auditor.py"

SKILLS_ROOT="${1:-$HOME/.cursor/skills}"
OUTPUT_DIR="${2:-$SCRIPT_DIR/reports}"

mkdir -p "$OUTPUT_DIR"

echo "=========================================="
echo "  Skill 批量评测"
echo "  搜索目录: $SKILLS_ROOT"
echo "  报告输出: $OUTPUT_DIR"
echo "=========================================="
echo ""

TOTAL=0
PASS=0
FAIL=0

while IFS= read -r skill_md; do
    skill_dir=$(dirname "$skill_md")
    skill_name=$(basename "$skill_dir")
    report_file="$OUTPUT_DIR/${skill_name}_report.md"

    echo "评测: $skill_name"
    python3 "$AUDITOR" "$skill_dir" -o "$report_file" -q 2>/dev/null

    score=$(python3 "$AUDITOR" "$skill_dir" --json -q 2>/dev/null | python3 -c "import json,sys; print(json.load(sys.stdin)['total_weighted'])" 2>/dev/null)

    if [ -n "$score" ]; then
        TOTAL=$((TOTAL + 1))
        result=$(echo "$score >= 60" | bc -l 2>/dev/null || python3 -c "print('1' if $score >= 60 else '0')")
        if [ "$result" = "1" ]; then
            echo "  → $score/100 ✅"
            PASS=$((PASS + 1))
        else
            echo "  → $score/100 ❌"
            FAIL=$((FAIL + 1))
        fi
    else
        echo "  → 评测失败"
        FAIL=$((FAIL + 1))
        TOTAL=$((TOTAL + 1))
    fi
done < <(find "$SKILLS_ROOT" -name "SKILL.md" -type f | sort)

echo ""
echo "=========================================="
echo "  评测完成"
echo "  总计: $TOTAL | 通过(≥60): $PASS | 未通过: $FAIL"
echo "  报告目录: $OUTPUT_DIR"
echo "=========================================="
