"""Update data/v3_configuration_map.json for the 2026-11-26 cohort: one row per cohort id, chart labels checked against the 2026-11-26
cost-chart capture (AA dropped " with fallback" from its Claude labels), and a Coding Agent Index pin only where several exact
records exist (the configuration's own vendor agent, O123).

    PYTHONPATH=. python3 research/2026-11-26-recapture/update_configuration_map.py
"""

import json
import re
from pathlib import Path

from valuerank import value_v3 as v

ROOT = Path(__file__).resolve().parents[2]
VENDOR_AGENT = {"OpenAI": "Codex", "Anthropic": "Claude Code", "Google": "Antigravity CLI", "Meta": "Muse Code"}


def main() -> None:
    path = ROOT / "data" / "v3_configuration_map.json"
    document = json.loads(path.read_text())
    charts = {item["slug"]: {row["model"] for row in item["rows"]} if "rows" in item else {row["model"] for row in item["models"]}
              for item in json.loads((ROOT / "data/aa/cost_charts_capture.json").read_text())["evaluations"]}
    agent_labels = [row["label"] for row in json.loads((ROOT / "data/aa/coding_agents_capture.json").read_text())["configurations"]]
    mapping = json.loads((ROOT / "data/aa_mapping.json").read_text())
    rows = document["rows"]
    cleared = list(document["unheldLabels"]["cleared"])
    for item in mapping:
        row = rows.setdefault(item["id"], {"coding-agent-index": None, "frontiercode": None, "itbench-aa": None})
        for chart in ("frontiercode", "itbench-aa"):
            label = row.get(chart)
            candidates = [label] if label else []
            candidates += [re.sub(r" with fallback\)$", ")", label)] if label else []
            candidates += [item["displayName"]]
            found = next((name for name in candidates if name in charts[chart]), None)
            if label and found != label:
                cleared.append({"id": item["id"], "chart": chart, "label": label, "reason": "2026-11-26: AA's chart no longer holds this label" + (f" (now {found!r})" if found else "")})
            row[chart] = found
        configuration = {"id": item["id"], "name": item["displayName"], "family": item["family"], "effort": item["aaVariant"]}
        exact = v.exact_agent_records(configuration, agent_labels)
        if len(exact) > 1:
            vendor = VENDOR_AGENT[next(d for prefix, d in (("GPT", "OpenAI"), ("Claude", "Anthropic"), ("Gemini", "Google"), ("Muse", "Meta")) if item["displayName"].startswith(prefix))]
            pin = [label for label in exact if label.startswith(vendor + " - ")]
            if len(pin) != 1:
                raise ValueError(f"{item['id']}: no unique vendor-agent record among {exact}")
            row["coding-agent-index"] = pin[0]
        else:
            row["coding-agent-index"] = None
    document["unheldLabels"]["cleared"] = cleared
    document["observedAt"] = "2026-11-26"
    path.write_text(json.dumps(document, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"rows": len(rows), "pins": {k: v["coding-agent-index"] for k, v in rows.items() if v["coding-agent-index"]}, "itbench": {k: v["itbench-aa"] for k, v in rows.items() if v["itbench-aa"] and k in {m["id"] for m in mapping}}}, indent=1))


if __name__ == "__main__":
    main()
