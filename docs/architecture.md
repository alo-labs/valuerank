# Architecture

ValueRank turns pinned benchmark and pricing snapshots into a ranked publication: four Markdown documents at the repository root and a multi-page static site under `site/`. The pipeline is a set of independent stages in the `valuerank/` package. Every stage is a plain module with a `main()` function, and runs with `python3 -m valuerank.<stage>` from the repository root. The pipeline stages use only the Python standard library, except the site generator (stage 9), which also needs Jinja2 (`requirements.txt`). Two Playwright helpers in `scripts/` capture a client-rendered leaderboard and render share images.

## Design principles

- **Snapshots are the source of truth.** Every number in the publication traces to a committed JSON file under `data/`. Browser captures that cannot be committed (large HTML) are local-only; their decoded form is committed.
- **Exact-variant evidence only.** Results are never transferred between model versions, reasoning efforts or agent harnesses. Missing values stay `null` and each row's available priorities are renormalized; see `methodology.md` for the published policy.
- **Reproducible output.** Stages stamp the observation instant from `valuerank.clock`, which honours `VALUERANK_NOW`. With the instant pinned to the committed value, the offline stages regenerate the committed Markdown and the whole `site/` tree byte for byte (`npm run verify:docs`).
- **Generated files are never edited by hand.** `valuerank.emit_docs` writes `README.md`, `methodology.md`, `scores.md` and `raw-data.md`. `valuerank.site.build` writes everything under `site/` (pages, public JSON, assets, redirects, archive, sitemap). `scripts/generate-og-cards.mjs` writes the share images. The one hand-maintained file under `site/` is `site/CNAME`, which sets the custom domain. To change a generated file, change its snapshot, emitter, view model, template or asset, then regenerate.

## Stages and data flow

| Order | Stage | Reads | Writes | Needs |
|---:|---|---|---|---|
| 1 | `valuerank.fetch_livebench` | LiveBench release data over HTTPS (pinned commit), `data/aa_metrics.json` | `data/livebench.json` | Network |
| 2 | `scripts/scrape-tb4.js` | tbench.ai Terminal-Bench 4.0 page | `data/tb4-scrape.json` (local-only) | Network, Playwright |
| 3 | `valuerank.build_tb4` | `data/tb4-scrape.json`, `data/aa_metrics.json`, `data/provider_claims.json` | `data/tb4.json` | Local capture |
| 4 | `valuerank.capture_aa` | AA model pages over HTTPS (roster from `data/aa_mapping.json`), preserved captures | `data/aa/aa_v432_snapshot.json`, `data/aa/*.html`, `data/aa/*.txt` (HTML/text local-only) | Network |
| 5 | `valuerank.build_aa_metrics` | `data/aa_mapping.json`, `data/aa/*` captures, `data/provider_claims.json` | `data/aa_metrics.json`, `data/coverage_matrix.json` | Local captures |
| 6 | `valuerank.build_scores` | `data/aa_deepswe.json`, `data/aa_metrics.json`, `data/livebench.json`, `data/tb4.json`, `data/bug_hunt.json`, `data/coverage_matrix.json`, `data/aa_reconciliation_inventory.json`, `data/run_manifest.json` | `data/scores.json`, `data/coverage_matrix.json`, `data/ranking_summary.json`, `data/run_manifest.json` | Offline |
| 7 | `valuerank.aa_reconciliation` | `data/aa_reconciliation_inventory.json`, `data/aa_metrics.json`, `data/scores.json` | `data/aa_reconciliation_report.json` | Offline; fails when the inventory is older than 7 days |
| 8 | `valuerank.emit_docs` | `data/` snapshots: scores, AA metrics, coverage matrix, AA DeepSWE, LiveBench, Terminal-Bench 4.0, Bug Hunt, run manifest, provider claims and plan cost routes | `README.md`, `methodology.md`, `scores.md`, `raw-data.md` (Markdown only) | Offline |
| 9 | `valuerank.site.build` | `data/` snapshots (through the view models), `valuerank/site/templates/`, `valuerank/site/assets/`, `valuerank/site/legacy/coding-agents-v0.3.html` | `site/`: pages, `site/data/`, `site/assets/`, redirect stubs, `site/archive/coding-agents-v0.3/`, `site/sitemap.xml`, `site/robots.txt` | Offline; Jinja2 |
| 10 | `scripts/generate-og-cards.mjs` | `site/data/*.json` | `site/og/<key>.png` for the nine core pages, `site/og/models/<slug>.png` per model, `site/og/archive.png` (38 cards) | Playwright |

`npm run refresh` runs the stages in this order (see `package.json`). `npm run build:docs` runs stages 8 and 9, `npm run build:site` runs stage 9 alone, and `npm run build:publication` adds stage 10.

Stage 8 embeds `valuerank.plan_costs` (subscription routes from `data/plan_cost_routes.json` turned into effective plan costs: AA total cost ÷ Value Multiple ÷ AA Intelligence Index, in USD per Index point). It also calls `valuerank.aa_reconciliation` to render the frontier comparison tables.

`valuerank.build_deepswe` converts the historical DeepSWE Best page capture (`data/deepswe-scrape.json`) into `data/deepswe.json`. That file is retained for audit only; current DeepSWE values come from the hand-curated `data/aa_deepswe.json`.

## The site generator

`valuerank.site.build` (stage 9) renders the public site in three layers.

`site/index.html` is an output of this stage, not a template. The templates live in `valuerank/site/templates/`.

