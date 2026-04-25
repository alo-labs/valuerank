# ValueRank — Limitations, Gaps & Benchmark Reference
**Updated per version**

← [README](README.md) · [Insights](insights.md) · [Methodology](methodology.md)

---

## 14. Limitations & Known Gaps

### 14.1 Data Freshness

**v5.0 new models (April 26, 2026):**
- **Amazon Nova Pro:** 17 of 18 dims ⊘. Only Cost ($200.98) confirmed. All quality scores neutral-50. Highest data-gap count in the cohort.
- **Gemma 3 27B:** 16 of 18 dims ⊘. Cost ($0.00 free tier) and Speed (24.6 tok/s) confirmed; GPQA (42.4%) confirmed. All other dims ⊘.
- **Phi-4:** 16 of 18 dims ⊘. Cost ($4.27) and Speed (34.2 tok/s) confirmed. All quality dims ⊘ including GPQA.
- **Llama 4 Scout:** 8 of 18 dims confirmed (Cost, IF, Speed, LCB~, HLE, GPQA, MMLU, SciCode). 10 remain ⊘. All LCB provisional (~, version ambiguity).
- **Llama 4 Maverick:** 9 of 18 dims confirmed (Cost, IF, Speed, LCB~, HLE, GPQA, MMLU, SciCode; + AA Intelligence Index ref). 9 remain ⊘.
- **Mistral Large 3:** 4 of 18 dims confirmed/scored (Cost, Speed, LCB~, GPQA). 14 remain ⊘. LCB is provisional (~).
- **Grok 3:** 4 of 18 dims confirmed/scored (Cost, Speed, LCB~, GPQA~). 14 remain ⊘. Both LCB and GPQA are provisional (~) and may reflect Grok 3 Think mode.
- **o3-mini (high):** 9 of 18 dims confirmed (Cost, IF, Term, LCB~, Speed, τ²~, HLE, GPQA, MMLU, AIME, SciCode — actually 11). 7 remain ⊘. τ² and LCB are provisional (~).

**Existing model gaps (carried from v4.3):**
- **DeepSeek V4-Pro:** 5 dims still ⊘: IFBench, τ²-Bench, OSWorld, RULER, AIME, SciCode (LCB now confirmed at 93.5%).
- **GPT-5.5:** 4 dims ⊘: LCR, AIME, SciCode, LCB (not in pool — reverted from v4.2 provisional fill).
- **Gemini 3.1 Pro:** OSWorld confirmed not published by Google as of April 26, 2026.
- All other data sourced from official publications and established leaderboards as of April 26, 2026.

### 14.2 GPT-5.5 SWE-bench Verified — Confirmed

The 88.7%† provisional value from v3.0 is now confirmed on the canonical swebench.com leaderboard. The dagger (†) marker is removed in v4.0. GPT-5.5 is the confirmed #1 on SWE-bench Verified as of April 25, 2026.

### 14.3 Benchmark Contamination Risk

LiveCodeBench v4 and τ²-Bench use rolling test sets specifically to address contamination, but older benchmarks (GPQA, SWE-bench) may have varying contamination levels across models depending on training cutoff and data curation practices.

### 14.4 Mode Selection Ambiguity

Several models offer multiple reasoning modes. Published benchmark scores typically reflect the best available mode. Rankings may not reflect the model's behavior at its production-default mode.

### 14.5 GPT-5.5 AA-Omniscience

The 86% hallucination rate driving the −29 raw Omniscience score comes from early independent evaluations specifically targeting GPT-5.5's xhigh reasoning mode. At standard or high reasoning modes, both accuracy and hallucination rates would differ significantly.

### 14.6 GPT-5.4 AIME Conflict

LayerLens independent testing: 16.67%. Multiple secondary sources attribute 100% performance to GPT-5.4 (possibly misattributed from GPT-5.2 xhigh). Unresolvable with current data. GPT-5.4 receives ⊘=50 on AIME 2025.

### 14.7 Dimension Coverage Status (v5.0)

