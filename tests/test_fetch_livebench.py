"""Behavior tests for the pinned LiveBench release stage (valuerank.fetch_livebench).

Every test runs against small synthetic release payloads under
``tests/fixtures/external/livebench``. ``fetch`` is exercised with
``urllib.request.urlopen`` patched at the boundary, and ``main`` receives an
injected fetcher, so nothing here reaches livebench.ai or GitHub. Output is
written only into temporary directories.
"""

from __future__ import annotations

import csv
import hashlib
import io
import json
import math
import re
import runpy
import sys
import urllib.error
import urllib.request
from pathlib import Path

import pytest

import valuerank.paths as paths
from valuerank import fetch_livebench as stage
from valuerank.paths import ROOT

FIXTURES = Path(__file__).parent / "fixtures" / "external" / "livebench"
TABLE_CSV = (FIXTURES / "table.csv").read_bytes()
COST_CSV = (FIXTURES / "cost.csv").read_bytes()
CATEGORIES_JSON = (FIXTURES / "categories.json").read_bytes()
COST_KEY = "cost_per_successful_task"

GPT_LIVEBENCH = "gpt-6-astra-max"
OPUS_LIVEBENCH = "claude-opus-5-max-effort"
FABLE_LIVEBENCH = "claude-fable-5-1-max-effort"


class FakeResponse:
    """The subset of an ``http.client`` response that ``fetch`` reads."""

    def __init__(self, payload: bytes, *, status: int = 200, content_type: str | None = "text/csv"):
        self._payload = payload
        self.status = status
        self.headers = {} if content_type is None else {"Content-Type": content_type}

    def read(self) -> bytes:
        return self._payload

    def __enter__(self) -> FakeResponse:
        return self

    def __exit__(self, *exc_info) -> None:
        return None


def release_routes(
    table: bytes = TABLE_CSV, cost: bytes = COST_CSV, categories: bytes = CATEGORIES_JSON
) -> dict[str, bytes]:
    return {stage.URLS["table"]: table, stage.URLS["cost"]: cost, stage.URLS["categories"]: categories}


def scripted_fetch(routes: dict[str, bytes], calls: list[str]):
    """An injected source fetcher that serves canned bytes and records each requested URL."""

    def fetch_url(url: str) -> tuple[bytes, dict[str, str | int]]:
        calls.append(url)
        payload = routes[url]
        return payload, {
            "url": url,
            "status": "200",
            "contentType": "text/csv",
            "bytes": len(payload),
            "sha256": hashlib.sha256(payload).hexdigest(),
        }

    return fetch_url


def parsed_tables(table: bytes = TABLE_CSV, cost: bytes = COST_CSV):
    table_by_model = {row["model"]: row for row in csv.DictReader(io.StringIO(table.decode("utf-8")))}
    cost_by_model = {row["model"]: row for row in csv.DictReader(io.StringIO(cost.decode("utf-8")))}
    return table_by_model, cost_by_model


def labelled_categories() -> dict[str, list[str]]:
    categories = json.loads(CATEGORIES_JSON)
    return {stage.CATEGORY_LABELS[key]: list(tasks) for key, tasks in categories.items()}


def build(model_id: str, livebench_model: str | None, table: bytes = TABLE_CSV, cost: bytes = COST_CSV):
    table_by_model, cost_by_model = parsed_tables(table, cost)
    return stage.build_record(
        model_id=model_id,
        display_name=model_id.upper(),
        livebench_model=livebench_model,
        table_by_model=table_by_model,
        cost_by_model=cost_by_model,
        task_categories=labelled_categories(),
        cost_key=COST_KEY,
    )


# ---------------------------------------------------------------------------
# number(): converting release cells, including blanks and malformed values
# ---------------------------------------------------------------------------


@pytest.mark.parametrize("value", [None, "", "   ", "n/a", "N/A", "NA", "null", "-", "—"])
def test_number_treats_absent_markers_as_missing_not_zero(value):
    assert stage.number(value, "m.task") is None


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        ("$1,234.50", 1234.5),
        ("45%", 45.0),
        (" 12 ", 12.0),
        ("0", 0.0),
        (7, 7.0),
        ("1e3", 1000.0),
        ("-2.5", -2.5),
    ],
)
def test_number_parses_currency_percent_and_separators(value, expected):
    assert stage.number(value, "m.task") == expected


