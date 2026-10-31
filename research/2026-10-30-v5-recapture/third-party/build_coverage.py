"""Third-party board coverage for the AA Intelligence Index v5 cohort (owner decisions O132, O135), read 2026-10-30.

Re-reads, with the 2026-10-25 methods (research/2026-10-25-board-reread/), every board an added leaf uses: Bug Hunt Bench,
Vals Vibe Code Bench v1.1 and Code Migration v1.1, LiveBench 2.0, AI Coding Daily (every row, hidden older rows included)
and the tbench.ai Terminal-Bench 4.0 leaderboard. Matching is exact configuration only (O36): the source row must name the
same model version and the same reasoning effort as the AA configuration; no value moves across efforts or versions.
MiMo-V2.6-Flash, which AA plots without an effort, is taken at Xiaomi's documented default (O135, mimo-flash-effort.md).

    python3 -I research/2026-10-30-v5-recapture/third-party/build_coverage.py

Writes coverage-2026-10-30.json (other boards) and vals-catalogue-2026-10-30.json (Vals) next to this file.
"""

from __future__ import annotations

import csv
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
CUTOFF = "2026-10-30T22:15:18Z"  # the v5 chart capture instant (../notes.md)
O135 = ("Owner decision O135 (2026-10-30): AA plots MiMo-V2.6-Flash without an effort; Xiaomi's API documents a single "
        "thinking mode (thinking.type enabled/disabled, default enabled; on the Responses API every reasoning.effort other "
        "than none enables the same, undifferentiated reasoning), so the configuration is thinking enabled, the default "
        "(mimo-flash-effort.md).")

# id: (family, effort). Effort None = AA plots no effort (MiMo-V2.6-Flash; O135 takes the documented default).
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
}
FALLBACK = {"claude-opus-5-5-high", "claude-opus-5-5-xhigh", "claude-opus-5-5", "claude-sonnet-5-5"}
FALLBACK_NOTE = "AA labels this configuration '... with default fallback'; the source has no fallback qualifier (as on 2026-10-25)."

BUGHUNT = {"luna": "GPT-6 Luna", "haiku": "Haiku 5.5", "mimo-flash": "MiMo-V2.6-Flash", "terra": "GPT-6.1 Terra", "sol": "GPT-6.1 Sol",
           "astra": "GPT-6 Astra", "opus": "Opus 5.5", "sonnet": "Sonnet 5.5", "carbon": "Gemini 4 Carbon"}
VALS = {"luna": "openai/gpt-6-luna", "haiku": "anthropic/claude-haiku-5-5", "mimo-flash": "xiaomi/mimo-v2.6-flash",
        "terra": "openai/gpt-6.1-terra", "sol": "openai/gpt-6.1-sol", "astra": "openai/gpt-6-astra",
        "opus": "anthropic/claude-opus-5-5", "sonnet": "anthropic/claude-sonnet-5-5", "carbon": "google/gemini-4-carbon"}
LIVEBENCH = {"luna": "gpt-6-luna", "haiku": "claude-haiku-5.5", "mimo-flash": "mimo-v2.6-flash", "terra": "gpt-6.1-terra",
             "sol": "gpt-6.1-sol", "astra": "gpt-6-astra", "opus": "claude-opus-5.5", "sonnet": "claude-sonnet-5.5", "carbon": "gemini-4-carbon"}
AICD = {"luna": "GPT-6-Luna", "haiku": "Haiku 5.5", "mimo-flash": "MiMo-V2.6 Flash", "terra": "GPT-6.1-Terra", "sol": "GPT-6.1-Sol",
        "astra": "GPT-6-Astra", "opus": "Opus 5.5", "sonnet": "Sonnet 5.5", "carbon": "Gemini 4 Carbon"}
TBENCH = {"luna": "GPT-6 Luna", "haiku": "Haiku 5.5", "mimo-flash": "MiMo-V2.6-Flash", "terra": "GPT-6.1 Terra", "sol": "GPT-6.1 Sol",
          "astra": "GPT-6 Astra", "opus": "Opus 5.5", "sonnet": "Sonnet 5.5", "carbon": "Gemini 4 Carbon"}
AICD_EFFORT = {"Low": "low", "Medium": "medium", "High": "high", "Xhigh": "xhigh", "Max": "max"}

READ = {name: (HERE / path).read_text().strip() for name, path in {
    "bughunt": "bughunt/readAt.txt", "vibe-code": "vals/vibe-code.readAt.txt", "code-migration-v1-1": "vals/code-migration-v1-1.readAt.txt",
    "livebench": "livebench/readAt.txt", "aicd": "aicd/livewire.readAt.txt", "aicdPage": "aicd/leaderboard.readAt.txt"}.items()}
