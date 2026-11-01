"""Third-party board coverage for the 37-configuration cohort of the 2026-11-01 re-capture (owner decisions O65, O68, O145).

Re-reads, with the 2026-10-25 and 2026-10-30 methods (research/2026-10-25-board-reread/,
research/2026-10-30-v5-recapture/third-party/), every board a ranking uses: Bug Hunt Bench, Vals Vibe Code Bench v1.1 and
Code Migration v1.1, LiveBench 2.0 (release 20261025 pinned under O139), AI Coding Daily (every row, hidden older rows
included) and the tbench.ai Terminal-Bench 4.0 leaderboard. The cohort is the 27 configurations of the 2026-10-30 read plus
the ten that left at the v5 re-capture and are retained for one release under O145 (../cohort.json).

Matching is exact configuration only (O36): the source row must name the same model version and the same reasoning effort
as the AA configuration; no value moves across efforts or versions. Where AA plots no effort, the configuration is the
provider's documented default (O66 Kimi K3.1 Pro: max; O135/O140 MiMo-V2.6-Flash: thinking enabled; O135 MiniMax-M3.1-Flash:
max, minimax-effort.md) or the owner's stated mapping (O54/E252 MiMo-V2.6-Pro: thinking enabled, labelled high).

    python3 -I research/2026-11-01-recapture/third-party/build_coverage.py

Writes coverage-2026-11-01.json (other boards) and vals-catalogue-2026-11-01.json (Vals) next to this file.
"""

from __future__ import annotations

import csv
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
PREVIOUS = HERE.parents[1] / "2026-10-30-v5-recapture" / "third-party"
CUTOFF = "2026-11-01T05:53:05Z"  # the new chart capture instant (../chart-capture.json)
PREVIOUS_CUTOFF = "2026-10-30T22:15:18Z"  # the v5 chart capture (2026-10-30 read)
O135 = ("Owner decision O135 (2026-10-30): AA plots MiMo-V2.6-Flash without an effort; Xiaomi's API documents a single "
        "thinking mode (thinking.type enabled/disabled, default enabled; on the Responses API every reasoning.effort other "
        "than none enables the same, undifferentiated reasoning), so the configuration is thinking enabled, the default "
        "(../../2026-10-30-v5-recapture/third-party/mimo-flash-effort.md; Xiaomi docs re-read 2026-11-01, mimo/).")
O66 = ("Owner decision O66 (2026-10-25): AA plots Kimi K3.1 Pro without an effort; Moonshot's API documents reasoning_effort "
       "low / high / max with max the default, so its configuration is taken at max, its maximum effort.")
O54 = ("Owner decision O54 / E252: AA plots MiMo-V2.6-Pro without an effort; Xiaomi documents one thinking mode for "
       "mimo-v2.6-pro (thinking.type enabled/disabled, default enabled; re-read 2026-11-01, mimo/), so the configuration is "
       "thinking enabled, which the owner labels high: a source row labelled high, or stating reasoning enabled, is that "
       "configuration.")
O135_MINIMAX = ("Owner decision O135 (2026-10-30) applied to MiniMax-M3.1-Flash: AA plots it without an effort; MiniMax's API "
                "documents reasoning_effort / output_config.effort low, medium, high, xhigh, max with max the default when "
                "omitted, and thinking cannot be disabled (minimax-effort.md, read 2026-11-01), so the configuration is max. "
                "The O135 research outcome for MiniMax awaits the owner's confirmation (as O140 confirmed MiMo-V2.6-Flash).")

