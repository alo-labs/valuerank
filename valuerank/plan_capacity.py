"""Plan capacity under simultaneous usage windows (E30, E39, E56, E69).

The scored Plan target is token-equivalent capacity: the most API-priced
consumption a plan admits over its fee period under every evidenced window.
Time is a grid of steps; each window w has a length, a budget B_w and burn
coefficients a_wk (budget units per token of category k), so one unit of the
workload's demand vector x costs sum_k a_wk x_k of that window's budget.

Window semantics are encoded as recorded: fixed-reset windows (instances start
at a phase and repeat), sliding windows (every run of `length` consecutive
steps), and session-anchored windows (a session starts at the first consuming
step after the previous one ends). Consumption is divisible (E69).

The lower bound is a verified feasible schedule built greedily as early as
possible (sessions therefore run back to back). The upper bound is a valid
relaxation: in every window family, ceil(horizon / length) disjoint instances
cover the horizon, so total consumption cannot exceed that many budgets, nor
the per-step throughput limit times the horizon. A point capacity is certified
only when the bounds coincide; otherwise the interval is reported.

Demand objects carry units (E94): tokens per deployment-equivalent task, per
component pass (task multiplicity times the per-task vector, or an evidenced
component-pass vector) and per complete workload pass (the sum over the
workload's components). Capacity accepts only a workload-pass demand, so
capacity is counted in complete workload passes per fee period.
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field

SEMANTICS = ("fixed", "sliding", "session")
DEMAND_UNITS = ("per-task", "component-pass", "workload-pass")
TOLERANCE = 1e-9


@dataclass(frozen=True)
class Window:
    name: str
    length: int  # steps
    budget: float  # budget units per window instance
    semantics: str
    phase: int = 0  # fixed-reset offset in steps
    burn: dict = field(default_factory=dict)  # category -> budget units per token

    def __post_init__(self):
        if self.semantics not in SEMANTICS or self.length <= 0 or self.budget < 0:
            raise ValueError(f"invalid window {self.name}")


@dataclass(frozen=True)
class Demand:
    """A category-token vector with its unit: per-task, component-pass or workload-pass (E94)."""

    tokens: dict
    unit: str
    component: str | None = None

    def __post_init__(self):
        if self.unit not in DEMAND_UNITS:
            raise ValueError(f"unknown demand unit: {self.unit}")


def component_pass(per_task: Demand, multiplicity: int) -> Demand:
    """d_ie = n_e * t_ie: one pass over a component's tasks."""

    if per_task.unit != "per-task":
        raise ValueError(f"a component pass is built from a per-task vector, not {per_task.unit}")
    return Demand({category: multiplicity * tokens for category, tokens in per_task.tokens.items()}, "component-pass", per_task.component)


def workload_pass(components: list[Demand]) -> Demand:
    """d_iW = sum over the workload's components of d_ie, one complete workload pass."""

    totals: dict = {}
    for demand in components:
        if demand.unit != "component-pass":
            raise ValueError(f"a workload pass sums component-pass vectors, not {demand.unit}")
        for category, tokens in demand.tokens.items():
            totals[category] = totals.get(category, 0.0) + tokens
    return Demand(totals, "workload-pass")


def priced(demand: Demand, prices: dict) -> float:
    """p . d in USD (prices per token by category); reconciles to the scored cost at the same unit."""

    return sum(prices[category] * tokens for category, tokens in demand.tokens.items())


def unit_burn(window: Window, demand: dict) -> float:
    """Budget units one workload unit consumes in this window: sum_k a_wk x_k (unlisted categories burn nothing)."""

    return sum(window.burn.get(category, 0.0) * tokens for category, tokens in demand.items())


def _instance(window: Window, step: int) -> int:
    return (step - window.phase) // window.length


