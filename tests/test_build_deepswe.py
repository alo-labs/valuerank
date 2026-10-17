"""Behavior tests for the DeepSWE snapshot stage (valuerank.build_deepswe)."""

from __future__ import annotations

import json
import os
import runpy
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

from valuerank import build_deepswe

# The committed golden (data/deepswe.json) was built from the browser capture and
# records the historical relative snapshot path, so the CLI runs from a working
# directory that holds that same relative path.
GOLDEN_SOURCE = Path("data/deepswe-browser-2026-09-29.json")
GOLDEN_SNAPSHOT_PATH = "data/deepswe-browser-2026-09-29.json"
ROSTER = list(build_deepswe.DISPLAY)
TEXT_SAMPLE = (
    "DeepSWE\nBlog\nRun\n113 tasks\n91 repos\n5 languages\nmodels 28\n"
    "Configs (57/70)\nUpdated September 22, 2026\n"
)


def run_cli(workdir: Path, python_root: Path, *args: str) -> subprocess.CompletedProcess[str]:
    """Run the stage exactly as a user would: ``python -m valuerank.build_deepswe SOURCE OUTPUT``."""

    env = {**os.environ, "PYTHONPATH": str(python_root)}
    return subprocess.run(
        [sys.executable, "-m", "valuerank.build_deepswe", *args],
        cwd=workdir,
        env=env,
        capture_output=True,
        text=True,
        check=False,
    )


def stage_golden_snapshot(workdir: Path, repo: Path) -> None:
    target = workdir / GOLDEN_SNAPSHOT_PATH
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(repo / GOLDEN_SOURCE, target)


def card(
    slug: str,
    *,
    effort: str = "high",
    pct: str = "50%",
    cost: str = "$1.25",
    tokens: str = "10k",
    steps: str = "7",
) -> str:
    return "\n".join([slug, f"[{effort}]", pct, cost, tokens, steps])


def roster_payload(slugs: list[str] = ROSTER, **fields) -> dict:
    return {"cards": [card(slug) for slug in slugs], "scrapedAt": "2026-09-29T00:00:00Z", "textSample": TEXT_SAMPLE, **fields}


def write_payload(path: Path, payload: dict) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload), encoding="utf-8")
    return path


# ---------------------------------------------------------------------------
# Committed golden and the command-line contract
# ---------------------------------------------------------------------------


def test_cli_reproduces_the_committed_golden_snapshot_byte_for_byte(repo_copy, pinned_clock, tmp_path):
    workdir = tmp_path / "workdir"
    stage_golden_snapshot(workdir, repo_copy)
    output = tmp_path / "out" / "deepswe.json"

    completed = run_cli(workdir, repo_copy, GOLDEN_SNAPSHOT_PATH, str(output))

    assert completed.returncode == 0, completed.stderr
    assert output.read_bytes() == (repo_copy / "data" / "deepswe.json").read_bytes()
    summary = json.loads(completed.stdout)
    assert summary["n"] == 21
    assert summary["sourceUpdatedOn"] == "September 22, 2026"


def test_cli_refuses_a_roster_that_is_not_exactly_twenty_one_cards(repo_copy, tmp_path):
    payload = json.loads((repo_copy / GOLDEN_SOURCE).read_text(encoding="utf-8"))
    payload["cards"] = payload["cards"][:-1]
    source = tmp_path / "short-roster.json"
    source.write_text(json.dumps(payload), encoding="utf-8")
    output = tmp_path / "deepswe.json"

    completed = run_cli(tmp_path, repo_copy, str(source), str(output))

    assert completed.returncode != 0
    assert "expected 21 current Best cards, parsed 20" in completed.stderr
    assert not output.exists(), "a rejected roster must not leave a partial snapshot behind"


