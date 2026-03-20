#!/usr/bin/env python3
"""
Skill 评测工具 v3.0
基于 "Cursor Agent Skills 核心原理与工程推演" PPT 的最佳实践
六维度量化评分 + 自动化检查 + Markdown 报告生成

用法:
    python3 skill_auditor.py <skill-path>
    python3 skill_auditor.py <skill-path> --output report.md
    python3 skill_auditor.py <skill-path> --json
"""

import os
import re
import sys
import json
import yaml
import argparse
from datetime import datetime
from pathlib import Path
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class CheckResult:
    name: str
    passed: bool
    score: float
    max_score: float
    category: str
    detail: str = ""
    severity: str = "info"  # info, warning, error


@dataclass
class DimensionScore:
    name: str
    weight: float
    raw_score: float
    max_score: float
    checks: list = field(default_factory=list)

    @property
    def percentage(self):
        return (self.raw_score / self.max_score * 100) if self.max_score > 0 else 0

    @property
    def weighted_score(self):
        return self.percentage * self.weight / 100


@dataclass
class AuditReport:
    skill_name: str
    skill_path: str
    timestamp: str
    skill_md_lines: int
    dimensions: list = field(default_factory=list)
    bonus_checks: list = field(default_factory=list)

    @property
    def total_weighted(self):
        return sum(d.weighted_score for d in self.dimensions)

    @property
    def grade(self):
        s = self.total_weighted
        if s >= 90:
            return "S"
        elif s >= 80:
            return "A"
        elif s >= 70:
            return "B"
        elif s >= 60:
            return "C"
        elif s >= 50:
            return "D"
        else:
            return "F"

    @property
    def bonus_score(self):
        return sum(c.score for c in self.bonus_checks if c.passed)


