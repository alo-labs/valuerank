#!/usr/bin/env python3
"""Build ValueRank's primary composite from eligible overlap and AA frontier models.

The comparison roster comes from the mapped AA model data, not the retired
DeepSWE Best leaderboard. Exact DeepSWE and Bug Hunt overlaps remain eligible;
the selected AA Intelligence Index versus total-cost frontier models are also
included with per-row coverage when benchmark results are missing.

Near-frontier policy: a plotted configuration within the policy's Index-point
gap of the rendered frontier (``nearFrontierRows`` in the reconciliation
inventory, mirrored by the capture's ``near_frontier``) makes its model family
a required primary-ranking family too, unless the family is explicitly deferred
(``requiredFamilyModelId`` null).  Near rows are validated against the capture
like frontier rows.  Every model row reports ``aaFrontierTier`` ("frontier",
"near" or null), ``aaFrontierConfiguration`` (the family's best frontier
configuration, or its smallest-gap near configuration), ``aaFrontierIntelligenceGap``
and ``aaFrontierFootnote``; ``frontierSelection`` summarises frontier and near
families.  Near families that are also frontier families keep the frontier tier.

Owner decision O33: every evidenced effort (an exact AA DeepSWE result and a
matched exact Bug Hunt result) is ranked as its own row, so a family can have
several roster configurations.  The family annotations above and the frontier
or near inclusion reason belong to the family's primary configuration only; an
evidenced sibling is ranked through the overlap reason and reports its own tier
(the tier of its exact plotted configuration, or null).
"""

from __future__ import annotations

import json
import math
import re
from pathlib import Path

from valuerank import exact_match, value_v3
from valuerank.fetch_deepswe import normalise_name, roster_names
from valuerank.clock import iso_z, utcnow


from valuerank.paths import DATA, ROOT
from valuerank.plan_costs import COST_WEIGHT_PCT, blend, cost_per_index_point, cost_scores
from valuerank.release import DATE as PUBLISH_DATE, VERSION
BUG_HUNT_PRIORITY = 20
BUG_HUNT_EMPHASIS_PRIORITY = 30
DEEPSWE_PRIORITY = 25

DEVELOPER = {
    "GPT-6 Astra": "OpenAI",
    "Gemini 3.8 Flash": "Google DeepMind",
    "Claude Opus 5": "Anthropic",
    "Claude Opus 5.5": "Anthropic",
    "Claude Haiku 5.5": "Anthropic",
    "Claude Sonnet 5.5": "Anthropic",
    "Gemini 4 Argon": "Google DeepMind",
    "GPT-5.6 Sol": "OpenAI",
    "Claude Fable 5": "Anthropic",
    "GLM-5.3": "Z AI",
    "Kimi K3": "Moonshot AI",
    "Grok 4.6": "xAI",
    "GPT-5.6 Luna": "OpenAI",
    "GPT-5.5": "OpenAI",
    "Gemini 3.7 Flash": "Google DeepMind",
    "GLM-5.3 Flash": "Z AI",
    "DeepSeek V4 Pro": "DeepSeek",
    "Claude Opus 4.8": "Anthropic",
    "Qwen3.8 Max": "Alibaba",
    "Muse Spark 1.2": "Meta",
    "Claude Sonnet 5": "Anthropic",
    "DeepSeek V4 Flash": "DeepSeek",
    "Gemini 3.6 Flash": "Google DeepMind",
    "GLM-5.2": "Z AI",
    "Gemini 3.5 Flash": "Google DeepMind",
    "GPT-6 Sol": "OpenAI",
    "GPT-6.1 Sol": "OpenAI",
    "GPT-6 Luna": "OpenAI",
    "Grok 4.7": "xAI",
    "MiMo-V2.6-Pro": "Xiaomi",
    "MiMo-V2.6-Flash": "Xiaomi",
    "Claude Fable 5.1": "Anthropic",
    "Muse Spark 1.3": "Meta",
    "Muse Wonder": "Meta",
    "Muse Wonder Full": "Meta",
    # O33: other evidenced efforts of a family, ranked as their own rows.
    "GPT-6.1 Sol (xhigh)": "OpenAI",
    "GPT-6.1 Sol (high)": "OpenAI",
    "GPT-6.1 Sol (medium)": "OpenAI",
    "GPT-6.1 Sol (low)": "OpenAI",
    "Claude Haiku 5.5 (max)": "Anthropic",
    "Claude Haiku 5.5 (high)": "Anthropic",
    "Claude Haiku 5.5 (medium)": "Anthropic",
    "Claude Haiku 5.5 (low)": "Anthropic",
    "Claude Sonnet 5.5 (xhigh)": "Anthropic",
    "Claude Sonnet 5.5 (high)": "Anthropic",
    "Claude Sonnet 5.5 (medium)": "Anthropic",
    "Claude Sonnet 5.5 (low)": "Anthropic",
    "Muse Spark 1.3 (xhigh)": "Meta",
    "Grok 4.6 (xhigh)": "xAI",
}

SHORT = {
    "GPT-6 Astra": "GPT-6 Astra",
    "Gemini 3.8 Flash": "Gem 3.8 Flash",
    "Claude Opus 5": "Opus 5",
    "Claude Opus 5.5": "Opus 5.5",
    "Claude Haiku 5.5": "Haiku 5.5",
    "Claude Sonnet 5.5": "Sonnet 5.5",
    "Gemini 4 Argon": "Gem 4 Argon",
    "GPT-5.6 Sol": "GPT-5.6 Sol",
    "Claude Fable 5": "Fable 5",
    "GLM-5.3": "GLM-5.3",
    "Kimi K3": "Kimi K3",
    "Grok 4.6": "Grok 4.6",
    "GPT-5.6 Luna": "GPT-5.6 Luna",
    "GPT-5.5": "GPT-5.5",
    "Gemini 3.7 Flash": "Gem 3.7 Flash",
    "GLM-5.3 Flash": "GLM-5.3 Flash",
    "DeepSeek V4 Pro": "DeepSeek V4 Pro",
    "Claude Opus 4.8": "Opus 4.8",
    "Qwen3.8 Max": "Qwen3.8 Max",
    "Muse Spark 1.2": "Muse Spark",
    "Claude Sonnet 5": "Sonnet 5",
    "DeepSeek V4 Flash": "DeepSeek V4 Flash",
    "Gemini 3.6 Flash": "Gem 3.6 Flash",
    "GLM-5.2": "GLM-5.2",
    "Gemini 3.5 Flash": "Gem 3.5 Flash",
    "GPT-6 Sol": "GPT-6 Sol",
    "GPT-6.1 Sol": "GPT-6.1 Sol",
    "GPT-6 Luna": "GPT-6 Luna",
    "Grok 4.7": "Grok 4.7",
    "MiMo-V2.6-Pro": "MiMo V2.6 Pro",
    "MiMo-V2.6-Flash": "MiMo V2.6 Flash",
    "Claude Fable 5.1": "Fable 5.1",
    "Muse Spark 1.3": "Muse Spark 1.3",
    "Muse Wonder": "Muse Wonder",
    "Muse Wonder Full": "Muse Wonder Full",
    "GPT-6.1 Sol (xhigh)": "GPT-6.1 Sol (xhigh)",
    "GPT-6.1 Sol (high)": "GPT-6.1 Sol (high)",
    "GPT-6.1 Sol (medium)": "GPT-6.1 Sol (medium)",
    "GPT-6.1 Sol (low)": "GPT-6.1 Sol (low)",
    "Claude Haiku 5.5 (max)": "Haiku 5.5 (max)",
    "Claude Haiku 5.5 (high)": "Haiku 5.5 (high)",
    "Claude Haiku 5.5 (medium)": "Haiku 5.5 (medium)",
    "Claude Haiku 5.5 (low)": "Haiku 5.5 (low)",
    "Claude Sonnet 5.5 (xhigh)": "Sonnet 5.5 (xhigh)",
    "Claude Sonnet 5.5 (high)": "Sonnet 5.5 (high)",
    "Claude Sonnet 5.5 (medium)": "Sonnet 5.5 (medium)",
    "Claude Sonnet 5.5 (low)": "Sonnet 5.5 (low)",
    "Muse Spark 1.3 (xhigh)": "Muse Spark 1.3 (xhigh)",
    "Grok 4.6 (xhigh)": "Grok 4.6 (xhigh)",
}

# The priority values are ValueRank's quality priorities, not the Artificial
# Analysis component weights.  AA's official component weights are retained in
# aa_metrics.json and documented separately.  Cost has no priority: it carries
# a fixed COST_WEIGHT_PCT share of every overall score, and the quality
# priorities share the rest.
COST_KEY = "costComposite"
COST_MODE = "aa-per-index-point"
CANDIDATES = [
    (COST_KEY, "Cost", False, None),
    ("omniNonHallucination", "Non-Hallucination", True, 6),
    ("terminalBenchV4", "Terminal-Bench 4.0", True, 6),
    ("livebenchInstructionFollowing", "Instruction Following (LiveBench)", True, 5),
    ("deepswePassAt1", "DeepSWE v1.1", True, DEEPSWE_PRIORITY),
    ("gdpvalV21", "GDPval-AA v2.1", True, 6),
    ("automationBenchAA", "AutomationBench-AA", True, 5),
    ("aaLcr", "AA-LCR v1.1", True, 4),
    ("omniAccuracy", "AA-Omniscience Accuracy", True, 4),
    ("hle", "HLE", True, 4),
    ("gpqaDiamond", "GPQA Diamond (legacy)", True, 4),
    ("scicode", "SciCode", True, 4),
    ("critpt", "CritPt", True, 3),
    ("intelligenceIndex", "AA Intelligence Index", True, 6),
    ("speed", "Speed", True, 5),
]


def rank_normalize(values, higher_better=True):
    """Convert values to a 0--100 rank score, averaging exact ties."""

    if not values:
        return []
    indexed = sorted(enumerate(values), key=lambda pair: pair[1], reverse=higher_better)
    ranks = [0.0] * len(values)
    cursor = 0
    while cursor < len(indexed):
        end = cursor
        while end + 1 < len(indexed) and indexed[end + 1][1] == indexed[cursor][1]:
            end += 1
        average_rank = sum(range(cursor + 1, end + 2)) / (end - cursor + 1)
        for position in range(cursor, end + 1):
            ranks[indexed[position][0]] = average_rank
        cursor = end + 1
    if len(values) == 1:
        return [100.0]
    return [round(((len(values) - rank) / (len(values) - 1)) * 100, 1) for rank in ranks]


def normalize_dimension(key, values, higher_better):
    """Cost is scored on a log scale so cost ratios keep their size; other dimensions by rank."""

    return cost_scores(values) if key == COST_KEY else rank_normalize(values, higher_better)


