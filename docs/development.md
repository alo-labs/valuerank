# Development guide

## Prerequisites

| Tool | Version | Used for |
|---|---|---|
| Python | 3.12 or newer (CI runs 3.12 and 3.13) | The pipeline, the site generator and the Python test suite |
| Node.js | 20 or newer (CI uses 22) | The npm task runner, the Node tests, the browser helpers and the end-to-end suite |
| Playwright Chromium | installed with `npx playwright install chromium` | `npm run capture:tb4`, `npm run generate:og`, `npm run test:e2e` |
| Git | any recent | The test fixtures list files with `git ls-files`, so run the tests from a checkout |

The Markdown pipeline uses only the Python standard library. The site generator needs Jinja2, pinned in `requirements.txt`. The test tooling is pinned in `requirements-dev.txt`.

## Setup

```bash
git clone https://github.com/alo-labs/valuerank.git
cd valuerank
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt -r requirements-dev.txt
npm ci
npx playwright install chromium
```

Activate the virtual environment (`source .venv/bin/activate`) before you run the npm scripts. They call `python3`, so the environment's Python must be the first one on `PATH`. Alternatively, call `.venv/bin/python` directly.

## Everyday commands

| Command | What it does |
|---|---|
| `npm test` | `test:py`, then `test:js`, then `test:e2e`. Stops at the first failure. |
| `npm run test:py` | `pytest` with branch coverage. `pyproject.toml` sets `fail_under = 100` for `valuerank/`. |
| `npm run test:js` | Node's test runner over `tests/js/`, with line, branch and function thresholds at 100% for `scripts/**` and `valuerank/site/assets/js/**`. |
| `npm run test:e2e` | Browser scenarios in `tests/e2e/` against the generated `site/`. External requests are blocked. Run `npm run build:site` first. |
| `npm run verify:docs` | Regenerates the Markdown documents and the site with the clock pinned to the committed observation instant. Fails if a tracked file under `README.md`, `methodology.md`, `scores.md`, `raw-data.md`, `site/` or `data/` differs from the committed version. |
| `npm run verify` | `npm test` followed by `npm run verify:docs`. CI runs the same checks as separate steps. |
| `npm run build:site` | Stage 9 only: renders `site/` from the snapshots (`python3 -m valuerank.site.build`). |
| `npm run build:docs` | Stage 8 (the Markdown documents) and stage 9 (the site). Stamps the current time unless `VALUERANK_NOW` is set. |
| `npm run build:publication` | `build:docs`, then `generate:og`. |
| `npm run generate:og` | Stage 10: renders the Open Graph share cards with Playwright. |
| `npm run preview` | Serves `site/` at `http://localhost:7890/` with `python3 -m http.server`. It does not build. |
| `npm run build:scores` | Stage 6, scoring from the committed snapshots. |
| `npm run reconcile:aa` | Stage 7, the AA frontier gate. |
| `npm run refresh` | The full refresh, including network captures; see `docs/refresh-and-release.md`. |

Run a single stage directly with `python3 -m valuerank.<stage>`; the module docstrings describe their arguments.

## Reproducibility and the clock

Every stage stamps an observation instant through `valuerank.clock.utcnow()`. Set `VALUERANK_NOW` to an ISO 8601 instant to pin it:

```bash
VALUERANK_NOW=2026-10-07T17:23:20Z python3 -m valuerank.build_scores
```

The committed outputs were generated with the instant recorded in `data/ranking_summary.json` (`observedAt`). `npm run verify:docs` reads that value, regenerates and diffs. When you intentionally change a generator or a snapshot, regenerate with the same pinned instant so the diff shows only your change. A real refresh, which captures new data, stamps a new instant.

The site build (`valuerank.site.build`) does not read the clock. Its dates come from the snapshots and from `valuerank/release.py`, so its output does not depend on `VALUERANK_NOW`.

## Building and previewing the site

The site is generated. Build it, then serve it:

```bash
npm run build:site
npm run preview
```

Open `http://localhost:7890/`. `npm run preview` serves the files that are on disk. It does not rebuild them, so rebuild after every change to a template, an asset, a view model or a snapshot.

