"""Published diagnostics: rank agreement, matched cost, workload cross-check, weights and exposure.

Everything here is descriptive: no diagnostic changes a score. Rank
statistics are computed on an explicitly named common panel (E65), and
undefined results (too few rows, no rank variation) are reported as such.
"""

from __future__ import annotations

import hashlib
import json

import random
import statistics

CROSSCHECK_MIN_ROWS = 8
CROSSCHECK_WARN_TAU = 0.5
MATCHED_RATIO_LIMIT = 1.5
MATCHED_RANK_GAP = 3
NON_DISCRIMINATING_SD = 3.0


def kendall_tau_b(xs: list[float], ys: list[float]) -> float | None:
    """Kendall's tau-b; None when either variable has no variation or fewer than two pairs."""

    if len(xs) != len(ys):
        raise ValueError("tau-b needs paired values")
    concordant = discordant = ties_x = ties_y = 0
    n = len(xs)
    for i in range(n):
        for j in range(i + 1, n):
            dx, dy = xs[i] - xs[j], ys[i] - ys[j]
            if dx == 0 and dy == 0:
                continue
            if dx == 0:
                ties_x += 1
            elif dy == 0:
                ties_y += 1
            elif (dx > 0) == (dy > 0):
                concordant += 1
            else:
                discordant += 1
    denominator = ((concordant + discordant + ties_x) * (concordant + discordant + ties_y)) ** 0.5
    return (concordant - discordant) / denominator if denominator else None


def bootstrap_tau(xs: list[float], ys: list[float], *, draws: int = 2000, seed: int = 20261019) -> tuple[float, float] | None:
    """A model-row bootstrap 95% interval for tau-b (labelled matched-panel sensitivity)."""

    rng = random.Random(seed)
    n = len(xs)
    values = []
    for _ in range(draws):
        picks = [rng.randrange(n) for _ in range(n)]
        tau = kendall_tau_b([xs[k] for k in picks], [ys[k] for k in picks])
        if tau is not None:
            values.append(tau)
    if not values:
        return None
    values.sort()
    return values[int(0.025 * (len(values) - 1))], values[int(0.975 * (len(values) - 1))]


def agreement(first: dict, second: dict, *, label: str, min_rows: int = 3) -> dict:
    """Tau-b between two scores on their common panel, with the panel and a bootstrap interval."""

    panel = sorted(row for row in first if row in second and first[row] is not None and second[row] is not None)
    excluded = sorted((set(first) | set(second)) - set(panel))
    if len(panel) < min_rows:
        return {"label": label, "panel": panel, "excluded": excluded, "tau": None, "interval": None, "status": "undefined (panel too small)"}
    xs, ys = [first[row] for row in panel], [second[row] for row in panel]
    tau = kendall_tau_b(xs, ys)
    return {
        "label": label,
        "panel": panel,
        "excluded": excluded,
        "tau": tau,
        "interval": bootstrap_tau(xs, ys) if tau is not None else None,
        "status": "defined" if tau is not None else "undefined (no rank variation)",
    }


def workload_crosscheck(cost_per_solve: dict, basket_cost: dict, *, label: str) -> dict:
    """E41: tau-b between basket-cost rank and cost per solved task, suppressed below 8 rows; warn below 0.5."""

    result = agreement(cost_per_solve, basket_cost, label=label, min_rows=CROSSCHECK_MIN_ROWS)
    tau, interval = result["tau"], result["interval"]
    if tau is None:
        result["warning"] = None
    elif tau < CROSSCHECK_WARN_TAU:
        result["warning"] = "low agreement"
    elif interval is not None and interval[0] < CROSSCHECK_WARN_TAU:
        result["warning"] = "uncertain agreement"
    else:
        result["warning"] = None
    return result


def cost_per_solve(cost_per_attempted_task: float | None, resolved_fraction: float | None) -> float | None:
    """Mean cost per attempted task / resolved fraction from one execution (E68); infinite when nothing resolved."""

    if cost_per_attempted_task is None or resolved_fraction is None:
        return None
    return float("inf") if resolved_fraction == 0 else cost_per_attempted_task / resolved_fraction


def competition_ranks(values: dict, *, lower_is_better: bool) -> dict:
    ordered = sorted(values.values(), reverse=not lower_is_better)
    return {row: 1 + sum(1 for other in ordered if (other < value if lower_is_better else other > value)) for row, value in values.items()}


def matched_cost(family_costs: dict, weights: dict) -> float | None:
    """C^match = sum over execution families of omega_g * one-pass cost (E24/E55); None unless every family is priced."""

    if any(family_costs.get(family) is None for family in weights):
        return None
    total_weight = sum(weights.values())
    return sum(weights[family] / total_weight * family_costs[family] for family in weights)


