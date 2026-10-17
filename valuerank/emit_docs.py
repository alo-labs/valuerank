#!/usr/bin/env python3
"""Emit the Markdown publication: README, methodology, score tables and raw data.

The website under site/ is owned by ``python -m valuerank.site.build``.
"""

from __future__ import annotations

import json
from html import escape as html_escape


from valuerank.paths import DATA, ROOT
from valuerank.plan_costs import build_cost_fields, load_plan_routes
from valuerank.aa_reconciliation import reconcile as reconcile_aa, publication as aa_reconciliation_publication

from valuerank.release import DATE, VERSION
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


def fnum(value, places=2, dash="—"):
    return f"{value:.{places}f}" if isinstance(value, (int, float)) else dash


def pct(value, places=2):
    return f"{value * 100:.{places}f}%" if isinstance(value, (int, float)) else "—"


def metric_coverage_summary(model, weights):
    coverage = model.get("metricCoverage") or {}
    model_dims = model.get("dims", {})
    if "missingKeys" in coverage:
        missing_keys = set(coverage.get("missingKeys") or [])
    else:
        missing_keys = {
            weight["key"]
            for weight in weights
            if model_dims.get(weight["key"]) is None
        }
    missing_labels = [weight["label"] for weight in weights if weight["key"] in missing_keys]
    available_keys = {
        weight["key"]
        for weight in weights
        if model_dims.get(weight["key"]) is not None
    }
    available_priority = coverage.get("availablePriority")
    if not isinstance(available_priority, (int, float)):
        available_priority = sum(weight.get("priority", 0) for weight in weights if weight["key"] in available_keys)
    total_priority = coverage.get("totalPriority")
    if not isinstance(total_priority, (int, float)):
        total_priority = sum(weight.get("priority", 0) for weight in weights)
    coverage_pct = coverage.get("coveragePct")
    if not isinstance(coverage_pct, (int, float)) and total_priority:
        coverage_pct = 100 * available_priority / total_priority
    if isinstance(coverage_pct, (int, float)):
        coverage_text = f"{coverage_pct:.2f}% ({available_priority:g}/{total_priority:g} priority)"
    else:
        coverage_text = "—"
    return coverage_text, ", ".join(missing_labels) or "none"


def names(values):
    return ", ".join(values) if values else "none"


def primary_rows(models, weights):
    rows = []
    for model in models:
        coverage_text, missing_text = metric_coverage_summary(model, weights)
        rank = model.get("rank") if model.get("rank") is not None else "—"
        rows.append(
            f"| {rank} | {model['name']} | {fnum(model.get('overallScore'), 1)} | "
            f"{fnum(model.get('qualityScore'), 1)} | {fnum(model.get('costComposite'))} | "
            f"{coverage_text} | Missing: {missing_text} |"
        )
    return "\n".join(rows)


def dimension_table(weights):
    return "\n".join(
        f"| {index} | {md_benchmark_link(weight['label'])} | {weight['weightPct']:.2f}% | {'higher' if weight['higherBetter'] else 'lower'} |"
        for index, weight in enumerate(weights, 1)
    )


def livebench_table(livebench_rows):
    return "\n".join(
        f"| {record['name']} | {record['livebenchModel']} | {record['instructionFollowingScore']:.2f} | {record['overallScore']:.2f} | ${record['costPerSuccessfulTaskUsd']:.4f} |"
        for record in livebench_rows
    )


def tb4_table(tb4_rows):
    return "\n".join(
        f"| {entry['rankLabel']} | {entry['baseModel']} | {entry['agent']} | {entry['resolutionRatePct']:.1f}% ± {entry['uncertaintyPct']:.1f}% | {entry['tokens']} | {'—' if entry['costUsd'] is None else f"${entry['costUsd']:,.0f}"} |"
        for entry in tb4_rows
    )


def bug_hunt_emphasis_table(bug_hunt_ranking, bug_hunt_records):
    return "\n".join(
        f"| {item['rank']} | {item['name']} | {record['fixedOf105']:g}/105 | "
        f"{item['emphasisScore']:.1f} | n={record['sampleN']} ({record['aggregation']}) | "
        f"{record['effort']} ({record['effortStatus']}) | "
        f"{record['harness']} / {record['route']} | {item['primaryRank']} |"
        for item in bug_hunt_ranking["ranking"]
        for record in [bug_hunt_records[item["modelId"]]]
    )


def bug_hunt_raw_table(all_models, bug_hunt_records):
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


def deepswe_chart_table(deepswe_configurations):
    return "\n".join(
        f"| {item['sourceOrder']} | {item['agent']} | {item['model']} | {item.get('effort') or 'not shown'} | "
        f"{item['scorePct']:.1f}% | "
        f"{'Exact: ' + item['valueRankModelId'] if item.get('valueRankModelId') else item['matchStatus'].replace('_', ' ')} | "
        f"{item.get('matchNote', '—')} |"
        for item in deepswe_configurations
    )


def plan_evidence_label(route):
    if route.get("evidenceClass") == "user_assumption":
        return "Provisional assumption"
    if route.get("evidenceClass") == "controlled_account_workload_projection":
        return "Controlled account measurement / workload projection"
    return str(route.get("evidenceClass", "Unclassified")).replace("_", " ")


def plan_usd(value, missing):
    return f"${value:,.2f}" if isinstance(value, (int, float)) else missing


def plan_source_html(route):
    url = route.get("sourceUrl")
    return html_external_link("Source", url) if url else "User assumption"


def plan_intelligence_label(model, aa_document):
    value = model.get("intelligenceIndex")
    record = aa_document.get("models", {}).get(model["id"], {})
    metric_precision = ((record.get("metricSources") or {}).get("intelligenceIndex") or {}).get("precision")
    precision = str(metric_precision or (record.get("extraction") or {}).get("precision") or "")
    if isinstance(value, (int, float)) and "display-rounded" in precision:
        label = str(value).removesuffix(".0") + " (rounded)"
    else:
        label = fnum(value)
    return label + (" (estimated)" if model.get("intelligenceIndexStatus") == "estimated" else "")


