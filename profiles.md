# ValueRank — Model Profiles
**Per-model analysis | Updated per version**

← [README](README.md) · [Scores](scores.md) · [Insights](insights.md)

---

## 11. Model Profiles

### 11.1 Gemini 3.1 Pro 🥇
**Overall:** #1 | **Quality:** #2~ (provisional, pending LCB verification; see [limitations.md §14.11](limitations.md#1411-external-research-data-conflicts-v42)) | **Cost tier:** Premium ($892.28 eval cost)

**v4.0 extends Gemini's lead to 70.6 pts (+1.1 vs v3.0 69.5).** The n=12 renormalization of Cost (60.0→63.6) and BrowseComp (60.0→71.4 as n grows from 6→8) contribute +0.9 and +0.34 pts. MMLU-Pro drops from 100.0 to 80.0 (−0.4 pts) as Opus 4.7 (89.87%~) displaces Gemini from #1 to #2 in that dimension. Net gain ≈ +1.1 pts.

**Why Gemini holds #1:** The only model with real data on 17 of 18 dimensions (OSWorld remains ⊘). Leads on IFBench (100.0), Speed (100.0), τ²-Bench (100.0), GPQA Diamond (100.0), SciCode (100.0), AA-Omniscience (100.0). GDP (9.1 — rank 11/12) remains the structural weakness: human preference evaluators consistently rank Gemini near-last on conversational quality.

**v4.2:** Score drops 70.6→70.0 (−0.6 pts) as LCB rank compresses from 3/5 to 4/6 with GPT-5.5 insertion. Quality drops to #2~ (72.1); provisional pending LCB confirmation. Gemini's near-complete 17/18 data profile means it cannot be displaced by surprise real data; its overall #1 lead is structural.

**Best for:** Production SE workloads requiring consistent, instruction-following intelligence at scale. Long-context tasks (2M token window). Coverage-critical deployments where missing-data risk is unacceptable.

---

### 11.2 GPT-5.5 🥈
**Overall:** #2 | **Quality:** #1~ (provisional; LCB 91.7%~ secondary source; see [limitations.md §14.11](limitations.md#1411-external-research-data-conflicts-v42)) | **Cost tier:** Very Expensive ($3,357.00 eval cost)

**v4.0 confirms GPT-5.5 as quality #2 (70.9 pts, up from 62.4).** Two v4.0 fills: Speed confirmed at 74.7 tok/s (rank 5/12, score 63.6) and SWEPro confirmed at 68.8 (tied rank 3.5/9 with Kimi). Together these add +0.68+1.25 = +1.93 pts vs. neutral-50, pushing GPT-5.5 to quality #2 above Claude Opus 4.7. The SWE-bench Verified † dagger is removed — the 88.7% figure is now confirmed on swebench.com. Overall score rises 64.0 → 65.2.

**v4.2 LCB fill (provisional):** Multi-AI research report (April 26, 2026) attributes ~91.7% to GPT-5.5 on LCB v4 — rank 2/6, score 80.0~. If confirmed, this adds +1.8 pts (65.2→67.0) and raises quality to #1 (72.7~, narrowly above Gemini's 72.1). The 0.6-pt margin falls within the SEAL CI "effectively tied" band. See [limitations.md §14.11](limitations.md#1411-external-research-data-conflicts-v42) for source conflicts. Overall score *with fill*: **67.0~**.

**Remaining gaps (3 of 18 ⊘):** LCR (not published), AIME 2025, SciCode. LCB provisionally filled at ~91.7%~ (pending primary-source confirmation). These three ⊘ dimensions are the remaining uncertainty band.

**AA-Omniscience caveat (0.0 score):** The −29 raw score (57% accuracy − 86% hallucination at xhigh) is GPT-5.5's one confirmed weakness. At standard reasoning tiers, both accuracy and hallucination rates would differ significantly.

