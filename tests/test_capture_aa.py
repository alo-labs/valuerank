"""Behavior tests for the AA payload capture stage (network mocked at urllib)."""

from __future__ import annotations

import hashlib
import json
import runpy
import urllib.error
import urllib.request
from datetime import datetime, timedelta
from pathlib import Path

import pytest

from valuerank import capture_aa as ca

NOW = "2026-10-21T05:24:16Z"  # pinned_clock instant


def _shifted(delta: timedelta) -> str:
    """The pinned instant moved by ``delta``, spelled as an AA observedAt value."""
    moment = datetime.strptime(NOW, "%Y-%m-%dT%H:%M:%SZ") + delta
    return moment.strftime("%Y-%m-%dT%H:%M:%SZ")


PAGE_FIXTURES = Path(__file__).parent / "fixtures" / "aa_pages"


def page_html(model: dict) -> str:
    inner = json.dumps(json.dumps(model))[1:-1]
    return 'x \\"currentModel\\":' + inner + ' y'


class FakeResponse:
    def __init__(self, body: bytes, status=200, content_type="text/html; charset=utf-8"):
        self._body, self.status = body, status
        self.headers = {"Content-Type": content_type} if content_type else {}

    def read(self):
        return self._body

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return False


@pytest.fixture
def net(monkeypatch):
    """Replace urllib.request.urlopen; ``net.pages`` maps URL -> response or exception."""

    class Net:
        pages: dict = {}
        calls: list = []

    state = Net()
    state.pages, state.calls = {}, []

    def fake_urlopen(request, timeout=None):
        state.calls.append((request.full_url, dict(request.header_items()), timeout))
        result = state.pages[request.full_url]
        if isinstance(result, Exception):
            raise result
        return result

    monkeypatch.setattr(urllib.request, "urlopen", fake_urlopen)
    return state


@pytest.fixture
def world(tmp_path, monkeypatch, pinned_clock):
    root = tmp_path / "root"
    aa = root / "data" / "aa"
    aa.mkdir(parents=True)
    monkeypatch.setattr(ca, "ROOT", root)
    monkeypatch.setattr(ca, "AA_DIR", aa)
    monkeypatch.setattr(ca, "EXTRACT_PATH", aa / "aa_extract.json")
    monkeypatch.setattr(ca, "OUTPUT_PATH", aa / "aa_v432_snapshot.json")
    return aa


def entry(model_id="m", **extra):
    return {"id": model_id, "displayName": model_id.upper(), "url": f"https://artificialanalysis.ai/models/{model_id}", **extra}


def preserved(model_id="m", capture=None, **overrides):
    page = {"id": model_id, "url": f"https://artificialanalysis.ai/models/{model_id}", "model": {"slug": model_id},
            "capture": {"observedAt": "2026-10-15T00:00:00Z", "precision": "rounded", "method": "browser"}}
    if capture is not None:
        page["capture"] = capture
    page.update(overrides)
    return page


# --------------------------------------------------------------------------- preserved_public_capture


def test_fresh_preserved_capture_is_reused_unchanged(pinned_clock):
    existing = preserved()
    assert ca.preserved_public_capture(entry(), {"m": existing}) is existing


def test_preserved_capture_accepts_captured_at_when_no_observed_at(pinned_clock):
    existing = preserved(capture={"capturedAt": "2026-10-16T12:00:00+00:00", "precision": "p", "method": "m"})
    assert ca.preserved_public_capture(entry(), {"m": existing}) is existing


def test_preserved_capture_at_exact_age_limit_is_still_fresh(pinned_clock):
    existing = preserved(capture={"observedAt": _shifted(-timedelta(days=7)), "precision": "p", "method": "m"})
    assert ca.preserved_public_capture(entry(), {"m": existing}) is existing  # exactly 7 days


