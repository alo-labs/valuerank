"""Behavior tests for the Terminal-Bench 4.0 normalisation stage (valuerank.build_tb4).

The stage reads a rendered leaderboard capture plus the AA cohort map and the
provider-claims file. These tests use the hand-written synthetic copies under
``tests/fixtures/external/tb4``; the real capture (data/tb4-scrape.json) is a
gitignored local file and is never required here.
"""

from __future__ import annotations

import hashlib
import json
import re
import runpy
import shutil
import sys
from pathlib import Path

import pytest

import valuerank.paths as paths
from valuerank import build_tb4
from valuerank.paths import ROOT

FIXTURES = Path(__file__).parent / "fixtures" / "external" / "tb4"


@pytest.fixture
def data_dir(tmp_path, pinned_clock) -> Path:
    """A temporary data directory holding the synthetic AA map and provider claims."""

    data = tmp_path / "data"
    data.mkdir()
    for name in ("aa_metrics.json", "provider_claims.json"):
        shutil.copy2(FIXTURES / name, data / name)
    return data


def synthetic_scrape() -> dict:
    return json.loads((FIXTURES / "scrape.json").read_text(encoding="utf-8"))


def write_json(path: Path, document: dict) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(document), encoding="utf-8")
    return path


def read_document(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


# ---------------------------------------------------------------------------
# parse_rate(): "58.2% ± 2.8%" -> (fraction, uncertainty in points)
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    ("value", "rate", "uncertainty"),
    [
        ("58.2% ± 2.8%", 0.582, 2.8),
        ("100% ± 0%", 1.0, 0.0),
        ("  7.5%±0.5%  ", 0.075, 0.5),
    ],
)
def test_parse_rate_returns_the_rate_as_a_fraction_and_the_uncertainty_in_points(value, rate, uncertainty):
    parsed_rate, parsed_uncertainty = build_tb4.parse_rate(value)

    assert parsed_rate == pytest.approx(rate)
    assert parsed_uncertainty == uncertainty


@pytest.mark.parametrize("value", ["58.2%", "58.2 ± 2.8%", "58.2% ± 2.8", "fifty percent", "", "-1% ± 2%", "58.2%±"])
def test_parse_rate_refuses_anything_other_than_a_rate_with_an_uncertainty(value):
    with pytest.raises(ValueError, match=re.escape(f"unexpected Terminal-Bench resolution rate: {value!r}")):
        build_tb4.parse_rate(value)


# ---------------------------------------------------------------------------
# parse_cost(): "$3.3k" -> dollars rounded to cents
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    ("value", "dollars"),
    [
        ("$450", 450.0),
        ("$1.5", 1.5),
        ("$3.3k", 3300.0),
        ("$1.2K", 1200.0),
        ("$2m", 2_000_000.0),
        ("$0.5M", 500_000.0),
        ("  $2.00 ", 2.0),
        ("$1.239", 1.24),
        ("$1.001k", 1001.0),
    ],
)
def test_parse_cost_expands_magnitude_suffixes_and_rounds_to_cents(value, dollars):
    assert build_tb4.parse_cost(value) == dollars


@pytest.mark.parametrize("value", ["3.3k", "$", "$abc", "$3.3x", "$3.3 k", "$-2", "USD 3"])
def test_parse_cost_refuses_values_without_a_dollar_amount(value):
    with pytest.raises(ValueError, match=re.escape(f"unexpected Terminal-Bench cost: {value!r}")):
        build_tb4.parse_cost(value)


@pytest.mark.parametrize("value", ["—", "–", "-", "", "  ", "n/a", "N/A", " N/a "])
def test_parse_cost_returns_none_when_the_leaderboard_publishes_no_cost(value):
    assert build_tb4.parse_cost(value) is None


