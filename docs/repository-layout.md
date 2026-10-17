# Repository layout

ValueRank is a research workspace with a small, reproducible publication pipeline and a generated static site. The layout separates five kinds of material: pipeline and site code, canonical data snapshots, generated publication output, tests, and dated research ledgers.

| Path | Kind | Notes |
|---|---|---|
| `valuerank/` | Pipeline code | One module per stage, run as `python3 -m valuerank.<stage>`. The Markdown stages use the standard library only. |
| `valuerank/site/` | Site generator | `build.py` (orchestrator), `viewmodel.py`, `evidence.py`, `picks.py`, `changelog.py` and `export.py` (view models and public JSON), `templates/` (Jinja2 pages and partials), `assets/` (stylesheet, ES modules, charts, favicon; copied to `site/assets/`) and `legacy/` (the archived coding-agents v0.3 page). Needs Jinja2. |
| `scripts/` | Browser helpers | Playwright capture and Open Graph rendering (`scripts/README.md`). |
| `data/` | Canonical inputs and generated outputs | Committed JSON snapshots (`aa_mapping.json`, `bug_hunt.json`, …) and generated files (`scores.json`, `coverage_matrix.json`, `ranking_summary.json`, `run_manifest.json`, …). Browser HTML/text captures under `data/aa/` and `data/snapshots/` are local-only and ignored. |
| `site/` | Published static site (generated) | Committed GitHub Pages output. Every file is written by `valuerank.site.build` or `scripts/generate-og-cards.mjs`, except `site/CNAME`, which sets the custom domain. Never edit a generated file by hand. |
| `README.md`, `methodology.md`, `scores.md`, `raw-data.md` | Generated publication | Written by `valuerank.emit_docs`; do not edit by hand. |
| `tests/` | Test suite | `pytest` for Python (`tests/test_*.py`, fixtures under `tests/fixtures/`), `node --test` for `scripts/`, the site's client code and its charts (`tests/js/`), and Playwright scenarios (`tests/e2e/`). See `docs/testing.md`. |
| `docs/` | Contributor documentation | Architecture, development, testing, refresh and release guides; the site experience plan and the site data contract. |
| `research/` | Dated research ledgers | Immutable records of each refresh and investigation. Historical ledgers may reference the pre-2026-10-17 layout; see the path map below. |
| `benchmarks/`, `coding-agents-valuerank/`, `skills/`, `projects/` | Supporting analyses and auxiliary projects | Not part of the pipeline. |
| `archive/` | Historical material | `archive/refresh-v1.3/` is the retired v1.3.1 pipeline and its snapshots, kept as provenance; `archive/value-rank-v4/` holds the earlier modular documents. |
| `.github/workflows/` | CI and deployment | `ci.yml` installs the Python and Node dependencies and Chromium, then runs the Python, Node and end-to-end tests and the publication sync check. `deploy.yml` calls `ci.yml` and uploads the committed `site/` to GitHub Pages without rebuilding it. |
| `package.json`, `package-lock.json`, `pyproject.toml`, `requirements.txt`, `requirements-dev.txt` | Dependencies and task definitions | npm scripts and Node lock file; Python project metadata and pytest and coverage settings; runtime (Jinja2) and test Python pins. |

## Generated site layout

`valuerank.site.build` writes the pages below and the files under `site/data/` and `site/assets/`. `scripts/generate-og-cards.mjs` writes the share images. Nothing under `site/` is edited by hand, except `site/CNAME`. The custom domain is `valuerank.alolabs.dev`.