# id: (family, effort). Effort None = AA plots no effort and a documented single-mode equivalent applies (MiMo).
COHORT = {
    "gpt-6-luna-low": ("luna", "low"), "gpt-6-luna-medium": ("luna", "medium"), "gpt-6-luna-high": ("luna", "high"),
    "gpt-6-luna-xhigh": ("luna", "xhigh"), "gpt-6-luna": ("luna", "max"),
    "claude-haiku-5-5-low": ("haiku", "low"), "claude-haiku-5-5-medium": ("haiku", "medium"), "claude-haiku-5-5-high": ("haiku", "high"),
    "mimo-v2-6-flash": ("mimo-flash", None),
    "gpt-6.1-terra-low": ("terra", "low"), "gpt-6.1-terra-medium": ("terra", "medium"), "gpt-6.1-terra-high": ("terra", "high"),
    "gpt-6.1-terra-xhigh": ("terra", "xhigh"), "gpt-6.1-terra": ("terra", "max"),
    "gpt-6.1-sol-low": ("sol", "low"), "gpt-6.1-sol-medium": ("sol", "medium"), "gpt-6.1-sol-high": ("sol", "high"),
    "gpt-6.1-sol-xhigh": ("sol", "xhigh"), "gpt-6.1-sol": ("sol", "max"),
    "gpt-6-astra-high": ("astra", "high"), "gpt-6-astra-xhigh": ("astra", "xhigh"), "gpt-6-astra": ("astra", "max"),
    "claude-opus-5-5-high": ("opus", "high"), "claude-opus-5-5-xhigh": ("opus", "xhigh"), "claude-opus-5-5": ("opus", "max"),
    "claude-sonnet-5-5": ("sonnet", "max"),
    "gemini-4-carbon": ("carbon", "high"),
    # Retained one release under O145 (left the cohort at the v5 re-capture).
    "claude-haiku-5-5": ("haiku", "xhigh"), "claude-haiku-5-5-max": ("haiku", "max"),
    "claude-opus-5-5-medium": ("opus", "medium"), "claude-sonnet-5-5-xhigh": ("sonnet", "xhigh"),
    "deepseek-v4-1-flash-1017": ("deepseek-flash-1017", "max"), "gemini-4-argon": ("argon", "high"),
    "gpt-5.6-luna-low": ("luna-5.6", "low"), "kimi-k3-1-pro": ("kimi-k3.1-pro", "max"),
    "mimo-v2-6-pro": ("mimo-pro", None), "minimax-m3-1-flash": ("minimax-flash", "max"),
}
RETAINED = {"claude-haiku-5-5", "claude-haiku-5-5-max", "claude-opus-5-5-medium", "claude-sonnet-5-5-xhigh",
            "deepseek-v4-1-flash-1017", "gemini-4-argon", "gpt-5.6-luna-low", "kimi-k3-1-pro", "mimo-v2-6-pro", "minimax-m3-1-flash"}
FALLBACK = {"claude-opus-5-5-high", "claude-opus-5-5-xhigh", "claude-opus-5-5", "claude-sonnet-5-5"}
FALLBACK_NOTE = "AA labels this configuration '... with default fallback'; the source has no fallback qualifier (as on 2026-10-25)."
EFFORT_NOTE = {"kimi-k3-1-pro": O66, "minimax-m3-1-flash": O135_MINIMAX}

# The 2026-10-25 release's matches (git show f2a182a:data/*.json) for the retained ten: reference only, re-established here.
REFERENCE_20261025 = {
    "bug-hunt": {"claude-haiku-5-5": 18.3, "claude-haiku-5-5-max": 21.5, "claude-opus-5-5-medium": 30.3, "claude-sonnet-5-5-xhigh": 36.0,
                 "deepseek-v4-1-flash-1017": 42.7, "gemini-4-argon": 40.7, "gpt-5.6-luna-low": 4.0, "kimi-k3-1-pro": 36.0,
                 "mimo-v2-6-pro": 18},
    "vibe-code": {"claude-haiku-5-5-max": 90.444, "deepseek-v4-1-flash-1017": 87.73, "gemini-4-argon": 91.906, "mimo-v2-6-pro": 85.223,
                  "kimi-k3-1-pro": 84.894},
    "code-migration-v1-1": {"claude-haiku-5-5-max": 52.36, "deepseek-v4-1-flash-1017": 67.524, "gemini-4-argon": 70.796,
                            "mimo-v2-6-pro": 48.786},
    "livebench2-overall": {"claude-haiku-5-5-max": 69.85, "deepseek-v4-1-flash-1017": 74.02, "gemini-4-argon": 79.3,
                           "mimo-v2-6-pro": 68.48, "kimi-k3-1-pro": 71.29},
    "aicd": {"claude-opus-5-5-medium": 56.95, "deepseek-v4-1-flash-1017": 52.24, "gemini-4-argon": 49.9, "gpt-5.6-luna-low": 30.51,
             "mimo-v2-6-pro": 47.56, "kimi-k3-1-pro": 54.63},
    "tbench-4": {},
}

BUGHUNT = {"luna": "GPT-6 Luna", "haiku": "Haiku 5.5", "mimo-flash": "MiMo-V2.6-Flash", "terra": "GPT-6.1 Terra", "sol": "GPT-6.1 Sol",
           "astra": "GPT-6 Astra", "opus": "Opus 5.5", "sonnet": "Sonnet 5.5", "carbon": "Gemini 4 Carbon",
           "deepseek-flash-1017": "DeepSeek V4.1 Flash 1017", "argon": "Gemini 4 Argon", "luna-5.6": "GPT-5.6 Luna",
           "kimi-k3.1-pro": "Kimi K3.1 Pro", "mimo-pro": "MiMo-V2.6-Pro", "minimax-flash": "MiniMax-M3.1-Flash"}
