#!/usr/bin/env python3
"""Emit the Markdown publication for methodology v3: README, methodology, score tables and raw data.

Every number comes from the ``v3`` section of ``data/scores.json``, read through the site view model
(``valuerank.site.viewmodel.build_bundle``) so the Markdown and the website state the same values.
The website under site/ is owned by ``python -m valuerank.site.build``.
"""

from __future__ import annotations

import json
import statistics
from datetime import date

from valuerank import basket
from valuerank import exact_match
from valuerank import plan_routes
from valuerank import quality as q
from valuerank import scenarios
from valuerank import value_v3
from valuerank.aa_reconciliation import publication as aa_reconciliation_publication, reconcile as reconcile_aa
from valuerank.paths import DATA, ROOT
from valuerank.publication import (
    AA_CODING_AGENTS_URL,
    AA_DEEPSWE_URL,
    AA_METHODOLOGY_URL,
    BUG_HUNT_URL,
    TERMINAL_BENCH_URL,
    model_inclusion,
    plan_evidence_label,
)
from valuerank.release import DATE, VERSION
from valuerank.site import viewmodel

DASH = "—"
SITE_URL = "https://valuerank.alolabs.dev"
SPEC_DIR = "research/2026-10-19-methodology-codesign/"
SEMIANALYSIS_URL = "https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x"
OUTPUTS = ("README.md", "methodology.md", "scores.md", "raw-data.md")
# Cohort routes, in the order a row is classified (a row can carry several inclusion reasons).
COHORT_ROUTES = (
    ("Required AA Intelligence Index versus total-evaluation-cost frontier family", "On AA's rendered frontier"),
    ("Near-frontier AA family", "Near-frontier family"),
    ("Plotted on or within the near gap of AA's rendered frontier (O51)", "Plotted on or near AA's rendered frontier, another effort of a frontier or near family (O51)"),
)
LEAF_TRANSFORMS = {
    "bugHunt": "z = 100 × bugs fixed / 105",
    "frontierCode": "z = 100 × score",
    "terminalBench": "z = resolution %",
    "gdpval": "z = 100 × (Elo − 500) / 2000 (AA's integration transform)",
    "automationBench": "z = 100 × score",
    "omniscience": "z = (I + 100) / 2 on AA's Omniscience Index I (O28)",
    "lcr": "z = 100 × accuracy",
    "hle": "z = 100 × accuracy",
    "scicode": "z = 100 × score",
    "critpt": "z = 100 × score",
    "vibeCode": "z = pass rate %",
    "codeMigration": "z = pass rate %",
    "livebench2Overall": "z = LiveBench's weighted Overall of the seven category scores (release 2026-10-23, O67)",
    "aiCodingDaily": "z = 100 × points / 60",
}
SOURCE_LABELS = {"aa": "AA-run", "independent": "independent"}
SOURCE_TYPE_LABELS = {"aa_recapture": "newer AA capture", "independent": "independent run", "model_provider_claim": "model-provider result"}
LEAF_SEARCH_DAYS = value_v3.LEAF_SEARCH_MAX_AGE_DAYS
# Owner-authorised route applications in the Plan evidence policy, printed when recorded.
POLICY_APPLICATIONS = (
    ("gptApplication", "GPT"),
    ("claudeApplication", "Claude"),
    ("mimoApplication", "MiMo"),
    ("unsupportedModels", "Other models"),
    # I78 L5: the registry's statement of owner decisions O72 onwards, rendered as it is recorded.
    ("o72Application", "Plan evidence after the O71 search"),
)
CHARGE_LABELS = {
    "contestantModelTokens": "Contestant tokens",
    "otherModelCalls": "Other model calls",
    "externalTools": "External tools",
    "executionEnvironment": "Execution environment",
    "preparation": "Preparation",
    "grading": "Grading",
}
FLAG_LEGEND = (
    ("subset cost", "scored on the workload of the components it has, against that workload's own anchors; its ordering against main-workload rows is not identified (O17)"),
    ("provider-claimed leaf", "a quality leaf comes from the model provider's own published result (O36's last source); the row competes but earns no interval label (E233)"),
    ("provisional quality", "observed leaves cover under 70% of quality weight, fewer than two software-engineering leaves or under 40% software-engineering weight are observed, or a leaf weighing 20% or more of its ranking's quality is missing; ranked and flagged, never floored (O8)"),
    ("partial component", "AA marks tasks of a basket component missing or declined (E37), or the component's cost cannot be reconciled with AA's prices (E170)"),
    ("valuation basis unverified", "AA's cost reconciles with neither its displayed prices nor a registered price record; ranked, but outside interval outputs and cost anchors (E170 outcome 4)"),
    ("no cost", "AA publishes no cost for the configuration, so it has no value score and no rank (AGENTS.md); its quality is shown"),
    ("AA cost caveat", "AA states that its published cost omits a pricing term"),
    ("API-cost fallback", "no admitted Plan route; the Plan ranking uses the API cost (O13)"),
    # I78 L5: the selected Plan route's own lifecycle flags, so every human-readable ranking shows them.
    ("route possibly superseded", "the selected Plan route's evidence (or its donor's) may be superseded by age or a detected change (E18, E151, O77-O79); it stays selected and earns no interval label (E228)"),
    ("fault window", "the selected Plan route rests on a controlled measurement inside an acknowledged accounting-fault window; it stays selected until two concordant user reports for its plan replace it (O91, O92, O93)"),
)


# --- formatting helpers ----------------------------------------------------------------------


def fnum(value, places=2, dash=DASH):
    return f"{value:.{places}f}" if isinstance(value, (int, float)) else dash


def pct(value, places=2):
    """A fraction as a percentage."""

    return f"{value * 100:.{places}f}%" if isinstance(value, (int, float)) else DASH


def usd(value, places=2):
    return f"${value:,.{places}f}" if isinstance(value, (int, float)) else DASH


def names(values):
    return ", ".join(values) if values else "none"


def series(values):
    """``a``, ``a and b``, ``a, b and c``."""

    return " and ".join([", ".join(values[:-1]), values[-1]]) if len(values) > 1 else names(values)


def markdown_table(headers, rows, numeric=()):
    """A Markdown table; ``numeric`` holds the indices of right-aligned columns. Pipes and newlines in cells are escaped."""

    def clean(value):
        return str(value).replace("|", "\\|").replace("\n", " ")

    rule = ["---:" if index in numeric else "---" for index in range(len(headers))]
    lines = ["| " + " | ".join(headers) + " |", "|" + "|".join(rule) + "|"]
    lines += ["| " + " | ".join(clean(value) for value in row) + " |" for row in rows]
    return "\n".join(lines)


def model_inclusion_markdown(inclusion, level="##"):
    lines = [
        f"{level} Model inclusion",
        "",
        f"**Frontier rule.** {inclusion['frontierRule']}",
        "",
        f"**Near-frontier rule.** {inclusion['nearFrontierRule']}",
    ]
    if inclusion["policyText"]:
        lines += ["", f"Policy as recorded: {inclusion['policyText']}"]
    for text in (inclusion["observation"], inclusion["nearFrontierStatus"]):
        if text:
            lines += ["", text]
    if inclusion["frontierFamilies"]:
        lines += ["", "Frontier families and the configuration selected for each:", ""]
        lines += [f"- {item['family']}: {item['configuration']}" for item in inclusion["frontierFamilies"]]
    if inclusion["nearFrontierFamilies"]:
        lines += ["", "Near-frontier families and each family's near point closest to the frontier (every configuration AA plots on or near the frontier is a cohort row, each effort its own row, O51; a family's primary configuration is its near point closest to the frontier, E193):", ""]
        lines += [
            f"- {item['family']}: {item['configuration']}, {item['gap']} Index point{'' if item['gap'] == '1' else 's'} below the frontier"
            for item in inclusion["nearFrontierFamilies"]
        ]
    for note in inclusion["footnotes"]:
        lines += ["", f"AA footnote ({', '.join(note['models'])}): {note['text']}"]
    return "\n".join(lines) + "\n"


def tb4_table(tb4_rows):
    return "\n".join(
        f"| {entry['rankLabel']} | {entry['baseModel']} | {entry['agent']} | {entry['resolutionRatePct']:.1f}% ± {entry['uncertaintyPct']:.1f}% | {entry['tokens']} | {'—' if entry['costUsd'] is None else f"${entry['costUsd']:,.0f}"} |"
        for entry in tb4_rows
    )


def deepswe_chart_table(deepswe_configurations):
    return "\n".join(
        f"| {item['sourceOrder']} | {item['agent']} | {item['model']} | {item.get('effort') or 'not shown'} | "
        f"{item['scorePct']:.1f}% | "
        f"{'Exact: ' + item['valueRankModelId'] if item.get('valueRankModelId') else item['matchStatus'].replace('_', ' ')} | "
        f"{item.get('matchNote', '—')} |"
        for item in deepswe_configurations
    )


def configuration_label(row, names_by_id):
    """``Name (effort)``: the configuration a v3 row scores. A sibling effort's name already ends with it (O33)."""

    name = names_by_id[row["id"]]
    suffix = f" ({row['effort']})" if row.get("effort") else ""
    return name if name.endswith(suffix) else name + suffix


def model_link(entry, label=None):
    return f"[{label or entry['name']}]({SITE_URL}/models/{entry['slug']}/)"


def rank_text(rank):
    return DASH if rank is None else rank


def workload_text(entry):
    """The workload a row is scored on; a row without a cost has none."""

    if entry["cost"]["apiUsd"] is None:
        return DASH
    return "subset" if entry["cost"]["subset"] else "main"


def short_flags(entry, row):
    """The row's flags as the short words of ``FLAG_LEGEND``, in the legend's order."""

    cost = entry["cost"]
    present = {
        "subset cost": cost["subset"] and cost["apiUsd"] is not None,
        "provider-claimed leaf": any(leaf.get("sourceType") == "model_provider_claim" for leaf in (row.get("quality") or {}).get("leaves", {}).values()),
        "provisional quality": entry["coverage"]["provisional"],
        "partial component": bool(cost["partialComponents"]),
        "valuation basis unverified": (row.get("valuationGate") or {}).get("outcome") == "valuation basis unverified" and cost["apiUsd"] is not None,
        "no cost": cost["apiUsd"] is None,
        "AA cost caveat": bool(row.get("aaCostCaveat")),
        "API-cost fallback": cost["fallback"] is not None,
        "route possibly superseded": bool({"possibly-superseded", "expired"} & set((row.get("plan") or {}).get("flags", []))),
        "fault window": plan_routes.FAULT_FLAG in (row.get("plan") or {}).get("flags", []),
    }
    return ", ".join(word for word, _text in FLAG_LEGEND if present[word]) or DASH


def basket_runs_text(amount, api_cost):
    """I27: basket runs one fee period buys at full utilisation, the selected amount over the basket's API cost (O3)."""

    if not amount or amount.get("amountUsd") is None or not api_cost:
        return DASH
    return f"{amount['amountUsd'] / api_cost:.2f} per {amount['feePeriod']}"


def plan_amount_text(amount):
    """E166: the selected route's amount with its kind; none for API-fallback rows."""

    if amount is None:
        return DASH
    value = f"{usd(amount['amountUsd'], 0)} per {amount['feePeriod']}: " if amount["amountUsd"] is not None else "fee not established: "
    return value + amount["amountKind"] + (f" from {amount['donorRouteId']}" if amount["donorRouteId"] else "")


def route_text(entry):
    route = entry["cost"]["route"]
    if route is None:
        return DASH
    return f"{route['planLabel']} ({route['valueMultiple']:g}×, {route['grade']})"


def share(value):
    return f"{100 * value:.1f}%"


def component_label(key):
    return basket.COMPONENT_LABELS.get(key, key)


# --- shared facts ----------------------------------------------------------------------------


class Facts:
    """Everything the four documents quote, computed once from one data directory."""

    def __init__(self, data, track=None):
        # O53: one Facts per ranking; the leading ranking's Facts carries the others in ``tracks``.
        self.track = track or q.DEFAULT_TRACK
        self.bundle = viewmodel.build_bundle(data, track)
        self.scores = json.loads((data / "scores.json").read_text())
        self.routes_document = json.loads((data / "plan_cost_routes.json").read_text())
        self.deepswe = json.loads((data / "aa_deepswe.json").read_text())
        self.tb4 = json.loads((data / "tb4.json").read_text())
        self.leaf_evidence = json.loads((data / "leaf_evidence.json").read_text())
        self.bug_hunt = json.loads((data / "bug_hunt.json").read_text())
        self.v3 = self.scores["v3"] if self.track == q.DEFAULT_TRACK else self.scores["v3Tracks"][self.track]
        self.rows = {row["id"]: row for row in self.v3["rows"]}
        self.names = {model["id"]: model["name"] for model in self.scores["models"]}
        self.rankings = self.bundle.rankings
        self.ranked = [entry for entry in self.rankings["models"] if entry["rankingEligible"]]
        self.unranked = [entry for entry in self.rankings["models"] if not entry["rankingEligible"]]
        self.method = self.bundle.extras["method"]
        self.inclusion = model_inclusion(self.scores.get("frontierSelection"), self.scores["models"])
        self.cost_pct = self.rankings["costWeightPct"]
        self.quality_pct = 100.0 - self.cost_pct
        self.tracks = {}
        if track is None:
            reconciliation, _html = aa_reconciliation_publication(reconcile_aa(data=data))
            self.reconciliation_md = reconciliation
            for other in q.TRACKS:
                if other != q.DEFAULT_TRACK:
                    with q.active_track(other):
                        self.tracks[other] = Facts(data, other)

    def row(self, entry):
        return self.rows[self.source_id(entry)]

    def source_id(self, entry):
        return next(model["id"] for model in self.scores["models"] if viewmodel.slugify(model["id"]) == entry["slug"])

    def label(self, model_id):
        if model_id not in self.rows and "@" in model_id:
            # O48: a Plan row "<configuration>@<plan>" reads as the configuration on its plan.
            configuration, slug = model_id.split("@", 1)
            # O91: a frozen anchor setter may be a plan row no longer in the table; its plan is named from the route registry,
            # and only the API-fallback slug reads as an API-cost fallback.
            plans = {value_v3.plan_slug(route["plan"]): route["plan"] for route in self.routes_document["routes"] if route.get("plan")}
            return f"{self.label(configuration)} on {'API-cost fallback' if slug == value_v3.API_FALLBACK_PLAN else plans.get(slug, slug)}"
        return configuration_label(self.rows[model_id], self.names) if model_id in self.rows else self.names.get(model_id, model_id)

    def labels(self, model_ids):
        return names([self.label(model_id) for model_id in model_ids])

    def cohort_route(self, model_id):
        reasons = next(model for model in self.scores["models"] if model["id"] == model_id).get("rankingInclusionReasons") or []
        for prefix, label in COHORT_ROUTES:
            if any(reason.startswith(prefix) for reason in reasons):
                return label
        raise ValueError(f"ranked configuration {model_id} has no recorded cohort inclusion reason")


# --- interval and scenario summaries ----------------------------------------------------------


