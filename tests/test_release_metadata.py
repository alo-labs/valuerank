"""Every place that states the release version must agree with valuerank.release."""

import json
import tomllib
from pathlib import Path

from valuerank import build_scores, emit_docs, release
from valuerank.paths import ROOT


def declared_versions(root: Path) -> dict[str, str]:
    """Return the release version declared by each file that carries one."""

    return {
        "package.json": json.loads((root / "package.json").read_text()).get("version"),
        "pyproject.toml": tomllib.loads((root / "pyproject.toml").read_text())["project"]["version"],
    }


def test_release_module_is_the_single_source_for_version_and_dates():
    assert release.VERSION.startswith("v")
    assert emit_docs.VERSION is release.VERSION
    assert build_scores.VERSION is release.VERSION
    assert emit_docs.DATE is release.DATE
    assert build_scores.PUBLISH_DATE is release.DATE
    assert emit_docs.SHORT_DATE is release.SHORT_DATE
    source = (ROOT / "valuerank" / "emit_docs.py").read_text() + (ROOT / "valuerank" / "build_scores.py").read_text()
    assert 'VERSION = "v' not in source, "version literals must live only in valuerank/release.py"


def test_package_manifests_agree_with_the_release_module():
    versions = declared_versions(ROOT)

    assert set(versions.values()) == {release.VERSION.removeprefix("v")}, versions


def test_ranking_summary_carries_the_declared_version():
    summary = json.loads((ROOT / "data" / "ranking_summary.json").read_text())

    assert summary["version"] == release.VERSION
    assert summary["publishDate"] == release.DATE


def test_declared_versions_reads_both_manifests(tmp_path):
    (tmp_path / "package.json").write_text('{"version": "1.0.0"}')
    (tmp_path / "pyproject.toml").write_text('[project]\nversion = "1.0.1"\n')

    assert declared_versions(tmp_path) == {"package.json": "1.0.0", "pyproject.toml": "1.0.1"}
