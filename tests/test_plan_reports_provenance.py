"""Provenance of data/plan_reports.json: every row is a transcription of the O71 plan-allowance record (review I65, L1).

The record is the stage-1 files, the stage-2 notes and report, the stage-3 report, evidence, sources and decision record,
and the earlier MiMo token-plan research. Each row's URL, observer and values must occur in that text; a value may appear
in the record's own formatting ("$1,266", "1266", "32,97", "$2k").
"""

from __future__ import annotations

import json
import re
from functools import lru_cache
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
TABLE = json.loads((ROOT / "data" / "plan_reports.json").read_text(encoding="utf-8"))
ROWS = TABLE["reports"]

STAGE1 = ROOT / "research" / "2026-10-25-plan-allowances"
STAGE3 = ROOT / "research" / "2026-10-25-plan-allowances-sb-deep-research"
MIMO = ROOT / "research" / "2026-10-23-mimo-token-plans"
ENTRANTS = ROOT / "research" / "2026-10-31-plan-allowances-v5-entrants"


def record_files() -> list[Path]:
    files = sorted(STAGE1.glob("stage1-*.md"))
    files += sorted((STAGE1 / "research_notes" / "Plan allowance user reports").glob("*.md"))
    files += [STAGE1 / "reports" / "Plan allowance user reports.md"]
    files += [STAGE3 / name for name in ("research_report.md", "evidence.jsonl", "sources.jsonl", "decision-record.md")]
    files += sorted(MIMO.rglob("*.md"))
    # Reviewer 74 M1 (E278): the 2026-10-31 search for the v5 entrants, all three stages.
    files += sorted(ENTRANTS.glob("stage1-*.md")) + [ENTRANTS / "stage2" / "report.md"] + sorted((ENTRANTS / "stage2" / "research_notes").glob("*.md"))
    files += [ENTRANTS / "stage3-sb-deep-research" / name for name in ("research_report.md", "evidence.jsonl", "sources.jsonl", "decision-record.md")]
    return files


@lru_cache(maxsize=1)
def record_text() -> str:
    parts = []
    for path in record_files():
        text = path.read_text(encoding="utf-8")
        parts.append(text)
        if path.suffix == ".jsonl":  # also the decoded form, in case a line escapes characters
            parts.extend(json.dumps(json.loads(line), ensure_ascii=False) for line in text.splitlines() if line.strip())
    return "\n".join(parts)


def spellings(value: float) -> set[str]:
    """The ways the record writes a dollar figure: plain, thousands-separated, two decimals, decimal comma, or $Nk."""

    out = {f"{value:g}", f"{value:,g}"}
    if value != int(value):
        out |= {f"{value:.2f}", f"{value:,.2f}", f"{value:.2f}".replace(".", ","), f"{value:g}".replace(".", ",")}
    else:
        out |= {f"{int(value)}", f"{int(value):,}"}
        if value >= 1000 and value % 100 == 0:
            out.add(f"{value / 1000:g}k")
    return out


def occurs(value: float, text: str) -> bool:
    for spelling in spellings(value):
        if re.search(rf"(?<![\d.,]){re.escape(spelling)}(?!\d|[.,]\d)", text):
            return True
    return False


def test_record_files_exist():
    missing = [str(path) for path in record_files() if not path.exists()]
    assert not missing and len(record_files()) > 15


@pytest.mark.parametrize("row", ROWS, ids=[row["id"] for row in ROWS])
def test_row_is_in_the_record(row):
    text = record_text()
    if row["url"] is not None:
        assert row["url"] in text, f"url not in the record: {row['url']}"
    assert row["observer"] in text, f"observer not in the record: {row['observer']}"
    for key in ("valueLower", "valueUpper"):
        assert occurs(row[key], text), f"{key} {row[key]} not in the record"
    assert row["valueLower"] <= row["valueUpper"]
    for path in row["source"]:
        assert (ROOT / path).exists(), path


@pytest.mark.parametrize("row", ROWS, ids=[row["id"] for row in ROWS])
def test_row_schema(row):
    assert row["stage"] in {"S1", "S2", "S3"}
    assert row["unit"] in {"5h", "week", "month"}
    assert row["reportDate"]
    if row["windowStated"]:
        assert row["windowStart"] and row["windowEnd"], "a stated window needs both dates"
    else:
        assert row["windowStart"] is None and row["windowEnd"] == row["reportDate"]
    if row.get("speedMode") is not None:
        assert row["speedMode"] in TABLE["speedModeMultipliers"].get(row["provider"], {})
    if row["modelId"] is None:
        assert row["modelUnstated"]


def test_ids_are_unique():
    ids = [row["id"] for row in ROWS]
    assert len(ids) == len(set(ids))


def test_not_tabulated_reports_are_in_the_record():
    text = record_text()
    for entry in TABLE["notTabulated"]:
        assert entry["observer"] in text, entry["observer"]
        assert entry["reason"]
        assert all((ROOT / path).exists() for path in entry["source"])
