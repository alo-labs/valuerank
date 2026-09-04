#!/usr/bin/env python3
"""Emit the v1.4.0 README, methodology, score tables, raw data, and site.

The site keeps the existing interactive publication shell, but all ranking
constants and model data are generated from .refresh/v1.4/scores.json.
"""

from __future__ import annotations

import json
import re
import sys
from html import escape as html_escape
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REFRESH = ROOT / ".refresh" / "v1.4"
RESEARCH = ROOT / "research" / "2026-09-04-valuerank-refresh"
sys.path.insert(0, str(ROOT / "scripts"))
from site_header import inject_header

VERSION = "v1.4.0"
DATE = "September 5, 2026"
CURRENCY = "$"

scores = json.loads((REFRESH / "scores.json").read_text())
coverage_document = json.loads((REFRESH / "coverage_matrix.json").read_text())
livebench_document = json.loads((REFRESH / "livebench.json").read_text())
tb4_document = json.loads((REFRESH / "tb4.json").read_text())
manifest = json.loads((RESEARCH / "run_manifest.json").read_text())
models = scores["models"]
weights = scores["weights"]
n = len(models)
d = len(weights)
pareto = scores["pareto"]
model_by_id = {model["id"]: model for model in models}
livebench_rows = [record for record in livebench_document["models"].values() if record.get("matched")]
livebench_pareto = [livebench_document["models"][model_id] for model_id in livebench_document["pareto"]]
tb4_rows = tb4_document["rows"]
deepswe_updated = scores["cohort"].get("sourceUpdatedOn") or "September 3, 2026"
aa_version = scores.get("benchmarkVersion") or "Artificial Analysis Intelligence Index v4.1.1"
dropped = manifest.get("scoring", {}).get("droppedDimensions", [])


def fnum(value, places=2, dash="—"):
    return f"{value:.{places}f}" if isinstance(value, (int, float)) else dash


def pct(value, places=2):
    return f"{value * 100:.{places}f}%" if isinstance(value, (int, float)) else "—"


def names(values):
    return ", ".join(values) if values else "none"


livebench_pareto_text = names([record["name"] for record in livebench_pareto]) if livebench_pareto else "none"


def primary_rows():
    return "\n".join(
        f"| {model['rank']} | {model['name']} | {model['overallScore']:.1f} | {model['qualityScore']:.1f} | {model['costComposite']:.2f} |"
        for model in models
    )


def dimension_table():
    return "\n".join(
        f"| {index} | {weight['label']} | {weight['weightPct']:.2f}% | {'higher' if weight['higherBetter'] else 'lower'} |"
        for index, weight in enumerate(weights, 1)
    )


def livebench_table():
    return "\n".join(
        f"| {record['name']} | {record['livebenchModel']} | {record['instructionFollowingScore']:.2f} | {record['overallScore']:.2f} | ${record['costPerSuccessfulTaskUsd']:.4f} |"
        for record in livebench_rows
    )


def tb4_table():
    return "\n".join(
        f"| {entry['rankLabel']} | {entry['baseModel']} | {entry['agent']} | {entry['resolutionRatePct']:.1f}% ± {entry['uncertaintyPct']:.1f}% | {entry['tokens']} | ${entry['costUsd']:,.0f} |"
        for entry in tb4_rows
    )


pareto_text = names(pareto)
drop_text = "\n".join(
    f"| {item['label']} | {names(item['missing'])} | {item['reason']} |" for item in dropped
) or "| None | — | All candidate dimensions have complete coverage. |"

readme = f"""# ValueRank
**Frontier AI model ranking focused on production value**

**Version:** {VERSION}
**Updated:** {DATE}
**Scope:** {n} models from the current DeepSWE Best roster, {d} retained zero-gap dimensions

## Current result

ValueRank combines current DeepSWE agent performance with Artificial Analysis Intelligence Index v4.1.1 component results and a two-source cost penalty. The complete current DeepSWE Best roster is retained; no missing cell is filled with a neutral value. LiveBench Instruction Following and Terminal-Bench 4.0 are published alongside the score as separately sourced coverage-only views until their official coverage is complete for this cohort.

| Rank | Model | Overall | Quality | Composite Cost |
|---:|---|---:|---:|---:|
{primary_rows()}

The current Pareto frontier—undominated on composite cost versus quality—is: **{pareto_text}**.

## What changed in v1.4

- DeepSWE is refreshed to the live v1.1 Best page: **{n} models**, **113 tasks**, source updated **{deepswe_updated}**.
- Artificial Analysis is migrated to the current **{aa_version}** identity: GDPval-AA v2, τ³-Banking, its source Terminal-Bench v2.1 component, SciCode, AA-LCR, HLE, GPQA Diamond, CritPt, and split AA-Omniscience accuracy/non-hallucination components.
- The standalone Terminal-Bench view is replaced by the official **Terminal-Bench 4.0** snapshot: **{tb4_document['rowN']} rows**, with **{tb4_document['matchedN']}/{tb4_document['cohortN']}** overlap with the ranked cohort.
- **LiveBench {livebench_document['release'].replace('_', '-')}** supplies the Instruction Following component and Overall-vs-Cost view: **{livebench_document['matchedN']}/{livebench_document['cohortN']}** cohort rows matched; the current LiveBench Pareto frontier is **{livebench_pareto_text}**.
- The ranked pool is **{n} models**, with all current DeepSWE entries preserved.
- The score retains **{d} zero-gap dimensions**; **{names([item['label'] for item in dropped])}** are excluded because each has incomplete official cohort coverage. Missing external values remain null and are not neutral-filled.
- Speed remains an auditable coverage field (20/{n} AA pages publish a numeric value) but is not imputed into the primary score because GPT-6 Astra's selected page reports N/A.
- Legacy v1.3.1 values are not numerically comparable: the AA benchmark identities and the DeepSWE cohort have changed.

## Sources and audit trail

- [DeepSWE Best](https://deepswe.datacurve.ai/) for pass@1, uncertainty, average cost, output tokens, and agent steps.
- [Artificial Analysis methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) and the linked first-party model pages for current component values and Intelligence Index evaluation cost.
- [LiveBench](https://livebench.ai/) and its [official release data repository](https://github.com/livebench/new-livebench) for the pinned 2026-06-25 task/category table, Instruction Following means, Overall Score, and Cost Per Successful Task.
- [Terminal-Bench 4.0](https://www.tbench.ai/) and the [official Harbor repository](https://github.com/harbor-framework/terminal-bench) for the current rendered leaderboard and task identity.
- [Research report](research/2026-09-04-valuerank-refresh/research_report.md) for the source ledger, evidence spans, triangulation, critique cycles, and decisions.
- [Coverage matrix](.refresh/v1.4/coverage_matrix.json) for primary and supplemental availability, including fields not used in the score.

## Files

- [scores.md](scores.md): final ranking, weights, and normalized matrix
- [raw-data.md](raw-data.md): source values, selected AA variants, and supplemental coverage
- [methodology.md](methodology.md): cohort, benchmark versions, normalization, and zero-gap rule
- [site/index.html](site/index.html): interactive static publication
- [site/tb4/index.html](site/tb4/index.html): current Terminal-Bench 4.0 score-versus-cost publication
- [research/2026-09-04-valuerank-refresh/](research/2026-09-04-valuerank-refresh/): reproducible research package
- [.refresh/v1.4/](.refresh/v1.4/): refresh scripts and machine-readable snapshots/outputs
"""
(ROOT / "README.md").write_text(readme)

