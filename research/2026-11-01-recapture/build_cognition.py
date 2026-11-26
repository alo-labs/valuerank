"""O153 (2026-11-01): merge Cognition's FrontierCode 2.0 board and its exact-configuration map into data/.

Reads the first-party capture in third-party/cognition/ (data.json and the reviewed cohort mapping) and writes
data/cognition_frontiercode.json["v2_0"] (the board verbatim) and ["v2_0Map"] (cohort id -> Cognition model and effort,
exact matches only), and points leaf_evidence.json's cognitionCapture at the 2.0 artifact. Idempotent.
"""

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CAPTURE = ROOT / "research/2026-11-01-recapture/third-party/cognition"


def main() -> None:
    raw = (CAPTURE / "frontier-code-2.0-data.json").read_bytes()
    capture = json.loads((CAPTURE / "frontiercode-2.0-2026-11-01.json").read_text())
    exact = {item["configurationId"]: {"model": item["cognitionModel"], "effort": item["cognitionEffort"], "harness": item["cognitionHarness"],
                                       **({"caveat": item["caveat"]} if item.get("caveat") else {})}
             for item in capture["cohortMapping"]["configurations"] if item["status"] == "exact"}
    path = ROOT / "data/cognition_frontiercode.json"
    document = json.loads(path.read_text())
    document["v2_0"] = json.loads(raw)
    document["v2_0Map"] = dict(sorted(exact.items()))
    path.write_text(json.dumps(document, indent=1, ensure_ascii=False) + "\n")
    path = ROOT / "data/leaf_evidence.json"
    evidence = json.loads(path.read_text())
    evidence["cognitionCapture"] = {"url": "https://cognition.com/data/frontier-code-2.0/data.json", "lastModified": "2026-10-31T13:46:59Z",
                                    "capturedOn": capture["capturedAt"][:10], "sha256": hashlib.sha256(raw).hexdigest(),
                                    "file": "data/cognition_frontiercode.json", "artifact": "research/2026-11-01-recapture/third-party/cognition/frontier-code-2.0-data.json",
                                    "note": "O153: Cognition's FrontierCode 2.0 board gap-fills the leaf after AA's run (exact model and effort, v2_0Map) and feeds the AA-Cognition agreement diagnostic."}
    path.write_text(json.dumps(evidence, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"exact": len(exact)}))


if __name__ == "__main__":
    main()