@pytest.mark.parametrize("value", ["abc", "$", "12 points"])
def test_number_rejects_non_numeric_values_with_the_label(value):
    expected = f"non-numeric LiveBench value for m.task: {value!r}"
    with pytest.raises(ValueError, match=re.escape(expected)):
        stage.number(value, "m.task")


@pytest.mark.parametrize("value", ["nan", "inf", "-inf"])
def test_number_rejects_non_finite_values(value):
    with pytest.raises(ValueError, match="non-finite LiveBench value for m.task"):
        stage.number(value, "m.task")


# ---------------------------------------------------------------------------
# mean(): category and overall means
# ---------------------------------------------------------------------------


def test_mean_averages_and_rounds_to_six_places():
    assert stage.mean([1, 2, 3, 4], "Reasoning") == 2.5
    assert stage.mean([1, 1, 2], "Reasoning") == 1.333333


def test_mean_refuses_an_empty_category_instead_of_dividing_by_zero():
    with pytest.raises(ValueError, match="empty LiveBench category: Reasoning"):
        stage.mean([], "Reasoning")


@pytest.mark.parametrize("values", [[1.0, math.nan], [math.inf]])
def test_mean_refuses_non_finite_inputs(values):
    with pytest.raises(ValueError, match="non-finite LiveBench category: Reasoning"):
        stage.mean(values, "Reasoning")


# ---------------------------------------------------------------------------
# pareto_ids(): cost-versus-score frontier over usable rows
# ---------------------------------------------------------------------------


def point(model_id: str, score: float | None, cost: float | None, *, matched: bool = True) -> dict:
    return {
        "modelId": model_id,
        "matched": matched,
        "overallScore": score,
        "costPerSuccessfulTaskUsd": cost,
    }


def frontier(*rows: dict) -> list[str]:
    return stage.pareto_ids({row["modelId"]: row for row in rows})


def test_pareto_keeps_models_no_other_model_beats_on_both_axes_sorted_by_cost():
    kept = frontier(
        point("expensive-best", 70, 2.0),
        point("cheap-weak", 50, 1.0),
        point("dominated", 60, 3.0),
    )

    assert kept == ["cheap-weak", "expensive-best"]


def test_pareto_drops_a_model_that_is_both_costlier_and_weaker_than_another():
    assert frontier(point("a", 50, 1.0), point("b", 70, 2.0), point("c", 60, 3.0)) == ["a", "b"]


def test_pareto_equal_cost_with_a_higher_score_dominates():
    assert frontier(point("a", 50, 1.0), point("b", 60, 1.0)) == ["b"]


def test_pareto_equal_score_with_a_lower_cost_dominates():
    assert frontier(point("a", 60, 2.0), point("b", 60, 1.0)) == ["b"]


def test_pareto_keeps_exact_ties_because_neither_strictly_beats_the_other():
    assert frontier(point("a", 50, 1.0), point("b", 50, 1.0)) == ["a", "b"]


def test_pareto_ignores_unmatched_or_incomplete_rows_even_when_they_would_dominate():
    kept = frontier(
        point("unmatched-better", 99, 0.5, matched=False),
        point("no-score", None, 0.4),
        point("no-cost", 98, None),
        point("real", 50, 2.0),
    )

    assert kept == ["real"]


def test_pareto_of_nothing_usable_is_empty():
    assert frontier() == []
    assert frontier(point("unmatched", 50, 1.0, matched=False)) == []


# ---------------------------------------------------------------------------
# build_record(): one cohort row, matched, unmatched or refused
# ---------------------------------------------------------------------------


def test_build_record_without_a_livebench_mapping_is_unmatched_and_imputes_nothing():
    record = build("gpt-6.1-sol", None)

    assert record["matched"] is False
    assert record["matchStatus"] == "no_verified_exact_mapping"
    assert record["livebenchModel"] is None
    assert record["coverageNote"].startswith("No exact mapped task-and-cost result")
    assert record["tasks"] == {}
    assert record["categoryScores"] == {}
    assert record["overallScore"] is None
    assert record["instructionFollowingScore"] is None
    assert record["costPerSuccessfulTaskUsd"] is None


def test_build_record_with_a_mapping_absent_from_the_release_is_unmatched():
    record = build("claude-sonnet-5", "claude-sonnet-5-xhigh-effort")

    assert record["matched"] is False
    assert record["matchStatus"] == "no_exact_match_in_pinned_release"
    assert record["livebenchModel"] == "claude-sonnet-5-xhigh-effort"
    assert record["tasks"] == {}