methodology = f"""# ValueRank Methodology

**Version:** {VERSION}
**Updated:** {DATE}

## Cohort and source versions

The ranked cohort is the complete **{n}-model current DeepSWE Best roster**. Each model is represented by the Best-page effort row shown by DeepSWE; all {n} rows have pass@1, uncertainty, average cost, output-token, and agent-step values.

- DeepSWE source: [live leaderboard](https://deepswe.datacurve.ai/), v1.1, 113 tasks, updated {deepswe_updated}.
- AA source: [Intelligence Index methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking), current {aa_version}.
- AA model values: one first-party model page per DeepSWE family, with the effort-specific URL selected by .refresh/v1.4/aa_mapping.json and recorded in aa_metrics.json.
- LiveBench source: [livebench.ai](https://livebench.ai/), pinned release **2026-06-25** with seven categories, including the four-task Instruction Following category and published Cost Per Successful Task values.
- Terminal-Bench source: [tbench.ai](https://www.tbench.ai/), current **4.0** rendered leaderboard snapshot with {tb4_document['rowN']} official rows.

The old v1.3.1 publication used an earlier cohort and older AA benchmark identities. It remains historical; its numerical scores must not be compared directly with v1.4.0.

## Primary dimensions

The score retains only dimensions with a genuine value for every one of the {n} ranked models. Values are stored as raw fractions in scores.json, then converted to rank scores.

| # | Dimension | ValueRank weight | Direction |
|---:|---|---:|---|
{dimension_table()}

The ten AA component entries below correspond to the nine current AA evaluations because Omniscience is split into accuracy and non-hallucination reliability:

| AA evaluation/component | Current methodology weight |
|---|---:|
| GDPval-AA v2 | 20% |
| τ³-Banking | 14% |
| AA source Terminal-Bench v2.1 | 16% |
| SciCode | 8% |
| AA-LCR | 6% |
| Humanity's Last Exam | 12% |
| GPQA Diamond | 6% |
| CritPt | 6% |
| AA-Omniscience Accuracy | 8% |
| AA-Omniscience Non-Hallucination Rate | 4% |

These AA methodology weights describe the source index, not the combined ValueRank weights above. ValueRank adds DeepSWE, cost, and AA Index signals using the explicitly published priority table.

## Zero-gap rule

- A candidate dimension is scored only when all {n} models have a published value.
- Missing values remain null in aa_metrics.json and are listed in coverage_matrix.json.
- No neutral 50, median, model-family, or legacy-version substitution is used.
- In v1.4.0, **Speed is dropped from the primary score** because the selected GPT-6 Astra AA page reports N/A. Numeric speed values for the other 20 models remain in raw data and the coverage matrix.
- LiveBench Instruction Following is available for **{livebench_document['matchedN']}/{livebench_document['cohortN']}** cohort models, and Terminal-Bench 4.0 is available for **{tb4_document['matchedN']}/{tb4_document['cohortN']}**. Both are retained as null-safe coverage fields and visualized separately; neither is weighted into the primary score until it satisfies the zero-gap rule.

Dropped candidate dimensions:

| Dimension | Missing models | Decision |
|---|---|---|
{drop_text}

## Rank normalization

For each retained dimension, models are ranked from best to worst and mapped with:

((n - rank) / (n - 1)) × 100

Rank 1 maps to 100, rank {n} maps to 0, and exact ties receive the average tied rank. Lower-is-better dimensions, including composite Cost, reverse the ordering before normalization.

## Cost construction

The Cost input is an average of two independently observed penalties:

1. AA Intelligence Index total evaluation cost, normalized against the highest current cohort cost.
2. DeepSWE Best average cost per task, normalized against the highest current cohort cost.
3. The two 0–100 penalties are averaged into costComposite.
4. costComposite is rank-normalized with lower cost better.

This avoids treating a single vendor's price surface as the whole production-cost story while keeping the two source quantities visible in every score row.

## Quality score and interpretation

Overall Score is the weighted sum of all retained dimensions. Quality Score removes Cost and renormalizes the remaining retained dimensions to 100%. Scores are rank-relative to this cohort, not probabilities and not an absolute model capability scale.

## Supplemental data

Artificial Analysis exposes additional evaluations—such as MLCR, Harvey, APEX-Agents, MMMU-Pro, AutomationBench, EnterpriseOpsGym, ITBench SRE, Briefcase, and other legacy/current fields. They are preserved in aa_metrics.json when published, and their coverage is reported in coverage_matrix.json, but they are not added to the primary score when incomplete or outside the current v4.1.1 index definition. The AA source payload still records its own v2.1 component for provenance; the standalone current Terminal-Bench publication is TB4.

LiveBench is incorporated as the current external Instruction Following source. Its four official task values—paraphrase, simplify, story_generation, and summarize—are averaged into the published Instruction Following value; LiveBench Overall is the mean of its seven category means. The LiveBench chart uses the official Overall Score against the official Cost Per Successful Task for the 20 matched cohort rows.

Terminal-Bench 4.0 is incorporated as the current external terminal-agent source. The standalone page shows all 14 official rows and the current cohort overlap, while the ValueRank score keeps the field coverage-only because 10 of the 21 ranked models are not present in the pinned TB4 table.

## Limitations

- DeepSWE and AA measure different tasks, harnesses, and sampling procedures; this is a transparent synthesis, not a new benchmark.
- Rank normalization discards magnitude differences and should be read with the raw values and uncertainty fields.
- Page variants can differ by reasoning effort; the selected URL and variant are recorded per model.
- Speed is intentionally coverage-only in this release because one current page has N/A.
- LiveBench and Terminal-Bench have different task suites and release surfaces from the AA source component; their displayed values should not be substituted for one another or read as a continuous version-to-version series.
"""
(ROOT / "methodology.md").write_text(methodology)

