# Development guide

## Prerequisites

| Tool | Version | Used for |
|---|---|---|
| Python | 3.12 or newer | The pipeline (standard library only) and the test suite |
| Node.js | 20 or newer (CI uses 22) | Browser helpers, Node tests, npm task runner |
| Playwright Chromium | installed via `npx playwright install chromium` | `npm run capture:tb4`, `npm run generate:og` only |
| Git | any recent | The test fixtures copy tracked files with `git ls-files` |

## Setup

```bash
git clone https://github.com/alo-labs/valuerank.git
cd valuerank
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
npm ci
```

Activate the virtual environment (`source .venv/bin/activate`) so that the `python3` used by the npm scripts is the one with the test tooling, or call `.venv/bin/python` directly. The pipeline stages themselves run on any Python 3.12+ without extra packages.

Playwright's browser build is needed only for the two browser helpers:

```bash
npx playwright install chromium
```

## Everyday commands

| Command | What it does |
|---|---|
| `npm test` | Python tests with the 100% coverage gate, then Node tests with the 100% coverage gate |
| `npm run test:py` | `pytest` with branch coverage (`pyproject.toml` sets `fail_under = 100`) |
| `npm run test:js` | Node's built-in test runner over `tests/js/` with line, branch and function thresholds at 100% for `scripts/` |
| `npm run verify:docs` | Regenerates the Markdown documents and site pages with the clock pinned to the committed observation instant and fails if anything differs from the committed files |
| `npm run verify` | `npm test` followed by `npm run verify:docs`; this is what CI runs |
| `npm run build:docs` | Stages 8 and 9 only (emitters), stamping the current time unless `VALUERANK_NOW` is set |
| `npm run build:scores` | Stage 6, scoring from the committed snapshots |
| `npm run reconcile:aa` | Stage 7, the AA frontier gate |
| `npm run refresh` | The full refresh, including network captures; see `docs/refresh-and-release.md` |

Run a single stage directly with `python3 -m valuerank.<stage>`; the module docstrings describe their arguments.

## Reproducibility and the clock

Every stage stamps an observation instant through `valuerank.clock.utcnow()`. Set `VALUERANK_NOW` to an ISO 8601 instant to pin it:

```bash
VALUERANK_NOW=2026-10-07T17:23:20Z python3 -m valuerank.build_scores
```

The committed outputs were generated with the instant recorded in `data/ranking_summary.json` (`observedAt`). `npm run verify:docs` reads that value, regenerates and diffs. When you intentionally change a generator or a snapshot, regenerate with the same pinned instant so the diff shows only your change, and let a real refresh (which captures new data) stamp a new instant.

## Previewing the site

The site is static. Serve the `site/` directory with any file server, for example:

```bash
python3 -m http.server 7890 --directory site
```

and open `http://localhost:7890/`.

## Conventions

- Pipeline code lives in `valuerank/`; one module per stage, importable without side effects, with `main()` taking explicit paths so tests can point it at a temporary copy of the repository.
- Tests live in `tests/` (Python) and `tests/js/` (Node). They never write into the real repository; use the `repo_copy` fixture from `tests/conftest.py` or `tmp_path`.
- Coverage exclusions are disabled on purpose (`exclude_lines = []`). Reach the branch with a test or remove the code.
- Generated documents (`README.md`, `methodology.md`, `scores.md`, `raw-data.md`, `site/index.html`, `site/tb4/index.html`) are never edited by hand.
- Dated `research/` directories are immutable. Current guidance lives in `docs/`.
- Dependencies are pinned: `requirements-dev.txt` for Python tooling, `package.json` plus `package-lock.json` for Node, `projects/nz-egg-market/requirements.txt` for the auxiliary PDF project.

## Troubleshooting

| Symptom | Cause and fix |
|---|---|
| `AA reconciliation blocked … Inventory is stale or future-dated (N days)` and exit code 1 from `npm run reconcile:aa` or `npm run refresh` | The frontier inventory in `data/aa_reconciliation_inventory.json` is older than 7 days. Recapture the AA frontier during a refresh, or run `python3 -m valuerank.aa_reconciliation --report-only` to write an honest blocked report without passing the gate. Offline regeneration with `VALUERANK_NOW` pinned to the committed instant is unaffected. |
| `VALUERANK_NOW must be an ISO 8601 instant` | The override is set to something `datetime.fromisoformat` cannot parse. Use `YYYY-MM-DDTHH:MM:SSZ` or an explicit offset. |
| `npm run verify:docs` fails with a diff | A generator or snapshot changed without regenerating, or a document was edited by hand. Run `npm run build:docs` with the pinned instant (see above) and commit the regenerated files, or revert the hand edit. |
| `shared header injection expected one nav in …` | A site page lost or gained a `<nav>`; the shared header injector requires exactly one. Restore the page structure. |
| `chart tab order replacement failed` or `Cannot insert AA comparison: publication shell lacks </main>` | `site/index.html` is missing a marker the emitter relies on. Restore the marker; the template and the emitter must change together. |
| `browserType.launch: Executable doesn't exist` | Install the Playwright browser: `npx playwright install chromium`. |
| `ModuleNotFoundError: No module named 'valuerank'` | Run from the repository root with `python3 -m valuerank.<stage>`; the package is not installed into site-packages. |
| `pytest: command not found` or `No module named pytest` | The virtual environment is not active. Use `.venv/bin/python -m pytest` or activate it. |
| `build_aa_metrics` or `build_tb4` cannot find captures | `data/aa/*.html`, `data/aa/*.txt` and `data/tb4-scrape.json` are local-only. Capture them (`npm run capture:aa`, `npm run capture:tb4`) before rebuilding; CI never runs these stages. |
