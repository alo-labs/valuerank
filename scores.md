# ValueRank — Scores
**Updated every version | Primary calculation file**

← [README](README.md) · [Raw Data](raw-data.md) · [Methodology](methodology.md)

---

## 7. Normalized Rank Scores

### 7.1 Methodology Recap

For each dimension, models with real data are ranked 1–n (best to worst). Score = `((n − rank) / (n − 1)) × 100`. Missing data = **50⊘**. All columns fully renormalized for the 20-model v5.0 field. Ties receive the average of their tied ranks' scores.

**n values by dimension (v5.0):** Cost=20, IF=14, Term=13, SWE=10, SWEPro=9, LCB=10, GDP=12, Spd=19, τ²=12, OSW=6, BC=8, LCR=10, HLE=15, GPQA=18, MMLU=9, AIME=7, Sci=13, Omni=8

### 7.2 Complete Normalized Score Matrix (18 dimensions)

| Model | Cost | IF | Term | SWE | SWEPro | LCB | GDP | Spd | τ² | OSW | BC | LCR | HLE | GPQA | MMLU | AIME | Sci | Omni |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gemini 3.1 Pro | 36.8 | **100.0** | 58.3 | 61.1 | 50.0⊘ | 55.6 | 9.1 | **88.9** | **100.0** | 50.0⊘ | **71.4** | 88.9 | 92.9 | **100.0** | **87.5** | 41.7 | **100.0** | **100.0** |
| GPT-5.5 | 15.8 | 76.9 | **100.0** | **100.0** | 68.8 | 50.0⊘ | **100.0** | 61.1 | 90.9 | **100.0** | **100.0** | 50.0⊘ | 85.7 | 88.2 | 50.0⊘ | 50.0⊘ | 50.0⊘ | 0.0 |
| Mistral Large 3 | **84.2** | 50.0⊘ | 50.0⊘ | 50.0⊘ | 50.0⊘ | **88.9~** | 50.0⊘ | 44.4 | 50.0⊘ | 50.0⊘ | 50.0⊘ | 50.0⊘ | 50.0⊘ | 5.9 | 50.0⊘ | 50.0⊘ | 50.0⊘ | 50.0⊘ |
| Gemma 3 27B | **100.0** | 50.0⊘ | 50.0⊘ | 50.0⊘ | 50.0⊘ | 50.0⊘ | 50.0⊘ | 5.6 | 50.0⊘ | 50.0⊘ | 50.0⊘ | 50.0⊘ | 50.0⊘ | 0.0 | 50.0⊘ | 50.0⊘ | 50.0⊘ | 50.0⊘ |
| Phi-4 | **94.7** | 50.0⊘ | 50.0⊘ | 50.0⊘ | 50.0⊘ | 50.0⊘ | 50.0⊘ | 11.1 | 50.0⊘ | 50.0⊘ | 50.0⊘ | 50.0⊘ | 50.0⊘ | 50.0⊘ | 50.0⊘ | 50.0⊘ | 50.0⊘ | 50.0⊘ |
| Kimi K2.6 | 31.6 | 84.6 | 41.7 | 44.4 | **68.8** | **77.8** | 36.4 | 72.2 | 72.7 | 40.0 | 28.6 | 61.1 | 57.1 | 76.5 | 37.5 | 66.7 | 75.0 | 42.9 |
| KAT-Coder-Pro-V2 | **73.7** | 38.5 | **91.7†** | 27.8 | 50.0⊘ | 50.0⊘ | 0.0 | **83.3** | 63.6 | 50.0⊘ | 50.0⊘ | 33.3 | 21.4 | 41.2 | 50.0⊘ | 50.0⊘ | 25.0 | 50.0⊘ |
| Amazon Nova Pro | **63.2** | 50.0⊘ | 50.0⊘ | 50.0⊘ | 50.0⊘ | 50.0⊘ | 50.0⊘ | 50.0⊘ | 50.0⊘ | 50.0⊘ | 50.0⊘ | 50.0⊘ | 50.0⊘ | 50.0⊘ | 50.0⊘ | 50.0⊘ | 50.0⊘ | 50.0⊘ |
| Grok 3 | 57.9 | 50.0⊘ | 50.0⊘ | 50.0⊘ | 50.0⊘ | **66.7~** | 50.0⊘ | 55.6 | 50.0⊘ | 50.0⊘ | 50.0⊘ | 50.0⊘ | 50.0⊘ | **35.3~** | 50.0⊘ | 50.0⊘ | 50.0⊘ | 50.0⊘ |
| GPT-5.4 | 21.1 | 53.8 | 83.3 | 50.0⊘ | **87.5** | 22.2 | 72.7 | 66.7 | 54.5 | 60.0 | **85.7** | **100.0** | 78.6 | 82.4 | 50.0⊘ | 50.0⊘ | **91.7** | 50.0⊘ |
| MiniMax M2.7 | **68.4** | 69.2 | 8.3 | 50.0⊘ | 25.0~ | 50.0⊘ | 27.3 | 36.1 | 40.9 | 50.0⊘ | 50.0⊘ | 44.4 | 28.6 | 52.9 | 50.0⊘ | 50.0⊘ | 58.3 | **71.4** |
| GLM 5.1 | 42.1 | **92.3** | 66.7 | 0.0 | 50.0~ | 50.0⊘ | 45.5 | 36.1 | **81.8** | 50.0⊘ | 0.0~ | 22.2 | 50.0 | 47.1 | 50.0~ | 41.7 | 41.7 | 28.6 |
| Llama 4 Maverick | **78.9** | 15.4 | 50.0⊘ | 50.0⊘ | 50.0⊘ | 11.1~ | 50.0⊘ | **77.8** | 50.0⊘ | 50.0⊘ | 50.0⊘ | 50.0⊘ | 7.1 | 17.6 | 25.0 | 50.0⊘ | 16.7 | 50.0⊘ |
| Llama 4 Scout | **89.5** | 0.0 | 50.0⊘ | 50.0⊘ | 50.0⊘ | 0.0~ | 50.0⊘ | **100.0** | 50.0⊘ | 50.0⊘ | 50.0⊘ | 50.0⊘ | 0.0 | 11.8 | 0.0 | 50.0⊘ | 0.0 | 50.0⊘ |
| Claude Opus 4.7 | 5.3 | 30.8 | 75.0 | **88.9** | **100.0** | 50.0⊘ | **90.9** | 22.2 | 9.1 | **80.0** | 14.3 | 77.8 | **100.0** | **94.1** | **100.0~** | **91.7** | **83.3** | **85.7** |
| DeepSeek V4-Pro | 26.3 | 50.0⊘ | 50.0†self | 61.1 | 12.5 | **100.0** | 54.5 | 16.7 | 50.0⊘ | 50.0⊘ | 42.9 | 50.0⊘ | 64.3 | 64.7 | 62.5 | 50.0⊘ | 50.0⊘ | 14.3 |
| Qwen 3.6 Plus | 47.4 | 61.5 | 25.0 | 11.1 | 37.5~ | 50.0⊘ | 18.2 | 50.0 | 18.2 | 50.0⊘ | 50.0⊘ | 61.1 | 35.7 | 70.6 | **75.0** | 50.0⊘ | 8.3 | 50.0⊘ |
| o3-mini (high) | 52.6 | 46.2 | 0.0 | 50.0⊘ | 50.0⊘ | 33.3~ | 50.0⊘ | **94.4** | 0.0~ | 50.0⊘ | 50.0⊘ | 50.0⊘ | 14.3 | 23.5 | 12.5 | 16.7 | 33.3 | 50.0⊘ |
| Claude Sonnet 4.6 | 10.5 | 23.1 | 16.7 | 27.8 | 50.0⊘ | 50.0⊘ | **81.8** | 27.8 | 27.3 | 0.0 | 50.0⊘ | 11.1 | 42.9 | 58.8 | 50.0⊘ | 0.0 | 50.0 | 50.0⊘ |
| Claude Opus 4.6 | 0.0 | 7.7 | 33.3 | **77.8** | 0.0 | 44.4 | 63.6 | 0.0 | 40.9 | 20.0 | 57.1~ | 0.0 | 71.4 | 29.4 | 50.0⊘ | **91.7** | 66.7 | 57.1 |

