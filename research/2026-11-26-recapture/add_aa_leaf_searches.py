"""Log the O36/O38 exhaustive searches for the AA leaves AA's model page no longer carries for a cohort configuration (2026-11-26).

    PYTHONPATH=. python3 research/2026-11-26-recapture/add_aa_leaf_searches.py

One entry per (configuration, leaf) whose AA page field is missing, replacing earlier entries for the same pair; other entries stay.
The open-web step is aa-leaf-search.md (queries and rejected candidates).
"""

import json
from pathlib import Path

from valuerank import value_v3 as v

ROOT = Path(__file__).resolve().parents[2]
RECORD = "research/2026-11-26-recapture/aa-leaf-search.md"
SEARCHED = "2026-11-26"
FIELDS = {**v.FRACTION_LEAVES, "gdpval": "gdpval", "omniscience": "omniscience", "terminalBench": "terminalBench41"}
QUERIES = ['"GPT-6.2 Sol" GDPval-AA Artificial Analysis', '"Gemini 4 Neon" GDPval-AA OR "AA-LCR" Artificial Analysis',
           '"Muse Ember" GDPval-AA OR "AA-LCR" long context reasoning score', '"GPT-6.2 Astra" "AA-LCR" OR GDPval Artificial Analysis Intelligence Index']
CANDIDATES = [
    {"candidate": "artificialanalysis.ai model pages and Intelligence Index v5.0.x descriptions for the model", "resolution": "reject",
     "reason": "the current Index has nine evaluations and runs GDP.pdf, not GDPval-AA or AA-LCR; the page carries no value for this leaf"},
    {"candidate": "GDPval-AA and AA-LCR figures on pages of other models (GPT-6 Sol, Gemini 4 Argon)", "resolution": "reject",
     "reason": "other models; no value moves across models (O36)"},
    {"candidate": "Meta's Muse Ember evaluation report (research.meta.ai)", "resolution": "reject", "reason": "the provider's own document with neither score"},
]


def main() -> None:
    snapshot = {page["id"]: page["model"] for page in json.loads((ROOT / "data/aa/aa_v432_snapshot.json").read_text())["pages"]}
    path = ROOT / "data" / "leaf_evidence.json"
    document = json.loads(path.read_text())
    added = []
    for model_id, page in snapshot.items():
        for leaf, field in FIELDS.items():
            if leaf in ("omniscience", "terminalBench") or page.get(field) is not None:
                continue
            added.append({
                "modelId": model_id, "leaf": leaf, "searchedOn": SEARCHED, "result": "not found", "searchKind": "O36 exhaustive search",
                "sources": [f"https://artificialanalysis.ai/models/{page['slug']} (model page captured 2026-11-26; no `{field}` value)"],
                "notes": "AA's Intelligence Index v5.0.2 no longer runs this evaluation; its page carries it only for models evaluated before the change.",
                "openWeb": {"searchedOn": SEARCHED, "record": RECORD, "queries": QUERIES, "candidates": CANDIDATES},
            })
    pairs = {(item["modelId"], item["leaf"]) for item in added}
    document["searches"] = [item for item in document.get("searches", []) if (item["modelId"], item["leaf"]) not in pairs] + added
    path.write_text(json.dumps(document, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"added": len(added), "searches": len(document["searches"])}))


if __name__ == "__main__":
    main()
