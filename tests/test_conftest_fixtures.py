import json

from valuerank import clock


def test_repo_copy_mirrors_tracked_data_and_site(repo_copy):
    assert (repo_copy / "data" / "scores.json").is_file()
    assert (repo_copy / "data" / "aa" / "aa_v432_snapshot.json").is_file()
    assert (repo_copy / "site" / "index.html").is_file()
    assert not (repo_copy / "data" / "tb4-scrape.json").exists(), "ignored local captures must not be copied"
    assert json.loads((repo_copy / "data" / "ranking_summary.json").read_text())["version"].startswith("v")


def test_pinned_clock_matches_committed_observation_instant(repo_copy, pinned_clock):
    summary = json.loads((repo_copy / "data" / "ranking_summary.json").read_text())

    assert clock.iso_z() == pinned_clock == summary["observedAt"]