| Dimension | v4.3 Coverage | v5.0 Coverage | Notes |
|---|---|---|---|
| Cost | 12/12 (100%) | 20/20 (100%) | All confirmed |
| IFBench | 11/12 (92%) | 14/20 (70%) | 8 new models: 3 confirmed, 5 ⊘ |
| Terminal-Bench 2.0 | 12/12 (100%) | 13/20 (65%) | 7 new models all ⊘ except o3-mini |
| SWE-bench V | 10/12 (83%) | 10/20 (50%) | No new models confirmed |
| SWE-bench Pro | 9/12 (75%) | 9/20 (45%) | No new models confirmed |
| LCB v4 | 5/12 (42%) | 10/20 (50%) | 5 new ~ fills; all provisional |
| GDPval-AA ELO | 12/12 (100%) | 12/20 (60%) | 8 new models all ⊘ |
| Speed | 12/12 (100%) | 19/20 (95%) | Nova Pro only ⊘ |
| τ²-Bench | 11/12 (92%) | 12/20 (60%) | o3-mini ~; others ⊘ |
| OSWorld | 6/12 (50%) | 6/20 (30%) | No new models confirmed |
| BrowseComp | 8/12 (67%) | 8/20 (40%) | No new models confirmed |
| RULER/LCR | 10/12 (83%) | 10/20 (50%) | No new models confirmed |
| HLE | 12/12 (100%) | 15/20 (75%) | Scout, Maverick, o3-mini confirmed |
| GPQA Diamond | 12/12 (100%) | 18/20 (90%) | 6 new confirmed; Phi-4 + NovaPro ⊘ |
| MMLU-Pro | 6/12 (50%) | 9/20 (45%) | Scout, Maverick, o3-mini confirmed |
| AIME 2025 | 6/12 (50%) | 7/20 (35%) | o3-mini only new confirmed |
| SciCode | 9/12 (75%) | 13/20 (65%) | Scout, Maverick, o3-mini, Qwen confirmed |
| AA-Omniscience | 8/12 (67%) | 8/20 (40%) | No new models confirmed |

**v5.0 coverage observations:** Adding 8 models reduces coverage percentages for most dimensions because the new entrants bring limited benchmark data. The field now has 20 models but median coverage per quality dimension dropped from ~75% to ~52%. GPQA (90%) and Speed (95%) remain the best-covered dimensions. OSWorld, BrowseComp, SWE-bench V/Pro, and RULER/LCR are critically under-covered at 30–50%.

### 14.8 Framework Design Constraints

The 25% cost weight reflects a deliberate choice for production scale optimization. Academic or research applications would reasonably down-weight cost and up-weight quality dimensions. Custom weight configurations are recommended for teams with different budget constraints.

### 14.9 BigCodeBench and GAIA Slots

Both benchmarks remain reserved as scored dimensions pending ≥4 model submissions from the current 20-model inventory. Re-evaluation planned for v5.1+ as coverage expands with new entrants.

### 14.12 v5.0 New-Model Data Notes

**LCB version ambiguity (5 models):** LCB scores for Llama 4 Scout (32.8%), Llama 4 Maverick (43.4%), o3-mini (71.7%), Grok 3 (79.4%), Mistral Large 3 (82.8%) are all marked ~ (provisional). These models were evaluated after April 2025 and may use LCBv5 or LCBv6 rather than the canonical LCBv4 pool. Scores included with ~ notation and treated as comparable pending confirmation on livecodebench.github.io. If any are confirmed as a different LCB version, they will be moved to ⊘.

**Grok 3 Think mode risk (2 dims):** GPQA (84.6%~) and LCB (79.4%~) are from secondary sources that may reflect Grok 3 Think (reasoning mode) rather than standard Grok 3. Standard-mode GPQA would likely be lower, potentially below the current threshold for several rank positions. Verification priority: confirm mode on canonical leaderboard.

**Free-tier cost validity (Gemma 3 27B):** $0.00 AA eval cost reflects Google's OpenRouter free tier as of April 2026. This is a confirmed AA measurement, not an assumption. However, free-tier rate limits and availability may not match production deployment requirements. Teams should verify free-tier SLAs before treating this as a $0 production cost.

**o3-mini τ²-Bench version:** o3-mini τ²-Bench score of 28.7%~ is from a secondary source and marked provisional. If confirmed, it places o3-mini last in the τ² pool (rank 12/12). The score is directionally consistent with o3-mini's known weakness on multi-step agentic task execution.

### 14.10 FireBench Sub-Dimension Coverage and Reliability Roadmap

