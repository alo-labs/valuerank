"""Behavior tests for the AA model-page decoder and metrics/coverage builder."""

from __future__ import annotations

import json
import runpy
from pathlib import Path

import pytest

from valuerank import build_aa_metrics as bam

FIXTURES = Path(__file__).parent / "fixtures" / "aa"
PAGE_FIXTURES = Path(__file__).parent / "fixtures" / "aa_pages"
VERSION = "Artificial Analysis Intelligence Index v4.3.2"


def escaped_payload(model: dict) -> str:
    """Render ``model`` the way an AA page embeds it: JSON inside a JSON string."""

    inner = json.dumps(json.dumps(model))[1:-1]
    return 'prefix <script>self.__next_f.push([1,"x\\"currentModel\\":' + inner + ',\\"after\\":1"])</script>'


# --------------------------------------------------------------------------- helpers


def test_json_value_walks_dotted_paths_and_tolerates_non_dicts():
    obj = {"a": {"b": {"c": 5}}, "flat": 1}
    assert bam.json_value(obj, "a.b.c") == 5
    assert bam.json_value(obj, "a.x") is None
    assert bam.json_value(obj, "flat.deeper") is None  # int is not traversable


@pytest.mark.parametrize(
    "value, expected",
    [(None, None), (True, True), (3, 3.0), (2.5, 2.5), ("7", None), ([1], None)],
)
def test_clean_number_keeps_null_and_bools_and_drops_strings(value, expected):
    result = bam.clean_number(value)
    assert result == expected
    assert type(result) is type(expected)


def test_summary_speed_reads_model_summary_value():
    text = (FIXTURES / "model-summary.txt").read_text()
    assert bam.summary_speed(text) == 87.5


@pytest.mark.parametrize("label", ["N/A", "Unknown", "n/a"])
def test_summary_speed_preserves_unavailable_as_null_not_zero(label):
    assert bam.summary_speed(f"Model summary\nSpeed {label} Output tokens per second") is None


def test_summary_speed_without_match_is_null_and_ignores_text_before_summary():
    assert bam.summary_speed("Speed 99 Output tokens per second\nModel summary\nnothing here") is None
    assert bam.summary_speed("no summary heading at all") is None
    assert bam.summary_speed("Model summary Speed 1.5e1 Output tokens per second") == 15.0


# --------------------------------------------------------------------------- decode_current_model


def test_decode_current_model_returns_embedded_object():
    model = {"slug": "m-1", "intelligenceIndex": 61.2, "effort": {"slug": "high"}}
    assert bam.decode_current_model(escaped_payload(model)) == model


def test_decode_rejects_page_without_marker():
    with pytest.raises(ValueError, match="marker not found"):
        bam.decode_current_model("<html>nothing</html>")


def test_decode_rejects_unterminated_object():
    html = 'x \\"currentModel\\":{\\"slug\\":\\"a\\"'
    with pytest.raises(ValueError, match="unterminated"):
        bam.decode_current_model(html)


@pytest.mark.parametrize("body", ["{x}", "{\\q}"])
def test_decode_rejects_undecodable_json(body):
    with pytest.raises(ValueError, match="JSON decode failed"):
        bam.decode_current_model('\\"currentModel\\":' + body)


def test_decode_rejects_model_without_slug():
    with pytest.raises(ValueError, match="no slug"):
        bam.decode_current_model(escaped_payload({"name": "no slug"}))


# --------------------------------------------------------------------------- decode_page_model


def page_fixture(name: str) -> str:
    """Real excerpt cut from an AA model page (JSON-escaped flight payload)."""

    return (PAGE_FIXTURES / name).read_text()


def test_page_slug_is_the_last_url_path_segment_with_or_without_trailing_slash():
    assert bam.page_slug("https://artificialanalysis.ai/models/claude-haiku-5-5-xhigh") == "claude-haiku-5-5-xhigh"
    assert bam.page_slug("https://artificialanalysis.ai/models/claude-haiku-5-5-xhigh/") == "claude-haiku-5-5-xhigh"
    assert bam.page_slug("https://artificialanalysis.ai/models/m?tab=x#top") == "m"


def test_decode_page_model_reads_slug_keyed_object_from_page_without_legacy_marker():
    html = page_fixture("haiku-xhigh-full.txt") + page_fixture("haiku-xhigh-decoy.txt")
    assert bam.LEGACY_MARKER not in html
    model = bam.decode_page_model(html, "claude-haiku-5-5-xhigh")
    assert model["slug"] == "claude-haiku-5-5-xhigh"
    assert model["name"] == "Claude Haiku 5.5 (Xhigh)"
    assert model["effort"]["slug"] == "xhigh"
    assert model["intelligenceIndex"] == pytest.approx(41.2489304677024)
    assert model["intelligenceIndexCost"]["total"] == pytest.approx(157.5758646895501)
    assert len(model) == 91


