"""Third-party board coverage for the 45-configuration cohort of the 2026-11-26 re-capture.

Adapted from research/2026-11-01-recapture/third-party/build_coverage.py (the 37-configuration read of 2026-11-01), which
followed research/2026-10-25-board-reread/ and research/2026-10-30-v5-recapture/third-party/. It re-reads every board a
ranking uses: Bug Hunt Bench, Vals Vibe Code Bench v1.1 and Code Migration v1.1 (the pinned versions), LiveBench 2.0
(release 20261106, owner decision O211), AI Coding Daily (every row, hidden older rows included), the tbench.ai
Terminal-Bench leaderboard (4.1 since AA's Coding Agent Index v2.1) and, as a cross-check source (E234), Cognition's
FrontierCode 2.0 leaderboard. The cohort is ../cohort.json (45 configurations: 20 frontier, 11 near, 14 retained).

Matching is exact configuration only (O36): the source row must name the same model version and the same reasoning effort
as the AA configuration; no value moves across efforts or versions. Where AA plots no effort, the configuration is the
provider's documented default or the owner's stated mapping (O135/O140/O149 MiMo-V2.6-Flash: thinking enabled).

    python3 -I research/2026-11-26-recapture/third-party/build_coverage.py

Writes next to this file: coverage-2026-11-26.json (Bug Hunt, LiveBench 2.0 Overall, AI Coding Daily, tbench.ai),
vals-catalogue-2026-11-26.json (Vals) and cognition/frontiercode-2.0-2026-11-26.json (Cognition cross-check board).
Prints exact / plausible / absent counts per board ("absent" is the schema's word for "no exact match, reason recorded").
"""

from __future__ import annotations

import csv
import hashlib
import html
import json
import re
from decimal import ROUND_HALF_UP, Decimal
from pathlib import Path

HERE =Path(__file__).resolve().parent
PREVIOUS = HERE.parents[1] / "2026-11-01-recapture" / "third-party"
CUTOFF = "2026-11-26T02:18:20Z"  # the new chart capture instant (../chart-capture.json capturedAt)
PREVIOUS_CUTOFF = "2026-11-01T05:53:05Z"  # the 2026-11-01 chart capture
PREVIOUS_TAG, TAG = "20261101", "20261126"
LIVEBENCH_RELEASE = "20261106"  # owner decision O211 (previous pin 20261025, O139)
PREVIOUS_LIVEBENCH_RELEASE = "20261025"

O135 = ("Owner decision O135 (2026-10-30): AA plots MiMo-V2.6-Flash without an effort; Xiaomi's API documents a single "
        "thinking mode (thinking.type enabled/disabled, default enabled; on the Responses API every reasoning.effort other "
        "than none enables the same, undifferentiated reasoning), so the configuration is thinking enabled, the default "
        "(../../2026-10-30-v5-recapture/third-party/mimo-flash-effort.md; Xiaomi docs last read 2026-11-01, "
        "../../2026-11-01-recapture/third-party/mimo/; not re-read on 2026-11-26).")

FALLBACK_NOTE = ("AA's pages name this configuration '(<Effort>, Default Fallback)' (its chart label shows only the effort since "
                 "2026-11-26, and said 'with fallback' before); the source has no fallback qualifier (as on 2026-10-25 and 2026-11-01).")

# id: (family, effort). Effort None = AA plots no effort and a documented single-mode equivalent applies (MiMo-V2.6-Flash).
COHORT = {
    "gpt-6-luna-low": ("luna", "low"), "gpt-6-luna-medium": ("luna", "medium"), "gpt-6-luna-high": ("luna", "high"),
    "gpt-6-luna-xhigh": ("luna", "xhigh"), "gpt-6-luna": ("luna", "max"),
    "claude-haiku-5-5-low": ("haiku", "low"), "claude-haiku-5-5-medium": ("haiku", "medium"),
    "claude-haiku-5-5-high": ("haiku", "high"), "claude-haiku-5-5-xhigh": ("haiku", "xhigh"),
    "muse-ember-xhigh": ("ember", "xhigh"), "muse-ember": ("ember", "max"),
    "gpt-6-1-terra-low": ("terra", "low"), "gpt-6-1-terra-medium": ("terra", "medium"), "gpt-6-1-terra-high": ("terra", "high"),
    "gpt-6-1-terra-xhigh": ("terra", "xhigh"), "gpt-6-1-terra": ("terra", "max"),
    "gpt-6-1-sol-low": ("sol61", "low"), "gpt-6-1-sol-medium": ("sol61", "medium"), "gpt-6-1-sol-high": ("sol61", "high"),
    "gpt-6-1-sol-xhigh": ("sol61", "xhigh"), "gpt-6-1-sol": ("sol61", "max"),
    "gpt-6-2-sol-low": ("sol62", "low"), "gpt-6-2-sol-medium": ("sol62", "medium"), "gpt-6-2-sol-high": ("sol62", "high"),
    "gpt-6-2-sol-xhigh": ("sol62", "xhigh"), "gpt-6-2-sol": ("sol62", "max"),
    "gpt-6-2-astra-medium": ("astra62", "medium"), "gpt-6-2-astra-high": ("astra62", "high"),
    "gpt-6-2-astra-xhigh": ("astra62", "xhigh"), "gpt-6-2-astra": ("astra62", "max"),
    "gpt-6-astra-high": ("astra6", "high"), "gpt-6-astra-xhigh": ("astra6", "xhigh"), "gpt-6-astra": ("astra6", "max"),
    "claude-fable-5-2-high": ("fable", "high"), "claude-fable-5-2-xhigh": ("fable", "xhigh"), "claude-fable-5-2": ("fable", "max"),
    "gemini-4-neon-medium": ("neon", "medium"), "gemini-4-neon-high": ("neon", "high"), "gemini-4-neon": ("neon", "xhigh"),
    "gemini-4-carbon": ("carbon", "high"),
    "claude-opus-5-5-high": ("opus", "high"), "claude-opus-5-5-xhigh": ("opus", "xhigh"), "claude-opus-5-5": ("opus", "max"),
    "claude-sonnet-5-5": ("sonnet", "max"),
    "mimo-v2-6-flash": ("mimo-flash", None),
}
FALLBACK = {"claude-opus-5-5-high", "claude-opus-5-5-xhigh", "claude-opus-5-5", "claude-sonnet-5-5",
            "claude-fable-5-2-high", "claude-fable-5-2-xhigh", "claude-fable-5-2"}
NEW_FAMILIES = {"sol62": "GPT-6.2 Sol", "astra62": "GPT-6.2 Astra", "fable": "Claude Fable 5.2", "neon": "Gemini 4 Neon", "ember": "Muse Ember"}


def load_cohort() -> list[dict]:
    """../cohort.json when the release folder has it, else the snapshot read on 2026-11-26 (cohort-snapshot.json)."""
    for path in (HERE.parent / "cohort.json", HERE / "cohort-snapshot.json"):
        if path.exists():
            configurations = json.loads(path.read_text())["configurations"]
            if {c["id"] for c in configurations} != set(COHORT) or len(configurations) != len(COHORT):
                raise ValueError(f"{path} does not match this script's COHORT: "
                                 f"{sorted(set(c['id'] for c in configurations) ^ set(COHORT))}")
            ordered = {c["id"]: COHORT[c["id"]] for c in configurations}  # coverage follows the cohort file's order
            COHORT.clear()
            COHORT.update(ordered)
            for c in configurations:
                match = re.search(r"\((\w+)\)$", c["displayName"])
                effort = COHORT[c["id"]][1]
                if (match.group(1) if match else None) != effort:
                    raise ValueError(f"{c['id']}: display name '{c['displayName']}' disagrees with effort {effort}")
            return configurations
    raise FileNotFoundError("no cohort.json or cohort-snapshot.json")


CONFIGURATIONS = load_cohort()
RETAINED = {c["id"] for c in CONFIGURATIONS if c["chartTier"] == "retained"}


def old_id(model_id: str) -> str:
    """The id this configuration had in the 2026-11-01 coverage (ids then wrote versions with a dot: gpt-6.1-sol)."""
    if model_id == "claude-haiku-5-5-xhigh":
        return "claude-haiku-5-5"
    return "gpt-6.1-" + model_id[len("gpt-6-1-"):] if model_id.startswith("gpt-6-1-") else model_id


