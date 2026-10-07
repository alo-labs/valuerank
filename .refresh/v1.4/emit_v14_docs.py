#!/usr/bin/env python3
"""Emit the current README, methodology, score tables, raw data, and site.

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
RESEARCH = ROOT / "research" / "2026-09-29-valuerank-refresh-v4-3-2"
sys.path.insert(0, str(ROOT / "scripts"))
from plan_costs import build_cost_fields, load_plan_routes, route_summary
from site_header import inject_header
from aa_reconciliation import reconcile as reconcile_aa, publication as aa_reconciliation_publication

VERSION = "v1.9.4"
DATE = "October 8, 2026"
SHORT_DATE = "Oct 8"
CURRENCY = "$"

AA_INDEX_URL = "https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index"
AA_METHODOLOGY_URL = "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
AA_DEEPSWE_URL = "https://artificialanalysis.ai/agents/coding-agents?coding-agents-performance-chart=deep-swe-v1.1"
LIVEBENCH_URL = "https://livebench.ai/"
TERMINAL_BENCH_URL = "https://www.tbench.ai/leaderboard/terminal-bench/4.0"
BUG_HUNT_URL = "https://bughunt.productcompass.pm/"

BENCHMARK_URLS = {
    "DeepSWE pass@1": AA_DEEPSWE_URL,
    "AA-Briefcase": "https://artificialanalysis.ai/evaluations/aa-briefcase",
    "GDPval-AA v2.1": "https://artificialanalysis.ai/evaluations/gdpval-aa",
    "AutomationBench-AA": "https://artificialanalysis.ai/evaluations/automationbench-aa",
    "Terminal-Bench 4.0 (AA evaluation)": "https://artificialanalysis.ai/evaluations/terminalbench-4-0",
    "τ³-Banking (legacy)": "https://artificialanalysis.ai/evaluations/tau3-banking",
    "Terminal-Bench v2.1 (legacy)": "https://artificialanalysis.ai/evaluations/terminalbench-2-1",
    "Terminal-Bench 4.0": TERMINAL_BENCH_URL,
    "SciCode": "https://artificialanalysis.ai/evaluations/scicode",
    "Humanity's Last Exam": "https://artificialanalysis.ai/evaluations/humanitys-last-exam",
    "HLE": "https://artificialanalysis.ai/evaluations/humanitys-last-exam",
    "GDP.pdf": "https://artificialanalysis.ai/evaluations/gdp-pdf",
    "CritPt": "https://artificialanalysis.ai/evaluations/critpt",
    "AA-Omniscience Accuracy": "https://artificialanalysis.ai/evaluations/omniscience",
    "AA-Omniscience Non-Hallucination Rate": "https://artificialanalysis.ai/evaluations/omniscience",
    "AA-LCR v1.1": "https://artificialanalysis.ai/evaluations/artificial-analysis-long-context-reasoning",
    "GPQA Diamond (legacy)": "https://artificialanalysis.ai/evaluations/gpqa-diamond",
    "AA Intelligence Index": AA_INDEX_URL,
    "Artificial Analysis Intelligence Index": AA_INDEX_URL,
    "AA output speed (tok/s)": AA_METHODOLOGY_URL,
    "LiveBench": LIVEBENCH_URL,
    "Bug Hunt Bench": BUG_HUNT_URL,
}


def md_benchmark_link(label):
    url = BENCHMARK_URLS.get(label)
    return f"[{label}]({url})" if url else label


def html_external_link(label, url):
    return f'<a href="{html_escape(url, quote=True)}" target="_blank" rel="noopener">{html_escape(label)}</a>'

scores = json.loads((REFRESH / "scores.json").read_text())
aa_document = json.loads((REFRESH / "aa_metrics.json").read_text())
coverage_document = json.loads((REFRESH / "coverage_matrix.json").read_text())
deepswe_chart_doc = json.loads((REFRESH / "aa_deepswe.json").read_text())
livebench_document = json.loads((REFRESH / "livebench.json").read_text())
tb4_document = json.loads((REFRESH / "tb4.json").read_text())
bug_hunt_document = json.loads((REFRESH / "bug_hunt.json").read_text())
bug_hunt_ranking = scores["bugHuntEmphasisRanking"]
bug_hunt_records = {item["modelId"]: item for item in bug_hunt_document["models"]}
manifest = json.loads((RESEARCH / "run_manifest.json").read_text())
all_models = scores["models"]
models = [model for model in all_models if model.get("rankingEligible") is True]
unranked_models = [model for model in all_models if model.get("rankingEligible") is not True]
weights = scores["weights"]
deepswe_weight = next(weight for weight in weights if weight["key"] == "deepswePassAt1")
n = len(models)
source_n = len(all_models)
unranked_names = ", ".join(model["name"] for model in unranked_models) or "none"
bug_hunt_weight = next(weight for weight in weights if weight["key"] == "bugHuntFixedOf105")
d = len(weights)
pareto = scores["pareto"]
model_by_id = {model["id"]: model for model in all_models}
plan_route_document = load_plan_routes()
plan_cost_fields = build_cost_fields(models, plan_route_document)
plan_summary = route_summary(plan_route_document, plan_cost_fields)
livebench_models = {
    **livebench_document["models"],
    **livebench_document.get("supplementalModels", {}),
}
livebench_rows = [record for record in livebench_models.values() if record.get("matched")]
livebench_supplemental_rows = [
    record for record in livebench_document.get("supplementalModels", {}).values() if record.get("matched")
]
livebench_pareto = [livebench_models[model_id] for model_id in livebench_document["pareto"]]
tb4_rows = tb4_document["rows"]
provider_claims = json.loads((REFRESH / "provider_claims.json").read_text()).get("claims", [])
eligible_provider_claims = [item for item in provider_claims if item.get("eligibleForRanking") is True]
ranking_history_document = json.loads((REFRESH / "ranking_history_v1.5.json").read_text())
ranking_history = ranking_history_document.get("v150", {})
ranking_history_v190 = ranking_history_document.get("v190", {})
ranking_history_v191 = ranking_history_document.get("v191", {})
ranking_history_v192 = ranking_history_document.get("v192", {})
deepswe_updated = scores.get("deepsweObservedAt") or deepswe_chart_doc.get("observedAt", DATE)
deepswe_configurations = deepswe_chart_doc["configurations"]
deepswe_overlap_n = len([item for item in deepswe_configurations if item.get("valueRankModelId")])
bug_hunt_source_matches_n = scores.get("externalBenchmarks", {}).get("bugHunt", {}).get("matchedN", bug_hunt_ranking["matchedN"])
aa_version = scores.get("benchmarkVersion") or "Artificial Analysis Intelligence Index v4.3.2"
cost_mode = scores.get("costMode") or manifest.get("scoring", {}).get("costMode", "unknown")
cost_mode_label = "AA evaluation cost only" if cost_mode == "aa-only" else cost_mode
cost_coverage = scores.get("costCoverage") or manifest.get("scoring", {}).get("costCoverage", {})
cost_missing_text = ", ".join(cost_coverage.get("missingModels", [])) or "none"
dropped = manifest.get("scoring", {}).get("droppedDimensions", [])
cost_weight = next((weight for weight in weights if weight["key"] == "costComposite"), None)
cost_weight_text = f"{cost_weight['weightPct']:.2f}%" if cost_weight else "not included"
site_cost_summary = "The default API Costs basis uses AA total evaluation cost for its fixed benchmark suite, rank-normalized with lower cost better. Plan Costs divides the same AA cost by the highest eligible subscription Value Multiple."
site_cost_raw_input = "For the main-rank Cost dimension, the raw input is AA total evaluation cost in USD. Plan Costs applies the selected model route's Value Multiple to that same amount."
site_cost_weight = f"Cost contributes {cost_weight_text} to the main rank using AA total evaluation cost under API Costs; the Plan Costs basis applies the selected eligible Value Multiple."


def fnum(value, places=2, dash="—"):
    return f"{value:.{places}f}" if isinstance(value, (int, float)) else dash


def pct(value, places=2):
    return f"{value * 100:.{places}f}%" if isinstance(value, (int, float)) else "—"


def pct_points(value, places=1):
    return f"{value:.{places}f}%" if isinstance(value, (int, float)) else "—"


def names(values):
    return ", ".join(values) if values else "none"


speed_coverage = coverage_document.get("fields", {}).get("speed", {})
speed_missing_ids = set(speed_coverage.get("missingModels", []))
speed_missing_text = names([model["name"] for model in models if model["id"] in speed_missing_ids])
speed_selected_available_n = n - sum(model["id"] in speed_missing_ids for model in models)
speed_in_primary = any(weight["key"] == "speed" for weight in weights)
aa_index_estimated_models = names([model["name"] for model in models if model.get("intelligenceIndexStatus") == "estimated"])


livebench_pareto_text = names([record["name"] for record in livebench_pareto]) if livebench_pareto else "none"
livebench_supplemental_text = names([record["name"] for record in livebench_supplemental_rows]) if livebench_supplemental_rows else "none"
livebench_published_n = livebench_document.get("publishedN", len(livebench_rows))
livebench_supplemental_count = livebench_document.get("supplementalMatchedN", len(livebench_supplemental_rows))
livebench_supplemental_label = f"{livebench_supplemental_count} official supplemental model" + ("s" if livebench_supplemental_count != 1 else "")


def primary_rows():
    return "\n".join(
        f"| {model['rank']} | {model['name']} | {model['overallScore']:.1f} | {model['qualityScore']:.1f} | {model['costComposite']:.2f} |"
        for model in models
    )


def dimension_table():
    return "\n".join(
        f"| {index} | {md_benchmark_link(weight['label'])} | {weight['weightPct']:.2f}% | {'higher' if weight['higherBetter'] else 'lower'} |"
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


def bug_hunt_emphasis_table():
    return "\n".join(
        f"| {item['rank']} | {item['name']} | {record['fixedOf105']:g}/105 | "
        f"{item['emphasisScore']:.1f} | n={record['sampleN']} ({record['aggregation']}) | "
        f"{record['effort']} ({record['effortStatus']}) | "
        f"{record['harness']} / {record['route']} | {item['primaryRank']} |"
        for item in bug_hunt_ranking["ranking"]
        for record in [bug_hunt_records[item["modelId"]]]
    )


def bug_hunt_raw_table():
    return "\n".join(
        f"| [{model['name']}]({record.get('sourceUrl', BUG_HUNT_URL)}) | {record.get('fixedOf105') if record.get('matched') else '—'} | "
        f"{record.get('sampleN', '—')} / {record.get('aggregation', '—')} | {record.get('evaluatedModel', '—')} | "
        f"{record.get('effort', '—')} ({record.get('effortStatus', '—')}) | "
        f"{record.get('harness', '—')} | {record.get('route', '—')} | "
        f"{'Matched' if record.get('matched') else record.get('matchStatus', 'No result')} |"
        for model in all_models
        for record in [bug_hunt_records[model['id']]]
    ) + "\n" + "\n".join(
        f"| {model['name']} — separate owner configuration | {config['fixedOf105']} | "
        f"{config.get('sampleN', '—')} / {config.get('aggregation', '—')} | "
        f"[{config.get('evaluatedModel', '—')}]({record.get('sourceUrl', BUG_HUNT_URL)}) | "
        f"{config.get('effort', '—')} ({config.get('effortStatus', '—')}) | "
        f"{config.get('harness', '—')} | {config.get('route', '—')} | "
        f"Owner result present; excluded from selected variant: {config.get('selectionReason', record.get('note', 'Variant equivalence unresolved'))} |"
        for model in all_models
        for record in [bug_hunt_records[model['id']]]
        for config in record.get('availableOwnerConfigurations', [])
        if config.get('selected') is not True
    )


def deepswe_chart_table():
    return "\n".join(
        f"| {item['sourceOrder']} | {item['agent']} | {item['model']} | {item.get('effort') or 'not shown'} | "
        f"{item['scorePct']:.1f}% | "
        f"{'Exact: ' + item['valueRankModelId'] if item.get('valueRankModelId') else item['matchStatus'].replace('_', ' ')} | "
        f"{item.get('matchNote', '—')} |"
        for item in deepswe_configurations
    )


pareto_text = names(pareto)
drop_text = "\n".join(
    f"| {item['label']} | {names(item['missing'])} | {item['reason']} |" for item in dropped
) or "| None | — | All candidate dimensions have complete coverage. |"

aa_reconciliation_report = reconcile_aa()
aa_reconciliation_md, aa_reconciliation_html = aa_reconciliation_publication(aa_reconciliation_report)

readme = f"""# ValueRank
**Frontier AI model ranking focused on production value**

**Version:** {VERSION}
**Updated:** {DATE}
**Scope:** {n} primary-ranked models from a {source_n}-model AA-mapped comparison roster, {d} retained dimensions including Bug Hunt Bench

Publication updated October 8, 2026 with selective MiMo and AA frontier additions. Earlier AA/DeepSWE observations remain dated September 29–30; current MiMo owner run notes were observed October 7. See per-model dates and capture precision in raw-data.md. This publication combines source snapshots with different dates.

## Current result

ValueRank uses AA's [Coding Agent Index v1.5 DeepSWE v1.1 chart](https://artificialanalysis.ai/agents/coding-agents?coding-agents-performance-chart=deep-swe-v1.1), which publishes 25 agent/model configurations across 113 tasks, alongside the {source_n}-model AA-mapped comparison roster. The main score includes {n} rows with an exact DeepSWE model-variant result and an eligible Bug Hunt owner result; the other {len(unranked_models)} candidates remain source-only. Every chart result retains its displayed agent and effort, and results from other model versions or composite agents are not transferred. Provider claims fill benchmark-owner gaps only for the exact benchmark version and evaluated variant, remain visibly labelled, and are replaced by owner results when available.

| Rank | Model | Overall | Quality | AA eval-cost penalty (lower better) |
|---:|---|---:|---:|---:|
{primary_rows()}

The current Pareto frontier—undominated on composite cost versus quality—is: **{pareto_text}**.

## Refresh basis and v1.9 scoring update

