#!/usr/bin/env python3
"""
vm0-skills 文档生成脚本
解析 vm0-skills 仓库中的所有 SKILL.md 文件，提取元数据并生成索引文档。
"""

import re
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
SKILLS_DIR = BASE_DIR / "skills" / "vm0-skills"
DOC_DIR = BASE_DIR / "doc" / "vm0-skills"

# 技能分类映射
SKILL_CATEGORIES = {
    "设计与创意": ["figma"],
    "开发与代码平台": ["github", "github-copilot", "gitlab", "supabase", "sentry", "qdrant", "minio"],
    "通信与消息": ["slack", "slack-webhook", "discord", "discord-webhook", "gmail", "resend",
                    "zeptomail", "agentmail", "mailsac", "pushinator"],
    "项目管理与协作": ["notion", "jira", "linear", "monday", "lark", "intercom", "chatwoot",
                       "zendesk", "twenty"],
    "AI与机器学习": ["openai", "deepseek", "perplexity", "minimax", "fal.ai"],
    "媒体与内容": ["youtube", "elevenlabs", "runway", "cloudinary", "htmlcsstoimage", "imgur"],
    "搜索与数据": ["brave-search", "serpapi", "tavily", "firecrawl", "scrapeninja", "bright-data",
                    "supadata"],
    "自动化与工作流": ["apify", "browserbase", "browserless", "cronlytic", "workflow-migration"],
    "社交与内容发布": ["instagram", "dev.to", "hackernews", "qiita", "podchaser"],
    "营销与CRM": ["streak", "kommo", "instantly", "reportei", "shortio", "bitrix"],
    "文档与电子签名": ["pdf4me", "pdfco", "pdforge", "zapsign"],
    "基础设施": ["cloudflare-tunnel", "plausible", "pikvm"],
    "数据表格": ["google-sheets", "axiom"],
    "RSS与订阅": ["rss-fetch"],
    "金融与支付": ["mercury"],
    "VM0平台": ["vm0", "vm0-agent", "vm0-cli"],
}


def parse_frontmatter(content: str) -> dict:
    """解析 SKILL.md 的 YAML frontmatter"""
    info = {"name": "", "description": "", "secrets": []}

    fm_match = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    if not fm_match:
        return info

    fm = fm_match.group(1)

    # name
    name_m = re.search(r'^name:\s*(.+)', fm, re.MULTILINE)
    if name_m:
        info["name"] = name_m.group(1).strip()

    # description (可能多行)
    desc_m = re.search(r'^description:\s*(.+?)(?=\n\w|\nvm0_secrets|\n---|\Z)', fm, re.MULTILINE | re.DOTALL)
    if desc_m:
        desc = desc_m.group(1).strip()
        desc = re.sub(r'\s+', ' ', desc)
        info["description"] = desc

    # secrets
    secrets_m = re.search(r'vm0_secrets:\s*\n((?:\s+-\s+.+\n?)*)', fm)
    if secrets_m:
        info["secrets"] = re.findall(r'-\s+(\S+)', secrets_m.group(1))

    return info


def generate_index():
    """生成技能索引文档"""
    skills_data = {}

    # 扫描所有 SKILL.md
    for skill_dir in sorted(SKILLS_DIR.iterdir()):
        if not skill_dir.is_dir():
            continue
        skill_md = skill_dir / "SKILL.md"
        if not skill_md.exists():
            continue

        content = skill_md.read_text(encoding="utf-8")
        info = parse_frontmatter(content)
        if not info["name"]:
            info["name"] = skill_dir.name
        skills_data[skill_dir.name] = info

    # 生成索引
    lines = [
        "# vm0-skills 技能索引",
        "",
        f"> 自动生成 | 共 **{len(skills_data)}** 个技能 | 分 **{len(SKILL_CATEGORIES)}** 个类别",
        "",
    ]

    # 统计
    lines.append("## 分类统计\n")
    lines.append("| 类别 | 数量 |")
    lines.append("|------|------|")
    for cat, skill_list in SKILL_CATEGORIES.items():
        count = sum(1 for s in skill_list if s in skills_data)
        lines.append(f"| {cat} | {count} |")
    lines.append("")

    # 全部技能表
    lines.append("## 全部技能\n")
    for cat, skill_list in SKILL_CATEGORIES.items():
        lines.append(f"### {cat}\n")
        lines.append("| 技能 | 描述 | 密钥需求 |")
        lines.append("|------|------|----------|")
        for s in skill_list:
            if s in skills_data:
                info = skills_data[s]
                desc = info["description"][:80] + "..." if len(info["description"]) > 80 else info["description"]
                secrets = ", ".join(info["secrets"]) if info["secrets"] else "—"
                lines.append(f"| **{s}** | {desc} | {secrets} |")
        lines.append("")

    # 未分类
    categorized = set()
    for sl in SKILL_CATEGORIES.values():
        categorized.update(sl)
    uncategorized = [s for s in skills_data if s not in categorized]
    if uncategorized:
        lines.append("### 未分类\n")
        lines.append("| 技能 | 描述 | 密钥需求 |")
        lines.append("|------|------|----------|")
        for s in uncategorized:
            info = skills_data[s]
            desc = info["description"][:80] + "..." if len(info["description"]) > 80 else info["description"]
            secrets = ", ".join(info["secrets"]) if info["secrets"] else "—"
            lines.append(f"| **{s}** | {desc} | {secrets} |")
        lines.append("")

    lines.append("\n---\n*自动生成文档*\n")

    out = DOC_DIR / "00_技能索引.md"
    out.write_text("\n".join(lines), encoding="utf-8")
    print(f"生成: {out}")
    return len(skills_data)


def main():
    DOC_DIR.mkdir(parents=True, exist_ok=True)
    total = generate_index()
    print(f"\n完成! 共解析 {total} 个技能")


if __name__ == "__main__":
    main()
