# ValueRank v1.3.1 Scores

**Version:** v1.3.1
**Updated:** July 28, 2026

v1.3.1 ranks **n=17** DeepSWE Best models (excludes Kimi K2.7 Code — no AA Index total eval cost), retains **12 zero-gap dimensions**, drops IFBench / Terminal-Bench Hard / τ²-Bench (incomplete AA coverage on newest models), and restores **AA+DeepSWE composite Cost**.

## Final Ranking

| Rank | Model | Overall | Quality | Quality Rank | Missing Dims |
|---|---|---:|---:|---:|---:|
| 1 | Grok 4.5 | 60.6 | 44.9 | 11 | 0 |
| 2 | Kimi K3 | 59.2 | 66.4 | 4 | 0 |
| 3 | Muse Spark 1.1 | 58.9 | 39.5 | 14 | 0 |
| 4 | GPT-5.6 Terra | 58.8 | 60.0 | 6 | 0 |
| 5 | GPT-5.6 Sol | 58.2 | 73.8 | 2 | 0 |
| 6 | Claude Opus 5 | 56.5 | 74.3 | 1 | 0 |
| 7 | GPT-5.6 Luna | 53.9 | 41.1 | 13 | 0 |
| 8 | GPT-5.5 | 53.0 | 60.3 | 5 | 0 |
| 9 | Gemini 3.6 Flash | 52.6 | 36.2 | 15 | 0 |
| 10 | GLM-5.2 | 52.0 | 41.2 | 12 | 0 |
| 11 | Gemini 3.1 Pro | 51.0 | 45.6 | 8 | 0 |
| 12 | Claude Fable 5 | 50.0 | 73.6 | 3 | 0 |
| 13 | GPT-5.4 | 47.0 | 45.6 | 9 | 0 |
| 14 | Gemini 3.5 Flash | 42.8 | 30.5 | 16 | 0 |
| 15 | Claude Opus 4.8 | 40.8 | 54.2 | 7 | 0 |
| 16 | Claude Sonnet 5 | 32.9 | 45.5 | 10 | 0 |
| 17 | Claude Sonnet 4.6 | 21.7 | 17.2 | 17 | 0 |

## Pareto Frontier

Undominated on composite cost vs. quality:

- Claude Opus 5
- GPT-5.6 Sol
- GPT-5.6 Terra
- Kimi K3
- Grok 4.5
- Muse Spark 1.1
- Gemini 3.1 Pro

Dominated models: GPT-5.6 Luna, GPT-5.5, Gemini 3.6 Flash, GLM-5.2, Claude Fable 5, GPT-5.4, Gemini 3.5 Flash, Claude Opus 4.8, Claude Sonnet 5, Claude Sonnet 4.6.

## Normalized Dimension Matrix

Dimension order:

`[Cost, Hallucination, DeepSWE, GDPval-AA, AA-LCR, Omni Acc, HLE, GPQA, SciCode, CritPt, AA Intelligence Index, Speed]`

| Model | Normalized dimensions |
|---|---|
| Grok 4.5 | `[93.8, 50.0, 46.9, 50.0, 9.4, 68.8, 31.2, 68.8, 50.0, 25.0, 56.2, 25.0]` |
| Kimi K3 | `[43.8, 56.2, 75.0, 81.2, 100.0, 37.5, 62.5, 84.4, 87.5, 65.6, 81.2, 0.0]` |
| Muse Spark 1.1 | `[100.0, 81.2, 37.5, 12.5, 0.0, 18.8, 75.0, 12.5, 81.2, 18.8, 25.0, 62.5]` |
| GPT-5.6 Terra | `[56.2, 25.0, 84.4, 62.5, 81.2, 31.2, 50.0, 50.0, 43.8, 93.8, 68.8, 68.8]` |
| GPT-5.6 Sol | `[25.0, 6.2, 93.8, 87.5, 68.8, 93.8, 87.5, 96.9, 65.6, 100.0, 87.5, 43.8]` |
| Claude Opus 5 | `[18.8, 62.5, 100.0, 100.0, 34.4, 75.0, 93.8, 75.0, 56.2, 87.5, 100.0, 12.5]` |
| GPT-5.6 Luna | `[81.2, 0.0, 65.6, 56.2, 81.2, 25.0, 6.2, 21.9, 12.5, 43.8, 37.5, 87.5]` |
| GPT-5.5 | `[37.5, 18.8, 65.6, 37.5, 93.8, 87.5, 56.2, 84.4, 65.6, 75.0, 62.5, 50.0]` |
| Gemini 3.6 Flash | `[87.5, 43.8, 25.0, 31.2, 25.0, 56.2, 12.5, 62.5, 18.8, 6.2, 12.5, 100.0]` |
| GLM-5.2 | `[75.0, 100.0, 18.8, 43.8, 56.2, 0.0, 25.0, 6.2, 6.2, 53.1, 31.2, 93.8]` |
| Gemini 3.1 Pro | `[62.5, 68.8, 0.0, 0.0, 62.5, 81.2, 68.8, 96.9, 93.8, 37.5, 0.0, 56.2]` |
| Claude Fable 5 | `[0.0, 37.5, 84.4, 93.8, 34.4, 100.0, 100.0, 56.2, 100.0, 81.2, 93.8, 31.2]` |
| GPT-5.4 | `[50.0, 12.5, 31.2, 25.0, 81.2, 50.0, 43.8, 34.4, 75.0, 65.6, 43.8, 75.0]` |
| Gemini 3.5 Flash | `[68.8, 31.2, 12.5, 6.2, 18.8, 62.5, 37.5, 43.8, 25.0, 12.5, 18.8, 81.2]` |
| Claude Opus 4.8 | `[12.5, 93.8, 56.2, 68.8, 9.4, 43.8, 81.2, 34.4, 31.2, 53.1, 75.0, 18.8]` |
| Claude Sonnet 5 | `[6.2, 87.5, 46.9, 75.0, 46.9, 6.2, 18.8, 21.9, 37.5, 31.2, 50.0, 37.5]` |
| Claude Sonnet 4.6 | `[31.2, 75.0, 6.2, 18.8, 46.9, 12.5, 0.0, 0.0, 0.0, 0.0, 6.2, 6.2]` |
