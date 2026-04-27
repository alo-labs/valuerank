# ValueRank — Scores
**Updated every version | Primary calculation file**

← [README](README.md) · [Raw Data](raw-data.md) · [Methodology](methodology.md)

---

## 7. Normalized Rank Scores

### 7.1 Methodology Recap

For each dimension, models with real data are ranked 1–n (best to worst). Score = `((n − rank) / (n − 1)) × 100`. Missing data = **50⊘**. All columns fully renormalized for the 23-model v0.6 field. Ties receive the average of their tied ranks' scores.

**n values by dimension (v0.6):** Cost=23, IF=14, Term=13, SWE=15, SWEPro=11, LCB=10, GDP=14, Spd=22, τ²=14, OSW=6, BC=8, LCR=11, HLE=17, GPQA=22, MMLU=13, AIME=11, Sci=14, Omni=8

### 7.2 Complete Normalized Score Matrix (18 dimensions)

| Model | Cost | IF | Term | SWE | SWEPro | LCB | GDP | Spd | τ² | OSW | BC | LCR | HLE | GPQA | MMLU | AIME | Sci | Omni |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gemini 3.1 Pro | 31.8 | **100.0** | 58.3 | 75.0 | 50.0⊘ | 44.4 | 7.7 | **90.5** | **100.0** | 50.0⊘ | 71.4 | **90.0** | 93.8 | **100.0** | **91.7** | 60.0 | **100.0** | **100.0** |
| GPT-5.5 | 13.6 | 69.2 | **100.0** | **100.0** | 75.0 | 50.0⊘ | **100.0** | 61.9 | 92.3 | **100.0** | **100.0** | 50.0⊘ | 87.5 | 90.5 | 50.0⊘ | 50.0⊘ | 50.0⊘ | 0.0 |
| Mistral Large 3 | **86.4** | 50.0⊘ | 50.0⊘ | 50.0⊘ | 50.0⊘ | **88.9~** | 50.0⊘ | 47.6 | 50.0⊘ | 50.0⊘ | 50.0⊘ | 50.0⊘ | 50.0⊘ | 0.0 | 50.0⊘ | 50.0⊘ | 50.0⊘ | 50.0⊘ |
| Phi-4 | **95.5** | 50.0⊘ | 50.0⊘ | 50.0⊘ | 50.0⊘ | 50.0⊘ | 50.0⊘ | 14.3 | 50.0⊘ | 50.0⊘ | 50.0⊘ | 50.0⊘ | 50.0⊘ | 50.0⊘ | 50.0⊘ | 50.0⊘ | 50.0⊘ | 50.0⊘ |
| MiMo-V2.5-Pro | 54.5 | **76.9** | 50.0⊘ | 50.0⊘ | 50.0~ | 50.0⊘ | 50.0⊘ | 57.1 | 69.2 | 50.0⊘ | 50.0⊘ | 30.0 | 56.2 | 52.4 | 50.0⊘ | 50.0⊘ | 61.5 | 50.0⊘ |
| Kimi K2.6 | 27.3 | 84.6 | 41.7 | 64.3 | 75.0 | 77.8 | 46.2 | 76.2 | 76.9 | 40.0 | 28.6 | 65.0 | 62.5 | 81.0 | 41.7 | 80.0 | 76.9 | 42.9 |
| Gemma 4 31B Dense | **100.0** | 50.0⊘ | 50.0⊘ | 14.3~ | 0.0~ | 66.7~ | 30.8 | 23.8 | 46.2 | 50.0⊘ | 50.0⊘ | 50.0⊘ | 50.0⊘ | 33.3 | 50.0~ | 30.0~ | 50.0⊘ | 50.0⊘ |
| KAT-Coder-Pro-V2 | 72.7 | 38.5 | **91.7†** | 53.6 | 50.0⊘ | 50.0⊘ | 0.0 | **85.7** | 61.5 | 50.0⊘ | 50.0⊘ | 40.0 | 18.8 | 38.1 | 50.0⊘ | 50.0⊘ | 30.8 | 50.0⊘ |
| GLM 5.1 | 40.9 | **92.3** | 66.7 | 35.7 | 60.0 | 50.0⊘ | 53.8 | 40.5 | **84.6** | 50.0⊘ | 0.0~ | 20.0 | 50.0 | 47.6 | 58.3 | 60.0 | 38.5 | 28.6 |
| o4-mini | 59.1 | 50.0⊘ | 50.0⊘ | 21.4 | 50.0⊘ | 50.0⊘ | 50.0⊘ | **100.0** | 50.0⊘ | 50.0⊘ | 50.0⊘ | 50.0⊘ | 50.0⊘ | 19.0 | 50.0⊘ | 40.0 | 50.0⊘ | 50.0⊘ |
| Gemma 4 27B MoE | 81.8 | 50.0⊘ | 50.0⊘ | 7.1~ | 50.0⊘ | 55.6~ | 23.1 | 50.0⊘ | 23.1~ | 50.0⊘ | 50.0⊘ | 50.0⊘ | 50.0⊘ | 23.8 | 33.3~ | 20.0~ | 50.0⊘ | 50.0⊘ |
| GPT-5.4 | 18.2 | 46.2 | 83.3 | 50.0⊘ | **90.0** | 22.2 | 76.9 | 66.7 | 53.8 | 60.0 | **85.7** | **100.0** | 81.2 | 85.7 | 50.0⊘ | 50.0⊘ | **92.3** | 50.0⊘ |
| MiniMax M2.7 | 68.2 | 61.5 | 0.0 | 50.0⊘ | 30.0~ | 50.0⊘ | 38.5 | 40.5 | 34.6 | 50.0⊘ | 50.0⊘ | 50.0 | 31.2 | 57.1 | 50.0⊘ | 50.0⊘ | 53.8 | **71.4** |
| Grok 4.20 | 45.5 | 50.0⊘ | 50.0⊘ | 28.6~ | 50.0⊘ | 50.0⊘ | 50.0⊘‡‡ | 71.4 | 50.0⊘ | 50.0⊘ | 50.0⊘ | 50.0⊘ | 25.0~ | 66.7~ | 66.7~ | 60.0~ | 50.0⊘ | 50.0⊘ |
| Llama 4 Maverick | **77.3** | 15.4 | 50.0⊘ | 50.0⊘ | 50.0⊘ | 11.1~ | 50.0⊘ | **81.0** | 50.0⊘ | 50.0⊘ | 50.0⊘ | 50.0⊘ | 12.5 | 14.3 | 25.0 | 50.0⊘ | 23.1 | 50.0⊘ |
| Llama 4 Scout | **90.9** | 0.0 | 50.0⊘ | 50.0⊘ | 50.0⊘ | 0.0~ | 50.0⊘ | **95.2** | 50.0⊘ | 50.0⊘ | 50.0⊘ | 50.0⊘ | 0.0 | 9.5 | 8.3 | 50.0⊘ | 0.0 | 50.0⊘ |
| DeepSeek V4-Pro | 22.7 | 50.0⊘ | 50.0†self | 75.0 | 20.0 | **100.0** | 61.5 | 19.0 | 50.0⊘ | 50.0⊘ | 42.9 | 50.0⊘ | 68.8 | 71.4 | 75.0 | 50.0⊘ | 50.0⊘ | 14.3 |
| Claude Opus 4.7 | 4.5 | 30.8 | 75.0 | **92.9** | **100.0** | 50.0⊘ | **92.3** | 28.6 | 0.0 | **80.0** | 14.3 | **80.0** | **100.0** | **95.2** | **100.0~** | **95.0** | **84.6** | **85.7** |
| Qwen 3.6 Plus | 50.0 | 53.8 | 16.7 | 42.9 | 40.0~ | 50.0⊘ | 15.4 | 52.4 | 7.7 | 50.0⊘ | 50.0⊘ | 65.0 | 37.5 | 76.2 | 83.3 | 50.0⊘ | 7.7 | 50.0⊘ |
| Amazon Nova Premier | 63.6 | 50.0⊘ | 50.0⊘ | 0.0 | 50.0⊘ | 50.0⊘ | 50.0⊘ | 4.8 | 50.0⊘ | 50.0⊘ | 50.0⊘ | 50.0⊘ | 6.2 | 4.8 | 0.0 | 0.0~ | 15.4~ | 50.0⊘ |
| Qwen 3.6 Max Preview | 36.4 | 50.0⊘ | 29.2~ | 50.0⊘ | 50.0⊘ | 50.0⊘ | 50.0⊘ | 9.5 | 50.0⊘ | 50.0⊘ | 50.0⊘ | 50.0⊘ | 50.0⊘ | 42.9~ | 16.7~ | 50.0⊘ | 50.0⊘ | 50.0⊘ |
| Claude Sonnet 4.6 | 9.1 | 23.1 | 8.3 | 53.6 | 50.0⊘ | 50.0⊘ | **84.6** | 33.3 | 15.4 | 0.0 | 50.0⊘ | 10.0 | 43.8 | 61.9 | 50.0⊘ | 10.0 | 46.2 | 50.0⊘ |
| Claude Opus 4.6 | 0.0 | 7.7 | 29.2 | **85.7** | 10.0 | 33.3 | 69.2 | 0.0 | 34.6 | 20.0 | 57.1~ | 0.0 | 75.0 | 28.6 | 50.0⊘ | **95.0** | 69.2 | 57.1 |

