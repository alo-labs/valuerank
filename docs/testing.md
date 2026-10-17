# Testing

## What the suites prove

| Suite | Runner | Scope | Gate |
|---|---|---|---|
| Python unit tests (`tests/test_*.py`) | `pytest` | Every function and branch of each `valuerank/` module: the pipeline stages (scoring arithmetic, normalisation, evidence eligibility, template patching, error paths, CLI entry points) and the site generator (view models, evidence grades, picks, changelog, public JSON export, build orchestration) | 100% statements and branches of `valuerank/` (`pyproject.toml`, `fail_under = 100`, no exclusion patterns) |
| Site template tests (`tests/test_site_templates.py`) | `pytest` | Every page template renders from fixtures in `tests/fixtures/site/templates/` under the production Jinja2 environment (strict undefined, autoescape). The tests check the single `h1`, heading order, head metadata and skip link, the shared navigation and footer, escaping of untrusted strings, and the embedded JSON | Part of the Python run |
| Site view-model tests (`tests/test_site_viewmodel_*.py`, `tests/test_site_build*.py`, `tests/test_site_hardening.py`, `tests/test_plan_view.py`) | `pytest` | Unit, edge and golden tests of the view models. The golden tests run on a copy of the committed `data/` snapshots and check the documents against the scores and the plan arithmetic. The tests also cover the determinism of the public JSON export and the build's page catalogue and redirects | Part of the Python run |
| Python integration tests (`@pytest.mark.integration`) | `pytest` | Run the offline stages as subprocesses in a temporary copy: `build_scores`, `aa_reconciliation`, `emit_docs` and `site.build`. The regenerated Markdown and every file under `site/` must be byte-identical to the committed ones. The emitter is a fixed point when run twice, and the reconciliation gate blocks a stale inventory | Part of the same run |
| Node tests (`tests/js/**/*.test.mjs`) | `node --test` | (1) The browser helpers in `scripts/`: row filtering, capture document, card HTML, output paths, and their orchestration against a fake Playwright. (2) The site's client modules in `valuerank/site/assets/js/` and its chart modules, run against a fake DOM and a fake Plotly (`tests/js/helpers/`) | 100% lines, branches and functions of `scripts/**` and `valuerank/site/assets/js/**` (`npm run test:js`) |
| End-to-end tests (`tests/e2e/site.test.mjs`, `a11y.test.mjs`, `print.test.mjs`) | `node --test` with Playwright (Chromium) and `@axe-core/playwright` | Real browser scenarios against the generated `site/`: the answer page and basis toggle, URL state on the rankings page (filters, sorting, columns, compare, chart tab), CSV and JSON export, mobile navigation, the theme toggle, legacy redirects, one `h1`, a skip link and a canonical URL on every page; an axe audit of twelve pages in both themes at 1280 and 375 px asserting zero serious or critical violations; print media hides navigation and controls and prints black on white | No coverage gate. Each scenario asserts visible behaviour |
| Publication sync (`npm run verify:docs`) | shell | Regenerates the Markdown documents and `site/` in place with the clock pinned to `data/ranking_summary.json`'s `observedAt`, then fails on any difference in the tracked files | CI step |
| Release metadata (`tests/test_release_metadata.py`) | `pytest` | `valuerank/release.py` is the only version literal. `package.json`, `pyproject.toml` and `data/ranking_summary.json` agree with it | Part of the Python run |

Run everything with `npm run verify`. CI (`.github/workflows/ci.yml`) runs `test:py`, `test:js`, `test:e2e` and `verify:docs` on Python 3.12 and 3.13 with Node 22. The Pages deployment (`.github/workflows/deploy.yml`) calls the same workflow before it uploads `site/`.

## Coverage denominator

The gates measure application code only.

