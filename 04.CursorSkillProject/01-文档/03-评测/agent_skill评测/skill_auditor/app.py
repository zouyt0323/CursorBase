#!/usr/bin/env python3
"""
Skill 评测工具 Web UI v3.0
Flask 应用 — 六维度评分（基于PPT最佳实践）+ 雷达图 + 历史记录 + 对比模式
"""

import os
import json
import time
from pathlib import Path
from flask import Flask, render_template_string, request, jsonify, send_file
from skill_auditor import SkillAuditor, generate_markdown_report, generate_json_report

app = Flask(__name__)

HISTORY_FILE = Path(__file__).parent / "audit_history.json"


def load_history():
    if HISTORY_FILE.exists():
        return json.loads(HISTORY_FILE.read_text(encoding="utf-8"))
    return []


def save_history(history):
    HISTORY_FILE.write_text(json.dumps(history, ensure_ascii=False, indent=2), encoding="utf-8")


HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Skill 评测工具 v3.0 — 基于 PPT 最佳实践</title>
<script src="https://cdn.jsdelivr.net/npm/chart.js@4"></script>
<style>
:root {
    --bg: #0f172a; --surface: #1e293b; --surface2: #334155;
    --text: #e2e8f0; --text2: #94a3b8; --accent: #3b82f6;
    --green: #22c55e; --yellow: #eab308; --red: #ef4444;
    --purple: #a855f7; --radius: 12px;
}
* { margin: 0; padding: 0; box-sizing: border-box; }
body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
       background: var(--bg); color: var(--text); min-height: 100vh; }
.container { max-width: 1200px; margin: 0 auto; padding: 20px; }
h1 { text-align: center; font-size: 1.8rem; margin: 20px 0; color: var(--accent); }
.subtitle { text-align: center; color: var(--text2); margin-bottom: 30px; }

/* Nav tabs */
.tabs { display: flex; gap: 4px; margin-bottom: 24px; background: var(--surface);
        border-radius: var(--radius); padding: 4px; }
.tab { flex: 1; padding: 10px; text-align: center; border-radius: 8px;
       cursor: pointer; transition: all .2s; color: var(--text2); border: none;
       background: transparent; font-size: .95rem; }
.tab.active { background: var(--accent); color: white; }
.tab:hover:not(.active) { background: var(--surface2); }
.tab-content { display: none; } .tab-content.active { display: block; }

/* Input */
.input-group { display: flex; gap: 12px; margin-bottom: 24px; }
.input-group input { flex: 1; padding: 12px 16px; border-radius: var(--radius);
    border: 1px solid var(--surface2); background: var(--surface); color: var(--text);
    font-size: 1rem; outline: none; }
.input-group input:focus { border-color: var(--accent); }
.btn { padding: 12px 24px; border-radius: var(--radius); border: none;
       background: var(--accent); color: white; font-size: 1rem; cursor: pointer;
       transition: all .2s; font-weight: 600; }
.btn:hover { opacity: .9; transform: translateY(-1px); }
.btn:disabled { opacity: .5; cursor: not-allowed; }
.btn-sm { padding: 6px 14px; font-size: .85rem; }
.btn-outline { background: transparent; border: 1px solid var(--accent); color: var(--accent); }

/* Score ring */
.score-ring-container { display: flex; justify-content: center; margin: 20px 0; }
.score-ring { position: relative; width: 180px; height: 180px; }
.score-ring svg { transform: rotate(-90deg); }
.score-ring .value { position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);
    text-align: center; }
.score-ring .value .num { font-size: 2.5rem; font-weight: 700; }
.score-ring .value .grade { font-size: 1.2rem; color: var(--text2); }

/* Cards */
.card { background: var(--surface); border-radius: var(--radius); padding: 20px;
        margin-bottom: 16px; }
.card-title { font-size: 1.1rem; font-weight: 600; margin-bottom: 12px; }
.grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }
.grid-3 { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 16px; }
@media (max-width: 768px) { .grid-2, .grid-3 { grid-template-columns: 1fr; } }

/* Progress bars */
.dim-bar { margin-bottom: 12px; }
.dim-bar .label { display: flex; justify-content: space-between; margin-bottom: 4px;
    font-size: .9rem; }
.dim-bar .bar { height: 8px; background: var(--surface2); border-radius: 4px; overflow: hidden; }
.dim-bar .fill { height: 100%; border-radius: 4px; transition: width .8s ease; }

/* Check items */
.check-list { list-style: none; }
.check-item { padding: 8px 0; border-bottom: 1px solid var(--surface2); display: flex;
    align-items: center; gap: 8px; font-size: .9rem; }
.check-item:last-child { border-bottom: none; }
.check-icon { font-size: 1.1rem; }
.check-detail { color: var(--text2); font-size: .8rem; margin-left: auto; }

