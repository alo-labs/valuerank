# Decision record — AF-DECIDE rollup

**Workflow.** WF-SILVER-DEEP-RESEARCH · FS-SILVER_DEEP_RESEARCH · mode `deep` · research_type `default` · run 2026-10-17 (UTC) · 131 graded sources, 273 evidence rows, 116 claims (110 active) · validators pass, zero factual claims unsupported.

**Question.** Which other websites rank or compare AI models on value (quality against cost, including subscription-plan cost) as ValueRank does, and how do they differ?

## Decision

ValueRank's defensible positioning is narrow and should be stated narrowly: *the only site found in this search that joins a per-variant benchmark quality measure to a plan-derived cost in one ranked figure* (USD per Intelligence Index point on a subscription), with per-number evidence grades. It should not be described as "the only value ranking": at least thirteen aggregators rank models on API price-performance, two sites maintain dated plan-allowance measurements, and two partial combinations exist (RemakeBench pairs quality evidence with plan-priced cost but states "There is no aggregate score"; Klu lists one subscription-only model with plan prices in a footnote and computes no value).

## Alternatives considered

| Positioning | Why not |
|---|---|
| "The value ranking for AI models" | Overclaims against thirteen API price-performance sites (BenchLM, TokenCost, Model Price Watch, CostGoat, LM Market Cap, WhatLLM, Dervity, Klu, LLM Stats, Vellum, KickLLM, Analytical Insider, Artificial Analysis itself). |
| "The only site with plan-cost rankings" | Wokey and RemakeBench publish maintained plan-allowance measurements; consumer guides compare plan limits; RemakeBench is a partial combination. |
| Dropping the plan basis to avoid its fragility | The plan basis is the one feature without a substitute in the landscape; its fragility is manageable by publishing ranges, dates and evidence classes. |

## Evidence summary

- **API price-performance is crowded and formula-dependent.** Value leaders differ by site because formulas differ (score ÷ output list price; 3:1 or 0.75/0.25 blended price; measured cost per task). Five of twelve tabled aggregators take Artificial Analysis cost or index data, so agreement among them is not independent confirmation (F2, Table 2).
- **Cost per task is the measured family.** Artificial Analysis publishes intelligence against cost per task and total cost to run its index using provider-reported token counts and live cache rates; Aider, Terminal-Bench, Vals, HAL and LiveBench publish measured run cost; none includes subscription plans, and AA states its coding-agent cost excludes consumer plan pricing (F3).
- **Plan allowances are measured by a few, conflict, and move.** Like-for-like weekly Claude Max 20× figures: Wokey $1,751, a Hacker News rate-limit estimate $1,949, RemakeBench $2,155, SemiAnalysis about $2,710–2,930 (1.7× spread); OpenAI's $200 plan fell from about $2,200/week in July to roughly $500–650 in October as plan labels changed (F4, Tables 3 and 3b). Twelve consumer guides convert no allowance to dollars; Copilot and Cursor sell credits and multiples with no independent measurement; Chinese coding plans are compared on price and quota only (F8).
- **Provenance practice.** Dating appears at 9 of 12 aggregators, variant labels at 3, an imputation policy at 2; no site grades each number as measured, claimed, estimated or assumed (F5). The one non-US value view is SuperCLUE's token-cost quadrant, confirmed only via a national business daily (F7).
- **ValueRank's own formula has testable weaknesses** (F9): the Value Multiple depends on workload mix (cache-heavy measurement versus AA's token mix); selecting the highest eligible multiple biases plan cost downward; the numerator source is partly paywalled; no failure-rate adjustment (AA's total cost includes failed attempts but is not divided by successes).
- **Reuse terms are an open question** (F10): Artificial Analysis' terms (revised 2026-09-15) grant a personal, noncommercial licence, bar commercial exploitation and scraping, and require attribution for the free API; LiveBench states no data licence. The corpus does not establish how ValueRank obtains AA figures or whether its use is permitted.

## Tradeoffs and risks

- Narrow positioning is less marketable but survives scrutiny; the broad claim would be falsified by any reader who knows BenchLM or RemakeBench.
- Publishing allowance ranges with dates and classes makes the plan basis honest but visibly unstable; the alternative (point values) is unstable invisibly.
- The licensing question could constrain the API basis entirely if AA's terms apply as written; resolving it is a prerequisite to any commercial framing of the site.

## Confidence and remaining gaps

Confidence in the landscape map: high for the API price-performance and cost-per-task families (primary pages read), medium for plan measurements (C-grade measurers, conflicting figures), low for LMArena's price display and the SuperCLUE quadrant (relay-grade only). Not read: five long-tail aggregator pages, two Morph pages (HTTP 429), Google's own Gemini plan page, X, any European or Indian leaderboard, enterprise and open-weight self-hosting cost. No ValueRank values were recomputed; F9 is an inference about the formula.

## Downstream handoff

See `handoff.md`: positioning copy for the site and README; plan-basis presentation changes (ranges, dates, evidence classes, failure-rate caveat, AA-dependence note); a neighbour watch list (RemakeBench, Wokey, BenchLM, Klu, SuperCLUE); a licensing check with Artificial Analysis and LiveBench; and refresh targets for the next run.