def diagnostic_object(weights: dict, leaf_map: dict, price_rule: str, panel_rule: str) -> dict:
    """E103: the matched-cost diagnostic as a versioned object D with an identity hash."""

    payload = {
        "families": sorted(weights),
        "weights": {family: weights[family] for family in sorted(weights)},
        "leafToFamily": {leaf: leaf_map[leaf] for leaf in sorted(leaf_map)},
        "priceRule": price_rule,
        "panelRule": panel_rule,
    }
    identity = hashlib.sha256(json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()).hexdigest()[:16]
    return {"id": identity, **payload}


def matched_cost_bridge(old: dict, new: dict, old_costs: dict, new_costs: dict) -> dict:
    """E103: old/new bridge on the common evidenced panel, separating cost-data from composition changes.

    For each row: dataRefresh = C(old D, new costs) - C(old D, old costs) and
    composition = C(new D, new costs) - C(old D, new costs).
    """

    rows = {}
    for row in sorted(set(old_costs) & set(new_costs)):
        before = matched_cost(old_costs[row], old["weights"])
        refreshed = matched_cost(new_costs[row], old["weights"])
        after = matched_cost(new_costs[row], new["weights"])
        if None in (before, refreshed, after):
            continue
        rows[row] = {"old": before, "new": after, "dataRefresh": refreshed - before, "composition": after - refreshed}
    return {"oldId": old["id"], "newId": new["id"], "sameObject": old["id"] == new["id"], "panel": sorted(rows), "rows": rows}


def matched_cost_warnings(matched: dict, basket: dict) -> dict:
    """Cost-shape warnings on the common panel: pairwise reversals and the ratio/rank rule (diagnostic only)."""

    panel = sorted(row for row in matched if matched[row] is not None and basket.get(row) is not None)
    if len(panel) < 2:
        return {"panel": panel, "warnings": {}}
    ratios = {row: matched[row] / basket[row] for row in panel}
    median = statistics.median(ratios.values())
    matched_rank = competition_ranks({row: matched[row] for row in panel}, lower_is_better=True)
    basket_rank = competition_ranks({row: basket[row] for row in panel}, lower_is_better=True)
    warnings = {}
    for row in panel:
        relative = ratios[row] / median
        reversals = sorted(
            other for other in panel if other != row
            and (matched[row] - matched[other]) * (basket[row] - basket[other]) < 0
        )
        ratio_flag = (relative > MATCHED_RATIO_LIMIT or relative < 1 / MATCHED_RATIO_LIMIT) and abs(matched_rank[row] - basket_rank[row]) > MATCHED_RANK_GAP
        warnings[row] = {"relativeRatio": relative, "reversals": reversals, "ratioRankWarning": ratio_flag}
    return {"panel": panel, "warnings": warnings}


def effective_weights(z_by_leaf: dict, weights: dict) -> dict:
    """w_i * SD(z_i), normalised over leaves with at least two observed values."""

    raw = {}
    for leaf, values in z_by_leaf.items():
        observed = [value for value in values if value is not None]
        if len(observed) >= 2:
            raw[leaf] = weights[leaf] * statistics.pstdev(observed)
    total = sum(raw.values())
    return {leaf: value / total for leaf, value in raw.items()} if total else {}


def non_discriminating(z_by_leaf: dict) -> list:
    """Leaves whose cohort SD(z) is below 3 points (still scored; excluded from drift-flag counting)."""

    result = []
    for leaf, values in z_by_leaf.items():
        observed = [value for value in values if value is not None]
        if len(observed) >= 2 and statistics.pstdev(observed) < NON_DISCRIMINATING_SD:
            result.append(leaf)
    return sorted(result)


def exposure(leaf_attributes: dict, weights: dict, attribute: str) -> dict:
    """Share of nominal quality weight by one provenance attribute (E57)."""

    totals: dict[str, float] = {}
    for leaf, attributes in leaf_attributes.items():
        key = attributes[attribute]
        totals[key] = totals.get(key, 0.0) + weights[leaf]
    grand = sum(totals.values())
    return {key: value / grand for key, value in sorted(totals.items())}


def paired_rank_change(baseline: dict, branch: dict, *, higher_is_better: bool = True) -> dict:
    """Rank changes on the common evaluable panel of two runs (E65)."""

    panel = sorted(row for row in baseline if row in branch and baseline[row] is not None and branch[row] is not None)
    base_rank = competition_ranks({row: baseline[row] for row in panel}, lower_is_better=not higher_is_better)
    branch_rank = competition_ranks({row: branch[row] for row in panel}, lower_is_better=not higher_is_better)
    changes = {row: branch_rank[row] - base_rank[row] for row in panel}
    worst = max(panel, key=lambda row: (abs(changes[row]), row)) if panel else None
    return {
        "panel": panel,
        "excluded": sorted((set(baseline) | set(branch)) - set(panel)),
        "changes": changes,
        "maxAbsChange": abs(changes[worst]) if worst else None,
        "maxRow": worst,
    }
