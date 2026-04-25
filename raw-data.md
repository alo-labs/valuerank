# ValueRank — Raw Data
**Source of truth for all benchmark scores | Updated every version**

← [README](README.md) · [Methodology](methodology.md) · [Scores](scores.md)

---

## 4. Cost Analysis

### 4.1 Artificial Analysis Index Eval Cost (Total USD to Run AA Benchmark Suite)

| Model | AA Index Eval Cost | vs. Cheapest |
|---|---|---|
| **Gemma 3 27B** | **$0.00** | **0.0× (free)** |
| **Phi-4** | **$4.27** | **—** |
| **Llama 4 Scout** | **$26.42** | **—** |
| **Mistral Large 3** | **$38.67** | **—** |
| **Llama 4 Maverick** | **$62.28** | **—** |
| KAT-Coder-Pro-V2 | $73.49 | 1.0× (cheapest paid) |
| MiniMax M2.7 | $175.51 | 2.4× |
| **Amazon Nova Pro** | **$200.98** | **2.7×** |
| **Grok 3** | **$311.71** | **4.2×** |
| **o3-mini (high)** | **$314.72** | **4.3×** |
| Qwen 3.6 Plus | $482.65 | 6.6× |
| GLM 5.1 | $543.95 | 7.4× |
| Gemini 3.1 Pro | $892.28 | 12.1× |
| Kimi K2.6 | $947.87 | 12.9× |
| DeepSeek V4-Pro | $1,071.28 | 14.6× |
| GPT-5.4 | $2,851.01 | 38.8× |
| GPT-5.5 | $3,357.00 | 45.7× |
| Claude Sonnet 4.6 | $3,959.36 | 53.9× |
| Claude Opus 4.7 | $4,811.04 | 65.5× |
| Claude Opus 4.6 | $4,969.68 | 67.6× |

