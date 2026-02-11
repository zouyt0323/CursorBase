#!/usr/bin/env python3
"""
解析 skills/anthropics-skills/skills/ 下所有 SKILL.md（YAML frontmatter），
为 doc/anthropics-skills/ 目录生成中文说明文档。
"""

import re
import os
from pathlib import Path
from typing import Dict, List, Tuple

# ── 路径 ──────────────────────────────────────────────
BASE_DIR   = Path(__file__).parent.parent  # 项目根目录
SKILLS_DIR = BASE_DIR / "skills" / "anthropics-skills" / "skills"
OUT_DIR    = BASE_DIR / "doc" / "anthropics-skills"

# ── 技能分类 ──────────────────────────────────────────
# 按照 Anthropic 官方 README 的分类
SKILL_CATEGORIES: Dict[str, Dict[str, str]] = {
    "creative-design": {
        "cn": "创意与设计",
        "desc": "艺术创作、视觉设计、主题美化、前端界面设计",
    },
    "development-technical": {
        "cn": "开发与技术",
        "desc": "MCP 服务器开发、Web 应用测试、技能创建、GIF 制作",
    },
    "enterprise-communication": {
        "cn": "企业与沟通",
        "desc": "内部沟通、品牌规范、文档协作",
    },
    "document-skills": {
        "cn": "文档处理",
        "desc": "Word/PDF/PPT/Excel 文档的创建、编辑、转换与处理",
    },
}

# 每个技能的分类归属
SKILL_TO_CATEGORY: Dict[str, str] = {
    "algorithmic-art":        "creative-design",
    "canvas-design":          "creative-design",
    "frontend-design":        "creative-design",
    "theme-factory":          "creative-design",
    "mcp-builder":            "development-technical",
    "webapp-testing":         "development-technical",
    "web-artifacts-builder":  "development-technical",
    "skill-creator":          "development-technical",
    "slack-gif-creator":      "development-technical",
    "brand-guidelines":       "enterprise-communication",
    "internal-comms":         "enterprise-communication",
    "doc-coauthoring":        "enterprise-communication",
    "docx":                   "document-skills",
    "pdf":                    "document-skills",
    "pptx":                   "document-skills",
    "xlsx":                   "document-skills",
}