def norm_values(model):
    return ", ".join(f"{model['dims'][weight['key']]:.1f}" for weight in weights)


norm_rows = "\n".join(
    f"| {model['rank']} | {model['name']} | [{norm_values(model)}] |"
    for model in models
)
scores_md = f"""# ValueRank {VERSION} Scores

**Updated:** {DATE} · **Cohort:** {n} · **Retained dimensions:** {d} · **Cost mode:** AA + DeepSWE

## Final ranking

| Rank | Model | Overall | Quality | Quality Rank | Composite Cost |
|---:|---|---:|---:|---:|---:|
{chr(10).join(f"| {m['rank']} | {m['name']} | {m['overallScore']:.1f} | {m['qualityScore']:.1f} | {m['qualityRank']} | {m['costComposite']:.2f} |" for m in models)}

## Pareto frontier

Undominated on composite cost versus quality: **{pareto_text}**.

## Weights

| Dimension | Weight | Direction |
|---|---:|---|
{chr(10).join(f"| {w['label']} | {w['weightPct']:.2f}% | {'higher' if w['higherBetter'] else 'lower'} |" for w in weights)}

## Normalized dimension matrix

Dimension order is the order in weights above:

[{', '.join(w['key'] for w in weights)}]

| Rank | Model | Normalized dimensions |
|---:|---|---|
{norm_rows}

## Coverage decision

The score is zero-gap across all retained dimensions. The dropped candidate dimensions are listed below with their missing cohort rows; their values remain null rather than being replaced by a neutral score.

## External benchmark supplements

LiveBench provides the four-task Instruction Following view and the Overall Score versus Cost Per Successful Task Pareto analysis; Terminal-Bench 4.0 provides the current standalone terminal-agent leaderboard. Their incomplete cohort coverage keeps them supplemental rather than weighted into this zero-gap ranking. See [raw-data.md](raw-data.md) for the source-backed tables.
"""
(ROOT / "scores.md").write_text(scores_md)

aa_variant_rows = "\n".join(
    f"| {model['name']} | {model['aaSlug']} | {model['aaVariant'] or 'not stated'} | [page]({model['aaUrl']}) |"
    for model in models
)
raw_rows = "\n".join(
    f"| {model['rank']} | {model['name']} | {model['deepsweEffort']} | {model['deepswePassAt1Pct']:.1f}% ± {model['deepsweUncertaintyPct']:.1f}% | {CURRENCY}{model['deepsweCost']:.2f} | {pct(model['gdpvalV2'])} | {pct(model['tau3Banking'])} | {pct(model.get('aaTerminalBenchV21'))} | {pct(model['scicode'])} | {pct(model['aaLcr'])} | {pct(model['hle'])} | {pct(model['gpqaDiamond'])} | {pct(model['critpt'])} | {pct(model['omniAccuracy'])} | {pct(model['omniNonHallucination'])} | {fnum(model['intelligenceIndex'])} | {CURRENCY}{model['aaEvalCost']:.2f} | {fnum(model.get('speed'), 1)} |"
    for model in models
)
supplemental_rows = "\n".join(
    f"| {field} | {data.get('availableN', '—')}/{data.get('cohortN', n)} | {names(data.get('missingModels', []))} | {'Primary' if data.get('includedInPrimaryScore') else 'Supplemental / not scored'} |"
    for field, data in coverage_document.get("fields", {}).items()
    if data.get("group") == "supplemental"
)
livebench_raw_rows = livebench_table()
tb4_raw_rows = tb4_table()
raw_data = f"""# ValueRank {VERSION} Raw Data

**Version:** {VERSION} · **Updated:** {DATE} · **DeepSWE source update:** {deepswe_updated} · **AA source:** {aa_version}

All {n} current DeepSWE Best models are retained. Raw AA benchmark values are percentages below for readability; the machine-readable files preserve fractions. Speed is shown when published but is not part of the primary score because GPT-6 Astra is N/A. The external benchmark tables are kept separate from the AA source matrix so version identities remain unambiguous.

## Selected AA pages

| Model | AA slug | AA effort | Source |
|---|---|---|---|
{aa_variant_rows}

## AA source input matrix

| # | Model | Effort | DeepSWE pass@1 | DeepSWE avg cost | GDPval-AA v2 | τ³-Banking | AA Terminal-Bench v2.1 | SciCode | AA-LCR | HLE | GPQA | CritPt | Omni Accuracy | Omni Non-Hallucination | AA Index | AA eval cost | Speed tok/s |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
{raw_rows}

## LiveBench external component

LiveBench release **{livebench_document['release']}** supplies the four-task Instruction Following mean and its seven-category Overall Score. Cost is the official **Cost Per Successful Task** field. The pinned table matches **{livebench_document['matchedN']}/{livebench_document['cohortN']}** ranked models; GPT-6 Astra is unavailable in this release.

| Model | LiveBench variant | Instruction Following | Overall Score | Cost Per Successful Task |
|---|---|---:|---:|---:|
{livebench_raw_rows}

LiveBench Pareto frontier (Overall Score vs Cost Per Successful Task): **{livebench_pareto_text}**.

## Terminal-Bench 4.0 external component

The current official TB4 snapshot contains **{tb4_document['rowN']} rows** and overlaps **{tb4_document['matchedN']}/{tb4_document['cohortN']}** ranked models. It replaces the old standalone TB2.1 publication; the AA source matrix above keeps its v2.1 field only as explicit AA-source provenance.

| Rank | Model | Agent | Resolution rate | Tokens | Cost |
|---:|---|---|---:|---:|---:|
{tb4_raw_rows}

## Cost construction

| Model | AA cost penalty | DeepSWE cost penalty | Composite cost |
|---|---:|---:|---:|
{chr(10).join(f"| {m['name']} | {m['aaCostNorm']:.2f} | {m['deepSweCostNorm']:.2f} | {m['costComposite']:.2f} |" for m in models)}

## Supplemental Artificial Analysis coverage

These fields are preserved for future analysis but remain outside the primary score because they are incomplete across the current cohort or are not part of the current AA v4.1.1 weighted index. LiveBench and TB4 are external coverage-only components under the same no-imputation policy.

| Field | Available | Missing models | Role |
|---|---:|---|---|
{supplemental_rows}

## Dropped primary candidate

| Dimension | Missing model | Treatment |
|---|---|---|
{drop_text}

Missing values are intentionally represented as null; no old-version, model-family, median, or neutral-fill substitution is used.

## Machine-readable artifacts

- [.refresh/v1.4/deepswe.json](.refresh/v1.4/deepswe.json): current DeepSWE extraction
- [.refresh/v1.4/aa_metrics.json](.refresh/v1.4/aa_metrics.json): decoded current AA model payloads
- [.refresh/v1.4/scores.json](.refresh/v1.4/scores.json): normalized scores and rankings
- [.refresh/v1.4/coverage_matrix.json](.refresh/v1.4/coverage_matrix.json): primary and supplemental availability
- [.refresh/v1.4/livebench.json](.refresh/v1.4/livebench.json): pinned LiveBench task/category/cost snapshot and Pareto data
- [.refresh/v1.4/tb4.json](.refresh/v1.4/tb4.json): normalized official Terminal-Bench 4.0 rendered leaderboard
- [research/2026-09-04-valuerank-refresh/evidence.jsonl](research/2026-09-04-valuerank-refresh/evidence.jsonl): source/evidence ledger
"""
(ROOT / "raw-data.md").write_text(raw_data)