- **{n}/{source_n}** AA-mapped candidates have both an exact DeepSWE v1.1 chart variant and a Bug Hunt owner result, so only those enter the main composite. The other candidates remain unranked: **{unranked_names}**.
- Bug Hunt Bench has priority **{bug_hunt_weight['priority']}** and weight **{bug_hunt_weight['weightPct']:.2f}%** in the main rank. DeepSWE v1.1 has priority **{deepswe_weight['priority']}** and weight **{deepswe_weight['weightPct']:.2f}%**. A separate Bug Hunt emphasis view gives Bug Hunt still more weight.
- AA's Coding Agent Index v1.5 chart reports **{len(deepswe_configurations)} configurations** for DeepSWE v1.1 across **{deepswe_chart_doc['benchmarkTasks']} tasks**, observed **{deepswe_updated}**. All configurations and model-version mapping decisions are retained in [.refresh/v1.4/aa_deepswe.json](.refresh/v1.4/aa_deepswe.json); **{deepswe_overlap_n}** configurations map to the current model variants.
- Artificial Analysis now uses **{aa_version}**: AA-Briefcase v1.1, GDPval-AA v2.1, AutomationBench-AA, Terminal-Bench 4.0, SciCode, HLE, GDP.pdf, CritPt, AA-LCR v1.1, and split AA-Omniscience accuracy/reliability components. τ³-Banking and Terminal-Bench 2.1 remain historical source fields only.
- The standalone Terminal-Bench page has **{tb4_document['rowN']} official rows**, including **{tb4_document['matchedN']}/{tb4_document['cohortN']}** direct cohort matches. One separately labelled DeepSeek V4.1-Flash provider claim is used for the current `deepseek-v4-flash` API alias; official and claim counts are kept distinct.
- **{md_benchmark_link('LiveBench')} {livebench_document['release'].replace('_', '-')}** provides the four-task Instruction Following mean plus Overall Score and Cost Per Successful Task views; the primary score includes Instruction Following because it has zero gaps in the exact-match cohort.
- The companion Bug Hunt emphasis ranking covers the same **{bug_hunt_ranking['matchedN']}** exact-overlap models and raises Bug Hunt to **{bug_hunt_ranking['benchmarkWeightPct']:.2f}%**; its ranked table and the full source snapshot are documented in [scores.md](scores.md#bug-hunt-emphasis-ranking) and [.refresh/v1.4/bug_hunt.json](.refresh/v1.4/bug_hunt.json).
- The AA chart's full **{len(deepswe_configurations)}-configuration** DeepSWE v1.1 result set remains available in the raw-data table; model variants and Devin composite-agent results stay separate.
- The score retains **{d} zero-gap dimensions**; **{names([item['label'] for item in dropped])}** remain excluded because each has incomplete eligible coverage. Missing values remain null and are not neutral-filled.
- AA output speed is numeric for **{speed_selected_available_n}/{n}** selected pages; **{speed_missing_text}** has no value, so Speed is {'retained' if speed_in_primary else 'excluded'} under the zero-gap rule.
- AA total evaluation cost is available for **{cost_coverage.get('availableN', '—')}/{n}** primary models. The API Costs baseline uses it consistently; the Plan Costs basis divides the same value by each model's highest eligible subscription Value Multiple.
- Earlier ValueRank versions are not numerically comparable because this release changes benchmark weights and the ranked cohort.

## Sources and audit trail

- [AA Coding Agent Index v1.5 — DeepSWE v1.1](https://artificialanalysis.ai/agents/coding-agents?coding-agents-performance-chart=deep-swe-v1.1) is the benchmark-owner source for all DeepSWE values in this release. The public 25-configuration capture and model-variant decisions are recorded in [.refresh/v1.4/aa_deepswe.json](.refresh/v1.4/aa_deepswe.json).
- [Artificial Analysis methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) and the linked first-party model pages for current component values and Intelligence Index evaluation cost.
- [LiveBench](https://livebench.ai/) and its [official release data repository](https://github.com/livebench/new-livebench), pinned at [release data commit {livebench_document['source'].get('releaseDataCommit', 'not recorded')}](https://github.com/livebench/new-livebench/commit/{livebench_document['source'].get('releaseDataCommit', '')}), for the 2026-06-25 task/category table, Instruction Following means, Overall Score, and Cost Per Successful Task.
- [Terminal-Bench 4.0](https://www.tbench.ai/) and the [official Harbor repository](https://github.com/harbor-framework/terminal-bench) for the current rendered leaderboard and task identity.
- [Bug Hunt Bench]({BUG_HUNT_URL}), with owner-published [combined scoreboard]({bug_hunt_document['sources']['scoreboard']}) and [run notes]({bug_hunt_document['sources']['runNotes']}) pinned to commit **{bug_hunt_document['sourceCommit']}**.
- [Refresh record](research/2026-09-29-valuerank-refresh-v4-3-2/README.md) for the v4.3.2 source change, evidence boundary, provider claims, and scoring decisions.
- [Provider claim ledger](.refresh/v1.4/provider_claims.json) for provider-sourced values, eligibility, and alias/variant caveats. Provider values never masquerade as benchmark-owner measurements.
- [Coverage matrix](.refresh/v1.4/coverage_matrix.json) for primary and supplemental availability, including fields not used in the score.

## Files

- [scores.md](scores.md): final ranking, weights, and normalized matrix
- [raw-data.md](raw-data.md): source values, selected AA variants, and supplemental coverage
- [methodology.md](methodology.md): cohort, benchmark versions, normalization, and zero-gap rule
- [site/index.html](site/index.html): interactive static publication
- [site/tb4/index.html](site/tb4/index.html): current Terminal-Bench 4.0 score-versus-cost publication
- [research/2026-09-29-valuerank-refresh-v4-3-2/](research/2026-09-29-valuerank-refresh-v4-3-2/): reproducible v4.3.2 refresh package
- [.refresh/v1.4/](.refresh/v1.4/): refresh scripts and machine-readable snapshots/outputs
"""
(ROOT / "README.md").write_text(readme + aa_reconciliation_md)

methodology = f"""# ValueRank Methodology

**Version:** {VERSION}
**Updated:** {DATE}

## Cohort and source versions

The model universe is the **{source_n}-model AA-mapped ValueRank comparison roster**. AA's Coding Agent Index v1.5 chart publishes **{len(deepswe_configurations)} DeepSWE v1.1 configurations** across **{deepswe_chart_doc['benchmarkTasks']} tasks**. The primary rank contains **{n} models** with both an exact chart model-variant result and an eligible Bug Hunt owner result; all other candidates remain visible without a composite rank. Each chart result retains its displayed model variant, agent, and effort.

- DeepSWE v1.1 source: [AA Coding Agent Index v1.5](https://artificialanalysis.ai/agents/coding-agents?coding-agents-performance-chart=deep-swe-v1.1). The published chart says each score averages pass@1 across three attempts per task; the 25 visible configurations and exact-variant mapping decisions are pinned in [.refresh/v1.4/aa_deepswe.json](.refresh/v1.4/aa_deepswe.json).
- AA source: [Intelligence Index methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking), current {aa_version}.
- AA v4.3.2 model values: first-party model pages selected by .refresh/v1.4/aa_mapping.json and recorded in aa_metrics.json.
- LiveBench source: [livebench.ai](https://livebench.ai/), pinned release **2026-06-25** with seven categories, including the four-task Instruction Following category and published Cost Per Successful Task values. The data files are pinned to release commit **{livebench_document['source'].get('releaseDataCommit', 'not recorded')}**.
- Terminal-Bench source: [tbench.ai](https://www.tbench.ai/), current **4.0** rendered leaderboard snapshot with {tb4_document['rowN']} official rows, **{tb4_document['matchedN']}** direct cohort matches, and **{tb4_document.get('providerClaimN', 0)}** eligible provider claim.

Earlier publications used different source snapshots, weights, or cohorts. They remain historical; their numerical scores must not be compared directly with {VERSION}.

## Primary dimensions

The score retains only dimensions with a genuine value for every one of the {n} ranked models, including exact owner-published Bug Hunt values. Values are stored as raw fractions in scores.json, then converted to rank scores within this cohort.

| # | Dimension | ValueRank weight | Direction |
|---:|---|---:|---|
{dimension_table()}

The eleven AA source components below correspond to ten current AA evaluations because Omniscience is split into accuracy and non-hallucination reliability:

| AA evaluation/component | Current methodology weight |
|---|---:|
| {md_benchmark_link('AA-Briefcase')} | 15% |
| {md_benchmark_link('GDPval-AA v2.1')} | 10% |
| {md_benchmark_link('AutomationBench-AA')} | 5% |
| {md_benchmark_link('Terminal-Bench 4.0 (AA evaluation)')} | 10% |
| {md_benchmark_link('SciCode')} | 10% |
| {md_benchmark_link("Humanity's Last Exam")} | 10% |
| {md_benchmark_link('GDP.pdf')} | 10% |
| {md_benchmark_link('CritPt')} | 10% |
| {md_benchmark_link('AA-Omniscience Accuracy')} | 10% |
| {md_benchmark_link('AA-Omniscience Non-Hallucination Rate')} | 5% |
| {md_benchmark_link('AA-LCR v1.1')} | 5% |

These AA methodology weights describe the source index, not the combined ValueRank weights above. ValueRank adds DeepSWE, cost, and AA Index signals using the explicitly published priority table. The AA Index value for {aa_index_estimated_models} is the benchmark owner’s estimate pending independent evaluation.

## API Costs and Plan Costs

The default API Costs basis uses each model's AA total evaluation cost in USD. Plan Costs divides that same value by the model's highest eligible subscription Value Multiple. Lower cost ranks better in both views; the site switcher recalculates the primary composite when the cost basis changes.

## Zero-gap rule

- A candidate dimension is scored only when every model has an eligible value from the benchmark owner or an exact-version provider claim.
- Missing values remain null in aa_metrics.json and are listed in coverage_matrix.json.
- No neutral 50, median, or mismatched-version value is used. Provider claims remain source-typed and are eligible only for the stated benchmark version and evaluated model/route.
- AA output speed covers **{speed_selected_available_n}/{n}** selected pages; **{speed_missing_text}** is missing, so Speed is {'retained' if speed_in_primary else 'excluded'} under the zero-gap rule.
- GPQA Diamond remains an explicitly labelled legacy ValueRank input; it is not a component of the v4.3.2 source composite.
- AA total evaluation cost is available for **{cost_coverage.get('availableN', '—')}/{n}** ranked models; the cost component uses **{cost_mode_label}** consistently across this cohort.
- LiveBench Instruction Following is available for **{sum(model.get('livebenchInstructionFollowing') is not None for model in models)}/{n}** ranked models and is scored. Terminal-Bench 4.0 remains supplemental because it has gaps in this cohort.
- Bug Hunt Bench has **{bug_hunt_source_matches_n}/{source_n}** exact owner results; **{bug_hunt_ranking['matchedN']}** also have an exact AA DeepSWE model-variant result and enter the primary composite at **{bug_hunt_weight['weightPct']:.2f}%**. {len(unranked_models)} candidates without the full overlap are not ranked.

Dropped candidate dimensions:

| Dimension | Missing models | Decision |
|---|---|---|
{drop_text}

## Rank normalization

For each retained dimension, models are ranked from best to worst and mapped with:

((n - rank) / (n - 1)) × 100

Rank 1 maps to 100, rank {n} maps to 0, and exact ties receive the average tied rank. Lower-is-better dimensions, including composite Cost, reverse the ordering before normalization.

## Benchmark evaluation cost (score input)

The Cost input uses **{cost_mode_label}** for every one of the {n} ranked models. AA Intelligence Index evaluation cost is normalized into costComposite; lower evaluation cost is better. No DeepSWE leaderboard cost or missing-value fill is used.

## Quality score and interpretation

Overall Score is the weighted sum of all retained dimensions. Quality Score removes Cost and renormalizes the remaining retained dimensions to 100%. Scores are rank-relative to this cohort, not probabilities and not an absolute model capability scale.

## Supplemental data

{md_benchmark_link('Artificial Analysis Intelligence Index')} exposes additional evaluations—such as MLCR, Harvey, APEX-Agents, MMMU-Pro, EnterpriseOpsGym, ITBench SRE, and legacy fields. They are preserved in aa_metrics.json when published, and their coverage is reported in coverage_matrix.json. AA-Briefcase, GDP.pdf, AutomationBench-AA, and AA's Terminal-Bench 4.0 evaluation are v4.3.2 source components, not standalone ValueRank dimensions. GPQA Diamond and the old τ³-Banking/TB2.1 fields are separately labelled legacy data.

{md_benchmark_link('LiveBench')} is incorporated as the current external Instruction Following source. Its four official task values—paraphrase, simplify, story_generation, and summarize—are averaged into the published Instruction Following value; LiveBench Overall is the mean of its seven category means. The LiveBench chart uses the official Overall Score against the official Cost Per Successful Task for the {livebench_document['matchedN']} matched cohort rows plus {livebench_supplemental_label}: {livebench_supplemental_text}.

{md_benchmark_link('Terminal-Bench 4.0')} is incorporated as the current external terminal-agent source. The official page shows {tb4_document['rowN']} owner rows; a separate provider-claim row is included for the current DeepSeek V4 Flash API alias and is explicitly labelled. Together they provide {tb4_document.get('rankingAvailableN', tb4_document['matchedN'])}/{tb4_document['cohortN']} eligible cohort values, leaving {len(tb4_document.get('rankingMissingModels', tb4_document['missingModels']))} gaps.

## Provider claim policy

When the benchmark owner has not published a result for a model, ValueRank uses a model-provider-published claim when the benchmark version and evaluated model identity match. The claim keeps its source type, direct source link, date, and any alias/variant caveat in the raw data and evidence ledger. A benchmark-owner result supersedes the claim when it becomes available. Claims for different versions or variants remain audit-only.

## Bug Hunt Bench scoring

Bug Hunt Bench reports planted bugs fixed out of **105** across two repositories. The owner scoreboard snapshot is pinned at commit **{bug_hunt_ranking['sourceCommit']}** and provides **{bug_hunt_source_matches_n}/{source_n}** exact results in the AA-mapped comparison roster. **{bug_hunt_ranking['matchedN']}** of those also have an exact AA DeepSWE v1.1 model-variant result, so both values enter the main {n}-model composite at Bug Hunt priority **{bug_hunt_weight['priority']}** (**{bug_hunt_weight['weightPct']:.2f}%**).

The companion Bug Hunt emphasis ranking uses the same {n}-model exact-overlap cohort and re-ranks the other retained dimensions within those models. It gives Bug Hunt priority **{bug_hunt_ranking['benchmarkPriority']}** out of **{bug_hunt_ranking['totalPriority']}**, or **{bug_hunt_ranking['benchmarkWeightPct']:.2f}%**. Ties use average rank, then lower cost and model name. Its scores are a separate weighting view and should not be compared numerically with the primary composite.

The scoreboard tests an agentic model-and-harness configuration. Runs vary in effort, agent CLI, route, and repeat count; those details remain in the table, and single-run rows are noisy. The {len(unranked_models)} models without the full AA DeepSWE and Bug Hunt overlap remain unranked; some have only one of those results. No values are inferred or neutral-filled. A provider claim may fill an owner gap only for an exact benchmark version and evaluated model variant, and an owner result supersedes it when published.

## Limitations

- The AA DeepSWE chart and the other AA Index components measure distinct tasks and use different evaluation setups; ValueRank is a transparent synthesis, not a new benchmark.
- Bug Hunt results also depend on the tested agent CLI/harness, effort, and route; they measure the tested stack, not model capability in isolation.
- Rank normalization discards magnitude differences. The AA DeepSWE chart publishes rounded percentage values without uncertainty intervals; read them alongside the exact agent and effort configuration.
- Page variants can differ by reasoning effort; the selected URL and variant are recorded per model.
- Provider claims may use a different harness or sampling procedure than the benchmark owner; displayed claim values are not presented as independent benchmark-owner measurements.
- AA output speed is numeric for **{speed_selected_available_n}/{n}** selected pages; **{speed_missing_text}** has no value, so Speed is {"included" if speed_in_primary else "excluded"} under the zero-gap rule.
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

**Updated:** {DATE} · **Cohort:** {n} · **Retained dimensions:** {d} · **Default cost basis:** API Costs (AA total evaluation cost)

API Costs uses the AA total evaluation cost in USD; Plan Costs divides that same value by the highest eligible subscription Value Multiple. The site switcher recalculates the main rank and cost-based charts using the selected basis.

## Final ranking

| Rank | Model | Overall | Quality | Quality Rank | AA eval-cost penalty (lower better) |
|---:|---|---:|---:|---:|---:|
{chr(10).join(f"| {m['rank']} | {m['name']} | {m['overallScore']:.1f} | {m['qualityScore']:.1f} | {m['qualityRank']} | {m['costComposite']:.2f} |" for m in models)}

## Bug Hunt Emphasis Ranking

Bug Hunt is included in the main **{n}-model primary ranking** at **{bug_hunt_weight['weightPct']:.2f}%**. The companion emphasis view uses the same cohort and increases Bug Hunt's weight to **{bug_hunt_ranking['benchmarkWeightPct']:.2f}%** by re-ranking the other retained dimensions within those models.

| Bug Hunt rank | Model | Fixed / 105 | Emphasis score | Runs / aggregation | Effort | Harness / route | Primary rank |
|---:|---|---:|---:|---|---|---|---:|
{bug_hunt_emphasis_table()}

Source: [Bug Hunt Bench]({BUG_HUNT_URL}) and the pinned [owner scoreboard]({bug_hunt_document['sources']['scoreboard']}) at commit **{bug_hunt_ranking['sourceCommit']}**. The run configuration details and coverage gaps are in [raw-data.md](raw-data.md).

## Pareto frontier

Undominated on composite cost versus quality: **{pareto_text}**.

## Weights

| Dimension | Weight | Direction |
|---|---:|---|
{chr(10).join(f"| {md_benchmark_link(w['label'])} | {w['weightPct']:.2f}% | {'higher' if w['higherBetter'] else 'lower'} |" for w in weights)}

## Normalized dimension matrix

Dimension order is the order in weights above:

[{', '.join(w['key'] for w in weights)}]

| Rank | Model | Normalized dimensions |
|---:|---|---|
{norm_rows}

## Coverage decision

The score is zero-gap across all retained dimensions for the {n} exact-match models. {len(unranked_models)} models remain in the {source_n}-model source roster without a primary rank because they lack exact eligible Bug Hunt results. Dropped candidate dimensions are listed below; missing values remain null rather than receiving neutral scores.

## External benchmark coverage

{md_benchmark_link('Artificial Analysis Intelligence Index')} provides the current AA component scores used by this release. {md_benchmark_link('LiveBench')} Instruction Following remains supplemental because the pinned release lacks full coverage in the exact-match cohort; its Overall Score and Cost Per Successful Task are also supplemental. {md_benchmark_link('Terminal-Bench 4.0')} remains supplemental because coverage is incomplete in the exact-match cohort. See [raw-data.md](raw-data.md) for source-backed tables.
"""
(ROOT / "scores.md").write_text(scores_md)

aa_variant_rows = "\n".join(
    f"| {model['name']} | {model['aaSlug']} | {model['aaVariant'] or 'not stated'} | [page]({model['aaUrl']}) |"
    for model in all_models
)
raw_rows = "\n".join(
    f"| {model['rank'] if model.get('rank') is not None else '—'} | {model['name']} | "
    f"{((model.get('deepsweScoreConfig') or {}).get('agent', '—'))} / "
    f"{((model.get('deepsweScoreConfig') or {}).get('model', '—'))} / "
    f"{((model.get('deepsweScoreConfig') or {}).get('effort') or 'not shown')} | "
    f"{fnum(model.get('deepswePassAt1Pct'), 1)}% | {fnum(model.get('briefcaseElo'))} | "
    f"{fnum(model.get('gdpvalV21'), 1)} | {pct(model.get('automationBenchAA'))} | "
    f"{pct(model.get('aaTerminalBenchV40'))} | {pct(model.get('aaTerminalBenchV21'))} | "
    f"{pct(model.get('legacyTau3Banking'))} | {pct(model['scicode'])} | "
    f"{pct(model.get('gdpPdfAllPass'))} | {pct(model['aaLcr'])} | {pct(model['hle'])} | "
    f"{pct(model['gpqaDiamond'])} | {pct(model['critpt'])} | {pct(model['omniAccuracy'])} | "
    f"{pct(model['omniNonHallucination'])} | "
    f"{fnum(model['intelligenceIndex'])}{' (estimated)' if model.get('intelligenceIndexStatus') == 'estimated' else ''} | "
    f"{CURRENCY}{fnum(model.get('aaEvalCost'))} | {fnum(model.get('speed'), 1)} |"
    for model in all_models
)
supplemental_rows = "\n".join(
    f"| {field} | {data.get('availableN', '—')}/{data.get('cohortN', n)} | {names(data.get('missingModels', []))} | {'Primary' if data.get('includedInPrimaryScore') else 'Supplemental / not scored'} |"
    for field, data in coverage_document.get("fields", {}).items()
    if data.get("group") == "supplemental"
)
livebench_raw_rows = livebench_table()
tb4_raw_rows = tb4_table()
aa_evidence_rows = "\n".join(
    "| " + " | ".join(str(value).replace("|", "\\|").replace("\n", " ") for value in (
        model['name'],
        (record.get('extraction') or {}).get('sourceObservedAt') or aa_document.get('observedAt') or 'Not recorded',
        (record.get('extraction') or {}).get('precision') or 'No rounding metadata recorded',
        (record.get('extraction') or {}).get('note') or 'Retained earlier source snapshot',
    )) + " |"
    for model in all_models
    for record in [aa_document.get('models', {}).get(model['id'], {})]
)
provider_claim_rows = "\n".join(
    f"| {claim['benchmark']} {claim['benchmarkVersion']} | {claim.get('cohortModelId', '—')} | {claim.get('evaluatedModel', '—')} | {pct(claim.get('value'))} | {'Ranking eligible' if claim.get('eligibleForRanking') is True else 'Audit only'} | {claim.get('sourceType', '—')} | [provider source]({claim['sourceUrl']}) | {claim.get('caveat', claim.get('eligibilityReason', '—'))} |"
    for claim in provider_claims
)
raw_data = f"""# ValueRank {VERSION} Raw Data

**Version:** {VERSION} · **Updated:** {DATE} · **AA DeepSWE chart observed:** {deepswe_updated} · **AA source:** [{aa_version}]({AA_METHODOLOGY_URL})

This is a selective publication update with mixed source dates. Earlier AA and DeepSWE observations remain September 29–30 captures; the newly added MiMo AA observations and AA displayed frontier were captured October 8. Bug Hunt's base snapshot remains pinned separately from the selectively added MiMo owner run notes observed October 7. The publication date does not imply that all benchmark rows were recaptured October 8. Per-model AA dates, precision, and source notes appear below; rounded public chart/tooltips preserve their displayed precision and do not establish hidden unrounded payload values.

The AA chart publishes {len(deepswe_configurations)} DeepSWE v1.1 agent/model configurations; {deepswe_overlap_n} exact model variants map to this {source_n}-model ValueRank comparison roster. The main score ranks {n} models with both an exact AA DeepSWE result and a Bug Hunt owner result; the other candidates remain source-only: {unranked_names}. Raw AA values keep their source units: Elo fields remain Elo, and ratio fields are shown as percentages. **{aa_index_estimated_models}** has an AA Intelligence Index estimate; it is labelled in the matrix. Benchmark-owner results, estimates, and provider claims remain source-typed.

## DeepSWE v1.1 AA chart configurations

AA publishes 25 of 25 configurations in the visible chart. Pass@1 is averaged across three attempts per task. Exact model-version mismatches and composite-agent configurations remain separate from ValueRank model-family rows.

| # | Agent | Evaluated model variant | Effort | Pass@1 | ValueRank mapping | Mapping note |
|---:|---|---|---|---:|---|---|
{deepswe_chart_table()}

## Selected AA pages

| Model | AA slug | AA effort | Source |
|---|---|---|---|
{aa_variant_rows}

### AA observation dates and precision

| Model | Source observation | Capture precision | Capture note |
|---|---|---|---|
{aa_evidence_rows}

## AA source input matrix

| # | Model | AA DeepSWE agent / variant / effort | DeepSWE pass@1 (AA) | AA-Briefcase Elo | GDPval-AA v2.1 | AutomationBench-AA | AA Terminal-Bench 4.0 | AA Terminal-Bench 2.1 legacy | τ³-Banking legacy | SciCode | GDP.pdf all-pass | AA-LCR v1.1 | HLE | GPQA legacy | CritPt | Omni Accuracy | Omni Non-Hallucination | AA Index | AA eval cost | Speed tok/s |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
{raw_rows}

## {md_benchmark_link('LiveBench')} external component

{md_benchmark_link('LiveBench')} release **{livebench_document['release']}** supplies the four-task Instruction Following mean and its seven-category Overall Score. Cost is the official **Cost Per Successful Task** field. The pinned table matches **{livebench_document['matchedN']}/{livebench_document['cohortN']}** ranked models and includes **{livebench_supplemental_label}** outside that cohort: **{livebench_supplemental_text}**.

| Model | LiveBench variant | Instruction Following | Overall Score | Cost Per Successful Task |
|---|---|---:|---:|---:|
{livebench_raw_rows}

LiveBench Pareto frontier (Overall Score vs Cost Per Successful Task): **{livebench_pareto_text}**.

## {md_benchmark_link('Bug Hunt Bench')} external component

The benchmark owner reports planted bugs fixed out of 105 across two repositories. This snapshot has **{bug_hunt_source_matches_n}/{source_n}** eligible exact selected-variant Bug Hunt results; **{bug_hunt_ranking['matchedN']}** also have an exact AA DeepSWE variant and enter the main score and emphasis view. The base snapshot is pinned to [scoreboard commit {bug_hunt_ranking['sourceCommit']}]({bug_hunt_document['sources']['scoreboard']}); selectively added MiMo records link to their individual owner notes at commit `7dd3c23a4c86a3fac586707d01129bf549bae325`, observed October 7. Per-record links preserve each source snapshot. The {len(unranked_models)} models without full overlap remain unranked: {unranked_names}.

| Model | Fixed / 105 | Runs / aggregation | Evaluated model | Effort and status | Harness | Route | Coverage |
|---|---:|---|---|---|---|---|---|
{bug_hunt_raw_table()}

Where no eligible selected-variant result exists, the model receives no inferred or neutral score. MiMo Flash has an owner default-route result (23.3/105, mean of three); its reasoning state was unasserted and untested, so equivalence to the selected AA reasoning variant remains unresolved and the owner result is shown separately. Provider-claim eligibility remains a separate exact-version and exact-variant audit.

## {md_benchmark_link('Terminal-Bench 4.0')} external component

The current official {md_benchmark_link('Terminal-Bench 4.0')} snapshot contains **{tb4_document['rowN']} rows** and overlaps **{tb4_document['matchedN']}/{tb4_document['cohortN']}** ranked models. It replaces the old standalone TB2.1 publication; the AA source matrix above keeps its v2.1 field only as explicit AA-source provenance.

| Rank | Model | Agent | Resolution rate | Tokens | Cost |
|---:|---|---|---:|---:|---:|
{tb4_raw_rows}

## Provider claims (separate from benchmark-owner results)

The ledger contains **{len(eligible_provider_claims)} ranking-eligible provider claim** and separately records claims that fail version, implementation, or evaluated-variant checks. The eligible DeepSeek value is a V4.1-Flash Terminal-Bench 4.0 claim for the current `deepseek-v4-flash` API alias; it is not a direct result for the retired V4 Flash model. Google’s GDP.pdf and AutomationBench claims remain audit-only because the model card does not establish the selected medium effort and exact AA component implementation.

| Benchmark and version | Cohort model | Evaluated model | Provider value | Status | Source type | Source | Caveat |
|---|---|---|---:|---|---|---|---|
{provider_claim_rows}

## Benchmark evaluation cost (score input)

The API Costs baseline uses AA total evaluation cost in USD. AA cost is available for **{cost_coverage.get('availableN', '—')}/{cost_coverage.get('cohortN', n)}** ranked models; missing values are **{cost_missing_text}**. Plan Costs divides the same AA cost by each model's highest eligible subscription Value Multiple. No DeepSWE leaderboard cost is used.

| Model | AA evaluation cost (USD) | AA cost penalty | Composite cost |
|---|---:|---:|---:|
{chr(10).join(f"| {m['name']} | {fnum(m.get('aaEvalCost'))} | {fnum(m.get('aaCostNorm'))} | {fnum(m.get('costComposite'))} |" for m in models)}

## Supplemental Artificial Analysis coverage

These fields are preserved for future analysis but remain outside the primary score because they are incomplete across the current cohort or are not separate ValueRank dimensions. AA-Briefcase and GDP.pdf are current v4.3.2 source components represented in the raw matrix; GPQA Diamond is retained as an explicitly labelled legacy ValueRank input. LiveBench and Terminal-Bench 4.0 are external coverage-only components under the same no-imputation policy.

| Field | Available | Missing models | Role |
|---|---:|---|---|
{supplemental_rows}

## Dropped primary candidate

| Dimension | Missing model | Treatment |
|---|---|---|
{drop_text}

Missing values are intentionally represented as null; no old-version, model-family, median, or neutral-fill substitution is used.

## Machine-readable artifacts

- [.refresh/v1.4/aa_deepswe.json](.refresh/v1.4/aa_deepswe.json): AA Coding Agent Index v1.5 DeepSWE v1.1 chart, all 25 configurations and exact model-variant mappings
- [.refresh/v1.4/aa_metrics.json](.refresh/v1.4/aa_metrics.json): decoded current AA model payloads
- [.refresh/v1.4/scores.json](.refresh/v1.4/scores.json): normalized scores and rankings
- [.refresh/v1.4/coverage_matrix.json](.refresh/v1.4/coverage_matrix.json): primary and supplemental availability
- [.refresh/v1.4/livebench.json](.refresh/v1.4/livebench.json): pinned LiveBench task/category/cost snapshot and Pareto data
- [.refresh/v1.4/tb4.json](.refresh/v1.4/tb4.json): normalized official Terminal-Bench 4.0 rendered leaderboard
- [.refresh/v1.4/bug_hunt.json](.refresh/v1.4/bug_hunt.json): pinned Bug Hunt scoreboard, exact matches, and explicit mismatches
- [research/2026-09-29-valuerank-refresh-v4-3-2/README.md](research/2026-09-29-valuerank-refresh-v4-3-2/README.md): v4.3.2 source-change, evidence, and scoring record
- [.refresh/v1.4/provider_claims.json](.refresh/v1.4/provider_claims.json): provider claim values, source URLs, eligibility, and caveats
- [.refresh/v1.4/deepswe.json](.refresh/v1.4/deepswe.json): historical DeepSWE Best snapshot retained for audit only; it is not used for current DeepSWE scores
- [.refresh/v1.4/tb4-browser-2026-09-29.json](.refresh/v1.4/tb4-browser-2026-09-29.json): built-in browser Terminal-Bench snapshot
"""
(ROOT / "raw-data.md").write_text(raw_data + aa_reconciliation_md)


# Existing interactive publication shell. Data constants and model data are
# regenerated to prevent stale v1.3 UI.
site_path = ROOT / "site" / "index.html"
html = site_path.read_text()

cost_basis_css = r"""    /* API-price versus subscription-plan cost switcher */
    .cost-basis-control {
      display:flex; align-items:center; gap:12px; flex-wrap:wrap; width:100%;
      padding:12px 14px; border:1px solid var(--border); border-radius:var(--radius);
      background:var(--bg-card); margin-bottom:14px;
    }
    .cost-basis-label { font-size:11px; font-weight:700; letter-spacing:.06em; text-transform:uppercase; color:var(--text-secondary); }
    .cost-basis-options { display:inline-flex; gap:3px; padding:3px; border:1px solid var(--border); border-radius:999px; background:var(--bg); }
    .cost-basis-btn {
      border:0; border-radius:999px; background:transparent; color:var(--text-dim); cursor:pointer;
      font:600 12px var(--font-body); padding:6px 12px; transition:background .2s,color .2s,box-shadow .2s;
    }
    .cost-basis-btn:hover { color:var(--text-primary); }
    .cost-basis-btn:focus-visible { outline:2px solid var(--accent-light); outline-offset:2px; }
    .cost-basis-btn.active { background:var(--accent); color:#fff; box-shadow:0 1px 4px rgba(0,0,0,.18); }
    .cost-basis-context { flex:1 1 280px; color:var(--text-dim); font-size:11px; line-height:1.5; }
    .cost-cell { display:inline-flex; flex-direction:column; align-items:flex-start; gap:2px; line-height:1.15; }
    .cost-meta { color:var(--text-dim); font-size:9px; line-height:1.25; max-width:180px; white-space:normal; }
    .cost-score { color:var(--text-dim); font-size:9px; }
"""
if "/* API-price versus subscription-plan cost switcher */" not in html:
    html = html.replace("    /* CA Cost + Value columns */", cost_basis_css + "    /* CA Cost + Value columns */", 1)

cost_basis_markup = r"""    <div class="cost-basis-control" id="cost-basis-control" role="group" aria-labelledby="cost-basis-label">
      <span class="cost-basis-label" id="cost-basis-label">Cost basis</span>
      <div class="cost-basis-options">
        <button type="button" class="cost-basis-btn active" data-cost-basis="api" aria-pressed="true">API Costs</button>
        <button type="button" class="cost-basis-btn" data-cost-basis="plan" aria-pressed="false">Plan Costs</button>
      </div>
      <span class="cost-basis-context" id="cost-basis-context">AA total evaluation cost at API rates; the default cost-weighted score uses the API-cost rank.</span>
    </div>
"""
if 'id="cost-basis-control"' not in html:
    html = html.replace('    <div class="table-controls">', cost_basis_markup + '    <div class="table-controls">', 1)
html = html.replace(
    '<th data-col="evalCost">Composite Cost (0-100)</th>',
    '<th data-col="evalCost">Cost <span id="cost-basis-table-label">(API Costs)</span></th>',
    1,
)

weight_by_key = {weight["key"]: weight for weight in weights}
SITE_DIM_META = {
    "costComposite": ("costComposite", "Cost", "Composite Cost", "cost"),
    "omniNonHallucination": ("omniNonHallucination", "NonHalluc", "AA-Omniscience Non-Hallucination Rate", "rely"),
    "omniAccuracy": ("omniAccuracy", "OmniAcc", "AA-Omniscience Accuracy", "rely"),
    "terminalBenchV4": ("terminalBenchV4", "Terminal4", "Terminal-Bench 4.0", "code"),
    "livebenchInstructionFollowing": ("livebenchInstructionFollowing", "LiveBench IF", "Instruction Following (LiveBench)", "language"),
    "bugHuntFixedOf105": ("bugHuntFixedOf105", "Bug Hunt", "Bug Hunt Bench bugs fixed out of 105", "code"),
    "deepswePassAt1": ("deepswePassAt1", "DeepSWE", "DeepSWE pass@1", "code"),
    "gdpvalV21": ("gdpvalV21", "GDPv2.1", "GDPval-AA v2.1", "code"),
    "automationBenchAA": ("automationBenchAA", "AutoBench", "AutomationBench-AA", "code"),
    "aaLcr": ("aaLcr", "LCR", "AA-LCR v1.1", "code"),
    "hle": ("hle", "HLE", "Humanity's Last Exam", "intel"),
    "gpqaDiamond": ("gpqaDiamond", "GPQA", "GPQA Diamond (legacy)", "intel"),
    "scicode": ("scicode", "Sci", "SciCode", "intel"),
    "critpt": ("critpt", "CritPt", "CritPt", "intel"),
    "intelligenceIndex": ("intelligenceIndex", "AAI", "Artificial Analysis Intelligence Index", "prod"),
    "speed": ("speed", "Speed", "AA output speed (tok/s)", "prod"),
}
SITE_DIM_LINKS = {
    "Composite Cost": None,
    "AA-Omniscience Non-Hallucination Rate": BENCHMARK_URLS["AA-Omniscience Non-Hallucination Rate"],
    "DeepSWE pass@1": BENCHMARK_URLS["DeepSWE pass@1"],
    "GDPval-AA v2.1": BENCHMARK_URLS["GDPval-AA v2.1"],
    "AutomationBench-AA": BENCHMARK_URLS["AutomationBench-AA"],
    "Terminal-Bench 4.0": BENCHMARK_URLS["Terminal-Bench 4.0"],
    "Instruction Following (LiveBench)": BENCHMARK_URLS["LiveBench"],
    "Bug Hunt Bench bugs fixed out of 105": BENCHMARK_URLS["Bug Hunt Bench"],
    "AA-LCR v1.1": BENCHMARK_URLS["AA-LCR v1.1"],
    "AA-Omniscience Accuracy": BENCHMARK_URLS["AA-Omniscience Accuracy"],
    "Humanity's Last Exam": BENCHMARK_URLS["Humanity's Last Exam"],
    "GPQA Diamond (legacy)": BENCHMARK_URLS["GPQA Diamond (legacy)"],
    "CritPt": BENCHMARK_URLS["CritPt"],
    "Artificial Analysis Intelligence Index": BENCHMARK_URLS["Artificial Analysis Intelligence Index"],
    "AA output speed (tok/s)": BENCHMARK_URLS["AA output speed (tok/s)"],
}
unknown_site_dims = [weight["key"] for weight in weights if weight["key"] not in SITE_DIM_META]
if unknown_site_dims:
    raise SystemExit(f"site dimension metadata missing: {unknown_site_dims}")
SITE_DIMS = [SITE_DIM_META[weight["key"]] for weight in weights]
speed_dim_idx = next((index for index, item in enumerate(SITE_DIMS) if item[0] == "speed"), -1)
site_models = []
for model, cost_fields in zip(models, plan_cost_fields):
    site_models.append({
        "rank": model["rank"],
        "name": model["name"],
        "shortName": model["shortName"],
        "developer": model["developer"],
        "evalCost": model["costComposite"],
        "aaEvalCost": round(model["aaEvalCost"], 2) if model.get("aaEvalCost") is not None else None,
        "deepSweCost": model["deepsweCost"],
        "deepSwePassAt1Pct": model.get("deepswePassAt1Pct"),
        "apiCost": cost_fields["apiCost"],
        "planCost": cost_fields["planCost"],
        "planComparableCost": cost_fields["planComparableCost"],
        "apiCostScore": cost_fields["apiCostScore"],
        "planCostScore": cost_fields["planCostScore"],
        "planCostFallback": cost_fields["planCostFallback"],
        "planRoute": cost_fields["planRoute"],
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
        "missingCount": sum(1 for weight in weights if weight["key"] not in model["dims"]),
        "dims": [model["dims"][dim_key] for dim_key, _key, _full, _cat in SITE_DIMS],
        "isMissing": [False] * len(SITE_DIMS),
        "vRanks": {"v70": None, "v80": None, "v90": None, "v100": None, "v110": None, "v120": None, "v130": None, "v131": None, "v140": None, "v150": ranking_history.get(model["id"]), "v160": None, "v170": None, "v190": ranking_history_v190.get(model["id"]), "v191": ranking_history_v191.get(model["id"]), "v192": ranking_history_v192.get(model["id"]), "v193": model.get("rank")},
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
    f"<tr><td>{html_escape(record['name'])}</td><td class=\"mono\">{html_escape(record['livebenchModel'])}</td><td class=\"mono\">{record['instructionFollowingScore']:.2f}</td><td class=\"mono\">{record['overallScore']:.2f}</td><td class=\"mono\">&#36;{record['costPerSuccessfulTaskUsd']:.4f}</td><td>{'Frontier' if record['modelId'] in livebench_document['pareto'] else '—'}</td></tr>"
    for record in livebench_rows
)
bug_hunt_site_table_rows = "\n".join(
    f"<tr><td>{item['rank']}</td><td>{html_external_link(item['name'], record.get('sourceUrl', BUG_HUNT_URL))}</td>"
    f"<td class=\"mono\">{record['fixedOf105']:g}/105</td>"
    f"<td class=\"mono\">{item['emphasisScore']:.1f}</td><td>n={record['sampleN']} ({html_escape(record['aggregation'])})</td>"
    f"<td>{html_escape(str(record['effort']))} ({html_escape(str(record['effortStatus']))})</td>"
    f"<td>{html_escape(record['harness'])} / {html_escape(record['route'])}</td><td>{item['primaryRank']}</td></tr>"
    for item in bug_hunt_ranking["ranking"]
    for record in [bug_hunt_records[item["modelId"]]]
)

plan_site_meta = {
    "asOf": plan_summary["asOf"],
    "routeCount": plan_summary["routeCount"],
    "supportedModelCount": plan_summary["supportedModelCount"],
    "fallbackModelCount": plan_summary["fallbackModelCount"],
    "totalModelCount": n,
    "mixId": plan_summary["mixId"],
}

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
dim_links_js = "const DIM_LINKS = " + json.dumps([SITE_DIM_LINKS.get(item[2]) for item in SITE_DIMS]) + ";"
if re.search(r"const DIM_LINKS\s*=\s*\[[^\]]*\];", html):
    html = replace_once(html, r"const DIM_LINKS\s*=\s*\[[^\]]*\];", dim_links_js, "DIM_LINKS")
else:
    html = html.replace("const DIM_CAT = " + json.dumps([item[3] for item in SITE_DIMS]) + ";", "const DIM_CAT = " + json.dumps([item[3] for item in SITE_DIMS]) + ";\n" + dim_links_js, 1)
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
html = replace_once(html, r"const SPEED_DIM_IDX\s*=\s*[^;]+;[^\n]*", "const SPEED_DIM_IDX = " + str(speed_dim_idx) + ";", "SPEED_DIM_IDX")

cost_switcher_js = r"""// COST BASIS SWITCHER START
const PLAN_COST_META = PLAN_META_JSON;
let costBasis = 'api';
let costWeightPct = COST_WEIGHT_DEFAULT;

function costBasisLabel() {
  return costBasis === 'plan' ? 'Plan Costs' : 'API Costs';
}

function planRouteFor(model) {
  return model.planRoute || null;
}

function hasPlanRoute(model) {
  return planRouteFor(model) !== null && Number.isFinite(Number(model.planCost));
}

function activeCostUsd(model) {
  return costBasis === 'plan' && hasPlanRoute(model) ? Number(model.planCost) : Number(model.apiCost);
}

function activeCostScore(model) {
  const candidate = costBasis === 'plan' ? model.planCostScore : model.apiCostScore;
  if (candidate !== null && candidate !== undefined && Number.isFinite(Number(candidate))) return Number(candidate);
  if (model.apiCostScore !== null && model.apiCostScore !== undefined && Number.isFinite(Number(model.apiCostScore))) return Number(model.apiCostScore);
  const base = model.dims?.[0];
  return base !== null && base !== undefined && Number.isFinite(Number(base)) ? Number(base) : 50;
}

function formatValueMultiple(route) {
  return route ? Number(route.valueMultiple).toLocaleString(undefined, { maximumFractionDigits: 3 }) + '×' : '—';
}

function activeCostRouteLabel(model) {
  if (costBasis !== 'plan') return 'AA evaluation cost at API rates';
  const route = planRouteFor(model);
  return route ? `${route.planLabel} · ${formatValueMultiple(route)}` : 'API fallback · no verified subscription route';
}

function costBasisTooltip(model) {
  const api = fmtUsd(model.apiCost, { minimumFractionDigits: 2, maximumFractionDigits: 2 });
  const plan = model.planCost == null
    ? 'unavailable'
    : fmtUsd(model.planCost, { minimumFractionDigits: 2, maximumFractionDigits: 2 });
  const route = planRouteFor(model);
  const routeText = route
    ? `${route.planLabel} (${formatValueMultiple(route)}; ${route.evidenceClass})`
    : 'No verified subscription route; API fallback';
  return `API Cost: ${api}<br>Plan Cost: ${plan}<br>Route: ${routeText}`;
}

function recomputeCostState() {
  MODELS.forEach(model => {
    model.activeCostUsd = activeCostUsd(model);
    model.evalCost = activeCostScore(model);
    model.dims[0] = model.evalCost;
    model.costTier = compositeCostTier(model.evalCost);
    model.activeScore = computeNewScore(model, costWeightPct);
    model.overallScore = model.activeScore;
  });
  const sorted = [...MODELS].sort((a, b) => b.activeScore - a.activeScore || a.name.localeCompare(b.name));
  sorted.forEach((model, index) => { model.rank = index + 1; });
  tableModels = MODELS.map(model => ({ ...model, score: model.activeScore }));
}

function updateCostBasisUI() {
  const label = costBasisLabel();
  document.querySelectorAll('[data-cost-basis]').forEach(button => {
    const active = button.dataset.costBasis === costBasis;
    button.classList.toggle('active', active);
    button.setAttribute('aria-pressed', active ? 'true' : 'false');
  });
  const tableLabel = document.getElementById('cost-basis-table-label');
  if (tableLabel) tableLabel.textContent = `(${label})`;
  const context = document.getElementById('cost-basis-context');
  if (context) {
    context.textContent = costBasis === 'plan'
      ? `AA total evaluation cost ÷ highest eligible Value Multiple. ${PLAN_COST_META.supportedModelCount}/${PLAN_COST_META.totalModelCount} models have a verified plan route; the rest remain API-priced.`
      : 'AA total evaluation cost at API rates; cost-weighted scores use the API-cost rank.';
  }
  const note = document.getElementById('cost-note');
  if (note) note.textContent = `${label} · Cost weight: ${costWeightPct.toFixed(2)}%${costBasis === 'plan' ? ` · ${PLAN_COST_META.fallbackModelCount} API fallback${PLAN_COST_META.fallbackModelCount === 1 ? '' : 's'}` : ''}`;
  document.querySelectorAll('[data-cost-basis-label]').forEach(element => { element.textContent = label; });
}

function applyCostBasis(nextBasis) {
  costBasis = nextBasis === 'plan' ? 'plan' : 'api';
  recomputeCostState();
  updateCostBasisUI();
}

function rerenderCostBasisViews() {
  recomputeCostState();
  updateCostBasisUI();
  if (typeof renderTable === 'function') renderTable();
  if (typeof renderHeroPodium === 'function') renderHeroPodium();
  const costChartKeys = ['pareto', 'decomp', 'displacement', 'heatmap', 'bubble', 'frontier2'];
  if (typeof rendered !== 'undefined' && typeof chartRenderers !== 'undefined') {
    costChartKeys.forEach(key => {
      if (!rendered[key] || !chartRenderers[key]) return;
      try { chartRenderers[key](); rendered[key] = true; }
      catch (error) { console.error('Cost-basis chart render failed:', key, error); }
    });
  }
  const dataHeatmap = document.getElementById('chart-heatmap-data');
  if (dataHeatmap && typeof renderHeatmap === 'function') renderHeatmap('chart-heatmap-data', 480);
  if (typeof lucide !== 'undefined') lucide.createIcons();
}

function setCostBasis(nextBasis) {
  applyCostBasis(nextBasis);
  try { localStorage.setItem('vr-cost-basis', costBasis); } catch (error) { /* storage is optional */ }
  rerenderCostBasisViews();
}

function initCostBasis() {
  document.querySelectorAll('[data-cost-basis]').forEach(button => {
    button.addEventListener('click', () => setCostBasis(button.dataset.costBasis));
  });
  let saved = 'api';
  try { saved = localStorage.getItem('vr-cost-basis') || 'api'; } catch (error) { /* storage is optional */ }
  applyCostBasis(saved);
}
// COST BASIS SWITCHER END""".replace("PLAN_META_JSON", json.dumps(plan_site_meta, ensure_ascii=False)).replace("COST_WEIGHT_DEFAULT", f"{cost_weight['weightPct']:.4f}")
cost_switcher_pattern = r"// COST BASIS SWITCHER START[\s\S]*?// COST BASIS SWITCHER END"
if re.search(cost_switcher_pattern, html):
    html = replace_once(html, cost_switcher_pattern, cost_switcher_js, "cost basis switcher")
else:
    html = html.replace("const SPEED_DIM_IDX = " + str(speed_dim_idx) + ";", "const SPEED_DIM_IDX = " + str(speed_dim_idx) + ";\n\n" + cost_switcher_js, 1)

# Keep every cost-bearing interactive surface honest when the basis changes.
# These replacements are intentionally idempotent because the emitter reads
# its own generated shell on subsequent refreshes.
dynamic_cost_chart_replacements = [
    (
        "  return `AA Eval Cost: ${fmtUsd(m.aaEvalCost)}<br>DeepSWE Avg Cost: ${fmtUsd(m.deepSweCost, { minimumFractionDigits: 2, maximumFractionDigits: 2 })}`;",
        "  return `Selected ${costBasisLabel()}: ${fmtUsd(m.activeCostUsd, { minimumFractionDigits: 2, maximumFractionDigits: 2 })}<br>${costBasisTooltip(m)}`;",
    ),
    (
        "    fmtUsd(m.deepSweCost, { minimumFractionDigits: 2, maximumFractionDigits: 2 })\n  ];",
        "    fmtUsd(m.deepSweCost, { minimumFractionDigits: 2, maximumFractionDigits: 2 }),\n    costBasisTooltip(m)\n  ];",
    ),
    (
        "    '<b>%{customdata[0]}</b><br>Quality: %{y:.1f}<br>Composite Cost: %{x:.1f}<br>Overall: %{customdata[1]}<br>AA Eval: %{customdata[3]}<br>DeepSWE: %{customdata[4]}<br>Missing scored cells: %{customdata[2]}<extra></extra>';",
        "    '<b>%{customdata[0]}</b><br>Quality: %{y:.1f}<br>' + costBasisLabel() + ': %{x:.1f}<br>Overall: %{customdata[1]}<br>%{customdata[5]}<br>Missing scored cells: %{customdata[2]}<extra></extra>';",
    ),
    (
        "    '<b>%{customdata[0]}</b><br>Quality: %{y:.1f}<br>Composite Cost: %{x:.1f}<br>Overall: %{customdata[1]}<br>AA Eval: %{customdata[3]}<br>DeepSWE: %{customdata[4]}<extra>Frontier</extra>';",
        "    '<b>%{customdata[0]}</b><br>Quality: %{y:.1f}<br>' + costBasisLabel() + ': %{x:.1f}<br>Overall: %{customdata[1]}<br>%{customdata[5]}<extra>Frontier</extra>';",
    ),
    (
        "title: { text: 'ValueRank Pareto Frontier — Quality vs Composite Cost', font: plotlyTitle(14) },",
        "title: { text: 'ValueRank Pareto Frontier — Quality vs ' + costBasisLabel(), font: plotlyTitle(14) },",
    ),
    (
        "      title: 'Composite Cost (0–100, lower better)',",
        "      title: costBasisLabel() + ' (0–100, lower better)',",
    ),
    (
        "     title:{text:'Score Decomposition by Macro-Category', font:plotlyTitle(14)},",
        "     title:{text:'Score Decomposition by Macro-Category (' + costBasisLabel() + ')', font:plotlyTitle(14)},",
    ),
    (
        "     title:{text:'Rank Displacement: Quality Rank vs. Overall Rank (with 25% Cost Weight)', font:plotlyTitle(14)},",
        "     title:{text:'Rank Displacement: Quality Rank vs. Overall Rank (with ' + costWeightPct + '% ' + costBasisLabel() + ' weight)', font:plotlyTitle(14)},",
    ),
    (
        "  const colLabels = colOrder.map(i => DIM_KEYS[i]);",
        "  const colLabels = colOrder.map(i => i === 0 ? costBasisLabel() : DIM_KEYS[i]);",
    ),
    (
        "'<br>Composite Cost: ' + m.evalCost.toFixed(1) + '<br>' + fmtAaDeepSweHover(m) + '<extra></extra>'",
        "'<br>' + costBasisLabel() + ': ' + m.evalCost.toFixed(1) + '<br>' + fmtAaDeepSweHover(m) + '<extra></extra>'",
    ),
    (
        "title:{text:'Speed × Quality × Cost (numeric AA speed only)', font:plotlyTitle(14)},",
        "title:{text:'Speed × Quality × ' + costBasisLabel() + ' (numeric AA speed only)', font:plotlyTitle(14)},",
    ),
    (
        "hovertemplate: MODELS.map(m => `<b>${m.name}</b><br>Quality: ${m.qualityScore}<br>Composite Cost: ${m.evalCost.toFixed(1)}<br>${fmtAaDeepSweHover(m)}<extra></extra>`),",
        "hovertemplate: MODELS.map(m => `<b>${m.name}</b><br>Quality: ${m.qualityScore}<br>${costBasisLabel()}: ${m.evalCost.toFixed(1)}<br>${fmtAaDeepSweHover(m)}<extra></extra>`),",
    ),
    (
        "hovertemplate: MODELS.map(m => `<b>${m.name}</b><br>Overall: ${m.overallScore}<br>Quality: ${m.qualityScore}<br>Change: ${(m.overallScore-m.qualityScore).toFixed(1)}<extra></extra>`),",
        "hovertemplate: MODELS.map(m => `<b>${m.name}</b><br>Overall: ${m.overallScore}<br>Quality: ${m.qualityScore}<br>${costBasisLabel()}: ${m.evalCost.toFixed(1)}<br>Change: ${(m.overallScore-m.qualityScore).toFixed(1)}<br>${fmtAaDeepSweHover(m)}<extra></extra>`),",
    ),
    (
        "title:{text:'Cost Impact: Quality Score (○) vs. Overall Score (◆) — Lines show effect of 25% cost weight', font:plotlyTitle(13)},",
        "title:{text:'Cost Impact: Quality Score (○) vs. Overall Score (◆) — Lines show effect of ' + costWeightPct + '% ' + costBasisLabel() + ' weight', font:plotlyTitle(13)},",
    ),
    (
        "    xaxis:{...getPlotlyLayout().xaxis, title:'Composite Cost (0-100)', range:[0,105]},",
        "    xaxis:{...getPlotlyLayout().xaxis, title:costBasisLabel() + ' (0-100)', range:[0,105]},",
    ),
    (
        "    annotations:[\n      {x:7.04, y:58.1, xref:'x', yref:'y', text:'MiMo +13.9 pts<br>(cost bonus)', font:{color:'#22c55e',size:9}, showarrow:true, arrowcolor:'#22c55e', ax:50, ay:20},\n      {x:80.37, y:51.8, xref:'x', yref:'y', text:'Opus 4.8 -14.5 pts<br>(cost penalty)', font:{color:'#ef4444',size:9}, showarrow:true, arrowcolor:'#ef4444', ax:0, ay:70},\n    ]",
        "    annotations:[]",
    ),
]
for old, new in dynamic_cost_chart_replacements:
    if old in html:
        html = html.replace(old, new, 1)

dynamic_hero_replacements = [
    (
        '<div class="podium-hero-meta">${m1.developer} · ${m1.costTier} · ${costBasisLabel()} ${fmtUsd(m1.activeCostUsd, {minimumFractionDigits:2, maximumFractionDigits:2})} · ${activeCostRouteLabel(m1)} · ${m1.evalCost.toFixed(1)} score · AA ${fmtUsd(m1.aaEvalCost, {maximumFractionDigits:0})} · DeepSWE ${fmtUsd(m1.deepSweCost, {minimumFractionDigits:2, maximumFractionDigits:2})}</div>',
        '<div class="podium-hero-meta">${m1.developer} · ${m1.costTier} · ${costBasisLabel()} ${fmtUsd(m1.activeCostUsd, {minimumFractionDigits:2, maximumFractionDigits:2})} · ${activeCostRouteLabel(m1)} · ${m1.evalCost.toFixed(1)} score · AA ${fmtUsd(m1.aaEvalCost, {maximumFractionDigits:0})} · DeepSWE v1.1 ${m1.deepSwePassAt1Pct == null ? "—" : Number(m1.deepSwePassAt1Pct).toFixed(1) + "%"}</div>',
    ),
    (
        '<div class="podium-runner-meta">${m.developer} · $${m.evalCost.toFixed(1)} composite</div>',
        '<div class="podium-runner-meta">${m.developer} · ${costBasisLabel()} ${fmtUsd(m.activeCostUsd, {minimumFractionDigits:2, maximumFractionDigits:2})} · ${activeCostRouteLabel(m)}</div>',
    ),
]
for old, new in dynamic_hero_replacements:
    if old in html:
        html = html.replace(old, new, 1)

ranking_table_function = r"""function renderTable() {
  let models = tableModels.filter(m => {
    if (tierFilter === 'all') return true;
    if (tierFilter === 'Expensive') return ['Expensive','Very Expensive','Ultra-Premium'].includes(m.costTier);
    return m.costTier === tierFilter;
  });
  models.sort((a,b) => sortDir * (a[sortCol] > b[sortCol] ? 1 : a[sortCol] < b[sortCol] ? -1 : 0));
  if (sortCol === 'rank' || sortCol === 'qualityRank' || sortCol === 'missingCount') {
    models.sort((a,b) => sortDir * (a[sortCol] - b[sortCol]));
  }
  if (sortCol === 'evalCost') models.sort((a,b) => sortDir * (a.evalCost - b.evalCost));
  if (sortCol === 'score') models.sort((a,b) => sortDir * (b.score - a.score));

  const tbody = document.getElementById('ranking-tbody');
  tbody.innerHTML = models.map((m, idx) => {
    const rank = idx + 1;
    const dispRank = sortCol === 'score' ? m.rank : rank;
    const rankCls = dispRank===1?'r1':dispRank===2?'r2':dispRank===3?'r3':'';
    const delta = m.qualityRank - m.rank;
    const deltaStr = delta > 0 ? `+${delta}▲` : delta < 0 ? `${delta}▼` : '—';
    const deltaCls = delta > 0 ? 'delta-up' : delta < 0 ? 'delta-down' : 'delta-same';
    const barW = Math.round((m.score/100)*100);
    const cost = activeCostUsd(m);
    const routeText = activeCostRouteLabel(m);
    return `<tr>
      <td><span class="rank-cell ${rankCls}">${dispRank}</span></td>
      <td>
        <div class="model-name">${m.name}</div>
        <div class="model-dev">${m.developer}</div>
      </td>
      <td>
        <div class="score-bar-wrap">
          <span class="score-val" style="color:${scoreColor(m.score)}">${m.score.toFixed(1)}</span>
          <div class="score-bar"><div class="score-bar-fill" style="width:${barW}%;background:${scoreColor(m.score)}"></div></div>
        </div>
      </td>
      <td><span class="mono" style="color:${scoreColor(m.qualityScore)}">${m.qualityScore.toFixed(1)}</span></td>
      <td><span class="quality-pill">#${m.qualityRank}</span></td>
      <td data-sort-value="${cost}">
        <span class="cost-cell">
          <span class="mono">${fmtUsd(cost, { minimumFractionDigits: 2, maximumFractionDigits: 2 })}</span>
          <span class="cost-meta">${routeText}</span>
          <span class="cost-score">Score ${m.evalCost.toFixed(1)}</span>
        </span>
      </td>
      <td><span class="tier-badge ${tierClass(m.costTier)}">${m.costTier}</span></td>
      <td><span class="missing-dots">${m.missingCount > 0 ? '⊘'.repeat(Math.min(m.missingCount,7)) + (m.missingCount > 7 ? '+' : '') + ` ${m.missingCount}` : '✓ Full'}</span></td>
    </tr>`;
  }).join('');
}"""
html = replace_once(html, r"function renderTable\(\) \{[\s\S]*?\n\}\n\nfunction initTable\(\)", ranking_table_function.rstrip() + "\n\nfunction initTable()", "ranking table")

cost_slider_function = r"""function initCostSlider() {
  const slider = document.getElementById('cost-slider');
  const valEl  = document.getElementById('slider-val');
  if (!slider) return;
  slider.addEventListener('input', () => {
    const cw = Number.parseFloat(slider.value);
    if (!Number.isFinite(cw)) return;
    costWeightPct = cw;
    if (valEl) valEl.textContent = `${cw.toFixed(2)}%`;
    applyCostBasis(costBasis);
    rerenderCostBasisViews();
  });
}"""
html = replace_once(html, r"function initCostSlider\(\) \{[\s\S]*?\n\}(?=\n\n// ─+)", cost_slider_function.rstrip(), "cost slider")

dim_table_function = r"""function renderDimTable() {
  const catLabels = { cost:'Cost', rely:'Reliability', code:'Code/Agentic', prod:'Production', intel:'Intelligence' };
  const catClasses = { cost:'cat-cost', rely:'cat-rely', code:'cat-code', prod:'cat-prod', intel:'cat-intel' };
  const tbody = document.getElementById('dim-table-body');
  tbody.innerHTML = DIM_KEYS.map((k,i) => {
    const label = DIM_LINKS[i]
      ? `<a href="${DIM_LINKS[i]}" target="_blank" rel="noopener">${DIM_FULL[i]}</a>`
      : DIM_FULL[i];
    return `
    <tr>
      <td><strong>${label}</strong> <span class="mono text-muted" style="font-size:10px;">(${k})</span></td>
      <td>
        <div style="display:flex;align-items:center;gap:6px;">
          <div class="w-bar" style="width:${DIM_WEIGHTS[i]*3}px;"></div>
          <span class="mono">${DIM_WEIGHTS[i]}%</span>
        </div>
      </td>
      <td><span class="cat-badge ${catClasses[DIM_CAT[i]]}">${catLabels[DIM_CAT[i]]}</span></td>
    </tr>`;
  }).join('');
}"""
html = replace_once(html, r"function renderDimTable\(\) \{[\s\S]*?\n\}", dim_table_function.rstrip(), "dimension table")

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
      { fontSize: 9, markerRadius: 24, safety: 1.12 },
    );
    const annotations = [...(layout.annotations || []), ...modelAnnotations];
    return Plotly.relayout(gd, { annotations }).then(() => repairCollisionSafeLabelAnnotations(gd, modelAnnotations));
  });
}
"""
html = replace_once(html, r"function renderBubble\(\) \{[\s\S]*?\n\}\n\n// ─+\n// CHART 6", speed_function + "\n// ─────────────────────────────────────────────\n// CHART 6", "speed chart")

# The renderer above is replaced as a whole, so apply its basis-aware labels
# after that replacement.  The remaining chart functions are patched here as
# well, after their source has been normalized by the earlier replacements.
post_renderer_cost_replacements = [
    (
        "     title:{text:'Score Decomposition by Macro-Category', font:plotlyTitle(14)},",
        "     title:{text:'Score Decomposition by Macro-Category (' + costBasisLabel() + ')', font:plotlyTitle(14)},",
    ),
    (
        "     title:{text:'Rank Displacement: Quality Rank vs. Overall Rank (with 25% Cost Weight)', font:plotlyTitle(14)},",
        "     title:{text:'Rank Displacement: Quality Rank vs. Overall Rank (with ' + costWeightPct + '% ' + costBasisLabel() + ' weight)', font:plotlyTitle(14)},",
    ),
    (
        "     hovertemplate:'<b>' + m.name + '</b><br>Speed: ' + Number(m.speed).toFixed(1) + ' tok/s<br>Speed percentile score: ' + speedScore(m).toFixed(1) + '<br>Quality: ' + m.qualityScore.toFixed(1) + '<br>Composite Cost: ' + m.evalCost.toFixed(1) + '<br>' + fmtAaDeepSweHover(m) + '<extra></extra>',",
        "     hovertemplate:'<b>' + m.name + '</b><br>Speed: ' + Number(m.speed).toFixed(1) + ' tok/s<br>Speed percentile score: ' + speedScore(m).toFixed(1) + '<br>Quality: ' + m.qualityScore.toFixed(1) + '<br>' + costBasisLabel() + ': ' + m.evalCost.toFixed(1) + '<br>' + fmtAaDeepSweHover(m) + '<extra></extra>',",
    ),
    (
        "     title:{text:'Speed × Quality × Cost (numeric AA speed only)', font:plotlyTitle(14)},",
        "     title:{text:'Speed × Quality × ' + costBasisLabel() + ' (numeric AA speed only)', font:plotlyTitle(14)},",
    ),
    (
        "  const colLabels = colOrder.map(i => DIM_KEYS[i]);",
        "  const colLabels = colOrder.map(i => i === 0 ? costBasisLabel() : DIM_KEYS[i]);",
    ),
]
for old, new in post_renderer_cost_replacements:
    if old in html:
        html = html.replace(old, new, 1)

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
    const annotations = buildCollisionSafeLabelAnnotations(points, gd, { fontSize: 9, markerRadius: 11, safety: 1.12 });
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
html = html.replace("Sep 4", "Sep 6")
html = html.replace("Sep 5", "Sep 6")
html = html.replace("ValueRank v1.4.0", f"ValueRank {VERSION}")
html = html.replace("Production AI Ranking Framework · v1.4.0", f"Production AI Ranking Framework · {VERSION}")
html = html.replace("v1.4.0 uses zero missing benchmark cells", f"{VERSION} uses zero missing benchmark cells")

if "try { initCostBasis(); } catch (e) { console.error(e); }" not in html:
    html = html.replace(
        "  if (document.getElementById('ranking-tbody')) {\n    try { renderHeroPodium(); } catch (e) { console.error(e); }",
        "  if (document.getElementById('ranking-tbody')) {\n    try { initCostBasis(); } catch (e) { console.error(e); }\n    try { renderHeroPodium(); } catch (e) { console.error(e); }",
        1,
    )
html = html.replace("v1.4.0 Release", f"{VERSION} Release")
html = html.replace("primary-source data in v1.4.0", f"primary-source data in {VERSION}")
html = html.replace("retained v1.4.0 dimension", f"retained {VERSION} dimension")
html = html.replace("in <strong>v1.4.0</strong>", f"in <strong>{VERSION}</strong>")
html = html.replace("v1.4.0 has <strong>no missing-data", f"{VERSION} has <strong>no missing-data")
html = html.replace("In <strong>v1.4.0</strong>", f"In <strong>{VERSION}</strong>")
html = html.replace("in v1.4.0", f"in {VERSION}")
html = html.replace("weighted average of 13 normalized", f"weighted average of {d} normalized")
html = html.replace("cost is constructed from normalized AA eval cost plus normalized DeepSWE average cost before rank-normalization.", f"cost uses {cost_mode_label} and is rank-normalized with lower cost better.")
html = html.replace("two-source cost composite", f"{cost_mode_label} cost composite")
html = html.replace("The composite cost term values models that stay efficient on both public pricing surfaces.", f"The composite cost term uses {cost_mode_label}.")
html = html.replace("September 5, 2026", DATE)
html = html.replace("v1.4.0 to", f"{VERSION} to")
html = html.replace("v === 'v1.4.0' ?", f"v === '{VERSION}' ?")
html = html.replace("Ranking History — v0.7 to v1.4.0", f"Ranking History — v0.7 to {VERSION}")
html = html.replace("x:'v1.4.0', y:1", f"x:'{VERSION}', y:1")
html = html.replace("text:'v1.4.0: 21 models · 12 dims'", f"text:'{VERSION}: {n} models · {d} dims'")
html = re.sub(r"const SPEED_DIM_IDX = [-0-9]+;.*", f"const SPEED_DIM_IDX = {speed_dim_idx};", html, count=1)
html = re.sub(
    r"const versions = \[[^;]*\];",
    "const versions = ['v0.7','v0.8','v0.9','v1.0','v1.1','v1.2','v1.3','v1.3.1','v1.4.0','v1.5.0','v1.6.0','v1.7.0','v1.9.0','v1.9.1','v1.9.2','v1.9.3'];",
    html,
    count=1,
)
html = re.sub(
    r"const vKeys = \[[^;]*\];",
    "const vKeys = ['v70','v80','v90','v100','v110','v120','v130','v131','v140','v150','v160','v170','v190','v191','v192','v193'];",
    html,
    count=1,
)

hero_desc = (
    f'ValueRank ranks <strong>{n} models</strong> with both exact AA DeepSWE v1.1 model-variant results and Bug Hunt results from a {source_n}-model AA-mapped comparison roster across a '
    f'<strong>zero-gap {d}-dimension set</strong>; Bug Hunt contributes {bug_hunt_weight["weightPct"]:.2f}% of the main score. {VERSION} uses '
    f'<strong>{html_external_link(aa_version, AA_METHODOLOGY_URL)}</strong> components plus DeepSWE performance; the score uses AA evaluation cost, with selectable API-price and subscription-plan cost views. '
    f'Speed is {"included in the score" if speed_in_primary else "excluded from the score"}; AA speed is numeric for {speed_selected_available_n}/{n} selected pages and missing for {speed_missing_text}. The incomplete dimensions {", ".join(item["label"] for item in dropped if item["label"] != "Speed")} remain supplemental because exact cohort coverage is incomplete.'
)
html = replace_once(html, r'<p class="hero-desc">[\s\S]*?</p>', f'<p class="hero-desc">\n          {hero_desc}\n        </p>', "hero copy")
html = replace_once(html, r'<div class="(?:nav-meta|vr-nav-meta)">[^<]*</div>', f'<div class="vr-nav-meta">{DATE} · {n} models · {d} dimensions</div>', "nav metadata")
html = replace_once(html, r'<span class="hero-statbar-num">\d+</span>\s*<span class="hero-statbar-label">Models Ranked', f'<span class="hero-statbar-num">{n}</span>\n        <span class="hero-statbar-label">Models Ranked', "model stat")
html = replace_once(html, r'<span class="hero-statbar-num">\d+</span>\s*<span class="hero-statbar-label">Scored Dimensions', f'<span class="hero-statbar-num">{d}</span>\n        <span class="hero-statbar-label">Scored Dimensions', "dimension stat")
html = replace_once(html, r'<span class="hero-statbar-num">(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) \d{1,2}</span>', f'<span class="hero-statbar-num">{SHORT_DATE}</span>', "date stat")

insight_bodies = [
    'The Pareto view highlights models that are not outperformed on both quality and the selected cost basis.',
    'Quality and overall scores separate benchmark performance from the selected cost view.',
    'Compare API Costs and Plan Costs with Quality to find the best fit for your usage.',
    f'{VERSION} uses <strong>{len(deepswe_configurations)} AA DeepSWE chart configurations</strong> and keeps <strong>{d} zero-gap dimensions</strong>; {"Speed is included" if speed_in_primary else "Speed is excluded"} because coverage is {speed_selected_available_n}/{n}.',
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
    (r'<div class="chart-desc"><strong>(?:ValueRank )?Pareto Frontier:</strong>[\s\S]*?</div>', f'<div class="chart-desc"><strong>ValueRank Pareto Frontier:</strong> Current frontier: <strong>{pareto_text}</strong>. Every other ranked model is dominated on composite cost versus quality.</div>'),
    (r'(<div class="chart-desc"><strong>Score Decomposition:</strong>)[\s\S]*?</div>', f'\\1 {VERSION} decomposes the weighted <strong>{d}-dimension</strong> score into Cost, Reliability, Agentic, Intelligence, and Platform macro-categories.</div>'),
    (r'(<div class="chart-desc"><strong>Dimension Heatmap:</strong>)[\s\S]*?</div>', f'\\1 All {n} models × {d} retained dimensions. Color = normalized rank score; every displayed cell is confirmed source data.</div>'),
    (r'(<div class="chart-desc"><strong>Version History:</strong>)[\s\S]*?</div>', f'\\1 Historical rank context through {VERSION}. The current point is a new benchmark-version snapshot, not a claim of score continuity.</div>'),
]
for pattern, replacement in chart_replacements:
    html = replace_once(html, pattern, replacement, "chart copy")
html = re.sub(
    r"(?:Quality vs Composite Cost — (?:ValueRank )?Pareto Frontier|ValueRank Pareto Frontier — Quality vs Composite Cost)",
    "ValueRank Pareto Frontier — Quality vs Composite Cost",
    html,
)

html = re.sub(
    r'(<div class="section-sub">)How scores are calculated(?: across)?[\s\S]*?(</div>)',
    rf'\1How scores are calculated across {d} current zero-gap dimensions, with explicit cost construction and coverage provenance.\2',
    html,
    count=1,
)
html = html.replace("Cost now uses a composite 0–100 scale built from normalized AA eval cost and normalized DeepSWE average cost per task.", site_cost_summary)
html = html.replace("For Cost, the raw input is a composite of normalized AA eval cost plus normalized DeepSWE average cost per task.", site_cost_raw_input)
html = html.replace("The 25% cost weight therefore now combines Artificial Analysis eval cost with DeepSWE average cost per task into a single cost-efficiency term.", site_cost_weight)
html = html.replace("⊘ Missing: %{customdata[2]}", "Missing scored cells: %{customdata[2]}")

# Apply the final cost-basis labels after every renderer and card replacement.
# Keeping these replacements at the end makes the generated artifact idempotent
# even when an earlier chart renderer is replaced wholesale.
final_cost_surface_replacements = [
    (
        "title:{text:'Score Decomposition by Macro-Category', font:plotlyTitle(14)},",
        "title:{text:'Score Decomposition by Macro-Category (' + costBasisLabel() + ')', font:plotlyTitle(14)},",
    ),
    (
        "title:{text:'Rank Displacement: Quality Rank vs. Overall Rank (with 25% Cost Weight)', font:plotlyTitle(14)},",
        "title:{text:'Rank Displacement: Quality Rank vs. Overall Rank (with ' + costWeightPct + '% ' + costBasisLabel() + ' weight)', font:plotlyTitle(14)},",
    ),
    (
        "hovertemplate:'<b>' + m.name + '</b><br>Speed: ' + Number(m.speed).toFixed(1) + ' tok/s<br>Speed percentile score: ' + speedScore(m).toFixed(1) + '<br>Quality: ' + m.qualityScore.toFixed(1) + '<br>Composite Cost: ' + m.evalCost.toFixed(1) + '<br>' + fmtAaDeepSweHover(m) + '<extra></extra>',",
        "hovertemplate:'<b>' + m.name + '</b><br>Speed: ' + Number(m.speed).toFixed(1) + ' tok/s<br>Speed percentile score: ' + speedScore(m).toFixed(1) + '<br>Quality: ' + m.qualityScore.toFixed(1) + '<br>' + costBasisLabel() + ': ' + m.evalCost.toFixed(1) + '<br>' + fmtAaDeepSweHover(m) + '<extra></extra>',",
    ),
    (
        "title:{text:'Speed × Quality × Cost (numeric AA speed only)', font:plotlyTitle(14)},",
        "title:{text:'Speed × Quality × ' + costBasisLabel() + ' (numeric AA speed only)', font:plotlyTitle(14)},",
    ),
    (
        "const colLabels = colOrder.map(i => DIM_KEYS[i]);",
        "const colLabels = colOrder.map(i => i === 0 ? costBasisLabel() : DIM_KEYS[i]);",
    ),
    (
        "Cost now uses a 0–100 rank scale built from normalized DeepSWE average cost per task; captured AA total evaluation costs remain source-only because v4.2 coverage is incomplete.",
        site_cost_summary,
    ),
    (
        "Every other ranked model is dominated on composite cost versus quality.",
        "Every other ranked model is dominated on the selected <span data-cost-basis-label>API Costs</span> versus quality.",
    ),
    (
        "Which models are fast AND high-quality AND cheap on the composite-cost basis?",
        "Which models are fast AND high-quality AND cheap on the selected <span data-cost-basis-label>API Costs</span> basis?",
    ),
    (
        "Color = cost tier. Hover for raw AA cost and DeepSWE average-cost components.",
        "Color = cost tier. Hover for the selected cost basis, route provenance, and source components.",
    ),
    (
        "X-axis = composite cost.",
        "X-axis = <span data-cost-basis-label>API Costs</span> score.",
    ),
    (
        "The composite cost term uses DeepSWE-only.",
        "The composite cost term uses the selected cost basis; Plan Costs divide API task cost by the highest eligible Value Multiple.",
    ),
    (
        "and the DeepSWE-only cost composite.",
        "and the selected <span data-cost-basis-label>API Costs</span> cost composite.",
    ),
    (
        "function compositeCostTier(cost) {\n  if (cost <= 15) return 'Budget';\n  if (cost <= 22) return 'Near-Budget';\n  if (cost <= 35) return 'Mid-Range';\n  if (cost <= 55) return 'Premium';\n  return 'Expensive';\n}",
        "function compositeCostTier(cost) {\n  const costPenalty = 100 - Number(cost);\n  if (costPenalty <= 15) return 'Budget';\n  if (costPenalty <= 22) return 'Near-Budget';\n  if (costPenalty <= 35) return 'Mid-Range';\n  if (costPenalty <= 55) return 'Premium';\n  return 'Expensive';\n}",
    ),
]
for old, new in final_cost_surface_replacements:
    if old in html:
        html = html.replace(old, new, 1)
html = re.sub(
    r'(<h3 style="font-size:14px;font-weight:700;margin-bottom:16px;">)Dimension Weights \([^<]*</h3>',
    rf'\1Dimension Weights ({d} Total)</h3>',
    html,
    count=1,
)
html = html.replace("The <strong>overall Score</strong> includes all <strong>12 dimensions</strong>", f"The <strong>overall Score</strong> includes all <strong>{d} retained dimensions</strong>")
html = html.replace("the <strong>11 non-cost dimensions</strong>", f"the <strong>{d - 1} non-cost dimensions</strong>")
html = html.replace("speed among the platform dims", f"Speed is {'included' if speed_in_primary else 'excluded'} as a platform dimension; numeric for {speed_selected_available_n}/{n} selected pages")
html = html.replace("Speed is shown separately when an AA page publishes a numeric value", f"Speed is {'included' if speed_in_primary else 'excluded'} as a platform dimension; numeric for {speed_selected_available_n}/{n} selected pages")
html = html.replace("the highest-quality model", "the current quality leader")
html = html.replace("Gemini 3.1 Pro</strong> stays overall <strong>#1</strong> in v1.2", f"{models[0]['name']}</strong> is overall <strong>#1</strong> in {VERSION}")
quality_leader = min(models, key=lambda item: item["qualityRank"])
html = re.sub(
    r"The composite cost term uses [\s\S]*?because its composite cost is the highest in the cohort\.",
    f'The composite cost term uses {cost_mode_label}. That is why <strong>{models[0]["name"]}</strong> is overall <strong>#{models[0]["rank"]}</strong> in {VERSION}, while <strong>{quality_leader["name"]}</strong> is the current quality leader in the cohort (Quality <strong>#{quality_leader["qualityRank"]}</strong>) and ranks overall <strong>#{quality_leader["rank"]}</strong> after cost.',
    html,
    count=1,
)
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
    lambda match: match.group(1) + "['v0.7','v0.8','v0.9','v1.0','v1.1','v1.2','v1.3','v1.3.1','v1.4.0','v1.5.0','v1.6.0','v1.7.0','v1.9.0','v1.9.1','v1.9.2','v1.9.3'];",
    html,
    count=1,
)
html = re.sub(
    r"(function renderVersionTable\(\) \{[\s\S]*?const vKeys = )\[[^;]*\];",
    lambda match: match.group(1) + "['v70','v80','v90','v100','v110','v120','v130','v131','v140','v150','v160','v170','v190','v191','v192','v193'];",
    html,
    count=1,
)

if 'data-chart="livebenchPareto"' not in html:
    html = html.replace(
        '      <button class="chart-tab" data-chart="frontier2">Cost Impact</button>',
        '      <button class="chart-tab" data-chart="livebenchPareto">LiveBench Pareto</button>\n      <button class="chart-tab" data-chart="frontier2">Cost Impact</button>',
        1,
    )
chart_tab_pattern = r'<div class="chart-tabs">[\s\S]*?</div>'


def arrange_chart_tabs(match):
    buttons = re.findall(r'(?m)^[ \t]*<button class="chart-tab[^"]*" data-chart="[^"]+">[^<]*</button>', match.group(0))
    button_by_chart = {
        re.search(r'data-chart="([^"]+)"', button).group(1): button.strip()
        for button in buttons
    }
    if "pareto" not in button_by_chart or "livebenchPareto" not in button_by_chart:
        return match.group(0)
    button_by_chart["pareto"] = re.sub(r">Pareto Frontier<", ">ValueRank Pareto Frontier<", button_by_chart["pareto"])
    ordered = [button_by_chart["pareto"], button_by_chart["livebenchPareto"]]
    ordered.extend(button for chart, button in button_by_chart.items() if chart not in {"pareto", "livebenchPareto"})
    return '    <div class="chart-tabs">\n' + "\n".join(f"      {button}" for button in ordered) + '\n    </div>'


html, chart_tab_count = re.subn(chart_tab_pattern, arrange_chart_tabs, html, count=1)
if chart_tab_count != 1:
    raise SystemExit(f"chart tab order replacement failed: {chart_tab_count}")
if 'id="panel-livebenchPareto"' not in html:
    livebench_panel = f'''       <!-- LiveBench Pareto -->
       <div class="chart-panel" id="panel-livebenchPareto">
         <div class="chart-desc"><strong>{html_external_link('LiveBench', LIVEBENCH_URL)} Pareto:</strong> Official LiveBench Overall Score versus Cost Per Successful Task for {livebench_document['matchedN']}/{livebench_document['cohortN']} matched cohort rows plus {livebench_supplemental_label}: {html_escape(livebench_supplemental_text)}. Higher Overall and lower cost are better; GPT-6 Astra is omitted because this pinned release has no row for it.</div>
         <div id="chart-livebench-pareto" class="plotly-chart" style="height:520px;"></div>
       </div>
'''
    html = html.replace('      <!-- Two-frontier / Cost Impact -->', livebench_panel + '      <!-- Two-frontier / Cost Impact -->', 1)
if 'livebenchPareto: renderLiveBenchPareto' not in html:
    html = html.replace('  frontier2: renderFrontier2,', '  livebenchPareto: renderLiveBenchPareto,\n  frontier2: renderFrontier2,', 1)
if "'chart-heatmap-data','chart-livebench-pareto'" not in html:
    html = html.replace("    'chart-heatmap-data'", "    'chart-heatmap-data','chart-livebench-pareto'", 1)

livebench_card = f'''    <div class="card mb-6" id="livebench-data">
       <h3 style="font-size:14px;font-weight:700;margin-bottom:8px;">{html_external_link('LiveBench External Coverage', LIVEBENCH_URL)}</h3>
        <p class="method-text" style="margin-bottom:16px;">Release <strong>{livebench_document['release']}</strong> matches <strong>{livebench_document['matchedN']}/{livebench_document['cohortN']}</strong> AA comparison candidates and includes <strong>{livebench_supplemental_label}</strong> outside the source roster: <strong>{html_escape(livebench_supplemental_text)}</strong>. Instruction Following is the four-task LiveBench mean, but it remains supplemental because the pinned release lacks complete coverage for the current cohort; it does not contribute to the zero-gap primary score. Overall and cost are also shown as supplemental metrics.</p>
      <div style="overflow-x:auto;">
        <table class="dim-table">
          <thead><tr><th>Model</th><th>LiveBench variant</th><th>Instruction Following</th><th>Overall</th><th>Cost / successful task</th><th>Frontier</th></tr></thead>
          <tbody>{livebench_site_table_rows}</tbody>
        </table>
      </div>
      <p class="method-text" style="margin-top:12px;">Source: <a href="{livebench_document['source']['homepage']}" target="_blank" rel="noopener">LiveBench</a>; pinned data release 2026-06-25 at <a href="https://github.com/livebench/new-livebench/commit/{livebench_document['source'].get('releaseDataCommit', '')}" target="_blank" rel="noopener">{html_escape(livebench_document['source'].get('releaseDataCommit', 'unrecorded'))}</a>. Pareto frontier: <strong>{html_escape(livebench_pareto_text)}</strong>.</p>
    </div>
'''
livebench_start = html.find('    <div class="card mb-6" id="livebench-data">')
if livebench_start >= 0:
    next_card = html.find('    <div class="card mb-6">', livebench_start + 1)
    if next_card < 0:
        raise SystemExit("next data card not found after existing LiveBench card")
    html = html[:livebench_start] + livebench_card + html[next_card:]
else:
    data_start = html.find('<!-- DATA -->')
    data_card = html.find('    <div class="card mb-6">', data_start)
    if data_start < 0 or data_card < 0:
        raise SystemExit("data section insertion point not found")
    html = html[:data_card] + livebench_card + html[data_card:]

bug_hunt_card = f'''    <!-- BUG HUNT DATA CARD START -->
    <div class="card mb-6" id="bughunt-data">
      <h3 style="font-size:14px;font-weight:700;margin-bottom:8px;">{html_external_link('Bug Hunt Results', BUG_HUNT_URL)}</h3>
      <p class="method-text" style="margin-bottom:16px;">Bug Hunt has <strong>{bug_hunt_source_matches_n}/{source_n}</strong> exact owner results; <strong>{bug_hunt_ranking['matchedN']}</strong> overlap with an exact AA DeepSWE model variant and contribute to the primary score at <strong>{bug_hunt_weight['weightPct']:.2f}%</strong>. The companion emphasis view raises Bug Hunt to <strong>{bug_hunt_ranking['benchmarkWeightPct']:.2f}%</strong> (priority {bug_hunt_ranking['benchmarkPriority']} of {bug_hunt_ranking['totalPriority']}). {len(unranked_models)} candidates without the full overlap remain unranked. The table preserves effort, harness, route, and repeat count because results measure each tested agent stack.</p>
      <div style="overflow-x:auto;">
        <table class="dim-table">
          <thead><tr><th>Bug Hunt rank</th><th>Model</th><th>Fixed / 105</th><th>Emphasis score</th><th>Runs</th><th>Effort</th><th>Harness / route</th><th>Primary rank</th></tr></thead>
          <tbody>{bug_hunt_site_table_rows}</tbody>
        </table>
      </div>
      <p class="method-text" style="margin-top:12px;">Source: <a href="{BUG_HUNT_URL}" target="_blank" rel="noopener">Bug Hunt Bench</a>. Base snapshot: <a href="{bug_hunt_document['sources']['scoreboard']}" target="_blank" rel="noopener">owner scoreboard</a> at <code>{html_escape(bug_hunt_ranking['sourceCommit'])}</code>; selective MiMo additions: <a href="https://github.com/phuryn/bug-hunt-bench/blob/7dd3c23a4c86a3fac586707d01129bf549bae325/results/run-notes.md" target="_blank" rel="noopener">owner run notes at 7dd3c23</a>, observed October 7. Rows link to their individual source evidence. Rows with no eligible selected-variant result remain excluded from this matched cohort. MiMo Flash's owner default-route result is 23.3/105 (mean of three); reasoning state was unasserted and untested, so selected-reasoning equivalence remains unresolved. The separate result is preserved in raw data.</p>
    </div>
    <!-- BUG HUNT DATA CARD END -->
'''
if '<!-- BUG HUNT DATA CARD START -->' in html:
    html, replacement_count = re.subn(
        r'<!-- BUG HUNT DATA CARD START -->[\s\S]*?<!-- BUG HUNT DATA CARD END -->',
        lambda _match: bug_hunt_card.strip(),
        html,
        count=1,
    )
    if replacement_count != 1:
        raise SystemExit(f"Bug Hunt card replacement failed: {replacement_count}")
else:
    livebench_start = html.find('    <div class="card mb-6" id="livebench-data">')
    next_card = html.find('    <div class="card mb-6"', livebench_start + 1) if livebench_start >= 0 else -1
    if livebench_start < 0 or next_card < 0:
        raise SystemExit("Bug Hunt card insertion point after LiveBench not found")
    html = html[:next_card] + bug_hunt_card + html[next_card:]

# Refresh current-release copy retained in the prior generated template.
html = html.replace("ValueRank v1.5.0", f"ValueRank {VERSION}")
html = html.replace("Production AI Ranking Framework · v1.5.0", f"Production AI Ranking Framework · {VERSION}")
html = html.replace("v1.5.0 uses zero missing benchmark cells and no neutral-fill placeholders", f"{VERSION} uses zero-gap dimensions and no neutral-fill placeholders")
html = html.replace("v1.5.0 Release", f"{VERSION} Release")
html = html.replace("For each of 12 dimensions", f"For each of {d} retained dimensions")
html = html.replace("all 12 dimensions", f"all {d} retained dimensions")
html = html.replace("12 normalized dimension scores", f"{d} normalized dimension scores")
html = html.replace("for every retained v1.5.0 dimension", f"for every retained {VERSION} dimension")
html = html.replace("v1.5.0 has <strong>no missing-data cells</strong> and therefore uses <strong>no neutral-fill values</strong>", f"{VERSION} excludes incomplete candidate dimensions and uses no neutral-fill values")
html = html.replace("There are <strong>no neutral missing-data cells</strong> in v1.5.0.", f"In {VERSION}, incomplete candidate dimensions are excluded rather than imputed.")
html = html.replace("All scored cells are confirmed primary-source data in v1.5.0", f"All retained score inputs are source-backed in {VERSION}")
html = html.replace("cost uses deepswe-only (AA v4.2 total cost incomplete)", f"cost uses {cost_mode_label}")
html = html.replace("captured AA total evaluation costs remain source-only because v4.2 coverage is incomplete.", f"captured AA total evaluation costs remain source-only because coverage is {cost_coverage.get('availableN', 0)}/{n}.")
html = html.replace("The 25% cost weight therefore uses the cohort-wide DeepSWE average cost per task because the v4.2 AA total-cost field is incomplete.", f"The {weight_by_key['costComposite']['weightPct']:.2f}% cost weight uses {cost_mode_label}; AA total evaluation cost is missing for {cost_missing_text}, so no selective substitution is used.")
html = html.replace("Speed is retained as a platform dimension because v4.2 publishes numeric values for every selected page", f"Speed is {'included' if speed_in_primary else 'excluded'} because coverage is {speed_selected_available_n}/{n}; missing for {speed_missing_text}.")
html = html.replace("Hallucination rate remains a primary reliability factor", "Non-Hallucination Rate remains a primary reliability factor")
html = html.replace("That is why <strong>Gemini 3.8 Flash</strong> is overall <strong>#1</strong> in v1.5.0, while <strong>GPT-6 Astra</strong> is the current quality leader in the cohort (Quality <strong>#1</strong>) and ranks overall <strong>#4</strong> after cost.", f"That is why <strong>{models[0]['name']}</strong> is overall <strong>#{models[0]['rank']}</strong> in {VERSION}, while <strong>{quality_leader['name']}</strong> is the current quality leader in the cohort (Quality <strong>#{quality_leader['qualityRank']}</strong>) and ranks overall <strong>#{quality_leader['rank']}</strong> after cost.")
html = html.replace("Ranking History — v0.7 to v1.5.0", f"Ranking History — v0.7 to {VERSION}")
html = html.replace("x:'v1.5.0', y:1", f"x:'{VERSION}', y:1")
html = html.replace("text:'v1.5.0: 21 models · 12 dims'", f"text:'{VERSION}: {n} models · {d} dims'")
html = html.replace("September 6, 2026", DATE)
html = html.replace("ValueRank v1.5.0 · September 6, 2026 · 21 models × 12 dimensions", f"ValueRank {VERSION} · {DATE} · {n} models × {d} dimensions")
html = re.sub("const SPEED_DIM_IDX = [-0-9]+;.*", f"const SPEED_DIM_IDX = {speed_dim_idx};", html, count=1)
html = html.replace(
    "For each of 12 retained dimensions, all 21 models are ranked 1–21 (best to worst). The formula maps rank 1 → 100 pts and rank 21 → 0 pts, with tied ranks receiving the average of their tied positions. v1.6.0 excludes incomplete candidate dimensions and uses no neutral-fill values.",
    f"For each of {d} retained dimensions, the {n} exact-overlap models are ranked from 1–{n}. Rank 1 maps to 100 points and rank {n} to 0; ties receive the average tied rank. {VERSION} excludes incomplete dimensions and does not fill missing values.",
)
html = html.replace(
    "The final ValueRank score is a weighted sum across all 12 retained dimensions. <strong>Cost weight: 25%</strong> (slider-adjustable). Non-Hallucination Rate remains a primary reliability factor, and cost uses DeepSWE-only and is rank-normalized with lower cost better.",
    f"The final ValueRank score is a weighted sum across {d} retained dimensions. <strong>Cost weight: {weight_by_key['costComposite']['weightPct']:.2f}%</strong> (slider-adjustable). Bug Hunt Bench contributes <strong>{weight_by_key['bugHuntFixedOf105']['weightPct']:.2f}%</strong> and DeepSWE v1.1 contributes <strong>{weight_by_key['deepswePassAt1']['weightPct']:.2f}%</strong>. API Costs uses AA total evaluation cost; Plan Costs divides the same value by the highest eligible subscription Value Multiple.",
)
html = html.replace(
    "If even one of the 21-model cohort is genuinely missing from a benchmark, that benchmark is excluded from the current primary score. The official-source owner is checked first, then current secondary implementations are checked before a benchmark is ruled out.",
    f"If any of the {n} primary-cohort models is missing from a benchmark, that dimension is excluded from the composite. Exact benchmark-version and evaluated-model matches are required; the full source roster contains {source_n} candidates.",
)
html = html.replace(
    "The 68% non-cost portion, computed as the weighted sum of all 13 non-cost dimensions. Represents pure capability ranking without cost penalty.",
    f"The weighted sum of the {d - 1} non-cost dimensions, renormalized to 100%. It represents benchmark capability without the cost penalty.",
)
html = html.replace(
    "Each model's score is a weighted average of 14 normalized dimension scores. Each dimension score is calculated as <code>((n − rank) / (n − 1)) × 100</code>, where <strong>n = 21</strong> for every retained v1.6.0 dimension. A score of <strong>100</strong> = top of pool and <strong>0</strong> = bottom of pool. In v1.6.0, incomplete candidate dimensions are excluded rather than imputed. For AA-Omniscience Hallucination Rate, lower raw hallucination rate is ranked better. For Cost, the raw input is normalized DeepSWE average cost per task; captured AA total evaluation costs remain source-only because coverage is 20/21.",
    f"Each model's score is a weighted average of {d} normalized dimension scores across the {n}-model exact-overlap cohort. Each dimension score uses <code>((n − rank) / (n − 1)) × 100</code>, with n = {n}; ties receive average rank. Incomplete dimensions are excluded rather than imputed. AA-Omniscience is represented as Non-Hallucination Rate, where higher is better. API Costs uses AA total evaluation cost; Plan Costs divides that amount by the highest eligible subscription Value Multiple, with lower cost better in both views.",
)
html = html.replace(
    "The 32.05% cost weight uses DeepSWE-only; AA total evaluation cost is missing for Gemini 3.7 Flash, so no selective substitution is used.",
    f"The {weight_by_key['costComposite']['weightPct']:.2f}% cost weight uses AA total evaluation cost, complete for all {n} primary models; no selective substitution is used.",
)
html = html.replace(
    "In <strong>v1.5.0</strong>, there are <strong>no ⊘ cells</strong> because any benchmark without full cohort coverage is excluded entirely.",
    f"In <strong>{VERSION}</strong>, there are <strong>no ⊘ cells</strong> because any dimension without full coverage in the {n}-model cohort is excluded.",
)
html = html.replace(
    "The <strong>overall Score</strong> includes all <strong>12 retained dimensions</strong> with cost at 25% (slider default) and Speed is excluded because coverage is 20/21; missing for Kimi K3.. The <strong>Quality Score</strong> is recalculated using only the <strong>13 non-cost dimensions</strong> (renormalized to 100%). It answers: <em>\"which model is best at actual tasks?\"</em> independent of composite cost. The Rankings table shows both, and the Quality Rank column lets you sort by quality alone.",
    f"The <strong>overall Score</strong> includes all <strong>{d} retained dimensions</strong>, including Bug Hunt and DeepSWE v1.1, with cost at {weight_by_key['costComposite']['weightPct']:.2f}% by default. The <strong>Quality Score</strong> renormalizes the <strong>{d - 1} non-cost dimensions</strong> to 100%. It answers: <em>\"which model ranks highest on the selected benchmarks?\"</em> independent of composite cost. The Rankings table shows both, and the Quality Rank column lets you sort by quality alone.",
)
html = html.replace(
    "The composite cost term uses the selected cost basis; Plan Costs divide API task cost by the highest eligible Value Multiple. That is why <strong>Gemini 3.8 Flash</strong> is overall <strong>#1</strong> in v1.6.0, while <strong>GPT-6 Astra</strong> is the current quality leader in the cohort (Quality <strong>#1</strong>) and ranks overall <strong>#2</strong> after cost.",
    f"ValueRank reflects the selected benchmarks and their weights, including DeepSWE v1.1 and Bug Hunt in the main rank; it is not a general model-capability verdict. The current overall leader is <strong>{models[0]['name']}</strong> (#{models[0]['rank']}); the quality leader is <strong>{quality_leader['name']}</strong> (#{quality_leader['qualityRank']}). API Costs and Plan Costs are presented as separate cost views.",
)

html = html.replace(
    '<span class="hero-statbar-num">25%</span>',
    f'<span class="hero-statbar-num">{cost_weight["weightPct"]:.2f}%</span>',
    1,
)
html = html.replace(
    'Drag the cost weight slider to see how rankings shift. Cost is rank-normalized from the selected API-price or subscription-plan task-cost basis; captured AA total evaluation costs remain source-only because coverage is 20/21. Click any column header to sort.',
    f'Drag the cost weight slider to see how rankings shift. API Costs uses AA total evaluation cost; Plan Costs divides the same cost by the highest eligible subscription Value Multiple. The default Cost weight is {cost_weight["weightPct"]:.2f}%. Click any column header to sort.',
)
html = html.replace(
    '<input type="range" id="cost-slider" min="0" max="50" value="25" step="1">',
    f'<input type="range" id="cost-slider" min="0" max="50" value="{cost_weight["weightPct"]:.4f}" step="0.01">',
)
html = html.replace(
    '<span class="slider-val" id="slider-val">25%</span>',
    f'<span class="slider-val" id="slider-val">{cost_weight["weightPct"]:.2f}%</span>',
)
html = html.replace(
    'Official LiveBench Overall Score versus Cost Per Successful Task for 20/21 matched cohort rows.',
    f'Official LiveBench Overall Score versus Cost Per Successful Task for {livebench_document["matchedN"]}/{livebench_document["cohortN"]} AA source candidates.',
)
html = html.replace(
    'diamond = overall score (with 25% cost weight).',
    'diamond = overall score (with the currently selected cost weight).',
)
html = html.replace(
    'API list-price task cost; cost-weighted scores use the API-cost rank.',
    'AA total evaluation cost at API rates; the default cost-weighted score uses the API-cost rank.',
)
html = html.replace(
    'How many places does a 25% cost weight move each model from its quality-only rank?',
    'How many places does the selected cost weight move each model from its quality-only rank?',
)
html = html.replace(
    'Frontier models ranked on real-world value. ValueRank v1.7.0 · 21 models from Artificial Analysis & DeepSWE Best, with a separate Bug Hunt emphasis ranking.',
    f'Frontier models ranked on real-world value. ValueRank {VERSION} · {n} models; DeepSWE v1.1 and Bug Hunt shape the primary score.',
)
html = html.replace(
    '// Dims: Cost Halluc DeepSWE GDP LCR OmniAcc HLE GPQA Sci CritPt AAI Spd',
    '// Dims: Cost NonHalluc LiveBenchIF DeepSWE GDP AutomationBench LCR OmniAcc HLE GPQA SciCode CritPt AAI BugHunt',
)
html = html.replace(
    'Independent rankings from Artificial Analysis & DeepSWE. ValueRank v1.7.0 · 21 models, plus a matched-cohort Bug Hunt emphasis ranking.',
    f'Evidence-backed rankings from benchmark owners. ValueRank {VERSION} · {n} models; DeepSWE v1.1 and Bug Hunt are in the primary rank.',
)
html = html.replace('Production AI Ranking Framework · v1.7.0', f'Production AI Ranking Framework · {VERSION}')
html = html.replace('Current Top 3 · DeepSWE Cohort', 'Current Top 3 · Shared DeepSWE + Bug Hunt Cohort')
html = html.replace(
    'v1.7.0 primary score uses zero-gap dimensions and no neutral-fill placeholders',
    f'{VERSION} primary score uses zero-gap dimensions and no neutral-fill placeholders',
)
html = html.replace('<div class="insight-title">v1.7.0 Release</div>', f'<div class="insight-title">{VERSION} Release</div>')
html = html.replace(
    '<h3 style="font-size:14px;font-weight:700;margin-bottom:12px;">Normalized Score Matrix (21 × 12)</h3>',
    f'<h3 style="font-size:14px;font-weight:700;margin-bottom:12px;">Normalized Score Matrix ({n} × {d})</h3>',
)
html = html.replace(
    'All retained score inputs are source-backed in v1.7.0',
    f'All retained score inputs are source-backed in {VERSION}',
)
html = html.replace(
    'ValueRank v1.7.0 · September 29, 2026 · 21 models × 12 primary dimensions',
    f'ValueRank {VERSION} · {DATE} · {n} models × {d} primary dimensions',
)
html = html.replace('Cost weight: 25% (default)', f'Cost weight: {cost_weight["weightPct"]:.2f}% (default)')
html = html.replace('Why does cost get 25% of the weight?', f'Why is cost weighted at {cost_weight["weightPct"]:.2f}% by default?')
html = html.replace('Ranking History — v0.7 to v1.7.0', f'Ranking History — v0.7 to {VERSION}')
html = html.replace(
    "name:'Overall Score (with 25% cost)',",
    "name:'Overall Score (with ' + costWeightPct + '% ' + costBasisLabel() + ')',",
)
html = html.replace(
    'What happened to the models that were ranked in v1.1 but not in v1.2?',
    "Why isn't Claude Opus 5.5 in the primary ranking?",
)

def replace_faq_answer(source, question, answer):
    pattern = (
        r'(<div class="faq-item">\s*<button class="faq-q"[^>]*>\s*'
        + re.escape(question)
        + r'\s*<i data-lucide="chevron-down" class="faq-chevron"></i>\s*</button>\s*'
        r'<div class="faq-a">)[\s\S]*?(</div>\s*</div>)'
    )
    updated, count = re.subn(
        pattern,
        lambda match: match.group(1) + answer + match.group(2),
        source,
        count=1,
    )
    if count != 1:
        raise SystemExit(f"FAQ answer replacement failed: {question}")
    return updated

html = re.sub(
    r"Why is cost weighted at [0-9.]+% by default\?",
    f"Why is cost weighted at {cost_weight['weightPct']:.2f}% by default?",
    html,
    count=1,
)
html = html.replace(
    "Why isn't Claude Opus 5.5 in the primary ranking?",
    "Is Claude Opus 5.5 included in the primary ranking?",
    1,
)

faq_updates = [
    (
        'What does the overall score actually represent?',
        f'Each model’s score is a weighted average of {d} normalized dimension scores across the {n}-model exact-overlap cohort. Each dimension score uses <code>((n − rank) / (n − 1)) × 100</code>, with n = {n}; ties receive average rank. Incomplete dimensions are excluded rather than imputed. AA-Omniscience is represented as Non-Hallucination Rate, where higher is better. API Costs uses AA total evaluation cost; Plan Costs divides the same value by the highest eligible subscription Value Multiple.',
    ),
    (
        f'Why is cost weighted at {cost_weight["weightPct"]:.2f}% by default?',
        f'Cost has a {cost_weight["weightPct"]:.2f}% weight in the primary score. The API Costs basis uses AA total evaluation cost; Plan Costs divides that same cost by the highest eligible subscription Value Multiple. Both views use the same benchmark suite and lower cost ranks better.',
    ),
    (
        'What does ⊘ mean in ValueRank?',
        f'In historical ValueRank versions, ⊘ marked a genuine benchmark data gap. In {VERSION}, incomplete dimensions are excluded from the composite, so every ranked model has full coverage across the retained dimensions.',
    ),
    (
        "What's the difference between Score and Quality Score?",
        f'The overall Score includes all {d} retained dimensions, including Bug Hunt and DeepSWE v1.1, with cost at {cost_weight["weightPct"]:.2f}% by default. Quality Score renormalizes the {d - 1} non-cost dimensions to 100%, showing benchmark performance without the cost weight.',
    ),
    (
        'What is the Pareto frontier?',
        'The Pareto frontier contains models that are not dominated on both quality and cost under the selected cost basis. The Pareto chart updates when you switch between API Costs and Plan Costs.',
    ),
    (
        'Are scores comparable across ValueRank versions?',
        'Prior-version scores are not directly comparable. The eligible models, benchmark versions, dimensions, and weights can change, shifting rank-normalized scores. Use the version history table for rank movement and each release record for its own score values.',
    ),
    (
        'How often is ValueRank updated?',
        f'ValueRank is refreshed when primary benchmark results or cost inputs materially change. {VERSION} uses AA Coding Agent Index v1.5 DeepSWE v1.1 results, includes Bug Hunt in the primary score, and ranks {n} exact-overlap models across {d} zero-gap dimensions.',
    ),
    (
        "Is Claude Opus 5.5 included in the primary ranking?",
        f'Claude Opus 5.5 is included in {VERSION}. The {html_external_link("AA Coding Agent Index v1.5 DeepSWE v1.1 chart", AA_DEEPSWE_URL)} reports 68.0% for Claude Code / Opus 5.5 / max; the {html_external_link("Bug Hunt owner scoreboard", BUG_HUNT_URL)} reports 41.7/105 (mean of three runs) for Opus 5.5 max. The {html_external_link("AA model profile", "https://artificialanalysis.ai/models/claude-opus-5-5")} labels its corresponding profile max with fallback. The composite ranks {n} exact-overlap models across {d} zero-gap dimensions; the pinned LiveBench release predates Opus 5.5, so Instruction Following remains supplemental.',
    ),
]
for question, answer in faq_updates:
    html = replace_faq_answer(html, question, answer)

site_path.write_text(html)
inject_header(site_path, "llm", f"{DATE} · {n} models · {d} scored dimensions", VERSION)

# Normalize current-release copy after applying the shared header. The site is
# an inherited publication shell, so exact legacy-string replacements above
# can miss text left by earlier refreshes.
html = site_path.read_text()


def replace_current_copy(source, pattern, replacement, label):
    updated, count = re.subn(pattern, replacement, source, count=1)
    if count != 1:
        raise SystemExit(f"current-release copy replacement failed: {label}")
    return updated


current_description = (
    f"ValueRank {VERSION}: {n} models ranked across {d} zero-gap dimensions; "
    "DeepSWE v1.1 and Bug Hunt are included in the primary score."
)
for attribute in (
    'name="description"',
    'property="og:description"',
    'name="twitter:description"',
):
    html = replace_current_copy(
        html,
        rf'(<meta {attribute} content=")[^"]*(">)',
        lambda match: match.group(1) + html_escape(current_description, quote=True) + match.group(2),
        f"meta {attribute}",
    )

html = replace_current_copy(
    html,
    r'(<div class="hero-eyebrow">[\s\S]*?Production AI Ranking Framework · )v[0-9.]+',
    lambda match: match.group(1) + VERSION,
    "hero release",
)
html = replace_current_copy(
    html,
    r'(<span class="hero-statbar-num">)[^<]*(</span>\s*<span class="hero-statbar-label">Cost Weight</span>)',
    lambda match: match.group(1) + f'{cost_weight["weightPct"]:.2f}%' + match.group(2),
    "hero cost weight",
)
html = replace_current_copy(
    html,
    r'(<div class="section-sub">)Drag the cost weight slider[\s\S]*?(</div>)',
    lambda match: match.group(1)
    + f'Drag the cost weight slider to see how rankings shift. API Costs uses AA total evaluation cost; Plan Costs divides the same cost by the highest eligible subscription Value Multiple. The default Cost weight is {cost_weight["weightPct"]:.2f}%. Click any column header to sort.'
    + match.group(2),
    "ranking cost explanation",
)
html = replace_current_copy(
    html,
    r'(<input type="range" id="cost-slider"[^>]*value=")[^"]+(" step=")[^"]+(">)',
    lambda match: match.group(1) + f'{cost_weight["weightPct"]:.4f}' + match.group(2) + "0.01" + match.group(3),
    "cost slider default",
)
html = replace_current_copy(
    html,
    r'(<span class="slider-val" id="slider-val">)[^<]*(</span>)',
    lambda match: match.group(1) + f'{cost_weight["weightPct"]:.2f}%' + match.group(2),
    "cost slider label",
)
html = replace_current_copy(
    html,
    r'(<span class="seal-note">)v[0-9.]+ primary score uses [^<]*(</span>)',
    lambda match: match.group(1) + f'{VERSION} primary score uses {d} zero-gap dimensions and no neutral-fill placeholders' + match.group(2),
    "ranking release note",
)
html = replace_current_copy(
    html,
    r'(<span class="seal-note" id="cost-note">)Cost weight: [^<]*(</span>)',
    lambda match: match.group(1) + f'Cost weight: {cost_weight["weightPct"]:.2f}% (default)' + match.group(2),
    "cost weight note",
)
html = replace_current_copy(
    html,
    r'(<div class="insight-title">)v[0-9.]+ Release(</div>)',
    lambda match: match.group(1) + f'{VERSION} Release' + match.group(2),
    "release insight title",
)
html = replace_current_copy(
    html,
    r'(<h3[^>]*>Normalized Score Matrix \()[0-9]+\s*[×x]\s*[0-9]+(\)</h3>)',
    lambda match: match.group(1) + f'{n} × {d}' + match.group(2),
    "score matrix heading",
)
html = replace_current_copy(
    html,
    r'(<span style="margin-left:12px;">)All retained score inputs are source-backed in v[0-9.]+(</span>)',
    lambda match: match.group(1) + f'All retained score inputs are source-backed in {VERSION}' + match.group(2),
    "score matrix source note",
)

formula_copy = (
    f"For each of {d} retained dimensions, the {n} exact-overlap models are ranked from 1–{n}. "
    f"Rank 1 maps to 100 points and rank {n} to 0; ties receive the average tied rank. "
    f"{VERSION} excludes incomplete dimensions and does not fill missing values."
)
html = replace_current_copy(
    html,
    r'(<h3[^>]*>Scoring Formula</h3>\s*<div class="method-formula">[\s\S]*?</div>\s*<p class="method-text">)[\s\S]*?(</p>)',
    lambda match: match.group(1) + formula_copy + match.group(2),
    "scoring formula cohort",
)
weights_copy = (
    f"The final ValueRank score is a weighted sum across {d} retained dimensions. "
    f"<strong>Cost weight: {cost_weight['weightPct']:.2f}%</strong> (slider-adjustable). "
    f"Bug Hunt Bench contributes <strong>{bug_hunt_weight['weightPct']:.2f}%</strong> and "
    f"DeepSWE v1.1 contributes <strong>{deepswe_weight['weightPct']:.2f}%</strong>. "
    "API Costs uses AA total evaluation cost; Plan Costs divides the same value by the highest eligible subscription Value Multiple."
)
html = replace_current_copy(
    html,
    r'(<h3[^>]*>Scoring Formula</h3>[\s\S]*?<hr class="divider"[^>]*>\s*<p class="method-text">)[\s\S]*?(</p>)',
    lambda match: match.group(1) + weights_copy + match.group(2),
    "scoring formula weights",
)
html = replace_current_copy(
    html,
    r'(<strong>Zero-gap benchmark rule:</strong>)[\s\S]*?(</div>)',
    lambda match: match.group(1)
    + f' If any of the {n} primary-cohort models is missing from a benchmark, that dimension is excluded from the composite. Exact benchmark-version and evaluated-model matches are required; the full source roster contains {source_n} candidates.'
    + match.group(2),
    "zero-gap rule",
)
html = replace_current_copy(
    html,
    r'(<strong>Quality sub-score:</strong>)[\s\S]*?(</div>)',
    lambda match: match.group(1)
    + f'The weighted sum of the {d - 1} non-cost dimensions, renormalized to 100%. It represents benchmark capability without the cost penalty.'
    + match.group(2),
    "quality sub-score",
)
html = replace_current_copy(
    html,
    r'(<div class="card mb-6" id="livebench-data">[\s\S]*?<p class="method-text" style="margin-bottom:16px;">)[\s\S]*?(</p>)',
    lambda match: match.group(1)
    + f'Release <strong>{livebench_document["release"]}</strong> matches <strong>{livebench_document["matchedN"]}/{livebench_document["cohortN"]}</strong> AA comparison candidates and includes <strong>{livebench_supplemental_label}</strong> outside the source roster: <strong>{html_escape(livebench_supplemental_text)}</strong>. Instruction Following is the four-task LiveBench mean, but it remains supplemental because the pinned release has incomplete coverage for the current cohort; it does not contribute to the zero-gap primary score. Overall and cost are also shown as supplemental metrics.'
    + match.group(2),
    "LiveBench primary coverage note",
)
html = replace_current_copy(
    html,
    r"(<div>ValueRank )v[0-9.]+ · [^<]+ · [0-9]+ models × [0-9]+ primary dimensions",
    lambda match: match.group(1) + f'{VERSION} · {DATE} · {n} models × {d} primary dimensions',
    "footer release",
)
html = replace_current_copy(
    html,
    r"(title:\{text:'Ranking History — v0\.7 to )v[0-9.]+",
    lambda match: match.group(1) + VERSION,
    "ranking history chart title",
)
html = re.sub(r"<!-- aa-reconciliation:start -->[\s\S]*?<!-- aa-reconciliation:end -->", "", html)
if "</main>" not in html:
    raise ValueError("Cannot insert AA comparison: publication shell lacks </main>")
source_date_note = ('<p class="method-text">Publication updated October 8, 2026 with selective additions. Earlier AA and DeepSWE snapshots remain dated September 29–30; MiMo AA and frontier observations were captured October 8, and selective MiMo Bug Hunt owner notes were observed October 7. Rounded public AA metrics preserve captured display precision; source dates and precision are listed in raw data.</p>')
aa_reconciliation_html = aa_reconciliation_html.replace('</p>', '</p>' + source_date_note, 1)
html = html.replace("</main>", aa_reconciliation_html + "\n</main>", 1)
site_path.write_text(html)

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
