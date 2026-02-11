#!/usr/bin/env python3
"""
解析 skills/antigravity-awesome-skills/CATALOG.md，
为 doc/antigravity-awesome-skills/ 目录生成中文说明文档。
"""

import re
import os
from pathlib import Path
from typing import List, Dict, Any, Tuple

# ── 路径 ──────────────────────────────────────────────
BASE_DIR   = Path(__file__).parent.parent  # script/ 的上一级即项目根目录
CATALOG    = BASE_DIR / "skills" / "antigravity-awesome-skills" / "CATALOG.md"
OUT_DIR    = BASE_DIR / "doc" / "antigravity-awesome-skills"

# ── 分类中文名 ────────────────────────────────────────
CATEGORY_CN: Dict[str, str] = {
    "architecture":   "架构与设计",
    "business":       "商业与营销",
    "data-ai":        "数据与 AI",
    "development":    "开发与实现",
    "general":        "通用与综合",
    "infrastructure": "基础设施与运维",
    "security":       "安全与合规",
    "testing":        "测试与质量",
    "workflow":       "工作流与协作",
}

# ── 技能 ID 片段 → 中文 ──────────────────────────────
SEGMENT_CN: Dict[str, str] = {
    # 常见技术术语
    "angular": "Angular", "react": "React", "vue": "Vue", "next": "Next",
    "nuxt": "Nuxt", "svelte": "Svelte", "remix": "Remix", "astro": "Astro",
    "python": "Python", "rust": "Rust", "go": "Go", "java": "Java",
    "kotlin": "Kotlin", "swift": "Swift", "ruby": "Ruby", "php": "PHP",
    "typescript": "TypeScript", "javascript": "JavaScript", "node": "Node",
    "deno": "Deno", "bun": "Bun", "elixir": "Elixir", "dart": "Dart",
    "flutter": "Flutter", "django": "Django", "flask": "Flask",
    "fastapi": "FastAPI", "express": "Express", "nest": "Nest",
    "spring": "Spring", "rails": "Rails", "laravel": "Laravel",
    "docker": "Docker", "kubernetes": "Kubernetes", "k8s": "K8s",
    "aws": "AWS", "azure": "Azure", "gcp": "GCP", "terraform": "Terraform",
    "ansible": "Ansible", "nginx": "Nginx", "redis": "Redis",
    "postgres": "PostgreSQL", "mysql": "MySQL", "mongo": "MongoDB",
    "graphql": "GraphQL", "grpc": "gRPC", "rest": "REST",
    "api": "API", "sdk": "SDK", "cli": "CLI", "ui": "UI", "ux": "UX",
    "css": "CSS", "html": "HTML", "sass": "Sass", "tailwind": "Tailwind",
    "webpack": "Webpack", "vite": "Vite", "esbuild": "esbuild",
    "git": "Git", "ci": "CI", "cd": "CD", "devops": "DevOps",
    "ml": "机器学习", "ai": "人工智能", "llm": "大语言模型", "nlp": "自然语言处理",
    "rag": "RAG 检索增强生成", "embedding": "向量嵌入", "vector": "向量",
    "agent": "智能体", "multi": "多", "mcp": "MCP",
    "seo": "SEO 搜索引擎优化",
    "auth": "认证", "oauth": "OAuth", "jwt": "JWT", "rbac": "RBAC",
    "sql": "SQL", "nosql": "NoSQL", "orm": "ORM",
    "test": "测试", "testing": "测试", "tdd": "TDD 测试驱动开发",
    "e2e": "端到端", "unit": "单元", "integration": "集成",
    "debug": "调试", "debugging": "调试", "log": "日志", "logging": "日志",
    "monitor": "监控", "monitoring": "监控", "observability": "可观测性",
    "security": "安全", "pentest": "渗透测试", "vulnerability": "漏洞",
    "compliance": "合规", "audit": "审计", "encryption": "加密",
    "deploy": "部署", "deployment": "部署", "release": "发布",
    "build": "构建", "builder": "构建器", "scaffold": "脚手架",
    "config": "配置", "configuration": "配置",
    "migration": "迁移", "upgrade": "升级", "refactor": "重构",
    "performance": "性能", "optimization": "优化", "optimize": "优化",
    "cache": "缓存", "caching": "缓存",
    "queue": "消息队列", "messaging": "消息通信", "event": "事件",
    "stream": "流处理", "streaming": "流处理",
    "micro": "微", "service": "服务", "services": "服务",
    "serverless": "无服务器",
    "container": "容器", "orchestration": "编排",
    "database": "数据库", "data": "数据", "analytics": "分析",
    "pipeline": "流水线", "etl": "ETL",
    "infra": "基础设施", "infrastructure": "基础设施",
    "network": "网络", "networking": "网络",
    "storage": "存储", "backup": "备份",
    "design": "设计", "pattern": "模式", "patterns": "模式",
    "clean": "整洁", "solid": "SOLID",
    "ddd": "领域驱动设计", "domain": "领域",
    "architecture": "架构", "architect": "架构师",
    "review": "评审", "code": "代码",
    "doc": "文档", "docs": "文档", "documentation": "文档",
    "comment": "注释", "readme": "README",
    "style": "风格", "guide": "指南", "guidelines": "指南",
    "workflow": "工作流", "automation": "自动化", "automate": "自动化",
    "changelog": "变更日志", "version": "版本", "versioning": "版本管理",
    "i18n": "国际化", "l10n": "本地化", "localization": "本地化",
    "accessibility": "无障碍", "a11y": "无障碍",
    "responsive": "响应式", "mobile": "移动端",
    "android": "Android", "ios": "iOS",
    "web": "Web", "app": "应用", "application": "应用",
    "frontend": "前端", "backend": "后端", "fullstack": "全栈",
    "state": "状态", "management": "管理", "manager": "管理器",
    "error": "错误", "handling": "处理", "handler": "处理器",
    "validation": "校验", "validator": "校验器",
    "form": "表单", "input": "输入", "output": "输出",
    "file": "文件", "image": "图像", "video": "视频", "audio": "音频",
    "chat": "聊天", "bot": "机器人", "assistant": "助手",
    "search": "搜索", "index": "索引", "indexing": "索引",
    "scraper": "爬虫", "scraping": "抓取", "crawler": "爬虫",
    "email": "邮件", "notification": "通知", "alert": "告警",
    "payment": "支付", "billing": "计费", "subscription": "订阅",
    "pricing": "定价", "invoice": "发票",
    "user": "用户", "role": "角色", "permission": "权限",
    "project": "项目", "task": "任务", "issue": "问题",
    "plan": "计划", "planning": "规划",
    "setup": "配置", "init": "初始化", "initialize": "初始化",
    "create": "创建", "generator": "生成器", "generate": "生成",
    "convert": "转换", "converter": "转换器", "transform": "变换",
    "analyze": "分析", "analyzer": "分析器", "analysis": "分析",
    "improve": "改进", "improvement": "改进",
    "driven": "驱动", "based": "基于",
    "system": "系统", "systems": "系统",
    "feature": "功能", "features": "功能",
    "model": "模型", "models": "模型",
    "schema": "模式/Schema", "type": "类型", "types": "类型",
    "smart": "智能", "auto": "自动",
    "full": "全", "stack": "栈",
    "real": "实时", "time": "时间",
    "high": "高", "low": "低",
    "open": "开源", "source": "源码",
    "standard": "标准", "standards": "标准",
    "best": "最佳", "practice": "实践", "practices": "实践",
    "advanced": "高级", "expert": "专家",
    "modern": "现代", "legacy": "遗留",
    "clean": "整洁", "minimal": "极简",
    "enterprise": "企业级",
    "cloud": "云", "native": "原生",
    "edge": "边缘", "compute": "计算",
    "record": "记录", "records": "记录",
    "decision": "决策",
    "prompt": "提示词", "engineering": "工程",
    "cursor": "Cursor", "copilot": "Copilot",
    "rube": "Rube", "composio": "Composio",
}

