"""Behavior tests for the Coding Agent Index cost capture (network mocked at urllib)."""

from __future__ import annotations

import json
import runpy
import urllib.request

import pytest

from valuerank import capture_coding_agents as cca


def row(identifier, label, *, total=300.0, mean=1.0, agent="Agent", model="Model (max)", evals=None, **extra):
    document = {
        "id": identifier,
        "displayLabel": label,
        "display": {"agent": agent, "model": model},
        "agentName": agent,
        "isDefault": True,
        "isUnavailable": False,
        "indexScore": 0.5,
        "sums": {"costUsd": total},
        "mean": {"reward": 0.5, "costUsd": mean},
        "evals": evals
        if evals is not None
        else [
            {
                "datasetIndexName": "deep-swe-v1.1",
                "refDatasetName": "datacurve/deep-swe-1-1@1",
                "weight": 1 / 3,
                "safety": {"attemptCount": 339},
                "mean": {"reward": 0.7},
            }
        ],
    }
    document.update(extra)
    return document


def page(*flight_lines: str) -> str:
    """An HTML page whose flight payload is ``flight_lines``, split over two push chunks."""

    text = "\n".join(flight_lines) + "\n"
    middle = len(text) // 2
    chunks = [text[:middle], text[middle:]]
    scripts = "".join(f"<script>self.__next_f.push([1,{json.dumps(chunk)}])</script>" for chunk in chunks)
    return f"<html><body>{scripts}</body></html>"


def test_flight_text_joins_pushed_chunks_in_order():
    html = page('1:{"a":1}', '2:["b"]')
    assert cca.flight_text(html) == '1:{"a":1}\n2:["b"]\n'


def test_flight_values_skip_lines_that_are_not_json():
    text = '1:{"a":1}\n2:[broken\n3:"text line"\n4:["x",{"y":2}]\n'
    assert cca.flight_values(text) == [{"a": 1}, ["x", {"y": 2}]]


def test_configuration_rows_dedupe_by_id_and_require_cost_blocks():
    first = row("a1", "Agent - Model (max)")
    duplicate = dict(first, displayLabel="duplicate label ignored")
    no_sums = {"id": "b2", "displayLabel": "No sums", "mean": {}}
    no_id = row("", "No id")
    values = [{"rows": [first, no_sums]}, ["$", {"benchmarkRows": [duplicate, no_id]}], "scalar"]
    rows = cca.configuration_rows(values)
    assert [item["displayLabel"] for item in rows] == ["Agent - Model (max)"]


def test_configuration_record_keeps_costs_and_implied_task_count():
    record = cca.configuration_record(row("a1", "Codex - GPT (max)", total=468.7, mean=1.554))
    assert record["label"] == "Codex - GPT (max)"
    assert record["agent"] == "Agent" and record["model"] == "Model (max)"
    assert record["totalCostUsd"] == 468.7 and record["meanCostPerTaskUsd"] == 1.554
    assert record["pricedTaskCount"] == round(468.7 / 1.554, 6)
    assert record["components"] == [
        {"name": "deep-swe-v1.1", "dataset": "datacurve/deep-swe-1-1@1", "weight": 1 / 3, "attempts": 339, "reward": 0.7}
    ]


def test_configuration_record_without_costs_or_display_falls_back():
    raw = row("u1", "Mirror - Beam", total=None, mean=None, evals=[{"datasetIndexName": "x"}])
    raw.pop("display")
    raw["indexScore"] = True  # a boolean is not a score
    record = cca.configuration_record(raw)
    assert record["agent"] == "Agent" and record["model"] is None
    assert record["totalCostUsd"] is None and record["meanCostPerTaskUsd"] is None
    assert record["pricedTaskCount"] is None and record["indexScore"] is None
    assert record["components"] == [{"name": "x", "dataset": None, "weight": None, "attempts": None, "reward": None}]


def test_configuration_record_with_zero_mean_has_no_task_count():
    record = cca.configuration_record(row("z1", "Zero", total=0.0, mean=0.0, evals=[]))
    assert record["pricedTaskCount"] is None and record["components"] == []


def test_capture_document_sorts_records_and_hashes_the_response():
    html = page(
        "1:" + json.dumps({"rows": [row("b", "Zeta - M"), row("a", "Alpha - M")]}),
    )
    document = cca.capture_document(html, captured_at="2026-10-19T00:00:00Z", response_bytes=b"abc")
    assert [record["label"] for record in document["configurations"]] == ["Alpha - M", "Zeta - M"]
    assert document["capturedAt"] == "2026-10-19T00:00:00Z"
    assert document["source"] == cca.SOURCE_URL
    assert document["responseSha256"] == "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad"


def test_capture_document_without_rows_fails_loudly():
    with pytest.raises(ValueError, match="no Coding Agent Index configuration rows"):
        cca.capture_document(page('1:{"a":1}'), captured_at="x", response_bytes=b"")


class FakeResponse:
    def __init__(self, body: bytes):
        self._body = body

    def read(self):
        return self._body

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return False


def test_main_writes_the_capture(monkeypatch, tmp_path, capsys):
    html = page("1:" + json.dumps({"rows": [row("a", "Alpha - M", total=10.0, mean=None), row("b", "Beta - M")]}))
    seen = {}

    def fake_urlopen(request, timeout=None):
        seen["url"], seen["timeout"] = request.full_url, timeout
        return FakeResponse(html.encode())

    output = tmp_path / "data" / "aa" / "coding_agents_capture.json"
    output.parent.mkdir(parents=True)
    monkeypatch.setattr(urllib.request, "urlopen", fake_urlopen)
    monkeypatch.setattr(cca, "OUTPUT_PATH", output)
    monkeypatch.setattr(cca, "ROOT", tmp_path)
    monkeypatch.setattr(cca, "iso_z", lambda: "2026-10-19T12:00:00Z")
    assert cca.main() == 0
    written = json.loads(output.read_text())
    assert seen == {"url": cca.SOURCE_URL, "timeout": 60}
    assert written["capturedAt"] == "2026-10-19T12:00:00Z"
    summary = json.loads(capsys.readouterr().out)
    assert summary == {"configurations": 2, "priced": 2, "output": "data/aa/coding_agents_capture.json"}


def test_module_entry_point(monkeypatch, tmp_path):
    html = page("1:" + json.dumps({"rows": [row("a", "Alpha - M")]}))
    monkeypatch.setattr(urllib.request, "urlopen", lambda request, timeout=None: FakeResponse(html.encode()))
    import valuerank.paths as paths

    monkeypatch.setattr(paths, "DATA", tmp_path / "data")
    monkeypatch.setattr(paths, "ROOT", tmp_path)
    (tmp_path / "data" / "aa").mkdir(parents=True)
    with pytest.warns(RuntimeWarning), pytest.raises(SystemExit) as exit_info:
        runpy.run_module("valuerank.capture_coding_agents", run_name="__main__", alter_sys=True)
    assert exit_info.value.code == 0
    assert (tmp_path / "data" / "aa" / "coding_agents_capture.json").exists()