# E206: the owner's largest-sample current mean at the exact effort over every harness; a tie at the largest sample is
# broken only by a recorded selection reason (else the build stops).
BUGHUNT_SELECTION = {
    "deepseek-v4-1-flash-1017": ("DeepSeek V4.1 Flash 1017 (max effort, DeepSeek Harness) - mean of 7",
                                 "Two owner means of seven runs exist at max effort: DeepSeek Harness 42.7 and Claude Code 39.1. The "
                                 "DeepSeek Harness row is DeepSeek's own agent, matching the benchmark's native-CLI method (the "
                                 "2026-10-23 editor selection recorded in data/bug_hunt.json at f2a182a). Since commit 03d6127 "
                                 "(2026-10-27) the owner no longer features the Claude Code row; the DeepSeek Harness row stays featured."),
}
VALS = {"luna": "openai/gpt-6-luna", "haiku": "anthropic/claude-haiku-5-5", "mimo-flash": "xiaomi/mimo-v2.6-flash",
        "terra": "openai/gpt-6.1-terra", "sol": "openai/gpt-6.1-sol", "astra": "openai/gpt-6-astra",
        "opus": "anthropic/claude-opus-5-5", "sonnet": "anthropic/claude-sonnet-5-5", "carbon": "google/gemini-4-carbon",
        "deepseek-flash-1017": "deepseek/deepseek-v4.1-flash-1017", "argon": "google/gemini-4-argon", "luna-5.6": "openai/gpt-5.6-luna",
        "kimi-k3.1-pro": "kimi/kimi-k3.1-pro", "mimo-pro": "xiaomi/mimo-v2.6-pro", "minimax-flash": "minimax/MiniMax-M3.1-flash"}
LIVEBENCH = {"luna": "gpt-6-luna", "haiku": "claude-haiku-5.5", "mimo-flash": "mimo-v2.6-flash", "terra": "gpt-6.1-terra",
             "sol": "gpt-6.1-sol", "astra": "gpt-6-astra", "opus": "claude-opus-5.5", "sonnet": "claude-sonnet-5.5", "carbon": "gemini-4-carbon",
             "deepseek-flash-1017": "deepseek-v4.1-flash-1017", "argon": "gemini-4-argon", "luna-5.6": "gpt-5.6-luna",
             "kimi-k3.1-pro": "kimi-k3.1-pro", "mimo-pro": "mimo-v2.6-pro", "minimax-flash": "minimax-m3.1-flash"}
AICD = {"luna": "GPT-6-Luna", "haiku": "Haiku 5.5", "mimo-flash": "MiMo-V2.6 Flash", "terra": "GPT-6.1-Terra", "sol": "GPT-6.1-Sol",
        "astra": "GPT-6-Astra", "opus": "Opus 5.5", "sonnet": "Sonnet 5.5", "carbon": "Gemini 4 Carbon",
        "deepseek-flash-1017": "Deepseek-V4.1-Flash-1017", "argon": "Gemini 4 Argon", "luna-5.6": "GPT-5.6-Luna",
        "kimi-k3.1-pro": "Kimi K3.1 Pro", "mimo-pro": "MiMo-V2.6 Pro", "minimax-flash": "MiniMax M3.1-Flash"}
TBENCH = {"luna": "GPT-6 Luna", "haiku": "Haiku 5.5", "mimo-flash": "MiMo-V2.6-Flash", "terra": "GPT-6.1 Terra", "sol": "GPT-6.1 Sol",
          "astra": "GPT-6 Astra", "opus": "Opus 5.5", "sonnet": "Sonnet 5.5", "carbon": "Gemini 4 Carbon",
          "deepseek-flash-1017": "DeepSeek V4.1 Flash 1017", "argon": "Gemini 4 Argon", "luna-5.6": "GPT-5.6 Luna",
          "kimi-k3.1-pro": "Kimi K3.1 Pro", "mimo-pro": "MiMo-V2.6-Pro", "minimax-flash": "MiniMax-M3.1-Flash"}
AICD_EFFORT = {"Low": "low", "Medium": "medium", "High": "high", "Xhigh": "xhigh", "Max": "max"}

