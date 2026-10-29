"""v3 cost diagnostics: Index figures, target-basket readiness, the SWE cost companion and the matched-cost object.

Every output here is a diagnostic: published beside the ranking, never scored.

* ``index_diagnostics`` (Outputs, item 4): AA Intelligence Index, total Index cost, USD per Index point, the
  canonical Index token counts and median output speed of the exact configuration.
* ``basket_readiness`` (E22, E42): per target component its inclusion status, missing configurations, task
  multiplicity, cost availability and the quality weight it prices; per scored row its expenditure shares
  s_ie = c_ie / C_iW and concentration HHI_i; the task-family overlap matrix; the priced-mix coverage.
* ``swe_companion`` (O14): c_SWE from published SWE per-task costs, flagged when its ratio to the basket cost
  deviates by more than 50% from the panel median.
* ``matched_cost`` (E24, E55, E103): C^match over AA-priced execution families with frozen quality-derived
  weights, its pairwise reversals against the basket cost and the R_i warning, on the main-workload panel.
"""

from __future__ import annotations

import hashlib
import json
import statistics

from valuerank import basket
from valuerank import quality as q

# Execution family behind each quality leaf (E55): a leaf references exactly one family, and a target component
# prices the leaf when the family runs inside it (Terminal-Bench runs in AA's Index and in the Coding Agent Index).
LEAF_FAMILIES = {
    "bugHunt": "bug-hunt",
    "frontierCode": "frontiercode-v1.1-main",
    "terminalBench": "terminal-bench-v4",
    "gdpval": "gdpval-aa",
    "automationBench": "automationbench-aa",
    "omniscience": "omniscience",
    "lcr": "artificial-analysis-long-context-reasoning",
    "hle": "humanitys-last-exam",
    "scicode": "scicode",
    "critpt": "critpt",
    # O53-O55: leaves run outside AA, whose task families no AA cost component prices.
    "vibeCode": "vals-vibe-code-bench",
    "codeMigration": "vals-code-migration",
    "livebench2Overall": "livebench-2-overall",
    "aiCodingDaily": "ai-coding-daily",
}
# Task families inside each target component (E42); the Coding Agent Index pools three families.
COMPONENT_FAMILIES = {
    basket.CODING_AGENT_INDEX: tuple(basket.CODING_AGENT_TASKS),
    basket.FRONTIERCODE: ("frontiercode-v1.1-main",),  # O116: the stand-in while the Coding Agent Index is pending
    "itbench-aa": ("itbench-aa",),
    **{component: (component,) for component in basket.INDEX_SDLC_TASKS},
}
COMPONENT_FAMILIES["terminalbench-4-0"] = ("terminal-bench-v4",)
STAND_IN_IDLE = "not needed: the Coding Agent Index it stands in for is admitted (O116)"
POOLED = "unidentified: the component publishes one pooled cost across its families"

# Matched-cost families (E103): leaves whose execution family has an exact AA per-evaluation cost per task for
# every configuration (task count x mean cost per task); the AA Index evaluation slug and its task count.
MATCHED_FAMILIES = {
    "terminalBench": ("terminalbench-4-0", basket.INDEX_SDLC_TASKS["terminalbench-4-0"]),
    "gdpval": ("gdpval-aa", basket.INDEX_SDLC_TASKS["gdpval-aa"]),
    "automationBench": ("automationbench-aa", basket.INDEX_SDLC_TASKS["automationbench-aa"]),
    "lcr": ("artificial-analysis-long-context-reasoning", basket.INDEX_SDLC_TASKS["artificial-analysis-long-context-reasoning"]),
    "scicode": ("scicode", basket.INDEX_SDLC_TASKS["scicode"]),
    "hle": ("humanitys-last-exam", basket.INDEX_RESIDUAL_TASKS["humanitys-last-exam"]),
    "critpt": ("critpt", basket.INDEX_RESIDUAL_TASKS["critpt"]),
    "omniscience": ("omniscience", basket.INDEX_RESIDUAL_TASKS["omniscience"]),
}
UNPRICED_REASONS = {
    "bugHunt": "the owner's runs publish no cost",
    "frontierCode": "the Coding Agent Index v2.0 publishes one pooled cost for FrontierCode, SWE-Atlas-QnA-AA and Terminal-Bench (O50)",
    "vibeCode": "run by Vals AI, outside every AA cost component",
    "codeMigration": "run by Vals AI, outside every AA cost component",
    "livebench2Overall": "run by LiveBench, outside every AA cost component",
    "aiCodingDaily": "run by AI Coding Daily, outside every AA cost component",
}
# Leaves whose score is a solved fraction, so a cost per solved task is defined (not GDPval's Elo or the Omniscience index).
SOLVED_FRACTION_LEAVES = {"terminalBench", "lcr", "hle", "scicode", "critpt"}
MATCHED_MIN_PRICED_WEIGHT = 0.40
MATCHED_RATIO_LIMIT = 1.5
MATCHED_RANK_LIMIT = 3
SWE_COMPONENTS = (basket.CODING_AGENT_INDEX, "terminalbench-4-0")
SWE_DEVIATION_LIMIT = 0.5