# ── 常见英文短语 → 中文（用于功能翻译） ──────────────
PHRASE_CN: List[Tuple[str, str]] = [
    # 长短语放前面，优先匹配
    ("Use PROACTIVELY", "主动使用"),
    ("Use proactively", "主动使用"),
    ("use proactively", "主动使用"),
    ("Use when", "适用于"),
    ("use when", "适用于"),
    ("Use this skill when", "适用于"),
    ("This skill should be used when", "适用于"),
    ("Always search tools first", "始终先搜索可用工具"),
    ("Always search tools first for current schemas", "始终先搜索可用工具以获取最新 schema"),
    ("best practices", "最佳实践"),
    ("Best practices", "最佳实践"),
    ("deep knowledge", "深入掌握"),
    ("Deep knowledge", "深入掌握"),
    ("with expertise in", "精通"),
    ("specializing in", "专攻"),
    ("Specializing in", "专攻"),
    ("expert with", "专家，擅长"),
    ("Expert with", "专家，擅长"),
    ("Master modern", "精通现代"),
    ("master modern", "精通现代"),
    ("state management", "状态管理"),
    ("State Management", "状态管理"),
    ("error handling", "错误处理"),
    ("Error Handling", "错误处理"),
    ("code review", "代码评审"),
    ("Code Review", "代码评审"),
    ("pull request", "Pull Request"),
    ("Pull Request", "Pull Request"),
    ("design patterns", "设计模式"),
    ("Design Patterns", "设计模式"),
    ("clean architecture", "整洁架构"),
    ("Clean Architecture", "整洁架构"),
    ("event-driven", "事件驱动"),
    ("Event-driven", "事件驱动"),
    ("domain-driven", "领域驱动"),
    ("Domain-driven", "领域驱动"),
    ("test-driven", "测试驱动"),
    ("Test-driven", "测试驱动"),
    ("dependency injection", "依赖注入"),
    ("Dependency Injection", "依赖注入"),
    ("continuous integration", "持续集成"),
    ("Continuous Integration", "持续集成"),
    ("continuous deployment", "持续部署"),
    ("Continuous Deployment", "持续部署"),
    ("machine learning", "机器学习"),
    ("Machine Learning", "机器学习"),
    ("natural language", "自然语言"),
    ("Natural Language", "自然语言"),
    ("real-time", "实时"),
    ("Real-time", "实时"),
    ("end-to-end", "端到端"),
    ("End-to-end", "端到端"),
    ("cross-platform", "跨平台"),
    ("Cross-platform", "跨平台"),
    ("open source", "开源"),
    ("Open Source", "开源"),
    ("version control", "版本控制"),
    ("Version Control", "版本控制"),
    ("access control", "访问控制"),
    ("Access Control", "访问控制"),
    ("role-based", "基于角色的"),
    ("Role-based", "基于角色的"),
    ("token-based", "基于令牌的"),
    ("Token-based", "基于令牌的"),
    ("zero trust", "零信任"),
    ("Zero Trust", "零信任"),
    ("supply chain", "供应链"),
    ("attack surface", "攻击面"),
    ("threat model", "威胁建模"),
    ("penetration testing", "渗透测试"),
    ("security audit", "安全审计"),
    ("vulnerability scan", "漏洞扫描"),
    ("data pipeline", "数据流水线"),
    ("Data Pipeline", "数据流水线"),
    ("data lake", "数据湖"),
    ("data warehouse", "数据仓库"),
    ("feature engineering", "特征工程"),
    ("model training", "模型训练"),
    ("prompt engineering", "提示词工程"),
    ("Prompt Engineering", "提示词工程"),
    ("fine-tuning", "微调"),
    ("Fine-tuning", "微调"),
    ("retrieval augmented", "检索增强"),
    ("Retrieval Augmented", "检索增强"),
    ("vector database", "向量数据库"),
    ("knowledge graph", "知识图谱"),
    ("API design", "API 设计"),
    ("api design", "API 设计"),
    ("responsive design", "响应式设计"),
    ("system design", "系统设计"),
    ("database design", "数据库设计"),
    ("schema design", "模式设计"),
    ("microservice", "微服务"),
    ("Microservice", "微服务"),
    ("microservices", "微服务"),
    ("Microservices", "微服务"),
    ("serverless", "无服务器"),
    ("Serverless", "无服务器"),
    ("monorepo", "Monorepo"),
    ("container", "容器"),
    ("Container", "容器"),
    ("orchestration", "编排"),
    ("load balancing", "负载均衡"),
    ("auto-scaling", "自动伸缩"),
    ("high availability", "高可用"),
    ("disaster recovery", "灾难恢复"),
    ("infrastructure as code", "基础设施即代码"),
    ("Infrastructure as Code", "基础设施即代码"),
    ("via Rube MCP (Composio)", "通过 Rube MCP（Composio）"),
    ("Automate", "自动化"),
    ("automate", "自动化"),
    ("Initialize", "初始化"),
    ("initialize", "初始化"),
    ("Generate", "生成"),
    ("generate", "生成"),
    ("Implement", "实现"),
    ("implement", "实现"),
    ("Configure", "配置"),
    ("configure", "配置"),
    ("Optimize", "优化"),
    ("optimize", "优化"),
    ("Analyze", "分析"),
    ("analyze", "分析"),
    ("Validate", "校验"),
    ("validate", "校验"),
    ("Build", "构建"),
    ("Deploy", "部署"),
    ("Monitor", "监控"),
    ("Manage", "管理"),
    ("manage", "管理"),
    ("Create", "创建"),
    ("create", "创建"),
    ("Review", "评审"),
    ("Debug", "调试"),
    ("Test", "测试"),
    ("Scan", "扫描"),
    ("Search", "搜索"),
]

