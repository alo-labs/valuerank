# Refresh and release procedure

A refresh captures new source data, recomputes the ranking and regenerates the publication. A release is a refresh plus a version bump, a verified commit on `main` and the GitHub Pages deployment that follows automatically.

## Before you start

- Read `AGENTS.md`: the model-inclusion policy (every model family on the AA Intelligence Index versus total-cost Pareto frontier, plus every near-frontier family within 3 Index points of it at its cost), the exact-variant evidence rules and the subscription-allowance evidence rules are binding on every refresh.
- Work on a clean `main` with `npm run verify` passing.
- Install the Python dependencies in the virtual environment (`.venv/bin/python -m pip install -r requirements.txt -r requirements-dev.txt`) and Playwright Chromium (`npx playwright install chromium`).

## 1. Capture and curate sources

Capture the AA chart first. In the built-in browser open AA's "Intelligence Index vs. Cost to Run" chart, select the complete catalog and capture every plotted point (not only the vertices of the Pareto line) together with the rendered line and any footnote shown on the chart. Then list the frontier and near-frontier families against the roster:

```bash
python3 -m valuerank.frontier <capture> --roster data/aa_mapping.json
```

The command prints each family on the rendered frontier and each near-frontier family (public Index within 3 points of the frontier at its cost), and whether the roster already has it. Add every missing family to `data/aa_mapping.json` (or record a dated, reasoned deferral) before running `npm run build:aa`. Frontier membership is the line AA renders as observed, never recomputed from rounded values.

Automated captures:

```bash
npm run refresh:external   # LiveBench (HTTPS) and Terminal-Bench 4.0 (Playwright) -> data/livebench.json, data/tb4.json
npm run capture:deepswe    # AA DeepSWE v1.1 coding-agent chart (HTTPS, page payload) -> data/aa_deepswe.json
npm run build:aa           # AA model pages (HTTPS) -> data/aa/aa_v432_snapshot.json -> data/aa_metrics.json
npm run capture:basket     # AA Coding Agent Index (with safety-refusal counts, O63) and cost charts -> data/aa/coding_agents_capture.json, data/aa/cost_charts_capture.json
```

`npm run refresh` runs all of these. The basket captures must be within 7 days of the model-page snapshot and not after the release cutoff (E217, O65); AA data read after the cutoff moves the cutoff and every AA source is re-captured. After each capture, review `data/aa/coding_agents_manifest.json` (O64): a new, relabelled or vanished Coding Agent Index row stops the build until it is registered. Classify every note the captures record in `data/aa/aa_footnote_register.json` by its exact text (O100): the chart's footnotes, and from the first capture later than the 2026-10-25T09:56:47Z release captures the notes AA prints on model pages, the Coding Agent Index and the cost charts, which each capture must record verbatim in a `notes` list per row, page and chart (O103); a pricing omission registered on any of them makes the row an O94 row when its chart or index is admitted to the ranking's cost workload (O106, O108, O109). Record every documented plan change as a typed record (limit, price, credit, availability or metering; O99, O105, O111): the build derives each route's label and blocking dates from them, within the measurement's span bounded by its model's launch and stated schedule (O107, O110). The capture scripts (`valuerank.capture_aa`, `valuerank.capture_coding_agents`, `scripts/capture-aa-cost-charts.js`, whose cost-chart legend is today hard-coded as `DECLINED_NOTE`) do not record notes yet and must be extended to record them, the legend verbatim, before the next refresh; until then the build stops on a new capture. An unregistered or changed note, a row whose inventory note differs from the chart capture, or a post-O103 capture without `notes` stops the build.

The AA page capture decodes each model page's payload object keyed by the page slug. `capture:deepswe` records every configuration that has a DeepSWE evaluation at the owner's full precision.

Hand-curated snapshots (record the observation date and source inside each file):

