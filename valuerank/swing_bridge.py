"""Score-swing attribution by replay (methodology v3, E177).

A release's score changes are decomposed by replaying the build from the two releases'
evidence bundles, one input class at a time in a declared order. Each row publishes every
step's change, the order-dependence term (forward minus reverse ordering) and the replay
residual (the replayed final score minus the published score). A change is attributed only
when the residual is within 1e-6 points and every step carrying more than 5 points names the
changed bundle fields behind it; rows ranked in only one release are listed as cohort
admissions or exits, never held by this gate.

The first step, "method and clock", scores the previous release's inputs with the current
code, anchors and release clock and compares them with the previous published scores. A
replay the current anchors cannot score (an admitted-workload change) is a versioned
migration, governed by its dual-run comparison (O12), not by this gate.
"""

from __future__ import annotations

import copy
from datetime import date

from valuerank import value_v3 as v

SWING_LIMIT = 5.0
RESIDUAL_TOLERANCE = 1e-6
PRICE_FIELDS = ("price1mInputTokens", "price1mOutputTokens", "cacheHitPrice", "cacheWritePrice")
TOKEN_FIELDS = ("intelligenceIndexEvaluations", "intelligenceIndexCost", "canonicalIntelligenceIndexTokenCount", "intelligenceIndexCostPerTask", "intelligenceIndexOutputTokensPerTask")
# Each data class: the snapshot page fields it owns ("*" = every field no other class owns) and its whole documents.
CLASSES = {
    "price": {"fields": PRICE_FIELDS, "documents": ("priceRecords",)},
    # O64: the reviewed manifest describes the agent capture, so the two change together.
    "tokenUse": {"fields": TOKEN_FIELDS, "documents": ("codingAgents", "codingAgentsManifest", "costCharts")},
    "benchmarkRecord": {"fields": "*", "documents": ("bugHunt", "bugHuntScoreboard", "tb4", "leafEvidence", "cognitionFrontierCode", "sweTracks")},
    "planEvidence": {"fields": (), "documents": ("planRoutes",)},
    "cohort": {"fields": (), "documents": ("configurationMap", "frontierCapture", "roster")},
}
ORDER = tuple(CLASSES)
METHOD_STEP = "method and clock"
CACHE_RATE_LABEL = "AA cache-rate update"
MIGRATION = "versioned migration: the current anchors cannot score this replay; the dual-run comparison governs (O12)"


def _classified(documents: dict) -> None:
    """Every evidence document belongs to exactly one class (the snapshot is split by field)."""

    owned = {key for spec in CLASSES.values() for key in spec["documents"]} | {"snapshot"}
    if set(documents) - owned:
        raise ValueError(f"unclassified evidence documents: {sorted(set(documents) - owned)}")


def _pages(documents: dict) -> dict:
    return {page["model"]["slug"]: page["model"] for page in documents["snapshot"]["pages"]}


def _owner(field: str) -> str:
    return next((name for name, spec in CLASSES.items() if spec["fields"] != "*" and field in spec["fields"]), "benchmarkRecord")


def apply_class(state: dict, current: dict, name: str) -> dict:
    """The state with one class's inputs taken from the current release (the cohort class also adds and drops pages)."""

    state = copy.deepcopy(state)
    spec = CLASSES[name]
    for key in spec["documents"]:
        if key in current["documents"]:
            state["documents"][key] = copy.deepcopy(current["documents"][key])
    pages, new_pages = _pages(state["documents"]), _pages(current["documents"])
    for slug, page in pages.items():
        if slug not in new_pages:
            continue
        for field in set(page) | set(new_pages[slug]):
            if _owner(field) != name:
                continue
            if field in new_pages[slug]:
                page[field] = copy.deepcopy(new_pages[slug][field])
            else:
                del page[field]
    if name == "cohort":
        state["configurations"] = copy.deepcopy(current["configurations"])
        kept = [page for page in state["documents"]["snapshot"]["pages"] if page["model"]["slug"] in new_pages]
        added = [copy.deepcopy(page) for page in current["documents"]["snapshot"]["pages"] if page["model"]["slug"] not in pages]
        state["documents"]["snapshot"]["pages"] = kept + added
    return state


def changed_fields(previous: dict, current: dict) -> dict:
    """Per class, the bundle fields that differ between the releases (artifact and locator)."""

    changes = {name: [] for name in ORDER}
    for name, spec in CLASSES.items():
        changes[name] += [key for key in spec["documents"] if previous["documents"].get(key) != current["documents"].get(key)]
    old_pages, new_pages = _pages(previous["documents"]), _pages(current["documents"])
    for slug in sorted(set(old_pages) & set(new_pages)):
        for field in sorted(set(old_pages[slug]) | set(new_pages[slug])):
            if old_pages[slug].get(field) != new_pages[slug].get(field):
                changes[_owner(field)].append(f"snapshot:pages[model.slug={slug}].model.{field}")
    changes["cohort"] += [f"snapshot:pages[model.slug={slug}]" for slug in sorted(set(old_pages) ^ set(new_pages))]
    if previous["configurations"] != current["configurations"]:
        changes["cohort"].append("configurations")
    return changes


