"""Canonical repository locations (valuerank/paths.py) and the package contract (valuerank/__init__.py)."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import valuerank
from valuerank import paths
from valuerank.paths import AA_DIR, DATA, ROOT, SITE


def test_root_is_the_checkout_that_holds_the_project_file():
    assert (ROOT / "pyproject.toml").is_file()
    assert (ROOT / "valuerank" / "paths.py").is_file()


def test_root_is_the_resolved_directory_above_the_package():
    assert ROOT.is_absolute()
    assert ROOT == ROOT.resolve()
    assert ROOT == Path(valuerank.__file__).resolve().parent.parent


def test_data_aa_and_site_are_anchored_at_root_and_exist():
    assert DATA == ROOT / "data"
    assert AA_DIR == DATA / "aa"
    assert SITE == ROOT / "site"
    assert DATA.is_dir()
    assert AA_DIR.is_dir()
    assert SITE.is_dir()


def test_paths_module_exports_the_same_locations_the_stages_import():
    assert (paths.ROOT, paths.DATA, paths.AA_DIR, paths.SITE) == (ROOT, DATA, AA_DIR, SITE)


def test_package_docstring_documents_the_stage_runner_contract():
    assert valuerank.__doc__ is not None
    assert "ValueRank publication pipeline" in valuerank.__doc__
    assert "python3 -m valuerank.<stage>" in valuerank.__doc__


def test_importing_the_package_runs_no_pipeline_stage():
    completed = subprocess.run(
        [
            sys.executable,
            "-c",
            "import sys, valuerank; print(sorted(name for name in sys.modules if name.startswith('valuerank.')))",
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=True,
    )

    assert completed.stdout.strip() == "[]"
