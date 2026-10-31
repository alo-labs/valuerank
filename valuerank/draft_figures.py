#!/usr/bin/env python3
"""Draft figures (editor decision E265): the methodology draft never copies a "today" figure by hand.

The draft is written as a source file, ``draft-rNNN.src.md``, whose current-release figures are placeholders resolved
from the build: ``{{max:PATH|FORMAT}}`` and ``{{aicd:PATH|FORMAT}}`` read a ranking's v3 section of
``data/scores.json``, ``{{top:PATH|FORMAT}}`` reads the file's root, and ``{{fig:NAME}}`` reads a named figure of the
figures manifest (``data/figures.json``, both rankings, rebuilt with the docs). ``render`` writes the published
``draft-rNNN.md`` from its source; ``check`` fails when the newest draft differs from its rendering, when a
placeholder does not resolve, or when a sentence that speaks of today still carries an unmarked number. A sentence that
says a source publishes or carries no such field carries an ``{{absent:KEY}}`` marker (rendered as nothing) whose claim
is tested against the pinned data (I60 M2). A stale figure that a reviewer finds after this is a bug in the check, not
in the draft.

    python3 -m valuerank.draft_figures manifest  # write data/figures.json (run by `npm run build:docs`)
    python3 -m valuerank.draft_figures render    # (re)write the newest draft from its source
    python3 -m valuerank.draft_figures check     # verify it (run by the tests and by `npm run verify:docs`)
"""

from __future__ import annotations

import json
import math
import re
import sys
from datetime import date, timedelta
from pathlib import Path

from valuerank import exact_match
from valuerank import plan_admission
from valuerank import plan_routes as pr
from valuerank import quality as q
from valuerank import value_v3
from valuerank.paths import DATA, ROOT

SPEC_DIR = ROOT / "research" / "2026-10-19-methodology-codesign"
MANIFEST = "figures.json"
PLACEHOLDER = re.compile(r"\{\{(?P<scope>max|aicd|common|top|fig|name|absent):(?P<path>[^|}]+)(?:\|(?P<fmt>[^}]+))?\}\}")
_TOKEN = re.compile(r'\[(?P<bracket>[^\]]+)\]|(?P<key>[^.\[\]]+)')
DRAFT = re.compile(r"draft-r(?P<number>\d+)\.src\.md$")


class FigureError(ValueError):
    """A placeholder that does not resolve or format."""


def resolve(document, path: str):
    """``a.b[id=x].c[0]["0.3"]``: dict keys, list indices and ``[field=value]`` selectors over lists of dicts."""

    value = document
    for match in _TOKEN.finditer(path):
        token = match.group("key") if match.group("key") is not None else match.group("bracket")
        if match.group("bracket") is not None and "=" in token and not token.startswith('"'):
            field, wanted = token.split("=", 1)
            found = [item for item in value if isinstance(item, dict) and str(item.get(field)) == wanted]
            if len(found) != 1:
                raise FigureError(f"{path}: {len(found)} items with {field}={wanted}")
            value = found[0]
        elif match.group("bracket") is not None and token.isdigit():
            value = value[int(token)]
        else:
            key = token.strip('"')
            if not isinstance(value, dict) or key not in value:
                raise FigureError(f"{path}: no key {key!r}")
            value = value[key]
    return value


def series(values: list[str]) -> str:
    """``a``, ``a and b``, ``a, b and c``; ``none`` for an empty list."""

    if not values:
        return "none"
    return " and ".join([", ".join(values[:-1]), values[-1]]) if len(values) > 1 else values[0]


def display_names(scores: dict) -> dict:
    """Configuration id -> "Name (effort)", the draft's way of naming a configuration."""

    names = {}
    for model in scores["models"]:
        suffix = f" ({model['aaVariant']})" if model.get("aaVariant") else ""
        names[model["id"]] = model["name"] if model["name"].endswith(suffix) else model["name"] + suffix
    return names


def fmt(value, spec: str | None, names: dict) -> str:
    """Format one resolved value. ``.Nf``, ``,.Nf``, ``pct.N``, ``int``, ``count``, ``name``, ``names``, ``usd.N``,
    ``range`` (a two-item rank band), ``signed.N`` and ``str``; without a spec, a string or integer is printed as it is."""

    if spec is None:
        if isinstance(value, bool) or not isinstance(value, (str, int)):
            raise FigureError(f"value {value!r} needs a format")
        return str(value)
    if spec == "count":
        return str(len(value))
    if spec == "name":
        return names[value]
    if spec == "names":
        return series([names[item] for item in value])
    if spec == "list":
        return series([str(item) for item in value])
    if spec == "str":
        return str(value)
    if spec == "range":
        low, high = value
        return str(low) if low == high else f"{low}–{high}"
    if not isinstance(value, (int, float)) or isinstance(value, bool):
        raise FigureError(f"value {value!r} is not a number for format {spec}")
    if spec == "int":
        return str(int(round(value)))
    if spec.startswith("pct."):
        return f"{value * 100:.{int(spec[4:])}f}%"
    if spec.startswith("usd."):
        return f"${value:,.{int(spec[4:])}f}"
    if spec.startswith("signed."):
        return f"{value:+.{int(spec[7:])}f}".replace("-", "−")
    if spec.startswith(",.") and spec.endswith("f"):
        return f"{value:,.{int(spec[2:-1])}f}"
    if spec.startswith(".") and spec.endswith("f"):
        return f"{value:.{int(spec[1:-1])}f}"
    raise FigureError(f"unknown format {spec!r}")