FireBench (arXiv:2603.04857, 2026) identifies six constraint categories in enterprise instruction-following: **(1) output format compliance**, **(2) ordered responses**, **(3) item ranking**, **(4) overconfidence calibration**, **(5) positive content requirements**, and **(6) negative content requirements**. The current Reliability dimension (IFBench, 18%) and its planned composite (IFEval 65% + IFBench 35%) cover these categories unevenly:

| FireBench Category | IFEval Coverage | IFBench Coverage | Composite Gap |
|---|---|---|---|
| Output format compliance | Strong (26 fixed format constraint types) | Partial (novel format phrasings) | Minimal — composite covers well |
| Ordered responses | Weak (limited fixed ordering tasks) | Moderate (novel ordering constraints) | Partial — IFBench adds generalization signal |
| Item ranking | None in fixed set | Moderate (novel ranking/priority constraints) | Partial — IFBench adds but does not saturate |
| Overconfidence calibration | None | None | **Full gap** — not an IF metric; addressed separately by AA-Omniscience (1% weight) |
| Positive content requirements | Strong (phrase inclusion, keyword requirements) | Strong (out-of-domain generalization) | Minimal — composite covers well |
| Negative content requirements | Partial (fixed forbidden-phrase patterns) | Moderate (novel exclusion phrasings) | Partial — composite improves but does not saturate |

**Coverage summary:** The IFEval+IFBench composite addresses 5 of 6 FireBench categories (format compliance, positive content well; ordered responses, item ranking, negative content partially). It has zero coverage of overconfidence calibration — the category where models that rank 1st on format compliance often rank 5th or 6th, per FireBench's 13–25 pp cross-category variance finding. ValueRank addresses calibration separately via AA-Omniscience at 1% weight — a defensible design choice because calibration is a distinct epistemic property (does the model know what it doesn't know?) rather than a format-compliance property (does the model follow the stated constraint?).

**Roadmap implications:** Future Reliability dimension upgrades will target the two partially-covered categories — ordered responses and item ranking — which FireBench identifies as particularly discriminative for enterprise use cases such as prioritized task queues and structured report generation. A FireBench-aligned sub-scoring scheme (model-level scores for each of the 6 categories) would allow ValueRank to weight enterprise IF failures by category severity. This upgrade is contingent on FireBench publishing per-model category breakdowns as standard leaderboard output.

### 14.11 External Research Data Conflicts (v4.2 → resolved v4.3)

The multi-AI aggregated research report (April 26, 2026) provided two fills incorporated in v4.2 and three conflicts flagged. All three were resolved in v4.3 via primary-source verification on April 26, 2026.