def interval_sentences(facts):
    """Plain sentences for the interval outputs of both bases (E21, E38)."""

    sentences = []
    for basis, label in (("api", "API"), ("plan", "Plan")):
        result = facts.v3["intervals"][basis]
        if result["status"] != "evaluated":
            sentences.append(f"{label} basis: interval outputs not evaluated ({result.get('reason', result['status'])}).")
            continue
        frontier = result["frontier"]
        definite = [row_id for row_id, item in frontier.items() if item.get("definite") == "certified"]
        possible = [row_id for row_id, item in frontier.items() if item.get("possible") == "certified" and item.get("definite") != "certified"]
        text = (
            f"{label} basis, main workload: the definite frontier (no configuration can beat it on both cost and quality anywhere "
            f"inside the published record's precision and missing-evidence bounds) is {facts.labels(definite)}; "
            f"the possible frontier adds {facts.labels(possible)}."
        )
        if result["unevaluable"]:
            text += f" Not evaluable on this workload: {facts.labels(result['unevaluable'])}."
        if result.get("blockers"):
            text += f" Competing without a label (AA cost on a price not in force, O29): {facts.labels(result['blockers'])}."
        for bar in result.get("bars", []):
            reference = bar_name(bar["reference"])
            if bar["status"] != "certified":
                text += f" Cheapest at or above {reference}: {bar['status']}."
            elif bar["confirmedCheapest"]:
                text += f" Cheapest at or above {reference}: {facts.label(bar['confirmedCheapest'])} (confirmed)."
            else:
                text += f" Cheapest at or above {reference}: not unique; possibly {facts.labels(bar['possibleCheapest'])}."
            if bar["status"] == "certified":
                text += f" (Bar comparison: {bar['comparison']}.)"
        sentences.append(text)
    return sentences


CODING_COMPONENTS = ("coding-agent-index", "terminalbench-4-0", "scicode")
# Basket components priced in the cost but with no quality leaf of their own (E203 disclosure; O6 and O15 stand).
UNREWARDED_COMPONENTS = ("aa-briefcase", "gdp-pdf")


def _median_share(v3, keys):
    shares = [
        sum(row["cost"]["componentsDetail"][key]["costUsd"] for key in keys if key in row["cost"]["components"]) / row["cost"]["costUsd"]
        for row in v3["rows"] if row["cost"]["fullCost"] and row["cost"]["costUsd"]
    ]
    return (statistics.median(shares), min(shares), max(shares), len(shares)) if shares else None


def coding_share_text(v3):
    """E200: the share of the basket's cost that coding and terminal tasks carry, beside the basket label."""

    coding = _median_share(v3, CODING_COMPONENTS)
    if coding is None:
        return ""
    middle, low, high, n = coding
    admitted = v3["admission"]["admitted"]
    labels = ", ".join(component_label(key) for key in CODING_COMPONENTS if key in admitted)
    unrewarded = _median_share(v3, UNREWARDED_COMPONENTS)[0]
    # The Coding Agent Index's SWE-Atlas QnA has no quality leaf; its share is only stated while the index is in the basket (O50).
    atlas = (f"; the Coding Agent Index's SWE-Atlas QnA ({basket.CODING_AGENT_TASKS['swe-atlas-qna']} of its {sum(basket.CODING_AGENT_TASKS.values())} "
             "tasks) has no quality leaf either, and its cost share is not separable because AA publishes one pooled cost"
             if basket.CODING_AGENT_INDEX in admitted else "")
    return (f" Coding and terminal tasks ({labels}) make up {pct(middle, 0)} of the basket's cost (median over {n} configurations "
            f"with the full basket; {pct(low, 0)} to {pct(high, 0)}); {', '.join(component_label(key) for key in UNREWARDED_COMPONENTS)}, "
            f"which have no quality leaf, make up {pct(unrewarded, 0)}{atlas}.")


def influence_text(v3, short=False):
    """E196: cost's nominal weight beside its share of the variance in value on the common panel (E189)."""

    shares = {basis: (v3["costInfluence"][basis]["commonWorkload"]["varianceAllocation"] or {}).get("cost") for basis in ("api", "plan")}
    if None in shares.values():
        return ""
    if short:
        return f"; {pct(shares['api'], 0)} of API and {pct(shares['plan'], 0)} of Plan value variance"
    if max(shares.values()) > 1:
        # E196 (I47 L1): above 100% the quality term is negative: cheaper configurations score higher on quality, so quality offsets cost.
        return (f" That weight is nominal: on the current panel cost's covariance allocation of value variance is {pct(shares['api'], 0)} on the API basis "
                f"and {pct(shares['plan'], 0)} on the Plan basis; an allocation above 100% means quality's is negative: dearer configurations score "
                "higher on quality, so the quality differences partly offset the cost differences instead of adding spread of their own (see [methodology.md](methodology.md)).")
    if min(shares.values()) < 0:
        # The covariance allocation is negative when dearer configurations score higher on quality: cost then offsets quality.
        return (f" That weight is nominal: on the current panel cost's covariance allocation of value variance is {pct(shares['api'], 0)} on the API basis "
                f"and {pct(shares['plan'], 0)} on the Plan basis; a negative allocation means dearer configurations score higher on quality, so cost "
                "offsets quality differences instead of adding spread of its own (see [methodology.md](methodology.md)).")
    return (f" That weight is nominal: on the current panel cost accounts for {pct(shares['api'], 0)} of the variance in API value and "
            f"{pct(shares['plan'], 0)} in Plan value, because cost scores spread more than quality scores (see [methodology.md](methodology.md)).")


def policy_bar_text(policy, facts):
    """E199: the bar recomputed over the frontier and near-frontier configurations alone, as a sensitivity."""

    head = "- **Frontier-families bar (E199, sensitivity; the frozen bar stays primary):** "
    if policy["status"] != "evaluated":
        return head + policy["status"] + "."
    result, text = policy["api"], f"{bar_name(policy['bar'])} over {len(policy['population'])} configurations"
    if result["status"] != "certified":
        return head + f"{text}; API main workload {result['status']}."
    answer = f"{facts.label(result['confirmedCheapest'])} (confirmed)" if result["confirmedCheapest"] else f"not unique; possibly {facts.labels(result['possibleCheapest'])}"
    return head + f"{text}; cheapest at or above it on the API main workload: {answer} ({result['comparison']})."


def costed_ladder_text(diagnostic, facts):
    """I28: the ladder over scored rows alone, beside the frozen ladder whose population keeps costless rows by choice."""

    head = "- **Ladder over scored rows (I28, sensitivity; the frozen ladder stays primary):** the bar population keeps full-benchmark rows that have no cost"
    if not diagnostic["excluded"]:
        return head + "; today every such row has a cost, so the ladder is unchanged."
    ladder = " / ".join(f"{level:.1f}" for level in diagnostic["levels"]) or "unavailable"
    return head + f" ({facts.labels(diagnostic['excluded'])}); without them ({diagnostic['population']} rows) the ladder (headline, lower quartile, upper quartile) would be {ladder}."


def family_primary_text(diagnostic, facts):
    """E205: the ladder and anchors with one row per family, beside the frozen ones (a diagnostic)."""

    head = "- **One row per family (E205, diagnostic; the frozen ladder and anchors stay primary):** "
    ladder = " / ".join(f"{item['level']:.1f}" for item in diagnostic["ladder"]) or "unavailable"
    frozen = " / ".join(f"{item['level']:.1f}" for item in diagnostic["frozenLadder"]) or "unavailable"
    text = head + f"with each family's primary configuration only ({len(diagnostic['population'])} rows in the one-row-per-family bar population), the ladder (headline, lower quartile, upper quartile) would be {ladder} against {frozen} frozen"
    if diagnostic["status"] != "evaluated":
        return text + f"; anchors {diagnostic['status']}."
    return text + "; anchors rebuilt from its " + f"{len(diagnostic['references'])} references move " + "; ".join(
        f"{label} {rank_change_text(diagnostic['bases'][basis]['rankChanges']['changes'], facts.labels)} (value points per cost doubling "
        f"{fnum(diagnostic['bases'][basis]['exchangeRate']['valuePointsPerCostDoubling'], 2)} vs {fnum(diagnostic['bases'][basis]['frozenExchangeRate']['valuePointsPerCostDoubling'], 2)} frozen)"
        for basis, label in (("api", "API"), ("plan", "Plan"))
    ) + "."


def search_gap_text(policy):
    """E213: the days between the evidence search cutoff and the release cutoff, which no report search covered."""

    searched, end = policy.get("searchCutoff"), policy["reportingWindow"]["end"]
    if not searched or searched >= end:
        return ""
    gap = (date.fromisoformat(end) - date.fromisoformat(searched)).days
    return f"; end-user reports were last searched on {searched}, so reports dated in the {gap} days after it were not searched"


def cross_harness_text(facts):
    """E224: configurations Bug Hunt reports on two or more harnesses at the same effort (a diagnostic, no score change)."""

    parts = [f"{facts.names.get(row['id'], row['id'])}: " + ", ".join(f"{item['harness']} {fnum(item['fixedOf105'], 1)} ({item['runs']} run{'s' if item['runs'] != 1 else ''})" for item in row["bugHuntCrossHarness"])
             for row in facts.scores["models"] if row.get("rankingEligible") and row.get("bugHuntCrossHarness")]
    return ("Cross-harness results at the same effort (E224, diagnostic): " + "; ".join(parts) + ".") if parts else "No ranked configuration has Bug Hunt results on two harnesses at the same effort (E224)."


def selected_agents_text(facts, tb4):
    """E225/O37: how many cohort rows each registered tbench.ai agent matches (the cross-check and gap-fill pool)."""

    counts = {}
    for row in facts.scores["models"]:
        if row.get("rankingEligible"):
            chosen = exact_match.select_tb4_row(row["id"], row.get("aaVariant"), tb4["rows"])
            if chosen is not None:
                counts[chosen["agent"]] = counts.get(chosen["agent"], 0) + 1
    order = ", ".join(f"{agent} {counts[agent]}" for agent in exact_match.TB4_AGENT_PREFERENCE if agent in counts)
    return (f"Since O37 the Terminal-Bench leaf is AA's own run; these rows cross-check it and fill a gap. Matched agents for cohort rows, "
            f"in the registered preference order (E225): {order or 'none'}.")


def bar_currency_text(currency):
    """E207: how many bar-population rows reach each frozen bar now, the ladder this population would freeze, and the flag."""

    reach = "; ".join(f"{bar_name(item)}: {item['reachN']} of {item['populationN']}" for item in currency["bars"]) or "no bar frozen"
    ladder = " / ".join(f"{item['level']:.1f}" for item in currency["currentLadder"]) or "unavailable"
    return (f"- **Bar currency (E207, informational):** rows reaching each frozen bar: {reach}; the current population would freeze {ladder}; "
            f"lifetime {currency['lifetime']}; " + (f"flag: {currency['flag']}." if currency["flag"] else "no staleness flag."))


def observed_range_text(result, facts):
    """E219: the API bar results with missing leaves bounded by the cohort's observed range (a sensitivity, not evidence)."""

    head = "- **Observed-range sensitivity (E219, not evidence; no label changes):** "
    if result["status"] != "evaluated":
        return head + result["status"] + "."
    parts = []
    for bar in result["bars"]:
        level = next(item["level"] for item in facts.v3["barPolicy"]["bars"] if item["id"] == bar["bar"])
        answer = facts.label(bar["confirmedCheapest"]) + " confirmed cheapest" if bar["confirmedCheapest"] else f"possibly cheapest {facts.labels(bar['possibleCheapest'])}"
        parts.append(f"quality {level:.1f}: {bar['possibleQualifierN']} can qualify, {bar['confirmedQualifierN']} confirmed; {answer}")
    return head + "with each missing leaf inside the cohort's observed range for that leaf, " + "; ".join(parts) + "."


def required_scores_text(result, facts):
    """E221: for the headline bar, what each open row's missing leaves would need to average (not a claim)."""

    head = "- **What would settle the headline bar (E221, not a claim):** "
    if result["status"] != "evaluated" or not result["bars"]:
        return head + (result["status"] if result["status"] != "evaluated" else "no bar") + "."
    bar = result["bars"][0]
    parts = [f"{facts.label(item['row'])} {fnum(item['required'], 1)} ({', '.join(LEAF_LABELS[key] for key in item['missing'])})" if item["required"] is not None
             else f"{facts.label(item['row'])} (no missing leaf; reporting precision only)" for item in bar["rows"]]
    return head + (f"rows that can but need not reach quality {bar['level']:.1f}, with the mean score their missing leaves would need: " + "; ".join(parts) + "."
                   if parts else f"no row is open at quality {bar['level']:.1f}.")


def common_leaf_text(diagnostic, facts):
    """E226: the leaf-availability effect: quality on the leaves (nearly) every row has, beside the displayed quality."""

    sparse = ", ".join(LEAF_LABELS[key] for key in diagnostic["sparseLeaves"]) or "none"
    reach = "; ".join(f"quality {item['level']:.1f}: {item['displayedReachN']} → {item['commonLeafReachN']}" for item in diagnostic["barReach"])
    moves = "; ".join(f"{label} {rank_change_text(diagnostic['bases'][basis]['rankChanges']['changes'], facts.labels)}" for basis, label in (("api", "API"), ("plan", "Plan")))
    flagged = ", ".join(f"{facts.label(row_id)} {fnum(diagnostic['rows'][row_id]['effect'], 1)}" for row_id in diagnostic["flagged"]) or "none"
    return (f"- **Common leaf set (E226, diagnostic; scores unchanged):** without the leaves fewer than 90% of cohort rows have ({sparse}), {moves}; "
            f"rows reaching each bar: {reach}; rows whose displayed quality differs from common-leaf quality by more than one cost doubling's worth: {flagged}.")


def agent_safety_text(rows):
    """O63: AA's safety-refusal outcomes on each ranked row's Coding Agent Index record (disclosed and flagged only)."""

    flagged = []
    for row in rows:
        safety = row.get("agentSafety") or {}
        if safety.get("status") != "flagged":
            continue
        parts = [f"{safety['blocked']} blocked" if safety["blocked"] else None,
                 f"{safety['fallback']} finished by {' or '.join(safety['fallbackModels'])}" if safety["fallback"] else None]
        flagged.append(f"{row['name']} ({', '.join(part for part in parts if part)} of {safety['attempts']} attempts)")
    return ("- **Coding Agent Index safety refusals (O63, flagged; costs and scores unchanged):** "
            + ("; ".join(flagged) if flagged else "none") + ".")


def harness_by_leaf_text(facts):
    """E227: the agent or harness each harness-run leaf was scored on, by cohort rows (each lab's model in its own agent)."""

    # O37: the Terminal-Bench leaf is AA's own run, so its agent is the leaf's provenance (tbench.ai's only for a gap fill).
    tb_agents = {row["id"]: (row["quality"]["leaves"].get("terminalBench") or {}).get("agent") for row in facts.v3["rows"]}
    # AI Coding Daily names the harness on each record (E257, I50 M2); I49 M1: every count is over this ranking's own rows.
    aicd = {row["id"]: (row["quality"]["leaves"].get("aiCodingDaily") or {}).get("harness") for row in facts.v3["rows"]}
    leaves = [("Terminal-Bench", lambda row: tb_agents.get(row["id"])),
              ("Bug Hunt", lambda row: (row.get("bugHunt") or {}).get("harness") if (row.get("bugHunt") or {}).get("matched") else None)]
    if "aiCodingDaily" in q.LEAF_BY_KEY:
        leaves.append(("AI Coding Daily", lambda row: aicd.get(row["id"])))
    ranked = {row["id"] for row in facts.v3["rows"]}
    parts = []
    for name, pick in leaves:
        counts = {}
        for row in facts.scores["models"]:
            agent = pick(row) if row["id"] in ranked else None
            if agent:
                counts[agent] = counts.get(agent, 0) + 1
        parts.append(f"{name}: " + (", ".join(f"{agent} {count}" for agent, count in sorted(counts.items(), key=lambda item: (-item[1], item[0]))) or "none"))
    return "- **Harness by leaf (E227):** " + "; ".join(parts) + "."