READ = {name: (HERE / path).read_text().strip() for name, path in {
    "bughunt": "bughunt/readAt.txt", "vibe-code": "vals/vibe-code.readAt.txt", "code-migration-v1-1": "vals/code-migration-v1-1.readAt.txt",
    "livebench": "livebench/readAt.txt", "aicd": "aicd/livewire.readAt.txt", "aicdPage": "aicd/leaderboard.readAt.txt"}.items()}
READ["tbench"] = json.loads((HERE / "tbench" / "tb4-rows-parsed-2026-11-01.json").read_text())["scrapedAt"]
BUGHUNT_COMMIT = next((HERE / "bughunt").glob("combined-*.csv")).stem.split("-", 1)[1]


def cell(status, value=None, label=None, effort=None, note=None, **extra):
    return {"status": status, "value": value, "sourceLabel": label, "effort": effort, "note": note, **extra}


def join_notes(*notes) -> str | None:
    text = " ".join(note for note in notes if note)
    return text or None


def base_note(model_id: str) -> str | None:
    return join_notes(FALLBACK_NOTE if model_id in FALLBACK else None, EFFORT_NOTE.get(model_id))


def near_note(rows: list[tuple[str, object]], what: str) -> str:
    return (f"Non-matching rows at other efforts: " + "; ".join(f"{label} = {value}" for label, value in rows) + "." if rows
            else f"No {what} row for this model at any effort.")


def previous_values(path: Path, key_field: str) -> dict:
    document = json.loads(path.read_text())
    return {board[key_field]: {model_id: c.get("value") for model_id, c in board["coverage"].items()} for board in document["benchmarks"]}


PREVIOUS_OTHER = previous_values(PREVIOUS / "coverage-2026-10-30.json", "key")
PREVIOUS_VALS = previous_values(PREVIOUS / "vals-catalogue-2026-10-30.json", "slug")


def annotate(board: dict, key: str, previous: dict) -> dict:
    """Adds the per-board change record against the 2026-10-30 read (the 27) and the 2026-10-25 release (the retained ten)."""
    old = previous.get(key, {})
    changed = {model_id: {"20261030": old[model_id], "20261101": c["value"]} for model_id, c in board["coverage"].items()
               if model_id in old and old[model_id] != c["value"]}
    reference = REFERENCE_20261025.get(key, {})
    retained = {}
    for model_id in sorted(RETAINED):
        c = board["coverage"][model_id]
        retained[model_id] = {"release20261025": reference.get(model_id), "20261101": c["value"], "status": c["status"],
                              "same": reference.get(model_id) == c["value"]}
    board["valueChangesSince20261030"] = changed
    board["retainedAgainst20261025Release"] = retained
    return board


def bughunt() -> dict:
    meta = json.loads((HERE / "bughunt" / "benchmark.json").read_text())
    runs = [run for run in meta["runs"] if not run.get("superseded")]
    board = {"key": "bug-hunt", "name": "Bug Hunt Bench", "updated": meta["meta"]["updated"], "readAt": READ["bughunt"],
             "sourceUrl": "https://bughunt.productcompass.pm/data/benchmark.json; https://github.com/phuryn/bug-hunt-bench/tree/"
                          f"{BUGHUNT_COMMIT}/results (combined-scoreboard.csv, run-notes.md)",
             "sourceCommit": BUGHUNT_COMMIT, "metric": "planted bugs fixed of 105 (owner-published mean where repeated runs exist)",
             "matching": "the board's current row (not superseded) for the same model and effort; the owner's largest-sample mean when "
                         "repeated runs exist (E206), a tie broken only by a recorded selection reason",
             "harness": "each model's native agentic CLI (named per row)", "coverage": {}}
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
        wanted = "enabled" if family == "mimo-pro" else effort
        hit = [run for run in rows if run["effort"] == wanted]
        if not hit:
            note = near_note([(run["id"], run["fixed"]) for run in rows], "Bug Hunt")
            if family == "minimax-flash":
                note += (" The owner's site data (benchmark.json) and the scoreboard and run notes at this commit name no MiniMax "
                         "model (O38 search; as at f2a182a, 'owner_result_missing').")
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
        note = base_note(model_id)
        if family == "mimo-pro":
            note = join_notes(O54, "Bug Hunt's first-party row asserts thinking.type=enabled on Xiaomi's API (effort token "
                                   "'enabled'), the documented single mode (E206). The OpenRouter 'default' rows (current: mean of 3, "
                                   "22.7) do not assert a reasoning state and stay unmatched, as at f2a182a.")
        if family == "argon":
            note = join_notes(note, "High is Gemini 4 Argon's ceiling. combined-scoreboard.csv also lists a single Gemini CLI run at "
                                    "high (33/105, a different harness; not in benchmark.json's current rows); the Antigravity CLI "
                                    "mean of 3 is the largest-sample mean (E206, E224).")
        alternates = [{"id": other["id"], "fixed": other["fixed"], "nRuns": other["n_runs"], "harness": other["harness"],
                       "featured": other.get("featured")} for other in hit if other is not run]
        extra = {"harness": run["harness"], "harnessVersion": run.get("harness_version"), "date": run["date"], "nRuns": run["n_runs"],
                 "featured": run.get("featured")}
        if alternates:
            extra["alternates"] = alternates
        if selection_reason:
            extra["selectionReason"] = selection_reason
        board["coverage"][model_id] = cell("exact", run["fixed"], run["id"], wanted, note, **extra)
    return annotate(board, "bug-hunt", PREVIOUS_OTHER)