/* History table */
table { width: 100%; border-collapse: collapse; }
th, td { padding: 10px 12px; text-align: left; border-bottom: 1px solid var(--surface2); }
th { color: var(--text2); font-size: .85rem; font-weight: 500; }
td { font-size: .9rem; }
tr:hover { background: var(--surface2); }

/* Radar chart */
.radar-container { max-width: 400px; margin: 0 auto; }

/* Report */
.report-box { background: var(--bg); border: 1px solid var(--surface2); border-radius: var(--radius);
    padding: 16px; max-height: 500px; overflow-y: auto; font-family: monospace;
    font-size: .85rem; line-height: 1.6; white-space: pre-wrap; }

/* Loading */
.spinner { display: inline-block; width: 20px; height: 20px; border: 3px solid var(--surface2);
    border-top-color: var(--accent); border-radius: 50%; animation: spin .8s linear infinite; }
@keyframes spin { to { transform: rotate(360deg); } }

/* Badge */
.badge { display: inline-block; padding: 2px 8px; border-radius: 4px; font-size: .75rem;
    font-weight: 600; }
.badge-s { background: var(--purple); color: white; }
.badge-a { background: var(--green); color: white; }
.badge-b { background: #06b6d4; color: white; }
.badge-c { background: var(--yellow); color: #000; }
.badge-d { background: #f97316; color: white; }
.badge-f { background: var(--red); color: white; }

.empty-state { text-align: center; padding: 60px 20px; color: var(--text2); }
.empty-state .icon { font-size: 3rem; margin-bottom: 12px; }
</style>
</head>
<body>
<div class="container">
    <h1>Skill 评测工具 v3.0</h1>
    <p class="subtitle">六维度量化评分 · 基于 PPT 最佳实践 · 自动化检查 · 可视化报告</p>

    <div class="tabs">
        <button class="tab active" onclick="switchTab('audit')">评测</button>
        <button class="tab" onclick="switchTab('history')">历史记录</button>
        <button class="tab" onclick="switchTab('compare')">对比模式</button>
    </div>

    <!-- Audit Tab -->
    <div id="tab-audit" class="tab-content active">
        <div class="input-group">
            <input type="text" id="skill-path" placeholder="输入 Skill 目录路径，例如 ~/.cursor/skills/my-skill">
            <button class="btn" id="audit-btn" onclick="runAudit()">开始评测</button>
        </div>
        <div id="result-area"></div>
    </div>

    <!-- History Tab -->
    <div id="tab-history" class="tab-content">
        <div id="history-area"></div>
    </div>

    <!-- Compare Tab -->
    <div id="tab-compare" class="tab-content">
        <div id="compare-area">
            <div class="empty-state">
                <div class="icon">📊</div>
                <p>在历史记录中勾选多个评测记录进行对比</p>
            </div>
        </div>
    </div>
</div>

<script>
let currentReport = null;
let compareList = [];

function switchTab(name) {
    document.querySelectorAll('.tab').forEach((t, i) => {
        t.classList.toggle('active', ['audit','history','compare'][i] === name);
    });
    document.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));
    document.getElementById('tab-' + name).classList.add('active');
    if (name === 'history') loadHistory();
}

async function runAudit() {
    const path = document.getElementById('skill-path').value.trim();
    if (!path) return alert('请输入 Skill 路径');
    const btn = document.getElementById('audit-btn');
    btn.disabled = true;
    btn.innerHTML = '<span class="spinner"></span> 评测中...';
    document.getElementById('result-area').innerHTML = '';

    try {
        const resp = await fetch('/api/audit', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({path})
        });
        const data = await resp.json();
        if (data.error) throw new Error(data.error);
        currentReport = data;
        renderResult(data);
    } catch (e) {
        document.getElementById('result-area').innerHTML =
            `<div class="card" style="color:var(--red)">评测失败: ${e.message}</div>`;
    } finally {
        btn.disabled = false;
        btn.innerHTML = '开始评测';
    }
}

function gradeColor(grade) {
    return {S:'#a855f7',A:'#22c55e',B:'#06b6d4',C:'#eab308',D:'#f97316',F:'#ef4444'}[grade]||'#94a3b8';
}

function dimColor(pct) {
    if (pct >= 70) return 'var(--green)';
    if (pct >= 50) return 'var(--yellow)';
    return 'var(--red)';
}