READ["tbench"] = json.loads((HERE / "tbench" / "tb4-rows-parsed-2026-10-30.json").read_text())["scrapedAt"]
BUGHUNT_COMMIT = next((HERE / "bughunt").glob("combined-*.csv")).stem.split("-", 1)[1]


def cell(status, value=None, label=None, effort=None, note=None, **extra):
    return {"status": status, "value": value, "sourceLabel": label, "effort": effort, "note": note, **extra}


def near_note(rows: list[tuple[str, object]], what: str) -> str:
    return (f"Non-matching rows at other efforts: " + "; ".join(f"{label} = {value}" for label, value in rows) + "." if rows
            else f"No {what} row for this model at any effort.")


def bughunt() -> dict:
    meta = json.loads((HERE / "bughunt" / "benchmark.json").read_text())
    runs = [run for run in meta["runs"] if not run.get("superseded")]
    board = {"key": "bug-hunt", "name": "Bug Hunt Bench", "updated": meta["meta"]["updated"], "readAt": READ["bughunt"],
             "sourceUrl": "https://bughunt.productcompass.pm/data/benchmark.json; https://github.com/phuryn/bug-hunt-bench/tree/"
                          f"{BUGHUNT_COMMIT}/results (combined-scoreboard.csv, run-notes.md)",
             "sourceCommit": BUGHUNT_COMMIT, "metric": "planted bugs fixed of 105 (owner-published mean where repeated runs exist)",
             "matching": "the board's current row (not superseded) for the same model and effort; the owner's mean when repeated runs exist",
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
                    "rather than known-inert', run notes). Whether this route's default equals Xiaomi's documented default "
                    "(thinking enabled) is not shown by the board: owner to confirm before it counts as exact.",
                    harness=run["harness"], harnessVersion=run.get("harness_version"), date=run["date"], nRuns=run["n_runs"],
                    routeModelId=run.get("model_id"))
            else:
                board["coverage"][model_id] = cell("absent", note="No MiMo-V2.6-Flash row.")
            continue
        hit = [run for run in rows if run["effort"] == effort]
        if len(hit) > 1:
            raise ValueError(f"{model_id}: {len(hit)} current Bug Hunt rows")
        if hit:
            run = hit[0]
            note = FALLBACK_NOTE if model_id in FALLBACK else None
            if run["date"] > CUTOFF[:10]:
                raise ValueError(f"{model_id}: Bug Hunt row dated after the capture day")
            board["coverage"][model_id] = cell("exact", run["fixed"], run["id"], effort, note, harness=run["harness"],
                                               harnessVersion=run.get("harness_version"), date=run["date"], nRuns=run["n_runs"],
                                               featured=run.get("featured"))
        else:
            board["coverage"][model_id] = cell("absent", note=near_note([(run["id"], run["fixed"]) for run in rows], "Bug Hunt"))
    return board


def vals() -> dict:
    document = {"capturedAt": max(READ["vibe-code"], READ["code-migration-v1-1"]),
                "method": "As on 2026-10-25: each board page read, its benchmarkViewUrl prop's hashed /_astro/benchmark_view_*.json "
                          "downloaded (vals/<slug>.json, URL in vals/<slug>.jsonUrl.txt); values from tasks.overall.<model key>. "
                          "Exact = same Vals model key (model version) and reasoning_effort/compute_effort equal to AA's effort; "
                          "plausible = AA plots no effort and Vals records none; absent otherwise. Vals model pages for "
                          "MiMo-V2.6-Flash, GPT-6.1 Terra and Gemini 4 Carbon in vals/_models/ (read "
                          + (HERE / "vals" / "_models" / "readAt.txt").read_text().strip() + ").",
                "cohortSource": "research/2026-10-30-v5-recapture/cohort.json (27 configurations)", "benchmarks": []}
    for slug, name, harness in (("vibe-code", "Vibe Code Bench v1.1", "OpenHands"), ("code-migration-v1-1", "Code Migration v1.1", "Pi agent harness")):
        source = json.loads((HERE / "vals" / f"{slug}.json").read_text())
        old = json.loads((HERE.parents[1] / "2026-10-25-board-reread" / "vals" / f"{slug}.json").read_text())["tasks"]["overall"]
        rows = source["tasks"]["overall"]
        board = {"slug": slug, "name": name, "version": "1.1", "updated": source["metadata"]["updated"], "models": len(rows),
                 "harness": harness + ", the same for every model row", "sourceUrl": f"https://www.vals.ai/benchmarks/{slug}",
                 "jsonUrl": (HERE / "vals" / f"{slug}.jsonUrl.txt").read_text().strip(),
                 "captureFile": f"research/2026-10-30-v5-recapture/third-party/vals/{slug}.json", "readAt": READ[slug],
                 "changesSince20261025": {"added": sorted(set(rows) - set(old)), "removed": sorted(set(old) - set(rows)),
                                          "valueChanged": sorted(key for key in old if key in rows and
                                                                 (old[key]["accuracy"], old[key]["stderr"]) != (rows[key]["accuracy"], rows[key]["stderr"]))},
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
                                                       "model page (read 2026-10-30) states no reasoning setting; Xiaomi's API has thinking "
                                                       "on by default, so a run that set nothing ran thinking enabled only if Vals did not "
                                                       "disable it: owner to confirm (as 2026-10-25: plausible)."}
            elif row_effort == effort:
                board["coverage"][model_id] = {"status": "exact", "value": row["accuracy"], "stderr": row["stderr"], "valsKey": key,
                                               "effort": effort, "harness": row.get("harness"),
                                               "note": FALLBACK_NOTE if model_id in FALLBACK else None}
            else:
                board["coverage"][model_id] = {"status": "absent", "value": None, "stderr": None, "valsKey": None, "effort": None,
                                               "note": f"Vals ran this model only at {row_effort} ({row['accuracy']}), not {effort}; not transferred."}
        board["coverageCounts"] = {status: sum(1 for c in board["coverage"].values() if c["status"] == status) for status in ("exact", "plausible", "absent")}
        document["benchmarks"].append(board)
    return document