def index_diagnostics(page: dict) -> dict:
    """Outputs item 4: AA's Index figures for the exact configuration (diagnostics only, never scored)."""

    index = page.get("intelligenceIndex")
    total = (page.get("intelligenceIndexCost") or {}).get("total")
    valid = isinstance(index, (int, float)) and index > 0 and isinstance(total, (int, float))
    return {
        "intelligenceIndex": index,
        "indexTotalCostUsd": total,
        "usdPerIndexPoint": total / index if valid else None,
        "indexTokens": page.get("canonicalIntelligenceIndexTokenCount"),
        "outputSpeedTokensPerSecond": (page.get("outputSpeedVariance") or {}).get("median"),
    }


def _tasks(component: str):
    if component == basket.CODING_AGENT_INDEX:
        return sum(basket.CODING_AGENT_TASKS.values())
    return basket.INDEX_SDLC_TASKS.get(component, "chart total (no task count)")


def basket_readiness(rows: list[dict], admission: dict, main_workload: str) -> dict:
    """E22/E42: target-basket readiness, expenditure shares and concentration, and the task-family overlap matrix."""

    priced_by = {
        component: {leaf.key for leaf in q.LEAVES if LEAF_FAMILIES[leaf.key] in COMPONENT_FAMILIES[component]}
        for component in basket.TARGET_COMPONENTS
    }
    components = {}
    for component in basket.TARGET_COMPONENTS:
        item = admission["components"][component]
        missing = sorted(row["id"] for row in rows if (row["components"].get(component) or {}).get("completeness") != basket.COMPLETE)
        components[component] = {
            "status": "admitted" if item["admitted"] else STAND_IN_IDLE if item.get("standsInFor") and not item.get("eligible") else "pending capture",
            "missingConfigurations": missing,
            "tasks": _tasks(component),
            "costAvailable": item["available"],
            "costComplete": item["covered"],
            "pricedQualityWeight": sum(q.LEAF_BY_KEY[key].weight for key in sorted(priced_by[component])) / 100.0,
        }
    priced_leaves = sorted({key for component in admission["admitted"] for key in priced_by[component]})
    shares = {}
    for row in rows:
        if row["cost"]["workload"] != main_workload or not row["cost"]["costUsd"]:
            continue
        total = row["cost"]["costUsd"]
        split = {component: row["components"][component]["costUsd"] / total for component in row["cost"]["components"]}
        shares[row["id"]] = {"shares": split, "hhi": sum(share ** 2 for share in split.values())}
    families = sorted({family for members in COMPONENT_FAMILIES.values() for family in members})
    overlap = {
        family: sorted(component for component, members in COMPONENT_FAMILIES.items() if family in members)
        for family in families
    }
    return {
        "components": components,
        "pricedMixCoverage": sum(q.LEAF_BY_KEY[key].weight for key in priced_leaves) / 100.0,
        "pricedLeaves": priced_leaves,
        "expenditure": shares,
        "overlap": {family: members for family, members in overlap.items() if len(members) > 1},
        "familyConcentration": {component: POOLED for component, members in COMPONENT_FAMILIES.items() if len(members) > 1},
    }


def _panel_ratios(values: dict, reference: dict) -> dict:
    return {row_id: values[row_id] / reference[row_id] for row_id in values if reference.get(row_id)}


def swe_companion(rows: list[dict], main_workload: str) -> dict:
    """O14: c_SWE = the SWE components' published per-task costs times their tasks; flagged against the panel median."""

    costs, basket_costs = {}, {}
    for row in rows:
        detail = row["components"]
        if row["cost"]["workload"] != main_workload or any((detail.get(key) or {}).get("costUsd") is None for key in SWE_COMPONENTS):
            continue
        costs[row["id"]] = sum(detail[key]["costUsd"] for key in SWE_COMPONENTS)
        basket_costs[row["id"]] = row["cost"]["costUsd"]
    ratios = _panel_ratios(costs, basket_costs)
    median = statistics.median(ratios.values()) if ratios else None
    return {
        "rule": "c_SWE = Coding Agent Index cost + Terminal-Bench 4.0 (AA Index run) cost, from published per-task costs; flagged when its ratio to the basket cost deviates by more than 50% from the panel median",
        "excludedComponents": {},  # O50: FrontierCode is priced inside the Coding Agent Index v2.0
        "medianRatio": median,
        "rows": {
            row_id: {"cSweUsd": costs[row_id], "ratio": ratio, "flag": abs(ratio / median - 1.0) > SWE_DEVIATION_LIMIT}
            for row_id, ratio in ratios.items()
        },
        "unidentified": sorted(row["id"] for row in rows if row["cost"]["workload"] == main_workload and row["id"] not in costs),
    }


