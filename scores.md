# ValueRank v1.3 Scores

**Version:** v1.3
**Updated:** July 28, 2026

v1.3 expands the ranked cohort to the full DeepSWE Best roster (**n=18**), retains **12 zero-gap dimensions**, drops IFBench / Terminal-Bench Hard / τ²-Bench (incomplete AA coverage on newest models), and uses DeepSWE-only Cost.

## Final Ranking

| Rank | Model | Overall | Quality | Quality Rank | Missing Dims |
|---|---|---:|---:|---:|---:|
| 1 | Kimi K3 | 66.9 | 67.9 | 4 | 0 |
| 2 | Grok 4.5 | 62.8 | 48.1 | 9 | 0 |
| 3 | Muse Spark 1.1 | 61.0 | 42.6 | 14 | 0 |
| 4 | GPT-5.6 Terra | 60.7 | 61.7 | 6 | 0 |
| 5 | GPT-5.6 Sol | 60.2 | 74.7 | 3 | 0 |
| 6 | Claude Opus 5 | 57.1 | 75.8 | 1 | 0 |
| 7 | GPT-5.6 Luna | 56.2 | 43.9 | 12 | 0 |
| 8 | GPT-5.5 | 55.3 | 62.0 | 5 | 0 |
| 9 | Claude Fable 5 | 53.0 | 75.2 | 2 | 0 |
| 10 | GLM-5.2 | 52.4 | 43.8 | 13 | 0 |
| 11 | Gemini 3.6 Flash | 51.7 | 39.9 | 15 | 0 |
| 12 | GPT-5.4 | 47.8 | 48.1 | 10 | 0 |
| 13 | Claude Opus 4.8 | 42.4 | 56.9 | 7 | 0 |
| 14 | Gemini 3.1 Pro | 39.7 | 47.4 | 11 | 0 |
| 15 | Kimi K2.7 Code | 34.8 | 9.6 | 18 | 0 |
| 16 | Gemini 3.5 Flash | 34.8 | 34.6 | 16 | 0 |
| 17 | Claude Sonnet 5 | 32.8 | 48.2 | 8 | 0 |
| 18 | Claude Sonnet 4.6 | 30.3 | 19.7 | 17 | 0 |

## Pareto Frontier

Undominated on composite cost vs. quality:

- Claude Opus 5
- GPT-5.6 Sol
- Kimi K3
- Grok 4.5
- Muse Spark 1.1

Dominated models: GPT-5.6 Terra, GPT-5.6 Luna, GPT-5.5, Claude Fable 5, GLM-5.2, Gemini 3.6 Flash, GPT-5.4, Claude Opus 4.8, Gemini 3.1 Pro, Kimi K2.7 Code, Gemini 3.5 Flash, Claude Sonnet 5, Claude Sonnet 4.6.

## Normalized Dimension Matrix

Dimension order:

`[Cost, Hallucination, DeepSWE, GDPval-AA, AA-LCR, Omni Acc, HLE, GPQA, SciCode, CritPt, AA Intelligence Index, Speed]`

| Model | Normalized dimensions |
|---|---|
| Kimi K3 | `[64.7, 58.8, 76.5, 82.4, 100.0, 41.2, 64.7, 85.3, 88.2, 67.6, 82.4, 0.0]` |
| Grok 4.5 | `[94.1, 52.9, 50.0, 52.9, 14.7, 70.6, 35.3, 70.6, 52.9, 29.4, 58.8, 29.4]` |
| Muse Spark 1.1 | `[100.0, 82.4, 41.2, 17.6, 0.0, 23.5, 76.5, 17.6, 82.4, 23.5, 29.4, 64.7]` |
| GPT-5.6 Terra | `[58.8, 23.5, 85.3, 64.7, 82.4, 35.3, 52.9, 52.9, 47.1, 94.1, 70.6, 70.6]` |
| GPT-5.6 Sol | `[29.4, 5.9, 94.1, 88.2, 70.6, 94.1, 88.2, 97.1, 67.6, 100.0, 88.2, 47.1]` |
| Claude Opus 5 | `[17.6, 64.7, 100.0, 100.0, 38.2, 76.5, 94.1, 76.5, 58.8, 88.2, 100.0, 17.6]` |
| GPT-5.6 Luna | `[82.4, 0.0, 67.6, 58.8, 82.4, 29.4, 11.8, 26.5, 17.6, 47.1, 41.2, 88.2]` |
| GPT-5.5 | `[41.2, 17.6, 67.6, 41.2, 94.1, 88.2, 58.8, 85.3, 67.6, 76.5, 64.7, 52.9]` |
| Claude Fable 5 | `[5.9, 41.2, 85.3, 94.1, 38.2, 100.0, 100.0, 58.8, 100.0, 82.4, 94.1, 35.3]` |
| GLM-5.2 | `[70.6, 100.0, 23.5, 47.1, 58.8, 0.0, 29.4, 5.9, 11.8, 55.9, 35.3, 94.1]` |
| Gemini 3.6 Flash | `[76.5, 47.1, 29.4, 35.3, 29.4, 58.8, 17.6, 64.7, 23.5, 11.8, 17.6, 100.0]` |
| GPT-5.4 | `[47.1, 11.8, 35.3, 29.4, 82.4, 52.9, 47.1, 38.2, 76.5, 67.6, 47.1, 76.5]` |
| Claude Opus 4.8 | `[11.8, 94.1, 58.8, 70.6, 14.7, 47.1, 82.4, 38.2, 35.3, 55.9, 76.5, 23.5]` |
| Gemini 3.1 Pro | `[23.5, 70.6, 0.0, 0.0, 64.7, 82.4, 70.6, 97.1, 94.1, 41.2, 5.9, 58.8]` |
| Kimi K2.7 Code | `[88.2, 29.4, 11.8, 5.9, 5.9, 11.8, 5.9, 11.8, 5.9, 5.9, 0.0, 5.9]` |
| Gemini 3.5 Flash | `[35.3, 35.3, 17.6, 11.8, 23.5, 64.7, 41.2, 47.1, 29.4, 17.6, 23.5, 82.4]` |
| Claude Sonnet 5 | `[0.0, 88.2, 50.0, 76.5, 50.0, 5.9, 23.5, 26.5, 41.2, 35.3, 52.9, 41.2]` |
| Claude Sonnet 4.6 | `[52.9, 76.5, 5.9, 23.5, 50.0, 17.6, 0.0, 0.0, 0.0, 0.0, 11.8, 11.8]` |