def greedy_schedule(windows: list[Window], demand: dict, horizon: int, *, step_limit: float = math.inf, available: set | None = None) -> list[float]:
    """The earliest-possible schedule: at each step consume the most every window still allows.

    ``available`` (E117) restricts consumption to the calendar's available steps (y_t = 0 elsewhere).
    """

    burns = [unit_burn(window, demand) for window in windows]
    schedule = []
    used_fixed = [dict() for _ in windows]
    session_start = [None for _ in windows]
    session_used = [0.0 for _ in windows]
    for step in range(horizon):
        allowance = step_limit if available is None or step in available else 0.0
        for index, (window, burn) in enumerate(zip(windows, burns)):
            if burn <= 0:
                continue
            if window.semantics == "fixed":
                remaining = window.budget - used_fixed[index].get(_instance(window, step), 0.0)
            elif window.semantics == "sliding":
                recent = schedule[max(0, step - window.length + 1):step]
                remaining = window.budget - burn * sum(recent)
            else:
                start = session_start[index]
                active = start is not None and step < start + window.length
                remaining = window.budget - (session_used[index] if active else 0.0)
            allowance = min(allowance, max(0.0, remaining) / burn)
        amount = 0.0 if allowance == math.inf else allowance
        schedule.append(amount)
        for index, (window, burn) in enumerate(zip(windows, burns)):
            if amount <= 0 or burn <= 0:
                continue
            if window.semantics == "fixed":
                key = _instance(window, step)
                used_fixed[index][key] = used_fixed[index].get(key, 0.0) + burn * amount
            elif window.semantics == "session":
                start = session_start[index]
                if start is None or step >= start + window.length:
                    session_start[index], session_used[index] = step, 0.0
                session_used[index] += burn * amount
    return schedule


def verify_schedule(schedule: list[float], windows: list[Window], demand: dict, *, step_limit: float = math.inf) -> bool:
    """True when the schedule respects every window under its recorded semantics and the step limit."""

    if any(amount < -TOLERANCE or amount > step_limit + TOLERANCE for amount in schedule):
        return False
    for window in windows:
        burn = unit_burn(window, demand)
        if burn <= 0:
            continue
        if window.semantics == "fixed":
            totals: dict[int, float] = {}
            for step, amount in enumerate(schedule):
                totals[_instance(window, step)] = totals.get(_instance(window, step), 0.0) + burn * amount
            if any(total > window.budget + TOLERANCE for total in totals.values()):
                return False
        elif window.semantics == "sliding":
            for end in range(len(schedule)):
                if burn * sum(schedule[max(0, end - window.length + 1):end + 1]) > window.budget + TOLERANCE:
                    return False
        else:
            start, used = None, 0.0
            for step, amount in enumerate(schedule):
                if amount <= 0:
                    continue
                if start is None or step >= start + window.length:
                    start, used = step, 0.0
                used += burn * amount
                if used > window.budget + TOLERANCE:
                    return False
    return True


def instance_count(window: Window, horizon: int) -> int:
    """How many window instances can hold consumption within the horizon.

    Fixed windows: every instance index that a step of the horizon falls in
    (a misaligned phase adds a partial instance). Sliding and session windows:
    ceil(horizon / length), since that many disjoint blocks of `length` steps
    cover the horizon and sessions cannot overlap.
    """

    if window.semantics == "fixed":
        return _instance(window, horizon - 1) - _instance(window, 0) + 1
    return math.ceil(horizon / window.length)


def relaxed_upper_bound(windows: list[Window], demand: dict, horizon: int, *, step_limit: float = math.inf) -> float:
    """A valid upper bound: per window family, its instance count times its budget; and the throughput limit."""

    bound = step_limit * horizon
    for window in windows:
        burn = unit_burn(window, demand)
        if burn > 0:
            bound = min(bound, instance_count(window, horizon) * window.budget / burn)
    return bound


def capacity(windows: list[Window], workload: Demand, horizon: int, *, grid_minutes: int, step_limit: float = math.inf, available: set | None = None) -> dict:
    """Token-equivalent capacity in complete workload passes: verified lower bound, relaxed upper bound, certification."""

    if workload.unit != "workload-pass":
        raise ValueError(f"capacity needs a workload-pass demand, not {workload.unit}")
    demand = workload.tokens
    schedule = greedy_schedule(windows, demand, horizon, step_limit=step_limit, available=available)
    # Only a schedule re-verified against the recorded semantics may serve as the lower bound.
    verified = verify_schedule(schedule, windows, demand, step_limit=step_limit)
    lower = sum(schedule) if verified else None
    upper = relaxed_upper_bound(windows, demand, horizon, step_limit=step_limit)
    bounded = upper != math.inf
    return {
        "status": "verified" if verified else "unresolved",
        "feasibleLowerBound": lower,
        "relaxedUpperBound": upper if bounded else None,
        "capacityBoundedness": "bounded" if bounded else "unbounded",
        "gridResolutionMinutes": grid_minutes,
        "optimalityScope": "grid schedule with recorded window semantics",
        "pointCertified": verified and bounded and abs(upper - lower) <= TOLERANCE * max(1.0, upper),
        "schedule": schedule if verified else None,
    }


