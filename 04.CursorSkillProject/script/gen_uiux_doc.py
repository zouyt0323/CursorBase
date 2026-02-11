#!/usr/bin/env python3
"""
解析 skills/ui-ux-pro-max/ 的 CSV 数据文件，
汇总统计信息并输出到 doc/ui-ux-pro-max/ 目录。

此脚本主要用于统计验证，详细的分析文档由人工编写。
"""

import csv
import os
from pathlib import Path

BASE_DIR   = Path(__file__).parent.parent
DATA_DIR   = BASE_DIR / "skills" / "ui-ux-pro-max" / "src" / "ui-ux-pro-max" / "data"
OUT_DIR    = BASE_DIR / "doc" / "ui-ux-pro-max"


def count_csv_rows(filepath: Path) -> int:
    """统计 CSV 文件的数据行数（不含表头）。"""
    if not filepath.exists():
        return 0
    with open(filepath, encoding='utf-8', errors='replace') as f:
        reader = csv.reader(f)
        rows = list(reader)
        return max(0, len(rows) - 1)  # 减去表头


def main():
    print(f"扫描数据目录: {DATA_DIR}")

    if not DATA_DIR.exists():
        print(f"错误: 数据目录不存在 {DATA_DIR}")
        return

    # 统计主要 CSV 文件
    main_csvs = [
        ("styles.csv", "UI 风格"),
        ("colors.csv", "配色方案"),
        ("typography.csv", "字体搭配"),
        ("ux-guidelines.csv", "UX 指南"),
        ("charts.csv", "图表类型"),
        ("ui-reasoning.csv", "推理规则"),
        ("products.csv", "产品类别"),
        ("landing.csv", "着陆页模式"),
        ("icons.csv", "图标指南"),
        ("react-performance.csv", "React 性能规则"),
        ("web-interface.csv", "Web 界面规则"),
    ]

    print("\n=== 主要数据文件统计 ===\n")
    total_rules = 0
    stats = []
    for filename, label in main_csvs:
        count = count_csv_rows(DATA_DIR / filename)
        total_rules += count
        stats.append((filename, label, count))
        print(f"  {label:15s} ({filename:25s}): {count:4d} 条")

    # 统计技术栈 CSV
    stacks_dir = DATA_DIR / "stacks"
    print("\n=== 技术栈数据统计 ===\n")
    stack_count = 0
    stack_rules = 0
    if stacks_dir.exists():
        for csv_file in sorted(stacks_dir.glob("*.csv")):
            count = count_csv_rows(csv_file)
            stack_name = csv_file.stem
            stack_count += 1
            stack_rules += count
            stats.append((f"stacks/{csv_file.name}", stack_name, count))
            print(f"  {stack_name:20s}: {count:4d} 条规则")

    total_rules += stack_rules
    print(f"\n=== 总计 ===")
    print(f"  主要数据文件: {len(main_csvs)} 个")
    print(f"  技术栈文件:   {stack_count} 个")
    print(f"  总数据条目:   {total_rules} 条")

    # 生成统计汇总 Markdown
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    summary_lines = [
        "# UI UX Pro Max — 数据统计汇总\n",
        "*由 `script/gen_uiux_doc.py` 自动生成*\n",
        "## 主要数据文件\n",
        "| 文件 | 说明 | 数据条数 |",
        "| --- | --- | ---: |",
    ]
    for filename, label, count in stats:
        if not filename.startswith("stacks/"):
            summary_lines.append(f"| {filename} | {label} | {count} |")

    summary_lines.append(f"\n**主要数据合计**：{total_rules - stack_rules} 条\n")

    summary_lines.append("## 技术栈数据\n")
    summary_lines.append("| 技术栈 | 规则数 |")
    summary_lines.append("| --- | ---: |")
    for filename, label, count in stats:
        if filename.startswith("stacks/"):
            summary_lines.append(f"| {label} | {count} |")

    summary_lines.append(f"\n**技术栈合计**：{stack_count} 个栈，{stack_rules} 条规则\n")
    summary_lines.append(f"## 总计\n")
    summary_lines.append(f"- **数据文件总数**：{len(main_csvs) + stack_count}")
    summary_lines.append(f"- **数据条目总数**：{total_rules}")

    out_file = OUT_DIR / "数据统计.md"
    out_file.write_text("\n".join(summary_lines), encoding='utf-8')
    print(f"\n写入 {out_file}")
    print("完成！")


if __name__ == "__main__":
    main()
