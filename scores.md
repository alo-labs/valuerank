# ValueRank v3.0.0 Scores

**Updated:** October 19, 2026 · methodology 3.0.0 · SDLC basket v1 · anchor version `v3-2026-10-21`

Value = 25% × cost score + 75% × quality. Costs are USD per basket run; the cost score is log-scaled against the frozen anchors of the row's workload (see [methodology.md](methodology.md)).

## Ranking

| Configuration | Plan rank | Plan value | Plan cost score | API rank | API value | API cost score | Quality | Quality coverage | Workload |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| [Claude Sonnet 5.5 (max)](https://valuerank.alolabs.dev/models/claude-sonnet-5-5/) | 1 | 61.13 | 51.58 | 14 | 51.55 | 13.26 | 64.32 | 100% | main |
| [Claude Opus 5.5 (max)](https://valuerank.alolabs.dev/models/claude-opus-5-5/) | 2 | 60.86 | 50.84 | 15 | 51.18 | 12.15 | 64.19 | 100% | main |
| [GPT-6.1 Sol (max)](https://valuerank.alolabs.dev/models/gpt-6-1-sol/) | 3 | 59.77 | 55.09 | 2 | 58.08 | 48.32 | 61.33 | 100% | main |
| [Claude Haiku 5.5 (xhigh)](https://valuerank.alolabs.dev/models/claude-haiku-5-5/) | 4 | 57.00 | 91.94 | 11 | 52.53 | 74.05 | 45.36 | 90% | main |
| [Claude Opus 5 (max)](https://valuerank.alolabs.dev/models/claude-opus-5/) | 5 | 56.45 | 52.40 | 21 | 46.98 | 14.50 | 57.81 | 80% | main |
| [GPT-6 Sol (max)](https://valuerank.alolabs.dev/models/gpt-6-sol/) | 6 | 56.15 | 49.79 | 8 | 53.79 | 40.34 | 58.28 | 90% | main |
| [GPT-6 Luna (max)](https://valuerank.alolabs.dev/models/gpt-6-luna/) | 7 | 56.14 | 81.33 | 3 | 57.77 | 87.85 | 47.74 | 100% | main |
| [GPT-5.6 Luna (max)](https://valuerank.alolabs.dev/models/gpt-5-6-luna/) | 8 | 55.29 | 71.13 | 6 | 55.63 | 72.49 | 50.01 | 90% | main |
| [GPT-5.6 Sol (max)](https://valuerank.alolabs.dev/models/gpt-5-6-sol/) | 9 | 55.03 | 41.05 | 13 | 51.57 | 27.17 | 59.70 | 90% | main |
| [GPT-6 Astra (max)](https://valuerank.alolabs.dev/models/gpt-6-astra/) | 10 | 54.03 | 33.48 | 16 | 50.85 | 20.77 | 60.88 | 100% | main |
| [MiMo-V2.6-Flash](https://valuerank.alolabs.dev/models/mimo-v2-6-flash/) | 11 | 53.47 | 58.66 | 1 | 60.91 | 88.43 | 51.74 | 50% | subset |
| [Claude Fable 5.1 (max)](https://valuerank.alolabs.dev/models/claude-fable-5-1/) | 12 | 53.01 | 31.30 | 18 | 47.58 | 9.56 | 60.25 | 100% | main |
| [Gemini 4 Argon (high)](https://valuerank.alolabs.dev/models/gemini-4-argon/) | 13 | 52.77 | 15.20 | 4 | 56.45 | 29.89 | 65.30 | 90% | main |
| [Muse Wonder (max)](https://valuerank.alolabs.dev/models/muse-wonder/) | 14 | 50.41 | 8.36 | 9 | 53.21 | 19.59 | 64.42 | 80% | main |
| [MiMo-V2.6-Pro](https://valuerank.alolabs.dev/models/mimo-v2-6-pro/) | 15 | 50.02 | 49.80 | 5 | 56.28 | 74.86 | 50.09 | 60% | subset |
| [Muse Spark 1.3 (max)](https://valuerank.alolabs.dev/models/muse-spark-1-3/) | 16 | 48.71 | 18.36 | 10 | 52.78 | 34.66 | 58.82 | 90% | main |
| [DeepSeek V4 Flash (max)](https://valuerank.alolabs.dev/models/deepseek-v4-flash/) | 17 | 47.30 | 45.03 | 7 | 54.75 | 74.82 | 48.06 | 80% | main |
| [DeepSeek V4 Pro (max)](https://valuerank.alolabs.dev/models/deepseek-v4-pro/) | 18 | 45.69 | 32.77 | 12 | 51.59 | 56.36 | 50.00 | 80% | main |
| [Grok 4.7 (xhigh)](https://valuerank.alolabs.dev/models/grok-4-7/) | 19 | 44.54 | 8.06 | 19 | 47.31 | 19.15 | 56.70 | 100% | main |
| [GLM-5.3 (max)](https://valuerank.alolabs.dev/models/glm-5-3/) | 20 | 43.25 | 16.71 | 20 | 47.11 | 32.17 | 52.09 | 100% | main |
| [Gemini 3.8 Flash (high)](https://valuerank.alolabs.dev/models/gemini-3-8-flash/) | 21 | 43.13 | 21.71 | 17 | 47.62 | 39.70 | 50.26 | 100% | main |
| [Qwen3.8 Max](https://valuerank.alolabs.dev/models/qwen3-8-max/) | 22 | 38.42 | 10.54 | 22 | 41.50 | 22.87 | 47.71 | 100% | main |
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
| Claude Sonnet 5.5 (max) | 72.0 | 48.9 | 45.8 | 61.8 | 66.9 | 71.8 | 66.2 | 82.7 | 55.0 | 61.0 | 31.4 | 64.32 | no |
| Claude Opus 5.5 (max) | 68.4 | 39.7 | 52.2 | 64.8 | 68.3 | 69.5 | 73.2 | 84.7 | 61.4 | 66.9 | 31.7 | 64.19 | no |
| GPT-6.1 Sol (max) | 69.6 | 42.2 | 49.1 | 58.2 | 54.7 | 64.9 | 70.8 | 83.0 | 52.9 | 54.2 | 31.7 | 61.33 | no |
| Claude Haiku 5.5 (xhigh) | 49.0 | 17.4 | 45.5 | — | 50.7 | 36.0 | 53.0 | 78.3 | 42.7 | 51.7 | 22.6 | 45.36 | no |
| Claude Opus 5 (max) | 62.5 | 25.7 | — | — | 61.1 | 56.6 | 68.5 | 79.3 | 54.9 | 56.4 | 29.1 | 57.81 | no |
| GPT-6 Sol (max) | 69.0 | 27.9 | — | 49.4 | 50.4 | 61.6 | 63.6 | 83.7 | 47.9 | 57.6 | 30.9 | 58.28 | no |
| GPT-6 Luna (max) | 63.7 | 17.4 | 41.9 | 16.4 | 46.6 | 53.2 | 50.3 | 83.3 | 38.5 | 54.6 | 19.4 | 47.74 | no |
| GPT-5.6 Luna (max) | 66.4 | 29.8 | — | 17.3 | 48.0 | 50.2 | 44.9 | 83.7 | 39.5 | 53.6 | 20.6 | 50.01 | no |
| GPT-5.6 Sol (max) | 72.3 | 41.4 | — | 37.3 | 55.4 | 60.1 | 61.0 | 84.0 | 49.5 | 57.1 | 32.3 | 59.70 | no |
| GPT-6 Astra (max) | 67.6 | 42.9 | 47.0 | 58.2 | 53.6 | 68.5 | 71.7 | 80.7 | 54.7 | 56.5 | 31.7 | 60.88 | no |
| MiMo-V2.6-Flash | — | — | 42.1 | — | 55.4 | 64.1 | 43.7 | 74.3 | 35.1 | 51.3 | 12.0 | 51.74 | coverage 50% below 70%; 1 SWE leaves observed (need 2); observed SWE weight 10% below 40%; DeepSWE v1.1 missing |
| Claude Fable 5.1 (max) | 64.3 | 41.0 | 49.0 | 57.9 | 62.7 | 59.4 | 71.7 | 85.3 | 59.1 | 63.1 | 29.7 | 60.25 | no |
| Gemini 4 Argon (high) | 78.8 | 38.8 | 43.5 | — | 56.2 | 77.5 | 71.2 | 79.7 | 57.1 | 61.8 | 27.1 | 65.30 | no |
| Muse Wonder (max) | 75.8 | 30.2 | — | — | 63.5 | 68.1 | 62.7 | 80.7 | 50.1 | 60.3 | 28.3 | 64.42 | no |
| MiMo-V2.6-Pro | — | 17.1 | 45.4 | — | 59.2 | 58.6 | 54.2 | 86.3 | 49.4 | 60.9 | 26.6 | 50.09 | coverage 60% below 70%; observed SWE weight 20% below 40%; DeepSWE v1.1 missing |
| Muse Spark 1.3 (max) | 71.7 | 30.7 | 40.6 | — | 59.0 | 57.9 | 62.5 | 83.0 | 48.7 | 58.8 | 24.9 | 58.82 | no |
| DeepSeek V4 Flash (max) | 54.3 | 20.7 | — | — | 46.7 | 54.0 | 42.9 | 79.7 | 38.6 | 50.3 | 16.6 | 48.06 | no |
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
| Claude Sonnet 5.5 (max) | $4,299.81 | $826.00 | — | $1,863.13 | $1,504.30 | $79.43 | $678.32 | $834.67 | $80.07 | $33.93 | $9,373.65 | none |
| Claude Opus 5.5 (max) | $3,950.02 | $1,015.00 | $146.00 | $1,915.18 | $1,962.05 | $155.23 | $938.69 | $865.21 | $135.11 | $67.66 | $9,989.15 | none |
| GPT-6.1 Sol (max) | $470.90 | $81.00 | — | $210.45 | $196.57 | $41.99 | $195.01 | $120.30 | $12.50 | $19.94 | $1,267.66 | none |
| Claude Haiku 5.5 (xhigh) | $184.98 | $16.00 | — | $33.29 | $20.26 | $2.73 | $18.14 | $30.38 | $0.77 | $1.53 | $292.07 | none |
| Claude Opus 5 (max) | $3,269.11 | — | — | $1,619.19 | $1,488.52 | $108.57 | $864.64 | $1,273.08 | $33.90 | $76.11 | $8,733.13 | none |
| GPT-6 Sol (max) | $905.89 | — | $38.00 | $238.81 | $280.84 | $42.54 | $235.06 | $264.22 | $12.24 | $19.82 | $1,999.41 | none |
| GPT-6 Luna (max) | $53.30 | $9.00 | — | $15.47 | $19.66 | $2.85 | $23.91 | $15.59 | $1.06 | $1.02 | $132.87 | none |
| GPT-5.6 Luna (max) | $132.72 | — | — | $35.95 | $24.18 | $5.68 | $59.91 | $56.06 | $2.67 | $2.09 | $319.25 | none |
| GPT-5.6 Sol (max) | $1,925.06 | — | $106.00 | $365.84 | $618.22 | $92.85 | $638.90 | $534.15 | $22.95 | $40.16 | $4,238.14 | none |
| GPT-6 Astra (max) | $2,262.53 | $422.00 | $133.00 | $864.69 | $996.49 | $207.58 | $1,048.30 | $560.88 | $66.89 | $99.73 | $6,107.09 | none |
| MiMo-V2.6-Flash | — | — | — | $13.81 | $16.10 | $2.01 | $10.94 | $15.19 | $0.81 | $1.51 | $60.37 | Coding Agent Index |
| Claude Fable 5.1 (max) | $3,753.59 | $1,200.00 | $237.00 | $2,066.92 | $2,150.47 | $277.49 | $1,715.62 | $1,268.42 | $189.65 | $158.45 | $11,580.62 | none |
| Gemini 4 Argon (high) | $1,770.70 | $670.00 | — | $530.33 | $400.23 | $25.93 | $399.89 | $447.49 | $30.44 | $23.64 | $3,628.64 | none |
| Muse Wonder (max) | $2,439.83 | — | — | $1,133.00 | $1,075.46 | $72.26 | $545.12 | $1,185.90 | $38.88 | $43.70 | $6,534.16 | none |
| MiMo-V2.6-Pro | — | $18.00 | — | $34.60 | $35.47 | $2.40 | $27.77 | $28.91 | $2.25 | $4.74 | $136.13 | Coding Agent Index |
| Muse Spark 1.3 (max) | $1,205.18 | — | — | $369.37 | $448.59 | $20.51 | $238.77 | $457.96 | $11.31 | $13.29 | $2,764.98 | none |
| DeepSeek V4 Flash (max) | $25.77 | — | — | $38.53 | $63.77 | $4.66 | $69.22 | $60.65 | $12.16 | $4.76 | $279.51 | none |
| DeepSeek V4 Pro (max) | $72.13 | — | — | $90.59 | $127.70 | $11.00 | $223.87 | $247.85 | $14.47 | $13.89 | $801.50 | none |
| Grok 4.7 (xhigh) | $2,671.69 | $1,131.00 | $203.00 | $846.62 | $1,415.17 | $32.43 | $707.44 | $963.85 | $38.30 | $24.51 | $6,700.02 | none |
| GLM-5.3 (max) | $1,285.14 | $432.00 | $91.00 | $514.04 | $496.54 | $17.34 | $302.51 | $532.24 | $23.62 | $14.86 | $3,186.29 | none |
| Gemini 3.8 Flash (high) | $747.62 | $372.00 | $86.00 | $245.87 | $372.82 | $10.90 | $278.70 | $385.54 | $22.12 | $9.88 | $2,073.44 | none |
| Qwen3.8 Max | $1,054.13 | $675.00 | $327.00 | $1,781.49 | $998.39 | $33.31 | $261.64 | $1,232.62 | $32.57 | $22.88 | $5,417.03 | none |
| Muse Wonder Full (max) | — | — | — | — | — | — | — | — | — | — | — | Coding Agent Index, AA-Briefcase, GDPval-AA, GDP.pdf, AutomationBench-AA, Terminal-Bench 4.0 (AA Index run), SciCode, AA-LCR |

### Valuation basis

Valuation-basis gate (E170): 21 compatible as captured, 2 valuation basis unverified (flagged: Claude Fable 5.1 (max), Muse Wonder Full (max)). AA's Index category costs reconcile exactly with the prices AA displays for each configuration at capture, so its applied prices are the prices in force at the release cutoff. Token metering (E176): 23 not published per configuration; AA values cached input at live measurements of each model's typical cache-hit rate. Source intervals (E174): terminalBench: captured, level 95% (tbench.ai: "The whiskers span the 95% confidence interval"); gdpval: published, not captured, level not stated by the source (the 95% level on AA's methodology page belongs to AA-Briefcase).

## Plan route selection

The Plan amount is the selected multiple times the cash paid for the fee period (E166), typed by what the measurement establishes; it is not capacity unless it says so. The multiple values only the measured workload's API-equivalent consumption; other plan features are not valued.

| Configuration | Selected route | Plan amount | Identification | Plan cost (USD per basket run) | Flags | Selection reason |
|---|---|---|---|---:|---|---|
| Claude Sonnet 5.5 (max) | Claude Pro $20 · common Claude assumption (58.9×, assumption) | $1,178 per month: assumed API-equivalent consumption (owner-named transfer) from claude-pro-opus55-semianalysis | unidentified | $159.15 | workload-unmatched; owner-named transfer (assumption); valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| Claude Opus 5.5 (max) | Claude Pro $20 · Opus 5.5 (58.9×, measured) | $1,178 per month: measured-workload capacity | unidentified | $169.60 | workload-unmatched; valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| GPT-6.1 Sol (max) | ChatGPT Pro $500 · common GPT assumption (10.772×, measured) | $5,386 per month: measured-workload capacity | unidentified | $117.68 | workload-unmatched; valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| Claude Haiku 5.5 (xhigh) | Claude Pro $20 · common Claude assumption (58.9×, assumption) | $1,178 per month: assumed API-equivalent consumption (owner-named transfer) from claude-pro-opus55-semianalysis | unidentified | $4.96 | workload-unmatched; owner-named transfer (assumption); valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| Claude Opus 5 (max) | Claude Pro $20 · common Claude assumption (58.9×, assumption) | $1,178 per month: assumed API-equivalent consumption (owner-named transfer) from claude-pro-opus55-semianalysis | unidentified | $148.27 | workload-unmatched; owner-named transfer (assumption); valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| GPT-6 Sol (max) | ChatGPT Pro $500 · common GPT assumption (10.772×, assumption) | $5,386 per month: assumed API-equivalent consumption (owner-named transfer) | unidentified | $185.61 | workload-unmatched; owner-named transfer (assumption); valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| GPT-6 Luna (max) | ChatGPT Pro $500 · common GPT assumption (10.772×, assumption) | $5,386 per month: assumed API-equivalent consumption (owner-named transfer) | unidentified | $12.33 | workload-unmatched; owner-named transfer (assumption); valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| GPT-5.6 Luna (max) | ChatGPT Pro $500 · common GPT assumption (10.772×, assumption) | $5,386 per month: assumed API-equivalent consumption (owner-named transfer) | unidentified | $29.64 | workload-unmatched; owner-named transfer (assumption); valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| GPT-5.6 Sol (max) | ChatGPT Pro $500 · common GPT assumption (10.772×, assumption) | $5,386 per month: assumed API-equivalent consumption (owner-named transfer) | unidentified | $393.44 | workload-unmatched; owner-named transfer (assumption); valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| GPT-6 Astra (max) | ChatGPT Plus $20 · common GPT assumption (8.1×, measured) | $162 per month: measured-workload capacity | unidentified | $753.96 | workload-unmatched; valuation basis unverified | higher evidence grade |
| MiMo-V2.6-Flash | MiMo · provisional 1.5x assumption (1.5×, assumption) | fee not established: assumed API-equivalent consumption (owner-named transfer) | unidentified | $40.25 | workload-unmatched; owner-named transfer (assumption); valuation basis unverified; observed-usage multiple; full utilisation not established | only remaining eligible route |
| Claude Fable 5.1 (max) | Claude Max $100 · Fable 5.1 (12.73×, measured) | $1,273 per month: measured-workload capacity | unidentified | $909.71 | workload-unmatched; valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| Gemini 4 Argon (high) | — | — | — | $3,628.64 | API-cost fallback: no admitted Plan route; cross-estimand ordering not identified | no eligible route |
| Muse Wonder (max) | — | — | — | $6,534.16 | API-cost fallback: no admitted Plan route; cross-estimand ordering not identified | no eligible route |
| MiMo-V2.6-Pro | MiMo · provisional 1.5x assumption (1.5×, assumption) | fee not established: assumed API-equivalent consumption (owner-named transfer) | unidentified | $90.75 | workload-unmatched; owner-named transfer (assumption); valuation basis unverified; observed-usage multiple; full utilisation not established | only remaining eligible route |
| Muse Spark 1.3 (max) | — | — | — | $2,764.98 | API-cost fallback: no admitted Plan route; cross-estimand ordering not identified | no eligible route |
| DeepSeek V4 Flash (max) | — | — | — | $279.51 | API-cost fallback: no admitted Plan route; cross-estimand ordering not identified | no eligible route |
| DeepSeek V4 Pro (max) | — | — | — | $801.50 | API-cost fallback: no admitted Plan route; cross-estimand ordering not identified | no eligible route |
| Grok 4.7 (xhigh) | — | — | — | $6,700.02 | API-cost fallback: no admitted Plan route; cross-estimand ordering not identified | no eligible route |
| GLM-5.3 (max) | — | — | — | $3,186.29 | API-cost fallback: no admitted Plan route; cross-estimand ordering not identified | no eligible route |
| Gemini 3.8 Flash (high) | — | — | — | $2,073.44 | API-cost fallback: no admitted Plan route; cross-estimand ordering not identified | no eligible route |
| Qwen3.8 Max | — | — | — | $5,417.03 | API-cost fallback: no admitted Plan route; cross-estimand ordering not identified | no eligible route |
| Muse Wonder Full (max) | — | — | — | — | — | no eligible route |

### Route alternatives

Every admissible route-measurement pair in comparator order (E171) and the comparator's pick with the selected pair removed (E179). A larger displayed multiple is arithmetic on the measured workload, never a claim that the route is cheaper on the scored workload. Workday-feasible multiple (E15), for the 13 routed rows: not evaluated: no evidenced quota schema for this route.

| Configuration | Admissible pairs | Unidentified | Pairs (multiple, status) | Leave-selected-out choice |
|---|---:|---:|---|---|
| Claude Sonnet 5.5 (max) | 3 | 3 | claude-pro-common-opus55-assumption (58.9×, selected); claude-max20x-common-opus55-assumption (58.63×, not selected by the comparator); claude-max5x-common-opus55-assumption (57.25×, not selected by the comparator) | claude-max20x-common-opus55-assumption (58.63×, value 61.12) |
| Claude Opus 5.5 (max) | 3 | 3 | claude-pro-opus55-semianalysis (58.9×, selected); claude-max20x-opus55-semianalysis (58.63×, not selected by the comparator); claude-max5x-opus55-semianalysis (57.25×, not selected by the comparator) | claude-max20x-opus55-semianalysis (58.63×, value 60.84) |
| GPT-6.1 Sol (max) | 4 | 4 | chatgpt-pro500-common-semianalysis-assumption (10.772×, selected); chatgpt-pro100-common-semianalysis-assumption (10.55×, not selected by the comparator); chatgpt-pro200-common-semianalysis-assumption (10.42×, not selected by the comparator); chatgpt-plus-common-semianalysis-assumption (8.1×, not selected by the comparator) | chatgpt-pro100-common-semianalysis-assumption (10.55×, value 59.71) |
| Claude Haiku 5.5 (xhigh) | 3 | 3 | claude-pro-common-opus55-assumption (58.9×, selected); claude-max20x-common-opus55-assumption (58.63×, not selected by the comparator); claude-max5x-common-opus55-assumption (57.25×, not selected by the comparator) | claude-max20x-common-opus55-assumption (58.63×, value 56.99) |
| Claude Opus 5 (max) | 3 | 3 | claude-pro-common-opus55-assumption (58.9×, selected); claude-max20x-common-opus55-assumption (58.63×, not selected by the comparator); claude-max5x-common-opus55-assumption (57.25×, not selected by the comparator) | claude-max20x-common-opus55-assumption (58.63×, value 56.44) |
| GPT-6 Sol (max) | 4 | 4 | chatgpt-pro500-common-semianalysis-assumption (10.772×, selected); chatgpt-pro100-common-semianalysis-assumption (10.55×, not selected by the comparator); chatgpt-pro200-common-semianalysis-assumption (10.42×, not selected by the comparator); chatgpt-plus-common-semianalysis-assumption (8.1×, not selected by the comparator) | chatgpt-pro100-common-semianalysis-assumption (10.55×, value 56.09) |
| GPT-6 Luna (max) | 4 | 4 | chatgpt-pro500-common-semianalysis-assumption (10.772×, selected); chatgpt-pro100-common-semianalysis-assumption (10.55×, not selected by the comparator); chatgpt-pro200-common-semianalysis-assumption (10.42×, not selected by the comparator); chatgpt-plus-common-semianalysis-assumption (8.1×, not selected by the comparator) | chatgpt-pro100-common-semianalysis-assumption (10.55×, value 56.08) |
| GPT-5.6 Luna (max) | 4 | 4 | chatgpt-pro500-common-semianalysis-assumption (10.772×, selected); chatgpt-pro100-common-semianalysis-assumption (10.55×, not selected by the comparator); chatgpt-pro200-common-semianalysis-assumption (10.42×, not selected by the comparator); chatgpt-plus-common-semianalysis-assumption (8.1×, not selected by the comparator) | chatgpt-pro100-common-semianalysis-assumption (10.55×, value 55.23) |
| GPT-5.6 Sol (max) | 4 | 4 | chatgpt-pro500-common-semianalysis-assumption (10.772×, selected); chatgpt-pro100-common-semianalysis-assumption (10.55×, not selected by the comparator); chatgpt-pro200-common-semianalysis-assumption (10.42×, not selected by the comparator); chatgpt-plus-common-semianalysis-assumption (8.1×, not selected by the comparator) | chatgpt-pro100-common-semianalysis-assumption (10.55×, value 54.97) |
| GPT-6 Astra (max) | 4 | 4 | chatgpt-plus-common-semianalysis-assumption (8.1×, selected); chatgpt-pro500-common-semianalysis-assumption (10.772×, not selected by the comparator); chatgpt-pro100-common-semianalysis-assumption (10.55×, not selected by the comparator); chatgpt-pro200-common-semianalysis-assumption (10.42×, not selected by the comparator) | chatgpt-pro500-common-semianalysis-assumption (10.772×, value 54.86) |
| MiMo-V2.6-Flash | 1 | 1 | mimo-provisional-user-assumption (1.5×, selected) | none: the row would fall back to API cost (O13) |
| Claude Fable 5.1 (max) | 2 | 2 | claude-max5x-fable51-semianalysis (12.73×, selected); claude-max20x-fable51-semianalysis (12.425×, not selected by the comparator) | claude-max20x-fable51-semianalysis (12.425×, value 52.94) |
| MiMo-V2.6-Pro | 1 | 1 | mimo-provisional-user-assumption (1.5×, selected) | none: the row would fall back to API cost (O13) |

### Measured-only Plan view

Admission: exact-route measurement candidates of grade controlled or concordant reports (no transfers, no diagnostics). Selection: the official selector (E111, E88, E85) rerun among the admitted candidates. Panel: rows with an admitted measured candidate; others listed as 'no measured route' (no API fallback).

| Configuration | Status | Route | Plan cost | Value | Rank |
|---|---|---|---:|---:|---:|
| Claude Opus 5.5 (max) | measured, target-workload unmatched | claude-pro-opus55-semianalysis | $169.60 | 60.86 | 1 |
| GPT-6.1 Sol (max) | measured, target-workload unmatched | chatgpt-pro500-common-semianalysis-assumption | $117.68 | 59.77 | 2 |
| GPT-6 Astra (max) | measured, target-workload unmatched | chatgpt-plus-common-semianalysis-assumption | $753.96 | 54.03 | 3 |
| Claude Fable 5.1 (max) | measured, target-workload unmatched | claude-max5x-fable51-semianalysis | $909.71 | 53.01 | 4 |
| Claude Haiku 5.5 (xhigh) | no measured route | — | — | — | — |
| Claude Opus 5 (max) | no measured route | — | — | — | — |
| Claude Sonnet 5.5 (max) | no measured route | — | — | — | — |
| DeepSeek V4 Flash (max) | no measured route | — | — | — | — |
| DeepSeek V4 Pro (max) | no measured route | — | — | — | — |
| GLM-5.3 (max) | no measured route | — | — | — | — |
| GPT-5.6 Luna (max) | no measured route | — | — | — | — |
| GPT-5.6 Sol (max) | no measured route | — | — | — | — |
| GPT-6 Luna (max) | no measured route | — | — | — | — |
| GPT-6 Sol (max) | no measured route | — | — | — | — |
| Gemini 3.8 Flash (high) | no measured route | — | — | — | — |
| Gemini 4 Argon (high) | no measured route | — | — | — | — |
| Grok 4.7 (xhigh) | no measured route | — | — | — | — |
| MiMo-V2.6-Flash | no measured route | — | — | — | — |
| MiMo-V2.6-Pro | no measured route | — | — | — | — |
| Muse Spark 1.3 (max) | no measured route | — | — | — | — |
| Muse Wonder (max) | no measured route | — | — | — | — |
| Muse Wonder Full (max) | no measured route | — | — | — | — |
| Qwen3.8 Max | no measured route | — | — | — | — |

#### Measured-evidence calibration (diagnostic)

References: each workload's measured-only rows with complete cost evidence are the references: c_L = cheapest / 2, c_H = dearest x 2 (diagnostic only; the official anchors are unchanged). Status: evaluated.

- Workload `9a0d376cc6080f3c`: measured anchors $58.84 to $1,507.92 from Claude Opus 5.5 (max), GPT-6 Astra (max), GPT-6.1 Sol (max); anchor ratio 25.6 against the official 5404.5. Official Plan anchors are set by Claude Haiku 5.5 (xhigh) (owner-named transfer) at the low end and Grok 4.7 (xhigh) (API-cost fallback) at the high end.
- Workload `1453a9a0576b02ea`: measured-evidence calibration unavailable (fewer than two measured references); measured rows none. Official Plan anchors are set by Claude Haiku 5.5 (xhigh) (owner-named transfer) at the low end and Qwen3.8 Max (API-cost fallback) at the high end.

| Configuration | Value on official Plan anchors | Value on measured anchors | Rank change |
|---|---:|---:|---:|
| Claude Fable 5.1 (max) | 53.01 | 49.08 | 0 |
| Claude Opus 5.5 (max) | 60.86 | 64.99 | 1 |
| GPT-6 Astra (max) | 54.03 | 51.00 | 0 |
| GPT-6.1 Sol (max) | 59.77 | 65.65 | -1 |

Pairwise reversals: Claude Opus 5.5 (max) and GPT-6.1 Sol (max). Largest value change: 5.89 points.

## Interval outputs

**API basis, main workload: frontier.** Not evaluable: Claude Fable 5.1 (max), MiMo-V2.6-Flash, MiMo-V2.6-Pro, Muse Wonder Full (max).

| Configuration | Possible frontier | Definite frontier | Definite counterexample | Possible frontier blocked by |
|---|---|---|---|---|
| Gemini 4 Argon (high) | certified | disproved | GPT-6.1 Sol (max) | — |
| Claude Sonnet 5.5 (max) | certified | disproved | Gemini 4 Argon (high) | — |
| GPT-6.1 Sol (max) | certified | certified | — | — |
| Muse Wonder (max) | certified | disproved | Gemini 4 Argon (high) | — |
| Claude Opus 5.5 (max) | disproved | disproved | Gemini 4 Argon (high) | Claude Sonnet 5.5 (max) |
| GPT-6 Astra (max) | disproved | disproved | Gemini 4 Argon (high) | GPT-6.1 Sol (max) |
| GPT-5.6 Sol (max) | certified | disproved | Gemini 4 Argon (high) | — |
| Muse Spark 1.3 (max) | certified | disproved | GPT-6.1 Sol (max) | — |
| GPT-6 Sol (max) | certified | disproved | GPT-6.1 Sol (max) | — |
| Grok 4.7 (xhigh) | disproved | disproved | Gemini 4 Argon (high) | Gemini 4 Argon (high), GPT-6.1 Sol (max), GPT-6 Astra (max) |
| GPT-5.6 Luna (max) | certified | disproved | GPT-6 Luna (max) | — |
| GPT-6 Luna (max) | certified | certified | — | — |
| Claude Haiku 5.5 (xhigh) | certified | disproved | GPT-6 Luna (max) | — |
| Gemini 3.8 Flash (high) | disproved | disproved | GPT-6.1 Sol (max) | GPT-6.1 Sol (max), GPT-6 Sol (max) |
| GLM-5.3 (max) | disproved | disproved | GPT-6.1 Sol (max) | GPT-6.1 Sol (max), Muse Spark 1.3 (max), GPT-6 Sol (max) |
| Claude Opus 5 (max) | certified | disproved | Gemini 4 Argon (high) | — |
| DeepSeek V4 Flash (max) | certified | disproved | GPT-6 Luna (max) | — |
| Qwen3.8 Max | disproved | disproved | Gemini 4 Argon (high) | Gemini 4 Argon (high), GPT-6.1 Sol (max), GPT-5.6 Sol (max), Muse Spark 1.3 (max), GPT-6 Sol (max), GPT-6 Luna (max), Gemini 3.8 Flash (high), GLM-5.3 (max) |
| DeepSeek V4 Pro (max) | certified | disproved | GPT-5.6 Luna (max) | — |

**API basis, main workload: cheapest at or above quality 58.3** (lower-median displayed quality of the non-provisional ranked configurations at freeze (E192)). Status certified; confirmed cheapest: none.

Configurations that can be confirmed to qualify: 5 (confirmation needs the full-composite lower bound, with missing leaves at 0, to clear the bar; O25). Cheaper same-family configurations on AA's chart that were not evaluated (one configuration per family is ranked, E193; E201): GPT-6.1 Sol (max): GPT-6.1 Sol (xhigh), GPT-6.1 Sol (high), GPT-6.1 Sol (medium), GPT-6.1 Sol (low); DeepSeek V4 Flash (max): DeepSeek V4 Flash (high).

Bar comparison: compares 12 configurations that can qualify. The bar is a displayed-quality level; qualification tests each row's full-composite bounds, so a row above the bar on displayed quality can still fail to qualify confirmed when leaves are missing (E198).

| Configuration | Displayed quality − bar | Confirmed qualifies | Possibly qualifies | Possibly cheapest |
|---|---:|---|---|---|
| Gemini 4 Argon (high) | 7.0 | certified | certified | disproved |
| Claude Sonnet 5.5 (max) | 6.0 | certified | certified | disproved |
| GPT-6.1 Sol (max) | 3.1 | certified | certified | certified |
| Muse Wonder (max) | 6.1 | disproved | certified | disproved |
| Claude Opus 5.5 (max) | 5.9 | certified | certified | disproved |
| GPT-6 Astra (max) | 2.6 | certified | certified | disproved |
| GPT-5.6 Sol (max) | 1.4 | disproved | certified | disproved |
| Muse Spark 1.3 (max) | 0.5 | disproved | certified | disproved |
| GPT-6 Sol (max) | 0.0 | disproved | certified | disproved |
| Grok 4.7 (xhigh) | -1.6 | disproved | disproved | disproved |
| GPT-5.6 Luna (max) | -8.3 | disproved | disproved | disproved |
| GPT-6 Luna (max) | -10.5 | disproved | disproved | disproved |
| Claude Haiku 5.5 (xhigh) | -12.9 | disproved | disproved | disproved |
| Gemini 3.8 Flash (high) | -8.0 | disproved | disproved | disproved |
| GLM-5.3 (max) | -6.2 | disproved | disproved | disproved |
| Claude Opus 5 (max) | -0.5 | disproved | certified | disproved |
| DeepSeek V4 Flash (max) | -10.2 | disproved | certified | certified |
| Qwen3.8 Max | -10.6 | disproved | disproved | disproved |
| DeepSeek V4 Pro (max) | -8.3 | disproved | certified | certified |

**Plan basis, main workload:** not evaluated (no row has FullCost and an identified M_W (E61/E67)).

**API basis, subset workload (AA-Briefcase, GDPval-AA, GDP.pdf, AutomationBench-AA, Terminal-Bench 4.0 (AA Index run), SciCode, AA-LCR; orderings across workloads not identified): frontier.** Not evaluable: Claude Fable 5.1 (max), Muse Wonder Full (max).

| Configuration | Possible frontier | Definite frontier | Definite counterexample | Possible frontier blocked by |
|---|---|---|---|---|
| Gemini 4 Argon (high) | certified | disproved | GPT-6.1 Sol (max) | — |
| Claude Sonnet 5.5 (max) | certified | disproved | Gemini 4 Argon (high) | — |
| GPT-6.1 Sol (max) | certified | disproved | MiMo-V2.6-Pro | — |
| Muse Wonder (max) | certified | disproved | Gemini 4 Argon (high) | — |
| Claude Opus 5.5 (max) | disproved | disproved | Gemini 4 Argon (high) | Claude Sonnet 5.5 (max) |
| GPT-6 Astra (max) | disproved | disproved | Gemini 4 Argon (high) | GPT-6.1 Sol (max) |
| GPT-5.6 Sol (max) | certified | disproved | Gemini 4 Argon (high) | — |
| Muse Spark 1.3 (max) | certified | disproved | GPT-6.1 Sol (max) | — |
| MiMo-V2.6-Pro | certified | disproved | GPT-6 Luna (max) | — |
| GPT-6 Sol (max) | certified | disproved | GPT-6.1 Sol (max) | — |
| Grok 4.7 (xhigh) | disproved | disproved | Gemini 4 Argon (high) | Gemini 4 Argon (high), GPT-6.1 Sol (max), GPT-6 Astra (max) |
| GPT-5.6 Luna (max) | certified | disproved | MiMo-V2.6-Pro | — |
| GPT-6 Luna (max) | certified | disproved | MiMo-V2.6-Flash | — |
| MiMo-V2.6-Flash | certified | certified | — | — |
| Claude Haiku 5.5 (xhigh) | certified | disproved | GPT-6 Luna (max) | — |
| Gemini 3.8 Flash (high) | disproved | disproved | GPT-6.1 Sol (max) | GPT-6.1 Sol (max), GPT-6 Sol (max) |
| GLM-5.3 (max) | disproved | disproved | Gemini 4 Argon (high) | Gemini 4 Argon (high), GPT-6.1 Sol (max), Muse Spark 1.3 (max), GPT-6 Sol (max) |
| Claude Opus 5 (max) | certified | disproved | Gemini 4 Argon (high) | — |
| DeepSeek V4 Flash (max) | certified | disproved | MiMo-V2.6-Pro | — |
| Qwen3.8 Max | disproved | disproved | Gemini 4 Argon (high) | Gemini 4 Argon (high), GPT-6.1 Sol (max), Muse Wonder (max), GPT-6 Astra (max), GPT-5.6 Sol (max), Muse Spark 1.3 (max), GPT-6 Sol (max), Grok 4.7 (xhigh), GPT-6 Luna (max), Gemini 3.8 Flash (high), GLM-5.3 (max) |
| DeepSeek V4 Pro (max) | certified | disproved | MiMo-V2.6-Pro | — |

**API basis, subset workload (AA-Briefcase, GDPval-AA, GDP.pdf, AutomationBench-AA, Terminal-Bench 4.0 (AA Index run), SciCode, AA-LCR; orderings across workloads not identified): cheapest at or above quality 58.3** (lower-median displayed quality of the non-provisional ranked configurations at freeze (E192)). Status certified; confirmed cheapest: none.

Configurations that can be confirmed to qualify: 5 (confirmation needs the full-composite lower bound, with missing leaves at 0, to clear the bar; O25). Cheaper same-family configurations on AA's chart that were not evaluated (one configuration per family is ranked, E193; E201): GPT-6.1 Sol (max): GPT-6.1 Sol (xhigh), GPT-6.1 Sol (high), GPT-6.1 Sol (medium), GPT-6.1 Sol (low); DeepSeek V4 Flash (max): DeepSeek V4 Flash (high).

Bar comparison: compares 14 configurations that can qualify. The bar is a displayed-quality level; qualification tests each row's full-composite bounds, so a row above the bar on displayed quality can still fail to qualify confirmed when leaves are missing (E198).

| Configuration | Displayed quality − bar | Confirmed qualifies | Possibly qualifies | Possibly cheapest |
|---|---:|---|---|---|
| Gemini 4 Argon (high) | 7.0 | certified | certified | disproved |
| Claude Sonnet 5.5 (max) | 6.0 | certified | certified | disproved |
| GPT-6.1 Sol (max) | 3.1 | certified | certified | certified |
| Muse Wonder (max) | 6.1 | disproved | certified | disproved |
| Claude Opus 5.5 (max) | 5.9 | certified | certified | disproved |
| GPT-6 Astra (max) | 2.6 | certified | certified | disproved |
| GPT-5.6 Sol (max) | 1.4 | disproved | certified | disproved |
| Muse Spark 1.3 (max) | 0.5 | disproved | certified | disproved |
| MiMo-V2.6-Pro | -8.2 | disproved | certified | certified |
| GPT-6 Sol (max) | 0.0 | disproved | certified | disproved |
| Grok 4.7 (xhigh) | -1.6 | disproved | disproved | disproved |
| GPT-5.6 Luna (max) | -8.3 | disproved | disproved | disproved |
| GPT-6 Luna (max) | -10.5 | disproved | disproved | disproved |
| MiMo-V2.6-Flash | -6.5 | disproved | certified | certified |
| Claude Haiku 5.5 (xhigh) | -12.9 | disproved | disproved | disproved |
| Gemini 3.8 Flash (high) | -8.0 | disproved | disproved | disproved |
| GLM-5.3 (max) | -6.2 | disproved | disproved | disproved |
| Claude Opus 5 (max) | -0.5 | disproved | certified | disproved |
| DeepSeek V4 Flash (max) | -10.2 | disproved | certified | certified |
| Qwen3.8 Max | -10.6 | disproved | disproved | disproved |
| DeepSeek V4 Pro (max) | -8.3 | disproved | certified | certified |

**Plan basis, subset workload (AA-Briefcase, GDPval-AA, GDP.pdf, AutomationBench-AA, Terminal-Bench 4.0 (AA Index run), SciCode, AA-LCR; orderings across workloads not identified):** not evaluated (unevaluable: no Plan multiple is identified for a subset workload (E149, E190)).

## Scenario shares

Frequencies over 10,000 scenarios per run (seed 20261021); streams are defined in [methodology.md](methodology.md#uncertainty-outputs). The shares exclude benchmark sampling noise beyond S1M and fitted-rating uncertainty (E155).

### API basis: rank 1

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M |
|---|---:|---:|---:|---:|---:|
| Claude Fable 5.1 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Haiku 5.5 (xhigh) | 0.0% | 0.0% | 0.7% | 0.0% | 0.0% |
| Claude Opus 5 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Sonnet 5.5 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| DeepSeek V4 Flash (max) | 0.0% | 16.0% | 15.2% | 20.6% | 16.6% |
| DeepSeek V4 Pro (max) | 0.0% | 0.7% | 1.5% | 2.5% | 0.6% |
| GLM-5.3 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-5.6 Luna (max) | 0.0% | 14.1% | 11.9% | 21.2% | 14.9% |
| GPT-5.6 Sol (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Luna (max) | 0.0% | 0.0% | 25.2% | 0.0% | 2.3% |
| GPT-6 Sol (max) | 0.0% | 0.0% | 0.4% | 0.0% | 0.0% |
| GPT-6.1 Sol (max) | 100.0% | 58.9% | 36.1% | 40.0% | 54.9% |
| Gemini 3.8 Flash (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Gemini 4 Argon (high) | 0.0% | 10.2% | 8.4% | 14.9% | 10.5% |
| Grok 4.7 (xhigh) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Muse Spark 1.3 (max) | 0.0% | 0.0% | 0.1% | 0.0% | 0.0% |
| Muse Wonder (max) | 0.0% | 0.1% | 0.5% | 0.8% | 0.1% |
| Qwen3.8 Max | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |

### API basis: rank 3 or better

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M |
|---|---:|---:|---:|---:|---:|
| Claude Fable 5.1 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Haiku 5.5 (xhigh) | 0.0% | 3.2% | 5.9% | 4.0% | 3.1% |
| Claude Opus 5 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Sonnet 5.5 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| DeepSeek V4 Flash (max) | 0.0% | 30.0% | 30.2% | 30.2% | 30.0% |
| DeepSeek V4 Pro (max) | 0.0% | 4.3% | 6.0% | 8.0% | 4.6% |
| GLM-5.3 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-5.6 Luna (max) | 0.0% | 35.2% | 34.1% | 36.8% | 35.6% |
| GPT-5.6 Sol (max) | 0.0% | 0.1% | 0.4% | 0.2% | 0.1% |
| GPT-6 Astra (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Luna (max) | 100.0% | 89.4% | 86.6% | 77.6% | 89.3% |
| GPT-6 Sol (max) | 0.0% | 4.6% | 5.6% | 5.3% | 4.6% |
| GPT-6.1 Sol (max) | 100.0% | 99.5% | 95.6% | 97.7% | 99.1% |
| Gemini 3.8 Flash (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Gemini 4 Argon (high) | 100.0% | 29.9% | 29.5% | 33.4% | 29.7% |
| Grok 4.7 (xhigh) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Muse Spark 1.3 (max) | 0.0% | 1.2% | 2.6% | 1.5% | 1.2% |
| Muse Wonder (max) | 0.0% | 2.7% | 3.6% | 5.4% | 2.6% |
| Qwen3.8 Max | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |

### API basis: on the frontier

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M |
|---|---:|---:|---:|---:|---:|
| Claude Fable 5.1 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Haiku 5.5 (xhigh) | 0.0% | 17.8% | 15.6% | 22.5% | 17.7% |
| Claude Opus 5 (max) | 0.0% | 3.0% | 3.4% | 5.0% | 2.7% |
| Claude Opus 5.5 (max) | 0.0% | 0.0% | 14.9% | 0.0% | 12.0% |
| Claude Sonnet 5.5 (max) | 0.0% | 40.1% | 36.5% | 35.9% | 39.8% |
| DeepSeek V4 Flash (max) | 100.0% | 56.9% | 54.0% | 57.7% | 56.9% |
| DeepSeek V4 Pro (max) | 1.2% | 37.0% | 36.2% | 35.7% | 37.6% |
| GLM-5.3 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-5.6 Luna (max) | 100.0% | 50.5% | 50.4% | 45.2% | 50.6% |
| GPT-5.6 Sol (max) | 0.0% | 9.2% | 8.0% | 13.0% | 8.2% |
| GPT-6 Astra (max) | 0.0% | 0.0% | 0.1% | 0.0% | 0.5% |
| GPT-6 Luna (max) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% |
| GPT-6 Sol (max) | 0.0% | 11.5% | 11.2% | 21.1% | 11.5% |
| GPT-6.1 Sol (max) | 100.0% | 100.0% | 99.4% | 100.0% | 100.0% |
| Gemini 3.8 Flash (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Gemini 4 Argon (high) | 100.0% | 72.8% | 74.1% | 63.8% | 73.1% |
| Grok 4.7 (xhigh) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Muse Spark 1.3 (max) | 0.0% | 15.5% | 13.7% | 24.7% | 15.5% |
| Muse Wonder (max) | 0.0% | 29.3% | 27.9% | 29.9% | 29.7% |
| Qwen3.8 Max | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |

### API basis: value-score dispersion (SD; covariance term)

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M |
|---|---:|---:|---:|---:|---:|
| Claude Fable 5.1 (max) | 0.00 (+0.00) | 0.00 (+0.00) | 0.72 (+0.00) | 0.00 (+0.00) | 0.16 (+0.00) |
| Claude Haiku 5.5 (xhigh) | 0.00 (+0.00) | 2.17 (+0.00) | 2.45 (+0.00) | 2.66 (+0.00) | 2.14 (+0.00) |
| Claude Opus 5 (max) | 0.00 (+0.00) | 3.03 (+0.00) | 3.36 (+0.00) | 3.71 (+0.00) | 3.05 (+0.00) |
| Claude Opus 5.5 (max) | 0.00 (+0.00) | 0.00 (+0.00) | 0.81 (+0.00) | 0.00 (+0.00) | 0.13 (+0.00) |
| Claude Sonnet 5.5 (max) | 0.00 (+0.00) | 0.00 (+0.00) | 0.77 (+0.00) | 0.00 (+0.00) | 0.13 (+0.00) |
| DeepSeek V4 Flash (max) | 0.00 (+0.00) | 3.05 (+0.00) | 3.37 (+0.00) | 3.72 (+0.00) | 3.10 (+0.00) |
| DeepSeek V4 Pro (max) | 0.00 (+0.00) | 3.08 (+0.00) | 3.40 (+0.00) | 3.76 (+0.00) | 3.09 (+0.00) |
| GLM-5.3 (max) | 0.00 (+0.00) | 0.00 (+0.00) | 1.14 (+0.00) | 0.00 (+0.00) | 0.14 (+0.00) |
| GPT-5.6 Luna (max) | 0.00 (+0.00) | 2.17 (+0.00) | 2.61 (+0.00) | 2.66 (+0.00) | 2.18 (+0.00) |
| GPT-5.6 Sol (max) | 0.00 (+0.00) | 2.19 (+0.00) | 2.50 (+0.00) | 2.66 (+0.00) | 2.17 (+0.00) |
| GPT-6 Astra (max) | 0.00 (+0.00) | 0.00 (+0.00) | 0.76 (+0.00) | 0.00 (+0.00) | 0.12 (+0.00) |
| GPT-6 Luna (max) | 0.00 (+0.00) | 0.00 (+0.00) | 1.42 (+0.00) | 0.00 (+0.00) | 0.12 (+0.00) |
| GPT-6 Sol (max) | 0.00 (+0.00) | 2.17 (+0.00) | 2.50 (+0.00) | 2.65 (+0.00) | 2.17 (+0.00) |
| GPT-6.1 Sol (max) | 0.00 (+0.00) | 0.00 (+0.00) | 0.78 (+0.00) | 0.00 (+0.00) | 0.13 (+0.00) |
| Gemini 3.8 Flash (high) | 0.00 (+0.00) | 0.00 (+0.00) | 1.51 (+0.00) | 0.00 (+0.00) | 0.15 (+0.00) |
| Gemini 4 Argon (high) | 0.00 (+0.00) | 2.16 (+0.00) | 2.56 (+0.00) | 2.65 (+0.00) | 2.17 (+0.00) |
| Grok 4.7 (xhigh) | 0.00 (+0.00) | 0.00 (+0.00) | 1.35 (+0.00) | 0.00 (+0.00) | 0.15 (+0.00) |
| Muse Spark 1.3 (max) | 0.00 (+0.00) | 2.17 (+0.00) | 2.53 (+0.00) | 2.64 (+0.00) | 2.17 (+0.00) |
| Muse Wonder (max) | 0.00 (+0.00) | 3.08 (+0.00) | 3.42 (+0.00) | 3.75 (+0.00) | 3.04 (+0.00) |
| Qwen3.8 Max | 0.00 (+0.00) | 0.00 (+0.00) | 0.97 (+0.00) | 0.00 (+0.00) | 0.16 (+0.00) |

Plan streams S1, S2, S1 endpoint-heavy and S1M run with owner-named transfers off (E167): Claude Haiku 5.5 (xhigh), Claude Opus 5 (max), Claude Sonnet 5.5 (max), GPT-5.6 Luna (max), GPT-5.6 Sol (max), GPT-6 Luna (max), GPT-6 Sol (max) depend on a transfer and are unevaluable there (—), never reselected or replaced by API cost.

### Plan basis: rank 1

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M |
|---|---:|---:|---:|---:|---:|
| Claude Fable 5.1 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Haiku 5.5 (xhigh) | 0.0% | — | — | — | — |
| Claude Opus 5 (max) | 0.0% | — | — | — | — |
| Claude Opus 5.5 (max) | 0.0% | 100.0% | 100.0% | 100.0% | 100.0% |
| Claude Sonnet 5.5 (max) | 100.0% | — | — | — | — |
| DeepSeek V4 Flash (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| DeepSeek V4 Pro (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GLM-5.3 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-5.6 Luna (max) | 0.0% | — | — | — | — |
| GPT-5.6 Sol (max) | 0.0% | — | — | — | — |
| GPT-6 Astra (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Luna (max) | 0.0% | — | — | — | — |
| GPT-6 Sol (max) | 0.0% | — | — | — | — |
| GPT-6.1 Sol (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Gemini 3.8 Flash (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Gemini 4 Argon (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Grok 4.7 (xhigh) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Muse Spark 1.3 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Muse Wonder (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Qwen3.8 Max | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |

### Plan basis: rank 3 or better

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M |
|---|---:|---:|---:|---:|---:|
| Claude Fable 5.1 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Haiku 5.5 (xhigh) | 0.0% | — | — | — | — |
| Claude Opus 5 (max) | 0.0% | — | — | — | — |
| Claude Opus 5.5 (max) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% |
| Claude Sonnet 5.5 (max) | 100.0% | — | — | — | — |
| DeepSeek V4 Flash (max) | 0.0% | 0.8% | 2.5% | 3.5% | 0.8% |
| DeepSeek V4 Pro (max) | 0.0% | 0.0% | 0.4% | 0.0% | 0.0% |
| GLM-5.3 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-5.6 Luna (max) | 0.0% | — | — | — | — |
| GPT-5.6 Sol (max) | 0.0% | — | — | — | — |
| GPT-6 Astra (max) | 0.0% | 78.7% | 77.6% | 63.4% | 78.9% |
| GPT-6 Luna (max) | 0.0% | — | — | — | — |
| GPT-6 Sol (max) | 0.0% | — | — | — | — |
| GPT-6.1 Sol (max) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% |
| Gemini 3.8 Flash (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Gemini 4 Argon (high) | 0.0% | 18.1% | 16.4% | 26.7% | 18.1% |
| Grok 4.7 (xhigh) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Muse Spark 1.3 (max) | 0.0% | 0.0% | 0.1% | 0.0% | 0.0% |
| Muse Wonder (max) | 0.0% | 2.5% | 3.0% | 6.4% | 2.2% |
| Qwen3.8 Max | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |

### Plan basis: on the frontier

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M |
|---|---:|---:|---:|---:|---:|
| Claude Fable 5.1 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Haiku 5.5 (xhigh) | 100.0% | — | — | — | — |
| Claude Opus 5 (max) | 0.0% | — | — | — | — |
| Claude Opus 5.5 (max) | 0.0% | 100.0% | 100.0% | 100.0% | 100.0% |
| Claude Sonnet 5.5 (max) | 100.0% | — | — | — | — |
| DeepSeek V4 Flash (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| DeepSeek V4 Pro (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GLM-5.3 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-5.6 Luna (max) | 100.0% | — | — | — | — |
| GPT-5.6 Sol (max) | 0.0% | — | — | — | — |
| GPT-6 Astra (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Luna (max) | 100.0% | — | — | — | — |
| GPT-6 Sol (max) | 0.0% | — | — | — | — |
| GPT-6.1 Sol (max) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% |
| Gemini 3.8 Flash (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Gemini 4 Argon (high) | 100.0% | 46.4% | 47.4% | 47.5% | 45.8% |
| Grok 4.7 (xhigh) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Muse Spark 1.3 (max) | 0.0% | 0.0% | 1.3% | 0.0% | 0.0% |
| Muse Wonder (max) | 0.0% | 20.8% | 21.7% | 23.0% | 20.9% |
| Qwen3.8 Max | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |

### Plan basis: value-score dispersion (SD; covariance term)

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M |
|---|---:|---:|---:|---:|---:|
| Claude Fable 5.1 (max) | 0.00 (+0.00) | 0.00 (+0.00) | 0.73 (+0.00) | 0.00 (+0.00) | 0.16 (+0.00) |
| Claude Haiku 5.5 (xhigh) | 0.00 (+0.00) | — | — | — | — |
| Claude Opus 5 (max) | 0.00 (+0.00) | — | — | — | — |
| Claude Opus 5.5 (max) | 0.00 (+0.00) | 0.00 (+0.00) | 0.81 (+0.00) | 0.00 (+0.00) | 0.13 (+0.00) |
| Claude Sonnet 5.5 (max) | 0.00 (+0.00) | — | — | — | — |
| DeepSeek V4 Flash (max) | 0.00 (+0.00) | 3.07 (+0.00) | 3.32 (+0.00) | 3.72 (+0.00) | 3.04 (+0.00) |
| DeepSeek V4 Pro (max) | 0.00 (+0.00) | 3.05 (+0.00) | 3.38 (+0.00) | 3.78 (+0.00) | 3.07 (+0.00) |
| GLM-5.3 (max) | 0.00 (+0.00) | 0.00 (+0.00) | 1.14 (+0.00) | 0.00 (+0.00) | 0.14 (+0.00) |
| GPT-5.6 Luna (max) | 0.00 (+0.00) | — | — | — | — |
| GPT-5.6 Sol (max) | 0.00 (+0.00) | — | — | — | — |
| GPT-6 Astra (max) | 0.00 (+0.00) | 0.00 (+0.00) | 0.76 (+0.00) | 0.00 (+0.00) | 0.12 (+0.00) |
| GPT-6 Luna (max) | 0.00 (+0.00) | — | — | — | — |
| GPT-6 Sol (max) | 0.00 (+0.00) | — | — | — | — |
| GPT-6.1 Sol (max) | 0.00 (+0.00) | 0.00 (+0.00) | 0.78 (+0.00) | 0.00 (+0.00) | 0.13 (+0.00) |
| Gemini 3.8 Flash (high) | 0.00 (+0.00) | 0.00 (+0.00) | 1.51 (+0.00) | 0.00 (+0.00) | 0.15 (+0.00) |
| Gemini 4 Argon (high) | 0.00 (+0.00) | 2.16 (+0.00) | 2.55 (+0.00) | 2.65 (+0.00) | 2.16 (+0.00) |
| Grok 4.7 (xhigh) | 0.00 (+0.00) | 0.00 (+0.00) | 1.35 (+0.00) | 0.00 (+0.00) | 0.15 (+0.00) |
| Muse Spark 1.3 (max) | 0.00 (+0.00) | 2.16 (+0.00) | 2.54 (+0.00) | 2.65 (+0.00) | 2.16 (+0.00) |
| Muse Wonder (max) | 0.00 (+0.00) | 3.06 (+0.00) | 3.37 (+0.00) | 3.75 (+0.00) | 3.06 (+0.00) |
| Qwen3.8 Max | 0.00 (+0.00) | 0.00 (+0.00) | 0.98 (+0.00) | 0.00 (+0.00) | 0.16 (+0.00) |

### Named S2 specification branches

- **Bug Hunt harness band (E19)** (S2): unevaluable; the captured tbench.ai leaderboard lists no configuration under two or more agents, so no cross-agent spread exists
- **cache-hit variation (E34)** (S2): unevaluable; AA's published cost embeds its cache-pricing protocol; varying the cache-hit rate needs each basket component's cache-read and uncached-input demand, which AA publishes only for the whole Index (E157)
- **first-party list versus cross-provider median price rule (E122)** (S2): unevaluable; AA publishes one price per configuration under its own rule; the alternative rule's prices are not captured

### Cheapest-above-the-bar labels (API basis)

The 90% rule's error bound holds per published event (candidate and kernel assignment); it is not corrected across the listed candidates (E198). Each kernel assignment code gives the kernel used for the candidate and the competitors, in that order (U uniform, H endpoint-heavy; a quality-level bar has no reference rows, so it takes no letter); the label needs every assignment met.

| Bar | Candidate | Reading | Frequency range | Kernel assignments | Label |
|---|---|---|---|---|---|
| quality 58.3 | GPT-6.1 Sol (max) | supported under all registered role-group kernel checks | 93.7% to 98.8% | UU met, UH met, HU met, HH met | yes |
| quality 58.3 | DeepSeek V4 Flash (max) | not scenario-supported | 0.0% to 0.6% | UU not met, UH not met, HU not met, HH not met | no |
| quality 58.3 | DeepSeek V4 Pro (max) | not scenario-supported | 1.2% to 5.7% | UU not met, UH not met, HU not met, HH not met | no |

## Diagnostics

- **Terminal-Bench same-harness (Terminus 2):** undefined (panel too small); 13 rows ran on mixed harnesses.
- **Quality agreement:** quality agreement (matched-panel sensitivity): Kendall tau 0.87 (interval 0.62 to 1.00) on 13 rows.
- **Quality-substitution value agreement (API):** quality-substitution value agreement, api basis (matched-panel sensitivity): Kendall tau 0.31 (interval -0.22 to 0.68) on 13 rows.
- **Quality-substitution value agreement (Plan):** quality-substitution value agreement, plan basis (matched-panel sensitivity): Kendall tau 0.67 (interval 0.24 to 0.92) on 13 rows.
- **Disjoint-evidence agreement:** disjoint-evidence agreement (restricted evidence comparison, not an eligible ranking): Kendall tau 0.69 (interval 0.42 to 0.91) on 13 rows.
- **Quality source shares:** AA-run 80%, independent 20%.
- **Non-discriminating leaves:** lcr.
- **Group drift:** estimated; flagged: none.
- **Omniscience abstention sensitivity** (z_pen = max(0, I)): 17 rows move; largest move 4 (Claude Opus 5.5 (max), DeepSeek V4 Pro (max)).
- **GDPval-AA logistic sensitivity** (z = 100 / (1 + 10^((1600 - E) / 400)) against AA's pinned anchor; every other input fixed): API 17 rows move; largest move 4 (DeepSeek V4 Pro (max), Gemini 3.8 Flash (high)); Plan 9 rows move; largest move 2 (Claude Fable 5.1 (max)).
- **Anchor stability:** trimmed anchors (P10 / 2 and P90 x 2 (diagnostic only)) give $144.78 to $17,722.46; 13 rows move; largest move 3 (Claude Haiku 5.5 (xhigh), Muse Wonder (max)).

- **Basket readiness (E22):** priced leaves cover 67% of nominal quality weight (AutomationBench-AA, DeepSWE v1.1, GDPval-AA v2.1, AA-LCR v1.1, SciCode, Terminal-Bench 4.0 (tbench.ai)); pending components: FrontierCode, ITBench-AA.
- **SWE cost companion (O14, diagnostic):** 20 rows evaluated; flagged far from the median ratio: none.
- **Matched-cost diagnostic (E55):** evaluated at 50% priced quality weight; basket/matched cost-order reversals with separated intervals: 5; rank-gap warnings: 0.
- **Frontier-families anchors (E187, diagnostic):** anchors rebuilt from the 8 frontier and near-frontier references move API no rank changes (value points per cost doubling 3.04 vs 3.04 frozen); Plan 3 rows move; largest move 2 (GPT-6 Luna (max)) (value points per cost doubling 2.17 vs 2.02 frozen).
- **Frontier-families bar (E199, sensitivity; the frozen bar stays primary):** quality 60.9 over 8 configurations; cheapest at or above it on the API main workload: GPT-6.1 Sol (max) (confirmed) (compares 10 configurations that can qualify).

### Leave-one-component-out cost family (E172)

Each admitted basket unit removed in turn, scored on anchors rebuilt by the freeze rule (rank changes against the primary ranking; quality held fixed).

| Removed component | API rank changes | Plan rank changes | API value points per cost doubling |
|---|---|---|---:|
| Coding Agent Index | 14 rows move; largest move 5 (DeepSeek V4 Flash (max)) | 8 rows move; largest move 1 (Claude Fable 5.1 (max), Claude Opus 5 (max), DeepSeek V4 Pro (max), Gemini 4 Argon (high), GPT-5.6 Luna (max), GPT-5.6 Sol (max), GPT-6 Sol (max), Grok 4.7 (xhigh)) | 2.77 |
| AA-Briefcase | 8 rows move; largest move 2 (Claude Opus 5.5 (max), Claude Sonnet 5.5 (max), DeepSeek V4 Pro (max), GPT-5.6 Sol (max)) | no rank changes | 3.00 |
| GDPval-AA | 6 rows move; largest move 2 (Claude Sonnet 5.5 (max), DeepSeek V4 Pro (max)) | 2 rows move; largest move 1 (GPT-6 Luna (max), GPT-6 Sol (max)) | 2.98 |
| GDP.pdf | 6 rows move; largest move 2 (Claude Sonnet 5.5 (max), DeepSeek V4 Pro (max)) | no rank changes | 2.96 |
| AutomationBench-AA | 6 rows move; largest move 1 (Claude Fable 5.1 (max), Claude Haiku 5.5 (xhigh), Claude Opus 5 (max), DeepSeek V4 Pro (max), Gemini 3.8 Flash (high), GLM-5.3 (max)) | 4 rows move; largest move 1 (Gemini 3.8 Flash (high), GLM-5.3 (max), GPT-6 Luna (max), GPT-6 Sol (max)) | 2.94 |
| Terminal-Bench 4.0 (AA Index run) | 2 rows move; largest move 1 (Claude Haiku 5.5 (xhigh), DeepSeek V4 Pro (max)) | no rank changes | 2.96 |
| SciCode | 4 rows move; largest move 2 (Claude Sonnet 5.5 (max), DeepSeek V4 Pro (max)) | no rank changes | 2.96 |
| AA-LCR | 4 rows move; largest move 2 (Claude Sonnet 5.5 (max), DeepSeek V4 Pro (max)) | no rank changes | 2.96 |

### Subset rows: paired bridge and missing spend (E10, E173)

- **MiMo-V2.6-Flash, MiMo-V2.6-Pro** (subset without Coding Agent Index): Coding Agent Index is 40% of the full basket (median; 9% to 63% over 20 rows). Scored on its own subset anchors, the direction of its subset effect is not known. Paired bridge on the 20 full rows: API: the full rows' values change by -0.36 points (median; -2.59 to 1.20), 10 rows move; largest move 4 (Claude Haiku 5.5 (xhigh), DeepSeek V4 Flash (max), DeepSeek V4 Pro (max)); Plan: the full rows' values change by -0.37 points (median; -1.61 to 0.42), 8 rows move; largest move 1 (Claude Fable 5.1 (max), Claude Opus 5 (max), DeepSeek V4 Pro (max), Gemini 4 Argon (high), GPT-5.6 Luna (max), GPT-5.6 Sol (max), GPT-6 Sol (max), Grok 4.7 (xhigh)).

### Deletion sensitivity

| Branch | Retained nominal weight | Status | API rank changes | Plan rank changes |
|---|---:|---|---|---|
| leave-out:deepswe | 70% | evaluated | 20 rows move; largest move 7 (Claude Opus 5.5 (max)) | 16 rows move; largest move 5 (GPT-5.6 Luna (max), MiMo-V2.6-Flash) |
| leave-out:bugHunt | 90% | evaluated | 17 rows move; largest move 4 (Claude Opus 5 (max), MiMo-V2.6-Pro) | 8 rows move; largest move 4 (MiMo-V2.6-Flash) |
| leave-out:frontierCode | 90% | evaluated | 14 rows move; largest move 3 (Claude Sonnet 5.5 (max), DeepSeek V4 Pro (max), GPT-5.6 Sol (max)) | 14 rows move; largest move 2 (GPT-5.6 Sol (max), GPT-6 Luna (max), MiMo-V2.6-Flash, Muse Wonder (max)) |
| leave-out:terminalBench | 90% | evaluated | 14 rows move; largest move 4 (GPT-5.6 Sol (max)) | 10 rows move; largest move 4 (Claude Opus 5 (max)) |
| leave-out:gdpval | 90% | evaluated | 7 rows move; largest move 2 (GPT-6 Astra (max)) | 10 rows move; largest move 2 (Claude Opus 5 (max), Gemini 4 Argon (high), GPT-6 Sol (max), MiMo-V2.6-Flash) |
| leave-out:automationBench | 90% | evaluated | 13 rows move; largest move 3 (Claude Opus 5 (max)) | 5 rows move; largest move 2 (MiMo-V2.6-Flash) |
| leave-out:omniscience | 90% | evaluated | 9 rows move; largest move 3 (Gemini 3.8 Flash (high), GLM-5.3 (max)) | 9 rows move; largest move 3 (Claude Opus 5 (max)) |
| leave-out:lcr | 95% | evaluated | 9 rows move; largest move 4 (DeepSeek V4 Pro (max)) | 6 rows move; largest move 2 (Gemini 4 Argon (high), MiMo-V2.6-Flash) |
| leave-out:hle | 98% | evaluated | no rank changes | no rank changes |
| leave-out:scicode | 98% | evaluated | 3 rows move; largest move 2 (DeepSeek V4 Pro (max)) | no rank changes |
| leave-out:critpt | 98% | evaluated | 2 rows move; largest move 1 (Claude Sonnet 5.5 (max), GPT-5.6 Sol (max)) | 2 rows move; largest move 1 (GPT-6 Astra (max), MiMo-V2.6-Flash) |
| leave-source-out:Artificial Analysis | 20% | not identifiable under the coverage rule | — | — |
| basket-scope | 87% | evaluated | 13 rows move; largest move 3 (Gemini 3.8 Flash (high), GLM-5.3 (max)) | 10 rows move; largest move 7 (MiMo-V2.6-Flash) |

### Cost-component removal (Terminal-Bench 4.0 (AA Index run): evaluated)

| Basis | Run | Rank changes |
|---|---|---|
| api | cost-component removal, original anchors | 2 rows move; largest move 1 (Claude Haiku 5.5 (xhigh), DeepSeek V4 Pro (max)) |
| api | alternative workload, recalibrated anchors | 2 rows move; largest move 1 (Claude Haiku 5.5 (xhigh), DeepSeek V4 Pro (max)) |
| plan | cost-component removal, original anchors; fixed-multiple arithmetic stress (not identified Plan economics for the altered workload) | no rank changes |
| plan | alternative workload, recalibrated anchors; fixed-multiple arithmetic stress (not identified Plan economics for the altered workload) | no rank changes |

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