def plan_markdown_table(headers, rows):
    def clean(value):
        text = str(value).replace("|", "\\|").replace("\n", " ")
        return f"[Source]({text})" if text.startswith("https://") else text
    return "\n".join(["| " + " | ".join(headers) + " |", "|" + "|".join("---" for _ in headers) + "|"] + ["| " + " | ".join(clean(value) for value in row) + " |" for row in rows])


def plan_html_table(headers, rows):
    def cell(value):
        text = str(value)
        return html_external_link("Source", text) if text.startswith("https://") else html_escape(text)
    return '<div class="table-wrap"><table><thead><tr>' + ''.join(f'<th scope="col">{html_escape(header)}</th>' for header in headers) + '</tr></thead><tbody>' + ''.join('<tr>' + ''.join(f'<td>{cell(value)}</td>' for value in row) + '</tr>' for row in rows) + '</tbody></table></div>'


FRONTIER_RULE = (
    "Every model family on the Pareto frontier that Artificial Analysis (AA) renders on its Intelligence Index versus "
    "total cost to run chart is ranked, with the exact configuration AA selects on that line. Frontier membership is AA's "
    "rendered line as observed; ValueRank never recomputes it from rounded values."
)
NEAR_FRONTIER_RULE = (
    "A plotted configuration is near-frontier when its public (rounded integer) Intelligence Index is within {gap} points of the "
    "rendered frontier's Index at its cost, meaning the highest Index among rendered-frontier points that cost no more. "
    "Every near-frontier family is ranked (its selected configuration may differ from the near configuration) or is explicitly "
    "deferred by a dated, reasoned roster decision. The cost ratio to the frontier is reported for information only."
)
DEFAULT_NEAR_GAP = 3


def _count(value, noun, plural=None):
    return f"{value} {noun if value == 1 else plural or noun + 's'}"


def _clean_number(value):
    return str(int(value)) if isinstance(value, (int, float)) and float(value).is_integer() else str(value)


def model_inclusion(selection, models):
    """The model-inclusion policy and its observed facts, read from ``frontierSelection`` (optional, every field).

    Shared by the Markdown emitter and the site view model so both state the same rules and numbers.
    """

    selection = selection or {}
    policy = selection.get("nearFrontierPolicy") or {}
    universe = selection.get("sourceUniverse") or {}
    head = ["Chart observed"] if selection.get("capturedAt") or selection.get("indexVersion") or universe else []
    if head:
        if selection.get("capturedAt"):
            head.append(selection["capturedAt"])
        if selection.get("indexVersion"):
            head.append(f"(Intelligence Index v{selection['indexVersion']})")
    facts = []
    if universe.get("selectedModelN") is not None:
        facts.append(f"{universe['selectedModelN']} catalog models selected")
    if universe.get("plottedPointN") is not None:
        facts.append(_count(universe["plottedPointN"], "plotted point"))
    if universe.get("observedFrontierPointN") is not None:
        vertices = _count(universe["observedFrontierPointN"], "rendered Pareto vertex", "rendered Pareto vertices")
        facts.append(vertices + (f" across {_count(selection['familyN'], 'family', 'families')}" if selection.get("familyN") is not None else ""))
    sentences = []
    if head:
        sentences.append(" ".join(head) + (": " + (", ".join(facts[:-1]) + " and " + facts[-1] if len(facts) > 1 else facts[0]) if facts else "") + ".")
    if selection.get("nearFrontierPointN") is not None:
        near = _count(selection["nearFrontierPointN"], "plotted point")
        if selection.get("nearFrontierFamilyN") is not None:
            near += f" across {_count(selection['nearFrontierFamilyN'], 'family', 'families')}"
        sentences.append(f"{near} {'is' if selection['nearFrontierPointN'] == 1 else 'are'} near-frontier.")
    status = [
        text
        for text in (
            f"{selection['nearFrontierRequiredModelN']} required" if selection.get("nearFrontierRequiredModelN") is not None else None,
            f"{selection['nearFrontierDeferredN']} deferred by roster decision" if selection.get("nearFrontierDeferredN") is not None else None,
        )
        if text
    ]
    footnotes = {}
    for model in models:
        if model.get("aaFrontierFootnote"):
            footnotes.setdefault(model["aaFrontierFootnote"], []).append(model["name"])
    gap = _clean_number(policy.get("maxIntelligenceGap", DEFAULT_NEAR_GAP))
    return {
        "frontierRule": FRONTIER_RULE,
        "nearFrontierGap": gap,
        "nearFrontierRule": NEAR_FRONTIER_RULE.format(gap=gap),
        "policyText": policy.get("text"),
        "observation": " ".join(sentences) or None,
        "nearFrontierStatus": "Near-frontier models: " + ", ".join(status) + "." if status else None,
        "frontierFamilies": [
            {"family": item["family"], "configuration": item["configuration"]} for item in selection.get("frontierFamilies") or []
        ],
        "nearFrontierFamilies": [
            {"family": item["family"], "configuration": item["configuration"], "gap": _clean_number(item["intelligenceGap"])}
            for item in selection.get("nearFrontierFamilies") or []
        ],
        "footnotes": [{"text": text, "models": names_} for text, names_ in footnotes.items()],
    }


def model_inclusion_markdown(inclusion, level="##"):
    lines = [
        f"{level} Model inclusion",
        "",
        f"**Frontier rule.** {inclusion['frontierRule']}",
        "",
        f"**Near-frontier rule.** {inclusion['nearFrontierRule']}",
    ]
    if inclusion["policyText"]:
        lines += ["", f"Policy as recorded: {inclusion['policyText']}"]
    for text in (inclusion["observation"], inclusion["nearFrontierStatus"]):
        if text:
            lines += ["", text]
    if inclusion["frontierFamilies"]:
        lines += ["", "Frontier families and the configuration selected for each:", ""]
        lines += [f"- {item['family']}: {item['configuration']}" for item in inclusion["frontierFamilies"]]
    if inclusion["nearFrontierFamilies"]:
        lines += ["", "Near-frontier families and the configuration selected for each:", ""]
        lines += [
            f"- {item['family']}: {item['configuration']}, {item['gap']} Index points below the frontier"
            for item in inclusion["nearFrontierFamilies"]
        ]
    for note in inclusion["footnotes"]:
        lines += ["", f"AA footnote ({', '.join(note['models'])}): {note['text']}"]
    return "\n".join(lines) + "\n"