# ── 使用场景常见短语翻译 ──────────────────────────────
SCENARIO_CN: List[Tuple[str, str]] = [
    ("setting up", "配置或搭建"),
    ("Setting up", "配置或搭建"),
    ("working with", "使用或处理"),
    ("Working with", "使用或处理"),
    ("building", "构建"),
    ("Building", "构建"),
    ("creating", "创建"),
    ("Creating", "创建"),
    ("implementing", "实现"),
    ("Implementing", "实现"),
    ("debugging", "调试"),
    ("Debugging", "调试"),
    ("testing", "测试"),
    ("Testing", "测试"),
    ("optimizing", "优化"),
    ("Optimizing", "优化"),
    ("deploying", "部署"),
    ("Deploying", "部署"),
    ("migrating", "迁移"),
    ("Migrating", "迁移"),
    ("configuring", "配置"),
    ("Configuring", "配置"),
    ("managing", "管理"),
    ("Managing", "管理"),
    ("analyzing", "分析"),
    ("Analyzing", "分析"),
    ("reviewing", "评审"),
    ("Reviewing", "评审"),
    ("writing", "编写"),
    ("Writing", "编写"),
    ("refactoring", "重构"),
    ("Refactoring", "重构"),
    ("choosing between", "在……之间选择"),
    ("integrating", "集成"),
    ("Integrating", "集成"),
    ("monitoring", "监控"),
    ("Monitoring", "监控"),
    ("automating", "自动化"),
    ("Automating", "自动化"),
    ("securing", "保护安全"),
    ("Securing", "保护安全"),
    ("scaling", "扩展"),
    ("Scaling", "扩展"),
    ("designing", "设计"),
    ("Designing", "设计"),
    ("documenting", "编写文档"),
    ("Documenting", "编写文档"),
    ("auditing", "审计"),
    ("Auditing", "审计"),
    ("scanning", "扫描"),
    ("Scanning", "扫描"),
    ("generating", "生成"),
    ("Generating", "生成"),
    ("improving", "改进"),
    ("Improving", "改进"),
    ("converting", "转换"),
    ("Converting", "转换"),
    ("evaluating", "评估"),
    ("Evaluating", "评估"),
]