**⊘** = missing data, neutral score 50.0. **~** = secondary source (probable confidence). **†/†self** = self-reported, not on canonical leaderboard. **‡‡** = Grok 4.20 GDP ELO marked ⊘ (Arena ELO 1482 found; GDPval ELO not confirmed).

**Key v0.6 dimension normalization notes (n changes from v0.5):**
- **Cost (n=20→23):** Added Gemma 4 27B MoE ($41.51), MiMo ($461.59), Qwen 3.6 Max Preview ($860.56). Replacements shifted 4 positions: Gemma 3 ($0)→Gemma 4 31B ($0, still rank 1); Nova Pro ($201)→Nova Premier ($376); Grok 3 ($312)→Grok 4.20 ($514); o3-mini ($315)→o4-mini ($460). Formula now ((23−rank)/22)×100. Phi-4 stays rank 2 (95.5, was 94.7); Gemini drops from rank 13 (36.8) to rank 16 (31.8). All paid models compressed by 2–6 pts.
- **IF (n=14):** Net flat — added MiMo (79.9, rank 6), lost o3-mini (67.1). MiMo enters mid-pack; existing top-5 unchanged.
- **Term (n=13):** Net flat — added Qwen Max (65.4~, rank 9), lost o3-mini (6.1, was last). MiniMax drops from 8.3 to 0.0 (now last).
- **SWE (n=10→15):** Massive expansion — 5 new real scores from replacements/new (Gemma 4 31B 64, Nova Premier 42.4, Grok 4.20 70.8, o4-mini 68.1, Gemma 4 27B MoE 60). Kimi rises 44.4→64.3 (rank 6/15); GPT-5.5 holds 100.0 (rank 1).
- **SWEPro (n=9→11):** Added Gemma 4 31B (48), MiMo (57.2). MiMo rank 5/11 (50.0); Opus 4.7 holds rank 1 (100.0).
- **LCB (n=10):** Net flat — added Gemma 4 31B (80~) and Gemma 4 27B MoE (77~), lost Grok 3 (79.4~) and o3-mini (71.7~). DeepSeek holds rank 1 (100.0); ML3 rank 2 (88.9~).
- **GDP (n=12→14):** Added Gemma 4 31B ELO 1452, Gemma 4 27B MoE ELO 1441. Grok 4.20 GDP marked ⊘ (no GDPval ELO confirmed). KAT still rank 14 last (0.0).
- **Spd (n=19→22):** Gained 3 real scores: Nova Premier (28.2, was ⊘ for Nova Pro), Qwen Max (33.3, new), MiMo (61.0, new). Plus o3-mini 131.7→o4-mini 159.5 takes over rank 1 (100.0). Llama 4 Scout drops 100.0→95.2.
- **τ² (n=12→14):** Added MiMo (94.2, rank 4), Gemma 4 31B (86.4), Gemma 4 27B MoE (84~). Lost o3-mini (28.7~, was last). Opus 4.7 still last (0.0).
- **HLE (n=15→17):** Added Nova Premier (4.7), Grok 4.20 (24~), MiMo (33.8). Lost o3-mini (12.3). Opus 4.7 holds rank 1 (100.0).
- **GPQA (n=18→22):** Added 4 real scores from new entrants and 1 net from replacements (Gemma 4 31B 84.3 vs Gemma 3 42.4 — both real, different cohort positions; MiMo 86.6, Qwen Max 86.0~, Gemma 4 27B MoE 82.3). Gemini holds 100.0; Opus 4.7 95.2.
- **MMLU (n=9→13):** Added 4 real scores (Gemma 4 31B 85.2~, Nova Premier 73.3, Grok 4.20 86.6~, Qwen Max 79.0~, Gemma 4 27B MoE 82.6~) minus o3-mini (79.1) lost. Opus 4.7 holds rank 1 (100.0); Gemini 91.7.
- **AIME (n=7→11):** Added 4 real scores (Gemma 4 31B 89.2~, Nova Premier 17.0~, Grok 4.20 95.0~, Gemma 4 27B MoE 88.3~); o3-mini 77.0→o4-mini 92.7 (rank shifts). Opus 4.7 / Opus 4.6 tied rank 1.5 (95.0).
- **Sci (n=13→14):** Added MiMo (50.2) and Nova Premier (27.9~); lost o3-mini (39.8). Gemini holds 100.0.