def norm_values(model, weights):
    return ", ".join(
        f"{model['dims'][weight['key']]:.1f}"
        if isinstance(model.get("dims", {}).get(weight["key"]), (int, float))
        else "⊘"
        for weight in weights
    )


def main(*, root=ROOT, data=DATA) -> int:
    """Emit every publication output beneath ``root`` from the snapshots in ``data``."""

    scores = json.loads((data / "scores.json").read_text())
    aa_document = json.loads((data / "aa_metrics.json").read_text())
    coverage_document = json.loads((data / "coverage_matrix.json").read_text())
    deepswe_chart_doc = json.loads((data / "aa_deepswe.json").read_text())
    livebench_document = json.loads((data / "livebench.json").read_text())
    tb4_document = json.loads((data / "tb4.json").read_text())
    bug_hunt_document = json.loads((data / "bug_hunt.json").read_text())
    bug_hunt_ranking = scores["bugHuntEmphasisRanking"]
    bug_hunt_records = {item["modelId"]: item for item in bug_hunt_document["models"]}
    manifest = json.loads((data / "run_manifest.json").read_text())
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
    plan_route_document = load_plan_routes(data / "plan_cost_routes.json")
    plan_cost_fields = build_cost_fields(models, plan_route_document)
    candidate_plan_cost_fields = build_cost_fields(all_models, plan_route_document)
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
    provider_claims = json.loads((data / "provider_claims.json").read_text()).get("claims", [])
    eligible_provider_claims = [item for item in provider_claims if item.get("eligibleForRanking") is True]
    deepswe_updated = scores.get("deepsweObservedAt") or deepswe_chart_doc.get("observedAt", DATE)
    deepswe_configurations = deepswe_chart_doc["configurations"]
    deepswe_overlap_n = len([item for item in deepswe_configurations if item.get("valueRankModelId")])
    bug_hunt_source_matches_n = scores.get("externalBenchmarks", {}).get("bugHunt", {}).get("matchedN", bug_hunt_ranking["matchedN"])
    aa_version = scores.get("benchmarkVersion") or "Artificial Analysis Intelligence Index v4.3.2"
    cost_mode = scores.get("costMode") or manifest.get("scoring", {}).get("costMode", "unknown")
    cost_mode_label = "AA evaluation cost only" if cost_mode == "aa-only" else cost_mode
    cost_coverage = scores.get("costCoverage") or manifest.get("scoring", {}).get("costCoverage", {})
    cost_missing_text = ", ".join(cost_coverage.get("missingModels", [])) or "none"
    dropped = scores.get("droppedDimensions")
    if dropped is None:
        dropped = coverage_document.get("scoring", {}).get(
            "droppedDimensions", manifest.get("scoring", {}).get("droppedDimensions", [])
        )
    cost_weight = next((weight for weight in weights if weight["key"] == "costComposite"), None)
    cost_weight_text = f"{cost_weight['weightPct']:.2f}%" if cost_weight else "not included"
    inclusion_md = model_inclusion_markdown(model_inclusion(scores.get("frontierSelection"), all_models))


    speed_coverage = coverage_document.get("fields", {}).get("speed", {})
    speed_missing_ids = set(speed_coverage.get("missingModels", []))
    speed_missing_text = names([model["name"] for model in models if model["id"] in speed_missing_ids])
    speed_selected_available_n = n - sum(model["id"] in speed_missing_ids for model in models)
    aa_index_estimated_models = names([model["name"] for model in models if model.get("intelligenceIndexStatus") == "estimated"])


    livebench_pareto_text = names([record["name"] for record in livebench_pareto]) if livebench_pareto else "none"
    livebench_supplemental_text = names([record["name"] for record in livebench_supplemental_rows]) if livebench_supplemental_rows else "none"
    livebench_supplemental_count = livebench_document.get("supplementalMatchedN", len(livebench_supplemental_rows))
    livebench_supplemental_label = f"{livebench_supplemental_count} official supplemental model" + ("s" if livebench_supplemental_count != 1 else "")


    pareto_text = names(pareto)
    drop_text = "\n".join(
        f"| {item['label']} | {names(item['missing'])} | {item['reason']} |" for item in dropped
    ) or "| None | — | All candidate dimensions have complete coverage. |"

    aa_reconciliation_report = reconcile_aa(data=data)
    aa_reconciliation_md, _ = aa_reconciliation_publication(aa_reconciliation_report)


    plan_candidate_headers = ["Model", "Primary rank", "AA Intelligence Index", "API evaluation cost", "Effective Plan evaluation cost", "Effective Plan cost per Index point", "Selected plan / multiple", "Evidence / source variant", "Source date", "Source"]
    plan_candidate_cells = []
    for model, field in zip(all_models, candidate_plan_cost_fields):
        route = field["planRoute"]
        plan_candidate_cells.append([
            model["name"],
            str(model["rank"]) if model.get("rank") is not None else "Unranked candidate",
            plan_intelligence_label(model, aa_document),
            plan_usd(field["apiCost"], "Not established"),
            plan_usd(field["planCostPerRun"], "API fallback" if route is None else "Not established"),
            plan_usd(field["planComparableCost"], "Not established") + (" (API fallback)" if route is None and field["planComparableCost"] is not None else ""),
            f"{route['planLabel']} / {route['valueMultiple']:g}×" if route else "No eligible route",
            (plan_evidence_label(route) + (f" / {route['sourceModel']}" if route.get("sourceModel") else "")) if route else "API fallback",
            (route.get("sourcePublicationDate") or route.get("reportDate") or route.get("validFrom") or "Not recorded") if route else "—",
            (route.get("sourceUrl") or "User assumption") if route else "—",
        ])

    plan_route_headers = ["Plan", "Eligible model variants", "Monthly fee", "API equivalent numerator", "Value Multiple", "Evidence / source model", "Source date", "Source"]
    plan_route_cells = []
    for route in plan_route_document["routes"]:
        plan_route_cells.append([
            route["planLabel"],
            ", ".join(model_by_id[model_id]["name"] if model_id in model_by_id else model_id for model_id in route["modelIds"]),
            plan_usd(route.get("planPriceUsd"), "Not established"),
            plan_usd(route.get("apiEquivalentUsd"), "Not measured") + (" (applied estimate)" if route.get("numeratorKind") == "applied_estimate" else ""),
            f"{route['valueMultiple']:g}×",
            plan_evidence_label(route) + (f" / {route['sourceModel']}" if route.get("sourceModel") else ""),
            route.get("sourcePublicationDate") or route.get("reportDate") or route.get("validFrom") or "Not recorded",
            route.get("sourceUrl") or "User assumption",
        ])


    claude_common = sorted(
        (route for route in plan_route_document.get("routes", []) if str(route.get("id", "")).endswith("common-opus55-assumption")),
        key=lambda route: float(route.get("planPriceUsd") or 0),
    )
    claude_common_copy = (
        "The common Claude multiples ("
        + "; ".join(
            f"{'Pro' if route['plan'] == 'Claude Pro' else 'Max $' + str(route['planPriceUsd'])} {route['valueMultiple']}×" for route in claude_common
        )
        + ") are an owner-authorized (2026-10-18) application of Opus 5.5's measured figures to the other Claude models, not measurements of those models; "
        "the same source measured Fable 5.1 at 12.4–12.7× on the Max plans, so the applied multiples may overstate the plan value of cheaper Claude models. "
    ) if claude_common else ""
    plan_policy_copy = (
        f"Plan route evidence as of {plan_route_document.get('asOf', 'not recorded')}. Effective Plan evaluation cost is AA API evaluation cost divided by the highest eligible Value Multiple. Effective Plan cost per Index point is that amount divided by the model's AA Intelligence Index; the Plan-basis rank uses it so that a plan allowance is credited with the work it buys and token-efficient models are rewarded, while models without an eligible route are compared on API cost per Index point. "
        "The candidate comparison includes unranked source candidates; a Plan route does not establish a primary composite rank or ValueRank quality frontier membership. "
        "For Anthropic and Codex, the user-selected SemiAnalysis analysis supplies controlled subscription-account measurements with workload projections; its allocation regime, workload and evaluated model remain in the route evidence. "
        "The common ChatGPT multiples (Plus 8.1×; Pro $100 10.55×; Pro $200 10.42×; Pro $500 10.772×) are a provisional cross-model application: the source projections evaluate Astra for Plus and Sol for the Pro tiers, and do not establish the same allowance for every GPT variant. "
        + claude_common_copy +
        "The highest eligible common GPT route is Pro $500 at 10.772×. MiMo Pro and MiMo Flash use a provisional user assumption of 1.5×; their subscription fee is not established and their API equivalent dollar numerator is not measured. "
        "For other providers, eligible measured routes require actual end-user API-priced usage, exact variants, plan tier and report date in the preceding month. Mixed or unidentified model usage remains provider/plan evidence and does not enter a model route. Provider allowance, quota and marketing figures cannot supply a measured numerator."
    )
    plan_comparison_md = (
        "\n\n## Plan Costs candidate comparison\n\n" + plan_policy_copy + "\n\n"
        + plan_markdown_table(plan_candidate_headers, plan_candidate_cells)
        + "\n\n### Plan route evidence\n\n" + plan_markdown_table(plan_route_headers, plan_route_cells)
        + "\n\nThe selected source is [SemiAnalysis](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x). Full route assumptions, allocation regimes, workloads, source links and eligibility are retained in `data/plan_cost_routes.json`.\n"
    )


    readme = f"""# ValueRank
**Frontier AI model ranking focused on production value**

**Version:** {VERSION}
**Updated:** {DATE}
**Scope:** {n} primary-ranked models from a {source_n}-model AA-mapped comparison roster, {d} retained dimensions including Bug Hunt Bench

Publication updated October 8, 2026 with the current AA frontier reconciliation and selected benchmark updates. The complete 31-configuration DeepSWE v1.1 chart was observed October 8; the original 25 configuration records retain their earlier per-row observation dates. Earlier AA component snapshots retain their recorded dates, while the newly captured AA frontier profiles are dated October 8 and MiMo owner run notes October 7. See per-model dates and capture precision in raw-data.md.

## Current result

The selected catalog is reconciled against AA's [Intelligence Index score versus total benchmark-run cost Pareto frontier](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index), and includes every model family on that observed frontier plus every near-frontier family (see Model inclusion below). The primary score uses each model's available exact-version values across the {d} retained dimensions; missing values remain null and each row's available priorities are renormalized to 100%. Every DeepSWE result retains its displayed agent, model and effort; results from other model versions or composite agents are not transferred. Provider claims fill owner gaps only for the exact benchmark version and evaluated variant, remain visibly labelled, and are replaced by owner results when available. Coverage and missing metrics are shown beside each score.

| Rank | Model | Overall | Quality | AA eval-cost penalty (lower better) | Baseline priority coverage | Missing metrics |
|---:|---|---:|---:|---:|---:|---|
{primary_rows(models, weights)}

The current Pareto frontier—undominated on composite cost versus quality—is: **{pareto_text}**.

{inclusion_md}
## Refresh basis and v1.9 scoring update

- The primary rank includes available exact-version evidence for each selected AA frontier model; it does not require every model to have every retained metric. The remaining **{len(unranked_models)}** candidates have no rankable primary score: **{unranked_names}**.
- For each model, ValueRank retains only its observed metrics, renormalizes that row's available dimension priorities, and reports `availablePriority / totalPriority` coverage plus missing metric names. No missing value receives a zero or neutral fill.
- Bug Hunt Bench has priority **{bug_hunt_weight['priority']}** and weight **{bug_hunt_weight['weightPct']:.2f}%** in the main rank. DeepSWE v1.1 has priority **{deepswe_weight['priority']}** and weight **{deepswe_weight['weightPct']:.2f}%**. A separate Bug Hunt emphasis view gives Bug Hunt still more weight.
- AA's Coding Agent Index v1.5 chart reports **{len(deepswe_configurations)} configurations** for DeepSWE v1.1 across **{deepswe_chart_doc['benchmarkTasks']} tasks**, observed **{deepswe_updated}**. All configurations and model-version mapping decisions are retained in [data/aa_deepswe.json](data/aa_deepswe.json); **{deepswe_overlap_n}** configurations map to selected model variants.
- Artificial Analysis now uses **{aa_version}**: AA-Briefcase v1.1, GDPval-AA v2.1, AutomationBench-AA, Terminal-Bench 4.0, SciCode, HLE, GDP.pdf, CritPt, AA-LCR v1.1, and split AA-Omniscience accuracy/reliability components. τ³-Banking and Terminal-Bench 2.1 remain historical source fields only.
- The standalone Terminal-Bench page has **{tb4_document['rowN']} official rows**, including **{tb4_document['matchedN']}/{tb4_document['cohortN']}** direct cohort matches. One separately labelled DeepSeek V4.1-Flash provider claim is used for the current `deepseek-v4-flash` API alias; official and claim counts are kept distinct.
- **{md_benchmark_link('LiveBench')} {livebench_document['release'].replace('_', '-')}** provides the four-task Instruction Following mean plus Overall Score and Cost Per Successful Task views; Instruction Following contributes where a selected model has an eligible value and is included in the row's available-priority calculation.
- The companion Bug Hunt emphasis ranking covers **{bug_hunt_ranking['matchedN']}** eligible exact-variant owner results and raises Bug Hunt to **{bug_hunt_ranking['benchmarkWeightPct']:.2f}%** within that separate view; its ranked table and source snapshot are documented in [scores.md](scores.md#bug-hunt-emphasis-ranking) and [data/bug_hunt.json](data/bug_hunt.json).
- The AA chart's full **{len(deepswe_configurations)}-configuration** DeepSWE v1.1 result set remains available in the raw-data table; model variants and Devin composite-agent results stay separate.
- The score retains **{d} primary dimensions**; **{names([item['label'] for item in dropped])}** remain supplemental under the published dimension-selection policy. A missing value in a retained dimension remains null and is omitted from that model's weighted score.
- AA output speed is numeric for **{speed_selected_available_n}/{n}** selected pages; **{speed_missing_text}** has no value. Where Speed is retained, its weight is applied only to rows with a value and included in their displayed coverage.
- AA total evaluation cost is available for **{cost_coverage.get('availableN', '—')}/{n}** primary models. API Costs uses that amount where available; Plan Costs divides the same amount by each model's highest eligible subscription Value Multiple and by its AA Intelligence Index (USD per Index point), and both views renormalize each row over its available dimensions.
- Earlier ValueRank versions are not numerically comparable because this release changes benchmark weights and the ranked cohort.

## Sources and audit trail

- [AA Coding Agent Index v1.5 — DeepSWE v1.1](https://artificialanalysis.ai/agents/coding-agents?coding-agents-performance-chart=deep-swe-v1.1) is the benchmark-owner source for all DeepSWE values in this release. The complete {len(deepswe_configurations)}-configuration chart inventory, observed {deepswe_updated}, and model-variant decisions are recorded in [data/aa_deepswe.json](data/aa_deepswe.json).
- [Artificial Analysis methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) and the linked first-party model pages for current component values and Intelligence Index evaluation cost.
- [LiveBench](https://livebench.ai/) and its [official release data repository](https://github.com/livebench/new-livebench), pinned at [release data commit {livebench_document['source'].get('releaseDataCommit', 'not recorded')}](https://github.com/livebench/new-livebench/commit/{livebench_document['source'].get('releaseDataCommit', '')}), for the 2026-06-25 task/category table, Instruction Following means, Overall Score, and Cost Per Successful Task.
- [Terminal-Bench 4.0](https://www.tbench.ai/) and the [official Harbor repository](https://github.com/harbor-framework/terminal-bench) for the current rendered leaderboard and task identity.
- [Bug Hunt Bench]({BUG_HUNT_URL}), with owner-published [combined scoreboard]({bug_hunt_document['sources']['scoreboard']}) and [run notes]({bug_hunt_document['sources']['runNotes']}) pinned to commit **{bug_hunt_document['sourceCommit']}**.
- [Refresh record](research/2026-09-29-valuerank-refresh-v4-3-2/README.md) for the v4.3.2 source change, evidence boundary, provider claims, and scoring decisions.
- [Provider claim ledger](data/provider_claims.json) for provider-sourced values, eligibility, and alias/variant caveats. Provider values never masquerade as benchmark-owner measurements.
- [Coverage matrix](data/coverage_matrix.json) for primary and supplemental availability, including fields not used in the score.

## Files

- [scores.md](scores.md): final ranking, weights, and normalized matrix
- [raw-data.md](raw-data.md): source values, selected AA variants, and supplemental coverage
- [methodology.md](methodology.md): frontier selection, benchmark versions, normalization, and row-level coverage
- [https://valuerank.alolabs.dev/](https://valuerank.alolabs.dev/): website, generated by `valuerank.site.build` (source under [valuerank/site/](valuerank/site/))
- [https://valuerank.alolabs.dev/benchmarks/terminal-bench-4/](https://valuerank.alolabs.dev/benchmarks/terminal-bench-4/): current Terminal-Bench 4.0 score-versus-cost page
- [research/2026-09-29-valuerank-refresh-v4-3-2/](research/2026-09-29-valuerank-refresh-v4-3-2/): reproducible v4.3.2 refresh package
- [data/](data/): machine-readable snapshots and generated outputs (pipeline code lives in [valuerank/](valuerank/))
- [docs/](docs/README.md): contributor documentation (repository layout, architecture, development, testing, refresh and release); `npm run verify` runs every check
"""
    (root / "README.md").write_text(readme + aa_reconciliation_md + plan_comparison_md)

    methodology = f"""# ValueRank Methodology

**Version:** {VERSION}
**Updated:** {DATE}

## Cohort and source versions

The selected catalog is reconciled against AA's current Pareto frontier of Intelligence Index score versus total USD benchmark-run cost and includes every model family on that frontier plus every near-frontier family; the full policy follows. AA's Coding Agent Index v1.5 chart publishes **{len(deepswe_configurations)} DeepSWE v1.1 configurations** across **{deepswe_chart_doc['benchmarkTasks']} tasks**, observed **{deepswe_updated}**. The primary rank includes every selected model with at least one eligible exact-version non-cost quality metric; a model does not need complete benchmark overlap. Models without an observed quality metric remain unranked. Each chart result retains its displayed model variant, agent, and effort.

- DeepSWE v1.1 source: [AA Coding Agent Index v1.5](https://artificialanalysis.ai/agents/coding-agents?coding-agents-performance-chart=deep-swe-v1.1). The published chart says each score averages pass@1 across three attempts per task; the complete {len(deepswe_configurations)}-configuration inventory and exact-variant mapping decisions are pinned in [data/aa_deepswe.json](data/aa_deepswe.json).
- AA source: [Intelligence Index methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking), current {aa_version}.
- AA Intelligence Index percentile comparisons use whole-point precision for every model because fresh public labels are rounded while older captures retain finer raw precision. Raw source inputs remain unchanged; sub-point differences should not be read as a reliable ordering.
- AA v4.3.2 model values: first-party model pages selected by data/aa_mapping.json and recorded in aa_metrics.json.
- LiveBench source: [livebench.ai](https://livebench.ai/), pinned release **2026-06-25** with seven categories, including the four-task Instruction Following category and published Cost Per Successful Task values. The data files are pinned to release commit **{livebench_document['source'].get('releaseDataCommit', 'not recorded')}**.
- Terminal-Bench source: [tbench.ai](https://www.tbench.ai/), current **4.0** rendered leaderboard snapshot with {tb4_document['rowN']} official rows, **{tb4_document['matchedN']}** direct cohort matches, and **{tb4_document.get('providerClaimN', 0)}** eligible provider claim.

Earlier publications used different source snapshots, weights, or cohorts. They remain historical; their numerical scores must not be compared directly with {VERSION}.

{inclusion_md}
## Primary dimensions

The retained dimension set is selected from eligible current source coverage and the published priority policy. For each dimension, only models with a genuine exact-version value are ranked; scores remain missing for other rows. Each model's available dimension priorities are then renormalized to 100%, and its `availablePriority / totalPriority` coverage and missing metrics are published with the score. Raw benchmark values remain in scores.json; normalized rank scores are calculated from available values only.

| # | Dimension | ValueRank weight | Direction |
|---:|---|---:|---|
{dimension_table(weights)}

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

The API Costs basis uses each model's AA total evaluation cost in USD. Plan Costs divides that same value by the model's highest eligible subscription Value Multiple and then by its AA Intelligence Index, so the Plan input is USD per Index point: a plan allowance is credited with the work it buys, which rewards token-efficient models. Models without an eligible route are compared on API cost per Index point. Lower cost ranks better in both views; the site opens on Plan Costs and the site switcher recalculates the primary composite when the cost basis changes.

## Missing-metric handling

- A retained dimension contributes to a model only when that model has an eligible value from the benchmark owner or an exact-version provider claim. Ranking within each dimension uses only models with eligible values.
- Missing values remain null in aa_metrics.json and are listed in coverage_matrix.json.
- Each row's retained priorities are renormalized over that model's available values. Coverage is available priority divided by total retained priority; missing metric names accompany the percentage.
- No zero, neutral 50, median, or mismatched-version value is used. Provider claims remain source-typed and are eligible only for the stated benchmark version and evaluated model/route.
- AA output speed covers **{speed_selected_available_n}/{n}** selected pages; **{speed_missing_text}** is missing. If retained, Speed contributes only where a value exists and the gap is included in row coverage.
- GPQA Diamond remains an explicitly labelled legacy ValueRank input; it is not a component of the v4.3.2 source composite.
- AA total evaluation cost is available for **{cost_coverage.get('availableN', '—')}/{n}** ranked models; the cost component uses **{cost_mode_label}** consistently across this cohort.
- LiveBench Instruction Following is available for **{sum(model.get('livebenchInstructionFollowing') is not None for model in models)}/{n}** ranked models and is scored where present. Terminal-Bench 4.0 is supplemental in this release under the published dimension-selection policy.
- Bug Hunt Bench has **{bug_hunt_source_matches_n}/{source_n}** exact owner results. Eligible exact-variant results contribute where present at the published Bug Hunt priority; the separate emphasis view includes **{bug_hunt_ranking['matchedN']}** rows with eligible results.

Dropped candidate dimensions:

| Dimension | Missing models | Decision |
|---|---|---|
{drop_text}

## Rank normalization

For each retained dimension, models with an eligible value are ranked from best to worst and mapped using that dimension's available sample size:

((n - rank) / (n - 1)) × 100

Rank 1 maps to 100, the worst observed rank maps to 0, and exact ties receive the average tied rank. The sample size is the number of models with a value for that dimension. Lower-is-better dimensions, including composite Cost, reverse the ordering before normalization.

## Benchmark evaluation cost (score input)

The Cost input uses **{cost_mode_label}** where an AA Intelligence Index total evaluation cost is available; lower evaluation cost is better. Plan Costs divides that same total benchmark cost by the model's highest eligible subscription Value Multiple and by its AA Intelligence Index (USD per Index point). A missing cost remains null and the row's other available priorities are renormalized; no DeepSWE leaderboard cost or missing-value fill is used.

## Quality score and interpretation

Overall Score is the weighted sum of a model's available retained dimensions, with that row's available priorities renormalized to 100%. Quality Score removes Cost and renormalizes the available non-cost dimensions to 100%. Scores are rank-relative to the values available for this release, not probabilities and not an absolute model capability scale; row coverage is displayed beside each score.

## Supplemental data

{md_benchmark_link('Artificial Analysis Intelligence Index')} exposes additional evaluations—such as MLCR, Harvey, APEX-Agents, MMMU-Pro, EnterpriseOpsGym, ITBench SRE, and legacy fields. They are preserved in aa_metrics.json when published, and their coverage is reported in coverage_matrix.json. AA-Briefcase, GDP.pdf, AutomationBench-AA, and AA's Terminal-Bench 4.0 evaluation are v4.3.2 source components, not standalone ValueRank dimensions. GPQA Diamond and the old τ³-Banking/TB2.1 fields are separately labelled legacy data.

{md_benchmark_link('LiveBench')} is incorporated as the current external Instruction Following source. Its four official task values—paraphrase, simplify, story_generation, and summarize—are averaged into the published Instruction Following value; LiveBench Overall is the mean of its seven category means. The LiveBench chart uses the official Overall Score against the official Cost Per Successful Task for the {livebench_document['matchedN']} matched cohort rows plus {livebench_supplemental_label}: {livebench_supplemental_text}.

{md_benchmark_link('Terminal-Bench 4.0')} is incorporated as the current external terminal-agent source. The official page shows {tb4_document['rowN']} owner rows; a separate provider-claim row is included for the current DeepSeek V4 Flash API alias and is explicitly labelled. Together they provide {tb4_document.get('rankingAvailableN', tb4_document['matchedN'])}/{tb4_document['cohortN']} eligible cohort values, leaving {len(tb4_document.get('rankingMissingModels', tb4_document['missingModels']))} gaps.

## Provider claim policy

When the benchmark owner has not published a result for a model, ValueRank uses a model-provider-published claim when the benchmark version and evaluated model identity match. The claim keeps its source type, direct source link, date, and any alias/variant caveat in the raw data and evidence ledger. A benchmark-owner result supersedes the claim when it becomes available. Claims for different versions or variants remain audit-only.

## Bug Hunt Bench scoring

Bug Hunt Bench reports planted bugs fixed out of **105** across two repositories. The owner scoreboard snapshot is pinned at commit **{bug_hunt_ranking['sourceCommit']}** and provides **{bug_hunt_source_matches_n}/{source_n}** exact results in the AA-mapped comparison roster. Each eligible exact-variant owner value contributes to that model's primary score at Bug Hunt priority **{bug_hunt_weight['priority']}** (**{bug_hunt_weight['weightPct']:.2f}%** before row-level renormalization).

The companion Bug Hunt emphasis ranking uses **{bug_hunt_ranking['matchedN']}** eligible owner-result rows and re-ranks the other available dimensions within that subset. It gives Bug Hunt priority **{bug_hunt_ranking['benchmarkPriority']}** out of **{bug_hunt_ranking['totalPriority']}**, or **{bug_hunt_ranking['benchmarkWeightPct']:.2f}%** before row-level renormalization. Ties use average rank, then lower cost and model name. Its scores are a separate weighting view and should not be compared numerically with the primary composite.

The scoreboard tests an agentic model-and-harness configuration. Runs vary in effort, agent CLI, route, and repeat count; those details remain in the table, and single-run rows are noisy. Models remain visible when one or more retained metrics are missing, with their available-priority coverage shown. A model with no rankable primary metric remains unranked. No values are inferred or neutral-filled. A provider claim may fill an owner gap only for an exact benchmark version and evaluated model variant, and an owner result supersedes it when published.

## Limitations

- The AA DeepSWE chart and the other AA Index components measure distinct tasks and use different evaluation setups; ValueRank is a transparent synthesis, not a new benchmark.
- Bug Hunt results also depend on the tested agent CLI/harness, effort, and route; they measure the tested stack, not model capability in isolation.
- Rank normalization discards magnitude differences. The AA DeepSWE chart publishes rounded percentage values without uncertainty intervals; read them alongside the exact agent and effort configuration.
- Page variants can differ by reasoning effort; the selected URL and variant are recorded per model.
- Provider claims may use a different harness or sampling procedure than the benchmark owner; displayed claim values are not presented as independent benchmark-owner measurements.
- AA output speed is numeric for **{speed_selected_available_n}/{n}** selected pages; **{speed_missing_text}** has no value. When retained, Speed affects only rows with a value and the per-row coverage makes that difference visible.
- LiveBench and Terminal-Bench have different task suites and release surfaces from the AA source component; their displayed values should not be substituted for one another or read as a continuous version-to-version series.
"""
    (root / "methodology.md").write_text(methodology + "\n\n## Subscription evidence policy\n\n" + plan_policy_copy + "\n")


    norm_rows = "\n".join(
        f"| {model['rank']} | {model['name']} | [{norm_values(model, weights)}] |"
        for model in models
    )
    scores_md = f"""# ValueRank {VERSION} Scores

**Updated:** {DATE} · **Cohort:** {n} · **Retained dimensions:** {d} · **Default cost basis:** API Costs (AA total evaluation cost)

API Costs uses the AA total evaluation cost in USD; Plan Costs divides that same value by the highest eligible subscription Value Multiple and by the model's AA Intelligence Index (USD per Index point). The site switcher recalculates the main rank and cost-based charts using the selected basis.

## Final ranking

| Rank | Model | Overall | Quality | Quality Rank | AA eval-cost penalty (lower better) | Baseline priority coverage | Missing metrics |
|---:|---|---:|---:|---:|---:|---:|---|
{chr(10).join(f"| {m.get('rank') or '—'} | {m['name']} | {fnum(m.get('overallScore'), 1)} | {fnum(m.get('qualityScore'), 1)} | {m.get('qualityRank') or '—'} | {fnum(m.get('costComposite'))} | {metric_coverage_summary(m, weights)[0]} | {metric_coverage_summary(m, weights)[1]} |" for m in models)}

## Bug Hunt Emphasis Ranking

Bug Hunt is included in the main **{n}-model primary ranking** at **{bug_hunt_weight['weightPct']:.2f}%**. The companion emphasis view uses the same cohort and increases Bug Hunt's weight to **{bug_hunt_ranking['benchmarkWeightPct']:.2f}%** by re-ranking the other retained dimensions within those models.

| Bug Hunt rank | Model | Fixed / 105 | Emphasis score | Runs / aggregation | Effort | Harness / route | Primary rank |
|---:|---|---:|---:|---|---|---|---:|
{bug_hunt_emphasis_table(bug_hunt_ranking, bug_hunt_records)}

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

The current AA Intelligence Index score-versus-total-benchmark-cost frontier, and its near-frontier families, are reconciled into the selected catalog (see Model inclusion in methodology.md). The primary rank uses each model's available exact-version values and renormalizes its retained priorities per row; the ranking table reports the available-priority percentage and missing metric names. {len(unranked_models)} source candidates have no rankable primary score. Dropped candidate dimensions are listed below; missing values remain null rather than receiving zero or neutral scores.

## External benchmark coverage

{md_benchmark_link('Artificial Analysis Intelligence Index')} provides the current AA component scores used by this release. {md_benchmark_link('LiveBench')} Instruction Following contributes for rows with an eligible value; its Overall Score and Cost Per Successful Task remain supplemental. {md_benchmark_link('Terminal-Bench 4.0')} remains supplemental under this release's dimension-selection policy. See [raw-data.md](raw-data.md) for source-backed tables.
"""
    (root / "scores.md").write_text(scores_md)

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
    livebench_raw_rows = livebench_table(livebench_rows)
    tb4_raw_rows = tb4_table(tb4_rows)
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