**⊘** = missing data, neutral score 50.0. **~** = secondary source (probable confidence). **†/†self** = self-reported, not on canonical leaderboard.

**Key v5.0 dimension normalization notes (n expansions):**
- **Cost (n=12→20):** 5 ultra-cheap models enter (Gemma3 $0.00, Phi-4 $4.27, Scout $26.42, ML3 $38.67, Maverick $62.28) plus NovaPro $200.98, Grok3 $311.71, o3mini $314.72. Formula shifts to ((20−rank)/19)×100. KAT drops from rank 1 (100.0) to rank 6 (73.7). Gemini drops from rank 5 (63.6) to rank 13 (36.8). All existing models compressed by 4–32 pts on Cost.
- **IF (n=11→14):** Scout (39.5%), Maverick (43.0%), o3mini (67.1%) added. o3mini rank 8/14 (46.2); KAT rank 9 (38.5). GLM still rank 2 (92.3); Kimi rank 3 (84.6). Existing top-5 unchanged in relative order.
- **Term (n=12→13):** o3mini (6.1%) enters as dead last. All existing ranks shift: Gemini 54.5→58.3; KAT 90.9→91.7; DeepSeek 45.5→50.0.
- **LCB (n=5→10):** 5 new provisional ~ entries: ML3 82.8%~, Grok3 79.4%~, o3mini 71.7%~, Maverick 43.4%~, Scout 32.8%~. Dramatic lifts for existing low-ranked models: GPT-5.4 0.0→22.2 (+22.2), Opus4.6 25.0→44.4 (+19.4), Gemini 50.0→55.6 (+5.6), Kimi 75.0→77.8 (+2.8).
- **HLE (n=12→15):** Scout (4.3%), Maverick (4.8%), o3mini (12.3%) added. All at bottom of cohort. Opus4.7 holds rank 1 (100.0); Gemini rank 2 (92.9); GPT-5.5 rank 3 (85.7).
- **GPQA (n=12→18):** 6 new real scores: Grok3 84.6%~, o3mini 77.3%, Maverick 67.1%, Scout 58.7%, ML3 43.9%, Gemma3 42.4%. All insert below existing models. Top-4 compressed slightly: Gemini still 100.0, Opus47 94.1, GPT55 88.2.
- **MMLU (n=6→9):** Maverick (80.5%), o3mini (79.1%), Scout (74.3%) added. Pool grows to 9 real scorers. Gemini drops from 100.0 to 87.5 (rank 1→2; Opus47 89.87%~ still #1).
- **AIME (n=6→7):** o3mini (77.0%) adds as rank 6. Opus47/Opus46 improve from 90.0 to 91.7 (rank 1.5 in n=7); Kimi improves from 60.0 to 66.7; Gemini/GLM 30.0→41.7.
- **SciCode (n=9→13):** o3mini (39.8%), Maverick (33.1%), Scout (17.0%), Qwen (21.4%) all add. Gemini remains #1 (100.0). o3mini rank 9 (33.3); KAT shifts from 0.0 to 25.0 (rank 10/13).
- **τ² (n=11→12):** o3mini (28.7%~) enters at rank 12 (last, score 0.0). Opus4.7 shifts from rank 11 (0.0) to rank 11 (9.1); Sonnet 20.0→27.3; Qwen 10.0→18.2.
- **Spd (n=12→19):** 7 new models. Scout (142.5) #1, o3mini (131.7) #2, Kimi slides from rank 2 to rank 6 (100.0→72.2). Gemini rank 3 (88.9→88.9 stable). MiniMax/GLM tied rank 12.5 (36.1).

### 7.3 Cost Score Derivation (v5.0)

Cost ranks (cheapest = rank 1, n=20 real scorers). Formula: ((20−rank)/19)×100.

| Model | AA Eval Cost | Rank | Score |
|---|---|---|---|
| Gemma 3 27B | $0.00 | 1 | **100.0** |
| Phi-4 | $4.27 | 2 | **94.7** |
| Llama 4 Scout | $26.42 | 3 | **89.5** |
| Mistral Large 3 | $38.67 | 4 | **84.2** |
| Llama 4 Maverick | $62.28 | 5 | **78.9** |
| KAT-Coder-Pro-V2 | $73.49 | 6 | **73.7** |
| MiniMax M2.7 | $175.51 | 7 | **68.4** |
| Amazon Nova Pro | $200.98 | 8 | **63.2** |
| Grok 3 | $311.71 | 9 | **57.9** |
| o3-mini (high) | $314.72 | 10 | **52.6** |
| Qwen 3.6 Plus | $482.65 | 11 | **47.4** |
| GLM 5.1 | $543.95 | 12 | **42.1** |
| Gemini 3.1 Pro | $892.28 | 13 | **36.8** |
| Kimi K2.6 | $947.87 | 14 | **31.6** |
| DeepSeek V4-Pro | $1,071.28 | 15 | **26.3** |
| GPT-5.4 | $2,851.01 | 16 | **21.1** |
| GPT-5.5 | $3,357.00 | 17 | **15.8** |
| Claude Sonnet 4.6 | $3,959.36 | 18 | **10.5** |
| Claude Opus 4.7 | $4,811.04 | 19 | **5.3** |
| Claude Opus 4.6 | $4,969.68 | 20 | **0.0** |

> **v4.0→v5.0 cost compression:** n expands 12→20. All existing model cost scores drop under the new formula. KAT-Coder-Pro-V2 falls from rank 1 (100.0) to rank 6 (73.7, −26.3 pts). MiniMax falls from rank 2 (90.9) to rank 7 (68.4, −22.5 pts). The 5 ultra-cheap entrants (Gemma3 through Maverick, $0–$62) dominate ranks 1–5. Nova Pro ($200.98) inserts at rank 8 above Grok3/o3mini.

---

## 8. Quality-Only Ranking (Unweighted)

Equally weighting all 17 non-cost dimensions (5.88% each) to show pure capability without cost penalty.

| Rank | Model | IF Score | Benchmark Quality‡ | Total Quality |
|---|---|---|---|---|
| 1 | **Gemini 3.1 Pro** | 100.0 | **72.2** | **73.8** |
| 2 | GPT-5.5 | 76.9 | 71.5 | 71.9 |
| 3 | Claude Opus 4.7 | 30.8 | 72.7 | 70.2 |
| 4 | GPT-5.4 | 53.8 | 67.8 | 67.0 |
| 5 | Kimi K2.6 | 84.6 | 56.2 | 57.9 |
| 6 | Grok 3 | 50.0⊘ | 50.5 | 50.4 |
| 7 | Amazon Nova Pro | 50.0⊘ | 50.0 | 50.0 |
| 8 | DeepSeek V4-Pro | 50.0⊘ | 49.6 | 49.6 |
| 9 | Mistral Large 3 | 50.0⊘ | 49.3 | 49.4 |
| 10 | Phi-4 | 50.0⊘ | 47.6 | 47.7 |
| 11 | KAT-Coder-Pro-V2 | 38.5 | 46.1 | 45.6 |
| 12 | MiniMax M2.7 | 69.2 | 43.3 | 44.8 |
| 13 | Gemma 3 27B | 50.0⊘ | 44.1 | 44.4 |
| 14 | GLM 5.1 | 92.3 | 41.3 | 44.3 |
| 15 | Qwen 3.6 Plus | 61.5 | 41.3 | 42.5 |
| 16 | Claude Opus 4.6 | 7.7 | 44.0 | 41.8 |
| 17 | Llama 4 Maverick | 15.4 | 41.0 | 39.5 |
| 18 | o3-mini (high) | 46.2 | 36.1 | 36.7 |
| 19 | Claude Sonnet 4.6 | 23.1 | 37.1 | 36.3 |
| 20 | Llama 4 Scout | 0.0 | 38.2 | 36.0 |

> **‡** IF Score = raw normalized IFBench score (0–100; ⊘=50.0). Benchmark Quality = equal-weighted avg of the other 16 non-cost dims. Total Quality = equal-weighted avg of all 17 non-cost dims.
>
> **v5.0 quality notes:** Gemini retains quality #1 (73.8, +1.1 from expanded pools). Opus4.7 holds quality #3 (70.2) with AIME improving 90.0→91.7 and τ² improving 0.0→9.1. Grok3 quality #6 (50.4) and NovaPro quality #7 (50.0) are dominated by neutral-50s — they rank above DeepSeek/ML3 purely on the marginal LCB and Speed fills. Models with 15+ ⊘ entries (NovaPro, Phi-4, Gemma3) cluster near quality rank 7–13 based entirely on cost and one or two confirmed benchmarks. **GLM quality #14 despite having IF #2 (92.3):** BrowseComp 0.0 (last of 8) erases 3 IF-equivalent points; the GLM pattern (narrow coding + long-context strength, weak web-browsing + MMLU) is amplified in equal-weight quality scoring.

---

## 9. Final Cost-Weighted Ranking

**Weights:** Cost 25%, IF 18%, Term 8%, SWE 7%, SWEPro 4%, LCB 6%, GDP 5%, Spd 5%, τ² 4%, OSW 4%, BC 3%, LCR 2%, HLE 2%, GPQA 2%, MMLU 2%, AIME 1%, Sci 1%, Omni 1%

### 9.1 Final Weighted Scores

| Rank | Model | Cost (25%) | IF (18%) | Quality (57%) | Main Score |
|---|---|---|---|---|---|
| 🥇 1 | **Gemini 3.1 Pro** | 9.20 | 18.00 | 37.14 | **64.3** |
| 🥈 2 | **GPT-5.5** | 3.95 | 13.84 | 45.92 | **63.7** |
| 🥉 3 | **Mistral Large 3** | 21.05 | 9.00 | 29.67 | **59.7** |
| 4 | **Gemma 3 27B** | 25.00 | 9.00 | 25.28 | **59.3** |
| 5 | **Phi-4** | 23.68 | 9.00 | 26.56 | **59.2** |
| 6 | Kimi K2.6 | 7.90 | 15.23 | 31.16 | **54.3** |
| 7 | KAT-Coder-Pro-V2 | 18.43 | 6.93 | 28.64 | **54.0** |
| 8 | **Amazon Nova Pro** | 15.79 | 9.00 | 28.50 | **53.3** |
| 9 | **Grok 3** | 14.47 | 9.00 | 29.49 | **53.0** |
| 10 | GPT-5.4 | 5.26 | 9.68 | 37.26 | **52.2** |
| 11 | MiniMax M2.7 | 17.11 | 12.46 | 21.79 | **51.4** |
| 12 | GLM 5.1 | 10.53 | 16.61 | 24.21 | **51.3** |
| 13 | **Llama 4 Maverick** | 19.74 | 2.77 | 25.19 | **47.7** |
| 14 | **Llama 4 Scout** | 22.37 | 0.00 | 24.74 | **47.1** |
| 15 | Claude Opus 4.7 | 1.32 | 5.54 | 38.92 | **45.8** |
| 16 | DeepSeek V4-Pro | 6.58 | 9.00 | 29.62 | **45.2** |
| 17 | Qwen 3.6 Plus | 11.84 | 11.07 | 20.84 | **43.8** |
| 18 | o3-mini (high) | 13.16 | 8.32 | 21.22 | **42.7** |
| 19 | Claude Sonnet 4.6 | 2.63 | 4.16 | 20.62 | **27.4** |
| 20 | Claude Opus 4.6 | 0.00 | 1.39 | 23.31 | **24.7** |

> **Bold** = v5.0 new entrant. Columns: Cost = norm_cost × 0.25 (max 25.0 pts); IF = norm_IF × 0.18 (max 18.0 pts); Quality = weighted sum of remaining 16 dims × weights (summing to 57%); Main Score = Cost + IF + Quality.

### 9.2 Score Derivation Detail — Part A (Ranks 1–10)

| Dim | Wt | Gemini | GPT-5.5 | ML3 | Gemma3 | Phi-4 | Kimi | KAT | NovaPro | Grok3 | GPT-5.4 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Cost | 25% | 9.20 | 3.95 | 21.05 | 25.00 | 23.68 | 7.90 | 18.43 | 15.79 | 14.47 | 5.26 |
| IF | 18% | 18.00 | 13.84 | 9.00 | 9.00 | 9.00 | 15.23 | 6.93 | 9.00 | 9.00 | 9.68 |
| Term | 8% | 4.66 | 8.00 | 4.00 | 4.00 | 4.00 | 3.34 | 7.34 | 4.00 | 4.00 | 6.66 |
| SWE | 7% | 4.28 | 7.00 | 3.50 | 3.50 | 3.50 | 3.11 | 1.95 | 3.50 | 3.50 | 3.50 |
| SWEPro | 4% | 2.00 | 2.75 | 2.00 | 2.00 | 2.00 | 2.75 | 2.00 | 2.00 | 2.00 | 3.50 |
| LCB | 6% | 3.34 | 3.00 | 5.33 | 3.00 | 3.00 | 4.67 | 3.00 | 3.00 | 4.00 | 1.33 |
| GDP | 5% | 0.46 | 5.00 | 2.50 | 2.50 | 2.50 | 1.82 | 0.00 | 2.50 | 2.50 | 3.64 |
| Spd | 5% | 4.45 | 3.06 | 2.22 | 0.28 | 0.56 | 3.61 | 4.17 | 2.50 | 2.78 | 3.34 |
| τ² | 4% | 4.00 | 3.64 | 2.00 | 2.00 | 2.00 | 2.91 | 2.54 | 2.00 | 2.00 | 2.18 |
| OSW | 4% | 2.00 | 4.00 | 2.00 | 2.00 | 2.00 | 1.60 | 2.00 | 2.00 | 2.00 | 2.40 |
| BC | 3% | 2.14 | 3.00 | 1.50 | 1.50 | 1.50 | 0.86 | 1.50 | 1.50 | 1.50 | 2.57 |
| LCR | 2% | 1.78 | 1.00 | 1.00 | 1.00 | 1.00 | 1.22 | 0.67 | 1.00 | 1.00 | 2.00 |
| HLE | 2% | 1.86 | 1.71 | 1.00 | 1.00 | 1.00 | 1.14 | 0.43 | 1.00 | 1.00 | 1.57 |
| GPQA | 2% | 2.00 | 1.76 | 0.12 | 0.00 | 1.00 | 1.53 | 0.82 | 1.00 | 0.71 | 1.65 |
| MMLU | 2% | 1.75 | 1.00 | 1.00 | 1.00 | 1.00 | 0.75 | 1.00 | 1.00 | 1.00 | 1.00 |
| AIME | 1% | 0.42 | 0.50 | 0.50 | 0.50 | 0.50 | 0.67 | 0.50 | 0.50 | 0.50 | 0.50 |
| Sci | 1% | 1.00 | 0.50 | 0.50 | 0.50 | 0.50 | 0.75 | 0.25 | 0.50 | 0.50 | 0.92 |
| Omni | 1% | 1.00 | 0.00 | 0.50 | 0.50 | 0.50 | 0.43 | 0.50 | 0.50 | 0.50 | 0.50 |
| **Total** | | **64.3** | **63.7** | **59.7** | **59.3** | **59.2** | **54.3** | **54.0** | **53.3** | **53.0** | **52.2** |

### 9.3 Score Derivation Detail — Part B (Ranks 11–20)

| Dim | Wt | MiniMax | GLM | Maverick | Scout | Opus4.7 | DeepSeek | Qwen | o3-mini | Sonnet | Opus4.6 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Cost | 25% | 17.11 | 10.53 | 19.74 | 22.37 | 1.32 | 6.58 | 11.84 | 13.16 | 2.63 | 0.00 |
| IF | 18% | 12.46 | 16.61 | 2.77 | 0.00 | 5.54 | 9.00 | 11.07 | 8.32 | 4.16 | 1.39 |
| Term | 8% | 0.66 | 5.34 | 4.00 | 4.00 | 6.00 | 4.00 | 2.00 | 0.00 | 1.34 | 2.66 |
| SWE | 7% | 3.50 | 0.00 | 3.50 | 3.50 | 6.22 | 4.28 | 0.78 | 3.50 | 1.95 | 5.45 |
| SWEPro | 4% | 1.00 | 2.00 | 2.00 | 2.00 | 4.00 | 0.50 | 1.50 | 2.00 | 2.00 | 0.00 |
| LCB | 6% | 3.00 | 3.00 | 0.67 | 0.00 | 3.00 | 6.00 | 3.00 | 2.00 | 3.00 | 2.66 |
| GDP | 5% | 1.37 | 2.28 | 2.50 | 2.50 | 4.55 | 2.73 | 0.91 | 2.50 | 4.09 | 3.18 |
| Spd | 5% | 1.81 | 1.81 | 3.89 | 5.00 | 1.11 | 0.84 | 2.50 | 4.72 | 1.39 | 0.00 |
| τ² | 4% | 1.64 | 3.27 | 2.00 | 2.00 | 0.36 | 2.00 | 0.73 | 0.00 | 1.09 | 1.64 |
| OSW | 4% | 2.00 | 2.00 | 2.00 | 2.00 | 3.20 | 2.00 | 2.00 | 2.00 | 0.00 | 0.80 |
| BC | 3% | 1.50 | 0.00 | 1.50 | 1.50 | 0.43 | 1.29 | 1.50 | 1.50 | 1.50 | 1.71 |
| LCR | 2% | 0.89 | 0.44 | 1.00 | 1.00 | 1.56 | 1.00 | 1.22 | 1.00 | 0.22 | 0.00 |
| HLE | 2% | 0.57 | 1.00 | 0.14 | 0.00 | 2.00 | 1.29 | 0.71 | 0.29 | 0.86 | 1.43 |
| GPQA | 2% | 1.06 | 0.94 | 0.35 | 0.24 | 1.88 | 1.29 | 1.41 | 0.47 | 1.18 | 0.59 |
| MMLU | 2% | 1.00 | 1.00 | 0.50 | 0.00 | 2.00 | 1.25 | 1.50 | 0.25 | 1.00 | 1.00 |
| AIME | 1% | 0.50 | 0.42 | 0.50 | 0.50 | 0.92 | 0.50 | 0.50 | 0.17 | 0.00 | 0.92 |
| Sci | 1% | 0.58 | 0.42 | 0.17 | 0.00 | 0.83 | 0.50 | 0.08 | 0.33 | 0.50 | 0.67 |
| Omni | 1% | 0.71 | 0.29 | 0.50 | 0.50 | 0.86 | 0.14 | 0.50 | 0.50 | 0.50 | 0.57 |
| **Total** | | **51.4** | **51.3** | **47.7** | **47.1** | **45.8** | **45.2** | **43.8** | **42.7** | **27.4** | **24.7** |

> **Gemini #1 narrative:** Cost compression from n=20 drops Gemini's Cost contribution from 15.9 to 9.2 (−6.7 pts), but quality pool expansions add back ~1 pt: AIME 0.30→0.42, LCB 3.00→3.34, HLE 1.82→1.86. Net: −6.3 pts, holds #1 with 64.3.
> **GPT-5.5 #2:** Only −1.5 pts from v4.3; cost compression −2.8 pts, partially offset by LCB pool expansion (+0.34), HLE expansion (+0.14), AIME (+0.00), GPQA (+0.24). Holds #2 comfortably at 63.7.
> **New entrants #3–5:** ML3 (59.7), Gemma3 (59.3), Phi-4 (59.2) are cost arbitrage: ML3 has LCB rank 2 (88.9~) delivering +5.33; Gemma3 and Phi-4 are nearly pure-cost plays with 14–16 ⊘ dims each. Separation between #3–5 is within SEAL CI — effectively tied.
> **Nova Pro #8:** 17-of-18 dims are ⊘ (only Cost confirmed). Score 53.3 = Cost 15.79 + 17 × (50.0 × weight). Any confirmed benchmark fill that lands below neutral-50 will drop it; any above neutral will lift it. The most data-sparse model in the cohort.
> **Grok3 #9:** Marginally above Nova Pro due to LCB 66.7~ and Speed 55.6 lifting two dims above neutral-50. GPQA 35.3~ is a drag (below neutral). Both LCB and GPQA are ~ (secondary sources, possibly Grok3 Think mode).
> **Claude models:** Opus4.7 +1.9 pts (AIME 90→91.7, τ² 0→9.1, LCB pool expansion, GPQA compression minor); Sonnet +2.3 pts; Opus4.6 +4.2 pts — all three benefit from quality dimension pool expansions despite further cost compression. Opus4.6 gains +19.4 on LCB (25.0→44.4), +1.7 on AIME (90.0→91.7).

---

## 10. Ranking Changes (v4.0 → v4.3 → v5.0)

### Existing 12 Models

| Model | v4.0 | v4.0 Score | v4.3 | v4.3 Score | **v5.0** | **v5.0 Score** | Net v4.3→v5.0 |
|---|---|---|---|---|---|---|---|
| Gemini 3.1 Pro | #1 | 70.6 | #1 | 70.6 | **#1** | **64.3** | −6.3 pts; holds #1 |
| GPT-5.5 | #2 | 65.2 | #2 | 65.2 | **#2** | **63.7** | −1.5 pts; holds #2 |
| KAT-Coder-Pro-V2 | #3 | 58.0 | #3 | 58.0 | **#7** | **54.0** | −4.0 pts; 5 new models above |
| Kimi K2.6 | #5 | 57.6 | #4 | 57.6 | **#6** | **54.3** | −3.3 pts; ML3/Gemma3/Phi4 above |
| GLM 5.1 | #4 | 56.7 | #5 | 56.7 | **#12** | **51.3** | −5.4 pts; 7 new models above |
| MiniMax M2.7 | #6 | 53.6 | #6 | 53.6 | **#11** | **51.4** | −2.2 pts; 6 new models above |
| GPT-5.4 | #7 | 51.9 | #7 | 51.9 | **#10** | **52.2** | +0.3 pts; LCB 0.0→22.2 (+1.33) offsets cost |
| Qwen 3.6 Plus | #8 | 48.6 | #8 | 48.6 | **#17** | **43.8** | −4.8 pts; 9 new/lifted models above |
| DeepSeek V4-Pro | #9 | 48.2 | #9 | 48.2 | **#16** | **45.2** | −3.0 pts; LCB 100.0 unchanged; cost drops |
| Claude Opus 4.7 | #10 | 43.9 | #10 | 43.9 | **#15** | **45.8** | +1.9 pts; pool expansions dominate |
| Claude Sonnet 4.6 | #11 | 25.1 | #11 | 25.1 | **#19** | **27.4** | +2.3 pts; GDP/LCB/AIME all improve |
| Claude Opus 4.6 | #12 | 20.5 | #12 | 20.5 | **#20** | **24.7** | +4.2 pts; LCB +19.4, AIME +1.7 |

### 8 New Entrants (v5.0 debut)

| Model | v5.0 Rank | v5.0 Score | Quality Rank | Key strength |
|---|---|---|---|---|
| Mistral Large 3 | **#3** | **59.7** | #9 | LCB 88.9~ (rank 2/10) + cost $38.67 |
| Gemma 3 27B | **#4** | **59.3** | #13 | Cost $0.00 (free); 14 ⊘ dims |
| Phi-4 | **#5** | **59.2** | #10 | Cost $4.27 (rank 2/20); 16 ⊘ dims |
| Amazon Nova Pro | **#8** | **53.3** | #7 | Cost $200.98 (rank 8/20); 17 ⊘ dims |
| Grok 3 | **#9** | **53.0** | #6 | Cost + LCB 66.7~ + Speed 55.6; GPQA 35.3~ |
| Llama 4 Maverick | **#13** | **47.7** | #17 | Cost $62.28 + Speed 77.8; weak IF (15.4) |
| Llama 4 Scout | **#14** | **47.1** | #20 | Cost $26.42 + Speed #1 (100.0); IF 0.0 (last) |
| o3-mini (high) | **#18** | **42.7** | #18 | Speed #2 (94.4); τ² 0.0 (last), Term 0.0 (last) |

> **v4.0 full history context:** v1.0–v3.0 history available in git log. v4.0 added DeepSeek V4-Pro (12th model, 16 gap-fills). v4.1 added Pareto analysis and reliability dimension. v4.2 provisionally filled GPT-5.5 LCB at ~91.7%~. v4.3 (April 26, 2026) corrected two data errors: (1) Kimi τ²-Bench 72.4%→96.0% (+3.7 pts); (2) GPT-5.5 LCB reverted to ⊘ (misattribution confirmed). v5.0 (April 26, 2026) expands to 20 models with 8 new entrants.