def quality_weight_pct(priority, quality_priority, cost_retained=True):
    """A quality dimension's nominal weight: its share of the weight cost leaves (all of it without cost)."""

    share = 100.0 - COST_WEIGHT_PCT if cost_retained else 100.0
    return round(share * priority / quality_priority, 4)


def coverage_pct(has_cost, cost_retained, available_priority, total_priority):
    """Share of the scoring weight that has an eligible value: cost's fixed share plus the quality share."""

    cost_share = COST_WEIGHT_PCT if cost_retained else 0.0
    quality = (100.0 - cost_share) * available_priority / total_priority if total_priority else 0.0
    return round((cost_share if has_cost else 0.0) + quality, 2)


def quality_score(dims, weights):
    """Priority-weighted mean of the available non-cost dimension scores, or None."""

    available = [weight for weight in weights if weight["key"] != COST_KEY and weight["key"] in dims]
    priority = sum(weight["priority"] for weight in available)
    if not priority:
        return None
    return sum(dims[weight["key"]] * weight["priority"] for weight in available) / priority


def frontier_effort(variant):
    effort = str(variant or "").casefold().strip()
    if "fallback" in effort:
        effort = effort.split(" with ", 1)[0].split(" (", 1)[0].strip()
    return effort


NO_FRONTIER_TIER = {"tier": None, "configuration": None, "intelligenceGap": None, "footnote": None}

# E195: frontier membership is AA's rendered Pareto path as observed. Each frontier point must sit on a path vertex
# (one point per vertex) and the path must rise strictly in chart coordinates; rounded tooltip values tie (GPT-6 Luna
# (max) and MiMo-V2.6-Flash both display 38) and are never used to recompute or check membership.
PATH_TOLERANCE_PX = 0.5
_PATH_NUMBER = r"-?\d+(?:\.\d+)?"
_PATH = re.compile(rf"M {_PATH_NUMBER} {_PATH_NUMBER}(?: L {_PATH_NUMBER} {_PATH_NUMBER})*")


def check_rendered_path(capture):
    """E195: the captured frontier points are exactly the vertices of the rendered Pareto path, which rises strictly."""

    path = capture.get("rendered_pareto_svg_path")
    if not isinstance(path, str) or not _PATH.fullmatch(path):
        raise ValueError("AA frontier capture must carry the rendered Pareto path as M/L coordinate pairs")
    numbers = [float(token) for token in re.findall(_PATH_NUMBER, path)]
    vertices = list(zip(numbers[0::2], numbers[1::2]))
    points = sorted((require_number(item.get("svg_x"), "svg_x"), require_number(item.get("svg_y"), "svg_y")) for item in capture.get("frontier", []))
    if len(vertices) != len(points) or any(
        abs(vx - px) > PATH_TOLERANCE_PX or abs(vy - py) > PATH_TOLERANCE_PX for (vx, vy), (px, py) in zip(vertices, points)
    ):
        raise ValueError("AA frontier capture points do not match the rendered Pareto path vertices")
    # Chart y grows downward, so a rising path has x strictly increasing and y strictly decreasing.
    if any(x2 <= x1 or y2 >= y1 for (x1, y1), (x2, y2) in zip(vertices, vertices[1:])):
        raise ValueError("AA rendered Pareto path does not rise strictly in chart coordinates")
    # E204: a plotted point left of the path's first vertex is neither frontier nor near (no F(c) there), so it would
    # drop out silently; the build stops until the owner records a decision for it.
    left = sorted(item["model_name"] for item in capture.get("points", []) if require_number(item.get("svg_x"), "svg_x") < vertices[0][0] - PATH_TOLERANCE_PX)
    if left:
        raise ValueError("AA plotted points lie left of the rendered Pareto path (an owner decision is required, E204): " + "; ".join(left))
    # E214: AA plots each Claude configuration only "with fallback", so the qualifier names AA's serving setting and a
    # third-party record matches by model and effort. Were AA to plot both states, that match would be ambiguous.
    states = {}
    for item in capture.get("points", []):
        states.setdefault((item.get("family"), item.get("effort")), set()).add(bool(item.get("fallback")))
    twins = sorted(f"{family} ({effort})" for (family, effort), seen in states.items() if len(seen) > 1)
    if twins:
        raise ValueError("AA plots configurations both with and without fallback (a matching decision is required, E214): " + "; ".join(twins))


def frontier_order(row):
    """E193: a family's highest rendered-frontier point first; along the strictly rising line that is also its dearest."""

    return (-row["intelligenceIndex"], -row["totalCostUsd"], row["name"])


# O31: a Bug Hunt scoreboard name may add only a version number to AA's model name ("Muse Wonder 1.0").
VERSION_SUFFIX = r"( v?\d+(\.\d+)*)?"
# O33: the effort follows the name as "(<effort> effort, ...)", or on some rows as a bare known effort ("Grok 4.6 (xhigh) seq").
SCOREBOARD_EFFORT = re.compile(r"(\w+) effort|(minimal|low|medium|high|xhigh|max)(?=[),;])")
# DeepSWE statuses that place a chart configuration on a roster entry (a duplicate row of a mapped configuration included).
MAPPED_STATUSES = {"exact_variant", "duplicate_configuration"}


def scoreboard_matches(names, scoreboard_rows):
    """Bug Hunt scoreboard rows for a model answering to one of ``names``, as (effort, row name) pairs."""

    matches = []
    for row in scoreboard_rows:
        base, _, rest = row["model"].partition(" (")
        effort = SCOREBOARD_EFFORT.match(rest)
        if effort and any(re.fullmatch(re.escape(name) + VERSION_SUFFIX, normalise_name(base)) for name in names):
            matches.append((effort.group(1) or effort.group(2), row["model"]))
    return matches


def evidenced_efforts(aa_model, deepswe_configurations, scoreboard_rows):
    """O30/O31: the efforts at which a model has both an exact AA DeepSWE result and a Bug Hunt result."""

    names = roster_names(aa_model)
    deepswe = {item["effort"] for item in deepswe_configurations if item.get("effort") and normalise_name(item["model"]) in names}
    return deepswe & {effort for effort, _name in scoreboard_matches(names, scoreboard_rows)}


def best_evidenced_effort(aa_model, efforts, points):
    """O30/O31: the evidenced effort with the highest AA Index, then the lower total cost, or None without evidence.

    A single evidenced effort needs no chart point; several are ordered by their plotted points on AA's chart.
    """

    if len(efforts) <= 1:
        return next(iter(efforts), None)
    family = model_family(aa_model)
    plotted = {point["effort"]: point for point in points if point.get("family") == family}
    if not efforts <= set(plotted):
        raise ValueError(f"evidenced efforts of {family} cannot be ordered: not all are plotted on AA's chart")
    return min(efforts, key=lambda effort: (-plotted[effort]["intelligence_index_display"], plotted[effort]["total_cost_usd"], effort))


MEAN_OF = re.compile(r"mean of (\d+)")


def scoreboard_sample(name):
    """The run count a scoreboard row reports ("... - mean of 3"); a row without one is a single run."""

    match = MEAN_OF.search(name)
    return int(match.group(1)) if match else 1


def check_bug_hunt_selection(model_id, aa_model, record, scoreboard_rows):
    """E206: a matched record is the owner's largest-sample published result for the model at the configuration's exact
    effort, over every harness and route, unless the record states its selection reason.

    Effort tokens match exactly (xhigh is not max) or by a documented single-mode equivalent; a record read from the
    run notes under a name the scoreboard does not parse has no candidates here and keeps its recorded effort status.
    """

    if record.get("matched") is not True or record.get("selectionReason"):
        return
    names = roster_names(aa_model)
    candidates = [
        row for row in scoreboard_rows for effort, _name in scoreboard_matches(names, [row])
        if exact_match.efforts_match(model_id, aa_model.get("aaVariant"), effort)
    ]
    if not candidates:
        return
    largest = max(scoreboard_sample(row["model"]) for row in candidates)
    values = {row["fixedOf105"] for row in candidates if scoreboard_sample(row["model"]) == largest}
    if record.get("sampleN") != largest or values != {record.get("fixedOf105")}:
        raise ValueError(f"Bug Hunt record for {model_id} is not the owner's largest-sample result at its effort and carries no selection reason (E206)")


def bug_hunt_cross_harness(model_id, aa_model, scoreboard_rows):
    """E224: the owner's largest-sample result on each harness for the configuration's exact effort, when Bug Hunt
    reports it on two or more harnesses; None otherwise (a diagnostic of how much the harness moves the leaf)."""

    best = {}
    for row in scoreboard_rows:
        for effort, _name in scoreboard_matches(roster_names(aa_model), [row]):
            if exact_match.efforts_match(model_id, aa_model.get("aaVariant"), effort):
                current = best.get(row["harness"])
                if current is None or scoreboard_sample(row["model"]) > current["runs"]:
                    best[row["harness"]] = {"harness": row["harness"], "fixedOf105": row["fixedOf105"], "runs": scoreboard_sample(row["model"])}
    return sorted(best.values(), key=lambda item: item["harness"]) if len(best) > 1 else None


def exact_bug_hunt(model_id, effort, record):
    """The Bug Hunt record as it applies to the ranked configuration: an owner match at another effort is not used."""

    if record.get("matched") is True and not exact_match.efforts_match(model_id, effort, record.get("effort")):
        return {**record, "matched": False, "matchStatus": "effort_mismatch",
                "note": f"The owner's result is for effort {record.get('effort')}; the ranked configuration is {effort}. No result is transferred between efforts."}
    return record


def model_family(aa_model):
    """The AA family a roster configuration belongs to (its chart points' family); the display name when not recorded."""

    return aa_model.get("family") or aa_model["displayName"]


def family_names(model, aa_models):
    """O33: the names a DeepSWE chart model answers to: its own, and every name of the roster configurations it matches."""

    key = normalise_name(model)
    names = {key}
    for entry in aa_models.values():
        entry_names = roster_names(entry)
        if key in entry_names:
            names |= set(entry_names)
    return names


def unrostered_evidence(deepswe_configurations, scoreboard_rows, aa_models):
    """O31/O33: DeepSWE configurations with an effort that Bug Hunt's scoreboard also reports at that effort, but that
    are not mapped to a roster entry (any match status other than an exact variant or a duplicate of one).

    Since O33 this includes another effort of a model already in the roster ("effort_mismatch"). A scoreboard name may
    add only a version number ("Muse Wonder 1.0" for AA's "Muse Wonder", but not "Muse Wonder Full 1.0"), so a match
    is flagged for a roster decision rather than silently skipped; identity is then settled when the model is added.
    """

    found = []
    for item in deepswe_configurations:
        if item.get("matchStatus") in MAPPED_STATUSES or not item.get("effort"):
            continue
        names = family_names(item["model"], aa_models)
        rows = [name for effort, name in scoreboard_matches(names, scoreboard_rows) if effort == item["effort"]]
        if rows:
            found.append(f"{item['displayLabel']} / Bug Hunt {rows[0]}")
    return found