def mix_check_text(rows):
    """E208: the token-mix status of each selected Plan route (never compared with AA's Index-wide shares)."""

    counts = {}
    for row in rows:
        status = (row.get("plan") or {}).get("mixCheck")
        if status:
            counts[status] = counts.get(status, 0) + 1
    return "- **Token mix (E208):** " + ("; ".join(f"{count} selected routes: {status}" for status, count in sorted(counts.items())) or "no selected Plan route") + "."


def bar_name(bar):
    """E192: a bar is a frozen quality level."""

    return f"quality {bar['level']:.1f}"


def displayed_cheapest_sentences(facts):
    """E203: the displayed-record cheapest row at each bar, on the headline scale (a record, not a claim)."""

    sentences = []
    for basis, label in (("api", "API"), ("plan", "Plan")):
        parts = [
            f"at or above {bar_name(item)}: {facts.labels(item['cheapest'])} ({usd(item['costUsd'])} per basket run; {item['qualifierN']} reach it)"
            if item["cheapest"] else f"at or above {bar_name(item)}: none"
            for item in facts.v3["displayedCheapest"][basis]["bars"]
        ]
        sentences.append(f"{label} basis, displayed record (not a claim; E203): cheapest " + "; ".join(parts) + ".")
        margin = facts.v3["displayedCheapest"][basis].get("margin")
        companions = [f"at or above quality {item['margin']['level']:.1f}: {facts.labels(item['margin']['cheapest']) or 'none'}"
                      + (f" ({usd(item['margin']['costUsd'])} per basket run)" if item["margin"]["cheapest"] else "")
                      for item in facts.v3["displayedCheapest"][basis]["bars"] if "margin" in item]
        if companions:
            sentences.append(f"{label} basis, noise-margin companion (O44; each bar plus {margin:.1f} quality points, so the bar's own configuration cannot "
                             "decide it): cheapest " + "; ".join(companions) + ".")
    # I57 L5: a bar's cheapest row that carries an O63 safety-refusal flag is marked beside the claims it can affect.
    flags = {row["id"]: row.get("agentSafety") or {} for row in facts.v3.get("rows", [])}
    cheapest = {row_id.split("@")[0] for basis in ("api", "plan") for item in facts.v3["displayedCheapest"][basis]["bars"]
                for row_id in [*(item["cheapest"] or []), *((item.get("margin") or {}).get("cheapest") or [])]}
    flagged = [f"{facts.labels([row_id])} ({flags[row_id]['blocked']} blocked and {flags[row_id]['fallback']} fallback attempts of {flags[row_id]['attempts']})"
               for row_id in sorted(cheapest) if flags.get(row_id, {}).get("status") == "flagged"]
    if flagged:
        sentences.append("Safety-refusal flags (O63; costs and scores unchanged) on these bars' cheapest rows: " + "; ".join(flagged) + ".")
    sensitive = [f"{label} quality {entry['level']:.1f}" for basis, label in (("api", "API"), ("plan", "Plan"))
                 for entry in facts.v3["diagnostics"]["gapFillBars"]["bases"][basis] if not entry["survives"]]
    if sensitive:
        sentences.append("Fill-sensitive (E234): the displayed-record cheapest row changes when gap-filled leaves are removed or lowered by the measured offset at "
                         + ", ".join(sensitive) + ".")
    # O43: the claims cover ranked configurations only; a listed family (O41) is outside them.
    if facts.v3.get("listedIndicative"):
        sentences.append("These outputs compare ranked configurations only; listed families shown with an indicative value (O41) are outside them (O43): "
                         + ", ".join(item["name"] for item in facts.v3["listedIndicative"]) + ".")
    return sentences


def run_label(run):
    return run["stratum"] + (" endpoint-heavy" if run["alternative"] else "")


# --- README ------------------------------------------------------------------------------------


def leaders(facts):
    """One sentence naming each basis' leader (with its subset and provisional caveats) and the quality leader."""

    parts = []
    for basis, label in (("plan", "Plan"), ("api", "API")):
        leader = min((entry for entry in facts.ranked if entry["rank"][basis] is not None), key=lambda entry: (entry["rank"][basis], entry["name"]))
        route = leader["cost"]["route"] or {}
        transfer = basis == "plan" and route.get("grade") == "assumption"
        assumption = plan_routes.OWNER_ASSUMPTIONS[route.get("assumptionKind") or "transfer"][0] if transfer else None
        caveats = [word for word, present in (("subset cost", leader["cost"]["subset"]), ("provisional quality", leader["coverage"]["provisional"]), (assumption, transfer)) if present]
        parts.append(f"{leader['name']} leads the {label} ranking at {leader['overall'][basis]:.1f}" + (f" ({', '.join(caveats)})" if caveats else ""))
    quality = min(facts.ranked, key=lambda entry: (entry["qualityRank"], entry["name"]))
    return "; ".join(parts) + f"; {quality['name']} leads on quality."


def plan_rows_table(facts):
    """O48: the Plan ranking itself, one row per configuration and plan."""

    result = facts.v3["diagnostics"]["rankSeparability"]["plan"]["bands"]
    transferred = set(facts.v3["diagnostics"]["rankSeparability"]["planAssumedRouteRows"])
    rows = []
    for item in sorted(facts.v3["planRows"], key=lambda item: (item["rank"] is None, item["rank"] or 0, item["id"])):
        if item["rank"] is None:
            continue
        band = result.get(item["id"])
        band_label = DASH if band is None else (f"{band[0]}" if band[0] == band[1] else f"{band[0]}–{band[1]}") + ("†" if item["id"] in transferred else "")
        rows.append([rank_text(item["rank"]), facts.label(item["configurationId"]), item["plan"] or "API-cost fallback (no admitted plan)",
                     DASH if item["multiple"] is None else f"{item['multiple']:g}×", usd(item["costUsd"]), fnum(item["value"], 1), fnum(item["quality"], 1),
                     item["grade"] or "fallback", band_label])
    return ("\n\n### Plan ranking: every plan (O48)\n\n" + PLAN_ROW_TEXT + "\n\n"
            + markdown_table(["Plan rank", "Configuration", "Plan", "Value Multiple", "Plan cost (USD per basket run)", "Plan value", "Quality", "Route evidence", "Noise band"],
                             rows, numeric={0, 3, 4, 5, 6}))


PLAN_ROW_TEXT = ("The Plan ranking has one row per configuration and subscription plan (owner decision O48): each plan on which the configuration "
                 "has an admitted route, with that plan's route chosen by the official comparator; a configuration with no admitted route keeps one "
                 "API-cost row. Rows of one configuration share its quality and API cost and differ only by the plan's Value Multiple. The table above "
                 "shows each configuration's own plan row (its selected route).")


def open_web_text(step):
    """E240: a search's open-web discovery step, as queries, candidates and their resolutions."""

    if not step:
        return DASH
    candidates = step.get("candidates", [])
    registered = sum(1 for item in candidates if item["resolution"] == "register")
    return (f"{step.get('searchedOn', '')}: {len(step['queries'])} queries, {len(candidates)} candidates "
            f"({registered} registered, {len(candidates) - registered} rejected)")


def ranking_rows(facts, flags=True):
    """The ranking table's rows for one ranking (O53)."""

    table_rows = []
    for entry in facts.ranked:
        row = facts.row(entry)
        table_rows.append([
            rank_text(entry["rank"]["plan"]),
            rank_text(entry["rank"]["api"]),
            model_link(entry, configuration_label(row, facts.names)),
            fnum(entry["overall"]["plan"], 1),
            fnum(entry["overall"]["api"], 1),
            fnum(entry["quality"], 1),
            f"{entry['coverage']['pct']:.0f}%",
            usd(entry["cost"]["apiUsd"]),
            usd(entry["cost"]["planUsd"]),
            route_text(entry),
            *([short_flags(entry, row)] if flags else []),
            band_text(facts, row["id"]),
        ])
    return table_rows


RANKING_HEADERS = ['Plan rank', 'API rank', 'Configuration', 'Plan value', 'API value', 'Quality', 'Quality coverage', 'API cost (USD per basket run)',
                   'Plan cost (USD per basket run)', 'Plan route', 'Flags', 'Noise band (Plan / API)']


def leaf_set_text(leaves):
    """A ranking's software-engineering leaves and weights, then the rest (O53-O55)."""

    swe = [leaf for leaf in leaves if leaf.group == "swe"]
    return (", ".join(f"{leaf.label} {fnum(leaf.weight, 0)}%" for leaf in swe)
            + f" (software engineering {fnum(sum(leaf.weight for leaf in swe), 0)}%), plus the {len(leaves) - len(swe)} leaves outside software engineering every ranking shares")


def track_rankings_markdown(facts):
    """O53: every ranking other than the leading one, with its leaf set, table and listed configurations."""

    sections = []
    for track, other in facts.tracks.items():
        with q.active_track(track):
            listed = [entry for entry in other.unranked if entry["slug"] in {viewmodel.slugify(row["id"]) for row in facts.scores["models"] if row.get("rankingInclusionReasons")}]
            sections.append(
                f"### {q.TRACK_LABELS[track]}\n\n{viewmodel.TRACK_LEADS[track]} Its leaves: {leaf_set_text(q.LEAVES)}. "
                f"It ranks {len(other.ranked)} configurations, each with every leaf for its exact configuration (O36); its cost anchors and quality bars are its own "
                f"(anchor version `{other.v3['anchorVersion']}`), so its values are not comparable with the {q.TRACK_NAMES[q.DEFAULT_TRACK]}'s. "
                f"The interactive table is at [valuerank.alolabs.dev{viewmodel.TRACK_PATHS[track]}](https://valuerank.alolabs.dev{viewmodel.TRACK_PATHS[track]}).\n\n"
                + markdown_table(RANKING_HEADERS, ranking_rows(other), numeric={0, 1, 3, 4, 5, 6, 7, 8})
                + f"\n\n{separability_text(other).strip()}"
                + f"\n\nCohort configurations without this ranking's full set ({len(listed)}): {names([entry['name'] for entry in listed])}.\n"
            )
    return "\n".join(sections)


def readme(facts):
    v3, method = facts.v3, facts.method
    admitted = [item["label"] for item in method["basket"]["admitted"]]
    yield_ = v3["identificationYield"]
    table_rows = ranking_rows(facts)
    exploratory = (
        f" No Value Multiple is yet identified on the basket itself ({yield_['pointIdentified'] + yield_['setIdentified']} of {yield_['rows']} rows), "
        "so the Plan ranking is labelled exploratory."
        if yield_["exploratory"] else ""
    )
    legend = "\n".join(f"- **{word}**: {text}." for word, text in FLAG_LEGEND)
    intervals = "\n".join(f"- {sentence}" for sentence in interval_sentences(facts) + displayed_cheapest_sentences(facts))
    return f"""# ValueRank
**Frontier AI configurations ranked by value for software engineering and DevOps: benchmark quality against what the work costs**

**Version:** {VERSION}
**Updated:** {DATE}
**Methodology:** {v3['methodologyVersion']} · {v3['basketVersion']} · anchor version {v3['anchorVersion']}
**Scope:** {len(facts.ranked)} cohort configurations ({sum(1 for entry in facts.ranked if entry['rank']['api'] is not None)} with a value score) from a {len(facts.scores['models'])}-model AA-mapped roster; value is a {facts.cost_pct:.0f}% cost score (nominal weight{influence_text(v3, short=True)}) plus {facts.quality_pct:.0f}% quality over {len(q.LEAVES)} benchmark leaves

## Current result

ValueRank ranks frontier AI model configurations (see Model inclusion) by value for software engineering and DevOps work, separately for API buyers and for subscription (Plan) buyers. It publishes {len(q.TRACKS)} rankings (owner decision O53), each over the configurations that have its complete benchmark set: the **{q.TRACK_NAMES[q.DEFAULT_TRACK]}** below ({viewmodel.TRACK_LEADS[q.DEFAULT_TRACK][0].lower()}{viewmodel.TRACK_LEADS[q.DEFAULT_TRACK][1:-1]}) and {names(['the ' + q.TRACK_NAMES[track] for track in facts.tracks])} after it. The {q.TRACK_NAMES[q.DEFAULT_TRACK]}'s leaves: {leaf_set_text(q.LEAVES)}. Value is a fixed **{facts.cost_pct:.0f}%** cost score plus **{facts.quality_pct:.0f}%** benchmark quality.{influence_text(v3)} Cost is the {method['costLabel']}: Artificial Analysis' (AA) published cost of running the {series(admitted)} once at API rates (the {q.TRACK_NAMES[q.DEFAULT_TRACK]}'s basket; each ranking admits its own components, E254), scored on a log scale against frozen anchors so cost ratios keep their size.{coding_share_text(v3)} Quality is the weighted mean of {len(q.LEAVES)} (in the {q.TRACK_NAMES[q.DEFAULT_TRACK]}; {', '.join(f'{len(q.TRACKS[track])} in the {q.TRACK_NAMES[track]}' for track in q.TRACKS if track != q.DEFAULT_TRACK)}) benchmark leaves on fixed 0–100 anchors, and every configuration ranked in a ranking has all of that ranking's leaves for its exact configuration (O36): a leaf AA has not run comes from another party's run of the same benchmark, then from the model provider's published result, and a configuration still missing one after a logged exhaustive search is listed, not ranked. The Plan ranking divides the basket's API cost by a subscription route's Value Multiple at full utilisation, with one row per configuration and plan (O48), and uses the API cost, flagged, when no route is admitted.{exploratory}

{leaders(facts)}

{markdown_table(RANKING_HEADERS, table_rows, numeric={0, 1, 3, 4, 5, 6, 7, 8})}

Values are rounded for display; ranks are competition ranks (equal values share the better rank). The Plan rank is that of the configuration's own plan row (its selected route) in the Plan ranking of every plan below.{separability_text(facts)}{plan_rows_table(facts)}

{legend}

Not ranked in the {q.TRACK_NAMES[facts.track]} ({len(facts.unranked)} roster models): {names([entry['name'] for entry in facts.unranked])}. Reasons are listed in [scores.md](scores.md#not-ranked).{incomplete_text(facts)}{listed_indicative_text(facts)}

{track_rankings_markdown(facts)}
### What the evidence supports

{intervals}

Scenario shares by stream, diagnostics and the release gates are in [scores.md](scores.md); the inputs behind every number are in [raw-data.md](raw-data.md).

{model_inclusion_markdown(facts.inclusion)}
## How v3 scores value

- **Cost is the SDLC basket.** {v3['basketVersion']}: AA's published cost of running the {series(admitted)} once at API rates, in USD per basket run. Pending capture: {names([item['label'] for item in method['basket']['pending']])}. v2 used AA's cost to run the whole Intelligence Index per Index point.
- **Cost keeps its magnitude.** The cost score is 100 × (ln c_H − ln c) / (ln c_H − ln c_L), clipped to 0–100, against anchors frozen with anchor version `{v3['anchorVersion']}`. A model entering or leaving the cohort does not move another model's score. At the API anchors, doubling cost costs {method['exchangeRate']['api']['valuePointsPerCostDoubling']:.2f} value points, which {method['exchangeRate']['api']['qualityPointsPerCostDoubling']:.2f} quality points offset.
- **Quality is measured, not ranked.** Each leaf ({len(q.LEAVES)} in the {q.TRACK_NAMES[q.DEFAULT_TRACK]}) is placed on fixed 0–100 anchors from its raw value, so quality no longer depends on which other models are ranked. Only configurations with every leaf are ranked (O36), so all ranked rows are scored on the same benchmarks; each leaf filled from another party or a provider is listed in [raw-data.md](raw-data.md#leaf-gap-fills-and-searches-o36).
- **Plan value is route evidence.** Each subscription route carries its Value Multiple, evidence grade (controlled measurement, concordant reports, owner-named assumption) and identification status; the Plan ranking is labelled exploratory until multiples are identified on the basket.
- **Uncertainty is shown, not hidden.** Interval outputs certify which frontier and cheapest-above-a-bar claims the published record supports; scenario shares report frequencies over declared streams.
- v3 values are not numerically comparable with v2 or earlier releases.

## Sources and audit trail

- [Artificial Analysis methodology]({AA_METHODOLOGY_URL}) and its model pages: Intelligence Index component scores and the per-task evaluation costs of the basket.
- [AA Coding Agent Index v2.0]({AA_CODING_AGENTS_URL}): the Coding Agent Index cost (FrontierCode, Terminal-Bench and SWE-Atlas-QnA-AA) for each exact configuration (O50); AA withdrew DeepSWE v1.1 in October 2026 and it is no longer a leaf (O49).
- AA's own Terminal-Bench 4.0 run (the leaf; [tbench.ai]({TERMINAL_BENCH_URL}) rows fill a gap and serve as a cross-check, O37), [Bug Hunt Bench]({BUG_HUNT_URL}) owner-published runs, [Cognition's FrontierCode leaderboard]({facts.leaf_evidence['cognitionCapture']['url']}) and model-provider results for leaves AA has not run (O36).
- [SemiAnalysis subscription measurements]({SEMIANALYSIS_URL}) (owner-selected 2026-10-07) for the Claude and ChatGPT plan Value Multiples; owner-named transfers are labelled as assumptions.
- The evidence bundle in `data/scores.json` lists every input artifact with its SHA-256; bundle hash `{v3['evidenceBundle']['bundleHash']}`.
- [Methodology co-design record]({SPEC_DIR}): the reviewed specification, every owner and editor decision, and each reviewer's findings.

## Files

- [methodology.md](methodology.md): how value, cost, quality, the Plan basis and the uncertainty outputs are computed
- [scores.md](scores.md): rankings, leaf scores, basket costs, Plan routes, interval outputs, scenario shares, diagnostics and release gates
- [raw-data.md](raw-data.md): every leaf input with its evidence locator, component costs, benchmark source tables, Plan routes and the evidence bundle
- [https://valuerank.alolabs.dev/](https://valuerank.alolabs.dev/): website, generated by `valuerank.site.build` (source under [valuerank/site/](valuerank/site/))
- [https://valuerank.alolabs.dev/benchmarks/terminal-bench-4/](https://valuerank.alolabs.dev/benchmarks/terminal-bench-4/): current Terminal-Bench 4.0 score-versus-cost page
- [data/](data/): machine-readable snapshots and generated outputs (pipeline code lives in [valuerank/](valuerank/))
- [docs/](docs/README.md): contributor documentation (repository layout, architecture, development, testing, refresh and release); `npm run verify` runs every check
""" + facts.reconciliation_md