**Best for:** Terminal/CLI agents (#1 TB 2.0), computer-use/GUI agents (#1 OSWorld), deep web research (#1 BrowseComp), τ²-Bench-sensitive agentic pipelines, SWE-bench code repair (#1 confirmed 88.7%).

---

### 11.3 KAT-Coder-Pro-V2 🥉
**Overall:** #3 | **Quality:** #7 | **Cost tier:** Budget ($73.49 eval cost)

**v3.0 cost weight compression reduces KAT's advantage slightly.** Cost weight drops 28%→25%, reducing KAT's cost contribution from 28.0 → 25.0 pts (−3.0). KAT stays at rank 1 eval cost (100.0) but earns fewer points for it. Quality profile unchanged: #2 Terminal-Bench 2.0 (90.0), #2 Speed (90.0), eval cost sole rank 1. At 58.4 pts, KAT drops from #2 to #3 but remains the best cost-to-terminal-performance ratio in the field by a wide margin.

**New dimensions:** All three new dims (SWEPro, BrowseComp, MMLU-Pro) are ⊘ → neutral-50. These contribute 3.0+1.5+1.0 = 5.5 pts at equal neutral-50 weight — no discrimination against or for KAT. KAT's strong profile (100+90+90 on three key dims) keeps it competitive.

**Best for:** Specialized terminal/coding pipelines requiring fast, cost-efficient output at scale. Not a general-purpose model; avoid for reasoning-heavy, knowledge, or GUI tasks (HLE 0.0, GPQA 9.1).

---

### 11.4 GLM 5.1
**Overall:** #4 | **Quality:** #10 | **Cost tier:** Mid-Range ($543.95 eval cost)

**v4.0 delivers a double hit to GLM's quality score.** BrowseComp fills in at 68%~ — last in the 8-model cohort (score 0.0), costing −1.5 pts at 3% weight vs. neutral-50. MMLU-Pro fills in at 85.8%~ (rank 5/6, score 20.0), costing −0.6 pts at 2% weight. Combined −2.1 pts quality impact drops GLM from quality #7 (43.1) to quality #10 (38.1). Overall score falls 58.2 → 56.7. GLM holds #4 overall only because its strong IFBench (#2, 90.0) and τ²-Bench (#3, 80.0) — both at high weights — provide a durable cost-weighted floor.

**Best for:** Instruction-following tasks requiring τ²-Bench multi-step reliability at mid-range cost. A strong alternative to Gemini for budget-conscious instruction-following workloads. Note BrowseComp weakness — not suitable for deep web research pipelines.

---

### 11.5 MiniMax M2.7
**Overall:** #5~ | **Quality:** #8 | **Cost tier:** Near-Budget ($175.51 eval cost)

**v4.2: MiniMax rises #6→#5~** (provisional) — Kimi's LCB rank compression drops Kimi to 53.9, leaving MiniMax (54.0 unchanged) 0.1 pts ahead. The margin is within the SEAL CI "effectively tied" band; treat as statistically co-ranked with Kimi pending LCB confirmation.

**v4.0: MiniMax drops from #5 to #6** as Kimi overtakes it (+2.2 pts vs. MiniMax's −1.0 pts). SWEPro fills at 56.2%~ (rank 7/9, score 25.0) — below neutral-50 (−1.0 pts at 4% weight). GDP compresses slightly as DeepSeek enters the pool. Cost score improves marginally (90.0→90.9 with n=12). Final: 54.0 pts (down from 55.0).

**Best for:** High-volume classification, summarization, extraction tasks at near-budget cost. Not suitable for coding-agent applications (Terminal-Bench last in field, 0.0). SWEPro weakness confirms: avoid for code repair pipelines.

---

### 11.6 Kimi K2.6
**Overall:** #6~ | **Quality:** #5 | **Cost tier:** Premium ($947.87 eval cost)

**v4.2: Kimi drops #5→#6~** (provisional) — LCB rank compresses from 2/5 to 3/6 as GPT-5.5 inserts at rank 2 (~91.7%, secondary source). Cost: −0.9 pts (54.8→53.9). MiniMax (54.0) is 0.1 pts ahead — within SEAL CI "effectively tied" band; treat as co-ranked pending LCB confirmation.

**v4.0: Kimi rises from #6 to #5** (+2.2 pts, 52.6→54.8). The primary driver is SWEPro renormalization: with n expanding from 5→9, Kimi's 58.6% (tied rank 3.5/9 with GPT-5.5) improves from score 37.5 to 68.8 (+1.25 pts at 4% weight). Cost also improves as n=12 lifts rank-6/12 from 50.0 to 54.5 (+1.125 pts at 25% weight). These gains outweigh minor compressions elsewhere. τ²-Bench (0.0 — rank 11/11) remains the dominant weakness at 4% weight. MMLU-Pro 84.6% at rank 6/6 (last in cohort) now scores 0.0 — last in the enlarged cohort.

**Best for:** Coding-heavy pipelines (LCB #2 at 60.0 normalized, second only to DeepSeek), open-weight deployments (Apache 2.0), long-context tasks (200K), SWE-bench Pro competitive at 58.6%.

---

### 11.7 GPT-5.4
**Overall:** #7 | **Quality:** #4 | **Cost tier:** Expensive ($2,851.01 eval cost)

**v4.0: GPT-5.4 drops to quality #4** (64.4, up from 62.9 in v3.0 but displaced from #3 as GPT-5.5 rises to quality #2 and Opus 4.7 holds quality #3). Overall score rises slightly 52.1→52.3 as SWEPro improves from rank 2/5 (75.0) to rank 2/9 (87.5) with n-expansion — the biggest per-dimension gain. Cost moves from 40.0 to 36.4 (rank 8/12 as DeepSeek inserts) but this is offset by SWEPro gain. Net +0.2 pts.

**Best for:** Long-context retrieval (#1 LCR 100.0), BrowseComp web research (#2 at 85.7%), SWE-bench Pro (#2 at 87.5 normalized), Terminal-Bench (81.8). Teams running research, retrieval, or code repair at expensive-but-not-ultra-expensive tier.

---

### 11.8 DeepSeek V4-Pro *(v4.0 gap-fills confirmed)*
**Overall:** #9 | **Quality:** #6 | **Cost tier:** Premium ($1,071.28 eval cost)

**v4.0 delivers a significant downward revision: #8→#9, 51.1→48.2 (−2.9 pts).** Four dimensions that were ⊘ in v3.0 now have confirmed real data — every one came in below neutral-50:

| Dimension | ⊘ Assumption (v3.0) | v4.0 Real Value | Score | Impact |
|---|---|---|---|---|
| Cost | 50.0⊘ | $1,071.28 (rank 7/12) | 45.5 | −1.13 pts |
| Terminal-Bench 2.0 | 50.0⊘ | 67.9%†self (rank 7/12) | 45.5 | −0.36 pts |
| SWE-bench Pro | 50.0⊘ | 55.4% (rank 8/9) | 12.5 | −1.50 pts |
| AA-Omniscience | 50.0⊘ | −10 (84% acc − 94% hall.) | 14.3 | −0.36 pts |

These four fills subtract a net 3.35 pts from the ⊘ baseline, partially offset by GDPval ELO 1,554 (rank 6/12, score 54.5, +0.23 pts above prior ⊘). The lesson: DeepSeek V4-Pro's neutral-50 provisional score in v3.0 was too optimistic. Its real cost-weighted profile is clearly below the frontier leaders.

**Confirmed strengths:** LiveCodeBench v4 (93.5%, rank 1/5 — LCB champion), SWE-bench Verified (80.6%, tied rank 4.5/10), BrowseComp (83.4%, rank 4/8), GDPval ELO 1,554 (above neutral).

**Remaining ⊘ (7 of 18):** IFBench, τ²-Bench, OSWorld, RULER, AIME, SciCode, LCB not yet in ranking pool. Speed corrected to 35.8 tok/s (rank 11/12, score 9.1).

**Best for:** LiveCodeBench coding tasks (#1 globally), SWE-bench GitHub issue resolution, open-source deployments requiring on-premise licensing (Apache 2.0, 1M context). Avoid latency-sensitive streaming (35.8 tok/s, second-slowest in field).

---

### 11.9 Qwen 3.6 Plus
**Overall:** #8 | **Quality:** #9 | **Cost tier:** Mid-Range ($482.65 eval cost)

**v4.0: Qwen rises from #9 to #8** — not because its own score improved (49.7→49.0, slight decline), but because DeepSeek falls past it (51.1→48.2). Qwen's SWEPro fills at 56.6%~ (rank 5/9, score 37.5) — below neutral-50 (−0.5 pts). Speed compresses slightly (60.0→54.5) as GPT-5.5 inserts at rank 5. MMLU-Pro drops from rank 2/4 (66.7) to rank 3/6 (60.0) as new models enter. Net: −0.7 pts own score.

**Best for:** High-volume mid-range workloads. MMLU-Pro at rank 3/6 (88.5%) indicates strong knowledge breadth. Avoid τ²-Bench-sensitive or agentic pipelines (rank 9/11, score 20.0).

---

### 11.10 Claude Opus 4.7
**Overall:** #10 | **Quality:** #3 | **Cost tier:** Ultra-Premium ($4,811.04 eval cost)

**v4.0: Opus 4.7 gains +1.4 pts (42.9→44.3) and rises to quality #3 (68.7).** The biggest single positive fill is MMLU-Pro 89.87%~ — this puts Opus 4.7 at rank 1/6, score 100.0, worth +2.0 pts at 2% weight vs. neutral-50. BrowseComp (14.3, rank 7/8) and Omni (85.7, rank 2/8) also fill in above neutral. Cost compresses slightly (10.0→9.1 as n=12), costing −0.23 pts. Net +1.4 pts.

**Quality-cost paradox deepens in v4.0:** Quality #3 (68.7 pts) but #10 overall — a 7-rank gap, the largest in the field. GPT-5.5 displaces Opus 4.7 from quality #2, but Opus 4.7's benchmark profile remains extraordinary: #1 SWE-bench Pro (100.0), #1 HLE (100.0), #1 MMLU-Pro (100.0~), #2 GPQA (90.9). For teams where quality-per-outcome is the only metric, Opus 4.7 is the definitive choice.

**Best for:** High-stakes software engineering (SWE-bench Pro #1, 64.3%), expert-knowledge tasks (HLE #1, 46.9%), graduate-level reasoning (MMLU-Pro #1~, GPQA #2), enterprise customers unconstrained by cost.

---

### 11.11 Claude Sonnet 4.6
**Overall:** #11 | **Quality:** #12 | **Cost tier:** Very Expensive ($3,959.36 eval cost)

All three new dimensions (SWEPro, BrowseComp, MMLU-Pro) are ⊘ → neutral-50 for Sonnet. GDP renorms to 81.8 (rank 3/12 — 1,675 ELO, same rank as v3.0 but n expands to 12) and Terminal-Bench renorms to 9.1 (rank 11/12 as DeepSeek inserts above Sonnet). Final: 25.5 pts.

**Best for:** Simple conversational tasks where Anthropic ecosystem compatibility is required. Not recommended for coding-agent, agentic, or math-intensive pipelines.

---

### 11.12 Claude Opus 4.6
**Overall:** #12 | **Quality:** #11 | **Cost tier:** Ultra-Premium ($4,969.68 eval cost)

Most expensive model to run ($4,969.68, rank 11/11, cost score 0.0). SWE-bench Pro (51.9%, rank 9/9, score 0.0) is Opus 4.6's worst result in the new dimensions — last in the expanded SWE-Pro cohort. **BrowseComp now filled at 83.7%~ (score 57.1~, rank 4/8)** — above neutral-50, a positive v4.0 fill. MMLU-Pro remains ⊘ (neutral-50). AIME 2025 tied rank 1.5 at 99.8% (90.0) and SWE-bench #3 (77.8) remain the dimension bright spots. At essentially equivalent eval cost to Opus 4.7 ($4,970 vs $4,811) but lower quality on nearly every dimension, migration to 4.7 is the dominant recommendation.

**Best for:** Legacy deployments that cannot migrate; no new deployments recommended.