# Existing interactive publication shell. Data constants and model data are
# regenerated to prevent stale v1.3 UI.
site_path = ROOT / "site" / "index.html"
html = site_path.read_text()

weight_by_key = {weight["key"]: weight for weight in weights}
SITE_DIM_META = {
    "costComposite": ("costComposite", "Cost", "Composite Cost", "cost"),
    "omniNonHallucination": ("omniNonHallucination", "NonHalluc", "AA-Omniscience Non-Hallucination Rate", "rely"),
    "omniAccuracy": ("omniAccuracy", "OmniAcc", "AA-Omniscience Accuracy", "rely"),
    "terminalBenchV4": ("terminalBenchV4", "Terminal4", "Terminal-Bench 4.0", "code"),
    "livebenchInstructionFollowing": ("livebenchInstructionFollowing", "LiveBench IF", "Instruction Following (LiveBench)", "language"),
    "deepswePassAt1": ("deepswePassAt1", "DeepSWE", "DeepSWE pass@1", "code"),
    "gdpvalV2": ("gdpvalV2", "GDPv2", "GDPval-AA v2", "code"),
    "tau3Banking": ("tau3Banking", "Tau3", "τ³-Banking", "code"),
    "aaLcr": ("aaLcr", "LCR", "AA-LCR", "code"),
    "hle": ("hle", "HLE", "Humanity's Last Exam", "intel"),
    "gpqaDiamond": ("gpqaDiamond", "GPQA", "GPQA Diamond", "intel"),
    "scicode": ("scicode", "Sci", "SciCode", "intel"),
    "critpt": ("critpt", "CritPt", "CritPt", "intel"),
    "intelligenceIndex": ("intelligenceIndex", "AAI", "Artificial Analysis Intelligence Index", "prod"),
}
unknown_site_dims = [weight["key"] for weight in weights if weight["key"] not in SITE_DIM_META]
if unknown_site_dims:
    raise SystemExit(f"site dimension metadata missing: {unknown_site_dims}")
SITE_DIMS = [SITE_DIM_META[weight["key"]] for weight in weights]
site_models = []
for model in models:
    site_models.append({
        "rank": model["rank"],
        "name": model["name"],
        "shortName": model["shortName"],
        "developer": model["developer"],
        "evalCost": model["costComposite"],
        "aaEvalCost": round(model["aaEvalCost"], 2),
        "deepSweCost": model["deepsweCost"],
        "aaCostNorm": model["aaCostNorm"],
        "deepSweCostNorm": model["deepSweCostNorm"],
        "speed": model.get("speed"),
        "aaUrl": model["aaUrl"],
        "livebench": {
            "model": model.get("livebenchModel"),
            "overallScore": model.get("livebenchOverall"),
            "instructionFollowingScore": model.get("livebenchInstructionFollowing"),
            "costPerSuccessfulTaskUsd": model.get("livebenchCostPerSuccessfulTask"),
        },
        "terminalBenchV4": {
            "model": model.get("terminalBenchV4Model"),
            "resolutionRate": model.get("terminalBenchV4"),
            "resolutionRatePct": model.get("terminalBenchV4Pct"),
            "uncertaintyPct": model.get("terminalBenchV4UncertaintyPct"),
            "costUsd": model.get("terminalBenchV4Cost"),
            "agent": model.get("terminalBenchV4Agent"),
            "releaseDate": model.get("terminalBenchV4ReleaseDate"),
        },
        "overallScore": model["overallScore"],
        "qualityScore": model["qualityScore"],
        "qualityRank": model["qualityRank"],
        "missingCount": 0,
        "dims": [model["dims"][dim_key] for dim_key, _key, _full, _cat in SITE_DIMS],
        "isMissing": [False] * len(SITE_DIMS),
        "vRanks": {"v70": None, "v80": None, "v90": None, "v100": None, "v110": None, "v120": None, "v130": None, "v131": None, "v140": model["rank"]},
    })

site_livebench = [
    {
        "id": record["modelId"],
        "name": record["name"],
        "livebenchModel": record["livebenchModel"],
        "overallScore": record["overallScore"],
        "instructionFollowingScore": record["instructionFollowingScore"],
        "costPerSuccessfulTaskUsd": record["costPerSuccessfulTaskUsd"],
        "pareto": record["modelId"] in livebench_document["pareto"],
    }
    for record in livebench_rows
]
livebench_site_table_rows = "\n".join(
    f"<tr><td>{html_escape(record['name'])}</td><td class=\"mono\">{html_escape(record['livebenchModel'])}</td><td class=\"mono\">{record['instructionFollowingScore']:.2f}</td><td class=\"mono\">{record['overallScore']:.2f}</td><td class=\"mono\">${record['costPerSuccessfulTaskUsd']:.4f}</td><td>{'Frontier' if record['modelId'] in livebench_document['pareto'] else '—'}</td></tr>"
    for record in livebench_rows
)

def replace_once(source, pattern, replacement, label):
    result, count = re.subn(pattern, replacement, source, count=1)
    if count != 1:
        if label in {"heatmap column order", "heatmap category labels"} and count == 0:
            return source
        if label == "date stat" and re.search(r'<span class="hero-statbar-num">Sep \d+</span>', source):
            return source
        raise SystemExit(f"{label} replacement failed: {count}")
    return result

