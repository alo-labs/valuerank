#!/usr/bin/env python3
"""Generate the current Terminal-Bench 4.0 static publication page."""

from __future__ import annotations

import json
import sys
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REFRESH = ROOT / ".refresh" / "v1.4"
OUT = ROOT / "site" / "tb4" / "index.html"
sys.path.insert(0, str(ROOT / "scripts"))
from site_header import inject_header


def main() -> int:
    document = json.loads((REFRESH / "tb4.json").read_text())
    entries = document["rows"]
    best_rate = -float("inf")
    frontier_count = 0
    for entry in sorted(entries, key=lambda item: (item["costUsd"], -item["resolutionRate"])):
        if entry["resolutionRate"] > best_rate:
            best_rate = entry["resolutionRate"]
            frontier_count += 1
    rows_html = "\n".join(
        "<tr>"
        f"<td class=\"mono\">{escape(entry['rankLabel'])}</td>"
        f"<td><strong>{escape(entry['baseModel'])}</strong><span class=\"variant\">{escape(entry['model'])}</span></td>"
        f"<td>{escape(entry['agent'])}</td>"
        f"<td class=\"mono\">{entry['resolutionRatePct']:.1f}% <span class=\"uncertainty\">± {entry['uncertaintyPct']:.1f}%</span></td>"
        f"<td class=\"mono\">{escape(entry['tokens'])}</td>"
        f"<td class=\"mono\">${entry['costUsd']:,.0f}</td>"
        f"<td class=\"{'covered' if entry['cohortModelId'] else 'muted'}\">{'ValueRank cohort' if entry['cohortModelId'] else 'Official-only'}</td>"
        "</tr>"
        for entry in entries
    )
    entries_json = json.dumps(entries, ensure_ascii=False, separators=(",", ":"))
    missing_html = ", ".join(escape(name) for name in document["missingModels"])
    template = r'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>Terminal-Bench 4.0 — Score vs Cost · ValueRank</title>
  <meta name="description" content="Official Terminal-Bench 4.0 resolution rate versus total cost, with a Pareto frontier and ValueRank cohort coverage.">
  <meta property="og:title" content="Terminal-Bench 4.0 — Score vs Cost · ValueRank">
  <meta property="og:description" content="Official Terminal-Bench 4.0 resolution rate versus total cost with Pareto frontier.">
  <meta property="og:url" content="https://valuerank.alolabs.dev/tb4/">
  <meta property="og:type" content="website">
  <meta property="og:image" content="https://valuerank.alolabs.dev/tb4/og.png?v=1">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:type" content="image/png">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Terminal-Bench 4.0 — Score vs Cost · ValueRank">
  <meta name="twitter:description" content="Official Terminal-Bench 4.0 resolution rate versus total cost with Pareto frontier.">
  <meta name="twitter:image" content="https://valuerank.alolabs.dev/tb4/og.png?v=1">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600&family=IBM+Plex+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&display=swap" rel="stylesheet">
  <script src="https://cdn.plot.ly/plotly-2.27.0.min.js"></script>
  <script src="https://unpkg.com/lucide@latest/dist/umd/lucide.min.js"></script>
  <script>(function(){var s=localStorage.getItem('vr-theme');if(s==='dark')document.documentElement.setAttribute('data-theme','dark');}());</script>
  <style>
    :root { --bg-page:#f8f9fc; --bg-card:#fff; --nav-bg:rgba(248,249,252,.92); --accent:#4f46e5; --green:#059669; --text-primary:#0f172a; --text-secondary:#475569; --text-dim:#94a3b8; --border:#e2e8f0; --font-heading:'IBM Plex Sans',system-ui,sans-serif; --font-mono:'IBM Plex Mono',monospace; }
    [data-theme="dark"] { --bg-page:#0a0a0f; --bg-card:#12121a; --nav-bg:rgba(10,10,15,.88); --accent:#818cf8; --green:#34d399; --text-primary:#e2e8f0; --text-secondary:#94a3b8; --text-dim:#64748b; --border:#1e293b; }
    *,*::before,*::after { box-sizing:border-box; }
    html { scroll-behavior:smooth; -webkit-font-smoothing:antialiased; }
    body { margin:0; background:var(--bg-page); color:var(--text-primary); font-family:var(--font-heading); font-size:14px; line-height:1.7; }
    main { max-width:1160px; margin:0 auto; padding:104px 24px 64px; }
    h1,h2 { letter-spacing:-.025em; line-height:1.15; }
    h1 { font-size:clamp(2rem,5vw,3.8rem); margin:0 0 14px; }
    h2 { font-size:1.35rem; margin:0 0 8px; }
    .eyebrow { color:var(--accent); font:600 11px/1.4 var(--font-mono); letter-spacing:.08em; text-transform:uppercase; }
    .lede { max-width:760px; color:var(--text-secondary); font-size:16px; margin:0; }
    .hero { padding:28px 0 30px; }
    .hero a,.source a { color:var(--accent); }
    .stats { display:flex; flex-wrap:wrap; gap:10px; margin-top:24px; }
    .stat { background:var(--bg-card); border:1px solid var(--border); border-radius:10px; padding:12px 16px; min-width:150px; }
    .stat strong { display:block; font:600 20px/1.2 var(--font-mono); }
    .stat span { color:var(--text-dim); font-size:11px; }
    .card { background:var(--bg-card); border:1px solid var(--border); border-radius:14px; padding:20px; margin-top:24px; }
    .card-head { display:flex; justify-content:space-between; align-items:flex-start; gap:16px; flex-wrap:wrap; }
    .sub { color:var(--text-secondary); margin:0 0 16px; }
    #chart { height:560px; margin-top:12px; }
    .table-wrap { overflow-x:auto; }
    table { width:100%; border-collapse:collapse; min-width:800px; }
    th,td { text-align:left; padding:11px 9px; border-bottom:1px solid var(--border); vertical-align:top; }
    th { color:var(--text-dim); font:600 11px/1.4 var(--font-mono); text-transform:uppercase; letter-spacing:.04em; white-space:nowrap; }
    td.mono { font-family:var(--font-mono); }
    td strong { display:block; }
    .variant { display:block; color:var(--text-dim); font-size:11px; }
    .uncertainty { color:var(--text-dim); }
    .covered { color:var(--green); font-size:12px; }
    .muted { color:var(--text-dim); font-size:12px; }
    .note { color:var(--text-secondary); font-size:13px; }
    .source { display:flex; flex-wrap:wrap; gap:18px; color:var(--text-dim); font-size:12px; }
    footer { max-width:1160px; margin:0 auto; padding:24px; border-top:1px solid var(--border); color:var(--text-dim); font-size:12px; }
    @media (max-width:700px) { main { padding-inline:14px; } .card { padding:14px; } #chart { height:480px; } }
  </style>
</head>
<body>
  <nav></nav>
  <main>
    <section class="hero">
      <div class="eyebrow">Official benchmark view · current release 4.0</div>
      <h1>Terminal-Bench 4.0</h1>
      <p class="lede">Resolution rate versus total benchmark cost for the current official leaderboard. The chart marks models that are undominated when higher resolution and lower cost are considered together.</p>
      <div class="stats">
        <div class="stat"><strong>__ROW_N__</strong><span>official rows</span></div>
        <div class="stat"><strong>__MATCHED_N__/__COHORT_N__</strong><span>ValueRank cohort coverage</span></div>
        <div class="stat"><strong>__FRONTIER_N__</strong><span>cost / resolution frontier rows</span></div>
        <div class="stat"><strong>Sep 2026</strong><span>latest observed release window</span></div>
      </div>
    </section>

    <section class="card">
      <div class="card-head"><div><h2>Resolution Rate vs Cost</h2><p class="sub">X-axis is logarithmic because official run costs span orders of magnitude; hover for agent, uncertainty, tokens, and rank.</p></div><div class="eyebrow">Higher is better · lower cost is better</div></div>
      <div id="chart" aria-label="Terminal-Bench 4.0 resolution rate versus cost chart"></div>
    </section>

    <section class="card">
      <h2>Official Terminal-Bench 4.0 leaderboard</h2>
      <p class="sub">The table reproduces the current rendered official rows. “ValueRank cohort” identifies rows that map exactly to the 21-model DeepSWE cohort; unmatched models stay visible as official-only rows.</p>
      <div class="table-wrap"><table>
        <thead><tr><th>Rank</th><th>Model</th><th>Agent</th><th>Resolution rate</th><th>Tokens</th><th>Cost</th><th>ValueRank coverage</th></tr></thead>
        <tbody>__ROWS_HTML__</tbody>
      </table></div>
    </section>

    <section class="card">
      <h2>Coverage and interpretation</h2>
      <p class="note">The TB4 snapshot overlaps __MATCHED_N__ of the __COHORT_N__ current ValueRank models. The missing cohort rows are: __MISSING_MODELS__.</p>
      <p class="note">ValueRank keeps TB4 as an auditable external component and does not neutral-fill the ten missing cohort values. It therefore does not change the primary zero-gap score until the official source covers the complete cohort.</p>
      <div class="source">
        <span>Source: <a href="https://www.tbench.ai/" target="_blank" rel="noopener">tbench.ai</a></span>
        <span>Target release: <a href="https://www.tbench.ai/leaderboard/terminal-bench/4.0" target="_blank" rel="noopener">Terminal-Bench 4.0</a></span>
        <span>Tasks: <a href="https://hub.harborframework.com/datasets/terminal-bench/terminal-bench/4?tab=tasks" target="_blank" rel="noopener">Harbor dataset</a></span>
      </div>
    </section>
  </main>
  <footer>ValueRank · Terminal-Bench 4.0 · Official snapshot · <a href="/">LLM Models</a> · <a href="/coding-agents/">Coding Agents</a></footer>
  <script>
    const ENTRIES = __ENTRIES_JSON__;
    const PLOTLY_CONFIG = {responsive:true, displaylogo:false, modeBarButtonsToRemove:['lasso2d','select2d']};
    const isDark = () => document.documentElement.getAttribute('data-theme') === 'dark';
    function layout() {
      return {
        paper_bgcolor:'transparent', plot_bgcolor:'transparent', font:{family:'IBM Plex Sans, sans-serif', color:isDark()?'#cbd5e1':'#334155'},
        margin:{l:64,r:24,t:28,b:80}, hovermode:'closest',
        xaxis:{type:'log', title:'Total cost (USD, log scale)', gridcolor:isDark()?'#1e293b':'#e2e8f0', zeroline:false, tickprefix:'$', tickformat:',.0f'},
        yaxis:{title:'Resolution rate (%)', range:[0,64], gridcolor:isDark()?'#1e293b':'#e2e8f0', zeroline:false, ticksuffix:'%'},
        legend:{orientation:'h', y:-.18},
      };
    }
    function frontierRows(rows) {
      const sorted = [...rows].sort((a,b) => a.costUsd-b.costUsd || b.resolutionRate-a.resolutionRate);
      let best = -Infinity;
      return sorted.filter(row => { if (row.resolutionRate > best) { best=row.resolutionRate; return true; } return false; });
    }
    function render() {
      const frontier = frontierRows(ENTRIES);
      const ids = new Set(frontier.map(row => row.model));
      const dominated = ENTRIES.filter(row => !ids.has(row.model));
      const custom = row => [row.baseModel,row.agent,row.resolutionRatePct,row.uncertaintyPct,row.tokens,row.rankLabel,row.model];
      const hover = '<b>%{customdata[0]}</b><br>Resolution: %{customdata[2]:.1f}% ± %{customdata[3]:.1f}%<br>Cost: $%{x:,.0f}<br>Agent: %{customdata[1]}<br>Tokens: %{customdata[4]}<br>Rank: %{customdata[5]}<br>Variant: %{customdata[6]}<extra></extra>';
      const traces = [
        {x:dominated.map(row=>row.costUsd), y:dominated.map(row=>row.resolutionRatePct), mode:'markers', type:'scatter', name:'Official rows', marker:{size:11,color:'#a78bfa',opacity:.65}, customdata:dominated.map(custom), hovertemplate:hover},
        {x:frontier.map(row=>row.costUsd), y:frontier.map(row=>row.resolutionRatePct), mode:'markers', type:'scatter', name:'Pareto frontier', marker:{size:15,color:'#10b981',line:{width:2,color:isDark()?'#064e3b':'#ecfdf5'}}, customdata:frontier.map(custom), hovertemplate:hover.replace('<extra></extra>','<extra>Frontier</extra>')},
        {x:frontier.map(row=>row.costUsd), y:frontier.map(row=>row.resolutionRatePct), mode:'lines', type:'scatter', name:'frontier-curve', line:{shape:'spline',dash:'dot',color:'#94a3b8',width:2}, hoverinfo:'skip', showlegend:false},
      ];
      Plotly.newPlot('chart', traces, layout(), PLOTLY_CONFIG).then(() => {
        const gd = document.getElementById('chart');
        const frontierIds = new Set(frontier.map(row => row.model));
        const points = ENTRIES.map(row => ({
          id: row.model,
          label: row.baseModel,
          x: row.costUsd,
          y: row.resolutionRatePct,
          frontier: frontierIds.has(row.model),
        }));
        const annotations = buildCollisionSafeLabelAnnotations(points, gd, { fontSize: 9, markerRadius: 12, safety: 1.12 });
        return Plotly.relayout(gd, { annotations }).then(() => repairCollisionSafeLabelAnnotations(gd, annotations));
      });
    }
    function updateTheme() { const el=document.getElementById('chart'); if (el && el.querySelector('.plotly')) Plotly.relayout(el, layout()); }
    document.getElementById('theme-toggle').addEventListener('click', () => { const next=isDark()?'':'dark'; document.documentElement.setAttribute('data-theme',next); localStorage.setItem('vr-theme',next?'dark':'light'); requestAnimationFrame(updateTheme); });
    document.addEventListener('DOMContentLoaded', () => { render(); if (typeof lucide !== 'undefined') lucide.createIcons(); });
  </script>
</body>
</html>
'''
    html = template.replace("__ROW_N__", str(document["rowN"]))
    html = html.replace("__MATCHED_N__", str(document["matchedN"]))
    html = html.replace("__COHORT_N__", str(document["cohortN"]))
    html = html.replace("__FRONTIER_N__", str(frontier_count))
    html = html.replace("__MISSING_MODELS__", missing_html)
    html = html.replace("__ROWS_HTML__", rows_html)
    html = html.replace("__ENTRIES_JSON__", entries_json)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(html)
    inject_header(OUT, "tb4", f"{document['rowN']} official rows · current 4.0", "v1.4.0")
    print(json.dumps({"output": str(OUT.relative_to(ROOT)), "rows": document["rowN"], "matched": document["matchedN"]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
