# DR-TRIANGULATE: claims cross-checked across sources

Run: `2026-10-17-value-ranking-sites-landscape` (mode `deep`, research_type `default`). First triangulated 2026-10-18 (host date) from 91 sources and 218 evidence rows. **Refreshed in DR-REFINE (2026-10-17 UTC)** against the second retrieval pass (`retrieval/angle-e.jsonl`): 131 sources and 273 evidence rows (all eight-character evidence prefixes remain unique). Claims C1, C2, C3, C8 to C10, C12, C15, C16, C20 and C21 and conflicts X1, X2 and X5 were revised; C22 to C28 and X13 to X16 are new. No retrieval was done in the refresh itself.

**Notation.** `S<n>` is the display number of a source (its position in `sources.jsonl`, as printed by `citation_manager.py assign-display-numbers`; S92 to S131 are the second-pass sources). Evidence is cited by the first eight hex characters of `evidence_id` (all 273 prefixes are unique). Grades are the `reliability_code` stored on each source row (NATO-style letter for source reliability, digit for information credibility). Confidence values are the retrieval agents' own and are quoted where they limit a claim.

**Escalation rule applied** (`reference/source-grading.md`): a core claim needs at least one `A*`, `B1` or `B2` source, or three or more `C*` sources. Sources graded `E*`/`F6` may not carry a core claim alone; `A/B` versus `D/E` conflicts are recorded below. Outcomes use these labels:

| Label | Meaning |
|---|---|
| PASS-AB | at least one A or B1/B2 source directly supports the claim |
| PASS-3C | no A/B source, but three or more independent C sources agree |
| PASS-PRIMARY | the claim is about a site's own method and rests on that site's own page (the best possible source), with no independent confirmation |
| BOUNDED-NEGATIVE | an absence claim: supported by several pages that lack the feature, never provable; stated as "not found in this search" |
| SECONDARY-ONLY | the primary page could not be read; claim rests on secondary reports |
| SINGLE-SOURCED | one source only, no corroboration |
| UNSUPPORTED | evidence insufficient; reported as a gap |

## 1. Core claims

### C1. No other public site combines benchmark quality with subscription-plan cost at the model level (assumption A1)

- **Definition (added in refine).** A site *combines* when, for a named model variant, it (a) reports a quality measure, (b) reports a plan-derived cost (an allowance priced at API rates, or the plan fee divided by it) and (c) joins them in one figure or ranking across models. Showing (a) and (b) side by side without (c) is a **partial combination**. The verdict depends on this definition; under a looser one (side-by-side display counts) it fails for RemakeBench.
- **Boundary evidence (AA only).** Artificial Analysis states its Coding Agent Index cost is "pay-per-token API cost, not consumer plan pricing" and acknowledges that "many users will access coding agent harnesses through subscription plan offerings" (74d45988, 9844fd34; S16, B2). This shows AA's own scope; it is not evidence about other sites.
- **Partial combinations.** RemakeBench: per-round quality evidence for four models, a cross-vendor allowance table, API-equivalent task costs with the subscription charge recorded as zero, and one model's 18 tasks costed at $1,267, which is 58.8% of a week of allowance (76be258a, eaceded4, 2bde0a91, 13640ab8, 1032adb2; S109, S108, S54), but "There is no aggregate score" (76be258a; S109). Klu: a subscription-only model on the Klu Index (97) with plan prices of $50 and $200 in a footnote, price shown as "Subscription", no value metric computed (c1866a94, 909140e0; S18, C3).
- **Cost side only.** aipricing.guru (1ab603f6, 03d44a0c, 4be107a3; S44, C2), SemiAnalysis (14b6f5f0; S46 C3, S50 B2), Wokey (5111682e; S52).
- **Second-pass negatives.** Twelve consumer plan guides convert no allowance to dollars and join none to quality (C24); Tembo and Fast.io join quality to API cost only (b84150a1, d9c7238c; S100, S102); GitHub Copilot and Cursor publish credits or multiples (C22); Chinese vendor plans use requests and prompts (C23); Hacker News and Reddit items are single-user allowance estimates (C28); Vellum (49d65d22; S19), Scale (15691b7c; S20), BenchLM (3accb461, ab48edab; S29, S106) show no plan pricing; LMArena only as a D4 relay (c766eba2; S13).
- **Not tested.** Gemini primary plan pages (only consumer guides mention Gemini); five lead-scan pages (discretestack, neura.market, aiven, yourgpt, llmleaderboard.in); two Morph pages (HTTP 429, S98, S99); SemiAnalysis's paywalled third-party plan section (S50); X posts; Reddit except through mirrors.
- **Outcome: BOUNDED-NEGATIVE, definition-dependent** (re-graded from "PASS-AB for the AA boundary"). Several pages that lack the feature (more than twenty C-grade or lower pages across C1 and the second pass) and no page that has it. Absence claim, never provable.

### C2. Several sites offer API price-performance views (assumption A2)

- Artificial Analysis publishes Intelligence Index versus Cost per Task, Total Cost and Score versus Total Cost with a Pareto line (914291b0, 7c59143f, 33176205, 259ee057, 908b508c; S15, S36, B2).
- Independent aggregators with explicit value or cost-per-task views: BenchLM (15d3a9b9; S29), TokenCost (4af6f42f; S31, B2), Model Price Watch (bb6276e7; S38), CostGoat (970e3151; S34), LM Market Cap (69984bac; S40), AI Model Comparison (9d51c84e; S41), Dervity (7fca5fa3; S42), WhatLLM (a1cd5428; S39), Swfte (7a21bae0; S43), Klu (db54c221; S18), LLM Stats (03e2225b; S7), KickLLM (40ddcda8; S32) and Analytical Insider (04e2b86b; S33). That is **thirteen aggregators**: twelve in report Table 2 plus LM Market Cap (Score/$ column, formula not read). Fast.io (d9c7238c; S102) and Tembo (b84150a1; S100) join quality to API cost without a formula or from the SWE-bench board.
- **Outcome: PASS-AB.** A2 is confirmed. See C3 for the dependence on AA.

### C3. Artificial Analysis is the shared upstream for part of the API value views

- Corrected count (refine): **five of the twelve** aggregators in report Table 2 take AA cost or the AA index. Klu "retain[s] Artificial Analysis's measured pricing" (f14c55f8, f76d8c15; S18). WhatLLM data "is pulled from Artificial Analysis" (92b36303; S39) and "remains subject to Artificial Analysis and provider terms" (d6fce15d; S105). Dervity's cost per task is "from Artificial Analysis" (7fca5fa3; S42). AI Model Comparison divides the AA index by a blended price (9d51c84e; S41). Analytical Insider divides the AA Intelligence Index by blended price (04e2b86b; S33). Epoch's price-trend work uses AA and Epoch data (0be486bd; S70, search-summary paraphrase, 0.7). ValueRank itself builds on AA (cabcc834; S91).
- **Seven of twelve are not documented as AA-derived** on the pages read: BenchLM, Model Price Watch, TokenCost, CostGoat, KickLLM, Swfte, LLM Stats (list prices or composites of other benchmarks). The earlier wording "most aggregators inherit AA" was an overstatement and is withdrawn.
- **Outcome: PARTLY CONFIRMED** (PASS-3C on the five: S18, S39, S42 C3 plus S105 B2 for WhatLLM; B2 anchor S70). The consequence is a correlation risk for those five, not for the field.