def livebench_effort(site: str, label: str) -> str | None:
    import re
    match = re.search(r'"' + re.escape(label) + r'":\{[^}]*?effort:"(\w+)"', site)
    return match.group(1) if match else None


def livebench() -> dict:
    release = "20261025"
    table = {row["model"]: row for row in csv.DictReader((HERE / "livebench" / f"table-{release}.csv").open())}
    categories = json.loads((HERE / "livebench" / f"categories-{release}.json").read_text())
    names = {"Long Agentic": "long_agentic", "Reasoning": "reasoning", "Coding": "coding", "Browser": "browser",
             "Data Analysis": "data_analysis", "Research": "research", "Design": "design"}
    weights = {column: float(categories["_overall_weights"].get(name, 1.0)) for name, column in names.items()}
    site = (HERE / "livebench" / "site-main.js").read_text()
    board = {"key": "livebench2-overall", "name": "LiveBench 2.0 Overall", "version": f"LiveBench 2.0 release {release}",
             "updated": "2026-10-25 (site's displayed release date '25 October 2026'; release files' HTTP Last-Modified 2026-10-30T22:01:11Z)",
             "readAt": READ["livebench"], "sourceUrl": f"https://livebench.ai/data/{release}/table.csv",
             "pinnedReleaseStatus": "The 2026-10-25 read pinned release 20261023 (O67). On 2026-10-30 the site bundle lists releases "
                                    "['20261014', '20261025'] (no /new-only release) and every https://livebench.ai/data/20261023/ file "
                                    "returns HTTP 404 (livebench/release-20261023-404/). 20261025 is the newer release that replaces it: "
                                    "its table equals 20261023's for every shared model except three Nemotron browser cells, adds "
                                    "gpt-6.1-terra and mistral-large-4-0, and drops beam-1.0.",
             "weights": weights, "harness": "LiveBench's own; one run per model at its highest supported effort (effort from the site bundle's model metadata)",
             "metric": "weighted mean of the seven category scores with the release's _overall_weights (as O67), 0-100", "coverage": {}}
    for model_id, (family, effort) in COHORT.items():
        label = LIVEBENCH[family]
        row = table.get(label)
        if row is None:
            board["coverage"][model_id] = cell("absent", note=f"No {label} row in release {release} (nor in the site's model metadata).")
            continue
        row_effort = livebench_effort(site, label)
        categories_ = {column: float(row[column]) for column in weights}
        overall = round(sum(weights[c] * v for c, v in categories_.items()) / sum(weights.values()), 2)
        if row_effort == effort:
            board["coverage"][model_id] = cell("exact", overall, label, effort, FALLBACK_NOTE if model_id in FALLBACK else None,
                                               categories=categories_)
        else:
            board["coverage"][model_id] = cell("absent", note=f"LiveBench 2.0 has {label} at {row_effort} only (Overall {overall}); not transferred.")
    return board


