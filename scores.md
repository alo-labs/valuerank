# ValueRank — Scores
**Updated every version | Primary calculation file**

← [README](README.md) · [Raw Data](raw-data.md) · [Methodology](methodology.md)

---

## 7. Normalized Rank Scores

### 7.1 Methodology Recap

For each dimension, models with real data are ranked 1–n (best to worst). Score = `((n − rank) / (n − 1)) × 100`. Missing data = **50⊘**. All columns are fully renormalized for the 12-model v3.0 field. Ties receive the average of their tied ranks.

### 7.2 Complete Normalized Score Matrix (18 dimensions)

| Model | Cost | IF | Term | SWE | SWEPro | LCB | GDP | Spd | τ² | OSW | BC | LCR | HLE | GPQA | MMLU | AIME | Sci | Omni |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gemini 3.1 Pro | **63.6** | 100.0 | **54.5** | 61.1 | 50.0⊘ | **40.0** | **9.1** | 100.0 | 100.0 | 50.0⊘ | **71.4** | 88.9 | 90.9 | 100.0 | **80.0** | 30.0 | 100.0 | 100.0 |
| Kimi K2.6 | **54.5** | 80.0 | **36.4** | 44.4 | **68.8** | **60.0** | **36.4** | **81.8** | 0.0 | 40.0 | **28.6** | 61.1 | 45.5 | 63.6 | 0.0 | 60.0 | 66.7 | **42.9** |
| MiniMax M2.7 | **90.9** | 60.0 | 0.0 | 50.0⊘ | **25.0~** | 50.0⊘ | **27.3** | **40.9** | 45.0 | 50.0⊘ | 50.0⊘ | 44.4 | 9.1 | 27.3 | 50.0⊘ | 50.0⊘ | 44.4 | **71.4** |
| GPT-5.4 | **36.4** | 40.0 | **81.8** | 50.0⊘ | **87.5** | 0.0 | **72.7** | **72.7** | 60.0 | 60.0 | **85.7** | 100.0 | 72.7 | 72.7 | 50.0⊘ | 50.0⊘ | 88.9 | 50.0⊘ |
| Qwen 3.6 Plus | **81.8** | 50.0 | **18.2** | 11.1 | **37.5~** | 50.0⊘ | **18.2** | **54.5** | 20.0 | 50.0⊘ | 50.0⊘ | 61.1 | 18.2 | 54.5 | **60.0** | 50.0⊘ | 0.0 | 50.0⊘ |
| KAT-Coder-Pro-V2 | **100.0** | 30.0 | **90.9** | 27.8 | 50.0⊘ | 50.0⊘ | 0.0 | **90.9** | 70.0 | 50.0⊘ | 50.0⊘ | 33.3 | 0.0 | 9.1 | 50.0⊘ | 50.0⊘ | 11.1 | 50.0⊘ |
| GLM 5.1 | **72.7** | 90.0 | **63.6** | 0.0 | **50.0~** | 50.0⊘ | **45.5** | **40.9** | 80.0 | 50.0⊘ | **0.0~** | 22.2 | 36.4 | 18.2 | **20.0~** | 30.0 | 22.2 | **28.6** |
| Claude Opus 4.7 | **9.1** | 20.0 | **72.7** | 88.9 | 100.0 | 50.0⊘ | **90.9** | **18.2** | 10.0 | 80.0 | **14.3** | 77.8 | 100.0 | 90.9 | **100.0~** | 90.0 | 77.8 | **85.7** |
| GPT-5.5 | **27.3** | **70.0** | 100.0 | **100.0** | **68.8** | **80.0~** | 100.0 | **63.6** | 90.0 | 100.0 | 100.0 | 50.0⊘ | 81.8 | 81.8 | 50.0⊘ | 50.0⊘ | 50.0⊘ | 0.0 |
| Claude Sonnet 4.6 | **18.2** | 10.0 | **9.1** | 27.8 | 50.0⊘ | 50.0⊘ | **81.8** | **27.3** | 30.0 | 0.0 | 50.0⊘ | 11.1 | 27.3 | 36.4 | 50.0⊘ | 0.0 | 33.3 | 50.0⊘ |
| Claude Opus 4.6 | 0.0 | 0.0 | **27.3** | 77.8 | 0.0 | **20.0** | **63.6** | 0.0 | 45.0 | 20.0 | **57.1~** | 0.0 | 63.6 | 0.0 | 50.0⊘ | 90.0 | 55.6 | **57.1** |
| DeepSeek V4-Pro | **45.5** | 50.0⊘ | **45.5†self** | 61.1 | **12.5** | 100.0 | **54.5** | **9.1** | 50.0⊘ | 50.0⊘ | **42.9** | 50.0⊘ | 54.5 | 45.5 | **40.0** | 50.0⊘ | 50.0⊘ | **14.3** |