BUGHUNT = {"luna": "GPT-6 Luna", "haiku": "Haiku 5.5", "ember": "Muse Ember", "terra": "GPT-6.1 Terra", "sol61": "GPT-6.1 Sol",
           "sol62": "GPT-6.2 Sol", "astra62": "GPT-6.2 Astra", "astra6": "GPT-6 Astra", "fable": "Fable 5.2",
           "neon": "Gemini 4 Neon", "carbon": "Gemini 4 Carbon", "opus": "Opus 5.5", "sonnet": "Sonnet 5.5",
           "mimo-flash": "MiMo-V2.6-Flash"}
# E206: the owner's largest-sample current mean at the exact effort over every harness; a tie at the largest sample is
# broken only by a recorded selection reason (else the build stops). No cohort configuration ties on 2026-11-26.
BUGHUNT_SELECTION: dict[str, tuple[str, str]] = {}
VALS_NEON_KEY = "google/cobalt-c-high-1p00"  # Vals' JSON key for the row its pages label "Gemini 4 Neon" (checked in vals())
VALS = {"luna": "openai/gpt-6-luna", "haiku": "anthropic/claude-haiku-5-5", "ember": "meta/muse-ember",
        "terra": "openai/gpt-6.1-terra", "sol61": "openai/gpt-6.1-sol", "sol62": "openai/gpt-6.2-sol",
        "astra62": "openai/gpt-6.2-astra", "astra6": "openai/gpt-6-astra", "fable": "anthropic/claude-fable-5-2",
        "neon": VALS_NEON_KEY, "carbon": "google/gemini-4-carbon", "opus": "anthropic/claude-opus-5-5",
        "sonnet": "anthropic/claude-sonnet-5-5", "mimo-flash": "xiaomi/mimo-v2.6-flash"}
LIVEBENCH = {"luna": "gpt-6-luna", "haiku": "claude-haiku-5.5", "ember": "muse-ember", "terra": "gpt-6.1-terra", "sol61": "gpt-6.1-sol",
             "sol62": "gpt-6.2-sol", "astra62": "gpt-6.2-astra", "astra6": "gpt-6-astra", "fable": "claude-fable-5.2",
             "neon": "gemini-4-neon", "carbon": "gemini-4-carbon", "opus": "claude-opus-5.5", "sonnet": "claude-sonnet-5.5",
             "mimo-flash": "mimo-v2.6-flash"}
AICD = {"luna": "GPT-6-Luna", "haiku": "Haiku 5.5", "ember": "Muse Ember 1.0", "terra": "GPT-6.1-Terra", "sol61": "GPT-6.1-Sol",
        "sol62": "GPT-6.2-Sol", "astra62": "GPT-6.2-Astra", "astra6": "GPT-6-Astra", "fable": "Fable 5.2",
        "neon": "Gemini 4 Neon", "carbon": "Gemini 4 Carbon", "opus": "Opus 5.5", "sonnet": "Sonnet 5.5",
        "mimo-flash": "MiMo-V2.6 Flash"}
TBENCH = {"luna": "GPT-6 Luna", "haiku": "Haiku 5.5", "ember": "Muse Ember", "terra": "GPT-6.1 Terra", "sol61": "GPT-6.1 Sol",
          "sol62": "GPT-6.2 Sol", "astra62": "GPT-6.2 Astra", "astra6": "GPT-6 Astra", "fable": "Fable 5.2",
          "neon": "Gemini 4 Neon", "carbon": "Gemini 4 Carbon", "opus": "Opus 5.5", "sonnet": "Sonnet 5.5",
          "mimo-flash": "MiMo V2.6 Flash"}
COGNITION = {"luna": "GPT-6 Luna", "haiku": "Claude Haiku 5.5", "ember": None, "terra": None, "sol61": "GPT-6.1 Sol",
             "sol62": "GPT-6.2 Sol", "astra62": "GPT-6.2 Astra", "astra6": "GPT-6 Astra", "fable": "Claude Fable 5.2",
             "neon": "Gemini 4 Neon", "carbon": "Gemini 4 Carbon", "opus": "Claude Opus 5.5", "sonnet": "Claude Sonnet 5.5",
             "mimo-flash": None}
AICD_EFFORT = {"Low": "low", "Medium": "medium", "High": "high", "Xhigh": "xhigh", "Max": "max"}

READ = {name: (HERE / path).read_text().strip() for name, path in {
    "bughunt": "bughunt/readAt.txt", "vibe-code": "vals/vibe-code.readAt.txt", "code-migration-v1-1": "vals/code-migration-v1-1.readAt.txt",
    "vibe-code-v1-1-1": "vals/vibe-code-v1-1-1.readAt.txt", "livebench": "livebench/readAt.txt", "aicd": "aicd/livewire.readAt.txt",
    "aicdPage": "aicd/leaderboard.readAt.txt", "cognition": "cognition/data.readAt.txt", "cognitionPage": "cognition/readAt.txt"}.items()}
TBENCH_SCRAPE = json.loads((HERE / "tbench" / "tbench-scrape-2026-11-26.json").read_text())
READ["tbench"] = TBENCH_SCRAPE["scrapedAt"]
BUGHUNT_COMMIT = next((HERE / "bughunt").glob("combined-*.csv")).stem.split("-", 1)[1]


def fixed1(x: float) -> float:
    """The page's JS (100*x).toFixed(1): the double's exact value rounded half up (ties go to the larger n)."""
    return float(Decimal(100 * x).quantize(Decimal("0.1"), rounding=ROUND_HALF_UP))


def cell(status, value=None, label=None, effort=None, note=None, **extra):
    return {"status": status, "value": value, "sourceLabel": label, "effort": effort, "note": note, **extra}


def join_notes(*notes) -> str | None:
    text = " ".join(note for note in notes if note)
    return text or None


def base_note(model_id: str) -> str | None:
    return FALLBACK_NOTE if model_id in FALLBACK else None


def near_note(rows: list[tuple[str, object]], what: str) -> str:
    return (f"Non-matching rows at other efforts: " + "; ".join(f"{label} = {value}" for label, value in rows) + "." if rows
            else f"No {what} row for this model at any effort.")


def previous_values(path: Path, key_field: str) -> dict:
    document = json.loads(path.read_text())
    return {board[key_field]: {model_id: (c.get("status"), c.get("value")) for model_id, c in board["coverage"].items()}
            for board in document["benchmarks"]}


PREVIOUS_OTHER = previous_values(PREVIOUS / "coverage-2026-11-01.json", "key")
PREVIOUS_VALS = previous_values(PREVIOUS / "vals-catalogue-2026-11-01.json", "slug")


def annotate(board: dict, key: str, previous: dict) -> dict:
    """Per-board change record against the 2026-11-01 read (the cohort ids of that read, matched through old_id)."""
    old = previous.get(key, {})
    changed, new_configurations = {}, []
    for model_id, c in board["coverage"].items():
        before = old.get(old_id(model_id))
        if before is None:
            new_configurations.append(model_id)
        elif before != (c["status"], c["value"]):
            changed[model_id] = {PREVIOUS_TAG: {"status": before[0], "value": before[1]}, TAG: {"status": c["status"], "value": c["value"]}}
    board[f"valueChangesSince{PREVIOUS_TAG}"] = changed
    board["configurationsNotInThe20261101Cohort"] = new_configurations
    return board


def counts(board: dict) -> dict:
    return {status: sum(1 for c in board["coverage"].values() if c["status"] == status) for status in ("exact", "plausible", "absent")}


def check_no_text(pattern: str, paths: list[Path]) -> None:
    """Stops if a model name that this build records as having no row actually appears in the saved board files."""
    for path in paths:
        if re.search(pattern, path.read_text(errors="replace"), re.I):
            raise ValueError(f"'{pattern}' appears in {path.name}: recorded as no row, review")


