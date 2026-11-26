"""Log the O36 exhaustive searches for the AA leaves GPT-5.6 Luna (low) lacks (owner decision O145 retains it; AA's v5 page
for it has no value), with the open-web step of gpt-5.6-luna-low-search.md.

    python3 research/2026-11-01-recapture/add_retained_searches.py
"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RECORD = "research/2026-11-01-recapture/gpt-5.6-luna-low-search.md"
AA_LEAVES = ("frontierCode", "terminalBench", "automationBench", "lcr", "tbScience", "hle", "critpt", "omniscience", "gdpval")
QUERIES = ['"GPT-5.6 Luna" FrontierCode 2.0 OR "HLE-Diamond" OR "Terminal-Bench-Science" OR "CritPt" low effort',
           '"GPT-5.6 Luna" Artificial Analysis Intelligence Index v5']
CANDIDATES = [
    {"candidate": "benchlm.ai, datalearner.com and lmmarketcap.com model and comparison pages for GPT-5.6 Luna", "resolution": "reject",
     "reason": "aggregators, not a registered source (E239); they report the max effort, not low, and earlier benchmark versions"},
    {"candidate": "artificialanalysis.ai pages for GPT-5.6 Luna's other efforts, comparisons and translated copies", "resolution": "reject",
     "reason": "other efforts or Intelligence Index v4.x views; the low configuration's own page has no v5 value"},
]
path = ROOT / "data" / "leaf_evidence.json"
document = json.loads(path.read_text())
document["searches"] = [item for item in document["searches"] if not (item["modelId"] == "gpt-5.6-luna-low" and item["leaf"] in AA_LEAVES)]
for leaf in AA_LEAVES:
    document["searches"].append({
        "modelId": "gpt-5.6-luna-low", "leaf": leaf, "searchedOn": "2026-11-01", "result": "not found", "searchKind": "O36 exhaustive search",
        "sources": ["https://artificialanalysis.ai/models/gpt-5-6-luna-low (model page captured 2026-11-01T05:57:26Z; no Intelligence Index v5 field)"],
        "notes": "Retained one release under owner decision O145; AA no longer plots GPT-5.6 Luna on the v5 chart and its page has no v5 value.",
        "openWeb": {"searchedOn": "2026-11-01", "record": RECORD, "queries": QUERIES, "candidates": CANDIDATES},
    })
path.write_text(json.dumps(document, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"added": len(AA_LEAVES), "searches": len(document["searches"])}))