def test_main_keeps_a_row_without_a_published_cost_and_counts_it(data_dir, capsys):
    scrape_document = synthetic_scrape()
    scrape_document["rows"].append(["20", "Muse Spark 1.3 (xhigh)", "Muse Code", "14.5% ± 2.9%", "Sep 2, 2026", "9.0B", "—"])
    scrape = write_json(data_dir / "scrape.json", scrape_document)
    output = data_dir / "tb4.json"

    assert build_tb4.main([str(scrape), str(output)], data=data_dir) == 0

    document = read_document(output)
    assert document["rowN"] == 5
    assert document["rowsWithoutCostN"] == 1
    assert document["rows"][4]["costUsd"] is None
    assert document["rows"][4]["cohortModelId"] == "muse-spark-1-3-xhigh"  # O33: exact model and effort alias
    assert document["rows"][0]["costUsd"] == 3300.0
    assert json.loads(capsys.readouterr().out)["rowsWithoutCostN"] == 1


def test_an_exact_alias_names_one_effort_and_never_its_family(data_dir):
    """O33: a family ranked at several efforts is aliased by the exact displayed model and effort only."""

    scrape_document = synthetic_scrape()
    scrape_document["rows"].append(["21", "Muse Spark 1.3 (high)", "Muse Code", "12.0% ± 2.9%", "Sep 2, 2026", "9.0B", "—"])
    output = data_dir / "tb4.json"
    assert build_tb4.main([str(write_json(data_dir / "scrape.json", scrape_document)), str(output)], data=data_dir) == 0
    assert read_document(output)["rows"][4]["cohortModelId"] is None


def test_parse_cost_refuses_a_malformed_decimal_rather_than_guessing():
    with pytest.raises(ValueError):
        build_tb4.parse_cost("$1.2.3")


# ---------------------------------------------------------------------------
# main(): normalised rows, cohort and provider-claim eligibility, provenance
# ---------------------------------------------------------------------------


def test_main_normalises_rows_matches_the_cohort_and_records_capture_provenance(data_dir, capsys):
    scrape = write_json(data_dir / "captures" / "scrape.json", synthetic_scrape())
    output = data_dir / "out" / "tb4.json"
    output.parent.mkdir(parents=True)

    assert build_tb4.main([str(scrape), str(output)], data=data_dir) == 0

    document = read_document(output)
    assert document["schemaVersion"] == "valuerank-terminal-bench-v1"
    assert document["version"] == "4.0"
    assert document["observedAt"] == "2026-10-23T06:26:23Z"
    assert document["source"] == {
        "publisher": "Terminal-Bench / Harbor",
        "targetUrl": "https://www.tbench.ai/leaderboard/terminal-bench/4.0",
        "renderedUrl": "https://www.tbench.ai/",
        "homepage": "https://www.tbench.ai/",
        "tasksUrl": "https://hub.harborframework.com/datasets/terminal-bench/terminal-bench/4?tab=tasks",
        "captureSha256": hashlib.sha256(scrape.read_bytes()).hexdigest(),
        "capturePath": str(scrape),
        "captureMethod": "rendered leaderboard snapshot",
        "capturedAt": "2026-09-04T13:50:16.451Z",
    }
    assert document["rowN"] == 4
    assert document["rowsWithoutCostN"] == 0
    assert document["cohortN"] == 6
    assert document["matchedN"] == 4
    assert document["missingModels"] == ["Gemini 3.7 Flash", "Claude Sonnet 5"]
    assert document["rankingAvailableN"] == 5
    assert document["rankingMissingModels"] == ["Claude Sonnet 5"]
    assert document["providerClaimN"] == 2
    assert [claim["claimId"] for claim in document["providerClaims"]] == [
        "gemini-37-flash-tb4-a",
        "gemini-37-flash-tb4-b",
    ]
    assert document["rows"][0] == {
        "rank": 1,
        "rankLabel": "1",
        "model": "GPT-6 Astra (max)",
        "baseModel": "GPT-6 Astra",
        "agent": "Codex",
        "resolutionRate": 0.582,
        "resolutionRatePct": 58.2,
        "uncertaintyPct": 2.8,
        "releaseDate": "Sep 3, 2026",
        "tokens": "1.5B",
        "costUsd": 3300.0,
        "cohortModelId": "gpt-6-astra",
    }
    assert document["rows"][1]["cohortModelId"] == "claude-fable-5-1", "Fable 5.1 joined the cohort (O31)"
    assert document["rows"][1]["baseModel"] == "Fable 5.1"
    assert document["rows"][3]["baseModel"] == "Grok 4.6", "a name without a parenthetical is its own base"
    assert document["rows"][3]["costUsd"] == 450.0
    assert list(document["cohortRows"]) == ["gpt-6-astra", "claude-opus-5", "grok-4.6", "claude-fable-5-1"]
    assert document["cohortRows"]["claude-opus-5"]["model"] == "Opus 5 (max)"
    assert document["cohortRows"]["claude-opus-5"]["costUsd"] == 6000.0
    assert "providerClaimPolicy" in document