def test_module_entrypoint_exits_zero_after_writing_the_snapshot(tmp_path, monkeypatch):
    # runpy re-executes the file as __main__; drop the cached module so it runs fresh.
    monkeypatch.delitem(sys.modules, "valuerank.build_deepswe", raising=False)
    source = write_payload(tmp_path / "snap.json", roster_payload())
    output = tmp_path / "deepswe.json"
    monkeypatch.setattr(sys, "argv", ["build_deepswe.py", str(source), str(output)])

    with pytest.raises(SystemExit) as exit_info:
        runpy.run_module("valuerank.build_deepswe", run_name="__main__", alter_sys=True)

    assert exit_info.value.code == 0
    assert json.loads(output.read_text(encoding="utf-8"))["n"] == 21


# ---------------------------------------------------------------------------
# parse_percent(): "74% ± 3%" -> (74.0, "3")
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        ("74%±3%", (74.0, "3")),
        ("58.2%", (58.2, None)),
        ("0%", (0.0, None)),
    ],
)
def test_parse_percent_reads_the_point_estimate_and_optional_uncertainty(value, expected):
    assert build_deepswe.parse_percent(value) == expected


# Regression: the source cards write the uncertainty as "74% ± 3%" with spaces; the
# original pattern missed it and every uncertaintyPct was silently lost.
def test_parse_percent_reads_an_uncertainty_written_with_spaces_around_the_plus_minus():
    assert build_deepswe.parse_percent("74% ± 1%") == (74.0, "1")


@pytest.mark.parametrize("value", ["invalid", "±3%", "%", ""])
def test_parse_percent_refuses_text_without_a_leading_percentage(value):
    with pytest.raises(ValueError, match=f"invalid DeepSWE percentage: {value!r}"):
        build_deepswe.parse_percent(value)


# ---------------------------------------------------------------------------
# parse_tokens(): "30k" -> 30000, unparseable labels -> None
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    ("value", "tokens"),
    [
        ("900", 900),
        ("30k", 30_000),
        ("1.2K", 1_200),
        ("1.5M", 1_500_000),
        ("2m", 2_000_000),
        (" 143k ", 143_000),
    ],
)
def test_parse_tokens_expands_magnitude_suffixes(value, tokens):
    assert build_deepswe.parse_tokens(value) == tokens


@pytest.mark.parametrize("value", ["n/a", "", "30kk", "k", "1,2k"])
def test_parse_tokens_returns_none_for_labels_it_cannot_read(value):
    assert build_deepswe.parse_tokens(value) is None


# ---------------------------------------------------------------------------
# parse_card(): one "slug / [effort] / pass / cost / tokens / steps" card
# ---------------------------------------------------------------------------


def test_parse_card_reads_every_field_of_a_roster_card():
    parsed = build_deepswe.parse_card("gpt-6-astra\n[XHIGH]\n74%±3%\n$6.52\n30k\n29")

    assert parsed == {
        "slug": "gpt-6-astra",
        "name": "gpt-6-astra",
        "displayName": "GPT-6 Astra",
        "effort": "xhigh",
        "passRate": 0.74,
        "passAt1Pct": 74.0,
        "uncertaintyPct": 3.0,
        "avgCost": 6.52,
        "outputTokens": 30_000,
        "outputTokensLabel": "30k",
        "agentSteps": 29,
        "source": "DeepSWE Best page card",
    }


def test_parse_card_ignores_blank_lines_and_surrounding_whitespace():
    parsed = build_deepswe.parse_card("\n  gemini-3.8-flash \n\n [high] \n 74%±1% \n$2.36\n143k\n166\n\n")

    assert parsed["slug"] == "gemini-3.8-flash"
    assert parsed["effort"] == "high"
    assert parsed["passAt1Pct"] == 74.0
    assert parsed["uncertaintyPct"] == 1.0
    assert parsed["outputTokens"] == 143_000
    assert parsed["agentSteps"] == 166