class SkillAuditor:
    def __init__(self, skill_path: str):
        self.skill_path = Path(skill_path).resolve()
        self.skill_md_path = self.skill_path / "SKILL.md"
        self.skill_md_content = ""
        self.skill_md_lines = 0
        self.yaml_raw = ""
        self.yaml_data = {}
        self.markdown_body = ""
        self.markdown_body_lines = 0
        self.all_files = []
        self.script_files = []
        self.reference_files = []
        self.asset_files = []

    def load(self):
        if not self.skill_path.is_dir():
            print(f"[ERROR] 路径不存在或不是目录: {self.skill_path}")
            sys.exit(1)

        self.all_files = list(self.skill_path.rglob("*"))

        if self.skill_md_path.exists():
            self.skill_md_content = self.skill_md_path.read_text(encoding="utf-8", errors="replace")
            self.skill_md_lines = len(self.skill_md_content.splitlines())
            self._parse_yaml()
            self._extract_markdown_body()

        scripts_dir = self.skill_path / "scripts"
        if scripts_dir.is_dir():
            self.script_files = [f for f in scripts_dir.rglob("*") if f.is_file()]

        refs_dir = self.skill_path / "references"
        if refs_dir.is_dir():
            self.reference_files = [f for f in refs_dir.rglob("*") if f.is_file()]

        assets_dir = self.skill_path / "assets"
        if assets_dir.is_dir():
            self.asset_files = [f for f in assets_dir.rglob("*") if f.is_file()]

    def _parse_yaml(self):
        match = re.match(r"^---\s*\n(.*?)\n---", self.skill_md_content, re.DOTALL)
        if match:
            self.yaml_raw = match.group(1)
            try:
                self.yaml_data = yaml.safe_load(self.yaml_raw) or {}
            except yaml.YAMLError:
                self.yaml_data = {}

    def _extract_markdown_body(self):
        match = re.match(r"^---\s*\n.*?\n---\s*\n?", self.skill_md_content, re.DOTALL)
        if match:
            self.markdown_body = self.skill_md_content[match.end():]
        else:
            self.markdown_body = self.skill_md_content
        self.markdown_body_lines = len(self.markdown_body.splitlines())

    def _count_words(self, text: str) -> int:
        """统计中英文混合词数：英文按空格分词，中文按字符计数"""
        en_words = len(re.findall(r'[a-zA-Z]+', text))
        zh_chars = len(re.findall(r'[\u4e00-\u9fff]', text))
        return en_words + zh_chars

    def audit(self) -> AuditReport:
        self.load()
        report = AuditReport(
            skill_name=self.yaml_data.get("name", self.skill_path.name),
            skill_path=str(self.skill_path),
            timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            skill_md_lines=self.skill_md_lines,
        )

        report.dimensions = [
            self._check_context_efficiency(),
            self._check_structure_compliance(),
            self._check_description_seo(),
            self._check_content_quality(),
            self._check_security_sandbox(),
            self._check_maintainability(),
        ]
        report.bonus_checks = self._check_best_practices()
        return report

    # ─── 维度一：上下文效率（25%）───
    # PPT 核心原则：精简第一，上下文窗口是极度稀缺的公共资源

    def _check_context_efficiency(self) -> DimensionScore:
        checks = []

        # PPT P3: 只添加 Agent 绝对不知道的信息
        yaml_word_count = self._count_words(self.yaml_raw) if self.yaml_raw else 0
        yaml_under_100 = yaml_word_count <= 100
        checks.append(CheckResult(
            "YAML Frontmatter ≤ 100 词", yaml_under_100,
            4 if yaml_under_100 else (2 if yaml_word_count <= 150 else 0), 4,
            "上下文效率",
            f"当前 {yaml_word_count} 词（PPT P4: 第1级元数据约100词）"
        ))

        # PPT P4: SKILL.md 正文 < 5000 词
        body_word_count = self._count_words(self.markdown_body)
        body_under_5000 = body_word_count < 5000
        checks.append(CheckResult(
            "Markdown 正文 < 5000 词", body_under_5000,
            3 if body_under_5000 else 0, 3,
            "上下文效率",
            f"当前 {body_word_count} 词（PPT P4: 第2级正文<5000词）"
        ))

        # PPT P7/P9: 500 行红线
        body_under_500 = self.markdown_body_lines <= 500
        if self.markdown_body_lines <= 300:
            line_score = 5
        elif self.markdown_body_lines <= 500:
            line_score = 3
        elif self.markdown_body_lines <= 700:
            line_score = 1
        else:
            line_score = 0
        checks.append(CheckResult(
            "正文行数控制（黄金法则 ≤ 500 行）", body_under_500,
            line_score, 5,
            "上下文效率",
            f"当前 {self.markdown_body_lines} 行（PPT P7: 将正文严格控制在500行以内）",
            severity="warning" if self.markdown_body_lines > 500 else "info"
        ))

        # PPT P9: 代码示例沟通效率 > 文字
        code_blocks = re.findall(r'```[\s\S]*?```', self.markdown_body)
        code_lines = sum(len(block.splitlines()) for block in code_blocks)
        total_body_lines = max(self.markdown_body_lines, 1)
        code_ratio = code_lines / total_body_lines if total_body_lines > 0 else 0

        good_code_ratio = code_ratio >= 0.15
        checks.append(CheckResult(
            "代码示例占比 ≥ 15%", good_code_ratio,
            3 if good_code_ratio else (1 if code_ratio >= 0.05 else 0), 3,
            "上下文效率",
            f"代码比例: {code_ratio:.1%}（PPT P9: 代码示例沟通效率远高于冗长文字解释）"
        ))

        # PPT P3: 不含通用编程常识
        generic_patterns = [
            r'(?:how to|如何)\s+(?:create|write|make)\s+(?:a )?\s*(?:loop|function|class|variable)',
            r'(?:what is|什么是)\s+(?:a )?\s*(?:loop|function|class|variable|array|list)',
            r'for\s+i\s+in\s+range',
        ]
        has_generic = any(re.search(p, self.markdown_body, re.IGNORECASE) for p in generic_patterns)
        checks.append(CheckResult(
            "不含通用编程常识", not has_generic,
            2 if not has_generic else 0, 2,
            "上下文效率",
            "PPT P3: 不要教 Agent 如何写基本的 Python 循环"
        ))

        raw = sum(c.score for c in checks)
        max_s = sum(c.max_score for c in checks)
        return DimensionScore("上下文效率", 25, max(0, raw), max_s, checks)

    # ─── 维度二：结构合规性（20%）───
    # PPT P4-P6: 三级渐进式加载 + 文件解剖学

    def _check_structure_compliance(self) -> DimensionScore:
        checks = []

        # PPT P5: SKILL.md 存在（必需）
        checks.append(CheckResult(
            "SKILL.md 存在", self.skill_md_path.exists(),
            4 if self.skill_md_path.exists() else 0, 4,
            "结构合规性",
            "PPT P5: 必需的主文件"
        ))

        # PPT P5/P7: YAML Frontmatter 存在
        has_yaml = bool(self.yaml_data)
        checks.append(CheckResult(
            "YAML Frontmatter 存在", has_yaml,
            3 if has_yaml else 0, 3,
            "结构合规性",
            "PPT P7: YAML Frontmatter（触发器）占 15%"
        ))

        has_name = "name" in self.yaml_data
        checks.append(CheckResult(
            "name 字段存在", has_name,
            2 if has_name else 0, 2,
            "结构合规性",
            "PPT P7: 包含 Skill 标识符"
        ))

        has_desc = "description" in self.yaml_data
        checks.append(CheckResult(
            "description 字段存在", has_desc,
            2 if has_desc else 0, 2,
            "结构合规性",
            "PPT P7: 包含触发条件和功能描述"
        ))

        # PPT P5: 标准目录结构 (scripts/, references/, assets/)
        has_scripts_dir = (self.skill_path / "scripts").is_dir()
        has_refs_dir = (self.skill_path / "references").is_dir()
        has_assets_dir = (self.skill_path / "assets").is_dir()
        bundled_count = sum([has_scripts_dir, has_refs_dir, has_assets_dir])

        checks.append(CheckResult(
            "使用标准捆绑资源目录", bundled_count >= 1,
            min(bundled_count, 3), 3,
            "结构合规性",
            f"检测到: {', '.join(filter(None, ['scripts/' if has_scripts_dir else '', 'references/' if has_refs_dir else '', 'assets/' if has_assets_dir else '']))}（PPT P5: scripts/ + references/ + assets/）"
        ))

        # PPT P11: 超过 500 行时使用 references/ 分离
        if self.markdown_body_lines > 500:
            uses_refs = bool(self.reference_files)
            checks.append(CheckResult(
                "超 500 行时使用 references/ 分离", uses_refs,
                3 if uses_refs else 0, 3,
                "结构合规性",
                f"正文 {self.markdown_body_lines} 行，{'已' if uses_refs else '未'}使用 references/ 分离（PPT P11: 渐进式内容分离架构）",
                severity="warning" if not uses_refs else "info"
            ))
        else:
            checks.append(CheckResult(
                "正文在 500 行内无需强制分离", True,
                3, 3,
                "结构合规性",
                f"正文 {self.markdown_body_lines} 行，无需分离"
            ))

        # PPT P11: references 文件有 TOC（超100行时）
        long_refs_without_toc = 0
        for rf in self.reference_files:
            if rf.suffix in ('.md', '.txt'):
                try:
                    ref_content = rf.read_text(encoding="utf-8", errors="replace")
                    ref_lines = len(ref_content.splitlines())
                    if ref_lines > 100:
                        toc_markers = ["table of contents", "目录", "## 目录", "## toc"]
                        if not any(m in ref_content.lower() for m in toc_markers):
                            long_refs_without_toc += 1
                except Exception:
                    pass

        refs_have_toc = long_refs_without_toc == 0
        checks.append(CheckResult(
            ">100 行参考文件有目录", refs_have_toc,
            2 if refs_have_toc else 0, 2,
            "结构合规性",
            f"{long_refs_without_toc} 个参考文件缺少目录（PPT P11: 超过100行必须添加目录）" if not refs_have_toc else "合规"
        ))

        # 目录名规范
        dir_name = self.skill_path.name
        name_val = self.yaml_data.get("name", "")
        name_valid = bool(re.match(r'^[a-z0-9][a-z0-9\-]*$', name_val)) if name_val else True
        checks.append(CheckResult(
            "name 使用小写+连字符", name_valid,
            2 if name_valid else 0, 2,
            "结构合规性",
            f"name: {name_val or '(未设置)'}"
        ))

        raw = sum(c.score for c in checks)
        max_s = sum(c.max_score for c in checks)
        return DimensionScore("结构合规性", 20, max(0, raw), max_s, checks)

    # ─── 维度三：Description SEO 质量（15%）───
    # PPT P8: Description 是决定 Skill 是否被唤醒的 SEO 搜索引擎

    def _check_description_seo(self) -> DimensionScore:
        checks = []
        desc = self.yaml_data.get("description", "")
        desc_lower = desc.lower()

        # PPT P8: 必须声明"做什么"
        action_keywords = ["use this", "用于", "create", "生成", "处理", "manage", "帮助",
                          "analyze", "分析", "build", "构建", "convert", "转换", "handle"]
        has_what = any(kw in desc_lower for kw in action_keywords)
        checks.append(CheckResult(
            "Description 声明做什么", has_what,
            3 if has_what else 0, 3,
            "Description SEO",
            "PPT P8: 必须明确声明'做什么'"
        ))

        # PPT P8: 必须声明"什么时候用"
        trigger_keywords = ["use when", "when", "trigger", "触发", "whenever", "use this",
                           "当", "如果", "需要时"]
        has_when = any(kw in desc_lower for kw in trigger_keywords)
        checks.append(CheckResult(
            "Description 声明什么时候用", has_when,
            3 if has_when else 0, 3,
            "Description SEO",
            "PPT P8: 必须明确声明'什么时候用'"
        ))

        # PPT P8: 穷举同义词
        desc_words = set(re.findall(r'\b\w+\b', desc_lower))
        synonym_groups_found = 0
        synonym_groups = [
            {"word", "doc", "document", "docx", "文档"},
            {"pdf", "portable document"},
            {"image", "picture", "photo", "图片", "图像"},
            {"test", "testing", "测试", "spec"},
            {"deploy", "deployment", "部署", "发布"},
            {"code", "coding", "编码", "代码"},
            {"api", "endpoint", "接口"},
        ]
        for group in synonym_groups:
            found = desc_words & group
            if len(found) >= 2:
                synonym_groups_found += 1

        has_synonyms = synonym_groups_found >= 1 or len(desc) > 100
        checks.append(CheckResult(
            "Description 覆盖同义词", has_synonyms,
            3 if has_synonyms else (1 if len(desc) > 80 else 0), 3,
            "Description SEO",
            f"同义词组匹配: {synonym_groups_found}（PPT P8: 穷举用户可能使用的所有同义词）"
        ))

        # PPT P8: 负面条件排除
        exclude_keywords = ["do not", "don't", "不要", "不适用", "except", "exclude",
                           "not for", "不用于", "avoid", "skip"]
        has_exclude = any(kw in desc_lower for kw in exclude_keywords)
        checks.append(CheckResult(
            "Description 包含排除条件", has_exclude,
            3 if has_exclude else 0, 3,
            "Description SEO",
            "PPT P8: 明确的排除条件能极大降低相似Skill共存时的误触发率"
        ))

        # Description 长度合理
        desc_len = len(desc)
        if desc_len >= 80:
            len_score = 3
        elif desc_len >= 50:
            len_score = 2
        elif desc_len > 0:
            len_score = 1
        else:
            len_score = 0
        checks.append(CheckResult(
            "Description 长度充足（≥80字符）", desc_len >= 80,
            len_score, 3,
            "Description SEO",
            f"当前长度: {desc_len} 字符"
        ))

        raw = sum(c.score for c in checks)
        max_s = sum(c.max_score for c in checks)
        return DimensionScore("Description SEO", 15, max(0, raw), max_s, checks)

    # ─── 维度四：内容质量（20%）───
    # PPT P9-P13: 代码优先、自由度设定、排版心理学、结构化导航

    def _check_content_quality(self) -> DimensionScore:
        checks = []
        content = self.skill_md_content
        content_lower = content.lower()
        body = self.markdown_body
        body_lower = body.lower()

        # PPT P9: 包含可执行代码示例
        code_blocks = re.findall(r'```(?:bash|python|sh|javascript|typescript|go|rust|java)', body_lower)
        has_exec_code = len(code_blocks) > 0
        checks.append(CheckResult(
            "包含可执行代码示例", has_exec_code,
            3 if has_exec_code else 0, 3,
            "内容质量",
            f"找到 {len(code_blocks)} 个代码块（PPT P9: 代码示例沟通效率远高于冗长文字解释）"
        ))

        # PPT P12: CRITICAL 标签节制使用（5-8个以内）
        critical_count = len(re.findall(r'(?://\s*)?CRITICAL', content, re.IGNORECASE))
        critical_ok = critical_count <= 8
        checks.append(CheckResult(
            "CRITICAL 标签 ≤ 8 个", critical_ok,
            2 if critical_ok else 0, 2,
            "内容质量",
            f"当前 {critical_count} 个（PPT P12: 整个Skill最多允许5-8个，滥用导致注意力衰减）",
            severity="warning" if not critical_ok else "info"
        ))

        # PPT P12: 使用编号步骤（非 bullet 字符）
        numbered_steps = re.findall(r'^\s*\d+[\.\)]\s+', body, re.MULTILINE)
        has_numbered = len(numbered_steps) >= 2
        checks.append(CheckResult(
            "使用编号步骤", has_numbered,
            2 if has_numbered else 0, 2,
            "内容质量",
            f"找到 {len(numbered_steps)} 个编号步骤（PPT P12: 多步骤流程必须使用明确编号）"
        ))

        # PPT P12: 正反对比示例
        has_contrast = (
            ("❌" in content and "✅" in content) or
            ("WRONG" in content and "CORRECT" in content) or
            ("bad" in body_lower and "good" in body_lower) or
            ("错误" in body and "正确" in body)
        )
        checks.append(CheckResult(
            "包含正反对比示例", has_contrast,
            2 if has_contrast else 0, 2,
            "内容质量",
            "PPT P12: 必须同时展示典型坏代码与正确的标准答案"
        ))

        # PPT P13: Quick Reference 映射表
        table_rows = re.findall(r'^\|.+\|.+\|', body, re.MULTILINE)
        has_qr_table = len(table_rows) >= 3
        checks.append(CheckResult(
            "包含 Quick Reference 映射表", has_qr_table,
            3 if has_qr_table else (1 if len(table_rows) >= 1 else 0), 3,
            "内容质量",
            f"找到 {len(table_rows)} 行表格（PPT P13: Agent能在3秒内找到正确工具路径）"
        ))

        # PPT P13: ASCII 决策树
        tree_chars = ["├", "│", "└", "→", "├──", "└──"]
        tree_count = sum(1 for c in tree_chars if c in body)
        has_tree = tree_count >= 2
        checks.append(CheckResult(
            "包含 ASCII 决策树/目录树", has_tree,
            2 if has_tree else 0, 2,
            "内容质量",
            f"PPT P13: 决策树比文字段落节省约60%的Token"
        ))

        # PPT P10: 操作自由度标注
        constraint_keywords = ["must", "必须", "always", "never", "禁止", "strictly", "严格"]
        guide_keywords = ["recommend", "建议", "prefer", "可以", "suggest", "consider"]
        has_constraints = any(kw in body_lower for kw in constraint_keywords)
        has_guides = any(kw in body_lower for kw in guide_keywords)
        freedom_score = (1 if has_constraints else 0) + (1 if has_guides else 0)
        checks.append(CheckResult(
            "明确操作自由度", freedom_score >= 1,
            freedom_score, 2,
            "内容质量",
            f"{'有' if has_constraints else '无'}约束指令, {'有' if has_guides else '无'}灵活指导（PPT P10: 根据任务脆弱程度设定自由度）"
        ))

        # 文档结构清晰
        headings = re.findall(r'^#{1,3}\s+.+', body, re.MULTILINE)
        good_structure = len(headings) >= 3
        checks.append(CheckResult(
            "文档结构清晰（≥3 个章节）", good_structure,
            2 if good_structure else 0, 2,
            "内容质量",
            f"找到 {len(headings)} 个章节标题"
        ))

        raw = sum(c.score for c in checks)
        max_s = sum(c.max_score for c in checks)
        return DimensionScore("内容质量", 20, max(0, raw), max_s, checks)

    # ─── 维度五：安全与沙箱（10%）───
    # PPT P14: 将外部脚本作为受保护的执行黑盒与安全沙箱

    def _check_security_sandbox(self) -> DimensionScore:
        checks = []
        all_content = self.skill_md_content

        for sf in self.script_files:
            try:
                all_content += "\n" + sf.read_text(encoding="utf-8", errors="replace")
            except Exception:
                pass

        # 硬编码敏感信息检测
        secret_patterns = [
            r'(?:api[_-]?key|apikey)\s*[=:]\s*["\'][^"\']{10,}',
            r'(?:password|passwd|pwd)\s*[=:]\s*["\'][^"\']+',
            r'(?:secret|token)\s*[=:]\s*["\'][^"\']{10,}',
            r'(?:sk-|pk-)[a-zA-Z0-9]{20,}',
        ]
        has_secrets = any(re.search(p, all_content, re.IGNORECASE) for p in secret_patterns)
        checks.append(CheckResult(
            "未检测到硬编码敏感信息", not has_secrets,
            3 if not has_secrets else 0, 3,
            "安全与沙箱",
            severity="error" if has_secrets else "info"
        ))

        # PPT P14: 脚本使用 --help 接口
        has_help_interface = False
        for sf in self.script_files:
            try:
                script_content = sf.read_text(encoding="utf-8", errors="replace")
                if "--help" in script_content or "argparse" in script_content or "parser.add" in script_content:
                    has_help_interface = True
                    break
            except Exception:
                pass
        if not self.script_files:
            has_help_interface = True  # 无脚本时不扣分

        checks.append(CheckResult(
            "脚本提供 --help 接口", has_help_interface,
            2 if has_help_interface else 0, 2,
            "安全与沙箱",
            "PPT P14: 总是先运行--help。100行代码占300Token，而--help输出不到50Token"
        ))

        # PPT P14: 资源清理机制
        cleanup_patterns = [
            r'finally\s*:', r'process\.terminate', r'process\.kill',
            r'cleanup', r'atexit', r'signal\.signal',
            r'try\s*:.*?finally', r'with\s+',
        ]
        has_cleanup = any(re.search(p, all_content, re.IGNORECASE) for p in cleanup_patterns)
        if not self.script_files:
            has_cleanup = True

        checks.append(CheckResult(
            "脚本有资源清理机制", has_cleanup,
            2 if has_cleanup else 0, 2,
            "安全与沙箱",
            "PPT P14: 使用finally块，先process.terminate()再process.kill()"
        ))

        # PPT P14: Auto-repair 能力边界标注
        repair_keywords = ["auto-repair", "自动修复", "retry", "重试", "fallback", "降级"]
        has_repair_note = any(kw in all_content.lower() for kw in repair_keywords)
        checks.append(CheckResult(
            "标注自动修复能力边界", has_repair_note or not self.script_files,
            1 if (has_repair_note or not self.script_files) else 0, 1,
            "安全与沙箱",
            "PPT P14: 划定Agent自动修复能力边界，防止盲目重试"
        ))

        # 危险函数检测
        danger_patterns = [
            r'\beval\s*\(', r'\bexec\s*\(', r'os\.system\s*\(',
            r'__import__\s*\(',
        ]
        has_danger = any(re.search(p, all_content) for p in danger_patterns)
        checks.append(CheckResult(
            "未检测到危险函数调用", not has_danger,
            2 if not has_danger else 0, 2,
            "安全与沙箱",
            severity="error" if has_danger else "info"
        ))

        raw = sum(c.score for c in checks)
        max_s = sum(c.max_score for c in checks)
        return DimensionScore("安全与沙箱", 10, max(0, raw), max_s, checks)

    # ─── 维度六：可维护性（10%）───

    def _check_maintainability(self) -> DimensionScore:
        checks = []

        # 脚本注释率
        total_lines = 0
        comment_lines = 0
        for sf in self.script_files:
            try:
                lines = sf.read_text(encoding="utf-8", errors="replace").splitlines()
                total_lines += len(lines)
                for line in lines:
                    stripped = line.strip()
                    if stripped.startswith("#") or stripped.startswith("//") or stripped.startswith("/*"):
                        comment_lines += 1
            except Exception:
                pass

        if total_lines > 0:
            ratio = comment_lines / total_lines
            good_comments = ratio >= 0.10
        else:
            good_comments = True
            ratio = 0

        checks.append(CheckResult(
            "脚本有适当注释（>10%）", good_comments,
            2 if good_comments else 0, 2,
            "可维护性",
            f"注释比例: {ratio:.1%} ({comment_lines}/{total_lines})"
        ))

        # PPT P11: 无信息重复
        body_lines = self.markdown_body.splitlines()
        seen_lines = set()
        duplicate_lines = 0
        for line in body_lines:
            stripped = line.strip()
            if len(stripped) > 30:
                if stripped in seen_lines:
                    duplicate_lines += 1
                seen_lines.add(stripped)

        no_duplicates = duplicate_lines <= 2
        checks.append(CheckResult(
            "无明显内容重复", no_duplicates,
            2 if no_duplicates else 0, 2,
            "可维护性",
            f"发现 {duplicate_lines} 行重复内容（PPT P11: 绝对禁止信息重复）",
            severity="warning" if not no_duplicates else "info"
        ))

        # 版本/日期信息
        version_keywords = ["version", "更新", "v1", "v2", "v3", "日期", "date", "changelog"]
        has_version = any(kw in self.skill_md_content.lower() for kw in version_keywords)
        checks.append(CheckResult(
            "有版本/更新说明", has_version,
            2 if has_version else 0, 2,
            "可维护性"
        ))

        # 依赖说明
        dep_keywords = ["dependency", "依赖", "require", "prerequisite", "install", "pip install", "npm install"]
        has_dep = any(kw in self.skill_md_content.lower() for kw in dep_keywords)
        checks.append(CheckResult(
            "有依赖说明", has_dep,
            2 if has_dep else 0, 2,
            "可维护性"
        ))

        # 错误处理说明
        error_keywords = ["error", "异常", "失败", "fail", "exception", "troubleshoot", "排错"]
        has_error = any(kw in self.skill_md_content.lower() for kw in error_keywords)
        checks.append(CheckResult(
            "有错误处理说明", has_error,
            2 if has_error else 0, 2,
            "可维护性"
        ))

        raw = sum(c.score for c in checks)
        max_s = sum(c.max_score for c in checks)
        return DimensionScore("可维护性", 10, max(0, raw), max_s, checks)

    # ─── 最佳实践（加分项）───
    # 来自 PPT 全文总结的高级技巧

    def _check_best_practices(self) -> list:
        checks = []
        content = self.skill_md_content
        body = self.markdown_body

        # PPT P14: 脚本不被读入上下文（通过 --help 接口）
        help_in_skill = "--help" in content
        checks.append(CheckResult(
            "SKILL.md 引导使用 --help", help_in_skill,
            2, 2, "最佳实践",
            "PPT P14: 强制隔离源码，总是先运行--help"
        ))

        # PPT P11: 按领域平行组织子文件
        ref_count = len(self.reference_files)
        checks.append(CheckResult(
            "参考文件 ≥ 2（按领域平行组织）", ref_count >= 2,
            2, 2, "最佳实践",
            f"当前 {ref_count} 个参考文件（PPT P11: 按领域平行组织）"
        ))

        # PPT P7: YAML 占比约 15%
        yaml_lines = len(self.yaml_raw.splitlines()) if self.yaml_raw else 0
        total = max(self.skill_md_lines, 1)
        yaml_ratio = yaml_lines / total
        yaml_ratio_ok = 0.05 <= yaml_ratio <= 0.30
        checks.append(CheckResult(
            "YAML 占比在 5%-30% 范围内", yaml_ratio_ok,
            1, 1, "最佳实践",
            f"YAML 占比: {yaml_ratio:.1%}（PPT P7: YAML占约15%）"
        ))

        # PPT P6: scripts/ 中脚本可直接执行
        executable_scripts = 0
        for sf in self.script_files:
            if sf.suffix in ('.py', '.sh', '.bash', '.js', '.ts'):
                executable_scripts += 1
        checks.append(CheckResult(
            "scripts/ 含可执行脚本", executable_scripts >= 1 or not self.script_files,
            1, 1, "最佳实践",
            f"找到 {executable_scripts} 个可执行脚本"
        ))

        # PPT P13: 使用 Markdown 表格做 Quick Reference
        table_pattern = r'\|.+\|.+\|\s*\n\|[-:\s|]+\|\s*\n'
        has_proper_table = bool(re.search(table_pattern, body))
        checks.append(CheckResult(
            "使用标准 Markdown 表格", has_proper_table,
            1, 1, "最佳实践"
        ))

        return checks