# ── 技能中文信息 ──────────────────────────────────────
SKILL_CN_INFO: Dict[str, Dict[str, str]] = {
    "algorithmic-art": {
        "cn_name": "算法艺术",
        "cn_function": "使用 p5.js 创建带有种子随机性和交互参数探索的算法艺术。支持生成式艺术、流场、粒子系统等创作方式。输出 .md、.html 和 .js 文件，通过「算法哲学」的概念来表达计算美学。",
        "cn_domain": "创意设计、生成式艺术、算法可视化、交互式艺术",
        "cn_scenario": "当用户请求使用代码创作艺术、生成式艺术、算法艺术、流场或粒子系统时。创建原创算法艺术，避免复制现有艺术家的作品以防止版权问题。",
    },
    "brand-guidelines": {
        "cn_name": "品牌规范",
        "cn_function": "应用 Anthropic 官方品牌色彩和排版规范到各类制品中，使其具有 Anthropic 的视觉风格。包含主色调（深色 #141413、浅色 #faf9f5、橙色 #d97757、蓝色 #6a9bcc）、强调色以及字体（Poppins 用于标题，Lora 用于正文）等品牌标识资源。",
        "cn_domain": "品牌设计、视觉规范、企业形象、UI 风格指南",
        "cn_scenario": "当需要应用品牌色彩或风格指南、视觉格式化或公司设计标准时使用。",
    },
    "canvas-design": {
        "cn_name": "画布设计",
        "cn_function": "使用设计哲学创作精美的 .png 和 .pdf 格式视觉艺术。通过两步工作流：首先在 .md 文件中创建设计哲学，然后将其实现为视觉作品，强调形式、空间、色彩、构图，文字仅作为视觉点缀。",
        "cn_domain": "视觉设计、海报设计、平面设计、艺术创作",
        "cn_scenario": "当用户要求创建海报、艺术作品、设计或其他静态视觉作品时使用。创建原创视觉设计，避免复制现有艺术家的作品。",
    },
    "doc-coauthoring": {
        "cn_name": "文档协作",
        "cn_function": "引导用户通过结构化工作流协作撰写文档。三阶段流程：(1) 上下文收集；(2) 内容细化与结构优化；(3) 读者测试。支持文档、提案、技术规格、决策文档等结构化内容的高效撰写。",
        "cn_domain": "文档写作、技术文档、提案撰写、协作编辑",
        "cn_scenario": "当用户想要撰写文档、提案、技术规格、决策文档或类似结构化内容时使用。触发词包括：写文档、创建提案、起草规格等。",
    },
    "docx": {
        "cn_name": "Word 文档处理",
        "cn_function": "创建、读取、编辑和处理 Word 文档（.docx 文件）。支持格式化功能包括目录、标题、页码、信头等。可提取或重新组织 .docx 文件内容、插入或替换图片、执行查找替换、处理修订和批注、将内容转换为精美的 Word 文档。.docx 本质上是 XML 文件的 ZIP 压缩包，使用 pandoc、LibreOffice 等工具链。",
        "cn_domain": "文档处理、办公自动化、Word 文档、文件格式转换",
        "cn_scenario": "当用户提到「Word 文档」、「.docx」，或请求制作带格式的专业文档（报告、备忘录、信函、模板）时使用。不适用于 PDF、电子表格、Google Docs 或与文档生成无关的编程任务。",
    },
    "frontend-design": {
        "cn_name": "前端设计",
        "cn_function": "创建独特的、生产级别的前端界面，具有高设计质量。生成创意且精美的代码和 UI 设计，避免通用的 AI 美学（如 Inter 字体、紫色渐变等常见 AI 风格）。涵盖排版、色彩、动效、构图和背景等设计要素，支持 HTML/CSS/JS、React、Vue 等技术栈。",
        "cn_domain": "前端开发、UI/UX 设计、Web 组件、响应式设计",
        "cn_scenario": "当用户要求构建 Web 组件、页面、应用（包括网站、着陆页、仪表板、React 组件、HTML/CSS 布局），或需要美化任何 Web 界面时使用。",
    },
    "internal-comms": {
        "cn_name": "内部沟通",
        "cn_function": "帮助编写各类内部沟通材料的资源集。支持 3P 更新（进展/计划/问题）、公司通讯、FAQ 解答、状态报告、领导力汇报、项目更新和事故报告等格式。根据沟通类型加载对应的指南模板（examples/ 目录），遵循其格式和语调。",
        "cn_domain": "企业沟通、项目管理、报告撰写、团队协作",
        "cn_scenario": "当被要求编写内部沟通材料时使用，包括状态报告、领导力汇报、3P 更新、公司通讯、FAQ、事故报告、项目更新等。",
    },
    "mcp-builder": {
        "cn_name": "MCP 服务器构建",
        "cn_function": "创建高质量的 MCP（模型上下文协议）服务器的指南，使大语言模型能够通过精心设计的工具与外部服务交互。支持 Python（FastMCP）和 Node/TypeScript（MCP SDK）两种技术栈。质量以 LLM 完成真实任务的能力衡量。工作流包括研究规划、API 覆盖率分析、工具命名、上下文管理和错误消息处理等阶段。",
        "cn_domain": "AI 工具开发、API 集成、LLM 工具链、MCP 协议",
        "cn_scenario": "当构建 MCP 服务器以集成外部 API 或服务时使用，无论使用 Python（FastMCP）还是 Node/TypeScript（MCP SDK）。",
    },
    "pdf": {
        "cn_name": "PDF 文档处理",
        "cn_function": "处理 PDF 文件的全方位工具集。支持读取/提取文本和表格、合并/拆分 PDF、旋转页面、添加水印、创建新 PDF、填写 PDF 表单、加密/解密、提取图片、以及对扫描 PDF 进行 OCR 使其可搜索。主要使用 Python 的 pypdf 等库，包含 reference.md 和 forms.md 等高级参考。",
        "cn_domain": "文档处理、PDF 操作、表单处理、OCR 文字识别",
        "cn_scenario": "当用户想对 PDF 文件做任何操作时使用，包括读取、提取、合并、拆分、旋转、加密、填表、OCR 等。只要提到 .pdf 文件或要求生成 PDF，即应使用本技能。",
    },
    "pptx": {
        "cn_name": "PPT 演示文稿处理",
        "cn_function": "处理 .pptx 文件的全方位工具集。支持创建幻灯片、演示文稿、提案稿；读取、解析或提取文本；编辑、修改或更新现有演示文稿；合并或拆分幻灯片文件；处理模板、布局、演讲备注和批注。包含文本提取（markitdown）、缩略图生成和 XML 解包等功能。",
        "cn_domain": "文档处理、演示文稿、PPT 制作、商务报告",
        "cn_scenario": "当涉及 .pptx 文件时使用——无论是作为输入、输出还是两者兼有。触发词包括「幻灯片」、「演示文稿」、「提案稿」或引用 .pptx 文件名。",
    },
    "skill-creator": {
        "cn_name": "技能创建器",
        "cn_function": "创建有效技能的指南。技能是模块化的软件包，可通过专业知识、工作流和工具集成来扩展 Claude 的能力。强调简洁性、适当的自由度（高/中/低），以及技能结构（SKILL.md 加可选资源）。包含初始化、打包和快速验证脚本。",
        "cn_domain": "AI 工具开发、技能扩展、Claude 定制、插件开发",
        "cn_scenario": "当用户想要创建新技能或更新现有技能以扩展 Claude 的能力（包括专业知识、工作流或工具集成）时使用。",
    },
    "slack-gif-creator": {
        "cn_name": "Slack GIF 制作",
        "cn_function": "为 Slack 创建优化的动画 GIF 的知识和工具。提供约束（尺寸：128x128 表情符号、480x480 消息）、验证工具和动画概念。使用 GIFBuilder 和 PIL 构建帧、添加并保存为 Slack 友好的优化格式。",
        "cn_domain": "动画制作、GIF 创作、Slack 集成、视觉通信",
        "cn_scenario": "当用户请求为 Slack 创建动画 GIF 时使用，例如「为我做一个 X 做 Y 动作的 Slack GIF」。",
    },
    "theme-factory": {
        "cn_name": "主题工厂",
        "cn_function": "为各类制品（幻灯片、文档、报告、HTML 着陆页等）应用主题样式的工具包。提供 10 个预设主题（海洋深处、日落大道、森林树冠、现代极简、黄金时刻、北极霜冻、沙漠玫瑰、科技创新、植物花园、午夜银河），每个主题包含配色方案和字体搭配，也可即时生成新主题。",
        "cn_domain": "视觉设计、主题定制、样式管理、品牌美化",
        "cn_scenario": "当需要为幻灯片、文档、报告、HTML 页面等制品应用统一的视觉主题时使用。可从 10 个预设主题中选择，或动态生成新主题。",
    },
    "webapp-testing": {
        "cn_name": "Web 应用测试",
        "cn_function": "使用 Playwright 交互和测试本地 Web 应用的工具包。支持验证前端功能、调试 UI 行为、捕获浏览器截图和查看浏览器日志。提供 with_server.py 脚本管理服务器生命周期，支持静态和动态应用、单服务器和多服务器场景。",
        "cn_domain": "Web 测试、前端测试、UI 自动化、Playwright",
        "cn_scenario": "当需要与本地 Web 应用交互并测试时使用，包括验证前端功能、调试 UI 行为、捕获截图和查看日志。",
    },
    "web-artifacts-builder": {
        "cn_name": "Web 制品构建器",
        "cn_function": "使用现代前端技术（React、Tailwind CSS、shadcn/ui）创建精细的多组件 HTML 制品的工具套件。技术栈：React 18 + TypeScript + Vite + Parcel + Tailwind CSS + shadcn/ui。工作流包括初始化、编辑代码、打包和展示。适用于需要状态管理、路由或 shadcn/ui 组件的复杂制品。",
        "cn_domain": "前端开发、组件构建、React 应用、UI 工具链",
        "cn_scenario": "当需要使用 React、Tailwind CSS、shadcn/ui 创建复杂的多组件 HTML 制品时使用。不适用于简单的单文件 HTML/JSX 制品。",
    },
    "xlsx": {
        "cn_name": "Excel 电子表格处理",
        "cn_function": "处理电子表格文件（.xlsx、.xlsm、.csv、.tsv）的全方位工具。支持打开、读取、编辑、修复现有文件（添加列、计算公式、格式化、图表、清理数据）；从头或从其他数据源创建新电子表格；在表格文件格式之间转换。财务模型遵循专业规范：颜色约定（蓝色输入、黑色公式、绿色内部链接、红色外部链接、黄色关键假设）和数字格式规范。",
        "cn_domain": "数据处理、电子表格、Excel 操作、财务建模",
        "cn_scenario": "当电子表格文件（.xlsx、.xlsm、.csv、.tsv）是主要输入或输出时使用。包括读取、编辑、创建电子表格，或清理和重组混乱的表格数据。当用户提到电子表格文件名时触发。不适用于 Word 文档、HTML 报告、独立脚本或数据库流水线。",
    },
}


