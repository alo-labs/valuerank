#!/bin/bash
# Regenerate every output at the v5 release cutoff (O132): scores, scenarios, scores again, docs, OG cards, the draft.
set -e
cd "$(dirname "$0")/../.."
export VALUERANK_NOW=2026-10-31T04:10:00Z
python3 -m valuerank.build_scores >/dev/null
python3 -m valuerank.value_v3 scenarios >/dev/null
python3 -m valuerank.build_scores >/dev/null
python3 -m valuerank.aa_reconciliation >/dev/null || true
npm run -s build:docs >/dev/null
npm run -s generate:og >/dev/null 2>&1 || true
python3 -m valuerank.draft_figures render
python3 -m valuerank.draft_figures check && echo CHECK_OK
