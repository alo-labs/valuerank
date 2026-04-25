# ValueRank — Model Profiles
**Per-model analysis | Updated per version**

← [README](README.md) · [Scores](scores.md) · [Insights](insights.md)

---

## 11. Model Profiles

### 11.1 Gemini 3.1 Pro 🥇
**Overall:** #1 | **Quality:** #1 | **Cost tier:** Premium ($892.28 eval cost)

**v4.0 extends Gemini's lead to 70.6 pts (+1.1 vs v3.0 69.5).** The n=12 renormalization of Cost (60.0→63.6) and BrowseComp (60.0→71.4 as n grows from 6→8) contribute +0.9 and +0.34 pts. MMLU-Pro drops from 100.0 to 80.0 (−0.4 pts) as Opus 4.7 (89.87%~) displaces Gemini from #1 to #2 in that dimension. Net gain ≈ +1.1 pts.

**Why Gemini holds #1:** The only model with real data on 17 of 18 dimensions (OSWorld remains ⊘). Leads on IFBench (100.0), Speed (100.0), τ²-Bench (100.0), GPQA Diamond (100.0), SciCode (100.0), AA-Omniscience (100.0). GDP (9.1 — rank 11/12) remains the structural weakness: human preference evaluators consistently rank Gemini near-last on conversational quality.

**v4.2:** Score drops 70.6→70.0 (−0.6 pts) as LCB rank compresses from 3/5 to 4/6 with provisional GPT-5.5 insertion. Quality drops to provisional #2 (72.1).

**v4.3:** Score restores to **70.6** (+0.6 pts) as LCB pool reverts to n=5 — GPT-5.5's 91.7%~ fill was Gemini's own score misattributed. Gemini LCB rank returns to 3/5 (score 50.0). **Quality reclaims #1 (72.7)**, confirmed — GPT-5.5 drops to quality #2 (70.9) with LCB provisional removed. Open item: pricepertoken.com suggests Gemini may have a current LCB of 91.7% ("Gemini 3 Pro Preview") — pending identity confirmation on canonical leaderboard (see [limitations.md §14.11](limitations.md#1411-external-research-data-conflicts-v42)).

**Best for:** Production SE workloads requiring consistent, instruction-following intelligence at scale. Long-context tasks (2M token window). Coverage-critical deployments where missing-data risk is unacceptable.

---

### 11.2 GPT-5.5 🥈
**Overall:** #2 | **Quality:** #2 | **Cost tier:** Very Expensive ($3,357.00 eval cost)

**v5.0: GPT-5.5 holds #2 overall, drops −1.5 pts** (65.2→63.7). Cost rank 9→17/20 (−11.3 pts on Cost dim, −2.8 pts weighted). Quality gains: LCB pool expansion still ⊘ for GPT-5.5 (not in pool); GPQA improves slightly (n=12→18, rank 3/18 = 88.2 vs prior 81.8, +0.13 pts); HLE rank 3/15 (85.7, +0.14 pts); τ² rank 2/12 (90.9 vs prior 90.0, +0.04 pts). Net quality gain: ~+0.3 pts. Net total: −1.5 pts. Holds quality #2 (71.9) well clear of quality #3 Opus4.7 (70.2).

**v4.0 confirms GPT-5.5 as quality #2 (70.9 pts, up from 62.4).** Two v4.0 fills: Speed confirmed at 74.7 tok/s (rank 5/12, score 63.6) and SWEPro confirmed at 68.8 (tied rank 3.5/9 with Kimi). Together these add +0.68+1.25 = +1.93 pts vs. neutral-50, pushing GPT-5.5 to quality #2 above Claude Opus 4.7. The SWE-bench Verified † dagger is removed — the 88.7% figure is now confirmed on swebench.com. Overall score rises 64.0 → 65.2.