def generate_markdown_report(report: AuditReport) -> str:
    lines = []
    lines.append("=" * 60)
    lines.append("# Skill 评测报告 v3.0")
    lines.append("=" * 60)
    lines.append("")

    lines.append("## 基本信息")
    lines.append(f"- **Skill 名称**: {report.skill_name}")
    lines.append(f"- **Skill 路径**: {report.skill_path}")
    lines.append(f"- **评测时间**: {report.timestamp}")
    lines.append(f"- **SKILL.md 行数**: {report.skill_md_lines}")
    lines.append("")

    grade_emoji = {"S": "🏆", "A": "⭐", "B": "👍", "C": "📋", "D": "⚠️", "F": "❌"}
    lines.append("## 总体评分")
    lines.append(f"- **加权总分**: {report.total_weighted:.1f} / 100")
    lines.append(f"- **评级**: {grade_emoji.get(report.grade, '')} {report.grade}")
    if report.bonus_score > 0:
        lines.append(f"- **最佳实践加分**: +{report.bonus_score}")
    lines.append("")

    lines.append("## 分维度评分")
    lines.append("")
    lines.append("| 维度 | 权重 | 得分 | 满分 | 百分比 | 加权分 |")
    lines.append("|------|------|------|------|--------|--------|")
    for d in report.dimensions:
        bar = "█" * int(d.percentage / 10) + "░" * (10 - int(d.percentage / 10))
        lines.append(
            f"| {d.name} | {d.weight}% | {d.raw_score:.0f} | {d.max_score:.0f} | "
            f"{bar} {d.percentage:.0f}% | {d.weighted_score:.1f} |"
        )
    lines.append("")

    lines.append("## 评测维度说明")
    lines.append("")
    lines.append("本工具基于 **\"Cursor Agent Skills 核心原理与工程推演\"** PPT 的最佳实践进行评测：")
    lines.append("")
    lines.append("| 维度 | 权重 | 核心原则 |")
    lines.append("|------|------|----------|")
    lines.append("| 上下文效率 | 25% | 精简第一，上下文窗口是极度稀缺的公共资源 |")
    lines.append("| 结构合规性 | 20% | 三级渐进式加载 + 标准文件解剖学结构 |")
    lines.append("| Description SEO | 15% | Description 是决定 Skill 是否被唤醒的 SEO 搜索引擎 |")
    lines.append("| 内容质量 | 20% | 代码优先、排版心理学、结构化导航 |")
    lines.append("| 安全与沙箱 | 10% | 将外部脚本作为受保护的执行黑盒与安全沙箱 |")
    lines.append("| 可维护性 | 10% | 无信息重复、版本管理、依赖说明 |")
    lines.append("")

    lines.append("## 自动化检查结果")
    lines.append("")

    for d in report.dimensions:
        lines.append(f"### {d.name}（权重 {d.weight}%）")
        lines.append("")
        passed = [c for c in d.checks if c.passed]
        failed = [c for c in d.checks if not c.passed and c.max_score > 0]
        warnings = [c for c in d.checks if c.severity == "warning"]

        if passed:
            lines.append("**通过项:**")
            for c in passed:
                detail = f" — {c.detail}" if c.detail else ""
                lines.append(f"- ✅ {c.name} (+{c.score:.0f}){detail}")
            lines.append("")

        if failed:
            lines.append("**失败项:**")
            for c in failed:
                detail = f" — {c.detail}" if c.detail else ""
                lines.append(f"- ❌ {c.name} (0/{c.max_score:.0f}){detail}")
            lines.append("")

        if warnings:
            lines.append("**警告项:**")
            for c in warnings:
                detail = f" — {c.detail}" if c.detail else ""
                lines.append(f"- ⚠️ {c.name}{detail}")
            lines.append("")

    if report.bonus_checks:
        lines.append("### 最佳实践（加分项）")
        lines.append("")
        for c in report.bonus_checks:
            icon = "✅" if c.passed else "⬜"
            detail = f" — {c.detail}" if c.detail else ""
            lines.append(f"- {icon} {c.name} (+{c.score if c.passed else 0}/{c.max_score}){detail}")
        lines.append("")

    lines.append("## 改进建议")
    lines.append("")
    suggestions = []
    for d in report.dimensions:
        for c in d.checks:
            if not c.passed and c.max_score > 0:
                suggestions.append((d.name, c))

    if suggestions:
        current_dim = ""
        for dim_name, c in suggestions:
            if dim_name != current_dim:
                lines.append(f"### {dim_name}")
                current_dim = dim_name
            lines.append(f"- {c.name}: {c.detail or '建议补充此项'}")
        lines.append("")
    else:
        lines.append("所有检查项均已通过，无需改进。")
        lines.append("")

    lines.append("---")
    lines.append(f"*报告生成时间: {report.timestamp} | Skill Auditor v3.0 — 基于 \"Cursor Agent Skills 核心原理与工程推演\" PPT*")

    return "\n".join(lines)