1. **View models** (`valuerank/site/viewmodel.py`, with `evidence.py`, `picks.py` and `changelog.py`). `build_bundle` computes each public document once from the `data/` snapshots: the rankings, one document per roster model, plans, benchmarks, Terminal-Bench 4.0, LiveBench and the changelog. Each page has a function that returns its `page` mapping. Field names and rules are in `docs/site-data-contract.md`.
2. **Templates** (`valuerank/site/templates/`). One Jinja2 template per page type, a `base.html` layout and shared partials in `partials/`. The environment is strict (`StrictUndefined`) and autoescapes HTML, so a missing key fails the build instead of printing an empty value.
3. **Orchestrator** (`valuerank/site/build.py`, `main()`). It holds the page catalogue (path, template, title, description and OG image), the navigation, and the list of every file the build writes.

The build writes these files under `site/`:

- **Pages:** `/`, `/rankings/`, `/models/` (index), `/models/<slug>/` (one per roster model), `/plans/`, `/benchmarks/`, `/benchmarks/terminal-bench-4/`, `/methodology/`, `/changelog/` and `/data/`. Model pages for models that left the roster are removed.
- **Public JSON** in `site/data/` (written by `valuerank/site/export.py`): `rankings.json`, `plans.json`, `benchmarks.json`, `livebench.json`, `changelog.json`, `benchmarks/terminal-bench-4.json` and `models/<slug>.json`. The output is deterministic: two-space indent, UTF-8, a trailing newline, and `NaN` is rejected.
- **Static files:** `site/assets/`, a copy of `valuerank/site/assets/` that replaces the previous copy; the redirect stubs `/tb4/` and `/coding-agents/`; the archived coding-agents v0.3 page at `/archive/coding-agents-v0.3/`, with an archive banner; `sitemap.xml`; and `robots.txt`.

The build does not read the clock. Its dates come from the snapshots (`observedAt`) and from `valuerank/release.py`.

### Evidence grades

Every value that reaches a page carries an evidence grade, defined in `valuerank/site/evidence.py`: `measured`, `claim`, `estimate` and `assumption`, from strongest to weakest, plus `missing` for a value that does not enter the score. A model's grade is the weakest grade among the values that enter its score. The `badge` partial renders the grade on each page that shows one.

### URL state

Every filter, slider, toggle, sort, column choice, comparison and chart tab is in the query string. The keys are listed in `docs/site-data-contract.md`. `valuerank/site/assets/js/urlstate.js` parses and serialises them (`parseState` and `serializeState`). Keys that equal their default are left out, so a clean URL stays clean. The page writes the state with `history.replaceState`, and a URL value wins over the defaults on load. The theme is the only value stored in the browser: `localStorage`, key `vr-theme`.

### Client modules and lazy charts

The client modules in `valuerank/site/assets/js/` run in the browser. `app.js` holds the shared page behaviour: theme, mobile navigation, basis toggle, URL state sync and FAQ expanders. The rankings instrument is built from `rankings.js`, `filters.js`, `scoring.js`, `compare.js`, `format.js`, `export.js` and `dom.js`. `assets/js/package.json` marks the directory as ES modules. Each module has a Node test under `tests/js/site/`.

Each page type has an entry module in `valuerank/site/assets/js/pages/`. `base.html` loads the modules that the page view lists in `scripts`, as ES modules. `boot.js` wires the shared behaviour, the page's public JSON and the chart layer together. `static.js` serves pages that have no behaviour of their own.

Charts are mounted when their container comes within 200 px of the viewport (`IntersectionObserver` in `valuerank/site/assets/js/charts/index.js`). Plotly loads once, when the first chart mounts, from the pinned build `https://cdn.plot.ly/plotly-2.27.0.min.js` (`charts/plotly-loader.js`). The end-to-end suite blocks that request, so charts render as placeholders there.

## Curated inputs

These files are maintained by hand during a refresh, with their source and observation date recorded inside them:

| File | Content |
|---|---|
| `data/aa_mapping.json` | Model roster: AA identifiers, selected page variants, display names |
| `data/aa_deepswe.json` | Every configuration on AA's DeepSWE v1.1 chart and the exact-variant mapping decisions |
| `data/bug_hunt.json` | Pinned Bug Hunt Bench scoreboard with exact matches and explicit mismatches |
| `data/provider_claims.json` | Provider-published values, eligibility and caveats |
| `data/plan_cost_routes.json` | Subscription routes, value multiples and their evidence |
| `data/aa_reconciliation_inventory.json` | Observed AA Intelligence Index versus total-cost frontier (points to its raw capture through `captureArtifact`) |
| `data/aa_frontier_capture.json` | Raw browser capture of that frontier; the inventory and the capture must agree row for row |
| `data/ranking_history_v1.5.json` | Recorded historical ranks for the changelog and the model history |
| `data/deepswe-browser-2026-09-29.json`, `data/tb4-browser-2026-09-29.json` | Built-in-browser snapshots retained as evidence |

Release metadata (version string and publication date) is defined once in `valuerank/release.py`; `docs/refresh-and-release.md` lists every other place to update.

## Research ledgers

Dated directories under `research/` are immutable records of what was observed and decided during each refresh or investigation. They may cite the pre-2026-10-17 layout; `docs/repository-layout.md` maps old paths to new ones. The frozen `research/2026-09-29-valuerank-refresh-v4-3-2/run_manifest.json` is the snapshot that stage 6 used to copy forward; the live manifest is `data/run_manifest.json`.