def vals() -> dict:
    document = {"capturedAt": max(READ["vibe-code"], READ["code-migration-v1-1"]),
                "method": "As on 2026-10-25 and 2026-10-30: each board page read, its benchmarkViewUrl prop's hashed "
                          "/_astro/benchmark_view_*.json downloaded (vals/<slug>.json, URL in vals/<slug>.jsonUrl.txt); values from "
                          "tasks.overall.<model key>. Exact = same Vals model key (model version) and reasoning_effort/compute_effort "
                          "equal to AA's effort, or, where AA plots no effort, the documented or owner-stated equivalent (O66, O135, "
                          "O54/E252); plausible = AA plots no effort and Vals records none (MiMo-V2.6-Flash, O140); absent otherwise. "
                          "Vals model pages for MiMo-V2.6-Pro and MiniMax-M3.1-Flash in vals/_models/ (read "
                          + (HERE / "vals" / "_models" / "readAt.txt").read_text().strip() + ").",
                "cohortSource": "research/2026-11-01-recapture/cohort.json (37 configurations: 27 + 10 retained under O145)", "benchmarks": []}
    for slug, name, harness in (("vibe-code", "Vibe Code Bench v1.1", "OpenHands"), ("code-migration-v1-1", "Code Migration v1.1", "Pi agent harness")):
        source = json.loads((HERE / "vals" / f"{slug}.json").read_text())
        old = json.loads((PREVIOUS / "vals" / f"{slug}.json").read_text())["tasks"]["overall"]
        rows = source["tasks"]["overall"]
        board = {"slug": slug, "name": name, "version": "1.1", "updated": source["metadata"]["updated"], "models": len(rows),
                 "harness": harness + ", the same for every model row", "sourceUrl": f"https://www.vals.ai/benchmarks/{slug}",
                 "jsonUrl": (HERE / "vals" / f"{slug}.jsonUrl.txt").read_text().strip(),
                 "captureFile": f"research/2026-11-01-recapture/third-party/vals/{slug}.json", "readAt": READ[slug],
                 "changesSince20261030": {"added": sorted(set(rows) - set(old)), "removed": sorted(set(old) - set(rows)),
                                          "valueChanged": sorted(key for key in old if key in rows and
                                                                 (old[key]["accuracy"], old[key]["stderr"]) != (rows[key]["accuracy"], rows[key]["stderr"])),
                                          "fileIdentical": (HERE / "vals" / f"{slug}.json").read_bytes() == (PREVIOUS / "vals" / f"{slug}.json").read_bytes()},
                 "coverage": {}}
        for model_id, (family, effort) in COHORT.items():
            key = VALS[family]
            row = rows.get(key)
            row_effort = (row.get("reasoning_effort") or row.get("compute_effort")) if row else None
            if row is None:
                board["coverage"][model_id] = {"status": "absent", "value": None, "stderr": None, "valsKey": None, "effort": None,
                                               "note": f"No {key} row on this board."}
            elif family == "mimo-flash":
                board["coverage"][model_id] = {"status": "plausible", "value": row["accuracy"], "stderr": row["stderr"], "valsKey": key,
                                               "effort": row_effort, "harness": row.get("harness"),
                                               "note": O135 + " Vals records reasoning, reasoning_effort and compute_effort as null and its "
                                                       "MiMo-V2.6-Flash model page (read 2026-10-30) states no reasoning setting; it stays "
                                                       "unmatched under O140. New evidence for the owner: Vals' MiMo-V2.6-Pro model page "
                                                       "(vals/_models/xiaomi_mimo-v2.6-pro.html, read 2026-11-01), in its 2026-09-22 update "
                                                       "covering both models, says 'We evaluated them with reasoning enabled' through the "
                                                       "official Xiaomi API."}
            elif family == "mimo-pro":
                board["coverage"][model_id] = {"status": "exact", "value": row["accuracy"], "stderr": row["stderr"], "valsKey": key,
                                               "effort": "enabled (high, O54)", "harness": row.get("harness"), "match": "owner (O54, E252)",
                                               "note": O54 + " Vals records reasoning, reasoning_effort and compute_effort as null; its model "
                                                       "page (read 2026-11-01) says of MiMo V2.6 Pro and Flash 'We evaluated them with "
                                                       "reasoning enabled' through the official Xiaomi API (2026-09-22 update)."}
            elif row_effort == effort:
                note = base_note(model_id)
                if family == "minimax-flash":
                    note = join_notes(note, "Vals' model page (read 2026-11-01): run 'via the official MiniMax API at temperature 1, "
                                            "top_p 0.95, compute effort max'.")
                board["coverage"][model_id] = {"status": "exact", "value": row["accuracy"], "stderr": row["stderr"], "valsKey": key,
                                               "effort": effort, "harness": row.get("harness"), "note": note}
            else:
                board["coverage"][model_id] = {"status": "absent", "value": None, "stderr": None, "valsKey": None, "effort": None,
                                               "note": f"Vals ran this model only at {row_effort} ({row['accuracy']}), not {effort}; not transferred."}
        board["coverageCounts"] = {status: sum(1 for c in board["coverage"].values() if c["status"] == status) for status in ("exact", "plausible", "absent")}
        document["benchmarks"].append(annotate(board, slug, PREVIOUS_VALS))
    return document