### C4. "Value" formulas differ across sites, so value leaders can differ

| Site | Formula as stated | Evidence | Grade |
|---|---|---|---|
| BenchLM | overall weighted score ÷ output price per 1M tokens | 15d3a9b9, d0d37a3c | C2 |
| Model Price Watch | average benchmark score ÷ blended price, blend (3×input + output) ÷ 4 | bb6276e7, 86ac17e3 | C2 |
| TokenCost | quality (0.6 SWE-bench Verified, 0.4 Terminal-Bench 2.1) ÷ blended $/1M (0.75 input, 0.25 output) | 4af6f42f, 446c1d01 | B2 |
| CostGoat | quality ÷ output price, with a quality floor | 970e3151, 562e8998 | C2 |
| KickLLM | 60% quality (MMLU, HumanEval) with inverse blended cost and 10% breadth | 40ddcda8 | D3, stale |
| Analytical Insider | AA Intelligence Index ÷ blended price (3:1), normalised; the formula does not reproduce the table | 04e2b86b, 4398bc75 | D3, stale |
| AI Model Comparison | AA index ÷ blended price (75/25); inferred, not defined | 9d51c84e | C3 |
| Swfte | composite quality ÷ cost, weights unpublished | 7a21bae0 | C3 |
| Klu | "best value" is simply the lowest price | 9d1cd4ef | C3 |
| Dervity, WhatLLM, AA | measured cost per task including reasoning tokens | 7fca5fa3, a1cd5428, 914291b0 | C3, C3, B2 |
| SuperCLUE | average price per question over one agentic task | 0f67abb0, 952aa8d4 | B2 (secondary) |
| ValueRank | AA total cost ÷ highest eligible plan Value Multiple ÷ AA Intelligence Index (USD per Index point) | cabcc834 | A1, conflict of interest |

- **Value leaders can differ by formula (two sites compared).** BenchLM's top entry is Qwen3.7 Flash (score 46.9 at $0.13 per 1M output tokens) and BenchLM itself warns that "a very cheap model with a modest overall score can rank high here" (d0d37a3c; S29). Klu's "best value" is Ling 3.1 Flash at $0.45 (9d1cd4ef; S18), while Klu's own top-index model is Claude Opus 5.5. Two sites, two formulas, two different low-cost leaders. TokenCost says its blend assumption "moves the value ranking" (446c1d01; S31, B2).
- **Gap.** The corpus holds leader names for only two sites; a full cross-site leader table was not captured. Do not claim a numeric disagreement beyond these examples. Wording in the report was softened (refine) to "leaders can differ by formula"; Klu's "best value" is the lowest listed price, a different definition of value and not a ratio. **AA-derived** (report Table 2): AI Model Comparison (index), Analytical Insider (index), Klu (cost), WhatLLM (cost), Dervity (cost); the other seven are not.
- **Outcome: PASS-AB** (S31 B2 plus ten C pages). Each formula is confirmed on the site's own page (PASS-PRIMARY per site).

### C5. Token-price and blended-price views understate or distort run cost because of reasoning tokens, caching and output pricing

- KickLLM concedes list-price blended cost misses thinking tokens: "actual cost per task can be 2-8x higher" (4ccdfabd; S32, D3, single self-description). Output tokens cost three to ten times input tokens (4d70e4b1; S75, C3). A search-summary of an AA study reports o1 generating over 44 million tokens versus about 5.5 million for GPT-4o and $2,767 to run (8d9dcf1e; S79, B3, confidence 0.65). AA's page records a model that generated 350M tokens against a median of 67M (7e5b9eb0; S3, B3, confidence 0.4, seen in search only). Arize (10 models, 40 tasks, 2,400 runs) argues cost per successful task "can diverge from token price by more than an order of magnitude and inverts the ranking the pricing pages give you" (af55e562; S27, C2, commercial interest). AA reasoning models run at their maximum output budget (abe197f7, e318ff62; S1, B2).
- **Outcome: PASS-3C** (S27, S32, S75) with a B2 methodological anchor (S1). Magnitudes are vendor claims; the direction is consistent.

### C6. BenchLM ranks "value" on output-token price alone and admits cheap-model bias

- Primary page only (15d3a9b9, d0d37a3c; S29, C2). Mirror page defines no formula and the equivalence is an inference (f4322a61; S30, C3).
- **Outcome: PASS-PRIMARY.** No independent confirmation.

### C7. Several benchmark owners publish measured dollar cost beside quality