| Site path | Produced by | Notes |
|---|---|---|
| `/` | `valuerank/site/templates/index.html` | Answer page: headline, picks, compact ranking table and the Pareto chart. |
| `/rankings/` | `valuerank/site/templates/rankings.html` | The full table with filters, column choice, compare and export. |
| `/models/` | `valuerank/site/templates/models.html` | Index of the roster, ranked first. |
| `/models/<slug>/` | `valuerank/site/templates/model.html` | One page per roster model. Pages for models that left the roster are removed on rebuild. |
| `/plans/` | `valuerank/site/templates/plans.html` | Subscription routes, the worked example and the candidate comparison. |
| `/benchmarks/` | `valuerank/site/templates/benchmarks.html` | Source registry, coverage and the frontier. |
| `/benchmarks/terminal-bench-4/` | `valuerank/site/templates/benchmark_tb4.html` | Terminal-Bench 4.0 page. |
| `/methodology/` | `valuerank/site/templates/methodology.html` | Scoring, evidence grades, FAQ and limitations. |
| `/changelog/` | `valuerank/site/templates/changelog.html` | Release history and rank changes. |
| `/data/` | `valuerank/site/templates/data.html` | Download page that lists every JSON file with its schema. |
| `/archive/coding-agents-v0.3/` | `valuerank/site/legacy/coding-agents-v0.3.html`, with an archive banner | Frozen v0.3 snapshot. |
| `/tb4/`, `/coding-agents/` | `valuerank/site/templates/redirect.html` | Redirect stubs for the old URLs. |
| `/assets/` | Copied from `valuerank/site/assets/` | Stylesheet, ES modules, charts and favicon. |
| `/data/*.json` | `valuerank/site/export.py` | `rankings.json`, `plans.json`, `benchmarks.json`, `livebench.json`, `changelog.json`, `benchmarks/terminal-bench-4.json` and `models/<slug>.json`. |
| `/sitemap.xml`, `/robots.txt` | `valuerank/site/build.py` | The sitemap lists every generated page and the archive page. |
| `/og/<key>.png`, `/og/models/<slug>.png`, `/og/archive.png` | `scripts/generate-og-cards.mjs` | Share images, one per page, drawn from the public JSON; each page's `og:image` points at its own card. |

## Path map for historical references

The layout changed on 2026-10-17. The site generator (2026-10-18) removed the two page modules and moved the archived coding-agents page. Older research ledgers and commit messages use the previous paths:

| Before | Now |
|---|---|
| `.refresh/v1.4/*.py` | `valuerank/*.py` (`build_deepswe_v14.py` → `build_deepswe.py`, `capture_aa_v432.py` → `capture_aa.py`, `emit_v14_docs.py` → `emit_docs.py`) |
| `.refresh/v1.4/*.json`, `.refresh/v1.4/aa/` | `data/*.json`, `data/aa/` |
| `.refresh/v1.4/scrape_tb4.js` | `scripts/scrape-tb4.js` |
| `scripts/plan_costs.py` | `valuerank/plan_costs.py` |
| `scripts/site_header.py`, `valuerank/site_header.py` | Removed. The shared header and footer are in `valuerank/site/templates/base.html` and `partials/`. |
| `scripts/generate_tb4_page.py`, `valuerank/tb4_page.py` | Removed. The Terminal-Bench 4.0 page is `valuerank/site/templates/benchmark_tb4.html`, built at `/benchmarks/terminal-bench-4/`. |
| `site/index.html` (patched in place by the emitter) | Generated by `valuerank.site.build` from `valuerank/site/templates/index.html` |
| `site/coding-agents/index.html` | `valuerank/site/legacy/coding-agents-v0.3.html`, archived at `/archive/coding-agents-v0.3/`. `/coding-agents/` redirects there. |
| `site/tb4/index.html` | Generated at `/benchmarks/terminal-bench-4/`. `/tb4/` redirects there. |
| `scripts/site-generate-og-cards.mjs` | `scripts/generate-og-cards.mjs` |
| `research/2026-09-29-valuerank-refresh-v4-3-2/run_manifest.json` (generated copy) | `data/run_manifest.json`; the research copy is now a frozen snapshot |
| `research/2026-10-08-frontier-inclusion/current-frontier.json` (pipeline input) | `data/aa_frontier_capture.json`; the research copy is a frozen snapshot |
| `.refresh/v1.3/` | `archive/refresh-v1.3/` |
| `scripts/charts/`, `.refresh/parse_deepswe.py` | Removed (unreferenced legacy generators; available in git history) |

## Local-only material

Installed environments, browser and tool state, graph output, captures and logs are reproducible and ignored by `.gitignore`: `.venv/`, `node_modules/`, `__pycache__/`, `.pytest_cache/`, `.coverage`, `htmlcov/`, `.claude/`, `.opencode/`, `graphify-out/`, `.tmp/`, `.runs/`, `artifacts/`, `data/aa/*.html`, `data/aa/*.txt`, `data/snapshots/`, `data/tb4-scrape.json`, `research/sources/`, `projects/*/source-corpus/`.

The generated `site/` is not local-only. It is committed, because the deployment uploads it as committed.