def test_main_summary_reports_counts_missing_models_and_the_output_path(data_dir, capsys):
    scrape = write_json(data_dir / "scrape.json", synthetic_scrape())
    output = data_dir / "tb4.json"

    build_tb4.main([str(scrape), str(output)], data=data_dir)

    summary = json.loads(capsys.readouterr().out)
    assert summary == {
        "version": "4.0",
        "rows": 4,
        "rowsWithoutCostN": 0,
        "cohortN": 6,
        "matchedN": 4,
        "rankingAvailableN": 5,
        "providerClaimN": 2,
        "missingModels": ["Gemini 3.7 Flash", "Claude Sonnet 5"],
        "rankingMissingModels": ["Claude Sonnet 5"],
        "output": str(output),
    }


def test_main_takes_its_default_capture_and_output_from_the_data_directory(data_dir, monkeypatch):
    write_json(data_dir / "tb4-scrape.json", synthetic_scrape())
    monkeypatch.setattr(sys, "argv", ["build_tb4.py"])

    assert build_tb4.main(data=data_dir) == 0

    document = read_document(data_dir / "tb4.json")
    assert document["source"]["capturePath"] == str(data_dir / "tb4-scrape.json")
    assert document["rowN"] == 4


def test_main_reads_the_explicit_arguments_from_argv_when_none_are_passed(data_dir, monkeypatch):
    scrape = write_json(data_dir / "elsewhere" / "capture.json", synthetic_scrape())
    output = data_dir / "elsewhere" / "normalised.json"
    monkeypatch.setattr(sys, "argv", ["build_tb4.py", str(scrape), str(output)])

    assert build_tb4.main(data=data_dir) == 0

    assert read_document(output)["source"]["capturePath"] == str(scrape)
    assert not (data_dir / "tb4.json").exists(), "an explicit output path replaces the default"


def test_main_with_only_an_input_path_writes_the_default_output_in_the_data_directory(data_dir):
    scrape = write_json(data_dir / "elsewhere" / "capture.json", synthetic_scrape())

    assert build_tb4.main([str(scrape)], data=data_dir) == 0

    assert read_document(data_dir / "tb4.json")["rowN"] == 4


def test_main_records_the_capture_method_when_the_capture_states_one(data_dir):
    capture = {**synthetic_scrape(), "captureMethod": "browser-rendered DOM"}
    scrape = write_json(data_dir / "scrape.json", capture)
    output = data_dir / "tb4.json"

    build_tb4.main([str(scrape), str(output)], data=data_dir)

    assert read_document(output)["source"]["captureMethod"] == "browser-rendered DOM"


def test_main_treats_a_claims_file_without_a_claims_list_as_having_no_claims(data_dir):
    write_json(data_dir / "provider_claims.json", {"schemaVersion": "synthetic-provider-claims"})
    scrape = write_json(data_dir / "scrape.json", synthetic_scrape())
    output = data_dir / "tb4.json"

    build_tb4.main([str(scrape), str(output)], data=data_dir)

    document = read_document(output)
    assert document["providerClaimN"] == 0
    assert document["providerClaims"] == []
    assert document["rankingAvailableN"] == 4
    assert document["rankingMissingModels"] == ["Gemini 3.7 Flash", "Claude Sonnet 5"]