def bughunt() -> dict:
    meta = json.loads((HERE / "bughunt" / "benchmark.json").read_text())
    all_runs = meta["runs"]
    runs = [run for run in all_runs if not run.get("superseded")]
    scoreboard = {row["model"]: float(row["fixed_of_105"]) for row in
                  csv.DictReader((HERE / "bughunt" / f"combined-{BUGHUNT_COMMIT}.csv").read_text().splitlines())}
    board = {"key": "bug-hunt", "name": "Bug Hunt Bench", "updated": meta["meta"]["updated"], "readAt": READ["bughunt"],
             "sourceUrl": "https://bughunt.productcompass.pm/data/benchmark.json; https://github.com/phuryn/bug-hunt-bench/tree/"
                          f"{BUGHUNT_COMMIT}/results (combined-scoreboard.csv, run-notes.md)",
             "sourceCommit": BUGHUNT_COMMIT, "metric": "planted bugs fixed of 105 (owner-published mean where repeated runs exist)",
             "matching": "the board's current row (not superseded) for the same model and effort; the owner's largest-sample mean when "
                         "repeated runs exist (E206), a tie broken only by a recorded selection reason",
             "harness": "each model's native agentic CLI (named per row)",
             "boardSchemaNote": "benchmark.json gained a top-level 'harness_comparison_runs' list (14 DeepSeek V4.1 Flash 1017 rows, "
                                "none in this cohort) with the 2026-11-23 Harness Comparisons reports; run rows are unchanged in shape.",
             "coverage": {}}
    board["crossCheck"] = {"cellsMatchedToCombinedScoreboardCsv": 0}
    for model_id, (family, effort) in COHORT.items():
        rows = [run for run in runs if run["model"] == BUGHUNT[family]]
        if family == "mimo-flash":
            hit = [run for run in rows if run["effort"] == "default"]
            if len(hit) == 1:
                run = hit[0]
                board["coverage"][model_id] = cell(
                    "plausible", run["fixed"], run["id"], "default", O135 + " Bug Hunt ran the provider default through "
                    "OpenRouter without asserting a reasoning state ('effort is `default` ... for this model the dial is untested "
                    "rather than known-inert', run notes). The board does not show that this route's default is Xiaomi's documented "
                    "default (thinking enabled), so the run stays unmatched (owner decision O140, 2026-10-30).",
                    harness=run["harness"], harnessVersion=run.get("harness_version"), date=run["date"], nRuns=run["n_runs"],
                    routeModelId=run.get("model_id"))
            else:
                board["coverage"][model_id] = cell("absent", note="No MiMo-V2.6-Flash row.")
            continue
        hit = [run for run in rows if run["effort"] == effort]
        if not hit:
            note = near_note([(run["id"], run["fixed"]) for run in rows], "Bug Hunt")
            if family == "ember":
                check_no_text(r"\bmuse ember\b", [HERE / "bughunt" / "benchmark.json", *sorted((HERE / "bughunt").glob("*.csv")),
                                                    *sorted((HERE / "bughunt").glob("run-notes-*.md"))])
                note = ("No Muse Ember row, and no mention of the name, in benchmark.json, the combined scoreboard, runs, coverage or "
                        f"run notes at {BUGHUNT_COMMIT[:7]}. The board's Meta rows are Muse Spark 1.2/1.3 and Muse Wonder (Full) 1.0, other "
                        "models; none is transferred (O36).")
            board["coverage"][model_id] = cell("absent", note=note)
            continue
        largest = max(run["n_runs"] for run in hit)
        top = [run for run in hit if run["n_runs"] == largest]
        selection_reason = None
        if len(top) > 1:
            if model_id not in BUGHUNT_SELECTION:
                raise ValueError(f"{model_id}: {len(top)} current Bug Hunt rows tie at n={largest}; no recorded selection")
            chosen_id, selection_reason = BUGHUNT_SELECTION[model_id]
            run = next(run for run in top if run["id"] == chosen_id)
        else:
            run = top[0]
        if run["date"] > CUTOFF[:10]:
            raise ValueError(f"{model_id}: Bug Hunt row dated after the capture day")
        if scoreboard.get(run["id"]) != float(run["fixed"]):
            raise ValueError(f"{model_id}: benchmark.json row '{run['id']}' ({run['fixed']}) is not in combined-scoreboard.csv "
                             f"({scoreboard.get(run['id'])})")
        board["crossCheck"]["cellsMatchedToCombinedScoreboardCsv"] += 1
        note = base_note(model_id)
        if family == "neon":
            old_rows = [r for r in all_runs if r["model"] == "Gemini 4 Neon" and r["effort"] == effort and r.get("superseded")]
            if old_rows:
                note = join_notes(note, "The 2026-11-19 row on Antigravity CLI 1.5.11 (" + "; ".join(
                    f"{r['fixed']} of 105, mean of {r['n_runs']}" for r in old_rows) + ") is superseded on the board by this "
                    "2026-11-25 rerun on Antigravity CLI 1.5.16; the current row is the leaf. No score is retracted, per the board.")
        alternates = [{"id": other["id"], "fixed": other["fixed"], "nRuns": other["n_runs"], "harness": other["harness"],
                       "featured": other.get("featured")} for other in hit if other is not run]
        extra = {"harness": run["harness"], "harnessVersion": run.get("harness_version"), "date": run["date"], "nRuns": run["n_runs"],
                 "featured": run.get("featured")}
        if alternates:
            extra["alternates"] = alternates
        superseded = [{"id": other["id"], "fixed": other["fixed"], "nRuns": other["n_runs"], "date": other["date"]}
                      for other in all_runs if other["model"] == BUGHUNT[family] and other["effort"] == effort and other.get("superseded")]
        if superseded:
            extra["supersededRowsOnBoard"] = superseded
        if selection_reason:
            extra["selectionReason"] = selection_reason
        board["coverage"][model_id] = cell("exact", run["fixed"], run["id"], effort, note, **extra)
    return annotate(board, "bug-hunt", PREVIOUS_OTHER)


def rendered_vals_row(page: str, link: str, label: str) -> tuple[float, float] | None:
    """(score %, cost per test) of the table row on a saved Vals benchmark page whose model link is /models/<link>."""
    match = re.search(r'/models/' + re.escape(link) + r'">' + re.escape(label) + r'</a>\s*</th>\s*<td>[^<]*</td>\s*<td>([\d.]+)%</td>\s*'
                      r'<td>\$([\d.]+)</td>', page)
    return (float(match.group(1)), float(match.group(2))) if match else None


def vals_page_text(path: Path) -> str:
    text = re.sub(r"<script.*?</script>|<style.*?</style>", "", path.read_text(), flags=re.S)
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", text)))


