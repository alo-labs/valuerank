"""Capture the Artificial Analysis DeepSWE v1.1 coding-agent chart from its page payload."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import urllib.request
from collections import Counter
from pathlib import Path

from valuerank.clock import iso_z
from valuerank.paths import DATA

USER_AGENT = "ValueRank/1.6 official-source-refresh"
URL = "https://artificialanalysis.ai/agents/coding-agents?coding-agents-performance-chart=deep-swe-v1.1"
SCHEMA_VERSION = "valuerank-aa-coding-agent-deepswe/v2"
DEFAULT_INDEX_VERSION = "v1.5"
INDEX_VERSION = re.compile(r"Coding Agent Index (v\d+(?:\.\d+)*)")
FALLBACK_SUFFIX = " with fallback"
METHODOLOGY = "The chart states each benchmark score averages pass@1 across three attempts per task."
CAPTURE_METHOD = (
    "Automatic capture of the coding-agents page payload (every configuration with a DeepSWE v1.1 "
    "evaluation); scores are the owner's mean reward at full precision"
)
SELECTION_POLICY = (
    "Use the benchmark-owner chart for the exact displayed model version and retain its agent and effort "
    "configuration. Do not transfer scores across model versions or composite-agent configurations. A ValueRank "
    "family row is mapped only when its evaluated model variant matches the chart row."
)
BENCHMARK_SLUG = "DeepSWE v1.1"
ROW_ARRAY_KEYS = ("rows", "benchmarkRows")
FLIGHT_REFERENCE = re.compile(r"^\$[0-9a-f]+:props:children:props:rows:(\d+)$")
# The remainder of a JavaScript string literal: anything up to the first unescaped quote.
EFFORTS = frozenset({"minimal", "low", "medium", "high", "xhigh", "max"})
TRAILING_PAREN = re.compile(r"\s*\(([^()]*)\)$")
REASONING_SUFFIX = re.compile(r"\s*\(\{'reasoning_effort': '([^']*)'\}\)$")
STRING_BODY = re.compile(r'(?:[^"\\]|\\.)*', re.DOTALL)


def decode_array(page_text: str, key: str) -> list[list]:
    """Decode every ``"<key>":[ ... ]`` array of the escaped Next.js flight payload."""

    marker = '\\"%s\\":[' % key
    arrays = []
    position = page_text.find(marker)
    while position >= 0:
        start = position + len(marker) - 1
        literal = STRING_BODY.match(page_text, start).group(0)
        decoded = json.loads('"' + literal + '"')
        try:
            array, _ = json.JSONDecoder().raw_decode(decoded)
        except json.JSONDecodeError as exc:
            raise ValueError(f"coding-agent {key} array is truncated or malformed") from exc
        arrays.append(array)
        position = page_text.find(marker, start + len(literal))
    return arrays


def has_deepswe_eval(row: dict) -> bool:
    return any(item.get("evaluationDatasetSlug") == BENCHMARK_SLUG for item in row["evals"])


def extract_deepswe_rows(page_text: str) -> list[dict]:
    """Every distinct configuration (by ``id``) with a DeepSWE v1.1 evaluation, in page order."""

    decoded = {key: decode_array(page_text, key) for key in ROW_ARRAY_KEYS}
    if not any(decoded.values()):
        raise ValueError("no coding-agent row arrays found in the page payload")
    primary = decoded["rows"][0] if decoded["rows"] else []
    distinct: dict[str, dict] = {}
    for key in ROW_ARRAY_KEYS:
        for array in decoded[key]:
            for item in array:
                if isinstance(item, str):
                    reference = FLIGHT_REFERENCE.match(item)
                    if reference is None or int(reference.group(1)) >= len(primary):
                        raise ValueError(f"unresolvable flight reference {item!r}")
                    item = primary[int(reference.group(1))]
                if not isinstance(item, dict):
                    raise ValueError(f"unexpected item in the {key} array: {item!r}")
                distinct.setdefault(item["id"], item)
    rows = [row for row in distinct.values() if has_deepswe_eval(row)]
    if not rows:
        raise ValueError("the page payload has no configuration with a DeepSWE v1.1 evaluation")
    return rows


def peel_suffixes(text: str) -> tuple[str, str | None, bool]:
    """Strip trailing ``(<effort>)`` and ``(with fallback)`` groups; return the rest, effort, fallback."""

    effort = None
    fallback = False
    while match := TRAILING_PAREN.search(text):
        token = match.group(1).strip().lower()
        if token == "with fallback":
            fallback = True
        elif token in EFFORTS and effort is None:
            effort = token
        else:
            break
        text = text[: match.start()]
    return text, effort, fallback


def parse_identity(row: dict) -> dict:
    """Agent, model, effort (lowercase or None) and fallback flag of a configuration.

    AA spells the effort inconsistently: usually ``Sonnet 5.5 (max)`` on the model, but
    sometimes only on the display label, or only as a ``({'reasoning_effort': ...})``
    suffix of the label. The model name is the display model without those suffixes.
    """

    display = row.get("display") or {}
    agent, model_text = display.get("agent"), display.get("model")
    if not agent or not model_text:
        raise ValueError(f"{row['id']} has no display agent/model")
    label = row.get("displayLabel") or ""
    reasoning = REASONING_SUFFIX.search(label)
    if reasoning:
        label = label[: reasoning.start()]
    if label.startswith(agent + " - "):
        label = label[len(agent) + 3 :]
    model, model_effort, model_fallback = peel_suffixes(model_text)
    _, label_effort, label_fallback = peel_suffixes(label)
    reasoning_effort = reasoning.group(1).lower() if reasoning else None
    return {
        "agent": agent,
        "model": model,
        "effort": model_effort or label_effort or reasoning_effort,
        "fallback": model_fallback or label_fallback,
    }


def agent_version(row: dict, eval_index_name: str) -> str | None:
    """The agent release behind a DeepSWE run: an explicit key, else the owner's version range."""

    if row.get("agentVersion"):
        return row["agentVersion"]
    span = (row.get("versions") or {}).get(eval_index_name)
    if not span:
        return None
    low = (span.get("min") or {}).get("version")
    high = (span.get("max") or {}).get("version")
    if not low or not high:
        return low or high
    return low if low == high else f"{low} to {high}"


