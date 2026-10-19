"""The SDLC cost basket (owner decision O15): component costs, completeness, admission and the workload.

C_W, the scored API cost, is the sum of AA's published costs for the admitted
basket components of an exact configuration: the seven SDLC evaluations of the
AA Intelligence Index, the Coding Agent Index total and, once admitted, the
chart-captured FrontierCode and ITBench-AA totals. HLE, AA-Omniscience and
CritPt are excluded from C_W; together with the seven they reconcile to AA's
published total Index cost, which stays a diagnostic.

A component is admitted to the workload when exact-configuration cost exists for
at least two-thirds of the ranked rows (the reference panel). A row missing an
admitted component is scored on the subset it has (owner decision O17); a row is
eligible for the interval outputs only when no admitted component is marked
incomplete by AA (FullCost, owner decision O27).
"""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction

# Fixed task counts of the AA Intelligence Index v4.3.2 evaluations (AA total = sum of cost per task x count).
INDEX_SDLC_TASKS = {
    "aa-briefcase": 91,
    "gdpval-aa": 220,
    "gdp-pdf": 100,
    "automationbench-aa": 657,
    "terminalbench-4-0": 66,
    "scicode": 288,
    "artificial-analysis-long-context-reasoning": 100,
}
INDEX_RESIDUAL_TASKS = {"humanitys-last-exam": 2158, "critpt": 70, "omniscience": 6000}
CODING_AGENT_TASKS = {"deep-swe-v1.1": 113, "swe-atlas-qna": 124, "terminal-bench-v4": 66}
CODING_AGENT_REPETITIONS = 3
CODING_AGENT_INDEX = "coding-agent-index"
CHART_COMPONENTS = ("frontiercode", "itbench-aa")
TARGET_COMPONENTS = (CODING_AGENT_INDEX, *CHART_COMPONENTS, *INDEX_SDLC_TASKS)
COMPONENT_LABELS = {
    CODING_AGENT_INDEX: "Coding Agent Index",
    "frontiercode": "FrontierCode",
    "itbench-aa": "ITBench-AA",
    "aa-briefcase": "AA-Briefcase",
    "gdpval-aa": "GDPval-AA",
    "gdp-pdf": "GDP.pdf",
    "automationbench-aa": "AutomationBench-AA",
    "terminalbench-4-0": "Terminal-Bench 4.0 (AA Index run)",
    "scicode": "SciCode",
    "artificial-analysis-long-context-reasoning": "AA-LCR",
}
ADMISSION_SHARE = Fraction(2, 3)
CHART_HALF_WIDTH_USD = 0.5  # chart labels are rounded to USD 1

COMPLETE = "confirmed-complete"
UNRESOLVED = "unresolved"
INCOMPLETE = "confirmed-incomplete"


def component_cost(cost_usd, *, half_width=0.0, completeness=COMPLETE, source, configuration=None, detail=None) -> dict:
    return {
        "costUsd": cost_usd,
        "halfWidthUsd": half_width,
        "completeness": completeness,
        "source": source,
        "configuration": configuration,
        "detail": detail or {},
    }


def index_components(evaluations: list[dict], published_total: float | None) -> tuple[dict, dict]:
    """The seven SDLC component costs and the Index reconciliation for one AA model page.

    Each evaluation's cost is its published cost per task times its fixed task
    count. When the ten evaluations reproduce AA's published total at source
    precision, the components are confirmed complete; otherwise unresolved.
    """

    by_slug = {item.get("slug"): item.get("costPerTask") for item in evaluations}
    all_tasks = {**INDEX_SDLC_TASKS, **INDEX_RESIDUAL_TASKS}
    costs = {slug: by_slug[slug] * tasks for slug, tasks in all_tasks.items() if isinstance(by_slug.get(slug), (int, float))}
    complete_set = len(costs) == len(all_tasks)
    seven = sum(costs[slug] for slug in INDEX_SDLC_TASKS if slug in costs)
    residual = sum(costs[slug] for slug in INDEX_RESIDUAL_TASKS if slug in costs)
    reconstructed = seven + residual
    relative_error = (
        abs(reconstructed - published_total) / published_total
        if complete_set and isinstance(published_total, (int, float)) and published_total > 0
        else None
    )
    reconciled = relative_error is not None and relative_error <= 1e-6
    status = COMPLETE if reconciled else UNRESOLVED
    components = {
        slug: component_cost(
            costs[slug],
            completeness=status,
            source="AA Intelligence Index evaluation cost (cost per task x task count)",
            detail={"tasks": INDEX_SDLC_TASKS[slug], "costPerTaskUsd": by_slug[slug]},
        )
        for slug in INDEX_SDLC_TASKS
        if slug in costs
    }
    reconciliation = {
        "sdlcSevenUsd": seven,
        "residualUsd": residual,
        "reconstructedTotalUsd": reconstructed,
        "publishedTotalUsd": published_total,
        "relativeError": relative_error,
        "reconciled": reconciled,
    }
    return components, reconciliation