def livebench_effort(site: str, label: str) -> str | None:
    match = re.search(r'"' + re.escape(label) + r'":\{[^}]*?effort:"(\w+)"', site)
    return match.group(1) if match else None


def livebench() -> dict:
    release = "20261025"
    table = {row["model"]: row for row in csv.DictReader((HERE / "livebench" / f"table-{release}.csv").open())}
    old_table = {row["model"]: row for row in csv.DictReader((PREVIOUS / "livebench" / f"table-{release}.csv").open())}
    categories = json.loads((HERE / "livebench" / f"categories-{release}.json").read_text())
    names = {"Long Agentic": "long_agentic", "Reasoning": "reasoning", "Coding": "coding", "Browser": "browser",
             "Data Analysis": "data_analysis", "Research": "research", "Design": "design"}
    weights = {column: float(categories["_overall_weights"].get(name, 1.0)) for name, column in names.items()}
    site = (HERE / "livebench" / "site-main.js").read_text()
    releases = re.search(r'=\["(20\d{6})"(?:,"(20\d{6})")*\]', site)
    release_list = re.findall(r'"(20\d{6})"', releases.group(0)) if releases else []
    if max(release_list) != release:
        raise ValueError(f"LiveBench lists a newer release than the pinned {release}: {release_list} (record it; do not switch, O139)")
    last_modified = re.search(r"last-modified: (.+)", (HERE / "livebench" / f"table-{release}.headers.txt").read_text(), re.I).group(1).strip()
    changed_cells = [{"model": model, "column": column, "20261030": old_table[model][column], "20261101": row[column]}
                     for model, row in table.items() if model in old_table for column in row if row[column] != old_table[model][column]]
    board = {"key": "livebench2-overall", "name": "LiveBench 2.0 Overall", "version": f"LiveBench 2.0 release {release}",
             "updated": f"2026-10-25 (site's displayed release date '25 October 2026'; release files' HTTP Last-Modified {last_modified})",
             "readAt": READ["livebench"], "sourceUrl": f"https://livebench.ai/data/{release}/table.csv",
             "pinnedReleaseStatus": f"Release {release} stays pinned under O139. On 2026-11-01 the site bundle (main.1e1ce12d.js) lists "
                                    f"releases {release_list}; no newer release exists (data/20261026 to data/20261101 return 404, "
                                    "livebench/newer-release-probe.txt). The release was edited in place after the 2026-10-30 read "
                                    "(files' Last-Modified moved from 22:01:11Z to 22:21:40Z on 2026-10-30): see releaseCellChangesSince20261030.",
             "releaseCellChangesSince20261030": changed_cells,
             "weights": weights, "harness": "LiveBench's own; one run per model at its highest supported effort (effort from the site bundle's model metadata)",
             "metric": "weighted mean of the seven category scores with the release's _overall_weights (as O67), 0-100", "coverage": {}}
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
        categories_ = {column: float(row[column]) for column in weights}
        overall = round(sum(weights[c] * v for c, v in categories_.items()) / sum(weights.values()), 2)
        wanted = "high" if family == "mimo-pro" else effort
        if row_effort == wanted:
            note = O54 if family == "mimo-pro" else base_note(model_id)
            if label in {change["model"] for change in changed_cells}:
                old_row = old_table[label]
                old_overall = round(sum(weights[c] * float(old_row[c]) for c in weights) / sum(weights.values()), 2)
                note = join_notes(note, f"Release {release} was edited in place after the 2026-10-30 read: "
                                        + "; ".join(f"{change['column']} {change['20261030']} -> {change['20261101']}"
                                                    for change in changed_cells if change["model"] == label)
                                        + f" (Overall {old_overall} -> {overall}).")
            board["coverage"][model_id] = cell("exact", overall, label, wanted, note, categories=categories_)
        else:
            board["coverage"][model_id] = cell("absent", note=f"LiveBench 2.0 has {label} at {row_effort} only (Overall {overall}); not transferred.")
    return annotate(board, "livebench2-overall", PREVIOUS_OTHER)


