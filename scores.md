# ValueRank v3.0.0 Scores

**Updated:** October 19, 2026 · methodology 3.0.0 · SDLC basket v1 · anchor version `v3-2026-10-23`

Value = 25% × cost score + 75% × quality. Costs are USD per basket run; the cost score is log-scaled against the frozen anchors of the row's workload (see [methodology.md](methodology.md)).

## Ranking

| Configuration | Plan rank | Plan value | Plan cost score | API rank | API value | API cost score | Quality | Quality coverage | Workload |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| [Claude Opus 5.5 (max)](https://valuerank.alolabs.dev/models/claude-opus-5-5/) | 1 | 62.33 | 53.51 | 6 | 51.99 | 12.17 | 65.26 | 100% | main |
| [Claude Sonnet 5.5 (max)](https://valuerank.alolabs.dev/models/claude-sonnet-5-5/) | 4 | 62.13 | 54.16 | 7 | 51.83 | 12.98 | 64.78 | 100% | main |
| [GPT-6.1 Sol (max)](https://valuerank.alolabs.dev/models/gpt-6-1-sol/) | 7 | 60.32 | 58.11 | 1 | 57.72 | 47.74 | 61.05 | 100% | main |
| [Claude Haiku 5.5 (max)](https://valuerank.alolabs.dev/models/claude-haiku-5-5-max/) | 11 | 56.84 | 85.44 | 9 | 48.48 | 52.01 | 47.30 | 100% | main |
| [GPT-6 Astra (max)](https://valuerank.alolabs.dev/models/gpt-6-astra/) | 14 | 56.66 | 40.29 | 8 | 51.66 | 20.30 | 62.12 | 100% | main |
| [GPT-6 Luna (max)](https://valuerank.alolabs.dev/models/gpt-6-luna/) | 17 | 54.87 | 90.25 | 4 | 54.27 | 87.83 | 43.08 | 100% | main |
| [MiMo-V2.6-Pro](https://valuerank.alolabs.dev/models/mimo-v2-6-pro/) | 22 | 48.54 | 44.90 | 2 | 56.94 | 78.48 | 49.76 | 100% | subset |
| [DeepSeek V4.1 Flash 1017 (max)](https://valuerank.alolabs.dev/models/deepseek-v4-1-flash-1017/) | 24 | 48.30 | 31.54 | 3 | 56.24 | 63.30 | 53.88 | 100% | subset |
| [Gemini 4 Argon (high)](https://valuerank.alolabs.dev/models/gemini-4-argon/) | 25 | 47.98 | 9.75 | 5 | 52.83 | 29.14 | 60.72 | 100% | main |

## Not ranked

| Model | Reasons |
|---|---|
| Claude Fable 5 | Not plotted on or within the near gap of AA's rendered frontier (O51) |
| Claude Fable 5.1 | Not plotted on or within the near gap of AA's rendered frontier (O51) |
| Claude Haiku 5.5 | Incomplete benchmark evidence after an exhaustive search (O36, O53): Max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Long Agentic, LiveBench 2.0 Coding; AI Coding Daily ranking: no AI Coding Daily (excl. bug finding) |
| Claude Haiku 5.5 (high) | Not in the max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Long Agentic, LiveBench 2.0 Coding; ranked in the AI Coding Daily ranking |
| Claude Haiku 5.5 (low) | Incomplete benchmark evidence after an exhaustive search (O36, O53): Max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Long Agentic, LiveBench 2.0 Coding; AI Coding Daily ranking: no AI Coding Daily (excl. bug finding) |
| Claude Haiku 5.5 (medium) | Not in the max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Long Agentic, LiveBench 2.0 Coding; ranked in the AI Coding Daily ranking |
| Claude Opus 4.8 | Not plotted on or within the near gap of AA's rendered frontier (O51) |
| Claude Opus 5 | Not plotted on or within the near gap of AA's rendered frontier (O51) |
| Claude Opus 5.5 (high) | Not in the max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Long Agentic, LiveBench 2.0 Coding; ranked in the AI Coding Daily ranking |
| Claude Opus 5.5 (medium) | Not in the max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Long Agentic, LiveBench 2.0 Coding; ranked in the AI Coding Daily ranking |
| Claude Opus 5.5 (xhigh) | Incomplete benchmark evidence after an exhaustive search (O36, O53): Max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Long Agentic, LiveBench 2.0 Coding; AI Coding Daily ranking: no AI Coding Daily (excl. bug finding) |
| Claude Sonnet 5 | Not plotted on or within the near gap of AA's rendered frontier (O51) |
| Claude Sonnet 5.5 (high) | Not plotted on or within the near gap of AA's rendered frontier (O51) |
| Claude Sonnet 5.5 (low) | Not plotted on or within the near gap of AA's rendered frontier (O51) |
| Claude Sonnet 5.5 (medium) | Not plotted on or within the near gap of AA's rendered frontier (O51) |
| Claude Sonnet 5.5 (xhigh) | Incomplete benchmark evidence after an exhaustive search (O36, O53): Max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Long Agentic, LiveBench 2.0 Coding; AI Coding Daily ranking: no AI Coding Daily (excl. bug finding) |
| DeepSeek V4 Flash | Not plotted on or within the near gap of AA's rendered frontier (O51) |
| DeepSeek V4 Pro | Not plotted on or within the near gap of AA's rendered frontier (O51) |
| GLM-5.2 | No eligible exact-model Bug Hunt result in the selected source snapshot; Not plotted on or within the near gap of AA's rendered frontier (O51) |
| GLM-5.3 | Not plotted on or within the near gap of AA's rendered frontier (O51) |
| GLM-5.3 Flash | Not plotted on or within the near gap of AA's rendered frontier (O51) |
| GPT-5.5 | No eligible exact-model Bug Hunt result in the selected source snapshot; Not plotted on or within the near gap of AA's rendered frontier (O51) |
| GPT-5.6 Luna | Not plotted on or within the near gap of AA's rendered frontier (O51) |
| GPT-5.6 Luna (low) | Not in the max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Long Agentic, LiveBench 2.0 Coding; ranked in the AI Coding Daily ranking |
| GPT-5.6 Sol | Not plotted on or within the near gap of AA's rendered frontier (O51) |
| GPT-6 Astra (high) | Not in the max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Long Agentic, LiveBench 2.0 Coding; ranked in the AI Coding Daily ranking |
| GPT-6 Astra (xhigh) | Incomplete benchmark evidence after an exhaustive search (O36, O53): Max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Long Agentic, LiveBench 2.0 Coding; AI Coding Daily ranking: no AI Coding Daily (excl. bug finding) |
| GPT-6 Luna (high) | Not in the max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Long Agentic, LiveBench 2.0 Coding; ranked in the AI Coding Daily ranking |
| GPT-6 Luna (low) | Incomplete benchmark evidence after an exhaustive search (O36, O53): Max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Long Agentic, LiveBench 2.0 Coding; AI Coding Daily ranking: no AI Coding Daily (excl. bug finding) |
| GPT-6 Luna (medium) | Not in the max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Long Agentic, LiveBench 2.0 Coding; ranked in the AI Coding Daily ranking |
| GPT-6 Luna (xhigh) | Not in the max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Long Agentic, LiveBench 2.0 Coding; ranked in the AI Coding Daily ranking |
| GPT-6 Sol | Not plotted on or within the near gap of AA's rendered frontier (O51) |
| GPT-6.1 Sol (high) | Not in the max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Long Agentic, LiveBench 2.0 Coding; ranked in the AI Coding Daily ranking |
| GPT-6.1 Sol (low) | Not plotted on or within the near gap of AA's rendered frontier (O51) |
| GPT-6.1 Sol (medium) | Not in the max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Long Agentic, LiveBench 2.0 Coding; ranked in the AI Coding Daily ranking |
| GPT-6.1 Sol (xhigh) | Incomplete benchmark evidence after an exhaustive search (O36, O53): Max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Long Agentic, LiveBench 2.0 Coding; AI Coding Daily ranking: no AI Coding Daily (excl. bug finding) |
| Gemini 3.5 Flash | No eligible exact-model Bug Hunt result in the selected source snapshot; Not plotted on or within the near gap of AA's rendered frontier (O51) |
| Gemini 3.6 Flash | No eligible exact-model Bug Hunt result in the selected source snapshot; Not plotted on or within the near gap of AA's rendered frontier (O51) |
| Gemini 3.7 Flash | No eligible exact-model Bug Hunt result in the selected source snapshot; Not plotted on or within the near gap of AA's rendered frontier (O51) |
| Gemini 3.8 Flash | Not plotted on or within the near gap of AA's rendered frontier (O51) |
| Grok 4.6 | No eligible exact-model Bug Hunt result in the selected source snapshot; Not plotted on or within the near gap of AA's rendered frontier (O51) |
| Grok 4.6 (xhigh) | Not plotted on or within the near gap of AA's rendered frontier (O51) |
| Grok 4.7 | Not plotted on or within the near gap of AA's rendered frontier (O51) |
| Kimi K3 | No eligible exact-model Bug Hunt result in the selected source snapshot; Not plotted on or within the near gap of AA's rendered frontier (O51) |
| MiMo-V2.6-Flash | Incomplete benchmark evidence after an exhaustive search (O36, O53): Max-effort ranking: no Bug Hunt Bench, Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Long Agentic, LiveBench 2.0 Coding; AI Coding Daily ranking: no Bug Hunt Bench, AI Coding Daily (excl. bug finding) |
| MiniMax-M3.1-Flash | Incomplete benchmark evidence after an exhaustive search (O36, O53): Max-effort ranking: no Bug Hunt Bench, Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Long Agentic, LiveBench 2.0 Coding; AI Coding Daily ranking: no Bug Hunt Bench, AI Coding Daily (excl. bug finding) |
| Muse Spark 1.2 | No eligible exact-model Bug Hunt result in the selected source snapshot; Not plotted on or within the near gap of AA's rendered frontier (O51) |
| Muse Spark 1.3 | Not plotted on or within the near gap of AA's rendered frontier (O51) |
| Muse Spark 1.3 (xhigh) | Not plotted on or within the near gap of AA's rendered frontier (O51) |
| Muse Wonder | Not plotted on or within the near gap of AA's rendered frontier (O51) |
| Muse Wonder Full | Not plotted on or within the near gap of AA's rendered frontier (O51) |
| Qwen3.8 Max | Not plotted on or within the near gap of AA's rendered frontier (O51) |

## Quality leaf scores

Each leaf's score z on its fixed 0–100 anchors; "—" marks a leaf with no eligible exact-configuration result.

| Configuration | FrontierCode 1.1 | Terminal-Bench 4.0 (AA run) | Bug Hunt Bench | Vibe Code Bench v1.1 (Vals) | Code Migration v1.1 (Vals) | LiveBench 2.0 Long Agentic | LiveBench 2.0 Coding | GDPval-AA v2.1 | AutomationBench-AA | AA-Omniscience | AA-LCR v1.1 | Humanity's Last Exam | SciCode | CritPt | Quality | Provisional |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Claude Opus 5.5 (max) | 52.2 | 59.6 | 39.7 | 90.3 | 81.0 | 85.0 | 96.3 | 68.3 | 69.5 | 73.2 | 84.7 | 61.4 | 66.9 | 31.7 | 65.26 | no |
| Claude Sonnet 5.5 (max) | 45.8 | 63.6 | 48.9 | 92.4 | 86.9 | 78.8 | 94.7 | 66.9 | 71.8 | 66.2 | 82.7 | 55.0 | 61.0 | 31.4 | 64.78 | no |
| GPT-6.1 Sol (max) | 49.1 | 56.1 | 42.2 | 88.9 | 77.3 | 73.0 | 96.0 | 54.6 | 64.9 | 70.8 | 83.0 | 52.9 | 54.2 | 31.7 | 61.05 | no |
| Claude Haiku 5.5 (max) | 41.8 | 32.8 | 20.5 | 90.4 | 52.4 | 57.6 | 91.4 | 55.9 | 35.4 | 55.3 | 82.7 | 44.4 | 55.0 | 18.9 | 47.30 | no |
| GPT-6 Astra (max) | 47.0 | 59.1 | 42.9 | 89.6 | 80.6 | 82.4 | 93.7 | 53.6 | 68.5 | 71.7 | 80.7 | 54.7 | 56.5 | 31.7 | 62.12 | no |
| GPT-6 Luna (max) | 41.9 | 12.6 | 17.4 | 81.6 | 46.7 | 48.1 | 84.5 | 46.6 | 53.2 | 50.3 | 83.3 | 38.5 | 54.6 | 19.4 | 43.08 | no |
| MiMo-V2.6-Pro | 45.4 | 34.8 | 17.1 | 85.2 | 48.8 | 47.5 | 81.5 | 59.2 | 58.6 | 54.2 | 86.3 | 49.4 | 60.9 | 26.6 | 49.76 | no |
| DeepSeek V4.1 Flash 1017 (max) | 43.7 | 33.8 | 40.7 | 87.7 | 67.5 | 50.9 | 96.0 | 62.3 | 66.6 | 52.4 | 82.7 | 43.3 | 55.9 | 24.0 | 53.88 | no |
| Gemini 4 Argon (high) | 43.5 | 57.1 | 38.8 | 91.9 | 70.8 | 69.9 | 89.7 | 56.2 | 77.5 | 71.2 | 79.7 | 57.1 | 61.8 | 27.1 | 60.72 | no |

## AI Coding Daily ranking

The configurations AI Coding Daily has tested, mostly at high and medium effort, scored on the AA leaves plus AI Coding Daily. Anchor version `v3-2026-10-23-aicd`; leaves: FrontierCode 1.1 21%, Terminal-Bench 4.0 (AA run) 17%, Bug Hunt Bench 12%, AI Coding Daily (excl. bug finding) 10% (software engineering 60%), plus the 7 leaves outside software engineering every ranking shares.

| Configuration | Plan rank | Plan value | Plan cost score | API rank | API value | API cost score | Quality | Quality coverage | Workload |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| [Claude Opus 5.5 (high)](https://valuerank.alolabs.dev/models/claude-opus-5-5-high/) | 1 | 58.11 | 52.03 | 6 | 48.94 | 15.34 | 60.13 | 100% | main |
| [Claude Opus 5.5 (medium)](https://valuerank.alolabs.dev/models/claude-opus-5-5-medium/) | 4 | 57.99 | 54.95 | 5 | 49.17 | 19.70 | 59.00 | 100% | main |
| [GPT-6.1 Sol (high)](https://valuerank.alolabs.dev/models/gpt-6-1-sol-high/) | 7 | 55.23 | 49.45 | 1 | 52.66 | 39.19 | 57.16 | 100% | main |
| [GPT-6.1 Sol (medium)](https://valuerank.alolabs.dev/models/gpt-6-1-sol-medium/) | 11 | 53.84 | 52.77 | 2 | 51.68 | 44.14 | 54.19 | 100% | main |
| [Claude Haiku 5.5 (high)](https://valuerank.alolabs.dev/models/claude-haiku-5-5-high/) | 14 | 53.52 | 87.70 | 7 | 48.75 | 68.64 | 42.13 | 100% | main |
| [Claude Haiku 5.5 (medium)](https://valuerank.alolabs.dev/models/claude-haiku-5-5-medium/) | 18 | 51.91 | 92.44 | 10 | 47.73 | 75.71 | 38.40 | 100% | main |
| [GPT-6 Astra (high)](https://valuerank.alolabs.dev/models/gpt-6-astra-high/) | 21 | 51.64 | 30.79 | 12 | 46.77 | 11.30 | 58.59 | 100% | main |
| [GPT-6 Luna (max)](https://valuerank.alolabs.dev/models/gpt-6-luna/) | 25 | 49.04 | 67.89 | 8 | 48.75 | 66.74 | 42.75 | 100% | main |
| [GPT-6 Luna (xhigh)](https://valuerank.alolabs.dev/models/gpt-6-luna-xhigh/) | 29 | 46.77 | 73.09 | 11 | 47.13 | 74.51 | 38.00 | 100% | main |
| [MiMo-V2.6-Pro](https://valuerank.alolabs.dev/models/mimo-v2-6-pro/) | 32 | 46.41 | 37.90 | 3 | 51.43 | 57.98 | 49.24 | 100% | main |
| [DeepSeek V4.1 Flash 1017 (max)](https://valuerank.alolabs.dev/models/deepseek-v4-1-flash-1017/) | 33 | 46.27 | 26.62 | 4 | 50.58 | 43.84 | 52.82 | 100% | main |
| [Gemini 4 Argon (high)](https://valuerank.alolabs.dev/models/gemini-4-argon/) | 37 | 45.91 | 7.56 | 9 | 47.86 | 15.36 | 58.70 | 100% | main |
| [GPT-6 Luna (high)](https://valuerank.alolabs.dev/models/gpt-6-luna-high/) | 39 | 45.88 | 76.13 | 13 | 46.61 | 79.06 | 35.80 | 100% | main |
| [GPT-6 Luna (medium)](https://valuerank.alolabs.dev/models/gpt-6-luna-medium/) | 43 | 44.31 | 80.41 | 14 | 45.57 | 85.46 | 32.28 | 100% | main |
| [GPT-5.6 Luna (low)](https://valuerank.alolabs.dev/models/gpt-5-6-luna-low/) | 47 | 36.63 | 82.58 | 15 | 38.16 | 88.70 | 21.31 | 100% | main |

### AI Coding Daily ranking: quality leaf scores

| Configuration | FrontierCode 1.1 | Terminal-Bench 4.0 (AA run) | Bug Hunt Bench | AI Coding Daily (excl. bug finding) | GDPval-AA v2.1 | AutomationBench-AA | AA-Omniscience | AA-LCR v1.1 | Humanity's Last Exam | SciCode | CritPt | Quality | Provisional |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Claude Opus 5.5 (high) | 54.0 | 56.6 | 30.2 | 96.1 | 60.2 | 63.2 | 70.3 | 82.7 | 55.6 | 60.4 | 30.9 | 60.13 | no |
| Claude Opus 5.5 (medium) | 57.1 | 52.5 | 28.9 | 94.9 | 54.1 | 61.2 | 70.2 | 84.3 | 54.7 | 59.3 | 27.7 | 59.00 | no |
| GPT-6.1 Sol (high) | 46.6 | 51.5 | 34.8 | 94.7 | 50.4 | 64.5 | 70.7 | 82.3 | 51.4 | 55.8 | 30.0 | 57.16 | no |
| GPT-6.1 Sol (medium) | 43.3 | 48.0 | 27.6 | 92.8 | 47.4 | 62.6 | 70.0 | 83.3 | 49.9 | 53.2 | 27.7 | 54.19 | no |
| Claude Haiku 5.5 (high) | 43.6 | 21.7 | 15.2 | 85.9 | 45.8 | 33.7 | 52.9 | 77.3 | 37.3 | 48.7 | 18.6 | 42.13 | no |
| Claude Haiku 5.5 (medium) | 40.4 | 15.2 | 11.4 | 85.5 | 38.6 | 28.6 | 52.2 | 77.3 | 33.8 | 49.0 | 12.9 | 38.40 | no |
| GPT-6 Astra (high) | 50.9 | 54.0 | 33.3 | 94.6 | 51.1 | 66.6 | 71.9 | 80.0 | 53.1 | 55.4 | 28.9 | 58.59 | no |
| GPT-6 Luna (max) | 41.9 | 12.6 | 17.4 | 86.7 | 46.6 | 53.2 | 50.3 | 83.3 | 38.5 | 54.6 | 19.4 | 42.75 | no |
| GPT-6 Luna (xhigh) | 33.2 | 8.1 | 13.3 | 83.2 | 43.1 | 47.8 | 49.1 | 80.0 | 34.3 | 51.7 | 17.4 | 38.00 | no |
| MiMo-V2.6-Pro | 45.4 | 34.8 | 17.1 | 79.3 | 59.2 | 58.6 | 54.2 | 86.3 | 49.4 | 60.9 | 26.6 | 49.24 | no |
| DeepSeek V4.1 Flash 1017 (max) | 43.7 | 33.8 | 40.7 | 87.1 | 62.3 | 66.6 | 52.4 | 82.7 | 43.3 | 55.9 | 24.0 | 52.82 | no |
| Gemini 4 Argon (high) | 43.5 | 57.1 | 38.8 | 83.2 | 56.2 | 77.5 | 71.2 | 79.7 | 57.1 | 61.8 | 27.1 | 58.70 | no |
| GPT-6 Luna (high) | 32.0 | 4.5 | 8.6 | 79.5 | 42.0 | 47.8 | 47.2 | 79.3 | 32.9 | 50.3 | 15.4 | 35.80 | no |
| GPT-6 Luna (medium) | 31.8 | 2.5 | 3.8 | 67.0 | 38.1 | 40.5 | 47.5 | 78.3 | 28.3 | 50.9 | 10.6 | 32.28 | no |
| GPT-5.6 Luna (low) | 15.4 | 0.0 | 3.8 | 50.9 | 24.6 | 11.7 | 42.7 | 70.0 | 19.8 | 46.1 | 2.6 | 21.31 | no |


## Basket cost by component

USD at API rates for the exact configuration; "—" marks a component without an exact cost.

| Configuration | Coding Agent Index | ITBench-AA | AA-Briefcase | GDPval-AA | GDP.pdf | AutomationBench-AA | Terminal-Bench 4.0 (AA Index run) | SciCode | AA-LCR | Basket cost | Missing admitted components |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Claude Opus 5.5 (max) | $3,312.59 | $146.00 | $1,915.18 | $1,962.05 | $155.23 | $938.69 | $865.21 | $135.11 | $67.66 | $9,351.72 | none |
| Claude Sonnet 5.5 (max) | $3,857.44 | — | $1,863.13 | $1,504.30 | $79.43 | $678.32 | $834.67 | $80.07 | $33.93 | $8,931.28 | none |
| GPT-6.1 Sol (max) | $436.35 | — | $210.45 | $196.57 | $41.99 | $195.01 | $120.30 | $12.50 | $19.94 | $1,233.11 | none |
| Claude Haiku 5.5 (max) | $775.43 | — | $61.41 | $48.90 | $5.27 | $27.80 | $43.02 | $3.15 | $1.93 | $966.92 | none |
| GPT-6 Astra (max) | $2,040.49 | $133.00 | $864.69 | $996.49 | $207.58 | $1,048.30 | $560.88 | $66.89 | $99.73 | $5,885.05 | none |
| GPT-6 Luna (max) | $46.16 | — | $15.47 | $19.66 | $2.85 | $23.91 | $15.59 | $1.06 | $1.02 | $125.72 | none |
| MiMo-V2.6-Pro | — | — | $34.60 | $35.47 | $2.40 | $27.77 | $28.91 | $2.25 | $4.74 | $136.13 | Coding Agent Index |
| DeepSeek V4.1 Flash 1017 (max) | — | — | $61.72 | $77.91 | $4.23 | $114.26 | $58.09 | $4.65 | $3.26 | $324.12 | Coding Agent Index |
| Gemini 4 Argon (high) | $1,699.83 | — | $530.33 | $400.23 | $25.93 | $399.89 | $447.49 | $30.44 | $23.64 | $3,557.77 | none |

### Valuation basis

Valuation-basis gate (E170): 9 compatible as captured. AA's Index category costs reconcile exactly with the prices AA displays for each configuration at capture, so its applied prices are the prices in force at the release cutoff. Token metering (E176): 9 not published per configuration; AA values cached input at live measurements of each model's typical cache-hit rate. Source intervals (E174): terminalBench: captured, level 95% (tbench.ai: "The whiskers span the 95% confidence interval"); gdpval: published, not captured, level not stated by the source (the 95% level on AA's methodology page belongs to AA-Briefcase).

## Plan route selection

The Plan amount is the selected multiple times the cash paid for the fee period (E166), typed by what the measurement establishes; it is not capacity unless it says so. The multiple values only the measured workload's API-equivalent consumption; other plan features are not valued.

| Configuration | Selected route | Plan amount | Basket runs per fee period | Identification | Plan cost (USD per basket run) | Flags | Selection reason |
|---|---|---|---|---|---:|---|---|
| Claude Opus 5.5 (max) | Claude Pro $20 · Opus 5.5 (58.9×, measured) | $1,178 per month: measured-workload capacity | 0.13 per month | unidentified | $158.77 | workload-unmatched; valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| Claude Sonnet 5.5 (max) | Claude Pro $20 · common Claude assumption (58.9×, assumption) | $1,178 per month: assumed API-equivalent consumption (owner-named transfer) from claude-pro-opus55-semianalysis | 0.13 per month | unidentified | $151.63 | workload-unmatched; owner-named transfer (assumption); valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| GPT-6.1 Sol (max) | ChatGPT Pro 500 $500 · GPT-6.1 Sol (10.772×, measured) | $5,386 per month: measured-workload capacity | 4.37 per month | unidentified | $114.47 | workload-unmatched; valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| Claude Haiku 5.5 (max) | Claude Pro $20 · common Claude assumption (58.9×, assumption) | $1,178 per month: assumed API-equivalent consumption (owner-named transfer) from claude-pro-opus55-semianalysis | 1.22 per month | unidentified | $16.42 | workload-unmatched; owner-named transfer (assumption); valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| GPT-6 Astra (max) | ChatGPT Pro 200 $200 · GPT-6 Astra (14.485×, measured) | $2,897 per month: measured-workload capacity | 0.49 per month | unidentified | $406.29 | workload-unmatched; valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| GPT-6 Luna (max) | ChatGPT Pro 500 $500 · common GPT assumption (10.772×, assumption) | $5,386 per month: assumed API-equivalent consumption (owner-named transfer) from chatgpt-pro500-gpt61sol-semianalysis | 42.84 per month | unidentified | $11.67 | workload-unmatched; owner-named transfer (assumption); valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| MiMo-V2.6-Pro | MiMo Token Plan Max $100 · quota ceiling (provider-derived) (1.1808×, assumption) | $118 per month: assumed API-equivalent consumption (owner-named transfer) | 0.87 per month | unidentified | $115.28 | workload-unmatched; owner-named transfer (assumption); valuation basis unverified; observed-usage multiple; full utilisation not established | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| DeepSeek V4.1 Flash 1017 (max) | — | — | — | — | $324.12 | API-cost fallback: no admitted Plan route; cross-estimand ordering not identified | no eligible route |
| Gemini 4 Argon (high) | — | — | — | — | $3,557.77 | API-cost fallback: no admitted Plan route; cross-estimand ordering not identified | no eligible route |

### Route alternatives

Every admissible route-measurement pair in comparator order (E171) and the comparator's pick with the selected pair removed (E179). A larger displayed multiple is arithmetic on the measured workload, never a claim that the route is cheaper on the scored workload. Workday-feasible multiple (E15), for the 7 routed rows: not evaluated: no evidenced quota schema for this route.

| Configuration | Admissible pairs | Unidentified | Pairs (multiple, status) | Leave-selected-out choice |
|---|---:|---:|---|---|
| Claude Opus 5.5 (max) | 3 | 3 | claude-pro-opus55-semianalysis (58.9×, selected); claude-max20x-opus55-semianalysis (58.63×, not selected by the comparator); claude-max5x-opus55-semianalysis (57.25×, not selected by the comparator) | claude-max20x-opus55-semianalysis (58.63×, value 62.31) |
| Claude Sonnet 5.5 (max) | 3 | 3 | claude-pro-claude-sonnet-5-5-common-opus55-assumption (58.9×, selected); claude-max20x-claude-sonnet-5-5-common-opus55-assumption (58.63×, not selected by the comparator); claude-max5x-claude-sonnet-5-5-common-opus55-assumption (57.25×, not selected by the comparator) | claude-max20x-claude-sonnet-5-5-common-opus55-assumption (58.63×, value 62.11) |
| GPT-6.1 Sol (max) | 4 | 4 | chatgpt-pro500-gpt61sol-semianalysis (10.772×, selected); chatgpt-plus-gpt61sol-semianalysis (10.55×, not selected by the comparator); chatgpt-pro100-gpt61sol-semianalysis (10.55×, not selected by the comparator); chatgpt-pro200-gpt61sol-semianalysis (10.42×, not selected by the comparator) | chatgpt-plus-gpt61sol-semianalysis (10.55×, value 60.24) |
| Claude Haiku 5.5 (max) | 3 | 3 | claude-pro-claude-haiku-5-5-max-common-opus55-assumption (58.9×, selected); claude-max20x-claude-haiku-5-5-max-common-opus55-assumption (58.63×, not selected by the comparator); claude-max5x-claude-haiku-5-5-max-common-opus55-assumption (57.25×, not selected by the comparator) | claude-max20x-claude-haiku-5-5-max-common-opus55-assumption (58.63×, value 56.82) |
| GPT-6 Astra (max) | 4 | 4 | chatgpt-pro200-gpt6astra-semianalysis (14.485×, selected); chatgpt-pro500-gpt6astra-semianalysis (13.91×, not selected by the comparator); chatgpt-pro100-gpt6astra-semianalysis (13.22×, not selected by the comparator); chatgpt-plus-gpt6astra-semianalysis (8.1×, not selected by the comparator) | chatgpt-pro500-gpt6astra-semianalysis (13.91×, value 56.52) |
| GPT-6 Luna (max) | 4 | 4 | chatgpt-pro500-gpt-6-luna-common-gpt-assumption (10.772×, selected); chatgpt-pro100-gpt-6-luna-common-gpt-assumption (10.55×, not selected by the comparator); chatgpt-pro200-gpt-6-luna-common-gpt-assumption (10.42×, not selected by the comparator); chatgpt-plus-gpt-6-luna-common-gpt-assumption (8.1×, not selected by the comparator) | chatgpt-pro100-gpt-6-luna-common-gpt-assumption (10.55×, value 54.80) |
| MiMo-V2.6-Pro | 4 | 4 | mimo-tokenplan-max-mimo-v2-6-pro-quota-ceiling (1.1808×, selected); mimo-tokenplan-pro-mimo-v2-6-pro-quota-ceiling (1.0944×, not selected by the comparator); mimo-tokenplan-standard-mimo-v2-6-pro-quota-ceiling (0.99×, not selected by the comparator); mimo-tokenplan-lite-mimo-v2-6-pro-quota-ceiling (0.984×, not selected by the comparator) | mimo-tokenplan-pro-mimo-v2-6-pro-quota-ceiling (1.0944×, value 48.30) |

### Measured-only Plan view

Admission: exact-route measurement candidates of grade controlled or concordant reports (no transfers, no diagnostics). Selection: the official selector (E111, E88, E85) rerun among the admitted candidates. Panel: rows with an admitted measured candidate; others listed as 'no measured route' (no API fallback).

| Configuration | Status | Route | Plan cost | Value | Rank |
|---|---|---|---:|---:|---:|
| Claude Opus 5.5 (max) | measured, target-workload unmatched | claude-pro-opus55-semianalysis | $158.77 | 62.33 | 1 |
| GPT-6.1 Sol (max) | measured, target-workload unmatched | chatgpt-pro500-gpt61sol-semianalysis | $114.47 | 60.32 | 2 |
| GPT-6 Astra (max) | measured, target-workload unmatched | chatgpt-pro200-gpt6astra-semianalysis | $406.29 | 56.66 | 3 |
| Claude Haiku 5.5 (max) | no measured route | — | — | — | — |
| Claude Sonnet 5.5 (max) | no measured route | — | — | — | — |
| DeepSeek V4.1 Flash 1017 (max) | no measured route | — | — | — | — |
| GPT-6 Luna (max) | no measured route | — | — | — | — |
| Gemini 4 Argon (high) | no measured route | — | — | — | — |
| MiMo-V2.6-Pro | no measured route | — | — | — | — |

#### Measured-evidence calibration (diagnostic)

References: each workload's measured-only rows with complete cost evidence are the references: c_L = cheapest / 2, c_H = dearest x 2 (diagnostic only; the official anchors are unchanged). Status: evaluated.

- Workload `9a0d376cc6080f3c`: measured anchors $57.24 to $812.57 from Claude Opus 5.5 (max), GPT-6 Astra (max), GPT-6.1 Sol (max); anchor ratio 14.2 against the official 1219.4. Official Plan anchors are set by GPT-6 Luna (max) on ChatGPT Pro 500 (owner-named transfer) at the low end and Gemini 4 Argon (high) on API-cost fallback at the high end.
- Workload `1453a9a0576b02ea`: measured-evidence calibration unavailable (fewer than two measured references); measured rows none. Official Plan anchors are set by Claude Haiku 5.5 (max) on Claude Pro (owner-named transfer) at the low end and Gemini 4 Argon (high) on API-cost fallback at the high end.

| Configuration | Value on official Plan anchors | Value on measured anchors | Rank change |
|---|---:|---:|---:|
| Claude Opus 5.5 (max) | 62.33 | 64.33 | 0 |
| GPT-6 Astra (max) | 56.66 | 53.12 | 0 |
| GPT-6.1 Sol (max) | 60.32 | 64.26 | 0 |

Pairwise reversals: none. Largest value change: 3.94 points.

## Interval outputs

**API basis, main workload: frontier.** Not evaluable: DeepSeek V4.1 Flash 1017 (max), MiMo-V2.6-Pro.

| Configuration | Possible frontier | Definite frontier | Definite counterexample | Possible frontier blocked by |
|---|---|---|---|---|
| Claude Sonnet 5.5 (max) | certified | certified | — | — |
| Claude Opus 5.5 (max) | certified | certified | — | — |
| GPT-6.1 Sol (max) | certified | certified | — | — |
| Gemini 4 Argon (high) | disproved | disproved | GPT-6.1 Sol (max) | GPT-6.1 Sol (max) |
| GPT-6 Astra (max) | certified | certified | — | — |
| Claude Haiku 5.5 (max) | certified | certified | — | — |
| GPT-6 Luna (max) | certified | certified | — | — |

**API basis, main workload: cheapest at or above quality 60.7** (lower-median displayed quality of the non-provisional cohort configurations at freeze (E192; headline bar)). Status certified; confirmed cheapest: GPT-6.1 Sol (max).

Configurations that can be confirmed to qualify: 4 (confirmation needs the full-composite lower bound, with missing leaves at 0, to clear the bar; O25). Cheaper same-family configurations on AA's chart that were not evaluated (not ranked: not plotted on or near the frontier; E201, O51): GPT-6.1 Sol (max): GPT-6.1 Sol (xhigh), GPT-6.1 Sol (high), GPT-6.1 Sol (medium), GPT-6.1 Sol (low).

Bar comparison: compares 5 configurations that can qualify. The bar is a displayed-quality level; qualification tests each row's full-composite bounds, so a row above the bar on displayed quality can still fail to qualify confirmed when leaves are missing (E198).

| Configuration | Displayed quality − bar | Confirmed qualifies | Possibly qualifies | Possibly cheapest |
|---|---:|---|---|---|
| Claude Sonnet 5.5 (max) | 4.1 | certified | certified | disproved |
| Claude Opus 5.5 (max) | 4.5 | certified | certified | disproved |
| GPT-6.1 Sol (max) | 0.3 | certified | certified | certified |
| Gemini 4 Argon (high) | 0.0 | disproved | certified | disproved |
| GPT-6 Astra (max) | 1.4 | certified | certified | disproved |
| Claude Haiku 5.5 (max) | -13.4 | disproved | disproved | disproved |
| GPT-6 Luna (max) | -17.6 | disproved | disproved | disproved |

**API basis, main workload: cheapest at or above quality 49.8** (lower-quartile displayed quality of the non-provisional cohort configurations at freeze (O34)). Status certified; confirmed cheapest: GPT-6.1 Sol (max).

Configurations that can be confirmed to qualify: 5 (confirmation needs the full-composite lower bound, with missing leaves at 0, to clear the bar; O25). Cheaper same-family configurations on AA's chart that were not evaluated (not ranked: not plotted on or near the frontier; E201, O51): GPT-6.1 Sol (max): GPT-6.1 Sol (xhigh), GPT-6.1 Sol (high), GPT-6.1 Sol (medium), GPT-6.1 Sol (low).

Bar comparison: compares 5 configurations that can qualify. The bar is a displayed-quality level; qualification tests each row's full-composite bounds, so a row above the bar on displayed quality can still fail to qualify confirmed when leaves are missing (E198).

| Configuration | Displayed quality − bar | Confirmed qualifies | Possibly qualifies | Possibly cheapest |
|---|---:|---|---|---|
| Claude Sonnet 5.5 (max) | 15.0 | certified | certified | disproved |
| Claude Opus 5.5 (max) | 15.5 | certified | certified | disproved |
| GPT-6.1 Sol (max) | 11.3 | certified | certified | certified |
| Gemini 4 Argon (high) | 11.0 | certified | certified | disproved |
| GPT-6 Astra (max) | 12.4 | certified | certified | disproved |
| Claude Haiku 5.5 (max) | -2.5 | disproved | disproved | disproved |
| GPT-6 Luna (max) | -6.7 | disproved | disproved | disproved |

**API basis, main workload: cheapest at or above quality 62.1** (upper-quartile displayed quality of the non-provisional cohort configurations at freeze (O34)). Status certified; confirmed cheapest: none.

Configurations that can be confirmed to qualify: 2 (confirmation needs the full-composite lower bound, with missing leaves at 0, to clear the bar; O25). Cheaper same-family configurations on AA's chart that were not evaluated (not ranked: not plotted on or near the frontier; E201, O51): Claude Sonnet 5.5 (max): Claude Sonnet 5.5 (xhigh with fallback), Claude Sonnet 5.5 (high with fallback), Claude Sonnet 5.5 (medium with fallback), Claude Sonnet 5.5 (low with fallback); GPT-6 Astra (max): GPT-6 Astra (xhigh), GPT-6 Astra (high), GPT-6 Astra (medium), GPT-6 Astra (low).

Bar comparison: compares 3 configurations that can qualify. The bar is a displayed-quality level; qualification tests each row's full-composite bounds, so a row above the bar on displayed quality can still fail to qualify confirmed when leaves are missing (E198).

| Configuration | Displayed quality − bar | Confirmed qualifies | Possibly qualifies | Possibly cheapest |
|---|---:|---|---|---|
| Claude Sonnet 5.5 (max) | 2.7 | certified | certified | certified |
| Claude Opus 5.5 (max) | 3.1 | certified | certified | disproved |
| GPT-6.1 Sol (max) | -1.1 | disproved | disproved | disproved |
| Gemini 4 Argon (high) | -1.4 | disproved | disproved | disproved |
| GPT-6 Astra (max) | 0.0 | disproved | certified | certified |
| Claude Haiku 5.5 (max) | -14.8 | disproved | disproved | disproved |
| GPT-6 Luna (max) | -19.0 | disproved | disproved | disproved |

**Plan basis, main workload:** not evaluated (no row has FullCost and an identified M_W (E61/E67)).

**API basis, subset workload (AA-Briefcase, GDPval-AA, GDP.pdf, AutomationBench-AA, Terminal-Bench 4.0 (AA Index run), SciCode, AA-LCR; orderings across workloads not identified): frontier.** Not evaluable: none.

| Configuration | Possible frontier | Definite frontier | Definite counterexample | Possible frontier blocked by |
|---|---|---|---|---|
| Claude Sonnet 5.5 (max) | certified | certified | — | — |
| DeepSeek V4.1 Flash 1017 (max) | certified | certified | — | — |
| Claude Opus 5.5 (max) | certified | certified | — | — |
| GPT-6.1 Sol (max) | certified | certified | — | — |
| Gemini 4 Argon (high) | disproved | disproved | GPT-6.1 Sol (max) | GPT-6.1 Sol (max) |
| GPT-6 Astra (max) | certified | certified | — | — |
| MiMo-V2.6-Pro | certified | certified | — | — |
| Claude Haiku 5.5 (max) | disproved | disproved | MiMo-V2.6-Pro | MiMo-V2.6-Pro |
| GPT-6 Luna (max) | certified | certified | — | — |

**API basis, subset workload (AA-Briefcase, GDPval-AA, GDP.pdf, AutomationBench-AA, Terminal-Bench 4.0 (AA Index run), SciCode, AA-LCR; orderings across workloads not identified): cheapest at or above quality 60.7** (lower-median displayed quality of the non-provisional cohort configurations at freeze (E192; headline bar)). Status certified; confirmed cheapest: GPT-6.1 Sol (max).

Configurations that can be confirmed to qualify: 4 (confirmation needs the full-composite lower bound, with missing leaves at 0, to clear the bar; O25). Cheaper same-family configurations on AA's chart that were not evaluated (not ranked: not plotted on or near the frontier; E201, O51): GPT-6.1 Sol (max): GPT-6.1 Sol (xhigh), GPT-6.1 Sol (high), GPT-6.1 Sol (medium), GPT-6.1 Sol (low).

Bar comparison: compares 5 configurations that can qualify. The bar is a displayed-quality level; qualification tests each row's full-composite bounds, so a row above the bar on displayed quality can still fail to qualify confirmed when leaves are missing (E198).

| Configuration | Displayed quality − bar | Confirmed qualifies | Possibly qualifies | Possibly cheapest |
|---|---:|---|---|---|
| Claude Sonnet 5.5 (max) | 4.1 | certified | certified | disproved |
| DeepSeek V4.1 Flash 1017 (max) | -6.8 | disproved | disproved | disproved |
| Claude Opus 5.5 (max) | 4.5 | certified | certified | disproved |
| GPT-6.1 Sol (max) | 0.3 | certified | certified | certified |
| Gemini 4 Argon (high) | 0.0 | disproved | certified | disproved |
| GPT-6 Astra (max) | 1.4 | certified | certified | disproved |
| MiMo-V2.6-Pro | -11.0 | disproved | disproved | disproved |
| Claude Haiku 5.5 (max) | -13.4 | disproved | disproved | disproved |
| GPT-6 Luna (max) | -17.6 | disproved | disproved | disproved |

**API basis, subset workload (AA-Briefcase, GDPval-AA, GDP.pdf, AutomationBench-AA, Terminal-Bench 4.0 (AA Index run), SciCode, AA-LCR; orderings across workloads not identified): cheapest at or above quality 49.8** (lower-quartile displayed quality of the non-provisional cohort configurations at freeze (O34)). Status certified; confirmed cheapest: none.

Configurations that can be confirmed to qualify: 6 (confirmation needs the full-composite lower bound, with missing leaves at 0, to clear the bar; O25). Cheaper same-family configurations on AA's chart that were not evaluated (not ranked: not plotted on or near the frontier; E201, O51): none.

Bar comparison: compares 7 configurations that can qualify. The bar is a displayed-quality level; qualification tests each row's full-composite bounds, so a row above the bar on displayed quality can still fail to qualify confirmed when leaves are missing (E198).

| Configuration | Displayed quality − bar | Confirmed qualifies | Possibly qualifies | Possibly cheapest |
|---|---:|---|---|---|
| Claude Sonnet 5.5 (max) | 15.0 | certified | certified | disproved |
| DeepSeek V4.1 Flash 1017 (max) | 4.1 | certified | certified | certified |
| Claude Opus 5.5 (max) | 15.5 | certified | certified | disproved |
| GPT-6.1 Sol (max) | 11.3 | certified | certified | disproved |
| Gemini 4 Argon (high) | 11.0 | certified | certified | disproved |
| GPT-6 Astra (max) | 12.4 | certified | certified | disproved |
| MiMo-V2.6-Pro | 0.0 | disproved | certified | certified |
| Claude Haiku 5.5 (max) | -2.5 | disproved | disproved | disproved |
| GPT-6 Luna (max) | -6.7 | disproved | disproved | disproved |

**API basis, subset workload (AA-Briefcase, GDPval-AA, GDP.pdf, AutomationBench-AA, Terminal-Bench 4.0 (AA Index run), SciCode, AA-LCR; orderings across workloads not identified): cheapest at or above quality 62.1** (upper-quartile displayed quality of the non-provisional cohort configurations at freeze (O34)). Status certified; confirmed cheapest: none.

Configurations that can be confirmed to qualify: 2 (confirmation needs the full-composite lower bound, with missing leaves at 0, to clear the bar; O25). Cheaper same-family configurations on AA's chart that were not evaluated (not ranked: not plotted on or near the frontier; E201, O51): Claude Sonnet 5.5 (max): Claude Sonnet 5.5 (xhigh with fallback), Claude Sonnet 5.5 (high with fallback), Claude Sonnet 5.5 (medium with fallback), Claude Sonnet 5.5 (low with fallback); GPT-6 Astra (max): GPT-6 Astra (xhigh), GPT-6 Astra (high), GPT-6 Astra (medium), GPT-6 Astra (low).

Bar comparison: compares 3 configurations that can qualify. The bar is a displayed-quality level; qualification tests each row's full-composite bounds, so a row above the bar on displayed quality can still fail to qualify confirmed when leaves are missing (E198).

| Configuration | Displayed quality − bar | Confirmed qualifies | Possibly qualifies | Possibly cheapest |
|---|---:|---|---|---|
| Claude Sonnet 5.5 (max) | 2.7 | certified | certified | certified |
| DeepSeek V4.1 Flash 1017 (max) | -8.2 | disproved | disproved | disproved |
| Claude Opus 5.5 (max) | 3.1 | certified | certified | disproved |
| GPT-6.1 Sol (max) | -1.1 | disproved | disproved | disproved |
| Gemini 4 Argon (high) | -1.4 | disproved | disproved | disproved |
| GPT-6 Astra (max) | 0.0 | disproved | certified | certified |
| MiMo-V2.6-Pro | -12.4 | disproved | disproved | disproved |
| Claude Haiku 5.5 (max) | -14.8 | disproved | disproved | disproved |
| GPT-6 Luna (max) | -19.0 | disproved | disproved | disproved |

**Plan basis, subset workload (AA-Briefcase, GDPval-AA, GDP.pdf, AutomationBench-AA, Terminal-Bench 4.0 (AA Index run), SciCode, AA-LCR; orderings across workloads not identified):** not evaluated (unevaluable: no Plan multiple is identified for a subset workload (E149, E190)).

## Scenario shares

Frequencies over 10,000 scenarios per run (seed 20261023); streams are defined in [methodology.md](methodology.md#uncertainty-outputs). S1T adds benchmark sampling noise under an independent-task approximation (O39); the other streams exclude it, and every stream excludes correlated-task, harness and attempt effects (E155).

### API basis: rank 1

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M | S1T |
|---|---:|---:|---:|---:|---:|---:|
| Claude Haiku 5.5 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Sonnet 5.5 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Luna (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.9% |
| GPT-6.1 Sol (max) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 99.1% |
| Gemini 4 Argon (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.1% |

### API basis: rank 3 or better

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M | S1T |
|---|---:|---:|---:|---:|---:|---:|
| Claude Haiku 5.5 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (max) | 0.0% | 0.0% | 1.8% | 0.0% | 0.0% | 21.2% |
| Claude Sonnet 5.5 (max) | 0.0% | 0.0% | 3.4% | 0.0% | 0.0% | 17.0% |
| GPT-6 Astra (max) | 0.0% | 0.0% | 0.3% | 0.0% | 0.0% | 13.0% |
| GPT-6 Luna (max) | 100.0% | 100.0% | 96.8% | 100.0% | 100.0% | 93.4% |
| GPT-6.1 Sol (max) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% |
| Gemini 4 Argon (high) | 100.0% | 100.0% | 97.8% | 100.0% | 100.0% | 55.5% |

### API basis: on the frontier

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M | S1T |
|---|---:|---:|---:|---:|---:|---:|
| Claude Haiku 5.5 (max) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 98.3% |
| Claude Opus 5.5 (max) | 100.0% | 100.0% | 80.1% | 100.0% | 100.0% | 57.8% |
| Claude Sonnet 5.5 (max) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 87.6% |
| GPT-6 Astra (max) | 100.0% | 100.0% | 99.7% | 100.0% | 100.0% | 58.4% |
| GPT-6 Luna (max) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% |
| GPT-6.1 Sol (max) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% |
| Gemini 4 Argon (high) | 0.0% | 0.0% | 25.0% | 0.0% | 0.0% | 44.0% |

### API basis: value-score dispersion (SD; covariance term)

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M | S1T |
|---|---:|---:|---:|---:|---:|---:|
| Claude Haiku 5.5 (max) | 0.00 (+0.00) | 0.00 (+0.00) | 1.36 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.09 (+0.00) |
| Claude Opus 5.5 (max) | 0.00 (+0.00) | 0.00 (+0.00) | 1.15 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.09 (+0.00) |
| Claude Sonnet 5.5 (max) | 0.00 (+0.00) | 0.00 (+0.00) | 1.14 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.07 (+0.00) |
| GPT-6 Astra (max) | 0.00 (+0.00) | 0.00 (+0.00) | 1.14 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.08 (+0.00) |
| GPT-6 Luna (max) | 0.00 (+0.00) | 0.00 (+0.00) | 1.51 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.00 (+0.00) |
| GPT-6.1 Sol (max) | 0.00 (+0.00) | 0.00 (+0.00) | 1.05 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.11 (+0.00) |
| Gemini 4 Argon (high) | 0.00 (+0.00) | 0.00 (+0.00) | 1.17 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.11 (+0.00) |

Plan streams S1, S2, S1 endpoint-heavy, S1M and S1T run with owner-named transfers off (E167): Claude Haiku 5.5 (max) on Claude Max 20x, Claude Haiku 5.5 (max) on Claude Max 5x, Claude Haiku 5.5 (max) on Claude Pro, Claude Sonnet 5.5 (max) on Claude Max 20x, Claude Sonnet 5.5 (max) on Claude Max 5x, Claude Sonnet 5.5 (max) on Claude Pro, GPT-6 Luna (max) on ChatGPT Plus, GPT-6 Luna (max) on ChatGPT Pro 100, GPT-6 Luna (max) on ChatGPT Pro 200, GPT-6 Luna (max) on ChatGPT Pro 500 depend on a transfer and are unevaluable there (—), never reselected or replaced by API cost.

### Plan basis: rank 1

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M | S1T |
|---|---:|---:|---:|---:|---:|---:|
| Claude Haiku 5.5 (max) on Claude Max 20x | 0.0% | — | — | — | — | — |
| Claude Haiku 5.5 (max) on Claude Max 5x | 0.0% | — | — | — | — | — |
| Claude Haiku 5.5 (max) on Claude Pro | 0.0% | — | — | — | — | — |
| Claude Opus 5.5 (max) on Claude Max 20x | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (max) on Claude Max 5x | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (max) on Claude Pro | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 90.1% |
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
| GPT-6.1 Sol (max) on ChatGPT Pro 500 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 9.9% |
| Gemini 4 Argon (high) on API-cost fallback | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |

### Plan basis: rank 3 or better

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M | S1T |
|---|---:|---:|---:|---:|---:|---:|
| Claude Haiku 5.5 (max) on Claude Max 20x | 0.0% | — | — | — | — | — |
| Claude Haiku 5.5 (max) on Claude Max 5x | 0.0% | — | — | — | — | — |
| Claude Haiku 5.5 (max) on Claude Pro | 0.0% | — | — | — | — | — |
| Claude Opus 5.5 (max) on Claude Max 20x | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 90.8% |
| Claude Opus 5.5 (max) on Claude Max 5x | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 88.9% |
| Claude Opus 5.5 (max) on Claude Pro | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 90.9% |
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
| GPT-6.1 Sol (max) on ChatGPT Plus | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 9.2% |
| GPT-6.1 Sol (max) on ChatGPT Pro 100 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 9.2% |
| GPT-6.1 Sol (max) on ChatGPT Pro 200 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (max) on ChatGPT Pro 500 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 11.1% |
| Gemini 4 Argon (high) on API-cost fallback | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |

### Plan basis: on the frontier

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M | S1T |
|---|---:|---:|---:|---:|---:|---:|
| Claude Haiku 5.5 (max) on Claude Max 20x | 0.0% | — | — | — | — | — |
| Claude Haiku 5.5 (max) on Claude Max 5x | 0.0% | — | — | — | — | — |
| Claude Haiku 5.5 (max) on Claude Pro | 100.0% | — | — | — | — | — |
| Claude Opus 5.5 (max) on Claude Max 20x | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (max) on Claude Max 5x | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (max) on Claude Pro | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 97.9% |
| Claude Sonnet 5.5 (max) on Claude Max 20x | 0.0% | — | — | — | — | — |
| Claude Sonnet 5.5 (max) on Claude Max 5x | 0.0% | — | — | — | — | — |
| Claude Sonnet 5.5 (max) on Claude Pro | 100.0% | — | — | — | — | — |
| GPT-6 Astra (max) on ChatGPT Plus | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (max) on ChatGPT Pro 100 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (max) on ChatGPT Pro 200 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 6.0% |
| GPT-6 Astra (max) on ChatGPT Pro 500 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Luna (max) on ChatGPT Plus | 0.0% | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 100 | 0.0% | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 200 | 0.0% | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 500 | 100.0% | — | — | — | — | — |
| GPT-6.1 Sol (max) on ChatGPT Plus | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (max) on ChatGPT Pro 100 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (max) on ChatGPT Pro 200 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (max) on ChatGPT Pro 500 | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% |
| Gemini 4 Argon (high) on API-cost fallback | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 1.2% |

### Plan basis: value-score dispersion (SD; covariance term)

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M | S1T |
|---|---:|---:|---:|---:|---:|---:|
| Claude Haiku 5.5 (max) on Claude Max 20x | 0.00 (+0.00) | — | — | — | — | — |
| Claude Haiku 5.5 (max) on Claude Max 5x | 0.00 (+0.00) | — | — | — | — | — |
| Claude Haiku 5.5 (max) on Claude Pro | 0.00 (+0.00) | — | — | — | — | — |
| Claude Opus 5.5 (max) on Claude Max 20x | 0.00 (+0.00) | 0.00 (+0.00) | 1.15 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.08 (+0.00) |
| Claude Opus 5.5 (max) on Claude Max 5x | 0.00 (+0.00) | 0.00 (+0.00) | 1.15 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.08 (+0.00) |
| Claude Opus 5.5 (max) on Claude Pro | 0.00 (+0.00) | 0.00 (+0.00) | 1.15 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.08 (+0.00) |
| Claude Sonnet 5.5 (max) on Claude Max 20x | 0.00 (+0.00) | — | — | — | — | — |
| Claude Sonnet 5.5 (max) on Claude Max 5x | 0.00 (+0.00) | — | — | — | — | — |
| Claude Sonnet 5.5 (max) on Claude Pro | 0.00 (+0.00) | — | — | — | — | — |
| GPT-6 Astra (max) on ChatGPT Plus | 0.00 (+0.00) | 0.00 (+0.00) | 1.14 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.09 (+0.00) |
| GPT-6 Astra (max) on ChatGPT Pro 100 | 0.00 (+0.00) | 0.00 (+0.00) | 1.14 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.09 (+0.00) |
| GPT-6 Astra (max) on ChatGPT Pro 200 | 0.00 (+0.00) | 0.00 (+0.00) | 1.14 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.09 (+0.00) |
| GPT-6 Astra (max) on ChatGPT Pro 500 | 0.00 (+0.00) | 0.00 (+0.00) | 1.14 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.09 (+0.00) |
| GPT-6 Luna (max) on ChatGPT Plus | 0.00 (+0.00) | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 100 | 0.00 (+0.00) | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 200 | 0.00 (+0.00) | — | — | — | — | — |
| GPT-6 Luna (max) on ChatGPT Pro 500 | 0.00 (+0.00) | — | — | — | — | — |
| GPT-6.1 Sol (max) on ChatGPT Plus | 0.00 (+0.00) | 0.00 (+0.00) | 1.06 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.10 (+0.00) |
| GPT-6.1 Sol (max) on ChatGPT Pro 100 | 0.00 (+0.00) | 0.00 (+0.00) | 1.06 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.10 (+0.00) |
| GPT-6.1 Sol (max) on ChatGPT Pro 200 | 0.00 (+0.00) | 0.00 (+0.00) | 1.06 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.10 (+0.00) |
| GPT-6.1 Sol (max) on ChatGPT Pro 500 | 0.00 (+0.00) | 0.00 (+0.00) | 1.06 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.10 (+0.00) |
| Gemini 4 Argon (high) on API-cost fallback | 0.00 (+0.00) | 0.00 (+0.00) | 1.18 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.11 (+0.00) |

### Named S2 specification branches

- **Bug Hunt harness band (E19)** (S2): unevaluable; the captured tbench.ai leaderboard lists no configuration under two or more agents, so no cross-agent spread exists
- **cache-hit variation (E34)** (S2): unevaluable; AA's published cost embeds its cache-pricing protocol; varying the cache-hit rate needs each basket component's cache-read and uncached-input demand, which AA publishes only for the whole Index (E157)
- **first-party list versus cross-provider median price rule (E122)** (S2): unevaluable; AA publishes one price per configuration under its own rule; the alternative rule's prices are not captured

### Cheapest-above-the-bar labels (API basis)

The 90% rule's error bound holds per published event (candidate and kernel assignment); it is not corrected across the listed candidates (E198). Each kernel assignment code gives the kernel used for the candidate and the competitors, in that order (U uniform, H endpoint-heavy; a quality-level bar has no reference rows, so it takes no letter); the label needs every assignment met.

| Bar | Candidate | Reading | Frequency range | Kernel assignments | Label |
|---|---|---|---|---|---|
| quality 60.7 | GPT-6.1 Sol (max) | supported under all registered role-group kernel checks | 100.0% to 100.0% | UU met, UH met, HU met, HH met | yes |
| quality 49.8 | GPT-6.1 Sol (max) | supported under all registered role-group kernel checks | 100.0% to 100.0% | UU met, UH met, HU met, HH met | yes |
| quality 62.1 | Claude Sonnet 5.5 (max) | not scenario-supported | 49.7% to 51.0% | UU not met, UH not met, HU not met, HH not met | no |
| quality 62.1 | GPT-6 Astra (max) | not scenario-supported | 49.5% to 50.4% | UU not met, UH not met, HU not met, HH not met | no |

## Diagnostics

- **Terminal-Bench cross-source agreement (AA's mini-SWE-agent run against tbench.ai):** defined; 0 rows take the leaf from tbench.ai (gap fill).
- **Rank separability (O39, independent-task approximation):** median separation 3.01 value points (API) and 3.01 (Plan); separable adjacent ranks: API 1 of 8, Plan 2 of 11. Assumptions: tasks are independent and each leaf's score is a mean over its published task count (plug-in binomial with the proportion (k + 1/2) / (n + 1), I28); attempts averaged within a task and tasks shared across models are ignored, so the noise is approximate; GDPval-AA: AA's displayed rating interval (-26/+26 Elo for Claude Opus 5.5) read as a 95% normal interval, SD 13.3 Elo for every row; AA-Omniscience: each of 6,000 questions scores +1, 0 or -1, with the shares from AA's accuracy and hallucination rate; Vals boards (Vibe Code Bench v1.1, Code Migration v1.1): Vals' published standard error per record, read as the leaf's SD; AI Coding Daily: judged points over its six graded projects read as a binomial share of 60 points (an assumption; the board publishes no error).
- **FrontierCode against Cognition:** FrontierCode cross-source agreement (AA against Cognition, same name and effort; E234): Kendall tau 0.87 (interval 0.33 to 1.00) on 6 rows. Cognition minus AA: mean +1.7 points, largest 6.3.
- **Gap-fill removal (E234, diagnostic):** no ranked row has a leaf from another party or the provider.
- **Bar results without the gap fills (E234, sensitivity; labels unchanged):** cheapest displayed row as published, with fills removed, and with third-party fills lowered by the mean offset 1.7 points — API quality 60.7: GPT-6.1 Sol (max) in all three; API quality 49.8: GPT-6.1 Sol (max) in all three; API quality 62.1: GPT-6 Astra (max) in all three; Plan quality 60.7: GPT-6.1 Sol (max) in all three; Plan quality 49.8: GPT-6.1 Sol (max) in all three; Plan quality 62.1: Claude Sonnet 5.5 (max) in all three.
- **Quality agreement:** quality agreement (matched-panel sensitivity): Kendall tau 0.89 (interval 0.61 to 1.00) on 9 rows.
- **Quality-substitution value agreement (API):** quality-substitution value agreement, api basis (matched-panel sensitivity): Kendall tau 0.44 (interval -0.27 to 1.00) on 9 rows.
- **Quality-substitution value agreement (Plan):** quality-substitution value agreement, plan basis (matched-panel sensitivity): Kendall tau 0.78 (interval 0.44 to 1.00) on 9 rows.
- **Disjoint-evidence agreement:** disjoint-evidence agreement (restricted evidence comparison, not an eligible ranking): Kendall tau 0.78 (interval 0.42 to 1.00) on 9 rows.
- **Quality source shares:** AA-run 72%, independent 28%.
- **Non-discriminating leaves:** lcr.
- **Group drift:** estimated; flagged: none.
- **Omniscience abstention sensitivity** (z_pen = max(0, I)): 4 rows move; largest move 1 (Claude Sonnet 5.5 (max), Gemini 4 Argon (high), GPT-6 Astra (max), GPT-6 Luna (max)).
- **GDPval-AA logistic sensitivity** (z = 100 / (1 + 10^((1600 - E) / 400)) against AA's pinned anchor; every other input fixed): API 4 rows move; largest move 2 (Claude Opus 5.5 (max), Gemini 4 Argon (high)); Plan 2 rows move; largest move 1 (DeepSeek V4.1 Flash 1017 (max), MiMo-V2.6-Pro).
- **Anchor stability:** trimmed anchors (P10 / 2 and P90 x 2 (diagnostic only)) give $315.22 to $18,198.91; 4 rows move; largest move 3 (Claude Haiku 5.5 (max)).

- **Basket readiness (E22):** priced leaves cover 59% of nominal quality weight (AutomationBench-AA, FrontierCode 1.1, GDPval-AA v2.1, AA-LCR v1.1, SciCode, Terminal-Bench 4.0 (AA run)); pending components: ITBench-AA.
- **SWE cost companion (O14, diagnostic):** 7 rows evaluated; flagged far from the median ratio: Claude Haiku 5.5 (max).
- **Matched-cost diagnostic (E55):** evaluated at 54% priced quality weight; basket/matched cost-order reversals with separated intervals: 0; rank-gap warnings: 0.
- **Frontier-families anchors (E187, diagnostic):** anchors rebuilt from the 7 frontier and near-frontier references move API no rank changes (value points per cost doubling 3.04 vs 3.04 frozen); Plan no rank changes (value points per cost doubling 2.44 vs 2.44 frozen).
- **Frontier-families bar (E199, sensitivity; the frozen bar stays primary):** quality 60.7 over 9 configurations; cheapest at or above it on the API main workload: GPT-6.1 Sol (max) (confirmed) (compares 5 configurations that can qualify).
- **One row per family (E205, diagnostic; the frozen ladder and anchors stay primary):** with each family's primary configuration only (7 rows in the one-row-per-family bar population), the ladder (headline, lower quartile, upper quartile) would be 60.7 / 49.8 / 61.1 against 60.7 / 49.8 / 62.1 frozen; anchors rebuilt from its 5 references move API no rank changes (value points per cost doubling 3.04 vs 3.04 frozen); Plan no rank changes (value points per cost doubling 2.44 vs 2.44 frozen).
- **Ladder over scored rows (I28, sensitivity; the frozen ladder stays primary):** the bar population keeps full-benchmark rows that have no cost; today every such row has a cost, so the ladder is unchanged.
- **Bar currency (E207, informational):** rows reaching each frozen bar: quality 60.7: 5 of 9; quality 49.8: 7 of 9; quality 62.1: 3 of 9; the current population would freeze 60.7 / 49.8 / 62.1; lifetime until the next anchor re-freeze or methodology version, whichever comes first; no staleness flag.
- **Token mix (E208):** 1 selected routes: mix not reported: the measurement publishes no token-category shares; 6 selected routes: mix unidentified: the basket's token-category shares are set-identified only (E124), so the L1 test (above 0.30 flags mix-unmatched) is not computed.
- **Observed-range sensitivity (E219, not evidence; no label changes):** with each missing leaf inside the cohort's observed range for that leaf, quality 60.7: 5 can qualify, 4 confirmed; GPT-6.1 Sol (max) confirmed cheapest; quality 49.8: 5 can qualify, 5 confirmed; GPT-6.1 Sol (max) confirmed cheapest; quality 62.1: 3 can qualify, 2 confirmed; possibly cheapest Claude Sonnet 5.5 (max), GPT-6 Astra (max).
- **What would settle the headline bar (E221, not a claim):** rows that can but need not reach quality 60.7, with the mean score their missing leaves would need: Gemini 4 Argon (high) (no missing leaf; reporting precision only).
- **Common leaf set (E226, diagnostic; scores unchanged):** without the leaves fewer than 90% of cohort rows have (none), API no rank changes; Plan no rank changes; rows reaching each bar: quality 60.7: 5 → 5; quality 49.8: 7 → 7; quality 62.1: 3 → 3; rows whose displayed quality differs from common-leaf quality by more than one cost doubling's worth: none.
- **Harness by leaf (E227):** Terminal-Bench: mini-SWE-agent 9; Bug Hunt: Codex CLI 10, Claude Code 7, Antigravity CLI 1, Claude Code / Anthropic-compatible shim 1, DeepSeek Harness / DeepSeek API 1.

### Leave-one-component-out cost family (E172)

Each admitted basket unit removed in turn, scored on anchors rebuilt by the freeze rule (rank changes against the primary ranking; quality held fixed).

| Removed component | API rank changes | Plan rank changes | API value points per cost doubling |
|---|---|---|---:|
| Coding Agent Index | 3 rows move; largest move 3 (Claude Haiku 5.5 (max)) | 2 rows move; largest move 1 (Claude Opus 5.5 (max), Claude Sonnet 5.5 (max)) | 3.03 |
| AA-Briefcase | no rank changes | 2 rows move; largest move 1 (Claude Haiku 5.5 (max), GPT-6 Astra (max)) | 3.10 |
| GDPval-AA | no rank changes | 2 rows move; largest move 1 (Claude Haiku 5.5 (max), GPT-6 Astra (max)) | 3.08 |
| GDP.pdf | no rank changes | no rank changes | 3.04 |
| AutomationBench-AA | 3 rows move; largest move 2 (GPT-6 Astra (max)) | 2 rows move; largest move 1 (Claude Haiku 5.5 (max), GPT-6 Astra (max)) | 2.99 |
| Terminal-Bench 4.0 (AA Index run) | no rank changes | 2 rows move; largest move 1 (Claude Haiku 5.5 (max), GPT-6 Astra (max)) | 3.02 |
| SciCode | no rank changes | no rank changes | 3.05 |
| AA-LCR | no rank changes | no rank changes | 3.04 |

### Subset rows: paired bridge and missing spend (E10, E173)

- **DeepSeek V4.1 Flash 1017 (max), MiMo-V2.6-Pro** (subset without Coding Agent Index): Coding Agent Index is 37% of the full basket (median; 35% to 80% over 7 rows). Scored on its own subset anchors, the direction of its subset effect is not known. Paired bridge on the 7 full rows: API: the full rows' values change by 0.01 points (median; -0.07 to 5.12), 3 rows move; largest move 3 (Claude Haiku 5.5 (max)); Plan: the full rows' values change by -1.54 points (median; -2.45 to 1.40), 2 rows move; largest move 1 (Claude Opus 5.5 (max), Claude Sonnet 5.5 (max)).

### Deletion sensitivity

| Branch | Retained nominal weight | Status | API rank changes | Plan rank changes |
|---|---:|---|---|---|
| leave-out:frontierCode | 82% | evaluated | 7 rows move; largest move 2 (Claude Opus 5.5 (max), Claude Sonnet 5.5 (max), GPT-6 Luna (max)) | 6 rows move; largest move 2 (Gemini 4 Argon (high), MiMo-V2.6-Pro) |
| leave-out:terminalBench | 86% | evaluated | 5 rows move; largest move 2 (GPT-6.1 Sol (max)) | 4 rows move; largest move 1 (DeepSeek V4.1 Flash 1017 (max), GPT-6 Astra (max), GPT-6 Luna (max), MiMo-V2.6-Pro) |
| leave-out:bugHunt | 90% | evaluated | 4 rows move; largest move 1 (Claude Sonnet 5.5 (max), GPT-6 Astra (max), GPT-6.1 Sol (max), MiMo-V2.6-Pro) | 2 rows move; largest move 1 (DeepSeek V4.1 Flash 1017 (max), Gemini 4 Argon (high)) |
| leave-out:vibeCode | 95% | evaluated | no rank changes | 2 rows move; largest move 1 (Claude Haiku 5.5 (max), GPT-6 Astra (max)) |
| leave-out:codeMigration | 94% | evaluated | 4 rows move; largest move 1 (Claude Sonnet 5.5 (max), GPT-6 Astra (max), GPT-6.1 Sol (max), MiMo-V2.6-Pro) | no rank changes |
| leave-out:livebenchAgentic | 95% | evaluated | 2 rows move; largest move 1 (Claude Opus 5.5 (max), Claude Sonnet 5.5 (max)) | 2 rows move; largest move 1 (Claude Opus 5.5 (max), Claude Sonnet 5.5 (max)) |
| leave-out:livebenchCoding | 98% | evaluated | no rank changes | 2 rows move; largest move 1 (Claude Haiku 5.5 (max), GPT-6 Astra (max)) |
| leave-out:gdpval | 90% | evaluated | 3 rows move; largest move 2 (GPT-6 Astra (max)) | 5 rows move; largest move 2 (Gemini 4 Argon (high)) |
| leave-out:automationBench | 90% | evaluated | 2 rows move; largest move 1 (Claude Opus 5.5 (max), Gemini 4 Argon (high)) | no rank changes |
| leave-out:omniscience | 90% | evaluated | 2 rows move; largest move 1 (Claude Opus 5.5 (max), Claude Sonnet 5.5 (max)) | 4 rows move; largest move 1 (Claude Opus 5.5 (max), Claude Sonnet 5.5 (max), DeepSeek V4.1 Flash 1017 (max), MiMo-V2.6-Pro) |
| leave-out:lcr | 95% | evaluated | no rank changes | 4 rows move; largest move 2 (Gemini 4 Argon (high), MiMo-V2.6-Pro) |
| leave-out:hle | 98% | evaluated | no rank changes | no rank changes |
| leave-out:scicode | 98% | evaluated | no rank changes | no rank changes |
| leave-out:critpt | 98% | evaluated | no rank changes | no rank changes |
| leave-source-out:Artificial Analysis | 28% | not identifiable under the coverage rule | — | — |
| leave-source-out:Vals AI | 89% | evaluated | 2 rows move; largest move 1 (Claude Sonnet 5.5 (max), GPT-6 Astra (max)) | no rank changes |
| leave-source-out:LiveBench | 93% | evaluated | 2 rows move; largest move 1 (Claude Opus 5.5 (max), Claude Sonnet 5.5 (max)) | 2 rows move; largest move 1 (Claude Opus 5.5 (max), Claude Sonnet 5.5 (max)) |
| basket-scope | 87% | evaluated | 4 rows move; largest move 1 (Claude Opus 5.5 (max), Claude Sonnet 5.5 (max), DeepSeek V4.1 Flash 1017 (max), MiMo-V2.6-Pro) | 4 rows move; largest move 1 (Claude Opus 5.5 (max), Claude Sonnet 5.5 (max), DeepSeek V4.1 Flash 1017 (max), MiMo-V2.6-Pro) |

### Cost-component removal (Terminal-Bench 4.0 (AA Index run): evaluated)

| Basis | Run | Rank changes |
|---|---|---|
| api | cost-component removal, original anchors | no rank changes |
| api | alternative workload, recalibrated anchors | no rank changes |
| plan | cost-component removal, original anchors; fixed-multiple arithmetic stress (not identified Plan economics for the altered workload) | 2 rows move; largest move 1 (Claude Haiku 5.5 (max), GPT-6 Astra (max)) |
| plan | alternative workload, recalibrated anchors; fixed-multiple arithmetic stress (not identified Plan economics for the altered workload) | 2 rows move; largest move 1 (Claude Haiku 5.5 (max), GPT-6 Astra (max)) |

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
| score swing gate (E177) | vacuous | first v3 release: no previous v3 release to compare |
| anchor migration (E184) | vacuous | no main-workload migration deferred |
| configuration map coverage | passed | every cohort row has a pinned identity |
| quality clipping audit (E110) | passed | saturation disclosed; domain violations block the build |
| full benchmark set (O36, O38) | fired | listed, not ranked: gpt-6.1-sol-high, claude-opus-5-5-high, claude-opus-5-5-medium, gpt-6.1-sol-medium, gpt-6-astra-high, claude-haiku-5-5-high, gpt-6-luna-xhigh, claude-haiku-5-5-medium, gpt-6-luna-high, gpt-6-luna-medium, gpt-5.6-luna-low, claude-haiku-5-5, claude-haiku-5-5-low, claude-opus-5-5-xhigh, claude-sonnet-5-5-xhigh, gpt-6-astra-xhigh, gpt-6-luna-low, gpt-6.1-sol-xhigh, mimo-v2-6-flash, minimax-m3-1-flash |
| missing-leaf rules (O8 provisional, E198b, E201b, E219, E221, E226) | vacuous | no ranked row has a missing leaf (O36) |
| S1M interval stream (E145) | vacuous | dormant: no ranked leaf carries a published confidence interval since O37, so S1M equals S1 (E236) |
| provider-claim label denial (E233) | vacuous | no row has a provider-claimed leaf |
| scenario outputs current (E72) | passed | scenario input hash matches the scored inputs |