# --- methodology -------------------------------------------------------------------------------


def methodology(facts):
    v3, method = facts.v3, facts.method
    admission = v3["admission"]
    main = v3["mainWorkload"]
    cohort = {label: [] for _prefix, label in COHORT_ROUTES}
    for row_id in facts.rows:
        cohort[facts.cohort_route(row_id)].append(facts.label(row_id))
    cohort_lines = "\n".join(f"- {route} ({len(members)}): {', '.join(members)}" for route, members in cohort.items() if members)
    incomplete = v3["incompleteEvidence"]
    incomplete_line = (f"\n\n{len(incomplete)} more cohort configurations are listed, not ranked, because a quality benchmark is still missing after an exhaustive "
                       f"search logged within {LEAF_SEARCH_DAYS} days of the cutoff (O36; a required frontier family is listed the same way, O38): "
                       + "; ".join(f"{item['name']} (no {', '.join(LEAF_LABELS[key] for key in item['missing'])})" for item in incomplete) + "."
                       + "".join(f" Of these, {len(ranked)} are ranked in the {q.TRACK_NAMES[track]} (O53): {names(ranked)}."
                                 for track, other in facts.tracks.items()
                                 for ranked in [[item['name'] for item in incomplete if item['id'] in other.rows]] if ranked)
                       ) if incomplete else ""
    component_rows = [
        [component_label(key), "admitted" if item["admitted"] else "pending capture", item["available"], item["covered"], item["ranked"]]
        for key, item in admission["components"].items()
    ]
    boundary = v3["costBoundary"]
    boundary_rows = [
        [component_label(key)] + [classes.get(name, DASH) for name in boundary["chargeClasses"]]
        for key, classes in boundary["components"].items()
    ]
    anchor_rows = []
    for workload_id, workload in v3["workloads"].items():
        for basis, anchors in workload["anchors"].items():
            anchor_rows.append([f"`{workload_id}` ({workload['role']})", basis, usd(anchors["low"]), usd(anchors["high"]), len(anchors["referenceIds"]), workload.get("anchorStatus", DASH)])
    # O53-O55: one column of weights per ranking; a leaf a ranking does not use shows a dash.
    leaf_rows = [
        [md_link(leaf.label, viewmodel.LEAF_INFO[key]["url"]), q.GROUP_LABELS[leaf.group]]
        + [f"{weight:.2f}%" if weight is not None else DASH
           for weight in (next((item.weight for item in q.TRACKS[track] if item.key == key), None) for track in q.TRACKS)]
        + [viewmodel.LEAF_INFO[key]["unit"], LEAF_TRANSFORMS[key], "AA-run" if leaf.source == "aa" else "independent"]
        for key, leaf in q.ALL_LEAVES.items()
    ]
    required = [leaf.label for track in q.TRACKS.values() for leaf in track if leaf.weight >= q.REQUIRED_LEAF_WEIGHT]
    rate_rows = [
        [basis, f"{rate['anchorRatio']:.1f}", f"{rate['valuePointsPerCostDoubling']:.2f}", f"{rate['qualityPointsPerCostDoubling']:.2f}"]
        for basis, rate in v3["exchangeRate"].items()
    ]
    influence_rows = [
        [basis, len(item["commonWorkload"]["panel"]), pct(item["commonWorkload"]["costShare"], 1), item["commonWorkload"]["status"],
         pct((item["commonWorkload"]["varianceAllocation"] or {}).get("cost"), 1), fnum(item["orderingAgreement"]["costVsValue"], 2), fnum(item["orderingAgreement"]["qualityVsValue"], 2)]
        for basis, item in v3["costInfluence"].items()
    ]
    policy = v3["anchorPolicy"]
    bar = v3["barPolicy"]
    routes_policy = facts.routes_document["evidencePolicy"]
    exception = routes_policy["selectedSourceException"]
    policy_lines = "\n".join(f"- {label}: {routes_policy[key]}" for key, label in POLICY_APPLICATIONS if routes_policy.get(key))
    yield_ = v3["identificationYield"]
    measured = v3["measuredOnlyPlanView"]["specification"]
    streams = "\n".join(f"- **{key}**: {text}." for key, text in method["streamDescriptions"].items())
    not_quantified = "\n".join(f"- {text}." for text in method["notQuantified"])
    gate_rows = [[item["rule"], item["status"], item["detail"]] for item in v3["manifest"]]
    limitations = "\n".join(f"- {text}" for text in viewmodel.methodology_page(facts.bundle)["limitations"])
    scenarios = v3["scenarios"]
    interval_notes = "".join(
        f"{stream} draws {q.LEAF_BY_KEY[item['leaf']].label} inside its source's published {item['confidenceLevel']:.0%} confidence interval, labelled "
        f"{item['permittedLabel']} under its interpretation contract (E165; estimand: {item['sourceEstimand']}; method: {item['sourceIntervalMethod']}; "
        f"sampling unit: {item['samplingUnit']}); {item['tailTreatment']}. "
        for stream, items in scenarios.get("intervalInterpretation", {}).items()
        for item in items
    )
    scenario_scope = (
        f"{scenarios['scenarios']:,} scenarios per run, seed {scenarios['seed']}, input hash `{scenarios['inputHash'][:16]}`"
        if scenarios.get("status") == "current" else f"scenario outputs {scenarios.get('status')}"
    )
    return f"""# ValueRank Methodology

**Version:** {VERSION} (methodology {v3['methodologyVersion']})
**Updated:** {DATE}

This page summarises how ValueRank scores value. The normative specification, its review record and every owner and editor decision are in [{SPEC_DIR}]({SPEC_DIR}); where this summary is less precise, the specification governs.

## Objective and claim scope

ValueRank asks which frontier AI model configuration is lowest cost for the value it delivers on software-development work, once subscription economics and software-engineering benchmarks are weighed alongside general capability. It serves two buyers, ranked separately: **API buyers**, who pay per token (including through third-party agents), and **Plan buyers**, who use a provider subscription such as Claude Code, Codex or ChatGPT. The claim is scoped to value among the ranked configurations, under the published benchmark mix and evidence; it is not a market-wide optimum. Every ranked row is a **configuration**: a model version at one reasoning effort. Results are never transferred between versions or efforts.

## Cohort

{len(facts.rows)} configurations are ranked:

{cohort_lines}{incomplete_line} {plotted_names_text(facts)}{" A listed frontier or near-frontier family also shows, apart from the ranking, an indicative value on the leaves it has, labelled not ranked and not comparable (O41)." if v3["listedIndicative"] else ""}

The remaining {len(facts.unranked) - len(incomplete)} roster models are not ranked; each keeps a page with the evidence held for it.

{model_inclusion_markdown(facts.inclusion)}
## Value

Value on a basis = **{facts.cost_pct:.0f}%** × cost score + **{facts.quality_pct:.0f}%** × quality score (owner decision, 2026-10-19). Both scores run from 0 to 100, higher is better. Cost's share is fixed: a configuration missing quality evidence keeps cost at {facts.cost_pct:.0f}%, and a configuration without a cost score has no value score. Ranks are competition ranks; equal values share the better rank.

## Cost: the SDLC basket

The cost figure is the **{boundary['label']}**. {v3['basketVersion']} holds the components the admission rule admits ({admission['selectionRule']}); its reference panel is {admission['jointCovered']} of the {len(facts.rows)} ranked configurations (at least {admission['requiredPanelSize']} required):

{markdown_table(['Component', 'Status', 'Exact cost available', 'Complete', 'Ranked'], component_rows, numeric={2, 3, 4})}

A configuration's basket cost is the sum of AA's published costs for the admitted components at that exact model and effort: each Intelligence Index component is AA's cost per task times its task count, and the Coding Agent Index cost is AA's unrounded mean cost per task times its 290 required tasks (O27, O50). The Index components plus AA's residual reproduce AA's published Index total for every configuration (see raw-data.md).

**Cost boundary.** Source: {boundary['source']}. AA's cost covers the contestant model's API tokens; other charges are included, excluded or unknown per component:

{markdown_table(['Component'] + [CHARGE_LABELS[name] for name in boundary['chargeClasses']], boundary_rows)}

**Subset workloads (O17).** A configuration without exact cost for an admitted component is scored on the workload made of the components it has, against that workload's own frozen anchors, and flagged "subset cost"; its ordering against main-workload configurations is not identified. A component AA marks with missing or declined tasks is flagged "partial component" (E37).

## Cost score and anchors

Cost score S_C = 100 × (ln c_H − ln c) / (ln c_H − ln c_L), clipped to 0–100. The anchors are frozen per workload and basis: c_L is half the cheapest reference cost and c_H twice the dearest, so no reference configuration clips. A release is held when more than max(1, 10% of ranked rows) clip on a basis or any ranked row lies beyond an anchor by more than a factor of 2 (owner decision O12). The gate counts ranked rows only; a listed configuration beyond the anchors never holds a release and is disclosed (owner decision O58). {listed_beyond_text(facts)}

{markdown_table(['Workload', 'Basis', 'Low anchor c_L (USD)', 'High anchor c_H (USD)', 'References', 'Status'], anchor_rows, numeric={2, 3, 4})}

**Anchor policy** (`{policy['policyId']}` v{policy['version']}). Population: {policy['populationRule']}. Plan anchors: {policy['planRule']}. At least {policy['minimumReferences']} references; below that, {policy['belowMinimum']}. Lifetime: {policy['lifetime']}.

**Exchange rate.** In the unclipped region a cost doubling changes value by −100 × {v3['beta']} × ln 2 / ln(c_H / c_L) points, offset by +100 × {v3['beta']} × ln 2 / ((1 − {v3['beta']}) × ln(c_H / c_L)) quality points. At the main-workload anchors:

{markdown_table(['Basis', 'Anchor ratio c_H / c_L', 'Value points per cost doubling', 'Quality points that offset it'], rate_rows, numeric={1, 2, 3})}

**Within-cohort influence (E91, E126).** Cost's share of the value dispersion on the common-workload panel, 0.25 × SD(S_C) / (0.25 × SD(S_C) + 0.75 × SD(S_Q)), is published and flagged below 10% or above 90%; the flag is informational and the cost weight never changes (O2). Because cost and quality covary, that ratio describes dispersion; the value-variance allocation Cov(0.25 S_C, V) / Var(V) and the Kendall tau of the cost-only and quality-only orderings against the value ordering show contribution (E189).

{markdown_table(['Basis', 'Panel', "Cost's share", 'Status', "Cost's variance allocation", 'Tau, cost vs value', 'Tau, quality vs value'], influence_rows, numeric={1, 2, 4, 5, 6})}

## Quality

Quality is the weighted mean of the leaves observed for the exact configuration, each placed on fixed 0–100 anchors from its raw value (clipped, with saturation disclosed). Group shares of quality: {', '.join(f"{q.GROUP_LABELS[group]} {share_value:.0f}%" for group, share_value in q.GROUPS.items())}.

**Two rankings (owner decisions O52–O55, O61).** ValueRank picks each ranking's benchmark set and ranks the configurations that have all of it, balancing the number of benchmarks against the number of configurations ranked. Outside AA, independent software-engineering benchmarks run few efforts per model, so no single set covers the cohort: LiveBench 2.0 and Vals AI run each model once at its top effort, and AI Coding Daily mostly at high and medium effort. The **{q.TRACK_NAMES['max']}** (leading, O54) adds LiveBench 2.0 Overall, LiveBench's weighted mean of its seven categories (Long Agentic, Reasoning, Coding, Browser, Data Analysis, Research, Design; release 2026-10-23, O67; O61: all are needed in the SDLC, and as an uncontaminated benchmark it carries no less weight than any single AA leaf), Vals Vibe Code Bench v1.1 and Vals Code Migration v1.1; the **{q.TRACK_NAMES['aicd']}** adds AI Coding Daily (its bug-finding column excluded because it overlaps Bug Hunt). Each ranking has its own frozen anchors, quality bars, scenario run and diagnostics, so values are comparable within a ranking, not across. Surge's Complex Constraints (instruction following, IFBench's successor) is dropped for now and CursorBench 4.0 and Surge sudo L7 are excluded by the owner; Epoch MirrorCode, SWE-bench-Live and SWE-PolyBench each cover too few cohort configurations at their exact effort (O53, O54; [research record](research/2026-10-23-swe-benchmarks/reports/SWE%20benchmark%20candidates.md)). MiMo-V2.6-Pro's results are taken at high, its AA configuration (O54); Vals records its run without a level, read as the same single reasoning mode (E252). Kimi K3.1 Pro's results are taken at max, its maximum and default effort (O66).

{markdown_table(['Leaf', 'Group'] + [f"Weight, {q.TRACK_NAMES[track]}" for track in q.TRACKS] + ['Raw unit', 'Score', 'Run by'], leaf_rows, numeric={2, 3})}

{source_clocks_text(facts)}

Only configurations with every leaf are ranked (O36). A leaf is taken, in order, from AA (or the benchmark's own primary source), from a newer AA capture, from another party that ran the same benchmark version on the exact configuration (Cognition for FrontierCode, tbench.ai for Terminal-Bench), then from the model provider's published result. A row with a provider-claimed leaf competes in the interval outputs but earns no label of its own (E233). A configuration still missing a leaf after an exhaustive search logged within {LEAF_SEARCH_DAYS} days of the cutoff is listed with its missing leaves and search, not ranked; a required frontier family is listed the same way (O38). For a listed frontier or near-frontier family the search also logs an open-web discovery step: its queries and every candidate result, each resolved by a dated registry addition or a dated rejection with its reason, and the build fails on an unresolved candidate (E240). Every gap fill and search is in [raw-data.md](raw-data.md#leaf-gap-fills-and-searches-o36).

Coverage is the observed share of quality weight. A row is **provisional** when coverage is below {q.MIN_COVERAGE:.0%}, fewer than {q.MIN_SWE_LEAVES} software-engineering leaves are observed, observed software-engineering weight is below {q.MIN_SWE_WEIGHT:.0%}, or a leaf weighing {q.REQUIRED_LEAF_WEIGHT:.0f}% or more of quality ({names(sorted(set(required))) or 'none'}) is missing. Provisional rows are ranked and flagged; there is no quality floor (O8). Missing leaves are never filled; the interval outputs treat each one as anywhere in 0–100.

## Plan basis

Plan cost = basket API cost ÷ a subscription route's Value Multiple, at full utilisation. **The Plan ranking has one row per configuration and plan (owner decision O48)**: every plan on which the configuration has an eligible route, each plan's route chosen by the comparator below among that plan's candidates; rows of one configuration share its quality and API cost and differ only by the plan's multiple, share every scenario draw, and are told apart by any value gap; a configuration's own Plan figures (the main table, model pages, and the Plan diagnostics that rebuild anchors or move evidence) are those of its selected route's plan row. Every route record names one model and one plan (O45). A Value Multiple is the API-priced usage a subscription delivers per dollar of fee. Route evidence is graded: **controlled** measurements of the exact model (or, ranked just below them, of the same model at another effort: an O88 route, measured evidence under O90), **reports** (at least two independent, comparable end-user reports concordant within 20%), owner **assumptions** (a measured multiple transferred to another model, or an O46 quota ceiling, labelled), and **diagnostic** evidence, which is shown but never ranked. Two owner-authorised classes sit beside them: GPT-6.1 Sol and GPT-6 Astra keep their own SemiAnalysis figure on every ChatGPT plan (a figure that names a model without an effort binds to its unsuffixed, max row), and every other GPT row takes the lower of the two figures per plan as a labelled assumption (O45); each MiMo-V2.6 model takes, per Token Plan tier, the quota-implied ceiling — the tier's monthly credits valued at Xiaomi's API rate for that model over the list fee — labelled provider-derived and not a measurement (O46), because Xiaomi prices credits at parity with its API and no end-user measurement of a V2.6 billing period exists. Routes certifiably dearer than another identified route of at least equal grade are set aside (E88); the official route is then chosen by identification class, evidence grade, the comparison multiple, lower gross cash and route ID (E85). Evidence past its 90-day expiry and 30-day grace is demoted to diagnostic. A configuration without an admitted route uses its API cost, flagged. Each Plan row publishes its fee period, the cash paid and the selected multiple's amount (multiple × gross cash), typed by what the measurement establishes (E166): measured-workload capacity, observed eligible consumption with capacity not established, assumed API-equivalent consumption for an owner-named transfer (with its donor), consumption measured on the same model at another effort (an O88 route, with its donor), the full quota at API rates for an O46 ceiling, or identified target-workload capacity; API-fallback rows publish none.

**Identification (E61).** A multiple is measured on its own workload; it identifies the basket's multiple only when the workloads match. Today {yield_['pointIdentified']} of {yield_['rows']} Plan rows are point-identified and {yield_['setIdentified']} set-identified, so the Plan ranking is {'labelled exploratory' if yield_['exploratory'] else 'not labelled exploratory'}. A measured-only Plan view (`{measured['id']}`) re-runs the selection over {measured['admission']}, without owner assumptions or API fallbacks. Because the official Plan anchors include owner assumptions and API fallbacks, a calibration diagnostic rescores the measured-only rows on anchors built from measured evidence alone (E164), so an assumption's effect through the exchange rate is visible.

**Subscription evidence policy** (as of {facts.routes_document['asOf']}; reporting window {routes_policy['reportingWindow']['start']} to {routes_policy['reportingWindow']['end']}{search_gap_text(routes_policy)}):

- Default numerator: {routes_policy['defaultNumerator']}
- Selected source for {', '.join(exception['providers'])}: [SemiAnalysis]({exception['sourceUrl']}) ({exception['publicationDate']}, owner-selected {exception['authorizedOn']}): {exception['evidenceType']}
{policy_lines}
- Provider allowance, quota and marketing figures never supply the measured numerator; a provider's published price can be the fee denominator only when the tier mapping is supported.

## Uncertainty outputs

**Interval outputs (O25).** Each observed leaf is placed anywhere inside its published reporting precision, each missing leaf anywhere in 0–100 and each cost inside its rounding. A configuration is on the **definite frontier** when no other configuration can beat it on both cost and quality for any values in those boxes, and on the **possible frontier** when some values put it there. The **cheapest above a quality bar** is confirmed only when its worst cost is below the best cost of every other configuration that could qualify. The bar is pinned by policy `{bar['policyId']}` v{bar['version']}: the {bar['position']} of {bar['populationRule']}, ordered by {bar['order']}, selected {bar['selectionMode']}; {bar['reference']}; {bar['nonTautology']}; {bar['lifetime']}. Current headline bar: {method['barLevel'] or 'none'}{"; ladder: " + ", ".join(method["barLadder"]) if method.get("barLadder") else ""}.

**Scenario shares** are frequencies over declared streams, never probabilities ({scenario_scope}):

{streams}

S1 also runs with the endpoint-heavy kernel. **S1T (owner decision O39)** redraws every leaf with plug-in binomial noise from its published task count (the proportion taken as (k + ½)/(n + 1), so a 0% or 100% score keeps a positive spread) (FrontierCode 100, Terminal-Bench 66, AutomationBench-AA 657, AA-LCR 100, SciCode 288, HLE 2,158, CritPt 70, Bug Hunt's 105 bugs, AA-Omniscience's 6,000 questions scored +1/0/−1, LiveBench 2.0 Overall as the weighted mean of its seven category shares, with the release's weights (O67) (Long Agentic 18, Reasoning 4, Coding 29, Browser 25, Data Analysis 3, Research 22, Design 25; Reasoning and Data Analysis publish only their parts, so their counts are the wide reading, E264), AI Coding Daily's 6 graded projects), with GDPval-AA drawn from each row's displayed rating interval read as a 95% normal interval (an assumption) and the two Vals boards from Vals' published standard error (E256). Tasks are treated as independent, so it is an approximation; it never authorises a label or changes a score. From the same noise the ranking prints a **noise band** beside each rank (O42): rows in value order join the current band while their value is not separable from the band's first row (1.96 × √(SD_i² + SD_j²), with analytic quality-leaf SDs; cost is not drawn), otherwise they start a new one, so every row is inseparable from its band's first row and adjacent rows in different bands may also be inseparable. Shared tasks correlate two rows' errors and narrow the true threshold (separable adjacent ranks at correlations 0.3 and 0.6 are published), while omitted sources widen it (run-to-run and harness variance, AA's single cost run, owner-assumption error on the Plan basis); the net direction is not established. Each bar also has a **noise-margin companion** (O44): the cheapest configuration whose displayed quality clears the bar by at least the quality noise margin, 1.96 × √2 × the median row's quality SD. On the Plan basis the core streams (S1, S2, S1M and S1T) run with owner assumptions off (E167): a row whose selected route rests on any owner assumption is unevaluable there, never reselected or replaced by API cost, while S0 keeps the displayed record. {interval_notes}A cheapest-above-the-bar label is published only when the share clears a sequential threshold with its per-look error controlled. Not quantified in these shares:

{not_quantified}

## Diagnostics

Diagnostics are published beside the ranking and never change a score: Terminal-Bench cross-source agreement (AA's run against tbench.ai), FrontierCode cross-source agreement (AA against Cognition) and gap-fill removal (E234), anchor stability (exchange-rate series and trimmed-anchor rank shifts), Omniscience abstention sensitivity, quality source shares, matched-panel quality agreement, non-discriminating leaves, group drift, quality dispersion, deletion sensitivity (leave-one-benchmark-out and source deletions) and the standing removal of the Terminal-Bench cost component. Current results are in [scores.md](scores.md#diagnostics).

## Release gates

{markdown_table(['Rule', 'Status', 'Detail'], gate_rows)}

## Limitations

{limitations}

## Machine-readable files

- [data/scores.json](data/scores.json): the `v3` section holds every row, workload, anchor, interval output, scenario result, diagnostic and the evidence bundle
- [data/plan_cost_routes.json](data/plan_cost_routes.json): subscription routes, their evidence, sources and policy
- [data/v3_frozen.json](data/v3_frozen.json): frozen anchors, bar policy and anchor policy for anchor version `{v3['anchorVersion']}`
- [data/v3_scenarios.json](data/v3_scenarios.json): scenario-share runs for every stream
- [data/tb4.json](data/tb4.json), [data/bug_hunt.json](data/bug_hunt.json): independent benchmark snapshots ([data/aa_deepswe.json](data/aa_deepswe.json) keeps AA's last DeepSWE v1.1 capture, no longer scored, O49)
- [data/leaf_evidence.json](data/leaf_evidence.json), [data/cognition_frontiercode.json](data/cognition_frontiercode.json): leaf gap fills and the exhaustive-search log (O36/O37)
"""


