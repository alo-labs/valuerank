"""Shared public vocabulary: source URLs, the model-inclusion policy and route evidence labels.

The Markdown emitter (``valuerank.emit_docs``) and the site view model (``valuerank.site.viewmodel``)
both import from here, so the README and the website state the same rules, numbers and links.
"""

from __future__ import annotations

AA_INDEX_URL = "https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index"
AA_METHODOLOGY_URL = "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
AA_DEEPSWE_URL = "https://artificialanalysis.ai/agents/coding-agents?coding-agents-performance-chart=deep-swe-v1.1"
AA_CODING_AGENTS_URL = "https://artificialanalysis.ai/agents/coding-agents"
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


def plan_evidence_label(route):
    if route.get("sameModelAcrossEfforts"):
        # O88, O90 (I74 L1): the same model's controlled measurement serving another effort is measured evidence.
        return "Same-model measurement from another effort (owner decisions O88, O90)"
    if route.get("evidenceClass") == "user_assumption":
        return "Provisional assumption"
    if route.get("evidenceClass") == "provider_quota_ceiling":
        # O46: the quota-implied ceiling, an owner-authorised provider-derived figure, never a measurement.
        return "Provider quota ceiling (owner decision O46; not a measurement)"
    if route.get("evidenceClass") == "controlled_account_workload_projection":
        # O40: an exact measurement the selected article added after the owner's selection replaces the transfer at once.
        added = f" (added after selection, {route['addedAfterSelection']})" if route.get("addedAfterSelection") else ""
        return "Controlled account measurement / workload projection" + added
    return str(route.get("evidenceClass", "Unclassified")).replace("_", " ")


FRONTIER_RULE = (
    "Every model family on the Pareto frontier that Artificial Analysis (AA) renders on its Intelligence Index versus "
    "total cost to run chart is ranked at its highest point on that line (along the strictly rising line also its dearest). "
    "Frontier membership is AA's rendered line as observed; ValueRank never recomputes it from rounded values."
)
NEAR_FRONTIER_RULE = (
    "A plotted configuration is near-frontier when its public (rounded integer) Intelligence Index is within {gap} points of the "
    "rendered frontier's Index at its cost, meaning the highest Index among rendered-frontier points that cost no more. "
    "Every near-frontier family is ranked or is explicitly deferred by a dated, reasoned roster decision. Every configuration AA plots on "
    "the frontier or within the gap is a cohort row (O51); a near family's primary configuration is its near point with the smallest Index gap. The cost ratio to the frontier is reported for information only."
)
DEFAULT_NEAR_GAP = 3


def _count(value, noun, plural=None):
    return f"{value} {noun if value == 1 else plural or noun + 's'}"


def _clean_number(value):
    return str(int(value)) if isinstance(value, (int, float)) and float(value).is_integer() else str(value)


def _configuration_name(model):
    """``Name (effort)``, so several ranked efforts of one family read distinctly (O33)."""

    suffix = f" ({model['aaVariant']})" if model.get("aaVariant") else ""
    return model["name"] if model["name"].endswith(suffix) else model["name"] + suffix


def model_inclusion(selection, models):
    """The model-inclusion policy and its observed facts, read from ``frontierSelection`` (optional, every field)."""

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
            footnotes.setdefault(model["aaFrontierFootnote"], []).append(_configuration_name(model))
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
