# ValueRank
**Frontier AI model ranking — 20 models × 18 dimensions, rank-based normalization**

**Version 5.0 | April 26, 2026**

---

## Documents

| File | Description | Update freq |
|---|---|---|
| [`scores.md`](scores.md) | Normalized matrix, quality ranking, final ranking, version history | Every version |
| [`raw-data.md`](raw-data.md) | All raw benchmark scores, cost data, speed data | Every version |
| [`profiles.md`](profiles.md) | Per-model analysis (all 12) | Per version |
| [`insights.md`](insights.md) | Strategic insights, Pareto analysis, use case matrix | Per version |
| [`limitations.md`](limitations.md) | Known gaps, data conflicts, benchmark reference index | Per version |
| [`methodology.md`](methodology.md) | Formula, weights, protocols, appendix — stable reference | Rarely |
| [`research.md`](research.md) | Primary research evidence — 3 research runs sourcing every data point | Archival |

---

## Ranking Snapshot (v5.0, April 26, 2026)

| Rank | Model | Score | Quality | Cost Tier | Developer |
|---|---|---|---|---|---|
| 🥇 1 | **Gemini 3.1 Pro** | **64.3** | #1 | Premium ($892) | Google DeepMind |
| 🥈 2 | **GPT-5.5** | **63.7** | #2 | Very Expensive ($3,357) | OpenAI |
| 🥉 3 | **Mistral Large 3** | **59.7** | #9 | Ultra-Budget ($39) | Mistral AI |
| 4 | **Gemma 3 27B** | **59.3** | #13 | Free ($0) | Google DeepMind |
| 5 | **Phi-4** | **59.2** | #10 | Ultra-Budget ($4) | Microsoft |
| 6 | Kimi K2.6 | 54.3 | #5 | Premium ($948) | Moonshot AI |
| 7 | KAT-Coder-Pro-V2 | 54.0 | #11 | Budget ($73) | Kay (alo-exp) |
| 8 | **Amazon Nova Pro** | **53.3** | #7 | Near-Budget ($201) | Amazon |
| 9 | **Grok 3** | **53.0** | #6 | Value ($312) | xAI |
| 10 | GPT-5.4 | 52.2 | #4 | Expensive ($2,851) | OpenAI |
| 11 | MiniMax M2.7 | 51.4 | #12 | Near-Budget ($176) | MiniMax |
| 12 | GLM 5.1 | 51.3 | #14 | Mid-Range ($544) | Zhipu AI |
| 13 | **Llama 4 Maverick** | **47.7** | #17 | Ultra-Budget ($62) | Meta |
| 14 | **Llama 4 Scout** | **47.1** | #20 | Ultra-Budget ($26) | Meta |
| 15 | Claude Opus 4.7 | 45.8 | #3 | Ultra-Premium ($4,811) | Anthropic |
| 16 | DeepSeek V4-Pro | 45.2 | #8 | Premium ($1,071) | DeepSeek |
| 17 | Qwen 3.6 Plus | 43.8 | #15 | Mid-Range ($483) | Alibaba |
| 18 | **o3-mini (high)** | **42.7** | #18 | Value ($315) | OpenAI |
| 19 | Claude Sonnet 4.6 | 27.4 | #19 | Very Expensive ($3,959) | Anthropic |
| 20 | Claude Opus 4.6 | 24.7 | #16 | Ultra-Premium ($4,970) | Anthropic |

