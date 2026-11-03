# ValueRank v3.0.0 Scores

**Updated:** October 19, 2026 · methodology 3.0.0 · SDLC basket v1 · anchor version `v3-2026-11-01-a3`

Value = 25% × cost score + 75% × quality. Costs are USD per basket run; the cost score is log-scaled against the frozen anchors of the row's workload (see [methodology.md](methodology.md)).

## Ranking

| Configuration | Plan rank | Plan value | Plan cost score | API rank | API value | API cost score | Quality | Quality coverage | Workload |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| [GPT-6.1 Sol (max)](https://valuerank.alolabs.dev/models/gpt-6-1-sol/) | 1 | 71.51 | 78.75 | 1 | 64.01 | 48.73 | 69.10 | 100% | main |
| [Claude Sonnet 5.5 (max)](https://valuerank.alolabs.dev/models/claude-sonnet-5-5/) | 5 | 68.59 | 68.78 | 6 | 54.51 | 12.43 | 68.53 | 100% | main |
| [Claude Opus 5.5 (max)](https://valuerank.alolabs.dev/models/claude-opus-5-5/) | 7 | 68.51 | 69.19 | 7 | 54.38 | 12.67 | 68.28 | 100% | main |
| [Claude Haiku 5.5 (max)](https://valuerank.alolabs.dev/models/claude-haiku-5-5-max/) | 11 | 62.41 | 100.00 | 8 | 50.86 | 53.79 | 49.89 | 100% | main |
| [GPT-6 Astra (max)](https://valuerank.alolabs.dev/models/gpt-6-astra/) | 14 | 62.07 | 39.06 | 3 | 57.35 | 20.20 | 69.73 | 100% | main |
| [GPT-6 Luna (max)](https://valuerank.alolabs.dev/models/gpt-6-luna/) | 17 | 58.76 | 100.00 | 5 | 55.65 | 87.57 | 45.01 | 100% | main |
| [MiMo-V2.6-Pro](https://valuerank.alolabs.dev/models/mimo-v2-6-pro/) | 22 | 52.27 | 63.69 | 4 | 56.26 | 79.62 | 48.47 | 100% | subset |
| [DeepSeek V4.1 Flash 1017 (max)](https://valuerank.alolabs.dev/models/deepseek-v4-1-flash-1017/) | 23 | 51.88 | 35.30 | 2 | 59.54 | 65.93 | 57.40 | 100% | main |
| [Gemini 4 Argon (high)](https://valuerank.alolabs.dev/models/gemini-4-argon/) | 27 | 46.58 | 0.00 | 9 | 50.44 | 15.44 | 62.11 | 100% | main |

## Not ranked

| Model | Reasons |
|---|---|
| Claude Haiku 5.5 (high) | Not in the max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall; ranked in the AI Coding Daily ranking, common-leaf diagnostic ranking |
| Claude Haiku 5.5 (low) | Incomplete benchmark evidence after an exhaustive search (O36, O53): Max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall; AI Coding Daily ranking: no AI Coding Daily (excl. bug finding) |
| Claude Haiku 5.5 (medium) | Not in the max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall; ranked in the AI Coding Daily ranking, common-leaf diagnostic ranking |
| Claude Haiku 5.5 (xhigh) | Incomplete benchmark evidence after an exhaustive search (O36, O53): Max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall; AI Coding Daily ranking: no AI Coding Daily (excl. bug finding) |
| Claude Opus 5.5 (high) | Not in the max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall; ranked in the AI Coding Daily ranking, common-leaf diagnostic ranking |
| Claude Opus 5.5 (medium) | Not in the max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall; ranked in the AI Coding Daily ranking, common-leaf diagnostic ranking |
| Claude Opus 5.5 (xhigh) | Incomplete benchmark evidence after an exhaustive search (O36, O53): Max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall; AI Coding Daily ranking: no AI Coding Daily (excl. bug finding) |
| Claude Sonnet 5.5 (xhigh) | Incomplete benchmark evidence after an exhaustive search (O36, O53): Max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall; AI Coding Daily ranking: no AI Coding Daily (excl. bug finding) |
| GPT-5.6 Luna | Incomplete benchmark evidence after an exhaustive search (O36, O53): Max-effort ranking: no FrontierCode 2.0, Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall, AA-Omniscience v1.1, HLE-Diamond, Terminal-Bench-Science 0.1, CritPt v2 (hard subset); AI Coding Daily ranking: no FrontierCode 2.0, AA-Omniscience v1.1, HLE-Diamond, Terminal-Bench-Science 0.1, CritPt v2 (hard subset) |
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
| Kimi K3.1 Pro | Not in the max-effort ranking: no Code Migration v1.1 (Vals); ranked in the AI Coding Daily ranking, common-leaf diagnostic ranking |
| MiMo-V2.6-Flash | Incomplete benchmark evidence after an exhaustive search (O36, O53): Max-effort ranking: no Bug Hunt Bench, LiveBench 2.0 Overall; AI Coding Daily ranking: no Bug Hunt Bench |
| MiniMax-M3.1-Flash | Incomplete benchmark evidence after an exhaustive search (O36, O53): Max-effort ranking: no Bug Hunt Bench, Code Migration v1.1 (Vals); AI Coding Daily ranking: no Bug Hunt Bench |

## Quality leaf scores

Each leaf's score z on its fixed 0–100 anchors; "—" marks a leaf with no eligible exact-configuration result.

| Configuration | FrontierCode 2.0 | Terminal-Bench 4.0 (AA run) | Bug Hunt Bench | Vibe Code Bench v1.1 (Vals) | Code Migration v1.1 (Vals) | LiveBench 2.0 Overall | GDPval-AA v2.1 | AutomationBench-AA | AA-Omniscience v1.1 | AA-LCR v1.1 | HLE-Diamond | Terminal-Bench-Science 0.1 | CritPt v2 (hard subset) | Quality | Provisional |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| GPT-6.1 Sol (max) | 40.6 | 56.1 | 109.6 | 88.9 | 77.3 | 84.1 | 55.4 | 64.9 | 71.0 | 83.0 | 58.8 | 58.1 | 68.5 | 69.10 | no |
| Claude Sonnet 5.5 (max) | 41.7 | 63.6 | 77.6 | 92.4 | 86.9 | 80.0 | 66.9 | 71.8 | 65.2 | 82.7 | 53.3 | 53.3 | 56.0 | 68.53 | no |
| Claude Opus 5.5 (max) | 46.4 | 59.6 | 50.7 | 90.3 | 81.0 | 85.1 | 68.3 | 69.5 | 74.1 | 84.7 | 67.9 | 59.0 | 61.0 | 68.28 | no |
| Claude Haiku 5.5 (max) | 34.9 | 32.8 | 30.5 | 90.4 | 52.4 | 69.8 | 56.5 | 35.4 | 56.1 | 82.7 | 29.6 | 20.0 | 41.0 | 49.89 | no |
| GPT-6 Astra (max) | 42.4 | 59.1 | 100.0 | 89.6 | 80.6 | 85.6 | 54.2 | 68.5 | 71.2 | 80.7 | 63.8 | 63.3 | 70.5 | 69.73 | no |
| GPT-6 Luna (max) | 25.2 | 12.6 | 41.0 | 81.6 | 46.7 | 64.6 | 47.2 | 53.2 | 45.9 | 83.3 | 22.2 | 8.6 | 41.5 | 45.01 | no |
| MiMo-V2.6-Pro | 24.0 | 34.8 | 22.0 | 85.2 | 48.8 | 68.5 | 59.5 | 58.6 | 47.8 | 86.3 | 15.2 | 5.7 | 34.0 | 48.47 | no |
| DeepSeek V4.1 Flash 1017 (max) | 28.5 | 33.8 | 86.7 | 87.7 | 67.5 | 72.9 | 62.3 | 66.6 | 50.5 | 82.7 | 25.3 | 12.9 | 24.0 | 57.40 | no |
| Gemini 4 Argon (high) | 25.7 | 57.1 | 48.0 | 91.9 | 70.8 | 79.3 | 56.5 | 77.5 | 73.0 | 79.7 | 56.7 | 52.9 | 52.5 | 62.11 | no |

## AI Coding Daily ranking

The configurations AI Coding Daily has tested, mostly at high and medium effort, scored on the AA leaves plus AI Coding Daily. Anchor version `v3-2026-11-01-a3-aicd`; leaves: FrontierCode 2.0 21%, Terminal-Bench 4.0 (AA run) 17%, Bug Hunt Bench 12%, AI Coding Daily (excl. bug finding) 10% (software engineering 60%), plus the 7 leaves outside software engineering every ranking shares.

| Configuration | Plan rank | Plan value | Plan cost score | API rank | API value | API cost score | Quality | Quality coverage | Workload |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| [GPT-6.1 Sol (high)](https://valuerank.alolabs.dev/models/gpt-6-1-sol-high/) | 1 | 61.44 | 63.94 | 1 | 57.44 | 47.96 | 60.60 | 100% | main |
| [GPT-6.1 Terra (max)](https://valuerank.alolabs.dev/models/gpt-6-1-terra/) | 5 | 60.74 | 56.81 | 2 | 57.36 | 43.26 | 62.05 | 100% | main |
| [Claude Opus 5.5 (high)](https://valuerank.alolabs.dev/models/claude-opus-5-5-high/) | 8 | 60.34 | 66.70 | 11 | 49.47 | 23.23 | 58.21 | 100% | main |
| [GPT-6.1 Sol (medium)](https://valuerank.alolabs.dev/models/gpt-6-1-sol-medium/) | 10 | 60.25 | 72.14 | 3 | 55.55 | 53.36 | 56.28 | 100% | main |
| [Claude Opus 5.5 (medium)](https://valuerank.alolabs.dev/models/claude-opus-5-5-medium/) | 11 | 60.24 | 73.44 | 12 | 48.80 | 27.66 | 55.84 | 100% | main |
| [GPT-6.1 Terra (xhigh)](https://valuerank.alolabs.dev/models/gpt-6-1-terra-xhigh/) | 19 | 56.44 | 74.22 | 6 | 51.57 | 54.74 | 50.52 | 100% | main |
| [GPT-6.1 Terra (high)](https://valuerank.alolabs.dev/models/gpt-6-1-terra-high/) | 22 | 56.16 | 82.12 | 8 | 50.62 | 59.94 | 47.51 | 100% | main |
| [GPT-6 Luna (max)](https://valuerank.alolabs.dev/models/gpt-6-luna/) | 25 | 55.69 | 99.72 | 14 | 48.64 | 71.53 | 41.02 | 100% | main |
| [GPT-6.1 Terra (medium)](https://valuerank.alolabs.dev/models/gpt-6-1-terra-medium/) | 26 | 55.67 | 89.32 | 10 | 49.51 | 64.68 | 44.45 | 100% | main |
| [GPT-6.1 Sol (low)](https://valuerank.alolabs.dev/models/gpt-6-1-sol-low/) | 31 | 55.47 | 83.55 | 9 | 49.80 | 60.88 | 46.11 | 100% | main |
| [GPT-6 Astra (high)](https://valuerank.alolabs.dev/models/gpt-6-astra-high/) | 37 | 54.30 | 30.25 | 5 | 52.02 | 21.14 | 62.32 | 100% | main |
| [Claude Haiku 5.5 (high)](https://valuerank.alolabs.dev/models/claude-haiku-5-5-high/) | 42 | 53.46 | 100.00 | 15 | 46.52 | 72.25 | 37.95 | 100% | main |
| [GPT-6 Luna (xhigh)](https://valuerank.alolabs.dev/models/gpt-6-luna-xhigh/) | 45 | 51.38 | 100.00 | 16 | 45.79 | 77.63 | 35.17 | 100% | main |
| [Claude Haiku 5.5 (medium)](https://valuerank.alolabs.dev/models/claude-haiku-5-5-medium/) | 50 | 49.88 | 100.00 | 19 | 44.81 | 79.73 | 33.17 | 100% | main |
| [GPT-6 Luna (high)](https://valuerank.alolabs.dev/models/gpt-6-luna-high/) | 53 | 49.73 | 100.00 | 17 | 45.30 | 82.25 | 32.98 | 100% | main |
| [Kimi K3.1 Pro (max)](https://valuerank.alolabs.dev/models/kimi-k3-1-pro/) | 57 | 45.43 | 0.00 | 7 | 51.01 | 22.30 | 60.58 | 100% | main |
| [GPT-6 Luna (medium)](https://valuerank.alolabs.dev/models/gpt-6-luna-medium/) | 58 | 45.35 | 100.00 | 20 | 42.64 | 89.16 | 27.14 | 100% | main |
| [DeepSeek V4.1 Flash 1017 (max)](https://valuerank.alolabs.dev/models/deepseek-v4-1-flash-1017/) | 62 | 43.14 | 10.72 | 4 | 52.98 | 50.06 | 53.95 | 100% | main |
| [Gemini 4 Argon (high)](https://valuerank.alolabs.dev/models/gemini-4-argon/) | 63 | 42.43 | 0.00 | 18 | 45.14 | 10.84 | 56.57 | 100% | main |
| [MiMo-V2.6-Pro](https://valuerank.alolabs.dev/models/mimo-v2-6-pro/) | 64 | 41.83 | 37.29 | 13 | 48.75 | 64.97 | 43.34 | 100% | main |

### AI Coding Daily ranking: quality leaf scores

| Configuration | FrontierCode 2.0 | Terminal-Bench 4.0 (AA run) | Bug Hunt Bench | AI Coding Daily (excl. bug finding) | GDPval-AA v2.1 | AutomationBench-AA | AA-Omniscience v1.1 | AA-LCR v1.1 | HLE-Diamond | Terminal-Bench-Science 0.1 | CritPt v2 (hard subset) | Quality | Provisional |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| GPT-6.1 Sol (high) | 36.7 | 51.5 | 76.5 | 94.7 | 51.0 | 64.5 | 70.5 | 82.3 | 51.9 | 46.2 | 67.5 | 60.60 | no |
| GPT-6.1 Terra (max) | 42.3 | 55.6 | 88.7 | 87.5 | 48.8 | 60.2 | 64.8 | 82.7 | 47.3 | 57.6 | 64.5 | 62.05 | no |
| Claude Opus 5.5 (high) | 35.9 | 56.6 | 42.4 | 96.1 | 60.7 | 63.2 | 71.2 | 82.7 | 55.6 | 49.0 | 58.0 | 58.21 | no |
| GPT-6.1 Sol (medium) | 33.4 | 48.0 | 59.5 | 92.8 | 48.0 | 62.6 | 70.1 | 83.3 | 46.0 | 37.1 | 65.0 | 56.28 | no |
| Claude Opus 5.5 (medium) | 33.1 | 52.5 | 43.6 | 94.9 | 54.6 | 61.2 | 69.9 | 84.3 | 51.4 | 43.3 | 52.5 | 55.84 | no |
| GPT-6.1 Terra (xhigh) | 36.9 | 46.5 | 28.3 | 80.2 | 45.7 | 59.9 | 64.5 | 81.7 | 42.3 | 41.9 | 57.5 | 50.52 | no |
| GPT-6.1 Terra (high) | 37.5 | 41.9 | 16.4 | 77.8 | 42.6 | 58.5 | 63.9 | 82.3 | 35.4 | 33.3 | 60.5 | 47.51 | no |
| GPT-6 Luna (max) | 25.2 | 12.6 | 41.0 | 86.7 | 47.2 | 53.2 | 45.9 | 83.3 | 22.2 | 8.6 | 41.5 | 41.02 | no |
| GPT-6.1 Terra (medium) | 34.5 | 32.3 | 14.6 | 78.2 | 41.2 | 57.8 | 63.3 | 80.7 | 31.3 | 24.8 | 56.0 | 44.45 | no |
| GPT-6.1 Sol (low) | 20.2 | 30.8 | 46.5 | 87.8 | 41.1 | 52.6 | 69.0 | 84.0 | 38.2 | 11.0 | 59.5 | 46.11 | no |
| GPT-6 Astra (high) | 40.1 | 54.0 | 75.0 | 94.6 | 51.8 | 66.6 | 72.3 | 80.0 | 59.3 | 59.5 | 71.5 | 62.32 | no |
| Claude Haiku 5.5 (high) | 23.2 | 21.7 | 20.0 | 85.9 | 46.2 | 33.7 | 52.6 | 77.3 | 23.7 | 10.0 | 42.5 | 37.95 | no |
| GPT-6 Luna (xhigh) | 18.4 | 8.1 | 26.0 | 83.2 | 43.6 | 47.8 | 43.5 | 80.0 | 18.9 | 5.2 | 35.5 | 35.17 | no |
| Claude Haiku 5.5 (medium) | 16.1 | 15.2 | 16.0 | 85.5 | 39.1 | 28.6 | 52.1 | 77.3 | 16.8 | 7.1 | 30.0 | 33.17 | no |
| GPT-6 Luna (high) | 18.6 | 4.5 | 18.0 | 79.5 | 42.6 | 47.8 | 43.6 | 79.3 | 15.6 | 2.9 | 30.5 | 32.98 | no |
| Kimi K3.1 Pro (max) | 25.5 | 67.2 | 65.3 | 91.0 | 67.9 | 73.3 | 64.9 | 86.3 | 37.3 | 34.3 | 45.0 | 60.58 | no |
| GPT-6 Luna (medium) | 12.8 | 2.5 | 4.0 | 67.0 | 38.5 | 40.5 | 43.2 | 78.3 | 15.1 | 1.4 | 26.0 | 27.14 | no |
| DeepSeek V4.1 Flash 1017 (max) | 28.5 | 33.8 | 86.7 | 87.1 | 62.3 | 66.6 | 50.5 | 82.7 | 25.3 | 12.9 | 24.0 | 53.95 | no |
| Gemini 4 Argon (high) | 25.7 | 57.1 | 48.0 | 83.2 | 56.5 | 77.5 | 73.0 | 79.7 | 56.7 | 52.9 | 52.5 | 56.57 | no |
| MiMo-V2.6-Pro | 24.0 | 34.8 | 22.0 | 79.3 | 59.5 | 58.6 | 47.8 | 86.3 | 15.2 | 5.7 | 34.0 | 43.34 | no |

### AI Coding Daily ranking: displayed record and noise

- API basis, displayed record (not a claim; E203): cheapest at or above quality 47.5: GPT-6.1 Terra (high) ($236.92 per basket run; 11 reach it); at or above quality 38.0: Claude Haiku 5.5 (high) ($107.80 per basket run; 16 reach it); at or above quality 56.6: GPT-6.1 Sol (high) ($509.65 per basket run; 6 reach it).
- API basis, cheaper same-family efforts on AA's chart that this ranking could not evaluate (O143, E201c): below Claude Haiku 5.5 (high): Claude Haiku 5.5 (low); below GPT-6.1 Terra (high): GPT-6.1 Terra (non-reasoning), GPT-6.1 Terra (low).
- API basis, noise-margin companion (O44; each bar plus 5.9 quality points, so the bar's own configuration cannot decide it): cheapest at or above quality 53.5: GPT-6.1 Sol (medium) ($360.71 per basket run); at or above quality 43.9: GPT-6.1 Terra (medium) ($174.91 per basket run); at or above quality 62.5: none.
- Plan basis, displayed record (not a claim; E203): cheapest at or above quality 47.5: GPT-6.1 Terra (high) on ChatGPT Pro 500 ($21.99 per basket run; 33 reach it); at or above quality 38.0: Claude Haiku 5.5 (high) on Claude Pro ($1.83 per basket run; 52 reach it); at or above quality 56.6: Claude Opus 5.5 (high) on Claude Pro ($42.11 per basket run; 17 reach it).
- Plan basis, cheaper same-family efforts on AA's chart that this ranking could not evaluate (O143, E201c): below Claude Haiku 5.5 (high): Claude Haiku 5.5 (low); below Claude Opus 5.5 (high): Claude Opus 5.5 (low with fallback); below GPT-6.1 Terra (high): GPT-6.1 Terra (non-reasoning), GPT-6.1 Terra (low).
- Plan basis, noise-margin companion (O44; each bar plus 5.9 quality points, so the bar's own configuration cannot decide it): cheapest at or above quality 53.5: Claude Opus 5.5 (medium) on Claude Pro ($31.71 per basket run); at or above quality 43.9: GPT-6.1 Terra (medium) on ChatGPT Pro 500 ($16.24 per basket run); at or above quality 62.5: none.
- AA cost caveat (O94; ranked at the published cost, no label of its own) on these bars' cheapest rows: Claude Haiku 5.5 (high) (AA's cost omits a pricing term; up to 5× on its cost).
- Plan route flags on these bars' cheapest plan rows: Claude Haiku 5.5 (high) on Claude Pro (possibly-superseded); Claude Opus 5.5 (high) on Claude Pro (possibly-superseded); Claude Opus 5.5 (medium) on Claude Pro (possibly-superseded); GPT-6.1 Terra (high) on ChatGPT Pro 500 (possibly-superseded, measured inside an acknowledged accounting-fault window (O91, O92)); GPT-6.1 Terra (medium) on ChatGPT Pro 500 (possibly-superseded, measured inside an acknowledged accounting-fault window (O91, O92)).
- These outputs compare ranked configurations only; listed families shown with an indicative value (O41) are outside them (O43): GPT-6.1 Sol (max), Claude Opus 5.5 (max), Claude Sonnet 5.5, GPT-6 Astra (max), Claude Haiku 5.5 (max), Claude Haiku 5.5 (low), Claude Haiku 5.5 (xhigh), Claude Opus 5.5 (xhigh), Claude Sonnet 5.5 (xhigh), GPT-5.6 Luna, GPT-6 Astra (xhigh), GPT-6 Luna (low), GPT-6.1 Sol (xhigh), GPT-6.1 Terra (low), Gemini 4 Carbon, MiMo-V2.6-Flash, MiniMax-M3.1-Flash.

Benchmark sampling noise (O39, an independent-task approximation): two values must differ by about 4.5 value points (median, 95%) to separate, and 0 of 19 adjacent API ranks and 0 of 34 adjacent Plan ranks of different configurations do (32 more adjacent Plan pairs are one configuration on two plans, ordered by the plans' multiples alone; E258). Its net direction is not established: every configuration is scored on the same tasks, which correlates their errors and narrows the true threshold (API 0 at correlation 0.3, 0 at correlation 0.6; Plan 1 at correlation 0.3, 1 at correlation 0.6), while sources it leaves out widen it (run-to-run and harness variance, AA's single cost run and, for the 42 Plan rows on an owner assumption (38 owner-named transfers and 4 O46 provider quota ceilings), that assumption's error). The noise band column groups each row with the band's first row it cannot be told apart from (O42); a Plan band marked † rests on an owner assumption (an owner-named transfer or an O46 provider quota ceiling) and excludes its error: an assumed multiple can be wrong by a factor of about 2.1 before the row's value moves by the median threshold (a tolerance, not an estimate of the assumption's error). The S1T scenario shares in [scores.md](scores.md) show each row's rank-1 and top-3 frequencies under that noise. AI Coding Daily's noise treats its six graded projects as six trials of the share of 60 points (n = 6, the wide reading, E263); read as 60 trials, the median threshold would be 3.2 (API) and 3.3 (Plan), with 0 and 1 adjacent ranks separable.


**Listed frontier families: indicative value, not ranked and not comparable (O41).** Quality is the mean over the leaves the configuration has, renormalised, with no imputation, so these values cannot be compared with the ranking above.

| Configuration | Missing | Quality (remaining leaves) | Quality coverage | Plan value (indicative) | API value (indicative) | API cost (USD per basket run) | Plan cost (USD per basket run) |
|---|---|---:|---:|---:|---:|---:|---:|
| GPT-6.1 Sol (max) | AI Coding Daily (excl. bug finding) | 64.0 | 90% | 60.3 | 57.5 | $950.68 | $88.25 |
| Claude Opus 5.5 (max) | AI Coding Daily (excl. bug finding) | 60.6 | 90% | 55.9 | 47.2 | $7,048.37 | $119.67 |
| Claude Sonnet 5.5 | AI Coding Daily (excl. bug finding) | 62.4 | 90% | 57.6 | 48.7 | $6,644.38 | $112.81 |
| GPT-6 Astra (max) | AI Coding Daily (excl. bug finding) | 64.1 | 90% | 52.5 | 51.3 | $4,767.90 | $329.16 |
| Claude Haiku 5.5 (max) | AI Coding Daily (excl. bug finding) | 41.1 | 90% | 55.9 | 45.3 | $270.65 | $4.60 |
| Claude Haiku 5.5 (low) | AI Coding Daily (excl. bug finding) | 22.4 | 90% | 41.8 | 39.1 | $36.79 | $0.62 |
| Claude Haiku 5.5 (xhigh) | AI Coding Daily (excl. bug finding) | 37.6 | 90% | 53.2 | 44.6 | $164.01 | $2.78 |
| Claude Opus 5.5 (xhigh) | AI Coding Daily (excl. bug finding) | 58.8 | 90% | 57.7 | 47.9 | $4,214.23 | $71.55 |
| Claude Sonnet 5.5 (xhigh) | AI Coding Daily (excl. bug finding) | 53.8 | 90% | 56.7 | 46.0 | $2,611.82 | $44.34 |
| GPT-5.6 Luna | FrontierCode 2.0, AA-Omniscience v1.1, HLE-Diamond, Terminal-Bench-Science 0.1, CritPt v2 (hard subset) | 20.1 | 64% | — | — | — | — |
| GPT-6 Astra (xhigh) | AI Coding Daily (excl. bug finding) | 63.0 | 90% | 54.1 | 52.1 | $3,186.48 | $219.99 |
| GPT-6 Luna (low) | AI Coding Daily (excl. bug finding) | 15.6 | 90% | 36.7 | 36.7 | $7.95 | $0.74 |
| GPT-6.1 Sol (xhigh) | AI Coding Daily (excl. bug finding) | 61.3 | 90% | 60.8 | 57.2 | $617.20 | $57.30 |
| GPT-6.1 Terra (low) | AI Coding Daily (excl. bug finding) | 33.0 | 90% | 49.8 | 42.9 | $104.95 | $9.74 |
| Gemini 4 Carbon | Bug Hunt Bench, AI Coding Daily (excl. bug finding) | 62.1 | 78% | 46.6 | 49.1 | $5,716.87 | $5,716.87 |
| MiMo-V2.6-Flash | Bug Hunt Bench | 42.0 | 88% | 44.9 | 50.6 | $82.84 | $72.16 |
| MiniMax-M3.1-Flash | Bug Hunt Bench | 44.1 | 88% | 37.7 | 46.9 | $323.30 | $323.30 |

### AI Coding Daily ranking: Plan routes and calibration

#### Measured-evidence calibration (diagnostic)

References: each workload's measured-only rows with complete cost evidence are the references: c_L = cheapest / 2, c_H = dearest x 2 (diagnostic only; the official anchors are unchanged). Status: evaluated.

- Workload `835a9baf594a1251`: measured anchors $10.35 to $391.32 from GPT-6 Astra (high), GPT-6.1 Sol (high), GPT-6.1 Sol (low), GPT-6.1 Sol (medium); anchor ratio 37.8 against the official 67.6. Official Plan anchors are set by GPT-6.1 Sol (low) on ChatGPT Pro 500 (same-model measurement from another effort) at the low end and GPT-6 Astra (high) on ChatGPT Plus (same-model measurement from another effort) at the high end.

| Configuration | Value on official Plan anchors | Value on measured anchors | Rank change |
|---|---:|---:|---:|
| Claude Opus 5.5 (high) ‡ | 60.34 | 59.00 | 2 |
| Claude Opus 5.5 (medium) ‡ | 60.24 | 59.18 | -2 |
| GPT-6 Astra (high) ‡ | 54.30 | 51.51 | 0 |
| GPT-6.1 Sol (high) ‡ | 61.44 | 59.99 | 0 |
| GPT-6.1 Sol (low) ‡ | 55.47 | 54.81 | 0 |
| GPT-6.1 Sol (medium) ‡ | 60.25 | 59.13 | 0 |

Pairwise reversals: Claude Opus 5.5 (high) and Claude Opus 5.5 (medium); Claude Opus 5.5 (high) and GPT-6.1 Sol (medium); Claude Opus 5.5 (medium) and GPT-6.1 Sol (medium). Largest value change: 2.79 points.

‡ measured on the same model at another effort (an O88 route; measured evidence under O90).

### AI Coding Daily ranking: interval outputs

**API basis, main workload: frontier.** Not evaluable: Claude Opus 5.5 (high), Claude Opus 5.5 (medium). Competing without a label of its own (E183): Claude Haiku 5.5 (high): AA's cost omits a pricing term (O94); competes over its published cost up to the stated factor; Claude Haiku 5.5 (medium): AA's cost omits a pricing term (O94); competes over its published cost up to the stated factor.

| Configuration | Possible frontier | Definite frontier | Definite counterexample | Possible frontier blocked by |
|---|---|---|---|---|
| GPT-6.1 Terra (max) | certified | certified | — | — |
| GPT-6.1 Sol (high) | certified | certified | — | — |
| DeepSeek V4.1 Flash 1017 (max) | disproved | disproved | GPT-6.1 Sol (medium) | GPT-6.1 Sol (medium) |
| GPT-6.1 Sol (medium) | certified | certified | — | — |
| Gemini 4 Argon (high) | disproved | disproved | GPT-6.1 Terra (max) | GPT-6.1 Terra (max), GPT-6.1 Sol (high), Kimi K3.1 Pro (max), GPT-6 Astra (high) |
| Kimi K3.1 Pro (max) | disproved | disproved | GPT-6.1 Terra (max) | GPT-6.1 Terra (max), GPT-6.1 Sol (high) |
| GPT-6 Astra (high) | certified | certified | — | — |
| GPT-6.1 Sol (low) | certified | certified | — | — |
| GPT-6.1 Terra (xhigh) | certified | certified | — | — |
| GPT-6.1 Terra (high) | certified | certified | — | — |
| GPT-6 Luna (max) | certified | certified | — | — |
| MiMo-V2.6-Pro | certified | certified | — | — |
| GPT-6.1 Terra (medium) | certified | certified | — | — |
| GPT-6 Luna (xhigh) | certified | certified | — | — |
| GPT-6 Luna (high) | certified | certified | — | — |
| GPT-6 Luna (medium) | certified | certified | — | — | These labels carry the workload cross-check warning (E41, O160: τ_b 0.35 on 20 configurations): the basket-cost order behind them agrees weakly with cost per solved task; the attribution is in scores.json `diagnostics.workloadCrossCheck.attribution`.

**API basis, main workload: cheapest at or above quality 47.5** (lower-median displayed quality of the non-provisional cohort configurations at freeze (E192; headline bar)). Status certified; confirmed cheapest: none.

Configurations that can be confirmed to qualify: 8 (confirmation needs the full-composite lower bound, with missing leaves at 0, to clear the bar; O25). Cheaper same-family configurations on AA's chart that were not evaluated (not ranked in this ranking: lacking its full benchmark set, or not plotted on or near the frontier; E201c, O51): GPT-6.1 Terra (xhigh): GPT-6.1 Terra (non-reasoning), GPT-6.1 Terra (low); GPT-6.1 Terra (high): GPT-6.1 Terra (non-reasoning), GPT-6.1 Terra (low).

Bar comparison: compares 9 configurations that can qualify. The bar is a displayed-quality level; qualification tests each row's full-composite bounds, so a row above the bar on displayed quality can still fail to qualify confirmed when leaves are missing (E198).

| Configuration | Displayed quality − bar | Confirmed qualifies | Possibly qualifies | Possibly cheapest |
|---|---:|---|---|---|
| GPT-6.1 Terra (max) | 14.5 | certified | certified | disproved |
| GPT-6.1 Sol (high) | 13.1 | certified | certified | disproved |
| DeepSeek V4.1 Flash 1017 (max) | 6.4 | certified | certified | disproved |
| GPT-6.1 Sol (medium) | 8.8 | certified | certified | disproved |
| Gemini 4 Argon (high) | 9.1 | certified | certified | disproved |
| Kimi K3.1 Pro (max) | 13.1 | certified | certified | disproved |
| GPT-6 Astra (high) | 14.8 | certified | certified | disproved |
| GPT-6.1 Sol (low) | -1.4 | disproved | disproved | disproved |
| GPT-6.1 Terra (xhigh) | 3.0 | certified | certified | certified |
| GPT-6.1 Terra (high) | 0.0 | disproved | certified | certified |
| GPT-6 Luna (max) | -6.5 | disproved | disproved | disproved |
| MiMo-V2.6-Pro | -4.2 | disproved | disproved | disproved |
| GPT-6.1 Terra (medium) | -3.1 | disproved | disproved | disproved |
| GPT-6 Luna (xhigh) | -12.3 | disproved | disproved | disproved |
| GPT-6 Luna (high) | -14.5 | disproved | disproved | disproved |
| GPT-6 Luna (medium) | -20.4 | disproved | disproved | disproved |

**API basis, main workload: cheapest at or above quality 38.0** (lower-quartile displayed quality of the non-provisional cohort configurations at freeze (O34)). Status certified; confirmed cheapest: none.

Configurations that can be confirmed to qualify: 13 (confirmation needs the full-composite lower bound, with missing leaves at 0, to clear the bar; O25). Cheaper same-family configurations on AA's chart that were not evaluated (not ranked in this ranking: lacking its full benchmark set, or not plotted on or near the frontier; E201c, O51): GPT-6 Luna (max): GPT-6 Luna (low), GPT-6 Luna (non-reasoning).

Bar comparison: compares 13 configurations that can qualify and 1 blocker(s) that can qualify but earn no label (E315). The bar is a displayed-quality level; qualification tests each row's full-composite bounds, so a row above the bar on displayed quality can still fail to qualify confirmed when leaves are missing (E198).

| Configuration | Displayed quality − bar | Confirmed qualifies | Possibly qualifies | Possibly cheapest |
|---|---:|---|---|---|
| GPT-6.1 Terra (max) | 24.1 | certified | certified | disproved |
| GPT-6.1 Sol (high) | 22.7 | certified | certified | disproved |
| DeepSeek V4.1 Flash 1017 (max) | 16.0 | certified | certified | disproved |
| GPT-6.1 Sol (medium) | 18.3 | certified | certified | disproved |
| Gemini 4 Argon (high) | 18.6 | certified | certified | disproved |
| Kimi K3.1 Pro (max) | 22.6 | certified | certified | disproved |
| GPT-6 Astra (high) | 24.4 | certified | certified | disproved |
| GPT-6.1 Sol (low) | 8.2 | certified | certified | disproved |
| GPT-6.1 Terra (xhigh) | 12.6 | certified | certified | disproved |
| GPT-6.1 Terra (high) | 9.6 | certified | certified | disproved |
| GPT-6 Luna (max) | 3.1 | certified | certified | certified |
| MiMo-V2.6-Pro | 5.4 | certified | certified | disproved |
| GPT-6.1 Terra (medium) | 6.5 | certified | certified | disproved |
| GPT-6 Luna (xhigh) | -2.8 | disproved | disproved | disproved |
| GPT-6 Luna (high) | -5.0 | disproved | disproved | disproved |
| GPT-6 Luna (medium) | -10.8 | disproved | disproved | disproved |

**API basis, main workload: cheapest at or above quality 56.6** (upper-quartile displayed quality of the non-provisional cohort configurations at freeze (O34)). Status certified; confirmed cheapest: GPT-6.1 Sol (high).

Configurations that can be confirmed to qualify: 4 (confirmation needs the full-composite lower bound, with missing leaves at 0, to clear the bar; O25). Cheaper same-family configurations on AA's chart that were not evaluated (not ranked in this ranking: lacking its full benchmark set, or not plotted on or near the frontier; E201c, O51): none.

Bar comparison: compares 5 configurations that can qualify. The bar is a displayed-quality level; qualification tests each row's full-composite bounds, so a row above the bar on displayed quality can still fail to qualify confirmed when leaves are missing (E198).

| Configuration | Displayed quality − bar | Confirmed qualifies | Possibly qualifies | Possibly cheapest |
|---|---:|---|---|---|
| GPT-6.1 Terra (max) | 5.5 | certified | certified | disproved |
| GPT-6.1 Sol (high) | 4.0 | certified | certified | certified |
| DeepSeek V4.1 Flash 1017 (max) | -2.6 | disproved | disproved | disproved |
| GPT-6.1 Sol (medium) | -0.3 | disproved | disproved | disproved |
| Gemini 4 Argon (high) | 0.0 | disproved | certified | disproved |
| Kimi K3.1 Pro (max) | 4.0 | certified | certified | disproved |
| GPT-6 Astra (high) | 5.7 | certified | certified | disproved |
| GPT-6.1 Sol (low) | -10.5 | disproved | disproved | disproved |
| GPT-6.1 Terra (xhigh) | -6.1 | disproved | disproved | disproved |
| GPT-6.1 Terra (high) | -9.1 | disproved | disproved | disproved |
| GPT-6 Luna (max) | -15.6 | disproved | disproved | disproved |
| MiMo-V2.6-Pro | -13.2 | disproved | disproved | disproved |
| GPT-6.1 Terra (medium) | -12.1 | disproved | disproved | disproved |
| GPT-6 Luna (xhigh) | -21.4 | disproved | disproved | disproved |
| GPT-6 Luna (high) | -23.6 | disproved | disproved | disproved |
| GPT-6 Luna (medium) | -29.4 | disproved | disproved | disproved |

**Plan basis, main workload:** not evaluated (no row has FullCost and an identified M_W (E61/E67)).

### AI Coding Daily ranking: scenario shares

The scenario panel is the 20 rows scored on the main workload (E96, E266).

Frequencies over 10,000 scenarios per run (seed 20261101); streams are defined in [methodology.md](methodology.md#uncertainty-outputs). S1T adds benchmark sampling noise under an independent-task approximation (O39); the other streams exclude it, and every stream excludes correlated-task, harness and attempt effects (E155).

### API basis: rank 1

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M | S1T | S1T recentred |
|---|---:|---:|---:|---:|---:|---:|---:|
| Claude Haiku 5.5 (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Haiku 5.5 (medium) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (medium) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| DeepSeek V4.1 Flash 1017 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.4% | 0.2% |
| GPT-6 Astra (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Luna (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Luna (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Luna (medium) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Luna (xhigh) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (high) | 100.0% | 100.0% | 56.7% | 100.0% | 100.0% | 44.9% | 45.7% |
| GPT-6.1 Sol (low) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (medium) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 7.8% | 7.1% |
| GPT-6.1 Terra (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Terra (max) | 0.0% | 0.0% | 43.3% | 0.0% | 0.0% | 47.0% | 46.9% |
| GPT-6.1 Terra (medium) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Terra (xhigh) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Gemini 4 Argon (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Kimi K3.1 Pro (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| MiMo-V2.6-Pro | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |

### API basis: rank 3 or better

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M | S1T | S1T recentred |
|---|---:|---:|---:|---:|---:|---:|---:|
| Claude Haiku 5.5 (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Haiku 5.5 (medium) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (medium) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| DeepSeek V4.1 Flash 1017 (max) | 0.0% | 0.0% | 1.5% | 0.0% | 0.0% | 13.7% | 13.1% |
| GPT-6 Astra (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 3.7% | 3.2% |
| GPT-6 Luna (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Luna (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Luna (medium) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Luna (xhigh) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (high) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 97.7% | 98.0% |
| GPT-6.1 Sol (low) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.1% | 0.1% |
| GPT-6.1 Sol (medium) | 100.0% | 100.0% | 98.5% | 100.0% | 100.0% | 83.7% | 85.0% |
| GPT-6.1 Terra (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.7% | 0.5% |
| GPT-6.1 Terra (max) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 97.0% | 96.9% |
| GPT-6.1 Terra (medium) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.1% | 0.1% |
| GPT-6.1 Terra (xhigh) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 2.7% | 2.5% |
| Gemini 4 Argon (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Kimi K3.1 Pro (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.7% | 0.6% |
| MiMo-V2.6-Pro | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |

### API basis: on the frontier

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M | S1T | S1T recentred |
|---|---:|---:|---:|---:|---:|---:|---:|
| Claude Haiku 5.5 (high) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 82.6% | 84.3% |
| Claude Haiku 5.5 (medium) | 100.0% | 100.0% | 60.4% | 100.0% | 100.0% | 51.3% | 52.4% |
| Claude Opus 5.5 (high) | 0.0% | 0.0% | 0.5% | 0.0% | 0.0% | 3.1% | 3.0% |
| Claude Opus 5.5 (medium) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.3% | 0.3% |
| DeepSeek V4.1 Flash 1017 (max) | 0.0% | 0.0% | 6.7% | 0.0% | 0.0% | 22.4% | 20.3% |
| GPT-6 Astra (high) | 100.0% | 100.0% | 60.0% | 100.0% | 100.0% | 39.3% | 39.2% |
| GPT-6 Luna (high) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 98.3% | 98.8% |
| GPT-6 Luna (max) | 100.0% | 100.0% | 99.9% | 100.0% | 100.0% | 86.6% | 87.4% |
| GPT-6 Luna (medium) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% |
| GPT-6 Luna (xhigh) | 100.0% | 100.0% | 99.5% | 100.0% | 100.0% | 68.8% | 68.5% |
| GPT-6.1 Sol (high) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 92.3% | 93.3% |
| GPT-6.1 Sol (low) | 100.0% | 100.0% | 87.0% | 100.0% | 100.0% | 62.4% | 64.4% |
| GPT-6.1 Sol (medium) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 97.1% | 97.4% |
| GPT-6.1 Terra (high) | 100.0% | 100.0% | 81.8% | 100.0% | 100.0% | 62.3% | 62.3% |
| GPT-6.1 Terra (max) | 100.0% | 100.0% | 98.9% | 100.0% | 100.0% | 70.3% | 70.4% |
| GPT-6.1 Terra (medium) | 100.0% | 100.0% | 87.3% | 100.0% | 100.0% | 61.5% | 62.2% |
| GPT-6.1 Terra (xhigh) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 81.0% | 80.9% |
| Gemini 4 Argon (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.1% | 0.1% |
| Kimi K3.1 Pro (max) | 0.0% | 0.0% | 16.8% | 0.0% | 0.0% | 20.4% | 20.9% |
| MiMo-V2.6-Pro | 100.0% | 100.0% | 96.5% | 100.0% | 100.0% | 80.3% | 79.6% |

### API basis: value-score dispersion (SD; covariance term)

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M | S1T | S1T recentred |
|---|---:|---:|---:|---:|---:|---:|---:|
| Claude Haiku 5.5 (high) | 0.00 (+0.00) | 0.00 (+0.00) | 1.64 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.44 (+0.00) | 1.42 (+0.00) |
| Claude Haiku 5.5 (medium) | 0.00 (+0.00) | 0.00 (+0.00) | 1.80 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.39 (+0.00) | 1.35 (+0.00) |
| Claude Opus 5.5 (high) | 0.00 (+0.00) | 0.00 (+0.00) | 1.45 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.40 (+0.00) | 1.36 (+0.00) |
| Claude Opus 5.5 (medium) | 0.00 (+0.00) | 0.00 (+0.00) | 1.47 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.44 (+0.00) | 1.39 (+0.00) |
| DeepSeek V4.1 Flash 1017 (max) | 0.00 (+0.00) | 0.00 (+0.00) | 1.81 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.58 (+0.00) | 1.59 (+0.00) |
| GPT-6 Astra (high) | 0.00 (+0.00) | 0.00 (+0.00) | 1.33 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.54 (+0.00) | 1.48 (+0.00) |
| GPT-6 Luna (high) | 0.00 (+0.00) | 0.00 (+0.00) | 1.80 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.37 (+0.00) | 1.37 (+0.00) |
| GPT-6 Luna (max) | 0.00 (+0.00) | 0.00 (+0.00) | 1.72 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.44 (+0.00) | 1.40 (+0.00) |
| GPT-6 Luna (medium) | 0.00 (+0.00) | 0.00 (+0.00) | 1.74 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.41 (+0.00) | 1.41 (+0.00) |
| GPT-6 Luna (xhigh) | 0.00 (+0.00) | 0.00 (+0.00) | 1.79 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.40 (+0.00) | 1.36 (+0.00) |
| GPT-6.1 Sol (high) | 0.00 (+0.00) | 0.00 (+0.00) | 1.43 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.53 (+0.00) | 1.47 (+0.00) |
| GPT-6.1 Sol (low) | 0.00 (+0.00) | 0.00 (+0.00) | 1.71 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.50 (+0.00) | 1.49 (+0.00) |
| GPT-6.1 Sol (medium) | 0.00 (+0.00) | 0.00 (+0.00) | 1.41 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.51 (+0.00) | 1.46 (+0.00) |
| GPT-6.1 Terra (high) | 0.00 (+0.00) | 0.00 (+0.00) | 1.38 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.59 (+0.00) | 1.62 (+0.00) |
| GPT-6.1 Terra (max) | 0.00 (+0.00) | 0.00 (+0.00) | 1.32 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.65 (+0.00) | 1.63 (+0.00) |
| GPT-6.1 Terra (medium) | 0.00 (+0.00) | 0.00 (+0.00) | 1.47 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.58 (+0.00) | 1.56 (+0.00) |
| GPT-6.1 Terra (xhigh) | 0.00 (+0.00) | 0.00 (+0.00) | 1.24 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.62 (+0.00) | 1.59 (+0.00) |
| Gemini 4 Argon (high) | 0.00 (+0.00) | 0.00 (+0.00) | 1.53 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.59 (+0.00) | 1.54 (+0.00) |
| Kimi K3.1 Pro (max) | 0.00 (+0.00) | 0.00 (+0.00) | 1.65 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.48 (+0.00) | 1.44 (+0.00) |
| MiMo-V2.6-Pro | 0.00 (+0.00) | 0.00 (+0.00) | 1.52 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.54 (+0.00) | 1.57 (+0.00) |

Plan streams S1, S2, S1 endpoint-heavy, S1M, S1T and S1T recentred run with owner assumptions off (owner-named transfers and O46 provider quota ceilings; E167): Claude Haiku 5.5 (high) on Claude Max 20x, Claude Haiku 5.5 (high) on Claude Max 5x, Claude Haiku 5.5 (high) on Claude Pro, Claude Haiku 5.5 (medium) on Claude Max 20x, Claude Haiku 5.5 (medium) on Claude Max 5x, Claude Haiku 5.5 (medium) on Claude Pro, GPT-6 Luna (high) on ChatGPT Plus, GPT-6 Luna (high) on ChatGPT Pro 100, GPT-6 Luna (high) on ChatGPT Pro 200, GPT-6 Luna (high) on ChatGPT Pro 500, GPT-6 Luna (max) on ChatGPT Plus, GPT-6 Luna (max) on ChatGPT Pro 100, GPT-6 Luna (max) on ChatGPT Pro 200, GPT-6 Luna (max) on ChatGPT Pro 500, GPT-6 Luna (medium) on ChatGPT Plus, GPT-6 Luna (medium) on ChatGPT Pro 100, GPT-6 Luna (medium) on ChatGPT Pro 200, GPT-6 Luna (medium) on ChatGPT Pro 500, GPT-6 Luna (xhigh) on ChatGPT Plus, GPT-6 Luna (xhigh) on ChatGPT Pro 100, GPT-6 Luna (xhigh) on ChatGPT Pro 200, GPT-6 Luna (xhigh) on ChatGPT Pro 500, GPT-6.1 Terra (high) on ChatGPT Plus, GPT-6.1 Terra (high) on ChatGPT Pro 100, GPT-6.1 Terra (high) on ChatGPT Pro 200, GPT-6.1 Terra (high) on ChatGPT Pro 500, GPT-6.1 Terra (max) on ChatGPT Plus, GPT-6.1 Terra (max) on ChatGPT Pro 100, GPT-6.1 Terra (max) on ChatGPT Pro 200, GPT-6.1 Terra (max) on ChatGPT Pro 500, GPT-6.1 Terra (medium) on ChatGPT Plus, GPT-6.1 Terra (medium) on ChatGPT Pro 100, GPT-6.1 Terra (medium) on ChatGPT Pro 200, GPT-6.1 Terra (medium) on ChatGPT Pro 500, GPT-6.1 Terra (xhigh) on ChatGPT Plus, GPT-6.1 Terra (xhigh) on ChatGPT Pro 100, GPT-6.1 Terra (xhigh) on ChatGPT Pro 200, GPT-6.1 Terra (xhigh) on ChatGPT Pro 500, MiMo-V2.6-Pro on MiMo Token Plan Lite, MiMo-V2.6-Pro on MiMo Token Plan Max, MiMo-V2.6-Pro on MiMo Token Plan Pro, MiMo-V2.6-Pro on MiMo Token Plan Standard depend on an owner assumption and are unevaluable there (—), never reselected or replaced by API cost.

### Plan basis: rank 1

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M | S1T | S1T recentred |
|---|---:|---:|---:|---:|---:|---:|---:|
| Claude Haiku 5.5 (high) on Claude Max 20x | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (high) on Claude Max 5x | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (high) on Claude Pro | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (medium) on Claude Max 20x | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (medium) on Claude Max 5x | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (medium) on Claude Pro | 0.0% | — | — | — | — | — | — |
| Claude Opus 5.5 (high) on Claude Max 20x | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (high) on Claude Max 5x | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (high) on Claude Pro | 0.0% | 0.0% | 12.2% | 0.0% | 0.0% | 16.9% | 15.9% |
| Claude Opus 5.5 (medium) on Claude Max 20x | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (medium) on Claude Max 5x | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (medium) on Claude Pro | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 15.4% | 15.8% |
| DeepSeek V4.1 Flash 1017 (max) on API-cost fallback | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (high) on ChatGPT Plus | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (high) on ChatGPT Pro 100 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (high) on ChatGPT Pro 200 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (high) on ChatGPT Pro 500 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Luna (high) on ChatGPT Plus | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (high) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (high) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (high) on ChatGPT Pro 500 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Plus | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 500 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (medium) on ChatGPT Plus | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (medium) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (medium) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (medium) on ChatGPT Pro 500 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (xhigh) on ChatGPT Plus | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (xhigh) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (xhigh) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (xhigh) on ChatGPT Pro 500 | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Sol (high) on ChatGPT Plus | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (high) on ChatGPT Pro 100 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (high) on ChatGPT Pro 200 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (high) on ChatGPT Pro 500 | 100.0% | 100.0% | 87.8% | 100.0% | 100.0% | 50.4% | 51.2% |
| GPT-6.1 Sol (low) on ChatGPT Plus | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (low) on ChatGPT Pro 100 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (low) on ChatGPT Pro 200 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (low) on ChatGPT Pro 500 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (medium) on ChatGPT Plus | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (medium) on ChatGPT Pro 100 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (medium) on ChatGPT Pro 200 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (medium) on ChatGPT Pro 500 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 17.3% | 17.1% |
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
| Gemini 4 Argon (high) on API-cost fallback | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Kimi K3.1 Pro (max) on API-cost fallback | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| MiMo-V2.6-Pro on MiMo Token Plan Lite | 0.0% | — | — | — | — | — | — |
| MiMo-V2.6-Pro on MiMo Token Plan Max | 0.0% | — | — | — | — | — | — |
| MiMo-V2.6-Pro on MiMo Token Plan Pro | 0.0% | — | — | — | — | — | — |
| MiMo-V2.6-Pro on MiMo Token Plan Standard | 0.0% | — | — | — | — | — | — |

### Plan basis: rank 3 or better

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M | S1T | S1T recentred |
|---|---:|---:|---:|---:|---:|---:|---:|
| Claude Haiku 5.5 (high) on Claude Max 20x | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (high) on Claude Max 5x | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (high) on Claude Pro | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (medium) on Claude Max 20x | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (medium) on Claude Max 5x | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (medium) on Claude Pro | 0.0% | — | — | — | — | — | — |
| Claude Opus 5.5 (high) on Claude Max 20x | 0.0% | 0.0% | 14.9% | 0.0% | 0.0% | 17.9% | 17.2% |
| Claude Opus 5.5 (high) on Claude Max 5x | 0.0% | 0.0% | 7.5% | 0.0% | 0.0% | 14.3% | 13.6% |
| Claude Opus 5.5 (high) on Claude Pro | 0.0% | 0.0% | 15.8% | 0.0% | 0.0% | 18.8% | 18.2% |
| Claude Opus 5.5 (medium) on Claude Max 20x | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 16.3% | 16.8% |
| Claude Opus 5.5 (medium) on Claude Max 5x | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 13.3% | 13.3% |
| Claude Opus 5.5 (medium) on Claude Pro | 0.0% | 0.0% | 1.1% | 0.0% | 0.0% | 17.2% | 17.7% |
| DeepSeek V4.1 Flash 1017 (max) on API-cost fallback | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (high) on ChatGPT Plus | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (high) on ChatGPT Pro 100 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (high) on ChatGPT Pro 200 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (high) on ChatGPT Pro 500 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Luna (high) on ChatGPT Plus | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (high) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (high) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (high) on ChatGPT Pro 500 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Plus | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 500 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (medium) on ChatGPT Plus | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (medium) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (medium) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (medium) on ChatGPT Pro 500 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (xhigh) on ChatGPT Plus | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (xhigh) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (xhigh) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (xhigh) on ChatGPT Pro 500 | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Sol (high) on ChatGPT Plus | 100.0% | 100.0% | 85.1% | 100.0% | 100.0% | 49.0% | 49.6% |
| GPT-6.1 Sol (high) on ChatGPT Pro 100 | 100.0% | 100.0% | 85.1% | 100.0% | 100.0% | 49.0% | 49.6% |
| GPT-6.1 Sol (high) on ChatGPT Pro 200 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (high) on ChatGPT Pro 500 | 100.0% | 100.0% | 91.5% | 100.0% | 100.0% | 53.6% | 54.7% |
| GPT-6.1 Sol (low) on ChatGPT Plus | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (low) on ChatGPT Pro 100 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (low) on ChatGPT Pro 200 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (low) on ChatGPT Pro 500 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (medium) on ChatGPT Plus | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 16.6% | 16.3% |
| GPT-6.1 Sol (medium) on ChatGPT Pro 100 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 16.6% | 16.3% |
| GPT-6.1 Sol (medium) on ChatGPT Pro 200 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (medium) on ChatGPT Pro 500 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 19.6% | 19.1% |
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
| Gemini 4 Argon (high) on API-cost fallback | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Kimi K3.1 Pro (max) on API-cost fallback | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| MiMo-V2.6-Pro on MiMo Token Plan Lite | 0.0% | — | — | — | — | — | — |
| MiMo-V2.6-Pro on MiMo Token Plan Max | 0.0% | — | — | — | — | — | — |
| MiMo-V2.6-Pro on MiMo Token Plan Pro | 0.0% | — | — | — | — | — | — |
| MiMo-V2.6-Pro on MiMo Token Plan Standard | 0.0% | — | — | — | — | — | — |

### Plan basis: on the frontier

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M | S1T | S1T recentred |
|---|---:|---:|---:|---:|---:|---:|---:|
| Claude Haiku 5.5 (high) on Claude Max 20x | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (high) on Claude Max 5x | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (high) on Claude Pro | 100.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (medium) on Claude Max 20x | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (medium) on Claude Max 5x | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (medium) on Claude Pro | 100.0% | — | — | — | — | — | — |
| Claude Opus 5.5 (high) on Claude Max 20x | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (high) on Claude Max 5x | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (high) on Claude Pro | 100.0% | 100.0% | 98.4% | 100.0% | 100.0% | 66.5% | 67.8% |
| Claude Opus 5.5 (medium) on Claude Max 20x | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (medium) on Claude Max 5x | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (medium) on Claude Pro | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 99.9% | 100.0% |
| DeepSeek V4.1 Flash 1017 (max) on API-cost fallback | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (high) on ChatGPT Plus | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (high) on ChatGPT Pro 100 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (high) on ChatGPT Pro 200 | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 70.3% | 71.5% |
| GPT-6 Astra (high) on ChatGPT Pro 500 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Luna (high) on ChatGPT Plus | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (high) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (high) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (high) on ChatGPT Pro 500 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Plus | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 500 | 100.0% | — | — | — | — | — | — |
| GPT-6 Luna (medium) on ChatGPT Plus | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (medium) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (medium) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (medium) on ChatGPT Pro 500 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (xhigh) on ChatGPT Plus | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (xhigh) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (xhigh) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (xhigh) on ChatGPT Pro 500 | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Sol (high) on ChatGPT Plus | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (high) on ChatGPT Pro 100 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (high) on ChatGPT Pro 200 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (high) on ChatGPT Pro 500 | 100.0% | 100.0% | 98.3% | 100.0% | 100.0% | 77.4% | 79.0% |
| GPT-6.1 Sol (low) on ChatGPT Plus | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (low) on ChatGPT Pro 100 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (low) on ChatGPT Pro 200 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (low) on ChatGPT Pro 500 | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% |
| GPT-6.1 Sol (medium) on ChatGPT Plus | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (medium) on ChatGPT Pro 100 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (medium) on ChatGPT Pro 200 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (medium) on ChatGPT Pro 500 | 100.0% | 100.0% | 73.1% | 100.0% | 100.0% | 56.5% | 56.3% |
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
| Gemini 4 Argon (high) on API-cost fallback | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.4% | 0.4% |
| Kimi K3.1 Pro (max) on API-cost fallback | 0.0% | 0.0% | 7.6% | 0.0% | 0.0% | 19.5% | 20.1% |
| MiMo-V2.6-Pro on MiMo Token Plan Lite | 0.0% | — | — | — | — | — | — |
| MiMo-V2.6-Pro on MiMo Token Plan Max | 0.0% | — | — | — | — | — | — |
| MiMo-V2.6-Pro on MiMo Token Plan Pro | 0.0% | — | — | — | — | — | — |
| MiMo-V2.6-Pro on MiMo Token Plan Standard | 0.0% | — | — | — | — | — | — |

### Plan basis: value-score dispersion (SD; covariance term)

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M | S1T | S1T recentred |
|---|---:|---:|---:|---:|---:|---:|---:|
| Claude Haiku 5.5 (high) on Claude Max 20x | 0.00 (+0.00) | — | — | — | — | — | — |
| Claude Haiku 5.5 (high) on Claude Max 5x | 0.00 (+0.00) | — | — | — | — | — | — |
| Claude Haiku 5.5 (high) on Claude Pro | 0.00 (+0.00) | — | — | — | — | — | — |
| Claude Haiku 5.5 (medium) on Claude Max 20x | 0.00 (+0.00) | — | — | — | — | — | — |
| Claude Haiku 5.5 (medium) on Claude Max 5x | 0.00 (+0.00) | — | — | — | — | — | — |
| Claude Haiku 5.5 (medium) on Claude Pro | 0.00 (+0.00) | — | — | — | — | — | — |
| Claude Opus 5.5 (high) on Claude Max 20x | 0.00 (+0.00) | 0.00 (+0.00) | 1.43 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.41 (+0.00) | 1.34 (+0.00) |
| Claude Opus 5.5 (high) on Claude Max 5x | 0.00 (+0.00) | 0.00 (+0.00) | 1.43 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.41 (+0.00) | 1.34 (+0.00) |
| Claude Opus 5.5 (high) on Claude Pro | 0.00 (+0.00) | 0.00 (+0.00) | 1.43 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.41 (+0.00) | 1.34 (+0.00) |
| Claude Opus 5.5 (medium) on Claude Max 20x | 0.00 (+0.00) | 0.00 (+0.00) | 1.45 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.43 (+0.00) | 1.39 (+0.00) |
| Claude Opus 5.5 (medium) on Claude Max 5x | 0.00 (+0.00) | 0.00 (+0.00) | 1.45 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.43 (+0.00) | 1.39 (+0.00) |
| Claude Opus 5.5 (medium) on Claude Pro | 0.00 (+0.00) | 0.00 (+0.00) | 1.45 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.43 (+0.00) | 1.39 (+0.00) |
| DeepSeek V4.1 Flash 1017 (max) on API-cost fallback | 0.00 (+0.00) | 0.00 (+0.00) | 1.79 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.60 (+0.00) | 1.59 (+0.00) |
| GPT-6 Astra (high) on ChatGPT Plus | 0.00 (+0.00) | 0.00 (+0.00) | 1.32 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.53 (+0.00) | 1.48 (+0.00) |
| GPT-6 Astra (high) on ChatGPT Pro 100 | 0.00 (+0.00) | 0.00 (+0.00) | 1.32 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.53 (+0.00) | 1.48 (+0.00) |
| GPT-6 Astra (high) on ChatGPT Pro 200 | 0.00 (+0.00) | 0.00 (+0.00) | 1.32 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.53 (+0.00) | 1.48 (+0.00) |
| GPT-6 Astra (high) on ChatGPT Pro 500 | 0.00 (+0.00) | 0.00 (+0.00) | 1.32 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.53 (+0.00) | 1.48 (+0.00) |
| GPT-6 Luna (high) on ChatGPT Plus | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6 Luna (high) on ChatGPT Pro 100 | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6 Luna (high) on ChatGPT Pro 200 | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6 Luna (high) on ChatGPT Pro 500 | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Plus | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 100 | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 200 | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 500 | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6 Luna (medium) on ChatGPT Plus | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6 Luna (medium) on ChatGPT Pro 100 | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6 Luna (medium) on ChatGPT Pro 200 | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6 Luna (medium) on ChatGPT Pro 500 | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6 Luna (xhigh) on ChatGPT Plus | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6 Luna (xhigh) on ChatGPT Pro 100 | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6 Luna (xhigh) on ChatGPT Pro 200 | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6 Luna (xhigh) on ChatGPT Pro 500 | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6.1 Sol (high) on ChatGPT Plus | 0.00 (+0.00) | 0.00 (+0.00) | 1.42 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.52 (+0.00) | 1.48 (+0.00) |
| GPT-6.1 Sol (high) on ChatGPT Pro 100 | 0.00 (+0.00) | 0.00 (+0.00) | 1.42 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.52 (+0.00) | 1.48 (+0.00) |
| GPT-6.1 Sol (high) on ChatGPT Pro 200 | 0.00 (+0.00) | 0.00 (+0.00) | 1.42 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.52 (+0.00) | 1.48 (+0.00) |
| GPT-6.1 Sol (high) on ChatGPT Pro 500 | 0.00 (+0.00) | 0.00 (+0.00) | 1.42 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.52 (+0.00) | 1.48 (+0.00) |
| GPT-6.1 Sol (low) on ChatGPT Plus | 0.00 (+0.00) | 0.00 (+0.00) | 1.69 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.48 (+0.00) | 1.47 (+0.00) |
| GPT-6.1 Sol (low) on ChatGPT Pro 100 | 0.00 (+0.00) | 0.00 (+0.00) | 1.69 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.48 (+0.00) | 1.47 (+0.00) |
| GPT-6.1 Sol (low) on ChatGPT Pro 200 | 0.00 (+0.00) | 0.00 (+0.00) | 1.69 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.48 (+0.00) | 1.47 (+0.00) |
| GPT-6.1 Sol (low) on ChatGPT Pro 500 | 0.00 (+0.00) | 0.00 (+0.00) | 1.69 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.48 (+0.00) | 1.47 (+0.00) |
| GPT-6.1 Sol (medium) on ChatGPT Plus | 0.00 (+0.00) | 0.00 (+0.00) | 1.39 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.52 (+0.00) | 1.50 (+0.00) |
| GPT-6.1 Sol (medium) on ChatGPT Pro 100 | 0.00 (+0.00) | 0.00 (+0.00) | 1.39 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.52 (+0.00) | 1.50 (+0.00) |
| GPT-6.1 Sol (medium) on ChatGPT Pro 200 | 0.00 (+0.00) | 0.00 (+0.00) | 1.39 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.52 (+0.00) | 1.50 (+0.00) |
| GPT-6.1 Sol (medium) on ChatGPT Pro 500 | 0.00 (+0.00) | 0.00 (+0.00) | 1.39 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.52 (+0.00) | 1.50 (+0.00) |
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
| Gemini 4 Argon (high) on API-cost fallback | 0.00 (+0.00) | 0.00 (+0.00) | 1.49 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.58 (+0.00) | 1.56 (+0.00) |
| Kimi K3.1 Pro (max) on API-cost fallback | 0.00 (+0.00) | 0.00 (+0.00) | 1.62 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.49 (+0.00) | 1.47 (+0.00) |
| MiMo-V2.6-Pro on MiMo Token Plan Lite | 0.00 (+0.00) | — | — | — | — | — | — |
| MiMo-V2.6-Pro on MiMo Token Plan Max | 0.00 (+0.00) | — | — | — | — | — | — |
| MiMo-V2.6-Pro on MiMo Token Plan Pro | 0.00 (+0.00) | — | — | — | — | — | — |
| MiMo-V2.6-Pro on MiMo Token Plan Standard | 0.00 (+0.00) | — | — | — | — | — | — |

### Named S2 specification branches

- **Bug Hunt harness band (E19)** (S2): unevaluable; the captured tbench.ai leaderboard lists no configuration under two or more agents, so no cross-agent spread exists
- **cache-hit variation (E34)** (S2): unevaluable; AA's published cost embeds its cache-pricing protocol; varying the cache-hit rate needs each basket component's cache-read and uncached-input demand, which AA publishes only for the whole Index (E157)
- **first-party list versus cross-provider median price rule (E122)** (S2): unevaluable; AA publishes one price per configuration under its own rule; the alternative rule's prices are not captured

### Cheapest-above-the-bar labels (API basis)

The 90% rule's error bound holds per published event (candidate and kernel assignment); it is not corrected across the listed candidates (E198). Each kernel assignment code gives the kernel used for the candidate and the competitors, in that order (U uniform, H endpoint-heavy; a quality-level bar has no reference rows, so it takes no letter); the label needs every assignment met.

| Bar | Candidate | Reading | Frequency range | Kernel assignments | Label |
|---|---|---|---|---|---|
| quality 47.5 | GPT-6.1 Terra (xhigh) | not scenario-supported | 49.5% to 50.5% | UU not met, UH not met, HU not met, HH not met | no |
| quality 47.5 | GPT-6.1 Terra (high) | not scenario-supported | 49.2% to 50.5% | UU not met, UH not met, HU not met, HH not met | no |
| quality 38.0 | GPT-6 Luna (max) | not scenario-supported | 49.9% to 50.6% | UU not met, UH not met, HU not met, HH not met | no |
| quality 56.6 | GPT-6.1 Sol (high) | supported under all registered role-group kernel checks | 100.0% to 100.0% | UU met, UH met, HU met, HH met | yes | These labels carry the workload cross-check warning (E41, O160: τ_b 0.35 on 20 configurations): the basket-cost order behind them agrees weakly with cost per solved task; the attribution is in scores.json `diagnostics.workloadCrossCheck.attribution`.

### AI Coding Daily ranking: diagnostics

- **Terminal-Bench cross-source agreement (AA's mini-SWE-agent run against tbench.ai):** undefined (panel too small); 0 rows take the leaf from tbench.ai (gap fill).
- **Workload cross-check (E41, mandatory diagnostic):** Terminal-Bench 4.0 cost per solved task on AA's own execution against basket cost: τ_b 0.35 (interval -0.07 to 0.67), low agreement; panel (20): Claude Haiku 5.5 (high), Claude Haiku 5.5 (medium), Claude Opus 5.5 (high), Claude Opus 5.5 (medium), DeepSeek V4.1 Flash 1017 (max), Gemini 4 Argon (high), GPT-6 Astra (high), GPT-6 Luna (max), GPT-6 Luna (high), GPT-6 Luna (medium), GPT-6 Luna (xhigh), GPT-6.1 Sol (high), GPT-6.1 Sol (low), GPT-6.1 Sol (medium), GPT-6.1 Terra (max), GPT-6.1 Terra (high), GPT-6.1 Terra (medium), GPT-6.1 Terra (xhigh), Kimi K3.1 Pro (max), MiMo-V2.6-Pro.
- **Rank separability (O39, independent-task approximation):** median separation 4.51 value points (API) and 4.54 (Plan); separable adjacent ranks: API 0 of 19, Plan 0 of 34. Assumptions: tasks are independent and each leaf's score is a mean over its published task count (a binomial leaf drawn from its Jeffreys posterior Beta(k + 1/2, n - k + 1/2), O142; plug-in SDs with the proportion (k + 1/2) / (n + 1), I28); attempts averaged within a task and tasks shared across models are ignored, so the noise is approximate; GDPval-AA: each row's rating interval as AA's model page displays it, read as a 95% normal interval (AA states no level), SD = half-width / 1.96; AA-Omniscience: each of 3,000 questions scores +1, 0 or -1, with the shares from AA's accuracy and hallucination rate; Vals boards (Vibe Code Bench v1.1, Code Migration v1.1): Vals' published standard error per record, read as the leaf's SD; AI Coding Daily: judged points over its six graded projects read as a binomial share of 60 points (an assumption; the board publishes no error).
- **FrontierCode against Cognition:** FrontierCode 2.0 cross-source agreement (AA against Cognition, exact model and effort; E234, O153): Kendall tau 0.91 (interval 0.83 to 0.97) on 26 rows. Cognition minus AA: mean -1.5 points, largest 7.7.
- **Gap-fill removal (E234, diagnostic):** no ranked row has a leaf from another party or the provider.
- **Bar results without the gap fills (E234, sensitivity; labels unchanged):** cheapest displayed row as published, with fills removed, and with third-party fills third-party fills minus the signed mean offset -1.5 points (third party minus AA) — API quality 47.5: GPT-6.1 Terra (high) in all three; API quality 38.0: Claude Haiku 5.5 (high) in all three; API quality 56.6: GPT-6.1 Sol (high) in all three; Plan quality 47.5: GPT-6.1 Terra (high) in all three; Plan quality 38.0: Claude Haiku 5.5 (high) in all three; Plan quality 56.6: Claude Opus 5.5 (high) in all three.
- **Harness cost (O123, S2 stress):** unevaluable: no model is listed under two or more agents in AA's Coding Agent Index capture, so no agent effect is identified (O123). Coding Agent Index agents (each part of its costed configuration; none is the run behind the FrontierCode or Terminal-Bench leaf): GPT-6.1 Terra (max): Codex; DeepSeek V4.1 Flash 1017 (max): DeepSeek Harness; Gemini 4 Argon (high): Antigravity CLI; GPT-6.1 Terra (xhigh): Codex; GPT-6.1 Terra (high): Codex; GPT-6 Luna (max): Codex; GPT-6.1 Terra (medium): Codex.
- **Quality agreement:** quality agreement (matched-panel sensitivity): Kendall tau 0.64 (interval 0.42 to 0.84) on 20 rows.
- **Quality-substitution value agreement (API):** quality-substitution value agreement, api basis (matched-panel sensitivity): Kendall tau 0.45 (interval 0.09 to 0.74) on 20 rows.
- **Quality-substitution value agreement (Plan):** quality-substitution value agreement, plan basis (matched-panel sensitivity): Kendall tau 0.56 (interval 0.24 to 0.84) on 20 rows.
- **Disjoint-evidence agreement:** disjoint-evidence agreement (restricted evidence comparison, not an eligible ranking): Kendall tau 0.52 (interval 0.27 to 0.73) on 20 rows.
- **Quality source shares:** AA-run 78%, independent 22%.
- **Non-discriminating leaves:** lcr.
- **Group drift:** estimated; flagged: none.
- **Omniscience abstention sensitivity** (z_pen = max(0, I)): 10 rows move; largest move 3 (Gemini 4 Argon (high)).
- **GDPval-AA logistic sensitivity** (z = 100 / (1 + 10^((1600 - E) / 400)) against AA's pinned anchor; every other input fixed): API 12 rows move; largest move 4 (MiMo-V2.6-Pro); Plan 9 rows move; largest move 2 (Claude Opus 5.5 (high), Claude Opus 5.5 (medium), GPT-6.1 Terra (max)).
- **Anchor stability:** trimmed anchors (P10 / 2 and P90 x 2 (diagnostic only)) give $33.31 to $5,465.34; 15 rows move; largest move 5 (Kimi K3.1 Pro (max)).

- **Basket readiness (E22):** priced leaves cover 50% of nominal quality weight (AutomationBench-AA, FrontierCode 2.0, Terminal-Bench-Science 0.1, Terminal-Bench 4.0 (AA run)); pending components: Coding Agent Index, ITBench-AA.
- **SWE cost companion (O14, diagnostic):** 7 rows evaluated; flagged far from the median ratio: DeepSeek V4.1 Flash 1017 (max).
- **Matched-cost diagnostic (E55):** evaluated at 63% priced quality weight; basket/matched cost-order reversals with separated intervals: 2; rank-gap warnings: 0.
- **Frontier-families anchors (E187, diagnostic):** anchors rebuilt from the 14 frontier and near-frontier references move API 10 rows move; largest move 3 (GPT-6 Luna (max)) (value points per cost doubling 3.02 vs 2.71 frozen); Plan 10 rows move; largest move 3 (Claude Opus 5.5 (medium)) (value points per cost doubling 4.77 vs 4.11 frozen).
- **Frontier-families bar (E199, sensitivity; the frozen bar stays primary):** quality 46.1 over 15 configurations; cheapest at or above it on the API main workload: not unique; possibly GPT-6.1 Sol (low), GPT-6.1 Terra (high) (compares 10 configurations that can qualify).
- **One row per family (E205, diagnostic; the frozen ladder and anchors stay primary):** with each family's primary configuration only (3 rows in the one-row-per-family bar population), the ladder (headline, lower quartile, upper quartile) would be 38.0 against 47.5 / 38.0 / 56.6 frozen; anchors rebuilt from its 3 references move API 19 rows move; largest move 16 (DeepSeek V4.1 Flash 1017 (max)) (value points per cost doubling 6.16 vs 2.71 frozen); Plan anchors unavailable: fewer than 2 measured references (O157).
- **Ladder over scored rows (I28, sensitivity; the frozen ladder stays primary):** the bar population keeps full-benchmark rows that have no cost; today every such row has a cost, so the ladder is unchanged.
- **Bar currency (E207, informational):** rows reaching each frozen bar: quality 47.5: 11 of 20; quality 38.0: 16 of 20; quality 56.6: 6 of 20; the current population would freeze 47.5 / 38.0 / 56.6; lifetime until the next anchor re-freeze or methodology version, whichever comes first; no staleness flag.
- **Token mix (E208):** 1 selected routes: mix not reported: the measurement publishes no token-category shares; 16 selected routes: mix unidentified: the basket's token-category shares are set-identified only (E124), so the L1 test (above 0.30 flags mix-unmatched) is not computed.
- **Observed-range sensitivity (E219, not evidence; no label changes):** with each missing leaf inside the cohort's observed range for that leaf, quality 47.5: 9 can qualify, 8 confirmed; possibly cheapest GPT-6.1 Terra (xhigh), GPT-6.1 Terra (high); quality 38.0: 13 can qualify, 13 confirmed; possibly cheapest GPT-6 Luna (max); quality 56.6: 5 can qualify, 4 confirmed; GPT-6.1 Sol (high) confirmed cheapest.
- **What would settle the headline bar (E221, not a claim):** rows that can but need not reach quality 47.5, with the mean score their missing leaves would need: GPT-6.1 Terra (high) (no missing leaf; reporting precision only).
- **Common leaf set (E226, diagnostic; scores unchanged):** without the leaves fewer than 90% of cohort rows have (none), API no rank changes; Plan no rank changes; rows reaching each bar: quality 47.5: 11 → 11; quality 38.0: 16 → 16; quality 56.6: 6 → 6; rows whose displayed quality differs from common-leaf quality by more than one cost doubling's worth: none.
- **Harness by leaf (E227):** Terminal-Bench: mini-SWE-agent 20; Bug Hunt: Codex CLI 12, Claude Code 4, Antigravity CLI 1, Claude Code / Moonshot API 1, Claude Code / Xiaomi first-party 1, DeepSeek Harness / DeepSeek API 1; AI Coding Daily: Codex CLI 12, Claude Code 4, OpenCode 2, DeepSeek Harness 1, Devin 1.
- **Coding Agent Index safety refusals (O63, flagged; costs and scores unchanged):** none.

### Leave-one-component-out cost family (E172)

Each admitted basket unit removed in turn, scored on anchors rebuilt by the freeze rule (rank changes against the primary ranking; quality held fixed).

| Removed component | API rank changes | Plan rank changes | API value points per cost doubling |
|---|---|---|---:|
| AA-Briefcase | 9 rows move; largest move 2 (Claude Opus 5.5 (high)) | 8 rows move; largest move 3 (Claude Opus 5.5 (medium), GPT-6.1 Terra (max)) | 2.74 |
| GDP.pdf | no rank changes | 13 rows move; largest move 3 (GPT-6.1 Sol (low), GPT-6.1 Terra (xhigh)) | 2.69 |
| AutomationBench-AA | 5 rows move; largest move 2 (GPT-6.1 Sol (low)) | 14 rows move; largest move 4 (GPT-6.1 Sol (low)) | 2.62 |
| Terminal-Bench 4.0 (AA Index run) | 6 rows move; largest move 1 (Claude Opus 5.5 (high), Claude Opus 5.5 (medium), GPT-6.1 Sol (high), GPT-6.1 Terra (max), GPT-6.1 Terra (medium), MiMo-V2.6-Pro) | 11 rows move; largest move 3 (Claude Opus 5.5 (medium)) | 2.71 |
| FrontierCode 2.0 | 13 rows move; largest move 2 (Claude Opus 5.5 (medium)) | 9 rows move; largest move 2 (Claude Opus 5.5 (high)) | 2.80 |
| Terminal-Bench-Science | 6 rows move; largest move 2 (Claude Opus 5.5 (high), GPT-6.1 Sol (low)) | 8 rows move; largest move 2 (Claude Opus 5.5 (medium), GPT-6.1 Terra (max)) | 2.70 |

### Subset rows: paired bridge and missing spend (E10, E173)

No row is scored on a subset workload.

### Deletion sensitivity

| Branch | Retained nominal weight | Status | API rank changes | Plan rank changes |
|---|---:|---|---|---|
| leave-out:frontierCode | 79% | evaluated | 15 rows move; largest move 4 (GPT-6.1 Terra (medium)) | 11 rows move; largest move 4 (GPT-6.1 Sol (low)) |
| leave-out:terminalBench | 83% | evaluated | 14 rows move; largest move 8 (GPT-6 Luna (max)) | 17 rows move; largest move 3 (GPT-6.1 Sol (low), GPT-6.1 Terra (high), GPT-6.1 Terra (xhigh)) |
| leave-out:bugHunt | 88% | evaluated | 16 rows move; largest move 9 (DeepSeek V4.1 Flash 1017 (max)) | 15 rows move; largest move 6 (GPT-6.1 Terra (max)) |
| leave-out:aiCodingDaily | 90% | evaluated | 10 rows move; largest move 3 (Gemini 4 Argon (high)) | 9 rows move; largest move 2 (GPT-6 Luna (max)) |
| leave-out:gdpval | 90% | evaluated | 11 rows move; largest move 2 (Gemini 4 Argon (high)) | 7 rows move; largest move 3 (GPT-6 Luna (max)) |
| leave-out:automationBench | 90% | evaluated | 10 rows move; largest move 3 (Claude Haiku 5.5 (medium)) | 5 rows move; largest move 2 (GPT-6.1 Sol (low)) |
| leave-out:omniscience | 90% | evaluated | 10 rows move; largest move 4 (GPT-6.1 Sol (low)) | 7 rows move; largest move 2 (GPT-6 Luna (max)) |
| leave-out:lcr | 95% | evaluated | 6 rows move; largest move 2 (Claude Opus 5.5 (high), Gemini 4 Argon (high)) | 2 rows move; largest move 1 (GPT-6 Luna (max), GPT-6.1 Terra (medium)) |
| leave-out:hle | 98% | evaluated | 3 rows move; largest move 2 (Claude Opus 5.5 (medium)) | 2 rows move; largest move 1 (Claude Opus 5.5 (high), GPT-6.1 Sol (medium)) |
| leave-out:tbScience | 98% | evaluated | 3 rows move; largest move 2 (Claude Opus 5.5 (medium)) | 2 rows move; largest move 1 (Claude Opus 5.5 (high), GPT-6.1 Sol (medium)) |
| leave-out:critpt | 98% | evaluated | 4 rows move; largest move 1 (Claude Opus 5.5 (high), Claude Opus 5.5 (medium), GPT-6.1 Terra (medium), MiMo-V2.6-Pro) | 2 rows move; largest move 1 (Claude Opus 5.5 (medium), GPT-6.1 Sol (medium)) |
| leave-source-out:Artificial Analysis | 22% | not identifiable under the coverage rule | — | — |
| basket-scope | 87% | evaluated | 10 rows move; largest move 4 (GPT-6 Luna (max), GPT-6.1 Sol (low), MiMo-V2.6-Pro) | 13 rows move; largest move 2 (GPT-6 Luna (max)) |

### Cost-component removal (Terminal-Bench 4.0 (AA Index run): evaluated)

| Basis | Run | Rank changes |
|---|---|---|
| api | cost-component removal, original anchors | 6 rows move; largest move 1 (Claude Opus 5.5 (high), Claude Opus 5.5 (medium), GPT-6.1 Sol (high), GPT-6.1 Terra (max), GPT-6.1 Terra (medium), MiMo-V2.6-Pro) |
| api | alternative workload, recalibrated anchors | 6 rows move; largest move 1 (Claude Opus 5.5 (high), Claude Opus 5.5 (medium), GPT-6.1 Sol (high), GPT-6.1 Terra (max), GPT-6.1 Terra (medium), MiMo-V2.6-Pro) |
| plan | cost-component removal, original anchors; fixed-multiple arithmetic stress (not identified Plan economics for the altered workload) | 7 rows move; largest move 2 (GPT-6 Luna (max)) |
| plan | alternative workload, recalibrated anchors; fixed-multiple arithmetic stress (not identified Plan economics for the altered workload) | 11 rows move; largest move 3 (Claude Opus 5.5 (medium)) |

### AI Coding Daily ranking: release gates

| Rule | Status | Detail |
|---|---|---|
| clip gate (E20) | passed | no basis exceeds the clipping allowance |
| cost influence flag (E91) | passed | cost not discriminating (< 10%); informational only; beta never changes (O2) |
| realised influence (E272) | fired | API: cost term offsetting (-56% of value variance); informational only, beta never changes (O2) |
| quality influence flag (E126) | passed | quality not discriminating (cost share > 90%); informational only |
| subset scoring (O17) | vacuous | subset rows scored on their own workload and anchors |
| partial component flag (E37) | fired | AA declined- or missing-task markers, or an Index reconstruction that misses AA's total (E209) |
| route dominance filter (E88) | vacuous | certifiably dearer routes set aside |
| Plan exploratory label (E61) | fired | fewer than half of Plan rows have an identified M_W |
| Plan evidence lifecycle and change detection (E18, E151, E269, O77, O79) | fired | 60 of 67 plan rows carry a possibly-superseded or expired route: claude-haiku-5-5-high@claude-max-20x, claude-haiku-5-5-high@claude-max-5x, claude-haiku-5-5-high@claude-pro, claude-haiku-5-5-medium@claude-max-20x, claude-haiku-5-5-medium@claude-max-5x, claude-haiku-5-5-medium@claude-pro, claude-opus-5-5-high@claude-max-20x, claude-opus-5-5-high@claude-max-5x, claude-opus-5-5-high@claude-pro, claude-opus-5-5-medium@claude-max-20x, claude-opus-5-5-medium@claude-max-5x, claude-opus-5-5-medium@claude-pro, gpt-6-astra-high@chatgpt-plus, gpt-6-astra-high@chatgpt-pro-100, gpt-6-astra-high@chatgpt-pro-200, gpt-6-astra-high@chatgpt-pro-500, gpt-6-luna-high@chatgpt-plus, gpt-6-luna-high@chatgpt-pro-100, gpt-6-luna-high@chatgpt-pro-200, gpt-6-luna-high@chatgpt-pro-500, gpt-6-luna-medium@chatgpt-plus, gpt-6-luna-medium@chatgpt-pro-100, gpt-6-luna-medium@chatgpt-pro-200, gpt-6-luna-medium@chatgpt-pro-500, gpt-6-luna-xhigh@chatgpt-plus, gpt-6-luna-xhigh@chatgpt-pro-100, gpt-6-luna-xhigh@chatgpt-pro-200, gpt-6-luna-xhigh@chatgpt-pro-500, gpt-6-luna@chatgpt-plus, gpt-6-luna@chatgpt-pro-100, gpt-6-luna@chatgpt-pro-200, gpt-6-luna@chatgpt-pro-500, gpt-6.1-sol-high@chatgpt-plus, gpt-6.1-sol-high@chatgpt-pro-100, gpt-6.1-sol-high@chatgpt-pro-200, gpt-6.1-sol-high@chatgpt-pro-500, gpt-6.1-sol-low@chatgpt-plus, gpt-6.1-sol-low@chatgpt-pro-100, gpt-6.1-sol-low@chatgpt-pro-200, gpt-6.1-sol-low@chatgpt-pro-500, gpt-6.1-sol-medium@chatgpt-plus, gpt-6.1-sol-medium@chatgpt-pro-100, gpt-6.1-sol-medium@chatgpt-pro-200, gpt-6.1-sol-medium@chatgpt-pro-500, gpt-6.1-terra-high@chatgpt-plus, gpt-6.1-terra-high@chatgpt-pro-100, gpt-6.1-terra-high@chatgpt-pro-200, gpt-6.1-terra-high@chatgpt-pro-500, gpt-6.1-terra-medium@chatgpt-plus, gpt-6.1-terra-medium@chatgpt-pro-100, gpt-6.1-terra-medium@chatgpt-pro-200, gpt-6.1-terra-medium@chatgpt-pro-500, gpt-6.1-terra-xhigh@chatgpt-plus, gpt-6.1-terra-xhigh@chatgpt-pro-100, gpt-6.1-terra-xhigh@chatgpt-pro-200, gpt-6.1-terra-xhigh@chatgpt-pro-500, gpt-6.1-terra@chatgpt-plus, gpt-6.1-terra@chatgpt-pro-100, gpt-6.1-terra@chatgpt-pro-200, gpt-6.1-terra@chatgpt-pro-500 |
| acknowledged accounting-fault windows (O91, O92, O93, O95, O96) | fired | 12 of 67 plan rows rest on a measurement inside an acknowledged fault window; they stay selected and yield to two concordant user reports for their own model and plan, and the transfers resting on them follow: gpt-6-astra-high@chatgpt-pro-500, gpt-6-luna-high@chatgpt-pro-500, gpt-6-luna-medium@chatgpt-pro-500, gpt-6-luna-xhigh@chatgpt-pro-500, gpt-6-luna@chatgpt-pro-500, gpt-6.1-sol-high@chatgpt-pro-500, gpt-6.1-sol-low@chatgpt-pro-500, gpt-6.1-sol-medium@chatgpt-pro-500, gpt-6.1-terra-high@chatgpt-pro-500, gpt-6.1-terra-medium@chatgpt-pro-500, gpt-6.1-terra-xhigh@chatgpt-pro-500, gpt-6.1-terra@chatgpt-pro-500 |
| AA cost omits a pricing term (O94, O98, O100, O106, O108, O109, O114) | fired | ranked at the published cost; compete in interval outputs and the scenario labels' BlockerSafe test over [C, factor × C] ([C, ∞) without a stated factor, O98) without a label (scenario frequencies draw them at the published cost, O114), and leave the anchor population at the next freeze: claude-haiku-5-5-high (up to 5×), claude-haiku-5-5-medium (up to 5×) |
| valuation-basis gate (E170) | passed | every ranked row is compatible as captured or after evidenced revaluation |
| source clocks and evidence freshness (O59, O60, O65, E211, E216, E217, E218) | passed | every capture is within its age gate and none after the cutoff unless its source predates the cutoff's day; the build stops otherwise |
| build-stopping evidence gates (O64, O69, O71, O75, O99, O100, O101, O103, O105-O111, E195, E204, E225) | passed | the Coding Agent Index manifest (O64), the Terminal-Bench agent list (E225), cutoff-day row dates (O69), the three-stage all-provider plan search (O71, O75), the typed change records behind every route flag and partition split, which also produce each route's label and blocking dates within its launch- and schedule-bounded span (O99, O101, O105, O107, O110, O111), the register of AA notes covering every captured one, with the chart's inventory and duplicate-entry checks, the post-O103 capture notes, the basket-chart labels and chart-level notes' named rows (O100, O103, O106, O108) and the frontier path checks (E195, E204) hold; the build stops otherwise |
| score swing gate (E177) | vacuous | first v3 release: no previous v3 release to compare |
| ranking coverage (O166) | vacuous | ranks 20 of 37 cohort configurations; first v3 release: no previous v3 release to compare |
| anchor migration (E184) | vacuous | no main-workload migration deferred |
| frozen admission (O169) | vacuous | every frozen component still meets the admission threshold |
| configuration map coverage | fired | cohort rows without a configuration-map entry (chart labels; the agent record is derived, E267): gpt-6.1-terra, gpt-6.1-terra-high, gpt-6.1-terra-medium, gpt-6.1-terra-xhigh |
| quality clipping audit (E110) | passed | saturation disclosed; domain violations block the build |
| full benchmark set (O36, O38) | fired | listed, not ranked: gpt-6.1-sol, claude-opus-5-5, claude-sonnet-5-5, gpt-6-astra, claude-haiku-5-5-max, claude-haiku-5-5-low, claude-haiku-5-5, claude-opus-5-5-xhigh, claude-sonnet-5-5-xhigh, gpt-5.6-luna-low, gpt-6-astra-xhigh, gpt-6-luna-low, gpt-6.1-sol-xhigh, gpt-6.1-terra-low, gemini-4-carbon, mimo-v2-6-flash, minimax-m3-1-flash |
| missing-leaf rules (O8 provisional, E198b, E201b, E219, E221, E226) | vacuous | no ranked row has a missing leaf (O36) |
| S1M interval stream (E145) | vacuous | dormant: no ranked leaf carries a published confidence interval since O37, so S1M equals S1 (E236) |
| provider-claim label denial (E233) | vacuous | no row has a provider-claimed leaf |
| scenario outputs current (E72) | passed | scenario input hash matches the scored inputs |

## Common-leaf ranking (diagnostic)

Diagnostic only (O121): every configuration with AA's leaves and Bug Hunt, at any effort, scored on the ten leaves the two leading rankings share; it earns no label and never holds a release. Anchor version `v3-2026-11-01-a3-common`; leaves: FrontierCode 2.0 25%, Terminal-Bench 4.0 (AA run) 20%, Bug Hunt Bench 15% (software engineering 60%), plus the 7 leaves outside software engineering every ranking shares.

**Diagnostic ranking (O121).** It earns no interval or scenario label and its clip gate (passes on its own) never holds the release. Its bars sit at the same ladder positions as the leading rankings' but at its own levels, so the comparison below asks whether a configuration the leading rankings cannot rank would answer the same question. The answers are displayed records, not claims: a difference smaller than this ranking's quality noise margin (5.1 points, O44) is not evidence.

| Basis | Bar position | Cheapest here | Cheapest, max-effort ranking | Cheapest, AI Coding Daily ranking |
|---|---|---|---|---|
| API | median | GPT-6.1 Sol (medium) | GPT-6.1 Sol (max) (differs) | GPT-6.1 Terra (high) (differs) |
| API | lower quartile | GPT-6 Luna (max) | DeepSeek V4.1 Flash 1017 (max) (differs) | Claude Haiku 5.5 (high) (differs) |
| API | upper quartile | GPT-6.1 Sol (xhigh) | GPT-6.1 Sol (max) (differs) | GPT-6.1 Sol (high) (differs) |
| Plan | median | Claude Opus 5.5 (medium) on Claude Pro | GPT-6.1 Sol (max) on ChatGPT Pro 500 (differs) | GPT-6.1 Terra (high) on ChatGPT Pro 500 (differs) |
| Plan | lower quartile | Claude Haiku 5.5 (xhigh) on Claude Pro | Claude Haiku 5.5 (max) on Claude Pro (differs) | Claude Haiku 5.5 (high) on Claude Pro (differs) |
| Plan | upper quartile | GPT-6.1 Sol (xhigh) on ChatGPT Pro 500 | GPT-6.1 Sol (max) on ChatGPT Pro 500 (differs) | Claude Opus 5.5 (high) on Claude Pro (differs) |

| Configuration | Plan rank | Plan value | Plan cost score | API rank | API value | API cost score | Quality | Quality coverage | Workload |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| [GPT-6.1 Sol (xhigh)](https://valuerank.alolabs.dev/models/gpt-6-1-sol-xhigh/) | 1 | 61.93 | 63.86 | 2 | 55.42 | 37.82 | 61.29 | 100% | main |
| [GPT-6.1 Sol (max)](https://valuerank.alolabs.dev/models/gpt-6-1-sol/) | 2 | 61.82 | 54.73 | 1 | 56.26 | 32.50 | 64.18 | 100% | main |
| [GPT-6.1 Terra (max)](https://valuerank.alolabs.dev/models/gpt-6-1-terra/) | 9 | 59.88 | 61.55 | 3 | 53.62 | 36.48 | 59.33 | 100% | main |
| [GPT-6.1 Sol (high)](https://valuerank.alolabs.dev/models/gpt-6-1-sol-high/) | 12 | 59.31 | 67.90 | 4 | 52.38 | 40.18 | 56.44 | 100% | main |
| [Claude Sonnet 5.5 (max)](https://valuerank.alolabs.dev/models/claude-sonnet-5-5/) | 16 | 58.91 | 49.55 | 8 | 48.65 | 8.54 | 62.03 | 100% | main |
| [Claude Opus 5.5 (xhigh)](https://valuerank.alolabs.dev/models/claude-opus-5-5-xhigh/) | 20 | 58.26 | 59.16 | 12 | 47.01 | 14.15 | 57.96 | 100% | main |
| [GPT-6.1 Sol (medium)](https://valuerank.alolabs.dev/models/gpt-6-1-sol-medium/) | 23 | 57.47 | 75.20 | 7 | 49.78 | 44.44 | 51.56 | 100% | main |
| [Claude Opus 5.5 (high)](https://valuerank.alolabs.dev/models/claude-opus-5-5-high/) | 26 | 57.35 | 70.36 | 15 | 44.93 | 20.69 | 53.01 | 100% | main |
| [Claude Sonnet 5.5 (xhigh)](https://valuerank.alolabs.dev/models/claude-sonnet-5-5-xhigh/) | 30 | 57.12 | 69.27 | 16 | 44.82 | 20.05 | 53.08 | 100% | main |
| [Claude Opus 5.5 (medium)](https://valuerank.alolabs.dev/models/claude-opus-5-5-medium/) | 32 | 57.01 | 76.36 | 18 | 43.96 | 24.18 | 50.56 | 100% | main |
| [Claude Opus 5.5 (max)](https://valuerank.alolabs.dev/models/claude-opus-5-5/) | 36 | 56.84 | 48.30 | 13 | 46.72 | 7.81 | 59.69 | 100% | main |
| [GPT-6 Astra (xhigh)](https://valuerank.alolabs.dev/models/gpt-6-astra-xhigh/) | 39 | 56.13 | 35.44 | 5 | 51.67 | 17.60 | 63.03 | 100% | main |
| [Claude Haiku 5.5 (max)](https://valuerank.alolabs.dev/models/claude-haiku-5-5-max/) | 42 | 55.25 | 100.00 | 21 | 42.24 | 47.98 | 40.33 | 100% | main |
| [GPT-6 Astra (max)](https://valuerank.alolabs.dev/models/gpt-6-astra/) | 45 | 54.83 | 26.92 | 6 | 51.25 | 12.63 | 64.13 | 100% | main |
| [GPT-6.1 Terra (xhigh)](https://valuerank.alolabs.dev/models/gpt-6-1-terra-xhigh/) | 48 | 53.92 | 77.06 | 14 | 46.04 | 45.52 | 46.21 | 100% | main |
| [GPT-6.1 Terra (high)](https://valuerank.alolabs.dev/models/gpt-6-1-terra-high/) | 51 | 53.25 | 84.08 | 17 | 44.64 | 49.62 | 42.98 | 100% | main |
| [GPT-6 Astra (high)](https://valuerank.alolabs.dev/models/gpt-6-astra-high/) | 52 | 53.23 | 37.91 | 9 | 48.51 | 19.04 | 58.33 | 100% | main |
| [Claude Haiku 5.5 (xhigh)](https://valuerank.alolabs.dev/models/claude-haiku-5-5/) | 58 | 52.47 | 100.00 | 24 | 41.01 | 54.16 | 36.63 | 100% | main |
| [GPT-6.1 Terra (medium)](https://valuerank.alolabs.dev/models/gpt-6-1-terra-medium/) | 62 | 52.19 | 90.49 | 20 | 42.91 | 53.36 | 39.42 | 100% | main |
| [GPT-6.1 Sol (low)](https://valuerank.alolabs.dev/models/gpt-6-1-sol-low/) | 67 | 51.68 | 85.36 | 19 | 42.93 | 50.37 | 40.45 | 100% | main |
| [GPT-6 Luna (max)](https://valuerank.alolabs.dev/models/gpt-6-luna/) | 71 | 51.16 | 99.75 | 25 | 40.92 | 58.76 | 34.97 | 100% | main |
| [Claude Haiku 5.5 (high)](https://valuerank.alolabs.dev/models/claude-haiku-5-5-high/) | 77 | 48.65 | 100.00 | 27 | 38.49 | 59.33 | 31.54 | 100% | main |
| [GPT-6.1 Terra (low)](https://valuerank.alolabs.dev/models/gpt-6-1-terra-low/) | 80 | 48.62 | 100.00 | 26 | 38.53 | 59.66 | 31.49 | 100% | main |
| [GPT-6 Luna (xhigh)](https://valuerank.alolabs.dev/models/gpt-6-luna-xhigh/) | 84 | 46.46 | 100.00 | 28 | 37.35 | 63.57 | 28.61 | 100% | main |
| [GPT-6 Luna (high)](https://valuerank.alolabs.dev/models/gpt-6-luna-high/) | 88 | 44.83 | 100.00 | 29 | 36.64 | 67.21 | 26.45 | 100% | main |
| [Claude Haiku 5.5 (medium)](https://valuerank.alolabs.dev/models/claude-haiku-5-5-medium/) | 92 | 44.65 | 100.00 | 30 | 35.96 | 65.23 | 26.20 | 100% | main |
| [DeepSeek V4.1 Flash 1017 (max)](https://valuerank.alolabs.dev/models/deepseek-v4-1-flash-1017/) | 95 | 42.63 | 20.53 | 10 | 47.96 | 41.84 | 50.00 | 100% | main |
| [Kimi K3.1 Pro (max)](https://valuerank.alolabs.dev/models/kimi-k3-1-pro/) | 96 | 42.35 | 0.00 | 11 | 47.34 | 19.96 | 56.47 | 100% | main |
| [Claude Haiku 5.5 (low)](https://valuerank.alolabs.dev/models/claude-haiku-5-5-low/) | 97 | 40.95 | 100.00 | 31 | 34.09 | 72.57 | 21.26 | 100% | main |
| [GPT-6 Luna (medium)](https://valuerank.alolabs.dev/models/gpt-6-luna-medium/) | 100 | 40.86 | 100.00 | 32 | 34.02 | 72.66 | 21.14 | 100% | main |
| [MiMo-V2.6-Pro](https://valuerank.alolabs.dev/models/mimo-v2-6-pro/) | 104 | 39.61 | 44.18 | 23 | 41.96 | 53.59 | 38.08 | 100% | main |
| [Gemini 4 Argon (high)](https://valuerank.alolabs.dev/models/gemini-4-argon/) | 105 | 39.33 | 0.00 | 22 | 42.06 | 10.92 | 52.43 | 100% | main |
| [GPT-6 Luna (low)](https://valuerank.alolabs.dev/models/gpt-6-luna-low/) | 109 | 35.91 | 100.00 | 33 | 33.77 | 91.46 | 14.55 | 100% | main |

### Common-leaf ranking (diagnostic): quality leaf scores

| Configuration | FrontierCode 2.0 | Terminal-Bench 4.0 (AA run) | Bug Hunt Bench | GDPval-AA v2.1 | AutomationBench-AA | AA-Omniscience v1.1 | AA-LCR v1.1 | HLE-Diamond | Terminal-Bench-Science 0.1 | CritPt v2 (hard subset) | Quality | Provisional |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| GPT-6.1 Sol (xhigh) | 38.5 | 54.0 | 99.4 | 52.7 | 66.6 | 71.2 | 79.7 | 55.8 | 50.5 | 68.0 | 61.29 | no |
| GPT-6.1 Sol (max) | 40.6 | 56.1 | 109.6 | 55.4 | 64.9 | 71.0 | 83.0 | 58.8 | 58.1 | 68.5 | 64.18 | no |
| GPT-6.1 Terra (max) | 42.3 | 55.6 | 88.7 | 48.8 | 60.2 | 64.8 | 82.7 | 47.3 | 57.6 | 64.5 | 59.33 | no |
| GPT-6.1 Sol (high) | 36.7 | 51.5 | 76.5 | 51.0 | 64.5 | 70.5 | 82.3 | 51.9 | 46.2 | 67.5 | 56.44 | no |
| Claude Sonnet 5.5 (max) | 41.7 | 63.6 | 77.6 | 66.9 | 71.8 | 65.2 | 82.7 | 53.3 | 53.3 | 56.0 | 62.03 | no |
| Claude Opus 5.5 (xhigh) | 43.8 | 59.6 | 49.3 | 66.8 | 65.0 | 71.6 | 84.7 | 64.0 | 61.9 | 63.0 | 57.96 | no |
| GPT-6.1 Sol (medium) | 33.4 | 48.0 | 59.5 | 48.0 | 62.6 | 70.1 | 83.3 | 46.0 | 37.1 | 65.0 | 51.56 | no |
| Claude Opus 5.5 (high) | 35.9 | 56.6 | 42.4 | 60.7 | 63.2 | 71.2 | 82.7 | 55.6 | 49.0 | 58.0 | 53.01 | no |
| Claude Sonnet 5.5 (xhigh) | 35.6 | 57.1 | 50.0 | 61.8 | 65.5 | 60.3 | 79.7 | 44.1 | 52.4 | 54.0 | 53.08 | no |
| Claude Opus 5.5 (medium) | 33.1 | 52.5 | 43.6 | 54.6 | 61.2 | 69.9 | 84.3 | 51.4 | 43.3 | 52.5 | 50.56 | no |
| Claude Opus 5.5 (max) | 46.4 | 59.6 | 50.7 | 68.3 | 69.5 | 74.1 | 84.7 | 67.9 | 59.0 | 61.0 | 59.69 | no |
| GPT-6 Astra (xhigh) | 41.4 | 59.6 | 96.0 | 53.5 | 67.2 | 71.8 | 80.0 | 61.5 | 54.8 | 70.5 | 63.03 | no |
| Claude Haiku 5.5 (max) | 34.9 | 32.8 | 30.5 | 56.5 | 35.4 | 56.1 | 82.7 | 29.6 | 20.0 | 41.0 | 40.33 | no |
| GPT-6 Astra (max) | 42.4 | 59.1 | 100.0 | 54.2 | 68.5 | 71.2 | 80.7 | 63.8 | 63.3 | 70.5 | 64.13 | no |
| GPT-6.1 Terra (xhigh) | 36.9 | 46.5 | 28.3 | 45.7 | 59.9 | 64.5 | 81.7 | 42.3 | 41.9 | 57.5 | 46.21 | no |
| GPT-6.1 Terra (high) | 37.5 | 41.9 | 16.4 | 42.6 | 58.5 | 63.9 | 82.3 | 35.4 | 33.3 | 60.5 | 42.98 | no |
| GPT-6 Astra (high) | 40.1 | 54.0 | 75.0 | 51.8 | 66.6 | 72.3 | 80.0 | 59.3 | 59.5 | 71.5 | 58.33 | no |
| Claude Haiku 5.5 (xhigh) | 29.9 | 29.3 | 25.0 | 51.1 | 36.0 | 53.9 | 78.3 | 28.8 | 18.1 | 44.5 | 36.63 | no |
| GPT-6.1 Terra (medium) | 34.5 | 32.3 | 14.6 | 41.2 | 57.8 | 63.3 | 80.7 | 31.3 | 24.8 | 56.0 | 39.42 | no |
| GPT-6.1 Sol (low) | 20.2 | 30.8 | 46.5 | 41.1 | 52.6 | 69.0 | 84.0 | 38.2 | 11.0 | 59.5 | 40.45 | no |
| GPT-6 Luna (max) | 25.2 | 12.6 | 41.0 | 47.2 | 53.2 | 45.9 | 83.3 | 22.2 | 8.6 | 41.5 | 34.97 | no |
| Claude Haiku 5.5 (high) | 23.2 | 21.7 | 20.0 | 46.2 | 33.7 | 52.6 | 77.3 | 23.7 | 10.0 | 42.5 | 31.54 | no |
| GPT-6.1 Terra (low) | 24.5 | 15.2 | 11.0 | 35.2 | 56.2 | 61.5 | 81.0 | 24.9 | 7.6 | 48.5 | 31.49 | no |
| GPT-6 Luna (xhigh) | 18.4 | 8.1 | 26.0 | 43.6 | 47.8 | 43.5 | 80.0 | 18.9 | 5.2 | 35.5 | 28.61 | no |
| GPT-6 Luna (high) | 18.6 | 4.5 | 18.0 | 42.6 | 47.8 | 43.6 | 79.3 | 15.6 | 2.9 | 30.5 | 26.45 | no |
| Claude Haiku 5.5 (medium) | 16.1 | 15.2 | 16.0 | 39.1 | 28.6 | 52.1 | 77.3 | 16.8 | 7.1 | 30.0 | 26.20 | no |
| DeepSeek V4.1 Flash 1017 (max) | 28.5 | 33.8 | 86.7 | 62.3 | 66.6 | 50.5 | 82.7 | 25.3 | 12.9 | 24.0 | 50.00 | no |
| Kimi K3.1 Pro (max) | 25.5 | 67.2 | 65.3 | 67.9 | 73.3 | 64.9 | 86.3 | 37.3 | 34.3 | 45.0 | 56.47 | no |
| Claude Haiku 5.5 (low) | 8.0 | 12.6 | 13.0 | 31.5 | 22.9 | 51.1 | 72.0 | 14.1 | 1.9 | 21.5 | 21.26 | no |
| GPT-6 Luna (medium) | 12.8 | 2.5 | 4.0 | 38.5 | 40.5 | 43.2 | 78.3 | 15.1 | 1.4 | 26.0 | 21.14 | no |
| MiMo-V2.6-Pro | 24.0 | 34.8 | 22.0 | 59.5 | 58.6 | 47.8 | 86.3 | 15.2 | 5.7 | 34.0 | 38.08 | no |
| Gemini 4 Argon (high) | 25.7 | 57.1 | 48.0 | 56.5 | 77.5 | 73.0 | 79.7 | 56.7 | 52.9 | 52.5 | 52.43 | no |
| GPT-6 Luna (low) | 2.2 | 0.0 | 13.0 | 27.0 | 12.0 | 41.0 | 74.0 | 10.2 | 1.0 | 9.5 | 14.55 | no |

### Common-leaf ranking (diagnostic): displayed record and noise

- API basis, displayed record (not a claim; E203): cheapest at or above quality 50.0: GPT-6.1 Sol (medium) ($360.71 per basket run; 17 reach it); at or above quality 35.0: GPT-6 Luna (max) ($112.84 per basket run; 25 reach it); at or above quality 58.0: GPT-6.1 Sol (xhigh) ($617.20 per basket run; 9 reach it).
- API basis, cheaper same-family efforts on AA's chart that this ranking could not evaluate (O143, E201c): below GPT-6 Luna (max): GPT-6 Luna (non-reasoning).
- API basis, noise-margin companion (O44; each bar plus 5.1 quality points, so the bar's own configuration cannot decide it): cheapest at or above quality 55.1: GPT-6.1 Sol (high) ($509.65 per basket run); at or above quality 40.0: GPT-6.1 Sol (low) ($223.06 per basket run); at or above quality 63.0: GPT-6.1 Sol (max) ($950.68 per basket run).
- Plan basis, displayed record (not a claim; E203): cheapest at or above quality 50.0: Claude Opus 5.5 (medium) on Claude Pro ($31.71 per basket run; 53 reach it); at or above quality 35.0: Claude Haiku 5.5 (xhigh) on Claude Pro ($2.78 per basket run; 83 reach it); at or above quality 58.0: GPT-6.1 Sol (xhigh) on ChatGPT Pro 500 ($57.30 per basket run; 33 reach it).
- Plan basis, cheaper same-family efforts on AA's chart that this ranking could not evaluate (O143, E201c): below Claude Opus 5.5 (medium): Claude Opus 5.5 (low with fallback).
- Plan basis, noise-margin companion (O44; each bar plus 5.1 quality points, so the bar's own configuration cannot decide it): cheapest at or above quality 55.1: GPT-6.1 Sol (high) on ChatGPT Pro 500 ($47.31 per basket run); at or above quality 40.0: Claude Haiku 5.5 (max) on Claude Pro ($4.60 per basket run); at or above quality 63.0: GPT-6.1 Sol (max) on ChatGPT Pro 500 ($88.25 per basket run).
- Safety-refusal flags (O63; costs and scores unchanged) on these bars' cheapest rows: Claude Haiku 5.5 (max) (0 blocked and 3 fallback attempts of 870); GPT-6.1 Sol (max) (15 blocked and 0 fallback attempts of 870).
- AA cost caveat (O94; ranked at the published cost, no label of its own) on these bars' cheapest rows: Claude Haiku 5.5 (xhigh) (AA's cost omits a pricing term; up to 5× on its cost); Claude Haiku 5.5 (max) (AA's cost omits a pricing term; up to 5× on its cost).
- Plan route flags on these bars' cheapest plan rows: Claude Haiku 5.5 (max) on Claude Pro (possibly-superseded); Claude Haiku 5.5 (xhigh) on Claude Pro (possibly-superseded); Claude Opus 5.5 (medium) on Claude Pro (possibly-superseded); GPT-6.1 Sol (high) on ChatGPT Pro 500 (possibly-superseded, measured inside an acknowledged accounting-fault window (O91, O92)); GPT-6.1 Sol (xhigh) on ChatGPT Pro 500 (possibly-superseded, measured inside an acknowledged accounting-fault window (O91, O92)); GPT-6.1 Sol (max) on ChatGPT Pro 500 (possibly-superseded, measured inside an acknowledged accounting-fault window (O91, O92)).
- These outputs compare ranked configurations only; listed families shown with an indicative value (O41) are outside them (O43): GPT-5.6 Luna, Gemini 4 Carbon, MiMo-V2.6-Flash, MiniMax-M3.1-Flash.

Benchmark sampling noise (O39, an independent-task approximation): two values must differ by about 3.8 value points (median, 95%) to separate, and 0 of 32 adjacent API ranks and 1 of 49 adjacent Plan ranks of different configurations do (62 more adjacent Plan pairs are one configuration on two plans, ordered by the plans' multiples alone; E258). Its net direction is not established: every configuration is scored on the same tasks, which correlates their errors and narrows the true threshold (API 0 at correlation 0.3, 2 at correlation 0.6; Plan 1 at correlation 0.3, 1 at correlation 0.6), while sources it leaves out widen it (run-to-run and harness variance, AA's single cost run and, for the 65 Plan rows on an owner assumption (61 owner-named transfers and 4 O46 provider quota ceilings), that assumption's error). The noise band column groups each row with the band's first row it cannot be told apart from (O42); a Plan band marked † rests on an owner assumption (an owner-named transfer or an O46 provider quota ceiling) and excludes its error: an assumed multiple can be wrong by a factor of about 2.1 before the row's value moves by the median threshold (a tolerance, not an estimate of the assumption's error). The S1T scenario shares in [scores.md](scores.md) show each row's rank-1 and top-3 frequencies under that noise.


**Listed frontier families: indicative value, not ranked and not comparable (O41).** Quality is the mean over the leaves the configuration has, renormalised, with no imputation, so these values cannot be compared with the ranking above.

| Configuration | Missing | Quality (remaining leaves) | Quality coverage | Plan value (indicative) | API value (indicative) | API cost (USD per basket run) | Plan cost (USD per basket run) |
|---|---|---:|---:|---:|---:|---:|---:|
| GPT-5.6 Luna | FrontierCode 2.0, AA-Omniscience v1.1, HLE-Diamond, Terminal-Bench-Science 0.1, CritPt v2 (hard subset) | 13.2 | 60% | — | — | — | — |
| Gemini 4 Carbon | Bug Hunt Bench | 61.2 | 85% | 45.9 | 48.5 | $5,716.87 | $5,716.87 |
| MiMo-V2.6-Flash | Bug Hunt Bench | 36.3 | 85% | 42.0 | 42.9 | $82.84 | $72.16 |
| MiniMax-M3.1-Flash | Bug Hunt Bench | 37.8 | 85% | 35.2 | 39.8 | $323.30 | $323.30 |

### Common-leaf ranking (diagnostic): Plan routes and calibration

#### Measured-evidence calibration (diagnostic)

References: each workload's measured-only rows with complete cost evidence are the references: c_L = cheapest / 2, c_H = dearest x 2 (diagnostic only; the official anchors are unchanged). Status: evaluated.

- Workload `835a9baf594a1251`: measured anchors $10.35 to $658.32 from GPT-6 Astra (max), GPT-6 Astra (high), GPT-6 Astra (xhigh), GPT-6.1 Sol (max), GPT-6.1 Sol (high), GPT-6.1 Sol (low), GPT-6.1 Sol (medium), GPT-6.1 Sol (xhigh); anchor ratio 63.6 against the official 113.7. Official Plan anchors are set by GPT-6.1 Sol (low) on ChatGPT Pro 500 (same-model measurement from another effort) at the low end and GPT-6 Astra (max) on ChatGPT Plus (controlled measurement) at the high end.

| Configuration | Value on official Plan anchors | Value on measured anchors | Rank change |
|---|---:|---:|---:|
| Claude Opus 5.5 (high) ‡ | 57.35 | 56.31 | 0 |
| Claude Opus 5.5 (max) | 56.84 | 55.03 | 0 |
| Claude Opus 5.5 (medium) ‡ | 57.01 | 56.18 | 0 |
| Claude Opus 5.5 (xhigh) ‡ | 58.26 | 56.83 | 0 |
| GPT-6 Astra (high) ‡ | 53.23 | 51.06 | 1 |
| GPT-6 Astra (max) | 54.83 | 52.27 | 0 |
| GPT-6 Astra (xhigh) ‡ | 56.13 | 53.87 | 0 |
| GPT-6.1 Sol (high) ‡ | 59.31 | 58.18 | 0 |
| GPT-6.1 Sol (low) ‡ | 51.68 | 51.17 | -1 |
| GPT-6.1 Sol (max) | 61.82 | 60.23 | 0 |
| GPT-6.1 Sol (medium) ‡ | 57.47 | 56.61 | 0 |
| GPT-6.1 Sol (xhigh) ‡ | 61.93 | 60.66 | 0 |

Pairwise reversals: GPT-6 Astra (high) and GPT-6.1 Sol (low). Largest value change: 2.56 points.

‡ measured on the same model at another effort (an O88 route; measured evidence under O90).

### Common-leaf ranking (diagnostic): interval outputs

**API basis, main workload: frontier.** Not evaluable: Claude Opus 5.5 (max), Claude Opus 5.5 (high), Claude Opus 5.5 (medium), Claude Opus 5.5 (xhigh). Competing without a label of its own (E183): Claude Haiku 5.5 (xhigh): AA's cost omits a pricing term (O94); competes over its published cost up to the stated factor; Claude Haiku 5.5 (high): AA's cost omits a pricing term (O94); competes over its published cost up to the stated factor; Claude Haiku 5.5 (low): AA's cost omits a pricing term (O94); competes over its published cost up to the stated factor; Claude Haiku 5.5 (max): AA's cost omits a pricing term (O94); competes over its published cost up to the stated factor; Claude Haiku 5.5 (medium): AA's cost omits a pricing term (O94); competes over its published cost up to the stated factor.

| Configuration | Possible frontier | Definite frontier | Definite counterexample | Possible frontier blocked by |
|---|---|---|---|---|
| GPT-6.1 Sol (max) | certified | certified | — | — |
| GPT-6.1 Terra (max) | disproved | disproved | GPT-6.1 Sol (xhigh) | GPT-6.1 Sol (xhigh) |
| Claude Sonnet 5.5 (max) | disproved | disproved | GPT-6.1 Sol (max) | GPT-6.1 Sol (max), GPT-6 Astra (max), GPT-6 Astra (xhigh) |
| GPT-6.1 Sol (high) | certified | certified | — | — |
| GPT-6 Astra (max) | disproved | disproved | GPT-6.1 Sol (max) | GPT-6.1 Sol (max) |
| DeepSeek V4.1 Flash 1017 (max) | disproved | disproved | GPT-6.1 Sol (medium) | GPT-6.1 Sol (medium) |
| GPT-6.1 Sol (medium) | certified | certified | — | — |
| Gemini 4 Argon (high) | disproved | disproved | GPT-6.1 Sol (max) | GPT-6.1 Sol (max), GPT-6.1 Terra (max), GPT-6.1 Sol (high), GPT-6 Astra (max), Kimi K3.1 Pro (max), GPT-6 Astra (high), Claude Sonnet 5.5 (xhigh), GPT-6 Astra (xhigh), GPT-6.1 Sol (xhigh) |
| Kimi K3.1 Pro (max) | disproved | disproved | GPT-6.1 Sol (max) | GPT-6.1 Sol (max), GPT-6.1 Terra (max), GPT-6.1 Sol (xhigh) |
| GPT-6 Astra (high) | disproved | disproved | GPT-6.1 Sol (max) | GPT-6.1 Sol (max), GPT-6.1 Terra (max), GPT-6.1 Sol (xhigh) |
| GPT-6.1 Sol (low) | certified | certified | — | — |
| GPT-6.1 Terra (xhigh) | certified | certified | — | — |
| GPT-6.1 Terra (high) | certified | certified | — | — |
| GPT-6 Luna (max) | certified | certified | — | — |
| MiMo-V2.6-Pro | certified | certified | — | — |
| GPT-6.1 Terra (medium) | certified | certified | — | — |
| GPT-6 Luna (xhigh) | certified | certified | — | — |
| GPT-6 Luna (high) | certified | certified | — | — |
| GPT-6 Luna (medium) | certified | certified | — | — |
| Claude Sonnet 5.5 (xhigh) | disproved | disproved | GPT-6.1 Sol (max) | GPT-6.1 Sol (max), GPT-6.1 Terra (max), GPT-6.1 Sol (high), GPT-6.1 Sol (xhigh) |
| GPT-6 Astra (xhigh) | disproved | disproved | GPT-6.1 Sol (max) | GPT-6.1 Sol (max) |
| GPT-6 Luna (low) | certified | certified | — | — |
| GPT-6.1 Sol (xhigh) | certified | certified | — | — |
| GPT-6.1 Terra (low) | certified | certified | — | — | Safety-refusal flags (O63; costs and scores unchanged) on these labelled rows: GPT-6.1 Sol (max) (15 blocked and 0 fallback attempts of 870); GPT-6.1 Terra (low) (1 blocked and 0 fallback attempts of 870).

**API basis, main workload: cheapest at or above quality 50.0** (lower-median displayed quality of the non-provisional cohort configurations at freeze (E192; headline bar)). Status certified; confirmed cheapest: GPT-6.1 Sol (medium).

Configurations that can be confirmed to qualify: 12 (confirmation needs the full-composite lower bound, with missing leaves at 0, to clear the bar; O25). Cheaper same-family configurations on AA's chart that were not evaluated (not ranked in this ranking: lacking its full benchmark set, or not plotted on or near the frontier; E201c, O51): none.

Bar comparison: compares 13 configurations that can qualify. The bar is a displayed-quality level; qualification tests each row's full-composite bounds, so a row above the bar on displayed quality can still fail to qualify confirmed when leaves are missing (E198).

| Configuration | Displayed quality − bar | Confirmed qualifies | Possibly qualifies | Possibly cheapest |
|---|---:|---|---|---|
| GPT-6.1 Sol (max) | 14.2 | certified | certified | disproved |
| GPT-6.1 Terra (max) | 9.3 | certified | certified | disproved |
| Claude Sonnet 5.5 (max) | 12.0 | certified | certified | disproved |
| GPT-6.1 Sol (high) | 6.4 | certified | certified | disproved |
| GPT-6 Astra (max) | 14.1 | certified | certified | disproved |
| DeepSeek V4.1 Flash 1017 (max) | 0.0 | disproved | certified | disproved |
| GPT-6.1 Sol (medium) | 1.6 | certified | certified | certified |
| Gemini 4 Argon (high) | 2.4 | certified | certified | disproved |
| Kimi K3.1 Pro (max) | 6.5 | certified | certified | disproved |
| GPT-6 Astra (high) | 8.3 | certified | certified | disproved |
| GPT-6.1 Sol (low) | -9.5 | disproved | disproved | disproved |
| GPT-6.1 Terra (xhigh) | -3.8 | disproved | disproved | disproved |
| GPT-6.1 Terra (high) | -7.0 | disproved | disproved | disproved |
| GPT-6 Luna (max) | -15.0 | disproved | disproved | disproved |
| MiMo-V2.6-Pro | -11.9 | disproved | disproved | disproved |
| GPT-6.1 Terra (medium) | -10.6 | disproved | disproved | disproved |
| GPT-6 Luna (xhigh) | -21.4 | disproved | disproved | disproved |
| GPT-6 Luna (high) | -23.6 | disproved | disproved | disproved |
| GPT-6 Luna (medium) | -28.9 | disproved | disproved | disproved |
| Claude Sonnet 5.5 (xhigh) | 3.1 | certified | certified | disproved |
| GPT-6 Astra (xhigh) | 13.0 | certified | certified | disproved |
| GPT-6 Luna (low) | -35.5 | disproved | disproved | disproved |
| GPT-6.1 Sol (xhigh) | 11.3 | certified | certified | disproved |
| GPT-6.1 Terra (low) | -18.5 | disproved | disproved | disproved |

**API basis, main workload: cheapest at or above quality 35.0** (lower-quartile displayed quality of the non-provisional cohort configurations at freeze (O34)). Status certified; confirmed cheapest: none.

Configurations that can be confirmed to qualify: 18 (confirmation needs the full-composite lower bound, with missing leaves at 0, to clear the bar; O25). Cheaper same-family configurations on AA's chart that were not evaluated (not ranked in this ranking: lacking its full benchmark set, or not plotted on or near the frontier; E201c, O51): GPT-6 Luna (max): GPT-6 Luna (non-reasoning).

Bar comparison: compares 19 configurations that can qualify and 2 blocker(s) that can qualify but earn no label (E315). The bar is a displayed-quality level; qualification tests each row's full-composite bounds, so a row above the bar on displayed quality can still fail to qualify confirmed when leaves are missing (E198).

| Configuration | Displayed quality − bar | Confirmed qualifies | Possibly qualifies | Possibly cheapest |
|---|---:|---|---|---|
| GPT-6.1 Sol (max) | 29.2 | certified | certified | disproved |
| GPT-6.1 Terra (max) | 24.4 | certified | certified | disproved |
| Claude Sonnet 5.5 (max) | 27.1 | certified | certified | disproved |
| GPT-6.1 Sol (high) | 21.5 | certified | certified | disproved |
| GPT-6 Astra (max) | 29.2 | certified | certified | disproved |
| DeepSeek V4.1 Flash 1017 (max) | 15.0 | certified | certified | disproved |
| GPT-6.1 Sol (medium) | 16.6 | certified | certified | disproved |
| Gemini 4 Argon (high) | 17.5 | certified | certified | disproved |
| Kimi K3.1 Pro (max) | 21.5 | certified | certified | disproved |
| GPT-6 Astra (high) | 23.4 | certified | certified | disproved |
| GPT-6.1 Sol (low) | 5.5 | certified | certified | disproved |
| GPT-6.1 Terra (xhigh) | 11.2 | certified | certified | disproved |
| GPT-6.1 Terra (high) | 8.0 | certified | certified | disproved |
| GPT-6 Luna (max) | 0.0 | disproved | certified | certified |
| MiMo-V2.6-Pro | 3.1 | certified | certified | certified |
| GPT-6.1 Terra (medium) | 4.5 | certified | certified | disproved |
| GPT-6 Luna (xhigh) | -6.4 | disproved | disproved | disproved |
| GPT-6 Luna (high) | -8.5 | disproved | disproved | disproved |
| GPT-6 Luna (medium) | -13.8 | disproved | disproved | disproved |
| Claude Sonnet 5.5 (xhigh) | 18.1 | certified | certified | disproved |
| GPT-6 Astra (xhigh) | 28.1 | certified | certified | disproved |
| GPT-6 Luna (low) | -20.4 | disproved | disproved | disproved |
| GPT-6.1 Sol (xhigh) | 26.3 | certified | certified | disproved |
| GPT-6.1 Terra (low) | -3.5 | disproved | disproved | disproved |

**API basis, main workload: cheapest at or above quality 58.0** (upper-quartile displayed quality of the non-provisional cohort configurations at freeze (O34)). Status certified; confirmed cheapest: GPT-6.1 Sol (xhigh).

Configurations that can be confirmed to qualify: 7 (confirmation needs the full-composite lower bound, with missing leaves at 0, to clear the bar; O25). Cheaper same-family configurations on AA's chart that were not evaluated (not ranked in this ranking: lacking its full benchmark set, or not plotted on or near the frontier; E201c, O51): none.

Bar comparison: compares 7 configurations that can qualify. The bar is a displayed-quality level; qualification tests each row's full-composite bounds, so a row above the bar on displayed quality can still fail to qualify confirmed when leaves are missing (E198).

| Configuration | Displayed quality − bar | Confirmed qualifies | Possibly qualifies | Possibly cheapest |
|---|---:|---|---|---|
| GPT-6.1 Sol (max) | 6.2 | certified | certified | disproved |
| GPT-6.1 Terra (max) | 1.4 | certified | certified | disproved |
| Claude Sonnet 5.5 (max) | 4.1 | certified | certified | disproved |
| GPT-6.1 Sol (high) | -1.5 | disproved | disproved | disproved |
| GPT-6 Astra (max) | 6.2 | certified | certified | disproved |
| DeepSeek V4.1 Flash 1017 (max) | -8.0 | disproved | disproved | disproved |
| GPT-6.1 Sol (medium) | -6.4 | disproved | disproved | disproved |
| Gemini 4 Argon (high) | -5.5 | disproved | disproved | disproved |
| Kimi K3.1 Pro (max) | -1.5 | disproved | disproved | disproved |
| GPT-6 Astra (high) | 0.4 | certified | certified | disproved |
| GPT-6.1 Sol (low) | -17.5 | disproved | disproved | disproved |
| GPT-6.1 Terra (xhigh) | -11.7 | disproved | disproved | disproved |
| GPT-6.1 Terra (high) | -15.0 | disproved | disproved | disproved |
| GPT-6 Luna (max) | -23.0 | disproved | disproved | disproved |
| MiMo-V2.6-Pro | -19.9 | disproved | disproved | disproved |
| GPT-6.1 Terra (medium) | -18.5 | disproved | disproved | disproved |
| GPT-6 Luna (xhigh) | -29.4 | disproved | disproved | disproved |
| GPT-6 Luna (high) | -31.5 | disproved | disproved | disproved |
| GPT-6 Luna (medium) | -36.8 | disproved | disproved | disproved |
| Claude Sonnet 5.5 (xhigh) | -4.9 | disproved | disproved | disproved |
| GPT-6 Astra (xhigh) | 5.1 | certified | certified | disproved |
| GPT-6 Luna (low) | -43.4 | disproved | disproved | disproved |
| GPT-6.1 Sol (xhigh) | 3.3 | certified | certified | certified |
| GPT-6.1 Terra (low) | -26.5 | disproved | disproved | disproved |

**Plan basis, main workload:** not evaluated (no row has FullCost and an identified M_W (E61/E67)).

### Common-leaf ranking (diagnostic): scenario shares

The scenario panel is the 33 rows scored on the main workload (E96, E266).

Frequencies over 10,000 scenarios per run (seed 20261101); streams are defined in [methodology.md](methodology.md#uncertainty-outputs). S1T adds benchmark sampling noise under an independent-task approximation (O39); the other streams exclude it, and every stream excludes correlated-task, harness and attempt effects (E155).

### API basis: rank 1

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M | S1T | S1T recentred |
|---|---:|---:|---:|---:|---:|---:|---:|
| Claude Haiku 5.5 (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Haiku 5.5 (low) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Haiku 5.5 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Haiku 5.5 (medium) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Haiku 5.5 (xhigh) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (medium) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (xhigh) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Sonnet 5.5 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Sonnet 5.5 (xhigh) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| DeepSeek V4.1 Flash 1017 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.2% | 0.2% |
| GPT-6 Astra (xhigh) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.5% | 0.6% |
| GPT-6 Luna (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Luna (low) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Luna (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Luna (medium) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Luna (xhigh) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 1.2% | 1.1% |
| GPT-6.1 Sol (low) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (max) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 59.6% | 59.6% |
| GPT-6.1 Sol (medium) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (xhigh) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 32.2% | 32.4% |
| GPT-6.1 Terra (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Terra (low) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Terra (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 6.3% | 6.0% |
| GPT-6.1 Terra (medium) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Terra (xhigh) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Gemini 4 Argon (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Kimi K3.1 Pro (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| MiMo-V2.6-Pro | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |

### API basis: rank 3 or better

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M | S1T | S1T recentred |
|---|---:|---:|---:|---:|---:|---:|---:|
| Claude Haiku 5.5 (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Haiku 5.5 (low) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Haiku 5.5 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Haiku 5.5 (medium) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Haiku 5.5 (xhigh) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (medium) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (xhigh) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Sonnet 5.5 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.1% | 0.1% |
| Claude Sonnet 5.5 (xhigh) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| DeepSeek V4.1 Flash 1017 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.1% | 0.1% |
| GPT-6 Astra (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.2% | 0.1% |
| GPT-6 Astra (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 8.9% | 8.9% |
| GPT-6 Astra (xhigh) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 13.6% | 13.7% |
| GPT-6 Luna (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Luna (low) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Luna (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Luna (medium) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Luna (xhigh) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (high) | 0.0% | 0.0% | 0.1% | 0.0% | 0.0% | 25.4% | 25.5% |
| GPT-6.1 Sol (low) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (max) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 96.9% | 96.5% |
| GPT-6.1 Sol (medium) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 1.1% | 1.1% |
| GPT-6.1 Sol (xhigh) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 92.0% | 92.3% |
| GPT-6.1 Terra (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Terra (low) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Terra (max) | 100.0% | 100.0% | 99.9% | 100.0% | 100.0% | 61.7% | 61.7% |
| GPT-6.1 Terra (medium) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Terra (xhigh) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Gemini 4 Argon (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Kimi K3.1 Pro (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| MiMo-V2.6-Pro | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |

### API basis: on the frontier

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M | S1T | S1T recentred |
|---|---:|---:|---:|---:|---:|---:|---:|
| Claude Haiku 5.5 (high) | 100.0% | 100.0% | 53.2% | 100.0% | 100.0% | 50.0% | 50.6% |
| Claude Haiku 5.5 (low) | 100.0% | 100.0% | 55.7% | 100.0% | 100.0% | 52.2% | 52.7% |
| Claude Haiku 5.5 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 10.5% | 10.5% |
| Claude Haiku 5.5 (medium) | 0.0% | 0.0% | 37.7% | 0.0% | 0.0% | 44.1% | 45.2% |
| Claude Haiku 5.5 (xhigh) | 100.0% | 100.0% | 91.9% | 100.0% | 100.0% | 74.9% | 76.0% |
| Claude Opus 5.5 (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (max) | 0.0% | 0.0% | 0.4% | 0.0% | 0.0% | 0.4% | 0.3% |
| Claude Opus 5.5 (medium) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (xhigh) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.2% | 0.2% |
| Claude Sonnet 5.5 (max) | 0.0% | 0.0% | 1.5% | 0.0% | 0.0% | 6.8% | 6.6% |
| Claude Sonnet 5.5 (xhigh) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| DeepSeek V4.1 Flash 1017 (max) | 0.0% | 0.0% | 16.9% | 0.0% | 0.0% | 29.0% | 29.3% |
| GPT-6 Astra (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 1.2% | 1.2% |
| GPT-6 Astra (max) | 0.0% | 0.0% | 47.5% | 0.0% | 0.0% | 37.2% | 37.6% |
| GPT-6 Astra (xhigh) | 0.0% | 0.0% | 1.5% | 0.0% | 0.0% | 31.8% | 30.3% |
| GPT-6 Luna (high) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 99.8% | 99.9% |
| GPT-6 Luna (low) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% |
| GPT-6 Luna (max) | 100.0% | 100.0% | 99.7% | 100.0% | 100.0% | 90.6% | 90.2% |
| GPT-6 Luna (medium) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% |
| GPT-6 Luna (xhigh) | 100.0% | 100.0% | 99.8% | 100.0% | 100.0% | 81.7% | 81.2% |
| GPT-6.1 Sol (high) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 94.8% | 95.2% |
| GPT-6.1 Sol (low) | 100.0% | 100.0% | 73.6% | 100.0% | 100.0% | 59.6% | 59.6% |
| GPT-6.1 Sol (max) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 80.5% | 80.2% |
| GPT-6.1 Sol (medium) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 97.7% | 97.6% |
| GPT-6.1 Sol (xhigh) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 94.5% | 94.9% |
| GPT-6.1 Terra (high) | 100.0% | 100.0% | 92.8% | 100.0% | 100.0% | 79.3% | 79.7% |
| GPT-6.1 Terra (low) | 100.0% | 100.0% | 99.7% | 100.0% | 100.0% | 92.2% | 92.3% |
| GPT-6.1 Terra (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 25.3% | 25.0% |
| GPT-6.1 Terra (medium) | 100.0% | 100.0% | 91.3% | 100.0% | 100.0% | 65.8% | 66.3% |
| GPT-6.1 Terra (xhigh) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 88.5% | 88.8% |
| Gemini 4 Argon (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Kimi K3.1 Pro (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.1% | 0.1% |
| MiMo-V2.6-Pro | 100.0% | 100.0% | 94.9% | 100.0% | 100.0% | 69.7% | 70.1% |

### API basis: value-score dispersion (SD; covariance term)

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M | S1T | S1T recentred |
|---|---:|---:|---:|---:|---:|---:|---:|
| Claude Haiku 5.5 (high) | 0.00 (+0.00) | 0.00 (+0.00) | 0.98 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.14 (+0.00) | 1.15 (+0.00) |
| Claude Haiku 5.5 (low) | 0.00 (+0.00) | 0.00 (+0.00) | 1.13 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 0.89 (+0.00) | 0.89 (+0.00) |
| Claude Haiku 5.5 (max) | 0.00 (+0.00) | 0.00 (+0.00) | 0.80 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.29 (+0.00) | 1.32 (+0.00) |
| Claude Haiku 5.5 (medium) | 0.00 (+0.00) | 0.00 (+0.00) | 1.08 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.03 (+0.00) | 1.03 (+0.00) |
| Claude Haiku 5.5 (xhigh) | 0.00 (+0.00) | 0.00 (+0.00) | 0.86 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.25 (+0.00) | 1.27 (+0.00) |
| Claude Opus 5.5 (high) | 0.00 (+0.00) | 0.00 (+0.00) | 1.01 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.38 (+0.00) | 1.36 (+0.00) |
| Claude Opus 5.5 (max) | 0.00 (+0.00) | 0.00 (+0.00) | 0.82 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.38 (+0.00) | 1.40 (+0.00) |
| Claude Opus 5.5 (medium) | 0.00 (+0.00) | 0.00 (+0.00) | 0.99 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.39 (+0.00) | 1.38 (+0.00) |
| Claude Opus 5.5 (xhigh) | 0.00 (+0.00) | 0.00 (+0.00) | 0.84 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.40 (+0.00) | 1.41 (+0.00) |
| Claude Sonnet 5.5 (max) | 0.00 (+0.00) | 0.00 (+0.00) | 1.02 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.46 (+0.00) | 1.48 (+0.00) |
| Claude Sonnet 5.5 (xhigh) | 0.00 (+0.00) | 0.00 (+0.00) | 0.88 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.40 (+0.00) | 1.39 (+0.00) |
| DeepSeek V4.1 Flash 1017 (max) | 0.00 (+0.00) | 0.00 (+0.00) | 1.67 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.48 (+0.00) | 1.49 (+0.00) |
| GPT-6 Astra (high) | 0.00 (+0.00) | 0.00 (+0.00) | 1.04 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.52 (+0.00) | 1.52 (+0.00) |
| GPT-6 Astra (max) | 0.00 (+0.00) | 0.00 (+0.00) | 1.50 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.60 (+0.00) | 1.58 (+0.00) |
| GPT-6 Astra (xhigh) | 0.00 (+0.00) | 0.00 (+0.00) | 1.42 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.58 (+0.00) | 1.58 (+0.00) |
| GPT-6 Luna (high) | 0.00 (+0.00) | 0.00 (+0.00) | 1.27 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 0.92 (+0.00) | 0.91 (+0.00) |
| GPT-6 Luna (low) | 0.00 (+0.00) | 0.00 (+0.00) | 1.18 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 0.55 (+0.00) | 0.54 (+0.00) |
| GPT-6 Luna (max) | 0.00 (+0.00) | 0.00 (+0.00) | 1.18 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.18 (+0.00) | 1.19 (+0.00) |
| GPT-6 Luna (medium) | 0.00 (+0.00) | 0.00 (+0.00) | 1.36 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 0.71 (+0.00) | 0.71 (+0.00) |
| GPT-6 Luna (xhigh) | 0.00 (+0.00) | 0.00 (+0.00) | 1.20 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.01 (+0.00) | 1.02 (+0.00) |
| GPT-6.1 Sol (high) | 0.00 (+0.00) | 0.00 (+0.00) | 1.15 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.52 (+0.00) | 1.53 (+0.00) |
| GPT-6.1 Sol (low) | 0.00 (+0.00) | 0.00 (+0.00) | 1.26 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.30 (+0.00) | 1.32 (+0.00) |
| GPT-6.1 Sol (max) | 0.00 (+0.00) | 0.00 (+0.00) | 1.79 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.64 (+0.00) | 1.64 (+0.00) |
| GPT-6.1 Sol (medium) | 0.00 (+0.00) | 0.00 (+0.00) | 1.00 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.45 (+0.00) | 1.45 (+0.00) |
| GPT-6.1 Sol (xhigh) | 0.00 (+0.00) | 0.00 (+0.00) | 1.59 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.59 (+0.00) | 1.60 (+0.00) |
| GPT-6.1 Terra (high) | 0.00 (+0.00) | 0.00 (+0.00) | 1.16 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.31 (+0.00) | 1.31 (+0.00) |
| GPT-6.1 Terra (low) | 0.00 (+0.00) | 0.00 (+0.00) | 1.38 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.06 (+0.00) | 1.06 (+0.00) |
| GPT-6.1 Terra (max) | 0.00 (+0.00) | 0.00 (+0.00) | 1.23 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.57 (+0.00) | 1.56 (+0.00) |
| GPT-6.1 Terra (medium) | 0.00 (+0.00) | 0.00 (+0.00) | 1.19 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.26 (+0.00) | 1.26 (+0.00) |
| GPT-6.1 Terra (xhigh) | 0.00 (+0.00) | 0.00 (+0.00) | 0.96 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.37 (+0.00) | 1.37 (+0.00) |
| Gemini 4 Argon (high) | 0.00 (+0.00) | 0.00 (+0.00) | 1.36 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.33 (+0.00) | 1.33 (+0.00) |
| Kimi K3.1 Pro (max) | 0.00 (+0.00) | 0.00 (+0.00) | 1.48 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.40 (+0.00) | 1.41 (+0.00) |
| MiMo-V2.6-Pro | 0.00 (+0.00) | 0.00 (+0.00) | 1.16 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.23 (+0.00) | 1.24 (+0.00) |

Plan streams S1, S2, S1 endpoint-heavy, S1M, S1T and S1T recentred run with owner assumptions off (owner-named transfers and O46 provider quota ceilings; E167): Claude Haiku 5.5 (high) on Claude Max 20x, Claude Haiku 5.5 (high) on Claude Max 5x, Claude Haiku 5.5 (high) on Claude Pro, Claude Haiku 5.5 (low) on Claude Max 20x, Claude Haiku 5.5 (low) on Claude Max 5x, Claude Haiku 5.5 (low) on Claude Pro, Claude Haiku 5.5 (max) on Claude Max 20x, Claude Haiku 5.5 (max) on Claude Max 5x, Claude Haiku 5.5 (max) on Claude Pro, Claude Haiku 5.5 (medium) on Claude Max 20x, Claude Haiku 5.5 (medium) on Claude Max 5x, Claude Haiku 5.5 (medium) on Claude Pro, Claude Haiku 5.5 (xhigh) on Claude Max 20x, Claude Haiku 5.5 (xhigh) on Claude Max 5x, Claude Haiku 5.5 (xhigh) on Claude Pro, Claude Sonnet 5.5 (max) on Claude Max 20x, Claude Sonnet 5.5 (max) on Claude Max 5x, Claude Sonnet 5.5 (max) on Claude Pro, Claude Sonnet 5.5 (xhigh) on Claude Max 20x, Claude Sonnet 5.5 (xhigh) on Claude Max 5x, Claude Sonnet 5.5 (xhigh) on Claude Pro, GPT-6 Luna (high) on ChatGPT Plus, GPT-6 Luna (high) on ChatGPT Pro 100, GPT-6 Luna (high) on ChatGPT Pro 200, GPT-6 Luna (high) on ChatGPT Pro 500, GPT-6 Luna (low) on ChatGPT Plus, GPT-6 Luna (low) on ChatGPT Pro 100, GPT-6 Luna (low) on ChatGPT Pro 200, GPT-6 Luna (low) on ChatGPT Pro 500, GPT-6 Luna (max) on ChatGPT Plus, GPT-6 Luna (max) on ChatGPT Pro 100, GPT-6 Luna (max) on ChatGPT Pro 200, GPT-6 Luna (max) on ChatGPT Pro 500, GPT-6 Luna (medium) on ChatGPT Plus, GPT-6 Luna (medium) on ChatGPT Pro 100, GPT-6 Luna (medium) on ChatGPT Pro 200, GPT-6 Luna (medium) on ChatGPT Pro 500, GPT-6 Luna (xhigh) on ChatGPT Plus, GPT-6 Luna (xhigh) on ChatGPT Pro 100, GPT-6 Luna (xhigh) on ChatGPT Pro 200, GPT-6 Luna (xhigh) on ChatGPT Pro 500, GPT-6.1 Terra (high) on ChatGPT Plus, GPT-6.1 Terra (high) on ChatGPT Pro 100, GPT-6.1 Terra (high) on ChatGPT Pro 200, GPT-6.1 Terra (high) on ChatGPT Pro 500, GPT-6.1 Terra (low) on ChatGPT Plus, GPT-6.1 Terra (low) on ChatGPT Pro 100, GPT-6.1 Terra (low) on ChatGPT Pro 200, GPT-6.1 Terra (low) on ChatGPT Pro 500, GPT-6.1 Terra (max) on ChatGPT Plus, GPT-6.1 Terra (max) on ChatGPT Pro 100, GPT-6.1 Terra (max) on ChatGPT Pro 200, GPT-6.1 Terra (max) on ChatGPT Pro 500, GPT-6.1 Terra (medium) on ChatGPT Plus, GPT-6.1 Terra (medium) on ChatGPT Pro 100, GPT-6.1 Terra (medium) on ChatGPT Pro 200, GPT-6.1 Terra (medium) on ChatGPT Pro 500, GPT-6.1 Terra (xhigh) on ChatGPT Plus, GPT-6.1 Terra (xhigh) on ChatGPT Pro 100, GPT-6.1 Terra (xhigh) on ChatGPT Pro 200, GPT-6.1 Terra (xhigh) on ChatGPT Pro 500, MiMo-V2.6-Pro on MiMo Token Plan Lite, MiMo-V2.6-Pro on MiMo Token Plan Max, MiMo-V2.6-Pro on MiMo Token Plan Pro, MiMo-V2.6-Pro on MiMo Token Plan Standard depend on an owner assumption and are unevaluable there (—), never reselected or replaced by API cost.

### Plan basis: rank 1

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M | S1T | S1T recentred |
|---|---:|---:|---:|---:|---:|---:|---:|
| Claude Haiku 5.5 (high) on Claude Max 20x | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (high) on Claude Max 5x | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (high) on Claude Pro | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (low) on Claude Max 20x | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (low) on Claude Max 5x | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (low) on Claude Pro | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (max) on Claude Max 20x | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (max) on Claude Max 5x | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (max) on Claude Pro | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (medium) on Claude Max 20x | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (medium) on Claude Max 5x | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (medium) on Claude Pro | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (xhigh) on Claude Max 20x | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (xhigh) on Claude Max 5x | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (xhigh) on Claude Pro | 0.0% | — | — | — | — | — | — |
| Claude Opus 5.5 (high) on Claude Max 20x | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (high) on Claude Max 5x | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (high) on Claude Pro | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.1% | 0.2% |
| Claude Opus 5.5 (max) on Claude Max 20x | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (max) on Claude Max 5x | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (max) on Claude Pro | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.1% | 0.0% |
| Claude Opus 5.5 (medium) on Claude Max 20x | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (medium) on Claude Max 5x | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (medium) on Claude Pro | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.1% | 0.1% |
| Claude Opus 5.5 (xhigh) on Claude Max 20x | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (xhigh) on Claude Max 5x | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (xhigh) on Claude Pro | 0.0% | 0.0% | 0.4% | 0.0% | 0.0% | 0.7% | 0.7% |
| Claude Sonnet 5.5 (max) on Claude Max 20x | 0.0% | — | — | — | — | — | — |
| Claude Sonnet 5.5 (max) on Claude Max 5x | 0.0% | — | — | — | — | — | — |
| Claude Sonnet 5.5 (max) on Claude Pro | 0.0% | — | — | — | — | — | — |
| Claude Sonnet 5.5 (xhigh) on Claude Max 20x | 0.0% | — | — | — | — | — | — |
| Claude Sonnet 5.5 (xhigh) on Claude Max 5x | 0.0% | — | — | — | — | — | — |
| Claude Sonnet 5.5 (xhigh) on Claude Pro | 0.0% | — | — | — | — | — | — |
| DeepSeek V4.1 Flash 1017 (max) on API-cost fallback | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
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
| GPT-6 Luna (low) on ChatGPT Plus | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (low) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (low) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (low) on ChatGPT Pro 500 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Plus | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 500 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (medium) on ChatGPT Plus | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (medium) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (medium) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (medium) on ChatGPT Pro 500 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (xhigh) on ChatGPT Plus | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (xhigh) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (xhigh) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (xhigh) on ChatGPT Pro 500 | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Sol (high) on ChatGPT Plus | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (high) on ChatGPT Pro 100 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (high) on ChatGPT Pro 200 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (high) on ChatGPT Pro 500 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 4.1% | 3.8% |
| GPT-6.1 Sol (low) on ChatGPT Plus | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (low) on ChatGPT Pro 100 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (low) on ChatGPT Pro 200 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (low) on ChatGPT Pro 500 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (max) on ChatGPT Plus | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (max) on ChatGPT Pro 100 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (max) on ChatGPT Pro 200 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (max) on ChatGPT Pro 500 | 0.0% | 0.0% | 33.0% | 0.0% | 0.0% | 44.9% | 45.4% |
| GPT-6.1 Sol (medium) on ChatGPT Plus | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (medium) on ChatGPT Pro 100 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (medium) on ChatGPT Pro 200 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (medium) on ChatGPT Pro 500 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.3% | 0.3% |
| GPT-6.1 Sol (xhigh) on ChatGPT Plus | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (xhigh) on ChatGPT Pro 100 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (xhigh) on ChatGPT Pro 200 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (xhigh) on ChatGPT Pro 500 | 100.0% | 100.0% | 66.6% | 100.0% | 100.0% | 49.7% | 49.4% |
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
| Gemini 4 Argon (high) on API-cost fallback | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Kimi K3.1 Pro (max) on API-cost fallback | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| MiMo-V2.6-Pro on MiMo Token Plan Lite | 0.0% | — | — | — | — | — | — |
| MiMo-V2.6-Pro on MiMo Token Plan Max | 0.0% | — | — | — | — | — | — |
| MiMo-V2.6-Pro on MiMo Token Plan Pro | 0.0% | — | — | — | — | — | — |
| MiMo-V2.6-Pro on MiMo Token Plan Standard | 0.0% | — | — | — | — | — | — |

### Plan basis: rank 3 or better

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M | S1T | S1T recentred |
|---|---:|---:|---:|---:|---:|---:|---:|
| Claude Haiku 5.5 (high) on Claude Max 20x | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (high) on Claude Max 5x | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (high) on Claude Pro | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (low) on Claude Max 20x | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (low) on Claude Max 5x | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (low) on Claude Pro | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (max) on Claude Max 20x | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (max) on Claude Max 5x | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (max) on Claude Pro | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (medium) on Claude Max 20x | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (medium) on Claude Max 5x | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (medium) on Claude Pro | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (xhigh) on Claude Max 20x | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (xhigh) on Claude Max 5x | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (xhigh) on Claude Pro | 0.0% | — | — | — | — | — | — |
| Claude Opus 5.5 (high) on Claude Max 20x | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.1% | 0.2% |
| Claude Opus 5.5 (high) on Claude Max 5x | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.1% | 0.1% |
| Claude Opus 5.5 (high) on Claude Pro | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.2% | 0.2% |
| Claude Opus 5.5 (max) on Claude Max 20x | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.1% | 0.1% |
| Claude Opus 5.5 (max) on Claude Max 5x | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.1% | 0.0% |
| Claude Opus 5.5 (max) on Claude Pro | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.1% | 0.1% |
| Claude Opus 5.5 (medium) on Claude Max 20x | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.1% | 0.1% |
| Claude Opus 5.5 (medium) on Claude Max 5x | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.1% | 0.1% |
| Claude Opus 5.5 (medium) on Claude Pro | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.1% | 0.1% |
| Claude Opus 5.5 (xhigh) on Claude Max 20x | 0.0% | 0.0% | 0.4% | 0.0% | 0.0% | 0.8% | 0.8% |
| Claude Opus 5.5 (xhigh) on Claude Max 5x | 0.0% | 0.0% | 0.2% | 0.0% | 0.0% | 0.6% | 0.6% |
| Claude Opus 5.5 (xhigh) on Claude Pro | 0.0% | 0.0% | 0.4% | 0.0% | 0.0% | 0.9% | 0.8% |
| Claude Sonnet 5.5 (max) on Claude Max 20x | 0.0% | — | — | — | — | — | — |
| Claude Sonnet 5.5 (max) on Claude Max 5x | 0.0% | — | — | — | — | — | — |
| Claude Sonnet 5.5 (max) on Claude Pro | 0.0% | — | — | — | — | — | — |
| Claude Sonnet 5.5 (xhigh) on Claude Max 20x | 0.0% | — | — | — | — | — | — |
| Claude Sonnet 5.5 (xhigh) on Claude Max 5x | 0.0% | — | — | — | — | — | — |
| Claude Sonnet 5.5 (xhigh) on Claude Pro | 0.0% | — | — | — | — | — | — |
| DeepSeek V4.1 Flash 1017 (max) on API-cost fallback | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
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
| GPT-6 Luna (low) on ChatGPT Plus | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (low) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (low) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (low) on ChatGPT Pro 500 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Plus | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 500 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (medium) on ChatGPT Plus | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (medium) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (medium) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (medium) on ChatGPT Pro 500 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (xhigh) on ChatGPT Plus | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (xhigh) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (xhigh) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (xhigh) on ChatGPT Pro 500 | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Sol (high) on ChatGPT Plus | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 4.0% | 3.8% |
| GPT-6.1 Sol (high) on ChatGPT Pro 100 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 4.0% | 3.8% |
| GPT-6.1 Sol (high) on ChatGPT Pro 200 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (high) on ChatGPT Pro 500 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 4.6% | 4.3% |
| GPT-6.1 Sol (low) on ChatGPT Plus | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (low) on ChatGPT Pro 100 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (low) on ChatGPT Pro 200 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (low) on ChatGPT Pro 500 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (max) on ChatGPT Plus | 0.0% | 0.0% | 33.0% | 0.0% | 0.0% | 44.8% | 45.3% |
| GPT-6.1 Sol (max) on ChatGPT Pro 100 | 0.0% | 0.0% | 33.0% | 0.0% | 0.0% | 44.8% | 45.3% |
| GPT-6.1 Sol (max) on ChatGPT Pro 200 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (max) on ChatGPT Pro 500 | 54.8% | 55.7% | 47.9% | 55.2% | 55.7% | 46.9% | 47.5% |
| GPT-6.1 Sol (medium) on ChatGPT Plus | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.3% | 0.3% |
| GPT-6.1 Sol (medium) on ChatGPT Pro 100 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.3% | 0.3% |
| GPT-6.1 Sol (medium) on ChatGPT Pro 200 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (medium) on ChatGPT Pro 500 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.4% | 0.3% |
| GPT-6.1 Sol (xhigh) on ChatGPT Plus | 100.0% | 100.0% | 66.6% | 100.0% | 100.0% | 49.7% | 49.3% |
| GPT-6.1 Sol (xhigh) on ChatGPT Pro 100 | 100.0% | 100.0% | 66.6% | 100.0% | 100.0% | 49.7% | 49.3% |
| GPT-6.1 Sol (xhigh) on ChatGPT Pro 200 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (xhigh) on ChatGPT Pro 500 | 100.0% | 100.0% | 79.8% | 100.0% | 100.0% | 51.4% | 51.3% |
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
| Gemini 4 Argon (high) on API-cost fallback | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Kimi K3.1 Pro (max) on API-cost fallback | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| MiMo-V2.6-Pro on MiMo Token Plan Lite | 0.0% | — | — | — | — | — | — |
| MiMo-V2.6-Pro on MiMo Token Plan Max | 0.0% | — | — | — | — | — | — |
| MiMo-V2.6-Pro on MiMo Token Plan Pro | 0.0% | — | — | — | — | — | — |
| MiMo-V2.6-Pro on MiMo Token Plan Standard | 0.0% | — | — | — | — | — | — |

### Plan basis: on the frontier

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M | S1T | S1T recentred |
|---|---:|---:|---:|---:|---:|---:|---:|
| Claude Haiku 5.5 (high) on Claude Max 20x | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (high) on Claude Max 5x | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (high) on Claude Pro | 100.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (low) on Claude Max 20x | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (low) on Claude Max 5x | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (low) on Claude Pro | 100.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (max) on Claude Max 20x | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (max) on Claude Max 5x | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (max) on Claude Pro | 100.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (medium) on Claude Max 20x | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (medium) on Claude Max 5x | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (medium) on Claude Pro | 100.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (xhigh) on Claude Max 20x | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (xhigh) on Claude Max 5x | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (xhigh) on Claude Pro | 100.0% | — | — | — | — | — | — |
| Claude Opus 5.5 (high) on Claude Max 20x | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (high) on Claude Max 5x | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (high) on Claude Pro | 100.0% | 100.0% | 93.8% | 100.0% | 100.0% | 62.1% | 63.3% |
| Claude Opus 5.5 (max) on Claude Max 20x | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (max) on Claude Max 5x | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (max) on Claude Pro | 0.0% | 0.0% | 1.8% | 0.0% | 0.0% | 3.4% | 3.5% |
| Claude Opus 5.5 (medium) on Claude Max 20x | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (medium) on Claude Max 5x | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (medium) on Claude Pro | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% |
| Claude Opus 5.5 (xhigh) on Claude Max 20x | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (xhigh) on Claude Max 5x | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (xhigh) on Claude Pro | 0.0% | 0.0% | 4.6% | 0.0% | 0.0% | 11.1% | 11.4% |
| Claude Sonnet 5.5 (max) on Claude Max 20x | 0.0% | — | — | — | — | — | — |
| Claude Sonnet 5.5 (max) on Claude Max 5x | 0.0% | — | — | — | — | — | — |
| Claude Sonnet 5.5 (max) on Claude Pro | 0.0% | — | — | — | — | — | — |
| Claude Sonnet 5.5 (xhigh) on Claude Max 20x | 0.0% | — | — | — | — | — | — |
| Claude Sonnet 5.5 (xhigh) on Claude Max 5x | 0.0% | — | — | — | — | — | — |
| Claude Sonnet 5.5 (xhigh) on Claude Pro | 100.0% | — | — | — | — | — | — |
| DeepSeek V4.1 Flash 1017 (max) on API-cost fallback | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (high) on ChatGPT Plus | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (high) on ChatGPT Pro 100 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (high) on ChatGPT Pro 200 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 1.3% | 1.0% |
| GPT-6 Astra (high) on ChatGPT Pro 500 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (max) on ChatGPT Plus | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (max) on ChatGPT Pro 100 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (max) on ChatGPT Pro 200 | 0.0% | 0.0% | 46.8% | 0.0% | 0.0% | 37.3% | 36.5% |
| GPT-6 Astra (max) on ChatGPT Pro 500 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (xhigh) on ChatGPT Plus | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (xhigh) on ChatGPT Pro 100 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (xhigh) on ChatGPT Pro 200 | 0.0% | 0.0% | 0.6% | 0.0% | 0.0% | 30.2% | 30.2% |
| GPT-6 Astra (xhigh) on ChatGPT Pro 500 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Luna (high) on ChatGPT Plus | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (high) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (high) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (high) on ChatGPT Pro 500 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (low) on ChatGPT Plus | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (low) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (low) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (low) on ChatGPT Pro 500 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Plus | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 500 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (medium) on ChatGPT Plus | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (medium) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (medium) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (medium) on ChatGPT Pro 500 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (xhigh) on ChatGPT Plus | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (xhigh) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (xhigh) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (xhigh) on ChatGPT Pro 500 | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Sol (high) on ChatGPT Plus | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (high) on ChatGPT Pro 100 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (high) on ChatGPT Pro 200 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (high) on ChatGPT Pro 500 | 100.0% | 100.0% | 99.8% | 100.0% | 100.0% | 86.1% | 85.8% |
| GPT-6.1 Sol (low) on ChatGPT Plus | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (low) on ChatGPT Pro 100 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (low) on ChatGPT Pro 200 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (low) on ChatGPT Pro 500 | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% |
| GPT-6.1 Sol (max) on ChatGPT Plus | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (max) on ChatGPT Pro 100 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (max) on ChatGPT Pro 200 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (max) on ChatGPT Pro 500 | 100.0% | 100.0% | 99.9% | 100.0% | 100.0% | 82.3% | 82.3% |
| GPT-6.1 Sol (medium) on ChatGPT Plus | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (medium) on ChatGPT Pro 100 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (medium) on ChatGPT Pro 200 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (medium) on ChatGPT Pro 500 | 100.0% | 100.0% | 92.8% | 100.0% | 100.0% | 64.3% | 65.2% |
| GPT-6.1 Sol (xhigh) on ChatGPT Plus | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (xhigh) on ChatGPT Pro 100 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (xhigh) on ChatGPT Pro 200 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (xhigh) on ChatGPT Pro 500 | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 94.8% | 94.9% |
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
| GPT-6.1 Terra (medium) on ChatGPT Pro 500 | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Terra (xhigh) on ChatGPT Plus | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Terra (xhigh) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Terra (xhigh) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Terra (xhigh) on ChatGPT Pro 500 | 100.0% | — | — | — | — | — | — |
| Gemini 4 Argon (high) on API-cost fallback | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Kimi K3.1 Pro (max) on API-cost fallback | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| MiMo-V2.6-Pro on MiMo Token Plan Lite | 0.0% | — | — | — | — | — | — |
| MiMo-V2.6-Pro on MiMo Token Plan Max | 0.0% | — | — | — | — | — | — |
| MiMo-V2.6-Pro on MiMo Token Plan Pro | 0.0% | — | — | — | — | — | — |
| MiMo-V2.6-Pro on MiMo Token Plan Standard | 0.0% | — | — | — | — | — | — |

### Plan basis: value-score dispersion (SD; covariance term)

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M | S1T | S1T recentred |
|---|---:|---:|---:|---:|---:|---:|---:|
| Claude Haiku 5.5 (high) on Claude Max 20x | 0.00 (+0.00) | — | — | — | — | — | — |
| Claude Haiku 5.5 (high) on Claude Max 5x | 0.00 (+0.00) | — | — | — | — | — | — |
| Claude Haiku 5.5 (high) on Claude Pro | 0.00 (+0.00) | — | — | — | — | — | — |
| Claude Haiku 5.5 (low) on Claude Max 20x | 0.00 (+0.00) | — | — | — | — | — | — |
| Claude Haiku 5.5 (low) on Claude Max 5x | 0.00 (+0.00) | — | — | — | — | — | — |
| Claude Haiku 5.5 (low) on Claude Pro | 0.00 (+0.00) | — | — | — | — | — | — |
| Claude Haiku 5.5 (max) on Claude Max 20x | 0.00 (+0.00) | — | — | — | — | — | — |
| Claude Haiku 5.5 (max) on Claude Max 5x | 0.00 (+0.00) | — | — | — | — | — | — |
| Claude Haiku 5.5 (max) on Claude Pro | 0.00 (+0.00) | — | — | — | — | — | — |
| Claude Haiku 5.5 (medium) on Claude Max 20x | 0.00 (+0.00) | — | — | — | — | — | — |
| Claude Haiku 5.5 (medium) on Claude Max 5x | 0.00 (+0.00) | — | — | — | — | — | — |
| Claude Haiku 5.5 (medium) on Claude Pro | 0.00 (+0.00) | — | — | — | — | — | — |
| Claude Haiku 5.5 (xhigh) on Claude Max 20x | 0.00 (+0.00) | — | — | — | — | — | — |
| Claude Haiku 5.5 (xhigh) on Claude Max 5x | 0.00 (+0.00) | — | — | — | — | — | — |
| Claude Haiku 5.5 (xhigh) on Claude Pro | 0.00 (+0.00) | — | — | — | — | — | — |
| Claude Opus 5.5 (high) on Claude Max 20x | 0.00 (+0.00) | 0.00 (+0.00) | 1.00 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.38 (+0.00) | 1.39 (+0.00) |
| Claude Opus 5.5 (high) on Claude Max 5x | 0.00 (+0.00) | 0.00 (+0.00) | 1.00 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.38 (+0.00) | 1.39 (+0.00) |
| Claude Opus 5.5 (high) on Claude Pro | 0.00 (+0.00) | 0.00 (+0.00) | 1.00 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.38 (+0.00) | 1.39 (+0.00) |
| Claude Opus 5.5 (max) on Claude Max 20x | 0.00 (+0.00) | 0.00 (+0.00) | 0.82 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.39 (+0.00) | 1.39 (+0.00) |
| Claude Opus 5.5 (max) on Claude Max 5x | 0.00 (+0.00) | 0.00 (+0.00) | 0.82 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.39 (+0.00) | 1.39 (+0.00) |
| Claude Opus 5.5 (max) on Claude Pro | 0.00 (+0.00) | 0.00 (+0.00) | 0.82 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.39 (+0.00) | 1.39 (+0.00) |
| Claude Opus 5.5 (medium) on Claude Max 20x | 0.00 (+0.00) | 0.00 (+0.00) | 0.99 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.38 (+0.00) | 1.38 (+0.00) |
| Claude Opus 5.5 (medium) on Claude Max 5x | 0.00 (+0.00) | 0.00 (+0.00) | 0.99 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.38 (+0.00) | 1.38 (+0.00) |
| Claude Opus 5.5 (medium) on Claude Pro | 0.00 (+0.00) | 0.00 (+0.00) | 0.99 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.38 (+0.00) | 1.38 (+0.00) |
| Claude Opus 5.5 (xhigh) on Claude Max 20x | 0.00 (+0.00) | 0.00 (+0.00) | 0.84 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.40 (+0.00) | 1.41 (+0.00) |
| Claude Opus 5.5 (xhigh) on Claude Max 5x | 0.00 (+0.00) | 0.00 (+0.00) | 0.84 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.40 (+0.00) | 1.41 (+0.00) |
| Claude Opus 5.5 (xhigh) on Claude Pro | 0.00 (+0.00) | 0.00 (+0.00) | 0.84 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.40 (+0.00) | 1.41 (+0.00) |
| Claude Sonnet 5.5 (max) on Claude Max 20x | 0.00 (+0.00) | — | — | — | — | — | — |
| Claude Sonnet 5.5 (max) on Claude Max 5x | 0.00 (+0.00) | — | — | — | — | — | — |
| Claude Sonnet 5.5 (max) on Claude Pro | 0.00 (+0.00) | — | — | — | — | — | — |
| Claude Sonnet 5.5 (xhigh) on Claude Max 20x | 0.00 (+0.00) | — | — | — | — | — | — |
| Claude Sonnet 5.5 (xhigh) on Claude Max 5x | 0.00 (+0.00) | — | — | — | — | — | — |
| Claude Sonnet 5.5 (xhigh) on Claude Pro | 0.00 (+0.00) | — | — | — | — | — | — |
| DeepSeek V4.1 Flash 1017 (max) on API-cost fallback | 0.00 (+0.00) | 0.00 (+0.00) | 1.68 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.49 (+0.00) | 1.48 (+0.00) |
| GPT-6 Astra (high) on ChatGPT Plus | 0.00 (+0.00) | 0.00 (+0.00) | 1.05 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.53 (+0.00) | 1.51 (+0.00) |
| GPT-6 Astra (high) on ChatGPT Pro 100 | 0.00 (+0.00) | 0.00 (+0.00) | 1.05 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.53 (+0.00) | 1.51 (+0.00) |
| GPT-6 Astra (high) on ChatGPT Pro 200 | 0.00 (+0.00) | 0.00 (+0.00) | 1.05 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.53 (+0.00) | 1.51 (+0.00) |
| GPT-6 Astra (high) on ChatGPT Pro 500 | 0.00 (+0.00) | 0.00 (+0.00) | 1.05 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.53 (+0.00) | 1.51 (+0.00) |
| GPT-6 Astra (max) on ChatGPT Plus | 0.00 (+0.00) | 0.00 (+0.00) | 1.50 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.59 (+0.00) | 1.59 (+0.00) |
| GPT-6 Astra (max) on ChatGPT Pro 100 | 0.00 (+0.00) | 0.00 (+0.00) | 1.50 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.59 (+0.00) | 1.59 (+0.00) |
| GPT-6 Astra (max) on ChatGPT Pro 200 | 0.00 (+0.00) | 0.00 (+0.00) | 1.50 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.59 (+0.00) | 1.59 (+0.00) |
| GPT-6 Astra (max) on ChatGPT Pro 500 | 0.00 (+0.00) | 0.00 (+0.00) | 1.50 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.59 (+0.00) | 1.59 (+0.00) |
| GPT-6 Astra (xhigh) on ChatGPT Plus | 0.00 (+0.00) | 0.00 (+0.00) | 1.42 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.59 (+0.00) | 1.58 (+0.00) |
| GPT-6 Astra (xhigh) on ChatGPT Pro 100 | 0.00 (+0.00) | 0.00 (+0.00) | 1.42 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.59 (+0.00) | 1.58 (+0.00) |
| GPT-6 Astra (xhigh) on ChatGPT Pro 200 | 0.00 (+0.00) | 0.00 (+0.00) | 1.42 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.59 (+0.00) | 1.58 (+0.00) |
| GPT-6 Astra (xhigh) on ChatGPT Pro 500 | 0.00 (+0.00) | 0.00 (+0.00) | 1.42 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.59 (+0.00) | 1.58 (+0.00) |
| GPT-6 Luna (high) on ChatGPT Plus | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6 Luna (high) on ChatGPT Pro 100 | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6 Luna (high) on ChatGPT Pro 200 | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6 Luna (high) on ChatGPT Pro 500 | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6 Luna (low) on ChatGPT Plus | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6 Luna (low) on ChatGPT Pro 100 | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6 Luna (low) on ChatGPT Pro 200 | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6 Luna (low) on ChatGPT Pro 500 | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Plus | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 100 | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 200 | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 500 | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6 Luna (medium) on ChatGPT Plus | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6 Luna (medium) on ChatGPT Pro 100 | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6 Luna (medium) on ChatGPT Pro 200 | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6 Luna (medium) on ChatGPT Pro 500 | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6 Luna (xhigh) on ChatGPT Plus | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6 Luna (xhigh) on ChatGPT Pro 100 | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6 Luna (xhigh) on ChatGPT Pro 200 | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6 Luna (xhigh) on ChatGPT Pro 500 | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6.1 Sol (high) on ChatGPT Plus | 0.00 (+0.00) | 0.00 (+0.00) | 1.15 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.53 (+0.00) | 1.51 (+0.00) |
| GPT-6.1 Sol (high) on ChatGPT Pro 100 | 0.00 (+0.00) | 0.00 (+0.00) | 1.15 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.53 (+0.00) | 1.51 (+0.00) |
| GPT-6.1 Sol (high) on ChatGPT Pro 200 | 0.00 (+0.00) | 0.00 (+0.00) | 1.15 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.53 (+0.00) | 1.51 (+0.00) |
| GPT-6.1 Sol (high) on ChatGPT Pro 500 | 0.00 (+0.00) | 0.00 (+0.00) | 1.15 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.53 (+0.00) | 1.51 (+0.00) |
| GPT-6.1 Sol (low) on ChatGPT Plus | 0.00 (+0.00) | 0.00 (+0.00) | 1.26 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.31 (+0.00) | 1.30 (+0.00) |
| GPT-6.1 Sol (low) on ChatGPT Pro 100 | 0.00 (+0.00) | 0.00 (+0.00) | 1.26 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.31 (+0.00) | 1.30 (+0.00) |
| GPT-6.1 Sol (low) on ChatGPT Pro 200 | 0.00 (+0.00) | 0.00 (+0.00) | 1.26 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.31 (+0.00) | 1.30 (+0.00) |
| GPT-6.1 Sol (low) on ChatGPT Pro 500 | 0.00 (+0.00) | 0.00 (+0.00) | 1.26 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.31 (+0.00) | 1.30 (+0.00) |
| GPT-6.1 Sol (max) on ChatGPT Plus | 0.00 (+0.00) | 0.00 (+0.00) | 1.79 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.63 (+0.00) | 1.62 (+0.00) |
| GPT-6.1 Sol (max) on ChatGPT Pro 100 | 0.00 (+0.00) | 0.00 (+0.00) | 1.79 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.63 (+0.00) | 1.62 (+0.00) |
| GPT-6.1 Sol (max) on ChatGPT Pro 200 | 0.00 (+0.00) | 0.00 (+0.00) | 1.79 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.63 (+0.00) | 1.62 (+0.00) |
| GPT-6.1 Sol (max) on ChatGPT Pro 500 | 0.00 (+0.00) | 0.00 (+0.00) | 1.79 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.63 (+0.00) | 1.62 (+0.00) |
| GPT-6.1 Sol (medium) on ChatGPT Plus | 0.00 (+0.00) | 0.00 (+0.00) | 1.00 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.46 (+0.00) | 1.47 (+0.00) |
| GPT-6.1 Sol (medium) on ChatGPT Pro 100 | 0.00 (+0.00) | 0.00 (+0.00) | 1.00 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.46 (+0.00) | 1.47 (+0.00) |
| GPT-6.1 Sol (medium) on ChatGPT Pro 200 | 0.00 (+0.00) | 0.00 (+0.00) | 1.00 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.46 (+0.00) | 1.47 (+0.00) |
| GPT-6.1 Sol (medium) on ChatGPT Pro 500 | 0.00 (+0.00) | 0.00 (+0.00) | 1.00 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.46 (+0.00) | 1.47 (+0.00) |
| GPT-6.1 Sol (xhigh) on ChatGPT Plus | 0.00 (+0.00) | 0.00 (+0.00) | 1.59 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.61 (+0.00) | 1.61 (+0.00) |
| GPT-6.1 Sol (xhigh) on ChatGPT Pro 100 | 0.00 (+0.00) | 0.00 (+0.00) | 1.59 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.61 (+0.00) | 1.61 (+0.00) |
| GPT-6.1 Sol (xhigh) on ChatGPT Pro 200 | 0.00 (+0.00) | 0.00 (+0.00) | 1.59 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.61 (+0.00) | 1.61 (+0.00) |
| GPT-6.1 Sol (xhigh) on ChatGPT Pro 500 | 0.00 (+0.00) | 0.00 (+0.00) | 1.59 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.61 (+0.00) | 1.61 (+0.00) |
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
| Gemini 4 Argon (high) on API-cost fallback | 0.00 (+0.00) | 0.00 (+0.00) | 1.36 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.35 (+0.00) | 1.34 (+0.00) |
| Kimi K3.1 Pro (max) on API-cost fallback | 0.00 (+0.00) | 0.00 (+0.00) | 1.49 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.40 (+0.00) | 1.39 (+0.00) |
| MiMo-V2.6-Pro on MiMo Token Plan Lite | 0.00 (+0.00) | — | — | — | — | — | — |
| MiMo-V2.6-Pro on MiMo Token Plan Max | 0.00 (+0.00) | — | — | — | — | — | — |
| MiMo-V2.6-Pro on MiMo Token Plan Pro | 0.00 (+0.00) | — | — | — | — | — | — |
| MiMo-V2.6-Pro on MiMo Token Plan Standard | 0.00 (+0.00) | — | — | — | — | — | — |

### Named S2 specification branches

- **Bug Hunt harness band (E19)** (S2): unevaluable; the captured tbench.ai leaderboard lists no configuration under two or more agents, so no cross-agent spread exists
- **cache-hit variation (E34)** (S2): unevaluable; AA's published cost embeds its cache-pricing protocol; varying the cache-hit rate needs each basket component's cache-read and uncached-input demand, which AA publishes only for the whole Index (E157)
- **first-party list versus cross-provider median price rule (E122)** (S2): unevaluable; AA publishes one price per configuration under its own rule; the alternative rule's prices are not captured

### Common-leaf ranking (diagnostic): diagnostics

- **Terminal-Bench cross-source agreement (AA's mini-SWE-agent run against tbench.ai):** defined; 0 rows take the leaf from tbench.ai (gap fill).
- **Workload cross-check (E41, mandatory diagnostic):** Terminal-Bench 4.0 cost per solved task on AA's own execution against basket cost: τ_b 0.52 (interval 0.22 to 0.77), uncertain agreement; panel (33): Claude Haiku 5.5 (xhigh), Claude Haiku 5.5 (high), Claude Haiku 5.5 (low), Claude Haiku 5.5 (max), Claude Haiku 5.5 (medium), Claude Opus 5.5 (max), Claude Opus 5.5 (high), Claude Opus 5.5 (medium), Claude Opus 5.5 (xhigh), Claude Sonnet 5.5 (max), Claude Sonnet 5.5 (xhigh), DeepSeek V4.1 Flash 1017 (max), Gemini 4 Argon (high), GPT-6 Astra (max), GPT-6 Astra (high), GPT-6 Astra (xhigh), GPT-6 Luna (max), GPT-6 Luna (high), GPT-6 Luna (low), GPT-6 Luna (medium), GPT-6 Luna (xhigh), GPT-6.1 Sol (max), GPT-6.1 Sol (high), GPT-6.1 Sol (low), GPT-6.1 Sol (medium), GPT-6.1 Sol (xhigh), GPT-6.1 Terra (max), GPT-6.1 Terra (high), GPT-6.1 Terra (low), GPT-6.1 Terra (medium), GPT-6.1 Terra (xhigh), Kimi K3.1 Pro (max), MiMo-V2.6-Pro.
- **Rank separability (O39, independent-task approximation):** median separation 3.77 value points (API) and 3.89 (Plan); separable adjacent ranks: API 0 of 32, Plan 1 of 49. Assumptions: tasks are independent and each leaf's score is a mean over its published task count (a binomial leaf drawn from its Jeffreys posterior Beta(k + 1/2, n - k + 1/2), O142; plug-in SDs with the proportion (k + 1/2) / (n + 1), I28); attempts averaged within a task and tasks shared across models are ignored, so the noise is approximate; GDPval-AA: each row's rating interval as AA's model page displays it, read as a 95% normal interval (AA states no level), SD = half-width / 1.96; AA-Omniscience: each of 3,000 questions scores +1, 0 or -1, with the shares from AA's accuracy and hallucination rate; Vals boards (Vibe Code Bench v1.1, Code Migration v1.1): Vals' published standard error per record, read as the leaf's SD; AI Coding Daily: judged points over its six graded projects read as a binomial share of 60 points (an assumption; the board publishes no error).
- **FrontierCode against Cognition:** FrontierCode 2.0 cross-source agreement (AA against Cognition, exact model and effort; E234, O153): Kendall tau 0.91 (interval 0.83 to 0.97) on 26 rows. Cognition minus AA: mean -1.5 points, largest 7.7.
- **Gap-fill removal (E234, diagnostic):** no ranked row has a leaf from another party or the provider.
- **Bar results without the gap fills (E234, sensitivity; labels unchanged):** cheapest displayed row as published, with fills removed, and with third-party fills third-party fills minus the signed mean offset -1.5 points (third party minus AA) — API quality 50.0: GPT-6.1 Sol (medium) in all three; API quality 35.0: GPT-6 Luna (max) in all three; API quality 58.0: GPT-6.1 Sol (xhigh) in all three; Plan quality 50.0: Claude Opus 5.5 (medium) in all three; Plan quality 35.0: Claude Haiku 5.5 (xhigh) in all three; Plan quality 58.0: GPT-6.1 Sol (xhigh) in all three.
- **Harness cost (O123, S2 stress):** unevaluable: no model is listed under two or more agents in AA's Coding Agent Index capture, so no agent effect is identified (O123). Coding Agent Index agents (each part of its costed configuration; none is the run behind the FrontierCode or Terminal-Bench leaf): GPT-6.1 Sol (max): Codex; GPT-6.1 Terra (max): Codex; Claude Opus 5.5 (max): Claude Code; Claude Sonnet 5.5 (max): Claude Code; GPT-6 Astra (max): Codex; DeepSeek V4.1 Flash 1017 (max): DeepSeek Harness; Gemini 4 Argon (high): Antigravity CLI; Claude Haiku 5.5 (max): Claude Code; GPT-6.1 Terra (xhigh): Codex; GPT-6.1 Terra (high): Codex; GPT-6 Luna (max): Codex; GPT-6.1 Terra (medium): Codex; GPT-6.1 Terra (low): Codex.
- **Quality agreement:** quality agreement (matched-panel sensitivity): Kendall tau 0.76 (interval 0.64 to 0.86) on 33 rows.
- **Quality-substitution value agreement (API):** quality-substitution value agreement, api basis (matched-panel sensitivity): Kendall tau 0.68 (interval 0.51 to 0.81) on 33 rows.
- **Quality-substitution value agreement (Plan):** quality-substitution value agreement, plan basis (matched-panel sensitivity): Kendall tau 0.57 (interval 0.36 to 0.74) on 33 rows.
- **Disjoint-evidence agreement:** disjoint-evidence agreement (restricted evidence comparison, not an eligible ranking): Kendall tau 0.61 (interval 0.47 to 0.74) on 33 rows.
- **Quality source shares:** AA-run 85%, independent 15%.
- **Non-discriminating leaves:** none.
- **Group drift:** estimated; flagged: none.
- **Omniscience abstention sensitivity** (z_pen = max(0, I)): 13 rows move; largest move 3 (DeepSeek V4.1 Flash 1017 (max)).
- **GDPval-AA logistic sensitivity** (z = 100 / (1 + 10^((1600 - E) / 400)) against AA's pinned anchor; every other input fixed): API 18 rows move; largest move 4 (GPT-6 Astra (high), MiMo-V2.6-Pro); Plan 19 rows move; largest move 4 (Claude Opus 5.5 (max), GPT-6.1 Sol (medium)).
- **Anchor stability:** trimmed anchors (P10 / 2 and P90 x 2 (diagnostic only)) give $31.35 to $8,586.96; 25 rows move; largest move 7 (Gemini 4 Argon (high)).

- **Basket readiness (E22):** priced leaves cover 57% of nominal quality weight (AutomationBench-AA, FrontierCode 2.0, Terminal-Bench-Science 0.1, Terminal-Bench 4.0 (AA run)); pending components: Coding Agent Index, ITBench-AA.
- **SWE cost companion (O14, diagnostic):** 13 rows evaluated; flagged far from the median ratio: DeepSeek V4.1 Flash 1017 (max), Claude Haiku 5.5 (max).
- **Matched-cost diagnostic (E55):** evaluated at 70% priced quality weight; basket/matched cost-order reversals with separated intervals: 4; rank-gap warnings: 0.
- **Frontier-families anchors (E187, diagnostic):** anchors rebuilt from the 22 frontier and near-frontier references move API no rank changes (value points per cost doubling 2.14 vs 2.14 frozen); Plan 19 rows move; largest move 4 (GPT-6 Astra (high)) (value points per cost doubling 4.17 vs 3.66 frozen).
- **Frontier-families bar (E199, sensitivity; the frozen bar stays primary):** quality 46.2 over 25 configurations; cheapest at or above it on the API main workload: not unique; possibly GPT-6.1 Sol (medium), GPT-6.1 Terra (xhigh) (compares 14 configurations that can qualify).
- **One row per family (E205, diagnostic; the frozen ladder and anchors stay primary):** with each family's primary configuration only (7 rows in the one-row-per-family bar population), the ladder (headline, lower quartile, upper quartile) would be 58.0 / 31.5 / 62.0 against 50.0 / 35.0 / 58.0 frozen; anchors rebuilt from its 6 references move API 20 rows move; largest move 5 (Gemini 4 Argon (high)) (value points per cost doubling 2.82 vs 2.14 frozen); Plan 24 rows move; largest move 6 (GPT-6 Astra (max), GPT-6.1 Sol (low)) (value points per cost doubling 7.54 vs 3.66 frozen).
- **Ladder over scored rows (I28, sensitivity; the frozen ladder stays primary):** the bar population keeps full-benchmark rows that have no cost; today every such row has a cost, so the ladder is unchanged.
- **Bar currency (E207, informational):** rows reaching each frozen bar: quality 50.0: 17 of 33; quality 35.0: 25 of 33; quality 58.0: 9 of 33; the current population would freeze 50.0 / 35.0 / 58.0; lifetime until the next anchor re-freeze or methodology version, whichever comes first; no staleness flag.
- **Token mix (E208):** 1 selected routes: mix not reported: the measurement publishes no token-category shares; 29 selected routes: mix unidentified: the basket's token-category shares are set-identified only (E124), so the L1 test (above 0.30 flags mix-unmatched) is not computed.
- **Observed-range sensitivity (E219, not evidence; no label changes):** with each missing leaf inside the cohort's observed range for that leaf, quality 50.0: 13 can qualify, 12 confirmed; GPT-6.1 Sol (medium) confirmed cheapest; quality 35.0: 19 can qualify, 18 confirmed; possibly cheapest GPT-6 Luna (max), MiMo-V2.6-Pro; quality 58.0: 7 can qualify, 7 confirmed; GPT-6.1 Sol (xhigh) confirmed cheapest.
- **What would settle the headline bar (E221, not a claim):** rows that can but need not reach quality 50.0, with the mean score their missing leaves would need: DeepSeek V4.1 Flash 1017 (max) (no missing leaf; reporting precision only).
- **Common leaf set (E226, diagnostic; scores unchanged):** without the leaves fewer than 90% of cohort rows have (none), API no rank changes; Plan no rank changes; rows reaching each bar: quality 50.0: 17 → 17; quality 35.0: 25 → 25; quality 58.0: 9 → 9; rows whose displayed quality differs from common-leaf quality by more than one cost doubling's worth: none.
- **Harness by leaf (E227):** Terminal-Bench: mini-SWE-agent 33; Bug Hunt: Codex CLI 18, Claude Code 11, Antigravity CLI 1, Claude Code / Moonshot API 1, Claude Code / Xiaomi first-party 1, DeepSeek Harness / DeepSeek API 1.
- **Coding Agent Index safety refusals (O63, flagged; costs and scores unchanged):** GPT-6.1 Sol (max) (15 blocked of 870 attempts); Claude Opus 5.5 (max) (76 finished by Claude Opus 4.8 or Claude Opus 5 of 870 attempts); Claude Sonnet 5.5 (45 finished by Claude Opus 4.8 of 870 attempts); GPT-6 Astra (max) (13 blocked of 870 attempts); Claude Haiku 5.5 (max) (3 finished by Claude Opus 5 of 870 attempts); GPT-6.1 Terra (low) (1 blocked of 870 attempts).

### Leave-one-component-out cost family (E172)

Each admitted basket unit removed in turn, scored on anchors rebuilt by the freeze rule (rank changes against the primary ranking; quality held fixed).

| Removed component | API rank changes | Plan rank changes | API value points per cost doubling |
|---|---|---|---:|
| AA-Briefcase | 6 rows move; largest move 1 (Claude Haiku 5.5 (high), Gemini 4 Argon (high), GPT-6.1 Sol (low), GPT-6.1 Terra (low), GPT-6.1 Terra (medium), MiMo-V2.6-Pro) | 24 rows move; largest move 3 (DeepSeek V4.1 Flash 1017 (max), GPT-6 Astra (max), GPT-6 Astra (high), GPT-6.1 Sol (medium)) | 2.21 |
| GDP.pdf | 5 rows move; largest move 2 (GPT-6 Luna (low)) | 19 rows move; largest move 3 (Claude Haiku 5.5 (xhigh), DeepSeek V4.1 Flash 1017 (max), GPT-6 Astra (max), GPT-6 Astra (high)) | 2.08 |
| AutomationBench-AA | 10 rows move; largest move 2 (Claude Haiku 5.5 (low), GPT-6 Luna (low)) | 22 rows move; largest move 6 (Claude Haiku 5.5 (max)) | 2.00 |
| Terminal-Bench 4.0 (AA Index run) | 4 rows move; largest move 1 (Claude Haiku 5.5 (high), Gemini 4 Argon (high), GPT-6.1 Terra (low), MiMo-V2.6-Pro) | 18 rows move; largest move 4 (GPT-6 Astra (high)) | 2.16 |
| FrontierCode 2.0 | 11 rows move; largest move 2 (GPT-6.1 Terra (high)) | 18 rows move; largest move 4 (GPT-6 Astra (max)) | 2.17 |
| Terminal-Bench-Science | 13 rows move; largest move 2 (GPT-6.1 Sol (low)) | 23 rows move; largest move 4 (Claude Sonnet 5.5 (xhigh)) | 2.19 |

### Subset rows: paired bridge and missing spend (E10, E173)

No row is scored on a subset workload.

### Deletion sensitivity

| Branch | Retained nominal weight | Status | API rank changes | Plan rank changes |
|---|---:|---|---|---|
| leave-out:frontierCode | 75% | evaluated | 18 rows move; largest move 6 (Gemini 4 Argon (high)) | 27 rows move; largest move 5 (GPT-6.1 Sol (low)) |
| leave-out:terminalBench | 80% | evaluated | 21 rows move; largest move 10 (GPT-6 Luna (max)) | 20 rows move; largest move 6 (GPT-6 Luna (max)) |
| leave-out:bugHunt | 85% | evaluated | 26 rows move; largest move 11 (DeepSeek V4.1 Flash 1017 (max)) | 28 rows move; largest move 12 (GPT-6.1 Sol (max)) |
| leave-out:gdpval | 90% | evaluated | 13 rows move; largest move 2 (GPT-6.1 Terra (high)) | 20 rows move; largest move 4 (GPT-6 Astra (xhigh)) |
| leave-out:automationBench | 90% | evaluated | 15 rows move; largest move 2 (Claude Haiku 5.5 (xhigh), Claude Haiku 5.5 (max), Claude Haiku 5.5 (medium), Gemini 4 Argon (high), GPT-6 Luna (low)) | 11 rows move; largest move 2 (GPT-6.1 Terra (high)) |
| leave-out:omniscience | 90% | evaluated | 18 rows move; largest move 4 (MiMo-V2.6-Pro) | 22 rows move; largest move 2 (Claude Haiku 5.5 (low), Claude Opus 5.5 (medium), Claude Sonnet 5.5 (xhigh), GPT-6 Luna (max)) |
| leave-out:lcr | 95% | evaluated | 8 rows move; largest move 1 (Claude Haiku 5.5 (high), Claude Haiku 5.5 (max), Claude Opus 5.5 (high), Claude Sonnet 5.5 (xhigh), Gemini 4 Argon (high), GPT-6.1 Sol (low), GPT-6.1 Terra (low), GPT-6.1 Terra (medium)) | 8 rows move; largest move 1 (Claude Haiku 5.5 (max), Claude Opus 5.5 (max), Claude Opus 5.5 (medium), Gemini 4 Argon (high), GPT-6 Astra (max), GPT-6 Astra (high), GPT-6.1 Terra (high), MiMo-V2.6-Pro) |
| leave-out:hle | 98% | evaluated | 6 rows move; largest move 1 (Claude Opus 5.5 (high), Claude Sonnet 5.5 (xhigh), Gemini 4 Argon (high), GPT-6.1 Sol (low), GPT-6.1 Terra (medium), MiMo-V2.6-Pro) | no rank changes |
| leave-out:tbScience | 98% | evaluated | 4 rows move; largest move 1 (Claude Haiku 5.5 (xhigh), Gemini 4 Argon (high), GPT-6 Luna (max), MiMo-V2.6-Pro) | no rank changes |
| leave-out:critpt | 98% | evaluated | 4 rows move; largest move 1 (Claude Haiku 5.5 (high), GPT-6.1 Sol (low), GPT-6.1 Terra (low), GPT-6.1 Terra (medium)) | 2 rows move; largest move 1 (GPT-6 Astra (high), GPT-6.1 Terra (high)) |
| leave-source-out:Artificial Analysis | 15% | not identifiable under the coverage rule | — | — |
| basket-scope | 87% | evaluated | 18 rows move; largest move 4 (MiMo-V2.6-Pro) | 20 rows move; largest move 2 (Claude Haiku 5.5 (low), Claude Sonnet 5.5 (xhigh), GPT-6 Luna (max), MiMo-V2.6-Pro) |

### Cost-component removal (Terminal-Bench 4.0 (AA Index run): evaluated)

| Basis | Run | Rank changes |
|---|---|---|
| api | cost-component removal, original anchors | 4 rows move; largest move 1 (Claude Haiku 5.5 (high), Gemini 4 Argon (high), GPT-6.1 Terra (low), MiMo-V2.6-Pro) |
| api | alternative workload, recalibrated anchors | 4 rows move; largest move 1 (Claude Haiku 5.5 (high), Gemini 4 Argon (high), GPT-6.1 Terra (low), MiMo-V2.6-Pro) |
| plan | cost-component removal, original anchors; fixed-multiple arithmetic stress (not identified Plan economics for the altered workload) | 6 rows move; largest move 1 (Claude Haiku 5.5 (xhigh), Claude Haiku 5.5 (max), Claude Opus 5.5 (high), GPT-6 Astra (max), GPT-6.1 Sol (medium), GPT-6.1 Terra (medium)) |
| plan | alternative workload, recalibrated anchors; fixed-multiple arithmetic stress (not identified Plan economics for the altered workload) | 18 rows move; largest move 4 (GPT-6 Astra (high)) |

### Common-leaf ranking (diagnostic): release gates

| Rule | Status | Detail |
|---|---|---|
| clip gate (E20) | passed | no basis exceeds the clipping allowance |
| cost influence flag (E91) | passed | cost not discriminating (< 10%); informational only; beta never changes (O2) |
| realised influence (E272) | fired | API: cost term offsetting (-62% of value variance); Plan: cost term offsetting (-28% of value variance); informational only, beta never changes (O2) |
| quality influence flag (E126) | passed | quality not discriminating (cost share > 90%); informational only |
| subset scoring (O17) | vacuous | subset rows scored on their own workload and anchors |
| partial component flag (E37) | fired | AA declined- or missing-task markers, or an Index reconstruction that misses AA's total (E209) |
| route dominance filter (E88) | vacuous | certifiably dearer routes set aside |
| Plan exploratory label (E61) | fired | fewer than half of Plan rows have an identified M_W |
| Plan evidence lifecycle and change detection (E18, E151, E269, O77, O79) | fired | 105 of 112 plan rows carry a possibly-superseded or expired route: claude-haiku-5-5-high@claude-max-20x, claude-haiku-5-5-high@claude-max-5x, claude-haiku-5-5-high@claude-pro, claude-haiku-5-5-low@claude-max-20x, claude-haiku-5-5-low@claude-max-5x, claude-haiku-5-5-low@claude-pro, claude-haiku-5-5-max@claude-max-20x, claude-haiku-5-5-max@claude-max-5x, claude-haiku-5-5-max@claude-pro, claude-haiku-5-5-medium@claude-max-20x, claude-haiku-5-5-medium@claude-max-5x, claude-haiku-5-5-medium@claude-pro, claude-haiku-5-5@claude-max-20x, claude-haiku-5-5@claude-max-5x, claude-haiku-5-5@claude-pro, claude-opus-5-5-high@claude-max-20x, claude-opus-5-5-high@claude-max-5x, claude-opus-5-5-high@claude-pro, claude-opus-5-5-medium@claude-max-20x, claude-opus-5-5-medium@claude-max-5x, claude-opus-5-5-medium@claude-pro, claude-opus-5-5-xhigh@claude-max-20x, claude-opus-5-5-xhigh@claude-max-5x, claude-opus-5-5-xhigh@claude-pro, claude-opus-5-5@claude-max-20x, claude-opus-5-5@claude-max-5x, claude-opus-5-5@claude-pro, claude-sonnet-5-5-xhigh@claude-max-20x, claude-sonnet-5-5-xhigh@claude-max-5x, claude-sonnet-5-5-xhigh@claude-pro, claude-sonnet-5-5@claude-max-20x, claude-sonnet-5-5@claude-max-5x, claude-sonnet-5-5@claude-pro, gpt-6-astra-high@chatgpt-plus, gpt-6-astra-high@chatgpt-pro-100, gpt-6-astra-high@chatgpt-pro-200, gpt-6-astra-high@chatgpt-pro-500, gpt-6-astra-xhigh@chatgpt-plus, gpt-6-astra-xhigh@chatgpt-pro-100, gpt-6-astra-xhigh@chatgpt-pro-200, gpt-6-astra-xhigh@chatgpt-pro-500, gpt-6-astra@chatgpt-plus, gpt-6-astra@chatgpt-pro-100, gpt-6-astra@chatgpt-pro-200, gpt-6-astra@chatgpt-pro-500, gpt-6-luna-high@chatgpt-plus, gpt-6-luna-high@chatgpt-pro-100, gpt-6-luna-high@chatgpt-pro-200, gpt-6-luna-high@chatgpt-pro-500, gpt-6-luna-low@chatgpt-plus, gpt-6-luna-low@chatgpt-pro-100, gpt-6-luna-low@chatgpt-pro-200, gpt-6-luna-low@chatgpt-pro-500, gpt-6-luna-medium@chatgpt-plus, gpt-6-luna-medium@chatgpt-pro-100, gpt-6-luna-medium@chatgpt-pro-200, gpt-6-luna-medium@chatgpt-pro-500, gpt-6-luna-xhigh@chatgpt-plus, gpt-6-luna-xhigh@chatgpt-pro-100, gpt-6-luna-xhigh@chatgpt-pro-200, gpt-6-luna-xhigh@chatgpt-pro-500, gpt-6-luna@chatgpt-plus, gpt-6-luna@chatgpt-pro-100, gpt-6-luna@chatgpt-pro-200, gpt-6-luna@chatgpt-pro-500, gpt-6.1-sol-high@chatgpt-plus, gpt-6.1-sol-high@chatgpt-pro-100, gpt-6.1-sol-high@chatgpt-pro-200, gpt-6.1-sol-high@chatgpt-pro-500, gpt-6.1-sol-low@chatgpt-plus, gpt-6.1-sol-low@chatgpt-pro-100, gpt-6.1-sol-low@chatgpt-pro-200, gpt-6.1-sol-low@chatgpt-pro-500, gpt-6.1-sol-medium@chatgpt-plus, gpt-6.1-sol-medium@chatgpt-pro-100, gpt-6.1-sol-medium@chatgpt-pro-200, gpt-6.1-sol-medium@chatgpt-pro-500, gpt-6.1-sol-xhigh@chatgpt-plus, gpt-6.1-sol-xhigh@chatgpt-pro-100, gpt-6.1-sol-xhigh@chatgpt-pro-200, gpt-6.1-sol-xhigh@chatgpt-pro-500, gpt-6.1-sol@chatgpt-plus, gpt-6.1-sol@chatgpt-pro-100, gpt-6.1-sol@chatgpt-pro-200, gpt-6.1-sol@chatgpt-pro-500, gpt-6.1-terra-high@chatgpt-plus, gpt-6.1-terra-high@chatgpt-pro-100, gpt-6.1-terra-high@chatgpt-pro-200, gpt-6.1-terra-high@chatgpt-pro-500, gpt-6.1-terra-low@chatgpt-plus, gpt-6.1-terra-low@chatgpt-pro-100, gpt-6.1-terra-low@chatgpt-pro-200, gpt-6.1-terra-low@chatgpt-pro-500, gpt-6.1-terra-medium@chatgpt-plus, gpt-6.1-terra-medium@chatgpt-pro-100, gpt-6.1-terra-medium@chatgpt-pro-200, gpt-6.1-terra-medium@chatgpt-pro-500, gpt-6.1-terra-xhigh@chatgpt-plus, gpt-6.1-terra-xhigh@chatgpt-pro-100, gpt-6.1-terra-xhigh@chatgpt-pro-200, gpt-6.1-terra-xhigh@chatgpt-pro-500, gpt-6.1-terra@chatgpt-plus, gpt-6.1-terra@chatgpt-pro-100, gpt-6.1-terra@chatgpt-pro-200, gpt-6.1-terra@chatgpt-pro-500 |
| acknowledged accounting-fault windows (O91, O92, O93, O95, O96) | fired | 18 of 112 plan rows rest on a measurement inside an acknowledged fault window; they stay selected and yield to two concordant user reports for their own model and plan, and the transfers resting on them follow: gpt-6-astra-high@chatgpt-pro-500, gpt-6-astra-xhigh@chatgpt-pro-500, gpt-6-astra@chatgpt-pro-500, gpt-6-luna-high@chatgpt-pro-500, gpt-6-luna-low@chatgpt-pro-500, gpt-6-luna-medium@chatgpt-pro-500, gpt-6-luna-xhigh@chatgpt-pro-500, gpt-6-luna@chatgpt-pro-500, gpt-6.1-sol-high@chatgpt-pro-500, gpt-6.1-sol-low@chatgpt-pro-500, gpt-6.1-sol-medium@chatgpt-pro-500, gpt-6.1-sol-xhigh@chatgpt-pro-500, gpt-6.1-sol@chatgpt-pro-500, gpt-6.1-terra-high@chatgpt-pro-500, gpt-6.1-terra-low@chatgpt-pro-500, gpt-6.1-terra-medium@chatgpt-pro-500, gpt-6.1-terra-xhigh@chatgpt-pro-500, gpt-6.1-terra@chatgpt-pro-500 |
| AA cost omits a pricing term (O94, O98, O100, O106, O108, O109, O114) | fired | ranked at the published cost; compete in interval outputs and the scenario labels' BlockerSafe test over [C, factor × C] ([C, ∞) without a stated factor, O98) without a label (scenario frequencies draw them at the published cost, O114), and leave the anchor population at the next freeze: claude-haiku-5-5 (up to 5×), claude-haiku-5-5-high (up to 5×), claude-haiku-5-5-low (up to 5×), claude-haiku-5-5-max (up to 5×), claude-haiku-5-5-medium (up to 5×) |
| valuation-basis gate (E170) | passed | every ranked row is compatible as captured or after evidenced revaluation |
| source clocks and evidence freshness (O59, O60, O65, E211, E216, E217, E218) | passed | every capture is within its age gate and none after the cutoff unless its source predates the cutoff's day; the build stops otherwise |
| build-stopping evidence gates (O64, O69, O71, O75, O99, O100, O101, O103, O105-O111, E195, E204, E225) | passed | the Coding Agent Index manifest (O64), the Terminal-Bench agent list (E225), cutoff-day row dates (O69), the three-stage all-provider plan search (O71, O75), the typed change records behind every route flag and partition split, which also produce each route's label and blocking dates within its launch- and schedule-bounded span (O99, O101, O105, O107, O110, O111), the register of AA notes covering every captured one, with the chart's inventory and duplicate-entry checks, the post-O103 capture notes, the basket-chart labels and chart-level notes' named rows (O100, O103, O106, O108) and the frontier path checks (E195, E204) hold; the build stops otherwise |
| score swing gate (E177) | vacuous | first v3 release: no previous v3 release to compare |
| ranking coverage (O166) | vacuous | ranks 33 of 37 cohort configurations; first v3 release: no previous v3 release to compare |
| anchor migration (E184) | vacuous | no main-workload migration deferred |
| frozen admission (O169) | vacuous | every frozen component still meets the admission threshold |
| configuration map coverage | fired | cohort rows without a configuration-map entry (chart labels; the agent record is derived, E267): gpt-6.1-terra, gpt-6.1-terra-high, gpt-6.1-terra-low, gpt-6.1-terra-medium, gpt-6.1-terra-xhigh |
| quality clipping audit (E110) | passed | saturation disclosed; domain violations block the build |
| full benchmark set (O36, O38) | fired | listed, not ranked: gpt-5.6-luna-low, gemini-4-carbon, mimo-v2-6-flash, minimax-m3-1-flash |
| missing-leaf rules (O8 provisional, E198b, E201b, E219, E221, E226) | vacuous | no ranked row has a missing leaf (O36) |
| S1M interval stream (E145) | vacuous | dormant: no ranked leaf carries a published confidence interval since O37, so S1M equals S1 (E236) |
| provider-claim label denial (E233) | vacuous | no row has a provider-claimed leaf |
| scenario outputs current (E72) | passed | scenario input hash matches the scored inputs |
| diagnostic ranking (O121) | fired | no label is issued and the gates are disclosed without holding the release |


## Basket cost by component

USD at API rates for the exact configuration; "—" marks a component without an exact cost.

| Configuration | Coding Agent Index | ITBench-AA | AA-Briefcase | GDP.pdf | AutomationBench-AA | Terminal-Bench 4.0 (AA Index run) | FrontierCode 2.0 | Terminal-Bench-Science | Basket cost | Missing admitted components |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| GPT-6.1 Sol (max) | $436.35 | — | $210.45 | $41.99 | $195.01 | $120.30 | $149.21 | $233.73 | $1,387.03 | none |
| Claude Sonnet 5.5 (max) | $3,857.44 | — | $1,863.13 | $79.43 | $678.32 | $834.67 | $1,525.59 | $1,663.25 | $10,501.82 | none |
| Claude Opus 5.5 (max) | $3,312.59 | $146.00 | $1,915.18 | $155.23 | $938.69 | $865.21 | $1,776.08 | $1,397.97 | $10,360.96 | none |
| Claude Haiku 5.5 (max) | $775.43 | — | $61.41 | $5.27 | $27.80 | $43.02 | $60.79 | $72.36 | $1,046.08 | none |
| GPT-6 Astra (max) | $2,040.49 | $133.00 | $864.69 | $207.58 | $1,048.30 | $560.88 | $863.12 | $1,223.34 | $6,808.39 | none |
| GPT-6 Luna (max) | $46.16 | — | $15.47 | $2.85 | $23.91 | $15.59 | $23.22 | $31.79 | $158.99 | none |
| MiMo-V2.6-Pro | — | — | $34.60 | $2.40 | $27.77 | $28.91 | $33.87 | $44.15 | $171.70 | Coding Agent Index |
| DeepSeek V4.1 Flash 1017 (max) | $85.92 | — | $61.72 | $4.23 | $114.26 | $58.09 | $68.49 | $138.73 | $531.44 | none |
| Gemini 4 Argon (high) | $3,402.24 | — | $834.38 | $51.87 | $738.10 | $691.61 | $1,853.84 | $1,308.87 | $8,880.92 | none |

### Valuation basis

Valuation-basis gate (E170): 9 compatible as captured. AA's Index category costs reconcile exactly with the prices AA displays for each configuration at capture, so its applied prices are the prices in force at the release cutoff. Token metering (E176): 9 not published per configuration; AA values cached input at live measurements of each model's typical cache-hit rate. Source intervals (E174): terminalBench: captured, level 95% (tbench.ai: "The whiskers span the 95% confidence interval"); gdpval: captured, level unstated, level not stated by the source (the 95% level on AA's methodology page belongs to AA-Briefcase).

## Plan route selection

The Plan amount is the selected multiple times the cash paid for the fee period (E166), typed by what the measurement establishes; it is not capacity unless it says so. The multiple values only the measured workload's API-equivalent consumption; other plan features are not valued.

| Configuration | Selected route | Plan amount | Basket runs per fee period | Identification | Plan cost (USD per basket run) | Flags | Selection reason |
|---|---|---|---|---|---:|---|---|
| GPT-6.1 Sol (max) | ChatGPT Pro 500 $500 · GPT-6.1 Sol (10.772×, measured) | $5,386 per month: measured-workload capacity | 3.88 per month | unidentified | $128.76 | workload-unmatched; possibly-superseded; measured inside an acknowledged accounting-fault window (O91, O92); valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| Claude Sonnet 5.5 (max) | Claude Pro $20 · common Claude assumption (58.9×, assumption) | $1,178 per month: assumed API-equivalent consumption (owner-named transfer) from claude-pro-opus55-semianalysis | 0.11 per month | unidentified | $178.30 | workload-unmatched; owner-named transfer (assumption); possibly-superseded; valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| Claude Opus 5.5 (max) | Claude Pro $20 · Opus 5.5 (58.9×, measured) | $1,178 per month: measured-workload capacity | 0.11 per month | unidentified | $175.91 | workload-unmatched; possibly-superseded; valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| Claude Haiku 5.5 (max) | Claude Pro $20 · common Claude assumption (58.9×, assumption) | $1,178 per month: assumed API-equivalent consumption (owner-named transfer) from claude-pro-opus55-semianalysis | 1.13 per month | unidentified | $17.76 | workload-unmatched; owner-named transfer (assumption); possibly-superseded; valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| GPT-6 Astra (max) | ChatGPT Pro 200 $200 · GPT-6 Astra (14.485×, measured) | $2,897 per month: measured-workload capacity | 0.43 per month | unidentified | $470.03 | workload-unmatched; possibly-superseded; valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| GPT-6 Luna (max) | ChatGPT Pro 500 $500 · common GPT assumption (10.772×, assumption) | $5,386 per month: assumed API-equivalent consumption (owner-named transfer) from chatgpt-pro500-gpt61sol-semianalysis | 33.88 per month | unidentified | $14.76 | workload-unmatched; owner-named transfer (assumption); possibly-superseded; measured inside an acknowledged accounting-fault window (O91, O92); valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| MiMo-V2.6-Pro | MiMo Token Plan Max $100 · quota ceiling (provider-derived) (1.1808×, assumption) | $118 per month: provider quota ceiling: the full quota at API rates (O46; full use assumed) | 0.69 per month | unidentified | $145.41 | workload-unmatched; provider quota ceiling; full use assumed, the optimistic end on use; credits valued at the recorded API rate, not the highest (O46, O125) | larger quota-ceiling multiple (O46: provider-derived, not observed) |
| DeepSeek V4.1 Flash 1017 (max) | — | — | — | — | $531.44 | API-cost fallback: no admitted Plan route; cross-estimand ordering not identified | no eligible route |
| Gemini 4 Argon (high) | — | — | — | — | $8,880.92 | API-cost fallback: no admitted Plan route; cross-estimand ordering not identified | no eligible route |

### Route alternatives

Every admissible route-measurement pair in comparator order (E171) and the comparator's pick with the selected pair removed (E179). A larger displayed multiple is arithmetic on the measured workload, never a claim that the route is cheaper on the scored workload. Workday-feasible multiple (E15), for the 7 routed rows: not evaluated: no evidenced quota schema for this route.

| Configuration | Admissible pairs | Unidentified | Pairs (multiple, status) | Leave-selected-out choice |
|---|---:|---:|---|---|
| GPT-6.1 Sol (max) | 4 | 4 | chatgpt-pro500-gpt61sol-semianalysis (10.772×, selected); chatgpt-plus-gpt61sol-semianalysis (10.55×, not selected by the comparator); chatgpt-pro100-gpt61sol-semianalysis (10.55×, not selected by the comparator); chatgpt-pro200-gpt61sol-semianalysis (10.42×, not selected by the comparator) | chatgpt-plus-gpt61sol-semianalysis (10.55×, value 71.35) |
| Claude Sonnet 5.5 (max) | 3 | 3 | claude-pro-claude-sonnet-5-5-common-opus55-assumption (58.9×, selected); claude-max20x-claude-sonnet-5-5-common-opus55-assumption (58.63×, not selected by the comparator); claude-max5x-claude-sonnet-5-5-common-opus55-assumption (57.25×, not selected by the comparator) | claude-max20x-claude-sonnet-5-5-common-opus55-assumption (58.63×, value 68.56) |
| Claude Opus 5.5 (max) | 3 | 3 | claude-pro-opus55-semianalysis (58.9×, selected); claude-max20x-opus55-semianalysis (58.63×, not selected by the comparator); claude-max5x-opus55-semianalysis (57.25×, not selected by the comparator) | claude-max20x-opus55-semianalysis (58.63×, value 68.47) |
| Claude Haiku 5.5 (max) | 3 | 3 | claude-pro-claude-haiku-5-5-max-common-opus55-assumption (58.9×, selected); claude-max20x-claude-haiku-5-5-max-common-opus55-assumption (58.63×, not selected by the comparator); claude-max5x-claude-haiku-5-5-max-common-opus55-assumption (57.25×, not selected by the comparator) | claude-max20x-claude-haiku-5-5-max-common-opus55-assumption (58.63×, value 62.41) |
| GPT-6 Astra (max) | 4 | 4 | chatgpt-pro200-gpt6astra-semianalysis (14.485×, selected); chatgpt-pro500-gpt6astra-semianalysis (13.91×, not selected by the comparator); chatgpt-pro100-gpt6astra-semianalysis (13.22×, not selected by the comparator); chatgpt-plus-gpt6astra-semianalysis (8.1×, not selected by the comparator) | chatgpt-pro500-gpt6astra-semianalysis (13.91×, value 61.76) |
| GPT-6 Luna (max) | 4 | 4 | chatgpt-pro500-gpt-6-luna-common-gpt-assumption (10.772×, selected); chatgpt-pro100-gpt-6-luna-common-gpt-assumption (10.55×, not selected by the comparator); chatgpt-pro200-gpt-6-luna-common-gpt-assumption (10.42×, not selected by the comparator); chatgpt-plus-gpt-6-luna-common-gpt-assumption (8.1×, not selected by the comparator) | chatgpt-pro100-gpt-6-luna-common-gpt-assumption (10.55×, value 58.76) |
| MiMo-V2.6-Pro | 4 | 4 | mimo-tokenplan-max-mimo-v2-6-pro-quota-ceiling (1.1808×, selected); mimo-tokenplan-pro-mimo-v2-6-pro-quota-ceiling (1.0944×, not selected by the comparator); mimo-tokenplan-standard-mimo-v2-6-pro-quota-ceiling (0.99×, not selected by the comparator); mimo-tokenplan-lite-mimo-v2-6-pro-quota-ceiling (0.984×, not selected by the comparator) | mimo-tokenplan-pro-mimo-v2-6-pro-quota-ceiling (1.0944×, value 51.69) |

### Route brackets (O144, O146)

A plan meter counts tokens (O126), so a multiple measured on one model or effort is worth the target's price per metered token over the donor's: a Claude transfer (O144) is bracketed by the two models' list prices over the registry's shared token mix, and a same-model cross-effort route (O146) by the two configurations' own Intelligence Index token mixes. Each row is rescored at M × min(1, r) and M × max(1, r) with every other row at its displayed value. ChatGPT transfers are not bracketed (Codex credits are priced per model at API parity, O144). Scores and ranks are unchanged.

6 rows bracketed; 6 change Plan rank within their bracket.

| Plan row | Rule | Price ratio r | Multiple range | Plan value range | Plan rank range |
|---|---|---:|---|---|---|
| Claude Sonnet 5.5 (max) on claude-max-20x | O144 | 0.500 | 29.32–58.63 | 63.25–68.56 | 6–10 |
| Claude Sonnet 5.5 (max) on claude-max-5x | O144 | 0.500 | 28.62–57.25 | 63.07–68.38 | 9–10 |
| Claude Sonnet 5.5 (max) on claude-pro | O144 | 0.500 | 29.45–58.90 | 63.28–68.59 | 5–10 |
| Claude Haiku 5.5 (max) on claude-max-20x | O144 | 0.031 | 1.83–58.63 | 45.69–62.41 | 11–27 |
| Claude Haiku 5.5 (max) on claude-max-5x | O144 | 0.031 | 1.79–57.25 | 45.51–62.41 | 11–27 |
| Claude Haiku 5.5 (max) on claude-pro | O144 | 0.031 | 1.84–58.90 | 45.72–62.41 | 11–27 |

### Plan allowance report cells (O71, O81)

53 cells; 0 pass. A cell on a plan the Plan ranking does not list is evidence only (O85).

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
| Google | Google AI (tier unstated) (not listed) | Gemini 4 Argon | week | global | 0 of 1 | fails: 0 non-provisional report(s) in the current partition |
| Google | Google AI Pro | Gemini 4 Argon | week | global | 3 of 3 | fails: largest lower bound 1.35× the smallest upper bound (O86 allows 1.20×) in the current partition |
| Kimi | Kimi Allegretto (legacy, CN) (not listed) | Kimi K3.1 Pro | 5h | CN | 2 of 4 | fails: a 5-hour figure never converts to a billing period (O82) |
| Kimi | Kimi Allegretto (legacy, CN) (not listed) | Kimi K3.1 Pro | month | CN | 2 of 3 | fails: 1 non-provisional report(s) in the current partition |
| Kimi | Kimi Allegretto (legacy, CN) (not listed) | Kimi K3.1 Pro | week | CN | 1 of 3 | fails: 0 non-provisional report(s) in the current partition |
| Kimi | Kimi Allegro (legacy, CN) (not listed) | Kimi K3.1 Pro | 5h | CN | 1 of 5 | fails: a 5-hour figure never converts to a billing period (O82) |
| Kimi | Kimi Allegro (legacy, CN) (not listed) | Kimi K3.1 Pro | month | CN | 0 of 1 | fails: 0 non-provisional report(s) in the current partition |
| Kimi | Kimi Allegro (legacy, CN) (not listed) | Kimi K3.1 Pro | week | CN | 0 of 2 | fails: 0 non-provisional report(s) in the current partition |
| Kimi | Kimi Max (new, CN) (not listed) | Kimi K3.1 Pro | 5h | CN | 0 of 2 | fails: a 5-hour figure never converts to a billing period (O82) |
| Kimi | Kimi Max (new, CN) (not listed) | Kimi K3.1 Pro | month | CN | 0 of 1 | fails: 0 non-provisional report(s) in the current partition |
| Kimi | Kimi Plus | Kimi K3.1 Pro | 5h | global | 0 of 1 | fails: a 5-hour figure never converts to a billing period (O82) |
| Kimi | Kimi Plus (new, CN) (not listed) | Kimi K3.1 Pro | 5h | CN | 0 of 1 | fails: a 5-hour figure never converts to a billing period (O82) |
| Kimi | Kimi Pro (new, CN) (not listed) | Kimi K3.1 Pro | 5h | CN | 0 of 1 | fails: a 5-hour figure never converts to a billing period (O82) |
| Kimi | Kimi Ultra (new, CN) (not listed) | Kimi K3.1 Pro | 5h | CN | 0 of 1 | fails: a 5-hour figure never converts to a billing period (O82) |
| Kimi | Kimi legacy plan (tier not stated, CN) (not listed) | Kimi K3.1 Pro | 5h | CN | 0 of 1 | fails: a 5-hour figure never converts to a billing period (O82) |
| Kimi | Kimi ¥199 plan (legacy or new not stated, CN) (not listed) | Kimi K3.1 Pro | 5h | CN | 0 of 2 | fails: a 5-hour figure never converts to a billing period (O82) |
| MiniMax | MiniMax M Plan (tier unstated) (not listed) | MiniMax-M3.1-Flash | week | global | 0 of 1 | fails: 0 non-provisional report(s) in the current partition |
| MiniMax | MiniMax Token Plan Max (legacy) (not listed) | MiniMax-M3.1-Flash | 5h | global | 0 of 1 | fails: a 5-hour figure never converts to a billing period (O82) |
| MiniMax | MiniMax Token Plan Max (legacy) (not listed) | MiniMax-M3.1-Flash | week | global | 1 of 1 | fails: 0 non-provisional report(s) in the current partition |
| MiniMax | MiniMax Token Plan lowest tier (legacy) (not listed) | MiniMax-M3.1-Flash | 5h | global | 1 of 1 | fails: a 5-hour figure never converts to a billing period (O82) |
| MiniMax | MiniMax lowest tier ("lite") (not listed) | — | week | global | 0 of 1 | fails: 0 non-provisional report(s) in the current partition |
| OpenAI | ChatGPT (legacy account, tier unstated) (not listed) | GPT-6.1 Sol | week | global | 0 of 1 | fails: 0 non-provisional report(s) in the current partition |
| OpenAI | ChatGPT Plus | GPT-5.6 Luna | 5h | global | 0 of 1 | fails: a 5-hour figure never converts to a billing period (O82) |
| OpenAI | ChatGPT Plus | GPT-5.6 Luna | week | global | 0 of 1 | fails: 0 non-provisional report(s) in the current partition |
| OpenAI | ChatGPT Plus | GPT-6 Astra | 5h | global | 0 of 2 | fails: a 5-hour figure never converts to a billing period (O82) |
| OpenAI | ChatGPT Plus | GPT-6 Luna | 5h | global | 0 of 1 | fails: a 5-hour figure never converts to a billing period (O82) |
| OpenAI | ChatGPT Plus | GPT-6 Luna | month | global | 0 of 1 | fails: 0 non-provisional report(s) in the current partition |
| OpenAI | ChatGPT Plus | GPT-6.1 Sol | 5h | global | 1 of 3 | fails: a 5-hour figure never converts to a billing period (O82) |
| OpenAI | ChatGPT Plus | GPT-6.1 Sol | week | global | 1 of 2 | fails: 0 non-provisional report(s) in the current partition |
| OpenAI | ChatGPT Plus | GPT-6.1 Terra | 5h | global | 3 of 3 | fails: a 5-hour figure never converts to a billing period (O82) |
| OpenAI | ChatGPT Pro (tier unstated) (not listed) | GPT-6 Astra | week | global | 0 of 1 | fails: 0 non-provisional report(s) in the current partition |
| OpenAI | ChatGPT Pro 100 | GPT-6 Astra | week | global | 0 of 4 | fails: 0 non-provisional report(s) in the current partition |
| OpenAI | ChatGPT Pro 100 | GPT-6.1 Sol | week | global | 0 of 1 | fails: 0 non-provisional report(s) in the current partition |
| OpenAI | ChatGPT Pro 200 (grandfathered 20x) | GPT-6 Astra | week | global | 0 of 1 | fails: 0 non-provisional report(s) in the current partition |
| OpenAI | ChatGPT Pro 200 (grandfathered 20x) | GPT-6.1 Sol | week | global | 1 of 3 | fails: 0 non-provisional report(s) in the current partition |
| OpenAI | ChatGPT Pro 500 | GPT-6 Astra | week | global | 0 of 1 | fails: 0 non-provisional report(s) in the current partition |
| OpenAI | ChatGPT Pro 500 | GPT-6.1 Sol | week | global | 0 of 1 | fails: 0 non-provisional report(s) in the current partition |
| Xiaomi | MiMo Token Plan Lite | MiMo-V2.6-Pro | month | global | 1 of 1 | fails: 1 non-provisional report(s) in the current partition |
| Xiaomi | MiMo Token Plan Max | MiMo-V2.6-Pro | month | global | 1 of 1 | fails: 1 non-provisional report(s) in the current partition |

### Measured-only Plan view

Admission: measurement candidates of grade controlled (exact effort, or the same model at another effort, O90) or concordant reports (no owner assumption of any kind, no diagnostics). Selection: the official selector (E111, E88, E85) rerun among the admitted candidates. Panel: rows with an admitted measured candidate; others listed as 'no measured route' (no API fallback).

| Configuration | Status | Route | Plan cost | Value | Rank |
|---|---|---|---:|---:|---:|
| GPT-6.1 Sol (max) | measured, target-workload unmatched | chatgpt-pro500-gpt61sol-semianalysis | $128.76 | 71.51 | 1 |
| Claude Opus 5.5 (max) | measured, target-workload unmatched | claude-pro-opus55-semianalysis | $175.91 | 68.51 | 2 |
| GPT-6 Astra (max) | measured, target-workload unmatched | chatgpt-pro200-gpt6astra-semianalysis | $470.03 | 62.07 | 3 |
| Claude Haiku 5.5 (max) | no measured route | — | — | — | — |
| Claude Sonnet 5.5 (max) | no measured route | — | — | — | — |
| DeepSeek V4.1 Flash 1017 (max) | no measured route | — | — | — | — |
| GPT-6 Luna (max) | no measured route | — | — | — | — |
| Gemini 4 Argon (high) | no measured route | — | — | — | — |
| MiMo-V2.6-Pro | no measured route | — | — | — | — |

#### Measured-evidence calibration (diagnostic)

References: each workload's measured-only rows with complete cost evidence are the references: c_L = cheapest / 2, c_H = dearest x 2 (diagnostic only; the official anchors are unchanged). Status: evaluated.

- Workload `aad36e77d6e17386`: measured anchors $64.38 to $940.06 from GPT-6 Astra (max), GPT-6.1 Sol (max); anchor ratio 14.6 against the official 26.1. Official Plan anchors are set by GPT-6.1 Sol (max) on ChatGPT Pro 500 (controlled measurement) at the low end and GPT-6 Astra (max) on ChatGPT Plus (controlled measurement) at the high end.
- Workload `835a9baf594a1251`: measured-evidence calibration unavailable (fewer than two measured references); measured rows none. Official Plan anchors are set by GPT-6.1 Sol (max) on ChatGPT Pro 500 (controlled measurement) at the low end and GPT-6 Astra (max) on ChatGPT Plus (controlled measurement) at the high end.

| Configuration | Value on official Plan anchors | Value on measured anchors | Rank change |
|---|---:|---:|---:|
| Claude Opus 5.5 (max) | 68.51 | 66.84 | 0 |
| GPT-6 Astra (max) | 62.07 | 58.76 | 0 |
| GPT-6.1 Sol (max) | 71.51 | 70.36 | 0 |

Pairwise reversals: none. Largest value change: 3.30 points.

## Interval outputs

**API basis, main workload: frontier.** Not evaluable: Claude Opus 5.5 (max), MiMo-V2.6-Pro. Competing without a label of its own (E183): Claude Haiku 5.5 (max): AA's cost omits a pricing term (O94); competes over its published cost up to the stated factor.

| Configuration | Possible frontier | Definite frontier | Definite counterexample | Possible frontier blocked by |
|---|---|---|---|---|
| GPT-6.1 Sol (max) | certified | certified | — | — |
| Claude Sonnet 5.5 (max) | disproved | disproved | GPT-6.1 Sol (max) | GPT-6.1 Sol (max), GPT-6 Astra (max) |
| GPT-6 Astra (max) | certified | certified | — | — |
| DeepSeek V4.1 Flash 1017 (max) | certified | certified | — | — |
| Gemini 4 Argon (high) | disproved | disproved | GPT-6.1 Sol (max) | GPT-6.1 Sol (max), GPT-6 Astra (max) |
| GPT-6 Luna (max) | certified | certified | — | — | Safety-refusal flags (O63; costs and scores unchanged) on these labelled rows: GPT-6 Astra (max) (13 blocked and 0 fallback attempts of 870); GPT-6.1 Sol (max) (15 blocked and 0 fallback attempts of 870).

**API basis, main workload: cheapest at or above quality 62.1** (lower-median displayed quality of the non-provisional cohort configurations at freeze (E192; headline bar)). Status certified; confirmed cheapest: GPT-6.1 Sol (max).

Configurations that can be confirmed to qualify: 3 (confirmation needs the full-composite lower bound, with missing leaves at 0, to clear the bar; O25). Cheaper same-family configurations on AA's chart that were not evaluated (not ranked in this ranking: lacking its full benchmark set, or not plotted on or near the frontier; E201c, O51): GPT-6.1 Sol (max): GPT-6.1 Sol (xhigh), GPT-6.1 Sol (high), GPT-6.1 Sol (medium), GPT-6.1 Sol (low).

Bar comparison: compares 4 configurations that can qualify. The bar is a displayed-quality level; qualification tests each row's full-composite bounds, so a row above the bar on displayed quality can still fail to qualify confirmed when leaves are missing (E198).

| Configuration | Displayed quality − bar | Confirmed qualifies | Possibly qualifies | Possibly cheapest |
|---|---:|---|---|---|
| GPT-6.1 Sol (max) | 7.0 | certified | certified | certified |
| Claude Sonnet 5.5 (max) | 6.4 | certified | certified | disproved |
| GPT-6 Astra (max) | 7.6 | certified | certified | disproved |
| DeepSeek V4.1 Flash 1017 (max) | -4.7 | disproved | disproved | disproved |
| Gemini 4 Argon (high) | 0.0 | disproved | certified | disproved |
| GPT-6 Luna (max) | -17.1 | disproved | disproved | disproved |

**API basis, main workload: cheapest at or above quality 49.9** (lower-quartile displayed quality of the non-provisional cohort configurations at freeze (O34)). Status certified; confirmed cheapest: DeepSeek V4.1 Flash 1017 (max).

Configurations that can be confirmed to qualify: 5 (confirmation needs the full-composite lower bound, with missing leaves at 0, to clear the bar; O25). Cheaper same-family configurations on AA's chart that were not evaluated (not ranked in this ranking: lacking its full benchmark set, or not plotted on or near the frontier; E201c, O51): none.

Bar comparison: compares 5 configurations that can qualify and 1 blocker(s) that can qualify but earn no label (E315). The bar is a displayed-quality level; qualification tests each row's full-composite bounds, so a row above the bar on displayed quality can still fail to qualify confirmed when leaves are missing (E198).

| Configuration | Displayed quality − bar | Confirmed qualifies | Possibly qualifies | Possibly cheapest |
|---|---:|---|---|---|
| GPT-6.1 Sol (max) | 19.2 | certified | certified | disproved |
| Claude Sonnet 5.5 (max) | 18.6 | certified | certified | disproved |
| GPT-6 Astra (max) | 19.8 | certified | certified | disproved |
| DeepSeek V4.1 Flash 1017 (max) | 7.5 | certified | certified | certified |
| Gemini 4 Argon (high) | 12.2 | certified | certified | disproved |
| GPT-6 Luna (max) | -4.9 | disproved | disproved | disproved |

**API basis, main workload: cheapest at or above quality 68.5** (upper-quartile displayed quality of the non-provisional cohort configurations at freeze (O34)). Status certified; confirmed cheapest: GPT-6.1 Sol (max).

Configurations that can be confirmed to qualify: 2 (confirmation needs the full-composite lower bound, with missing leaves at 0, to clear the bar; O25). Cheaper same-family configurations on AA's chart that were not evaluated (not ranked in this ranking: lacking its full benchmark set, or not plotted on or near the frontier; E201c, O51): GPT-6.1 Sol (max): GPT-6.1 Sol (xhigh), GPT-6.1 Sol (high), GPT-6.1 Sol (medium), GPT-6.1 Sol (low).

Bar comparison: compares 3 configurations that can qualify. The bar is a displayed-quality level; qualification tests each row's full-composite bounds, so a row above the bar on displayed quality can still fail to qualify confirmed when leaves are missing (E198).

| Configuration | Displayed quality − bar | Confirmed qualifies | Possibly qualifies | Possibly cheapest |
|---|---:|---|---|---|
| GPT-6.1 Sol (max) | 0.6 | certified | certified | certified |
| Claude Sonnet 5.5 (max) | 0.0 | disproved | certified | disproved |
| GPT-6 Astra (max) | 1.2 | certified | certified | disproved |
| DeepSeek V4.1 Flash 1017 (max) | -11.1 | disproved | disproved | disproved |
| Gemini 4 Argon (high) | -6.4 | disproved | disproved | disproved |
| GPT-6 Luna (max) | -23.5 | disproved | disproved | disproved |

**Plan basis, main workload:** not evaluated (no row has FullCost and an identified M_W (E61/E67)).

**API basis, subset workload (AA-Briefcase, GDP.pdf, AutomationBench-AA, Terminal-Bench 4.0 (AA Index run), FrontierCode 2.0, Terminal-Bench-Science; orderings across workloads not identified): frontier.** Not evaluable: Claude Opus 5.5 (max). Competing without a label of its own (E183): Claude Haiku 5.5 (max): AA's cost omits a pricing term (O94); competes over its published cost up to the stated factor.

| Configuration | Possible frontier | Definite frontier | Definite counterexample | Possible frontier blocked by |
|---|---|---|---|---|
| GPT-6.1 Sol (max) | certified | certified | — | — |
| Claude Sonnet 5.5 (max) | disproved | disproved | GPT-6.1 Sol (max) | GPT-6.1 Sol (max), GPT-6 Astra (max) |
| GPT-6 Astra (max) | certified | certified | — | — |
| DeepSeek V4.1 Flash 1017 (max) | certified | certified | — | — |
| Gemini 4 Argon (high) | disproved | disproved | GPT-6.1 Sol (max) | GPT-6.1 Sol (max), GPT-6 Astra (max) |
| GPT-6 Luna (max) | certified | certified | — | — |
| MiMo-V2.6-Pro | certified | certified | — | — | Safety-refusal flags (O63; costs and scores unchanged) on these labelled rows: GPT-6 Astra (max) (13 blocked and 0 fallback attempts of 870); GPT-6.1 Sol (max) (15 blocked and 0 fallback attempts of 870).

**API basis, subset workload (AA-Briefcase, GDP.pdf, AutomationBench-AA, Terminal-Bench 4.0 (AA Index run), FrontierCode 2.0, Terminal-Bench-Science; orderings across workloads not identified): cheapest at or above quality 62.1** (lower-median displayed quality of the non-provisional cohort configurations at freeze (E192; headline bar)). Status certified; confirmed cheapest: GPT-6.1 Sol (max).

Configurations that can be confirmed to qualify: 3 (confirmation needs the full-composite lower bound, with missing leaves at 0, to clear the bar; O25). Cheaper same-family configurations on AA's chart that were not evaluated (not ranked in this ranking: lacking its full benchmark set, or not plotted on or near the frontier; E201c, O51): GPT-6.1 Sol (max): GPT-6.1 Sol (xhigh), GPT-6.1 Sol (high), GPT-6.1 Sol (medium), GPT-6.1 Sol (low).

Bar comparison: compares 4 configurations that can qualify. The bar is a displayed-quality level; qualification tests each row's full-composite bounds, so a row above the bar on displayed quality can still fail to qualify confirmed when leaves are missing (E198).

| Configuration | Displayed quality − bar | Confirmed qualifies | Possibly qualifies | Possibly cheapest |
|---|---:|---|---|---|
| GPT-6.1 Sol (max) | 7.0 | certified | certified | certified |
| Claude Sonnet 5.5 (max) | 6.4 | certified | certified | disproved |
| GPT-6 Astra (max) | 7.6 | certified | certified | disproved |
| DeepSeek V4.1 Flash 1017 (max) | -4.7 | disproved | disproved | disproved |
| Gemini 4 Argon (high) | 0.0 | disproved | certified | disproved |
| GPT-6 Luna (max) | -17.1 | disproved | disproved | disproved |
| MiMo-V2.6-Pro | -13.6 | disproved | disproved | disproved |

**API basis, subset workload (AA-Briefcase, GDP.pdf, AutomationBench-AA, Terminal-Bench 4.0 (AA Index run), FrontierCode 2.0, Terminal-Bench-Science; orderings across workloads not identified): cheapest at or above quality 49.9** (lower-quartile displayed quality of the non-provisional cohort configurations at freeze (O34)). Status certified; confirmed cheapest: none.

Configurations that can be confirmed to qualify: 5 (confirmation needs the full-composite lower bound, with missing leaves at 0, to clear the bar; O25). Cheaper same-family configurations on AA's chart that were not evaluated (not ranked in this ranking: lacking its full benchmark set, or not plotted on or near the frontier; E201c, O51): none.

Bar comparison: compares 5 configurations that can qualify and 1 blocker(s) that can qualify but earn no label (E315). The bar is a displayed-quality level; qualification tests each row's full-composite bounds, so a row above the bar on displayed quality can still fail to qualify confirmed when leaves are missing (E198).

| Configuration | Displayed quality − bar | Confirmed qualifies | Possibly qualifies | Possibly cheapest |
|---|---:|---|---|---|
| GPT-6.1 Sol (max) | 19.2 | certified | certified | disproved |
| Claude Sonnet 5.5 (max) | 18.6 | certified | certified | disproved |
| GPT-6 Astra (max) | 19.8 | certified | certified | disproved |
| DeepSeek V4.1 Flash 1017 (max) | 7.5 | certified | certified | certified |
| Gemini 4 Argon (high) | 12.2 | certified | certified | disproved |
| GPT-6 Luna (max) | -4.9 | disproved | disproved | disproved |
| MiMo-V2.6-Pro | -1.4 | disproved | disproved | disproved |

**API basis, subset workload (AA-Briefcase, GDP.pdf, AutomationBench-AA, Terminal-Bench 4.0 (AA Index run), FrontierCode 2.0, Terminal-Bench-Science; orderings across workloads not identified): cheapest at or above quality 68.5** (upper-quartile displayed quality of the non-provisional cohort configurations at freeze (O34)). Status certified; confirmed cheapest: GPT-6.1 Sol (max).

Configurations that can be confirmed to qualify: 2 (confirmation needs the full-composite lower bound, with missing leaves at 0, to clear the bar; O25). Cheaper same-family configurations on AA's chart that were not evaluated (not ranked in this ranking: lacking its full benchmark set, or not plotted on or near the frontier; E201c, O51): GPT-6.1 Sol (max): GPT-6.1 Sol (xhigh), GPT-6.1 Sol (high), GPT-6.1 Sol (medium), GPT-6.1 Sol (low).

Bar comparison: compares 3 configurations that can qualify. The bar is a displayed-quality level; qualification tests each row's full-composite bounds, so a row above the bar on displayed quality can still fail to qualify confirmed when leaves are missing (E198).

| Configuration | Displayed quality − bar | Confirmed qualifies | Possibly qualifies | Possibly cheapest |
|---|---:|---|---|---|
| GPT-6.1 Sol (max) | 0.6 | certified | certified | certified |
| Claude Sonnet 5.5 (max) | 0.0 | disproved | certified | disproved |
| GPT-6 Astra (max) | 1.2 | certified | certified | disproved |
| DeepSeek V4.1 Flash 1017 (max) | -11.1 | disproved | disproved | disproved |
| Gemini 4 Argon (high) | -6.4 | disproved | disproved | disproved |
| GPT-6 Luna (max) | -23.5 | disproved | disproved | disproved |
| MiMo-V2.6-Pro | -20.1 | disproved | disproved | disproved |

**Plan basis, subset workload (AA-Briefcase, GDP.pdf, AutomationBench-AA, Terminal-Bench 4.0 (AA Index run), FrontierCode 2.0, Terminal-Bench-Science; orderings across workloads not identified):** not evaluated (unevaluable: no Plan multiple is identified for a subset workload (E149, E190)).

## Scenario shares

The scenario panel is the 8 rows scored on the main workload (E96, E266); MiMo-V2.6-Pro (subset workload) are not in it and have no scenario shares, so the shares below compare the main-workload rows only.

Frequencies over 10,000 scenarios per run (seed 20261101); streams are defined in [methodology.md](methodology.md#uncertainty-outputs). S1T adds benchmark sampling noise under an independent-task approximation (O39); the other streams exclude it, and every stream excludes correlated-task, harness and attempt effects (E155).

### API basis: rank 1

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M | S1T | S1T recentred |
|---|---:|---:|---:|---:|---:|---:|---:|
| Claude Haiku 5.5 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Sonnet 5.5 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| DeepSeek V4.1 Flash 1017 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.1% | 0.1% |
| GPT-6 Astra (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Luna (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (max) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 99.9% | 99.9% |
| Gemini 4 Argon (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |

### API basis: rank 3 or better

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M | S1T | S1T recentred |
|---|---:|---:|---:|---:|---:|---:|---:|
| Claude Haiku 5.5 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 1.0% | 0.9% |
| Claude Sonnet 5.5 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 1.5% | 1.8% |
| DeepSeek V4.1 Flash 1017 (max) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 99.9% | 99.8% |
| GPT-6 Astra (max) | 100.0% | 100.0% | 92.4% | 100.0% | 100.0% | 86.1% | 87.1% |
| GPT-6 Luna (max) | 0.0% | 0.0% | 7.6% | 0.0% | 0.0% | 11.5% | 10.5% |
| GPT-6.1 Sol (max) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% |
| Gemini 4 Argon (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |

### API basis: on the frontier

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M | S1T | S1T recentred |
|---|---:|---:|---:|---:|---:|---:|---:|
| Claude Haiku 5.5 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (max) | 0.0% | 0.0% | 18.0% | 0.0% | 0.0% | 13.1% | 12.2% |
| Claude Sonnet 5.5 (max) | 0.0% | 0.0% | 3.0% | 0.0% | 0.0% | 15.4% | 14.5% |
| DeepSeek V4.1 Flash 1017 (max) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% |
| GPT-6 Astra (max) | 100.0% | 100.0% | 95.3% | 100.0% | 100.0% | 63.3% | 62.0% |
| GPT-6 Luna (max) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% |
| GPT-6.1 Sol (max) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% |
| Gemini 4 Argon (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |

### API basis: value-score dispersion (SD; covariance term)

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M | S1T | S1T recentred |
|---|---:|---:|---:|---:|---:|---:|---:|
| Claude Haiku 5.5 (max) | 0.00 (+0.00) | 0.00 (+0.00) | 1.33 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 0.98 (+0.00) | 0.98 (+0.00) |
| Claude Opus 5.5 (max) | 0.00 (+0.00) | 0.00 (+0.00) | 1.10 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 0.97 (+0.00) | 0.98 (+0.00) |
| Claude Sonnet 5.5 (max) | 0.00 (+0.00) | 0.00 (+0.00) | 1.11 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.02 (+0.00) | 1.01 (+0.00) |
| DeepSeek V4.1 Flash 1017 (max) | 0.00 (+0.00) | 0.00 (+0.00) | 1.58 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.03 (+0.00) | 1.01 (+0.00) |
| GPT-6 Astra (max) | 0.00 (+0.00) | 0.00 (+0.00) | 1.35 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.04 (+0.00) | 1.05 (+0.00) |
| GPT-6 Luna (max) | 0.00 (+0.00) | 0.00 (+0.00) | 1.47 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 0.92 (+0.00) | 0.93 (+0.00) |
| GPT-6.1 Sol (max) | 0.00 (+0.00) | 0.00 (+0.00) | 1.51 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.08 (+0.00) | 1.06 (+0.00) |
| Gemini 4 Argon (high) | 0.00 (+0.00) | 0.00 (+0.00) | 1.48 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 0.97 (+0.00) | 0.96 (+0.00) |

Plan streams S1, S2, S1 endpoint-heavy, S1M, S1T and S1T recentred run with owner assumptions off (owner-named transfers and O46 provider quota ceilings; E167): Claude Haiku 5.5 (max) on Claude Max 20x, Claude Haiku 5.5 (max) on Claude Max 5x, Claude Haiku 5.5 (max) on Claude Pro, Claude Sonnet 5.5 (max) on Claude Max 20x, Claude Sonnet 5.5 (max) on Claude Max 5x, Claude Sonnet 5.5 (max) on Claude Pro, GPT-6 Luna (max) on ChatGPT Plus, GPT-6 Luna (max) on ChatGPT Pro 100, GPT-6 Luna (max) on ChatGPT Pro 200, GPT-6 Luna (max) on ChatGPT Pro 500 depend on an owner assumption and are unevaluable there (—), never reselected or replaced by API cost.

### Plan basis: rank 1

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M | S1T | S1T recentred |
|---|---:|---:|---:|---:|---:|---:|---:|
| Claude Haiku 5.5 (max) on Claude Max 20x | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (max) on Claude Max 5x | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (max) on Claude Pro | 0.0% | — | — | — | — | — | — |
| Claude Opus 5.5 (max) on Claude Max 20x | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (max) on Claude Max 5x | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (max) on Claude Pro | 0.0% | 0.0% | 0.2% | 0.0% | 0.0% | 2.2% | 1.8% |
| Claude Sonnet 5.5 (max) on Claude Max 20x | 0.0% | — | — | — | — | — | — |
| Claude Sonnet 5.5 (max) on Claude Max 5x | 0.0% | — | — | — | — | — | — |
| Claude Sonnet 5.5 (max) on Claude Pro | 0.0% | — | — | — | — | — | — |
| DeepSeek V4.1 Flash 1017 (max) on API-cost fallback | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (max) on ChatGPT Plus | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (max) on ChatGPT Pro 100 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (max) on ChatGPT Pro 200 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (max) on ChatGPT Pro 500 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Luna (max) on ChatGPT Plus | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 500 | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Sol (max) on ChatGPT Plus | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (max) on ChatGPT Pro 100 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (max) on ChatGPT Pro 200 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (max) on ChatGPT Pro 500 | 100.0% | 100.0% | 99.8% | 100.0% | 100.0% | 97.8% | 98.2% |
| Gemini 4 Argon (high) on API-cost fallback | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |

### Plan basis: rank 3 or better

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M | S1T | S1T recentred |
|---|---:|---:|---:|---:|---:|---:|---:|
| Claude Haiku 5.5 (max) on Claude Max 20x | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (max) on Claude Max 5x | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (max) on Claude Pro | 0.0% | — | — | — | — | — | — |
| Claude Opus 5.5 (max) on Claude Max 20x | 0.0% | 0.0% | 0.2% | 0.0% | 0.0% | 2.6% | 2.2% |
| Claude Opus 5.5 (max) on Claude Max 5x | 0.0% | 0.0% | 0.1% | 0.0% | 0.0% | 1.6% | 1.3% |
| Claude Opus 5.5 (max) on Claude Pro | 0.0% | 0.0% | 0.3% | 0.0% | 0.0% | 2.7% | 2.3% |
| Claude Sonnet 5.5 (max) on Claude Max 20x | 0.0% | — | — | — | — | — | — |
| Claude Sonnet 5.5 (max) on Claude Max 5x | 0.0% | — | — | — | — | — | — |
| Claude Sonnet 5.5 (max) on Claude Pro | 0.0% | — | — | — | — | — | — |
| DeepSeek V4.1 Flash 1017 (max) on API-cost fallback | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (max) on ChatGPT Plus | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (max) on ChatGPT Pro 100 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (max) on ChatGPT Pro 200 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (max) on ChatGPT Pro 500 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Luna (max) on ChatGPT Plus | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 500 | 0.0% | — | — | — | — | — | — |
| GPT-6.1 Sol (max) on ChatGPT Plus | 100.0% | 100.0% | 99.8% | 100.0% | 100.0% | 97.4% | 97.8% |
| GPT-6.1 Sol (max) on ChatGPT Pro 100 | 100.0% | 100.0% | 99.8% | 100.0% | 100.0% | 97.4% | 97.8% |
| GPT-6.1 Sol (max) on ChatGPT Pro 200 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (max) on ChatGPT Pro 500 | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 98.4% | 98.7% |
| Gemini 4 Argon (high) on API-cost fallback | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |

### Plan basis: on the frontier

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M | S1T | S1T recentred |
|---|---:|---:|---:|---:|---:|---:|---:|
| Claude Haiku 5.5 (max) on Claude Max 20x | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (max) on Claude Max 5x | 0.0% | — | — | — | — | — | — |
| Claude Haiku 5.5 (max) on Claude Pro | 100.0% | — | — | — | — | — | — |
| Claude Opus 5.5 (max) on Claude Max 20x | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (max) on Claude Max 5x | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (max) on Claude Pro | 0.0% | 0.0% | 36.5% | 0.0% | 0.0% | 34.0% | 33.1% |
| Claude Sonnet 5.5 (max) on Claude Max 20x | 0.0% | — | — | — | — | — | — |
| Claude Sonnet 5.5 (max) on Claude Max 5x | 0.0% | — | — | — | — | — | — |
| Claude Sonnet 5.5 (max) on Claude Pro | 0.0% | — | — | — | — | — | — |
| DeepSeek V4.1 Flash 1017 (max) on API-cost fallback | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (max) on ChatGPT Plus | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (max) on ChatGPT Pro 100 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (max) on ChatGPT Pro 200 | 100.0% | 100.0% | 78.1% | 100.0% | 100.0% | 54.6% | 54.2% |
| GPT-6 Astra (max) on ChatGPT Pro 500 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Luna (max) on ChatGPT Plus | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 500 | 100.0% | — | — | — | — | — | — |
| GPT-6.1 Sol (max) on ChatGPT Plus | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (max) on ChatGPT Pro 100 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (max) on ChatGPT Pro 200 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (max) on ChatGPT Pro 500 | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% |
| Gemini 4 Argon (high) on API-cost fallback | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |

### Plan basis: value-score dispersion (SD; covariance term)

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M | S1T | S1T recentred |
|---|---:|---:|---:|---:|---:|---:|---:|
| Claude Haiku 5.5 (max) on Claude Max 20x | 0.00 (+0.00) | — | — | — | — | — | — |
| Claude Haiku 5.5 (max) on Claude Max 5x | 0.00 (+0.00) | — | — | — | — | — | — |
| Claude Haiku 5.5 (max) on Claude Pro | 0.00 (+0.00) | — | — | — | — | — | — |
| Claude Opus 5.5 (max) on Claude Max 20x | 0.00 (+0.00) | 0.00 (+0.00) | 1.11 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 0.98 (+0.00) | 0.97 (+0.00) |
| Claude Opus 5.5 (max) on Claude Max 5x | 0.00 (+0.00) | 0.00 (+0.00) | 1.11 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 0.98 (+0.00) | 0.97 (+0.00) |
| Claude Opus 5.5 (max) on Claude Pro | 0.00 (+0.00) | 0.00 (+0.00) | 1.11 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 0.98 (+0.00) | 0.97 (+0.00) |
| Claude Sonnet 5.5 (max) on Claude Max 20x | 0.00 (+0.00) | — | — | — | — | — | — |
| Claude Sonnet 5.5 (max) on Claude Max 5x | 0.00 (+0.00) | — | — | — | — | — | — |
| Claude Sonnet 5.5 (max) on Claude Pro | 0.00 (+0.00) | — | — | — | — | — | — |
| DeepSeek V4.1 Flash 1017 (max) on API-cost fallback | 0.00 (+0.00) | 0.00 (+0.00) | 1.56 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.02 (+0.00) | 1.04 (+0.00) |
| GPT-6 Astra (max) on ChatGPT Plus | 0.00 (+0.00) | 0.00 (+0.00) | 1.34 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.04 (+0.00) | 1.05 (+0.00) |
| GPT-6 Astra (max) on ChatGPT Pro 100 | 0.00 (+0.00) | 0.00 (+0.00) | 1.34 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.04 (+0.00) | 1.05 (+0.00) |
| GPT-6 Astra (max) on ChatGPT Pro 200 | 0.00 (+0.00) | 0.00 (+0.00) | 1.34 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.04 (+0.00) | 1.05 (+0.00) |
| GPT-6 Astra (max) on ChatGPT Pro 500 | 0.00 (+0.00) | 0.00 (+0.00) | 1.34 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.04 (+0.00) | 1.05 (+0.00) |
| GPT-6 Luna (max) on ChatGPT Plus | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 100 | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 200 | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 500 | 0.00 (+0.00) | — | — | — | — | — | — |
| GPT-6.1 Sol (max) on ChatGPT Plus | 0.00 (+0.00) | 0.00 (+0.00) | 1.49 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.08 (+0.00) | 1.06 (+0.00) |
| GPT-6.1 Sol (max) on ChatGPT Pro 100 | 0.00 (+0.00) | 0.00 (+0.00) | 1.49 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.08 (+0.00) | 1.06 (+0.00) |
| GPT-6.1 Sol (max) on ChatGPT Pro 200 | 0.00 (+0.00) | 0.00 (+0.00) | 1.49 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.08 (+0.00) | 1.06 (+0.00) |
| GPT-6.1 Sol (max) on ChatGPT Pro 500 | 0.00 (+0.00) | 0.00 (+0.00) | 1.49 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.08 (+0.00) | 1.06 (+0.00) |
| Gemini 4 Argon (high) on API-cost fallback | 0.00 (+0.00) | 0.00 (+0.00) | 1.48 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 0.97 (+0.00) | 0.96 (+0.00) |

### Named S2 specification branches

- **Bug Hunt harness band (E19)** (S2): unevaluable; the captured tbench.ai leaderboard lists no configuration under two or more agents, so no cross-agent spread exists
- **cache-hit variation (E34)** (S2): unevaluable; AA's published cost embeds its cache-pricing protocol; varying the cache-hit rate needs each basket component's cache-read and uncached-input demand, which AA publishes only for the whole Index (E157)
- **first-party list versus cross-provider median price rule (E122)** (S2): unevaluable; AA publishes one price per configuration under its own rule; the alternative rule's prices are not captured

### Cheapest-above-the-bar labels (API basis)

The 90% rule's error bound holds per published event (candidate and kernel assignment); it is not corrected across the listed candidates (E198). Each kernel assignment code gives the kernel used for the candidate and the competitors, in that order (U uniform, H endpoint-heavy; a quality-level bar has no reference rows, so it takes no letter); the label needs every assignment met.

| Bar | Candidate | Reading | Frequency range | Kernel assignments | Label |
|---|---|---|---|---|---|
| quality 62.1 | GPT-6.1 Sol (max) | supported under all registered role-group kernel checks | 100.0% to 100.0% | UU met, UH met, HU met, HH met | yes |
| quality 49.9 | DeepSeek V4.1 Flash 1017 (max) | supported under all registered role-group kernel checks | 100.0% to 100.0% | UU met, UH met, HU met, HH met | yes |
| quality 68.5 | GPT-6.1 Sol (max) | supported under all registered role-group kernel checks | 100.0% to 100.0% | UU met, UH met, HU met, HH met | yes | Safety-refusal flags (O63; costs and scores unchanged) on these labelled rows: GPT-6.1 Sol (max) (15 blocked and 0 fallback attempts of 870).

## Diagnostics

- **Terminal-Bench cross-source agreement (AA's mini-SWE-agent run against tbench.ai):** defined; 0 rows take the leaf from tbench.ai (gap fill).
- **Workload cross-check (E41, mandatory diagnostic):** Terminal-Bench 4.0 cost per solved task on AA's own execution against basket cost: τ_b 0.86 (interval 0.48 to 1.00), uncertain agreement; panel (8): Claude Haiku 5.5 (max), Claude Opus 5.5 (max), Claude Sonnet 5.5 (max), DeepSeek V4.1 Flash 1017 (max), Gemini 4 Argon (high), GPT-6 Astra (max), GPT-6 Luna (max), GPT-6.1 Sol (max).
- **Rank separability (O39, independent-task approximation):** median separation 2.74 value points (API) and 2.77 (Plan); separable adjacent ranks: API 2 of 6, Plan 1 of 8. Assumptions: tasks are independent and each leaf's score is a mean over its published task count (a binomial leaf drawn from its Jeffreys posterior Beta(k + 1/2, n - k + 1/2), O142; plug-in SDs with the proportion (k + 1/2) / (n + 1), I28); attempts averaged within a task and tasks shared across models are ignored, so the noise is approximate; GDPval-AA: each row's rating interval as AA's model page displays it, read as a 95% normal interval (AA states no level), SD = half-width / 1.96; AA-Omniscience: each of 3,000 questions scores +1, 0 or -1, with the shares from AA's accuracy and hallucination rate; Vals boards (Vibe Code Bench v1.1, Code Migration v1.1): Vals' published standard error per record, read as the leaf's SD; AI Coding Daily: judged points over its six graded projects read as a binomial share of 60 points (an assumption; the board publishes no error).
- **FrontierCode against Cognition:** FrontierCode 2.0 cross-source agreement (AA against Cognition, exact model and effort; E234, O153): Kendall tau 0.91 (interval 0.83 to 0.97) on 26 rows. Cognition minus AA: mean -1.5 points, largest 7.7.
- **Gap-fill removal (E234, diagnostic):** no ranked row has a leaf from another party or the provider.
- **Bar results without the gap fills (E234, sensitivity; labels unchanged):** cheapest displayed row as published, with fills removed, and with third-party fills third-party fills minus the signed mean offset -1.5 points (third party minus AA) — API quality 62.1: GPT-6.1 Sol (max) in all three; API quality 49.9: DeepSeek V4.1 Flash 1017 (max) in all three; API quality 68.5: GPT-6.1 Sol (max) in all three; Plan quality 62.1: GPT-6.1 Sol (max) in all three; Plan quality 49.9: Claude Haiku 5.5 (max) in all three; Plan quality 68.5: GPT-6.1 Sol (max) in all three.
- **Harness cost (O123, S2 stress):** unevaluable: no model is listed under two or more agents in AA's Coding Agent Index capture, so no agent effect is identified (O123). Coding Agent Index agents (each part of its costed configuration; none is the run behind the FrontierCode or Terminal-Bench leaf): GPT-6.1 Sol (max): Codex; Claude Opus 5.5 (max): Claude Code; Claude Sonnet 5.5 (max): Claude Code; GPT-6 Astra (max): Codex; DeepSeek V4.1 Flash 1017 (max): DeepSeek Harness; Gemini 4 Argon (high): Antigravity CLI; Claude Haiku 5.5 (max): Claude Code; GPT-6 Luna (max): Codex.
- **Quality agreement:** quality agreement (matched-panel sensitivity): Kendall tau 0.78 (interval 0.45 to 1.00) on 9 rows.
- **Quality-substitution value agreement (API):** quality-substitution value agreement, api basis (matched-panel sensitivity): Kendall tau 0.83 (interval 0.31 to 1.00) on 9 rows.
- **Quality-substitution value agreement (Plan):** quality-substitution value agreement, plan basis (matched-panel sensitivity): Kendall tau 0.83 (interval 0.45 to 1.00) on 9 rows.
- **Disjoint-evidence agreement:** disjoint-evidence agreement (restricted evidence comparison, not an eligible ranking): Kendall tau 0.50 (interval -0.10 to 0.93) on 9 rows.
- **Quality source shares:** AA-run 66%, independent 34%.
- **Non-discriminating leaves:** lcr.
- **Group drift:** estimated; flagged: knowledge.
- **Omniscience abstention sensitivity** (z_pen = max(0, I)): 5 rows move; largest move 2 (Claude Opus 5.5 (max)).
- **GDPval-AA logistic sensitivity** (z = 100 / (1 + 10^((1600 - E) / 400)) against AA's pinned anchor; every other input fixed): API 3 rows move; largest move 2 (GPT-6 Luna (max)); Plan no rank changes.
- **Anchor stability:** trimmed anchors (P10 / 2 and P90 x 2 (diagnostic only)) give $172.61 to $19,382.74; 2 rows move; largest move 1 (GPT-6 Astra (max), GPT-6 Luna (max)).

- **Basket readiness (E22):** priced leaves cover 38% of nominal quality weight (AutomationBench-AA, FrontierCode 2.0, Terminal-Bench-Science 0.1, Terminal-Bench 4.0 (AA run)); pending components: ITBench-AA.
- **SWE cost companion (O14, diagnostic):** 8 rows evaluated; flagged far from the median ratio: Claude Haiku 5.5 (max).
- **Matched-cost diagnostic (E55):** evaluated at 51% priced quality weight; basket/matched cost-order reversals with separated intervals: 2; rank-gap warnings: 0.
- **Frontier-families anchors (E187, diagnostic):** anchors rebuilt from the 4 frontier and near-frontier references move API no rank changes (value points per cost doubling 3.11 vs 3.11 frozen); Plan no rank changes (value points per cost doubling 6.46 vs 5.31 frozen).
- **Frontier-families bar (E199, sensitivity; the frozen bar stays primary):** quality 68.5 over 5 configurations; cheapest at or above it on the API main workload: GPT-6.1 Sol (max) (confirmed) (compares 3 configurations that can qualify).
- **One row per family (E205, diagnostic; the frozen ladder and anchors stay primary):** with each family's primary configuration only (2 rows in the one-row-per-family bar population), the ladder (headline, lower quartile, upper quartile) would be 68.5 against 62.1 / 49.9 / 68.5 frozen; anchors rebuilt from its 2 references move API 4 rows move; largest move 3 (Claude Haiku 5.5 (max)) (value points per cost doubling 5.08 vs 3.11 frozen); Plan anchors unavailable: fewer than 2 measured references (O157).
- **Ladder over scored rows (I28, sensitivity; the frozen ladder stays primary):** the bar population keeps full-benchmark rows that have no cost; today every such row has a cost, so the ladder is unchanged.
- **Bar currency (E207, informational):** rows reaching each frozen bar: quality 62.1: 5 of 9; quality 49.9: 7 of 9; quality 68.5: 3 of 9; the current population would freeze 62.1 / 49.9 / 68.5; lifetime until the next anchor re-freeze or methodology version, whichever comes first; no staleness flag.
- **Token mix (E208):** 1 selected routes: mix not reported: the measurement publishes no token-category shares; 6 selected routes: mix unidentified: the basket's token-category shares are set-identified only (E124), so the L1 test (above 0.30 flags mix-unmatched) is not computed.
- **Observed-range sensitivity (E219, not evidence; no label changes):** with each missing leaf inside the cohort's observed range for that leaf, quality 62.1: 4 can qualify, 3 confirmed; GPT-6.1 Sol (max) confirmed cheapest; quality 49.9: 5 can qualify, 5 confirmed; DeepSeek V4.1 Flash 1017 (max) confirmed cheapest; quality 68.5: 3 can qualify, 2 confirmed; GPT-6.1 Sol (max) confirmed cheapest.
- **What would settle the headline bar (E221, not a claim):** rows that can but need not reach quality 62.1, with the mean score their missing leaves would need: Gemini 4 Argon (high) (no missing leaf; reporting precision only).
- **Common leaf set (E226, diagnostic; scores unchanged):** without the leaves fewer than 90% of cohort rows have (none), API no rank changes; Plan no rank changes; rows reaching each bar: quality 62.1: 5 → 5; quality 49.9: 7 → 7; quality 68.5: 3 → 3; rows whose displayed quality differs from common-leaf quality by more than one cost doubling's worth: none.
- **Harness by leaf (E227):** Terminal-Bench: mini-SWE-agent 9; Bug Hunt: Claude Code 3, Codex CLI 3, Antigravity CLI 1, Claude Code / Xiaomi first-party 1, DeepSeek Harness / DeepSeek API 1.
- **Coding Agent Index safety refusals (O63, flagged; costs and scores unchanged):** GPT-6.1 Sol (max) (15 blocked of 870 attempts); Claude Opus 5.5 (max) (76 finished by Claude Opus 4.8 or Claude Opus 5 of 870 attempts); Claude Sonnet 5.5 (45 finished by Claude Opus 4.8 of 870 attempts); GPT-6 Astra (max) (13 blocked of 870 attempts); Claude Haiku 5.5 (max) (3 finished by Claude Opus 5 of 870 attempts).

### Leave-one-component-out cost family (E172)

Each admitted basket unit removed in turn, scored on anchors rebuilt by the freeze rule (rank changes against the primary ranking; quality held fixed).

| Removed component | API rank changes | Plan rank changes | API value points per cost doubling |
|---|---|---|---:|
| Coding Agent Index | 3 rows move; largest move 2 (Claude Haiku 5.5 (max)) | 2 rows move; largest move 1 (GPT-6 Astra (max), GPT-6 Luna (max)) | 3.17 |
| AA-Briefcase | no rank changes | 4 rows move; largest move 1 (Claude Opus 5.5 (max), Claude Sonnet 5.5 (max), GPT-6 Astra (max), GPT-6 Luna (max)) | 3.16 |
| GDP.pdf | no rank changes | 2 rows move; largest move 1 (Claude Opus 5.5 (max), Claude Sonnet 5.5 (max)) | 3.10 |
| AutomationBench-AA | 2 rows move; largest move 1 (Claude Haiku 5.5 (max), Gemini 4 Argon (high)) | 2 rows move; largest move 1 (Claude Opus 5.5 (max), Claude Sonnet 5.5 (max)) | 3.05 |
| Terminal-Bench 4.0 (AA Index run) | no rank changes | 2 rows move; largest move 1 (GPT-6 Astra (max), GPT-6 Luna (max)) | 3.10 |
| FrontierCode 2.0 | 4 rows move; largest move 1 (Claude Haiku 5.5 (max), Claude Opus 5.5 (max), Claude Sonnet 5.5 (max), Gemini 4 Argon (high)) | 2 rows move; largest move 1 (Claude Opus 5.5 (max), Claude Sonnet 5.5 (max)) | 3.11 |
| Terminal-Bench-Science | 2 rows move; largest move 1 (Claude Haiku 5.5 (max), Gemini 4 Argon (high)) | no rank changes | 3.08 |

### Subset rows: paired bridge and missing spend (E10, E173)

- **MiMo-V2.6-Pro** (subset without Coding Agent Index): Coding Agent Index is 32% of the full basket (median; 16% to 74% over 8 rows). Scored on its own subset anchors, the direction of its subset effect is not known. Paired bridge on the 8 full rows: API: the full rows' values change by -0.09 points (median; -0.94 to 4.38), 3 rows move; largest move 2 (Claude Haiku 5.5 (max)); Plan: the full rows' values change by 0.00 points (median; -1.43 to 0.66), no rank changes.

### Deletion sensitivity

| Branch | Retained nominal weight | Status | API rank changes | Plan rank changes |
|---|---:|---|---|---|
| leave-out:frontierCode | 85% | evaluated | 2 rows move; largest move 1 (Claude Haiku 5.5 (max), Gemini 4 Argon (high)) | 4 rows move; largest move 1 (Claude Haiku 5.5 (max), DeepSeek V4.1 Flash 1017 (max), GPT-6 Astra (max), MiMo-V2.6-Pro) |
| leave-out:terminalBench | 89% | evaluated | 5 rows move; largest move 2 (GPT-6 Luna (max)) | 4 rows move; largest move 1 (Claude Opus 5.5 (max), Claude Sonnet 5.5 (max), DeepSeek V4.1 Flash 1017 (max), MiMo-V2.6-Pro) |
| leave-out:bugHunt | 92% | evaluated | 6 rows move; largest move 3 (GPT-6 Astra (max)) | 3 rows move; largest move 2 (Claude Opus 5.5 (max)) |
| leave-out:vibeCode | 95% | evaluated | 2 rows move; largest move 1 (Claude Haiku 5.5 (max), Gemini 4 Argon (high)) | 2 rows move; largest move 1 (Claude Haiku 5.5 (max), GPT-6 Astra (max)) |
| leave-out:codeMigration | 94% | evaluated | 2 rows move; largest move 1 (Claude Opus 5.5 (max), Claude Sonnet 5.5 (max)) | 2 rows move; largest move 1 (Claude Opus 5.5 (max), Claude Sonnet 5.5 (max)) |
| leave-out:livebench2Overall | 85% | evaluated | no rank changes | 4 rows move; largest move 1 (Claude Haiku 5.5 (max), DeepSeek V4.1 Flash 1017 (max), GPT-6 Astra (max), MiMo-V2.6-Pro) |
| leave-out:gdpval | 90% | evaluated | 4 rows move; largest move 1 (Claude Haiku 5.5 (max), Gemini 4 Argon (high), GPT-6 Luna (max), MiMo-V2.6-Pro) | 4 rows move; largest move 1 (Claude Haiku 5.5 (max), DeepSeek V4.1 Flash 1017 (max), GPT-6 Astra (max), MiMo-V2.6-Pro) |
| leave-out:automationBench | 90% | evaluated | 2 rows move; largest move 1 (Claude Opus 5.5 (max), Claude Sonnet 5.5 (max)) | 2 rows move; largest move 1 (Claude Opus 5.5 (max), Claude Sonnet 5.5 (max)) |
| leave-out:omniscience | 90% | evaluated | no rank changes | 4 rows move; largest move 1 (Claude Haiku 5.5 (max), DeepSeek V4.1 Flash 1017 (max), GPT-6 Astra (max), MiMo-V2.6-Pro) |
| leave-out:lcr | 95% | evaluated | 2 rows move; largest move 1 (Claude Haiku 5.5 (max), Gemini 4 Argon (high)) | 4 rows move; largest move 1 (Claude Haiku 5.5 (max), DeepSeek V4.1 Flash 1017 (max), GPT-6 Astra (max), MiMo-V2.6-Pro) |
| leave-out:hle | 98% | evaluated | no rank changes | no rank changes |
| leave-out:tbScience | 98% | evaluated | no rank changes | no rank changes |
| leave-out:critpt | 98% | evaluated | no rank changes | no rank changes |
| leave-source-out:Artificial Analysis | 34% | not identifiable under the coverage rule | — | — |
| leave-source-out:Vals AI | 89% | evaluated | 2 rows move; largest move 1 (Claude Opus 5.5 (max), Claude Sonnet 5.5 (max)) | 4 rows move; largest move 1 (Claude Haiku 5.5 (max), Claude Opus 5.5 (max), Claude Sonnet 5.5 (max), GPT-6 Astra (max)) |
| basket-scope | 87% | evaluated | no rank changes | 2 rows move; largest move 1 (DeepSeek V4.1 Flash 1017 (max), MiMo-V2.6-Pro) |

### Cost-component removal (Terminal-Bench 4.0 (AA Index run): evaluated)

| Basis | Run | Rank changes |
|---|---|---|
| api | cost-component removal, original anchors | no rank changes |
| api | alternative workload, recalibrated anchors | no rank changes |
| plan | cost-component removal, original anchors; fixed-multiple arithmetic stress (not identified Plan economics for the altered workload) | 2 rows move; largest move 1 (Claude Haiku 5.5 (max), GPT-6 Astra (max)) |
| plan | alternative workload, recalibrated anchors; fixed-multiple arithmetic stress (not identified Plan economics for the altered workload) | 2 rows move; largest move 1 (GPT-6 Astra (max), GPT-6 Luna (max)) |

## Release gates

| Rule | Status | Detail |
|---|---|---|
| clip gate (E20) | passed | no basis exceeds the clipping allowance |
| cost influence flag (E91) | passed | cost not discriminating (< 10%); informational only; beta never changes (O2) |
| realised influence (E272) | passed | cost's value-variance allocation lies within 0-100% on both bases |
| quality influence flag (E126) | passed | quality not discriminating (cost share > 90%); informational only |
| subset scoring (O17) | fired | subset rows scored on their own workload and anchors |
| partial component flag (E37) | fired | AA declined- or missing-task markers, or an Index reconstruction that misses AA's total (E209) |
| route dominance filter (E88) | vacuous | certifiably dearer routes set aside |
| Plan exploratory label (E61) | fired | fewer than half of Plan rows have an identified M_W |
| Plan evidence lifecycle and change detection (E18, E151, E269, O77, O79) | fired | 21 of 27 plan rows carry a possibly-superseded or expired route: claude-haiku-5-5-max@claude-max-20x, claude-haiku-5-5-max@claude-max-5x, claude-haiku-5-5-max@claude-pro, claude-opus-5-5@claude-max-20x, claude-opus-5-5@claude-max-5x, claude-opus-5-5@claude-pro, claude-sonnet-5-5@claude-max-20x, claude-sonnet-5-5@claude-max-5x, claude-sonnet-5-5@claude-pro, gpt-6-astra@chatgpt-plus, gpt-6-astra@chatgpt-pro-100, gpt-6-astra@chatgpt-pro-200, gpt-6-astra@chatgpt-pro-500, gpt-6-luna@chatgpt-plus, gpt-6-luna@chatgpt-pro-100, gpt-6-luna@chatgpt-pro-200, gpt-6-luna@chatgpt-pro-500, gpt-6.1-sol@chatgpt-plus, gpt-6.1-sol@chatgpt-pro-100, gpt-6.1-sol@chatgpt-pro-200, gpt-6.1-sol@chatgpt-pro-500 |
| acknowledged accounting-fault windows (O91, O92, O93, O95, O96) | fired | 3 of 27 plan rows rest on a measurement inside an acknowledged fault window; they stay selected and yield to two concordant user reports for their own model and plan, and the transfers resting on them follow: gpt-6-astra@chatgpt-pro-500, gpt-6-luna@chatgpt-pro-500, gpt-6.1-sol@chatgpt-pro-500 |
| AA cost omits a pricing term (O94, O98, O100, O106, O108, O109, O114) | fired | ranked at the published cost; compete in interval outputs and the scenario labels' BlockerSafe test over [C, factor × C] ([C, ∞) without a stated factor, O98) without a label (scenario frequencies draw them at the published cost, O114), and leave the anchor population at the next freeze: claude-haiku-5-5-max (up to 5×) |
| valuation-basis gate (E170) | passed | every ranked row is compatible as captured or after evidenced revaluation |
| source clocks and evidence freshness (O59, O60, O65, E211, E216, E217, E218) | passed | every capture is within its age gate and none after the cutoff unless its source predates the cutoff's day; the build stops otherwise |
| build-stopping evidence gates (O64, O69, O71, O75, O99, O100, O101, O103, O105-O111, E195, E204, E225) | passed | the Coding Agent Index manifest (O64), the Terminal-Bench agent list (E225), cutoff-day row dates (O69), the three-stage all-provider plan search (O71, O75), the typed change records behind every route flag and partition split, which also produce each route's label and blocking dates within its launch- and schedule-bounded span (O99, O101, O105, O107, O110, O111), the register of AA notes covering every captured one, with the chart's inventory and duplicate-entry checks, the post-O103 capture notes, the basket-chart labels and chart-level notes' named rows (O100, O103, O106, O108) and the frontier path checks (E195, E204) hold; the build stops otherwise |
| score swing gate (E177) | vacuous | first v3 release: no previous v3 release to compare |
| ranking coverage (O166) | vacuous | ranks 9 of 37 cohort configurations; first v3 release: no previous v3 release to compare |
| anchor migration (E184) | vacuous | no main-workload migration deferred |
| frozen admission (O169) | vacuous | every frozen component still meets the admission threshold |
| configuration map coverage | passed | every cohort row has a configuration-map entry |
| quality clipping audit (E110) | passed | saturation disclosed; domain violations block the build |
| full benchmark set (O36, O38) | fired | listed, not ranked: gpt-6.1-terra, gpt-6.1-sol-high, gpt-6.1-sol-medium, claude-opus-5-5-high, kimi-k3-1-pro, gpt-6-astra-high, claude-opus-5-5-medium, gpt-6.1-sol-low, gpt-6.1-terra-xhigh, gpt-6.1-terra-high, claude-haiku-5-5-high, gpt-6.1-terra-medium, claude-haiku-5-5-medium, gpt-6-luna-xhigh, gpt-6-luna-high, gpt-6-luna-medium, claude-haiku-5-5-low, claude-haiku-5-5, claude-opus-5-5-xhigh, claude-sonnet-5-5-xhigh, gpt-5.6-luna-low, gpt-6-astra-xhigh, gpt-6-luna-low, gpt-6.1-sol-xhigh, gpt-6.1-terra-low, gemini-4-carbon, mimo-v2-6-flash, minimax-m3-1-flash |
| missing-leaf rules (O8 provisional, E198b, E201b, E219, E221, E226) | vacuous | no ranked row has a missing leaf (O36) |
| S1M interval stream (E145) | vacuous | dormant: no ranked leaf carries a published confidence interval since O37, so S1M equals S1 (E236) |
| provider-claim label denial (E233) | vacuous | no row has a provider-claimed leaf |
| scenario outputs current (E72) | passed | scenario input hash matches the scored inputs |