def vals() -> dict:
    document = {"capturedAt": max(READ["vibe-code"], READ["code-migration-v1-1"]),
                "method": "As on 2026-10-25, 2026-10-30 and 2026-11-01: each board page read, its benchmarkViewUrl prop's hashed "
                          "/_astro/benchmark_view_*.json downloaded (vals/<slug>.json, URL in vals/<slug>.jsonUrl.txt); values from "
                          "tasks.overall.<model key>. Exact = same Vals model key (model version) and reasoning_effort/compute_effort "
                          "equal to AA's effort, or, where AA plots no effort, the documented or owner-stated equivalent (O149 "
                          "MiMo-V2.6-Flash); absent otherwise. Vals model pages read 2026-11-26 in vals/_models/ (read "
                          + (HERE / "vals" / "_models" / "readAt.txt").read_text().strip() + "; MiMo-V2.6-Pro page "
                          + (HERE / "vals" / "_models" / "mimo.readAt.txt").read_text().strip() + ").",
                "cohortSource": "research/2026-11-26-recapture/cohort.json (45 configurations: 31 current + 14 retained)", "benchmarks": []}
    for slug, name, harness in (("vibe-code", "Vibe Code Bench v1.1", "OpenHands"), ("code-migration-v1-1", "Code Migration v1.1", "Pi agent harness")):
        source = json.loads((HERE / "vals" / f"{slug}.json").read_text())
        old = json.loads((PREVIOUS / "vals" / f"{slug}.json").read_text())["tasks"]["overall"]
        rows = source["tasks"]["overall"]
        page = (HERE / "vals" / f"{slug}.html").read_text()
        board = {"slug": slug, "name": name, "version": "1.1", "updated": source["metadata"]["updated"], "models": len(rows),
                 "harness": harness + ", the same for every model row", "sourceUrl": f"https://www.vals.ai/benchmarks/{slug}",
                 "jsonUrl": (HERE / "vals" / f"{slug}.jsonUrl.txt").read_text().strip(),
                 "captureFile": f"research/2026-11-26-recapture/third-party/vals/{slug}.json", "readAt": READ[slug],
                 f"changesSince{PREVIOUS_TAG}": {
                     "added": sorted(set(rows) - set(old)), "removed": sorted(set(old) - set(rows)),
                     "valueChanged": sorted(key for key in old if key in rows and
                                            (old[key]["accuracy"], old[key]["stderr"]) != (rows[key]["accuracy"], rows[key]["stderr"])),
                     "fileIdentical": (HERE / "vals" / f"{slug}.json").read_bytes() == (PREVIOUS / "vals" / f"{slug}.json").read_bytes()},
                 "coverage": {}}
        text = vals_page_text(HERE / "vals" / f"{slug}.html")
        superseded = re.search(r"Archived Benchmark (.{0,260}?Previous results are preserved here\.)", text)
        board["versionStatus"] = ({"archived": True, "bannerText": superseded.group(1).strip(), "supersededBy": "Vibe Code Bench v1.1.1",
                                   "successorSlug": "vibe-code-v1-1-1", "pinnedHere": "v1.1 stays the leaf (owner instruction 2026-11-26); "
                                   "v1.1.1 values are reference only (successorReference), never moved into coverage."}
                                  if superseded else
                                  {"archived": False, "bannerText": None, "supersededBy": None,
                                   "note": "No 'superseded' or 'Archived Benchmark' banner on the page on 2026-11-26."})
        for model_id, (family, effort) in COHORT.items():
            key = VALS[family]
            row = rows.get(key)
            row_effort = (row.get("reasoning_effort") or row.get("compute_effort")) if row else None
            if row is None:
                board["coverage"][model_id] = {"status": "absent", "value": None, "stderr": None, "valsKey": None, "effort": None,
                                               "note": f"No {key} row on this board." + (" The board lists no Gemini 4 Neon row." if family == "neon" else "")}
            elif family == "mimo-flash":
                # O149 (2026-11-01): Vals states both MiMo models were evaluated with reasoning enabled, which is
                # MiMo-V2.6-Flash's configuration (thinking enabled, O140), so its records match.
                mimo_page = vals_page_text(HERE / "vals" / "_models" / "xiaomi_mimo-v2.6-pro.html")
                if "We evaluated them with reasoning enabled" not in mimo_page:
                    raise ValueError("Vals' MiMo model page no longer says 'We evaluated them with reasoning enabled'")
                board["coverage"][model_id] = {"status": "exact", "value": row["accuracy"], "stderr": row["stderr"], "valsKey": key,
                                               "effort": "enabled (O140)", "harness": row.get("harness"), "match": "owner (O149)",
                                               "note": O135 + " Vals records reasoning, reasoning_effort and compute_effort as null; its "
                                                       "MiMo-V2.6-Pro model page (vals/_models/xiaomi_mimo-v2.6-pro.html, re-read "
                                                       "2026-11-26), in its 2026-09-22 update covering both MiMo V2.6 models, still says "
                                                       "'We evaluated them with reasoning enabled' through the official Xiaomi API, so the "
                                                       "record is the thinking-enabled configuration (owner decision O149, 2026-11-01)."}
            elif row_effort == effort:
                note = base_note(model_id)
                extra = {}
                if family == "neon":
                    # Vals' JSON keeps the pre-release codename; its page labels the row "Gemini 4 Neon". The saved page's rendered
                    # row must carry the same score and cost as the JSON key, or the alias is not established.
                    rendered = rendered_vals_row(page, "google_gemini-4-neon", "Gemini 4 Neon")
                    if rendered is None or abs(rendered[0] - round(row["accuracy"], 2)) > 0.011 or abs(rendered[1] - round(row["cost_per_test"], 2)) > 0.011:
                        raise ValueError(f"{slug}: rendered 'Gemini 4 Neon' row {rendered} does not match JSON key {key}")
                    extra = {"match": "page label (rendered row)", "renderedRow": {"model": "Gemini 4 Neon", "scorePct": rendered[0], "costPerTest": rendered[1]}}
                    note = join_notes(note, f"Vals' JSON names this row '{key}' (a pre-release codename); the benchmark page labels the same "
                                            f"row 'Gemini 4 Neon' (link /models/google_gemini-4-neon) with identical score ({rendered[0]}%) and "
                                            f"cost (${rendered[1]}), and the Gemini 4 Neon model page (vals/_models/google_gemini-4-neon.html) "
                                            "records Reasoning Effort: xhigh, equal to the key's reasoning_effort.")
                if family == "fable":
                    note = join_notes(note, "Vals' Claude Fable 5.2 page (vals/_models/anthropic_claude-fable-5-2.html) records 'Compute "
                                            "Effort: high'; Vals evaluated this model at high only.")
                if family == "ember":
                    note = join_notes(note, "Vals' Muse Ember page (vals/_models/meta_muse-ember.html) records 'Reasoning Effort: max'.")
                board["coverage"][model_id] = {"status": "exact", "value": row["accuracy"], "stderr": row["stderr"], "valsKey": key,
                                               "effort": effort, "harness": row.get("harness"), "note": note, **extra}
            else:
                board["coverage"][model_id] = {"status": "absent", "value": None, "stderr": None, "valsKey": None, "effort": None,
                                               "note": f"Vals ran this model only at {row_effort} ({row['accuracy']}), not {effort}; not transferred."}
        board["coverageCounts"] = counts(board)
        board = annotate(board, slug, PREVIOUS_VALS)
        if slug == "vibe-code":
            board["successorReference"] = vals_successor()
        document["benchmarks"].append(board)
    return document


def vals_successor() -> dict:
    """Vibe Code Bench v1.1.1 facts for the README note: reference only, never matched into coverage."""
    source = json.loads((HERE / "vals" / "vibe-code-v1-1-1.json").read_text())
    rows = source["tasks"]["overall"]
    v11 = json.loads((HERE / "vals" / "vibe-code.json").read_text())["tasks"]["overall"]
    values = {}
    for model_id, (family, effort) in COHORT.items():
        key = VALS[family]
        row = rows.get(key)
        if row is None or family == "mimo-flash":
            continue
        row_effort = row.get("reasoning_effort") or row.get("compute_effort")
        if row_effort == effort:
            values[model_id] = {"valsKey": key, "value": row["accuracy"], "stderr": row["stderr"], "valsEffort": row_effort,
                                "v1_1Value": v11[key]["accuracy"]}
    shared = sorted(set(rows) & set(v11))
    same_cost = sum(1 for k in shared if rows[k]["cost_per_test"] == v11[k]["cost_per_test"])
    drops = [v11[k]["accuracy"] - rows[k]["accuracy"] for k in shared]
    return {"notUsedAsLeaf": True, "slug": "vibe-code-v1-1-1", "version": source["metadata"]["version"], "updated": source["metadata"]["updated"],
            "models": len(rows), "jsonUrl": (HERE / "vals" / "vibe-code-v1-1-1.jsonUrl.txt").read_text().strip(),
            "captureFile": "research/2026-11-26-recapture/third-party/vals/vibe-code-v1-1-1.json", "readAt": READ["vibe-code-v1-1-1"],
            "whatChanged": "Vals' banner on v1.1: 'superseded by v1.1.1, which upgrades the grader, requires every substep to pass, and fixes "
                           "ambiguous tests'. Of the {n} model keys on both versions, {c} have identical cost per test (the runs look reused and re-graded) "
                           "and the accuracy falls by {lo:.1f} to {hi:.1f} points (mean {mean:.1f}).".format(
                               n=len(shared), c=same_cost, lo=min(drops), hi=max(drops), mean=sum(drops) / len(drops)),
            "coverageAtSameEffort": values,
            "coverageAtSameEffortNote": "Cohort configurations whose Vals effort equals AA's, with the v1.1.1 value beside the v1.1 leaf. Reference only: "
                                        "no v1.1.1 value enters coverage. Vals' v1.1.1 board has no Gemini 4 Neon row under 'google/gemini-4-neon' either; "
                                        "its page labels the codename key '" + VALS_NEON_KEY + "' as Gemini 4 Neon (80.23%), which is the same alias as on v1.1."}


def livebench_effort(site: str, label: str) -> str | None:
    match = re.search(r'"' + re.escape(label) + r'":\{[^}]*?effort:"(\w+)"', site)
    return match.group(1) if match else None