def normalise_name(name: str) -> str:
    """Comparable model name: lowercase, single spaces, hyphens as spaces, no leading "claude "."""

    collapsed = " ".join(name.lower().replace("-", " ").split())
    return collapsed.removeprefix("claude ")


def effort_text(effort: str | None) -> str:
    return effort or "no effort"


def map_to_roster(configs: list[dict], roster: dict) -> list[dict]:
    """Attach ``valueRankModelId``/``matchStatus``/``matchNote`` to each configuration.

    A configuration maps to a roster model only when the normalised model name equals the
    roster display name and the effort equals the roster ``aaVariant`` (None equals None).
    The fallback marker is recorded but never used for matching. When several rows map
    to one roster model only the highest scoring row keeps the id.
    """

    families: dict[str, list[tuple[str, dict, str]]] = {}
    for model_id, entry in roster.items():
        names = {normalise_name(entry["displayName"]): f"display name {entry['displayName']!r}"}
        family = TRAILING_PAREN.sub("", entry.get("aaShortName") or "")
        if family:
            names.setdefault(normalise_name(family), f"AA short name {family!r}")
        for key, matched in names.items():
            families.setdefault(key, []).append((model_id, entry, matched))
    kept: dict[str, dict] = {}
    for item in configs:
        candidates = families.get(normalise_name(item["model"]), [])
        exact = [match for match in candidates if match[1].get("aaVariant") == item["effort"]]
        item["valueRankModelId"] = None
        if exact:
            model_id, entry, matched = exact[0]
            item["matchStatus"] = "exact_variant"
            item["matchNote"] = (
                f"Exact variant: chart model {item['model']} ({effort_text(item['effort'])}) matches the roster "
                f"{matched} at effort {effort_text(entry.get('aaVariant'))}."
            )
            held = kept.get(model_id)
            if held is None or item["scorePct"] > held["scorePct"]:
                kept[model_id] = item
            item["valueRankModelId"] = model_id
        elif candidates:
            variants = ", ".join(effort_text(e.get("aaVariant")) for _, e, _ in candidates)
            if item["effort"] is None:
                item["matchStatus"] = "effort_unconfirmed"
                item["matchNote"] = (
                    f"The chart row shows no effort; the roster's selected configuration is {variants}, "
                    "so the variant cannot be confirmed and no result is transferred."
                )
            else:
                item["matchStatus"] = "effort_mismatch"
                item["matchNote"] = (
                    f"Model family matches the roster {candidates[0][2]}, but the chart row's effort "
                    f"({item['effort']}) differs from the roster variant ({variants}); "
                    "ValueRank never substitutes a different reasoning effort."
                )
        else:
            item["matchStatus"] = "not_in_roster"
            item["matchNote"] = "No ValueRank roster model has this chart model name."
            if " + " in item["model"]:
                item["matchNote"] += " It is a composite agent configuration."
        if item["fallback"]:
            item["matchNote"] += (
                " AA labels this configuration 'with fallback'; the marker is recorded "
                "but does not affect matching."
            )
    for item in configs:
        winner = kept.get(item["valueRankModelId"])
        if winner is not None and winner is not item:
            item["valueRankModelId"] = None
            item["matchStatus"] = "duplicate_configuration"
            item["matchNote"] = (
                f"Another configuration of the same roster model and effort scored higher or earlier and "
                f"was kept: {winner['displayLabel']} (source id {winner['sourceId']}); "
                "a roster model maps to only one chart row."
            )
    return configs


