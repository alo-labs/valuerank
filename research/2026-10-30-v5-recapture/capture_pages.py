"""Capture the v5 cohort's AA model pages (O132) with valuerank.capture_aa's page reader, into this folder."""

import concurrent.futures
import json
import sys
from pathlib import Path

from valuerank.capture_aa import capture
from valuerank.clock import iso_z

COHORT = json.loads((Path(__file__).parent / "cohort.json").read_text())
pages = list(concurrent.futures.ThreadPoolExecutor(max_workers=4).map(lambda entry: capture(entry, {}), COHORT["configurations"]))
document = {"schemaVersion": "valuerank-aa-page-snapshot/v2", "benchmarkVersion": "Artificial Analysis Intelligence Index v5.0",
            "capturedAt": iso_z(), "source": "https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index",
            "concurrency": 4, "pages": pages}
Path(sys.argv[1]).write_text(json.dumps(document, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"pages": len(pages), "capturedAt": document["capturedAt"]}))