def test_parse_card_leaves_uncertainty_empty_when_the_card_states_none():
    parsed = build_deepswe.parse_card(card("kimi-k3", pct="69%"))

    assert parsed["uncertaintyPct"] is None
    assert parsed["passAt1Pct"] == 69.0


def test_parse_card_keeps_an_unreadable_token_label_with_no_numeric_value():
    parsed = build_deepswe.parse_card(card("kimi-k3", tokens="n/a"))

    assert parsed["outputTokens"] is None
    assert parsed["outputTokensLabel"] == "n/a"


@pytest.mark.parametrize(
    "lines",
    [
        ["gpt-6-astra", "[high]", "50%", "$1.00", "10k"],  # too few lines to be a card
        ["not-on-the-roster", "[high]", "50%", "$1.00", "10k", "7"],
        ["gpt-6-astra", "high", "50%", "$1.00", "10k", "7"],  # effort not bracketed
        ["gpt-6-astra", "[high]", "50%", "1.00", "10k", "7"],  # cost lacks the dollar sign
        ["gpt-6-astra", "[high]", "50%", "$1.00", "10k", "seven"],  # steps not an integer
    ],
    ids=["too-short", "off-roster", "unbracketed-effort", "undollared-cost", "non-integer-steps"],
)
def test_parse_card_skips_entries_that_are_not_roster_cards(lines):
    assert build_deepswe.parse_card("\n".join(lines)) is None


def test_parse_card_refuses_a_malformed_percentage_instead_of_skipping_the_card():
    with pytest.raises(ValueError, match="invalid DeepSWE percentage: 'fifty'"):
        build_deepswe.parse_card(card("gpt-6-astra", pct="fifty"))


# ---------------------------------------------------------------------------
# main(): ranked roster, summary fields, refusals and printed output
# ---------------------------------------------------------------------------


def test_main_writes_the_ranked_roster_and_its_source_summary(tmp_path):
    source = write_payload(tmp_path / "snap.json", roster_payload())
    output = tmp_path / "deepswe.json"

    assert build_deepswe.main([str(source), str(output)]) == 0

    document = json.loads(output.read_text(encoding="utf-8"))
    assert document["version"] == "v1.1"
    assert document["observedAt"] == "2026-09-29T00:00:00Z"
    assert document["source"] == "https://deepswe.datacurve.ai/"
    assert document["sourceSnapshot"] == str(source)
    assert document["leaderboard"] == "Best"
    assert document["sourceUpdatedOn"] == "September 22, 2026"
    assert (document["tasks"], document["repositories"], document["languages"]) == (113, 91, 5)
    assert document["modelCatalog"] == 28
    assert document["configsShown"] == "57/70"
    assert document["n"] == 21
    assert [model["slug"] for model in document["models"]] == ROSTER
    assert [model["rank"] for model in document["models"]] == list(range(1, 22))
    assert document["models"][0] == {
        "slug": "gpt-6-astra",
        "name": "gpt-6-astra",
        "displayName": "GPT-6 Astra",
        "effort": "high",
        "passRate": 0.5,
        "passAt1Pct": 50.0,
        "uncertaintyPct": None,
        "avgCost": 1.25,
        "outputTokens": 10_000,
        "outputTokensLabel": "10k",
        "agentSteps": 7,
        "source": "DeepSWE Best page card",
        "rank": 1,
    }
    assert output.read_text(encoding="utf-8") == json.dumps(document, indent=2) + "\n"


def test_main_prints_each_model_with_rank_name_pass_rate_price_and_effort(tmp_path, capsys):
    source = write_payload(tmp_path / "snap.json", roster_payload())

    build_deepswe.main([str(source), str(tmp_path / "deepswe.json")])

    summary = json.loads(capsys.readouterr().out)
    assert summary["n"] == 21
    assert summary["sourceUpdatedOn"] == "September 22, 2026"
    assert summary["models"][0] == [1, "GPT-6 Astra", 50.0, 1.25, "high"]
    assert len(summary["models"]) == 21