html = replace_once(html, r"const DIM_KEYS\s*=\s*\[[^\]]*\];", "const DIM_KEYS = " + json.dumps([item[1] for item in SITE_DIMS], ensure_ascii=False) + ";", "DIM_KEYS")
html = replace_once(html, r"const DIM_FULL\s*=\s*\[[^\]]*\];", "const DIM_FULL = " + json.dumps([item[2] for item in SITE_DIMS], ensure_ascii=False) + ";", "DIM_FULL")
html = replace_once(html, r"const DIM_WEIGHTS\s*=\s*\[[^\]]*\];", "const DIM_WEIGHTS = " + json.dumps([weight_by_key[item[0]]["weightPct"] for item in SITE_DIMS]) + ";", "DIM_WEIGHTS")
html = replace_once(html, r"const DIM_CAT\s*=\s*\[[^\]]*\];", "const DIM_CAT = " + json.dumps([item[3] for item in SITE_DIMS]) + ";", "DIM_CAT")
macro_labels = {
    "cost": ("Cost", "#22c55e"),
    "rely": ("Reliability", "#a78bfa"),
    "code": ("Agentic", "#3b82f6"),
    "intel": ("Intelligence", "#eab308"),
    "prod": ("Platform", "#f97316"),
    "language": ("Language", "#ec4899"),
}
macro_defs = []
for category, (label, color) in macro_labels.items():
    indices = [index for index, item in enumerate(SITE_DIMS) if item[3] == category]
    if indices:
        macro_defs.append({"key": category, "label": label, "color": color, "dimIdxs": indices})
macro = "const MACRO_CATS = " + json.dumps(macro_defs, ensure_ascii=False) + ";"
html = replace_once(html, r"const MACRO_CATS\s*=\s*\[[\s\S]*?\];", macro, "MACRO_CATS")
html = replace_once(
    html,
    r"const MODELS\s*=\s*\[[\s\S]*?\];(?:\s*const LIVEBENCH\s*=\s*\[[\s\S]*?\];)?",
    "const MODELS = " + json.dumps(site_models, ensure_ascii=False, indent=2) + ";\n\nconst LIVEBENCH = " + json.dumps(site_livebench, ensure_ascii=False, indent=2) + ";",
    "MODELS",
)
html = replace_once(html, r"const SPEED_DIM_IDX\s*=\s*[^;]+;", "const SPEED_DIM_IDX = -1; // speed is coverage-only in v1.4.0; GPT-6 Astra reports N/A", "SPEED_DIM_IDX")

html = replace_once(
    html,
    r"  // Column order:[\s\S]*?  const z\s*=",
    "  // Column order follows generated Cost | Reliability | Agentic | Intelligence | Platform groups.\n  const colOrder = DIM_KEYS.map((_, i) => i);\n  const colLabels = colOrder.map(i => DIM_KEYS[i]);\n  const colFull   = colOrder.map(i => DIM_FULL[i]);\n  const colWeights= colOrder.map(i => DIM_WEIGHTS[i]);\n\n  const z =",
    "heatmap column order",
)
divider_values = []
for index in range(1, len(SITE_DIMS)):
    if SITE_DIMS[index][3] != SITE_DIMS[index - 1][3]:
        divider_values.append(index - 0.5)
html = replace_once(html, r"  const dividers = \[[^\]]*\];", "  const dividers = " + json.dumps(divider_values) + ";", "heatmap dividers")
cat_positions = []
for category, (label, color) in macro_labels.items():
    indices = [index for index, item in enumerate(SITE_DIMS) if item[3] == category]
    if indices:
        cat_positions.append({"x": sum(indices) / len(indices), "text": label, "color": color, "y": -0.08})
cat_labels_js = "  const catLabels = " + json.dumps(cat_positions, ensure_ascii=False) + ";\n\n  const catAnnotations"
html = replace_once(
    html,
    r"  const catLabels = \[[\s\S]*?  \];\n\n  const catAnnotations",
    cat_labels_js,
    "heatmap category labels",
)

speed_function = r"""function renderBubble() {
  const bubbleModels = MODELS.filter(m => Number.isFinite(Number(m.speed)));
  const target = document.getElementById('chart-bubble');
  if (!bubbleModels.length) {
    target.innerHTML = '<div class="ca-dash" style="padding:32px;text-align:center;">No numeric speed values are available for this cohort.</div>';
    return;
  }
  const speeds = bubbleModels.map(m => Number(m.speed));
  const minSpeed = Math.min(...speeds);
  const maxSpeed = Math.max(...speeds);
  const speedScore = m => ((Number(m.speed) - minSpeed) / ((maxSpeed - minSpeed) || 1)) * 100;
  const maxCost = Math.max(...MODELS.map(m => m.evalCost));
  const traces = bubbleModels.map(m => ({
    x:[speedScore(m)], y:[m.qualityScore],
    mode:'markers', name:m.shortName,
    marker:{size:10 + (m.evalCost / maxCost) * 30, color:TIER_COLORS[m.costTier] || '#64748b', opacity:0.8, line:{color:'rgba(255,255,255,0.15)',width:1}},
    hovertemplate:'<b>' + m.name + '</b><br>Speed: ' + Number(m.speed).toFixed(1) + ' tok/s<br>Speed percentile score: ' + speedScore(m).toFixed(1) + '<br>Quality: ' + m.qualityScore.toFixed(1) + '<br>Composite Cost: ' + m.evalCost.toFixed(1) + '<br>' + fmtAaDeepSweHover(m) + '<extra></extra>',
    showlegend:false
  }));
  const layout = {
    ...getPlotlyLayout(),
    title:{text:'Speed × Quality × Cost (numeric AA speed only)', font:plotlyTitle(14)},
    xaxis:{...getPlotlyLayout().xaxis, title:'Speed percentile (' + minSpeed.toFixed(1) + '–' + maxSpeed.toFixed(1) + ' tok/s)', range:[-5,105]},
    yaxis:{...getPlotlyLayout().yaxis, title:'Quality Sub-Score', range:[25,80]},
    shapes:[
      {type:'line', x0:50, x1:50, y0:25, y1:80, line:{color:plotlyDim(),dash:'dot',width:1.5}},
      {type:'line', x0:-5, x1:105, y0:50, y1:50, line:{color:plotlyDim(),dash:'dot',width:1.5}},
    ],
    annotations:[
      {x:25, y:78, xref:'x', yref:'y', text:'Slow, High Quality', font:{color:'#6b7280',size:9}, showarrow:false},
      {x:80, y:78, xref:'x', yref:'y', text:'<b>Production Sweet Spot</b>', font:{color:'#22c55e',size:9}, showarrow:false},
      {x:80, y:32, xref:'x', yref:'y', text:'Fast & Cheap', font:{color:'#6b7280',size:9}, showarrow:false},
      {x:25, y:32, xref:'x', yref:'y', text:'Avoid', font:{color:'#6b7280',size:9}, showarrow:false},
    ]
  };
  Plotly.newPlot('chart-bubble', traces, layout, PLOTLY_CONFIG).then(() => {
    const gd = document.getElementById('chart-bubble');
    const modelAnnotations = buildCollisionSafeLabelAnnotations(
      bubbleModels.map(m => ({ id: m.name, label: m.shortName, x: speedScore(m), y: m.qualityScore })),
      gd,
      { fontSize: 9, markerRadius: 24, safety: 1.35 },
    );
    const annotations = [...(layout.annotations || []), ...modelAnnotations];
    return Plotly.relayout(gd, { annotations }).then(() => repairCollisionSafeLabelAnnotations(gd, modelAnnotations));
  });
}
"""
html = replace_once(html, r"function renderBubble\(\) \{[\s\S]*?\n\}\n\n// ─+\n// CHART 6", speed_function + "\n// ─────────────────────────────────────────────\n// CHART 6", "speed chart")