- **Python:** every module in `valuerank/` (`[tool.coverage.run] source = ["valuerank"]`). That includes `valuerank/site/`: the view models, evidence, picks, changelog, export and the build. Branch coverage is on, and `exclude_lines = []` means `pragma: no cover` has no effect. `if __name__ == "__main__"` guards count. The tests exercise them with `runpy.run_module(..., run_name="__main__")` against a temporary copy of the repository.
- **Node:** `scripts/scrape-tb4.js`, `scripts/generate-og-cards.mjs` and every module under `valuerank/site/assets/js/`, including the charts (`--test-coverage-include='scripts/**'` and `--test-coverage-include='valuerank/site/assets/js/**'`). The CLI guards in the scripts are exercised by spawning the script as a child process with a preloaded fake `playwright` module. Node merges the child's coverage because it inherits `NODE_V8_COVERAGE`.

Not in the denominator, on purpose:

- The Jinja2 templates in `valuerank/site/templates/` and the archived page `valuerank/site/legacy/coding-agents-v0.3.html`. The template tests and the end-to-end suite check their output.
- The end-to-end tests in `tests/e2e/`, which are not coverage-instrumented.
- `archive/refresh-v1.3/` (retired pipeline kept as provenance, not executed by anything).
- `projects/nz-egg-market/market-structure/build_market_structure_pdf.py` (auxiliary ReportLab project, not part of the publication).
- `research/*.cjs` audit scripts (one-off arithmetic checks recorded with their ledgers).

This page does not record the counts. The gate output prints the current numbers on every run.

## Test design rules

- **Deterministic:** the clock is pinned with `VALUERANK_NOW` (fixture `pinned_clock`). No sleeps, and no real-time comparisons beyond the clock module's own test.
- **Isolated:** nothing writes into the real repository. The `repo_copy` fixture in `tests/conftest.py` copies the files that `git ls-files --cached --others --exclude-standard` lists into `tmp_path`, so new files are included. Synthetic fixtures live under `tests/fixtures/`.
- **No network:** `urllib.request.urlopen` is replaced at the module boundary. Playwright is replaced by fakes that implement the few page methods the scripts call. The end-to-end browser aborts every `http` or `https` request that is not to `127.0.0.1`.
- **Behavioural assertions:** tests check values, ordering, rounding, null handling, inserted content, escaping and error messages, not merely that a function returned.
- **Local-only captures** (`data/aa/*.html`, `data/aa/*.txt`, `data/tb4-scrape.json`) are never required by tests. The stages that parse them are tested with small hand-written fixtures.

## Known limitations

- **Live fetches.** `fetch_livebench`, `capture_aa` and the browser capture in `scripts/scrape-tb4.js` are tested against fakes. A change in the upstream page structure is detected only by a real refresh.
- **Client-side JavaScript.** The Node tests run the site modules against a fake DOM and a fake Plotly. The end-to-end suite runs them in Chromium against the generated `site/`. That suite aborts the Plotly script and the Google Fonts stylesheet, so charts show placeholders there, and chart output is not pixel-tested. After you change a chart module or a chart template, run `npm run build:site`, then `npm run preview`, and check the chart in a browser.
- **The end-to-end suite reads `site/` as it is on disk.** It does not build the site. Run `npm run build:site` before `npm run test:e2e`.
- **Share images.** The OG script is tested through a fake page object. Pixel output is checked by eye when `npm run generate:og` runs during a release. The script writes one card per page (38 in total) from `site/data/*.json`; the card builders are pure functions tested in Node.
- **Stage coverage of `verify:docs`.** `npm run verify:docs` regenerates stage 8 (Markdown) and stage 9 (site) from the committed snapshots. It does not run scoring (stage 6) or the capture stages. The integration test `test_offline_stages_regenerate_the_committed_publication` runs `build_scores`, `aa_reconciliation`, `emit_docs` and `site.build` in a temporary copy and compares the results with the committed files.
- **Untracked files.** `verify:docs` compares tracked files with `git diff`, which does not list untracked files. A newly generated page that is not yet committed passes the check. Run `git status --short site` before you commit.
- **Capture-based stages.** `build_aa_metrics` and `build_tb4` regenerate their committed outputs only on a machine that holds the local captures. CI never runs these stages, so their committed outputs are not regenerated in CI.