def test_decode_page_model_ignores_decoys_before_after_and_nested_slug_mentions():
    # GPT-6 Luna's page also carries a ``currentRelease`` object (slug + index, no cost)
    # and its own release block inside the model; neither may be mistaken for the model.
    html = page_fixture("gpt-6-luna-decoy.txt") + page_fixture("gpt-6-luna-full.txt")
    model = bam.decode_page_model(html, "gpt-6-luna")
    assert model["name"] == "GPT-6 Luna (Max)" and model["effort"]["slug"] == "max"
    assert model["intelligenceIndexCost"]["total"] == pytest.approx(122.05438368649308)
    assert model["release"]["slug"] == "gpt-6-luna"


def test_decode_page_model_accepts_identical_duplicate_objects():
    full = page_fixture("haiku-xhigh-full.txt")
    model = bam.decode_page_model(full + full, "claude-haiku-5-5-xhigh")
    assert model == bam.decode_page_model(full, "claude-haiku-5-5-xhigh")


def test_decode_page_model_matches_legacy_extraction_where_the_marker_exists():
    html = page_fixture("mimo-v2-6-pro-full.txt")
    assert bam.LEGACY_MARKER in html
    model = bam.decode_page_model(html, "mimo-v2-6-pro")
    assert model == bam.decode_current_model(html)
    assert model["intelligenceIndex"] == pytest.approx(46.3242065310383)


def test_decode_page_model_falls_back_to_legacy_marker_for_objects_without_cost():
    model = {"slug": "m", "intelligenceIndex": 50}
    assert bam.decode_page_model(escaped_payload(model), "m") == model


def test_decode_page_model_prefers_slug_keyed_object_over_a_marker_for_another_slug():
    html = escaped_payload({"slug": "other", "intelligenceIndex": 1}) + page_fixture("haiku-xhigh-full.txt")
    model = bam.decode_page_model(html, "claude-haiku-5-5-xhigh")
    assert model["slug"] == "claude-haiku-5-5-xhigh"


def test_decode_page_model_rejects_marker_object_for_a_different_slug():
    with pytest.raises(ValueError, match="currentModel slug 'other' does not match page slug 'm'"):
        bam.decode_page_model(escaped_payload({"slug": "other"}), "m")


def test_decode_page_model_propagates_legacy_marker_without_slug():
    with pytest.raises(ValueError, match="no slug"):
        bam.decode_page_model(escaped_payload({"name": "no slug"}), "m")


def test_decode_page_model_rejects_decoy_only_page():
    html = page_fixture("haiku-xhigh-decoy.txt") + page_fixture("gpt-6-luna-decoy.txt")
    with pytest.raises(ValueError, match="no full model object for slug 'claude-haiku-5-5-xhigh'"):
        bam.decode_page_model(html, "claude-haiku-5-5-xhigh")


def test_decode_page_model_ignores_slug_mention_outside_any_object():
    with pytest.raises(ValueError, match="no full model object for slug 'm'"):
        bam.decode_page_model('\\"slug\\":\\"m\\"', "m")


def test_decode_page_model_rejects_page_without_any_slug_mention():
    with pytest.raises(ValueError, match="no full model object for slug 'm'"):
        bam.decode_page_model("<html>blocked</html>", "m")


def compact_escaped(model: dict) -> str:
    """The model as the flight payload spells it: compact JSON, then JSON-string escaped."""

    return json.dumps(json.dumps(model, separators=(",", ":")))[1:-1]


def full_object(slug: str, **changes) -> str:
    return compact_escaped({"slug": slug, "intelligenceIndex": 10, "intelligenceIndexCost": {"total": 5}, **changes})


def test_decode_page_model_rejects_disagreeing_full_objects():
    html = "a" + full_object("m") + "b" + full_object("m", intelligenceIndex=11)
    with pytest.raises(ValueError, match="full model objects for slug 'm' disagree"):
        bam.decode_page_model(html, "m")


def test_decode_page_model_rejects_keyed_object_disagreeing_with_legacy_marker():
    marker_object = compact_escaped({"slug": "m", "intelligenceIndex": 99})
    html = '\\"currentModel\\":' + marker_object + "," + full_object("m")
    with pytest.raises(ValueError, match="full model objects for slug 'm' disagree"):
        bam.decode_page_model(html, "m")