@pytest.mark.parametrize(
    "observed",
    [_shifted(-timedelta(days=7, seconds=1)), _shifted(timedelta(seconds=1))],
)
def test_preserved_capture_outside_window_demands_recapture(pinned_clock, observed):
    existing = preserved(capture={"observedAt": observed, "precision": "p", "method": "m"})
    with pytest.raises(ValueError, match=r"older than 7 days or future-dated.*requires a public rendered capture"):
        ca.preserved_public_capture(entry(), {"m": existing})


@pytest.mark.parametrize(
    "existing",
    [
        None,
        "not a dict",
        preserved(url="https://artificialanalysis.ai/models/other"),
        preserved(capture="not a dict"),
        preserved(capture={"precision": "p", "method": "m"}),
        preserved(capture={"observedAt": "2026-10-15T00:00:00Z", "method": "m"}),
        preserved(capture={"observedAt": "2026-10-15T00:00:00Z", "precision": "p"}),
        preserved(model="nope"),
        preserved(model={"name": "no slug"}),
        preserved(capture={"observedAt": "garbage", "precision": "p", "method": "m"}),
        preserved(capture={"observedAt": 12345, "precision": "p", "method": "m"}),
    ],
)
def test_unusable_preserved_records_demand_a_public_recapture(pinned_clock, existing):
    with pytest.raises(ValueError, match="m requires a public rendered capture in the built-in browser"):
        ca.preserved_public_capture(entry(), {"m": existing} if existing is not None else {})


def test_missing_capture_block_demands_recapture(pinned_clock):
    existing = preserved()
    existing["capture"] = None
    with pytest.raises(ValueError, match="requires a public rendered capture"):
        ca.preserved_public_capture(entry(), {"m": existing})


def test_timezone_naive_capture_date_is_rejected_with_cause(pinned_clock):
    existing = preserved(capture={"observedAt": "2026-10-15T00:00:00", "precision": "p", "method": "m"})
    with pytest.raises(ValueError, match="requires a public rendered capture") as info:
        ca.preserved_public_capture(entry(), {"m": existing})
    assert str(info.value.__cause__) == "capture date requires a timezone"


# --------------------------------------------------------------------------- capture


def test_capture_fetches_and_decodes_page(net):
    body = page_html({"slug": "m", "intelligenceIndex": 50}).encode()
    net.pages["https://artificialanalysis.ai/models/m"] = FakeResponse(body)
    result = ca.capture(entry(), {})
    assert result == {
        "id": "m", "requestedName": "M", "url": "https://artificialanalysis.ai/models/m",
        "model": {"slug": "m", "intelligenceIndex": 50},
        "capture": {"status": 200, "contentType": "text/html; charset=utf-8", "responseBytes": len(body),
                    "responseSha256": hashlib.sha256(body).hexdigest()},
    }
    url, headers, timeout = net.calls[0]
    assert url == "https://artificialanalysis.ai/models/m" and timeout == 45
    assert headers["User-agent"] == "ValueRank/1.6 official-source-refresh"


def test_capture_defaults_missing_content_type_to_empty(net):
    net.pages["https://artificialanalysis.ai/models/m"] = FakeResponse(
        page_html({"slug": "m"}).encode(), content_type=None)
    result = ca.capture({"id": "m", "url": "https://artificialanalysis.ai/models/m"}, {})
    assert result["capture"]["contentType"] == "" and result["requestedName"] is None


def test_capture_replaces_undecodable_bytes_before_decoding(net):
    body = b"\xff" + page_html({"slug": "m"}).encode()
    net.pages["https://artificialanalysis.ai/models/m"] = FakeResponse(body)
    assert ca.capture(entry(), {})["capture"]["responseBytes"] == len(body)


def test_capture_public_rendered_uses_preserved_record_without_network(net, pinned_clock):
    existing = preserved()
    assert ca.capture(entry(captureMode="public-rendered"), {"m": existing}) is existing
    assert net.calls == []


