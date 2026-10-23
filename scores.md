# ValueRank v3.0.0 Scores

**Updated:** October 19, 2026 · methodology 3.0.0 · SDLC basket v1 · anchor version `v3-2026-10-23`

Value = 25% × cost score + 75% × quality. Costs are USD per basket run; the cost score is log-scaled against the frozen anchors of the row's workload (see [methodology.md](methodology.md)).

## Ranking

| Configuration | Plan rank | Plan value | Plan cost score | API rank | API value | API cost score | Quality | Quality coverage | Workload |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| [Claude Opus 5.5 (xhigh)](https://valuerank.alolabs.dev/models/claude-opus-5-5-xhigh/) | 1 | 53.95 | 43.22 | 9 | 47.15 | 16.00 | 57.53 | 100% | main |
| [Claude Opus 5.5 (high)](https://valuerank.alolabs.dev/models/claude-opus-5-5-high/) | 4 | 53.81 | 49.39 | 8 | 47.33 | 23.48 | 55.28 | 100% | main |
| [Claude Opus 5.5 (medium)](https://valuerank.alolabs.dev/models/claude-opus-5-5-medium/) | 7 | 53.71 | 52.16 | 7 | 47.38 | 26.84 | 54.23 | 100% | main |
| [Claude Sonnet 5.5 (max)](https://valuerank.alolabs.dev/models/claude-sonnet-5-5/) | 9 | 53.69 | 39.00 | 12 | 46.66 | 10.89 | 58.58 | 100% | main |
| [Claude Opus 5.5 (max)](https://valuerank.alolabs.dev/models/claude-opus-5-5/) | 13 | 53.49 | 37.19 | 13 | 46.37 | 8.70 | 58.93 | 100% | main |
| [Claude Sonnet 5.5 (xhigh)](https://valuerank.alolabs.dev/models/claude-sonnet-5-5-xhigh/) | 16 | 52.33 | 49.58 | 14 | 45.86 | 23.71 | 53.25 | 100% | main |
| [GPT-6.1 Sol (max)](https://valuerank.alolabs.dev/models/gpt-6-1-sol/) | 19 | 51.63 | 40.58 | 2 | 50.01 | 34.12 | 55.31 | 100% | main |
| [GPT-6.1 Sol (xhigh)](https://valuerank.alolabs.dev/models/gpt-6-1-sol-xhigh/) | 22 | 51.55 | 45.15 | 1 | 50.18 | 39.67 | 53.68 | 100% | main |
| [GPT-6.1 Sol (high)](https://valuerank.alolabs.dev/models/gpt-6-1-sol-high/) | 26 | 50.84 | 46.94 | 3 | 49.56 | 41.83 | 52.14 | 100% | main |
| [Claude Haiku 5.5 (xhigh)](https://valuerank.alolabs.dev/models/claude-haiku-5-5/) | 31 | 49.49 | 78.97 | 17 | 44.58 | 59.31 | 39.66 | 100% | main |
| [GPT-6.1 Sol (medium)](https://valuerank.alolabs.dev/models/gpt-6-1-sol-medium/) | 34 | 49.21 | 50.09 | 4 | 48.10 | 45.65 | 48.92 | 100% | main |
| [GPT-6 Astra (xhigh)](https://valuerank.alolabs.dev/models/gpt-6-astra-xhigh/) | 37 | 48.98 | 27.19 | 11 | 46.66 | 17.91 | 56.24 | 100% | main |
| [Claude Haiku 5.5 (max)](https://valuerank.alolabs.dev/models/claude-haiku-5-5-max/) | 40 | 48.88 | 72.95 | 18 | 43.64 | 52.02 | 40.85 | 100% | main |
| [GPT-6 Astra (max)](https://valuerank.alolabs.dev/models/gpt-6-astra/) | 43 | 48.67 | 27.34 | 16 | 45.43 | 14.37 | 55.79 | 100% | main |
| [Claude Haiku 5.5 (high)](https://valuerank.alolabs.dev/models/claude-haiku-5-5-high/) | 48 | 48.10 | 83.25 | 19 | 43.42 | 64.50 | 36.39 | 100% | main |
| [GPT-6 Astra (high)](https://valuerank.alolabs.dev/models/gpt-6-astra-high/) | 51 | 47.65 | 29.23 | 15 | 45.44 | 20.38 | 53.79 | 100% | main |
| [Claude Haiku 5.5 (medium)](https://valuerank.alolabs.dev/models/claude-haiku-5-5-medium/) | 56 | 46.13 | 87.74 | 21 | 41.68 | 69.94 | 32.26 | 100% | main |
| [GPT-6 Luna (max)](https://valuerank.alolabs.dev/models/gpt-6-luna/) | 59 | 43.61 | 64.44 | 20 | 43.26 | 63.04 | 36.67 | 100% | main |
| [Claude Haiku 5.5 (low)](https://valuerank.alolabs.dev/models/claude-haiku-5-5-low/) | 62 | 43.46 | 92.82 | 25 | 39.28 | 76.10 | 27.00 | 100% | main |
| [Gemini 4 Argon (high)](https://valuerank.alolabs.dev/models/gemini-4-argon/) | 65 | 43.04 | 7.18 | 10 | 47.12 | 23.50 | 54.99 | 100% | main |
| [MiMo-V2.6-Pro](https://valuerank.alolabs.dev/models/mimo-v2-6-pro/) | 67 | 42.51 | 35.98 | 5 | 47.59 | 56.30 | 44.69 | 100% | main |
| [DeepSeek V4.1 Flash 1017 (max)](https://valuerank.alolabs.dev/models/deepseek-v4-1-flash-1017/) | 68 | 42.39 | 25.27 | 6 | 47.43 | 45.41 | 48.10 | 100% | main |
| [GPT-6 Luna (xhigh)](https://valuerank.alolabs.dev/models/gpt-6-luna-xhigh/) | 72 | 41.08 | 69.38 | 22 | 40.99 | 69.02 | 31.64 | 100% | main |
| [GPT-6 Luna (high)](https://valuerank.alolabs.dev/models/gpt-6-luna-high/) | 76 | 40.20 | 72.27 | 23 | 40.27 | 72.52 | 29.52 | 100% | main |
| [GPT-6 Luna (medium)](https://valuerank.alolabs.dev/models/gpt-6-luna-medium/) | 80 | 39.36 | 76.33 | 24 | 39.64 | 77.44 | 27.04 | 100% | main |
| [GPT-6 Luna (low)](https://valuerank.alolabs.dev/models/gpt-6-luna-low/) | 84 | 34.95 | 87.77 | 26 | 35.83 | 91.30 | 17.34 | 100% | main |
| [GPT-5.6 Luna (low)](https://valuerank.alolabs.dev/models/gpt-5-6-luna-low/) | 88 | 32.31 | 78.39 | 27 | 32.70 | 79.93 | 16.96 | 100% | main |

## Not ranked

| Model | Reasons |
|---|---|
| Claude Fable 5 | No exact-variant AA DeepSWE result in the selected source snapshot; Not a required AA frontier or near-frontier family model |
| Claude Fable 5.1 | No exact-variant AA DeepSWE result in the selected source snapshot; Not a required AA frontier or near-frontier family model |
| Claude Opus 4.8 | No exact-variant AA DeepSWE result in the selected source snapshot; Not a required AA frontier or near-frontier family model |
| Claude Opus 5 | No exact-variant AA DeepSWE result in the selected source snapshot; Not a required AA frontier or near-frontier family model |
| Claude Sonnet 5 | No exact-variant AA DeepSWE result in the selected source snapshot; Not a required AA frontier or near-frontier family model |
| Claude Sonnet 5.5 (high) | No exact-variant AA DeepSWE result in the selected source snapshot; Not a required AA frontier or near-frontier family model |
| Claude Sonnet 5.5 (low) | No exact-variant AA DeepSWE result in the selected source snapshot; Not a required AA frontier or near-frontier family model |
| Claude Sonnet 5.5 (medium) | No exact-variant AA DeepSWE result in the selected source snapshot; Not a required AA frontier or near-frontier family model |
| DeepSeek V4 Flash | No exact-variant AA DeepSWE result in the selected source snapshot; Not a required AA frontier or near-frontier family model |
| DeepSeek V4 Pro | No exact-variant AA DeepSWE result in the selected source snapshot; Not a required AA frontier or near-frontier family model |
| GLM-5.2 | No eligible exact-model Bug Hunt result in the selected source snapshot; No exact-variant AA DeepSWE result in the selected source snapshot; Not a required AA frontier or near-frontier family model |
| GLM-5.3 | No exact-variant AA DeepSWE result in the selected source snapshot; Not a required AA frontier or near-frontier family model |
| GLM-5.3 Flash | No exact-variant AA DeepSWE result in the selected source snapshot; Not a required AA frontier or near-frontier family model |
| GPT-5.5 | No eligible exact-model Bug Hunt result in the selected source snapshot; No exact-variant AA DeepSWE result in the selected source snapshot; Not a required AA frontier or near-frontier family model |
| GPT-5.6 Luna | No exact-variant AA DeepSWE result in the selected source snapshot; Not a required AA frontier or near-frontier family model |
| GPT-5.6 Sol | No exact-variant AA DeepSWE result in the selected source snapshot; Not a required AA frontier or near-frontier family model |
| GPT-6 Sol | No exact-variant AA DeepSWE result in the selected source snapshot; Not a required AA frontier or near-frontier family model |
| GPT-6.1 Sol (low) | No exact-variant AA DeepSWE result in the selected source snapshot; Not a required AA frontier or near-frontier family model |
| Gemini 3.5 Flash | No eligible exact-model Bug Hunt result in the selected source snapshot; No exact-variant AA DeepSWE result in the selected source snapshot; Not a required AA frontier or near-frontier family model |
| Gemini 3.6 Flash | No eligible exact-model Bug Hunt result in the selected source snapshot; No exact-variant AA DeepSWE result in the selected source snapshot; Not a required AA frontier or near-frontier family model |
| Gemini 3.7 Flash | No eligible exact-model Bug Hunt result in the selected source snapshot; No exact-variant AA DeepSWE result in the selected source snapshot; Not a required AA frontier or near-frontier family model |
| Gemini 3.8 Flash | No exact-variant AA DeepSWE result in the selected source snapshot; Not a required AA frontier or near-frontier family model |
| Grok 4.6 | No eligible exact-model Bug Hunt result in the selected source snapshot; No exact-variant AA DeepSWE result in the selected source snapshot; Not a required AA frontier or near-frontier family model |
| Grok 4.6 (xhigh) | No exact-variant AA DeepSWE result in the selected source snapshot; Not a required AA frontier or near-frontier family model |
| Grok 4.7 | No exact-variant AA DeepSWE result in the selected source snapshot; Not a required AA frontier or near-frontier family model |
| Kimi K3 | No eligible exact-model Bug Hunt result in the selected source snapshot; No exact-variant AA DeepSWE result in the selected source snapshot; Not a required AA frontier or near-frontier family model |
| MiMo-V2.6-Flash | Incomplete benchmark evidence after an exhaustive search (O36): no Bug Hunt Bench |
| MiniMax-M3.1-Flash | Incomplete benchmark evidence after an exhaustive search (O36): no Bug Hunt Bench |
| Muse Spark 1.2 | No eligible exact-model Bug Hunt result in the selected source snapshot; No exact-variant AA DeepSWE result in the selected source snapshot; Not a required AA frontier or near-frontier family model |
| Muse Spark 1.3 | No exact-variant AA DeepSWE result in the selected source snapshot; Not a required AA frontier or near-frontier family model |
| Muse Spark 1.3 (xhigh) | No exact-variant AA DeepSWE result in the selected source snapshot; Not a required AA frontier or near-frontier family model |
| Muse Wonder | No exact-variant AA DeepSWE result in the selected source snapshot; Not a required AA frontier or near-frontier family model |
| Muse Wonder Full | No exact-variant AA DeepSWE result in the selected source snapshot; Not a required AA frontier or near-frontier family model |
| Qwen3.8 Max | No exact-variant AA DeepSWE result in the selected source snapshot; Not a required AA frontier or near-frontier family model |

## Quality leaf scores

Each leaf's score z on its fixed 0–100 anchors; "—" marks a leaf with no eligible exact-configuration result.

| Configuration | FrontierCode 1.1 | Terminal-Bench 4.0 (AA run) | Bug Hunt Bench | GDPval-AA v2.1 | AutomationBench-AA | AA-Omniscience | AA-LCR v1.1 | Humanity's Last Exam | SciCode | CritPt | Quality | Provisional |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Claude Opus 5.5 (xhigh) | 53.5 | 59.6 | 34.3 | 66.5 | 65.0 | 71.3 | 84.7 | 57.5 | 65.0 | 31.7 | 57.53 | no |
| Claude Opus 5.5 (high) | 54.0 | 56.6 | 30.2 | 60.2 | 63.2 | 70.3 | 82.7 | 55.6 | 60.4 | 30.9 | 55.28 | no |
| Claude Opus 5.5 (medium) | 57.1 | 52.5 | 28.9 | 54.1 | 61.2 | 70.2 | 84.3 | 54.7 | 59.3 | 27.7 | 54.23 | no |
| Claude Sonnet 5.5 (max) | 45.8 | 63.6 | 48.9 | 66.9 | 71.8 | 66.2 | 82.7 | 55.0 | 61.0 | 31.4 | 58.58 | no |
| Claude Opus 5.5 (max) | 52.2 | 59.6 | 39.7 | 68.3 | 69.5 | 73.2 | 84.7 | 61.4 | 66.9 | 31.7 | 58.93 | no |
| Claude Sonnet 5.5 (xhigh) | 46.1 | 57.1 | 34.3 | 61.4 | 65.5 | 61.8 | 79.7 | 50.0 | 57.3 | 31.1 | 53.25 | no |
| GPT-6.1 Sol (max) | 49.1 | 56.1 | 42.2 | 54.6 | 64.9 | 70.8 | 83.0 | 52.9 | 54.2 | 31.7 | 55.31 | no |
| GPT-6.1 Sol (xhigh) | 46.3 | 54.0 | 40.7 | 51.8 | 66.6 | 70.4 | 79.7 | 52.6 | 55.7 | 31.7 | 53.68 | no |
| GPT-6.1 Sol (high) | 46.6 | 51.5 | 34.8 | 50.4 | 64.5 | 70.7 | 82.3 | 51.4 | 55.8 | 30.0 | 52.14 | no |
| Claude Haiku 5.5 (xhigh) | 45.5 | 29.3 | 17.4 | 50.6 | 36.0 | 53.0 | 78.3 | 42.7 | 51.7 | 22.6 | 39.66 | no |
| GPT-6.1 Sol (medium) | 43.3 | 48.0 | 27.6 | 47.4 | 62.6 | 70.0 | 83.3 | 49.9 | 53.2 | 27.7 | 48.92 | no |
| GPT-6 Astra (xhigh) | 50.6 | 59.6 | 41.0 | 52.8 | 67.2 | 71.7 | 80.0 | 54.6 | 55.7 | 31.4 | 56.24 | no |
| Claude Haiku 5.5 (max) | 41.8 | 32.8 | 20.5 | 55.9 | 35.4 | 55.3 | 82.7 | 44.4 | 55.0 | 18.9 | 40.85 | no |
| GPT-6 Astra (max) | 47.0 | 59.1 | 42.9 | 53.6 | 68.5 | 71.7 | 80.7 | 54.7 | 56.5 | 31.7 | 55.79 | no |
| Claude Haiku 5.5 (high) | 43.6 | 21.7 | 15.2 | 45.8 | 33.7 | 52.9 | 77.3 | 37.3 | 48.7 | 18.6 | 36.39 | no |
| GPT-6 Astra (high) | 50.9 | 54.0 | 33.3 | 51.1 | 66.6 | 71.9 | 80.0 | 53.1 | 55.4 | 28.9 | 53.79 | no |
| Claude Haiku 5.5 (medium) | 40.4 | 15.2 | 11.4 | 38.6 | 28.6 | 52.2 | 77.3 | 33.8 | 49.0 | 12.9 | 32.26 | no |
| GPT-6 Luna (max) | 41.9 | 12.6 | 17.4 | 46.6 | 53.2 | 50.3 | 83.3 | 38.5 | 54.6 | 19.4 | 36.67 | no |
| Claude Haiku 5.5 (low) | 29.3 | 12.6 | 10.5 | 31.0 | 22.9 | 51.6 | 72.0 | 27.0 | 49.2 | 9.1 | 27.00 | no |
| Gemini 4 Argon (high) | 43.5 | 57.1 | 38.8 | 56.2 | 77.5 | 71.2 | 79.7 | 57.1 | 61.8 | 27.1 | 54.99 | no |
| MiMo-V2.6-Pro | 45.4 | 34.8 | 17.1 | 59.2 | 58.6 | 54.2 | 86.3 | 49.4 | 60.9 | 26.6 | 44.69 | no |
| DeepSeek V4.1 Flash 1017 (max) | 43.7 | 33.8 | 40.7 | 62.3 | 66.6 | 52.4 | 82.7 | 43.3 | 55.9 | 24.0 | 48.10 | no |
| GPT-6 Luna (xhigh) | 33.2 | 8.1 | 13.3 | 43.1 | 47.8 | 49.1 | 80.0 | 34.3 | 51.7 | 17.4 | 31.64 | no |
| GPT-6 Luna (high) | 32.0 | 4.5 | 8.6 | 42.0 | 47.8 | 47.2 | 79.3 | 32.9 | 50.3 | 15.4 | 29.52 | no |
| GPT-6 Luna (medium) | 31.8 | 2.5 | 3.8 | 38.1 | 40.5 | 47.5 | 78.3 | 28.3 | 50.9 | 10.6 | 27.04 | no |
| GPT-6 Luna (low) | 14.1 | 0.0 | 3.8 | 26.5 | 12.0 | 45.4 | 74.0 | 20.3 | 46.9 | 2.6 | 17.34 | no |
| GPT-5.6 Luna (low) | 15.4 | 0.0 | 3.8 | 24.6 | 11.7 | 42.7 | 70.0 | 19.8 | 46.1 | 2.6 | 16.96 | no |

## Basket cost by component

USD at API rates for the exact configuration; "—" marks a component without an exact cost.

| Configuration | Coding Agent Index | ITBench-AA | AA-Briefcase | GDPval-AA | GDP.pdf | AutomationBench-AA | Terminal-Bench 4.0 (AA Index run) | SciCode | AA-LCR | Basket cost | Missing admitted components |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Claude Opus 5.5 (xhigh) | — | — | $1,116.22 | $926.56 | $96.43 | $576.87 | $579.37 | $19.46 | $59.89 | $3,374.80 | none |
| Claude Opus 5.5 (high) | — | — | $570.64 | $339.39 | $82.54 | $458.99 | $337.85 | $11.58 | $59.18 | $1,860.17 | none |
| Claude Opus 5.5 (medium) | — | — | $400.24 | $188.41 | $79.53 | $419.46 | $266.84 | $10.22 | $59.00 | $1,423.70 | none |
| Claude Sonnet 5.5 (max) | $3,857.44 | — | $1,863.13 | $1,504.30 | $79.43 | $678.32 | $834.67 | $80.07 | $33.93 | $5,073.84 | none |
| Claude Opus 5.5 (max) | $3,312.59 | $146.00 | $1,915.18 | $1,962.05 | $155.23 | $938.69 | $865.21 | $135.11 | $67.66 | $6,039.13 | none |
| Claude Sonnet 5.5 (xhigh) | — | — | $634.80 | $430.06 | $46.01 | $277.51 | $401.18 | $6.81 | $29.66 | $1,826.03 | none |
| GPT-6.1 Sol (max) | $436.35 | — | $210.45 | $196.57 | $41.99 | $195.01 | $120.30 | $12.50 | $19.94 | $796.76 | none |
| GPT-6.1 Sol (xhigh) | — | — | $94.51 | $122.86 | $36.81 | $164.62 | $67.71 | $6.35 | $19.35 | $512.20 | none |
| GPT-6.1 Sol (high) | — | — | $76.16 | $94.10 | $34.94 | $148.34 | $54.66 | $3.73 | $19.14 | $431.07 | none |
| Claude Haiku 5.5 (xhigh) | — | — | $33.29 | $20.26 | $2.73 | $18.14 | $30.38 | $0.77 | $1.53 | $107.10 | none |
| GPT-6.1 Sol (medium) | — | — | $42.26 | $50.86 | $33.75 | $128.97 | $40.51 | $2.68 | $19.02 | $318.05 | none |
| GPT-6 Astra (xhigh) | — | — | $597.28 | $668.39 | $191.27 | $924.00 | $386.46 | $35.03 | $96.99 | $2,899.42 | none |
| Claude Haiku 5.5 (max) | $775.43 | — | $61.41 | $48.90 | $5.27 | $27.80 | $43.02 | $3.15 | $1.93 | $191.49 | none |
| GPT-6 Astra (max) | $2,040.49 | $133.00 | $864.69 | $996.49 | $207.58 | $1,048.30 | $560.88 | $66.89 | $99.73 | $3,844.56 | none |
| Claude Haiku 5.5 (high) | — | — | $20.29 | $9.59 | $2.26 | $14.91 | $21.88 | $0.43 | $1.50 | $70.85 | none |
| GPT-6 Astra (high) | — | — | $433.48 | $535.08 | $179.48 | $850.94 | $267.10 | $20.04 | $95.97 | $2,382.09 | none |
| Claude Haiku 5.5 (medium) | — | — | $12.10 | $4.56 | $2.06 | $12.57 | $12.79 | $0.34 | $1.49 | $45.91 | none |
| GPT-6 Luna (max) | $46.16 | — | $15.47 | $19.66 | $2.85 | $23.91 | $15.59 | $1.06 | $1.02 | $79.56 | none |
| Claude Haiku 5.5 (low) | — | — | $4.30 | $2.28 | $1.93 | $10.04 | $7.82 | $0.27 | $1.48 | $28.12 | none |
| Gemini 4 Argon (high) | $1,699.83 | — | $530.33 | $400.23 | $25.93 | $399.89 | $447.49 | $30.44 | $23.64 | $1,857.94 | none |
| MiMo-V2.6-Pro | — | — | $34.60 | $35.47 | $2.40 | $27.77 | $28.91 | $2.25 | $4.74 | $136.13 | none |
| DeepSeek V4.1 Flash 1017 (max) | — | — | $61.72 | $77.91 | $4.23 | $114.26 | $58.09 | $4.65 | $3.26 | $324.12 | none |
| GPT-6 Luna (xhigh) | — | — | $7.51 | $10.06 | $2.07 | $15.31 | $13.08 | $0.41 | $0.98 | $49.41 | none |
| GPT-6 Luna (high) | — | — | $5.66 | $7.02 | $1.88 | $13.63 | $7.95 | $0.28 | $0.97 | $37.39 | none |
| GPT-6 Luna (medium) | — | — | $3.01 | $3.73 | $1.74 | $10.89 | $4.72 | $0.20 | $0.96 | $25.26 | none |
| GPT-6 Luna (low) | — | — | $0.55 | $0.83 | $1.66 | $3.86 | $0.36 | $0.15 | $0.96 | $8.37 | none |
| GPT-5.6 Luna (low) | — | — | $1.14 | $1.79 | $3.41 | $11.25 | $0.78 | $0.42 | $1.91 | $20.71 | none |

### Valuation basis

Valuation-basis gate (E170): 27 compatible as captured. AA's Index category costs reconcile exactly with the prices AA displays for each configuration at capture, so its applied prices are the prices in force at the release cutoff. Token metering (E176): 27 not published per configuration; AA values cached input at live measurements of each model's typical cache-hit rate. Source intervals (E174): terminalBench: captured, level 95% (tbench.ai: "The whiskers span the 95% confidence interval"); gdpval: published, not captured, level not stated by the source (the 95% level on AA's methodology page belongs to AA-Briefcase).

## Plan route selection

The Plan amount is the selected multiple times the cash paid for the fee period (E166), typed by what the measurement establishes; it is not capacity unless it says so. The multiple values only the measured workload's API-equivalent consumption; other plan features are not valued.

| Configuration | Selected route | Plan amount | Basket runs per fee period | Identification | Plan cost (USD per basket run) | Flags | Selection reason |
|---|---|---|---|---|---:|---|---|
| Claude Opus 5.5 (xhigh) | Claude Pro $20 · common Claude assumption (58.9×, assumption) | $1,178 per month: assumed API-equivalent consumption (owner-named transfer) from claude-pro-opus55-semianalysis | 0.35 per month | unidentified | $57.30 | workload-unmatched; owner-named transfer (assumption); valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| Claude Opus 5.5 (high) | Claude Pro $20 · common Claude assumption (58.9×, assumption) | $1,178 per month: assumed API-equivalent consumption (owner-named transfer) from claude-pro-opus55-semianalysis | 0.63 per month | unidentified | $31.58 | workload-unmatched; owner-named transfer (assumption); valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| Claude Opus 5.5 (medium) | Claude Pro $20 · common Claude assumption (58.9×, assumption) | $1,178 per month: assumed API-equivalent consumption (owner-named transfer) from claude-pro-opus55-semianalysis | 0.83 per month | unidentified | $24.17 | workload-unmatched; owner-named transfer (assumption); valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| Claude Sonnet 5.5 (max) | Claude Pro $20 · common Claude assumption (58.9×, assumption) | $1,178 per month: assumed API-equivalent consumption (owner-named transfer) from claude-pro-opus55-semianalysis | 0.23 per month | unidentified | $86.14 | workload-unmatched; owner-named transfer (assumption); valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| Claude Opus 5.5 (max) | Claude Pro $20 · Opus 5.5 (58.9×, measured) | $1,178 per month: measured-workload capacity | 0.20 per month | unidentified | $102.53 | workload-unmatched; valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| Claude Sonnet 5.5 (xhigh) | Claude Pro $20 · common Claude assumption (58.9×, assumption) | $1,178 per month: assumed API-equivalent consumption (owner-named transfer) from claude-pro-opus55-semianalysis | 0.65 per month | unidentified | $31.00 | workload-unmatched; owner-named transfer (assumption); valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| GPT-6.1 Sol (max) | ChatGPT Pro 500 $500 · GPT-6.1 Sol (10.772×, measured) | $5,386 per month: measured-workload capacity | 6.76 per month | unidentified | $73.97 | workload-unmatched; valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| GPT-6.1 Sol (xhigh) | ChatGPT Pro 500 $500 · common GPT assumption (10.772×, assumption) | $5,386 per month: assumed API-equivalent consumption (owner-named transfer) from chatgpt-pro500-gpt61sol-semianalysis | 10.52 per month | unidentified | $47.55 | workload-unmatched; owner-named transfer (assumption); valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| GPT-6.1 Sol (high) | ChatGPT Pro 500 $500 · common GPT assumption (10.772×, assumption) | $5,386 per month: assumed API-equivalent consumption (owner-named transfer) from chatgpt-pro500-gpt61sol-semianalysis | 12.49 per month | unidentified | $40.02 | workload-unmatched; owner-named transfer (assumption); valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| Claude Haiku 5.5 (xhigh) | Claude Pro $20 · common Claude assumption (58.9×, assumption) | $1,178 per month: assumed API-equivalent consumption (owner-named transfer) from claude-pro-opus55-semianalysis | 11.00 per month | unidentified | $1.82 | workload-unmatched; owner-named transfer (assumption); valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| GPT-6.1 Sol (medium) | ChatGPT Pro 500 $500 · common GPT assumption (10.772×, assumption) | $5,386 per month: assumed API-equivalent consumption (owner-named transfer) from chatgpt-pro500-gpt61sol-semianalysis | 16.93 per month | unidentified | $29.53 | workload-unmatched; owner-named transfer (assumption); valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| GPT-6 Astra (xhigh) | ChatGPT Pro 500 $500 · common GPT assumption (10.772×, assumption) | $5,386 per month: assumed API-equivalent consumption (owner-named transfer) from chatgpt-pro500-gpt61sol-semianalysis | 1.86 per month | unidentified | $269.16 | workload-unmatched; owner-named transfer (assumption); valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| Claude Haiku 5.5 (max) | Claude Pro $20 · common Claude assumption (58.9×, assumption) | $1,178 per month: assumed API-equivalent consumption (owner-named transfer) from claude-pro-opus55-semianalysis | 6.15 per month | unidentified | $3.25 | workload-unmatched; owner-named transfer (assumption); valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| GPT-6 Astra (max) | ChatGPT Pro 200 $200 · GPT-6 Astra (14.485×, measured) | $2,897 per month: measured-workload capacity | 0.75 per month | unidentified | $265.42 | workload-unmatched; valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| Claude Haiku 5.5 (high) | Claude Pro $20 · common Claude assumption (58.9×, assumption) | $1,178 per month: assumed API-equivalent consumption (owner-named transfer) from claude-pro-opus55-semianalysis | 16.63 per month | unidentified | $1.20 | workload-unmatched; owner-named transfer (assumption); valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| GPT-6 Astra (high) | ChatGPT Pro 500 $500 · common GPT assumption (10.772×, assumption) | $5,386 per month: assumed API-equivalent consumption (owner-named transfer) from chatgpt-pro500-gpt61sol-semianalysis | 2.26 per month | unidentified | $221.14 | workload-unmatched; owner-named transfer (assumption); valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| Claude Haiku 5.5 (medium) | Claude Pro $20 · common Claude assumption (58.9×, assumption) | $1,178 per month: assumed API-equivalent consumption (owner-named transfer) from claude-pro-opus55-semianalysis | 25.66 per month | unidentified | $0.78 | workload-unmatched; owner-named transfer (assumption); valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| GPT-6 Luna (max) | ChatGPT Pro 500 $500 · common GPT assumption (10.772×, assumption) | $5,386 per month: assumed API-equivalent consumption (owner-named transfer) from chatgpt-pro500-gpt61sol-semianalysis | 67.69 per month | unidentified | $7.39 | workload-unmatched; owner-named transfer (assumption); valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| Claude Haiku 5.5 (low) | Claude Pro $20 · common Claude assumption (58.9×, assumption) | $1,178 per month: assumed API-equivalent consumption (owner-named transfer) from claude-pro-opus55-semianalysis | 41.89 per month | unidentified | $0.48 | workload-unmatched; owner-named transfer (assumption); valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| Gemini 4 Argon (high) | — | — | — | — | $1,857.94 | API-cost fallback: no admitted Plan route; cross-estimand ordering not identified | no eligible route |
| MiMo-V2.6-Pro | MiMo Token Plan Max $100 · quota ceiling (provider-derived) (1.1808×, assumption) | $118 per month: assumed API-equivalent consumption (owner-named transfer) | 0.87 per month | unidentified | $115.28 | workload-unmatched; owner-named transfer (assumption); valuation basis unverified; observed-usage multiple; full utilisation not established | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| DeepSeek V4.1 Flash 1017 (max) | — | — | — | — | $324.12 | API-cost fallback: no admitted Plan route; cross-estimand ordering not identified | no eligible route |
| GPT-6 Luna (xhigh) | ChatGPT Pro 500 $500 · common GPT assumption (10.772×, assumption) | $5,386 per month: assumed API-equivalent consumption (owner-named transfer) from chatgpt-pro500-gpt61sol-semianalysis | 109.00 per month | unidentified | $4.59 | workload-unmatched; owner-named transfer (assumption); valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| GPT-6 Luna (high) | ChatGPT Pro 500 $500 · common GPT assumption (10.772×, assumption) | $5,386 per month: assumed API-equivalent consumption (owner-named transfer) from chatgpt-pro500-gpt61sol-semianalysis | 144.04 per month | unidentified | $3.47 | workload-unmatched; owner-named transfer (assumption); valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| GPT-6 Luna (medium) | ChatGPT Pro 500 $500 · common GPT assumption (10.772×, assumption) | $5,386 per month: assumed API-equivalent consumption (owner-named transfer) from chatgpt-pro500-gpt61sol-semianalysis | 213.23 per month | unidentified | $2.34 | workload-unmatched; owner-named transfer (assumption); valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| GPT-6 Luna (low) | ChatGPT Pro 500 $500 · common GPT assumption (10.772×, assumption) | $5,386 per month: assumed API-equivalent consumption (owner-named transfer) from chatgpt-pro500-gpt61sol-semianalysis | 643.22 per month | unidentified | $0.78 | workload-unmatched; owner-named transfer (assumption); valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| GPT-5.6 Luna (low) | ChatGPT Pro 500 $500 · common GPT assumption (10.772×, assumption) | $5,386 per month: assumed API-equivalent consumption (owner-named transfer) from chatgpt-pro500-gpt61sol-semianalysis | 260.07 per month | unidentified | $1.92 | workload-unmatched; owner-named transfer (assumption); valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |

### Route alternatives

Every admissible route-measurement pair in comparator order (E171) and the comparator's pick with the selected pair removed (E179). A larger displayed multiple is arithmetic on the measured workload, never a claim that the route is cheaper on the scored workload. Workday-feasible multiple (E15), for the 25 routed rows: not evaluated: no evidenced quota schema for this route.

| Configuration | Admissible pairs | Unidentified | Pairs (multiple, status) | Leave-selected-out choice |
|---|---:|---:|---|---|
| Claude Opus 5.5 (xhigh) | 3 | 3 | claude-pro-claude-opus-5-5-xhigh-common-opus55-assumption (58.9×, selected); claude-max20x-claude-opus-5-5-xhigh-common-opus55-assumption (58.63×, not selected by the comparator); claude-max5x-claude-opus-5-5-xhigh-common-opus55-assumption (57.25×, not selected by the comparator) | claude-max20x-claude-opus-5-5-xhigh-common-opus55-assumption (58.63×, value 53.94) |
| Claude Opus 5.5 (high) | 3 | 3 | claude-pro-claude-opus-5-5-high-common-opus55-assumption (58.9×, selected); claude-max20x-claude-opus-5-5-high-common-opus55-assumption (58.63×, not selected by the comparator); claude-max5x-claude-opus-5-5-high-common-opus55-assumption (57.25×, not selected by the comparator) | claude-max20x-claude-opus-5-5-high-common-opus55-assumption (58.63×, value 53.80) |
| Claude Opus 5.5 (medium) | 3 | 3 | claude-pro-claude-opus-5-5-medium-common-opus55-assumption (58.9×, selected); claude-max20x-claude-opus-5-5-medium-common-opus55-assumption (58.63×, not selected by the comparator); claude-max5x-claude-opus-5-5-medium-common-opus55-assumption (57.25×, not selected by the comparator) | claude-max20x-claude-opus-5-5-medium-common-opus55-assumption (58.63×, value 53.70) |
| Claude Sonnet 5.5 (max) | 3 | 3 | claude-pro-claude-sonnet-5-5-common-opus55-assumption (58.9×, selected); claude-max20x-claude-sonnet-5-5-common-opus55-assumption (58.63×, not selected by the comparator); claude-max5x-claude-sonnet-5-5-common-opus55-assumption (57.25×, not selected by the comparator) | claude-max20x-claude-sonnet-5-5-common-opus55-assumption (58.63×, value 53.68) |
| Claude Opus 5.5 (max) | 3 | 3 | claude-pro-opus55-semianalysis (58.9×, selected); claude-max20x-opus55-semianalysis (58.63×, not selected by the comparator); claude-max5x-opus55-semianalysis (57.25×, not selected by the comparator) | claude-max20x-opus55-semianalysis (58.63×, value 53.48) |
| Claude Sonnet 5.5 (xhigh) | 3 | 3 | claude-pro-claude-sonnet-5-5-xhigh-common-opus55-assumption (58.9×, selected); claude-max20x-claude-sonnet-5-5-xhigh-common-opus55-assumption (58.63×, not selected by the comparator); claude-max5x-claude-sonnet-5-5-xhigh-common-opus55-assumption (57.25×, not selected by the comparator) | claude-max20x-claude-sonnet-5-5-xhigh-common-opus55-assumption (58.63×, value 52.32) |
| GPT-6.1 Sol (max) | 4 | 4 | chatgpt-pro500-gpt61sol-semianalysis (10.772×, selected); chatgpt-plus-gpt61sol-semianalysis (10.55×, not selected by the comparator); chatgpt-pro100-gpt61sol-semianalysis (10.55×, not selected by the comparator); chatgpt-pro200-gpt61sol-semianalysis (10.42×, not selected by the comparator) | chatgpt-plus-gpt61sol-semianalysis (10.55×, value 51.57) |
| GPT-6.1 Sol (xhigh) | 4 | 4 | chatgpt-pro500-gpt-6.1-sol-xhigh-common-gpt-assumption (10.772×, selected); chatgpt-pro100-gpt-6.1-sol-xhigh-common-gpt-assumption (10.55×, not selected by the comparator); chatgpt-pro200-gpt-6.1-sol-xhigh-common-gpt-assumption (10.42×, not selected by the comparator); chatgpt-plus-gpt-6.1-sol-xhigh-common-gpt-assumption (8.1×, not selected by the comparator) | chatgpt-pro100-gpt-6.1-sol-xhigh-common-gpt-assumption (10.55×, value 51.49) |
| GPT-6.1 Sol (high) | 4 | 4 | chatgpt-pro500-gpt-6.1-sol-high-common-gpt-assumption (10.772×, selected); chatgpt-pro100-gpt-6.1-sol-high-common-gpt-assumption (10.55×, not selected by the comparator); chatgpt-pro200-gpt-6.1-sol-high-common-gpt-assumption (10.42×, not selected by the comparator); chatgpt-plus-gpt-6.1-sol-high-common-gpt-assumption (8.1×, not selected by the comparator) | chatgpt-pro100-gpt-6.1-sol-high-common-gpt-assumption (10.55×, value 50.78) |
| Claude Haiku 5.5 (xhigh) | 3 | 3 | claude-pro-claude-haiku-5-5-common-opus55-assumption (58.9×, selected); claude-max20x-claude-haiku-5-5-common-opus55-assumption (58.63×, not selected by the comparator); claude-max5x-claude-haiku-5-5-common-opus55-assumption (57.25×, not selected by the comparator) | claude-max20x-claude-haiku-5-5-common-opus55-assumption (58.63×, value 49.48) |
| GPT-6.1 Sol (medium) | 4 | 4 | chatgpt-pro500-gpt-6.1-sol-medium-common-gpt-assumption (10.772×, selected); chatgpt-pro100-gpt-6.1-sol-medium-common-gpt-assumption (10.55×, not selected by the comparator); chatgpt-pro200-gpt-6.1-sol-medium-common-gpt-assumption (10.42×, not selected by the comparator); chatgpt-plus-gpt-6.1-sol-medium-common-gpt-assumption (8.1×, not selected by the comparator) | chatgpt-pro100-gpt-6.1-sol-medium-common-gpt-assumption (10.55×, value 49.16) |
| GPT-6 Astra (xhigh) | 4 | 4 | chatgpt-pro500-gpt-6-astra-xhigh-common-gpt-assumption (10.772×, selected); chatgpt-pro100-gpt-6-astra-xhigh-common-gpt-assumption (10.55×, not selected by the comparator); chatgpt-pro200-gpt-6-astra-xhigh-common-gpt-assumption (10.42×, not selected by the comparator); chatgpt-plus-gpt-6-astra-xhigh-common-gpt-assumption (8.1×, not selected by the comparator) | chatgpt-pro100-gpt-6-astra-xhigh-common-gpt-assumption (10.55×, value 48.93) |
| Claude Haiku 5.5 (max) | 3 | 3 | claude-pro-claude-haiku-5-5-max-common-opus55-assumption (58.9×, selected); claude-max20x-claude-haiku-5-5-max-common-opus55-assumption (58.63×, not selected by the comparator); claude-max5x-claude-haiku-5-5-max-common-opus55-assumption (57.25×, not selected by the comparator) | claude-max20x-claude-haiku-5-5-max-common-opus55-assumption (58.63×, value 48.86) |
| GPT-6 Astra (max) | 4 | 4 | chatgpt-pro200-gpt6astra-semianalysis (14.485×, selected); chatgpt-pro500-gpt6astra-semianalysis (13.91×, not selected by the comparator); chatgpt-pro100-gpt6astra-semianalysis (13.22×, not selected by the comparator); chatgpt-plus-gpt6astra-semianalysis (8.1×, not selected by the comparator) | chatgpt-pro500-gpt6astra-semianalysis (13.91×, value 48.57) |
| Claude Haiku 5.5 (high) | 3 | 3 | claude-pro-claude-haiku-5-5-high-common-opus55-assumption (58.9×, selected); claude-max20x-claude-haiku-5-5-high-common-opus55-assumption (58.63×, not selected by the comparator); claude-max5x-claude-haiku-5-5-high-common-opus55-assumption (57.25×, not selected by the comparator) | claude-max20x-claude-haiku-5-5-high-common-opus55-assumption (58.63×, value 48.09) |
| GPT-6 Astra (high) | 4 | 4 | chatgpt-pro500-gpt-6-astra-high-common-gpt-assumption (10.772×, selected); chatgpt-pro100-gpt-6-astra-high-common-gpt-assumption (10.55×, not selected by the comparator); chatgpt-pro200-gpt-6-astra-high-common-gpt-assumption (10.42×, not selected by the comparator); chatgpt-plus-gpt-6-astra-high-common-gpt-assumption (8.1×, not selected by the comparator) | chatgpt-pro100-gpt-6-astra-high-common-gpt-assumption (10.55×, value 47.60) |
| Claude Haiku 5.5 (medium) | 3 | 3 | claude-pro-claude-haiku-5-5-medium-common-opus55-assumption (58.9×, selected); claude-max20x-claude-haiku-5-5-medium-common-opus55-assumption (58.63×, not selected by the comparator); claude-max5x-claude-haiku-5-5-medium-common-opus55-assumption (57.25×, not selected by the comparator) | claude-max20x-claude-haiku-5-5-medium-common-opus55-assumption (58.63×, value 46.12) |
| GPT-6 Luna (max) | 4 | 4 | chatgpt-pro500-gpt-6-luna-common-gpt-assumption (10.772×, selected); chatgpt-pro100-gpt-6-luna-common-gpt-assumption (10.55×, not selected by the comparator); chatgpt-pro200-gpt-6-luna-common-gpt-assumption (10.42×, not selected by the comparator); chatgpt-plus-gpt-6-luna-common-gpt-assumption (8.1×, not selected by the comparator) | chatgpt-pro100-gpt-6-luna-common-gpt-assumption (10.55×, value 43.56) |
| Claude Haiku 5.5 (low) | 3 | 3 | claude-pro-claude-haiku-5-5-low-common-opus55-assumption (58.9×, selected); claude-max20x-claude-haiku-5-5-low-common-opus55-assumption (58.63×, not selected by the comparator); claude-max5x-claude-haiku-5-5-low-common-opus55-assumption (57.25×, not selected by the comparator) | claude-max20x-claude-haiku-5-5-low-common-opus55-assumption (58.63×, value 43.45) |
| MiMo-V2.6-Pro | 4 | 4 | mimo-tokenplan-max-mimo-v2-6-pro-quota-ceiling (1.1808×, selected); mimo-tokenplan-pro-mimo-v2-6-pro-quota-ceiling (1.0944×, not selected by the comparator); mimo-tokenplan-standard-mimo-v2-6-pro-quota-ceiling (0.99×, not selected by the comparator); mimo-tokenplan-lite-mimo-v2-6-pro-quota-ceiling (0.984×, not selected by the comparator) | mimo-tokenplan-pro-mimo-v2-6-pro-quota-ceiling (1.0944×, value 42.32) |
| GPT-6 Luna (xhigh) | 4 | 4 | chatgpt-pro500-gpt-6-luna-xhigh-common-gpt-assumption (10.772×, selected); chatgpt-pro100-gpt-6-luna-xhigh-common-gpt-assumption (10.55×, not selected by the comparator); chatgpt-pro200-gpt-6-luna-xhigh-common-gpt-assumption (10.42×, not selected by the comparator); chatgpt-plus-gpt-6-luna-xhigh-common-gpt-assumption (8.1×, not selected by the comparator) | chatgpt-pro100-gpt-6-luna-xhigh-common-gpt-assumption (10.55×, value 41.02) |
| GPT-6 Luna (high) | 4 | 4 | chatgpt-pro500-gpt-6-luna-high-common-gpt-assumption (10.772×, selected); chatgpt-pro100-gpt-6-luna-high-common-gpt-assumption (10.55×, not selected by the comparator); chatgpt-pro200-gpt-6-luna-high-common-gpt-assumption (10.42×, not selected by the comparator); chatgpt-plus-gpt-6-luna-high-common-gpt-assumption (8.1×, not selected by the comparator) | chatgpt-pro100-gpt-6-luna-high-common-gpt-assumption (10.55×, value 40.15) |
| GPT-6 Luna (medium) | 4 | 4 | chatgpt-pro500-gpt-6-luna-medium-common-gpt-assumption (10.772×, selected); chatgpt-pro100-gpt-6-luna-medium-common-gpt-assumption (10.55×, not selected by the comparator); chatgpt-pro200-gpt-6-luna-medium-common-gpt-assumption (10.42×, not selected by the comparator); chatgpt-plus-gpt-6-luna-medium-common-gpt-assumption (8.1×, not selected by the comparator) | chatgpt-pro100-gpt-6-luna-medium-common-gpt-assumption (10.55×, value 39.31) |
| GPT-6 Luna (low) | 4 | 4 | chatgpt-pro500-gpt-6-luna-low-common-gpt-assumption (10.772×, selected); chatgpt-pro100-gpt-6-luna-low-common-gpt-assumption (10.55×, not selected by the comparator); chatgpt-pro200-gpt-6-luna-low-common-gpt-assumption (10.42×, not selected by the comparator); chatgpt-plus-gpt-6-luna-low-common-gpt-assumption (8.1×, not selected by the comparator) | chatgpt-pro100-gpt-6-luna-low-common-gpt-assumption (10.55×, value 34.89) |
| GPT-5.6 Luna (low) | 4 | 4 | chatgpt-pro500-gpt-5.6-luna-low-common-gpt-assumption (10.772×, selected); chatgpt-pro100-gpt-5.6-luna-low-common-gpt-assumption (10.55×, not selected by the comparator); chatgpt-pro200-gpt-5.6-luna-low-common-gpt-assumption (10.42×, not selected by the comparator); chatgpt-plus-gpt-5.6-luna-low-common-gpt-assumption (8.1×, not selected by the comparator) | chatgpt-pro100-gpt-5.6-luna-low-common-gpt-assumption (10.55×, value 32.26) |

### Measured-only Plan view

Admission: exact-route measurement candidates of grade controlled or concordant reports (no transfers, no diagnostics). Selection: the official selector (E111, E88, E85) rerun among the admitted candidates. Panel: rows with an admitted measured candidate; others listed as 'no measured route' (no API fallback).

| Configuration | Status | Route | Plan cost | Value | Rank |
|---|---|---|---:|---:|---:|
| Claude Opus 5.5 (max) | measured, target-workload unmatched | claude-pro-opus55-semianalysis | $102.53 | 53.49 | 1 |
| GPT-6.1 Sol (max) | measured, target-workload unmatched | chatgpt-pro500-gpt61sol-semianalysis | $73.97 | 51.63 | 2 |
| GPT-6 Astra (max) | measured, target-workload unmatched | chatgpt-pro200-gpt6astra-semianalysis | $265.42 | 48.67 | 3 |
| Claude Haiku 5.5 (high) | no measured route | — | — | — | — |
| Claude Haiku 5.5 (low) | no measured route | — | — | — | — |
| Claude Haiku 5.5 (max) | no measured route | — | — | — | — |
| Claude Haiku 5.5 (medium) | no measured route | — | — | — | — |
| Claude Haiku 5.5 (xhigh) | no measured route | — | — | — | — |
| Claude Opus 5.5 (high) | no measured route | — | — | — | — |
| Claude Opus 5.5 (medium) | no measured route | — | — | — | — |
| Claude Opus 5.5 (xhigh) | no measured route | — | — | — | — |
| Claude Sonnet 5.5 (max) | no measured route | — | — | — | — |
| Claude Sonnet 5.5 (xhigh) | no measured route | — | — | — | — |
| DeepSeek V4.1 Flash 1017 (max) | no measured route | — | — | — | — |
| GPT-5.6 Luna (low) | no measured route | — | — | — | — |
| GPT-6 Astra (high) | no measured route | — | — | — | — |
| GPT-6 Astra (xhigh) | no measured route | — | — | — | — |
| GPT-6 Luna (high) | no measured route | — | — | — | — |
| GPT-6 Luna (low) | no measured route | — | — | — | — |
| GPT-6 Luna (max) | no measured route | — | — | — | — |
| GPT-6 Luna (medium) | no measured route | — | — | — | — |
| GPT-6 Luna (xhigh) | no measured route | — | — | — | — |
| GPT-6.1 Sol (high) | no measured route | — | — | — | — |
| GPT-6.1 Sol (medium) | no measured route | — | — | — | — |
| GPT-6.1 Sol (xhigh) | no measured route | — | — | — | — |
| Gemini 4 Argon (high) | no measured route | — | — | — | — |
| MiMo-V2.6-Pro | no measured route | — | — | — | — |

#### Measured-evidence calibration (diagnostic)

References: each workload's measured-only rows with complete cost evidence are the references: c_L = cheapest / 2, c_H = dearest x 2 (diagnostic only; the official anchors are unchanged). Status: evaluated.

- Workload `1453a9a0576b02ea`: measured anchors $36.98 to $530.83 from Claude Opus 5.5 (max), GPT-6 Astra (max), GPT-6.1 Sol (max); anchor ratio 14.4 against the official 15566.8. Official Plan anchors are set by claude-haiku-5-5-low@claude-pro (not in the current table) at the low end and gemini-4-argon@api (not in the current table) at the high end.

| Configuration | Value on official Plan anchors | Value on measured anchors | Rank change |
|---|---:|---:|---:|
| Claude Opus 5.5 (max) | 53.49 | 59.62 | 1 |
| GPT-6 Astra (max) | 48.67 | 48.34 | 0 |
| GPT-6.1 Sol (max) | 51.63 | 59.98 | -1 |

Pairwise reversals: Claude Opus 5.5 (max) and GPT-6.1 Sol (max). Largest value change: 8.35 points.

## Interval outputs

**API basis, main workload: frontier.** Not evaluable: none.

| Configuration | Possible frontier | Definite frontier | Definite counterexample | Possible frontier blocked by |
|---|---|---|---|---|
| Claude Sonnet 5.5 (max) | certified | certified | — | — |
| Claude Opus 5.5 (max) | certified | certified | — | — |
| DeepSeek V4.1 Flash 1017 (max) | disproved | disproved | GPT-6.1 Sol (medium) | GPT-6.1 Sol (medium) |
| GPT-6.1 Sol (max) | certified | certified | — | — |
| Gemini 4 Argon (high) | disproved | disproved | GPT-6.1 Sol (max) | GPT-6.1 Sol (max) |
| GPT-6 Astra (max) | disproved | disproved | Claude Opus 5.5 (xhigh) | Claude Opus 5.5 (xhigh), GPT-6 Astra (xhigh) |
| Claude Opus 5.5 (xhigh) | certified | certified | — | — |
| GPT-6.1 Sol (xhigh) | certified | certified | — | — |
| GPT-6 Astra (xhigh) | certified | certified | — | — |
| GPT-6.1 Sol (high) | certified | certified | — | — |
| Claude Opus 5.5 (high) | disproved | disproved | GPT-6.1 Sol (max) | GPT-6.1 Sol (max) |
| MiMo-V2.6-Pro | certified | certified | — | — |
| Claude Sonnet 5.5 (xhigh) | disproved | disproved | GPT-6.1 Sol (max) | GPT-6.1 Sol (max), GPT-6.1 Sol (xhigh), Claude Opus 5.5 (medium) |
| Claude Haiku 5.5 (max) | disproved | disproved | MiMo-V2.6-Pro | MiMo-V2.6-Pro |
| Claude Opus 5.5 (medium) | disproved | disproved | GPT-6.1 Sol (max) | GPT-6.1 Sol (max) |
| Claude Haiku 5.5 (xhigh) | certified | certified | — | — |
| GPT-6.1 Sol (medium) | certified | certified | — | — |
| GPT-6 Astra (high) | disproved | disproved | GPT-6.1 Sol (max) | GPT-6.1 Sol (max), Gemini 4 Argon (high), Claude Opus 5.5 (high), Claude Opus 5.5 (medium) |
| GPT-6 Luna (max) | certified | certified | — | — |
| Claude Haiku 5.5 (high) | certified | certified | — | — |
| GPT-6 Luna (xhigh) | disproved | disproved | Claude Haiku 5.5 (medium) | Claude Haiku 5.5 (medium) |
| Claude Haiku 5.5 (medium) | certified | certified | — | — |
| Claude Haiku 5.5 (low) | disproved | disproved | GPT-6 Luna (medium) | GPT-6 Luna (medium) |
| GPT-6 Luna (high) | certified | certified | — | — |
| GPT-6 Luna (medium) | certified | certified | — | — |
| GPT-6 Luna (low) | certified | certified | — | — |
| GPT-5.6 Luna (low) | disproved | disproved | GPT-6 Luna (low) | GPT-6 Luna (low) |

**API basis, main workload: cheapest at or above quality 48.9** (lower-median displayed quality of the non-provisional cohort configurations at freeze (E192; headline bar)). Status certified; confirmed cheapest: none.

Configurations that can be confirmed to qualify: 13 (confirmation needs the full-composite lower bound, with missing leaves at 0, to clear the bar; O25). Cheaper same-family configurations on AA's chart that were not evaluated (not ranked: not plotted on or near the frontier; E201, O51): GPT-6.1 Sol (high): GPT-6.1 Sol (low); GPT-6.1 Sol (medium): GPT-6.1 Sol (low).

Bar comparison: compares 14 configurations that can qualify. The bar is a displayed-quality level; qualification tests each row's full-composite bounds, so a row above the bar on displayed quality can still fail to qualify confirmed when leaves are missing (E198).

| Configuration | Displayed quality − bar | Confirmed qualifies | Possibly qualifies | Possibly cheapest |
|---|---:|---|---|---|
| Claude Sonnet 5.5 (max) | 9.7 | certified | certified | disproved |
| Claude Opus 5.5 (max) | 10.0 | certified | certified | disproved |
| DeepSeek V4.1 Flash 1017 (max) | -0.8 | disproved | disproved | disproved |
| GPT-6.1 Sol (max) | 6.4 | certified | certified | disproved |
| Gemini 4 Argon (high) | 6.1 | certified | certified | disproved |
| GPT-6 Astra (max) | 6.9 | certified | certified | disproved |
| Claude Opus 5.5 (xhigh) | 8.6 | certified | certified | disproved |
| GPT-6.1 Sol (xhigh) | 4.8 | certified | certified | disproved |
| GPT-6 Astra (xhigh) | 7.3 | certified | certified | disproved |
| GPT-6.1 Sol (high) | 3.2 | certified | certified | certified |
| Claude Opus 5.5 (high) | 6.4 | certified | certified | disproved |
| MiMo-V2.6-Pro | -4.2 | disproved | disproved | disproved |
| Claude Sonnet 5.5 (xhigh) | 4.3 | certified | certified | disproved |
| Claude Haiku 5.5 (max) | -8.1 | disproved | disproved | disproved |
| Claude Opus 5.5 (medium) | 5.3 | certified | certified | disproved |
| Claude Haiku 5.5 (xhigh) | -9.3 | disproved | disproved | disproved |
| GPT-6.1 Sol (medium) | 0.0 | disproved | certified | certified |
| GPT-6 Astra (high) | 4.9 | certified | certified | disproved |
| GPT-6 Luna (max) | -12.2 | disproved | disproved | disproved |
| Claude Haiku 5.5 (high) | -12.5 | disproved | disproved | disproved |
| GPT-6 Luna (xhigh) | -17.3 | disproved | disproved | disproved |
| Claude Haiku 5.5 (medium) | -16.7 | disproved | disproved | disproved |
| Claude Haiku 5.5 (low) | -21.9 | disproved | disproved | disproved |
| GPT-6 Luna (high) | -19.4 | disproved | disproved | disproved |
| GPT-6 Luna (medium) | -21.9 | disproved | disproved | disproved |
| GPT-6 Luna (low) | -31.6 | disproved | disproved | disproved |
| GPT-5.6 Luna (low) | -32.0 | disproved | disproved | disproved |

**API basis, main workload: cheapest at or above quality 32.3** (lower-quartile displayed quality of the non-provisional cohort configurations at freeze (O34)). Status certified; confirmed cheapest: none.

Configurations that can be confirmed to qualify: 20 (confirmation needs the full-composite lower bound, with missing leaves at 0, to clear the bar; O25). Cheaper same-family configurations on AA's chart that were not evaluated (not ranked: not plotted on or near the frontier; E201, O51): none.

Bar comparison: compares 21 configurations that can qualify. The bar is a displayed-quality level; qualification tests each row's full-composite bounds, so a row above the bar on displayed quality can still fail to qualify confirmed when leaves are missing (E198).

| Configuration | Displayed quality − bar | Confirmed qualifies | Possibly qualifies | Possibly cheapest |
|---|---:|---|---|---|
| Claude Sonnet 5.5 (max) | 26.3 | certified | certified | disproved |
| Claude Opus 5.5 (max) | 26.7 | certified | certified | disproved |
| DeepSeek V4.1 Flash 1017 (max) | 15.8 | certified | certified | disproved |
| GPT-6.1 Sol (max) | 23.1 | certified | certified | disproved |
| Gemini 4 Argon (high) | 22.7 | certified | certified | disproved |
| GPT-6 Astra (max) | 23.5 | certified | certified | disproved |
| Claude Opus 5.5 (xhigh) | 25.3 | certified | certified | disproved |
| GPT-6.1 Sol (xhigh) | 21.4 | certified | certified | disproved |
| GPT-6 Astra (xhigh) | 24.0 | certified | certified | disproved |
| GPT-6.1 Sol (high) | 19.9 | certified | certified | disproved |
| Claude Opus 5.5 (high) | 23.0 | certified | certified | disproved |
| MiMo-V2.6-Pro | 12.4 | certified | certified | disproved |
| Claude Sonnet 5.5 (xhigh) | 21.0 | certified | certified | disproved |
| Claude Haiku 5.5 (max) | 8.6 | certified | certified | disproved |
| Claude Opus 5.5 (medium) | 22.0 | certified | certified | disproved |
| Claude Haiku 5.5 (xhigh) | 7.4 | certified | certified | disproved |
| GPT-6.1 Sol (medium) | 16.7 | certified | certified | disproved |
| GPT-6 Astra (high) | 21.5 | certified | certified | disproved |
| GPT-6 Luna (max) | 4.4 | certified | certified | disproved |
| Claude Haiku 5.5 (high) | 4.1 | certified | certified | certified |
| GPT-6 Luna (xhigh) | -0.6 | disproved | disproved | disproved |
| Claude Haiku 5.5 (medium) | 0.0 | disproved | certified | certified |
| Claude Haiku 5.5 (low) | -5.3 | disproved | disproved | disproved |
| GPT-6 Luna (high) | -2.7 | disproved | disproved | disproved |
| GPT-6 Luna (medium) | -5.2 | disproved | disproved | disproved |
| GPT-6 Luna (low) | -14.9 | disproved | disproved | disproved |
| GPT-5.6 Luna (low) | -15.3 | disproved | disproved | disproved |

**API basis, main workload: cheapest at or above quality 55.0** (upper-quartile displayed quality of the non-provisional cohort configurations at freeze (O34)). Status certified; confirmed cheapest: GPT-6.1 Sol (max).

Configurations that can be confirmed to qualify: 7 (confirmation needs the full-composite lower bound, with missing leaves at 0, to clear the bar; O25). Cheaper same-family configurations on AA's chart that were not evaluated (not ranked: not plotted on or near the frontier; E201, O51): GPT-6.1 Sol (max): GPT-6.1 Sol (low).

Bar comparison: compares 8 configurations that can qualify. The bar is a displayed-quality level; qualification tests each row's full-composite bounds, so a row above the bar on displayed quality can still fail to qualify confirmed when leaves are missing (E198).

| Configuration | Displayed quality − bar | Confirmed qualifies | Possibly qualifies | Possibly cheapest |
|---|---:|---|---|---|
| Claude Sonnet 5.5 (max) | 3.6 | certified | certified | disproved |
| Claude Opus 5.5 (max) | 3.9 | certified | certified | disproved |
| DeepSeek V4.1 Flash 1017 (max) | -6.9 | disproved | disproved | disproved |
| GPT-6.1 Sol (max) | 0.3 | certified | certified | certified |
| Gemini 4 Argon (high) | 0.0 | disproved | certified | disproved |
| GPT-6 Astra (max) | 0.8 | certified | certified | disproved |
| Claude Opus 5.5 (xhigh) | 2.5 | certified | certified | disproved |
| GPT-6.1 Sol (xhigh) | -1.3 | disproved | disproved | disproved |
| GPT-6 Astra (xhigh) | 1.3 | certified | certified | disproved |
| GPT-6.1 Sol (high) | -2.9 | disproved | disproved | disproved |
| Claude Opus 5.5 (high) | 0.3 | certified | certified | disproved |
| MiMo-V2.6-Pro | -10.3 | disproved | disproved | disproved |
| Claude Sonnet 5.5 (xhigh) | -1.7 | disproved | disproved | disproved |
| Claude Haiku 5.5 (max) | -14.1 | disproved | disproved | disproved |
| Claude Opus 5.5 (medium) | -0.8 | disproved | disproved | disproved |
| Claude Haiku 5.5 (xhigh) | -15.3 | disproved | disproved | disproved |
| GPT-6.1 Sol (medium) | -6.1 | disproved | disproved | disproved |
| GPT-6 Astra (high) | -1.2 | disproved | disproved | disproved |
| GPT-6 Luna (max) | -18.3 | disproved | disproved | disproved |
| Claude Haiku 5.5 (high) | -18.6 | disproved | disproved | disproved |
| GPT-6 Luna (xhigh) | -23.3 | disproved | disproved | disproved |
| Claude Haiku 5.5 (medium) | -22.7 | disproved | disproved | disproved |
| Claude Haiku 5.5 (low) | -28.0 | disproved | disproved | disproved |
| GPT-6 Luna (high) | -25.5 | disproved | disproved | disproved |
| GPT-6 Luna (medium) | -28.0 | disproved | disproved | disproved |
| GPT-6 Luna (low) | -37.7 | disproved | disproved | disproved |
| GPT-5.6 Luna (low) | -38.0 | disproved | disproved | disproved |

**Plan basis, main workload:** not evaluated (no row has FullCost and an identified M_W (E61/E67)).

## Scenario shares

Frequencies over 10,000 scenarios per run (seed 20261023); streams are defined in [methodology.md](methodology.md#uncertainty-outputs). S1T adds benchmark sampling noise under an independent-task approximation (O39); the other streams exclude it, and every stream excludes correlated-task, harness and attempt effects (E155).

### API basis: rank 1

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M | S1T |
|---|---:|---:|---:|---:|---:|---:|
| Claude Haiku 5.5 (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Haiku 5.5 (low) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Haiku 5.5 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Haiku 5.5 (medium) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Haiku 5.5 (xhigh) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 1.1% |
| Claude Opus 5.5 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.2% |
| Claude Opus 5.5 (medium) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 1.1% |
| Claude Opus 5.5 (xhigh) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.9% |
| Claude Sonnet 5.5 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.4% |
| Claude Sonnet 5.5 (xhigh) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| DeepSeek V4.1 Flash 1017 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 1.4% |
| GPT-5.6 Luna (low) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (xhigh) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.3% |
| GPT-6 Luna (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Luna (low) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Luna (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Luna (medium) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Luna (xhigh) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 20.4% |
| GPT-6.1 Sol (max) | 0.0% | 0.0% | 2.2% | 0.0% | 0.0% | 32.3% |
| GPT-6.1 Sol (medium) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 3.4% |
| GPT-6.1 Sol (xhigh) | 100.0% | 100.0% | 97.7% | 100.0% | 100.0% | 36.2% |
| Gemini 4 Argon (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.9% |
| MiMo-V2.6-Pro | 0.0% | 0.0% | 0.1% | 0.0% | 0.0% | 1.5% |

### API basis: rank 3 or better

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M | S1T |
|---|---:|---:|---:|---:|---:|---:|
| Claude Haiku 5.5 (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Haiku 5.5 (low) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Haiku 5.5 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Haiku 5.5 (medium) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Haiku 5.5 (xhigh) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 9.1% |
| Claude Opus 5.5 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 2.1% |
| Claude Opus 5.5 (medium) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 9.4% |
| Claude Opus 5.5 (xhigh) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 7.1% |
| Claude Sonnet 5.5 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 3.4% |
| Claude Sonnet 5.5 (xhigh) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 1.1% |
| DeepSeek V4.1 Flash 1017 (max) | 0.0% | 0.0% | 0.3% | 0.0% | 0.0% | 10.2% |
| GPT-5.6 Luna (low) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.5% |
| GPT-6 Astra (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.5% |
| GPT-6 Astra (xhigh) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 3.5% |
| GPT-6 Luna (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Luna (low) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Luna (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Luna (medium) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Luna (xhigh) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6.1 Sol (high) | 100.0% | 100.0% | 99.5% | 100.0% | 100.0% | 62.3% |
| GPT-6.1 Sol (max) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 73.3% |
| GPT-6.1 Sol (medium) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 21.0% |
| GPT-6.1 Sol (xhigh) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 76.9% |
| Gemini 4 Argon (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 7.5% |
| MiMo-V2.6-Pro | 0.0% | 0.0% | 0.2% | 0.0% | 0.0% | 11.8% |

### API basis: on the frontier

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M | S1T |
|---|---:|---:|---:|---:|---:|---:|
| Claude Haiku 5.5 (high) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 94.6% |
| Claude Haiku 5.5 (low) | 0.0% | 0.0% | 48.4% | 0.0% | 0.0% | 47.3% |
| Claude Haiku 5.5 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 6.7% |
| Claude Haiku 5.5 (medium) | 100.0% | 100.0% | 99.9% | 100.0% | 100.0% | 89.3% |
| Claude Haiku 5.5 (xhigh) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 83.0% |
| Claude Opus 5.5 (high) | 0.0% | 0.0% | 44.7% | 0.0% | 0.0% | 26.6% |
| Claude Opus 5.5 (max) | 100.0% | 100.0% | 71.4% | 100.0% | 100.0% | 40.6% |
| Claude Opus 5.5 (medium) | 0.0% | 0.0% | 6.3% | 0.0% | 0.0% | 25.8% |
| Claude Opus 5.5 (xhigh) | 100.0% | 100.0% | 99.6% | 100.0% | 100.0% | 47.0% |
| Claude Sonnet 5.5 (max) | 100.0% | 100.0% | 91.2% | 100.0% | 100.0% | 48.4% |
| Claude Sonnet 5.5 (xhigh) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 10.4% |
| DeepSeek V4.1 Flash 1017 (max) | 0.0% | 0.0% | 23.5% | 0.0% | 0.0% | 37.5% |
| GPT-5.6 Luna (low) | 0.0% | 0.0% | 0.2% | 0.0% | 0.0% | 38.8% |
| GPT-6 Astra (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 7.4% |
| GPT-6 Astra (max) | 0.0% | 0.0% | 0.1% | 0.0% | 0.0% | 12.1% |
| GPT-6 Astra (xhigh) | 100.0% | 100.0% | 96.5% | 100.0% | 100.0% | 34.4% |
| GPT-6 Luna (high) | 100.0% | 100.0% | 99.9% | 100.0% | 100.0% | 82.5% |
| GPT-6 Luna (low) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% |
| GPT-6 Luna (max) | 100.0% | 100.0% | 64.9% | 100.0% | 100.0% | 54.9% |
| GPT-6 Luna (medium) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% |
| GPT-6 Luna (xhigh) | 0.0% | 0.0% | 21.1% | 0.0% | 0.0% | 37.5% |
| GPT-6.1 Sol (high) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 84.7% |
| GPT-6.1 Sol (max) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 68.0% |
| GPT-6.1 Sol (medium) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 94.5% |
| GPT-6.1 Sol (xhigh) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 69.8% |
| Gemini 4 Argon (high) | 0.0% | 0.0% | 25.2% | 0.0% | 0.0% | 28.6% |
| MiMo-V2.6-Pro | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 97.4% |

### API basis: value-score dispersion (SD; covariance term)

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M | S1T |
|---|---:|---:|---:|---:|---:|---:|
| Claude Haiku 5.5 (high) | 0.00 (+0.00) | 0.00 (+0.00) | 1.11 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.30 (+0.00) |
| Claude Haiku 5.5 (low) | 0.00 (+0.00) | 0.00 (+0.00) | 1.10 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.14 (+0.00) |
| Claude Haiku 5.5 (max) | 0.00 (+0.00) | 0.00 (+0.00) | 0.97 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.36 (+0.00) |
| Claude Haiku 5.5 (medium) | 0.00 (+0.00) | 0.00 (+0.00) | 1.21 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.21 (+0.00) |
| Claude Haiku 5.5 (xhigh) | 0.00 (+0.00) | 0.00 (+0.00) | 1.02 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.34 (+0.00) |
| Claude Opus 5.5 (high) | 0.00 (+0.00) | 0.00 (+0.00) | 0.94 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.41 (+0.00) |
| Claude Opus 5.5 (max) | 0.00 (+0.00) | 0.00 (+0.00) | 0.85 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.41 (+0.00) |
| Claude Opus 5.5 (medium) | 0.00 (+0.00) | 0.00 (+0.00) | 0.96 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.40 (+0.00) |
| Claude Opus 5.5 (xhigh) | 0.00 (+0.00) | 0.00 (+0.00) | 0.91 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.40 (+0.00) |
| Claude Sonnet 5.5 (max) | 0.00 (+0.00) | 0.00 (+0.00) | 0.78 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.41 (+0.00) |
| Claude Sonnet 5.5 (xhigh) | 0.00 (+0.00) | 0.00 (+0.00) | 0.82 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.44 (+0.00) |
| DeepSeek V4.1 Flash 1017 (max) | 0.00 (+0.00) | 0.00 (+0.00) | 0.88 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.39 (+0.00) |
| GPT-5.6 Luna (low) | 0.00 (+0.00) | 0.00 (+0.00) | 1.20 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 0.76 (+0.00) |
| GPT-6 Astra (high) | 0.00 (+0.00) | 0.00 (+0.00) | 0.86 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.43 (+0.00) |
| GPT-6 Astra (max) | 0.00 (+0.00) | 0.00 (+0.00) | 0.75 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.43 (+0.00) |
| GPT-6 Astra (xhigh) | 0.00 (+0.00) | 0.00 (+0.00) | 0.72 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.43 (+0.00) |
| GPT-6 Luna (high) | 0.00 (+0.00) | 0.00 (+0.00) | 1.43 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.04 (+0.00) |
| GPT-6 Luna (low) | 0.00 (+0.00) | 0.00 (+0.00) | 1.27 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 0.74 (+0.00) |
| GPT-6 Luna (max) | 0.00 (+0.00) | 0.00 (+0.00) | 1.33 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.21 (+0.00) |
| GPT-6 Luna (medium) | 0.00 (+0.00) | 0.00 (+0.00) | 1.46 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 0.97 (+0.00) |
| GPT-6 Luna (xhigh) | 0.00 (+0.00) | 0.00 (+0.00) | 1.33 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.12 (+0.00) |
| GPT-6.1 Sol (high) | 0.00 (+0.00) | 0.00 (+0.00) | 0.83 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.43 (+0.00) |
| GPT-6.1 Sol (max) | 0.00 (+0.00) | 0.00 (+0.00) | 0.69 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.44 (+0.00) |
| GPT-6.1 Sol (medium) | 0.00 (+0.00) | 0.00 (+0.00) | 0.97 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.43 (+0.00) |
| GPT-6.1 Sol (xhigh) | 0.00 (+0.00) | 0.00 (+0.00) | 0.73 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.43 (+0.00) |
| Gemini 4 Argon (high) | 0.00 (+0.00) | 0.00 (+0.00) | 0.94 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.43 (+0.00) |
| MiMo-V2.6-Pro | 0.00 (+0.00) | 0.00 (+0.00) | 1.18 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.37 (+0.00) |

Plan streams S1, S2, S1 endpoint-heavy, S1M and S1T run with owner-named transfers off (E167): claude-haiku-5-5-high@claude-max-20x, claude-haiku-5-5-high@claude-max-5x, claude-haiku-5-5-high@claude-pro, claude-haiku-5-5-low@claude-max-20x, claude-haiku-5-5-low@claude-max-5x, claude-haiku-5-5-low@claude-pro, claude-haiku-5-5-max@claude-max-20x, claude-haiku-5-5-max@claude-max-5x, claude-haiku-5-5-max@claude-pro, claude-haiku-5-5-medium@claude-max-20x, claude-haiku-5-5-medium@claude-max-5x, claude-haiku-5-5-medium@claude-pro, claude-haiku-5-5@claude-max-20x, claude-haiku-5-5@claude-max-5x, claude-haiku-5-5@claude-pro, claude-opus-5-5-high@claude-max-20x, claude-opus-5-5-high@claude-max-5x, claude-opus-5-5-high@claude-pro, claude-opus-5-5-medium@claude-max-20x, claude-opus-5-5-medium@claude-max-5x, claude-opus-5-5-medium@claude-pro, claude-opus-5-5-xhigh@claude-max-20x, claude-opus-5-5-xhigh@claude-max-5x, claude-opus-5-5-xhigh@claude-pro, claude-sonnet-5-5-xhigh@claude-max-20x, claude-sonnet-5-5-xhigh@claude-max-5x, claude-sonnet-5-5-xhigh@claude-pro, claude-sonnet-5-5@claude-max-20x, claude-sonnet-5-5@claude-max-5x, claude-sonnet-5-5@claude-pro, gpt-5.6-luna-low@chatgpt-plus, gpt-5.6-luna-low@chatgpt-pro-100, gpt-5.6-luna-low@chatgpt-pro-200, gpt-5.6-luna-low@chatgpt-pro-500, gpt-6-astra-high@chatgpt-plus, gpt-6-astra-high@chatgpt-pro-100, gpt-6-astra-high@chatgpt-pro-200, gpt-6-astra-high@chatgpt-pro-500, gpt-6-astra-xhigh@chatgpt-plus, gpt-6-astra-xhigh@chatgpt-pro-100, gpt-6-astra-xhigh@chatgpt-pro-200, gpt-6-astra-xhigh@chatgpt-pro-500, gpt-6-luna-high@chatgpt-plus, gpt-6-luna-high@chatgpt-pro-100, gpt-6-luna-high@chatgpt-pro-200, gpt-6-luna-high@chatgpt-pro-500, gpt-6-luna-low@chatgpt-plus, gpt-6-luna-low@chatgpt-pro-100, gpt-6-luna-low@chatgpt-pro-200, gpt-6-luna-low@chatgpt-pro-500, gpt-6-luna-medium@chatgpt-plus, gpt-6-luna-medium@chatgpt-pro-100, gpt-6-luna-medium@chatgpt-pro-200, gpt-6-luna-medium@chatgpt-pro-500, gpt-6-luna-xhigh@chatgpt-plus, gpt-6-luna-xhigh@chatgpt-pro-100, gpt-6-luna-xhigh@chatgpt-pro-200, gpt-6-luna-xhigh@chatgpt-pro-500, gpt-6-luna@chatgpt-plus, gpt-6-luna@chatgpt-pro-100, gpt-6-luna@chatgpt-pro-200, gpt-6-luna@chatgpt-pro-500, gpt-6.1-sol-high@chatgpt-plus, gpt-6.1-sol-high@chatgpt-pro-100, gpt-6.1-sol-high@chatgpt-pro-200, gpt-6.1-sol-high@chatgpt-pro-500, gpt-6.1-sol-medium@chatgpt-plus, gpt-6.1-sol-medium@chatgpt-pro-100, gpt-6.1-sol-medium@chatgpt-pro-200, gpt-6.1-sol-medium@chatgpt-pro-500, gpt-6.1-sol-xhigh@chatgpt-plus, gpt-6.1-sol-xhigh@chatgpt-pro-100, gpt-6.1-sol-xhigh@chatgpt-pro-200, gpt-6.1-sol-xhigh@chatgpt-pro-500, mimo-v2-6-pro@mimo-token-plan-lite, mimo-v2-6-pro@mimo-token-plan-max, mimo-v2-6-pro@mimo-token-plan-pro, mimo-v2-6-pro@mimo-token-plan-standard depend on a transfer and are unevaluable there (—), never reselected or replaced by API cost.

### Plan basis: rank 1

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M | S1T |
|---|---:|---:|---:|---:|---:|---:|
| claude-haiku-5-5-high@claude-max-20x | 0.0% | — | — | — | — | — |
| claude-haiku-5-5-high@claude-max-5x | 0.0% | — | — | — | — | — |
| claude-haiku-5-5-high@claude-pro | 0.0% | — | — | — | — | — |
| claude-haiku-5-5-low@claude-max-20x | 0.0% | — | — | — | — | — |
| claude-haiku-5-5-low@claude-max-5x | 0.0% | — | — | — | — | — |
| claude-haiku-5-5-low@claude-pro | 0.0% | — | — | — | — | — |
| claude-haiku-5-5-max@claude-max-20x | 0.0% | — | — | — | — | — |
| claude-haiku-5-5-max@claude-max-5x | 0.0% | — | — | — | — | — |
| claude-haiku-5-5-max@claude-pro | 0.0% | — | — | — | — | — |
| claude-haiku-5-5-medium@claude-max-20x | 0.0% | — | — | — | — | — |
| claude-haiku-5-5-medium@claude-max-5x | 0.0% | — | — | — | — | — |
| claude-haiku-5-5-medium@claude-pro | 0.0% | — | — | — | — | — |
| claude-haiku-5-5@claude-max-20x | 0.0% | — | — | — | — | — |
| claude-haiku-5-5@claude-max-5x | 0.0% | — | — | — | — | — |
| claude-haiku-5-5@claude-pro | 0.0% | — | — | — | — | — |
| claude-opus-5-5-high@claude-max-20x | 0.0% | — | — | — | — | — |
| claude-opus-5-5-high@claude-max-5x | 0.0% | — | — | — | — | — |
| claude-opus-5-5-high@claude-pro | 0.0% | — | — | — | — | — |
| claude-opus-5-5-medium@claude-max-20x | 0.0% | — | — | — | — | — |
| claude-opus-5-5-medium@claude-max-5x | 0.0% | — | — | — | — | — |
| claude-opus-5-5-medium@claude-pro | 0.0% | — | — | — | — | — |
| claude-opus-5-5-xhigh@claude-max-20x | 0.0% | — | — | — | — | — |
| claude-opus-5-5-xhigh@claude-max-5x | 0.0% | — | — | — | — | — |
| claude-opus-5-5-xhigh@claude-pro | 100.0% | — | — | — | — | — |
| claude-opus-5-5@claude-max-20x | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| claude-opus-5-5@claude-max-5x | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| claude-opus-5-5@claude-pro | 0.0% | 100.0% | 100.0% | 100.0% | 100.0% | 81.9% |
| claude-sonnet-5-5-xhigh@claude-max-20x | 0.0% | — | — | — | — | — |
| claude-sonnet-5-5-xhigh@claude-max-5x | 0.0% | — | — | — | — | — |
| claude-sonnet-5-5-xhigh@claude-pro | 0.0% | — | — | — | — | — |
| claude-sonnet-5-5@claude-max-20x | 0.0% | — | — | — | — | — |
| claude-sonnet-5-5@claude-max-5x | 0.0% | — | — | — | — | — |
| claude-sonnet-5-5@claude-pro | 0.0% | — | — | — | — | — |
| deepseek-v4-1-flash-1017@api | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| gemini-4-argon@api | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| gpt-5.6-luna-low@chatgpt-plus | 0.0% | — | — | — | — | — |
| gpt-5.6-luna-low@chatgpt-pro-100 | 0.0% | — | — | — | — | — |
| gpt-5.6-luna-low@chatgpt-pro-200 | 0.0% | — | — | — | — | — |
| gpt-5.6-luna-low@chatgpt-pro-500 | 0.0% | — | — | — | — | — |
| gpt-6-astra-high@chatgpt-plus | 0.0% | — | — | — | — | — |
| gpt-6-astra-high@chatgpt-pro-100 | 0.0% | — | — | — | — | — |
| gpt-6-astra-high@chatgpt-pro-200 | 0.0% | — | — | — | — | — |
| gpt-6-astra-high@chatgpt-pro-500 | 0.0% | — | — | — | — | — |
| gpt-6-astra-xhigh@chatgpt-plus | 0.0% | — | — | — | — | — |
| gpt-6-astra-xhigh@chatgpt-pro-100 | 0.0% | — | — | — | — | — |
| gpt-6-astra-xhigh@chatgpt-pro-200 | 0.0% | — | — | — | — | — |
| gpt-6-astra-xhigh@chatgpt-pro-500 | 0.0% | — | — | — | — | — |
| gpt-6-astra@chatgpt-plus | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| gpt-6-astra@chatgpt-pro-100 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| gpt-6-astra@chatgpt-pro-200 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.3% |
| gpt-6-astra@chatgpt-pro-500 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| gpt-6-luna-high@chatgpt-plus | 0.0% | — | — | — | — | — |
| gpt-6-luna-high@chatgpt-pro-100 | 0.0% | — | — | — | — | — |
| gpt-6-luna-high@chatgpt-pro-200 | 0.0% | — | — | — | — | — |
| gpt-6-luna-high@chatgpt-pro-500 | 0.0% | — | — | — | — | — |
| gpt-6-luna-low@chatgpt-plus | 0.0% | — | — | — | — | — |
| gpt-6-luna-low@chatgpt-pro-100 | 0.0% | — | — | — | — | — |
| gpt-6-luna-low@chatgpt-pro-200 | 0.0% | — | — | — | — | — |
| gpt-6-luna-low@chatgpt-pro-500 | 0.0% | — | — | — | — | — |
| gpt-6-luna-medium@chatgpt-plus | 0.0% | — | — | — | — | — |
| gpt-6-luna-medium@chatgpt-pro-100 | 0.0% | — | — | — | — | — |
| gpt-6-luna-medium@chatgpt-pro-200 | 0.0% | — | — | — | — | — |
| gpt-6-luna-medium@chatgpt-pro-500 | 0.0% | — | — | — | — | — |
| gpt-6-luna-xhigh@chatgpt-plus | 0.0% | — | — | — | — | — |
| gpt-6-luna-xhigh@chatgpt-pro-100 | 0.0% | — | — | — | — | — |
| gpt-6-luna-xhigh@chatgpt-pro-200 | 0.0% | — | — | — | — | — |
| gpt-6-luna-xhigh@chatgpt-pro-500 | 0.0% | — | — | — | — | — |
| gpt-6-luna@chatgpt-plus | 0.0% | — | — | — | — | — |
| gpt-6-luna@chatgpt-pro-100 | 0.0% | — | — | — | — | — |
| gpt-6-luna@chatgpt-pro-200 | 0.0% | — | — | — | — | — |
| gpt-6-luna@chatgpt-pro-500 | 0.0% | — | — | — | — | — |
| gpt-6.1-sol-high@chatgpt-plus | 0.0% | — | — | — | — | — |
| gpt-6.1-sol-high@chatgpt-pro-100 | 0.0% | — | — | — | — | — |
| gpt-6.1-sol-high@chatgpt-pro-200 | 0.0% | — | — | — | — | — |
| gpt-6.1-sol-high@chatgpt-pro-500 | 0.0% | — | — | — | — | — |
| gpt-6.1-sol-medium@chatgpt-plus | 0.0% | — | — | — | — | — |
| gpt-6.1-sol-medium@chatgpt-pro-100 | 0.0% | — | — | — | — | — |
| gpt-6.1-sol-medium@chatgpt-pro-200 | 0.0% | — | — | — | — | — |
| gpt-6.1-sol-medium@chatgpt-pro-500 | 0.0% | — | — | — | — | — |
| gpt-6.1-sol-xhigh@chatgpt-plus | 0.0% | — | — | — | — | — |
| gpt-6.1-sol-xhigh@chatgpt-pro-100 | 0.0% | — | — | — | — | — |
| gpt-6.1-sol-xhigh@chatgpt-pro-200 | 0.0% | — | — | — | — | — |
| gpt-6.1-sol-xhigh@chatgpt-pro-500 | 0.0% | — | — | — | — | — |
| gpt-6.1-sol@chatgpt-plus | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| gpt-6.1-sol@chatgpt-pro-100 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| gpt-6.1-sol@chatgpt-pro-200 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| gpt-6.1-sol@chatgpt-pro-500 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 17.8% |
| mimo-v2-6-pro@mimo-token-plan-lite | 0.0% | — | — | — | — | — |
| mimo-v2-6-pro@mimo-token-plan-max | 0.0% | — | — | — | — | — |
| mimo-v2-6-pro@mimo-token-plan-pro | 0.0% | — | — | — | — | — |
| mimo-v2-6-pro@mimo-token-plan-standard | 0.0% | — | — | — | — | — |

### Plan basis: rank 3 or better

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M | S1T |
|---|---:|---:|---:|---:|---:|---:|
| claude-haiku-5-5-high@claude-max-20x | 0.0% | — | — | — | — | — |
| claude-haiku-5-5-high@claude-max-5x | 0.0% | — | — | — | — | — |
| claude-haiku-5-5-high@claude-pro | 0.0% | — | — | — | — | — |
| claude-haiku-5-5-low@claude-max-20x | 0.0% | — | — | — | — | — |
| claude-haiku-5-5-low@claude-max-5x | 0.0% | — | — | — | — | — |
| claude-haiku-5-5-low@claude-pro | 0.0% | — | — | — | — | — |
| claude-haiku-5-5-max@claude-max-20x | 0.0% | — | — | — | — | — |
| claude-haiku-5-5-max@claude-max-5x | 0.0% | — | — | — | — | — |
| claude-haiku-5-5-max@claude-pro | 0.0% | — | — | — | — | — |
| claude-haiku-5-5-medium@claude-max-20x | 0.0% | — | — | — | — | — |
| claude-haiku-5-5-medium@claude-max-5x | 0.0% | — | — | — | — | — |
| claude-haiku-5-5-medium@claude-pro | 0.0% | — | — | — | — | — |
| claude-haiku-5-5@claude-max-20x | 0.0% | — | — | — | — | — |
| claude-haiku-5-5@claude-max-5x | 0.0% | — | — | — | — | — |
| claude-haiku-5-5@claude-pro | 0.0% | — | — | — | — | — |
| claude-opus-5-5-high@claude-max-20x | 0.0% | — | — | — | — | — |
| claude-opus-5-5-high@claude-max-5x | 0.0% | — | — | — | — | — |
| claude-opus-5-5-high@claude-pro | 0.0% | — | — | — | — | — |
| claude-opus-5-5-medium@claude-max-20x | 0.0% | — | — | — | — | — |
| claude-opus-5-5-medium@claude-max-5x | 0.0% | — | — | — | — | — |
| claude-opus-5-5-medium@claude-pro | 0.0% | — | — | — | — | — |
| claude-opus-5-5-xhigh@claude-max-20x | 100.0% | — | — | — | — | — |
| claude-opus-5-5-xhigh@claude-max-5x | 100.0% | — | — | — | — | — |
| claude-opus-5-5-xhigh@claude-pro | 100.0% | — | — | — | — | — |
| claude-opus-5-5@claude-max-20x | 0.0% | 100.0% | 100.0% | 100.0% | 100.0% | 82.6% |
| claude-opus-5-5@claude-max-5x | 0.0% | 100.0% | 100.0% | 100.0% | 100.0% | 80.8% |
| claude-opus-5-5@claude-pro | 0.0% | 100.0% | 100.0% | 100.0% | 100.0% | 82.8% |
| claude-sonnet-5-5-xhigh@claude-max-20x | 0.0% | — | — | — | — | — |
| claude-sonnet-5-5-xhigh@claude-max-5x | 0.0% | — | — | — | — | — |
| claude-sonnet-5-5-xhigh@claude-pro | 0.0% | — | — | — | — | — |
| claude-sonnet-5-5@claude-max-20x | 0.0% | — | — | — | — | — |
| claude-sonnet-5-5@claude-max-5x | 0.0% | — | — | — | — | — |
| claude-sonnet-5-5@claude-pro | 0.0% | — | — | — | — | — |
| deepseek-v4-1-flash-1017@api | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| gemini-4-argon@api | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| gpt-5.6-luna-low@chatgpt-plus | 0.0% | — | — | — | — | — |
| gpt-5.6-luna-low@chatgpt-pro-100 | 0.0% | — | — | — | — | — |
| gpt-5.6-luna-low@chatgpt-pro-200 | 0.0% | — | — | — | — | — |
| gpt-5.6-luna-low@chatgpt-pro-500 | 0.0% | — | — | — | — | — |
| gpt-6-astra-high@chatgpt-plus | 0.0% | — | — | — | — | — |
| gpt-6-astra-high@chatgpt-pro-100 | 0.0% | — | — | — | — | — |
| gpt-6-astra-high@chatgpt-pro-200 | 0.0% | — | — | — | — | — |
| gpt-6-astra-high@chatgpt-pro-500 | 0.0% | — | — | — | — | — |
| gpt-6-astra-xhigh@chatgpt-plus | 0.0% | — | — | — | — | — |
| gpt-6-astra-xhigh@chatgpt-pro-100 | 0.0% | — | — | — | — | — |
| gpt-6-astra-xhigh@chatgpt-pro-200 | 0.0% | — | — | — | — | — |
| gpt-6-astra-xhigh@chatgpt-pro-500 | 0.0% | — | — | — | — | — |
| gpt-6-astra@chatgpt-plus | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| gpt-6-astra@chatgpt-pro-100 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.2% |
| gpt-6-astra@chatgpt-pro-200 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.4% |
| gpt-6-astra@chatgpt-pro-500 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.3% |
| gpt-6-luna-high@chatgpt-plus | 0.0% | — | — | — | — | — |
| gpt-6-luna-high@chatgpt-pro-100 | 0.0% | — | — | — | — | — |
| gpt-6-luna-high@chatgpt-pro-200 | 0.0% | — | — | — | — | — |
| gpt-6-luna-high@chatgpt-pro-500 | 0.0% | — | — | — | — | — |
| gpt-6-luna-low@chatgpt-plus | 0.0% | — | — | — | — | — |
| gpt-6-luna-low@chatgpt-pro-100 | 0.0% | — | — | — | — | — |
| gpt-6-luna-low@chatgpt-pro-200 | 0.0% | — | — | — | — | — |
| gpt-6-luna-low@chatgpt-pro-500 | 0.0% | — | — | — | — | — |
| gpt-6-luna-medium@chatgpt-plus | 0.0% | — | — | — | — | — |
| gpt-6-luna-medium@chatgpt-pro-100 | 0.0% | — | — | — | — | — |
| gpt-6-luna-medium@chatgpt-pro-200 | 0.0% | — | — | — | — | — |
| gpt-6-luna-medium@chatgpt-pro-500 | 0.0% | — | — | — | — | — |
| gpt-6-luna-xhigh@chatgpt-plus | 0.0% | — | — | — | — | — |
| gpt-6-luna-xhigh@chatgpt-pro-100 | 0.0% | — | — | — | — | — |
| gpt-6-luna-xhigh@chatgpt-pro-200 | 0.0% | — | — | — | — | — |
| gpt-6-luna-xhigh@chatgpt-pro-500 | 0.0% | — | — | — | — | — |
| gpt-6-luna@chatgpt-plus | 0.0% | — | — | — | — | — |
| gpt-6-luna@chatgpt-pro-100 | 0.0% | — | — | — | — | — |
| gpt-6-luna@chatgpt-pro-200 | 0.0% | — | — | — | — | — |
| gpt-6-luna@chatgpt-pro-500 | 0.0% | — | — | — | — | — |
| gpt-6.1-sol-high@chatgpt-plus | 0.0% | — | — | — | — | — |
| gpt-6.1-sol-high@chatgpt-pro-100 | 0.0% | — | — | — | — | — |
| gpt-6.1-sol-high@chatgpt-pro-200 | 0.0% | — | — | — | — | — |
| gpt-6.1-sol-high@chatgpt-pro-500 | 0.0% | — | — | — | — | — |
| gpt-6.1-sol-medium@chatgpt-plus | 0.0% | — | — | — | — | — |
| gpt-6.1-sol-medium@chatgpt-pro-100 | 0.0% | — | — | — | — | — |
| gpt-6.1-sol-medium@chatgpt-pro-200 | 0.0% | — | — | — | — | — |
| gpt-6.1-sol-medium@chatgpt-pro-500 | 0.0% | — | — | — | — | — |
| gpt-6.1-sol-xhigh@chatgpt-plus | 0.0% | — | — | — | — | — |
| gpt-6.1-sol-xhigh@chatgpt-pro-100 | 0.0% | — | — | — | — | — |
| gpt-6.1-sol-xhigh@chatgpt-pro-200 | 0.0% | — | — | — | — | — |
| gpt-6.1-sol-xhigh@chatgpt-pro-500 | 0.0% | — | — | — | — | — |
| gpt-6.1-sol@chatgpt-plus | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 17.2% |
| gpt-6.1-sol@chatgpt-pro-100 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 17.2% |
| gpt-6.1-sol@chatgpt-pro-200 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| gpt-6.1-sol@chatgpt-pro-500 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 18.8% |
| mimo-v2-6-pro@mimo-token-plan-lite | 0.0% | — | — | — | — | — |
| mimo-v2-6-pro@mimo-token-plan-max | 0.0% | — | — | — | — | — |
| mimo-v2-6-pro@mimo-token-plan-pro | 0.0% | — | — | — | — | — |
| mimo-v2-6-pro@mimo-token-plan-standard | 0.0% | — | — | — | — | — |

### Plan basis: on the frontier

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M | S1T |
|---|---:|---:|---:|---:|---:|---:|
| claude-haiku-5-5-high@claude-max-20x | 0.0% | — | — | — | — | — |
| claude-haiku-5-5-high@claude-max-5x | 0.0% | — | — | — | — | — |
| claude-haiku-5-5-high@claude-pro | 100.0% | — | — | — | — | — |
| claude-haiku-5-5-low@claude-max-20x | 0.0% | — | — | — | — | — |
| claude-haiku-5-5-low@claude-max-5x | 0.0% | — | — | — | — | — |
| claude-haiku-5-5-low@claude-pro | 100.0% | — | — | — | — | — |
| claude-haiku-5-5-max@claude-max-20x | 0.0% | — | — | — | — | — |
| claude-haiku-5-5-max@claude-max-5x | 0.0% | — | — | — | — | — |
| claude-haiku-5-5-max@claude-pro | 100.0% | — | — | — | — | — |
| claude-haiku-5-5-medium@claude-max-20x | 0.0% | — | — | — | — | — |
| claude-haiku-5-5-medium@claude-max-5x | 0.0% | — | — | — | — | — |
| claude-haiku-5-5-medium@claude-pro | 100.0% | — | — | — | — | — |
| claude-haiku-5-5@claude-max-20x | 0.0% | — | — | — | — | — |
| claude-haiku-5-5@claude-max-5x | 0.0% | — | — | — | — | — |
| claude-haiku-5-5@claude-pro | 100.0% | — | — | — | — | — |
| claude-opus-5-5-high@claude-max-20x | 0.0% | — | — | — | — | — |
| claude-opus-5-5-high@claude-max-5x | 0.0% | — | — | — | — | — |
| claude-opus-5-5-high@claude-pro | 100.0% | — | — | — | — | — |
| claude-opus-5-5-medium@claude-max-20x | 0.0% | — | — | — | — | — |
| claude-opus-5-5-medium@claude-max-5x | 0.0% | — | — | — | — | — |
| claude-opus-5-5-medium@claude-pro | 100.0% | — | — | — | — | — |
| claude-opus-5-5-xhigh@claude-max-20x | 0.0% | — | — | — | — | — |
| claude-opus-5-5-xhigh@claude-max-5x | 0.0% | — | — | — | — | — |
| claude-opus-5-5-xhigh@claude-pro | 100.0% | — | — | — | — | — |
| claude-opus-5-5@claude-max-20x | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| claude-opus-5-5@claude-max-5x | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| claude-opus-5-5@claude-pro | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 91.1% |
| claude-sonnet-5-5-xhigh@claude-max-20x | 0.0% | — | — | — | — | — |
| claude-sonnet-5-5-xhigh@claude-max-5x | 0.0% | — | — | — | — | — |
| claude-sonnet-5-5-xhigh@claude-pro | 0.0% | — | — | — | — | — |
| claude-sonnet-5-5@claude-max-20x | 0.0% | — | — | — | — | — |
| claude-sonnet-5-5@claude-max-5x | 0.0% | — | — | — | — | — |
| claude-sonnet-5-5@claude-pro | 100.0% | — | — | — | — | — |
| deepseek-v4-1-flash-1017@api | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| gemini-4-argon@api | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 5.0% |
| gpt-5.6-luna-low@chatgpt-plus | 0.0% | — | — | — | — | — |
| gpt-5.6-luna-low@chatgpt-pro-100 | 0.0% | — | — | — | — | — |
| gpt-5.6-luna-low@chatgpt-pro-200 | 0.0% | — | — | — | — | — |
| gpt-5.6-luna-low@chatgpt-pro-500 | 0.0% | — | — | — | — | — |
| gpt-6-astra-high@chatgpt-plus | 0.0% | — | — | — | — | — |
| gpt-6-astra-high@chatgpt-pro-100 | 0.0% | — | — | — | — | — |
| gpt-6-astra-high@chatgpt-pro-200 | 0.0% | — | — | — | — | — |
| gpt-6-astra-high@chatgpt-pro-500 | 0.0% | — | — | — | — | — |
| gpt-6-astra-xhigh@chatgpt-plus | 0.0% | — | — | — | — | — |
| gpt-6-astra-xhigh@chatgpt-pro-100 | 0.0% | — | — | — | — | — |
| gpt-6-astra-xhigh@chatgpt-pro-200 | 0.0% | — | — | — | — | — |
| gpt-6-astra-xhigh@chatgpt-pro-500 | 0.0% | — | — | — | — | — |
| gpt-6-astra@chatgpt-plus | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| gpt-6-astra@chatgpt-pro-100 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| gpt-6-astra@chatgpt-pro-200 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 10.6% |
| gpt-6-astra@chatgpt-pro-500 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| gpt-6-luna-high@chatgpt-plus | 0.0% | — | — | — | — | — |
| gpt-6-luna-high@chatgpt-pro-100 | 0.0% | — | — | — | — | — |
| gpt-6-luna-high@chatgpt-pro-200 | 0.0% | — | — | — | — | — |
| gpt-6-luna-high@chatgpt-pro-500 | 0.0% | — | — | — | — | — |
| gpt-6-luna-low@chatgpt-plus | 0.0% | — | — | — | — | — |
| gpt-6-luna-low@chatgpt-pro-100 | 0.0% | — | — | — | — | — |
| gpt-6-luna-low@chatgpt-pro-200 | 0.0% | — | — | — | — | — |
| gpt-6-luna-low@chatgpt-pro-500 | 0.0% | — | — | — | — | — |
| gpt-6-luna-medium@chatgpt-plus | 0.0% | — | — | — | — | — |
| gpt-6-luna-medium@chatgpt-pro-100 | 0.0% | — | — | — | — | — |
| gpt-6-luna-medium@chatgpt-pro-200 | 0.0% | — | — | — | — | — |
| gpt-6-luna-medium@chatgpt-pro-500 | 0.0% | — | — | — | — | — |
| gpt-6-luna-xhigh@chatgpt-plus | 0.0% | — | — | — | — | — |
| gpt-6-luna-xhigh@chatgpt-pro-100 | 0.0% | — | — | — | — | — |
| gpt-6-luna-xhigh@chatgpt-pro-200 | 0.0% | — | — | — | — | — |
| gpt-6-luna-xhigh@chatgpt-pro-500 | 0.0% | — | — | — | — | — |
| gpt-6-luna@chatgpt-plus | 0.0% | — | — | — | — | — |
| gpt-6-luna@chatgpt-pro-100 | 0.0% | — | — | — | — | — |
| gpt-6-luna@chatgpt-pro-200 | 0.0% | — | — | — | — | — |
| gpt-6-luna@chatgpt-pro-500 | 0.0% | — | — | — | — | — |
| gpt-6.1-sol-high@chatgpt-plus | 0.0% | — | — | — | — | — |
| gpt-6.1-sol-high@chatgpt-pro-100 | 0.0% | — | — | — | — | — |
| gpt-6.1-sol-high@chatgpt-pro-200 | 0.0% | — | — | — | — | — |
| gpt-6.1-sol-high@chatgpt-pro-500 | 0.0% | — | — | — | — | — |
| gpt-6.1-sol-medium@chatgpt-plus | 0.0% | — | — | — | — | — |
| gpt-6.1-sol-medium@chatgpt-pro-100 | 0.0% | — | — | — | — | — |
| gpt-6.1-sol-medium@chatgpt-pro-200 | 0.0% | — | — | — | — | — |
| gpt-6.1-sol-medium@chatgpt-pro-500 | 0.0% | — | — | — | — | — |
| gpt-6.1-sol-xhigh@chatgpt-plus | 0.0% | — | — | — | — | — |
| gpt-6.1-sol-xhigh@chatgpt-pro-100 | 0.0% | — | — | — | — | — |
| gpt-6.1-sol-xhigh@chatgpt-pro-200 | 0.0% | — | — | — | — | — |
| gpt-6.1-sol-xhigh@chatgpt-pro-500 | 0.0% | — | — | — | — | — |
| gpt-6.1-sol@chatgpt-plus | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| gpt-6.1-sol@chatgpt-pro-100 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| gpt-6.1-sol@chatgpt-pro-200 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| gpt-6.1-sol@chatgpt-pro-500 | 0.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% |
| mimo-v2-6-pro@mimo-token-plan-lite | 0.0% | — | — | — | — | — |
| mimo-v2-6-pro@mimo-token-plan-max | 0.0% | — | — | — | — | — |
| mimo-v2-6-pro@mimo-token-plan-pro | 0.0% | — | — | — | — | — |
| mimo-v2-6-pro@mimo-token-plan-standard | 0.0% | — | — | — | — | — |

### Plan basis: value-score dispersion (SD; covariance term)

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M | S1T |
|---|---:|---:|---:|---:|---:|---:|
| claude-haiku-5-5-high@claude-max-20x | 0.00 (+0.00) | — | — | — | — | — |
| claude-haiku-5-5-high@claude-max-5x | 0.00 (+0.00) | — | — | — | — | — |
| claude-haiku-5-5-high@claude-pro | 0.00 (+0.00) | — | — | — | — | — |
| claude-haiku-5-5-low@claude-max-20x | 0.00 (+0.00) | — | — | — | — | — |
| claude-haiku-5-5-low@claude-max-5x | 0.00 (+0.00) | — | — | — | — | — |
| claude-haiku-5-5-low@claude-pro | 0.00 (+0.00) | — | — | — | — | — |
| claude-haiku-5-5-max@claude-max-20x | 0.00 (+0.00) | — | — | — | — | — |
| claude-haiku-5-5-max@claude-max-5x | 0.00 (+0.00) | — | — | — | — | — |
| claude-haiku-5-5-max@claude-pro | 0.00 (+0.00) | — | — | — | — | — |
| claude-haiku-5-5-medium@claude-max-20x | 0.00 (+0.00) | — | — | — | — | — |
| claude-haiku-5-5-medium@claude-max-5x | 0.00 (+0.00) | — | — | — | — | — |
| claude-haiku-5-5-medium@claude-pro | 0.00 (+0.00) | — | — | — | — | — |
| claude-haiku-5-5@claude-max-20x | 0.00 (+0.00) | — | — | — | — | — |
| claude-haiku-5-5@claude-max-5x | 0.00 (+0.00) | — | — | — | — | — |
| claude-haiku-5-5@claude-pro | 0.00 (+0.00) | — | — | — | — | — |
| claude-opus-5-5-high@claude-max-20x | 0.00 (+0.00) | — | — | — | — | — |
| claude-opus-5-5-high@claude-max-5x | 0.00 (+0.00) | — | — | — | — | — |
| claude-opus-5-5-high@claude-pro | 0.00 (+0.00) | — | — | — | — | — |
| claude-opus-5-5-medium@claude-max-20x | 0.00 (+0.00) | — | — | — | — | — |
| claude-opus-5-5-medium@claude-max-5x | 0.00 (+0.00) | — | — | — | — | — |
| claude-opus-5-5-medium@claude-pro | 0.00 (+0.00) | — | — | — | — | — |
| claude-opus-5-5-xhigh@claude-max-20x | 0.00 (+0.00) | — | — | — | — | — |
| claude-opus-5-5-xhigh@claude-max-5x | 0.00 (+0.00) | — | — | — | — | — |
| claude-opus-5-5-xhigh@claude-pro | 0.00 (+0.00) | — | — | — | — | — |
| claude-opus-5-5@claude-max-20x | 0.00 (+0.00) | 0.00 (+0.00) | 0.87 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.44 (+0.00) |
| claude-opus-5-5@claude-max-5x | 0.00 (+0.00) | 0.00 (+0.00) | 0.87 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.44 (+0.00) |
| claude-opus-5-5@claude-pro | 0.00 (+0.00) | 0.00 (+0.00) | 0.87 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.44 (+0.00) |
| claude-sonnet-5-5-xhigh@claude-max-20x | 0.00 (+0.00) | — | — | — | — | — |
| claude-sonnet-5-5-xhigh@claude-max-5x | 0.00 (+0.00) | — | — | — | — | — |
| claude-sonnet-5-5-xhigh@claude-pro | 0.00 (+0.00) | — | — | — | — | — |
| claude-sonnet-5-5@claude-max-20x | 0.00 (+0.00) | — | — | — | — | — |
| claude-sonnet-5-5@claude-max-5x | 0.00 (+0.00) | — | — | — | — | — |
| claude-sonnet-5-5@claude-pro | 0.00 (+0.00) | — | — | — | — | — |
| deepseek-v4-1-flash-1017@api | 0.00 (+0.00) | 0.00 (+0.00) | 0.89 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.39 (+0.00) |
| gemini-4-argon@api | 0.00 (+0.00) | 0.00 (+0.00) | 0.95 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.42 (+0.00) |
| gpt-5.6-luna-low@chatgpt-plus | 0.00 (+0.00) | — | — | — | — | — |
| gpt-5.6-luna-low@chatgpt-pro-100 | 0.00 (+0.00) | — | — | — | — | — |
| gpt-5.6-luna-low@chatgpt-pro-200 | 0.00 (+0.00) | — | — | — | — | — |
| gpt-5.6-luna-low@chatgpt-pro-500 | 0.00 (+0.00) | — | — | — | — | — |
| gpt-6-astra-high@chatgpt-plus | 0.00 (+0.00) | — | — | — | — | — |
| gpt-6-astra-high@chatgpt-pro-100 | 0.00 (+0.00) | — | — | — | — | — |
| gpt-6-astra-high@chatgpt-pro-200 | 0.00 (+0.00) | — | — | — | — | — |
| gpt-6-astra-high@chatgpt-pro-500 | 0.00 (+0.00) | — | — | — | — | — |
| gpt-6-astra-xhigh@chatgpt-plus | 0.00 (+0.00) | — | — | — | — | — |
| gpt-6-astra-xhigh@chatgpt-pro-100 | 0.00 (+0.00) | — | — | — | — | — |
| gpt-6-astra-xhigh@chatgpt-pro-200 | 0.00 (+0.00) | — | — | — | — | — |
| gpt-6-astra-xhigh@chatgpt-pro-500 | 0.00 (+0.00) | — | — | — | — | — |
| gpt-6-astra@chatgpt-plus | 0.00 (+0.00) | 0.00 (+0.00) | 0.76 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.42 (+0.00) |
| gpt-6-astra@chatgpt-pro-100 | 0.00 (+0.00) | 0.00 (+0.00) | 0.76 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.42 (+0.00) |
| gpt-6-astra@chatgpt-pro-200 | 0.00 (+0.00) | 0.00 (+0.00) | 0.76 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.42 (+0.00) |
| gpt-6-astra@chatgpt-pro-500 | 0.00 (+0.00) | 0.00 (+0.00) | 0.76 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.42 (+0.00) |
| gpt-6-luna-high@chatgpt-plus | 0.00 (+0.00) | — | — | — | — | — |
| gpt-6-luna-high@chatgpt-pro-100 | 0.00 (+0.00) | — | — | — | — | — |
| gpt-6-luna-high@chatgpt-pro-200 | 0.00 (+0.00) | — | — | — | — | — |
| gpt-6-luna-high@chatgpt-pro-500 | 0.00 (+0.00) | — | — | — | — | — |
| gpt-6-luna-low@chatgpt-plus | 0.00 (+0.00) | — | — | — | — | — |
| gpt-6-luna-low@chatgpt-pro-100 | 0.00 (+0.00) | — | — | — | — | — |
| gpt-6-luna-low@chatgpt-pro-200 | 0.00 (+0.00) | — | — | — | — | — |
| gpt-6-luna-low@chatgpt-pro-500 | 0.00 (+0.00) | — | — | — | — | — |
| gpt-6-luna-medium@chatgpt-plus | 0.00 (+0.00) | — | — | — | — | — |
| gpt-6-luna-medium@chatgpt-pro-100 | 0.00 (+0.00) | — | — | — | — | — |
| gpt-6-luna-medium@chatgpt-pro-200 | 0.00 (+0.00) | — | — | — | — | — |
| gpt-6-luna-medium@chatgpt-pro-500 | 0.00 (+0.00) | — | — | — | — | — |
| gpt-6-luna-xhigh@chatgpt-plus | 0.00 (+0.00) | — | — | — | — | — |
| gpt-6-luna-xhigh@chatgpt-pro-100 | 0.00 (+0.00) | — | — | — | — | — |
| gpt-6-luna-xhigh@chatgpt-pro-200 | 0.00 (+0.00) | — | — | — | — | — |
| gpt-6-luna-xhigh@chatgpt-pro-500 | 0.00 (+0.00) | — | — | — | — | — |
| gpt-6-luna@chatgpt-plus | 0.00 (+0.00) | — | — | — | — | — |
| gpt-6-luna@chatgpt-pro-100 | 0.00 (+0.00) | — | — | — | — | — |
| gpt-6-luna@chatgpt-pro-200 | 0.00 (+0.00) | — | — | — | — | — |
| gpt-6-luna@chatgpt-pro-500 | 0.00 (+0.00) | — | — | — | — | — |
| gpt-6.1-sol-high@chatgpt-plus | 0.00 (+0.00) | — | — | — | — | — |
| gpt-6.1-sol-high@chatgpt-pro-100 | 0.00 (+0.00) | — | — | — | — | — |
| gpt-6.1-sol-high@chatgpt-pro-200 | 0.00 (+0.00) | — | — | — | — | — |
| gpt-6.1-sol-high@chatgpt-pro-500 | 0.00 (+0.00) | — | — | — | — | — |
| gpt-6.1-sol-medium@chatgpt-plus | 0.00 (+0.00) | — | — | — | — | — |
| gpt-6.1-sol-medium@chatgpt-pro-100 | 0.00 (+0.00) | — | — | — | — | — |
| gpt-6.1-sol-medium@chatgpt-pro-200 | 0.00 (+0.00) | — | — | — | — | — |
| gpt-6.1-sol-medium@chatgpt-pro-500 | 0.00 (+0.00) | — | — | — | — | — |
| gpt-6.1-sol-xhigh@chatgpt-plus | 0.00 (+0.00) | — | — | — | — | — |
| gpt-6.1-sol-xhigh@chatgpt-pro-100 | 0.00 (+0.00) | — | — | — | — | — |
| gpt-6.1-sol-xhigh@chatgpt-pro-200 | 0.00 (+0.00) | — | — | — | — | — |
| gpt-6.1-sol-xhigh@chatgpt-pro-500 | 0.00 (+0.00) | — | — | — | — | — |
| gpt-6.1-sol@chatgpt-plus | 0.00 (+0.00) | 0.00 (+0.00) | 0.70 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.42 (+0.00) |
| gpt-6.1-sol@chatgpt-pro-100 | 0.00 (+0.00) | 0.00 (+0.00) | 0.70 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.42 (+0.00) |
| gpt-6.1-sol@chatgpt-pro-200 | 0.00 (+0.00) | 0.00 (+0.00) | 0.70 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.42 (+0.00) |
| gpt-6.1-sol@chatgpt-pro-500 | 0.00 (+0.00) | 0.00 (+0.00) | 0.70 (+0.00) | 0.00 (+0.00) | 0.00 (+0.00) | 1.42 (+0.00) |
| mimo-v2-6-pro@mimo-token-plan-lite | 0.00 (+0.00) | — | — | — | — | — |
| mimo-v2-6-pro@mimo-token-plan-max | 0.00 (+0.00) | — | — | — | — | — |
| mimo-v2-6-pro@mimo-token-plan-pro | 0.00 (+0.00) | — | — | — | — | — |
| mimo-v2-6-pro@mimo-token-plan-standard | 0.00 (+0.00) | — | — | — | — | — |

### Named S2 specification branches

- **Bug Hunt harness band (E19)** (S2): unevaluable; the captured tbench.ai leaderboard lists no configuration under two or more agents, so no cross-agent spread exists
- **cache-hit variation (E34)** (S2): unevaluable; AA's published cost embeds its cache-pricing protocol; varying the cache-hit rate needs each basket component's cache-read and uncached-input demand, which AA publishes only for the whole Index (E157)
- **first-party list versus cross-provider median price rule (E122)** (S2): unevaluable; AA publishes one price per configuration under its own rule; the alternative rule's prices are not captured

### Cheapest-above-the-bar labels (API basis)

The 90% rule's error bound holds per published event (candidate and kernel assignment); it is not corrected across the listed candidates (E198). Each kernel assignment code gives the kernel used for the candidate and the competitors, in that order (U uniform, H endpoint-heavy; a quality-level bar has no reference rows, so it takes no letter); the label needs every assignment met.

| Bar | Candidate | Reading | Frequency range | Kernel assignments | Label |
|---|---|---|---|---|---|
| quality 48.9 | GPT-6.1 Sol (high) | not scenario-supported | 49.3% to 50.4% | UU not met, UH not met, HU not met, HH not met | no |
| quality 48.9 | GPT-6.1 Sol (medium) | not scenario-supported | 49.8% to 51.3% | UU not met, UH not met, HU not met, HH not met | no |
| quality 32.3 | Claude Haiku 5.5 (high) | not scenario-supported | 48.9% to 50.5% | UU not met, UH not met, HU not met, HH not met | no |
| quality 32.3 | Claude Haiku 5.5 (medium) | not scenario-supported | 49.5% to 49.7% | UU not met, UH not met, HU not met, HH not met | no |
| quality 55.0 | GPT-6.1 Sol (max) | supported under all registered role-group kernel checks | 100.0% to 100.0% | UU met, UH met, HU met, HH met | yes |

## Diagnostics

- **Terminal-Bench cross-source agreement (AA's mini-SWE-agent run against tbench.ai):** defined; 0 rows take the leaf from tbench.ai (gap fill).
- **Rank separability (O39, independent-task approximation):** median separation 3.88 value points (API) and 0.00 (Plan); separable adjacent ranks: API 2 of 26, Plan 51 of 90. Assumptions: tasks are independent and each leaf's score is a mean over its published task count (plug-in binomial with the proportion (k + 1/2) / (n + 1), I28); attempts averaged within a task and tasks shared across models are ignored, so the noise is approximate; GDPval-AA: AA's displayed rating interval (-26/+26 Elo for Claude Opus 5.5) read as a 95% normal interval, SD 13.3 Elo for every row; AA-Omniscience: each of 6,000 questions scores +1, 0 or -1, with the shares from AA's accuracy and hallucination rate.
- **FrontierCode against Cognition:** FrontierCode cross-source agreement (AA against Cognition, same name and effort; E234): Kendall tau 0.81 (interval 0.29 to 1.00) on 7 rows. Cognition minus AA: mean +1.5 points, largest 6.3.
- **Gap-fill removal (E234, diagnostic; scores unchanged):** with these leaves removed and the rest renormalised — GPT-6 Astra (xhigh) (FrontierCode 1.1); GPT-6 Astra (high) (FrontierCode 1.1); GPT-5.6 Luna (low) (FrontierCode 1.1) — API 9 rows move; largest move 6 (GPT-6 Astra (xhigh)); Plan 5 rows move; largest move 2 (GPT-6 Astra (xhigh)).
- **Bar results without the gap fills (E234, sensitivity; labels unchanged):** cheapest displayed row as published, with fills removed, and with third-party fills lowered by the mean offset 1.5 points — API quality 48.9: GPT-6.1 Sol (medium) in all three; API quality 32.3: Claude Haiku 5.5 (medium) in all three; API quality 55.0: GPT-6.1 Sol (max) in all three; Plan quality 48.9: Claude Opus 5.5 (medium) in all three; Plan quality 32.3: Claude Haiku 5.5 (medium) in all three; Plan quality 55.0: Claude Opus 5.5 (high) in all three.
- **Quality agreement:** quality agreement (matched-panel sensitivity): Kendall tau 0.75 (interval 0.57 to 0.88) on 27 rows.
- **Quality-substitution value agreement (API):** quality-substitution value agreement, api basis (matched-panel sensitivity): Kendall tau 0.60 (interval 0.33 to 0.79) on 27 rows.
- **Quality-substitution value agreement (Plan):** quality-substitution value agreement, plan basis (matched-panel sensitivity): Kendall tau 0.62 (interval 0.43 to 0.78) on 27 rows.
- **Disjoint-evidence agreement:** disjoint-evidence agreement (restricted evidence comparison, not an eligible ranking): Kendall tau 0.69 (interval 0.47 to 0.84) on 27 rows.
- **Quality source shares:** AA-run 85%, independent 15%.
- **Non-discriminating leaves:** none.
- **Group drift:** estimated; flagged: knowledge.
- **Omniscience abstention sensitivity** (z_pen = max(0, I)): 11 rows move; largest move 7 (DeepSeek V4.1 Flash 1017 (max)).
- **GDPval-AA logistic sensitivity** (z = 100 / (1 + 10^((1600 - E) / 400)) against AA's pinned anchor; every other input fixed): API 14 rows move; largest move 8 (GPT-6.1 Sol (medium)); Plan 15 rows move; largest move 4 (DeepSeek V4.1 Flash 1017 (max)).
- **Anchor stability:** trimmed anchors (P10 / 2 and P90 x 2 (diagnostic only)) give $13.49 to $7,125.41; 17 rows move; largest move 7 (Claude Haiku 5.5 (xhigh)).

- **Basket readiness (E22):** priced leaves cover 47% of nominal quality weight (AutomationBench-AA, GDPval-AA v2.1, AA-LCR v1.1, SciCode, Terminal-Bench 4.0 (AA run)); pending components: Coding Agent Index, ITBench-AA.
- **SWE cost companion (O14, diagnostic):** 7 rows evaluated; flagged far from the median ratio: Claude Haiku 5.5 (max).
- **Matched-cost diagnostic (E55):** evaluated at 60% priced quality weight; basket/matched cost-order reversals with separated intervals: 2; rank-gap warnings: 0.
- **Frontier-families anchors (E187, diagnostic):** anchors rebuilt from the 27 frontier and near-frontier references move API no rank changes (value points per cost doubling 2.17 vs 2.17 frozen); Plan no rank changes (value points per cost doubling 1.80 vs 1.80 frozen).
- **Frontier-families bar (E199, sensitivity; the frozen bar stays primary):** quality 48.9 over 27 configurations; cheapest at or above it on the API main workload: not unique; possibly GPT-6.1 Sol (high), GPT-6.1 Sol (medium) (compares 14 configurations that can qualify).
- **One row per family (E205, diagnostic; the frozen ladder and anchors stay primary):** with each family's primary configuration only (10 rows in the one-row-per-family bar population), the ladder (headline, lower quartile, upper quartile) would be 48.1 / 39.7 / 55.3 against 48.9 / 32.3 / 55.0 frozen; anchors rebuilt from its 10 references move API 7 rows move; largest move 2 (Claude Haiku 5.5 (xhigh)) (value points per cost doubling 2.45 vs 2.17 frozen); Plan 14 rows move; largest move 3 (Claude Haiku 5.5 (high), Gemini 4 Argon (high)) (value points per cost doubling 2.08 vs 1.80 frozen).
- **Ladder over scored rows (I28, sensitivity; the frozen ladder stays primary):** the bar population keeps full-benchmark rows that have no cost; today every such row has a cost, so the ladder is unchanged.
- **Bar currency (E207, informational):** rows reaching each frozen bar: quality 48.9: 14 of 27; quality 32.3: 21 of 27; quality 55.0: 8 of 27; the current population would freeze 48.9 / 32.3 / 55.0; lifetime until the next anchor re-freeze or methodology version, whichever comes first; no staleness flag.
- **Token mix (E208):** 1 selected routes: mix not reported: the measurement publishes no token-category shares; 24 selected routes: mix unidentified: the basket's token-category shares are set-identified only (E124), so the L1 test (above 0.30 flags mix-unmatched) is not computed.
- **Observed-range sensitivity (E219, not evidence; no label changes):** with each missing leaf inside the cohort's observed range for that leaf, quality 48.9: 14 can qualify, 13 confirmed; possibly cheapest GPT-6.1 Sol (high), GPT-6.1 Sol (medium); quality 32.3: 21 can qualify, 20 confirmed; possibly cheapest Claude Haiku 5.5 (high), Claude Haiku 5.5 (medium); quality 55.0: 8 can qualify, 7 confirmed; GPT-6.1 Sol (max) confirmed cheapest.
- **What would settle the headline bar (E221, not a claim):** rows that can but need not reach quality 48.9, with the mean score their missing leaves would need: GPT-6.1 Sol (medium) (no missing leaf; reporting precision only).
- **Common leaf set (E226, diagnostic; scores unchanged):** without the leaves fewer than 90% of cohort rows have (none), API no rank changes; Plan no rank changes; rows reaching each bar: quality 48.9: 14 → 14; quality 32.3: 21 → 21; quality 55.0: 8 → 8; rows whose displayed quality differs from common-leaf quality by more than one cost doubling's worth: none.
- **Harness by leaf (E227):** Terminal-Bench: mini-SWE-agent 27; Bug Hunt: Codex CLI 13, Claude Code 11, Antigravity CLI 1, Claude Code / Anthropic-compatible shim 1, DeepSeek Harness / DeepSeek API 1.

### Leave-one-component-out cost family (E172)

Each admitted basket unit removed in turn, scored on anchors rebuilt by the freeze rule (rank changes against the primary ranking; quality held fixed).

| Removed component | API rank changes | Plan rank changes | API value points per cost doubling |
|---|---|---|---:|
| AA-Briefcase | 13 rows move; largest move 3 (DeepSeek V4.1 Flash 1017 (max)) | 6 rows move; largest move 2 (Claude Haiku 5.5 (max), Claude Sonnet 5.5 (max)) | 2.26 |
| GDPval-AA | 12 rows move; largest move 3 (Claude Opus 5.5 (medium)) | 7 rows move; largest move 2 (Claude Haiku 5.5 (max), Claude Opus 5.5 (max), Claude Opus 5.5 (high), Claude Opus 5.5 (medium), Claude Sonnet 5.5 (max)) | 2.26 |
| GDP.pdf | 4 rows move; largest move 2 (Claude Opus 5.5 (high), Claude Opus 5.5 (medium), DeepSeek V4.1 Flash 1017 (max), MiMo-V2.6-Pro) | no rank changes | 2.12 |
| AutomationBench-AA | 13 rows move; largest move 5 (MiMo-V2.6-Pro) | 13 rows move; largest move 2 (Claude Haiku 5.5 (xhigh), Claude Opus 5.5 (medium), Claude Opus 5.5 (xhigh)) | 2.06 |
| Terminal-Bench 4.0 (AA Index run) | 11 rows move; largest move 2 (Gemini 4 Argon (high)) | 4 rows move; largest move 1 (Claude Haiku 5.5 (low), Claude Haiku 5.5 (max), GPT-6 Astra (xhigh), GPT-6 Luna (max)) | 2.21 |
| SciCode | 6 rows move; largest move 1 (Claude Opus 5.5 (xhigh), Claude Sonnet 5.5 (max), Gemini 4 Argon (high), GPT-6 Astra (max), GPT-6 Astra (high), GPT-6 Astra (xhigh)) | no rank changes | 2.18 |
| AA-LCR | 3 rows move; largest move 2 (DeepSeek V4.1 Flash 1017 (max)) | no rank changes | 2.15 |

### Subset rows: paired bridge and missing spend (E10, E173)

No row is scored on a subset workload.

### Deletion sensitivity

| Branch | Retained nominal weight | Status | API rank changes | Plan rank changes |
|---|---:|---|---|---|
| leave-out:frontierCode | 75% | evaluated | 22 rows move; largest move 9 (MiMo-V2.6-Pro) | 16 rows move; largest move 5 (Claude Haiku 5.5 (xhigh), Claude Opus 5.5 (medium)) |
| leave-out:terminalBench | 80% | evaluated | 20 rows move; largest move 13 (GPT-6 Luna (max)) | 20 rows move; largest move 5 (Gemini 4 Argon (high)) |
| leave-out:bugHunt | 85% | evaluated | 15 rows move; largest move 6 (DeepSeek V4.1 Flash 1017 (max)) | 14 rows move; largest move 2 (Claude Opus 5.5 (xhigh), MiMo-V2.6-Pro) |
| leave-out:gdpval | 90% | evaluated | 14 rows move; largest move 5 (DeepSeek V4.1 Flash 1017 (max), MiMo-V2.6-Pro) | 14 rows move; largest move 3 (Claude Haiku 5.5 (xhigh)) |
| leave-out:automationBench | 90% | evaluated | 19 rows move; largest move 3 (Claude Haiku 5.5 (xhigh), DeepSeek V4.1 Flash 1017 (max), Gemini 4 Argon (high), MiMo-V2.6-Pro) | 11 rows move; largest move 3 (Claude Haiku 5.5 (high)) |
| leave-out:omniscience | 90% | evaluated | 12 rows move; largest move 3 (Claude Sonnet 5.5 (max)) | 11 rows move; largest move 3 (Claude Haiku 5.5 (low), Claude Sonnet 5.5 (max), DeepSeek V4.1 Flash 1017 (max)) |
| leave-out:lcr | 95% | evaluated | 8 rows move; largest move 5 (MiMo-V2.6-Pro) | 15 rows move; largest move 2 (Claude Sonnet 5.5 (max), Gemini 4 Argon (high), GPT-6 Astra (xhigh)) |
| leave-out:hle | 98% | evaluated | 2 rows move; largest move 1 (Claude Sonnet 5.5 (max), GPT-6 Astra (xhigh)) | 2 rows move; largest move 1 (Claude Opus 5.5 (medium), Claude Sonnet 5.5 (max)) |
| leave-out:scicode | 98% | evaluated | 2 rows move; largest move 1 (GPT-6 Astra (max), GPT-6 Astra (high)) | 2 rows move; largest move 1 (Claude Opus 5.5 (medium), Claude Sonnet 5.5 (max)) |
| leave-out:critpt | 98% | evaluated | 2 rows move; largest move 1 (Claude Sonnet 5.5 (max), GPT-6 Astra (xhigh)) | no rank changes |
| leave-source-out:Artificial Analysis | 15% | not identifiable under the coverage rule | — | — |
| basket-scope | 87% | evaluated | 13 rows move; largest move 5 (Claude Sonnet 5.5 (max)) | 9 rows move; largest move 3 (Claude Haiku 5.5 (low), Claude Sonnet 5.5 (max), DeepSeek V4.1 Flash 1017 (max)) |

### Cost-component removal (Terminal-Bench 4.0 (AA Index run): evaluated)

| Basis | Run | Rank changes |
|---|---|---|
| api | cost-component removal, original anchors | 11 rows move; largest move 2 (Gemini 4 Argon (high)) |
| api | alternative workload, recalibrated anchors | 11 rows move; largest move 2 (Gemini 4 Argon (high)) |
| plan | cost-component removal, original anchors; fixed-multiple arithmetic stress (not identified Plan economics for the altered workload) | 4 rows move; largest move 1 (Claude Haiku 5.5 (low), Claude Haiku 5.5 (max), GPT-6 Astra (xhigh), GPT-6 Luna (max)) |
| plan | alternative workload, recalibrated anchors; fixed-multiple arithmetic stress (not identified Plan economics for the altered workload) | 4 rows move; largest move 1 (Claude Haiku 5.5 (low), Claude Haiku 5.5 (max), GPT-6 Astra (xhigh), GPT-6 Luna (max)) |

## Release gates

| Rule | Status | Detail |
|---|---|---|
| clip gate (E20) | passed | no basis exceeds the clipping allowance |
| cost influence flag (E91) | passed | cost not discriminating (< 10%); informational only; beta never changes (O2) |
| quality influence flag (E126) | passed | quality not discriminating (cost share > 90%); informational only |
| subset scoring (O17) | vacuous | subset rows scored on their own workload and anchors |
| partial component flag (E37) | vacuous | AA declined- or missing-task markers, or an Index reconstruction that misses AA's total (E209) |
| route dominance filter (E88) | vacuous | certifiably dearer routes set aside |
| Plan exploratory label (E61) | fired | fewer than half of Plan rows have an identified M_W |
| score swing gate (E177) | vacuous | first v3 release: no previous v3 release to compare |
| anchor migration (E184) | vacuous | no main-workload migration deferred |
| configuration map coverage | passed | every cohort row has a pinned identity |
| quality clipping audit (E110) | passed | saturation disclosed; domain violations block the build |
| full benchmark set (O36, O38) | fired | listed, not ranked: mimo-v2-6-flash, minimax-m3-1-flash |
| missing-leaf rules (O8 provisional, E198b, E201b, E219, E221, E226) | vacuous | no ranked row has a missing leaf (O36) |
| S1M interval stream (E145) | vacuous | dormant: no ranked leaf carries a published confidence interval since O37, so S1M equals S1 (E236) |
| provider-claim label denial (E233) | vacuous | no row has a provider-claimed leaf |
| scenario outputs current (E72) | passed | scenario input hash matches the scored inputs |
