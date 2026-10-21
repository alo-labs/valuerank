# ValueRank v3.0.0 Scores

**Updated:** October 19, 2026 · methodology 3.0.0 · SDLC basket v1 · anchor version `v3-2026-10-21`

Value = 25% × cost score + 75% × quality. Costs are USD per basket run; the cost score is log-scaled against the frozen anchors of the row's workload (see [methodology.md](methodology.md)).

## Ranking

| Configuration | Plan rank | Plan value | Plan cost score | API rank | API value | API cost score | Quality | Quality coverage | Workload |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| [Claude Sonnet 5.5 (max)](https://valuerank.alolabs.dev/models/claude-sonnet-5-5/) | 1 | 59.46 | 44.32 | 13 | 51.37 | 11.96 | 64.50 | 100% | main |
| [GPT-6.1 Sol (xhigh)](https://valuerank.alolabs.dev/models/gpt-6-1-sol-xhigh/) | 2 | 59.08 | 51.61 | 1 | 58.76 | 50.34 | 61.57 | 100% | main |
| [Claude Opus 5.5 (max)](https://valuerank.alolabs.dev/models/claude-opus-5-5/) | 3 | 58.68 | 43.69 | 14 | 50.49 | 10.96 | 63.67 | 100% | main |
| [Claude Sonnet 5.5 (xhigh)](https://valuerank.alolabs.dev/models/claude-sonnet-5-5-xhigh/) | 4 | 58.64 | 56.28 | 11 | 52.29 | 30.86 | 59.43 | 100% | main |
| [GPT-6.1 Sol (high)](https://valuerank.alolabs.dev/models/gpt-6-1-sol-high/) | 5 | 57.99 | 53.27 | 4 | 57.91 | 52.97 | 59.56 | 100% | main |
| [GPT-6.1 Sol (medium)](https://valuerank.alolabs.dev/models/gpt-6-1-sol-medium/) | 6 | 57.91 | 56.03 | 2 | 58.23 | 57.33 | 58.54 | 100% | main |
| [GPT-6.1 Sol (max)](https://valuerank.alolabs.dev/models/gpt-6-1-sol/) | 7 | 57.67 | 47.34 | 5 | 56.73 | 43.59 | 61.11 | 100% | main |
| [Claude Sonnet 5.5 (high)](https://valuerank.alolabs.dev/models/claude-sonnet-5-5-high/) | 8 | 57.60 | 64.48 | 10 | 52.44 | 43.84 | 55.31 | 100% | main |
| [GPT-6.1 Sol (low)](https://valuerank.alolabs.dev/models/gpt-6-1-sol-low/) | 9 | 54.29 | 59.51 | 7 | 55.12 | 62.84 | 52.55 | 100% | main |
| [Claude Sonnet 5.5 (medium)](https://valuerank.alolabs.dev/models/claude-sonnet-5-5-medium/) | 10 | 54.23 | 69.82 | 18 | 49.85 | 52.28 | 49.03 | 100% | main |
| [GPT-6 Sol (max)](https://valuerank.alolabs.dev/models/gpt-6-sol/) | 11 | 53.32 | 42.79 | 12 | 51.72 | 36.39 | 56.83 | 100% | main |
| [Claude Opus 5 (max)](https://valuerank.alolabs.dev/models/claude-opus-5/) | 12 | 53.22 | 45.03 | 29 | 45.23 | 13.08 | 55.95 | 100% | main |
| [GPT-6 Luna (max)](https://valuerank.alolabs.dev/models/gpt-6-luna/) | 13 | 52.99 | 69.89 | 6 | 55.33 | 79.25 | 47.36 | 100% | main |
| [GPT-6 Astra (max)](https://valuerank.alolabs.dev/models/gpt-6-astra/) | 14 | 52.92 | 28.77 | 15 | 50.41 | 18.74 | 60.97 | 100% | main |
| [GPT-5.6 Sol (max)](https://valuerank.alolabs.dev/models/gpt-5-6-sol/) | 15 | 52.87 | 35.27 | 16 | 50.18 | 24.51 | 58.74 | 100% | main |
| [Claude Haiku 5.5 (xhigh)](https://valuerank.alolabs.dev/models/claude-haiku-5-5/) | 16 | 52.56 | 79.00 | 19 | 49.51 | 66.80 | 43.75 | 100% | main |
| [MiMo-V2.6-Pro](https://valuerank.alolabs.dev/models/mimo-v2-6-pro/) | 17 | 52.20 | 43.46 | 3 | 57.93 | 66.40 | 55.11 | 100% | subset |
| [Claude Sonnet 5.5 (low)](https://valuerank.alolabs.dev/models/claude-sonnet-5-5-low/) | 18 | 51.64 | 72.17 | 23 | 47.59 | 56.00 | 44.79 | 100% | main |
| [Gemini 4 Argon (high)](https://valuerank.alolabs.dev/models/gemini-4-argon/) | 19 | 51.62 | 13.06 | 8 | 55.10 | 26.97 | 64.47 | 100% | main |
| [GPT-5.6 Luna (max)](https://valuerank.alolabs.dev/models/gpt-5-6-luna/) | 20 | 51.60 | 61.13 | 9 | 52.67 | 65.39 | 48.42 | 100% | main |
| [Claude Haiku 5.5 (high)](https://valuerank.alolabs.dev/models/claude-haiku-5-5-high/) | 21 | 51.55 | 83.77 | 20 | 49.19 | 74.33 | 40.81 | 100% | main |
| [Claude Fable 5.1 (max)](https://valuerank.alolabs.dev/models/claude-fable-5-1/) | 22 | 51.47 | 26.89 | 24 | 46.90 | 8.62 | 59.66 | 100% | main |
| [Claude Haiku 5.5 (medium)](https://valuerank.alolabs.dev/models/claude-haiku-5-5-medium/) | 23 | 50.87 | 88.36 | 21 | 49.17 | 81.60 | 38.37 | 100% | main |
| [Claude Haiku 5.5 (max)](https://valuerank.alolabs.dev/models/claude-haiku-5-5-max/) | 24 | 49.80 | 66.97 | 30 | 45.00 | 47.77 | 44.08 | 100% | main |
| [Claude Haiku 5.5 (low)](https://valuerank.alolabs.dev/models/claude-haiku-5-5-low/) | 25 | 49.11 | 93.07 | 22 | 48.10 | 89.04 | 34.45 | 100% | main |
| [Muse Spark 1.3 (max)](https://valuerank.alolabs.dev/models/muse-spark-1-3/) | 26 | 46.15 | 15.78 | 17 | 50.02 | 31.26 | 56.27 | 100% | main |
| [Grok 4.7 (xhigh)](https://valuerank.alolabs.dev/models/grok-4-7/) | 27 | 43.37 | 6.93 | 28 | 45.96 | 17.27 | 55.52 | 100% | main |
| [GLM-5.3 (max)](https://valuerank.alolabs.dev/models/glm-5-3/) | 28 | 42.67 | 14.36 | 27 | 46.34 | 29.02 | 52.11 | 100% | main |
| [Gemini 3.8 Flash (high)](https://valuerank.alolabs.dev/models/gemini-3-8-flash/) | 29 | 42.41 | 18.66 | 25 | 46.70 | 35.81 | 50.32 | 100% | main |
| [DeepSeek V4 Pro (max)](https://valuerank.alolabs.dev/models/deepseek-v4-pro/) | 30 | 41.01 | 28.16 | 26 | 46.68 | 50.84 | 45.29 | 100% | main |
| [Qwen3.8 Max](https://valuerank.alolabs.dev/models/qwen3-8-max/) | 31 | 38.94 | 9.06 | 31 | 41.83 | 20.63 | 48.90 | 100% | main |
| [Muse Wonder Full (max)](https://valuerank.alolabs.dev/models/muse-wonder-full/) | — | — | — | — | — | — | 64.39 | 100% | — |

## Not ranked

| Model | Reasons |
|---|---|
| Claude Fable 5 | No exact-variant AA DeepSWE result in the selected source snapshot; Not a required AA frontier or near-frontier family model |
| Claude Opus 4.8 | No exact-variant AA DeepSWE result in the selected source snapshot; Not a required AA frontier or near-frontier family model |
| Claude Sonnet 5 | No exact-variant AA DeepSWE result in the selected source snapshot; Not a required AA frontier or near-frontier family model |
| DeepSeek V4 Flash | Incomplete benchmark evidence after an exhaustive search (O36): no FrontierCode 1.1 |
| GLM-5.2 | No eligible exact-model Bug Hunt result in the selected source snapshot; No exact-variant AA DeepSWE result in the selected source snapshot; Not a required AA frontier or near-frontier family model |
| GLM-5.3 Flash | No exact-variant AA DeepSWE result in the selected source snapshot; Not a required AA frontier or near-frontier family model |
| GPT-5.5 | No eligible exact-model Bug Hunt result in the selected source snapshot; No exact-variant AA DeepSWE result in the selected source snapshot; Not a required AA frontier or near-frontier family model |
| Gemini 3.5 Flash | No eligible exact-model Bug Hunt result in the selected source snapshot; No exact-variant AA DeepSWE result in the selected source snapshot; Not a required AA frontier or near-frontier family model |
| Gemini 3.6 Flash | No eligible exact-model Bug Hunt result in the selected source snapshot; No exact-variant AA DeepSWE result in the selected source snapshot; Not a required AA frontier or near-frontier family model |
| Gemini 3.7 Flash | No eligible exact-model Bug Hunt result in the selected source snapshot; No exact-variant AA DeepSWE result in the selected source snapshot; Not a required AA frontier or near-frontier family model |
| Grok 4.6 | No eligible exact-model Bug Hunt result in the selected source snapshot; No exact-variant AA DeepSWE result in the selected source snapshot; Not a required AA frontier or near-frontier family model |
| Grok 4.6 (xhigh) | Incomplete benchmark evidence after an exhaustive search (O36): no FrontierCode 1.1 |
| Kimi K3 | No eligible exact-model Bug Hunt result in the selected source snapshot; No exact-variant AA DeepSWE result in the selected source snapshot; Not a required AA frontier or near-frontier family model |
| MiMo-V2.6-Flash | Incomplete benchmark evidence after an exhaustive search (O36): no Bug Hunt Bench |
| Muse Spark 1.2 | No eligible exact-model Bug Hunt result in the selected source snapshot; No exact-variant AA DeepSWE result in the selected source snapshot; Not a required AA frontier or near-frontier family model |
| Muse Spark 1.3 (xhigh) | Incomplete benchmark evidence after an exhaustive search (O36): no FrontierCode 1.1 |
| Muse Wonder | Incomplete benchmark evidence after an exhaustive search (O36): no FrontierCode 1.1 |

## Quality leaf scores

Each leaf's score z on its fixed 0–100 anchors; "—" marks a leaf with no eligible exact-configuration result.

| Configuration | DeepSWE v1.1 | Bug Hunt Bench | FrontierCode 1.1 | Terminal-Bench 4.0 (AA run) | GDPval-AA v2.1 | AutomationBench-AA | AA-Omniscience | AA-LCR v1.1 | Humanity's Last Exam | SciCode | CritPt | Quality | Provisional |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Claude Sonnet 5.5 (max) | 72.0 | 48.9 | 45.8 | 63.6 | 66.9 | 71.8 | 66.2 | 82.7 | 55.0 | 61.0 | 31.4 | 64.50 | no |
| GPT-6.1 Sol (xhigh) | 73.2 | 40.7 | 49.3 | 54.0 | 51.9 | 66.6 | 70.4 | 79.7 | 52.6 | 55.7 | 31.7 | 61.57 | no |
| Claude Opus 5.5 (max) | 68.4 | 39.7 | 52.2 | 59.6 | 68.3 | 69.5 | 73.2 | 84.7 | 61.4 | 66.9 | 31.7 | 63.67 | no |
| Claude Sonnet 5.5 (xhigh) | 68.4 | 34.3 | 46.1 | 57.1 | 61.4 | 65.5 | 61.8 | 79.7 | 50.0 | 57.3 | 31.1 | 59.43 | no |
| GPT-6.1 Sol (high) | 70.5 | 34.8 | 48.0 | 51.5 | 50.6 | 64.5 | 70.7 | 82.3 | 51.4 | 55.8 | 30.0 | 59.56 | no |
| GPT-6.1 Sol (medium) | 72.0 | 27.6 | 50.2 | 48.0 | 47.5 | 62.6 | 70.0 | 83.3 | 49.9 | 53.2 | 27.7 | 58.54 | no |
| GPT-6.1 Sol (max) | 69.6 | 42.2 | 49.1 | 56.1 | 54.7 | 64.9 | 70.8 | 83.0 | 52.9 | 54.2 | 31.7 | 61.11 | no |
| Claude Sonnet 5.5 (high) | 66.7 | 32.7 | 44.3 | 43.9 | 52.5 | 59.4 | 60.5 | 78.0 | 45.8 | 53.7 | 24.6 | 55.31 | no |
| GPT-6.1 Sol (low) | 67.6 | 21.4 | 45.5 | 30.8 | 40.7 | 52.6 | 68.8 | 84.0 | 47.4 | 53.2 | 24.9 | 52.55 | no |
| Claude Sonnet 5.5 (medium) | 65.5 | 22.2 | 29.3 | 29.8 | 41.2 | 54.9 | 60.0 | 76.3 | 39.8 | 52.9 | 16.9 | 49.03 | no |
| GPT-6 Sol (max) | 69.0 | 27.9 | 49.3 | 43.9 | 50.4 | 61.6 | 63.6 | 83.7 | 47.9 | 57.6 | 30.9 | 56.83 | no |
| Claude Opus 5 (max) | 62.5 | 25.7 | 48.0 | 49.0 | 61.1 | 56.6 | 68.5 | 79.3 | 54.9 | 56.4 | 29.1 | 55.95 | no |
| GPT-6 Luna (max) | 63.7 | 17.4 | 41.9 | 12.6 | 46.6 | 53.2 | 50.3 | 83.3 | 38.5 | 54.6 | 19.4 | 47.36 | no |
| GPT-6 Astra (max) | 67.6 | 42.9 | 47.0 | 59.1 | 53.6 | 68.5 | 71.7 | 80.7 | 54.7 | 56.5 | 31.7 | 60.97 | no |
| GPT-5.6 Sol (max) | 72.3 | 41.4 | 47.5 | 39.9 | 55.4 | 60.1 | 61.0 | 84.0 | 49.5 | 57.1 | 32.3 | 58.74 | no |
| Claude Haiku 5.5 (xhigh) | 49.0 | 17.4 | 45.5 | 29.3 | 50.7 | 36.0 | 53.0 | 78.3 | 42.7 | 51.7 | 22.6 | 43.75 | no |
| MiMo-V2.6-Pro | 71.9 | 17.1 | 45.4 | 34.8 | 59.2 | 58.6 | 54.2 | 86.3 | 49.4 | 60.9 | 26.6 | 55.11 | no |
| Claude Sonnet 5.5 (low) | 61.9 | 18.1 | 26.4 | 20.7 | 33.8 | 49.4 | 59.7 | 76.0 | 36.2 | 49.1 | 11.4 | 44.79 | no |
| Gemini 4 Argon (high) | 78.8 | 38.8 | 43.5 | 57.1 | 56.2 | 77.5 | 71.2 | 79.7 | 57.1 | 61.8 | 27.1 | 64.47 | no |
| GPT-5.6 Luna (max) | 66.4 | 29.8 | 39.8 | 11.6 | 48.0 | 50.2 | 44.9 | 83.7 | 39.5 | 53.6 | 20.6 | 48.42 | no |
| Claude Haiku 5.5 (high) | 46.3 | 15.2 | 43.6 | 21.7 | 45.9 | 33.7 | 52.9 | 77.3 | 37.3 | 48.7 | 18.6 | 40.81 | no |
| Claude Fable 5.1 (max) | 64.3 | 41.0 | 49.0 | 52.0 | 62.7 | 59.4 | 71.7 | 85.3 | 59.1 | 63.1 | 29.7 | 59.66 | no |
| Claude Haiku 5.5 (medium) | 47.5 | 11.4 | 40.4 | 15.2 | 38.7 | 28.6 | 52.2 | 77.3 | 33.8 | 49.0 | 12.9 | 38.37 | no |
| Claude Haiku 5.5 (max) | 46.0 | 20.5 | 41.8 | 32.8 | 55.9 | 35.4 | 55.3 | 82.7 | 44.4 | 55.0 | 18.9 | 44.08 | no |
| Claude Haiku 5.5 (low) | 45.4 | 10.5 | 29.3 | 12.6 | 31.1 | 22.9 | 51.6 | 72.0 | 27.0 | 49.2 | 9.1 | 34.45 | no |
| Muse Spark 1.3 (max) | 71.7 | 30.7 | 40.6 | 33.3 | 59.0 | 57.9 | 62.5 | 83.0 | 48.7 | 58.8 | 24.9 | 56.27 | no |
| Grok 4.7 (xhigh) | 72.6 | 27.6 | 33.8 | 25.8 | 60.6 | 65.6 | 66.0 | 76.7 | 43.1 | 57.4 | 17.7 | 55.52 | no |
| GLM-5.3 (max) | 61.4 | 18.1 | 40.1 | 41.9 | 57.5 | 62.2 | 57.1 | 79.7 | 42.3 | 59.0 | 19.1 | 52.11 | no |
| Gemini 3.8 Flash (high) | 65.8 | 17.1 | 36.4 | 19.7 | 46.8 | 59.9 | 64.8 | 81.3 | 47.8 | 56.6 | 18.3 | 50.32 | no |
| DeepSeek V4 Pro (max) | 57.2 | 15.2 | 38.8 | 14.1 | 47.5 | 56.7 | 50.4 | 80.3 | 41.0 | 51.0 | 18.0 | 45.29 | no |
| Qwen3.8 Max | 51.0 | 24.5 | 43.2 | 38.9 | 58.3 | 56.2 | 56.0 | 80.3 | 43.1 | 52.1 | 17.7 | 48.90 | no |
| Muse Wonder Full (max) | 77.0 | 40.0 | 44.9 | 57.1 | 67.9 | 71.3 | 65.1 | 83.7 | 53.6 | 62.6 | 32.9 | 64.39 | no |

## Basket cost by component

USD at API rates for the exact configuration; "—" marks a component without an exact cost.

| Configuration | Coding Agent Index | FrontierCode | ITBench-AA | AA-Briefcase | GDPval-AA | GDP.pdf | AutomationBench-AA | Terminal-Bench 4.0 (AA Index run) | SciCode | AA-LCR | Basket cost | Missing admitted components |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Claude Sonnet 5.5 (max) | $4,299.81 | $826.00 | — | $1,863.13 | $1,504.30 | $79.43 | $678.32 | $834.67 | $80.07 | $33.93 | $9,373.65 | none |
| GPT-6.1 Sol (xhigh) | $315.03 | — | — | $94.51 | $122.86 | $36.81 | $164.62 | $67.71 | $6.35 | $19.35 | $827.23 | none |
| Claude Opus 5.5 (max) | $3,950.02 | $1,015.00 | $146.00 | $1,915.18 | $1,962.05 | $155.23 | $938.69 | $865.21 | $135.11 | $67.66 | $9,989.15 | none |
| Claude Sonnet 5.5 (xhigh) | $1,010.02 | $120.00 | — | $634.80 | $430.06 | $46.01 | $277.51 | $401.18 | $6.81 | $29.66 | $2,836.05 | none |
| GPT-6.1 Sol (high) | $269.44 | — | — | $76.16 | $94.10 | $34.94 | $148.34 | $54.66 | $3.73 | $19.14 | $700.51 | none |
| GPT-6.1 Sol (medium) | $213.52 | — | — | $42.26 | $50.86 | $33.75 | $128.97 | $40.51 | $2.68 | $19.02 | $531.56 | none |
| GPT-6.1 Sol (max) | $470.90 | $81.00 | — | $210.45 | $196.57 | $41.99 | $195.01 | $120.30 | $12.50 | $19.94 | $1,267.66 | none |
| Claude Sonnet 5.5 (high) | $374.36 | — | — | $297.64 | $151.47 | $40.86 | $205.39 | $144.29 | $4.61 | $29.39 | $1,248.00 | none |
| GPT-6.1 Sol (low) | $151.14 | — | — | $16.12 | $23.10 | $33.41 | $104.75 | $25.27 | $2.43 | $18.99 | $375.21 | none |
| Claude Sonnet 5.5 (medium) | $187.48 | — | — | $126.68 | $69.91 | $38.14 | $172.20 | $104.16 | $3.90 | $29.16 | $731.63 | none |
| GPT-6 Sol (max) | $905.89 | — | $38.00 | $238.81 | $280.84 | $42.54 | $235.06 | $264.22 | $12.24 | $19.82 | $1,999.41 | none |
| Claude Opus 5 (max) | $3,269.11 | — | — | $1,619.19 | $1,488.52 | $108.57 | $864.64 | $1,273.08 | $33.90 | $76.11 | $8,733.13 | none |
| GPT-6 Luna (max) | $53.30 | $9.00 | — | $15.47 | $19.66 | $2.85 | $23.91 | $15.59 | $1.06 | $1.02 | $132.87 | none |
| GPT-6 Astra (max) | $2,262.53 | $422.00 | $133.00 | $864.69 | $996.49 | $207.58 | $1,048.30 | $560.88 | $66.89 | $99.73 | $6,107.09 | none |
| GPT-5.6 Sol (max) | $1,925.06 | — | $106.00 | $365.84 | $618.22 | $92.85 | $638.90 | $534.15 | $22.95 | $40.16 | $4,238.14 | none |
| Claude Haiku 5.5 (xhigh) | $184.98 | $16.00 | — | $33.29 | $20.26 | $2.73 | $18.14 | $30.38 | $0.77 | $1.53 | $292.07 | none |
| MiMo-V2.6-Pro | — | $18.00 | — | $34.60 | $35.47 | $2.40 | $27.77 | $28.91 | $2.25 | $4.74 | $136.13 | Coding Agent Index |
| Claude Sonnet 5.5 (low) | $146.38 | — | — | $73.03 | $45.90 | $37.23 | $158.19 | $84.80 | $3.73 | $29.14 | $578.39 | none |
| Gemini 4 Argon (high) | $1,770.70 | $670.00 | — | $530.33 | $400.23 | $25.93 | $399.89 | $447.49 | $30.44 | $23.64 | $3,628.64 | none |
| GPT-5.6 Luna (max) | $132.72 | — | — | $35.95 | $24.18 | $5.68 | $59.91 | $56.06 | $2.67 | $2.09 | $319.25 | none |
| Claude Haiku 5.5 (high) | $110.50 | — | — | $20.29 | $9.59 | $2.26 | $14.91 | $21.88 | $0.43 | $1.50 | $181.35 | none |
| Claude Fable 5.1 (max) | $3,753.59 | $1,200.00 | $237.00 | $2,066.92 | $2,150.47 | $277.49 | $1,715.62 | $1,268.42 | $189.65 | $158.45 | $11,580.62 | none |
| Claude Haiku 5.5 (medium) | $68.60 | — | — | $12.10 | $4.56 | $2.06 | $12.57 | $12.79 | $0.34 | $1.49 | $114.51 | none |
| Claude Haiku 5.5 (max) | $781.84 | $33.00 | — | $61.41 | $48.90 | $5.27 | $27.80 | $43.02 | $3.15 | $1.93 | $973.34 | none |
| Claude Haiku 5.5 (low) | $43.40 | — | — | $4.30 | $2.28 | $1.93 | $10.04 | $7.82 | $0.27 | $1.48 | $71.52 | none |
| Muse Spark 1.3 (max) | $1,205.18 | — | — | $369.37 | $448.59 | $20.51 | $238.77 | $457.96 | $11.31 | $13.29 | $2,764.98 | none |
| Grok 4.7 (xhigh) | $2,671.69 | $1,131.00 | $203.00 | $846.62 | $1,415.17 | $32.43 | $707.44 | $963.85 | $38.30 | $24.51 | $6,700.02 | none |
| GLM-5.3 (max) | $1,285.14 | $432.00 | $91.00 | $514.04 | $496.54 | $17.34 | $302.51 | $532.24 | $23.62 | $14.86 | $3,186.29 | none |
| Gemini 3.8 Flash (high) | $747.62 | $372.00 | $86.00 | $245.87 | $372.82 | $10.90 | $278.70 | $385.54 | $22.12 | $9.88 | $2,073.44 | none |
| DeepSeek V4 Pro (max) | $72.13 | — | — | $90.59 | $127.70 | $11.00 | $223.87 | $247.85 | $14.47 | $13.89 | $801.50 | none |
| Qwen3.8 Max | $1,054.13 | $675.00 | $327.00 | $1,781.49 | $998.39 | $33.31 | $261.64 | $1,232.62 | $32.57 | $22.88 | $5,417.03 | none |
| Muse Wonder Full (max) | — | — | — | — | — | — | — | — | — | — | — | Coding Agent Index, AA-Briefcase, GDPval-AA, GDP.pdf, AutomationBench-AA, Terminal-Bench 4.0 (AA Index run), SciCode, AA-LCR |

### Valuation basis

Valuation-basis gate (E170): 30 compatible as captured, 2 valuation basis unverified (flagged: Claude Fable 5.1 (max), Muse Wonder Full (max)). AA's Index category costs reconcile exactly with the prices AA displays for each configuration at capture, so its applied prices are the prices in force at the release cutoff. Token metering (E176): 32 not published per configuration; AA values cached input at live measurements of each model's typical cache-hit rate. Source intervals (E174): terminalBench: captured, level 95% (tbench.ai: "The whiskers span the 95% confidence interval"); gdpval: published, not captured, level not stated by the source (the 95% level on AA's methodology page belongs to AA-Briefcase).

## Plan route selection

The Plan amount is the selected multiple times the cash paid for the fee period (E166), typed by what the measurement establishes; it is not capacity unless it says so. The multiple values only the measured workload's API-equivalent consumption; other plan features are not valued.

| Configuration | Selected route | Plan amount | Basket runs per fee period | Identification | Plan cost (USD per basket run) | Flags | Selection reason |
|---|---|---|---|---|---:|---|---|
| Claude Sonnet 5.5 (max) | Claude Pro $20 · common Claude assumption (58.9×, assumption) | $1,178 per month: assumed API-equivalent consumption (owner-named transfer) from claude-pro-opus55-semianalysis | 0.13 per month | unidentified | $159.15 | workload-unmatched; owner-named transfer (assumption); valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| GPT-6.1 Sol (xhigh) | ChatGPT Pro $500 · common GPT assumption (10.772×, assumption) | $5,386 per month: assumed API-equivalent consumption (owner-named transfer) | 6.51 per month | unidentified | $76.79 | workload-unmatched; owner-named transfer (assumption); valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| Claude Opus 5.5 (max) | Claude Pro $20 · Opus 5.5 (58.9×, measured) | $1,178 per month: measured-workload capacity | 0.12 per month | unidentified | $169.60 | workload-unmatched; valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| Claude Sonnet 5.5 (xhigh) | Claude Pro $20 · common Claude assumption (58.9×, assumption) | $1,178 per month: assumed API-equivalent consumption (owner-named transfer) from claude-pro-opus55-semianalysis | 0.42 per month | unidentified | $48.15 | workload-unmatched; owner-named transfer (assumption); valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| GPT-6.1 Sol (high) | ChatGPT Pro $500 · common GPT assumption (10.772×, assumption) | $5,386 per month: assumed API-equivalent consumption (owner-named transfer) | 7.69 per month | unidentified | $65.03 | workload-unmatched; owner-named transfer (assumption); valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| GPT-6.1 Sol (medium) | ChatGPT Pro $500 · common GPT assumption (10.772×, assumption) | $5,386 per month: assumed API-equivalent consumption (owner-named transfer) | 10.13 per month | unidentified | $49.35 | workload-unmatched; owner-named transfer (assumption); valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| GPT-6.1 Sol (max) | ChatGPT Pro $500 · common GPT assumption (10.772×, measured) | $5,386 per month: measured-workload capacity | 4.25 per month | unidentified | $117.68 | workload-unmatched; valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| Claude Sonnet 5.5 (high) | Claude Pro $20 · common Claude assumption (58.9×, assumption) | $1,178 per month: assumed API-equivalent consumption (owner-named transfer) from claude-pro-opus55-semianalysis | 0.94 per month | unidentified | $21.19 | workload-unmatched; owner-named transfer (assumption); valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| GPT-6.1 Sol (low) | ChatGPT Pro $500 · common GPT assumption (10.772×, assumption) | $5,386 per month: assumed API-equivalent consumption (owner-named transfer) | 14.35 per month | unidentified | $34.83 | workload-unmatched; owner-named transfer (assumption); valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| Claude Sonnet 5.5 (medium) | Claude Pro $20 · common Claude assumption (58.9×, assumption) | $1,178 per month: assumed API-equivalent consumption (owner-named transfer) from claude-pro-opus55-semianalysis | 1.61 per month | unidentified | $12.42 | workload-unmatched; owner-named transfer (assumption); valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| GPT-6 Sol (max) | ChatGPT Pro $500 · common GPT assumption (10.772×, assumption) | $5,386 per month: assumed API-equivalent consumption (owner-named transfer) | 2.69 per month | unidentified | $185.61 | workload-unmatched; owner-named transfer (assumption); valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| Claude Opus 5 (max) | Claude Pro $20 · common Claude assumption (58.9×, assumption) | $1,178 per month: assumed API-equivalent consumption (owner-named transfer) from claude-pro-opus55-semianalysis | 0.13 per month | unidentified | $148.27 | workload-unmatched; owner-named transfer (assumption); valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| GPT-6 Luna (max) | ChatGPT Pro $500 · common GPT assumption (10.772×, assumption) | $5,386 per month: assumed API-equivalent consumption (owner-named transfer) | 40.54 per month | unidentified | $12.33 | workload-unmatched; owner-named transfer (assumption); valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| GPT-6 Astra (max) | ChatGPT Plus $20 · common GPT assumption (8.1×, measured) | $162 per month: measured-workload capacity | 0.03 per month | unidentified | $753.96 | workload-unmatched; valuation basis unverified | higher evidence grade |
| GPT-5.6 Sol (max) | ChatGPT Pro $500 · common GPT assumption (10.772×, assumption) | $5,386 per month: assumed API-equivalent consumption (owner-named transfer) | 1.27 per month | unidentified | $393.44 | workload-unmatched; owner-named transfer (assumption); valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| Claude Haiku 5.5 (xhigh) | Claude Pro $20 · common Claude assumption (58.9×, assumption) | $1,178 per month: assumed API-equivalent consumption (owner-named transfer) from claude-pro-opus55-semianalysis | 4.03 per month | unidentified | $4.96 | workload-unmatched; owner-named transfer (assumption); valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| MiMo-V2.6-Pro | MiMo · provisional 1.5x assumption (1.5×, assumption) | fee not established: assumed API-equivalent consumption (owner-named transfer) | — | unidentified | $90.75 | workload-unmatched; owner-named transfer (assumption); valuation basis unverified; observed-usage multiple; full utilisation not established | only remaining eligible route |
| Claude Sonnet 5.5 (low) | Claude Pro $20 · common Claude assumption (58.9×, assumption) | $1,178 per month: assumed API-equivalent consumption (owner-named transfer) from claude-pro-opus55-semianalysis | 2.04 per month | unidentified | $9.82 | workload-unmatched; owner-named transfer (assumption); valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| Gemini 4 Argon (high) | — | — | — | — | $3,628.64 | API-cost fallback: no admitted Plan route; cross-estimand ordering not identified | no eligible route |
| GPT-5.6 Luna (max) | ChatGPT Pro $500 · common GPT assumption (10.772×, assumption) | $5,386 per month: assumed API-equivalent consumption (owner-named transfer) | 16.87 per month | unidentified | $29.64 | workload-unmatched; owner-named transfer (assumption); valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| Claude Haiku 5.5 (high) | Claude Pro $20 · common Claude assumption (58.9×, assumption) | $1,178 per month: assumed API-equivalent consumption (owner-named transfer) from claude-pro-opus55-semianalysis | 6.50 per month | unidentified | $3.08 | workload-unmatched; owner-named transfer (assumption); valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| Claude Fable 5.1 (max) | Claude Max $100 · Fable 5.1 (12.73×, measured) | $1,273 per month: measured-workload capacity | 0.11 per month | unidentified | $909.71 | workload-unmatched; valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| Claude Haiku 5.5 (medium) | Claude Pro $20 · common Claude assumption (58.9×, assumption) | $1,178 per month: assumed API-equivalent consumption (owner-named transfer) from claude-pro-opus55-semianalysis | 10.29 per month | unidentified | $1.94 | workload-unmatched; owner-named transfer (assumption); valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| Claude Haiku 5.5 (max) | Claude Pro $20 · common Claude assumption (58.9×, assumption) | $1,178 per month: assumed API-equivalent consumption (owner-named transfer) from claude-pro-opus55-semianalysis | 1.21 per month | unidentified | $16.53 | workload-unmatched; owner-named transfer (assumption); valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| Claude Haiku 5.5 (low) | Claude Pro $20 · common Claude assumption (58.9×, assumption) | $1,178 per month: assumed API-equivalent consumption (owner-named transfer) from claude-pro-opus55-semianalysis | 16.47 per month | unidentified | $1.21 | workload-unmatched; owner-named transfer (assumption); valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| Muse Spark 1.3 (max) | — | — | — | — | $2,764.98 | API-cost fallback: no admitted Plan route; cross-estimand ordering not identified | no eligible route |
| Grok 4.7 (xhigh) | — | — | — | — | $6,700.02 | API-cost fallback: no admitted Plan route; cross-estimand ordering not identified | no eligible route |
| GLM-5.3 (max) | — | — | — | — | $3,186.29 | API-cost fallback: no admitted Plan route; cross-estimand ordering not identified | no eligible route |
| Gemini 3.8 Flash (high) | — | — | — | — | $2,073.44 | API-cost fallback: no admitted Plan route; cross-estimand ordering not identified | no eligible route |
| DeepSeek V4 Pro (max) | — | — | — | — | $801.50 | API-cost fallback: no admitted Plan route; cross-estimand ordering not identified | no eligible route |
| Qwen3.8 Max | — | — | — | — | $5,417.03 | API-cost fallback: no admitted Plan route; cross-estimand ordering not identified | no eligible route |
| Muse Wonder Full (max) | — | — | — | — | — | — | no eligible route |

### Route alternatives

Every admissible route-measurement pair in comparator order (E171) and the comparator's pick with the selected pair removed (E179). A larger displayed multiple is arithmetic on the measured workload, never a claim that the route is cheaper on the scored workload. Workday-feasible multiple (E15), for the 24 routed rows: not evaluated: no evidenced quota schema for this route.

| Configuration | Admissible pairs | Unidentified | Pairs (multiple, status) | Leave-selected-out choice |
|---|---:|---:|---|---|
| Claude Sonnet 5.5 (max) | 3 | 3 | claude-pro-common-opus55-assumption (58.9×, selected); claude-max20x-common-opus55-assumption (58.63×, not selected by the comparator); claude-max5x-common-opus55-assumption (57.25×, not selected by the comparator) | claude-max20x-common-opus55-assumption (58.63×, value 59.45) |
| GPT-6.1 Sol (xhigh) | 4 | 4 | chatgpt-pro500-common-semianalysis-assumption (10.772×, selected); chatgpt-pro100-common-semianalysis-assumption (10.55×, not selected by the comparator); chatgpt-pro200-common-semianalysis-assumption (10.42×, not selected by the comparator); chatgpt-plus-common-semianalysis-assumption (8.1×, not selected by the comparator) | chatgpt-pro100-common-semianalysis-assumption (10.55×, value 59.03) |
| Claude Opus 5.5 (max) | 3 | 3 | claude-pro-opus55-semianalysis (58.9×, selected); claude-max20x-opus55-semianalysis (58.63×, not selected by the comparator); claude-max5x-opus55-semianalysis (57.25×, not selected by the comparator) | claude-max20x-opus55-semianalysis (58.63×, value 58.67) |
| Claude Sonnet 5.5 (xhigh) | 3 | 3 | claude-pro-common-opus55-assumption (58.9×, selected); claude-max20x-common-opus55-assumption (58.63×, not selected by the comparator); claude-max5x-common-opus55-assumption (57.25×, not selected by the comparator) | claude-max20x-common-opus55-assumption (58.63×, value 58.63) |
| GPT-6.1 Sol (high) | 4 | 4 | chatgpt-pro500-common-semianalysis-assumption (10.772×, selected); chatgpt-pro100-common-semianalysis-assumption (10.55×, not selected by the comparator); chatgpt-pro200-common-semianalysis-assumption (10.42×, not selected by the comparator); chatgpt-plus-common-semianalysis-assumption (8.1×, not selected by the comparator) | chatgpt-pro100-common-semianalysis-assumption (10.55×, value 57.93) |
| GPT-6.1 Sol (medium) | 4 | 4 | chatgpt-pro500-common-semianalysis-assumption (10.772×, selected); chatgpt-pro100-common-semianalysis-assumption (10.55×, not selected by the comparator); chatgpt-pro200-common-semianalysis-assumption (10.42×, not selected by the comparator); chatgpt-plus-common-semianalysis-assumption (8.1×, not selected by the comparator) | chatgpt-pro100-common-semianalysis-assumption (10.55×, value 57.86) |
| GPT-6.1 Sol (max) | 4 | 4 | chatgpt-pro500-common-semianalysis-assumption (10.772×, selected); chatgpt-pro100-common-semianalysis-assumption (10.55×, not selected by the comparator); chatgpt-pro200-common-semianalysis-assumption (10.42×, not selected by the comparator); chatgpt-plus-common-semianalysis-assumption (8.1×, not selected by the comparator) | chatgpt-pro100-common-semianalysis-assumption (10.55×, value 57.62) |
| Claude Sonnet 5.5 (high) | 3 | 3 | claude-pro-common-opus55-assumption (58.9×, selected); claude-max20x-common-opus55-assumption (58.63×, not selected by the comparator); claude-max5x-common-opus55-assumption (57.25×, not selected by the comparator) | claude-max20x-common-opus55-assumption (58.63×, value 57.59) |
| GPT-6.1 Sol (low) | 4 | 4 | chatgpt-pro500-common-semianalysis-assumption (10.772×, selected); chatgpt-pro100-common-semianalysis-assumption (10.55×, not selected by the comparator); chatgpt-pro200-common-semianalysis-assumption (10.42×, not selected by the comparator); chatgpt-plus-common-semianalysis-assumption (8.1×, not selected by the comparator) | chatgpt-pro100-common-semianalysis-assumption (10.55×, value 54.24) |
| Claude Sonnet 5.5 (medium) | 3 | 3 | claude-pro-common-opus55-assumption (58.9×, selected); claude-max20x-common-opus55-assumption (58.63×, not selected by the comparator); claude-max5x-common-opus55-assumption (57.25×, not selected by the comparator) | claude-max20x-common-opus55-assumption (58.63×, value 54.22) |
| GPT-6 Sol (max) | 4 | 4 | chatgpt-pro500-common-semianalysis-assumption (10.772×, selected); chatgpt-pro100-common-semianalysis-assumption (10.55×, not selected by the comparator); chatgpt-pro200-common-semianalysis-assumption (10.42×, not selected by the comparator); chatgpt-plus-common-semianalysis-assumption (8.1×, not selected by the comparator) | chatgpt-pro100-common-semianalysis-assumption (10.55×, value 53.27) |
| Claude Opus 5 (max) | 3 | 3 | claude-pro-common-opus55-assumption (58.9×, selected); claude-max20x-common-opus55-assumption (58.63×, not selected by the comparator); claude-max5x-common-opus55-assumption (57.25×, not selected by the comparator) | claude-max20x-common-opus55-assumption (58.63×, value 53.21) |
| GPT-6 Luna (max) | 4 | 4 | chatgpt-pro500-common-semianalysis-assumption (10.772×, selected); chatgpt-pro100-common-semianalysis-assumption (10.55×, not selected by the comparator); chatgpt-pro200-common-semianalysis-assumption (10.42×, not selected by the comparator); chatgpt-plus-common-semianalysis-assumption (8.1×, not selected by the comparator) | chatgpt-pro100-common-semianalysis-assumption (10.55×, value 52.94) |
| GPT-6 Astra (max) | 4 | 4 | chatgpt-plus-common-semianalysis-assumption (8.1×, selected); chatgpt-pro500-common-semianalysis-assumption (10.772×, not selected by the comparator); chatgpt-pro100-common-semianalysis-assumption (10.55×, not selected by the comparator); chatgpt-pro200-common-semianalysis-assumption (10.42×, not selected by the comparator) | chatgpt-pro500-common-semianalysis-assumption (10.772×, value 53.63) |
| GPT-5.6 Sol (max) | 4 | 4 | chatgpt-pro500-common-semianalysis-assumption (10.772×, selected); chatgpt-pro100-common-semianalysis-assumption (10.55×, not selected by the comparator); chatgpt-pro200-common-semianalysis-assumption (10.42×, not selected by the comparator); chatgpt-plus-common-semianalysis-assumption (8.1×, not selected by the comparator) | chatgpt-pro100-common-semianalysis-assumption (10.55×, value 52.82) |
| Claude Haiku 5.5 (xhigh) | 3 | 3 | claude-pro-common-opus55-assumption (58.9×, selected); claude-max20x-common-opus55-assumption (58.63×, not selected by the comparator); claude-max5x-common-opus55-assumption (57.25×, not selected by the comparator) | claude-max20x-common-opus55-assumption (58.63×, value 52.55) |
| MiMo-V2.6-Pro | 1 | 1 | mimo-provisional-user-assumption (1.5×, selected) | none: the row would fall back to API cost (O13) |
| Claude Sonnet 5.5 (low) | 3 | 3 | claude-pro-common-opus55-assumption (58.9×, selected); claude-max20x-common-opus55-assumption (58.63×, not selected by the comparator); claude-max5x-common-opus55-assumption (57.25×, not selected by the comparator) | claude-max20x-common-opus55-assumption (58.63×, value 51.62) |
| GPT-5.6 Luna (max) | 4 | 4 | chatgpt-pro500-common-semianalysis-assumption (10.772×, selected); chatgpt-pro100-common-semianalysis-assumption (10.55×, not selected by the comparator); chatgpt-pro200-common-semianalysis-assumption (10.42×, not selected by the comparator); chatgpt-plus-common-semianalysis-assumption (8.1×, not selected by the comparator) | chatgpt-pro100-common-semianalysis-assumption (10.55×, value 51.55) |
| Claude Haiku 5.5 (high) | 3 | 3 | claude-pro-common-opus55-assumption (58.9×, selected); claude-max20x-common-opus55-assumption (58.63×, not selected by the comparator); claude-max5x-common-opus55-assumption (57.25×, not selected by the comparator) | claude-max20x-common-opus55-assumption (58.63×, value 51.54) |
| Claude Fable 5.1 (max) | 2 | 2 | claude-max5x-fable51-semianalysis (12.73×, selected); claude-max20x-fable51-semianalysis (12.425×, not selected by the comparator) | claude-max20x-fable51-semianalysis (12.425×, value 51.41) |
| Claude Haiku 5.5 (medium) | 3 | 3 | claude-pro-common-opus55-assumption (58.9×, selected); claude-max20x-common-opus55-assumption (58.63×, not selected by the comparator); claude-max5x-common-opus55-assumption (57.25×, not selected by the comparator) | claude-max20x-common-opus55-assumption (58.63×, value 50.85) |
| Claude Haiku 5.5 (max) | 3 | 3 | claude-pro-common-opus55-assumption (58.9×, selected); claude-max20x-common-opus55-assumption (58.63×, not selected by the comparator); claude-max5x-common-opus55-assumption (57.25×, not selected by the comparator) | claude-max20x-common-opus55-assumption (58.63×, value 49.79) |
| Claude Haiku 5.5 (low) | 3 | 3 | claude-pro-common-opus55-assumption (58.9×, selected); claude-max20x-common-opus55-assumption (58.63×, not selected by the comparator); claude-max5x-common-opus55-assumption (57.25×, not selected by the comparator) | claude-max20x-common-opus55-assumption (58.63×, value 49.10) |

### Measured-only Plan view

Admission: exact-route measurement candidates of grade controlled or concordant reports (no transfers, no diagnostics). Selection: the official selector (E111, E88, E85) rerun among the admitted candidates. Panel: rows with an admitted measured candidate; others listed as 'no measured route' (no API fallback).

| Configuration | Status | Route | Plan cost | Value | Rank |
|---|---|---|---:|---:|---:|
| Claude Opus 5.5 (max) | measured, target-workload unmatched | claude-pro-opus55-semianalysis | $169.60 | 58.68 | 1 |
| GPT-6.1 Sol (max) | measured, target-workload unmatched | chatgpt-pro500-common-semianalysis-assumption | $117.68 | 57.67 | 2 |
| GPT-6 Astra (max) | measured, target-workload unmatched | chatgpt-plus-common-semianalysis-assumption | $753.96 | 52.92 | 3 |
| Claude Fable 5.1 (max) | measured, target-workload unmatched | claude-max5x-fable51-semianalysis | $909.71 | 51.47 | 4 |
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
| Grok 4.7 (xhigh) | no measured route | — | — | — | — |
| MiMo-V2.6-Pro | no measured route | — | — | — | — |
| Muse Spark 1.3 (max) | no measured route | — | — | — | — |
| Muse Wonder Full (max) | no measured route | — | — | — | — |
| Qwen3.8 Max | no measured route | — | — | — | — |

#### Measured-evidence calibration (diagnostic)

References: each workload's measured-only rows with complete cost evidence are the references: c_L = cheapest / 2, c_H = dearest x 2 (diagnostic only; the official anchors are unchanged). Status: evaluated.

- Workload `9a0d376cc6080f3c`: measured anchors $58.84 to $1,507.92 from Claude Opus 5.5 (max), GPT-6 Astra (max), GPT-6.1 Sol (max); anchor ratio 25.6 against the official 22070.1. Official Plan anchors are set by Claude Haiku 5.5 (low) (owner-named transfer) at the low end and Grok 4.7 (xhigh) (API-cost fallback) at the high end.
- Workload `1453a9a0576b02ea`: measured-evidence calibration unavailable (fewer than two measured references); measured rows none. Official Plan anchors are set by Claude Haiku 5.5 (low) (owner-named transfer) at the low end and Qwen3.8 Max (API-cost fallback) at the high end.

| Configuration | Value on official Plan anchors | Value on measured anchors | Rank change |
|---|---:|---:|---:|
| Claude Fable 5.1 (max) | 51.47 | 48.64 | 0 |
| Claude Opus 5.5 (max) | 58.68 | 64.60 | 1 |
| GPT-6 Astra (max) | 52.92 | 51.07 | 0 |
| GPT-6.1 Sol (max) | 57.67 | 65.49 | -1 |

Pairwise reversals: Claude Opus 5.5 (max) and GPT-6.1 Sol (max). Largest value change: 7.82 points.

## Interval outputs

**API basis, main workload: frontier.** Not evaluable: Claude Fable 5.1 (max), MiMo-V2.6-Pro, Muse Wonder Full (max).

| Configuration | Possible frontier | Definite frontier | Definite counterexample | Possible frontier blocked by |
|---|---|---|---|---|
| Gemini 4 Argon (high) | certified | certified | — | — |
| GPT-6.1 Sol (xhigh) | certified | certified | — | — |
| Claude Sonnet 5.5 (max) | certified | certified | — | — |
| GPT-6.1 Sol (max) | disproved | disproved | GPT-6.1 Sol (xhigh) | GPT-6.1 Sol (xhigh) |
| GPT-6.1 Sol (high) | certified | certified | — | — |
| GPT-6.1 Sol (medium) | certified | certified | — | — |
| Claude Opus 5.5 (max) | disproved | disproved | Gemini 4 Argon (high) | Gemini 4 Argon (high), Claude Sonnet 5.5 (max) |
| GPT-6 Astra (max) | disproved | disproved | Gemini 4 Argon (high) | Gemini 4 Argon (high), GPT-6.1 Sol (xhigh), GPT-6.1 Sol (max) |
| GPT-5.6 Sol (max) | disproved | disproved | Gemini 4 Argon (high) | Gemini 4 Argon (high), GPT-6.1 Sol (xhigh), GPT-6.1 Sol (max), GPT-6.1 Sol (high), Claude Sonnet 5.5 (xhigh) |
| Muse Spark 1.3 (max) | disproved | disproved | GPT-6.1 Sol (xhigh) | GPT-6.1 Sol (xhigh), GPT-6.1 Sol (max), GPT-6.1 Sol (high), GPT-6.1 Sol (medium), GPT-6 Sol (max) |
| Claude Sonnet 5.5 (xhigh) | disproved | disproved | GPT-6.1 Sol (xhigh) | GPT-6.1 Sol (xhigh), GPT-6.1 Sol (max), GPT-6.1 Sol (high) |
| GPT-6 Sol (max) | disproved | disproved | GPT-6.1 Sol (xhigh) | GPT-6.1 Sol (xhigh), GPT-6.1 Sol (max), GPT-6.1 Sol (high), GPT-6.1 Sol (medium) |
| Grok 4.7 (xhigh) | disproved | disproved | Gemini 4 Argon (high) | Gemini 4 Argon (high), GPT-6.1 Sol (xhigh), GPT-6.1 Sol (max), GPT-6.1 Sol (high), GPT-6.1 Sol (medium), GPT-6 Astra (max), GPT-5.6 Sol (max), Muse Spark 1.3 (max), Claude Sonnet 5.5 (xhigh), GPT-6 Sol (max) |
| GPT-6.1 Sol (low) | certified | certified | — | — |
| Claude Sonnet 5.5 (high) | disproved | disproved | GPT-6.1 Sol (xhigh) | GPT-6.1 Sol (xhigh), GPT-6.1 Sol (high), GPT-6.1 Sol (medium) |
| GPT-5.6 Luna (max) | certified | certified | — | — |
| GPT-6 Luna (max) | certified | certified | — | — |
| Claude Haiku 5.5 (max) | disproved | disproved | GPT-6.1 Sol (xhigh) | GPT-6.1 Sol (xhigh), GPT-6.1 Sol (high), GPT-6.1 Sol (medium), GPT-6.1 Sol (low), GPT-5.6 Luna (max), GPT-6 Luna (max), Claude Sonnet 5.5 (medium), Claude Sonnet 5.5 (low), DeepSeek V4 Pro (max) |
| Claude Haiku 5.5 (xhigh) | disproved | disproved | GPT-6 Luna (max) | GPT-6 Luna (max) |
| Gemini 3.8 Flash (high) | disproved | disproved | GPT-6.1 Sol (xhigh) | GPT-6.1 Sol (xhigh), GPT-6.1 Sol (max), GPT-6.1 Sol (high), GPT-6.1 Sol (medium), GPT-6 Sol (max), GPT-6.1 Sol (low), Claude Sonnet 5.5 (high) |
| Claude Sonnet 5.5 (medium) | disproved | disproved | GPT-6.1 Sol (high) | GPT-6.1 Sol (high), GPT-6.1 Sol (medium), GPT-6.1 Sol (low) |
| Claude Opus 5 (max) | disproved | disproved | Gemini 4 Argon (high) | Gemini 4 Argon (high), GPT-6.1 Sol (xhigh), GPT-6.1 Sol (max), GPT-6.1 Sol (high), GPT-6.1 Sol (medium), GPT-6 Astra (max), GPT-5.6 Sol (max), Muse Spark 1.3 (max), Claude Sonnet 5.5 (xhigh), GPT-6 Sol (max) |
| GLM-5.3 (max) | disproved | disproved | GPT-6.1 Sol (xhigh) | GPT-6.1 Sol (xhigh), GPT-6.1 Sol (max), GPT-6.1 Sol (high), GPT-6.1 Sol (medium), Muse Spark 1.3 (max), Claude Sonnet 5.5 (xhigh), GPT-6 Sol (max), GPT-6.1 Sol (low), Claude Sonnet 5.5 (high) |
| Claude Haiku 5.5 (high) | disproved | disproved | GPT-6 Luna (max) | GPT-6 Luna (max) |
| Claude Haiku 5.5 (medium) | certified | certified | — | — |
| Claude Haiku 5.5 (low) | certified | certified | — | — |
| Claude Sonnet 5.5 (low) | disproved | disproved | GPT-6.1 Sol (medium) | GPT-6.1 Sol (medium), GPT-6.1 Sol (low), GPT-5.6 Luna (max), GPT-6 Luna (max) |
| Qwen3.8 Max | disproved | disproved | Gemini 4 Argon (high) | Gemini 4 Argon (high), GPT-6.1 Sol (xhigh), GPT-6.1 Sol (max), GPT-6.1 Sol (high), GPT-6.1 Sol (medium), GPT-5.6 Sol (max), Muse Spark 1.3 (max), Claude Sonnet 5.5 (xhigh), GPT-6 Sol (max), GPT-6.1 Sol (low), Claude Sonnet 5.5 (high), Gemini 3.8 Flash (high), Claude Sonnet 5.5 (medium), GLM-5.3 (max) |
| DeepSeek V4 Pro (max) | disproved | disproved | GPT-6.1 Sol (high) | GPT-6.1 Sol (high), GPT-6.1 Sol (medium), GPT-6.1 Sol (low), GPT-5.6 Luna (max), GPT-6 Luna (max), Claude Sonnet 5.5 (medium) |

**API basis, main workload: cheapest at or above quality 55.3** (lower-median displayed quality of the non-provisional cohort configurations at freeze (E192; headline bar)). Status certified; confirmed cheapest: GPT-6.1 Sol (medium).

Configurations that can be confirmed to qualify: 14 (confirmation needs the full-composite lower bound, with missing leaves at 0, to clear the bar; O25). Cheaper same-family configurations on AA's chart that were not evaluated (not ranked: no exact DeepSWE and Bug Hunt pair; E201, O33): none.

Bar comparison: compares 15 configurations that can qualify. The bar is a displayed-quality level; qualification tests each row's full-composite bounds, so a row above the bar on displayed quality can still fail to qualify confirmed when leaves are missing (E198).

| Configuration | Displayed quality − bar | Confirmed qualifies | Possibly qualifies | Possibly cheapest |
|---|---:|---|---|---|
| Gemini 4 Argon (high) | 9.2 | certified | certified | disproved |
| GPT-6.1 Sol (xhigh) | 6.3 | certified | certified | disproved |
| Claude Sonnet 5.5 (max) | 9.2 | certified | certified | disproved |
| GPT-6.1 Sol (max) | 5.8 | certified | certified | disproved |
| GPT-6.1 Sol (high) | 4.3 | certified | certified | disproved |
| GPT-6.1 Sol (medium) | 3.2 | certified | certified | certified |
| Claude Opus 5.5 (max) | 8.4 | certified | certified | disproved |
| GPT-6 Astra (max) | 5.7 | certified | certified | disproved |
| GPT-5.6 Sol (max) | 3.4 | certified | certified | disproved |
| Muse Spark 1.3 (max) | 1.0 | certified | certified | disproved |
| Claude Sonnet 5.5 (xhigh) | 4.1 | certified | certified | disproved |
| GPT-6 Sol (max) | 1.5 | certified | certified | disproved |
| Grok 4.7 (xhigh) | 0.2 | certified | certified | disproved |
| GPT-6.1 Sol (low) | -2.8 | disproved | disproved | disproved |
| Claude Sonnet 5.5 (high) | 0.0 | disproved | certified | disproved |
| GPT-5.6 Luna (max) | -6.9 | disproved | disproved | disproved |
| GPT-6 Luna (max) | -7.9 | disproved | disproved | disproved |
| Claude Haiku 5.5 (max) | -11.2 | disproved | disproved | disproved |
| Claude Haiku 5.5 (xhigh) | -11.6 | disproved | disproved | disproved |
| Gemini 3.8 Flash (high) | -5.0 | disproved | disproved | disproved |
| Claude Sonnet 5.5 (medium) | -6.3 | disproved | disproved | disproved |
| Claude Opus 5 (max) | 0.6 | certified | certified | disproved |
| GLM-5.3 (max) | -3.2 | disproved | disproved | disproved |
| Claude Haiku 5.5 (high) | -14.5 | disproved | disproved | disproved |
| Claude Haiku 5.5 (medium) | -16.9 | disproved | disproved | disproved |
| Claude Haiku 5.5 (low) | -20.9 | disproved | disproved | disproved |
| Claude Sonnet 5.5 (low) | -10.5 | disproved | disproved | disproved |
| Qwen3.8 Max | -6.4 | disproved | disproved | disproved |
| DeepSeek V4 Pro (max) | -10.0 | disproved | disproved | disproved |

**API basis, main workload: cheapest at or above quality 47.4** (lower-quartile displayed quality of the non-provisional cohort configurations at freeze (O34)). Status certified; confirmed cheapest: none.

Configurations that can be confirmed to qualify: 21 (confirmation needs the full-composite lower bound, with missing leaves at 0, to clear the bar; O25). Cheaper same-family configurations on AA's chart that were not evaluated (not ranked: no exact DeepSWE and Bug Hunt pair; E201, O33): GPT-5.6 Luna (max): GPT-5.6 Luna (xhigh), GPT-5.6 Luna (high), GPT-5.6 Luna (medium), GPT-5.6 Luna (low), GPT-5.6 Luna (non-reasoning); GPT-6 Luna (max): GPT-6 Luna (xhigh), GPT-6 Luna (high), GPT-6 Luna (medium), GPT-6 Luna (low), GPT-6 Luna (non-reasoning).

Bar comparison: compares 22 configurations that can qualify. The bar is a displayed-quality level; qualification tests each row's full-composite bounds, so a row above the bar on displayed quality can still fail to qualify confirmed when leaves are missing (E198).

| Configuration | Displayed quality − bar | Confirmed qualifies | Possibly qualifies | Possibly cheapest |
|---|---:|---|---|---|
| Gemini 4 Argon (high) | 17.1 | certified | certified | disproved |
| GPT-6.1 Sol (xhigh) | 14.2 | certified | certified | disproved |
| Claude Sonnet 5.5 (max) | 17.1 | certified | certified | disproved |
| GPT-6.1 Sol (max) | 13.8 | certified | certified | disproved |
| GPT-6.1 Sol (high) | 12.2 | certified | certified | disproved |
| GPT-6.1 Sol (medium) | 11.2 | certified | certified | disproved |
| Claude Opus 5.5 (max) | 16.3 | certified | certified | disproved |
| GPT-6 Astra (max) | 13.6 | certified | certified | disproved |
| GPT-5.6 Sol (max) | 11.4 | certified | certified | disproved |
| Muse Spark 1.3 (max) | 8.9 | certified | certified | disproved |
| Claude Sonnet 5.5 (xhigh) | 12.1 | certified | certified | disproved |
| GPT-6 Sol (max) | 9.5 | certified | certified | disproved |
| Grok 4.7 (xhigh) | 8.2 | certified | certified | disproved |
| GPT-6.1 Sol (low) | 5.2 | certified | certified | disproved |
| Claude Sonnet 5.5 (high) | 7.9 | certified | certified | disproved |
| GPT-5.6 Luna (max) | 1.1 | certified | certified | certified |
| GPT-6 Luna (max) | 0.0 | disproved | certified | certified |
| Claude Haiku 5.5 (max) | -3.3 | disproved | disproved | disproved |
| Claude Haiku 5.5 (xhigh) | -3.6 | disproved | disproved | disproved |
| Gemini 3.8 Flash (high) | 3.0 | certified | certified | disproved |
| Claude Sonnet 5.5 (medium) | 1.7 | certified | certified | disproved |
| Claude Opus 5 (max) | 8.6 | certified | certified | disproved |
| GLM-5.3 (max) | 4.7 | certified | certified | disproved |
| Claude Haiku 5.5 (high) | -6.6 | disproved | disproved | disproved |
| Claude Haiku 5.5 (medium) | -9.0 | disproved | disproved | disproved |
| Claude Haiku 5.5 (low) | -12.9 | disproved | disproved | disproved |
| Claude Sonnet 5.5 (low) | -2.6 | disproved | disproved | disproved |
| Qwen3.8 Max | 1.5 | certified | certified | disproved |
| DeepSeek V4 Pro (max) | -2.1 | disproved | disproved | disproved |

**API basis, main workload: cheapest at or above quality 59.6** (upper-quartile displayed quality of the non-provisional cohort configurations at freeze (O34)). Status certified; confirmed cheapest: none.

Configurations that can be confirmed to qualify: 6 (confirmation needs the full-composite lower bound, with missing leaves at 0, to clear the bar; O25). Cheaper same-family configurations on AA's chart that were not evaluated (not ranked: no exact DeepSWE and Bug Hunt pair; E201, O33): none.

Bar comparison: compares 7 configurations that can qualify. The bar is a displayed-quality level; qualification tests each row's full-composite bounds, so a row above the bar on displayed quality can still fail to qualify confirmed when leaves are missing (E198).

| Configuration | Displayed quality − bar | Confirmed qualifies | Possibly qualifies | Possibly cheapest |
|---|---:|---|---|---|
| Gemini 4 Argon (high) | 4.9 | certified | certified | disproved |
| GPT-6.1 Sol (xhigh) | 2.0 | certified | certified | certified |
| Claude Sonnet 5.5 (max) | 4.9 | certified | certified | disproved |
| GPT-6.1 Sol (max) | 1.6 | certified | certified | disproved |
| GPT-6.1 Sol (high) | 0.0 | disproved | certified | certified |
| GPT-6.1 Sol (medium) | -1.0 | disproved | disproved | disproved |
| Claude Opus 5.5 (max) | 4.1 | certified | certified | disproved |
| GPT-6 Astra (max) | 1.4 | certified | certified | disproved |
| GPT-5.6 Sol (max) | -0.8 | disproved | disproved | disproved |
| Muse Spark 1.3 (max) | -3.3 | disproved | disproved | disproved |
| Claude Sonnet 5.5 (xhigh) | -0.1 | disproved | disproved | disproved |
| GPT-6 Sol (max) | -2.7 | disproved | disproved | disproved |
| Grok 4.7 (xhigh) | -4.0 | disproved | disproved | disproved |
| GPT-6.1 Sol (low) | -7.0 | disproved | disproved | disproved |
| Claude Sonnet 5.5 (high) | -4.3 | disproved | disproved | disproved |
| GPT-5.6 Luna (max) | -11.1 | disproved | disproved | disproved |
| GPT-6 Luna (max) | -12.2 | disproved | disproved | disproved |
| Claude Haiku 5.5 (max) | -15.5 | disproved | disproved | disproved |
| Claude Haiku 5.5 (xhigh) | -15.8 | disproved | disproved | disproved |
| Gemini 3.8 Flash (high) | -9.2 | disproved | disproved | disproved |
| Claude Sonnet 5.5 (medium) | -10.5 | disproved | disproved | disproved |
| Claude Opus 5 (max) | -3.6 | disproved | disproved | disproved |
| GLM-5.3 (max) | -7.5 | disproved | disproved | disproved |
| Claude Haiku 5.5 (high) | -18.8 | disproved | disproved | disproved |
| Claude Haiku 5.5 (medium) | -21.2 | disproved | disproved | disproved |
| Claude Haiku 5.5 (low) | -25.1 | disproved | disproved | disproved |
| Claude Sonnet 5.5 (low) | -14.8 | disproved | disproved | disproved |
| Qwen3.8 Max | -10.7 | disproved | disproved | disproved |
| DeepSeek V4 Pro (max) | -14.3 | disproved | disproved | disproved |

**Plan basis, main workload:** not evaluated (no row has FullCost and an identified M_W (E61/E67)).

**API basis, subset workload (AA-Briefcase, GDPval-AA, GDP.pdf, AutomationBench-AA, Terminal-Bench 4.0 (AA Index run), SciCode, AA-LCR; orderings across workloads not identified): frontier.** Not evaluable: Claude Fable 5.1 (max), Muse Wonder Full (max). Competing without a label (AA cost on a price not in force, O29, E183): MiMo-V2.6-Pro.

| Configuration | Possible frontier | Definite frontier | Definite counterexample | Possible frontier blocked by |
|---|---|---|---|---|
| Gemini 4 Argon (high) | certified | certified | — | — |
| GPT-6.1 Sol (xhigh) | certified | certified | — | — |
| Claude Sonnet 5.5 (max) | certified | certified | — | — |
| GPT-6.1 Sol (max) | disproved | disproved | GPT-6.1 Sol (xhigh) | GPT-6.1 Sol (xhigh) |
| GPT-6.1 Sol (high) | certified | certified | — | — |
| GPT-6.1 Sol (medium) | certified | certified | — | — |
| Claude Opus 5.5 (max) | disproved | disproved | Gemini 4 Argon (high) | Gemini 4 Argon (high), Claude Sonnet 5.5 (max) |
| GPT-6 Astra (max) | disproved | disproved | Gemini 4 Argon (high) | Gemini 4 Argon (high), GPT-6.1 Sol (xhigh), GPT-6.1 Sol (max) |
| GPT-5.6 Sol (max) | disproved | disproved | Gemini 4 Argon (high) | Gemini 4 Argon (high), GPT-6.1 Sol (xhigh), GPT-6.1 Sol (max), GPT-6.1 Sol (high), Claude Sonnet 5.5 (xhigh) |
| Muse Spark 1.3 (max) | disproved | disproved | GPT-6.1 Sol (xhigh) | GPT-6.1 Sol (xhigh), GPT-6.1 Sol (max), GPT-6.1 Sol (high), GPT-6.1 Sol (medium), GPT-6 Sol (max) |
| Claude Sonnet 5.5 (xhigh) | disproved | disproved | GPT-6.1 Sol (xhigh) | GPT-6.1 Sol (xhigh), GPT-6.1 Sol (max), GPT-6.1 Sol (high) |
| GPT-6 Sol (max) | disproved | disproved | GPT-6.1 Sol (xhigh) | GPT-6.1 Sol (xhigh), GPT-6.1 Sol (max), GPT-6.1 Sol (high), GPT-6.1 Sol (medium) |
| Grok 4.7 (xhigh) | disproved | disproved | Gemini 4 Argon (high) | Gemini 4 Argon (high), GPT-6.1 Sol (xhigh), GPT-6.1 Sol (max), GPT-6.1 Sol (high), GPT-6.1 Sol (medium), GPT-6 Astra (max), GPT-5.6 Sol (max), Muse Spark 1.3 (max), Claude Sonnet 5.5 (xhigh), GPT-6 Sol (max) |
| GPT-6.1 Sol (low) | disproved | disproved | MiMo-V2.6-Pro | MiMo-V2.6-Pro |
| Claude Sonnet 5.5 (high) | disproved | disproved | GPT-6.1 Sol (xhigh) | GPT-6.1 Sol (xhigh), GPT-6.1 Sol (max), GPT-6.1 Sol (high), GPT-6.1 Sol (medium) |
| GPT-5.6 Luna (max) | disproved | disproved | MiMo-V2.6-Pro | MiMo-V2.6-Pro |
| GPT-6 Luna (max) | certified | certified | — | — |
| Claude Haiku 5.5 (max) | disproved | disproved | MiMo-V2.6-Pro | MiMo-V2.6-Pro, GPT-5.6 Luna (max), GPT-6 Luna (max) |
| Claude Haiku 5.5 (xhigh) | disproved | disproved | GPT-6 Luna (max) | GPT-6 Luna (max) |
| Gemini 3.8 Flash (high) | disproved | disproved | GPT-6.1 Sol (xhigh) | GPT-6.1 Sol (xhigh), GPT-6.1 Sol (max), GPT-6.1 Sol (high), GPT-6.1 Sol (medium), GPT-6 Sol (max), MiMo-V2.6-Pro, GPT-6.1 Sol (low), Claude Sonnet 5.5 (high) |
| Claude Sonnet 5.5 (medium) | disproved | disproved | GPT-6.1 Sol (xhigh) | GPT-6.1 Sol (xhigh), GPT-6.1 Sol (high), GPT-6.1 Sol (medium), MiMo-V2.6-Pro, GPT-6.1 Sol (low) |
| Claude Opus 5 (max) | disproved | disproved | Gemini 4 Argon (high) | Gemini 4 Argon (high), GPT-6.1 Sol (xhigh), Claude Sonnet 5.5 (max), GPT-6.1 Sol (max), GPT-6.1 Sol (high), GPT-6.1 Sol (medium), GPT-6 Astra (max), GPT-5.6 Sol (max), Muse Spark 1.3 (max), Claude Sonnet 5.5 (xhigh), GPT-6 Sol (max) |
| GLM-5.3 (max) | disproved | disproved | Gemini 4 Argon (high) | Gemini 4 Argon (high), GPT-6.1 Sol (xhigh), GPT-6.1 Sol (max), GPT-6.1 Sol (high), GPT-6.1 Sol (medium), Muse Spark 1.3 (max), Claude Sonnet 5.5 (xhigh), GPT-6 Sol (max), MiMo-V2.6-Pro, GPT-6.1 Sol (low), Claude Sonnet 5.5 (high) |
| Claude Haiku 5.5 (high) | certified | certified | — | — |
| Claude Haiku 5.5 (medium) | certified | certified | — | — |
| Claude Haiku 5.5 (low) | certified | certified | — | — |
| Claude Sonnet 5.5 (low) | disproved | disproved | GPT-6.1 Sol (high) | GPT-6.1 Sol (high), GPT-6.1 Sol (medium), MiMo-V2.6-Pro, GPT-6.1 Sol (low), GPT-5.6 Luna (max), GPT-6 Luna (max) |
| Qwen3.8 Max | disproved | disproved | Gemini 4 Argon (high) | Gemini 4 Argon (high), GPT-6.1 Sol (xhigh), GPT-6.1 Sol (max), GPT-6.1 Sol (high), GPT-6.1 Sol (medium), GPT-6 Astra (max), GPT-5.6 Sol (max), Muse Spark 1.3 (max), Claude Sonnet 5.5 (xhigh), GPT-6 Sol (max), Grok 4.7 (xhigh), MiMo-V2.6-Pro, GPT-6.1 Sol (low), Claude Sonnet 5.5 (high), Gemini 3.8 Flash (high), Claude Sonnet 5.5 (medium), GLM-5.3 (max) |
| DeepSeek V4 Pro (max) | disproved | disproved | GPT-6.1 Sol (xhigh) | GPT-6.1 Sol (xhigh), GPT-6.1 Sol (high), GPT-6.1 Sol (medium), MiMo-V2.6-Pro, GPT-6.1 Sol (low), GPT-5.6 Luna (max), GPT-6 Luna (max), Claude Sonnet 5.5 (medium) |

**API basis, subset workload (AA-Briefcase, GDPval-AA, GDP.pdf, AutomationBench-AA, Terminal-Bench 4.0 (AA Index run), SciCode, AA-LCR; orderings across workloads not identified): cheapest at or above quality 55.3** (lower-median displayed quality of the non-provisional cohort configurations at freeze (E192; headline bar)). Status certified; confirmed cheapest: GPT-6.1 Sol (medium).

Configurations that can be confirmed to qualify: 14 (confirmation needs the full-composite lower bound, with missing leaves at 0, to clear the bar; O25). Cheaper same-family configurations on AA's chart that were not evaluated (not ranked: no exact DeepSWE and Bug Hunt pair; E201, O33): none.

Bar comparison: compares 15 configurations that can qualify. The bar is a displayed-quality level; qualification tests each row's full-composite bounds, so a row above the bar on displayed quality can still fail to qualify confirmed when leaves are missing (E198).

| Configuration | Displayed quality − bar | Confirmed qualifies | Possibly qualifies | Possibly cheapest |
|---|---:|---|---|---|
| Gemini 4 Argon (high) | 9.2 | certified | certified | disproved |
| GPT-6.1 Sol (xhigh) | 6.3 | certified | certified | disproved |
| Claude Sonnet 5.5 (max) | 9.2 | certified | certified | disproved |
| GPT-6.1 Sol (max) | 5.8 | certified | certified | disproved |
| GPT-6.1 Sol (high) | 4.3 | certified | certified | disproved |
| GPT-6.1 Sol (medium) | 3.2 | certified | certified | certified |
| Claude Opus 5.5 (max) | 8.4 | certified | certified | disproved |
| GPT-6 Astra (max) | 5.7 | certified | certified | disproved |
| GPT-5.6 Sol (max) | 3.4 | certified | certified | disproved |
| Muse Spark 1.3 (max) | 1.0 | certified | certified | disproved |
| Claude Sonnet 5.5 (xhigh) | 4.1 | certified | certified | disproved |
| GPT-6 Sol (max) | 1.5 | certified | certified | disproved |
| Grok 4.7 (xhigh) | 0.2 | certified | certified | disproved |
| GPT-6.1 Sol (low) | -2.8 | disproved | disproved | disproved |
| Claude Sonnet 5.5 (high) | 0.0 | disproved | certified | disproved |
| GPT-5.6 Luna (max) | -6.9 | disproved | disproved | disproved |
| GPT-6 Luna (max) | -7.9 | disproved | disproved | disproved |
| Claude Haiku 5.5 (max) | -11.2 | disproved | disproved | disproved |
| Claude Haiku 5.5 (xhigh) | -11.6 | disproved | disproved | disproved |
| Gemini 3.8 Flash (high) | -5.0 | disproved | disproved | disproved |
| Claude Sonnet 5.5 (medium) | -6.3 | disproved | disproved | disproved |
| Claude Opus 5 (max) | 0.6 | certified | certified | disproved |
| GLM-5.3 (max) | -3.2 | disproved | disproved | disproved |
| Claude Haiku 5.5 (high) | -14.5 | disproved | disproved | disproved |
| Claude Haiku 5.5 (medium) | -16.9 | disproved | disproved | disproved |
| Claude Haiku 5.5 (low) | -20.9 | disproved | disproved | disproved |
| Claude Sonnet 5.5 (low) | -10.5 | disproved | disproved | disproved |
| Qwen3.8 Max | -6.4 | disproved | disproved | disproved |
| DeepSeek V4 Pro (max) | -10.0 | disproved | disproved | disproved |

**API basis, subset workload (AA-Briefcase, GDPval-AA, GDP.pdf, AutomationBench-AA, Terminal-Bench 4.0 (AA Index run), SciCode, AA-LCR; orderings across workloads not identified): cheapest at or above quality 47.4** (lower-quartile displayed quality of the non-provisional cohort configurations at freeze (O34)). Status certified; confirmed cheapest: none.

Configurations that can be confirmed to qualify: 21 (confirmation needs the full-composite lower bound, with missing leaves at 0, to clear the bar; O25). Cheaper same-family configurations on AA's chart that were not evaluated (not ranked: no exact DeepSWE and Bug Hunt pair; E201, O33): GPT-6 Luna (max): GPT-6 Luna (xhigh), GPT-6 Luna (high), GPT-6 Luna (medium), GPT-6 Luna (low), GPT-6 Luna (non-reasoning).

Bar comparison: compares 22 configurations that can qualify. The bar is a displayed-quality level; qualification tests each row's full-composite bounds, so a row above the bar on displayed quality can still fail to qualify confirmed when leaves are missing (E198).

| Configuration | Displayed quality − bar | Confirmed qualifies | Possibly qualifies | Possibly cheapest |
|---|---:|---|---|---|
| Gemini 4 Argon (high) | 17.1 | certified | certified | disproved |
| GPT-6.1 Sol (xhigh) | 14.2 | certified | certified | disproved |
| Claude Sonnet 5.5 (max) | 17.1 | certified | certified | disproved |
| GPT-6.1 Sol (max) | 13.8 | certified | certified | disproved |
| GPT-6.1 Sol (high) | 12.2 | certified | certified | disproved |
| GPT-6.1 Sol (medium) | 11.2 | certified | certified | disproved |
| Claude Opus 5.5 (max) | 16.3 | certified | certified | disproved |
| GPT-6 Astra (max) | 13.6 | certified | certified | disproved |
| GPT-5.6 Sol (max) | 11.4 | certified | certified | disproved |
| Muse Spark 1.3 (max) | 8.9 | certified | certified | disproved |
| Claude Sonnet 5.5 (xhigh) | 12.1 | certified | certified | disproved |
| GPT-6 Sol (max) | 9.5 | certified | certified | disproved |
| Grok 4.7 (xhigh) | 8.2 | certified | certified | disproved |
| GPT-6.1 Sol (low) | 5.2 | certified | certified | disproved |
| Claude Sonnet 5.5 (high) | 7.9 | certified | certified | disproved |
| GPT-5.6 Luna (max) | 1.1 | certified | certified | disproved |
| GPT-6 Luna (max) | 0.0 | disproved | certified | certified |
| Claude Haiku 5.5 (max) | -3.3 | disproved | disproved | disproved |
| Claude Haiku 5.5 (xhigh) | -3.6 | disproved | disproved | disproved |
| Gemini 3.8 Flash (high) | 3.0 | certified | certified | disproved |
| Claude Sonnet 5.5 (medium) | 1.7 | certified | certified | disproved |
| Claude Opus 5 (max) | 8.6 | certified | certified | disproved |
| GLM-5.3 (max) | 4.7 | certified | certified | disproved |
| Claude Haiku 5.5 (high) | -6.6 | disproved | disproved | disproved |
| Claude Haiku 5.5 (medium) | -9.0 | disproved | disproved | disproved |
| Claude Haiku 5.5 (low) | -12.9 | disproved | disproved | disproved |
| Claude Sonnet 5.5 (low) | -2.6 | disproved | disproved | disproved |
| Qwen3.8 Max | 1.5 | certified | certified | disproved |
| DeepSeek V4 Pro (max) | -2.1 | disproved | disproved | disproved |

**API basis, subset workload (AA-Briefcase, GDPval-AA, GDP.pdf, AutomationBench-AA, Terminal-Bench 4.0 (AA Index run), SciCode, AA-LCR; orderings across workloads not identified): cheapest at or above quality 59.6** (upper-quartile displayed quality of the non-provisional cohort configurations at freeze (O34)). Status certified; confirmed cheapest: none.

Configurations that can be confirmed to qualify: 6 (confirmation needs the full-composite lower bound, with missing leaves at 0, to clear the bar; O25). Cheaper same-family configurations on AA's chart that were not evaluated (not ranked: no exact DeepSWE and Bug Hunt pair; E201, O33): none.

Bar comparison: compares 7 configurations that can qualify. The bar is a displayed-quality level; qualification tests each row's full-composite bounds, so a row above the bar on displayed quality can still fail to qualify confirmed when leaves are missing (E198).

| Configuration | Displayed quality − bar | Confirmed qualifies | Possibly qualifies | Possibly cheapest |
|---|---:|---|---|---|
| Gemini 4 Argon (high) | 4.9 | certified | certified | disproved |
| GPT-6.1 Sol (xhigh) | 2.0 | certified | certified | certified |
| Claude Sonnet 5.5 (max) | 4.9 | certified | certified | disproved |
| GPT-6.1 Sol (max) | 1.6 | certified | certified | disproved |
| GPT-6.1 Sol (high) | 0.0 | disproved | certified | certified |
| GPT-6.1 Sol (medium) | -1.0 | disproved | disproved | disproved |
| Claude Opus 5.5 (max) | 4.1 | certified | certified | disproved |
| GPT-6 Astra (max) | 1.4 | certified | certified | disproved |
| GPT-5.6 Sol (max) | -0.8 | disproved | disproved | disproved |
| Muse Spark 1.3 (max) | -3.3 | disproved | disproved | disproved |
| Claude Sonnet 5.5 (xhigh) | -0.1 | disproved | disproved | disproved |
| GPT-6 Sol (max) | -2.7 | disproved | disproved | disproved |
| Grok 4.7 (xhigh) | -4.0 | disproved | disproved | disproved |
| GPT-6.1 Sol (low) | -7.0 | disproved | disproved | disproved |
| Claude Sonnet 5.5 (high) | -4.3 | disproved | disproved | disproved |
| GPT-5.6 Luna (max) | -11.1 | disproved | disproved | disproved |
| GPT-6 Luna (max) | -12.2 | disproved | disproved | disproved |
| Claude Haiku 5.5 (max) | -15.5 | disproved | disproved | disproved |
| Claude Haiku 5.5 (xhigh) | -15.8 | disproved | disproved | disproved |
| Gemini 3.8 Flash (high) | -9.2 | disproved | disproved | disproved |
| Claude Sonnet 5.5 (medium) | -10.5 | disproved | disproved | disproved |
| Claude Opus 5 (max) | -3.6 | disproved | disproved | disproved |
| GLM-5.3 (max) | -7.5 | disproved | disproved | disproved |
| Claude Haiku 5.5 (high) | -18.8 | disproved | disproved | disproved |
| Claude Haiku 5.5 (medium) | -21.2 | disproved | disproved | disproved |
| Claude Haiku 5.5 (low) | -25.1 | disproved | disproved | disproved |
| Claude Sonnet 5.5 (low) | -14.8 | disproved | disproved | disproved |
| Qwen3.8 Max | -10.7 | disproved | disproved | disproved |
| DeepSeek V4 Pro (max) | -14.3 | disproved | disproved | disproved |

**Plan basis, subset workload (AA-Briefcase, GDPval-AA, GDP.pdf, AutomationBench-AA, Terminal-Bench 4.0 (AA Index run), SciCode, AA-LCR; orderings across workloads not identified):** not evaluated (unevaluable: no Plan multiple is identified for a subset workload (E149, E190)).

## Scenario shares

Frequencies over 10,000 scenarios per run (seed 20261021); streams are defined in [methodology.md](methodology.md#uncertainty-outputs). S1T adds benchmark sampling noise under an independent-task approximation (O39); the other streams exclude it, and every stream excludes correlated-task, harness and attempt effects (E155).

### API basis: rank 1

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M | S1T |
|---|---:|---:|---:|---:|---:|---:|
| Claude Fable 5.1 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Haiku 5.5 (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Haiku 5.5 (low) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Haiku 5.5 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Haiku 5.5 (medium) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Haiku 5.5 (xhigh) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Sonnet 5.5 (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Sonnet 5.5 (low) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Sonnet 5.5 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Sonnet 5.5 (medium) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Sonnet 5.5 (xhigh) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| DeepSeek V4 Pro (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GLM-5.3 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-5.6 Luna (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-5.6 Sol (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Luna (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.2% |
| GPT-6 Sol (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 19.5% |
| GPT-6.1 Sol (low) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.2% |
| GPT-6.1 Sol (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 4.3% |
| GPT-6.1 Sol (medium) | 0.0% | 0.0% | 4.0% | 0.0% | 0.0% | 27.7% |
| GPT-6.1 Sol (xhigh) | 100.0% | 100.0% | 96.0% | 100.0% | 100.0% | 48.0% |
| Gemini 3.8 Flash (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Gemini 4 Argon (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.1% |
| Grok 4.7 (xhigh) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Muse Spark 1.3 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Qwen3.8 Max | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |

### API basis: rank 3 or better

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M | S1T |
|---|---:|---:|---:|---:|---:|---:|
| Claude Fable 5.1 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Haiku 5.5 (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Haiku 5.5 (low) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Haiku 5.5 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Haiku 5.5 (medium) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Haiku 5.5 (xhigh) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Sonnet 5.5 (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Sonnet 5.5 (low) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Sonnet 5.5 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Sonnet 5.5 (medium) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Sonnet 5.5 (xhigh) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| DeepSeek V4 Pro (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GLM-5.3 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-5.6 Luna (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-5.6 Sol (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Luna (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 5.6% |
| GPT-6 Sol (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (high) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 76.0% |
| GPT-6.1 Sol (low) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 4.1% |
| GPT-6.1 Sol (max) | 0.0% | 0.0% | 0.1% | 0.0% | 0.0% | 34.3% |
| GPT-6.1 Sol (medium) | 100.0% | 100.0% | 99.9% | 100.0% | 100.0% | 84.1% |
| GPT-6.1 Sol (xhigh) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 92.4% |
| Gemini 3.8 Flash (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Gemini 4 Argon (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 3.4% |
| Grok 4.7 (xhigh) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Muse Spark 1.3 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Qwen3.8 Max | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |

### API basis: on the frontier

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M | S1T |
|---|---:|---:|---:|---:|---:|---:|
| Claude Fable 5.1 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.1% |
| Claude Haiku 5.5 (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.1% |
| Claude Haiku 5.5 (low) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% |
| Claude Haiku 5.5 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Haiku 5.5 (medium) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 95.8% |
| Claude Haiku 5.5 (xhigh) | 0.0% | 0.0% | 0.1% | 0.0% | 0.0% | 6.2% |
| Claude Opus 5 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (max) | 0.0% | 0.0% | 3.1% | 0.0% | 0.0% | 19.9% |
| Claude Sonnet 5.5 (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.1% |
| Claude Sonnet 5.5 (low) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Sonnet 5.5 (max) | 100.0% | 100.0% | 51.4% | 100.0% | 100.0% | 47.5% |
| Claude Sonnet 5.5 (medium) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Sonnet 5.5 (xhigh) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 7.0% |
| DeepSeek V4 Pro (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GLM-5.3 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-5.6 Luna (max) | 100.0% | 100.0% | 99.2% | 100.0% | 100.0% | 68.9% |
| GPT-5.6 Sol (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.2% |
| GPT-6 Astra (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 3.9% |
| GPT-6 Luna (max) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% |
| GPT-6 Sol (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.2% |
| GPT-6.1 Sol (high) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 67.2% |
| GPT-6.1 Sol (low) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 96.2% |
| GPT-6.1 Sol (max) | 0.0% | 0.0% | 2.9% | 0.0% | 0.0% | 37.8% |
| GPT-6.1 Sol (medium) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 99.5% |
| GPT-6.1 Sol (xhigh) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 77.4% |
| Gemini 3.8 Flash (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Gemini 4 Argon (high) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 85.3% |
| Grok 4.7 (xhigh) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Muse Spark 1.3 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.1% |
| Qwen3.8 Max | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |

### API basis: value-score dispersion (SD; covariance term)

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M | S1T |
|---|---:|---:|---:|---:|---:|---:|
| Claude Fable 5.1 (max) | 0.00 (+0.00) | 0.00 (+0.00) | 0.74 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.26 (+0.00) |
| Claude Haiku 5.5 (high) | 0.00 (+0.00) | 0.00 (+0.00) | 1.01 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.22 (+0.00) |
| Claude Haiku 5.5 (low) | 0.00 (+0.00) | 0.00 (+0.00) | 1.18 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.19 (+0.00) |
| Claude Haiku 5.5 (max) | 0.00 (+0.00) | 0.00 (+0.00) | 0.89 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.23 (+0.00) |
| Claude Haiku 5.5 (medium) | 0.00 (+0.00) | 0.00 (+0.00) | 1.16 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.22 (+0.00) |
| Claude Haiku 5.5 (xhigh) | 0.00 (+0.00) | 0.00 (+0.00) | 0.94 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.26 (+0.00) |
| Claude Opus 5 (max) | 0.00 (+0.00) | 0.00 (+0.00) | 0.96 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.26 (+0.00) |
| Claude Opus 5.5 (max) | 0.00 (+0.00) | 0.00 (+0.00) | 0.81 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.22 (+0.00) |
| Claude Sonnet 5.5 (high) | 0.00 (+0.00) | 0.00 (+0.00) | 0.92 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.23 (+0.00) |
| Claude Sonnet 5.5 (low) | 0.00 (+0.00) | 0.00 (+0.00) | 1.39 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.18 (+0.00) |
| Claude Sonnet 5.5 (max) | 0.00 (+0.00) | 0.00 (+0.00) | 0.77 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.20 (+0.00) |
| Claude Sonnet 5.5 (medium) | 0.00 (+0.00) | 0.00 (+0.00) | 1.31 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.21 (+0.00) |
| Claude Sonnet 5.5 (xhigh) | 0.00 (+0.00) | 0.00 (+0.00) | 0.88 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.23 (+0.00) |
| DeepSeek V4 Pro (max) | 0.00 (+0.00) | 0.00 (+0.00) | 1.33 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.21 (+0.00) |
| GLM-5.3 (max) | 0.00 (+0.00) | 0.00 (+0.00) | 1.13 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.24 (+0.00) |
| GPT-5.6 Luna (max) | 0.00 (+0.00) | 0.00 (+0.00) | 1.40 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.18 (+0.00) |
| GPT-5.6 Sol (max) | 0.00 (+0.00) | 0.00 (+0.00) | 0.98 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.19 (+0.00) |
| GPT-6 Astra (max) | 0.00 (+0.00) | 0.00 (+0.00) | 0.76 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.23 (+0.00) |
| GPT-6 Luna (max) | 0.00 (+0.00) | 0.00 (+0.00) | 1.45 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.18 (+0.00) |
| GPT-6 Sol (max) | 0.00 (+0.00) | 0.00 (+0.00) | 1.06 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.20 (+0.00) |
| GPT-6.1 Sol (high) | 0.00 (+0.00) | 0.00 (+0.00) | 0.97 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.22 (+0.00) |
| GPT-6.1 Sol (low) | 0.00 (+0.00) | 0.00 (+0.00) | 1.33 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.21 (+0.00) |
| GPT-6.1 Sol (max) | 0.00 (+0.00) | 0.00 (+0.00) | 0.78 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.24 (+0.00) |
| GPT-6.1 Sol (medium) | 0.00 (+0.00) | 0.00 (+0.00) | 1.14 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.19 (+0.00) |
| GPT-6.1 Sol (xhigh) | 0.00 (+0.00) | 0.00 (+0.00) | 0.90 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.19 (+0.00) |
| Gemini 3.8 Flash (high) | 0.00 (+0.00) | 0.00 (+0.00) | 1.49 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.19 (+0.00) |
| Gemini 4 Argon (high) | 0.00 (+0.00) | 0.00 (+0.00) | 1.15 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.12 (+0.00) |
| Grok 4.7 (xhigh) | 0.00 (+0.00) | 0.00 (+0.00) | 1.47 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.16 (+0.00) |
| Muse Spark 1.3 (max) | 0.00 (+0.00) | 0.00 (+0.00) | 1.24 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.17 (+0.00) |
| Qwen3.8 Max | 0.00 (+0.00) | 0.00 (+0.00) | 0.84 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.29 (+0.00) |

Plan streams S1, S2, S1 endpoint-heavy, S1M and S1T run with owner-named transfers off (E167): Claude Haiku 5.5 (high), Claude Haiku 5.5 (low), Claude Haiku 5.5 (max), Claude Haiku 5.5 (medium), Claude Haiku 5.5 (xhigh), Claude Opus 5 (max), Claude Sonnet 5.5 (high), Claude Sonnet 5.5 (low), Claude Sonnet 5.5 (max), Claude Sonnet 5.5 (medium), Claude Sonnet 5.5 (xhigh), GPT-5.6 Luna (max), GPT-5.6 Sol (max), GPT-6 Luna (max), GPT-6 Sol (max), GPT-6.1 Sol (high), GPT-6.1 Sol (low), GPT-6.1 Sol (medium), GPT-6.1 Sol (xhigh) depend on a transfer and are unevaluable there (—), never reselected or replaced by API cost.

### Plan basis: rank 1

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M | S1T |
|---|---:|---:|---:|---:|---:|---:|
| Claude Fable 5.1 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Haiku 5.5 (high) | 0.0% | — | — | — | — | — |
| Claude Haiku 5.5 (low) | 0.0% | — | — | — | — | — |
| Claude Haiku 5.5 (max) | 0.0% | — | — | — | — | — |
| Claude Haiku 5.5 (medium) | 0.0% | — | — | — | — | — |
| Claude Haiku 5.5 (xhigh) | 0.0% | — | — | — | — | — |
| Claude Opus 5 (max) | 0.0% | — | — | — | — | — |
| Claude Opus 5.5 (max) | 0.0% | 100.0% | 100.0% | 100.0% | 100.0% | 71.9% |
| Claude Sonnet 5.5 (high) | 0.0% | — | — | — | — | — |
| Claude Sonnet 5.5 (low) | 0.0% | — | — | — | — | — |
| Claude Sonnet 5.5 (max) | 100.0% | — | — | — | — | — |
| Claude Sonnet 5.5 (medium) | 0.0% | — | — | — | — | — |
| Claude Sonnet 5.5 (xhigh) | 0.0% | — | — | — | — | — |
| DeepSeek V4 Pro (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GLM-5.3 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-5.6 Luna (max) | 0.0% | — | — | — | — | — |
| GPT-5.6 Sol (max) | 0.0% | — | — | — | — | — |
| GPT-6 Astra (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Luna (max) | 0.0% | — | — | — | — | — |
| GPT-6 Sol (max) | 0.0% | — | — | — | — | — |
| GPT-6.1 Sol (high) | 0.0% | — | — | — | — | — |
| GPT-6.1 Sol (low) | 0.0% | — | — | — | — | — |
| GPT-6.1 Sol (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 28.1% |
| GPT-6.1 Sol (medium) | 0.0% | — | — | — | — | — |
| GPT-6.1 Sol (xhigh) | 0.0% | — | — | — | — | — |
| Gemini 3.8 Flash (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Gemini 4 Argon (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Grok 4.7 (xhigh) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Muse Spark 1.3 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Qwen3.8 Max | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |

### Plan basis: rank 3 or better

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M | S1T |
|---|---:|---:|---:|---:|---:|---:|
| Claude Fable 5.1 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 15.7% |
| Claude Haiku 5.5 (high) | 0.0% | — | — | — | — | — |
| Claude Haiku 5.5 (low) | 0.0% | — | — | — | — | — |
| Claude Haiku 5.5 (max) | 0.0% | — | — | — | — | — |
| Claude Haiku 5.5 (medium) | 0.0% | — | — | — | — | — |
| Claude Haiku 5.5 (xhigh) | 0.0% | — | — | — | — | — |
| Claude Opus 5 (max) | 0.0% | — | — | — | — | — |
| Claude Opus 5.5 (max) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% |
| Claude Sonnet 5.5 (high) | 0.0% | — | — | — | — | — |
| Claude Sonnet 5.5 (low) | 0.0% | — | — | — | — | — |
| Claude Sonnet 5.5 (max) | 100.0% | — | — | — | — | — |
| Claude Sonnet 5.5 (medium) | 0.0% | — | — | — | — | — |
| Claude Sonnet 5.5 (xhigh) | 0.0% | — | — | — | — | — |
| DeepSeek V4 Pro (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GLM-5.3 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-5.6 Luna (max) | 0.0% | — | — | — | — | — |
| GPT-5.6 Sol (max) | 0.0% | — | — | — | — | — |
| GPT-6 Astra (max) | 0.0% | 100.0% | 99.5% | 100.0% | 100.0% | 67.2% |
| GPT-6 Luna (max) | 0.0% | — | — | — | — | — |
| GPT-6 Sol (max) | 0.0% | — | — | — | — | — |
| GPT-6.1 Sol (high) | 0.0% | — | — | — | — | — |
| GPT-6.1 Sol (low) | 0.0% | — | — | — | — | — |
| GPT-6.1 Sol (max) | 0.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% |
| GPT-6.1 Sol (medium) | 0.0% | — | — | — | — | — |
| GPT-6.1 Sol (xhigh) | 100.0% | — | — | — | — | — |
| Gemini 3.8 Flash (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Gemini 4 Argon (high) | 0.0% | 0.0% | 0.5% | 0.0% | 0.0% | 17.1% |
| Grok 4.7 (xhigh) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Muse Spark 1.3 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Qwen3.8 Max | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |

### Plan basis: on the frontier

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M | S1T |
|---|---:|---:|---:|---:|---:|---:|
| Claude Fable 5.1 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 2.4% |
| Claude Haiku 5.5 (high) | 100.0% | — | — | — | — | — |
| Claude Haiku 5.5 (low) | 100.0% | — | — | — | — | — |
| Claude Haiku 5.5 (max) | 0.0% | — | — | — | — | — |
| Claude Haiku 5.5 (medium) | 100.0% | — | — | — | — | — |
| Claude Haiku 5.5 (xhigh) | 100.0% | — | — | — | — | — |
| Claude Opus 5 (max) | 0.0% | — | — | — | — | — |
| Claude Opus 5.5 (max) | 0.0% | 100.0% | 100.0% | 100.0% | 100.0% | 86.9% |
| Claude Sonnet 5.5 (high) | 100.0% | — | — | — | — | — |
| Claude Sonnet 5.5 (low) | 100.0% | — | — | — | — | — |
| Claude Sonnet 5.5 (max) | 100.0% | — | — | — | — | — |
| Claude Sonnet 5.5 (medium) | 100.0% | — | — | — | — | — |
| Claude Sonnet 5.5 (xhigh) | 100.0% | — | — | — | — | — |
| DeepSeek V4 Pro (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GLM-5.3 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-5.6 Luna (max) | 0.0% | — | — | — | — | — |
| GPT-5.6 Sol (max) | 0.0% | — | — | — | — | — |
| GPT-6 Astra (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 9.6% |
| GPT-6 Luna (max) | 100.0% | — | — | — | — | — |
| GPT-6 Sol (max) | 0.0% | — | — | — | — | — |
| GPT-6.1 Sol (high) | 100.0% | — | — | — | — | — |
| GPT-6.1 Sol (low) | 0.0% | — | — | — | — | — |
| GPT-6.1 Sol (max) | 0.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% |
| GPT-6.1 Sol (medium) | 0.0% | — | — | — | — | — |
| GPT-6.1 Sol (xhigh) | 100.0% | — | — | — | — | — |
| Gemini 3.8 Flash (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Gemini 4 Argon (high) | 0.0% | 100.0% | 84.6% | 100.0% | 100.0% | 61.1% |
| Grok 4.7 (xhigh) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Muse Spark 1.3 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Qwen3.8 Max | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |

### Plan basis: value-score dispersion (SD; covariance term)

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M | S1T |
|---|---:|---:|---:|---:|---:|---:|
| Claude Fable 5.1 (max) | 0.00 (+0.00) | 0.00 (+0.00) | 0.75 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.24 (+0.00) |
| Claude Haiku 5.5 (high) | 0.00 (+0.00) | — | — | — | — | — |
| Claude Haiku 5.5 (low) | 0.00 (+0.00) | — | — | — | — | — |
| Claude Haiku 5.5 (max) | 0.00 (+0.00) | — | — | — | — | — |
| Claude Haiku 5.5 (medium) | 0.00 (+0.00) | — | — | — | — | — |
| Claude Haiku 5.5 (xhigh) | 0.00 (+0.00) | — | — | — | — | — |
| Claude Opus 5 (max) | 0.00 (+0.00) | — | — | — | — | — |
| Claude Opus 5.5 (max) | 0.00 (+0.00) | 0.00 (+0.00) | 0.81 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.21 (+0.00) |
| Claude Sonnet 5.5 (high) | 0.00 (+0.00) | — | — | — | — | — |
| Claude Sonnet 5.5 (low) | 0.00 (+0.00) | — | — | — | — | — |
| Claude Sonnet 5.5 (max) | 0.00 (+0.00) | — | — | — | — | — |
| Claude Sonnet 5.5 (medium) | 0.00 (+0.00) | — | — | — | — | — |
| Claude Sonnet 5.5 (xhigh) | 0.00 (+0.00) | — | — | — | — | — |
| DeepSeek V4 Pro (max) | 0.00 (+0.00) | 0.00 (+0.00) | 1.33 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.20 (+0.00) |
| GLM-5.3 (max) | 0.00 (+0.00) | 0.00 (+0.00) | 1.13 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.26 (+0.00) |
| GPT-5.6 Luna (max) | 0.00 (+0.00) | — | — | — | — | — |
| GPT-5.6 Sol (max) | 0.00 (+0.00) | — | — | — | — | — |
| GPT-6 Astra (max) | 0.00 (+0.00) | 0.00 (+0.00) | 0.76 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.22 (+0.00) |
| GPT-6 Luna (max) | 0.00 (+0.00) | — | — | — | — | — |
| GPT-6 Sol (max) | 0.00 (+0.00) | — | — | — | — | — |
| GPT-6.1 Sol (high) | 0.00 (+0.00) | — | — | — | — | — |
| GPT-6.1 Sol (low) | 0.00 (+0.00) | — | — | — | — | — |
| GPT-6.1 Sol (max) | 0.00 (+0.00) | 0.00 (+0.00) | 0.79 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.21 (+0.00) |
| GPT-6.1 Sol (medium) | 0.00 (+0.00) | — | — | — | — | — |
| GPT-6.1 Sol (xhigh) | 0.00 (+0.00) | — | — | — | — | — |
| Gemini 3.8 Flash (high) | 0.00 (+0.00) | 0.00 (+0.00) | 1.50 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.18 (+0.00) |
| Gemini 4 Argon (high) | 0.00 (+0.00) | 0.00 (+0.00) | 1.15 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.13 (+0.00) |
| Grok 4.7 (xhigh) | 0.00 (+0.00) | 0.00 (+0.00) | 1.49 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.16 (+0.00) |
| Muse Spark 1.3 (max) | 0.00 (+0.00) | 0.00 (+0.00) | 1.24 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.19 (+0.00) |
| Qwen3.8 Max | 0.00 (+0.00) | 0.00 (+0.00) | 0.84 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.29 (+0.00) |

### Named S2 specification branches

- **Bug Hunt harness band (E19)** (S2): unevaluable; the captured tbench.ai leaderboard lists no configuration under two or more agents, so no cross-agent spread exists
- **cache-hit variation (E34)** (S2): unevaluable; AA's published cost embeds its cache-pricing protocol; varying the cache-hit rate needs each basket component's cache-read and uncached-input demand, which AA publishes only for the whole Index (E157)
- **first-party list versus cross-provider median price rule (E122)** (S2): unevaluable; AA publishes one price per configuration under its own rule; the alternative rule's prices are not captured

### Cheapest-above-the-bar labels (API basis)

The 90% rule's error bound holds per published event (candidate and kernel assignment); it is not corrected across the listed candidates (E198). Each kernel assignment code gives the kernel used for the candidate and the competitors, in that order (U uniform, H endpoint-heavy; a quality-level bar has no reference rows, so it takes no letter); the label needs every assignment met.

| Bar | Candidate | Reading | Frequency range | Kernel assignments | Label |
|---|---|---|---|---|---|
| quality 55.3 | GPT-6.1 Sol (medium) | supported under all registered role-group kernel checks | 100.0% to 100.0% | UU met, UH met, HU met, HH met | yes |
| quality 47.4 | GPT-5.6 Luna (max) | not scenario-supported | 49.6% to 51.3% | UU not met, UH not met, HU not met, HH not met | no |
| quality 47.4 | GPT-6 Luna (max) | not scenario-supported | 48.7% to 50.4% | UU not met, UH not met, HU not met, HH not met | no |
| quality 59.6 | GPT-6.1 Sol (xhigh) | not scenario-supported | 49.9% to 51.3% | UU not met, UH not met, HU not met, HH not met | no |
| quality 59.6 | GPT-6.1 Sol (high) | not scenario-supported | 49.4% to 50.2% | UU not met, UH not met, HU not met, HH not met | no |

## Diagnostics

- **Terminal-Bench cross-source agreement (AA's mini-SWE-agent run against tbench.ai):** defined; 0 rows take the leaf from tbench.ai (gap fill).
- **Rank separability (O39, independent-task approximation):** median separation 3.34 value points (API) and 3.35 (Plan); separable adjacent ranks: API 0 of 30, Plan 0 of 30. Assumptions: tasks are independent and each leaf's score is a mean over its published task count (plug-in binomial); attempts averaged within a task and tasks shared across models are ignored, so the noise is approximate; GDPval-AA: AA's displayed rating interval (-26/+26 Elo for Claude Opus 5.5) read as a 95% normal interval, SD 13.3 Elo for every row; AA-Omniscience: each of 6,000 questions scores +1, 0 or -1, with the shares from AA's accuracy and hallucination rate.
- **FrontierCode against Cognition:** FrontierCode cross-source agreement (AA against Cognition, same name and effort; E234): Kendall tau 0.73 (interval 0.41 to 1.00) on 10 rows. Cognition minus AA: mean +2.5 points, largest 11.8.
- **Gap-fill removal (E234, diagnostic; scores unchanged):** with these leaves removed and the rest renormalised — GPT-6.1 Sol (xhigh) (FrontierCode 1.1); GPT-6.1 Sol (high) (FrontierCode 1.1); GPT-6.1 Sol (medium) (FrontierCode 1.1); GPT-5.6 Sol (max) (FrontierCode 1.1); GPT-6 Sol (max) (FrontierCode 1.1); MiMo-V2.6-Pro (DeepSWE v1.1); GPT-6.1 Sol (low) (FrontierCode 1.1); GPT-5.6 Luna (max) (FrontierCode 1.1); Claude Opus 5 (max) (FrontierCode 1.1) — API 11 rows move; largest move 6 (MiMo-V2.6-Pro); Plan 15 rows move; largest move 8 (MiMo-V2.6-Pro).
- **Bar results without the gap fills (E234, sensitivity; labels unchanged):** cheapest displayed row as published, with fills removed, and with third-party fills lowered by the mean offset 2.5 points — API quality 55.3: GPT-6.1 Sol (medium) in all three; API quality 47.4: GPT-6 Luna (max) in all three; API quality 59.6: GPT-6.1 Sol (high) as published, GPT-6.1 Sol (high) with the fills removed, GPT-6.1 Sol (xhigh) with third-party fills lowered by the offset; Plan quality 55.3: Claude Sonnet 5.5 (high) in all three; Plan quality 47.4: GPT-6 Luna (max) in all three; Plan quality 59.6: GPT-6.1 Sol (high) as published, GPT-6.1 Sol (high) with the fills removed, GPT-6.1 Sol (xhigh) with third-party fills lowered by the offset.
- **Quality agreement:** quality agreement (matched-panel sensitivity): Kendall tau 0.71 (interval 0.57 to 0.83) on 32 rows.
- **Quality-substitution value agreement (API):** quality-substitution value agreement, api basis (matched-panel sensitivity): Kendall tau 0.59 (interval 0.39 to 0.76) on 31 rows.
- **Quality-substitution value agreement (Plan):** quality-substitution value agreement, plan basis (matched-panel sensitivity): Kendall tau 0.61 (interval 0.40 to 0.77) on 31 rows.
- **Disjoint-evidence agreement:** disjoint-evidence agreement (restricted evidence comparison, not an eligible ranking): Kendall tau 0.66 (interval 0.51 to 0.79) on 32 rows.
- **Quality source shares:** AA-run 90%, independent 10%.
- **Non-discriminating leaves:** none.
- **Group drift:** estimated; flagged: knowledge.
- **Omniscience abstention sensitivity** (z_pen = max(0, I)): 12 rows move; largest move 2 (Claude Fable 5.1 (max), Claude Haiku 5.5 (low), DeepSeek V4 Pro (max), Gemini 4 Argon (high), GPT-5.6 Luna (max), GPT-6 Luna (max), Grok 4.7 (xhigh), MiMo-V2.6-Pro).
- **GDPval-AA logistic sensitivity** (z = 100 / (1 + 10^((1600 - E) / 400)) against AA's pinned anchor; every other input fixed): API 26 rows move; largest move 5 (Grok 4.7 (xhigh)); Plan 19 rows move; largest move 6 (Claude Fable 5.1 (max)).
- **Anchor stability:** trimmed anchors (P10 / 2 and P90 x 2 (diagnostic only)) give $85.83 to $14,213.29; 19 rows move; largest move 9 (Claude Haiku 5.5 (medium)).

- **Basket readiness (E22):** priced leaves cover 67% of nominal quality weight (AutomationBench-AA, DeepSWE v1.1, GDPval-AA v2.1, AA-LCR v1.1, SciCode, Terminal-Bench 4.0 (AA run)); pending components: FrontierCode, ITBench-AA.
- **SWE cost companion (O14, diagnostic):** 30 rows evaluated; flagged far from the median ratio: Claude Haiku 5.5 (max).
- **Matched-cost diagnostic (E55):** evaluated at 50% priced quality weight; basket/matched cost-order reversals with separated intervals: 14; rank-gap warnings: 2.
- **Frontier-families anchors (E187, diagnostic):** anchors rebuilt from the 8 frontier and near-frontier references move API 12 rows move; largest move 7 (Claude Haiku 5.5 (medium), Claude Opus 5.5 (max)) (value points per cost doubling 3.04 vs 2.74 frozen); Plan 26 rows move; largest move 7 (Claude Haiku 5.5 (high)) (value points per cost doubling 2.17 vs 1.73 frozen).
- **Frontier-families bar (E199, sensitivity; the frozen bar stays primary):** quality 61.0 over 9 configurations; cheapest at or above it on the API main workload: GPT-6.1 Sol (xhigh) (confirmed) (compares 6 configurations that can qualify).
- **One row per family (E205, diagnostic; the frozen ladder and anchors stay primary):** with each family's primary configuration only (20 rows in the one-row-per-family bar population), the ladder (headline, lower quartile, upper quartile) would be 55.9 / 48.9 / 61.0 against 55.3 / 47.4 / 59.6 frozen; anchors rebuilt from its 17 references move API 12 rows move; largest move 7 (Claude Haiku 5.5 (medium), Claude Opus 5.5 (max)) (value points per cost doubling 3.04 vs 2.74 frozen); Plan 19 rows move; largest move 5 (Claude Haiku 5.5 (high), Gemini 4 Argon (high), GPT-6 Astra (max)) (value points per cost doubling 2.02 vs 1.73 frozen).
- **Bar currency (E207, informational):** rows reaching each frozen bar: quality 55.3: 17 of 32; quality 47.4: 25 of 32; quality 59.6: 9 of 32; the current population would freeze 55.3 / 47.4 / 59.6; lifetime until the next anchor re-freeze or methodology version, whichever comes first; no staleness flag.
- **Token mix (E208):** 1 selected routes: mix not reported: the measurement publishes no token-category shares; 23 selected routes: mix unidentified: the basket's token-category shares are set-identified only (E124), so the L1 test (above 0.30 flags mix-unmatched) is not computed.
- **Observed-range sensitivity (E219, not evidence; no label changes):** with each missing leaf inside the cohort's observed range for that leaf, quality 55.3: 15 can qualify, 14 confirmed; GPT-6.1 Sol (medium) confirmed cheapest; quality 47.4: 22 can qualify, 21 confirmed; possibly cheapest GPT-5.6 Luna (max), GPT-6 Luna (max); quality 59.6: 7 can qualify, 6 confirmed; possibly cheapest GPT-6.1 Sol (xhigh), GPT-6.1 Sol (high).
- **What would settle the headline bar (E221, not a claim):** rows that can but need not reach quality 55.3, with the mean score their missing leaves would need: Claude Sonnet 5.5 (high) (no missing leaf; reporting precision only).
- **Common leaf set (E226, diagnostic; scores unchanged):** without the leaves fewer than 90% of cohort rows have (none), API no rank changes; Plan no rank changes; rows reaching each bar: quality 55.3: 17 → 17; quality 47.4: 25 → 25; quality 59.6: 9 → 9; rows whose displayed quality differs from common-leaf quality by more than one cost doubling's worth: none.
- **Harness by leaf (E227):** DeepSWE: Claude Code 14, Codex 11, Muse Code 2, Antigravity CLI 1, Antigravity SDK 1, Grok Build 1, Opencode 1; Terminal-Bench: mini-SWE-agent 32; Bug Hunt: Claude Code 13, Codex CLI 10, Antigravity CLI 2, Muse Code / Meta API 2, Claude Code / Alibaba API 1, Claude Code / Anthropic-compatible shim 1, Claude Code / DeepSeek API 1, Claude Code / Z.ai API 1, Grok Build CLI (ACP) 1.

### Leave-one-component-out cost family (E172)

Each admitted basket unit removed in turn, scored on anchors rebuilt by the freeze rule (rank changes against the primary ranking; quality held fixed).

| Removed component | API rank changes | Plan rank changes | API value points per cost doubling |
|---|---|---|---:|
| Coding Agent Index | 21 rows move; largest move 9 (Claude Haiku 5.5 (max)) | 12 rows move; largest move 6 (Claude Sonnet 5.5 (low)) | 2.47 |
| AA-Briefcase | 9 rows move; largest move 2 (Claude Sonnet 5.5 (medium), GPT-5.6 Luna (max), GPT-5.6 Sol (max)) | 13 rows move; largest move 3 (Claude Sonnet 5.5 (high)) | 2.73 |
| GDPval-AA | 2 rows move; largest move 1 (Gemini 4 Argon (high), GPT-6.1 Sol (low)) | 8 rows move; largest move 3 (Claude Fable 5.1 (max), Gemini 4 Argon (high)) | 2.75 |
| GDP.pdf | 3 rows move; largest move 2 (GPT-6 Luna (max)) | no rank changes | 2.68 |
| AutomationBench-AA | 13 rows move; largest move 2 (DeepSeek V4 Pro (max)) | 6 rows move; largest move 1 (Claude Fable 5.1 (max), Claude Haiku 5.5 (high), Gemini 4 Argon (high), GPT-5.6 Luna (max), GPT-6.1 Sol (high), GPT-6.1 Sol (medium)) | 2.68 |
| Terminal-Bench 4.0 (AA Index run) | 8 rows move; largest move 2 (DeepSeek V4 Pro (max), Gemini 4 Argon (high)) | 11 rows move; largest move 2 (GPT-5.6 Luna (max)) | 2.68 |
| SciCode | 3 rows move; largest move 2 (Gemini 4 Argon (high)) | no rank changes | 2.68 |
| AA-LCR | 2 rows move; largest move 2 (Gemini 4 Argon (high), GPT-6 Luna (max)) | no rank changes | 2.67 |

### Subset rows: paired bridge and missing spend (E10, E173)

- **MiMo-V2.6-Pro** (subset without Coding Agent Index): Coding Agent Index is 40% of the full basket (median; 9% to 80% over 30 rows). Scored on its own subset anchors, the direction of its subset effect is not known. Paired bridge on the 30 full rows: API: the full rows' values change by -0.50 points (median; -2.32 to 3.39), 15 rows move; largest move 9 (Claude Haiku 5.5 (max)); Plan: the full rows' values change by -0.38 points (median; -1.19 to 2.04), 12 rows move; largest move 6 (Claude Sonnet 5.5 (low)).

### Deletion sensitivity

| Branch | Retained nominal weight | Status | API rank changes | Plan rank changes |
|---|---:|---|---|---|
| leave-out:deepswe | 70% | evaluated | 28 rows move; largest move 8 (GPT-5.6 Luna (max)) | 29 rows move; largest move 10 (Claude Fable 5.1 (max)) |
| leave-out:bugHunt | 90% | evaluated | 15 rows move; largest move 3 (Claude Fable 5.1 (max), GPT-5.6 Sol (max)) | 18 rows move; largest move 3 (MiMo-V2.6-Pro) |
| leave-out:frontierCode | 90% | evaluated | 21 rows move; largest move 3 (Claude Sonnet 5.5 (low), Claude Sonnet 5.5 (medium)) | 18 rows move; largest move 3 (Claude Haiku 5.5 (xhigh), Gemini 4 Argon (high), GPT-6 Astra (max)) |
| leave-out:terminalBench | 90% | evaluated | 24 rows move; largest move 6 (GPT-6 Astra (max)) | 24 rows move; largest move 8 (GPT-5.6 Luna (max)) |
| leave-out:gdpval | 90% | evaluated | 18 rows move; largest move 3 (Claude Opus 5.5 (max), Claude Sonnet 5.5 (medium)) | 20 rows move; largest move 3 (Claude Opus 5 (max), Claude Opus 5.5 (max), GPT-6.1 Sol (medium)) |
| leave-out:automationBench | 90% | evaluated | 12 rows move; largest move 5 (Claude Haiku 5.5 (xhigh)) | 12 rows move; largest move 5 (Claude Haiku 5.5 (xhigh)) |
| leave-out:omniscience | 90% | evaluated | 15 rows move; largest move 2 (Claude Fable 5.1 (max), DeepSeek V4 Pro (max), Gemini 3.8 Flash (high), GLM-5.3 (max), GPT-5.6 Sol (max)) | 19 rows move; largest move 4 (Claude Sonnet 5.5 (low)) |
| leave-out:lcr | 95% | evaluated | 8 rows move; largest move 2 (Gemini 4 Argon (high), GPT-5.6 Luna (max)) | 13 rows move; largest move 3 (Claude Fable 5.1 (max)) |
| leave-out:hle | 98% | evaluated | 6 rows move; largest move 1 (DeepSeek V4 Pro (max), Gemini 3.8 Flash (high), Gemini 4 Argon (high), GPT-6.1 Sol (high), GPT-6.1 Sol (low), MiMo-V2.6-Pro) | 2 rows move; largest move 1 (Claude Opus 5.5 (max), Claude Sonnet 5.5 (xhigh)) |
| leave-out:scicode | 98% | evaluated | 6 rows move; largest move 1 (Claude Opus 5.5 (max), Gemini 4 Argon (high), GPT-6 Astra (max), GPT-6.1 Sol (high), GPT-6.1 Sol (low), MiMo-V2.6-Pro) | 6 rows move; largest move 1 (Claude Opus 5.5 (max), Claude Sonnet 5.5 (low), Claude Sonnet 5.5 (xhigh), Gemini 4 Argon (high), GPT-6 Astra (max), GPT-6 Luna (max)) |
| leave-out:critpt | 98% | evaluated | 4 rows move; largest move 1 (Claude Haiku 5.5 (high), Claude Haiku 5.5 (medium), Gemini 4 Argon (high), GPT-6.1 Sol (low)) | 4 rows move; largest move 1 (Claude Fable 5.1 (max), Claude Haiku 5.5 (high), Claude Sonnet 5.5 (low), Gemini 4 Argon (high)) |
| leave-source-out:Artificial Analysis | 10% | not identifiable under the coverage rule | — | — |
| basket-scope | 87% | evaluated | 16 rows move; largest move 2 (Claude Fable 5.1 (max), DeepSeek V4 Pro (max), Gemini 3.8 Flash (high), GLM-5.3 (max), GPT-5.6 Sol (max), GPT-6 Astra (max)) | 18 rows move; largest move 3 (Claude Opus 5 (max), Claude Sonnet 5.5 (high), GPT-5.6 Luna (max), MiMo-V2.6-Pro) |

### Cost-component removal (Terminal-Bench 4.0 (AA Index run): evaluated)

| Basis | Run | Rank changes |
|---|---|---|
| api | cost-component removal, original anchors | 6 rows move; largest move 2 (Claude Fable 5.1 (max), DeepSeek V4 Pro (max)) |
| api | alternative workload, recalibrated anchors | 8 rows move; largest move 2 (DeepSeek V4 Pro (max), Gemini 4 Argon (high)) |
| plan | cost-component removal, original anchors; fixed-multiple arithmetic stress (not identified Plan economics for the altered workload) | 9 rows move; largest move 2 (GPT-5.6 Luna (max)) |
| plan | alternative workload, recalibrated anchors; fixed-multiple arithmetic stress (not identified Plan economics for the altered workload) | 11 rows move; largest move 2 (GPT-5.6 Luna (max)) |

## Release gates

| Rule | Status | Detail |
|---|---|---|
| clip gate (E20) | passed | no basis exceeds the clipping allowance |
| cost influence flag (E91) | passed | cost not discriminating (< 10%); informational only; beta never changes (O2) |
| quality influence flag (E126) | passed | quality not discriminating (cost share > 90%); informational only |
| subset scoring (O17) | fired | subset rows scored on their own workload and anchors |
| partial component flag (E37) | fired | AA declined- or missing-task markers, or an Index reconstruction that misses AA's total (E209) |
| route dominance filter (E88) | vacuous | certifiably dearer routes set aside |
| Plan exploratory label (E61) | fired | fewer than half of Plan rows have an identified M_W |
| score swing gate (E177) | vacuous | first v3 release: no previous v3 release to compare |
| anchor migration (E184) | vacuous | no main-workload migration deferred |
| configuration map coverage | passed | every cohort row has a pinned identity |
| quality clipping audit (E110) | passed | saturation disclosed; domain violations block the build |
| full benchmark set (O36, O38) | fired | listed, not ranked: deepseek-v4-flash, grok-4.6-xhigh, mimo-v2-6-flash, muse-spark-1-3-xhigh, muse-wonder |
| missing-leaf rules (O8 provisional, E198b, E201b, E219, E221, E226) | vacuous | no ranked row has a missing leaf (O36) |
| S1M interval stream (E145) | vacuous | dormant: no ranked leaf carries a published confidence interval since O37, so S1M equals S1 (E236) |
| provider-claim label denial (E233) | fired | competes, earns no label: mimo-v2-6-pro |
| scenario outputs current (E72) | passed | scenario input hash matches the scored inputs |
