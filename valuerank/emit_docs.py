#!/usr/bin/env python3
"""Emit the Markdown publication for methodology v3: README, methodology, score tables and raw data.

Every number comes from the ``v3`` section of ``data/scores.json``, read through the site view model
(``valuerank.site.viewmodel.build_bundle``) so the Markdown and the website state the same values.
The website under site/ is owned by ``python -m valuerank.site.build``.
"""

from __future__ import annotations

import json
import statistics

from valuerank import basket
from valuerank import quality as q
from valuerank import scenarios
from valuerank.aa_reconciliation import publication as aa_reconciliation_publication, reconcile as reconcile_aa
from valuerank.paths import DATA, ROOT
from valuerank.publication import (
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
    ("Exact AA DeepSWE and eligible Bug Hunt overlap", "Exact DeepSWE and Bug Hunt results for the exact configuration (O31, O33)"),
)
LEAF_TRANSFORMS = {
    "deepswe": "z = pass@1 %",
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
}
SOURCE_LABELS = {"aa": "AA-run", "independent": "independent"}
# Owner-authorised route applications in the Plan evidence policy, printed when recorded.
POLICY_APPLICATIONS = (
    ("gptApplication", "GPT"),
    ("claudeApplication", "Claude"),
    ("mimoApplication", "MiMo"),
    ("unsupportedModels", "Other models"),
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
    ("provisional quality", "observed leaves cover under 70% of quality weight, fewer than two software-engineering leaves or under 40% software-engineering weight are observed, or DeepSWE is missing; ranked and flagged, never floored (O8)"),
    ("partial component", "AA marks tasks of a basket component missing or declined (E37), or the component's cost cannot be reconciled with AA's prices (E170)"),
    ("valuation basis unverified", "AA's cost reconciles with neither its displayed prices nor a registered price record; ranked, but outside interval outputs and cost anchors (E170 outcome 4)"),
    ("no cost", "AA publishes no cost for the configuration, so it has no value score and no rank (AGENTS.md); its quality is shown"),
    ("AA cost caveat", "AA states that its published cost omits a pricing term"),
    ("API-cost fallback", "no admitted Plan route; the Plan ranking uses the API cost (O13)"),
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
        lines += ["", "Near-frontier families and each family's near point closest to the frontier (a family's primary configuration is its configuration with exact DeepSWE and Bug Hunt results when it has one, O30, and every other effort with both results is ranked as its own row, O33, so the ranked configurations can differ):", ""]
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
        "provisional quality": entry["coverage"]["provisional"],
        "partial component": bool(cost["partialComponents"]),
        "valuation basis unverified": (row.get("valuationGate") or {}).get("outcome") == "valuation basis unverified" and cost["apiUsd"] is not None,
        "no cost": cost["apiUsd"] is None,
        "AA cost caveat": bool(row.get("aaCostCaveat")),
        "API-cost fallback": cost["fallback"] is not None,
    }
    return ", ".join(word for word, _text in FLAG_LEGEND if present[word]) or DASH


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

    def __init__(self, data):
        self.bundle = viewmodel.build_bundle(data)
        self.scores = json.loads((data / "scores.json").read_text())
        self.routes_document = json.loads((data / "plan_cost_routes.json").read_text())
        self.deepswe = json.loads((data / "aa_deepswe.json").read_text())
        self.tb4 = json.loads((data / "tb4.json").read_text())
        self.bug_hunt = json.loads((data / "bug_hunt.json").read_text())
        self.v3 = self.scores["v3"]
        self.rows = {row["id"]: row for row in self.v3["rows"]}
        self.names = {model["id"]: model["name"] for model in self.scores["models"]}
        self.rankings = self.bundle.rankings
        self.ranked = [entry for entry in self.rankings["models"] if entry["rankingEligible"]]
        self.unranked = [entry for entry in self.rankings["models"] if not entry["rankingEligible"]]
        self.method = self.bundle.extras["method"]
        self.inclusion = model_inclusion(self.scores.get("frontierSelection"), self.scores["models"])
        self.cost_pct = self.rankings["costWeightPct"]
        self.quality_pct = 100.0 - self.cost_pct
        reconciliation, _html = aa_reconciliation_publication(reconcile_aa(data=data))
        self.reconciliation_md = reconciliation

    def row(self, entry):
        return self.rows[self.source_id(entry)]

    def source_id(self, entry):
        return next(model["id"] for model in self.scores["models"] if viewmodel.slugify(model["id"]) == entry["slug"])

    def label(self, model_id):
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
    labels = ", ".join(component_label(key) for key in CODING_COMPONENTS)
    unrewarded = _median_share(v3, UNREWARDED_COMPONENTS)[0]
    return (f" Coding and terminal tasks ({labels}) make up {pct(middle, 0)} of the basket's cost (median over {n} configurations "
            f"with the full basket; {pct(low, 0)} to {pct(high, 0)}); {', '.join(component_label(key) for key in UNREWARDED_COMPONENTS)}, "
            f"which have no quality leaf, make up {pct(unrewarded, 0)}.")