def livebench() -> dict:
    release, previous_release = LIVEBENCH_RELEASE, PREVIOUS_LIVEBENCH_RELEASE
    table = {row["model"]: row for row in csv.DictReader((HERE / "livebench" / f"table-{release}.csv").open())}
    old_table = {row["model"]: row for row in csv.DictReader((HERE / "livebench" / f"table-{previous_release}.csv").open())}
    categories = json.loads((HERE / "livebench" / f"categories-{release}.json").read_text())
    names = {"Long Agentic": "long_agentic", "Reasoning": "reasoning", "Coding": "coding", "Browser": "browser",
             "Data Analysis": "data_analysis", "Research": "research", "Design": "design"}
    weights = {column: float(categories["_overall_weights"].get(name, 1.0)) for name, column in names.items()}
    site = (HERE / "livebench" / "site-main.js").read_text()
    releases = re.search(r'=\["(20\d{6})"(?:,"(20\d{6})")*\]', site)
    release_list = re.findall(r'"(20\d{6})"', releases.group(0)) if releases else []
    if max(release_list) != release:
        raise ValueError(f"LiveBench lists a newer release than the pinned {release}: {release_list} (record it; do not switch)")
    last_modified = re.search(r"last-modified: (.+)", (HERE / "livebench" / f"table-{release}.headers.txt").read_text(), re.I).group(1).strip()

    def overall(row: dict) -> float:
        return round(sum(weights[c] * float(row[c]) for c in weights) / sum(weights.values()), 2)

    # Files of the previous pin and of 20261014 as saved on 2026-11-01 versus today's copies (in-place edits).
    in_place = {}
    for stem, ext in (("table", "csv"), ("categories", "json"), ("cost", "csv"), ("notes", "json"), ("breakdown", "json")):
        for rel in (previous_release, "20261014"):
            now = (HERE / "livebench" / f"{stem}-{rel}.{ext}").read_bytes()
            before = (PREVIOUS / "livebench" / f"{stem}-{rel}.{ext}").read_bytes()
            in_place[f"{stem}-{rel}.{ext}"] = "identical" if now == before else "changed since the 2026-11-01 copy"
    old_breakdown = json.loads((PREVIOUS / "livebench" / f"breakdown-{previous_release}.json").read_text())
    new_breakdown = json.loads((HERE / "livebench" / f"breakdown-{previous_release}.json").read_text())
    edits = []
    for category, body in new_breakdown.items():
        for model, entry in body.get("models", {}).items():
            before = old_breakdown.get(category, {}).get("models", {}).get(model)
            if before is not None and before != entry:
                old_scores, new_scores = before.get("scores", {}), entry.get("scores", {})
                edits.append({"category": category, "model": model, **{part: [old_scores.get(part), new_scores.get(part)]
                                                                         for part in set(old_scores) | set(new_scores) if old_scores.get(part) != new_scores.get(part)}})
    notes = " ".join(json.loads((HERE / "livebench" / f"notes-{release}.json").read_text()))
    fable_note = re.search(r"max-effort run scored lower overall \((\d+\.\d) at max against (\d+\.\d)\)", notes)
    board = {"key": "livebench2-overall", "name": "LiveBench 2.0 Overall", "version": f"LiveBench 2.0 release {release}",
             "updated": f"2026-11-06 (release 20261106; release files' HTTP Last-Modified {last_modified})",
             "readAt": READ["livebench"], "sourceUrl": f"https://livebench.ai/data/{release}/table.csv",
             "pinnedReleaseStatus": f"Release {release} is pinned under owner decision O211 (the 2026-11-01 read pinned 20261025, O139). On "
                                    f"2026-11-26 the site bundle (main.099aad9b.js) lists releases {release_list}; no newer release exists "
                                    "(data/20261107 to data/20261126 return 404, livebench/newer-release-probe.txt). Release 20261025 and "
                                    "20261014 are still served and saved.",
             "previousPin": {"release": previous_release, "inPlaceEditsSince20261101": in_place, "breakdownScoreEdits": edits},
             "weights": weights, "harness": "LiveBench's own; one run per model at its highest supported effort (effort from the site bundle's model metadata)",
             "metric": "weighted mean of the seven category scores with the release's _overall_weights (as O67), 0-100",
             "weightsNote": "notes.json still says 'Every suite counts equally' while categories.json carries _overall_weights (Long Agentic 2.0, "
                            "Coding 1.5, Design 1.5). The site's own Overall for Claude Fable 5.2 (xhigh), 84.9 (notes.json), equals the weighted mean "
                            f"{overall(table['claude-fable-5.2'])} and not the unweighted mean "
                            f"{round(sum(float(table['claude-fable-5.2'][c]) for c in weights) / 7, 2)}, so the weighted method (O67) is the board's own.",
             "coverage": {}}
    for model_id, (family, effort) in COHORT.items():
        label = LIVEBENCH[family]
        row = table.get(label)
        if row is None:
            board["coverage"][model_id] = cell("absent", note=f"No {label} row in release {release} (nor in the site's model metadata)."
                                               if livebench_effort(site, label) is None else
                                               f"No {label} row in release {release} (the site's model metadata lists it at "
                                               f"{livebench_effort(site, label)}).")
            continue
        row_effort = livebench_effort(site, label)
        value = overall(row)
        if row_effort == effort:
            note = base_note(model_id)
            if family == "fable":
                note = join_notes(note, f"LiveBench shows Claude Fable 5.2 at xhigh: its notes.json says 'Claude Fable 5.2 is shown at xhigh because "
                                        f"its max-effort run scored lower overall ({fable_note.group(1)} at max against {fable_note.group(2)})'. "
                                        f"The weighted Overall rebuilt here, {value}, rounds to the site's {fable_note.group(2)}.")
            extra = {"categories": {column: float(row[column]) for column in weights}}
            if label in old_table:
                extra["previousPinOverall"] = overall(old_table[label])
            board["coverage"][model_id] = cell("exact", value, label, effort, note, **extra)
        elif family == "fable" and effort == "max":
            board["coverage"][model_id] = cell(
                "absent", None, None, None,
                f"LiveBench has Claude Fable 5.2 at xhigh only (Overall {value}). Its notes.json states that the max-effort run scored "
                f"{fable_note.group(1)} overall (against {fable_note.group(2)} at xhigh) but publishes no row or category scores for that run, so "
                "the weighted Overall cannot be rebuilt and no value is entered; the stated figure is carried as siteNoteOverallAtMax for the "
                "owner's decision (it is the same Overall metric at the same effort, but it is a note, not a table row).",
                siteNoteOverallAtMax=float(fable_note.group(1)))
        else:
            board["coverage"][model_id] = cell("absent", note=f"LiveBench 2.0 has {label} at {row_effort} only (Overall {value}); not transferred.")
    return annotate(board, "livebench2-overall", PREVIOUS_OTHER)


def aicd_header() -> dict:
    text = vals_page_text(HERE / "aicd" / "leaderboard.html")
    maxima = {"total": re.search(r"Total points \(max (\d+)\)", text), "laravel": re.search(r"Laravel Code Quality \(max (\d+)\)", text),
              "react": re.search(r"React-TS Code Quality \(max (\d+)\)", text), "bug": re.search(r"Bug Finding Test \(max (\d+)\)", text),
              "python": re.search(r"Python Code Quality \(max (\d+)\)", text), "edge": re.search(r"Edge-case Testing \((\d+) projects, max (\d+)\)", text)}
    parsed = {key: int(match.group(match.lastindex)) for key, match in maxima.items() if match}
    if (parsed.get("laravel"), parsed.get("react"), parsed.get("edge")) != (20, 20, 20):
        raise ValueError(f"AI Coding Daily leaf columns no longer max 20 each: {parsed}")
    update = re.search(r"Last update: ([^()]*\([^)]*\))", text)
    return {"maxima": parsed, "edgeProjects": int(maxima["edge"].group(1)), "lastUpdate": update.group(1).strip() if update else None,
            "penaltyColumn": "Penalty = points deducted for inconsistent results across attempts (negative or 0); total = Laravel + React-TS + "
                             "Bug Finding + Python + Edge-case + Penalty"}


