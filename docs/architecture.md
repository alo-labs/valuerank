# Architecture

ValueRank turns pinned benchmark and pricing snapshots into a ranked publication: four Markdown documents at the repository root and a static site under `site/`. The pipeline is a set of independent stages in the `valuerank/` package. Every stage is a plain module with a `main()` function, runs with `python3 -m valuerank.<stage>` from the repository root, and needs only the Python standard library. Two Playwright helpers in `scripts/` capture a client-rendered leaderboard and render share images.

## Design principles

- **Snapshots are the source of truth.** Every number in the publication traces to a committed JSON file under `data/`. Browser captures that cannot be committed (large HTML) are local-only; their decoded form is committed.
- **Exact-variant evidence only.** Results are never transferred between model versions, reasoning efforts or agent harnesses. Missing values stay `null` and each row's available priorities are renormalized; see `methodology.md` for the published policy.
- **Reproducible output.** Stages stamp the observation instant from `valuerank.clock`, which honours `VALUERANK_NOW`. With the instant pinned to the committed value, every offline stage regenerates the committed files byte for byte (`npm run verify:docs`).
- **Generated documents are never edited by hand.** `README.md`, `methodology.md`, `scores.md`, `raw-data.md`, `site/index.html` and `site/tb4/index.html` are outputs of the emitters. Copy changes go into `valuerank/emit_docs.py` or `valuerank/tb4_page.py`.

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
| 8 | `valuerank.emit_docs` | `data/*.json`, `data/plan_cost_routes.json`, `data/ranking_history_v1.5.json`, `site/index.html`, `site/coding-agents/index.html` | `README.md`, `methodology.md`, `scores.md`, `raw-data.md`, `site/index.html`, `site/coding-agents/index.html` | Offline |
| 9 | `valuerank.tb4_page` | `data/tb4.json` | `site/tb4/index.html` | Offline |
| 10 | `scripts/generate-og-cards.mjs` | card definitions in the script | `site/og.png`, `site/tb4/og.png`, `site/coding-agents/og.png` | Playwright |

`npm run refresh` runs the stages in this order (see `package.json`); `npm run build:docs` runs only stages 8 and 9, and `npm run build:publication` adds stage 10.

Stage 6 also embeds `valuerank.plan_costs` (subscription routes from `data/plan_cost_routes.json` turned into effective plan costs) and stage 8 calls `valuerank.aa_reconciliation.reconcile` again to render the frontier comparison tables. `valuerank.site_header` renders the shared navigation, chart-label and table-sort assets that stages 8 and 9 inject into every page.

`valuerank.build_deepswe` converts the historical DeepSWE Best page capture (`data/deepswe-scrape.json`) into `data/deepswe.json`. That file is retained for audit only; current DeepSWE values come from the hand-curated `data/aa_deepswe.json`.

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
| `data/ranking_history_v1.5.json` | Recorded historical ranks for the site history chart |
| `data/deepswe-browser-2026-09-29.json`, `data/tb4-browser-2026-09-29.json` | Built-in-browser snapshots retained as evidence |

Release metadata (version string and publication date) is defined once in `valuerank/release.py`; `docs/refresh-and-release.md` lists every other place to update.

## The site template

`site/index.html` is both the template and the output of stage 8. The emitter reads the committed page, replaces marked regions (chart tabs, FAQ answers, data cards, the `<!-- aa-reconciliation:start -->` and `<!-- plan-candidates:start -->` blocks, version labels) and writes it back. Guard checks raise `SystemExit` or `ValueError` when an expected marker is missing, so a structural change to the page must be made in both the page and the emitter. Running the emitter repeatedly is a fixed point; `tests/test_emit_docs_idempotent.py` enforces that.

`site/coding-agents/index.html` is a historical page: the emitter only refreshes its header and historical labels. The TB4 page is regenerated from a template string inside `valuerank/tb4_page.py`.

## Research ledgers

Dated directories under `research/` are immutable records of what was observed and decided during each refresh or investigation. They may cite the pre-2026-10-17 layout; `docs/repository-layout.md` maps old paths to new ones. The frozen `research/2026-09-29-valuerank-refresh-v4-3-2/run_manifest.json` is the snapshot that stage 6 used to copy forward; the live manifest is `data/run_manifest.json`.