def influence_text(v3, short=False):
    """E196: cost's nominal weight beside its share of the variance in value on the common panel (E189)."""

    shares = {basis: (v3["costInfluence"][basis]["commonWorkload"]["varianceAllocation"] or {}).get("cost") for basis in ("api", "plan")}
    if None in shares.values():
        return ""
    if short:
        return f"; {pct(shares['api'], 0)} of API and {pct(shares['plan'], 0)} of Plan value variance"
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
    return sentences


def run_label(run):
    return run["stratum"] + (" endpoint-heavy" if run["alternative"] else "")


# --- README ------------------------------------------------------------------------------------


def leaders(facts):
    """One sentence naming each basis' leader (with its subset and provisional caveats) and the quality leader."""

    parts = []
    for basis, label in (("plan", "Plan"), ("api", "API")):
        leader = min((entry for entry in facts.ranked if entry["rank"][basis] is not None), key=lambda entry: (entry["rank"][basis], entry["name"]))
        transfer = basis == "plan" and (leader["cost"]["route"] or {}).get("grade") == "assumption"
        caveats = [word for word, present in (("subset cost", leader["cost"]["subset"]), ("provisional quality", leader["coverage"]["provisional"]), ("owner-named transfer", transfer)) if present]
        parts.append(f"{leader['name']} leads the {label} ranking at {leader['overall'][basis]:.1f}" + (f" ({', '.join(caveats)})" if caveats else ""))
    quality = min(facts.ranked, key=lambda entry: (entry["qualityRank"], entry["name"]))
    return "; ".join(parts) + f"; {quality['name']} leads on quality."


def readme(facts):
    v3, method = facts.v3, facts.method
    admitted = [item["label"] for item in method["basket"]["admitted"]]
    yield_ = v3["identificationYield"]
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
            short_flags(entry, row),
        ])
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

ValueRank ranks frontier AI model configurations (see Model inclusion) by value for software engineering and DevOps work, separately for API buyers and for subscription (Plan) buyers. Value is a fixed **{facts.cost_pct:.0f}%** cost score plus **{facts.quality_pct:.0f}%** benchmark quality.{influence_text(v3)} Cost is the {method['costLabel']}: Artificial Analysis' (AA) published cost of running the {series(admitted)} once at API rates, scored on a log scale against frozen anchors so cost ratios keep their size.{coding_share_text(v3)} Quality is the weighted mean of {len(q.LEAVES)} benchmark leaves on fixed 0–100 anchors, over the leaves observed for the exact configuration; missing evidence is never filled in. The Plan ranking divides the basket's API cost by the selected subscription route's Value Multiple at full utilisation, and uses the API cost, flagged, when no route is admitted.{exploratory}

{leaders(facts)}

{markdown_table(['Plan rank', 'API rank', 'Configuration', 'Plan value', 'API value', 'Quality', 'Quality coverage', 'API cost (USD per basket run)', 'Plan cost (USD per basket run)', 'Plan route', 'Flags'], table_rows, numeric={0, 1, 3, 4, 5, 6, 7, 8})}

Values are rounded for display; ranks are competition ranks (equal values share the better rank).

{legend}