EXCLUDED_POLICY_ROLES = {"evaluation-repetition", "platform-overhead"}


def numerator_treatment(record: dict) -> str:
    """E75/E97: included / excluded / bounded for one measured execution record, never by task outcome.

    Delivered, policy-permitted execution counts whether the task passed or failed
    and includes model-generated refusals and policy-permitted retries, matching
    the API basket's support; transport errors and requests rejected before
    execution deliver nothing and are excluded; consumption that cannot be
    separated from excluded overhead is carried as a bound.
    """

    if record.get("tokenObservability") == "inseparable":
        return "bounded"
    if record.get("requestDeliveryStatus") != "delivered" or record.get("deploymentPolicyRole") in EXCLUDED_POLICY_ROLES:
        return "excluded"
    return "included"


def capacity_across_semantics(window_sets: dict, workload: Demand, horizon: int, *, grid_minutes: int, step_limit: float = math.inf) -> dict:
    """E115: capacity across the publicly admissible window mechanisms S_r of a route.

    The true mechanism is one of S_r, so min over s of the verified lower bounds is
    a valid lower bound and max over s of the relaxed upper bounds a valid upper
    bound; a point is identified only when they coincide. A mechanism without a
    verified lower bound or a finite upper bound leaves that side unestablished.
    """

    results = {name: capacity(windows, workload, horizon, grid_minutes=grid_minutes, step_limit=step_limit) for name, windows in sorted(window_sets.items())}
    lowers = [result["feasibleLowerBound"] for result in results.values()]
    uppers = [result["relaxedUpperBound"] for result in results.values()]
    lower = None if None in lowers else min(lowers)
    upper = None if None in uppers else max(uppers)
    point = lower is not None and upper is not None and abs(upper - lower) <= TOLERANCE * max(1.0, upper)
    if point:
        status = "identified across semantics"
    elif lower is not None and upper is not None:
        status = "bounded across semantics"
    else:
        status = "semantics unresolved; conservative achievable capacity only"
    return {"semantics": results, "lowerBound": lower, "upperBound": upper, "pointIdentified": point, "status": status}


def certified_multiple_bounds(capacity_result: dict, api_cost_per_unit: float, payment: dict) -> dict:
    """E105: M_W bounds from capacity bounds, converted directly only under fixed positive gross cash.

    ``payment`` is {"rule": "fixed", "grossCashUsd": F0}, or another rule with an
    optional ``certificate`` {"multipleLower", "multipleUpper"} computed at the
    consumption-optimal, minimum-cash solution (M* = U*/F*). Capacity bounds of an
    arbitrary feasible schedule never bound M* when cash depends on consumption,
    so without a certificate M_W stays unidentified. One-sided or non-positive
    bounds are unidentified (E67).
    """

    if payment.get("rule") == "fixed":
        cash = payment.get("grossCashUsd") or 0.0
        lower_units, upper_units = capacity_result.get("feasibleLowerBound"), capacity_result.get("relaxedUpperBound")
        if cash <= 0 or lower_units is None or upper_units is None:
            return {"identification": "unidentified", "lower": None, "upper": None, "derivation": "fixed cash: capacity bounds unavailable"}
        lower, upper = lower_units * api_cost_per_unit / cash, upper_units * api_cost_per_unit / cash
        derivation = "fixed positive gross cash: capacity bounds / F0"
        point = capacity_result.get("pointCertified") is True
    else:
        certificate = payment.get("certificate") or {}
        lower, upper = certificate.get("multipleLower"), certificate.get("multipleUpper")
        if lower is None or upper is None:
            return {"identification": "unidentified", "lower": None, "upper": None, "derivation": "consumption-dependent payment without a lexicographic certificate"}
        derivation = "certified at the consumption-optimal, minimum-cash solution"
        point = lower == upper
    if not 0 < lower <= upper < math.inf:
        return {"identification": "unidentified", "lower": None, "upper": None, "derivation": "bounds not strictly positive and finite"}
    return {"identification": "point-identified" if point else "set-identified", "lower": lower, "upper": upper, "derivation": derivation}


def value_multiple(units: float, api_cost_per_unit: float, gross_cash: float) -> float | None:
    """M = API-priced capacity / gross cash paid for the fee period (gross-cash convention)."""

    if gross_cash <= 0:
        return None
    return units * api_cost_per_unit / gross_cash