@pytest.mark.parametrize(
    "fragment",
    [
        '{\\"slug\\":\\"m\\",\\"intelligenceIndexCost\\":{',  # never closed
        '{\\"slug\\":\\"m\\",\\"intelligenceIndexCost\\":\\q}',  # invalid JSON string escape
        '{\\"slug\\":\\"m\\",\\"intelligenceIndexCost\\":x}',  # invalid JSON document
    ],
)
def test_decode_page_model_skips_undecodable_candidates(fragment):
    with pytest.raises(ValueError, match="no full model object for slug 'm'"):
        bam.decode_page_model(fragment, "m")
    # ...but still finds a good object elsewhere on the same page.
    assert bam.decode_page_model(fragment + full_object("m"), "m")["intelligenceIndex"] == 10


# --------------------------------------------------------------------------- selected_page


@pytest.fixture
def aa_dir(tmp_path, monkeypatch):
    directory = tmp_path / "aa"
    directory.mkdir()
    monkeypatch.setattr(bam, "AA_DIR", directory)
    return directory


ENTRY = {"id": "e1", "url": "https://artificialanalysis.ai/models/the-slug/"}


def test_selected_page_prefers_exact_names(aa_dir):
    for suffix in ("html", "txt"):
        (aa_dir / f"e1__the-slug.{suffix}").write_text("x")
        (aa_dir / f"e1__the-slug-extra.{suffix}").write_text("y")
    slug, html, text = bam.selected_page(ENTRY)
    assert slug == "the-slug"
    assert html.name == "e1__the-slug.html" and text.name == "e1__the-slug.txt"


def test_selected_page_falls_back_to_first_sorted_glob_match(aa_dir):
    for name in ("e1__the-slug-b", "e1__the-slug-a"):
        (aa_dir / f"{name}.html").write_text("x")
        (aa_dir / f"{name}.txt").write_text("x")
    _, html, text = bam.selected_page(ENTRY)
    assert html.name == "e1__the-slug-a.html" and text.name == "e1__the-slug-a.txt"


def test_selected_page_mixes_exact_html_with_glob_text(aa_dir):
    (aa_dir / "e1__the-slug.html").write_text("x")
    (aa_dir / "e1__the-slug-max.txt").write_text("x")
    _, html, text = bam.selected_page(ENTRY)
    assert html.name == "e1__the-slug.html" and text.name == "e1__the-slug-max.txt"


def test_selected_page_missing_html_raises(aa_dir):
    (aa_dir / "e1__the-slug.txt").write_text("x")
    with pytest.raises(FileNotFoundError, match="raw page snapshot missing for e1"):
        bam.selected_page(ENTRY)


def test_selected_page_missing_text_raises(aa_dir):
    (aa_dir / "e1__the-slug.html").write_text("x")
    with pytest.raises(FileNotFoundError, match="raw page snapshot missing for e1"):
        bam.selected_page(ENTRY)


# --------------------------------------------------------------------------- main


@pytest.fixture
def world(tmp_path, monkeypatch, pinned_clock):
    """A temporary repository root wired into the module's path constants."""

    root = tmp_path / "root"
    data = root / "data"
    (data / "aa").mkdir(parents=True)
    paths = {
        "ROOT": root,
        "DATA": data,
        "AA_DIR": data / "aa",
        "MAPPING_PATH": data / "aa_mapping.json",
        "EXTRACT_PATH": data / "aa" / "aa_extract.json",
        "SNAPSHOT_PATH": data / "aa" / "aa_v432_snapshot.json",
        "OUTPUT_PATH": data / "aa_metrics.json",
        "COVERAGE_PATH": data / "coverage_matrix.json",
    }
    for name, value in paths.items():
        monkeypatch.setattr(bam, name, value)

    class World:
        pass

    w = World()
    w.root, w.data, w.paths = root, data, paths

    def write(mapping=(), extract=(), claims=(), snapshot=None, policy="policy-text"):
        w.paths["MAPPING_PATH"].write_text(json.dumps(list(mapping)))
        w.paths["EXTRACT_PATH"].write_text(json.dumps(list(extract)))
        (data / "provider_claims.json").write_text(json.dumps({"policy": policy, "claims": list(claims)}))
        if snapshot is not None:
            w.paths["SNAPSHOT_PATH"].write_text(json.dumps(snapshot))

    def page(entry_id, slug, model, speed_text=None):
        (data / "aa" / f"{entry_id}__{slug}.html").write_text(escaped_payload(model))
        (data / "aa" / f"{entry_id}__{slug}.txt").write_text(
            speed_text if speed_text is not None else "Model summary\nSpeed 42 Output tokens per second\n"
        )

    def run():
        assert bam.main() == 0
        return (
            json.loads(w.paths["OUTPUT_PATH"].read_text()),
            json.loads(w.paths["COVERAGE_PATH"].read_text()),
        )

    w.write, w.page, w.run = write, page, run
    return w


