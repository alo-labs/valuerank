# ValueRank

**Frontier AI model ranking — 12 models × 18 dimensions, rank-based normalization**

Last updated: April 25, 2026 (v4.0)

---

## Files

| File | Description |
|---|---|
| [`ai-models-ranking.md`](ai-models-ranking.md) | The ranking document — v4.0, 12 models, 18 scored dimensions, methodology, model profiles, and use-case matrix |
| [`research.md`](research.md) | Primary research evidence — 3 research runs (Quick → Deep → UltraDeep) that sourced every data point in the ranking |

---

## Ranking Snapshot (v4.0, April 25, 2026)

| Rank | Model | Score | Developer |
|---|---|---|---|
| 1 | Gemini 3.1 Pro | 70.6 | Google DeepMind |
| 2 | GPT-5.5 | 65.2 | OpenAI |
| 3 | KAT-Coder-Pro-V2 | 58.4 | Kay (alo-exp) |
| 4 | GLM 5.1 | 56.5 | Zhipu AI |
| 5 | Kimi K2.6 | 53.5 | Moonshot AI |
| 6 | MiniMax M2.7 | 54.0 | MiniMax |
| 7 | GPT-5.4 | 51.7 | OpenAI |
| 8 | Qwen 3.6 Plus | 49.0 | Alibaba |
| 9 | DeepSeek V4-Pro | 47.2 | DeepSeek |
| 10 | Claude Opus 4.7 | 44.2 | Anthropic |
| 11 | Claude Sonnet 4.6 | 25.5 | Anthropic |
| 12 | Claude Opus 4.6 | 21.2 | Anthropic |

*Scores are weighted composites across 18 benchmark dimensions. See `ai-models-ranking.md` for full methodology.*

---

## Methodology

- **Scoring:** Rank-based normalization → `((n − rank) / (n − 1)) × 100` per dimension; missing data = neutral-50
- **Dimensions (18):** Cost, IFBench, Terminal-Bench 2.0, SWE-bench V, SWE-bench Pro, LCB v4, GDPval-AA ELO, Speed, τ²-Bench, OSWorld, BrowseComp, RULER/LCR, HLE, GPQA Diamond, MMLU-Pro, AIME 2025, SciCode, AA-Omniscience
- **Weights:** Cost 25%, IFBench 18%, Terminal-Bench 8%, SWE-bench V 7%, SWE-bench Pro 4%, LCB 6%, GDPval 5%, Speed 5%, τ² 4%, OSWorld 4%, BrowseComp 3%, LCR 2%, HLE 2%, GPQA 2%, MMLU-Pro 2%, AIME 1%, SciCode 1%, AA-Omni 1%

---

## Research Provenance

The ranking is backed by 3 research runs totaling 60+ web sources:

| Run | Mode | Purpose | Sources |
|---|---|---|---|
| 1 | Quick | Initial data: GPT-5.5, DeepSeek V4-Pro, Kimi K2.6 launch | 22 |
| 2 | Deep | Full 12-model update, 3 new dimensions activated | 25 |
| 3 | UltraDeep | Gap-fill: all remaining ⊘ cells, 60+ targets | 17 |

All findings documented in [`research.md`](research.md) with confidence levels (confirmed / probable / unverified) and source URLs.
