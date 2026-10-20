# ValueRank v3.0.0 Scores

**Updated:** October 19, 2026 · methodology 3.0.0 · SDLC basket v1 · anchor version `v3-2026-10-19`

Value = 25% × cost score + 75% × quality. Costs are USD per basket run; the cost score is log-scaled against the frozen anchors of the row's workload (see [methodology.md](methodology.md)).

## Ranking

| Configuration | Plan rank | Plan value | Plan cost score | API rank | API value | API cost score | Quality | Quality coverage | Workload |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| [Claude Sonnet 5.5 (max)](https://valuerank.alolabs.dev/models/claude-sonnet-5-5/) | 1 | 61.13 | 51.58 | 13 | 51.55 | 13.26 | 64.32 | 100% | main |
| [Claude Opus 5.5 (max)](https://valuerank.alolabs.dev/models/claude-opus-5-5/) | 2 | 60.86 | 50.84 | 14 | 51.18 | 12.15 | 64.19 | 100% | main |
| [GPT-6.1 Sol (max)](https://valuerank.alolabs.dev/models/gpt-6-1-sol/) | 3 | 59.77 | 55.09 | 2 | 58.08 | 48.32 | 61.33 | 100% | main |
| [Claude Haiku 5.5 (xhigh)](https://valuerank.alolabs.dev/models/claude-haiku-5-5/) | 4 | 57.00 | 91.94 | 10 | 52.53 | 74.05 | 45.36 | 90% | main |
| [GPT-6 Astra (xhigh)](https://valuerank.alolabs.dev/models/gpt-6-astra/) | 5 | 56.58 | 34.83 | 8 | 53.82 | 23.81 | 63.82 | 40% | subset |
| [Claude Opus 5 (max)](https://valuerank.alolabs.dev/models/claude-opus-5/) | 6 | 56.45 | 52.40 | 18 | 46.98 | 14.50 | 57.81 | 80% | main |
| [GPT-6 Sol (max)](https://valuerank.alolabs.dev/models/gpt-6-sol/) | 7 | 56.15 | 49.79 | 9 | 53.79 | 40.34 | 58.28 | 90% | main |
| [GPT-6 Luna (max)](https://valuerank.alolabs.dev/models/gpt-6-luna/) | 8 | 56.14 | 81.33 | 3 | 57.77 | 87.85 | 47.74 | 100% | main |
| [GPT-5.6 Luna (max)](https://valuerank.alolabs.dev/models/gpt-5-6-luna/) | 9 | 55.29 | 71.13 | 6 | 55.63 | 72.49 | 50.01 | 90% | main |
| [GPT-5.6 Sol (max)](https://valuerank.alolabs.dev/models/gpt-5-6-sol/) | 10 | 55.03 | 41.05 | 12 | 51.57 | 27.17 | 59.70 | 90% | main |
| [MiMo-V2.6-Flash](https://valuerank.alolabs.dev/models/mimo-v2-6-flash/) | 11 | 53.47 | 58.66 | 1 | 60.91 | 88.43 | 51.74 | 50% | subset |
| [Gemini 4 Argon (high)](https://valuerank.alolabs.dev/models/gemini-4-argon/) | 12 | 52.77 | 15.20 | 4 | 56.45 | 29.89 | 65.30 | 90% | main |
| [MiMo-V2.6-Pro](https://valuerank.alolabs.dev/models/mimo-v2-6-pro/) | 13 | 50.02 | 49.80 | 5 | 56.28 | 74.86 | 50.09 | 60% | subset |
| [DeepSeek V4 Flash (max)](https://valuerank.alolabs.dev/models/deepseek-v4-flash/) | 14 | 47.30 | 45.03 | 7 | 54.75 | 74.82 | 48.06 | 80% | main |
| [DeepSeek V4 Pro (max)](https://valuerank.alolabs.dev/models/deepseek-v4-pro/) | 15 | 45.69 | 32.77 | 11 | 51.59 | 56.36 | 50.00 | 80% | main |
| [Grok 4.7 (xhigh)](https://valuerank.alolabs.dev/models/grok-4-7/) | 16 | 44.54 | 8.06 | 16 | 47.31 | 19.15 | 56.70 | 100% | main |
| [GLM-5.3 (max)](https://valuerank.alolabs.dev/models/glm-5-3/) | 17 | 43.25 | 16.71 | 17 | 47.11 | 32.17 | 52.09 | 100% | main |
| [Gemini 3.8 Flash (high)](https://valuerank.alolabs.dev/models/gemini-3-8-flash/) | 18 | 43.13 | 21.71 | 15 | 47.62 | 39.70 | 50.26 | 100% | main |
| [Qwen3.8 Max](https://valuerank.alolabs.dev/models/qwen3-8-max/) | 19 | 38.42 | 10.54 | 19 | 41.50 | 22.87 | 47.71 | 100% | main |

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
| Grok 4.6 | No exact-variant AA DeepSWE result in the selected source snapshot; Not a required AA frontier or near-frontier family model |
| Kimi K3 | No exact-variant AA DeepSWE result in the selected source snapshot; Not a required AA frontier or near-frontier family model |
| Muse Spark 1.2 | No exact-variant AA DeepSWE result in the selected source snapshot; Not a required AA frontier or near-frontier family model |

## Quality leaf scores

Each leaf's score z on its fixed 0–100 anchors; "—" marks a leaf with no eligible exact-configuration result.

| Configuration | DeepSWE v1.1 | Bug Hunt Bench | AA FrontierCode 1.1 | Terminal-Bench 4.0 (tbench.ai) | GDPval-AA v2.1 | AutomationBench-AA | AA-Omniscience | AA-LCR v1.1 | Humanity's Last Exam | SciCode | CritPt | Quality | Provisional |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Claude Sonnet 5.5 (max) | 72.0 | 48.9 | 45.8 | 61.8 | 66.9 | 71.8 | 66.2 | 82.7 | 55.0 | 61.0 | 31.4 | 64.32 | no |
| Claude Opus 5.5 (max) | 68.4 | 39.7 | 52.2 | 64.8 | 68.3 | 69.5 | 73.2 | 84.7 | 61.4 | 66.9 | 31.7 | 64.19 | no |
| GPT-6.1 Sol (max) | 69.6 | 42.2 | 49.1 | 58.2 | 54.7 | 64.9 | 70.8 | 83.0 | 52.9 | 54.2 | 31.7 | 61.33 | no |
| Claude Haiku 5.5 (xhigh) | 49.0 | 17.4 | 45.5 | — | 50.7 | 36.0 | 53.0 | 78.3 | 42.7 | 51.7 | 22.6 | 45.36 | no |
| GPT-6 Astra (xhigh) | — | — | — | — | 52.8 | 67.2 | 71.7 | 80.0 | 54.6 | 55.7 | 31.4 | 63.82 | coverage 40% below 70%; 0 SWE leaves observed (need 2); observed SWE weight 0% below 40%; DeepSWE v1.1 missing |
| Claude Opus 5 (max) | 62.5 | 25.7 | — | — | 61.1 | 56.6 | 68.5 | 79.3 | 54.9 | 56.4 | 29.1 | 57.81 | no |
| GPT-6 Sol (max) | 69.0 | 27.9 | — | 49.4 | 50.4 | 61.6 | 63.6 | 83.7 | 47.9 | 57.6 | 30.9 | 58.28 | no |
| GPT-6 Luna (max) | 63.7 | 17.4 | 41.9 | 16.4 | 46.6 | 53.2 | 50.3 | 83.3 | 38.5 | 54.6 | 19.4 | 47.74 | no |
| GPT-5.6 Luna (max) | 66.4 | 29.8 | — | 17.3 | 48.0 | 50.2 | 44.9 | 83.7 | 39.5 | 53.6 | 20.6 | 50.01 | no |
| GPT-5.6 Sol (max) | 72.3 | 41.4 | — | 37.3 | 55.4 | 60.1 | 61.0 | 84.0 | 49.5 | 57.1 | 32.3 | 59.70 | no |
| MiMo-V2.6-Flash | — | — | 42.1 | — | 55.4 | 64.1 | 43.7 | 74.3 | 35.1 | 51.3 | 12.0 | 51.74 | coverage 50% below 70%; 1 SWE leaves observed (need 2); observed SWE weight 10% below 40%; DeepSWE v1.1 missing |
| Gemini 4 Argon (high) | 78.8 | 38.8 | 43.5 | — | 56.2 | 77.5 | 71.2 | 79.7 | 57.1 | 61.8 | 27.1 | 65.30 | no |
| MiMo-V2.6-Pro | — | 17.1 | 45.4 | — | 59.2 | 58.6 | 54.2 | 86.3 | 49.4 | 60.9 | 26.6 | 50.09 | coverage 60% below 70%; observed SWE weight 20% below 40%; DeepSWE v1.1 missing |
| DeepSeek V4 Flash (max) | 54.3 | 20.7 | — | — | 46.7 | 54.0 | 42.9 | 79.7 | 38.6 | 50.3 | 16.6 | 48.06 | no |
| DeepSeek V4 Pro (max) | 57.2 | 15.2 | — | — | 47.5 | 56.7 | 50.4 | 80.3 | 41.0 | 51.0 | 18.0 | 50.00 | no |
| Grok 4.7 (xhigh) | 72.6 | 27.6 | 33.8 | 37.6 | 60.6 | 65.6 | 66.0 | 76.7 | 43.1 | 57.4 | 17.7 | 56.70 | no |
| GLM-5.3 (max) | 61.4 | 18.1 | 40.1 | 41.8 | 57.5 | 62.2 | 57.1 | 79.7 | 42.3 | 59.0 | 19.1 | 52.09 | no |
| Gemini 3.8 Flash (high) | 65.8 | 17.1 | 36.4 | 19.1 | 46.8 | 59.9 | 64.8 | 81.3 | 47.8 | 56.6 | 18.3 | 50.26 | no |
| Qwen3.8 Max | 51.0 | 24.5 | 43.2 | 27.0 | 58.3 | 56.2 | 56.0 | 80.3 | 43.1 | 52.1 | 17.7 | 47.71 | no |

## Basket cost by component

USD at API rates for the exact configuration; "—" marks a component without an exact cost.

| Configuration | Coding Agent Index | FrontierCode | ITBench-AA | AA-Briefcase | GDPval-AA | GDP.pdf | AutomationBench-AA | Terminal-Bench 4.0 (AA Index run) | SciCode | AA-LCR | Basket cost | Missing admitted components |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Claude Sonnet 5.5 (max) | $4,299.81 | $826.00 | — | $1,863.13 | $1,504.30 | $79.43 | $678.32 | $834.67 | $80.07 | $33.93 | $9,373.65 | none |
| Claude Opus 5.5 (max) | $3,950.02 | $1,015.00 | $146.00 | $1,915.18 | $1,962.05 | $155.23 | $938.69 | $865.21 | $135.11 | $67.66 | $9,989.15 | none |
| GPT-6.1 Sol (max) | $470.90 | $81.00 | — | $210.45 | $196.57 | $41.99 | $195.01 | $120.30 | $12.50 | $19.94 | $1,267.66 | none |
| Claude Haiku 5.5 (xhigh) | $184.98 | $16.00 | — | $33.29 | $20.26 | $2.73 | $18.14 | $30.38 | $0.77 | $1.53 | $292.07 | none |
| GPT-6 Astra (xhigh) | — | — | — | $597.28 | $668.39 | $191.27 | $924.00 | $386.46 | $35.03 | $96.99 | $2,899.42 | Coding Agent Index |
| Claude Opus 5 (max) | $3,269.11 | — | — | $1,619.19 | $1,488.52 | $108.57 | $864.64 | $1,273.08 | $33.90 | $76.11 | $8,733.13 | none |
| GPT-6 Sol (max) | $905.89 | — | $38.00 | $238.81 | $280.84 | $42.54 | $235.06 | $264.22 | $12.24 | $19.82 | $1,999.41 | none |
| GPT-6 Luna (max) | $53.30 | $9.00 | — | $15.47 | $19.66 | $2.85 | $23.91 | $15.59 | $1.06 | $1.02 | $132.87 | none |
| GPT-5.6 Luna (max) | $132.72 | — | — | $35.95 | $24.18 | $5.68 | $59.91 | $56.06 | $2.67 | $2.09 | $319.25 | none |
| GPT-5.6 Sol (max) | $1,925.06 | — | $106.00 | $365.84 | $618.22 | $92.85 | $638.90 | $534.15 | $22.95 | $40.16 | $4,238.14 | none |
| MiMo-V2.6-Flash | — | — | — | $13.81 | $16.10 | $2.01 | $10.94 | $15.19 | $0.81 | $1.51 | $60.37 | Coding Agent Index |
| Gemini 4 Argon (high) | $1,770.70 | $670.00 | — | $530.33 | $400.23 | $25.93 | $399.89 | $447.49 | $30.44 | $23.64 | $3,628.64 | none |
| MiMo-V2.6-Pro | — | $18.00 | — | $34.60 | $35.47 | $2.40 | $27.77 | $28.91 | $2.25 | $4.74 | $136.13 | Coding Agent Index |
| DeepSeek V4 Flash (max) | $25.77 | — | — | $38.53 | $63.77 | $4.66 | $69.22 | $60.65 | $12.16 | $4.76 | $279.51 | none |
| DeepSeek V4 Pro (max) | $72.13 | — | — | $90.59 | $127.70 | $11.00 | $223.87 | $247.85 | $14.47 | $13.89 | $801.50 | none |
| Grok 4.7 (xhigh) | $2,671.69 | $1,131.00 | $203.00 | $846.62 | $1,415.17 | $32.43 | $707.44 | $963.85 | $38.30 | $24.51 | $6,700.02 | none |
| GLM-5.3 (max) | $1,285.14 | $432.00 | $91.00 | $514.04 | $496.54 | $17.34 | $302.51 | $532.24 | $23.62 | $14.86 | $3,186.29 | none |
| Gemini 3.8 Flash (high) | $747.62 | $372.00 | $86.00 | $245.87 | $372.82 | $10.90 | $278.70 | $385.54 | $22.12 | $9.88 | $2,073.44 | none |
| Qwen3.8 Max | $1,054.13 | $675.00 | $327.00 | $1,781.49 | $998.39 | $33.31 | $261.64 | $1,232.62 | $32.57 | $22.88 | $5,417.03 | none |

### Valuation basis

Valuation-basis gate (E170): 19 compatible as captured. AA's Index category costs reconcile exactly with the prices AA displays for each configuration at capture, so its applied prices are the prices in force at the release cutoff. Token metering (E176): 19 not published per configuration; AA values cached input at live measurements of each model's typical cache-hit rate. Source intervals (E174): terminalBench: captured, level 95% (tbench.ai: "The whiskers span the 95% confidence interval"); gdpval: published, not captured, level not stated by the source (the 95% level on AA's methodology page belongs to AA-Briefcase).

## Plan route selection

The Plan amount is the selected multiple times the cash paid for the fee period (E166), typed by what the measurement establishes; it is not capacity unless it says so. The multiple values only the measured workload's API-equivalent consumption; other plan features are not valued.

| Configuration | Selected route | Plan amount | Identification | Plan cost (USD per basket run) | Flags | Selection reason |
|---|---|---|---|---:|---|---|
| Claude Sonnet 5.5 (max) | Claude Pro $20 · common Claude assumption (58.9×, assumption) | $1,178 per month: assumed API-equivalent consumption (owner-named transfer) from claude-pro-opus55-semianalysis | unidentified | $159.15 | workload-unmatched; owner-named transfer (assumption); valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| Claude Opus 5.5 (max) | Claude Pro $20 · Opus 5.5 (58.9×, measured) | $1,178 per month: measured-workload capacity | unidentified | $169.60 | workload-unmatched; valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| GPT-6.1 Sol (max) | ChatGPT Pro $500 · common GPT assumption (10.772×, measured) | $5,386 per month: measured-workload capacity | unidentified | $117.68 | workload-unmatched; valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| Claude Haiku 5.5 (xhigh) | Claude Pro $20 · common Claude assumption (58.9×, assumption) | $1,178 per month: assumed API-equivalent consumption (owner-named transfer) from claude-pro-opus55-semianalysis | unidentified | $4.96 | workload-unmatched; owner-named transfer (assumption); valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| GPT-6 Astra (xhigh) | ChatGPT Plus $20 · common GPT assumption (8.1×, measured) | $162 per month: measured-workload capacity | unidentified | $357.95 | workload-unmatched; valuation basis unverified | higher evidence grade |
| Claude Opus 5 (max) | Claude Pro $20 · common Claude assumption (58.9×, assumption) | $1,178 per month: assumed API-equivalent consumption (owner-named transfer) from claude-pro-opus55-semianalysis | unidentified | $148.27 | workload-unmatched; owner-named transfer (assumption); valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| GPT-6 Sol (max) | ChatGPT Pro $500 · common GPT assumption (10.772×, assumption) | $5,386 per month: assumed API-equivalent consumption (owner-named transfer) | unidentified | $185.61 | workload-unmatched; owner-named transfer (assumption); valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| GPT-6 Luna (max) | ChatGPT Pro $500 · common GPT assumption (10.772×, assumption) | $5,386 per month: assumed API-equivalent consumption (owner-named transfer) | unidentified | $12.33 | workload-unmatched; owner-named transfer (assumption); valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| GPT-5.6 Luna (max) | ChatGPT Pro $500 · common GPT assumption (10.772×, assumption) | $5,386 per month: assumed API-equivalent consumption (owner-named transfer) | unidentified | $29.64 | workload-unmatched; owner-named transfer (assumption); valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| GPT-5.6 Sol (max) | ChatGPT Pro $500 · common GPT assumption (10.772×, assumption) | $5,386 per month: assumed API-equivalent consumption (owner-named transfer) | unidentified | $393.44 | workload-unmatched; owner-named transfer (assumption); valuation basis unverified | larger observed multiple (observed-workload multiple — target-workload ordering not identified) |
| MiMo-V2.6-Flash | MiMo · provisional 1.5x assumption (1.5×, assumption) | fee not established: assumed API-equivalent consumption (owner-named transfer) | unidentified | $40.25 | workload-unmatched; owner-named transfer (assumption); valuation basis unverified; observed-usage multiple; full utilisation not established | only remaining eligible route |
| Gemini 4 Argon (high) | — | — | — | $3,628.64 | API-cost fallback: no admitted Plan route; cross-estimand ordering not identified | no eligible route |
| MiMo-V2.6-Pro | MiMo · provisional 1.5x assumption (1.5×, assumption) | fee not established: assumed API-equivalent consumption (owner-named transfer) | unidentified | $90.75 | workload-unmatched; owner-named transfer (assumption); valuation basis unverified; observed-usage multiple; full utilisation not established | only remaining eligible route |
| DeepSeek V4 Flash (max) | — | — | — | $279.51 | API-cost fallback: no admitted Plan route; cross-estimand ordering not identified | no eligible route |
| DeepSeek V4 Pro (max) | — | — | — | $801.50 | API-cost fallback: no admitted Plan route; cross-estimand ordering not identified | no eligible route |
| Grok 4.7 (xhigh) | — | — | — | $6,700.02 | API-cost fallback: no admitted Plan route; cross-estimand ordering not identified | no eligible route |
| GLM-5.3 (max) | — | — | — | $3,186.29 | API-cost fallback: no admitted Plan route; cross-estimand ordering not identified | no eligible route |
| Gemini 3.8 Flash (high) | — | — | — | $2,073.44 | API-cost fallback: no admitted Plan route; cross-estimand ordering not identified | no eligible route |
| Qwen3.8 Max | — | — | — | $5,417.03 | API-cost fallback: no admitted Plan route; cross-estimand ordering not identified | no eligible route |

### Route alternatives

Every admissible route-measurement pair in comparator order (E171) and the comparator's pick with the selected pair removed (E179). A larger displayed multiple is arithmetic on the measured workload, never a claim that the route is cheaper on the scored workload. Workday-feasible multiple (E15), for the 12 routed rows: not evaluated: no evidenced quota schema for this route.

| Configuration | Admissible pairs | Unidentified | Pairs (multiple, status) | Leave-selected-out choice |
|---|---:|---:|---|---|
| Claude Sonnet 5.5 (max) | 3 | 3 | claude-pro-common-opus55-assumption (58.9×, selected); claude-max20x-common-opus55-assumption (58.63×, not selected by the comparator); claude-max5x-common-opus55-assumption (57.25×, not selected by the comparator) | claude-max20x-common-opus55-assumption (58.63×, value 61.12) |
| Claude Opus 5.5 (max) | 3 | 3 | claude-pro-opus55-semianalysis (58.9×, selected); claude-max20x-opus55-semianalysis (58.63×, not selected by the comparator); claude-max5x-opus55-semianalysis (57.25×, not selected by the comparator) | claude-max20x-opus55-semianalysis (58.63×, value 60.84) |
| GPT-6.1 Sol (max) | 4 | 4 | chatgpt-pro500-common-semianalysis-assumption (10.772×, selected); chatgpt-pro100-common-semianalysis-assumption (10.55×, not selected by the comparator); chatgpt-pro200-common-semianalysis-assumption (10.42×, not selected by the comparator); chatgpt-plus-common-semianalysis-assumption (8.1×, not selected by the comparator) | chatgpt-pro100-common-semianalysis-assumption (10.55×, value 59.71) |
| Claude Haiku 5.5 (xhigh) | 3 | 3 | claude-pro-common-opus55-assumption (58.9×, selected); claude-max20x-common-opus55-assumption (58.63×, not selected by the comparator); claude-max5x-common-opus55-assumption (57.25×, not selected by the comparator) | claude-max20x-common-opus55-assumption (58.63×, value 56.99) |
| GPT-6 Astra (xhigh) | 4 | 4 | chatgpt-plus-common-semianalysis-assumption (8.1×, selected); chatgpt-pro500-common-semianalysis-assumption (10.772×, not selected by the comparator); chatgpt-pro100-common-semianalysis-assumption (10.55×, not selected by the comparator); chatgpt-pro200-common-semianalysis-assumption (10.42×, not selected by the comparator) | chatgpt-pro500-common-semianalysis-assumption (10.772×, value 57.35) |
| Claude Opus 5 (max) | 3 | 3 | claude-pro-common-opus55-assumption (58.9×, selected); claude-max20x-common-opus55-assumption (58.63×, not selected by the comparator); claude-max5x-common-opus55-assumption (57.25×, not selected by the comparator) | claude-max20x-common-opus55-assumption (58.63×, value 56.44) |
| GPT-6 Sol (max) | 4 | 4 | chatgpt-pro500-common-semianalysis-assumption (10.772×, selected); chatgpt-pro100-common-semianalysis-assumption (10.55×, not selected by the comparator); chatgpt-pro200-common-semianalysis-assumption (10.42×, not selected by the comparator); chatgpt-plus-common-semianalysis-assumption (8.1×, not selected by the comparator) | chatgpt-pro100-common-semianalysis-assumption (10.55×, value 56.09) |
| GPT-6 Luna (max) | 4 | 4 | chatgpt-pro500-common-semianalysis-assumption (10.772×, selected); chatgpt-pro100-common-semianalysis-assumption (10.55×, not selected by the comparator); chatgpt-pro200-common-semianalysis-assumption (10.42×, not selected by the comparator); chatgpt-plus-common-semianalysis-assumption (8.1×, not selected by the comparator) | chatgpt-pro100-common-semianalysis-assumption (10.55×, value 56.08) |
| GPT-5.6 Luna (max) | 4 | 4 | chatgpt-pro500-common-semianalysis-assumption (10.772×, selected); chatgpt-pro100-common-semianalysis-assumption (10.55×, not selected by the comparator); chatgpt-pro200-common-semianalysis-assumption (10.42×, not selected by the comparator); chatgpt-plus-common-semianalysis-assumption (8.1×, not selected by the comparator) | chatgpt-pro100-common-semianalysis-assumption (10.55×, value 55.23) |
| GPT-5.6 Sol (max) | 4 | 4 | chatgpt-pro500-common-semianalysis-assumption (10.772×, selected); chatgpt-pro100-common-semianalysis-assumption (10.55×, not selected by the comparator); chatgpt-pro200-common-semianalysis-assumption (10.42×, not selected by the comparator); chatgpt-plus-common-semianalysis-assumption (8.1×, not selected by the comparator) | chatgpt-pro100-common-semianalysis-assumption (10.55×, value 54.97) |
| MiMo-V2.6-Flash | 1 | 1 | mimo-provisional-user-assumption (1.5×, selected) | none: the row would fall back to API cost (O13) |
| MiMo-V2.6-Pro | 1 | 1 | mimo-provisional-user-assumption (1.5×, selected) | none: the row would fall back to API cost (O13) |

### Measured-only Plan view

Admission: exact-route measurement candidates of grade controlled or concordant reports (no transfers, no diagnostics). Selection: the official selector (E111, E88, E85) rerun among the admitted candidates. Panel: rows with an admitted measured candidate; others listed as 'no measured route' (no API fallback).

| Configuration | Status | Route | Plan cost | Value | Rank |
|---|---|---|---:|---:|---:|
| Claude Opus 5.5 (max) | measured, target-workload unmatched | claude-pro-opus55-semianalysis | $169.60 | 60.86 | 1 |
| GPT-6.1 Sol (max) | measured, target-workload unmatched | chatgpt-pro500-common-semianalysis-assumption | $117.68 | 59.77 | 2 |
| GPT-6 Astra (xhigh) | measured, target-workload unmatched | chatgpt-plus-common-semianalysis-assumption | $357.95 | 56.58 | 3 |
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
| Qwen3.8 Max | no measured route | — | — | — | — |

#### Measured-evidence calibration (diagnostic)

References: each workload's measured-only rows with complete cost evidence are the references: c_L = cheapest / 2, c_H = dearest x 2 (diagnostic only; the official anchors are unchanged). Status: evaluated.

- Workload `9a0d376cc6080f3c`: measured anchors $58.84 to $339.19 from Claude Opus 5.5 (max), GPT-6.1 Sol (max); anchor ratio 5.8 against the official 5404.5. Official Plan anchors are set by Claude Haiku 5.5 (xhigh) (owner-named transfer) at the low end and Grok 4.7 (xhigh) (API-cost fallback) at the high end.
- Workload `1453a9a0576b02ea`: measured-evidence calibration unavailable (fewer than two measured references); measured rows GPT-6 Astra (xhigh). Official Plan anchors are set by Claude Haiku 5.5 (xhigh) (owner-named transfer) at the low end and Qwen3.8 Max (API-cost fallback) at the high end.

| Configuration | Value on official Plan anchors | Value on measured anchors | Rank change |
|---|---:|---:|---:|
| Claude Opus 5.5 (max) | 60.86 | 58.04 | 1 |
| GPT-6.1 Sol (max) | 59.77 | 61.10 | -1 |

Pairwise reversals: Claude Opus 5.5 (max) and GPT-6.1 Sol (max). Largest value change: 2.82 points.

## Interval outputs

**API basis, main workload: frontier.** Not evaluable: GPT-6 Astra (xhigh), MiMo-V2.6-Flash, MiMo-V2.6-Pro.

| Configuration | Possible frontier | Definite frontier | Definite counterexample | Possible frontier blocked by |
|---|---|---|---|---|
| Gemini 4 Argon (high) | certified | disproved | GPT-6.1 Sol (max) | — |
| GPT-6.1 Sol (max) | certified | certified | — | — |
| Claude Sonnet 5.5 (max) | certified | disproved | Gemini 4 Argon (high) | — |
| Claude Opus 5.5 (max) | disproved | disproved | Gemini 4 Argon (high) | Claude Sonnet 5.5 (max) |
| GPT-5.6 Sol (max) | certified | disproved | Gemini 4 Argon (high) | — |
| GPT-6 Sol (max) | certified | disproved | GPT-6.1 Sol (max) | — |
| Grok 4.7 (xhigh) | disproved | disproved | Gemini 4 Argon (high) | Gemini 4 Argon (high), GPT-6.1 Sol (max) |
| GPT-5.6 Luna (max) | certified | disproved | GPT-6 Luna (max) | — |
| GPT-6 Luna (max) | certified | certified | — | — |
| Claude Haiku 5.5 (xhigh) | certified | disproved | GPT-6 Luna (max) | — |
| Gemini 3.8 Flash (high) | disproved | disproved | GPT-6.1 Sol (max) | GPT-6.1 Sol (max), GPT-6 Sol (max) |
| Claude Opus 5 (max) | certified | disproved | Gemini 4 Argon (high) | — |
| GLM-5.3 (max) | disproved | disproved | GPT-6.1 Sol (max) | GPT-6.1 Sol (max), GPT-6 Sol (max) |
| DeepSeek V4 Flash (max) | certified | disproved | GPT-6 Luna (max) | — |
| Qwen3.8 Max | disproved | disproved | Gemini 4 Argon (high) | Gemini 4 Argon (high), GPT-6.1 Sol (max), GPT-5.6 Sol (max), GPT-6 Sol (max), GPT-6 Luna (max), Gemini 3.8 Flash (high), GLM-5.3 (max) |
| DeepSeek V4 Pro (max) | certified | disproved | GPT-5.6 Luna (max) | — |

**API basis: cheapest at or above GPT-6 Luna (max)'s quality** (median definite-frontier configuration on the API basis at freeze, by displayed quality (lower median)). Status certified; confirmed cheapest: GPT-6 Luna (max).

| Configuration | Confirmed qualifies | Possibly qualifies | Possibly cheapest |
|---|---|---|---|
| Gemini 4 Argon (high) | certified | certified | disproved |
| GPT-6.1 Sol (max) | certified | certified | disproved |
| Claude Sonnet 5.5 (max) | certified | certified | disproved |
| Claude Opus 5.5 (max) | certified | certified | disproved |
| GPT-5.6 Sol (max) | certified | certified | disproved |
| GPT-6 Sol (max) | certified | certified | disproved |
| Grok 4.7 (xhigh) | certified | certified | disproved |
| GPT-5.6 Luna (max) | disproved | certified | disproved |
| GPT-6 Luna (max) | certified | certified | certified |
| Claude Haiku 5.5 (xhigh) | disproved | certified | disproved |
| Gemini 3.8 Flash (high) | certified | certified | disproved |
| Claude Opus 5 (max) | disproved | certified | disproved |
| GLM-5.3 (max) | certified | certified | disproved |
| DeepSeek V4 Flash (max) | disproved | certified | disproved |
| Qwen3.8 Max | disproved | disproved | disproved |
| DeepSeek V4 Pro (max) | disproved | certified | disproved |

**Plan basis:** not evaluated (no row has FullCost and an identified M_W (E61/E67)).

## Scenario shares

Frequencies over 10,000 scenarios per run (seed 20261017); streams are defined in [methodology.md](methodology.md#uncertainty-outputs).

### API basis: rank 1

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M |
|---|---:|---:|---:|---:|---:|
| Claude Haiku 5.5 (xhigh) | 0.0% | 0.0% | 0.8% | 0.0% | 0.0% |
| Claude Opus 5 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Sonnet 5.5 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| DeepSeek V4 Flash (max) | 0.0% | 17.1% | 14.3% | 20.1% | 16.4% |
| DeepSeek V4 Pro (max) | 0.0% | 0.6% | 1.4% | 2.5% | 0.6% |
| GLM-5.3 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-5.6 Luna (max) | 0.0% | 14.7% | 12.2% | 21.0% | 14.8% |
| GPT-5.6 Sol (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Luna (max) | 0.0% | 0.0% | 25.6% | 0.0% | 2.4% |
| GPT-6 Sol (max) | 0.0% | 0.0% | 0.4% | 0.0% | 0.0% |
| GPT-6.1 Sol (max) | 100.0% | 57.8% | 36.6% | 40.8% | 56.1% |
| Gemini 3.8 Flash (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Gemini 4 Argon (high) | 0.0% | 9.8% | 8.7% | 15.6% | 9.6% |
| Grok 4.7 (xhigh) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Qwen3.8 Max | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |

### API basis: rank 3 or better

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M |
|---|---:|---:|---:|---:|---:|
| Claude Haiku 5.5 (xhigh) | 0.0% | 3.7% | 6.9% | 4.5% | 3.7% |
| Claude Opus 5 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Opus 5.5 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Claude Sonnet 5.5 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| DeepSeek V4 Flash (max) | 0.0% | 31.3% | 31.3% | 30.5% | 31.3% |
| DeepSeek V4 Pro (max) | 0.0% | 4.9% | 5.9% | 8.7% | 4.2% |
| GLM-5.3 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-5.6 Luna (max) | 0.0% | 36.7% | 35.6% | 39.0% | 36.5% |
| GPT-5.6 Sol (max) | 0.0% | 0.2% | 0.3% | 0.5% | 0.2% |
| GPT-6 Luna (max) | 100.0% | 88.7% | 88.0% | 78.7% | 89.5% |
| GPT-6 Sol (max) | 0.0% | 4.9% | 6.2% | 5.8% | 5.1% |
| GPT-6.1 Sol (max) | 100.0% | 99.5% | 95.5% | 97.8% | 99.1% |
| Gemini 3.8 Flash (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Gemini 4 Argon (high) | 100.0% | 30.2% | 30.3% | 34.5% | 30.4% |
| Grok 4.7 (xhigh) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Qwen3.8 Max | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |

### API basis: on the frontier

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M |
|---|---:|---:|---:|---:|---:|
| Claude Haiku 5.5 (xhigh) | 0.0% | 18.0% | 15.3% | 23.0% | 17.8% |
| Claude Opus 5 (max) | 0.0% | 4.5% | 4.9% | 7.7% | 4.6% |
| Claude Opus 5.5 (max) | 0.0% | 0.0% | 20.9% | 0.0% | 16.7% |
| Claude Sonnet 5.5 (max) | 0.0% | 55.3% | 50.3% | 49.8% | 54.0% |
| DeepSeek V4 Flash (max) | 100.0% | 57.5% | 54.4% | 56.9% | 57.5% |
| DeepSeek V4 Pro (max) | 1.0% | 37.4% | 36.3% | 36.1% | 37.0% |
| GLM-5.3 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-5.6 Luna (max) | 100.0% | 50.5% | 50.3% | 45.9% | 50.0% |
| GPT-5.6 Sol (max) | 0.0% | 8.8% | 8.4% | 14.4% | 8.3% |
| GPT-6 Luna (max) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% |
| GPT-6 Sol (max) | 0.0% | 11.5% | 11.2% | 21.9% | 11.6% |
| GPT-6.1 Sol (max) | 100.0% | 100.0% | 99.3% | 100.0% | 100.0% |
| Gemini 3.8 Flash (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Gemini 4 Argon (high) | 100.0% | 73.8% | 75.4% | 65.2% | 73.8% |
| Grok 4.7 (xhigh) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Qwen3.8 Max | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |

### API basis: value-score dispersion (SD; covariance term)

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M |
|---|---:|---:|---:|---:|---:|
| Claude Haiku 5.5 (xhigh) | 0.00 (+0.00) | 2.17 (+0.00) | 2.45 (+0.00) | 2.64 (+0.00) | 2.16 (+0.00) |
| Claude Opus 5 (max) | 0.00 (+0.00) | 3.07 (+0.00) | 3.34 (+0.00) | 3.72 (+0.00) | 3.07 (+0.00) |
| Claude Opus 5.5 (max) | 0.00 (+0.00) | 0.00 (+0.00) | 0.80 (+0.00) | 0.00 (+0.00) | 0.13 (+0.00) |
| Claude Sonnet 5.5 (max) | 0.00 (+0.00) | 0.00 (+0.00) | 0.77 (+0.00) | 0.00 (+0.00) | 0.13 (+0.00) |
| DeepSeek V4 Flash (max) | 0.00 (+0.00) | 3.06 (+0.00) | 3.31 (+0.00) | 3.73 (+0.00) | 3.07 (+0.00) |
| DeepSeek V4 Pro (max) | 0.00 (+0.00) | 3.09 (+0.00) | 3.34 (+0.00) | 3.76 (+0.00) | 3.04 (+0.00) |
| GLM-5.3 (max) | 0.00 (+0.00) | 0.00 (+0.00) | 1.13 (+0.00) | 0.00 (+0.00) | 0.14 (+0.00) |
| GPT-5.6 Luna (max) | 0.00 (+0.00) | 2.16 (+0.00) | 2.62 (+0.00) | 2.66 (+0.00) | 2.18 (+0.00) |
| GPT-5.6 Sol (max) | 0.00 (+0.00) | 2.16 (+0.00) | 2.48 (+0.00) | 2.65 (+0.00) | 2.18 (+0.00) |
| GPT-6 Luna (max) | 0.00 (+0.00) | 0.00 (+0.00) | 1.41 (+0.00) | 0.00 (+0.00) | 0.12 (+0.00) |
| GPT-6 Sol (max) | 0.00 (+0.00) | 2.16 (+0.00) | 2.49 (+0.00) | 2.65 (+0.00) | 2.20 (+0.00) |
| GPT-6.1 Sol (max) | 0.00 (+0.00) | 0.00 (+0.00) | 0.78 (+0.00) | 0.00 (+0.00) | 0.13 (+0.00) |
| Gemini 3.8 Flash (high) | 0.00 (+0.00) | 0.00 (+0.00) | 1.51 (+0.00) | 0.00 (+0.00) | 0.15 (+0.00) |
| Gemini 4 Argon (high) | 0.00 (+0.00) | 2.16 (+0.00) | 2.58 (+0.00) | 2.66 (+0.00) | 2.16 (+0.00) |
| Grok 4.7 (xhigh) | 0.00 (+0.00) | 0.00 (+0.00) | 1.35 (+0.00) | 0.00 (+0.00) | 0.15 (+0.00) |
| Qwen3.8 Max | 0.00 (+0.00) | 0.00 (+0.00) | 0.96 (+0.00) | 0.00 (+0.00) | 0.17 (+0.00) |

Plan streams S1, S2, S1 endpoint-heavy and S1M run with owner-named transfers off (E167): Claude Haiku 5.5 (xhigh), Claude Opus 5 (max), Claude Sonnet 5.5 (max), GPT-5.6 Luna (max), GPT-5.6 Sol (max), GPT-6 Luna (max), GPT-6 Sol (max) depend on a transfer and are unevaluable there (—), never reselected or replaced by API cost.

### Plan basis: rank 1

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M |
|---|---:|---:|---:|---:|---:|
| Claude Haiku 5.5 (xhigh) | 0.0% | — | — | — | — |
| Claude Opus 5 (max) | 0.0% | — | — | — | — |
| Claude Opus 5.5 (max) | 0.0% | 100.0% | 100.0% | 100.0% | 100.0% |
| Claude Sonnet 5.5 (max) | 100.0% | — | — | — | — |
| DeepSeek V4 Flash (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| DeepSeek V4 Pro (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GLM-5.3 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-5.6 Luna (max) | 0.0% | — | — | — | — |
| GPT-5.6 Sol (max) | 0.0% | — | — | — | — |
| GPT-6 Luna (max) | 0.0% | — | — | — | — |
| GPT-6 Sol (max) | 0.0% | — | — | — | — |
| GPT-6.1 Sol (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Gemini 3.8 Flash (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Gemini 4 Argon (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Grok 4.7 (xhigh) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Qwen3.8 Max | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |

### Plan basis: rank 3 or better

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M |
|---|---:|---:|---:|---:|---:|
| Claude Haiku 5.5 (xhigh) | 0.0% | — | — | — | — |
| Claude Opus 5 (max) | 0.0% | — | — | — | — |
| Claude Opus 5.5 (max) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% |
| Claude Sonnet 5.5 (max) | 100.0% | — | — | — | — |
| DeepSeek V4 Flash (max) | 0.0% | 14.3% | 14.2% | 18.8% | 13.9% |
| DeepSeek V4 Pro (max) | 0.0% | 5.0% | 5.4% | 7.8% | 4.8% |
| GLM-5.3 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-5.6 Luna (max) | 0.0% | — | — | — | — |
| GPT-5.6 Sol (max) | 0.0% | — | — | — | — |
| GPT-6 Luna (max) | 0.0% | — | — | — | — |
| GPT-6 Sol (max) | 0.0% | — | — | — | — |
| GPT-6.1 Sol (max) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% |
| Gemini 3.8 Flash (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Gemini 4 Argon (high) | 0.0% | 80.7% | 80.4% | 73.4% | 81.3% |
| Grok 4.7 (xhigh) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Qwen3.8 Max | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |

### Plan basis: on the frontier

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M |
|---|---:|---:|---:|---:|---:|
| Claude Haiku 5.5 (xhigh) | 100.0% | — | — | — | — |
| Claude Opus 5 (max) | 0.0% | — | — | — | — |
| Claude Opus 5.5 (max) | 0.0% | 100.0% | 100.0% | 100.0% | 100.0% |
| Claude Sonnet 5.5 (max) | 100.0% | — | — | — | — |
| DeepSeek V4 Flash (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| DeepSeek V4 Pro (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GLM-5.3 (max) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-5.6 Luna (max) | 100.0% | — | — | — | — |
| GPT-5.6 Sol (max) | 0.0% | — | — | — | — |
| GPT-6 Luna (max) | 100.0% | — | — | — | — |
| GPT-6 Sol (max) | 0.0% | — | — | — | — |
| GPT-6.1 Sol (max) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% |
| Gemini 3.8 Flash (high) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Gemini 4 Argon (high) | 100.0% | 45.2% | 47.4% | 46.8% | 45.4% |
| Grok 4.7 (xhigh) | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Qwen3.8 Max | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |

### Plan basis: value-score dispersion (SD; covariance term)

| Configuration | S0 | S1 | S2 | S1 endpoint-heavy | S1M |
|---|---:|---:|---:|---:|---:|
| Claude Haiku 5.5 (xhigh) | 0.00 (+0.00) | — | — | — | — |
| Claude Opus 5 (max) | 0.00 (+0.00) | — | — | — | — |
| Claude Opus 5.5 (max) | 0.00 (+0.00) | 0.00 (+0.00) | 0.81 (+0.00) | 0.00 (+0.00) | 0.13 (+0.00) |
| Claude Sonnet 5.5 (max) | 0.00 (+0.00) | — | — | — | — |
| DeepSeek V4 Flash (max) | 0.00 (+0.00) | 3.07 (+0.00) | 3.33 (+0.00) | 3.77 (+0.00) | 3.09 (+0.00) |
| DeepSeek V4 Pro (max) | 0.00 (+0.00) | 3.07 (+0.00) | 3.35 (+0.00) | 3.70 (+0.00) | 3.06 (+0.00) |
| GLM-5.3 (max) | 0.00 (+0.00) | 0.00 (+0.00) | 1.14 (+0.00) | 0.00 (+0.00) | 0.14 (+0.00) |
| GPT-5.6 Luna (max) | 0.00 (+0.00) | — | — | — | — |
| GPT-5.6 Sol (max) | 0.00 (+0.00) | — | — | — | — |
| GPT-6 Luna (max) | 0.00 (+0.00) | — | — | — | — |
| GPT-6 Sol (max) | 0.00 (+0.00) | — | — | — | — |
| GPT-6.1 Sol (max) | 0.00 (+0.00) | 0.00 (+0.00) | 0.78 (+0.00) | 0.00 (+0.00) | 0.13 (+0.00) |
| Gemini 3.8 Flash (high) | 0.00 (+0.00) | 0.00 (+0.00) | 1.51 (+0.00) | 0.00 (+0.00) | 0.15 (+0.00) |
| Gemini 4 Argon (high) | 0.00 (+0.00) | 2.15 (+0.00) | 2.57 (+0.00) | 2.65 (+0.00) | 2.18 (+0.00) |
| Grok 4.7 (xhigh) | 0.00 (+0.00) | 0.00 (+0.00) | 1.35 (+0.00) | 0.00 (+0.00) | 0.15 (+0.00) |
| Qwen3.8 Max | 0.00 (+0.00) | 0.00 (+0.00) | 0.98 (+0.00) | 0.00 (+0.00) | 0.16 (+0.00) |

### Named S2 specification branches

- **Bug Hunt harness band (E19)** (S2): unevaluable; the captured tbench.ai leaderboard lists no configuration under two or more agents, so no cross-agent spread exists
- **cache-hit variation (E34)** (S2): unevaluable; AA's published cost embeds its cache-pricing protocol; varying the cache-hit rate needs each basket component's cache-read and uncached-input demand, which AA publishes only for the whole Index (E157)
- **first-party list versus cross-provider median price rule (E122)** (S2): unevaluable; AA publishes one price per configuration under its own rule; the alternative rule's prices are not captured

### Cheapest-above-the-bar labels (API basis)

Each kernel assignment code gives the kernel used for the candidate, the reference and the competitors, in that order (U uniform, H endpoint-heavy); the label needs every assignment met.

| Bar | Candidate | Reading | Frequency range | Kernel assignments | Label |
|---|---|---|---|---|---|
| GPT-6 Luna (max) | GPT-6 Luna (max) | supported under all registered role-group kernel checks | 100.0% to 100.0% | UUU met, UUH met, HHU met, HHH met | yes |

## Diagnostics

- **Terminal-Bench same-harness (Terminus 2):** undefined (panel too small); 11 rows ran on mixed harnesses.
- **Quality agreement:** quality agreement (matched-panel sensitivity): Kendall tau 0.85 (interval 0.48 to 1.00) on 11 rows.
- **Quality-substitution value agreement (API):** quality-substitution value agreement, api basis (matched-panel sensitivity): Kendall tau 0.38 (interval -0.14 to 0.76) on 11 rows.
- **Quality-substitution value agreement (Plan):** quality-substitution value agreement, plan basis (matched-panel sensitivity): Kendall tau 0.82 (interval 0.53 to 1.00) on 11 rows.
- **Disjoint-evidence agreement:** disjoint-evidence agreement (restricted evidence comparison, not an eligible ranking): Kendall tau 0.75 (interval 0.40 to 1.00) on 11 rows.
- **Quality source shares:** AA-run 80%, independent 20%.
- **Non-discriminating leaves:** lcr.
- **Group drift:** estimated; flagged: none.
- **Omniscience abstention sensitivity** (z_pen = max(0, I)): 15 rows move; largest move 5 (Claude Opus 5.5 (max)).
- **GDPval-AA logistic sensitivity** (z = 100 / (1 + 10^((1600 - E) / 400)) against AA's pinned anchor; every other input fixed): API 13 rows move; largest move 4 (Claude Opus 5.5 (max), Claude Sonnet 5.5 (max)); Plan 8 rows move; largest move 2 (Claude Opus 5 (max), GPT-6 Astra (xhigh)).
- **Anchor stability:** trimmed anchors (P10 / 2 and P90 x 2 (diagnostic only)) give $142.90 to $18,106.78; 9 rows move; largest move 2 (Gemini 4 Argon (high)).

- **Basket readiness (E22):** priced leaves cover 67% of nominal quality weight (AutomationBench-AA, DeepSWE v1.1, GDPval-AA v2.1, AA-LCR v1.1, SciCode, Terminal-Bench 4.0 (tbench.ai)); pending components: FrontierCode, ITBench-AA.
- **SWE cost companion (O14, diagnostic):** 16 rows evaluated; flagged far from the median ratio: none.
- **Matched-cost diagnostic (E55):** evaluated at 50% priced quality weight; basket/matched cost-order reversals with separated intervals: 4; rank-gap warnings: 0.

### Leave-one-component-out cost family (E172)

Each admitted basket unit removed in turn, scored on anchors rebuilt by the freeze rule (rank changes against the primary ranking; quality held fixed).

| Removed component | API rank changes | Plan rank changes | API value points per cost doubling |
|---|---|---|---:|
| Coding Agent Index | 9 rows move; largest move 3 (DeepSeek V4 Pro (max)) | 6 rows move; largest move 1 (Claude Opus 5 (max), DeepSeek V4 Pro (max), GPT-5.6 Luna (max), GPT-5.6 Sol (max), GPT-6 Sol (max), Grok 4.7 (xhigh)) | 2.89 |
| AA-Briefcase | 6 rows move; largest move 2 (Claude Sonnet 5.5 (max), GPT-5.6 Sol (max)) | no rank changes | 3.08 |
| GDPval-AA | 2 rows move; largest move 1 (Claude Sonnet 5.5 (max), GPT-5.6 Sol (max)) | 2 rows move; largest move 1 (GPT-6 Luna (max), GPT-6 Sol (max)) | 3.07 |
| GDP.pdf | 2 rows move; largest move 1 (DeepSeek V4 Pro (max), GPT-5.6 Sol (max)) | no rank changes | 3.03 |
| AutomationBench-AA | 2 rows move; largest move 1 (Claude Haiku 5.5 (xhigh), DeepSeek V4 Pro (max)) | 4 rows move; largest move 1 (Gemini 3.8 Flash (high), GLM-5.3 (max), GPT-6 Luna (max), GPT-6 Sol (max)) | 2.98 |
| Terminal-Bench 4.0 (AA Index run) | 2 rows move; largest move 1 (Claude Haiku 5.5 (xhigh), DeepSeek V4 Pro (max)) | no rank changes | 3.02 |
| SciCode | 2 rows move; largest move 1 (Claude Sonnet 5.5 (max), GPT-5.6 Sol (max)) | no rank changes | 3.04 |
| AA-LCR | no rank changes | no rank changes | 3.04 |

### Subset rows: paired bridge and missing spend (E10, E173)

- **GPT-6 Astra (xhigh), MiMo-V2.6-Flash, MiMo-V2.6-Pro** (subset without Coding Agent Index): Coding Agent Index is 40% of the full basket (median; 9% to 63% over 16 rows). Scored on its own subset anchors, the direction of its subset effect is not known. Paired bridge on the 16 full rows: API: the full rows' values change by -0.32 points (median; -2.59 to 1.20), 9 rows move; largest move 3 (DeepSeek V4 Pro (max)); Plan: the full rows' values change by -0.45 points (median; -1.61 to 0.42), 6 rows move; largest move 1 (Claude Opus 5 (max), DeepSeek V4 Pro (max), GPT-5.6 Luna (max), GPT-5.6 Sol (max), GPT-6 Sol (max), Grok 4.7 (xhigh)).

### Deletion sensitivity

| Branch | Retained nominal weight | Status | API rank changes | Plan rank changes |
|---|---:|---|---|---|
| leave-out:deepswe | 70% | evaluated | 17 rows move; largest move 5 (Claude Opus 5.5 (max), GPT-5.6 Luna (max)) | 12 rows move; largest move 4 (MiMo-V2.6-Flash) |
| leave-out:bugHunt | 90% | evaluated | 14 rows move; largest move 4 (MiMo-V2.6-Pro) | 12 rows move; largest move 5 (GPT-6 Astra (xhigh)) |
| leave-out:frontierCode | 90% | evaluated | 9 rows move; largest move 3 (Claude Sonnet 5.5 (max)) | 10 rows move; largest move 3 (GPT-6 Luna (max)) |
| leave-out:terminalBench | 90% | evaluated | 11 rows move; largest move 3 (GPT-5.6 Luna (max)) | 11 rows move; largest move 4 (Claude Opus 5 (max), GPT-5.6 Luna (max), GPT-5.6 Sol (max), GPT-6 Astra (xhigh), GPT-6 Luna (max)) |
| leave-out:gdpval | 90% | evaluated | 5 rows move; largest move 3 (GPT-6 Astra (xhigh)) | 9 rows move; largest move 2 (Claude Haiku 5.5 (xhigh), Claude Opus 5 (max), GPT-6 Sol (max)) |
| leave-out:automationBench | 90% | evaluated | 13 rows move; largest move 3 (Claude Opus 5 (max)) | 5 rows move; largest move 2 (GPT-6 Astra (xhigh)) |
| leave-out:omniscience | 90% | evaluated | 9 rows move; largest move 2 (Gemini 3.8 Flash (high), GLM-5.3 (max), GPT-5.6 Luna (max)) | 5 rows move; largest move 6 (GPT-6 Astra (xhigh)) |
| leave-out:lcr | 95% | evaluated | 9 rows move; largest move 3 (DeepSeek V4 Pro (max)) | 7 rows move; largest move 2 (GPT-6 Astra (xhigh)) |
| leave-out:hle | 98% | evaluated | no rank changes | no rank changes |
| leave-out:scicode | 98% | evaluated | 3 rows move; largest move 2 (DeepSeek V4 Pro (max)) | no rank changes |
| leave-out:critpt | 98% | evaluated | 2 rows move; largest move 1 (Claude Sonnet 5.5 (max), GPT-5.6 Sol (max)) | 2 rows move; largest move 1 (Claude Haiku 5.5 (xhigh), GPT-6 Astra (xhigh)) |
| leave-source-out:Artificial Analysis | 20% | not identifiable under the coverage rule | — | — |
| basket-scope | 87% | evaluated | 11 rows move; largest move 2 (Gemini 3.8 Flash (high), GLM-5.3 (max), GPT-5.6 Luna (max)) | 8 rows move; largest move 7 (MiMo-V2.6-Flash) |

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
| partial component flag (E37) | vacuous | AA declined- or missing-task markers |
| route dominance filter (E88) | vacuous | certifiably dearer routes set aside |
| Plan exploratory label (E61) | fired | fewer than half of Plan rows have an identified M_W |
| score swing gate (E177) | vacuous | first v3 release: no previous v3 release to compare |
| anchor migration (E184) | vacuous | no main-workload migration deferred |
| configuration map coverage | passed | every cohort row has a pinned identity |
| quality clipping audit (E110) | passed | saturation disclosed; domain violations block the build |
| scenario outputs current (E72) | passed | scenario input hash matches the scored inputs |