def md_link(label, url):
    return f"[{label}]({url})" if url else label


# --- scores ------------------------------------------------------------------------------------


SCORE_HEADERS = ['Configuration', 'Plan rank', 'Plan value', 'Plan cost score', 'API rank', 'API value', 'API cost score', 'Quality', 'Quality coverage', 'Workload']


def score_rows(facts):
    """scores.md's ranking table rows for one ranking."""

    rows = []
    for entry in facts.ranked:
        row = facts.row(entry)
        rows.append([
            model_link(entry, configuration_label(row, facts.names)),
            rank_text(entry["rank"]["plan"]), fnum(entry["overall"]["plan"], 2), fnum(entry["costDims"]["plan"], 2),
            rank_text(entry["rank"]["api"]), fnum(entry["overall"]["api"], 2), fnum(entry["costDims"]["api"], 2),
            fnum(entry["quality"], 2), f"{entry['coverage']['pct']:.0f}%", workload_text(entry),
        ])
    return rows


def leaf_table(facts):
    """Each ranked row's leaf scores for the active ranking's leaves."""

    leaf_rows = []
    for entry in facts.ranked:
        row = facts.row(entry)
        leaves = row["quality"]["leaves"]
        leaf_rows.append(
            [configuration_label(row, facts.names)]
            + [fnum(leaves[leaf.key]["z"], 1) if leaf.key in leaves else DASH for leaf in q.LEAVES]
            + [fnum(row["quality"]["displayed"], 2), "; ".join(row["quality"]["provisionalReasons"]) or "no"]
        )
    return markdown_table(["Configuration"] + [leaf.label for leaf in q.LEAVES] + ["Quality", "Provisional"], leaf_rows, numeric=set(range(1, len(q.LEAVES) + 2)))


def track_scores_markdown(facts):
    """O53: each other ranking's table and leaf scores in scores.md."""

    sections = []
    for track, other in facts.tracks.items():
        with q.active_track(track):
            sections.append(
                f"## {q.TRACK_LABELS[track]}\n\n{viewmodel.TRACK_LEADS[track]} Anchor version `{other.v3['anchorVersion']}`; leaves: {leaf_set_text(q.LEAVES)}.\n\n"
                + markdown_table(SCORE_HEADERS, score_rows(other), numeric={1, 2, 3, 4, 5, 6, 7, 8})
                + f"\n\n### {q.TRACK_LABELS[track]}: quality leaf scores\n\n" + leaf_table(other) + "\n"
                # I47 M1: the per-ranking disclosures the specification points to are printed for every ranking.
                # I48 M1: the ranking's displayed-record results (E203), noise-margin companions (O44), separability and indicative values (O41).
                + f"\n### {q.TRACK_LABELS[track]}: displayed record and noise\n\n"
                + "".join(f"- {sentence}\n" for sentence in displayed_cheapest_sentences(other))
                + f"\n{separability_text(other).strip()}\n{listed_indicative_text(other)}\n"
                + f"\n### {q.TRACK_LABELS[track]}: Plan routes and calibration\n\n{calibration_markdown(other)}\n"
                + f"\n### {q.TRACK_LABELS[track]}: interval outputs\n\n{interval_tables(other)}\n"
                + f"\n### {q.TRACK_LABELS[track]}: scenario shares\n\n{scenario_panel_note(other)}{scenario_tables(other)}\n"
                + f"\n### {q.TRACK_LABELS[track]}: diagnostics\n\n{diagnostics_markdown(other)}\n"
            )
    return "\n".join(sections)


