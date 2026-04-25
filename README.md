# ValueRank
**Frontier AI model ranking — 12 models × 18 dimensions, rank-based normalization**

**Version 4.2 | April 26, 2026**

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

## Ranking Snapshot (v4.2, April 26, 2026)

| Rank | Model | Score | Quality | Cost Tier | Developer |
|---|---|---|---|---|---|
| 🥇 1 | **Gemini 3.1 Pro** | **70.0** | #2~ | Premium ($892) | Google DeepMind |
| 🥈 2 | **GPT-5.5** | **67.0~** | #1~ (prov.) | Very Expensive ($3,357) | OpenAI |
| 🥉 3 | **KAT-Coder-Pro-V2** | **58.4** | #7 | Budget ($73) | Kay (alo-exp) |
| 4 | GLM 5.1 | 56.7 | #10 | Mid-Range ($544) | Zhipu AI |
| 5 | MiniMax M2.7 | 54.0 | #8 | Near-Budget ($176) | MiniMax |
| 6 | Kimi K2.6 | 53.9~ | #5 | Premium ($948) | Moonshot AI |
| 7 | GPT-5.4 | 52.3 | #4 | Expensive ($2,851) | OpenAI |
| 8 | Qwen 3.6 Plus | 49.0 | #9 | Mid-Range ($483) | Alibaba |
| 9 | DeepSeek V4-Pro | 48.2 | #6 | Premium ($1,071) | DeepSeek |
| 10 | Claude Opus 4.7 | 44.3 | #3 | Ultra-Premium ($4,811) | Anthropic |
| 11 | Claude Sonnet 4.6 | 25.5 | #12 | Very Expensive ($3,959) | Anthropic |
| 12 | Claude Opus 4.6 | 20.6 | #11 | Ultra-Premium ($4,970) | Anthropic |