def aicd(bughunt_board: dict) -> dict:
    rows = json.loads((HERE / "aicd" / "leaderboard-allrows-parsed.json").read_text())
    old_rows = {(r["model"], r["harness"], r["tested"]): r for r in json.loads((PREVIOUS / "aicd" / "leaderboard-allrows-parsed.json").read_text())}
    new_keys = {(r["model"], r["harness"], r["tested"]) for r in rows}
    columns = ("total", "laravel", "react", "bug", "edge", "cost", "time")
    board = {"key": "aicd", "name": "AI Coding Daily LLM Coding Leaderboard", "version": "v2 scoring with Bug Finding",
             "readAt": READ["aicd"], "pageReadAt": READ["aicdPage"],
             "sourceUrl": "https://aicodingdaily.com/leaderboard (every row: Livewire POST to /livewire-71a08158/update with "
                          "hiddenOlderModelIds=[]; bestHarnessOnly false)",
             "rows": len(rows), "values": "total (max 70), nonBug = Laravel + React-TS + Edge-case (max 60, the ValueRank leaf), and each column",
             "rowChangesSince20261030": {
                 "added": sorted(f"{m} [{h}, {t}]" for (m, h, t) in new_keys - set(old_rows)),
                 "removed": sorted(f"{m} [{h}, {t}]" for (m, h, t) in set(old_rows) - new_keys),
                 "valueChanged": [{"row": f"{r['model']} [{r['harness']}, {r['tested']}]",
                                   "changes": {c: [old_rows[k][c], r[c]] for c in columns if old_rows[k][c] != r[c]}}
                                  for r in rows for k in [(r["model"], r["harness"], r["tested"])]
                                  if k in old_rows and any(old_rows[k][c] != r[c] for c in columns)]},
             "coverage": {}}
    for model_id, (family, effort) in COHORT.items():
        prefix = AICD[family] + " ("
        family_rows = [row for row in rows if row["model"].startswith(prefix)]
        wanted = "high" if family in ("mimo-flash", "mimo-pro") else effort
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
            entries.append({"total": float(row["total"]),
                            "nonBug": round(float(row["laravel"]) + float(row["react"]) + float(row["edge"]), 2),
                            "laravel": float(row["laravel"]), "react": float(row["react"]), "bug": bug, "edge": float(row["edge"]),
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
        elif family == "mimo-pro":
            note = O54 + " The board's only MiMo-V2.6-Pro row is labelled High."
        if entries[0]["bug"] is None:
            note = join_notes(note, f"Tested {entries[0]['tested']}, before the Bug Finding project was added (2026-10-03): the listed "
                                    f"total {entries[0]['total']} is out of 60 (Laravel + React-TS + Edge-case), so no /70 total or "
                                    "bug-finding score exists; the non-bug leaf is exact. Row is hidden by default as an older LLM.")
        extra = {"rows": entries}
        if selection:
            extra["selection"] = selection
        board["coverage"][model_id] = cell("exact", entries[0]["nonBug"], hit[0]["model"], wanted, note, **extra)
    return annotate(board, "aicd", PREVIOUS_OTHER)


def tbench() -> dict:
    parsed = json.loads((HERE / "tbench" / "tb4-rows-parsed-2026-11-01.json").read_text())
    scrape = json.loads((HERE / "tbench" / "tb4-scrape-2026-11-01.json").read_text())
    old_parsed = json.loads((PREVIOUS / "tbench" / "tb4-rows-parsed-2026-10-30.json").read_text())
    rendered = {(row[1], row[2]) for row in scrape["rows"][1:] if len(row) == 7}
    unchanged = parsed["rows"] == old_parsed["rows"] and parsed["leaderboardUpdatedAt"] == old_parsed["leaderboardUpdatedAt"]
    board = {"key": "tbench-4", "name": "Terminal-Bench 4.0 (tbench.ai)", "updated": parsed["leaderboardUpdatedAt"],
             "readAt": READ["tbench"], "sourceUrl": parsed["source"] + " (redirects to https://www.tbench.ai/)",
             "note": f"Reference only: ValueRank's Terminal-Bench leaf comes from AA. The rendered table shows {len(rendered)} rows (one per "
                     f"model, its best effort); the page's own embedded leaderboard payload holds {parsed['rowCount']} rows (status "
                     "'display'), including lower-effort rows the default view hides. "
                     + ("Payload rows and leaderboard updated_at identical to the 2026-10-30 read." if unchanged
                        else "Payload rows or updated_at changed since the 2026-10-30 read."),
             "coverage": {}}
    for model_id, (family, effort) in COHORT.items():
        rows = [row for row in parsed["rows"] if row["model"] == TBENCH[family]]
        wanted = "high" if family == "mimo-pro" else effort
        hit = [row for row in rows if row["effort"] == wanted]
        if hit:
            row = hit[0]
            label = f"{row['model']} ({row['effort']})"
            shown = (label, row["agent"]) in rendered
            board["coverage"][model_id] = cell("exact", row["accuracy"], label, wanted,
                                               ("" if shown else "In the page payload only, not in the default rendered table. ")
                                               + (FALLBACK_NOTE if model_id in FALLBACK else ""), agent=row["agent"], ci95=row["ci95"],
                                               date=row["date"], renderedInTable=shown)
        else:
            board["coverage"][model_id] = cell("absent", note=near_note([(f"{row['model']} ({row['effort']})", row["accuracy"]) for row in rows], "Terminal-Bench 4.0"))
    return annotate(board, "tbench-4", PREVIOUS_OTHER)


def later_rows(boards: list[dict]) -> str:
    return (f"No row on any board is dated after {CUTOFF} (the 2026-11-01 chart capture); the build stops on a Bug Hunt or AI Coding "
            f"Daily row dated after that day. Changes after the previous cutoff ({PREVIOUS_CUTOFF}) are listed in README.md: LiveBench "
            "release 20261025 was edited in place (files' Last-Modified 2026-10-30T22:21:40Z) and one AI Coding Daily row outside the "
            "cohort (Mistral Large 4 (High)) changed values.")


def main() -> None:
    bug = bughunt()
    boards = [bug, livebench(), aicd(bug), tbench()]
    other = {"capturedAt": max(READ[k] for k in ("bughunt", "livebench", "aicd", "tbench")),
             "readAt": {"bugHunt": READ["bughunt"], "liveBench": READ["livebench"], "aiCodingDaily": READ["aicd"],
                        "aiCodingDailyPage": READ["aicdPage"], "tbench": READ["tbench"]},
             "cutoff": CUTOFF,
             "cohort": "research/2026-11-01-recapture/cohort.json (37 configurations: 27 + 10 retained under O145)",
             "retained": sorted(RETAINED),
             "statusRule": "exact = source row names the same model version and the same reasoning effort as the AA configuration (where AA "
                           "plots no effort: the documented default under O66/O135, or the owner's O54 mapping for MiMo-V2.6-Pro); "
                           "plausible = same model, effort not confirmable (MiMo-V2.6-Flash rows that record no effort; O140 keeps them "
                           "unmatched); absent = no row at this effort. No value is transferred across efforts or versions.",
             "laterRowCheck": later_rows(boards),
             "benchmarks": boards}
    (HERE / "coverage-2026-11-01.json").write_text(json.dumps(other, indent=1, ensure_ascii=False) + "\n")
    (HERE / "vals-catalogue-2026-11-01.json").write_text(json.dumps(vals(), indent=1, ensure_ascii=False) + "\n")
    print("wrote coverage-2026-11-01.json and vals-catalogue-2026-11-01.json")


if __name__ == "__main__":
    main()