def unranked_evidence(deepswe_configurations, scoreboard_rows, aa_models, bug_hunt_by_id):
    """O33: roster configurations mapped to an exact DeepSWE result whose effort Bug Hunt's scoreboard also reports, but
    whose Bug Hunt record is not a matched result at that effort, so the configuration would silently go unranked."""

    found = []
    for item in deepswe_configurations:
        model_id = item.get("valueRankModelId")
        if not model_id or not item.get("effort"):
            continue
        aa_model = aa_models[model_id]
        efforts = {effort for effort, _name in scoreboard_matches(roster_names(aa_model), scoreboard_rows)}
        if item["effort"] in efforts and not exact_match.bug_hunt_matches(model_id, aa_model.get("aaVariant"), bug_hunt_by_id.get(model_id)):
            found.append(f"{model_id} ({item['effort']})")
    return found


def near_order(row):
    """E193: smallest Index gap to the rendered frontier, then the lower total cost, then the name."""

    return (row["intelligenceGap"], row["totalCostUsd"], row["name"])


def capture_row_matches(item, capture_item):
    """True when an inventory row agrees with its capture row on identity, display index and cost."""

    if capture_item is None:
        return False
    inventory_effort = str(item.get("evaluatedVariant") or "").casefold()
    expected_capture_effort = None if inventory_effort == "reasoning" else frontier_effort(inventory_effort)
    capture_fallback = capture_item.get("fallback")
    captured_has_fallback = capture_fallback is True or "fallback" in str(capture_fallback or "").casefold()
    url = item.get("sourceUrl")
    return not (
        capture_item.get("model_name") != item.get("name")
        or capture_item.get("family") != item.get("family")
        or capture_item.get("effort") != expected_capture_effort
        or captured_has_fallback != ("fallback" in inventory_effort)
        or capture_item.get("intelligence_index_display") != item.get("intelligenceIndex")
        or round(require_number(capture_item.get("total_cost_usd"), f"{url}.total_cost_usd"), 2)
        != round(require_number(item.get("totalCostUsd"), f"{url}.totalCostUsd"), 2)
    )


def near_frontier_selection(inventory, capture, frontier_urls, frontier_family_ids, aa_models):
    """Validate the near-frontier rows against the capture; return ``{family: {"modelId", "rows"}}``.

    ``frontier_family_ids`` maps each frontier family to its set of required model IDs.
    A null ``modelId`` marks a family deferred by a dated roster decision.
    """

    rows, capture_rows = inventory.get("nearFrontierRows"), capture.get("near_frontier")
    policy, capture_policy = inventory.get("nearFrontierPolicy"), capture.get("near_frontier_policy")
    if not (isinstance(rows, list) and isinstance(capture_rows, list)
            and isinstance(policy, dict) and isinstance(capture_policy, dict)):
        raise ValueError("AA reconciliation inventory and frontier capture must carry the near-frontier policy and rows")
    point_counts = (
        capture.get("universe", {}).get("near_frontier_points"),
        inventory.get("sourceUniverse", {}).get("nearFrontierPointN"),
        len(rows),
        len(capture_rows),
    )
    if len(set(point_counts)) != 1:
        raise ValueError("AA near-frontier point counts do not reconcile across the inventory, its universe, and the capture")
    if policy.get("maxIntelligenceGap") is None or capture_policy.get("max_intelligence_gap") != policy["maxIntelligenceGap"]:
        raise ValueError("AA near-frontier policy differs between the inventory and its capture")
    capture_by_url = {item.get("url"): item for item in capture_rows}
    families, urls = {}, set()
    for item in rows:
        family, required_id, url = item.get("family"), item.get("requiredFamilyModelId"), item.get("sourceUrl")
        if (
            not family or not url or item.get("directlyObservedFrontier") is not False
            or "requiredFamilyModelId" not in item
            or (required_id is not None and (not isinstance(required_id, str) or not required_id))
        ):
            raise ValueError(
                "Every AA near-frontier inventory row must carry its family, owner URL, a false direct-observation flag, "
                "and a required model ID string or null"
            )
        if url in urls or url in frontier_urls:
            raise ValueError(f"AA near-frontier inventory has a duplicate owner URL: {url}")
        urls.add(url)
        capture_item = capture_by_url.get(url)
        if not capture_row_matches(item, capture_item) or capture_item.get("intelligence_gap") != item.get("intelligenceGap"):
            raise ValueError(f"AA near-frontier row is inconsistent with its current frontier capture: {url}")
        families.setdefault(family, []).append(item)
    selection = {}
    for family, family_rows in families.items():
        required_ids = {item["requiredFamilyModelId"] for item in family_rows}
        if len(required_ids) != 1:
            raise ValueError(f"AA near-frontier family has inconsistent required model IDs: {family}")
        model_id = next(iter(required_ids))
        if family in frontier_family_ids and frontier_family_ids[family] != required_ids:
            raise ValueError(f"AA near-frontier family disagrees with its frontier model ID: {family}")
        if model_id is not None:
            aa_model = aa_models.get(model_id)
            if aa_model is None:
                raise ValueError(f"AA near-frontier family model is absent from the selected AA metrics roster: {model_id}")
            if aa_model.get("displayName") != family:
                raise ValueError(f"AA near-frontier family does not match selected catalog identity for {model_id}")
        selection[family] = {"modelId": model_id, "rows": family_rows}
    return selection


def configuration_tiers(frontier_rows, near_rows):
    """O33: each plotted frontier or near configuration's own tier annotation, keyed by its AA owner URL.

    A ranked sibling of a family reports the tier of its own exact configuration, never the family's.
    """

    tiers = {}
    for item in near_rows:
        tiers[item["sourceUrl"]] = {"tier": "near", "configuration": item["name"],
                                    "intelligenceGap": item["intelligenceGap"], "footnote": item.get("sourceFootnote")}
    for item in frontier_rows:
        tiers[item["sourceUrl"]] = {"tier": "frontier", "configuration": item["name"],
                                    "intelligenceGap": 0, "footnote": item.get("sourceFootnote")}
    return tiers


def frontier_tiers(frontier_families, near_families):
    """Per-family AA tier annotations plus the sorted frontier and near family summaries."""

    annotations, frontier_list, near_list = {}, [], []
    for family, group in near_families.items():
        best = min(group["rows"], key=near_order)
        annotations[family] = {"tier": "near", "configuration": best["name"],
                               "intelligenceGap": best["intelligenceGap"], "footnote": best.get("sourceFootnote")}
        near_list.append({"family": family, "modelId": group["modelId"], "configuration": best["name"],
                          "intelligenceGap": best["intelligenceGap"]})
    for family, family_rows in frontier_families.items():
        best = min(family_rows, key=frontier_order)
        annotations[family] = {"tier": "frontier", "configuration": best["name"],
                               "intelligenceGap": 0, "footnote": best.get("sourceFootnote")}
        frontier_list.append({"family": family, "modelId": best["requiredFamilyModelId"], "configuration": best["name"]})
    return (annotations, sorted(frontier_list, key=lambda item: item["family"]),
            sorted(near_list, key=lambda item: item["family"]))


def require_number(value, label):
    if value is None or isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"missing/non-numeric required value: {label}")
    if not math.isfinite(float(value)):
        raise ValueError(f"non-finite required value: {label}")
    return float(value)


def optional_number(value, label):
    return None if value is None else require_number(value, label)


def comparison_number(value, key, label):
    value = require_number(value, label)
    # New public captures expose whole-point II labels. Compare at that shared
    # precision so older full-precision inputs do not create spurious ordering.
    return round(value) if key == "intelligenceIndex" else value