def configuration_key(agent: str, model: str, effort: str | None, fallback: bool) -> tuple:
    return (agent.lower(), model.lower(), effort, bool(fallback))


def previous_key(item: dict) -> tuple:
    """Key of a row from a previous capture, tolerating the v1 spellings ("max with fallback", "composite")."""

    effort = item.get("effort")
    fallback = item.get("fallback", False)
    if effort and effort.endswith(FALLBACK_SUFFIX):
        effort, fallback = effort[: -len(FALLBACK_SUFFIX)], True
    if effort == "composite":
        effort = None
    return configuration_key(item["agent"], item["model"], effort, fallback)


def build_configuration(row: dict, observed_at: str) -> dict:
    item = next(e for e in row["evals"] if e.get("evaluationDatasetSlug") == BENCHMARK_SLUG)
    mean = item.get("mean") or {}
    reward = mean.get("reward")
    if isinstance(reward, bool) or not isinstance(reward, (int, float)) or not 0 <= reward <= 1:
        raise ValueError(f"{row['id']} has an invalid DeepSWE v1.1 reward: {reward!r}")
    identity = parse_identity(row)
    return {
        "sourceOrder": 0,
        "sourceId": row["id"],
        **identity,
        "displayLabel": row["displayLabel"],
        "scorePct": round(reward * 100, 1),
        "rewardMean": reward,
        "attemptCount": (item.get("safety") or {}).get("attemptCount"),
        "meanInputTokens": mean.get("inputTokens"),
        "meanOutputTokens": mean.get("outputTokens"),
        "scorePrecision": "payload_full_precision",
        "agentVersion": agent_version(row, item.get("datasetIndexName")),
        "valueRankModelId": None,
        "matchStatus": None,
        "matchNote": None,
        "observedAt": observed_at,
        "previouslyObservedAt": None,
        "previousScorePct": None,
    }