def scores_markdown(facts):
    v3 = facts.v3
    ranking_rows = score_rows(facts)
    components = list(basket.TARGET_COMPONENTS)
    cost_rows = []
    for entry in facts.ranked:
        row = facts.row(entry)
        detail = row["cost"]["componentsDetail"]
        cost_rows.append(
            [configuration_label(row, facts.names)]
            + [usd(detail[key]["costUsd"]) if key in detail else DASH for key in components]
            + [usd(row["cost"]["costUsd"]), names([component_label(key) for key in row["cost"]["missingComponents"]])]
        )
    plan_rows = []
    for entry in facts.ranked:
        row = facts.row(entry)
        plan = row["plan"]
        plan_rows.append([
            configuration_label(row, facts.names), route_text(entry), plan_amount_text(plan["amount"]), basket_runs_text(plan["amount"], row["api"]["costUsd"]),
            plan.get("selectedIdentification") or DASH,
            usd(row["planScore"]["costUsd"]), "; ".join(plan["flags"]) or DASH, plan.get("selectionReason") or DASH,
        ])
    # E171/E179: each row's admissible route-measurement pairs and the comparator's pick without the selected one.
    alternative_rows = []
    for entry in facts.ranked:
        row = facts.row(entry)
        table = row["plan"]["routeAlternatives"]
        if not table["pairs"]:
            continue
        fallback = table["leaveSelectedOut"]
        alternative_rows.append([
            configuration_label(row, facts.names), table["admissiblePairs"], table["unidentifiedPairs"],
            "; ".join(f"{item['routeId']} ({item['displayedMultiple']:g}×, {item['status']})" for item in table["pairs"]),
            f"{fallback['routeId']} ({fallback['displayedMultiple']:g}×, value {fnum(fallback['displayedPlanValue'], 2)})" if fallback else "none: the row would fall back to API cost (O13)",
        ])
    routed = [row for row in v3["rows"] if row["plan"]["routeAlternatives"]["pairs"]]
    workday = sorted({row["plan"]["workday"]["status"] for row in routed})
    gate_outcomes = sorted({row["valuationGate"]["outcome"] for row in v3["rows"]})
    gate_counts = ", ".join(f"{sum(1 for row in v3['rows'] if row['valuationGate']['outcome'] == outcome)} {outcome}" for outcome in gate_outcomes)
    flagged_gate = [row["id"] for row in v3["rows"] if row["valuationGate"]["flag"]]
    metering = ", ".join(f"{count} {label}" for label, count in v3["meteringMix"].items() if count)
    intervals_text = "; ".join(f"{item['leaf']}: {item['status']}, level {item['level']}" for item in v3["sourceIntervals"])
    measured = v3["measuredOnlyPlanView"]
    measured_rows = [
        # I75 L1: a row measured on the same model at another effort (an O88 route, O90) says so.
        [facts.label(model_id), item["status"] + ("; measured at another effort (O88, O90)" if item.get("crossEffort") else ""), item.get("routeId") or DASH, usd(item.get("costUsd")), fnum(item.get("value"), 2), item.get("rank") or DASH]
        for model_id, item in sorted(measured["rows"].items(), key=lambda pair: (pair[1].get("rank") is None, pair[1].get("rank") or 0, facts.label(pair[0])))
    ]
    unranked_rows = [[entry["name"], "; ".join(entry["exclusionReasons"]) or DASH] for entry in facts.unranked]
    return f"""# ValueRank {VERSION} Scores

**Updated:** {DATE} · methodology {v3['methodologyVersion']} · {v3['basketVersion']} · anchor version `{v3['anchorVersion']}`

Value = {facts.cost_pct:.0f}% × cost score + {facts.quality_pct:.0f}% × quality. Costs are USD per basket run; the cost score is log-scaled against the frozen anchors of the row's workload (see [methodology.md](methodology.md)).

## Ranking

{markdown_table(SCORE_HEADERS, ranking_rows, numeric={1, 2, 3, 4, 5, 6, 7, 8})}

## Not ranked

{markdown_table(['Model', 'Reasons'], unranked_rows)}

## Quality leaf scores

Each leaf's score z on its fixed 0–100 anchors; "—" marks a leaf with no eligible exact-configuration result.

{leaf_table(facts)}

{track_scores_markdown(facts)}

## Basket cost by component

USD at API rates for the exact configuration; "—" marks a component without an exact cost.

{markdown_table(['Configuration'] + [component_label(key) for key in components] + ['Basket cost', 'Missing admitted components'], cost_rows, numeric=set(range(1, len(components) + 2)))}

### Valuation basis

Valuation-basis gate (E170): {gate_counts}{(' (flagged: ' + facts.labels(flagged_gate) + ')') if flagged_gate else ''}. AA's Index category costs reconcile exactly with the prices AA displays for each configuration at capture, so its applied prices are the prices in force at the release cutoff. Token metering (E176): {metering}; AA values cached input at live measurements of each model's typical cache-hit rate. Source intervals (E174): {intervals_text}.

## Plan route selection

The Plan amount is the selected multiple times the cash paid for the fee period (E166), typed by what the measurement establishes; it is not capacity unless it says so. The multiple values only the measured workload's API-equivalent consumption; other plan features are not valued.

{markdown_table(['Configuration', 'Selected route', 'Plan amount', 'Basket runs per fee period', 'Identification', 'Plan cost (USD per basket run)', 'Flags', 'Selection reason'], plan_rows, numeric={5})}

### Route alternatives

Every admissible route-measurement pair in comparator order (E171) and the comparator's pick with the selected pair removed (E179). A larger displayed multiple is arithmetic on the measured workload, never a claim that the route is cheaper on the scored workload. Workday-feasible multiple (E15), for the {len(routed)} routed rows: {'; '.join(workday) or 'none routed'}.

{markdown_table(['Configuration', 'Admissible pairs', 'Unidentified', 'Pairs (multiple, status)', 'Leave-selected-out choice'], alternative_rows, numeric={1, 2})}

### Plan allowance report cells (O71, O81)

{report_cells_markdown(facts)}

### Measured-only Plan view

Admission: {measured['specification']['admission']}. Selection: {measured['specification']['selection']}. Panel: {measured['specification']['panel']}.

{markdown_table(['Configuration', 'Status', 'Route', 'Plan cost', 'Value', 'Rank'], measured_rows, numeric={3, 4, 5})}

{calibration_markdown(facts)}

## Interval outputs

{interval_tables(facts)}

## Scenario shares

{scenario_panel_note(facts)}{scenario_tables(facts)}

## Diagnostics

{diagnostics_markdown(facts)}

## Release gates

{markdown_table(['Rule', 'Status', 'Detail'], [[item['rule'], item['status'], item['detail']] for item in v3['manifest']])}
"""


def report_cells_markdown(facts):
    """I78 L5: every O71 report cell's verdict, as the build computed it (O81-O87, O93)."""

    cells = facts.v3.get("planAllowanceCells") or []
    if not cells:
        return "No report cell."
    passing = sum(cell["status"] == "passes" for cell in cells)
    rows = [[cell["provider"], cell["plan"] + ("" if cell.get("listed", True) else " (not listed)"), cell["modelId"] or DASH, cell["unit"], cell["region"],
             str(sum(1 for report in cell["reports"] if report["excluded"] is None)) + f" of {len(cell['reports'])}", cell["status"]]
            for cell in sorted(cells, key=lambda item: (item["provider"], item["plan"], str(item["modelId"]), item["unit"], item["region"]))]
    return (f"{len(cells)} cells; {passing} pass{'es' if passing == 1 else ''}. A cell on a plan the Plan ranking does not list is evidence only (O85).\n\n"
            + markdown_table(["Provider", "Plan", "Model", "Unit", "Region", "Eligible reports", "Verdict"], rows))


def scenario_panel_note(facts):
    """E266: the scenario panel is the main workload's rows; a subset-workload row gets no scenario share."""

    rows = facts.v3["rows"]
    subset = [facts.label(row["id"]) for row in rows if row["cost"]["workload"] != facts.v3["mainWorkload"]]
    panel = f"The scenario panel is the {len(rows) - len(subset)} rows scored on the main workload (E96, E266)"
    if not subset:
        return panel + ".\n\n"
    return (panel + "; " + series(subset) + " (subset workload) are not in it and have no scenario shares, so the shares below compare "
            "the main-workload rows only.\n\n")


def anchor_setter(facts, end):
    """One official Plan anchor setter; an API-cost fallback plan row already names its evidence (O48)."""

    label = facts.label(end["row"])
    return label if label.endswith(end["evidence"]) else f"{label} ({end['evidence']})"


def calibration_markdown(facts):
    """E164: the measured-only rows rescored on anchors built from measured evidence alone."""

    measured = facts.v3["measuredOnlyPlanView"]
    calibration = measured["calibration"]
    lines = [f"#### Measured-evidence calibration (diagnostic)\n\nReferences: {calibration['rule']}. Status: {calibration['status']}.\n"]
    for workload, item in calibration["workloads"].items():
        provenance = item["officialAnchorProvenance"]
        extremes = (
            f" Official Plan anchors are set by {anchor_setter(facts, provenance['low'])} at the low end "
            f"and {anchor_setter(facts, provenance['high'])} at the high end."
            if provenance else " The workload has no official Plan anchors."
        )
        if item["status"] != "evaluated":
            lines.append(f"- Workload `{workload}`: {item['status']}; measured rows {facts.labels(item['rows'])}.{extremes}")
            continue
        anchors = item["anchors"]
        official_ratio = f"{item['officialExchangeRate']['anchorRatio']:.1f}" if item["officialExchangeRate"] else DASH
        lines.append(
            f"- Workload `{workload}`: measured anchors {usd(anchors['low'])} to {usd(anchors['high'])} from {facts.labels(item['references'])}; "
            f"anchor ratio {item['exchangeRate']['anchorRatio']:.1f} against the official {official_ratio}.{extremes}"
        )
    rows = [
        # I75 L1: a reference measured on the same model at another effort (an O88 route, O90) is marked.
        [facts.label(row_id) + (" ‡" if measured["rows"][row_id].get("crossEffort") else ""), fnum(measured["rows"][row_id]["value"], 2), fnum(value, 2),
         calibration["rankChange"]["changes"].get(row_id, DASH)]
        for row_id, value in sorted(calibration["values"].items(), key=lambda pair: facts.label(pair[0]))
    ]
    if rows:
        lines.append("\n" + markdown_table(["Configuration", "Value on official Plan anchors", "Value on measured anchors", "Rank change"], rows, numeric={1, 2, 3}))
        reversals = "; ".join(f"{facts.label(a)} and {facts.label(b)}" for a, b in calibration["reversals"]) or "none"
        lines.append(f"\nPairwise reversals: {reversals}. Largest value change: {fnum(calibration['maxAbsValueChange'], 2)} points.")
        if any(measured["rows"][row_id].get("crossEffort") for row_id in calibration["values"]):
            lines.append("\n‡ measured on the same model at another effort (an O88 route; measured evidence under O90).")
    return "\n".join(lines)


def interval_block(facts, result, label, workload_label):
    """One basis's frontier and bar tables on one workload (E21, E38, E183)."""

    if result["status"] != "evaluated":
        return f"**{label} basis, {workload_label}:** not evaluated ({result.get('reason', result['status'])})."
    rows = [
        [facts.label(row_id), item["possible"], item["definite"], facts.label(item["definiteCounterexample"]) if item["definiteCounterexample"] else DASH,
         facts.labels(item["possibleBlockedBy"]) if item["possibleBlockedBy"] else DASH]
        for row_id, item in result["frontier"].items()
        if "possible" in item
    ]
    text = f"**{label} basis, {workload_label}: frontier.** Not evaluable: {facts.labels(result['unevaluable'])}."
    if result.get("blockers"):
        text += f" Competing without a label (AA cost on a price not in force, O29, E183): {facts.labels(result['blockers'])}."
    text += "\n\n"
    text += markdown_table(["Configuration", "Possible frontier", "Definite frontier", "Definite counterexample", "Possible frontier blocked by"], rows)
    for bar in result.get("bars", []):
        reference = bar_name(bar["reference"])
        text += f"\n\n**{label} basis, {workload_label}: cheapest at or above {reference}** ({bar['reference']['rule']}). Status {bar['status']}"
        if bar["status"] == "certified":
            text += f"; confirmed cheapest: {facts.label(bar['confirmedCheapest']) if bar['confirmedCheapest'] else 'none'}.\n\n"
            siblings = "; ".join(f"{facts.label(row_id)}: {', '.join(names)}" for row_id, names in bar["uncheckedCheaperSiblings"].items() if names)
            text += f"Configurations that can be confirmed to qualify: {bar['confirmedQualifierN']} (confirmation needs the full-composite lower bound, with missing leaves at 0, to clear the bar; O25). "
            text += f"Cheaper same-family configurations on AA's chart that were not evaluated (not ranked in this ranking: lacking its full benchmark set, or not plotted on or near the frontier; E201c, O51): {siblings or 'none'}.\n\n"
            text += f"Bar comparison: {bar['comparison']}. The bar is a displayed-quality level; qualification tests each row's full-composite bounds, so a row above the bar on displayed quality can still fail to qualify confirmed when leaves are missing (E198).\n\n"
            bar_rows = [[facts.label(row_id), fnum(item["displayedMargin"], 1), item["confirmed"], item["possible"], item["possibleCheapest"]] for row_id, item in bar["rows"].items() if "confirmed" in item]
            text += markdown_table(["Configuration", "Displayed quality − bar", "Confirmed qualifies", "Possibly qualifies", "Possibly cheapest"], bar_rows, numeric={1})
        else:
            text += "."
    return text


def interval_tables(facts):
    sections = [interval_block(facts, facts.v3["intervals"][basis], label, "main workload") for basis, label in (("api", "API"), ("plan", "Plan"))]
    # E190: the same outputs on each subset workload, over every row with full cost there.
    for item in facts.v3["subsetIntervals"].values():
        workload_label = "subset workload (" + ", ".join(component_label(key) for key in item["components"]) + "; orderings across workloads not identified)"
        sections += [interval_block(facts, item[basis], label, workload_label) for basis, label in (("api", "API"), ("plan", "Plan"))]
    return "\n\n".join(sections)


def scenario_tables(facts):
    scenarios = facts.v3["scenarios"]
    if scenarios.get("status") != "current":
        return f"Scenario outputs are {scenarios.get('status')}; no shares are published for this release."
    parts = [f"Frequencies over {scenarios['scenarios']:,} scenarios per run (seed {scenarios['seed']}); streams are defined in [methodology.md](methodology.md#uncertainty-outputs). S1T adds benchmark sampling noise under an independent-task approximation (O39); the other streams exclude it, and every stream excludes correlated-task, harness and attempt effects (E155)."]
    for basis, label in (("api", "API"), ("plan", "Plan")):
        runs = scenarios["results"][basis]
        row_ids = sorted({row_id for run in runs for row_id in run["panel"]}, key=facts.label)
        excluded = {item["row"] for run in runs for item in run.get("excluded", [])}
        if excluded:
            off = [run_label(run) for run in runs if run.get("excluded")]
            parts.append(
                f"{label} streams {series(off)} run with owner assumptions off ({plan_routes.assumption_kinds_text("and", plural=True)}; E167): {facts.labels(sorted(excluded, key=facts.label))} "
                "depend on an owner assumption and are unevaluable there (—), never reselected or replaced by API cost."
            )
        for event, event_label in (("top1", "rank 1"), ("top3", "rank 3 or better"), ("frontier", "on the frontier")):
            rows = [[facts.label(row_id)] + [share(run["rows"][row_id][event]["share"]) if row_id in run["rows"] else DASH for run in runs] for row_id in row_ids]
            parts.append(f"### {label} basis: {event_label}\n\n" + markdown_table(["Configuration"] + [run_label(run) for run in runs], rows, numeric=set(range(1, len(runs) + 1))))
        # E87: the row-level scenario dispersion of the value score, with the cost-quality covariance term beside it.
        rows = [[facts.label(row_id)] + [dispersion_text(run["rows"][row_id]["dispersion"]) if row_id in run["rows"] else DASH for run in runs] for row_id in row_ids]
        parts.append(f"### {label} basis: value-score dispersion (SD; covariance term)\n\n" + markdown_table(["Configuration"] + [run_label(run) for run in runs], rows, numeric=set(range(1, len(runs) + 1))))
    branches = [f"- **{item['id']}** ({item['stratum']}): {item['status']}" + (f"; {item['reason']}" if item.get("reason") else f"; band width {fnum(item['width'], 1)} points") for item in scenarios["namedBranches"]]
    parts.append("### Named S2 specification branches\n\n" + "\n".join(branches))
    labels = []
    for item in scenarios["barLabels"]:
        for candidate, result in item.get("candidates", {}).items():
            low, high = result["frequencyRange"]
            labels.append([
                bar_name(item), facts.label(candidate), result["reading"], f"{share(low)} to {share(high)}",
                ", ".join(f"{code} {outcome['status']}" for code, outcome in result["assignments"].items()), "yes" if result["label"] else "no",
            ])
    if labels:
        parts.append("### Cheapest-above-the-bar labels (API basis)\n\nThe 90% rule's error bound holds per published event (candidate and kernel assignment); it is not corrected across the listed candidates (E198). Each kernel assignment code gives the kernel used for the candidate and the competitors, in that order (U uniform, H endpoint-heavy; a quality-level bar has no reference rows, so it takes no letter); the label needs every assignment met.\n\n"
                     + markdown_table(["Bar", "Candidate", "Reading", "Frequency range", "Kernel assignments", "Label"], labels))
    return "\n\n".join(parts)