def aicd(bughunt_board: dict) -> dict:
    rows = json.loads((HERE / "aicd" / "leaderboard-allrows-parsed.json").read_text())
    old_rows = {(r["model"], r["harness"]): r for r in json.loads((PREVIOUS / "aicd" / "leaderboard-allrows-parsed.json").read_text())}
    new_keys = {(r["model"], r["harness"]) for r in rows}
    columns = ("laravel", "react", "bug", "edge")
    header = aicd_header()
    identity_ok = 0
    for r in rows:
        parts = [float(r[c]) for c in ("laravel", "react", "bug", "python", "edge") if r.get(c)]
        if abs(sum(parts) + float(r["penalty"].replace("−", "-")) - float(r["total"])) <= 0.02:
            identity_ok += 1
    board = {"key": "aicd", "name": "AI Coding Daily LLM Coding Leaderboard",
             "version": "v3 scoring: Laravel + React-TS + Bug Finding + Python + Edge-case (max 90) less a consistency penalty",
             "readAt": READ["aicd"], "pageReadAt": READ["aicdPage"],
             "sourceUrl": "https://aicodingdaily.com/leaderboard (every row: Livewire POST to /livewire-71a08158/update with "
                          "hiddenOlderModelIds=[]; bestHarnessOnly false)",
             "rows": len(rows), "boardHeader": header,
             "values": "value = nonBug = Laravel + React-TS + Edge-case (max 60, the ValueRank leaf as before); each row also carries total (now "
                       "max 90), python (new project, max 20), bug (max 10), penalty and the other columns",
             "methodologyChange": "Since 2026-11-11 the board scores 8 projects / 33 prompts and adds the Python 'Pricing Engine' project and a "
                                  "per-project Consistency Penalty (methodology article, aicd/articles/methodology.html, published 2026-11-11). The "
                                  "total moved from max 70 to max 90; Laravel, React-TS and Edge-case keep their max of 20 and their definitions, so the "
                                  "non-bug leaf (max 60) is still well defined, but a leaf that included Python would be max 80 (nonBugWithPython). "
                                  "Almost every row was re-dated 2026-11-13/14 when its Python run was added; its Laravel, React-TS and Edge-case "
                                  "scores are unchanged except where listed in rowChangesSince20261101.",
             "totalIdentityCheck": f"{identity_ok} of {len(rows)} rows satisfy total = columns + penalty within 0.02",
             f"rowChangesSince{PREVIOUS_TAG}": {
                 "added": sorted(f"{m} [{h}]" for (m, h) in new_keys - set(old_rows)),
                 "removed": sorted(f"{m} [{h}]" for (m, h) in set(old_rows) - new_keys),
                 "leafOrBugColumnChanged": [{"row": f"{r['model']} [{r['harness']}]",
                                             "changes": {c: [old_rows[k][c], r[c]] for c in columns if old_rows[k][c] != r[c]}}
                                            for r in rows for k in [(r["model"], r["harness"])]
                                            if k in old_rows and any(old_rows[k][c] != r[c] for c in columns)],
                 "testedDateMoved": sum(1 for r in rows for k in [(r["model"], r["harness"])] if k in old_rows and old_rows[k]["tested"] != r["tested"]),
                 "rowsCompared": sum(1 for r in rows if (r["model"], r["harness"]) in old_rows)},
             "coverage": {}}
    for model_id, (family, effort) in COHORT.items():
        prefix = AICD[family] + " ("
        family_rows = [row for row in rows if row["model"].startswith(prefix)]
        wanted = "high" if family == "mimo-flash" else effort
        hit = [row for row in family_rows if AICD_EFFORT.get(row["model"][len(prefix):-1]) == wanted]
        if not hit:
            board["coverage"][model_id] = cell("absent", note=near_note([(f"{row['model']} [{row['harness']}, {row['tested']}]", row["total"])
                                                                         for row in family_rows], "AI Coding Daily"))
            continue
        entries = []
        for row in hit:
            if row["tested"] > CUTOFF[:10]:
                raise ValueError(f"{row['model']} dated after the capture day")
            bug = float(row["bug"]) if row["bug"] else None
            python = float(row["python"]) if row.get("python") else None
            non_bug = round(float(row["laravel"]) + float(row["react"]) + float(row["edge"]), 2)
            entries.append({"total": float(row["total"]), "nonBug": non_bug,
                            "nonBugWithPython": round(non_bug + python, 2) if python is not None else None,
                            "laravel": float(row["laravel"]), "react": float(row["react"]), "bug": bug, "python": python,
                            "edge": float(row["edge"]), "penalty": float(row["penalty"].replace("−", "-")),
                            "harness": row["harness"], "tested": row["tested"], "ageText": row["age"], "cost": row["cost"],
                            "time": row["time"], "rank": row["rank"]})
        selection = None
        if len(entries) > 1:
            # E268 (I50 M2): the row on the harness of the configuration's Bug Hunt record, else the latest test date, else stop.
            bug_harness = (bughunt_board["coverage"][model_id].get("harness") or "")
            same = [e for e in entries if bug_harness.startswith(e["harness"])]
            if len(same) == 1:
                chosen, selection = same[0], f"E268: the row on the Bug Hunt record's harness ({bug_harness})."
            else:
                latest = max(e["tested"] for e in entries)
                dated = [e for e in entries if e["tested"] == latest]
                if len(dated) != 1:
                    raise ValueError(f"{model_id}: {len(entries)} AI Coding Daily rows and no E268 tie-break")
                chosen, selection = dated[0], "E268: the latest test date."
            entries = [chosen] + [e for e in entries if e is not chosen]
        note = base_note(model_id)
        if family == "mimo-flash":
            note = (O135 + " The board's only MiMo-V2.6-Flash row is labelled High; Xiaomi documents every enabled level as the same "
                    "reasoning ('Values xhigh, max and ultra are mapped to high'), so the High row is the documented default "
                    "configuration (thinking enabled). The row does not name the provider route behind OpenCode.")
        elif family == "ember":
            note = ("The board names the model 'Muse Ember 1.0'; AA, Vals and tbench.ai name it 'Muse Ember' (no version), and the board's own "
                    "video title is 'I Tested NEW Muse Ember on Coding' (aicd/model-pages/muse-ember-1-0.html). No other Muse Ember version "
                    "appears on any board, so '1.0' is read as the model's release name, not a second version. Flag for the owner (O36 asks for the "
                    "same model version).")
        if entries[0]["bug"] is None:
            note = join_notes(note, f"Tested {entries[0]['tested']}, before the Bug Finding project was added (2026-10-03): the listed "
                                    f"total {entries[0]['total']} is out of 60 (Laravel + React-TS + Edge-case), so no total with bug-finding "
                                    "exists; the non-bug leaf is exact. Row is hidden by default as an older LLM.")
        if entries[0]["python"] is None:
            note = join_notes(note, "No Python Code Quality score on this row (total and the new methodology's Python project are absent).")
        extra = {"rows": entries}
        if selection:
            extra["selection"] = selection
        board["coverage"][model_id] = cell("exact", entries[0]["nonBug"], hit[0]["model"], wanted, note, **extra)
    return annotate(board, "aicd", PREVIOUS_OTHER)


def tbench() -> dict:
    parsed = json.loads((HERE / "tbench" / "tbench-rows-parsed-2026-11-26.json").read_text())
    old_parsed = json.loads((PREVIOUS / "tbench" / "tb4-rows-parsed-2026-11-01.json").read_text())
    scrape = TBENCH_SCRAPE
    scrape_40 = json.loads((HERE / "tbench" / "tbench-v40-scrape-2026-11-26.json").read_text())
    flight = _flight(scrape["scripts"])
    leaderboard = re.search(r'"id":"([0-9a-f-]+)","package_id":"[0-9a-f-]+","package":"terminal-bench/terminal-bench","dataset_version_ids":'
                            r'\[([^\]]*)\],"name":"([^"]+)","title":"([^"]+)","description":"([^"]+)"', flight)
    if leaderboard is None or leaderboard.group(4) != "Terminal-Bench 4.1":
        raise ValueError(f"the tbench.ai default leaderboard is no longer Terminal-Bench 4.1: {leaderboard and leaderboard.group(4)}")
    version = "4.1"
    rendered = {(row[1], row[2]) for row in scrape["rows"][1:] if len(row) == 7}
    rendered_40 = sum(1 for row in scrape_40["rows"][1:] if len(row) == 7)
    previous_by_key = {(r["model"], r["effort"], r["agent"]): r["accuracy"] for r in old_parsed["rows"]}
    board = {"key": "tbench-4", "name": "Terminal-Bench 4.1 (tbench.ai)", "version": version, "updated": parsed["leaderboardUpdatedAt"],
             "readAt": READ["tbench"], "sourceUrl": "https://www.tbench.ai/ (the /leaderboard/terminal-bench/4.0 and /4.1 paths redirect to the home page)",
             "leaderboard": {"id": leaderboard.group(1), "name": leaderboard.group(3), "title": leaderboard.group(4), "description": leaderboard.group(5),
                             "datasetVersionIds": json.loads("[" + leaderboard.group(2) + "]"),
                             "rowVersionRule": "The embedded payload has one leaderboard (id above, name 4-1-0) and no per-row version field; every "
                                               "row is therefore a Terminal-Bench 4.1 row (cell.version)."},
             "versionsOffered": {"4.1": f"default board ({parsed['rowCount']} payload rows, {len(rendered)} in the rendered table)",
                                 "4.0": f"older board, rendered with /?version=4.0 ({rendered_40} rows; saved only as tbench/tbench-v40-scrape-2026-11-26.json "
                                        "for reference, its rows are fetched client-side and are not in the embedded payload); 3.0 is also selectable "
                                        "(/leaderboard/terminal-bench/3.0 redirects to /?version=3.0). 4.0 values are never matched: AA's Index runs 4.1."},
             "note": f"Reference only: ValueRank's Terminal-Bench leaf comes from AA, whose Coding Agent Index v2.1 runs Terminal-Bench 4.1. The rendered "
                     f"table shows {len(rendered)} rows (one per model, its best effort); the page's own embedded leaderboard payload holds "
                     f"{parsed['rowCount']} rows (status 'display'), including lower-effort rows the default view hides.",
             "coverage": {}}
    for model_id, (family, effort) in COHORT.items():
        rows = [row for row in parsed["rows"] if row["model"] == TBENCH[family]]
        if family == "mimo-flash":
            hit = [row for row in rows if row["effort"] == "none"]
            if hit:
                row = hit[0]
                board["coverage"][model_id] = cell(
                    "plausible", row["accuracy"], f"{row['model']} ({row['effort']})", row["effort"],
                    O135 + " tbench.ai's only MiMo V2.6 Flash row is labelled effort 'none' on mini-swe-agent: the board does not say whether that is "
                    "the provider default (thinking enabled) or reasoning off, so the row stays unmatched (the O140 rule for a board that records "
                    "no effort). Version 4.1.", agent=row["agent"], ci95=row["ci95"], date=row["date"], version=version,
                    renderedInTable=(f"{row['model']} ({row['effort']})", row["agent"]) in rendered)
            else:
                board["coverage"][model_id] = cell("absent", note="No MiMo V2.6 Flash row on tbench.ai.")
            continue
        hit = [row for row in rows if row["effort"] == effort]
        if hit:
            row = hit[0]
            label = f"{row['model']} ({row['effort']})"
            shown = (label, row["agent"]) in rendered
            note = join_notes("" if shown else "In the page payload only, not in the default rendered table.", base_note(model_id))
            before = previous_by_key.get((row["model"], row["effort"], row["agent"]))
            if before is not None:
                note = join_notes(note, f"The 2026-11-01 read of the Terminal-Bench 4.0 board listed this row at {before}; that is a different version "
                                        "and is not used.")
            board["coverage"][model_id] = cell("exact", row["accuracy"], label, effort, note, agent=row["agent"], ci95=row["ci95"],
                                               date=row["date"], version=version, renderedInTable=shown)
        else:
            board["coverage"][model_id] = cell("absent", note=near_note([(f"{row['model']} ({row['effort']})", row["accuracy"]) for row in rows],
                                                                        "Terminal-Bench 4.1"))
    return annotate(board, "tbench-4", PREVIOUS_OTHER)