> **What is AA Index Eval Cost?** Artificial Analysis runs each model through its full standardized Intelligence Index benchmark suite and records the actual total USD spent — API price × real token consumption across all tasks. This is the only publicly available, standardized, usage-weighted cost dataset for frontier models. Unlike raw $/1M token pricing, eval cost captures true user cost: a verbose model that uses 10× more tokens costs 10× more even at the same token price. Source: artificialanalysis.ai Intelligence Index.
> **Why not per-token API pricing?** Per-token pricing ($/1M input + $/1M output) ignores verbosity: a model priced at $3/1M tokens that generates 4× as many tokens per task has an effective task cost of $12/1M — more expensive than a $10/1M model that answers correctly in one concise pass. Reasoning models amplify this problem: the "Price of Progress" literature (arXiv:2511.23455) documents that frontier-level *total* costs have risen 3–18× per year even as per-token prices fall, because reasoning-mode token counts dominate spend. AA Eval Cost captures the full price-times-tokens picture by measuring what it actually costs to run a standardized benchmark suite end-to-end. This is why ValueRank switched from raw API pricing to AA Eval Cost in v2.5 — it produced dramatically different rankings (e.g., GPT-5.5 moved from rank 11 by per-token list price to rank 9 by eval cost, because its reasoning throughput per task is more efficient than Anthropic's Opus models despite similar headline prices).
> **v5.0 note (Gemma 3 27B $0.00):** Google offers Gemma 3 27B free via the OpenRouter free tier; Artificial Analysis evaluated it at $0.00. This is a legitimate AA-confirmed eval cost, not missing data. The five sub-$65 models (Gemma3, Phi-4, Scout, ML3, Maverick) dominate cost ranks 1–5, dramatically compressing the cost scores of all previously ranked models — KAT-Coder-Pro-V2 drops from rank 1 (100.0) to rank 6 (73.7) with n=20.

### 4.2 Cost Efficiency Tier Summary

| Tier | Models | AA Eval Cost Range |
|---|---|---|
| **Free** | **Gemma 3 27B** | **$0.00** |
| **Ultra-Budget** | **Phi-4, Llama 4 Scout, Mistral Large 3, Llama 4 Maverick** | **$4–$62** |
| Budget | KAT-Coder-Pro-V2 | $73 |
| Near-Budget | MiniMax M2.7, **Amazon Nova Pro** | $176–$201 |
| **Value** | **Grok 3, o3-mini (high)** | **$312–$315** |
| Mid-Range | Qwen 3.6 Plus, GLM 5.1 | $483–$544 |
| Premium | Gemini 3.1 Pro, Kimi K2.6, DeepSeek V4-Pro | $892–$1,071 |
| Expensive | GPT-5.4 | $2,851 |
| Very Expensive | GPT-5.5, Claude Sonnet 4.6 | $3,357–$3,959 |
| Ultra-Premium | Claude Opus 4.7, Claude Opus 4.6 | $4,811–$4,970 |

---

## 5. Raw Benchmark Data

### 5.1 Quality Benchmarks

| Model | IFBench | Term-Bench 2.0 | SWE-Bench V | SWE-Pro | LCB v4 | GDPval ELO | τ²-Bench | OSWorld | RULER (LCR)‡ | HLE | GPQA◇ | AIME 2025 | SciCode |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gemini 3.1 Pro | 89.4% | 68.5% | 80.6% | ⊘ | 76.3% | 1,314 | 99.3% | ⊘ | 94.2%‡ | 44.7% | 94.3% | 95.0% | 58.9% |
| Kimi K2.6 | 82.1% | 66.7% | 80.2% | 58.6% | 82.6% | 1,520 | 96.0% | 73.1% | 87.5%‡ | 34.7% | 90.5% | 96.1% | 52.2% |
| MiniMax M2.7 | 75.7% | 57.0% | ⊘ | 56.2%~ | ⊘ | 1,514 | 84.8% | ⊘ | 81.3%‡ | 28.1% | 87.4% | ⊘ | 47.0% |
| GPT-5.4 | 73.9% | 75.1% | ⊘ | 59.1% | 63.8% | 1,674 | 87.1% | 75.0% | 97.8%‡ | 41.6% | 92.0% | ⊘ | 56.6% |
| Qwen 3.6 Plus | 74.2% | 61.6% | 78.8% | 56.6%~ | ⊘ | 1,361 | 78.2% | ⊘ | 87.5%‡ | 28.8% | 90.4% | ⊘ | 21.4% |
| KAT-Coder-Pro-V2 | 67.0% | 76.2%† | 79.6% | ⊘ | ⊘ | 1,124 | 93.9% | ⊘ | 74.6%‡ | 12.7% | 85.5% | ⊘ | 38.3% |
| GLM 5.1 | 85.9% | 69.0% | 77.8% | 58.4%~ | ⊘ | 1,535 | 97.7% | ⊘ | 68.3%‡ | 31.0% | 86.2% | 95.0% | 43.8% |
| Claude Opus 4.7 | 52.1% | 69.4% | 87.6% | 64.3% | ⊘ | 1,753 | 74.0% | 78.0% | 92.4%‡ | 46.9% | 94.2% | 99.8% | 54.5% |
| GPT-5.5 | 75.9% | 82.7% | 88.7% | 58.6% | ⊘ | 1,784 | 98.0% | 78.7% | ⊘ | 44.3% | 93.6% | ⊘ | ⊘ |
| Claude Sonnet 4.6 | 45.6% | 59.1% | 79.6% | ⊘ | ⊘ | 1,675 | 79.5% | 72.5% | 61.2%‡ | 30.0% | 87.5% | 57.1% | 46.9% |
| Claude Opus 4.6 | 40.2% | 65.4% | 80.8% | 51.9% | 76.0% | 1,619 | 84.8% | 72.7% | 54.7%‡ | 40.0% | 84.0% | 99.8% | 51.9% |
| DeepSeek V4-Pro | ⊘ | 67.9%†self | 80.6% | 55.4% | 93.5% | 1,554 | ⊘ | ⊘ | ⊘ | 37.7% | 88.8% | ⊘ | ⊘ |
| **Gemma 3 27B** | **⊘** | **⊘** | **⊘** | **⊘** | **⊘** | **⊘** | **⊘** | **⊘** | **⊘** | **⊘** | **42.4%** | **⊘** | **⊘** |
| **Phi-4** | **⊘** | **⊘** | **⊘** | **⊘** | **⊘** | **⊘** | **⊘** | **⊘** | **⊘** | **⊘** | **⊘** | **⊘** | **⊘** |
| **Llama 4 Scout** | **39.5%** | **⊘** | **⊘** | **⊘** | **32.8%~** | **⊘** | **⊘** | **⊘** | **⊘** | **4.3%** | **58.7%** | **⊘** | **17.0%** |
| **Mistral Large 3** | **⊘** | **⊘** | **⊘** | **⊘** | **82.8%~** | **⊘** | **⊘** | **⊘** | **⊘** | **⊘** | **43.9%** | **⊘** | **⊘** |
| **Llama 4 Maverick** | **43.0%** | **⊘** | **⊘** | **⊘** | **43.4%~** | **⊘** | **⊘** | **⊘** | **⊘** | **4.8%** | **67.1%** | **⊘** | **33.1%** |
| **Amazon Nova Pro** | **⊘** | **⊘** | **⊘** | **⊘** | **⊘** | **⊘** | **⊘** | **⊘** | **⊘** | **⊘** | **⊘** | **⊘** | **⊘** |
| **Grok 3** | **⊘** | **⊘** | **⊘** | **⊘** | **79.4%~** | **⊘** | **⊘** | **⊘** | **⊘** | **⊘** | **84.6%~** | **⊘** | **⊘** |
| **o3-mini (high)** | **67.1%** | **6.1%** | **⊘** | **⊘** | **71.7%~** | **⊘** | **28.7%~** | **⊘** | **⊘** | **12.3%** | **77.3%** | **77.0%** | **39.8%** |

> **† Footnotes:** KAT-Coder-Pro-V2 TB 2.0 (76.2%†) is not on the public tbench.ai leaderboard; value from KAT technical report referencing "Terminal-Bench Hard" — potentially different variant. DeepSeek V4-Pro TB 2.0 (67.9%†self) is from DeepSeek's own model card on HuggingFace — confirmed absent from canonical tbench.ai leaderboard as of April 25, 2026. Both marked †/†self. GPT-5.5 SWE-bench Verified (88.7%) confirmed by multiple independent sources (OpenAI tech card + TokenMix, Fast Company, Investing.com, RD World Online).
> **v4.3 corrections (carried forward):** (1) **Kimi K2.6 τ²-Bench corrected 72.4%→96.0%** — primary source: AA article "Kimi K2.6: The new leading open weights model." (2) **GPT-5.5 LCB reverted to ⊘** — pricepertoken.com confirms 91.7% belongs to Gemini 3 Pro Preview, not GPT-5.5. (3) **DeepSeek V4-Pro hallucination rate 94% confirmed** — no score change.
> **v5.0 new model LCB footnote:** LCB scores for Llama 4 Scout (32.8%), Llama 4 Maverick (43.4%), o3-mini (71.7%), Grok 3 (79.4%), Mistral Large 3 (82.8%) are all marked ~ (provisional) — version ambiguity: these models were evaluated after April 2025 and may use LCBv5 or LCBv6 rather than the canonical LCBv4. Scores are included in the LCB dimension with ~ notation; treated as comparable pending confirmation on the canonical livecodebench.github.io leaderboard.
> **v5.0 Grok 3 footnote:** GPQA 84.6%~ and LCB 79.4%~ found in secondary sources; these figures may reflect Grok 3 Think (reasoning mode) rather than standard Grok 3. Marked ~ until confirmed on canonical leaderboards.
> **‡ RULER (LCR) footnote:** No model in this cohort was found on any public RULER leaderboard as of 2026-04-26. Values drawn from model cards and internal evaluation documents; none confirmed against ruler-bench.github.io or llm-stats leaderboards. RULER scores should be treated as provisional.
> **~ footnote (SWE-Pro):** SWE-Pro scores for GLM (58.4%), Qwen (56.6%), MiniMax (56.2%) from BenchLM.ai leaderboard — probable confidence. DeepSeek SWE-Pro 55.4% confirmed on HuggingFace model card + BenchLM.
> **Bold** = v5.0 new model data.

### 5.2 New Scored Dimensions (v3.0)

| Model | BrowseComp | MMLU-Pro |
|---|---|---|
| Gemini 3.1 Pro | 85.9% | 89.8% |
| Kimi K2.6 | 83.2% | 84.6% |
| MiniMax M2.7 | ⊘ | ⊘ |
| GPT-5.4 | 89.3% | ⊘ |
| Qwen 3.6 Plus | ⊘ | 88.5% |
| KAT-Coder-Pro-V2 | ⊘ | ⊘ |
| GLM 5.1 | 68%~ | 85.8%~ |
| Claude Opus 4.7 | 79.3% | 89.87%~ |
| GPT-5.5 | 90.1% | ⊘* |
| Claude Sonnet 4.6 | ⊘ | ⊘ |
| Claude Opus 4.6 | 83.7%~ | ⊘ |
| DeepSeek V4-Pro | 83.4% | 87.5% |
| **Gemma 3 27B** | **⊘** | **⊘** |
| **Phi-4** | **⊘** | **⊘** |
| **Llama 4 Scout** | **⊘** | **74.3%** |
| **Mistral Large 3** | **⊘** | **⊘** |
| **Llama 4 Maverick** | **⊘** | **80.5%** |
| **Amazon Nova Pro** | **⊘** | **⊘** |
| **Grok 3** | **⊘** | **⊘** |
| **o3-mini (high)** | **⊘** | **79.1%** |

> *GPT-5.5 MMLU-Pro = 54.6% seen in one source — anomalously low vs. frontier cluster (84–92%), likely 0-shot vs. few-shot methodology difference. Treated as ⊘ (unreliable) for scoring.
> **~ footnote:** GLM BrowseComp (68%), GLM MMLU-Pro (85.8%), Claude Opus 4.6 BrowseComp (83.7%) sourced from BenchLM.ai — probable confidence. Claude Opus 4.7 MMLU-Pro (89.87%) sourced from aggregator leaderboard — probable confidence, #1 in cohort above Gemini 89.8%.
> **Bold** = v5.0 new model data.

### 5.3 Composite / Special Dimensions

| Model | AA-Omniscience (Acc% − Hall%) | Speed (tok/s) | AA Index Eval Cost ($) | AA Intelligence Index |
|---|---|---|---|---|
| Gemini 3.1 Pro | +34 (82% acc − 48% hall) | 128.0 | $892.28 | 57 |
| Kimi K2.6 | +6 (45% acc − 39% hall) | 100.4 | $947.87 | 54~ |
| MiniMax M2.7 | +12 (71% acc − 59% hall) | 49.0 | $175.51 | ⊘ |
| GPT-5.4 | ⊘ | 74.8 | $2,851.01 | 57 |
| Qwen 3.6 Plus | ⊘ | 53.0 | $482.65 | ⊘ |
| KAT-Coder-Pro-V2 | ⊘ | 113.5 | $73.49 | ⊘ |
| GLM 5.1 | −1 (64% acc − 65% hall) | 49.0 | $543.95 | ⊘ |
| Claude Opus 4.7 | +22 (76% acc − 54% hall) | 42.0 | $4,811.04 | 57 |
| GPT-5.5 | −29 (57% acc − 86% hall) | 74.7 | $3,357.00 | 60† |
| Claude Sonnet 4.6 | ⊘ | 46.0 | $3,959.36 | ⊘ |
| Claude Opus 4.6 | +8 (68% acc − 60% hall) | 18.2 | $4,969.68 | ⊘ |
| DeepSeek V4-Pro | −10 (84% acc − 94% hall) | 35.8 | $1,071.28 | ⊘ |
| **Gemma 3 27B** | **⊘** | **24.6** | **$0.00** | **10** |
| **Phi-4** | **⊘** | **34.2** | **$4.27** | **10** |
| **Llama 4 Scout** | **⊘** | **142.5** | **$26.42** | **⊘** |
| **Mistral Large 3** | **⊘** | **49.8** | **$38.67** | **23** |
| **Llama 4 Maverick** | **⊘** | **111.0** | **$62.28** | **⊘** |
| **Amazon Nova Pro** | **⊘** | **⊘** | **$200.98** | **13** |
| **Grok 3** | **⊘** | **71.6** | **$311.71** | **⊘** |
| **o3-mini (high)** | **⊘** | **131.7** | **$314.72** | **⊘** |

> **AA-Omniscience note (GPT-5.5):** Despite being rated #1 on the AA Intelligence Index v4.0 (score 60 xhigh), GPT-5.5's AA-Omniscience score is −29, the worst of all models with real data. This reflects an 86% hallucination rate at high-confidence assertions — a known characteristic of the xhigh reasoning mode that prioritizes bold inference over calibrated uncertainty.
> **AA-Omniscience note (DeepSeek V4-Pro):** 94% hallucination rate — when the model doesn't know an answer it responds anyway in 94% of cases. An 11-point improvement over DeepSeek V3.2 (−21). Source: Artificial Analysis article "DeepSeek is back among the leading open weights models." Kimi K2.6 +6 score (39% hall rate) confirms by Artificial Analysis Omniscience data.
> **Speed note (GPT-5.5):** 74.7 tok/s is the xhigh reasoning mode throughput (primary scoring configuration). GPT-5.5 (high) = 81.9 tok/s. Source: artificialanalysis.ai/models/gpt-5-5. DeepSeek speed corrected from 33.5 to 35.8 tok/s (same source, updated measurement).
> **AA Intelligence Index note:** Artificial Analysis's composite benchmark score (equal-weighted across Coding, Reasoning, Language, Math at 25% each; 10 benchmarks total; cost explicitly excluded). † GPT-5.5 score 60 is for xhigh reasoning mode; high mode = 59 (source: artificialanalysis.ai/models/gpt-5-5). ~ Kimi K2.6 score 54 is from a multi-AI aggregated research report (April 26, 2026; 6 sources); not yet confirmed on the canonical AA leaderboard. The 5 known scores (4 AA-confirmed + Kimi~) span a compressed 54–60 band — masking the wide ValueRank spread of 20.6–70.0. This compression confirms that quality-only composites do not adequately differentiate production value when cost is ignored. ⊘ = score not confirmed from AA leaderboard for this cohort model as of April 26, 2026.

---

## 6. Speed & Latency Reference Data

### 6.1 Inference Speed (tok/s) — Scored Dimension

| Model | Output tok/s | Notes |
|---|---|---|
| **Llama 4 Scout** | **142.5** | **Fastest in field; MoE architecture with sparse activation** |
| **o3-mini (high)** | **131.7** | **High for a reasoning model; second fastest overall** |
| Gemini 3.1 Pro | 128.0 | Third fastest; TPU infrastructure advantage |
| KAT-Coder-Pro-V2 | 113.5 | Fourth fastest; specialized decode path |
| **Llama 4 Maverick** | **111.0** | **Fifth fastest; large MoE with efficient decode** |
| Kimi K2.6 | 100.4 | Sixth fastest |
| GPT-5.4 | 74.8 | Moderate throughput; confirmed by AA leaderboard |
| GPT-5.5 | 74.7 | xhigh reasoning mode; near-tied with GPT-5.4; high for a reasoning model |
| **Grok 3** | **71.6** | **Moderate; confirmed by AA leaderboard** |
| Qwen 3.6 Plus | 53.0 | Mid-range |
| **Mistral Large 3** | **49.8** | **Mid-range; confirmed by AA leaderboard** |
| MiniMax M2.7 | 49.0 | Budget tier; tied with GLM |
| GLM 5.1 | 49.0 | Tied with MiniMax |
| Claude Sonnet 4.6 | 46.0 | Moderate |
| Claude Opus 4.7 | 42.0 | Constrained by 200K context |
| DeepSeek V4-Pro | 35.8 | Below open-weight median; 1.6T MoE routing overhead |
| **Phi-4** | **34.2** | **Compact model; constrained by smaller parameter count** |
| **Gemma 3 27B** | **24.6** | **Small model; low throughput despite compact size** |
| Claude Opus 4.6 | 18.2 | Slowest with real data |
| **Amazon Nova Pro** | **⊘** | **Not published** |

### 6.2 Time-to-First-Token (TTFT) — Reference Only, Not Scored

| Model | TTFT (ms) | Mode | Notes |
|---|---|---|---|
| Claude Sonnet 4.6 | ~1,420 | Non-reasoning | Fast initial response |
| Kimi K2.6 | ~2,100 | Standard | Consistent |
| MiniMax M2.7 | ~2,400 | Standard | Budget model; acceptable |
| Gemini 3.1 Pro | ~3,800 | Think mode | Includes partial reasoning warmup |
| GPT-5.4 | ~4,200 | Standard | Moderate |
| Qwen 3.6 Plus | ~5,100 | Thinking mode | |
| GLM 5.1 | ~6,300 | Standard | Slower architecture |
| Claude Opus 4.7 | ~8,900 | Extended thinking | |
| Claude Opus 4.6 | ~9,200 | Extended thinking | |
| DeepSeek V4-Pro | ~6,800 | Reasoning mode | Estimated; MoE warmup overhead |
| GPT-5.5 | ~172,720 | xhigh reasoning | Full CoT included; not comparable to above |
| KAT-Coder-Pro-V2 | ⊘ | n/a | Not published |

> **Why TTFT is excluded from scoring:** At xhigh, GPT-5.5's TTFT encompasses the entire chain-of-thought computation. Comparing 172,720 ms (GPT-5.5 xhigh) to 1,420 ms (Claude Sonnet) would penalize reasoning models for their reasoning — a category error. Speed (tok/s) is the only throughput dimension scored, as it measures a comparable post-generation metric across all modes.