def generate_skill_section(skill_id: str, description: str) -> str:
    """为单个技能生成中文文档段落。"""
    info = SKILL_CN_INFO.get(skill_id, {})
    cn_name = info.get("cn_name", skill_id)
    cn_func = info.get("cn_function", "（无中文描述）")
    cn_domain = info.get("cn_domain", "")
    cn_scenario = info.get("cn_scenario", "")

    parts = []
    parts.append(f"## {skill_id}\n")
    parts.append(f"**中文名**：{cn_name}\n")

    parts.append("### 功能\n")
    parts.append(f"{cn_func}\n")
    parts.append("**英文原文**：\n")
    parts.append(f"{description}\n")

    parts.append("### 使用领域\n")
    parts.append(f"{cn_domain}\n")

    parts.append("### 使用场景\n")
    parts.append(f"{cn_scenario}\n")

    # 许可证信息
    cat = SKILL_TO_CATEGORY.get(skill_id, "")
    if cat == "document-skills":
        parts.append("\n> **许可证**：专有软件（Proprietary），仅供参考，详见 LICENSE.txt\n")
    else:
        parts.append("\n> **许可证**：Apache 2.0 开源，详见 LICENSE.txt\n")

    return "\n".join(parts)


def parse_frontmatter(skill_path: Path) -> Dict[str, str]:
    """解析 SKILL.md 的 YAML frontmatter。"""
    content = skill_path.read_text(encoding='utf-8')
    m = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    if not m:
        return {"name": skill_path.parent.name, "description": ""}

    fm = m.group(1)
    result = {}
    # 简单的 YAML 解析（name 和 description）
    for key in ["name", "description", "license"]:
        km = re.search(rf'^{key}:\s*(.+?)$', fm, re.MULTILINE)
        if km:
            val = km.group(1).strip().strip('"').strip("'")
            result[key] = val

    # description 可能跨多行
    dm = re.search(r'^description:\s*(.*?)(?=^[a-z_-]+:|\Z)', fm, re.MULTILINE | re.DOTALL)
    if dm:
        desc = dm.group(1).strip()
        # 合并多行
        desc = re.sub(r'\s*\n\s*', ' ', desc)
        result["description"] = desc

    if "name" not in result:
        result["name"] = skill_path.parent.name

    return result