def _flight(scripts: list[str]) -> str:
    parts = []
    for script in scripts:
        for match in re.finditer(r'self\.__next_f\.push\(\[1,("(?:[^"\\]|\\.)*")\]\)', script, re.S):
            parts.append(json.loads(match.group(1)))
    return "".join(parts)


def cognition() -> dict:
    """Cognition's FrontierCode 2.0 board (E234 cross-check source): rows, exact cohort mapping and artifact hashes."""
    path = HERE / "cognition" / "frontier-code-2.0-data.json"
    raw = json.loads(path.read_text())
    previous = json.loads((PREVIOUS / "cognition" / "frontier-code-2.0-data.json").read_text())
    page_text = vals_page_text(HERE / "cognition" / "frontiercode.html")
    changelog = []
    section = page_text[page_text.find("Changelog Models added"):]
    for part in re.split(r"(?=(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) \d{1,2}, 2026 )", section)[1:]:
        changelog.append(part.strip())
    chunk = next(p for p in sorted((HERE / "cognition" / "next-static").glob("*.js")) if "frontier-code-2.0/data.json" in p.read_text())
    lineage_match = re.search(r'let o=(\{"GPT-6\.2 Sol":.*?\}),r=Object\.values', chunk.read_text())
    lineage = json.loads(lineage_match.group(1)) if lineage_match else {}
    lineage_models = sorted({m for models in lineage.values() for m in models})
    excluded_match = re.search(r'l=(\["Beam 1\.0".*?\.\.\.r\])', chunk.read_text())
    defaults_hidden = re.findall(r'"([^"]+)"', excluded_match.group(1)) if excluded_match else []
    ld = re.search(r'"@type":"ItemList","name":"FrontierCode 2\.0 Leaderboard".*?"itemListElement":(\[.*?\])\}</script>',
                   (HERE / "cognition" / "frontiercode.html").read_text(), re.S)
    top10 = json.loads(ld.group(1)) if ld else []
    rows = []
    best = {}
    for model in raw["models"]:
        scores = {effort: raw["data"][model][effort]["main"]["new_score"] for effort in raw["efforts"][model] if raw["data"][model][effort].get("main")}
        best[model] = max(scores, key=lambda e: scores[e])
        for effort in raw["efforts"][model]:
            sub = raw["data"][model][effort].get("main")
            if sub is None:
                continue
            rows.append({"model": model, "effort": effort, "harness": raw["harness"][model], "subset": "main", "subsetTaskCount": raw["subsets"]["main"],
                         "scorePct": fixed1(sub["new_score"]), "newScoreRaw": sub["new_score"],
                         "passRatePct": fixed1(sub["correct"]), "correctRaw": sub["correct"],
                         "costPerRolloutUsd": sub["cost"], "outputTokensPerRollout": sub["tokens"],
                         "flaggedRatePct": fixed1(sub["flagged_rate"]), "runsN": None,
                         "isModelBestEffort": effort == best[model], "historicalLineageOnly": model in lineage_models})
    top10_check = []
    for item in top10:
        score = float(re.search(r"([\d.]+)%", item["description"]).group(1))
        data_best = next(r for r in rows if r["model"] == item["name"] and r["isModelBestEffort"])
        top10_check.append({"model": item["name"], "ldJsonScorePct": score, "dataJsonBestEffort": data_best["effort"],
                            "dataJsonScorePct": data_best["scorePct"], "match": score == data_best["scorePct"]})
    mapping = []
    for model_id, (family, effort) in COHORT.items():
        config = next(c for c in CONFIGURATIONS if c["id"] == model_id)
        item = {"configurationId": model_id, "displayName": config["displayName"], "chartTier": config["chartTier"]}
        model = COGNITION[family]
        if model is None or model not in raw["models"]:
            name = {"ember": "Muse Ember", "terra": "GPT-6.1 Terra", "mimo-flash": "MiMo-V2.6-Flash"}[family]
            item.update({"status": "no row", "reason": f"No {name} row on Cognition's FrontierCode 2.0 data.json ({len(raw['models'])} models; "
                                                        "none by that name)."})
        elif effort is None or effort not in raw["efforts"][model]:
            item.update({"status": "no row", "reason": f"Cognition lists {model} only at {raw['efforts'][model]}; no {effort} row, nothing transferred.",
                         "cognitionModel": model})
        else:
            sub = raw["data"][model][effort]["main"]
            lineage_only = model in lineage_models
            item.update({"status": "exact", "cognitionModel": model, "cognitionEffort": effort, "cognitionHarness": raw["harness"][model],
                         "cognitionScorePct": fixed1(sub["new_score"]), "cognitionCostPerRolloutUsd": sub["cost"],
                         "reason": "Exact model label and exact effort label on Cognition's board.",
                         "caveat": ("Cognition's board JS lists this model under another model's lineage (shown in the lineage animation on hover, "
                                    "excluded from the default list); its row is in data.json." if lineage_only else None)})
            if model_id in FALLBACK:
                item["fallbackNote"] = FALLBACK_NOTE
        mapping.append(item)
    exact = sum(1 for item in mapping if item["status"] == "exact")
    artifacts = []
    for rel, url in (("frontiercode.html", "https://cognition.com/frontiercode"),
                     ("frontiercode-leaderboard-data.json", "https://cognition.com/data/frontiercode-leaderboard/data.json"),
                     ("frontier-code-2.0-data.json", "https://cognition.com/data/frontier-code-2.0/data.json"),
                     ("blog-frontier-code-2.0.html", "https://cognition.com/blog/frontier-code-2.0")):
        artifacts.append({"path": rel, "url": url, "sha256": hashlib.sha256((HERE / "cognition" / rel).read_bytes()).hexdigest()})
    for chunk_path in sorted((HERE / "cognition" / "next-static").glob("*.js")):
        artifacts.append({"path": f"next-static/{chunk_path.name}", "url": f"https://cognition.com/_next/static/immutable/chunks/{chunk_path.name}",
                          "sha256": hashlib.sha256(chunk_path.read_bytes()).hexdigest()})
    last_modified = re.search(r"last-modified: (.+)", (HERE / "cognition" / "frontier-code-2.0-data.json.headers").read_text(), re.I).group(1).strip()
    old_scores = {(m, e): previous["data"][m][e]["main"]["new_score"] for m in previous["models"] for e in previous["efforts"][m]
                  if previous["data"][m][e].get("main")}
    changed_since = {f"{r['model']} {r['effort']}": {PREVIOUS_TAG: fixed1(old_scores[(r["model"], r["effort"])]), TAG: r["scorePct"]}
                     for r in rows if (r["model"], r["effort"]) in old_scores and fixed1(old_scores[(r["model"], r["effort"])]) != r["scorePct"]}
    return {
        "schema": "valuerank-third-party-capture/cognition-frontiercode-2.0", "benchmark": "FrontierCode 2.0", "publisher": "Cognition",
        "sourceUrls": {"data": "https://cognition.com/data/frontier-code-2.0/data.json", "page": "https://cognition.com/frontiercode",
                       "blog": "https://cognition.com/blog/frontier-code-2.0",
                       "discoveredVia": f"Leaderboard client component (module 9623/60302 in /_next/static/immutable/chunks/{chunk.name}) config "
                                        "{label:'FrontierCode 2.0', dataUrl:'/data/frontier-code-2.0/data.json'}; read as text, not executed."},
        "capturedAt": READ["cognitionPage"], "dataJsonCapturedAt": READ["cognition"],
        "boardLastUpdated": "2026-11-24",
        "boardLastUpdatedNote": "Latest entry in the page's own Changelog ('Nov 24, 2026: Added SWE-2.1.'). data.json HTTP Last-Modified: "
                                f"{last_modified} (server header, not a board statement).",
        "blogPublished": "2026-10-27", "taskCount": raw["subsets"]["main"], "subsets": raw["subsets"],
        "scoring": {"scoreField": "new_score", "score": "Score is a weighted aggregate of the rubric items. Solutions that don't pass blocking criteria "
                                                         "receive 0; runs flagged for unfair internet use receive 0 (board text). Since 2026-11-11 the "
                                                         "cheating scanner combines rule-based checks with a filtering judge and every result was rescored.",
                    "passRate": "Field 'correct': fraction of trials satisfying every blocker rubric criterion (all-or-nothing per trial), averaged over tasks.",
                    "cost": "Field 'cost': mean USD spend per rollout at list API pricing, including public discounts (board label 'Cost / rollout').",
                    "tokens": "Mean output tokens per rollout.", "flaggedRate": "Fraction of runs flagged for unfair internet use (each scored 0).",
                    "headlineRanking": "The default table and ld+json top-10 rank each model at its best-scoring effort; a per-effort view lists every row.",
                    "rounding": "scorePct reproduces the page's JS (100*x).toFixed(1)."},
        "runsPerTask": None, "runsPerTaskNote": "Not stated for the board; runsN is null on every row.",
        "harnessLabelsNote": "data.json's harness map now holds display labels ('Devin CLI', 'Codex', 'Claude Code', 'Antigravity CLI', ...); on "
                             "2026-11-01 it held raw keys ('devin-cli', 'codex', 'claude-code').",
        "historicalLineageModels": lineage_models, "lineageMap": lineage,
        "historicalLineageNote": "Board JS (chunk above) lists these as lineage of the model that replaced them; they stay in data.json and are hidden from "
                                 "the default list. On 2026-11-01 only GPT-5.5, GPT-5.6 Sol, GPT-6 Sol, Claude Opus 4.8, Claude Opus 5, SWE-1.6 and "
                                 "SWE-1.7 were lineage; GPT-6.1 Sol, GPT-6 Astra and Claude Fable 5.1 now are too.",
        "excludedFromDefaultList": defaults_hidden, "rowCount": len(rows), "modelCount": len(raw["models"]), "rows": rows,
        "ldJsonTop10Check": top10_check,
        "blogCrossCheck": "The blog (2026-10-27) was edited in place: its results chart now lists Fable 5.2, GPT-6.2 Sol/Astra and Gemini 4 Neon with the "
                          "same best-effort values as data.json's ld+json top 10 (checked above). Third-party mirrors were not used.",
        "changelogSinceLastRead": changelog[:next(i for i, c in enumerate(changelog) if c.startswith("Oct 28, 2026"))],
        "valueChangesSince20261101": changed_since,
        "cohortMapping": {"rule": "Exact Cognition model label + exact Cognition effort label only; no best-of across efforts; no assumed efforts.",
                          "aaSource": "data/aa_metrics.json models.<id>.metrics.frontierCode20 (AA FrontierCode 2.0); the AA cross-check fields "
                                      "(aaFrontierCode20, aaMinusCognitionPts) are filled by the release build once the 2026-11-26 AA capture is merged: "
                                      "this capture carries Cognition's side only.",
                          "counts": {"cohort": len(mapping), "exact": exact, "noRow": sum(1 for i in mapping if i["status"] == "no row")},
                          "configurations": mapping},
        "artifacts": artifacts,
        "handling": "Downloaded files are untrusted data. Parsed with python3 -I; JS was read as text only, never executed.",
    }


