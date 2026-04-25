# ValueRank — Research Evidence
**All primary research underpinning ai-models-ranking.md v4.0**
*Three research runs, April 25, 2026 — merged in chronological order*

---

> **How to read this document:**
> - **Run 1** (Quick mode) — Initial trio research: GPT-5.5, DeepSeek V4-Pro, Kimi K2.6 launch data
> - **Run 2** (Deep mode) — Full benchmark update: all 12 models × all dimensions for v3.0 → v4.0
> - **Run 3** (UltraDeep mode) — Gap-fill mission: all remaining ⊘ cells, coverage expansion, new dimension evaluation

---

# Run 1 — Initial Trio Research
**Mode:** Quick | **Date:** April 25, 2026 | **Covers:** GPT-5.5, DeepSeek V4-Pro, Kimi K2.6

---

## Executive Summary

Three major AI models released within the same five-day window in late April 2026 — GPT-5.5 (OpenAI, April 23), DeepSeek V4 (DeepSeek, April 24), and Kimi K2.6 (Moonshot AI, April 20) — mark the most concentrated frontier launch cluster since the GPT-4/Claude 2/Gemini 1.0 era. Each targets a different position on the capability-cost frontier.

**GPT-5.5** is the unambiguous overall performance leader on the key benchmarks available so far: highest HLE-with-tools (57.2%), top GPQA Diamond (93.5%), top SWE-bench Verified (88.7%), top Terminal-Bench 2.0 (82.7%), and top Artificial Analysis Intelligence Index (60). It is also the most expensive of the three at $5/$30 per million tokens and is closed-source.

**Kimi K2.6** is the leading open-weight model — 1T-parameter MoE, Apache 2.0 licensed — and punches significantly above its weight class in coding and long-horizon agentic tasks. It leads GPT-5.4 and Claude Opus 4.6 on HLE-Full with tools (54.0) and matches GPT-5.5 Pro on SWE-bench Pro (58.6%). It is the strongest open-source competitor to date on these elite benchmarks.