def entry(model_id, slug=None, name=None, **extra):
    slug = slug or model_id
    return {"id": model_id, "displayName": name or model_id.upper(), "url": f"https://artificialanalysis.ai/models/{slug}", **extra}


def test_main_decodes_html_pages_into_metrics_with_units_and_nulls(world, capsys):
    world.write(
        mapping=[{"id": "full", "displayName": "Mapped Full", "aaSlug": "full", "aaVariant": "max"}],
        extract=[entry("full", name="Raw Full", captureMode="html")],
    )
    world.page("full", "full", {
        "slug": "full", "name": "Full (Max)", "shortName": "Full", "release": "2026-07", "isReasoning": True,
        "effort": {"slug": "max"}, "intelligenceIndex": 61, "gdpval": 1500, "lcr": 0.5, "hle": 0.25,
        "gpqa": 0.9, "scicode": 0.4, "critpt": 0.1, "gdpPdfAllPass": 0.3, "terminalBench40": 0.6,
        "automationBenchPartialScore": 0.2, "gdpvalNormalizedDisplay": 0.5,
        "briefcaseBreakdown": {"overall": {"elo": 1500}, "rubricPassRate": 0.8, "totalCost": 12.5},
        "omniscienceBreakdown": {"accuracy": 0.4, "hallucinationRate": 0.3},
        "intelligenceIndexCost": {"total": 99.5}, "mmmuPro": 0.7, "tauBanking": 0.2,
        "terminalBenchV21": 0.33,
    })
    output, coverage = world.run()
    model = output["models"]["full"]
    metrics = model["metrics"]
    assert model["displayName"] == "Mapped Full" and model["family"] == "Mapped Full"  # family defaults to the name
    assert (model["aaSlug"], model["aaName"], model["aaShortName"], model["aaVariant"]) == ("full", "Full (Max)", "Full", "max")
    assert model["release"] == "2026-07" and model["isReasoning"] is True
    assert metrics["intelligenceIndex"] == 61.0
    assert metrics["briefcaseElo"] == 1500.0
    assert metrics["briefcaseNormalized"] == pytest.approx(0.5)  # (1500-500)/2000
    assert metrics["gdpvalV21"] == 1500.0 and metrics["gdpvalV21Normalized"] == 0.5
    assert metrics["omniAccuracy"] == 0.4
    assert metrics["omniNonHallucination"] == pytest.approx(0.7)  # 1 - hallucination rate
    assert metrics["aaEvalCost"] == 99.5
    assert metrics["speed"] == 42.0
    assert metrics["terminalBenchV40"] == 0.6 and metrics["aaLcr"] == 0.5 and metrics["gpqaDiamond"] == 0.9
    assert model["supplemental"]["mmmuPro"] == 0.7
    assert model["supplemental"]["briefcaseElo"] == 1500.0
    assert model["supplemental"]["briefcaseRubricPassRate"] == 0.8
    assert model["supplemental"]["briefcaseTotalCost"] == 12.5
    assert model["supplemental"]["tauBanking"] == 0.2 and model["supplemental"]["terminalBenchV21"] == 0.33
    assert model["supplemental"]["livecodebench"] is None  # absent stays null, not 0
    assert model["intelligenceIndexStatus"] == "measured"
    source = model["metricSources"]["intelligenceIndex"]
    assert source == {"sourceType": "benchmark_owner", "sourceUrl": "https://artificialanalysis.ai/models/full",
                      "observedAt": None, "precision": None}
    extraction = model["extraction"]
    assert extraction["htmlSnapshot"] == "data/aa/full__full.html"
    assert extraction["textSnapshot"] == "data/aa/full__full.txt"
    assert extraction["sourceSnapshot"] is None and extraction["captureMode"] == "html"
    assert extraction["method"] == "decoded currentModel object from first-party page payload"
    assert output["sourceSnapshot"] is None and output["observedAt"] == "2026-10-21T05:24:16Z"
    assert output["benchmarkVersion"] == VERSION and output["providerClaimPolicy"] == "policy-text"
    assert coverage["cohortN"] == 1 and coverage["cohort"].endswith("1-model ValueRank comparison roster")
    assert coverage["sourceSnapshot"] is None
    printed = json.loads(capsys.readouterr().out)
    assert printed["models"] == 1 and printed["primaryFields"] == 14 and printed["additionalFields"] == 3
    assert printed["outputs"] == ["data/aa_metrics.json", "data/coverage_matrix.json"]


