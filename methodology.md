# ValueRank — Methodology
**Stable reference | Updates only on formula/weight/protocol changes**

← [README](README.md) · [Raw Data](raw-data.md) · [Scores](scores.md)

---

## 3. Methodology

### 3.1 Scoring Formula

All dimensions use rank-based normalization:

```
Normalized Score = ((n − rank) / (n − 1)) × 100
```

Where `n` is the number of models with real data for that dimension. This formula is scale-invariant — percentages, ELO ratings, tokens/second, and composite indices all normalize identically. Rank 1 (best) always scores 100; rank n (worst) always scores 0.

**Missing data:** Models without published results for a dimension receive a neutral score of **50** (midpoint). This neither rewards nor penalizes absent data. Missing values are marked **⊘** throughout.

### 3.2 Final Score Formula

```
Final Score = Σ (Normalized Score × Dimension Weight)
```

Weights are fixed; see §3.4 for rationale.

### 3.3 TTFT Exclusion

Time-to-first-token (TTFT) was evaluated for inclusion in v2.0 but excluded from scoring in both v2.0 and v2.1. Root cause: reasoning-mode models (GPT-5.5 xhigh, Gemini 3.1 Pro think mode) exhibit TTFT values of 100,000–200,000 ms because the metric captures full chain-of-thought latency. Non-reasoning models like Claude Sonnet 4.6 return first tokens in ~1,400 ms. These two populations measure fundamentally different things. Including both in a single scored dimension would penalize reasoning models for being reasoning models. TTFT raw data is preserved in [raw-data.md §6.2](raw-data.md#62-time-to-first-token-ttft--reference-only-not-scored) for reference.

### 3.4 Dimension Weights

| # | Dimension | Abbrev | Weight | Rationale |
|---|---|---|---|---|
| 1 | Cost Efficiency (AA Index Eval Cost) | Cost | **25%** | Dominant production selection factor; total USD to run AA's full benchmark suite (price × actual benchmark token usage). Reduced 28%→25% in v3.0 to accommodate 3 new dimensions. |
| 2 | Reliability — Instruction Following (IFBench) | IF | **18%** | Production systems have machine consumers: parsers that cannot tolerate format failures the way a human reader can. A model that follows 90% of constraints is not "90% as useful" — the 10% failure rate requires catch-and-retry logic, human review, or output degradation, multiplying real operational cost non-linearly. IFBench (58 out-of-domain verifiable constraints, Allen AI, NeurIPS 2025) tests generalization beyond IFEval's fixed 26-constraint set. IFBench is unsaturated at 58–76% for current frontier models, making it a live discriminator where MMLU and HellaSwag have lost power. FireBench (arXiv:2603.04857, 2026) confirms the problem is real: no frontier model exceeds 75% on enterprise IF tasks, and top models show 13–25 pp variance across constraint categories — format compliance may rank 1st while item-ranking tasks rank 5th or 6th. Future versions will incorporate IFEval as a composite (IFEval 65% + IFBench 35%, per BenchLM methodology) when full-cohort IFEval data is available. Reduced 20%→18% in v3.0. |
| 3 | Terminal-Bench 2.0 | Term | **8%** | Primary SE harness benchmark; direct proxy for coding-agent performance. Reduced 9%→8%. |
| 4 | SWE-bench Verified | SWE | **7%** | Real GitHub issue resolution; industry standard for SE agents. Reduced 8%→7%. |
| 5 | SWE-bench Pro *(new v3.0)* | SWEPro | **4%** | Harder single-pass SWE variant; complementary to Verified score. |
| 6 | LiveCodeBench v4 | LCB | **6%** | Contamination-resistant coding; rolling test set. Reduced 7%→6%. |
| 7 | GDPval-AA ELO | GDP | **5%** | Aggregated human preference across 141 models. Unchanged. |
| 8 | Speed (tok/s) | Spd | **5%** | Output throughput; practical for streaming and bulk workloads. Unchanged. |
| 9 | τ²-Bench | τ² | **4%** | Multi-step tool-use reliability; phone/computer agent tasks. Unchanged. |
| 10 | OSWorld | OSW | **4%** | Computer use / GUI agent benchmark. Unchanged. |
| 11 | BrowseComp *(new v3.0)* | BC | **3%** | Deep web research agent; 1,266 hard-to-find information retrieval tasks. |
| 12 | Long-Context Retrieval (RULER) | LCR | **2%** | Needle-in-haystack at 128K+; long-context faithfulness. Reduced 3%→2%. |
| 13 | Humanity's Last Exam (HLE) | HLE | **2%** | Frontier expert knowledge breadth (without-tools, canonical Scale Labs leaderboard). Unchanged. |
| 14 | GPQA Diamond | GPQA | **2%** | Graduate-level science reasoning. Unchanged. |
| 15 | MMLU-Pro *(new v3.0)* | MMLU | **2%** | Graduate-level knowledge breadth; 10-choice enhanced MMLU format. |
| 16 | AIME 2025 | AIME | **1%** | Competition math; reasoning ceiling. Unchanged. |
| 17 | SciCode | Sci | **1%** | Scientific coding (domain-expert tasks). Unchanged. |
| 18 | AA-Omniscience | Omni | **1%** | Hallucination-adjusted accuracy (accuracy% − hallucination_rate%). Unchanged. |
| | **Total** | | **100%** | |

**Weight redistribution v2.5→v3.0:** Added 9% total for 3 new dimensions (SWEPro=4%, BC=3%, MMLU=2%). Offset by reducing: Cost −3%, IF −2%, Term −1%, SWE −1%, LCB −1%, LCR −1%. All other dimensions unchanged. Rationale: proportional reductions from higher-weight dimensions; LCR reduced to 2% given its provisional data footnote (no canonical leaderboard confirmations).

**Framework slots (collected, not yet scored):** BigCodeBench, GAIA Level 3. As of April 25, 2026, no 2026-era frontier models have submitted to these leaderboards in sufficient numbers for activation. Will be re-evaluated in v4.0.

### 3.5 Dimension Categories (BenchLM-Inspired)

Analogous to BenchLM's categorical organization (Agentic / Coding / Reasoning / Knowledge / IF / Multilingual), the 18 dimensions group into five production-relevant clusters. Category weights reflect the sum of included dimension weights.

| Category | Dimensions | Combined Weight | Rationale |
|---|---|---|---|
| **Cost & Efficiency** | Cost, Speed | **30%** | Total financial cost and output throughput — the "price-per-useful-token" axes. Largest combined category by design: production model selection begins with operational economics. |
| **Reliability** | IFBench (Reliability — IF) | **18%** | Machine-consumer interface quality: parsers, APIs, and downstream pipelines that cannot tolerate format failures. Deliberate standalone category — instruction-following is a systems-integration property, not a reasoning property. |
| **Coding & SE Agents** | Terminal-Bench 2.0, SWE-bench Verified, SWE-bench Pro, LiveCodeBench v4 | **25%** | Software engineering task completion across four sub-types: terminal/CLI agents, real-world GitHub issue resolution, hard single-pass code repair, and contamination-resistant coding evaluation. |
| **Agentic Tasks** | GDPval-AA ELO, τ²-Bench, OSWorld, BrowseComp | **16%** | Multi-step autonomous operation beyond pure coding: human preference alignment, tool-use reliability, GUI/desktop automation, and deep web research. |
| **Knowledge & Reasoning** | HLE, GPQA Diamond, MMLU-Pro, AIME 2025, SciCode, RULER/LCR, AA-Omniscience | **11%** | Expert knowledge breadth, scientific reasoning, mathematical ceilings, domain coding, long-context fidelity, and hallucination-calibrated accuracy. Intentionally the lowest-weight category: these dimensions predict performance on novel hard tasks but have the least production-deployment relevance per the 25% cost anchor. |

**Category notes:**
- **ValueRank vs. BenchLM:** BenchLM includes Multilingual and Multimodal as first-class categories; ValueRank omits both because the 12-model cohort lacks systematic multilingual and multimodal benchmark coverage. These will be activated as category dimensions when ≥4 cohort models have published scores on a canonical multilingual benchmark.
- **Reliability as standalone:** BenchLM places IF within a broader evaluation composite at lower relative weight (~6%). ValueRank elevates it to a standalone 18% category — the largest non-cost single dimension — reflecting the production systems argument in §3.4 that machine consumers transform IF failures from inconveniences into operational costs.
- **Cost & Efficiency at 30%:** No other public ranking framework treats cost as a 30% cluster. DigitalApplied's Q2 2026 efficient frontier analysis and AA's Pareto leaderboard both incorporate cost, but neither weights it above quality in a composite.

---

## 16. Methodology Appendix

### 16A. Normalization Examples

**Example 1: IFBench v3.0 (n=11 models with real data, 1 model ⊘)**

Raw scores: Gemini 89.4%, GLM 85.9%, Kimi 82.1%, GPT-5.5 75.9%, MiniMax 75.7%, Qwen 74.2%, GPT-5.4 73.9%, KAT 67.0%, Opus 4.7 52.1%, Sonnet 45.6%, Opus 4.6 40.2%
DeepSeek: ⊘ → 50.0

Ranks (1=best): Gemini=1, GLM=2, Kimi=3, GPT-5.5=4, MiniMax=5, Qwen=6, GPT-5.4=7, KAT=8, Opus 4.7=9, Sonnet=10, Opus 4.6=11
Formula `((n-rank)/(n-1)) × 100` where n=11:
- Gemini: (10/10)×100 = **100.0**
- GLM: (9/10)×100 = **90.0**
- GPT-5.5: (7/10)×100 = **70.0** ← filled from ⊘ in v2.5
- Opus 4.6: (0/10)×100 = **0.0**

**Example 2: Cost v3.0 (n=11 real scorers, DeepSeek ⊘)**

Same as v2.5. KAT-Coder-Pro-V2: rank 1 → (10/10)×100 = **100.0**. Gemini: rank 5 → (6/10)×100 = **60.0**. Opus 4.6: rank 11 → (0/10)×100 = **0.0**. DeepSeek: ⊘ → **50.0⊘**.

**Example 3: SWE-bench Verified v3.0 (n=10 scorers, 2 ties)**

GPT-5.5 (88.7%) rank 1, Opus 4.7 (87.6%) rank 2, Opus 4.6 (80.8%) rank 3, Gemini+DeepSeek (80.6%) tie rank 4.5, Kimi (80.2%) rank 6, KAT+Sonnet (79.6%) tie rank 7.5, Qwen (78.8%) rank 9, GLM (77.8%) rank 10. MiniMax+GPT-5.4 ⊘.
Ties: `(n-avg_rank)/(n-1)×100`: Gemini/DeepSeek = (10-4.5)/9×100 = **61.1**; KAT/Sonnet = (10-7.5)/9×100 = **27.8**.

### 16B. Sensitivity Analysis

**What if cost weight = 15% (quality-forward scenario)?**

| Rank | Model | Score |
|---|---|---|
| 1 | Gemini 3.1 Pro | 72.8 |
| 2 | GPT-5.5 | 67.7 |
| 3 | Claude Opus 4.7 | 61.8 |
| 4 | GPT-5.4 | 56.5 |
| 5 | GLM 5.1 | 55.0 |

At 15% cost weight, GPT-5.5 extends its #2 advantage (quality leads on 5 confirmed agentic dims). Claude Opus 4.7 recovers to #3 as cost penalty ($4,811) shrinks. KAT-Coder-Pro-V2 drops out of top-5 as its quality (#10) becomes the binding constraint at lower cost weight.

**What if cost weight = 40% (cost-extreme scenario)?**

| Rank | Model | Score |
|---|---|---|
| 1 | KAT-Coder-Pro-V2 | 66.1 |
| 2 | Gemini 3.1 Pro | 65.2 |
| 3 | MiniMax M2.7 | 62.8 |
| 4 | GLM 5.1 | 60.8 |
| 5 | Qwen 3.6 Plus | 57.0 |

At 40% cost weight, KAT overtakes Gemini. MiniMax rises to #3. GPT-5.5 drops to #8 (cost 40% weight at 30.0 score = 12.0 pts). Claude Opus 4.6 collapses to #12 (cost score 0.0 at 40% = structurally fatal).

**What if Reliability (IFBench) weight = 10% (reduced from 18%)?**

Freed 8% redistributed proportionally to the 16 remaining quality dimensions (Quality: 57%→65%). Cost fixed at 25%.

| Rank | Model | Score |
|---|---|---|
| 1 | Gemini 3.1 Pro | 67.8 |
| 2 | GPT-5.5 | 66.1 |
| 3 | KAT-Coder-Pro-V2 | 60.0 |
| 4 | GPT-5.4 | 54.1 |
| 5 | GLM 5.1 | 52.7 |

At 10% Reliability weight, GPT-5.4 rises from #7 to #4 — its overall quality (64.4) is strong but its IFBench normalized score (40.0) is weak; lower IF weight rewards the former. GLM drops from #4 to #5 as its IFBench advantage (90.0 normalized) matters less. KAT holds #3 — it is IFBench-weak (30.0 normalized) but cost-dominant (100.0); the cost weight of 25% keeps it well above lower-cost competitors. Gemini and GPT-5.5 remain #1 and #2 regardless of IF weight: Gemini leads IFBench (100.0), GPT-5.5 leads the overall quality distribution.

**What if Reliability (IFBench) weight = 25% (increased from 18%)?**

Added 7% sourced proportionally from the 16 remaining quality dimensions (Quality: 57%→50%). Cost fixed at 25%.

| Rank | Model | Score |
|---|---|---|
| 1 | Gemini 3.1 Pro | 73.1 |
| 2 | GPT-5.5 | 64.5 |
| 3 | GLM 5.1 | 60.3 |
| 4 | KAT-Coder-Pro-V2 | 57.1 |
| 5 | Kimi K2.6 | 57.1 |

At 25% Reliability weight, GLM 5.1 rises from #4 to #3 (IFBench #2 at 90.0 normalized contributes 22.5 pts). Kimi enters the top 5 (IFBench #3 at 80.0 → 20.0 pts at 25% weight). GPT-5.4 drops below top-5 (IFBench 40.0 normalized → only 10.0 pts). Claude Opus 4.7 drops to #10 — its IFBench weakness (52.1% raw, 20.0 normalized) inflicts its largest penalty at 25% weight, offsetting its strong benchmark quality elsewhere. A 25% Reliability weight is defensible for deployment contexts with strictly machine-consumer outputs (APIs, parsers, structured data pipelines) where format failures have zero operational tolerance.

### Statistical Confidence and Rank Uncertainty

The rank-based normalization formula treats all rank separations as equivalent: the gap between rank 1 and rank 2 is scored identically to the gap between rank 6 and rank 7, regardless of the size of the underlying score difference. This is a deliberate choice for scale-invariance (§3.1), but it has a known limitation: **adjacent ranks may be statistically indistinguishable** on the underlying benchmark.

SEAL Leaderboards (Scale Labs) operationalizes this directly: their statistical rank is computed as the count of models that are **statistically significantly better at 95% CI** + 1, rather than the raw ordinal position. Under SEAL methodology, two models with overlapping confidence intervals receive the same statistical rank even when their point estimates differ. In the current ValueRank cohort, this distinction matters most for:

- **IFBench (n=11):** Frontier models cluster at 73–90%. Kimi (82.1%) and GPT-5.5 (75.9%) are raw ranks 3 and 4, but the ~6 pp gap may fall within sampling variability for a 58-item benchmark.
- **SWE-bench Pro (n=9):** Five models cluster at 55.4–58.6% (DeepSeek, MiniMax, Qwen, GLM, Kimi). The 3.2 pp spread across 5 models likely yields multiple statistical ties under 95% CI testing.
- **HLE and GPQA Diamond:** Score ranges are wide (HLE: 12.7%–46.9%; GPQA: 84.0%–94.3%), so adjacent-rank uncertainty is lower for these dimensions.

**Practical implication:** ValueRank's rank-based scores are point estimates. Final composite scores within 2–3 points of each other (e.g., Kimi 54.8 vs. MiniMax 54.0 vs. GPT-5.4 52.3) should be treated as effectively tied, pending statistical significance analysis on individual contributing dimensions. The cost and IF weight sensitivity analyses above provide a partial guard: models that consistently appear in the top positions across multiple weight scenarios have more robust rankings than models that appear in only one scenario.

### 16C. Adding a New Model (Maintenance Protocol)

When a new model is released:

1. **Collect all 18 dimension values** — use official publications, then established third-party evaluators (Artificial Analysis, LMSYS, alo-exp leaderboards). Mark any missing as ⊘.
2. **Recompute all ranks** — every dimension with real data for the new model requires full reranking of ALL models in that dimension. Do not preserve old ranks.
3. **Apply normalization formula** using the new `n` (count of models with real data per dimension).
4. **Recalculate all final scores** — renormalization changes every model's score, not just the new arrival's.
5. **Update Ranking Changes table** — document Δ vs previous version for every model.
6. **Tag version** — increment minor version (e.g., v3.0 → v3.1) for model additions; increment major version for dimension additions or weight changes.
7. **Flag provisional** — mark models with >6 missing dimensions as "provisional ranking" in the Executive Summary.

### 16D. Dimension Activation Protocol

Reserved dimensions (BigCodeBench, GAIA Level 3) activate when:
- ≥4 models in the current inventory have published scores
- Scores come from the primary leaderboard (not secondary reports)
- At least one model in the top-3 of the current ranking has a score

When activated: increment to next major version, rerun full normalization including new dimension weight (determined at activation time), update all profiles and strategic insights.

### 16E. Benchmark Retirement Protocol

A dimension may be retired if:
- The primary leaderboard ceases maintenance for >12 months
- Strong evidence of widespread test-set leakage across ≥5 models emerges
- A successor benchmark explicitly replaces it

Retirement requires: remove from scoring, mark as "retired" in the benchmark reference index, document rationale in changelog, do NOT retroactively recalculate historical versions.

### 16F. Scheduled Review Cadence

| Trigger | Action |
|---|---|
| New frontier model launch | Add to inventory within 7 days; publish next minor version within 14 days |
| Major benchmark update | Evaluate for dimension replacement; publish impact analysis |
| Quarterly | Full data refresh on all 18 dimensions for all models |
| Semi-annual | Weight review — validate 25% cost weight against production survey data |

### 16G. v3.0 Research Sources

Key sources used for v3.0 data updates (from deep-research pipeline, April 25, 2026):
- Artificial Analysis Kimi K2.6 article (GDPval 1,520 confirmed)
- Digital Applied / AA τ²-Bench leaderboard (Gemini 99.3% confirmed)
- OpenAI GPT-5.5 technical card, Harvey research preview, designforonline.com (IFBench 75.9% confirmed)
- VentureBeat, BuildFastWithAI (DeepSeek V4-Pro SWE-bench 80.6% confirmed)
- BuildFastWithAI, OfficeChai (DeepSeek V4-Pro LCB 93.5% confirmed)
- Artificial Analysis (DeepSeek V4-Pro Speed 33.5 tok/s confirmed)
- Scale Labs leaderboard, agi.safe.ai (HLE methodology resolved: without-tools canonical)
- BenchLM, Vellum, multiple sources (BrowseComp scores for 6 models)
- Scale Labs SWE-bench Pro leaderboard, marc0.dev (SWE-Pro scores for 5 models)
- Artificial Analysis MMLU-Pro, Kaggle MMLU-Pro leaderboard (MMLU-Pro scores for 4 models)

### 16H. v4.0 Research Sources

Key sources used for v4.0 gap-fill updates (from ultradeep research pipeline, April 25, 2026):
- Artificial Analysis AA Index Eval Cost leaderboard (DeepSeek V4-Pro $1,071.28 confirmed; GPT-5.5 Speed 74.7 tok/s confirmed; DeepSeek Speed corrected 33.5→35.8 tok/s)
- DeepSeek V4-Pro official model card / self-reported benchmarks (TB 2.0 67.9%†self)
- Scale Labs SWE-bench Pro leaderboard (SWEPro fills: GLM 58.4%~, Qwen 56.6%~, MiniMax 56.2%~, DeepSeek 55.4%; n expanded 5→9)
- Artificial Analysis GDPval leaderboard (DeepSeek V4-Pro ELO 1,554 confirmed; n expanded 11→12)
- BenchLM / llm-stats.com/benchmarks/browsecomp (BrowseComp fills: Opus 4.6 83.7%~, GLM 68%~; n expanded 6→8)
- Artificial Analysis MMLU-Pro leaderboard (MMLU-Pro fills: Opus 4.7 89.87%~, GLM 85.8%~; n expanded 4→6)
- Artificial Analysis Omniscience leaderboard (Omni fills: Kimi +6 = 45%−39%, DeepSeek −10 = 84%−94%; n expanded 6→8)
- swebench.com canonical leaderboard (GPT-5.5 88.7% confirmed; † removed)

### 16I. Framework Philosophy: ValueRank vs. HELM

**HELM (Holistic Evaluation of Language Models, Stanford CRFM, 2022)** is the most prominent academic antecedent to multi-dimensional LLM evaluation. HELM evaluates models across 7 metrics — accuracy, calibration, robustness, fairness, bias, toxicity, and efficiency — over 16 diverse scenarios. Its defining design decision is to **refuse to produce a single composite score.** HELM explicitly holds that "no single number can capture the full picture" of model behavior, and that collapsing dimensions into a composite risks masking performance variations that matter for specific use cases.

ValueRank deliberately departs from this stance on two dimensions:

**1. Integration over parallelism.** HELM reports 7 metrics per scenario as parallel columns; practitioners must perform their own weighting. ValueRank argues that leaving integration to the practitioner does not eliminate implicit weighting — it just makes the weighting invisible and inconsistent. A practitioner who mentally weights cost at ~25% when selecting a model is making the same judgment ValueRank makes explicitly. The difference is transparency and reproducibility: explicit weights can be challenged, debated, and adjusted via the sensitivity analysis in §16B; implicit weights cannot.

**2. Financial cost over computational cost.** HELM's efficiency metric measures computational resource requirements (tokens generated, latency, memory), grounded in a 2022 context where the relevant cost question was GPU budget. ValueRank uses AA Eval Cost (total USD per benchmark run) as the primary cost signal, reflecting the 2025–2026 reality where frontier models are API-accessed and the relevant cost question is dollar spend per task. HELM's calibration metric (confidence alignment with correctness) maps directly to ValueRank's AA-Omniscience dimension (accuracy% − hallucination_rate%). HELM's robustness metric (performance under input perturbation) maps philosophically to ValueRank's IFBench Reliability dimension (performance under novel constraint variation).

**Where HELM's philosophy prevails in ValueRank:** The quality-only ranking (§8) and sensitivity analysis (§16B) are ValueRank's concession to HELM's point. §8 strips out cost entirely to show pure capability rankings, and §16B shows how rankings shift at alternative cost weights (15% and 40%). These sections allow practitioners who disagree with the 25% cost weight to recalibrate without abandoning the framework.

**Where ValueRank diverges:** For production deployment decisions — the primary use case of this document — a single ranked output is more actionable than a parallel multi-metric table. The Pareto frontier analysis in [insights.md §12.6](insights.md#126-pareto-frontier-analysis--quality--cost--speed) shows the consequence of HELM's approach applied to our three primary axes: it yields only two rational model choices, leaving 10 of 12 models with no clear positioning. A weighted composite resolves this by encoding the tradeoff explicitly.

### 16J. v4.1 Methodology Sources

Key sources informing v4.1 methodology additions (from ultradeep research pipeline, April 25–26, 2026):
- Allen AI IFBench GitHub repo + Artificial Analysis IFBench leaderboard (IFBench 58-constraint design; frontier scores 58–76%)
- FireBench paper arXiv:2603.04857 (enterprise IF: best model 74.0%; 13–25 pp category variance)
- BenchLM.ai composite IF methodology (IFEval 65% + IFBench 35% rationale)
- arXiv:2511.23455 "Price of Progress" (per-token vs. task-level cost; reasoning token inflation)
- DigitalApplied Q2 2026 Efficient Frontier analysis (Pareto methodology: quality × cost × speed)
- Liang et al. 2022 "Holistic Evaluation of Language Models" arXiv:2211.09110 (HELM 7-metric framework; multi-metric vs. composite philosophy)
