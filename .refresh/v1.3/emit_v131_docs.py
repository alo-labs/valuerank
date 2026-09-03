#!/usr/bin/env python3
"""Emit v1.3.1 markdown + patch site/index.html MODELS from scores.json."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path("/Users/shafqat/valuerank")
R = ROOT / ".refresh" / "v1.3"
VERSION = "v1.3.1"
DATE = "July 28, 2026"

data = json.loads((R / "scores.json").read_text())
manifest = json.loads((R / "run_manifest.json").read_text())
models = data["models"]
weights = data["weights"]
pareto = data["pareto"]
appendix = data.get("appendixNonRanked") or []
n = len(models)
d = len(weights)
dim_labels = [w["label"] for w in weights]
dim_order = ", ".join(dim_labels)

# ── methodology.md ──────────────────────────────────────────────
ranked_list = "\n".join(f"- {m['name']}" for m in models)
excl = appendix[0] if appendix else None
excl_block = ""
if excl:
    excl_block = f"""
## Ranked-cohort exclusion

**{excl['name']}** is on the DeepSWE Best roster but **not ranked** in ValueRank {VERSION}:

- Reason: no published AA Intelligence Index **total eval cost** on [{excl.get('aaUrl', 'https://artificialanalysis.ai/models/kimi-k2-7-code')}]({excl.get('aaUrl', 'https://artificialanalysis.ai/models/kimi-k2-7-code')}).
- Evidence: [`.refresh/v1.3/aa-kimi-k27-cost-search.md`](.refresh/v1.3/aa-kimi-k27-cost-search.md) (search verdict NOT FOUND, 2026-07-28).
- DeepSWE pass@1 / avg cost remain in [raw-data.md](raw-data.md) as a non-ranked appendix row.
"""

weight_rows = "\n".join(
    f"| {w['label']} | {w['weight']:.2f}% |" for w in weights
)

methodology = f"""# ValueRank Methodology

**Version:** {VERSION}
**Updated:** {DATE}

## Cohort Rule