This publication combines source snapshots with different observation dates. The complete AA DeepSWE v1.1 chart inventory was observed October 8 and contains 31 configurations; the original 25 configuration records retain their prior per-row observation dates. Earlier AA component snapshots retain their recorded dates, while newly captured AA frontier profiles were observed October 8. Bug Hunt's base snapshot remains pinned separately from the selectively added MiMo owner run notes observed October 7. The publication date does not imply that every benchmark row was recaptured October 8. Per-model AA dates, precision, and source notes appear below; rounded public chart/tooltips preserve their displayed precision and do not establish hidden unrounded payload values.

The AA chart publishes {len(deepswe_configurations)} DeepSWE v1.1 agent/model configurations; {deepswe_overlap_n} exact model variants map to selected catalog entries. The primary score uses eligible exact-version dimensions available for each model rather than requiring complete benchmark overlap. Missing values remain null and are reported with row-level priority coverage. Raw AA values keep their source units: Elo fields remain Elo, and ratio fields are shown as percentages. **{aa_index_estimated_models}** has an AA Intelligence Index estimate; it is labelled in the matrix. Benchmark-owner results, estimates, and provider claims remain source-typed.

## DeepSWE v1.1 AA chart configurations

The visible chart contains all {len(deepswe_configurations)} configurations in the October 8 capture. Pass@1 is averaged across three attempts per task. Exact model-version mismatches and composite-agent configurations remain separate from ValueRank model-family rows; the original 25 records retain their previous row observation dates.