> **Bold** = v5.0 new entrant. Scores within 2–3 pts are effectively tied per SEAL CI. Ranks 3–5 (ML3/Gemma3/Phi-4, scores 59.7–59.2) are statistically tied — cost arbitrage entries with 14–16 ⊘ dims (ML3=14, Gemma3=15, Phi-4=16). Nova Pro (#8) has 17 of 18 dims ⊘ — cost-only placement. ~ notation on LCB for 5 new entrants (version ambiguity). See [scores.md §10](scores.md#10-ranking-changes-v40--v43--v50) for full version history.

---

## Executive Summary

This report ranks 20 frontier AI models across 18 dimensions — 15 quality benchmarks plus cost efficiency, inference speed (tok/s), and task-level reliability — using rank-based normalization with a 25% cost weight. The framework is designed to reflect the total value equation for production software engineering teams: raw capability matters, but so does price, throughput, and reliability at scale.

**v5.0 Headline Finding (20-model expansion — 8 new entrants):** Adding 8 models expands the cost range from $73–$4,970 to $0–$4,970, triggering a massive cost score compression for all existing models. Five ultra-cheap entrants (Gemma3 $0, Phi-4 $4, Scout $26, ML3 $39, Maverick $62) dominate cost ranks 1–5, pushing KAT-Coder-Pro-V2 from rank 1 (100.0) to rank 6 (73.7). The result: **cost arbitrage entries ML3/Gemma3/Phi-4 debut at ranks #3–#5** (scores 59.7–59.2, statistically tied) despite 14–16 ⊘ dims each (ML3=14, Gemma3=15, Phi-4=16) — a direct consequence of the 25% cost weight and neutral-50 convention for missing data. **Existing models that score above neutral on quality gain from pool expansions:** GPT-5.4 gains +0.3 pts (LCB 0.0→22.2); Opus 4.7 gains +1.9 pts; Sonnet +2.3 pts; Opus 4.6 +4.2 pts (LCB 25.0→44.4). **Existing models near neutral on quality lose from cost compression alone:** GLM falls #5→#12 (−5.4 pts); KAT falls #3→#7 (−4.0 pts); Qwen falls #8→#17 (−4.8 pts).

**v4.3 corrections (carried forward):** Kimi K2.6 τ²-Bench corrected 72.4%→96.0% (primary source confirmed); GPT-5.5 LCB reverted to ⊘ (misattribution resolved). All ~ markers removed from v4.3 scores before v5.0 expansion.

**Top 10 (v5.0):**
1. 🥇 **Gemini 3.1 Pro** — 64.3 pts (#1 overall; quality #1; −6.3 from cost compression; #1 IFBench, τ², GPQA, Sci, Omni)
2. 🥈 **GPT-5.5** — 63.7 pts (#2 overall; quality #2; −1.5 pts; #1 Terminal, SWE-V, OSWorld, BrowseComp)
3. 🥉 **Mistral Large 3** — 59.7 pts (new; LCB rank 2/10 at 82.8%~; cost $39; 14 quality dims ⊘)
4. **Gemma 3 27B** — 59.3 pts (new; $0.00 free tier; GPQA and Speed confirmed; 15 dims ⊘)
5. **Phi-4** — 59.2 pts (new; $4.27; only Speed confirmed below neutral; 16 dims ⊘)
6. **Kimi K2.6** — 54.3 pts (↓ from #4; −3.3 pts from cost compression; quality #5)
7. **KAT-Coder-Pro-V2** — 54.0 pts (↓ from #3; −4.0 pts; #2 Terminal-Bench; cost rank 6/20)
8. **Amazon Nova Pro** — 53.3 pts (new; 17 of 18 dims ⊘; cost-only placement at $201)
9. **Grok 3** — 53.0 pts (new; LCB 66.7~, Speed 55.6; GPQA 35.3~ below neutral)
10. **GPT-5.4** — 52.2 pts (↓ from #7; +0.3 pts; LCB 0.0→22.2 from pool expansion; quality #4)

---

## Model Inventory

| # | Model | Provider | Release | Context | Primary Tier |
|---|---|---|---|---|---|
| 1 | Gemini 3.1 Pro | Google DeepMind | 2026-02 | 2M tokens | Frontier |
| 2 | GPT-5.5 | OpenAI | 2026-04-23 | 512K tokens | Frontier |
| 3 | Mistral Large 3 | Mistral AI | 2025-11 | 128K tokens | Frontier |
| 4 | Gemma 3 27B | Google DeepMind | 2025-03 | 128K tokens | Open (free tier) |
| 5 | Phi-4 | Microsoft | 2024-12 | 16K tokens | Compact |
| 6 | Kimi K2.6 | Moonshot AI | 2026-01 | 200K tokens | Frontier |
| 7 | KAT-Coder-Pro-V2 | KAT AI | 2026-01 | 64K tokens | Specialist |
| 8 | Amazon Nova Pro | Amazon | 2024-12 | 300K tokens | Frontier |
| 9 | Grok 3 | xAI | 2025-02 | 131K tokens | Frontier |
| 10 | GPT-5.4 | OpenAI | 2026-03 | 256K tokens | Frontier |
| 11 | MiniMax M2.7 | MiniMax | 2026-02 | 1M tokens | Frontier |
| 12 | GLM 5.1 | Zhipu AI | 2026-01 | 128K tokens | Frontier |
| 13 | Llama 4 Maverick | Meta | 2025-04 | 1M tokens | Frontier (OSS) |
| 14 | Llama 4 Scout | Meta | 2025-04 | 10M tokens | Open (OSS) |
| 15 | Claude Opus 4.7 | Anthropic | 2026-03 | 200K tokens | Frontier |
| 16 | DeepSeek V4-Pro | DeepSeek | 2026-04-24 | 1M tokens | Frontier (OSS) |
| 17 | Qwen 3.6 Plus | Alibaba | 2026-02 | 128K tokens | Frontier |
| 18 | o3-mini (high) | OpenAI | 2025-01 | 200K tokens | Reasoning |
| 19 | Claude Sonnet 4.6 | Anthropic | 2026-02 | 200K tokens | Frontier |
| 20 | Claude Opus 4.6 | Anthropic | 2025-11 | 200K tokens | Frontier |

---

## Methodology (summary)

- **Formula:** `((n − rank) / (n − 1)) × 100` per dimension; n = models with real data. Missing = neutral-50 (⊘). Tied ranks averaged.
- **Dimensions (18):** Cost, IFBench, Terminal-Bench 2.0, SWE-bench V, SWE-bench Pro, LCB v4, GDPval-AA ELO, Speed, τ²-Bench, OSWorld, BrowseComp, RULER/LCR, HLE, GPQA Diamond, MMLU-Pro, AIME 2025, SciCode, AA-Omniscience
- **Weights:** Cost 25%, IFBench 18%, Terminal-Bench 8%, SWE-bench V 7%, SWE-bench Pro 4%, LCB 6%, GDPval 5%, Speed 5%, τ² 4%, OSWorld 4%, BrowseComp 3%, LCR 2%, HLE 2%, GPQA 2%, MMLU-Pro 2%, AIME 1%, SciCode 1%, AA-Omni 1%

Full formula, weight rationale, normalization examples, sensitivity analysis, and maintenance protocols → [methodology.md](methodology.md)

---

## Research Provenance

The ranking is backed by 4 research runs totaling 80+ web sources:

| Run | Mode | Purpose | Sources |
|---|---|---|---|
| 1 | Quick | Initial data: GPT-5.5, DeepSeek V4-Pro, Kimi K2.6 launch | 22 |
| 2 | Deep | Full 12-model update, 3 new dimensions activated | 25 |
| 3 | UltraDeep | Gap-fill: all remaining ⊘ cells, 60+ targets | 17 |
| 4 | Standard | v5.0 expansion: 8 new model benchmark data, cost/speed confirmation | 20+ |

All findings documented in [`research.md`](research.md) with confidence levels (confirmed / probable / unverified) and source URLs.

---

*Report maintained by the Kay project team | Feedback: kay-rankings@alo-exp.dev*
*Next scheduled update: May 2026 quality gap-fill run (priority: Nova Pro, Gemma3, Phi-4 benchmark data) or next major model launch, whichever comes first*