def _ranks(values: dict) -> dict:
    """Competition ranks, 1 = cheapest."""

    ordered = sorted(values.values())
    return {row: 1 + sum(1 for other in ordered if other < value) for row, value in values.items()}


def matched_cost(rows: list[dict], main_workload: str) -> dict:
    """E24/E55/E103: C^match over AA-priced execution families with frozen weights, and its warnings against C_W."""

    priced_weight = sum(q.LEAF_BY_KEY[leaf].weight for leaf in MATCHED_FAMILIES) / 100.0
    weights = {leaf: q.LEAF_BY_KEY[leaf].weight / (100.0 * priced_weight) for leaf in MATCHED_FAMILIES}
    definition = {
        "families": {leaf: {"family": LEAF_FAMILIES[leaf], "evaluation": slug, "tasks": tasks} for leaf, (slug, tasks) in MATCHED_FAMILIES.items()},
        "weights": weights,
        "priceRule": "AA's published cost per task for the exact configuration (provider-reported tokens at AA's prices) times the published task count",
        "panelRule": "main-workload rows with every matched family priced, fixed before ranks are examined",
    }
    definition["id"] = hashlib.sha256(json.dumps(definition, sort_keys=True).encode()).hexdigest()[:16]
    result = {
        "definition": definition,
        "pricedQualityWeight": priced_weight,
        "unpricedLeaves": {leaf: UNPRICED_REASONS[leaf] for leaf in UNPRICED_REASONS if leaf in q.LEAF_BY_KEY},
    }
    if priced_weight < MATCHED_MIN_PRICED_WEIGHT:
        return {**result, "status": "unidentified (priced quality weight below 40%)", "rows": {}, "reversals": [], "warnings": []}
    matched, reference, feasibility = {}, {}, {}
    for row in rows:
        costs = {item["slug"]: item.get("costPerTask") for item in row["page"].get("intelligenceIndexEvaluations") or []}
        passes = {leaf: costs[slug] * tasks for leaf, (slug, tasks) in MATCHED_FAMILIES.items() if isinstance(costs.get(slug), (int, float))}
        observations = row["evidence"]["observations"]
        feasibility[row["id"]] = {
            leaf: {
                "passCostUsd": passes.get(leaf),
                "costPerSolvedTaskUsd": (
                    passes[leaf] / (tasks * observations[leaf].z / 100.0)
                    if leaf in SOLVED_FRACTION_LEAVES and leaf in passes and leaf in observations and observations[leaf].z > 0 else None
                ),
                "panelWeight": weights[leaf],
            }
            for leaf, (_slug, tasks) in MATCHED_FAMILIES.items()
        }
        if row["cost"]["workload"] == main_workload and len(passes) == len(MATCHED_FAMILIES) and row["cost"]["costUsd"]:
            matched[row["id"]] = sum(weights[leaf] * passes[leaf] for leaf in MATCHED_FAMILIES)
            reference[row["id"]] = row
    ratios = _panel_ratios(matched, {row_id: row["cost"]["costUsd"] for row_id, row in reference.items()})
    median = statistics.median(ratios.values()) if ratios else None
    match_rank = _ranks(matched)
    basket_rank = _ranks({row_id: row["cost"]["costUsd"] for row_id, row in reference.items()})
    panel = sorted(matched)
    reversals = [
        [a, b]
        for index, a in enumerate(panel)
        for b in panel[index + 1:]
        if (matched[a] - matched[b]) * (reference[a]["cost"]["costUsd"] - reference[b]["cost"]["costUsd"]) < 0
        and (reference[a]["cost"]["highUsd"] < reference[b]["cost"]["lowUsd"] or reference[b]["cost"]["highUsd"] < reference[a]["cost"]["lowUsd"])
    ]
    warnings = [
        row_id for row_id in panel
        if (ratios[row_id] / median > MATCHED_RATIO_LIMIT or ratios[row_id] / median < 1.0 / MATCHED_RATIO_LIMIT)
        and abs(match_rank[row_id] - basket_rank[row_id]) > MATCHED_RANK_LIMIT
    ]
    return {
        **result,
        "status": "evaluated",
        "panel": panel,
        "unidentified": sorted(row["id"] for row in rows if row["id"] not in matched),
        "medianRatio": median,
        "rows": {
            row_id: {"cMatchUsd": matched[row_id], "ratio": ratios[row_id], "matchRank": match_rank[row_id], "basketRank": basket_rank[row_id]}
            for row_id in panel
        },
        "reversals": reversals,
        "warnings": warnings,
        "feasibility": feasibility,
    }