| # | Agent | Evaluated model variant | Effort | Pass@1 | ValueRank mapping | Mapping note |
|---:|---|---|---|---:|---|---|
{deepswe_chart_table(deepswe_configurations)}

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

The benchmark owner reports planted bugs fixed out of 105 across two repositories. This snapshot has **{bug_hunt_source_matches_n}/{source_n}** eligible exact selected-variant Bug Hunt results. Eligible results contribute where available to each model’s primary score; the separate Bug Hunt emphasis view includes **{bug_hunt_ranking['matchedN']}** exact-variant results. The base snapshot is pinned to [scoreboard commit {bug_hunt_ranking['sourceCommit']}]({bug_hunt_document['sources']['scoreboard']}); selectively added MiMo records link to their individual owner notes at commit `7dd3c23a4c86a3fac586707d01129bf549bae325`, observed October 7. Per-record links preserve each source snapshot. Models without any available primary quality dimension remain unranked: {unranked_names}.

| Model | Fixed / 105 | Runs / aggregation | Evaluated model | Effort and status | Harness | Route | Coverage |
|---|---:|---|---|---|---|---|---|
{bug_hunt_raw_table(all_models, bug_hunt_records)}

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

The API Costs baseline uses AA total evaluation cost in USD. AA cost is available for **{cost_coverage.get('availableN', '—')}/{cost_coverage.get('cohortN', n)}** ranked models; missing values are **{cost_missing_text}**. Plan Costs divides the same AA cost by each model's highest eligible subscription Value Multiple and by its AA Intelligence Index (USD per Index point). No DeepSWE leaderboard cost is used.

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

