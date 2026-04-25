# ValueRank — Limitations, Gaps & Benchmark Reference
**Updated per version**

← [README](README.md) · [Insights](insights.md) · [Methodology](methodology.md)

---

## 14. Limitations & Known Gaps

### 14.1 Data Freshness

- **DeepSeek V4-Pro** (April 24, 2026): 7 dimensions remain ⊘ after v4.0 gap-fills: IFBench, τ²-Bench, OSWorld, RULER, AIME, SciCode, LCB (not yet in LCB pool). All four confirmed fills (Cost, Term, SWEPro, Omni) came in below neutral-50 — the provisional #8 rank in v3.0 was optimistic.
- **GPT-5.5** (April 23, 2026): 3 dimensions still ⊘. Speed (63.6) and SWEPro (68.8) confirmed in v4.0; LCB provisionally filled at ~91.7%~ in v4.2 (secondary source, multi-AI aggregated report; see §14.11 for conflicts). Confirmed ⊘ remaining: LCR, AIME, SciCode.
- All other model data is sourced from official publications and established leaderboards as of April 25, 2026.

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

### 14.7 Dimension Coverage Status (v4.0)

| Dimension | v3.0 Coverage | v4.0 Coverage | Discriminative Power |
|---|---|---|---|
| SWE-bench Pro | 5/12 (42%) | 9/12 (75%) | High — 5.2% spread between #1 and #2 |
| BrowseComp | 6/12 (50%) | 8/12 (67%) | High — GLM 0.0 vs GPT-5.5 100.0 reveals clear separation |
| MMLU-Pro | 4/12 (33%) | 6/12 (50%) | Moderate — still 6 models at neutral-50 |

SWEPro is now sufficiently covered to be highly discriminative. MMLU-Pro remains the weakest of the three activated dimensions; expect further coverage expansion in v4.1+.

### 14.8 Framework Design Constraints

The 25% cost weight reflects a deliberate choice for production scale optimization. Academic or research applications would reasonably down-weight cost and up-weight quality dimensions. Custom weight configurations are recommended for teams with different budget constraints.

### 14.9 BigCodeBench and GAIA Slots

Both benchmarks remain reserved as scored dimensions pending ≥4 model submissions from the current 12-model inventory. Will be re-evaluated in v4.0.

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

### 14.11 External Research Data Conflicts (v4.2)

The multi-AI aggregated research report (April 26, 2026; sources: Gemini, Claude, ChatGPT, Copilot, Perplexity, DeepSeek) provided two fills incorporated in v4.2 and three conflicts flagged but not acted upon. All three unresolved conflicts require primary-source verification before updating.

| Dimension | External Report Value | ValueRank Current Value | Source of Conflict | Resolution |
|---|---|---|---|---|
| **GPT-5.5 LCB v4** | ~91.7% | ⊘ → **91.7%~** (v4.2 fill) | Multi-AI report (6 sources); approximate (~) | **Incorporated with ~ notation.** Rank 2/6, score 80.0~. Note: report shows Kimi LCB = 89.6% vs our 82.6% — suggests possible LCB version mismatch. Pending canonical leaderboard confirmation. |
| **Kimi K2.6 AA Intelligence Index** | 54 | ⊘ → **54~** (v4.2 fill) | Multi-AI report; reference column only (non-scored) | **Incorporated with ~ notation.** Non-scored reference column; no score impact. |
| **Kimi K2.6 τ²-Bench** | 96% | 72.4% (canonical) | Multi-AI report vs. Artificial Analysis leaderboard | **Not updated.** 96% would make Kimi τ² rank 2/11 (above GPT-5.5's 98.0%). Major discrepancy — possible τ¹-Bench vs. τ²-Bench variant confusion, or different test set. Requires direct AA leaderboard verification. |
| **Kimi K2.6 LCB v4** | 89.6% | 82.6% (canonical) | Multi-AI report vs. prior research session | **Not updated.** If 89.6% were correct (still rank 2/5 in the existing 5-model pool, unchanged score), our score would be unaffected but raw value would differ. Low-priority pending LCB leaderboard check. |
| **DeepSeek V4-Pro hallucination rate** | 54% | 94% (from AA article) | Multi-AI report vs. Artificial Analysis article | **Not updated.** 94% hallucination rate is sourced from an Artificial Analysis article ("DeepSeek is back among the leading open weights models") cited in §5.3. The 54% figure may reflect V4-Flash rather than V4-Pro, or a different measurement methodology. Requires primary AA source re-verification. |

**Verification priority:** LCB leaderboard (affects GPT-5.5 quality rank + Kimi/MiniMax ordering) → AA τ²-Bench leaderboard (Kimi τ² would significantly improve Kimi's score) → DeepSeek hallucination rate (AA Omniscience scoring).

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