> ~ = includes provisional data (GPT-5.5 LCB ~91.7%~, secondary source). Scores within 2–3 pts are effectively tied per SEAL CI. See [scores.md §10](scores.md#10-ranking-changes-v10--v20--v25--v30--v40) for full version history.

---

## Executive Summary

This report ranks 12 frontier AI models across 18 dimensions — 15 quality benchmarks plus cost efficiency, inference speed (tok/s), and task-level reliability — using rank-based normalization with a 25% cost weight. The framework is designed to reflect the total value equation for production software engineering teams: raw capability matters, but so does price, throughput, and reliability at scale.

**v4.0 Headline Finding (UltraDeep gap-fill — 16 data points):** A comprehensive research mission filled 16 ⊘ cells and corrected 1 value across 8 dimensions for newly released models. **DeepSeek V4-Pro's real scores** (Cost $1,071.28, Speed 35.8 tok/s, SWEPro 55.4%, Omni −10) are mostly below the neutral-50 assumptions it held in v3.0 — the model drops from #8 to #9. **GPT-5.5 Speed confirmed** at 74.7 tok/s (xhigh), and SWE-bench Verified 88.7% dagger removed (now multi-source confirmed). **SWE-bench Pro** expands from 5/12 to 9/12 coverage. **BrowseComp** reaches 8/12; **MMLU-Pro** reaches 6/12 with Claude Opus 4.7 taking the new #1 (89.87%). **Key ranking shifts:** Kimi K2.6 rises #6→#5 (SWEPro + cost improve); MiniMax falls #5→#6; GLM falls #4→#4 (score drops 58.2→56.7 from BrowseComp 0.0 + MMLU-Pro 20.0); Qwen rises #9→#8; DeepSeek falls #8→#9. Quality-only: GPT-5.5 surges to #2 (70.9, was #4) as Speed and SWEPro fill in.

**v4.2 update (secondary source fills):** GPT-5.5 LCB provisionally filled at ~91.7%~ (+1.8 pts, 65.2→67.0~); quality #1 provisional (72.7~ vs Gemini 72.1, within SEAL CI). Kimi drops #5→#6~ (53.9, −0.9 pts); MiniMax rises #6→#5 (54.0, +0.1 margin — SEAL CI tied). Three data conflicts flagged in [limitations.md §14.11](limitations.md#1411-external-research-data-conflicts-v42) — not incorporated.

**Top 6 (v4.2):**
1. 🥇 **Gemini 3.1 Pro** — 70.0 pts (#1 overall; broadest coverage; #1 IFBench, Speed, τ², GPQA, Sci, Omni)
2. 🥈 **GPT-5.5** — 67.0~ pts (#2 overall; LCB provisional 91.7%~; score +1.8 pts; provisional quality #1 72.7~)
3. 🥉 **KAT-Coder-Pro-V2** — 58.4 pts (sole cheapest to run, $73.49; #2 Terminal-Bench + Speed)
4. **GLM 5.1** — 56.7 pts (eval cost rank 4/12; #2 IFBench + #3 τ²-Bench; BrowseComp 0.0 hurts)
5. **MiniMax M2.7** — 54.0 pts (↑ from #6; near-budget $175.51; passes Kimi by 0.1 pts — SEAL CI tied)
6. **Kimi K2.6** — 53.9~ pts (↓ from #5; LCB rank compression −0.9 pts; SEAL CI tied with MiniMax)

---

## Model Inventory

| # | Model | Provider | Release | Context | Primary Tier |
|---|---|---|---|---|---|
| 1 | Gemini 3.1 Pro | Google DeepMind | 2026-02 | 2M tokens | Frontier |
| 2 | Kimi K2.6 | Moonshot AI | 2026-01 | 200K tokens | Frontier |
| 3 | MiniMax M2.7 | MiniMax | 2026-02 | 1M tokens | Frontier |
| 4 | GPT-5.4 | OpenAI | 2026-03 | 256K tokens | Frontier |
| 5 | Qwen 3.6 Plus | Alibaba | 2026-02 | 128K tokens | Frontier |
| 6 | KAT-Coder-Pro-V2 | KAT AI | 2026-01 | 64K tokens | Specialist |
| 7 | GLM 5.1 | Zhipu AI | 2026-01 | 128K tokens | Frontier |
| 8 | Claude Opus 4.7 | Anthropic | 2026-03 | 200K tokens | Frontier |
| 9 | GPT-5.5 | OpenAI | 2026-04-23 | 512K tokens | Frontier |
| 10 | Claude Sonnet 4.6 | Anthropic | 2026-02 | 200K tokens | Frontier |
| 11 | Claude Opus 4.6 | Anthropic | 2025-11 | 200K tokens | Frontier |
| 12 | DeepSeek V4-Pro | DeepSeek | 2026-04-24 | 1M tokens | Frontier (OSS) |

---

## Methodology (summary)

- **Formula:** `((n − rank) / (n − 1)) × 100` per dimension; n = models with real data. Missing = neutral-50 (⊘). Tied ranks averaged.
- **Dimensions (18):** Cost, IFBench, Terminal-Bench 2.0, SWE-bench V, SWE-bench Pro, LCB v4, GDPval-AA ELO, Speed, τ²-Bench, OSWorld, BrowseComp, RULER/LCR, HLE, GPQA Diamond, MMLU-Pro, AIME 2025, SciCode, AA-Omniscience
- **Weights:** Cost 25%, IFBench 18%, Terminal-Bench 8%, SWE-bench V 7%, SWE-bench Pro 4%, LCB 6%, GDPval 5%, Speed 5%, τ² 4%, OSWorld 4%, BrowseComp 3%, LCR 2%, HLE 2%, GPQA 2%, MMLU-Pro 2%, AIME 1%, SciCode 1%, AA-Omni 1%

Full formula, weight rationale, normalization examples, sensitivity analysis, and maintenance protocols → [methodology.md](methodology.md)

---

## Research Provenance

The ranking is backed by 3 research runs totaling 60+ web sources:

| Run | Mode | Purpose | Sources |
|---|---|---|---|
| 1 | Quick | Initial data: GPT-5.5, DeepSeek V4-Pro, Kimi K2.6 launch | 22 |
| 2 | Deep | Full 12-model update, 3 new dimensions activated | 25 |
| 3 | UltraDeep | Gap-fill: all remaining ⊘ cells, 60+ targets | 17 |

All findings documented in [`research.md`](research.md) with confidence levels (confirmed / probable / unverified) and source URLs.

---

*Report maintained by the Kay project team | Feedback: kay-rankings@alo-exp.dev*
*Next scheduled update: May 2026 quarterly refresh or next major model launch, whichever comes first*