- [data/aa_deepswe.json](data/aa_deepswe.json): AA Coding Agent Index v1.5 DeepSWE v1.1 chart, all {len(deepswe_configurations)} configurations and exact model-variant mappings
- [data/aa_metrics.json](data/aa_metrics.json): decoded current AA model payloads
- [data/scores.json](data/scores.json): normalized scores and rankings
- [data/coverage_matrix.json](data/coverage_matrix.json): primary and supplemental availability
- [data/livebench.json](data/livebench.json): pinned LiveBench task/category/cost snapshot and Pareto data
- [data/tb4.json](data/tb4.json): normalized official Terminal-Bench 4.0 rendered leaderboard
- [data/bug_hunt.json](data/bug_hunt.json): pinned Bug Hunt scoreboard, exact matches, and explicit mismatches
- [research/2026-09-29-valuerank-refresh-v4-3-2/README.md](research/2026-09-29-valuerank-refresh-v4-3-2/README.md): v4.3.2 source-change, evidence, and scoring record
- [data/provider_claims.json](data/provider_claims.json): provider claim values, source URLs, eligibility, and caveats
- [data/deepswe.json](data/deepswe.json): historical DeepSWE Best snapshot retained for audit only; it is not used for current DeepSWE scores
- [data/tb4-browser-2026-09-29.json](data/tb4-browser-2026-09-29.json): built-in browser Terminal-Bench snapshot
"""
    (root / "raw-data.md").write_text(raw_data + aa_reconciliation_md + plan_comparison_md)

    print(json.dumps({
        "version": VERSION,
        "models": n,
        "dimensions": d,
        "dropped": [item["label"] for item in dropped],
        "outputs": ["README.md", "methodology.md", "scores.md", "raw-data.md"],
    }, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
