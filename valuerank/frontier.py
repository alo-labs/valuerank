"""Pareto frontier of Artificial Analysis' "Intelligence Index vs. Cost to Run".

Points are dicts with ``intelligence`` (higher is better) and ``cost_usd``
(lower is better); extra keys are preserved on every returned copy.

Published near-Pareto policy: a plotted configuration is near the frontier
when its Intelligence Index is within 3 points (inclusive) of the rendered
frontier's intelligence at its cost.  The frontier's intelligence at cost
``c`` is the highest intelligence among frontier points with cost <= ``c``;
a point cheaper than every frontier point has no defined gap and is not
near.  The cost ratio (point cost over the cheapest frontier cost reaching
the point's intelligence) is reported for information only and is not a
criterion.  The threshold is the default of :func:`classify`.

CLI::

    python3 -m valuerank.frontier <capture.json> [--roster data/aa_mapping.json]
"""

import argparse
import json
import re

MAX_INTELLIGENCE_GAP = 3.0

_NUMBER = re.compile(r"^\$?\s*(\d[\d,]*(?:\.\d+)?)$")
_EFFORT = re.compile(r"^(.*?)\s*\(([^()]+)\)$")
_TIER_ORDER = {"frontier": 0, "near": 1}


def _key(point):
    return (point["intelligence"], point["cost_usd"])


def pareto_frontier(points):
    """Return the non-dominated points (cost ascending), each marked."""
    kept = []
    for p in points:
        i, c = _key(p)
        dominated = any(
            q["intelligence"] >= i and q["cost_usd"] <= c
            and (q["intelligence"] > i or q["cost_usd"] < c)
            for q in points
        )
        if not dominated:
            kept.append({**p, "frontier": True})
    return sorted(kept, key=lambda p: (p["cost_usd"], -p["intelligence"],
                                       str(p.get("name", ""))))


def frontier_gaps(points, frontier):
    """Attach ``intelligence_gap`` and ``cost_ratio`` to copies of points."""
    on_frontier = {_key(f) for f in frontier}
    result = []
    for p in points:
        i, c = _key(p)
        if _key(p) in on_frontier:
            result.append({**p, "intelligence_gap": 0, "cost_ratio": 1.0})
            continue
        best = [f["intelligence"] for f in frontier if f["cost_usd"] <= c]
        gap = max(0.0, max(best) - i) if best else None
        reach = [f["cost_usd"] for f in frontier if f["intelligence"] >= i]
        ratio = None
        if reach and min(reach) > 0:
            ratio = c / min(reach)
        result.append({**p, "intelligence_gap": gap, "cost_ratio": ratio})
    return result


def classify(points, *, max_intelligence_gap=MAX_INTELLIGENCE_GAP):
    """Add ``tier`` (frontier / near / dominated) to copies of points.

    Only the intelligence gap decides ``near``; ``cost_ratio`` is informative.
    """
    frontier = pareto_frontier(points)
    on_frontier = {_key(f) for f in frontier}
    result = []
    for p in frontier_gaps(points, frontier):
        if _key(p) in on_frontier:
            tier = "frontier"
        elif (p["intelligence_gap"] is not None
              and p["intelligence_gap"] <= max_intelligence_gap):
            tier = "near"
        else:
            tier = "dominated"
        result.append({**p, "frontier": tier == "frontier", "tier": tier})
    return result


def _best_rank(point):
    if point["tier"] == "frontier":
        return (-point["intelligence"], point["cost_usd"], point.get("name", ""))
    return (point["intelligence_gap"], point["cost_usd"], point.get("name", ""))


def family_selection(classified, roster_families):
    """Pick one best configuration per family that has a frontier/near point."""
    groups = {}
    for p in classified:
        groups.setdefault(p["family"], []).append(p)
    records = []
    for family, members in groups.items():
        for tier in ("frontier", "near"):
            candidates = [m for m in members if m["tier"] == tier]
            if candidates:
                best = min(candidates, key=_best_rank)
                break
        else:
            continue
        records.append({
            "family": family,
            "tier": tier,
            "configuration": best,
            "in_roster": family in roster_families,
            "other_configurations": [m["name"] for m in members
                                     if m is not best],
        })
    return sorted(records, key=lambda r: (
        _TIER_ORDER[r["tier"]], -r["configuration"]["intelligence"],
        r["family"]))


def _number_after(lines, index):
    if index + 1 >= len(lines):
        return None
    match = _NUMBER.match(lines[index + 1])
    return float(match.group(1).replace(",", "")) if match else None


def _find_line(lines, predicate):
    return next((n for n, line in enumerate(lines) if predicate(line)), None)


def parse_tooltip(text):
    """Parse chart tooltip text; None when intelligence or cost is missing.

    A trailing ``*`` on the model name marks an AA footnote: it is stripped
    from the name and the ``* ...`` footnote lines are returned as ``footnote``
    (None when absent).  "Click for more info" lines are ignored.
    """
    lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
    notes = [ln[2:].strip() for ln in lines if ln.startswith("* ")]
    lines = [ln for ln in lines
             if not ln.startswith("* ") and ln != "Click for more info"]
    if not lines:
        return None
    name = lines[0].rstrip("*").rstrip()
    rest = lines[1:]
    i_at = _find_line(rest, lambda ln: "Intelligence Index" in ln
                      and "Cost to Run" not in ln)
    c_at = _find_line(rest, lambda ln: "Cost to Run" in ln)
    if i_at is None or c_at is None:
        return None
    intelligence = _number_after(rest, i_at)
    cost = _number_after(rest, c_at)
    if intelligence is None or cost is None:
        return None
    match = _EFFORT.match(name)
    family, effort = (match.group(1), match.group(2)) if match else (name, None)
    return {"name": name, "family": family, "effort": effort,
            "intelligence": intelligence, "cost_usd": cost,
            "footnote": " ".join(notes) or None}


def _normalise(name):
    return " ".join(name.lower().replace("-", " ").split())


def main(argv=None):
    parser = argparse.ArgumentParser(prog="valuerank.frontier")
    parser.add_argument("capture")
    parser.add_argument("--roster")
    args = parser.parse_args(argv)
    with open(args.capture, encoding="utf-8") as fh:
        raw = json.load(fh)["points"]
    parsed, unparsed = [], []
    for item in raw:
        info = parse_tooltip(item["tip"])
        if info is None:
            unparsed.append(item)
        else:
            parsed.append({**item, **info})
    roster_names = set()
    if args.roster:
        with open(args.roster, encoding="utf-8") as fh:
            roster_names = {_normalise(r["displayName"]) for r in json.load(fh)}
    classified = classify(parsed)
    roster = {p["family"] for p in classified
              if _normalise(p["family"]) in roster_names}
    by_tier = {t: [p for p in classified if p["tier"] == t]
               for t in ("frontier", "near", "dominated")}
    report = {
        "frontier": sorted(by_tier["frontier"], key=lambda p: p["cost_usd"]),
        "near": by_tier["near"],
        "families": family_selection(classified, roster),
        "counts": {"total": len(classified),
                   **{t: len(v) for t, v in by_tier.items()},
                   "unparsed": len(unparsed)},
        "unparsed": unparsed,
    }
    print(json.dumps(report, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