def test_build_record_with_a_table_row_but_no_cost_row_is_unmatched():
    table, _ = parsed_tables()
    cost_without_gpt = {}
    record = stage.build_record(
        model_id="gpt-6-astra",
        display_name="GPT-6 Astra",
        livebench_model=GPT_LIVEBENCH,
        table_by_model=table,
        cost_by_model=cost_without_gpt,
        task_categories=labelled_categories(),
        cost_key=COST_KEY,
    )

    assert record["matched"] is False
    assert record["matchStatus"] == "no_exact_match_in_pinned_release"


def test_build_record_for_a_matched_model_computes_tasks_categories_and_overall():
    record = build("gpt-6-astra", GPT_LIVEBENCH)

    assert record["matched"] is True
    assert record["matchStatus"] == "matched"
    assert record["coverageNote"] is None
    assert record["tasks"] == {
        "amc": 90.0,
        "completion": 70.0,
        "ifeval": 100.0,
        "plot": 30.0,
        "spatial": 60.0,
        "tablejoin": 40.0,
        "terminal": 50.0,
        "zebra": 80.0,
    }
    assert record["categoryScores"] == {
        "Reasoning": 70.0,
        "Coding": 70.0,
        "Agentic Coding": 50.0,
        "Mathematics": 90.0,
        "Data Analysis": 40.0,
        "Language": 30.0,
        "Instruction Following": 100.0,
    }
    assert record["overallScore"] == 64.285714
    assert record["instructionFollowingScore"] == 100.0
    assert record["costPerSuccessfulTaskUsd"] == 0.25


def test_build_record_refuses_a_blank_task_cell_rather_than_imputing_it():
    table = TABLE_CSV.replace(b"gpt-6-astra-max,80,60,", b"gpt-6-astra-max,80,,")

    with pytest.raises(ValueError, match="incomplete LiveBench category for gpt-6-astra: Reasoning"):
        build("gpt-6-astra", GPT_LIVEBENCH, table=table)


def test_build_record_treats_an_n_a_task_cell_as_missing_and_imputes_nothing():
    table = TABLE_CSV.replace(b"gpt-6-astra-max,80,60,70,50,90,40,30,100", b"gpt-6-astra-max,80,60,70,n/a,90,40,30,100")

    with pytest.raises(ValueError, match="incomplete LiveBench category for gpt-6-astra: Agentic Coding"):
        build("gpt-6-astra", GPT_LIVEBENCH, table=table)


def test_build_record_reports_a_malformed_task_cell_with_its_label():
    table = TABLE_CSV.replace(b"gpt-6-astra-max,80,60", b"gpt-6-astra-max,eighty,60")

    with pytest.raises(ValueError, match="non-numeric LiveBench value for gpt-6-astra.zebra"):
        build("gpt-6-astra", GPT_LIVEBENCH, table=table)


@pytest.mark.parametrize("cost_cell", [b"0", b"-1", b"", b"n/a"])
def test_build_record_refuses_a_missing_or_non_positive_cost(cost_cell):
    cost = COST_CSV.replace(b"gpt-6-astra-max,$0.25", b"gpt-6-astra-max," + cost_cell)

    with pytest.raises(ValueError, match="missing/non-positive LiveBench cost for gpt-6-astra"):
        build("gpt-6-astra", GPT_LIVEBENCH, cost=cost)


# ---------------------------------------------------------------------------
# fetch(): urllib boundary, provenance capture and error propagation
# ---------------------------------------------------------------------------


def test_fetch_returns_the_exact_bytes_with_hash_and_header_provenance(monkeypatch):
    payload = b"model,zebra\ngpt,1\n"
    seen: dict[str, object] = {}

    def fake_urlopen(request, timeout=None):
        seen["timeout"] = timeout
        seen["user_agent"] = request.get_header("User-agent")
        seen["url"] = request.full_url
        return FakeResponse(payload, status=203, content_type="text/csv; charset=utf-8")

    monkeypatch.setattr(urllib.request, "urlopen", fake_urlopen)

    body, source = stage.fetch("https://example.test/table.csv")

    assert body == payload
    assert source == {
        "url": "https://example.test/table.csv",
        "status": "203",
        "contentType": "text/csv; charset=utf-8",
        "bytes": len(payload),
        "sha256": hashlib.sha256(payload).hexdigest(),
    }
    assert seen == {
        "timeout": 30,
        "user_agent": "ValueRank/1.4 official-source-refresh",
        "url": "https://example.test/table.csv",
    }