Not ranked ({len(facts.unranked)} roster models): {names([entry['name'] for entry in facts.unranked])}. Reasons are listed in [scores.md](scores.md#not-ranked).

### What the evidence supports

{intervals}

Scenario shares by stream, diagnostics and the release gates are in [scores.md](scores.md); the inputs behind every number are in [raw-data.md](raw-data.md).

{model_inclusion_markdown(facts.inclusion)}
## How v3 scores value

- **Cost is the SDLC basket.** {v3['basketVersion']}: AA's published cost of running the {series(admitted)} once at API rates, in USD per basket run. Pending capture: {names([item['label'] for item in method['basket']['pending']])}. v2 used AA's cost to run the whole Intelligence Index per Index point.
- **Cost keeps its magnitude.** The cost score is 100 × (ln c_H − ln c) / (ln c_H − ln c_L), clipped to 0–100, against anchors frozen with anchor version `{v3['anchorVersion']}`. A model entering or leaving the cohort does not move another model's score. At the API anchors, doubling cost costs {method['exchangeRate']['api']['valuePointsPerCostDoubling']:.2f} value points, which {method['exchangeRate']['api']['qualityPointsPerCostDoubling']:.2f} quality points offset.
- **Quality is measured, not ranked.** Each of the {len(q.LEAVES)} leaves is placed on fixed 0–100 anchors from its raw value, so quality no longer depends on which other models are ranked. A missing leaf is left out of that configuration's mean, its coverage is shown, and low coverage marks the row provisional.
- **Plan value is route evidence.** Each subscription route carries its Value Multiple, evidence grade (controlled measurement, concordant reports, owner-named assumption) and identification status; the Plan ranking is labelled exploratory until multiples are identified on the basket.
- **Uncertainty is shown, not hidden.** Interval outputs certify which frontier and cheapest-above-a-bar claims the published record supports; scenario shares report frequencies over declared streams.
- v3 values are not numerically comparable with v2 or earlier releases.

## Sources and audit trail

- [Artificial Analysis methodology]({AA_METHODOLOGY_URL}) and its model pages: Intelligence Index component scores and the per-task evaluation costs of the basket.
- [AA Coding Agent Index, DeepSWE v1.1]({AA_DEEPSWE_URL}): DeepSWE pass@1 and the Coding Agent Index cost for each exact configuration.
- [Terminal-Bench 4.0]({TERMINAL_BENCH_URL}) official leaderboard rows and [Bug Hunt Bench]({BUG_HUNT_URL}) owner-published runs.
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
    leaf_rows = [
        [md_link(leaf.label, viewmodel.LEAF_INFO[leaf.key]["url"]), q.GROUP_LABELS[leaf.group], f"{leaf.weight:.2f}%", f"{facts.quality_pct * leaf.weight / 100:.2f}%",
         viewmodel.LEAF_INFO[leaf.key]["unit"], LEAF_TRANSFORMS[leaf.key], "AA-run" if leaf.source == "aa" else "independent"]
        for leaf in q.LEAVES
    ]
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

{cohort_lines}

The remaining {len(facts.unranked)} roster models are not ranked; each keeps a page with the evidence held for it.

{model_inclusion_markdown(facts.inclusion)}
## Value

Value on a basis = **{facts.cost_pct:.0f}%** × cost score + **{facts.quality_pct:.0f}%** × quality score (owner decision, 2026-10-19). Both scores run from 0 to 100, higher is better. Cost's share is fixed: a configuration missing quality evidence keeps cost at {facts.cost_pct:.0f}%, and a configuration without a cost score has no value score. Ranks are competition ranks; equal values share the better rank.

## Cost: the SDLC basket

The cost figure is the **{boundary['label']}**. {v3['basketVersion']} holds the components the admission rule admits ({admission['selectionRule']}); its reference panel is {admission['jointCovered']} of the {len(facts.rows)} ranked configurations (at least {admission['requiredPanelSize']} required):

{markdown_table(['Component', 'Status', 'Exact cost available', 'Complete', 'Ranked'], component_rows, numeric={2, 3, 4})}

A configuration's basket cost is the sum of AA's published costs for the admitted components at that exact model and effort: each Intelligence Index component is AA's cost per task times its task count, and the Coding Agent Index cost is read from AA's chart (rounded to USD 1). The Index components plus AA's residual reproduce AA's published Index total for every configuration (see raw-data.md).

**Cost boundary.** Source: {boundary['source']}. AA's cost covers the contestant model's API tokens; other charges are included, excluded or unknown per component:

{markdown_table(['Component'] + [CHARGE_LABELS[name] for name in boundary['chargeClasses']], boundary_rows)}

**Subset workloads (O17).** A configuration without exact cost for an admitted component is scored on the workload made of the components it has, against that workload's own frozen anchors, and flagged "subset cost"; its ordering against main-workload configurations is not identified. A component AA marks with missing or declined tasks is flagged "partial component" (E37).

## Cost score and anchors

Cost score S_C = 100 × (ln c_H − ln c) / (ln c_H − ln c_L), clipped to 0–100. The anchors are frozen per workload and basis: c_L is half the cheapest reference cost and c_H twice the dearest, so no reference configuration clips. A release is held when more than max(1, 10% of ranked rows) clip on a basis or any row lies beyond an anchor by more than a factor of 2 (owner decision O12).

{markdown_table(['Workload', 'Basis', 'Low anchor c_L (USD)', 'High anchor c_H (USD)', 'References', 'Status'], anchor_rows, numeric={2, 3, 4})}

**Anchor policy** (`{policy['policyId']}` v{policy['version']}). Population: {policy['populationRule']}. Plan anchors: {policy['planRule']}. At least {policy['minimumReferences']} references; below that, {policy['belowMinimum']}. Lifetime: {policy['lifetime']}.

**Exchange rate.** In the unclipped region a cost doubling changes value by −100 × {v3['beta']} × ln 2 / ln(c_H / c_L) points, offset by +100 × {v3['beta']} × ln 2 / ((1 − {v3['beta']}) × ln(c_H / c_L)) quality points. At the main-workload anchors:

{markdown_table(['Basis', 'Anchor ratio c_H / c_L', 'Value points per cost doubling', 'Quality points that offset it'], rate_rows, numeric={1, 2, 3})}

**Within-cohort influence (E91, E126).** Cost's share of the value dispersion on the common-workload panel, 0.25 × SD(S_C) / (0.25 × SD(S_C) + 0.75 × SD(S_Q)), is published and flagged below 10% or above 90%; the flag is informational and the cost weight never changes (O2). Because cost and quality covary, that ratio describes dispersion; the value-variance allocation Cov(0.25 S_C, V) / Var(V) and the Kendall tau of the cost-only and quality-only orderings against the value ordering show contribution (E189).

{markdown_table(['Basis', 'Panel', "Cost's share", 'Status', "Cost's variance allocation", 'Tau, cost vs value', 'Tau, quality vs value'], influence_rows, numeric={1, 2, 4, 5, 6})}

## Quality

Quality is the weighted mean of the leaves observed for the exact configuration, each placed on fixed 0–100 anchors from its raw value (clipped, with saturation disclosed). Group shares of quality: {', '.join(f"{q.GROUP_LABELS[group]} {share_value:.0f}%" for group, share_value in q.GROUPS.items())}.

{markdown_table(['Leaf', 'Group', 'Weight in quality', 'Weight in value', 'Raw unit', 'Score', 'Run by'], leaf_rows, numeric={2, 3})}

Coverage is the observed share of quality weight. A row is **provisional** when coverage is below {q.MIN_COVERAGE:.0%}, fewer than {q.MIN_SWE_LEAVES} software-engineering leaves are observed, observed software-engineering weight is below {q.MIN_SWE_WEIGHT:.0%}, or a leaf weighing {q.REQUIRED_LEAF_WEIGHT:.0f}% or more of quality (DeepSWE) is missing. Provisional rows are ranked and flagged; there is no quality floor (O8). Missing leaves are never filled; the interval outputs treat each one as anywhere in 0–100.

## Plan basis

Plan cost = basket API cost ÷ the Value Multiple of the selected subscription route, at full utilisation. A Value Multiple is the API-priced usage a subscription delivers per dollar of fee. Route evidence is graded: **controlled** measurements of the exact model, **reports** (at least two independent, comparable end-user reports concordant within 20%), owner-named **assumptions** (a measured multiple transferred to another model, labelled), and **diagnostic** evidence, which is shown but never ranked. Routes certifiably dearer than another identified route of at least equal grade are set aside (E88); the official route is then chosen by identification class, evidence grade, the comparison multiple, lower gross cash and route ID (E85). Evidence past its 90-day expiry and 30-day grace is demoted to diagnostic. A configuration without an admitted route uses its API cost, flagged. Each Plan row publishes its fee period, the cash paid and the selected multiple's amount (multiple × gross cash), typed by what the measurement establishes (E166): measured-workload capacity, observed eligible consumption with capacity not established, assumed API-equivalent consumption for an owner-named transfer (with its donor), or identified target-workload capacity; API-fallback rows publish none.

**Identification (E61).** A multiple is measured on its own workload; it identifies the basket's multiple only when the workloads match. Today {yield_['pointIdentified']} of {yield_['rows']} Plan rows are point-identified and {yield_['setIdentified']} set-identified, so the Plan ranking is {'labelled exploratory' if yield_['exploratory'] else 'not labelled exploratory'}. A measured-only Plan view (`{measured['id']}`) re-runs the selection over {measured['admission']}, without transfers or fallbacks. Because the official Plan anchors include transfers and fallbacks, a calibration diagnostic rescores the measured-only rows on anchors built from measured evidence alone (E164), so an assumption's effect through the exchange rate is visible.

**Subscription evidence policy** (as of {facts.routes_document['asOf']}; reporting window {routes_policy['reportingWindow']['start']} to {routes_policy['reportingWindow']['end']}):

- Default numerator: {routes_policy['defaultNumerator']}
- Selected source for {', '.join(exception['providers'])}: [SemiAnalysis]({exception['sourceUrl']}) ({exception['publicationDate']}, owner-selected {exception['authorizedOn']}): {exception['evidenceType']}
{policy_lines}
- Provider allowance, quota and marketing figures never supply the measured numerator; a provider's published price can be the fee denominator only when the tier mapping is supported.

## Uncertainty outputs

**Interval outputs (O25).** Each observed leaf is placed anywhere inside its published reporting precision, each missing leaf anywhere in 0–100 and each cost inside its rounding. A configuration is on the **definite frontier** when no other configuration can beat it on both cost and quality for any values in those boxes, and on the **possible frontier** when some values put it there. The **cheapest above a quality bar** is confirmed only when its worst cost is below the best cost of every other configuration that could qualify. The bar is pinned by policy `{bar['policyId']}` v{bar['version']}: the {bar['position']} of {bar['populationRule']}, ordered by {bar['order']}, selected {bar['selectionMode']}; {bar['reference']}; {bar['nonTautology']}; {bar['lifetime']}. Current headline bar: {method['barLevel'] or 'none'}{"; ladder: " + ", ".join(method["barLadder"]) if method.get("barLadder") else ""}.

**Scenario shares** are frequencies over declared streams, never probabilities ({scenario_scope}):

{streams}

S1 also runs with the endpoint-heavy kernel. On the Plan basis the core streams (S1, S2 and S1M) run with owner-named transfers off (E167): a row whose selected route is a transfer is unevaluable there, never reselected or replaced by API cost, while S0 keeps the displayed record. {interval_notes}A cheapest-above-the-bar label is published only when the share clears a sequential threshold with its per-look error controlled. Not quantified in these shares:

{not_quantified}

## Diagnostics

Diagnostics are published beside the ranking and never change a score: Terminal-Bench same-harness agreement, anchor stability (exchange-rate series and trimmed-anchor rank shifts), Omniscience abstention sensitivity, quality source shares, matched-panel quality agreement, non-discriminating leaves, group drift, quality dispersion, deletion sensitivity (leave-one-benchmark-out and source deletions) and the standing removal of the Terminal-Bench cost component. Current results are in [scores.md](scores.md#diagnostics).

## Release gates

{markdown_table(['Rule', 'Status', 'Detail'], gate_rows)}

## Limitations

{limitations}

## Machine-readable files

- [data/scores.json](data/scores.json): the `v3` section holds every row, workload, anchor, interval output, scenario result, diagnostic and the evidence bundle
- [data/plan_cost_routes.json](data/plan_cost_routes.json): subscription routes, their evidence, sources and policy
- [data/v3_frozen.json](data/v3_frozen.json): frozen anchors, bar policy and anchor policy for anchor version `{v3['anchorVersion']}`
- [data/v3_scenarios.json](data/v3_scenarios.json): scenario-share runs for every stream
- [data/aa_deepswe.json](data/aa_deepswe.json), [data/tb4.json](data/tb4.json), [data/bug_hunt.json](data/bug_hunt.json): independent benchmark snapshots
"""


def md_link(label, url):
    return f"[{label}]({url})" if url else label


# --- scores ------------------------------------------------------------------------------------


def scores_markdown(facts):
    v3 = facts.v3
    ranking_rows = []
    for entry in facts.ranked:
        row = facts.row(entry)
        ranking_rows.append([
            model_link(entry, configuration_label(row, facts.names)),
            rank_text(entry["rank"]["plan"]), fnum(entry["overall"]["plan"], 2), fnum(entry["costDims"]["plan"], 2),
            rank_text(entry["rank"]["api"]), fnum(entry["overall"]["api"], 2), fnum(entry["costDims"]["api"], 2),
            fnum(entry["quality"], 2), f"{entry['coverage']['pct']:.0f}%", workload_text(entry),
        ])
    leaf_headers = ["Configuration"] + [leaf.label for leaf in q.LEAVES] + ["Quality", "Provisional"]
    leaf_rows = []
    for entry in facts.ranked:
        row = facts.row(entry)
        leaves = row["quality"]["leaves"]
        leaf_rows.append(
            [configuration_label(row, facts.names)]
            + [fnum(leaves[leaf.key]["z"], 1) if leaf.key in leaves else DASH for leaf in q.LEAVES]
            + [fnum(row["quality"]["displayed"], 2), "; ".join(row["quality"]["provisionalReasons"]) or "no"]
        )
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
            configuration_label(row, facts.names), route_text(entry), plan_amount_text(plan["amount"]), plan.get("selectedIdentification") or DASH,
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
        [facts.label(model_id), item["status"], item.get("routeId") or DASH, usd(item.get("costUsd")), fnum(item.get("value"), 2), item.get("rank") or DASH]
        for model_id, item in sorted(measured["rows"].items(), key=lambda pair: (pair[1].get("rank") is None, pair[1].get("rank") or 0, facts.label(pair[0])))
    ]
    unranked_rows = [[entry["name"], "; ".join(entry["exclusionReasons"]) or DASH] for entry in facts.unranked]
    return f"""# ValueRank {VERSION} Scores

**Updated:** {DATE} · methodology {v3['methodologyVersion']} · {v3['basketVersion']} · anchor version `{v3['anchorVersion']}`

Value = {facts.cost_pct:.0f}% × cost score + {facts.quality_pct:.0f}% × quality. Costs are USD per basket run; the cost score is log-scaled against the frozen anchors of the row's workload (see [methodology.md](methodology.md)).

## Ranking

{markdown_table(['Configuration', 'Plan rank', 'Plan value', 'Plan cost score', 'API rank', 'API value', 'API cost score', 'Quality', 'Quality coverage', 'Workload'], ranking_rows, numeric={1, 2, 3, 4, 5, 6, 7, 8})}

## Not ranked

{markdown_table(['Model', 'Reasons'], unranked_rows)}

## Quality leaf scores

Each leaf's score z on its fixed 0–100 anchors; "—" marks a leaf with no eligible exact-configuration result.

{markdown_table(leaf_headers, leaf_rows, numeric=set(range(1, len(q.LEAVES) + 2)))}

## Basket cost by component

USD at API rates for the exact configuration; "—" marks a component without an exact cost.

{markdown_table(['Configuration'] + [component_label(key) for key in components] + ['Basket cost', 'Missing admitted components'], cost_rows, numeric=set(range(1, len(components) + 2)))}

### Valuation basis

Valuation-basis gate (E170): {gate_counts}{(' (flagged: ' + facts.labels(flagged_gate) + ')') if flagged_gate else ''}. AA's Index category costs reconcile exactly with the prices AA displays for each configuration at capture, so its applied prices are the prices in force at the release cutoff. Token metering (E176): {metering}; AA values cached input at live measurements of each model's typical cache-hit rate. Source intervals (E174): {intervals_text}.

## Plan route selection

The Plan amount is the selected multiple times the cash paid for the fee period (E166), typed by what the measurement establishes; it is not capacity unless it says so. The multiple values only the measured workload's API-equivalent consumption; other plan features are not valued.

{markdown_table(['Configuration', 'Selected route', 'Plan amount', 'Identification', 'Plan cost (USD per basket run)', 'Flags', 'Selection reason'], plan_rows, numeric={4})}

### Route alternatives

Every admissible route-measurement pair in comparator order (E171) and the comparator's pick with the selected pair removed (E179). A larger displayed multiple is arithmetic on the measured workload, never a claim that the route is cheaper on the scored workload. Workday-feasible multiple (E15), for the {len(routed)} routed rows: {'; '.join(workday) or 'none routed'}.

{markdown_table(['Configuration', 'Admissible pairs', 'Unidentified', 'Pairs (multiple, status)', 'Leave-selected-out choice'], alternative_rows, numeric={1, 2})}

### Measured-only Plan view

Admission: {measured['specification']['admission']}. Selection: {measured['specification']['selection']}. Panel: {measured['specification']['panel']}.

{markdown_table(['Configuration', 'Status', 'Route', 'Plan cost', 'Value', 'Rank'], measured_rows, numeric={3, 4, 5})}

{calibration_markdown(facts)}

## Interval outputs

{interval_tables(facts)}

## Scenario shares

{scenario_tables(facts)}

## Diagnostics

{diagnostics_markdown(facts)}

## Release gates

{markdown_table(['Rule', 'Status', 'Detail'], [[item['rule'], item['status'], item['detail']] for item in v3['manifest']])}
"""


def calibration_markdown(facts):
    """E164: the measured-only rows rescored on anchors built from measured evidence alone."""

    measured = facts.v3["measuredOnlyPlanView"]
    calibration = measured["calibration"]
    lines = [f"#### Measured-evidence calibration (diagnostic)\n\nReferences: {calibration['rule']}. Status: {calibration['status']}.\n"]
    for workload, item in calibration["workloads"].items():
        provenance = item["officialAnchorProvenance"]
        extremes = (
            f" Official Plan anchors are set by {facts.label(provenance['low']['row'])} ({provenance['low']['evidence']}) at the low end "
            f"and {facts.label(provenance['high']['row'])} ({provenance['high']['evidence']}) at the high end."
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
        [facts.label(row_id), fnum(measured["rows"][row_id]["value"], 2), fnum(value, 2), calibration["rankChange"]["changes"].get(row_id, DASH)]
        for row_id, value in sorted(calibration["values"].items(), key=lambda pair: facts.label(pair[0]))
    ]
    if rows:
        lines.append("\n" + markdown_table(["Configuration", "Value on official Plan anchors", "Value on measured anchors", "Rank change"], rows, numeric={1, 2, 3}))
        reversals = "; ".join(f"{facts.label(a)} and {facts.label(b)}" for a, b in calibration["reversals"]) or "none"
        lines.append(f"\nPairwise reversals: {reversals}. Largest value change: {fnum(calibration['maxAbsValueChange'], 2)} points.")
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
            text += f"Cheaper same-family configurations on AA's chart that were not evaluated (not ranked: no exact DeepSWE and Bug Hunt pair; E201, O33): {siblings or 'none'}.\n\n"
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
    parts = [f"Frequencies over {scenarios['scenarios']:,} scenarios per run (seed {scenarios['seed']}); streams are defined in [methodology.md](methodology.md#uncertainty-outputs). The shares exclude benchmark sampling noise beyond S1M and fitted-rating uncertainty (E155)."]
    for basis, label in (("api", "API"), ("plan", "Plan")):
        runs = scenarios["results"][basis]
        row_ids = sorted({row_id for run in runs for row_id in run["panel"]}, key=facts.label)
        excluded = {item["row"] for run in runs for item in run.get("excluded", [])}
        if excluded:
            off = [run_label(run) for run in runs if run.get("excluded")]
            parts.append(
                f"{label} streams {series(off)} run with owner-named transfers off (E167): {facts.labels(sorted(excluded, key=facts.label))} "
                "depend on a transfer and are unevaluable there (—), never reselected or replaced by API cost."
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
    return f"{len(moved)} rows move; largest move {largest} ({names_label([row_id for row_id, change in moved.items() if abs(change) == largest])})"


LEAF_LABELS = {leaf.key: leaf.label for leaf in q.LEAVES}


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
        f"- **Terminal-Bench same-harness ({harness['defaultHarness']}):** {harness['agreement']['status']}; {len(harness['harnessMixed'])} rows ran on mixed harnesses.",
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


def raw_data(facts):
    v3 = facts.v3
    leaf_rows = []
    for entry in facts.ranked:
        row = facts.row(entry)
        audit = {item["leaf"]: item for item in row["quality"]["clipAudit"]}
        for leaf in q.LEAVES:
            if leaf.key not in row["quality"]["leaves"]:
                continue
            detail = row["quality"]["leaves"][leaf.key]
            evidence = detail.get("evidence") or {}
            leaf_rows.append([
                configuration_label(row, facts.names), leaf.label, audit[leaf.key]["raw"], audit[leaf.key]["unit"], fnum(detail["z"], 2),
                " / ".join(str(part) for part in (detail.get("configuration"), detail.get("agent")) if part) or DASH,
                f"`{evidence['artifact']}` `{evidence['locator']}`" if evidence else DASH,
            ])
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
    bundle = v3["evidenceBundle"]
    bundle_rows = [[item["key"], f"`{item['artifact']}`", f"`{item['sha256']}`", item.get("capturedAt") or DASH, item.get("extractor") or DASH] for item in bundle["artifacts"]]
    deepswe = facts.deepswe["configurations"]
    tb4 = facts.tb4
    return f"""# ValueRank {VERSION} Raw Data

**Updated:** {DATE} · methodology {v3['methodologyVersion']}

Every input behind the published scores, with the artifact and locator that holds it. Generated from the committed snapshots in [data/](data/); nothing here is edited by hand.

## Quality leaf inputs

{markdown_table(['Configuration', 'Leaf', 'Raw value', 'Unit', 'Score z', 'Evaluated configuration / agent', 'Evidence'], leaf_rows, numeric={2, 4})}

## Basket cost components

{markdown_table(['Configuration', 'Component', 'Cost (USD)', 'Completeness', 'Tasks', 'USD per task', 'Source'], component_rows, numeric={2, 4, 5})}

### AA Index total reconciliation

The seven Index components plus AA's residual reproduce AA's published Intelligence Index total cost.

{markdown_table(['Configuration', 'Index SDLC components', 'Residual', 'Reconstructed total', 'Published total', 'Reconciled'], reconciliation_rows, numeric={1, 2, 3, 4})}

## DeepSWE v1.1 AA chart configurations

The AA chart publishes {len(deepswe)} DeepSWE v1.1 configurations across {facts.deepswe['benchmarkTasks']} tasks, observed {facts.deepswe.get('observedAt', DASH)}. Each keeps its displayed agent, model and effort; only exact matches enter a score.

| # | Agent | Evaluated model variant | Effort | pass@1 | ValueRank match | Note |
|---:|---|---|---|---:|---|---|
{deepswe_chart_table(deepswe)}

## Terminal-Bench 4.0 official rows

{tb4['rowN']} official rows ({tb4['matchedN']} of {tb4['cohortN']} cohort matches), observed {tb4.get('observedAt', DASH)}. The published ± is the source's 95% confidence interval (used by stream S1M).

| Rank | Base model | Agent | Resolution rate | Tokens | Cost |
|---|---|---|---:|---|---:|
{tb4_table(tb4['rows'])}

## Bug Hunt Bench matched runs

Owner-published runs at commit `{facts.bug_hunt['sourceCommit']}`; the score is the mean bugs fixed of 105 over the runs for the exact model, effort and harness.

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
