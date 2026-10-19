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
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field

SEMANTICS = ("fixed", "sliding", "session")
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


def unit_burn(window: Window, demand: dict) -> float:
    """Budget units one workload unit consumes in this window: sum_k a_wk x_k (unlisted categories burn nothing)."""

    return sum(window.burn.get(category, 0.0) * tokens for category, tokens in demand.items())


def _instance(window: Window, step: int) -> int:
    return (step - window.phase) // window.length


def greedy_schedule(windows: list[Window], demand: dict, horizon: int, *, step_limit: float = math.inf) -> list[float]:
    """The earliest-possible schedule: at each step consume the most every window still allows."""

    burns = [unit_burn(window, demand) for window in windows]
    schedule = []
    used_fixed = [dict() for _ in windows]
    session_start = [None for _ in windows]
    session_used = [0.0 for _ in windows]
    for step in range(horizon):
        allowance = step_limit
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


def capacity(windows: list[Window], demand: dict, horizon: int, *, grid_minutes: int, step_limit: float = math.inf) -> dict:
    """Token-equivalent capacity in workload units: verified lower bound, relaxed upper bound and certification."""

    schedule = greedy_schedule(windows, demand, horizon, step_limit=step_limit)
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


def value_multiple(units: float, api_cost_per_unit: float, gross_cash: float) -> float | None:
    """M = API-priced capacity / gross cash paid for the fee period (gross-cash convention)."""

    if gross_cash <= 0:
        return None
    return units * api_cost_per_unit / gross_cash