def test_fetch_records_an_empty_content_type_when_the_server_sends_none(monkeypatch):
    monkeypatch.setattr(
        urllib.request,
        "urlopen",
        lambda request, timeout=None: FakeResponse(b"", content_type=None),
    )

    body, source = stage.fetch("https://example.test/empty")

    assert body == b""
    assert source["contentType"] == ""
    assert source["bytes"] == 0
    assert source["sha256"] == hashlib.sha256(b"").hexdigest()


def test_fetch_lets_transport_failures_propagate_instead_of_publishing_partial_data(monkeypatch):
    def unreachable(request, timeout=None):
        raise urllib.error.URLError("network unreachable")

    monkeypatch.setattr(urllib.request, "urlopen", unreachable)

    with pytest.raises(urllib.error.URLError, match="network unreachable"):
        stage.fetch("https://example.test/down")


# ---------------------------------------------------------------------------
# main(): the release document, its printed summary and every refusal
# ---------------------------------------------------------------------------


AA_MODELS = {
    "gpt-6-astra": {"displayName": "GPT-6 Astra"},
    "claude-opus-5": {"displayName": "Claude Opus 5"},
    "gpt-6.1-sol": {"displayName": "GPT-6.1 Sol"},
    "claude-sonnet-5": {"displayName": "Claude Sonnet 5"},
}
SMALL_COHORT = {
    "gpt-6-astra": GPT_LIVEBENCH,
    "claude-opus-5": OPUS_LIVEBENCH,
    "gpt-6.1-sol": None,
    "claude-sonnet-5": "claude-sonnet-5-xhigh-effort",
}
SMALL_SUPPLEMENTAL = {"claude-fable-5-1": ("Claude Fable 5.1", FABLE_LIVEBENCH)}


@pytest.fixture
def small_world(monkeypatch, tmp_path, pinned_clock):
    """A four-model cohort, one supplemental model and a tmp data directory with the AA map."""

    monkeypatch.setattr(stage, "COHORT_MAP", dict(SMALL_COHORT))
    monkeypatch.setattr(stage, "SUPPLEMENTAL_MAP", dict(SMALL_SUPPLEMENTAL))
    data = tmp_path / "data"
    data.mkdir()
    (data / "aa_metrics.json").write_text(json.dumps({"models": AA_MODELS}), encoding="utf-8")
    return data


def run_main(data: Path, *, routes: dict[str, bytes] | None = None, calls: list[str] | None = None) -> int:
    fetch_url = scripted_fetch(routes if routes is not None else release_routes(), calls if calls is not None else [])
    return stage.main(data=data, fetch_url=fetch_url)


def read_document(data: Path) -> dict:
    return json.loads((data / "livebench.json").read_text(encoding="utf-8"))


def test_main_writes_the_release_document_with_the_pinned_observation_instant(small_world, capsys):
    assert run_main(small_world) == 0

    document = read_document(small_world)
    assert document["schemaVersion"] == "valuerank-livebench-v1"
    assert document["release"] == "2026_06_25"
    assert document["observedAt"] == "2026-10-25T09:56:47Z"
    assert document["categories"]["Instruction Following"] == ["ifeval"]
    assert "IF" not in document["categories"]
    assert document["cohortN"] == 4
    assert document["supplementalN"] == 1
    assert document["publishedN"] == 3
    assert list(document["models"]) == ["gpt-6-astra", "claude-opus-5", "gpt-6.1-sol", "claude-sonnet-5"]
    assert list(document["supplementalModels"]) == ["claude-fable-5-1"]


def test_main_file_is_indented_utf8_json_with_a_trailing_newline(small_world):
    run_main(small_world)

    raw = (small_world / "livebench.json").read_text(encoding="utf-8")
    assert raw.endswith("}\n")
    assert raw == json.dumps(read_document(small_world), indent=2, ensure_ascii=False) + "\n"


def test_main_records_release_provenance_and_the_hash_of_each_source_file(small_world):
    run_main(small_world)

    source = read_document(small_world)["source"]
    assert source["publisher"] == "LiveBench"
    assert source["homepage"] == "https://livebench.ai/"
    assert source["repository"] == "https://github.com/livebench/new-livebench"
    assert source["releaseDataCommit"] == stage.RELEASE_DATA_COMMIT
    assert source["releaseDate"] == "2026-06-25"
    assert source["urls"] == stage.URLS
    files = source["files"]
    assert files["table"]["sha256"] == hashlib.sha256(TABLE_CSV).hexdigest()
    assert files["cost"]["sha256"] == hashlib.sha256(COST_CSV).hexdigest()
    assert files["categories"]["sha256"] == hashlib.sha256(CATEGORIES_JSON).hexdigest()
    assert files["table"]["bytes"] == len(TABLE_CSV)
    assert files["categories"]["url"] == stage.URLS["categories"]