## Conventions

- Pipeline code lives in `valuerank/`: one module per stage, importable without side effects, with `main()` taking explicit paths so tests can point it at a temporary copy of the repository.
- The site generator lives in `valuerank/site/`. View models compute the public documents, templates render them, and assets are copied unchanged. `docs/site-data-contract.md` is the contract between the three. Change the contract before you change a view model, a template or a client script.
- Tests live in `tests/` (Python), `tests/js/` (Node) and `tests/e2e/` (browser). They never write into the real repository. Use the `repo_copy` fixture from `tests/conftest.py` or `tmp_path`. The end-to-end tests only read `site/`.
- Coverage exclusions are disabled on purpose (`exclude_lines = []`). Reach the branch with a test or remove the code.
- Generated files are never edited by hand: `README.md`, `methodology.md`, `scores.md`, `raw-data.md`, and everything under `site/` except `site/CNAME`. Change the generator, the template or the snapshot instead.
- Dated `research/` directories are immutable. Current guidance lives in `docs/`.
- Dependencies are pinned: `requirements.txt` (Jinja2) and `requirements-dev.txt` (pytest, pytest-cov, coverage) for Python; `package.json` plus `package-lock.json` for Node, where Playwright 1.62.0 is a dev dependency; and `projects/nz-egg-market/requirements.txt` for the auxiliary PDF project.

## Troubleshooting

| Symptom | Cause and fix |
|---|---|
| `AA reconciliation blocked … Inventory is stale or future-dated (N days)` and exit code 1 from `npm run reconcile:aa` or `npm run refresh` | The frontier inventory in `data/aa_reconciliation_inventory.json` is older than 7 days. Recapture the AA frontier during a refresh, or run `python3 -m valuerank.aa_reconciliation --report-only` to write an honest blocked report without passing the gate. Offline regeneration with `VALUERANK_NOW` pinned to the committed instant is unaffected. |
| `VALUERANK_NOW must be an ISO 8601 instant` | The override is set to something that cannot be parsed. Use `YYYY-MM-DDTHH:MM:SSZ` or an explicit offset. |
| `npm run verify:docs` fails with a diff | A generator or snapshot changed without regenerating, or a generated file was edited by hand. `verify:docs` regenerates in place with the pinned instant, so run it, then read `git diff` and `git status --short`. New untracked files do not appear in `git diff`. Commit the regenerated files, or revert the hand edit. |
| `jinja2.exceptions.UndefinedError` while running `npm run build:site` or `npm run build:docs` | A template uses a key that the view model does not provide. The build uses `StrictUndefined`, so the message names the missing key. Add the key to the view model in `valuerank/site/viewmodel.py` and to `docs/site-data-contract.md`, or correct the template name or key. |
| `ModuleNotFoundError: No module named 'jinja2'` | The site generator needs its runtime dependency. Run `.venv/bin/python -m pip install -r requirements.txt`. |
| `browserType.launch: Executable doesn't exist` | The Playwright browser is missing. Install it with `npx playwright install chromium`. This affects `npm run test:e2e`, `npm run generate:og` and `npm run capture:tb4`. |
| `npm run test:e2e` fails on old text, missing pages or 404s | The end-to-end suite serves `site/` as it is on disk and does not build it. Run `npm run build:site` (and `npm run build:docs` after a snapshot change), then run the suite again. |
| Node rejects a `--test-coverage-*` option, or `npm run test:js` fails before any test runs | The Node version is probably too old for the coverage options of the test runner. Use Node 22, as CI does. |
| `ModuleNotFoundError: No module named 'valuerank'` | Run from the repository root with `python3 -m valuerank.<stage>`. The package is not installed into site-packages. |
| `pytest: command not found` or `No module named pytest` | The virtual environment is not active. Use `.venv/bin/python -m pytest` or activate it. |
| `build_aa_metrics` or `build_tb4` cannot find captures | `data/aa/*.html`, `data/aa/*.txt` and `data/tb4-scrape.json` are local-only. Capture them (`npm run capture:aa`, `npm run capture:tb4`) before rebuilding. CI never runs these stages. |