function renderResult(r) {
    const color = gradeColor(r.grade);
    const pct = r.total_weighted / 100;
    const circumference = 2 * Math.PI * 70;
    const offset = circumference * (1 - pct);

    let html = `
    <div class="grid-2">
        <div class="card">
            <div class="score-ring-container">
                <div class="score-ring">
                    <svg width="180" height="180">
                        <circle cx="90" cy="90" r="70" fill="none" stroke="var(--surface2)" stroke-width="12"/>
                        <circle cx="90" cy="90" r="70" fill="none" stroke="${color}" stroke-width="12"
                            stroke-dasharray="${circumference}" stroke-dashoffset="${offset}"
                            stroke-linecap="round" style="transition:stroke-dashoffset 1s ease"/>
                    </svg>
                    <div class="value">
                        <div class="num" style="color:${color}">${r.total_weighted.toFixed(1)}</div>
                        <div class="grade">${r.grade} 级</div>
                    </div>
                </div>
            </div>
            <div style="text-align:center;color:var(--text2)">
                ${r.skill_name} · ${r.skill_md_lines} 行
                ${r.bonus_score > 0 ? `<br>最佳实践加分: +${r.bonus_score}` : ''}
            </div>
        </div>
        <div class="card">
            <div class="card-title">六维度雷达图</div>
            <div class="radar-container"><canvas id="radar-chart"></canvas></div>
        </div>
    </div>

    <div class="card">
        <div class="card-title">维度得分</div>
        ${r.dimensions.map(d => `
        <div class="dim-bar">
            <div class="label"><span>${d.name} (${d.weight}%)</span><span>${d.percentage.toFixed(0)}% → ${d.weighted_score.toFixed(1)}</span></div>
            <div class="bar"><div class="fill" style="width:${d.percentage}%;background:${dimColor(d.percentage)}"></div></div>
        </div>`).join('')}
    </div>

    <div class="grid-2">
        ${r.dimensions.map(d => `
        <div class="card">
            <div class="card-title">${d.name}</div>
            <ul class="check-list">
                ${d.checks.map(c => `
                <li class="check-item">
                    <span class="check-icon">${c.passed ? '✅' : '❌'}</span>
                    <span>${c.name}</span>
                    <span class="check-detail">${c.passed ? '+'+c.score : '0/'+c.max_score}${c.detail ? ' · '+c.detail : ''}</span>
                </li>`).join('')}
            </ul>
        </div>`).join('')}
    </div>

    ${r.bonus_checks ? `
    <div class="card">
        <div class="card-title">最佳实践（加分项）</div>
        <ul class="check-list">
            ${r.bonus_checks.map(c => `
            <li class="check-item">
                <span class="check-icon">${c.passed ? '✅' : '⬜'}</span>
                <span>${c.name}</span>
                <span class="check-detail">${c.passed ? '+'+c.score : '0'}</span>
            </li>`).join('')}
        </ul>
    </div>` : ''}

    <div class="card">
        <div class="card-title">Markdown 报告
            <button class="btn btn-sm btn-outline" style="float:right" onclick="downloadReport()">下载</button>
        </div>
        <div class="report-box" id="report-text">加载中...</div>
    </div>`;

    document.getElementById('result-area').innerHTML = html;

    new Chart(document.getElementById('radar-chart'), {
        type: 'radar',
        data: {
            labels: r.dimensions.map(d => d.name),
            datasets: [{
                label: r.skill_name,
                data: r.dimensions.map(d => d.percentage),
                backgroundColor: color + '33',
                borderColor: color,
                borderWidth: 2,
                pointBackgroundColor: color
            }]
        },
        options: {
            scales: { r: { min: 0, max: 100, ticks: { stepSize: 20, color: '#94a3b8' },
                grid: { color: '#334155' }, pointLabels: { color: '#e2e8f0', font: { size: 13 } } } },
            plugins: { legend: { display: false } }
        }
    });

    fetch('/api/report?path=' + encodeURIComponent(r.skill_path))
        .then(r => r.text()).then(t => { document.getElementById('report-text').textContent = t; });
}

function downloadReport() {
    if (!currentReport) return;
    const text = document.getElementById('report-text').textContent;
    const blob = new Blob([text], {type: 'text/markdown'});
    const a = document.createElement('a');
    a.href = URL.createObjectURL(blob);
    a.download = currentReport.skill_name + '_AUDIT_REPORT.md';
    a.click();
}