def test_main_requests_the_three_pinned_release_files_in_order(small_world):
    calls: list[str] = []

    run_main(small_world, calls=calls)

    assert calls == [stage.URLS["table"], stage.URLS["cost"], stage.URLS["categories"]]


def test_main_counts_matched_and_missing_models_and_names_the_missing_ones(small_world):
    run_main(small_world)

    document = read_document(small_world)
    assert document["matchedN"] == 2
    assert document["missingModels"] == ["GPT-6.1 Sol", "Claude Sonnet 5"]
    assert document["models"]["gpt-6-astra"]["matchStatus"] == "matched"
    assert document["models"]["gpt-6.1-sol"]["matchStatus"] == "no_verified_exact_mapping"
    assert document["models"]["claude-sonnet-5"]["matchStatus"] == "no_exact_match_in_pinned_release"


def test_main_keeps_supplemental_models_out_of_the_cohort_but_in_the_represented_set(small_world):
    run_main(small_world)

    document = read_document(small_world)
    assert "claude-fable-5-1" not in document["models"]
    assert document["supplementalMatchedN"] == 1
    assert document["supplementalModels"]["claude-fable-5-1"]["matched"] is True
    assert document["representedN"] == 3


def test_main_pareto_frontier_spans_cohort_and_supplemental_models(small_world):
    run_main(small_world)

    # Opus is strictly cheaper-and-weaker than GPT-6 Astra; Fable has the top score.
    assert read_document(small_world)["pareto"] == ["gpt-6-astra", "claude-fable-5-1"]


def test_main_prints_a_summary_of_counts_missing_models_and_frontier(small_world, capsys):
    run_main(small_world)

    summary = json.loads(capsys.readouterr().out)
    assert summary == {
        "release": "2026_06_25",
        "cohortN": 4,
        "matchedN": 2,
        "publishedN": 3,
        "supplementalModels": ["claude-fable-5-1"],
        "missingModels": ["GPT-6.1 Sol", "Claude Sonnet 5"],
        "pareto": ["gpt-6-astra", "claude-fable-5-1"],
        "output": "data/livebench.json",
    }


def test_main_ignores_a_utf8_byte_order_mark_on_the_release_table(small_world):
    run_main(small_world, routes=release_routes(table=b"\xef\xbb\xbf" + TABLE_CSV))

    document = read_document(small_world)
    assert document["matchedN"] == 2
    assert document["publishedN"] == 3


@pytest.mark.parametrize(
    ("aa_models", "message"),
    [
        ({}, "LiveBench mapping expects a non-empty AA comparison cohort"),
        (
            {**AA_MODELS, "gpt-5.5": {"displayName": "GPT-5.5"}},
            "LiveBench cohort mapping does not exactly match the AA model map",
        ),
    ],
    ids=["empty-cohort", "cohort-drift"],
)
def test_main_refuses_a_cohort_that_does_not_match_the_aa_map(small_world, aa_models, message):
    (small_world / "aa_metrics.json").write_text(json.dumps({"models": aa_models}), encoding="utf-8")

    with pytest.raises(ValueError, match=message):
        run_main(small_world)
    assert not (small_world / "livebench.json").exists()