# ════════════════════════════════════════════════════════
# 辅助函数
# ════════════════════════════════════════════════════════

def parse_catalog(content: str) -> Dict[str, List[Dict[str, str]]]:
    """解析 CATALOG.md，返回 {category: [skill_dict, ...]}"""
    result: Dict[str, List[Dict[str, str]]] = {}
    current_cat = None

    # 先把跨行的表格行合并（有些 description 里有换行）
    lines = content.splitlines()
    merged: List[str] = []
    for line in lines:
        # 如果上一行是未闭合的表格行（列数不够），则拼接
        if merged and merged[-1].startswith('|') and merged[-1].count('|') < 5:
            merged[-1] = merged[-1].rstrip() + ' ' + line.lstrip()
        else:
            merged.append(line)

    for line in merged:
        # 分类标题：## category (N)
        m = re.match(r'^## (\S+)\s*\((\d+)\)', line)
        if m:
            current_cat = m.group(1)
            result[current_cat] = []
            continue

        # 表格行（跳过表头和分隔行）
        if current_cat and line.startswith('|') and not line.startswith('| ---') and not line.startswith('| Skill'):
            cols = [c.strip() for c in line.split('|')]
            # cols: ['', skill, description, tags, triggers, '']
            if len(cols) >= 5:
                skill_id = cols[1].strip('` ')
                result[current_cat].append({
                    'id': skill_id,
                    'description': cols[2],
                    'tags': cols[3],
                    'triggers': cols[4],
                })
    return result


