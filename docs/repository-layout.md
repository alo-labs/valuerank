# Repository layout

ValueRank is a research workspace with a small reproducible publication pipeline. Keep canonical inputs and generators separate from local captures and rendered QA output.

## Canonical product surface

- `README.md` — current root ValueRank overview and published ranking snapshot.
- `methodology.md` — current cohort, dimensions, weights, normalization, and source policy.
- `raw-data.md` — current source-backed benchmark and cost inputs.
- `scores.md` — current normalized matrix, ranking, and Pareto frontier.
- `coding-agents-valuerank/` — separate harness/model/effort-variant ranking.
- `site/` — committed static GitHub Pages output.

## Refresh pipeline

`.refresh/v1.3/` contains the current extraction, scoring, evidence, and document-emission pipeline. Its canonical text/JSON snapshots and scripts are committed because they are needed to reproduce the published documents. Browser HTML captures, screenshots, logs, and failed-agent output are local-only and ignored.

The coding-agent refresh is under `.refresh/v1.3/coding-agents/`. The Open Graph generator is `scripts/site-generate-og-cards.mjs` and can be run with `npm run generate:og` after installing the root Node dependencies.

## Research and supporting analyses

- `benchmarks/` — benchmark-specific research packages, including the C25 versus MiMo comparison.
- `research/code-quality/` — static-analysis benchmark research.
- `research/deep-research-skills/` — durable multi-agent deep-research reports and evidence ledgers.
- `research/kimi/` — durable Kimi model and pricing notes.
- `research/pi/` — Pi benchmark and skills research.
- `research/agent-benchmarks/` — other benchmark summaries such as LoCoBench.
- `research/sources/` — local source documents only; ignored because source files may be licensed or confidential.

## Auxiliary projects

- `projects/nz-egg-market/market-structure/` — the ReportLab generator and selected final PDF for the separate NZ egg-market infographic.
- `projects/nz-egg-market/source-corpus/` — local source corpus for that project; ignored and never staged by default.
- `projects/coderstrust/` — separate competitor-research material; local source captures are ignored.

## Local-only output

Do not commit installed environments, browser/tool state, graphify output, visual-audit captures, screenshots, logs, or generated chart files. They are reproducible and ignored by `.gitignore`:

- `.venv/`, `node_modules/`
- `.claude/`, `.opencode/`
- `graphify-out/`, `.visual-audit/`, `.runs/`, `.tmp/`
- `artifacts/`, `benchmark-runs/`, `multi-ai-deep-research-out/`

## Reproducibility

```text
python3 -m venv .venv
python3 -m pip install -r requirements.txt
npm install
npm run generate:og
```

The refresh scripts currently use the absolute project root captured in their configuration. If the repository is cloned elsewhere, update that configuration before running a full refresh.