**v4.2 LCB fill (provisional — reverted in v4.3):** Multi-AI research report attributed ~91.7% to GPT-5.5 on LCB v4, adding +1.8 pts (65.2→67.0~). Reverted: primary-source verification confirmed 91.7% belongs to Gemini 3 Pro Preview, not GPT-5.5. Score returns to **65.2**. See [limitations.md §14.11](limitations.md#1411-external-research-data-conflicts-v42).

**Remaining gaps (4 of 18 ⊘):** LCR (not published), AIME 2025, SciCode, LCB (not in pool). These four ⊘ dimensions are the remaining uncertainty band.

**AA-Omniscience caveat (0.0 score):** The −29 raw score (57% accuracy − 86% hallucination at xhigh) is GPT-5.5's one confirmed weakness. At standard reasoning tiers, both accuracy and hallucination rates would differ significantly.

**Best for:** Terminal/CLI agents (#1 TB 2.0), computer-use/GUI agents (#1 OSWorld), deep web research (#1 BrowseComp), τ²-Bench-sensitive agentic pipelines, SWE-bench code repair (#1 confirmed 88.7%).

---

### 11.3 KAT-Coder-Pro-V2
**Overall:** #7 | **Quality:** #11 | **Cost tier:** Budget ($73.49 eval cost)

**v5.0: KAT drops #3→#7** (58.0→54.0, −4.0 pts). Cost rank falls 1→6 as 5 ultra-cheap entrants insert above it; Cost contribution drops 25.0→18.4 (−6.6 pts). Partially offset by quality pool expansions: SciCode n=9→13 improves KAT from 0.0 to 25.0 (rank 10/13, +0.25 pts), GPQA n=12→18 shifts rank from 9/12→11/18 (41.2 vs prior 9.1, +0.32 pts), AIME n=6→7 stays at neutral-50, LCB still ⊘. Net quality gain: ~+0.6 pts. Net total: −4.0 pts. KAT is no longer the cheapest paid model — Mistral Large 3, Maverick, Scout all undercut it on cost.

**v3.0 cost weight compression reduces KAT's advantage slightly.** Cost weight drops 28%→25%, reducing KAT's cost contribution from 28.0 → 25.0 pts (−3.0). KAT stays at rank 1 eval cost (100.0) but earns fewer points for it. Quality profile unchanged: #2 Terminal-Bench 2.0 (90.0), #2 Speed (90.0), eval cost sole rank 1. At 58.4 pts, KAT drops from #2 to #3 but remains the best cost-to-terminal-performance ratio in the field by a wide margin.

**New dimensions:** All three new dims (SWEPro, BrowseComp, MMLU-Pro) are ⊘ → neutral-50. These contribute 3.0+1.5+1.0 = 5.5 pts at equal neutral-50 weight — no discrimination against or for KAT. KAT's strong profile (100+90+90 on three key dims) keeps it competitive.

**Best for:** Specialized terminal/coding pipelines requiring fast, cost-efficient output at scale. Not a general-purpose model; avoid for reasoning-heavy, knowledge, or GUI tasks (HLE 0.0, GPQA 9.1).

---

### 11.4 GLM 5.1
**Overall:** #12 | **Quality:** #14 | **Cost tier:** Mid-Range ($543.95 eval cost)

**v5.0: GLM drops #5→#12** (56.7→51.3, −5.4 pts). Cost rank falls 4→12 (−30.6 pts on Cost dim, −7.65 pts weighted). Quality pool expansions add modest offsets: AIME improves 30.0→41.7 (Gemini/GLM rank 4.5/7 vs prior 4.5/6), GPQA n=12→18 shifts GLM to rank 10/18 (47.1 vs prior 18.2), τ² improves 80.0→81.8 (rank 3/12 vs prior 3/11). Net quality gain ~+2.3 pts. Net total: −5.4 pts. Seven new models insert above GLM in the final ranking.

**v4.0 delivers a double hit to GLM's quality score.** BrowseComp fills in at 68%~ — last in the 8-model cohort (score 0.0), costing −1.5 pts at 3% weight vs. neutral-50. MMLU-Pro fills in at 85.8%~ (rank 5/6, score 20.0), costing −0.6 pts at 2% weight. Combined −2.1 pts quality impact drops GLM from quality #7 (43.1) to quality #10 (38.1). Overall score falls 58.2 → 56.7. GLM had held #4 overall due to strong IFBench (#2, 90.0) and τ²-Bench (#3, 80.0) — both at high weights.

**v4.3: GLM falls #4→#5** (score unchanged at 56.7) — Kimi K2.6's τ²-Bench correction (+3.7 pts, 53.9→57.6) pushes Kimi above GLM. GLM's quality and dimension profile is unaffected; the rank change is driven entirely by Kimi's correction.

**Best for:** Instruction-following tasks requiring τ²-Bench multi-step reliability at mid-range cost. A strong alternative to Gemini for budget-conscious instruction-following workloads. Note BrowseComp weakness — not suitable for deep web research pipelines.

---

### 11.5 MiniMax M2.7
**Overall:** #11 | **Quality:** #12 | **Cost tier:** Near-Budget ($175.51 eval cost)

**v5.0: MiniMax drops #6→#11** (53.6→51.4, −2.2 pts). Cost rank falls 2→7 (−22.5 pts on Cost dim, −5.6 pts weighted). Quality pool expansions recover ~+3.4 pts: GPQA n=12→18 improves from 27.3 to 52.9 (rank 9/18, +0.51 pts), τ² 35.0→40.9 (+0.24 pts), AIME stays neutral. Six new entrants insert above MiniMax overall. Despite cost compression, MiniMax retains its core value proposition: highest IF score (#5 at 69.2) among the ≤$200 eval cost models, and AA-Omniscience rank 3/8 (71.4).

**v4.3: MiniMax falls #5→#6** (53.6, −0.4 pts) — τ²-Bench pool reconstitution costs all non-Kimi τ² participants −0.4 pts as ranks shift. Score drops 54.0→53.6. Kimi's correction (+3.7 pts) simultaneously pushes Kimi to #4, dropping both GLM and MiniMax one position each.

**v4.2: MiniMax provisionally rose #6→#5~** — Kimi's LCB rank compression dropped Kimi to 53.9, leaving MiniMax (54.0) marginally ahead. Superseded by v4.3 correction.

**v4.0: MiniMax drops from #5 to #6** as Kimi overtakes it (+2.2 pts vs. MiniMax's −1.0 pts). SWEPro fills at 56.2%~ (rank 7/9, score 25.0) — below neutral-50 (−1.0 pts at 4% weight). GDP compresses slightly as DeepSeek enters the pool. Cost score improves marginally (90.0→90.9 with n=12). Final: 54.0 pts (down from 55.0).

**Best for:** High-volume classification, summarization, extraction tasks at near-budget cost. Not suitable for coding-agent applications (Terminal-Bench last in field, 0.0). SWEPro weakness confirms: avoid for code repair pipelines.

---

### 11.6 Kimi K2.6
**Overall:** #6 | **Quality:** #5 | **Cost tier:** Premium ($947.87 eval cost)

**v5.0: Kimi drops #4→#6** (57.6→54.3, −3.3 pts). Cost rank falls 6→14 (−22.9 pts on Cost dim, −5.7 pts weighted). Quality gains partially offset: LCB improves 75.0→77.8 (+0.17 pts), AIME improves 60.0→66.7 (+0.07 pts), GPQA 63.6→76.5 (+0.25 pts), HLE improves to 57.1 (rank 7/15, +0.14 pts). Quality score rises ~57.9 (up from ~53.0 in v4.3). Three cheaper models (ML3, Gemma3, Phi4) insert above at ranks 3–5.

**v4.3: Kimi rises #6→#4** (+3.7 pts, 53.9→57.6) — the largest single-model gain in v4.3. Two drivers: **(1) τ²-Bench corrected from 72.4% to 96.0%** (primary source: AA article) — moves Kimi from rank 11/11 (last, score 0.0) to rank 4/11 (score 70.0), +2.8 pts at 4% weight. **(2) LCB pool reconstitution** as GPT-5.5 provisional fill reverts — Kimi rises from rank 3/6 (score 60.0) to rank 2/5 (score 75.0), +0.9 pts at 6% weight. Combined +3.7 pts. τ²-Bench (now 70.0, rank 4/11) transitions from dominant weakness to competitive dimension. MMLU-Pro 84.6% at rank 6/6 (score 0.0) remains the new weakest dimension.

**v4.2: Kimi drops #5→#6~** — LCB rank compresses from 2/5 to 3/6 with provisional GPT-5.5 insertion. Superseded by v4.3 correction.

**v4.0: Kimi rises from #6 to #5** (+2.2 pts, 52.6→54.8). SWEPro renormalization (n=5→9) and cost improvement drive gains. τ²-Bench (0.0, rank 11/11) was the dominant weakness — now corrected.

**Best for:** Coding-heavy pipelines (LCB #2 normalized at 75.0, second only to DeepSeek), multi-step agentic tasks (τ²-Bench rank 4/11 confirmed at 96%), open-weight deployments (Apache 2.0), long-context tasks (200K), SWE-bench Pro competitive at 58.6%.

---

### 11.7 GPT-5.4
**Overall:** #10 | **Quality:** #4 | **Cost tier:** Expensive ($2,851.01 eval cost)

**v5.0: GPT-5.4 drops #7→#10 but gains +0.3 pts** (51.9→52.2). Cost compression costs −3.8 pts (rank 8→16/20); quality gains more than compensate: LCB improves 0.0→22.2 (+1.33 pts at 6%), SciCode improves from 88.9 to 91.7 (n-shift minor), GPQA expands n=12→18 but GPT-5.4 rank holds (rank 4/18, score 82.4 vs prior 72.7 — actually improves). Net +0.3 pts. Holds quality #4 (67.0). Despite overall rank drop, GPT-5.4 is the highest-scoring model that costs under $3,000/eval in this cohort.

**v4.0: GPT-5.4 drops to quality #4** (64.4, up from 62.9 in v3.0 but displaced from #3 as GPT-5.5 rises to quality #2 and Opus 4.7 holds quality #3). Overall score rises slightly 52.1→52.3 as SWEPro improves from rank 2/5 (75.0) to rank 2/9 (87.5) with n-expansion — the biggest per-dimension gain. Cost moves from 40.0 to 36.4 (rank 8/12 as DeepSeek inserts) but this is offset by SWEPro gain. Net +0.2 pts.

**Best for:** Long-context retrieval (#1 LCR 100.0), BrowseComp web research (#2 at 85.7%), SWE-bench Pro (#2 at 87.5 normalized), Terminal-Bench (81.8). Teams running research, retrieval, or code repair at expensive-but-not-ultra-expensive tier.

---

### 11.8 DeepSeek V4-Pro *(v4.0 gap-fills confirmed)*
**Overall:** #16 | **Quality:** #8 | **Cost tier:** Premium ($1,071.28 eval cost)

**v5.0: DeepSeek drops #9→#16** (48.2→45.2, −3.0 pts). Cost rank falls 7→15/20 (−19.2 pts on Cost dim, −4.8 pts weighted). Quality gains: LCB holds rank 1/10 (100.0, unchanged), GPQA n=12→18 but DeepSeek rank 7/18 (64.7 vs prior 45.5 — major improvement, +0.38 pts). MMLU improves 40.0→62.5 (rank 4/9, +0.45 pts). HLE 64.3 (rank 6/15, +0.29 pts vs prior 54.5). Net quality gain ~+1.8 pts. Net total: −3.0 pts. LCB #1 (100.0) remains DeepSeek's defining strength — no model has touched it at 93.5%.

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
**Overall:** #17 | **Quality:** #15 | **Cost tier:** Mid-Range ($482.65 eval cost)

**v5.0: Qwen drops #8→#17** (48.6→43.8, −4.8 pts). Cost rank falls 3→11/20 (−34.4 pts on Cost dim, −8.6 pts weighted). Some quality recovery: GPQA improves 54.5→70.6 (rank 6/18, +0.32 pts), MMLU improves 60.0→75.0 (rank 3/9, +0.30 pts), LCR holds rank 4.5/10 (61.1). Net quality gain ~+3.8 pts. Nine new and reranked models land above Qwen. At $482 eval cost Qwen is now the 11th cheapest of 20, fully mid-field — its value proposition has eroded substantially with the arrival of cheaper alternatives.

**v4.0: Qwen rises from #9 to #8** — not because its own score improved (49.7→49.0, slight decline), but because DeepSeek falls past it (51.1→48.2). Qwen's SWEPro fills at 56.6%~ (rank 5/9, score 37.5) — below neutral-50 (−0.5 pts). Speed compresses slightly (60.0→54.5) as GPT-5.5 inserts at rank 5. MMLU-Pro drops from rank 2/4 (66.7) to rank 3/6 (60.0) as new models enter. Net: −0.7 pts own score.

**Best for:** High-volume mid-range workloads. MMLU-Pro at rank 3/6 (88.5%) indicates strong knowledge breadth. Avoid τ²-Bench-sensitive or agentic pipelines (rank 9/11, score 20.0).

---

### 11.10 Claude Opus 4.7
**Overall:** #15 | **Quality:** #3 | **Cost tier:** Ultra-Premium ($4,811.04 eval cost)

**v5.0: Opus 4.7 drops #10→#15 but gains +1.9 pts** (43.9→45.8). Cost compression is modest (rank 11→19/20, −3.8 pts weighted) because Opus 4.7 was already near-last on cost. Quality gains dominate: AIME improves 90.0→91.7 (+0.017 pts), τ² improves 0.0→9.1 (+0.36 pts), LCB pool expansion still ⊘ (no change), GPQA holds rank 2/18 (94.1, +0.24 pts vs prior 90.9), HLE rank 1/15 unchanged (100.0), MMLU rank 1/9 unchanged (100.0~). Net quality: ~+1.9 pts. Holds quality #3 behind Gemini (#1) and GPT-5.5 (#2) — the strongest quality-per-dollar argument for teams where outcomes, not throughput, are the constraint.

**v4.0: Opus 4.7 gains +1.4 pts (42.9→44.3) and rises to quality #3 (68.7).** The biggest single positive fill is MMLU-Pro 89.87%~ — this puts Opus 4.7 at rank 1/6, score 100.0, worth +2.0 pts at 2% weight vs. neutral-50. BrowseComp (14.3, rank 7/8) and Omni (85.7, rank 2/8) also fill in above neutral. Cost compresses slightly (10.0→9.1 as n=12), costing −0.23 pts. Net +1.4 pts.

**Quality-cost paradox deepens in v4.0:** Quality #3 (68.7 pts) but #10 overall — a 7-rank gap, the largest in the field. GPT-5.5 displaces Opus 4.7 from quality #2, but Opus 4.7's benchmark profile remains extraordinary: #1 SWE-bench Pro (100.0), #1 HLE (100.0), #1 MMLU-Pro (100.0~), #2 GPQA (90.9). For teams where quality-per-outcome is the only metric, Opus 4.7 is the definitive choice.

**Best for:** High-stakes software engineering (SWE-bench Pro #1, 64.3%), expert-knowledge tasks (HLE #1, 46.9%), graduate-level reasoning (MMLU-Pro #1~, GPQA #2), enterprise customers unconstrained by cost.

---

### 11.11 Claude Sonnet 4.6
**Overall:** #19 | **Quality:** #19 | **Cost tier:** Very Expensive ($3,959.36 eval cost)

**v5.0: Sonnet drops #11→#19 but gains +2.3 pts** (25.1→27.4). Cost rank 10→18/20 (−7.7 pts weighted). Quality gains: GDP holds rank 3/12 (81.8); GPQA improves from 36.4 to 58.8 (rank 8/18, +0.45 pts); HLE improves to 42.9 (rank 9/15, +0.29 pts); τ² improves 20.0→27.3 (+0.29 pts); LCB still ⊘. Net +2.3 pts. Eight new entrants plus lifted Opus models push Sonnet to #19.

All three new dimensions (SWEPro, BrowseComp, MMLU-Pro) are ⊘ → neutral-50 for Sonnet. GDP renorms to 81.8 (rank 3/12 — 1,675 ELO, same rank as v3.0 but n expands to 12) and Terminal-Bench renorms to 9.1 (rank 11/12 as DeepSeek inserts above Sonnet). Final: 25.5 pts.

**Best for:** Simple conversational tasks where Anthropic ecosystem compatibility is required. Not recommended for coding-agent, agentic, or math-intensive pipelines.

---

### 11.12 Claude Opus 4.6
**Overall:** #20 | **Quality:** #16 | **Cost tier:** Ultra-Premium ($4,969.68 eval cost)

**v5.0: Opus 4.6 drops #12→#20 but gains +4.2 pts** (20.5→24.7) — the largest absolute gain of any existing model. Cost rank 12→20/20 (unchanged at 0.0 — still last). Quality gains dominate: LCB improves 25.0→44.4 (+1.16 pts at 6%) as GPT-5.5 leaves the pool and 5 new provisional entries expand n=5→10; AIME improves 90.0→91.7 (+0.017 pts); τ² 35.0→40.9 (+0.24 pts); GPQA improves from 0.0 to 29.4 (rank 13/18, +0.59 pts). Net quality gain: ~+4.2 pts. Opus 4.6 remains #20 overall and the most expensive model per eval dollar — the migration recommendation to Opus 4.7 stands.

Most expensive model to run ($4,969.68, rank 11/11, cost score 0.0). SWE-bench Pro (51.9%, rank 9/9, score 0.0) is Opus 4.6's worst result in the new dimensions — last in the expanded SWE-Pro cohort. **BrowseComp now filled at 83.7%~ (score 57.1~, rank 4/8)** — above neutral-50, a positive v4.0 fill. MMLU-Pro remains ⊘ (neutral-50). AIME 2025 tied rank 1.5 at 99.8% (90.0) and SWE-bench #3 (77.8) remain the dimension bright spots. At essentially equivalent eval cost to Opus 4.7 ($4,970 vs $4,811) but lower quality on nearly every dimension, migration to 4.7 is the dominant recommendation.

**Best for:** Legacy deployments that cannot migrate; no new deployments recommended.

---

### 11.13 Mistral Large 3
**Overall:** #3 | **Quality:** #9 | **Cost tier:** Ultra-Budget ($38.67 eval cost)

**v5.0 debut: 59.7 pts.** Mistral Large 3 enters at #3 overall, driven almost entirely by two factors: (1) **cost rank 4/20** (84.2 pts at 25% weight = 21.1 pts), and (2) **LCB rank 2/10** with 82.8%~ (88.9 normalized at 6% weight = 5.33 pts). Together these two dimensions contribute 26.4 of 59.7 total pts (44%). All other 16 dimensions are either ⊘ (neutral-50) or the confirmed GPQA 43.9% (rank 17/18 = 5.9, below neutral). Speed 49.8 tok/s is slightly below the ⊘ neutral (44.4, rank 11/19).

**The LCB ambiguity:** The 82.8% LCB score is marked ~ (provisional) — version uncertainty. Models evaluated after April 2025 may use LCBv5 or LCBv6 rather than the canonical LCBv4. If ML3's actual LCBv4 score is significantly lower (e.g., 50–60%), its score would fall to ~54–55 pts, dropping it to ranks 7–9. The LCB fill is the single largest uncertainty in ML3's placement.

**Quality profile (#9):** With 14 of 17 quality dims at ⊘ and Speed below neutral, ML3 quality = 49.4 — technically middle-of-field, but this reflects almost entirely the neutral-50 assumption across unconfirmed dims. Real quality rank is unknown. GPQA 43.9% (rank 17/18) is the one confirmed quality signal and it is below-average.

**Best for:** Cost-sensitive inference workloads where LCB coding performance at $38/eval is the selection criterion. Strong candidate for coding pipelines if the LCB ~ score is confirmed on the canonical leaderboard. Verify before committing to production — 14 dimensions remain unconfirmed.

---

### 11.14 Gemma 3 27B
**Overall:** #4 | **Quality:** #13 | **Cost tier:** Free ($0.00 eval cost via OpenRouter free tier)

**v5.0 debut: 59.3 pts.** Gemma 3 27B is the most extreme cost-arbitrage entry in this cohort: $0.00 AA eval cost (via Google's OpenRouter free tier) gives it rank 1/20 on Cost (100.0 pts) worth 25.0 pts weighted — the maximum possible cost contribution. Everything else is either ⊘ or confirmed-weak. Only GPQA (42.4%, rank 18/18 = 0.0) and Speed (24.6 tok/s, rank 18/19 = 5.6) have real data. Both are below neutral-50.

**Score decomposition:** Cost 25.0 + 16 ⊘ dims × (avg ~2.15 pts weighted) + GPQA 0.0 + Speed 0.28 = 59.3. Remove the free-tier cost advantage and Gemma3 would score roughly 34.3 pts — near the bottom of the field.

**The free-tier question:** AA's $0.00 eval cost is confirmed for the OpenRouter free tier as of April 2026. This may not reflect production API pricing for high-volume deployments. Teams should verify whether free-tier rate limits and availability meet their SLA requirements before treating this as a $0 production cost model.

**14 of 18 dimensions unconfirmed.** The neutral-50 assumption benefits Gemma3 by assigning 50.0 to all unconfirmed quality dims. If confirmed quality scores land below neutral (as GPQA 0.0 suggests is possible for a 27B model vs. frontier peers), the true score would be significantly lower.

**Best for:** Zero-cost evaluation workloads, development and testing, budget-constrained research contexts where free-tier limits are acceptable. Not recommended for production coding or reasoning-intensive workloads — GPQA 0.0 indicates well-below-frontier reasoning at this scale.

---

### 11.15 Phi-4
**Overall:** #5 | **Quality:** #10 | **Cost tier:** Ultra-Budget ($4.27 eval cost)

**v5.0 debut: 59.2 pts.** Nearly identical to Gemma 3 27B in structure: cost-dominant scoring with 16 of 18 dimensions unconfirmed. Cost rank 2/20 (94.7 pts) at 25% weight = 23.7 pts. Only Speed (34.2 tok/s, rank 17/19 = 11.1) is confirmed alongside cost; GPQA is ⊘ (50.0⊘). Speed below neutral costs −1.9 pts vs. neutral-50. All other 16 dims at neutral-50.

**Phi-4 vs. Gemma 3 27B:** ML3 > Gemma3 > Phi-4 at ranks 3–5 are within 0.5 pts of each other (59.7/59.3/59.2) — effectively tied within SEAL CI. The rank ordering is driven by LCB (ML3 has it, others don't), cost rank (Gemma3 $0 vs Phi-4 $4.27 vs ML3 $38.67), and GPQA (Phi-4 ⊘ vs Gemma3 0.0 vs ML3 5.9). All three have the same structural uncertainty: scores will shift substantially once quality benchmarks are confirmed.

**16 of 18 dimensions unconfirmed.** Phi-4 is Microsoft's compact reasoning-focused model; published GPQA and coding benchmark results exist in the literature but were not confirmed on canonical leaderboards as of April 26, 2026. A future research run filling even 4–5 quality dims could materially change its placement.

**Best for:** Ultra-low-cost inference at near-zero API cost. Same caveats as Gemma3: verify free/low-tier availability for production volumes. Potentially valuable for on-device or edge deployment scenarios given compact size.

---

### 11.16 Amazon Nova Pro
**Overall:** #8 | **Quality:** #7 | **Cost tier:** Near-Budget ($200.98 eval cost)

**v5.0 debut: 53.3 pts.** Nova Pro is the most data-sparse entry in the cohort: 17 of 18 dimensions are ⊘ (only Cost is confirmed at $200.98, rank 8/20 = 63.2). Score = Cost 15.79 + 17 × (50.0 × dim_weight) = 53.3 exactly. Quality rank #7 (50.0) reflects pure neutral-50 averaging across all quality dims — Nova Pro has zero confirmed quality data points.

**What this ranking means:** Nova Pro's #8 ranking is not a statement about quality. It is a statement that $200.98 eval cost + no confirmed quality data yields 53.3 pts under this framework's neutral-50 convention for missing data. The moment any confirmed quality benchmark fills in — whether above or below 50.0 — the score will move accordingly. Nova Pro is the clearest example of a model where the ⊘ assumption may be distorting placement.

**Why include it:** Amazon Nova Pro is a commercially significant frontier model from a major cloud provider. Including it with neutral-50 ⊘ fills maintains the ranking's coverage of the deployment landscape while being transparent about data absence. A single quality research run could fill 6–10 dimensions and produce a reliable placement.

**Best for:** Cannot recommend for specific workloads without benchmark data. Cost efficiency is real ($200.98 is competitive). Teams using AWS natively may find Nova Pro practical — run your own benchmarks before committing.

---

### 11.17 Grok 3
**Overall:** #9 | **Quality:** #6 | **Cost tier:** Value ($311.71 eval cost)

**v5.0 debut: 53.0 pts.** Grok 3 has partial data: Cost confirmed ($311.71, rank 9/20 = 57.9), Speed confirmed (71.6 tok/s, rank 9/19 = 55.6), LCB provisional 79.4%~ (rank 4/10 = 66.7), GPQA provisional 84.6%~ (rank 12/18 = 35.3). Remaining 14 dims ⊘.

**The ~ caveat:** Both LCB (79.4%) and GPQA (84.6%) are from secondary sources and may reflect **Grok 3 Think** (reasoning mode) rather than standard Grok 3. Standard-mode scores would likely be lower. If the true GPQA is ~70% (standard mode estimate), GPQA score would fall from 35.3 to ~17.6, costing ~0.35 pts. If LCB is ~65%, LCB score would fall from 66.7 to ~33.3, costing ~2.0 pts. Combined downside risk ~−2.4 pts. Upside risk is lower since both values already clear neutral-50.

**Speed (55.6) above neutral:** At 71.6 tok/s, Grok3 is solidly mid-field — faster than GPT-5.4/5.5, slower than Kimi/KAT. The speed advantage over Nova Pro is confirmed; it's one of only two differentiating confirmed quality signals.

**Best for:** LCB coding workloads if the 79.4%~ score confirms on canonical leaderboard (would rank #4 in pool). Verify Grok3 standard vs. Think mode before using LCB/GPQA figures for benchmarking.

---

### 11.18 Llama 4 Maverick
**Overall:** #13 | **Quality:** #17 | **Cost tier:** Ultra-Budget ($62.28 eval cost)

**v5.0 debut: 47.7 pts.** Maverick's profile is a mixed bag: strong cost rank 5/20 (78.9, contributing 19.7 pts) and strong Speed rank 5/19 (77.8, contributing 3.9 pts), but weak confirmed quality scores across the board. IF 43.0% is rank 12/14 (15.4); LCB 43.4%~ is rank 9/10 (11.1~); HLE 4.8% is rank 14/15 (7.1); GPQA 67.1% is rank 15/18 (17.6); MMLU 80.5% is rank 7/9 (25.0).

**Quality gap:** Every confirmed quality benchmark places Maverick in the bottom half of the cohort. Cost + Speed account for 23.6 of 47.7 pts (49%). This is the clearest example of a fast, cheap model that underperforms on reasoning and instruction-following at frontier scale. The MoE architecture delivers throughput efficiency but benchmark capability lags significantly behind comparable-cost alternatives.

**Compared to Scout:** Maverick (#13, 47.7) ranks above Scout (#14, 47.1) despite Scout having better cost ($26 vs $62) and best-in-field speed (100.0 vs 77.8), because Maverick has higher scores on every confirmed quality dimension (IF 15.4 vs 0.0; GPQA 17.6 vs 11.8; MMLU 25.0 vs 0.0; SciCode 16.7 vs 0.0). Scout's speed advantage (+22.2 pts) and cost advantage (+10.6 pts) don't overcome Maverick's quality margin.

**Best for:** High-throughput, cost-sensitive pipelines where task complexity is low — summarization, classification, extraction at scale. Not suitable for coding agents, complex reasoning, or instruction-following tasks requiring frontier performance.

---

### 11.19 Llama 4 Scout
**Overall:** #14 | **Quality:** #20 | **Cost tier:** Ultra-Budget ($26.42 eval cost)

**v5.0 debut: 47.1 pts.** Scout has the strongest Speed in the entire 20-model cohort (142.5 tok/s, rank 1/19, score 100.0) and the 3rd cheapest eval cost ($26.42, rank 3/20, score 89.5). Together Cost + Speed = 22.4 + 5.0 = 27.4 pts of 47.1 total (58%). Every other confirmed quality benchmark is either last or near-last: IF 39.5% = rank 14/14 (0.0, dead last); LCB 32.8%~ = rank 10/10 (0.0~, dead last); HLE 4.3% = rank 15/15 (0.0, dead last); GPQA 58.7% = rank 16/18 (11.8); MMLU 74.3% = rank 9/9 (0.0, last); SciCode 17.0% = rank 13/13 (0.0, dead last).

**The pattern:** Scout holds last or penultimate position on every confirmed quality benchmark. This is consistent with an extremely lightweight MoE model optimized for inference speed rather than reasoning depth. The high benchmark costs relative to Gemma3/Phi-4 (both cheaper per token) reflect Scout's larger effective deployment at scale, but the quality floor is clearly below other budget alternatives.

**Speed #1 is real and confirmed:** At 142.5 tok/s, Scout outputs tokens faster than any other model in this cohort — 11% faster than o3-mini (131.7) and 11% faster than Gemini (128.0). For streaming, real-time, or extremely latency-sensitive pipelines, Scout's throughput is unmatched.

**Best for:** Maximum-throughput pipelines where task quality requirements are minimal: token streaming, real-time autocomplete, simple classification, preprocessing. Not suitable for any task requiring reasoning, coding, instruction following, or knowledge recall.

---

### 11.20 o3-mini (high)
**Overall:** #18 | **Quality:** #18 | **Cost tier:** Value ($314.72 eval cost)

**v5.0 debut: 42.7 pts.** o3-mini (high) is the counterintuitive entry: a reasoning-capable model from OpenAI that scores below most new entrants despite strong Speed (#2 at 94.4) and confirmed real data on more dimensions than most new entrants (9 of 18 confirmed). The problem is what those confirmed dimensions reveal.

**The τ²-Bench paradox:** o3-mini scores 28.7%~ on τ²-Bench — rank 12/12 (0.0, dead last). τ²-Bench measures multi-step agentic task reliability, and o3-mini's result of 28.7% (vs. 74–99% for top models) is a significant confirmed weakness for a reasoning model. At 4% weight, this costs the maximum possible penalty (0.0 vs 50.0⊘ baseline = −2.0 pts weighted).

**Terminal-Bench 0.0:** o3-mini scores 6.1% on Terminal-Bench 2.0 — rank 13/13 (0.0, dead last at 8% weight). This is the largest single-dimension drag: 0.0 vs 50.0⊘ = −4.0 pts weighted. A reasoning model that scores near-zero on CLI/terminal task execution — likely because the benchmark rewards rapid, direct execution while o3-mini's chain-of-thought generates verbose intermediate reasoning steps that fail the task format.

**AIME/SciCode/GPQA confirmed below frontier:** AIME 77.0% = rank 6/7 (16.7), GPQA 77.3% = rank 14/18 (23.5), SciCode 39.8% = rank 9/13 (33.3). These are respectable scores in absolute terms but below the frontier cluster in a 20-model field.

**Score decomposition:** Cost 13.16 + IF 8.32 + Speed 4.72 = 26.2 pts from three positive dims. Terminal 0.00 + τ² 0.00 = two zero-contribution dims that normally contribute ~6.0 pts. Net drag from confirmed negatives: ~−10 pts vs. a pure-⊘ model at this cost tier.

**Best for:** Math-heavy reasoning tasks where τ²-Bench and terminal execution are not in scope (AIME, SciCode). High-throughput inference at $314 eval cost. Avoid for agentic pipelines, CLI/tool-use agents, or multi-step task execution — the τ²-Bench and Terminal-Bench scores confirm this is not o3-mini's strength.