def dispersion_text(spread):
    """E87: the value-score SD over a stream's scenarios with the covariance term, or the undefined status."""

    if spread["status"] != "defined":
        return spread["status"]
    return f"{spread['valueSd']:.2f} ({spread['covarianceTerm']:+.2f})"


def rank_change_text(changes, names_label):
    moved = {row_id: change for row_id, change in changes.items() if change}
    if not moved:
        return "no rank changes"
    largest = max(abs(change) for change in moved.values())
    return (f"{len(moved)} {'row moves' if len(moved) == 1 else 'rows move'}; largest move {largest} "
            f"({names_label([row_id for row_id, change in moved.items() if abs(change) == largest])})")


LEAF_LABELS = {key: leaf.label for key, leaf in q.ALL_LEAVES.items()}


def gap_fill_text(sensitivity, facts):
    """E234: rank changes when each row's leaves from another party or the provider are removed."""

    filled = sensitivity["rows"]
    if not filled:
        return "- **Gap-fill removal (E234, diagnostic):** no ranked row has a leaf from another party or the provider."
    rows = "; ".join(f"{facts.label(row_id)} ({', '.join(LEAF_LABELS[key] for key in leaves)})" for row_id, leaves in filled.items())
    moves = "; ".join(f"{label} {rank_change_text(sensitivity['bases'][basis]['rankChanges']['changes'], facts.labels)}" for basis, label in (("api", "API"), ("plan", "Plan")))
    return f"- **Gap-fill removal (E234, diagnostic; scores unchanged):** with these leaves removed and the rest renormalised — {rows} — {moves}."


def band_text(facts, row_id):
    """O42: the row's band of ranks it cannot be separated from under benchmark sampling noise, Plan then API."""

    result = facts.v3["diagnostics"]["rankSeparability"]
    # O48: a configuration's Plan band is that of its own plan row (its selected route); a plan row ID is used as is.
    plan_row = next((row.get("planRowId") for row in facts.v3["rows"] if row["id"] == row_id), row_id)
    parts = []
    for basis in ("plan", "api"):
        key = plan_row if basis == "plan" else row_id
        band = result[basis]["bands"].get(key)
        mark = "†" if basis == "plan" and band is not None and key in result["planAssumedRouteRows"] else ""
        parts.append(DASH if band is None else (f"{band[0]}" if band[0] == band[1] else f"{band[0]}–{band[1]}") + mark)
    return " / ".join(parts)


def plotted_names_text(facts):
    """E214, O54: AA's plotted names as captured, so the fallback and no-effort statements cannot go stale."""

    state = facts.scores["aaPlottedNames"]
    return (f"AA plots {series(state['withFallback'])} only \"with fallback\", and every other cohort family ({series(state['withoutFallback'])}) without it; "
            "a third-party record matches by model and effort, and the build stops if AA plots one model and effort both ways (E214). "
            f"AA plots {series(state['noEffort'])} with no effort (O54, O66).")


def source_clocks_text(facts):
    """O59/O60: when each non-AA quality source was captured, and its own last update."""

    clocks = facts.v3["sourceClocks"]
    items = "; ".join(f"{clock['source']}, captured {clock['capturedAt']}" + (f" (source updated {clock['sourceUpdated'][:10]})" if clock["sourceUpdated"] else "")
                      for clock in clocks)
    return ("**Source clocks (owner decisions O59, O60).** Each non-AA quality source is captured at most 30 days before the release cutoff; "
            "a capture taken after the cutoff stands only when the source's own last update is dated before the cutoff's day. " + items + ".")


def listed_beyond_text(facts):
    """O58: the listed configurations whose cost lies outside a ranking's frozen anchors, per ranking."""

    parts = []
    for item_facts in [facts, *facts.tracks.values()]:
        items = [item for item in item_facts.v3["gates"]["listedBeyondAnchors"] if item["basis"] == "api"]
        label = q.TRACK_LABELS[item_facts.track]
        if not items:
            parts.append(f"{label}: no listed configuration lies beyond the API anchors.")
            continue
        listed = "; ".join(f"{item['name']} ({item['side']}, by a factor of {item['factor']:.1f}"
                           + (", a point on AA's rendered frontier" if item["renderedFrontier"] else "") + ")" for item in items)
        parts.append(f"{label}, listed beyond the API anchors: {listed}.")
    return " ".join(parts)


def listed_indicative_text(facts):
    """O41: a separated, non-ranked indicative value for each listed frontier or near-frontier family."""

    items = facts.v3["listedIndicative"]
    if not items:
        return ""
    rows = [[item["name"], ", ".join(LEAF_LABELS[key] for key in item["missing"]), fnum(item["quality"], 1), f"{100 * item['coverage']:.0f}%",
             fnum(item["plan"]["value"], 1), fnum(item["api"]["value"], 1), usd(item["api"]["costUsd"]), usd(item["plan"]["costUsd"])] for item in items]
    return ("\n\n**Listed frontier families: indicative value, not ranked and not comparable (O41).** Quality is the mean over the leaves the "
            "configuration has, renormalised, with no imputation, so these values cannot be compared with the ranking above.\n\n"
            + markdown_table(["Configuration", "Missing", "Quality (remaining leaves)", "Quality coverage", "Plan value (indicative)", "API value (indicative)",
                              "API cost (USD per basket run)", "Plan cost (USD per basket run)"], rows, numeric={2, 3, 4, 5, 6, 7}))


def separability_text(facts):
    """O39: how far apart two values must be to separate under benchmark sampling noise (independent-task approximation)."""

    result = facts.v3["diagnostics"]["rankSeparability"]
    api, plan = result["api"], result["plan"]
    grid = lambda item: ", ".join(f"{count} at correlation {rho}" for rho, count in item["byCorrelation"].items() if rho != "0.0")
    return (f" Benchmark sampling noise (O39, an independent-task approximation): two values must differ by about {api['medianSeparation']:.1f} value points "
            f"(median, 95%) to separate, and {api['separableAdjacentPairs']} of {api['adjacentPairs']} adjacent API ranks and {plan['separableAdjacentPairs']} of "
            f"{plan['adjacentPairs']} adjacent Plan ranks of different configurations do ({plan['sameConfigurationAdjacentPairs']} more adjacent Plan pairs are one "
            "configuration on two plans, ordered by the plans' multiples alone; E258). Its net direction is not established: every configuration is scored on the same tasks, which "
            f"correlates their errors and narrows the true threshold (API {grid(api)}; Plan {grid(plan)}), while sources it leaves out widen it (run-to-run and "
            f"harness variance, AA's single cost run and, for the {len(result['planAssumedRouteRows'])} Plan rows on an owner assumption ({plan_routes.assumption_counts_text(result.get('planAssumedRouteKinds') or {})}), that assumption's error). "
            "The noise band column groups each row with the band's first row it cannot be told apart from (O42); a Plan band marked † rests on an owner assumption "
            f"({plan_routes.assumption_kinds_text()}) and excludes its error: an assumed multiple can be wrong by a factor of about {plan['costTolerance']:.1f} before the row's value moves by the "
            "median threshold (a tolerance, not an estimate of the assumption's error). The S1T scenario shares in [scores.md](scores.md) "
            "show each row's rank-1 and top-3 frequencies under that noise." + aicd_narrow_text(api, plan))


def aicd_narrow_text(api, plan):
    """E263: AI Coding Daily's noise is read as six trials of the points share; the n = 60 reading is a sensitivity."""

    if "aicdNarrow" not in api:
        return ""
    return (" AI Coding Daily's noise treats its six graded projects as six trials of the share of 60 points (n = 6, the wide reading, E263); "
            f"read as 60 trials, the median threshold would be {api['aicdNarrow']['medianSeparation']:.1f} (API) and "
            f"{plan['aicdNarrow']['medianSeparation']:.1f} (Plan), with {api['aicdNarrow']['separableAdjacentPairs']} and "
            f"{plan['aicdNarrow']['separableAdjacentPairs']} adjacent ranks separable.")


def gap_fill_bars_text(result, facts):
    """E234: whether each bar's displayed-record cheapest row survives removing the gap fills or lowering them by the offset."""

    parts = []
    for basis, label in (("api", "API"), ("plan", "Plan")):
        for entry in result["bases"][basis]:
            if entry["survives"]:
                parts.append(f"{label} quality {entry['level']:.1f}: {facts.labels(entry['published']) or 'none'} in all three")
            else:
                parts.append(f"{label} quality {entry['level']:.1f}: {facts.labels(entry['published']) or 'none'} as published, {facts.labels(entry['removed']) or 'none'} "
                             f"with the fills removed, {facts.labels(entry['lowered']) or 'none'} with third-party fills lowered by the offset")
    offset = "no measured offset" if result["meanOffset"] is None else f"lowered by the mean offset {result['meanOffset']:.1f} points"
    return "- **Bar results without the gap fills (E234, sensitivity; labels unchanged):** cheapest displayed row as published, with fills removed, and with third-party fills " + offset + " — " + "; ".join(parts) + "."


def incomplete_text(facts):
    """O36/O38: the cohort configurations listed, not ranked, for a benchmark still missing after the logged search."""

    items = facts.v3["incompleteEvidence"]
    if not items:
        return ""
    frontier = {row["id"] for row in facts.scores["models"] if any(reason.startswith("Required AA") for reason in row.get("rankingInclusionReasons") or [])}
    parts = [f"{item['name']} ({'an AA frontier family; ' if item['id'] in frontier else ''}no {', '.join(LEAF_LABELS[key] for key in item['missing'])})" for item in items]
    return (f" Of these, {len(items)} qualify for the cohort but are listed, not ranked, because a benchmark is still missing after a logged search "
            f"(O36, O38): " + "; ".join(parts) + ".")


def agreement_text(result):
    """One agreement statistic: its label, status and, when defined, tau with its bootstrap interval and panel size."""

    if result["tau"] is None:
        return f"{result['label']}: {result['status']}; panel of {len(result['panel'])} rows."
    return f"{result['label']}: Kendall tau {result['tau']:.2f} (interval {result['interval'][0]:.2f} to {result['interval'][1]:.2f}) on {len(result['panel'])} rows."


def cost_diagnostics_markdown(facts):
    """Basket readiness (E22), the SWE companion (O14), the matched-cost object (E55), the leave-one-component-out
    family (E172) and the paired full/subset bridges with missing shares (E10, E173)."""

    diagnostics = facts.v3["diagnostics"]
    readiness, companion, matched = diagnostics["basketReadiness"], diagnostics["sweCompanion"], diagnostics["matchedCost"]
    pending = [component_label(key) for key, item in readiness["components"].items() if item["status"] != "admitted"]
    flagged = [row_id for row_id, item in companion["rows"].items() if item["flag"]]
    lines = [
        f"- **Basket readiness (E22):** priced leaves cover {pct(readiness['pricedMixCoverage'], 0)} of nominal quality weight ({names([LEAF_LABELS.get(key, key) for key in readiness['pricedLeaves']])}); pending components: {names(pending) or 'none'}.",
        f"- **SWE cost companion (O14, diagnostic):** {len(companion['rows'])} rows evaluated; flagged far from the median ratio: {facts.labels(flagged) if flagged else 'none'}.",
        f"- **Matched-cost diagnostic (E55):** {matched['status']}" + (f" at {pct(matched['pricedQualityWeight'], 0)} priced quality weight; basket/matched cost-order reversals with separated intervals: {len(matched['reversals'])}; rank-gap warnings: {len(matched['warnings'])}." if matched["status"] == "evaluated" else "."),
    ]
    family_rows = []
    for item in diagnostics["costComponentFamily"]:
        bases = item.get("bases", {})
        family_rows.append([component_label(item["component"])] + [
            rank_change_text(bases[basis]["recalibrated"]["rankChanges"]["changes"], facts.labels) if basis in bases else DASH for basis in ("api", "plan")
        ] + [fnum(bases["api"]["recalibrated"]["exchangeRate"]["valuePointsPerCostDoubling"], 2) if "api" in bases else DASH])
    frontier = diagnostics["frontierAnchors"]
    if frontier["status"] == "evaluated":
        lines.append(
            f"- **Frontier-families anchors (E187, diagnostic):** anchors rebuilt from the {len(frontier['references'])} frontier and near-frontier references move "
            + "; ".join(f"{label} {rank_change_text(frontier['bases'][basis]['rankChanges']['changes'], facts.labels)} (value points per cost doubling {fnum(frontier['bases'][basis]['exchangeRate']['valuePointsPerCostDoubling'], 2)} vs {fnum(frontier['bases'][basis]['frozenExchangeRate']['valuePointsPerCostDoubling'], 2)} frozen)" for basis, label in (("api", "API"), ("plan", "Plan")))
            + "."
        )
    else:
        lines.append(f"- **Frontier-families anchors (E187, diagnostic):** {frontier['status']}.")
    lines.append(policy_bar_text(frontier["bar"], facts))
    lines.append(family_primary_text(diagnostics["familyPrimary"], facts))
    lines.append(costed_ladder_text(diagnostics["costedBarLadder"], facts))
    lines.append(bar_currency_text(facts.v3["barCurrency"]))
    lines.append(mix_check_text(facts.v3["rows"]))
    lines.append(observed_range_text(facts.v3["observedRangeBars"], facts))
    lines.append(required_scores_text(facts.v3["requiredMissingScores"], facts))
    lines.append(common_leaf_text(diagnostics["commonLeaf"], facts))
    lines.append(harness_by_leaf_text(facts))
    lines.append(agent_safety_text(facts.v3["rows"]))
    bridge_lines = []
    for bridge in diagnostics["subsetBridges"]:
        missing = "; ".join(
            f"{component_label(key)} is {pct(share['median'], 0)} of the full basket (median; {pct(share['min'], 0)} to {pct(share['max'], 0)} over {share['n']} rows)"
            if share["n"] else f"{component_label(key)}: no expenditure evidence" for key, share in bridge["missingExpenditureShare"].items()
        )
        effects = []
        for basis, label in (("api", "API"), ("plan", "Plan")):
            result = bridge["bases"][basis]
            if result["status"] == "evaluated":
                spread = result["valueDifference"]
                effects.append(f"{label}: the full rows' values change by {fnum(spread['median'], 2)} points (median; {fnum(spread['min'], 2)} to {fnum(spread['max'], 2)}), {rank_change_text(result['rankChanges']['changes'], facts.labels)}")
            else:
                effects.append(f"{label}: {result['status']}")
        bridge_lines.append(f"- **{facts.labels(bridge['subsetRows'])}** (subset without {names([component_label(key) for key in bridge['missingComponents']])}): {missing}. Scored on its own subset anchors, the direction of its subset effect is not known. Paired bridge on the {len(bridge['pairedRows'])} full rows: {'; '.join(effects)}.")
    return "\n".join(lines) + "\n\n### Leave-one-component-out cost family (E172)\n\nEach admitted basket unit removed in turn, scored on anchors rebuilt by the freeze rule (rank changes against the primary ranking; quality held fixed).\n\n" + markdown_table(
        ["Removed component", "API rank changes", "Plan rank changes", "API value points per cost doubling"], family_rows, numeric={3}
    ) + "\n\n### Subset rows: paired bridge and missing spend (E10, E173)\n\n" + ("\n".join(bridge_lines) or "No row is scored on a subset workload.")