def test_main_decodes_markerless_html_page_through_its_slug_keyed_object(world):
    world.write(
        mapping=[{"id": "haiku", "displayName": "Haiku (xhigh)", "family": "Claude Haiku 5.5", "aaSlug": "claude-haiku-5-5-xhigh", "aaVariant": "xhigh"}],
        extract=[entry("haiku", slug="claude-haiku-5-5-xhigh")],
    )
    slug = "claude-haiku-5-5-xhigh"
    (world.data / "aa" / f"haiku__{slug}.html").write_text(
        page_fixture("haiku-xhigh-full.txt") + page_fixture("haiku-xhigh-decoy.txt"))
    (world.data / "aa" / f"haiku__{slug}.txt").write_text("Model summary\nSpeed 195.3 Output tokens per second\n")
    output, _ = world.run()
    model = output["models"]["haiku"]
    metrics = model["metrics"]
    assert (model["aaSlug"], model["aaName"], model["aaVariant"]) == (slug, "Claude Haiku 5.5 (Xhigh)", "xhigh")
    assert (model["displayName"], model["family"]) == ("Haiku (xhigh)", "Claude Haiku 5.5")  # O33: a sibling's AA family
    assert model["release"] == {"slug": "claude-haiku-5-5", "name": "Claude Haiku 5.5", "deprecatedTo": None}
    assert metrics["intelligenceIndex"] == pytest.approx(41.2489304677024)
    assert metrics["aaEvalCost"] == pytest.approx(157.5758646895501)
    assert metrics["speed"] == 195.3  # raw-HTML mode keeps reading the page's visible summary text
    assert model["intelligenceIndexStatus"] == "measured"
    # Every retained ranking dimension is read from the new object, none silently null.
    assert metrics["briefcaseElo"] == 1531.52 and metrics["briefcaseNormalized"] == pytest.approx((1531.52 - 500) / 2000)
    assert metrics["gdpvalV21"] == 1513.05 and metrics["gdpvalV21Normalized"] == 0.506525
    assert metrics["automationBenchAA"] == pytest.approx(0.35953889773428194)
    assert metrics["terminalBenchV40"] == pytest.approx(0.292929292929293)
    assert metrics["scicode"] == pytest.approx(0.517361111111111) and metrics["hle"] == pytest.approx(0.42678405931418)
    assert metrics["gdpPdfAllPass"] == 0.182 and metrics["critpt"] == pytest.approx(0.225714285714286)
    assert metrics["omniAccuracy"] == 0.3495
    assert metrics["omniNonHallucination"] == pytest.approx(1 - 0.44427363566487316)
    assert metrics["aaLcr"] == pytest.approx(0.783333333333333)
    assert metrics["gpqaDiamond"] is None  # AA publishes gpqa: null for this model; legacy field, not ranked


def test_main_snapshot_speed_comes_from_output_speed_variance_median_of_a_decoded_page(world):
    """AA pages carry no ``speed`` key; the headline speed is ``outputSpeedVariance.median``.

    On the saved pages that median equals ``performanceByPromptType.long.medianOutputSpeed``.
    """

    slug = "claude-haiku-5-5-xhigh"
    decoded = bam.decode_page_model(page_fixture("haiku-xhigh-full.txt"), slug)
    assert "speed" not in decoded
    assert decoded["outputSpeedVariance"]["median"] == decoded["performanceByPromptType"]["long"]["medianOutputSpeed"]
    world.write(extract=[entry("haiku", slug=slug)], snapshot={"pages": [snapshot_page("haiku", decoded, {})]})
    output, _ = world.run()
    assert output["models"]["haiku"]["metrics"]["speed"] == pytest.approx(195.273087468701)