livebench_function = r"""function renderLiveBenchPareto() {
  const rows = LIVEBENCH.filter(m => Number.isFinite(Number(m.overallScore)) && Number.isFinite(Number(m.costPerSuccessfulTaskUsd)));
  const target = document.getElementById('chart-livebench-pareto');
  if (!rows.length) {
    target.innerHTML = '<div class="ca-dash" style="padding:32px;text-align:center;">No matched LiveBench rows are available.</div>';
    return;
  }
  const frontier = rows.filter(m => m.pareto).sort((a, b) => a.costPerSuccessfulTaskUsd - b.costPerSuccessfulTaskUsd);
  const frontierSet = new Set(frontier.map(m => m.id));
  const dominated = rows.filter(m => !frontierSet.has(m.id));
  const custom = m => [m.name, m.livebenchModel, m.instructionFollowingScore, m.costPerSuccessfulTaskUsd];
  const hover = '<b>%{customdata[0]}</b><br>Overall Score: %{y:.2f}<br>Instruction Following: %{customdata[2]:.2f}<br>Cost Per Successful Task: $%{customdata[3]:.4f}<br>LiveBench variant: %{customdata[1]}<extra></extra>';
  const traces = [
    {
      x: dominated.map(m => m.costPerSuccessfulTaskUsd), y: dominated.map(m => m.overallScore),
      mode: 'markers', type: 'scatter', name: 'Dominated',
      marker: { size: 11, color: '#a78bfa', opacity: 0.65 },
      customdata: dominated.map(custom), hovertemplate: hover,
    },
    {
      x: frontier.map(m => m.costPerSuccessfulTaskUsd), y: frontier.map(m => m.overallScore),
      mode: 'markers', type: 'scatter', name: 'Pareto frontier',
      marker: { size: 14, color: '#10b981', line: { width: 2, color: isPlotDark() ? '#064e3b' : '#ecfdf5' } },
      customdata: frontier.map(custom), hovertemplate: hover.replace('<extra></extra>', '<extra>Frontier</extra>'),
    },
    {
      x: frontier.map(m => m.costPerSuccessfulTaskUsd), y: frontier.map(m => m.overallScore),
      mode: 'lines', type: 'scatter', name: 'frontier-curve',
      line: { shape: 'spline', dash: 'dot', color: '#94a3b8', width: 2 }, hoverinfo: 'skip', showlegend: false,
    },
  ];
  const scores = rows.map(m => m.overallScore);
  const yMin = Math.max(0, Math.floor(Math.min(...scores) - 2));
  const yMax = Math.min(100, Math.ceil(Math.max(...scores) + 2));
  const layout = {
    ...getPlotlyLayout(),
    title: { text: 'LiveBench Overall Score vs Cost Per Successful Task', font: plotlyTitle(14) },
    xaxis: { ...getPlotlyLayout().xaxis, title: 'Cost Per Successful Task (USD, log scale)', type: 'log', tickprefix: '$', tickformat: ',.2f' },
    yaxis: { ...getPlotlyLayout().yaxis, title: 'Overall Score', range: [yMin, yMax], autorange: false },
    legend: { orientation: 'h', y: -0.18 },
    margin: { ...getPlotlyLayout().margin, r: 72, b: 96 },
  };
  Plotly.newPlot('chart-livebench-pareto', traces, layout, PLOTLY_CONFIG).then(() => {
    const gd = document.getElementById('chart-livebench-pareto');
    const points = rows.map(m => ({
      id: m.id,
      label: m.name,
      x: m.costPerSuccessfulTaskUsd,
      y: m.overallScore,
      frontier: frontierSet.has(m.id),
    }));
    const annotations = buildCollisionSafeLabelAnnotations(points, gd, { fontSize: 9, markerRadius: 11, safety: 1.35 });
    return Plotly.relayout(gd, { annotations }).then(() => repairCollisionSafeLabelAnnotations(gd, annotations));
  });
}
"""
if "function renderLiveBenchPareto()" in html:
    html = replace_once(html, r"function renderLiveBenchPareto\(\) \{[\s\S]*?\n\}(?=\n\nfunction renderPareto\(\))", livebench_function.rstrip(), "LiveBench Pareto chart")
else:
    html = html.replace("function renderPareto()", livebench_function + "\nfunction renderPareto()", 1)
if "function renderPareto()" not in html:
    raise SystemExit("root Pareto renderer missing")

html = html.replace("const versions = ['v0.7','v0.8','v0.9','v1.0','v1.1','v1.2','v1.3','v1.3.1'];", "const versions = ['v0.7','v0.8','v0.9','v1.0','v1.1','v1.2','v1.3','v1.3.1','v1.4.0'];")
html = html.replace("const vKeys = ['v70','v80','v90','v100','v110','v120','v130','v131'];", "const vKeys = ['v70','v80','v90','v100','v110','v120','v130','v131','v140'];")
html = html.replace("v === 'v1.3.1' ?", "v === 'v1.4.0' ?")
html = html.replace("v1.3.1: 17 models · 12 dims", "v1.4.0: 21 models · 13 dims")
html = html.replace("v1.4.0: 21 models · 13 dims", f"v1.4.0: {n} models · {d} dims")