async function loadHistory() {
    const resp = await fetch('/api/history');
    const data = await resp.json();
    if (!data.length) {
        document.getElementById('history-area').innerHTML =
            '<div class="empty-state"><div class="icon">📋</div><p>暂无评测记录</p></div>';
        return;
    }
    let html = `<div class="card"><table>
        <tr><th></th><th>Skill</th><th>得分</th><th>评级</th><th>维度速览</th><th>时间</th><th>操作</th></tr>
        ${data.map((r, i) => `<tr>
            <td><input type="checkbox" onchange="toggleCompare(${i})" ${compareList.includes(i)?'checked':''}></td>
            <td>${r.skill_name}</td>
            <td>${r.total_weighted.toFixed(1)}</td>
            <td><span class="badge badge-${r.grade.toLowerCase()}">${r.grade}</span></td>
            <td>${r.dimensions.map(d => {
                const c = d.percentage >= 70 ? 'var(--green)' : d.percentage >= 50 ? 'var(--yellow)' : 'var(--red)';
                return `<span style="display:inline-block;width:12px;height:12px;border-radius:2px;background:${c};margin-right:2px" title="${d.name}: ${d.percentage.toFixed(0)}%"></span>`;
            }).join('')}</td>
            <td style="color:var(--text2);font-size:.8rem">${r.timestamp}</td>
            <td><button class="btn btn-sm btn-outline" onclick="viewHistory(${i})">查看</button></td>
        </tr>`).join('')}
    </table></div>
    <div style="margin-top:12px">
        <button class="btn" onclick="runCompare()">对比选中项</button>
    </div>`;
    document.getElementById('history-area').innerHTML = html;
}

function toggleCompare(idx) {
    const i = compareList.indexOf(idx);
    if (i >= 0) compareList.splice(i, 1);
    else compareList.push(idx);
}

async function viewHistory(idx) {
    const resp = await fetch('/api/history');
    const data = await resp.json();
    if (data[idx]) {
        currentReport = data[idx];
        switchTab('audit');
        renderResult(data[idx]);
    }
}

async function runCompare() {
    if (compareList.length < 2) return alert('请至少选择 2 个记录进行对比');
    const resp = await fetch('/api/history');
    const data = await resp.json();
    const selected = compareList.map(i => data[i]).filter(Boolean);

    switchTab('compare');
    const colors = ['#3b82f6','#22c55e','#a855f7','#f97316','#ef4444'];
    let html = `<div class="card">
        <div class="card-title">雷达图对比</div>
        <div class="radar-container"><canvas id="compare-radar"></canvas></div>
    </div>
    <div class="card"><table>
        <tr><th>维度</th>${selected.map(s => `<th>${s.skill_name}</th>`).join('')}</tr>
        ${selected[0].dimensions.map((d, di) => `<tr>
            <td>${d.name}</td>
            ${selected.map(s => `<td>${s.dimensions[di].percentage.toFixed(0)}%</td>`).join('')}
        </tr>`).join('')}
        <tr style="font-weight:600"><td>总分</td>
            ${selected.map(s => `<td>${s.total_weighted.toFixed(1)} [${s.grade}]</td>`).join('')}
        </tr>
    </table></div>`;

    document.getElementById('compare-area').innerHTML = html;

    new Chart(document.getElementById('compare-radar'), {
        type: 'radar',
        data: {
            labels: selected[0].dimensions.map(d => d.name),
            datasets: selected.map((s, i) => ({
                label: s.skill_name,
                data: s.dimensions.map(d => d.percentage),
                backgroundColor: colors[i % colors.length] + '22',
                borderColor: colors[i % colors.length],
                borderWidth: 2,
                pointBackgroundColor: colors[i % colors.length]
            }))
        },
        options: {
            scales: { r: { min: 0, max: 100, ticks: { stepSize: 20, color: '#94a3b8' },
                grid: { color: '#334155' }, pointLabels: { color: '#e2e8f0', font: { size: 13 } } } },
            plugins: { legend: { labels: { color: '#e2e8f0' } } }
        }
    });
}
</script>
</body>
</html>
"""


@app.route("/")
def index():
    return render_template_string(HTML_TEMPLATE)


@app.route("/api/audit", methods=["POST"])
def api_audit():
    data = request.json
    path = data.get("path", "").strip()
    if not path:
        return jsonify({"error": "请提供 Skill 路径"}), 400

    path = os.path.expanduser(path)
    if not os.path.isdir(path):
        return jsonify({"error": f"路径不存在: {path}"}), 400

    try:
        auditor = SkillAuditor(path)
        report = auditor.audit()
        result = generate_json_report(report)

        history = load_history()
        history.insert(0, result)
        if len(history) > 100:
            history = history[:100]
        save_history(history)

        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/history")
def api_history():
    return jsonify(load_history())


@app.route("/api/report")
def api_report():
    path = request.args.get("path", "")
    if not path or not os.path.isdir(path):
        return "路径无效", 400

    auditor = SkillAuditor(path)
    report = auditor.audit()
    return generate_markdown_report(report), 200, {"Content-Type": "text/plain; charset=utf-8"}


if __name__ == "__main__":
    print("Skill 评测工具 Web UI v3.0 — 基于 PPT 最佳实践")
    print("访问 http://localhost:5000")
    app.run(host="0.0.0.0", port=5000, debug=False)