def skill_id_to_chinese(sid: str) -> str:
    """将 skill-id 转为中文名。"""
    parts = re.split(r'[-_]', sid)
    cn_parts = []
    for p in parts:
        low = p.lower()
        if low in SEGMENT_CN:
            cn_parts.append(SEGMENT_CN[low])
        else:
            cn_parts.append(p.capitalize())
    return " ".join(cn_parts)


def first_sentence(desc: str) -> str:
    """取描述的第一句话。"""
    # 先去掉 "Use when ..." / "This skill ..." 前缀的句子
    # 取到第一个句号
    m = re.match(r'^(.+?\.)\s', desc)
    if m:
        return m.group(1)
    return desc[:200]


def translate_desc(desc: str) -> str:
    """尽量把英文描述翻译成中文概要。"""
    text = first_sentence(desc)
    # 先替换长短语
    for en, cn in PHRASE_CN:
        text = text.replace(en, cn)
    # 再替换单词（全词匹配，不区分大小写）
    for en, cn in sorted(SEGMENT_CN.items(), key=lambda x: -len(x[0])):
        text = re.sub(r'\b' + re.escape(en) + r'\b', cn, text, flags=re.IGNORECASE)
    return text


def domain_for_skill(category: str, tags: str, desc: str) -> str:
    """推断使用领域。"""
    cat_cn = CATEGORY_CN.get(category, category)

    # 从标签提取更细的领域
    tag_list = [t.strip() for t in tags.split(',') if t.strip()]
    tag_descs = []
    for t in tag_list:
        low = t.lower()
        if low in SEGMENT_CN:
            tag_descs.append(SEGMENT_CN[low])
        else:
            tag_descs.append(t)
    tag_str = "、".join(tag_descs[:6]) if tag_descs else ""

    base_domain_map = {
        "architecture":   "系统架构、技术选型、架构决策与文档、事件驱动与领域设计",
        "business":       "商业策略、市场营销、SEO、内容创作、客户运营",
        "data-ai":        "数据工程、机器学习、大语言模型、RAG、数据分析与可视化",
        "development":    "软件开发、前后端框架、API 设计、编程语言与工具链",
        "general":        "通用开发、调试、文档、代码规范、工具配置",
        "infrastructure": "云计算、容器化、CI/CD、基础设施即代码、监控与运维",
        "security":       "网络安全、渗透测试、合规审计、安全编码、漏洞管理",
        "testing":        "单元测试、集成测试、端到端测试、TDD、测试自动化",
        "workflow":       "工作流自动化、项目管理、版本控制、变更日志、第三方集成",
    }
    base = base_domain_map.get(category, cat_cn)
    if tag_str:
        return f"{base}；相关标签：{tag_str}"
    return base