html = html.replace("v1.3.1", VERSION)
html = html.replace("July 28, 2026", DATE)
html = html.replace("17 models", f"{n} models")
html = html.replace("n=17", f"n={n}")
html = html.replace("12 dimensions", f"{d} dimensions")
html = html.replace("12 Total", f"{d} Total")
html = html.replace("All 17", f"All {n}")
html = html.replace("all 17", f"all {n}")
html = html.replace("12 normalized", f"{d} normalized")
html = html.replace("all 11 non-cost", f"all {d - 1} non-cost")
html = html.replace("75% non-cost", f"{100 - weight_by_key['costComposite']['weightPct']:.0f}% non-cost")
html = html.replace("the 8 ranked models", f"the {n}-model cohort")
html = html.replace("n = 17", f"n = {n}")
html = html.replace("rank 17", f"rank {n}")
html = html.replace("17 DeepSWE", f"{n} DeepSWE")
html = html.replace("12 zero-gap dimensions", f"{d} zero-gap dimensions")
html = html.replace("17 × 12", f"{n} × {d}")
html = html.replace("ranked 1–17", f"ranked 1–{n}")
html = html.replace("Seven complementary charts", "Eight complementary charts")
html = html.replace("Sep 4", "Sep 5")
html = re.sub(
    r"const versions = \[[^;]*\];",
    "const versions = ['v0.7','v0.8','v0.9','v1.0','v1.1','v1.2','v1.3','v1.3.1','v1.4.0'];",
    html,
    count=1,
)
html = re.sub(
    r"const vKeys = \[[^;]*\];",
    "const vKeys = ['v70','v80','v90','v100','v110','v120','v130','v131','v140'];",
    html,
    count=1,
)

hero_desc = (
    f'ValueRank ranks <strong>{n} current DeepSWE Best models</strong> across a '
    f'<strong>zero-gap {d}-dimension set</strong>. {VERSION} uses Artificial Analysis '
    f'<strong>{aa_version}</strong> components plus DeepSWE performance and a composite AA+DeepSWE Cost. '
    f'Speed is preserved as coverage-only because GPT-6 Astra has no numeric AA speed value. LiveBench Instruction Following and Terminal-Bench 4.0 are shown as external coverage-only views.'
)
html = replace_once(html, r'<p class="hero-desc">[\s\S]*?</p>', f'<p class="hero-desc">\n          {hero_desc}\n        </p>', "hero copy")
html = replace_once(html, r'<div class="(?:nav-meta|vr-nav-meta)">[^<]*</div>', f'<div class="vr-nav-meta">{DATE} · {n} models · {d} dimensions</div>', "nav metadata")
html = replace_once(html, r'<span class="hero-statbar-num">\d+</span>\s*<span class="hero-statbar-label">Models Ranked', f'<span class="hero-statbar-num">{n}</span>\n        <span class="hero-statbar-label">Models Ranked', "model stat")
html = replace_once(html, r'<span class="hero-statbar-num">\d+</span>\s*<span class="hero-statbar-label">Scored Dimensions', f'<span class="hero-statbar-num">{d}</span>\n        <span class="hero-statbar-label">Scored Dimensions', "dimension stat")
html = replace_once(html, r'<span class="hero-statbar-num">(?:Jul 28|Sep \d+)</span>', '<span class="hero-statbar-num">Sep 5</span>', "date stat")

insight_bodies = [
    f'The current Pareto frontier contains <strong>{len(pareto)} models</strong> undominated on composite cost versus quality: {pareto_text}.',
    f'<strong>{models[0]["name"]}</strong> leads the current ValueRank score at <strong>{models[0]["overallScore"]:.1f}</strong>; its position reflects both quality and the two-source cost composite.',
    f'<strong>{min(models, key=lambda item: item["costComposite"])["name"]}</strong> has the lowest composite cost penalty in this cohort, while the quality sub-score keeps capability visible separately.',
    f'{VERSION} refreshes the full <strong>{n}-model</strong> DeepSWE roster against <strong>{aa_version}</strong>, keeps <strong>{d} zero-gap dimensions</strong>, and leaves Speed supplemental because GPT-6 Astra reports N/A.',
]
grid_start = html.find('<div class="insight-grid"')
grid_end = html.find('</section>', grid_start)
if grid_start < 0 or grid_end < 0:
    raise SystemExit("insight grid not found")
grid = html[grid_start:grid_end]
insight_cursor = iter(insight_bodies)
grid, insight_count = re.subn(
    r'<div class="insight-body">[\s\S]*?</div>',
    lambda _match: f'<div class="insight-body">{next(insight_cursor)}</div>',
    grid,
    count=len(insight_bodies),
)
if insight_count != len(insight_bodies):
    raise SystemExit(f"insight replacement failed: {insight_count}")
html = html[:grid_start] + grid + html[grid_end:]

chart_replacements = [
    (r'(<div class="chart-desc"><strong>Pareto Frontier:</strong>)[\s\S]*?</div>', f'\\1 Current frontier: <strong>{pareto_text}</strong>. Every other ranked model is dominated on composite cost versus quality.</div>'),
    (r'(<div class="chart-desc"><strong>Score Decomposition:</strong>)[\s\S]*?</div>', f'\\1 {VERSION} decomposes the weighted <strong>{d}-dimension</strong> score into Cost, Reliability, Agentic, Intelligence, and Platform macro-categories.</div>'),
    (r'(<div class="chart-desc"><strong>Dimension Heatmap:</strong>)[\s\S]*?</div>', f'\\1 All {n} models × {d} retained dimensions. Color = normalized rank score; every displayed cell is confirmed source data.</div>'),
    (r'(<div class="chart-desc"><strong>Version History:</strong>)[\s\S]*?</div>', f'\\1 Historical rank context through {VERSION}. The current point is a new benchmark-version snapshot, not a claim of score continuity.</div>'),
]
for pattern, replacement in chart_replacements:
    html = replace_once(html, pattern, replacement, "chart copy")

