#!/usr/bin/env python3
"""Draft figures (editor decision E265): the methodology draft never copies a "today" figure by hand.

The draft is written as a source file, ``draft-rNNN.src.md``, whose current-release figures are placeholders resolved
from the build: ``{{max:PATH|FORMAT}}`` and ``{{aicd:PATH|FORMAT}}`` read a ranking's v3 section of
``data/scores.json``, ``{{top:PATH|FORMAT}}`` reads the file's root, and ``{{fig:NAME}}`` reads a named figure of the
figures manifest (``data/figures.json``, both rankings, rebuilt with the docs). ``render`` writes the published
``draft-rNNN.md`` from its source; ``check`` fails when the newest draft differs from its rendering, when a
placeholder does not resolve, or when a sentence that speaks of today still carries an unmarked number. A stale figure
that a reviewer finds after this is a bug in the check, not in the draft.

    python3 -m valuerank.draft_figures manifest  # write data/figures.json (run by `npm run build:docs`)
    python3 -m valuerank.draft_figures render    # (re)write the newest draft from its source
    python3 -m valuerank.draft_figures check     # verify it (run by the tests and by `npm run verify:docs`)
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

from valuerank import quality as q
from valuerank.paths import DATA, ROOT

SPEC_DIR = ROOT / "research" / "2026-10-19-methodology-codesign"
MANIFEST = "figures.json"
PLACEHOLDER = re.compile(r"\{\{(?P<scope>max|aicd|top|fig):(?P<path>[^|}]+)(?:\|(?P<fmt>[^}]+))?\}\}")
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
    ``range`` (a two-item rank band) and ``str``; without a spec, a string or integer is printed as it is."""

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
        figures[f"{track}.listed"] = len(section["listedIndicative"])
        figures[f"{track}.planRows"] = len(section["planRows"])
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
        cross = section["diagnostics"]["frontierCodeCrossSource"]
        figures[f"{track}.fillEffect.mean"] = f"{weights['frontierCode'] / 100 * cross['meanOffset']:.2f}"
        figures[f"{track}.fillEffect.max"] = f"{weights['frontierCode'] / 100 * cross['maxAbsOffset']:.2f}"
    both = set(ranked["max"]) & set(ranked["aicd"])
    figures["both.names"], figures["both.count"] = order(both), len(both)
    figures["rankedAny"] = len(set(ranked["max"]) | set(ranked["aicd"]))
    excluded = {item["id"] for item in sections["max"]["incompleteEvidence"]} & {item["id"] for item in sections["aicd"]["incompleteEvidence"]}
    figures["excluded"], figures["excluded.names"] = len(excluded), order(excluded)
    figures.update(family_figures(scores, excluded, order))
    return {key: str(value) for key, value in sorted(figures.items())}


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
    return {
        "near.primaries": by_gap([model for model in near_families if model.get("familyPrimary")]),
        "near.others": by_gap([model for model in near_families if not model.get("familyPrimary")]),
        "frontierFamilies.nearPoints": order(model["id"] for model in frontier_near),
        "frontierFamilies.dearerNearPoints": order(model["id"] for model in frontier_near
                                                   if model["aaEvalCost"] > primary[family(model)]["aaEvalCost"]),
        "excluded.frontierPrimaries": order(model["id"] for model in cohort if model["id"] in excluded and model.get("familyPrimary") and family(model) in frontier_families),
        "excluded.nearPrimaries": order(model["id"] for model in cohort if model["id"] in excluded and model.get("familyPrimary") and family(model) not in frontier_families),
        "excluded.nearPoints": order(model["id"] for model in frontier_near if model["id"] in excluded),
        "excluded.frontierPoints": order(model["id"] for model in cohort if model["id"] in excluded and not model.get("familyPrimary")
                                         and model["aaFrontierTier"] == "frontier"),
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
    scopes = {"max": scores["v3"], "aicd": scores["v3Tracks"]["aicd"], "top": scores}

    def replace(match: re.Match) -> str:
        scope, path, spec = match.group("scope"), match.group("path").strip(), match.group("fmt")
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
RULE_CONSTANTS = ("more than 5 points", "within 3 points", "n = 8 rows", "Pro $100", "Pro $200", "Pro $500", "of 60 points", "> 5 points", "40 of the 100", "n = 60", "n = 6", "÷ 60", "÷ √6", "±26 Elo", "1/0.75", "carries 75%", "below 3 points", "> 0", "under 40%", "290 ×", "290 required", "the 290", "⌈2N/3⌉", "10⁻⁶", "0–100", "0 or 100", "correlations 0, 0.3 and 0.6", "correlation 0", "sum to 1", "25% cost", "the 25% weight", "1.96", "√2", "0.75", "0.25",
                  "factor-2", "factor of 2", "two-thirds", "30 days", "7 days", "45 days", "0.5 W_g", "1.5 W_g")
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


def lint(source: str, names: list[str], configurations: list[str] = (), release_day: str | None = None) -> list[str]:
    """Numbers and configuration names left unmarked in a sentence that speaks of today."""

    problems = []
    for line_number, line in enumerate(source.splitlines(), 1):
        if line.startswith(HISTORY_HEADING):
            break  # the revision history records past drafts' figures as they were
        for sentence in _SENTENCE.split(line):
            # A count "N of M" states the current release unless the sentence dates it, whether or not it says today.
            if not dated(sentence, release_day):
                undated = PLACEHOLDER.sub("", sentence)
                for constant in RULE_CONSTANTS:
                    undated = undated.replace(constant, "")
                counts = [match.group(0) for match in _COUNT.finditer(undated)]
                if not _FIXTURE.search(sentence):
                    counts += [match.group(0) for match in _COUNTED.finditer(_NOT_A_FIGURE.sub("", undated))]
                if counts:
                    problems.append(f"line {line_number}: unmarked count(s) {', '.join(counts)} in an undated sentence: {sentence[:160]}")
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


def latest_source(spec_dir: Path = SPEC_DIR) -> Path:
    sources = [(int(match.group("number")), path) for path in spec_dir.glob("draft-r*.src.md") if (match := DRAFT.search(path.name))]
    if not sources:
        raise FigureError(f"no draft source in {spec_dir}")
    return max(sources)[1]


def published(source: Path) -> Path:
    return source.with_name(source.name.replace(".src.md", ".md"))


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
