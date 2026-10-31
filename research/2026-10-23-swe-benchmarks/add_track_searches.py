"""Log the O36 searches for the leaves the two rankings add (O53-O55) in data/leaf_evidence.json.

Every cohort configuration without an exact record for an added leaf gets one search entry per leaf, dated 2026-10-23.
The entry records the benchmark's own board as the primary source and the SWE benchmark research as its open-web step
(I28). A source row for the same model at another or an unstated effort is a candidate, rejected as not the exact
configuration. Entries this script wrote before are replaced; other entries are kept.

    python3 research/2026-10-23-swe-benchmarks/add_track_searches.py
"""

import json
from pathlib import Path

HERE = Path(__file__).parent
ROOT = HERE.parent.parent
SEARCHED = "2026-10-30"  # O68: every added-leaf board re-read in full on 2026-10-25; O132: again on 2026-10-30 (v5 cohort)
READ = HERE.parent / "2026-10-30-v5-recapture" / "third-party"
MARK = "O53 track leaf search"
RESEARCH = [
    "Claude deep research, three researchers: research/2026-10-23-swe-benchmarks/research_notes/SWE benchmark candidates/ (owner-named sources, Vals AI, other agentic benchmarks)",
    "Perplexity Search with Thinking on research/2026-10-23-swe-benchmarks/brief.md: GPT-6.1 Sol, Grok 4.7, Gemini 3.8 Flash (pplx-*.md)",
    "Coverage capture of every cohort configuration: research/2026-10-23-swe-benchmarks/vals-catalogue-2026-10-23.json and other-coverage-2026-10-23.json (raw pages and JSON in vals-capture/ and other-capture/)",
    "Check of Epoch MirrorCode, SWE-bench-Live and SWE-PolyBench (report addendum)",
    "Board re-read of 2026-10-25 (owner decision O68): research/2026-10-25-board-reread/ (Vals, AI Coding Daily with hidden rows, Bug Hunt at 9089dc5, LiveBench 2.0 release 2026-10-23)",
    "Kimi K3.1 Pro exhaustive search with open-web queries, 2026-10-25: research/2026-10-25-board-reread/kimi-search.md and kimi-search.json",
    "Board re-read of 2026-10-30 for the AA Intelligence Index v5 cohort (O132): research/2026-10-30-v5-recapture/third-party/ (Bug Hunt at 1249797, Vals, LiveBench 2.0 release 2026-10-25 (O139), AI Coding Daily with hidden rows, tbench.ai), with Xiaomi's MiMo-V2.6-Flash effort documentation (O140)",
]
LEAVES = {
    "bugHunt": ("other", "bug-hunt", "https://bughunt.productcompass.pm/data/benchmark.json and the owner's results at commit 12497971 (updated 2026-10-27, read 2026-10-30)"),
    "vibeCode": ("vals", "vibe-code", "https://www.vals.ai/benchmarks/vibe-code (benchmark_view JSON, updated 2026-10-29, read 2026-10-30)"),
    "codeMigration": ("vals", "code-migration-v1-1", "https://www.vals.ai/benchmarks/code-migration-v1-1 (benchmark_view JSON, updated 2026-10-28, read 2026-10-30)"),
    # O61: LiveBench 2.0 Overall replaces the Long Agentic and Coding categories; one LiveBench row per model, so its
    # coverage is the coding capture's.
    "livebench2Overall": ("other", "livebench2-overall", "https://livebench.ai/data/20261025/table.csv and the site bundle's model metadata (release 2026-10-25, read 2026-10-30; O67, O139)"),
    "aiCodingDaily": ("other", "aicd", "https://aicodingdaily.com/leaderboard, every row including hidden older models (updated 2026-10-27, read 2026-10-30)"),
}


def own_search(model_id: str) -> dict | None:
    """I58 L6: a configuration searched on its own logs its own queries and rejected candidates (E240)."""

    path = HERE.parent / "2026-10-25-board-reread" / "kimi-search.json"
    if model_id != "kimi-k3-1-pro" or not path.exists():
        return None
    search = json.loads(path.read_text())
    return {"searchedOn": SEARCHED, "record": "research/2026-10-25-board-reread/kimi-search.md",
            "queries": [item["query"] for item in search.get("openWeb", [])],
            "candidates": [{"url": candidate.get("url"), "resolution": "reject", "reason": candidate.get("reason") or candidate.get("verdict")}
                           for item in search.get("openWeb", []) for candidate in item.get("candidates", [])]}


def main() -> None:
    vals = {item["slug"]: item for item in json.loads((READ / "vals-catalogue-2026-10-30.json").read_text())["benchmarks"]}
    other = {item["key"]: item for item in json.loads((READ / "coverage-2026-10-30.json").read_text())["benchmarks"]}
    cohort = [row["id"] for row in json.loads((HERE.parent / "2026-10-30-v5-recapture" / "cohort.json").read_text())["configurations"]]
    records = {(record["modelId"], record["leaf"]) for record in json.loads((ROOT / "data" / "swe_tracks.json").read_text())["records"]}
    # O132: the Bug Hunt leaf's records are data/bug_hunt.json's matched rows.
    records |= {(model["modelId"], "bugHunt") for model in json.loads((ROOT / "data" / "bug_hunt.json").read_text())["models"] if model.get("matched")}
    path = ROOT / "data" / "leaf_evidence.json"
    evidence = json.loads(path.read_text())
    # O132: the v5 cohort's searches replace every earlier one (all were older than the 7-day window of the new cutoff).
    searches = []
    for leaf, (origin, key, board) in LEAVES.items():
        coverage = (vals if origin == "vals" else other)[key]["coverage"]
        for model_id in cohort:
            if (model_id, leaf) in records:
                continue
            cell = coverage[model_id]
            candidates = []
            if cell["status"] == "plausible":
                candidates.append({
                    "url": board.split(" ")[0], "publisher": board.split("/")[2], "published": SEARCHED,
                    "reports": f"{cell.get('sourceLabel') or cell.get('valsKey')}: {cell['value']} at effort {cell.get('effort') or 'not stated'}",
                    "resolution": "reject", "reason": "not the exact configuration: AA plots this model without an effort label and the source's effort is not established as AA's",
                })
            searches.append({
                "modelId": model_id, "leaf": leaf, "searchedOn": SEARCHED, "result": "not found", "searchKind": MARK,
                "sources": [board],
                "notes": cell.get("note") or f"No {leaf} record for this configuration at its exact effort.",
                "openWeb": own_search(model_id) or {"searchedOn": SEARCHED, "record": "research/2026-10-23-swe-benchmarks/reports/SWE benchmark candidates.md",
                                                     "queries": RESEARCH, "candidates": candidates},
            })
    evidence["searches"] = searches
    path.write_text(json.dumps(evidence, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"searches": len(searches), "trackSearches": sum(1 for entry in searches if entry.get("searchKind") == MARK)}))


if __name__ == "__main__":
    main()