html = re.sub(
    r'(<div class="section-sub">)How scores are calculated,[\s\S]*?(</div>)',
    rf'\1How scores are calculated across {d} current zero-gap dimensions, with explicit cost construction and coverage provenance.\2',
    html,
    count=1,
)
html = re.sub(
    r'(<h3 style="font-size:14px;font-weight:700;margin-bottom:16px;">)Dimension Weights \([^<]*</h3>',
    rf'\1Dimension Weights ({d} Total)</h3>',
    html,
    count=1,
)
html = html.replace("The <strong>overall Score</strong> includes all <strong>12 dimensions</strong>", f"The <strong>overall Score</strong> includes all <strong>{d} retained dimensions</strong>")
html = html.replace("the <strong>11 non-cost dimensions</strong>", f"the <strong>{d - 1} non-cost dimensions</strong>")
html = html.replace("speed among the platform dims", "Speed is shown separately when an AA page publishes a numeric value")
html = html.replace("the highest-quality model", "the current quality leader")
html = html.replace("Gemini 3.1 Pro</strong> stays overall <strong>#1</strong> in v1.2", f"{models[0]['name']}</strong> is overall <strong>#1</strong> in {VERSION}")
html = html.replace("For each of 13 dimensions", f"For each of {d} dimensions")
html = html.replace("weighted sum across all 13 dimensions", f"weighted sum across all {d} dimensions")
html = html.replace("all 12 non-cost dimensions", f"all {d - 1} non-cost dimensions")
html = html.replace("12 non-cost dimensions", f"{d - 1} non-cost dimensions")
html = html.replace("<strong>13 dimensions</strong>", f"<strong>{d} dimensions</strong>")
html = html.replace("The 70% non-cost portion", f"The {100 - weight_by_key['costComposite']['weightPct']:.0f}% non-cost portion")
html = html.replace("21 models × 13 dimensions", f"{n} models × {d} dimensions")
html = html.replace("September 4, 2026", DATE)
html = html.replace("All scored cells are confirmed primary-source data in v1.2", f"All scored cells are confirmed primary-source data in {VERSION}")
html = html.replace("excluded from v1.2", "excluded from the current primary score")
html = re.sub(
    r"(function renderVersionTable\(\) \{[\s\S]*?const versions = )\[[^;]*\];",
    lambda match: match.group(1) + "['v0.7','v0.8','v0.9','v1.0','v1.1','v1.2','v1.3','v1.3.1','v1.4.0'];",
    html,
    count=1,
)

if 'data-chart="livebenchPareto"' not in html:
    html = html.replace(
        '      <button class="chart-tab" data-chart="frontier2">Cost Impact</button>',
        '      <button class="chart-tab" data-chart="livebenchPareto">LiveBench Pareto</button>\n      <button class="chart-tab" data-chart="frontier2">Cost Impact</button>',
        1,
    )
if 'id="panel-livebenchPareto"' not in html:
    livebench_panel = f'''       <!-- LiveBench Pareto -->
       <div class="chart-panel" id="panel-livebenchPareto">
         <div class="chart-desc"><strong>LiveBench Pareto:</strong> Official LiveBench Overall Score versus Cost Per Successful Task for {livebench_document['matchedN']}/{livebench_document['cohortN']} matched cohort rows. Higher Overall and lower cost are better; GPT-6 Astra is omitted because this pinned release has no row for it.</div>
         <div id="chart-livebench-pareto" class="plotly-chart" style="height:520px;"></div>
       </div>
'''
    html = html.replace('      <!-- Two-frontier / Cost Impact -->', livebench_panel + '      <!-- Two-frontier / Cost Impact -->', 1)
if 'livebenchPareto: renderLiveBenchPareto' not in html:
    html = html.replace('  frontier2: renderFrontier2,', '  livebenchPareto: renderLiveBenchPareto,\n  frontier2: renderFrontier2,', 1)
if "'chart-heatmap-data','chart-livebench-pareto'" not in html:
    html = html.replace("    'chart-heatmap-data'", "    'chart-heatmap-data','chart-livebench-pareto'", 1)

if 'id="livebench-data"' not in html:
    livebench_card = f'''    <div class="card mb-6" id="livebench-data">
      <h3 style="font-size:14px;font-weight:700;margin-bottom:8px;">LiveBench External Coverage</h3>
      <p class="method-text" style="margin-bottom:16px;">Release <strong>{livebench_document['release']}</strong> matches <strong>{livebench_document['matchedN']}/{livebench_document['cohortN']}</strong> ranked models. Instruction Following is the four-task LiveBench mean; Overall is the seven-category mean; cost is the official Cost Per Successful Task. These fields are visible here and in the Pareto chart but are not imputed into the primary score.</p>
      <div style="overflow-x:auto;">
        <table class="dim-table">
          <thead><tr><th>Model</th><th>LiveBench variant</th><th>Instruction Following</th><th>Overall</th><th>Cost / successful task</th><th>Frontier</th></tr></thead>
          <tbody>{livebench_site_table_rows}</tbody>
        </table>
      </div>
      <p class="method-text" style="margin-top:12px;">Source: <a href="{livebench_document['source']['homepage']}" target="_blank" rel="noopener">LiveBench</a>; pinned data release 2026-06-25. Pareto frontier: <strong>{html_escape(livebench_pareto_text)}</strong>.</p>
    </div>
'''
    data_start = html.find('<!-- DATA -->')
    data_card = html.find('    <div class="card mb-6">', data_start)
    if data_start < 0 or data_card < 0:
        raise SystemExit("data section insertion point not found")
    html = html[:data_card] + livebench_card + html[data_card:]

site_path.write_text(html)
inject_header(site_path, "llm", f"{DATE} · {n} models · {d} scored dimensions", VERSION)

coding_path = ROOT / "site" / "coding-agents" / "index.html"
if coding_path.exists():
    coding_html = coding_path.read_text()
    coding_html = coding_html.replace(
        "Coding agents ranked on Artificial Analysis Coding Agent Index, Terminal-Bench 2.1, and cost. ValueRank v0.3 · 42 agents.",
        "Historical coding-agent snapshot using the Artificial Analysis Coding Agent Index and Terminal-Bench 2.1 source data. It is retained for provenance; the current standalone benchmark is Terminal-Bench 4.0.",
    )
    coding_html = coding_html.replace(
        "AA Coding Agent Index + Terminal-Bench 2.1 + cost. ValueRank v0.3 · 42 agents.",
        "Historical AA Coding Agent Index + Terminal-Bench 2.1 snapshot. ValueRank v0.3 · 42 agents.",
    )
    coding_html = coding_html.replace(
        "Overall = 0.25·Cost + 0.60·AA Coding Agent Index + 0.15·TB2.1 (missing TB2.1 → neutral 50). Cohort from Artificial Analysis; TB2.1 from tbench.ai.",
        "Historical snapshot: Overall = 0.25·Cost + 0.60·AA Coding Agent Index + 0.15·TB2.1, with the original neutral-fill policy. This page is not the current TB4 leaderboard; use the Terminal-Bench 4.0 page for current results.",
    )
    coding_html = coding_html.replace("<th>TB2.1</th>", "<th>TB2.1 (historical)</th>")
    coding_html = coding_html.replace("ValueRank coding-agents v0.3 · July 28, 2026", "ValueRank coding-agents v0.3 · historical TB2.1 snapshot")
    coding_path.write_text(coding_html)
    inject_header(coding_path, "coding", "Historical snapshot · 42 agent variants", VERSION)

print(json.dumps({
    "version": VERSION,
    "models": n,
    "dimensions": d,
    "dropped": [item["label"] for item in dropped],
        "outputs": ["README.md", "methodology.md", "scores.md", "raw-data.md", "site/index.html", "site/coding-agents/index.html"],
}, indent=2, ensure_ascii=False))
