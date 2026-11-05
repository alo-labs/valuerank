"""Version history and rank changes from ``data/ranking_history_v1.5.json`` plus the current release.

``build_changelog(history, current, names)`` returns the ``changelog.json`` document, newest first. Each version
carries ``ranks`` ({slug: rank}, API basis, only models with a record) next to its ``rankChanges``; slugs are the
model id with dots replaced by hyphens.
``model_history(history, current, model_id)`` returns one model's ``history`` list for ``models/<slug>.json``.

``history`` is the ranking-history document (keys ``v150``, ``v190`` ... map model id to a rank).
``current`` describes the published release: ``version``, ``dateIso``, ``dateHuman``, ``modelCount``,
``dimensionCount`` and ``ranks`` (model id -> ``{"api", "plan"}`` for ranked models only).

Historic ranks predate the plan basis, so they are recorded as API-basis ranks (``plan`` is ``null``)
and rank changes between consecutive versions compare API-basis ranks. A version that has no record for
a model contributes nothing for it: ranks and dates are never inferred. Only dates documented in
``VERSION_DATES`` are shown; every other historic date is ``null``.
"""

from __future__ import annotations

import datetime as dt
import re

# Release dates that are stated in the repository (the v1.5.0 page header; v2.0.0's valuerank/release.py); all others are unknown.
VERSION_DATES = {"v1.5.0": "2026-09-06", "v2.0.0": "2026-10-19"}

_KEY = re.compile(r"^v(\d)(\d)(\d)$")


def slugify(model_id: str) -> str:
    return model_id.replace(".", "-")


def _label(key: str) -> str:
    major, minor, patch = _KEY.match(key).groups()
    return f"v{major}.{minor}.{patch}"


def _human(iso: str | None) -> str | None:
    if iso is None:
        return None
    day = dt.date.fromisoformat(iso)
    return f"{day:%B} {day.day}, {day.year}"


def _records(history: dict) -> list[tuple[str, dict[str, int]]]:
    keys = sorted(key for key in history if _KEY.match(key))
    return [(_label(key), history[key]) for key in keys]


def _snapshots(history: dict, current: dict) -> list[dict]:
    snapshots = [
        {"version": label, "dateIso": VERSION_DATES.get(label), "ranks": dict(ranks), "models": len(ranks), "dimensions": None}
        for label, ranks in _records(history)
    ]
    snapshots.append(
        {
            "version": current["version"],
            "dateIso": current["dateIso"],
            # A configuration without a cost has no value score and no rank (AGENTS.md), so it is left out.
            "ranks": {model_id: ranks["api"] for model_id, ranks in current["ranks"].items() if ranks["api"] is not None},
            "models": current["modelCount"],
            "dimensions": current["dimensionCount"],
        }
    )
    return snapshots


def _summary(snapshot: dict, names: dict) -> str:
    ranks = snapshot["ranks"]
    if not ranks:
        return "No model is ranked in this release record."
    top = min(ranks, key=lambda model_id: (ranks[model_id], model_id))
    name = names.get(top, top)
    count = len(ranks)
    plural = "" if count == 1 else "s"
    if snapshot["dimensions"] is None:
        return f"{count} model{plural} ranked; {name} first."
    return f"{count} model{plural} ranked on {snapshot['dimensions']} dimensions; {name} is first on the API basis."


def build_changelog(history: dict, current: dict, names: dict) -> dict:
    snapshots = _snapshots(history, current)
    versions = []
    previous: dict[str, int] = {}
    for snapshot in snapshots:
        ranks = snapshot["ranks"]
        changes = sorted(
            (
                {"slug": slugify(model_id), "name": names.get(model_id, model_id), "from": previous[model_id], "to": rank}
                for model_id, rank in ranks.items()
                if model_id in previous and previous[model_id] != rank
            ),
            key=lambda change: (change["to"], change["name"]),
        )
        versions.append(
            {
                "version": snapshot["version"],
                "date": _human(snapshot["dateIso"]),
                "models": snapshot["models"],
                "dimensions": snapshot["dimensions"],
                "summary": _summary(snapshot, names),
                "rankChanges": changes,
                "ranks": {slugify(model_id): rank for model_id, rank in sorted(ranks.items())},
                "added": sorted(slugify(model_id) for model_id in set(ranks) - set(previous)) if previous else [],
                "removed": sorted(slugify(model_id) for model_id in set(previous) - set(ranks)),
            }
        )
        previous = ranks
    return {"versions": versions[::-1]}


def model_history(history: dict, current: dict, model_id: str) -> list[dict]:
    entries = [
        {"version": label, "date": VERSION_DATES.get(label), "rank": {"api": ranks[model_id], "plan": None}}
        for label, ranks in _records(history)
        if model_id in ranks
    ]
    if model_id in current["ranks"]:
        entries.append({"version": current["version"], "date": current["dateIso"], "rank": dict(current["ranks"][model_id])})
    return entries
