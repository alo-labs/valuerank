# ValueRank v3.0.0 Scores

**Updated:** October 19, 2026 · methodology 3.0.0 · SDLC basket v1 · anchor version `v3-2026-10-31`

Value = 25% × cost score + 75% × quality. Costs are USD per basket run; the cost score is log-scaled against the frozen anchors of the row's workload (see [methodology.md](methodology.md)).

## Ranking

| Configuration | Plan rank | Plan value | Plan cost score | API rank | API value | API cost score | Quality | Quality coverage | Workload |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| [Claude Opus 5.5 (max)](https://valuerank.alolabs.dev/models/claude-opus-5-5/) | 1 | 60.95 | 41.58 | 4 | 53.72 | 12.67 | 67.40 | 100% | main |
| [Claude Sonnet 5.5 (max)](https://valuerank.alolabs.dev/models/claude-sonnet-5-5/) | 4 | 60.01 | 41.33 | 5 | 52.78 | 12.43 | 66.23 | 100% | main |
| [GPT-6.1 Sol (max)](https://valuerank.alolabs.dev/models/gpt-6-1-sol/) | 7 | 59.61 | 47.33 | 1 | 59.96 | 48.73 | 63.71 | 100% | main |
| [GPT-6 Astra (max)](https://valuerank.alolabs.dev/models/gpt-6-astra/) | 11 | 54.74 | 23.48 | 3 | 53.92 | 20.20 | 65.16 | 100% | main |
| [GPT-6 Luna (max)](https://valuerank.alolabs.dev/models/gpt-6-luna/) | 14 | 54.15 | 87.23 | 2 | 54.24 | 87.57 | 43.13 | 100% | main |

## Not ranked

| Model | Reasons |
|---|---|
| Claude Haiku 5.5 (high) | Not in the max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall; ranked in the AI Coding Daily ranking, common-leaf diagnostic ranking |
| Claude Haiku 5.5 (low) | Incomplete benchmark evidence after an exhaustive search (O36, O53): Max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall; AI Coding Daily ranking: no AI Coding Daily (excl. bug finding) |
| Claude Haiku 5.5 (medium) | Not in the max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall; ranked in the AI Coding Daily ranking, common-leaf diagnostic ranking |
| Claude Opus 5.5 (high) | Not in the max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall; ranked in the AI Coding Daily ranking, common-leaf diagnostic ranking |
| Claude Opus 5.5 (xhigh) | Incomplete benchmark evidence after an exhaustive search (O36, O53): Max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall; AI Coding Daily ranking: no AI Coding Daily (excl. bug finding) |
| GPT-6 Astra (high) | Not in the max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall; ranked in the AI Coding Daily ranking, common-leaf diagnostic ranking |
| GPT-6 Astra (xhigh) | Incomplete benchmark evidence after an exhaustive search (O36, O53): Max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall; AI Coding Daily ranking: no AI Coding Daily (excl. bug finding) |
| GPT-6 Luna (high) | Not in the max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall; ranked in the AI Coding Daily ranking, common-leaf diagnostic ranking |
| GPT-6 Luna (low) | Incomplete benchmark evidence after an exhaustive search (O36, O53): Max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall; AI Coding Daily ranking: no AI Coding Daily (excl. bug finding) |
| GPT-6 Luna (medium) | Not in the max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall; ranked in the AI Coding Daily ranking, common-leaf diagnostic ranking |
| GPT-6 Luna (xhigh) | Not in the max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall; ranked in the AI Coding Daily ranking, common-leaf diagnostic ranking |
| GPT-6.1 Sol (high) | Not in the max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall; ranked in the AI Coding Daily ranking, common-leaf diagnostic ranking |
| GPT-6.1 Sol (low) | Not in the max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall; ranked in the AI Coding Daily ranking, common-leaf diagnostic ranking |
| GPT-6.1 Sol (medium) | Not in the max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall; ranked in the AI Coding Daily ranking, common-leaf diagnostic ranking |
| GPT-6.1 Sol (xhigh) | Incomplete benchmark evidence after an exhaustive search (O36, O53): Max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall; AI Coding Daily ranking: no AI Coding Daily (excl. bug finding) |
| GPT-6.1 Terra (high) | Not in the max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall; ranked in the AI Coding Daily ranking, common-leaf diagnostic ranking |
| GPT-6.1 Terra (low) | Incomplete benchmark evidence after an exhaustive search (O36, O53): Max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall; AI Coding Daily ranking: no AI Coding Daily (excl. bug finding) |
| GPT-6.1 Terra (max) | Not in the max-effort ranking: no Code Migration v1.1 (Vals); ranked in the AI Coding Daily ranking, common-leaf diagnostic ranking |
| GPT-6.1 Terra (medium) | Not in the max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall; ranked in the AI Coding Daily ranking, common-leaf diagnostic ranking |
| GPT-6.1 Terra (xhigh) | Not in the max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall; ranked in the AI Coding Daily ranking, common-leaf diagnostic ranking |
| Gemini 4 Carbon | Incomplete benchmark evidence after an exhaustive search (O36, O53): Max-effort ranking: no Bug Hunt Bench, Code Migration v1.1 (Vals), LiveBench 2.0 Overall; AI Coding Daily ranking: no Bug Hunt Bench, AI Coding Daily (excl. bug finding) |
| MiMo-V2.6-Flash | Incomplete benchmark evidence after an exhaustive search (O36, O53): Max-effort ranking: no Bug Hunt Bench, Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall; AI Coding Daily ranking: no Bug Hunt Bench |

## Quality leaf scores

Each leaf's score z on its fixed 0–100 anchors; "—" marks a leaf with no eligible exact-configuration result.

| Configuration | FrontierCode 2.0 | Terminal-Bench 4.0 (AA run) | Bug Hunt Bench | Vibe Code Bench v1.1 (Vals) | Code Migration v1.1 (Vals) | LiveBench 2.0 Overall | GDPval-AA v2.1 | AutomationBench-AA | AA-Omniscience v1.1 | AA-LCR v1.1 | HLE-Diamond | Terminal-Bench-Science 0.1 | CritPt v2 (hard subset) | Quality | Provisional |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Claude Opus 5.5 (max) | 46.4 | 59.6 | 39.7 | 90.3 | 81.0 | 85.1 | 68.3 | 69.5 | 74.1 | 84.7 | 67.9 | 59.0 | 61.0 | 67.40 | no |
| Claude Sonnet 5.5 (max) | 41.7 | 63.6 | 48.9 | 92.4 | 86.9 | 80.0 | 66.9 | 71.8 | 65.2 | 82.7 | 53.3 | 53.3 | 56.0 | 66.23 | no |
| GPT-6.1 Sol (max) | 40.6 | 56.1 | 42.2 | 88.9 | 77.3 | 84.1 | 55.4 | 64.9 | 71.0 | 83.0 | 58.8 | 58.1 | 68.5 | 63.71 | no |
| GPT-6 Astra (max) | 42.4 | 59.1 | 42.9 | 89.6 | 80.6 | 85.6 | 54.2 | 68.5 | 71.2 | 80.7 | 63.8 | 63.3 | 70.5 | 65.16 | no |
| GPT-6 Luna (max) | 25.2 | 12.6 | 17.4 | 81.6 | 46.7 | 64.6 | 47.2 | 53.2 | 45.9 | 83.3 | 22.2 | 8.6 | 41.5 | 43.13 | no |

## AI Coding Daily ranking

The configurations AI Coding Daily has tested, mostly at high and medium effort, scored on the AA leaves plus AI Coding Daily. Anchor version `v3-2026-10-31-aicd`; leaves: FrontierCode 2.0 21%, Terminal-Bench 4.0 (AA run) 17%, Bug Hunt Bench 12%, AI Coding Daily (excl. bug finding) 10% (software engineering 60%), plus the 7 leaves outside software engineering every ranking shares.

| Configuration | Plan rank | Plan value | Plan cost score | API rank | API value | API cost score | Quality | Quality coverage | Workload |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| [Claude Opus 5.5 (high)](https://valuerank.alolabs.dev/models/claude-opus-5-5-high/) | 1 | 54.23 | 46.66 | 8 | 46.16 | 14.41 | 56.75 | 100% | main |
| [GPT-6.1 Sol (high)](https://valuerank.alolabs.dev/models/gpt-6-1-sol-high/) | 4 | 52.88 | 44.73 | 1 | 52.19 | 41.98 | 55.59 | 100% | main |
| [Claude Haiku 5.5 (high)](https://valuerank.alolabs.dev/models/claude-haiku-5-5-high/) | 8 | 52.72 | 98.73 | 11 | 45.30 | 69.06 | 37.38 | 100% | main |
| [GPT-6.1 Terra (max)](https://valuerank.alolabs.dev/models/gpt-6-1-terra/) | 11 | 51.98 | 39.74 | 3 | 51.23 | 36.75 | 56.06 | 100% | main |
| [GPT-6.1 Sol (medium)](https://valuerank.alolabs.dev/models/gpt-6-1-sol-medium/) | 12 | 51.96 | 50.47 | 2 | 51.34 | 48.01 | 52.46 | 100% | main |
| [Claude Haiku 5.5 (medium)](https://valuerank.alolabs.dev/models/claude-haiku-5-5-medium/) | 19 | 49.47 | 100.00 | 14 | 43.82 | 77.40 | 32.63 | 100% | main |
| [GPT-6.1 Terra (high)](https://valuerank.alolabs.dev/models/gpt-6-1-terra-high/) | 22 | 49.35 | 57.45 | 4 | 48.82 | 55.33 | 46.65 | 100% | main |
| [GPT-6.1 Terra (xhigh)](https://valuerank.alolabs.dev/models/gpt-6-1-terra-xhigh/) | 23 | 49.29 | 51.92 | 5 | 48.69 | 49.54 | 48.41 | 100% | main |
| [GPT-6 Astra (high)](https://valuerank.alolabs.dev/models/gpt-6-astra-high/) | 28 | 48.28 | 21.16 | 9 | 46.01 | 12.08 | 57.32 | 100% | main |
| [GPT-6.1 Terra (medium)](https://valuerank.alolabs.dev/models/gpt-6-1-terra-medium/) | 29 | 48.27 | 62.49 | 6 | 47.81 | 60.62 | 43.53 | 100% | main |
| [GPT-6.1 Sol (low)](https://valuerank.alolabs.dev/models/gpt-6-1-sol-low/) | 37 | 46.94 | 58.45 | 7 | 46.42 | 56.38 | 43.10 | 100% | main |
| [GPT-6 Luna (max)](https://valuerank.alolabs.dev/models/gpt-6-luna/) | 41 | 46.08 | 69.76 | 10 | 45.71 | 68.26 | 38.19 | 100% | main |
| [GPT-6 Luna (xhigh)](https://valuerank.alolabs.dev/models/gpt-6-luna-xhigh/) | 46 | 44.30 | 76.24 | 12 | 44.01 | 75.06 | 33.65 | 100% | main |
| [GPT-6 Luna (high)](https://valuerank.alolabs.dev/models/gpt-6-luna-high/) | 48 | 44.17 | 81.15 | 13 | 43.94 | 80.21 | 31.85 | 100% | main |
| [GPT-6 Luna (medium)](https://valuerank.alolabs.dev/models/gpt-6-luna-medium/) | 54 | 42.46 | 88.49 | 15 | 42.32 | 87.92 | 27.11 | 100% | main |

### AI Coding Daily ranking: quality leaf scores

| Configuration | FrontierCode 2.0 | Terminal-Bench 4.0 (AA run) | Bug Hunt Bench | AI Coding Daily (excl. bug finding) | GDPval-AA v2.1 | AutomationBench-AA | AA-Omniscience v1.1 | AA-LCR v1.1 | HLE-Diamond | Terminal-Bench-Science 0.1 | CritPt v2 (hard subset) | Quality | Provisional |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Claude Opus 5.5 (high) | 35.9 | 56.6 | 30.2 | 96.1 | 60.7 | 63.2 | 71.2 | 82.7 | 55.6 | 49.0 | 58.0 | 56.75 | no |
| GPT-6.1 Sol (high) | 36.7 | 51.5 | 34.8 | 94.7 | 51.0 | 64.5 | 70.5 | 82.3 | 51.9 | 46.2 | 67.5 | 55.59 | no |
| Claude Haiku 5.5 (high) | 23.2 | 21.7 | 15.2 | 85.9 | 46.2 | 33.7 | 52.6 | 77.3 | 23.7 | 10.0 | 42.5 | 37.38 | no |
| GPT-6.1 Terra (max) | 42.3 | 55.6 | 38.8 | 87.5 | 48.8 | 60.2 | 64.8 | 82.7 | 47.3 | 57.6 | 64.5 | 56.06 | no |
| GPT-6.1 Sol (medium) | 33.4 | 48.0 | 27.6 | 92.8 | 48.0 | 62.6 | 70.1 | 83.3 | 46.0 | 37.1 | 65.0 | 52.46 | no |
| Claude Haiku 5.5 (medium) | 16.1 | 15.2 | 11.4 | 85.5 | 39.1 | 28.6 | 52.1 | 77.3 | 16.8 | 7.1 | 30.0 | 32.63 | no |
| GPT-6.1 Terra (high) | 37.5 | 41.9 | 9.2 | 77.8 | 42.6 | 58.5 | 63.9 | 82.3 | 35.4 | 33.3 | 60.5 | 46.65 | no |
| GPT-6.1 Terra (xhigh) | 36.9 | 46.5 | 10.8 | 80.2 | 45.7 | 59.9 | 64.5 | 81.7 | 42.3 | 41.9 | 57.5 | 48.41 | no |
| GPT-6 Astra (high) | 40.1 | 54.0 | 33.3 | 94.6 | 51.8 | 66.6 | 72.3 | 80.0 | 59.3 | 59.5 | 71.5 | 57.32 | no |
| GPT-6.1 Terra (medium) | 34.5 | 32.3 | 7.0 | 78.2 | 41.2 | 57.8 | 63.3 | 80.7 | 31.3 | 24.8 | 56.0 | 43.53 | no |
| GPT-6.1 Sol (low) | 20.2 | 30.8 | 21.4 | 87.8 | 41.1 | 52.6 | 69.0 | 84.0 | 38.2 | 11.0 | 59.5 | 43.10 | no |
| GPT-6 Luna (max) | 25.2 | 12.6 | 17.4 | 86.7 | 47.2 | 53.2 | 45.9 | 83.3 | 22.2 | 8.6 | 41.5 | 38.19 | no |
| GPT-6 Luna (xhigh) | 18.4 | 8.1 | 13.3 | 83.2 | 43.6 | 47.8 | 43.5 | 80.0 | 18.9 | 5.2 | 35.5 | 33.65 | no |
| GPT-6 Luna (high) | 18.6 | 4.5 | 8.6 | 79.5 | 42.6 | 47.8 | 43.6 | 79.3 | 15.6 | 2.9 | 30.5 | 31.85 | no |
| GPT-6 Luna (medium) | 12.8 | 2.5 | 3.8 | 67.0 | 38.5 | 40.5 | 43.2 | 78.3 | 15.1 | 1.4 | 26.0 | 27.11 | no |

### AI Coding Daily ranking: displayed record and noise

- API basis, displayed record (not a claim; E203): cheapest at or above quality 43.5: GPT-6.1 Terra (medium) ($174.91 per basket run; 8 reach it); at or above quality 33.7: GPT-6 Luna (xhigh) ($76.38 per basket run; 12 reach it); at or above quality 52.5: GPT-6.1 Sol (medium) ($360.71 per basket run; 5 reach it).
- API basis, noise-margin companion (O44; each bar plus 5.6 quality points, so the bar's own configuration cannot decide it): cheapest at or above quality 49.2: GPT-6.1 Sol (medium) ($360.71 per basket run); at or above quality 39.3: GPT-6.1 Terra (medium) ($174.91 per basket run); at or above quality 58.1: none.
- Plan basis, displayed record (not a claim; E203): cheapest at or above quality 43.5: GPT-6.1 Terra (medium) on ChatGPT Pro 500 ($16.24 per basket run; 31 reach it); at or above quality 33.7: Claude Haiku 5.5 (high) on Claude Pro ($1.83 per basket run; 46 reach it); at or above quality 52.5: GPT-6.1 Sol (medium) on ChatGPT Pro 500 ($33.49 per basket run; 19 reach it).
- Plan basis, noise-margin companion (O44; each bar plus 5.6 quality points, so the bar's own configuration cannot decide it): cheapest at or above quality 49.2: GPT-6.1 Sol (medium) on ChatGPT Pro 500 ($33.49 per basket run); at or above quality 39.3: GPT-6.1 Terra (medium) on ChatGPT Pro 500 ($16.24 per basket run); at or above quality 58.1: none.
- AA cost caveat (O94; ranked at the published cost, no label of its own) on these bars' cheapest rows: Claude Haiku 5.5 (high) (AA's cost omits a pricing term; up to 5× on its cost).
- Plan route flags on these bars' cheapest plan rows: Claude Haiku 5.5 (high) on Claude Pro (possibly-superseded); GPT-6.1 Sol (medium) on ChatGPT Pro 500 (possibly-superseded, measured inside an acknowledged accounting-fault window (O91, O92)); GPT-6.1 Terra (medium) on ChatGPT Pro 500 (possibly-superseded, measured inside an acknowledged accounting-fault window (O91, O92)).
- These outputs compare ranked configurations only; listed families shown with an indicative value (O41) are outside them (O43): GPT-6.1 Sol (max), Claude Opus 5.5 (max), Claude Sonnet 5.5, GPT-6 Astra (max), Claude Haiku 5.5 (low), Claude Opus 5.5 (xhigh), GPT-6 Astra (xhigh), GPT-6 Luna (low), GPT-6.1 Sol (xhigh), GPT-6.1 Terra (low), Gemini 4 Carbon, MiMo-V2.6-Flash.

Benchmark sampling noise (O39, an independent-task approximation): two values must differ by about 4.2 value points (median, 95%) to separate, and 0 of 14 adjacent API ranks and 0 of 33 adjacent Plan ranks of different configurations do (23 more adjacent Plan pairs are one configuration on two plans, ordered by the plans' multiples alone; E258). Its net direction is not established: every configuration is scored on the same tasks, which correlates their errors and narrows the true threshold (API 0 at correlation 0.3, 0 at correlation 0.6; Plan 0 at correlation 0.3, 0 at correlation 0.6), while sources it leaves out widen it (run-to-run and harness variance, AA's single cost run and, for the 38 Plan rows on an owner assumption (38 owner-named transfers), that assumption's error). The noise band column groups each row with the band's first row it cannot be told apart from (O42); a Plan band marked † rests on an owner assumption (an owner-named transfer or an O46 provider quota ceiling) and excludes its error: an assumed multiple can be wrong by a factor of about 2.9 before the row's value moves by the median threshold (a tolerance, not an estimate of the assumption's error). The S1T scenario shares in [scores.md](scores.md) show each row's rank-1 and top-3 frequencies under that noise. AI Coding Daily's noise treats its six graded projects as six trials of the share of 60 points (n = 6, the wide reading, E263); read as 60 trials, the median threshold would be 3.0 (API) and 3.1 (Plan), with 0 and 0 adjacent ranks separable.


**Listed frontier families: indicative value, not ranked and not comparable (O41).** Quality is the mean over the leaves the configuration has, renormalised, with no imputation, so these values cannot be compared with the ranking above.

| Configuration | Missing | Quality (remaining leaves) | Quality coverage | Plan value (indicative) | API value (indicative) | API cost (USD per basket run) | Plan cost (USD per basket run) |
|---|---|---:|---:|---:|---:|---:|---:|
| GPT-6.1 Sol (max) | AI Coding Daily (excl. bug finding) | 55.0 | 90% | 49.8 | 49.0 | $950.68 | $88.25 |
| Claude Opus 5.5 (max) | AI Coding Daily (excl. bug finding) | 59.1 | 90% | 51.7 | 44.3 | $7,048.37 | $119.67 |
| Claude Sonnet 5.5 | AI Coding Daily (excl. bug finding) | 58.5 | 90% | 51.5 | 43.9 | $6,644.38 | $112.81 |
| GPT-6 Astra (max) | AI Coding Daily (excl. bug finding) | 56.4 | 90% | 45.5 | 43.1 | $4,767.90 | $329.16 |
| Claude Haiku 5.5 (low) | AI Coding Daily (excl. bug finding) | 22.1 | 90% | 41.6 | 38.5 | $36.79 | $0.62 |
| Claude Opus 5.5 (xhigh) | AI Coding Daily (excl. bug finding) | 56.8 | 90% | 52.1 | 43.9 | $4,214.23 | $71.55 |
| GPT-6 Astra (xhigh) | AI Coding Daily (excl. bug finding) | 55.7 | 90% | 46.6 | 44.3 | $3,186.48 | $219.99 |
| GPT-6 Luna (low) | AI Coding Daily (excl. bug finding) | 14.4 | 90% | 35.8 | 35.8 | $7.95 | $0.74 |
| GPT-6.1 Sol (xhigh) | AI Coding Daily (excl. bug finding) | 53.4 | 90% | 50.5 | 49.7 | $617.20 | $57.30 |
| GPT-6.1 Terra (low) | AI Coding Daily (excl. bug finding) | 32.3 | 90% | 42.0 | 41.6 | $104.95 | $9.74 |
| Gemini 4 Carbon | Bug Hunt Bench, AI Coding Daily (excl. bug finding) | 62.1 | 78% | 46.6 | 46.6 | $5,716.87 | $5,716.87 |
| MiMo-V2.6-Flash | Bug Hunt Bench | 42.0 | 88% | 40.9 | 49.9 | $82.84 | $72.16 |

### AI Coding Daily ranking: Plan routes and calibration

#### Measured-evidence calibration (diagnostic)

References: each workload's measured-only rows with complete cost evidence are the references: c_L = cheapest / 2, c_H = dearest x 2 (diagnostic only; the official anchors are unchanged). Status: evaluated.

- Workload `835a9baf594a1251`: measured anchors $10.35 to $391.32 from GPT-6 Astra (high), GPT-6.1 Sol (high), GPT-6.1 Sol (low), GPT-6.1 Sol (medium); anchor ratio 37.8 against the official 412.8. Official Plan anchors are set by GPT-6 Luna (medium) on ChatGPT Pro 500 (owner-named transfer) at the low end and GPT-6 Astra (high) on ChatGPT Plus (same-model measurement from another effort) at the high end.

| Configuration | Value on official Plan anchors | Value on measured anchors | Rank change |
|---|---:|---:|---:|
| Claude Opus 5.5 (high) ‡ | 54.23 | 57.91 | 0 |
| GPT-6 Astra (high) ‡ | 48.28 | 47.76 | 1 |
| GPT-6.1 Sol (high) ‡ | 52.88 | 56.24 | 1 |
| GPT-6.1 Sol (low) ‡ | 46.94 | 52.56 | -1 |
| GPT-6.1 Sol (medium) ‡ | 51.96 | 56.26 | -1 |

Pairwise reversals: GPT-6 Astra (high) and GPT-6.1 Sol (low); GPT-6.1 Sol (high) and GPT-6.1 Sol (medium). Largest value change: 5.62 points.

‡ measured on the same model at another effort (an O88 route; measured evidence under O90).

### AI Coding Daily ranking: interval outputs

**API basis, main workload: frontier.** Not evaluable: Claude Opus 5.5 (high). Competing without a label of its own (E183): Claude Haiku 5.5 (high): AA's cost omits a pricing term (O94); competes over its published cost up to the stated factor; Claude Haiku 5.5 (medium): AA's cost omits a pricing term (O94); competes over its published cost up to the stated factor.

| Configuration | Possible frontier | Definite frontier | Definite counterexample | Possible frontier blocked by |
|---|---|---|---|---|
| GPT-6.1 Terra (max) | certified | certified | — | — |
| GPT-6.1 Sol (high) | certified | certified | — | — |
| GPT-6.1 Sol (medium) | certified | certified | — | — |
| GPT-6 Astra (high) | certified | certified | — | — |
| GPT-6.1 Terra (xhigh) | certified | certified | — | — |
| GPT-6.1 Sol (low) | disproved | disproved | GPT-6.1 Terra (medium) | GPT-6.1 Terra (medium) |
| GPT-6.1 Terra (high) | certified | certified | — | — |
| GPT-6 Luna (max) | certified | certified | — | — |
| GPT-6.1 Terra (medium) | certified | certified | — | — |
| GPT-6 Luna (xhigh) | certified | certified | — | — |
| GPT-6 Luna (high) | certified | certified | — | — |
| GPT-6 Luna (medium) | certified | certified | — | — |

**API basis, main workload: cheapest at or above quality 43.5** (lower-median displayed quality of the non-provisional cohort configurations at freeze (E192; headline bar)). Status certified; confirmed cheapest: none.

Configurations that can be confirmed to qualify: 6 (confirmation needs the full-composite lower bound, with missing leaves at 0, to clear the bar; O25). Cheaper same-family configurations on AA's chart that were not evaluated (not ranked in this ranking: lacking its full benchmark set, or not plotted on or near the frontier; E201c, O51): GPT-6.1 Terra (high): GPT-6.1 Terra (non-reasoning), GPT-6.1 Terra (low); GPT-6.1 Terra (medium): GPT-6.1 Terra (low).

Bar comparison: compares 7 configurations that can qualify. The bar is a displayed-quality level; qualification tests each row's full-composite bounds, so a row above the bar on displayed quality can still fail to qualify confirmed when leaves are missing (E198).

| Configuration | Displayed quality − bar | Confirmed qualifies | Possibly qualifies | Possibly cheapest |
|---|---:|---|---|---|
| GPT-6.1 Terra (max) | 12.5 | certified | certified | disproved |
| GPT-6.1 Sol (high) | 12.1 | certified | certified | disproved |
| GPT-6.1 Sol (medium) | 8.9 | certified | certified | disproved |
| GPT-6 Astra (high) | 13.8 | certified | certified | disproved |
| GPT-6.1 Terra (xhigh) | 4.9 | certified | certified | disproved |
| GPT-6.1 Sol (low) | -0.4 | disproved | disproved | disproved |
| GPT-6.1 Terra (high) | 3.1 | certified | certified | certified |
| GPT-6 Luna (max) | -5.3 | disproved | disproved | disproved |
| GPT-6.1 Terra (medium) | 0.0 | disproved | certified | certified |
| GPT-6 Luna (xhigh) | -9.9 | disproved | disproved | disproved |
| GPT-6 Luna (high) | -11.7 | disproved | disproved | disproved |
| GPT-6 Luna (medium) | -16.4 | disproved | disproved | disproved |

**API basis, main workload: cheapest at or above quality 33.7** (lower-quartile displayed quality of the non-provisional cohort configurations at freeze (O34)). Status certified; confirmed cheapest: none.

Configurations that can be confirmed to qualify: 9 (confirmation needs the full-composite lower bound, with missing leaves at 0, to clear the bar; O25). Cheaper same-family configurations on AA's chart that were not evaluated (not ranked in this ranking: lacking its full benchmark set, or not plotted on or near the frontier; E201c, O51): GPT-6 Luna (max): GPT-6 Luna (low), GPT-6 Luna (non-reasoning); GPT-6 Luna (xhigh): GPT-6 Luna (low), GPT-6 Luna (non-reasoning).

Bar comparison: compares 10 configurations that can qualify. The bar is a displayed-quality level; qualification tests each row's full-composite bounds, so a row above the bar on displayed quality can still fail to qualify confirmed when leaves are missing (E198).

| Configuration | Displayed quality − bar | Confirmed qualifies | Possibly qualifies | Possibly cheapest |
|---|---:|---|---|---|
| GPT-6.1 Terra (max) | 22.4 | certified | certified | disproved |
| GPT-6.1 Sol (high) | 21.9 | certified | certified | disproved |
| GPT-6.1 Sol (medium) | 18.8 | certified | certified | disproved |
| GPT-6 Astra (high) | 23.7 | certified | certified | disproved |
| GPT-6.1 Terra (xhigh) | 14.8 | certified | certified | disproved |
| GPT-6.1 Sol (low) | 9.4 | certified | certified | disproved |
| GPT-6.1 Terra (high) | 13.0 | certified | certified | disproved |
| GPT-6 Luna (max) | 4.5 | certified | certified | certified |
| GPT-6.1 Terra (medium) | 9.9 | certified | certified | disproved |
| GPT-6 Luna (xhigh) | 0.0 | disproved | certified | certified |
| GPT-6 Luna (high) | -1.8 | disproved | disproved | disproved |
| GPT-6 Luna (medium) | -6.5 | disproved | disproved | disproved |

**API basis, main workload: cheapest at or above quality 52.5** (upper-quartile displayed quality of the non-provisional cohort configurations at freeze (O34)). Status certified; confirmed cheapest: none.

Configurations that can be confirmed to qualify: 3 (confirmation needs the full-composite lower bound, with missing leaves at 0, to clear the bar; O25). Cheaper same-family configurations on AA's chart that were not evaluated (not ranked in this ranking: lacking its full benchmark set, or not plotted on or near the frontier; E201c, O51): none.

Bar comparison: compares 4 configurations that can qualify. The bar is a displayed-quality level; qualification tests each row's full-composite bounds, so a row above the bar on displayed quality can still fail to qualify confirmed when leaves are missing (E198).

| Configuration | Displayed quality − bar | Confirmed qualifies | Possibly qualifies | Possibly cheapest |
|---|---:|---|---|---|
| GPT-6.1 Terra (max) | 3.6 | certified | certified | disproved |
| GPT-6.1 Sol (high) | 3.1 | certified | certified | certified |
| GPT-6.1 Sol (medium) | 0.0 | disproved | certified | certified |
| GPT-6 Astra (high) | 4.9 | certified | certified | disproved |
| GPT-6.1 Terra (xhigh) | -4.0 | disproved | disproved | disproved |
| GPT-6.1 Sol (low) | -9.4 | disproved | disproved | disproved |
| GPT-6.1 Terra (high) | -5.8 | disproved | disproved | disproved |
| GPT-6 Luna (max) | -14.3 | disproved | disproved | disproved |
| GPT-6.1 Terra (medium) | -8.9 | disproved | disproved | disproved |
| GPT-6 Luna (xhigh) | -18.8 | disproved | disproved | disproved |
| GPT-6 Luna (high) | -20.6 | disproved | disproved | disproved |
| GPT-6 Luna (medium) | -25.3 | disproved | disproved | disproved |

**Plan basis, main workload:** not evaluated (no row has FullCost and an identified M_W (E61/E67)).

### AI Coding Daily ranking: scenario shares

The scenario panel is the 15 rows scored on the main workload (E96, E266).

Frequencies over 10,000 scenarios per run (seed 20261031); streams are defined in [methodology.md](methodology.md#uncertainty-outputs). S1T adds benchmark sampling noise under an independent-task approximation (O39); the other streams exclude it, and every stream excludes correlated-task, harness and attempt effects (E155).

### API basis: rank 1

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M | S1T |
|---|---:|---:|---:|---:|---:|---:|
| Claude Haiku 5.5 (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Haiku 5.5 (medium) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Luna (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Luna (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Luna (medium) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Luna (xhigh) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (high) | 100.0% | 100.0% | 99.6% | 100.0% | 100.0% | 50.5% |
| GPT-6.1 Sol (low) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (medium) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 23.3% |
| GPT-6.1 Terra (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 1.6% |
| GPT-6.1 Terra (max) | 0.0% | 0.0% | 0.4% | 0.0% | 0.0% | 23.2% |
| GPT-6.1 Terra (medium) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.2% |
| GPT-6.1 Terra (xhigh) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 1.1% |

### API basis: rank 3 or better

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M | S1T |
|---|---:|---:|---:|---:|---:|---:|
| Claude Haiku 5.5 (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Haiku 5.5 (medium) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.1% |
| GPT-6 Astra (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.2% |
| GPT-6 Luna (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Luna (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.1% |
| GPT-6 Luna (medium) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Luna (xhigh) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (high) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 93.7% |
| GPT-6.1 Sol (low) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.4% |
| GPT-6.1 Sol (medium) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 83.5% |
| GPT-6.1 Terra (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 19.6% |
| GPT-6.1 Terra (max) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 79.6% |
| GPT-6.1 Terra (medium) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 6.2% |
| GPT-6.1 Terra (xhigh) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 16.7% |

### API basis: on the frontier

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M | S1T |
|---|---:|---:|---:|---:|---:|---:|
| Claude Haiku 5.5 (high) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 89.9% |
| Claude Haiku 5.5 (medium) | 100.0% | 100.0% | 82.7% | 100.0% | 100.0% | 61.2% |
| Claude Opus 5.5 (high) | 100.0% | 100.0% | 84.5% | 100.0% | 100.0% | 46.6% |
| GPT-6 Astra (high) | 100.0% | 100.0% | 93.2% | 100.0% | 100.0% | 41.9% |
| GPT-6 Luna (high) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 95.3% |
| GPT-6 Luna (max) | 100.0% | 100.0% | 87.7% | 100.0% | 100.0% | 62.0% |
| GPT-6 Luna (medium) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% |
| GPT-6 Luna (xhigh) | 100.0% | 100.0% | 93.2% | 100.0% | 100.0% | 57.2% |
| GPT-6.1 Sol (high) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 88.8% |
| GPT-6.1 Sol (low) | 0.0% | 0.0% | 33.0% | 0.0% | 0.0% | 43.3% |
| GPT-6.1 Sol (medium) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 90.7% |
| GPT-6.1 Terra (high) | 100.0% | 100.0% | 99.9% | 100.0% | 100.0% | 79.8% |
| GPT-6.1 Terra (max) | 100.0% | 100.0% | 82.6% | 100.0% | 100.0% | 57.0% |
| GPT-6.1 Terra (medium) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 96.5% |
| GPT-6.1 Terra (xhigh) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 69.8% |

### API basis: value-score dispersion (SD; covariance term)

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M | S1T |
|---|---:|---:|---:|---:|---:|---:|
| Claude Haiku 5.5 (high) | 0.00 (+0.00) | 0.00 (+0.00) | 1.70 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.39 (+0.00) |
| Claude Haiku 5.5 (medium) | 0.00 (+0.00) | 0.00 (+0.00) | 1.85 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.31 (+0.00) |
| Claude Opus 5.5 (high) | 0.00 (+0.00) | 0.00 (+0.00) | 1.57 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.30 (+0.00) |
| GPT-6 Astra (high) | 0.00 (+0.00) | 0.00 (+0.00) | 1.45 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.36 (+0.00) |
| GPT-6 Luna (high) | 0.00 (+0.00) | 0.00 (+0.00) | 1.88 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.39 (+0.00) |
| GPT-6 Luna (max) | 0.00 (+0.00) | 0.00 (+0.00) | 1.82 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.34 (+0.00) |
| GPT-6 Luna (medium) | 0.00 (+0.00) | 0.00 (+0.00) | 1.75 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.54 (+0.00) |
| GPT-6 Luna (xhigh) | 0.00 (+0.00) | 0.00 (+0.00) | 1.87 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.35 (+0.00) |
| GPT-6.1 Sol (high) | 0.00 (+0.00) | 0.00 (+0.00) | 1.47 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.32 (+0.00) |
| GPT-6.1 Sol (low) | 0.00 (+0.00) | 0.00 (+0.00) | 1.81 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.42 (+0.00) |
| GPT-6.1 Sol (medium) | 0.00 (+0.00) | 0.00 (+0.00) | 1.57 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.36 (+0.00) |
| GPT-6.1 Terra (high) | 0.00 (+0.00) | 0.00 (+0.00) | 1.52 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.63 (+0.00) |
| GPT-6.1 Terra (max) | 0.00 (+0.00) | 0.00 (+0.00) | 1.17 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.52 (+0.00) |
| GPT-6.1 Terra (medium) | 0.00 (+0.00) | 0.00 (+0.00) | 1.61 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.57 (+0.00) |
| GPT-6.1 Terra (xhigh) | 0.00 (+0.00) | 0.00 (+0.00) | 1.54 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.59 (+0.00) |

Plan streams S1, S2, S1 endpoint-heavy, S1M and S1T run with owner assumptions off (owner-named transfers and O46 provider quota ceilings; E167): Claude Haiku 5.5 (high) on Claude Max 20x, Claude Haiku 5.5 (high) on Claude Max 5x, Claude Haiku 5.5 (high) on Claude Pro, Claude Haiku 5.5 (medium) on Claude Max 20x, Claude Haiku 5.5 (medium) on Claude Max 5x, Claude Haiku 5.5 (medium) on Claude Pro, GPT-6 Luna (high) on ChatGPT Plus, GPT-6 Luna (high) on ChatGPT Pro 100, GPT-6 Luna (high) on ChatGPT Pro 200, GPT-6 Luna (high) on ChatGPT Pro 500, GPT-6 Luna (max) on ChatGPT Plus, GPT-6 Luna (max) on ChatGPT Pro 100, GPT-6 Luna (max) on ChatGPT Pro 200, GPT-6 Luna (max) on ChatGPT Pro 500, GPT-6 Luna (medium) on ChatGPT Plus, GPT-6 Luna (medium) on ChatGPT Pro 100, GPT-6 Luna (medium) on ChatGPT Pro 200, GPT-6 Luna (medium) on ChatGPT Pro 500, GPT-6 Luna (xhigh) on ChatGPT Plus, GPT-6 Luna (xhigh) on ChatGPT Pro 100, GPT-6 Luna (xhigh) on ChatGPT Pro 200, GPT-6 Luna (xhigh) on ChatGPT Pro 500, GPT-6.1 Terra (high) on ChatGPT Plus, GPT-6.1 Terra (high) on ChatGPT Pro 100, GPT-6.1 Terra (high) on ChatGPT Pro 200, GPT-6.1 Terra (high) on ChatGPT Pro 500, GPT-6.1 Terra (max) on ChatGPT Plus, GPT-6.1 Terra (max) on ChatGPT Pro 100, GPT-6.1 Terra (max) on ChatGPT Pro 200, GPT-6.1 Terra (max) on ChatGPT Pro 500, GPT-6.1 Terra (medium) on ChatGPT Plus, GPT-6.1 Terra (medium) on ChatGPT Pro 100, GPT-6.1 Terra (medium) on ChatGPT Pro 200, GPT-6.1 Terra (medium) on ChatGPT Pro 500, GPT-6.1 Terra (xhigh) on ChatGPT Plus, GPT-6.1 Terra (xhigh) on ChatGPT Pro 100, GPT-6.1 Terra (xhigh) on ChatGPT Pro 200, GPT-6.1 Terra (xhigh) on ChatGPT Pro 500 depend on an owner assumption and are unevaluable there (—), never reselected or replaced by API cost.

### Plan basis: rank 1

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M | S1T |
|---|---:|---:|---:|---:|---:|---:|
| Claude Haiku 5.5 (high) on Claude Max 20x | 0.0% | — | — | — | — | — |
| Claude Haiku 5.5 (high) on Claude Max 5x | 0.0% | — | — | — | — | — |
| Claude Haiku 5.5 (high) on Claude Pro | 0.0% | — | — | — | — | — |
| Claude Haiku 5.5 (medium) on Claude Max 20x | 0.0% | — | — | — | — | — |
| Claude Haiku 5.5 (medium) on Claude Max 5x | 0.0% | — | — | — | — | — |
| Claude Haiku 5.5 (medium) on Claude Pro | 0.0% | — | — | — | — | — |
| Claude Opus 5.5 (high) on Claude Max 20x | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (high) on Claude Max 5x | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (high) on Claude Pro | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 72.0% |
| GPT-6 Astra (high) on ChatGPT Plus | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (high) on ChatGPT Pro 100 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (high) on ChatGPT Pro 200 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (high) on ChatGPT Pro 500 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Luna (high) on ChatGPT Plus | 0.0% | — | — | — | — | — |
| GPT-6 Luna (high) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — |
| GPT-6 Luna (high) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — |
| GPT-6 Luna (high) on ChatGPT Pro 500 | 0.0% | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Plus | 0.0% | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 500 | 0.0% | — | — | — | — | — |
| GPT-6 Luna (medium) on ChatGPT Plus | 0.0% | — | — | — | — | — |
| GPT-6 Luna (medium) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — |
| GPT-6 Luna (medium) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — |
| GPT-6 Luna (medium) on ChatGPT Pro 500 | 0.0% | — | — | — | — | — |
| GPT-6 Luna (xhigh) on ChatGPT Plus | 0.0% | — | — | — | — | — |
| GPT-6 Luna (xhigh) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — |
| GPT-6 Luna (xhigh) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — |
| GPT-6 Luna (xhigh) on ChatGPT Pro 500 | 0.0% | — | — | — | — | — |
| GPT-6.1 Sol (high) on ChatGPT Plus | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (high) on ChatGPT Pro 100 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (high) on ChatGPT Pro 200 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (high) on ChatGPT Pro 500 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 20.6% |
| GPT-6.1 Sol (low) on ChatGPT Plus | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (low) on ChatGPT Pro 100 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (low) on ChatGPT Pro 200 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (low) on ChatGPT Pro 500 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (medium) on ChatGPT Plus | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (medium) on ChatGPT Pro 100 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (medium) on ChatGPT Pro 200 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (medium) on ChatGPT Pro 500 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 7.3% |
| GPT-6.1 Terra (high) on ChatGPT Plus | 0.0% | — | — | — | — | — |
| GPT-6.1 Terra (high) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — |
| GPT-6.1 Terra (high) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — |
| GPT-6.1 Terra (high) on ChatGPT Pro 500 | 0.0% | — | — | — | — | — |
| GPT-6.1 Terra (max) on ChatGPT Plus | 0.0% | — | — | — | — | — |
| GPT-6.1 Terra (max) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — |
| GPT-6.1 Terra (max) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — |
| GPT-6.1 Terra (max) on ChatGPT Pro 500 | 0.0% | — | — | — | — | — |
| GPT-6.1 Terra (medium) on ChatGPT Plus | 0.0% | — | — | — | — | — |
| GPT-6.1 Terra (medium) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — |
| GPT-6.1 Terra (medium) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — |
| GPT-6.1 Terra (medium) on ChatGPT Pro 500 | 0.0% | — | — | — | — | — |
| GPT-6.1 Terra (xhigh) on ChatGPT Plus | 0.0% | — | — | — | — | — |
| GPT-6.1 Terra (xhigh) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — |
| GPT-6.1 Terra (xhigh) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — |
| GPT-6.1 Terra (xhigh) on ChatGPT Pro 500 | 0.0% | — | — | — | — | — |

### Plan basis: rank 3 or better

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M | S1T |
|---|---:|---:|---:|---:|---:|---:|
| Claude Haiku 5.5 (high) on Claude Max 20x | 0.0% | — | — | — | — | — |
| Claude Haiku 5.5 (high) on Claude Max 5x | 0.0% | — | — | — | — | — |
| Claude Haiku 5.5 (high) on Claude Pro | 0.0% | — | — | — | — | — |
| Claude Haiku 5.5 (medium) on Claude Max 20x | 0.0% | — | — | — | — | — |
| Claude Haiku 5.5 (medium) on Claude Max 5x | 0.0% | — | — | — | — | — |
| Claude Haiku 5.5 (medium) on Claude Pro | 0.0% | — | — | — | — | — |
| Claude Opus 5.5 (high) on Claude Max 20x | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 73.4% |
| Claude Opus 5.5 (high) on Claude Max 5x | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 69.7% |
| Claude Opus 5.5 (high) on Claude Pro | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 73.7% |
| GPT-6 Astra (high) on ChatGPT Plus | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (high) on ChatGPT Pro 100 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (high) on ChatGPT Pro 200 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (high) on ChatGPT Pro 500 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Luna (high) on ChatGPT Plus | 0.0% | — | — | — | — | — |
| GPT-6 Luna (high) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — |
| GPT-6 Luna (high) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — |
| GPT-6 Luna (high) on ChatGPT Pro 500 | 0.0% | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Plus | 0.0% | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 500 | 0.0% | — | — | — | — | — |
| GPT-6 Luna (medium) on ChatGPT Plus | 0.0% | — | — | — | — | — |
| GPT-6 Luna (medium) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — |
| GPT-6 Luna (medium) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — |
| GPT-6 Luna (medium) on ChatGPT Pro 500 | 0.0% | — | — | — | — | — |
| GPT-6 Luna (xhigh) on ChatGPT Plus | 0.0% | — | — | — | — | — |
| GPT-6 Luna (xhigh) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — |
| GPT-6 Luna (xhigh) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — |
| GPT-6 Luna (xhigh) on ChatGPT Pro 500 | 0.0% | — | — | — | — | — |
| GPT-6.1 Sol (high) on ChatGPT Plus | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 19.6% |
| GPT-6.1 Sol (high) on ChatGPT Pro 100 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 19.6% |
| GPT-6.1 Sol (high) on ChatGPT Pro 200 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (high) on ChatGPT Pro 500 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 22.3% |
| GPT-6.1 Sol (low) on ChatGPT Plus | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (low) on ChatGPT Pro 100 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (low) on ChatGPT Pro 200 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (low) on ChatGPT Pro 500 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (medium) on ChatGPT Plus | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 7.0% |
| GPT-6.1 Sol (medium) on ChatGPT Pro 100 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 7.0% |
| GPT-6.1 Sol (medium) on ChatGPT Pro 200 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (medium) on ChatGPT Pro 500 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 8.5% |
| GPT-6.1 Terra (high) on ChatGPT Plus | 0.0% | — | — | — | — | — |
| GPT-6.1 Terra (high) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — |
| GPT-6.1 Terra (high) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — |
| GPT-6.1 Terra (high) on ChatGPT Pro 500 | 0.0% | — | — | — | — | — |
| GPT-6.1 Terra (max) on ChatGPT Plus | 0.0% | — | — | — | — | — |
| GPT-6.1 Terra (max) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — |
| GPT-6.1 Terra (max) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — |
| GPT-6.1 Terra (max) on ChatGPT Pro 500 | 0.0% | — | — | — | — | — |
| GPT-6.1 Terra (medium) on ChatGPT Plus | 0.0% | — | — | — | — | — |
| GPT-6.1 Terra (medium) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — |
| GPT-6.1 Terra (medium) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — |
| GPT-6.1 Terra (medium) on ChatGPT Pro 500 | 0.0% | — | — | — | — | — |
| GPT-6.1 Terra (xhigh) on ChatGPT Plus | 0.0% | — | — | — | — | — |
| GPT-6.1 Terra (xhigh) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — |
| GPT-6.1 Terra (xhigh) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — |
| GPT-6.1 Terra (xhigh) on ChatGPT Pro 500 | 0.0% | — | — | — | — | — |

### Plan basis: on the frontier

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M | S1T |
|---|---:|---:|---:|---:|---:|---:|
| Claude Haiku 5.5 (high) on Claude Max 20x | 0.0% | — | — | — | — | — |
| Claude Haiku 5.5 (high) on Claude Max 5x | 0.0% | — | — | — | — | — |
| Claude Haiku 5.5 (high) on Claude Pro | 100.0% | — | — | — | — | — |
| Claude Haiku 5.5 (medium) on Claude Max 20x | 0.0% | — | — | — | — | — |
| Claude Haiku 5.5 (medium) on Claude Max 5x | 0.0% | — | — | — | — | — |
| Claude Haiku 5.5 (medium) on Claude Pro | 100.0% | — | — | — | — | — |
| Claude Opus 5.5 (high) on Claude Max 20x | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (high) on Claude Max 5x | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (high) on Claude Pro | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 95.5% |
| GPT-6 Astra (high) on ChatGPT Plus | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (high) on ChatGPT Pro 100 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (high) on ChatGPT Pro 200 | 100.0% | 100.0% | 94.2% | 100.0% | 100.0% | 52.7% |
| GPT-6 Astra (high) on ChatGPT Pro 500 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Luna (high) on ChatGPT Plus | 0.0% | — | — | — | — | — |
| GPT-6 Luna (high) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — |
| GPT-6 Luna (high) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — |
| GPT-6 Luna (high) on ChatGPT Pro 500 | 0.0% | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Plus | 0.0% | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 500 | 100.0% | — | — | — | — | — |
| GPT-6 Luna (medium) on ChatGPT Plus | 0.0% | — | — | — | — | — |
| GPT-6 Luna (medium) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — |
| GPT-6 Luna (medium) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — |
| GPT-6 Luna (medium) on ChatGPT Pro 500 | 0.0% | — | — | — | — | — |
| GPT-6 Luna (xhigh) on ChatGPT Plus | 0.0% | — | — | — | — | — |
| GPT-6 Luna (xhigh) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — |
| GPT-6 Luna (xhigh) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — |
| GPT-6 Luna (xhigh) on ChatGPT Pro 500 | 0.0% | — | — | — | — | — |
| GPT-6.1 Sol (high) on ChatGPT Plus | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (high) on ChatGPT Pro 100 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (high) on ChatGPT Pro 200 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (high) on ChatGPT Pro 500 | 0.0% | 0.0% | 0.1% | 0.0% | 0.0% | 31.1% |
| GPT-6.1 Sol (low) on ChatGPT Plus | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (low) on ChatGPT Pro 100 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (low) on ChatGPT Pro 200 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (low) on ChatGPT Pro 500 | 0.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% |
| GPT-6.1 Sol (medium) on ChatGPT Plus | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (medium) on ChatGPT Pro 100 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (medium) on ChatGPT Pro 200 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (medium) on ChatGPT Pro 500 | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% |
| GPT-6.1 Terra (high) on ChatGPT Plus | 0.0% | — | — | — | — | — |
| GPT-6.1 Terra (high) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — |
| GPT-6.1 Terra (high) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — |
| GPT-6.1 Terra (high) on ChatGPT Pro 500 | 100.0% | — | — | — | — | — |
| GPT-6.1 Terra (max) on ChatGPT Plus | 0.0% | — | — | — | — | — |
| GPT-6.1 Terra (max) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — |
| GPT-6.1 Terra (max) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — |
| GPT-6.1 Terra (max) on ChatGPT Pro 500 | 0.0% | — | — | — | — | — |
| GPT-6.1 Terra (medium) on ChatGPT Plus | 0.0% | — | — | — | — | — |
| GPT-6.1 Terra (medium) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — |
| GPT-6.1 Terra (medium) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — |
| GPT-6.1 Terra (medium) on ChatGPT Pro 500 | 100.0% | — | — | — | — | — |
| GPT-6.1 Terra (xhigh) on ChatGPT Plus | 0.0% | — | — | — | — | — |
| GPT-6.1 Terra (xhigh) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — |
| GPT-6.1 Terra (xhigh) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — |
| GPT-6.1 Terra (xhigh) on ChatGPT Pro 500 | 100.0% | — | — | — | — | — |

### Plan basis: value-score dispersion (SD; covariance term)

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M | S1T |
|---|---:|---:|---:|---:|---:|---:|
| Claude Haiku 5.5 (high) on Claude Max 20x | 0.00 (+0.00) | — | — | — | — | — |
| Claude Haiku 5.5 (high) on Claude Max 5x | 0.00 (+0.00) | — | — | — | — | — |
| Claude Haiku 5.5 (high) on Claude Pro | 0.00 (+0.00) | — | — | — | — | — |
| Claude Haiku 5.5 (medium) on Claude Max 20x | 0.00 (+0.00) | — | — | — | — | — |
| Claude Haiku 5.5 (medium) on Claude Max 5x | 0.00 (+0.00) | — | — | — | — | — |
| Claude Haiku 5.5 (medium) on Claude Pro | 0.00 (+0.00) | — | — | — | — | — |
| Claude Opus 5.5 (high) on Claude Max 20x | 0.00 (+0.00) | 0.00 (+0.00) | 1.57 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.30 (+0.00) |
| Claude Opus 5.5 (high) on Claude Max 5x | 0.00 (+0.00) | 0.00 (+0.00) | 1.57 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.30 (+0.00) |
| Claude Opus 5.5 (high) on Claude Pro | 0.00 (+0.00) | 0.00 (+0.00) | 1.57 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.30 (+0.00) |
| GPT-6 Astra (high) on ChatGPT Plus | 0.00 (+0.00) | 0.00 (+0.00) | 1.45 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.35 (+0.00) |
| GPT-6 Astra (high) on ChatGPT Pro 100 | 0.00 (+0.00) | 0.00 (+0.00) | 1.45 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.35 (+0.00) |
| GPT-6 Astra (high) on ChatGPT Pro 200 | 0.00 (+0.00) | 0.00 (+0.00) | 1.45 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.35 (+0.00) |
| GPT-6 Astra (high) on ChatGPT Pro 500 | 0.00 (+0.00) | 0.00 (+0.00) | 1.45 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.35 (+0.00) |
| GPT-6 Luna (high) on ChatGPT Plus | 0.00 (+0.00) | — | — | — | — | — |
| GPT-6 Luna (high) on ChatGPT Pro 100 | 0.00 (+0.00) | — | — | — | — | — |
| GPT-6 Luna (high) on ChatGPT Pro 200 | 0.00 (+0.00) | — | — | — | — | — |
| GPT-6 Luna (high) on ChatGPT Pro 500 | 0.00 (+0.00) | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Plus | 0.00 (+0.00) | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 100 | 0.00 (+0.00) | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 200 | 0.00 (+0.00) | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 500 | 0.00 (+0.00) | — | — | — | — | — |
| GPT-6 Luna (medium) on ChatGPT Plus | 0.00 (+0.00) | — | — | — | — | — |
| GPT-6 Luna (medium) on ChatGPT Pro 100 | 0.00 (+0.00) | — | — | — | — | — |
| GPT-6 Luna (medium) on ChatGPT Pro 200 | 0.00 (+0.00) | — | — | — | — | — |
| GPT-6 Luna (medium) on ChatGPT Pro 500 | 0.00 (+0.00) | — | — | — | — | — |
| GPT-6 Luna (xhigh) on ChatGPT Plus | 0.00 (+0.00) | — | — | — | — | — |
| GPT-6 Luna (xhigh) on ChatGPT Pro 100 | 0.00 (+0.00) | — | — | — | — | — |
| GPT-6 Luna (xhigh) on ChatGPT Pro 200 | 0.00 (+0.00) | — | — | — | — | — |
| GPT-6 Luna (xhigh) on ChatGPT Pro 500 | 0.00 (+0.00) | — | — | — | — | — |
| GPT-6.1 Sol (high) on ChatGPT Plus | 0.00 (+0.00) | 0.00 (+0.00) | 1.48 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.33 (+0.00) |
| GPT-6.1 Sol (high) on ChatGPT Pro 100 | 0.00 (+0.00) | 0.00 (+0.00) | 1.48 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.33 (+0.00) |
| GPT-6.1 Sol (high) on ChatGPT Pro 200 | 0.00 (+0.00) | 0.00 (+0.00) | 1.48 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.33 (+0.00) |
| GPT-6.1 Sol (high) on ChatGPT Pro 500 | 0.00 (+0.00) | 0.00 (+0.00) | 1.48 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.33 (+0.00) |
| GPT-6.1 Sol (low) on ChatGPT Plus | 0.00 (+0.00) | 0.00 (+0.00) | 1.82 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.41 (+0.00) |
| GPT-6.1 Sol (low) on ChatGPT Pro 100 | 0.00 (+0.00) | 0.00 (+0.00) | 1.82 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.41 (+0.00) |
| GPT-6.1 Sol (low) on ChatGPT Pro 200 | 0.00 (+0.00) | 0.00 (+0.00) | 1.82 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.41 (+0.00) |
| GPT-6.1 Sol (low) on ChatGPT Pro 500 | 0.00 (+0.00) | 0.00 (+0.00) | 1.82 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.41 (+0.00) |
| GPT-6.1 Sol (medium) on ChatGPT Plus | 0.00 (+0.00) | 0.00 (+0.00) | 1.58 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.36 (+0.00) |
| GPT-6.1 Sol (medium) on ChatGPT Pro 100 | 0.00 (+0.00) | 0.00 (+0.00) | 1.58 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.36 (+0.00) |
| GPT-6.1 Sol (medium) on ChatGPT Pro 200 | 0.00 (+0.00) | 0.00 (+0.00) | 1.58 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.36 (+0.00) |
| GPT-6.1 Sol (medium) on ChatGPT Pro 500 | 0.00 (+0.00) | 0.00 (+0.00) | 1.58 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.36 (+0.00) |
| GPT-6.1 Terra (high) on ChatGPT Plus | 0.00 (+0.00) | — | — | — | — | — |
| GPT-6.1 Terra (high) on ChatGPT Pro 100 | 0.00 (+0.00) | — | — | — | — | — |
| GPT-6.1 Terra (high) on ChatGPT Pro 200 | 0.00 (+0.00) | — | — | — | — | — |
| GPT-6.1 Terra (high) on ChatGPT Pro 500 | 0.00 (+0.00) | — | — | — | — | — |
| GPT-6.1 Terra (max) on ChatGPT Plus | 0.00 (+0.00) | — | — | — | — | — |
| GPT-6.1 Terra (max) on ChatGPT Pro 100 | 0.00 (+0.00) | — | — | — | — | — |
| GPT-6.1 Terra (max) on ChatGPT Pro 200 | 0.00 (+0.00) | — | — | — | — | — |
| GPT-6.1 Terra (max) on ChatGPT Pro 500 | 0.00 (+0.00) | — | — | — | — | — |
| GPT-6.1 Terra (medium) on ChatGPT Plus | 0.00 (+0.00) | — | — | — | — | — |
| GPT-6.1 Terra (medium) on ChatGPT Pro 100 | 0.00 (+0.00) | — | — | — | — | — |
| GPT-6.1 Terra (medium) on ChatGPT Pro 200 | 0.00 (+0.00) | — | — | — | — | — |
| GPT-6.1 Terra (medium) on ChatGPT Pro 500 | 0.00 (+0.00) | — | — | — | — | — |
| GPT-6.1 Terra (xhigh) on ChatGPT Plus | 0.00 (+0.00) | — | — | — | — | — |
| GPT-6.1 Terra (xhigh) on ChatGPT Pro 100 | 0.00 (+0.00) | — | — | — | — | — |
| GPT-6.1 Terra (xhigh) on ChatGPT Pro 200 | 0.00 (+0.00) | — | — | — | — | — |
| GPT-6.1 Terra (xhigh) on ChatGPT Pro 500 | 0.00 (+0.00) | — | — | — | — | — |

### Named S2 specification branches

- **Bug Hunt harness band (E19)** (S2): unevaluable; the captured tbench.ai leaderboard lists no configuration under two or more agents, so no cross-agent spread exists
- **cache-hit variation (E34)** (S2): unevaluable; AA's published cost embeds its cache-pricing protocol; varying the cache-hit rate needs each basket component's cache-read and uncached-input demand, which AA publishes only for the whole Index (E157)
- **first-party list versus cross-provider median price rule (E122)** (S2): unevaluable; AA publishes one price per configuration under its own rule; the alternative rule's prices are not captured

### Cheapest-above-the-bar labels (API basis)

The 90% rule's error bound holds per published event (candidate and kernel assignment); it is not corrected across the listed candidates (E198). Each kernel assignment code gives the kernel used for the candidate and the competitors, in that order (U uniform, H endpoint-heavy; a quality-level bar has no reference rows, so it takes no letter); the label needs every assignment met.

| Bar | Candidate | Reading | Frequency range | Kernel assignments | Label |
|---|---|---|---|---|---|
| quality 43.5 | GPT-6.1 Terra (high) | not scenario-supported | 49.9% to 50.7% | UU not met, UH not met, HU not met, HH not met | no |
| quality 43.5 | GPT-6.1 Terra (medium) | not scenario-supported | 49.3% to 50.6% | UU not met, UH not met, HU not met, HH not met | no |
| quality 33.7 | GPT-6 Luna (max) | not scenario-supported | 0.0% to 0.0% | UU not met, UH not met, HU not met, HH not met | no |
| quality 33.7 | GPT-6 Luna (xhigh) | not scenario-supported | 49.8% to 50.6% | UU not met, UH not met, HU not met, HH not met | no |
| quality 52.5 | GPT-6.1 Sol (high) | not scenario-supported | 49.1% to 50.5% | UU not met, UH not met, HU not met, HH not met | no |
| quality 52.5 | GPT-6.1 Sol (medium) | not scenario-supported | 49.5% to 50.6% | UU not met, UH not met, HU not met, HH not met | no |

### AI Coding Daily ranking: diagnostics

- **Terminal-Bench cross-source agreement (AA's mini-SWE-agent run against tbench.ai):** undefined (panel too small); 0 rows take the leaf from tbench.ai (gap fill).
- **Rank separability (O39, independent-task approximation):** median separation 4.20 value points (API) and 4.39 (Plan); separable adjacent ranks: API 0 of 14, Plan 0 of 33. Assumptions: tasks are independent and each leaf's score is a mean over its published task count (plug-in binomial with the proportion (k + 1/2) / (n + 1), I28); attempts averaged within a task and tasks shared across models are ignored, so the noise is approximate; GDPval-AA: each row's rating interval as AA's model page displays it, read as a 95% normal interval (AA states no level), SD = half-width / 1.96; AA-Omniscience: each of 6,000 questions scores +1, 0 or -1, with the shares from AA's accuracy and hallucination rate; Vals boards (Vibe Code Bench v1.1, Code Migration v1.1): Vals' published standard error per record, read as the leaf's SD; AI Coding Daily: judged points over its six graded projects read as a binomial share of 60 points (an assumption; the board publishes no error).
- **FrontierCode against Cognition:** FrontierCode cross-source agreement (AA against Cognition; E234): retired (O136): the leaf is AA's FrontierCode 2.0 and Cognition's board publishes FrontierCode 1.1, so no fill or comparison is made across the two versions; panel of 0 rows.
- **Gap-fill removal (E234, diagnostic):** no ranked row has a leaf from another party or the provider.
- **Bar results without the gap fills (E234, sensitivity; labels unchanged):** cheapest displayed row as published, with fills removed, and with third-party fills no measured offset — API quality 43.5: GPT-6.1 Terra (medium) in all three; API quality 33.7: GPT-6 Luna (xhigh) in all three; API quality 52.5: GPT-6.1 Sol (medium) in all three; Plan quality 43.5: GPT-6.1 Terra (medium) in all three; Plan quality 33.7: Claude Haiku 5.5 (high) in all three; Plan quality 52.5: GPT-6.1 Sol (medium) in all three.
- **Harness cost (O123, S2 stress):** unevaluable: no model is listed under two or more agents in AA's Coding Agent Index capture, so no agent effect is identified (O123). Coding Agent Index agents (each part of its costed configuration; none is the run behind the FrontierCode or Terminal-Bench leaf): GPT-6.1 Terra (max): Codex; GPT-6.1 Terra (xhigh): Codex; GPT-6.1 Terra (high): Codex; GPT-6 Luna (max): Codex; GPT-6.1 Terra (medium): Codex.
- **Quality agreement:** quality agreement (matched-panel sensitivity): Kendall tau 0.60 (interval 0.26 to 0.88) on 15 rows.
- **Quality-substitution value agreement (API):** quality-substitution value agreement, api basis (matched-panel sensitivity): Kendall tau 0.10 (interval -0.47 to 0.64) on 15 rows.
- **Quality-substitution value agreement (Plan):** quality-substitution value agreement, plan basis (matched-panel sensitivity): Kendall tau 0.37 (interval -0.01 to 0.66) on 15 rows.
- **Disjoint-evidence agreement:** disjoint-evidence agreement (restricted evidence comparison, not an eligible ranking): Kendall tau 0.58 (interval 0.22 to 0.87) on 15 rows.
- **Quality source shares:** AA-run 78%, independent 22%.
- **Non-discriminating leaves:** lcr.
- **Group drift:** estimated; flagged: none.
- **Omniscience abstention sensitivity** (z_pen = max(0, I)): no rank changes.
- **GDPval-AA logistic sensitivity** (z = 100 / (1 + 10^((1600 - E) / 400)) against AA's pinned anchor; every other input fixed): API 6 rows move; largest move 2 (Claude Opus 5.5 (high), GPT-6.1 Sol (low)); Plan 2 rows move; largest move 2 (Claude Haiku 5.5 (medium), GPT-6.1 Terra (xhigh)).
- **Anchor stability:** trimmed anchors (P10 / 2 and P90 x 2 (diagnostic only)) give $29.40 to $1,340.81; 10 rows move; largest move 7 (Claude Opus 5.5 (high)).

- **Basket readiness (E22):** priced leaves cover 50% of nominal quality weight (AutomationBench-AA, FrontierCode 2.0, Terminal-Bench-Science 0.1, Terminal-Bench 4.0 (AA run)); pending components: Coding Agent Index, ITBench-AA.
- **SWE cost companion (O14, diagnostic):** 5 rows evaluated; flagged far from the median ratio: none.
- **Matched-cost diagnostic (E55):** evaluated at 63% priced quality weight; basket/matched cost-order reversals with separated intervals: 1; rank-gap warnings: 0.
- **Frontier-families anchors (E187, diagnostic):** anchors rebuilt from the 14 frontier and near-frontier references move API no rank changes (value points per cost doubling 3.02 vs 3.02 frozen); Plan 5 rows move; largest move 2 (Claude Haiku 5.5 (high)) (value points per cost doubling 2.65 vs 2.88 frozen).
- **Frontier-families bar (E199, sensitivity; the frozen bar stays primary):** quality 43.5 over 15 configurations; cheapest at or above it on the API main workload: not unique; possibly GPT-6.1 Terra (high), GPT-6.1 Terra (medium) (compares 7 configurations that can qualify).
- **One row per family (E205, diagnostic; the frozen ladder and anchors stay primary):** with each family's primary configuration only (3 rows in the one-row-per-family bar population), the ladder (headline, lower quartile, upper quartile) would be 37.4 against 43.5 / 33.7 / 52.5 frozen; anchors rebuilt from its 3 references move API 15 rows move; largest move 14 (GPT-6 Luna (medium)) (value points per cost doubling 6.16 vs 3.02 frozen); Plan 14 rows move; largest move 6 (GPT-6 Astra (high)) (value points per cost doubling 4.47 vs 2.88 frozen).
- **Ladder over scored rows (I28, sensitivity; the frozen ladder stays primary):** the bar population keeps full-benchmark rows that have no cost; today every such row has a cost, so the ladder is unchanged.
- **Bar currency (E207, informational):** rows reaching each frozen bar: quality 43.5: 8 of 15; quality 33.7: 12 of 15; quality 52.5: 5 of 15; the current population would freeze 43.5 / 33.7 / 52.5; lifetime until the next anchor re-freeze or methodology version, whichever comes first; no staleness flag.
- **Token mix (E208):** 15 selected routes: mix unidentified: the basket's token-category shares are set-identified only (E124), so the L1 test (above 0.30 flags mix-unmatched) is not computed.
- **Observed-range sensitivity (E219, not evidence; no label changes):** with each missing leaf inside the cohort's observed range for that leaf, quality 43.5: 7 can qualify, 6 confirmed; possibly cheapest GPT-6.1 Terra (high), GPT-6.1 Terra (medium); quality 33.7: 10 can qualify, 9 confirmed; possibly cheapest GPT-6 Luna (max), GPT-6 Luna (xhigh); quality 52.5: 4 can qualify, 3 confirmed; possibly cheapest GPT-6.1 Sol (high), GPT-6.1 Sol (medium).
- **What would settle the headline bar (E221, not a claim):** rows that can but need not reach quality 43.5, with the mean score their missing leaves would need: GPT-6.1 Terra (medium) (no missing leaf; reporting precision only).
- **Common leaf set (E226, diagnostic; scores unchanged):** without the leaves fewer than 90% of cohort rows have (none), API no rank changes; Plan no rank changes; rows reaching each bar: quality 43.5: 8 → 8; quality 33.7: 12 → 12; quality 52.5: 5 → 5; rows whose displayed quality differs from common-leaf quality by more than one cost doubling's worth: none.
- **Harness by leaf (E227):** Terminal-Bench: mini-SWE-agent 15; Bug Hunt: Codex CLI 12, Claude Code 3; AI Coding Daily: Codex CLI 12, Claude Code 3.
- **Coding Agent Index safety refusals (O63, flagged; costs and scores unchanged):** none.

### Leave-one-component-out cost family (E172)

Each admitted basket unit removed in turn, scored on anchors rebuilt by the freeze rule (rank changes against the primary ranking; quality held fixed).

| Removed component | API rank changes | Plan rank changes | API value points per cost doubling |
|---|---|---|---:|
| AA-Briefcase | 5 rows move; largest move 2 (Claude Haiku 5.5 (medium)) | 4 rows move; largest move 1 (Claude Haiku 5.5 (high), GPT-6.1 Terra (max), GPT-6.1 Terra (high), GPT-6.1 Terra (xhigh)) | 3.06 |
| GDP.pdf | no rank changes | 2 rows move; largest move 2 (Claude Haiku 5.5 (high), GPT-6.1 Sol (medium)) | 3.03 |
| AutomationBench-AA | 4 rows move; largest move 1 (Claude Opus 5.5 (high), GPT-6 Astra (high), GPT-6 Luna (high), GPT-6 Luna (xhigh)) | 2 rows move; largest move 2 (Claude Haiku 5.5 (high), GPT-6.1 Sol (medium)) | 3.01 |
| Terminal-Bench 4.0 (AA Index run) | 4 rows move; largest move 1 (Claude Haiku 5.5 (medium), GPT-6 Luna (high), GPT-6.1 Sol (medium), GPT-6.1 Terra (max)) | 4 rows move; largest move 1 (Claude Haiku 5.5 (high), GPT-6.1 Terra (max), GPT-6.1 Terra (high), GPT-6.1 Terra (xhigh)) | 3.00 |
| FrontierCode 2.0 | 4 rows move; largest move 1 (Claude Opus 5.5 (high), GPT-6 Astra (high), GPT-6.1 Sol (medium), GPT-6.1 Terra (max)) | 5 rows move; largest move 2 (Claude Haiku 5.5 (high)) | 3.01 |
| Terminal-Bench-Science | 8 rows move; largest move 3 (GPT-6.1 Sol (low)) | 4 rows move; largest move 1 (Claude Haiku 5.5 (high), GPT-6.1 Terra (max), GPT-6.1 Terra (high), GPT-6.1 Terra (xhigh)) | 2.99 |

### Subset rows: paired bridge and missing spend (E10, E173)

No row is scored on a subset workload.

### Deletion sensitivity

| Branch | Retained nominal weight | Status | API rank changes | Plan rank changes |
|---|---:|---|---|---|
| leave-out:frontierCode | 79% | evaluated | 7 rows move; largest move 3 (GPT-6.1 Sol (low)) | 7 rows move; largest move 3 (GPT-6.1 Terra (high)) |
| leave-out:terminalBench | 83% | evaluated | 9 rows move; largest move 6 (Claude Opus 5.5 (high), GPT-6 Luna (max)) | 12 rows move; largest move 4 (GPT-6 Luna (max)) |
| leave-out:bugHunt | 88% | evaluated | 4 rows move; largest move 1 (Claude Opus 5.5 (high), GPT-6 Luna (high), GPT-6 Luna (xhigh), GPT-6.1 Sol (low)) | 9 rows move; largest move 3 (Claude Haiku 5.5 (medium)) |
| leave-out:aiCodingDaily | 90% | evaluated | 6 rows move; largest move 2 (GPT-6 Astra (high), GPT-6.1 Sol (low)) | 8 rows move; largest move 4 (Claude Haiku 5.5 (medium)) |
| leave-out:gdpval | 90% | evaluated | 7 rows move; largest move 2 (Claude Haiku 5.5 (medium)) | 6 rows move; largest move 2 (Claude Haiku 5.5 (high), Claude Haiku 5.5 (medium)) |
| leave-out:automationBench | 90% | evaluated | 8 rows move; largest move 2 (Claude Haiku 5.5 (high), Claude Haiku 5.5 (medium)) | 2 rows move; largest move 1 (Claude Haiku 5.5 (high), GPT-6.1 Sol (high)) |
| leave-out:omniscience | 90% | evaluated | 4 rows move; largest move 3 (GPT-6 Luna (max), GPT-6.1 Sol (low)) | 4 rows move; largest move 2 (Claude Haiku 5.5 (medium), GPT-6.1 Terra (xhigh)) |
| leave-out:lcr | 95% | evaluated | 5 rows move; largest move 2 (GPT-6.1 Sol (low)) | 2 rows move; largest move 2 (Claude Haiku 5.5 (medium), GPT-6.1 Terra (xhigh)) |
| leave-out:hle | 98% | evaluated | no rank changes | 2 rows move; largest move 1 (GPT-6 Astra (high), GPT-6.1 Terra (medium)) |
| leave-out:tbScience | 98% | evaluated | 2 rows move; largest move 1 (GPT-6 Astra (high), GPT-6 Luna (max)) | 6 rows move; largest move 1 (Claude Haiku 5.5 (high), GPT-6 Astra (high), GPT-6.1 Sol (high), GPT-6.1 Sol (medium), GPT-6.1 Terra (max), GPT-6.1 Terra (medium)) |
| leave-out:critpt | 98% | evaluated | no rank changes | 2 rows move; largest move 1 (GPT-6 Astra (high), GPT-6.1 Terra (medium)) |
| leave-source-out:Artificial Analysis | 22% | not identifiable under the coverage rule | — | — |
| basket-scope | 87% | evaluated | 5 rows move; largest move 4 (GPT-6.1 Sol (low)) | 6 rows move; largest move 1 (Claude Haiku 5.5 (high), GPT-6 Luna (max), GPT-6.1 Sol (high), GPT-6.1 Sol (low), GPT-6.1 Terra (high), GPT-6.1 Terra (xhigh)) |

### Cost-component removal (Terminal-Bench 4.0 (AA Index run): evaluated)

| Basis | Run | Rank changes |
|---|---|---|
| api | cost-component removal, original anchors | 4 rows move; largest move 1 (Claude Haiku 5.5 (medium), GPT-6 Luna (high), GPT-6.1 Sol (medium), GPT-6.1 Terra (max)) |
| api | alternative workload, recalibrated anchors | 4 rows move; largest move 1 (Claude Haiku 5.5 (medium), GPT-6 Luna (high), GPT-6.1 Sol (medium), GPT-6.1 Terra (max)) |
| plan | cost-component removal, original anchors; fixed-multiple arithmetic stress (not identified Plan economics for the altered workload) | 5 rows move; largest move 2 (Claude Haiku 5.5 (medium)) |
| plan | alternative workload, recalibrated anchors; fixed-multiple arithmetic stress (not identified Plan economics for the altered workload) | 4 rows move; largest move 1 (Claude Haiku 5.5 (high), GPT-6.1 Terra (max), GPT-6.1 Terra (high), GPT-6.1 Terra (xhigh)) |

### AI Coding Daily ranking: release gates

| Rule | Status | Detail |
|---|---|---|
| clip gate (E20) | passed | no basis exceeds the clipping allowance |
| cost influence flag (E91) | passed | cost not discriminating (< 10%); informational only; beta never changes (O2) |
| realised influence (E272) | fired | API: cost term offsetting (-99% of value variance); Plan: cost term offsetting (-54% of value variance); informational only, beta never changes (O2) |
| quality influence flag (E126) | passed | quality not discriminating (cost share > 90%); informational only |
| subset scoring (O17) | vacuous | subset rows scored on their own workload and anchors |
| partial component flag (E37) | fired | AA declined- or missing-task markers, or an Index reconstruction that misses AA's total (E209) |
| route dominance filter (E88) | vacuous | certifiably dearer routes set aside |
| Plan exploratory label (E61) | fired | fewer than half of Plan rows have an identified M_W |
| Plan evidence lifecycle and change detection (E18, E151, E269, O77, O79) | fired | 57 of 57 plan rows carry a possibly-superseded or expired route: claude-haiku-5-5-high@claude-max-20x, claude-haiku-5-5-high@claude-max-5x, claude-haiku-5-5-high@claude-pro, claude-haiku-5-5-medium@claude-max-20x, claude-haiku-5-5-medium@claude-max-5x, claude-haiku-5-5-medium@claude-pro, claude-opus-5-5-high@claude-max-20x, claude-opus-5-5-high@claude-max-5x, claude-opus-5-5-high@claude-pro, gpt-6-astra-high@chatgpt-plus, gpt-6-astra-high@chatgpt-pro-100, gpt-6-astra-high@chatgpt-pro-200, gpt-6-astra-high@chatgpt-pro-500, gpt-6-luna-high@chatgpt-plus, gpt-6-luna-high@chatgpt-pro-100, gpt-6-luna-high@chatgpt-pro-200, gpt-6-luna-high@chatgpt-pro-500, gpt-6-luna-medium@chatgpt-plus, gpt-6-luna-medium@chatgpt-pro-100, gpt-6-luna-medium@chatgpt-pro-200, gpt-6-luna-medium@chatgpt-pro-500, gpt-6-luna-xhigh@chatgpt-plus, gpt-6-luna-xhigh@chatgpt-pro-100, gpt-6-luna-xhigh@chatgpt-pro-200, gpt-6-luna-xhigh@chatgpt-pro-500, gpt-6-luna@chatgpt-plus, gpt-6-luna@chatgpt-pro-100, gpt-6-luna@chatgpt-pro-200, gpt-6-luna@chatgpt-pro-500, gpt-6.1-sol-high@chatgpt-plus, gpt-6.1-sol-high@chatgpt-pro-100, gpt-6.1-sol-high@chatgpt-pro-200, gpt-6.1-sol-high@chatgpt-pro-500, gpt-6.1-sol-low@chatgpt-plus, gpt-6.1-sol-low@chatgpt-pro-100, gpt-6.1-sol-low@chatgpt-pro-200, gpt-6.1-sol-low@chatgpt-pro-500, gpt-6.1-sol-medium@chatgpt-plus, gpt-6.1-sol-medium@chatgpt-pro-100, gpt-6.1-sol-medium@chatgpt-pro-200, gpt-6.1-sol-medium@chatgpt-pro-500, gpt-6.1-terra-high@chatgpt-plus, gpt-6.1-terra-high@chatgpt-pro-100, gpt-6.1-terra-high@chatgpt-pro-200, gpt-6.1-terra-high@chatgpt-pro-500, gpt-6.1-terra-medium@chatgpt-plus, gpt-6.1-terra-medium@chatgpt-pro-100, gpt-6.1-terra-medium@chatgpt-pro-200, gpt-6.1-terra-medium@chatgpt-pro-500, gpt-6.1-terra-xhigh@chatgpt-plus, gpt-6.1-terra-xhigh@chatgpt-pro-100, gpt-6.1-terra-xhigh@chatgpt-pro-200, gpt-6.1-terra-xhigh@chatgpt-pro-500, gpt-6.1-terra@chatgpt-plus, gpt-6.1-terra@chatgpt-pro-100, gpt-6.1-terra@chatgpt-pro-200, gpt-6.1-terra@chatgpt-pro-500 |
| acknowledged accounting-fault windows (O91, O92, O93, O95, O96) | fired | 12 of 57 plan rows rest on a measurement inside an acknowledged fault window; they stay selected and yield to two concordant user reports for their own model and plan, and the transfers resting on them follow: gpt-6-astra-high@chatgpt-pro-500, gpt-6-luna-high@chatgpt-pro-500, gpt-6-luna-medium@chatgpt-pro-500, gpt-6-luna-xhigh@chatgpt-pro-500, gpt-6-luna@chatgpt-pro-500, gpt-6.1-sol-high@chatgpt-pro-500, gpt-6.1-sol-low@chatgpt-pro-500, gpt-6.1-sol-medium@chatgpt-pro-500, gpt-6.1-terra-high@chatgpt-pro-500, gpt-6.1-terra-medium@chatgpt-pro-500, gpt-6.1-terra-xhigh@chatgpt-pro-500, gpt-6.1-terra@chatgpt-pro-500 |
| AA cost omits a pricing term (O94, O98, O100, O106, O108, O109, O114) | fired | ranked at the published cost; compete in interval outputs and the scenario labels' BlockerSafe test over [C, factor × C] ([C, ∞) without a stated factor, O98) without a label (scenario frequencies draw them at the published cost, O114), and leave the anchor population at the next freeze: claude-haiku-5-5-high (up to 5×), claude-haiku-5-5-medium (up to 5×) |
| valuation-basis gate (E170) | passed | every ranked row is compatible as captured or after evidenced revaluation |
| source clocks and evidence freshness (O59, O60, O65, E211, E216, E217, E218) | passed | every capture is within its age gate and none after the cutoff unless its source predates the cutoff's day; the build stops otherwise |
| build-stopping evidence gates (O64, O69, O71, O75, O99, O100, O101, O103, O105-O111, E195, E204, E225) | passed | the Coding Agent Index manifest (O64), the Terminal-Bench agent list (E225), cutoff-day row dates (O69), the three-stage all-provider plan search (O71, O75), the typed change records behind every route flag and partition split, which also produce each route's label and blocking dates within its launch- and schedule-bounded span (O99, O101, O105, O107, O110, O111), the register of AA notes covering every captured one, with the chart's inventory and duplicate-entry checks, the post-O103 capture notes, the basket-chart labels and chart-level notes' named rows (O100, O103, O106, O108) and the frontier path checks (E195, E204) hold; the build stops otherwise |
| score swing gate (E177) | vacuous | first v3 release: no previous v3 release to compare |
| anchor migration (E184) | vacuous | no main-workload migration deferred |
| configuration map coverage | fired | cohort rows without a configuration-map entry (chart labels; the agent record is derived, E267): gpt-6.1-terra, gpt-6.1-terra-high, gpt-6.1-terra-medium, gpt-6.1-terra-xhigh |
| quality clipping audit (E110) | passed | saturation disclosed; domain violations block the build |
| full benchmark set (O36, O38) | fired | listed, not ranked: gpt-6.1-sol, claude-opus-5-5, claude-sonnet-5-5, gpt-6-astra, claude-haiku-5-5-low, claude-opus-5-5-xhigh, gpt-6-astra-xhigh, gpt-6-luna-low, gpt-6.1-sol-xhigh, gpt-6.1-terra-low, gemini-4-carbon, mimo-v2-6-flash |
| missing-leaf rules (O8 provisional, E198b, E201b, E219, E221, E226) | vacuous | no ranked row has a missing leaf (O36) |
| S1M interval stream (E145) | vacuous | dormant: no ranked leaf carries a published confidence interval since O37, so S1M equals S1 (E236) |
| provider-claim label denial (E233) | vacuous | no row has a provider-claimed leaf |
| scenario outputs current (E72) | passed | scenario input hash matches the scored inputs |

## Common-leaf ranking (diagnostic)

Diagnostic only (O121): every configuration with AA's leaves and Bug Hunt, at any effort, scored on the ten leaves the two leading rankings share; it earns no label and never holds a release. Anchor version `v3-2026-10-31-common`; leaves: FrontierCode 2.0 25%, Terminal-Bench 4.0 (AA run) 20%, Bug Hunt Bench 15% (software engineering 60%), plus the 7 leaves outside software engineering every ranking shares.

**Diagnostic ranking (O121).** It earns no interval or scenario label and its clip gate (would hold on its own) never holds the release. Its bars sit at the same ladder positions as the leading rankings' but at its own levels, so the comparison below asks whether a configuration the leading rankings cannot rank would answer the same question. The answers are displayed records, not claims: a difference smaller than this ranking's quality noise margin (4.7 points, O44) is not evidence.

| Basis | Bar position | Cheapest here | Cheapest, max-effort ranking | Cheapest, AI Coding Daily ranking |
|---|---|---|---|---|
| API | median | GPT-6.1 Terra (xhigh) | GPT-6 Astra (max) (differs) | GPT-6.1 Terra (medium) (differs) |
| API | lower quartile | GPT-6.1 Terra (low) | GPT-6.1 Sol (max) (differs) | GPT-6 Luna (xhigh) (differs) |
| API | upper quartile | GPT-6.1 Sol (xhigh) | Claude Opus 5.5 (max) (differs) | GPT-6.1 Sol (medium) (differs) |
| Plan | median | GPT-6.1 Terra (xhigh) on ChatGPT Pro 500 | Claude Opus 5.5 (max) on Claude Pro (differs) | GPT-6.1 Terra (medium) on ChatGPT Pro 500 (differs) |
| Plan | lower quartile | Claude Haiku 5.5 (high) on Claude Pro | GPT-6.1 Sol (max) on ChatGPT Pro 500 (differs) | Claude Haiku 5.5 (high) on Claude Pro |
| Plan | upper quartile | GPT-6.1 Sol (xhigh) on ChatGPT Pro 500 | Claude Opus 5.5 (max) on Claude Pro (differs) | GPT-6.1 Sol (medium) on ChatGPT Pro 500 (differs) |

| Configuration | Plan rank | Plan value | Plan cost score | API rank | API value | API cost score | Quality | Quality coverage | Workload |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| [Claude Opus 5.5 (max)](https://valuerank.alolabs.dev/models/claude-opus-5-5/) | 1 | 50.62 | 28.34 | 6 | 45.49 | 7.81 | 58.04 | 100% | main |
| [Claude Sonnet 5.5 (max)](https://valuerank.alolabs.dev/models/claude-sonnet-5-5/) | 3 | 50.55 | 29.07 | 8 | 45.42 | 8.54 | 57.71 | 100% | main |
| [Claude Opus 5.5 (xhigh)](https://valuerank.alolabs.dev/models/claude-opus-5-5-xhigh/) | 7 | 50.46 | 34.71 | 9 | 45.32 | 14.15 | 55.71 | 100% | main |
| [GPT-6.1 Sol (xhigh)](https://valuerank.alolabs.dev/models/gpt-6-1-sol-xhigh/) | 10 | 48.72 | 37.46 | 1 | 48.81 | 37.82 | 52.48 | 100% | main |
| [Claude Opus 5.5 (high)](https://valuerank.alolabs.dev/models/claude-opus-5-5-high/) | 11 | 48.70 | 41.28 | 14 | 43.55 | 20.69 | 51.17 | 100% | main |
| [GPT-6.1 Sol (max)](https://valuerank.alolabs.dev/models/gpt-6-1-sol/) | 17 | 48.58 | 32.11 | 2 | 48.68 | 32.50 | 54.07 | 100% | main |
| [GPT-6.1 Terra (max)](https://valuerank.alolabs.dev/models/gpt-6-1-terra/) | 21 | 47.91 | 36.11 | 3 | 48.00 | 36.48 | 51.84 | 100% | main |
| [GPT-6.1 Sol (high)](https://valuerank.alolabs.dev/models/gpt-6-1-sol-high/) | 24 | 47.59 | 39.84 | 4 | 47.68 | 40.18 | 50.18 | 100% | main |
| [GPT-6 Astra (xhigh)](https://valuerank.alolabs.dev/models/gpt-6-astra-xhigh/) | 29 | 46.28 | 20.79 | 7 | 45.48 | 17.60 | 54.77 | 100% | main |
| [GPT-6.1 Sol (medium)](https://valuerank.alolabs.dev/models/gpt-6-1-sol-medium/) | 31 | 46.12 | 44.12 | 5 | 46.20 | 44.44 | 46.78 | 100% | main |
| [GPT-6 Astra (max)](https://valuerank.alolabs.dev/models/gpt-6-astra/) | 36 | 45.62 | 15.80 | 10 | 44.83 | 12.63 | 55.56 | 100% | main |
| [GPT-6 Astra (high)](https://valuerank.alolabs.dev/models/gpt-6-astra-high/) | 39 | 44.62 | 22.24 | 13 | 43.82 | 19.04 | 52.08 | 100% | main |
| [GPT-6.1 Terra (xhigh)](https://valuerank.alolabs.dev/models/gpt-6-1-terra-xhigh/) | 43 | 43.99 | 45.21 | 11 | 44.07 | 45.52 | 43.58 | 100% | main |
| [GPT-6.1 Terra (high)](https://valuerank.alolabs.dev/models/gpt-6-1-terra-high/) | 47 | 43.76 | 49.33 | 12 | 43.83 | 49.62 | 41.90 | 100% | main |
| [Claude Haiku 5.5 (high)](https://valuerank.alolabs.dev/models/claude-haiku-5-5-high/) | 50 | 43.16 | 80.15 | 18 | 37.95 | 59.33 | 30.82 | 100% | main |
| [GPT-6.1 Terra (medium)](https://valuerank.alolabs.dev/models/gpt-6-1-terra-medium/) | 56 | 41.98 | 53.09 | 15 | 42.05 | 53.36 | 38.28 | 100% | main |
| [Claude Haiku 5.5 (medium)](https://valuerank.alolabs.dev/models/claude-haiku-5-5-medium/) | 60 | 40.66 | 86.08 | 22 | 35.44 | 65.23 | 25.51 | 100% | main |
| [GPT-6.1 Sol (low)](https://valuerank.alolabs.dev/models/gpt-6-1-sol-low/) | 63 | 40.04 | 50.08 | 16 | 40.11 | 50.37 | 36.69 | 100% | main |
| [Claude Haiku 5.5 (low)](https://valuerank.alolabs.dev/models/claude-haiku-5-5-low/) | 67 | 39.03 | 93.47 | 24 | 33.81 | 72.57 | 20.88 | 100% | main |
| [GPT-6 Luna (max)](https://valuerank.alolabs.dev/models/gpt-6-luna/) | 70 | 38.20 | 58.53 | 17 | 38.26 | 58.76 | 31.43 | 100% | main |
| [GPT-6.1 Terra (low)](https://valuerank.alolabs.dev/models/gpt-6-1-terra-low/) | 73 | 37.88 | 59.42 | 19 | 37.94 | 59.66 | 30.70 | 100% | main |
| [GPT-6 Luna (xhigh)](https://valuerank.alolabs.dev/models/gpt-6-luna-xhigh/) | 78 | 35.87 | 63.36 | 20 | 35.93 | 63.57 | 26.71 | 100% | main |
| [GPT-6 Luna (high)](https://valuerank.alolabs.dev/models/gpt-6-luna-high/) | 81 | 35.53 | 67.02 | 21 | 35.58 | 67.21 | 25.03 | 100% | main |
| [GPT-6 Luna (medium)](https://valuerank.alolabs.dev/models/gpt-6-luna-medium/) | 86 | 33.96 | 72.51 | 23 | 34.00 | 72.66 | 21.11 | 100% | main |
| [GPT-6 Luna (low)](https://valuerank.alolabs.dev/models/gpt-6-luna-low/) | 90 | 32.73 | 91.41 | 25 | 32.74 | 91.46 | 13.17 | 100% | main |

### Common-leaf ranking (diagnostic): quality leaf scores

| Configuration | FrontierCode 2.0 | Terminal-Bench 4.0 (AA run) | Bug Hunt Bench | GDPval-AA v2.1 | AutomationBench-AA | AA-Omniscience v1.1 | AA-LCR v1.1 | HLE-Diamond | Terminal-Bench-Science 0.1 | CritPt v2 (hard subset) | Quality | Provisional |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Claude Opus 5.5 (max) | 46.4 | 59.6 | 39.7 | 68.3 | 69.5 | 74.1 | 84.7 | 67.9 | 59.0 | 61.0 | 58.04 | no |
| Claude Sonnet 5.5 (max) | 41.7 | 63.6 | 48.9 | 66.9 | 71.8 | 65.2 | 82.7 | 53.3 | 53.3 | 56.0 | 57.71 | no |
| Claude Opus 5.5 (xhigh) | 43.8 | 59.6 | 34.3 | 66.8 | 65.0 | 71.6 | 84.7 | 64.0 | 61.9 | 63.0 | 55.71 | no |
| GPT-6.1 Sol (xhigh) | 38.5 | 54.0 | 40.7 | 52.7 | 66.6 | 71.2 | 79.7 | 55.8 | 50.5 | 68.0 | 52.48 | no |
| Claude Opus 5.5 (high) | 35.9 | 56.6 | 30.2 | 60.7 | 63.2 | 71.2 | 82.7 | 55.6 | 49.0 | 58.0 | 51.17 | no |
| GPT-6.1 Sol (max) | 40.6 | 56.1 | 42.2 | 55.4 | 64.9 | 71.0 | 83.0 | 58.8 | 58.1 | 68.5 | 54.07 | no |
| GPT-6.1 Terra (max) | 42.3 | 55.6 | 38.8 | 48.8 | 60.2 | 64.8 | 82.7 | 47.3 | 57.6 | 64.5 | 51.84 | no |
| GPT-6.1 Sol (high) | 36.7 | 51.5 | 34.8 | 51.0 | 64.5 | 70.5 | 82.3 | 51.9 | 46.2 | 67.5 | 50.18 | no |
| GPT-6 Astra (xhigh) | 41.4 | 59.6 | 41.0 | 53.5 | 67.2 | 71.8 | 80.0 | 61.5 | 54.8 | 70.5 | 54.77 | no |
| GPT-6.1 Sol (medium) | 33.4 | 48.0 | 27.6 | 48.0 | 62.6 | 70.1 | 83.3 | 46.0 | 37.1 | 65.0 | 46.78 | no |
| GPT-6 Astra (max) | 42.4 | 59.1 | 42.9 | 54.2 | 68.5 | 71.2 | 80.7 | 63.8 | 63.3 | 70.5 | 55.56 | no |
| GPT-6 Astra (high) | 40.1 | 54.0 | 33.3 | 51.8 | 66.6 | 72.3 | 80.0 | 59.3 | 59.5 | 71.5 | 52.08 | no |
| GPT-6.1 Terra (xhigh) | 36.9 | 46.5 | 10.8 | 45.7 | 59.9 | 64.5 | 81.7 | 42.3 | 41.9 | 57.5 | 43.58 | no |
| GPT-6.1 Terra (high) | 37.5 | 41.9 | 9.2 | 42.6 | 58.5 | 63.9 | 82.3 | 35.4 | 33.3 | 60.5 | 41.90 | no |
| Claude Haiku 5.5 (high) | 23.2 | 21.7 | 15.2 | 46.2 | 33.7 | 52.6 | 77.3 | 23.7 | 10.0 | 42.5 | 30.82 | no |
| GPT-6.1 Terra (medium) | 34.5 | 32.3 | 7.0 | 41.2 | 57.8 | 63.3 | 80.7 | 31.3 | 24.8 | 56.0 | 38.28 | no |
| Claude Haiku 5.5 (medium) | 16.1 | 15.2 | 11.4 | 39.1 | 28.6 | 52.1 | 77.3 | 16.8 | 7.1 | 30.0 | 25.51 | no |
| GPT-6.1 Sol (low) | 20.2 | 30.8 | 21.4 | 41.1 | 52.6 | 69.0 | 84.0 | 38.2 | 11.0 | 59.5 | 36.69 | no |
| Claude Haiku 5.5 (low) | 8.0 | 12.6 | 10.5 | 31.5 | 22.9 | 51.1 | 72.0 | 14.1 | 1.9 | 21.5 | 20.88 | no |
| GPT-6 Luna (max) | 25.2 | 12.6 | 17.4 | 47.2 | 53.2 | 45.9 | 83.3 | 22.2 | 8.6 | 41.5 | 31.43 | no |
| GPT-6.1 Terra (low) | 24.5 | 15.2 | 5.7 | 35.2 | 56.2 | 61.5 | 81.0 | 24.9 | 7.6 | 48.5 | 30.70 | no |
| GPT-6 Luna (xhigh) | 18.4 | 8.1 | 13.3 | 43.6 | 47.8 | 43.5 | 80.0 | 18.9 | 5.2 | 35.5 | 26.71 | no |
| GPT-6 Luna (high) | 18.6 | 4.5 | 8.6 | 42.6 | 47.8 | 43.6 | 79.3 | 15.6 | 2.9 | 30.5 | 25.03 | no |
| GPT-6 Luna (medium) | 12.8 | 2.5 | 3.8 | 38.5 | 40.5 | 43.2 | 78.3 | 15.1 | 1.4 | 26.0 | 21.11 | no |
| GPT-6 Luna (low) | 2.2 | 0.0 | 3.8 | 27.0 | 12.0 | 41.0 | 74.0 | 10.2 | 1.0 | 9.5 | 13.17 | no |

### Common-leaf ranking (diagnostic): displayed record and noise

- API basis, displayed record (not a claim; E203): cheapest at or above quality 43.6: GPT-6.1 Terra (xhigh) ($330.42 per basket run; 13 reach it); at or above quality 30.7: GPT-6.1 Terra (low) ($104.95 per basket run; 19 reach it); at or above quality 52.5: GPT-6.1 Sol (xhigh) ($617.20 per basket run; 7 reach it).
- API basis, noise-margin companion (O44; each bar plus 4.7 quality points, so the bar's own configuration cannot decide it): cheapest at or above quality 48.3: GPT-6.1 Sol (high) ($509.65 per basket run); at or above quality 35.4: GPT-6.1 Terra (medium) ($174.91 per basket run); at or above quality 57.2: Claude Sonnet 5.5 (max) ($6,644.38 per basket run).
- Plan basis, displayed record (not a claim; E203): cheapest at or above quality 43.6: GPT-6.1 Terra (xhigh) on ChatGPT Pro 500 ($30.67 per basket run; 48 reach it); at or above quality 30.7: Claude Haiku 5.5 (high) on Claude Pro ($1.83 per basket run; 71 reach it); at or above quality 52.5: GPT-6.1 Sol (xhigh) on ChatGPT Pro 500 ($57.30 per basket run; 25 reach it).
- Plan basis, noise-margin companion (O44; each bar plus 4.7 quality points, so the bar's own configuration cannot decide it): cheapest at or above quality 48.3: Claude Opus 5.5 (high) on Claude Pro ($42.11 per basket run); at or above quality 35.4: GPT-6.1 Terra (medium) on ChatGPT Pro 500 ($16.24 per basket run); at or above quality 57.2: Claude Sonnet 5.5 (max) on Claude Pro ($112.81 per basket run).
- Safety-refusal flags (O63; costs and scores unchanged) on these bars' cheapest rows: Claude Sonnet 5.5 (max) (0 blocked and 45 fallback attempts of 870); GPT-6.1 Terra (low) (1 blocked and 0 fallback attempts of 870).
- AA cost caveat (O94; ranked at the published cost, no label of its own) on these bars' cheapest rows: Claude Haiku 5.5 (high) (AA's cost omits a pricing term; up to 5× on its cost).
- Plan route flags on these bars' cheapest plan rows: Claude Haiku 5.5 (high) on Claude Pro (possibly-superseded); Claude Opus 5.5 (high) on Claude Pro (possibly-superseded); Claude Sonnet 5.5 (max) on Claude Pro (possibly-superseded); GPT-6.1 Sol (xhigh) on ChatGPT Pro 500 (possibly-superseded, measured inside an acknowledged accounting-fault window (O91, O92)); GPT-6.1 Terra (medium) on ChatGPT Pro 500 (possibly-superseded, measured inside an acknowledged accounting-fault window (O91, O92)); GPT-6.1 Terra (xhigh) on ChatGPT Pro 500 (possibly-superseded, measured inside an acknowledged accounting-fault window (O91, O92)).
- These outputs compare ranked configurations only; listed families shown with an indicative value (O41) are outside them (O43): Gemini 4 Carbon, MiMo-V2.6-Flash.

Benchmark sampling noise (O39, an independent-task approximation): two values must differ by about 3.6 value points (median, 95%) to separate, and 0 of 24 adjacent API ranks and 0 of 41 adjacent Plan ranks of different configurations do (51 more adjacent Plan pairs are one configuration on two plans, ordered by the plans' multiples alone; E258). Its net direction is not established: every configuration is scored on the same tasks, which correlates their errors and narrows the true threshold (API 0 at correlation 0.3, 1 at correlation 0.6; Plan 0 at correlation 0.3, 0 at correlation 0.6), while sources it leaves out widen it (run-to-run and harness variance, AA's single cost run and, for the 52 Plan rows on an owner assumption (52 owner-named transfers), that assumption's error). The noise band column groups each row with the band's first row it cannot be told apart from (O42); a Plan band marked † rests on an owner assumption (an owner-named transfer or an O46 provider quota ceiling) and excludes its error: an assumed multiple can be wrong by a factor of about 3.2 before the row's value moves by the median threshold (a tolerance, not an estimate of the assumption's error). The S1T scenario shares in [scores.md](scores.md) show each row's rank-1 and top-3 frequencies under that noise.


**Listed frontier families: indicative value, not ranked and not comparable (O41).** Quality is the mean over the leaves the configuration has, renormalised, with no imputation, so these values cannot be compared with the ranking above.

| Configuration | Missing | Quality (remaining leaves) | Quality coverage | Plan value (indicative) | API value (indicative) | API cost (USD per basket run) | Plan cost (USD per basket run) |
|---|---|---:|---:|---:|---:|---:|---:|
| Gemini 4 Carbon | Bug Hunt Bench | 61.2 | 85% | 45.9 | 48.5 | $5,716.87 | $5,716.87 |
| MiMo-V2.6-Flash | Bug Hunt Bench | 36.3 | 85% | 35.9 | 42.9 | $82.84 | $72.16 |

### Common-leaf ranking (diagnostic): Plan routes and calibration

#### Measured-evidence calibration (diagnostic)

References: each workload's measured-only rows with complete cost evidence are the references: c_L = cheapest / 2, c_H = dearest x 2 (diagnostic only; the official anchors are unchanged). Status: evaluated.

- Workload `835a9baf594a1251`: measured anchors $10.35 to $658.32 from GPT-6 Astra (max), GPT-6 Astra (high), GPT-6 Astra (xhigh), GPT-6.1 Sol (max), GPT-6.1 Sol (high), GPT-6.1 Sol (low), GPT-6.1 Sol (medium), GPT-6.1 Sol (xhigh); anchor ratio 63.6 against the official 3191.4. Official Plan anchors are set by GPT-6 Luna (low) on ChatGPT Pro 500 (owner-named transfer) at the low end and GPT-6 Astra (max) on ChatGPT Plus (controlled measurement) at the high end.

| Configuration | Value on official Plan anchors | Value on measured anchors | Rank change |
|---|---:|---:|---:|
| Claude Opus 5.5 (high) ‡ | 48.70 | 54.93 | -2 |
| Claude Opus 5.5 (max) | 50.62 | 53.80 | 3 |
| Claude Opus 5.5 (xhigh) ‡ | 50.46 | 55.14 | -1 |
| GPT-6 Astra (high) ‡ | 44.62 | 46.37 | 0 |
| GPT-6 Astra (max) | 45.62 | 45.84 | 2 |
| GPT-6 Astra (xhigh) ‡ | 46.28 | 47.68 | 2 |
| GPT-6.1 Sol (high) ‡ | 47.59 | 53.49 | -1 |
| GPT-6.1 Sol (low) ‡ | 40.04 | 48.35 | -3 |
| GPT-6.1 Sol (max) | 48.58 | 52.65 | 2 |
| GPT-6.1 Sol (medium) ‡ | 46.12 | 53.02 | -2 |
| GPT-6.1 Sol (xhigh) ‡ | 48.72 | 54.06 | 0 |

Pairwise reversals: Claude Opus 5.5 (max) and Claude Opus 5.5 (high); Claude Opus 5.5 (max) and Claude Opus 5.5 (xhigh); Claude Opus 5.5 (max) and GPT-6.1 Sol (xhigh); Claude Opus 5.5 (high) and GPT-6.1 Sol (xhigh); GPT-6 Astra (max) and GPT-6 Astra (high); GPT-6 Astra (max) and GPT-6.1 Sol (low); GPT-6 Astra (high) and GPT-6.1 Sol (low); GPT-6 Astra (xhigh) and GPT-6.1 Sol (low); GPT-6 Astra (xhigh) and GPT-6.1 Sol (medium); GPT-6.1 Sol (max) and GPT-6.1 Sol (high); GPT-6.1 Sol (max) and GPT-6.1 Sol (medium). Largest value change: 8.31 points.

‡ measured on the same model at another effort (an O88 route; measured evidence under O90).

### Common-leaf ranking (diagnostic): interval outputs

**API basis, main workload: frontier.** Not evaluable: Claude Opus 5.5 (max), Claude Opus 5.5 (high), Claude Opus 5.5 (xhigh). Competing without a label of its own (E183): Claude Haiku 5.5 (high): AA's cost omits a pricing term (O94); competes over its published cost up to the stated factor; Claude Haiku 5.5 (low): AA's cost omits a pricing term (O94); competes over its published cost up to the stated factor; Claude Haiku 5.5 (medium): AA's cost omits a pricing term (O94); competes over its published cost up to the stated factor.

| Configuration | Possible frontier | Definite frontier | Definite counterexample | Possible frontier blocked by |
|---|---|---|---|---|
| GPT-6.1 Sol (max) | certified | certified | — | — |
| GPT-6.1 Terra (max) | disproved | disproved | GPT-6.1 Sol (xhigh) | GPT-6.1 Sol (xhigh) |
| GPT-6.1 Sol (high) | certified | certified | — | — |
| Claude Sonnet 5.5 (max) | certified | certified | — | — |
| GPT-6 Astra (max) | certified | certified | — | — |
| GPT-6.1 Sol (medium) | certified | certified | — | — |
| GPT-6 Astra (high) | disproved | disproved | GPT-6.1 Sol (max) | GPT-6.1 Sol (max), GPT-6.1 Sol (xhigh) |
| GPT-6.1 Terra (xhigh) | certified | certified | — | — |
| GPT-6.1 Sol (low) | disproved | disproved | GPT-6.1 Terra (medium) | GPT-6.1 Terra (medium) |
| GPT-6.1 Terra (high) | certified | certified | — | — |
| GPT-6 Luna (max) | certified | certified | — | — |
| GPT-6.1 Terra (medium) | certified | certified | — | — |
| GPT-6 Luna (xhigh) | certified | certified | — | — |
| GPT-6 Luna (high) | certified | certified | — | — |
| GPT-6 Luna (medium) | certified | certified | — | — |
| GPT-6 Astra (xhigh) | certified | certified | — | — |
| GPT-6 Luna (low) | certified | certified | — | — |
| GPT-6.1 Sol (xhigh) | certified | certified | — | — |
| GPT-6.1 Terra (low) | certified | certified | — | — | Safety-refusal flags (O63; costs and scores unchanged) on these labelled rows: Claude Sonnet 5.5 (max) (0 blocked and 45 fallback attempts of 870); GPT-6 Astra (max) (13 blocked and 0 fallback attempts of 870); GPT-6.1 Sol (max) (15 blocked and 0 fallback attempts of 870); GPT-6.1 Terra (low) (1 blocked and 0 fallback attempts of 870).

**API basis, main workload: cheapest at or above quality 43.6** (lower-median displayed quality of the non-provisional cohort configurations at freeze (E192; headline bar)). Status certified; confirmed cheapest: none.

Configurations that can be confirmed to qualify: 9 (confirmation needs the full-composite lower bound, with missing leaves at 0, to clear the bar; O25). Cheaper same-family configurations on AA's chart that were not evaluated (not ranked in this ranking: lacking its full benchmark set, or not plotted on or near the frontier; E201c, O51): GPT-6.1 Terra (xhigh): GPT-6.1 Terra (non-reasoning).

Bar comparison: compares 10 configurations that can qualify. The bar is a displayed-quality level; qualification tests each row's full-composite bounds, so a row above the bar on displayed quality can still fail to qualify confirmed when leaves are missing (E198).

| Configuration | Displayed quality − bar | Confirmed qualifies | Possibly qualifies | Possibly cheapest |
|---|---:|---|---|---|
| GPT-6.1 Sol (max) | 10.5 | certified | certified | disproved |
| GPT-6.1 Terra (max) | 8.3 | certified | certified | disproved |
| GPT-6.1 Sol (high) | 6.6 | certified | certified | disproved |
| Claude Sonnet 5.5 (max) | 14.1 | certified | certified | disproved |
| GPT-6 Astra (max) | 12.0 | certified | certified | disproved |
| GPT-6.1 Sol (medium) | 3.2 | certified | certified | certified |
| GPT-6 Astra (high) | 8.5 | certified | certified | disproved |
| GPT-6.1 Terra (xhigh) | 0.0 | disproved | certified | certified |
| GPT-6.1 Sol (low) | -6.9 | disproved | disproved | disproved |
| GPT-6.1 Terra (high) | -1.7 | disproved | disproved | disproved |
| GPT-6 Luna (max) | -12.2 | disproved | disproved | disproved |
| GPT-6.1 Terra (medium) | -5.3 | disproved | disproved | disproved |
| GPT-6 Luna (xhigh) | -16.9 | disproved | disproved | disproved |
| GPT-6 Luna (high) | -18.6 | disproved | disproved | disproved |
| GPT-6 Luna (medium) | -22.5 | disproved | disproved | disproved |
| GPT-6 Astra (xhigh) | 11.2 | certified | certified | disproved |
| GPT-6 Luna (low) | -30.4 | disproved | disproved | disproved |
| GPT-6.1 Sol (xhigh) | 8.9 | certified | certified | disproved |
| GPT-6.1 Terra (low) | -12.9 | disproved | disproved | disproved |

**API basis, main workload: cheapest at or above quality 30.7** (lower-quartile displayed quality of the non-provisional cohort configurations at freeze (O34)). Status certified; confirmed cheapest: none.

Configurations that can be confirmed to qualify: 14 (confirmation needs the full-composite lower bound, with missing leaves at 0, to clear the bar; O25). Cheaper same-family configurations on AA's chart that were not evaluated (not ranked in this ranking: lacking its full benchmark set, or not plotted on or near the frontier; E201c, O51): GPT-6 Luna (max): GPT-6 Luna (non-reasoning).

Bar comparison: compares 15 configurations that can qualify. The bar is a displayed-quality level; qualification tests each row's full-composite bounds, so a row above the bar on displayed quality can still fail to qualify confirmed when leaves are missing (E198).

| Configuration | Displayed quality − bar | Confirmed qualifies | Possibly qualifies | Possibly cheapest |
|---|---:|---|---|---|
| GPT-6.1 Sol (max) | 23.4 | certified | certified | disproved |
| GPT-6.1 Terra (max) | 21.1 | certified | certified | disproved |
| GPT-6.1 Sol (high) | 19.5 | certified | certified | disproved |
| Claude Sonnet 5.5 (max) | 27.0 | certified | certified | disproved |
| GPT-6 Astra (max) | 24.9 | certified | certified | disproved |
| GPT-6.1 Sol (medium) | 16.1 | certified | certified | disproved |
| GPT-6 Astra (high) | 21.4 | certified | certified | disproved |
| GPT-6.1 Terra (xhigh) | 12.9 | certified | certified | disproved |
| GPT-6.1 Sol (low) | 6.0 | certified | certified | disproved |
| GPT-6.1 Terra (high) | 11.2 | certified | certified | disproved |
| GPT-6 Luna (max) | 0.7 | certified | certified | certified |
| GPT-6.1 Terra (medium) | 7.6 | certified | certified | disproved |
| GPT-6 Luna (xhigh) | -4.0 | disproved | disproved | disproved |
| GPT-6 Luna (high) | -5.7 | disproved | disproved | disproved |
| GPT-6 Luna (medium) | -9.6 | disproved | disproved | disproved |
| GPT-6 Astra (xhigh) | 24.1 | certified | certified | disproved |
| GPT-6 Luna (low) | -17.5 | disproved | disproved | disproved |
| GPT-6.1 Sol (xhigh) | 21.8 | certified | certified | disproved |
| GPT-6.1 Terra (low) | 0.0 | disproved | certified | certified |

**API basis, main workload: cheapest at or above quality 52.5** (upper-quartile displayed quality of the non-provisional cohort configurations at freeze (O34)). Status certified; confirmed cheapest: none.

Configurations that can be confirmed to qualify: 4 (confirmation needs the full-composite lower bound, with missing leaves at 0, to clear the bar; O25). Cheaper same-family configurations on AA's chart that were not evaluated (not ranked in this ranking: lacking its full benchmark set, or not plotted on or near the frontier; E201c, O51): none.

Bar comparison: compares 5 configurations that can qualify. The bar is a displayed-quality level; qualification tests each row's full-composite bounds, so a row above the bar on displayed quality can still fail to qualify confirmed when leaves are missing (E198).

| Configuration | Displayed quality − bar | Confirmed qualifies | Possibly qualifies | Possibly cheapest |
|---|---:|---|---|---|
| GPT-6.1 Sol (max) | 1.6 | certified | certified | certified |
| GPT-6.1 Terra (max) | -0.6 | disproved | disproved | disproved |
| GPT-6.1 Sol (high) | -2.3 | disproved | disproved | disproved |
| Claude Sonnet 5.5 (max) | 5.2 | certified | certified | disproved |
| GPT-6 Astra (max) | 3.1 | certified | certified | disproved |
| GPT-6.1 Sol (medium) | -5.7 | disproved | disproved | disproved |
| GPT-6 Astra (high) | -0.4 | disproved | disproved | disproved |
| GPT-6.1 Terra (xhigh) | -8.9 | disproved | disproved | disproved |
| GPT-6.1 Sol (low) | -15.8 | disproved | disproved | disproved |
| GPT-6.1 Terra (high) | -10.6 | disproved | disproved | disproved |
| GPT-6 Luna (max) | -21.0 | disproved | disproved | disproved |
| GPT-6.1 Terra (medium) | -14.2 | disproved | disproved | disproved |
| GPT-6 Luna (xhigh) | -25.8 | disproved | disproved | disproved |
| GPT-6 Luna (high) | -27.4 | disproved | disproved | disproved |
| GPT-6 Luna (medium) | -31.4 | disproved | disproved | disproved |
| GPT-6 Astra (xhigh) | 2.3 | certified | certified | disproved |
| GPT-6 Luna (low) | -39.3 | disproved | disproved | disproved |
| GPT-6.1 Sol (xhigh) | 0.0 | disproved | certified | certified |
| GPT-6.1 Terra (low) | -21.8 | disproved | disproved | disproved |

**Plan basis, main workload:** not evaluated (no row has FullCost and an identified M_W (E61/E67)).

### Common-leaf ranking (diagnostic): scenario shares

The scenario panel is the 25 rows scored on the main workload (E96, E266).

Scenario outputs are stale (inputs changed since the scenario run); no shares are published for this release.

### Common-leaf ranking (diagnostic): diagnostics

- **Terminal-Bench cross-source agreement (AA's mini-SWE-agent run against tbench.ai):** defined; 0 rows take the leaf from tbench.ai (gap fill).
- **Rank separability (O39, independent-task approximation):** median separation 3.59 value points (API) and 3.65 (Plan); separable adjacent ranks: API 0 of 24, Plan 0 of 41. Assumptions: tasks are independent and each leaf's score is a mean over its published task count (plug-in binomial with the proportion (k + 1/2) / (n + 1), I28); attempts averaged within a task and tasks shared across models are ignored, so the noise is approximate; GDPval-AA: each row's rating interval as AA's model page displays it, read as a 95% normal interval (AA states no level), SD = half-width / 1.96; AA-Omniscience: each of 6,000 questions scores +1, 0 or -1, with the shares from AA's accuracy and hallucination rate; Vals boards (Vibe Code Bench v1.1, Code Migration v1.1): Vals' published standard error per record, read as the leaf's SD; AI Coding Daily: judged points over its six graded projects read as a binomial share of 60 points (an assumption; the board publishes no error).
- **FrontierCode against Cognition:** FrontierCode cross-source agreement (AA against Cognition; E234): retired (O136): the leaf is AA's FrontierCode 2.0 and Cognition's board publishes FrontierCode 1.1, so no fill or comparison is made across the two versions; panel of 0 rows.
- **Gap-fill removal (E234, diagnostic):** no ranked row has a leaf from another party or the provider.
- **Bar results without the gap fills (E234, sensitivity; labels unchanged):** cheapest displayed row as published, with fills removed, and with third-party fills no measured offset — API quality 43.6: GPT-6.1 Terra (xhigh) in all three; API quality 30.7: GPT-6.1 Terra (low) in all three; API quality 52.5: GPT-6.1 Sol (xhigh) in all three; Plan quality 43.6: GPT-6.1 Terra (xhigh) in all three; Plan quality 30.7: Claude Haiku 5.5 (high) in all three; Plan quality 52.5: GPT-6.1 Sol (xhigh) in all three.
- **Harness cost (O123, S2 stress):** unevaluable: no model is listed under two or more agents in AA's Coding Agent Index capture, so no agent effect is identified (O123). Coding Agent Index agents (each part of its costed configuration; none is the run behind the FrontierCode or Terminal-Bench leaf): GPT-6.1 Sol (max): Codex; GPT-6.1 Terra (max): Codex; Claude Opus 5.5 (max): Claude Code; Claude Sonnet 5.5 (max): Claude Code; GPT-6 Astra (max): Codex; GPT-6.1 Terra (xhigh): Codex; GPT-6.1 Terra (high): Codex; GPT-6 Luna (max): Codex; GPT-6.1 Terra (medium): Codex; GPT-6.1 Terra (low): Codex.
- **Quality agreement:** quality agreement (matched-panel sensitivity): Kendall tau 0.74 (interval 0.59 to 0.87) on 25 rows.
- **Quality-substitution value agreement (API):** quality-substitution value agreement, api basis (matched-panel sensitivity): Kendall tau 0.61 (interval 0.38 to 0.80) on 25 rows.
- **Quality-substitution value agreement (Plan):** quality-substitution value agreement, plan basis (matched-panel sensitivity): Kendall tau 0.63 (interval 0.46 to 0.79) on 25 rows.
- **Disjoint-evidence agreement:** disjoint-evidence agreement (restricted evidence comparison, not an eligible ranking): Kendall tau 0.70 (interval 0.55 to 0.84) on 25 rows.
- **Quality source shares:** AA-run 85%, independent 15%.
- **Non-discriminating leaves:** none.
- **Group drift:** estimated; flagged: none.
- **Omniscience abstention sensitivity** (z_pen = max(0, I)): 11 rows move; largest move 2 (GPT-6 Astra (high), GPT-6.1 Terra (high), GPT-6.1 Terra (low)).
- **GDPval-AA logistic sensitivity** (z = 100 / (1 + 10^((1600 - E) / 400)) against AA's pinned anchor; every other input fixed): API 11 rows move; largest move 3 (Claude Opus 5.5 (high), GPT-6.1 Sol (medium)); Plan 5 rows move; largest move 2 (GPT-6.1 Sol (xhigh)).
- **Anchor stability:** trimmed anchors (P10 / 2 and P90 x 2 (diagnostic only)) give $26.39 to $7,005.54; 16 rows move; largest move 7 (GPT-6.1 Terra (medium)).

- **Basket readiness (E22):** priced leaves cover 57% of nominal quality weight (AutomationBench-AA, FrontierCode 2.0, Terminal-Bench-Science 0.1, Terminal-Bench 4.0 (AA run)); pending components: Coding Agent Index, ITBench-AA.
- **SWE cost companion (O14, diagnostic):** 10 rows evaluated; flagged far from the median ratio: none.
- **Matched-cost diagnostic (E55):** evaluated at 70% priced quality weight; basket/matched cost-order reversals with separated intervals: 2; rank-gap warnings: 0.
- **Frontier-families anchors (E187, diagnostic):** anchors rebuilt from the 22 frontier and near-frontier references move API no rank changes (value points per cost doubling 2.14 vs 2.14 frozen); Plan 4 rows move; largest move 1 (Claude Opus 5.5 (high), GPT-6 Astra (xhigh), GPT-6.1 Sol (medium), GPT-6.1 Sol (xhigh)) (value points per cost doubling 2.26 vs 2.15 frozen).
- **Frontier-families bar (E199, sensitivity; the frozen bar stays primary):** quality 43.6 over 25 configurations; cheapest at or above it on the API main workload: not unique; possibly GPT-6.1 Sol (medium), GPT-6.1 Terra (xhigh) (compares 10 configurations that can qualify).
- **One row per family (E205, diagnostic; the frozen ladder and anchors stay primary):** with each family's primary configuration only (7 rows in the one-row-per-family bar population), the ladder (headline, lower quartile, upper quartile) would be 54.1 / 30.8 / 54.8 against 43.6 / 30.7 / 52.5 frozen; anchors rebuilt from its 6 references move API 11 rows move; largest move 6 (GPT-6.1 Terra (high)) (value points per cost doubling 2.82 vs 2.14 frozen); Plan 15 rows move; largest move 5 (Claude Haiku 5.5 (high)) (value points per cost doubling 2.81 vs 2.15 frozen).
- **Ladder over scored rows (I28, sensitivity; the frozen ladder stays primary):** the bar population keeps full-benchmark rows that have no cost; today every such row has a cost, so the ladder is unchanged.
- **Bar currency (E207, informational):** rows reaching each frozen bar: quality 43.6: 13 of 25; quality 30.7: 19 of 25; quality 52.5: 7 of 25; the current population would freeze 43.6 / 30.7 / 52.5; lifetime until the next anchor re-freeze or methodology version, whichever comes first; no staleness flag.
- **Token mix (E208):** 25 selected routes: mix unidentified: the basket's token-category shares are set-identified only (E124), so the L1 test (above 0.30 flags mix-unmatched) is not computed.
- **Observed-range sensitivity (E219, not evidence; no label changes):** with each missing leaf inside the cohort's observed range for that leaf, quality 43.6: 10 can qualify, 9 confirmed; possibly cheapest GPT-6.1 Sol (medium), GPT-6.1 Terra (xhigh); quality 30.7: 15 can qualify, 14 confirmed; possibly cheapest GPT-6 Luna (max), GPT-6.1 Terra (low); quality 52.5: 5 can qualify, 4 confirmed; possibly cheapest GPT-6.1 Sol (max), GPT-6.1 Sol (xhigh).
- **What would settle the headline bar (E221, not a claim):** rows that can but need not reach quality 43.6, with the mean score their missing leaves would need: GPT-6.1 Terra (xhigh) (no missing leaf; reporting precision only).
- **Common leaf set (E226, diagnostic; scores unchanged):** without the leaves fewer than 90% of cohort rows have (none), API no rank changes; Plan no rank changes; rows reaching each bar: quality 43.6: 13 → 13; quality 30.7: 19 → 19; quality 52.5: 7 → 7; rows whose displayed quality differs from common-leaf quality by more than one cost doubling's worth: none.
- **Harness by leaf (E227):** Terminal-Bench: mini-SWE-agent 25; Bug Hunt: Codex CLI 18, Claude Code 7.
- **Coding Agent Index safety refusals (O63, flagged; costs and scores unchanged):** GPT-6.1 Sol (max) (15 blocked of 870 attempts); Claude Opus 5.5 (max) (76 finished by Claude Opus 4.8 or Claude Opus 5 of 870 attempts); Claude Sonnet 5.5 (45 finished by Claude Opus 4.8 of 870 attempts); GPT-6 Astra (max) (13 blocked of 870 attempts); GPT-6.1 Terra (low) (1 blocked of 870 attempts).

### Leave-one-component-out cost family (E172)

Each admitted basket unit removed in turn, scored on anchors rebuilt by the freeze rule (rank changes against the primary ranking; quality held fixed).

| Removed component | API rank changes | Plan rank changes | API value points per cost doubling |
|---|---|---|---:|
| AA-Briefcase | 10 rows move; largest move 2 (Claude Opus 5.5 (high), GPT-6 Astra (xhigh)) | 6 rows move; largest move 2 (Claude Haiku 5.5 (high), GPT-6.1 Sol (xhigh)) | 2.19 |
| GDP.pdf | 7 rows move; largest move 2 (GPT-6.1 Terra (low)) | 6 rows move; largest move 1 (Claude Opus 5.5 (xhigh), Claude Sonnet 5.5 (max), GPT-6 Astra (xhigh), GPT-6 Luna (max), GPT-6.1 Sol (medium), GPT-6.1 Terra (low)) | 2.07 |
| AutomationBench-AA | 10 rows move; largest move 2 (GPT-6 Astra (high), GPT-6.1 Terra (low)) | 10 rows move; largest move 1 (Claude Haiku 5.5 (medium), Claude Opus 5.5 (xhigh), Claude Sonnet 5.5 (max), GPT-6 Astra (xhigh), GPT-6 Luna (max), GPT-6.1 Sol (high), GPT-6.1 Sol (low), GPT-6.1 Sol (medium), GPT-6.1 Terra (max), GPT-6.1 Terra (low)) | 1.99 |
| Terminal-Bench 4.0 (AA Index run) | 4 rows move; largest move 1 (Claude Haiku 5.5 (low), Claude Haiku 5.5 (medium), GPT-6 Luna (high), GPT-6 Luna (medium)) | 8 rows move; largest move 1 (Claude Haiku 5.5 (high), Claude Opus 5.5 (high), Claude Opus 5.5 (xhigh), Claude Sonnet 5.5 (max), GPT-6 Astra (xhigh), GPT-6.1 Sol (medium), GPT-6.1 Sol (xhigh), GPT-6.1 Terra (high)) | 2.14 |
| FrontierCode 2.0 | 2 rows move; largest move 1 (Claude Sonnet 5.5 (max), GPT-6 Astra (xhigh)) | 2 rows move; largest move 1 (GPT-6 Astra (xhigh), GPT-6.1 Sol (medium)) | 2.16 |
| Terminal-Bench-Science | 6 rows move; largest move 2 (Claude Opus 5.5 (high), Claude Sonnet 5.5 (max), GPT-6 Astra (xhigh), GPT-6.1 Terra (high)) | 11 rows move; largest move 2 (Claude Opus 5.5 (max)) | 2.16 |

### Subset rows: paired bridge and missing spend (E10, E173)

No row is scored on a subset workload.

### Deletion sensitivity

| Branch | Retained nominal weight | Status | API rank changes | Plan rank changes |
|---|---:|---|---|---|
| leave-out:frontierCode | 75% | evaluated | 16 rows move; largest move 3 (Claude Opus 5.5 (high)) | 10 rows move; largest move 2 (GPT-6.1 Sol (low), GPT-6.1 Terra (medium)) |
| leave-out:terminalBench | 80% | evaluated | 15 rows move; largest move 2 (Claude Opus 5.5 (xhigh)) | 17 rows move; largest move 3 (Claude Haiku 5.5 (high)) |
| leave-out:bugHunt | 85% | evaluated | 14 rows move; largest move 5 (GPT-6.1 Terra (high), GPT-6.1 Terra (xhigh)) | 18 rows move; largest move 3 (GPT-6.1 Terra (xhigh)) |
| leave-out:gdpval | 90% | evaluated | 13 rows move; largest move 3 (Claude Opus 5.5 (max), GPT-6 Astra (max)) | 9 rows move; largest move 2 (Claude Opus 5.5 (high)) |
| leave-out:automationBench | 90% | evaluated | 17 rows move; largest move 3 (Claude Opus 5.5 (xhigh)) | 15 rows move; largest move 2 (Claude Haiku 5.5 (high), Claude Opus 5.5 (xhigh), GPT-6.1 Sol (xhigh)) |
| leave-out:omniscience | 90% | evaluated | 8 rows move; largest move 3 (Claude Sonnet 5.5 (max)) | 9 rows move; largest move 2 (GPT-6.1 Sol (max)) |
| leave-out:lcr | 95% | evaluated | 9 rows move; largest move 2 (Claude Opus 5.5 (max), GPT-6 Astra (high), GPT-6.1 Terra (high)) | 2 rows move; largest move 1 (Claude Opus 5.5 (max), Claude Sonnet 5.5 (max)) |
| leave-out:hle | 98% | evaluated | 2 rows move; largest move 2 (Claude Opus 5.5 (max), Claude Sonnet 5.5 (max)) | 2 rows move; largest move 1 (Claude Opus 5.5 (max), Claude Sonnet 5.5 (max)) |
| leave-out:tbScience | 98% | evaluated | 5 rows move; largest move 2 (Claude Opus 5.5 (max)) | 2 rows move; largest move 1 (Claude Opus 5.5 (max), Claude Sonnet 5.5 (max)) |
| leave-out:critpt | 98% | evaluated | 2 rows move; largest move 1 (Claude Sonnet 5.5 (max), GPT-6 Astra (xhigh)) | 2 rows move; largest move 1 (Claude Opus 5.5 (high), GPT-6.1 Sol (xhigh)) |
| leave-source-out:Artificial Analysis | 15% | not identifiable under the coverage rule | — | — |
| basket-scope | 87% | evaluated | 9 rows move; largest move 3 (Claude Sonnet 5.5 (max)) | 10 rows move; largest move 2 (GPT-6 Luna (max), GPT-6.1 Sol (max)) |

### Cost-component removal (Terminal-Bench 4.0 (AA Index run): evaluated)

| Basis | Run | Rank changes |
|---|---|---|
| api | cost-component removal, original anchors | 4 rows move; largest move 1 (Claude Haiku 5.5 (low), Claude Haiku 5.5 (medium), GPT-6 Luna (high), GPT-6 Luna (medium)) |
| api | alternative workload, recalibrated anchors | 4 rows move; largest move 1 (Claude Haiku 5.5 (low), Claude Haiku 5.5 (medium), GPT-6 Luna (high), GPT-6 Luna (medium)) |
| plan | cost-component removal, original anchors; fixed-multiple arithmetic stress (not identified Plan economics for the altered workload) | 2 rows move; largest move 1 (Claude Opus 5.5 (high), GPT-6.1 Sol (xhigh)) |
| plan | alternative workload, recalibrated anchors; fixed-multiple arithmetic stress (not identified Plan economics for the altered workload) | 8 rows move; largest move 1 (Claude Haiku 5.5 (high), Claude Opus 5.5 (high), Claude Opus 5.5 (xhigh), Claude Sonnet 5.5 (max), GPT-6 Astra (xhigh), GPT-6.1 Sol (medium), GPT-6.1 Sol (xhigh), GPT-6.1 Terra (high)) |

### Common-leaf ranking (diagnostic): release gates

| Rule | Status | Detail |
|---|---|---|
| clip gate (E20) | passed | no basis exceeds the clipping allowance |
| cost influence flag (E91) | passed | cost not discriminating (< 10%); informational only; beta never changes (O2) |
| realised influence (E272) | fired | API: cost term offsetting (-90% of value variance); Plan: cost term offsetting (-73% of value variance); informational only, beta never changes (O2) |
| quality influence flag (E126) | passed | quality not discriminating (cost share > 90%); informational only |
| subset scoring (O17) | vacuous | subset rows scored on their own workload and anchors |
| partial component flag (E37) | fired | AA declined- or missing-task markers, or an Index reconstruction that misses AA's total (E209) |
| route dominance filter (E88) | vacuous | certifiably dearer routes set aside |
| Plan exploratory label (E61) | fired | fewer than half of Plan rows have an identified M_W |
| Plan evidence lifecycle and change detection (E18, E151, E269, O77, O79) | fired | 93 of 93 plan rows carry a possibly-superseded or expired route: claude-haiku-5-5-high@claude-max-20x, claude-haiku-5-5-high@claude-max-5x, claude-haiku-5-5-high@claude-pro, claude-haiku-5-5-low@claude-max-20x, claude-haiku-5-5-low@claude-max-5x, claude-haiku-5-5-low@claude-pro, claude-haiku-5-5-medium@claude-max-20x, claude-haiku-5-5-medium@claude-max-5x, claude-haiku-5-5-medium@claude-pro, claude-opus-5-5-high@claude-max-20x, claude-opus-5-5-high@claude-max-5x, claude-opus-5-5-high@claude-pro, claude-opus-5-5-xhigh@claude-max-20x, claude-opus-5-5-xhigh@claude-max-5x, claude-opus-5-5-xhigh@claude-pro, claude-opus-5-5@claude-max-20x, claude-opus-5-5@claude-max-5x, claude-opus-5-5@claude-pro, claude-sonnet-5-5@claude-max-20x, claude-sonnet-5-5@claude-max-5x, claude-sonnet-5-5@claude-pro, gpt-6-astra-high@chatgpt-plus, gpt-6-astra-high@chatgpt-pro-100, gpt-6-astra-high@chatgpt-pro-200, gpt-6-astra-high@chatgpt-pro-500, gpt-6-astra-xhigh@chatgpt-plus, gpt-6-astra-xhigh@chatgpt-pro-100, gpt-6-astra-xhigh@chatgpt-pro-200, gpt-6-astra-xhigh@chatgpt-pro-500, gpt-6-astra@chatgpt-plus, gpt-6-astra@chatgpt-pro-100, gpt-6-astra@chatgpt-pro-200, gpt-6-astra@chatgpt-pro-500, gpt-6-luna-high@chatgpt-plus, gpt-6-luna-high@chatgpt-pro-100, gpt-6-luna-high@chatgpt-pro-200, gpt-6-luna-high@chatgpt-pro-500, gpt-6-luna-low@chatgpt-plus, gpt-6-luna-low@chatgpt-pro-100, gpt-6-luna-low@chatgpt-pro-200, gpt-6-luna-low@chatgpt-pro-500, gpt-6-luna-medium@chatgpt-plus, gpt-6-luna-medium@chatgpt-pro-100, gpt-6-luna-medium@chatgpt-pro-200, gpt-6-luna-medium@chatgpt-pro-500, gpt-6-luna-xhigh@chatgpt-plus, gpt-6-luna-xhigh@chatgpt-pro-100, gpt-6-luna-xhigh@chatgpt-pro-200, gpt-6-luna-xhigh@chatgpt-pro-500, gpt-6-luna@chatgpt-plus, gpt-6-luna@chatgpt-pro-100, gpt-6-luna@chatgpt-pro-200, gpt-6-luna@chatgpt-pro-500, gpt-6.1-sol-high@chatgpt-plus, gpt-6.1-sol-high@chatgpt-pro-100, gpt-6.1-sol-high@chatgpt-pro-200, gpt-6.1-sol-high@chatgpt-pro-500, gpt-6.1-sol-low@chatgpt-plus, gpt-6.1-sol-low@chatgpt-pro-100, gpt-6.1-sol-low@chatgpt-pro-200, gpt-6.1-sol-low@chatgpt-pro-500, gpt-6.1-sol-medium@chatgpt-plus, gpt-6.1-sol-medium@chatgpt-pro-100, gpt-6.1-sol-medium@chatgpt-pro-200, gpt-6.1-sol-medium@chatgpt-pro-500, gpt-6.1-sol-xhigh@chatgpt-plus, gpt-6.1-sol-xhigh@chatgpt-pro-100, gpt-6.1-sol-xhigh@chatgpt-pro-200, gpt-6.1-sol-xhigh@chatgpt-pro-500, gpt-6.1-sol@chatgpt-plus, gpt-6.1-sol@chatgpt-pro-100, gpt-6.1-sol@chatgpt-pro-200, gpt-6.1-sol@chatgpt-pro-500, gpt-6.1-terra-high@chatgpt-plus, gpt-6.1-terra-high@chatgpt-pro-100, gpt-6.1-terra-high@chatgpt-pro-200, gpt-6.1-terra-high@chatgpt-pro-500, gpt-6.1-terra-low@chatgpt-plus, gpt-6.1-terra-low@chatgpt-pro-100, gpt-6.1-terra-low@chatgpt-pro-200, gpt-6.1-terra-low@chatgpt-pro-500, gpt-6.1-terra-medium@chatgpt-plus, gpt-6.1-terra-medium@chatgpt-pro-100, gpt-6.1-terra-medium@chatgpt-pro-200, gpt-6.1-terra-medium@chatgpt-pro-500, gpt-6.1-terra-xhigh@chatgpt-plus, gpt-6.1-terra-xhigh@chatgpt-pro-100, gpt-6.1-terra-xhigh@chatgpt-pro-200, gpt-6.1-terra-xhigh@chatgpt-pro-500, gpt-6.1-terra@chatgpt-plus, gpt-6.1-terra@chatgpt-pro-100, gpt-6.1-terra@chatgpt-pro-200, gpt-6.1-terra@chatgpt-pro-500 |
| acknowledged accounting-fault windows (O91, O92, O93, O95, O96) | fired | 18 of 93 plan rows rest on a measurement inside an acknowledged fault window; they stay selected and yield to two concordant user reports for their own model and plan, and the transfers resting on them follow: gpt-6-astra-high@chatgpt-pro-500, gpt-6-astra-xhigh@chatgpt-pro-500, gpt-6-astra@chatgpt-pro-500, gpt-6-luna-high@chatgpt-pro-500, gpt-6-luna-low@chatgpt-pro-500, gpt-6-luna-medium@chatgpt-pro-500, gpt-6-luna-xhigh@chatgpt-pro-500, gpt-6-luna@chatgpt-pro-500, gpt-6.1-sol-high@chatgpt-pro-500, gpt-6.1-sol-low@chatgpt-pro-500, gpt-6.1-sol-medium@chatgpt-pro-500, gpt-6.1-sol-xhigh@chatgpt-pro-500, gpt-6.1-sol@chatgpt-pro-500, gpt-6.1-terra-high@chatgpt-pro-500, gpt-6.1-terra-low@chatgpt-pro-500, gpt-6.1-terra-medium@chatgpt-pro-500, gpt-6.1-terra-xhigh@chatgpt-pro-500, gpt-6.1-terra@chatgpt-pro-500 |
| AA cost omits a pricing term (O94, O98, O100, O106, O108, O109, O114) | fired | ranked at the published cost; compete in interval outputs and the scenario labels' BlockerSafe test over [C, factor × C] ([C, ∞) without a stated factor, O98) without a label (scenario frequencies draw them at the published cost, O114), and leave the anchor population at the next freeze: claude-haiku-5-5-high (up to 5×), claude-haiku-5-5-low (up to 5×), claude-haiku-5-5-medium (up to 5×) |
| valuation-basis gate (E170) | passed | every ranked row is compatible as captured or after evidenced revaluation |
| source clocks and evidence freshness (O59, O60, O65, E211, E216, E217, E218) | passed | every capture is within its age gate and none after the cutoff unless its source predates the cutoff's day; the build stops otherwise |
| build-stopping evidence gates (O64, O69, O71, O75, O99, O100, O101, O103, O105-O111, E195, E204, E225) | passed | the Coding Agent Index manifest (O64), the Terminal-Bench agent list (E225), cutoff-day row dates (O69), the three-stage all-provider plan search (O71, O75), the typed change records behind every route flag and partition split, which also produce each route's label and blocking dates within its launch- and schedule-bounded span (O99, O101, O105, O107, O110, O111), the register of AA notes covering every captured one, with the chart's inventory and duplicate-entry checks, the post-O103 capture notes, the basket-chart labels and chart-level notes' named rows (O100, O103, O106, O108) and the frontier path checks (E195, E204) hold; the build stops otherwise |
| score swing gate (E177) | vacuous | first v3 release: no previous v3 release to compare |
| anchor migration (E184) | vacuous | no main-workload migration deferred |
| configuration map coverage | fired | cohort rows without a configuration-map entry (chart labels; the agent record is derived, E267): gpt-6.1-terra, gpt-6.1-terra-high, gpt-6.1-terra-low, gpt-6.1-terra-medium, gpt-6.1-terra-xhigh |
| quality clipping audit (E110) | passed | saturation disclosed; domain violations block the build |
| full benchmark set (O36, O38) | fired | listed, not ranked: gemini-4-carbon, mimo-v2-6-flash |
| missing-leaf rules (O8 provisional, E198b, E201b, E219, E221, E226) | vacuous | no ranked row has a missing leaf (O36) |
| S1M interval stream (E145) | vacuous | dormant: no ranked leaf carries a published confidence interval since O37, so S1M equals S1 (E236) |
| provider-claim label denial (E233) | vacuous | no row has a provider-claimed leaf |
| scenario outputs current (E72) | fired | scenario outputs stale (inputs changed since the scenario run); release held |
| diagnostic ranking (O121) | fired | no label is issued and the gates are disclosed without holding the release |


## Basket cost by component

USD at API rates for the exact configuration; "—" marks a component without an exact cost.

| Configuration | Coding Agent Index | ITBench-AA | AA-Briefcase | GDP.pdf | AutomationBench-AA | Terminal-Bench 4.0 (AA Index run) | FrontierCode 2.0 | Terminal-Bench-Science | Basket cost | Missing admitted components |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Claude Opus 5.5 (max) | $3,312.59 | $146.00 | $1,915.18 | $155.23 | $938.69 | $865.21 | $1,776.08 | $1,397.97 | $10,360.96 | none |
| Claude Sonnet 5.5 (max) | $3,857.44 | — | $1,863.13 | $79.43 | $678.32 | $834.67 | $1,525.59 | $1,663.25 | $10,501.82 | none |
| GPT-6.1 Sol (max) | $436.35 | — | $210.45 | $41.99 | $195.01 | $120.30 | $149.21 | $233.73 | $1,387.03 | none |
| GPT-6 Astra (max) | $2,040.49 | $133.00 | $864.69 | $207.58 | $1,048.30 | $560.88 | $863.12 | $1,223.34 | $6,808.39 | none |
| GPT-6 Luna (max) | $46.16 | — | $15.47 | $2.85 | $23.91 | $15.59 | $23.22 | $31.79 | $158.99 | none |

### Valuation basis

Valuation-basis gate (E170): 5 compatible as captured. AA's Index category costs reconcile exactly with the prices AA displays for each configuration at capture, so its applied prices are the prices in force at the release cutoff. Token metering (E176): 5 not published per configuration; AA values cached input at live measurements of each model's typical cache-hit rate. Source intervals (E174): terminalBench: captured, level 95% (tbench.ai: "The whiskers span the 95% confidence interval"); gdpval: captured, level unstated, level not stated by the source (the 95% level on AA's methodology page belongs to AA-Briefcase).

## Plan route selection

The Plan amount is the selected multiple times the cash paid for the fee period (E166), typed by what the measurement establishes; it is not capacity unless it says so. The multiple values only the measured workload's API-equivalent consumption; other plan features are not valued.

| Configuration | Selected route | Plan amount | Basket runs per fee period | Identification | Plan cost (USD per basket run) | Flags | Selection reason |
|---|---|---|---|---|---:|---|---|
| Claude Opus 5.5 (max) | Claude Pro $20 · Opus 5.5 (58.9×, measured) | $1,178 per month: measured-workload capacity | 0.11 per month | unidentified | $175.91 | workload-unmatched; possibly-superseded; valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| Claude Sonnet 5.5 (max) | Claude Pro $20 · common Claude assumption (58.9×, assumption) | $1,178 per month: assumed API-equivalent consumption (owner-named transfer) from claude-pro-opus55-semianalysis | 0.11 per month | unidentified | $178.30 | workload-unmatched; owner-named transfer (assumption); possibly-superseded; valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| GPT-6.1 Sol (max) | ChatGPT Pro 500 $500 · GPT-6.1 Sol (10.772×, measured) | $5,386 per month: measured-workload capacity | 3.88 per month | unidentified | $128.76 | workload-unmatched; possibly-superseded; measured inside an acknowledged accounting-fault window (O91, O92); valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| GPT-6 Astra (max) | ChatGPT Pro 200 $200 · GPT-6 Astra (14.485×, measured) | $2,897 per month: measured-workload capacity | 0.43 per month | unidentified | $470.03 | workload-unmatched; possibly-superseded; valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| GPT-6 Luna (max) | ChatGPT Pro 500 $500 · common GPT assumption (10.772×, assumption) | $5,386 per month: assumed API-equivalent consumption (owner-named transfer) from chatgpt-pro500-gpt61sol-semianalysis | 33.88 per month | unidentified | $14.76 | workload-unmatched; owner-named transfer (assumption); possibly-superseded; measured inside an acknowledged accounting-fault window (O91, O92); valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |

### Route alternatives

Every admissible route-measurement pair in comparator order (E171) and the comparator's pick with the selected pair removed (E179). A larger displayed multiple is arithmetic on the measured workload, never a claim that the route is cheaper on the scored workload. Workday-feasible multiple (E15), for the 5 routed rows: not evaluated: no evidenced quota schema for this route.

| Configuration | Admissible pairs | Unidentified | Pairs (multiple, status) | Leave-selected-out choice |
|---|---:|---:|---|---|
| Claude Opus 5.5 (max) | 3 | 3 | claude-pro-opus55-semianalysis (58.9×, selected); claude-max20x-opus55-semianalysis (58.63×, not selected by the comparator); claude-max5x-opus55-semianalysis (57.25×, not selected by the comparator) | claude-max20x-opus55-semianalysis (58.63×, value 60.93) |
| Claude Sonnet 5.5 (max) | 3 | 3 | claude-pro-claude-sonnet-5-5-common-opus55-assumption (58.9×, selected); claude-max20x-claude-sonnet-5-5-common-opus55-assumption (58.63×, not selected by the comparator); claude-max5x-claude-sonnet-5-5-common-opus55-assumption (57.25×, not selected by the comparator) | claude-max20x-claude-sonnet-5-5-common-opus55-assumption (58.63×, value 59.99) |
| GPT-6.1 Sol (max) | 4 | 4 | chatgpt-pro500-gpt61sol-semianalysis (10.772×, selected); chatgpt-plus-gpt61sol-semianalysis (10.55×, not selected by the comparator); chatgpt-pro100-gpt61sol-semianalysis (10.55×, not selected by the comparator); chatgpt-pro200-gpt61sol-semianalysis (10.42×, not selected by the comparator) | chatgpt-plus-gpt61sol-semianalysis (10.55×, value 59.52) |
| GPT-6 Astra (max) | 4 | 4 | chatgpt-pro200-gpt6astra-semianalysis (14.485×, selected); chatgpt-pro500-gpt6astra-semianalysis (13.91×, not selected by the comparator); chatgpt-pro100-gpt6astra-semianalysis (13.22×, not selected by the comparator); chatgpt-plus-gpt6astra-semianalysis (8.1×, not selected by the comparator) | chatgpt-pro500-gpt6astra-semianalysis (13.91×, value 54.55) |
| GPT-6 Luna (max) | 4 | 4 | chatgpt-pro500-gpt-6-luna-common-gpt-assumption (10.772×, selected); chatgpt-pro100-gpt-6-luna-common-gpt-assumption (10.55×, not selected by the comparator); chatgpt-pro200-gpt-6-luna-common-gpt-assumption (10.42×, not selected by the comparator); chatgpt-plus-gpt-6-luna-common-gpt-assumption (8.1×, not selected by the comparator) | chatgpt-pro100-gpt-6-luna-common-gpt-assumption (10.55×, value 54.06) |

### Plan allowance report cells (O71, O81)

52 cells; 0 pass. A cell on a plan the Plan ranking does not list is evidence only (O85).

| Provider | Plan | Model | Unit | Region | Eligible reports | Verdict |
|---|---|---|---|---|---|---|
| Anthropic | Claude (plan redacted) (not listed) | Claude Opus 5.5 | week | global | 0 of 1 | fails: 0 non-provisional report(s) in the current partition |
| Anthropic | Claude Max (tier unstated) (not listed) | Claude Opus 5.5 | week | global | 0 of 3 | fails: 0 non-provisional report(s) in the current partition |
| Anthropic | Claude Max 20x | Claude Opus 5.5 | 5h | global | 1 of 2 | fails: a 5-hour figure never converts to a billing period (O82) |
| Anthropic | Claude Max 20x | Claude Opus 5.5 | month | global | 0 of 1 | fails: 0 non-provisional report(s) in the current partition |
| Anthropic | Claude Max 20x | Claude Opus 5.5 | week | global | 4 of 11 | fails: 0 non-provisional report(s) in the current partition |
| Anthropic | Claude Max 20x | — | week | global | 0 of 6 | fails: 0 non-provisional report(s) in the current partition |
| Anthropic | Claude Max 5x | Claude Opus 5.5 | month | global | 0 of 1 | fails: 0 non-provisional report(s) in the current partition |
| Anthropic | Claude Max 5x | Claude Opus 5.5 | week | global | 2 of 2 | fails: 0 non-provisional report(s) in the current partition |
| Anthropic | Claude Max 5x | — | week | global | 0 of 1 | fails: 0 non-provisional report(s) in the current partition |
| Anthropic | Claude Pro | Claude Opus 5.5 | 5h | global | 1 of 4 | fails: a 5-hour figure never converts to a billing period (O82) |
| Anthropic | Claude Pro | Claude Opus 5.5 | month | global | 0 of 1 | fails: 0 non-provisional report(s) in the current partition |
| Anthropic | Claude Pro | Claude Opus 5.5 | week | global | 1 of 9 | fails: 0 non-provisional report(s) in the current partition |
| Anthropic | Claude Pro | — | week | global | 0 of 1 | fails: 0 non-provisional report(s) in the current partition |
| Anthropic | Claude Team Premium (not listed) | Claude Opus 5.5 | week | global | 0 of 1 | fails: 0 non-provisional report(s) in the current partition |
| Google | Google AI (tier unstated) (not listed) | gemini-4-argon | week | global | 0 of 1 | fails: 0 non-provisional report(s) in the current partition |
| Google | Google AI Pro | gemini-4-argon | week | global | 3 of 3 | fails: largest lower bound 1.35× the smallest upper bound (O86 allows 1.20×) in the current partition |
| Kimi | Kimi Allegretto (legacy, CN) (not listed) | kimi-k3-1-pro | 5h | CN | 2 of 4 | fails: a 5-hour figure never converts to a billing period (O82) |
| Kimi | Kimi Allegretto (legacy, CN) (not listed) | kimi-k3-1-pro | month | CN | 2 of 3 | fails: 1 non-provisional report(s) in the current partition |
| Kimi | Kimi Allegretto (legacy, CN) (not listed) | kimi-k3-1-pro | week | CN | 1 of 3 | fails: 0 non-provisional report(s) in the current partition |
| Kimi | Kimi Allegro (legacy, CN) (not listed) | kimi-k3-1-pro | 5h | CN | 1 of 5 | fails: a 5-hour figure never converts to a billing period (O82) |
| Kimi | Kimi Allegro (legacy, CN) (not listed) | kimi-k3-1-pro | month | CN | 0 of 1 | fails: 0 non-provisional report(s) in the current partition |
| Kimi | Kimi Allegro (legacy, CN) (not listed) | kimi-k3-1-pro | week | CN | 0 of 2 | fails: 0 non-provisional report(s) in the current partition |
| Kimi | Kimi Max (new, CN) (not listed) | kimi-k3-1-pro | 5h | CN | 0 of 2 | fails: a 5-hour figure never converts to a billing period (O82) |
| Kimi | Kimi Max (new, CN) (not listed) | kimi-k3-1-pro | month | CN | 0 of 1 | fails: 0 non-provisional report(s) in the current partition |
| Kimi | Kimi Plus | kimi-k3-1-pro | 5h | global | 0 of 1 | fails: a 5-hour figure never converts to a billing period (O82) |
| Kimi | Kimi Plus (new, CN) (not listed) | kimi-k3-1-pro | 5h | CN | 0 of 1 | fails: a 5-hour figure never converts to a billing period (O82) |
| Kimi | Kimi Pro (new, CN) (not listed) | kimi-k3-1-pro | 5h | CN | 0 of 1 | fails: a 5-hour figure never converts to a billing period (O82) |
| Kimi | Kimi Ultra (new, CN) (not listed) | kimi-k3-1-pro | 5h | CN | 0 of 1 | fails: a 5-hour figure never converts to a billing period (O82) |
| Kimi | Kimi legacy plan (tier not stated, CN) (not listed) | kimi-k3-1-pro | 5h | CN | 0 of 1 | fails: a 5-hour figure never converts to a billing period (O82) |
| Kimi | Kimi ¥199 plan (legacy or new not stated, CN) (not listed) | kimi-k3-1-pro | 5h | CN | 0 of 2 | fails: a 5-hour figure never converts to a billing period (O82) |
| MiniMax | MiniMax M Plan (tier unstated) (not listed) | minimax-m3-1-flash | week | global | 0 of 1 | fails: 0 non-provisional report(s) in the current partition |
| MiniMax | MiniMax Token Plan Max (legacy) (not listed) | minimax-m3-1-flash | 5h | global | 0 of 1 | fails: a 5-hour figure never converts to a billing period (O82) |
| MiniMax | MiniMax Token Plan Max (legacy) (not listed) | minimax-m3-1-flash | week | global | 1 of 1 | fails: 0 non-provisional report(s) in the current partition |
| MiniMax | MiniMax Token Plan lowest tier (legacy) (not listed) | minimax-m3-1-flash | 5h | global | 1 of 1 | fails: a 5-hour figure never converts to a billing period (O82) |
| MiniMax | MiniMax lowest tier ("lite") (not listed) | — | week | global | 0 of 1 | fails: 0 non-provisional report(s) in the current partition |
| OpenAI | ChatGPT (legacy account, tier unstated) (not listed) | GPT-6.1 Sol | week | global | 0 of 1 | fails: 0 non-provisional report(s) in the current partition |
| OpenAI | ChatGPT Plus | GPT-6 Astra | 5h | global | 0 of 2 | fails: a 5-hour figure never converts to a billing period (O82) |
| OpenAI | ChatGPT Plus | GPT-6 Luna | 5h | global | 0 of 1 | fails: a 5-hour figure never converts to a billing period (O82) |
| OpenAI | ChatGPT Plus | GPT-6 Luna | month | global | 0 of 1 | fails: 0 non-provisional report(s) in the current partition |
| OpenAI | ChatGPT Plus | GPT-6.1 Sol | 5h | global | 0 of 3 | fails: a 5-hour figure never converts to a billing period (O82) |
| OpenAI | ChatGPT Plus | GPT-6.1 Sol | week | global | 0 of 2 | fails: 0 non-provisional report(s) in the current partition |
| OpenAI | ChatGPT Plus | gpt-5.6-luna-low | 5h | global | 0 of 1 | fails: a 5-hour figure never converts to a billing period (O82) |
| OpenAI | ChatGPT Plus | gpt-5.6-luna-low | week | global | 0 of 1 | fails: 0 non-provisional report(s) in the current partition |
| OpenAI | ChatGPT Pro (tier unstated) (not listed) | GPT-6 Astra | week | global | 0 of 1 | fails: 0 non-provisional report(s) in the current partition |
| OpenAI | ChatGPT Pro 100 | GPT-6 Astra | week | global | 0 of 4 | fails: 0 non-provisional report(s) in the current partition |
| OpenAI | ChatGPT Pro 100 | GPT-6.1 Sol | week | global | 0 of 1 | fails: 0 non-provisional report(s) in the current partition |
| OpenAI | ChatGPT Pro 200 (grandfathered 20x) | GPT-6 Astra | week | global | 0 of 1 | fails: 0 non-provisional report(s) in the current partition |
| OpenAI | ChatGPT Pro 200 (grandfathered 20x) | GPT-6.1 Sol | week | global | 1 of 3 | fails: 0 non-provisional report(s) in the current partition |
| OpenAI | ChatGPT Pro 500 | GPT-6 Astra | week | global | 0 of 1 | fails: 0 non-provisional report(s) in the current partition |
| OpenAI | ChatGPT Pro 500 | GPT-6.1 Sol | week | global | 0 of 1 | fails: 0 non-provisional report(s) in the current partition |
| Xiaomi | MiMo Token Plan Lite | mimo-v2-6-pro | month | global | 1 of 1 | fails: 1 non-provisional report(s) in the current partition |
| Xiaomi | MiMo Token Plan Max | mimo-v2-6-pro | month | global | 1 of 1 | fails: 1 non-provisional report(s) in the current partition |

### Measured-only Plan view

Admission: measurement candidates of grade controlled (exact effort, or the same model at another effort, O90) or concordant reports (no owner assumption of any kind, no diagnostics). Selection: the official selector (E111, E88, E85) rerun among the admitted candidates. Panel: rows with an admitted measured candidate; others listed as 'no measured route' (no API fallback).

| Configuration | Status | Route | Plan cost | Value | Rank |
|---|---|---|---:|---:|---:|
| Claude Opus 5.5 (max) | measured, target-workload unmatched | claude-pro-opus55-semianalysis | $175.91 | 60.95 | 1 |
| GPT-6.1 Sol (max) | measured, target-workload unmatched | chatgpt-pro500-gpt61sol-semianalysis | $128.76 | 59.61 | 2 |
| GPT-6 Astra (max) | measured, target-workload unmatched | chatgpt-pro200-gpt6astra-semianalysis | $470.03 | 54.74 | 3 |
| Claude Sonnet 5.5 (max) | no measured route | — | — | — | — |
| GPT-6 Luna (max) | no measured route | — | — | — | — |

#### Measured-evidence calibration (diagnostic)

References: each workload's measured-only rows with complete cost evidence are the references: c_L = cheapest / 2, c_H = dearest x 2 (diagnostic only; the official anchors are unchanged). Status: evaluated.

- Workload `aad36e77d6e17386`: measured anchors $64.38 to $940.06 from GPT-6 Astra (max), GPT-6.1 Sol (max); anchor ratio 14.6 against the official 227.8. Official Plan anchors are set by GPT-6 Luna (max) on ChatGPT Pro 500 (owner-named transfer) at the low end and GPT-6 Astra (max) on ChatGPT Plus (controlled measurement) at the high end.

| Configuration | Value on official Plan anchors | Value on measured anchors | Rank change |
|---|---:|---:|---:|
| Claude Opus 5.5 (max) | 60.95 | 66.18 | 1 |
| GPT-6 Astra (max) | 54.74 | 55.33 | 0 |
| GPT-6.1 Sol (max) | 59.61 | 66.32 | -1 |

Pairwise reversals: Claude Opus 5.5 (max) and GPT-6.1 Sol (max). Largest value change: 6.70 points.

## Interval outputs

**API basis, main workload: frontier.** Not evaluable: Claude Opus 5.5 (max).

| Configuration | Possible frontier | Definite frontier | Definite counterexample | Possible frontier blocked by |
|---|---|---|---|---|
| GPT-6.1 Sol (max) | certified | certified | — | — |
| Claude Sonnet 5.5 (max) | certified | certified | — | — |
| GPT-6 Astra (max) | certified | certified | — | — |
| GPT-6 Luna (max) | certified | certified | — | — | Safety-refusal flags (O63; costs and scores unchanged) on these labelled rows: Claude Sonnet 5.5 (max) (0 blocked and 45 fallback attempts of 870); GPT-6 Astra (max) (13 blocked and 0 fallback attempts of 870); GPT-6.1 Sol (max) (15 blocked and 0 fallback attempts of 870).

**API basis, main workload: cheapest at or above quality 65.2** (lower-median displayed quality of the non-provisional cohort configurations at freeze (E192; headline bar)). Status certified; confirmed cheapest: none.

Configurations that can be confirmed to qualify: 1 (confirmation needs the full-composite lower bound, with missing leaves at 0, to clear the bar; O25). Cheaper same-family configurations on AA's chart that were not evaluated (not ranked in this ranking: lacking its full benchmark set, or not plotted on or near the frontier; E201c, O51): Claude Sonnet 5.5 (max): Claude Sonnet 5.5 (xhigh with fallback), Claude Sonnet 5.5 (high with fallback), Claude Sonnet 5.5 (medium with fallback), Claude Sonnet 5.5 (low with fallback); GPT-6 Astra (max): GPT-6 Astra (xhigh), GPT-6 Astra (high), GPT-6 Astra (medium), GPT-6 Astra (low).

Bar comparison: compares 2 configurations that can qualify. The bar is a displayed-quality level; qualification tests each row's full-composite bounds, so a row above the bar on displayed quality can still fail to qualify confirmed when leaves are missing (E198).

| Configuration | Displayed quality − bar | Confirmed qualifies | Possibly qualifies | Possibly cheapest |
|---|---:|---|---|---|
| GPT-6.1 Sol (max) | -1.5 | disproved | disproved | disproved |
| Claude Sonnet 5.5 (max) | 1.1 | certified | certified | certified |
| GPT-6 Astra (max) | 0.0 | disproved | certified | certified |
| GPT-6 Luna (max) | -22.0 | disproved | disproved | disproved |

**API basis, main workload: cheapest at or above quality 63.7** (lower-quartile displayed quality of the non-provisional cohort configurations at freeze (O34)). Status certified; confirmed cheapest: none.

Configurations that can be confirmed to qualify: 2 (confirmation needs the full-composite lower bound, with missing leaves at 0, to clear the bar; O25). Cheaper same-family configurations on AA's chart that were not evaluated (not ranked in this ranking: lacking its full benchmark set, or not plotted on or near the frontier; E201c, O51): GPT-6.1 Sol (max): GPT-6.1 Sol (xhigh), GPT-6.1 Sol (high), GPT-6.1 Sol (medium), GPT-6.1 Sol (low); GPT-6 Astra (max): GPT-6 Astra (xhigh), GPT-6 Astra (high), GPT-6 Astra (medium), GPT-6 Astra (low).

Bar comparison: compares 3 configurations that can qualify. The bar is a displayed-quality level; qualification tests each row's full-composite bounds, so a row above the bar on displayed quality can still fail to qualify confirmed when leaves are missing (E198).

| Configuration | Displayed quality − bar | Confirmed qualifies | Possibly qualifies | Possibly cheapest |
|---|---:|---|---|---|
| GPT-6.1 Sol (max) | 0.0 | disproved | certified | certified |
| Claude Sonnet 5.5 (max) | 2.5 | certified | certified | disproved |
| GPT-6 Astra (max) | 1.5 | certified | certified | certified |
| GPT-6 Luna (max) | -20.6 | disproved | disproved | disproved |

**API basis, main workload: cheapest at or above quality 66.2** (upper-quartile displayed quality of the non-provisional cohort configurations at freeze (O34)). Status certified; confirmed cheapest: none.

Configurations that can be confirmed to qualify: 0 (confirmation needs the full-composite lower bound, with missing leaves at 0, to clear the bar; O25). Cheaper same-family configurations on AA's chart that were not evaluated (not ranked in this ranking: lacking its full benchmark set, or not plotted on or near the frontier; E201c, O51): Claude Sonnet 5.5 (max): Claude Sonnet 5.5 (xhigh with fallback), Claude Sonnet 5.5 (high with fallback), Claude Sonnet 5.5 (medium with fallback), Claude Sonnet 5.5 (low with fallback).

Bar comparison: vacuous: fewer than two evaluable configurations can qualify. The bar is a displayed-quality level; qualification tests each row's full-composite bounds, so a row above the bar on displayed quality can still fail to qualify confirmed when leaves are missing (E198).

| Configuration | Displayed quality − bar | Confirmed qualifies | Possibly qualifies | Possibly cheapest |
|---|---:|---|---|---|
| GPT-6.1 Sol (max) | -2.5 | disproved | disproved | disproved |
| Claude Sonnet 5.5 (max) | 0.0 | disproved | certified | certified |
| GPT-6 Astra (max) | -1.1 | disproved | disproved | disproved |
| GPT-6 Luna (max) | -23.1 | disproved | disproved | disproved |

**Plan basis, main workload:** not evaluated (no row has FullCost and an identified M_W (E61/E67)).

## Scenario shares

The scenario panel is the 5 rows scored on the main workload (E96, E266).

Frequencies over 10,000 scenarios per run (seed 20261031); streams are defined in [methodology.md](methodology.md#uncertainty-outputs). S1T adds benchmark sampling noise under an independent-task approximation (O39); the other streams exclude it, and every stream excludes correlated-task, harness and attempt effects (E155).

### API basis: rank 1

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M | S1T |
|---|---:|---:|---:|---:|---:|---:|
| Claude Opus 5.5 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Sonnet 5.5 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Luna (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (max) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% |

### API basis: rank 3 or better

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M | S1T |
|---|---:|---:|---:|---:|---:|---:|
| Claude Opus 5.5 (max) | 0.0% | 0.0% | 43.8% | 0.0% | 0.0% | 49.9% |
| Claude Sonnet 5.5 (max) | 0.0% | 0.0% | 1.0% | 0.0% | 0.0% | 16.1% |
| GPT-6 Astra (max) | 100.0% | 100.0% | 79.2% | 100.0% | 100.0% | 59.3% |
| GPT-6 Luna (max) | 100.0% | 100.0% | 75.9% | 100.0% | 100.0% | 74.7% |
| GPT-6.1 Sol (max) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% |

### API basis: on the frontier

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M | S1T |
|---|---:|---:|---:|---:|---:|---:|
| Claude Opus 5.5 (max) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 87.5% |
| Claude Sonnet 5.5 (max) | 0.0% | 0.0% | 1.9% | 0.0% | 0.0% | 24.4% |
| GPT-6 Astra (max) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 78.9% |
| GPT-6 Luna (max) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% |
| GPT-6.1 Sol (max) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% |

### API basis: value-score dispersion (SD; covariance term)

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M | S1T |
|---|---:|---:|---:|---:|---:|---:|
| Claude Opus 5.5 (max) | 0.00 (+0.00) | 0.00 (+0.00) | 1.23 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 0.96 (+0.00) |
| Claude Sonnet 5.5 (max) | 0.00 (+0.00) | 0.00 (+0.00) | 1.18 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 0.97 (+0.00) |
| GPT-6 Astra (max) | 0.00 (+0.00) | 0.00 (+0.00) | 1.28 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 0.96 (+0.00) |
| GPT-6 Luna (max) | 0.00 (+0.00) | 0.00 (+0.00) | 1.59 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 0.89 (+0.00) |
| GPT-6.1 Sol (max) | 0.00 (+0.00) | 0.00 (+0.00) | 1.28 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 0.96 (+0.00) |

Plan streams S1, S2, S1 endpoint-heavy, S1M and S1T run with owner assumptions off (owner-named transfers and O46 provider quota ceilings; E167): Claude Sonnet 5.5 (max) on Claude Max 20x, Claude Sonnet 5.5 (max) on Claude Max 5x, Claude Sonnet 5.5 (max) on Claude Pro, GPT-6 Luna (max) on ChatGPT Plus, GPT-6 Luna (max) on ChatGPT Pro 100, GPT-6 Luna (max) on ChatGPT Pro 200, GPT-6 Luna (max) on ChatGPT Pro 500 depend on an owner assumption and are unevaluable there (—), never reselected or replaced by API cost.

### Plan basis: rank 1

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M | S1T |
|---|---:|---:|---:|---:|---:|---:|
| Claude Opus 5.5 (max) on Claude Max 20x | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (max) on Claude Max 5x | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (max) on Claude Pro | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 83.5% |
| Claude Sonnet 5.5 (max) on Claude Max 20x | 0.0% | — | — | — | — | — |
| Claude Sonnet 5.5 (max) on Claude Max 5x | 0.0% | — | — | — | — | — |
| Claude Sonnet 5.5 (max) on Claude Pro | 0.0% | — | — | — | — | — |
| GPT-6 Astra (max) on ChatGPT Plus | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (max) on ChatGPT Pro 100 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (max) on ChatGPT Pro 200 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (max) on ChatGPT Pro 500 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Luna (max) on ChatGPT Plus | 0.0% | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 500 | 0.0% | — | — | — | — | — |
| GPT-6.1 Sol (max) on ChatGPT Plus | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (max) on ChatGPT Pro 100 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (max) on ChatGPT Pro 200 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (max) on ChatGPT Pro 500 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 16.5% |

### Plan basis: rank 3 or better

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M | S1T |
|---|---:|---:|---:|---:|---:|---:|
| Claude Opus 5.5 (max) on Claude Max 20x | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 84.6% |
| Claude Opus 5.5 (max) on Claude Max 5x | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 81.2% |
| Claude Opus 5.5 (max) on Claude Pro | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 85.0% |
| Claude Sonnet 5.5 (max) on Claude Max 20x | 0.0% | — | — | — | — | — |
| Claude Sonnet 5.5 (max) on Claude Max 5x | 0.0% | — | — | — | — | — |
| Claude Sonnet 5.5 (max) on Claude Pro | 0.0% | — | — | — | — | — |
| GPT-6 Astra (max) on ChatGPT Plus | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (max) on ChatGPT Pro 100 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (max) on ChatGPT Pro 200 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (max) on ChatGPT Pro 500 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Luna (max) on ChatGPT Plus | 0.0% | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 500 | 0.0% | — | — | — | — | — |
| GPT-6.1 Sol (max) on ChatGPT Plus | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 15.4% |
| GPT-6.1 Sol (max) on ChatGPT Pro 100 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 15.4% |
| GPT-6.1 Sol (max) on ChatGPT Pro 200 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (max) on ChatGPT Pro 500 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 18.9% |

### Plan basis: on the frontier

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M | S1T |
|---|---:|---:|---:|---:|---:|---:|
| Claude Opus 5.5 (max) on Claude Max 20x | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (max) on Claude Max 5x | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (max) on Claude Pro | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 97.8% |
| Claude Sonnet 5.5 (max) on Claude Max 20x | 0.0% | — | — | — | — | — |
| Claude Sonnet 5.5 (max) on Claude Max 5x | 0.0% | — | — | — | — | — |
| Claude Sonnet 5.5 (max) on Claude Pro | 0.0% | — | — | — | — | — |
| GPT-6 Astra (max) on ChatGPT Plus | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (max) on ChatGPT Pro 100 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (max) on ChatGPT Pro 200 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 10.7% |
| GPT-6 Astra (max) on ChatGPT Pro 500 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Luna (max) on ChatGPT Plus | 0.0% | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 500 | 100.0% | — | — | — | — | — |
| GPT-6.1 Sol (max) on ChatGPT Plus | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (max) on ChatGPT Pro 100 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (max) on ChatGPT Pro 200 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (max) on ChatGPT Pro 500 | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% |

### Plan basis: value-score dispersion (SD; covariance term)

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M | S1T |
|---|---:|---:|---:|---:|---:|---:|
| Claude Opus 5.5 (max) on Claude Max 20x | 0.00 (+0.00) | 0.00 (+0.00) | 1.24 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 0.96 (+0.00) |
| Claude Opus 5.5 (max) on Claude Max 5x | 0.00 (+0.00) | 0.00 (+0.00) | 1.24 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 0.96 (+0.00) |
| Claude Opus 5.5 (max) on Claude Pro | 0.00 (+0.00) | 0.00 (+0.00) | 1.24 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 0.96 (+0.00) |
| Claude Sonnet 5.5 (max) on Claude Max 20x | 0.00 (+0.00) | — | — | — | — | — |
| Claude Sonnet 5.5 (max) on Claude Max 5x | 0.00 (+0.00) | — | — | — | — | — |
| Claude Sonnet 5.5 (max) on Claude Pro | 0.00 (+0.00) | — | — | — | — | — |
| GPT-6 Astra (max) on ChatGPT Plus | 0.00 (+0.00) | 0.00 (+0.00) | 1.29 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 0.96 (+0.00) |
| GPT-6 Astra (max) on ChatGPT Pro 100 | 0.00 (+0.00) | 0.00 (+0.00) | 1.29 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 0.96 (+0.00) |
| GPT-6 Astra (max) on ChatGPT Pro 200 | 0.00 (+0.00) | 0.00 (+0.00) | 1.29 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 0.96 (+0.00) |
| GPT-6 Astra (max) on ChatGPT Pro 500 | 0.00 (+0.00) | 0.00 (+0.00) | 1.29 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 0.96 (+0.00) |
| GPT-6 Luna (max) on ChatGPT Plus | 0.00 (+0.00) | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 100 | 0.00 (+0.00) | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 200 | 0.00 (+0.00) | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 500 | 0.00 (+0.00) | — | — | — | — | — |
| GPT-6.1 Sol (max) on ChatGPT Plus | 0.00 (+0.00) | 0.00 (+0.00) | 1.29 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 0.97 (+0.00) |
| GPT-6.1 Sol (max) on ChatGPT Pro 100 | 0.00 (+0.00) | 0.00 (+0.00) | 1.29 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 0.97 (+0.00) |
| GPT-6.1 Sol (max) on ChatGPT Pro 200 | 0.00 (+0.00) | 0.00 (+0.00) | 1.29 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 0.97 (+0.00) |
| GPT-6.1 Sol (max) on ChatGPT Pro 500 | 0.00 (+0.00) | 0.00 (+0.00) | 1.29 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 0.97 (+0.00) |

### Named S2 specification branches

- **Bug Hunt harness band (E19)** (S2): unevaluable; the captured tbench.ai leaderboard lists no configuration under two or more agents, so no cross-agent spread exists
- **cache-hit variation (E34)** (S2): unevaluable; AA's published cost embeds its cache-pricing protocol; varying the cache-hit rate needs each basket component's cache-read and uncached-input demand, which AA publishes only for the whole Index (E157)
- **first-party list versus cross-provider median price rule (E122)** (S2): unevaluable; AA publishes one price per configuration under its own rule; the alternative rule's prices are not captured

### Cheapest-above-the-bar labels (API basis)

The 90% rule's error bound holds per published event (candidate and kernel assignment); it is not corrected across the listed candidates (E198). Each kernel assignment code gives the kernel used for the candidate and the competitors, in that order (U uniform, H endpoint-heavy; a quality-level bar has no reference rows, so it takes no letter); the label needs every assignment met.

| Bar | Candidate | Reading | Frequency range | Kernel assignments | Label |
|---|---|---|---|---|---|
| quality 65.2 | Claude Sonnet 5.5 (max) | not scenario-supported | 0.0% to 0.0% | UU not met, UH not met, HU not met, HH not met | no |
| quality 65.2 | GPT-6 Astra (max) | not scenario-supported | 49.4% to 50.6% | UU not met, UH not met, HU not met, HH not met | no |
| quality 63.7 | GPT-6.1 Sol (max) | not scenario-supported | 50.1% to 50.7% | UU not met, UH not met, HU not met, HH not met | no |
| quality 63.7 | GPT-6 Astra (max) | not scenario-supported | 49.3% to 49.6% | UU not met, UH not met, HU not met, HH not met | no |
| quality 66.2 | Claude Sonnet 5.5 (max) | not scenario-supported | 0.0% to 0.0% | UU not met, UH not met, HU not met, HH not met | no |

## Diagnostics

- **Terminal-Bench cross-source agreement (AA's mini-SWE-agent run against tbench.ai):** defined; 0 rows take the leaf from tbench.ai (gap fill).
- **Rank separability (O39, independent-task approximation):** median separation 2.60 value points (API) and 2.65 (Plan); separable adjacent ranks: API 1 of 4, Plan 1 of 5. Assumptions: tasks are independent and each leaf's score is a mean over its published task count (plug-in binomial with the proportion (k + 1/2) / (n + 1), I28); attempts averaged within a task and tasks shared across models are ignored, so the noise is approximate; GDPval-AA: each row's rating interval as AA's model page displays it, read as a 95% normal interval (AA states no level), SD = half-width / 1.96; AA-Omniscience: each of 6,000 questions scores +1, 0 or -1, with the shares from AA's accuracy and hallucination rate; Vals boards (Vibe Code Bench v1.1, Code Migration v1.1): Vals' published standard error per record, read as the leaf's SD; AI Coding Daily: judged points over its six graded projects read as a binomial share of 60 points (an assumption; the board publishes no error).
- **FrontierCode against Cognition:** FrontierCode cross-source agreement (AA against Cognition; E234): retired (O136): the leaf is AA's FrontierCode 2.0 and Cognition's board publishes FrontierCode 1.1, so no fill or comparison is made across the two versions; panel of 0 rows.
- **Gap-fill removal (E234, diagnostic):** no ranked row has a leaf from another party or the provider.
- **Bar results without the gap fills (E234, sensitivity; labels unchanged):** cheapest displayed row as published, with fills removed, and with third-party fills no measured offset — API quality 65.2: GPT-6 Astra (max) in all three; API quality 63.7: GPT-6.1 Sol (max) in all three; API quality 66.2: Claude Opus 5.5 (max) in all three; Plan quality 65.2: Claude Opus 5.5 (max) in all three; Plan quality 63.7: GPT-6.1 Sol (max) in all three; Plan quality 66.2: Claude Opus 5.5 (max) in all three.
- **Harness cost (O123, S2 stress):** unevaluable: no model is listed under two or more agents in AA's Coding Agent Index capture, so no agent effect is identified (O123). Coding Agent Index agents (each part of its costed configuration; none is the run behind the FrontierCode or Terminal-Bench leaf): GPT-6.1 Sol (max): Codex; Claude Opus 5.5 (max): Claude Code; Claude Sonnet 5.5 (max): Claude Code; GPT-6 Astra (max): Codex; GPT-6 Luna (max): Codex.
- **Quality agreement:** quality agreement (matched-panel sensitivity): Kendall tau 0.60 (interval -0.71 to 1.00) on 5 rows.
- **Quality-substitution value agreement (API):** quality-substitution value agreement, api basis (matched-panel sensitivity): Kendall tau 0.80 (interval 0.00 to 1.00) on 5 rows.
- **Quality-substitution value agreement (Plan):** quality-substitution value agreement, plan basis (matched-panel sensitivity): Kendall tau 0.60 (interval -0.71 to 1.00) on 5 rows.
- **Disjoint-evidence agreement:** disjoint-evidence agreement (restricted evidence comparison, not an eligible ranking): Kendall tau 0.60 (interval -0.71 to 1.00) on 5 rows.
- **Quality source shares:** AA-run 66%, independent 34%.
- **Non-discriminating leaves:** lcr.
- **Group drift:** estimated; flagged: knowledge.
- **Omniscience abstention sensitivity** (z_pen = max(0, I)): 2 rows move; largest move 2 (Claude Opus 5.5 (max), GPT-6 Luna (max)).
- **GDPval-AA logistic sensitivity** (z = 100 / (1 + 10^((1600 - E) / 400)) against AA's pinned anchor; every other input fixed): API 4 rows move; largest move 3 (GPT-6 Luna (max)); Plan no rank changes.
- **Anchor stability:** trimmed anchors (P10 / 2 and P90 x 2 (diagnostic only)) give $263.70 to $18,787.58; no rank changes.

- **Basket readiness (E22):** priced leaves cover 38% of nominal quality weight (AutomationBench-AA, FrontierCode 2.0, Terminal-Bench-Science 0.1, Terminal-Bench 4.0 (AA run)); pending components: ITBench-AA.
- **SWE cost companion (O14, diagnostic):** 5 rows evaluated; flagged far from the median ratio: none.
- **Matched-cost diagnostic (E55):** evaluated at 51% priced quality weight; basket/matched cost-order reversals with separated intervals: 1; rank-gap warnings: 0.
- **Frontier-families anchors (E187, diagnostic):** anchors rebuilt from the 4 frontier and near-frontier references move API no rank changes (value points per cost doubling 3.11 vs 3.11 frozen); Plan 2 rows move; largest move 1 (GPT-6 Astra (max), GPT-6 Luna (max)) (value points per cost doubling 3.57 vs 3.19 frozen).
- **Frontier-families bar (E199, sensitivity; the frozen bar stays primary):** quality 65.2 over 5 configurations; cheapest at or above it on the API main workload: not unique; possibly Claude Sonnet 5.5 (max), GPT-6 Astra (max) (compares 2 configurations that can qualify).
- **One row per family (E205, diagnostic; the frozen ladder and anchors stay primary):** with each family's primary configuration only (2 rows in the one-row-per-family bar population), the ladder (headline, lower quartile, upper quartile) would be 63.7 against 65.2 / 63.7 / 66.2 frozen; anchors rebuilt from its 2 references move API no rank changes (value points per cost doubling 5.08 vs 3.11 frozen); Plan 5 rows move; largest move 2 (GPT-6.1 Sol (max)) (value points per cost doubling 10.12 vs 3.19 frozen).
- **Ladder over scored rows (I28, sensitivity; the frozen ladder stays primary):** the bar population keeps full-benchmark rows that have no cost; today every such row has a cost, so the ladder is unchanged.
- **Bar currency (E207, informational):** rows reaching each frozen bar: quality 65.2: 3 of 5; quality 63.7: 4 of 5; quality 66.2: 2 of 5; the current population would freeze 65.2 / 63.7 / 66.2; lifetime until the next anchor re-freeze or methodology version, whichever comes first; no staleness flag.
- **Token mix (E208):** 5 selected routes: mix unidentified: the basket's token-category shares are set-identified only (E124), so the L1 test (above 0.30 flags mix-unmatched) is not computed.
- **Observed-range sensitivity (E219, not evidence; no label changes):** with each missing leaf inside the cohort's observed range for that leaf, quality 65.2: 2 can qualify, 1 confirmed; possibly cheapest Claude Sonnet 5.5 (max), GPT-6 Astra (max); quality 63.7: 3 can qualify, 2 confirmed; possibly cheapest GPT-6.1 Sol (max), GPT-6 Astra (max); quality 66.2: 1 can qualify, 0 confirmed; possibly cheapest Claude Sonnet 5.5 (max).
- **What would settle the headline bar (E221, not a claim):** rows that can but need not reach quality 65.2, with the mean score their missing leaves would need: GPT-6 Astra (max) (no missing leaf; reporting precision only).
- **Common leaf set (E226, diagnostic; scores unchanged):** without the leaves fewer than 90% of cohort rows have (none), API no rank changes; Plan no rank changes; rows reaching each bar: quality 65.2: 3 → 3; quality 63.7: 4 → 4; quality 66.2: 2 → 2; rows whose displayed quality differs from common-leaf quality by more than one cost doubling's worth: none.
- **Harness by leaf (E227):** Terminal-Bench: mini-SWE-agent 5; Bug Hunt: Codex CLI 3, Claude Code 2.
- **Coding Agent Index safety refusals (O63, flagged; costs and scores unchanged):** GPT-6.1 Sol (max) (15 blocked of 870 attempts); Claude Opus 5.5 (max) (76 finished by Claude Opus 4.8 or Claude Opus 5 of 870 attempts); Claude Sonnet 5.5 (45 finished by Claude Opus 4.8 of 870 attempts); GPT-6 Astra (max) (13 blocked of 870 attempts).

### Leave-one-component-out cost family (E172)

Each admitted basket unit removed in turn, scored on anchors rebuilt by the freeze rule (rank changes against the primary ranking; quality held fixed).

| Removed component | API rank changes | Plan rank changes | API value points per cost doubling |
|---|---|---|---:|
| Coding Agent Index | no rank changes | 2 rows move; largest move 1 (GPT-6 Astra (max), GPT-6 Luna (max)) | 3.14 |
| AA-Briefcase | 2 rows move; largest move 1 (Claude Opus 5.5 (max), GPT-6 Astra (max)) | 2 rows move; largest move 1 (GPT-6 Astra (max), GPT-6 Luna (max)) | 3.16 |
| GDP.pdf | no rank changes | 2 rows move; largest move 1 (GPT-6 Astra (max), GPT-6 Luna (max)) | 3.10 |
| AutomationBench-AA | no rank changes | 4 rows move; largest move 1 (Claude Sonnet 5.5 (max), GPT-6 Astra (max), GPT-6 Luna (max), GPT-6.1 Sol (max)) | 3.05 |
| Terminal-Bench 4.0 (AA Index run) | no rank changes | 2 rows move; largest move 1 (GPT-6 Astra (max), GPT-6 Luna (max)) | 3.10 |
| FrontierCode 2.0 | 2 rows move; largest move 1 (Claude Opus 5.5 (max), GPT-6 Astra (max)) | 2 rows move; largest move 1 (GPT-6 Astra (max), GPT-6 Luna (max)) | 3.11 |
| Terminal-Bench-Science | no rank changes | 2 rows move; largest move 1 (GPT-6 Astra (max), GPT-6 Luna (max)) | 3.07 |

### Subset rows: paired bridge and missing spend (E10, E173)

No row is scored on a subset workload.

### Deletion sensitivity

| Branch | Retained nominal weight | Status | API rank changes | Plan rank changes |
|---|---:|---|---|---|
| leave-out:frontierCode | 85% | evaluated | 2 rows move; largest move 1 (GPT-6 Astra (max), GPT-6 Luna (max)) | no rank changes |
| leave-out:terminalBench | 89% | evaluated | no rank changes | 4 rows move; largest move 1 (Claude Sonnet 5.5 (max), GPT-6 Astra (max), GPT-6 Luna (max), GPT-6.1 Sol (max)) |
| leave-out:bugHunt | 92% | evaluated | 2 rows move; largest move 1 (Claude Opus 5.5 (max), GPT-6 Astra (max)) | no rank changes |
| leave-out:vibeCode | 95% | evaluated | 3 rows move; largest move 2 (GPT-6 Luna (max)) | no rank changes |
| leave-out:codeMigration | 94% | evaluated | no rank changes | no rank changes |
| leave-out:livebench2Overall | 85% | evaluated | 2 rows move; largest move 1 (Claude Opus 5.5 (max), GPT-6 Astra (max)) | no rank changes |
| leave-out:gdpval | 90% | evaluated | 2 rows move; largest move 1 (GPT-6 Astra (max), GPT-6 Luna (max)) | 2 rows move; largest move 1 (Claude Sonnet 5.5 (max), GPT-6.1 Sol (max)) |
| leave-out:automationBench | 90% | evaluated | 3 rows move; largest move 2 (GPT-6 Luna (max)) | no rank changes |
| leave-out:omniscience | 90% | evaluated | no rank changes | no rank changes |
| leave-out:lcr | 95% | evaluated | 3 rows move; largest move 2 (GPT-6 Luna (max)) | no rank changes |
| leave-out:hle | 98% | evaluated | no rank changes | no rank changes |
| leave-out:tbScience | 98% | evaluated | no rank changes | no rank changes |
| leave-out:critpt | 98% | evaluated | no rank changes | no rank changes |
| leave-source-out:Artificial Analysis | 34% | not identifiable under the coverage rule | — | — |
| leave-source-out:Vals AI | 89% | evaluated | no rank changes | no rank changes |
| basket-scope | 87% | evaluated | no rank changes | 2 rows move; largest move 1 (GPT-6 Astra (max), GPT-6 Luna (max)) |

### Cost-component removal (Terminal-Bench 4.0 (AA Index run): evaluated)

| Basis | Run | Rank changes |
|---|---|---|
| api | cost-component removal, original anchors | no rank changes |
| api | alternative workload, recalibrated anchors | no rank changes |
| plan | cost-component removal, original anchors; fixed-multiple arithmetic stress (not identified Plan economics for the altered workload) | no rank changes |
| plan | alternative workload, recalibrated anchors; fixed-multiple arithmetic stress (not identified Plan economics for the altered workload) | 2 rows move; largest move 1 (GPT-6 Astra (max), GPT-6 Luna (max)) |

## Release gates

| Rule | Status | Detail |
|---|---|---|
| clip gate (E20) | passed | no basis exceeds the clipping allowance |
| cost influence flag (E91) | passed | cost not discriminating (< 10%); informational only; beta never changes (O2) |
| realised influence (E272) | fired | Plan: cost term offsetting (-37% of value variance); informational only, beta never changes (O2) |
| quality influence flag (E126) | passed | quality not discriminating (cost share > 90%); informational only |
| subset scoring (O17) | vacuous | subset rows scored on their own workload and anchors |
| partial component flag (E37) | fired | AA declined- or missing-task markers, or an Index reconstruction that misses AA's total (E209) |
| route dominance filter (E88) | vacuous | certifiably dearer routes set aside |
| Plan exploratory label (E61) | fired | fewer than half of Plan rows have an identified M_W |
| Plan evidence lifecycle and change detection (E18, E151, E269, O77, O79) | fired | 18 of 18 plan rows carry a possibly-superseded or expired route: claude-opus-5-5@claude-max-20x, claude-opus-5-5@claude-max-5x, claude-opus-5-5@claude-pro, claude-sonnet-5-5@claude-max-20x, claude-sonnet-5-5@claude-max-5x, claude-sonnet-5-5@claude-pro, gpt-6-astra@chatgpt-plus, gpt-6-astra@chatgpt-pro-100, gpt-6-astra@chatgpt-pro-200, gpt-6-astra@chatgpt-pro-500, gpt-6-luna@chatgpt-plus, gpt-6-luna@chatgpt-pro-100, gpt-6-luna@chatgpt-pro-200, gpt-6-luna@chatgpt-pro-500, gpt-6.1-sol@chatgpt-plus, gpt-6.1-sol@chatgpt-pro-100, gpt-6.1-sol@chatgpt-pro-200, gpt-6.1-sol@chatgpt-pro-500 |
| acknowledged accounting-fault windows (O91, O92, O93, O95, O96) | fired | 3 of 18 plan rows rest on a measurement inside an acknowledged fault window; they stay selected and yield to two concordant user reports for their own model and plan, and the transfers resting on them follow: gpt-6-astra@chatgpt-pro-500, gpt-6-luna@chatgpt-pro-500, gpt-6.1-sol@chatgpt-pro-500 |
| AA cost omits a pricing term (O94, O98, O100, O106, O108, O109, O114) | passed | no AA cost note names an omitted pricing term |
| valuation-basis gate (E170) | passed | every ranked row is compatible as captured or after evidenced revaluation |
| source clocks and evidence freshness (O59, O60, O65, E211, E216, E217, E218) | passed | every capture is within its age gate and none after the cutoff unless its source predates the cutoff's day; the build stops otherwise |
| build-stopping evidence gates (O64, O69, O71, O75, O99, O100, O101, O103, O105-O111, E195, E204, E225) | passed | the Coding Agent Index manifest (O64), the Terminal-Bench agent list (E225), cutoff-day row dates (O69), the three-stage all-provider plan search (O71, O75), the typed change records behind every route flag and partition split, which also produce each route's label and blocking dates within its launch- and schedule-bounded span (O99, O101, O105, O107, O110, O111), the register of AA notes covering every captured one, with the chart's inventory and duplicate-entry checks, the post-O103 capture notes, the basket-chart labels and chart-level notes' named rows (O100, O103, O106, O108) and the frontier path checks (E195, E204) hold; the build stops otherwise |
| score swing gate (E177) | vacuous | first v3 release: no previous v3 release to compare |
| anchor migration (E184) | vacuous | no main-workload migration deferred |
| configuration map coverage | passed | every cohort row has a configuration-map entry |
| quality clipping audit (E110) | passed | saturation disclosed; domain violations block the build |
| full benchmark set (O36, O38) | fired | listed, not ranked: gpt-6.1-terra, gpt-6.1-sol-high, gpt-6.1-sol-medium, gpt-6-astra-high, claude-opus-5-5-high, gpt-6.1-terra-xhigh, claude-haiku-5-5-high, gpt-6.1-sol-low, gpt-6.1-terra-high, gpt-6.1-terra-medium, claude-haiku-5-5-medium, gpt-6-luna-xhigh, gpt-6-luna-high, gpt-6-luna-medium, claude-haiku-5-5-low, claude-opus-5-5-xhigh, gpt-6-astra-xhigh, gpt-6-luna-low, gpt-6.1-sol-xhigh, gpt-6.1-terra-low, gemini-4-carbon, mimo-v2-6-flash |
| missing-leaf rules (O8 provisional, E198b, E201b, E219, E221, E226) | vacuous | no ranked row has a missing leaf (O36) |
| S1M interval stream (E145) | vacuous | dormant: no ranked leaf carries a published confidence interval since O37, so S1M equals S1 (E236) |
| provider-claim label denial (E233) | vacuous | no row has a provider-claimed leaf |
| scenario outputs current (E72) | passed | scenario input hash matches the scored inputs |