def generate_json_report(report: AuditReport) -> dict:
    return {
        "skill_name": report.skill_name,
        "skill_path": report.skill_path,
        "timestamp": report.timestamp,
        "skill_md_lines": report.skill_md_lines,
        "total_weighted": round(report.total_weighted, 1),
        "grade": report.grade,
        "bonus_score": report.bonus_score,
        "dimensions": [
            {
                "name": d.name,
                "weight": d.weight,
                "raw_score": d.raw_score,
                "max_score": d.max_score,
                "percentage": round(d.percentage, 1),
                "weighted_score": round(d.weighted_score, 1),
                "checks": [
                    {
                        "name": c.name,
                        "passed": c.passed,
                        "score": c.score,
                        "max_score": c.max_score,
                        "detail": c.detail,
                    }
                    for c in d.checks
                ],
            }
            for d in report.dimensions
        ],
        "bonus_checks": [
            {"name": c.name, "passed": c.passed, "score": c.score, "detail": c.detail}
            for c in report.bonus_checks
        ],
    }


def print_console_summary(report: AuditReport):
    grade_color = {
        "S": "\033[1;35m", "A": "\033[1;32m", "B": "\033[1;36m",
        "C": "\033[1;33m", "D": "\033[1;31m", "F": "\033[1;31m"
    }
    reset = "\033[0m"
    bold = "\033[1m"

    print(f"\n{bold}{'=' * 55}{reset}")
    print(f"{bold}  Skill Auditor v3.0 — 基于 PPT 最佳实践{reset}")
    print(f"{bold}  评测结果: {report.skill_name}{reset}")
    print(f"{'=' * 55}")
    print(f"  路径: {report.skill_path}")
    print(f"  SKILL.md: {report.skill_md_lines} 行")
    print()

    gc = grade_color.get(report.grade, "")
    print(f"  {bold}总分: {gc}{report.total_weighted:.1f}/100 [{report.grade}]{reset}")
    if report.bonus_score > 0:
        print(f"  最佳实践加分: +{report.bonus_score}")
    print()

    for d in report.dimensions:
        bar_filled = int(d.percentage / 5)
        bar = "█" * bar_filled + "░" * (20 - bar_filled)
        color = "\033[32m" if d.percentage >= 70 else "\033[33m" if d.percentage >= 50 else "\033[31m"
        print(f"  {d.name:12s} [{color}{bar}{reset}] {d.percentage:5.1f}% (权重{d.weight}% → {d.weighted_score:.1f})")

    print()

    total_passed = sum(1 for d in report.dimensions for c in d.checks if c.passed)
    total_failed = sum(1 for d in report.dimensions for c in d.checks if not c.passed and c.max_score > 0)
    print(f"  检查项: ✅ {total_passed} 通过  ❌ {total_failed} 失败")

    failed = [(d.name, c) for d in report.dimensions for c in d.checks if not c.passed and c.max_score > 0]
    if failed:
        print(f"\n  {bold}需改进:{reset}")
        for dim, c in failed[:8]:
            print(f"    [{dim}] {c.name}")
            if c.detail:
                print(f"           {c.detail}")
        if len(failed) > 8:
            print(f"    ... 还有 {len(failed) - 8} 项")

    print(f"\n{'=' * 55}\n")


def main():
    parser = argparse.ArgumentParser(description="Skill 评测工具 v3.0 — 基于 \"Cursor Agent Skills 核心原理与工程推演\" PPT")
    parser.add_argument("skill_path", help="Skill 目录路径")
    parser.add_argument("--output", "-o", help="输出 Markdown 报告路径")
    parser.add_argument("--json", action="store_true", help="输出 JSON 格式")
    parser.add_argument("--quiet", "-q", action="store_true", help="安静模式，只输出报告")
    args = parser.parse_args()

    auditor = SkillAuditor(args.skill_path)
    report = auditor.audit()

    if not args.quiet:
        print_console_summary(report)

    if args.json:
        print(json.dumps(generate_json_report(report), ensure_ascii=False, indent=2))
    else:
        md_report = generate_markdown_report(report)

        output_path = args.output or os.path.join(args.skill_path, "AUDIT_REPORT.md")
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(md_report)

        if not args.quiet:
            print(f"  报告已保存: {output_path}")


if __name__ == "__main__":
    main()