### 7.3 Cost Score Derivation (v0.6)

Cost ranks (cheapest = rank 1, n=23 real scorers). Formula: ((23−rank)/22)×100.

| Model | AA Eval Cost | Rank | Score |
|---|---|---|---|
| Gemma 4 31B Dense | $0.00 | 1 | **100.0** |
| Phi-4 | $4.27 | 2 | **95.5** |
| Llama 4 Scout | $26.42 | 3 | **90.9** |
| Mistral Large 3 | $38.67 | 4 | **86.4** |
| Gemma 4 27B MoE | $41.51 | 5 | **81.8** |
| Llama 4 Maverick | $62.28 | 6 | **77.3** |
| KAT-Coder-Pro-V2 | $73.49 | 7 | **72.7** |
| MiniMax M2.7 | $175.51 | 8 | **68.2** |
| Amazon Nova Premier | $375.98 | 9 | **63.6** |
| o4-mini | $459.80 | 10 | **59.1** |
| MiMo-V2.5-Pro | $461.59 | 11 | **54.5** |
| Qwen 3.6 Plus | $482.65 | 12 | **50.0** |
| Grok 4.20 | $514.16 | 13 | **45.5** |
| GLM 5.1 | $543.95 | 14 | **40.9** |
| Qwen 3.6 Max Preview | $860.56 | 15 | **36.4** |
| Gemini 3.1 Pro | $892.28 | 16 | **31.8** |
| Kimi K2.6 | $947.87 | 17 | **27.3** |
| DeepSeek V4-Pro | $1,071.28 | 18 | **22.7** |
| GPT-5.4 | $2,851.01 | 19 | **18.2** |
| GPT-5.5 | $3,357.00 | 20 | **13.6** |
| Claude Sonnet 4.6 | $3,959.36 | 21 | **9.1** |
| Claude Opus 4.7 | $4,811.04 | 22 | **4.5** |
| Claude Opus 4.6 | $4,969.68 | 23 | **0.0** |