**⊘** = missing data, assigned neutral score of 50.0. **Bold** = changed or filled from v3.0. **~** = BenchLM/secondary source (probable confidence).

**Key v3.0 dimension normalization notes (carried forward):**
- **IF (n=11):** GPT-5.5 75.9% fills gap → rank 4; GPT-5.5: 50⊘→70.0; GLM shifts 88.9→90.0; Kimi 77.8→80.0.
- **SWE (n=10):** GPT-5.5 88.7% (#1, dagger removed v4.0), DeepSeek 80.6% ties Gemini (rank 4.5). KAT/Sonnet tied (rank 7.5) = 27.8.
- **τ² (n=11):** Gemini 99.3% corrected (#1); GPT-5.5 at #2 (90.0); GLM at #3 (80.0).
- **HLE (n=12):** DeepSeek 37.7% at rank 6; all scores from v2.4 base.
- **GPQA (n=12):** DeepSeek 88.8% at rank 7; existing models shifted.
- **LCB (n=5):** DeepSeek 93.5% at rank 1 (#1 in cohort); Kimi at rank 2 (75.0).

**Key v4.0 dimension normalization notes (new):**
- **Cost (n=11→12):** DeepSeek $1,071.28 fills gap → rank 7/12. Formula n=12: ((12−rank)/11)×100. All 11 existing models shift: KAT unchanged (100.0), others compress upward or downward by 0.9–4.5 pts depending on rank. DeepSeek: 50⊘→45.5 (below neutral).
- **Term (n=11→12):** DeepSeek 67.9%†self fills gap → rank 7/12 (between Gemini 68.5% and Kimi 66.7%). Score = 45.5. All other models shift: GPT-5.5 100.0 unchanged; Gemini 50→54.5; MiniMax 0.0 unchanged.
- **SWEPro (n=5→9):** GLM 58.4%~, Qwen 56.6%~, MiniMax 56.2%~, DeepSeek 55.4% added. New n=9. Kimi/GPT-5.5 (58.6%, tied rank 3.5): 37.5→68.8; GPT-5.4 (rank 2): 75.0→87.5; Qwen: 50⊘→37.5; MiniMax: 50⊘→25.0; DeepSeek: 50⊘→12.5; Opus4.6 (rank 9): 0.0 unchanged.
- **GDP (n=11→12):** DeepSeek 1,554 fills gap → rank 6/12. GPT-5.5 100.0 unchanged; all others compress by 0.9–4.5 pts. DeepSeek: 50⊘→54.5 (above neutral — one positive fill for DeepSeek).
- **Spd (n=11→12):** GPT-5.5 74.7 tok/s fills gap → rank 5/12 (near-tied with GPT-5.4 74.8). DeepSeek corrected 33.5→35.8 (rank 11 unchanged). GPT-5.5: 50⊘→63.6; Qwen compresses 60→54.5; MiniMax/GLM tied: 45→40.9.
- **BC (n=6→8):** Opus4.6 83.7%~ (rank 4) and GLM 68%~ (rank 8/last) added. GPT-5.5 100.0 unchanged; Opus4.7: 0.0→14.3; GLM: 50⊘→0.0 (major drop); Kimi: 20.0→28.6; Gemini: 60.0→71.4.
- **MMLU (n=4→6):** Opus4.7 89.87%~ (rank 1) and GLM 85.8%~ (rank 5) added. Gemini drops 100.0→80.0 (displaced to rank 2); Qwen: 66.7→60.0; DeepSeek: 33.3→40.0; Kimi 0.0 unchanged. Opus4.7: 50⊘→100.0 (major positive).
- **Omni (n=6→8):** Kimi +6 (rank 5) and DeepSeek −10 (rank 7) added. Opus4.7: 80.0→85.7; MiniMax: 60.0→71.4; Opus4.6: 40.0→57.1; Kimi: 50⊘→42.9 (below neutral); DeepSeek: 50⊘→14.3 (well below neutral).

**Key v4.2 dimension normalization notes (new):**
- **LCB (n=5→6):** GPT-5.5 ~91.7%~ fills gap → rank 2/6 (between DeepSeek 93.5% #1 and Kimi 82.6% #3). Score = 80.0~. All models with existing LCB real data shift: DeepSeek rank 1 (100.0, unchanged); GPT-5.5: 50.0⊘→80.0~; Kimi: 75.0→60.0 (rank 2→3); Gemini: 50.0→40.0 (rank 3→4); Opus4.6: 25.0→20.0 (rank 4→5); GPT-5.4: 0.0 unchanged (rank 5→6). The 6 models with ⊘ (MiniMax, Qwen, KAT, GLM, Opus4.7, Sonnet) remain at 50.0⊘.

### 7.3 Cost Score Derivation

Cost ranks (cheapest = rank 1, n=12 real scorers). No ties.

| Model | AA Index Eval Cost ($) | Cost Rank | Score = ((12−rank)/11)×100 |
|---|---|---|---|
| KAT-Coder-Pro-V2 | $73.49 | 1 | **100.0** |
| MiniMax M2.7 | $175.51 | 2 | **90.9** |
| Qwen 3.6 Plus | $482.65 | 3 | **81.8** |
| GLM 5.1 | $543.95 | 4 | **72.7** |
| Gemini 3.1 Pro | $892.28 | 5 | **63.6** |
| Kimi K2.6 | $947.87 | 6 | **54.5** |
| DeepSeek V4-Pro | $1,071.28 | 7 | **45.5** |
| GPT-5.4 | $2,851.01 | 8 | **36.4** |
| GPT-5.5 | $3,357.00 | 9 | **27.3** |
| Claude Sonnet 4.6 | $3,959.36 | 10 | **18.2** |
| Claude Opus 4.7 | $4,811.04 | 11 | **9.1** |
| Claude Opus 4.6 | $4,969.68 | 12 | **0.0** |

> **v3.0→v4.0:** DeepSeek V4-Pro confirms $1,071.28 AA Index eval cost (rank 7/12, between Kimi $947.87 and GPT-5.4 $2,851.01). n expands 11→12. All existing model scores update under the new formula ((12−rank)/11)×100.

---

## 8. Quality-Only Ranking (Unweighted)

Equally weighting all 17 non-cost dimensions (5.88% each) to show pure capability ranking without cost penalty.

| Rank | Model | IF Score | Benchmark Quality‡ | Total Quality |
|---|---|---|---|---|
| 1 | **GPT-5.5** | 70.0 | **72.9~** | **72.7~** |
| 2 | Gemini 3.1 Pro | 100.0 | 70.4 | 72.1 |
| 3 | Claude Opus 4.7 | 20.0 | 71.7 | 68.7 |
| 4 | GPT-5.4 | 40.0 | 65.9 | 64.4 |
| 5 | Kimi K2.6 | 80.0 | 46.1 | 48.0 |
| 6 | DeepSeek V4-Pro | 50.0⊘ | 45.6 | 45.9 |
| 7 | KAT-Coder-Pro-V2 | 30.0 | 42.7 | 41.9 |
| 8 | MiniMax M2.7 | 60.0 | 39.7 | 40.9 |
| 9 | Qwen 3.6 Plus | 50.0 | 37.7 | 38.4 |
| 10 | GLM 5.1 | 90.0 | 34.9 | 38.1 |
| 11 | Claude Opus 4.6 | 0.0 | 39.2 | 36.9 |
| 12 | Claude Sonnet 4.6 | 10.0 | 33.4 | 32.0 |

> **‡** IF Score = raw normalized IFBench score (0–100 scale; ⊘ = 50.0). Benchmark Quality = equal-weighted avg of the other 16 non-cost dims. Total Quality = equal-weighted avg of all 17 non-cost dims. ⊘ on DeepSeek IF/Term/τ²/etc. = neutral-50 in both averages. **~** = includes GPT-5.5 LCB 80.0~ (secondary-source score; see [limitations.md §14.11](limitations.md#1411-external-research-data-conflicts-v42)). The 0.6-pt quality gap between GPT-5.5 (72.7) and Gemini (72.1) falls within the SEAL statistical CI band (§16B) — treat as effectively tied for quality #1.

**v4.2 quality update:** **GPT-5.5 provisionally rises to quality #1** (72.7~) as LCB fills at ~91.7% (rank 2/6, score 80.0, secondary source). Gemini drops to quality #2 (72.1) — its LCB rank compresses from 3/5 to 4/6 as GPT-5.5 inserts above it. The gap is 0.6 pts, within SEAL CI; treat as statistically tied. **Claude Opus 4.7 holds quality #3** (68.7) unchanged. **Kimi drops slightly** (48.9→48.0) as its LCB rank compresses from 2/5 to 3/6 with GPT-5.5 insertion. **GPT-5.5 now leads on 8 of 14 confirmed quality dimensions** (TB 2.0, GDP, OSWorld, BrowseComp, SWE-V, SWEPro tied, τ², LCB~). *(v4.0 note: GPT-5.5 surged to quality #2 as Speed 63.6 and SWEPro 68.8 filled; DeepSeek at quality #6 45.9; GLM at quality #10 38.1 from BrowseComp 0.0 double hit — all unchanged in v4.2.)*

---

## 9. Final Cost-Weighted Ranking

**Weights:** Cost 25%, IF 18%, Term 8%, SWE 7%, SWEPro 4%, LCB 6%, GDP 5%, Spd 5%, τ² 4%, OSW 4%, BC 3%, LCR 2%, HLE 2%, GPQA 2%, MMLU 2%, AIME 1%, Sci 1%, Omni 1%

### Final Weighted Scores

| Main Rank | Model | Cost (25%) | IF (18%) | Quality (57%) | Main Score |
|---|---|---|---|---|---|
| 🥇 1 | **Gemini 3.1 Pro** | 15.9 | 18.0 | 36.1 | **70.0** |
| 🥈 2 | **GPT-5.5** | 6.8 | 12.6 | 47.6~ | **67.0~** |
| 🥉 3 | **KAT-Coder-Pro-V2** | 25.0 | 5.4 | 28.0 | **58.4** |
| 4 | **GLM 5.1** | 18.2 | 16.2 | 22.3 | **56.7** |
| 5 | **MiniMax M2.7** | 22.7 | 10.8 | 20.5 | **54.0** |
| 6 | **Kimi K2.6** | 13.6 | 14.4 | 25.9 | **53.9** |
| 7 | **GPT-5.4** | 9.1 | 7.2 | 36.0 | **52.3** |
| 8 | **Qwen 3.6 Plus** | 20.5 | 9.0 | 19.6 | **49.0** |
| 9 | **DeepSeek V4-Pro** | 11.4 | 9.0 | 27.8 | **48.2** |
| 10 | **Claude Opus 4.7** | 2.3 | 3.6 | 38.4 | **44.3** |
| 11 | **Claude Sonnet 4.6** | 4.6 | 1.8 | 19.2 | **25.5** |
| 12 | **Claude Opus 4.6** | 0.0 | 0.0 | 20.6 | **20.6** |

> **Main:** All 12 models, 18 dimensions. Columns: Cost = norm_cost × 0.25 (max 25.0 pts); IF = norm_IF × 0.18 (max 18.0 pts); Quality = weighted sum of remaining 16 dims × their weights (summing to 57%); Main Score = Cost + IF + Quality. `Final = Σ(normalized_score × weight)`.
> **GPT-5.5 note:** As of v4.2, 3 of 17 quality dimensions remain ⊘ (neutral-50): LCR, AIME, SciCode. LCB provisionally filled at ~91.7%~ (rank 2/6, score 80.0~; secondary source — see [limitations.md §14.11](limitations.md#1411-external-research-data-conflicts-v42)). Speed (63.6) and SWEPro (68.8) confirmed; GPT-5.5 leads or ties on 8 of 14 confirmed quality dimensions; provisional quality #1 (72.7~, pending LCB primary-source verification).
> **DeepSeek V4-Pro note:** As of v4.0, 7 of 18 dimensions remain ⊘: IFBench, τ², OSWorld, RULER, AIME, SciCode, and LCB. Four gap-fills confirmed (Cost 45.5, Term 45.5†self, SWEPro 12.5, Omni 14.3) — all below neutral-50, confirming the downward revision from provisional #8 to #9.

### Score Derivation Detail

| Dim | Wt | Gemini | GPT-5.5 | KAT | GLM | Kimi | MiniMax | GPT-5.4 | Qwen | DeepSeek | Opus4.7 | Sonnet | Opus4.6 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cost | 25% | 15.90 | 6.83 | 25.00 | 18.18 | 13.63 | 22.73 | 9.10 | 20.45 | 11.38 | 2.28 | 4.55 | 0.00 |
| IF | 18% | 18.00 | 12.60 | 5.40 | 16.20 | 14.40 | 10.80 | 7.20 | 9.00 | 9.00 | 3.60 | 1.80 | 0.00 |
| Term | 8% | 4.36 | 8.00 | 7.27 | 5.09 | 2.91 | 0.00 | 6.54 | 1.46 | 3.64 | 5.82 | 0.73 | 2.18 |
| SWE | 7% | 4.28 | 7.00 | 1.95 | 0.00 | 3.11 | 3.50 | 3.50 | 0.78 | 4.28 | 6.22 | 1.95 | 5.45 |
| SWEPro | 4% | 2.00 | 2.75 | 2.00 | 2.00 | 2.75 | 1.00 | 3.50 | 1.50 | 0.50 | 4.00 | 2.00 | 0.00 |
| LCB | 6% | 2.40 | 4.80~ | 3.00 | 3.00 | 3.60 | 3.00 | 0.00 | 3.00 | 6.00 | 3.00 | 3.00 | 1.20 |
| GDP | 5% | 0.46 | 5.00 | 0.00 | 2.28 | 1.82 | 1.37 | 3.64 | 0.91 | 2.73 | 4.55 | 4.09 | 3.18 |
| Spd | 5% | 5.00 | 3.18 | 4.55 | 2.05 | 4.09 | 2.05 | 3.64 | 2.73 | 0.46 | 0.91 | 1.37 | 0.00 |
| τ² | 4% | 4.00 | 3.60 | 2.80 | 3.20 | 0.00 | 1.80 | 2.40 | 0.80 | 2.00 | 0.40 | 1.20 | 1.80 |
| OSW | 4% | 2.00 | 4.00 | 2.00 | 2.00 | 1.60 | 2.00 | 2.40 | 2.00 | 2.00 | 3.20 | 0.00 | 0.80 |
| BC | 3% | 2.14 | 3.00 | 1.50 | 0.00 | 0.86 | 1.50 | 2.57 | 1.50 | 1.29 | 0.43 | 1.50 | 1.71 |
| LCR | 2% | 1.78 | 1.00 | 0.67 | 0.44 | 1.22 | 0.89 | 2.00 | 1.22 | 1.00 | 1.56 | 0.22 | 0.00 |
| HLE | 2% | 1.82 | 1.64 | 0.00 | 0.73 | 0.91 | 0.18 | 1.45 | 0.36 | 1.09 | 2.00 | 0.55 | 1.27 |
| GPQA | 2% | 2.00 | 1.64 | 0.18 | 0.36 | 1.27 | 0.55 | 1.45 | 1.09 | 0.91 | 1.82 | 0.73 | 0.00 |
| MMLU | 2% | 1.60 | 1.00 | 1.00 | 0.40 | 0.00 | 1.00 | 1.00 | 1.20 | 0.80 | 2.00 | 1.00 | 1.00 |
| AIME | 1% | 0.30 | 0.50 | 0.50 | 0.30 | 0.60 | 0.50 | 0.50 | 0.50 | 0.50 | 0.90 | 0.00 | 0.90 |
| Sci | 1% | 1.00 | 0.50 | 0.11 | 0.22 | 0.67 | 0.44 | 0.89 | 0.00 | 0.50 | 0.78 | 0.33 | 0.56 |
| Omni | 1% | 1.00 | 0.00 | 0.50 | 0.29 | 0.43 | 0.71 | 0.50 | 0.50 | 0.14 | 0.86 | 0.50 | 0.57 |
| **Total** | | **70.0** | **67.0~** | **58.4** | **56.7** | **53.9** | **54.0** | **52.3** | **49.0** | **48.2** | **44.3** | **25.5** | **20.6** |

> **v4.0 main shakeup:** Kimi rises #6→#5 (+2.2 pts) as SWEPro (68.8) and GDP fills outweigh term/cost compression. MiniMax falls #5→#6 as SWEPro 25.0 (below neutral) and GDP compression cost 1.0 pts. DeepSeek falls #8→#9 (−2.9 pts): Cost 45.5, Term 45.5, SWEPro 12.5, Omni 14.3 — all four confirmed fills below neutral-50. Qwen rises #9→#8 (+0 pts net but surpasses DeepSeek as DeepSeek falls). GPT-5.5 continues to consolidate quality #2 as Speed (63.6) and SWEPro (68.8) confirm above-neutral scores.
> **v4.2 main shakeup:** **GPT-5.5 score improves 65.2→67.0~ (+1.8 pts)** as LCB fills at ~91.7%~ (secondary source, rank 2/6). **Kimi falls #5→#6** (54.8→53.9, −0.9 pts) — LCB rank compresses from 2 to 3 as GPT-5.5 inserts above it. **MiniMax rises #6→#5** by 0.1-pt margin (54.0 vs Kimi 53.9) — within the SEAL CI "effectively tied" band. **Gemini dips 70.6→70.0** (LCB rank 3→4, −0.6 pts); holds #1 overall. **Opus 4.6: 20.9→20.6** (−0.3 pts). All v4.2 score changes carry ~ and are pending primary-source LCB verification.

---

## 10. Ranking Changes (v1.0 → v2.0 → v2.5 → v3.0 → v4.0)

| Model | v1.0 | v2.0 | v2.1.1 | v2.3 | v2.4 | v2.5 | v3.0 | **v4.0** | v4.0 Score | Net Trend |
|---|---|---|---|---|---|---|---|---|---|---|
| Gemini 3.1 Pro | #1 | #1 | #1 | #2 | #1 | #1 | #1 | **#1** | 70.6 | ↑ Holds #1; all 8 renorm dims favor Gemini net +1.1 pts |
| GPT-5.5 | — | — | #6 | #4 | #8 | #6 | #2 | **#2** | 65.2 | ↑ Speed (63.6) + SWEPro (68.8) confirm quality #2; +1.2 pts |
| KAT-Coder-Pro-V2 | #6 | #4 | #5 | #5 | #3 | #2 | #3 | **#3** | 58.4 | ─ Stable; +0.1 pts as n=12 slightly lifts rank-2 scores |
| GLM 5.1 | #7 | #7 | #7 | #7 | #5 | #3 | #4 | **#4** | 56.7 | ↓ BrowseComp 0.0 (last/8) + MMLU-Pro 20.0 double hit; −1.5 pts |
| Kimi K2.6 | #2 | #2 | #2 | #1 | #2 | #4 | #6 | **#5** | 54.8 | ↑ SWEPro 68.8 + Cost/Term n-expansion; +2.2 pts |
| MiniMax M2.7 | #3 | #3 | #3 | #3 | #4 | #5 | #5 | **#6** | 54.0 | ↓ SWEPro 25.0 (below neutral) + GDP drop; −1.0 pts |
| GPT-5.4 | #4 | #5 | #4 | #6 | #7 | #8 | #7 | **#7** | 52.3 | ↑ SWEPro rank improves (75→87.5 with n=9); +0.2 pts |
| Qwen 3.6 Plus | #5 | #6 | #8 | #8 | #6 | #7 | #9 | **#8** | 49.0 | ↑ Rises as DeepSeek falls past it; own score −0.7 pts |
| DeepSeek V4-Pro | — | — | — | — | — | — | #8 | **#9** | 48.2 | ↓↓ All 4 gap-fills below neutral: Cost 45.5, Term 45.5, SWEPro 12.5, Omni 14.3; −2.9 pts |
| Claude Opus 4.7 | #8 | #8 | #9 | #9 | #9 | #9 | #10 | **#10** | 44.3 | ↑ MMLU-Pro #1 (100.0~) + BC/Omni fills; +1.4 pts |
| Claude Sonnet 4.6 | #9 | #10 | #10 | #10 | #10 | #10 | #11 | **#11** | 25.5 | ─ Minor compression; −0.6 pts |
| Claude Opus 4.6 | #10 | #9 | #11 | #11 | #11 | #11 | #12 | **#12** | 20.9 | ↑ BC 57.1%~ + Omni 57.1%~ fill in above neutral; +0.3 pts |

**v4.2 rank changes (LCB provisional fill, secondary source):** Gemini 70.6→70.0 (−0.6); GPT-5.5 65.2→**67.0~** (+1.8, score only — rank holds #2); Kimi 54.8→53.9, **#5→#6** (−0.9); MiniMax **#6→#5** (54.0, unchanged score); Opus 4.6 20.9→20.6 (−0.3). All ~ pending primary-source LCB verification.