| Dimension | External Report Value | v4.3 Resolution | Score Impact |
|---|---|---|---|
| **GPT-5.5 LCB v4** | ~91.7%~ (v4.2 fill) | **CORRECTED — reverted to ⊘.** pricepertoken.com LCB leaderboard confirms 91.7% belongs to Gemini 3 Pro Preview, not GPT-5.5. GPT-5.5 is absent from the LCB pool. Misattribution by multi-AI report. | GPT-5.5: −1.8 pts (67.0~→65.2); ~ removed. LCB pool n=6→5; Kimi/Gemini/Opus4.6 all gain from reconstitution. |
| **Kimi K2.6 τ²-Bench** | 96% | **CONFIRMED — updated from 72.4% to 96.0%.** Primary source: AA article "Kimi K2.6: The new leading open weights model" (artificialanalysis.ai) explicitly reports 96% τ²-Bench Telecom for Kimi K2.6. The prior 72.4% was erroneous. | Kimi: +3.7 pts total (57.6, rises #6→#4). τ² pool shift costs all other ranked models 0.4 pts each. |
| **DeepSeek V4-Pro hallucination rate** | 54% (multi-AI) vs 94% (AA) | **CONFIRMED at 94%.** AA article explicitly: "V4 Pro and V4 Flash both have a very high hallucination rate of 94% and 96% respectively." The 54% likely refers to V4-Flash or different methodology. | No change — ValueRank's 94% was correct. |
| **Kimi K2.6 AA Intelligence Index** | 54~ (v4.2 non-scored fill) | Stands. Non-scored reference column; confirmed directionally consistent with AA article data. | No score impact (reference column only). |
| **Kimi K2.6 LCB v4** | 89.6% (multi-AI) vs 82.6% (canonical) | **Still unresolved.** With GPT-5.5 LCB reverted, Kimi's LCB pool rank is now 2/5 (score 75.0) regardless of whether raw value is 82.6% or 89.6%. Score is unchanged either way — low priority. | No score impact at current pool composition. |

**New open item (v4.3):** pricepertoken.com LCB leaderboard shows "Gemini 3 Pro Preview" = 91.7% at rank 1 (above DeepSeek V4-Pro 93.5% at rank 1 in our data — possible different snapshot dates). Our Gemini 3.1 Pro currently has LCB = 76.3% (rank 3/5). If "Gemini 3 Pro Preview" = "Gemini 3.1 Pro," Gemini's LCB would update to 91.7% (rank 2/5, score 75.0, up from 50.0 — +1.5 pts at 6% weight = +0.09 pts). Naming ambiguity and possible snapshot mismatch prevent update. **Verification priority:** confirm "Gemini 3 Pro Preview" identity on canonical LiveCodeBench leaderboard.

---

## 15. Benchmark Reference Index

| Benchmark | Dimension | Type | What it Measures | Source |
|---|---|---|---|---|
| AA Index Eval Cost | Cost | USD | Total cost to run AA's full Intelligence Index benchmark suite (price × actual token usage) | artificialanalysis.ai |
| IFBench | IF (Reliability) | Accuracy % | Reliability dimension: instruction-following generalization across 58 out-of-domain verifiable constraints (Allen AI, NeurIPS 2025). Tests constraint compliance on constraint types not seen in training — unsaturated at 58–76% for current frontier models. Used as the primary Reliability signal; future composite will add IFEval (IFEval 65% + IFBench 35%). | Artificial Analysis IFBench leaderboard; github.com/allenai/IFBench |
| Terminal-Bench 2.0 | Term | Accuracy % | Terminal/CLI agentic task completion | tbench.ai |
| SWE-bench Verified | SWE | Accuracy % | Real GitHub issue resolution (verified subset) | swebench.com |
| SWE-bench Pro | SWEPro | Accuracy % | Harder single-pass GitHub issue resolution; stricter criteria | Scale Labs leaderboard |
| LiveCodeBench v4 | LCB | Accuracy % | Rolling contamination-resistant coding eval | livecodebench.github.io |
| GDPval-AA ELO | GDP | ELO rating | Human preference pairwise comparisons, 141 models | Artificial Analysis GDPval |
| Speed (tok/s) | Spd | Tokens/second | Output generation throughput | Artificial Analysis; provider specs |
| τ²-Bench | τ² | Accuracy % | Multi-step phone/computer agent task success | Artificial Analysis τ²-Bench leaderboard |
| OSWorld | OSW | Accuracy % | Desktop GUI agent task success | os-world.github.io |
| BrowseComp | BC | Accuracy % | Persistent web navigation; 1,266 hard-to-find information retrieval | BenchLM / llm-stats.com/benchmarks/browsecomp |
| RULER (LCR) | LCR | Accuracy % | Long-context retrieval fidelity (128K–1M) | ruler-bench.github.io (provisional data) |
| Humanity's Last Exam | HLE | Accuracy % | Expert-level knowledge breadth; 3,000 questions; WITHOUT-TOOLS canonical | Scale Labs / agi.safe.ai |
| GPQA Diamond | GPQA | Accuracy % | Graduate-level science reasoning (diamond subset) | arXiv:2311.12022 |
| MMLU-Pro | MMLU | Accuracy % | Enhanced MMLU with 10-choice reasoning-focused questions | Artificial Analysis / Kaggle MMLU-Pro leaderboard |
| AIME 2025 | AIME | Accuracy % | American Invitational Mathematics Exam 2025 | aops.com / arXiv reports |
| SciCode | Sci | Accuracy % | Scientific coding tasks (domain-expert problems) | scicode-bench.github.io |
| AA-Omniscience | Omni | Score | accuracy% − hallucination_rate% | Artificial Analysis Omniscience v2 |
| TTFT | Ref only | Milliseconds | Time-to-first-token (not scored; see [methodology.md §3.3](methodology.md#33-ttft-exclusion)) | Artificial Analysis |
| BigCodeBench | (reserved) | Accuracy % | Function-level coding with complex instructions | bigcodebench.github.io |
| GAIA Level 3 | (reserved) | Accuracy % | General AI assistant real-world tasks, hardest tier | huggingface.co/GAIA |
