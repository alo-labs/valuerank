# 2026-11-26 re-capture (the "next release" after v3.0.0)

Status: in progress. Nothing under `data/` has been changed yet.

## What AA looks like today (captured 2026-11-26T02:18:20Z)
- Intelligence Index **v5.0.2** (the 2026-11-01 release used v5.0). The chart: 155 models selected, 136 plotted circles, one Pareto path.
- Coding Agent Index **v2.1** (was v2.0): FrontierCode-AA 2.0, **Terminal-Bench 4.1**, SWE-Atlas-QnA-AA. The Index's evaluation list now has `terminalbench-4-1` where the engine has `terminalbench-4-0`.
- AA dropped the " with fallback" wording from the Claude chart labels; the pages still say "Default Fallback", slugs and costs are unchanged (Opus 5.5 (max) $8,909.67, Index 59 now, was 58).
- Rendered frontier (19 configurations) and near gap (11): GPT-6 Luna low/high, Claude Haiku 5.5 low/medium, Muse Ember xhigh/max, GPT-6.1 Terra medium/high, GPT-6.2 Sol low..max, GPT-6.1 Sol medium, GPT-6.2 Astra high/xhigh/max, Claude Fable 5.2 xhigh/max; near: Fable 5.2 high, Gemini 4 Neon xhigh/high/medium, Gemini 4 Carbon high, Opus 5.5 max, GPT-6.2 Astra medium, GPT-6.1 Sol max, GPT-6.1 Terra xhigh, Haiku 5.5 xhigh, GPT-6 Luna xhigh. Retained one release (O145): 14 configurations that left. Cohort 44 (`cohort.json`, `urls.json`).
- Two overlapped circles return the topmost circle's tooltip. The hidden frontier circle (id 36667da0-…, fill #1f1f1f) is GPT-6 Luna (medium): its id equals the model page's `model.id`, Index 18.45 (shows 18), cost $39.55. Handle it by id, not by tooltip.
- Bug Hunt Bench (updated 2026-11-25, 226 runs) now covers GPT-6.2 Sol/Astra, Fable 5.2, Gemini 4 Neon/Hydrogen/Carbon/Argon, Muse Spark 1.3.

## Scripts here
`capture_chart.mjs` (adds overlapped-circle handling), `build_cohort.py` (cohort and `urls.json` from AA family pages), `build_inputs.py` (patched for `urls.json` and the index version); the other scripts are copies of the 2026-11-01 ones and still need adapting.

## Open points
Scope and panel re-review after the migration; Terminal-Bench leaf 4.0 to 4.1; Index naming (v5.0.2); Gemini 4 Carbon introductory price; GDP.pdf leaf; the plan-side three-stage search for OpenAI, Meta, Anthropic (Fable 5.2) and Google plans.