{VERSION} ranks **{n}** models from the current [DeepSWE](https://deepswe.datacurve.ai/) Best roster (source updated July 25, 2026; roster size 18). Historical exclusions that remain off-roster: `Grok-Build-0.1`, `Gemini 3 Flash`, `Claude Opus 4.6`. `Grok 4.5` is ranked (it is on DeepSWE Best).

**Changelog vs v1.3:** `{excl['name'] if excl else 'n/a'}` removed from the ranked cohort so Cost can restore the AA+DeepSWE composite (AA Index total eval cost unpublished for that model).

Ranked cohort (n={n}):

{ranked_list}
{excl_block}
## Zero-Gap Rule

- Every retained dimension must have a genuine current score for all **{n}** ranked models.
- If even one ranked model is genuinely missing from a benchmark, that benchmark is excluded.
- {VERSION} has **zero missing benchmark cells** and uses **no neutral 50 placeholders** on the main product.

## Scored Dimensions

ValueRank {VERSION} uses **{d}** fully covered dimensions:

{chr(10).join(f"{i}. {lab}" for i, lab in enumerate(dim_labels, 1))}

Dropped vs v1.2 (incomplete AA coverage for newest DeepSWE models — still incomplete after excluding Kimi K2.7 Code): IFBench, Terminal-Bench Hard, τ²-Bench Telecom.

## Weights

Relative v1.2 priorities are preserved among retained dimensions and renormalized to 100%:

| Dimension | Weight |
|---|---:|
{weight_rows}

## Normalization

`((n - rank) / (n - 1)) * 100` with `n = {n}`.

- Best → 100, worst → 0, ties average ranks.
- For Hallucination, lower raw rate is better.
- For Cost, lower composite cost is better.

## Cost Construction

Composite AA+DeepSWE (restored in {VERSION}):

1. Normalize AA Intelligence Index **total eval cost** onto 0–100 (highest-cost ranked model = 100; higher cost = higher penalty).
2. Normalize DeepSWE Best-row average cost per task onto 0–100 the same way.
3. Average the two penalties → composite cost scale.
4. Rank-normalize that composite (lower better) for the Cost dimension.

## Quality Score

Quality removes the Cost term and renormalizes remaining non-cost dimensions to 100%.

## Source Policy

- DeepSWE for pass@1 and avg cost.
- Artificial Analysis model pages for retained AA metrics.
- Official-first gap audit for excluded benchmarks (see raw-data.md).
"""
(ROOT / "methodology.md").write_text(methodology)

# ── scores.md ───────────────────────────────────────────────────
rank_rows = "\n".join(
    f"| {m['rank']} | {m['name']} | {m['overallScore']} | {m['qualityScore']} | {m['qualityRank']} | 0 |"
    for m in models
)
pareto_bullets = "\n".join(f"- {p}" for p in pareto)
dominated = [m["name"] for m in models if m["name"] not in pareto]
norm_rows = "\n".join(
    f"| {m['name']} | `[{', '.join(str(m['dims'][w['key']]) for w in weights)}]` |"
    for m in models
)

scores_md = f"""# ValueRank {VERSION} Scores

**Version:** {VERSION}
**Updated:** {DATE}

{VERSION} ranks **n={n}** DeepSWE Best models (excludes Kimi K2.7 Code — no AA Index total eval cost), retains **{d} zero-gap dimensions**, drops IFBench / Terminal-Bench Hard / τ²-Bench (incomplete AA coverage on newest models), and restores **AA+DeepSWE composite Cost**.

## Final Ranking

| Rank | Model | Overall | Quality | Quality Rank | Missing Dims |
|---|---|---:|---:|---:|---:|
{rank_rows}

## Pareto Frontier

Undominated on composite cost vs. quality:

{pareto_bullets}

Dominated models: {", ".join(dominated)}.

## Normalized Dimension Matrix

Dimension order:

`[{dim_order}]`

| Model | Normalized dimensions |
|---|---|
{norm_rows}
"""
(ROOT / "scores.md").write_text(scores_md)

# ── README.md ───────────────────────────────────────────────────
readme_rows = "\n".join(
    f"| {m['rank']} | {m['name']} | {m['overallScore']} | {m['qualityScore']} | {m['costComposite']:.2f} |"
    for m in models
)
readme = f"""# ValueRank
**Frontier AI model ranking focused on production value**

**Version:** {VERSION}  
**Updated:** {DATE}  
**Scope:** {n} DeepSWE Best models (ranked), {d} scored dimensions

## What ValueRank is

ValueRank is a production-weighted ranking of frontier AI models. It combines benchmark quality, reliability, speed, and a composite cost term into a single rank-based score.

{VERSION} ranks **n={n}** models from the current DeepSWE Best roster, keeps the **zero-gap** rule (no neutral-50 fills), drops dimensions without full AA coverage on the new models, and restores **AA+DeepSWE composite Cost**. **Kimi K2.7 Code** remains on DeepSWE but is **excluded from the ranked cohort** because AA Intelligence Index total eval cost is unpublished ([search evidence](.refresh/v1.3/aa-kimi-k27-cost-search.md)).

- Keeps the ranked pool limited to **models on the current DeepSWE Best leaderboard** with complete Cost inputs
- Explicitly excludes off-roster historical models: **Grok-Build-0.1**, **Gemini 3 Flash**, **Claude Opus 4.6**
- Excludes **Kimi K2.7 Code** from ranking (no AA Index total eval cost; DeepSWE row preserved in raw-data)
- Includes **Grok 4.5**, **Claude Opus 5**, **GPT-5.6 Sol/Terra/Luna**, **Kimi K3**, **Muse Spark 1.1**, and other July 2026 DeepSWE entrants
- Uses only **benchmarks with full coverage across all {n} ranked models**
- Drops **IFBench**, **Terminal-Bench Hard**, and **τ²-Bench Telecom** (missing on newest AA model pages)
- Reruns the excluded-benchmark audit against **official sources first**, then secondary implementations

## {VERSION} Ranking

Cost is the average of normalized AA Index total eval cost and normalized DeepSWE avg cost per task (0–100, higher = costlier), then rank-normalized.

| Rank | Model | Score | Quality | Composite Cost |
|---|---|---:|---:|---:|
{readme_rows}

## {VERSION} Frontier

Undominated on composite cost vs. quality:

{pareto_bullets}

## Sources Used in {VERSION}

- [DeepSWE](https://deepswe.datacurve.ai/) (Best roster; updated July 25, 2026)
- [Artificial Analysis model pages](https://artificialanalysis.ai/models)
- Evidence ledger: [`.refresh/v1.3/`](.refresh/v1.3/)

## Files

- [scores.md](scores.md): final rankings and normalized scores
- [raw-data.md](raw-data.md): benchmark inputs and official-first exclusion audit
- [methodology.md](methodology.md): scoring method, weights, cohort rules, and audit policy
- [site/index.html](site/index.html): published static site
"""
(ROOT / "README.md").write_text(readme)

# ── raw-data.md (rebuild core sections from scores + appendix) ───
all_for_tables = models + appendix  # ranked first, then appendix

def row_deepswe(m):
    effort = m.get("deepsweEffort") or "—"
    return f"| {m['name']} | {effort} | {m['deepswePassAt1']} | {m['deepsweCost']:.2f} |"

def row_omni(m):
    return f"| {m['name']} | {m.get('omniAcc'):.1f} | {m.get('omniHalluc'):.1f} |"

def row_agentic(m):
    return (
        f"| {m['name']} | {m.get('gdpvalNormalized'):.1f} | {m.get('lcr'):.1f} | "
        f"{m.get('hle'):.1f} | {m.get('gpqa'):.1f} | {m.get('scicode'):.1f} | {m.get('critpt'):.1f} |"
    )

def row_cost_speed(m):
    ec = m.get("evalCost")
    ec_s = f"{ec:.2f}" if isinstance(ec, (int, float)) else "—"
    return f"| {m['name']} | {ec_s} | {m.get('speed'):.1f} | {m.get('intelligenceIndex'):.1f} |"

def row_cost_comp(m):
    aa = m.get("aaCostNorm")
    ds = m.get("deepSweCostNorm")
    cc = m.get("costComposite")
    aa_s = f"{aa:.2f}" if isinstance(aa, (int, float)) else "—"
    return f"| {m['name']} | {aa_s} | {ds:.2f} | {cc:.2f} |"

aa_variants = "\n".join(
    f"- `{m['name']}` → [`{m['aaSlug']}`]({m['aaUrl']})" for m in all_for_tables
)

excl_note = ""
if excl:
    excl_note = (
        f"\n\n## Non-ranked DeepSWE appendix\n\n"
        f"**{excl['name']}** is preserved for transparency but **not scored** in {VERSION}:\n\n"
        f"- DeepSWE pass@1 = {excl['deepswePassAt1']}, avg cost/task = ${excl['deepsweCost']:.2f}\n"
        f"- AA Index = {excl.get('intelligenceIndex')}, speed = {excl.get('speed')} tok/s\n"
        f"- AA Index total eval cost = **unpublished** ([search](.refresh/v1.3/aa-kimi-k27-cost-search.md))\n"
        f"- Exclusion reason: {excl.get('exclusionReason')}\n"
    )

dropped = manifest["droppedDimensions"]
drop_rows = "\n".join(
    f"| {d['label']} | {', '.join(d['missing'])} |" for d in dropped
)

raw = f"""# ValueRank {VERSION} Raw Data
**Version:** {VERSION}
**Updated:** {DATE}

{VERSION} ranks **n={n}** models from the DeepSWE Best roster (roster has 18; **Kimi K2.7 Code** excluded from ranking). Dimensions without full ranked-cohort coverage are excluded (zero-gap). Cost uses the **AA Index total eval cost + DeepSWE avg cost** composite.

## Primary Sources
- [DeepSWE](https://deepswe.datacurve.ai/) for `DeepSWE pass@1` and `DeepSWE Avg Cost ($)` (Best / max-effort row per family; source updated July 25, 2026)
- Artificial Analysis model pages for retained AA dimensions (see evidence ledger under `.refresh/v1.3/`)

## Artificial Analysis variant selection
Per family, the AA model-page variant with the most complete coverage of **retained** dimensions is used:
{aa_variants}

## DeepSWE

| Model | Effort | DeepSWE pass@1 | DeepSWE Avg Cost ($) |
|---|---|---:|---:|
{chr(10).join(row_deepswe(m) for m in all_for_tables)}

## AA-Omniscience

| Model | Accuracy | Hallucination Rate |
|---|---:|---:|
{chr(10).join(row_omni(m) for m in all_for_tables)}

## Agentic / reasoning benchmarks (retained)

| Model | GDPval-AA | AA-LCR | HLE | GPQA | SciCode | CritPt |
|---|---:|---:|---:|---:|---:|---:|
{chr(10).join(row_agentic(m) for m in all_for_tables)}

## Cost & speed (AA)

| Model | Eval Cost ($) | Speed (tok/s) | AA Index |
|---|---:|---:|---:|
{chr(10).join(row_cost_speed(m) for m in all_for_tables)}
{excl_note}
## Cost construction (AA+DeepSWE composite)

For ranked models: normalize AA eval cost and DeepSWE avg cost to 0–100 (max in ranked cohort = 100), then average.

| Model | AA Cost (0-100) | DeepSWE Cost (0-100) | Composite Cost (0-100) |
|---|---:|---:|---:|
{chr(10).join(row_cost_comp(m) for m in models)}

## Dropped dimensions (incomplete coverage)

Re-checked after excluding Kimi K2.7 Code — IFBench / Terminal-Bench Hard / τ² still miss other newest models, so they stay dropped.

| Dimension | Models missing |
|---|---|
{drop_rows}

## Official-first excluded benchmark audit

Re-checked against the n={n} ranked cohort (DeepSWE Best minus Kimi K2.7 Code). A benchmark remains excluded unless a currently published implementation contains **all {n}** ranked models.

| Benchmark | Official source outcome | Best current secondary outcome |
|---|---|---|
| APEX-Agents | [Mercor APEX-Agents](https://www.mercor.com/apex/apex-agents-leaderboard/) does not cover the expanded July 2026 DeepSWE cohort (missing multiple new models including Claude Opus 5, GPT-5.6 family, Kimi K3, Grok 4.5, Muse Spark, etc.) | [AA APEX-Agents-AA](https://artificialanalysis.ai/evaluations/apex-agents-aa) still incomplete for n={n} |
| ITBench | [IBM ITBench Kaggle](https://www.kaggle.com/benchmarks/ibm-research/itbench) lacks exact ValueRank cohort names | [AA ITBench-AA](https://artificialanalysis.ai/evaluations/itbench-aa) incomplete |
| MMMU-Pro | [MMMU site](https://mmmu-benchmark.github.io/) is paper-era / incomplete for current cohort | [AA MMMU-Pro](https://artificialanalysis.ai/evaluations/mmmu-pro) incomplete |
| MMLU-Pro | [TIGER-Lab MMLU-Pro](https://huggingface.co/spaces/TIGER-Lab/MMLU-Pro) incomplete for current cohort | Kaggle / LLM Stats incomplete |
| LiveCodeBench | [LiveCodeBench](https://livecodebench.github.io/) paper-era leaderboard incomplete | AA / Kaggle / LLM Stats incomplete |
| Global-MMLU-Lite | [Cohere Labs Kaggle](https://www.kaggle.com/benchmarks/cohere-labs/global-mmlu-lite) incomplete | Secondary incomplete |
| AIME 2025 | Owner publishes exam, not full frontier leaderboard | AA / Kaggle incomplete for n={n} |
| MATH-500 | Owner publishes dataset, not full frontier leaderboard | Kaggle incomplete for n={n} |
"""
(ROOT / "raw-data.md").write_text(raw)

# Legacy v4 documents live under archive/value-rank-v4/ and are intentionally
# not regenerated by the current v1.3.1 pipeline.

# ── site/index.html ─────────────────────────────────────────────
site = ROOT / "site" / "index.html"
html = site.read_text()

site_models = []
for m in models:
    dims = [m["dims"][w["key"]] for w in weights]
    site_models.append(
        {
            "rank": m["rank"],
            "name": m["name"],
            "shortName": m["shortName"],
            "developer": m["developer"],
            "evalCost": m["costComposite"],
            "aaEvalCost": round(m["evalCost"], 2) if m.get("evalCost") is not None else None,
            "deepSweCost": m["deepsweCost"],
            "aaCostNorm": m["aaCostNorm"],
            "deepSweCostNorm": m["deepSweCostNorm"],
            "overallScore": m["overallScore"],
            "qualityScore": m["qualityScore"],
            "qualityRank": m["qualityRank"],
            "missingCount": 0,
            "dims": dims,
            "isMissing": [False] * len(dims),
            "vRanks": {
                "v70": None,
                "v80": None,
                "v90": None,
                "v100": None,
                "v110": None,
                "v120": None,
                "v130": None,
                "v131": m["rank"],
            },
        }
    )

# Compact JS object literal (match existing style: unquoted keys where possible)
def js_val(v):
    if v is None:
        return "null"
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, (int, float)):
        return str(v)
    if isinstance(v, str):
        return json.dumps(v)
    if isinstance(v, list):
        return "[" + ",".join(js_val(x) for x in v) + "]"
    if isinstance(v, dict):
        parts = []
        for k, val in v.items():
            parts.append(f"{k}:{js_val(val)}")
        return "{" + ",".join(parts) + "}"
    return json.dumps(v)

models_js = "[\n" + ",\n".join("  " + js_val(m) for m in site_models) + "\n]"

html2, nsub = re.subn(
    r"const MODELS\s*=\s*\[[\s\S]*?\];",
    "const MODELS = " + models_js + ";",
    html,
    count=1,
)
if nsub != 1:
    raise SystemExit(f"MODELS replace failed: {nsub}")

# DIM_WEIGHTS
weights_js = "[" + ", ".join(str(w["weight"]) for w in weights) + "]"
html2, nsub = re.subn(
    r"const DIM_WEIGHTS\s*=\s*\[[^\]]*\];",
    f"const DIM_WEIGHTS = {weights_js};",
    html2,
    count=1,
)
if nsub != 1:
    raise SystemExit(f"DIM_WEIGHTS replace failed: {nsub}")

# Version / n models string replacements
repls = [
    (r'content="Frontier models ranked on real-world value\.[^"]*"',
     f'content="Frontier models ranked on real-world value. ValueRank {VERSION} · {n} models from Artificial Analysis & DeepSWE Best."'),
    (r'content="Independent rankings from Artificial Analysis[^"]*"',
     f'content="Independent rankings from Artificial Analysis & DeepSWE. ValueRank {VERSION} · {n} models."'),
    (r'<span class="badge">v1\.3(?:\.1)?</span>',
     f'<span class="badge">{VERSION}</span>'),
    (r'<div class="nav-meta">July 28, 2026 · \d+ models · \d+ dimensions</div>',
     f'<div class="nav-meta">{DATE} · {n} models · {d} dimensions</div>'),
    (r'Production AI Ranking Framework · v1\.3(?:\.1)?',
     f'Production AI Ranking Framework · {VERSION}'),
]

for pat, rep in repls:
    html2, c = re.subn(pat, rep, html2)
    # allow multiple for meta descriptions
    if c == 0 and "content=" not in pat:
        print(f"WARN: no match for {pat}")

# Hero paragraph
hero_new = (
    f'ValueRank ranks <strong>{n} DeepSWE Best models</strong> across a '
    f'<strong>zero-gap {d}-dimension set</strong>. {VERSION} <strong>excludes Kimi K2.7 Code</strong> '
    f'from the ranked cohort (no published AA Index total eval cost — '
    f'<a href="https://artificialanalysis.ai/models/kimi-k2-7-code">AA model page</a>), '
    f'restores <strong>AA+DeepSWE composite Cost</strong>, and still '
    f'<strong>drops IFBench / Terminal-Bench Hard / τ²-Bench</strong> for incomplete AA coverage on other newest models.'
)
html2, c = re.subn(
    r"ValueRank now ranks[\s\S]*?Kimi K2\.7 Code\.",
    hero_new,
    html2,
    count=1,
)
if c != 1:
    # try alternate hero already partially edited
    html2, c2 = re.subn(
        r"ValueRank (?:now )?ranks[\s\S]{20,800}?Kimi K2\.7 Code[^.]*\.",
        hero_new,
        html2,
        count=1,
    )
    if c2 != 1:
        print(f"WARN: hero replace count={c}/{c2}")

# Methodology body snippets that still say DeepSWE-only / 18 models
html2 = html2.replace(
    "All 18 models × 1",
    f"All {n} models × 1",
)
html2 = html2.replace(
    "all 18 models are ranked",
    f"all {n} models are ranked",
)
html2 = html2.replace(
    "v1.3 expands the cohort to <strong>18 DeepSWE Best",
    f"{VERSION} ranks <strong>{n} DeepSWE Best",
)
# Version string updates — word-boundary only; never touch v130/v131 object keys
html2 = re.sub(r"\bv1\.3\b(?!\.\d)", VERSION, html2)

# Cost methodology section — restore composite language
html2 = re.sub(
    r"DeepSWE-only Cost</strong> because AA Index total eval cost is unpublished for Kimi K2\.7 Code\.",
    "AA+DeepSWE composite Cost</strong> (Kimi K2.7 Code excluded from ranking — no AA Index total eval cost).",
    html2,
)
html2 = re.sub(
    r"uses <strong>DeepSWE-only Cost</strong>[^<]*",
    "uses <strong>AA+DeepSWE composite Cost</strong>. ",
    html2,
)

# Insight cards — light refresh for top story
q1 = sorted(models, key=lambda x: x["qualityRank"])[0]
pareto_n = len(pareto)
insight_pareto = (
    f'The Pareto frontier is a <strong>{pareto_n}-model</strong> set undominated on composite cost vs quality: '
    + ", ".join(pareto)
    + "."
)
# Replace first insight-body about Pareto if present
html2 = re.sub(
    r'(<div class="insight-body">)The Pareto frontier is a <strong>\d+-model</strong>[\s\S]*?</div>',
    r"\1" + insight_pareto + "</div>",
    html2,
    count=1,
)

# Seal note
html2 = re.sub(
    r'v1\.3(?:\.1)? uses zero missing benchmark cells',
    f'{VERSION} uses zero missing benchmark cells',
    html2,
)

site.write_text(html2)

# Annotate kimi search doc with decision
kimi_path = R / "aa-kimi-k27-cost-search.md"
kimi = kimi_path.read_text()
decision = (
    "\n---\n\n## Decision ({DATE} — ValueRank {VERSION})\n\n"
    "**User decision:** Exclude **Kimi K2.7 Code** from the ranked cohort rather than keep "
    "DeepSWE-only Cost for all models. Cost construction restored to AA+DeepSWE composite for "
    f"**n={n}**. This search verdict (NOT FOUND) remains the evidence for the exclusion.\n"
)
if "## Decision" not in kimi:
    kimi_path.write_text(kimi.rstrip() + decision)

print(f"Emitted {VERSION}: n={n} d={d} costMode={models[0]['costMode']}")
print("TOP5:", [(m["rank"], m["name"], m["overallScore"]) for m in models[:5]])
print("PARETO:", pareto)
print("site MODELS patched; methodology/scores/README/raw-data updated")