> **v0.5→v0.6 cost compression:** n expands 20→23. All paid models drop 2–6 pts. Largest movers: KAT 73.7→72.7, Gemini 36.8→31.8, GPT-5.5 15.8→13.6. Gemma 4 31B Dense holds rank 1 (100.0, identical to Gemma 3 27B's free pricing). The 3 new entrants slot into mid-pack: Gemma 4 27B MoE rank 5 (81.8), Nova Premier rank 9 (63.6), MiMo/o4-mini/Qwen Max rank 10–15.

---

## 8. Quality-Only Ranking (Unweighted)

Equally weighting all 17 non-cost dimensions (5.88% each) to show pure capability without cost penalty.

| Rank | Model | IF Score | Total Quality |
|---|---|---|---|
| 1 | **Gemini 3.1 Pro** | 100.0 | **75.5** |
| 2 | GPT-5.5 | 69.2 | **72.1** |
| 3 | Claude Opus 4.7 | 30.8 | **70.8** |
| 4 | GPT-5.4 | 46.2 | **67.3** |
| 5 | Kimi K2.6 | 84.6 | **62.4** |
| 6 | MiMo-V2.5-Pro | 76.9 | **53.1** |
| 7 | DeepSeek V4-Pro | 50.0⊘ | **52.8** |
| 8 | Grok 4.20 | 50.0⊘ | **51.1** |
| 9 | Mistral Large 3 | 50.0⊘ | **49.2** |
| 10 | GLM 5.1 | 92.3 | **49.2** |
| 11 | o4-mini | 50.0⊘ | **48.8** |
| 12 | Phi-4 | 50.0⊘ | **47.9** |
| 13 | KAT-Coder-Pro-V2 | 38.5 | **47.6** |
| 14 | MiniMax M2.7 | 61.5 | **45.2** |
| 15 | Qwen 3.6 Plus | 53.8 | **44.0** |
| 16 | Qwen 3.6 Max Preview | 50.0⊘ | **44.0** |
| 17 | Claude Opus 4.6 | 7.7 | **42.5** |
| 18 | Gemma 4 31B Dense | 50.0⊘ | **40.9** |
| 19 | Gemma 4 27B MoE | 50.0⊘ | **40.4** |
| 20 | Llama 4 Maverick | 15.4 | **40.1** |
| 21 | Claude Sonnet 4.6 | 23.1 | **37.7** |
| 22 | Llama 4 Scout | 0.0 | **36.1** |
| 23 | Amazon Nova Premier | 50.0⊘ | **31.2** |

> **‡** Total Quality = equal-weighted avg of all 17 non-cost dims (each 1/17 = 5.88%).
>
> **v0.6 quality notes:** Gemini retains quality #1 (75.5, +1.7 from expanded SWE/Tau2/MMLU pools). MiMo's debut at quality #6 (53.1) is driven by IF 76.9 (rank 5) + τ² 94.2 + GPQA 86.6 + LCB 73.3. Grok 4.20 (#8, 51.1) lifts above Mistral Large 3 (#9) on GPQA/MMLU/AIME real scores despite 11 ⊘ dims. Nova Premier (#23, 31.2) is dominated by floor scores (HLE 4.7%, GPQA 56.9%, MMLU 73.3%, Speed 28.2 tok/s) — significantly lower than Nova Pro's 50.0⊘ neutral baseline.

---

## 9. Final Cost-Weighted Ranking

**Weights:** Cost 25%, IF 18%, Term 8%, SWE 7%, SWEPro 4%, LCB 6%, GDP 5%, Spd 5%, τ² 4%, OSW 4%, BC 3%, LCR 2%, HLE 2%, GPQA 2%, MMLU 2%, AIME 1%, Sci 1%, Omni 1%

### 9.1 Final Weighted Scores

| Rank | Model | Cost (25%) | IF (18%) | Quality (57%) | Main Score |
|---|---|---|---|---|---|
| 🥇 1 | **Gemini 3.1 Pro** | 7.95 | 18.00 | 37.79 | **63.7** |
| 🥈 2 | **GPT-5.5** | 3.40 | 12.46 | 46.34 | **62.2** |
| 🥉 3 | Mistral Large 3 | 21.60 | 9.00 | 29.66 | **60.3** |
| 4 | Phi-4 | 23.88 | 9.00 | 26.71 | **59.6** |
| 5 | **MiMo-V2.5-Pro** | 13.62 | 13.84 | 29.50 | **57.0** |
| 6 | Kimi K2.6 | 6.83 | 15.23 | 34.13 | **56.2** |
| 7 | **Gemma 4 31B Dense** | 25.00 | 9.00 | 22.05 | **56.0** |
| 8 | KAT-Coder-Pro-V2 | 18.18 | 6.93 | 30.61 | **55.7** |
| 9 | GLM 5.1 | 10.22 | 16.61 | 28.21 | **55.0** |
| 10 | **o4-mini** | 14.78 | 9.00 | 28.36 | **52.1** |
| 11 | **Gemma 4 27B MoE** | 20.45 | 9.00 | 22.27 | **51.7** |
| 12 | GPT-5.4 | 4.55 | 8.32 | 37.59 | **50.5** |
| 13 | MiniMax M2.7 | 17.05 | 11.07 | 22.10 | **50.2** |
| 14 | **Grok 4.20** | 11.38 | 9.00 | 28.31 | **48.7** |
| 15 | Llama 4 Maverick | 19.32 | 2.77 | 25.51 | **47.6** |
| 16 | Llama 4 Scout | 22.73 | 0.00 | 24.55 | **47.3** |
| 17 | DeepSeek V4-Pro | 5.67 | 9.00 | 31.79 | **46.5** |
| 18 | Claude Opus 4.7 | 1.12 | 5.54 | 39.34 | **46.0** |
| 19 | Qwen 3.6 Plus | 12.50 | 9.68 | 22.45 | **44.6** |
| 20 | **Amazon Nova Premier** | 15.90 | 9.00 | 19.05 | **44.0** |
| 21 | **Qwen 3.6 Max Preview** | 9.10 | 9.00 | 24.00 | **42.1** |
| 22 | Claude Sonnet 4.6 | 2.27 | 4.16 | 21.78 | **28.2** |
| 23 | Claude Opus 4.6 | 0.00 | 1.39 | 23.39 | **24.8** |

> **Bold** = v0.6 new or replaced entrant. Columns: Cost = norm_cost × 0.25 (max 25.0 pts); IF = norm_IF × 0.18 (max 18.0 pts); Quality = weighted sum of remaining 16 dims (summing to 57%); Main Score = Cost + IF + Quality.

### 9.2 Score Derivation Detail — Part A (Ranks 1–12)

| Dim | Wt | Gemini | GPT-5.5 | ML3 | Phi-4 | MiMo | Kimi | Gemma4-31B | KAT | GLM | o4-mini | Gemma4-MoE | GPT-5.4 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cost | 25% | 7.95 | 3.40 | 21.60 | 23.88 | 13.62 | 6.83 | 25.00 | 18.18 | 10.22 | 14.78 | 20.45 | 4.55 |
| IF | 18% | 18.00 | 12.46 | 9.00 | 9.00 | 13.84 | 15.23 | 9.00 | 6.93 | 16.61 | 9.00 | 9.00 | 8.32 |
| Term | 8% | 4.66 | 8.00 | 4.00 | 4.00 | 4.00 | 3.34 | 4.00 | 7.34 | 5.34 | 4.00 | 4.00 | 6.66 |
| SWE | 7% | 5.25 | 7.00 | 3.50 | 3.50 | 3.50 | 4.50 | 1.00 | 3.75 | 2.50 | 1.50 | 0.50 | 3.50 |
| SWEPro | 4% | 2.00 | 3.00 | 2.00 | 2.00 | 2.00 | 3.00 | 0.00 | 2.00 | 2.40 | 2.00 | 2.00 | 3.60 |
| LCB | 6% | 2.66 | 3.00 | 5.33 | 3.00 | 3.00 | 4.67 | 4.00 | 3.00 | 3.00 | 3.00 | 3.34 | 1.33 |
| GDP | 5% | 0.39 | 5.00 | 2.50 | 2.50 | 2.50 | 2.31 | 1.54 | 0.00 | 2.69 | 2.50 | 1.16 | 3.85 |
| Spd | 5% | 4.53 | 3.10 | 2.38 | 0.72 | 2.86 | 3.81 | 1.19 | 4.29 | 2.02 | 5.00 | 2.50 | 3.34 |
| τ² | 4% | 4.00 | 3.69 | 2.00 | 2.00 | 2.77 | 3.08 | 1.85 | 2.46 | 3.38 | 2.00 | 0.92 | 2.15 |
| OSW | 4% | 2.00 | 4.00 | 2.00 | 2.00 | 2.00 | 1.60 | 2.00 | 2.00 | 2.00 | 2.00 | 2.00 | 2.40 |
| BC | 3% | 2.14 | 3.00 | 1.50 | 1.50 | 1.50 | 0.86 | 1.50 | 1.50 | 0.00 | 1.50 | 1.50 | 2.57 |
| LCR | 2% | 1.80 | 1.00 | 1.00 | 1.00 | 0.60 | 1.30 | 1.00 | 0.80 | 0.40 | 1.00 | 1.00 | 2.00 |
| HLE | 2% | 1.88 | 1.75 | 1.00 | 1.00 | 1.12 | 1.25 | 1.00 | 0.38 | 1.00 | 1.00 | 1.00 | 1.62 |
| GPQA | 2% | 2.00 | 1.81 | 0.00 | 1.00 | 1.05 | 1.62 | 0.67 | 0.76 | 0.95 | 0.38 | 0.48 | 1.71 |
| MMLU | 2% | 1.83 | 1.00 | 1.00 | 1.00 | 1.00 | 0.83 | 1.00 | 1.00 | 1.17 | 1.00 | 0.67 | 1.00 |
| AIME | 1% | 0.60 | 0.50 | 0.50 | 0.50 | 0.50 | 0.80 | 0.30 | 0.50 | 0.60 | 0.40 | 0.20 | 0.50 |
| Sci | 1% | 1.00 | 0.50 | 0.50 | 0.50 | 0.61 | 0.77 | 0.50 | 0.31 | 0.39 | 0.50 | 0.50 | 0.92 |
| Omni | 1% | 1.00 | 0.00 | 0.50 | 0.50 | 0.50 | 0.43 | 0.50 | 0.50 | 0.29 | 0.50 | 0.50 | 0.50 |
| **Total** |  | **63.7** | **62.2** | **60.3** | **59.6** | **57.0** | **56.2** | **56.0** | **55.7** | **55.0** | **52.1** | **51.7** | **50.5** |

### 9.3 Score Derivation Detail — Part B (Ranks 13–23)

| Dim | Wt | MiniMax | Grok 4.20 | Maverick | Scout | DeepSeek | Opus 4.7 | Qwen Plus | Nova Prem | Qwen Max | Sonnet 4.6 | Opus 4.6 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cost | 25% | 17.05 | 11.38 | 19.32 | 22.73 | 5.67 | 1.12 | 12.50 | 15.90 | 9.10 | 2.27 | 0.00 |
| IF | 18% | 11.07 | 9.00 | 2.77 | 0.00 | 9.00 | 5.54 | 9.68 | 9.00 | 9.00 | 4.16 | 1.39 |
| Term | 8% | 0.00 | 4.00 | 4.00 | 4.00 | 4.00 | 6.00 | 1.34 | 4.00 | 2.34 | 0.66 | 2.34 |
| SWE | 7% | 3.50 | 2.00 | 3.50 | 3.50 | 5.25 | 6.50 | 3.00 | 0.00 | 3.50 | 3.75 | 6.00 |
| SWEPro | 4% | 1.20 | 2.00 | 2.00 | 2.00 | 0.80 | 4.00 | 1.60 | 2.00 | 2.00 | 2.00 | 0.40 |
| LCB | 6% | 3.00 | 3.00 | 0.67 | 0.00 | 6.00 | 3.00 | 3.00 | 3.00 | 3.00 | 3.00 | 2.00 |
| GDP | 5% | 1.93 | 2.50 | 2.50 | 2.50 | 3.08 | 4.62 | 0.77 | 2.50 | 2.50 | 4.23 | 3.46 |
| Spd | 5% | 2.02 | 3.57 | 4.05 | 4.76 | 0.95 | 1.43 | 2.62 | 0.24 | 0.48 | 1.67 | 0.00 |
| τ² | 4% | 1.38 | 2.00 | 2.00 | 2.00 | 2.00 | 0.00 | 0.31 | 2.00 | 2.00 | 0.62 | 1.38 |
| OSW | 4% | 2.00 | 2.00 | 2.00 | 2.00 | 2.00 | 3.20 | 2.00 | 2.00 | 2.00 | 0.00 | 0.80 |
| BC | 3% | 1.50 | 1.50 | 1.50 | 1.50 | 1.29 | 0.43 | 1.50 | 1.50 | 1.50 | 1.50 | 1.71 |
| LCR | 2% | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.60 | 1.30 | 1.00 | 1.00 | 0.20 | 0.00 |
| HLE | 2% | 0.62 | 0.50 | 0.25 | 0.00 | 1.38 | 2.00 | 0.75 | 0.12 | 1.00 | 0.88 | 1.50 |
| GPQA | 2% | 1.14 | 1.33 | 0.29 | 0.19 | 1.43 | 1.90 | 1.52 | 0.10 | 0.86 | 1.24 | 0.57 |
| MMLU | 2% | 1.00 | 1.33 | 0.50 | 0.17 | 1.50 | 2.00 | 1.67 | 0.00 | 0.33 | 1.00 | 1.00 |
| AIME | 1% | 0.50 | 0.60 | 0.50 | 0.50 | 0.50 | 0.95 | 0.50 | 0.00 | 0.50 | 0.10 | 0.95 |
| Sci | 1% | 0.54 | 0.50 | 0.23 | 0.00 | 0.50 | 0.85 | 0.08 | 0.15 | 0.50 | 0.46 | 0.69 |
| Omni | 1% | 0.71 | 0.50 | 0.50 | 0.50 | 0.14 | 0.86 | 0.50 | 0.50 | 0.50 | 0.50 | 0.57 |
| **Total** |  | **50.2** | **48.7** | **47.6** | **47.3** | **46.5** | **46.0** | **44.6** | **44.0** | **42.1** | **28.2** | **24.8** |

> **Gemini #1 narrative:** Cost compression from n=23 drops Gemini's Cost contribution from 9.20 to 7.95 (−1.25 pts), but quality pool expansions add ~0.7 pts: SWE 4.28→5.25 (+0.97), AIME 0.42→0.60, MMLU 1.75→1.83. Net: −0.6 pts; holds #1 at 63.7.
> **GPT-5.5 #2:** Cost compression −0.55 pts; quality flat. SWEPro 2.75→3.00, GPQA 1.76→1.81. Holds #2 at 62.2 (−1.5 from v0.5).
> **MiMo #5 debut:** Xiaomi's first ValueRank entry lands at #5 (57.0). Driven by IF 76.9 (13.84 pts, rank 6/14), τ² 94.2 (2.77, rank 4), GPQA 86.6 (1.05, rank 6/22), LCR 73.3 (0.60), and a respectable cost ($461.59, 13.62). The main weakness: 9 ⊘ dims, including Term-Bench, OSWorld, BrowseComp.
> **Gemma 4 31B Dense #7:** Replaces Gemma 3 27B (#4 in v0.5) — drops 3 spots despite being functionally superior. Why: Gemma 3 had 15 ⊘ dims worth 50.0 each (~75% of its score); Gemma 4 31B's real scores in SWE (14.3), SWEPro (0.0), GPQA (33.3), AIME (30.0), MMLU (50.0) actually pull the score *down* relative to a 50.0 neutral. The cost rank-1 advantage (25.00 pts) is preserved, but the quality contribution drops from "all neutral" to "real low-mid".
> **o4-mini #10:** Replaces o3-mini (#18 in v0.5) — gains 8 spots. Key drivers: SWE 68.1% (real, 1.50 pts), GPQA 81.4% (0.38), AIME 92.7% (0.40), Speed 159.5 tok/s (5.00 pts, rank 1/22). Cost slightly higher ($459.80 vs $314.72) but the real data fills offset that easily.
> **Grok 4.20 #14:** Replaces Grok 3 (#9 in v0.5) — drops 5 spots. The new real scores (GPQA 88.0~, MMLU 86.6~, AIME 95.0~, HLE 24.0~, SWE 70.8~, Speed 78.3) are competitive but cost more than doubled ($312→$514). Cost contribution drops 14.47→11.38 (−3.1 pts). The GDP marker ⊘ keeps GDP at neutral instead of real-low.
> **Nova Premier #20:** Replaces Nova Pro (#8 in v0.5) — drops 12 spots. The price/quality tradeoff worsens: cost rises $201→$376 (cost 15.79→15.90, basically flat) but the real benchmark fills are floor-level: HLE 4.7% (0.12), GPQA 56.9% (0.10), MMLU 73.3% (0.00, rank 13/13 last), Speed 28.2 (0.24). Nova Pro's 50.0⊘ neutrals were worth 19.05 pts; Nova Premier's actual scores total 19.05 pts but the worse positions drag overall down.
> **Qwen 3.6 Max Preview #21:** Pool addition. Quality #16 (44.0) — same as Qwen 3.6 Plus despite higher cost ($860 vs $483). The MMLU-Pro 79.0%~ (lower than Qwen Plus's 88.5%) is suspicious — probable methodology mismatch. Net: Qwen Max sits below Qwen Plus on overall score (42.1 vs 44.6).
> **Claude Opus 4.7 #18:** Drops 3 spots from #15. Cost 5.3→4.5 (−0.8); quality flat. Other models lifted past it.

---

## 10. Ranking Changes (v0.5 → v0.6)

### Existing Models Carried Over

| Model | v0.5 Rank | v0.5 Score | **v0.6 Rank** | **v0.6 Score** | Net |
|---|---|---|---|---|---|
| Gemini 3.1 Pro | #1 | 64.3 | **#1** | **63.7** | −0.6 pts; holds #1 |
| GPT-5.5 | #2 | 63.7 | **#2** | **62.2** | −1.5 pts; holds #2 |
| Mistral Large 3 | #3 | 59.7 | **#3** | **60.3** | +0.6 pts; holds #3 |
| Phi-4 | #5 | 59.2 | **#4** | **59.6** | +0.4 pts; gains 1 (Gemma 3→Gemma 4 dropped) |
| Kimi K2.6 | #6 | 54.3 | **#6** | **56.2** | +1.9 pts; quality pool expansions lift |
| KAT-Coder-Pro-V2 | #7 | 54.0 | **#8** | **55.7** | +1.7 pts; drops 1 (MiMo enters above) |
| GPT-5.4 | #10 | 52.2 | **#12** | **50.5** | −1.7 pts; cost compression dominates |
| MiniMax M2.7 | #11 | 51.4 | **#13** | **50.2** | −1.2 pts; drops 2 |
| GLM 5.1 | #12 | 51.3 | **#9** | **55.0** | +3.7 pts; gains 3 from SWE/SWEPro/Tau2 expansions |
| Llama 4 Maverick | #13 | 47.7 | **#15** | **47.6** | flat; drops 2 |
| Llama 4 Scout | #14 | 47.1 | **#16** | **47.3** | +0.2 pts; drops 2 |
| Claude Opus 4.7 | #15 | 45.8 | **#18** | **46.0** | +0.2 pts; drops 3 |
| DeepSeek V4-Pro | #16 | 45.2 | **#17** | **46.5** | +1.3 pts; drops 1 |
| Qwen 3.6 Plus | #17 | 43.8 | **#19** | **44.6** | +0.8 pts; drops 2 |
| Claude Sonnet 4.6 | #19 | 27.4 | **#22** | **28.2** | +0.8 pts; drops 3 |
| Claude Opus 4.6 | #20 | 24.7 | **#23** | **24.8** | +0.1 pts; drops 3 |

### Replaced Models (4 swaps)

| Old (v0.5) | v0.5 Rank | New (v0.6) | **v0.6 Rank** | Driver |
|---|---|---|---|---|
| Gemma 3 27B | #4 (59.3) | **Gemma 4 31B Dense** | **#7 (56.0)** | Real benchmarks pull score below neutral-50 baselines |
| Amazon Nova Pro | #8 (53.3) | **Amazon Nova Premier** | **#20 (44.0)** | Higher cost + real low scores (HLE 4.7%, GPQA 56.9%) hurt |
| Grok 3 | #9 (53.0) | **Grok 4.20** | **#14 (48.7)** | Cost +65% with mixed quality fills |
| o3-mini (high) | #18 (42.7) | **o4-mini** | **#10 (52.1)** | SWE 68.1% real fill + Speed #1 (159.5 tok/s) lifts +8 spots |

### New Pool Additions (3 new entrants)

| Model | **v0.6 Rank** | **v0.6 Score** | Quality Rank | Key strength |
|---|---|---|---|---|
| **MiMo-V2.5-Pro** | **#5** | **57.0** | #6 | IF 79.9% + τ² 94.2% + AA Index 54 |
| **Gemma 4 27B MoE** | **#11** | **51.7** | #19 | Free tier #5 cost rank ($41.51) + real GPQA 82.3% |
| **Qwen 3.6 Max Preview** | **#21** | **42.1** | #16 | Limited fills; flagship cost ($860) without offsetting quality |

> **v0.5 → v0.6 narrative:** Pool expanded 20 → 23. Top 3 unchanged (Gemini, GPT-5.5, ML3). Phi-4 gains 1 spot (4 → 4 actually 5 → 4) as Gemma 3 (#4) was replaced by Gemma 4 31B which drops to #7. MiMo-V2.5-Pro debuts at #5, the strongest new entry — Xiaomi's first appearance. GLM jumps from #12 to #9 (+3, biggest gainer) as the SWE / SWEPro / τ² expansions credit its existing real scores. The bottom of the pack expanded with Nova Premier (#20), Qwen Max (#21), Sonnet (#22), Opus 4.6 (#23) — the new entrants pushed the Anthropic non-Opus-4.7 models down 3 spots each.