def build_bug_hunt_emphasis(rows, weights, document):
    matched_rows = [
        row for row in rows
        if row.get("bugHunt", {}).get("matched") is True
        and row.get("deepswePassAt1Pct") is not None
    ]
    if len(matched_rows) < 2:
        emphasis_weights = [{
            "key": "bugHuntFixedOf105",
            "label": "Bug Hunt Bench",
            "higherBetter": True,
            "priority": BUG_HUNT_EMPHASIS_PRIORITY,
            "weightPct": 100.0,
        }]
        matched_ids = {row["id"] for row in matched_rows}
        return {
            "benchmark": document["benchmark"],
            "benchmarkVersion": document["benchmarkVersion"],
            "sourceCommit": document["sourceCommit"],
            "sources": document["sources"],
            "matchedN": 0,
            "availableMeasuredN": len(matched_rows),
            "cohortN": len(rows),
            "coveragePct": 0.0,
            "basePrioritySum": 0,
            "benchmarkPriority": BUG_HUNT_EMPHASIS_PRIORITY,
            "totalPriority": BUG_HUNT_EMPHASIS_PRIORITY,
            "benchmarkWeightPct": 100.0,
            "weights": emphasis_weights,
            "missingModels": [row["name"] for row in rows if row["id"] not in matched_ids],
            "unscoredMeasuredModels": [row["name"] for row in matched_rows],
            "excludedResults": document.get("excludedResults", []),
            "providerClaimAudit": document.get("providerClaimAudit", {}),
            "ranking": [],
        }, [], emphasis_weights

    emphasis_base_weights = []
    for weight in weights:
        key = weight["key"]
        available_rows = [row for row in matched_rows if row.get(key) is not None]
        if len(available_rows) < 2:
            continue
        normalized = normalize_dimension(
            key,
            [comparison_number(row[key], key, f"{row['id']}.{key}") for row in available_rows],
            weight["higherBetter"],
        )
        for row, score in zip(available_rows, normalized):
            row.setdefault("bugHuntEmphasisDims", {})[key] = score
        emphasis_base_weights.append(weight)

    emphasis_base_priority = sum(
        weight["priority"] for weight in emphasis_base_weights if weight["key"] != COST_KEY
    )
    total_priority = emphasis_base_priority + BUG_HUNT_EMPHASIS_PRIORITY
    emphasis_has_cost = any(weight["key"] == COST_KEY for weight in emphasis_base_weights)
    emphasis_weights = [
        {
            "key": weight["key"],
            "label": weight["label"],
            "higherBetter": weight["higherBetter"],
            "priority": weight["priority"],
            "weightPct": COST_WEIGHT_PCT
            if weight["key"] == COST_KEY
            else quality_weight_pct(weight["priority"], total_priority, emphasis_has_cost),
        }
        for weight in emphasis_base_weights
    ]
    emphasis_weights.append({
        "key": "bugHuntFixedOf105",
        "label": "Bug Hunt Bench",
        "higherBetter": True,
        "priority": BUG_HUNT_EMPHASIS_PRIORITY,
        "weightPct": quality_weight_pct(BUG_HUNT_EMPHASIS_PRIORITY, total_priority, emphasis_has_cost),
    })
    bug_hunt_values = [
        require_number(row["bugHunt"]["fixedOf105"], f"{row['id']}.bugHunt.fixedOf105")
        for row in matched_rows
    ]
    bug_hunt_normalized = rank_normalize(bug_hunt_values, True)
    for row, score in zip(matched_rows, bug_hunt_normalized):
        row.setdefault("bugHuntEmphasisDims", {})["bugHuntFixedOf105"] = score
        row["bugHuntEmphasisScore"] = blend(
            row["bugHuntEmphasisDims"].get(COST_KEY),
            quality_score(row["bugHuntEmphasisDims"], emphasis_weights),
        )
    # A row without a cost gets no score and no emphasis rank (AGENTS.md); it keeps its normalised Bug Hunt value.
    for row in matched_rows:
        row["bugHuntEmphasisRank"] = None
    ranked_rows = sorted(
        [row for row in matched_rows if row["bugHuntEmphasisScore"] is not None],
        key=lambda row: (
            -row["bugHuntEmphasisScore"],
            row["costComposite"] if row["costComposite"] is not None else math.inf,
            row["name"],
        ),
    )
    for rank, row in enumerate(ranked_rows, 1):
        row["bugHuntEmphasisRank"] = rank
    matched_ids = {row["id"] for row in matched_rows}
    missing_models = [row["name"] for row in rows if row["id"] not in matched_ids]
    ranking = {
        "benchmark": document["benchmark"],
        "benchmarkVersion": document["benchmarkVersion"],
        "sourceCommit": document["sourceCommit"],
        "sources": document["sources"],
        "matchedN": len(ranked_rows),
        "cohortN": len(rows),
        "coveragePct": round(100.0 * len(ranked_rows) / len(rows), 2),
        "basePrioritySum": emphasis_base_priority,
        "benchmarkPriority": BUG_HUNT_EMPHASIS_PRIORITY,
        "totalPriority": total_priority,
        "benchmarkWeightPct": quality_weight_pct(BUG_HUNT_EMPHASIS_PRIORITY, total_priority, emphasis_has_cost),
        "weights": emphasis_weights,
        "missingModels": missing_models,
        "excludedResults": document.get("excludedResults", []),
        "providerClaimAudit": document.get("providerClaimAudit", {}),
        "ranking": [
            {
                "rank": row["bugHuntEmphasisRank"],
                "modelId": row["id"],
                "name": row["name"],
                "fixedOf105": row["bugHunt"]["fixedOf105"],
                "emphasisScore": row["bugHuntEmphasisScore"],
                "primaryRank": row["rank"],
            }
            for row in ranked_rows
        ],
    }
    return ranking, ranked_rows, emphasis_weights


