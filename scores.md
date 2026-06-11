# ValueRank v0.9 Scores

**Version:** v0.9  
**Updated:** June 12, 2026

## Final Ranking

v0.9 adds AA-Omniscience Hallucination Rate as a 6% primary reliability factor, funded by reducing IFBench from 18% to 12%. It also replaces direct AA eval cost with a composite cost built from normalized AA eval cost plus normalized DeepSWE average cost per task.

| Rank | Model | Overall | Quality | Quality Rank | Missing Dims |
|---|---|---:|---:|---:|---:|
| 1 | Gemini 3.1 Pro | 69.4 | 61.8 | 3 | 6 |
| 2 | MiMo-V2.5-Pro | 61.1 | 48.1 | 8 | 11 |
| 3 | MiniMax M3 | 58.5 | 54.9 | 4 | 9 |
| 4 | Kimi K2.6 | 52.8 | 44.7 | 9 | 8 |
| 5 | GPT-5.5 | 52.1 | 64.3 | 2 | 7 |
| 6 | Claude Opus 4.8 | 51.2 | 65.7 | 1 | 8 |
| 7 | DeepSeek V4-Pro | 49.5 | 37.8 | 14 | 10 |
| 8 | Gemini 3.5 Flash | 48.5 | 54.4 | 5 | 9 |
| 9 | GPT-5.4 Mini | 45.4 | 40.0 | 13 | 9 |
| 10 | GLM 5.1 | 43.8 | 40.5 | 12 | 9 |
| 11 | Claude Sonnet 4.6 | 43.8 | 43.0 | 10 | 9 |
| 12 | GPT-5.4 | 41.9 | 48.2 | 7 | 10 |
| 13 | Claude Opus 4.6 | 41.3 | 42.3 | 11 | 12 |
| 14 | Claude Opus 4.7 | 40.7 | 54.3 | 6 | 12 |

## Pareto Frontier

Undominated on composite cost vs. quality:

- MiMo-V2.5-Pro
- Gemini 3.1 Pro
- GPT-5.5
- Claude Opus 4.8

## Normalized Dimension Matrix

Dimension order:

`[Cost, IF, Halluc, Term, SWE, SWEPro, LCB, DeepSWE, AAI, Spd, Tau2, OSW, BC, LCR, HLE, GPQA, MMLU, AIME, Sci, Omni]`

Missing cells still receive neutral `50.0`. `Halluc` is AA-Omniscience Hallucination Rate, normalized with lower raw rate ranked better. `Omni` is the AA-Omniscience Index.

| Model | Normalized dimensions |
|---|---|
| Gemini 3.1 Pro | `[92.3, 100.0, 46.2, 50.0, 70.0, 0.0, 50.0, 7.7, 76.9, 84.6, 50.0, 50.0, 50.0, 66.7, 90.0, 100.0, 50.0, 50.0, 100.0, 100.0]` |
| MiMo-V2.5-Pro | `[100.0, 50.0, 92.3, 50.0, 50.0, 50.0, 50.0, 23.1, 42.3, 7.7, 50.0, 50.0, 50.0, 77.8, 30.0, 50.0, 50.0, 50.0, 45.5, 30.8]` |
| MiniMax M3 | `[69.2, 50.0, 100.0, 50.0, 50.0, 50.0, 50.0, 30.8, 57.7, 19.2, 50.0, 100.0, 50.0, 88.9, 60.0, 77.8, 50.0, 50.0, 9.1, 15.4]` |
| Kimi K2.6 | `[76.9, 50.0, 61.5, 50.0, 10.0, 50.0, 50.0, 42.3, 42.3, 53.8, 50.0, 0.0, 50.0, 44.4, 50.0, 44.4, 50.0, 50.0, 68.2, 46.2]` |
| GPT-5.5 | `[15.4, 50.0, 23.1, 100.0, 90.0, 50.0, 50.0, 100.0, 92.3, 46.2, 50.0, 50.0, 50.0, 100.0, 80.0, 88.9, 50.0, 50.0, 81.8, 69.2]` |
| Claude Opus 4.8 | `[7.7, 50.0, 76.9, 75.0, 100.0, 50.0, 50.0, 92.3, 100.0, 61.5, 50.0, 50.0, 50.0, 11.1, 100.0, 55.6, 50.0, 50.0, 68.2, 92.3]` |
| DeepSeek V4-Pro | `[84.6, 50.0, 0.0, 50.0, 50.0, 50.0, 50.0, 0.0, 30.8, 38.5, 50.0, 50.0, 50.0, 0.0, 40.0, 33.3, 50.0, 50.0, 36.4, 7.7]` |
| Gemini 3.5 Flash | `[30.8, 50.0, 38.5, 50.0, 60.0, 50.0, 50.0, 57.7, 57.7, 92.3, 50.0, 50.0, 50.0, 27.8, 70.0, 66.7, 50.0, 50.0, 54.5, 76.9]` |
| GPT-5.4 Mini | `[61.5, 50.0, 7.7, 50.0, 0.0, 50.0, 50.0, 42.3, 15.4, 100.0, 50.0, 50.0, 50.0, 27.8, 0.0, 16.7, 50.0, 50.0, 27.3, 0.0]` |
| GLM 5.1 | `[53.8, 50.0, 84.6, 0.0, 20.0, 50.0, 50.0, 15.4, 23.1, 69.2, 50.0, 50.0, 50.0, 50.0, 10.0, 0.0, 50.0, 50.0, 0.0, 23.1]` |
| Claude Sonnet 4.6 | `[46.2, 50.0, 53.8, 50.0, 30.0, 50.0, 50.0, 69.2, 0.0, 19.2, 50.0, 50.0, 50.0, 55.6, 20.0, 16.7, 50.0, 50.0, 18.2, 53.8]` |
| GPT-5.4 | `[23.1, 0.0, 15.4, 50.0, 50.0, 100.0, 50.0, 84.6, 76.9, 76.9, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 90.9, 38.5]` |
| Claude Opus 4.6 | `[38.5, 50.0, 30.8, 50.0, 40.0, 50.0, 50.0, 57.7, 7.7, 0.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 61.5]` |
| Claude Opus 4.7 | `[0.0, 50.0, 69.2, 25.0, 80.0, 50.0, 50.0, 76.9, 76.9, 30.8, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 84.6]` |
