# Repository layout

ValueRank is a research workspace with a small, reproducible publication pipeline. The layout separates four kinds of material: pipeline code, canonical data snapshots, generated publication output, and dated research ledgers.

| Path | Kind | Notes |
|---|---|---|
| `valuerank/` | Pipeline code | One module per stage, run as `python3 -m valuerank.<stage>`. Standard library only. |
| `scripts/` | Browser helpers | Playwright capture and Open Graph rendering (`scripts/README.md`). |
| `data/` | Canonical inputs and generated outputs | Committed JSON snapshots (`aa_mapping.json`, `bug_hunt.json`, …) and generated files (`scores.json`, `coverage_matrix.json`, `ranking_summary.json`, `run_manifest.json`, …). Browser HTML/text captures under `data/aa/` and `data/snapshots/` are local-only and ignored. |
| `site/` | Published static site | Committed GitHub Pages output. `site/index.html` is patched in place by the emitter; it is both template and output. |
| `README.md`, `methodology.md`, `scores.md`, `raw-data.md` | Generated publication | Written by `valuerank.emit_docs`; do not edit by hand. |
| `tests/` | Test suite | `pytest` for Python, `node --test` for `scripts/`; see `docs/testing.md`. |
| `docs/` | Contributor documentation | Architecture, development, testing, refresh and release guides. |
| `research/` | Dated research ledgers | Immutable records of each refresh and investigation. Historical ledgers may reference the pre-2026-10-17 layout; see the path map below. |
| `benchmarks/`, `coding-agents-valuerank/`, `skills/`, `projects/` | Supporting analyses and auxiliary projects | Not part of the pipeline. |
| `archive/` | Historical material | `archive/refresh-v1.3/` is the retired v1.3.1 pipeline and its snapshots; `archive/value-rank-v4/` holds the earlier modular documents. |
| `.github/workflows/` | CI and deployment | `ci.yml` runs tests, coverage gates and the publication sync check; `deploy.yml` publishes `site/` after `ci.yml` passes. |

## Path map for historical references

The layout changed on 2026-10-17. Older research ledgers and commit messages use the previous paths:

| Before | Now |
|---|---|
| `.refresh/v1.4/*.py` | `valuerank/*.py` (`build_deepswe_v14.py` → `build_deepswe.py`, `capture_aa_v432.py` → `capture_aa.py`, `emit_v14_docs.py` → `emit_docs.py`) |
| `.refresh/v1.4/*.json`, `.refresh/v1.4/aa/` | `data/*.json`, `data/aa/` |
| `.refresh/v1.4/scrape_tb4.js` | `scripts/scrape-tb4.js` |
| `scripts/plan_costs.py`, `scripts/site_header.py`, `scripts/generate_tb4_page.py` | `valuerank/plan_costs.py`, `valuerank/site_header.py`, `valuerank/tb4_page.py` |
| `scripts/site-generate-og-cards.mjs` | `scripts/generate-og-cards.mjs` |
| `research/2026-09-29-valuerank-refresh-v4-3-2/run_manifest.json` (generated copy) | `data/run_manifest.json`; the research copy is now a frozen snapshot |
| `research/2026-10-08-frontier-inclusion/current-frontier.json` (pipeline input) | `data/aa_frontier_capture.json`; the research copy is a frozen snapshot |
| `.refresh/v1.3/` | `archive/refresh-v1.3/` |
| `scripts/charts/`, `.refresh/parse_deepswe.py` | Removed (unreferenced legacy generators; available in git history) |

## Local-only material

Installed environments, browser and tool state, graph output, captures and logs are reproducible and ignored by `.gitignore`: `.venv/`, `node_modules/`, `.claude/`, `.opencode/`, `graphify-out/`, `.tmp/`, `.runs/`, `artifacts/`, `data/aa/*.html`, `data/aa/*.txt`, `data/snapshots/`, `data/tb4-scrape.json`, `research/sources/`, `projects/*/source-corpus/`.
