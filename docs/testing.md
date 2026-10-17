# Testing

## What the suites prove

| Suite | Runner | Scope | Gate |
|---|---|---|---|
| Python unit tests (`tests/test_*.py`) | `pytest` | Every function and branch of each `valuerank/` stage: scoring arithmetic, normalisation, evidence eligibility, template patching, error paths, CLI entry points | 100% statements, branches, functions and lines of `valuerank/` (`pyproject.toml`, `fail_under = 100`, no exclusion patterns) |
| Python integration tests (`@pytest.mark.integration`) | `pytest` | Run the real stages as subprocesses in a temporary copy of the repository: the offline pipeline regenerates the committed publication byte for byte, the emitter is a fixed point when run twice, the reconciliation gate blocks a stale inventory | Part of the same run |
| Node tests (`tests/js/*.test.mjs`) | `node --test` | The browser helpers' pure logic (row filtering, capture document, card HTML, output paths) and their orchestration against a fake Playwright | 100% lines, branches and functions of `scripts/` (`npm run test:js` thresholds) |
| Publication sync (`npm run verify:docs`) | shell | Regenerates the documents in place with the clock pinned to `data/ranking_summary.json`'s `observedAt` and fails on any diff | CI step |
| Release metadata (`tests/test_release_metadata.py`) | `pytest` | Version constants in both emitters, `package.json`, `pyproject.toml` and `data/ranking_summary.json` agree | Part of the Python run |

Run everything with `npm run verify`. CI (`.github/workflows/ci.yml`) runs the same commands on Python 3.12 and 3.13 with Node 22, and the Pages deployment waits for it.

## Coverage denominator

Measured on 2026-10-17 at commit b4b5b9b: Python 1,837 statements and 584 branches across the 15 modules of `valuerank/` (633 tests, about 14 s); Node 2 scripts (28 tests, under 2 s). Both gates print 100% and fail the build below it.

Coverage is measured over application code only:

- Python: every module in `valuerank/` (`[tool.coverage.run] source = ["valuerank"]`), with branch coverage enabled and `exclude_lines = []`, so `pragma: no cover` has no effect and `if __name__ == "__main__"` guards count. The guards are exercised with `runpy.run_module(..., run_name="__main__")` against a temporary copy of the repository.
- Node: `scripts/scrape-tb4.js` and `scripts/generate-og-cards.mjs` (`--test-coverage-include='scripts/**'`). Their CLI entry guards are exercised by spawning the script as a child process with a preloaded fake `playwright` module; Node merges the child's coverage because it inherits `NODE_V8_COVERAGE`.

Not in the denominator, deliberately:

- `archive/refresh-v1.3/` (retired pipeline kept as provenance, not executed by anything).
- `projects/nz-egg-market/market-structure/build_market_structure_pdf.py` (auxiliary ReportLab project, not part of the publication).
- `research/*.cjs` audit scripts (one-off arithmetic checks recorded with their ledgers).
- Inline JavaScript inside `site/*.html` (chart rendering and table sorting run in the visitor's browser; the strings that inject them are covered, their behaviour is checked manually on the preview).

## Test design rules

- Deterministic: the clock is pinned with `VALUERANK_NOW` (fixture `pinned_clock`); no sleeps, no real time comparisons beyond the clock module's own test.
- Isolated: nothing writes into the real repository. `repo_copy` (in `tests/conftest.py`) copies the tracked `data/`, `site/`, `valuerank/` and research manifest into `tmp_path`; synthetic fixtures live under `tests/fixtures/`.
- No network: `urllib.request.urlopen` is replaced at the module boundary; Playwright is replaced by fakes implementing the few page methods the scripts call.
- Behavioural assertions: tests check values, ordering, rounding, null handling, inserted content and error messages, not merely that a function returned.
- Local-only captures (`data/aa/*.html`, `data/aa/*.txt`, `data/tb4-scrape.json`) are never required by tests; the stages that parse them are tested with small hand-written fixtures.

## Known limitations

- Live HTTP fetches (`fetch_livebench`, `capture_aa`) and the live browser captures (`scripts/scrape-tb4.js`) are tested against fakes. A change in the upstream page structure is only detected by running a real refresh.
- The site's client-side JavaScript (Plotly charts, label collision repair, table sorting, theme toggle) has no automated browser test; preview the site after changing `valuerank/site_header.py` or the chart code in `site/index.html`.
- Open Graph PNG rendering is tested through a fake page object; pixel output is verified by eye when `npm run generate:og` is run during a release.
- `build_aa_metrics` and `build_tb4` regenerate their committed outputs only on a machine that holds the local captures; `npm run verify:docs` therefore covers stages 6 to 9, not the capture stages. The local `data/tb4-scrape.json` from the 2026-09-29 refresh was lost on 2026-10-17 (a test wrote through the script's default path before its injection was fixed); the committed `data/tb4.json` is intact and the raw capture is recreated by `npm run capture:tb4` at the next refresh.