def coding_agent_component(record: dict | None) -> dict | None:
    """The Coding Agent Index cost record for one exact configuration (owner decision O27).

    The record is AA's documented cost-to-run metric (average API cost per task,
    a pooled per-task-attempt average that excludes missing telemetry) times the
    303 required tasks. AA's undocumented ``sums.costUsd`` is kept only as a
    reconciliation diagnostic; attempt coverage is a precision diagnostic (E53).
    """

    if record is None or not record.get("meanCostPerTaskUsd"):
        return None
    required_tasks = sum(CODING_AGENT_TASKS.values())
    mean = record["meanCostPerTaskUsd"]
    total = record.get("totalCostUsd")
    attempts = sum(component.get("attempts") or 0 for component in record.get("components") or [])
    return component_cost(
        mean * required_tasks,
        completeness=COMPLETE,
        source="AA Coding Agent Index cost to run (mean API cost per task) x 303 tasks",
        configuration=record["label"],
        detail={
            "meanCostPerTaskUsd": mean,
            "requiredTasks": required_tasks,
            "publishedSumUsd": total,
            "sumTaskEquivalent": total / mean if total is not None else None,
            "attempts": attempts,
            "requiredAttempts": required_tasks * CODING_AGENT_REPETITIONS,
        },
    )


def chart_component(row: dict | None, *, source: str) -> dict | None:
    """A chart-captured total (rounded to USD 1); AA's '*' marks declined tasks, i.e. an incomplete run."""

    if row is None or row.get("totalUsd") is None:
        return None
    return component_cost(
        float(row["totalUsd"]),
        half_width=CHART_HALF_WIDTH_USD,
        completeness=INCOMPLETE if row.get("declinedTasks") else COMPLETE,
        source=source,
        configuration=row["model"],
        detail={"label": row.get("totalUsdLabel")},
    )


def admitted_components(costs_by_row: dict, ranked_ids: list[str]) -> dict:
    """Admission per target component: exact cost for at least two-thirds of the ranked rows (E26)."""

    result = {}
    for component in TARGET_COMPONENTS:
        panel = [row_id for row_id in ranked_ids if (costs_by_row.get(row_id) or {}).get(component) is not None]
        share = Fraction(len(panel), len(ranked_ids)) if ranked_ids else Fraction(0)
        result[component] = {
            "admitted": bool(ranked_ids) and share >= ADMISSION_SHARE,
            "referencePanel": panel,
            "covered": len(panel),
            "ranked": len(ranked_ids),
        }
    return result


def workload_hash(components: list[str]) -> str:
    """A stable identity for a workload: its components in canonical order."""

    canonical = json.dumps(sorted(components), separators=(",", ":"))
    return hashlib.sha256(canonical.encode()).hexdigest()[:16]


def row_cost(costs: dict, admitted: list[str]) -> dict:
    """C_W for one row: the displayed sum, its precision interval, and the eligibility predicates.

    A row missing an admitted component is a subset row (O17): its cost is the sum
    over the components it has, on that subset's own workload identity.
    """

    present = [component for component in admitted if costs.get(component) is not None]
    missing = [component for component in admitted if costs.get(component) is None]
    total = sum(costs[component]["costUsd"] for component in present) if present else None
    half_width = sum(costs[component]["halfWidthUsd"] for component in present)
    incomplete = [component for component in present if costs[component]["completeness"] != COMPLETE]
    return {
        "costUsd": total,
        "lowUsd": None if total is None else total - half_width,
        "highUsd": None if total is None else total + half_width,
        "workload": workload_hash(present) if present else None,
        "components": present,
        "missingComponents": missing,
        "subset": bool(missing),
        "partialComponents": incomplete,
        "fullCost": not missing and not incomplete and bool(present),
    }


def expenditure_shares(costs: dict, components: list[str]) -> tuple[dict, float | None]:
    """Per-component expenditure shares s_e and their concentration HHI (E22)."""

    present = [component for component in components if costs.get(component) is not None]
    total = sum(costs[component]["costUsd"] for component in present)
    if not present or total <= 0:
        return {}, None
    shares = {component: costs[component]["costUsd"] / total for component in present}
    return shares, sum(share * share for share in shares.values())
