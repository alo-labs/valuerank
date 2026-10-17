# Archived v1.3.1 refresh pipeline

This directory is the retired pipeline and its source snapshots for ValueRank v1.3.1 and the coding-agents v0.3 page (`coding-agents-valuerank/`, `site/coding-agents/`). It was moved here from `.refresh/v1.3/` on 2026-10-17 and is kept only as provenance for those historical publications.

- Nothing in the current pipeline (`valuerank/`) imports or reads from this directory.
- The scripts (`build_v13_scores.py`, `emit_v131_docs.py`, `extract_aa_metrics.py`, `coding-agents/*.js`, `scrape_*.js`) still reference the old layout and are not maintained or tested.
- Browser HTML captures, screenshots and logs in this directory are local-only and ignored by git; the JSON and text evidence is tracked.

The current coding-agents page is only patched (header and historical labels) by `valuerank.emit_docs`; a future independent coding-agents refresh should start from the current pipeline rather than from these scripts.