def test_duplicate_cohort_alias_is_rejected_instead_of_silently_picking_a_row(data_dir):
    # Two leaderboard rows resolving to the same cohort model are ambiguous evidence;
    # the stage must refuse rather than let the later row silently win.
    capture = synthetic_scrape()
    capture["rows"].append(["5", "Opus 5 (high)", "Claude Code", "49.0% ± 3.0%", "Jul 20, 2026", "5.0B", "$4.1k"])
    scrape = write_json(data_dir / "scrape.json", capture)
    output = data_dir / "tb4.json"

    with pytest.raises(ValueError, match="cohort aliases are not unique: claude-opus-5"):
        build_tb4.main([str(scrape), str(output)], data=data_dir)

    assert not output.exists()


# ---------------------------------------------------------------------------
# main(): refusals of malformed captures, with the message the operator sees
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "rows",
    [
        None,
        [],
        [["RANK", "MODEL", "AGENT", "RESOLUTION RATE", "RELEASE DATE", "COST", "TOKENS"]],
    ],
    ids=["no-rows-key", "empty-rows", "reordered-header"],
)
def test_main_refuses_a_capture_without_the_expected_table_header(data_dir, rows):
    capture = synthetic_scrape()
    if rows is None:
        del capture["rows"]
    else:
        capture["rows"] = rows
    scrape = write_json(data_dir / "scrape.json", capture)

    with pytest.raises(ValueError, match="Terminal-Bench capture does not contain the expected 4.0 table header"):
        build_tb4.main([str(scrape), str(data_dir / "tb4.json")], data=data_dir)
    assert not (data_dir / "tb4.json").exists()


@pytest.mark.parametrize("bad_row_index", [1, 2])
def test_main_names_the_one_based_data_row_with_the_wrong_cell_count(data_dir, bad_row_index):
    capture = synthetic_scrape()
    capture["rows"][bad_row_index] = capture["rows"][bad_row_index][:-1]
    scrape = write_json(data_dir / "scrape.json", capture)

    with pytest.raises(ValueError, match=re.escape(f"Terminal-Bench row {bad_row_index} has 6 cells, expected 7")):
        build_tb4.main([str(scrape), str(data_dir / "tb4.json")], data=data_dir)


def test_main_propagates_a_malformed_resolution_rate(data_dir):
    capture = synthetic_scrape()
    capture["rows"][1][3] = "58% correct"
    scrape = write_json(data_dir / "scrape.json", capture)

    with pytest.raises(ValueError, match="unexpected Terminal-Bench resolution rate: '58% correct'"):
        build_tb4.main([str(scrape), str(data_dir / "tb4.json")], data=data_dir)


def test_main_propagates_a_malformed_cost(data_dir):
    capture = synthetic_scrape()
    capture["rows"][2][6] = "$3.3 thousand"
    scrape = write_json(data_dir / "scrape.json", capture)

    with pytest.raises(ValueError, match=re.escape("unexpected Terminal-Bench cost: '$3.3 thousand'")):
        build_tb4.main([str(scrape), str(data_dir / "tb4.json")], data=data_dir)


# ---------------------------------------------------------------------------
# Executable entry point
# ---------------------------------------------------------------------------


def test_module_entrypoint_normalises_the_capture_and_exits_zero(data_dir, monkeypatch):
    monkeypatch.delitem(sys.modules, "valuerank.build_tb4", raising=False)
    monkeypatch.setattr(paths, "DATA", data_dir)
    scrape = write_json(data_dir / "scrape.json", synthetic_scrape())
    output = data_dir / "tb4.json"
    monkeypatch.setattr(sys, "argv", ["build_tb4.py", str(scrape), str(output)])
    real_document = ROOT / "data" / "tb4.json"
    before = real_document.read_bytes()

    with pytest.raises(SystemExit) as exit_info:
        runpy.run_module("valuerank.build_tb4", run_name="__main__", alter_sys=True)

    assert exit_info.value.code == 0
    assert read_document(output)["rowN"] == 4
    assert real_document.read_bytes() == before