def replay_values(state: dict, frozen: dict, release_day: date) -> dict:
    """Value scores per row and basis for one replay state, scored by the current code and anchors."""

    output = v.score(v.assemble(state["configurations"], state["documents"], release_day=release_day), frozen)
    return {row["id"]: {"api": row["api"]["value"], "plan": row["planScore"]["value"]} for row in output["rows"]}


def _steps(previous: dict, current: dict, frozen: dict, release_day: date, order: tuple) -> list[dict]:
    state, values = previous, replay_values(previous, frozen, release_day)
    trail = [values]
    for name in order:
        state = apply_class(state, current, name)
        trail.append(replay_values(state, frozen, release_day))
    return trail


def _difference(after, before):
    return None if after is None or before is None else after - before


def _cache_rate_rows(previous: dict, current: dict) -> set:
    """Rows whose token-use change is AA's cache rate alone: the cache-read cost moved with token totals and prices fixed."""

    rows = set()
    old_pages, new_pages = _pages(previous["documents"]), _pages(current["documents"])
    for slug in set(old_pages) & set(new_pages):
        old, new = old_pages[slug], new_pages[slug]
        totals = old.get("canonicalIntelligenceIndexTokenCount")
        fixed = bool(totals) and all(old.get(field) == new.get(field) for field in (*PRICE_FIELDS, "canonicalIntelligenceIndexTokenCount"))
        if fixed and (old.get("intelligenceIndexCost") or {}).get("cacheRead") != (new.get("intelligenceIndexCost") or {}).get("cacheRead"):
            rows.add(slug)
    return rows


def bridge(previous: dict, current: dict, frozen: dict, release_day: date) -> dict:
    """E177: the sequential replay bridge between two releases.

    Each release is {"configurations", "documents", "published": {row: {basis: value}}}; ``frozen`` and
    ``release_day`` are the current release's anchors and clock.
    """

    _classified(previous["documents"])
    _classified(current["documents"])
    try:
        forward = _steps(previous, current, frozen, release_day, ORDER)
        reverse = _steps(previous, current, frozen, release_day, tuple(reversed(ORDER)))
    except ValueError as error:
        if "workload migration" not in str(error):
            raise
        return {"status": MIGRATION, "rows": {}, "admissions": [], "exits": [], "changedFields": changed_fields(previous, current)}
    old_ids = {item["id"] for item in previous["configurations"]}
    new_ids = {item["id"] for item in current["configurations"]}
    fields = changed_fields(previous, current)
    slugs = {item["id"]: item["aaSlug"] for item in current["configurations"]}
    cache_rows = _cache_rate_rows(previous, current)
    rows = {}
    for row_id in sorted(old_ids & new_ids):
        entry = {}
        for basis in v.BASES:
            published_old, published_new = previous["published"][row_id][basis], current["published"][row_id][basis]
            steps = {METHOD_STEP: _difference(forward[0][row_id][basis], published_old)}
            backward = {}
            for index, name in enumerate(ORDER):
                steps[name] = _difference(forward[index + 1].get(row_id, {}).get(basis), forward[index].get(row_id, {}).get(basis))
                position = len(ORDER) - 1 - index
                backward[name] = _difference(reverse[position + 1].get(row_id, {}).get(basis), reverse[position].get(row_id, {}).get(basis))
            residual = _difference(forward[-1][row_id][basis], published_new)
            swing = _difference(published_new, published_old)
            carriers = [name for name in ORDER if steps[name] is not None and abs(steps[name]) > SWING_LIMIT]
            named = all(fields[name] for name in carriers)
            attributed = residual is not None and abs(residual) <= RESIDUAL_TOLERANCE and named
            entry[basis] = {
                "swing": swing,
                "steps": steps,
                "orderDependence": {name: _difference(steps[name], backward[name]) for name in ORDER},
                "replayResidual": residual,
                "attributed": attributed,
                "held": swing is not None and abs(swing) > SWING_LIMIT and not attributed,
                "tokenUseLabel": CACHE_RATE_LABEL if slugs[row_id] in cache_rows else "token use",
            }
        rows[row_id] = entry
    held = sorted(row_id for row_id, entry in rows.items() if any(item["held"] for item in entry.values()))
    return {
        "status": "held: unattributed score swing" if held else "passed",
        "order": [METHOD_STEP, *ORDER],
        "rows": rows,
        "held": held,
        "admissions": [{"row": row_id, "status": "cohort admission (no prior score)"} for row_id in sorted(new_ids - old_ids)],
        "exits": [{"row": row_id, "status": "cohort exit"} for row_id in sorted(old_ids - new_ids)],
        "changedFields": fields,
    }
