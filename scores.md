# ValueRank v3.0.0 Scores

**Updated:** October 19, 2026 · methodology 3.0.0 · SDLC basket v1 · anchor version `v3-2026-10-21`

Value = 25% × cost score + 75% × quality. Costs are USD per basket run; the cost score is log-scaled against the frozen anchors of the row's workload (see [methodology.md](methodology.md)).

## Ranking

| Configuration | Plan rank | Plan value | Plan cost score | API rank | API value | API cost score | Quality | Quality coverage | Workload |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| [GPT-6.1 Sol (xhigh)](https://valuerank.alolabs.dev/models/gpt-6-1-sol-xhigh/) | 1 | 60.93 | 51.61 | 1 | 60.62 | 50.34 | 64.04 | 80% | main |
| [GPT-6.1 Sol (high)](https://valuerank.alolabs.dev/models/gpt-6-1-sol-high/) | 2 | 59.83 | 53.27 | 3 | 59.75 | 52.97 | 62.01 | 80% | main |
| [GPT-6.1 Sol (medium)](https://valuerank.alolabs.dev/models/gpt-6-1-sol-medium/) | 3 | 59.68 | 56.03 | 2 | 60.00 | 57.33 | 60.89 | 80% | main |
| [Claude Sonnet 5.5 (max)](https://valuerank.alolabs.dev/models/claude-sonnet-5-5/) | 4 | 59.32 | 44.32 | 19 | 51.23 | 11.96 | 64.32 | 100% | main |
| [Claude Opus 5.5 (max)](https://valuerank.alolabs.dev/models/claude-opus-5-5/) | 5 | 59.07 | 43.69 | 22 | 50.89 | 10.96 | 64.19 | 100% | main |
| [Claude Sonnet 5.5 (xhigh)](https://valuerank.alolabs.dev/models/claude-sonnet-5-5-xhigh/) | 6 | 58.84 | 56.28 | 15 | 52.49 | 30.86 | 59.69 | 90% | main |
| [Claude Sonnet 5.5 (high)](https://valuerank.alolabs.dev/models/claude-sonnet-5-5-high/) | 7 | 58.55 | 64.48 | 11 | 53.39 | 43.84 | 56.57 | 90% | main |
| [GPT-6.1 Sol (max)](https://valuerank.alolabs.dev/models/gpt-6-1-sol/) | 8 | 57.83 | 47.34 | 6 | 56.89 | 43.59 | 61.33 | 100% | main |
| [GPT-6.1 Sol (low)](https://valuerank.alolabs.dev/models/gpt-6-1-sol-low/) | 9 | 57.00 | 59.51 | 5 | 57.83 | 62.84 | 56.16 | 80% | main |
| [Claude Sonnet 5.5 (medium)](https://valuerank.alolabs.dev/models/claude-sonnet-5-5-medium/) | 10 | 55.83 | 69.82 | 18 | 51.45 | 52.28 | 51.17 | 90% | main |
| [Claude Opus 5 (max)](https://valuerank.alolabs.dev/models/claude-opus-5/) | 11 | 54.61 | 45.03 | 33 | 46.62 | 13.08 | 57.81 | 80% | main |
| [GPT-6 Sol (max)](https://valuerank.alolabs.dev/models/gpt-6-sol/) | 12 | 54.40 | 42.79 | 13 | 52.80 | 36.39 | 58.28 | 90% | main |
| [Claude Haiku 5.5 (xhigh)](https://valuerank.alolabs.dev/models/claude-haiku-5-5/) | 13 | 53.77 | 79.00 | 24 | 50.72 | 66.80 | 45.36 | 90% | main |
| [Claude Sonnet 5.5 (low)](https://valuerank.alolabs.dev/models/claude-sonnet-5-5-low/) | 14 | 53.64 | 72.17 | 28 | 49.60 | 56.00 | 47.47 | 90% | main |
| [GPT-5.6 Sol (max)](https://valuerank.alolabs.dev/models/gpt-5-6-sol/) | 15 | 53.59 | 35.27 | 21 | 50.90 | 24.51 | 59.70 | 90% | main |
| [GPT-6 Luna (max)](https://valuerank.alolabs.dev/models/gpt-6-luna/) | 16 | 53.28 | 69.89 | 8 | 55.62 | 79.25 | 47.74 | 100% | main |
| [Claude Haiku 5.5 (high)](https://valuerank.alolabs.dev/models/claude-haiku-5-5-high/) | 17 | 53.14 | 83.77 | 23 | 50.78 | 74.33 | 42.93 | 90% | main |
| [GPT-6 Astra (max)](https://valuerank.alolabs.dev/models/gpt-6-astra/) | 18 | 52.85 | 28.77 | 25 | 50.35 | 18.74 | 60.88 | 100% | main |
| [Claude Haiku 5.5 (medium)](https://valuerank.alolabs.dev/models/claude-haiku-5-5-medium/) | 19 | 52.80 | 88.36 | 20 | 51.11 | 81.60 | 40.94 | 90% | main |
| [GPT-5.6 Luna (max)](https://valuerank.alolabs.dev/models/gpt-5-6-luna/) | 20 | 52.79 | 61.13 | 10 | 53.86 | 65.39 | 50.01 | 90% | main |
| [Gemini 4 Argon (high)](https://valuerank.alolabs.dev/models/gemini-4-argon/) | 21 | 52.24 | 13.06 | 7 | 55.71 | 26.97 | 65.30 | 90% | main |
| [Claude Fable 5.1 (max)](https://valuerank.alolabs.dev/models/claude-fable-5-1/) | 22 | 51.91 | 26.89 | 30 | 47.34 | 8.62 | 60.25 | 100% | main |
| [MiMo-V2.6-Flash](https://valuerank.alolabs.dev/models/mimo-v2-6-flash/) | 23 | 51.61 | 51.20 | 4 | 58.41 | 78.43 | 51.74 | 50% | subset |
| [Claude Haiku 5.5 (low)](https://valuerank.alolabs.dev/models/claude-haiku-5-5-low/) | 24 | 50.93 | 93.07 | 27 | 49.92 | 89.04 | 36.88 | 90% | main |
| [Claude Haiku 5.5 (max)](https://valuerank.alolabs.dev/models/claude-haiku-5-5-max/) | 25 | 50.74 | 66.97 | 35 | 45.94 | 47.77 | 45.33 | 90% | main |
| [Muse Wonder (max)](https://valuerank.alolabs.dev/models/muse-wonder/) | 26 | 50.11 | 7.18 | 14 | 52.73 | 17.67 | 64.42 | 80% | main |
| [MiMo-V2.6-Pro](https://valuerank.alolabs.dev/models/mimo-v2-6-pro/) | 27 | 48.43 | 43.46 | 9 | 54.17 | 66.40 | 50.09 | 60% | subset |
| [Muse Spark 1.3 (max)](https://valuerank.alolabs.dev/models/muse-spark-1-3/) | 28 | 48.06 | 15.78 | 16 | 51.93 | 31.26 | 58.82 | 90% | main |
| [Grok 4.6 (xhigh)](https://valuerank.alolabs.dev/models/grok-4-6-xhigh/) | 29 | 47.90 | 15.02 | 17 | 51.66 | 30.06 | 58.87 | 80% | main |
| [DeepSeek V4 Flash (max)](https://valuerank.alolabs.dev/models/deepseek-v4-flash/) | 30 | 45.72 | 38.69 | 12 | 52.92 | 67.49 | 48.06 | 80% | main |
| [Muse Spark 1.3 (xhigh)](https://valuerank.alolabs.dev/models/muse-spark-1-3-xhigh/) | 31 | 45.32 | 17.34 | 29 | 49.42 | 33.73 | 54.65 | 90% | main |
| [DeepSeek V4 Pro (max)](https://valuerank.alolabs.dev/models/deepseek-v4-pro/) | 32 | 44.54 | 28.16 | 26 | 50.21 | 50.84 | 50.00 | 80% | main |
| [Grok 4.7 (xhigh)](https://valuerank.alolabs.dev/models/grok-4-7/) | 33 | 44.26 | 6.93 | 31 | 46.84 | 17.27 | 56.70 | 100% | main |
| [GLM-5.3 (max)](https://valuerank.alolabs.dev/models/glm-5-3/) | 34 | 42.66 | 14.36 | 34 | 46.33 | 29.02 | 52.09 | 100% | main |
| [Gemini 3.8 Flash (high)](https://valuerank.alolabs.dev/models/gemini-3-8-flash/) | 35 | 42.36 | 18.66 | 32 | 46.65 | 35.81 | 50.26 | 100% | main |
| [Qwen3.8 Max](https://valuerank.alolabs.dev/models/qwen3-8-max/) | 36 | 38.04 | 9.06 | 36 | 40.94 | 20.63 | 47.71 | 100% | main |
| [Muse Wonder Full (max)](https://valuerank.alolabs.dev/models/muse-wonder-full/) | — | — | — | — | — | — | 67.74 | 80% | — |

## Not ranked

| Model | Reasons |
|---|---|
| Claude Fable 5 | No exact-variant AA DeepSWE result in the selected source snapshot; Not a required AA frontier or near-frontier family model |
| Claude Opus 4.8 | No exact-variant AA DeepSWE result in the selected source snapshot; Not a required AA frontier or near-frontier family model |
| Claude Sonnet 5 | No exact-variant AA DeepSWE result in the selected source snapshot; Not a required AA frontier or near-frontier family model |
| GLM-5.2 | No eligible exact-model Bug Hunt result in the selected source snapshot; No exact-variant AA DeepSWE result in the selected source snapshot; Not a required AA frontier or near-frontier family model |
| GLM-5.3 Flash | No exact-variant AA DeepSWE result in the selected source snapshot; Not a required AA frontier or near-frontier family model |
| GPT-5.5 | No eligible exact-model Bug Hunt result in the selected source snapshot; No exact-variant AA DeepSWE result in the selected source snapshot; Not a required AA frontier or near-frontier family model |
| Gemini 3.5 Flash | No eligible exact-model Bug Hunt result in the selected source snapshot; No exact-variant AA DeepSWE result in the selected source snapshot; Not a required AA frontier or near-frontier family model |
| Gemini 3.6 Flash | No eligible exact-model Bug Hunt result in the selected source snapshot; No exact-variant AA DeepSWE result in the selected source snapshot; Not a required AA frontier or near-frontier family model |
| Gemini 3.7 Flash | No eligible exact-model Bug Hunt result in the selected source snapshot; No exact-variant AA DeepSWE result in the selected source snapshot; Not a required AA frontier or near-frontier family model |
| Grok 4.6 | No eligible exact-model Bug Hunt result in the selected source snapshot; No exact-variant AA DeepSWE result in the selected source snapshot; Not a required AA frontier or near-frontier family model |
| Kimi K3 | No eligible exact-model Bug Hunt result in the selected source snapshot; No exact-variant AA DeepSWE result in the selected source snapshot; Not a required AA frontier or near-frontier family model |
| Muse Spark 1.2 | No eligible exact-model Bug Hunt result in the selected source snapshot; No exact-variant AA DeepSWE result in the selected source snapshot; Not a required AA frontier or near-frontier family model |

## Quality leaf scores

Each leaf's score z on its fixed 0–100 anchors; "—" marks a leaf with no eligible exact-configuration result.

| Configuration | DeepSWE v1.1 | Bug Hunt Bench | AA FrontierCode 1.1 | Terminal-Bench 4.0 (tbench.ai) | GDPval-AA v2.1 | AutomationBench-AA | AA-Omniscience | AA-LCR v1.1 | Humanity's Last Exam | SciCode | CritPt | Quality | Provisional |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| GPT-6.1 Sol (xhigh) | 73.2 | 40.7 | — | — | 51.9 | 66.6 | 70.4 | 79.7 | 52.6 | 55.7 | 31.7 | 64.04 | no |
| GPT-6.1 Sol (high) | 70.5 | 34.8 | — | — | 50.6 | 64.5 | 70.7 | 82.3 | 51.4 | 55.8 | 30.0 | 62.01 | no |
| GPT-6.1 Sol (medium) | 72.0 | 27.6 | — | — | 47.5 | 62.6 | 70.0 | 83.3 | 49.9 | 53.2 | 27.7 | 60.89 | no |
| Claude Sonnet 5.5 (max) | 72.0 | 48.9 | 45.8 | 61.8 | 66.9 | 71.8 | 66.2 | 82.7 | 55.0 | 61.0 | 31.4 | 64.32 | no |
| Claude Opus 5.5 (max) | 68.4 | 39.7 | 52.2 | 64.8 | 68.3 | 69.5 | 73.2 | 84.7 | 61.4 | 66.9 | 31.7 | 64.19 | no |
| Claude Sonnet 5.5 (xhigh) | 68.4 | 34.3 | 46.1 | — | 61.4 | 65.5 | 61.8 | 79.7 | 50.0 | 57.3 | 31.1 | 59.69 | no |
| Claude Sonnet 5.5 (high) | 66.7 | 32.7 | 44.3 | — | 52.5 | 59.4 | 60.5 | 78.0 | 45.8 | 53.7 | 24.6 | 56.57 | no |
| GPT-6.1 Sol (max) | 69.6 | 42.2 | 49.1 | 58.2 | 54.7 | 64.9 | 70.8 | 83.0 | 52.9 | 54.2 | 31.7 | 61.33 | no |
| GPT-6.1 Sol (low) | 67.6 | 21.4 | — | — | 40.7 | 52.6 | 68.8 | 84.0 | 47.4 | 53.2 | 24.9 | 56.16 | no |
| Claude Sonnet 5.5 (medium) | 65.5 | 22.2 | 29.3 | — | 41.2 | 54.9 | 60.0 | 76.3 | 39.8 | 52.9 | 16.9 | 51.17 | no |
| Claude Opus 5 (max) | 62.5 | 25.7 | — | — | 61.1 | 56.6 | 68.5 | 79.3 | 54.9 | 56.4 | 29.1 | 57.81 | no |
| GPT-6 Sol (max) | 69.0 | 27.9 | — | 49.4 | 50.4 | 61.6 | 63.6 | 83.7 | 47.9 | 57.6 | 30.9 | 58.28 | no |
| Claude Haiku 5.5 (xhigh) | 49.0 | 17.4 | 45.5 | — | 50.7 | 36.0 | 53.0 | 78.3 | 42.7 | 51.7 | 22.6 | 45.36 | no |
| Claude Sonnet 5.5 (low) | 61.9 | 18.1 | 26.4 | — | 33.8 | 49.4 | 59.7 | 76.0 | 36.2 | 49.1 | 11.4 | 47.47 | no |
| GPT-5.6 Sol (max) | 72.3 | 41.4 | — | 37.3 | 55.4 | 60.1 | 61.0 | 84.0 | 49.5 | 57.1 | 32.3 | 59.70 | no |
| GPT-6 Luna (max) | 63.7 | 17.4 | 41.9 | 16.4 | 46.6 | 53.2 | 50.3 | 83.3 | 38.5 | 54.6 | 19.4 | 47.74 | no |
| Claude Haiku 5.5 (high) | 46.3 | 15.2 | 43.6 | — | 45.9 | 33.7 | 52.9 | 77.3 | 37.3 | 48.7 | 18.6 | 42.93 | no |
| GPT-6 Astra (max) | 67.6 | 42.9 | 47.0 | 58.2 | 53.6 | 68.5 | 71.7 | 80.7 | 54.7 | 56.5 | 31.7 | 60.88 | no |
| Claude Haiku 5.5 (medium) | 47.5 | 11.4 | 40.4 | — | 38.7 | 28.6 | 52.2 | 77.3 | 33.8 | 49.0 | 12.9 | 40.94 | no |
| GPT-5.6 Luna (max) | 66.4 | 29.8 | — | 17.3 | 48.0 | 50.2 | 44.9 | 83.7 | 39.5 | 53.6 | 20.6 | 50.01 | no |
| Gemini 4 Argon (high) | 78.8 | 38.8 | 43.5 | — | 56.2 | 77.5 | 71.2 | 79.7 | 57.1 | 61.8 | 27.1 | 65.30 | no |
| Claude Fable 5.1 (max) | 64.3 | 41.0 | 49.0 | 57.9 | 62.7 | 59.4 | 71.7 | 85.3 | 59.1 | 63.1 | 29.7 | 60.25 | no |
| MiMo-V2.6-Flash | — | — | 42.1 | — | 55.4 | 64.1 | 43.7 | 74.3 | 35.1 | 51.3 | 12.0 | 51.74 | coverage 50% below 70%; 1 SWE leaves observed (need 2); observed SWE weight 10% below 40%; DeepSWE v1.1 missing |
| Claude Haiku 5.5 (low) | 45.4 | 10.5 | 29.3 | — | 31.1 | 22.9 | 51.6 | 72.0 | 27.0 | 49.2 | 9.1 | 36.88 | no |
| Claude Haiku 5.5 (max) | 46.0 | 20.5 | 41.8 | — | 55.9 | 35.4 | 55.3 | 82.7 | 44.4 | 55.0 | 18.9 | 45.33 | no |
| Muse Wonder (max) | 75.8 | 30.2 | — | — | 63.5 | 68.1 | 62.7 | 80.7 | 50.1 | 60.3 | 28.3 | 64.42 | no |
| MiMo-V2.6-Pro | — | 17.1 | 45.4 | — | 59.2 | 58.6 | 54.2 | 86.3 | 49.4 | 60.9 | 26.6 | 50.09 | coverage 60% below 70%; observed SWE weight 20% below 40%; DeepSWE v1.1 missing |
| Muse Spark 1.3 (max) | 71.7 | 30.7 | 40.6 | — | 59.0 | 57.9 | 62.5 | 83.0 | 48.7 | 58.8 | 24.9 | 58.82 | no |
| Grok 4.6 (xhigh) | 64.9 | 27.3 | — | — | 57.3 | 67.0 | 64.7 | 81.0 | 44.1 | 53.0 | 19.7 | 58.87 | no |
| DeepSeek V4 Flash (max) | 54.3 | 20.7 | — | — | 46.7 | 54.0 | 42.9 | 79.7 | 38.6 | 50.3 | 16.6 | 48.06 | no |
| Muse Spark 1.3 (xhigh) | 73.2 | 19.3 | — | 14.5 | 56.3 | 56.8 | 61.6 | 83.0 | 47.5 | 59.7 | 26.0 | 54.65 | no |
| DeepSeek V4 Pro (max) | 57.2 | 15.2 | — | — | 47.5 | 56.7 | 50.4 | 80.3 | 41.0 | 51.0 | 18.0 | 50.00 | no |
| Grok 4.7 (xhigh) | 72.6 | 27.6 | 33.8 | 37.6 | 60.6 | 65.6 | 66.0 | 76.7 | 43.1 | 57.4 | 17.7 | 56.70 | no |
| GLM-5.3 (max) | 61.4 | 18.1 | 40.1 | 41.8 | 57.5 | 62.2 | 57.1 | 79.7 | 42.3 | 59.0 | 19.1 | 52.09 | no |
| Gemini 3.8 Flash (high) | 65.8 | 17.1 | 36.4 | 19.1 | 46.8 | 59.9 | 64.8 | 81.3 | 47.8 | 56.6 | 18.3 | 50.26 | no |
| Qwen3.8 Max | 51.0 | 24.5 | 43.2 | 27.0 | 58.3 | 56.2 | 56.0 | 80.3 | 43.1 | 52.1 | 17.7 | 47.71 | no |
| Muse Wonder Full (max) | 77.0 | 40.0 | — | — | 67.9 | 71.3 | 65.1 | 83.7 | 53.6 | 62.6 | 32.9 | 67.74 | no |

## Basket cost by component

USD at API rates for the exact configuration; "—" marks a component without an exact cost.

| Configuration | Coding Agent Index | FrontierCode | ITBench-AA | AA-Briefcase | GDPval-AA | GDP.pdf | AutomationBench-AA | Terminal-Bench 4.0 (AA Index run) | SciCode | AA-LCR | Basket cost | Missing admitted components |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| GPT-6.1 Sol (xhigh) | $315.03 | — | — | $94.51 | $122.86 | $36.81 | $164.62 | $67.71 | $6.35 | $19.35 | $827.23 | none |
| GPT-6.1 Sol (high) | $269.44 | — | — | $76.16 | $94.10 | $34.94 | $148.34 | $54.66 | $3.73 | $19.14 | $700.51 | none |
| GPT-6.1 Sol (medium) | $213.52 | — | — | $42.26 | $50.86 | $33.75 | $128.97 | $40.51 | $2.68 | $19.02 | $531.56 | none |
| Claude Sonnet 5.5 (max) | $4,299.81 | $826.00 | — | $1,863.13 | $1,504.30 | $79.43 | $678.32 | $834.67 | $80.07 | $33.93 | $9,373.65 | none |
| Claude Opus 5.5 (max) | $3,950.02 | $1,015.00 | $146.00 | $1,915.18 | $1,962.05 | $155.23 | $938.69 | $865.21 | $135.11 | $67.66 | $9,989.15 | none |
| Claude Sonnet 5.5 (xhigh) | $1,010.02 | $120.00 | — | $634.80 | $430.06 | $46.01 | $277.51 | $401.18 | $6.81 | $29.66 | $2,836.05 | none |
| Claude Sonnet 5.5 (high) | $374.36 | — | — | $297.64 | $151.47 | $40.86 | $205.39 | $144.29 | $4.61 | $29.39 | $1,248.00 | none |
| GPT-6.1 Sol (max) | $470.90 | $81.00 | — | $210.45 | $196.57 | $41.99 | $195.01 | $120.30 | $12.50 | $19.94 | $1,267.66 | none |
| GPT-6.1 Sol (low) | $151.14 | — | — | $16.12 | $23.10 | $33.41 | $104.75 | $25.27 | $2.43 | $18.99 | $375.21 | none |
| Claude Sonnet 5.5 (medium) | $187.48 | — | — | $126.68 | $69.91 | $38.14 | $172.20 | $104.16 | $3.90 | $29.16 | $731.63 | none |
| Claude Opus 5 (max) | $3,269.11 | — | — | $1,619.19 | $1,488.52 | $108.57 | $864.64 | $1,273.08 | $33.90 | $76.11 | $8,733.13 | none |
| GPT-6 Sol (max) | $905.89 | — | $38.00 | $238.81 | $280.84 | $42.54 | $235.06 | $264.22 | $12.24 | $19.82 | $1,999.41 | none |
| Claude Haiku 5.5 (xhigh) | $184.98 | $16.00 | — | $33.29 | $20.26 | $2.73 | $18.14 | $30.38 | $0.77 | $1.53 | $292.07 | none |
| Claude Sonnet 5.5 (low) | $146.38 | — | — | $73.03 | $45.90 | $37.23 | $158.19 | $84.80 | $3.73 | $29.14 | $578.39 | none |
| GPT-5.6 Sol (max) | $1,925.06 | — | $106.00 | $365.84 | $618.22 | $92.85 | $638.90 | $534.15 | $22.95 | $40.16 | $4,238.14 | none |
| GPT-6 Luna (max) | $53.30 | $9.00 | — | $15.47 | $19.66 | $2.85 | $23.91 | $15.59 | $1.06 | $1.02 | $132.87 | none |
| Claude Haiku 5.5 (high) | $110.50 | — | — | $20.29 | $9.59 | $2.26 | $14.91 | $21.88 | $0.43 | $1.50 | $181.35 | none |
| GPT-6 Astra (max) | $2,262.53 | $422.00 | $133.00 | $864.69 | $996.49 | $207.58 | $1,048.30 | $560.88 | $66.89 | $99.73 | $6,107.09 | none |
| Claude Haiku 5.5 (medium) | $68.60 | — | — | $12.10 | $4.56 | $2.06 | $12.57 | $12.79 | $0.34 | $1.49 | $114.51 | none |
| GPT-5.6 Luna (max) | $132.72 | — | — | $35.95 | $24.18 | $5.68 | $59.91 | $56.06 | $2.67 | $2.09 | $319.25 | none |
| Gemini 4 Argon (high) | $1,770.70 | $670.00 | — | $530.33 | $400.23 | $25.93 | $399.89 | $447.49 | $30.44 | $23.64 | $3,628.64 | none |
| Claude Fable 5.1 (max) | $3,753.59 | $1,200.00 | $237.00 | $2,066.92 | $2,150.47 | $277.49 | $1,715.62 | $1,268.42 | $189.65 | $158.45 | $11,580.62 | none |
| MiMo-V2.6-Flash | — | — | — | $13.81 | $16.10 | $2.01 | $10.94 | $15.19 | $0.81 | $1.51 | $60.37 | Coding Agent Index |
| Claude Haiku 5.5 (low) | $43.40 | — | — | $4.30 | $2.28 | $1.93 | $10.04 | $7.82 | $0.27 | $1.48 | $71.52 | none |
| Claude Haiku 5.5 (max) | $781.84 | $33.00 | — | $61.41 | $48.90 | $5.27 | $27.80 | $43.02 | $3.15 | $1.93 | $973.34 | none |
| Muse Wonder (max) | $2,439.83 | — | — | $1,133.00 | $1,075.46 | $72.26 | $545.12 | $1,185.90 | $38.88 | $43.70 | $6,534.16 | none |
| MiMo-V2.6-Pro | — | $18.00 | — | $34.60 | $35.47 | $2.40 | $27.77 | $28.91 | $2.25 | $4.74 | $136.13 | Coding Agent Index |
| Muse Spark 1.3 (max) | $1,205.18 | — | — | $369.37 | $448.59 | $20.51 | $238.77 | $457.96 | $11.31 | $13.29 | $2,764.98 | none |
| Grok 4.6 (xhigh) | $1,081.75 | — | — | $444.04 | $536.69 | $26.17 | $430.84 | $435.30 | $8.52 | $20.36 | $2,983.67 | none |
| DeepSeek V4 Flash (max) | $25.77 | — | — | $38.53 | $63.77 | $4.66 | $69.22 | $60.65 | $12.16 | $4.76 | $279.51 | none |
| Muse Spark 1.3 (xhigh) | $1,050.73 | — | — | $311.27 | $307.10 | $19.64 | $242.26 | $411.31 | $10.70 | $13.15 | $2,366.16 | none |
| DeepSeek V4 Pro (max) | $72.13 | — | — | $90.59 | $127.70 | $11.00 | $223.87 | $247.85 | $14.47 | $13.89 | $801.50 | none |
| Grok 4.7 (xhigh) | $2,671.69 | $1,131.00 | $203.00 | $846.62 | $1,415.17 | $32.43 | $707.44 | $963.85 | $38.30 | $24.51 | $6,700.02 | none |
| GLM-5.3 (max) | $1,285.14 | $432.00 | $91.00 | $514.04 | $496.54 | $17.34 | $302.51 | $532.24 | $23.62 | $14.86 | $3,186.29 | none |
| Gemini 3.8 Flash (high) | $747.62 | $372.00 | $86.00 | $245.87 | $372.82 | $10.90 | $278.70 | $385.54 | $22.12 | $9.88 | $2,073.44 | none |
| Qwen3.8 Max | $1,054.13 | $675.00 | $327.00 | $1,781.49 | $998.39 | $33.31 | $261.64 | $1,232.62 | $32.57 | $22.88 | $5,417.03 | none |
| Muse Wonder Full (max) | — | — | — | — | — | — | — | — | — | — | — | Coding Agent Index, AA-Briefcase, GDPval-AA, GDP.pdf, AutomationBench-AA, Terminal-Bench 4.0 (AA Index run), SciCode, AA-LCR |

### Valuation basis

Valuation-basis gate (E170): 35 compatible as captured, 2 valuation basis unverified (flagged: Claude Fable 5.1 (max), Muse Wonder Full (max)). AA's Index category costs reconcile exactly with the prices AA displays for each configuration at capture, so its applied prices are the prices in force at the release cutoff. Token metering (E176): 37 not published per configuration; AA values cached input at live measurements of each model's typical cache-hit rate. Source intervals (E174): terminalBench: captured, level 95% (tbench.ai: "The whiskers span the 95% confidence interval"); gdpval: published, not captured, level not stated by the source (the 95% level on AA's methodology page belongs to AA-Briefcase).

## Plan route selection

The Plan amount is the selected multiple times the cash paid for the fee period (E166), typed by what the measurement establishes; it is not capacity unless it says so. The multiple values only the measured workload's API-equivalent consumption; other plan features are not valued.

| Configuration | Selected route | Plan amount | Identification | Plan cost (USD per basket run) | Flags | Selection reason |
|---|---|---|---|---:|---|---|
| GPT-6.1 Sol (xhigh) | ChatGPT Pro $500 · common GPT assumption (10.772×, assumption) | $5,386 per month: assumed API-equivalent consumption (owner-named transfer) | unidentified | $76.79 | workload-unmatched; owner-named transfer (assumption); valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| GPT-6.1 Sol (high) | ChatGPT Pro $500 · common GPT assumption (10.772×, assumption) | $5,386 per month: assumed API-equivalent consumption (owner-named transfer) | unidentified | $65.03 | workload-unmatched; owner-named transfer (assumption); valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| GPT-6.1 Sol (medium) | ChatGPT Pro $500 · common GPT assumption (10.772×, assumption) | $5,386 per month: assumed API-equivalent consumption (owner-named transfer) | unidentified | $49.35 | workload-unmatched; owner-named transfer (assumption); valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| Claude Sonnet 5.5 (max) | Claude Pro $20 · common Claude assumption (58.9×, assumption) | $1,178 per month: assumed API-equivalent consumption (owner-named transfer) from claude-pro-opus55-semianalysis | unidentified | $159.15 | workload-unmatched; owner-named transfer (assumption); valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| Claude Opus 5.5 (max) | Claude Pro $20 · Opus 5.5 (58.9×, measured) | $1,178 per month: measured-workload capacity | unidentified | $169.60 | workload-unmatched; valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| Claude Sonnet 5.5 (xhigh) | Claude Pro $20 · common Claude assumption (58.9×, assumption) | $1,178 per month: assumed API-equivalent consumption (owner-named transfer) from claude-pro-opus55-semianalysis | unidentified | $48.15 | workload-unmatched; owner-named transfer (assumption); valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| Claude Sonnet 5.5 (high) | Claude Pro $20 · common Claude assumption (58.9×, assumption) | $1,178 per month: assumed API-equivalent consumption (owner-named transfer) from claude-pro-opus55-semianalysis | unidentified | $21.19 | workload-unmatched; owner-named transfer (assumption); valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| GPT-6.1 Sol (max) | ChatGPT Pro $500 · common GPT assumption (10.772×, measured) | $5,386 per month: measured-workload capacity | unidentified | $117.68 | workload-unmatched; valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| GPT-6.1 Sol (low) | ChatGPT Pro $500 · common GPT assumption (10.772×, assumption) | $5,386 per month: assumed API-equivalent consumption (owner-named transfer) | unidentified | $34.83 | workload-unmatched; owner-named transfer (assumption); valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| Claude Sonnet 5.5 (medium) | Claude Pro $20 · common Claude assumption (58.9×, assumption) | $1,178 per month: assumed API-equivalent consumption (owner-named transfer) from claude-pro-opus55-semianalysis | unidentified | $12.42 | workload-unmatched; owner-named transfer (assumption); valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| Claude Opus 5 (max) | Claude Pro $20 · common Claude assumption (58.9×, assumption) | $1,178 per month: assumed API-equivalent consumption (owner-named transfer) from claude-pro-opus55-semianalysis | unidentified | $148.27 | workload-unmatched; owner-named transfer (assumption); valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| GPT-6 Sol (max) | ChatGPT Pro $500 · common GPT assumption (10.772×, assumption) | $5,386 per month: assumed API-equivalent consumption (owner-named transfer) | unidentified | $185.61 | workload-unmatched; owner-named transfer (assumption); valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| Claude Haiku 5.5 (xhigh) | Claude Pro $20 · common Claude assumption (58.9×, assumption) | $1,178 per month: assumed API-equivalent consumption (owner-named transfer) from claude-pro-opus55-semianalysis | unidentified | $4.96 | workload-unmatched; owner-named transfer (assumption); valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| Claude Sonnet 5.5 (low) | Claude Pro $20 · common Claude assumption (58.9×, assumption) | $1,178 per month: assumed API-equivalent consumption (owner-named transfer) from claude-pro-opus55-semianalysis | unidentified | $9.82 | workload-unmatched; owner-named transfer (assumption); valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| GPT-5.6 Sol (max) | ChatGPT Pro $500 · common GPT assumption (10.772×, assumption) | $5,386 per month: assumed API-equivalent consumption (owner-named transfer) | unidentified | $393.44 | workload-unmatched; owner-named transfer (assumption); valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| GPT-6 Luna (max) | ChatGPT Pro $500 · common GPT assumption (10.772×, assumption) | $5,386 per month: assumed API-equivalent consumption (owner-named transfer) | unidentified | $12.33 | workload-unmatched; owner-named transfer (assumption); valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| Claude Haiku 5.5 (high) | Claude Pro $20 · common Claude assumption (58.9×, assumption) | $1,178 per month: assumed API-equivalent consumption (owner-named transfer) from claude-pro-opus55-semianalysis | unidentified | $3.08 | workload-unmatched; owner-named transfer (assumption); valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| GPT-6 Astra (max) | ChatGPT Plus $20 · common GPT assumption (8.1×, measured) | $162 per month: measured-workload capacity | unidentified | $753.96 | workload-unmatched; valuation basis unverified | higher evidence grade |
| Claude Haiku 5.5 (medium) | Claude Pro $20 · common Claude assumption (58.9×, assumption) | $1,178 per month: assumed API-equivalent consumption (owner-named transfer) from claude-pro-opus55-semianalysis | unidentified | $1.94 | workload-unmatched; owner-named transfer (assumption); valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| GPT-5.6 Luna (max) | ChatGPT Pro $500 · common GPT assumption (10.772×, assumption) | $5,386 per month: assumed API-equivalent consumption (owner-named transfer) | unidentified | $29.64 | workload-unmatched; owner-named transfer (assumption); valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| Gemini 4 Argon (high) | — | — | — | $3,628.64 | API-cost fallback: no admitted Plan route; cross-estimand ordering not identified | no eligible route |
| Claude Fable 5.1 (max) | Claude Max $100 · Fable 5.1 (12.73×, measured) | $1,273 per month: measured-workload capacity | unidentified | $909.71 | workload-unmatched; valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| MiMo-V2.6-Flash | MiMo · provisional 1.5x assumption (1.5×, assumption) | fee not established: assumed API-equivalent consumption (owner-named transfer) | unidentified | $40.25 | workload-unmatched; owner-named transfer (assumption); valuation basis unverified; observed-usage multiple; full utilisation not established | only remaining eligible route |
| Claude Haiku 5.5 (low) | Claude Pro $20 · common Claude assumption (58.9×, assumption) | $1,178 per month: assumed API-equivalent consumption (owner-named transfer) from claude-pro-opus55-semianalysis | unidentified | $1.21 | workload-unmatched; owner-named transfer (assumption); valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| Claude Haiku 5.5 (max) | Claude Pro $20 · common Claude assumption (58.9×, assumption) | $1,178 per month: assumed API-equivalent consumption (owner-named transfer) from claude-pro-opus55-semianalysis | unidentified | $16.53 | workload-unmatched; owner-named transfer (assumption); valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| Muse Wonder (max) | — | — | — | $6,534.16 | API-cost fallback: no admitted Plan route; cross-estimand ordering not identified | no eligible route |
| MiMo-V2.6-Pro | MiMo · provisional 1.5x assumption (1.5×, assumption) | fee not established: assumed API-equivalent consumption (owner-named transfer) | unidentified | $90.75 | workload-unmatched; owner-named transfer (assumption); valuation basis unverified; observed-usage multiple; full utilisation not established | only remaining eligible route |
| Muse Spark 1.3 (max) | — | — | — | $2,764.98 | API-cost fallback: no admitted Plan route; cross-estimand ordering not identified | no eligible route |
| Grok 4.6 (xhigh) | — | — | — | $2,983.67 | API-cost fallback: no admitted Plan route; cross-estimand ordering not identified | no eligible route |
| DeepSeek V4 Flash (max) | — | — | — | $279.51 | API-cost fallback: no admitted Plan route; cross-estimand ordering not identified | no eligible route |
| Muse Spark 1.3 (xhigh) | — | — | — | $2,366.16 | API-cost fallback: no admitted Plan route; cross-estimand ordering not identified | no eligible route |
| DeepSeek V4 Pro (max) | — | — | — | $801.50 | API-cost fallback: no admitted Plan route; cross-estimand ordering not identified | no eligible route |
| Grok 4.7 (xhigh) | — | — | — | $6,700.02 | API-cost fallback: no admitted Plan route; cross-estimand ordering not identified | no eligible route |
| GLM-5.3 (max) | — | — | — | $3,186.29 | API-cost fallback: no admitted Plan route; cross-estimand ordering not identified | no eligible route |
| Gemini 3.8 Flash (high) | — | — | — | $2,073.44 | API-cost fallback: no admitted Plan route; cross-estimand ordering not identified | no eligible route |
| Qwen3.8 Max | — | — | — | $5,417.03 | API-cost fallback: no admitted Plan route; cross-estimand ordering not identified | no eligible route |
| Muse Wonder Full (max) | — | — | — | — | — | no eligible route |

### Route alternatives

Every admissible route-measurement pair in comparator order (E171) and the comparator's pick with the selected pair removed (E179). A larger displayed multiple is arithmetic on the measured workload, never a claim that the route is cheaper on the scored workload. Workday-feasible multiple (E15), for the 25 routed rows: not evaluated: no evidenced quota schema for this route.

| Configuration | Admissible pairs | Unidentified | Pairs (multiple, status) | Leave-selected-out choice |
|---|---:|---:|---|---|
| GPT-6.1 Sol (xhigh) | 4 | 4 | chatgpt-pro500-common-semianalysis-assumption (10.772×, selected); chatgpt-pro100-common-semianalysis-assumption (10.55×, not selected by the comparator); chatgpt-pro200-common-semianalysis-assumption (10.42×, not selected by the comparator); chatgpt-plus-common-semianalysis-assumption (8.1×, not selected by the comparator) | chatgpt-pro100-common-semianalysis-assumption (10.55×, value 60.88) |
| GPT-6.1 Sol (high) | 4 | 4 | chatgpt-pro500-common-semianalysis-assumption (10.772×, selected); chatgpt-pro100-common-semianalysis-assumption (10.55×, not selected by the comparator); chatgpt-pro200-common-semianalysis-assumption (10.42×, not selected by the comparator); chatgpt-plus-common-semianalysis-assumption (8.1×, not selected by the comparator) | chatgpt-pro100-common-semianalysis-assumption (10.55×, value 59.77) |
| GPT-6.1 Sol (medium) | 4 | 4 | chatgpt-pro500-common-semianalysis-assumption (10.772×, selected); chatgpt-pro100-common-semianalysis-assumption (10.55×, not selected by the comparator); chatgpt-pro200-common-semianalysis-assumption (10.42×, not selected by the comparator); chatgpt-plus-common-semianalysis-assumption (8.1×, not selected by the comparator) | chatgpt-pro100-common-semianalysis-assumption (10.55×, value 59.63) |
| Claude Sonnet 5.5 (max) | 3 | 3 | claude-pro-common-opus55-assumption (58.9×, selected); claude-max20x-common-opus55-assumption (58.63×, not selected by the comparator); claude-max5x-common-opus55-assumption (57.25×, not selected by the comparator) | claude-max20x-common-opus55-assumption (58.63×, value 59.31) |
| Claude Opus 5.5 (max) | 3 | 3 | claude-pro-opus55-semianalysis (58.9×, selected); claude-max20x-opus55-semianalysis (58.63×, not selected by the comparator); claude-max5x-opus55-semianalysis (57.25×, not selected by the comparator) | claude-max20x-opus55-semianalysis (58.63×, value 59.06) |
| Claude Sonnet 5.5 (xhigh) | 3 | 3 | claude-pro-common-opus55-assumption (58.9×, selected); claude-max20x-common-opus55-assumption (58.63×, not selected by the comparator); claude-max5x-common-opus55-assumption (57.25×, not selected by the comparator) | claude-max20x-common-opus55-assumption (58.63×, value 58.83) |
| Claude Sonnet 5.5 (high) | 3 | 3 | claude-pro-common-opus55-assumption (58.9×, selected); claude-max20x-common-opus55-assumption (58.63×, not selected by the comparator); claude-max5x-common-opus55-assumption (57.25×, not selected by the comparator) | claude-max20x-common-opus55-assumption (58.63×, value 58.54) |
| GPT-6.1 Sol (max) | 4 | 4 | chatgpt-pro500-common-semianalysis-assumption (10.772×, selected); chatgpt-pro100-common-semianalysis-assumption (10.55×, not selected by the comparator); chatgpt-pro200-common-semianalysis-assumption (10.42×, not selected by the comparator); chatgpt-plus-common-semianalysis-assumption (8.1×, not selected by the comparator) | chatgpt-pro100-common-semianalysis-assumption (10.55×, value 57.78) |
| GPT-6.1 Sol (low) | 4 | 4 | chatgpt-pro500-common-semianalysis-assumption (10.772×, selected); chatgpt-pro100-common-semianalysis-assumption (10.55×, not selected by the comparator); chatgpt-pro200-common-semianalysis-assumption (10.42×, not selected by the comparator); chatgpt-plus-common-semianalysis-assumption (8.1×, not selected by the comparator) | chatgpt-pro100-common-semianalysis-assumption (10.55×, value 56.94) |
| Claude Sonnet 5.5 (medium) | 3 | 3 | claude-pro-common-opus55-assumption (58.9×, selected); claude-max20x-common-opus55-assumption (58.63×, not selected by the comparator); claude-max5x-common-opus55-assumption (57.25×, not selected by the comparator) | claude-max20x-common-opus55-assumption (58.63×, value 55.82) |
| Claude Opus 5 (max) | 3 | 3 | claude-pro-common-opus55-assumption (58.9×, selected); claude-max20x-common-opus55-assumption (58.63×, not selected by the comparator); claude-max5x-common-opus55-assumption (57.25×, not selected by the comparator) | claude-max20x-common-opus55-assumption (58.63×, value 54.60) |
| GPT-6 Sol (max) | 4 | 4 | chatgpt-pro500-common-semianalysis-assumption (10.772×, selected); chatgpt-pro100-common-semianalysis-assumption (10.55×, not selected by the comparator); chatgpt-pro200-common-semianalysis-assumption (10.42×, not selected by the comparator); chatgpt-plus-common-semianalysis-assumption (8.1×, not selected by the comparator) | chatgpt-pro100-common-semianalysis-assumption (10.55×, value 54.35) |
| Claude Haiku 5.5 (xhigh) | 3 | 3 | claude-pro-common-opus55-assumption (58.9×, selected); claude-max20x-common-opus55-assumption (58.63×, not selected by the comparator); claude-max5x-common-opus55-assumption (57.25×, not selected by the comparator) | claude-max20x-common-opus55-assumption (58.63×, value 53.76) |
| Claude Sonnet 5.5 (low) | 3 | 3 | claude-pro-common-opus55-assumption (58.9×, selected); claude-max20x-common-opus55-assumption (58.63×, not selected by the comparator); claude-max5x-common-opus55-assumption (57.25×, not selected by the comparator) | claude-max20x-common-opus55-assumption (58.63×, value 53.63) |
| GPT-5.6 Sol (max) | 4 | 4 | chatgpt-pro500-common-semianalysis-assumption (10.772×, selected); chatgpt-pro100-common-semianalysis-assumption (10.55×, not selected by the comparator); chatgpt-pro200-common-semianalysis-assumption (10.42×, not selected by the comparator); chatgpt-plus-common-semianalysis-assumption (8.1×, not selected by the comparator) | chatgpt-pro100-common-semianalysis-assumption (10.55×, value 53.54) |
| GPT-6 Luna (max) | 4 | 4 | chatgpt-pro500-common-semianalysis-assumption (10.772×, selected); chatgpt-pro100-common-semianalysis-assumption (10.55×, not selected by the comparator); chatgpt-pro200-common-semianalysis-assumption (10.42×, not selected by the comparator); chatgpt-plus-common-semianalysis-assumption (8.1×, not selected by the comparator) | chatgpt-pro100-common-semianalysis-assumption (10.55×, value 53.22) |
| Claude Haiku 5.5 (high) | 3 | 3 | claude-pro-common-opus55-assumption (58.9×, selected); claude-max20x-common-opus55-assumption (58.63×, not selected by the comparator); claude-max5x-common-opus55-assumption (57.25×, not selected by the comparator) | claude-max20x-common-opus55-assumption (58.63×, value 53.13) |
| GPT-6 Astra (max) | 4 | 4 | chatgpt-plus-common-semianalysis-assumption (8.1×, selected); chatgpt-pro500-common-semianalysis-assumption (10.772×, not selected by the comparator); chatgpt-pro100-common-semianalysis-assumption (10.55×, not selected by the comparator); chatgpt-pro200-common-semianalysis-assumption (10.42×, not selected by the comparator) | chatgpt-pro500-common-semianalysis-assumption (10.772×, value 53.57) |
| Claude Haiku 5.5 (medium) | 3 | 3 | claude-pro-common-opus55-assumption (58.9×, selected); claude-max20x-common-opus55-assumption (58.63×, not selected by the comparator); claude-max5x-common-opus55-assumption (57.25×, not selected by the comparator) | claude-max20x-common-opus55-assumption (58.63×, value 52.79) |
| GPT-5.6 Luna (max) | 4 | 4 | chatgpt-pro500-common-semianalysis-assumption (10.772×, selected); chatgpt-pro100-common-semianalysis-assumption (10.55×, not selected by the comparator); chatgpt-pro200-common-semianalysis-assumption (10.42×, not selected by the comparator); chatgpt-plus-common-semianalysis-assumption (8.1×, not selected by the comparator) | chatgpt-pro100-common-semianalysis-assumption (10.55×, value 52.74) |
| Claude Fable 5.1 (max) | 2 | 2 | claude-max5x-fable51-semianalysis (12.73×, selected); claude-max20x-fable51-semianalysis (12.425×, not selected by the comparator) | claude-max20x-fable51-semianalysis (12.425×, value 51.85) |
| MiMo-V2.6-Flash | 1 | 1 | mimo-provisional-user-assumption (1.5×, selected) | none: the row would fall back to API cost (O13) |
| Claude Haiku 5.5 (low) | 3 | 3 | claude-pro-common-opus55-assumption (58.9×, selected); claude-max20x-common-opus55-assumption (58.63×, not selected by the comparator); claude-max5x-common-opus55-assumption (57.25×, not selected by the comparator) | claude-max20x-common-opus55-assumption (58.63×, value 50.92) |
| Claude Haiku 5.5 (max) | 3 | 3 | claude-pro-common-opus55-assumption (58.9×, selected); claude-max20x-common-opus55-assumption (58.63×, not selected by the comparator); claude-max5x-common-opus55-assumption (57.25×, not selected by the comparator) | claude-max20x-common-opus55-assumption (58.63×, value 50.73) |
| MiMo-V2.6-Pro | 1 | 1 | mimo-provisional-user-assumption (1.5×, selected) | none: the row would fall back to API cost (O13) |

### Measured-only Plan view

Admission: exact-route measurement candidates of grade controlled or concordant reports (no transfers, no diagnostics). Selection: the official selector (E111, E88, E85) rerun among the admitted candidates. Panel: rows with an admitted measured candidate; others listed as 'no measured route' (no API fallback).

| Configuration | Status | Route | Plan cost | Value | Rank |
|---|---|---|---:|---:|---:|
| Claude Opus 5.5 (max) | measured, target-workload unmatched | claude-pro-opus55-semianalysis | $169.60 | 59.07 | 1 |
| GPT-6.1 Sol (max) | measured, target-workload unmatched | chatgpt-pro500-common-semianalysis-assumption | $117.68 | 57.83 | 2 |
| GPT-6 Astra (max) | measured, target-workload unmatched | chatgpt-plus-common-semianalysis-assumption | $753.96 | 52.85 | 3 |
| Claude Fable 5.1 (max) | measured, target-workload unmatched | claude-max5x-fable51-semianalysis | $909.71 | 51.91 | 4 |
| Claude Haiku 5.5 (high) | no measured route | — | — | — | — |
| Claude Haiku 5.5 (low) | no measured route | — | — | — | — |
| Claude Haiku 5.5 (max) | no measured route | — | — | — | — |
| Claude Haiku 5.5 (medium) | no measured route | — | — | — | — |
| Claude Haiku 5.5 (xhigh) | no measured route | — | — | — | — |
| Claude Opus 5 (max) | no measured route | — | — | — | — |
| Claude Sonnet 5.5 (high) | no measured route | — | — | — | — |
| Claude Sonnet 5.5 (low) | no measured route | — | — | — | — |
| Claude Sonnet 5.5 (max) | no measured route | — | — | — | — |
| Claude Sonnet 5.5 (medium) | no measured route | — | — | — | — |
| Claude Sonnet 5.5 (xhigh) | no measured route | — | — | — | — |
| DeepSeek V4 Flash (max) | no measured route | — | — | — | — |
| DeepSeek V4 Pro (max) | no measured route | — | — | — | — |
| GLM-5.3 (max) | no measured route | — | — | — | — |
| GPT-5.6 Luna (max) | no measured route | — | — | — | — |
| GPT-5.6 Sol (max) | no measured route | — | — | — | — |
| GPT-6 Luna (max) | no measured route | — | — | — | — |
| GPT-6 Sol (max) | no measured route | — | — | — | — |
| GPT-6.1 Sol (high) | no measured route | — | — | — | — |
| GPT-6.1 Sol (low) | no measured route | — | — | — | — |
| GPT-6.1 Sol (medium) | no measured route | — | — | — | — |
| GPT-6.1 Sol (xhigh) | no measured route | — | — | — | — |
| Gemini 3.8 Flash (high) | no measured route | — | — | — | — |
| Gemini 4 Argon (high) | no measured route | — | — | — | — |
| Grok 4.6 (xhigh) | no measured route | — | — | — | — |
| Grok 4.7 (xhigh) | no measured route | — | — | — | — |
| MiMo-V2.6-Flash | no measured route | — | — | — | — |
| MiMo-V2.6-Pro | no measured route | — | — | — | — |
| Muse Spark 1.3 (max) | no measured route | — | — | — | — |
| Muse Spark 1.3 (xhigh) | no measured route | — | — | — | — |
| Muse Wonder (max) | no measured route | — | — | — | — |
| Muse Wonder Full (max) | no measured route | — | — | — | — |
| Qwen3.8 Max | no measured route | — | — | — | — |

#### Measured-evidence calibration (diagnostic)

References: each workload's measured-only rows with complete cost evidence are the references: c_L = cheapest / 2, c_H = dearest x 2 (diagnostic only; the official anchors are unchanged). Status: evaluated.

- Workload `9a0d376cc6080f3c`: measured anchors $58.84 to $1,507.92 from Claude Opus 5.5 (max), GPT-6 Astra (max), GPT-6.1 Sol (max); anchor ratio 25.6 against the official 22070.1. Official Plan anchors are set by Claude Haiku 5.5 (low) (owner-named transfer) at the low end and Grok 4.7 (xhigh) (API-cost fallback) at the high end.
- Workload `1453a9a0576b02ea`: measured-evidence calibration unavailable (fewer than two measured references); measured rows none. Official Plan anchors are set by Claude Haiku 5.5 (low) (owner-named transfer) at the low end and Qwen3.8 Max (API-cost fallback) at the high end.

| Configuration | Value on official Plan anchors | Value on measured anchors | Rank change |
|---|---:|---:|---:|
| Claude Fable 5.1 (max) | 51.91 | 49.08 | 0 |
| Claude Opus 5.5 (max) | 59.07 | 64.99 | 1 |
| GPT-6 Astra (max) | 52.85 | 51.00 | 0 |
| GPT-6.1 Sol (max) | 57.83 | 65.65 | -1 |

Pairwise reversals: Claude Opus 5.5 (max) and GPT-6.1 Sol (max). Largest value change: 7.82 points.

## Interval outputs

**API basis, main workload: frontier.** Not evaluable: Claude Fable 5.1 (max), MiMo-V2.6-Flash, MiMo-V2.6-Pro, Muse Wonder Full (max).

| Configuration | Possible frontier | Definite frontier | Definite counterexample | Possible frontier blocked by |
|---|---|---|---|---|
| Gemini 4 Argon (high) | certified | disproved | GPT-6.1 Sol (xhigh) | — |
| GPT-6.1 Sol (xhigh) | certified | disproved | GPT-6.1 Sol (high) | — |
| Claude Sonnet 5.5 (max) | certified | disproved | Gemini 4 Argon (high) | — |
| GPT-6.1 Sol (max) | certified | disproved | GPT-6.1 Sol (xhigh) | — |
| GPT-6.1 Sol (high) | certified | disproved | GPT-6.1 Sol (medium) | — |
| Muse Wonder (max) | certified | disproved | Gemini 4 Argon (high) | — |
| GPT-6.1 Sol (medium) | certified | disproved | GPT-6.1 Sol (low) | — |
| Claude Opus 5.5 (max) | disproved | disproved | Gemini 4 Argon (high) | Claude Sonnet 5.5 (max) |
| GPT-6 Astra (max) | disproved | disproved | Gemini 4 Argon (high) | GPT-6.1 Sol (max) |
| GPT-5.6 Sol (max) | certified | disproved | Gemini 4 Argon (high) | — |
| Muse Spark 1.3 (max) | certified | disproved | GPT-6.1 Sol (xhigh) | — |
| Claude Sonnet 5.5 (xhigh) | certified | disproved | GPT-6.1 Sol (xhigh) | — |
| Muse Spark 1.3 (xhigh) | disproved | disproved | GPT-6.1 Sol (xhigh) | GPT-6.1 Sol (max) |
| GPT-6 Sol (max) | certified | disproved | GPT-6.1 Sol (xhigh) | — |
| Grok 4.7 (xhigh) | disproved | disproved | Gemini 4 Argon (high) | Gemini 4 Argon (high), GPT-6.1 Sol (max), GPT-6 Astra (max) |
| Claude Sonnet 5.5 (high) | certified | disproved | GPT-6.1 Sol (xhigh) | — |
| GPT-6.1 Sol (low) | certified | disproved | GPT-5.6 Luna (max) | — |
| GPT-5.6 Luna (max) | certified | disproved | GPT-6 Luna (max) | — |
| Grok 4.6 (xhigh) | certified | disproved | GPT-6.1 Sol (xhigh) | — |
| GPT-6 Luna (max) | certified | certified | — | — |
| Claude Haiku 5.5 (max) | disproved | disproved | GPT-6.1 Sol (xhigh) | GPT-6.1 Sol (xhigh) |
| Gemini 3.8 Flash (high) | disproved | disproved | GPT-6.1 Sol (xhigh) | GPT-6.1 Sol (xhigh), GPT-6.1 Sol (max), GPT-6 Sol (max), Claude Sonnet 5.5 (high) |
| Claude Haiku 5.5 (xhigh) | certified | disproved | GPT-6 Luna (max) | — |
| Claude Sonnet 5.5 (medium) | certified | disproved | GPT-6.1 Sol (high) | — |
| Claude Opus 5 (max) | certified | disproved | Gemini 4 Argon (high) | — |
| GLM-5.3 (max) | disproved | disproved | GPT-6.1 Sol (xhigh) | GPT-6.1 Sol (max), Muse Spark 1.3 (max), Claude Sonnet 5.5 (xhigh), GPT-6 Sol (max) |
| Claude Haiku 5.5 (high) | certified | disproved | GPT-6 Luna (max) | — |
| Claude Haiku 5.5 (medium) | certified | disproved | Claude Haiku 5.5 (low) | — |
| DeepSeek V4 Flash (max) | certified | disproved | GPT-6 Luna (max) | — |
| Claude Haiku 5.5 (low) | certified | certified | — | — |
| Claude Sonnet 5.5 (low) | certified | disproved | GPT-6.1 Sol (medium) | — |
| Qwen3.8 Max | disproved | disproved | Gemini 4 Argon (high) | Gemini 4 Argon (high), GPT-6.1 Sol (xhigh), GPT-6.1 Sol (max), GPT-6.1 Sol (high), GPT-6.1 Sol (medium), GPT-5.6 Sol (max), Muse Spark 1.3 (max), Claude Sonnet 5.5 (xhigh), Muse Spark 1.3 (xhigh), GPT-6 Sol (max), Claude Sonnet 5.5 (high), GPT-6 Luna (max), Gemini 3.8 Flash (high), GLM-5.3 (max) |
| DeepSeek V4 Pro (max) | certified | disproved | GPT-6.1 Sol (high) | — |

**API basis, main workload: cheapest at or above quality 56.7** (lower-median displayed quality of the non-provisional cohort configurations at freeze (E192; headline bar)). Status certified; confirmed cheapest: none.

Configurations that can be confirmed to qualify: 5 (confirmation needs the full-composite lower bound, with missing leaves at 0, to clear the bar; O25). Cheaper same-family configurations on AA's chart that were not evaluated (not ranked: no exact DeepSWE and Bug Hunt pair; E201, O33): DeepSeek V4 Flash (max): DeepSeek V4 Flash (high).

Bar comparison: compares 21 configurations that can qualify. The bar is a displayed-quality level; qualification tests each row's full-composite bounds, so a row above the bar on displayed quality can still fail to qualify confirmed when leaves are missing (E198).

| Configuration | Displayed quality − bar | Confirmed qualifies | Possibly qualifies | Possibly cheapest |
|---|---:|---|---|---|
| Gemini 4 Argon (high) | 8.6 | certified | certified | disproved |
| GPT-6.1 Sol (xhigh) | 7.3 | disproved | certified | certified |
| Claude Sonnet 5.5 (max) | 7.6 | certified | certified | disproved |
| GPT-6.1 Sol (max) | 4.6 | certified | certified | certified |
| GPT-6.1 Sol (high) | 5.3 | disproved | certified | certified |
| Muse Wonder (max) | 7.7 | disproved | certified | disproved |
| GPT-6.1 Sol (medium) | 4.2 | disproved | certified | certified |
| Claude Opus 5.5 (max) | 7.5 | certified | certified | disproved |
| GPT-6 Astra (max) | 4.2 | certified | certified | disproved |
| GPT-5.6 Sol (max) | 3.0 | disproved | certified | disproved |
| Muse Spark 1.3 (max) | 2.1 | disproved | certified | disproved |
| Claude Sonnet 5.5 (xhigh) | 3.0 | disproved | certified | disproved |
| Muse Spark 1.3 (xhigh) | -2.1 | disproved | certified | disproved |
| GPT-6 Sol (max) | 1.6 | disproved | certified | disproved |
| Grok 4.7 (xhigh) | 0.0 | disproved | certified | disproved |
| Claude Sonnet 5.5 (high) | -0.1 | disproved | certified | certified |
| GPT-6.1 Sol (low) | -0.5 | disproved | certified | certified |
| GPT-5.6 Luna (max) | -6.7 | disproved | disproved | disproved |
| Grok 4.6 (xhigh) | 2.2 | disproved | certified | disproved |
| GPT-6 Luna (max) | -9.0 | disproved | disproved | disproved |
| Claude Haiku 5.5 (max) | -11.4 | disproved | disproved | disproved |
| Gemini 3.8 Flash (high) | -6.4 | disproved | disproved | disproved |
| Claude Haiku 5.5 (xhigh) | -11.3 | disproved | disproved | disproved |
| Claude Sonnet 5.5 (medium) | -5.5 | disproved | disproved | disproved |
| Claude Opus 5 (max) | 1.1 | disproved | certified | disproved |
| GLM-5.3 (max) | -4.6 | disproved | disproved | disproved |
| Claude Haiku 5.5 (high) | -13.8 | disproved | disproved | disproved |
| Claude Haiku 5.5 (medium) | -15.8 | disproved | disproved | disproved |
| DeepSeek V4 Flash (max) | -8.6 | disproved | certified | certified |
| Claude Haiku 5.5 (low) | -19.8 | disproved | disproved | disproved |
| Claude Sonnet 5.5 (low) | -9.2 | disproved | disproved | disproved |
| Qwen3.8 Max | -9.0 | disproved | disproved | disproved |
| DeepSeek V4 Pro (max) | -6.7 | disproved | certified | certified |

**API basis, main workload: cheapest at or above quality 48.1** (lower-quartile displayed quality of the non-provisional cohort configurations at freeze (O34)). Status certified; confirmed cheapest: none.

Configurations that can be confirmed to qualify: 18 (confirmation needs the full-composite lower bound, with missing leaves at 0, to clear the bar; O25). Cheaper same-family configurations on AA's chart that were not evaluated (not ranked: no exact DeepSWE and Bug Hunt pair; E201, O33): GPT-5.6 Luna (max): GPT-5.6 Luna (xhigh), GPT-5.6 Luna (high), GPT-5.6 Luna (medium), GPT-5.6 Luna (low), GPT-5.6 Luna (non-reasoning); DeepSeek V4 Flash (max): DeepSeek V4 Flash (high).

Bar comparison: compares 29 configurations that can qualify. The bar is a displayed-quality level; qualification tests each row's full-composite bounds, so a row above the bar on displayed quality can still fail to qualify confirmed when leaves are missing (E198).

| Configuration | Displayed quality − bar | Confirmed qualifies | Possibly qualifies | Possibly cheapest |
|---|---:|---|---|---|
| Gemini 4 Argon (high) | 17.2 | certified | certified | disproved |
| GPT-6.1 Sol (xhigh) | 16.0 | certified | certified | disproved |
| Claude Sonnet 5.5 (max) | 16.3 | certified | certified | disproved |
| GPT-6.1 Sol (max) | 13.3 | certified | certified | disproved |
| GPT-6.1 Sol (high) | 13.9 | certified | certified | disproved |
| Muse Wonder (max) | 16.4 | certified | certified | disproved |
| GPT-6.1 Sol (medium) | 12.8 | certified | certified | certified |
| Claude Opus 5.5 (max) | 16.1 | certified | certified | disproved |
| GPT-6 Astra (max) | 12.8 | certified | certified | disproved |
| GPT-5.6 Sol (max) | 11.6 | certified | certified | disproved |
| Muse Spark 1.3 (max) | 10.8 | certified | certified | disproved |
| Claude Sonnet 5.5 (xhigh) | 11.6 | certified | certified | disproved |
| Muse Spark 1.3 (xhigh) | 6.6 | certified | certified | disproved |
| GPT-6 Sol (max) | 10.2 | certified | certified | disproved |
| Grok 4.7 (xhigh) | 8.6 | certified | certified | disproved |
| Claude Sonnet 5.5 (high) | 8.5 | certified | certified | disproved |
| GPT-6.1 Sol (low) | 8.1 | disproved | certified | certified |
| GPT-5.6 Luna (max) | 2.0 | disproved | certified | certified |
| Grok 4.6 (xhigh) | 10.8 | disproved | certified | disproved |
| GPT-6 Luna (max) | -0.3 | disproved | disproved | disproved |
| Claude Haiku 5.5 (max) | -2.7 | disproved | certified | disproved |
| Gemini 3.8 Flash (high) | 2.2 | certified | certified | disproved |
| Claude Haiku 5.5 (xhigh) | -2.7 | disproved | certified | certified |
| Claude Sonnet 5.5 (medium) | 3.1 | disproved | certified | disproved |
| Claude Opus 5 (max) | 9.7 | disproved | certified | disproved |
| GLM-5.3 (max) | 4.0 | certified | certified | disproved |
| Claude Haiku 5.5 (high) | -5.1 | disproved | certified | certified |
| Claude Haiku 5.5 (medium) | -7.1 | disproved | disproved | disproved |
| DeepSeek V4 Flash (max) | 0.0 | disproved | certified | certified |
| Claude Haiku 5.5 (low) | -11.2 | disproved | disproved | disproved |
| Claude Sonnet 5.5 (low) | -0.6 | disproved | certified | disproved |
| Qwen3.8 Max | -0.4 | disproved | disproved | disproved |
| DeepSeek V4 Pro (max) | 1.9 | disproved | certified | disproved |

**API basis, main workload: cheapest at or above quality 60.9** (upper-quartile displayed quality of the non-provisional cohort configurations at freeze (O34)). Status certified; confirmed cheapest: none.

Configurations that can be confirmed to qualify: 3 (confirmation needs the full-composite lower bound, with missing leaves at 0, to clear the bar; O25). Cheaper same-family configurations on AA's chart that were not evaluated (not ranked: no exact DeepSWE and Bug Hunt pair; E201, O33): none.

Bar comparison: compares 17 configurations that can qualify. The bar is a displayed-quality level; qualification tests each row's full-composite bounds, so a row above the bar on displayed quality can still fail to qualify confirmed when leaves are missing (E198).

| Configuration | Displayed quality − bar | Confirmed qualifies | Possibly qualifies | Possibly cheapest |
|---|---:|---|---|---|
| Gemini 4 Argon (high) | 4.4 | disproved | certified | disproved |
| GPT-6.1 Sol (xhigh) | 3.2 | disproved | certified | certified |
| Claude Sonnet 5.5 (max) | 3.4 | certified | certified | disproved |
| GPT-6.1 Sol (max) | 0.4 | certified | certified | certified |
| GPT-6.1 Sol (high) | 1.1 | disproved | certified | certified |
| Muse Wonder (max) | 3.5 | disproved | certified | disproved |
| GPT-6.1 Sol (medium) | 0.0 | disproved | certified | certified |
| Claude Opus 5.5 (max) | 3.3 | certified | certified | disproved |
| GPT-6 Astra (max) | 0.0 | disproved | certified | disproved |
| GPT-5.6 Sol (max) | -1.2 | disproved | certified | disproved |
| Muse Spark 1.3 (max) | -2.1 | disproved | certified | disproved |
| Claude Sonnet 5.5 (xhigh) | -1.2 | disproved | certified | disproved |
| Muse Spark 1.3 (xhigh) | -6.2 | disproved | disproved | disproved |
| GPT-6 Sol (max) | -2.6 | disproved | certified | disproved |
| Grok 4.7 (xhigh) | -4.2 | disproved | disproved | disproved |
| Claude Sonnet 5.5 (high) | -4.3 | disproved | certified | certified |
| GPT-6.1 Sol (low) | -4.7 | disproved | certified | certified |
| GPT-5.6 Luna (max) | -10.9 | disproved | disproved | disproved |
| Grok 4.6 (xhigh) | -2.0 | disproved | certified | disproved |
| GPT-6 Luna (max) | -13.1 | disproved | disproved | disproved |
| Claude Haiku 5.5 (max) | -15.6 | disproved | disproved | disproved |
| Gemini 3.8 Flash (high) | -10.6 | disproved | disproved | disproved |
| Claude Haiku 5.5 (xhigh) | -15.5 | disproved | disproved | disproved |
| Claude Sonnet 5.5 (medium) | -9.7 | disproved | disproved | disproved |
| Claude Opus 5 (max) | -3.1 | disproved | certified | disproved |
| GLM-5.3 (max) | -8.8 | disproved | disproved | disproved |
| Claude Haiku 5.5 (high) | -18.0 | disproved | disproved | disproved |
| Claude Haiku 5.5 (medium) | -19.9 | disproved | disproved | disproved |
| DeepSeek V4 Flash (max) | -12.8 | disproved | disproved | disproved |
| Claude Haiku 5.5 (low) | -24.0 | disproved | disproved | disproved |
| Claude Sonnet 5.5 (low) | -13.4 | disproved | disproved | disproved |
| Qwen3.8 Max | -13.2 | disproved | disproved | disproved |
| DeepSeek V4 Pro (max) | -10.9 | disproved | disproved | disproved |

**Plan basis, main workload:** not evaluated (no row has FullCost and an identified M_W (E61/E67)).

**API basis, subset workload (AA-Briefcase, GDPval-AA, GDP.pdf, AutomationBench-AA, Terminal-Bench 4.0 (AA Index run), SciCode, AA-LCR; orderings across workloads not identified): frontier.** Not evaluable: Claude Fable 5.1 (max), Muse Wonder Full (max).

| Configuration | Possible frontier | Definite frontier | Definite counterexample | Possible frontier blocked by |
|---|---|---|---|---|
| Gemini 4 Argon (high) | certified | disproved | GPT-6.1 Sol (xhigh) | — |
| GPT-6.1 Sol (xhigh) | certified | disproved | GPT-6.1 Sol (high) | — |
| Claude Sonnet 5.5 (max) | certified | disproved | Gemini 4 Argon (high) | — |
| GPT-6.1 Sol (max) | certified | disproved | GPT-6.1 Sol (xhigh) | — |
| GPT-6.1 Sol (high) | certified | disproved | GPT-6.1 Sol (medium) | — |
| Muse Wonder (max) | certified | disproved | Gemini 4 Argon (high) | — |
| GPT-6.1 Sol (medium) | certified | disproved | MiMo-V2.6-Pro | — |
| Claude Opus 5.5 (max) | disproved | disproved | Gemini 4 Argon (high) | Claude Sonnet 5.5 (max) |
| GPT-6 Astra (max) | disproved | disproved | Gemini 4 Argon (high) | GPT-6.1 Sol (max) |
| GPT-5.6 Sol (max) | certified | disproved | Gemini 4 Argon (high) | — |
| Muse Spark 1.3 (max) | certified | disproved | GPT-6.1 Sol (xhigh) | — |
| Claude Sonnet 5.5 (xhigh) | certified | disproved | GPT-6.1 Sol (xhigh) | — |
| Muse Spark 1.3 (xhigh) | disproved | disproved | GPT-6.1 Sol (xhigh) | GPT-6.1 Sol (max) |
| GPT-6 Sol (max) | certified | disproved | GPT-6.1 Sol (xhigh) | — |
| Grok 4.7 (xhigh) | disproved | disproved | Gemini 4 Argon (high) | Gemini 4 Argon (high), GPT-6.1 Sol (max), GPT-6 Astra (max) |
| MiMo-V2.6-Pro | certified | disproved | GPT-6 Luna (max) | — |
| Claude Sonnet 5.5 (high) | disproved | disproved | GPT-6.1 Sol (xhigh) | GPT-6.1 Sol (max) |
| GPT-6.1 Sol (low) | certified | disproved | MiMo-V2.6-Pro | — |
| GPT-5.6 Luna (max) | certified | disproved | MiMo-V2.6-Pro | — |
| Grok 4.6 (xhigh) | certified | disproved | Gemini 4 Argon (high) | — |
| GPT-6 Luna (max) | certified | disproved | MiMo-V2.6-Flash | — |
| Claude Haiku 5.5 (max) | certified | disproved | MiMo-V2.6-Pro | — |
| Gemini 3.8 Flash (high) | disproved | disproved | GPT-6.1 Sol (xhigh) | GPT-6.1 Sol (xhigh), GPT-6.1 Sol (max), GPT-6 Sol (max), Claude Sonnet 5.5 (high) |
| Claude Haiku 5.5 (xhigh) | certified | disproved | GPT-6 Luna (max) | — |
| MiMo-V2.6-Flash | certified | disproved | Claude Haiku 5.5 (medium) | — |
| Claude Sonnet 5.5 (medium) | certified | disproved | GPT-6.1 Sol (xhigh) | — |
| Claude Opus 5 (max) | certified | disproved | Gemini 4 Argon (high) | — |
| GLM-5.3 (max) | disproved | disproved | Gemini 4 Argon (high) | Gemini 4 Argon (high), GPT-6.1 Sol (max), Muse Spark 1.3 (max), Claude Sonnet 5.5 (xhigh), GPT-6 Sol (max) |
| Claude Haiku 5.5 (high) | certified | disproved | MiMo-V2.6-Flash | — |
| Claude Haiku 5.5 (medium) | certified | disproved | Claude Haiku 5.5 (low) | — |
| DeepSeek V4 Flash (max) | certified | disproved | MiMo-V2.6-Pro | — |
| Claude Haiku 5.5 (low) | certified | certified | — | — |
| Claude Sonnet 5.5 (low) | certified | disproved | GPT-6.1 Sol (high) | — |
| Qwen3.8 Max | disproved | disproved | Gemini 4 Argon (high) | Gemini 4 Argon (high), GPT-6.1 Sol (xhigh), GPT-6.1 Sol (max), GPT-6.1 Sol (high), Muse Wonder (max), GPT-6.1 Sol (medium), GPT-6 Astra (max), GPT-5.6 Sol (max), Muse Spark 1.3 (max), Claude Sonnet 5.5 (xhigh), Muse Spark 1.3 (xhigh), GPT-6 Sol (max), Grok 4.7 (xhigh), Claude Sonnet 5.5 (high), GPT-6 Luna (max), Gemini 3.8 Flash (high), GLM-5.3 (max) |
| DeepSeek V4 Pro (max) | certified | disproved | GPT-6.1 Sol (xhigh) | — |

**API basis, subset workload (AA-Briefcase, GDPval-AA, GDP.pdf, AutomationBench-AA, Terminal-Bench 4.0 (AA Index run), SciCode, AA-LCR; orderings across workloads not identified): cheapest at or above quality 56.7** (lower-median displayed quality of the non-provisional cohort configurations at freeze (E192; headline bar)). Status certified; confirmed cheapest: none.

Configurations that can be confirmed to qualify: 5 (confirmation needs the full-composite lower bound, with missing leaves at 0, to clear the bar; O25). Cheaper same-family configurations on AA's chart that were not evaluated (not ranked: no exact DeepSWE and Bug Hunt pair; E201, O33): DeepSeek V4 Flash (max): DeepSeek V4 Flash (high).

Bar comparison: compares 23 configurations that can qualify. The bar is a displayed-quality level; qualification tests each row's full-composite bounds, so a row above the bar on displayed quality can still fail to qualify confirmed when leaves are missing (E198).

| Configuration | Displayed quality − bar | Confirmed qualifies | Possibly qualifies | Possibly cheapest |
|---|---:|---|---|---|
| Gemini 4 Argon (high) | 8.6 | certified | certified | disproved |
| GPT-6.1 Sol (xhigh) | 7.3 | disproved | certified | certified |
| Claude Sonnet 5.5 (max) | 7.6 | certified | certified | disproved |
| GPT-6.1 Sol (max) | 4.6 | certified | certified | certified |
| GPT-6.1 Sol (high) | 5.3 | disproved | certified | certified |
| Muse Wonder (max) | 7.7 | disproved | certified | disproved |
| GPT-6.1 Sol (medium) | 4.2 | disproved | certified | certified |
| Claude Opus 5.5 (max) | 7.5 | certified | certified | disproved |
| GPT-6 Astra (max) | 4.2 | certified | certified | disproved |
| GPT-5.6 Sol (max) | 3.0 | disproved | certified | disproved |
| Muse Spark 1.3 (max) | 2.1 | disproved | certified | disproved |
| Claude Sonnet 5.5 (xhigh) | 3.0 | disproved | certified | disproved |
| Muse Spark 1.3 (xhigh) | -2.1 | disproved | certified | disproved |
| GPT-6 Sol (max) | 1.6 | disproved | certified | disproved |
| Grok 4.7 (xhigh) | 0.0 | disproved | certified | disproved |
| MiMo-V2.6-Pro | -6.6 | disproved | certified | certified |
| Claude Sonnet 5.5 (high) | -0.1 | disproved | certified | disproved |
| GPT-6.1 Sol (low) | -0.5 | disproved | certified | certified |
| GPT-5.6 Luna (max) | -6.7 | disproved | disproved | disproved |
| Grok 4.6 (xhigh) | 2.2 | disproved | certified | disproved |
| GPT-6 Luna (max) | -9.0 | disproved | disproved | disproved |
| Claude Haiku 5.5 (max) | -11.4 | disproved | disproved | disproved |
| Gemini 3.8 Flash (high) | -6.4 | disproved | disproved | disproved |
| Claude Haiku 5.5 (xhigh) | -11.3 | disproved | disproved | disproved |
| MiMo-V2.6-Flash | -5.0 | disproved | certified | certified |
| Claude Sonnet 5.5 (medium) | -5.5 | disproved | disproved | disproved |
| Claude Opus 5 (max) | 1.1 | disproved | certified | disproved |
| GLM-5.3 (max) | -4.6 | disproved | disproved | disproved |
| Claude Haiku 5.5 (high) | -13.8 | disproved | disproved | disproved |
| Claude Haiku 5.5 (medium) | -15.8 | disproved | disproved | disproved |
| DeepSeek V4 Flash (max) | -8.6 | disproved | certified | certified |
| Claude Haiku 5.5 (low) | -19.8 | disproved | disproved | disproved |
| Claude Sonnet 5.5 (low) | -9.2 | disproved | disproved | disproved |
| Qwen3.8 Max | -9.0 | disproved | disproved | disproved |
| DeepSeek V4 Pro (max) | -6.7 | disproved | certified | certified |

**API basis, subset workload (AA-Briefcase, GDPval-AA, GDP.pdf, AutomationBench-AA, Terminal-Bench 4.0 (AA Index run), SciCode, AA-LCR; orderings across workloads not identified): cheapest at or above quality 48.1** (lower-quartile displayed quality of the non-provisional cohort configurations at freeze (O34)). Status certified; confirmed cheapest: none.

Configurations that can be confirmed to qualify: 18 (confirmation needs the full-composite lower bound, with missing leaves at 0, to clear the bar; O25). Cheaper same-family configurations on AA's chart that were not evaluated (not ranked: no exact DeepSWE and Bug Hunt pair; E201, O33): GPT-5.6 Luna (max): GPT-5.6 Luna (xhigh), GPT-5.6 Luna (high), GPT-5.6 Luna (medium), GPT-5.6 Luna (low), GPT-5.6 Luna (non-reasoning); DeepSeek V4 Flash (max): DeepSeek V4 Flash (high).

Bar comparison: compares 31 configurations that can qualify. The bar is a displayed-quality level; qualification tests each row's full-composite bounds, so a row above the bar on displayed quality can still fail to qualify confirmed when leaves are missing (E198).

| Configuration | Displayed quality − bar | Confirmed qualifies | Possibly qualifies | Possibly cheapest |
|---|---:|---|---|---|
| Gemini 4 Argon (high) | 17.2 | certified | certified | disproved |
| GPT-6.1 Sol (xhigh) | 16.0 | certified | certified | disproved |
| Claude Sonnet 5.5 (max) | 16.3 | certified | certified | disproved |
| GPT-6.1 Sol (max) | 13.3 | certified | certified | disproved |
| GPT-6.1 Sol (high) | 13.9 | certified | certified | disproved |
| Muse Wonder (max) | 16.4 | certified | certified | disproved |
| GPT-6.1 Sol (medium) | 12.8 | certified | certified | certified |
| Claude Opus 5.5 (max) | 16.1 | certified | certified | disproved |
| GPT-6 Astra (max) | 12.8 | certified | certified | disproved |
| GPT-5.6 Sol (max) | 11.6 | certified | certified | disproved |
| Muse Spark 1.3 (max) | 10.8 | certified | certified | disproved |
| Claude Sonnet 5.5 (xhigh) | 11.6 | certified | certified | disproved |
| Muse Spark 1.3 (xhigh) | 6.6 | certified | certified | disproved |
| GPT-6 Sol (max) | 10.2 | certified | certified | disproved |
| Grok 4.7 (xhigh) | 8.6 | certified | certified | disproved |
| MiMo-V2.6-Pro | 2.0 | disproved | certified | certified |
| Claude Sonnet 5.5 (high) | 8.5 | certified | certified | disproved |
| GPT-6.1 Sol (low) | 8.1 | disproved | certified | certified |
| GPT-5.6 Luna (max) | 2.0 | disproved | certified | certified |
| Grok 4.6 (xhigh) | 10.8 | disproved | certified | disproved |
| GPT-6 Luna (max) | -0.3 | disproved | disproved | disproved |
| Claude Haiku 5.5 (max) | -2.7 | disproved | certified | certified |
| Gemini 3.8 Flash (high) | 2.2 | certified | certified | disproved |
| Claude Haiku 5.5 (xhigh) | -2.7 | disproved | certified | certified |
| MiMo-V2.6-Flash | 3.7 | disproved | certified | certified |
| Claude Sonnet 5.5 (medium) | 3.1 | disproved | certified | disproved |
| Claude Opus 5 (max) | 9.7 | disproved | certified | disproved |
| GLM-5.3 (max) | 4.0 | certified | certified | disproved |
| Claude Haiku 5.5 (high) | -5.1 | disproved | certified | certified |
| Claude Haiku 5.5 (medium) | -7.1 | disproved | disproved | disproved |
| DeepSeek V4 Flash (max) | 0.0 | disproved | certified | certified |
| Claude Haiku 5.5 (low) | -11.2 | disproved | disproved | disproved |
| Claude Sonnet 5.5 (low) | -0.6 | disproved | certified | disproved |
| Qwen3.8 Max | -0.4 | disproved | disproved | disproved |
| DeepSeek V4 Pro (max) | 1.9 | disproved | certified | disproved |

**API basis, subset workload (AA-Briefcase, GDPval-AA, GDP.pdf, AutomationBench-AA, Terminal-Bench 4.0 (AA Index run), SciCode, AA-LCR; orderings across workloads not identified): cheapest at or above quality 60.9** (upper-quartile displayed quality of the non-provisional cohort configurations at freeze (O34)). Status certified; confirmed cheapest: none.

Configurations that can be confirmed to qualify: 3 (confirmation needs the full-composite lower bound, with missing leaves at 0, to clear the bar; O25). Cheaper same-family configurations on AA's chart that were not evaluated (not ranked: no exact DeepSWE and Bug Hunt pair; E201, O33): none.

Bar comparison: compares 19 configurations that can qualify. The bar is a displayed-quality level; qualification tests each row's full-composite bounds, so a row above the bar on displayed quality can still fail to qualify confirmed when leaves are missing (E198).

| Configuration | Displayed quality − bar | Confirmed qualifies | Possibly qualifies | Possibly cheapest |
|---|---:|---|---|---|
| Gemini 4 Argon (high) | 4.4 | disproved | certified | disproved |
| GPT-6.1 Sol (xhigh) | 3.2 | disproved | certified | certified |
| Claude Sonnet 5.5 (max) | 3.4 | certified | certified | disproved |
| GPT-6.1 Sol (max) | 0.4 | certified | certified | certified |
| GPT-6.1 Sol (high) | 1.1 | disproved | certified | certified |
| Muse Wonder (max) | 3.5 | disproved | certified | disproved |
| GPT-6.1 Sol (medium) | 0.0 | disproved | certified | certified |
| Claude Opus 5.5 (max) | 3.3 | certified | certified | disproved |
| GPT-6 Astra (max) | 0.0 | disproved | certified | disproved |
| GPT-5.6 Sol (max) | -1.2 | disproved | certified | disproved |
| Muse Spark 1.3 (max) | -2.1 | disproved | certified | disproved |
| Claude Sonnet 5.5 (xhigh) | -1.2 | disproved | certified | disproved |
| Muse Spark 1.3 (xhigh) | -6.2 | disproved | disproved | disproved |
| GPT-6 Sol (max) | -2.6 | disproved | certified | disproved |
| Grok 4.7 (xhigh) | -4.2 | disproved | disproved | disproved |
| MiMo-V2.6-Pro | -10.8 | disproved | certified | certified |
| Claude Sonnet 5.5 (high) | -4.3 | disproved | certified | disproved |
| GPT-6.1 Sol (low) | -4.7 | disproved | certified | certified |
| GPT-5.6 Luna (max) | -10.9 | disproved | disproved | disproved |
| Grok 4.6 (xhigh) | -2.0 | disproved | certified | disproved |
| GPT-6 Luna (max) | -13.1 | disproved | disproved | disproved |
| Claude Haiku 5.5 (max) | -15.6 | disproved | disproved | disproved |
| Gemini 3.8 Flash (high) | -10.6 | disproved | disproved | disproved |
| Claude Haiku 5.5 (xhigh) | -15.5 | disproved | disproved | disproved |
| MiMo-V2.6-Flash | -9.1 | disproved | certified | certified |
| Claude Sonnet 5.5 (medium) | -9.7 | disproved | disproved | disproved |
| Claude Opus 5 (max) | -3.1 | disproved | certified | disproved |
| GLM-5.3 (max) | -8.8 | disproved | disproved | disproved |
| Claude Haiku 5.5 (high) | -18.0 | disproved | disproved | disproved |
| Claude Haiku 5.5 (medium) | -19.9 | disproved | disproved | disproved |
| DeepSeek V4 Flash (max) | -12.8 | disproved | disproved | disproved |
| Claude Haiku 5.5 (low) | -24.0 | disproved | disproved | disproved |
| Claude Sonnet 5.5 (low) | -13.4 | disproved | disproved | disproved |
| Qwen3.8 Max | -13.2 | disproved | disproved | disproved |
| DeepSeek V4 Pro (max) | -10.9 | disproved | disproved | disproved |

**Plan basis, subset workload (AA-Briefcase, GDPval-AA, GDP.pdf, AutomationBench-AA, Terminal-Bench 4.0 (AA Index run), SciCode, AA-LCR; orderings across workloads not identified):** not evaluated (unevaluable: no Plan multiple is identified for a subset workload (E149, E190)).

## Scenario shares

Frequencies over 10,000 scenarios per run (seed 20261021); streams are defined in [methodology.md](methodology.md#uncertainty-outputs). The shares exclude benchmark sampling noise beyond S1M and fitted-rating uncertainty (E155).

### API basis: rank 1

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M |
|---|---:|---:|---:|---:|---:|
| Claude Fable 5.1 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Haiku 5.5 (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Haiku 5.5 (low) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Haiku 5.5 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Haiku 5.5 (medium) | 0.0% | 0.0% | 0.1% | 0.0% | 0.0% |
| Claude Haiku 5.5 (xhigh) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Sonnet 5.5 (high) | 0.0% | 0.0% | 0.1% | 0.0% | 0.0% |
| Claude Sonnet 5.5 (low) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Sonnet 5.5 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Sonnet 5.5 (medium) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Sonnet 5.5 (xhigh) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| DeepSeek V4 Flash (max) | 0.0% | 1.5% | 1.4% | 2.5% | 1.1% |
| DeepSeek V4 Pro (max) | 0.0% | 0.0% | 0.1% | 0.1% | 0.0% |
| GLM-5.3 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-5.6 Luna (max) | 0.0% | 0.2% | 0.7% | 0.5% | 0.2% |
| GPT-5.6 Sol (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Luna (max) | 0.0% | 0.0% | 0.1% | 0.0% | 0.0% |
| GPT-6 Sol (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (high) | 0.0% | 23.4% | 23.2% | 23.3% | 24.8% |
| GPT-6.1 Sol (low) | 0.0% | 14.8% | 14.3% | 15.0% | 14.1% |
| GPT-6.1 Sol (max) | 0.0% | 1.1% | 1.1% | 1.0% | 1.1% |
| GPT-6.1 Sol (medium) | 0.0% | 28.6% | 27.8% | 27.2% | 27.8% |
| GPT-6.1 Sol (xhigh) | 100.0% | 29.8% | 30.0% | 28.9% | 30.1% |
| Gemini 3.8 Flash (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Gemini 4 Argon (high) | 0.0% | 0.6% | 0.9% | 1.3% | 0.8% |
| Grok 4.6 (xhigh) | 0.0% | 0.0% | 0.0% | 0.1% | 0.0% |
| Grok 4.7 (xhigh) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Muse Spark 1.3 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Muse Spark 1.3 (xhigh) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Muse Wonder (max) | 0.0% | 0.0% | 0.1% | 0.2% | 0.0% |
| Qwen3.8 Max | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |

### API basis: rank 3 or better

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M |
|---|---:|---:|---:|---:|---:|
| Claude Fable 5.1 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Haiku 5.5 (high) | 0.0% | 0.0% | 0.5% | 0.0% | 0.0% |
| Claude Haiku 5.5 (low) | 0.0% | 0.0% | 0.4% | 0.0% | 0.0% |
| Claude Haiku 5.5 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Haiku 5.5 (medium) | 0.0% | 0.0% | 0.9% | 0.0% | 0.0% |
| Claude Haiku 5.5 (xhigh) | 0.0% | 0.0% | 0.2% | 0.0% | 0.0% |
| Claude Opus 5 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Sonnet 5.5 (high) | 0.0% | 0.5% | 2.0% | 1.2% | 0.6% |
| Claude Sonnet 5.5 (low) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Sonnet 5.5 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Sonnet 5.5 (medium) | 0.0% | 0.0% | 0.4% | 0.0% | 0.0% |
| Claude Sonnet 5.5 (xhigh) | 0.0% | 0.0% | 0.3% | 0.0% | 0.0% |
| DeepSeek V4 Flash (max) | 0.0% | 9.6% | 9.1% | 13.9% | 9.4% |
| DeepSeek V4 Pro (max) | 0.0% | 0.4% | 1.2% | 1.6% | 0.3% |
| GLM-5.3 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-5.6 Luna (max) | 0.0% | 5.3% | 7.4% | 9.4% | 5.4% |
| GPT-5.6 Sol (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Luna (max) | 0.0% | 1.3% | 3.6% | 1.1% | 1.0% |
| GPT-6 Sol (max) | 0.0% | 0.1% | 0.8% | 0.3% | 0.1% |
| GPT-6.1 Sol (high) | 100.0% | 58.4% | 58.1% | 56.4% | 60.3% |
| GPT-6.1 Sol (low) | 0.0% | 45.5% | 44.0% | 43.9% | 45.2% |
| GPT-6.1 Sol (max) | 0.0% | 35.3% | 31.3% | 28.0% | 34.9% |
| GPT-6.1 Sol (medium) | 100.0% | 64.4% | 62.0% | 60.9% | 63.7% |
| GPT-6.1 Sol (xhigh) | 100.0% | 65.8% | 64.8% | 61.7% | 65.7% |
| Gemini 3.8 Flash (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Gemini 4 Argon (high) | 0.0% | 12.2% | 10.6% | 17.0% | 12.0% |
| Grok 4.6 (xhigh) | 0.0% | 0.5% | 1.0% | 2.1% | 0.6% |
| Grok 4.7 (xhigh) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Muse Spark 1.3 (max) | 0.0% | 0.0% | 0.1% | 0.0% | 0.0% |
| Muse Spark 1.3 (xhigh) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Muse Wonder (max) | 0.0% | 0.8% | 1.2% | 2.6% | 0.8% |
| Qwen3.8 Max | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |

### API basis: on the frontier

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M |
|---|---:|---:|---:|---:|---:|
| Claude Fable 5.1 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Haiku 5.5 (high) | 0.0% | 8.7% | 12.1% | 19.3% | 9.2% |
| Claude Haiku 5.5 (low) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% |
| Claude Haiku 5.5 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Haiku 5.5 (medium) | 100.0% | 80.5% | 81.7% | 75.8% | 79.5% |
| Claude Haiku 5.5 (xhigh) | 0.0% | 17.7% | 14.4% | 21.9% | 17.7% |
| Claude Opus 5 (max) | 0.0% | 1.2% | 1.5% | 2.3% | 1.4% |
| Claude Opus 5.5 (max) | 0.0% | 0.0% | 7.7% | 0.0% | 7.2% |
| Claude Sonnet 5.5 (high) | 0.0% | 2.9% | 3.4% | 4.0% | 2.7% |
| Claude Sonnet 5.5 (low) | 0.0% | 0.2% | 0.5% | 0.6% | 0.1% |
| Claude Sonnet 5.5 (max) | 0.0% | 23.4% | 22.1% | 15.5% | 23.2% |
| Claude Sonnet 5.5 (medium) | 0.0% | 0.3% | 0.8% | 0.9% | 0.4% |
| Claude Sonnet 5.5 (xhigh) | 0.0% | 8.6% | 7.3% | 10.5% | 8.4% |
| DeepSeek V4 Flash (max) | 100.0% | 57.3% | 51.2% | 57.1% | 56.3% |
| DeepSeek V4 Pro (max) | 0.0% | 0.9% | 1.2% | 2.0% | 0.7% |
| GLM-5.3 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-5.6 Luna (max) | 100.0% | 50.3% | 49.9% | 44.5% | 50.2% |
| GPT-5.6 Sol (max) | 0.0% | 2.7% | 3.3% | 3.4% | 2.7% |
| GPT-6 Astra (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.1% |
| GPT-6 Luna (max) | 100.0% | 100.0% | 93.7% | 100.0% | 100.0% |
| GPT-6 Sol (max) | 0.0% | 3.2% | 3.8% | 5.8% | 3.5% |
| GPT-6.1 Sol (high) | 100.0% | 48.8% | 49.7% | 47.1% | 50.6% |
| GPT-6.1 Sol (low) | 100.0% | 75.8% | 73.5% | 67.5% | 75.2% |
| GPT-6.1 Sol (max) | 0.0% | 23.1% | 21.6% | 20.7% | 23.0% |
| GPT-6.1 Sol (medium) | 100.0% | 71.4% | 70.2% | 65.4% | 72.1% |
| GPT-6.1 Sol (xhigh) | 100.0% | 45.6% | 45.6% | 41.5% | 45.4% |
| Gemini 3.8 Flash (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Gemini 4 Argon (high) | 100.0% | 45.5% | 46.1% | 37.7% | 45.8% |
| Grok 4.6 (xhigh) | 0.0% | 7.1% | 6.4% | 9.3% | 7.2% |
| Grok 4.7 (xhigh) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Muse Spark 1.3 (max) | 0.0% | 5.1% | 4.5% | 7.4% | 5.0% |
| Muse Spark 1.3 (xhigh) | 0.0% | 0.0% | 0.3% | 0.0% | 0.0% |
| Muse Wonder (max) | 0.0% | 20.6% | 20.1% | 20.3% | 20.4% |
| Qwen3.8 Max | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |

### API basis: value-score dispersion (SD; covariance term)

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M |
|---|---:|---:|---:|---:|---:|
| Claude Fable 5.1 (max) | 0.00 (+0.00) | 0.00 (+0.00) | 0.73 (+0.00) | 0.00 (+0.00) | 0.17 (+0.00) |
| Claude Haiku 5.5 (high) | 0.00 (+0.00) | 2.15 (+0.00) | 2.45 (+0.00) | 2.65 (+0.00) | 2.15 (+0.00) |
| Claude Haiku 5.5 (low) | 0.00 (+0.00) | 2.13 (+0.00) | 2.50 (+0.00) | 2.65 (+0.00) | 2.17 (+0.00) |
| Claude Haiku 5.5 (max) | 0.00 (+0.00) | 2.16 (+0.00) | 2.43 (+0.00) | 2.66 (+0.00) | 2.16 (+0.00) |
| Claude Haiku 5.5 (medium) | 0.00 (+0.00) | 2.14 (+0.00) | 2.47 (+0.00) | 2.66 (+0.00) | 2.17 (+0.00) |
| Claude Haiku 5.5 (xhigh) | 0.00 (+0.00) | 2.17 (+0.00) | 2.42 (+0.00) | 2.66 (+0.00) | 2.15 (+0.00) |
| Claude Opus 5 (max) | 0.00 (+0.00) | 3.09 (+0.00) | 3.37 (+0.00) | 3.74 (+0.00) | 3.07 (+0.00) |
| Claude Opus 5.5 (max) | 0.00 (+0.00) | 0.00 (+0.00) | 0.81 (+0.00) | 0.00 (+0.00) | 0.13 (+0.00) |
| Claude Sonnet 5.5 (high) | 0.00 (+0.00) | 2.16 (+0.00) | 2.42 (+0.00) | 2.65 (+0.00) | 2.17 (+0.00) |
| Claude Sonnet 5.5 (low) | 0.00 (+0.00) | 2.17 (+0.00) | 2.57 (+0.00) | 2.64 (+0.00) | 2.18 (+0.00) |
| Claude Sonnet 5.5 (max) | 0.00 (+0.00) | 0.00 (+0.00) | 0.77 (+0.00) | 0.00 (+0.00) | 0.13 (+0.00) |
| Claude Sonnet 5.5 (medium) | 0.00 (+0.00) | 2.18 (+0.00) | 2.57 (+0.00) | 2.65 (+0.00) | 2.16 (+0.00) |
| Claude Sonnet 5.5 (xhigh) | 0.00 (+0.00) | 2.17 (+0.00) | 2.42 (+0.00) | 2.66 (+0.00) | 2.18 (+0.00) |
| DeepSeek V4 Flash (max) | 0.00 (+0.00) | 3.04 (+0.00) | 3.32 (+0.00) | 3.74 (+0.00) | 3.08 (+0.00) |
| DeepSeek V4 Pro (max) | 0.00 (+0.00) | 3.02 (+0.00) | 3.37 (+0.00) | 3.72 (+0.00) | 3.07 (+0.00) |
| GLM-5.3 (max) | 0.00 (+0.00) | 0.00 (+0.00) | 1.14 (+0.00) | 0.00 (+0.00) | 0.14 (+0.00) |
| GPT-5.6 Luna (max) | 0.00 (+0.00) | 2.16 (+0.00) | 2.61 (+0.00) | 2.66 (+0.00) | 2.17 (+0.00) |
| GPT-5.6 Sol (max) | 0.00 (+0.00) | 2.17 (+0.00) | 2.47 (+0.00) | 2.66 (+0.00) | 2.19 (+0.00) |
| GPT-6 Astra (max) | 0.00 (+0.00) | 0.00 (+0.00) | 0.77 (+0.00) | 0.00 (+0.00) | 0.12 (+0.00) |
| GPT-6 Luna (max) | 0.00 (+0.00) | 0.00 (+0.00) | 1.40 (+0.00) | 0.00 (+0.00) | 0.12 (+0.00) |
| GPT-6 Sol (max) | 0.00 (+0.00) | 2.16 (+0.00) | 2.50 (+0.00) | 2.64 (+0.00) | 2.16 (+0.00) |
| GPT-6.1 Sol (high) | 0.00 (+0.00) | 3.08 (+0.00) | 3.36 (+0.00) | 3.75 (+0.00) | 3.06 (+0.00) |
| GPT-6.1 Sol (low) | 0.00 (+0.00) | 3.04 (+0.00) | 3.40 (+0.00) | 3.77 (+0.00) | 3.02 (+0.00) |
| GPT-6.1 Sol (max) | 0.00 (+0.00) | 0.00 (+0.00) | 0.79 (+0.00) | 0.00 (+0.00) | 0.13 (+0.00) |
| GPT-6.1 Sol (medium) | 0.00 (+0.00) | 3.07 (+0.00) | 3.45 (+0.00) | 3.75 (+0.00) | 3.03 (+0.00) |
| GPT-6.1 Sol (xhigh) | 0.00 (+0.00) | 3.06 (+0.00) | 3.35 (+0.00) | 3.76 (+0.00) | 3.06 (+0.00) |
| Gemini 3.8 Flash (high) | 0.00 (+0.00) | 0.00 (+0.00) | 1.51 (+0.00) | 0.00 (+0.00) | 0.15 (+0.00) |
| Gemini 4 Argon (high) | 0.00 (+0.00) | 2.18 (+0.00) | 2.56 (+0.00) | 2.65 (+0.00) | 2.18 (+0.00) |
| Grok 4.6 (xhigh) | 0.00 (+0.00) | 3.09 (+0.00) | 3.37 (+0.00) | 3.74 (+0.00) | 3.06 (+0.00) |
| Grok 4.7 (xhigh) | 0.00 (+0.00) | 0.00 (+0.00) | 1.35 (+0.00) | 0.00 (+0.00) | 0.15 (+0.00) |
| Muse Spark 1.3 (max) | 0.00 (+0.00) | 2.18 (+0.00) | 2.50 (+0.00) | 2.66 (+0.00) | 2.17 (+0.00) |
| Muse Spark 1.3 (xhigh) | 0.00 (+0.00) | 2.17 (+0.00) | 2.79 (+0.00) | 2.65 (+0.00) | 2.17 (+0.00) |
| Muse Wonder (max) | 0.00 (+0.00) | 3.07 (+0.00) | 3.42 (+0.00) | 3.77 (+0.00) | 3.06 (+0.00) |
| Qwen3.8 Max | 0.00 (+0.00) | 0.00 (+0.00) | 0.97 (+0.00) | 0.00 (+0.00) | 0.17 (+0.00) |

Plan streams S1, S2, S1 endpoint-heavy and S1M run with owner-named transfers off (E167): Claude Haiku 5.5 (high), Claude Haiku 5.5 (low), Claude Haiku 5.5 (max), Claude Haiku 5.5 (medium), Claude Haiku 5.5 (xhigh), Claude Opus 5 (max), Claude Sonnet 5.5 (high), Claude Sonnet 5.5 (low), Claude Sonnet 5.5 (max), Claude Sonnet 5.5 (medium), Claude Sonnet 5.5 (xhigh), GPT-5.6 Luna (max), GPT-5.6 Sol (max), GPT-6 Luna (max), GPT-6 Sol (max), GPT-6.1 Sol (high), GPT-6.1 Sol (low), GPT-6.1 Sol (medium), GPT-6.1 Sol (xhigh) depend on a transfer and are unevaluable there (—), never reselected or replaced by API cost.

### Plan basis: rank 1

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M |
|---|---:|---:|---:|---:|---:|
| Claude Fable 5.1 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Haiku 5.5 (high) | 0.0% | — | — | — | — |
| Claude Haiku 5.5 (low) | 0.0% | — | — | — | — |
| Claude Haiku 5.5 (max) | 0.0% | — | — | — | — |
| Claude Haiku 5.5 (medium) | 0.0% | — | — | — | — |
| Claude Haiku 5.5 (xhigh) | 0.0% | — | — | — | — |
| Claude Opus 5 (max) | 0.0% | — | — | — | — |
| Claude Opus 5.5 (max) | 0.0% | 100.0% | 100.0% | 100.0% | 100.0% |
| Claude Sonnet 5.5 (high) | 0.0% | — | — | — | — |
| Claude Sonnet 5.5 (low) | 0.0% | — | — | — | — |
| Claude Sonnet 5.5 (max) | 0.0% | — | — | — | — |
| Claude Sonnet 5.5 (medium) | 0.0% | — | — | — | — |
| Claude Sonnet 5.5 (xhigh) | 0.0% | — | — | — | — |
| DeepSeek V4 Flash (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| DeepSeek V4 Pro (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GLM-5.3 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-5.6 Luna (max) | 0.0% | — | — | — | — |
| GPT-5.6 Sol (max) | 0.0% | — | — | — | — |
| GPT-6 Astra (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Luna (max) | 0.0% | — | — | — | — |
| GPT-6 Sol (max) | 0.0% | — | — | — | — |
| GPT-6.1 Sol (high) | 0.0% | — | — | — | — |
| GPT-6.1 Sol (low) | 0.0% | — | — | — | — |
| GPT-6.1 Sol (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (medium) | 0.0% | — | — | — | — |
| GPT-6.1 Sol (xhigh) | 100.0% | — | — | — | — |
| Gemini 3.8 Flash (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Gemini 4 Argon (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Grok 4.6 (xhigh) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Grok 4.7 (xhigh) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Muse Spark 1.3 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Muse Spark 1.3 (xhigh) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Muse Wonder (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Qwen3.8 Max | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |

### Plan basis: rank 3 or better

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M |
|---|---:|---:|---:|---:|---:|
| Claude Fable 5.1 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Haiku 5.5 (high) | 0.0% | — | — | — | — |
| Claude Haiku 5.5 (low) | 0.0% | — | — | — | — |
| Claude Haiku 5.5 (max) | 0.0% | — | — | — | — |
| Claude Haiku 5.5 (medium) | 0.0% | — | — | — | — |
| Claude Haiku 5.5 (xhigh) | 0.0% | — | — | — | — |
| Claude Opus 5 (max) | 0.0% | — | — | — | — |
| Claude Opus 5.5 (max) | 0.0% | 100.0% | 100.0% | 100.0% | 100.0% |
| Claude Sonnet 5.5 (high) | 0.0% | — | — | — | — |
| Claude Sonnet 5.5 (low) | 0.0% | — | — | — | — |
| Claude Sonnet 5.5 (max) | 0.0% | — | — | — | — |
| Claude Sonnet 5.5 (medium) | 0.0% | — | — | — | — |
| Claude Sonnet 5.5 (xhigh) | 0.0% | — | — | — | — |
| DeepSeek V4 Flash (max) | 0.0% | 0.3% | 1.5% | 1.7% | 0.2% |
| DeepSeek V4 Pro (max) | 0.0% | 0.0% | 0.4% | 0.0% | 0.0% |
| GLM-5.3 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-5.6 Luna (max) | 0.0% | — | — | — | — |
| GPT-5.6 Sol (max) | 0.0% | — | — | — | — |
| GPT-6 Astra (max) | 0.0% | 68.5% | 66.1% | 52.4% | 67.5% |
| GPT-6 Luna (max) | 0.0% | — | — | — | — |
| GPT-6 Sol (max) | 0.0% | — | — | — | — |
| GPT-6.1 Sol (high) | 100.0% | — | — | — | — |
| GPT-6.1 Sol (low) | 0.0% | — | — | — | — |
| GPT-6.1 Sol (max) | 0.0% | 100.0% | 100.0% | 100.0% | 100.0% |
| GPT-6.1 Sol (medium) | 100.0% | — | — | — | — |
| GPT-6.1 Sol (xhigh) | 100.0% | — | — | — | — |
| Gemini 3.8 Flash (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Gemini 4 Argon (high) | 0.0% | 25.0% | 24.1% | 31.9% | 26.2% |
| Grok 4.6 (xhigh) | 0.0% | 1.1% | 2.0% | 3.6% | 1.0% |
| Grok 4.7 (xhigh) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Muse Spark 1.3 (max) | 0.0% | 0.0% | 0.2% | 0.0% | 0.0% |
| Muse Spark 1.3 (xhigh) | 0.0% | 0.0% | 0.1% | 0.0% | 0.0% |
| Muse Wonder (max) | 0.0% | 5.1% | 5.8% | 10.4% | 5.1% |
| Qwen3.8 Max | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |

### Plan basis: on the frontier

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M |
|---|---:|---:|---:|---:|---:|
| Claude Fable 5.1 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Haiku 5.5 (high) | 100.0% | — | — | — | — |
| Claude Haiku 5.5 (low) | 100.0% | — | — | — | — |
| Claude Haiku 5.5 (max) | 0.0% | — | — | — | — |
| Claude Haiku 5.5 (medium) | 100.0% | — | — | — | — |
| Claude Haiku 5.5 (xhigh) | 100.0% | — | — | — | — |
| Claude Opus 5 (max) | 0.0% | — | — | — | — |
| Claude Opus 5.5 (max) | 0.0% | 100.0% | 100.0% | 100.0% | 100.0% |
| Claude Sonnet 5.5 (high) | 100.0% | — | — | — | — |
| Claude Sonnet 5.5 (low) | 100.0% | — | — | — | — |
| Claude Sonnet 5.5 (max) | 100.0% | — | — | — | — |
| Claude Sonnet 5.5 (medium) | 100.0% | — | — | — | — |
| Claude Sonnet 5.5 (xhigh) | 100.0% | — | — | — | — |
| DeepSeek V4 Flash (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| DeepSeek V4 Pro (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GLM-5.3 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-5.6 Luna (max) | 0.0% | — | — | — | — |
| GPT-5.6 Sol (max) | 0.0% | — | — | — | — |
| GPT-6 Astra (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Luna (max) | 100.0% | — | — | — | — |
| GPT-6 Sol (max) | 0.0% | — | — | — | — |
| GPT-6.1 Sol (high) | 100.0% | — | — | — | — |
| GPT-6.1 Sol (low) | 0.0% | — | — | — | — |
| GPT-6.1 Sol (max) | 0.0% | 100.0% | 100.0% | 100.0% | 100.0% |
| GPT-6.1 Sol (medium) | 100.0% | — | — | — | — |
| GPT-6.1 Sol (xhigh) | 100.0% | — | — | — | — |
| Gemini 3.8 Flash (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Gemini 4 Argon (high) | 100.0% | 44.5% | 46.8% | 46.6% | 45.8% |
| Grok 4.6 (xhigh) | 0.0% | 4.6% | 4.8% | 10.1% | 4.1% |
| Grok 4.7 (xhigh) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Muse Spark 1.3 (max) | 0.0% | 0.0% | 1.0% | 0.0% | 0.0% |
| Muse Spark 1.3 (xhigh) | 0.0% | 0.0% | 0.2% | 0.0% | 0.0% |
| Muse Wonder (max) | 0.0% | 21.4% | 21.1% | 23.8% | 20.6% |
| Qwen3.8 Max | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |

### Plan basis: value-score dispersion (SD; covariance term)

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M |
|---|---:|---:|---:|---:|---:|
| Claude Fable 5.1 (max) | 0.00 (+0.00) | 0.00 (+0.00) | 0.72 (+0.00) | 0.00 (+0.00) | 0.16 (+0.00) |
| Claude Haiku 5.5 (high) | 0.00 (+0.00) | — | — | — | — |
| Claude Haiku 5.5 (low) | 0.00 (+0.00) | — | — | — | — |
| Claude Haiku 5.5 (max) | 0.00 (+0.00) | — | — | — | — |
| Claude Haiku 5.5 (medium) | 0.00 (+0.00) | — | — | — | — |
| Claude Haiku 5.5 (xhigh) | 0.00 (+0.00) | — | — | — | — |
| Claude Opus 5 (max) | 0.00 (+0.00) | — | — | — | — |
| Claude Opus 5.5 (max) | 0.00 (+0.00) | 0.00 (+0.00) | 0.81 (+0.00) | 0.00 (+0.00) | 0.13 (+0.00) |
| Claude Sonnet 5.5 (high) | 0.00 (+0.00) | — | — | — | — |
| Claude Sonnet 5.5 (low) | 0.00 (+0.00) | — | — | — | — |
| Claude Sonnet 5.5 (max) | 0.00 (+0.00) | — | — | — | — |
| Claude Sonnet 5.5 (medium) | 0.00 (+0.00) | — | — | — | — |
| Claude Sonnet 5.5 (xhigh) | 0.00 (+0.00) | — | — | — | — |
| DeepSeek V4 Flash (max) | 0.00 (+0.00) | 3.04 (+0.00) | 3.34 (+0.00) | 3.76 (+0.00) | 3.04 (+0.00) |
| DeepSeek V4 Pro (max) | 0.00 (+0.00) | 3.06 (+0.00) | 3.39 (+0.00) | 3.75 (+0.00) | 3.08 (+0.00) |
| GLM-5.3 (max) | 0.00 (+0.00) | 0.00 (+0.00) | 1.12 (+0.00) | 0.00 (+0.00) | 0.14 (+0.00) |
| GPT-5.6 Luna (max) | 0.00 (+0.00) | — | — | — | — |
| GPT-5.6 Sol (max) | 0.00 (+0.00) | — | — | — | — |
| GPT-6 Astra (max) | 0.00 (+0.00) | 0.00 (+0.00) | 0.76 (+0.00) | 0.00 (+0.00) | 0.12 (+0.00) |
| GPT-6 Luna (max) | 0.00 (+0.00) | — | — | — | — |
| GPT-6 Sol (max) | 0.00 (+0.00) | — | — | — | — |
| GPT-6.1 Sol (high) | 0.00 (+0.00) | — | — | — | — |
| GPT-6.1 Sol (low) | 0.00 (+0.00) | — | — | — | — |
| GPT-6.1 Sol (max) | 0.00 (+0.00) | 0.00 (+0.00) | 0.78 (+0.00) | 0.00 (+0.00) | 0.13 (+0.00) |
| GPT-6.1 Sol (medium) | 0.00 (+0.00) | — | — | — | — |
| GPT-6.1 Sol (xhigh) | 0.00 (+0.00) | — | — | — | — |
| Gemini 3.8 Flash (high) | 0.00 (+0.00) | 0.00 (+0.00) | 1.49 (+0.00) | 0.00 (+0.00) | 0.15 (+0.00) |
| Gemini 4 Argon (high) | 0.00 (+0.00) | 2.15 (+0.00) | 2.56 (+0.00) | 2.64 (+0.00) | 2.18 (+0.00) |
| Grok 4.6 (xhigh) | 0.00 (+0.00) | 3.07 (+0.00) | 3.36 (+0.00) | 3.75 (+0.00) | 3.06 (+0.00) |
| Grok 4.7 (xhigh) | 0.00 (+0.00) | 0.00 (+0.00) | 1.34 (+0.00) | 0.00 (+0.00) | 0.15 (+0.00) |
| Muse Spark 1.3 (max) | 0.00 (+0.00) | 2.16 (+0.00) | 2.53 (+0.00) | 2.63 (+0.00) | 2.19 (+0.00) |
| Muse Spark 1.3 (xhigh) | 0.00 (+0.00) | 2.19 (+0.00) | 2.78 (+0.00) | 2.64 (+0.00) | 2.15 (+0.00) |
| Muse Wonder (max) | 0.00 (+0.00) | 3.06 (+0.00) | 3.41 (+0.00) | 3.77 (+0.00) | 3.04 (+0.00) |
| Qwen3.8 Max | 0.00 (+0.00) | 0.00 (+0.00) | 0.95 (+0.00) | 0.00 (+0.00) | 0.16 (+0.00) |

### Named S2 specification branches

- **Bug Hunt harness band (E19)** (S2): unevaluable; the captured tbench.ai leaderboard lists no configuration under two or more agents, so no cross-agent spread exists
- **cache-hit variation (E34)** (S2): unevaluable; AA's published cost embeds its cache-pricing protocol; varying the cache-hit rate needs each basket component's cache-read and uncached-input demand, which AA publishes only for the whole Index (E157)
- **first-party list versus cross-provider median price rule (E122)** (S2): unevaluable; AA publishes one price per configuration under its own rule; the alternative rule's prices are not captured

### Cheapest-above-the-bar labels (API basis)

The 90% rule's error bound holds per published event (candidate and kernel assignment); it is not corrected across the listed candidates (E198). Each kernel assignment code gives the kernel used for the candidate and the competitors, in that order (U uniform, H endpoint-heavy; a quality-level bar has no reference rows, so it takes no letter); the label needs every assignment met.

| Bar | Candidate | Reading | Frequency range | Kernel assignments | Label |
|---|---|---|---|---|---|
| quality 56.7 | GPT-6.1 Sol (xhigh) | not scenario-supported | 3.8% to 4.8% | UU not met, UH not met, HU not met, HH not met | no |
| quality 56.7 | GPT-6.1 Sol (max) | not scenario-supported | 0.4% to 0.7% | UU not met, UH not met, HU not met, HH not met | no |
| quality 56.7 | GPT-6.1 Sol (high) | not scenario-supported | 14.9% to 15.6% | UU not met, UH not met, HU not met, HH not met | no |
| quality 56.7 | GPT-6.1 Sol (medium) | not scenario-supported | 39.8% to 44.5% | UU not met, UH not met, HU not met, HH not met | no |
| quality 56.7 | Claude Sonnet 5.5 (high) | not scenario-supported | 0.3% to 0.5% | UU not met, UH not met, HU not met, HH not met | no |
| quality 56.7 | GPT-6.1 Sol (low) | not scenario-supported | 31.5% to 35.0% | UU not met, UH not met, HU not met, HH not met | no |
| quality 56.7 | DeepSeek V4 Flash (max) | not scenario-supported | 1.3% to 6.0% | UU not met, UH not met, HU not met, HH not met | no |
| quality 56.7 | DeepSeek V4 Pro (max) | not scenario-supported | 0.2% to 0.6% | UU not met, UH not met, HU not met, HH not met | no |
| quality 48.1 | GPT-6.1 Sol (medium) | not scenario-supported | 0.5% to 1.0% | UU not met, UH not met, HU not met, HH not met | no |
| quality 48.1 | GPT-6.1 Sol (low) | not scenario-supported | 8.2% to 9.5% | UU not met, UH not met, HU not met, HH not met | no |
| quality 48.1 | GPT-5.6 Luna (max) | not scenario-supported | 15.2% to 22.2% | UU not met, UH not met, HU not met, HH not met | no |
| quality 48.1 | Claude Haiku 5.5 (xhigh) | not scenario-supported | 10.3% to 14.9% | UU not met, UH not met, HU not met, HH not met | no |
| quality 48.1 | Claude Haiku 5.5 (high) | not scenario-supported | 5.3% to 15.4% | UU not met, UH not met, HU not met, HH not met | no |
| quality 48.1 | DeepSeek V4 Flash (max) | not scenario-supported | 45.7% to 51.3% | UU not met, UH not met, HU not met, HH not met | no |
| quality 60.9 | GPT-6.1 Sol (xhigh) | not scenario-supported | 18.6% to 21.5% | UU not met, UH not met, HU not met, HH not met | no |
| quality 60.9 | GPT-6.1 Sol (max) | not scenario-supported | 16.2% to 18.5% | UU not met, UH not met, HU not met, HH not met | no |
| quality 60.9 | GPT-6.1 Sol (high) | not scenario-supported | 21.2% to 25.0% | UU not met, UH not met, HU not met, HH not met | no |
| quality 60.9 | GPT-6.1 Sol (medium) | not scenario-supported | 25.8% to 30.3% | UU not met, UH not met, HU not met, HH not met | no |
| quality 60.9 | Claude Sonnet 5.5 (high) | not scenario-supported | 0.0% to 0.6% | UU not met, UH not met, HU not met, HH not met | no |
| quality 60.9 | GPT-6.1 Sol (low) | not scenario-supported | 7.7% to 14.4% | UU not met, UH not met, HU not met, HH not met | no |

## Diagnostics

- **Terminal-Bench same-harness (Terminus 2):** undefined (panel too small); 14 rows ran on mixed harnesses.
- **Quality agreement:** quality agreement (matched-panel sensitivity): Kendall tau 0.80 (interval 0.47 to 1.00) on 14 rows.
- **Quality-substitution value agreement (API):** quality-substitution value agreement, api basis (matched-panel sensitivity): Kendall tau 0.36 (interval -0.09 to 0.69) on 14 rows.
- **Quality-substitution value agreement (Plan):** quality-substitution value agreement, plan basis (matched-panel sensitivity): Kendall tau 0.71 (interval 0.44 to 0.95) on 14 rows.
- **Disjoint-evidence agreement:** disjoint-evidence agreement (restricted evidence comparison, not an eligible ranking): Kendall tau 0.54 (interval 0.15 to 0.85) on 14 rows.
- **Quality source shares:** AA-run 80%, independent 20%.
- **Non-discriminating leaves:** none.
- **Group drift:** estimated; flagged: none.
- **Omniscience abstention sensitivity** (z_pen = max(0, I)): 25 rows move; largest move 9 (MiMo-V2.6-Pro).
- **GDPval-AA logistic sensitivity** (z = 100 / (1 + 10^((1600 - E) / 400)) against AA's pinned anchor; every other input fixed): API 31 rows move; largest move 7 (DeepSeek V4 Flash (max)); Plan 25 rows move; largest move 7 (Claude Fable 5.1 (max)).
- **Anchor stability:** trimmed anchors (P10 / 2 and P90 x 2 (diagnostic only)) give $100.49 to $13,333.70; 29 rows move; largest move 9 (Claude Haiku 5.5 (xhigh), Claude Haiku 5.5 (high)).

- **Basket readiness (E22):** priced leaves cover 67% of nominal quality weight (AutomationBench-AA, DeepSWE v1.1, GDPval-AA v2.1, AA-LCR v1.1, SciCode, Terminal-Bench 4.0 (tbench.ai)); pending components: FrontierCode, ITBench-AA.
- **SWE cost companion (O14, diagnostic):** 34 rows evaluated; flagged far from the median ratio: Claude Haiku 5.5 (max).
- **Matched-cost diagnostic (E55):** evaluated at 50% priced quality weight; basket/matched cost-order reversals with separated intervals: 24; rank-gap warnings: 3.
- **Frontier-families anchors (E187, diagnostic):** anchors rebuilt from the 8 frontier and near-frontier references move API 23 rows move; largest move 6 (Claude Haiku 5.5 (medium), Claude Sonnet 5.5 (max)) (value points per cost doubling 3.04 vs 2.74 frozen); Plan 20 rows move; largest move 5 (Claude Haiku 5.5 (high), Claude Opus 5 (max), GPT-6 Sol (max)) (value points per cost doubling 2.17 vs 1.73 frozen).
- **Frontier-families bar (E199, sensitivity; the frozen bar stays primary):** quality 60.9 over 8 configurations; cheapest at or above it on the API main workload: not unique; possibly GPT-6.1 Sol (xhigh), GPT-6.1 Sol (max), GPT-6.1 Sol (high), GPT-6.1 Sol (medium), Claude Sonnet 5.5 (high), GPT-6.1 Sol (low) (compares 17 configurations that can qualify).
- **One row per family (E205, diagnostic; the frozen ladder and anchors stay primary):** with each family's primary configuration only (22 bar-population rows), the ladder (headline, lower quartile, upper quartile) would be 58.3 / 50.0 / 60.9 against 56.7 / 48.1 / 60.9 frozen; anchors rebuilt from its 20 references move API 23 rows move; largest move 6 (Claude Haiku 5.5 (medium), Claude Sonnet 5.5 (max)) (value points per cost doubling 3.04 vs 2.74 frozen); Plan 16 rows move; largest move 4 (Claude Haiku 5.5 (high), GPT-5.6 Sol (max)) (value points per cost doubling 2.02 vs 1.73 frozen).
- **Bar currency (E207, informational):** rows reaching each frozen bar: quality 56.7: 18 of 35; quality 48.1: 27 of 35; quality 60.9: 10 of 35; the current population would freeze 56.7 / 48.1 / 60.9; lifetime until the next anchor re-freeze or methodology version, whichever comes first; no staleness flag.
- **Token mix (E208):** 2 selected routes: mix not reported: the measurement publishes no token-category shares; 23 selected routes: mix unidentified: the basket's token-category shares are set-identified only (E124), so the L1 test (above 0.30 flags mix-unmatched) is not computed.

### Leave-one-component-out cost family (E172)

Each admitted basket unit removed in turn, scored on anchors rebuilt by the freeze rule (rank changes against the primary ranking; quality held fixed).

| Removed component | API rank changes | Plan rank changes | API value points per cost doubling |
|---|---|---|---:|
| Coding Agent Index | 23 rows move; largest move 11 (DeepSeek V4 Flash (max)) | 20 rows move; largest move 7 (Claude Haiku 5.5 (max), Claude Sonnet 5.5 (low)) | 2.47 |
| AA-Briefcase | 12 rows move; largest move 2 (Claude Opus 5 (max), Claude Opus 5.5 (max), GPT-6 Sol (max), Muse Wonder (max)) | no rank changes | 2.73 |
| GDPval-AA | 15 rows move; largest move 2 (Claude Haiku 5.5 (medium), Claude Opus 5.5 (max), GPT-6 Astra (max)) | no rank changes | 2.75 |
| GDP.pdf | 10 rows move; largest move 2 (Claude Haiku 5.5 (medium), Claude Opus 5.5 (max), DeepSeek V4 Flash (max), Muse Wonder (max)) | 4 rows move; largest move 1 (Claude Haiku 5.5 (xhigh), Claude Haiku 5.5 (medium), Claude Sonnet 5.5 (low), GPT-5.6 Luna (max)) | 2.68 |
| AutomationBench-AA | 12 rows move; largest move 4 (DeepSeek V4 Pro (max)) | 9 rows move; largest move 2 (Claude Haiku 5.5 (xhigh)) | 2.68 |
| Terminal-Bench 4.0 (AA Index run) | 9 rows move; largest move 6 (DeepSeek V4 Pro (max)) | 2 rows move; largest move 2 (GPT-5.6 Luna (max), GPT-6 Astra (max)) | 2.68 |
| SciCode | 8 rows move; largest move 2 (Claude Haiku 5.5 (medium), Claude Opus 5.5 (max)) | 2 rows move; largest move 1 (Claude Haiku 5.5 (medium), GPT-5.6 Luna (max)) | 2.68 |
| AA-LCR | 6 rows move; largest move 2 (Claude Haiku 5.5 (medium), Claude Opus 5.5 (max), DeepSeek V4 Flash (max), Muse Wonder (max)) | no rank changes | 2.67 |

### Subset rows: paired bridge and missing spend (E10, E173)

- **MiMo-V2.6-Flash, MiMo-V2.6-Pro** (subset without Coding Agent Index): Coding Agent Index is 40% of the full basket (median; 9% to 80% over 34 rows). Scored on its own subset anchors, the direction of its subset effect is not known. Paired bridge on the 34 full rows: API: the full rows' values change by -0.50 points (median; -2.58 to 3.39), 20 rows move; largest move 11 (DeepSeek V4 Flash (max)); Plan: the full rows' values change by -0.31 points (median; -1.26 to 2.04), 20 rows move; largest move 7 (Claude Haiku 5.5 (max), Claude Sonnet 5.5 (low)).

### Deletion sensitivity

| Branch | Retained nominal weight | Status | API rank changes | Plan rank changes |
|---|---:|---|---|---|
| leave-out:deepswe | 70% | evaluated | 32 rows move; largest move 11 (GPT-5.6 Luna (max)) | 29 rows move; largest move 10 (MiMo-V2.6-Flash) |
| leave-out:bugHunt | 90% | evaluated | 27 rows move; largest move 7 (Claude Sonnet 5.5 (max), DeepSeek V4 Pro (max)) | 22 rows move; largest move 4 (Claude Sonnet 5.5 (max), MiMo-V2.6-Flash, Muse Wonder (max)) |
| leave-out:frontierCode | 90% | evaluated | 27 rows move; largest move 7 (Claude Sonnet 5.5 (low)) | 26 rows move; largest move 7 (Gemini 4 Argon (high)) |
| leave-out:terminalBench | 90% | evaluated | 29 rows move; largest move 16 (Muse Spark 1.3 (xhigh)) | 20 rows move; largest move 9 (GPT-5.6 Luna (max)) |
| leave-out:gdpval | 90% | evaluated | 21 rows move; largest move 5 (Claude Sonnet 5.5 (low), MiMo-V2.6-Pro) | 23 rows move; largest move 4 (Claude Haiku 5.5 (xhigh), Claude Haiku 5.5 (high)) |
| leave-out:automationBench | 90% | evaluated | 28 rows move; largest move 7 (Claude Haiku 5.5 (low)) | 18 rows move; largest move 4 (Claude Haiku 5.5 (low), Claude Haiku 5.5 (medium)) |
| leave-out:omniscience | 90% | evaluated | 24 rows move; largest move 5 (DeepSeek V4 Pro (max)) | 19 rows move; largest move 8 (MiMo-V2.6-Flash) |
| leave-out:lcr | 95% | evaluated | 14 rows move; largest move 3 (Claude Haiku 5.5 (medium), DeepSeek V4 Flash (max), GPT-6 Astra (max), MiMo-V2.6-Pro, Muse Wonder (max)) | 16 rows move; largest move 2 (Claude Haiku 5.5 (xhigh), Claude Haiku 5.5 (medium), Gemini 4 Argon (high), GPT-5.6 Sol (max), GPT-6 Astra (max), MiMo-V2.6-Pro) |
| leave-out:hle | 98% | evaluated | 2 rows move; largest move 1 (GPT-6 Sol (max), Muse Wonder (max)) | 5 rows move; largest move 2 (GPT-5.6 Luna (max)) |
| leave-out:scicode | 98% | evaluated | 2 rows move; largest move 1 (Claude Opus 5 (max), Gemini 3.8 Flash (high)) | 4 rows move; largest move 1 (Claude Haiku 5.5 (medium), Claude Sonnet 5.5 (low), GPT-5.6 Luna (max), GPT-5.6 Sol (max)) |
| leave-out:critpt | 98% | evaluated | 8 rows move; largest move 1 (Claude Opus 5 (max), Claude Opus 5.5 (max), DeepSeek V4 Pro (max), Gemini 3.8 Flash (high), GPT-5.6 Sol (max), GPT-6 Astra (max), GPT-6 Sol (max), Muse Wonder (max)) | 6 rows move; largest move 1 (Claude Fable 5.1 (max), Claude Haiku 5.5 (xhigh), Claude Haiku 5.5 (medium), Claude Sonnet 5.5 (low), GPT-5.6 Luna (max), MiMo-V2.6-Flash) |
| leave-source-out:Artificial Analysis | 20% | not identifiable under the coverage rule | — | — |
| basket-scope | 87% | evaluated | 24 rows move; largest move 5 (DeepSeek V4 Pro (max)) | 20 rows move; largest move 12 (MiMo-V2.6-Flash) |

### Cost-component removal (Terminal-Bench 4.0 (AA Index run): evaluated)

| Basis | Run | Rank changes |
|---|---|---|
| api | cost-component removal, original anchors | 13 rows move; largest move 7 (DeepSeek V4 Pro (max)) |
| api | alternative workload, recalibrated anchors | 9 rows move; largest move 6 (DeepSeek V4 Pro (max)) |
| plan | cost-component removal, original anchors; fixed-multiple arithmetic stress (not identified Plan economics for the altered workload) | 2 rows move; largest move 2 (GPT-5.6 Luna (max), GPT-6 Astra (max)) |
| plan | alternative workload, recalibrated anchors; fixed-multiple arithmetic stress (not identified Plan economics for the altered workload) | 2 rows move; largest move 2 (GPT-5.6 Luna (max), GPT-6 Astra (max)) |

## Release gates

| Rule | Status | Detail |
|---|---|---|
| clip gate (E20) | passed | no basis exceeds the clipping allowance |
| cost influence flag (E91) | passed | cost not discriminating (< 10%); informational only; beta never changes (O2) |
| quality influence flag (E126) | passed | quality not discriminating (cost share > 90%); informational only |
| subset scoring (O17) | fired | subset rows scored on their own workload and anchors |
| partial component flag (E37) | fired | AA declined- or missing-task markers |
| route dominance filter (E88) | vacuous | certifiably dearer routes set aside |
| Plan exploratory label (E61) | fired | fewer than half of Plan rows have an identified M_W |
| score swing gate (E177) | vacuous | first v3 release: no previous v3 release to compare |
| anchor migration (E184) | vacuous | no main-workload migration deferred |
| configuration map coverage | passed | every cohort row has a pinned identity |
| quality clipping audit (E110) | passed | saturation disclosed; domain violations block the build |
| scenario outputs current (E72) | passed | scenario input hash matches the scored inputs |