def test_capture_public_rendered_without_record_raises(net, pinned_clock):
    with pytest.raises(ValueError, match="requires a public rendered capture"):
        ca.capture(entry(captureMode="public-rendered"), {})


def test_capture_surfaces_http_failures(net):
    net.pages["https://artificialanalysis.ai/models/m"] = urllib.error.HTTPError(
        "https://artificialanalysis.ai/models/m", 503, "unavailable", {}, None)
    with pytest.raises(urllib.error.HTTPError):
        ca.capture(entry(), {})


def test_capture_rejects_page_without_a_model_object(net):
    net.pages["https://artificialanalysis.ai/models/m"] = FakeResponse(b"<html>blocked</html>")
    with pytest.raises(ValueError, match="no full model object for slug 'm'"):
        ca.capture(entry(), {})


def fixture_page(*names: str) -> bytes:
    return "".join((PAGE_FIXTURES / name).read_text() for name in names).encode()


@pytest.mark.parametrize("suffix", ["", "/"])
def test_capture_decodes_current_pages_that_lack_the_legacy_marker(net, suffix):
    slug = "claude-haiku-5-5-xhigh"
    url = f"https://artificialanalysis.ai/models/{slug}{suffix}"
    body = fixture_page("haiku-xhigh-full.txt", "haiku-xhigh-decoy.txt")
    net.pages[url] = FakeResponse(body)
    result = ca.capture({"id": "claude-haiku-5-5", "displayName": "Claude Haiku 5.5", "url": url}, {})
    assert result["id"] == "claude-haiku-5-5" and result["requestedName"] == "Claude Haiku 5.5"
    assert result["url"] == url  # recorded exactly as requested
    assert set(result) == {"id", "requestedName", "url", "model", "capture"}
    model = result["model"]
    assert model["slug"] == slug and model["effort"]["slug"] == "xhigh"
    assert model["intelligenceIndexCost"]["total"] == pytest.approx(157.5758646895501)
    assert result["capture"]["responseBytes"] == len(body)


def test_capture_uses_the_url_slug_to_pick_the_page_model(net):
    url = "https://artificialanalysis.ai/models/gpt-6-luna"
    net.pages[url] = FakeResponse(fixture_page("gpt-6-luna-decoy.txt", "gpt-6-luna-full.txt"))
    model = ca.capture({"id": "gpt-6-luna", "url": url}, {})["model"]
    assert model["name"] == "GPT-6 Luna (Max)"
    other = "https://artificialanalysis.ai/models/gpt-6-sol"
    net.pages[other] = FakeResponse(fixture_page("gpt-6-luna-decoy.txt", "gpt-6-luna-full.txt"))
    with pytest.raises(ValueError, match="no full model object for slug 'gpt-6-sol'"):
        ca.capture({"id": "gpt-6-sol", "url": other}, {})


def test_capture_still_reads_pages_that_keep_the_legacy_marker(net):
    url = "https://artificialanalysis.ai/models/mimo-v2-6-pro"
    net.pages[url] = FakeResponse(fixture_page("mimo-v2-6-pro-full.txt"))
    model = ca.capture({"id": "mimo-v2-6-pro", "url": url}, {})["model"]
    assert model["name"] == "MiMo-V2.6-Pro" and "effort" not in model


# --------------------------------------------------------------------------- main


def write_extract(aa, entries):
    (aa / "aa_extract.json").write_text(json.dumps(entries))


def test_main_writes_snapshot_with_expected_shape(world, net, capsys):
    write_extract(world, [entry("a"), entry("b")])
    for key in ("a", "b"):
        net.pages[f"https://artificialanalysis.ai/models/{key}"] = FakeResponse(page_html({"slug": key}).encode())
    assert ca.main() == 0
    document = json.loads((world / "aa_v432_snapshot.json").read_text())
    assert document["schemaVersion"] == "valuerank-aa-page-snapshot/v2"
    assert document["benchmarkVersion"] == "Artificial Analysis Intelligence Index v4.3.2"
    assert document["capturedAt"] == NOW and document["concurrency"] == 4
    assert document["source"].endswith("/evaluations/artificial-analysis-intelligence-index")
    assert [page["id"] for page in document["pages"]] == ["a", "b"]  # input order preserved
    assert document["pages"][0]["model"] == {"slug": "a"}
    printed = json.loads(capsys.readouterr().out)
    assert printed == {"models": 2, "uniqueIds": 2, "benchmarkVersion": document["benchmarkVersion"],
                       "capturedAt": NOW, "output": "data/aa/aa_v432_snapshot.json"}


