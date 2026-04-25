# ValueRank — Strategic Insights & Use Cases
**Updated per version**

← [README](README.md) · [Profiles](profiles.md) · [Limitations](limitations.md)

---

## 12. Strategic Insights

### 12.1 GPT-5.5 Confirmed as Quality #2 — Gap Narrows on Gemini

v4.0 confirms two more GPT-5.5 gaps: Speed at 74.7 tok/s (rank 5/12, score 63.6) and SWEPro at 68.8 (tied rank 3.5/9 with Kimi). With these fills, GPT-5.5 now holds confirmed #1 on 5 agentic dimensions (TB 2.0, GDP, OSWorld, BrowseComp, SWE-bench Verified) and quality #2 overall (70.9 pts). τ²-Bench is #2 (98.0% vs Gemini's 99.3%). The SWE-bench Verified dagger is removed — confirmed on canonical swebench.com.

**v4.2 update:** Gemini leads GPT-5.5 by 3.0~ pts (70.0 vs. 67.0~) after provisional LCB fill at ~91.7%~. GPT-5.5 now has 3 ⊘ dimensions (LCR, AIME, SciCode). The LCB fill adds +1.8 pts and narrows the gap from 5.4 pts to 3.0 pts — but is from a secondary source and pending LCB leaderboard confirmation (see [limitations.md §14.11](limitations.md#1411-external-research-data-conflicts-v42)). Gemini's near-complete 17/18 data profile means it cannot be displaced by surprise real data; its overall #1 lead is structural even if quality #1 is provisionally tied.

### 12.2 DeepSeek V4-Pro: The Gap-Fill Surprise

**The central v4.0 finding is that DeepSeek's neutral-50 provisional score was too optimistic.** All four confirmed gap-fills came in below neutral: Cost 45.5 (not cheap), TB 2.0 67.9%†self (mid-tier), SWEPro 55.4% (rank 8/9, second-worst in cohort), Omni −10 (84% accuracy vs. 94% hallucination rate). The net effect: −2.9 pts, dropping DeepSeek from #8 to #9.

This is a data lesson for provisional-model scoring: a composite AI Intelligence Index score of 52 (frontier parity) does not uniformly distribute across 18 dimensions. DeepSeek's gap-fills reveal a model strong on LCB (93.5%, #1) and SWE-bench Verified (80.6%) but surprisingly weak on structured code repair (SWEPro last-quintile) and hallucination control (94% rate). Its one positive fill — GDPval ELO 1,554 — confirms human preference quality above the open-weight median.

LCB dominance (93.5%) still establishes DeepSeek as the open-source coding champion for competition-programming tasks. At $1.74/$3.48 per MTok with a 1M context window, the value proposition is strongest for LCB-type batch coding workloads.

### 12.3 Coverage Expansion Sharpens Discrimination

v4.0 significantly expands coverage on three dimensions:

- **SWE-bench Pro** (5→9 models): Now covers 75% of the cohort. Opus 4.7 leads at 64.3% — a 5.2-point gap to #2 GPT-5.4 (59.1%). The expanded cohort confirms SWEPro is harder than SWE-bench Verified: scores are more spread out and DeepSeek (55.4%) is decisively below Kimi (58.6%).
- **BrowseComp** (6→8 models): Opus 4.6 (83.7%~) and GLM (68%~) added. GLM's last-place finish (0.0 normalized) is the most significant new data point — BrowseComp is GLM's structural blind spot.
- **MMLU-Pro** (4→6 models): Opus 4.7 (89.87%~) enters at rank 1, displacing Gemini from the MMLU-Pro lead. This is the largest single positive fill in v4.0 — Opus 4.7 gains +2.0 pts (100.0 × 2% weight) vs. neutral-50.

### 12.4 Kimi K2.6 Solidifies #5 — The SWEPro Renormalization Effect

With SWEPro n expanding from 5→9, Kimi's 58.6% improves in rank (from tied 3.5/5 to tied 3.5/9 — but score goes from 37.5 to 68.8 as the denominator grows). This +1.25 pt gain at 4% weight is the single largest per-dimension gain in v4.0 for any model. Combined with Cost score improvement (+1.13 pts at 25% weight), Kimi rises from #6 to #5. The τ²-Bench weakness (0.0, last in field) caps further rise.

### 12.5 The Anthropic Cost Structure Remains the Dominant Constraint

Under the AA Index Eval Cost methodology, all three Anthropic frontier models (Sonnet $3,959, Opus 4.7 $4,811, Opus 4.6 $4,970) remain in the top-4 most expensive to run. At 25% cost weight, Claude Opus 4.7's cost score (9.1) contributes only 2.3 pts vs. Gemini's 15.9 pts — a 13.6 pt cost disadvantage that even quality #3 (68.7 pts) cannot overcome. Opus 4.7 scores 44.3 overall vs. Gemini's 70.6 — a 26-pt gap driven almost entirely by the cost dimension. Teams running cost-unconstrained pipelines where SWEPro or HLE performance matters most should consider Opus 4.7; all production workloads face the structural cost ceiling.

### 12.6 Pareto Frontier Analysis — Quality × Cost × Speed

The main ranking integrates cost, reliability, and quality into a single composite score. A complementary view applies strict Pareto dominance across three independent axes: **quality-only score** ([scores.md §8](scores.md#8-quality-only-ranking-unweighted), equal-weight average of all 17 non-cost dimensions), **AA Eval Cost** (lower is better), and **Speed** (tok/s, higher is better). A model is Pareto-optimal if no other model is simultaneously at least as good on all three axes with strict improvement on at least one.

| Model | Quality Score | AA Eval Cost | Speed (tok/s) | Pareto Status |
|---|---|---|---|---|
| **Gemini 3.1 Pro** | **72.1** | $892.28 | **128.0** | **✓ Frontier** |
| **GPT-5.5** | **72.7~** | $3,357.00 | 74.7 | **✓~ Frontier (provisional)** — quality 72.7~ > Gemini's 72.1; Gemini no longer dominates all three axes |
| Claude Opus 4.7 | 68.7 | $4,811.04 | 42.0 | ✗ Dominated (Gemini) |
| GPT-5.4 | 64.4 | $2,851.01 | 74.8 | ✗ Dominated (Gemini) |
| Kimi K2.6 | 48.0 | $947.87 | 100.4 | ✗ Dominated (Gemini: $892 < $948, 128 > 100.4, 72.1 > 48.0) |
| DeepSeek V4-Pro | 45.9 | $1,071.28 | 35.8 | ✗ Dominated (Gemini) |
| **KAT-Coder-Pro-V2** | 41.9 | **$73.49** | 113.5 | **✓ Frontier** |
| MiniMax M2.7 | 40.9 | $175.51 | 49.0 | ✗ Dominated (KAT: higher quality, cheaper, faster) |
| Qwen 3.6 Plus | 38.4 | $482.65 | 53.0 | ✗ Dominated (KAT) |
| GLM 5.1 | 38.1 | $543.95 | 49.0 | ✗ Dominated (KAT) |
| Claude Opus 4.6 | 36.9 | $4,969.68 | 18.2 | ✗ Dominated (GLM and many others) |
| Claude Sonnet 4.6 | 32.0 | $3,959.36 | 46.0 | ✗ Dominated (Qwen: higher quality, much cheaper, faster) |

**v4.2 update: Provisionally 3 Pareto-optimal models.** With GPT-5.5's quality provisionally rising to 72.7~ (LCB 91.7%~, secondary source), GPT-5.5 now has *higher* quality than Gemini (72.1). Gemini can no longer dominate GPT-5.5 on all three axes — it wins cost and speed but loses quality by 0.6 pts. GPT-5.5 therefore becomes a provisional Pareto frontier member (highest quality, no model beats it on quality while also being cheaper and faster). The frontier expands from 2 to 3~: Gemini (quality-speed-cost balance), GPT-5.5~ (quality apex), KAT (cost floor). **However, the 0.6-pt quality gap is within the SEAL CI band ([methodology.md §16B](methodology.md#statistical-confidence-and-rank-uncertainty)) and the data is from a secondary source — pending LCB primary-source confirmation, revert to the v4.0 Pareto result (2 frontier models: Gemini + KAT).** KAT-Coder-Pro-V2 holds the budget frontier unchanged.

**Implication:** The Pareto analysis sharpens the main ranking's insight. The composite score resolves the quality-cost-speed tradeoff by weighting cost at 25%. The Pareto view shows that the same tradeoff, when left unresolved, yields (confirmed) two rational choices or (provisional v4.2) three: Gemini 3.1 Pro (quality-speed-cost balance), KAT-Coder-Pro-V2 (sole occupant of the cost frontier), and provisionally GPT-5.5~ (quality apex if LCB 91.7%~ is confirmed). The confirmed result is unchanged: every model except Gemini and KAT is dominated on all three confirmed-data axes simultaneously.

### 12.7 Cost-of-Pass — Expected Cost Per Correct Output

The Erol et al. 2025 framework (arXiv:2504.13359) defines **cost-of-pass** as the expected monetary cost to obtain one correct answer: `cost_of_pass = (cost per attempt) / (pass_rate)`. Applied to the AA Eval Cost data (§4.1) and benchmark pass rates (§5.1), this metric answers a question the main composite cannot: not "which model scores best relative to its cost?" but "how much does one correct output actually cost?"

**Methodology:** AA Eval Cost captures the total USD to run the full benchmark suite on each model. Treating it as a proxy for cost-per-run across a fixed task set and dividing by benchmark pass rate yields a relative cost-of-correct-output index. Relative comparisons across models on the same benchmark are valid; cross-benchmark comparisons are not (different tasks, different difficulty distributions).

**SWE-bench Verified (10 models with both cost and pass rate data):**

| Model | AA Eval Cost | SWE-V Pass Rate | Cost-of-Pass |
|---|---|---|---|
| **KAT-Coder-Pro-V2** | $73.49 | 79.6% | **$92** |
| Qwen 3.6 Plus | $482.65 | 78.8% | $613 |
| GLM 5.1 | $543.95 | 77.8% | $699 |
| Gemini 3.1 Pro | $892.28 | 80.6% | $1,107 |
| Kimi K2.6 | $947.87 | 80.2% | $1,182 |
| DeepSeek V4-Pro | $1,071.28 | 80.6% | $1,329 |
| GPT-5.5 | $3,357.00 | 88.7% | $3,786 |
| Claude Sonnet 4.6 | $3,959.36 | 79.6% | $4,973 |
| Claude Opus 4.7 | $4,811.04 | 87.6% | $5,492 |
| Claude Opus 4.6 | $4,969.68 | 80.8% | $6,151 |
| MiniMax M2.7 | $175.51 | ⊘ | — |
| GPT-5.4 | $2,851.01 | ⊘ | — |

**Terminal-Bench 2.0 (all 12 models):**

| Model | AA Eval Cost | TB 2.0 Pass Rate | Cost-of-Pass |
|---|---|---|---|
| **KAT-Coder-Pro-V2** | $73.49 | 76.2% | **$96** |
| MiniMax M2.7 | $175.51 | 57.0% | $308 |
| Qwen 3.6 Plus | $482.65 | 61.6% | $783 |
| GLM 5.1 | $543.95 | 69.0% | $788 |
| Gemini 3.1 Pro | $892.28 | 68.5% | $1,303 |
| Kimi K2.6 | $947.87 | 66.7% | $1,421 |
| DeepSeek V4-Pro†self | $1,071.28 | 67.9% | $1,578 |
| GPT-5.4 | $2,851.01 | 75.1% | $3,797 |
| GPT-5.5 | $3,357.00 | 82.7% | $4,059 |
| Claude Sonnet 4.6 | $3,959.36 | 59.1% | $6,700 |
| Claude Opus 4.7 | $4,811.04 | 69.4% | $6,933 |
| Claude Opus 4.6 | $4,969.68 | 65.4% | $7,598 |

†self = DeepSeek TB 2.0 is self-reported; treat cost-of-pass as provisional.

**Key findings:**
1. **KAT's cost advantage compounds.** At SWE-bench Verified, KAT's $92 cost-of-pass is 12× cheaper than Gemini ($1,107), 41× cheaper than GPT-5.5 ($3,786), and 67× cheaper than Claude Opus 4.6 ($6,151) — despite KAT's pass rate (79.6%) being near-equivalent to Gemini's (80.6%). The cost difference is entirely driven by eval cost ($73 vs $892), not quality.
2. **High pass rates do not offset high prices.** GPT-5.5's 88.7% SWE-V pass rate (best in field) still yields a $3,786 cost-of-pass — 3.4× Gemini's $1,107. Claude Opus 4.7's 87.6% SWE-V pass rate produces a $5,492 cost-of-pass because its $4,811 base cost cannot be overcome by any realistic pass rate advantage.
3. **Task-type specialization matters.** For Terminal-Bench specifically, MiniMax M2.7 ($308) is the second-cheapest model after KAT — despite its modest 57.0% pass rate. Its $175.51 eval cost dominates. Qwen and GLM cluster at $783–788, making them the natural mid-range choice for terminal workloads. This confirms the Erol et al. finding that cost-of-pass task-type specialization is real: the optimal model for SWE tasks (KAT, Gemini, Kimi) differs from the price-performance leader for terminal tasks (KAT, MiniMax).
4. **The 25% cost weight is validated by cost-of-pass math.** A 1-percentage-point difference in pass rate is worth approximately $50–$150 in cost-of-pass for budget models and $3,000–$6,000 for ultra-premium models. The cost dimension carries more dollar-value information per weight point than any single quality benchmark.

---

## 13. Use Case Recommendations

| Use Case | Primary Choice | Budget Alternative | Notes |
|---|---|---|---|
| Production SE pipeline (cost-first) | **Gemini 3.1 Pro** | GLM 5.1 | #1 overall at 70.0 pts; broadest coverage; $892 eval cost |
| Broadest-coverage production choice | **Gemini 3.1 Pro** | GPT-5.5 | Real data on 17/18 dims; #1 IFBench, Speed, τ², GPQA, Sci, Omni |
| Minimum eval-cost processing | **KAT-Coder-Pro-V2** | MiniMax M2.7 | $73.49 eval cost (#1) vs $175.51 (#2) |
| High-volume batch processing | **KAT-Coder-Pro-V2** | MiniMax M2.7 | KAT: $73.49 + TB 2.0 #2; MiniMax: $175.51 + IFBench #5 |
| Coding specialist (LCB / competition) | **DeepSeek V4-Pro** | GPT-5.5~ / Kimi K2.6 | LCB #1 (93.5%) vs #2~ GPT-5.5 (91.7%~, provisional) vs #3 Kimi (82.6%); DeepSeek + Kimi are open-source |
| Coding specialist (terminal/CLI) | **GPT-5.5** | KAT-Coder-Pro-V2 | TB 2.0: 82.7% (#1) vs 76.2% (#2) |
| Computer-use / GUI automation | **GPT-5.5** | Claude Opus 4.7 | OSWorld #1 (78.7%) by large margin |
| Multi-step agentic tasks (τ²) | **Gemini 3.1 Pro** | GPT-5.5 | τ²: 99.3% (#1) vs 98.0% (#2) — Gemini now leads |
| SWE-bench / GitHub issue resolution | **GPT-5.5** | Claude Opus 4.7 | SWE-V: 88.7% (#1, confirmed) vs 87.6% (#2, confirmed) |
| SWE-bench Pro / hard code repair | **Claude Opus 4.7** | GPT-5.4 | SWE-Pro: 64.3% (#1) — 5.2% lead over GPT-5.4 (59.1%) |
| Deep web research / BrowseComp | **GPT-5.5** | GPT-5.4 | BrowseComp: 90.1% (#1) vs 89.3% (#2) |
| Long-context retrieval (128K+) | **GPT-5.4** | Gemini 3.1 Pro | RULER: 97.8% vs 94.2% |
| Competition math / reasoning ceiling | **Claude Opus 4.7 / 4.6** | Kimi K2.6 | AIME: 99.8% (tied Opus) vs 96.1% (Kimi) |
| Graduate-level knowledge (MMLU-Pro) | **Claude Opus 4.7** | Gemini 3.1 Pro | MMLU-Pro: 89.87%~ (#1, v4.0 new) vs 89.8% (#2) |
| Instruction-following reliability | **Gemini 3.1 Pro** | GLM 5.1 | IFBench: 89.4% (#1) vs 85.9% (#2) |
| Fast streaming / real-time | **Gemini 3.1 Pro** | KAT-Coder-Pro-V2 | 128.0 tok/s (#1) vs 113.5 tok/s (#2) |
| Open-source / on-premise frontier | **DeepSeek V4-Pro** | Kimi K2.6 | LCB #1, Apache 2.0, 1M context, $1.74/MTok |
| Highest quality, cost unconstrained | **GPT-5.5** | Claude Opus 4.7 | 5 agentic dim leads (TB 2.0, GDP, OSWorld, BrowseComp, SWE-V); Opus 4.7 quality #3 (68.7); GPT-5.5 quality #2 (70.9) |
| Expert knowledge / HLE tasks | **Claude Opus 4.7** | Gemini 3.1 Pro | HLE #1 (46.9%) vs #2 (44.7%); MMLU-Pro #1 (89.87%~) |
| Mid-range instruction + agentic | **GLM 5.1** | Qwen 3.6 Plus | #4 overall (56.7); $544 eval cost; IFBench #2 + τ² #3 |
