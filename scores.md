# ValueRank v3.0.0 Scores

**Updated:** October 19, 2026 · methodology 3.0.0 · SDLC basket v1 · anchor version `v3-2026-10-25`

Value = 25% × cost score + 75% × quality. Costs are USD per basket run; the cost score is log-scaled against the frozen anchors of the row's workload (see [methodology.md](methodology.md)).

## Ranking

| Configuration | Plan rank | Plan value | Plan cost score | API rank | API value | API cost score | Quality | Quality coverage | Workload |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| [Claude Opus 5.5 (max)](https://valuerank.alolabs.dev/models/claude-opus-5-5/) | 1 | 64.16 | 53.51 | 6 | 53.83 | 12.17 | 67.71 | 100% | main |
| [Claude Sonnet 5.5 (max)](https://valuerank.alolabs.dev/models/claude-sonnet-5-5/) | 4 | 63.56 | 54.16 | 8 | 53.26 | 12.98 | 66.69 | 100% | main |
| [GPT-6.1 Sol (max)](https://valuerank.alolabs.dev/models/gpt-6-1-sol/) | 7 | 62.61 | 58.11 | 1 | 60.02 | 47.74 | 64.11 | 100% | main |
| [Claude Haiku 5.5 (max)](https://valuerank.alolabs.dev/models/claude-haiku-5-5-max/) | 11 | 59.19 | 85.44 | 9 | 50.83 | 52.01 | 50.44 | 100% | main |
| [GPT-6 Astra (max)](https://valuerank.alolabs.dev/models/gpt-6-astra/) | 14 | 58.78 | 40.29 | 7 | 53.78 | 20.30 | 64.94 | 100% | main |
| [GPT-6 Luna (max)](https://valuerank.alolabs.dev/models/gpt-6-luna/) | 17 | 57.59 | 90.25 | 4 | 56.98 | 87.83 | 46.70 | 100% | main |
| [DeepSeek V4.1 Flash 1017 (max)](https://valuerank.alolabs.dev/models/deepseek-v4-1-flash-1017/) | 22 | 53.08 | 40.16 | 2 | 59.80 | 67.07 | 57.38 | 100% | main |
| [MiMo-V2.6-Pro](https://valuerank.alolabs.dev/models/mimo-v2-6-pro/) | 23 | 51.18 | 44.90 | 3 | 59.57 | 78.48 | 53.27 | 100% | subset |
| [Gemini 4 Argon (high)](https://valuerank.alolabs.dev/models/gemini-4-argon/) | 27 | 50.09 | 9.75 | 5 | 54.94 | 29.14 | 63.54 | 100% | main |

## Not ranked

| Model | Reasons |
|---|---|
| Claude Fable 5 | Not plotted on or within the near gap of AA's rendered frontier (O51) |
| Claude Fable 5.1 | Not plotted on or within the near gap of AA's rendered frontier (O51) |
| Claude Haiku 5.5 | Incomplete benchmark evidence after an exhaustive search (O36, O53): Max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall; AI Coding Daily ranking: no AI Coding Daily (excl. bug finding) |
| Claude Haiku 5.5 (high) | Not in the max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall; ranked in the AI Coding Daily ranking, common-leaf diagnostic ranking |
| Claude Haiku 5.5 (low) | Incomplete benchmark evidence after an exhaustive search (O36, O53): Max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall; AI Coding Daily ranking: no AI Coding Daily (excl. bug finding) |
| Claude Haiku 5.5 (medium) | Not in the max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall; ranked in the AI Coding Daily ranking, common-leaf diagnostic ranking |
| Claude Opus 4.8 | Not plotted on or within the near gap of AA's rendered frontier (O51) |
| Claude Opus 5 | Not plotted on or within the near gap of AA's rendered frontier (O51) |
| Claude Opus 5.5 (high) | Not in the max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall; ranked in the AI Coding Daily ranking, common-leaf diagnostic ranking |
| Claude Opus 5.5 (medium) | Not in the max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall; ranked in the AI Coding Daily ranking, common-leaf diagnostic ranking |
| Claude Opus 5.5 (xhigh) | Incomplete benchmark evidence after an exhaustive search (O36, O53): Max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall; AI Coding Daily ranking: no AI Coding Daily (excl. bug finding) |
| Claude Sonnet 5 | Not plotted on or within the near gap of AA's rendered frontier (O51) |
| Claude Sonnet 5.5 (high) | Not plotted on or within the near gap of AA's rendered frontier (O51) |
| Claude Sonnet 5.5 (low) | Not plotted on or within the near gap of AA's rendered frontier (O51) |
| Claude Sonnet 5.5 (medium) | Not plotted on or within the near gap of AA's rendered frontier (O51) |
| Claude Sonnet 5.5 (xhigh) | Incomplete benchmark evidence after an exhaustive search (O36, O53): Max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall; AI Coding Daily ranking: no AI Coding Daily (excl. bug finding) |
| DeepSeek V4 Flash | Not plotted on or within the near gap of AA's rendered frontier (O51) |
| DeepSeek V4 Pro | Not plotted on or within the near gap of AA's rendered frontier (O51) |
| GLM-5.2 | No eligible exact-model Bug Hunt result in the selected source snapshot; Not plotted on or within the near gap of AA's rendered frontier (O51) |
| GLM-5.3 | Not plotted on or within the near gap of AA's rendered frontier (O51) |
| GLM-5.3 Flash | Not plotted on or within the near gap of AA's rendered frontier (O51) |
| GPT-5.5 | No eligible exact-model Bug Hunt result in the selected source snapshot; Not plotted on or within the near gap of AA's rendered frontier (O51) |
| GPT-5.6 Luna | Not plotted on or within the near gap of AA's rendered frontier (O51) |
| GPT-5.6 Luna (low) | Not in the max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall; ranked in the AI Coding Daily ranking, common-leaf diagnostic ranking |
| GPT-5.6 Sol | Not plotted on or within the near gap of AA's rendered frontier (O51) |
| GPT-6 Astra (high) | Not in the max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall; ranked in the AI Coding Daily ranking, common-leaf diagnostic ranking |
| GPT-6 Astra (xhigh) | Incomplete benchmark evidence after an exhaustive search (O36, O53): Max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall; AI Coding Daily ranking: no AI Coding Daily (excl. bug finding) |
| GPT-6 Luna (high) | Not in the max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall; ranked in the AI Coding Daily ranking, common-leaf diagnostic ranking |
| GPT-6 Luna (low) | Incomplete benchmark evidence after an exhaustive search (O36, O53): Max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall; AI Coding Daily ranking: no AI Coding Daily (excl. bug finding) |
| GPT-6 Luna (medium) | Not in the max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall; ranked in the AI Coding Daily ranking, common-leaf diagnostic ranking |
| GPT-6 Luna (xhigh) | Not in the max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall; ranked in the AI Coding Daily ranking, common-leaf diagnostic ranking |
| GPT-6 Sol | Not plotted on or within the near gap of AA's rendered frontier (O51) |
| GPT-6.1 Sol (high) | Not in the max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall; ranked in the AI Coding Daily ranking, common-leaf diagnostic ranking |
| GPT-6.1 Sol (low) | Not plotted on or within the near gap of AA's rendered frontier (O51) |
| GPT-6.1 Sol (medium) | Not in the max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall; ranked in the AI Coding Daily ranking, common-leaf diagnostic ranking |
| GPT-6.1 Sol (xhigh) | Incomplete benchmark evidence after an exhaustive search (O36, O53): Max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall; AI Coding Daily ranking: no AI Coding Daily (excl. bug finding) |
| Gemini 3.5 Flash | No eligible exact-model Bug Hunt result in the selected source snapshot; Not plotted on or within the near gap of AA's rendered frontier (O51) |
| Gemini 3.6 Flash | No eligible exact-model Bug Hunt result in the selected source snapshot; Not plotted on or within the near gap of AA's rendered frontier (O51) |
| Gemini 3.7 Flash | No eligible exact-model Bug Hunt result in the selected source snapshot; Not plotted on or within the near gap of AA's rendered frontier (O51) |
| Gemini 3.8 Flash | Not plotted on or within the near gap of AA's rendered frontier (O51) |
| Grok 4.6 | No eligible exact-model Bug Hunt result in the selected source snapshot; Not plotted on or within the near gap of AA's rendered frontier (O51) |
| Grok 4.6 (xhigh) | Not plotted on or within the near gap of AA's rendered frontier (O51) |
| Grok 4.7 | Not plotted on or within the near gap of AA's rendered frontier (O51) |
| Kimi K3 | No eligible exact-model Bug Hunt result in the selected source snapshot; Not plotted on or within the near gap of AA's rendered frontier (O51) |
| Kimi K3.1 Pro | Not in the max-effort ranking: no Code Migration v1.1 (Vals); ranked in the AI Coding Daily ranking, common-leaf diagnostic ranking |
| MiMo-V2.6-Flash | Incomplete benchmark evidence after an exhaustive search (O36, O53): Max-effort ranking: no Bug Hunt Bench, Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall; AI Coding Daily ranking: no Bug Hunt Bench, AI Coding Daily (excl. bug finding) |
| MiniMax-M3.1-Flash | Incomplete benchmark evidence after an exhaustive search (O36, O53): Max-effort ranking: no Bug Hunt Bench, Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall; AI Coding Daily ranking: no Bug Hunt Bench, AI Coding Daily (excl. bug finding) |
| Muse Spark 1.2 | No eligible exact-model Bug Hunt result in the selected source snapshot; Not plotted on or within the near gap of AA's rendered frontier (O51) |
| Muse Spark 1.3 | Not plotted on or within the near gap of AA's rendered frontier (O51) |
| Muse Spark 1.3 (xhigh) | Not plotted on or within the near gap of AA's rendered frontier (O51) |
| Muse Wonder | Not plotted on or within the near gap of AA's rendered frontier (O51) |
| Muse Wonder Full | Not plotted on or within the near gap of AA's rendered frontier (O51) |
| Qwen3.8 Max | Not plotted on or within the near gap of AA's rendered frontier (O51) |

## Quality leaf scores

Each leaf's score z on its fixed 0–100 anchors; "—" marks a leaf with no eligible exact-configuration result.

| Configuration | FrontierCode 1.1 | Terminal-Bench 4.0 (AA run) | Bug Hunt Bench | Vibe Code Bench v1.1 (Vals) | Code Migration v1.1 (Vals) | LiveBench 2.0 Overall | GDPval-AA v2.1 | AutomationBench-AA | AA-Omniscience | AA-LCR v1.1 | Humanity's Last Exam | SciCode | CritPt | Quality | Provisional |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Claude Opus 5.5 (max) | 52.2 | 59.6 | 39.7 | 90.3 | 81.0 | 85.1 | 68.3 | 69.5 | 73.2 | 84.7 | 61.4 | 66.9 | 31.7 | 67.71 | no |
| Claude Sonnet 5.5 (max) | 45.8 | 63.6 | 48.9 | 92.4 | 86.9 | 80.0 | 66.9 | 71.8 | 66.2 | 82.7 | 55.0 | 61.0 | 31.4 | 66.69 | no |
| GPT-6.1 Sol (max) | 49.1 | 56.1 | 42.2 | 88.9 | 77.3 | 84.1 | 54.8 | 64.9 | 70.8 | 83.0 | 52.9 | 54.2 | 31.7 | 64.11 | no |
| Claude Haiku 5.5 (max) | 41.8 | 32.8 | 20.5 | 90.4 | 52.4 | 69.8 | 56.0 | 35.4 | 55.3 | 82.7 | 44.4 | 55.0 | 18.9 | 50.44 | no |
| GPT-6 Astra (max) | 47.0 | 59.1 | 42.9 | 89.6 | 80.6 | 85.6 | 53.7 | 68.5 | 71.7 | 80.7 | 54.7 | 56.5 | 31.7 | 64.94 | no |
| GPT-6 Luna (max) | 41.9 | 12.6 | 17.4 | 81.6 | 46.7 | 64.6 | 46.6 | 53.2 | 50.3 | 83.3 | 38.5 | 54.6 | 19.4 | 46.70 | no |
| DeepSeek V4.1 Flash 1017 (max) | 43.7 | 33.8 | 40.7 | 87.7 | 67.5 | 74.0 | 62.3 | 66.6 | 52.4 | 82.7 | 43.3 | 55.9 | 24.0 | 57.38 | no |
| MiMo-V2.6-Pro | 45.4 | 34.8 | 17.1 | 85.2 | 48.8 | 68.5 | 59.2 | 58.6 | 54.2 | 86.3 | 49.4 | 60.9 | 26.6 | 53.27 | no |
| Gemini 4 Argon (high) | 43.5 | 57.1 | 38.8 | 91.9 | 70.8 | 79.3 | 56.2 | 77.5 | 71.2 | 79.7 | 57.1 | 61.8 | 27.1 | 63.54 | no |

## AI Coding Daily ranking

The configurations AI Coding Daily has tested, mostly at high and medium effort, scored on the AA leaves plus AI Coding Daily. Anchor version `v3-2026-10-25-aicd`; leaves: FrontierCode 1.1 21%, Terminal-Bench 4.0 (AA run) 17%, Bug Hunt Bench 12%, AI Coding Daily (excl. bug finding) 10% (software engineering 60%), plus the 7 leaves outside software engineering every ranking shares.

| Configuration | Plan rank | Plan value | Plan cost score | API rank | API value | API cost score | Quality | Quality coverage | Workload |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| [Claude Opus 5.5 (high)](https://valuerank.alolabs.dev/models/claude-opus-5-5-high/) | 1 | 58.39 | 53.14 | 7 | 48.94 | 15.34 | 60.14 | 100% | main |
| [Claude Opus 5.5 (medium)](https://valuerank.alolabs.dev/models/claude-opus-5-5-medium/) | 4 | 58.25 | 55.99 | 6 | 49.18 | 19.70 | 59.01 | 100% | main |
| [GPT-6.1 Sol (high)](https://valuerank.alolabs.dev/models/gpt-6-1-sol-high/) | 7 | 55.54 | 50.62 | 1 | 52.68 | 39.19 | 57.17 | 100% | main |
| [GPT-6.1 Sol (medium)](https://valuerank.alolabs.dev/models/gpt-6-1-sol-medium/) | 11 | 54.12 | 53.86 | 2 | 51.69 | 44.14 | 54.20 | 100% | main |
| [Claude Haiku 5.5 (high)](https://valuerank.alolabs.dev/models/claude-haiku-5-5-high/) | 15 | 53.59 | 87.98 | 9 | 48.76 | 68.64 | 42.13 | 100% | main |
| [GPT-6 Astra (high)](https://valuerank.alolabs.dev/models/gpt-6-astra-high/) | 18 | 52.84 | 35.55 | 13 | 46.78 | 11.30 | 58.61 | 100% | main |
| [Claude Haiku 5.5 (medium)](https://valuerank.alolabs.dev/models/claude-haiku-5-5-medium/) | 21 | 51.96 | 92.61 | 11 | 47.73 | 75.71 | 38.41 | 100% | main |
| [GPT-6 Luna (max)](https://valuerank.alolabs.dev/models/gpt-6-luna/) | 25 | 49.23 | 68.63 | 8 | 48.76 | 66.74 | 42.76 | 100% | main |
| [Kimi K3.1 Pro](https://valuerank.alolabs.dev/models/kimi-k3-1-pro/) | 29 | 48.10 | 7.39 | 5 | 49.21 | 11.83 | 61.67 | 100% | main |
| [GPT-6 Luna (xhigh)](https://valuerank.alolabs.dev/models/gpt-6-luna-xhigh/) | 30 | 46.93 | 73.71 | 12 | 47.13 | 74.51 | 38.00 | 100% | main |
| [MiMo-V2.6-Pro](https://valuerank.alolabs.dev/models/mimo-v2-6-pro/) | 33 | 46.76 | 39.34 | 3 | 51.43 | 57.98 | 49.24 | 100% | main |
| [DeepSeek V4.1 Flash 1017 (max)](https://valuerank.alolabs.dev/models/deepseek-v4-1-flash-1017/) | 34 | 46.70 | 28.31 | 4 | 50.58 | 43.84 | 52.82 | 100% | main |
| [Gemini 4 Argon (high)](https://valuerank.alolabs.dev/models/gemini-4-argon/) | 36 | 46.45 | 9.70 | 10 | 47.87 | 15.36 | 58.70 | 100% | main |
| [GPT-6 Luna (high)](https://valuerank.alolabs.dev/models/gpt-6-luna-high/) | 40 | 46.03 | 76.68 | 14 | 46.63 | 79.06 | 35.82 | 100% | main |
| [GPT-6 Luna (medium)](https://valuerank.alolabs.dev/models/gpt-6-luna-medium/) | 44 | 44.43 | 80.87 | 15 | 45.58 | 85.46 | 32.29 | 100% | main |
| [GPT-5.6 Luna (low)](https://valuerank.alolabs.dev/models/gpt-5-6-luna-low/) | 48 | 36.74 | 82.98 | 16 | 38.16 | 88.70 | 21.32 | 100% | main |

### AI Coding Daily ranking: quality leaf scores

| Configuration | FrontierCode 1.1 | Terminal-Bench 4.0 (AA run) | Bug Hunt Bench | AI Coding Daily (excl. bug finding) | GDPval-AA v2.1 | AutomationBench-AA | AA-Omniscience | AA-LCR v1.1 | Humanity's Last Exam | SciCode | CritPt | Quality | Provisional |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Claude Opus 5.5 (high) | 54.0 | 56.6 | 30.2 | 96.1 | 60.2 | 63.2 | 70.3 | 82.7 | 55.6 | 60.4 | 30.9 | 60.14 | no |
| Claude Opus 5.5 (medium) | 57.1 | 52.5 | 28.9 | 94.9 | 54.3 | 61.2 | 70.2 | 84.3 | 54.7 | 59.3 | 27.7 | 59.01 | no |
| GPT-6.1 Sol (high) | 46.6 | 51.5 | 34.8 | 94.7 | 50.6 | 64.5 | 70.7 | 82.3 | 51.4 | 55.8 | 30.0 | 57.17 | no |
| GPT-6.1 Sol (medium) | 43.3 | 48.0 | 27.6 | 92.8 | 47.5 | 62.6 | 70.0 | 83.3 | 49.9 | 53.2 | 27.7 | 54.20 | no |
| Claude Haiku 5.5 (high) | 43.6 | 21.7 | 15.2 | 85.9 | 45.8 | 33.7 | 52.9 | 77.3 | 37.3 | 48.7 | 18.6 | 42.13 | no |
| GPT-6 Astra (high) | 50.9 | 54.0 | 33.3 | 94.6 | 51.2 | 66.6 | 71.9 | 80.0 | 53.1 | 55.4 | 28.9 | 58.61 | no |
| Claude Haiku 5.5 (medium) | 40.4 | 15.2 | 11.4 | 85.5 | 38.8 | 28.6 | 52.2 | 77.3 | 33.8 | 49.0 | 12.9 | 38.41 | no |
| GPT-6 Luna (max) | 41.9 | 12.6 | 17.4 | 86.7 | 46.6 | 53.2 | 50.3 | 83.3 | 38.5 | 54.6 | 19.4 | 42.76 | no |
| Kimi K3.1 Pro | 47.1 | 67.2 | 34.3 | 91.0 | 67.3 | 73.3 | 64.8 | 86.3 | 52.5 | 60.8 | 24.6 | 61.67 | no |
| GPT-6 Luna (xhigh) | 33.2 | 8.1 | 13.3 | 83.2 | 43.2 | 47.8 | 49.1 | 80.0 | 34.3 | 51.7 | 17.4 | 38.00 | no |
| MiMo-V2.6-Pro | 45.4 | 34.8 | 17.1 | 79.3 | 59.2 | 58.6 | 54.2 | 86.3 | 49.4 | 60.9 | 26.6 | 49.24 | no |
| DeepSeek V4.1 Flash 1017 (max) | 43.7 | 33.8 | 40.7 | 87.1 | 62.3 | 66.6 | 52.4 | 82.7 | 43.3 | 55.9 | 24.0 | 52.82 | no |
| Gemini 4 Argon (high) | 43.5 | 57.1 | 38.8 | 83.2 | 56.2 | 77.5 | 71.2 | 79.7 | 57.1 | 61.8 | 27.1 | 58.70 | no |
| GPT-6 Luna (high) | 32.0 | 4.5 | 8.6 | 79.5 | 42.1 | 47.8 | 47.2 | 79.3 | 32.9 | 50.3 | 15.4 | 35.82 | no |
| GPT-6 Luna (medium) | 31.8 | 2.5 | 3.8 | 67.0 | 38.1 | 40.5 | 47.5 | 78.3 | 28.3 | 50.9 | 10.6 | 32.29 | no |
| GPT-5.6 Luna (low) | 15.4 | 0.0 | 3.8 | 50.9 | 24.7 | 11.7 | 42.7 | 70.0 | 19.8 | 46.1 | 2.6 | 21.32 | no |

### AI Coding Daily ranking: displayed record and noise

- API basis, displayed record (not a claim; E203): cheapest at or above quality 49.2: MiMo-V2.6-Pro ($136.13 per basket run; 9 reach it); at or above quality 38.0: Claude Haiku 5.5 (medium) ($45.91 per basket run; 13 reach it); at or above quality 58.6: Claude Opus 5.5 (medium) ($1,423.70 per basket run; 5 reach it).
- API basis, noise-margin companion (O44; each bar plus 5.9 quality points, so the bar's own configuration cannot decide it): cheapest at or above quality 55.1: GPT-6.1 Sol (high) ($431.07 per basket run); at or above quality 43.9: MiMo-V2.6-Pro ($136.13 per basket run); at or above quality 64.5: none.
- Plan basis, displayed record (not a claim; E203): cheapest at or above quality 49.2: Claude Opus 5.5 (medium) on Claude Pro ($24.17 per basket run; 25 reach it); at or above quality 38.0: Claude Haiku 5.5 (medium) on Claude Pro ($0.78 per basket run; 39 reach it); at or above quality 58.6: Claude Opus 5.5 (medium) on Claude Pro ($24.17 per basket run; 12 reach it).
- Plan basis, noise-margin companion (O44; each bar plus 5.9 quality points, so the bar's own configuration cannot decide it): cheapest at or above quality 55.1: Claude Opus 5.5 (medium) on Claude Pro ($24.17 per basket run); at or above quality 43.9: Claude Opus 5.5 (medium) on Claude Pro ($24.17 per basket run); at or above quality 64.5: none.
- AA cost caveat (O94; ranked at the published cost, no label of its own) on these bars' cheapest rows: Claude Haiku 5.5 (medium) (AA's cost omits a pricing term; up to 5× on its cost).
- Plan route flags on these bars' cheapest plan rows: Claude Haiku 5.5 (medium) on Claude Pro (possibly-superseded); Claude Opus 5.5 (medium) on Claude Pro (possibly-superseded).
- These outputs compare ranked configurations only; listed families shown with an indicative value (O41) are outside them (O43): Claude Sonnet 5.5, Claude Opus 5.5, GPT-6.1 Sol, GPT-6 Astra, Claude Haiku 5.5 (max), Claude Haiku 5.5, Claude Haiku 5.5 (low), Claude Opus 5.5 (xhigh), Claude Sonnet 5.5 (xhigh), GPT-6 Astra (xhigh), GPT-6 Luna (low), GPT-6.1 Sol (xhigh), MiMo-V2.6-Flash, MiniMax-M3.1-Flash.

Benchmark sampling noise (O39, an independent-task approximation): two values must differ by about 4.4 value points (median, 95%) to separate, and 1 of 15 adjacent API ranks and 1 of 19 adjacent Plan ranks of different configurations do (31 more adjacent Plan pairs are one configuration on two plans, ordered by the plans' multiples alone; E258). Its net direction is not established: every configuration is scored on the same tasks, which correlates their errors and narrows the true threshold (API 1 at correlation 0.3, 1 at correlation 0.6; Plan 1 at correlation 0.3, 1 at correlation 0.6), while sources it leaves out widen it (run-to-run and harness variance, AA's single cost run and, for the 30 Plan rows on an owner assumption (26 owner-named transfers and 4 O46 provider quota ceilings), that assumption's error). The noise band column groups each row with the band's first row it cannot be told apart from (O42); a Plan band marked † rests on an owner assumption (an owner-named transfer or an O46 provider quota ceiling) and excludes its error: an assumed multiple can be wrong by a factor of about 5.2 before the row's value moves by the median threshold (a tolerance, not an estimate of the assumption's error). The S1T scenario shares in [scores.md](scores.md) show each row's rank-1 and top-3 frequencies under that noise. AI Coding Daily's noise treats its six graded projects as six trials of the share of 60 points (n = 6, the wide reading, E263); read as 60 trials, the median threshold would be 3.3 (API) and 3.2 (Plan), with 1 and 1 adjacent ranks separable.


**Listed frontier families: indicative value, not ranked and not comparable (O41).** Quality is the mean over the leaves the configuration has, renormalised, with no imputation, so these values cannot be compared with the ranking above.

| Configuration | Missing | Quality (remaining leaves) | Quality coverage | Plan value (indicative) | API value (indicative) | API cost (USD per basket run) | Plan cost (USD per basket run) |
|---|---|---:|---:|---:|---:|---:|---:|
| Claude Sonnet 5.5 | AI Coding Daily (excl. bug finding) | 59.3 | 90% | 55.1 | 44.5 | $5,073.84 | $86.14 |
| Claude Opus 5.5 | AI Coding Daily (excl. bug finding) | 59.8 | 90% | 55.0 | 44.9 | $6,039.13 | $102.53 |
| GPT-6.1 Sol | AI Coding Daily (excl. bug finding) | 56.0 | 90% | 53.0 | 49.3 | $796.76 | $73.97 |
| GPT-6 Astra | AI Coding Daily (excl. bug finding) | 56.5 | 90% | 50.0 | 43.3 | $3,844.56 | $265.42 |
| Claude Haiku 5.5 (max) | AI Coding Daily (excl. bug finding) | 41.8 | 90% | 50.7 | 44.4 | $191.49 | $3.25 |
| Claude Haiku 5.5 | AI Coding Daily (excl. bug finding) | 40.5 | 90% | 51.3 | 45.8 | $107.10 | $1.82 |
| Claude Haiku 5.5 (low) | AI Coding Daily (excl. bug finding) | 27.9 | 90% | 45.4 | 41.9 | $28.12 | $0.48 |
| Claude Opus 5.5 (xhigh) | AI Coding Daily (excl. bug finding) | 58.4 | 90% | 55.5 | 45.2 | $3,374.80 | $57.30 |
| Claude Sonnet 5.5 (xhigh) | AI Coding Daily (excl. bug finding) | 54.1 | 90% | 53.9 | 44.5 | $1,826.03 | $31.00 |
| GPT-6 Astra (xhigh) | AI Coding Daily (excl. bug finding) | 56.9 | 90% | 51.0 | 44.7 | $2,899.42 | $200.17 |
| GPT-6 Luna (low) | AI Coding Daily (excl. bug finding) | 18.5 | 90% | 37.1 | 38.9 | $8.37 | $0.78 |
| GPT-6.1 Sol (xhigh) | AI Coding Daily (excl. bug finding) | 54.4 | 90% | 53.0 | 49.9 | $512.20 | $47.55 |
| MiMo-V2.6-Flash | Bug Hunt Bench, AI Coding Daily (excl. bug finding) | 44.1 | 78% | 45.0 | 50.9 | $60.37 | $52.59 |
| MiniMax-M3.1-Flash | Bug Hunt Bench, AI Coding Daily (excl. bug finding) | 46.6 | 78% | 42.9 | 47.2 | $234.35 | $234.35 |

### AI Coding Daily ranking: Plan routes and calibration

#### Measured-evidence calibration (diagnostic)

References: each workload's measured-only rows with complete cost evidence are the references: c_L = cheapest / 2, c_H = dearest x 2 (diagnostic only; the official anchors are unchanged). Status: evaluated.

- Workload `1453a9a0576b02ea`: measured anchors $12.09 to $328.91 from Claude Opus 5.5 (high), Claude Opus 5.5 (medium), GPT-6 Astra (high), GPT-6.1 Sol (high), GPT-6.1 Sol (medium); anchor ratio 27.2 against the official 11838.1. Official Plan anchors are set by Claude Haiku 5.5 (medium) on Claude Pro (owner-named transfer; AA cost caveat: leaves the anchors at the next freeze, O94) at the low end and Kimi K3.1 Pro on API-cost fallback at the high end.

| Configuration | Value on official Plan anchors | Value on measured anchors | Rank change |
|---|---:|---:|---:|
| Claude Opus 5.5 (high) ‡ | 58.39 | 62.83 | 1 |
| Claude Opus 5.5 (medium) ‡ | 58.25 | 64.01 | -1 |
| GPT-6 Astra (high) ‡ | 52.84 | 49.20 | 0 |
| GPT-6.1 Sol (high) ‡ | 55.54 | 58.82 | 1 |
| GPT-6.1 Sol (medium) ‡ | 54.12 | 58.89 | -1 |

Pairwise reversals: Claude Opus 5.5 (high) and Claude Opus 5.5 (medium); GPT-6.1 Sol (high) and GPT-6.1 Sol (medium). Largest value change: 5.76 points.

‡ measured on the same model at another effort (an O88 route; measured evidence under O90).

### AI Coding Daily ranking: interval outputs

**API basis, main workload: frontier.** Not evaluable: none. Competing without a label of its own (E183): Claude Haiku 5.5 (high): AA's cost omits a pricing term (O94); competes over its published cost up to the stated factor; Claude Haiku 5.5 (medium): AA's cost omits a pricing term (O94); competes over its published cost up to the stated factor.

| Configuration | Possible frontier | Definite frontier | Definite counterexample | Possible frontier blocked by |
|---|---|---|---|---|
| DeepSeek V4.1 Flash 1017 (max) | disproved | disproved | GPT-6.1 Sol (medium) | GPT-6.1 Sol (medium) |
| Gemini 4 Argon (high) | disproved | disproved | Claude Opus 5.5 (medium) | Claude Opus 5.5 (medium) |
| Kimi K3.1 Pro | certified | certified | — | — |
| GPT-6.1 Sol (high) | certified | certified | — | — |
| Claude Opus 5.5 (high) | certified | certified | — | — |
| MiMo-V2.6-Pro | certified | certified | — | — |
| Claude Opus 5.5 (medium) | certified | certified | — | — |
| GPT-6.1 Sol (medium) | certified | certified | — | — |
| GPT-6 Astra (high) | disproved | disproved | Gemini 4 Argon (high) | Gemini 4 Argon (high), Kimi K3.1 Pro, Claude Opus 5.5 (high), Claude Opus 5.5 (medium) |
| GPT-6 Luna (max) | certified | certified | — | — |
| GPT-6 Luna (xhigh) | certified | disproved | Claude Haiku 5.5 (medium) | — |
| GPT-6 Luna (high) | certified | certified | — | — |
| GPT-6 Luna (medium) | certified | certified | — | — |
| GPT-5.6 Luna (low) | certified | certified | — | — |

**API basis, main workload: cheapest at or above quality 49.2** (lower-median displayed quality of the non-provisional cohort configurations at freeze (E192; headline bar)). Status certified; confirmed cheapest: none.

Configurations that can be confirmed to qualify: 8 (confirmation needs the full-composite lower bound, with missing leaves at 0, to clear the bar; O25). Cheaper same-family configurations on AA's chart that were not evaluated (not ranked in this ranking: lacking its full benchmark set, or not plotted on or near the frontier; E201c, O51): GPT-6.1 Sol (medium): GPT-6.1 Sol (low).

Bar comparison: compares 9 configurations that can qualify. The bar is a displayed-quality level; qualification tests each row's full-composite bounds, so a row above the bar on displayed quality can still fail to qualify confirmed when leaves are missing (E198).

| Configuration | Displayed quality − bar | Confirmed qualifies | Possibly qualifies | Possibly cheapest |
|---|---:|---|---|---|
| DeepSeek V4.1 Flash 1017 (max) | 3.6 | certified | certified | disproved |
| Gemini 4 Argon (high) | 9.5 | certified | certified | disproved |
| Kimi K3.1 Pro | 12.4 | certified | certified | disproved |
| GPT-6.1 Sol (high) | 7.9 | certified | certified | disproved |
| Claude Opus 5.5 (high) | 10.9 | certified | certified | disproved |
| MiMo-V2.6-Pro | 0.0 | disproved | certified | certified |
| Claude Opus 5.5 (medium) | 9.8 | certified | certified | disproved |
| GPT-6.1 Sol (medium) | 5.0 | certified | certified | certified |
| GPT-6 Astra (high) | 9.4 | certified | certified | disproved |
| GPT-6 Luna (max) | -6.5 | disproved | disproved | disproved |
| GPT-6 Luna (xhigh) | -11.2 | disproved | disproved | disproved |
| GPT-6 Luna (high) | -13.4 | disproved | disproved | disproved |
| GPT-6 Luna (medium) | -17.0 | disproved | disproved | disproved |
| GPT-5.6 Luna (low) | -27.9 | disproved | disproved | disproved |

**API basis, main workload: cheapest at or above quality 38.0** (lower-quartile displayed quality of the non-provisional cohort configurations at freeze (O34)). Status certified; confirmed cheapest: none.

Configurations that can be confirmed to qualify: 10 (confirmation needs the full-composite lower bound, with missing leaves at 0, to clear the bar; O25). Cheaper same-family configurations on AA's chart that were not evaluated (not ranked in this ranking: lacking its full benchmark set, or not plotted on or near the frontier; E201c, O51): GPT-6 Luna (max): GPT-6 Luna (low), GPT-6 Luna (non-reasoning); GPT-6 Luna (xhigh): GPT-6 Luna (low), GPT-6 Luna (non-reasoning).

Bar comparison: compares 11 configurations that can qualify. The bar is a displayed-quality level; qualification tests each row's full-composite bounds, so a row above the bar on displayed quality can still fail to qualify confirmed when leaves are missing (E198).

| Configuration | Displayed quality − bar | Confirmed qualifies | Possibly qualifies | Possibly cheapest |
|---|---:|---|---|---|
| DeepSeek V4.1 Flash 1017 (max) | 14.8 | certified | certified | disproved |
| Gemini 4 Argon (high) | 20.7 | certified | certified | disproved |
| Kimi K3.1 Pro | 23.7 | certified | certified | disproved |
| GPT-6.1 Sol (high) | 19.2 | certified | certified | disproved |
| Claude Opus 5.5 (high) | 22.1 | certified | certified | disproved |
| MiMo-V2.6-Pro | 11.2 | certified | certified | disproved |
| Claude Opus 5.5 (medium) | 21.0 | certified | certified | disproved |
| GPT-6.1 Sol (medium) | 16.2 | certified | certified | disproved |
| GPT-6 Astra (high) | 20.6 | certified | certified | disproved |
| GPT-6 Luna (max) | 4.8 | certified | certified | certified |
| GPT-6 Luna (xhigh) | 0.0 | disproved | certified | certified |
| GPT-6 Luna (high) | -2.2 | disproved | disproved | disproved |
| GPT-6 Luna (medium) | -5.7 | disproved | disproved | disproved |
| GPT-5.6 Luna (low) | -16.7 | disproved | disproved | disproved |

**API basis, main workload: cheapest at or above quality 58.6** (upper-quartile displayed quality of the non-provisional cohort configurations at freeze (O34)). Status certified; confirmed cheapest: Claude Opus 5.5 (medium).

Configurations that can be confirmed to qualify: 4 (confirmation needs the full-composite lower bound, with missing leaves at 0, to clear the bar; O25). Cheaper same-family configurations on AA's chart that were not evaluated (not ranked in this ranking: lacking its full benchmark set, or not plotted on or near the frontier; E201c, O51): Claude Opus 5.5 (medium): Claude Opus 5.5 (low with fallback).

Bar comparison: compares 5 configurations that can qualify. The bar is a displayed-quality level; qualification tests each row's full-composite bounds, so a row above the bar on displayed quality can still fail to qualify confirmed when leaves are missing (E198).

| Configuration | Displayed quality − bar | Confirmed qualifies | Possibly qualifies | Possibly cheapest |
|---|---:|---|---|---|
| DeepSeek V4.1 Flash 1017 (max) | -5.8 | disproved | disproved | disproved |
| Gemini 4 Argon (high) | 0.1 | certified | certified | disproved |
| Kimi K3.1 Pro | 3.1 | certified | certified | disproved |
| GPT-6.1 Sol (high) | -1.4 | disproved | disproved | disproved |
| Claude Opus 5.5 (high) | 1.5 | certified | certified | disproved |
| MiMo-V2.6-Pro | -9.4 | disproved | disproved | disproved |
| Claude Opus 5.5 (medium) | 0.4 | certified | certified | certified |
| GPT-6.1 Sol (medium) | -4.4 | disproved | disproved | disproved |
| GPT-6 Astra (high) | 0.0 | disproved | certified | disproved |
| GPT-6 Luna (max) | -15.8 | disproved | disproved | disproved |
| GPT-6 Luna (xhigh) | -20.6 | disproved | disproved | disproved |
| GPT-6 Luna (high) | -22.8 | disproved | disproved | disproved |
| GPT-6 Luna (medium) | -26.3 | disproved | disproved | disproved |
| GPT-5.6 Luna (low) | -37.3 | disproved | disproved | disproved |

**Plan basis, main workload:** not evaluated (no row has FullCost and an identified M_W (E61/E67)).

### AI Coding Daily ranking: scenario shares

The scenario panel is the 16 rows scored on the main workload (E96, E266).

Frequencies over 10,000 scenarios per run (seed 20261025); streams are defined in [methodology.md](methodology.md#uncertainty-outputs). S1T adds benchmark sampling noise under an independent-task approximation (O39); the other streams exclude it, and every stream excludes correlated-task, harness and attempt effects (E155).

### API basis: rank 1

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M | S1T |
|---|---:|---:|---:|---:|---:|---:|
| Claude Haiku 5.5 (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.4% |
| Claude Haiku 5.5 (medium) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.3% |
| Claude Opus 5.5 (medium) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.6% |
| DeepSeek V4.1 Flash 1017 (max) | 0.0% | 0.0% | 0.1% | 0.0% | 0.0% | 6.9% |
| GPT-5.6 Luna (low) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Luna (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Luna (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.3% |
| GPT-6 Luna (medium) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Luna (xhigh) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (high) | 100.0% | 100.0% | 96.3% | 100.0% | 100.0% | 49.1% |
| GPT-6.1 Sol (medium) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 20.8% |
| Gemini 4 Argon (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.1% |
| Kimi K3.1 Pro | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.6% |
| MiMo-V2.6-Pro | 0.0% | 0.0% | 3.6% | 0.0% | 0.0% | 20.8% |

### API basis: rank 3 or better

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M | S1T |
|---|---:|---:|---:|---:|---:|---:|
| Claude Haiku 5.5 (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 6.2% |
| Claude Haiku 5.5 (medium) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.8% |
| Claude Opus 5.5 (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 5.2% |
| Claude Opus 5.5 (medium) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 8.1% |
| DeepSeek V4.1 Flash 1017 (max) | 0.0% | 0.0% | 14.8% | 0.0% | 0.0% | 40.5% |
| GPT-5.6 Luna (low) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.1% |
| GPT-6 Luna (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Luna (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 5.5% |
| GPT-6 Luna (medium) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Luna (xhigh) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.2% |
| GPT-6.1 Sol (high) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 88.4% |
| GPT-6.1 Sol (medium) | 100.0% | 100.0% | 93.8% | 100.0% | 100.0% | 69.0% |
| Gemini 4 Argon (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 2.1% |
| Kimi K3.1 Pro | 0.0% | 0.0% | 0.7% | 0.0% | 0.0% | 9.6% |
| MiMo-V2.6-Pro | 100.0% | 100.0% | 90.6% | 100.0% | 100.0% | 64.2% |

### API basis: on the frontier

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M | S1T |
|---|---:|---:|---:|---:|---:|---:|
| Claude Haiku 5.5 (high) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 86.3% |
| Claude Haiku 5.5 (medium) | 100.0% | 100.0% | 99.8% | 100.0% | 100.0% | 80.8% |
| Claude Opus 5.5 (high) | 100.0% | 100.0% | 95.9% | 100.0% | 100.0% | 49.2% |
| Claude Opus 5.5 (medium) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 74.4% |
| DeepSeek V4.1 Flash 1017 (max) | 0.0% | 0.0% | 9.9% | 0.0% | 0.0% | 32.0% |
| GPT-5.6 Luna (low) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% |
| GPT-6 Astra (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 5.3% |
| GPT-6 Luna (high) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 87.8% |
| GPT-6 Luna (max) | 100.0% | 100.0% | 82.4% | 100.0% | 100.0% | 57.9% |
| GPT-6 Luna (medium) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% |
| GPT-6 Luna (xhigh) | 0.0% | 0.0% | 28.9% | 0.0% | 0.0% | 40.9% |
| GPT-6.1 Sol (high) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 83.0% |
| GPT-6.1 Sol (medium) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 95.2% |
| Gemini 4 Argon (high) | 0.0% | 0.0% | 38.4% | 0.0% | 0.0% | 43.3% |
| Kimi K3.1 Pro | 100.0% | 100.0% | 98.1% | 100.0% | 100.0% | 61.9% |
| MiMo-V2.6-Pro | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 97.9% |

### API basis: value-score dispersion (SD; covariance term)

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M | S1T |
|---|---:|---:|---:|---:|---:|---:|
| Claude Haiku 5.5 (high) | 0.00 (+0.00) | 0.00 (+0.00) | 1.61 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.48 (+0.00) |
| Claude Haiku 5.5 (medium) | 0.00 (+0.00) | 0.00 (+0.00) | 1.74 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.46 (+0.00) |
| Claude Opus 5.5 (high) | 0.00 (+0.00) | 0.00 (+0.00) | 1.32 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.36 (+0.00) |
| Claude Opus 5.5 (medium) | 0.00 (+0.00) | 0.00 (+0.00) | 1.33 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.38 (+0.00) |
| DeepSeek V4.1 Flash 1017 (max) | 0.00 (+0.00) | 0.00 (+0.00) | 1.29 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.53 (+0.00) |
| GPT-5.6 Luna (low) | 0.00 (+0.00) | 0.00 (+0.00) | 1.44 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.63 (+0.00) |
| GPT-6 Astra (high) | 0.00 (+0.00) | 0.00 (+0.00) | 1.28 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.41 (+0.00) |
| GPT-6 Luna (high) | 0.00 (+0.00) | 0.00 (+0.00) | 1.85 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.46 (+0.00) |
| GPT-6 Luna (max) | 0.00 (+0.00) | 0.00 (+0.00) | 1.77 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.43 (+0.00) |
| GPT-6 Luna (medium) | 0.00 (+0.00) | 0.00 (+0.00) | 1.71 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.66 (+0.00) |
| GPT-6 Luna (xhigh) | 0.00 (+0.00) | 0.00 (+0.00) | 1.81 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.46 (+0.00) |
| GPT-6.1 Sol (high) | 0.00 (+0.00) | 0.00 (+0.00) | 1.31 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.38 (+0.00) |
| GPT-6.1 Sol (medium) | 0.00 (+0.00) | 0.00 (+0.00) | 1.42 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.45 (+0.00) |
| Gemini 4 Argon (high) | 0.00 (+0.00) | 0.00 (+0.00) | 1.13 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.62 (+0.00) |
| Kimi K3.1 Pro | 0.00 (+0.00) | 0.00 (+0.00) | 1.29 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.46 (+0.00) |
| MiMo-V2.6-Pro | 0.00 (+0.00) | 0.00 (+0.00) | 1.41 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.66 (+0.00) |

Plan streams S1, S2, S1 endpoint-heavy, S1M and S1T run with owner assumptions off (owner-named transfers and O46 provider quota ceilings; E167): Claude Haiku 5.5 (high) on Claude Max 20x, Claude Haiku 5.5 (high) on Claude Max 5x, Claude Haiku 5.5 (high) on Claude Pro, Claude Haiku 5.5 (medium) on Claude Max 20x, Claude Haiku 5.5 (medium) on Claude Max 5x, Claude Haiku 5.5 (medium) on Claude Pro, GPT-5.6 Luna (low) on ChatGPT Plus, GPT-5.6 Luna (low) on ChatGPT Pro 100, GPT-5.6 Luna (low) on ChatGPT Pro 200, GPT-5.6 Luna (low) on ChatGPT Pro 500, GPT-6 Luna (high) on ChatGPT Plus, GPT-6 Luna (high) on ChatGPT Pro 100, GPT-6 Luna (high) on ChatGPT Pro 200, GPT-6 Luna (high) on ChatGPT Pro 500, GPT-6 Luna (max) on ChatGPT Plus, GPT-6 Luna (max) on ChatGPT Pro 100, GPT-6 Luna (max) on ChatGPT Pro 200, GPT-6 Luna (max) on ChatGPT Pro 500, GPT-6 Luna (medium) on ChatGPT Plus, GPT-6 Luna (medium) on ChatGPT Pro 100, GPT-6 Luna (medium) on ChatGPT Pro 200, GPT-6 Luna (medium) on ChatGPT Pro 500, GPT-6 Luna (xhigh) on ChatGPT Plus, GPT-6 Luna (xhigh) on ChatGPT Pro 100, GPT-6 Luna (xhigh) on ChatGPT Pro 200, GPT-6 Luna (xhigh) on ChatGPT Pro 500, MiMo-V2.6-Pro on MiMo Token Plan Lite, MiMo-V2.6-Pro on MiMo Token Plan Max, MiMo-V2.6-Pro on MiMo Token Plan Pro, MiMo-V2.6-Pro on MiMo Token Plan Standard depend on an owner assumption and are unevaluable there (—), never reselected or replaced by API cost.

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
| Claude Opus 5.5 (high) on Claude Pro | 100.0% | 100.0% | 73.0% | 100.0% | 100.0% | 51.4% |
| Claude Opus 5.5 (medium) on Claude Max 20x | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (medium) on Claude Max 5x | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (medium) on Claude Pro | 0.0% | 0.0% | 27.0% | 0.0% | 0.0% | 46.1% |
| DeepSeek V4.1 Flash 1017 (max) on API-cost fallback | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-5.6 Luna (low) on ChatGPT Plus | 0.0% | — | — | — | — | — |
| GPT-5.6 Luna (low) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — |
| GPT-5.6 Luna (low) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — |
| GPT-5.6 Luna (low) on ChatGPT Pro 500 | 0.0% | — | — | — | — | — |
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
| GPT-6.1 Sol (high) on ChatGPT Pro 500 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 2.1% |
| GPT-6.1 Sol (medium) on ChatGPT Plus | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (medium) on ChatGPT Pro 100 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (medium) on ChatGPT Pro 200 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (medium) on ChatGPT Pro 500 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.3% |
| Gemini 4 Argon (high) on API-cost fallback | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Kimi K3.1 Pro on API-cost fallback | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| MiMo-V2.6-Pro on MiMo Token Plan Lite | 0.0% | — | — | — | — | — |
| MiMo-V2.6-Pro on MiMo Token Plan Max | 0.0% | — | — | — | — | — |
| MiMo-V2.6-Pro on MiMo Token Plan Pro | 0.0% | — | — | — | — | — |
| MiMo-V2.6-Pro on MiMo Token Plan Standard | 0.0% | — | — | — | — | — |

### Plan basis: rank 3 or better

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M | S1T |
|---|---:|---:|---:|---:|---:|---:|
| Claude Haiku 5.5 (high) on Claude Max 20x | 0.0% | — | — | — | — | — |
| Claude Haiku 5.5 (high) on Claude Max 5x | 0.0% | — | — | — | — | — |
| Claude Haiku 5.5 (high) on Claude Pro | 0.0% | — | — | — | — | — |
| Claude Haiku 5.5 (medium) on Claude Max 20x | 0.0% | — | — | — | — | — |
| Claude Haiku 5.5 (medium) on Claude Max 5x | 0.0% | — | — | — | — | — |
| Claude Haiku 5.5 (medium) on Claude Pro | 0.0% | — | — | — | — | — |
| Claude Opus 5.5 (high) on Claude Max 20x | 100.0% | 100.0% | 73.0% | 100.0% | 100.0% | 51.5% |
| Claude Opus 5.5 (high) on Claude Max 5x | 100.0% | 100.0% | 60.6% | 100.0% | 100.0% | 49.6% |
| Claude Opus 5.5 (high) on Claude Pro | 100.0% | 100.0% | 83.1% | 100.0% | 100.0% | 52.8% |
| Claude Opus 5.5 (medium) on Claude Max 20x | 0.0% | 0.0% | 27.0% | 0.0% | 0.0% | 46.2% |
| Claude Opus 5.5 (medium) on Claude Max 5x | 0.0% | 0.0% | 16.9% | 0.0% | 0.0% | 44.7% |
| Claude Opus 5.5 (medium) on Claude Pro | 0.0% | 0.0% | 39.4% | 0.0% | 0.0% | 48.0% |
| DeepSeek V4.1 Flash 1017 (max) on API-cost fallback | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-5.6 Luna (low) on ChatGPT Plus | 0.0% | — | — | — | — | — |
| GPT-5.6 Luna (low) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — |
| GPT-5.6 Luna (low) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — |
| GPT-5.6 Luna (low) on ChatGPT Pro 500 | 0.0% | — | — | — | — | — |
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
| GPT-6.1 Sol (high) on ChatGPT Plus | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 2.0% |
| GPT-6.1 Sol (high) on ChatGPT Pro 100 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 2.0% |
| GPT-6.1 Sol (high) on ChatGPT Pro 200 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (high) on ChatGPT Pro 500 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 2.4% |
| GPT-6.1 Sol (medium) on ChatGPT Plus | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.3% |
| GPT-6.1 Sol (medium) on ChatGPT Pro 100 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.3% |
| GPT-6.1 Sol (medium) on ChatGPT Pro 200 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (medium) on ChatGPT Pro 500 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.3% |
| Gemini 4 Argon (high) on API-cost fallback | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Kimi K3.1 Pro on API-cost fallback | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| MiMo-V2.6-Pro on MiMo Token Plan Lite | 0.0% | — | — | — | — | — |
| MiMo-V2.6-Pro on MiMo Token Plan Max | 0.0% | — | — | — | — | — |
| MiMo-V2.6-Pro on MiMo Token Plan Pro | 0.0% | — | — | — | — | — |
| MiMo-V2.6-Pro on MiMo Token Plan Standard | 0.0% | — | — | — | — | — |

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
| Claude Opus 5.5 (high) on Claude Pro | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 66.0% |
| Claude Opus 5.5 (medium) on Claude Max 20x | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (medium) on Claude Max 5x | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (medium) on Claude Pro | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% |
| DeepSeek V4.1 Flash 1017 (max) on API-cost fallback | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-5.6 Luna (low) on ChatGPT Plus | 0.0% | — | — | — | — | — |
| GPT-5.6 Luna (low) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — |
| GPT-5.6 Luna (low) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — |
| GPT-5.6 Luna (low) on ChatGPT Pro 500 | 0.0% | — | — | — | — | — |
| GPT-6 Astra (high) on ChatGPT Plus | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (high) on ChatGPT Pro 100 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (high) on ChatGPT Pro 200 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 18.5% |
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
| GPT-6.1 Sol (high) on ChatGPT Pro 500 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 7.0% |
| GPT-6.1 Sol (medium) on ChatGPT Plus | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (medium) on ChatGPT Pro 100 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (medium) on ChatGPT Pro 200 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (medium) on ChatGPT Pro 500 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 3.7% |
| Gemini 4 Argon (high) on API-cost fallback | 0.0% | 0.0% | 3.9% | 0.0% | 0.0% | 21.0% |
| Kimi K3.1 Pro on API-cost fallback | 100.0% | 100.0% | 98.2% | 100.0% | 100.0% | 58.8% |
| MiMo-V2.6-Pro on MiMo Token Plan Lite | 0.0% | — | — | — | — | — |
| MiMo-V2.6-Pro on MiMo Token Plan Max | 0.0% | — | — | — | — | — |
| MiMo-V2.6-Pro on MiMo Token Plan Pro | 0.0% | — | — | — | — | — |
| MiMo-V2.6-Pro on MiMo Token Plan Standard | 0.0% | — | — | — | — | — |

### Plan basis: value-score dispersion (SD; covariance term)

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M | S1T |
|---|---:|---:|---:|---:|---:|---:|
| Claude Haiku 5.5 (high) on Claude Max 20x | 0.00 (+0.00) | — | — | — | — | — |
| Claude Haiku 5.5 (high) on Claude Max 5x | 0.00 (+0.00) | — | — | — | — | — |
| Claude Haiku 5.5 (high) on Claude Pro | 0.00 (+0.00) | — | — | — | — | — |
| Claude Haiku 5.5 (medium) on Claude Max 20x | 0.00 (+0.00) | — | — | — | — | — |
| Claude Haiku 5.5 (medium) on Claude Max 5x | 0.00 (+0.00) | — | — | — | — | — |
| Claude Haiku 5.5 (medium) on Claude Pro | 0.00 (+0.00) | — | — | — | — | — |
| Claude Opus 5.5 (high) on Claude Max 20x | 0.00 (+0.00) | 0.00 (+0.00) | 1.32 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.36 (+0.00) |
| Claude Opus 5.5 (high) on Claude Max 5x | 0.00 (+0.00) | 0.00 (+0.00) | 1.32 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.36 (+0.00) |
| Claude Opus 5.5 (high) on Claude Pro | 0.00 (+0.00) | 0.00 (+0.00) | 1.32 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.36 (+0.00) |
| Claude Opus 5.5 (medium) on Claude Max 20x | 0.00 (+0.00) | 0.00 (+0.00) | 1.33 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.38 (+0.00) |
| Claude Opus 5.5 (medium) on Claude Max 5x | 0.00 (+0.00) | 0.00 (+0.00) | 1.33 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.38 (+0.00) |
| Claude Opus 5.5 (medium) on Claude Pro | 0.00 (+0.00) | 0.00 (+0.00) | 1.33 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.38 (+0.00) |
| DeepSeek V4.1 Flash 1017 (max) on API-cost fallback | 0.00 (+0.00) | 0.00 (+0.00) | 1.30 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.51 (+0.00) |
| GPT-5.6 Luna (low) on ChatGPT Plus | 0.00 (+0.00) | — | — | — | — | — |
| GPT-5.6 Luna (low) on ChatGPT Pro 100 | 0.00 (+0.00) | — | — | — | — | — |
| GPT-5.6 Luna (low) on ChatGPT Pro 200 | 0.00 (+0.00) | — | — | — | — | — |
| GPT-5.6 Luna (low) on ChatGPT Pro 500 | 0.00 (+0.00) | — | — | — | — | — |
| GPT-6 Astra (high) on ChatGPT Plus | 0.00 (+0.00) | 0.00 (+0.00) | 1.28 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.40 (+0.00) |
| GPT-6 Astra (high) on ChatGPT Pro 100 | 0.00 (+0.00) | 0.00 (+0.00) | 1.28 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.40 (+0.00) |
| GPT-6 Astra (high) on ChatGPT Pro 200 | 0.00 (+0.00) | 0.00 (+0.00) | 1.28 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.40 (+0.00) |
| GPT-6 Astra (high) on ChatGPT Pro 500 | 0.00 (+0.00) | 0.00 (+0.00) | 1.28 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.40 (+0.00) |
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
| GPT-6.1 Sol (high) on ChatGPT Plus | 0.00 (+0.00) | 0.00 (+0.00) | 1.31 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.40 (+0.00) |
| GPT-6.1 Sol (high) on ChatGPT Pro 100 | 0.00 (+0.00) | 0.00 (+0.00) | 1.31 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.40 (+0.00) |
| GPT-6.1 Sol (high) on ChatGPT Pro 200 | 0.00 (+0.00) | 0.00 (+0.00) | 1.31 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.40 (+0.00) |
| GPT-6.1 Sol (high) on ChatGPT Pro 500 | 0.00 (+0.00) | 0.00 (+0.00) | 1.31 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.40 (+0.00) |
| GPT-6.1 Sol (medium) on ChatGPT Plus | 0.00 (+0.00) | 0.00 (+0.00) | 1.42 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.43 (+0.00) |
| GPT-6.1 Sol (medium) on ChatGPT Pro 100 | 0.00 (+0.00) | 0.00 (+0.00) | 1.42 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.43 (+0.00) |
| GPT-6.1 Sol (medium) on ChatGPT Pro 200 | 0.00 (+0.00) | 0.00 (+0.00) | 1.42 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.43 (+0.00) |
| GPT-6.1 Sol (medium) on ChatGPT Pro 500 | 0.00 (+0.00) | 0.00 (+0.00) | 1.42 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.43 (+0.00) |
| Gemini 4 Argon (high) on API-cost fallback | 0.00 (+0.00) | 0.00 (+0.00) | 1.14 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.63 (+0.00) |
| Kimi K3.1 Pro on API-cost fallback | 0.00 (+0.00) | 0.00 (+0.00) | 1.29 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.46 (+0.00) |
| MiMo-V2.6-Pro on MiMo Token Plan Lite | 0.00 (+0.00) | — | — | — | — | — |
| MiMo-V2.6-Pro on MiMo Token Plan Max | 0.00 (+0.00) | — | — | — | — | — |
| MiMo-V2.6-Pro on MiMo Token Plan Pro | 0.00 (+0.00) | — | — | — | — | — |
| MiMo-V2.6-Pro on MiMo Token Plan Standard | 0.00 (+0.00) | — | — | — | — | — |

### Named S2 specification branches

- **Bug Hunt harness band (E19)** (S2): unevaluable; the captured tbench.ai leaderboard lists no configuration under two or more agents, so no cross-agent spread exists
- **cache-hit variation (E34)** (S2): unevaluable; AA's published cost embeds its cache-pricing protocol; varying the cache-hit rate needs each basket component's cache-read and uncached-input demand, which AA publishes only for the whole Index (E157)
- **first-party list versus cross-provider median price rule (E122)** (S2): unevaluable; AA publishes one price per configuration under its own rule; the alternative rule's prices are not captured

### Cheapest-above-the-bar labels (API basis)

The 90% rule's error bound holds per published event (candidate and kernel assignment); it is not corrected across the listed candidates (E198). Each kernel assignment code gives the kernel used for the candidate and the competitors, in that order (U uniform, H endpoint-heavy; a quality-level bar has no reference rows, so it takes no letter); the label needs every assignment met.

| Bar | Candidate | Reading | Frequency range | Kernel assignments | Label |
|---|---|---|---|---|---|
| quality 49.2 | MiMo-V2.6-Pro | not scenario-supported | 49.1% to 50.1% | UU not met, UH not met, HU not met, HH not met | no |
| quality 49.2 | GPT-6.1 Sol (medium) | not scenario-supported | 49.8% to 50.9% | UU not met, UH not met, HU not met, HH not met | no |
| quality 38.0 | GPT-6 Luna (max) | not scenario-supported | 0.0% to 0.0% | UU not met, UH not met, HU not met, HH not met | no |
| quality 38.0 | GPT-6 Luna (xhigh) | not scenario-supported | 0.0% to 0.0% | UU not met, UH not met, HU not met, HH not met | no |
| quality 58.6 | Claude Opus 5.5 (medium) | supported under all registered role-group kernel checks | 100.0% to 100.0% | UU met, UH met, HU met, HH met | yes |

### AI Coding Daily ranking: diagnostics

- **Terminal-Bench cross-source agreement (AA's mini-SWE-agent run against tbench.ai):** undefined (panel too small); 0 rows take the leaf from tbench.ai (gap fill).
- **Rank separability (O39, independent-task approximation):** median separation 4.43 value points (API) and 4.41 (Plan); separable adjacent ranks: API 1 of 15, Plan 1 of 19. Assumptions: tasks are independent and each leaf's score is a mean over its published task count (plug-in binomial with the proportion (k + 1/2) / (n + 1), I28); attempts averaged within a task and tasks shared across models are ignored, so the noise is approximate; GDPval-AA: each row's rating interval as AA's model page displays it, read as a 95% normal interval (AA states no level), SD = half-width / 1.96; AA-Omniscience: each of 6,000 questions scores +1, 0 or -1, with the shares from AA's accuracy and hallucination rate; Vals boards (Vibe Code Bench v1.1, Code Migration v1.1): Vals' published standard error per record, read as the leaf's SD; AI Coding Daily: judged points over its six graded projects read as a binomial share of 60 points (an assumption; the board publishes no error).
- **FrontierCode against Cognition:** FrontierCode cross-source agreement (AA against Cognition, same name and effort; E234): Kendall tau 0.77 (interval 0.58 to 0.91) on 22 rows. Cognition minus AA: mean +2.6 points, largest 11.6.
- **Gap-fill removal (E234, diagnostic; scores unchanged):** with these leaves removed and the rest renormalised — GPT-6 Astra (high) (FrontierCode 1.1); GPT-5.6 Luna (low) (FrontierCode 1.1) — API 4 rows move; largest move 3 (GPT-6 Astra (high)); Plan 3 rows move; largest move 2 (GPT-6 Astra (high)).
- **Bar results without the gap fills (E234, sensitivity; labels unchanged):** cheapest displayed row as published, with fills removed, and with third-party fills lowered by the mean offset 2.6 points — API quality 49.2: MiMo-V2.6-Pro in all three; API quality 38.0: Claude Haiku 5.5 (medium) in all three; API quality 58.6: Claude Opus 5.5 (medium) in all three; Plan quality 49.2: Claude Opus 5.5 (medium) in all three; Plan quality 38.0: Claude Haiku 5.5 (medium) in all three; Plan quality 58.6: Claude Opus 5.5 (medium) in all three.
- **Harness cost (O123, S2 stress):** unevaluable: no model is listed under two or more agents in AA's Coding Agent Index capture, so no agent effect is identified (O123). Coding Agent Index agents (each part of its costed configuration; none is the run behind the FrontierCode or Terminal-Bench leaf): DeepSeek V4.1 Flash 1017 (max): DeepSeek Harness; Gemini 4 Argon (high): Antigravity CLI; GPT-6 Luna (max): Codex.
- **Quality agreement:** quality agreement (matched-panel sensitivity): Kendall tau 0.68 (interval 0.39 to 0.92) on 16 rows.
- **Quality-substitution value agreement (API):** quality-substitution value agreement, api basis (matched-panel sensitivity): Kendall tau 0.42 (interval -0.03 to 0.75) on 16 rows.
- **Quality-substitution value agreement (Plan):** quality-substitution value agreement, plan basis (matched-panel sensitivity): Kendall tau 0.77 (interval 0.54 to 0.93) on 16 rows.
- **Disjoint-evidence agreement:** disjoint-evidence agreement (restricted evidence comparison, not an eligible ranking): Kendall tau 0.67 (interval 0.37 to 0.92) on 16 rows.
- **Quality source shares:** AA-run 78%, independent 22%.
- **Non-discriminating leaves:** none.
- **Group drift:** estimated; flagged: knowledge.
- **Omniscience abstention sensitivity** (z_pen = max(0, I)): 8 rows move; largest move 2 (Gemini 4 Argon (high), GPT-6 Astra (high), GPT-6 Luna (max), Kimi K3.1 Pro).
- **GDPval-AA logistic sensitivity** (z = 100 / (1 + 10^((1600 - E) / 400)) against AA's pinned anchor; every other input fixed): API 11 rows move; largest move 2 (Gemini 4 Argon (high), GPT-6 Astra (high), GPT-6.1 Sol (medium)); Plan 5 rows move; largest move 3 (GPT-6 Luna (xhigh)).
- **Anchor stability:** trimmed anchors (P10 / 2 and P90 x 2 (diagnostic only)) give $15.66 to $4,166.96; 13 rows move; largest move 4 (Claude Haiku 5.5 (high), Kimi K3.1 Pro).

- **Basket readiness (E22):** priced leaves cover 44% of nominal quality weight (AutomationBench-AA, GDPval-AA v2.1, AA-LCR v1.1, SciCode, Terminal-Bench 4.0 (AA run)); pending components: Coding Agent Index, FrontierCode 1.1, ITBench-AA.
- **SWE cost companion (O14, diagnostic):** 3 rows evaluated; flagged far from the median ratio: none.
- **Matched-cost diagnostic (E55):** evaluated at 57% priced quality weight; basket/matched cost-order reversals with separated intervals: 2; rank-gap warnings: 0.
- **Frontier-families anchors (E187, diagnostic):** anchors rebuilt from the 16 frontier and near-frontier references move API no rank changes (value points per cost doubling 2.83 vs 2.83 frozen); Plan no rank changes (value points per cost doubling 1.85 vs 1.85 frozen).
- **Frontier-families bar (E199, sensitivity; the frozen bar stays primary):** quality 49.2 over 16 configurations; cheapest at or above it on the API main workload: not unique; possibly MiMo-V2.6-Pro, GPT-6.1 Sol (medium) (compares 9 configurations that can qualify).
- **One row per family (E205, diagnostic; the frozen ladder and anchors stay primary):** with each family's primary configuration only (7 rows in the one-row-per-family bar population), the ladder (headline, lower quartile, upper quartile) would be 52.8 / 42.8 / 58.6 against 49.2 / 38.0 / 58.6 frozen; anchors rebuilt from its 7 references move API no rank changes (value points per cost doubling 2.83 vs 2.83 frozen); Plan 10 rows move; largest move 3 (GPT-6 Luna (high)) (value points per cost doubling 2.04 vs 1.85 frozen).
- **Ladder over scored rows (I28, sensitivity; the frozen ladder stays primary):** the bar population keeps full-benchmark rows that have no cost; today every such row has a cost, so the ladder is unchanged.
- **Bar currency (E207, informational):** rows reaching each frozen bar: quality 49.2: 9 of 16; quality 38.0: 13 of 16; quality 58.6: 5 of 16; the current population would freeze 49.2 / 38.0 / 58.6; lifetime until the next anchor re-freeze or methodology version, whichever comes first; no staleness flag.
- **Token mix (E208):** 1 selected routes: mix not reported: the measurement publishes no token-category shares; 12 selected routes: mix unidentified: the basket's token-category shares are set-identified only (E124), so the L1 test (above 0.30 flags mix-unmatched) is not computed.
- **Observed-range sensitivity (E219, not evidence; no label changes):** with each missing leaf inside the cohort's observed range for that leaf, quality 49.2: 9 can qualify, 8 confirmed; possibly cheapest MiMo-V2.6-Pro, GPT-6.1 Sol (medium); quality 38.0: 11 can qualify, 10 confirmed; possibly cheapest GPT-6 Luna (max), GPT-6 Luna (xhigh); quality 58.6: 5 can qualify, 4 confirmed; Claude Opus 5.5 (medium) confirmed cheapest.
- **What would settle the headline bar (E221, not a claim):** rows that can but need not reach quality 49.2, with the mean score their missing leaves would need: MiMo-V2.6-Pro (no missing leaf; reporting precision only).
- **Common leaf set (E226, diagnostic; scores unchanged):** without the leaves fewer than 90% of cohort rows have (none), API no rank changes; Plan no rank changes; rows reaching each bar: quality 49.2: 9 → 9; quality 38.0: 13 → 13; quality 58.6: 5 → 5; rows whose displayed quality differs from common-leaf quality by more than one cost doubling's worth: none.
- **Harness by leaf (E227):** Terminal-Bench: mini-SWE-agent 16; Bug Hunt: Codex CLI 8, Claude Code 4, Antigravity CLI 1, Claude Code / Anthropic-compatible shim 1, Claude Code / Moonshot API 1, DeepSeek Harness / DeepSeek API 1; AI Coding Daily: Codex CLI 8, Claude Code 4, OpenCode 2, DeepSeek Harness 1, Devin 1.
- **Coding Agent Index safety refusals (O63, flagged; costs and scores unchanged):** none.

### Leave-one-component-out cost family (E172)

Each admitted basket unit removed in turn, scored on anchors rebuilt by the freeze rule (rank changes against the primary ranking; quality held fixed).

| Removed component | API rank changes | Plan rank changes | API value points per cost doubling |
|---|---|---|---:|
| AA-Briefcase | 9 rows move; largest move 2 (Claude Haiku 5.5 (high)) | 6 rows move; largest move 1 (Claude Haiku 5.5 (high), DeepSeek V4.1 Flash 1017 (max), Gemini 4 Argon (high), GPT-6 Luna (xhigh), GPT-6.1 Sol (medium), MiMo-V2.6-Pro) | 2.89 |
| GDPval-AA | 7 rows move; largest move 2 (GPT-6 Luna (max)) | no rank changes | 2.90 |
| GDP.pdf | 4 rows move; largest move 1 (Claude Opus 5.5 (medium), GPT-6 Astra (high), GPT-6 Luna (xhigh), Kimi K3.1 Pro) | no rank changes | 2.77 |
| AutomationBench-AA | 9 rows move; largest move 2 (GPT-6 Astra (high)) | 6 rows move; largest move 1 (Claude Opus 5.5 (high), Claude Opus 5.5 (medium), DeepSeek V4.1 Flash 1017 (max), Gemini 4 Argon (high), GPT-6 Luna (high), MiMo-V2.6-Pro) | 2.62 |
| Terminal-Bench 4.0 (AA Index run) | 9 rows move; largest move 4 (Claude Haiku 5.5 (high)) | 2 rows move; largest move 1 (DeepSeek V4.1 Flash 1017 (max), Gemini 4 Argon (high)) | 2.86 |
| SciCode | no rank changes | no rank changes | 2.82 |
| AA-LCR | 4 rows move; largest move 1 (Claude Haiku 5.5 (high), Claude Opus 5.5 (medium), GPT-6 Luna (max), Kimi K3.1 Pro) | no rank changes | 2.80 |

### Subset rows: paired bridge and missing spend (E10, E173)

No row is scored on a subset workload.

### Deletion sensitivity

| Branch | Retained nominal weight | Status | API rank changes | Plan rank changes |
|---|---:|---|---|---|
| leave-out:frontierCode | 79% | evaluated | 9 rows move; largest move 4 (Gemini 4 Argon (high)) | 8 rows move; largest move 4 (Gemini 4 Argon (high)) |
| leave-out:terminalBench | 83% | evaluated | 15 rows move; largest move 8 (Kimi K3.1 Pro) | 15 rows move; largest move 5 (Kimi K3.1 Pro) |
| leave-out:bugHunt | 88% | evaluated | 11 rows move; largest move 3 (DeepSeek V4.1 Flash 1017 (max)) | 4 rows move; largest move 2 (DeepSeek V4.1 Flash 1017 (max), GPT-6 Luna (high)) |
| leave-out:aiCodingDaily | 90% | evaluated | 6 rows move; largest move 2 (Gemini 4 Argon (high), GPT-6 Luna (max)) | 4 rows move; largest move 3 (Gemini 4 Argon (high), GPT-6 Luna (xhigh)) |
| leave-out:gdpval | 90% | evaluated | 7 rows move; largest move 2 (Kimi K3.1 Pro) | 8 rows move; largest move 3 (Gemini 4 Argon (high)) |
| leave-out:automationBench | 90% | evaluated | 7 rows move; largest move 5 (Claude Haiku 5.5 (high)) | 6 rows move; largest move 1 (Claude Haiku 5.5 (high), Claude Haiku 5.5 (medium), Gemini 4 Argon (high), GPT-6 Astra (high), GPT-6 Luna (high), GPT-6.1 Sol (medium)) |
| leave-out:omniscience | 90% | evaluated | 5 rows move; largest move 2 (GPT-6.1 Sol (medium)) | 2 rows move; largest move 2 (DeepSeek V4.1 Flash 1017 (max), GPT-6 Luna (xhigh)) |
| leave-out:lcr | 95% | evaluated | 4 rows move; largest move 1 (Claude Haiku 5.5 (high), GPT-6 Astra (high), GPT-6 Luna (max), GPT-6 Luna (xhigh)) | 4 rows move; largest move 3 (Gemini 4 Argon (high), GPT-6 Luna (xhigh)) |
| leave-out:hle | 98% | evaluated | 2 rows move; largest move 1 (Claude Haiku 5.5 (high), GPT-6 Luna (max)) | 2 rows move; largest move 1 (DeepSeek V4.1 Flash 1017 (max), MiMo-V2.6-Pro) |
| leave-out:scicode | 98% | evaluated | 2 rows move; largest move 1 (Claude Haiku 5.5 (high), GPT-6 Luna (max)) | 2 rows move; largest move 1 (DeepSeek V4.1 Flash 1017 (max), MiMo-V2.6-Pro) |
| leave-out:critpt | 98% | evaluated | no rank changes | 2 rows move; largest move 1 (DeepSeek V4.1 Flash 1017 (max), MiMo-V2.6-Pro) |
| leave-source-out:Artificial Analysis | 22% | not identifiable under the coverage rule | — | — |
| basket-scope | 87% | evaluated | 3 rows move; largest move 2 (GPT-6.1 Sol (medium)) | 2 rows move; largest move 2 (DeepSeek V4.1 Flash 1017 (max), GPT-6 Luna (xhigh)) |

### Cost-component removal (Terminal-Bench 4.0 (AA Index run): evaluated)

| Basis | Run | Rank changes |
|---|---|---|
| api | cost-component removal, original anchors | 10 rows move; largest move 4 (Claude Haiku 5.5 (high)) |
| api | alternative workload, recalibrated anchors | 9 rows move; largest move 4 (Claude Haiku 5.5 (high)) |
| plan | cost-component removal, original anchors; fixed-multiple arithmetic stress (not identified Plan economics for the altered workload) | 2 rows move; largest move 1 (Claude Haiku 5.5 (high), GPT-6.1 Sol (medium)) |
| plan | alternative workload, recalibrated anchors; fixed-multiple arithmetic stress (not identified Plan economics for the altered workload) | 2 rows move; largest move 1 (DeepSeek V4.1 Flash 1017 (max), Gemini 4 Argon (high)) |

### AI Coding Daily ranking: release gates

| Rule | Status | Detail |
|---|---|---|
| clip gate (E20) | passed | no basis exceeds the clipping allowance |
| cost influence flag (E91) | passed | cost not discriminating (< 10%); informational only; beta never changes (O2) |
| quality influence flag (E126) | passed | quality not discriminating (cost share > 90%); informational only |
| subset scoring (O17) | vacuous | subset rows scored on their own workload and anchors |
| partial component flag (E37) | vacuous | AA declined- or missing-task markers, or an Index reconstruction that misses AA's total (E209) |
| route dominance filter (E88) | vacuous | certifiably dearer routes set aside |
| Plan exploratory label (E61) | fired | fewer than half of Plan rows have an identified M_W |
| Plan evidence lifecycle and change detection (E18, E151, E269, O77, O79) | fired | 44 of 51 plan rows carry a possibly-superseded or expired route: claude-haiku-5-5-high@claude-max-20x, claude-haiku-5-5-high@claude-max-5x, claude-haiku-5-5-high@claude-pro, claude-haiku-5-5-medium@claude-max-20x, claude-haiku-5-5-medium@claude-max-5x, claude-haiku-5-5-medium@claude-pro, claude-opus-5-5-high@claude-max-20x, claude-opus-5-5-high@claude-max-5x, claude-opus-5-5-high@claude-pro, claude-opus-5-5-medium@claude-max-20x, claude-opus-5-5-medium@claude-max-5x, claude-opus-5-5-medium@claude-pro, gpt-5.6-luna-low@chatgpt-plus, gpt-5.6-luna-low@chatgpt-pro-100, gpt-5.6-luna-low@chatgpt-pro-200, gpt-5.6-luna-low@chatgpt-pro-500, gpt-6-astra-high@chatgpt-plus, gpt-6-astra-high@chatgpt-pro-100, gpt-6-astra-high@chatgpt-pro-200, gpt-6-astra-high@chatgpt-pro-500, gpt-6-luna-high@chatgpt-plus, gpt-6-luna-high@chatgpt-pro-100, gpt-6-luna-high@chatgpt-pro-200, gpt-6-luna-high@chatgpt-pro-500, gpt-6-luna-medium@chatgpt-plus, gpt-6-luna-medium@chatgpt-pro-100, gpt-6-luna-medium@chatgpt-pro-200, gpt-6-luna-medium@chatgpt-pro-500, gpt-6-luna-xhigh@chatgpt-plus, gpt-6-luna-xhigh@chatgpt-pro-100, gpt-6-luna-xhigh@chatgpt-pro-200, gpt-6-luna-xhigh@chatgpt-pro-500, gpt-6-luna@chatgpt-plus, gpt-6-luna@chatgpt-pro-100, gpt-6-luna@chatgpt-pro-200, gpt-6-luna@chatgpt-pro-500, gpt-6.1-sol-high@chatgpt-plus, gpt-6.1-sol-high@chatgpt-pro-100, gpt-6.1-sol-high@chatgpt-pro-200, gpt-6.1-sol-high@chatgpt-pro-500, gpt-6.1-sol-medium@chatgpt-plus, gpt-6.1-sol-medium@chatgpt-pro-100, gpt-6.1-sol-medium@chatgpt-pro-200, gpt-6.1-sol-medium@chatgpt-pro-500 |
| acknowledged accounting-fault windows (O91, O92, O93, O95, O96) | fired | 8 of 51 plan rows rest on a measurement inside an acknowledged fault window; they stay selected and yield to two concordant user reports for their own model and plan, and the transfers resting on them follow: gpt-5.6-luna-low@chatgpt-pro-500, gpt-6-astra-high@chatgpt-pro-500, gpt-6-luna-high@chatgpt-pro-500, gpt-6-luna-medium@chatgpt-pro-500, gpt-6-luna-xhigh@chatgpt-pro-500, gpt-6-luna@chatgpt-pro-500, gpt-6.1-sol-high@chatgpt-pro-500, gpt-6.1-sol-medium@chatgpt-pro-500 |
| AA cost omits a pricing term (O94, O98, O100, O106, O108, O109, O114) | fired | ranked at the published cost; compete in interval outputs and the scenario labels' BlockerSafe test over [C, factor × C] ([C, ∞) without a stated factor, O98) without a label (scenario frequencies draw them at the published cost, O114), and leave the anchor population at the next freeze: claude-haiku-5-5-high (up to 5×), claude-haiku-5-5-medium (up to 5×) |
| valuation-basis gate (E170) | passed | every ranked row is compatible as captured or after evidenced revaluation |
| source clocks and evidence freshness (O59, O60, O65, E211, E216, E217, E218) | passed | every capture is within its age gate and none after the cutoff unless its source predates the cutoff's day; the build stops otherwise |
| build-stopping evidence gates (O64, O69, O71, O75, O99, O100, O101, O103, O105-O111, E195, E204, E225) | passed | the Coding Agent Index manifest (O64), the Terminal-Bench agent list (E225), cutoff-day row dates (O69), the three-stage all-provider plan search (O71, O75), the typed change records behind every route flag and partition split, which also produce each route's label and blocking dates within its launch- and schedule-bounded span (O99, O101, O105, O107, O110, O111), the register of AA notes covering every captured one, with the chart's inventory and duplicate-entry checks, the post-O103 capture notes, the basket-chart labels and chart-level notes' named rows (O100, O103, O106, O108) and the frontier path checks (E195, E204) hold; the build stops otherwise |
| score swing gate (E177) | vacuous | first v3 release: no previous v3 release to compare |
| anchor migration (E184) | vacuous | no main-workload migration deferred |
| configuration map coverage | passed | every cohort row has a configuration-map entry |
| quality clipping audit (E110) | passed | saturation disclosed; domain violations block the build |
| full benchmark set (O36, O38) | fired | listed, not ranked: claude-sonnet-5-5, claude-opus-5-5, gpt-6.1-sol, gpt-6-astra, claude-haiku-5-5-max, claude-haiku-5-5, claude-haiku-5-5-low, claude-opus-5-5-xhigh, claude-sonnet-5-5-xhigh, gpt-6-astra-xhigh, gpt-6-luna-low, gpt-6.1-sol-xhigh, mimo-v2-6-flash, minimax-m3-1-flash |
| missing-leaf rules (O8 provisional, E198b, E201b, E219, E221, E226) | vacuous | no ranked row has a missing leaf (O36) |
| S1M interval stream (E145) | vacuous | dormant: no ranked leaf carries a published confidence interval since O37, so S1M equals S1 (E236) |
| provider-claim label denial (E233) | vacuous | no row has a provider-claimed leaf |
| scenario outputs current (E72) | passed | scenario input hash matches the scored inputs |

## Common-leaf ranking (diagnostic)

Diagnostic only (O121): every configuration with AA's leaves and Bug Hunt, at any effort, scored on the ten leaves the two leading rankings share; it earns no label and never holds a release. Anchor version `v3-2026-10-25-common`; leaves: FrontierCode 1.1 25%, Terminal-Bench 4.0 (AA run) 20%, Bug Hunt Bench 15% (software engineering 60%), plus the 7 leaves outside software engineering every ranking shares.

**Diagnostic ranking (O121).** It earns no interval or scenario label and its clip gate (would hold on its own) never holds the release. Its bars sit at the same ladder positions as the leading rankings' but at its own levels, so the comparison below asks whether a configuration the leading rankings cannot rank would answer the same question.

| Basis | Bar position | Cheapest here | Cheapest, max-effort ranking | Cheapest, AI Coding Daily ranking |
|---|---|---|---|---|
| API | median | GPT-6.1 Sol (medium) | GPT-6.1 Sol (max) (differs) | MiMo-V2.6-Pro (differs) |
| API | lower quartile | Claude Haiku 5.5 (high) | DeepSeek V4.1 Flash 1017 (max) (differs) | Claude Haiku 5.5 (medium) (differs) |
| API | upper quartile | GPT-6.1 Sol (max) | GPT-6 Astra (max) (differs) | Claude Opus 5.5 (medium) (differs) |
| Plan | median | Claude Opus 5.5 (medium) on Claude Pro | GPT-6.1 Sol (max) on ChatGPT Pro 500 (differs) | Claude Opus 5.5 (medium) on Claude Pro |
| Plan | lower quartile | Claude Haiku 5.5 (high) on Claude Pro | GPT-6.1 Sol (max) on ChatGPT Pro 500 (differs) | Claude Haiku 5.5 (medium) on Claude Pro (differs) |
| Plan | upper quartile | Claude Opus 5.5 (high) on Claude Pro | Claude Sonnet 5.5 (max) on Claude Pro (differs) | Claude Opus 5.5 (medium) on Claude Pro (differs) |

| Configuration | Plan rank | Plan value | Plan cost score | API rank | API value | API cost score | Quality | Quality coverage | Workload |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| [Claude Opus 5.5 (medium)](https://valuerank.alolabs.dev/models/claude-opus-5-5-medium/) | 1 | 56.17 | 61.96 | 8 | 48.25 | 30.28 | 54.24 | 100% | main |
| [Claude Opus 5.5 (high)](https://valuerank.alolabs.dev/models/claude-opus-5-5-high/) | 2 | 56.16 | 58.80 | 9 | 48.09 | 26.49 | 55.28 | 100% | main |
| [Claude Opus 5.5 (xhigh)](https://valuerank.alolabs.dev/models/claude-opus-5-5-xhigh/) | 5 | 56.09 | 51.77 | 11 | 47.66 | 18.06 | 57.53 | 100% | main |
| [Claude Sonnet 5.5 (max)](https://valuerank.alolabs.dev/models/claude-sonnet-5-5/) | 10 | 55.68 | 46.96 | 13 | 47.01 | 12.28 | 58.58 | 100% | main |
| [Claude Opus 5.5 (max)](https://valuerank.alolabs.dev/models/claude-opus-5-5/) | 13 | 55.42 | 44.91 | 14 | 46.65 | 9.82 | 58.93 | 100% | main |
| [Claude Sonnet 5.5 (xhigh)](https://valuerank.alolabs.dev/models/claude-sonnet-5-5-xhigh/) | 16 | 54.69 | 59.02 | 15 | 46.63 | 26.75 | 53.25 | 100% | main |
| [GPT-6.1 Sol (xhigh)](https://valuerank.alolabs.dev/models/gpt-6-1-sol-xhigh/) | 19 | 53.76 | 53.97 | 1 | 51.46 | 44.75 | 53.69 | 100% | main |
| [GPT-6.1 Sol (max)](https://valuerank.alolabs.dev/models/gpt-6-1-sol/) | 22 | 53.69 | 48.76 | 2 | 51.12 | 38.50 | 55.33 | 100% | main |
| [GPT-6.1 Sol (high)](https://valuerank.alolabs.dev/models/gpt-6-1-sol-high/) | 27 | 53.12 | 56.01 | 3 | 50.92 | 47.20 | 52.16 | 100% | main |
| [Claude Haiku 5.5 (xhigh)](https://valuerank.alolabs.dev/models/claude-haiku-5-5/) | 31 | 52.87 | 92.48 | 16 | 46.48 | 66.92 | 39.67 | 100% | main |
| [Claude Haiku 5.5 (max)](https://valuerank.alolabs.dev/models/claude-haiku-5-5-max/) | 34 | 52.05 | 85.62 | 20 | 45.32 | 58.69 | 40.86 | 100% | main |
| [Claude Haiku 5.5 (high)](https://valuerank.alolabs.dev/models/claude-haiku-5-5-high/) | 37 | 51.63 | 97.36 | 19 | 45.49 | 72.77 | 36.39 | 100% | main |
| [GPT-6.1 Sol (medium)](https://valuerank.alolabs.dev/models/gpt-6-1-sol-medium/) | 39 | 51.59 | 59.60 | 4 | 49.57 | 51.50 | 48.93 | 100% | main |
| [GPT-6 Astra (xhigh)](https://valuerank.alolabs.dev/models/gpt-6-astra-xhigh/) | 44 | 51.44 | 37.02 | 12 | 47.24 | 20.21 | 56.25 | 100% | main |
| [GPT-6 Astra (max)](https://valuerank.alolabs.dev/models/gpt-6-astra/) | 47 | 50.27 | 33.69 | 18 | 45.90 | 16.21 | 55.80 | 100% | main |
| [GPT-6 Astra (high)](https://valuerank.alolabs.dev/models/gpt-6-astra-high/) | 48 | 50.19 | 39.34 | 17 | 46.10 | 22.99 | 53.80 | 100% | main |
| [Claude Haiku 5.5 (medium)](https://valuerank.alolabs.dev/models/claude-haiku-5-5-medium/) | 54 | 49.20 | 100.00 | 22 | 43.93 | 78.91 | 32.27 | 100% | main |
| [GPT-6 Luna (max)](https://valuerank.alolabs.dev/models/gpt-6-luna/) | 59 | 46.49 | 75.94 | 21 | 45.29 | 71.12 | 36.68 | 100% | main |
| [Claude Haiku 5.5 (low)](https://valuerank.alolabs.dev/models/claude-haiku-5-5-low/) | 63 | 45.26 | 100.00 | 26 | 41.73 | 85.85 | 27.02 | 100% | main |
| [Kimi K3.1 Pro](https://valuerank.alolabs.dev/models/kimi-k3-1-pro/) | 66 | 45.16 | 8.18 | 6 | 48.98 | 23.44 | 57.49 | 100% | main |
| [MiMo-V2.6-Pro](https://valuerank.alolabs.dev/models/mimo-v2-6-pro/) | 67 | 44.40 | 43.53 | 5 | 49.40 | 63.52 | 44.69 | 100% | main |
| [GPT-6 Luna (xhigh)](https://valuerank.alolabs.dev/models/gpt-6-luna-xhigh/) | 69 | 44.13 | 81.56 | 23 | 43.21 | 77.87 | 31.65 | 100% | main |
| [Gemini 4 Argon (high)](https://valuerank.alolabs.dev/models/gemini-4-argon/) | 72 | 43.93 | 10.73 | 10 | 47.88 | 26.51 | 55.00 | 100% | main |
| [DeepSeek V4.1 Flash 1017 (max)](https://valuerank.alolabs.dev/models/deepseek-v4-1-flash-1017/) | 73 | 43.91 | 31.33 | 7 | 48.88 | 51.23 | 48.10 | 100% | main |
| [GPT-6 Luna (high)](https://valuerank.alolabs.dev/models/gpt-6-luna-high/) | 76 | 43.36 | 84.85 | 24 | 42.61 | 81.82 | 29.54 | 100% | main |
| [GPT-6 Luna (medium)](https://valuerank.alolabs.dev/models/gpt-6-luna-medium/) | 80 | 42.66 | 89.48 | 25 | 42.13 | 87.37 | 27.05 | 100% | main |
| [GPT-6 Luna (low)](https://valuerank.alolabs.dev/models/gpt-6-luna-low/) | 85 | 38.02 | 100.00 | 27 | 38.02 | 100.00 | 17.35 | 100% | main |
| [GPT-5.6 Luna (low)](https://valuerank.alolabs.dev/models/gpt-5-6-luna-low/) | 89 | 35.68 | 91.82 | 28 | 35.27 | 90.18 | 16.97 | 100% | main |

### Common-leaf ranking (diagnostic): quality leaf scores

| Configuration | FrontierCode 1.1 | Terminal-Bench 4.0 (AA run) | Bug Hunt Bench | GDPval-AA v2.1 | AutomationBench-AA | AA-Omniscience | AA-LCR v1.1 | Humanity's Last Exam | SciCode | CritPt | Quality | Provisional |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Claude Opus 5.5 (medium) | 57.1 | 52.5 | 28.9 | 54.3 | 61.2 | 70.2 | 84.3 | 54.7 | 59.3 | 27.7 | 54.24 | no |
| Claude Opus 5.5 (high) | 54.0 | 56.6 | 30.2 | 60.2 | 63.2 | 70.3 | 82.7 | 55.6 | 60.4 | 30.9 | 55.28 | no |
| Claude Opus 5.5 (xhigh) | 53.5 | 59.6 | 34.3 | 66.5 | 65.0 | 71.3 | 84.7 | 57.5 | 65.0 | 31.7 | 57.53 | no |
| Claude Sonnet 5.5 (max) | 45.8 | 63.6 | 48.9 | 66.9 | 71.8 | 66.2 | 82.7 | 55.0 | 61.0 | 31.4 | 58.58 | no |
| Claude Opus 5.5 (max) | 52.2 | 59.6 | 39.7 | 68.3 | 69.5 | 73.2 | 84.7 | 61.4 | 66.9 | 31.7 | 58.93 | no |
| Claude Sonnet 5.5 (xhigh) | 46.1 | 57.1 | 34.3 | 61.4 | 65.5 | 61.8 | 79.7 | 50.0 | 57.3 | 31.1 | 53.25 | no |
| GPT-6.1 Sol (xhigh) | 46.3 | 54.0 | 40.7 | 52.0 | 66.6 | 70.4 | 79.7 | 52.6 | 55.7 | 31.7 | 53.69 | no |
| GPT-6.1 Sol (max) | 49.1 | 56.1 | 42.2 | 54.8 | 64.9 | 70.8 | 83.0 | 52.9 | 54.2 | 31.7 | 55.33 | no |
| GPT-6.1 Sol (high) | 46.6 | 51.5 | 34.8 | 50.6 | 64.5 | 70.7 | 82.3 | 51.4 | 55.8 | 30.0 | 52.16 | no |
| Claude Haiku 5.5 (xhigh) | 45.5 | 29.3 | 17.4 | 50.7 | 36.0 | 53.0 | 78.3 | 42.7 | 51.7 | 22.6 | 39.67 | no |
| Claude Haiku 5.5 (max) | 41.8 | 32.8 | 20.5 | 56.0 | 35.4 | 55.3 | 82.7 | 44.4 | 55.0 | 18.9 | 40.86 | no |
| Claude Haiku 5.5 (high) | 43.6 | 21.7 | 15.2 | 45.8 | 33.7 | 52.9 | 77.3 | 37.3 | 48.7 | 18.6 | 36.39 | no |
| GPT-6.1 Sol (medium) | 43.3 | 48.0 | 27.6 | 47.5 | 62.6 | 70.0 | 83.3 | 49.9 | 53.2 | 27.7 | 48.93 | no |
| GPT-6 Astra (xhigh) | 50.6 | 59.6 | 41.0 | 52.8 | 67.2 | 71.7 | 80.0 | 54.6 | 55.7 | 31.4 | 56.25 | no |
| GPT-6 Astra (max) | 47.0 | 59.1 | 42.9 | 53.7 | 68.5 | 71.7 | 80.7 | 54.7 | 56.5 | 31.7 | 55.80 | no |
| GPT-6 Astra (high) | 50.9 | 54.0 | 33.3 | 51.2 | 66.6 | 71.9 | 80.0 | 53.1 | 55.4 | 28.9 | 53.80 | no |
| Claude Haiku 5.5 (medium) | 40.4 | 15.2 | 11.4 | 38.8 | 28.6 | 52.2 | 77.3 | 33.8 | 49.0 | 12.9 | 32.27 | no |
| GPT-6 Luna (max) | 41.9 | 12.6 | 17.4 | 46.6 | 53.2 | 50.3 | 83.3 | 38.5 | 54.6 | 19.4 | 36.68 | no |
| Claude Haiku 5.5 (low) | 29.3 | 12.6 | 10.5 | 31.1 | 22.9 | 51.6 | 72.0 | 27.0 | 49.2 | 9.1 | 27.02 | no |
| Kimi K3.1 Pro | 47.1 | 67.2 | 34.3 | 67.3 | 73.3 | 64.8 | 86.3 | 52.5 | 60.8 | 24.6 | 57.49 | no |
| MiMo-V2.6-Pro | 45.4 | 34.8 | 17.1 | 59.2 | 58.6 | 54.2 | 86.3 | 49.4 | 60.9 | 26.6 | 44.69 | no |
| GPT-6 Luna (xhigh) | 33.2 | 8.1 | 13.3 | 43.2 | 47.8 | 49.1 | 80.0 | 34.3 | 51.7 | 17.4 | 31.65 | no |
| Gemini 4 Argon (high) | 43.5 | 57.1 | 38.8 | 56.2 | 77.5 | 71.2 | 79.7 | 57.1 | 61.8 | 27.1 | 55.00 | no |
| DeepSeek V4.1 Flash 1017 (max) | 43.7 | 33.8 | 40.7 | 62.3 | 66.6 | 52.4 | 82.7 | 43.3 | 55.9 | 24.0 | 48.10 | no |
| GPT-6 Luna (high) | 32.0 | 4.5 | 8.6 | 42.1 | 47.8 | 47.2 | 79.3 | 32.9 | 50.3 | 15.4 | 29.54 | no |
| GPT-6 Luna (medium) | 31.8 | 2.5 | 3.8 | 38.1 | 40.5 | 47.5 | 78.3 | 28.3 | 50.9 | 10.6 | 27.05 | no |
| GPT-6 Luna (low) | 14.1 | 0.0 | 3.8 | 26.6 | 12.0 | 45.4 | 74.0 | 20.3 | 46.9 | 2.6 | 17.35 | no |
| GPT-5.6 Luna (low) | 15.4 | 0.0 | 3.8 | 24.7 | 11.7 | 42.7 | 70.0 | 19.8 | 46.1 | 2.6 | 16.97 | no |

### Common-leaf ranking (diagnostic): displayed record and noise

- API basis, displayed record (not a claim; E203): cheapest at or above quality 48.9: GPT-6.1 Sol (medium) ($318.05 per basket run; 15 reach it); at or above quality 36.4: Claude Haiku 5.5 (high) ($70.85 per basket run; 21 reach it); at or above quality 55.3: GPT-6.1 Sol (max) ($796.76 per basket run; 8 reach it).
- API basis, noise-margin companion (O44; each bar plus 5.2 quality points, so the bar's own configuration cannot decide it): cheapest at or above quality 54.1: GPT-6.1 Sol (max) ($796.76 per basket run); at or above quality 41.6: MiMo-V2.6-Pro ($136.13 per basket run); at or above quality 60.5: none.
- Plan basis, displayed record (not a claim; E203): cheapest at or above quality 48.9: Claude Opus 5.5 (medium) on Claude Pro ($24.17 per basket run; 48 reach it); at or above quality 36.4: Claude Haiku 5.5 (high) on Claude Pro ($1.20 per basket run; 66 reach it); at or above quality 55.3: Claude Opus 5.5 (high) on Claude Pro ($31.58 per basket run; 25 reach it).
- Plan basis, noise-margin companion (O44; each bar plus 5.2 quality points, so the bar's own configuration cannot decide it): cheapest at or above quality 54.1: Claude Opus 5.5 (medium) on Claude Pro ($24.17 per basket run); at or above quality 41.6: Claude Opus 5.5 (medium) on Claude Pro ($24.17 per basket run); at or above quality 60.5: none.
- Safety-refusal flags (O63; costs and scores unchanged) on these bars' cheapest rows: GPT-6.1 Sol (max) (15 blocked and 0 fallback attempts of 870).
- AA cost caveat (O94; ranked at the published cost, no label of its own) on these bars' cheapest rows: Claude Haiku 5.5 (high) (AA's cost omits a pricing term; up to 5× on its cost).
- Plan route flags on these bars' cheapest plan rows: Claude Haiku 5.5 (high) on Claude Pro (possibly-superseded); Claude Opus 5.5 (high) on Claude Pro (possibly-superseded); Claude Opus 5.5 (medium) on Claude Pro (possibly-superseded).
- These outputs compare ranked configurations only; listed families shown with an indicative value (O41) are outside them (O43): MiMo-V2.6-Flash, MiniMax-M3.1-Flash.

Benchmark sampling noise (O39, an independent-task approximation): two values must differ by about 3.9 value points (median, 95%) to separate, and 2 of 27 adjacent API ranks and 2 of 48 adjacent Plan ranks of different configurations do (43 more adjacent Plan pairs are one configuration on two plans, ordered by the plans' multiples alone; E258). Its net direction is not established: every configuration is scored on the same tasks, which correlates their errors and narrows the true threshold (API 2 at correlation 0.3, 2 at correlation 0.6; Plan 2 at correlation 0.3, 2 at correlation 0.6), while sources it leaves out widen it (run-to-run and harness variance, AA's single cost run and, for the 49 Plan rows on an owner assumption (45 owner-named transfers and 4 O46 provider quota ceilings), that assumption's error). The noise band column groups each row with the band's first row it cannot be told apart from (O42); a Plan band marked † rests on an owner assumption (an owner-named transfer or an O46 provider quota ceiling) and excludes its error: an assumed multiple can be wrong by a factor of about 3.8 before the row's value moves by the median threshold (a tolerance, not an estimate of the assumption's error). The S1T scenario shares in [scores.md](scores.md) show each row's rank-1 and top-3 frequencies under that noise.


**Listed frontier families: indicative value, not ranked and not comparable (O41).** Quality is the mean over the leaves the configuration has, renormalised, with no imputation, so these values cannot be compared with the ranking above.

| Configuration | Missing | Quality (remaining leaves) | Quality coverage | Plan value (indicative) | API value (indicative) | API cost (USD per basket run) | Plan cost (USD per basket run) |
|---|---|---:|---:|---:|---:|---:|---:|
| MiMo-V2.6-Flash | Bug Hunt Bench | 43.2 | 85% | 45.6 | 51.2 | $60.37 | $52.59 |
| MiniMax-M3.1-Flash | Bug Hunt Bench | 45.5 | 85% | 42.9 | 48.1 | $234.35 | $234.35 |

### Common-leaf ranking (diagnostic): Plan routes and calibration

#### Measured-evidence calibration (diagnostic)

References: each workload's measured-only rows with complete cost evidence are the references: c_L = cheapest / 2, c_H = dearest x 2 (diagnostic only; the official anchors are unchanged). Status: evaluated.

- Workload `1453a9a0576b02ea`: measured anchors $12.09 to $530.83 from Claude Opus 5.5 (max), Claude Opus 5.5 (high), Claude Opus 5.5 (medium), Claude Opus 5.5 (xhigh), GPT-6 Astra (max), GPT-6 Astra (high), GPT-6 Astra (xhigh), GPT-6.1 Sol (max), GPT-6.1 Sol (high), GPT-6.1 Sol (medium), GPT-6.1 Sol (xhigh); anchor ratio 43.9 against the official 4799.4. Official Plan anchors are set by GPT-5.6 Luna (low) on ChatGPT Pro 500 (owner-named transfer) at the low end and Kimi K3.1 Pro on API-cost fallback at the high end.

| Configuration | Value on official Plan anchors | Value on measured anchors | Rank change |
|---|---:|---:|---:|
| Claude Opus 5.5 (high) ‡ | 56.16 | 60.11 | 0 |
| Claude Opus 5.5 (max) | 55.42 | 55.06 | 3 |
| Claude Opus 5.5 (medium) ‡ | 56.17 | 61.10 | 0 |
| Claude Opus 5.5 (xhigh) ‡ | 56.09 | 57.86 | 0 |
| GPT-6 Astra (high) ‡ | 50.19 | 48.10 | -1 |
| GPT-6 Astra (max) | 50.27 | 46.43 | 1 |
| GPT-6 Astra (xhigh) ‡ | 51.44 | 48.64 | 0 |
| GPT-6.1 Sol (high) ‡ | 53.12 | 56.20 | -2 |
| GPT-6.1 Sol (max) | 53.69 | 54.52 | 2 |
| GPT-6.1 Sol (medium) ‡ | 51.59 | 55.79 | -2 |
| GPT-6.1 Sol (xhigh) ‡ | 53.76 | 56.22 | -1 |

Pairwise reversals: Claude Opus 5.5 (max) and GPT-6.1 Sol (high); Claude Opus 5.5 (max) and GPT-6.1 Sol (medium); Claude Opus 5.5 (max) and GPT-6.1 Sol (xhigh); GPT-6 Astra (max) and GPT-6 Astra (high); GPT-6.1 Sol (max) and GPT-6.1 Sol (high); GPT-6.1 Sol (max) and GPT-6.1 Sol (medium). Largest value change: 4.93 points.

‡ measured on the same model at another effort (an O88 route; measured evidence under O90).

### Common-leaf ranking (diagnostic): interval outputs

**API basis, main workload: frontier.** Not evaluable: none. Competing without a label of its own (E183): Claude Haiku 5.5 (xhigh): AA's cost omits a pricing term (O94); competes over its published cost up to the stated factor; Claude Haiku 5.5 (high): AA's cost omits a pricing term (O94); competes over its published cost up to the stated factor; Claude Haiku 5.5 (low): AA's cost omits a pricing term (O94); competes over its published cost up to the stated factor; Claude Haiku 5.5 (max): AA's cost omits a pricing term (O94); competes over its published cost up to the stated factor; Claude Haiku 5.5 (medium): AA's cost omits a pricing term (O94); competes over its published cost up to the stated factor.

| Configuration | Possible frontier | Definite frontier | Definite counterexample | Possible frontier blocked by |
|---|---|---|---|---|
| Claude Sonnet 5.5 (max) | certified | certified | — | — |
| Claude Opus 5.5 (max) | certified | certified | — | — |
| DeepSeek V4.1 Flash 1017 (max) | disproved | disproved | GPT-6.1 Sol (medium) | GPT-6.1 Sol (medium) |
| GPT-6.1 Sol (max) | certified | certified | — | — |
| Gemini 4 Argon (high) | disproved | disproved | GPT-6.1 Sol (max) | GPT-6.1 Sol (max) |
| GPT-6 Astra (max) | disproved | disproved | Kimi K3.1 Pro | Kimi K3.1 Pro, Claude Opus 5.5 (xhigh), GPT-6 Astra (xhigh) |
| Kimi K3.1 Pro | certified | certified | — | — |
| GPT-6.1 Sol (high) | certified | certified | — | — |
| Claude Opus 5.5 (high) | disproved | disproved | GPT-6.1 Sol (max) | GPT-6.1 Sol (max) |
| MiMo-V2.6-Pro | certified | certified | — | — |
| Claude Opus 5.5 (medium) | disproved | disproved | GPT-6.1 Sol (max) | GPT-6.1 Sol (max) |
| GPT-6.1 Sol (medium) | certified | certified | — | — |
| GPT-6 Astra (high) | disproved | disproved | GPT-6.1 Sol (max) | GPT-6.1 Sol (max), Gemini 4 Argon (high), Kimi K3.1 Pro, Claude Opus 5.5 (high), Claude Opus 5.5 (medium) |
| GPT-6 Luna (max) | certified | certified | — | — |
| GPT-6 Luna (xhigh) | certified | disproved | Claude Haiku 5.5 (medium) | — |
| GPT-6 Luna (high) | certified | certified | — | — |
| GPT-6 Luna (medium) | certified | certified | — | — |
| GPT-5.6 Luna (low) | disproved | disproved | GPT-6 Luna (low) | GPT-6 Luna (low) |
| Claude Opus 5.5 (xhigh) | certified | certified | — | — |
| Claude Sonnet 5.5 (xhigh) | disproved | disproved | GPT-6.1 Sol (max) | GPT-6.1 Sol (max), Claude Opus 5.5 (medium), GPT-6.1 Sol (xhigh) |
| GPT-6 Astra (xhigh) | disproved | disproved | Kimi K3.1 Pro | Kimi K3.1 Pro |
| GPT-6 Luna (low) | certified | certified | — | — |
| GPT-6.1 Sol (xhigh) | certified | certified | — | — |

**API basis, main workload: cheapest at or above quality 48.9** (lower-median displayed quality of the non-provisional cohort configurations at freeze (E192; headline bar)). Status certified; confirmed cheapest: none.

Configurations that can be confirmed to qualify: 14 (confirmation needs the full-composite lower bound, with missing leaves at 0, to clear the bar; O25). Cheaper same-family configurations on AA's chart that were not evaluated (not ranked in this ranking: lacking its full benchmark set, or not plotted on or near the frontier; E201c, O51): GPT-6.1 Sol (high): GPT-6.1 Sol (low); GPT-6.1 Sol (medium): GPT-6.1 Sol (low).

Bar comparison: compares 15 configurations that can qualify. The bar is a displayed-quality level; qualification tests each row's full-composite bounds, so a row above the bar on displayed quality can still fail to qualify confirmed when leaves are missing (E198).

| Configuration | Displayed quality − bar | Confirmed qualifies | Possibly qualifies | Possibly cheapest |
|---|---:|---|---|---|
| Claude Sonnet 5.5 (max) | 9.7 | certified | certified | disproved |
| Claude Opus 5.5 (max) | 10.0 | certified | certified | disproved |
| DeepSeek V4.1 Flash 1017 (max) | -0.8 | disproved | disproved | disproved |
| GPT-6.1 Sol (max) | 6.4 | certified | certified | disproved |
| Gemini 4 Argon (high) | 6.1 | certified | certified | disproved |
| GPT-6 Astra (max) | 6.9 | certified | certified | disproved |
| Kimi K3.1 Pro | 8.6 | certified | certified | disproved |
| GPT-6.1 Sol (high) | 3.2 | certified | certified | certified |
| Claude Opus 5.5 (high) | 6.4 | certified | certified | disproved |
| MiMo-V2.6-Pro | -4.2 | disproved | disproved | disproved |
| Claude Opus 5.5 (medium) | 5.3 | certified | certified | disproved |
| GPT-6.1 Sol (medium) | 0.0 | disproved | certified | certified |
| GPT-6 Astra (high) | 4.9 | certified | certified | disproved |
| GPT-6 Luna (max) | -12.2 | disproved | disproved | disproved |
| GPT-6 Luna (xhigh) | -17.3 | disproved | disproved | disproved |
| GPT-6 Luna (high) | -19.4 | disproved | disproved | disproved |
| GPT-6 Luna (medium) | -21.9 | disproved | disproved | disproved |
| GPT-5.6 Luna (low) | -32.0 | disproved | disproved | disproved |
| Claude Opus 5.5 (xhigh) | 8.6 | certified | certified | disproved |
| Claude Sonnet 5.5 (xhigh) | 4.3 | certified | certified | disproved |
| GPT-6 Astra (xhigh) | 7.3 | certified | certified | disproved |
| GPT-6 Luna (low) | -31.6 | disproved | disproved | disproved |
| GPT-6.1 Sol (xhigh) | 4.8 | certified | certified | disproved |

**API basis, main workload: cheapest at or above quality 36.4** (lower-quartile displayed quality of the non-provisional cohort configurations at freeze (O34)). Status certified; confirmed cheapest: none.

Configurations that can be confirmed to qualify: 18 (confirmation needs the full-composite lower bound, with missing leaves at 0, to clear the bar; O25). Cheaper same-family configurations on AA's chart that were not evaluated (not ranked in this ranking: lacking its full benchmark set, or not plotted on or near the frontier; E201c, O51): GPT-6 Luna (max): GPT-6 Luna (non-reasoning).

Bar comparison: compares 18 configurations that can qualify. The bar is a displayed-quality level; qualification tests each row's full-composite bounds, so a row above the bar on displayed quality can still fail to qualify confirmed when leaves are missing (E198).

| Configuration | Displayed quality − bar | Confirmed qualifies | Possibly qualifies | Possibly cheapest |
|---|---:|---|---|---|
| Claude Sonnet 5.5 (max) | 22.2 | certified | certified | disproved |
| Claude Opus 5.5 (max) | 22.5 | certified | certified | disproved |
| DeepSeek V4.1 Flash 1017 (max) | 11.7 | certified | certified | disproved |
| GPT-6.1 Sol (max) | 18.9 | certified | certified | disproved |
| Gemini 4 Argon (high) | 18.6 | certified | certified | disproved |
| GPT-6 Astra (max) | 19.4 | certified | certified | disproved |
| Kimi K3.1 Pro | 21.1 | certified | certified | disproved |
| GPT-6.1 Sol (high) | 15.8 | certified | certified | disproved |
| Claude Opus 5.5 (high) | 18.9 | certified | certified | disproved |
| MiMo-V2.6-Pro | 8.3 | certified | certified | disproved |
| Claude Opus 5.5 (medium) | 17.8 | certified | certified | disproved |
| GPT-6.1 Sol (medium) | 12.5 | certified | certified | disproved |
| GPT-6 Astra (high) | 17.4 | certified | certified | disproved |
| GPT-6 Luna (max) | 0.3 | certified | certified | certified |
| GPT-6 Luna (xhigh) | -4.7 | disproved | disproved | disproved |
| GPT-6 Luna (high) | -6.9 | disproved | disproved | disproved |
| GPT-6 Luna (medium) | -9.3 | disproved | disproved | disproved |
| GPT-5.6 Luna (low) | -19.4 | disproved | disproved | disproved |
| Claude Opus 5.5 (xhigh) | 21.1 | certified | certified | disproved |
| Claude Sonnet 5.5 (xhigh) | 16.9 | certified | certified | disproved |
| GPT-6 Astra (xhigh) | 19.9 | certified | certified | disproved |
| GPT-6 Luna (low) | -19.0 | disproved | disproved | disproved |
| GPT-6.1 Sol (xhigh) | 17.3 | certified | certified | disproved |

**API basis, main workload: cheapest at or above quality 55.3** (upper-quartile displayed quality of the non-provisional cohort configurations at freeze (O34)). Status certified; confirmed cheapest: GPT-6.1 Sol (max).

Configurations that can be confirmed to qualify: 7 (confirmation needs the full-composite lower bound, with missing leaves at 0, to clear the bar; O25). Cheaper same-family configurations on AA's chart that were not evaluated (not ranked in this ranking: lacking its full benchmark set, or not plotted on or near the frontier; E201c, O51): GPT-6.1 Sol (max): GPT-6.1 Sol (low).

Bar comparison: compares 8 configurations that can qualify. The bar is a displayed-quality level; qualification tests each row's full-composite bounds, so a row above the bar on displayed quality can still fail to qualify confirmed when leaves are missing (E198).

| Configuration | Displayed quality − bar | Confirmed qualifies | Possibly qualifies | Possibly cheapest |
|---|---:|---|---|---|
| Claude Sonnet 5.5 (max) | 3.3 | certified | certified | disproved |
| Claude Opus 5.5 (max) | 3.6 | certified | certified | disproved |
| DeepSeek V4.1 Flash 1017 (max) | -7.2 | disproved | disproved | disproved |
| GPT-6.1 Sol (max) | 0.0 | certified | certified | certified |
| Gemini 4 Argon (high) | -0.3 | disproved | disproved | disproved |
| GPT-6 Astra (max) | 0.5 | certified | certified | disproved |
| Kimi K3.1 Pro | 2.2 | certified | certified | disproved |
| GPT-6.1 Sol (high) | -3.1 | disproved | disproved | disproved |
| Claude Opus 5.5 (high) | 0.0 | disproved | certified | disproved |
| MiMo-V2.6-Pro | -10.6 | disproved | disproved | disproved |
| Claude Opus 5.5 (medium) | -1.0 | disproved | disproved | disproved |
| GPT-6.1 Sol (medium) | -6.4 | disproved | disproved | disproved |
| GPT-6 Astra (high) | -1.5 | disproved | disproved | disproved |
| GPT-6 Luna (max) | -18.6 | disproved | disproved | disproved |
| GPT-6 Luna (xhigh) | -23.6 | disproved | disproved | disproved |
| GPT-6 Luna (high) | -25.7 | disproved | disproved | disproved |
| GPT-6 Luna (medium) | -28.2 | disproved | disproved | disproved |
| GPT-5.6 Luna (low) | -38.3 | disproved | disproved | disproved |
| Claude Opus 5.5 (xhigh) | 2.2 | certified | certified | disproved |
| Claude Sonnet 5.5 (xhigh) | -2.0 | disproved | disproved | disproved |
| GPT-6 Astra (xhigh) | 1.0 | certified | certified | disproved |
| GPT-6 Luna (low) | -37.9 | disproved | disproved | disproved |
| GPT-6.1 Sol (xhigh) | -1.6 | disproved | disproved | disproved |

**Plan basis, main workload:** not evaluated (no row has FullCost and an identified M_W (E61/E67)).

### Common-leaf ranking (diagnostic): scenario shares

The scenario panel is the 28 rows scored on the main workload (E96, E266).

Scenario outputs are stale (inputs changed since the scenario run); no shares are published for this release.

### Common-leaf ranking (diagnostic): diagnostics

- **Terminal-Bench cross-source agreement (AA's mini-SWE-agent run against tbench.ai):** defined; 0 rows take the leaf from tbench.ai (gap fill).
- **Rank separability (O39, independent-task approximation):** median separation 3.86 value points (API) and 3.93 (Plan); separable adjacent ranks: API 2 of 27, Plan 2 of 48. Assumptions: tasks are independent and each leaf's score is a mean over its published task count (plug-in binomial with the proportion (k + 1/2) / (n + 1), I28); attempts averaged within a task and tasks shared across models are ignored, so the noise is approximate; GDPval-AA: each row's rating interval as AA's model page displays it, read as a 95% normal interval (AA states no level), SD = half-width / 1.96; AA-Omniscience: each of 6,000 questions scores +1, 0 or -1, with the shares from AA's accuracy and hallucination rate; Vals boards (Vibe Code Bench v1.1, Code Migration v1.1): Vals' published standard error per record, read as the leaf's SD; AI Coding Daily: judged points over its six graded projects read as a binomial share of 60 points (an assumption; the board publishes no error).
- **FrontierCode against Cognition:** FrontierCode cross-source agreement (AA against Cognition, same name and effort; E234): Kendall tau 0.77 (interval 0.58 to 0.91) on 22 rows. Cognition minus AA: mean +2.6 points, largest 11.6.
- **Gap-fill removal (E234, diagnostic; scores unchanged):** with these leaves removed and the rest renormalised — GPT-6 Astra (high) (FrontierCode 1.1); GPT-5.6 Luna (low) (FrontierCode 1.1); GPT-6 Astra (xhigh) (FrontierCode 1.1) — API 9 rows move; largest move 4 (GPT-6 Astra (xhigh)); Plan 6 rows move; largest move 3 (GPT-6 Astra (xhigh)).
- **Bar results without the gap fills (E234, sensitivity; labels unchanged):** cheapest displayed row as published, with fills removed, and with third-party fills lowered by the mean offset 2.6 points — API quality 48.9: GPT-6.1 Sol (medium) in all three; API quality 36.4: Claude Haiku 5.5 (high) in all three; API quality 55.3: GPT-6.1 Sol (max) in all three; Plan quality 48.9: Claude Opus 5.5 (medium) in all three; Plan quality 36.4: Claude Haiku 5.5 (high) in all three; Plan quality 55.3: Claude Opus 5.5 (high) in all three.
- **Harness cost (O123, S2 stress):** unevaluable: no model is listed under two or more agents in AA's Coding Agent Index capture, so no agent effect is identified (O123). Coding Agent Index agents (each part of its costed configuration; none is the run behind the FrontierCode or Terminal-Bench leaf): Claude Sonnet 5.5 (max): Claude Code; Claude Opus 5.5 (max): Claude Code; DeepSeek V4.1 Flash 1017 (max): DeepSeek Harness; GPT-6.1 Sol (max): Codex; Gemini 4 Argon (high): Antigravity CLI; GPT-6 Astra (max): Codex; Claude Haiku 5.5 (max): Claude Code; GPT-6 Luna (max): Codex.
- **Quality agreement:** quality agreement (matched-panel sensitivity): Kendall tau 0.73 (interval 0.53 to 0.86) on 28 rows.
- **Quality-substitution value agreement (API):** quality-substitution value agreement, api basis (matched-panel sensitivity): Kendall tau 0.50 (interval 0.22 to 0.73) on 28 rows.
- **Quality-substitution value agreement (Plan):** quality-substitution value agreement, plan basis (matched-panel sensitivity): Kendall tau 0.62 (interval 0.42 to 0.80) on 28 rows.
- **Disjoint-evidence agreement:** disjoint-evidence agreement (restricted evidence comparison, not an eligible ranking): Kendall tau 0.66 (interval 0.44 to 0.82) on 28 rows.
- **Quality source shares:** AA-run 85%, independent 15%.
- **Non-discriminating leaves:** none.
- **Group drift:** estimated; flagged: knowledge.
- **Omniscience abstention sensitivity** (z_pen = max(0, I)): 15 rows move; largest move 4 (DeepSeek V4.1 Flash 1017 (max)).
- **GDPval-AA logistic sensitivity** (z = 100 / (1 + 10^((1600 - E) / 400)) against AA's pinned anchor; every other input fixed): API 18 rows move; largest move 5 (GPT-6.1 Sol (medium)); Plan 16 rows move; largest move 4 (Claude Haiku 5.5 (low), Claude Opus 5.5 (medium)).
- **Anchor stability:** trimmed anchors (P10 / 2 and P90 x 2 (diagnostic only)) give $16.88 to $8,426.69; 18 rows move; largest move 6 (Claude Haiku 5.5 (high), GPT-6 Luna (max)).

- **Basket readiness (E22):** priced leaves cover 47% of nominal quality weight (AutomationBench-AA, GDPval-AA v2.1, AA-LCR v1.1, SciCode, Terminal-Bench 4.0 (AA run)); pending components: Coding Agent Index, FrontierCode 1.1, ITBench-AA.
- **SWE cost companion (O14, diagnostic):** 8 rows evaluated; flagged far from the median ratio: Gemini 4 Argon (high), Claude Haiku 5.5 (max).
- **Matched-cost diagnostic (E55):** evaluated at 60% priced quality weight; basket/matched cost-order reversals with separated intervals: 3; rank-gap warnings: 0.
- **Frontier-families anchors (E187, diagnostic):** anchors rebuilt from the 28 frontier and near-frontier references move API 10 rows move; largest move 2 (Claude Haiku 5.5 (xhigh), Kimi K3.1 Pro) (value points per cost doubling 2.17 vs 2.45 frozen); Plan 19 rows move; largest move 4 (Claude Haiku 5.5 (high), GPT-6 Astra (xhigh)) (value points per cost doubling 1.76 vs 2.04 frozen).
- **Frontier-families bar (E199, sensitivity; the frozen bar stays primary):** quality 48.9 over 28 configurations; cheapest at or above it on the API main workload: not unique; possibly GPT-6.1 Sol (high), GPT-6.1 Sol (medium) (compares 15 configurations that can qualify).
- **One row per family (E205, diagnostic; the frozen ladder and anchors stay primary):** with each family's primary configuration only (11 rows in the one-row-per-family bar population), the ladder (headline, lower quartile, upper quartile) would be 53.8 / 39.7 / 55.3 against 48.9 / 36.4 / 55.3 frozen; anchors rebuilt from its 11 references move API no rank changes (value points per cost doubling 2.45 vs 2.45 frozen); Plan 2 rows move; largest move 1 (Claude Haiku 5.5 (high), GPT-6.1 Sol (medium)) (value points per cost doubling 2.03 vs 2.04 frozen).
- **Ladder over scored rows (I28, sensitivity; the frozen ladder stays primary):** the bar population keeps full-benchmark rows that have no cost; today every such row has a cost, so the ladder is unchanged.
- **Bar currency (E207, informational):** rows reaching each frozen bar: quality 48.9: 15 of 28; quality 36.4: 21 of 28; quality 55.3: 8 of 28; the current population would freeze 48.9 / 32.3 / 55.3; lifetime until the next anchor re-freeze or methodology version, whichever comes first; no staleness flag.
- **Token mix (E208):** 1 selected routes: mix not reported: the measurement publishes no token-category shares; 24 selected routes: mix unidentified: the basket's token-category shares are set-identified only (E124), so the L1 test (above 0.30 flags mix-unmatched) is not computed.
- **Observed-range sensitivity (E219, not evidence; no label changes):** with each missing leaf inside the cohort's observed range for that leaf, quality 48.9: 15 can qualify, 14 confirmed; possibly cheapest GPT-6.1 Sol (high), GPT-6.1 Sol (medium); quality 36.4: 18 can qualify, 18 confirmed; possibly cheapest GPT-6 Luna (max); quality 55.3: 8 can qualify, 7 confirmed; GPT-6.1 Sol (max) confirmed cheapest.
- **What would settle the headline bar (E221, not a claim):** rows that can but need not reach quality 48.9, with the mean score their missing leaves would need: GPT-6.1 Sol (medium) (no missing leaf; reporting precision only).
- **Common leaf set (E226, diagnostic; scores unchanged):** without the leaves fewer than 90% of cohort rows have (none), API no rank changes; Plan no rank changes; rows reaching each bar: quality 48.9: 15 → 15; quality 36.4: 21 → 21; quality 55.3: 8 → 8; rows whose displayed quality differs from common-leaf quality by more than one cost doubling's worth: none.
- **Harness by leaf (E227):** Terminal-Bench: mini-SWE-agent 28; Bug Hunt: Codex CLI 13, Claude Code 11, Antigravity CLI 1, Claude Code / Anthropic-compatible shim 1, Claude Code / Moonshot API 1, DeepSeek Harness / DeepSeek API 1.
- **Coding Agent Index safety refusals (O63, flagged; costs and scores unchanged):** Claude Sonnet 5.5 (45 finished by Claude Opus 4.8 of 870 attempts); Claude Opus 5.5 (76 finished by Claude Opus 4.8 or Claude Opus 5 of 870 attempts); GPT-6.1 Sol (15 blocked of 870 attempts); GPT-6 Astra (13 blocked of 870 attempts); Claude Haiku 5.5 (max) (3 finished by Claude Opus 5 of 870 attempts).

### Leave-one-component-out cost family (E172)

Each admitted basket unit removed in turn, scored on anchors rebuilt by the freeze rule (rank changes against the primary ranking; quality held fixed).

| Removed component | API rank changes | Plan rank changes | API value points per cost doubling |
|---|---|---|---:|
| AA-Briefcase | 16 rows move; largest move 3 (DeepSeek V4.1 Flash 1017 (max)) | 18 rows move; largest move 4 (Claude Haiku 5.5 (high)) | 2.26 |
| GDPval-AA | 12 rows move; largest move 3 (Claude Opus 5.5 (medium), Claude Opus 5.5 (xhigh)) | 20 rows move; largest move 4 (Claude Haiku 5.5 (high), Claude Opus 5.5 (medium), GPT-6 Astra (xhigh)) | 2.26 |
| GDP.pdf | 13 rows move; largest move 3 (MiMo-V2.6-Pro) | 18 rows move; largest move 4 (Claude Haiku 5.5 (high), GPT-6 Astra (xhigh)) | 2.12 |
| AutomationBench-AA | 13 rows move; largest move 6 (MiMo-V2.6-Pro) | 14 rows move; largest move 4 (Claude Haiku 5.5 (xhigh), Claude Haiku 5.5 (high), Claude Haiku 5.5 (max), GPT-6 Astra (high), GPT-6 Astra (xhigh)) | 2.06 |
| Terminal-Bench 4.0 (AA Index run) | 11 rows move; largest move 2 (Claude Haiku 5.5 (xhigh), GPT-6 Astra (max), Kimi K3.1 Pro) | 19 rows move; largest move 4 (Claude Haiku 5.5 (high), Gemini 4 Argon (high), GPT-6 Astra (xhigh)) | 2.21 |
| SciCode | 9 rows move; largest move 2 (Claude Haiku 5.5 (xhigh), GPT-6 Astra (max), Kimi K3.1 Pro) | 19 rows move; largest move 4 (Claude Haiku 5.5 (high), GPT-6 Astra (xhigh)) | 2.18 |
| AA-LCR | 13 rows move; largest move 2 (Claude Haiku 5.5 (xhigh), DeepSeek V4.1 Flash 1017 (max), Kimi K3.1 Pro) | 18 rows move; largest move 4 (Claude Haiku 5.5 (high), GPT-6 Astra (xhigh)) | 2.15 |

### Subset rows: paired bridge and missing spend (E10, E173)

No row is scored on a subset workload.

### Deletion sensitivity

| Branch | Retained nominal weight | Status | API rank changes | Plan rank changes |
|---|---:|---|---|---|
| leave-out:frontierCode | 75% | evaluated | 21 rows move; largest move 8 (Claude Opus 5.5 (medium)) | 21 rows move; largest move 6 (Claude Opus 5.5 (medium)) |
| leave-out:terminalBench | 80% | evaluated | 24 rows move; largest move 15 (GPT-6 Luna (max)) | 23 rows move; largest move 6 (Kimi K3.1 Pro) |
| leave-out:bugHunt | 85% | evaluated | 17 rows move; largest move 4 (Claude Haiku 5.5 (xhigh), Claude Sonnet 5.5 (max), DeepSeek V4.1 Flash 1017 (max)) | 16 rows move; largest move 3 (Claude Haiku 5.5 (xhigh)) |
| leave-out:gdpval | 90% | evaluated | 17 rows move; largest move 3 (Claude Opus 5.5 (max), Claude Opus 5.5 (medium), GPT-6 Astra (max), GPT-6 Astra (high)) | 7 rows move; largest move 3 (Claude Haiku 5.5 (max), GPT-6 Astra (xhigh)) |
| leave-out:automationBench | 90% | evaluated | 20 rows move; largest move 5 (Claude Haiku 5.5 (xhigh), Claude Haiku 5.5 (max)) | 13 rows move; largest move 3 (Claude Haiku 5.5 (xhigh)) |
| leave-out:omniscience | 90% | evaluated | 9 rows move; largest move 3 (GPT-6.1 Sol (medium)) | 16 rows move; largest move 3 (Claude Haiku 5.5 (low), Claude Opus 5.5 (medium), Claude Sonnet 5.5 (max), DeepSeek V4.1 Flash 1017 (max)) |
| leave-out:lcr | 95% | evaluated | 4 rows move; largest move 1 (Claude Haiku 5.5 (xhigh), GPT-6 Astra (high), Kimi K3.1 Pro, MiMo-V2.6-Pro) | 12 rows move; largest move 3 (GPT-6 Astra (xhigh)) |
| leave-out:hle | 98% | evaluated | 2 rows move; largest move 1 (Claude Opus 5.5 (max), Claude Sonnet 5.5 (xhigh)) | 2 rows move; largest move 1 (DeepSeek V4.1 Flash 1017 (max), Gemini 4 Argon (high)) |
| leave-out:scicode | 98% | evaluated | 2 rows move; largest move 1 (Claude Opus 5.5 (max), Claude Sonnet 5.5 (xhigh)) | 4 rows move; largest move 1 (Claude Haiku 5.5 (high), Claude Haiku 5.5 (low), GPT-6.1 Sol (medium), Kimi K3.1 Pro) |
| leave-out:critpt | 98% | evaluated | no rank changes | 4 rows move; largest move 1 (Claude Haiku 5.5 (high), Claude Haiku 5.5 (low), GPT-6.1 Sol (medium), Kimi K3.1 Pro) |
| leave-source-out:Artificial Analysis | 15% | not identifiable under the coverage rule | — | — |
| basket-scope | 87% | evaluated | 11 rows move; largest move 3 (DeepSeek V4.1 Flash 1017 (max), GPT-6.1 Sol (medium)) | 15 rows move; largest move 4 (DeepSeek V4.1 Flash 1017 (max)) |

### Cost-component removal (Terminal-Bench 4.0 (AA Index run): evaluated)

| Basis | Run | Rank changes |
|---|---|---|
| api | cost-component removal, original anchors | 14 rows move; largest move 3 (Claude Haiku 5.5 (xhigh)) |
| api | alternative workload, recalibrated anchors | 11 rows move; largest move 2 (Claude Haiku 5.5 (xhigh), GPT-6 Astra (max), Kimi K3.1 Pro) |
| plan | cost-component removal, original anchors; fixed-multiple arithmetic stress (not identified Plan economics for the altered workload) | 4 rows move; largest move 1 (Claude Haiku 5.5 (xhigh), Claude Haiku 5.5 (low), GPT-6.1 Sol (high), Kimi K3.1 Pro) |
| plan | alternative workload, recalibrated anchors; fixed-multiple arithmetic stress (not identified Plan economics for the altered workload) | 19 rows move; largest move 4 (Claude Haiku 5.5 (high), Gemini 4 Argon (high), GPT-6 Astra (xhigh)) |

### Common-leaf ranking (diagnostic): release gates

| Rule | Status | Detail |
|---|---|---|
| clip gate (E20) | fired | release held; remedy: O12 versioned re-freeze of the anchors with a dual run (O120) |
| cost influence flag (E91) | passed | cost not discriminating (< 10%); informational only; beta never changes (O2) |
| quality influence flag (E126) | passed | quality not discriminating (cost share > 90%); informational only |
| subset scoring (O17) | vacuous | subset rows scored on their own workload and anchors |
| partial component flag (E37) | vacuous | AA declined- or missing-task markers, or an Index reconstruction that misses AA's total (E209) |
| route dominance filter (E88) | vacuous | certifiably dearer routes set aside |
| Plan exploratory label (E61) | fired | fewer than half of Plan rows have an identified M_W |
| Plan evidence lifecycle and change detection (E18, E151, E269, O77, O79) | fired | 85 of 92 plan rows carry a possibly-superseded or expired route: claude-haiku-5-5-high@claude-max-20x, claude-haiku-5-5-high@claude-max-5x, claude-haiku-5-5-high@claude-pro, claude-haiku-5-5-low@claude-max-20x, claude-haiku-5-5-low@claude-max-5x, claude-haiku-5-5-low@claude-pro, claude-haiku-5-5-max@claude-max-20x, claude-haiku-5-5-max@claude-max-5x, claude-haiku-5-5-max@claude-pro, claude-haiku-5-5-medium@claude-max-20x, claude-haiku-5-5-medium@claude-max-5x, claude-haiku-5-5-medium@claude-pro, claude-haiku-5-5@claude-max-20x, claude-haiku-5-5@claude-max-5x, claude-haiku-5-5@claude-pro, claude-opus-5-5-high@claude-max-20x, claude-opus-5-5-high@claude-max-5x, claude-opus-5-5-high@claude-pro, claude-opus-5-5-medium@claude-max-20x, claude-opus-5-5-medium@claude-max-5x, claude-opus-5-5-medium@claude-pro, claude-opus-5-5-xhigh@claude-max-20x, claude-opus-5-5-xhigh@claude-max-5x, claude-opus-5-5-xhigh@claude-pro, claude-opus-5-5@claude-max-20x, claude-opus-5-5@claude-max-5x, claude-opus-5-5@claude-pro, claude-sonnet-5-5-xhigh@claude-max-20x, claude-sonnet-5-5-xhigh@claude-max-5x, claude-sonnet-5-5-xhigh@claude-pro, claude-sonnet-5-5@claude-max-20x, claude-sonnet-5-5@claude-max-5x, claude-sonnet-5-5@claude-pro, gpt-5.6-luna-low@chatgpt-plus, gpt-5.6-luna-low@chatgpt-pro-100, gpt-5.6-luna-low@chatgpt-pro-200, gpt-5.6-luna-low@chatgpt-pro-500, gpt-6-astra-high@chatgpt-plus, gpt-6-astra-high@chatgpt-pro-100, gpt-6-astra-high@chatgpt-pro-200, gpt-6-astra-high@chatgpt-pro-500, gpt-6-astra-xhigh@chatgpt-plus, gpt-6-astra-xhigh@chatgpt-pro-100, gpt-6-astra-xhigh@chatgpt-pro-200, gpt-6-astra-xhigh@chatgpt-pro-500, gpt-6-astra@chatgpt-plus, gpt-6-astra@chatgpt-pro-100, gpt-6-astra@chatgpt-pro-200, gpt-6-astra@chatgpt-pro-500, gpt-6-luna-high@chatgpt-plus, gpt-6-luna-high@chatgpt-pro-100, gpt-6-luna-high@chatgpt-pro-200, gpt-6-luna-high@chatgpt-pro-500, gpt-6-luna-low@chatgpt-plus, gpt-6-luna-low@chatgpt-pro-100, gpt-6-luna-low@chatgpt-pro-200, gpt-6-luna-low@chatgpt-pro-500, gpt-6-luna-medium@chatgpt-plus, gpt-6-luna-medium@chatgpt-pro-100, gpt-6-luna-medium@chatgpt-pro-200, gpt-6-luna-medium@chatgpt-pro-500, gpt-6-luna-xhigh@chatgpt-plus, gpt-6-luna-xhigh@chatgpt-pro-100, gpt-6-luna-xhigh@chatgpt-pro-200, gpt-6-luna-xhigh@chatgpt-pro-500, gpt-6-luna@chatgpt-plus, gpt-6-luna@chatgpt-pro-100, gpt-6-luna@chatgpt-pro-200, gpt-6-luna@chatgpt-pro-500, gpt-6.1-sol-high@chatgpt-plus, gpt-6.1-sol-high@chatgpt-pro-100, gpt-6.1-sol-high@chatgpt-pro-200, gpt-6.1-sol-high@chatgpt-pro-500, gpt-6.1-sol-medium@chatgpt-plus, gpt-6.1-sol-medium@chatgpt-pro-100, gpt-6.1-sol-medium@chatgpt-pro-200, gpt-6.1-sol-medium@chatgpt-pro-500, gpt-6.1-sol-xhigh@chatgpt-plus, gpt-6.1-sol-xhigh@chatgpt-pro-100, gpt-6.1-sol-xhigh@chatgpt-pro-200, gpt-6.1-sol-xhigh@chatgpt-pro-500, gpt-6.1-sol@chatgpt-plus, gpt-6.1-sol@chatgpt-pro-100, gpt-6.1-sol@chatgpt-pro-200, gpt-6.1-sol@chatgpt-pro-500 |
| acknowledged accounting-fault windows (O91, O92, O93, O95, O96) | fired | 13 of 92 plan rows rest on a measurement inside an acknowledged fault window; they stay selected and yield to two concordant user reports for their own model and plan, and the transfers resting on them follow: gpt-5.6-luna-low@chatgpt-pro-500, gpt-6-astra-high@chatgpt-pro-500, gpt-6-astra-xhigh@chatgpt-pro-500, gpt-6-astra@chatgpt-pro-500, gpt-6-luna-high@chatgpt-pro-500, gpt-6-luna-low@chatgpt-pro-500, gpt-6-luna-medium@chatgpt-pro-500, gpt-6-luna-xhigh@chatgpt-pro-500, gpt-6-luna@chatgpt-pro-500, gpt-6.1-sol-high@chatgpt-pro-500, gpt-6.1-sol-medium@chatgpt-pro-500, gpt-6.1-sol-xhigh@chatgpt-pro-500, gpt-6.1-sol@chatgpt-pro-500 |
| AA cost omits a pricing term (O94, O98, O100, O106, O108, O109, O114) | fired | ranked at the published cost; compete in interval outputs and the scenario labels' BlockerSafe test over [C, factor × C] ([C, ∞) without a stated factor, O98) without a label (scenario frequencies draw them at the published cost, O114), and leave the anchor population at the next freeze: claude-haiku-5-5 (up to 5×), claude-haiku-5-5-high (up to 5×), claude-haiku-5-5-low (up to 5×), claude-haiku-5-5-max (up to 5×), claude-haiku-5-5-medium (up to 5×) |
| valuation-basis gate (E170) | passed | every ranked row is compatible as captured or after evidenced revaluation |
| source clocks and evidence freshness (O59, O60, O65, E211, E216, E217, E218) | passed | every capture is within its age gate and none after the cutoff unless its source predates the cutoff's day; the build stops otherwise |
| build-stopping evidence gates (O64, O69, O71, O75, O99, O100, O101, O103, O105-O111, E195, E204, E225) | passed | the Coding Agent Index manifest (O64), the Terminal-Bench agent list (E225), cutoff-day row dates (O69), the three-stage all-provider plan search (O71, O75), the typed change records behind every route flag and partition split, which also produce each route's label and blocking dates within its launch- and schedule-bounded span (O99, O101, O105, O107, O110, O111), the register of AA notes covering every captured one, with the chart's inventory and duplicate-entry checks, the post-O103 capture notes, the basket-chart labels and chart-level notes' named rows (O100, O103, O106, O108) and the frontier path checks (E195, E204) hold; the build stops otherwise |
| score swing gate (E177) | vacuous | first v3 release: no previous v3 release to compare |
| anchor migration (E184) | vacuous | no main-workload migration deferred |
| configuration map coverage | passed | every cohort row has a configuration-map entry |
| quality clipping audit (E110) | passed | saturation disclosed; domain violations block the build |
| full benchmark set (O36, O38) | fired | listed, not ranked: mimo-v2-6-flash, minimax-m3-1-flash |
| missing-leaf rules (O8 provisional, E198b, E201b, E219, E221, E226) | vacuous | no ranked row has a missing leaf (O36) |
| S1M interval stream (E145) | vacuous | dormant: no ranked leaf carries a published confidence interval since O37, so S1M equals S1 (E236) |
| provider-claim label denial (E233) | vacuous | no row has a provider-claimed leaf |
| scenario outputs current (E72) | fired | scenario outputs stale (inputs changed since the scenario run); release held |
| diagnostic ranking (O121) | fired | no label is issued and the gates are disclosed without holding the release |


## Basket cost by component

USD at API rates for the exact configuration; "—" marks a component without an exact cost.

| Configuration | Coding Agent Index | FrontierCode 1.1 | ITBench-AA | AA-Briefcase | GDPval-AA | GDP.pdf | AutomationBench-AA | Terminal-Bench 4.0 (AA Index run) | SciCode | AA-LCR | Basket cost | Missing admitted components |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Claude Opus 5.5 (max) | $3,312.59 | $1,015.00 | $146.00 | $1,915.18 | $1,962.05 | $155.23 | $938.69 | $865.21 | $135.11 | $67.66 | $9,351.72 | none |
| Claude Sonnet 5.5 (max) | $3,857.44 | $826.00 | — | $1,863.13 | $1,504.30 | $79.43 | $678.32 | $834.67 | $80.07 | $33.93 | $8,931.28 | none |
| GPT-6.1 Sol (max) | $436.35 | $81.00 | — | $210.45 | $196.57 | $41.99 | $195.01 | $120.30 | $12.50 | $19.94 | $1,233.11 | none |
| Claude Haiku 5.5 (max) | $775.43 | $33.00 | — | $61.41 | $48.90 | $5.27 | $27.80 | $43.02 | $3.15 | $1.93 | $966.92 | none |
| GPT-6 Astra (max) | $2,040.49 | $422.00 | $133.00 | $864.69 | $996.49 | $207.58 | $1,048.30 | $560.88 | $66.89 | $99.73 | $5,885.05 | none |
| GPT-6 Luna (max) | $46.16 | $9.00 | — | $15.47 | $19.66 | $2.85 | $23.91 | $15.59 | $1.06 | $1.02 | $125.72 | none |
| DeepSeek V4.1 Flash 1017 (max) | $85.92 | $35.00 | — | $61.72 | $77.91 | $4.23 | $114.26 | $58.09 | $4.65 | $3.26 | $410.04 | none |
| MiMo-V2.6-Pro | — | $18.00 | — | $34.60 | $35.47 | $2.40 | $27.77 | $28.91 | $2.25 | $4.74 | $136.13 | Coding Agent Index |
| Gemini 4 Argon (high) | $1,699.83 | $670.00 | — | $530.33 | $400.23 | $25.93 | $399.89 | $447.49 | $30.44 | $23.64 | $3,557.77 | none |

### Valuation basis

Valuation-basis gate (E170): 9 compatible as captured. AA's Index category costs reconcile exactly with the prices AA displays for each configuration at capture, so its applied prices are the prices in force at the release cutoff. Token metering (E176): 9 not published per configuration; AA values cached input at live measurements of each model's typical cache-hit rate. Source intervals (E174): terminalBench: captured, level 95% (tbench.ai: "The whiskers span the 95% confidence interval"); gdpval: captured, level unstated, level not stated by the source (the 95% level on AA's methodology page belongs to AA-Briefcase).

## Plan route selection

The Plan amount is the selected multiple times the cash paid for the fee period (E166), typed by what the measurement establishes; it is not capacity unless it says so. The multiple values only the measured workload's API-equivalent consumption; other plan features are not valued.

| Configuration | Selected route | Plan amount | Basket runs per fee period | Identification | Plan cost (USD per basket run) | Flags | Selection reason |
|---|---|---|---|---|---:|---|---|
| Claude Opus 5.5 (max) | Claude Pro $20 · Opus 5.5 (58.9×, measured) | $1,178 per month: measured-workload capacity | 0.13 per month | unidentified | $158.77 | workload-unmatched; possibly-superseded; valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| Claude Sonnet 5.5 (max) | Claude Pro $20 · common Claude assumption (58.9×, assumption) | $1,178 per month: assumed API-equivalent consumption (owner-named transfer) from claude-pro-opus55-semianalysis | 0.13 per month | unidentified | $151.63 | workload-unmatched; owner-named transfer (assumption); possibly-superseded; valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| GPT-6.1 Sol (max) | ChatGPT Pro 500 $500 · GPT-6.1 Sol (10.772×, measured) | $5,386 per month: measured-workload capacity | 4.37 per month | unidentified | $114.47 | workload-unmatched; possibly-superseded; measured inside an acknowledged accounting-fault window (O91, O92); valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| Claude Haiku 5.5 (max) | Claude Pro $20 · common Claude assumption (58.9×, assumption) | $1,178 per month: assumed API-equivalent consumption (owner-named transfer) from claude-pro-opus55-semianalysis | 1.22 per month | unidentified | $16.42 | workload-unmatched; owner-named transfer (assumption); possibly-superseded; valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| GPT-6 Astra (max) | ChatGPT Pro 200 $200 · GPT-6 Astra (14.485×, measured) | $2,897 per month: measured-workload capacity | 0.49 per month | unidentified | $406.29 | workload-unmatched; possibly-superseded; valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| GPT-6 Luna (max) | ChatGPT Pro 500 $500 · common GPT assumption (10.772×, assumption) | $5,386 per month: assumed API-equivalent consumption (owner-named transfer) from chatgpt-pro500-gpt61sol-semianalysis | 42.84 per month | unidentified | $11.67 | workload-unmatched; owner-named transfer (assumption); possibly-superseded; measured inside an acknowledged accounting-fault window (O91, O92); valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| DeepSeek V4.1 Flash 1017 (max) | — | — | — | — | $410.04 | API-cost fallback: no admitted Plan route; cross-estimand ordering not identified | no eligible route |
| MiMo-V2.6-Pro | MiMo Token Plan Max $100 · quota ceiling (provider-derived) (1.1808×, assumption) | $118 per month: provider quota ceiling: the full quota at API rates (O46; full use assumed) | 0.87 per month | unidentified | $115.28 | workload-unmatched; provider quota ceiling; full use assumed (O46) | larger quota-ceiling multiple (O46: provider-derived, not observed) |
| Gemini 4 Argon (high) | — | — | — | — | $3,557.77 | API-cost fallback: no admitted Plan route; cross-estimand ordering not identified | no eligible route |

### Route alternatives

Every admissible route-measurement pair in comparator order (E171) and the comparator's pick with the selected pair removed (E179). A larger displayed multiple is arithmetic on the measured workload, never a claim that the route is cheaper on the scored workload. Workday-feasible multiple (E15), for the 7 routed rows: not evaluated: no evidenced quota schema for this route.

| Configuration | Admissible pairs | Unidentified | Pairs (multiple, status) | Leave-selected-out choice |
|---|---:|---:|---|---|
| Claude Opus 5.5 (max) | 3 | 3 | claude-pro-opus55-semianalysis (58.9×, selected); claude-max20x-opus55-semianalysis (58.63×, not selected by the comparator); claude-max5x-opus55-semianalysis (57.25×, not selected by the comparator) | claude-max20x-opus55-semianalysis (58.63×, value 64.14) |
| Claude Sonnet 5.5 (max) | 3 | 3 | claude-pro-claude-sonnet-5-5-common-opus55-assumption (58.9×, selected); claude-max20x-claude-sonnet-5-5-common-opus55-assumption (58.63×, not selected by the comparator); claude-max5x-claude-sonnet-5-5-common-opus55-assumption (57.25×, not selected by the comparator) | claude-max20x-claude-sonnet-5-5-common-opus55-assumption (58.63×, value 63.54) |
| GPT-6.1 Sol (max) | 4 | 4 | chatgpt-pro500-gpt61sol-semianalysis (10.772×, selected); chatgpt-plus-gpt61sol-semianalysis (10.55×, not selected by the comparator); chatgpt-pro100-gpt61sol-semianalysis (10.55×, not selected by the comparator); chatgpt-pro200-gpt61sol-semianalysis (10.42×, not selected by the comparator) | chatgpt-plus-gpt61sol-semianalysis (10.55×, value 62.54) |
| Claude Haiku 5.5 (max) | 3 | 3 | claude-pro-claude-haiku-5-5-max-common-opus55-assumption (58.9×, selected); claude-max20x-claude-haiku-5-5-max-common-opus55-assumption (58.63×, not selected by the comparator); claude-max5x-claude-haiku-5-5-max-common-opus55-assumption (57.25×, not selected by the comparator) | claude-max20x-claude-haiku-5-5-max-common-opus55-assumption (58.63×, value 59.17) |
| GPT-6 Astra (max) | 4 | 4 | chatgpt-pro200-gpt6astra-semianalysis (14.485×, selected); chatgpt-pro500-gpt6astra-semianalysis (13.91×, not selected by the comparator); chatgpt-pro100-gpt6astra-semianalysis (13.22×, not selected by the comparator); chatgpt-plus-gpt6astra-semianalysis (8.1×, not selected by the comparator) | chatgpt-pro500-gpt6astra-semianalysis (13.91×, value 58.64) |
| GPT-6 Luna (max) | 4 | 4 | chatgpt-pro500-gpt-6-luna-common-gpt-assumption (10.772×, selected); chatgpt-pro100-gpt-6-luna-common-gpt-assumption (10.55×, not selected by the comparator); chatgpt-pro200-gpt-6-luna-common-gpt-assumption (10.42×, not selected by the comparator); chatgpt-plus-gpt-6-luna-common-gpt-assumption (8.1×, not selected by the comparator) | chatgpt-pro100-gpt-6-luna-common-gpt-assumption (10.55×, value 57.51) |
| MiMo-V2.6-Pro | 4 | 4 | mimo-tokenplan-max-mimo-v2-6-pro-quota-ceiling (1.1808×, selected); mimo-tokenplan-pro-mimo-v2-6-pro-quota-ceiling (1.0944×, not selected by the comparator); mimo-tokenplan-standard-mimo-v2-6-pro-quota-ceiling (0.99×, not selected by the comparator); mimo-tokenplan-lite-mimo-v2-6-pro-quota-ceiling (0.984×, not selected by the comparator) | mimo-tokenplan-pro-mimo-v2-6-pro-quota-ceiling (1.0944×, value 50.93) |

### Plan allowance report cells (O71, O81)

52 cells; 0 pass. A cell on a plan the Plan ranking does not list is evidence only (O85).

| Provider | Plan | Model | Unit | Region | Eligible reports | Verdict |
|---|---|---|---|---|---|---|
| Anthropic | Claude (plan redacted) (not listed) | Claude Opus 5.5 | week | global | 0 of 1 | fails: 0 non-provisional report(s) in the current partition |
| Anthropic | Claude Max (tier unstated) (not listed) | Claude Opus 5.5 | week | global | 0 of 3 | fails: 0 non-provisional report(s) in the current partition |
| Anthropic | Claude Max 20x | Claude Opus 5.5 | 5h | global | 1 of 2 | fails: a 5-hour figure never converts to a billing period (O82) |
| Anthropic | Claude Max 20x | Claude Opus 5.5 | month | global | 0 of 1 | fails: 0 non-provisional report(s) in the current partition |
| Anthropic | Claude Max 20x | Claude Opus 5.5 | week | global | 4 of 11 | fails: 1 non-provisional report(s) in the current partition |
| Anthropic | Claude Max 20x | — | week | global | 0 of 6 | fails: 0 non-provisional report(s) in the current partition |
| Anthropic | Claude Max 5x | Claude Opus 5.5 | month | global | 0 of 1 | fails: 0 non-provisional report(s) in the current partition |
| Anthropic | Claude Max 5x | Claude Opus 5.5 | week | global | 2 of 2 | fails: 0 non-provisional report(s) in the current partition |
| Anthropic | Claude Max 5x | — | week | global | 0 of 1 | fails: 0 non-provisional report(s) in the current partition |
| Anthropic | Claude Pro | Claude Opus 5.5 | 5h | global | 1 of 4 | fails: a 5-hour figure never converts to a billing period (O82) |
| Anthropic | Claude Pro | Claude Opus 5.5 | month | global | 0 of 1 | fails: 0 non-provisional report(s) in the current partition |
| Anthropic | Claude Pro | Claude Opus 5.5 | week | global | 2 of 9 | fails: 0 non-provisional report(s) in the current partition |
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
| MiniMax | MiniMax Token Plan Max (legacy) (not listed) | MiniMax-M3.1-Flash | 5h | global | 1 of 1 | fails: a 5-hour figure never converts to a billing period (O82) |
| MiniMax | MiniMax Token Plan Max (legacy) (not listed) | MiniMax-M3.1-Flash | week | global | 1 of 1 | fails: 0 non-provisional report(s) in the current partition |
| MiniMax | MiniMax Token Plan lowest tier (legacy) (not listed) | MiniMax-M3.1-Flash | 5h | global | 1 of 1 | fails: a 5-hour figure never converts to a billing period (O82) |
| MiniMax | MiniMax lowest tier ("lite") (not listed) | — | week | global | 0 of 1 | fails: 0 non-provisional report(s) in the current partition |
| OpenAI | ChatGPT (legacy account, tier unstated) (not listed) | GPT-6.1 Sol | week | global | 0 of 1 | fails: 0 non-provisional report(s) in the current partition |
| OpenAI | ChatGPT Plus | GPT-5.6 Luna | 5h | global | 0 of 1 | fails: a 5-hour figure never converts to a billing period (O82) |
| OpenAI | ChatGPT Plus | GPT-5.6 Luna | week | global | 0 of 1 | fails: 0 non-provisional report(s) in the current partition |
| OpenAI | ChatGPT Plus | GPT-6 Astra | 5h | global | 0 of 2 | fails: a 5-hour figure never converts to a billing period (O82) |
| OpenAI | ChatGPT Plus | GPT-6 Luna | 5h | global | 1 of 1 | fails: a 5-hour figure never converts to a billing period (O82) |
| OpenAI | ChatGPT Plus | GPT-6 Luna | month | global | 0 of 1 | fails: 0 non-provisional report(s) in the current partition |
| OpenAI | ChatGPT Plus | GPT-6.1 Sol | 5h | global | 0 of 3 | fails: a 5-hour figure never converts to a billing period (O82) |
| OpenAI | ChatGPT Plus | GPT-6.1 Sol | week | global | 0 of 2 | fails: 0 non-provisional report(s) in the current partition |
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
| Claude Opus 5.5 (max) | measured, target-workload unmatched | claude-pro-opus55-semianalysis | $158.77 | 64.16 | 1 |
| GPT-6.1 Sol (max) | measured, target-workload unmatched | chatgpt-pro500-gpt61sol-semianalysis | $114.47 | 62.61 | 2 |
| GPT-6 Astra (max) | measured, target-workload unmatched | chatgpt-pro200-gpt6astra-semianalysis | $406.29 | 58.78 | 3 |
| Claude Haiku 5.5 (max) | no measured route | — | — | — | — |
| Claude Sonnet 5.5 (max) | no measured route | — | — | — | — |
| DeepSeek V4.1 Flash 1017 (max) | no measured route | — | — | — | — |
| GPT-6 Luna (max) | no measured route | — | — | — | — |
| Gemini 4 Argon (high) | no measured route | — | — | — | — |
| MiMo-V2.6-Pro | no measured route | — | — | — | — |

#### Measured-evidence calibration (diagnostic)

References: each workload's measured-only rows with complete cost evidence are the references: c_L = cheapest / 2, c_H = dearest x 2 (diagnostic only; the official anchors are unchanged). Status: evaluated.

- Workload `9a0d376cc6080f3c`: measured anchors $57.24 to $812.57 from Claude Opus 5.5 (max), GPT-6 Astra (max), GPT-6.1 Sol (max); anchor ratio 14.2 against the official 1219.4. Official Plan anchors are set by GPT-6 Luna (max) on ChatGPT Pro 500 (owner-named transfer) at the low end and Gemini 4 Argon (high) on API-cost fallback at the high end.
- Workload `1453a9a0576b02ea`: measured-evidence calibration unavailable (fewer than two measured references); measured rows none. Official Plan anchors are set by Claude Haiku 5.5 (max) on Claude Pro (owner-named transfer; AA cost caveat: leaves the anchors at the next freeze, O94) at the low end and Gemini 4 Argon (high) on API-cost fallback at the high end.

| Configuration | Value on official Plan anchors | Value on measured anchors | Rank change |
|---|---:|---:|---:|
| Claude Opus 5.5 (max) | 64.16 | 66.17 | 1 |
| GPT-6 Astra (max) | 58.78 | 55.24 | 0 |
| GPT-6.1 Sol (max) | 62.61 | 66.55 | -1 |

Pairwise reversals: Claude Opus 5.5 (max) and GPT-6.1 Sol (max). Largest value change: 3.94 points.

## Interval outputs

**API basis, main workload: frontier.** Not evaluable: MiMo-V2.6-Pro. Competing without a label of its own (E183): Claude Haiku 5.5 (max): AA's cost omits a pricing term (O94); competes over its published cost up to the stated factor.

| Configuration | Possible frontier | Definite frontier | Definite counterexample | Possible frontier blocked by |
|---|---|---|---|---|
| Claude Sonnet 5.5 (max) | certified | certified | — | — |
| Claude Opus 5.5 (max) | certified | certified | — | — |
| DeepSeek V4.1 Flash 1017 (max) | certified | certified | — | — |
| GPT-6.1 Sol (max) | certified | certified | — | — |
| Gemini 4 Argon (high) | disproved | disproved | GPT-6.1 Sol (max) | GPT-6.1 Sol (max) |
| GPT-6 Astra (max) | certified | certified | — | — |
| GPT-6 Luna (max) | certified | certified | — | — |

**API basis, main workload: cheapest at or above quality 63.5** (lower-median displayed quality of the non-provisional cohort configurations at freeze (E192; headline bar)). Status certified; confirmed cheapest: GPT-6.1 Sol (max).

Configurations that can be confirmed to qualify: 4 (confirmation needs the full-composite lower bound, with missing leaves at 0, to clear the bar; O25). Cheaper same-family configurations on AA's chart that were not evaluated (not ranked in this ranking: lacking its full benchmark set, or not plotted on or near the frontier; E201c, O51): GPT-6.1 Sol (max): GPT-6.1 Sol (xhigh), GPT-6.1 Sol (high), GPT-6.1 Sol (medium), GPT-6.1 Sol (low).

Bar comparison: compares 5 configurations that can qualify. The bar is a displayed-quality level; qualification tests each row's full-composite bounds, so a row above the bar on displayed quality can still fail to qualify confirmed when leaves are missing (E198).

| Configuration | Displayed quality − bar | Confirmed qualifies | Possibly qualifies | Possibly cheapest |
|---|---:|---|---|---|
| Claude Sonnet 5.5 (max) | 3.2 | certified | certified | disproved |
| Claude Opus 5.5 (max) | 4.2 | certified | certified | disproved |
| DeepSeek V4.1 Flash 1017 (max) | -6.2 | disproved | disproved | disproved |
| GPT-6.1 Sol (max) | 0.6 | certified | certified | certified |
| Gemini 4 Argon (high) | 0.0 | disproved | certified | disproved |
| GPT-6 Astra (max) | 1.4 | certified | certified | disproved |
| GPT-6 Luna (max) | -16.8 | disproved | disproved | disproved |

**API basis, main workload: cheapest at or above quality 53.3** (lower-quartile displayed quality of the non-provisional cohort configurations at freeze (O34)). Status certified; confirmed cheapest: DeepSeek V4.1 Flash 1017 (max).

Configurations that can be confirmed to qualify: 6 (confirmation needs the full-composite lower bound, with missing leaves at 0, to clear the bar; O25). Cheaper same-family configurations on AA's chart that were not evaluated (not ranked in this ranking: lacking its full benchmark set, or not plotted on or near the frontier; E201c, O51): none.

Bar comparison: compares 6 configurations that can qualify. The bar is a displayed-quality level; qualification tests each row's full-composite bounds, so a row above the bar on displayed quality can still fail to qualify confirmed when leaves are missing (E198).

| Configuration | Displayed quality − bar | Confirmed qualifies | Possibly qualifies | Possibly cheapest |
|---|---:|---|---|---|
| Claude Sonnet 5.5 (max) | 13.4 | certified | certified | disproved |
| Claude Opus 5.5 (max) | 14.4 | certified | certified | disproved |
| DeepSeek V4.1 Flash 1017 (max) | 4.1 | certified | certified | certified |
| GPT-6.1 Sol (max) | 10.8 | certified | certified | disproved |
| Gemini 4 Argon (high) | 10.3 | certified | certified | disproved |
| GPT-6 Astra (max) | 11.7 | certified | certified | disproved |
| GPT-6 Luna (max) | -6.6 | disproved | disproved | disproved |

**API basis, main workload: cheapest at or above quality 64.9** (upper-quartile displayed quality of the non-provisional cohort configurations at freeze (O34)). Status certified; confirmed cheapest: none.

Configurations that can be confirmed to qualify: 2 (confirmation needs the full-composite lower bound, with missing leaves at 0, to clear the bar; O25). Cheaper same-family configurations on AA's chart that were not evaluated (not ranked in this ranking: lacking its full benchmark set, or not plotted on or near the frontier; E201c, O51): Claude Sonnet 5.5 (max): Claude Sonnet 5.5 (xhigh with fallback), Claude Sonnet 5.5 (high with fallback), Claude Sonnet 5.5 (medium with fallback), Claude Sonnet 5.5 (low with fallback); GPT-6 Astra (max): GPT-6 Astra (xhigh), GPT-6 Astra (high), GPT-6 Astra (medium), GPT-6 Astra (low).

Bar comparison: compares 3 configurations that can qualify. The bar is a displayed-quality level; qualification tests each row's full-composite bounds, so a row above the bar on displayed quality can still fail to qualify confirmed when leaves are missing (E198).

| Configuration | Displayed quality − bar | Confirmed qualifies | Possibly qualifies | Possibly cheapest |
|---|---:|---|---|---|
| Claude Sonnet 5.5 (max) | 1.7 | certified | certified | certified |
| Claude Opus 5.5 (max) | 2.8 | certified | certified | disproved |
| DeepSeek V4.1 Flash 1017 (max) | -7.6 | disproved | disproved | disproved |
| GPT-6.1 Sol (max) | -0.8 | disproved | disproved | disproved |
| Gemini 4 Argon (high) | -1.4 | disproved | disproved | disproved |
| GPT-6 Astra (max) | 0.0 | disproved | certified | certified |
| GPT-6 Luna (max) | -18.2 | disproved | disproved | disproved |

**Plan basis, main workload:** not evaluated (no row has FullCost and an identified M_W (E61/E67)).

**API basis, subset workload (AA-Briefcase, GDPval-AA, GDP.pdf, AutomationBench-AA, Terminal-Bench 4.0 (AA Index run), SciCode, AA-LCR; orderings across workloads not identified): frontier.** Not evaluable: none. Competing without a label of its own (E183): Claude Haiku 5.5 (max): AA's cost omits a pricing term (O94); competes over its published cost up to the stated factor.

| Configuration | Possible frontier | Definite frontier | Definite counterexample | Possible frontier blocked by |
|---|---|---|---|---|
| Claude Sonnet 5.5 (max) | certified | certified | — | — |
| Claude Opus 5.5 (max) | certified | certified | — | — |
| DeepSeek V4.1 Flash 1017 (max) | certified | certified | — | — |
| GPT-6.1 Sol (max) | certified | certified | — | — |
| Gemini 4 Argon (high) | disproved | disproved | GPT-6.1 Sol (max) | GPT-6.1 Sol (max) |
| GPT-6 Astra (max) | certified | certified | — | — |
| MiMo-V2.6-Pro | certified | certified | — | — |
| GPT-6 Luna (max) | certified | certified | — | — |

**API basis, subset workload (AA-Briefcase, GDPval-AA, GDP.pdf, AutomationBench-AA, Terminal-Bench 4.0 (AA Index run), SciCode, AA-LCR; orderings across workloads not identified): cheapest at or above quality 63.5** (lower-median displayed quality of the non-provisional cohort configurations at freeze (E192; headline bar)). Status certified; confirmed cheapest: GPT-6.1 Sol (max).

Configurations that can be confirmed to qualify: 4 (confirmation needs the full-composite lower bound, with missing leaves at 0, to clear the bar; O25). Cheaper same-family configurations on AA's chart that were not evaluated (not ranked in this ranking: lacking its full benchmark set, or not plotted on or near the frontier; E201c, O51): GPT-6.1 Sol (max): GPT-6.1 Sol (xhigh), GPT-6.1 Sol (high), GPT-6.1 Sol (medium), GPT-6.1 Sol (low).

Bar comparison: compares 5 configurations that can qualify. The bar is a displayed-quality level; qualification tests each row's full-composite bounds, so a row above the bar on displayed quality can still fail to qualify confirmed when leaves are missing (E198).

| Configuration | Displayed quality − bar | Confirmed qualifies | Possibly qualifies | Possibly cheapest |
|---|---:|---|---|---|
| Claude Sonnet 5.5 (max) | 3.2 | certified | certified | disproved |
| Claude Opus 5.5 (max) | 4.2 | certified | certified | disproved |
| DeepSeek V4.1 Flash 1017 (max) | -6.2 | disproved | disproved | disproved |
| GPT-6.1 Sol (max) | 0.6 | certified | certified | certified |
| Gemini 4 Argon (high) | 0.0 | disproved | certified | disproved |
| GPT-6 Astra (max) | 1.4 | certified | certified | disproved |
| MiMo-V2.6-Pro | -10.3 | disproved | disproved | disproved |
| GPT-6 Luna (max) | -16.8 | disproved | disproved | disproved |

**API basis, subset workload (AA-Briefcase, GDPval-AA, GDP.pdf, AutomationBench-AA, Terminal-Bench 4.0 (AA Index run), SciCode, AA-LCR; orderings across workloads not identified): cheapest at or above quality 53.3** (lower-quartile displayed quality of the non-provisional cohort configurations at freeze (O34)). Status certified; confirmed cheapest: none.

Configurations that can be confirmed to qualify: 6 (confirmation needs the full-composite lower bound, with missing leaves at 0, to clear the bar; O25). Cheaper same-family configurations on AA's chart that were not evaluated (not ranked in this ranking: lacking its full benchmark set, or not plotted on or near the frontier; E201c, O51): none.

Bar comparison: compares 7 configurations that can qualify. The bar is a displayed-quality level; qualification tests each row's full-composite bounds, so a row above the bar on displayed quality can still fail to qualify confirmed when leaves are missing (E198).

| Configuration | Displayed quality − bar | Confirmed qualifies | Possibly qualifies | Possibly cheapest |
|---|---:|---|---|---|
| Claude Sonnet 5.5 (max) | 13.4 | certified | certified | disproved |
| Claude Opus 5.5 (max) | 14.4 | certified | certified | disproved |
| DeepSeek V4.1 Flash 1017 (max) | 4.1 | certified | certified | certified |
| GPT-6.1 Sol (max) | 10.8 | certified | certified | disproved |
| Gemini 4 Argon (high) | 10.3 | certified | certified | disproved |
| GPT-6 Astra (max) | 11.7 | certified | certified | disproved |
| MiMo-V2.6-Pro | 0.0 | disproved | certified | certified |
| GPT-6 Luna (max) | -6.6 | disproved | disproved | disproved |

**API basis, subset workload (AA-Briefcase, GDPval-AA, GDP.pdf, AutomationBench-AA, Terminal-Bench 4.0 (AA Index run), SciCode, AA-LCR; orderings across workloads not identified): cheapest at or above quality 64.9** (upper-quartile displayed quality of the non-provisional cohort configurations at freeze (O34)). Status certified; confirmed cheapest: none.

Configurations that can be confirmed to qualify: 2 (confirmation needs the full-composite lower bound, with missing leaves at 0, to clear the bar; O25). Cheaper same-family configurations on AA's chart that were not evaluated (not ranked in this ranking: lacking its full benchmark set, or not plotted on or near the frontier; E201c, O51): Claude Sonnet 5.5 (max): Claude Sonnet 5.5 (xhigh with fallback), Claude Sonnet 5.5 (high with fallback), Claude Sonnet 5.5 (medium with fallback), Claude Sonnet 5.5 (low with fallback); GPT-6 Astra (max): GPT-6 Astra (xhigh), GPT-6 Astra (high), GPT-6 Astra (medium), GPT-6 Astra (low).

Bar comparison: compares 3 configurations that can qualify. The bar is a displayed-quality level; qualification tests each row's full-composite bounds, so a row above the bar on displayed quality can still fail to qualify confirmed when leaves are missing (E198).

| Configuration | Displayed quality − bar | Confirmed qualifies | Possibly qualifies | Possibly cheapest |
|---|---:|---|---|---|
| Claude Sonnet 5.5 (max) | 1.7 | certified | certified | certified |
| Claude Opus 5.5 (max) | 2.8 | certified | certified | disproved |
| DeepSeek V4.1 Flash 1017 (max) | -7.6 | disproved | disproved | disproved |
| GPT-6.1 Sol (max) | -0.8 | disproved | disproved | disproved |
| Gemini 4 Argon (high) | -1.4 | disproved | disproved | disproved |
| GPT-6 Astra (max) | 0.0 | disproved | certified | certified |
| MiMo-V2.6-Pro | -11.7 | disproved | disproved | disproved |
| GPT-6 Luna (max) | -18.2 | disproved | disproved | disproved |

**Plan basis, subset workload (AA-Briefcase, GDPval-AA, GDP.pdf, AutomationBench-AA, Terminal-Bench 4.0 (AA Index run), SciCode, AA-LCR; orderings across workloads not identified):** not evaluated (unevaluable: no Plan multiple is identified for a subset workload (E149, E190)).

## Scenario shares

The scenario panel is the 8 rows scored on the main workload (E96, E266); MiMo-V2.6-Pro (subset workload) are not in it and have no scenario shares, so the shares below compare the main-workload rows only.

Frequencies over 10,000 scenarios per run (seed 20261025); streams are defined in [methodology.md](methodology.md#uncertainty-outputs). S1T adds benchmark sampling noise under an independent-task approximation (O39); the other streams exclude it, and every stream excludes correlated-task, harness and attempt effects (E155).

### API basis: rank 1

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M | S1T |
|---|---:|---:|---:|---:|---:|---:|
| Claude Haiku 5.5 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Sonnet 5.5 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| DeepSeek V4.1 Flash 1017 (max) | 0.0% | 0.0% | 37.3% | 0.0% | 0.0% | 44.0% |
| GPT-6 Astra (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Luna (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.3% |
| GPT-6.1 Sol (max) | 100.0% | 100.0% | 62.7% | 100.0% | 100.0% | 55.7% |
| Gemini 4 Argon (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |

### API basis: rank 3 or better

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M | S1T |
|---|---:|---:|---:|---:|---:|---:|
| Claude Haiku 5.5 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 1.0% |
| Claude Sonnet 5.5 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.2% |
| DeepSeek V4.1 Flash 1017 (max) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% |
| GPT-6 Astra (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.6% |
| GPT-6 Luna (max) | 100.0% | 100.0% | 97.4% | 100.0% | 100.0% | 91.6% |
| GPT-6.1 Sol (max) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% |
| Gemini 4 Argon (high) | 0.0% | 0.0% | 2.6% | 0.0% | 0.0% | 6.6% |

### API basis: on the frontier

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M | S1T |
|---|---:|---:|---:|---:|---:|---:|
| Claude Haiku 5.5 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (max) | 100.0% | 100.0% | 96.5% | 100.0% | 100.0% | 68.3% |
| Claude Sonnet 5.5 (max) | 100.0% | 100.0% | 99.9% | 100.0% | 100.0% | 76.4% |
| DeepSeek V4.1 Flash 1017 (max) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% |
| GPT-6 Astra (max) | 100.0% | 100.0% | 99.8% | 100.0% | 100.0% | 58.4% |
| GPT-6 Luna (max) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% |
| GPT-6.1 Sol (max) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% |
| Gemini 4 Argon (high) | 0.0% | 0.0% | 12.8% | 0.0% | 0.0% | 37.5% |

### API basis: value-score dispersion (SD; covariance term)

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M | S1T |
|---|---:|---:|---:|---:|---:|---:|
| Claude Haiku 5.5 (max) | 0.00 (+0.00) | 0.00 (+0.00) | 1.38 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.00 (+0.00) |
| Claude Opus 5.5 (max) | 0.00 (+0.00) | 0.00 (+0.00) | 1.15 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.00 (+0.00) |
| Claude Sonnet 5.5 (max) | 0.00 (+0.00) | 0.00 (+0.00) | 1.11 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.01 (+0.00) |
| DeepSeek V4.1 Flash 1017 (max) | 0.00 (+0.00) | 0.00 (+0.00) | 1.22 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.00 (+0.00) |
| GPT-6 Astra (max) | 0.00 (+0.00) | 0.00 (+0.00) | 1.20 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 0.98 (+0.00) |
| GPT-6 Luna (max) | 0.00 (+0.00) | 0.00 (+0.00) | 1.49 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 0.96 (+0.00) |
| GPT-6.1 Sol (max) | 0.00 (+0.00) | 0.00 (+0.00) | 1.14 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.00 (+0.00) |
| Gemini 4 Argon (high) | 0.00 (+0.00) | 0.00 (+0.00) | 1.20 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.00 (+0.00) |

Plan streams S1, S2, S1 endpoint-heavy, S1M and S1T run with owner assumptions off (owner-named transfers and O46 provider quota ceilings; E167): Claude Haiku 5.5 (max) on Claude Max 20x, Claude Haiku 5.5 (max) on Claude Max 5x, Claude Haiku 5.5 (max) on Claude Pro, Claude Sonnet 5.5 (max) on Claude Max 20x, Claude Sonnet 5.5 (max) on Claude Max 5x, Claude Sonnet 5.5 (max) on Claude Pro, GPT-6 Luna (max) on ChatGPT Plus, GPT-6 Luna (max) on ChatGPT Pro 100, GPT-6 Luna (max) on ChatGPT Pro 200, GPT-6 Luna (max) on ChatGPT Pro 500 depend on an owner assumption and are unevaluable there (—), never reselected or replaced by API cost.

### Plan basis: rank 1

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M | S1T |
|---|---:|---:|---:|---:|---:|---:|
| Claude Haiku 5.5 (max) on Claude Max 20x | 0.0% | — | — | — | — | — |
| Claude Haiku 5.5 (max) on Claude Max 5x | 0.0% | — | — | — | — | — |
| Claude Haiku 5.5 (max) on Claude Pro | 0.0% | — | — | — | — | — |
| Claude Opus 5.5 (max) on Claude Max 20x | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (max) on Claude Max 5x | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (max) on Claude Pro | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 86.1% |
| Claude Sonnet 5.5 (max) on Claude Max 20x | 0.0% | — | — | — | — | — |
| Claude Sonnet 5.5 (max) on Claude Max 5x | 0.0% | — | — | — | — | — |
| Claude Sonnet 5.5 (max) on Claude Pro | 0.0% | — | — | — | — | — |
| DeepSeek V4.1 Flash 1017 (max) on API-cost fallback | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
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
| GPT-6.1 Sol (max) on ChatGPT Pro 500 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 13.9% |
| Gemini 4 Argon (high) on API-cost fallback | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |

### Plan basis: rank 3 or better

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M | S1T |
|---|---:|---:|---:|---:|---:|---:|
| Claude Haiku 5.5 (max) on Claude Max 20x | 0.0% | — | — | — | — | — |
| Claude Haiku 5.5 (max) on Claude Max 5x | 0.0% | — | — | — | — | — |
| Claude Haiku 5.5 (max) on Claude Pro | 0.0% | — | — | — | — | — |
| Claude Opus 5.5 (max) on Claude Max 20x | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 87.0% |
| Claude Opus 5.5 (max) on Claude Max 5x | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 84.6% |
| Claude Opus 5.5 (max) on Claude Pro | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 87.2% |
| Claude Sonnet 5.5 (max) on Claude Max 20x | 0.0% | — | — | — | — | — |
| Claude Sonnet 5.5 (max) on Claude Max 5x | 0.0% | — | — | — | — | — |
| Claude Sonnet 5.5 (max) on Claude Pro | 0.0% | — | — | — | — | — |
| DeepSeek V4.1 Flash 1017 (max) on API-cost fallback | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (max) on ChatGPT Plus | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (max) on ChatGPT Pro 100 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (max) on ChatGPT Pro 200 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (max) on ChatGPT Pro 500 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Luna (max) on ChatGPT Plus | 0.0% | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 500 | 0.0% | — | — | — | — | — |
| GPT-6.1 Sol (max) on ChatGPT Plus | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 13.0% |
| GPT-6.1 Sol (max) on ChatGPT Pro 100 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 13.0% |
| GPT-6.1 Sol (max) on ChatGPT Pro 200 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (max) on ChatGPT Pro 500 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 15.4% |
| Gemini 4 Argon (high) on API-cost fallback | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |

### Plan basis: on the frontier

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M | S1T |
|---|---:|---:|---:|---:|---:|---:|
| Claude Haiku 5.5 (max) on Claude Max 20x | 0.0% | — | — | — | — | — |
| Claude Haiku 5.5 (max) on Claude Max 5x | 0.0% | — | — | — | — | — |
| Claude Haiku 5.5 (max) on Claude Pro | 100.0% | — | — | — | — | — |
| Claude Opus 5.5 (max) on Claude Max 20x | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (max) on Claude Max 5x | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (max) on Claude Pro | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 97.0% |
| Claude Sonnet 5.5 (max) on Claude Max 20x | 0.0% | — | — | — | — | — |
| Claude Sonnet 5.5 (max) on Claude Max 5x | 0.0% | — | — | — | — | — |
| Claude Sonnet 5.5 (max) on Claude Pro | 100.0% | — | — | — | — | — |
| DeepSeek V4.1 Flash 1017 (max) on API-cost fallback | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (max) on ChatGPT Plus | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (max) on ChatGPT Pro 100 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (max) on ChatGPT Pro 200 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 6.7% |
| GPT-6 Astra (max) on ChatGPT Pro 500 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Luna (max) on ChatGPT Plus | 0.0% | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 500 | 100.0% | — | — | — | — | — |
| GPT-6.1 Sol (max) on ChatGPT Plus | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (max) on ChatGPT Pro 100 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (max) on ChatGPT Pro 200 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (max) on ChatGPT Pro 500 | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% |
| Gemini 4 Argon (high) on API-cost fallback | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.8% |

### Plan basis: value-score dispersion (SD; covariance term)

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M | S1T |
|---|---:|---:|---:|---:|---:|---:|
| Claude Haiku 5.5 (max) on Claude Max 20x | 0.00 (+0.00) | — | — | — | — | — |
| Claude Haiku 5.5 (max) on Claude Max 5x | 0.00 (+0.00) | — | — | — | — | — |
| Claude Haiku 5.5 (max) on Claude Pro | 0.00 (+0.00) | — | — | — | — | — |
| Claude Opus 5.5 (max) on Claude Max 20x | 0.00 (+0.00) | 0.00 (+0.00) | 1.14 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 0.98 (+0.00) |
| Claude Opus 5.5 (max) on Claude Max 5x | 0.00 (+0.00) | 0.00 (+0.00) | 1.14 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 0.98 (+0.00) |
| Claude Opus 5.5 (max) on Claude Pro | 0.00 (+0.00) | 0.00 (+0.00) | 1.14 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 0.98 (+0.00) |
| Claude Sonnet 5.5 (max) on Claude Max 20x | 0.00 (+0.00) | — | — | — | — | — |
| Claude Sonnet 5.5 (max) on Claude Max 5x | 0.00 (+0.00) | — | — | — | — | — |
| Claude Sonnet 5.5 (max) on Claude Pro | 0.00 (+0.00) | — | — | — | — | — |
| DeepSeek V4.1 Flash 1017 (max) on API-cost fallback | 0.00 (+0.00) | 0.00 (+0.00) | 1.22 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.00 (+0.00) |
| GPT-6 Astra (max) on ChatGPT Plus | 0.00 (+0.00) | 0.00 (+0.00) | 1.19 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 0.99 (+0.00) |
| GPT-6 Astra (max) on ChatGPT Pro 100 | 0.00 (+0.00) | 0.00 (+0.00) | 1.19 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 0.99 (+0.00) |
| GPT-6 Astra (max) on ChatGPT Pro 200 | 0.00 (+0.00) | 0.00 (+0.00) | 1.19 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 0.99 (+0.00) |
| GPT-6 Astra (max) on ChatGPT Pro 500 | 0.00 (+0.00) | 0.00 (+0.00) | 1.19 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 0.99 (+0.00) |
| GPT-6 Luna (max) on ChatGPT Plus | 0.00 (+0.00) | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 100 | 0.00 (+0.00) | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 200 | 0.00 (+0.00) | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 500 | 0.00 (+0.00) | — | — | — | — | — |
| GPT-6.1 Sol (max) on ChatGPT Plus | 0.00 (+0.00) | 0.00 (+0.00) | 1.13 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.00 (+0.00) |
| GPT-6.1 Sol (max) on ChatGPT Pro 100 | 0.00 (+0.00) | 0.00 (+0.00) | 1.13 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.00 (+0.00) |
| GPT-6.1 Sol (max) on ChatGPT Pro 200 | 0.00 (+0.00) | 0.00 (+0.00) | 1.13 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.00 (+0.00) |
| GPT-6.1 Sol (max) on ChatGPT Pro 500 | 0.00 (+0.00) | 0.00 (+0.00) | 1.13 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.00 (+0.00) |
| Gemini 4 Argon (high) on API-cost fallback | 0.00 (+0.00) | 0.00 (+0.00) | 1.19 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.00 (+0.00) |

### Named S2 specification branches

- **Bug Hunt harness band (E19)** (S2): unevaluable; the captured tbench.ai leaderboard lists no configuration under two or more agents, so no cross-agent spread exists
- **cache-hit variation (E34)** (S2): unevaluable; AA's published cost embeds its cache-pricing protocol; varying the cache-hit rate needs each basket component's cache-read and uncached-input demand, which AA publishes only for the whole Index (E157)
- **first-party list versus cross-provider median price rule (E122)** (S2): unevaluable; AA publishes one price per configuration under its own rule; the alternative rule's prices are not captured

### Cheapest-above-the-bar labels (API basis)

The 90% rule's error bound holds per published event (candidate and kernel assignment); it is not corrected across the listed candidates (E198). Each kernel assignment code gives the kernel used for the candidate and the competitors, in that order (U uniform, H endpoint-heavy; a quality-level bar has no reference rows, so it takes no letter); the label needs every assignment met.

| Bar | Candidate | Reading | Frequency range | Kernel assignments | Label |
|---|---|---|---|---|---|
| quality 63.5 | GPT-6.1 Sol (max) | supported under all registered role-group kernel checks | 100.0% to 100.0% | UU met, UH met, HU met, HH met | yes |
| quality 53.3 | DeepSeek V4.1 Flash 1017 (max) | supported under all registered role-group kernel checks | 100.0% to 100.0% | UU met, UH met, HU met, HH met | yes |
| quality 64.9 | Claude Sonnet 5.5 (max) | not scenario-supported | 49.4% to 50.2% | UU not met, UH not met, HU not met, HH not met | no |
| quality 64.9 | GPT-6 Astra (max) | not scenario-supported | 49.9% to 50.3% | UU not met, UH not met, HU not met, HH not met | no |

## Diagnostics

- **Terminal-Bench cross-source agreement (AA's mini-SWE-agent run against tbench.ai):** defined; 0 rows take the leaf from tbench.ai (gap fill).
- **Rank separability (O39, independent-task approximation):** median separation 2.76 value points (API) and 2.76 (Plan); separable adjacent ranks: API 0 of 8, Plan 2 of 10. Assumptions: tasks are independent and each leaf's score is a mean over its published task count (plug-in binomial with the proportion (k + 1/2) / (n + 1), I28); attempts averaged within a task and tasks shared across models are ignored, so the noise is approximate; GDPval-AA: each row's rating interval as AA's model page displays it, read as a 95% normal interval (AA states no level), SD = half-width / 1.96; AA-Omniscience: each of 6,000 questions scores +1, 0 or -1, with the shares from AA's accuracy and hallucination rate; Vals boards (Vibe Code Bench v1.1, Code Migration v1.1): Vals' published standard error per record, read as the leaf's SD; AI Coding Daily: judged points over its six graded projects read as a binomial share of 60 points (an assumption; the board publishes no error).
- **FrontierCode against Cognition:** FrontierCode cross-source agreement (AA against Cognition, same name and effort; E234): Kendall tau 0.77 (interval 0.58 to 0.91) on 22 rows. Cognition minus AA: mean +2.6 points, largest 11.6.
- **Gap-fill removal (E234, diagnostic):** no ranked row has a leaf from another party or the provider.
- **Bar results without the gap fills (E234, sensitivity; labels unchanged):** cheapest displayed row as published, with fills removed, and with third-party fills lowered by the mean offset 2.6 points — API quality 63.5: GPT-6.1 Sol (max) in all three; API quality 53.3: DeepSeek V4.1 Flash 1017 (max) in all three; API quality 64.9: GPT-6 Astra (max) in all three; Plan quality 63.5: GPT-6.1 Sol (max) in all three; Plan quality 53.3: GPT-6.1 Sol (max) in all three; Plan quality 64.9: Claude Sonnet 5.5 (max) in all three.
- **Harness cost (O123, S2 stress):** unevaluable: no model is listed under two or more agents in AA's Coding Agent Index capture, so no agent effect is identified (O123). Coding Agent Index agents (each part of its costed configuration; none is the run behind the FrontierCode or Terminal-Bench leaf): Claude Sonnet 5.5 (max): Claude Code; Claude Opus 5.5 (max): Claude Code; DeepSeek V4.1 Flash 1017 (max): DeepSeek Harness; GPT-6.1 Sol (max): Codex; Gemini 4 Argon (high): Antigravity CLI; GPT-6 Astra (max): Codex; Claude Haiku 5.5 (max): Claude Code; GPT-6 Luna (max): Codex.
- **Quality agreement:** quality agreement (matched-panel sensitivity): Kendall tau 0.83 (interval 0.48 to 1.00) on 9 rows.
- **Quality-substitution value agreement (API):** quality-substitution value agreement, api basis (matched-panel sensitivity): Kendall tau 0.56 (interval 0.03 to 0.94) on 9 rows.
- **Quality-substitution value agreement (Plan):** quality-substitution value agreement, plan basis (matched-panel sensitivity): Kendall tau 0.78 (interval 0.44 to 1.00) on 9 rows.
- **Disjoint-evidence agreement:** disjoint-evidence agreement (restricted evidence comparison, not an eligible ranking): Kendall tau 0.72 (interval 0.31 to 1.00) on 9 rows.
- **Quality source shares:** AA-run 66%, independent 34%.
- **Non-discriminating leaves:** lcr.
- **Group drift:** estimated; flagged: none.
- **Omniscience abstention sensitivity** (z_pen = max(0, I)): no rank changes.
- **GDPval-AA logistic sensitivity** (z = 100 / (1 + 10^((1600 - E) / 400)) against AA's pinned anchor; every other input fixed): API 7 rows move; largest move 2 (GPT-6.1 Sol (max)); Plan no rank changes.
- **Anchor stability:** trimmed anchors (P10 / 2 and P90 x 2 (diagnostic only)) give $162.37 to $18,114.82; 4 rows move; largest move 1 (Claude Opus 5.5 (max), DeepSeek V4.1 Flash 1017 (max), GPT-6 Astra (max), GPT-6.1 Sol (max)).

- **Basket readiness (E22):** priced leaves cover 53% of nominal quality weight (AutomationBench-AA, FrontierCode 1.1, GDPval-AA v2.1, AA-LCR v1.1, SciCode, Terminal-Bench 4.0 (AA run)); pending components: FrontierCode 1.1, ITBench-AA.
- **SWE cost companion (O14, diagnostic):** 8 rows evaluated; flagged far from the median ratio: Claude Haiku 5.5 (max).
- **Matched-cost diagnostic (E55):** evaluated at 51% priced quality weight; basket/matched cost-order reversals with separated intervals: 1; rank-gap warnings: 0.
- **Frontier-families anchors (E187, diagnostic):** anchors rebuilt from the 8 frontier and near-frontier references move API no rank changes (value points per cost doubling 3.04 vs 3.04 frozen); Plan no rank changes (value points per cost doubling 2.44 vs 2.44 frozen).
- **Frontier-families bar (E199, sensitivity; the frozen bar stays primary):** quality 63.5 over 9 configurations; cheapest at or above it on the API main workload: GPT-6.1 Sol (max) (confirmed) (compares 5 configurations that can qualify).
- **One row per family (E205, diagnostic; the frozen ladder and anchors stay primary):** with each family's primary configuration only (7 rows in the one-row-per-family bar population), the ladder (headline, lower quartile, upper quartile) would be 63.5 / 53.3 / 64.1 against 63.5 / 53.3 / 64.9 frozen; anchors rebuilt from its 6 references move API no rank changes (value points per cost doubling 3.04 vs 3.04 frozen); Plan no rank changes (value points per cost doubling 2.44 vs 2.44 frozen).
- **Ladder over scored rows (I28, sensitivity; the frozen ladder stays primary):** the bar population keeps full-benchmark rows that have no cost; today every such row has a cost, so the ladder is unchanged.
- **Bar currency (E207, informational):** rows reaching each frozen bar: quality 63.5: 5 of 9; quality 53.3: 7 of 9; quality 64.9: 3 of 9; the current population would freeze 63.5 / 53.3 / 64.9; lifetime until the next anchor re-freeze or methodology version, whichever comes first; no staleness flag.
- **Token mix (E208):** 1 selected routes: mix not reported: the measurement publishes no token-category shares; 6 selected routes: mix unidentified: the basket's token-category shares are set-identified only (E124), so the L1 test (above 0.30 flags mix-unmatched) is not computed.
- **Observed-range sensitivity (E219, not evidence; no label changes):** with each missing leaf inside the cohort's observed range for that leaf, quality 63.5: 5 can qualify, 4 confirmed; GPT-6.1 Sol (max) confirmed cheapest; quality 53.3: 6 can qualify, 6 confirmed; DeepSeek V4.1 Flash 1017 (max) confirmed cheapest; quality 64.9: 3 can qualify, 2 confirmed; possibly cheapest Claude Sonnet 5.5 (max), GPT-6 Astra (max).
- **What would settle the headline bar (E221, not a claim):** rows that can but need not reach quality 63.5, with the mean score their missing leaves would need: Gemini 4 Argon (high) (no missing leaf; reporting precision only).
- **Common leaf set (E226, diagnostic; scores unchanged):** without the leaves fewer than 90% of cohort rows have (none), API no rank changes; Plan no rank changes; rows reaching each bar: quality 63.5: 5 → 5; quality 53.3: 7 → 7; quality 64.9: 3 → 3; rows whose displayed quality differs from common-leaf quality by more than one cost doubling's worth: none.
- **Harness by leaf (E227):** Terminal-Bench: mini-SWE-agent 9; Bug Hunt: Claude Code 3, Codex CLI 3, Antigravity CLI 1, Claude Code / Anthropic-compatible shim 1, DeepSeek Harness / DeepSeek API 1.
- **Coding Agent Index safety refusals (O63, flagged; costs and scores unchanged):** Claude Sonnet 5.5 (45 finished by Claude Opus 4.8 of 870 attempts); Claude Opus 5.5 (76 finished by Claude Opus 4.8 or Claude Opus 5 of 870 attempts); GPT-6.1 Sol (15 blocked of 870 attempts); GPT-6 Astra (13 blocked of 870 attempts); Claude Haiku 5.5 (max) (3 finished by Claude Opus 5 of 870 attempts).

### Leave-one-component-out cost family (E172)

Each admitted basket unit removed in turn, scored on anchors rebuilt by the freeze rule (rank changes against the primary ranking; quality held fixed).

| Removed component | API rank changes | Plan rank changes | API value points per cost doubling |
|---|---|---|---:|
| Coding Agent Index | 4 rows move; largest move 4 (Claude Haiku 5.5 (max)) | no rank changes | 3.03 |
| AA-Briefcase | no rank changes | no rank changes | 3.10 |
| GDPval-AA | no rank changes | 2 rows move; largest move 1 (Claude Haiku 5.5 (max), GPT-6 Astra (max)) | 3.08 |
| GDP.pdf | 2 rows move; largest move 1 (Claude Opus 5.5 (max), GPT-6 Astra (max)) | no rank changes | 3.04 |
| AutomationBench-AA | 4 rows move; largest move 1 (Claude Opus 5.5 (max), DeepSeek V4.1 Flash 1017 (max), GPT-6 Astra (max), GPT-6.1 Sol (max)) | 2 rows move; largest move 1 (Claude Haiku 5.5 (max), GPT-6 Astra (max)) | 2.99 |
| Terminal-Bench 4.0 (AA Index run) | no rank changes | no rank changes | 3.02 |
| SciCode | no rank changes | no rank changes | 3.05 |
| AA-LCR | no rank changes | no rank changes | 3.04 |

### Subset rows: paired bridge and missing spend (E10, E173)

- **MiMo-V2.6-Pro** (subset without Coding Agent Index): Coding Agent Index is 36% of the full basket (median; 21% to 80% over 8 rows). Scored on its own subset anchors, the direction of its subset effect is not known. Paired bridge on the 8 full rows: API: the full rows' values change by 0.00 points (median; -0.94 to 5.12), 4 rows move; largest move 4 (Claude Haiku 5.5 (max)); Plan: the full rows' values change by -1.66 points (median; -2.45 to 1.40), no rank changes.

### Deletion sensitivity

| Branch | Retained nominal weight | Status | API rank changes | Plan rank changes |
|---|---:|---|---|---|
| leave-out:frontierCode | 85% | evaluated | 3 rows move; largest move 2 (Claude Opus 5.5 (max)) | 6 rows move; largest move 1 (Claude Haiku 5.5 (max), Claude Opus 5.5 (max), Claude Sonnet 5.5 (max), Gemini 4 Argon (high), GPT-6 Astra (max), MiMo-V2.6-Pro) |
| leave-out:terminalBench | 89% | evaluated | 3 rows move; largest move 2 (GPT-6.1 Sol (max)) | 2 rows move; largest move 1 (GPT-6 Astra (max), GPT-6 Luna (max)) |
| leave-out:bugHunt | 92% | evaluated | 3 rows move; largest move 2 (MiMo-V2.6-Pro) | no rank changes |
| leave-out:vibeCode | 95% | evaluated | no rank changes | 2 rows move; largest move 1 (Claude Haiku 5.5 (max), GPT-6 Astra (max)) |
| leave-out:codeMigration | 94% | evaluated | 3 rows move; largest move 2 (MiMo-V2.6-Pro) | no rank changes |
| leave-out:livebench2Overall | 85% | evaluated | 5 rows move; largest move 2 (GPT-6.1 Sol (max)) | no rank changes |
| leave-out:gdpval | 90% | evaluated | 2 rows move; largest move 1 (Claude Opus 5.5 (max), GPT-6 Astra (max)) | 4 rows move; largest move 1 (Claude Haiku 5.5 (max), Gemini 4 Argon (high), GPT-6 Astra (max), MiMo-V2.6-Pro) |
| leave-out:automationBench | 90% | evaluated | 2 rows move; largest move 1 (DeepSeek V4.1 Flash 1017 (max), MiMo-V2.6-Pro) | no rank changes |
| leave-out:omniscience | 90% | evaluated | 5 rows move; largest move 2 (GPT-6.1 Sol (max)) | no rank changes |
| leave-out:lcr | 95% | evaluated | 2 rows move; largest move 1 (Claude Opus 5.5 (max), GPT-6 Astra (max)) | 2 rows move; largest move 1 (Claude Haiku 5.5 (max), GPT-6 Astra (max)) |
| leave-out:hle | 98% | evaluated | 2 rows move; largest move 1 (Claude Opus 5.5 (max), GPT-6 Astra (max)) | no rank changes |
| leave-out:scicode | 98% | evaluated | 2 rows move; largest move 1 (Claude Opus 5.5 (max), GPT-6 Astra (max)) | no rank changes |
| leave-out:critpt | 98% | evaluated | no rank changes | no rank changes |
| leave-source-out:Artificial Analysis | 34% | not identifiable under the coverage rule | — | — |
| leave-source-out:Vals AI | 89% | evaluated | 3 rows move; largest move 2 (MiMo-V2.6-Pro) | no rank changes |
| basket-scope | 87% | evaluated | 5 rows move; largest move 2 (Claude Sonnet 5.5 (max)) | no rank changes |

### Cost-component removal (Terminal-Bench 4.0 (AA Index run): evaluated)

| Basis | Run | Rank changes |
|---|---|---|
| api | cost-component removal, original anchors | 2 rows move; largest move 1 (DeepSeek V4.1 Flash 1017 (max), GPT-6.1 Sol (max)) |
| api | alternative workload, recalibrated anchors | no rank changes |
| plan | cost-component removal, original anchors; fixed-multiple arithmetic stress (not identified Plan economics for the altered workload) | no rank changes |
| plan | alternative workload, recalibrated anchors; fixed-multiple arithmetic stress (not identified Plan economics for the altered workload) | no rank changes |

## Release gates

| Rule | Status | Detail |
|---|---|---|
| clip gate (E20) | passed | no basis exceeds the clipping allowance |
| cost influence flag (E91) | passed | cost not discriminating (< 10%); informational only; beta never changes (O2) |
| quality influence flag (E126) | passed | quality not discriminating (cost share > 90%); informational only |
| subset scoring (O17) | fired | subset rows scored on their own workload and anchors |
| partial component flag (E37) | vacuous | AA declined- or missing-task markers, or an Index reconstruction that misses AA's total (E209) |
| route dominance filter (E88) | vacuous | certifiably dearer routes set aside |
| Plan exploratory label (E61) | fired | fewer than half of Plan rows have an identified M_W |
| Plan evidence lifecycle and change detection (E18, E151, E269, O77, O79) | fired | 21 of 27 plan rows carry a possibly-superseded or expired route: claude-haiku-5-5-max@claude-max-20x, claude-haiku-5-5-max@claude-max-5x, claude-haiku-5-5-max@claude-pro, claude-opus-5-5@claude-max-20x, claude-opus-5-5@claude-max-5x, claude-opus-5-5@claude-pro, claude-sonnet-5-5@claude-max-20x, claude-sonnet-5-5@claude-max-5x, claude-sonnet-5-5@claude-pro, gpt-6-astra@chatgpt-plus, gpt-6-astra@chatgpt-pro-100, gpt-6-astra@chatgpt-pro-200, gpt-6-astra@chatgpt-pro-500, gpt-6-luna@chatgpt-plus, gpt-6-luna@chatgpt-pro-100, gpt-6-luna@chatgpt-pro-200, gpt-6-luna@chatgpt-pro-500, gpt-6.1-sol@chatgpt-plus, gpt-6.1-sol@chatgpt-pro-100, gpt-6.1-sol@chatgpt-pro-200, gpt-6.1-sol@chatgpt-pro-500 |
| acknowledged accounting-fault windows (O91, O92, O93, O95, O96) | fired | 3 of 27 plan rows rest on a measurement inside an acknowledged fault window; they stay selected and yield to two concordant user reports for their own model and plan, and the transfers resting on them follow: gpt-6-astra@chatgpt-pro-500, gpt-6-luna@chatgpt-pro-500, gpt-6.1-sol@chatgpt-pro-500 |
| AA cost omits a pricing term (O94, O98, O100, O106, O108, O109, O114) | fired | ranked at the published cost; compete in interval outputs and the scenario labels' BlockerSafe test over [C, factor × C] ([C, ∞) without a stated factor, O98) without a label (scenario frequencies draw them at the published cost, O114), and leave the anchor population at the next freeze: claude-haiku-5-5-max (up to 5×) |
| valuation-basis gate (E170) | passed | every ranked row is compatible as captured or after evidenced revaluation |
| source clocks and evidence freshness (O59, O60, O65, E211, E216, E217, E218) | passed | every capture is within its age gate and none after the cutoff unless its source predates the cutoff's day; the build stops otherwise |
| build-stopping evidence gates (O64, O69, O71, O75, O99, O100, O101, O103, O105-O111, E195, E204, E225) | passed | the Coding Agent Index manifest (O64), the Terminal-Bench agent list (E225), cutoff-day row dates (O69), the three-stage all-provider plan search (O71, O75), the typed change records behind every route flag and partition split, which also produce each route's label and blocking dates within its launch- and schedule-bounded span (O99, O101, O105, O107, O110, O111), the register of AA notes covering every captured one, with the chart's inventory and duplicate-entry checks, the post-O103 capture notes, the basket-chart labels and chart-level notes' named rows (O100, O103, O106, O108) and the frontier path checks (E195, E204) hold; the build stops otherwise |
| score swing gate (E177) | vacuous | first v3 release: no previous v3 release to compare |
| anchor migration (E184) | vacuous | no main-workload migration deferred |
| configuration map coverage | passed | every cohort row has a configuration-map entry |
| quality clipping audit (E110) | passed | saturation disclosed; domain violations block the build |
| full benchmark set (O36, O38) | fired | listed, not ranked: kimi-k3-1-pro, gpt-6.1-sol-high, claude-opus-5-5-high, claude-opus-5-5-medium, gpt-6.1-sol-medium, gpt-6-astra-high, claude-haiku-5-5-high, gpt-6-luna-xhigh, claude-haiku-5-5-medium, gpt-6-luna-high, gpt-6-luna-medium, gpt-5.6-luna-low, claude-haiku-5-5, claude-haiku-5-5-low, claude-opus-5-5-xhigh, claude-sonnet-5-5-xhigh, gpt-6-astra-xhigh, gpt-6-luna-low, gpt-6.1-sol-xhigh, mimo-v2-6-flash, minimax-m3-1-flash |
| missing-leaf rules (O8 provisional, E198b, E201b, E219, E221, E226) | vacuous | no ranked row has a missing leaf (O36) |
| S1M interval stream (E145) | vacuous | dormant: no ranked leaf carries a published confidence interval since O37, so S1M equals S1 (E236) |
| provider-claim label denial (E233) | vacuous | no row has a provider-claimed leaf |
| scenario outputs current (E72) | passed | scenario input hash matches the scored inputs |
