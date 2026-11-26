"""Resolve overlapped chart circles by AA's own model ids (run before build_cohort.py).

A hover at a hidden circle's centre returns the tooltip of the circle drawn on top of it (two circles here: one at 1 px offset).
The circle's `data-chart-item-id` equals the `model.id` embedded in that model's page, so the hidden circle's model is read from
its page: the chart's rounded Index and two-decimal total cost are the page's `intelligenceIndex` rounded and
`intelligenceIndexCost.total` to cents, written in the tooltip's own layout and flagged `overlapResolution: model-page-id`.
A hidden circle whose model is not in the family pages searched stays 'unresolved' and is recorded (it is no cohort point
unless its tooltip's cost and Index put it on or within three points of the rendered frontier).

    python3 research/2026-11-26-recapture/resolve_overlaps.py
"""
from __future__ import annotations

import json
import re
import urllib.request
from pathlib import Path

from valuerank.capture_aa import capture

HERE = Path(__file__).parent
FAMILY_PAGES = ("gpt-6-luna", "claude-haiku-5-5", "deepseek-v4-1-flash-1017", "qwen4-max", "qwen3-8-max", "qwen3-8-27b", "gpt-6-2-sol", "gemini-4-neon", "claude-fable-5-2")


def fetch(url: str) -> str:
    with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"}), timeout=60) as response:
        return response.read().decode("utf-8", "replace").replace('\\"', '"')


def main() -> None:
    chart = json.loads((HERE / "chart-capture.json").read_text())
    todo = {h["id"]: h for h in chart["hovers"] if h.get("overlapResolution") == "unresolved"}
    found = {}
    for family in FAMILY_PAGES:
        if len(found) == len(todo):
            break
        try:
            page = fetch("https://artificialanalysis.ai/models/" + family)
        except Exception:
            continue
        for model_id in todo:
            if model_id in found:
                continue
            match = re.search(r'"id":"' + re.escape(model_id) + r'","slug":"([a-z0-9.\-]+)","name":"([^"]+)","shortName":"([^"]+)"', page)
            if match:
                found[model_id] = match.group(1)
    for model_id, slug in found.items():
        model = capture({"id": slug, "displayName": slug, "url": "https://artificialanalysis.ai/models/" + slug, "chartTier": "frontier"}, {})["model"]
        if model["id"] != model_id:
            raise ValueError(f"{slug} page model id {model['id']} is not the circle {model_id}")
        short, index, total = model["shortName"], model["intelligenceIndex"], model["intelligenceIndexCost"]["total"]
        hover = todo[model_id]
        hover["tooltip"] = f"{short}\nCost to Run Intelligence Index (USD, Log Scale)\n${total:,.2f}\nArtificial Analysis Intelligence Index\n{round(index)}\nClick for more info"
        hover["overlapResolution"] = "model-page-id"
        hover["resolvedFrom"] = f"https://artificialanalysis.ai/models/{slug}"
    for model_id in todo:
        if model_id not in found:
            todo[model_id]["resolvedFrom"] = None
            todo[model_id]["tooltip"] = "(overlapped circle, model not identified: not a cohort point)"
    (HERE / "chart-capture.json").write_text(json.dumps(chart, indent=1) + "\n")
    print(json.dumps({"resolved": found, "unresolved": [i for i in todo if i not in found]}, indent=1))


if __name__ == "__main__":
    main()