def test_main_keeps_fresh_public_record_from_stored_snapshot(world, net):
    write_extract(world, [entry("a"), entry("p", captureMode="public-rendered")])
    existing = preserved("p")
    (world / "aa_v432_snapshot.json").write_text(json.dumps({"pages": [existing]}))
    net.pages["https://artificialanalysis.ai/models/a"] = FakeResponse(page_html({"slug": "a"}).encode())
    assert ca.main() == 0
    pages = json.loads((world / "aa_v432_snapshot.json").read_text())["pages"]
    assert pages[1] == existing
    assert [call[0] for call in net.calls] == ["https://artificialanalysis.ai/models/a"]


def test_main_stale_public_record_fails_before_any_network_request(world, net):
    write_extract(world, [entry("a"), entry("p", captureMode="public-rendered")])
    stale = preserved("p", capture={"observedAt": "2026-09-01T00:00:00Z", "precision": "p", "method": "m"})
    original = json.dumps({"pages": [stale]})
    (world / "aa_v432_snapshot.json").write_text(original)
    with pytest.raises(ValueError, match="older than 7 days"):
        ca.main()
    assert net.calls == []
    assert (world / "aa_v432_snapshot.json").read_text() == original  # previous snapshot untouched


def test_main_http_failure_aborts_without_overwriting_snapshot(world, net):
    write_extract(world, [entry("a"), entry("b")])
    net.pages["https://artificialanalysis.ai/models/a"] = FakeResponse(page_html({"slug": "a"}).encode())
    net.pages["https://artificialanalysis.ai/models/b"] = urllib.error.URLError("boom")
    with pytest.raises(urllib.error.URLError):
        ca.main()
    assert not (world / "aa_v432_snapshot.json").exists()


@pytest.mark.parametrize("entries", [[], [entry("a"), entry("a")]])
def test_main_requires_nonempty_unique_cohort(world, net, entries):
    write_extract(world, entries)
    with pytest.raises(ValueError, match="non-empty cohort of unique selected URLs"):
        ca.main()


def test_main_tolerates_non_object_stored_snapshot(world, net):
    write_extract(world, [entry("a")])
    (world / "aa_v432_snapshot.json").write_text("[]")
    net.pages["https://artificialanalysis.ai/models/a"] = FakeResponse(page_html({"slug": "a"}).encode())
    assert ca.main() == 0
    assert json.loads((world / "aa_v432_snapshot.json").read_text())["pages"][0]["id"] == "a"


def test_module_guard_exits_with_main_status(tmp_path, monkeypatch, pinned_clock, net):
    root = tmp_path / "root"
    aa = root / "data" / "aa"
    aa.mkdir(parents=True)
    write_extract(aa, [entry("a")])
    net.pages["https://artificialanalysis.ai/models/a"] = FakeResponse(page_html({"slug": "a"}).encode())
    import valuerank.paths as paths

    monkeypatch.setattr(paths, "ROOT", root)
    monkeypatch.setattr(paths, "DATA", root / "data")
    with pytest.warns(RuntimeWarning), pytest.raises(SystemExit) as exit_info:
        runpy.run_module("valuerank.capture_aa", run_name="__main__", alter_sys=True)
    assert exit_info.value.code == 0
    assert json.loads((aa / "aa_v432_snapshot.json").read_text())["pages"][0]["model"] == {"slug": "a"}
