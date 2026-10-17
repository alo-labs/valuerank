# Refresh and release procedure

A refresh captures new source data, recomputes the ranking and regenerates the publication. A release is a refresh plus a version bump, a verified commit on `main` and the GitHub Pages deployment that follows automatically.

## Before you start

- Read `AGENTS.md`: the model-inclusion policy (every model on the AA Intelligence Index versus total-cost Pareto frontier), the exact-variant evidence rules and the subscription-allowance evidence rules are binding on every refresh.
- Work on a clean `main` with `npm run verify` passing.
- Have Playwright Chromium installed (`npx playwright install chromium`).

## 1. Capture and curate sources

Automated captures:

```bash
npm run refresh:external   # LiveBench (HTTPS) and Terminal-Bench 4.0 (Playwright) -> data/livebench.json, data/tb4.json
npm run build:aa           # AA model pages (HTTPS) -> data/aa/aa_v432_snapshot.json -> data/aa_metrics.json
```

Hand-curated snapshots (record the observation date and source inside each file):

- `data/aa_deepswe.json`: every configuration on AA's DeepSWE v1.1 chart with exact-variant mapping decisions.
- `data/bug_hunt.json`: the Bug Hunt Bench scoreboard pinned to a commit.
- `data/aa_reconciliation_inventory.json`: the observed AA frontier (the reconciliation gate rejects inventories older than 7 days).
- `data/aa_mapping.json`: add or retire roster entries when the frontier changes.
- `data/provider_claims.json`, `data/plan_cost_routes.json`: provider claims and subscription routes with their evidence.

Document the refresh in a new dated directory under `research/` (sources, evidence, decisions). Earlier refresh records such as `research/2026-09-29-valuerank-refresh-v4-3-2/` show the expected shape.

## 2. Bump the version

Update every version site together; `tests/test_release_metadata.py` fails when they disagree:

| Location | Field |
|---|---|
| `valuerank/release.py` | `VERSION`, `DATE`, `SHORT_DATE` (the only code that names the version) |
| `valuerank/emit_docs.py` | the site version-history lists (`const versions = [...]`) |
| `package.json`, `pyproject.toml` | `version` (without the leading `v`) |
| `data/ranking_history_v1.5.json` | add the new release's recorded ranks |

## 3. Score, reconcile and emit

```bash
npm run build:scores     # data/scores.json, data/coverage_matrix.json, data/ranking_summary.json, data/run_manifest.json
npm run reconcile:aa     # data/aa_reconciliation_report.json; exit 1 blocks the release when the frontier is stale or incomplete
npm run build:publication  # README.md, methodology.md, scores.md, raw-data.md, site/**, site/**/og.png
```

Do not set `VALUERANK_NOW` during a real refresh: the stamped instant must be the actual observation time. Afterwards, `data/ranking_summary.json` holds that instant and `npm run verify:docs` will reproduce the outputs from it.

## 4. Verify

```bash
npm run verify
```

This runs the Python and Node suites with their 100% coverage gates and then regenerates the documents with the clock pinned to the newly stamped instant, failing on any difference. Also review `git diff --stat` for unexpected files (local captures and logs are ignored and must stay so) and read the regenerated `README.md` ranking table once as a human.

## 5. Commit and deploy

Commit the generated documents, `data/` snapshots, the research record and the version bump in one commit with a subject such as `Publish ValueRank v1.9.7 with …`. Pushing to `main` triggers `.github/workflows/deploy.yml`, which runs the CI checks and then deploys `site/` to GitHub Pages at https://alo-labs.github.io/valuerank. The custom domain is configured through `site/CNAME`.

## Rolling back

The site is a pure function of `main`. Revert the publication commit and push; the deployment workflow republishes the previous `site/`.