def main():
    print(f"扫描技能目录: {SKILLS_DIR}")

    # 收集所有技能
    skills_data = {}
    for skill_dir in sorted(SKILLS_DIR.iterdir()):
        skill_md = skill_dir / "SKILL.md"
        if skill_md.exists():
            fm = parse_frontmatter(skill_md)
            sid = fm.get("name", skill_dir.name)
            skills_data[sid] = fm
            print(f"  发现: {sid}")

    total = len(skills_data)
    print(f"\n共发现 {total} 个技能")

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    # ── 1. 按分类生成文档 ──
    cat_skills: Dict[str, List[str]] = {}
    for sid in skills_data:
        cat = SKILL_TO_CATEGORY.get(sid, "uncategorized")
        cat_skills.setdefault(cat, []).append(sid)

    for cat_id, sids in sorted(cat_skills.items()):
        cat_info = SKILL_CATEGORIES.get(cat_id, {"cn": cat_id, "desc": ""})
        doc_parts = [
            f"# {cat_info['cn']}（{cat_id}）\n",
            f"共 {len(sids)} 个技能。{cat_info['desc']}\n",
        ]
        for sid in sorted(sids):
            desc = skills_data[sid].get("description", "")
            doc_parts.append("---\n")
            doc_parts.append(generate_skill_section(sid, desc))

        out_file = OUT_DIR / f"skills_{cat_id}.md"
        out_file.write_text("\n".join(doc_parts), encoding='utf-8')
        print(f"  写入 {out_file.name} ({len(sids)} 个技能)")

    # ── 2. 分类索引 ──
    idx_parts = [
        "# Anthropic Skills 分类索引\n",
        "本文档对 Anthropic 官方 Claude Skills 按分类整理，并为每个技能提供中文的**功能**、**使用领域**与**使用场景**说明。\n",
        f"**最新统计**：共 **{total}** 个技能，**{len(cat_skills)}** 个分类。\n",
        "| 分类 | 中文名 | 技能数量 | 文档链接 |",
        "| --- | --- | --- | --- |",
    ]
    for cat_id in sorted(cat_skills.keys()):
        cat_info = SKILL_CATEGORIES.get(cat_id, {"cn": cat_id})
        cnt = len(cat_skills[cat_id])
        idx_parts.append(f"| {cat_id} | {cat_info['cn']} | {cnt} | [skills_{cat_id}.md](skills_{cat_id}.md) |")
    idx_parts.append("\n---\n")

    (OUT_DIR / "00_分类索引.md").write_text("\n".join(idx_parts), encoding='utf-8')
    print("  写入 00_分类索引.md")

    # ── 3. README ──
    detail_rows = []
    for cat_id in sorted(cat_skills.keys()):
        cat_info = SKILL_CATEGORIES.get(cat_id, {"cn": cat_id})
        cnt = len(cat_skills[cat_id])
        detail_rows.append(f"| skills_{cat_id}.md | **{cat_info['cn']}**（{cnt} 个） |")

    detail_table = "\n".join(detail_rows)
    cat_names = ", ".join(sorted(cat_skills.keys()))

    readme = f"""# Anthropic Skills 中文说明文档

本目录包含对 **Anthropic 官方 Claude Skills** 的**分类索引**与**中文说明**。
数据来源：[https://github.com/anthropics/skills](https://github.com/anthropics/skills)

**未对 `skills` 文件夹做任何修改、新增或删除。**

## 文档结构

| 文件 | 说明 |
|------|------|
| [00_分类索引.md](00_分类索引.md) | 按分类总览，含各分类技能数量与链接 |
{detail_table}

## 每个技能的说明格式

每个技能均包含：

- **中文名**：该技能的中文名称，便于快速识别。
- **功能**：该技能能做什么，用中文详细解释其能力与侧重点；并保留**英文原文**便于对照。
- **使用领域**：该技能适用的技术/业务领域。
- **使用场景**：具体应在何时使用。
- **许可证**：开源（Apache 2.0）或专有（Proprietary）。

## 关于 Anthropic Skills

Skills 是 Claude 动态加载的指令、脚本和资源文件夹，用于提升特定任务的执行质量。
技能教会 Claude 以可重复的方式完成特定任务，无论是创建符合品牌规范的文档、分析数据，还是自动化个人任务。

更多信息请参考：
- [什么是 Skills？](https://support.claude.com/en/articles/12512176-what-are-skills)
- [在 Claude 中使用 Skills](https://support.claude.com/en/articles/12512180-using-skills-in-claude)
- [如何创建自定义 Skills](https://support.claude.com/en/articles/12512198-creating-custom-skills)

## 统计

- **总技能数**：{total}
- **分类数**：{len(cat_skills)}（{cat_names}）
- **来源**：Anthropic 官方 GitHub 仓库 anthropics/skills
- **生成脚本**：`script/gen_anthropic_skills_doc.py`
"""

    (OUT_DIR / "README.md").write_text(readme, encoding='utf-8')
    print("  写入 README.md")

    print(f"\n完成！共生成 {len(cat_skills) + 2} 个文件。")


if __name__ == "__main__":
    main()