def test_main_keeps_the_first_card_for_a_repeated_slug_and_ranks_the_rest_consecutively(tmp_path):
    slugs = list(ROSTER)
    slugs[5] = ROSTER[0]
    payload = roster_payload(slugs)
    payload["cards"][5] = card(ROSTER[0], effort="low")
    source = write_payload(tmp_path / "snap.json", payload)
    output = tmp_path / "deepswe.json"

    build_deepswe.main([str(source), str(output)])

    document = json.loads(output.read_text(encoding="utf-8"))
    assert document["n"] == 20
    assert [model["rank"] for model in document["models"]] == list(range(1, 21))
    assert [model["effort"] for model in document["models"] if model["slug"] == ROSTER[0]] == ["high"]
    assert ROSTER[5] not in [model["slug"] for model in document["models"]]


def test_main_ignores_entries_that_are_not_roster_cards(tmp_path):
    cards = [
        "Measuring frontier coding agents on original tasks",
        card("unknown-model"),
        *[card(slug) for slug in ROSTER],
    ]
    source = write_payload(tmp_path / "snap.json", {"cards": cards, "scrapedAt": "2026-09-29T00:00:00Z"})
    output = tmp_path / "deepswe.json"

    build_deepswe.main([str(source), str(output)])

    assert json.loads(output.read_text(encoding="utf-8"))["n"] == 21


@pytest.mark.parametrize(
    ("payload", "parsed"),
    [
        (roster_payload(ROSTER[:20]), 20),
        ({"cards": None}, 0),
    ],
    ids=["twenty-cards", "null-card-list"],
)
def test_main_refuses_any_roster_that_is_not_exactly_twenty_one_and_writes_nothing(tmp_path, payload, parsed):
    source = write_payload(tmp_path / "snap.json", payload)
    output = tmp_path / "deepswe.json"

    with pytest.raises(SystemExit) as refusal:
        build_deepswe.main([str(source), str(output)])

    assert refusal.value.code == f"expected 21 current Best cards, parsed {parsed}"
    assert not output.exists()


def test_main_leaves_summary_fields_null_when_the_capture_has_no_text_sample(tmp_path, pinned_clock):
    source = write_payload(tmp_path / "snap.json", {"cards": [card(slug) for slug in ROSTER]})
    output = tmp_path / "deepswe.json"

    build_deepswe.main([str(source), str(output)])

    document = json.loads(output.read_text(encoding="utf-8"))
    summary_fields = ("sourceUpdatedOn", "tasks", "repositories", "languages", "modelCatalog", "configsShown")
    assert {field: document[field] for field in summary_fields} == dict.fromkeys(summary_fields)


def test_main_stamps_the_pinned_clock_when_the_capture_has_no_scrape_time(tmp_path, pinned_clock):
    # Fallback path: the observation instant uses the same Z-suffixed format as every other stage.
    source = write_payload(tmp_path / "snap.json", {"cards": [card(slug) for slug in ROSTER]})
    output = tmp_path / "deepswe.json"

    build_deepswe.main([str(source), str(output)])

    assert json.loads(output.read_text(encoding="utf-8"))["observedAt"] == "2026-10-17T20:23:57Z"


def test_main_creates_a_missing_output_directory(tmp_path):
    source = write_payload(tmp_path / "snap.json", roster_payload())
    output = tmp_path / "missing" / "nested" / "deepswe.json"

    assert build_deepswe.main([str(source), str(output)]) == 0

    assert output.is_file()


def test_main_reads_its_two_paths_from_the_command_line_when_none_are_passed(tmp_path, monkeypatch):
    source = write_payload(tmp_path / "snap.json", roster_payload())
    output = tmp_path / "deepswe.json"
    monkeypatch.setattr(sys, "argv", ["build_deepswe.py", str(source), str(output)])

    assert build_deepswe.main() == 0

    assert json.loads(output.read_text(encoding="utf-8"))["n"] == 21