- AA (S15, S16, S17; B2), Aider ("Total cost" per entry, formula not on the page; d7c705fd; S6, B2), Terminal-Bench (COST and TOKENS columns with separate model and agent columns; 4a2e26df; S9, B3), Vals AI (accuracy, cost and latency per leaderboard; 588860ca; S8, B3), HAL Princeton ("cost-aware" agent leaderboard with token cost per run; 5df0deae, 3d811810; S67, B2), LiveBench (a `cost_2026_06_25.csv` in the pinned release data; 6e694250; S90, A2 for the file's existence; what it measures is undocumented in retrieved text, see C15).
- **Outcome: PASS-AB.** Absences recorded with caveats, not asserted: the Epoch benchmark hub shows no cost view in the fetched excerpt (c1c11133; S4, B2, confidence 0.5); the Scale leaderboard text contains no cost terms (cc0dc2d0, 15691b7c; S11 F6 unfetched, S20 B3); cost is not visible in the truncated SWE-bench fetch (a88a8606; S10, C3).

### C8. Plan-allowance value has been measured in five distinct classes, with different grades

1. **Controlled or account-based measurement**: SemiAnalysis isolates each token type with targeted prompts, records meter movement until error is within about 5%, then prices at API list rates (2e78f470, 78455d48; S50, B2; paraphrase from a fetch summary, 0.7; third-party plan section paywalled). Wokey remeasures weekly from real subscription accounts, five-account gate, manual check above 15% (52ceba1b, 5111682e; S52, C2). RemakeBench publishes a weekly allowance snapshot dated 2026-09-25 (53a223b7, f157c276, 638d773c; S53, S107); its Max 20x method page divides one account's logged spend by the app-reported 58% of a weekly quota over one week and notes that the plan string reads "Pro" (98008266, efe28642, 2edf813b; S108).
2. **Single-seat or single-author measurement**: ml0x parses 14,973 local session files on one Max 20x seat (1080b94f; S51, C3); Inventive HQ measures Codex plans from session logs and bar percentages (8dc04381, eab14dcf, a889863b; S116, C3); a Hacker News proxy post estimates Max 20x at about $1,949 per week from 11 sessions (b32605eb; S118, C3); a Hacker News comment reports about $2,200 per week for Pro 20x (98972d5b; S117, D4).
3. **Local trackers**: ai-usage-tracker (dfe9a829, 98c12605; S57, C2), claude-usage-tracker (857ab269; S58, C3), lpm (061c9777; S61, C3).
4. **Vendor-stated limits and guides**: aimodelscompared, exploreaitogether, fuelgauge, userightai (a5cec89b, d9628af1, ae8875e6, da421149; S55, S56, S59, S60; C2/C3). Copilot credits are vendor-defined at API rates (C22).
5. **Qualitative comparison pages** (new): eight further consumer pages compare tiers in words, ratings or multiples (S92 to S97, S101, S103; C24).
- **Outcome: PASS-AB** (S50 B2). The measured-versus-claimed separation holds: class 4 and 5 are provider claim or opinion, class 3 is user-local estimate, class 2 is single-user measurement, class 1 is controlled measurement of varying grade.

### C9. Plan-allowance comparisons exist mostly as posts and trackers rather than maintained rankings (assumption A3)

- **Supports A3**: twelve consumer guides state vendor limits or give verdicts (C24); individual measurements live in posts (S116, S117, S118, S119, S51); trackers are meters, not rankings (S61 to S64); SemiAnalysis is a dated analysis post (S50); Copilot and Cursor have vendor tables and no independent measurement (C22).
- **Counter-evidence**: Wokey publishes a weekly remeasurement with stated gates (S52), and RemakeBench keeps a dated Capacity Index with a cross-vendor table (S53, S107). aimodelscompared keeps dated update logs and says "Not published" rather than estimating (e595b5bf, c36ddee6; S55). These are maintained but rank plans, not models with quality.
- **Outcome: PARTLY REFUTED / NARROWED** (PASS-3C on the pattern, with two maintained exceptions). Restated: maintained plan-allowance measurement exists at two sites, but it is plan-level and quality-free; no maintained model-level ranking was found.

### C10. Allowance figures for Claude Max 20x: like-for-like comparison (revised in refine)

**Allowance measurements** (the API-list value of what the weekly limit permits), ascending:

| Source | Figure | Window or date | Priced model and method | Weekly | Monthly multiple (x4) | Grade |
|---|---|---|---|---|---|---|
| Wokey (S52; 5111682e) | about $1,751 per week | 2026-10-05 to 10-12 | official API list rates; median of account medians, at least five accounts | 1,751 | 35.0x | C2 |
| Hacker News proxy (S118; b32605eb) | about $1,949 per week (5-hour median $164) | posted 2026-03-26 | header-capturing proxy, 11 sessions, price-weighted quota, own tool | 1,949 | 39.0x | C3 |
| RemakeBench (S107, S108; 638d773c, 98008266, efe28642, 2edf813b) | about $2,155 per week | 2026-09-24 to 10-01 | one account, Opus 5.5 in Claude Code; $1,249.83 divided by 58% of weekly quota; plan string reads "Pro"; Medium confidence | 2,155 | 43.1x | B2 (store) |
| SemiAnalysis via explainx (S46; 14b6f5f0; primary S50 2e78f470) | about $11,726 per month of Opus 5.5, 58.6x | published 2026-10-05 | controlled token-type meter measurement | about 2,710 to 2,930 | 58.6x | C3 (primary B2, partly paywalled) |

- **Arithmetic (analyst's, not stated by sources).** The weekly spread is $1,751 to $2,931, **1.7x** (1.5x if the SemiAnalysis month is divided by 4.33); monthly multiples 35x to 59x. Wokey and RemakeBench differ by about 23%. RemakeBench's stated range $2,136 to $2,174 is rounding of the displayed 58% (1,249.83 divided by 57.5% to 58.5%), not repeated measurement.
- **Consumed workload, kept separate.** ml0x: one seat's use over 2026-07-29 to 08-28 priced at Opus 5 list rates, $26,187 per month (about $6,050 to $6,550 per week; 131x the fee), 96.4% cache hit (1080b94f; S51, C3). It is 2.2x SemiAnalysis's monthly figure, which a consumption total should not exceed if both were priced alike; the window predates the 13 September expiry of a temporary 50% increase (c36ddee6; S55), which explains at most 1.5x. It is an upper-envelope consumption datapoint and is not used to bound the allowance. A Reddit comment of "$1k+" on a $200 plan gives no window (275bc8fa; S120, D5).
- **Candidate explanations** (none verified): date, priced model, cache treatment, workload shape, silent limit changes (e85fd81e).
- **OpenAI $200 plan by date.** HN comment about $2,200 per week, "Pro 20x $200", GPT 5.6 Sol, 2026-07-18 (98972d5b; S117, D4); RemakeBench about $1,532 per week, 2026-09-25 (638d773c; S107); Inventive HQ about $650 per week for the "new 10x tier", about $1,300 grandfathered until 29 October, 2026-10-04 (8dc04381, a889863b; S116, C3); SemiAnalysis via explainx about $2,084 per month of GPT-6.1 Sol, which is about $480 to $520 per week, 2026-10-05 (14b6f5f0; S46). The fall with date and label is consistent with the SemiAnalysis summary that OpenAI halved the $200 plan's value (e85fd81e), not proved.
- **Outcome: CONTESTED WITHIN A RANGE.** No A or B source fixes one Max 20x allowance. Report a dated range with measurement class. Wokey's Max 20x-to-Pro weekly ratio of about 10x (e62e5e35, 5111682e; S52) is single-sourced but consistent with the five-hour-window statement (d9628af1; S56) and with weekly caps governing the month (78455d48; S50).

### C11. Plan allowances are opaque, model-specific and unstable

- Anthropic publishes no absolute message counts at any tier while OpenAI publishes Codex ranges (a5cec89b; S55, C2). A temporary 50% Claude Code weekly increase expired on 13 September and "never appeared in docs" (c36ddee6; S55). Grok plans were replaced on 2026-10-12 (122468a8; S56). Fable usage counts against only half of a $200 plan's limit (03fd0f2c, ee31ae11; S46, S50). An A/B test gave one account about 20% lower limits (e85fd81e; S50). Weekly caps are unpublished so "the multiple can change without a price change" (2c407573; S51).
- **Outcome: PASS-AB** (S50 B2 plus S51, S52, S55, S56). This is the strongest argument that any plan-cost ranking needs dated, model-specific, graded evidence.

### C12. Dated, exact-variant, graded evidence is rare (assumption A4)

- **Counts over the twelve aggregators of report Table 2 (analyst's tally).** Calendar date on the page: nine (BenchLM 3accb461, Model Price Watch, CostGoat, KickLLM d610547b, Analytical Insider 4398bc75, Swfte, Klu 9d1cd4ef, Dervity, WhatLLM methodology d6fce15d); absent at TokenCost, AI Model Comparison, LLM Stats; two of the nine are months-old publication dates. Variant or effort named: three (Klu 29d011bd, Dervity 7fca5fa3, TokenCost 0e55597d). Formula stated: six (BenchLM, TokenCost, Model Price Watch, CostGoat, KickLLM, Analytical Insider, the last irreproducible). Imputation or missing-value policy: two (TokenCost 473fb9be; BenchLM 12b04552, ab48edab).
- **Outside the twelve.** Variant plus effort in the label: AA (c6e57b1d; S3), Aider (d7c705fd; S6), OckBench (decb4d7c; S88, via search summary), SuperCLUE "GLM5.2 (max)" (a91b5530; S81). Model and agent separated: Terminal-Bench (S9). URL-and-date logging with "Not published": aimodelscompared (S55). Stated cadence and gates: Wokey (S52). Uncertainty or integrity markers: Terminal-Bench confidence intervals and canary string (S9), Scale score intervals (S20), BenchLM estimated versus supported positions (12b04552; S106).
- **Practices not found.** No site was found that labels each number as measured, provider claim, estimate or assumption (59a69c9a; S87, three searches and one topic listing, confidence 0.55). BenchLM is a partial analogue at row level (vendor-run numbers labelled and kept out of rank; estimated positions marked), with no assumption class and no per-number label. Several sites show no formula or weights (S7, S43, S41), stale or irreproducible tables (S32, S33, S49, S59).
- **Outcome: SPLIT.** Dating is common (nine of twelve); exact-variant labelling is a minority practice among aggregators (three of twelve) though standard at AA and the benchmark owners; imputation policies are rare (two); evidence-class grading is BOUNDED-NEGATIVE with a partial analogue. The earlier wording "common among the better sites" was circular and is withdrawn.

### C13. Several value pages are stale, unreproducible or unverifiable

- KickLLM was published 2026-04-07 and cites MMLU and HumanEval (d610547b, 40ddcda8; S32, D3). Analytical Insider is dated 2026-03-21 and its stated formula does not reproduce its table (DeepSeek V3: 86 ÷ $0.19 versus the listed 88; 4398bc75; S33, D3). Permutable cites AA Index v2 from February 2025 (83b688d2; S49, D4, search snippet). Fuelgauge is dated 2026-03-25 (S59). Vellum shows "updated Mon Sept 28" without a year (61883132; S19).
- **Outcome: PASS-3C** (S32, S33, S59, each independently dated). Low-grade pages should not drive findings; they are used only as examples of the problem.

### C14. A cost-aware evaluation literature predates and supports price-performance ranking

- HAL (5df0deae, bbcacbb0, 8a1f436a: "agents can be 100x more expensive while only being 1% better"; S67, B2), AI Agents That Matter ("jointly optimizing" cost and accuracy; c618e708, 489ab308; S68, B2), Cost-of-Pass (expected monetary cost of a correct solution; ce5df1a5, d98b684f, 98126ceb; S69, B2), The Price of Progress (benchmarks may present "a warped picture" of capability per dollar; 5cbc378b, 4a431957; S71, B2), Epoch price trends (9x to 900x per year price decline at fixed capability; 55bf436e, ae8683ba, 4882375a; S70, B2), the Stanford AI Index (more than 280-fold fall in inference cost at GPT-3.5-level capability; b3eca6ac; S84, A1).
- **Outcome: PASS-AB.** These are research and trend sources, not site rankings; they support the framing and the critique, not the site map.

### C15. Cost per success or per pass is argued to be a better unit than token price

- Cost-of-Pass (S69, B2); Arize (S27, C2); DoiT (f1e4aa6c; S47, C2, author at a cost vendor); HAL (S67). AA's total cost is token prices times tokens used across the evaluations, excluding repeats, with no division by the number of correct answers (e3f14e77; S17), and its cost per task is a weighted average over tasks (914291b0; S15). Neither definition, as quoted, conditions on correctness, so AA's spend **includes** tokens used on failed attempts and is **not divided by the number of successes**. The earlier statement that AA's figure "does not count failures" was wrong and is withdrawn.
- LiveBench's release data includes `cost_2026_06_25.csv` (6e694250; S90); ValueRank ingests it under a field named for cost per successful task; **no retrieved LiveBench text says what the file measures** (S21 and S131 READMEs link datasets and cover running evaluations only). The file is carried as a measured-cost file of unconfirmed definition (refine; delta cycle 1 #7).
- **Outcome: PASS-AB** for the AA-versus-cost-per-success distinction; the LiveBench unit is UNCONFIRMED.

### C16. A Chinese leaderboard now publishes a cost quadrant (SuperCLUE); the primary page is unconfirmed

- Jingji Cankao Bao (read through Eastmoney) states that on 30 June SuperCLUE "first released" a "Token cost quadrant" with task average score and average price per question, a nearly 20x price spread across seven domestic models on one engineering task needing dozens of dialogue turns, and a task-average-score gap above 70% between models (0f67abb0, 952aa8d4; S81, B2, direct Chinese-language reading by the retrieval agent). It names GLM5.2 (max) as top on score and price and MiMo-V2.5-pro as lowest price (a91b5530). Ifeng, via a search summary, says the same (7ff0e0b5; S78, C3). SuperCLUE's site is client-rendered; only its title was retrievable (77e281ff; S76, C3).
- **Manual translation check (refine).** The automatic claim verifier scored the English claim 0.15 against the Chinese quote (lexical artefact). The quoted paragraph 0f67abb0 was compared by hand: "average price per question differs by nearly 20 times; the highest task average scores differ by more than 70%". The report now says task average scores differed "by up to more than 70%" between models.
- OpenCompass: CompassRank returned only a title (58cdb110, 8e9d1f52; S77, S82); the README shows no cost feature (03c1402e; S83, A2). HELM: unconfirmed (bb932b80; S80). Chinese vendor coding plans are in C23. A Chinese-data economics paper reports an optimal cost-effectiveness zone (09479d4e, ab211925; S72, C3).
- **Outcome: SECONDARY-ONLY.** Two secondary sources agree, one B2; the owner page is unverified. SuperCLUE's May 2026 report has no cost dimension (c2ae2dbc; S78). OpenCompass and HELM cost treatment: UNSUPPORTED (gap, not a negative).

### C17. Hugging Face leaderboards do not rank on dollar cost

- The Open LLM Leaderboard v1 was archived in June 2024 (c153561d; S22, A2) and the project was reported ended around 2025-03-13 (0cd71aec; S24, C3, relayed). AI Energy Score measures energy per task (65b356b1; S25, B2) and LLM-Perf reports latency, throughput, memory and energy (cb19586c; S26, C3).
- **Outcome: PASS-AB.** They are out of the value set; they matter only as an "efficiency, not dollars" contrast.

### C18. Business models and independence vary and often involve affiliate links, ads or a gateway

- CostGoat discloses affiliate revenue and sells a spend-tracking app (42644209; S34); aitoolsrank has an affiliate model (e6519f8f; S45, D4); PricePerToken carries a sponsor banner (ea9b99aa; S35); Swfte promotes its own routing gateway (1529de55; S43); AI Model Comparison has a freemium Premium plan (bd5cb715; S41); LLM Stats offers a paid Data API and benchmarking services (b9515747, 47ac31ac; S7); Arize and DoiT are vendors with a commercial interest in cost-per-task framing (S27, S47). OpenRouter ranks popularity by token volume, not value (0be25505; S37, B2). Not Diamond appears only in a third-party directory with unverified vendor figures (924bf475; S89, D4).
- **Outcome: PASS-3C.** Independence is the rule's exception rather than the rule.

### C19. Artificial Analysis dollars are partly modelled, index definitions change across versions, and reuse is restricted

- Cost uses provider-reported token counts with a canonical-tokenizer fallback and live cache-hit-rate measurements rather than the one-off run (7d96aabd, b4fc294d, 744c471c; S1, B2). For at least one component the published cost covers contestant calls only (31ef13c9; S1). The Index moved from v4.0 to v4.1 and is v4.3.2 on the live page with ten evaluations (0555c470, ce935918; S2 B3, S15 B2); a lagging snippet and the live page disagree (X9). AA's methodology calls itself "a more useful synthesis comparison … than any other metric in existence today" (29fb5308; S2), a self-assessment.
- Reuse terms: see C26.
- **Outcome: PASS-AB.** The upstream on which much of the landscape (and ValueRank) rests is a single commercial vendor whose cost is a hybrid of measured and modelled quantities, under restrictive default reuse terms.

### C20. ValueRank's distinct feature set is the combination of plan cost per Index point, exact-variant policy and graded evidence

- ValueRank's methodology (S91; cabcc834) defines Plan Costs as AA total cost divided by the model's highest eligible subscription Value Multiple, divided by its AA Intelligence Index. The scope document lists the exact-variant evidence policy and the four evidence classes. No other page in the corpus (C1, C12) shows all three; BenchLM is a partial analogue on the third (S106).
- **Outcome: PASS-PRIMARY with conflict of interest.** S91 is graded A1 as the baseline but the research is commissioned by ValueRank's owner (bias flag `conflict_of_interest`); "alone" is a statement about this search, not about the market. Internal project documents (AGENTS.md instructions designating SemiAnalysis; an internal site audit) are marked "(internal context)" in the report and are not evidence. Counter-weights are in report F11 ("Where ValueRank is weaker").

### C21. Plan value is model-specific and cache-dominated, which constrains any model-level plan ranking

- On some plans, cache reads cost almost nothing and may not move the meter (3aa1df58; S50, B2, partial read); Wokey and ml0x say cache reads dominate long sessions and barely count (ac9a641a; S52; ac96d9e5; S51). The evidence is for Anthropic plans; it is **not established for OpenAI or other plans**. Per-model meters mean the multiple differs by model (ee31ae11, 03fd0f2c; S50, S46). SemiAnalysis frames the work as financial modelling, not a buyer's guide (d25a2882; S50).
- **Outcome: PASS-AB, partial read.** S50's stored evidence is a tool summary (confidence 0.65 to 0.8) of a partly paywalled page; the grade rests on the source's method and reputation, not on a complete reading. Supports ValueRank's refusal to transfer a multiple across models, and flags that its plan basis inherits the "API-equivalent at list rates" convention of its numerator sources (see C27).

### C22. GitHub Copilot and Cursor plans use credits or multiples, not measured allowances

- Copilot: Pro $10 with 1,500 AI credits, Pro+ $39 with 7,000, Max $100 with 20,000; organisation seats carry credits worth their price; overage $0.01 per credit (7e6f689e, de844f80; S110, A1). Credits are billed by token consumption at each model's listed API rate since 2026-06-01 (05ba2e58, 42dbf841; S112, C3). Completions are outside the pool (ee4b9fc2). The earlier request scheme (300 and 1,500 premium requests, per prompt times a model multiplier) is legacy (6556af8e, add87d51; S111). If a credit is worth the overage rate the individual pools are worth $15, $70 and $200 (analyst's arithmetic), about 1.5x to 2x the fee; the page does not state the dollar value of the individual pools.
- Cursor: sold inside The X Subscription; Plus $8, Premium 4x, Super 15x, Ultra 50x of Plus (b2dcae7e; S115, A1); shared Grok and Cursor weekly pool (a44b6994); legacy Pro, Pro+, Ultra, Start, Teams plans (b549aa49); third-party model usage not included in the monthly price (b2d3102b; S114, A1). Independent comparison pages give pricing-model rows only (9d30f5e4; S113, D4); Morph pages were unreadable (S98, S99).
- **Outcome: PASS-AB (vendor pages, A1, plus one C3 independent source for Copilot).** No independent allowance measurement found for either; neither joins quality.

### C23. Chinese vendor coding plans use requests and prompts and are not joined to quality

- Zhipu: official page gives a starting price of 18 USD and no quota table (0e7df606; S124, A1); legacy plan without weekly caps stopped auto-renewing 2026-04-30 (48895292; S125, B2); a third-party roundup (flagged possibly outdated) lists 49, 149, 469 yuan and about 80 prompts per five-hour window (9fea609c; S123, D4). Alibaba Bailian Pro 200 yuan per month for 90,000 requests (5f750617; S126, B3, community-authored). Kimi tiers 468 to 6,708 yuan a year via a relay (bb1a18c3; S127, C4); official page shows no quotas in rendered text (bc32f793; S128). DeepSeek is pay-per-token (cdc87740; S123). CodePick compares by price, quota mechanism and scenario with no quality score (9ac64ac2; S122, S123).
- **Outcome: PASS-3C for "no quality join" (S122, S123, S124/S128 plus S126); quotas SINGLE-SOURCED and unverified against official tables.**

### C24. Consumer plan guides convert no allowance to dollars

- Read in the second pass: AiZolo qualitative verdict (fe1d6275; S92, D4); Vortenza adjectives and superseded models (f36641d0; S93, E5); Altai qualitative "wall" (adfc367e; S94, D4); Tech Insider relays third-party benchmark numbers (a7a06896; S95, E5); BSWEN one developer's trial with star ratings (da0f76c7; S96, E5); AionX relative multiples (8f989096; S97, D4); MemoryPlugin limits qualitatively (fb97cff0; S101, C3); Fello AI verdicts by user type (9132b3d7; S103, D4). With the four first-pass guides (S55, S56, S59, S60) that is twelve.
- **Outcome: PASS-3C** (twelve independent pages, none converts an allowance to API-priced dollars or joins one to quality). Low-grade pages carry only the negative.

### C25. RemakeBench publishes no aggregate score and its Max 20x allowance is one account in one window

- "Per-round evidence stays on each ledger. There is no aggregate score." (76be258a; S109, B2). Per-task cost is API-equivalent; marginal subscription charge $0 (eaceded4). The Capacity Index expresses 18 Opus 5.5 grid tasks at $1,267.39 as 58.8% of one week (2bde0a91; S108). Allowance is logged spend divided by app-reported 58% of weekly quota, one window 2026-09-24 to 10-01 (98008266, efe28642); the plan string reads "Pro" and confidence is Medium (2edf813b).
- **Outcome: PASS-PRIMARY.** Strong for the "no aggregate score" statement (own page); weak as an allowance measurement.

### C26. Artificial Analysis grants a personal, noncommercial licence and requires attribution for API use; LiveBench states no data licence

- AA Website Terms (revised 2026-09-15): licence "solely for your own personal, noncommercial use" (66405636; S129, A1); no commercial exploitation of the site or any content (26221e56); no copying or republishing without express permission (2.2(d), per the stored claim of 26221e56); no scraping or mining by automated means, conditional exception for public search-engine spiders (5ec475e6). Free API: attribution required; subject to Terms of Use and Data Platform Terms, which were not retrieved (44865d85; S130, A1). WhatLLM: third-party data "remains subject to Artificial Analysis and provider terms" (d6fce15d; S105, B2). LiveBench README: datasets on Hugging Face; GitHub licence field NOASSERTION; no data-licence statement found (source note only; S131, B2, no evidence row).
- **Outcome: PASS-PRIMARY for what the terms say. Whether ValueRank's use fits them is a legal question that depends on facts outside the corpus (how it obtains the data, any permission, the Data Platform Terms); the report does not answer it and it is not legal advice.**

### C27. ValueRank's plan formula inherits unstable assumptions (analyst's inference, not a sourced fact)

- The formula divides AA's cost (AA token mix, live cache-hit rates, reasoning models at maximum output budget: abe197f7; S1) by a highest eligible multiple calibrated under another mix (cabcc834; S91). Cache reads are nearly free on some plans (3aa1df58), so a multiple calibrated on a cache-heavy mix covers fewer list-price dollars of an output-heavy run, and AA cost divided by the multiple understates its plan cost (direction only; size not estimated; established for Anthropic plans only). The maximum of several noisy estimates is biased upward; the allowance spread is 1.7x (C10). The numerator is partly paywalled and read through a C3 summary (S46, S50). Multiples are model-specific (03fd0f2c, ee31ae11).
- **Outcome: INFERENCE.** Stated as the main decision risk; no ValueRank value was recomputed. Test proposed (report Recommendation 2).

### C28. Community posts carry individual allowance estimates, not maintained rankings

- Hacker News: proxy estimate of Max 20x (b32605eb; S118, C3), Pro 20x about $2,200 per week (98972d5b; S117, D4), a recollection of $10 to $20 per day on Pro (d0e08f79; S119, D4, confidence 0.4). Reddit mirrors (reddit.com blocked): "$1k+" on $200 Max with ccusage (275bc8fa; S120, D5) and a second-hand claim that the Max 20x weekly limit is only twice Max 5x (398207f6; S121, D5), unchecked.
- **Outcome: SINGLE-SOURCED each; used only as flagged datapoints (Tables 3 and 3b) or not at all.**

## 2. Contradictions and conflicts register

| # | Conflict | Sources and grades | Resolution status |
|---|---|---|---|
| X1 | Claude Max 20× weekly allowance: $1,751 (Wokey), $1,949 (HN proxy), $2,155 (RemakeBench), about $2,710 to $2,930 (SemiAnalysis, derived) | S52 C2, S118 C3, S107/S108 B2 (store), S46 C3 / S50 B2 | **Narrowed in refine to 1.7× on like-for-like allowance measurements** (35x to 59x monthly multiple); differences from date, priced model, method; no A/B anchor. ml0x ($26,187 per month, consumed workload) is a different quantity and is excluded (X16). |
| X2 | OpenAI $200 plan: $2,200 per week (HN, July) versus $1,532 (RemakeBench, 25 Sep) versus about $650 (Inventive HQ, new 10× tier, 4 Oct) versus about $480 to $520 (SemiAnalysis, 5 Oct) | S117 D4, S107, S116 C3, S46 C3 | Explained in direction by date and plan label (OpenAI halved the $200 plan's value, S50 paraphrase); not proved that the labels name one product. |
| X3 | SemiAnalysis secondary summary says "about 4x" for Opus 5.5 versus GPT-6.1 Sol while its quoted figures ($11,726 versus $2,084) imply about 5.6× | S46 C3, S50 B2 paraphrase | Unresolved; do not cite a single multiple without the primary. |
| X4 | Value leaders can differ by formula (Qwen3.7 Flash at BenchLM versus Ling 3.1 Flash at Klu, the lowest listed price) | S29 C2, S18 C3 | Explained by formula, not contradiction. |
| X5 | LiveBench: live site and README yielded no cost view, but the pinned release data contains a cost file | S5 C4, S21 B3, S131 B2 versus S90 A2 | Resolved for **existence** of a cost file (retrieval artefact). **Open for its definition**: no retrieved LiveBench text says what it measures; Table 6 cell graded A2 for file existence only. |
| X6 | LMArena: secondary relays say it shows token pricing and a cost-per-task Pareto in Agents; no primary page was readable | S13 D4, S14 D4, S28 E5 | Unresolved; recorded as reported, not confirmed. E5 source must not carry a claim. |
| X7 | SuperCLUE quadrant: primary page unreadable | S81 B2, S78 C3, S76 C3 | Secondary-only. |
| X8 | Epoch, Scale, SWE-bench: "no cost view" found in excerpts, but fetches were truncated or tool-summarised | S4 B2 (0.5), S20 B3, S10 C3 | Treated as absence-in-fetched-text, not as proof. |
| X9 | Methodology snippet (v4.1, ja page) versus live Index page (v4.3.2) on AA composition | S2 B3 versus S15 B2 | Live page preferred; S2 is stale. |
| X10 | Cost-per-task magnitude of reasoning overhead: 2–8× (KickLLM) versus order-of-magnitude (Arize) versus 3–10× (output/input price ratio, a different quantity) | S32 D3, S27 C2, S75 C3 | Not comparable; direction agrees. |
| X11 | LLM Stats says price is folded into its composite (no formula), Klu says price is excluded from its index | S7 C3 versus S18 C3 | Real design difference; both confirmed on own pages. |
| X12 | A3 (plan comparisons are mostly posts) versus Wokey's weekly maintained measurement and RemakeBench's dated index | S52, S53 | A3 partially refuted; see C9. |
| X13 | RemakeBench Max 20× attribution: headline table says Claude Max 20×, method page says the measured account's plan string reads "Pro" | S107 versus S108 (same site, B2 store grades) | Open; confidence rated Medium by the site; weight reduced. |
| X14 | Cursor and Copilot plans: older $20/$60/$200 and premium-request comparisons versus current X Subscription and AI-credit plans | S111, S115 legacy notes versus S110, S114 | Resolved: legacy schemes are superseded; older comparison pages describe superseded plans. |
| X15 | AA default licence (personal, noncommercial; no scraping or commercial exploitation) versus pinned-snapshot reuse by ValueRank and redistribution by aggregators | S129, S130 versus S91, S105 | Open legal question; corpus lacks the Data Platform Terms and ValueRank's acquisition route. Not legal advice. |
| X16 | ml0x consumed workload ($26,187 per month) versus SemiAnalysis full monthly limit ($11,726) | S51 C3 versus S46 C3 / S50 B2 | Different quantities (consumption versus allowance), 2.2× apart at similar list pricing; a temporary 50% increase explains at most 1.5×; kept out of the allowance range. |

No A/B-graded source conflicts with a D/E-graded source on a core claim, apart from X6 (D4/E5 relays about LMArena, with no A/B reading available), so no extra adversarial pass was triggered by the escalation rule beyond the scheduled critique.

## 3. Core-claim status summary

| Claim | Outcome |
|---|---|
| C1 no site combines quality and plan cost (A1) | BOUNDED-NEGATIVE, definition-dependent (partial combinations: RemakeBench, Klu) |
| C2 several API price-performance sites (A2) | PASS-AB |
| C3 AA is the shared upstream | PARTLY CONFIRMED (five of twelve aggregators; B2 anchor) |
| C4 formulas differ, leaders differ | PASS-AB (leader comparison limited to two examples) |
| C5 reasoning tokens distort list-price views | PASS-3C (magnitudes are vendor claims) |
| C6 BenchLM output-price-only value | PASS-PRIMARY |
| C7 benchmark owners publish measured cost | PASS-AB |
| C8 five classes of allowance evidence | PASS-AB |
| C9 plan comparisons mostly posts/trackers (A3) | PARTLY REFUTED / NARROWED |
| C10 Max 20× allowance, like for like | CONTESTED WITHIN A RANGE (1.7×) |
| C11 allowances opaque and unstable | PASS-AB |
| C12 provenance practice (A4) | SPLIT: dating 9 of 12; variants 3 of 12; imputation 2; evidence-class grading BOUNDED-NEGATIVE |
| C13 stale and unreproducible pages | PASS-3C |
| C14 cost-aware literature | PASS-AB |
| C15 cost per success argument | PASS-AB |
| C16 SuperCLUE cost quadrant | SECONDARY-ONLY; OpenCompass and HELM UNSUPPORTED |
| C17 Hugging Face boards not dollar-based | PASS-AB |
| C18 business models | PASS-3C |
| C19 AA cost is hybrid; versions change | PASS-AB |
| C20 ValueRank's distinct combination | PASS-PRIMARY (conflict of interest) |
| C21 plan value is model-specific and cache-dominated | PASS-AB, partial read (Anthropic plans) |
| C22 Copilot and Cursor use credits or multiples | PASS-AB (vendor pages) |
| C23 Chinese plans use requests or prompts, no quality join | PASS-3C; quotas single-sourced |
| C24 twelve consumer guides convert no allowance to dollars | PASS-3C |
| C25 RemakeBench: no aggregate score; one-account allowance | PASS-PRIMARY |
| C26 AA terms: personal, noncommercial licence; attribution for API | PASS-PRIMARY; legal application OPEN |
| C27 ValueRank's plan formula inherits unstable assumptions | INFERENCE (main decision risk) |
| C28 community posts are individual estimates | SINGLE-SOURCED each |

**Single-sourced or unsupported after triangulation:** C6 (one page per site, as expected for self-description); the Max 20×/Pro weekly ratio of about 10× (Wokey only, S52); C10 exact allowance (contested within 1.7×, no A/B anchor; RemakeBench is one account, one window); C16 SuperCLUE primary (secondary-only); OpenCompass, HELM and SWE-bench cost treatment (unsupported, fetch failures); LMArena price display and agent cost Pareto (D4 relays only); evidence-class grading absence (single search log, 0.55); SemiAnalysis headline multiples (secondary only; primary partly paywalled); Chinese plan quotas (third-party); LiveBench cost-file definition and data licence (no retrieved text); AA Data Platform Terms (not retrieved).

## 4. Sites register

Columns: **Value framing** is how the site presents value; **cost basis** is one of list price per token (LP), blended price (BP), measured cost per task (MCT), total benchmark cost (TBC), plan allowance (PA); **plan** is whether subscription plans are covered; **overlap** with ValueRank is none, API basis, plan basis, or data supplier. Best-source grade is the highest-graded source about that site in the corpus. "n/s" means not stated on the page read.

### 4.1 API price-performance and cost-per-task aggregators

| Site | Value framing | Cost basis | Plan | Provenance | Cadence | Audience and model | Best grade | Overlap |
|---|---|---|---|---|---|---|---|---|
| Artificial Analysis (S15, S16, S36) | Intelligence Index versus cost per task, total cost, Pareto, "most attractive quadrant" | MCT, TBC (token prices × provider-reported tokens, live cache rates) | explicitly excluded | method page; version labels; variant and effort named; costs partly modelled | live page dated 2026-10-17; no stated schedule | developers and buyers; commercial | B2 | API basis; data supplier |
| AA Coding Agent Index (S16) | index versus average cost per task per agent variant | MCT at pay-per-token rates | excluded; acknowledges plans | simple average of three benchmarks | dated 2026-10-17 | coding-agent buyers | B2 | API basis; data supplier (DeepSWE, TB 4.0) |
| BenchLM (S29, S30) | "Best value overall": score ÷ output price | LP (output only) | none | formula stated; cheap-model caveat | updated 2026-10-17 | general; commercial | C2 | API basis |
| TokenCost (S31) | quality ÷ blended price | BP (0.75/0.25) | none | method, no imputation, exclusions listed | n/s | analysts; funding unknown | B2 | API basis |
| Model Price Watch (S38) | performance per dollar | BP (3:1) | none | formula stated | 2026-10-17 | general; funding unknown | C2 | API basis |
| CostGoat (S34) | quality ÷ output price, quality floor | LP (output) | none | third-party quality source; affiliate disclosed | 2026-10-16 | developers; affiliate | C2 | API basis |
| LM Market Cap (S40) | Score/$ column, Best Value card | LP | none | composite 90/10 | hourly | general; commercial | C3 | API basis |
| WhatLLM (S39) | "Best task cost" | MCT (from AA) | none | AA-derived | auto-refresh | general; unknown | C3 | API basis |
| Dervity dashboard (S42) | cost of one benchmark task incl. thinking tokens | MCT (from AA v4.3.2) | none | AA-derived | 2026-09-01 | general | C3 | API basis |
| AI Model Comparison (S41) | "most intelligence per dollar" | BP (75/25, inferred) | none | formula not defined | undated | freemium | C3 | API basis |
| Swfte (S43) | Value Score = quality ÷ cost | n/s | none | weights unpublished | 2026-10-17 | lead generation for a gateway | C3 | API basis |
| Klu (S18) | Klu Index versus price and cost per reasoning effort | BP (from AA), MCT per effort | footnote only | weights stated (35/30/20/15), price excluded from index | 2026-10-13 | general; commercial | C3 | API basis |
| LLM Stats (S7) | composite of intelligence, speed, price | LP | none | TrueSkill composite of others' results; no price formula | continuous | developers; paid API | C3 | API basis |
| Vellum (S19) | separate price table, cheapest list | LP | none | mixed provider-reported and independent | "updated Sept 28" | enterprise | C3 | API basis (weak) |
| PricePerToken (S35) | price tracking | LP | none | no value formula | 2026-10-17 | developers; ads | C3 | none |
| llm-price / ailesson (S48) | calculator | LP | none | n/s | 6-hour cache | developers | C3 | none |
| KickLLM (S32) | composite value index | BP | none | stale (2026-04-07), weak benchmarks | stale | marketing | D3 | API basis (unreliable) |
| Analytical Insider (S33) | value score, top 50 | BP | none | irreproducible | stale (2026-03-21) | marketing | D3 | API basis (unreliable) |
| Permutable (S49) | enterprise comparison | n/s | none | AA v2 basis, not fetched | 2025-06-02 | enterprise marketing | D4 | none |
| Fast.io (S102) | "price-performance sweet spot" in prose | LP, no formula | none | AA index and SWE-bench cited | 2026-06-14 | vendor promotion | D4 | none |
| Tembo (S100) | SWE-bench % resolved with average cost per task | MCT from SWE-bench board | none | republished official board | 2026-06 (captured) | vendor promotion | C3 | none |
| BenchLM methodology (S106) | score blend; vendor-run numbers labelled and kept out of rank; estimated positions marked; no imputation | LP | none | methodology page | undated | sells API and MCP data access | B2 | API basis |
| WhatLLM methodology (S105) | AA-derived scatter plots | from AA | none | editorial CC BY 4.0; data under AA terms | reviewed 2026-09-06 | redistributes AA data | B2 | API basis |
| Analytical Insider home (S104) | sales-lead service, not a value publisher | n/a | n/a | n/a | n/a | B2B lead generation | F6 | none |

### 4.2 Benchmark owners and evaluators with cost views

| Site | Value framing | Cost basis | Plan | Provenance | Cadence | Audience | Best grade | Overlap |
|---|---|---|---|---|---|---|---|---|
| Aider (S6) | polyglot pass rate with total cost per entry | MCT (per run total) | none | effort in label; formula not on page | n/s | developers; open source | B2 | none (comparable method) |
| Terminal-Bench (S9) | resolution rate with COST and TOKENS | MCT | none (agent and model separate) | 95% CI; canary string | n/s | agent builders | B3 | data supplier (TB 4.0 quality) |
| Vals AI (S8) | accuracy, cost, latency per leaderboard | MCT per benchmark | none | per-benchmark method pages | n/s | enterprise; commercial | B3 | none |
| HAL, Princeton (S67) | cost-aware agent leaderboard, Pareto | MCT | none | standardised, third-party | n/s | researchers | B2 | none |
| LiveBench (S90, S5, S21) | benchmark scores; release data includes cost file | MCT (per successful task) | none | pinned release commit | releases (2026-06-25) | researchers | A2 | data supplier |
| OckBench (S88) | reasoning efficiency score | output-only cost estimate | none | pins reasoning setting | n/s | researchers | B3 (search summary) | none |
| SuperCLUE (S81, S78, S76) | token cost quadrant (score versus price per question) | MCT on one task | none | secondary only | 2026-06-30 release | Chinese market | B2 (secondary) | none |
| LMArena (S13, S14, S28) | crowd preference; reported price display and agent cost Pareto | LP, MCT (unconfirmed) | none | not retrievable | n/s | general | D4 | none (unconfirmed) |
| Epoch AI hub (S4, S70) | capability tracking; separate price-trend analysis | n/a on hub; price at fixed capability in research | n/a | method pages; dated | updated 2026-10-17 | policy and research | B2 | none |
| Scale SEAL (S20, S11) | scores with confidence intervals | none | none | CIs | n/s | enterprise | B3 | none |
| SWE-bench (S10) | resolve rate | cost not visible | none | multiple leaderboards | n/s | researchers | C3 | none |
| OpenCompass (S77, S82, S83) | capability platform | not confirmed | none | open-source platform | n/s | Chinese market | A2 (README) | none |
| HELM (S80) | holistic evaluation | not confirmed | none | n/s | n/s | researchers | C3 | none |
| METR (S86) | task time horizon | none found | none | method post | n/s | researchers | A1 | none |
| Hugging Face boards (S22, S25, S26) | energy and throughput | energy, not dollars | none | archived or retired | n/a | researchers | A2 | none |
| OpenRouter rankings (S37) | usage by tokens | none | none | n/s | 2026-10-16 | developers | B2 | none |

### 4.3 Subscription-plan sites, measurements and trackers

| Site | Value framing | Cost basis | Quality link | Provenance | Cadence | Audience and model | Best grade | Overlap |
|---|---|---|---|---|---|---|---|---|
| SemiAnalysis (S50, S46) | plan value as API-equivalent monthly usage, 5× claim | PA at list API rates (controlled measurement) | none | method stated; partly paywalled | published 2026-10-05 | investors; paid newsletter | B2 | plan basis (ValueRank's selected numerator) |
| Wokey usage limits (S52) | weekly API-equivalent per plan | PA (account medians) | none | five-account gate; 15% review; weekly | every Monday | developers; gateway vendor | C2 | plan basis |
| RemakeBench Capacity Index (S53, S54, S107, S108, S109) | weekly API-equivalent allowance across vendors; share-of-week cost for one model | PA × 4 monthly | per-round evidence, "no aggregate score" | one account, one window; plan string "Pro"; Medium confidence | 2026-09-25 | benchmark lab | C3 to B2 | plan basis (closest); partial combination |
| ml0x (S51) | one seat's value | PA from logs | none | one user | 2026-08-28 | individual | C3 | none |
| aipricing.guru (S44) | subscription fee versus API-priced tokens | token math | disclaimed | stated disclaimers | 2026-10-17 | consumers; sponsored links | C2 | none |
| aimodelscompared (S55) | what 5× and 20× mean | vendor-published limits | none | URL and date logs; "Not published" | dated 2026-09-25 | consumers; affiliate possible | C2 | none |
| exploreaitogether (S56) | limits across vendors | vendor-published | none | dated 2026-10-14 | updated | consumers | C3 | none |
| fuelgauge, userightai (S59, S60) | limits guides | vendor-published plus estimates | none | dated; one stale | 2026-03-25; 2026-10-10 | consumers | C3 | none |
| aitoolsrank (S45) | API versus plan break-even | assumed session | none | contradictory dates | 2026-09-01 | affiliate | D4 | none |
| ai-usage-tracker (S57) | plan value multiple from local logs | PA estimate (lower bound) | none | open source | n/s | individuals | C2 | none |
| claude-usage-tracker (S58) | savings versus Pro, Max 5×, Max 20× | API-equivalent pace | none | open source | n/s | individuals | C3 | none |
| lpm, CUStats, Claude Monitor, SessionWatcher (S61 to S64) | limit-window meters | percent of window | none | no derivations | n/s | individuals | C3 | none |
| MemoryPlugin, ProductCompass (S65, S66) | plan guides | n/s (titles only) | n/s | unread | n/s | consumers | D4 | none |
| Not Diamond (S89) | routing vendor claims | n/s | n/s | directory only | 2026-07-08 | enterprise | D4 | none |
| Inventive HQ (S116) | Codex plan allowance from session logs and bar percentages ($650 per week for Pro $200 new tier) | PA, API-priced | none | single author; promotes own tool | 2026-10-04 | individual author | C3 | plan basis (weak) |
| Hacker News items (S117, S118, S119) | individual allowance estimates | PA, API-equivalent | none | self-reported | 2026-03-26 to 2026-07-18 | individuals | C3 to D4 | none |
| Reddit mirrors (S120, S121) | anecdotes and second-hand analysis | PA | none | third-party mirror; reddit.com blocked | 2026-01-28 to 2026-04-09 | individuals | D5 | none |
| AiZolo, Vortenza, Altai Tools, Tech Insider, BSWEN, AionX, MemoryPlugin, Fello AI (S92 to S97, S101, S103) | consumer plan guides, qualitative or relative multiples | vendor-published limits; list prices | none | mixed; several affiliate or product promotion | 2026-03 to 2026-10 | consumers | C3 to E5 | none |
| GitHub Copilot (S110, S111, S112, S113) | AI credits per plan, API-rate billing since 2026-06-01 | credits at API rates (vendor-defined) | none | vendor docs A1; CloudZero C3 | undated; June 2026 change | developers, organisations | A1 | none |
| Cursor (S114, S115) | multiples of an entry plan; third-party models billed separately | relative multiples | none | vendor pages A1 | undated | developers | A1 | none |
| Zhipu GLM Coding Plan (S124, S125), Alibaba Bailian (S126), Kimi (S127, S128), DeepSeek (S123), CodePick (S122, S123) | coding plans by price and quota | requests, prompts, yuan | none | vendor pages, relays, roundups | 2026-04 to 2026-09 | Chinese developers | A1 to D4 | none |
| Morph (S98, S99) | comparison pages | n/s | n/s | HTTP 429, unread | n/a | vendor promotion | F6 | none |

### 4.4 Owner terms of use

| Owner | Statement | Evidence | Grade |
|---|---|---|---|
| Artificial Analysis terms (S129) | personal, noncommercial licence; no commercial exploitation; no scraping or mining | 66405636, 26221e56, 5ec475e6 | A1 |
| Artificial Analysis free API (S130) | attribution required; subject to Terms of Use and Data Platform Terms (not retrieved) | 44865d85 | A1 |
| LiveBench README (S131) | datasets on Hugging Face; licence NOASSERTION; no data-licence statement found | source note only | B2 |

### 4.5 Baseline

| Site | Value framing | Cost basis | Plan | Provenance | Cadence | Audience | Grade | Overlap |
|---|---|---|---|---|---|---|---|---|
| ValueRank (S91) | 16 frontier models on 16 dimensions, two cost bases | TBC (AA) and PA-derived cost per Index point | yes, via Value Multiple | exact variant, dated, four evidence classes | per release from pinned snapshots (v1.9.6, 2026-10-08) | decision makers and analysts; owner-commissioned | A1, conflict of interest | n/a |