def named_figures(scores: dict, data: Path = DATA) -> dict:
    """The figures manifest: named figures for both rankings and the external facts the draft states (E265)."""

    capture = json.loads((data / "aa_frontier_capture.json").read_text())
    tracks = json.loads((data / "swe_tracks.json").read_text())
    figures = {
        "cohort.plotted": len(capture["frontier"]) + len(capture["near_frontier"]),
        "cohort.frontier": len(capture["frontier"]),
        "cohort.near": len(capture["near_frontier"]),
        "cohort.families": len({item["family"] for item in capture["frontier"] + capture["near_frontier"]}),
        "cohort.frontierFamilies": len({item["family"] for item in capture["frontier"]}),
        "cohort.nearOnlyFamilies": len({item["family"] for item in capture["near_frontier"]} - {item["family"] for item in capture["frontier"]}),
        "aa.plottedPoints": capture["universe"]["plotted_models_with_both_coordinates"],
        "aa.catalog": capture["universe"]["catalog_models"],
        "aa.capturedAt": capture["captured_at"],
        # E204: the first vertex of the rendered path and whether it is the cheapest plotted point.
        "aa.firstVertex": min(capture["frontier"], key=lambda item: item["total_cost_usd"])["model_name"],
        "aa.firstVertexCost": f"{min(item['total_cost_usd'] for item in capture['frontier']):,.2f}",
        "aa.cheapestPlottedCost": f"{min(item['total_cost_usd'] for item in capture['points']):,.2f}",
        # E195: rendered-frontier points whose rounded tooltip Index ties (I44 L3).
        "aa.frontierIndexTies": "; ".join(
            f"{series(sorted(item['model_name'] for item in capture['frontier'] if item['intelligence_index_display'] == index))} "
        f"{'both' if sum(1 for item in capture['frontier'] if item['intelligence_index_display'] == index) == 2 else 'all'} display {index}"
            for index in sorted({item["intelligence_index_display"] for item in capture["frontier"]})
            if sum(1 for item in capture["frontier"] if item["intelligence_index_display"] == index) > 1) or "none",
    }
    for track in q.TRACKS:
        section = scores["v3"] if track == q.DEFAULT_TRACK else scores["v3Tracks"][track]
        with q.active_track(track):
            for leaf in q.LEAVES:
                figures[f"{track}.weight.{leaf.key}"] = f"{leaf.weight:g}"
            shares = q.source_shares()
            figures[f"{track}.share.aa"] = f"{shares['aa'] * 100:.0f}%"
            figures[f"{track}.share.independent"] = f"{shares['independent'] * 100:.0f}%"
        figures.update(plan_band_figures(track, section, display_names(scores)))
        figures[f"{track}.ranked"] = len(section["rows"])
        figures[f"{track}.codingShare"] = f"{q.coding_specific_share(q.TRACKS[track]):.0f}"  # O122
        # I61 L7, O72: plan rows priced at API cost because their provider has no authorised or admitted route.
        fallback = [row for row in section["planRows"] if row["id"].endswith("@api")]
        figures[f"{track}.planRows"] = len(section["planRows"])
        figures[f"{track}.planFallbackRows"] = len(fallback)
        # I64 L5: plan rows whose selected route carries a lifecycle flag, or whose valuation basis is unverified.
        figures[f"{track}.planFlaggedRows"] = sum(bool({"possibly-superseded", "expired"} & set(row.get("flags", []))) for row in section["planRows"])
        # I78 L4: plan rows resting on a measurement in an acknowledged fault window (O91, O92).
        figures[f"{track}.planFaultRows"] = sum(pr.FAULT_FLAG in row.get("flags", []) for row in section["planRows"])
        figures[f"{track}.planUnverifiedRows"] = sum("valuation basis unverified" in row.get("flags", []) for row in section["planRows"])
        # I71: plan rows per owner-assumption kind, and every kind named from the one registry.
        kinds = {kind: sum(1 for row in section["planRows"] if row.get("grade") == "assumption" and (row.get("assumptionKind") or "transfer") == kind)
                 for kind in pr.OWNER_ASSUMPTIONS}
        figures[f"{track}.planAssumedRows"] = sum(kinds.values())
        figures[f"{track}.planAssumedKinds"] = pr.assumption_counts_text(kinds)
        names_of = display_names(scores)
        figures[f"{track}.planFallbackNames"] = series([names_of.get(row["id"].split("@")[0], row["id"].split("@")[0]) for row in fallback]) or "none"
        figures[f"{track}.listed"] = len(section["listedIndicative"])
        figures[f"{track}.planRows"] = len(section["planRows"])
    # O91, O92: the controlled measurements an acknowledged fault window flags, named.
    registry = json.loads((data / "plan_cost_routes.json").read_text()) if (data / "plan_cost_routes.json").exists() else {"routes": []}
    faults = ((registry.get("evidencePolicy") or {}).get("reportEligibilityProfile") or {}).get("accountingFaultDays") or []
    faulted = sorted(route["id"] for route in registry["routes"] if pr.in_fault_window(route, faults))
    figures["evidence.faultedRoutes"] = (f"{len(faulted)} route{'s' if len(faulted) != 1 else ''}: " + ", ".join(faulted)) if faulted else "none"
    figures["evidence.assumptionKinds"] = pr.assumption_kinds_text()
    figures["evidence.assumptionKindsPlural"] = pr.assumption_kinds_text("and", plural=True)
    for leaf, source in tracks["sources"].items():
        figures[f"source.{leaf}.records"] = sum(1 for record in tracks["records"] if record["leaf"] == leaf)
        figures[f"source.{leaf}.capturedAt"] = source["capturedAt"]
        figures[f"source.{leaf}.updated"] = source["updated"]
    # O46: the MiMo quota-ceiling multiples per Token Plan tier, read from the route registry.
    routes = json.loads((data / "plan_cost_routes.json").read_text())["routes"]
    for model_id in ("mimo-v2-6-pro", "mimo-v2-6-flash"):
        ceilings = [route for route in routes if route["id"].endswith("-quota-ceiling") and route.get("modelIds") == [model_id]]
        figures[f"mimoCeilings.{model_id}"] = " / ".join(f"{route['valueMultiple']:g}" for route in ceilings)
        figures[f"mimoCeilings.tiers"] = " / ".join(route["plan"].replace("MiMo Token Plan ", "") for route in ceilings)
    # I58 L2: the documented effort equivalents for AA's effort-less configurations, read from the two registries.
    equivalents = {**{key: sorted(value[0]) for key, value in exact_match.EFFORT_EQUIVALENTS.items()},
                   **{key: sorted({*exact_match.EFFORT_EQUIVALENTS.get(key, ((),))[0], effort}) for key, effort in value_v3.OWNER_STATED_EFFORT.items()}}
    cohort_ids = {model["id"] for model in scores["models"] if model.get("aaFrontierTier")}
    names_by_id = display_names(scores)
    figures["effortEquivalents"] = series([f"{names_by_id[key]} at {' or '.join(value)}" for key, value in sorted(equivalents.items())
                                           if key in cohort_ids]) or "none"
    figures["release.cutoff"] = scores["observedAt"]
    # I58 M2: the sources captured after the cutoff, read from the published clocks (O60).
    cutoff = scores["observedAt"]
    late = sorted({clock["source"].split(":")[0].split(" (")[0] if ":" in clock["source"] else clock["source"]
                   for clock in scores["v3"].get("sourceClocks", []) if "T" in clock["capturedAt"] and clock["capturedAt"] > cutoff})
    figures["sourceClocks.afterCutoff"] = series(late) or "none"
    figures.update(registry_figures(capture, json.loads((data / "plan_cost_routes.json").read_text()), release_day(scores)))
    names = display_names(scores)
    family = {model["id"]: model.get("family") or model["name"] for model in scores["models"]}
    sections = {track: scores["v3"] if track == q.DEFAULT_TRACK else scores["v3Tracks"][track] for track in q.TRACKS}
    ranked = {track: [row["id"] for row in section["rows"]] for track, section in sections.items()}
    order = lambda ids: series([names[item] for item in sorted(ids, key=lambda item: names[item])])
    for track, ids in ranked.items():
        section, weights = sections[track], {leaf.key: leaf.weight for leaf in q.TRACKS[track]}
        figures[f"{track}.rankedFamilies"] = len({family[item] for item in ids})
        # E234: rows with a leaf filled by another party, and listed rows whose indicative cost score clips (I35 L5).
        figures[f"{track}.gapFills"] = order(section["diagnostics"]["gapFillSensitivity"]["rows"])
        figures[f"{track}.indicativeClipped"] = order(item["id"] for item in section["listedIndicative"] if item["api"]["costScore"] in (0.0, 100.0))
        figures[f"{track}.indicativeClipped.plan"] = order(item["id"] for item in section["listedIndicative"] if item["plan"]["costScore"] in (0.0, 100.0))
        main = [row["id"] for row in section["rows"] if row["cost"]["workload"] == section["mainWorkload"]]
        figures[f"{track}.mainWorkloadRows"] = len(main)
        figures[f"{track}.subsetRows"] = order(item for item in ids if item not in main)
        figures[f"{track}.admissionThreshold"] = -(-2 * len(ids) // 3)  # E140: ceil(2N/3)
        components = section["admission"]["components"]
        figures[f"{track}.basket.admitted"] = sum(1 for item in components.values() if item["admitted"])
        figures[f"{track}.basket.target"] = len(components)
        # O58: listed rows beyond the anchors, per basis, with the factor, the side and the markers the gate output carries.
        for basis in ("api", "plan"):
            items = [item for item in section["gates"]["listedBeyondAnchors"] if item["basis"] == basis]
            figures[f"{track}.beyondAnchors.{basis}"] = "; ".join(
                f"{names[item['id']]} {item['factor']:.2f} {'below the low' if item['side'].startswith('below') else 'above the high'} anchor"
                + (" (" + ", ".join(mark for mark, on in (("rendered-frontier point", item["renderedFrontier"]), ("past the factor-2 limit", item["beyondFactorLimit"])) if on) + ")"
                   if item["renderedFrontier"] or item["beyondFactorLimit"] else "")
                for item in sorted(items, key=lambda item: -item["factor"])) or "none"
        # E114: flagged quality groups and non-discriminating leaves.
        drift = section["diagnostics"]["groupDrift"]
        group_labels = {"swe": "software engineering", "professional": "professional work", "reliability": "reliability", "knowledge": "knowledge"}
        figures[f"{track}.driftFlags"] = series([f"the {group_labels[key]} group (spread share {group['spreadShare'] * 100:.1f}% against a nominal "
                                                 f"{group['nominalShare'] * 100:.1f}%)" for key, group in drift.get("groups", {}).items() if group["flag"]])
        figures[f"{track}.nonDiscriminating"] = series([q.ALL_LEAVES[key].label for key in section["diagnostics"]["nonDiscriminatingLeaves"]])
    # O69: rows dated on the cutoff's day, placed before the cutoff by the board's relative age, disclosed.
    figures["cutoffDayRows"] = series([f"{names.get(record['modelId'], record['modelId'])} on {tracks['sources'][record['leaf']]['publisher'].split(' (')[0]}"
                                       for record in tracks["records"] if record.get("cutoffDayRow")]) or "none"
    # I50 M2: configurations a board lists twice, with the row the selection rule chose.
    tracks_records = [record for record in tracks["records"] if record.get("alternates")]
    figures["duplicateRows"] = series([f"{names.get(record['modelId'], record['modelId'])} on {tracks['sources'][record['leaf']]['publisher'].split(' (')[0]} "
                                       f"({record['harness']} chosen over {series([item['harness'] for item in record['alternates']])} by "
                                       f"{record['selection'].split('chosen by ')[1].split(' (')[0]})" for record in tracks_records]) or "none"
    # I53 M2: each subset-workload stratum's panel and the status its cost-influence statistics read.
    labels = {"max": "the max-effort ranking", "aicd": "the AI Coding Daily ranking", "common": "the common-leaf diagnostic ranking"}
    strata = [f"{labels.get(track, track)}'s {len(item['panel'])}-row {basis.upper() if basis == 'api' else 'Plan'} subset stratum reads \"{item['status']}\""
              for track, section in sections.items() for basis in ("api", "plan")
              for item in section["costInfluence"][basis].get("subsetStrata", {}).values()]
    figures["subsetStrata"] = series(strata) if strata else "no ranking has a subset stratum"
    # E234: whether every frozen bar keeps its displayed-record row with the fills published, removed and lowered.
    changed = [f"{track} {basis} {item['bar'].removeprefix('bar:')}" for track, section in sections.items()
               for basis, items in section["diagnostics"]["gapFillBars"]["bases"].items() for item in items if not item["survives"]]
    figures["gapFillBars"] = ("every bar of every ranking keeps its row in all three" if not changed
                              else "a bar's row changes at " + series(changed))
    both = set(ranked["max"]) & set(ranked["aicd"])
    figures["both.names"], figures["both.count"] = order(both), len(both)
    figures["rankedAny"] = len(set(ranked["max"]) | set(ranked["aicd"]))
    excluded = {item["id"] for item in sections["max"]["incompleteEvidence"]} & {item["id"] for item in sections["aicd"]["incompleteEvidence"]}
    figures["excluded"], figures["excluded.names"] = len(excluded), order(excluded)
    # O121: how many configurations neither leading ranking ranks that the diagnostic ranking does.
    common_only = set(ranked["common"]) - set(ranked["max"]) - set(ranked["aicd"])
    figures["commonOnly"], figures["commonOnly.names"] = len(common_only), order(common_only)
    # I53 L3: the leaves outside both rankings' added sets that excluded configurations lack, grouped by leaf set.
    added = {leaf.key for track in q.TRACKS for leaf in q.TRACKS[track]} - {leaf.key for leaf in q.COMMON_LEAVES} - {"frontierCode", "terminalBench", "bugHunt"}
    missing = {item["id"]: tuple(sorted(set(item["missing"]) - added)) for item in sections["max"]["incompleteEvidence"] if item["id"] in excluded}
    groups = {}
    for item_id, keys in missing.items():
        if keys:
            groups.setdefault(keys, []).append(item_id)
    figures["excluded.missingCore"] = "; ".join(
        f"{order(ids)} {'lacks' if len(ids) == 1 else 'lack'} {series([q.ALL_LEAVES[key].label for key in keys])}" for keys, ids in sorted(groups.items())) or "none"
    figures.update(family_figures(scores, excluded, order))
    return {key: str(value) for key, value in sorted(figures.items())}


def registry_figures(capture: dict, plan_document: dict, release: str) -> dict:
    """I50 L5: the current release's registry facts (report window, search cutoff, evidence stages, vertex checks), so
    the draft states them as placeholders even in a sentence that also carries a past date."""

    policy = plan_document["evidencePolicy"]
    window, cutoff = policy["reportingWindow"], policy["searchCutoff"]
    figures = {"evidence.windowStart": window["start"], "evidence.windowEnd": window["end"], "evidence.searchCutoff": cutoff,
               "evidence.searchGapDays": (date.fromisoformat(release) - date.fromisoformat(cutoff)).days}
    # I89 L1: each flagged measurement's label and blocking dates (O107, O110, O111), from the registry, grouped by date pair.
    groups: dict[tuple, list[str]] = {}
    for route in plan_document["routes"]:
        if route.get("changeDetectedOn") and route.get("valueMultipleKind") in pr.CONTROLLED_KINDS:
            blocking = route["blockingChangeOn"] if "blockingChangeOn" in route else route["changeDetectedOn"]
            groups.setdefault((route["changeDetectedOn"], blocking), []).append(f"{route['plan']} ({route.get('sourceModel')})")
    figures["evidence.changeDates"] = "; ".join([
        f"{series(sorted(set(names)))} possibly superseded from {label}" + (f", blocking from {blocking}" if blocking and blocking != label else "" if blocking else ", blocking nothing")
        for (label, blocking), names in sorted(groups.items())]) or "none"  # groups joined by semicolons, names within by series
    # I65 L4: the partition splits the build applies (O83), from the registry.
    records = plan_admission.profile_records(policy.get("reportEligibilityProfile") or {})
    splits = plan_admission.splitting(records)
    # I90 L3: in date order.
    figures["evidence.partitionSplits"] = series([f"{item['provider']} at {item['date']}" for item in sorted(splits, key=lambda item: item["date"])]) or "none"
    figures["evidence.meterResets"] = series([f"{item['provider']} at {item['date']}" for item in sorted(records, key=lambda item: item["date"]) if item.get("type") == "reset"]) or "none"
    # O99: metering-only announcements are logged but split nothing.
    figures["evidence.meteringAnnouncements"] = series([f"{item['provider']} at {item['date']}" for item in records if item.get("type") == "metering"]) or "none"
    # I61 L3: the stages and providers of the search that sets the cutoff, from its log entry.
    latest = max((entry for entry in policy.get("searchLog") or [] if entry.get("searchedOn") == cutoff and not entry.get("singleProvider")),
                 key=lambda entry: len(entry.get("stages") or []), default={})
    stages = [stage["stage"] for stage in latest.get("stages") or []]
    figures.update({"evidence.searchStageCount": len(stages) or 1, "evidence.searchStages": series(stages) or "plain web search",
                    "evidence.searchProviders": series([name for name in latest.get("providers") or [] if name != "DeepSeek"]) or "the providers logged"})
    reports = [route for route in plan_document["routes"] if route.get("valueMultipleKind") in pr.REPORT_KINDS]
    figures["evidence.reportDates"] = series([route.get("reportDate") or route["sourcePublicationDate"] for route in reports]) or "none"
    figures["evidence.reportRoutes"] = series([f"{route['plan']}, dated {route.get('reportDate') or route['sourcePublicationDate']}" for route in reports]) or "none"
    # E144: the SemiAnalysis measurement's lifecycle stages, from its observation date and the expiry constants.
    published = {route["sourcePublicationDate"] for route in plan_document["routes"]
                 if route.get("sourceEvidenceId") == "semianalysis" and route.get("valueMultipleKind") == "controlled_account_workload_projection"}
    if len(published) != 1:
        raise FigureError(f"expected one SemiAnalysis observation date, found {sorted(published)}")
    observed = date.fromisoformat(published.pop())
    figures.update({"semianalysis.observed": observed.isoformat(),
                    "semianalysis.lastCurrent": (observed + timedelta(pr.SOFT_EXPIRY_DAYS)).isoformat(),
                    "semianalysis.supersededFrom": (observed + timedelta(pr.SOFT_EXPIRY_DAYS + 1)).isoformat(),
                    "semianalysis.expiredFrom": (observed + timedelta(pr.HARD_EXPIRY_DAYS + 1)).isoformat(),
                    "semianalysis.demotedFrom": (observed + timedelta(pr.HARD_EXPIRY_DAYS + pr.GRACE_DAYS + 1)).isoformat()})
    # E195: the rendered path's vertices against the frontier circles, and the comparison with the previous capture.
    numbers = [float(item) for item in re.findall(r"-?\d+(?:\.\d+)?", capture["rendered_pareto_svg_path"])]
    vertices = list(zip(numbers[0::2], numbers[1::2]))
    worst = max(min(math.dist(vertex, (item["svg_x"], item["svg_y"])) for item in capture["frontier"]) for vertex in vertices)
    comparison = capture["comparison_to_previous_capture"]
    changes = [f"{name} entered" for name in comparison["added"]] + [f"{name} left" for name in comparison["removed"]]
    figures.update({"aa.vertices": len(vertices), "aa.vertexMatchPx": f"{worst:.1f}".rstrip("0").rstrip("."),
                    "aa.previousCapture": comparison["previous_capture_date"],
                    "aa.vertexChanges": series(changes) if changes else "no vertex entered or left"})
    return figures


def family_figures(scores: dict, excluded: set, order) -> dict:
    """E193/E251: family primaries and the other plotted points, by tier and Index gap, as the build records them."""

    cohort = [model for model in scores["models"] if model.get("aaFrontierTier")]
    family = lambda model: model.get("family") or model["name"]
    frontier_families = {family(model) for model in cohort if model["aaFrontierTier"] == "frontier"}
    primary = {family(model): model for model in cohort if model.get("familyPrimary")}

    def by_gap(models):
        gaps = sorted({model["aaFrontierIntelligenceGap"] for model in models})
        return ", ".join(f"{order(model['id'] for model in models if model['aaFrontierIntelligenceGap'] == gap)} at gap {gap}" for gap in gaps) or "none"

    near_families = [model for model in cohort if family(model) not in frontier_families]
    frontier_near = [model for model in cohort if family(model) in frontier_families and model["aaFrontierTier"] == "near"]
    # I58 M1: the excluded configurations fall into exactly one of five classes, checked as a partition.
    classes = {
        "frontierPrimaries": [m["id"] for m in cohort if m["id"] in excluded and m.get("familyPrimary") and family(m) in frontier_families],
        "nearPrimaries": [m["id"] for m in cohort if m["id"] in excluded and m.get("familyPrimary") and family(m) not in frontier_families],
        "nearPoints": [m["id"] for m in frontier_near if m["id"] in excluded and not m.get("familyPrimary")],
        "frontierPoints": [m["id"] for m in cohort if m["id"] in excluded and not m.get("familyPrimary") and m["aaFrontierTier"] == "frontier"],
        "nearFamilyPoints": [m["id"] for m in near_families if m["id"] in excluded and not m.get("familyPrimary")],
    }
    placed = [item for ids in classes.values() for item in ids]
    if sorted(placed) != sorted(excluded) or len(set(placed)) != len(placed):
        raise FigureError(f"the excluded configurations do not partition into the five classes: {sorted(set(excluded) ^ set(placed))}")
    return {
        "near.primaries": by_gap([model for model in near_families if model.get("familyPrimary")]),
        "near.others": by_gap([model for model in near_families if not model.get("familyPrimary")]),
        "frontierFamilies.nearPoints": order(model["id"] for model in frontier_near),
        "frontierFamilies.dearerNearPoints": order(model["id"] for model in frontier_near
                                                   if model["aaEvalCost"] > primary[family(model)]["aaEvalCost"]),
        **{f"excluded.{name}": order(ids) for name, ids in classes.items()},
    }


def plan_band_figures(track: str, section: dict, names: dict) -> dict:
    """O42/E248: configurations whose plan rows fall in more than one Plan band, and those whose plan rows span more
    than the Plan separation threshold (the case E248's invariant is stated for)."""

    separability = section["diagnostics"]["rankSeparability"]
    bands, threshold = separability["plan"]["bands"], separability["plan"]["medianSeparation"]
    by_configuration: dict[str, list[dict]] = {}
    for row in section["planRows"]:
        by_configuration.setdefault(row["configurationId"], []).append(row)
    straddle = [key for key, rows in by_configuration.items() if len({tuple(bands[row["id"]]) for row in rows if row["id"] in bands}) > 1]
    values = {key: [row["value"] for row in rows if row["value"] is not None] for key, rows in by_configuration.items()}
    span = [key for key, found in values.items() if found and max(found) - min(found) > threshold]
    ordered = lambda keys: series([names[key] for key in sorted(keys, key=lambda key: names[key])])
    return {f"{track}.planBandStraddlers": ordered(straddle), f"{track}.planSpanBeyondThreshold": ordered(span)}


def write_manifest(scores: dict, data: Path = DATA) -> dict:
    manifest = named_figures(scores, data)
    (data / MANIFEST).write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n")
    return manifest


def render(text: str, scores: dict, manifest: dict) -> str:
    """Replace every placeholder; a placeholder that does not resolve raises FigureError."""

    names = display_names(scores)
    scopes = {"max": scores["v3"], "aicd": scores["v3Tracks"]["aicd"], "common": scores["v3Tracks"]["common"], "top": scores}

    def replace(match: re.Match) -> str:
        scope, path, spec = match.group("scope"), match.group("path").strip(), match.group("fmt")
        if scope == "name":
            # I52 L6: a configuration named in a sentence about the current release is rendered from its id.
            if path not in names:
                raise FigureError(f"no configuration {path!r}")
            return names[path]
        if scope == "absent":
            # I60 M2: the marker names a registered absence claim; check() tests the claim against the data.
            if path not in ABSENCE_CLAIMS:
                raise FigureError(f"no absence claim {path!r}")
            return ""
        if scope == "fig":
            if path not in manifest:
                raise FigureError(f"no named figure {path!r}")
            return manifest[path]
        try:
            return fmt(resolve(scopes[scope], path), spec, names)
        except (KeyError, IndexError, TypeError) as error:
            raise FigureError(f"{scope}:{path}: {error}") from error

    return PLACEHOLDER.sub(replace, text)


# A "today" sentence may still hold numbers that are not current-release figures: names, versions, decision tags, dates
# and the rule constants below. Everything else must be a placeholder.
RULE_CONSTANTS = ("above 100%", "more than 5 points", "within 3 points", "n = 8 rows", "Pro $100", "Pro $200", "Pro $500", "of 60 points", "> 5 points", "40 of the 100", "n = 60", "n = 6", "÷ 60", "÷ √6", "±26 Elo", "1/0.75", "carries 75%", "below 3 points", "> 0", "under 40%", "290 ×", "× 290", "290 required", "the 290", "⌈2N/3⌉", "10⁻⁶", "0–100", "0 or 100", "correlations 0, 0.3 and 0.6", "correlation 0", "sum to 1", "25% cost", "the 25% weight", "1.96", "√2", "0.75", "0.25",
                  "factor-2", "factor of 2", "tolerance 0.5 px", "two-thirds", "30 days", "7 days", "45 days", "0.5 W_g", "1.5 W_g")
_NOT_A_FIGURE = re.compile(
    r"\b[OEIL]\d+\b|\br\d+\b|\b\d{4}-\d{2}-\d{2}(T\d{2}:\d{2}:\d{2}Z)?\b|\b\d{2}:\d{2}(:\d{2})?Z\b"
    r"|\bversion \d+\b|\bv\d+(\.\d+)*\b|\b[A-Z][\w.-]*-\d[\w.]*\b|\bS\d[A-Z]?\b|`[^`]*`|\[[^\]]*\]\([^)]*\)"
)
_NUMBER = re.compile(r"(?<![\w.])\d[\d,]*(\.\d+)?%?")
HISTORY_HEADING = "## Revision history"
_COUNT = re.compile(r"\b\d+ (?:of (?:the )?|against )\d+\b")
# A number counting cohort things, or a dollar amount, states the current release (I43 M1, L1) unless dated or a fixture.
_COUNTED = re.compile(r"(?<![\w.])\d[\d,]*(?:\.\d+)? (?:(?:cohort|ranked|plotted|scored|main-workload|full-basket|near|frontier|plan) )*"
                      r"(?:configurations?|rows?|references|families|points|leaves|components|vertices|plan rows)\b|\$\d[\d,]*(?:\.\d+)?")
_FIXTURE = re.compile(r"[Ff]ixture|test vector|e\.g\.|for example")
_SENTENCE = re.compile(r"(?<=[.;])\s+(?=[A-Z*(])")


def known_names(scores: dict, data: Path = DATA) -> list[str]:
    """Names that contain digits (models, families, plans, benchmarks), longest first so a longer name is removed first."""

    names = set(display_names(scores).values()) | {model["name"] for model in scores["models"]}
    names |= {model.get("family") for model in scores["models"] if model.get("family")}
    names |= {leaf.label for leaf in q.ALL_LEAVES.values()}
    routes = json.loads((data / "plan_cost_routes.json").read_text())
    names |= {route["plan"] for route in routes["routes"] if route.get("plan")}
    names |= {"LiveBench 2.0", "Terminal-Bench 4.0", "FrontierCode 1.1", "Vibe Code Bench v1.1", "Code Migration v1.1", "Bug Hunt Bench",
              "Coding Agent Index v2.0", "Intelligence Index v4.3.2", "AA-LCR v1.1", "Max 5x", "Max 20x", "Pro 500"}
    return sorted((name for name in names if name and re.search(r"\d", name)), key=len, reverse=True)


def configuration_names(scores: dict) -> list[str]:
    """Effort-qualified configuration names ("Name (effort)"), which a 'today' sentence may only state as a placeholder."""

    return sorted((name for name in display_names(scores).values() if name.endswith(")")), key=len, reverse=True)


def dated(sentence: str, release_day: str | None) -> bool:
    """A sentence is history when it carries a date before the release day (outside code spans and bold rule labels, which
    date a decision, not a figure) or says "at O<n>"; a date on the release day itself is today."""

    text = re.sub(r"`[^`]*`|\*\*[^*]*\*\*", "", sentence)
    if re.search(r"\bat O\d+\b", text):
        return True
    return any(release_day is None or found < release_day for found in re.findall(r"\b\d{4}-\d{2}-\d{2}\b", text))


# I72 L1: an enumeration of Plan evidence classes naming transfers beside fallbacks, ceilings or measured routes.
ASSUMPTION_LIST = re.compile(r"owner-named transfers?(?:,| and| or| /)[^.;]{0,80}(?:fallback|ceiling|measured route)|(?:fallback|ceiling|measured routes?)[^.;]{0,80}(?:,| and| or| /) owner-named transfers?"
                             r"|\btransfers (?:and|or) (?:API[- ]?(?:cost )?)?fallbacks")
ASSUMPTION_NAMED = re.compile(r"owner assumption|evidence\.assumptionKinds|O88")


def lint(source: str, names: list[str], configurations: list[str] = (), release_day: str | None = None) -> list[str]:
    """Numbers and configuration names left unmarked in a sentence that speaks of today."""

    problems = []
    for line_number, line in enumerate(source.splitlines(), 1):
        if line.startswith(HISTORY_HEADING):
            break  # the revision history records past drafts' figures as they were
        for sentence in _SENTENCE.split(line):
            # I72 L1: a hand-typed list of Plan evidence that names owner-named transfers beside another evidence class
            # must name every owner-assumption kind (generated, or as "owner assumptions"), so a new kind cannot be missed.
            if ASSUMPTION_LIST.search(sentence) and not ASSUMPTION_NAMED.search(sentence):
                problems.append(f"line {line_number}: owner-named transfers listed without the other owner-assumption kinds: {sentence[:160]}")
            # A count "N of M" states the current release unless the sentence dates it, whether or not it says today.
            if not dated(sentence, release_day):
                routed = [name for name in configurations if re.search(re.escape(name) + r" on (?:[A-Z][\w$.]*(?: [\w$.]+){0,3}|API-cost fallback)", PLACEHOLDER.sub("", sentence))]
                if routed:
                    problems.append(f"line {line_number}: unmarked configuration route(s) {', '.join(routed)} in an undated sentence: {sentence[:160]}")
                undated = PLACEHOLDER.sub("", sentence)
                for constant in RULE_CONSTANTS:
                    undated = undated.replace(constant, "")
                counts = [match.group(0) for match in _COUNT.finditer(undated)]
                # A name with digits ("Claude Haiku 5.5 rows") is not a count of rows.
                for name in names:
                    undated = undated.replace(name, "")
                if not _FIXTURE.search(sentence):
                    counts += [match.group(0) for match in _COUNTED.finditer(_NOT_A_FIGURE.sub("", undated))]
                if counts:
                    problems.append(f"line {line_number}: unmarked count(s) {', '.join(counts)} in an undated sentence: {sentence[:160]}")
                # I52 L6: an effort-qualified configuration name in an undated sentence states the current release.
                plain = PLACEHOLDER.sub("", sentence)
                named = [name for name in configurations if name in plain]
                if named and not _FIXTURE.search(sentence) and not re.search(r"\b[Tt]oday\b", sentence):
                    problems.append(f"line {line_number}: unmarked configuration name(s) {', '.join(named)} in an undated sentence: {sentence[:160]}")
            if not re.search(r"\b[Tt]oday\b", sentence):
                continue
            text = PLACEHOLDER.sub("", sentence)
            named = [name for name in configurations if name in text]
            for name in named:
                text = text.replace(name, "")
            if named:
                problems.append(f"line {line_number}: unmarked configuration name(s) {', '.join(named)} in a 'today' sentence: {sentence[:160]}")
            for name in names:
                text = text.replace(name, "")
            for constant in RULE_CONSTANTS:
                text = text.replace(constant, "")
            text = _NOT_A_FIGURE.sub("", text)
            found = [match.group(0) for match in _NUMBER.finditer(text)]
            if found:
                problems.append(f"line {line_number}: unmarked figure(s) {', '.join(found)} in a 'today' sentence: {sentence[:160]}")
    return problems


def release_day(scores: dict) -> str:
    """The release day the draft's figures describe (the release cutoff's date)."""

    return scores["observedAt"][:10]


_POINTER = re.compile(r"scores\.json `([^`]+)`")
_DOCUMENT = re.compile(r"\b(?:README|scores|methodology|raw-data)\.md\b")


def _resolves(document, path: str) -> bool:
    try:
        resolve(document, path)
        return True
    except (FigureError, KeyError, IndexError, TypeError):
        return False


def pointer_problems(text: str, scores: dict) -> list[str]:
    """I47/I48: a pointer to a scores.json field must name a field every ranking's section has (or the file's root has);
    `<basis>` stands for each basis and `[]` for a list's items."""

    sections = [scores["v3"], *scores["v3Tracks"].values()]
    problems = []
    # I47-I49: a pointer to a generated document can promise what the document does not print, and no check can read prose,
    # so the specification points only to scores.json fields, which every generated document is rendered from.
    for line_number, line in enumerate(text.split(HISTORY_HEADING)[0].splitlines(), 1):
        for sentence in _SENTENCE.split(line):
            if _DOCUMENT.search(sentence):
                problems.append(f"line {line_number}: the specification cites a generated document; cite the scores.json field instead: {sentence[:160]}")
    for path in sorted(set(_POINTER.findall(text))):
        concrete = [path.replace("<basis>", basis).replace("[]", "[0]") for basis in ("api", "plan")]
        if not (all(_resolves(section, item) for section in sections for item in concrete) or all(_resolves(scores, item) for item in concrete)):
            problems.append(f"pointer scores.json `{path}` does not resolve in every ranking")
    return problems


def latest_source(spec_dir: Path = SPEC_DIR) -> Path:
    sources = [(int(match.group("number")), path) for path in spec_dir.glob("draft-r*.src.md") if (match := DRAFT.search(path.name))]
    if not sources:
        raise FigureError(f"no draft source in {spec_dir}")
    return max(sources)[1]


def published(source: Path) -> Path:
    return source.with_name(source.name.replace(".src.md", ".md"))


# I50 L5: a registry fact typed by hand goes stale at the next refresh whether or not its sentence is dated, so in any
# sentence that speaks of the fact, its current value must come from a placeholder.
REGISTRY_FACTS = (
    ("evidence.windowStart", r"\bwindow\b", "{v}"),
    ("evidence.windowEnd", r"\bwindow (?:is|ends?|runs)\b", "{v}"),
    ("evidence.searchCutoff", r"\bsearch cutoff\b|\blast search\b", "{v}"),
    ("evidence.searchGapDays", r"\bsearch cutoff\b", r"\b{v} days? before\b|\bthose {v} days\b"),
    ("semianalysis.lastCurrent", r"\bCurrent day\b|\bsuperseded\b|\bexpired\b|\bdemoted\b", "{v}"),
    ("semianalysis.supersededFrom", r"\bsuperseded\b", "{v}"),
    ("semianalysis.expiredFrom", r"\bexpired\b", "{v}"),
    ("semianalysis.demotedFrom", r"\bdemoted\b", "{v}"),
    ("aa.vertices", r"\bvertices\b", r"\b{v} vertices\b"),
    ("aa.vertexMatchPx", r"\bvertices\b", r"\bat {v} px\b"),
    ("evidence.reportDates", r"\breport route\b", "{v}"),
    ("aa.capturedAt", r"\bcaptur\w*", "{v}"),
    ("aa.previousCapture", r"\bcaptur\w*", r"\bpreviously {v}\b|\bprevious capture \({v}\)"),
    ("release.cutoff", r"\bcutoff\b", "{v}"),
)


def registry_problems(text: str, manifest: dict) -> list[str]:
    problems = []
    for line_number, line in enumerate(text.split(HISTORY_HEADING)[0].splitlines(), 1):
        for sentence in _SENTENCE.split(line):
            typed = PLACEHOLDER.sub("", sentence)
            found = [key for key, context, pattern in REGISTRY_FACTS
                     if re.search(context, typed) and re.search(pattern.replace("{v}", re.escape(manifest[key])), typed)]
            if found:
                problems.append(f"line {line_number}: registry value(s) typed by hand ({', '.join(found)}); use the placeholder: {sentence[:160]}")
    return problems


def _keys(document) -> set[str]:
    """Every key anywhere in a JSON document."""

    if isinstance(document, dict):
        return set(document) | {key for value in document.values() for key in _keys(value)}
    if isinstance(document, list):
        return {key for value in document for key in _keys(value)}
    return set()


def _load(data: Path, relative: str):
    path = data / relative if not relative.startswith("research/") else ROOT / relative
    return json.loads(path.read_text())


def _no_key(relative: str, pattern: str, allowed: tuple[str, ...] = ()):
    return lambda data: not [key for key in _keys(_load(data, relative)) if re.search(pattern, key) and key not in allowed]


def _bug_hunt_search_empty(model_id: str):
    def holds(data: Path) -> bool:
        records = [item for item in _load(data, "bug_hunt.json")["models"] if item["modelId"] == model_id]
        searches = [item for item in _load(data, "leaf_evidence.json")["searches"] if item["modelId"] == model_id and item["leaf"] == "bugHunt"]
        return all(item.get("fixedOf105") is None for item in records) and bool(searches) and all(item["result"] == "not found" for item in searches)
    return holds


AA_LEAF_FIELDS = (*value_v3.FRACTION_LEAVES.values(), "terminalBench40", "omniscience", "gdpval")
_INTERVAL_SUFFIX = re.compile(r"(?i)(?:Interval|Ci95|Ci|Lower|Upper|Stderr|Se|Error)\Z")


def _leaf_interval_fields(data: Path, fields: tuple[str, ...]) -> set[str]:
    """Interval-like fields beside the named AA leaves on any captured page, and on the Index evaluation entries."""

    found = set()
    for page in _load(data, "aa/aa_v432_snapshot.json")["pages"]:
        model = page.get("model") or {}
        found |= {key for key in model for field in fields if key.startswith(field) and _INTERVAL_SUFFIX.match(key[len(field):])}
        found |= {key for item in model.get("intelligenceIndexEvaluations") or [] for key in item if re.search(r"(?i)interval|ci95|lower|upper|stderr", key)}
    return found


def _cohort_slugs(data: Path) -> set[str]:
    cohort = json.loads((ROOT / "research" / "2026-10-25-board-reread" / "cohort-2026-10-25.json").read_text())
    return {item.get("aaSlug") or item["id"] for item in cohort["configurations"]}


def _cohort_ifbench_absent(data: Path) -> bool:
    slugs = _cohort_slugs(data)
    return not [page for page in _load(data, "aa/aa_v432_snapshot.json")["pages"]
                if (page.get("model") or {}).get("slug") in slugs and page["model"].get("ifbench") is not None]


def _cohort_plan_routes(data: Path) -> list[dict]:
    cohort = {item["id"] for item in json.loads((ROOT / "research" / "2026-10-25-board-reread" / "cohort-2026-10-25.json").read_text())["configurations"]}
    return [route for route in _load(data, "plan_cost_routes.json")["routes"] if cohort & set(route.get("modelIds") or [])]


def _no_deepseek_plan(data: Path) -> bool:
    document = _load(data, "plan_cost_routes.json")
    entries = [entry for key in ("routes", "providerLevelEvidence", "excludedRoutes") for entry in document.get(key) or []]
    searched = [entry for entry in document["evidencePolicy"].get("searchLog") or [] if "DeepSeek" in (entry.get("providers") or [])]
    return bool(searched) and not [entry for entry in entries if entry.get("provider") == "DeepSeek"]


def _semianalysis_unhashed(data: Path) -> bool:
    routes = [route for route in _load(data, "plan_cost_routes.json")["routes"] if route.get("sourceEvidenceId") == "semianalysis"]
    return bool(routes) and not [key for route in routes for key in route if re.search(r"(?i)sha256|contentHash", key)]


# I60 M2: a statement that a source publishes, or the capture carries, no such field is a fact about the pinned data and
# goes stale when the field appears (AA's GDPval-AA interval did at the 2026-10-23 re-capture). Each claim the draft makes
# is registered here with its test; a sentence making one carries its {{absent:KEY}} marker, and a claim that no longer
# holds fails the check until the sentence is rewritten.
ABSENCE_CLAIMS = {
    "aa.meteringBasis": ("AA's pages carry no per-configuration token-metering basis",
                         lambda data: _no_key("aa/aa_v432_snapshot.json", r"(?i)metering|tokeni[sz]er|countBasis")(data)
                         and _no_key("aa/coding_agents_capture.json", r"(?i)metering|tokeni[sz]er|countBasis")(data)),
    "aa.agentDeclinedMarker": ("the Coding Agent Index capture carries no declined-task marker", _no_key("aa/coding_agents_capture.json", r"(?i)declin")),
    "aa.cacheSplit": ("the basket captures carry no cache split", lambda data: _no_key("aa/coding_agents_capture.json", r"(?i)cache")(data)
                      and _no_key("aa/cost_charts_capture.json", r"(?i)cache")(data)),
    "semianalysis.article": ("the SemiAnalysis article is not captured (no content hash)", _semianalysis_unhashed),
    "aa.cacheRateWindow": ("AA's pages carry no cache-rate measurement window", _no_key("aa/aa_v432_snapshot.json", r"(?i)cache\w*(?:window|date|period)")),
    "aa.otherCostBoundaries": ("AA's captured pages carry no cost-boundary statement for any other component", _no_key("aa/aa_v432_snapshot.json", r"(?i)boundary")),
    "aa.eloScaleFactor": ("AA's captured pages carry no GDPval-AA Elo scale factor", _no_key("aa/aa_v432_snapshot.json", r"(?i)scale(?:Factor)?\Z|eloScale")),
    "ifbench.cohort": ("no captured page of a cohort configuration carries an IFBench result", _cohort_ifbench_absent),
    "plan.repeats": ("no Plan route of a cohort configuration records repeated measurements", lambda data: not [route for route in _cohort_plan_routes(data) if (route.get("observedRuns") or 1) > 1]),
    "plan.burnEvidence": ("no Plan route of a cohort configuration records category-specific meter burn evidence", lambda data: not [route for route in _cohort_plan_routes(data) if any(re.search(r"(?i)burn|meterWeight", key) for key in route)]),
    "deepseek.plan": ("the registry holds no DeepSeek plan and the O71 search covered DeepSeek", _no_deepseek_plan),
    "aa.fitRevision": ("AA's captured pages carry no rating fit revision or freeze status", _no_key("aa/aa_v432_snapshot.json", r"(?i)revision|freeze|frozen")),
    "aicd.error": ("AI Coding Daily rows carry no error", _no_key("research/2026-10-25-board-reread/aicd/leaderboard-allrows-parsed.json", r"(?i)error|stderr|interval|ci\b")),
    "livebench.taskCounts": ("the 2026-10-23 LiveBench release carries no task counts",
                             _no_key("research/2026-10-25-board-reread/livebench/categories-20261023.json", r"(?i)count|tasks|questions")),
    "aa.terminalBenchInterval": ("AA's pages carry no Terminal-Bench 4.0 interval", lambda data: not _leaf_interval_fields(data, ("terminalBench40",))),
    "aa.leafIntervals": ("AA's pages carry no interval for a ValueRank AA leaf other than GDPval-AA's",
                         lambda data: _leaf_interval_fields(data, AA_LEAF_FIELDS) == {"gdpvalInterval"}),
}
# I61 L6: the vocabulary of a statement that a source publishes, provides, states or sells nothing of a kind.
ABSENCE = re.compile(r"\bnot captured\b|\b(?:carries|carry|publishes|publish|published|captures|capture|sells|sell) (?:no|none)\b|"
                     r"\bdoes not (?:carry|publish|capture|state|provide|sell)\b|\bnot published\b|\bpublish(?:es)? only\b|"
                     r"\bno (?:public |other )?(?:source|component|measurement|plan measurement)\b[^.;]{0,30}?\b(?:publishes|provides|states|sells)\b", re.I)


def absence_problems(text: str, data: Path = DATA) -> list[str]:
    """I60 M2: every absence sentence carries a registered marker, and every marked claim holds against the data."""

    problems = []
    for line_number, line in enumerate(text.split(HISTORY_HEADING)[0].splitlines(), 1):
        for sentence in _SENTENCE.split(line):
            marked = re.findall(r"\{\{absent:([^}|]+)\}\}", sentence)
            if ABSENCE.search(PLACEHOLDER.sub("", sentence)) and not marked:
                problems.append(f"line {line_number}: an absence statement without an {{{{absent:KEY}}}} marker: {sentence[:160]}")
            for key in marked:
                if key in ABSENCE_CLAIMS and not ABSENCE_CLAIMS[key][1](data):
                    problems.append(f"line {line_number}: absence claim {key} ({ABSENCE_CLAIMS[key][0]}) no longer holds; rewrite the sentence")
    return problems


GENERATED_DOCS = ("README.md", "methodology.md", "scores.md")


CHANGE_DATE = re.compile(r"\b(?:possibly superseded|flagged|blocked|blocking)(?: [a-z]+)? from \d{4}-\d{2}-\d{2}")


def change_date_problems(text: str) -> list[str]:
    """I90 L4: a route's change dates are generated from the registry ({{fig:evidence.changeDates}}); a literal one in the body
    (the revision history aside) could drift from the stored records, as r148's did."""

    body = "\n".join(line for line in text.splitlines() if not line.startswith("Revision history"))
    return [f"literal change date \"{match.group(0)}\": generate it from the registry (I90 L4)" for match in CHANGE_DATE.finditer(body)]


def assumption_list_problems(root: Path) -> list[str]:
    """I73 L1: a generated doc that lists owner-named transfers beside fallbacks, ceilings or measured routes names every kind."""

    problems = []
    for name in GENERATED_DOCS:
        path = root / name
        if not path.exists():
            continue
        for line_number, line in enumerate(path.read_text().splitlines(), 1):
            for sentence in _SENTENCE.split(line):
                if ASSUMPTION_LIST.search(sentence) and not ASSUMPTION_NAMED.search(sentence):
                    problems.append(f"{name}: line {line_number}: owner-named transfers listed without the other owner-assumption kinds: {sentence[:160]}")
    return problems


def check(spec_dir: Path = SPEC_DIR, data: Path = DATA) -> list[str]:
    """Every problem with the newest draft: rendering, staleness against its source, and unmarked 'today' figures."""

    scores = json.loads((data / "scores.json").read_text())
    manifest = named_figures(scores, data)
    source = latest_source(spec_dir)
    text = source.read_text()
    try:
        rendered = render(text, scores, manifest)
    except FigureError as error:
        return [f"{source.name}: {error}"]
    problems = [f"{source.name}: {problem}" for problem in lint(text, known_names(scores, data), configuration_names(scores), release_day(scores))]
    problems += [f"{source.name}: {problem}" for problem in pointer_problems(text, scores)]
    problems += [f"{source.name}: {problem}" for problem in registry_problems(text, manifest)]
    problems += [f"{source.name}: {problem}" for problem in absence_problems(text, data)]
    problems += [f"{source.name}: {problem}" for problem in change_date_problems(text)]
    # I73 L1: the generated docs carry the same lists, so the assumption-list rule reads them too.
    problems += assumption_list_problems(data.parent if data == DATA else data)
    target = published(source)
    if not target.exists() or target.read_text() != rendered:
        problems.append(f"{target.name} is not the rendering of {source.name} against the current data (run `python3 -m valuerank.draft_figures render`)")
    stored = data / MANIFEST
    if not stored.exists() or json.loads(stored.read_text()) != manifest:
        problems.append(f"data/{MANIFEST} is stale (run `npm run build:docs`)")
    return problems


def main(argv: list[str] | None = None, spec_dir: Path = SPEC_DIR, data: Path = DATA) -> int:
    command = (argv if argv is not None else sys.argv[1:] or ["check"])[0]
    if command == "manifest":
        manifest = write_manifest(json.loads((data / "scores.json").read_text()), data)
        print(json.dumps({"wrote": f"data/{MANIFEST}", "figures": len(manifest)}))
        return 0
    if command == "render":
        scores = json.loads((data / "scores.json").read_text())
        manifest = write_manifest(scores, data)
        source = latest_source(spec_dir)
        published(source).write_text(render(source.read_text(), scores, manifest))
        print(json.dumps({"rendered": published(source).name, "figures": len(manifest)}))
        return 0
    problems = check(spec_dir, data)
    for problem in problems:
        print(problem, file=sys.stderr)
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