def aicd() -> dict:
    rows = json.loads((HERE / "aicd" / "leaderboard-allrows-parsed.json").read_text())
    board = {"key": "aicd", "name": "AI Coding Daily LLM Coding Leaderboard", "version": "v2 scoring with Bug Finding",
             "readAt": READ["aicd"], "pageReadAt": READ["aicdPage"],
             "sourceUrl": "https://aicodingdaily.com/leaderboard (every row: Livewire POST to /livewire-71a08158/update with "
                          "hiddenOlderModelIds=[]; bestHarnessOnly false)",
             "rows": len(rows), "values": "total (max 70), nonBug = Laravel + React-TS + Edge-case (max 60, the ValueRank leaf), and each column",
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
            entries.append({"total": float(row["total"]),
                            "nonBug": round(float(row["laravel"]) + float(row["react"]) + float(row["edge"]), 2),
                            "laravel": float(row["laravel"]), "react": float(row["react"]), "bug": float(row["bug"]), "edge": float(row["edge"]),
                            "harness": row["harness"], "tested": row["tested"], "ageText": row["age"], "cost": row["cost"],
                            "time": row["time"], "rank": row["rank"]})
        note = FALLBACK_NOTE if model_id in FALLBACK else None
        if family == "mimo-flash":
            note = (O135 + " The board's only MiMo-V2.6-Flash row is labelled High; Xiaomi documents every enabled level as the same "
                    "reasoning ('Values xhigh, max and ultra are mapped to high'), so the High row is the documented default "
                    "configuration (thinking enabled). The row does not name the provider route behind OpenCode.")
        board["coverage"][model_id] = cell("exact", entries[0]["nonBug"], hit[0]["model"], wanted, note, rows=entries)
    return board


def tbench() -> dict:
    parsed = json.loads((HERE / "tbench" / "tb4-rows-parsed-2026-10-30.json").read_text())
    scrape = json.loads((HERE / "tbench" / "tb4-scrape-2026-10-30.json").read_text())
    rendered = {(row[1], row[2]) for row in scrape["rows"][1:] if len(row) == 7}
    board = {"key": "tbench-4", "name": "Terminal-Bench 4.0 (tbench.ai)", "updated": parsed["leaderboardUpdatedAt"],
             "readAt": READ["tbench"], "sourceUrl": parsed["source"] + " (redirects to https://www.tbench.ai/)",
             "note": "Reference only: ValueRank's Terminal-Bench leaf comes from AA. The rendered table shows 23 rows (one per model, "
                     "its best effort); the page's own embedded leaderboard payload holds 35 rows (status 'display'), including "
                     "lower-effort rows the default view hides. Leaderboard updated_at unchanged since the 2026-10-25 read.",
             "coverage": {}}
    for model_id, (family, effort) in COHORT.items():
        rows = [row for row in parsed["rows"] if row["model"] == TBENCH[family]]
        hit = [row for row in rows if row["effort"] == effort]
        if hit:
            row = hit[0]
            label = f"{row['model']} ({row['effort']})"
            shown = (label, row["agent"]) in rendered
            board["coverage"][model_id] = cell("exact", row["accuracy"], label, effort,
                                               ("" if shown else "In the page payload only, not in the default rendered table. ")
                                               + (FALLBACK_NOTE if model_id in FALLBACK else ""), agent=row["agent"], ci95=row["ci95"],
                                               date=row["date"], renderedInTable=shown)
        else:
            board["coverage"][model_id] = cell("absent", note=near_note([(f"{row['model']} ({row['effort']})", row["accuracy"]) for row in rows], "Terminal-Bench 4.0"))
    return board


def main() -> None:
    other = {"capturedAt": max(READ[k] for k in ("bughunt", "livebench", "aicd", "tbench")),
             "readAt": {"bugHunt": READ["bughunt"], "liveBench": READ["livebench"], "aiCodingDaily": READ["aicd"],
                        "aiCodingDailyPage": READ["aicdPage"], "tbench": READ["tbench"]},
             "cohort": "research/2026-10-30-v5-recapture/cohort.json (27 configurations)",
             "statusRule": "exact = source row names the same model version and the same reasoning effort as the AA configuration; "
                           "plausible = same model, effort not confirmable (MiMo-V2.6-Flash rows that record no effort; O135 owner check); "
                           "absent = no row at this effort. No value is transferred across efforts or versions.",
             "laterRowCheck": f"No row on any board is dated after {CUTOFF} (the v5 chart capture). Rows dated after the old cutoff "
                              "(2026-10-25) are listed in README.md.",
             "benchmarks": [bughunt(), livebench(), aicd(), tbench()]}
    (HERE / "coverage-2026-10-30.json").write_text(json.dumps(other, indent=1, ensure_ascii=False) + "\n")
    (HERE / "vals-catalogue-2026-10-30.json").write_text(json.dumps(vals(), indent=1, ensure_ascii=False) + "\n")
    print("wrote coverage-2026-10-30.json and vals-catalogue-2026-10-30.json")


if __name__ == "__main__":
    main()