def build_document(page_bytes: bytes, roster: dict, previous: dict | None, observed_at: str) -> dict:
    """The ``valuerank-aa-coding-agent-deepswe/v2`` document for a captured coding-agents page."""

    text = page_bytes.decode("utf-8", errors="replace")
    rows = extract_deepswe_rows(text)
    configurations = [build_configuration(row, observed_at) for row in rows]
    unavailable = {row["id"] for row in rows if row.get("isUnavailable")}
    configurations.sort(key=lambda c: (-c["scorePct"], c["displayLabel"]))
    map_to_roster(configurations, roster)
    earlier: dict[tuple, dict] = {}
    for item in (previous or {}).get("configurations", []):
        earlier.setdefault(previous_key(item), item)
    retained = 0
    for order, item in enumerate(configurations, start=1):
        item["sourceOrder"] = order
        if item["sourceId"] in unavailable:
            item["matchNote"] += " AA marks this configuration as unavailable."
        before = earlier.get(configuration_key(item["agent"], item["model"], item["effort"], item["fallback"]))
        if before is not None:
            retained += 1
            item["previouslyObservedAt"] = before.get("observedAt")
            item["previousScorePct"] = before.get("scorePct")
    current = {configuration_key(c["agent"], c["model"], c["effort"], c["fallback"]) for c in configurations}
    removed = len(set(earlier) - current)
    mapped = sum(1 for c in configurations if c["valueRankModelId"])
    previous_at = previous.get("observedAt") if previous else None
    found = INDEX_VERSION.search(text)
    version = found.group(1) if found else DEFAULT_INDEX_VERSION
    comparison = (
        f"Against the previous capture of {previous_at}: {retained} retained, "
        f"{len(configurations) - retained} new and {removed} removed (by agent, model, effort and fallback)."
        if previous
        else "No previous capture was available for comparison."
    )
    return {
        "schemaVersion": SCHEMA_VERSION,
        "benchmark": BENCHMARK_SLUG,
        "benchmarkTasks": 113,
        "observedConfigurationN": len(configurations),
        "observedAt": observed_at,
        "previousObservedAt": previous_at,
        "source": {
            "publisher": "Artificial Analysis",
            "sourceType": "benchmark_owner",
            "title": f"Artificial Analysis Coding Agent Index {version} \u2014 {BENCHMARK_SLUG}",
            "url": URL,
            "indexVersion": version,
            "metric": "Pass@1 (%)",
            "methodology": METHODOLOGY,
            "captureMethod": CAPTURE_METHOD,
            "captureSha256": hashlib.sha256(page_bytes).hexdigest(),
            "responseBytes": len(page_bytes),
        },
        "selectionPolicy": SELECTION_POLICY,
        "freshnessNote": (
            f"All {len(configurations)} configurations with a {BENCHMARK_SLUG} evaluation were captured "
            f"automatically on {observed_at[:10]}; {mapped} map to an exact ValueRank roster variant. {comparison} "
            "Scores are the owner's mean reward at full precision, rounded to one decimal place."
        ),
        "configurations": configurations,
    }


def fetch_page(url: str = URL) -> bytes:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=45) as response:
        return response.read()


def main(argv: list[str] | None = None, *, data: Path = DATA) -> int:
    parser = argparse.ArgumentParser(description="Capture the AA DeepSWE v1.1 coding-agent chart.")
    parser.add_argument("--out", type=Path, default=data / "aa_deepswe.json", help="output document path")
    parser.add_argument("--html", type=Path, help="read a saved coding-agents page instead of fetching it")
    args = parser.parse_args(argv)

    roster = json.loads((data / "aa_metrics.json").read_text())["models"]
    if not roster:
        raise ValueError("AA metrics snapshot must contain a non-empty comparison roster")
    previous = json.loads(args.out.read_text()) if args.out.exists() else None
    page_bytes = args.html.read_bytes() if args.html else fetch_page()
    document = build_document(page_bytes, roster, previous, iso_z())
    args.out.write_text(json.dumps(document, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    configurations = document["configurations"]
    print(json.dumps({
        "observedAt": document["observedAt"],
        "previousObservedAt": document["previousObservedAt"],
        "observedConfigurationN": document["observedConfigurationN"],
        "matchStatusCounts": dict(sorted(Counter(c["matchStatus"] for c in configurations).items())),
        "mappedModelIds": sorted(c["valueRankModelId"] for c in configurations if c["valueRankModelId"]),
        "output": str(args.out),
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
