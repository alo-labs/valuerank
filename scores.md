# ValueRank v3.0.0 Scores

**Updated:** October 19, 2026 · methodology 3.0.0 · SDLC basket v1 · anchor version `v3-2026-11-26-a4`

Value = 25% × cost score + 75% × quality. Costs are USD per basket run; the cost score is log-scaled against the frozen anchors of the row's workload (see [methodology.md](methodology.md)).

## Ranking

| Configuration | Plan rank | Plan value | Plan cost score | API rank | API value | API cost score | Quality | Quality coverage | Workload |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| [GPT-6.1 Sol (max)](https://valuerank.alolabs.dev/models/gpt-6-1-sol/) | 1 | 67.99 | 78.91 | 1 | 60.63 | 49.46 | 64.35 | 100% | main |
| [Claude Sonnet 5.5 (max)](https://valuerank.alolabs.dev/models/claude-sonnet-5-5/) | 5 | 65.59 | 70.61 | 4 | 51.40 | 13.86 | 63.92 | 100% | main |
| [Claude Opus 5.5 (max)](https://valuerank.alolabs.dev/models/claude-opus-5-5/) | 8 | 65.33 | 68.35 | 5 | 51.37 | 12.51 | 64.32 | 100% | main |
| [GPT-6 Astra (max)](https://valuerank.alolabs.dev/models/gpt-6-astra/) | 11 | 58.83 | 38.77 | 2 | 54.21 | 20.29 | 65.52 | 100% | main |
| [GPT-6 Luna (max)](https://valuerank.alolabs.dev/models/gpt-6-luna/) | 14 | 56.08 | 100.00 | 3 | 52.95 | 87.49 | 41.44 | 100% | main |

## Not ranked

| Model | Reasons |
|---|---|
| Claude Fable 5.2 (high) | Incomplete benchmark evidence after an exhaustive search (O36, O53): Max-effort ranking: no LiveBench 2.0 Overall; AI Coding Daily ranking: no AI Coding Daily (excl. bug finding) |
| Claude Fable 5.2 (max) | Incomplete benchmark evidence after an exhaustive search (O36, O53): Max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall; AI Coding Daily ranking: no AI Coding Daily (excl. bug finding) |
| Claude Fable 5.2 (xhigh) | Incomplete benchmark evidence after an exhaustive search (O36, O53): Max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals); AI Coding Daily ranking: no AI Coding Daily (excl. bug finding) |
| Claude Haiku 5.5 (high) | Not in the max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall; ranked in the AI Coding Daily ranking, common-leaf diagnostic ranking |
| Claude Haiku 5.5 (low) | Incomplete benchmark evidence after an exhaustive search (O36, O53): Max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall; AI Coding Daily ranking: no AI Coding Daily (excl. bug finding) |
| Claude Haiku 5.5 (medium) | Not in the max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall; ranked in the AI Coding Daily ranking, common-leaf diagnostic ranking |
| Claude Haiku 5.5 (xhigh) | Incomplete benchmark evidence after an exhaustive search (O36, O53): Max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall; AI Coding Daily ranking: no AI Coding Daily (excl. bug finding) |
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
| GPT-6.2 Astra (high) | Incomplete benchmark evidence after an exhaustive search (O36, O53): Max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall, GDPval-AA v2.1, AA-LCR v1.1; AI Coding Daily ranking: no GDPval-AA v2.1, AA-LCR v1.1 |
| GPT-6.2 Astra (max) | Incomplete benchmark evidence after an exhaustive search (O36, O53): Max-effort ranking: no Code Migration v1.1 (Vals), GDPval-AA v2.1, AA-LCR v1.1; AI Coding Daily ranking: no AI Coding Daily (excl. bug finding), GDPval-AA v2.1, AA-LCR v1.1 |
| GPT-6.2 Astra (medium) | Incomplete benchmark evidence after an exhaustive search (O36, O53): Max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall, GDPval-AA v2.1, AA-LCR v1.1; AI Coding Daily ranking: no GDPval-AA v2.1, AA-LCR v1.1 |
| GPT-6.2 Astra (xhigh) | Incomplete benchmark evidence after an exhaustive search (O36, O53): Max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall, GDPval-AA v2.1, AA-LCR v1.1; AI Coding Daily ranking: no AI Coding Daily (excl. bug finding), GDPval-AA v2.1, AA-LCR v1.1 |
| GPT-6.2 Sol (high) | Incomplete benchmark evidence after an exhaustive search (O36, O53): Max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall, GDPval-AA v2.1, AA-LCR v1.1; AI Coding Daily ranking: no GDPval-AA v2.1, AA-LCR v1.1 |
| GPT-6.2 Sol (low) | Incomplete benchmark evidence after an exhaustive search (O36, O53): Max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall, GDPval-AA v2.1, AA-LCR v1.1; AI Coding Daily ranking: no GDPval-AA v2.1, AA-LCR v1.1 |
| GPT-6.2 Sol (max) | Incomplete benchmark evidence after an exhaustive search (O36, O53): Max-effort ranking: no Code Migration v1.1 (Vals), GDPval-AA v2.1, AA-LCR v1.1; AI Coding Daily ranking: no AI Coding Daily (excl. bug finding), GDPval-AA v2.1, AA-LCR v1.1 |
| GPT-6.2 Sol (medium) | Incomplete benchmark evidence after an exhaustive search (O36, O53): Max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall, GDPval-AA v2.1, AA-LCR v1.1; AI Coding Daily ranking: no GDPval-AA v2.1, AA-LCR v1.1 |
| GPT-6.2 Sol (xhigh) | Incomplete benchmark evidence after an exhaustive search (O36, O53): Max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall, GDPval-AA v2.1, AA-LCR v1.1; AI Coding Daily ranking: no AI Coding Daily (excl. bug finding), GDPval-AA v2.1, AA-LCR v1.1 |
| Gemini 4 Carbon | Incomplete benchmark evidence after an exhaustive search (O36, O53): Max-effort ranking: no Code Migration v1.1 (Vals), AA-LCR v1.1; AI Coding Daily ranking: no AI Coding Daily (excl. bug finding), AA-LCR v1.1 |
| Gemini 4 Neon (high) | Incomplete benchmark evidence after an exhaustive search (O36, O53): Max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall, GDPval-AA v2.1, AA-LCR v1.1; AI Coding Daily ranking: no GDPval-AA v2.1, AA-LCR v1.1 |
| Gemini 4 Neon (medium) | Incomplete benchmark evidence after an exhaustive search (O36, O53): Max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall, GDPval-AA v2.1, AA-LCR v1.1; AI Coding Daily ranking: no GDPval-AA v2.1, AA-LCR v1.1 |
| Gemini 4 Neon (xhigh) | Incomplete benchmark evidence after an exhaustive search (O36, O53): Max-effort ranking: no Code Migration v1.1 (Vals), GDPval-AA v2.1, AA-LCR v1.1; AI Coding Daily ranking: no GDPval-AA v2.1, AA-LCR v1.1 |
| MiMo-V2.6-Flash | Incomplete benchmark evidence after an exhaustive search (O36, O53): Max-effort ranking: no Bug Hunt Bench, LiveBench 2.0 Overall; AI Coding Daily ranking: no Bug Hunt Bench |
| Muse Ember (max) | Incomplete benchmark evidence after an exhaustive search (O36, O53): Max-effort ranking: no Bug Hunt Bench, Code Migration v1.1 (Vals), LiveBench 2.0 Overall, GDPval-AA v2.1, AA-LCR v1.1; AI Coding Daily ranking: no Bug Hunt Bench, GDPval-AA v2.1, AA-LCR v1.1 |
| Muse Ember (xhigh) | Incomplete benchmark evidence after an exhaustive search (O36, O53): Max-effort ranking: no Bug Hunt Bench, Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall, GDPval-AA v2.1, AA-LCR v1.1; AI Coding Daily ranking: no Bug Hunt Bench, AI Coding Daily (excl. bug finding), GDPval-AA v2.1, AA-LCR v1.1 |

## Quality leaf scores

Each leaf's score z on its fixed 0–100 anchors; "—" marks a leaf with no eligible exact-configuration result.

| Configuration | FrontierCode 2.0 | Terminal-Bench 4.1 (AA run) | Bug Hunt Bench | Vibe Code Bench v1.1 (Vals) | Code Migration v1.1 (Vals) | LiveBench 2.0 Overall | GDPval-AA v2.1 | GDP.pdf (AA) | AutomationBench-AA | AA-Omniscience v1.1 | AA-LCR v1.1 | HLE-Diamond | Terminal-Bench-Science 0.1 | CritPt v2 (hard subset) | Quality | Provisional |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| GPT-6.1 Sol (max) | 40.6 | 56.6 | 78.7 | 75.1 | 77.3 | 81.2 | 55.4 | 31.0 | 64.9 | 71.0 | 83.0 | 58.8 | 58.1 | 69.5 | 64.35 | no |
| Claude Sonnet 5.5 (max) | 41.9 | 65.2 | 55.7 | 80.9 | 86.9 | 76.8 | 66.9 | 25.8 | 71.8 | 65.2 | 82.7 | 53.3 | 53.3 | 59.0 | 63.92 | no |
| Claude Opus 5.5 (max) | 46.9 | 59.1 | 36.4 | 78.5 | 81.0 | 83.4 | 68.3 | 26.2 | 69.5 | 74.1 | 84.7 | 67.9 | 59.0 | 68.0 | 64.32 | no |
| GPT-6 Astra (max) | 42.4 | 59.1 | 71.8 | 77.5 | 80.6 | 84.2 | 54.4 | 31.0 | 68.5 | 71.2 | 80.7 | 63.8 | 63.3 | 70.5 | 65.52 | no |
| GPT-6 Luna (max) | 25.2 | 12.6 | 29.5 | 65.3 | 46.7 | 60.4 | 47.2 | 22.8 | 53.2 | 45.9 | 83.3 | 22.2 | 8.6 | 42.5 | 41.44 | no |

## AI Coding Daily ranking

The configurations AI Coding Daily has tested, mostly at high and medium effort, scored on the AA leaves plus AI Coding Daily. Anchor version `v3-2026-11-26-a4-aicd`; leaves: FrontierCode 2.0 21%, Terminal-Bench 4.1 (AA run) 17%, Bug Hunt Bench 12%, AI Coding Daily (excl. bug finding) 10% (software engineering 60%), plus the 8 leaves outside software engineering every ranking shares.

| Configuration | Plan rank | Plan value | Plan cost score | API rank | API value | API cost score | Quality | Quality coverage | Workload |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| [GPT-6.1 Sol (high)](https://valuerank.alolabs.dev/models/gpt-6-1-sol-high/) | 1 | 58.65 | 63.94 | 1 | 53.16 | 41.98 | 56.88 | 100% | main |
| [GPT-6.1 Sol (medium)](https://valuerank.alolabs.dev/models/gpt-6-1-sol-medium/) | 5 | 58.07 | 72.14 | 3 | 52.04 | 48.01 | 53.38 | 100% | main |
| [Claude Opus 5.5 (high)](https://valuerank.alolabs.dev/models/claude-opus-5-5-high/) | 8 | 57.91 | 66.70 | 10 | 44.84 | 14.41 | 54.98 | 100% | main |
| [GPT-6.1 Terra (max)](https://valuerank.alolabs.dev/models/gpt-6-1-terra/) | 11 | 57.80 | 56.81 | 2 | 52.78 | 36.75 | 58.12 | 100% | main |
| [GPT-6.1 Terra (high)](https://valuerank.alolabs.dev/models/gpt-6-1-terra-high/) | 16 | 55.27 | 82.12 | 5 | 48.57 | 55.33 | 46.32 | 100% | main |
| [GPT-6.1 Terra (xhigh)](https://valuerank.alolabs.dev/models/gpt-6-1-terra-xhigh/) | 19 | 55.00 | 74.22 | 4 | 48.83 | 49.54 | 48.60 | 100% | main |
| [GPT-6.1 Terra (medium)](https://valuerank.alolabs.dev/models/gpt-6-1-terra-medium/) | 22 | 54.76 | 89.32 | 6 | 47.59 | 60.62 | 43.24 | 100% | main |
| [GPT-6.1 Sol (low)](https://valuerank.alolabs.dev/models/gpt-6-1-sol-low/) | 25 | 53.85 | 83.55 | 8 | 47.06 | 56.38 | 43.95 | 100% | main |
| [GPT-6 Luna (max)](https://valuerank.alolabs.dev/models/gpt-6-luna/) | 29 | 53.63 | 99.72 | 9 | 45.76 | 68.26 | 38.26 | 100% | main |
| [Claude Haiku 5.5 (high)](https://valuerank.alolabs.dev/models/claude-haiku-5-5-high/) | 35 | 52.12 | 100.00 | 11 | 44.39 | 69.06 | 36.17 | 100% | main |
| [GPT-6 Astra (high)](https://valuerank.alolabs.dev/models/gpt-6-astra-high/) | 39 | 51.65 | 30.25 | 7 | 47.10 | 12.08 | 58.78 | 100% | main |
| [GPT-6 Luna (xhigh)](https://valuerank.alolabs.dev/models/gpt-6-luna-xhigh/) | 42 | 49.74 | 100.00 | 12 | 43.51 | 75.06 | 32.99 | 100% | main |
| [Claude Haiku 5.5 (medium)](https://valuerank.alolabs.dev/models/claude-haiku-5-5-medium/) | 46 | 48.62 | 100.00 | 14 | 42.97 | 77.40 | 31.49 | 100% | main |
| [GPT-6 Luna (high)](https://valuerank.alolabs.dev/models/gpt-6-luna-high/) | 49 | 48.39 | 100.00 | 13 | 43.45 | 80.21 | 31.19 | 100% | main |
| [GPT-6 Luna (medium)](https://valuerank.alolabs.dev/models/gpt-6-luna-medium/) | 54 | 44.48 | 100.00 | 15 | 41.46 | 87.92 | 25.97 | 100% | main |

### AI Coding Daily ranking: quality leaf scores

| Configuration | FrontierCode 2.0 | Terminal-Bench 4.1 (AA run) | Bug Hunt Bench | AI Coding Daily (excl. bug finding) | GDPval-AA v2.1 | GDP.pdf (AA) | AutomationBench-AA | AA-Omniscience v1.1 | AA-LCR v1.1 | HLE-Diamond | Terminal-Bench-Science 0.1 | CritPt v2 (hard subset) | Quality | Provisional |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| GPT-6.1 Sol (high) | 36.7 | 51.0 | 55.0 | 93.5 | 51.1 | 32.0 | 64.5 | 70.5 | 82.3 | 51.9 | 46.2 | 68.5 | 56.88 | no |
| GPT-6.1 Sol (medium) | 33.4 | 48.0 | 42.7 | 92.4 | 48.2 | 30.0 | 62.6 | 70.1 | 83.3 | 46.0 | 37.1 | 67.0 | 53.38 | no |
| Claude Opus 5.5 (high) | 35.9 | 56.1 | 30.5 | 94.8 | 60.4 | 28.8 | 63.2 | 71.2 | 82.7 | 55.6 | 49.0 | 59.5 | 54.98 | no |
| GPT-6.1 Terra (max) | 42.1 | 56.6 | 63.7 | 86.5 | 48.7 | 28.6 | 60.2 | 64.8 | 82.7 | 47.3 | 57.6 | 68.0 | 58.12 | no |
| GPT-6.1 Terra (high) | 37.5 | 42.9 | 11.8 | 76.8 | 42.7 | 28.0 | 58.5 | 63.9 | 82.3 | 35.4 | 33.3 | 61.5 | 46.32 | no |
| GPT-6.1 Terra (xhigh) | 36.9 | 46.5 | 20.3 | 79.6 | 45.8 | 26.6 | 59.9 | 64.5 | 81.7 | 42.3 | 41.9 | 60.5 | 48.60 | no |
| GPT-6.1 Terra (medium) | 34.5 | 31.8 | 10.5 | 78.2 | 41.2 | 28.4 | 57.8 | 63.3 | 80.7 | 31.3 | 24.8 | 56.5 | 43.24 | no |
| GPT-6.1 Sol (low) | 20.2 | 30.8 | 33.4 | 88.5 | 41.1 | 27.0 | 52.6 | 69.0 | 84.0 | 38.2 | 11.0 | 62.5 | 43.95 | no |
| GPT-6 Luna (max) | 25.2 | 12.6 | 29.5 | 85.0 | 47.2 | 22.8 | 53.2 | 45.9 | 83.3 | 22.2 | 8.6 | 42.5 | 38.26 | no |
| Claude Haiku 5.5 (high) | 23.2 | 22.7 | 14.4 | 87.2 | 46.2 | 17.2 | 33.7 | 52.6 | 77.3 | 23.7 | 10.0 | 45.0 | 36.17 | no |
| GPT-6 Astra (high) | 40.1 | 54.5 | 53.9 | 94.0 | 51.9 | 31.0 | 66.6 | 72.3 | 80.0 | 59.3 | 59.5 | 71.5 | 58.78 | no |
| GPT-6 Luna (xhigh) | 18.4 | 8.1 | 18.7 | 82.4 | 43.7 | 18.6 | 47.8 | 43.5 | 80.0 | 18.9 | 5.2 | 37.0 | 32.99 | no |
| Claude Haiku 5.5 (medium) | 16.1 | 15.2 | 11.5 | 85.9 | 39.1 | 15.2 | 28.6 | 52.1 | 77.3 | 16.8 | 7.1 | 30.5 | 31.49 | no |
| GPT-6 Luna (high) | 18.6 | 5.1 | 12.9 | 79.1 | 42.5 | 18.2 | 47.8 | 43.6 | 79.3 | 15.6 | 2.9 | 31.0 | 31.19 | no |
| GPT-6 Luna (medium) | 12.8 | 2.5 | 2.9 | 68.8 | 38.5 | 13.8 | 40.5 | 43.2 | 78.3 | 15.1 | 1.4 | 27.5 | 25.97 | no |

### AI Coding Daily ranking: displayed record and noise

- API basis, displayed record (not a claim; E203): cheapest at or above quality 44.0: GPT-6.1 Sol (low) ($223.06 per basket run; 8 reach it); at or above quality 33.0: GPT-6 Luna (xhigh) ($76.38 per basket run; 12 reach it); at or above quality 53.4: GPT-6.1 Sol (medium) ($360.71 per basket run; 5 reach it).
- API basis, cheaper same-family efforts on AA's chart that this ranking could not evaluate (O143, E201c): below GPT-6 Luna (xhigh): GPT-6 Luna (low), GPT-6 Luna (non-reasoning).
- API basis, common-leaf diagnostic ranking at the same bar positions (O172; its own bar levels; no label by owner policy, O121, not for want of evidence; not a claim): cheapest at or above quality 48.2: GPT-6.1 Sol (medium); at or above quality 30.6: GPT-6.1 Terra (low); at or above quality 56.0: GPT-6.1 Sol (xhigh).
- API basis, pointwise noise-margin screen (O171; Δ = (Q − H)/√(σ² + σ_H²) at correlation 0 with the bar setter, 1.96 per comparison; separate comparisons, not a simultaneous confidence statement, E337): at or above quality 44.0: rounding-stable only (contested by GPT-6.1 Terra (medium)), 7 cheaper rows compared; at or above quality 33.0: rounding-stable only (contested by Claude Haiku 5.5 (medium), GPT-6 Luna (high)), 3 cheaper rows compared; at or above quality 53.4: rounding-stable only (contested by GPT-6.1 Terra (xhigh)), 10 cheaper rows compared.
- API basis, noise-margin companion (O44; each bar plus 5.5 quality points, so the bar's own configuration cannot decide it): cheapest at or above quality 49.4: GPT-6.1 Sol (medium) ($360.71 per basket run); at or above quality 38.5: GPT-6.1 Terra (medium) ($174.91 per basket run); at or above quality 58.9: none.
- Plan basis, displayed record (not a claim; E203): cheapest at or above quality 44.0: GPT-6.1 Sol (low) on ChatGPT Pro 500 ($20.71 per basket run; 31 reach it); at or above quality 33.0: Claude Haiku 5.5 (high) on Claude Pro ($1.83 per basket run; 49 reach it); at or above quality 53.4: GPT-6.1 Sol (medium) on ChatGPT Pro 500 ($33.49 per basket run; 19 reach it).
- Plan basis, cheaper same-family efforts on AA's chart that this ranking could not evaluate (O143, E201c): below Claude Haiku 5.5 (high): Claude Haiku 5.5 (low).
- Plan basis, common-leaf diagnostic ranking at the same bar positions (O172; its own bar levels; no label by owner policy, O121, not for want of evidence; not a claim): cheapest at or above quality 48.2: GPT-6.1 Sol (medium) on ChatGPT Pro 500; at or above quality 30.6: Claude Haiku 5.5 (xhigh) on Claude Pro; at or above quality 56.0: GPT-6.1 Sol (xhigh) on ChatGPT Pro 500.
- Plan basis, pointwise noise-margin screen (O171; Δ = (Q − H)/√(σ² + σ_H²) at correlation 0 with the bar setter, 1.96 per comparison; separate comparisons, not a simultaneous confidence statement, E337): at or above quality 44.0: rounding-stable only (contested by GPT-6.1 Terra (medium) on ChatGPT Pro 100, GPT-6.1 Terra (medium) on ChatGPT Pro 200, GPT-6.1 Terra (medium) on ChatGPT Pro 500), 25 cheaper rows compared; at or above quality 33.0: rounding-stable only (contested by Claude Haiku 5.5 (medium) on Claude Max 20x, Claude Haiku 5.5 (medium) on Claude Max 5x, Claude Haiku 5.5 (medium) on Claude Pro), 3 cheaper rows compared; at or above quality 53.4: rounding-stable only (contested by GPT-6.1 Terra (xhigh) on ChatGPT Pro 100, GPT-6.1 Terra (xhigh) on ChatGPT Pro 200, GPT-6.1 Terra (xhigh) on ChatGPT Pro 500), 38 cheaper rows compared.
- Plan basis, noise-margin companion (O44; each bar plus 5.5 quality points, so the bar's own configuration cannot decide it): cheapest at or above quality 49.4: GPT-6.1 Sol (medium) on ChatGPT Pro 500 ($33.49 per basket run); at or above quality 38.5: GPT-6.1 Terra (medium) on ChatGPT Pro 500 ($16.24 per basket run); at or above quality 58.9: none.
- AA cost caveat (O94; ranked at the published cost, no label of its own) on these bars' cheapest rows: Claude Haiku 5.5 (high) (AA's cost omits a pricing term; up to 5× on its cost).
- Plan route flags on these bars' cheapest plan rows: Claude Haiku 5.5 (high) on Claude Pro (possibly-superseded); GPT-6.1 Sol (low) on ChatGPT Pro 500 (possibly-superseded, measured inside an acknowledged accounting-fault window (O91, O92)); GPT-6.1 Sol (medium) on ChatGPT Pro 500 (possibly-superseded, measured inside an acknowledged accounting-fault window (O91, O92)); GPT-6.1 Terra (medium) on ChatGPT Pro 500 (possibly-superseded, measured inside an acknowledged accounting-fault window (O91, O92)).
- These outputs compare ranked configurations only; listed families shown with an indicative value (O41) are outside them (O43): GPT-6.1 Sol (max), Claude Opus 5.5 (max), GPT-6 Astra (max), Claude Sonnet 5.5, Claude Fable 5.2 (high), Claude Fable 5.2 (max), Claude Fable 5.2 (xhigh), Claude Haiku 5.5 (low), Claude Haiku 5.5 (xhigh), Claude Opus 5.5 (xhigh), GPT-6 Astra (xhigh), GPT-6 Luna (low), GPT-6.1 Sol (xhigh), GPT-6.1 Terra (low), GPT-6.2 Astra (high), GPT-6.2 Astra (max), GPT-6.2 Astra (medium), GPT-6.2 Astra (xhigh), GPT-6.2 Sol (high), GPT-6.2 Sol (low), GPT-6.2 Sol (max), GPT-6.2 Sol (medium), GPT-6.2 Sol (xhigh), Gemini 4 Carbon, Gemini 4 Neon (high), Gemini 4 Neon (medium), Gemini 4 Neon (xhigh), MiMo-V2.6-Flash, Muse Ember (max), Muse Ember (xhigh).

Benchmark sampling noise (O39, an independent-task approximation): two values must differ by about 4.1 value points (median, 95%) to separate, and 0 of 14 adjacent API ranks and 0 of 29 adjacent Plan ranks of different configurations do (33 more adjacent Plan pairs are one configuration on two plans, ordered by the plans' multiples alone; E258). Its net direction is not established: every configuration is scored on the same tasks, which correlates their errors and narrows the true threshold (API 0 at correlation 0.3, 1 at correlation 0.6; Plan 1 at correlation 0.3, 1 at correlation 0.6), while sources it leaves out widen it (run-to-run and harness variance, AA's single cost run and, for the 44 Plan rows on an owner assumption (38 owner-named transfers and 6 O198 published dollar limits), that assumption's error). The noise band column groups each row with the band's first row it cannot be told apart from (O42); a Plan band marked † rests on an owner assumption (an owner-named transfer, an O46 provider quota ceiling or an O198 published dollar limit) and excludes its error: an assumed multiple can be wrong by a factor of about 2.0 before the row's value moves by the median threshold (a tolerance, not an estimate of the assumption's error). The S1T scenario shares in [scores.md](scores.md) show each row's rank-1 and top-3 frequencies under that noise. AI Coding Daily's noise treats its seven graded projects as seven trials of the share of 80 points (n = 7, the wide reading, E263); read as 80 trials, the median threshold would be 3.1 (API) and 3.0 (Plan), with 0 and 2 adjacent ranks separable.


**Listed frontier families: indicative value, not ranked and not comparable (O41).** Quality is the mean over the leaves the configuration has, renormalised, with no imputation, so these values cannot be compared with the ranking above.

| Configuration | Missing | Quality (remaining leaves) | Quality coverage | Plan value (indicative) | API value (indicative) | API cost (USD per basket run) | Plan cost (USD per basket run) |
|---|---|---:|---:|---:|---:|---:|---:|
| GPT-6.1 Sol (max) | AI Coding Daily (excl. bug finding) | 58.6 | 90% | 56.3 | 51.7 | $950.68 | $88.25 |
| Claude Opus 5.5 (max) | AI Coding Daily (excl. bug finding) | 56.5 | 90% | 52.8 | 42.4 | $7,048.37 | $119.67 |
| GPT-6 Astra (max) | AI Coding Daily (excl. bug finding) | 59.0 | 90% | 48.8 | 45.0 | $4,767.90 | $329.16 |
| Claude Sonnet 5.5 | AI Coding Daily (excl. bug finding) | 57.6 | 90% | 54.0 | 43.2 | $6,644.38 | $112.81 |
| Claude Fable 5.2 (high) | AI Coding Daily (excl. bug finding) | 58.8 | 90% | 44.1 | 44.1 | $6,545.30 | $6,545.30 |
| Claude Fable 5.2 (max) | AI Coding Daily (excl. bug finding) | 62.6 | 90% | 47.0 | 47.0 | $19,550.04 | $19,550.04 |
| Claude Fable 5.2 (xhigh) | AI Coding Daily (excl. bug finding) | 59.7 | 90% | 44.8 | 44.8 | $10,674.12 | $10,674.12 |
| Claude Haiku 5.5 (low) | AI Coding Daily (excl. bug finding) | 20.8 | 90% | 40.6 | 37.5 | $36.79 | $0.62 |
| Claude Haiku 5.5 (xhigh) | AI Coding Daily (excl. bug finding) | 34.8 | 90% | 51.1 | 41.5 | $164.01 | $2.78 |
| Claude Opus 5.5 (xhigh) | AI Coding Daily (excl. bug finding) | 54.9 | 90% | 54.7 | 42.5 | $4,214.23 | $71.55 |
| GPT-6 Astra (xhigh) | AI Coding Daily (excl. bug finding) | 58.3 | 90% | 50.6 | 46.3 | $3,186.48 | $219.99 |
| GPT-6 Luna (low) | AI Coding Daily (excl. bug finding) | 14.1 | 90% | 35.6 | 35.6 | $7.95 | $0.74 |
| GPT-6.1 Sol (xhigh) | AI Coding Daily (excl. bug finding) | 56.3 | 90% | 57.1 | 51.9 | $617.20 | $57.30 |
| GPT-6.1 Terra (low) | AI Coding Daily (excl. bug finding) | 32.1 | 90% | 49.1 | 41.5 | $104.95 | $9.74 |
| GPT-6.2 Astra (high) | GDPval-AA v2.1, AA-LCR v1.1 | 68.5 | 90% | 51.4 | 56.4 | $1,768.79 | $1,768.79 |
| GPT-6.2 Astra (max) | AI Coding Daily (excl. bug finding), GDPval-AA v2.1, AA-LCR v1.1 | 64.4 | 80% | 48.3 | 51.0 | $3,055.74 | $3,055.74 |
| GPT-6.2 Astra (medium) | GDPval-AA v2.1, AA-LCR v1.1 | 64.8 | 90% | 48.6 | 54.7 | $1,385.56 | $1,385.56 |
| GPT-6.2 Astra (xhigh) | AI Coding Daily (excl. bug finding), GDPval-AA v2.1, AA-LCR v1.1 | 66.2 | 80% | 49.6 | 54.0 | $2,085.11 | $2,085.11 |
| GPT-6.2 Sol (high) | GDPval-AA v2.1, AA-LCR v1.1 | 61.0 | 90% | 48.0 | 56.5 | $484.85 | $484.85 |
| GPT-6.2 Sol (low) | GDPval-AA v2.1, AA-LCR v1.1 | 49.0 | 90% | 43.7 | 50.9 | $216.88 | $216.88 |
| GPT-6.2 Sol (max) | AI Coding Daily (excl. bug finding), GDPval-AA v2.1, AA-LCR v1.1 | 60.0 | 80% | 45.0 | 53.6 | $788.34 | $788.34 |
| GPT-6.2 Sol (medium) | GDPval-AA v2.1, AA-LCR v1.1 | 59.4 | 90% | 48.2 | 56.4 | $376.68 | $376.68 |
| GPT-6.2 Sol (xhigh) | AI Coding Daily (excl. bug finding), GDPval-AA v2.1, AA-LCR v1.1 | 57.1 | 80% | 44.2 | 52.9 | $555.09 | $555.09 |
| Gemini 4 Carbon | AI Coding Daily (excl. bug finding), AA-LCR v1.1 | 59.1 | 85% | 44.3 | 44.3 | $5,716.87 | $5,716.87 |
| Gemini 4 Neon (high) | GDPval-AA v2.1, AA-LCR v1.1 | 63.4 | 90% | 47.6 | 50.8 | $2,729.37 | $2,729.37 |
| Gemini 4 Neon (medium) | GDPval-AA v2.1, AA-LCR v1.1 | 57.4 | 90% | 43.1 | 48.9 | $1,487.26 | $1,487.26 |
| Gemini 4 Neon (xhigh) | GDPval-AA v2.1, AA-LCR v1.1 | 65.0 | 90% | 48.7 | 49.7 | $4,519.00 | $4,519.00 |
| MiMo-V2.6-Flash | Bug Hunt Bench | 39.4 | 88% | 43.0 | 47.9 | $82.84 | $72.16 |
| Muse Ember (max) | Bug Hunt Bench, GDPval-AA v2.1, AA-LCR v1.1 | 45.1 | 78% | 46.3 | 52.1 | $86.22 | $86.22 |
| Muse Ember (xhigh) | Bug Hunt Bench, AI Coding Daily (excl. bug finding), GDPval-AA v2.1, AA-LCR v1.1 | 37.1 | 68% | 41.1 | 46.7 | $74.03 | $74.03 |

### AI Coding Daily ranking: Plan routes and calibration

#### Measured-evidence calibration (diagnostic)

References: each workload's measured-only rows with complete cost evidence are the references: c_L = cheapest / 2, c_H = dearest x 2 (diagnostic only; the official anchors are unchanged). Status: evaluated.

- Workload `9c122a3ecb672aae`: measured anchors $10.35 to $391.32 from Claude Opus 5.5 (high), GPT-6 Astra (high), GPT-6.1 Sol (high), GPT-6.1 Sol (low), GPT-6.1 Sol (medium); anchor ratio 37.8 against the official 67.6. Official Plan anchors are set by GPT-6.1 Sol (low) on ChatGPT Pro 500 (same-model measurement from another effort) at the low end and GPT-6 Astra (high) on ChatGPT Plus (same-model measurement from another effort) at the high end.

| Configuration | Value on official Plan anchors | Value on measured anchors | Rank change |
|---|---:|---:|---:|
| Claude Opus 5.5 (high) ‡ | 57.91 | 56.58 | 0 |
| GPT-6 Astra (high) ‡ | 51.65 | 48.86 | 0 |
| GPT-6.1 Sol (high) ‡ | 58.65 | 57.20 | 0 |
| GPT-6.1 Sol (low) ‡ | 53.85 | 53.19 | 0 |
| GPT-6.1 Sol (medium) ‡ | 58.07 | 56.96 | 0 |

Pairwise reversals: none. Largest value change: 2.79 points.

‡ measured on the same model at another effort (an O88 route; measured evidence under O90).

### AI Coding Daily ranking: interval outputs

**API basis, main workload: frontier.** Not evaluable: none. Competing without a label of its own (E183): Claude Haiku 5.5 (high): AA's cost omits a pricing term (O94); competes over its published cost up to the stated factor; Claude Haiku 5.5 (medium): AA's cost omits a pricing term (O94); competes over its published cost up to the stated factor.

| Configuration | Possible frontier | Definite frontier | Definite counterexample | Possible frontier blocked by |
|---|---|---|---|---|
| GPT-6.1 Sol (high) | certified | certified | — | — |
| GPT-6.1 Terra (max) | certified | certified | — | — |
| GPT-6.1 Sol (medium) | certified | certified | — | — |
| GPT-6 Astra (high) | certified | certified | — | — |
| Claude Opus 5.5 (high) | disproved | disproved | GPT-6.1 Sol (high) | GPT-6.1 Sol (high), GPT-6.1 Terra (max) |
| GPT-6.1 Sol (low) | certified | certified | — | — |
| GPT-6.1 Terra (xhigh) | certified | certified | — | — |
| GPT-6.1 Terra (high) | certified | certified | — | — |
| GPT-6 Luna (max) | certified | certified | — | — |
| GPT-6.1 Terra (medium) | certified | certified | — | — |
| GPT-6 Luna (xhigh) | certified | certified | — | — |
| GPT-6 Luna (high) | certified | certified | — | — |
| GPT-6 Luna (medium) | certified | certified | — | — | These labels carry the workload cross-check warning (E41, O160, O183: cost per solved task, τ_b 0.12 on 15 configurations, low agreement): the basket-cost order behind them agrees weakly with cost per solved task; the attribution is in scores.json `diagnostics.workloadCrossCheck.attribution`.

**API basis, main workload: cheapest at or above quality 44.0** (lower-median displayed quality of the non-provisional cohort configurations at freeze (E192; headline bar)). Status certified; confirmed cheapest: none.

Configurations that can be confirmed to qualify: 7 (confirmation needs the full-composite lower bound, with missing leaves at 0, to clear the bar; O25). Cheaper same-family configurations on AA's chart that were not evaluated (not ranked in this ranking: lacking its full benchmark set, or not plotted on or near the frontier; E201c, O51): GPT-6.1 Terra (high): GPT-6.1 Terra (non-reasoning), GPT-6.1 Terra (low).

Bar comparison: compares 8 configurations that can qualify. The bar is a displayed-quality level; qualification tests each row's full-composite bounds, so a row above the bar on displayed quality can still fail to qualify confirmed when leaves are missing (E198).

| Configuration | Displayed quality − bar | Confirmed qualifies | Possibly qualifies | Possibly cheapest |
|---|---:|---|---|---|
| GPT-6.1 Sol (high) | 12.9 | certified | certified | disproved |
| GPT-6.1 Terra (max) | 14.2 | certified | certified | disproved |
| GPT-6.1 Sol (medium) | 9.4 | certified | certified | disproved |
| GPT-6 Astra (high) | 14.8 | certified | certified | disproved |
| Claude Opus 5.5 (high) | 11.0 | certified | certified | disproved |
| GPT-6.1 Sol (low) | 0.0 | disproved | certified | certified |
| GPT-6.1 Terra (xhigh) | 4.6 | certified | certified | disproved |
| GPT-6.1 Terra (high) | 2.4 | certified | certified | certified |
| GPT-6 Luna (max) | -5.7 | disproved | disproved | disproved |
| GPT-6.1 Terra (medium) | -0.7 | disproved | disproved | disproved |
| GPT-6 Luna (xhigh) | -11.0 | disproved | disproved | disproved |
| GPT-6 Luna (high) | -12.8 | disproved | disproved | disproved |
| GPT-6 Luna (medium) | -18.0 | disproved | disproved | disproved |

**API basis, main workload: cheapest at or above quality 33.0** (lower-quartile displayed quality of the non-provisional cohort configurations at freeze (O34)). Status certified; confirmed cheapest: none.

Configurations that can be confirmed to qualify: 10 (confirmation needs the full-composite lower bound, with missing leaves at 0, to clear the bar; O25). Cheaper same-family configurations on AA's chart that were not evaluated (not ranked in this ranking: lacking its full benchmark set, or not plotted on or near the frontier; E201c, O51): GPT-6 Luna (max): GPT-6 Luna (low), GPT-6 Luna (non-reasoning); GPT-6 Luna (xhigh): GPT-6 Luna (low), GPT-6 Luna (non-reasoning).

Bar comparison: compares 11 configurations that can qualify and 1 blocker(s) that can qualify but earn no label (E315). The bar is a displayed-quality level; qualification tests each row's full-composite bounds, so a row above the bar on displayed quality can still fail to qualify confirmed when leaves are missing (E198).

| Configuration | Displayed quality − bar | Confirmed qualifies | Possibly qualifies | Possibly cheapest |
|---|---:|---|---|---|
| GPT-6.1 Sol (high) | 23.9 | certified | certified | disproved |
| GPT-6.1 Terra (max) | 25.1 | certified | certified | disproved |
| GPT-6.1 Sol (medium) | 20.4 | certified | certified | disproved |
| GPT-6 Astra (high) | 25.8 | certified | certified | disproved |
| Claude Opus 5.5 (high) | 22.0 | certified | certified | disproved |
| GPT-6.1 Sol (low) | 11.0 | certified | certified | disproved |
| GPT-6.1 Terra (xhigh) | 15.6 | certified | certified | disproved |
| GPT-6.1 Terra (high) | 13.3 | certified | certified | disproved |
| GPT-6 Luna (max) | 5.3 | certified | certified | certified |
| GPT-6.1 Terra (medium) | 10.3 | certified | certified | disproved |
| GPT-6 Luna (xhigh) | 0.0 | disproved | certified | certified |
| GPT-6 Luna (high) | -1.8 | disproved | disproved | disproved |
| GPT-6 Luna (medium) | -7.0 | disproved | disproved | disproved |

**API basis, main workload: cheapest at or above quality 53.4** (upper-quartile displayed quality of the non-provisional cohort configurations at freeze (O34)). Status certified; confirmed cheapest: none.

Configurations that can be confirmed to qualify: 4 (confirmation needs the full-composite lower bound, with missing leaves at 0, to clear the bar; O25). Cheaper same-family configurations on AA's chart that were not evaluated (not ranked in this ranking: lacking its full benchmark set, or not plotted on or near the frontier; E201c, O51): none.

Bar comparison: compares 5 configurations that can qualify. The bar is a displayed-quality level; qualification tests each row's full-composite bounds, so a row above the bar on displayed quality can still fail to qualify confirmed when leaves are missing (E198).

| Configuration | Displayed quality − bar | Confirmed qualifies | Possibly qualifies | Possibly cheapest |
|---|---:|---|---|---|
| GPT-6.1 Sol (high) | 3.5 | certified | certified | certified |
| GPT-6.1 Terra (max) | 4.7 | certified | certified | disproved |
| GPT-6.1 Sol (medium) | 0.0 | disproved | certified | certified |
| GPT-6 Astra (high) | 5.4 | certified | certified | disproved |
| Claude Opus 5.5 (high) | 1.6 | certified | certified | disproved |
| GPT-6.1 Sol (low) | -9.4 | disproved | disproved | disproved |
| GPT-6.1 Terra (xhigh) | -4.8 | disproved | disproved | disproved |
| GPT-6.1 Terra (high) | -7.1 | disproved | disproved | disproved |
| GPT-6 Luna (max) | -15.1 | disproved | disproved | disproved |
| GPT-6.1 Terra (medium) | -10.1 | disproved | disproved | disproved |
| GPT-6 Luna (xhigh) | -20.4 | disproved | disproved | disproved |
| GPT-6 Luna (high) | -22.2 | disproved | disproved | disproved |
| GPT-6 Luna (medium) | -27.4 | disproved | disproved | disproved |

**Plan basis, main workload:** not evaluated (no row has FullCost and an identified M_W (E61/E67)).

### AI Coding Daily ranking: scenario shares

The scenario panel is the 15 rows scored on the main workload (E96, E266).

Frequencies over 10,000 scenarios per run (seed 20261126); streams are defined in [methodology.md](methodology.md#uncertainty-outputs). S1T adds benchmark sampling noise under an independent-task approximation (O39); the other streams exclude it, and every stream excludes correlated-task, harness and attempt effects (E155).

### API basis: rank 1

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M | S1T | S1T recentred |
|---|---:|---:|---:|---:|---:|---:|---:|
| Claude Haiku 5.5 (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Haiku 5.5 (medium) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Luna (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Luna (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Luna (medium) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Luna (xhigh) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (high) | 100.0% | 100.0% | 81.4% | 100.0% | 100.0% | 46.9% | 45.6% |
| GPT-6.1 Sol (low) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (medium) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 16.4% | 17.0% |
| GPT-6.1 Terra (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.1% | 0.1% |
| GPT-6.1 Terra (max) | 0.0% | 0.0% | 18.6% | 0.0% | 0.0% | 36.3% | 37.0% |
| GPT-6.1 Terra (medium) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Terra (xhigh) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.2% | 0.2% |

### API basis: rank 3 or better

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M | S1T | S1T recentred |
|---|---:|---:|---:|---:|---:|---:|---:|
| Claude Haiku 5.5 (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Haiku 5.5 (medium) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.4% | 0.5% |
| GPT-6 Luna (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Luna (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Luna (medium) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Luna (xhigh) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (high) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 97.0% | 97.2% |
| GPT-6.1 Sol (low) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.4% | 0.3% |
| GPT-6.1 Sol (medium) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 88.9% | 90.4% |
| GPT-6.1 Terra (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 7.2% | 6.3% |
| GPT-6.1 Terra (max) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 94.8% | 95.4% |
| GPT-6.1 Terra (medium) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 1.7% | 1.3% |
| GPT-6.1 Terra (xhigh) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 9.6% | 8.6% |

### API basis: on the frontier

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M | S1T | S1T recentred |
|---|---:|---:|---:|---:|---:|---:|---:|
| Claude Haiku 5.5 (high) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 87.5% | 88.4% |
| Claude Haiku 5.5 (medium) | 100.0% | 100.0% | 64.7% | 100.0% | 100.0% | 53.1% | 55.5% |
| Claude Opus 5.5 (high) | 0.0% | 0.0% | 0.1% | 0.0% | 0.0% | 5.6% | 5.3% |
| GPT-6 Astra (high) | 100.0% | 100.0% | 87.6% | 100.0% | 100.0% | 49.7% | 50.2% |
| GPT-6 Luna (high) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 97.7% | 98.4% |
| GPT-6 Luna (max) | 100.0% | 100.0% | 99.0% | 100.0% | 100.0% | 79.7% | 79.7% |
| GPT-6 Luna (medium) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% |
| GPT-6 Luna (xhigh) | 100.0% | 100.0% | 97.9% | 100.0% | 100.0% | 63.3% | 64.0% |
| GPT-6.1 Sol (high) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 90.4% | 90.2% |
| GPT-6.1 Sol (low) | 100.0% | 100.0% | 71.5% | 100.0% | 100.0% | 58.3% | 59.8% |
| GPT-6.1 Sol (medium) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 94.2% | 95.2% |
| GPT-6.1 Terra (high) | 100.0% | 100.0% | 95.4% | 100.0% | 100.0% | 74.6% | 74.1% |
| GPT-6.1 Terra (max) | 100.0% | 100.0% | 98.1% | 100.0% | 100.0% | 68.1% | 69.2% |
| GPT-6.1 Terra (medium) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 96.6% | 96.7% |
| GPT-6.1 Terra (xhigh) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 75.4% | 76.8% |

### API basis: value-score dispersion (SD; covariance term)

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M | S1T | S1T recentred |
|---|---:|---:|---:|---:|---:|---:|---:|
| Claude Haiku 5.5 (high) | 0.00 (+0.00) | 0.00 (+0.00) | 1.72 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.33 (+0.00) | 1.34 (+0.00) |
| Claude Haiku 5.5 (medium) | 0.00 (+0.00) | 0.00 (+0.00) | 1.85 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.27 (+0.00) | 1.26 (+0.00) |
| Claude Opus 5.5 (high) | 0.00 (+0.00) | 0.00 (+0.00) | 1.55 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.37 (+0.00) | 1.32 (+0.00) |
| GPT-6 Astra (high) | 0.00 (+0.00) | 0.00 (+0.00) | 1.29 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.43 (+0.00) | 1.40 (+0.00) |
| GPT-6 Luna (high) | 0.00 (+0.00) | 0.00 (+0.00) | 1.79 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.32 (+0.00) | 1.31 (+0.00) |
| GPT-6 Luna (max) | 0.00 (+0.00) | 0.00 (+0.00) | 1.68 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.35 (+0.00) | 1.36 (+0.00) |
| GPT-6 Luna (medium) | 0.00 (+0.00) | 0.00 (+0.00) | 1.75 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.33 (+0.00) | 1.32 (+0.00) |
| GPT-6 Luna (xhigh) | 0.00 (+0.00) | 0.00 (+0.00) | 1.78 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.31 (+0.00) | 1.30 (+0.00) |
| GPT-6.1 Sol (high) | 0.00 (+0.00) | 0.00 (+0.00) | 1.34 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.41 (+0.00) | 1.38 (+0.00) |
| GPT-6.1 Sol (low) | 0.00 (+0.00) | 0.00 (+0.00) | 1.73 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.39 (+0.00) | 1.37 (+0.00) |
| GPT-6.1 Sol (medium) | 0.00 (+0.00) | 0.00 (+0.00) | 1.44 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.42 (+0.00) | 1.38 (+0.00) |
| GPT-6.1 Terra (high) | 0.00 (+0.00) | 0.00 (+0.00) | 1.46 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.54 (+0.00) | 1.56 (+0.00) |
| GPT-6.1 Terra (max) | 0.00 (+0.00) | 0.00 (+0.00) | 1.10 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.53 (+0.00) | 1.50 (+0.00) |
| GPT-6.1 Terra (medium) | 0.00 (+0.00) | 0.00 (+0.00) | 1.55 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.50 (+0.00) | 1.49 (+0.00) |
| GPT-6.1 Terra (xhigh) | 0.00 (+0.00) | 0.00 (+0.00) | 1.37 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.55 (+0.00) | 1.54 (+0.00) |

Plan streams S1, S2, S1 endpoint-heavy, S1M, S1T and S1T recentred run with owner assumptions off (owner-named transfers, O46 provider quota ceilings and O198 published dollar limits; E167): Claude Haiku 5.5 (high) on Claude Max 20x, Claude Haiku 5.5 (high) on Claude Max 5x, Claude Haiku 5.5 (high) on Claude Pro, Claude Haiku 5.5 (high) on OpenCode Go, Claude Haiku 5.5 (medium) on Claude Max 20x, Claude Haiku 5.5 (medium) on Claude Max 5x, Claude Haiku 5.5 (medium) on Claude Pro, Claude Haiku 5.5 (medium) on OpenCode Go, GPT-6 Luna (high) on ChatGPT Plus, GPT-6 Luna (high) on ChatGPT Pro 100, GPT-6 Luna (high) on ChatGPT Pro 200, GPT-6 Luna (high) on ChatGPT Pro 500, GPT-6 Luna (high) on OpenCode Go, GPT-6 Luna (max) on ChatGPT Plus, GPT-6 Luna (max) on ChatGPT Pro 100, GPT-6 Luna (max) on ChatGPT Pro 200, GPT-6 Luna (max) on ChatGPT Pro 500, GPT-6 Luna (max) on OpenCode Go, GPT-6 Luna (medium) on ChatGPT Plus, GPT-6 Luna (medium) on ChatGPT Pro 100, GPT-6 Luna (medium) on ChatGPT Pro 200, GPT-6 Luna (medium) on ChatGPT Pro 500, GPT-6 Luna (medium) on OpenCode Go, GPT-6 Luna (xhigh) on ChatGPT Plus, GPT-6 Luna (xhigh) on ChatGPT Pro 100, GPT-6 Luna (xhigh) on ChatGPT Pro 200, GPT-6 Luna (xhigh) on ChatGPT Pro 500, GPT-6 Luna (xhigh) on OpenCode Go, GPT-6.1 Terra (high) on ChatGPT Plus, GPT-6.1 Terra (high) on ChatGPT Pro 100, GPT-6.1 Terra (high) on ChatGPT Pro 200, GPT-6.1 Terra (high) on ChatGPT Pro 500, GPT-6.1 Terra (max) on ChatGPT Plus, GPT-6.1 Terra (max) on ChatGPT Pro 100, GPT-6.1 Terra (max) on ChatGPT Pro 200, GPT-6.1 Terra (max) on ChatGPT Pro 500, GPT-6.1 Terra (medium) on ChatGPT Plus, GPT-6.1 Terra (medium) on ChatGPT Pro 100, GPT-6.1 Terra (medium) on ChatGPT Pro 200, GPT-6.1 Terra (medium) on ChatGPT Pro 500, GPT-6.1 Terra (xhigh) on ChatGPT Plus, GPT-6.1 Terra (xhigh) on ChatGPT Pro 100, GPT-6.1 Terra (xhigh) on ChatGPT Pro 200, GPT-6.1 Terra (xhigh) on ChatGPT Pro 500 depend on an owner assumption and are unevaluable there (—), never reselected or replaced by API cost.

### Plan basis: rank 1

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M | S1T | S1T recentred |
|---|---:|---:|---:|---:|---:|---:|---:|
| Claude Haiku 5.5 (high) on Claude Max 20x | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (high) on Claude Max 5x | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (high) on Claude Pro | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (high) on OpenCode Go | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (medium) on Claude Max 20x | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (medium) on Claude Max 5x | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (medium) on Claude Pro | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (medium) on OpenCode Go | 0.0% | — | — | — | — | — | — |
| Claude Opus 5.5 (high) on Claude Max 20x | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (high) on Claude Max 5x | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (high) on Claude Pro | 0.0% | 0.0% | 14.0% | 0.0% | 0.0% | 23.3% | 22.8% |
| GPT-6 Astra (high) on ChatGPT Plus | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (high) on ChatGPT Pro 100 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (high) on ChatGPT Pro 200 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (high) on ChatGPT Pro 500 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Luna (high) on ChatGPT Plus | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (high) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (high) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (high) on ChatGPT Pro 500 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (high) on OpenCode Go | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Plus | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 500 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (max) on OpenCode Go | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (medium) on ChatGPT Plus | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (medium) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (medium) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (medium) on ChatGPT Pro 500 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (medium) on OpenCode Go | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (xhigh) on ChatGPT Plus | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (xhigh) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (xhigh) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (xhigh) on ChatGPT Pro 500 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (xhigh) on OpenCode Go | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Sol (high) on ChatGPT Plus | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (high) on ChatGPT Pro 100 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (high) on ChatGPT Pro 200 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (high) on ChatGPT Pro 500 | 100.0% | 100.0% | 86.0% | 100.0% | 100.0% | 47.4% | 48.0% |
| GPT-6.1 Sol (low) on ChatGPT Plus | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (low) on ChatGPT Pro 100 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (low) on ChatGPT Pro 200 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (low) on ChatGPT Pro 500 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (medium) on ChatGPT Plus | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (medium) on ChatGPT Pro 100 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (medium) on ChatGPT Pro 200 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (medium) on ChatGPT Pro 500 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 29.3% | 29.1% |
| GPT-6.1 Terra (high) on ChatGPT Plus | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Terra (high) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Terra (high) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Terra (high) on ChatGPT Pro 500 | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Terra (max) on ChatGPT Plus | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Terra (max) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Terra (max) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Terra (max) on ChatGPT Pro 500 | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Terra (medium) on ChatGPT Plus | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Terra (medium) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Terra (medium) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Terra (medium) on ChatGPT Pro 500 | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Terra (xhigh) on ChatGPT Plus | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Terra (xhigh) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Terra (xhigh) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Terra (xhigh) on ChatGPT Pro 500 | 0.0% | — | — | — | — | — | — |

### Plan basis: rank 3 or better

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M | S1T | S1T recentred |
|---|---:|---:|---:|---:|---:|---:|---:|
| Claude Haiku 5.5 (high) on Claude Max 20x | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (high) on Claude Max 5x | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (high) on Claude Pro | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (high) on OpenCode Go | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (medium) on Claude Max 20x | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (medium) on Claude Max 5x | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (medium) on Claude Pro | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (medium) on OpenCode Go | 0.0% | — | — | — | — | — | — |
| Claude Opus 5.5 (high) on Claude Max 20x | 0.0% | 0.0% | 18.0% | 0.0% | 0.0% | 24.9% | 24.7% |
| Claude Opus 5.5 (high) on Claude Max 5x | 0.0% | 0.0% | 8.4% | 0.0% | 0.0% | 20.4% | 19.9% |
| Claude Opus 5.5 (high) on Claude Pro | 0.0% | 0.0% | 19.1% | 0.0% | 0.0% | 25.4% | 25.3% |
| GPT-6 Astra (high) on ChatGPT Plus | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (high) on ChatGPT Pro 100 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (high) on ChatGPT Pro 200 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (high) on ChatGPT Pro 500 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Luna (high) on ChatGPT Plus | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (high) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (high) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (high) on ChatGPT Pro 500 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (high) on OpenCode Go | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Plus | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 500 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (max) on OpenCode Go | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (medium) on ChatGPT Plus | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (medium) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (medium) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (medium) on ChatGPT Pro 500 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (medium) on OpenCode Go | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (xhigh) on ChatGPT Plus | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (xhigh) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (xhigh) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (xhigh) on ChatGPT Pro 500 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (xhigh) on OpenCode Go | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Sol (high) on ChatGPT Plus | 100.0% | 100.0% | 82.0% | 100.0% | 100.0% | 46.5% | 46.7% |
| GPT-6.1 Sol (high) on ChatGPT Pro 100 | 100.0% | 100.0% | 82.0% | 100.0% | 100.0% | 46.5% | 46.7% |
| GPT-6.1 Sol (high) on ChatGPT Pro 200 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (high) on ChatGPT Pro 500 | 100.0% | 100.0% | 91.5% | 100.0% | 100.0% | 50.7% | 51.2% |
| GPT-6.1 Sol (low) on ChatGPT Plus | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (low) on ChatGPT Pro 100 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (low) on ChatGPT Pro 200 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (low) on ChatGPT Pro 500 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.1% |
| GPT-6.1 Sol (medium) on ChatGPT Plus | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 28.5% | 28.4% |
| GPT-6.1 Sol (medium) on ChatGPT Pro 100 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 28.5% | 28.4% |
| GPT-6.1 Sol (medium) on ChatGPT Pro 200 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (medium) on ChatGPT Pro 500 | 0.0% | 0.0% | 0.3% | 0.0% | 0.0% | 32.2% | 31.9% |
| GPT-6.1 Terra (high) on ChatGPT Plus | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Terra (high) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Terra (high) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Terra (high) on ChatGPT Pro 500 | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Terra (max) on ChatGPT Plus | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Terra (max) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Terra (max) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Terra (max) on ChatGPT Pro 500 | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Terra (medium) on ChatGPT Plus | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Terra (medium) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Terra (medium) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Terra (medium) on ChatGPT Pro 500 | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Terra (xhigh) on ChatGPT Plus | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Terra (xhigh) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Terra (xhigh) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Terra (xhigh) on ChatGPT Pro 500 | 0.0% | — | — | — | — | — | — |

### Plan basis: on the frontier

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M | S1T | S1T recentred |
|---|---:|---:|---:|---:|---:|---:|---:|
| Claude Haiku 5.5 (high) on Claude Max 20x | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (high) on Claude Max 5x | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (high) on Claude Pro | 100.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (high) on OpenCode Go | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (medium) on Claude Max 20x | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (medium) on Claude Max 5x | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (medium) on Claude Pro | 100.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (medium) on OpenCode Go | 0.0% | — | — | — | — | — | — |
| Claude Opus 5.5 (high) on Claude Max 20x | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (high) on Claude Max 5x | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (high) on Claude Pro | 100.0% | 100.0% | 98.9% | 100.0% | 100.0% | 72.4% | 72.8% |
| GPT-6 Astra (high) on ChatGPT Plus | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (high) on ChatGPT Pro 100 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (high) on ChatGPT Pro 200 | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 73.7% | 74.5% |
| GPT-6 Astra (high) on ChatGPT Pro 500 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Luna (high) on ChatGPT Plus | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (high) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (high) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (high) on ChatGPT Pro 500 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (high) on OpenCode Go | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Plus | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 500 | 100.0% | — | — | — | — | — | — |
| GPT-6 Luna (max) on OpenCode Go | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (medium) on ChatGPT Plus | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (medium) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (medium) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (medium) on ChatGPT Pro 500 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (medium) on OpenCode Go | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (xhigh) on ChatGPT Plus | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (xhigh) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (xhigh) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (xhigh) on ChatGPT Pro 500 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (xhigh) on OpenCode Go | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Sol (high) on ChatGPT Plus | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (high) on ChatGPT Pro 100 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (high) on ChatGPT Pro 200 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (high) on ChatGPT Pro 500 | 100.0% | 100.0% | 99.1% | 100.0% | 100.0% | 74.0% | 74.6% |
| GPT-6.1 Sol (low) on ChatGPT Plus | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (low) on ChatGPT Pro 100 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (low) on ChatGPT Pro 200 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (low) on ChatGPT Pro 500 | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% |
| GPT-6.1 Sol (medium) on ChatGPT Plus | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (medium) on ChatGPT Pro 100 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (medium) on ChatGPT Pro 200 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (medium) on ChatGPT Pro 500 | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% |
| GPT-6.1 Terra (high) on ChatGPT Plus | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Terra (high) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Terra (high) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Terra (high) on ChatGPT Pro 500 | 100.0% | — | — | — | — | — | — |
| GPT-6.1 Terra (max) on ChatGPT Plus | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Terra (max) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Terra (max) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Terra (max) on ChatGPT Pro 500 | 100.0% | — | — | — | — | — | — |
| GPT-6.1 Terra (medium) on ChatGPT Plus | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Terra (medium) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Terra (medium) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Terra (medium) on ChatGPT Pro 500 | 100.0% | — | — | — | — | — | — |
| GPT-6.1 Terra (xhigh) on ChatGPT Plus | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Terra (xhigh) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Terra (xhigh) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Terra (xhigh) on ChatGPT Pro 500 | 100.0% | — | — | — | — | — | — |

### Plan basis: value-score dispersion (SD; covariance term)

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M | S1T | S1T recentred |
|---|---:|---:|---:|---:|---:|---:|---:|
| Claude Haiku 5.5 (high) on Claude Max 20x | 0.00 (+0.00) | — | — | — | — | — | — |
| Claude Haiku 5.5 (high) on Claude Max 5x | 0.00 (+0.00) | — | — | — | — | — | — |
| Claude Haiku 5.5 (high) on Claude Pro | 0.00 (+0.00) | — | — | — | — | — | — |
| Claude Haiku 5.5 (high) on OpenCode Go | 0.00 (+0.00) | — | — | — | — | — | — |
| Claude Haiku 5.5 (medium) on Claude Max 20x | 0.00 (+0.00) | — | — | — | — | — | — |
| Claude Haiku 5.5 (medium) on Claude Max 5x | 0.00 (+0.00) | — | — | — | — | — | — |
| Claude Haiku 5.5 (medium) on Claude Pro | 0.00 (+0.00) | — | — | — | — | — | — |
| Claude Haiku 5.5 (medium) on OpenCode Go | 0.00 (+0.00) | — | — | — | — | — | — |
| Claude Opus 5.5 (high) on Claude Max 20x | 0.00 (+0.00) | 0.00 (+0.00) | 1.55 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.34 (+0.00) | 1.30 (+0.00) |
| Claude Opus 5.5 (high) on Claude Max 5x | 0.00 (+0.00) | 0.00 (+0.00) | 1.55 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.34 (+0.00) | 1.30 (+0.00) |
| Claude Opus 5.5 (high) on Claude Pro | 0.00 (+0.00) | 0.00 (+0.00) | 1.55 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.34 (+0.00) | 1.30 (+0.00) |
| GPT-6 Astra (high) on ChatGPT Plus | 0.00 (+0.00) | 0.00 (+0.00) | 1.30 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.42 (+0.00) | 1.38 (+0.00) |
| GPT-6 Astra (high) on ChatGPT Pro 100 | 0.00 (+0.00) | 0.00 (+0.00) | 1.30 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.42 (+0.00) | 1.38 (+0.00) |
| GPT-6 Astra (high) on ChatGPT Pro 200 | 0.00 (+0.00) | 0.00 (+0.00) | 1.30 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.42 (+0.00) | 1.38 (+0.00) |
| GPT-6 Astra (high) on ChatGPT Pro 500 | 0.00 (+0.00) | 0.00 (+0.00) | 1.30 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.42 (+0.00) | 1.38 (+0.00) |
| GPT-6 Luna (high) on ChatGPT Plus | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6 Luna (high) on ChatGPT Pro 100 | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6 Luna (high) on ChatGPT Pro 200 | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6 Luna (high) on ChatGPT Pro 500 | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6 Luna (high) on OpenCode Go | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Plus | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 100 | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 200 | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 500 | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6 Luna (max) on OpenCode Go | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6 Luna (medium) on ChatGPT Plus | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6 Luna (medium) on ChatGPT Pro 100 | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6 Luna (medium) on ChatGPT Pro 200 | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6 Luna (medium) on ChatGPT Pro 500 | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6 Luna (medium) on OpenCode Go | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6 Luna (xhigh) on ChatGPT Plus | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6 Luna (xhigh) on ChatGPT Pro 100 | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6 Luna (xhigh) on ChatGPT Pro 200 | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6 Luna (xhigh) on ChatGPT Pro 500 | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6 Luna (xhigh) on OpenCode Go | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6.1 Sol (high) on ChatGPT Plus | 0.00 (+0.00) | 0.00 (+0.00) | 1.35 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.42 (+0.00) | 1.39 (+0.00) |
| GPT-6.1 Sol (high) on ChatGPT Pro 100 | 0.00 (+0.00) | 0.00 (+0.00) | 1.35 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.42 (+0.00) | 1.39 (+0.00) |
| GPT-6.1 Sol (high) on ChatGPT Pro 200 | 0.00 (+0.00) | 0.00 (+0.00) | 1.35 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.42 (+0.00) | 1.39 (+0.00) |
| GPT-6.1 Sol (high) on ChatGPT Pro 500 | 0.00 (+0.00) | 0.00 (+0.00) | 1.35 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.42 (+0.00) | 1.39 (+0.00) |
| GPT-6.1 Sol (low) on ChatGPT Plus | 0.00 (+0.00) | 0.00 (+0.00) | 1.75 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.40 (+0.00) | 1.38 (+0.00) |
| GPT-6.1 Sol (low) on ChatGPT Pro 100 | 0.00 (+0.00) | 0.00 (+0.00) | 1.75 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.40 (+0.00) | 1.38 (+0.00) |
| GPT-6.1 Sol (low) on ChatGPT Pro 200 | 0.00 (+0.00) | 0.00 (+0.00) | 1.75 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.40 (+0.00) | 1.38 (+0.00) |
| GPT-6.1 Sol (low) on ChatGPT Pro 500 | 0.00 (+0.00) | 0.00 (+0.00) | 1.75 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.40 (+0.00) | 1.38 (+0.00) |
| GPT-6.1 Sol (medium) on ChatGPT Plus | 0.00 (+0.00) | 0.00 (+0.00) | 1.45 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.41 (+0.00) | 1.39 (+0.00) |
| GPT-6.1 Sol (medium) on ChatGPT Pro 100 | 0.00 (+0.00) | 0.00 (+0.00) | 1.45 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.41 (+0.00) | 1.39 (+0.00) |
| GPT-6.1 Sol (medium) on ChatGPT Pro 200 | 0.00 (+0.00) | 0.00 (+0.00) | 1.45 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.41 (+0.00) | 1.39 (+0.00) |
| GPT-6.1 Sol (medium) on ChatGPT Pro 500 | 0.00 (+0.00) | 0.00 (+0.00) | 1.45 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.41 (+0.00) | 1.39 (+0.00) |
| GPT-6.1 Terra (high) on ChatGPT Plus | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6.1 Terra (high) on ChatGPT Pro 100 | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6.1 Terra (high) on ChatGPT Pro 200 | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6.1 Terra (high) on ChatGPT Pro 500 | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6.1 Terra (max) on ChatGPT Plus | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6.1 Terra (max) on ChatGPT Pro 100 | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6.1 Terra (max) on ChatGPT Pro 200 | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6.1 Terra (max) on ChatGPT Pro 500 | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6.1 Terra (medium) on ChatGPT Plus | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6.1 Terra (medium) on ChatGPT Pro 100 | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6.1 Terra (medium) on ChatGPT Pro 200 | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6.1 Terra (medium) on ChatGPT Pro 500 | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6.1 Terra (xhigh) on ChatGPT Plus | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6.1 Terra (xhigh) on ChatGPT Pro 100 | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6.1 Terra (xhigh) on ChatGPT Pro 200 | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6.1 Terra (xhigh) on ChatGPT Pro 500 | 0.00 (+0.00) | — | — | — | — | — | — |

### Named S2 specification branches

- **Bug Hunt harness band (E19)** (S2): unevaluable; the captured tbench.ai leaderboard lists no configuration under two or more agents, so no cross-agent spread exists
- **cache-hit variation (E34)** (S2): unevaluable; AA's published cost embeds its cache-pricing protocol; varying the cache-hit rate needs each basket component's cache-read and uncached-input demand, which AA publishes only for the whole Index (E157)
- **first-party list versus cross-provider median price rule (E122)** (S2): unevaluable; AA publishes one price per configuration under its own rule; the alternative rule's prices are not captured

### Cheapest-above-the-bar labels (API basis)

The 90% rule's error bound holds per published event (candidate and kernel assignment); it is not corrected across the listed candidates (E198). Each kernel assignment code gives the kernel used for the candidate and the competitors, in that order (U uniform, H endpoint-heavy; a quality-level bar has no reference rows, so it takes no letter); the label needs every assignment met.

| Bar | Candidate | Reading | Frequency range | Kernel assignments | Label |
|---|---|---|---|---|---|
| quality 44.0 | GPT-6.1 Sol (low) | not scenario-supported | 49.1% to 50.5% | UU not met, UH not met, HU not met, HH not met | no |
| quality 44.0 | GPT-6.1 Terra (high) | not scenario-supported | 49.5% to 50.7% | UU not met, UH not met, HU not met, HH not met | no |
| quality 33.0 | GPT-6 Luna (max) | not scenario-supported | 0.0% to 0.0% | UU not met, UH not met, HU not met, HH not met | no |
| quality 33.0 | GPT-6 Luna (xhigh) | not scenario-supported | 49.0% to 50.0% | UU not met, UH not met, HU not met, HH not met | no |
| quality 53.4 | GPT-6.1 Sol (high) | not scenario-supported | 50.1% to 50.7% | UU not met, UH not met, HU not met, HH not met | no |
| quality 53.4 | GPT-6.1 Sol (medium) | not scenario-supported | 49.1% to 49.4% | UU not met, UH not met, HU not met, HH not met | no |

### AI Coding Daily ranking: diagnostics

- **Terminal-Bench cross-source agreement (AA's mini-SWE-agent run against tbench.ai):** undefined (panel too small); 0 rows take the leaf from tbench.ai (gap fill).
- **Workload cross-check (E41, mandatory diagnostic):** Terminal-Bench 4.1 cost per solved task on AA's own execution against basket cost: τ_b 0.12 (interval -0.40 to 0.57), low agreement; panel (15): Claude Haiku 5.5 (high), Claude Haiku 5.5 (medium), Claude Opus 5.5 (high), GPT-6 Astra (high), GPT-6 Luna (max), GPT-6 Luna (high), GPT-6 Luna (medium), GPT-6 Luna (xhigh), GPT-6.1 Sol (high), GPT-6.1 Sol (low), GPT-6.1 Sol (medium), GPT-6.1 Terra (max), GPT-6.1 Terra (high), GPT-6.1 Terra (medium), GPT-6.1 Terra (xhigh).
- **Rank separability (O39, independent-task approximation):** median separation 4.10 value points (API) and 4.09 (Plan); separable adjacent ranks: API 0 of 14, Plan 0 of 29. Assumptions: tasks are independent and each leaf's score is a mean over its published task count (a binomial leaf drawn from its Jeffreys posterior Beta(k + 1/2, n - k + 1/2), O142; plug-in SDs with the proportion (k + 1/2) / (n + 1), I28); attempts averaged within a task and tasks shared across models are ignored, so the noise is approximate; GDPval-AA: each row's rating interval as AA's model page displays it, read as a 95% normal interval (AA states no level), SD = half-width / 1.96; AA-Omniscience: each of 3,000 questions scores +1, 0 or -1, with the shares from AA's accuracy and hallucination rate; Vals boards (Vibe Code Bench v1.1, Code Migration v1.1): Vals' published standard error per record, read as the leaf's SD; AI Coding Daily: judged points over its seven graded projects read as a binomial share of 80 points (an assumption; the board publishes no error).
- **FrontierCode against Cognition:** FrontierCode 2.0 cross-source agreement (AA against Cognition, exact model and effort; E234, O153): Kendall tau 0.91 (interval 0.81 to 0.98) on 22 rows. Cognition minus AA: mean +0.2 points, largest 3.9.
- **Gap-fill removal (E234, diagnostic):** no ranked row has a leaf from another party or the provider.
- **Bar results without the gap fills (E234, sensitivity; labels unchanged):** cheapest displayed row as published, with fills removed, and with third-party fills third-party fills minus the signed mean offset +0.2 points (third party minus AA) — API quality 44.0: GPT-6.1 Sol (low) in all three; API quality 33.0: GPT-6 Luna (xhigh) in all three; API quality 53.4: GPT-6.1 Sol (medium) in all three; Plan quality 44.0: GPT-6.1 Sol (low) in all three; Plan quality 33.0: Claude Haiku 5.5 (high) in all three; Plan quality 53.4: GPT-6.1 Sol (medium) in all three.
- **Harness cost (O123, S2 stress):** agent effects on log cost (Claude Code -0.08, Codex -0.03, DeepSeek Harness +0.36, Devin CLI -0.10, GitHub Copilot -0.25, Grok Build +0.15, Kimi Code CLI +0.22, Mistral Vibe -0.17, Muse Code +0.70, OpenCode -0.11, Pi -0.48, Qwen Code -0.14, mini-swe-agent -0.08); API ranks with each agent's effect removed: GPT-6.1 Sol (high) 1; GPT-6.1 Terra (max) 2; GPT-6.1 Sol (medium) 3; GPT-6.1 Terra (xhigh) 4; GPT-6.1 Terra (high) 5; GPT-6.1 Terra (medium) 6; GPT-6 Astra (high) 7; GPT-6.1 Sol (low) 8; GPT-6 Luna (max) 9; Claude Opus 5.5 (high) 10; Claude Haiku 5.5 (high) 11; GPT-6 Luna (xhigh) 12; GPT-6 Luna (high) 13; Claude Haiku 5.5 (medium) 14; GPT-6 Luna (medium) 15. Coding Agent Index agents (each part of its costed configuration; none is the run behind the FrontierCode or Terminal-Bench leaf): GPT-6.1 Terra (max): Codex; GPT-6 Luna (max): Codex.
- **Quality agreement:** quality agreement (matched-panel sensitivity): Kendall tau 0.64 (interval 0.29 to 0.90) on 15 rows.
- **Quality-substitution value agreement (API):** quality-substitution value agreement, api basis (matched-panel sensitivity): Kendall tau 0.30 (interval -0.21 to 0.75) on 15 rows.
- **Quality-substitution value agreement (Plan):** quality-substitution value agreement, plan basis (matched-panel sensitivity): Kendall tau 0.47 (interval 0.03 to 0.84) on 15 rows.
- **Disjoint-evidence agreement:** disjoint-evidence agreement (restricted evidence comparison, not an eligible ranking): Kendall tau 0.56 (interval 0.23 to 0.84) on 15 rows.
- **Quality source shares:** AA-run 78%, independent 22%.
- **Non-discriminating leaves:** lcr.
- **Group drift:** estimated; flagged: none.
- **Omniscience abstention sensitivity** (z_pen = max(0, I)): 4 rows move; largest move 1 (Claude Opus 5.5 (high), GPT-6 Astra (high), GPT-6 Luna (max), GPT-6.1 Terra (medium)).
- **GDPval-AA logistic sensitivity** (z = 100 / (1 + 10^((1600 - E) / 400)) against AA's pinned anchor; every other input fixed): API 2 rows move; largest move 1 (GPT-6 Astra (high), GPT-6.1 Terra (medium)); Plan 2 rows move; largest move 1 (Claude Opus 5.5 (high), GPT-6.1 Sol (medium)).
- **Anchor stability:** trimmed anchors (P10 / 2 and P90 x 2 (diagnostic only)) give $30.38 to $4,243.51; 7 rows move; largest move 4 (Claude Opus 5.5 (high)).

- **Basket readiness (E22):** priced leaves cover 55% of nominal quality weight (AutomationBench-AA, FrontierCode 2.0, GDP.pdf (AA), Terminal-Bench-Science 0.1, Terminal-Bench 4.1 (AA run)); pending components: Coding Agent Index, ITBench-AA.
- **SWE cost companion (O14, diagnostic):** 2 rows evaluated; flagged far from the median ratio: none.
- **Matched-cost diagnostic (E55):** evaluated at 68% priced quality weight; basket/matched cost-order reversals with separated intervals: 1; rank-gap warnings: 0.
- **Frontier-families anchors (E187, diagnostic):** anchors rebuilt from the 8 frontier and near-frontier references move API 10 rows move; largest move 4 (GPT-6 Astra (high)) (value points per cost doubling 4.71 vs 3.02 frozen); Plan anchors unavailable: fewer than 2 measured references (O157).
- **Frontier-families bar (E199, sensitivity; the frozen bar stays primary):** quality 33.0 over 8 configurations; cheapest at or above it on the API main workload: not unique; possibly GPT-6 Luna (max), GPT-6 Luna (xhigh) (compares 11 configurations that can qualify and 1 blocker(s) that can qualify but earn no label (E315)).
- **One row per family (E205, diagnostic; the frozen ladder and anchors stay primary):** with each family's primary configuration only (4 rows in the one-row-per-family bar population), the ladder (headline, lower quartile, upper quartile) would be 31.5 / 31.2 / 46.3 against 44.0 / 33.0 / 53.4 frozen; anchors rebuilt from its 4 references move API 15 rows move; largest move 6 (GPT-6 Luna (high), GPT-6 Luna (medium), GPT-6.1 Terra (xhigh)) (value points per cost doubling 5.36 vs 3.02 frozen); Plan anchors unavailable: fewer than 2 measured references (O157).
- **Ladder over scored rows (I28, sensitivity; the frozen ladder stays primary):** the bar population keeps full-benchmark rows that have no cost; today every such row has a cost, so the ladder is unchanged.
- **Bar currency (E207, informational):** rows reaching each frozen bar: quality 44.0: 8 of 15; quality 33.0: 12 of 15; quality 53.4: 5 of 15; the current population would freeze 44.0 / 33.0 / 53.4; lifetime until the next anchor re-freeze or methodology version, whichever comes first; no staleness flag.
- **Token mix (E208):** 15 selected routes: mix unidentified: the basket's token-category shares are set-identified only (E124), so the L1 test (above 0.30 flags mix-unmatched) is not computed.
- **Observed-range sensitivity (E219, not evidence; no label changes):** with each missing leaf inside the cohort's observed range for that leaf, quality 44.0: 8 can qualify, 7 confirmed; possibly cheapest GPT-6.1 Sol (low), GPT-6.1 Terra (high); quality 33.0: 11 can qualify, 10 confirmed; possibly cheapest GPT-6 Luna (max), GPT-6 Luna (xhigh); quality 53.4: 5 can qualify, 4 confirmed; possibly cheapest GPT-6.1 Sol (high), GPT-6.1 Sol (medium).
- **What would settle the headline bar (E221, not a claim):** rows that can but need not reach quality 44.0, with the mean score their missing leaves would need: GPT-6.1 Sol (low) (no missing leaf; reporting precision only).
- **Common leaf set (E226, diagnostic; scores unchanged):** without the leaves fewer than 90% of the ranking's ranked rows have (none), API no rank changes; Plan no rank changes; rows reaching each bar: quality 44.0: 8 → 8; quality 33.0: 12 → 12; quality 53.4: 5 → 5; rows whose displayed quality differs from common-leaf quality by more than one cost doubling's worth: none.
- **Harness by leaf (E227):** Terminal-Bench: mini-SWE-agent 15; Bug Hunt: Codex CLI 12, Claude Code 3; AI Coding Daily: Codex CLI 12, Claude Code 3.
- **Coding Agent Index safety refusals (O63, flagged; costs and scores unchanged):** none.

### Leave-one-component-out cost family (E172)

Each admitted basket unit removed in turn, scored on anchors rebuilt by the freeze rule (rank changes against the primary ranking; quality held fixed).

| Removed component | API rank changes | Plan rank changes | API value points per cost doubling |
|---|---|---|---:|
| AA-Briefcase | no rank changes | 9 rows move; largest move 2 (Claude Opus 5.5 (high)) | 3.06 |
| GDP.pdf | 2 rows move; largest move 1 (GPT-6 Astra (high), GPT-6.1 Sol (low)) | 4 rows move; largest move 1 (GPT-6 Astra (high), GPT-6 Luna (xhigh), GPT-6.1 Terra (medium), GPT-6.1 Terra (xhigh)) | 3.03 |
| AutomationBench-AA | 9 rows move; largest move 2 (GPT-6.1 Sol (low)) | 11 rows move; largest move 3 (GPT-6.1 Sol (low)) | 3.01 |
| Terminal-Bench 4.1 (AA Index run) | no rank changes | 6 rows move; largest move 1 (GPT-6 Astra (high), GPT-6 Luna (max), GPT-6 Luna (xhigh), GPT-6.1 Sol (low), GPT-6.1 Terra (medium), GPT-6.1 Terra (xhigh)) | 3.00 |
| FrontierCode 2.0 | 2 rows move; largest move 1 (GPT-6.1 Sol (high), GPT-6.1 Terra (max)) | 8 rows move; largest move 1 (Claude Opus 5.5 (high), GPT-6 Astra (high), GPT-6 Luna (max), GPT-6 Luna (xhigh), GPT-6.1 Sol (low), GPT-6.1 Terra (max), GPT-6.1 Terra (medium), GPT-6.1 Terra (xhigh)) | 3.01 |
| Terminal-Bench-Science | 2 rows move; largest move 1 (GPT-6.1 Sol (high), GPT-6.1 Terra (max)) | 8 rows move; largest move 2 (Claude Opus 5.5 (high), GPT-6.1 Sol (medium)) | 2.99 |

### Subset rows: paired bridge and missing spend (E10, E173)

No row is scored on a subset workload.

### Deletion sensitivity

| Branch | Retained nominal weight | Status | API rank changes | Plan rank changes |
|---|---:|---|---|---|
| leave-out:frontierCode | 79% | evaluated | 11 rows move; largest move 4 (GPT-6.1 Sol (low)) | 5 rows move; largest move 3 (GPT-6.1 Sol (low)) |
| leave-out:terminalBench | 83% | evaluated | 11 rows move; largest move 5 (Claude Opus 5.5 (high), GPT-6 Luna (max)) | 11 rows move; largest move 4 (GPT-6 Luna (max)) |
| leave-out:bugHunt | 88% | evaluated | 11 rows move; largest move 2 (GPT-6 Luna (xhigh)) | 5 rows move; largest move 3 (GPT-6.1 Terra (max)) |
| leave-out:aiCodingDaily | 90% | evaluated | 4 rows move; largest move 1 (GPT-6 Luna (high), GPT-6 Luna (xhigh), GPT-6.1 Sol (high), GPT-6.1 Terra (max)) | 7 rows move; largest move 2 (GPT-6.1 Terra (max)) |
| leave-out:gdpval | 95% | evaluated | no rank changes | 4 rows move; largest move 1 (Claude Haiku 5.5 (high), Claude Opus 5.5 (high), GPT-6 Astra (high), GPT-6.1 Terra (max)) |
| leave-out:gdpPdf | 95% | evaluated | 2 rows move; largest move 1 (GPT-6 Astra (high), GPT-6.1 Terra (medium)) | 2 rows move; largest move 1 (Claude Opus 5.5 (high), GPT-6.1 Terra (max)) |
| leave-out:automationBench | 90% | evaluated | 10 rows move; largest move 2 (Claude Haiku 5.5 (high), Claude Haiku 5.5 (medium)) | 5 rows move; largest move 2 (GPT-6.1 Terra (max)) |
| leave-out:omniscience | 90% | evaluated | 6 rows move; largest move 1 (GPT-6 Astra (high), GPT-6 Luna (max), GPT-6.1 Sol (high), GPT-6.1 Sol (low), GPT-6.1 Terra (max), GPT-6.1 Terra (medium)) | 7 rows move; largest move 2 (GPT-6.1 Terra (max)) |
| leave-out:lcr | 95% | evaluated | 2 rows move; largest move 1 (GPT-6 Astra (high), GPT-6.1 Terra (medium)) | 4 rows move; largest move 1 (Claude Haiku 5.5 (high), Claude Opus 5.5 (high), GPT-6 Astra (high), GPT-6.1 Terra (max)) |
| leave-out:hle | 98% | evaluated | 2 rows move; largest move 1 (GPT-6 Astra (high), GPT-6.1 Sol (low)) | 2 rows move; largest move 1 (Claude Opus 5.5 (high), GPT-6.1 Terra (max)) |
| leave-out:tbScience | 98% | evaluated | 2 rows move; largest move 1 (GPT-6 Astra (high), GPT-6.1 Sol (low)) | no rank changes |
| leave-out:critpt | 98% | evaluated | no rank changes | no rank changes |
| leave-source-out:Artificial Analysis | 22% | not identifiable under the coverage rule | — | — |
| basket-scope | 87% | evaluated | 4 rows move; largest move 1 (GPT-6 Luna (max), GPT-6.1 Sol (high), GPT-6.1 Sol (low), GPT-6.1 Terra (max)) | 8 rows move; largest move 2 (GPT-6 Luna (max), GPT-6.1 Terra (max)) |

### Cost-component removal (Terminal-Bench 4.1 (AA Index run): evaluated)

| Basis | Run | Rank changes |
|---|---|---|
| api | cost-component removal, original anchors | 2 rows move; largest move 1 (GPT-6 Astra (high), GPT-6.1 Sol (low)) |
| api | alternative workload, recalibrated anchors | no rank changes |
| plan | cost-component removal, original anchors; fixed-multiple arithmetic stress (not identified Plan economics for the altered workload) | 4 rows move; largest move 1 (Claude Haiku 5.5 (high), Claude Opus 5.5 (high), GPT-6 Astra (high), GPT-6.1 Sol (medium)) |
| plan | alternative workload, recalibrated anchors; fixed-multiple arithmetic stress (not identified Plan economics for the altered workload) | 6 rows move; largest move 1 (GPT-6 Astra (high), GPT-6 Luna (max), GPT-6 Luna (xhigh), GPT-6.1 Sol (low), GPT-6.1 Terra (medium), GPT-6.1 Terra (xhigh)) |

### AI Coding Daily ranking: release gates

| Rule | Status | Detail |
|---|---|---|
| clip gate (E20) | passed | no basis exceeds the clipping allowance |
| cost influence flag (E91) | passed | cost not discriminating (< 10%); informational only; beta never changes (O2) |
| realised influence (E272) | fired | API: cost term offsetting (-84% of value variance); Plan: cost term offsetting (-16% of value variance); informational only, beta never changes (O2) |
| quality influence flag (E126) | passed | quality not discriminating (cost share > 90%); informational only |
| subset scoring (O17) | vacuous | subset rows scored on their own workload and anchors |
| partial component flag (E37) | vacuous | AA declined- or missing-task markers, or an Index reconstruction that misses AA's total (E209) |
| route dominance filter (E88) | vacuous | certifiably dearer routes set aside |
| Plan exploratory label (E61) | fired | fewer than half of Plan rows have an identified M_W |
| Plan evidence lifecycle and change detection (E18, E151, E269, O77, O79) | fired | 57 of 63 plan rows carry a possibly-superseded or expired route: claude-haiku-5-5-high@claude-max-20x, claude-haiku-5-5-high@claude-max-5x, claude-haiku-5-5-high@claude-pro, claude-haiku-5-5-medium@claude-max-20x, claude-haiku-5-5-medium@claude-max-5x, claude-haiku-5-5-medium@claude-pro, claude-opus-5-5-high@claude-max-20x, claude-opus-5-5-high@claude-max-5x, claude-opus-5-5-high@claude-pro, gpt-6-astra-high@chatgpt-plus, gpt-6-astra-high@chatgpt-pro-100, gpt-6-astra-high@chatgpt-pro-200, gpt-6-astra-high@chatgpt-pro-500, gpt-6-luna-high@chatgpt-plus, gpt-6-luna-high@chatgpt-pro-100, gpt-6-luna-high@chatgpt-pro-200, gpt-6-luna-high@chatgpt-pro-500, gpt-6-luna-medium@chatgpt-plus, gpt-6-luna-medium@chatgpt-pro-100, gpt-6-luna-medium@chatgpt-pro-200, gpt-6-luna-medium@chatgpt-pro-500, gpt-6-luna-xhigh@chatgpt-plus, gpt-6-luna-xhigh@chatgpt-pro-100, gpt-6-luna-xhigh@chatgpt-pro-200, gpt-6-luna-xhigh@chatgpt-pro-500, gpt-6-luna@chatgpt-plus, gpt-6-luna@chatgpt-pro-100, gpt-6-luna@chatgpt-pro-200, gpt-6-luna@chatgpt-pro-500, gpt-6.1-sol-high@chatgpt-plus, gpt-6.1-sol-high@chatgpt-pro-100, gpt-6.1-sol-high@chatgpt-pro-200, gpt-6.1-sol-high@chatgpt-pro-500, gpt-6.1-sol-low@chatgpt-plus, gpt-6.1-sol-low@chatgpt-pro-100, gpt-6.1-sol-low@chatgpt-pro-200, gpt-6.1-sol-low@chatgpt-pro-500, gpt-6.1-sol-medium@chatgpt-plus, gpt-6.1-sol-medium@chatgpt-pro-100, gpt-6.1-sol-medium@chatgpt-pro-200, gpt-6.1-sol-medium@chatgpt-pro-500, gpt-6.1-terra-high@chatgpt-plus, gpt-6.1-terra-high@chatgpt-pro-100, gpt-6.1-terra-high@chatgpt-pro-200, gpt-6.1-terra-high@chatgpt-pro-500, gpt-6.1-terra-medium@chatgpt-plus, gpt-6.1-terra-medium@chatgpt-pro-100, gpt-6.1-terra-medium@chatgpt-pro-200, gpt-6.1-terra-medium@chatgpt-pro-500, gpt-6.1-terra-xhigh@chatgpt-plus, gpt-6.1-terra-xhigh@chatgpt-pro-100, gpt-6.1-terra-xhigh@chatgpt-pro-200, gpt-6.1-terra-xhigh@chatgpt-pro-500, gpt-6.1-terra@chatgpt-plus, gpt-6.1-terra@chatgpt-pro-100, gpt-6.1-terra@chatgpt-pro-200, gpt-6.1-terra@chatgpt-pro-500 |
| acknowledged accounting-fault windows (O91, O92, O93, O95, O96) | fired | 12 of 63 plan rows rest on a measurement inside an acknowledged fault window; they stay selected and yield to two concordant user reports for their own model and plan, and the transfers resting on them follow: gpt-6-astra-high@chatgpt-pro-500, gpt-6-luna-high@chatgpt-pro-500, gpt-6-luna-medium@chatgpt-pro-500, gpt-6-luna-xhigh@chatgpt-pro-500, gpt-6-luna@chatgpt-pro-500, gpt-6.1-sol-high@chatgpt-pro-500, gpt-6.1-sol-low@chatgpt-pro-500, gpt-6.1-sol-medium@chatgpt-pro-500, gpt-6.1-terra-high@chatgpt-pro-500, gpt-6.1-terra-medium@chatgpt-pro-500, gpt-6.1-terra-xhigh@chatgpt-pro-500, gpt-6.1-terra@chatgpt-pro-500 |
| AA cost omits a pricing term (O94, O98, O100, O106, O108, O109, O114) | fired | ranked at the published cost; compete in interval outputs and the scenario labels' BlockerSafe test over [C, factor × C] ([C, ∞) without a stated factor, O98) without a label (scenario frequencies draw them at the published cost, O114), and leave the anchor population at the next freeze: claude-haiku-5-5-high (up to 5×), claude-haiku-5-5-medium (up to 5×) |
| valuation-basis gate (E170) | passed | every ranked row is compatible as captured or after evidenced revaluation |
| source clocks and evidence freshness (O59, O60, O65, E211, E216, E217, E218) | passed | every capture is within its age gate and none after the cutoff unless its source predates the cutoff's day; the build stops otherwise |
| build-stopping evidence gates (O64, O69, O71, O75, O99, O100, O101, O103, O105-O111, E195, E204, E225) | passed | the Coding Agent Index manifest (O64), the Terminal-Bench agent list (E225), cutoff-day row dates (O69), the three-stage all-provider plan search (O71, O75), the typed change records behind every route flag and partition split, which also produce each route's label and blocking dates within its launch- and schedule-bounded span (O99, O101, O105, O107, O110, O111), the register of AA notes covering every captured one, with the chart's inventory and duplicate-entry checks, the post-O103 capture notes, the basket-chart labels and chart-level notes' named rows (O100, O103, O106, O108) and the frontier path checks (E195, E204) hold; the build stops otherwise |
| score swing gate (E177) | vacuous | first v3 release: no previous v3 release to compare |
| ranking coverage (O166) | vacuous | ranks 15 of 45 cohort configurations; first v3 release: no previous v3 release to compare |
| anchor migration (E184) | vacuous | no main-workload migration deferred |
| frozen admission (O169) | vacuous | every frozen component still meets the admission threshold |
| configuration map coverage | passed | every cohort row has a configuration-map entry |
| quality clipping audit (E110) | passed | saturation disclosed; domain violations block the build |
| full benchmark set (O36, O38) | fired | listed, not ranked: gpt-6.1-sol, claude-opus-5-5, gpt-6-astra, claude-sonnet-5-5, claude-fable-5-2-high, claude-fable-5-2, claude-fable-5-2-xhigh, claude-haiku-5-5-low, claude-haiku-5-5, claude-opus-5-5-xhigh, gpt-6-astra-xhigh, gpt-6-luna-low, gpt-6.1-sol-xhigh, gpt-6.1-terra-low, gpt-6.2-astra-high, gpt-6.2-astra, gpt-6.2-astra-medium, gpt-6.2-astra-xhigh, gpt-6.2-sol-high, gpt-6.2-sol-low, gpt-6.2-sol, gpt-6.2-sol-medium, gpt-6.2-sol-xhigh, gemini-4-carbon, gemini-4-neon-high, gemini-4-neon-medium, gemini-4-neon, mimo-v2-6-flash, muse-ember, muse-ember-xhigh |
| missing-leaf rules (O8 provisional, E198b, E201b, E219, E221, E226) | vacuous | no ranked row has a missing leaf (O36) |
| S1M interval stream (E145) | vacuous | dormant: no ranked leaf carries a published confidence interval since O37, so S1M equals S1 (E236) |
| provider-claim label denial (E233) | vacuous | no row has a provider-claimed leaf |
| scenario outputs current (E72) | passed | scenario input hash matches the scored inputs |

## Common-leaf ranking (diagnostic)

Diagnostic only (O121): every configuration with AA's leaves and Bug Hunt, at any effort, scored on the ten leaves the two leading rankings share; it earns no label and never holds a release. Anchor version `v3-2026-11-26-a4-common`; leaves: FrontierCode 2.0 25%, Terminal-Bench 4.1 (AA run) 20%, Bug Hunt Bench 15% (software engineering 60%), plus the 8 leaves outside software engineering every ranking shares.

**Diagnostic ranking (O121).** It earns no interval or scenario label and its clip gate (passes on its own) never holds the release. Its bars sit at the same ladder positions as the leading rankings' but at its own levels, so the comparison below asks whether a configuration the leading rankings cannot rank would answer the same question. The answers are displayed records, not claims: a difference smaller than this ranking's quality noise margin (4.9 points, O44) is not evidence.

| Basis | Bar position | Cheapest here | Cheapest, max-effort ranking | Cheapest, AI Coding Daily ranking |
|---|---|---|---|---|
| API | median | GPT-6.1 Sol (medium) | GPT-6.1 Sol (max) (differs) | GPT-6.1 Sol (low) (differs) |
| API | lower quartile | GPT-6.1 Terra (low) | GPT-6.1 Sol (max) (differs) | GPT-6 Luna (xhigh) (differs) |
| API | upper quartile | GPT-6.1 Sol (xhigh) | GPT-6.1 Sol (max) (differs) | GPT-6.1 Sol (medium) (differs) |
| Plan | median | GPT-6.1 Sol (medium) on ChatGPT Pro 500 | GPT-6.1 Sol (max) on ChatGPT Pro 500 (differs) | GPT-6.1 Sol (low) on ChatGPT Pro 500 (differs) |
| Plan | lower quartile | Claude Haiku 5.5 (xhigh) on Claude Pro | GPT-6.1 Sol (max) on ChatGPT Pro 500 (differs) | Claude Haiku 5.5 (high) on Claude Pro (differs) |
| Plan | upper quartile | GPT-6.1 Sol (xhigh) on ChatGPT Pro 500 | GPT-6.1 Sol (max) on ChatGPT Pro 500 (differs) | GPT-6.1 Sol (medium) on ChatGPT Pro 500 (differs) |

| Configuration | Plan rank | Plan value | Plan cost score | API rank | API value | API cost score | Quality | Quality coverage | Workload |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| [GPT-6.1 Sol (xhigh)](https://valuerank.alolabs.dev/models/gpt-6-1-sol-xhigh/) | 1 | 57.95 | 63.86 | 2 | 51.55 | 38.27 | 55.98 | 100% | main |
| [GPT-6.1 Sol (max)](https://valuerank.alolabs.dev/models/gpt-6-1-sol/) | 5 | 57.52 | 54.73 | 1 | 52.08 | 32.99 | 58.44 | 100% | main |
| [GPT-6.1 Terra (max)](https://valuerank.alolabs.dev/models/gpt-6-1-terra/) | 9 | 56.46 | 61.55 | 3 | 50.31 | 36.94 | 54.77 | 100% | main |
| [GPT-6.1 Sol (high)](https://valuerank.alolabs.dev/models/gpt-6-1-sol-high/) | 12 | 56.11 | 67.90 | 4 | 49.29 | 40.62 | 52.18 | 100% | main |
| [Claude Opus 5.5 (xhigh)](https://valuerank.alolabs.dev/models/claude-opus-5-5-xhigh/) | 16 | 55.34 | 59.16 | 14 | 44.24 | 14.77 | 54.07 | 100% | main |
| [Claude Sonnet 5.5 (max)](https://valuerank.alolabs.dev/models/claude-sonnet-5-5/) | 18 | 55.21 | 49.55 | 11 | 45.13 | 9.20 | 57.10 | 100% | main |
| [GPT-6.1 Sol (medium)](https://valuerank.alolabs.dev/models/gpt-6-1-sol-medium/) | 23 | 54.95 | 75.20 | 7 | 47.36 | 44.84 | 48.20 | 100% | main |
| [Claude Opus 5.5 (high)](https://valuerank.alolabs.dev/models/claude-opus-5-5-high/) | 27 | 54.74 | 70.36 | 17 | 42.46 | 21.26 | 49.53 | 100% | main |
| [Claude Opus 5.5 (max)](https://valuerank.alolabs.dev/models/claude-opus-5-5/) | 30 | 53.76 | 48.30 | 16 | 43.80 | 8.48 | 55.57 | 100% | main |
| [GPT-6 Astra (xhigh)](https://valuerank.alolabs.dev/models/gpt-6-astra-xhigh/) | 33 | 52.38 | 35.44 | 5 | 48.07 | 18.19 | 58.03 | 100% | main |
| [GPT-6.1 Terra (high)](https://valuerank.alolabs.dev/models/gpt-6-1-terra-high/) | 34 | 52.35 | 84.08 | 15 | 43.83 | 49.99 | 41.78 | 100% | main |
| [GPT-6.1 Terra (xhigh)](https://valuerank.alolabs.dev/models/gpt-6-1-terra-xhigh/) | 35 | 52.35 | 77.06 | 13 | 44.56 | 45.92 | 44.11 | 100% | main |
| [GPT-6.1 Terra (medium)](https://valuerank.alolabs.dev/models/gpt-6-1-terra-medium/) | 42 | 51.18 | 90.49 | 18 | 41.98 | 53.70 | 38.07 | 100% | main |
| [GPT-6 Astra (max)](https://valuerank.alolabs.dev/models/gpt-6-astra/) | 47 | 50.80 | 26.92 | 6 | 47.38 | 13.26 | 58.75 | 100% | main |
| [Claude Haiku 5.5 (xhigh)](https://valuerank.alolabs.dev/models/claude-haiku-5-5/) | 49 | 50.41 | 100.00 | 20 | 39.03 | 54.49 | 33.88 | 100% | main |
| [GPT-6 Astra (high)](https://valuerank.alolabs.dev/models/gpt-6-astra-high/) | 53 | 50.15 | 37.91 | 10 | 45.58 | 19.63 | 54.23 | 100% | main |
| [GPT-6.1 Sol (low)](https://valuerank.alolabs.dev/models/gpt-6-1-sol-low/) | 55 | 49.72 | 85.36 | 19 | 41.06 | 50.72 | 37.84 | 100% | main |
| [GPT-6 Luna (max)](https://valuerank.alolabs.dev/models/gpt-6-luna/) | 62 | 48.96 | 99.75 | 21 | 38.79 | 59.06 | 32.03 | 100% | main |
| [GPT-6.1 Terra (low)](https://valuerank.alolabs.dev/models/gpt-6-1-terra-low/) | 65 | 47.94 | 100.00 | 22 | 37.93 | 59.95 | 30.58 | 100% | main |
| [Claude Haiku 5.5 (high)](https://valuerank.alolabs.dev/models/claude-haiku-5-5-high/) | 70 | 47.11 | 100.00 | 23 | 37.02 | 59.62 | 29.48 | 100% | main |
| [Claude Fable 5.2 (max)](https://valuerank.alolabs.dev/models/claude-fable-5-2/) | 75 | 46.46 | 0.00 | 8 | 46.46 | 0.00 | 61.94 | 100% | main |
| [GPT-6 Luna (xhigh)](https://valuerank.alolabs.dev/models/gpt-6-luna-xhigh/) | 76 | 44.72 | 100.00 | 24 | 35.68 | 63.84 | 26.29 | 100% | main |
| [Claude Fable 5.2 (xhigh)](https://valuerank.alolabs.dev/models/claude-fable-5-2-xhigh/) | 80 | 44.18 | 0.00 | 12 | 45.03 | 3.40 | 58.90 | 100% | main |
| [Claude Fable 5.2 (high)](https://valuerank.alolabs.dev/models/claude-fable-5-2-high/) | 81 | 43.48 | 0.00 | 9 | 45.82 | 9.39 | 57.97 | 100% | main |
| [GPT-6 Luna (high)](https://valuerank.alolabs.dev/models/gpt-6-luna-high/) | 82 | 43.43 | 100.00 | 25 | 35.29 | 67.45 | 24.57 | 100% | main |
| [Claude Haiku 5.5 (medium)](https://valuerank.alolabs.dev/models/claude-haiku-5-5-medium/) | 86 | 43.25 | 100.00 | 26 | 34.62 | 65.48 | 24.34 | 100% | main |
| [GPT-6 Luna (medium)](https://valuerank.alolabs.dev/models/gpt-6-luna-medium/) | 89 | 39.82 | 100.00 | 27 | 33.04 | 72.86 | 19.76 | 100% | main |
| [Claude Haiku 5.5 (low)](https://valuerank.alolabs.dev/models/claude-haiku-5-5-low/) | 93 | 39.77 | 100.00 | 28 | 32.96 | 72.77 | 19.70 | 100% | main |
| [GPT-6 Luna (low)](https://valuerank.alolabs.dev/models/gpt-6-luna-low/) | 104 | 34.82 | 100.00 | 29 | 32.70 | 91.52 | 13.10 | 100% | main |

### Common-leaf ranking (diagnostic): quality leaf scores

| Configuration | FrontierCode 2.0 | Terminal-Bench 4.1 (AA run) | Bug Hunt Bench | GDPval-AA v2.1 | GDP.pdf (AA) | AutomationBench-AA | AA-Omniscience v1.1 | AA-LCR v1.1 | HLE-Diamond | Terminal-Bench-Science 0.1 | CritPt v2 (hard subset) | Quality | Provisional |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| GPT-6.1 Sol (xhigh) | 38.5 | 53.5 | 71.4 | 53.1 | 31.8 | 66.6 | 71.2 | 79.7 | 55.8 | 50.5 | 69.5 | 55.98 | no |
| GPT-6.1 Sol (max) | 40.6 | 56.6 | 78.7 | 55.4 | 31.0 | 64.9 | 71.0 | 83.0 | 58.8 | 58.1 | 69.5 | 58.44 | no |
| GPT-6.1 Terra (max) | 42.1 | 56.6 | 63.7 | 48.7 | 28.6 | 60.2 | 64.8 | 82.7 | 47.3 | 57.6 | 68.0 | 54.77 | no |
| GPT-6.1 Sol (high) | 36.7 | 51.0 | 55.0 | 51.1 | 32.0 | 64.5 | 70.5 | 82.3 | 51.9 | 46.2 | 68.5 | 52.18 | no |
| Claude Opus 5.5 (xhigh) | 44.2 | 59.6 | 35.4 | 66.8 | 26.6 | 65.0 | 71.6 | 84.7 | 64.0 | 61.9 | 67.5 | 54.07 | no |
| Claude Sonnet 5.5 (max) | 41.9 | 65.2 | 55.7 | 66.9 | 25.8 | 71.8 | 65.2 | 82.7 | 53.3 | 53.3 | 59.0 | 57.10 | no |
| GPT-6.1 Sol (medium) | 33.4 | 48.0 | 42.7 | 48.2 | 30.0 | 62.6 | 70.1 | 83.3 | 46.0 | 37.1 | 67.0 | 48.20 | no |
| Claude Opus 5.5 (high) | 35.9 | 56.1 | 30.5 | 60.4 | 28.8 | 63.2 | 71.2 | 82.7 | 55.6 | 49.0 | 59.5 | 49.53 | no |
| Claude Opus 5.5 (max) | 46.9 | 59.1 | 36.4 | 68.3 | 26.2 | 69.5 | 74.1 | 84.7 | 67.9 | 59.0 | 68.0 | 55.57 | no |
| GPT-6 Astra (xhigh) | 41.4 | 60.1 | 69.0 | 53.6 | 32.2 | 67.2 | 71.8 | 80.0 | 61.5 | 54.8 | 71.0 | 58.03 | no |
| GPT-6.1 Terra (high) | 37.5 | 42.9 | 11.8 | 42.7 | 28.0 | 58.5 | 63.9 | 82.3 | 35.4 | 33.3 | 61.5 | 41.78 | no |
| GPT-6.1 Terra (xhigh) | 36.9 | 46.5 | 20.3 | 45.8 | 26.6 | 59.9 | 64.5 | 81.7 | 42.3 | 41.9 | 60.5 | 44.11 | no |
| GPT-6.1 Terra (medium) | 34.5 | 31.8 | 10.5 | 41.2 | 28.4 | 57.8 | 63.3 | 80.7 | 31.3 | 24.8 | 56.5 | 38.07 | no |
| GPT-6 Astra (max) | 42.4 | 59.1 | 71.8 | 54.4 | 31.0 | 68.5 | 71.2 | 80.7 | 63.8 | 63.3 | 70.5 | 58.75 | no |
| Claude Haiku 5.5 (xhigh) | 29.9 | 28.8 | 18.0 | 51.2 | 18.2 | 36.0 | 53.9 | 78.3 | 28.8 | 18.1 | 47.5 | 33.88 | no |
| GPT-6 Astra (high) | 40.1 | 54.5 | 53.9 | 51.9 | 31.0 | 66.6 | 72.3 | 80.0 | 59.3 | 59.5 | 71.5 | 54.23 | no |
| GPT-6.1 Sol (low) | 20.2 | 30.8 | 33.4 | 41.1 | 27.0 | 52.6 | 69.0 | 84.0 | 38.2 | 11.0 | 62.5 | 37.84 | no |
| GPT-6 Luna (max) | 25.2 | 12.6 | 29.5 | 47.2 | 22.8 | 53.2 | 45.9 | 83.3 | 22.2 | 8.6 | 42.5 | 32.03 | no |
| GPT-6.1 Terra (low) | 24.5 | 15.2 | 7.9 | 35.2 | 25.6 | 56.2 | 61.5 | 81.0 | 24.9 | 7.6 | 50.5 | 30.58 | no |
| Claude Haiku 5.5 (high) | 23.2 | 22.7 | 14.4 | 46.2 | 17.2 | 33.7 | 52.6 | 77.3 | 23.7 | 10.0 | 45.0 | 29.48 | no |
| Claude Fable 5.2 (max) | 48.8 | 61.6 | 59.4 | 66.5 | 24.2 | 76.4 | 83.4 | 83.3 | 80.2 | 73.3 | 76.5 | 61.94 | no |
| GPT-6 Luna (xhigh) | 18.4 | 8.1 | 18.7 | 43.7 | 18.6 | 47.8 | 43.5 | 80.0 | 18.9 | 5.2 | 37.0 | 26.29 | no |
| Claude Fable 5.2 (xhigh) | 47.6 | 61.6 | 47.2 | 62.6 | 21.4 | 74.2 | 82.4 | 82.7 | 75.8 | 67.6 | 73.5 | 58.90 | no |
| Claude Fable 5.2 (high) | 49.1 | 60.1 | 42.7 | 60.9 | 21.8 | 71.4 | 82.0 | 83.3 | 73.8 | 70.0 | 73.0 | 57.97 | no |
| GPT-6 Luna (high) | 18.6 | 5.1 | 12.9 | 42.5 | 18.2 | 47.8 | 43.6 | 79.3 | 15.6 | 2.9 | 31.0 | 24.57 | no |
| Claude Haiku 5.5 (medium) | 16.1 | 15.2 | 11.5 | 39.1 | 15.2 | 28.6 | 52.1 | 77.3 | 16.8 | 7.1 | 30.5 | 24.34 | no |
| GPT-6 Luna (medium) | 12.8 | 2.5 | 2.9 | 38.5 | 13.8 | 40.5 | 43.2 | 78.3 | 15.1 | 1.4 | 27.5 | 19.76 | no |
| Claude Haiku 5.5 (low) | 8.0 | 12.6 | 9.3 | 31.5 | 11.2 | 22.9 | 51.1 | 72.0 | 14.1 | 1.9 | 21.5 | 19.70 | no |
| GPT-6 Luna (low) | 2.2 | 0.0 | 9.3 | 27.0 | 9.0 | 12.0 | 41.0 | 74.0 | 10.2 | 1.0 | 9.5 | 13.10 | no |

### Common-leaf ranking (diagnostic): displayed record and noise

- API basis, displayed record (not a claim; E203): cheapest at or above quality 48.2: GPT-6.1 Sol (medium) ($360.71 per basket run; 15 reach it); at or above quality 30.6: GPT-6.1 Terra (low) ($104.95 per basket run; 22 reach it); at or above quality 56.0: GPT-6.1 Sol (xhigh) ($617.20 per basket run; 8 reach it).
- API basis, pointwise noise-margin screen (O171; Δ = (Q − H)/√(σ² + σ_H²) at correlation 0 with the bar setter, 1.96 per comparison; separate comparisons, not a simultaneous confidence statement, E337): at or above quality 48.2: rounding-stable only (contested by GPT-6.1 Terra (xhigh)), 14 cheaper rows compared; at or above quality 30.6: rounding-stable only, 6 cheaper rows compared; at or above quality 56.0: rounding-stable only (contested by GPT-6.1 Sol (high)), 16 cheaper rows compared.
- API basis, noise-margin companion (O44; each bar plus 4.9 quality points, so the bar's own configuration cannot decide it): cheapest at or above quality 53.1: GPT-6.1 Sol (xhigh) ($617.20 per basket run); at or above quality 35.5: GPT-6.1 Terra (medium) ($174.91 per basket run); at or above quality 60.9: Claude Fable 5.2 (max) ($19,550.04 per basket run).
- Plan basis, displayed record (not a claim; E203): cheapest at or above quality 48.2: GPT-6.1 Sol (medium) on ChatGPT Pro 500 ($33.49 per basket run; 47 reach it); at or above quality 30.6: Claude Haiku 5.5 (xhigh) on Claude Pro ($2.78 per basket run; 76 reach it); at or above quality 56.0: GPT-6.1 Sol (xhigh) on ChatGPT Pro 500 ($57.30 per basket run; 22 reach it).
- Plan basis, pointwise noise-margin screen (O171; Δ = (Q − H)/√(σ² + σ_H²) at correlation 0 with the bar setter, 1.96 per comparison; separate comparisons, not a simultaneous confidence statement, E337): at or above quality 48.2: rounding-stable only (contested by GPT-6.1 Terra (xhigh) on ChatGPT Pro 100, GPT-6.1 Terra (xhigh) on ChatGPT Pro 200, GPT-6.1 Terra (xhigh) on ChatGPT Pro 500), 54 cheaper rows compared; at or above quality 30.6: rounding-stable only (contested by Claude Haiku 5.5 (high) on Claude Max 20x, Claude Haiku 5.5 (high) on Claude Max 5x, Claude Haiku 5.5 (high) on Claude Pro), 13 cheaper rows compared; at or above quality 56.0: rounding-stable only (contested by GPT-6.1 Sol (high) on ChatGPT Plus, GPT-6.1 Sol (high) on ChatGPT Pro 100, GPT-6.1 Sol (high) on ChatGPT Pro 200, GPT-6.1 Sol (high) on ChatGPT Pro 500), 69 cheaper rows compared.
- Plan basis, noise-margin companion (O44; each bar plus 4.9 quality points, so the bar's own configuration cannot decide it): cheapest at or above quality 53.1: GPT-6.1 Sol (xhigh) on ChatGPT Pro 500 ($57.30 per basket run); at or above quality 35.5: GPT-6.1 Terra (medium) on ChatGPT Pro 500 ($16.24 per basket run); at or above quality 60.9: Claude Fable 5.2 (max) on API-cost fallback ($19,550.04 per basket run).
- Safety-refusal flags (O63; costs and scores unchanged) on these bars' cheapest rows: Claude Fable 5.2 (max) (0 blocked and 63 fallback attempts of 966).
- AA cost caveat (O94; ranked at the published cost, no label of its own) on these bars' cheapest rows: Claude Haiku 5.5 (xhigh) (AA's cost omits a pricing term; up to 5× on its cost).
- Plan route flags on these bars' cheapest plan rows: Claude Haiku 5.5 (xhigh) on Claude Pro (possibly-superseded); GPT-6.1 Sol (medium) on ChatGPT Pro 500 (possibly-superseded, measured inside an acknowledged accounting-fault window (O91, O92)); GPT-6.1 Sol (xhigh) on ChatGPT Pro 500 (possibly-superseded, measured inside an acknowledged accounting-fault window (O91, O92)); GPT-6.1 Terra (medium) on ChatGPT Pro 500 (possibly-superseded, measured inside an acknowledged accounting-fault window (O91, O92)).
- These outputs compare ranked configurations only; listed families shown with an indicative value (O41) are outside them (O43): GPT-6.2 Astra (high), GPT-6.2 Astra (max), GPT-6.2 Astra (medium), GPT-6.2 Astra (xhigh), GPT-6.2 Sol (high), GPT-6.2 Sol (low), GPT-6.2 Sol (max), GPT-6.2 Sol (medium), GPT-6.2 Sol (xhigh), Gemini 4 Carbon, Gemini 4 Neon (high), Gemini 4 Neon (medium), Gemini 4 Neon (xhigh), MiMo-V2.6-Flash, Muse Ember (max), Muse Ember (xhigh).

Benchmark sampling noise (O39, an independent-task approximation): two values must differ by about 3.7 value points (median, 95%) to separate, and 0 of 28 adjacent API ranks and 1 of 55 adjacent Plan ranks of different configurations do (52 more adjacent Plan pairs are one configuration on two plans, ordered by the plans' multiples alone; E258). Its net direction is not established: every configuration is scored on the same tasks, which correlates their errors and narrows the true threshold (API 0 at correlation 0.3, 1 at correlation 0.6; Plan 1 at correlation 0.3, 1 at correlation 0.6), while sources it leaves out widen it (run-to-run and harness variance, AA's single cost run and, for the 64 Plan rows on an owner assumption (55 owner-named transfers and 9 O198 published dollar limits), that assumption's error). The noise band column groups each row with the band's first row it cannot be told apart from (O42); a Plan band marked † rests on an owner assumption (an owner-named transfer, an O46 provider quota ceiling or an O198 published dollar limit) and excludes its error: an assumed multiple can be wrong by a factor of about 2.0 before the row's value moves by the median threshold (a tolerance, not an estimate of the assumption's error). The S1T scenario shares in [scores.md](scores.md) show each row's rank-1 and top-3 frequencies under that noise.


**Listed frontier families: indicative value, not ranked and not comparable (O41).** Quality is the mean over the leaves the configuration has, renormalised, with no imputation, so these values cannot be compared with the ranking above.

| Configuration | Missing | Quality (remaining leaves) | Quality coverage | Plan value (indicative) | API value (indicative) | API cost (USD per basket run) | Plan cost (USD per basket run) |
|---|---|---:|---:|---:|---:|---:|---:|
| GPT-6.2 Astra (high) | GDPval-AA v2.1, AA-LCR v1.1 | 65.3 | 90% | 49.0 | 55.3 | $1,768.79 | $1,768.79 |
| GPT-6.2 Astra (max) | GDPval-AA v2.1, AA-LCR v1.1 | 64.3 | 90% | 48.3 | 52.9 | $3,055.74 | $3,055.74 |
| GPT-6.2 Astra (medium) | GDPval-AA v2.1, AA-LCR v1.1 | 61.0 | 90% | 45.7 | 52.8 | $1,385.56 | $1,385.56 |
| GPT-6.2 Astra (xhigh) | GDPval-AA v2.1, AA-LCR v1.1 | 66.4 | 90% | 49.8 | 55.6 | $2,085.11 | $2,085.11 |
| GPT-6.2 Sol (high) | GDPval-AA v2.1, AA-LCR v1.1 | 56.9 | 90% | 47.3 | 52.9 | $484.85 | $484.85 |
| GPT-6.2 Sol (low) | GDPval-AA v2.1, AA-LCR v1.1 | 42.8 | 90% | 41.1 | 44.9 | $216.88 | $216.88 |
| GPT-6.2 Sol (max) | GDPval-AA v2.1, AA-LCR v1.1 | 59.9 | 90% | 47.1 | 53.8 | $788.34 | $788.34 |
| GPT-6.2 Sol (medium) | GDPval-AA v2.1, AA-LCR v1.1 | 54.9 | 90% | 47.2 | 52.3 | $376.68 | $376.68 |
| GPT-6.2 Sol (xhigh) | GDPval-AA v2.1, AA-LCR v1.1 | 56.9 | 90% | 46.6 | 52.6 | $555.09 | $555.09 |
| Gemini 4 Carbon | AA-LCR v1.1 | 58.5 | 95% | 43.9 | 46.6 | $5,716.87 | $5,716.87 |
| Gemini 4 Neon (high) | GDPval-AA v2.1, AA-LCR v1.1 | 60.0 | 90% | 45.0 | 50.0 | $2,729.37 | $2,729.37 |
| Gemini 4 Neon (medium) | GDPval-AA v2.1, AA-LCR v1.1 | 52.9 | 90% | 39.7 | 46.6 | $1,487.26 | $1,487.26 |
| Gemini 4 Neon (xhigh) | GDPval-AA v2.1, AA-LCR v1.1 | 61.9 | 90% | 46.4 | 49.9 | $4,519.00 | $4,519.00 |
| MiMo-V2.6-Flash | Bug Hunt Bench | 33.8 | 85% | 40.1 | 41.1 | $82.84 | $72.16 |
| Muse Ember (max) | Bug Hunt Bench, GDPval-AA v2.1, AA-LCR v1.1 | 39.8 | 75% | 43.6 | 45.4 | $86.22 | $86.22 |
| Muse Ember (xhigh) | Bug Hunt Bench, GDPval-AA v2.1, AA-LCR v1.1 | 36.2 | 75% | 41.8 | 43.2 | $74.03 | $74.03 |

### Common-leaf ranking (diagnostic): Plan routes and calibration

#### Measured-evidence calibration (diagnostic)

References: each workload's measured-only rows with complete cost evidence are the references: c_L = cheapest / 2, c_H = dearest x 2 (diagnostic only; the official anchors are unchanged). Status: evaluated.

- Workload `9c122a3ecb672aae`: measured anchors $10.35 to $658.32 from Claude Opus 5.5 (max), Claude Opus 5.5 (high), Claude Opus 5.5 (xhigh), GPT-6 Astra (max), GPT-6 Astra (high), GPT-6 Astra (xhigh), GPT-6.1 Sol (max), GPT-6.1 Sol (high), GPT-6.1 Sol (low), GPT-6.1 Sol (medium), GPT-6.1 Sol (xhigh); anchor ratio 63.6 against the official 113.7. Official Plan anchors are set by GPT-6.1 Sol (low) on ChatGPT Pro 500 (same-model measurement from another effort) at the low end and GPT-6 Astra (max) on ChatGPT Plus (controlled measurement) at the high end.

| Configuration | Value on official Plan anchors | Value on measured anchors | Rank change |
|---|---:|---:|---:|
| Claude Opus 5.5 (high) ‡ | 54.74 | 53.70 | 0 |
| Claude Opus 5.5 (max) | 53.76 | 51.95 | 0 |
| Claude Opus 5.5 (xhigh) ‡ | 55.34 | 53.91 | 1 |
| GPT-6 Astra (high) ‡ | 50.15 | 47.98 | 1 |
| GPT-6 Astra (max) | 50.80 | 48.24 | 1 |
| GPT-6 Astra (xhigh) ‡ | 52.38 | 50.12 | 0 |
| GPT-6.1 Sol (high) ‡ | 56.11 | 54.98 | 0 |
| GPT-6.1 Sol (low) ‡ | 49.72 | 49.20 | -2 |
| GPT-6.1 Sol (max) | 57.52 | 55.93 | 0 |
| GPT-6.1 Sol (medium) ‡ | 54.95 | 54.08 | -1 |
| GPT-6.1 Sol (xhigh) ‡ | 57.95 | 56.69 | 0 |

Pairwise reversals: Claude Opus 5.5 (xhigh) and GPT-6.1 Sol (medium); GPT-6 Astra (max) and GPT-6.1 Sol (low); GPT-6 Astra (high) and GPT-6.1 Sol (low). Largest value change: 2.56 points.

‡ measured on the same model at another effort (an O88 route; measured evidence under O90).

### Common-leaf ranking (diagnostic): interval outputs

**API basis, main workload: frontier.** Not evaluable: none. Competing without a label of its own (E183): Claude Fable 5.2 (max): unverified valuation basis (E222), a provider-claimed leaf (E233), or a change-flagged (E228) Plan route; competes at its published record; Claude Fable 5.2 (high): unverified valuation basis (E222), a provider-claimed leaf (E233), or a change-flagged (E228) Plan route; competes at its published record; Claude Fable 5.2 (xhigh): unverified valuation basis (E222), a provider-claimed leaf (E233), or a change-flagged (E228) Plan route; competes at its published record; Claude Haiku 5.5 (xhigh): AA's cost omits a pricing term (O94); competes over its published cost up to the stated factor; Claude Haiku 5.5 (high): AA's cost omits a pricing term (O94); competes over its published cost up to the stated factor; Claude Haiku 5.5 (low): AA's cost omits a pricing term (O94); competes over its published cost up to the stated factor; Claude Haiku 5.5 (medium): AA's cost omits a pricing term (O94); competes over its published cost up to the stated factor.

| Configuration | Possible frontier | Definite frontier | Definite counterexample | Possible frontier blocked by |
|---|---|---|---|---|
| GPT-6.1 Sol (max) | certified | certified | — | — |
| Claude Opus 5.5 (max) | disproved | disproved | GPT-6.1 Sol (max) | GPT-6.1 Sol (max), GPT-6 Astra (max), Claude Sonnet 5.5 (max), Claude Fable 5.2 (high), GPT-6 Astra (xhigh), GPT-6.1 Sol (xhigh) |
| GPT-6.1 Sol (high) | certified | certified | — | — |
| GPT-6 Astra (max) | certified | certified | — | — |
| GPT-6.1 Terra (max) | disproved | disproved | GPT-6.1 Sol (xhigh) | GPT-6.1 Sol (xhigh) |
| Claude Sonnet 5.5 (max) | disproved | disproved | GPT-6.1 Sol (max) | GPT-6.1 Sol (max), GPT-6 Astra (max), Claude Fable 5.2 (high), GPT-6 Astra (xhigh) |
| GPT-6.1 Sol (medium) | certified | certified | — | — |
| GPT-6 Astra (high) | disproved | disproved | GPT-6.1 Sol (max) | GPT-6.1 Sol (max), GPT-6.1 Terra (max), GPT-6.1 Sol (xhigh) |
| Claude Opus 5.5 (high) | disproved | disproved | GPT-6.1 Sol (max) | GPT-6.1 Sol (max), GPT-6.1 Sol (high), GPT-6.1 Terra (max), GPT-6.1 Sol (xhigh) |
| GPT-6.1 Sol (low) | disproved | disproved | GPT-6.1 Terra (medium) | GPT-6.1 Terra (medium) |
| GPT-6.1 Terra (xhigh) | certified | certified | — | — |
| GPT-6.1 Terra (high) | certified | certified | — | — |
| GPT-6 Luna (max) | certified | certified | — | — |
| GPT-6.1 Terra (medium) | certified | certified | — | — |
| GPT-6 Luna (xhigh) | certified | certified | — | — |
| GPT-6 Luna (high) | certified | certified | — | — |
| GPT-6 Luna (medium) | certified | certified | — | — |
| Claude Opus 5.5 (xhigh) | disproved | disproved | GPT-6.1 Sol (max) | GPT-6.1 Sol (max), GPT-6.1 Terra (max), GPT-6 Astra (high), GPT-6 Astra (xhigh), GPT-6.1 Sol (xhigh) |
| GPT-6 Astra (xhigh) | disproved | disproved | GPT-6.1 Sol (max) | GPT-6.1 Sol (max) |
| GPT-6 Luna (low) | certified | certified | — | — |
| GPT-6.1 Sol (xhigh) | certified | certified | — | — |
| GPT-6.1 Terra (low) | certified | certified | — | — | Safety-refusal flags (O63; costs and scores unchanged) on these labelled rows: GPT-6 Astra (max) (13 blocked and 0 fallback attempts of 966); GPT-6.1 Sol (max) (15 blocked and 0 fallback attempts of 966). These labels carry the workload cross-check warning (E41, O160, O183: cost per solved task, τ_b 0.53 on 29 configurations, uncertain agreement): the basket-cost order behind them agrees weakly with cost per solved task; the attribution is in scores.json `diagnostics.workloadCrossCheck.attribution`.

**API basis, main workload: cheapest at or above quality 48.2** (lower-median displayed quality of the non-provisional cohort configurations at freeze (E192; headline bar)). Status certified; confirmed cheapest: none.

Configurations that can be confirmed to qualify: 11 (confirmation needs the full-composite lower bound, with missing leaves at 0, to clear the bar; O25). Cheaper same-family configurations on AA's chart that were not evaluated (not ranked in this ranking: lacking its full benchmark set, or not plotted on or near the frontier; E201c, O51): none.

Bar comparison: compares 12 configurations that can qualify and 3 blocker(s) that can qualify but earn no label (E315). The bar is a displayed-quality level; qualification tests each row's full-composite bounds, so a row above the bar on displayed quality can still fail to qualify confirmed when leaves are missing (E198).

| Configuration | Displayed quality − bar | Confirmed qualifies | Possibly qualifies | Possibly cheapest |
|---|---:|---|---|---|
| GPT-6.1 Sol (max) | 10.2 | certified | certified | disproved |
| Claude Opus 5.5 (max) | 7.4 | certified | certified | disproved |
| GPT-6.1 Sol (high) | 4.0 | certified | certified | certified |
| GPT-6 Astra (max) | 10.6 | certified | certified | disproved |
| GPT-6.1 Terra (max) | 6.6 | certified | certified | disproved |
| Claude Sonnet 5.5 (max) | 8.9 | certified | certified | disproved |
| GPT-6.1 Sol (medium) | 0.0 | disproved | certified | certified |
| GPT-6 Astra (high) | 6.0 | certified | certified | disproved |
| Claude Opus 5.5 (high) | 1.3 | certified | certified | disproved |
| GPT-6.1 Sol (low) | -10.4 | disproved | disproved | disproved |
| GPT-6.1 Terra (xhigh) | -4.1 | disproved | disproved | disproved |
| GPT-6.1 Terra (high) | -6.4 | disproved | disproved | disproved |
| GPT-6 Luna (max) | -16.2 | disproved | disproved | disproved |
| GPT-6.1 Terra (medium) | -10.1 | disproved | disproved | disproved |
| GPT-6 Luna (xhigh) | -21.9 | disproved | disproved | disproved |
| GPT-6 Luna (high) | -23.6 | disproved | disproved | disproved |
| GPT-6 Luna (medium) | -28.4 | disproved | disproved | disproved |
| Claude Opus 5.5 (xhigh) | 5.9 | certified | certified | disproved |
| GPT-6 Astra (xhigh) | 9.8 | certified | certified | disproved |
| GPT-6 Luna (low) | -35.1 | disproved | disproved | disproved |
| GPT-6.1 Sol (xhigh) | 7.8 | certified | certified | disproved |
| GPT-6.1 Terra (low) | -17.6 | disproved | disproved | disproved |

**API basis, main workload: cheapest at or above quality 30.6** (lower-quartile displayed quality of the non-provisional cohort configurations at freeze (O34)). Status certified; confirmed cheapest: none.

Configurations that can be confirmed to qualify: 17 (confirmation needs the full-composite lower bound, with missing leaves at 0, to clear the bar; O25). Cheaper same-family configurations on AA's chart that were not evaluated (not ranked in this ranking: lacking its full benchmark set, or not plotted on or near the frontier; E201c, O51): GPT-6 Luna (max): GPT-6 Luna (non-reasoning).

Bar comparison: compares 18 configurations that can qualify and 4 blocker(s) that can qualify but earn no label (E315). The bar is a displayed-quality level; qualification tests each row's full-composite bounds, so a row above the bar on displayed quality can still fail to qualify confirmed when leaves are missing (E198).

| Configuration | Displayed quality − bar | Confirmed qualifies | Possibly qualifies | Possibly cheapest |
|---|---:|---|---|---|
| GPT-6.1 Sol (max) | 27.9 | certified | certified | disproved |
| Claude Opus 5.5 (max) | 25.0 | certified | certified | disproved |
| GPT-6.1 Sol (high) | 21.6 | certified | certified | disproved |
| GPT-6 Astra (max) | 28.2 | certified | certified | disproved |
| GPT-6.1 Terra (max) | 24.2 | certified | certified | disproved |
| Claude Sonnet 5.5 (max) | 26.5 | certified | certified | disproved |
| GPT-6.1 Sol (medium) | 17.6 | certified | certified | disproved |
| GPT-6 Astra (high) | 23.6 | certified | certified | disproved |
| Claude Opus 5.5 (high) | 18.9 | certified | certified | disproved |
| GPT-6.1 Sol (low) | 7.3 | certified | certified | disproved |
| GPT-6.1 Terra (xhigh) | 13.5 | certified | certified | disproved |
| GPT-6.1 Terra (high) | 11.2 | certified | certified | disproved |
| GPT-6 Luna (max) | 1.4 | certified | certified | certified |
| GPT-6.1 Terra (medium) | 7.5 | certified | certified | disproved |
| GPT-6 Luna (xhigh) | -4.3 | disproved | disproved | disproved |
| GPT-6 Luna (high) | -6.0 | disproved | disproved | disproved |
| GPT-6 Luna (medium) | -10.8 | disproved | disproved | disproved |
| Claude Opus 5.5 (xhigh) | 23.5 | certified | certified | disproved |
| GPT-6 Astra (xhigh) | 27.4 | certified | certified | disproved |
| GPT-6 Luna (low) | -17.5 | disproved | disproved | disproved |
| GPT-6.1 Sol (xhigh) | 25.4 | certified | certified | disproved |
| GPT-6.1 Terra (low) | 0.0 | disproved | certified | certified |

**API basis, main workload: cheapest at or above quality 56.0** (upper-quartile displayed quality of the non-provisional cohort configurations at freeze (O34)). Status certified; confirmed cheapest: none.

Configurations that can be confirmed to qualify: 4 (confirmation needs the full-composite lower bound, with missing leaves at 0, to clear the bar; O25). Cheaper same-family configurations on AA's chart that were not evaluated (not ranked in this ranking: lacking its full benchmark set, or not plotted on or near the frontier; E201c, O51): none.

Bar comparison: compares 5 configurations that can qualify and 3 blocker(s) that can qualify but earn no label (E315). The bar is a displayed-quality level; qualification tests each row's full-composite bounds, so a row above the bar on displayed quality can still fail to qualify confirmed when leaves are missing (E198).

| Configuration | Displayed quality − bar | Confirmed qualifies | Possibly qualifies | Possibly cheapest |
|---|---:|---|---|---|
| GPT-6.1 Sol (max) | 2.5 | certified | certified | certified |
| Claude Opus 5.5 (max) | -0.4 | disproved | disproved | disproved |
| GPT-6.1 Sol (high) | -3.8 | disproved | disproved | disproved |
| GPT-6 Astra (max) | 2.8 | certified | certified | disproved |
| GPT-6.1 Terra (max) | -1.2 | disproved | disproved | disproved |
| Claude Sonnet 5.5 (max) | 1.1 | certified | certified | disproved |
| GPT-6.1 Sol (medium) | -7.8 | disproved | disproved | disproved |
| GPT-6 Astra (high) | -1.7 | disproved | disproved | disproved |
| Claude Opus 5.5 (high) | -6.4 | disproved | disproved | disproved |
| GPT-6.1 Sol (low) | -18.1 | disproved | disproved | disproved |
| GPT-6.1 Terra (xhigh) | -11.9 | disproved | disproved | disproved |
| GPT-6.1 Terra (high) | -14.2 | disproved | disproved | disproved |
| GPT-6 Luna (max) | -24.0 | disproved | disproved | disproved |
| GPT-6.1 Terra (medium) | -17.9 | disproved | disproved | disproved |
| GPT-6 Luna (xhigh) | -29.7 | disproved | disproved | disproved |
| GPT-6 Luna (high) | -31.4 | disproved | disproved | disproved |
| GPT-6 Luna (medium) | -36.2 | disproved | disproved | disproved |
| Claude Opus 5.5 (xhigh) | -1.9 | disproved | disproved | disproved |
| GPT-6 Astra (xhigh) | 2.0 | certified | certified | disproved |
| GPT-6 Luna (low) | -42.9 | disproved | disproved | disproved |
| GPT-6.1 Sol (xhigh) | 0.0 | disproved | certified | certified |
| GPT-6.1 Terra (low) | -25.4 | disproved | disproved | disproved |

**Plan basis, main workload:** not evaluated (no row has FullCost and an identified M_W (E61/E67)).

### Common-leaf ranking (diagnostic): scenario shares

The scenario panel is the 29 rows scored on the main workload (E96, E266).

Frequencies over 10,000 scenarios per run (seed 20261126); streams are defined in [methodology.md](methodology.md#uncertainty-outputs). S1T adds benchmark sampling noise under an independent-task approximation (O39); the other streams exclude it, and every stream excludes correlated-task, harness and attempt effects (E155).

### API basis: rank 1

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M | S1T | S1T recentred |
|---|---:|---:|---:|---:|---:|---:|---:|
| Claude Fable 5.2 (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Fable 5.2 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Fable 5.2 (xhigh) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Haiku 5.5 (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Haiku 5.5 (low) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Haiku 5.5 (medium) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Haiku 5.5 (xhigh) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (xhigh) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Sonnet 5.5 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.1% | 0.1% |
| GPT-6 Astra (xhigh) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.4% | 0.5% |
| GPT-6 Luna (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Luna (low) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Luna (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Luna (medium) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Luna (xhigh) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 2.6% | 2.6% |
| GPT-6.1 Sol (low) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (max) | 100.0% | 100.0% | 99.7% | 100.0% | 100.0% | 52.7% | 52.6% |
| GPT-6.1 Sol (medium) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.1% | 0.1% |
| GPT-6.1 Sol (xhigh) | 0.0% | 0.0% | 0.3% | 0.0% | 0.0% | 34.7% | 34.1% |
| GPT-6.1 Terra (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Terra (low) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Terra (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 9.4% | 10.0% |
| GPT-6.1 Terra (medium) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Terra (xhigh) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |

### API basis: rank 3 or better

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M | S1T | S1T recentred |
|---|---:|---:|---:|---:|---:|---:|---:|
| Claude Fable 5.2 (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.1% | 0.2% |
| Claude Fable 5.2 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.7% | 0.8% |
| Claude Fable 5.2 (xhigh) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Haiku 5.5 (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Haiku 5.5 (low) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Haiku 5.5 (medium) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Haiku 5.5 (xhigh) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (xhigh) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Sonnet 5.5 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.1% | 0.3% |
| GPT-6 Astra (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 4.1% | 3.8% |
| GPT-6 Astra (xhigh) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 9.7% | 9.2% |
| GPT-6 Luna (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Luna (low) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Luna (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Luna (medium) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Luna (xhigh) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (high) | 0.0% | 0.0% | 0.4% | 0.0% | 0.0% | 32.1% | 31.0% |
| GPT-6.1 Sol (low) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (max) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 94.3% | 94.5% |
| GPT-6.1 Sol (medium) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 3.5% | 3.6% |
| GPT-6.1 Sol (xhigh) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 90.1% | 90.1% |
| GPT-6.1 Terra (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Terra (low) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Terra (max) | 100.0% | 100.0% | 99.6% | 100.0% | 100.0% | 65.2% | 66.4% |
| GPT-6.1 Terra (medium) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Terra (xhigh) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |

### API basis: on the frontier

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M | S1T | S1T recentred |
|---|---:|---:|---:|---:|---:|---:|---:|
| Claude Fable 5.2 (high) | 0.0% | 0.0% | 28.3% | 0.0% | 0.0% | 16.9% | 17.3% |
| Claude Fable 5.2 (max) | 100.0% | 100.0% | 99.8% | 100.0% | 100.0% | 71.0% | 72.2% |
| Claude Fable 5.2 (xhigh) | 100.0% | 100.0% | 56.6% | 100.0% | 100.0% | 24.2% | 24.6% |
| Claude Haiku 5.5 (high) | 0.0% | 0.0% | 8.6% | 0.0% | 0.0% | 28.4% | 29.5% |
| Claude Haiku 5.5 (low) | 0.0% | 0.0% | 47.6% | 0.0% | 0.0% | 47.8% | 47.6% |
| Claude Haiku 5.5 (medium) | 0.0% | 0.0% | 38.7% | 0.0% | 0.0% | 43.6% | 44.9% |
| Claude Haiku 5.5 (xhigh) | 100.0% | 100.0% | 95.3% | 100.0% | 100.0% | 75.8% | 77.3% |
| Claude Opus 5.5 (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 1.1% | 1.2% |
| Claude Opus 5.5 (xhigh) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.9% | 0.9% |
| Claude Sonnet 5.5 (max) | 0.0% | 0.0% | 0.2% | 0.0% | 0.0% | 7.4% | 7.4% |
| GPT-6 Astra (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 3.2% | 3.3% |
| GPT-6 Astra (max) | 100.0% | 100.0% | 81.8% | 100.0% | 100.0% | 38.3% | 38.6% |
| GPT-6 Astra (xhigh) | 0.0% | 0.0% | 17.5% | 0.0% | 0.0% | 38.9% | 38.4% |
| GPT-6 Luna (high) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 99.8% | 99.8% |
| GPT-6 Luna (low) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% |
| GPT-6 Luna (max) | 100.0% | 100.0% | 92.6% | 100.0% | 100.0% | 72.2% | 71.2% |
| GPT-6 Luna (medium) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% |
| GPT-6 Luna (xhigh) | 100.0% | 100.0% | 99.5% | 100.0% | 100.0% | 74.6% | 75.8% |
| GPT-6.1 Sol (high) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 93.6% | 93.6% |
| GPT-6.1 Sol (low) | 0.0% | 0.0% | 42.2% | 0.0% | 0.0% | 46.4% | 44.9% |
| GPT-6.1 Sol (max) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 77.0% | 76.6% |
| GPT-6.1 Sol (medium) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 94.6% | 94.8% |
| GPT-6.1 Sol (xhigh) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 92.3% | 92.4% |
| GPT-6.1 Terra (high) | 100.0% | 100.0% | 99.6% | 100.0% | 100.0% | 90.6% | 90.9% |
| GPT-6.1 Terra (low) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 98.7% | 99.0% |
| GPT-6.1 Terra (max) | 0.0% | 0.0% | 0.5% | 0.0% | 0.0% | 30.6% | 31.1% |
| GPT-6.1 Terra (medium) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 96.6% | 96.5% |
| GPT-6.1 Terra (xhigh) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 83.1% | 83.6% |

### API basis: value-score dispersion (SD; covariance term)

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M | S1T | S1T recentred |
|---|---:|---:|---:|---:|---:|---:|---:|
| Claude Fable 5.2 (high) | 0.00 (+0.00) | 0.00 (+0.00) | 1.04 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.34 (+0.00) | 1.33 (+0.00) |
| Claude Fable 5.2 (max) | 0.00 (+0.00) | 0.00 (+0.00) | 0.97 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.36 (+0.00) | 1.36 (+0.00) |
| Claude Fable 5.2 (xhigh) | 0.00 (+0.00) | 0.00 (+0.00) | 1.03 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.34 (+0.00) | 1.33 (+0.00) |
| Claude Haiku 5.5 (high) | 0.00 (+0.00) | 0.00 (+0.00) | 1.02 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.12 (+0.00) | 1.10 (+0.00) |
| Claude Haiku 5.5 (low) | 0.00 (+0.00) | 0.00 (+0.00) | 1.15 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 0.85 (+0.00) | 0.85 (+0.00) |
| Claude Haiku 5.5 (medium) | 0.00 (+0.00) | 0.00 (+0.00) | 1.11 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.00 (+0.00) | 0.98 (+0.00) |
| Claude Haiku 5.5 (xhigh) | 0.00 (+0.00) | 0.00 (+0.00) | 0.94 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.21 (+0.00) | 1.20 (+0.00) |
| Claude Opus 5.5 (high) | 0.00 (+0.00) | 0.00 (+0.00) | 1.14 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.31 (+0.00) | 1.31 (+0.00) |
| Claude Opus 5.5 (max) | 0.00 (+0.00) | 0.00 (+0.00) | 1.03 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.33 (+0.00) | 1.31 (+0.00) |
| Claude Opus 5.5 (xhigh) | 0.00 (+0.00) | 0.00 (+0.00) | 1.03 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.32 (+0.00) | 1.32 (+0.00) |
| Claude Sonnet 5.5 (max) | 0.00 (+0.00) | 0.00 (+0.00) | 0.88 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.35 (+0.00) | 1.37 (+0.00) |
| GPT-6 Astra (high) | 0.00 (+0.00) | 0.00 (+0.00) | 0.89 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.38 (+0.00) | 1.40 (+0.00) |
| GPT-6 Astra (max) | 0.00 (+0.00) | 0.00 (+0.00) | 0.98 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.45 (+0.00) | 1.44 (+0.00) |
| GPT-6 Astra (xhigh) | 0.00 (+0.00) | 0.00 (+0.00) | 0.95 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.44 (+0.00) | 1.42 (+0.00) |
| GPT-6 Luna (high) | 0.00 (+0.00) | 0.00 (+0.00) | 1.25 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 0.89 (+0.00) | 0.88 (+0.00) |
| GPT-6 Luna (low) | 0.00 (+0.00) | 0.00 (+0.00) | 1.19 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 0.48 (+0.00) | 0.47 (+0.00) |
| GPT-6 Luna (max) | 0.00 (+0.00) | 0.00 (+0.00) | 1.12 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.08 (+0.00) | 1.10 (+0.00) |
| GPT-6 Luna (medium) | 0.00 (+0.00) | 0.00 (+0.00) | 1.33 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 0.71 (+0.00) | 0.71 (+0.00) |
| GPT-6 Luna (xhigh) | 0.00 (+0.00) | 0.00 (+0.00) | 1.18 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 0.95 (+0.00) | 0.94 (+0.00) |
| GPT-6.1 Sol (high) | 0.00 (+0.00) | 0.00 (+0.00) | 0.92 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.38 (+0.00) | 1.39 (+0.00) |
| GPT-6.1 Sol (low) | 0.00 (+0.00) | 0.00 (+0.00) | 1.25 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.22 (+0.00) | 1.22 (+0.00) |
| GPT-6.1 Sol (max) | 0.00 (+0.00) | 0.00 (+0.00) | 1.13 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.47 (+0.00) | 1.45 (+0.00) |
| GPT-6.1 Sol (medium) | 0.00 (+0.00) | 0.00 (+0.00) | 0.98 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.37 (+0.00) | 1.36 (+0.00) |
| GPT-6.1 Sol (xhigh) | 0.00 (+0.00) | 0.00 (+0.00) | 1.04 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.46 (+0.00) | 1.43 (+0.00) |
| GPT-6.1 Terra (high) | 0.00 (+0.00) | 0.00 (+0.00) | 1.25 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.25 (+0.00) | 1.25 (+0.00) |
| GPT-6.1 Terra (low) | 0.00 (+0.00) | 0.00 (+0.00) | 1.42 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.03 (+0.00) | 1.03 (+0.00) |
| GPT-6.1 Terra (max) | 0.00 (+0.00) | 0.00 (+0.00) | 0.82 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.40 (+0.00) | 1.41 (+0.00) |
| GPT-6.1 Terra (medium) | 0.00 (+0.00) | 0.00 (+0.00) | 1.26 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.21 (+0.00) | 1.23 (+0.00) |
| GPT-6.1 Terra (xhigh) | 0.00 (+0.00) | 0.00 (+0.00) | 1.11 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.30 (+0.00) | 1.30 (+0.00) |

Plan streams S1, S2, S1 endpoint-heavy, S1M, S1T and S1T recentred run with owner assumptions off (owner-named transfers, O46 provider quota ceilings and O198 published dollar limits; E167): Claude Haiku 5.5 (high) on Claude Max 20x, Claude Haiku 5.5 (high) on Claude Max 5x, Claude Haiku 5.5 (high) on Claude Pro, Claude Haiku 5.5 (high) on OpenCode Go, Claude Haiku 5.5 (low) on Claude Max 20x, Claude Haiku 5.5 (low) on Claude Max 5x, Claude Haiku 5.5 (low) on Claude Pro, Claude Haiku 5.5 (low) on OpenCode Go, Claude Haiku 5.5 (medium) on Claude Max 20x, Claude Haiku 5.5 (medium) on Claude Max 5x, Claude Haiku 5.5 (medium) on Claude Pro, Claude Haiku 5.5 (medium) on OpenCode Go, Claude Haiku 5.5 (xhigh) on Claude Max 20x, Claude Haiku 5.5 (xhigh) on Claude Max 5x, Claude Haiku 5.5 (xhigh) on Claude Pro, Claude Haiku 5.5 (xhigh) on OpenCode Go, Claude Sonnet 5.5 (max) on Claude Max 20x, Claude Sonnet 5.5 (max) on Claude Max 5x, Claude Sonnet 5.5 (max) on Claude Pro, GPT-6 Luna (high) on ChatGPT Plus, GPT-6 Luna (high) on ChatGPT Pro 100, GPT-6 Luna (high) on ChatGPT Pro 200, GPT-6 Luna (high) on ChatGPT Pro 500, GPT-6 Luna (high) on OpenCode Go, GPT-6 Luna (low) on ChatGPT Plus, GPT-6 Luna (low) on ChatGPT Pro 100, GPT-6 Luna (low) on ChatGPT Pro 200, GPT-6 Luna (low) on ChatGPT Pro 500, GPT-6 Luna (low) on OpenCode Go, GPT-6 Luna (max) on ChatGPT Plus, GPT-6 Luna (max) on ChatGPT Pro 100, GPT-6 Luna (max) on ChatGPT Pro 200, GPT-6 Luna (max) on ChatGPT Pro 500, GPT-6 Luna (max) on OpenCode Go, GPT-6 Luna (medium) on ChatGPT Plus, GPT-6 Luna (medium) on ChatGPT Pro 100, GPT-6 Luna (medium) on ChatGPT Pro 200, GPT-6 Luna (medium) on ChatGPT Pro 500, GPT-6 Luna (medium) on OpenCode Go, GPT-6 Luna (xhigh) on ChatGPT Plus, GPT-6 Luna (xhigh) on ChatGPT Pro 100, GPT-6 Luna (xhigh) on ChatGPT Pro 200, GPT-6 Luna (xhigh) on ChatGPT Pro 500, GPT-6 Luna (xhigh) on OpenCode Go, GPT-6.1 Terra (high) on ChatGPT Plus, GPT-6.1 Terra (high) on ChatGPT Pro 100, GPT-6.1 Terra (high) on ChatGPT Pro 200, GPT-6.1 Terra (high) on ChatGPT Pro 500, GPT-6.1 Terra (low) on ChatGPT Plus, GPT-6.1 Terra (low) on ChatGPT Pro 100, GPT-6.1 Terra (low) on ChatGPT Pro 200, GPT-6.1 Terra (low) on ChatGPT Pro 500, GPT-6.1 Terra (max) on ChatGPT Plus, GPT-6.1 Terra (max) on ChatGPT Pro 100, GPT-6.1 Terra (max) on ChatGPT Pro 200, GPT-6.1 Terra (max) on ChatGPT Pro 500, GPT-6.1 Terra (medium) on ChatGPT Plus, GPT-6.1 Terra (medium) on ChatGPT Pro 100, GPT-6.1 Terra (medium) on ChatGPT Pro 200, GPT-6.1 Terra (medium) on ChatGPT Pro 500, GPT-6.1 Terra (xhigh) on ChatGPT Plus, GPT-6.1 Terra (xhigh) on ChatGPT Pro 100, GPT-6.1 Terra (xhigh) on ChatGPT Pro 200, GPT-6.1 Terra (xhigh) on ChatGPT Pro 500 depend on an owner assumption and are unevaluable there (—), never reselected or replaced by API cost.

### Plan basis: rank 1

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M | S1T | S1T recentred |
|---|---:|---:|---:|---:|---:|---:|---:|
| Claude Fable 5.2 (high) on API-cost fallback | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Fable 5.2 (max) on API-cost fallback | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Fable 5.2 (xhigh) on API-cost fallback | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Haiku 5.5 (high) on Claude Max 20x | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (high) on Claude Max 5x | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (high) on Claude Pro | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (high) on OpenCode Go | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (low) on Claude Max 20x | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (low) on Claude Max 5x | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (low) on Claude Pro | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (low) on OpenCode Go | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (medium) on Claude Max 20x | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (medium) on Claude Max 5x | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (medium) on Claude Pro | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (medium) on OpenCode Go | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (xhigh) on Claude Max 20x | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (xhigh) on Claude Max 5x | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (xhigh) on Claude Pro | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (xhigh) on OpenCode Go | 0.0% | — | — | — | — | — | — |
| Claude Opus 5.5 (high) on Claude Max 20x | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (high) on Claude Max 5x | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (high) on Claude Pro | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 1.0% | 0.9% |
| Claude Opus 5.5 (max) on Claude Max 20x | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (max) on Claude Max 5x | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (max) on Claude Pro | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.1% | 0.2% |
| Claude Opus 5.5 (xhigh) on Claude Max 20x | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (xhigh) on Claude Max 5x | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (xhigh) on Claude Pro | 0.0% | 0.0% | 0.5% | 0.0% | 0.0% | 2.4% | 2.5% |
| Claude Sonnet 5.5 (max) on Claude Max 20x | 0.0% | — | — | — | — | — | — |
| Claude Sonnet 5.5 (max) on Claude Max 5x | 0.0% | — | — | — | — | — | — |
| Claude Sonnet 5.5 (max) on Claude Pro | 0.0% | — | — | — | — | — | — |
| GPT-6 Astra (high) on ChatGPT Plus | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (high) on ChatGPT Pro 100 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (high) on ChatGPT Pro 200 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (high) on ChatGPT Pro 500 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (max) on ChatGPT Plus | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (max) on ChatGPT Pro 100 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (max) on ChatGPT Pro 200 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (max) on ChatGPT Pro 500 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (xhigh) on ChatGPT Plus | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (xhigh) on ChatGPT Pro 100 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (xhigh) on ChatGPT Pro 200 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (xhigh) on ChatGPT Pro 500 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Luna (high) on ChatGPT Plus | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (high) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (high) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (high) on ChatGPT Pro 500 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (high) on OpenCode Go | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (low) on ChatGPT Plus | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (low) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (low) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (low) on ChatGPT Pro 500 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (low) on OpenCode Go | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Plus | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 500 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (max) on OpenCode Go | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (medium) on ChatGPT Plus | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (medium) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (medium) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (medium) on ChatGPT Pro 500 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (medium) on OpenCode Go | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (xhigh) on ChatGPT Plus | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (xhigh) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (xhigh) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (xhigh) on ChatGPT Pro 500 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (xhigh) on OpenCode Go | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Sol (high) on ChatGPT Plus | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (high) on ChatGPT Pro 100 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (high) on ChatGPT Pro 200 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (high) on ChatGPT Pro 500 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 7.7% | 8.0% |
| GPT-6.1 Sol (low) on ChatGPT Plus | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (low) on ChatGPT Pro 100 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (low) on ChatGPT Pro 200 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (low) on ChatGPT Pro 500 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (max) on ChatGPT Plus | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (max) on ChatGPT Pro 100 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (max) on ChatGPT Pro 200 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (max) on ChatGPT Pro 500 | 0.0% | 0.0% | 1.7% | 0.0% | 0.0% | 35.0% | 35.6% |
| GPT-6.1 Sol (medium) on ChatGPT Plus | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (medium) on ChatGPT Pro 100 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (medium) on ChatGPT Pro 200 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (medium) on ChatGPT Pro 500 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 1.8% | 1.6% |
| GPT-6.1 Sol (xhigh) on ChatGPT Plus | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (xhigh) on ChatGPT Pro 100 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (xhigh) on ChatGPT Pro 200 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (xhigh) on ChatGPT Pro 500 | 100.0% | 100.0% | 97.8% | 100.0% | 100.0% | 51.9% | 51.3% |
| GPT-6.1 Terra (high) on ChatGPT Plus | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Terra (high) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Terra (high) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Terra (high) on ChatGPT Pro 500 | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Terra (low) on ChatGPT Plus | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Terra (low) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Terra (low) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Terra (low) on ChatGPT Pro 500 | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Terra (max) on ChatGPT Plus | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Terra (max) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Terra (max) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Terra (max) on ChatGPT Pro 500 | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Terra (medium) on ChatGPT Plus | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Terra (medium) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Terra (medium) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Terra (medium) on ChatGPT Pro 500 | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Terra (xhigh) on ChatGPT Plus | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Terra (xhigh) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Terra (xhigh) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Terra (xhigh) on ChatGPT Pro 500 | 0.0% | — | — | — | — | — | — |

### Plan basis: rank 3 or better

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M | S1T | S1T recentred |
|---|---:|---:|---:|---:|---:|---:|---:|
| Claude Fable 5.2 (high) on API-cost fallback | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Fable 5.2 (max) on API-cost fallback | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Fable 5.2 (xhigh) on API-cost fallback | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Haiku 5.5 (high) on Claude Max 20x | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (high) on Claude Max 5x | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (high) on Claude Pro | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (high) on OpenCode Go | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (low) on Claude Max 20x | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (low) on Claude Max 5x | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (low) on Claude Pro | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (low) on OpenCode Go | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (medium) on Claude Max 20x | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (medium) on Claude Max 5x | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (medium) on Claude Pro | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (medium) on OpenCode Go | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (xhigh) on Claude Max 20x | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (xhigh) on Claude Max 5x | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (xhigh) on Claude Pro | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (xhigh) on OpenCode Go | 0.0% | — | — | — | — | — | — |
| Claude Opus 5.5 (high) on Claude Max 20x | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 1.1% | 1.0% |
| Claude Opus 5.5 (high) on Claude Max 5x | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.8% | 0.6% |
| Claude Opus 5.5 (high) on Claude Pro | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 1.2% | 1.1% |
| Claude Opus 5.5 (max) on Claude Max 20x | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.1% | 0.2% |
| Claude Opus 5.5 (max) on Claude Max 5x | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.1% | 0.1% |
| Claude Opus 5.5 (max) on Claude Pro | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.1% | 0.2% |
| Claude Opus 5.5 (xhigh) on Claude Max 20x | 0.0% | 0.0% | 0.8% | 0.0% | 0.0% | 2.7% | 2.7% |
| Claude Opus 5.5 (xhigh) on Claude Max 5x | 0.0% | 0.0% | 0.3% | 0.0% | 0.0% | 2.0% | 1.9% |
| Claude Opus 5.5 (xhigh) on Claude Pro | 0.0% | 0.0% | 0.8% | 0.0% | 0.0% | 2.9% | 2.8% |
| Claude Sonnet 5.5 (max) on Claude Max 20x | 0.0% | — | — | — | — | — | — |
| Claude Sonnet 5.5 (max) on Claude Max 5x | 0.0% | — | — | — | — | — | — |
| Claude Sonnet 5.5 (max) on Claude Pro | 0.0% | — | — | — | — | — | — |
| GPT-6 Astra (high) on ChatGPT Plus | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (high) on ChatGPT Pro 100 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (high) on ChatGPT Pro 200 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (high) on ChatGPT Pro 500 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (max) on ChatGPT Plus | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (max) on ChatGPT Pro 100 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (max) on ChatGPT Pro 200 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (max) on ChatGPT Pro 500 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (xhigh) on ChatGPT Plus | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (xhigh) on ChatGPT Pro 100 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (xhigh) on ChatGPT Pro 200 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (xhigh) on ChatGPT Pro 500 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Luna (high) on ChatGPT Plus | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (high) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (high) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (high) on ChatGPT Pro 500 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (high) on OpenCode Go | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (low) on ChatGPT Plus | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (low) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (low) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (low) on ChatGPT Pro 500 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (low) on OpenCode Go | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Plus | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 500 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (max) on OpenCode Go | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (medium) on ChatGPT Plus | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (medium) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (medium) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (medium) on ChatGPT Pro 500 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (medium) on OpenCode Go | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (xhigh) on ChatGPT Plus | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (xhigh) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (xhigh) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (xhigh) on ChatGPT Pro 500 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (xhigh) on OpenCode Go | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Sol (high) on ChatGPT Plus | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 7.6% | 7.9% |
| GPT-6.1 Sol (high) on ChatGPT Pro 100 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 7.6% | 7.9% |
| GPT-6.1 Sol (high) on ChatGPT Pro 200 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (high) on ChatGPT Pro 500 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 8.7% | 9.0% |
| GPT-6.1 Sol (low) on ChatGPT Plus | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (low) on ChatGPT Pro 100 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (low) on ChatGPT Pro 200 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (low) on ChatGPT Pro 500 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (max) on ChatGPT Plus | 0.0% | 0.0% | 1.7% | 0.0% | 0.0% | 34.8% | 35.5% |
| GPT-6.1 Sol (max) on ChatGPT Pro 100 | 0.0% | 0.0% | 1.7% | 0.0% | 0.0% | 34.8% | 35.5% |
| GPT-6.1 Sol (max) on ChatGPT Pro 200 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (max) on ChatGPT Pro 500 | 0.0% | 0.0% | 5.5% | 0.0% | 0.0% | 37.2% | 37.9% |
| GPT-6.1 Sol (medium) on ChatGPT Plus | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 1.7% | 1.5% |
| GPT-6.1 Sol (medium) on ChatGPT Pro 100 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 1.7% | 1.5% |
| GPT-6.1 Sol (medium) on ChatGPT Pro 200 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (medium) on ChatGPT Pro 500 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 2.1% | 1.8% |
| GPT-6.1 Sol (xhigh) on ChatGPT Plus | 100.0% | 100.0% | 97.5% | 100.0% | 100.0% | 51.7% | 51.1% |
| GPT-6.1 Sol (xhigh) on ChatGPT Pro 100 | 100.0% | 100.0% | 97.5% | 100.0% | 100.0% | 51.7% | 51.1% |
| GPT-6.1 Sol (xhigh) on ChatGPT Pro 200 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (xhigh) on ChatGPT Pro 500 | 100.0% | 100.0% | 99.2% | 100.0% | 100.0% | 54.3% | 53.6% |
| GPT-6.1 Terra (high) on ChatGPT Plus | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Terra (high) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Terra (high) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Terra (high) on ChatGPT Pro 500 | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Terra (low) on ChatGPT Plus | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Terra (low) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Terra (low) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Terra (low) on ChatGPT Pro 500 | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Terra (max) on ChatGPT Plus | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Terra (max) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Terra (max) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Terra (max) on ChatGPT Pro 500 | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Terra (medium) on ChatGPT Plus | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Terra (medium) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Terra (medium) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Terra (medium) on ChatGPT Pro 500 | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Terra (xhigh) on ChatGPT Plus | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Terra (xhigh) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Terra (xhigh) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Terra (xhigh) on ChatGPT Pro 500 | 0.0% | — | — | — | — | — | — |

### Plan basis: on the frontier

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M | S1T | S1T recentred |
|---|---:|---:|---:|---:|---:|---:|---:|
| Claude Fable 5.2 (high) on API-cost fallback | 0.0% | 0.0% | 28.6% | 0.0% | 0.0% | 17.5% | 17.0% |
| Claude Fable 5.2 (max) on API-cost fallback | 100.0% | 100.0% | 99.7% | 100.0% | 100.0% | 71.4% | 72.0% |
| Claude Fable 5.2 (xhigh) on API-cost fallback | 100.0% | 100.0% | 57.1% | 100.0% | 100.0% | 26.2% | 26.0% |
| Claude Haiku 5.5 (high) on Claude Max 20x | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (high) on Claude Max 5x | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (high) on Claude Pro | 100.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (high) on OpenCode Go | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (low) on Claude Max 20x | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (low) on Claude Max 5x | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (low) on Claude Pro | 100.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (low) on OpenCode Go | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (medium) on Claude Max 20x | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (medium) on Claude Max 5x | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (medium) on Claude Pro | 100.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (medium) on OpenCode Go | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (xhigh) on Claude Max 20x | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (xhigh) on Claude Max 5x | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (xhigh) on Claude Pro | 100.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (xhigh) on OpenCode Go | 0.0% | — | — | — | — | — | — |
| Claude Opus 5.5 (high) on Claude Max 20x | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (high) on Claude Max 5x | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (high) on Claude Pro | 100.0% | 100.0% | 96.7% | 100.0% | 100.0% | 69.3% | 70.4% |
| Claude Opus 5.5 (max) on Claude Max 20x | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (max) on Claude Max 5x | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (max) on Claude Pro | 0.0% | 0.0% | 4.3% | 0.0% | 0.0% | 9.5% | 9.7% |
| Claude Opus 5.5 (xhigh) on Claude Max 20x | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (xhigh) on Claude Max 5x | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (xhigh) on Claude Pro | 0.0% | 0.0% | 10.8% | 0.0% | 0.0% | 20.1% | 20.9% |
| Claude Sonnet 5.5 (max) on Claude Max 20x | 0.0% | — | — | — | — | — | — |
| Claude Sonnet 5.5 (max) on Claude Max 5x | 0.0% | — | — | — | — | — | — |
| Claude Sonnet 5.5 (max) on Claude Pro | 0.0% | — | — | — | — | — | — |
| GPT-6 Astra (high) on ChatGPT Plus | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (high) on ChatGPT Pro 100 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (high) on ChatGPT Pro 200 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 2.9% | 2.8% |
| GPT-6 Astra (high) on ChatGPT Pro 500 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (max) on ChatGPT Plus | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (max) on ChatGPT Pro 100 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (max) on ChatGPT Pro 200 | 100.0% | 100.0% | 81.0% | 100.0% | 100.0% | 37.6% | 38.8% |
| GPT-6 Astra (max) on ChatGPT Pro 500 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (xhigh) on ChatGPT Plus | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (xhigh) on ChatGPT Pro 100 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (xhigh) on ChatGPT Pro 200 | 0.0% | 0.0% | 15.7% | 0.0% | 0.0% | 36.8% | 37.3% |
| GPT-6 Astra (xhigh) on ChatGPT Pro 500 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Luna (high) on ChatGPT Plus | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (high) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (high) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (high) on ChatGPT Pro 500 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (high) on OpenCode Go | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (low) on ChatGPT Plus | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (low) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (low) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (low) on ChatGPT Pro 500 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (low) on OpenCode Go | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Plus | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 500 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (max) on OpenCode Go | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (medium) on ChatGPT Plus | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (medium) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (medium) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (medium) on ChatGPT Pro 500 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (medium) on OpenCode Go | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (xhigh) on ChatGPT Plus | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (xhigh) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (xhigh) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (xhigh) on ChatGPT Pro 500 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (xhigh) on OpenCode Go | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Sol (high) on ChatGPT Plus | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (high) on ChatGPT Pro 100 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (high) on ChatGPT Pro 200 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (high) on ChatGPT Pro 500 | 100.0% | 100.0% | 99.9% | 100.0% | 100.0% | 81.9% | 81.9% |
| GPT-6.1 Sol (low) on ChatGPT Plus | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (low) on ChatGPT Pro 100 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (low) on ChatGPT Pro 200 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (low) on ChatGPT Pro 500 | 0.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% |
| GPT-6.1 Sol (max) on ChatGPT Plus | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (max) on ChatGPT Pro 100 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (max) on ChatGPT Pro 200 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (max) on ChatGPT Pro 500 | 100.0% | 100.0% | 99.9% | 100.0% | 100.0% | 78.8% | 79.6% |
| GPT-6.1 Sol (medium) on ChatGPT Plus | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (medium) on ChatGPT Pro 100 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (medium) on ChatGPT Pro 200 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (medium) on ChatGPT Pro 500 | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% |
| GPT-6.1 Sol (xhigh) on ChatGPT Plus | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (xhigh) on ChatGPT Pro 100 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (xhigh) on ChatGPT Pro 200 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (xhigh) on ChatGPT Pro 500 | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 92.3% | 91.8% |
| GPT-6.1 Terra (high) on ChatGPT Plus | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Terra (high) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Terra (high) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Terra (high) on ChatGPT Pro 500 | 100.0% | — | — | — | — | — | — |
| GPT-6.1 Terra (low) on ChatGPT Plus | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Terra (low) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Terra (low) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Terra (low) on ChatGPT Pro 500 | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Terra (max) on ChatGPT Plus | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Terra (max) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Terra (max) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Terra (max) on ChatGPT Pro 500 | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Terra (medium) on ChatGPT Plus | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Terra (medium) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Terra (medium) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Terra (medium) on ChatGPT Pro 500 | 100.0% | — | — | — | — | — | — |
| GPT-6.1 Terra (xhigh) on ChatGPT Plus | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Terra (xhigh) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Terra (xhigh) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Terra (xhigh) on ChatGPT Pro 500 | 100.0% | — | — | — | — | — | — |

### Plan basis: value-score dispersion (SD; covariance term)

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M | S1T | S1T recentred |
|---|---:|---:|---:|---:|---:|---:|---:|
| Claude Fable 5.2 (high) on API-cost fallback | 0.00 (+0.00) | 0.00 (+0.00) | 1.04 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.34 (+0.00) | 1.35 (+0.00) |
| Claude Fable 5.2 (max) on API-cost fallback | 0.00 (+0.00) | 0.00 (+0.00) | 0.96 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.37 (+0.00) | 1.36 (+0.00) |
| Claude Fable 5.2 (xhigh) on API-cost fallback | 0.00 (+0.00) | 0.00 (+0.00) | 1.02 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.33 (+0.00) | 1.33 (+0.00) |
| Claude Haiku 5.5 (high) on Claude Max 20x | 0.00 (+0.00) | — | — | — | — | — | — |
| Claude Haiku 5.5 (high) on Claude Max 5x | 0.00 (+0.00) | — | — | — | — | — | — |
| Claude Haiku 5.5 (high) on Claude Pro | 0.00 (+0.00) | — | — | — | — | — | — |
| Claude Haiku 5.5 (high) on OpenCode Go | 0.00 (+0.00) | — | — | — | — | — | — |
| Claude Haiku 5.5 (low) on Claude Max 20x | 0.00 (+0.00) | — | — | — | — | — | — |
| Claude Haiku 5.5 (low) on Claude Max 5x | 0.00 (+0.00) | — | — | — | — | — | — |
| Claude Haiku 5.5 (low) on Claude Pro | 0.00 (+0.00) | — | — | — | — | — | — |
| Claude Haiku 5.5 (low) on OpenCode Go | 0.00 (+0.00) | — | — | — | — | — | — |
| Claude Haiku 5.5 (medium) on Claude Max 20x | 0.00 (+0.00) | — | — | — | — | — | — |
| Claude Haiku 5.5 (medium) on Claude Max 5x | 0.00 (+0.00) | — | — | — | — | — | — |
| Claude Haiku 5.5 (medium) on Claude Pro | 0.00 (+0.00) | — | — | — | — | — | — |
| Claude Haiku 5.5 (medium) on OpenCode Go | 0.00 (+0.00) | — | — | — | — | — | — |
| Claude Haiku 5.5 (xhigh) on Claude Max 20x | 0.00 (+0.00) | — | — | — | — | — | — |
| Claude Haiku 5.5 (xhigh) on Claude Max 5x | 0.00 (+0.00) | — | — | — | — | — | — |
| Claude Haiku 5.5 (xhigh) on Claude Pro | 0.00 (+0.00) | — | — | — | — | — | — |
| Claude Haiku 5.5 (xhigh) on OpenCode Go | 0.00 (+0.00) | — | — | — | — | — | — |
| Claude Opus 5.5 (high) on Claude Max 20x | 0.00 (+0.00) | 0.00 (+0.00) | 1.14 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.31 (+0.00) | 1.31 (+0.00) |
| Claude Opus 5.5 (high) on Claude Max 5x | 0.00 (+0.00) | 0.00 (+0.00) | 1.14 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.31 (+0.00) | 1.31 (+0.00) |
| Claude Opus 5.5 (high) on Claude Pro | 0.00 (+0.00) | 0.00 (+0.00) | 1.14 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.31 (+0.00) | 1.31 (+0.00) |
| Claude Opus 5.5 (max) on Claude Max 20x | 0.00 (+0.00) | 0.00 (+0.00) | 1.03 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.31 (+0.00) | 1.34 (+0.00) |
| Claude Opus 5.5 (max) on Claude Max 5x | 0.00 (+0.00) | 0.00 (+0.00) | 1.03 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.31 (+0.00) | 1.34 (+0.00) |
| Claude Opus 5.5 (max) on Claude Pro | 0.00 (+0.00) | 0.00 (+0.00) | 1.03 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.31 (+0.00) | 1.34 (+0.00) |
| Claude Opus 5.5 (xhigh) on Claude Max 20x | 0.00 (+0.00) | 0.00 (+0.00) | 1.04 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.33 (+0.00) | 1.31 (+0.00) |
| Claude Opus 5.5 (xhigh) on Claude Max 5x | 0.00 (+0.00) | 0.00 (+0.00) | 1.04 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.33 (+0.00) | 1.31 (+0.00) |
| Claude Opus 5.5 (xhigh) on Claude Pro | 0.00 (+0.00) | 0.00 (+0.00) | 1.04 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.33 (+0.00) | 1.31 (+0.00) |
| Claude Sonnet 5.5 (max) on Claude Max 20x | 0.00 (+0.00) | — | — | — | — | — | — |
| Claude Sonnet 5.5 (max) on Claude Max 5x | 0.00 (+0.00) | — | — | — | — | — | — |
| Claude Sonnet 5.5 (max) on Claude Pro | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6 Astra (high) on ChatGPT Plus | 0.00 (+0.00) | 0.00 (+0.00) | 0.87 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.40 (+0.00) | 1.39 (+0.00) |
| GPT-6 Astra (high) on ChatGPT Pro 100 | 0.00 (+0.00) | 0.00 (+0.00) | 0.87 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.40 (+0.00) | 1.39 (+0.00) |
| GPT-6 Astra (high) on ChatGPT Pro 200 | 0.00 (+0.00) | 0.00 (+0.00) | 0.87 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.40 (+0.00) | 1.39 (+0.00) |
| GPT-6 Astra (high) on ChatGPT Pro 500 | 0.00 (+0.00) | 0.00 (+0.00) | 0.87 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.40 (+0.00) | 1.39 (+0.00) |
| GPT-6 Astra (max) on ChatGPT Plus | 0.00 (+0.00) | 0.00 (+0.00) | 0.96 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.44 (+0.00) | 1.43 (+0.00) |
| GPT-6 Astra (max) on ChatGPT Pro 100 | 0.00 (+0.00) | 0.00 (+0.00) | 0.96 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.44 (+0.00) | 1.43 (+0.00) |
| GPT-6 Astra (max) on ChatGPT Pro 200 | 0.00 (+0.00) | 0.00 (+0.00) | 0.96 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.44 (+0.00) | 1.43 (+0.00) |
| GPT-6 Astra (max) on ChatGPT Pro 500 | 0.00 (+0.00) | 0.00 (+0.00) | 0.96 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.44 (+0.00) | 1.43 (+0.00) |
| GPT-6 Astra (xhigh) on ChatGPT Plus | 0.00 (+0.00) | 0.00 (+0.00) | 0.94 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.43 (+0.00) | 1.42 (+0.00) |
| GPT-6 Astra (xhigh) on ChatGPT Pro 100 | 0.00 (+0.00) | 0.00 (+0.00) | 0.94 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.43 (+0.00) | 1.42 (+0.00) |
| GPT-6 Astra (xhigh) on ChatGPT Pro 200 | 0.00 (+0.00) | 0.00 (+0.00) | 0.94 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.43 (+0.00) | 1.42 (+0.00) |
| GPT-6 Astra (xhigh) on ChatGPT Pro 500 | 0.00 (+0.00) | 0.00 (+0.00) | 0.94 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.43 (+0.00) | 1.42 (+0.00) |
| GPT-6 Luna (high) on ChatGPT Plus | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6 Luna (high) on ChatGPT Pro 100 | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6 Luna (high) on ChatGPT Pro 200 | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6 Luna (high) on ChatGPT Pro 500 | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6 Luna (high) on OpenCode Go | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6 Luna (low) on ChatGPT Plus | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6 Luna (low) on ChatGPT Pro 100 | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6 Luna (low) on ChatGPT Pro 200 | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6 Luna (low) on ChatGPT Pro 500 | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6 Luna (low) on OpenCode Go | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Plus | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 100 | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 200 | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 500 | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6 Luna (max) on OpenCode Go | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6 Luna (medium) on ChatGPT Plus | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6 Luna (medium) on ChatGPT Pro 100 | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6 Luna (medium) on ChatGPT Pro 200 | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6 Luna (medium) on ChatGPT Pro 500 | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6 Luna (medium) on OpenCode Go | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6 Luna (xhigh) on ChatGPT Plus | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6 Luna (xhigh) on ChatGPT Pro 100 | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6 Luna (xhigh) on ChatGPT Pro 200 | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6 Luna (xhigh) on ChatGPT Pro 500 | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6 Luna (xhigh) on OpenCode Go | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6.1 Sol (high) on ChatGPT Plus | 0.00 (+0.00) | 0.00 (+0.00) | 0.91 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.39 (+0.00) | 1.40 (+0.00) |
| GPT-6.1 Sol (high) on ChatGPT Pro 100 | 0.00 (+0.00) | 0.00 (+0.00) | 0.91 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.39 (+0.00) | 1.40 (+0.00) |
| GPT-6.1 Sol (high) on ChatGPT Pro 200 | 0.00 (+0.00) | 0.00 (+0.00) | 0.91 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.39 (+0.00) | 1.40 (+0.00) |
| GPT-6.1 Sol (high) on ChatGPT Pro 500 | 0.00 (+0.00) | 0.00 (+0.00) | 0.91 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.39 (+0.00) | 1.40 (+0.00) |
| GPT-6.1 Sol (low) on ChatGPT Plus | 0.00 (+0.00) | 0.00 (+0.00) | 1.23 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.22 (+0.00) | 1.22 (+0.00) |
| GPT-6.1 Sol (low) on ChatGPT Pro 100 | 0.00 (+0.00) | 0.00 (+0.00) | 1.23 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.22 (+0.00) | 1.22 (+0.00) |
| GPT-6.1 Sol (low) on ChatGPT Pro 200 | 0.00 (+0.00) | 0.00 (+0.00) | 1.23 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.22 (+0.00) | 1.22 (+0.00) |
| GPT-6.1 Sol (low) on ChatGPT Pro 500 | 0.00 (+0.00) | 0.00 (+0.00) | 1.23 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.22 (+0.00) | 1.22 (+0.00) |
| GPT-6.1 Sol (max) on ChatGPT Plus | 0.00 (+0.00) | 0.00 (+0.00) | 1.12 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.45 (+0.00) | 1.47 (+0.00) |
| GPT-6.1 Sol (max) on ChatGPT Pro 100 | 0.00 (+0.00) | 0.00 (+0.00) | 1.12 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.45 (+0.00) | 1.47 (+0.00) |
| GPT-6.1 Sol (max) on ChatGPT Pro 200 | 0.00 (+0.00) | 0.00 (+0.00) | 1.12 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.45 (+0.00) | 1.47 (+0.00) |
| GPT-6.1 Sol (max) on ChatGPT Pro 500 | 0.00 (+0.00) | 0.00 (+0.00) | 1.12 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.45 (+0.00) | 1.47 (+0.00) |
| GPT-6.1 Sol (medium) on ChatGPT Plus | 0.00 (+0.00) | 0.00 (+0.00) | 0.97 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.36 (+0.00) | 1.34 (+0.00) |
| GPT-6.1 Sol (medium) on ChatGPT Pro 100 | 0.00 (+0.00) | 0.00 (+0.00) | 0.97 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.36 (+0.00) | 1.34 (+0.00) |
| GPT-6.1 Sol (medium) on ChatGPT Pro 200 | 0.00 (+0.00) | 0.00 (+0.00) | 0.97 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.36 (+0.00) | 1.34 (+0.00) |
| GPT-6.1 Sol (medium) on ChatGPT Pro 500 | 0.00 (+0.00) | 0.00 (+0.00) | 0.97 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.36 (+0.00) | 1.34 (+0.00) |
| GPT-6.1 Sol (xhigh) on ChatGPT Plus | 0.00 (+0.00) | 0.00 (+0.00) | 1.03 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.44 (+0.00) | 1.43 (+0.00) |
| GPT-6.1 Sol (xhigh) on ChatGPT Pro 100 | 0.00 (+0.00) | 0.00 (+0.00) | 1.03 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.44 (+0.00) | 1.43 (+0.00) |
| GPT-6.1 Sol (xhigh) on ChatGPT Pro 200 | 0.00 (+0.00) | 0.00 (+0.00) | 1.03 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.44 (+0.00) | 1.43 (+0.00) |
| GPT-6.1 Sol (xhigh) on ChatGPT Pro 500 | 0.00 (+0.00) | 0.00 (+0.00) | 1.03 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.44 (+0.00) | 1.43 (+0.00) |
| GPT-6.1 Terra (high) on ChatGPT Plus | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6.1 Terra (high) on ChatGPT Pro 100 | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6.1 Terra (high) on ChatGPT Pro 200 | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6.1 Terra (high) on ChatGPT Pro 500 | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6.1 Terra (low) on ChatGPT Plus | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6.1 Terra (low) on ChatGPT Pro 100 | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6.1 Terra (low) on ChatGPT Pro 200 | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6.1 Terra (low) on ChatGPT Pro 500 | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6.1 Terra (max) on ChatGPT Plus | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6.1 Terra (max) on ChatGPT Pro 100 | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6.1 Terra (max) on ChatGPT Pro 200 | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6.1 Terra (max) on ChatGPT Pro 500 | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6.1 Terra (medium) on ChatGPT Plus | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6.1 Terra (medium) on ChatGPT Pro 100 | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6.1 Terra (medium) on ChatGPT Pro 200 | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6.1 Terra (medium) on ChatGPT Pro 500 | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6.1 Terra (xhigh) on ChatGPT Plus | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6.1 Terra (xhigh) on ChatGPT Pro 100 | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6.1 Terra (xhigh) on ChatGPT Pro 200 | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6.1 Terra (xhigh) on ChatGPT Pro 500 | 0.00 (+0.00) | — | — | — | — | — | — |

### Named S2 specification branches

- **Bug Hunt harness band (E19)** (S2): unevaluable; the captured tbench.ai leaderboard lists no configuration under two or more agents, so no cross-agent spread exists
- **cache-hit variation (E34)** (S2): unevaluable; AA's published cost embeds its cache-pricing protocol; varying the cache-hit rate needs each basket component's cache-read and uncached-input demand, which AA publishes only for the whole Index (E157)
- **first-party list versus cross-provider median price rule (E122)** (S2): unevaluable; AA publishes one price per configuration under its own rule; the alternative rule's prices are not captured

### Common-leaf ranking (diagnostic): diagnostics

- **Terminal-Bench cross-source agreement (AA's mini-SWE-agent run against tbench.ai):** defined; 0 rows take the leaf from tbench.ai (gap fill).
- **Workload cross-check (E41, mandatory diagnostic):** Terminal-Bench 4.1 cost per solved task on AA's own execution against basket cost: τ_b 0.53 (interval 0.18 to 0.81), uncertain agreement; panel (29): Claude Fable 5.2 (max), Claude Fable 5.2 (high), Claude Fable 5.2 (xhigh), Claude Haiku 5.5 (xhigh), Claude Haiku 5.5 (high), Claude Haiku 5.5 (low), Claude Haiku 5.5 (medium), Claude Opus 5.5 (max), Claude Opus 5.5 (high), Claude Opus 5.5 (xhigh), Claude Sonnet 5.5 (max), GPT-6 Astra (max), GPT-6 Astra (high), GPT-6 Astra (xhigh), GPT-6 Luna (max), GPT-6 Luna (high), GPT-6 Luna (low), GPT-6 Luna (medium), GPT-6 Luna (xhigh), GPT-6.1 Sol (max), GPT-6.1 Sol (high), GPT-6.1 Sol (low), GPT-6.1 Sol (medium), GPT-6.1 Sol (xhigh), GPT-6.1 Terra (max), GPT-6.1 Terra (high), GPT-6.1 Terra (low), GPT-6.1 Terra (medium), GPT-6.1 Terra (xhigh).
- **Rank separability (O39, independent-task approximation):** median separation 3.67 value points (API) and 3.61 (Plan); separable adjacent ranks: API 0 of 28, Plan 1 of 55. Assumptions: tasks are independent and each leaf's score is a mean over its published task count (a binomial leaf drawn from its Jeffreys posterior Beta(k + 1/2, n - k + 1/2), O142; plug-in SDs with the proportion (k + 1/2) / (n + 1), I28); attempts averaged within a task and tasks shared across models are ignored, so the noise is approximate; GDPval-AA: each row's rating interval as AA's model page displays it, read as a 95% normal interval (AA states no level), SD = half-width / 1.96; AA-Omniscience: each of 3,000 questions scores +1, 0 or -1, with the shares from AA's accuracy and hallucination rate; Vals boards (Vibe Code Bench v1.1, Code Migration v1.1): Vals' published standard error per record, read as the leaf's SD; AI Coding Daily: judged points over its seven graded projects read as a binomial share of 80 points (an assumption; the board publishes no error).
- **FrontierCode against Cognition:** FrontierCode 2.0 cross-source agreement (AA against Cognition, exact model and effort; E234, O153): Kendall tau 0.91 (interval 0.81 to 0.98) on 22 rows. Cognition minus AA: mean +0.2 points, largest 3.9.
- **Gap-fill removal (E234, diagnostic):** no ranked row has a leaf from another party or the provider.
- **Bar results without the gap fills (E234, sensitivity; labels unchanged):** cheapest displayed row as published, with fills removed, and with third-party fills third-party fills minus the signed mean offset +0.2 points (third party minus AA) — API quality 48.2: GPT-6.1 Sol (medium) in all three; API quality 30.6: GPT-6.1 Terra (low) in all three; API quality 56.0: GPT-6.1 Sol (xhigh) in all three; Plan quality 48.2: GPT-6.1 Sol (medium) in all three; Plan quality 30.6: Claude Haiku 5.5 (xhigh) in all three; Plan quality 56.0: GPT-6.1 Sol (xhigh) in all three.
- **Harness cost (O123, S2 stress):** agent effects on log cost (Claude Code -0.08, Codex -0.03, DeepSeek Harness +0.36, Devin CLI -0.10, GitHub Copilot -0.25, Grok Build +0.15, Kimi Code CLI +0.22, Mistral Vibe -0.17, Muse Code +0.70, OpenCode -0.11, Pi -0.48, Qwen Code -0.14, mini-swe-agent -0.08); API ranks with each agent's effect removed: GPT-6.1 Sol (max) 1; GPT-6.1 Sol (xhigh) 2; GPT-6.1 Terra (max) 3; GPT-6.1 Sol (high) 4; GPT-6 Astra (xhigh) 5; GPT-6 Astra (max) 6; GPT-6.1 Sol (medium) 7; Claude Fable 5.2 (max) 8; Claude Fable 5.2 (high) 9; GPT-6 Astra (high) 10; Claude Sonnet 5.5 (max) 11; Claude Fable 5.2 (xhigh) 12; GPT-6.1 Terra (xhigh) 13; Claude Opus 5.5 (xhigh) 14; GPT-6.1 Terra (high) 15; Claude Opus 5.5 (max) 16; Claude Opus 5.5 (high) 17; GPT-6.1 Terra (medium) 18; GPT-6.1 Sol (low) 19; Claude Haiku 5.5 (xhigh) 20; GPT-6 Luna (max) 21; GPT-6.1 Terra (low) 22; Claude Haiku 5.5 (high) 23; GPT-6 Luna (xhigh) 24; GPT-6 Luna (high) 25; Claude Haiku 5.5 (medium) 26; GPT-6 Luna (medium) 27; Claude Haiku 5.5 (low) 28; GPT-6 Luna (low) 29. Coding Agent Index agents (each part of its costed configuration; none is the run behind the FrontierCode or Terminal-Bench leaf): GPT-6.1 Sol (max): Codex; Claude Opus 5.5 (max): Claude Code; GPT-6 Astra (max): Codex; GPT-6.1 Terra (max): Codex; Claude Sonnet 5.5 (max): Claude Code; GPT-6 Luna (max): Codex; Claude Fable 5.2 (high): Claude Code; Claude Fable 5.2 (max): Claude Code; Claude Fable 5.2 (xhigh): Claude Code.
- **Quality agreement:** quality agreement (matched-panel sensitivity): Kendall tau 0.72 (interval 0.61 to 0.82) on 29 rows.
- **Quality-substitution value agreement (API):** quality-substitution value agreement, api basis (matched-panel sensitivity): Kendall tau 0.65 (interval 0.47 to 0.81) on 29 rows.
- **Quality-substitution value agreement (Plan):** quality-substitution value agreement, plan basis (matched-panel sensitivity): Kendall tau 0.55 (interval 0.32 to 0.75) on 29 rows.
- **Disjoint-evidence agreement:** disjoint-evidence agreement (restricted evidence comparison, not an eligible ranking): Kendall tau 0.60 (interval 0.43 to 0.73) on 29 rows.
- **Quality source shares:** AA-run 85%, independent 15%.
- **Non-discriminating leaves:** lcr.
- **Group drift:** estimated; flagged: none.
- **Omniscience abstention sensitivity** (z_pen = max(0, I)): 11 rows move; largest move 2 (Claude Fable 5.2 (xhigh)).
- **GDPval-AA logistic sensitivity** (z = 100 / (1 + 10^((1600 - E) / 400)) against AA's pinned anchor; every other input fixed): API 9 rows move; largest move 2 (Claude Opus 5.5 (max), GPT-6 Astra (high), GPT-6.1 Terra (xhigh)); Plan 13 rows move; largest move 2 (GPT-6.1 Sol (high)).
- **Anchor stability:** trimmed anchors (P10 / 2 and P90 x 2 (diagnostic only)) give $29.40 to $9,425.07; 19 rows move; largest move 7 (GPT-6.1 Terra (high)).

- **Basket readiness (E22):** priced leaves cover 62% of nominal quality weight (AutomationBench-AA, FrontierCode 2.0, GDP.pdf (AA), Terminal-Bench-Science 0.1, Terminal-Bench 4.1 (AA run)); pending components: Coding Agent Index, ITBench-AA.
- **SWE cost companion (O14, diagnostic):** 9 rows evaluated; flagged far from the median ratio: none.
- **Matched-cost diagnostic (E55):** evaluated at 75% priced quality weight; basket/matched cost-order reversals with separated intervals: 1; rank-gap warnings: 0.
- **Frontier-families anchors (E187, diagnostic):** anchors rebuilt from the 13 frontier and near-frontier references move API no rank changes (value points per cost doubling 2.12 vs 2.12 frozen); Plan 25 rows move; largest move 10 (GPT-6 Astra (high), GPT-6 Astra (xhigh)) (value points per cost doubling 6.51 vs 3.66 frozen).
- **Frontier-families bar (E199, sensitivity; the frozen bar stays primary):** quality 38.1 over 16 configurations; cheapest at or above it on the API main workload: not unique; possibly GPT-6.1 Terra (high), GPT-6.1 Terra (medium) (compares 15 configurations that can qualify and 3 blocker(s) that can qualify but earn no label (E315)).
- **One row per family (E205, diagnostic; the frozen ladder and anchors stay primary):** with each family's primary configuration only (6 rows in the one-row-per-family bar population), the ladder (headline, lower quartile, upper quartile) would be 41.8 / 24.6 / 48.2 against 48.2 / 30.6 / 56.0 frozen; anchors rebuilt from its 5 references move API 16 rows move; largest move 6 (GPT-6.1 Terra (high)) (value points per cost doubling 2.79 vs 2.12 frozen); Plan 25 rows move; largest move 10 (GPT-6 Astra (high), GPT-6 Astra (xhigh)) (value points per cost doubling 6.51 vs 3.66 frozen).
- **Ladder over scored rows (I28, sensitivity; the frozen ladder stays primary):** the bar population keeps full-benchmark rows that have no cost; today every such row has a cost, so the ladder is unchanged.
- **Bar currency (E207, informational):** rows reaching each frozen bar: quality 48.2: 15 of 29; quality 30.6: 22 of 29; quality 56.0: 8 of 29; the current population would freeze 48.2 / 30.6 / 56.0; lifetime until the next anchor re-freeze or methodology version, whichever comes first; no staleness flag.
- **Token mix (E208):** 26 selected routes: mix unidentified: the basket's token-category shares are set-identified only (E124), so the L1 test (above 0.30 flags mix-unmatched) is not computed.
- **Observed-range sensitivity (E219, not evidence; no label changes):** with each missing leaf inside the cohort's observed range for that leaf, quality 48.2: 12 can qualify, 11 confirmed; possibly cheapest GPT-6.1 Sol (high), GPT-6.1 Sol (medium); quality 30.6: 18 can qualify, 17 confirmed; possibly cheapest GPT-6 Luna (max), GPT-6.1 Terra (low); quality 56.0: 5 can qualify, 4 confirmed; possibly cheapest GPT-6.1 Sol (max), GPT-6.1 Sol (xhigh).
- **What would settle the headline bar (E221, not a claim):** rows that can but need not reach quality 48.2, with the mean score their missing leaves would need: GPT-6.1 Sol (medium) (no missing leaf; reporting precision only).
- **Common leaf set (E226, diagnostic; scores unchanged):** without the leaves fewer than 90% of the ranking's ranked rows have (none), API no rank changes; Plan no rank changes; rows reaching each bar: quality 48.2: 15 → 15; quality 30.6: 22 → 22; quality 56.0: 8 → 8; rows whose displayed quality differs from common-leaf quality by more than one cost doubling's worth: none.
- **Harness by leaf (E227):** Terminal-Bench: mini-SWE-agent 29; Bug Hunt: Codex CLI 18, Claude Code 11.
- **Coding Agent Index safety refusals (O63, flagged; costs and scores unchanged):** GPT-6.1 Sol (max) (15 blocked of 966 attempts); Claude Opus 5.5 (max) (77 finished by Claude Opus 4.8 or Claude Opus 5 of 966 attempts); GPT-6 Astra (max) (13 blocked of 966 attempts); Claude Sonnet 5.5 (45 finished by Claude Opus 4.8 of 966 attempts); Claude Fable 5.2 (high) (51 finished by Claude Opus 4.8 or Claude Opus 5 of 966 attempts); Claude Fable 5.2 (max) (63 finished by Claude Opus 4.8 or Claude Opus 5 of 966 attempts); Claude Fable 5.2 (xhigh) (55 finished by Claude Opus 4.8 or Claude Opus 5 of 966 attempts).

### Leave-one-component-out cost family (E172)

Each admitted basket unit removed in turn, scored on anchors rebuilt by the freeze rule (rank changes against the primary ranking; quality held fixed).

| Removed component | API rank changes | Plan rank changes | API value points per cost doubling |
|---|---|---|---:|
| AA-Briefcase | 6 rows move; largest move 1 (Claude Haiku 5.5 (low), Claude Opus 5.5 (max), Claude Opus 5.5 (xhigh), GPT-6 Luna (medium), GPT-6.1 Terra (high), GPT-6.1 Terra (xhigh)) | 14 rows move; largest move 4 (GPT-6 Astra (xhigh)) | 2.19 |
| GDP.pdf | 5 rows move; largest move 2 (GPT-6 Luna (low)) | 16 rows move; largest move 4 (GPT-6 Astra (xhigh)) | 2.07 |
| AutomationBench-AA | 11 rows move; largest move 2 (Claude Haiku 5.5 (xhigh), GPT-6 Luna (low), GPT-6.1 Terra (low)) | 16 rows move; largest move 4 (Claude Haiku 5.5 (xhigh), GPT-6 Astra (max)) | 1.99 |
| Terminal-Bench 4.1 (AA Index run) | 4 rows move; largest move 1 (Claude Haiku 5.5 (low), GPT-6 Astra (max), GPT-6 Luna (medium), GPT-6.1 Sol (medium)) | 14 rows move; largest move 4 (GPT-6 Astra (xhigh)) | 2.14 |
| FrontierCode 2.0 | 4 rows move; largest move 1 (Claude Fable 5.2 (xhigh), Claude Sonnet 5.5 (max), GPT-6 Astra (max), GPT-6.1 Sol (medium)) | 11 rows move; largest move 4 (GPT-6 Astra (xhigh)) | 2.16 |
| Terminal-Bench-Science | no rank changes | 13 rows move; largest move 4 (GPT-6 Astra (xhigh)) | 2.16 |

### Subset rows: paired bridge and missing spend (E10, E173)

No row is scored on a subset workload.

### Deletion sensitivity

| Branch | Retained nominal weight | Status | API rank changes | Plan rank changes |
|---|---:|---|---|---|
| leave-out:frontierCode | 75% | evaluated | 15 rows move; largest move 3 (GPT-6.1 Terra (high)) | 23 rows move; largest move 4 (GPT-6.1 Sol (low), GPT-6.1 Terra (high)) |
| leave-out:terminalBench | 80% | evaluated | 20 rows move; largest move 3 (Claude Opus 5.5 (high), GPT-6 Luna (max)) | 20 rows move; largest move 8 (GPT-6 Luna (max)) |
| leave-out:bugHunt | 85% | evaluated | 19 rows move; largest move 8 (GPT-6 Astra (max), GPT-6.1 Terra (high)) | 20 rows move; largest move 9 (GPT-6.1 Sol (max)) |
| leave-out:gdpval | 95% | evaluated | 6 rows move; largest move 1 (Claude Fable 5.2 (xhigh), Claude Haiku 5.5 (low), Claude Opus 5.5 (xhigh), Claude Sonnet 5.5 (max), GPT-6 Luna (medium), GPT-6.1 Terra (high)) | 9 rows move; largest move 2 (GPT-6.1 Sol (medium)) |
| leave-out:gdpPdf | 95% | evaluated | 9 rows move; largest move 2 (Claude Fable 5.2 (xhigh)) | 14 rows move; largest move 1 (Claude Fable 5.2 (max), Claude Fable 5.2 (xhigh), Claude Haiku 5.5 (xhigh), Claude Haiku 5.5 (high), Claude Haiku 5.5 (low), Claude Opus 5.5 (xhigh), Claude Sonnet 5.5 (max), GPT-6 Astra (max), GPT-6 Astra (high), GPT-6 Luna (medium), GPT-6 Luna (xhigh), GPT-6.1 Terra (high), GPT-6.1 Terra (medium), GPT-6.1 Terra (xhigh)) |
| leave-out:automationBench | 90% | evaluated | 11 rows move; largest move 2 (Claude Haiku 5.5 (medium), GPT-6 Luna (low), GPT-6 Luna (medium)) | 11 rows move; largest move 2 (Claude Haiku 5.5 (xhigh), Claude Haiku 5.5 (medium), GPT-6.1 Terra (medium)) |
| leave-out:omniscience | 90% | evaluated | 8 rows move; largest move 2 (Claude Fable 5.2 (high), Claude Sonnet 5.5 (max)) | 10 rows move; largest move 1 (Claude Fable 5.2 (high), Claude Opus 5.5 (xhigh), Claude Sonnet 5.5 (max), GPT-6 Astra (max), GPT-6 Luna (max), GPT-6 Luna (high), GPT-6.1 Sol (low), GPT-6.1 Terra (high), GPT-6.1 Terra (medium), GPT-6.1 Terra (xhigh)) |
| leave-out:lcr | 95% | evaluated | 4 rows move; largest move 1 (Claude Haiku 5.5 (low), Claude Opus 5.5 (max), GPT-6 Luna (medium), GPT-6.1 Terra (high)) | 14 rows move; largest move 1 (Claude Fable 5.2 (max), Claude Fable 5.2 (xhigh), Claude Haiku 5.5 (xhigh), Claude Haiku 5.5 (high), Claude Haiku 5.5 (low), Claude Opus 5.5 (xhigh), Claude Sonnet 5.5 (max), GPT-6 Astra (max), GPT-6 Astra (high), GPT-6 Luna (medium), GPT-6 Luna (xhigh), GPT-6.1 Terra (high), GPT-6.1 Terra (medium), GPT-6.1 Terra (xhigh)) |
| leave-out:hle | 98% | evaluated | 2 rows move; largest move 1 (GPT-6 Astra (max), GPT-6.1 Sol (medium)) | 8 rows move; largest move 2 (Claude Fable 5.2 (high), GPT-6 Astra (xhigh)) |
| leave-out:tbScience | 98% | evaluated | 2 rows move; largest move 1 (GPT-6 Astra (max), GPT-6.1 Sol (medium)) | 7 rows move; largest move 2 (Claude Fable 5.2 (high)) |
| leave-out:critpt | 98% | evaluated | 4 rows move; largest move 1 (Claude Haiku 5.5 (low), Claude Opus 5.5 (max), GPT-6 Luna (medium), GPT-6.1 Terra (high)) | 8 rows move; largest move 1 (Claude Fable 5.2 (high), Claude Haiku 5.5 (low), Claude Opus 5.5 (xhigh), Claude Sonnet 5.5 (max), GPT-6 Luna (high), GPT-6 Luna (medium), GPT-6.1 Terra (high), GPT-6.1 Terra (xhigh)) |
| leave-source-out:Artificial Analysis | 15% | not identifiable under the coverage rule | — | — |
| basket-scope | 87% | evaluated | 11 rows move; largest move 3 (Claude Sonnet 5.5 (max)) | 12 rows move; largest move 2 (Claude Sonnet 5.5 (max), GPT-6 Luna (high)) |

### Cost-component removal (Terminal-Bench 4.1 (AA Index run): evaluated)

| Basis | Run | Rank changes |
|---|---|---|
| api | cost-component removal, original anchors | 2 rows move; largest move 1 (Claude Haiku 5.5 (low), GPT-6 Luna (medium)) |
| api | alternative workload, recalibrated anchors | 4 rows move; largest move 1 (Claude Haiku 5.5 (low), GPT-6 Astra (max), GPT-6 Luna (medium), GPT-6.1 Sol (medium)) |
| plan | cost-component removal, original anchors; fixed-multiple arithmetic stress (not identified Plan economics for the altered workload) | 5 rows move; largest move 2 (GPT-6.1 Terra (xhigh)) |
| plan | alternative workload, recalibrated anchors; fixed-multiple arithmetic stress (not identified Plan economics for the altered workload) | 14 rows move; largest move 4 (GPT-6 Astra (xhigh)) |

### Common-leaf ranking (diagnostic): release gates

| Rule | Status | Detail |
|---|---|---|
| clip gate (E20) | passed | no basis exceeds the clipping allowance |
| cost influence flag (E91) | passed | cost not discriminating (< 10%); informational only; beta never changes (O2) |
| realised influence (E272) | fired | API: cost term offsetting (-78% of value variance); Plan: cost term offsetting (-35% of value variance); informational only, beta never changes (O2) |
| quality influence flag (E126) | passed | quality not discriminating (cost share > 90%); informational only |
| subset scoring (O17) | vacuous | subset rows scored on their own workload and anchors |
| partial component flag (E37) | vacuous | AA declined- or missing-task markers, or an Index reconstruction that misses AA's total (E209) |
| route dominance filter (E88) | vacuous | certifiably dearer routes set aside |
| Plan exploratory label (E61) | fired | fewer than half of Plan rows have an identified M_W |
| Plan evidence lifecycle and change detection (E18, E151, E269, O77, O79) | fired | 96 of 108 plan rows carry a possibly-superseded or expired route: claude-haiku-5-5-high@claude-max-20x, claude-haiku-5-5-high@claude-max-5x, claude-haiku-5-5-high@claude-pro, claude-haiku-5-5-low@claude-max-20x, claude-haiku-5-5-low@claude-max-5x, claude-haiku-5-5-low@claude-pro, claude-haiku-5-5-medium@claude-max-20x, claude-haiku-5-5-medium@claude-max-5x, claude-haiku-5-5-medium@claude-pro, claude-haiku-5-5@claude-max-20x, claude-haiku-5-5@claude-max-5x, claude-haiku-5-5@claude-pro, claude-opus-5-5-high@claude-max-20x, claude-opus-5-5-high@claude-max-5x, claude-opus-5-5-high@claude-pro, claude-opus-5-5-xhigh@claude-max-20x, claude-opus-5-5-xhigh@claude-max-5x, claude-opus-5-5-xhigh@claude-pro, claude-opus-5-5@claude-max-20x, claude-opus-5-5@claude-max-5x, claude-opus-5-5@claude-pro, claude-sonnet-5-5@claude-max-20x, claude-sonnet-5-5@claude-max-5x, claude-sonnet-5-5@claude-pro, gpt-6-astra-high@chatgpt-plus, gpt-6-astra-high@chatgpt-pro-100, gpt-6-astra-high@chatgpt-pro-200, gpt-6-astra-high@chatgpt-pro-500, gpt-6-astra-xhigh@chatgpt-plus, gpt-6-astra-xhigh@chatgpt-pro-100, gpt-6-astra-xhigh@chatgpt-pro-200, gpt-6-astra-xhigh@chatgpt-pro-500, gpt-6-astra@chatgpt-plus, gpt-6-astra@chatgpt-pro-100, gpt-6-astra@chatgpt-pro-200, gpt-6-astra@chatgpt-pro-500, gpt-6-luna-high@chatgpt-plus, gpt-6-luna-high@chatgpt-pro-100, gpt-6-luna-high@chatgpt-pro-200, gpt-6-luna-high@chatgpt-pro-500, gpt-6-luna-low@chatgpt-plus, gpt-6-luna-low@chatgpt-pro-100, gpt-6-luna-low@chatgpt-pro-200, gpt-6-luna-low@chatgpt-pro-500, gpt-6-luna-medium@chatgpt-plus, gpt-6-luna-medium@chatgpt-pro-100, gpt-6-luna-medium@chatgpt-pro-200, gpt-6-luna-medium@chatgpt-pro-500, gpt-6-luna-xhigh@chatgpt-plus, gpt-6-luna-xhigh@chatgpt-pro-100, gpt-6-luna-xhigh@chatgpt-pro-200, gpt-6-luna-xhigh@chatgpt-pro-500, gpt-6-luna@chatgpt-plus, gpt-6-luna@chatgpt-pro-100, gpt-6-luna@chatgpt-pro-200, gpt-6-luna@chatgpt-pro-500, gpt-6.1-sol-high@chatgpt-plus, gpt-6.1-sol-high@chatgpt-pro-100, gpt-6.1-sol-high@chatgpt-pro-200, gpt-6.1-sol-high@chatgpt-pro-500, gpt-6.1-sol-low@chatgpt-plus, gpt-6.1-sol-low@chatgpt-pro-100, gpt-6.1-sol-low@chatgpt-pro-200, gpt-6.1-sol-low@chatgpt-pro-500, gpt-6.1-sol-medium@chatgpt-plus, gpt-6.1-sol-medium@chatgpt-pro-100, gpt-6.1-sol-medium@chatgpt-pro-200, gpt-6.1-sol-medium@chatgpt-pro-500, gpt-6.1-sol-xhigh@chatgpt-plus, gpt-6.1-sol-xhigh@chatgpt-pro-100, gpt-6.1-sol-xhigh@chatgpt-pro-200, gpt-6.1-sol-xhigh@chatgpt-pro-500, gpt-6.1-sol@chatgpt-plus, gpt-6.1-sol@chatgpt-pro-100, gpt-6.1-sol@chatgpt-pro-200, gpt-6.1-sol@chatgpt-pro-500, gpt-6.1-terra-high@chatgpt-plus, gpt-6.1-terra-high@chatgpt-pro-100, gpt-6.1-terra-high@chatgpt-pro-200, gpt-6.1-terra-high@chatgpt-pro-500, gpt-6.1-terra-low@chatgpt-plus, gpt-6.1-terra-low@chatgpt-pro-100, gpt-6.1-terra-low@chatgpt-pro-200, gpt-6.1-terra-low@chatgpt-pro-500, gpt-6.1-terra-medium@chatgpt-plus, gpt-6.1-terra-medium@chatgpt-pro-100, gpt-6.1-terra-medium@chatgpt-pro-200, gpt-6.1-terra-medium@chatgpt-pro-500, gpt-6.1-terra-xhigh@chatgpt-plus, gpt-6.1-terra-xhigh@chatgpt-pro-100, gpt-6.1-terra-xhigh@chatgpt-pro-200, gpt-6.1-terra-xhigh@chatgpt-pro-500, gpt-6.1-terra@chatgpt-plus, gpt-6.1-terra@chatgpt-pro-100, gpt-6.1-terra@chatgpt-pro-200, gpt-6.1-terra@chatgpt-pro-500 |
| acknowledged accounting-fault windows (O91, O92, O93, O95, O96) | fired | 18 of 108 plan rows rest on a measurement inside an acknowledged fault window; they stay selected and yield to two concordant user reports for their own model and plan, and the transfers resting on them follow: gpt-6-astra-high@chatgpt-pro-500, gpt-6-astra-xhigh@chatgpt-pro-500, gpt-6-astra@chatgpt-pro-500, gpt-6-luna-high@chatgpt-pro-500, gpt-6-luna-low@chatgpt-pro-500, gpt-6-luna-medium@chatgpt-pro-500, gpt-6-luna-xhigh@chatgpt-pro-500, gpt-6-luna@chatgpt-pro-500, gpt-6.1-sol-high@chatgpt-pro-500, gpt-6.1-sol-low@chatgpt-pro-500, gpt-6.1-sol-medium@chatgpt-pro-500, gpt-6.1-sol-xhigh@chatgpt-pro-500, gpt-6.1-sol@chatgpt-pro-500, gpt-6.1-terra-high@chatgpt-pro-500, gpt-6.1-terra-low@chatgpt-pro-500, gpt-6.1-terra-medium@chatgpt-pro-500, gpt-6.1-terra-xhigh@chatgpt-pro-500, gpt-6.1-terra@chatgpt-pro-500 |
| AA cost omits a pricing term (O94, O98, O100, O106, O108, O109, O114) | fired | ranked at the published cost; compete in interval outputs and the scenario labels' BlockerSafe test over [C, factor × C] ([C, ∞) without a stated factor, O98) without a label (scenario frequencies draw them at the published cost, O114), and leave the anchor population at the next freeze: claude-haiku-5-5 (up to 5×), claude-haiku-5-5-high (up to 5×), claude-haiku-5-5-low (up to 5×), claude-haiku-5-5-medium (up to 5×) |
| valuation-basis gate (E170) | fired | rows outside the scored valuation outcomes: claude-fable-5-2, claude-fable-5-2-high, claude-fable-5-2-xhigh |
| source clocks and evidence freshness (O59, O60, O65, E211, E216, E217, E218) | passed | every capture is within its age gate and none after the cutoff unless its source predates the cutoff's day; the build stops otherwise |
| build-stopping evidence gates (O64, O69, O71, O75, O99, O100, O101, O103, O105-O111, E195, E204, E225) | passed | the Coding Agent Index manifest (O64), the Terminal-Bench agent list (E225), cutoff-day row dates (O69), the three-stage all-provider plan search (O71, O75), the typed change records behind every route flag and partition split, which also produce each route's label and blocking dates within its launch- and schedule-bounded span (O99, O101, O105, O107, O110, O111), the register of AA notes covering every captured one, with the chart's inventory and duplicate-entry checks, the post-O103 capture notes, the basket-chart labels and chart-level notes' named rows (O100, O103, O106, O108) and the frontier path checks (E195, E204) hold; the build stops otherwise |
| score swing gate (E177) | vacuous | first v3 release: no previous v3 release to compare |
| ranking coverage (O166) | vacuous | ranks 29 of 45 cohort configurations; first v3 release: no previous v3 release to compare |
| anchor migration (E184) | vacuous | no main-workload migration deferred |
| frozen admission (O169) | vacuous | every frozen component still meets the admission threshold |
| configuration map coverage | passed | every cohort row has a configuration-map entry |
| quality clipping audit (E110) | passed | saturation disclosed; domain violations block the build |
| full benchmark set (O36, O38) | fired | listed, not ranked: gpt-6.2-astra-high, gpt-6.2-astra, gpt-6.2-astra-medium, gpt-6.2-astra-xhigh, gpt-6.2-sol-high, gpt-6.2-sol-low, gpt-6.2-sol, gpt-6.2-sol-medium, gpt-6.2-sol-xhigh, gemini-4-carbon, gemini-4-neon-high, gemini-4-neon-medium, gemini-4-neon, mimo-v2-6-flash, muse-ember, muse-ember-xhigh |
| missing-leaf rules (O8 provisional, E198b, E201b, E219, E221, E226) | vacuous | no ranked row has a missing leaf (O36) |
| S1M interval stream (E145) | vacuous | dormant: no ranked leaf carries a published confidence interval since O37, so S1M equals S1 (E236) |
| provider-claim label denial (E233) | vacuous | no row has a provider-claimed leaf |
| scenario outputs current (E72) | passed | scenario input hash matches the scored inputs |
| diagnostic ranking (O121) | fired | no label is issued and the gates are disclosed without holding the release |


## Basket cost by component

USD at API rates for the exact configuration; "—" marks a component without an exact cost.

| Configuration | Coding Agent Index | ITBench-AA | AA-Briefcase | GDP.pdf | AutomationBench-AA | Terminal-Bench 4.1 (AA Index run) | FrontierCode 2.0 | Terminal-Bench-Science | Basket cost | Missing admitted components |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| GPT-6.1 Sol (max) | $485.12 | — | $210.45 | $41.99 | $195.01 | $120.30 | $149.21 | $233.73 | $1,435.80 | none |
| Claude Sonnet 5.5 (max) | $3,670.34 | — | $1,863.13 | $79.43 | $678.32 | $834.67 | $1,525.59 | $1,663.25 | $10,314.72 | none |
| Claude Opus 5.5 (max) | $4,061.44 | $146.00 | $1,915.18 | $155.23 | $938.69 | $865.21 | $1,776.08 | $1,397.97 | $11,109.82 | none |
| GPT-6 Astra (max) | $2,455.41 | $133.00 | $864.69 | $207.58 | $1,048.30 | $560.88 | $863.12 | $1,223.34 | $7,223.31 | none |
| GPT-6 Luna (max) | $61.88 | — | $15.47 | $2.85 | $23.91 | $15.59 | $23.22 | $31.79 | $174.72 | none |

### Valuation basis

Valuation-basis gate (E170): 5 compatible as captured. AA's Index category costs reconcile exactly with the prices AA displays for each configuration at capture, so its applied prices are the prices in force at the release cutoff. Token metering (E176): 5 not published per configuration; AA values cached input at live measurements of each model's typical cache-hit rate. Source intervals (E174): terminalBench: captured, level 95% (tbench.ai: "The whiskers span the 95% confidence interval"); gdpval: captured, level unstated, level not stated by the source (the 95% level on AA's methodology page belongs to AA-Briefcase).

## Plan route selection

The Plan amount is the selected multiple times the cash paid for the fee period (E166), typed by what the measurement establishes; it is not capacity unless it says so. The multiple values only the measured workload's API-equivalent consumption; other plan features are not valued.

| Configuration | Selected route | Plan amount | Basket runs per fee period | Identification | Plan cost (USD per basket run) | Flags | Selection reason |
|---|---|---|---|---|---:|---|---|
| GPT-6.1 Sol (max) | ChatGPT Pro 500 $500 · GPT-6.1 Sol (10.772×, measured) | $5,386 per month: measured-workload capacity | 3.75 per month | unidentified | $133.29 | workload-unmatched; possibly-superseded; measured inside an acknowledged accounting-fault window (O91, O92); valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| Claude Sonnet 5.5 (max) | Claude Pro $20 · common Claude assumption (58.9×, assumption) | $1,178 per month: assumed API-equivalent consumption (owner-named transfer) from claude-pro-opus55-semianalysis | 0.11 per month | unidentified | $175.12 | workload-unmatched; owner-named transfer (assumption); possibly-superseded; valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| Claude Opus 5.5 (max) | Claude Pro $20 · Opus 5.5 (58.9×, measured) | $1,178 per month: measured-workload capacity | 0.11 per month | unidentified | $188.62 | workload-unmatched; possibly-superseded; valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| GPT-6 Astra (max) | ChatGPT Pro 200 $200 · GPT-6 Astra (14.485×, measured) | $2,897 per month: measured-workload capacity | 0.40 per month | unidentified | $498.68 | workload-unmatched; possibly-superseded; valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| GPT-6 Luna (max) | ChatGPT Pro 500 $500 · common GPT assumption (10.772×, assumption) | $5,386 per month: assumed API-equivalent consumption (owner-named transfer) from chatgpt-pro500-gpt61sol-semianalysis | 30.83 per month | unidentified | $16.22 | workload-unmatched; owner-named transfer (assumption); possibly-superseded; measured inside an acknowledged accounting-fault window (O91, O92); valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |

### Route alternatives

Every admissible route-measurement pair in comparator order (E171) and the comparator's pick with the selected pair removed (E179). A larger displayed multiple is arithmetic on the measured workload, never a claim that the route is cheaper on the scored workload. Workday-feasible multiple (E15), for the 5 routed rows: not evaluated: no evidenced quota schema for this route.

| Configuration | Admissible pairs | Unidentified | Pairs (multiple, status) | Leave-selected-out choice |
|---|---:|---:|---|---|
| GPT-6.1 Sol (max) | 4 | 4 | chatgpt-pro500-gpt61sol-semianalysis (10.772×, selected); chatgpt-plus-gpt61sol-semianalysis (10.55×, not selected by the comparator); chatgpt-pro100-gpt61sol-semianalysis (10.55×, not selected by the comparator); chatgpt-pro200-gpt61sol-semianalysis (10.42×, not selected by the comparator) | chatgpt-plus-gpt61sol-semianalysis (10.55×, value 67.83) |
| Claude Sonnet 5.5 (max) | 3 | 3 | claude-pro-claude-sonnet-5-5-common-opus55-assumption (58.9×, selected); claude-max20x-claude-sonnet-5-5-common-opus55-assumption (58.63×, not selected by the comparator); claude-max5x-claude-sonnet-5-5-common-opus55-assumption (57.25×, not selected by the comparator) | claude-max20x-claude-sonnet-5-5-common-opus55-assumption (58.63×, value 65.56) |
| Claude Opus 5.5 (max) | 3 | 3 | claude-pro-opus55-semianalysis (58.9×, selected); claude-max20x-opus55-semianalysis (58.63×, not selected by the comparator); claude-max5x-opus55-semianalysis (57.25×, not selected by the comparator) | claude-max20x-opus55-semianalysis (58.63×, value 65.29) |
| GPT-6 Astra (max) | 4 | 4 | chatgpt-pro200-gpt6astra-semianalysis (14.485×, selected); chatgpt-pro500-gpt6astra-semianalysis (13.91×, not selected by the comparator); chatgpt-pro100-gpt6astra-semianalysis (13.22×, not selected by the comparator); chatgpt-plus-gpt6astra-semianalysis (8.1×, not selected by the comparator) | chatgpt-pro500-gpt6astra-semianalysis (13.91×, value 58.52) |
| GPT-6 Luna (max) | 5 | 5 | chatgpt-pro500-gpt-6-luna-common-gpt-assumption (10.772×, selected); chatgpt-pro100-gpt-6-luna-common-gpt-assumption (10.55×, not selected by the comparator); chatgpt-pro200-gpt-6-luna-common-gpt-assumption (10.42×, not selected by the comparator); chatgpt-plus-gpt-6-luna-common-gpt-assumption (8.1×, not selected by the comparator); opencode-go-gpt-6-luna-dollar-limit (1.5×, not selected by the comparator) | chatgpt-pro100-gpt-6-luna-common-gpt-assumption (10.55×, value 56.08) |

### Route brackets (O144, O146)

A plan meter counts tokens (O126), so a multiple measured on one model or effort is worth the target's price per metered token over the donor's: a Claude transfer (O144) is bracketed by the two models' list prices over the registry's shared token mix, and a same-model cross-effort route (O146) by the two configurations' own Intelligence Index token mixes. Each row is rescored at M × min(1, r) and M × max(1, r) with every other row at its displayed value. ChatGPT transfers are not bracketed (Codex credits are priced per model at API parity, O144). Scores and ranks are unchanged.

3 rows bracketed; 3 change Plan rank within their bracket.

| Plan row | Rule | Price ratio r | Multiple range | Plan value range | Plan rank range |
|---|---|---:|---|---|---|
| Claude Sonnet 5.5 (max) on claude-max-20x | O144 | 0.500 | 29.32–58.63 | 60.29–65.56 | 6–10 |
| Claude Sonnet 5.5 (max) on claude-max-5x | O144 | 0.500 | 28.62–57.25 | 60.10–65.38 | 7–10 |
| Claude Sonnet 5.5 (max) on claude-pro | O144 | 0.500 | 29.45–58.90 | 60.32–65.59 | 5–10 |

### Plan allowance report cells (O71, O81)

71 cells; 1 passes. A cell on a plan the Plan ranking does not list is evidence only (O85).

| Provider | Plan | Model | Unit | Region | Eligible reports | Verdict |
|---|---|---|---|---|---|---|
| Anthropic | Claude (plan redacted) (not listed) | Claude Opus 5.5 | week | global | 0 of 1 | fails: 0 non-provisional report(s) in the current partition |
| Anthropic | Claude Max (tier not stated; "a Max plan") (not listed) | Claude Opus 5.5 | 5h | global | 0 of 1 | fails: a 5-hour figure never converts to a billing period (O82) |
| Anthropic | Claude Max (tier unstated) (not listed) | Claude Opus 5.5 | week | global | 0 of 3 | fails: 0 non-provisional report(s) in the current partition |
| Anthropic | Claude Max 20x | Claude Fable 5.2 | month | global | 0 of 1 | fails: 0 non-provisional report(s) in the current partition |
| Anthropic | Claude Max 20x | Claude Fable 5.2 | week | global | 1 of 3 | fails: 1 non-provisional report(s) in the current partition |
| Anthropic | Claude Max 20x | Claude Opus 5.5 | 5h | global | 0 of 2 | fails: a 5-hour figure never converts to a billing period (O82) |
| Anthropic | Claude Max 20x | Claude Opus 5.5 | month | global | 0 of 1 | fails: 0 non-provisional report(s) in the current partition |
| Anthropic | Claude Max 20x | Claude Opus 5.5 | week | global | 2 of 16 | passes |
| Anthropic | Claude Max 20x | Claude Sonnet 5.5 | week | global | 0 of 2 | fails: 0 non-provisional report(s) in the current partition |
| Anthropic | Claude Max 20x | — | week | global | 0 of 6 | fails: 0 non-provisional report(s) in the current partition |
| Anthropic | Claude Max 20x / Ultra (not listed) | Claude Opus 5.5 | week | global | 0 of 1 | fails: 0 non-provisional report(s) in the current partition |
| Anthropic | Claude Max 5x | Claude Fable 5.2 | month | global | 1 of 1 | fails: 1 non-provisional report(s) in the current partition |
| Anthropic | Claude Max 5x | Claude Haiku 5.5 | 5h | global | 0 of 1 | fails: a 5-hour figure never converts to a billing period (O82) |
| Anthropic | Claude Max 5x | Claude Opus 5.5 | 5h | global | 0 of 1 | fails: a 5-hour figure never converts to a billing period (O82) |
| Anthropic | Claude Max 5x | Claude Opus 5.5 | month | global | 1 of 2 | fails: 1 non-provisional report(s) in the current partition |
| Anthropic | Claude Max 5x | Claude Opus 5.5 | week | global | 0 of 3 | fails: 0 non-provisional report(s) in the current partition |
| Anthropic | Claude Max 5x | Claude Sonnet 5.5 | 5h | global | 0 of 1 | fails: a 5-hour figure never converts to a billing period (O82) |
| Anthropic | Claude Max 5x | — | week | global | 0 of 1 | fails: 0 non-provisional report(s) in the current partition |
| Anthropic | Claude Pro | Claude Fable 5.2 | 5h | global | 0 of 1 | fails: a 5-hour figure never converts to a billing period (O82) |
| Anthropic | Claude Pro | Claude Opus 5.5 | 5h | global | 0 of 9 | fails: a 5-hour figure never converts to a billing period (O82) |
| Anthropic | Claude Pro | Claude Opus 5.5 | month | global | 0 of 1 | fails: 0 non-provisional report(s) in the current partition |
| Anthropic | Claude Pro | Claude Opus 5.5 | week | global | 0 of 9 | fails: 0 non-provisional report(s) in the current partition |
| Anthropic | Claude Pro | — | week | global | 0 of 1 | fails: 0 non-provisional report(s) in the current partition |
| Anthropic | Claude Team Premium (not listed) | Claude Opus 5.5 | week | global | 0 of 1 | fails: 0 non-provisional report(s) in the current partition |
| Google | Google AI (tier unstated) (not listed) | gemini-4-argon | week | global | 0 of 1 | fails: 0 non-provisional report(s) in the current partition |
| Google | Google AI Pro | gemini-4-argon | week | global | 0 of 3 | fails: 0 non-provisional report(s) in the current partition |
| Google | Google AI Pro | gemini-4-hydrogen | 5h | global | 0 of 1 | fails: a 5-hour figure never converts to a billing period (O82) |
| Google | Google AI Ultra 20x | Gemini 4 Carbon | 5h | global | 0 of 1 | fails: a 5-hour figure never converts to a billing period (O82) |
| Google | Google AI Ultra 20x | Gemini 4 Carbon | week | global | 0 of 1 | fails: 0 non-provisional report(s) in the current partition |
| Google | Google AI Ultra 5x | Gemini 4 Carbon | 5h | global | 0 of 1 | fails: a 5-hour figure never converts to a billing period (O82) |
| Google | Google AI Ultra 5x | Gemini 4 Neon | month | global | 1 of 1 | fails: 1 non-provisional report(s) in the current partition |
| Google | Google AI Ultra 5x | gemini-4-argon | 5h | global | 0 of 1 | fails: a 5-hour figure never converts to a billing period (O82) |
| Google | Google AI Ultra 5x | gemini-4-argon | week | global | 0 of 1 | fails: 0 non-provisional report(s) in the current partition |
| Kimi | Kimi Allegretto (legacy, CN) (not listed) | kimi-k3-1-pro | 5h | CN | 0 of 4 | fails: a 5-hour figure never converts to a billing period (O82) |
| Kimi | Kimi Allegretto (legacy, CN) (not listed) | kimi-k3-1-pro | month | CN | 0 of 3 | fails: 0 non-provisional report(s) in the current partition |
| Kimi | Kimi Allegretto (legacy, CN) (not listed) | kimi-k3-1-pro | week | CN | 0 of 2 | fails: 0 non-provisional report(s) in the current partition |
| Kimi | Kimi Allegro (legacy, CN) (not listed) | kimi-k3-1-pro | 5h | CN | 0 of 5 | fails: a 5-hour figure never converts to a billing period (O82) |
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
| MiniMax | MiniMax Token Plan Max (legacy) (not listed) | minimax-m3-1-flash | week | global | 0 of 1 | fails: 0 non-provisional report(s) in the current partition |
| MiniMax | MiniMax Token Plan lowest tier (legacy) (not listed) | minimax-m3-1-flash | 5h | global | 0 of 1 | fails: a 5-hour figure never converts to a billing period (O82) |
| MiniMax | MiniMax lowest tier ("lite") (not listed) | — | week | global | 0 of 1 | fails: 0 non-provisional report(s) in the current partition |
| OpenAI | ChatGPT (legacy account, tier unstated) (not listed) | GPT-6.1 Sol | week | global | 0 of 1 | fails: 0 non-provisional report(s) in the current partition |
| OpenAI | ChatGPT Plus | GPT-6 Astra | 5h | global | 0 of 2 | fails: a 5-hour figure never converts to a billing period (O82) |
| OpenAI | ChatGPT Plus | GPT-6 Luna | 5h | global | 0 of 1 | fails: a 5-hour figure never converts to a billing period (O82) |
| OpenAI | ChatGPT Plus | GPT-6 Luna | month | global | 0 of 1 | fails: 0 non-provisional report(s) in the current partition |
| OpenAI | ChatGPT Plus | GPT-6.1 Sol | 5h | global | 0 of 4 | fails: a 5-hour figure never converts to a billing period (O82) |
| OpenAI | ChatGPT Plus | GPT-6.1 Sol | week | global | 0 of 3 | fails: 0 non-provisional report(s) in the current partition |
| OpenAI | ChatGPT Plus | GPT-6.1 Terra | 5h | global | 3 of 3 | fails: a 5-hour figure never converts to a billing period (O82) |
| OpenAI | ChatGPT Plus | GPT-6.2 Sol | 5h | global | 2 of 2 | fails: a 5-hour figure never converts to a billing period (O82) |
| OpenAI | ChatGPT Plus | gpt-5.6-luna-low | 5h | global | 0 of 1 | fails: a 5-hour figure never converts to a billing period (O82) |
| OpenAI | ChatGPT Plus | gpt-5.6-luna-low | week | global | 0 of 1 | fails: 0 non-provisional report(s) in the current partition |
| OpenAI | ChatGPT Pro (tier unstated) (not listed) | GPT-6 Astra | week | global | 0 of 1 | fails: 0 non-provisional report(s) in the current partition |
| OpenAI | ChatGPT Pro 100 | GPT-6 Astra | week | global | 0 of 4 | fails: 0 non-provisional report(s) in the current partition |
| OpenAI | ChatGPT Pro 100 | GPT-6.1 Sol | week | global | 0 of 1 | fails: 0 non-provisional report(s) in the current partition |
| OpenAI | ChatGPT Pro 200 (grandfathered 20x) | GPT-6 Astra | week | global | 0 of 1 | fails: 0 non-provisional report(s) in the current partition |
| OpenAI | ChatGPT Pro 200 (grandfathered 20x) | GPT-6.1 Sol | week | global | 0 of 3 | fails: 0 non-provisional report(s) in the current partition |
| OpenAI | ChatGPT Pro 500 | GPT-6 Astra | week | global | 0 of 1 | fails: 0 non-provisional report(s) in the current partition |
| OpenAI | ChatGPT Pro 500 | GPT-6.1 Sol | week | global | 0 of 1 | fails: 0 non-provisional report(s) in the current partition |
| Xiaomi | MiMo Token Plan Lite | mimo-v2-6-pro | month | global | 0 of 1 | fails: 0 non-provisional report(s) in the current partition |
| Xiaomi | MiMo Token Plan Max | mimo-v2-6-pro | month | global | 0 of 1 | fails: 0 non-provisional report(s) in the current partition |

### Measured-only Plan view

Admission: measurement candidates of grade controlled (exact effort, or the same model at another effort, O90) or concordant reports (no owner assumption of any kind, no diagnostics). Selection: the official selector (E111, E88, E85) rerun among the admitted candidates. Panel: rows with an admitted measured candidate; others listed as 'no measured route' (no API fallback).

| Configuration | Status | Route | Plan cost | Value | Rank |
|---|---|---|---:|---:|---:|
| GPT-6.1 Sol (max) | measured, target-workload unmatched | chatgpt-pro500-gpt61sol-semianalysis | $133.29 | 67.99 | 1 |
| Claude Opus 5.5 (max) | measured, target-workload unmatched | claude-pro-opus55-semianalysis | $188.62 | 65.33 | 2 |
| GPT-6 Astra (max) | measured, target-workload unmatched | chatgpt-pro200-gpt6astra-semianalysis | $498.68 | 58.83 | 3 |
| Claude Sonnet 5.5 (max) | no measured route | — | — | — | — |
| GPT-6 Luna (max) | no measured route | — | — | — | — |

#### Measured-evidence calibration (diagnostic)

References: each workload's measured-only rows with complete cost evidence are the references: c_L = cheapest / 2, c_H = dearest x 2 (diagnostic only; the official anchors are unchanged). Status: evaluated.

- Workload `2774ca1a24867d8c`: measured anchors $66.65 to $997.35 from Claude Opus 5.5 (max), GPT-6 Astra (max), GPT-6.1 Sol (max); anchor ratio 15.0 against the official 26.8. Official Plan anchors are set by GPT-6.1 Sol (max) on ChatGPT Pro 500 (controlled measurement) at the low end and GPT-6 Astra (max) on ChatGPT Plus (controlled measurement) at the high end.

| Configuration | Value on official Plan anchors | Value on measured anchors | Rank change |
|---|---:|---:|---:|
| Claude Opus 5.5 (max) | 65.33 | 63.63 | 0 |
| GPT-6 Astra (max) | 58.83 | 55.54 | 0 |
| GPT-6.1 Sol (max) | 67.99 | 66.86 | 0 |

Pairwise reversals: none. Largest value change: 3.29 points.

## Interval outputs

**API basis, main workload: frontier.** Not evaluable: none.

| Configuration | Possible frontier | Definite frontier | Definite counterexample | Possible frontier blocked by |
|---|---|---|---|---|
| GPT-6.1 Sol (max) | certified | certified | — | — |
| Claude Opus 5.5 (max) | disproved | disproved | GPT-6.1 Sol (max) | GPT-6.1 Sol (max), GPT-6 Astra (max) |
| GPT-6 Astra (max) | certified | certified | — | — |
| Claude Sonnet 5.5 (max) | disproved | disproved | GPT-6.1 Sol (max) | GPT-6.1 Sol (max), GPT-6 Astra (max) |
| GPT-6 Luna (max) | certified | certified | — | — | Safety-refusal flags (O63; costs and scores unchanged) on these labelled rows: GPT-6 Astra (max) (13 blocked and 0 fallback attempts of 966); GPT-6.1 Sol (max) (15 blocked and 0 fallback attempts of 966).

**API basis, main workload: cheapest at or above quality 64.3** (lower-median displayed quality of the non-provisional cohort configurations at freeze (E192; headline bar)). Status labels withheld: the ranking's like-for-like workload cost check (basket cost against Terminal-Bench cost per attempted task) cannot be computed (a panel below the 8-row floor or no rank variation), so no label is cleared by it (O187).

**API basis, main workload: cheapest at or above quality 63.9** (lower-quartile displayed quality of the non-provisional cohort configurations at freeze (O34)). Status labels withheld: the ranking's like-for-like workload cost check (basket cost against Terminal-Bench cost per attempted task) cannot be computed (a panel below the 8-row floor or no rank variation), so no label is cleared by it (O187).

**API basis, main workload: cheapest at or above quality 64.3** (upper-quartile displayed quality of the non-provisional cohort configurations at freeze (O34)). Status labels withheld: the ranking's like-for-like workload cost check (basket cost against Terminal-Bench cost per attempted task) cannot be computed (a panel below the 8-row floor or no rank variation), so no label is cleared by it (O187).

**Plan basis, main workload:** not evaluated (no row has FullCost and an identified M_W (E61/E67)).

## Scenario shares

The scenario panel is the 5 rows scored on the main workload (E96, E266).

Frequencies over 10,000 scenarios per run (seed 20261126); streams are defined in [methodology.md](methodology.md#uncertainty-outputs). S1T adds benchmark sampling noise under an independent-task approximation (O39); the other streams exclude it, and every stream excludes correlated-task, harness and attempt effects (E155).

### API basis: rank 1

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M | S1T | S1T recentred |
|---|---:|---:|---:|---:|---:|---:|---:|
| Claude Opus 5.5 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Sonnet 5.5 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Luna (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (max) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% |

### API basis: rank 3 or better

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M | S1T | S1T recentred |
|---|---:|---:|---:|---:|---:|---:|---:|
| Claude Opus 5.5 (max) | 0.0% | 0.0% | 1.7% | 0.0% | 0.0% | 9.0% | 10.4% |
| Claude Sonnet 5.5 (max) | 0.0% | 0.0% | 6.1% | 0.0% | 0.0% | 10.4% | 12.0% |
| GPT-6 Astra (max) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 97.6% | 97.3% |
| GPT-6 Luna (max) | 100.0% | 100.0% | 92.1% | 100.0% | 100.0% | 83.0% | 80.3% |
| GPT-6.1 Sol (max) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% |

### API basis: on the frontier

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M | S1T | S1T recentred |
|---|---:|---:|---:|---:|---:|---:|---:|
| Claude Opus 5.5 (max) | 0.0% | 0.0% | 13.5% | 0.0% | 0.0% | 16.5% | 16.6% |
| Claude Sonnet 5.5 (max) | 0.0% | 0.0% | 1.2% | 0.0% | 0.0% | 13.5% | 13.9% |
| GPT-6 Astra (max) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 73.8% | 73.0% |
| GPT-6 Luna (max) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% |
| GPT-6.1 Sol (max) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% |

### API basis: value-score dispersion (SD; covariance term)

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M | S1T | S1T recentred |
|---|---:|---:|---:|---:|---:|---:|---:|
| Claude Opus 5.5 (max) | 0.00 (+0.00) | 0.00 (+0.00) | 1.27 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 0.97 (+0.00) | 0.96 (+0.00) |
| Claude Sonnet 5.5 (max) | 0.00 (+0.00) | 0.00 (+0.00) | 1.11 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 0.99 (+0.00) | 0.99 (+0.00) |
| GPT-6 Astra (max) | 0.00 (+0.00) | 0.00 (+0.00) | 1.16 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 0.99 (+0.00) | 1.00 (+0.00) |
| GPT-6 Luna (max) | 0.00 (+0.00) | 0.00 (+0.00) | 1.35 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 0.92 (+0.00) | 0.90 (+0.00) |
| GPT-6.1 Sol (max) | 0.00 (+0.00) | 0.00 (+0.00) | 1.18 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.02 (+0.00) | 1.02 (+0.00) |

Plan streams S1, S2, S1 endpoint-heavy, S1M, S1T and S1T recentred run with owner assumptions off (owner-named transfers, O46 provider quota ceilings and O198 published dollar limits; E167): Claude Sonnet 5.5 (max) on Claude Max 20x, Claude Sonnet 5.5 (max) on Claude Max 5x, Claude Sonnet 5.5 (max) on Claude Pro, GPT-6 Luna (max) on ChatGPT Plus, GPT-6 Luna (max) on ChatGPT Pro 100, GPT-6 Luna (max) on ChatGPT Pro 200, GPT-6 Luna (max) on ChatGPT Pro 500, GPT-6 Luna (max) on OpenCode Go depend on an owner assumption and are unevaluable there (—), never reselected or replaced by API cost.

### Plan basis: rank 1

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M | S1T | S1T recentred |
|---|---:|---:|---:|---:|---:|---:|---:|
| Claude Opus 5.5 (max) on Claude Max 20x | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (max) on Claude Max 5x | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (max) on Claude Pro | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 3.2% | 3.1% |
| Claude Sonnet 5.5 (max) on Claude Max 20x | 0.0% | — | — | — | — | — | — |
| Claude Sonnet 5.5 (max) on Claude Max 5x | 0.0% | — | — | — | — | — | — |
| Claude Sonnet 5.5 (max) on Claude Pro | 0.0% | — | — | — | — | — | — |
| GPT-6 Astra (max) on ChatGPT Plus | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (max) on ChatGPT Pro 100 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (max) on ChatGPT Pro 200 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (max) on ChatGPT Pro 500 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Luna (max) on ChatGPT Plus | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 500 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (max) on OpenCode Go | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Sol (max) on ChatGPT Plus | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (max) on ChatGPT Pro 100 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (max) on ChatGPT Pro 200 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (max) on ChatGPT Pro 500 | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 96.8% | 96.9% |

### Plan basis: rank 3 or better

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M | S1T | S1T recentred |
|---|---:|---:|---:|---:|---:|---:|---:|
| Claude Opus 5.5 (max) on Claude Max 20x | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 3.8% | 3.8% |
| Claude Opus 5.5 (max) on Claude Max 5x | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 2.1% | 2.3% |
| Claude Opus 5.5 (max) on Claude Pro | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 4.1% | 4.0% |
| Claude Sonnet 5.5 (max) on Claude Max 20x | 0.0% | — | — | — | — | — | — |
| Claude Sonnet 5.5 (max) on Claude Max 5x | 0.0% | — | — | — | — | — | — |
| Claude Sonnet 5.5 (max) on Claude Pro | 0.0% | — | — | — | — | — | — |
| GPT-6 Astra (max) on ChatGPT Plus | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (max) on ChatGPT Pro 100 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (max) on ChatGPT Pro 200 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (max) on ChatGPT Pro 500 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Luna (max) on ChatGPT Plus | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 500 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (max) on OpenCode Go | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Sol (max) on ChatGPT Plus | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 96.2% | 96.2% |
| GPT-6.1 Sol (max) on ChatGPT Pro 100 | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 96.2% | 96.2% |
| GPT-6.1 Sol (max) on ChatGPT Pro 200 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (max) on ChatGPT Pro 500 | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 97.9% | 97.7% |

### Plan basis: on the frontier

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M | S1T | S1T recentred |
|---|---:|---:|---:|---:|---:|---:|---:|
| Claude Opus 5.5 (max) on Claude Max 20x | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (max) on Claude Max 5x | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (max) on Claude Pro | 0.0% | 0.0% | 54.1% | 0.0% | 0.0% | 48.8% | 49.6% |
| Claude Sonnet 5.5 (max) on Claude Max 20x | 0.0% | — | — | — | — | — | — |
| Claude Sonnet 5.5 (max) on Claude Max 5x | 0.0% | — | — | — | — | — | — |
| Claude Sonnet 5.5 (max) on Claude Pro | 0.0% | — | — | — | — | — | — |
| GPT-6 Astra (max) on ChatGPT Plus | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (max) on ChatGPT Pro 100 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (max) on ChatGPT Pro 200 | 100.0% | 100.0% | 86.5% | 100.0% | 100.0% | 60.6% | 60.7% |
| GPT-6 Astra (max) on ChatGPT Pro 500 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Luna (max) on ChatGPT Plus | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 500 | 100.0% | — | — | — | — | — | — |
| GPT-6 Luna (max) on OpenCode Go | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Sol (max) on ChatGPT Plus | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (max) on ChatGPT Pro 100 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (max) on ChatGPT Pro 200 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (max) on ChatGPT Pro 500 | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% |

### Plan basis: value-score dispersion (SD; covariance term)

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M | S1T | S1T recentred |
|---|---:|---:|---:|---:|---:|---:|---:|
| Claude Opus 5.5 (max) on Claude Max 20x | 0.00 (+0.00) | 0.00 (+0.00) | 1.28 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 0.96 (+0.00) | 0.96 (+0.00) |
| Claude Opus 5.5 (max) on Claude Max 5x | 0.00 (+0.00) | 0.00 (+0.00) | 1.28 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 0.96 (+0.00) | 0.96 (+0.00) |
| Claude Opus 5.5 (max) on Claude Pro | 0.00 (+0.00) | 0.00 (+0.00) | 1.28 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 0.96 (+0.00) | 0.96 (+0.00) |
| Claude Sonnet 5.5 (max) on Claude Max 20x | 0.00 (+0.00) | — | — | — | — | — | — |
| Claude Sonnet 5.5 (max) on Claude Max 5x | 0.00 (+0.00) | — | — | — | — | — | — |
| Claude Sonnet 5.5 (max) on Claude Pro | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6 Astra (max) on ChatGPT Plus | 0.00 (+0.00) | 0.00 (+0.00) | 1.16 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.00 (+0.00) | 1.00 (+0.00) |
| GPT-6 Astra (max) on ChatGPT Pro 100 | 0.00 (+0.00) | 0.00 (+0.00) | 1.16 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.00 (+0.00) | 1.00 (+0.00) |
| GPT-6 Astra (max) on ChatGPT Pro 200 | 0.00 (+0.00) | 0.00 (+0.00) | 1.16 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.00 (+0.00) | 1.00 (+0.00) |
| GPT-6 Astra (max) on ChatGPT Pro 500 | 0.00 (+0.00) | 0.00 (+0.00) | 1.16 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.00 (+0.00) | 1.00 (+0.00) |
| GPT-6 Luna (max) on ChatGPT Plus | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 100 | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 200 | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 500 | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6 Luna (max) on OpenCode Go | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6.1 Sol (max) on ChatGPT Plus | 0.00 (+0.00) | 0.00 (+0.00) | 1.17 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.02 (+0.00) | 1.03 (+0.00) |
| GPT-6.1 Sol (max) on ChatGPT Pro 100 | 0.00 (+0.00) | 0.00 (+0.00) | 1.17 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.02 (+0.00) | 1.03 (+0.00) |
| GPT-6.1 Sol (max) on ChatGPT Pro 200 | 0.00 (+0.00) | 0.00 (+0.00) | 1.17 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.02 (+0.00) | 1.03 (+0.00) |
| GPT-6.1 Sol (max) on ChatGPT Pro 500 | 0.00 (+0.00) | 0.00 (+0.00) | 1.17 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.02 (+0.00) | 1.03 (+0.00) |

### Named S2 specification branches

- **Bug Hunt harness band (E19)** (S2): unevaluable; the captured tbench.ai leaderboard lists no configuration under two or more agents, so no cross-agent spread exists
- **cache-hit variation (E34)** (S2): unevaluable; AA's published cost embeds its cache-pricing protocol; varying the cache-hit rate needs each basket component's cache-read and uncached-input demand, which AA publishes only for the whole Index (E157)
- **first-party list versus cross-provider median price rule (E122)** (S2): unevaluable; AA publishes one price per configuration under its own rule; the alternative rule's prices are not captured

### Cheapest-above-the-bar labels (API basis)

The 90% rule's error bound holds per published event (candidate and kernel assignment); it is not corrected across the listed candidates (E198). Each kernel assignment code gives the kernel used for the candidate and the competitors, in that order (U uniform, H endpoint-heavy; a quality-level bar has no reference rows, so it takes no letter); the label needs every assignment met.

| Bar | Candidate | Reading | Frequency range | Kernel assignments | Label |
|---|---|---|---|---|---|
| quality 64.3 | GPT-6.1 Sol (max) | labels withheld: the ranking's like-for-like workload cost check (basket cost against Terminal-Bench cost per attempted task) cannot be computed (a panel below the 8-row floor or no rank variation), so no label is cleared by it (O187) | 100.0% to 100.0% | UU met, UH met, HU met, HH met | no |
| quality 63.9 | GPT-6.1 Sol (max) | labels withheld: the ranking's like-for-like workload cost check (basket cost against Terminal-Bench cost per attempted task) cannot be computed (a panel below the 8-row floor or no rank variation), so no label is cleared by it (O187) | 100.0% to 100.0% | UU met, UH met, HU met, HH met | no |
| quality 64.3 | GPT-6.1 Sol (max) | not scenario-supported | 49.5% to 50.9% | UU not met, UH not met, HU not met, HH not met | no |
| quality 64.3 | GPT-6 Astra (max) | not scenario-supported | 49.1% to 50.5% | UU not met, UH not met, HU not met, HH not met | no |

## Diagnostics

- **Terminal-Bench cross-source agreement (AA's mini-SWE-agent run against tbench.ai):** defined; 0 rows take the leaf from tbench.ai (gap fill).
- **Workload cross-check (E41, mandatory diagnostic):** Terminal-Bench 4.1 cost per solved task on AA's own execution against basket cost: suppressed: 5 rows, below the 8-row floor; panel (5): Claude Opus 5.5 (max), Claude Sonnet 5.5 (max), GPT-6 Astra (max), GPT-6 Luna (max), GPT-6.1 Sol (max).
- **Rank separability (O39, independent-task approximation):** median separation 2.70 value points (API) and 2.70 (Plan); separable adjacent ranks: API 1 of 4, Plan 1 of 6. Assumptions: tasks are independent and each leaf's score is a mean over its published task count (a binomial leaf drawn from its Jeffreys posterior Beta(k + 1/2, n - k + 1/2), O142; plug-in SDs with the proportion (k + 1/2) / (n + 1), I28); attempts averaged within a task and tasks shared across models are ignored, so the noise is approximate; GDPval-AA: each row's rating interval as AA's model page displays it, read as a 95% normal interval (AA states no level), SD = half-width / 1.96; AA-Omniscience: each of 3,000 questions scores +1, 0 or -1, with the shares from AA's accuracy and hallucination rate; Vals boards (Vibe Code Bench v1.1, Code Migration v1.1): Vals' published standard error per record, read as the leaf's SD; AI Coding Daily: judged points over its seven graded projects read as a binomial share of 80 points (an assumption; the board publishes no error).
- **FrontierCode against Cognition:** FrontierCode 2.0 cross-source agreement (AA against Cognition, exact model and effort; E234, O153): Kendall tau 0.91 (interval 0.81 to 0.98) on 22 rows. Cognition minus AA: mean +0.2 points, largest 3.9.
- **Gap-fill removal (E234, diagnostic):** no ranked row has a leaf from another party or the provider.
- **Bar results without the gap fills (E234, sensitivity; labels unchanged):** cheapest displayed row as published, with fills removed, and with third-party fills third-party fills minus the signed mean offset +0.2 points (third party minus AA) — API quality 64.3: GPT-6.1 Sol (max) in all three; API quality 63.9: GPT-6.1 Sol (max) in all three; API quality 64.3: GPT-6.1 Sol (max) in all three; Plan quality 64.3: GPT-6.1 Sol (max) in all three; Plan quality 63.9: GPT-6.1 Sol (max) in all three; Plan quality 64.3: GPT-6.1 Sol (max) in all three.
- **Harness cost (O123, S2 stress):** agent effects on log cost (Claude Code -0.08, Codex -0.03, DeepSeek Harness +0.36, Devin CLI -0.10, GitHub Copilot -0.25, Grok Build +0.15, Kimi Code CLI +0.22, Mistral Vibe -0.17, Muse Code +0.70, OpenCode -0.11, Pi -0.48, Qwen Code -0.14, mini-swe-agent -0.08); API ranks with each agent's effect removed: GPT-6.1 Sol (max) 1; GPT-6 Astra (max) 2; GPT-6 Luna (max) 3; Claude Sonnet 5.5 (max) 4; Claude Opus 5.5 (max) 5. Coding Agent Index agents (each part of its costed configuration; none is the run behind the FrontierCode or Terminal-Bench leaf): GPT-6.1 Sol (max): Codex; Claude Opus 5.5 (max): Claude Code; GPT-6 Astra (max): Codex; Claude Sonnet 5.5 (max): Claude Code; GPT-6 Luna (max): Codex.
- **Quality agreement:** quality agreement (matched-panel sensitivity): Kendall tau 0.80 (interval 0.00 to 1.00) on 5 rows.
- **Quality-substitution value agreement (API):** quality-substitution value agreement, api basis (matched-panel sensitivity): Kendall tau 0.80 (interval 0.00 to 1.00) on 5 rows.
- **Quality-substitution value agreement (Plan):** quality-substitution value agreement, plan basis (matched-panel sensitivity): Kendall tau 1.00 (interval 1.00 to 1.00) on 5 rows.
- **Disjoint-evidence agreement:** disjoint-evidence agreement (restricted evidence comparison, not an eligible ranking): Kendall tau 0.00 (interval -1.00 to 1.00) on 5 rows.
- **Quality source shares:** AA-run 66%, independent 34%.
- **Non-discriminating leaves:** lcr.
- **Group drift:** estimated; flagged: none.
- **Omniscience abstention sensitivity** (z_pen = max(0, I)): 2 rows move; largest move 1 (Claude Opus 5.5 (max), Claude Sonnet 5.5 (max)).
- **GDPval-AA logistic sensitivity** (z = 100 / (1 + 10^((1600 - E) / 400)) against AA's pinned anchor; every other input fixed): API 2 rows move; largest move 1 (Claude Opus 5.5 (max), Claude Sonnet 5.5 (max)); Plan no rank changes.
- **Anchor stability:** trimmed anchors (P10 / 2 and P90 x 2 (diagnostic only)) give $339.58 to $21,583.56; 2 rows move; largest move 1 (GPT-6 Astra (max), GPT-6 Luna (max)).

- **Basket readiness (E22):** priced leaves cover 43% of nominal quality weight (AutomationBench-AA, FrontierCode 2.0, GDP.pdf (AA), Terminal-Bench-Science 0.1, Terminal-Bench 4.1 (AA run)); pending components: ITBench-AA.
- **SWE cost companion (O14, diagnostic):** 5 rows evaluated; flagged far from the median ratio: none.
- **Matched-cost diagnostic (E55):** evaluated at 56% priced quality weight; basket/matched cost-order reversals with separated intervals: 0; rank-gap warnings: 0.
- **Frontier-families anchors (E187, diagnostic):** anchors rebuilt from the 2 frontier and near-frontier references move API no rank changes (value points per cost doubling 5.05 vs 3.13 frozen); Plan 2 rows move; largest move 1 (GPT-6 Astra (max), GPT-6 Luna (max)) (value points per cost doubling 10.00 vs 5.27 frozen).
- **Frontier-families bar (E199, sensitivity; the frozen bar stays primary):** quality 64.3 over 2 configurations; cheapest at or above it on the API main workload: GPT-6.1 Sol (max) (confirmed) (compares 3 configurations that can qualify).
- **One row per family (E205, diagnostic; the frozen ladder and anchors stay primary):** with each family's primary configuration only (1 rows in the one-row-per-family bar population), the ladder (headline, lower quartile, upper quartile) would be unavailable against 64.3 / 63.9 / 64.3 frozen; anchors unavailable: fewer than 2 family-primary references.
- **Ladder over scored rows (I28, sensitivity; the frozen ladder stays primary):** the bar population keeps full-benchmark rows that have no cost; today every such row has a cost, so the ladder is unchanged.
- **Bar currency (E207, informational):** rows reaching each frozen bar: quality 64.3: 3 of 5; quality 63.9: 4 of 5; quality 64.3: 2 of 5; the current population would freeze 64.3 / 63.9 / 64.3; lifetime until the next anchor re-freeze or methodology version, whichever comes first; no staleness flag. Spacing flag: adjacent bars 0.0 quality points apart at the closest, under the 3.7-point noise margin (O44): the ladder's levels are not statistically distinct, so read the noise-margin companions.
- **Token mix (E208):** 5 selected routes: mix unidentified: the basket's token-category shares are set-identified only (E124), so the L1 test (above 0.30 flags mix-unmatched) is not computed.
- **Observed-range sensitivity (E219, not evidence; no label changes):** with each missing leaf inside the cohort's observed range for that leaf, quality 64.3: 3 can qualify, 2 confirmed; GPT-6.1 Sol (max) confirmed cheapest; quality 63.9: 4 can qualify, 3 confirmed; GPT-6.1 Sol (max) confirmed cheapest; quality 64.3: 2 can qualify, 1 confirmed; possibly cheapest GPT-6.1 Sol (max), GPT-6 Astra (max).
- **What would settle the headline bar (E221, not a claim):** rows that can but need not reach quality 64.3, with the mean score their missing leaves would need: Claude Opus 5.5 (max) (no missing leaf; reporting precision only).
- **Common leaf set (E226, diagnostic; scores unchanged):** without the leaves fewer than 90% of the ranking's ranked rows have (none), API no rank changes; Plan no rank changes; rows reaching each bar: quality 64.3: 3 → 3; quality 63.9: 4 → 4; quality 64.3: 2 → 2; rows whose displayed quality differs from common-leaf quality by more than one cost doubling's worth: none.
- **Harness by leaf (E227):** Terminal-Bench: mini-SWE-agent 5; Bug Hunt: Codex CLI 3, Claude Code 2.
- **Coding Agent Index safety refusals (O63, flagged; costs and scores unchanged):** GPT-6.1 Sol (max) (15 blocked of 966 attempts); Claude Opus 5.5 (max) (77 finished by Claude Opus 4.8 or Claude Opus 5 of 966 attempts); GPT-6 Astra (max) (13 blocked of 966 attempts); Claude Sonnet 5.5 (45 finished by Claude Opus 4.8 of 966 attempts).

### Leave-one-component-out cost family (E172)

Each admitted basket unit removed in turn, scored on anchors rebuilt by the freeze rule (rank changes against the primary ranking; quality held fixed).

| Removed component | API rank changes | Plan rank changes | API value points per cost doubling |
|---|---|---|---:|
| Coding Agent Index | 2 rows move; largest move 1 (Claude Opus 5.5 (max), Claude Sonnet 5.5 (max)) | 2 rows move; largest move 1 (GPT-6 Astra (max), GPT-6 Luna (max)) | 3.14 |
| AA-Briefcase | no rank changes | 2 rows move; largest move 1 (GPT-6 Astra (max), GPT-6 Luna (max)) | 3.18 |
| GDP.pdf | no rank changes | 2 rows move; largest move 1 (GPT-6 Astra (max), GPT-6 Luna (max)) | 3.13 |
| AutomationBench-AA | 2 rows move; largest move 1 (Claude Opus 5.5 (max), Claude Sonnet 5.5 (max)) | 2 rows move; largest move 1 (GPT-6 Astra (max), GPT-6 Luna (max)) | 3.10 |
| Terminal-Bench 4.1 (AA Index run) | no rank changes | 2 rows move; largest move 1 (GPT-6 Astra (max), GPT-6 Luna (max)) | 3.12 |
| FrontierCode 2.0 | 2 rows move; largest move 1 (Claude Opus 5.5 (max), Claude Sonnet 5.5 (max)) | 2 rows move; largest move 1 (GPT-6 Astra (max), GPT-6 Luna (max)) | 3.15 |
| Terminal-Bench-Science | no rank changes | 2 rows move; largest move 1 (GPT-6 Astra (max), GPT-6 Luna (max)) | 3.09 |

### Subset rows: paired bridge and missing spend (E10, E173)

No row is scored on a subset workload.

### Deletion sensitivity

| Branch | Retained nominal weight | Status | API rank changes | Plan rank changes |
|---|---:|---|---|---|
| leave-out:frontierCode | 85% | evaluated | no rank changes | no rank changes |
| leave-out:terminalBench | 89% | evaluated | 4 rows move; largest move 1 (Claude Opus 5.5 (max), Claude Sonnet 5.5 (max), GPT-6 Astra (max), GPT-6 Luna (max)) | 2 rows move; largest move 1 (Claude Opus 5.5 (max), Claude Sonnet 5.5 (max)) |
| leave-out:bugHunt | 92% | evaluated | 2 rows move; largest move 1 (Claude Opus 5.5 (max), Claude Sonnet 5.5 (max)) | 3 rows move; largest move 2 (Claude Opus 5.5 (max)) |
| leave-out:vibeCode | 95% | evaluated | 2 rows move; largest move 1 (Claude Opus 5.5 (max), Claude Sonnet 5.5 (max)) | no rank changes |
| leave-out:codeMigration | 94% | evaluated | 2 rows move; largest move 1 (Claude Opus 5.5 (max), Claude Sonnet 5.5 (max)) | 2 rows move; largest move 1 (Claude Opus 5.5 (max), Claude Sonnet 5.5 (max)) |
| leave-out:livebench2Overall | 85% | evaluated | no rank changes | no rank changes |
| leave-out:gdpval | 95% | evaluated | no rank changes | no rank changes |
| leave-out:gdpPdf | 95% | evaluated | no rank changes | no rank changes |
| leave-out:automationBench | 90% | evaluated | 2 rows move; largest move 1 (Claude Opus 5.5 (max), Claude Sonnet 5.5 (max)) | no rank changes |
| leave-out:omniscience | 90% | evaluated | no rank changes | no rank changes |
| leave-out:lcr | 95% | evaluated | no rank changes | no rank changes |
| leave-out:hle | 98% | evaluated | no rank changes | no rank changes |
| leave-out:tbScience | 98% | evaluated | no rank changes | no rank changes |
| leave-out:critpt | 98% | evaluated | no rank changes | no rank changes |
| leave-source-out:Artificial Analysis | 34% | not identifiable under the coverage rule | — | — |
| leave-source-out:Vals AI | 89% | evaluated | 2 rows move; largest move 1 (Claude Opus 5.5 (max), Claude Sonnet 5.5 (max)) | 2 rows move; largest move 1 (Claude Opus 5.5 (max), Claude Sonnet 5.5 (max)) |
| basket-scope | 87% | evaluated | no rank changes | no rank changes |

### Cost-component removal (Terminal-Bench 4.1 (AA Index run): evaluated)

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
| realised influence (E272) | passed | cost's value-variance allocation lies within 0-100% on both bases |
| quality influence flag (E126) | passed | quality not discriminating (cost share > 90%); informational only |
| subset scoring (O17) | vacuous | subset rows scored on their own workload and anchors |
| partial component flag (E37) | vacuous | AA declined- or missing-task markers, or an Index reconstruction that misses AA's total (E209) |
| route dominance filter (E88) | vacuous | certifiably dearer routes set aside |
| Plan exploratory label (E61) | fired | fewer than half of Plan rows have an identified M_W |
| Plan evidence lifecycle and change detection (E18, E151, E269, O77, O79) | fired | 18 of 19 plan rows carry a possibly-superseded or expired route: claude-opus-5-5@claude-max-20x, claude-opus-5-5@claude-max-5x, claude-opus-5-5@claude-pro, claude-sonnet-5-5@claude-max-20x, claude-sonnet-5-5@claude-max-5x, claude-sonnet-5-5@claude-pro, gpt-6-astra@chatgpt-plus, gpt-6-astra@chatgpt-pro-100, gpt-6-astra@chatgpt-pro-200, gpt-6-astra@chatgpt-pro-500, gpt-6-luna@chatgpt-plus, gpt-6-luna@chatgpt-pro-100, gpt-6-luna@chatgpt-pro-200, gpt-6-luna@chatgpt-pro-500, gpt-6.1-sol@chatgpt-plus, gpt-6.1-sol@chatgpt-pro-100, gpt-6.1-sol@chatgpt-pro-200, gpt-6.1-sol@chatgpt-pro-500 |
| acknowledged accounting-fault windows (O91, O92, O93, O95, O96) | fired | 3 of 19 plan rows rest on a measurement inside an acknowledged fault window; they stay selected and yield to two concordant user reports for their own model and plan, and the transfers resting on them follow: gpt-6-astra@chatgpt-pro-500, gpt-6-luna@chatgpt-pro-500, gpt-6.1-sol@chatgpt-pro-500 |
| AA cost omits a pricing term (O94, O98, O100, O106, O108, O109, O114) | passed | no AA cost note names an omitted pricing term |
| valuation-basis gate (E170) | passed | every ranked row is compatible as captured or after evidenced revaluation |
| source clocks and evidence freshness (O59, O60, O65, E211, E216, E217, E218) | passed | every capture is within its age gate and none after the cutoff unless its source predates the cutoff's day; the build stops otherwise |
| build-stopping evidence gates (O64, O69, O71, O75, O99, O100, O101, O103, O105-O111, E195, E204, E225) | passed | the Coding Agent Index manifest (O64), the Terminal-Bench agent list (E225), cutoff-day row dates (O69), the three-stage all-provider plan search (O71, O75), the typed change records behind every route flag and partition split, which also produce each route's label and blocking dates within its launch- and schedule-bounded span (O99, O101, O105, O107, O110, O111), the register of AA notes covering every captured one, with the chart's inventory and duplicate-entry checks, the post-O103 capture notes, the basket-chart labels and chart-level notes' named rows (O100, O103, O106, O108) and the frontier path checks (E195, E204) hold; the build stops otherwise |
| score swing gate (E177) | vacuous | first v3 release: no previous v3 release to compare |
| ranking coverage (O166) | vacuous | ranks 5 of 45 cohort configurations; first v3 release: no previous v3 release to compare |
| anchor migration (E184) | vacuous | no main-workload migration deferred |
| frozen admission (O169) | vacuous | every frozen component still meets the admission threshold |
| configuration map coverage | passed | every cohort row has a configuration-map entry |
| quality clipping audit (E110) | passed | saturation disclosed; domain violations block the build |
| full benchmark set (O36, O38) | fired | listed, not ranked: gpt-6.1-sol-high, gpt-6.1-terra, gpt-6.1-sol-medium, gpt-6-astra-high, claude-opus-5-5-high, gpt-6.1-sol-low, gpt-6.1-terra-xhigh, gpt-6.1-terra-high, claude-haiku-5-5-high, gpt-6.1-terra-medium, gpt-6-luna-xhigh, claude-haiku-5-5-medium, gpt-6-luna-high, gpt-6-luna-medium, claude-fable-5-2-high, claude-fable-5-2, claude-fable-5-2-xhigh, claude-haiku-5-5-low, claude-haiku-5-5, claude-opus-5-5-xhigh, gpt-6-astra-xhigh, gpt-6-luna-low, gpt-6.1-sol-xhigh, gpt-6.1-terra-low, gpt-6.2-astra-high, gpt-6.2-astra, gpt-6.2-astra-medium, gpt-6.2-astra-xhigh, gpt-6.2-sol-high, gpt-6.2-sol-low, gpt-6.2-sol, gpt-6.2-sol-medium, gpt-6.2-sol-xhigh, gemini-4-carbon, gemini-4-neon-high, gemini-4-neon-medium, gemini-4-neon, mimo-v2-6-flash, muse-ember, muse-ember-xhigh |
| missing-leaf rules (O8 provisional, E198b, E201b, E219, E221, E226) | vacuous | no ranked row has a missing leaf (O36) |
| S1M interval stream (E145) | vacuous | dormant: no ranked leaf carries a published confidence interval since O37, so S1M equals S1 (E236) |
| provider-claim label denial (E233) | vacuous | no row has a provider-claimed leaf |
| scenario outputs current (E72) | passed | scenario input hash matches the scored inputs |