def test_main_alternate_field_names_and_estimated_index(world):
    world.write(extract=[entry("alt")])
    world.page("alt", "alt", {
        "slug": "alt", "effort": {"slug": "std"}, "intelligenceIndex": 50, "intelligenceIndexIsEstimated": True,
        "briefcaseElo": 1000, "briefcaseNormalizedDisplay": 0.9, "gdpvalNormalized": 0.25,
        "terminalbench40": 0.45, "omniscienceAccuracy": 0.55, "omniscienceNonHallucination": 0.8,
        "aaEvalCost": 7, "speed": "fast", "terminalbenchV21": 0.12, "gpqa": "oops",
        "briefcaseBreakdown": {"overall": {"elo": 2000}},
    }, speed_text="Model summary\nSpeed N/A Output tokens per second")
    output, _ = world.run()
    model = output["models"]["alt"]
    metrics = model["metrics"]
    assert model["displayName"] == "ALT"  # falls back to the extract entry name without a mapping
    assert metrics["briefcaseElo"] == 1000.0  # direct field wins over breakdown
    assert metrics["briefcaseNormalized"] == 0.9  # displayed value wins over derived Elo normalisation
    assert metrics["gdpvalV21Normalized"] == 0.25
    assert metrics["terminalBenchV40"] == 0.45
    assert metrics["omniAccuracy"] == 0.55 and metrics["omniNonHallucination"] == 0.8
    assert metrics["aaEvalCost"] == 7.0
    assert metrics["speed"] is None  # HTML mode reads the summary text, which says N/A
    assert metrics["gpqaDiamond"] is None  # strings are dropped, never coerced
    assert model["supplemental"]["terminalBenchV21"] == 0.12
    assert model["intelligenceIndexStatus"] == "estimated"
    assert model["metricSources"]["intelligenceIndex"]["sourceType"] == "benchmark_owner_estimate"
    assert model["metricSources"]["intelligenceIndex"]["status"] == "estimated"
    assert "speed" not in model["metricSources"]


def test_main_hallucination_rate_fallbacks_and_missing_values(world):
    world.write(extract=[entry("rate"), entry("flat"), entry("none")])
    world.page("rate", "rate", {"slug": "rate", "omniscienceHallucinationRate": 0.25})
    world.page("flat", "flat", {"slug": "flat", "omniscienceBreakdown": {"hallucinationRate": 0.1}})
    world.page("none", "none", {"slug": "none"})
    output, coverage = world.run()
    models = output["models"]
    assert models["rate"]["metrics"]["omniNonHallucination"] == 0.75
    assert models["flat"]["metrics"]["omniNonHallucination"] == pytest.approx(0.9)
    assert models["none"]["metrics"]["omniNonHallucination"] is None
    assert models["none"]["intelligenceIndexStatus"] == "missing"
    assert models["none"]["aaVariant"] is None
    assert list(models["none"]["metricSources"]) == ["speed"]  # only the summary-text speed exists
    # Coverage counts and the primary-score gate.
    field = coverage["fields"]["omniNonHallucination"]
    assert (field["availableN"], field["cohortN"], field["coveragePct"]) == (2, 3, 66.67)
    assert field["missingModels"] == ["none"] and field["includedInPrimaryScore"] is False
    assert coverage["fields"]["hle"]["group"] == "primary"
    assert coverage["fields"]["gpqaDiamond"]["group"] == "additional"
    assert coverage["fields"]["mmmuPro"]["group"] == "supplemental"
    assert coverage["fields"]["speed"]["availableN"] == 3  # summary text speed present for every html page


def test_main_primary_field_included_only_when_every_model_has_it(world):
    world.write(extract=[entry("a"), entry("b")])
    world.page("a", "a", {"slug": "a", "hle": 0.2, "scicode": 0.1})
    world.page("b", "b", {"slug": "b", "hle": 0.3})
    _, coverage = world.run()
    assert coverage["fields"]["hle"]["includedInPrimaryScore"] is True
    assert coverage["fields"]["hle"]["coveragePct"] == 100.0
    assert coverage["fields"]["scicode"]["includedInPrimaryScore"] is False
    assert coverage["fields"]["scicode"]["missingModels"] == ["b"]


def claim(key, value=0.5, **overrides):
    base = {"claimId": f"c-{key}", "cohortModelId": "m", "componentKey": key, "value": value,
            "eligibleForRanking": True, "benchmarkVersion": VERSION, "providerVariant": "max",
            "sourceUrl": "https://provider.example/claim"}
    base.update(overrides)
    return base