def later_rows() -> str:
    return (f"No row on any board is dated after {CUTOFF} (the 2026-11-26 chart capture); the build stops on a Bug Hunt or AI Coding "
            f"Daily row dated after that day. Newest rows: Bug Hunt 2026-11-25 (Gemini 4 Neon 1.5.16 reruns, commit {BUGHUNT_COMMIT[:7]}), AI Coding "
            "Daily 2026-11-25 (Gemini 4 Carbon), Vals boards updated 2026-11-19 (v1.1) and 2026-11-21 (v1.1.1), LiveBench release 2026-11-06, "
            "tbench.ai 4.1 leaderboard updated 2026-11-20, Cognition changelog 2026-11-24. Changes after the previous cutoff "
            f"({PREVIOUS_CUTOFF}) are listed in README.md.")


def main() -> None:
    bug = bughunt()
    boards = [bug, livebench(), aicd(bug), tbench()]
    other = {"capturedAt": max(READ[k] for k in ("bughunt", "livebench", "aicd", "tbench")),
             "readAt": {"bugHunt": READ["bughunt"], "liveBench": READ["livebench"], "aiCodingDaily": READ["aicd"],
                        "aiCodingDailyPage": READ["aicdPage"], "tbench": READ["tbench"], "cognition": READ["cognition"]},
             "cutoff": CUTOFF,
             "cohort": "research/2026-11-26-recapture/cohort.json (45 configurations: 20 frontier, 11 near, 14 retained)",
             "retained": sorted(RETAINED),
             "statusRule": "exact = source row names the same model version and the same reasoning effort as the AA configuration (where AA "
                           "plots no effort: the documented default under O135/O140/O149 for MiMo-V2.6-Flash); plausible = same model, effort "
                           "not confirmable (MiMo-V2.6-Flash rows that record no effort or 'default'/'none'; O140 keeps them unmatched); absent = "
                           "no row at this effort or no row for the model. No value is transferred across efforts or versions.",
             "laterRowCheck": later_rows(),
             "benchmarks": boards}
    (HERE / f"coverage-2026-11-26.json").write_text(json.dumps(other, indent=1, ensure_ascii=False) + "\n")
    vals_document = vals()
    (HERE / "vals-catalogue-2026-11-26.json").write_text(json.dumps(vals_document, indent=1, ensure_ascii=False) + "\n")
    cognition_document = cognition()
    (HERE / "cognition" / "frontiercode-2.0-2026-11-26.json").write_text(json.dumps(cognition_document, indent=1, ensure_ascii=False) + "\n")
    print("wrote coverage-2026-11-26.json, vals-catalogue-2026-11-26.json and cognition/frontiercode-2.0-2026-11-26.json")
    print(f"{'board':34} {'exact':>5} {'plausible':>9} {'absent':>6}")
    for board in boards + vals_document["benchmarks"]:
        c = counts(board)
        print(f"{board.get('key') or board['slug']:34} {c['exact']:>5} {c['plausible']:>9} {c['absent']:>6}")
    exact = sum(1 for i in cognition_document["cohortMapping"]["configurations"] if i["status"] == "exact")
    print(f"{'cognition-frontiercode-2.0':34} {exact:>5} {0:>9} {len(COHORT) - exact:>6}")
    print("new-family exact matches:")
    for board in boards + vals_document["benchmarks"]:
        hits = sorted(model_id for model_id, c in board["coverage"].items() if c["status"] == "exact" and COHORT[model_id][0] in NEW_FAMILIES)
        print(f"  {board.get('key') or board['slug']}: {', '.join(hits) or '-'}")
    hits = sorted(i["configurationId"] for i in cognition_document["cohortMapping"]["configurations"]
                  if i["status"] == "exact" and COHORT[i["configurationId"]][0] in NEW_FAMILIES)
    print(f"  cognition-frontiercode-2.0: {', '.join(hits) or '-'}")


if __name__ == "__main__":
    main()