def build_scenarios(triggers: str, desc: str) -> str:
    """生成使用场景。"""
    lines = []
    lines.append("以下为推荐使用本技能的典型场景及触发方式，满足任一即可考虑启用。\n")

    # 从 description 中提取 "Use when ..." 部分
    use_when = ""
    m = re.search(r'(?:Use when|Use this skill when|This skill should be used when)\s+(.+?)(?:\.\s|$)', desc)
    if m:
        raw = m.group(1).strip().rstrip('.')
        # 翻译
        translated = raw
        for en, cn in SCENARIO_CN:
            translated = translated.replace(en, cn)
        for en, cn in sorted(SEGMENT_CN.items(), key=lambda x: -len(x[0])):
            translated = re.sub(r'\b' + re.escape(en) + r'\b', cn, translated, flags=re.IGNORECASE)
        lines.append(f"- 在以下情况下可使用本技能：**{translated}**。\n")

    # 触发关键词
    trigger_list = [t.strip() for t in triggers.split(',') if t.strip()]
    if trigger_list:
        kw = "、".join(trigger_list[:15])
        lines.append(f"- **触发关键词**：在对话或任务中出现以下任一关键词时，本技能可能被自动启用：{kw}。\n")

    return "\n".join(lines)


def generate_category_doc(category: str, skills: List[Dict[str, str]]) -> str:
    """为一个分类生成完整文档。"""
    cat_cn = CATEGORY_CN.get(category, category)
    parts = [f"# {cat_cn}（{category}）\n\n共 {len(skills)} 个技能。\n"]

    for sk in skills:
        sid = sk['id']
        desc = sk['description']
        tags = sk['tags']
        triggers = sk['triggers']

        cn_name = skill_id_to_chinese(sid)
        cn_func = translate_desc(desc)
        en_first = first_sentence(desc)
        domain = domain_for_skill(category, tags, desc)
        scenarios = build_scenarios(triggers, desc)

        parts.append(f"\n---\n\n## {sid}\n")
        parts.append(f"\n**中文名**：{cn_name}\n")
        parts.append(f"\n### 功能\n")
        parts.append(f"\n{cn_func}\n")
        parts.append(f"\n**英文原文**：\n")
        parts.append(f"\n{en_first}\n")
        parts.append(f"\n### 使用领域\n")
        parts.append(f"\n{domain}\n")
        parts.append(f"\n### 使用场景\n")
        parts.append(f"\n{scenarios}\n")
        parts.append(f"\n<details>\n<summary>英文描述（原文）</summary>\n\n{desc}\n\n</details>\n")

    return "\n".join(parts)


def generate_index(catalog: Dict[str, List[Dict[str, str]]]) -> str:
    """生成分类索引。"""
    total = sum(len(v) for v in catalog.values())
    lines = [
        "# Cursor Skills 分类索引\n",
        "本文档对 Cursor Skills 按 CATALOG 分类整理，并为每个技能提供中文的**功能**、**使用领域**与**使用场景**说明。\n",
        f"**最新统计**：共 **{total}** 个技能，**{len(catalog)}** 个分类。\n",
        "| 分类 | 中文名 | 技能数量 | 文档链接 |",
        "| --- | --- | --- | --- |",
    ]
    for cat in catalog:
        cn = CATEGORY_CN.get(cat, cat)
        cnt = len(catalog[cat])
        lines.append(f"| {cat} | {cn} | {cnt} | [skills_{cat}.md](skills_{cat}.md) |")
    lines.append("\n---\n")
    return "\n".join(lines)


