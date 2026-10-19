"""Interval outputs: definite/possible frontier and cheapest-above-a-bar, decided exactly (E21, E38, E43, E45, E50).

Under owner decision O25 the admissible set Theta protects the published record:
each evaluable row has an independent box (cost interval from reporting
precision; quality interval from reporting precision plus 0-100 domains for
missing leaves). With independent boxes the decisions reduce exactly to
corners (each row's inputs move only its own cost and quality, and dominance
and qualification are monotone in them). A bar's reference quality Q_r is a
variable shared by every qualification condition, so bar decisions solve for
it exactly over its interval (breakpoint reasoning on a one-dimensional affine
threshold). Problems with other shared factors are returned as "unresolved"
rather than approximated.

Every label carries a status: certified / disproved / unresolved / unevaluable.
"""

from __future__ import annotations

from dataclasses import dataclass

CERTIFIED = "certified"
DISPROVED = "disproved"
UNRESOLVED = "unresolved"
UNEVALUABLE = "unevaluable"


@dataclass(frozen=True)
class Box:
    """One evaluable row's admissible box: cost [c_low, c_high] (USD) and quality [q_low, q_high] (0-100)."""

    row: str
    c_low: float
    c_high: float
    q_low: float
    q_high: float
    provisional: bool = False

    def __post_init__(self):
        if not (0 < self.c_low <= self.c_high) or not (self.q_low <= self.q_high):
            raise ValueError(f"invalid admissible box for {self.row}")


def _dominates(c_j, q_j, c_i, q_i) -> bool:
    return c_j <= c_i and q_j >= q_i and (c_j < c_i or q_j > q_i)


def frontier(boxes: list[Box], *, shared_factors: tuple = ()) -> dict:
    """Definite and possible frontier membership for every row, with witnesses.

    PossibleFrontier(i): i at its best corner, every j at its worst; certified iff
    no j dominates there. DefiniteFrontier(i): disproved by i at its worst corner
    and some j at its best that dominates; certified otherwise.
    """

    results = {}
    for box in boxes:
        if shared_factors:
            results[box.row] = {"definite": UNRESOLVED, "possible": UNRESOLVED, "reason": "shared factors are not supported by this solver"}
            continue
        others = [other for other in boxes if other.row != box.row]
        blockers = [
            other.row for other in others if _dominates(other.c_high, other.q_low, box.c_low, box.q_high)
        ]
        dominators = [
            other.row for other in others if _dominates(other.c_low, other.q_high, box.c_high, box.q_low)
        ]
        results[box.row] = {
            "possible": DISPROVED if blockers else CERTIFIED,
            "possibleWitness": None if blockers else {"row": "best corner", "others": "worst corners"},
            "possibleBlockedBy": blockers,
            "definite": DISPROVED if dominators else CERTIFIED,
            "definiteCounterexample": dominators[0] if dominators else None,
        }
    return results


@dataclass(frozen=True)
class Affine:
    """A bound that is affine in one shared factor t: base + slope * t."""

    base: float
    slope: float = 0.0

    def at(self, t: float) -> float:
        return self.base + self.slope * t

    def range(self, low: float, high: float) -> tuple[float, float]:
        ends = (self.at(low), self.at(high))
        return min(ends), max(ends)


@dataclass(frozen=True)
class SharedBox:
    """A row whose box bounds depend affinely on one shared factor t (e.g. a common price list or donor multiple)."""

    row: str
    c_low: Affine
    c_high: Affine
    q_low: Affine
    q_high: Affine


def _search(test, low: float, high: float, depth: int) -> tuple[str, float | None]:
    """Certified interval bisection over t in [low, high].

    ``test(lo, hi)`` returns "all" when the condition holds for every t in the
    sub-interval, "none" when it holds for no t, and "some" otherwise. Returns
    ("found", witness), ("absent", None) or ("unresolved", None) at the depth limit.
    """

    verdict = test(low, high)
    if verdict == "all":
        return "found", (low + high) / 2.0
    if verdict == "none":
        return "absent", None
    if depth == 0:
        return "unresolved", None
    middle = (low + high) / 2.0
    left = _search(test, low, middle, depth - 1)
    if left[0] == "found":
        return left
    right = _search(test, middle, high, depth - 1)
    if right[0] == "found":
        return right
    return ("unresolved", None) if "unresolved" in (left[0], right[0]) else ("absent", None)


def _recheck(test, outcome: tuple[str, float | None]) -> tuple[str, float | None]:
    """Re-check a returned witness as a single point against the original condition (E43)."""

    status, point = outcome
    if status == "found" and test(point, point) != "all":
        return "unresolved", None
    return outcome


def _dominance_verdict(c_j, q_j, c_i, q_i) -> str:
    """Interval verdict for 'j dominates i' given ranges (min, max) of each coordinate over a sub-interval."""

    # Certainly dominates: worst case for j still dominates.
    if c_j[1] <= c_i[0] and q_j[0] >= q_i[1] and (c_j[1] < c_i[0] or q_j[0] > q_i[1]):
        return "all"
    # Certainly does not: j cannot be weakly better on both, or can only tie exactly.
    if c_j[0] > c_i[1] or q_j[1] < q_i[0] or (c_j[0] >= c_i[1] and q_j[1] <= q_i[0]):
        return "none"
    return "some"