def diagnostics_markdown(facts):
    diagnostics = facts.v3["diagnostics"]
    harness = diagnostics["terminalBenchSameHarness"]
    agreement = diagnostics["qualityAgreement"]
    drift = diagnostics["groupDrift"]
    shares = diagnostics["qualitySourceShares"]
    abstention = diagnostics["omniscienceAbstentionSensitivity"]
    logistic = diagnostics["gdpvalLogisticSensitivity"]
    lines = [
        f"- **Terminal-Bench cross-source agreement (AA's {harness['defaultHarness']} run against tbench.ai):** {harness['agreement']['status']}; {len(harness['harnessMixed'])} rows take the leaf from tbench.ai (gap fill).",
        f"- **Rank separability (O39, independent-task approximation):** median separation {diagnostics['rankSeparability']['api']['medianSeparation']:.2f} value points (API) and "
        f"{diagnostics['rankSeparability']['plan']['medianSeparation']:.2f} (Plan); separable adjacent ranks: API {diagnostics['rankSeparability']['api']['separableAdjacentPairs']} of "
        f"{diagnostics['rankSeparability']['api']['adjacentPairs']}, Plan {diagnostics['rankSeparability']['plan']['separableAdjacentPairs']} of {diagnostics['rankSeparability']['plan']['adjacentPairs']}. "
        "Assumptions: " + "; ".join(diagnostics["rankSeparability"]["assumptions"]) + ".",
        f"- **FrontierCode against Cognition:** {agreement_text(diagnostics['frontierCodeCrossSource'])}"
        + (f" Cognition minus AA: mean {diagnostics['frontierCodeCrossSource']['meanOffset']:+.1f} points, largest {diagnostics['frontierCodeCrossSource']['maxAbsOffset']:.1f}."
           if diagnostics["frontierCodeCrossSource"]["tau"] is not None else ""),
        gap_fill_text(diagnostics["gapFillSensitivity"], facts),
        gap_fill_bars_text(diagnostics["gapFillBars"], facts),
        f"- **Quality agreement:** {agreement_text(agreement)}",
        *(f"- **Quality-substitution value agreement ({label}):** {agreement_text(diagnostics['qualitySubstitutionAgreement'][basis])}" for basis, label in (("api", "API"), ("plan", "Plan"))),
        f"- **Disjoint-evidence agreement:** {agreement_text(diagnostics['disjointEvidenceAgreement'])}",
        "- **Quality source shares:** " + ", ".join(f"{SOURCE_LABELS[source]} {share_value:.0%}" for source, share_value in shares.items()) + ".",
        f"- **Non-discriminating leaves:** {names(diagnostics['nonDiscriminatingLeaves'])}.",
        f"- **Group drift:** {drift['status']}" + ("; flagged: " + names([group for group, item in drift.get('groups', {}).items() if item['flag']]) if drift.get("groups") else "") + ".",
        f"- **Omniscience abstention sensitivity** ({abstention['rule']}): {rank_change_text(abstention['rankChanges']['changes'], facts.labels)}.",
        f"- **GDPval-AA logistic sensitivity** ({logistic['rule']}): API {rank_change_text(logistic['api']['rankChanges']['changes'], facts.labels)}; Plan {rank_change_text(logistic['plan']['rankChanges']['changes'], facts.labels)}.",
    ]
    stability = diagnostics["anchorStability"]
    lines.append(
        f"- **Anchor stability:** trimmed anchors ({stability['trimmedAnchors']['rule']}) give {usd(stability['trimmedAnchors']['low'])} to {usd(stability['trimmedAnchors']['high'])}; "
        f"{rank_change_text(stability['trimmedRankShifts']['changes'], facts.labels)}."
    )
    deletion_rows = []
    for branch in diagnostics["deletionSensitivity"]:
        cells = [branch["id"], pct(branch["retainedNominalWeight"], 0), branch["status"]]
        for basis in ("api", "plan"):
            result = (branch.get("bases") or {}).get(basis)
            cells.append(rank_change_text(result["rankChanges"]["changes"], facts.labels) if result else DASH)
        deletion_rows.append(cells)
    removal = diagnostics["costRemoval"]
    removal_rows = [
        [basis, item[key]["label"] + (f"; {item['multiplePolicy']}" if item["multiplePolicy"] else ""), rank_change_text(item[key]["rankChanges"]["changes"], facts.labels)]
        for basis, item in removal.get("bases", {}).items()
        for key in ("fixedAnchors", "recalibrated")
    ]
    return "\n".join(lines) + "\n\n" + cost_diagnostics_markdown(facts) + "\n\n### Deletion sensitivity\n\n" + markdown_table(
        ["Branch", "Retained nominal weight", "Status", "API rank changes", "Plan rank changes"], deletion_rows, numeric={1}
    ) + f"\n\n### Cost-component removal ({component_label(removal['component'])}: {removal['status']})\n\n" + markdown_table(["Basis", "Run", "Rank changes"], removal_rows)


# --- raw data ----------------------------------------------------------------------------------


def leaf_input_rows(facts, seen):
    """Every ranked row's leaf inputs in the active ranking, skipping (configuration, leaf) pairs already listed."""

    rows = []
    for entry in facts.ranked:
        row = facts.row(entry)
        audit = {item["leaf"]: item for item in row["quality"]["clipAudit"]}
        for leaf in q.LEAVES:  # O36: a ranked row has every leaf
            if (row["id"], leaf.key) in seen:
                continue
            seen.add((row["id"], leaf.key))
            detail = row["quality"]["leaves"][leaf.key]
            evidence = detail.get("evidence") or {}
            rows.append([
                configuration_label(row, facts.names), leaf.label, audit[leaf.key]["raw"], audit[leaf.key]["unit"], fnum(detail["z"], 2),
                " / ".join(str(part) for part in (detail.get("configuration"), detail.get("agent")) if part) or DASH,
                f"`{evidence['artifact']}` `{evidence['locator']}`" if evidence else DASH,
            ])
    return rows


def raw_data(facts):
    v3 = facts.v3
    seen = set()
    leaf_rows = leaf_input_rows(facts, seen)
    # O53: the other rankings' rows and leaves (an AI Coding Daily-only configuration, AI Coding Daily itself).
    for track, other in facts.tracks.items():
        with q.active_track(track):
            leaf_rows += leaf_input_rows(other, seen)
    component_rows = []
    reconciliation_rows = []
    for entry in facts.ranked:
        row = facts.row(entry)
        for key, item in row["cost"]["componentsDetail"].items():
            detail = item.get("detail") or {}
            component_rows.append([
                configuration_label(row, facts.names), component_label(key), usd(item["costUsd"]), item["completeness"],
                detail.get("tasks", DASH), usd(detail.get("costPerTaskUsd"), 4), item["source"],
            ])
        check = row["cost"]["indexReconciliation"]
        reconciliation_rows.append([
            configuration_label(row, facts.names), usd(check.get("sdlcSevenUsd")), usd(check.get("residualUsd")),
            usd(check.get("reconstructedTotalUsd")), usd(check.get("publishedTotalUsd")), "yes" if check.get("reconciled") else "no",
        ])
    bug_rows = [
        [facts.names.get(record["modelId"], record["modelId"]), record["evaluatedModel"], fnum(record["fixedOf105"], 1), record["sampleN"], record["effort"], record["harness"]]
        for record in facts.bug_hunt["models"]
        if record.get("matched") is True
    ]
    route_rows = [
        [route["planLabel"], names([facts.names.get(model_id, model_id) for model_id in route["modelIds"]]), usd(route.get("planPriceUsd")),
         f"{route['valueMultiple']:g}×", plan_evidence_label(route), route.get("sourceModel") or DASH, route.get("sourcePublicationDate") or DASH,
         md_link("Source", route.get("sourceUrl")) if route.get("sourceUrl") else "User assumption"]
        for route in facts.routes_document["routes"]
    ]
    amount_rows = [
        [facts.label(row["id"]), usd(row["plan"]["amount"]["amountUsd"], 0), row["plan"]["amount"]["amountTarget"], row["plan"]["amount"]["derivation"],
         row["plan"]["amount"]["workload"], row["plan"]["amount"]["cashObjectId"], row["plan"]["amount"]["measurementObjectId"]]
        for row in v3["rows"]
        if row["plan"]["amount"]
    ]
    ranked_ids = {row["id"] for row in v3["rows"]}
    fill_rows = [
        [facts.names.get(item["modelId"], item["modelId"]), LEAF_LABELS[item["leaf"]], f"{item['value']:g}", item["unit"], SOURCE_TYPE_LABELS[item["sourceType"]],
         item.get("publisher") or DASH, item.get("configuration") or DASH, item["benchmarkVersion"], item["metric"], md_link("Source", item["url"]) if item.get("url") else DASH]
        for item in facts.leaf_evidence["supplements"] if item["modelId"] in ranked_ids
    ]
    search_rows = [
        [facts.names.get(item["modelId"], item["modelId"]), LEAF_LABELS[item["leaf"]], item["searchedOn"], item["result"], len(item.get("sources") or []),
         open_web_text(item.get("openWeb")), item.get("notes") or DASH]
        for item in facts.leaf_evidence["searches"]
    ]
    bundle = v3["evidenceBundle"]
    bundle_rows = [[item["key"], f"`{item['artifact']}`", f"`{item['sha256']}`", item.get("capturedAt") or DASH, item.get("extractor") or DASH] for item in bundle["artifacts"]]
    deepswe = facts.deepswe["configurations"]
    tb4 = facts.tb4
    return f"""# ValueRank {VERSION} Raw Data

**Updated:** {DATE} · methodology {v3['methodologyVersion']}

Every input behind the published scores, with the artifact and locator that holds it. Generated from the committed snapshots in [data/](data/); nothing here is edited by hand.

## Quality leaf inputs

{markdown_table(['Configuration', 'Leaf', 'Raw value', 'Unit', 'Score z', 'Evaluated configuration / agent', 'Evidence'], leaf_rows, numeric={2, 4})}

## Leaf gap fills and searches (O36)

Leaves a ranked configuration takes from beyond its primary source, in the order a newer AA capture, another party's run of the same benchmark on the exact configuration, then the model provider's published result (O36/O37). Tbench.ai Terminal-Bench rows used as gap fills are in the leaf inputs above with their agent.

{markdown_table(['Configuration', 'Leaf', 'Value', 'Unit', 'Source type', 'Publisher', 'Evaluated configuration', 'Benchmark version', 'Metric (E237)', 'Source'], fill_rows, numeric={2})}

Exhaustive searches for the leaves a cohort configuration still lacks (each within {LEAF_SEARCH_DAYS} days of the cutoff; the configuration is listed, not ranked). The sources searched are in [data/leaf_evidence.json](data/leaf_evidence.json).

{markdown_table(['Configuration', 'Leaf', 'Searched', 'Result', 'Sources checked', 'Open-web discovery (E240)', 'Notes'], search_rows, numeric={4})}

## Basket cost components

{markdown_table(['Configuration', 'Component', 'Cost (USD)', 'Completeness', 'Tasks', 'USD per task', 'Source'], component_rows, numeric={2, 4, 5})}

### AA Index total reconciliation

The seven Index components plus AA's residual reproduce AA's published Intelligence Index total cost.

{markdown_table(['Configuration', 'Index SDLC components', 'Residual', 'Reconstructed total', 'Published total', 'Reconciled'], reconciliation_rows, numeric={1, 2, 3, 4})}

## DeepSWE v1.1 AA chart configurations (withdrawn by AA, not scored)

AA withdrew DeepSWE v1.1 from its Coding Agent Index (v2.0, October 2026) and the owner dropped it as a quality leaf in favour of FrontierCode (O49); this is AA's last capture, kept for the record. The AA chart published {len(deepswe)} DeepSWE v1.1 configurations across {facts.deepswe['benchmarkTasks']} tasks, observed {facts.deepswe.get('observedAt', DASH)}. Each keeps its displayed agent, model and effort; only exact matches enter a score.

| # | Agent | Evaluated model variant | Effort | pass@1 | ValueRank match | Note |
|---:|---|---|---|---:|---|---|
{deepswe_chart_table(deepswe)}

## Terminal-Bench 4.0 official rows

{tb4['rowN']} official rows ({tb4['matchedN']} of {tb4['cohortN']} cohort matches), observed {tb4.get('observedAt', DASH)}. The published ± is the source's 95% confidence interval (used by stream S1M). {selected_agents_text(facts, tb4)}

| Rank | Base model | Agent | Resolution rate | Tokens | Cost |
|---|---|---|---:|---|---:|
{tb4_table(tb4['rows'])}

## Bug Hunt Bench matched runs

Owner-published runs at commit `{facts.bug_hunt['sourceCommit']}`; the score is the owner's largest-sample mean of bugs fixed of 105 for the exact model and effort, with the harness that result was run on (E206). {cross_harness_text(facts)}

{markdown_table(['Model', 'Evaluated model', 'Bugs fixed of 105', 'Runs', 'Effort', 'Harness'], bug_rows, numeric={2, 3})}

## Plan routes

Route evidence as of {facts.routes_document['asOf']}. Full allocation regimes, workloads and notes are in [data/plan_cost_routes.json](data/plan_cost_routes.json).

{markdown_table(['Plan', 'Eligible configurations', 'Monthly fee', 'Value Multiple', 'Evidence', 'Source model', 'Source date', 'Source'], route_rows, numeric={2, 3})}

### Plan amounts and their lineage

Each routed row's amount with what it measures, how it was derived and which objects it comes from (E166, E168); API-fallback rows have none.

{markdown_table(['Configuration', 'Amount (USD per fee period)', 'Measures', 'Derivation', 'Workload', 'Cash object', 'Measurement object'], amount_rows, numeric={1})}

## Evidence bundle

Bundle hash `{bundle['bundleHash']}`: {bundle['rebuild']}.

{markdown_table(['Key', 'Artifact', 'SHA-256', 'Captured', 'Extractor'], bundle_rows)}
""" + facts.reconciliation_md


# --- entry point -------------------------------------------------------------------------------


def main(*, root=ROOT, data=DATA) -> int:
    """Emit every Markdown output beneath ``root`` from the snapshots in ``data``."""

    facts = Facts(data)
    documents = {
        "README.md": readme(facts),
        "methodology.md": methodology(facts),
        "scores.md": scores_markdown(facts),
        "raw-data.md": raw_data(facts),
    }
    # E155: no published sentence may put a source interval or run range into scenario shares without an admitting stream.
    violations = [f"{name}: {sentence}" for name, text in documents.items() for sentence in scenarios.lint_release_text(text)]
    if violations:
        raise ValueError("release-text lint (E155) rejects: " + " | ".join(violations))
    for name in OUTPUTS:
        (root / name).write_text(documents[name])
    print(json.dumps({
        "version": VERSION,
        "methodology": facts.v3["methodologyVersion"],
        "configurations": len(facts.rows),
        "outputs": list(OUTPUTS),
    }, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