def test_main_provider_claims_fill_only_exactly_eligible_missing_metrics(world):
    claims = [
        claim("hle", 0.77),
        {**claim("critpt", 0.4), "componentKey": None, "component": "critpt"},
        claim("scicode", 0.3, benchmarkVersion="Artificial Analysis Intelligence Index v4.2"),
        claim("aaLcr", 0.3, providerVariant="high"),
        claim("gdpvalV21", 0.3, eligibleForRanking=False),
        claim("gpqaDiamond", "0.3"),
        claim("notAMetric", 0.3),
        claim("intelligenceIndex", 99),  # already measured by AA: provider claim must not override
        claim("terminalBenchV40", 0.3, cohortModelId="other"),
    ]
    world.write(extract=[entry("m")], claims=claims)
    world.page("m", "m", {"slug": "m", "effort": {"slug": "max"}, "intelligenceIndex": 55})
    output, coverage = world.run()
    model = output["models"]["m"]
    metrics = model["metrics"]
    assert metrics["hle"] == 0.77 and metrics["critpt"] == 0.4
    assert model["metricSources"]["hle"] == {"sourceType": "model_provider_claim",
                                              "sourceUrl": "https://provider.example/claim", "claimId": "c-hle"}
    for rejected in ("scicode", "aaLcr", "gdpvalV21", "gpqaDiamond", "terminalBenchV40"):
        assert metrics[rejected] is None, rejected
    assert metrics["intelligenceIndex"] == 55.0
    assert model["metricSources"]["intelligenceIndex"]["sourceType"] == "benchmark_owner"
    assert len(model["providerClaims"]) == 8  # every claim for this model is retained, eligible or not
    assert coverage["fields"]["hle"]["providerClaimN"] == 1
    assert coverage["fields"]["scicode"]["providerClaimN"] == 0


def test_main_rejects_raw_page_whose_payload_belongs_to_another_slug(world):
    world.write(extract=[entry("m")])
    world.page("m", "m", {"slug": "actual"})
    with pytest.raises(ValueError, match="currentModel slug 'actual' does not match page slug 'm'"):
        bam.main()


def test_main_rejects_slug_and_variant_mismatch(world):
    world.write(mapping=[{"id": "m", "aaSlug": "expected"}], extract=[entry("m", slug="actual")])
    world.page("m", "actual", {"slug": "actual"})
    with pytest.raises(ValueError, match="slug mismatch for m: expected expected, got actual"):
        bam.main()
    world.write(mapping=[{"id": "m", "aaVariant": "max"}], extract=[entry("m")])
    world.page("m", "m", {"slug": "m", "effort": {"slug": "high"}})
    with pytest.raises(ValueError, match="variant mismatch for m: expected max"):
        bam.main()


def test_main_uses_glob_fallback_page_files(world):
    world.write(extract=[entry("g", slug="g")])
    world.page("g", "g-max", {"slug": "g", "intelligenceIndex": 10})
    output, _ = world.run()
    assert output["models"]["g"]["extraction"]["htmlSnapshot"] == "data/aa/g__g-max.html"


def snapshot_page(model_id, model, capture=None, **extra):
    page = {"id": model_id, "url": f"https://artificialanalysis.ai/models/{model_id}", "model": model}
    if capture is not None:
        page["capture"] = capture
    page.update(extra)
    return page