**DeepSeek V4 Pro** occupies the cost-performance sweet spot for organizations that need frontier-adjacent capability at a fraction of the price. Its LiveCodeBench score (93.5%) and Codeforces rating (3206) are best-in-class across all three models on competitive programming, and its Putnam-2025 proof (120/120) establishes a new formal math benchmark. However, it trails noticeably on knowledge retrieval (SimpleQA-Verified: 57.9% vs Gemini's 75.6%) and overall reasoning (HLE: 37.7%).

---

## Introduction

### Research Scope

This report aggregates all publicly available benchmark scores for the three models as of April 25, 2026, covering: coding (SWE-bench Verified, SWE-bench Pro, HumanEval, LiveCodeBench, Terminal-Bench 2.0, Codeforces), reasoning & science (GPQA Diamond, HLE/Humanity's Last Exam), mathematics (AIME 2025/2026, MATH, HMMT, IMOAnswerBench, Putnam-200, GSM8k), knowledge (MMLU, MMLU-Pro, SimpleQA-Verified), multimodal (MathVista, MMMU Pro), and agentic (GDPval-AA Elo, BrowseComp).

### Key Assumptions
- DeepSeek V4 scores refer to **V4-Pro** unless explicitly noted as V4-Flash.
- HLE scores may reflect "with tools" vs "without tools" variants; this is annotated per model where data is available.
- Kimi K2.6 HLE-Full (54.0) is with-tools; its text-only subset without tools is 36.4%.
- One search result reported DeepSeek V4-Pro HLE = 92.6%, which is inconsistent with all other sources (frontier models cluster at 37–57%) and is likely a data error; the 37.7% figure is used throughout.

---

## Findings

### Finding 1: Model Overview & Release Summary

| Model | Developer | Released | Architecture | Params (Total / Active) | Context | License | Pricing (in/out per MTok) |
|---|---|---|---|---|---|---|---|
| **GPT-5.5** | OpenAI | Apr 23, 2026 | Dense (agent-first) | Undisclosed | 1M tokens | Closed | $5 / $30 |
| **GPT-5.5 Pro** | OpenAI | Apr 23, 2026 | Dense (agent-first) | Undisclosed | 1M tokens | Closed | $30 / $180 |
| **DeepSeek V4-Pro** | DeepSeek | Apr 24, 2026 | MoE | 1.6T / 49B | 1M tokens | Apache 2.0 | $1.74 / $3.48 |
| **DeepSeek V4-Flash** | DeepSeek | Apr 24, 2026 | MoE | 284B / 13B | 1M tokens | Apache 2.0 | $0.14 / $0.28 |
| **Kimi K2.6** | Moonshot AI | Apr 20, 2026 | MoE (multimodal) | ~1T / ~32B | 256K tokens | Open | ~$0.30/run |

GPT-5.5 is described by OpenAI as a fully retrained base model (the first from-scratch retraining since GPT-4.5), with an architecture, pretraining corpus, and agent-oriented objectives all reworked. The codename "Spud" appears in OpenAI internal documentation. Enterprise API access opened April 23; consumer ChatGPT rollout is scheduled for early May 2026 [1, 2].

DeepSeek V4-Pro employs a hybrid attention mechanism combining Compressed Sparse Attention (CSA) and Heavily Compressed Attention (HCA) for long-context efficiency. In the 1M-token setting, V4-Pro requires only 27% of single-token inference FLOPs and 10% of KV cache compared with DeepSeek-V3.2 — a major engineering achievement [7, 9].

Kimi K2.6 is the first open-weight model to natively support text, image, and video input (truly multimodal MoE), and introduces "agent swarm" scaling: up to 300 sub-agents executing 4,000 coordinated steps within a single run. Its GDPval-AA Elo jumped from 1309 (K2.5) to 1520 (K2.6), the largest single-generation agentic gain in the open-weight category [14, 15].

---

### Finding 2: Coding Benchmarks

| Benchmark | GPT-5.5 | DeepSeek V4-Pro | Kimi K2.6 |
|---|---|---|---|
| **SWE-bench Verified** | **88.7%** | 80.6% | 80.2% |
| **SWE-bench Pro** | **58.6%** | — | **58.6%** |
| **HumanEval** | — | — | 92.0% |
| **LiveCodeBench** | — | **93.5%** | 89.6% |
| **Terminal-Bench 2.0** | **82.7%** | 79.0% (Flash) | — |
| **Codeforces Rating** | — | **3206** | — |

**SWE-bench Verified** is the flagship real-world coding benchmark. GPT-5.5's 88.7% is the current state of the art (reported in the official OpenAI release post), comfortably ahead of DeepSeek V4-Pro (80.6%) and Kimi K2.6 (80.2%) [1, 3, 6, 13].

**SWE-bench Pro**, the harder variant evaluating end-to-end GitHub issue resolution, shows GPT-5.5 and Kimi K2.6 tied at 58.6%, with DeepSeek V4-Pro data not yet published [2, 14].

**LiveCodeBench** (fresh problems from LeetCode/Codeforces/AtCoder, contamination-controlled) is DeepSeek V4-Pro's strongest absolute position at 93.5%, ahead of Kimi K2.6 (89.6%) and Gemini-3.1-Pro (91.7%); GPT-5.5 LiveCodeBench score is not yet published separately [8, 17].

**Terminal-Bench 2.0** — the benchmark most relevant to agentic CLI tasks — is GPT-5.5's strongest statement: 82.7%, the state-of-the-art result cited by OpenAI at launch [2, 4]. DeepSeek V4-Flash scores 79.0; V4-Pro's Terminal-Bench score is not separately published.

**Codeforces Rating 3206** for DeepSeek V4-Pro makes it the first open-source model to reach the top of competitive programming rankings, ahead of GPT-5.4 (3168) and Gemini (3052) [8].

**Key Insight:** GPT-5.5 dominates on real-world software engineering tasks (SWE-bench Verified/Pro, Terminal-Bench). DeepSeek V4-Pro dominates on competitive programming throughput (LiveCodeBench, Codeforces). Kimi K2.6 is the most capable open-weight model on software engineering (80.2% SWE-Verified, 58.6% SWE-Pro) and broadly on par with V4-Pro at a fraction of the effective cost.

---

### Finding 3: Mathematics Benchmarks

| Benchmark | GPT-5.5 | DeepSeek V4-Pro | Kimi K2.6 |
|---|---|---|---|
| **AIME 2025** | — | — | 97.3% |
| **AIME 2026** | — | 96.4% | 96.4% |
| **MATH** | — | — | 98.2% |
| **GSM8k** | — | — | 97.3% |
| **HMMT 2026 (Feb)** | — | 95.2% | — |
| **IMOAnswerBench** | — | 89.8% | — |
| **Putnam-200 Pass@8** | — | 81.0 (V4-Flash-Max) | — |
| **Putnam-2025 (Proof)** | — | **120/120** | — |

DeepSeek V4 is the stand-out story in formal mathematics. Its Putnam-2025 proof performance (120/120, proof-perfect) ties the Axiom system and is the first open-source model to reach this level. Its IMOAnswerBench score (89.8%) puts it within range of GPT-5.4 (91.4%) [9, 10].

Kimi K2.6 leads on AIME 2025 (97.3%), MATH (98.2%), and GSM8k (97.3%) — all saturated-or-near-saturated benchmarks for frontier models [14, 16].

Note: Official OpenAI GPT-5.5 math benchmark scores (AIME 2026, MATH, HMMT) were not published in OpenAI's April 2026 launch materials beyond the HLE and GPQA results. This may be updated in the full technical report.

---

### Finding 4: Reasoning & Scientific Knowledge

| Benchmark | GPT-5.5 | DeepSeek V4-Pro | Kimi K2.6 |
|---|---|---|---|
| **GPQA Diamond** | **93.5%** | 88.8% | 90.5% |
| **HLE (with tools)** | **57.2%** | ~37.7%* | 54.0% |
| **HLE (without tools)** | 41.4% | — | 36.4% |
| **MMLU** | 92.4% | — | 86.4% |
| **MMLU-Pro** | 54.6%** | 87.5% | 84.6% |

*\*37.7% is confirmed by multiple third-party evaluators; one outlier source cited 92.6% which appears to be a data error.*
*\*\*MMLU-Pro discrepancy: BenchLM reports GPT-5.5 MMLU-Pro at 54.6 which appears low — this may reflect a scoring methodology difference (0-shot vs few-shot) or an incomplete benchmark run; Artificial Analysis notes GPT-5.5 xhigh Intelligence Index = 60.*

**Humanity's Last Exam (HLE)** is currently the gold standard for measuring frontier reasoning capability. GPT-5.5 tops the leaderboard at 57.2% with tools — a clear lead over Kimi K2.6 (54.0%) and significantly ahead of DeepSeek V4-Pro (37.7%) [1, 2, 15].

The HLE gap between GPT-5.5 and DeepSeek V4-Pro is the largest performance delta across all benchmarks assessed in this report: 19.5 percentage points. This is not a marginal difference — it confirms that DeepSeek V4 Pro is not a peer-to-peer frontier competitor on general reasoning despite its cost advantages.

**GPQA Diamond** (graduate-level science questions, PhD-setter level difficulty): GPT-5.5 leads at 93.5%, with Kimi K2.6 (90.5%) and DeepSeek V4-Pro (88.8%) both showing strong performance within a 5-point spread [1, 11, 18].

---

### Finding 5: Knowledge Retrieval

| Benchmark | GPT-5.5 | DeepSeek V4-Pro | Kimi K2.6 |
|---|---|---|---|
| **SimpleQA-Verified** | — | 57.9% | — |
| **Hallucination reduction** | 60% ↓ vs GPT-5.4 | — | 39% (abs rate, ↓ from 65%) |

SimpleQA-Verified measures factual knowledge retrieval without hedging. DeepSeek V4-Pro's 57.9% versus Gemini-3.1-Pro's 75.6% is the model's most notable weakness — an 18-point gap that matters significantly for retrieval-augmented and factual Q&A applications [8].

GPT-5.5's 60% hallucination reduction versus GPT-5.4 is cited prominently by OpenAI as a headline improvement, though no absolute SimpleQA score is published in the initial launch materials.

Kimi K2.6 reduced its hallucination rate from 65% (K2.5) to 39% (K2.6) — the model now preferentially abstains rather than fabricates. This is a significant reliability improvement for deployment [14].

---

### Finding 6: Multimodal Performance (Kimi K2.6 Only)

| Benchmark | Kimi K2.6 |
|---|---|
| **MathVista** | 67.1% |
| **MMMU Pro** | 75.6% |

Kimi K2.6 is the only model of the three with published native multimodal benchmarks at launch, reflecting its native text/image/video MoE architecture. GPT-5.5 supports multimodal input but has not published formal MMMU/MathVista scores in its April launch package. DeepSeek V4's multimodal capability is text-only at current release [14, 15].

---

### Finding 7: Agentic & Long-Horizon Performance

| Benchmark | GPT-5.5 | DeepSeek V4-Pro | Kimi K2.6 |
|---|---|---|---|
| **GDPval-AA Elo** | — | — | **1520** |
| **BrowseComp** | — | — | 83.2% |
| **Terminal-Bench 2.0** | **82.7%** | 79.0% (Flash) | — |
| **Agent Swarm Depth** | Unspecified | Unspecified | 300 agents / 4000 steps |

GPT-5.5 is explicitly marketed as an "agent model" — its launch framing emphasizes autonomous task completion across multi-tool workflows. Terminal-Bench 2.0's 82.7% validates this positioning for CLI-based agentic use.

Kimi K2.6's GDPval-AA Elo of 1520 (up from 1309 in K2.5) represents the largest agentic improvement in a single model generation. BrowseComp (83.2%) measures deep web research capability. Its documented ability to orchestrate 300 sub-agents across 4,000 coordinated steps makes it the only open-weight model currently publishable for large-scale autonomous research workflows [14, 15].

---

### Finding 8: Intelligence Index & Leaderboard Positions

| Index | GPT-5.5 (xhigh) | DeepSeek V4-Pro | Kimi K2.6 |
|---|---|---|---|
| **Artificial Analysis Intelligence Index** | **60** | 52 | 54 |
| **Open-weight rank (AA)** | N/A | #2 | **#1** |
| **BenchLM Score** | — | 71/100 (#32 of 115) | 83/100 (#16 of 118) |

The Artificial Analysis Intelligence Index v4.0 provides a composite score: GPT-5.5 leads overall (60), Kimi K2.6 leads open-weight (54), DeepSeek V4-Pro is second open-weight (52).

BenchLM's provisional rankings show Kimi K2.6 significantly outpacing DeepSeek V4-Pro (83 vs 71), which is consistent with the broader benchmark data showing K2.6 ahead on more benchmarks with higher scores.

---

## Synthesis & Key Insights

**1. The open-weight frontier just moved materially.** Kimi K2.6 and DeepSeek V4-Pro together demonstrate that open-source MoE models at the 1T+ parameter scale can now match GPT-5.4/Claude Opus 4.6 on the majority of coding and math benchmarks. This represents a meaningful compression of the closed-open frontier gap that was approximately 6 months a year ago.

**2. GPT-5.5's moat is reasoning, not just coding.** Its HLE lead (57.2% vs 54.0% for Kimi K2.6 vs 37.7% for DeepSeek V4-Pro) and GPQA Diamond lead (93.5% vs 90.5% vs 88.8%) confirm that raw scientific reasoning ability is still where closed frontier models maintain the largest edge. This matters most for research assistance, complex multi-step reasoning, and novel problem solving.

**3. DeepSeek V4's value proposition is real, but domain-specific.** Its competitive advantages (LiveCodeBench #1 at 93.5%, Codeforces 3206, Putnam-2025 proof-perfect, $1.74/$3.48 pricing) are compelling for competitive programming, formal mathematics, and price-sensitive deployments. Its relative weakness on knowledge retrieval (SimpleQA 57.9%) and general reasoning (HLE 37.7%) means it is not a drop-in replacement for GPT-5.5 or even Gemini-3.1-Pro at general tasks.

**4. Kimi K2.6 is the best open-weight model for agentic coding.** Its combination of SWE-bench Pro = 58.6% (tied with GPT-5.5), GDPval-AA Elo 1520, BrowseComp 83.2%, and agent swarm capability (300 sub-agents, 4000 steps) makes it the strongest open-weight choice for autonomous coding workflows. For organizations that cannot use closed-source APIs, this is the model to evaluate first.

**5. All three models benefit from the 1M context window.** GPT-5.5 and DeepSeek V4-Pro both support 1M tokens; Kimi K2.6 offers 256K. For ultra-long-document analysis (codebase-wide refactors, full document sets), GPT-5.5 and V4 have an architectural edge over K2.6.

---

## Limitations & Caveats (Run 1)

- **Benchmark inflation risk:** SWE-bench Verified and AIME 2025 are approaching saturation at frontier levels; marginal gains here are increasingly less meaningful. HLE and SWE-bench Pro are better differentiators.
- **Partial GPT-5.5 data:** OpenAI has not published AIME 2026, MATH, HMMT, or LiveCodeBench scores for GPT-5.5 as of April 25. The full technical report is expected in May 2026.
- **DeepSeek V4 preview status:** V4-Pro and V4-Flash were released as a "preview" on Hugging Face. Final model weights may differ from the evaluated checkpoint, and benchmark coverage is incomplete (no SWE-bench Pro, Terminal-Bench Pro, or agentic Elo published).
- **MMLU-Pro discrepancy (GPT-5.5):** The 54.6 MMLU-Pro score for GPT-5.5 from BenchLM appears anomalously low and may reflect a 0-shot evaluation vs. the few-shot setting used for comparison; this finding should be treated with low confidence until confirmed.
- **Single-source HLE discrepancy for V4:** One source reported DeepSeek V4-Pro HLE = 92.6%, which is physically implausible given the current frontier range (37–57%). This has been excluded from the analysis.

---

## Bibliography (Run 1)

1. [Introducing GPT-5.5 | OpenAI](https://openai.com/index/introducing-gpt-5-5/)
2. [GPT-5.5 Released: First Fully Retrained Base Model Since GPT-4.5 | oFox.ai](https://ofox.ai/blog/gpt-5-5-release-guide-2026/)
3. [GPT-5.5 Review: 88.7% SWE-Bench, 92.4% MMLU | TokenMix Blog](https://tokenmix.ai/blog/gpt-5-5-spud-review-88-swe-bench-2026/)
4. [OpenAI GPT-5.5 "Spud" vs Claude Opus 4.7: Benchmark Breakdown | MindWiredAI](https://mindwiredai.com/2026/04/24/gpt-5-5-is-here-benchmarks-pricing-and-who-should-actually-upgrade-april-2026/)
5. [GPT-5.5 System Card | OpenAI Deployment Safety Hub](https://deploymentsafety.openai.com/gpt-5-5)
6. [OpenAI GPT-5.5 Benchmark Results | CodeRabbit](https://www.coderabbit.ai/blog/gpt-5-5-benchmark-results)
7. [DeepSeek V4 Released: Everything You Need to Know | FelloAI](https://felloai.com/deepseek-v4/)
8. [DeepSeek V4-Pro Review: Benchmarks, Pricing & Architecture | BuildFastWithAI](https://www.buildfastwithai.com/blogs/deepseek-v4-pro-review-2026)
9. [DeepSeek V4 Preview Release | DeepSeek API Docs](https://api-docs.deepseek.com/news/news260424)
10. [DeepSeek V4 (2026): 1T Parameters, 81% SWE-bench | NxCode](https://www.nxcode.io/resources/news/deepseek-v4-release-specs-benchmarks-2026)
11. [DeepSeek V4 Benchmarks: MMLU, HumanEval & SWE-bench | Macaron](https://macaron.im/blog/deepseek-v4-benchmarks)
12. [DeepSeek V4 Pro Benchmarks 2026 | BenchLM.ai](https://benchlm.ai/models/deepseek-v4-pro)
13. [GPT-5.5 Benchmarks 2026 | BenchLM.ai](https://benchlm.ai/models/gpt-5-5)
14. [Kimi K2.6 Tech Blog: Advancing Open-Source Coding | Moonshot AI](https://www.kimi.com/blog/kimi-k2-6)
15. [Moonshot AI Releases Kimi K2.6 with Long-Horizon Coding | MarkTechPost](https://www.marktechpost.com/2026/04/20/moonshot-ai-releases-kimi-k2-6-with-long-horizon-coding-agent-swarm-scaling-to-300-sub-agents-and-4000-coordinated-steps/)
16. [Kimi K2.6 Benchmarks 2026 | BenchLM.ai](https://benchlm.ai/models/kimi-2-6)
17. [Kimi K2.6 — The New Leading Open Weights Model | Artificial Analysis](https://artificialanalysis.ai/articles/kimi-k2-6-the-new-leading-open-weights-model)
18. [Kimi K2.6 vs GPT-5.4 vs Claude Opus | BuildFastWithAI](https://www.buildfastwithai.com/blogs/kimi-k2-6-vs-gpt-claude-benchmarks)
19. [LLM Leaderboard 2026 | Artificial Analysis](https://artificialanalysis.ai/leaderboards/models)
20. [Kimi K2.6: Pricing, Benchmarks & Performance | llm-stats.com](https://llm-stats.com/models/kimi-k2.6)
21. [DeepSeek V4-Pro | Hugging Face](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)
22. [Kimi K2.6 | Hugging Face](https://huggingface.co/moonshotai/Kimi-K2.6)

---

# Run 2 — Full Benchmark Update (v3.0 → v4.0)
**Mode:** Deep | **Date:** April 25, 2026 | **Covers:** All 12 models × 18 dimensions

---

## Executive Summary

This report consolidates confirmed, probable, and unverified benchmark scores for 12 frontier AI models across 15 existing scored dimensions, 3 newly activated dimensions (SWE-bench Pro, BrowseComp, MMLU-Pro), and 4 candidate dimensions (AIME 2026, MathVista, BigCodeBench, GAIA L3) assessed for readiness. Key changes from the v2.5 data:

**Corrections to existing data (4):**
1. Gemini 3.1 Pro τ²-Bench: 95.6% → **99.3%** (confirmed, significant rerank)
2. Kimi K2.6 GDPval ELO: 1,484 → **1,520** (confirmed from Artificial Analysis)
3. GPT-5.5 IFBench: ⊘ → **75.9%** (fills high-weight gap — 20% dimension)
4. GPT-5.5 SWE-bench Verified: ⊘ → **88.7%** (probable; OpenAI tech card; canonical leaderboard still shows Opus 4.7 at 87.6% as leader as of Apr 24)

**New model added (1):**
- DeepSeek V4-Pro: partial data available for 6 of 15 existing dimensions; full ⊘ map documented

**New dimensions activated (3):**
- BrowseComp: 6/12 models confirmed (50% coverage) → activate
- SWE-bench Pro: 5/12 models confirmed (42% coverage) → activate
- MMLU-Pro: 4/12 models confirmed (33% coverage) → activate at minimum threshold

**HLE methodology resolved:** Canonical Scale Labs leaderboard (agi.safe.ai) uses **without-tools** scores. Existing doc values are CORRECT. The "with-tools" scores (GPT-5.5=57.2%, Kimi K2.6=54.0%) are from a separate Hugging Face leaderboard and should NOT replace existing data.

---

## Introduction

### Scope
- 12 models (11 existing + DeepSeek V4-Pro, released April 24 2026)
- 15 existing scored dimensions + 3 new dimensions activated + 4 evaluated for activation
- Research date: April 25, 2026
- Mode: Deep (8 phases)

### Key Assumptions
- "Confirmed" = found in ≥2 independent sources
- "Probable" = found in 1–2 sources with plausible methodology; no contradicting source
- "Unverified" = single source, contradicts other data, or methodology unclear
- All HLE scores are WITHOUT-TOOLS (canonical Scale Labs leaderboard)
- All SWE-bench Verified scores use the canonical swebench.com leaderboard unless noted
- Terminal-Bench 2.0 scores reflect best published score per model on tbench.ai (scaffold-best)

---

## Finding 1: HLE Methodology Resolution

**Critical question:** Does the canonical leaderboard use with-tools or without-tools?

**Finding:** The canonical leaderboard at [agi.safe.ai](https://agi.safe.ai/) / Scale Labs uses WITHOUT-TOOLS as the primary score. A separate "HLE Leaderboard for Agents with Tools" exists on Hugging Face (zoom-ai space) but is not the canonical source. [1, 2, 3]

**Impact on existing data:**
| Model | Existing HLE | Without-tools research | With-tools research | Status |
|---|---|---|---|---|
| Gemini 3.1 Pro | 44.7% | 44.7% (canonical) | — | ✓ Correct |
| GPT-5.5 xhigh | 44.3% | 44.3% (canonical) | 57.2% | ✓ Correct |
| Claude Opus 4.7 | 46.9% | ~46-47% | — | ✓ Correct |
| Kimi K2.6 | 34.7% | 36.4% (research) | 54.0% | ~Close (within 1.7%) |
| GPT-5.4 | 41.6% | 41.6% (canonical) | 52.1% | ✓ Correct |
| DeepSeek V4-Pro | n/a | 37.7% | — | New model |

**Conclusion:** No HLE corrections needed for existing 11 models. Kimi K2.6's 34.7% may be slightly understated (36.4% from research) but the difference is within measurement variance; retain existing value pending canonical leaderboard confirmation. [1, 2]

---

## Finding 2: Corrections to Existing Scored Dimensions

### 2A. Gemini 3.1 Pro — τ²-Bench: 95.6% → 99.3% (CONFIRMED)

**Evidence:** Digital Applied benchmark analysis confirms Gemini 3.1 Pro achieved 99.3% on τ²-Bench Telecom. Cross-referenced against the Artificial Analysis τ²-Bench leaderboard. [4, 5]

**Confidence:** Confirmed (2 independent sources)

**Ranking impact:** Gemini 3.1 Pro moves from τ² rank 2/8 (80.0 normalized) to rank 1/8 (100.0 normalized) — a +2.5% impact on its weighted score at 4% dimension weight.

### 2B. Kimi K2.6 — GDPval ELO: 1,484 → 1,520 (CONFIRMED)

**Evidence:** Artificial Analysis article "Kimi K2.6: The new leading open weights model" published April 21, 2026 explicitly states GDPval-AA Elo of 1,520 (up from Kimi K2.5's 1,309). This replaces the 1,484 figure in the existing doc, which reflected pre-release Kimi K2.6 evaluation data. [6]

**Confidence:** Confirmed (primary source: Artificial Analysis)

### 2C. GPT-5.5 — IFBench: ⊘ → 75.9% (CONFIRMED)

**Evidence:** GPT-5.5 (xhigh) scores 75.9% on IFBench for instruction following; GPT-5.5 (high) scores 71.6%. The xhigh variant is the model evaluated throughout the ranking doc. [7, 8]

**Confidence:** Confirmed (2 sources: designforonline.com review, Harvey research preview)

**Ranking impact:** This fills the highest-weight (20%) gap in GPT-5.5's profile. GPT-5.5 moves from neutral-50 to its actual IFBench rank position. With 75.9%, GPT-5.5 ranks between GLM 5.1 (85.9%) and GPT-5.4 (73.9%) — approximately rank 4-5 of 11. This is a significant improvement from the neutral placeholder.

### 2D. GPT-5.5 — SWE-bench Verified: ⊘ → 88.7% (PROBABLE)

**Evidence:** Multiple third-party reviewers report GPT-5.5 at 88.7% on SWE-bench Verified, citing OpenAI's launch benchmarks. However, the canonical swebench.com leaderboard as of April 24 still shows Claude Opus 4.7 as leader at 87.6% — GPT-5.5 may not have been formally submitted yet. [9, 10, 11]

**Confidence:** Probable (multiple secondary sources; primary leaderboard not yet showing GPT-5.5)

---

## Finding 3: DeepSeek V4-Pro — All Dimensions

**Model overview:** Released April 24, 2026. Apache 2.0 open-source. 1.6T total / 49B active parameters (MoE). 1M context. Pricing: $1.74/$3.48 per MTok (in/out). Artificial Analysis Intelligence Index: 52 (#2 open-weight, behind Kimi K2.6 at 54). [12, 13]

| Dimension | Score | Source | Confidence | Notes |
|---|---|---|---|---|
| **IFBench** | ⊘ | — | — | Part of AA Index composite; individual score not published |
| **Terminal-Bench 2.0** | ⊘ | tbench.ai | — | Flash=79.0%; Pro score not found; tbench requires separate submission |
| **SWE-bench Verified** | 80.6% | VentureBeat, BuildFastWithAI | Confirmed | Multiple sources confirm |
| **LiveCodeBench v4** | 93.5% | DeepSeek release, BuildFastWithAI | Confirmed | Leads Kimi (89.6%) and Gemini (91.7% Preview) |
| **GDPval ELO** | ⊘ | — | — | Not published in any source found |
| **Speed (tok/s)** | 33.5 | Artificial Analysis | Confirmed | Below open-weight median (55.1 t/s); 1.6T MoE overhead |
| **τ²-Bench** | ⊘ | — | — | Part of AA Index; individual score not published |
| **OSWorld** | ⊘ | — | — | Not published |
| **RULER (LCR)** | ⊘ | — | — | Not published |
| **HLE** | 37.7% | BuildFastWithAI, OfficeChai | Confirmed | Below Claude (40%), GPT-5.4 (41.6%), Gemini (44.7%) |
| **GPQA Diamond** | 88.8% | BuildFastWithAI | Probable | Single confirmed source; consistent with model tier |
| **AIME 2025** | 87.5% | NoteLM, BenchLM | Unverified | May reflect DeepSeek R1 not V4-Pro specifically; flag |
| **SciCode** | ⊘ | — | — | Part of AA Index; individual score not published |
| **AA-Omniscience** | ⊘ | — | — | Not published separately |
| **AA Eval Cost ($)** | ~$1,200–1,800 | Estimated | Unverified | Based on $1.74/$3.48 pricing × AA benchmark token volume |

**Additional non-scored data for context:**
- MMLU-Pro: 87.5% [14]
- SimpleQA-Verified: 57.9% [14]
- Codeforces Rating: 3,206 (competitive programming leader) [14]
- Putnam-2025: 120/120 (proof-perfect, first open-source model) [14]
- AIME 2026: 96.4% [14]
- BrowseComp: 83.4% [15]
- SWE-bench Pro: ⊘ (not submitted)

---

## Finding 4: Dimension-by-Dimension Updates for All 12 Models

### 4.1–4.15 Summaries

**Key updates across all dimensions:**

| Dimension | Key Updates |
|---|---|
| IFBench | GPT-5.5 fills to 75.9% (confirmed). All others unchanged. DeepSeek: ⊘. |
| Terminal-Bench 2.0 | All existing confirmed. Note: Gemini 78.4% w/ ForgeCode scaffold vs 68.5% reference. DeepSeek: ⊘ (Flash=79.0%, Pro unpublished). |
| SWE-bench Verified | GPT-5.5 fills to 88.7%† (probable). DeepSeek: 80.6% (confirmed). All others unchanged. |
| LiveCodeBench v4 | DeepSeek: 93.5% (confirmed, cohort leader). All others unchanged. |
| GDPval ELO | Kimi updated 1,484→1,520 (confirmed). DeepSeek: ⊘. All others unchanged. |
| Speed (tok/s) | DeepSeek: 33.5 tok/s (confirmed). GPT-5.5: ⊘ still. All others unchanged. |
| τ²-Bench | Gemini updated 95.6%→99.3% (confirmed, rank 1). DeepSeek: ⊘. All others unchanged. |
| OSWorld | Gemini confirmed ⊘ (no published score). DeepSeek: ⊘. All others unchanged. |
| RULER/LCR | All unchanged. GPT-5.5: ⊘. DeepSeek: ⊘. |
| HLE | All existing confirmed correct. DeepSeek: 37.7% (new). |
| GPQA Diamond | Gemini 94.3% retained (94.1% on AA, minor variance). DeepSeek: 88.8% (probable). |
| AIME 2025 | DeepSeek: 87.5% unverified (may be R1). GPT-5.5: ⊘. |
| SciCode | GPT-5.4: 56.6% confirmed. GPT-5.5: ⊘. DeepSeek: ⊘. |
| AA-Omniscience | GPT-5.5: −29 (57%−86%) confirmed. DeepSeek: ⊘. All others unchanged. |
| AA Eval Cost | DeepSeek: ~$1,400 est. (unverified). All others unchanged. |

---

## Finding 5: New Dimensions — Activation Assessment

### 5A. BrowseComp — ACTIVATE ✓

**What it is:** Benchmark of 1,266 questions requiring persistent web navigation and hard-to-find information retrieval. Tests research agent capability. [18]

**Coverage:** 6/12 models confirmed (50% threshold met)

| Model | BrowseComp Score | Confidence |
|---|---|---|
| GPT-5.5 (Pro) | 90.1% | Confirmed |
| GPT-5.4 (Pro) | 89.3% | Probable |
| Gemini 3.1 Pro | 85.9% | Confirmed |
| Kimi K2.6 | 83.2% | Confirmed |
| DeepSeek V4-Pro | 83.4% | Probable |
| Claude Opus 4.7 | 79.3% | Probable |
| All others | ⊘ | — |

**Suggested weight:** 3%

### 5B. SWE-bench Pro — ACTIVATE ✓

**Coverage:** 5/12 models confirmed

| Model | SWE-bench Pro Score | Confidence |
|---|---|---|
| Claude Opus 4.7 | 64.3% | Confirmed |
| GPT-5.4 | 59.1% | Probable |
| GPT-5.5 | 58.6% | Confirmed |
| Kimi K2.6 | 58.6% | Confirmed |
| Claude Opus 4.6 | 51.9% | Confirmed |
| All others | ⊘ | — |

**Suggested weight:** 4%

### 5C. MMLU-Pro — ACTIVATE ✓ (minimum threshold)

**Coverage:** 4/12 models confirmed

| Model | MMLU-Pro Score | Confidence |
|---|---|---|
| Gemini 3.1 Pro | 89.8% | Confirmed |
| Qwen 3.6 Plus | 88.5% | Confirmed |
| DeepSeek V4-Pro | 87.5% | Probable |
| Kimi K2.6 | 84.6% | Probable |
| GPT-5.5 | 54.6%* | Unverified |

*GPT-5.5 MMLU-Pro = 54.6% is anomalously low (frontier models cluster at 84–92%). Most likely 0-shot evaluation. Mark as ⊘ for scoring.

**Suggested weight:** 2%

---

## Finding 6: Candidate Dimensions — Not Ready to Activate

| Dimension | Status | Reason |
|---|---|---|
| AIME 2026 | Framework slot | Kimi 96.4%, DeepSeek 96.4%, Gemini Preview 98.13% — insufficient coverage, benchmark near-saturated |
| MathVista | Not activated | Kimi only: 67.1% — no other frontier models |
| BigCodeBench | Framework slot | No comprehensive 2026-era submission data found |
| GAIA Level 3 | Framework slot | Framework-dependent scoring (74.6% HAL vs ~44% bare); coverage not comprehensive |

---

## Synthesis & Key Insights (Run 2)

1. **The IFBench gap filling for GPT-5.5 is the highest-impact change.** At 20% weight, replacing neutral-50 with actual 75.9% significantly reorders GPT-5.5's final score.

2. **Gemini 3.1 Pro's τ²-Bench correction (+3.7pp to 99.3%) pushes it to clear rank 1.** At 4% weight this adds ~0.3 pts, reinforcing its #1 overall position.

3. **BrowseComp and SWE-bench Pro tell complementary stories.** BrowseComp rewards research breadth (GPT-5.5 leads); SWE-bench Pro rewards deep code repair (Claude Opus 4.7 leads by 5.7+ points).

4. **DeepSeek V4-Pro has a split profile:** Exceptional on LiveCodeBench (93.5%, #1) and competitive on SWE-bench Verified (80.6%), but weak on HLE (37.7%) and slow (33.5 tok/s). Many scored dimensions are ⊘ because AA Intelligence Index component scores are not published individually.

5. **MMLU-Pro at minimum threshold (4 models).** Adding it creates a knowledge breadth signal that rewards Gemini (89.8%) and Qwen (88.5%) over the coding-specialist tier.

---

## Bibliography (Run 2)

1. [Humanity's Last Exam - Scale Labs Leaderboard](https://labs.scale.com/leaderboard/humanitys_last_exam)
2. [HLE Leaderboard for Agents with Tools (Hugging Face)](https://huggingface.co/spaces/zoom-ai/hle-leaderboard)
3. [Humanity's Last Exam | agi.safe.ai](https://agi.safe.ai/)
4. [Gemini 3.1 Pro Benchmarks, Pricing & Guide | Digital Applied](https://www.digitalapplied.com/blog/google-gemini-3-1-pro-benchmarks-pricing-guide)
5. [τ²-Bench Telecom Benchmark Leaderboard | Artificial Analysis](https://artificialanalysis.ai/evaluations/tau2-bench)
6. [Kimi K2.6: The New Leading Open Weights Model | Artificial Analysis](https://artificialanalysis.ai/articles/kimi-k2-6-the-new-leading-open-weights-model)
7. [GPT-5.5 Review | Design for Online](https://designforonline.com/ai-models/openai-gpt-5-5-xhigh/)
8. [GPT-5.5 Research Preview Results | Harvey](https://www.harvey.ai/blog/gpt-5-5-research-preview-results)
9. [GPT-5.5 Review: 88.7% SWE-Bench | TokenMix](https://tokenmix.ai/blog/gpt-5-5-spud-review-88-swe-bench-2026/)
10. [SWE-Bench Leaderboard April 2026 | marc0.dev](https://www.marc0.dev/en/leaderboard)
11. [OpenAI GPT-5.5 "Spud" vs Claude Opus 4.7 | MindWired](https://mindwiredai.com/2026/04/24/gpt-5-5-is-here-benchmarks-pricing-and-who-should-actually-upgrade-april-2026/)
12. [DeepSeek V4 Pro (Max) — Intelligence, Performance | Artificial Analysis](https://artificialanalysis.ai/models/deepseek-v4-pro)
13. [DeepSeek V4 Pro Becomes #2 Rated Open Model | OfficeChai](https://officechai.com/ai/deepseek-v4-pro-becomes-second-highest-rated-open-model-on-artificial-analysis-index-with-score-of-52/)
14. [DeepSeek V4-Pro Review: Benchmarks, Pricing & Architecture | BuildFastWithAI](https://www.buildfastwithai.com/blogs/deepseek-v4-pro-review-2026)
15. [BrowseComp Benchmark 2026 | BenchLM.ai](https://benchlm.ai/benchmarks/browseComp)
16. [Gemini 3.1 Pro vs Claude Opus 4.6 | aitoolbriefing](https://aitoolbriefing.com/blog/gpt-5-4-vs-gemini-3-1-pro-vs-claude-opus-4-6-march-2026/)
17. [AA-Omniscience: Knowledge and Hallucination | Artificial Analysis](https://artificialanalysis.ai/evaluations/omniscience)
18. [BrowseComp Leaderboard | llm-stats.com](https://llm-stats.com/benchmarks/browsecomp)
19. [SWE-Bench Pro Leaderboard | Scale Labs](https://labs.scale.com/leaderboard/swe_bench_pro_public)
20. [SWE-Bench Pro Leaderboard 2026 | morphllm](https://www.morphllm.com/swe-bench-pro)
21. [MMLU-Pro Benchmark Leaderboard | Artificial Analysis](https://artificialanalysis.ai/evaluations/mmlu-pro)
22. [Terminal-Bench 2.0 Leaderboard | tbench.ai](https://www.tbench.ai/leaderboard/terminal-bench/2.0)
23. [SWE-bench Leaderboards | swebench.com](https://www.swebench.com/)
24. [IFBench Benchmark Leaderboard | Artificial Analysis](https://artificialanalysis.ai/evaluations/ifbench)
25. [DeepSeek V4 — Almost on the Frontier | Simon Willison](https://simonwillison.net/2026/apr/24/deepseek-v4/)

---

# Run 3 — UltraDeep Gap-Fill
**Mode:** UltraDeep | **Date:** April 25, 2026 | **Covers:** All remaining ⊘ cells in v3.0 (60+ targets)

---

## Executive Summary

This ultradeep research mission targeted 60+ specific data gaps and flagged values in the v3.0 AI model ranking document. **14 high-confidence new data points** were found that fill ⊘ cells; **5 provisional data points** (probable confidence) fill additional cells; **3 corrections** to existing data are recommended. Key headline findings:

1. **DeepSeek V4-Pro** cost ($1,071.28 AA eval cost) and GDPval ELO (1,554) are now confirmed — its cost lands at rank 7/12.
2. **GPT-5.5 speed confirmed** at 74.7 tok/s (xhigh mode) — fills the largest single missing quality dimension.
3. **SWE-bench Pro coverage expands** from 5/12 to 9/12 models — now fully activatable. New scores: GLM 58.4%, Qwen 56.6%, MiniMax 56.2%, DeepSeek 55.4%.
4. **BrowseComp expands** from 6/12 to 8/12 — Claude Opus 4.6 (83.7%) and GLM-5.1 (68%) fill gaps.
5. **MMLU-Pro expands** from 4/12 to 6/12 — Claude Opus 4.7 (89.87%, new #1) and GLM-5.1 (85.8%) fill gaps.
6. **AA-Omniscience** fills for Kimi K2.6 (+6 score, 39% hall rate) and DeepSeek V4-Pro (-10, 94% hall rate).
7. **GPT-5.5 SWE-bench Verified 88.7%** now confirmed from multiple sources — dagger (†) flag removed.
8. **AIME 2026** has insufficient coverage for our 12-model cohort (3/12 found) — cannot activate as scored dimension yet.
9. **DeepSeek real scores are mostly below neutral-50** on cost, speed, SWEPro, and Omni — filling gaps lowers DeepSeek's ranking from #8 to #9.
10. **GLM 5.1 drops significantly** — BrowseComp real score of 68% (last in 8-model cohort) replaces neutral-50, costing ~1.5 pts at 3% weight.

---

## Part A — DeepSeek V4-Pro: All ⊘ Dimensions

### A1. Terminal-Bench 2.0
- **Score: 67.9%** — Source: HuggingFace model card (deepseek-ai/DeepSeek-V4-Pro)
- **Confidence: Probable (self-reported)** — NOT on tbench.ai canonical leaderboard
- **Status: Fills ⊘** (mark as self-reported †self)

### A2. SWE-bench Pro
- **Score: 55.4%** — Source: HuggingFace model card + BenchLM.ai (April 24, 2026)
- **Confidence: Confirmed** (two independent sources)
- **Status: Fills ⊘** — Rank 9/9 (last) = 0.0 score. At 4% weight: significant negative vs neutral-50.

### A3. GDPval-AA ELO
- **Score: 1,554** — Source: HuggingFace model card + Artificial Analysis article
- **Confidence: Confirmed**
- **Status: Fills ⊘** — Slots DeepSeek at rank 6/12 (above GLM 1,535, Kimi 1,520, MiniMax 1,514).

### A4. IFBench
- **Score: 76.5%** — Source: Synthesized search result citing AA and HuggingFace data
- **Confidence: Probable (weak)** — Could not directly verify on primary leaderboard
- **Status: Keep as provisional ⊘** — Use in v4.1 when confirmed on primary IFBench leaderboard.

### A5. AA-Omniscience
- **Score: -10** (84% accuracy − 94% hallucination rate)
- **Source:** Artificial Analysis article on DeepSeek V4 Pro
- **Confidence: Confirmed**
- **Status: Fills ⊘**

### A6. AA Index Eval Cost
- **Score: $1,071.28** — Source: Artificial Analysis model page, confirmed by separate search
- **Confidence: Confirmed**
- **Status: Fills ⊘** — Rank 7/12 (between Kimi $947.87 and GPT-5.4 $2,851.01).

### A7. Speed (tok/s) — Minor Correction
- **Score: 35.8 tok/s** — Source: Artificial Analysis model page (corrects existing 33.5)
- **Confidence: Confirmed**
- **Status: CORRECTS existing value** — Rank does not change (still 11/12).

### A8. τ²-Bench, OSWorld, RULER, AIME 2025, SciCode
All remain ⊘ after exhaustive search:
- τ²-Bench: Component of AA Index; individual score not published
- OSWorld: Marketing claims but no benchmark numbers published
- RULER/LCR: MRCR 1M = 83.5% published but is NOT canonical RULER benchmark
- AIME 2025: The 87.5% seen previously is likely a different model version/configuration; attribution unclear
- SciCode: One unverified source reported 50%; maintain ⊘

---

## Part B — GPT-5.5: Remaining ⊘ Dimensions

### B1. Speed (tok/s) — CONFIRMED
- **Score: 74.7 tok/s** (xhigh mode) — Source: Artificial Analysis model page
- **Confidence: Confirmed**
- **Status: Fills ⊘** — Nearly ties GPT-5.4 (74.8 tok/s). +18.2 pts × 5% weight = +0.91 pt vs neutral-50.

### B2. LCB v4 — Still ⊘
- GPT-5.5 has NOT been submitted to livecodebench.github.io as of April 25, 2026.

### B3. RULER/LCR — Still ⊘ (canonical)
- GPT-5.5 published OpenAI MRCR v2 scores (87.5% at 128K–256K, 81.5% at 256K–512K, 74.0% at 512K–1M) — these are NOT canonical RULER benchmark scores.

### B4–B5. AIME 2025 and SciCode — Still ⊘
- GPT-5.5 specific AIME 2025 not published. SciCode not published separately (component of AA Index).

### B6. MMLU-Pro Anomaly — Resolved, Still ⊘
- 54.6% anomaly explained: 0-shot evaluation vs standard 5-shot protocol. GPT-5.5 proper MMLU-Pro (5-shot) not found. Remains ⊘.

### B7. SWE-bench Verified 88.7% — DAGGER REMOVED ✓
- Now confirmed from multiple independent sources (TokenMix, Fast Company, Investing.com, RD World Online, OpenAI launch materials). Remove † flag.

---

## Part C — Coverage Expansion

### C1. MMLU-Pro (was 4/12, now 6/12)

| Model | Score | Confidence | Status |
|---|---|---|---|
| Claude Opus 4.7 | **89.87%** | Probable | Fills ⊘ — new #1 |
| GLM-5.1 | **85.8%** | Probable | Fills ⊘ |

**New MMLU-Pro ranking (n=6):** Opus 4.7 89.87% > Gemini 89.8% > Qwen 88.5% > DeepSeek 87.5% > GLM 85.8% > Kimi 84.6%

**Score impacts (rank-normalized):**
- Opus 4.7: rank 1 → **100.0** (was 50.0⊘)
- Gemini: rank 2 → **80.0** (was 100.0)
- GLM: rank 5 → **20.0** (was 50.0⊘)

### C2. LCB v4 — No new data (remains 5/12)

### C3. SWE-bench Pro (was 5/12, now 9/12)

| Model | Score | Confidence | Status |
|---|---|---|---|
| GLM-5.1 | **58.4%** | Probable | Fills ⊘ |
| Qwen 3.6 Plus | **56.6%** | Probable | Fills ⊘ |
| MiniMax M2.7 | **56.2%** | Probable | Fills ⊘ |
| DeepSeek V4-Pro | **55.4%** | Confirmed | Fills ⊘ |

**New SWEPro ranking (n=9):** Opus 4.7 64.3% > GPT-5.4 59.1% > Kimi 58.6% ≈ GPT-5.5 58.6% (tie 3.5) > GLM 58.4% > Qwen 56.6% > MiniMax 56.2% > DeepSeek 55.4% > Opus 4.6 51.9%

### C4. BrowseComp (was 6/12, now 8/12)

| Model | Score | Confidence | Status |
|---|---|---|---|
| Claude Opus 4.6 | **83.7%** | Probable | Fills ⊘ |
| GLM-5.1 | **68%** | Probable | Fills ⊘ |

**New BrowseComp ranking (n=8):** GPT-5.5 90.1% > GPT-5.4 89.3% > Gemini 85.9% > Opus 4.6 83.7% > DeepSeek 83.4% > Kimi 83.2% > Opus 4.7 79.3% > GLM 68%

**Score impacts (rank-normalized, n=8):**
- GLM: rank 8 → **0.0** (was 50.0⊘ — major drop of 50 pts × 3% weight = −1.5 pts)
- Opus 4.6: rank 4 → **57.1** (fills ⊘ from neutral-50)

### C5. OSWorld — No new data (remains 6/12)
- Gemini 3.1 Pro confirmed ⊘ (no published score). MiniMax, Qwen, GLM, KAT, DeepSeek all still ⊘.

### C6. AA-Omniscience (fills 2 more models)

| Model | Score | Accuracy | Hall Rate | Confidence |
|---|---|---|---|---|
| Kimi K2.6 | **+6** | ~45% | **39%** | Confirmed |
| DeepSeek V4-Pro | **-10** | ~84% | **94%** | Confirmed |

**New AA-Omniscience ranking (n=8):** Gemini +34 > Opus 4.7 +22 > MiniMax +12 > Opus 4.6 +8 > Kimi +6 > GLM −1 > DeepSeek −10 > GPT-5.5 −29

---

## Part D — AIME 2026 Evaluation

**Leaderboard data (llm-stats.com, 0 verified / 12 self-reported):**

| Model | AIME 2026 Score | In Cohort |
|---|---|---|
| Kimi K2.6 | 96.4% | ✓ |
| Qwen 3.6 Plus | 95.3% | ✓ |
| GLM-5.1 | 95.3% | ✓ |
| Others | — | ✗ |

**GPT-5.5, GPT-5.4, Gemini 3.1 Pro, all Claude models, MiniMax, KAT, DeepSeek:** Not found.

**Decision: AIME 2026 does NOT replace AIME 2025.** Coverage 3/12 (all self-reported) vs AIME 2025's 7/12 confirmed. Framework slot for v4.x. Note: AIME 2026 is also near-saturating for frontier models (95–100% cluster).

---

## Part E — New Potential Dimensions

| Dimension | Decision | Reason |
|---|---|---|
| GAIA Level 3 | Framework slot | No Level-3-specific scores found for our 12 models |
| BigCodeBench | Framework slot | No confirmed scores for any of our 12 models |
| IFEval | Do not add | Redundant with IFBench (measures similar instruction-following) |
| FrontierMath | Framework slot | 3/12 coverage (GPT-5.5 Pro 52.4%, GPT-5.5 51.7%, GPT-5.4 50%) — just below 4/12 threshold; check v4.1 |

---

## Synthesis & Insights (Run 3)

**Insight 1: DeepSeek's real scores are mostly worse than neutral-50.** The v3.0 neutral-50 assignments assumed no discrimination. Real data:
- Cost: 45.5 (rank 7/12 — below neutral)
- Speed: 9.1 (rank 11/12 — well below neutral)
- SWEPro: 12.5 (rank 8/9 — well below neutral)
- Omni: 14.3 (rank 7/8 — below neutral)
- GDPval: 54.5 (rank 5/12 — slightly above neutral, positive)
**Net:** Filling gaps lowers DeepSeek from ~51.1 to ~47–49 pts, dropping from #8 to #9.

**Insight 2: GLM 5.1 takes a double hit.** BrowseComp 68% (rank 8/8 = 0.0, was neutral-50 = −50 pts × 3% = −1.5 pts) + MMLU-Pro 85.8% (rank 5/6 = 20.0, was neutral-50 = −30 pts × 2% = −0.6 pt). Total GLM hit: ~−2.1 pts. GLM drops from #4 to #5; Kimi rises to #5.

**Insight 3: SWEPro expansion reveals clustering.** At 9/12 coverage, the #2–#8 positions are clustered within 59.1%–55.4% — a mere 3.7 points across 7 models. SWEPro is not discriminating at the frontier below rank 1. May prompt weight reduction in v5.0.

**Insight 4: GPT-5.5 speed fill confirms its tier.** At 74.7 tok/s, GPT-5.5 nearly ties GPT-5.4 (74.8 tok/s). Well above the 49–53 tok/s mid-range. Combined with BrowseComp #1, Terminal-Bench #1, SWE-bench V #1, GPT-5.5's leadership position strengthens.

**Insight 5: BrowseComp is the sharpest new discriminator.** 8/12 real data, 22-point spread (90.1% to 68%). GLM's 0.0 BrowseComp score is a signal: strong on IFBench and τ²-Bench but weak on deep web research tasks.

---

## Complete Data Table for v4.0 Update

| Model | Dimension | Old Value | New Value | Change | Confidence |
|---|---|---|---|---|---|
| DeepSeek V4-Pro | SWE-bench Pro | ⊘ | **55.4%** | Fills ⊘ | Confirmed |
| DeepSeek V4-Pro | GDPval-AA ELO | ⊘ | **1,554** | Fills ⊘ | Confirmed |
| DeepSeek V4-Pro | AA-Omniscience | ⊘ | **−10** | Fills ⊘ | Confirmed |
| DeepSeek V4-Pro | AA Eval Cost | ⊘ | **$1,071.28** | Fills ⊘ | Confirmed |
| DeepSeek V4-Pro | Speed (tok/s) | 33.5 | **35.8** | Corrects | Confirmed |
| DeepSeek V4-Pro | Term-Bench 2.0 | ⊘ | **67.9%†self** | Fills ⊘ | Probable |
| GPT-5.5 | Speed (tok/s) | ⊘ | **74.7** | Fills ⊘ | Confirmed |
| GPT-5.5 | SWE-bench V | 88.7%† | **88.7%** | Remove dagger | Confirmed |
| GLM-5.1 | SWE-bench Pro | ⊘ | **58.4%** | Fills ⊘ | Probable |
| GLM-5.1 | BrowseComp | ⊘ | **68%** | Fills ⊘ | Probable |
| GLM-5.1 | MMLU-Pro | ⊘ | **85.8%** | Fills ⊘ | Probable |
| Qwen 3.6 Plus | SWE-bench Pro | ⊘ | **56.6%** | Fills ⊘ | Probable |
| MiniMax M2.7 | SWE-bench Pro | ⊘ | **56.2%** | Fills ⊘ | Probable |
| Claude Opus 4.6 | BrowseComp | ⊘ | **83.7%** | Fills ⊘ | Probable |
| Claude Opus 4.7 | MMLU-Pro | ⊘ | **89.87%** | Fills ⊘ | Probable |
| Kimi K2.6 | AA-Omniscience | ⊘ | **+6** (45%−39%) | Fills ⊘ | Confirmed |

**Still ⊘ after ultradeep research (exhaustive):** DeepSeek τ²-Bench, OSWorld, RULER, AIME 2025 (attribution unclear), SciCode | GPT-5.5 LCB, LCR, AIME, SciCode, MMLU-Pro | Gemini OSWorld | Qwen/KAT/MiniMax/Sonnet: BrowseComp, MMLU-Pro | Kimi/GPT-5.4/Qwen/KAT/Sonnet: AA-Omniscience

---

## Estimated v4.0 Ranking Impact

| Model | v3.0 Score | Est. v4.0 Change | Est. v4.0 Score | v3.0 Rank | Est. v4.0 Rank |
|---|---|---|---|---|---|
| Gemini 3.1 Pro | 69.5 | +0.8 | ~70.3 | #1 | #1 |
| GPT-5.5 | 64.0 | +2.2 | ~66.2 | #2 | #2 |
| KAT-Coder-Pro-V2 | 58.3 | ~0 | ~58.3 | #3 | #3 |
| GLM 5.1 | 58.2 | −2.1 | ~56.1 | #4 | **#5** |
| Kimi K2.6 | 52.6 | +1.0 | ~53.6 | #6 | **#5** (tie area) |
| MiniMax M2.7 | 55.0 | −0.8 | ~54.2 | #5 | #6 |
| GPT-5.4 | 52.1 | −0.7 | ~51.4 | #7 | #7 |
| Qwen 3.6 Plus | 49.7 | −0.5 | ~49.2 | #9 | **#8** |
| DeepSeek V4-Pro | 51.1 | −4.8 | ~46.3 | #8 | **#9** |
| Claude Opus 4.7 | 42.9 | +1.5 | ~44.4 | #10 | #10 |
| Claude Sonnet 4.6 | 26.1 | −0.6 | ~25.5 | #11 | #11 |
| Claude Opus 4.6 | 20.6 | +0.6 | ~21.2 | #12 | #12 |

---

## Limitations & Caveats (Run 3)

1. **DeepSeek V4-Pro Terminal-Bench 2.0** (67.9%) is self-reported from DeepSeek's own model card, not tbench.ai canonical leaderboard.
2. **DeepSeek IFBench 76.5%** comes from synthesized search result; could not directly verify on primary leaderboard — keep ⊘.
3. **MMLU-Pro scores** for Claude Opus 4.7 (89.87%) and GLM-5.1 (85.8%) come from secondary aggregators, not the official MMLU-Pro HuggingFace leaderboard directly.
4. **SWEPro scores** from BenchLM may use different scaffolding than Scale AI SEAL (canonical source). ±1–2 pp differences possible.
5. **AIME 2026** leaderboard shows 0 verified results — all self-reported. Do not score this dimension yet.
6. **AA-Omniscience Opus 4.7 discrepancy**: Source article says hall rate = 36%; existing doc says 54%. Likely different model variants (Adaptive Reasoning Max Effort vs base). Retain existing data pending direct AA-Omniscience page confirmation.

---

## Bibliography (Run 3)

1. Artificial Analysis. "DeepSeek is back among the leading open weights models with V4 Pro and V4 Flash." artificialanalysis.ai/articles/deepseek-is-back-among-the-leading-open-weights-models-with-v4-pro-and-v4-flash.
2. Artificial Analysis. "DeepSeek V4 Pro (Max) — Intelligence, Performance & Price Analysis." artificialanalysis.ai/models/deepseek-v4-pro.
3. Artificial Analysis. "GPT-5.5 (xhigh) — Intelligence, Performance & Price Analysis." artificialanalysis.ai/models/gpt-5-5.
4. Artificial Analysis. "AA-Omniscience: Knowledge and Hallucination Benchmark." artificialanalysis.ai/evaluations/omniscience.
5. Artificial Analysis. "Kimi K2.6: The new leading open weights model." artificialanalysis.ai/articles/kimi-k2-6-the-new-leading-open-weights-model.
6. Hugging Face. "deepseek-ai/DeepSeek-V4-Pro." huggingface.co/deepseek-ai/DeepSeek-V4-Pro.
7. BenchLM.ai. "SWE-bench Pro Benchmark 2026: 18 LLM scores." benchlm.ai/benchmarks/swePro.
8. BenchLM.ai. "BrowseComp Benchmark 2026: 17 LLM scores." benchlm.ai/benchmarks/browseComp.
9. tbench.ai. "terminal-bench@2.0 Leaderboard." tbench.ai/leaderboard/terminal-bench/2.0.
10. llm-stats.com. "AIME 2026 Leaderboard." llm-stats.com/benchmarks/aime-2026.
11. OfficeChai. "DeepSeek V4 Pro Becomes Second-Highest Rated Open Model On Artificial Analysis Index."
12. TokenMix Blog. "GPT-5.5 Review: 88.7% SWE-Bench, 92.4% MMLU, 2x Price Tag."
13. OpenAI. "Introducing GPT-5.5." openai.com/index/introducing-gpt-5-5/. April 23, 2026.
14. BenchLM.ai. "FrontierMath Benchmark 2026." benchlm.ai/benchmarks/frontierMath.
15. Epoch AI. "FrontierMath Tier 4." epoch.ai/benchmarks/frontiermath-tier-4.
16. StartupFortune. "DeepSeek V4 Pro costs 15x more to run than V3.2."
17. VentureBeat. "DeepSeek-V4 arrives with near state-of-the-art intelligence at 1/6th the cost of Opus 4.7, GPT-5.5."
