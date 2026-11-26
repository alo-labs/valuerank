"""Render the precomputed comparison as self-contained SVG."""
import json
import math
from html import escape
from pathlib import Path

HERE = Path(__file__).resolve().parent
CUTOFF = "2026-11-01T06:10:00Z"
WORKLOADS = {"common": "835a9baf594a1251", "main": "aad36e77d6e17386", "aicd": "835a9baf594a1251"}

def esc(s):
    return escape(str(s), quote=True)

def grade(data, p, changed):
    if changed:
        return "owner-stated, unmeasured"
    for c in data.get("configurations", []):
        row = (c.get("tracks", {}).get("common") or {}).get("row") or {}
        if row.get("id") == p.get("id") and p.get("id") is not None:
            return (row.get("plan") or {}).get("grade") or "API fallback"
    return "API fallback"

def render_chart(data, chart):
    ps = data["pareto"]
    groups = {"api-common": [("Common leaves", "common", ps["apiCommon"])],
              "plan-common": [("Common leaves", "common", ps["planCommonWhatIf"])],
              "api-by-track": [("Max-effort", "main", ps["apiMain"]), ("AI Coding Daily", "aicd", ps["apiAicd"])]}[chart]
    plan = chart == "plan-common"
    height = 180 + 620 * len(groups) + 120
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="1400" height="{height}" viewBox="0 0 1400 {height}" role="img">',
           '<title>ValueRank cost and quality comparison</title><rect width="100%" height="100%" fill="white"/>',
           '<style>text{font-family:Arial,sans-serif;fill:#172337}.axis{stroke:#34445c;stroke-width:1.5}.grid{stroke:#d8e0eb}.frontier-step{fill:none;stroke:#176d64;stroke-width:3}.fallback-link{stroke:#6c788b;stroke-width:1.5}.small{font-size:15px}.key{font-size:15px}</style>',
           f'<text x="50" y="40" font-size="25" font-weight="bold">{esc(chart.replace("-", " ").title())}</text>',
           '<text x="50" y="67" class="small">Lower cost and higher quality are better; x-axis uses a log scale.</text>']
    for group_index, (title, track, points) in enumerate(groups):
        y0 = 95 + 620 * group_index
        fallback = ps["planCommonPublished"] if plan else []
        pairs = [(w, next((p for p in fallback if p["configuration"] == w["configuration"]), None)) for w in points]
        matches = [(w, f) for w, f in pairs if f and w["cost"] != f["cost"]]
        all_points = points + [f for _, f in matches if f]
        if not all_points:
            out.append(f'<text x="50" y="{y0+30}">{esc(title)}: no eligible rows</text>')
            continue
        if any(p["cost"] <= 0 or not math.isfinite(p["cost"]) or not math.isfinite(p["quality"]) for p in all_points):
            raise ValueError("Costs must be positive; costs and quality must be finite")
        logs = [math.log10(p["cost"]) for p in all_points]
        lo, hi = min(logs), max(logs)
        if hi == lo: lo, hi = lo-.5, hi+.5
        lo, hi = lo-.12*(hi-lo), hi+.12*(hi-lo)
        qs = [p["quality"] for p in all_points]
        qlo, qhi = min(qs), max(qs)
        if qlo == qhi: qlo, qhi = qlo-1, qhi+1
        qlo, qhi = qlo-.15*(qhi-qlo), qhi+.15*(qhi-qlo)
        left, right, top, bottom = 110, 900, y0+55, y0+385
        x = lambda p: left+(math.log10(p["cost"])-lo)/(hi-lo)*(right-left)
        y = lambda p: bottom-(p["quality"]-qlo)/(qhi-qlo)*(bottom-top)
        out.append(f'<text x="50" y="{y0+20}" font-size="20" font-weight="bold">{esc(title)} · {esc("Plan" if plan else "API")} · workload {WORKLOADS[track]}</text>')
        for i in range(5):
            yy = bottom-i*(bottom-top)/4
            xx = left+i*(right-left)/4
            out.append(f'<line class="grid" x1="{left}" y1="{yy:.2f}" x2="{right}" y2="{yy:.2f}"/><text class="small" x="55" y="{yy+5:.2f}">{qlo+i*(qhi-qlo)/4:.1f}</text>')
            out.append(f'<line class="grid" x1="{xx:.2f}" y1="{top}" x2="{xx:.2f}" y2="{bottom}"/><text class="small" text-anchor="middle" x="{xx:.2f}" y="{bottom+23}">${10**(lo+i*(hi-lo)/4):,.2f}</text>')
        out.append(f'<line class="axis" x1="{left}" y1="{bottom}" x2="{right}" y2="{bottom}"/><line class="axis" x1="{left}" y1="{top}" x2="{left}" y2="{bottom}"/>')
        out.append(f'<text class="small" x="340" y="{bottom+48}">Whole workload cost in USD (log scale)</text><text class="small" transform="translate(22 {bottom-40}) rotate(-90)">Displayed quality</text>')
        front = sorted((p for p in points if p["onFrontierAmongPlotted"]), key=lambda p:p["cost"])
        if front:
            d = f'M {x(front[0]):.2f} {y(front[0]):.2f}'
            for p in front[1:]: d += f' H {x(p):.2f} V {y(p):.2f}'
            out.append(f'<path class="frontier-step" d="{d}"/>')
        for w, f in matches:
            if f:
                out.append(f'<line class="fallback-link" x1="{x(w):.2f}" y1="{y(w):.2f}" x2="{x(f):.2f}" y2="{y(f):.2f}"/><circle class="fallback-marker" cx="{x(f):.2f}" cy="{y(f):.2f}" r="8" fill="white" stroke="#58677a" stroke-width="2"/>')
        used = []
        for i, p in enumerate(points, 1):
            actual_x, actual_y = x(p), y(p)
            cx, cy = actual_x, actual_y
            while any(math.hypot(cx-px, cy-py) < 23 for px, py in used):
                cy -= 24
            used.append((cx, cy))
            if cy != actual_y:
                out.append(f'<circle cx="{actual_x:.2f}" cy="{actual_y:.2f}" r="3" fill="#172337"/><line class="marker-leader" x1="{actual_x:.2f}" y1="{actual_y:.2f}" x2="{cx:.2f}" y2="{cy:.2f}" stroke="#172337"/>')
            color = "#126c62" if p["onFrontierAmongPlotted"] else "#a6b0bc"
            g = grade(data, p, any(w is p for w, _ in matches)) if plan else ""
            if g == "controlled": shape = f'<rect x="{cx-9:.2f}" y="{cy-9:.2f}" width="18" height="18" fill="{color}" stroke="#183445"/>'
            elif g == "assumption": shape = f'<path d="M {cx:.2f} {cy-11:.2f} l 11 11 -11 11 -11 -11 Z" fill="{color}" stroke="#183445"/>'
            else: shape = f'<circle cx="{cx:.2f}" cy="{cy:.2f}" r="10" fill="{color}" stroke="#183445"/>'
            out.append(f'<g><title>{esc(p["configuration"])} · ${p["cost"]:.2f} · quality {p["quality"]:.2f}</title>{shape}<text x="{cx:.2f}" y="{cy+4:.2f}" text-anchor="middle" font-size="11" font-weight="bold" style="fill:white">{i}</text></g>')
            status = "frontier" if p["onFrontierAmongPlotted"] else "dominated"
            full = "full-track Pareto set" if p["onFullTrackParetoSet"] else "not on full-track Pareto set"
            name = p["configuration"]
            if p.get("effort") and ("(" + p["effort"] + ")").lower() not in name.lower():
                name += " (" + p["effort"] + ")"
            out.append(f'<text class="key" x="930" y="{top+20+(i-1)*38}">{i}. {esc(name)}</text>')
            out.append(f'<text class="small" x="950" y="{top+37+(i-1)*38}">{esc(status)}; {esc(full)}{esc(" · "+g if plan else "")}</text>')
        out.append(f'<text class="small" x="50" y="{bottom+82}">Step: frontier among plotted points only. Grey: dominated. Leader lines offset overlapping markers from their exact points.</text>')
        if plan:
            out.append(f'<text class="small" x="50" y="{bottom+104}">Square: controlled; diamond: assumption; circle: owner-stated, unmeasured or API fallback. Hollow: published fallback.</text>')
            out.append(f'<text class="small" x="50" y="{bottom+126}">Line joins the published fallback to the what-if; step uses what-if costs.</text>')
    footer = height-65
    out.append(f'<text class="small" x="50" y="{footer}">Source: data/scores.json via comparison.json · cutoff {CUTOFF} · displayed-record precision, not sampling uncertainty.</text>')
    out.append(f'<text class="small" x="50" y="{footer+23}">Plan multiples are owner-authorised or assumed unless controlled. See comparison for neighbouring pairs not separable.</text></svg>')
    return "\n".join(out)

def main():
    data = json.loads((HERE / "comparison.json").read_text())
    for name in ("api-common", "plan-common", "api-by-track"):
        (HERE / f"pareto-{name}.svg").write_text(render_chart(data, name), encoding="utf-8")

if __name__ == "__main__":
    main()