def main(*, root: Path = ROOT, data: Path = DATA) -> int:
    deepswe_chart = json.loads((data / "aa_deepswe.json").read_text())
    aa_document = json.loads((data / "aa_metrics.json").read_text())
    # O31/O33: every configuration (model and effort) with an exact AA DeepSWE result and a Bug Hunt result must be in
    # the roster, even when another effort of the same model is already there.
    scoreboard_rows = json.loads((data / "bug_hunt_scoreboard.json").read_text())["rows"]
    missing = unrostered_evidence(deepswe_chart["configurations"], scoreboard_rows, aa_document["models"])
    if missing:
        raise ValueError("Configurations with both exact DeepSWE and Bug Hunt results are missing from the roster (O33): " + "; ".join(missing))
    frontier_inventory = json.loads((data / "aa_reconciliation_inventory.json").read_text())
    livebench_document = json.loads((data / "livebench.json").read_text())
    tb4_document = json.loads((data / "tb4.json").read_text())
    bug_hunt_document = json.loads((data / "bug_hunt.json").read_text())
    aa_models = aa_document["models"]
    livebench_models = livebench_document["models"]
    tb4_models = tb4_document["cohortRows"]
    tb4_provider_claims = {
        item["cohortModelId"]: item
        for item in tb4_document.get("providerClaims", [])
        if item.get("eligibleForRanking") is True
    }
    coverage_document = json.loads((data / "coverage_matrix.json").read_text())
    if not aa_models:
        raise ValueError("AA metrics snapshot must contain a non-empty comparison roster")
    observed_configuration_n = deepswe_chart.get("observedConfigurationN")
    configurations = deepswe_chart.get("configurations", [])
    if (
        isinstance(observed_configuration_n, bool)
        or not isinstance(observed_configuration_n, int)
        or observed_configuration_n < 1
        or len(configurations) != observed_configuration_n
        or deepswe_chart.get("benchmarkTasks") != 113
    ):
        raise ValueError(
            "AA Coding Agent Index DeepSWE chart must match its capture-backed configuration count and 113-task source"
        )
    deepswe_by_id = {}
    for config in configurations:
        model_id = config.get("valueRankModelId")
        if model_id is None:
            continue
        if config.get("matchStatus") != "exact_variant" or model_id in deepswe_by_id:
            raise ValueError(f"invalid or duplicate exact AA DeepSWE mapping for {model_id}")
        score_pct = require_number(config.get("scorePct"), f"{model_id}.DeepSWE scorePct")
        if not 0 <= score_pct <= 100:
            raise ValueError(f"invalid AA DeepSWE score for {model_id}")
        deepswe_by_id[model_id] = config
    if not set(deepswe_by_id).issubset(aa_models):
        raise ValueError("AA DeepSWE mapped model IDs must belong to the current ValueRank roster")

    frontier_rows = frontier_inventory.get("rows", [])
    frontier_universe = frontier_inventory.get("sourceUniverse", {})
    if (
        frontier_inventory.get("completeness", {}).get("status") != "complete"
        or not frontier_rows
        or len(frontier_rows) != frontier_universe.get("observedFrontierPointN")
    ):
        raise ValueError("AA reconciliation inventory must contain the complete observed frontier point set")
    capture_artifact = frontier_inventory.get("captureArtifact")
    if not capture_artifact:
        raise ValueError("AA reconciliation inventory must identify its current frontier capture artifact")
    frontier_capture = json.loads((root / capture_artifact).read_text())
    capture_rows = frontier_capture.get("frontier", [])
    capture_by_url = {item.get("url"): item for item in capture_rows if item.get("url")}
    capture_universe = frontier_capture.get("universe", {})
    if (
        len(capture_rows) != len(frontier_rows)
        or len(capture_by_url) != len(capture_rows)
        or frontier_capture.get("source_url") != frontier_inventory.get("sourceUrl")
        or capture_universe.get("rendered_pareto_vertices") != frontier_universe.get("observedFrontierPointN")
        or capture_universe.get("catalog_models") != frontier_universe.get("selectedModelN")
        or capture_universe.get("plotted_models_with_both_coordinates") != frontier_universe.get("plottedPointN")
    ):
        raise ValueError("AA reconciliation inventory no longer matches its complete direct-observation capture")
    check_rendered_path(frontier_capture)
    frontier_families = {}
    frontier_urls = set()
    for item in frontier_rows:
        family = item.get("family")
        required_id = item.get("requiredFamilyModelId")
        url = item.get("sourceUrl")
        if not family or not required_id or not url or item.get("directlyObservedFrontier") is not True:
            raise ValueError("Every AA frontier inventory row must carry its observed family, owner URL, and required model ID")
        if url in frontier_urls:
            raise ValueError(f"AA frontier inventory has a duplicate owner URL: {url}")
        frontier_urls.add(url)
        if not capture_row_matches(item, capture_by_url.get(url)):
            raise ValueError(f"AA reconciliation row is inconsistent with its current frontier capture: {url}")
        frontier_families.setdefault(family, []).append(item)

    frontier_selection_by_id = {}
    for family, family_rows in frontier_families.items():
        required_ids = {item["requiredFamilyModelId"] for item in family_rows}
        if len(required_ids) != 1:
            raise ValueError(f"AA frontier family has inconsistent required model IDs: {family}")
        model_id = next(iter(required_ids))
        aa_model = aa_models.get(model_id)
        if aa_model is None:
            raise ValueError(f"AA frontier family model is absent from the selected AA metrics roster: {model_id}")
        selected_rows = [
            item for item in family_rows
            if item.get("sourceUrl") == aa_model.get("aaUrl")
        ]
        if len(selected_rows) != 1:
            raise ValueError(f"AA frontier family must identify one exact selected source URL: {family}")
        frontier_item = selected_rows[0]
        if frontier_item is not min(family_rows, key=frontier_order):
            raise ValueError(f"AA frontier family must rank its highest rendered-frontier point (E193): {family}")
        if aa_model.get("aaSlug") != frontier_item.get("aaId"):
            raise ValueError(f"AA frontier source slug does not match selected catalog identity for {model_id}")
        if aa_model.get("displayName") != family:
            raise ValueError(f"AA frontier family does not match selected catalog identity for {model_id}")
        inventory_effort = str(frontier_item.get("evaluatedVariant") or "").casefold()
        selected_effort = aa_model.get("aaVariant")
        if inventory_effort == "reasoning":
            if selected_effort is not None:
                raise ValueError(f"AA reasoning-only frontier identity has an unexpected selected effort for {model_id}")
        else:
            normalized_effort = frontier_effort(inventory_effort)
            if selected_effort != normalized_effort:
                raise ValueError(f"AA frontier effort does not match selected catalog variant for {model_id}")
        fallback = "with fallback" if "fallback" in inventory_effort else None
        aa_labels = " ".join(
            str(aa_model.get(key) or "") for key in ("aaName", "aaShortName")
        ).casefold()
        if fallback and "fallback" not in aa_labels:
            raise ValueError(f"AA frontier fallback does not match selected catalog identity for {model_id}")
        frontier_selection_by_id[model_id] = {
            "family": family,
            "modelName": frontier_item["name"],
            "effort": frontier_item.get("evaluatedVariant"),
            "fallback": fallback,
            "url": frontier_item["sourceUrl"],
            "intelligenceIndexDisplay": frontier_item["intelligenceIndex"],
            "totalCostUsd": frontier_item["totalCostUsd"],
        }

    near_families = near_frontier_selection(
        frontier_inventory,
        frontier_capture,
        frontier_urls,
        {family: {item["requiredFamilyModelId"] for item in family_rows} for family, family_rows in frontier_families.items()},
        aa_models,
    )
    near_policy = frontier_inventory["nearFrontierPolicy"]
    aa_tiers, frontier_family_list, near_family_list = frontier_tiers(frontier_families, near_families)
    own_tiers = configuration_tiers(frontier_rows, frontier_inventory["nearFrontierRows"])
    # O33: the family annotations go to each family's primary configuration only.
    family_primary_ids = {family: group["modelId"] for family, group in near_families.items()}
    family_primary_ids.update({selection["family"]: model_id for model_id, selection in frontier_selection_by_id.items()})
    near_frontier_primary_ids = {group["modelId"] for group in near_families.values() if group["modelId"]}
    frontier_selection = {
        "sourceUrl": frontier_inventory["sourceUrl"],
        "captureArtifact": frontier_inventory["captureArtifact"],
        "capturedAt": frontier_capture.get("captured_at"),
        "indexVersion": frontier_capture.get("index_version"),
        "chartTitle": frontier_capture.get("chart_title"),
        "costUnit": frontier_capture.get("cost_unit"),
        "completeness": frontier_inventory["completeness"],
        "sourceUniverse": frontier_universe,
        "configurationN": len(frontier_rows),
        "familyN": len(frontier_families),
        "frontierFamilies": frontier_family_list,
        "nearFrontierPolicy": near_policy,
        "nearFrontierPointN": len(frontier_inventory["nearFrontierRows"]),
        "nearFrontierFamilyN": len(near_families),
        "nearFrontierRequiredModelN": len(near_frontier_primary_ids),
        "nearFrontierDeferredN": sum(group["modelId"] is None for group in near_families.values()),
        "nearFrontierFamilies": near_family_list,
        "selectedFamilyModelIds": [
            {
                "modelId": model_id,
                **selection,
            }
            for model_id, selection in sorted(
                frontier_selection_by_id.items(),
                key=lambda item: item[1]["family"],
            )
        ],
    }
    cohort_ids = set(aa_models)
    display_names = [item["displayName"] for item in aa_models.values()]
    if len(set(display_names)) != len(display_names):
        raise ValueError("Roster display names must be unique: several efforts of one family need distinct names (O33)")
    if set(livebench_models) != cohort_ids:
        raise ValueError("LiveBench snapshot must contain exactly the current AA model cohort")
    bug_hunt_by_id = {item["modelId"]: item for item in bug_hunt_document["models"]}
    if set(bug_hunt_by_id) != cohort_ids:
        raise ValueError("Bug Hunt snapshot must declare exactly the current AA model cohort")
    for model_id, item in bug_hunt_by_id.items():
        if item.get("matched") is True:
            require_number(item.get("fixedOf105"), f"{model_id}.bugHunt.fixedOf105")
            if not 0 <= item["fixedOf105"] <= 105 or item.get("sampleN", 0) < 1:
                raise ValueError(f"invalid Bug Hunt score/sample for {model_id}")

    # O33: a rostered configuration with both results is ranked, so its Bug Hunt record must be the matched result at its effort.
    unranked = unranked_evidence(deepswe_chart["configurations"], scoreboard_rows, aa_models, bug_hunt_by_id)
    if unranked:
        raise ValueError("Configurations with both exact DeepSWE and Bug Hunt results lack a matched Bug Hunt record at their effort (O33): " + "; ".join(unranked))
    bug_hunt_owner_matches = [item for item in bug_hunt_by_id.values() if item.get("matched") is True]
    bug_hunt_owner_missing_names = [
        aa_models[model_id]["displayName"]
        for model_id, item in bug_hunt_by_id.items()
        if item.get("matched") is not True
    ]

    rows = []
    for model_id, aa_model in aa_models.items():
        deepswe_model = deepswe_by_id.get(model_id)
        aa_metrics = aa_model["metrics"]
        supplemental = aa_model.get("supplemental", {})
        livebench = livebench_models[model_id]
        tb4 = tb4_models.get(model_id)
        # The legacy composite takes a Terminal-Bench row only at the configuration's own effort (AGENTS.md: no transfer).
        if tb4 is not None and not exact_match.efforts_match(model_id, aa_model.get("aaVariant"), exact_match.split_effort(tb4["model"])[1]):
            tb4 = None
        tb4_claim = tb4_provider_claims.get(model_id) if not tb4 else None
        display_name = aa_model["displayName"]
        if display_name not in DEVELOPER or display_name not in SHORT:
            raise ValueError(f"identity mapping missing: {display_name}")
        family = model_family(aa_model)
        bug_hunt = exact_bug_hunt(model_id, aa_model.get("aaVariant"), bug_hunt_by_id[model_id])
        check_bug_hunt_selection(model_id, aa_model, bug_hunt, scoreboard_rows)
        if family_primary_ids.get(family) == model_id:
            tier = aa_tiers[family]
        else:
            tier = own_tiers.get(aa_model["aaUrl"], NO_FRONTIER_TIER)
        row = {
            "id": model_id,
            "name": display_name,
            "family": family,
            "shortName": SHORT[display_name],
            "developer": DEVELOPER[display_name],
            "frontierSelection": frontier_selection_by_id.get(model_id),
            "aaFrontierTier": tier["tier"],
            "aaFrontierConfiguration": tier["configuration"],
            "aaFrontierIntelligenceGap": tier["intelligenceGap"],
            "aaFrontierFootnote": tier["footnote"],
            "bugHunt": bug_hunt,
            "bugHuntCrossHarness": bug_hunt_cross_harness(model_id, aa_model, scoreboard_rows),
            "rankDeepSWE": deepswe_model.get("sourceOrder") if deepswe_model else None,
            "deepsweEffort": deepswe_model.get("effort") if deepswe_model else None,
            "deepswePassAt1": (require_number(deepswe_model["scorePct"], f"{model_id}.DeepSWE scorePct") / 100) if deepswe_model else None,
            "deepswePassAt1Pct": require_number(deepswe_model["scorePct"], f"{model_id}.DeepSWE scorePct") if deepswe_model else None,
            "deepsweUncertaintyPct": None,
            "deepsweCost": None,
            "deepsweOutputTokens": None,
            "deepsweOutputTokensLabel": None,
            "deepsweAgent": deepswe_model.get("agent") if deepswe_model else None,
            "deepsweScoreConfig": deepswe_model,
            "deepsweAgentSteps": None,
            "aaSlug": aa_model["aaSlug"],
            "aaUrl": aa_model["aaUrl"],
            "aaVariant": aa_model.get("aaVariant"),
            "aaEvalCost": aa_metrics.get("aaEvalCost"),
            "briefcaseElo": aa_metrics.get("briefcaseElo"),
            "briefcaseNormalized": aa_metrics.get("briefcaseNormalized"),
            "intelligenceIndex": aa_metrics.get("intelligenceIndex"),
            "intelligenceIndexStatus": aa_model.get("intelligenceIndexStatus", "measured"),
            "gdpvalV21": aa_metrics.get("gdpvalV21"),
            "gdpvalV21Normalized": aa_metrics.get("gdpvalV21Normalized"),
            "automationBenchAA": aa_metrics.get("automationBenchAA"),
            "aaTerminalBenchV40": aa_metrics.get("terminalBenchV40"),
            "aaTerminalBenchV21": supplemental.get("terminalBenchV21"),
            "legacyTau3Banking": supplemental.get("tauBanking"),
            "livebenchModel": livebench.get("livebenchModel"),
            "livebenchOverall": livebench.get("overallScore"),
            "livebenchInstructionFollowing": livebench.get("instructionFollowingScore"),
            "livebenchCostPerSuccessfulTask": livebench.get("costPerSuccessfulTaskUsd"),
            "livebenchCategoryScores": livebench.get("categoryScores", {}),
            "livebenchTaskScores": livebench.get("tasks", {}),
            "terminalBenchV4": tb4.get("resolutionRate") if tb4 else (tb4_claim.get("value") if tb4_claim else None),
            "terminalBenchV4Pct": tb4.get("resolutionRatePct") if tb4 else (tb4_claim.get("valuePct") if tb4_claim else None),
            "terminalBenchV4UncertaintyPct": tb4.get("uncertaintyPct") if tb4 else None,
            "terminalBenchV4SourceType": "benchmark_owner" if tb4 else ("model_provider_claim" if tb4_claim else None),
            "terminalBenchV4Claim": tb4_claim,
            "terminalBenchV4Cost": tb4.get("costUsd") if tb4 else None,
            "terminalBenchV4Agent": tb4.get("agent") if tb4 else None,
            "terminalBenchV4Effort": tb4.get("model") if tb4 else (tb4_claim.get("evaluatedModel") if tb4_claim else None),
            "terminalBenchV4ReleaseDate": tb4.get("releaseDate") if tb4 else (tb4_claim.get("publishedOn") if tb4_claim else None),
            "terminalBenchV4Model": tb4.get("baseModel") if tb4 else (tb4_claim.get("evaluatedModel") if tb4_claim else None),
            "scicode": aa_metrics.get("scicode"),
            "gdpPdfAllPass": aa_metrics.get("gdpPdfAllPass"),
            "aaLcr": aa_metrics.get("aaLcr"),
            "hle": aa_metrics.get("hle"),
            "gpqaDiamond": aa_metrics.get("gpqaDiamond"),
            "critpt": aa_metrics.get("critpt"),
            "omniAccuracy": aa_metrics.get("omniAccuracy"),
            "omniNonHallucination": aa_metrics.get("omniNonHallucination"),
            "speed": aa_metrics.get("speed"),
            "supplemental": supplemental,
            "extraction": aa_model.get("extraction"),
        }
        rows.append(row)

    overlap_primary_ids = {
        row["id"] for row in rows
        if row["bugHunt"].get("matched") is True
        and row.get("deepswePassAt1Pct") is not None
    }
    frontier_primary_ids = set(frontier_selection_by_id)
    near_only_primary_ids = near_frontier_primary_ids - frontier_primary_ids
    primary_ids = overlap_primary_ids | frontier_primary_ids | near_frontier_primary_ids
    # O33: every evidenced effort is ranked as its own row (checked above) through the overlap reason. The frontier and
    # near rules still decide which configuration is a family's primary and carries its inclusion reason: a frontier
    # family's highest rendered point (checked above); a near family's highest-Index evidenced effort (several: the
    # highest AA Index, then the lower cost; E193/O30), else its smallest-gap near point.
    for family, group in sorted(near_families.items()):
        model_id = group["modelId"]
        if model_id is None or model_id in frontier_primary_ids:
            continue
        aa_model = aa_models[model_id]
        best = best_evidenced_effort(aa_model, evidenced_efforts(aa_model, deepswe_chart["configurations"], scoreboard_rows), frontier_capture["points"])
        if best is not None and aa_model.get("aaVariant") != best:
            raise ValueError(f"AA near-frontier family must rank its configuration with exact DeepSWE and Bug Hunt results (O30): {family} at {best}")
        if best is None and aa_model.get("aaUrl") != min(group["rows"], key=near_order)["sourceUrl"]:
            raise ValueError(f"AA near-frontier family without exact DeepSWE and Bug Hunt results must rank its smallest-gap near point (E193): {family}")
    primary_rows = [row for row in rows if row["id"] in primary_ids]
    unranked_rows = [row for row in rows if row["id"] not in primary_ids]

    # Token efficiency: AA total evaluation cost per AA Intelligence Index point
    # (USD per point, lower is better). A row without a cost or an Index has no cost value.
    for row in rows:
        if row["aaEvalCost"] is not None and require_number(row["aaEvalCost"], f"{row['id']}.aaEvalCost") <= 0:
            raise ValueError(f"AA evaluation cost must be positive: {row['id']}")
        row["aaCostPerIndexPoint"] = cost_per_index_point(row["aaEvalCost"], row.get("intelligenceIndex"))
    aa_cost_rows = [row for row in primary_rows if row["aaCostPerIndexPoint"] is not None]
    cost_mode = COST_MODE if aa_cost_rows else "unavailable (AA evaluation cost has no primary coverage)"
    for row in primary_rows:
        row["deepSweCostNorm"] = None
        row["costComposite"] = row["aaCostPerIndexPoint"]
        row["costMode"] = cost_mode
    for row in unranked_rows:
        row["deepSweCostNorm"] = None
        row["costComposite"] = None
        row["costMode"] = cost_mode

    coverage = {}
    for key, label, higher_better, priority in CANDIDATES:
        missing = [row["name"] for row in primary_rows if row.get(key) is None]
        source_missing = [row["name"] for row in rows if row.get(key) is None]
        coverage[key] = {
            "label": label,
            "missing": missing,
            "nMissing": len(missing),
            "availableN": len(primary_rows) - len(missing),
            "cohortN": len(primary_rows),
            "sourceMissing": source_missing,
            "sourceCohortN": len(rows),
            "sourceAvailableN": len(rows) - len(source_missing),
            "higherBetter": higher_better,
            "priority": priority,
        }
    retained = [candidate for candidate in CANDIDATES if coverage[candidate[0]]["availableN"] >= 2]
    dropped = [
        {
            "key": key,
            "label": label,
            "missing": coverage[key]["missing"],
            "sourceMissing": coverage[key]["sourceMissing"],
            "availableN": coverage[key]["availableN"],
            "reason": (
                "fewer than two primary models have observed values; no comparative percentile is assigned"
            ),
        }
        for key, label, _higher_better, _priority in CANDIDATES
        if coverage[key]["availableN"] < 2
    ]
    raw_priority_sum = sum(candidate[3] for candidate in retained if candidate[0] != COST_KEY)
    cost_retained = any(candidate[0] == COST_KEY for candidate in retained)
    base_weights = [
        {
            "key": key,
            "label": label,
            "higherBetter": higher_better,
            "priority": priority,
            "weightPct": COST_WEIGHT_PCT if key == COST_KEY else quality_weight_pct(priority, raw_priority_sum, cost_retained),
        }
        for key, label, higher_better, priority in retained
    ] if raw_priority_sum else []
    primary_bug_hunt_value_n = sum(
        row["bugHunt"].get("matched") is True for row in primary_rows
    )
    primary_has_bug_hunt_dimension = primary_bug_hunt_value_n >= 2
    primary_total_priority = raw_priority_sum + (
        BUG_HUNT_PRIORITY if primary_has_bug_hunt_dimension else 0
    )
    weights = [
        {
            **weight,
            "weightPct": COST_WEIGHT_PCT
            if weight["key"] == COST_KEY
            else quality_weight_pct(weight["priority"], primary_total_priority, cost_retained),
        }
        for weight in base_weights
    ]
    if primary_has_bug_hunt_dimension:
        weights.append({
            "key": "bugHuntFixedOf105",
            "label": "Bug Hunt Bench",
            "higherBetter": True,
            "priority": BUG_HUNT_PRIORITY,
            "weightPct": quality_weight_pct(BUG_HUNT_PRIORITY, primary_total_priority, cost_retained),
        })
    bug_hunt_primary_weight_pct = next(
        (weight["weightPct"] for weight in weights if weight["key"] == "bugHuntFixedOf105"),
        0.0,
    )

    for row in rows:
        row["dims"] = {}
        row["rankingEligible"] = row["id"] in primary_ids
        row["rankingInclusionReasons"] = []
        if row["id"] in overlap_primary_ids:
            row["rankingInclusionReasons"].append("Exact AA DeepSWE and eligible Bug Hunt overlap")
        if row["id"] in frontier_primary_ids:
            row["rankingInclusionReasons"].append(
                "Required AA Intelligence Index versus total-evaluation-cost frontier family"
            )
        if row["id"] in near_only_primary_ids:
            row["rankingInclusionReasons"].append(
                "Near-frontier AA family (within "
                f"{near_policy['maxIntelligenceGap']:g} Index points of the rendered frontier)"
            )
        row["missingFields"] = [key for key, _label, _higher, _priority in CANDIDATES if row.get(key) is None]
        row["rankingExclusionReasons"] = []
        row["familyPrimary"] = False
        if row["bugHunt"].get("matched") is not True and row["rankingEligible"]:
            row["missingFields"].append("bugHuntFixedOf105")
        if not row["rankingEligible"] and row["bugHunt"].get("matched") is not True:
            row["missingFields"].append("bugHuntFixedOf105")
            if row["bugHunt"].get("matchStatus") == "reasoning_variant_unverified":
                owner_configurations = row["bugHunt"].get("availableOwnerConfigurations", [])
                available_scores = [
                    f"{config['fixedOf105']:g}/105"
                    for config in owner_configurations
                    if isinstance(config.get("fixedOf105"), (int, float))
                    and not isinstance(config.get("fixedOf105"), bool)
                ]
                owner_result_note = (
                    f"owner default result {', '.join(available_scores)} available"
                    if available_scores else "owner default result available"
                )
                row["rankingExclusionReasons"].append(
                    "No eligible exact-variant Bug Hunt match; " + owner_result_note
                    + "; selected reasoning equivalence is unverified"
                )
            else:
                row["rankingExclusionReasons"].append("No eligible exact-model Bug Hunt result in the selected source snapshot")
        if not row["rankingEligible"] and row.get("deepswePassAt1Pct") is None:
            row["rankingExclusionReasons"].append("No exact-variant AA DeepSWE result in the selected source snapshot")
        if not row["rankingEligible"]:
            row["rankingExclusionReasons"].append("Not a required AA frontier or near-frontier family model")
            row["rank"] = None
            row["qualityRank"] = None
            row["overallScore"] = None
            row["qualityScore"] = None
            row["vRanks"] = {}
            row["pareto"] = None
            row["isMissing"] = True
            row["rankingStatus"] = "excluded_from_primary_cohort"
    # E205: each family's primary row (its frontier or near configuration; for a family ranked only through retention,
    # the highest-Index evidenced effort, then the lower cost), for the one-row-per-family diagnostic.
    ranked_families = {}
    for row in primary_rows:
        ranked_families.setdefault(row["family"], []).append(row)
    for group in ranked_families.values():
        primary = [row for row in group if row["id"] in frontier_primary_ids | near_only_primary_ids]
        if not primary:
            by_effort = {aa_models[row["id"]].get("aaVariant"): row for row in group}
            primary = [by_effort[best_evidenced_effort(aa_models[group[0]["id"]], set(by_effort), frontier_capture["points"])]]
        primary[0]["familyPrimary"] = True
    # O36: a configuration without the full benchmark set after the exhaustive search is listed, never ranked or normalised.
    incomplete = {
        item["id"]: item
        for item in value_v3.incomplete_configurations([value_v3.configuration(row) for row in primary_rows], value_v3.load_documents(data))
    }
    for weight in weights:
        key = weight["key"]
        available_rows = []
        values = []
        for row in primary_rows:
            if row["id"] in incomplete:
                continue
            if key == "bugHuntFixedOf105":
                value = row["bugHunt"].get("fixedOf105") if row["bugHunt"].get("matched") is True else None
            else:
                value = row.get(key)
            if value is None:
                continue
            available_rows.append(row)
            values.append(comparison_number(value, key, f"{row['id']}.{key}"))
        # Every retained weight has at least two observed primary values (see
        # ``retained`` and ``primary_has_bug_hunt_dimension``), so no guard is needed.
        normalized = normalize_dimension(key, values, weight["higherBetter"])
        for row, score in zip(available_rows, normalized):
            row["dims"][key] = score

    effective_keys = [weight["key"] for weight in weights]
    for row in rows:
        available_priority = sum(
            weight["priority"] for weight in weights
            if weight["key"] != COST_KEY and weight["key"] in row["dims"]
        )
        has_cost = COST_KEY in row["dims"]
        row["metricCoverage"] = {
            "costAvailable": has_cost,
            "availablePriority": available_priority,
            "totalPriority": primary_total_priority,
            "coveragePct": coverage_pct(has_cost, cost_retained, available_priority, primary_total_priority),
            "missingKeys": [key for key in effective_keys if key not in row["dims"]],
        }

    for row in primary_rows:
        quality = quality_score(row["dims"], weights)
        row["overallScore"] = blend(row["dims"].get(COST_KEY), quality)
        row["qualityScore"] = round(quality, 1) if quality is not None else None
        row["isMissing"] = bool(row["missingFields"] or row["metricCoverage"]["missingKeys"])
        row["rank"] = None
        row["qualityRank"] = None
        row["pareto"] = None
        row["rankingStatus"] = (
            "excluded_incomplete_benchmarks" if row["id"] in incomplete
            else "unranked_no_quality_dimension" if row["qualityScore"] is None
            else "unranked_no_cost" if row["overallScore"] is None
            else "rankable"
        )
        row["vRanks"] = {
            weight["key"]: row["dims"][weight["key"]]
            for weight in weights
            if weight["key"] in row["dims"]
        }
        if row["id"] in incomplete:
            missing = ", ".join(value_v3.LEAF_LABELS[key] for key in incomplete[row["id"]]["missing"])
            row["rankingEligible"] = False
            row["costComposite"] = None
            row["rankingExclusionReasons"].append(f"Incomplete benchmark evidence after an exhaustive search (O36): no {missing}")

    by_overall = sorted(
        [
            row for row in primary_rows
            if row["overallScore"] is not None and row["qualityScore"] is not None
        ],
        key=lambda row: (
            -row["overallScore"],
            row["costComposite"] if row["costComposite"] is not None else math.inf,
            row["name"],
        ),
    )
    for rank, row in enumerate(by_overall, 1):
        row["rank"] = rank
        row["rankingStatus"] = "ranked"
    unscored_primary_rows = sorted(
        [row for row in primary_rows if row["overallScore"] is None],
        key=lambda row: row["name"],
    )
    by_quality = sorted(
        [row for row in primary_rows if row["qualityScore"] is not None],
        key=lambda row: (
            -row["qualityScore"],
            row["costComposite"] if row["costComposite"] is not None else math.inf,
            row["name"],
        ),
    )
    for rank, row in enumerate(by_quality, 1):
        row["qualityRank"] = rank

    pareto_candidates = [
        row for row in primary_rows
        if row["costComposite"] is not None and row["qualityScore"] is not None
    ]
    pareto = []
    for row in pareto_candidates:
        dominated = any(
            other["id"] != row["id"]
            and other["costComposite"] <= row["costComposite"]
            and other["qualityScore"] >= row["qualityScore"]
            and (
                other["costComposite"] < row["costComposite"]
                or other["qualityScore"] > row["qualityScore"]
            )
            for other in pareto_candidates
        )
        row["pareto"] = not dominated
        if row["pareto"]:
            pareto.append(row["name"])

    # Retain a stronger Bug Hunt emphasis view as an optional companion to the primary rank.
    bug_hunt_emphasis, bug_hunt_ranked_rows, bug_hunt_weights = build_bug_hunt_emphasis(
        rows, base_weights, bug_hunt_document
    )
    primary_bug_hunt_matches = [
        row for row in primary_rows if row["bugHunt"].get("matched") is True
    ]
    primary_bug_hunt_missing_names = [
        row["name"] for row in primary_rows if row["bugHunt"].get("matched") is not True
    ]
    if len(primary_bug_hunt_matches) < 2:
        dropped.append({
            "key": "bugHuntFixedOf105",
            "label": "Bug Hunt Bench bugs fixed out of 105",
            "missing": primary_bug_hunt_missing_names,
            "sourceMissing": bug_hunt_owner_missing_names,
            "availableN": len(primary_bug_hunt_matches),
            "reason": "fewer than two primary models have eligible results; no comparative percentile is assigned",
        })

    # Keep source extraction coverage and add score-specific and explicitly
    # labelled external benchmark coverage.
    primary_dimension_keys = {weight["key"] for weight in weights}
    score_coverage = {
        key: {
            "label": item["label"],
            "availableN": item["cohortN"] - item["nMissing"],
            "cohortN": item["cohortN"],
            "coveragePct": round(100.0 * (item["cohortN"] - item["nMissing"]) / item["cohortN"], 2),
            "normalizableN": item["availableN"] if item["availableN"] >= 2 else 0,
            "missingModels": item["missing"],
            "sourceAvailableN": item["sourceAvailableN"],
            "sourceCohortN": item["sourceCohortN"],
            "sourceMissingModels": item["sourceMissing"],
            "includedInPrimaryScore": key in primary_dimension_keys,
        }
        for key, item in coverage.items()
    }
    score_coverage["bugHuntFixedOf105"] = {
        "label": "Bug Hunt Bench bugs fixed out of 105",
        "availableN": len(primary_bug_hunt_matches),
        "cohortN": len(primary_rows),
        "coveragePct": round(100.0 * len(primary_bug_hunt_matches) / len(primary_rows), 2),
        "normalizableN": len(primary_bug_hunt_matches) if len(primary_bug_hunt_matches) >= 2 else 0,
        "missingModels": primary_bug_hunt_missing_names,
        "sourceAvailableN": len(bug_hunt_owner_matches),
        "sourceCohortN": len(rows),
        "sourceMissingModels": bug_hunt_owner_missing_names,
        "rankableOverlapN": len(overlap_primary_ids),
        "includedInPrimaryScore": "bugHuntFixedOf105" in primary_dimension_keys,
    }
    external_coverage = {
        "livebenchOverall": {
            "group": "supplemental",
            "label": "LiveBench Overall Score",
            "availableN": sum(row["livebenchOverall"] is not None for row in primary_rows),
            "cohortN": len(primary_rows),
            "coveragePct": round(100 * sum(row["livebenchOverall"] is not None for row in primary_rows) / len(primary_rows), 2),
            "missingModels": [row["name"] for row in primary_rows if row["livebenchOverall"] is None],
            "sourceAvailableN": livebench_document["matchedN"],
            "sourceCohortN": len(rows),
            "sourceMissingModels": livebench_document["missingModels"],
            "includedInPrimaryScore": False,
            "sourceRelease": livebench_document["release"],
            "publishedN": livebench_document.get("publishedN", livebench_document["matchedN"]),
            "supplementalMatchedN": livebench_document.get("supplementalMatchedN", 0),
            "supplementalModels": [
                record["name"]
                for record in livebench_document.get("supplementalModels", {}).values()
                if record.get("matched")
            ],
        },
        "livebenchInstructionFollowing": {
            "group": "primary" if "livebenchInstructionFollowing" in primary_dimension_keys else "supplemental",
            "label": "Instruction Following (LiveBench)",
            "availableN": sum(row["livebenchInstructionFollowing"] is not None for row in primary_rows),
            "cohortN": len(primary_rows),
            "coveragePct": round(100 * sum(row["livebenchInstructionFollowing"] is not None for row in primary_rows) / len(primary_rows), 2),
            "missingModels": [row["name"] for row in primary_rows if row["livebenchInstructionFollowing"] is None],
            "sourceAvailableN": livebench_document["matchedN"],
            "sourceCohortN": len(rows),
            "sourceMissingModels": livebench_document["missingModels"],
            "includedInPrimaryScore": "livebenchInstructionFollowing" in primary_dimension_keys,
            "sourceRelease": livebench_document["release"],
            "publishedN": livebench_document.get("publishedN", livebench_document["matchedN"]),
            "supplementalMatchedN": livebench_document.get("supplementalMatchedN", 0),
            "supplementalModels": [
                record["name"]
                for record in livebench_document.get("supplementalModels", {}).values()
                if record.get("matched")
            ],
        },
        "livebenchCostPerSuccessfulTask": {
            "group": "supplemental",
            "label": "LiveBench Cost Per Successful Task",
            "availableN": sum(row["livebenchCostPerSuccessfulTask"] is not None for row in primary_rows),
            "cohortN": len(primary_rows),
            "coveragePct": round(100 * sum(row["livebenchCostPerSuccessfulTask"] is not None for row in primary_rows) / len(primary_rows), 2),
            "missingModels": [row["name"] for row in primary_rows if row["livebenchCostPerSuccessfulTask"] is None],
            "sourceAvailableN": livebench_document["matchedN"],
            "sourceCohortN": len(rows),
            "sourceMissingModels": livebench_document["missingModels"],
            "includedInPrimaryScore": False,
            "sourceRelease": livebench_document["release"],
            "publishedN": livebench_document.get("publishedN", livebench_document["matchedN"]),
            "supplementalMatchedN": livebench_document.get("supplementalMatchedN", 0),
            "supplementalModels": [
                record["name"]
                for record in livebench_document.get("supplementalModels", {}).values()
                if record.get("matched")
            ],
        },
        "terminalBenchV4": {
            "group": "primary" if "terminalBenchV4" in primary_dimension_keys else "supplemental",
            "label": "Terminal-Bench 4.0",
            "availableN": sum(row["terminalBenchV4"] is not None for row in primary_rows),
            "cohortN": len(primary_rows),
            "coveragePct": round(100 * sum(row["terminalBenchV4"] is not None for row in primary_rows) / len(primary_rows), 2),
            "sourceAvailableN": tb4_document.get("rankingAvailableN", tb4_document["matchedN"]),
            "sourceCohortN": len(rows),
            "officialMatchedN": tb4_document["matchedN"],
            "providerClaimMatchedN": tb4_document.get("providerClaimN", 0),
            "missingModels": [row["name"] for row in primary_rows if row["terminalBenchV4"] is None],
            "sourceMissingModels": tb4_document.get("rankingMissingModels", tb4_document["missingModels"]),
            "includedInPrimaryScore": "terminalBenchV4" in primary_dimension_keys,
            "sourceRelease": tb4_document["version"],
        },
        "bugHuntFixedOf105": {
            "group": "primary" if "bugHuntFixedOf105" in primary_dimension_keys else "supplemental",
            "label": "Bug Hunt Bench bugs fixed out of 105",
            "availableN": len(primary_bug_hunt_matches),
            "cohortN": len(primary_rows),
            "coveragePct": round(100.0 * len(primary_bug_hunt_matches) / len(primary_rows), 2),
            "missingModels": primary_bug_hunt_missing_names,
            "sourceAvailableN": len(bug_hunt_owner_matches),
            "sourceCohortN": len(rows),
            "sourceCoveragePct": round(100.0 * len(bug_hunt_owner_matches) / len(rows), 2),
            "sourceMissingModels": bug_hunt_owner_missing_names,
            "includedInPrimaryScore": "bugHuntFixedOf105" in primary_dimension_keys,
            "includedInBugHuntEmphasisRanking": bug_hunt_emphasis["matchedN"] >= 2,
            "sourceRelease": bug_hunt_document["benchmarkVersion"],
            "sourceCommit": bug_hunt_document["sourceCommit"],
        },
    }
    coverage_document["cohort"] = f"Artificial Analysis v4.3.2 mapped {len(rows)}-model ValueRank comparison roster"
    coverage_document["cohortN"] = len(rows)
    coverage_document["deepSweSource"] = deepswe_chart["source"]
    coverage_document["deepSweConfigurationsN"] = len(deepswe_chart["configurations"])
    coverage_document["deepSweObservedConfigurationN"] = observed_configuration_n
    coverage_document["frontierSelection"] = frontier_selection
    source_fields = dict(coverage_document.get("fields", {}))
    source_fields.update(external_coverage)
    coverage_document["fields"] = source_fields
    coverage_document["externalBenchmarks"] = {
        "livebench": {
            "release": livebench_document["release"],
            "matchedN": livebench_document["matchedN"],
            "cohortN": livebench_document["cohortN"],
            "publishedN": livebench_document.get("publishedN", livebench_document["matchedN"]),
            "supplementalMatchedN": livebench_document.get("supplementalMatchedN", 0),
            "supplementalModels": list(livebench_document.get("supplementalModels", {})),
            "pareto": livebench_document["pareto"],
        },
        "terminalBenchV4": {
            "version": tb4_document["version"],
            "matchedN": tb4_document["matchedN"],
            "providerClaimN": tb4_document.get("providerClaimN", 0),
            "rankingAvailableN": tb4_document.get("rankingAvailableN", tb4_document["matchedN"]),
            "cohortN": tb4_document["cohortN"],
        },
        "bugHunt": {
            "version": bug_hunt_document["benchmarkVersion"],
            "sourceCommit": bug_hunt_document["sourceCommit"],
            "matchedN": len(bug_hunt_owner_matches),
            "rankableOverlapN": len(overlap_primary_ids),
            "sourceCohortN": len(rows),
            "primaryCohortN": len(primary_rows),
            "sourceCoveragePct": round(100 * len(bug_hunt_owner_matches) / len(rows), 2),
            "primaryCoveragePct": round(100 * len(primary_bug_hunt_matches) / len(primary_rows), 2),
            "primaryWeightPct": bug_hunt_primary_weight_pct,
            "emphasisWeightPct": bug_hunt_emphasis["benchmarkWeightPct"],
        },
    }
    coverage_document["scoring"] = {
        "version": VERSION,
        "cohortN": len(primary_rows),
        "scoredN": len(by_overall),
        "exactBenchmarkOverlapN": len(overlap_primary_ids),
        "frontierRequiredModelN": len(frontier_primary_ids),
        "frontierRequiredModelIds": sorted(frontier_primary_ids),
        "frontierSelection": frontier_selection,
        "sourceCohortN": len(rows),
        "rankingExcludedModels": [row["name"] for row in unranked_rows],
        "rankingExclusions": [
            {"modelId": row["id"], "name": row["name"], "reasons": row["rankingExclusionReasons"]}
            for row in unranked_rows
        ],
        "costMode": cost_mode,
        "costCoverage": {
            "availableN": len(aa_cost_rows),
            "cohortN": len(primary_rows),
            "sourceAvailableN": sum(row["aaEvalCost"] is not None for row in rows),
            "sourceCohortN": len(rows),
            "missingModels": [row["name"] for row in primary_rows if row["aaEvalCost"] is None],
            "sourceMissingModels": [row["name"] for row in rows if row["aaEvalCost"] is None],
            "selectiveSubstitution": False,
        },
        "retainedDimensions": [weight["key"] for weight in weights],
        "droppedDimensions": dropped,
        "zeroGap": (
            not dropped
            and not any(
                item["missingModels"]
                for item in score_coverage.values()
                if item["includedInPrimaryScore"]
            )
        ),
        "noNeutralFills": True,
        "fields": score_coverage,
        "alternateRankings": {
            "bugHuntEmphasis": {
                "matchedN": bug_hunt_emphasis["matchedN"],
                "cohortN": bug_hunt_emphasis["cohortN"],
                "benchmarkWeightPct": bug_hunt_emphasis["benchmarkWeightPct"],
                "sourceCommit": bug_hunt_emphasis["sourceCommit"],
                "ranking": [
                    {"rank": item["rank"], "modelId": item["modelId"], "score": item["emphasisScore"]}
                    for item in bug_hunt_emphasis["ranking"]
                ],
            }
        },
    }

    observed_at = iso_z()
    ranking_summary = {
        "version": VERSION,
        "publishDate": PUBLISH_DATE,
        "observedAt": observed_at,
        "cohortN": len(primary_rows),
        "scoredN": len(by_overall),
        "exactBenchmarkOverlapN": len(overlap_primary_ids),
        "frontierRequiredModelN": len(frontier_primary_ids),
        "frontierSelection": frontier_selection,
        "sourceCohortN": len(rows),
        "rankingExcludedModels": [row["name"] for row in unranked_rows],
        "rankingExclusions": coverage_document["scoring"]["rankingExclusions"],
        "deepsweSource": deepswe_chart["source"],
        "deepsweObservedAt": deepswe_chart["observedAt"],
        "deepsweBenchmarkVersion": deepswe_chart["benchmark"],
        "deepsweConfigurationsN": len(deepswe_chart["configurations"]),
        "aaBenchmarkVersion": aa_document.get("benchmarkVersion"),
        "retainedDimensionN": len(weights),
        "retainedDimensions": [weight["label"] for weight in weights],
        "droppedDimensions": dropped,
        "zeroGap": coverage_document["scoring"]["zeroGap"],
        "costMode": cost_mode,
        "costCoverage": coverage_document["scoring"]["costCoverage"],
        "pareto": pareto,
        "topFive": [
            {"rank": row["rank"], "name": row["name"], "overallScore": row["overallScore"], "qualityScore": row["qualityScore"]}
            for row in by_overall[:5]
        ],
        "bugHuntEmphasis": {
            "matchedN": bug_hunt_emphasis["matchedN"],
            "cohortN": bug_hunt_emphasis["cohortN"],
            "benchmarkWeightPct": bug_hunt_emphasis["benchmarkWeightPct"],
            "sourceCommit": bug_hunt_emphasis["sourceCommit"],
            "topFive": [
                {"rank": item["rank"], "name": item["name"], "score": item["emphasisScore"], "fixedOf105": item["fixedOf105"]}
                for item in bug_hunt_emphasis["ranking"][:5]
            ],
        },
        "externalCoverage": {
            "livebench": f"{livebench_document['matchedN']}/{livebench_document['cohortN']}",
            "livebenchPublishedN": livebench_document.get("publishedN", livebench_document["matchedN"]),
            "livebenchSupplementalModels": list(livebench_document.get("supplementalModels", {})),
            "bugHunt": (
                f"{len(bug_hunt_owner_matches)}/{len(rows)} owner matches; "
                f"{len(overlap_primary_ids)} exact DeepSWE and Bug Hunt overlaps plus "
                f"{len(frontier_primary_ids)} selected AA frontier family models enter the primary cohort"
            ),
            "terminalBenchV4": f"{tb4_document.get('rankingAvailableN', tb4_document['matchedN'])}/{tb4_document['cohortN']} including {tb4_document.get('providerClaimN', 0)} provider claim",
        },
    }
    manifest_path = data / "run_manifest.json"
    manifest = json.loads(manifest_path.read_text())
    manifest["scoring"] = ranking_summary
    manifest["scoring"]["weights"] = weights
    manifest["scoring"]["bugHuntEmphasisRanking"] = bug_hunt_emphasis
    manifest["scoring"]["primaryMissingFields"] = {
        key: data["missing"] for key, data in coverage.items() if data["missing"]
    }
    manifest["scoring"]["providerClaimsUsed"] = [
        {"model": row["name"], "benchmark": "Terminal-Bench 4.0", "sourceUrl": row["terminalBenchV4Claim"]["sourceUrl"]}
        for row in primary_rows if row.get("terminalBenchV4Claim")
    ]

    v3_section = value_v3.build(
        # E187: the frontier-family flag rides with each configuration, so the frontier-families diagnostics exclude retained rows.
        [value_v3.configuration(row) for row in by_overall + unscored_primary_rows],
        data,
        release_day=utcnow().date(),
    )

    (data / "scores.json").write_text(
        json.dumps(
            {
                "version": VERSION,
                "publishDate": PUBLISH_DATE,
                "observedAt": observed_at,
                "benchmarkVersion": aa_document.get("benchmarkVersion"),
                "deepsweBenchmarkVersion": deepswe_chart["benchmark"],
                "deepsweSource": deepswe_chart["source"],
                "deepsweConfigurationsN": len(deepswe_chart["configurations"]),
                "deepsweObservedConfigurationN": observed_configuration_n,
                "cohort": {
                    "n": len(primary_rows),
                    "scoredN": len(by_overall),
                    "sourceN": len(rows),
                    "exactBenchmarkOverlapN": len(overlap_primary_ids),
                    "frontierRequiredModelN": len(frontier_primary_ids),
                    "source": "Artificial Analysis Coding Agent Index v1.5 DeepSWE v1.1 chart",
                    "sourceUpdatedOn": deepswe_chart["observedAt"],
                },
                "frontierSelection": frontier_selection,
                "weights": weights,
                "bugHuntEmphasisRanking": bug_hunt_emphasis,
                "costMode": cost_mode,
                "costCoverage": coverage_document["scoring"]["costCoverage"],
                "models": by_overall + unscored_primary_rows + sorted(unranked_rows, key=lambda row: row["name"]),
                "rankedModelIds": [row["id"] for row in by_overall],
                "pareto": pareto,
                "externalBenchmarks": {
                    "livebench": {
                        "release": livebench_document["release"],
                        "matchedN": livebench_document["matchedN"],
                        "cohortN": livebench_document["cohortN"],
                        "publishedN": livebench_document.get("publishedN", livebench_document["matchedN"]),
                        "supplementalMatchedN": livebench_document.get("supplementalMatchedN", 0),
                        "supplementalModels": list(livebench_document.get("supplementalModels", {})),
                        "pareto": livebench_document["pareto"],
                    },
                    "terminalBenchV4": {
                        "version": tb4_document["version"],
                        "matchedN": tb4_document["matchedN"],
                        "providerClaimN": tb4_document.get("providerClaimN", 0),
                        "rankingAvailableN": tb4_document.get("rankingAvailableN", tb4_document["matchedN"]),
                        "cohortN": tb4_document["cohortN"],
                    },
                    "bugHunt": {
                        "version": bug_hunt_document["benchmarkVersion"],
                        "matchedN": len(bug_hunt_owner_matches),
                        "rankableOverlapN": len(overlap_primary_ids),
                        "cohortN": len(rows),
                        "primaryCohortN": len(primary_rows),
                        "primaryCoveragePct": round(100.0 * len(primary_bug_hunt_matches) / len(primary_rows), 2),
                        "primaryWeightPct": bug_hunt_primary_weight_pct,
                        "sourceCommit": bug_hunt_document["sourceCommit"],
                    },
                },
                "appendixNonRanked": [
                    {
                        "id": row["id"],
                        "name": row["name"],
                        "reason": "; ".join(row["rankingExclusionReasons"]),
                    }
                    for row in unranked_rows
                ],
                "v3": v3_section,
            },
            indent=2,
            ensure_ascii=False,
        )
        + "\n"
    )
    (data / "coverage_matrix.json").write_text(json.dumps(coverage_document, indent=2, ensure_ascii=False) + "\n")
    (data / "ranking_summary.json").write_text(json.dumps(ranking_summary, indent=2, ensure_ascii=False) + "\n")
    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n")

    print(json.dumps({
        "version": VERSION,
        "n": len(primary_rows),
        "sourceN": len(rows),
        "retainedDimensions": len(weights),
        "dropped": dropped,
        "zeroGap": ranking_summary["zeroGap"],
        "topFive": ranking_summary["topFive"],
        "bugHuntEmphasisTopFive": ranking_summary["bugHuntEmphasis"]["topFive"],
        "outputs": [
            "data/scores.json",
            "data/coverage_matrix.json",
            "data/ranking_summary.json",
        ],
    }, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