@pytest.mark.parametrize(
    ("routes", "message"),
    [
        (
            release_routes(table=b"model,zebra,spatial,completion,terminal,amc,tablejoin,plot,ifeval\n"),
            "LiveBench source files returned no rows",
        ),
        (
            release_routes(cost=b"model,cost_per_successful_task\n"),
            "LiveBench source files returned no rows",
        ),
        (
            release_routes(categories=json.dumps({**json.loads(CATEGORIES_JSON), "Writing": ["zebra"]}).encode()),
            "unexpected LiveBench categories: ['Agentic Coding', 'Coding', 'Data Analysis', 'IF', 'Language', "
            "'Mathematics', 'Reasoning', 'Writing']",
        ),
        (
            release_routes(table=TABLE_CSV.replace(b",ifeval", b"")),
            "LiveBench table is missing tasks: ['ifeval']",
        ),
        (
            release_routes(cost=b"model,cost\ngpt-6-astra-max,0.25\n"),
            "LiveBench cost file is missing cost_per_successful_task",
        ),
        (
            release_routes(table=b"zebra,spatial,completion,terminal,amc,tablejoin,plot,ifeval\n80,60,70,50,90,40,30,100\n"),
            "LiveBench source contains an empty model key",
        ),
        (
            release_routes(cost=b"cost_per_successful_task\n0.25\n"),
            "LiveBench source contains an empty model key",
        ),
        (
            release_routes(cost=COST_CSV.replace(b"gpt-6-astra-max,$0.25", b"gpt-6-astra-max,0")),
            "missing/non-positive LiveBench cost for gpt-6-astra",
        ),
        (
            release_routes(table=TABLE_CSV.replace(b"gpt-6-astra-max,80,60", b"gpt-6-astra-max,,60")),
            "incomplete LiveBench category for gpt-6-astra: Reasoning",
        ),
    ],
    ids=[
        "table-without-rows",
        "cost-without-rows",
        "unexpected-category",
        "missing-task-column",
        "cost-without-key",
        "table-without-model-column",
        "cost-without-model-column",
        "non-positive-cost",
        "blank-task-cell",
    ],
)
def test_main_refuses_malformed_release_payloads_without_writing(small_world, routes, message):
    with pytest.raises(ValueError, match=re.escape(message)):
        run_main(small_world, routes=routes)
    assert not (small_world / "livebench.json").exists()


def test_main_refuses_a_supplemental_model_that_overlaps_the_cohort(small_world, monkeypatch):
    monkeypatch.setattr(stage, "SUPPLEMENTAL_MAP", {"gpt-6-astra": ("GPT-6 Astra", GPT_LIVEBENCH)})

    with pytest.raises(ValueError, match="LiveBench supplemental model overlaps cohort: gpt-6-astra"):
        run_main(small_world)


def test_main_refuses_a_supplemental_model_absent_from_the_release(small_world, monkeypatch):
    monkeypatch.setattr(stage, "SUPPLEMENTAL_MAP", {"claude-fable-5-1": ("Claude Fable 5.1", "not-in-release-max")})

    with pytest.raises(ValueError, match="LiveBench supplemental model is missing from release: not-in-release-max"):
        run_main(small_world)


# ---------------------------------------------------------------------------
# Committed configuration and the executable entry point
# ---------------------------------------------------------------------------


def test_cohort_map_covers_exactly_the_committed_aa_models(repo_copy):
    aa_document = json.loads((repo_copy / "data" / "aa_metrics.json").read_text(encoding="utf-8"))

    assert set(stage.COHORT_MAP) == set(aa_document["models"])


def test_supplemental_models_never_repeat_a_cohort_model():
    assert not set(stage.SUPPLEMENTAL_MAP) & set(stage.COHORT_MAP)


def test_module_entrypoint_writes_the_release_and_exits_zero(monkeypatch, tmp_path, pinned_clock):
    # runpy re-executes the file as __main__; drop the cached module so it runs fresh and warns nothing.
    monkeypatch.delitem(sys.modules, "valuerank.fetch_livebench", raising=False)
    data = tmp_path / "data"
    data.mkdir()
    (data / "aa_metrics.json").write_text(
        json.dumps({"models": {model_id: {"displayName": model_id} for model_id in stage.COHORT_MAP}}),
        encoding="utf-8",
    )
    # The entrypoint re-imports valuerank.paths, so redirecting DATA here keeps the real repo untouched.
    monkeypatch.setattr(paths, "DATA", data)
    routes = release_routes()
    monkeypatch.setattr(
        urllib.request,
        "urlopen",
        lambda request, timeout=None: FakeResponse(routes[request.full_url]),
    )
    real_document = ROOT / "data" / "livebench.json"
    before = real_document.read_bytes()

    with pytest.raises(SystemExit) as exit_info:
        runpy.run_module("valuerank.fetch_livebench", run_name="__main__", alter_sys=True)

    assert exit_info.value.code == 0
    document = read_document(data)
    assert document["release"] == "2026_06_25"
    assert document["cohortN"] == len(stage.COHORT_MAP)
    # GPT-6 Astra, Opus 5 and (since O31 moved it into the cohort) Fable 5.1 are in the fixture release.
    assert document["matchedN"] == 3
    assert document["supplementalN"] == 0
    assert real_document.read_bytes() == before