- `data/aa_deepswe.json`: exact-variant mapping decisions for the captured DeepSWE v1.1 configurations (the configurations themselves come from `npm run capture:deepswe`).
- `data/bug_hunt.json`: the Bug Hunt Bench scoreboard pinned to a commit.
- `data/aa_reconciliation_inventory.json`: the observed AA frontier (the reconciliation gate rejects inventories older than 7 days).
- `data/aa_mapping.json`: add or retire roster entries when the frontier changes.
- `data/provider_claims.json`, `data/plan_cost_routes.json`: provider claims and subscription routes with their evidence.

Document the refresh in a new dated directory under `research/` (sources, evidence, decisions). Earlier refresh records such as `research/2026-09-29-valuerank-refresh-v4-3-2/` show the expected shape.

## 2. Bump the version

Update every version site together. `tests/test_release_metadata.py` fails when the manifests disagree with `valuerank/release.py`.

| Location | Field |
|---|---|
| `valuerank/release.py` | `VERSION`, `DATE`, `SHORT_DATE`. This is the only file that names the version. The emitter, the site build and the score builder import it. |
| `package.json`, `pyproject.toml` | `version` (without the leading `v`) |
| `data/ranking_history_v1.5.json` | Earlier releases' API-basis ranks, one key per release: `v` followed by three digits (`v150` for 1.5.0, `v196` for 1.9.6). Before the bump, add the outgoing release's API-basis ranks under its key so that the changelog keeps them. The current release is computed at build time and is not stored in this file. |
| `tests/conftest.py` and the test literals | After `npm run build:scores` has stamped the new instant into `data/ranking_summary.json`, replace the previous instant in `tests/conftest.py` (`pinned_clock`) and in every test that asserts it, so the golden tests regenerate the committed publication from the same clock that produced it. |

`data/ranking_summary.json` also carries the version and date. `npm run build:scores` regenerates it, and the release test checks it.

## 3. Score, reconcile and emit

```bash
npm run build:scores        # data/scores.json, data/coverage_matrix.json, data/ranking_summary.json, data/run_manifest.json
npm run reconcile:aa        # data/aa_reconciliation_report.json; exit 1 blocks the release when the frontier is stale or incomplete
npm run build:publication   # README.md, methodology.md, scores.md, raw-data.md (emitter); site/** (site build); site/og/** (OG cards)
```

Do not set `VALUERANK_NOW` during a real refresh: the stamped instant must be the actual observation time. Afterwards, `data/ranking_summary.json` holds that instant, and `npm run verify:docs` reproduces the outputs from it.

`site/` is generated in full, so never edit a file under `site/` by hand. Change the snapshots, `valuerank/site/` (view models, templates or assets) or the data contract in `docs/site-data-contract.md`, then run `npm run build:publication`. The build replaces `site/assets/`, rewrites the pages, and removes model pages for models that left the roster.

The OG script (`npm run generate:og`) writes the share cards on every publication build, one per core page (`site/og/<key>.png`), one per roster model (`site/og/models/<slug>.png`) and `site/og/archive.png`, all read from `site/data/`, and its pixels are only checked by eye, so look at the home card and one model card after each release.

## 4. Verify

```bash
npm run verify
```

This runs the Python, Node and end-to-end suites with their coverage gates, then regenerates the documents and the site with the clock pinned to the newly stamped instant. It fails on any difference in the tracked files. The command is the same as before; it now also runs the end-to-end suite.

After it passes, review `git status --short`. Local captures and logs are ignored and must stay so. New files under `site/` must be the ones you expect, because `git diff` does not list untracked files. Read the regenerated `README.md` ranking table once as a human, and check the home page and the rankings page with `npm run preview`.

## 5. Commit and deploy

Commit the generated documents, the regenerated `site/`, the `data/` snapshots, the research record and the version bump in one commit, with a subject such as `Publish ValueRank v1.9.7 with …`.

Pushing to `main` triggers `.github/workflows/deploy.yml`. It runs the CI checks, then uploads the committed `site/` directory to GitHub Pages without rebuilding it. The commit must therefore contain everything the site needs. The custom domain is set by `site/CNAME` (`valuerank.alolabs.dev`).

## Rolling back

The published site is whatever is committed under `site/`. Revert the publication commit and push. The deployment workflow then republishes the previous `site/`.