def generate_readme(catalog: Dict[str, List[Dict[str, str]]]) -> str:
    """生成 README.md。"""
    total = sum(len(v) for v in catalog.values())
    cat_count = len(catalog)

    detail_rows = []
    for cat in catalog:
        cn = CATEGORY_CN.get(cat, cat)
        cnt = len(catalog[cat])
        detail_rows.append(f"| skills_{cat}.md | **{cn}**（{cnt} 个） |")

    detail_table = "\n".join(detail_rows)
    cat_names = ", ".join(catalog.keys())

    return f"""# Cursor Skills 中文说明文档

本目录包含对 **Cursor Skills** 的**分类索引**与**中文说明**，便于查找每个技能的功能与使用方法。
**未对 `skills` 文件夹做任何修改、新增或删除。**

## 文档结构

| 文件 | 说明 |
|------|------|
| [00_分类索引.md](00_分类索引.md) | 按 CATALOG 的 {cat_count} 大分类总览，含各分类技能数量与链接 |
{detail_table}
| [Android_开发相关_Skills.md](Android_开发相关_Skills.md) | **Android 开发**：适用于 Android 系统开发的技能汇总 |
| [如何使用_Skills.md](如何使用_Skills.md) | 手把手教程：如何安装与使用 Cursor Skills |

## 每个技能的说明格式

每个技能均包含：

- **中文名**：该技能的英文 ID 对应的中文名称，便于快速识别。
- **功能**：该技能能做什么，用中文详细解释其能力与侧重点；并保留**英文原文**（首句）便于对照。
- **使用领域**：该技能适用的技术/业务领域，并附相关标签。
- **使用场景**：具体应在何时使用——例如「当……时」、以及对话中出现哪些关键词时会触发。
- **英文描述（原文）**：折叠块中保留 CATALOG 原始英文描述，便于对照。

## 如何查找技能

1. 从 [00_分类索引.md](00_分类索引.md) 确定大致分类。
2. 打开对应 `skills_<分类>.md`，用编辑器搜索技能 ID（如 `angular`、`rag-engineer`）。
3. 或在整个 `doc` 目录下全文搜索关键词（如「RAG」「SEO」「测试」）。

## 数据来源与更新

- 分类与技能列表来自仓库内 `skills/antigravity-awesome-skills/CATALOG.md`（只读，未修改）。
- 中文「功能」「使用方法」由脚本根据 CATALOG 描述与触发词自动生成；若需最准确说明，请以各技能目录下的 `SKILL.md` 为准。
- 生成脚本：`gen_skills_doc.py`

## 统计

- **总技能数**：{total}
- **分类数**：{cat_count}（{cat_names}）
"""


# ════════════════════════════════════════════════════════
# 主程序
# ════════════════════════════════════════════════════════

def main():
    print(f"读取 CATALOG: {CATALOG}")
    content = CATALOG.read_text(encoding='utf-8')

    catalog = parse_catalog(content)
    total = sum(len(v) for v in catalog.values())
    print(f"解析完毕：{len(catalog)} 个分类，共 {total} 个技能")
    for cat, skills in catalog.items():
        print(f"  {cat}: {len(skills)}")

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    # 1. 各分类文档
    for cat, skills in catalog.items():
        doc = generate_category_doc(cat, skills)
        out_file = OUT_DIR / f"skills_{cat}.md"
        out_file.write_text(doc, encoding='utf-8')
        print(f"  写入 {out_file.name} ({len(skills)} 个技能)")

    # 2. 分类索引
    idx = generate_index(catalog)
    (OUT_DIR / "00_分类索引.md").write_text(idx, encoding='utf-8')
    print("  写入 00_分类索引.md")

    # 3. README
    readme = generate_readme(catalog)
    (OUT_DIR / "README.md").write_text(readme, encoding='utf-8')
    print("  写入 README.md")

    print(f"\n完成！共生成 {len(catalog) + 2} 个文件。")


if __name__ == "__main__":
    main()