def frontier_shared(boxes: list[SharedBox], t_low: float, t_high: float, *, depth: int = 30) -> dict:
    """Possible and definite frontier membership with one shared factor t in [t_low, t_high] (E43).

    PossibleFrontier(i): exists t with i at its best corner and every j at its
    worst, no j dominating. DefiniteFrontier(i): disproved by some t and j with i
    at its worst and j at its best, j dominating. Both are decided by certified
    bisection over t; an undecided search at the depth limit is "unresolved".
    """

    results = {}
    for box in boxes:
        others = [other for other in boxes if other.row != box.row]

        def none_dominates(lo, hi, box=box, others=others):
            verdicts = [
                _dominance_verdict(o.c_high.range(lo, hi), o.q_low.range(lo, hi), box.c_low.range(lo, hi), box.q_high.range(lo, hi))
                for o in others
            ]
            if all(v == "none" for v in verdicts):
                return "all"
            if any(v == "all" for v in verdicts):
                return "none"
            return "some"

        def some_dominates(lo, hi, box=box, others=others):
            verdicts = [
                _dominance_verdict(o.c_low.range(lo, hi), o.q_high.range(lo, hi), box.c_high.range(lo, hi), box.q_low.range(lo, hi))
                for o in others
            ]
            if any(v == "all" for v in verdicts):
                return "all"
            if all(v == "none" for v in verdicts):
                return "none"
            return "some"

        possible, witness = _recheck(none_dominates, _search(none_dominates, t_low, t_high, depth))
        dominated, counterexample = _recheck(some_dominates, _search(some_dominates, t_low, t_high, depth))
        results[box.row] = {
            "possible": {"found": CERTIFIED, "absent": DISPROVED, "unresolved": UNRESOLVED}[possible],
            "possibleWitnessT": witness,
            "definite": {"found": DISPROVED, "absent": CERTIFIED, "unresolved": UNRESOLVED}[dominated],
            "definiteCounterexampleT": counterexample,
        }
    return results


@dataclass(frozen=True)
class Reference:
    """A bar's reference-quality object (E52): its pinned row id and admissible quality interval."""

    row: str
    q_low: float
    q_high: float


def qualification(box: Box, reference: Reference) -> dict:
    """Confirmed / possible qualification against the reference (the reference always qualifies against itself)."""

    if box.row == reference.row:
        return {"confirmed": CERTIFIED, "possible": CERTIFIED}
    return {
        "confirmed": CERTIFIED if box.q_low >= reference.q_high else DISPROVED,
        "possible": CERTIFIED if box.q_high >= reference.q_low else DISPROVED,
    }


def _possibly_cheapest(box: Box, others: list[Box], reference: Reference) -> tuple[bool, float | None]:
    """Exact membership of K_r with a witness value of Q_r.

    For a fixed Q_r = t, i is best at its best corner and every j at its worst.
    i must qualify (t <= q_high(i), or i is the reference); every j that is
    surely cheaper than i's cheapest cost must fail to qualify (t > q_low(j));
    the reference itself, if it competes, always qualifies, so it must not be
    surely cheaper. The feasible t form an interval; the witness is its top.
    """

    upper = reference.q_high if box.row == reference.row else min(box.q_high, reference.q_high)
    lower_strict = None  # t must exceed this
    for other in others:
        if other.c_high >= box.c_low:
            continue  # i can be at least as cheap as this competitor
        if other.row == reference.row:
            return False, None  # the reference always qualifies and is surely cheaper
        lower_strict = other.q_low if lower_strict is None else max(lower_strict, other.q_low)
    if upper < reference.q_low:
        return False, None
    if lower_strict is not None and upper <= lower_strict:
        return False, None
    return True, upper


def cheapest_above_bar(boxes: list[Box], reference: Reference, *, shared_factors: tuple = ()) -> dict:
    """Qualification, the possible-cheapest set K_r and the confirmed unique cheapest for one bar.

    Confirmed cheapest (E38): i confirmed-qualifies, is not provisional, and its
    worst cost is strictly below the best cost of every other row that can
    possibly qualify (j != i). Ties never produce a unique label.
    """

    if shared_factors:
        return {"status": UNRESOLVED, "reason": "shared factors are not supported by this solver"}
    rows = {}
    members = []
    for box in boxes:
        others = [other for other in boxes if other.row != box.row]
        qualifies = qualification(box, reference)
        in_set, witness = _possibly_cheapest(box, others, reference)
        if in_set:
            members.append(box.row)
        rows[box.row] = {**qualifies, "possibleCheapest": CERTIFIED if in_set else DISPROVED, "witnessReferenceQuality": witness}
    confirmed = []
    for box in boxes:
        if rows[box.row]["confirmed"] != CERTIFIED or box.provisional:
            continue
        rivals = [other for other in boxes if other.row != box.row and rows[other.row]["possible"] == CERTIFIED]
        if all(box.c_high < other.c_low for other in rivals):
            confirmed.append(box.row)
    return {
        "status": CERTIFIED,
        "rows": rows,
        "possibleCheapest": members,
        "confirmedCheapest": confirmed[0] if confirmed else None,
    }