def test_main_snapshot_mode_carries_capture_provenance(world):
    snapshot = {"capturedAt": "2026-10-01T00:00:00Z", "pages": [
        snapshot_page("s1", {"slug": "s1", "effort": {"slug": "max"}, "intelligenceIndex": 40, "speed": 120,
                             "intelligenceIndexIsEstimated": True},
                      {"observedAt": "2026-10-05T10:00:00Z", "capturedAt": "ignored", "precision": "rounded",
                       "metricSourceUrls": {"intelligenceIndex": "https://aa.example/chart"},
                       "metricPrecision": {"intelligenceIndex": "whole"}, "captureMode": "public-rendered",
                       "note": "read from chart", "responseSha256": "abc", "method": "browser read"}),
        snapshot_page("s2", {"slug": "s2", "intelligenceIndex": 30, "outputSpeedVariance": {"median": 77.5}},
                      {"capturedAt": "2026-10-02T00:00:00Z", "captureMethod": "payload fetch"}),
        snapshot_page("s3", {"slug": "s3", "intelligenceIndex": 20}, {}),
        snapshot_page("s4", {"intelligenceIndex": 10}),
    ]}
    world.write(extract=[entry("s1", captureMode="entry-mode"), entry("s2"), entry("s3"), entry("s4")], snapshot=snapshot)
    output, coverage = world.run()
    s1, s2, s3, s4 = (output["models"][key] for key in ("s1", "s2", "s3", "s4"))
    assert s1["metrics"]["speed"] == 120.0 and s2["metrics"]["speed"] == 77.5 and s3["metrics"]["speed"] is None
    assert s1["metricSources"]["intelligenceIndex"] == {
        "sourceType": "benchmark_owner_estimate", "sourceUrl": "https://aa.example/chart",
        "observedAt": "2026-10-05T10:00:00Z", "precision": "whole", "status": "estimated"}
    assert s1["metricSources"]["speed"]["precision"] == "rounded"  # falls back to capture-level precision
    assert s1["metricSources"]["speed"]["sourceUrl"] == "https://artificialanalysis.ai/models/s1"
    assert s1["extraction"] == {
        "captureMode": "public-rendered", "htmlSnapshot": None, "textSnapshot": None,
        "sourceSnapshot": "data/aa/aa_v432_snapshot.json", "sourceObservedAt": "2026-10-05T10:00:00Z",
        "precision": "rounded", "note": "read from chart", "responseSha256": "abc", "method": "browser read"}
    assert s2["extraction"]["sourceObservedAt"] == "2026-10-02T00:00:00Z"  # capturedAt when observedAt absent
    assert s2["extraction"]["method"] == "payload fetch"
    assert s3["extraction"]["sourceObservedAt"] == "2026-10-01T00:00:00Z"  # document-level capturedAt
    assert s3["extraction"]["captureMode"] is None
    assert s3["extraction"]["method"].startswith("captured currentModel object")
    assert s4["aaSlug"] == "s4"  # slug falls back to the model id
    assert s4["extraction"]["captureMode"] is None
    assert output["sourceSnapshot"] == coverage["sourceSnapshot"] == "data/aa/aa_v432_snapshot.json"
    assert s1["aaUrl"] == "https://artificialanalysis.ai/models/s1"


def test_main_snapshot_entry_captures_mode_from_extract_entry(world):
    snapshot = {"pages": [snapshot_page("s", {"slug": "s"}, {})]}
    world.write(extract=[entry("s", captureMode="from-entry")], snapshot=snapshot)
    output, _ = world.run()
    assert output["models"]["s"]["extraction"]["captureMode"] == "from-entry"


def test_main_accepts_list_snapshots(world):
    world.write(extract=[entry("l")], snapshot=[snapshot_page("l", {"slug": "l", "intelligenceIndex": 5})])
    output, _ = world.run()
    assert output["models"]["l"]["metrics"]["intelligenceIndex"] == 5.0
    assert output["sourceSnapshot"] == "data/aa/aa_v432_snapshot.json"


@pytest.mark.parametrize("snapshot", [None, 7, {"pages": []}, {}])
def test_main_ignores_missing_or_unusable_snapshots(world, snapshot):
    world.write(extract=[entry("h")], snapshot=snapshot)
    world.page("h", "h", {"slug": "h", "intelligenceIndex": 5})
    output, coverage = world.run()
    assert output["models"]["h"]["extraction"]["sourceSnapshot"] is None
    assert output["sourceSnapshot"] is None and coverage["sourceSnapshot"] is None


def test_main_requires_raw_pages_when_snapshot_lacks_the_model(world):
    world.write(extract=[entry("absent")])
    with pytest.raises(FileNotFoundError):
        bam.main()


def test_module_guard_exits_with_main_status(tmp_path, monkeypatch, pinned_clock):
    root = tmp_path / "root"
    data = root / "data"
    (data / "aa").mkdir(parents=True)
    (data / "aa_mapping.json").write_text("[]")
    (data / "aa" / "aa_extract.json").write_text(json.dumps([entry("z")]))
    (data / "provider_claims.json").write_text(json.dumps({"claims": []}))
    snapshot = {"pages": [snapshot_page("z", {"slug": "z", "intelligenceIndex": 1}, {})]}
    (data / "aa" / "aa_v432_snapshot.json").write_text(json.dumps(snapshot))
    import valuerank.paths as paths

    monkeypatch.setattr(paths, "ROOT", root)
    monkeypatch.setattr(paths, "DATA", data)
    with pytest.warns(RuntimeWarning), pytest.raises(SystemExit) as exit_info:
        runpy.run_module("valuerank.build_aa_metrics", run_name="__main__", alter_sys=True)
    assert exit_info.value.code == 0
    assert json.loads((data / "aa_metrics.json").read_text())["models"]["z"]["metrics"]["intelligenceIndex"] == 1.0
    assert (data / "coverage_matrix.json").exists()
