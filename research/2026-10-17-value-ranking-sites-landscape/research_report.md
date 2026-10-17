---
title: "Who else ranks AI models on value? A landscape of price-performance and plan-allowance sites, compared with ValueRank"
date: 2026-10-17
mode: deep
question: "Which other websites rank or compare AI models on value (quality against cost, including subscription-plan cost), as ValueRank does, and how do they differ from ValueRank in method, evidence, cost treatment and audience?"
---

# Who else ranks AI models on value? A landscape of price-performance and plan-allowance sites, compared with ValueRank

## Executive Summary

This report maps the public sites that rank or compare AI models on value, meaning quality against cost, and tests four assumptions about how they differ from ValueRank. It rests on 131 graded sources read on 2026-10-17, so every conclusion is bounded by one dated search.

API price-performance views are plentiful and thin. Artificial Analysis (AA) publishes the measured basis: intelligence against cost per task and total cost to run its index [15], [17], [36]. Thirteen aggregators rebuild "value" from list prices, blends or AA data with different formulas, such as score divided by output price alone [29]. Five of the twelve in Table 2 take AA cost or the AA index, so their agreement is not independent [18], [39], [42].

No site was found that combines the two halves, meaning a quality measure and a plan-derived cost for a named model joined in one ranked figure. This bounded negative depends on that definition. RemakeBench comes closest, with per-round quality evidence, a plan-allowance table and one model's benchmark cost as a share of a week, but its own page says "There is no aggregate score" [109], [108]. Klu shows one subscription-only model with plan prices in a footnote and no computed value [18]. Consumer guides, GitHub Copilot, Cursor and Chinese coding plans state limits, credits or multiples without joining them to quality [110], [115], [123]. Gemini plans, five lead-scan pages and SemiAnalysis's paywalled section were not read.

Plan evidence is mostly guides, posts and trackers, with two maintained measurements (Wokey, RemakeBench) and no maintained model ranking [52], [107]. Allowance measurements disagree less than a raw comparison suggests: four for Claude Max 20x span about $1,751 to $2,931 per week (1.7 times) [52], [118], [107], [46]; one seat's consumed workload is a different quantity [51].

The main decision risk is ValueRank's own plan formula. It divides AA's cost by a multiple measured under a different token mix and takes the highest eligible multiple, which may overstate value for output-heavy models. Separately, AA's terms give a personal, noncommercial licence and require attribution for its free API [129], [130]; whether ValueRank's use fits is a legal question this report cannot answer.

Dating is common (nine of twelve aggregators), exact-variant labelling is a minority practice, and no per-number evidence class was found [87]. It recommends dated ranges, a sensitivity test, an exact API-basis disclosure and confirming AA's terms.

## Introduction

Many pages claim to rank models "by value". Some divide a benchmark score by a token price; some report what one benchmark task cost to run; a few ask what a monthly subscription is worth when its allowance is priced at API rates. These are different quantities with different evidence. This report therefore classifies sites by cost basis first (list price, blended price, measured cost per task, total benchmark cost, or plan allowance) and by audience and evidence practice second.

**Baseline.** ValueRank ranks frontier models on measured benchmark dimensions plus a cost dimension with two bases. The API basis is AA's total cost to run its Intelligence Index. The Plan basis divides that cost by the model's highest eligible subscription Value Multiple and then by its AA Intelligence Index, giving US dollars per Index point [91]. Its documentation commits to exact-variant evidence (nothing transferred between versions, efforts or harnesses), dated sources and four evidence classes: measured, claim, estimate and assumption. The baseline source is graded A1 as a record of what ValueRank does, but it is owner-commissioned with a declared conflict of interest, so statements about ValueRank's uniqueness are bounded claims and not findings about the market.

**Assumptions tested.** The scope set four assumptions. A1: no other public site combines benchmark quality with subscription-plan cost at the model level. *Combine* is defined here as follows: for a named model variant, a site (a) reports a quality measure, (b) reports a cost derived from a subscription plan (an allowance priced at API rates, or a plan fee divided by it), and (c) joins the two in one figure or ranking across models. A site that shows (a) and (b) side by side without (c) is a partial combination and is reported as one. The A1 verdict depends on this definition. A2: several sites offer API price-performance views. A3: plan-allowance comparisons exist mostly as posts and trackers rather than maintained rankings. A4: dated, exact-variant, graded evidence is rare. The verdicts are in the Synthesis.

**Evidence and grading.** Retrieval used host web tools, because the optional search-cli was not installed, in two passes on the same day: four angles plus a lead scan (91 sources), then, after the first critique, the plan-comparison and coding-agent cost pages, GitHub Copilot and Cursor plan pages, forum measurements, Chinese vendor plans and the reuse terms of AA and LiveBench (40 sources). Sources carry a NATO-style grade: a letter for reliability and a digit for credibility. A core claim needs one A or B1/B2 source, or three C sources; a claim about a site's own method may rest on its own page and is then labelled primary-only. Search-summary evidence, pages that returned only a title, and paywalled material are flagged where they limit a conclusion. Bracketed citations are Bibliography numbers; `triangulation.md` records evidence identifiers, grades and the escalation outcome per core claim and carries the sites register. Statements drawn from ValueRank's internal project documents are marked "(internal context)" and are not evidence.

**Scale of the landscape.** 131 sources under 99 publisher labels were registered. They fall into five families: API price-performance aggregators, benchmark owners with cost columns, plan-allowance measurements, plan guides and meters, and research or commentary. Capability-only and non-dollar boards (Epoch, Scale, METR, Hugging Face) were checked to confirm they lack a dollar value view.

Eleven findings follow, then a comparative table, the four verdicts, a counterevidence register, the limits and recommendations for ValueRank.

## Main Analysis

### F1. The landscape map and taxonomy

The first result is structural: the sites that look alike on the surface differ in what they actually measure. Table 1 sorts them by cost basis.

| Family | Representative sites | Cost basis | Quality basis | Typical evidence |
|---|---|---|---|---|
| API price-performance aggregators | AA, BenchLM, TokenCost, Model Price Watch, CostGoat, LM Market Cap, WhatLLM, Dervity, Klu, LLM Stats | list or blended price per token; sometimes measured cost per task | composites of others' benchmarks | dated pages, stated or opaque formulas |
| Benchmark owners with cost columns | Aider, Terminal-Bench, Vals AI, HAL, LiveBench | measured cost per run or per task | own evaluations | per-entry cost, little method |
| Plan-allowance measurement | SemiAnalysis, Wokey, RemakeBench Capacity Index, single-user posts (ml0x, Inventive HQ, Hacker News) | plan allowance priced at API list rates | none (RemakeBench: per-round evidence, no aggregate score) | controlled, account-based or single-seat measurement |
| Plan guides, vendor plan pages and meters | twelve consumer guides, Copilot, Cursor, Chinese vendor plans, ai-usage-tracker, lpm | vendor limits, credits or multiples; local-log estimates | none | dated notes, vendor tables |
| Research and commentary | HAL papers, Cost-of-Pass, The Price of Progress, Epoch price trends, Arize, DoiT | cost per correct solution, price at fixed capability | benchmark scores | peer-reviewed or vendor studies |

_Table 1. Families of value-related sites, by cost basis._

Three observations follow. First, the "value" label is not a family boundary: BenchLM calls its ratio "Best Value Overall" and bases it on output price [29], while AA never labels anything "value" but plots intelligence against measured cost per task with a Pareto line [15]. Second, a large minority of aggregators repackage AA (Klu, WhatLLM, Dervity [18], [39], [42]; the count is in F2). Third, the plan family is structurally separate from the quality family: the sites that measure plan allowance carry no quality ranking, and the closest bridge is a table of API-equivalent allowances beside per-round benchmark evidence at RemakeBench [53], [54], [109].

The overlap categories in the comparative table are four. None: the site neither ranks on value nor supplies ValueRank. API basis: its cost view could substitute for ValueRank's API basis. Plan basis: it measures the quantity ValueRank uses as its plan numerator. Data supplier: ValueRank ingests or builds on its data, as with AA, whose cost and Index data underpin ValueRank's cost basis [1], and LiveBench, whose pinned release data includes a per-model cost file that ValueRank ingests under the field name cost per successful task [90]. What that file measures is not documented in the LiveBench text retrieved: the README links datasets and covers running evaluations, and no cost method was found [21], [131].

Several well-known boards sit outside the value set. OpenRouter ranks models by tokens processed, which is popularity and not value [37]. The Hugging Face Open LLM Leaderboard was archived in June 2024 [22] and reported ended in 2025 [24]; the AI Energy Score reports energy per task [25] and LLM-Perf latency, throughput, memory and energy [26]. Epoch's benchmark hub states that its top priority is tracking state-of-the-art performance, with no cost view in the fetched excerpt [4]; Scale's leaderboard shows scores with intervals and no cost terms [20], and a truncated SWE-bench fetch showed no cost view [10]. These negatives come from partial fetches and are absence in the text read, not proof.

Business models are mixed. CostGoat discloses affiliate revenue [34], aitoolsrank has affiliate links [45], PricePerToken shows a sponsor banner [35], Swfte promotes its own routing gateway [43], AI Model Comparison sells a Premium tier [41], LLM Stats offers a paid data API [7], and BenchLM sells API and MCP data access [106]. AiZolo and Fello AI sell products that compete with the plans they compare [92], [103]; Arize and DoiT argue for cost per task from positions as cost or observability vendors [27], [47]. Independence from the products being compared is the exception.

### F2. API price-performance aggregators and their formulas

The core of assumption A2 is confirmed: thirteen aggregators publish an API price-performance view, twelve with a formula in Table 2 and LM Market Cap with a Score/$ column whose formula was not read [40]. The more useful result is how the formulas differ, because the formulas decide which model leads.

| Site | Formula as stated | AA-derived | Notes |
|---|---|---|---|
| BenchLM | overall weighted score divided by output price per 1M tokens [29] | no | warns cheap models rank high |
| Model Price Watch | average score divided by blended price, (3 x input + output) / 4 [38] | no | input-heavy blend |
| TokenCost | quality (0.6 SWE-bench Verified, 0.4 Terminal-Bench 2.1) divided by blended price, 0.75 input and 0.25 output [31] | no | says the blend moves rankings |
| CostGoat | quality divided by output price, with a quality floor [34] | no | quality from a third party |
| AI Model Comparison | AA index divided by blended price, 75/25 [41] | index | formula inferred, not defined |
| Analytical Insider | AA index divided by 3:1 blended price, normalised [33] | index | stale; does not reproduce its table |
| KickLLM | 60% quality (MMLU, HumanEval), inverse blended cost, 10% breadth [32] | no | stale April 2026 snapshot |
| Swfte | "quality divided by cost" [43] | no | weights unpublished |
| Klu | "best value" is the lowest price in the table [18] | cost | price excluded from the index |
| LLM Stats | composite of intelligence, speed, price [7] | no | no published price formula |
| WhatLLM | measured cost per task including thinking tokens [39] | cost | redistributed data stays under AA terms [105] |
| Dervity | measured cost per task including thinking tokens [42] | cost | inherited from AA |

_Table 2. Stated value formulas for API-basis sites. Five of the twelve (AI Model Comparison, Analytical Insider, Klu, WhatLLM, Dervity) take AA cost or the AA index._

Four points stand out. First, **leaders can differ by formula**. BenchLM's top value entry is Qwen3.7 Flash, with a score of 46.9 at $0.13 per million output tokens, and BenchLM itself states that "a very cheap model with a modest overall score can rank high here" [29]. Klu's best value is Ling 3.1 Flash at $0.45, which is simply the lowest listed price and not a quality-per-cost ratio, while its top-index model is Claude Opus 5.5 [18]. These are two different low-cost leaders reached by two definitions of value. The corpus holds leader names for only two sites, so a broader table of disagreement was not built; the finding is that the definition decides, not that every pair disagrees.

Second, **the blend is an assumption that moves rankings**. TokenCost (graded B2) states that its 0.75/0.25 mix "is a modelling assumption, not a measurement, and it moves the value ranking", notes that 23 scored models were benchmarked only at a raised reasoning effort, excluded 48 models for lack of a verifiable price, and states that "Nothing here is estimated, interpolated or inferred" [31]. BenchLM's methodology page adds that vendor-run numbers are shown and labelled but kept out of the rank, and that missing benchmark values are never added [106]. Model Price Watch weights input three to one [38]; CostGoat ignores input price but adds a quality floor so that cheap, weak models do not top the list [34], which BenchLM's value list lacks [29]. BenchLM's mirror page defines no formula [30], and PricePerToken and llm-price are price trackers without a value formula [35], [48]. Two further pages join quality to API cost without a formula: Fast.io asserts a price-performance "sweet spot" in prose [102], and Tembo reproduces the official SWE-bench board with an average cost per task [100].

Third, **list-price blends omit the thinking-token cost that dominates agentic runs**. KickLLM concedes that "actual cost per task can be 2-8x higher due to thinking tokens" [32]. Output tokens cost three to ten times input tokens [75], and hidden reasoning tokens are billed [75]. Sites that use AA's measured cost per task (Dervity, WhatLLM, Klu's explorer) avoid this at the price of inheriting AA's definition [39], [42], [18].

Fourth, **dependence on AA is the main structural fact, though not universal**. Klu's price column is AA's measured pricing [18]; WhatLLM refreshes from AA [39] and says third-party data stays under AA terms [105]; Dervity's cost per task is AA's, at Index v4.3.2 [42]; AI Model Comparison and Analytical Insider divide the AA index by a blended price [41], [33]. Seven of the twelve are not documented as using AA data on the pages read (BenchLM, Model Price Watch, TokenCost, CostGoat, KickLLM, Swfte, LLM Stats). Where several AA-derived sites agree on a cost, the agreement may be one measurement seen several times. Staleness compounds this: the KickLLM table dates from April 2026 and cites MMLU and HumanEval [32], the Analytical Insider article from March 2026 [33], and a Permutable post still cites AA Index version 2 from February 2025 [49]. The Analytical Insider home page is a sales-lead service and not a value publisher [104], which lowers the weight of that article. The corpus does not record which provider's price each aggregator uses for open-weight models, so cross-site price differences for those models cannot be attributed.

The upstream has caveats of its own. AA's cost is a hybrid: provider-reported token counts with a canonical-tokenizer fallback, combined with live measurements of each model's typical cache-hit rate rather than the one-off value from the evaluation run [1]. For at least one component evaluation the published cost covers contestant calls and excludes judge calls, document preparation and OCR [1]. The index composition changes between versions: a methodology snippet lists v4.1 with nine evaluations [2], the live page v4.3.2 with ten [15]. AA's methodology calls itself "a more useful synthesis comparison between language models than any other metric in existence today" [2], a self-assessment and not an independent verdict. Scores and costs across index versions may not be comparable.

In short, the family answers "how much quality per token dollar" in at least thirteen ways. Measured spend appears only where AA's cost per task or total cost is shown, directly or through Dervity, WhatLLM and Klu; the rest is price arithmetic over benchmarks that are mostly borrowed.

### F3. Cost per task and benchmark-owner cost views

The second family is closer to ValueRank's own cost basis, because it uses measured spend and not price lists. AA's chart plots the Intelligence Index against the weighted average cost per Index task, where "each evaluation's cost is calculated from input, cache hit, cache write, reasoning, and answer token prices, divided by task count, and weighted by its Intelligence Index weight" [15]. The chart on the page shows 32 of 694 models with a Pareto line and a "most attractive quadrant" [15]. The companion total-cost view prices the whole index run (token prices times tokens used across the evaluations, excluding repeats) and covers 28 of 704 tracked models in its default chart [17], [36]. A third view, Score versus Total Cost, is the chart type that ValueRank's project rules use to define which models must be included (internal context, not evidence) [15].

AA also runs a Coding Agent Index, a simple average of DeepSWE v1.1, Terminal-Bench 4.0 and SWE-Atlas-QnA [16]. Its cost chart plots pay-per-token API cost per task for each variant, and AA states that it "is intended to show pay-per-token API cost, not consumer plan pricing or the full operational cost of deploying the system in production", while acknowledging that "many users will access coding agent harnesses through subscription plan offerings" [16]. This is the clearest primary-source statement of the boundary between the API-basis and plan-basis worlds. It shows AA's own scope only; whether other sites join plan cost to quality is tested in F4, F8 and F11.

Other benchmark owners publish cost beside quality, usually without method. Aider gives a "Total cost" per entry, for example 29.0829 for gpt-5 (high), with the effort in the label but no calculation [6]. Terminal-Bench shows COST and TOKENS columns and separates model from agent harness, again without a calculation note [9]. Vals AI states that each leaderboard compares accuracy, cost and latency [8]. The Princeton Holistic Agent Leaderboard (HAL) describes itself as "standardized, cost-aware, and third-party", tracks token cost per run, and uses a Pareto framing to warn that "agents can be 100x more expensive while only being 1% better" [67]. LiveBench's pinned release data from 2026-06-25 includes a `cost_2026_06_25.csv` alongside its score table [90]. This resolves an apparent contradiction about existence: the live LiveBench site and its README returned no cost view [5], [21], but the release data shows that a per-model cost file is published, so the earlier absence was a retrieval artefact of a JavaScript-rendered site. It does not resolve the definition. The release listing names the file; ValueRank ingests it under a field named for cost per successful task [90]; no LiveBench text retrieved says what the file measures [21], [131]. The file is therefore carried as a measured-cost file of unconfirmed definition. LMArena is a harder case. Secondary relays report that it now shows token pricing beside scores and plots performance against cost per task with a Pareto frontier in its Agents view [13], but those are search-summary relays of grade D4, the primary blog post was not retrievable [28], and the claim is carried only as reported; a D4 critical write-up also questions an unverifiable agent-arena claim [14], and a BenchLM comparison page was seen only in search results [12].

Dollar cost per benchmark task is not the same as cost per success. A cost-aware literature argues that the more decision-relevant unit divides total spend, including failed attempts, by the number of successes. Cost-of-Pass formalises "the expected monetary cost of generating a correct solution" [69]. Arize's study of 10 models on 40 tasks (2,400 runs) reports that cost per successful task "can diverge from token price by more than an order of magnitude" and "inverts the ranking the pricing pages give you"; its cheapest cost per success also had the weakest pass rate, and it recommends reporting coverage beside cost [27]. AA's figures are built from token use across every task attempt, and nothing in their definitions, as quoted, conditions on correctness [15], [17]. They therefore include the spend on failed attempts and are not divided by the number of successes. That is the sense in which AA's measured spend and a cost-per-success unit are different quantities, and it is a gap in the denominator, not a failure to count the spend. If the LiveBench file is indeed a per-success figure, as ValueRank's field name implies [90], the two cost bases would also differ in unit; that cannot be confirmed from the text retrieved.

Reasoning tokens drive much of the divergence. AA runs reasoning models with their maximum output budget [1]. A relay of an AA study reports that o1 generated over 44 million tokens across seven benchmarks against about 5.5 million for GPT-4o and cost $2,767 to benchmark [79], and an AA model page notes a model that produced 350M tokens on the Index against a median of 67M [3]. These are search-summary evidence (B3, confidence 0.65 and 0.4) used only for direction: a low per-token price can still mean a high run cost. Epoch and the Stanford AI Index show the macro version, with the price of a fixed capability falling 9x to 900x a year [70] and GPT-3.5-level inference cost falling more than 280-fold between November 2022 and October 2024 [84].

### F4. Subscription-plan comparison and allowance measurement

This is where ValueRank's Plan basis lives, and where the evidence is least settled. Plan-allowance evidence comes in five classes, and the class determines how far a number can be trusted.

**Class 1, controlled and account-based measurement.** SemiAnalysis describes isolating each token type (input, cache write, cache read, output) with targeted prompts, recording meter movement per request until error is within about 5%, then pricing the tokens at API rates [50]. It argues that a month is capped by the weekly limits [50] and that reading from the cache costs almost nothing on some plans and may not move the meter at all [50]. Its stored evidence is a tool summary of a partly paywalled page, so the method is known at confidence 0.7. Wokey remeasures every Monday from real subscription accounts behind its gateway, publishes a plan only after at least five accounts and manually checks changes above 15% [52]. RemakeBench publishes a Capacity Index, a cross-vendor weekly allowance table dated 2026-09-25, with monthly values as the weekly figure times four [53], [107]. Its Claude Max 20x method page is more modest than the table suggests: it divides one account's logged API-equivalent spend by the app-reported percentage of the weekly quota, for a single week, and notes that the account's plan string reads "Pro" and not "Max 20×", with Medium confidence [108].

**Class 2, single-seat and single-author measurement.** One analysis parsed 14,973 local Claude Code session files from a single Max 20x seat (33.28 billion input tokens, 122 million output tokens, 96.4% cache hit, 2026-07-29 to 2026-08-28) and priced them at Opus 5 list rates to about $26,187 per month against the $200 fee [51]. An author who sells a usage-tracking tool measured Codex allowances from session logs and bar percentages [116], and Hacker News posters report their own tests (Tables 3 and 3b) [117], [118]; one further comment recalls $10 to $20 of daily value on Pro without measuring it [119]. The Reddit threads found are third-party mirrors, because reddit.com blocked retrieval, and are graded D5 [120], [121].

**Class 3, trackers.** ai-usage-tracker computes a plan value multiple as 30-day API-equivalent use divided by the plan price and states it is a lower bound because chat use is not logged [57]; claude-usage-tracker projects a 14-day pace against plan prices [58]; lpm, CUStats, Claude Monitor and SessionWatcher show percent-of-window with no allowance derivation [61], [62], [63], [64].

**Class 4, vendor-stated limits.** Guides restate provider limits and add their own arithmetic where limits are unpublished [55], [56], [59], [60]; aimodelscompared logs the URL and date of each check and writes "Not published" instead of estimating [55]. F8 covers vendors that publish credits or multiples. **Class 5, qualitative comparison pages.** Eight further consumer pages compare tiers in words, star ratings or relative multiples and convert nothing to dollars [92], [93], [94], [95], [96], [97], [101], [103].

The measurements disagree where they overlap, but less than a raw comparison suggests once like is compared with like. Table 3 lists the four Claude Max 20x measurements that estimate the plan's allowance, meaning the API-list value of what the weekly limit permits. Each uses a different method, date and priced model, so none replicates another.

| Source (store grade) | Reported figure | Window | Method and priced model | Weekly equivalent | Implied monthly multiple |
|---|---|---|---|---|---|
| Wokey [52] (C2) | about $1,751 per week | 2026-10-05 to 10-12 | median of account medians, at least five accounts; official API rates | $1,751 | 35.0x |
| Hacker News proxy post [118] (C3) | about $1,949 per week | posted 2026-03-26 | header-capturing proxy, 11 sessions; quota described as price-weighted; author's own tool | $1,949 | 39.0x |
| RemakeBench [107], [108] (B2) | about $2,155 per week | 2026-09-24 to 10-01 | one account, Opus 5.5 in Claude Code; logged spend divided by app-reported 58% of weekly quota; plan string reads "Pro" | $2,155 | 43.1x |
| SemiAnalysis via explainx [46] (C3; primary [50] B2, partly paywalled) | about $11,726 per month of Opus 5.5, 58.6x the fee | published 2026-10-05 | controlled token-type meter measurement | about $2,710 to $2,930 | 58.6x |

_Table 3. Claude Max 20x allowance: four allowance measurements. Weekly equivalents and implied multiples are the analyst's arithmetic (monthly divided by 4 or 4.33; weekly times 4, divided by the $200 fee). The RemakeBench range of $2,136 to $2,174 reflects rounding of the displayed 58% (1,249.83 divided by 57.5% to 58.5%) and is not a spread across repeated measurements._

The allowance measurements span about $1,751 to $2,931 per week, 1.7 times (1.5 times if SemiAnalysis's month is divided by 4.33), or about 35x to 59x the fee as a monthly multiple. Wokey and RemakeBench differ by about 23%. The corpus explains none of the differences; candidate causes are the date (the proxy post is six months older, and limits move without notice [51]), the model priced, cache treatment and workload shape. The sources agree that cache reads barely count against plan meters [52], [51], and SemiAnalysis says so for some plans [50]. RemakeBench's single account and "Pro" plan string reduce its weight, and the proxy post is a small self-built sample.

The ml0x figure is a different quantity: what one seat consumed over a calendar month at Opus 5 list rates, $26,187, or about $6,050 to $6,550 per week and 131 times the fee [51]. That is 2.2 times SemiAnalysis's figure for the full monthly limit, which a consumption total should not exceed if both were priced alike. The window predates the 13 September expiry of a temporary 50% weekly increase [55], which could explain at most a factor of 1.5, and the priced model and cache accounting are not documented well enough to resolve the rest. It is an upper-envelope consumption datapoint for a heavy cache-dominated user and is not used to bound the allowance. A Reddit post claiming "$1k+" of value on a $200 plan gives no window (D5) [120].

The OpenAI $200 plan shows a spread that resolves, in direction, once date and plan label are lined up (Table 3b).

| Source (store grade) | Reported figure | Date | Plan label | Weekly equivalent |
|---|---|---|---|---|
| Hacker News comment [117] (D4) | about $2,200 per week on GPT 5.6 Sol, method not given | 2026-07-18 | "Pro 20x $200" | $2,200 |
| RemakeBench [107] (B2) | about $1,532 per week | 2026-09-25 | "OpenAI Pro 20x" | $1,532 |
| Inventive HQ [116] (C3) | about $650 per week ($6.41 and $6.70 per 1%); a grandfathered $200 plan about $1,300 until 29 October | 2026-10-04 | Pro $200 "(new 10x tier)" | $650 |
| SemiAnalysis via explainx [46] (C3) | about $2,084 per month of GPT-6.1 Sol (10.4x the fee) | 2026-10-05 | ChatGPT Pro 200 | about $480 to $520 |

_Table 3b. OpenAI $200 plan allowance, by date. Weekly equivalents are the analyst's arithmetic._

Ordered by date the figures fall from $2,200 to roughly $500 to $650 as the label changes from "20x" to "10x". The SemiAnalysis summary says OpenAI halved the $200 plan's value and added a $500 tier [50], which is consistent with this pattern; it is not shown that the four labels name the same product, so the earlier three-fold gap is explained in direction, not resolved. The same summary says Anthropic offers about 4x OpenAI's API-equivalent value for Opus 5.5 against GPT-6.1 Sol [50], while the two quoted monthly figures imply about 5.6x [46]. The primary is partly paywalled, and no headline multiple should be quoted without it.

Three regularities limit any plan-based ranking. First, **allowances are model-specific**: Fable usage counts against only half of a $200 plan's limit [46], [50]. Second, **the advertised multiplier applies to the five-hour window**: Anthropic's ratios are stated per five-hour session [56], and Wokey finds the weekly ratio between Max 20x and Pro is about ten, not twenty [52]. Third, **limits are opaque and move without notice**. Anthropic publishes no absolute message counts at any tier while OpenAI publishes ranges for Codex [55]; Grok plans were replaced on 2026-10-12 [56]; one account received an A/B-tested limit about 20% lower [50]; and with unpublished weekly caps "the multiple can change without a price change" [51]. SemiAnalysis frames its work as an input for modelling AI lab financials and not as a buyer's guide [50].

Coverage of quality alongside plan cost is where the family stops. aipricing.guru compares the fee of 24 paid plans with API-priced estimated tokens but states "this is a metered API cost check, not a claim that the model, quality, native tools, or usage limits are equivalent" [44]. aitoolsrank uses an assumed two-thousand-token session and carries contradictory dates [45]. SemiAnalysis does not measure token efficiency or quality [46]. RemakeBench, the nearest neighbour, is examined in F11.

### F5. Provenance and evidence practices

Assumption A4 asks whether dated, exact-variant, graded evidence is rare. The evidence splits it into practices, and the answer differs for each. Counts in Table 4 are the analyst's tally over the twelve sites of Table 2 and the register in `triangulation.md`.

| Practice | Where found | Where absent or weak |
|---|---|---|
| Calendar date on the page | nine of the twelve aggregators, among them BenchLM (2026-10-17) [29], Model Price Watch [38], Klu (2026-10-13) [18] and WhatLLM's methodology page (reviewed 2026-09-06) [105]; also RemakeBench (2026-09-25) [53] and aimodelscompared logs [55] | TokenCost, AI Model Comparison and LLM Stats show no calendar date [31], [41], [7]; two of the nine (KickLLM, Analytical Insider) carry months-old publication dates and not refresh stamps [32], [33]; Vellum shows no year [19] |
| Exact variant and reasoning effort in the label | three of the twelve (Klu, Dervity, TokenCost) [18], [42], [31]; AA ("Adaptive Reasoning, Max Effort") [3], Aider ("gpt-5 (high)") [6], SuperCLUE "(max)" [81], OckBench settings [88] | LLM Stats, Swfte and most composites do not state variant handling [7], [43] |
| Formula disclosed | six of the twelve: BenchLM, TokenCost, Model Price Watch, CostGoat, KickLLM, Analytical Insider [29], [31], [38], [34], [32], [33] (the last does not reproduce its table) | Swfte, LLM Stats, AI Model Comparison [43], [7], [41] |
| Imputation or missing-value policy | TokenCost: no estimation or interpolation [31]; BenchLM: missing tests stay blank and vendor-run numbers stay out of the rank [106]; aimodelscompared: "Not published" [55] | most sites state none |
| Uncertainty or integrity markers | Terminal-Bench confidence intervals and canary string [9]; Scale score intervals [20]; BenchLM marks estimated against supported positions [106] | the other eleven aggregators in Table 2 show none in the pages read |
| Cadence and gates | Wokey weekly with five-account gate [52] | AA states no refresh schedule [1]; Epoch states none [4] |
| Evidence class per number | not found in three searches and one topic listing [87]; BenchLM is a partial analogue at row level [106] | all other sites reviewed |

_Table 4. Provenance practices across the landscape._

Dating is therefore common among aggregators, exact-variant labelling is a minority practice (three of twelve aggregators, though standard at AA and the benchmark owners), and imputation policies and uncertainty markers are rarer still. What was not found is a per-number evidence class. The negative finding comes from three searches for terms such as "evidence grade" and "exact model variant" and a GitHub topic listing, and is held at moderate confidence (0.55) [87]. The marker practices in the table are provenance signals of a kind, so the unmatched part of ValueRank's practice is narrower than "provenance": it is labelling each number as measured, claim, estimate or assumption. BenchLM comes nearest. In the analyst's reading it separates vendor-run numbers (claims) from independent rows and marks estimated against supported positions [106], which resembles two of the four classes at row level but is not a per-number label and has no assumption class. Other analogues in spirit are TokenCost's no-imputation policy [31], aimodelscompared's date-stamped checks with an explicit "Not published" [55], and OckBench's pinning of reasoning settings, known here only through a search summary [88].

Provenance failures also appear. Analytical Insider's value score cannot be reproduced from its stated formula: its inputs for DeepSeek V3 (86 and $0.19) do not give its listed 88 [33]. KickLLM measures quality with MMLU and HumanEval, aged six months [32]. Vellum's scores are "largely provider-reported" with some independent runs [19], and the Klu Index blends accuracy, evaluations, preference and speed with published weights (35, 30, 20, 15 percent) but unpublished inputs [18]. Vendor-reported results are the weakest tier of evidence in the ValueRank taxonomy, and several aggregators do not distinguish them from independent measurements.

### F6. Research and critique of price-performance ranking

A body of work predates the aggregator wave and supplies its justification and its limits. "AI Agents That Matter" argues that accuracy-only leaderboards reward needlessly complex and costly agents and motivates "jointly optimizing" cost and accuracy [68]. Cost-of-Pass introduces cost per correct solution and shows that lightweight models are most cost-effective on basic quantitative tasks while marginal performance gains rarely justify costs [69]. "The Price of Progress" argues that benchmark scores alone give "a warped picture of progress in practical capabilities per dollar" and urges that the price of benchmarking be publicised and taken into account [71]. A Chinese-data economics paper proposes an "optimal cost-effectiveness zone" using WiNEval-3.0 and reports diminishing marginal cost and diminishing returns to scale [72]. Epoch measures the price to reach a fixed capability and records declines of 9x to 900x per year with the caveat that the fastest drops are recent and may not persist [70]. The 2025 Stanford AI Index reports a more than 280-fold fall in inference cost at a fixed capability level over two years, a trend statement and not a model-by-model value ranking [84]. The Index's technical performance chapter also notes lower cost for agents on select tasks, qualitatively only [85].

The critique bears on ValueRank in three ways. First, price-performance is easily gamed by cheap, weak models unless the ranking floors quality or reports coverage; Arize's advice to "report coverage next to cost, always" [27] and CostGoat's quality floor [34] are two responses. Second, cost per task is not cost per success; a measured-spend ranking that is not divided by the number of successes leaves the cost of failure out of the unit [27], [69]. Third, the unit of time matters: the same capability gets cheaper quickly [70], so a ranking dated 2026-10-17 may be stale within months, as the Epoch price-trend work suggests [70], which is why the best aggregators timestamp aggressively.

Three research items were negative on cost framing in the text retrieved: the SWE Atlas abstract [73], the ChipBench abstract [74] and METR's time-horizon post [86].

### F7. Non-US views

Non-US coverage is thin: China is covered by one secondary press report on a leaderboard and by vendor plan pages (F8), and no European or Indian leaderboard was read. Jingji Cankao Bao, a Chinese financial newspaper read through Eastmoney, reports that on 30 June SuperCLUE "for the first time" released a Token cost quadrant, with task average score on one axis and average price per question on the other. It tested seven domestic models on one engineering problem needing dozens of dialogue turns, and found that average price per question differed by nearly 20 times and that task average scores differed by up to more than 70% [81]. Zhipu's GLM5.2 (max) is highest on both score and price, in the "premium quality" quadrant, and Xiaomi's MiMo-V2.5-pro lowest in price with a decent score, in the "economical" quadrant [81]. The report also states that several Chinese evaluation reports recently added cost evaluation for the first time [81]; a second report relays the event through a search summary [78]. The quadrant is a measured-spend, single-task view with an effort tag in the model name, similar in spirit to AA's cost per task, though on one task and seven models.

The primary SuperCLUE page is client-rendered and only its title could be retrieved, so the quadrant is graded secondary-only [76]. The automatic claim-support check could not match this Chinese-language source to the English claim (score 0.15, flagged for review); the quoted paragraph was compared with the claim by hand for this report and the translation holds, including both spreads. SuperCLUE's May 2026 general report (21 models, six tasks, 492 questions) has no cost dimension in the retrieved text [78], so the quadrant is a separate release and not a standing leaderboard. OpenCompass's CompassRank page is JavaScript-rendered [77], [82]; its README describes an evaluation platform with over 100 datasets and no price-normalised ranking [83]. HELM's page returned only a title [80]. For OpenCompass and HELM the correct statement is that cost treatment is unconfirmed, not absent. A commentary in the same report notes there is no standard for converting token consumption into business output [81]. An India-focused leaderboard named in the lead scan was not read.

### F8. Plan families beyond the Claude and Codex measurements

The second pass read the other plan families that the scope names. The result for assumption A1 is the same: vendors state allowances in incompatible units, independent measurement exists for few, and no page joins any to a quality measure.

**GitHub Copilot** is the one family where the vendor publishes a dollar-denominated allowance. The official plans page lists Pro at $10 with 1,500 AI credits, Pro+ at $39 with 7,000 and Max at $100 with 20,000; organisation seats carry credits worth their price, and usage beyond the pool costs $0.01 per credit [110]. An independent explainer confirms that on 1 June 2026 every Copilot plan moved to usage-based billing, with credits billed by token consumption at each model's listed API rate [112]. If a credit is worth the one-cent overage rate, the individual pools are worth $15, $70 and $200 against fees of $10, $39 and $100, so the vendor's own multiples are about 1.5x to 2x (the analyst's arithmetic; the page does not state the dollar value of the individual pools). Completions sit outside the pool and stay unlimited [110]. The earlier scheme of 300 or 1,500 premium requests, metered per prompt times a model multiplier, is marked legacy [111]. No independent measurement of a Copilot allowance was found, and none is needed in the way Anthropic's is, because the credit is defined at API rates.

**Cursor** is now sold inside "The X Subscription", with plans expressed as multiples of the entry plan (Plus at $8, Premium 4x, Super 15x, Ultra 50x) and a weekly pool shared with Grok; the former Pro, Pro+, Ultra, Start and Teams plans are legacy [115], [114]. Usage of third-party models, which includes the frontier models ValueRank ranks, is not in the monthly price and is bought separately at API list price [114], [115], so a plan-priced allowance for Claude or GPT inside Cursor is not defined by the plan fee. CloudZero notes both tools are now usage-billed, so sticker prices understate the comparison [112]; PricePerToken compares them on pricing-model rows only [113]. Two Morph comparison pages returned HTTP 429 and were not read [98], [99].

**Chinese vendor plans.** Zhipu's official page gives only a starting price of 18 USD per month and no quota table [124]; a news reprint reports that its legacy plan without weekly limits stopped auto-renewing on 30 April 2026 [125]; a third-party roundup, flagged by its publisher as possibly outdated, lists 49, 149 and 469 yuan tiers and about 80 prompts per five-hour window for Lite, unchecked against an official table [123]. Alibaba's Bailian Coding Plan is described in an article hosted on its developer community as Pro only, at 200 yuan per month for 90,000 requests [126]. Kimi's tiers are relayed by a crypto-news flash at 468 to 6,708 yuan a year, with Kimi Code needing the 948-yuan tier [127], and the official page shows no quotas in its rendered text [128]. DeepSeek has no coding plan in the roundup and bills per token [123]. CodePick compares these plans by price, quota mechanism and scenario, with no quality score [122], [123]. The units are requests and prompts, not API-priced dollars.

**Consumer chat plans.** Twelve consumer guides were read: four in the first pass [55], [56], [59], [60] and eight in the second (AiZolo, Vortenza, Altai Tools, Tech Insider, BSWEN, AionX, MemoryPlugin, Fello AI) [92], [93], [94], [95], [96], [97], [101], [103]. They restate list prices and vendor limits, give qualitative verdicts or star ratings, and keep allowances as relative multiples and windows [92], [94], [96], [97]. Vortenza joins $20 plans to benchmark names only through adjectives and names superseded models, and Tech Insider relays benchmark figures from other blogs [93], [95]. None converts an allowance into API-priced dollars or joins one to a measured quality score.

**Community measurements.** The forum sweep found three Hacker News items and two Reddit mirrors: individual allowance estimates (Tables 3 and 3b), a recollection [117], [118], [119], and an unchecked second-hand claim that the Max 20x weekly limit is only twice the Max 5x limit (D5) [121]. They show that much plan evidence lives in posts, but they are single-user claims, not maintained rankings.

"Allowance" is therefore not one unit. Claude and Codex give windows and multiples, Copilot gives credits at API rates, Cursor gives multiples and sells frontier models separately, and Chinese plans give requests or prompts. Only Copilot's unit is API-equivalent by the vendor's own definition, so a cross-vendor ranking needs a conversion per unit, each with a different evidence class.

### F9. ValueRank's plan formula tested on the same grounds

The report has faulted other sites for formula assumptions that move rankings (F2), list-price blends that miss reasoning tokens (F3) and allowance figures that depend on date and workload (F4). The same tests apply to ValueRank's Plan basis, which divides AA's total cost to run the Index by the model's highest eligible Value Multiple and then by its AA Intelligence Index [91]. What follows is the analyst's inference from the cited evidence; the report holds none of ValueRank's plan-cost values and recomputed nothing.

**1. The multiple is workload-dependent, and the numerator and divisor use different workloads.** The numerator is AA's measured spend, built from provider-reported token counts and live, model-specific cache-hit rates, with reasoning models run at their maximum output budget [1], [15]. The divisor is a ratio of API-priced allowance to fee, and the sources describe that ratio as shaped by workload: cache reads cost almost nothing on some plans and may not move the meter [50], most tokens in a long agentic session are cache reads [52], and one heavy seat ran at a 96.4% cache-hit rate [51]. A multiple therefore depends on the mix of cached input, fresh input and output used to calibrate it. If a model's Index run is more output-heavy or less cache-heavy than that mix, the same allowance covers fewer list-price dollars than the multiple assumes, and AA cost divided by the multiple understates the model's plan cost, so its value looks better than it is. The direction follows from the meter behaviour reported for Anthropic; the corpus does not establish that behaviour for OpenAI or other plans, and the size of the effect was not estimated. The formula treats the multiple as workload-independent, which the sources' own descriptions of it (model-specific, cache-dominated) do not support.

**2. The highest eligible multiple is a selection.** The retrieved text says "highest eligible" [91]; the eligibility rule is not in it. Where several plans, tiers or sources qualify, the maximum of several noisy estimates is biased upward, and the evidence shows noisy estimates: allowance measurements of one plan span 1.7 times (Table 3), the weekly ratio of Max 20x to Pro is about ten and not twenty [52], and OpenAI's figures move with plan generation (Table 3b). The effect is a systematic tilt toward higher stated value for the plan basis. How large it is depends on how many candidate multiples each model has, which this report cannot see.

**3. The numerator is partly paywalled and known mostly through a summary.** Project instructions designate the SemiAnalysis analysis for Anthropic and Codex (internal context, not evidence). Its method is described in the public portion [50], but the third-party plan section is paywalled, the headline multiples were read through a secondary summary graded C3 [46], and the stored method evidence is a tool summary at confidence 0.7. The summary and the headline figures also disagree on the Anthropic-to-OpenAI ratio (about 4x against 5.6x), so the numerator is credible in method and not independently reproducible from the pages read.

**4. The allowance is model-specific.** SemiAnalysis's headline multiples are for Opus 5.5 and GPT-6.1 Sol, and Fable usage counts against only half of a $200 plan's limit [46], [50]. ValueRank's exact-variant policy refuses to transfer evidence across versions or efforts [91]. A multiple measured on one model and applied to another model of the same provider is a transfer of that kind; whether ValueRank applies per-model multiples is not visible in the text read.

**What follows.** Plan cost is inversely proportional to the multiple, so a multiple that moves by 1.7 times moves every plan cost computed from it by the same factor. Within one provider using one multiple the order is unchanged; comparisons across providers, and between the plan basis and the API basis, are not. A sensitivity test is cheap: recompute the plan basis at the lowest and highest allowance in Table 3 and count the rank changes (Recommendation 2). Models whose AA cost is dominated by output or reasoning tokens deserve a flag.

**What the test does not show.** None of this shows that ValueRank's published figures are wrong. It shows that the plan basis rests on assumptions the report's own evidence calls unstable, as it said of others, and that the commissioner's strongest claim should carry that qualifier. This is the main decision risk in the report.

### F10. Reuse terms of the upstream data

ValueRank's cost and Index inputs come from AA [91], and a pinned-snapshot site depends on being allowed to republish derived figures. The second retrieval pass read the owners' public reuse terms.

AA's Website Terms of Use, last revised 2026-09-15, grant a "non-transferable, non-exclusive, revocable, limited" licence to use the site "solely for your own personal, noncommercial use" (section 2.1). They prohibit licensing, selling, distributing, hosting or otherwise commercially exploiting the site or any content displayed on it (2.2(a)), copying or republishing without express permission (2.2(d)), and using automated agents or scripts to scrape or mine the site (3(b)(vi)), with a conditional exception for public search-engine spiders [129]. AA's free API page states that attribution is required for all use of the free API and that benchmark, speed and pricing data are subject to the Terms of Use and to Data Platform Terms, which were not retrieved [130]. WhatLLM, a site that redistributes AA data, publishes its own editorial content under CC BY 4.0 and states that third-party benchmark, price and availability data "remains subject to Artificial Analysis and provider terms" [105], so at least one redistributor treats AA's terms as governing downstream use. LiveBench is different: its README links datasets on Hugging Face, GitHub reports the repository licence as unasserted, and no data-licence statement was found [131]. The absence of a stated licence is not a grant.

The evidence does not say how ValueRank obtains AA's figures (the free API, manual transcription or another route), whether it holds written permission, what the Data Platform Terms permit for commercial or derived use, or whether ValueRank's publication counts as commercial. Whether a pinned-snapshot ranking built on AA's data is permitted depends on those facts. That is a legal question; this report does not answer it and is not legal advice. The factual finding is narrower: the default licence on AA's site content is personal and noncommercial, attribution is required for API use, and ValueRank's dependence on a single upstream is a licence dependence as well as an accuracy dependence, shared by the aggregators that inherit AA data.

### F11. Where ValueRank overlaps, where it is alone, and what it could borrow

**Overlap with the API basis.** ValueRank's API basis, AA's total cost to run the Intelligence Index, comes from the same upstream as the cost views that AA, Klu, WhatLLM and Dervity display [15], [17], [18], [39], [42]. ValueRank is a consumer of AA data, like those aggregators, and shares their upstream risk: AA's costs are partly modelled [1], its index definition changes across versions [2], [15], it states no refresh schedule [1], and its reuse terms are restrictive (F10). ValueRank differs by pinning dated snapshots, restricting itself to exact variants, and combining AA's cost with benchmark data from LiveBench and others [90], [91].

**Overlap with the plan basis.** The plan multiple is an allowance that SemiAnalysis, Wokey and RemakeBench measure and stop at [50], [52], [53]. No site read divides a measured cost by such a multiple and by a quality index [91].

**Partial combinations.** Table 5 applies the definition of combine from the Introduction to the nearest sites.

| Site | (a) quality measure | (b) plan-derived cost | (c) joined ranked figure | Reading |
|---|---|---|---|---|
| RemakeBench [54], [108], [109] | per-round evidence for four models; "There is no aggregate score" | weekly allowance table; one model's 18 tasks costed at $1,267, 58.8% of a week; task costs API-equivalent, subscription charge recorded as zero | no | partial; not a ranking |
| Klu [18] | Klu Index 97 for a subscription-only model | plan prices of $50 and $200 in a footnote; price column shows "Subscription" | no value metric | partial; quality beside plan price only |
| aipricing.guru [44] | none | fee against API-priced tokens, 24 plans | no | cost side only |
| SemiAnalysis [50], Wokey [52] | none | measured allowance | no | cost side only |
| ValueRank [91] | 16 dimensions, exact variants | plan multiple applied to AA cost | USD per Index point | satisfies (a), (b), (c) |

_Table 5. Partial combinations against the definition of combine._

The two partial cases show where the definition bites. If quality evidence displayed beside plan-denominated cost counted as combining, RemakeBench would count and A1 would fail for it. The report does not count it, because the site states that it publishes no aggregate and records subscription charges as zero in its rounds [109], and its share-of-week figure covers only the model tested [108]. That is a judgement about a definition. A hostile reader could say that RemakeBench puts plan-priced cost beside measured quality and ValueRank adds a division; the answer is that the cross-model division by a quality index is the step the site does not take.

**Where ValueRank appears alone in this search.** Three features were not found together elsewhere: the model-level combination of benchmark quality and plan cost per quality point [91]; exact-variant pinning with no transfer across versions or efforts; and a visible evidence grade separating measurement, claim, estimate and assumption, for which BenchLM is only a partial analogue [106]. TokenCost has the best explicit no-imputation policy [31], Wokey and aimodelscompared the best dated plan notes [52], [55], and AA the best variant naming [3]. No page was found with all three plus a plan basis. The statement is about this search and carries the baseline's conflict of interest.

**Where ValueRank is weaker than the alternatives.** AA tracks 694 to 704 models with live pages [15], [17], where ValueRank ranks 16 frontier models from pinned snapshots updated per release [91]. Wokey remeasures plan allowances weekly [52], where ValueRank's plan basis rests on one analyst's measurement that is partly paywalled and was read here through a summary [46], [50]. ValueRank depends on one commercial upstream whose reuse terms are unconfirmed (F10), and its documentation is owner-written [91]. These are trade-offs, not flaws in its method, but they belong in any comparison with the commissioner on one side.

**What ValueRank could borrow** is listed in Recommendation 6, together with RemakeBench's cross-vendor table as a cross-check [53] and Arize's practice of reporting coverage beside cost [27].

## Synthesis

### Comparative landscape table

Table 6 condenses the sites register in `triangulation.md`. The grade is the best store grade of any source about the site.

| Site | Value framing and cost basis | Plan coverage | Grade | Overlap |
|---|---|---|---|---|
| Artificial Analysis [15], [16] | intelligence versus measured cost per task and total cost, Pareto | excluded | B2 | API basis; data supplier |
| BenchLM [29], [106] | score divided by output list price | none | B2 (methodology) | API basis |
| TokenCost [31] | quality divided by blended price (0.75/0.25) | none | B2 | API basis |
| Model Price Watch [38] | score divided by blended price (3:1) | none | C2 | API basis |
| CostGoat [34] | quality divided by output price, floor | none | C2 | API basis |
| LM Market Cap [40] | Score/$ column, list price | none | C3 | API basis |
| WhatLLM [39], [105] | best task cost, measured, from AA | none | B2 (methodology) | API basis |
| Dervity [42] | best task cost, measured, from AA | none | C3 | API basis |
| Klu [18] | index versus blended and per-effort cost, from AA | footnote; partial combination | C3 | API basis |
| LLM Stats [7] | composite including list price | none | C3 | API basis |
| Vellum [19] | separate list-price table | none | C3 | weak API basis |
| KickLLM [32] | blended-price value index | none | D3 | unreliable |
| Analytical Insider [33], [104] | blended-price value score | none | D3 | unreliable |
| Aider [6] | accuracy with total cost per run | none | B2 | none |
| Terminal-Bench [9] | resolution rate with cost and tokens | none | B3 | none |
| Vals AI [8] | accuracy, cost, latency | none | B3 | none |
| HAL [67] | cost-aware agent leaderboard | none | B2 | none |
| LiveBench [90], [131] | scores with a cost file of unconfirmed definition | none | A2 (file exists) | data supplier |
| SuperCLUE [81] | token cost quadrant, price per question, one task | none | B2 (secondary) | none |
| LMArena [13] | preference; reported price display | none | D4 | none (unconfirmed) |
| Epoch [4]; Scale [20]; METR [86]; Hugging Face [22], [25] | capability or energy; no dollar view found | none | B2; B3; A1; A2 | none |
| SemiAnalysis [50] | plan allowance at API list rates | yes | B2 | plan basis (numerator) |
| Wokey [52] | weekly plan allowance | yes | C2 | plan basis |
| RemakeBench [107], [109] | Capacity Index beside per-round evidence; "no aggregate score" | yes | B2 (single-window pages) | plan basis (closest); partial combination |
| aipricing.guru [44] | fee versus API-priced tokens | yes | C2 | none |
| Twelve consumer plan guides [55], [56], [59], [60], [92], [93], [94], [95], [96], [97], [101], [103] | limits, verdicts, ratings; no dollars | yes | C2 to E5 | none |
| GitHub Copilot [110], [112] | credits at API rates (vendor-defined) | yes | A1 vendor; C3 independent | none |
| Cursor [114], [115] | multiples of an entry plan; frontier models billed separately | yes | A1 vendor | none |
| Chinese vendor plans [123], [124], [126], [127] | price and quota in requests or prompts | yes | A1 to C4 | none |
| Community posts [117], [118], [119] | individual allowance estimates | yes | C3 to D4 | none |
| ValueRank [91] | 16 dimensions; total cost; plan-derived cost per Index point | yes | A1 (COI) | n/a |

_Table 6. Comparative landscape. COI: conflict of interest._

### Verdict on the four assumptions

| Assumption | Verdict | Basis |
|---|---|---|
| A1: no other public site combines quality and plan cost at the model level | Supported as a bounded negative that depends on the definition of combine | No site read satisfies (a) quality, (b) plan-derived cost and (c) a joined ranked figure. Partial: RemakeBench has evidence and allowance but "no aggregate score" [109]; Klu shows a plan-priced model in a footnote with no computed value [18]. Guides, Copilot, Cursor and Chinese plans do not join to quality [92], [110], [115], [123]. Not read: Gemini primary plan pages, five lead-scan pages, SemiAnalysis's paywalled section |
| A2: several sites offer API price-performance views | Confirmed | Thirteen aggregators with different formulas; five of twelve in Table 2 take AA cost or the index [29], [31], [38] |
| A3: plan comparisons exist mostly as posts and trackers | Partly refuted | Two sites keep plan-level measurements (Wokey weekly, RemakeBench dated) [52], [107]; twelve consumer guides convert no allowance to dollars; individual measurements sit in posts [117], [118]; no maintained model-level ranking was found |
| A4: dated, exact-variant, graded evidence is rare | Split | Dating at nine of twelve aggregators; variant labels at three; imputation policy at two; per-number evidence classes not found, BenchLM a partial analogue [106], [87] |

_Table 7. Assumption verdicts._

### Head-to-head: method, evidence, cost treatment and audience

Table 8 sets ValueRank beside the nearest sites on the four dimensions the question names. ValueRank's row is drawn from its published documentation. Audience and funding cells carry only what a page states.

| Site | Method | Evidence | Cost treatment | Audience and funding |
|---|---|---|---|---|
| ValueRank [91] | multi-dimension score over exact variants; missing values stay missing | dated snapshots; four evidence classes | AA total cost; that cost divided by plan Value Multiple and Index | owner-run; audience not stated in the text read |
| Artificial Analysis [15], [1] | index of ten evaluations, own runs | dated; variant and effort named; version labels | measured tokens at API prices plus live cache rates | commercial; terms restrict reuse [129] |
| TokenCost [31] | quality divided by blended price | method page; no imputation; exclusions listed | blended list price | not stated |
| BenchLM [29], [106] | weighted score divided by output price | formula and caveat stated; vendor-run numbers labelled | output list price | sells data access [106] |
| SemiAnalysis [50] | targeted prompts per token type, about 5% error | method described; partly paywalled | plan allowance at API list rates | frames work as an input for financial modelling |
| Wokey [52] | weekly account-median measurement | five-account gate; 15% review; dated | plan allowance at official API rates | measures accounts behind its own gateway |
| RemakeBench [107], [108], [109] | Capacity Index beside per-round evidence | dated; single window; Medium confidence stated | API-list equivalents, monthly = weekly x 4 | benchmark lab |

_Table 8. Head-to-head comparison on the four dimensions._

On **method**, ValueRank is the only entry that scores many benchmark dimensions with explicit missing-data handling and also derives a plan-adjusted cost. On **evidence**, the sharpest differences are imputation (TokenCost, BenchLM and ValueRank refuse it; most others state no policy) and per-number classes (only ValueRank, by its own documentation). On **cost treatment**, ValueRank spans measured AA spend for the API basis and a measured allowance multiple for the plan basis, at the price of inheriting two upstreams and the assumptions tested in F9. On **audience and funding**, the pages that state anything are commercial or lead-generating more often than not (affiliate links, advertising, a gateway, a premium tier, data access) [34], [35], [43], [41], [106]; ValueRank is owner-run, which removes the vendor incentive but brings the conflict-of-interest flag that applies to this report.

### Which site answers which question

For "what did this model cost to evaluate", AA's total cost and cost per task are the reference, with the cache-modelling and judge-exclusion caveats [1], [15]. For "which API model gives the most score per list-price dollar", the aggregators answer, depending on formula [29], [31], [38]. For "what does a subscription buy in API-priced tokens", SemiAnalysis is the controlled measurement and Wokey and RemakeBench the cross-checks [50], [52], [107]. For "what does a Copilot or Cursor plan include", the vendor tables [110], [115]. For "which model gives the most quality per plan dollar", only ValueRank answered among the sites read [91]. For "is a cheaper model cheaper per success", Cost-of-Pass, Arize and HAL [27], [67], [69].

**Why the gap exists.** This is the analyst's inference. A model-level plan ranking needs a quality measure per exact variant, an allowance measure per plan and model, and a way to join them that survives changes in limits. Allowances move with date and plan generation, differ by model, come in incompatible units (F8) and are mostly unpublished as absolute counts [55], [50]. The aggregators avoid the problem by pricing tokens at stable, public list rates. A plan-based ranking is therefore more fragile than an API-based one, and its credibility rests on dated, graded provenance, which few sites follow.

**Dependence and correlation.** Five of the twelve aggregators in Table 2 take AA cost or the AA index and Epoch's price work uses AA data [18], [39], [42], [41], [33], [70]; the other seven are documented as using list prices or composites of other benchmarks. The independent measured-spend sources outside AA are Aider, Terminal-Bench, Vals, HAL and LiveBench, each limited to its own benchmark [6], [9], [8], [67], [90]. Drawing on several owners is not distinctive, since TokenCost joins two benchmark owners to list prices [31]. What much of the field shares is the upstream, which is also a licence dependence (F10).

**Unit mismatch.** AA's cost per task, AA's total cost, Cost-of-Pass's cost per success, SuperCLUE's price per question and ValueRank's cost per Index point are five different units [15], [17], [69], [81], [91]. ValueRank's cost per Index point is a derived unit that depends on both the plan multiple and the Index definition and is not comparable to any other site's figure.

## Counterevidence Register

| Statement tested | Counterevidence | Effect |
|---|---|---|
| Nobody maintains a plan-allowance comparison | Wokey remeasures weekly [52]; RemakeBench keeps a dated Capacity Index [107] | A3 revised: maintained, plan-level, quality-free |
| No site puts plan cost beside quality | RemakeBench shows per-round evidence and a share-of-week cost for one model [108]; Klu lists a subscription-only model with plan prices in a footnote [18] | A1 stated as definition-dependent; both partial, with no aggregate or computed value [109] |
| Max 20x allowance figures differ by several times | Like-for-like allowance measurements span 1.7 times; the larger gap came from adding one seat's consumed workload [51] | Spread restated in Table 3 |
| LiveBench and LMArena publish no cost | LiveBench release data has a cost file [90]; secondary relays report LMArena price display [13] | Absences were fetch artefacts for LiveBench, whose file definition and LMArena remain unconfirmed |
| AA is the single anchor | Seven of twelve aggregators are not documented as using AA data; Aider, Terminal-Bench, Vals, HAL and LiveBench publish independent cost [6], [9], [8], [67], [90] | AA dominates cost views but is not alone |
| Plan guides convert allowances into value | Twelve guides keep limits as vendor text, multiples or verdicts [92], [97], [101]; only Copilot defines credits at API rates [110] | Conversion exists only where the vendor or a measurement supplies it |
| ValueRank can reuse AA data freely | AA's terms give a personal, noncommercial licence and require API attribution [129], [130] | Open legal question (F10) |

## Limitations and Gaps

**What could not be read.** SuperCLUE, OpenCompass CompassRank, LiveBench's live site, the LMArena price-performance blog, HELM and the Open LLM Leaderboard space were JavaScript-rendered or returned only a title [76], [77], [5], [28], [80], [23]. The SemiAnalysis primary is partly paywalled and its multiples are known through a secondary summary [46], [50]. Scale's hub was seen as a redirect and a second page [11], [20]. Two Morph pages returned HTTP 429 [98], [99]; reddit.com blocked retrieval, so only mirrors were read [120], [121]; Cursor's pricing page was read as extracted text [114]; Kimi's official page showed no quotas in static text [128]; AA's Data Platform Terms were not retrieved [130]. MemoryPlugin's blog home, ProductCompass and Not Diamond were seen only as titles or directory entries [65], [66], [89]. No primary Gemini plan page was read.

**Pages discovered but not read, and pages read in the second pass.** The lead scan named more than a dozen plan-comparison and coding-cost pages that the first retrieval pass did not read. Table 9 gives their dispositions.

| Lead-scan pages | Disposition |
|---|---|
| aizolo, vortenza, altaitools, tech-insider, docs.bswen, aionx, fast.io, felloai, memoryplugin | read [92], [93], [94], [95], [96], [97], [102], [103], [101]; none converts an allowance to dollars or joins one to quality |
| tembo | read [100]; SWE-bench quality with API cost per task, not plan prices |
| morphllm (two pages) | unreadable, HTTP 429 [98], [99] |
| analyticalinsider.ai home | read [104]; a sales-lead service, a false positive as a value publisher |
| discretestack, neura.market, aiven, yourgpt, llmleaderboard.in | not read; known only from lead-scan search summaries, which are discovery notes and not evidence |
| manishprakash substack, i10x | not read; commentary on coding-agent cost per finished task |

_Table 9. Disposition of lead-scan pages._

Because five pages and the Gemini plan pages remain unread, Reddit was reachable only through mirrors and X posts were not searched, A1 and A3 are bounded to the pages in the bibliography.

**Single-sourced or unsupported claims.** These core points rest on one source or on partial reads and are carried with hedges: BenchLM's formula and caveat (its own pages only) [29], [106]; Wokey's Max 20x-to-Pro ratio of about ten [52]; the RemakeBench allowance (one account, one window, plan string "Pro") [108]; the Hacker News and Inventive HQ measurements (single users) [116], [117], [118]; Chinese plan quotas (a third-party roundup, a community article and a news relay, with no official quota table) [123], [126], [127]; the SuperCLUE quadrant (secondary-only) [81]; OpenCompass, HELM and SWE-bench cost treatment (fetch failures, not shown absent); LMArena price display (D4 relays) [13]; the absence of evidence-class grading (three searches and one topic listing, confidence 0.55) [87]; the SemiAnalysis headline multiples [46]; and the definition of the LiveBench cost file [90], [131].

**Claim-support check.** The automatic check linked 110 active claims to evidence: 62 supported, 43 partial, 5 needing review and 0 unsupported; 6 earlier claims are marked superseded. The checker scores lexical, number and entity overlap with stored quotes, so a partial score often means that a page quote holds part of a sentence and a sibling evidence row holds the rest. The TokenCost, Model Price Watch and Klu formula sentences, which scored partial, were compared by hand with the stored page quotes and match them; the SuperCLUE claim was compared with the Chinese paragraph (F7). Claims below the supported threshold are listed in `validation/verify_claim_support.log`.

**Method limits.** Two search passes on one day cannot prove an absence; A1 and the "alone" statements are bounded negatives. The search was English-led, Chinese material came from press reports and vendor pages, and no European or Indian leaderboard was read. Tool-summarised fetches carry lower confidence. Aggregator pages change daily, plan figures are weekly snapshots, and no archived copies are recorded. Enterprise and negotiated pricing (committed-spend discounts, batch and cache pricing, business seats) and the provider chosen for open-weight models were not compared across sites. The ValueRank baseline is owner-commissioned; its internal documents are marked "(internal context)" and are not evidence.

**Not done.** No site's formula was reproduced, so formula statements are what each page says. Sites were not ranked by traffic. Leaders were compared for two sites only. The 2026 AI Index and later METR reports were not retrieved. No ValueRank plan-cost value was recomputed.

## Recommendations

These are the analyst's judgements, each tied to the finding it rests on. Clauses that use ValueRank's internal project documents are marked "(internal context)".

**1. Position on the plan basis, with its fragility visible.** The plan-basis gap is real in this search (F4, F8, F11), so the plan basis is ValueRank's most distinct feature and its least stable. Publish plan figures as dated ranges with measurement class and window, not point values. The four Max 20x allowance measurements span about 1.7 times (Table 3); the ml0x figure is consumed workload and belongs, if shown, in a separate upper-envelope line [51]. Project instructions designate SemiAnalysis as the numerator source for Anthropic and Codex (internal context); a tolerance band tied to Wokey and RemakeBench would show how stable that choice is [52], [107]. How much the spread matters for ValueRank's ordering is not known here: ValueRank can re-rank under the low and high multiples and count position changes (internal context; an action, not a finding).

**2. Test the plan formula and publish the sensitivity.** F9 finds that the plan basis divides a spend built from AA's token mix by a multiple calibrated on a different, cache-dominated mix, selects the highest eligible multiple, and rests on a partly paywalled numerator. Recompute the plan basis at the lowest and highest allowance in Table 3, publish the rank changes, state the eligibility rule and show results without the maximum rule, and flag models whose AA cost is dominated by output or reasoning tokens. AA's cost is built from input, cache-hit, cache-write, reasoning and answer token prices [15]; whether a per-token-type split is available to find those models was not established. Carry this as the main decision risk.

**3. State what the plan unit does and does not claim.** On some plans cache reads barely count against the meter, so API-equivalent multiples are inflated by cached input and are workload-shaped [50], [51], [52]; this is reported for Anthropic and not established for OpenAI or other plans. Allowances are model-specific [50]. Any worked plan example on the site (internal context: one is planned) should say the unit is "API-equivalent allowance at list rates", not a cash saving, with the lower-bound and assumption caveats that ai-usage-tracker states about its own value [57].

**4. Disclose the cost-per-success gap precisely.** ValueRank's API basis is AA's total cost to run the Intelligence Index [17], [91]. It is a measured spend over all attempts, not a cost per correct solution: tokens spent on failed attempts are in the figure, and it is not divided by the number of successes. State this beside the cost figure and consider showing coverage beside cost, as Arize recommends [27]. Where the LiveBench cost file is used [90], label its unit as ValueRank's ingestion defines it and say that LiveBench's own definition was not found [131], so it is not mixed with AA's.

**5. Make the AA dependence explicit, and confirm AA's terms.** Five of the twelve aggregators in Table 2 take AA cost or the AA index [18], [39], [42], [41], [33]. State that ValueRank's API basis is AA's measurement, that AA's cost is partly modelled [1], and the Index version at each snapshot, because composition changes between versions [2], [15]. Separately, confirm with AA or counsel that the way ValueRank obtains and republishes AA figures fits the Terms of Use and the Data Platform Terms, which this report could not retrieve, and carry the attribution the free API requires [129], [130]. Make the same check for LiveBench, whose repository states no data licence [131]. These are legal questions outside this report.

**6. Borrow named practices, and archive what you cite.** Adopt TokenCost's listed exclusions [31], Klu's per-effort view [18], Wokey's minimum-account gate and cadence [52], aimodelscompared's "Not published" convention [55], BenchLM's labelling of vendor-run numbers [106] and Terminal-Bench's separation of model and agent [9]. At each refresh keep a date-stamped copy or snapshot link of every cited page, because plan figures come from pages that change weekly [52] and cannot be re-checked later.

**7. Watch the nearest neighbours, with explicit triggers.** Check RemakeBench's Capacity Index, Wokey's weekly figures and the Copilot and Cursor plan pages at each refresh [107], [52], [110], [115]. Withdraw the "only site found" statement if any site (i) publishes an aggregate quality score beside a plan-derived cost, (ii) adds a quality-adjusted plan column, or (iii) divides a plan allowance by a quality index, or if the unread pages (Gemini plan pages, five lead-scan sites) show such a view. Wokey and RemakeBench must not replace the controlled measurement, but a divergence from it signals that a limit changed.

**8. Avoid claims the evidence cannot carry.** Do not call ValueRank the only site that ranks models on value; say it is the only one found in this search that joins benchmark quality to plan cost at the model level, with the conflict-of-interest note and the definition of combine. Do not quote LMArena's price display or the SuperCLUE quadrant as confirmed, cite a single Max 20x or Pro allowance without date, window and measurement class, or describe AA's or LiveBench's licence position beyond what the terms state.

**9. Treat audience positioning as a hypothesis.** ValueRank's own site audit found its single-page layout did not separate decision makers, analysts and auditors (internal context, not evidence). Whether buyers of coding-agent subscriptions want a quality-adjusted plan comparison was not tested. The pages read show no site serving that need [92], [110], [115], but absent supply is not evidence of demand; it is a question for a later study.

## Claims-Evidence Table

| Claim | Outcome | Principal sources |
|---|---|---|
| AA publishes measured cost per task and total cost and excludes plan pricing for coding agents | Confirmed, B2 | [15], [16], [17] |
| Thirteen sites publish API price-performance views with different formulas | Confirmed | [29], [31], [38], [34], [18] |
| Five of the twelve aggregators in Table 2 take AA cost or the AA index | Partly confirmed (C3 pages, B2 anchor); seven not documented as AA-derived | [18], [39], [42], [41], [33] |
| Benchmark owners publish measured cost | Confirmed; the LiveBench file's definition is unconfirmed | [6], [9], [8], [67], [90] |
| Claude Max 20x allowance measurements span about 1.7 times; ml0x is consumed workload | Contested within a range, no A or B anchor | [52], [118], [107], [46], [51] |
| OpenAI $200 plan figures fall with date and plan label | Consistent with a plan change; not shown | [117], [107], [116], [46] |
| Copilot credits are defined at API rates; Cursor sells third-party models outside the plan fee | Confirmed from vendor pages; independent source for Copilot | [110], [112], [114], [115] |
| No site joins quality to plan cost at the model level | Bounded and definition-dependent | [109], [18], [44], [110], [115] |
| ValueRank's plan formula treats the multiple as workload-independent | Analyst's inference from the sources | [50], [51], [52], [1] |
| AA's terms give a personal, noncommercial licence and require API attribution | Confirmed, primary | [129], [130] |
| No per-number evidence class was found | Bounded negative; BenchLM a partial analogue | [87], [106] |
| SuperCLUE published a cost quadrant on 30 June 2026 | Secondary-only | [81], [78], [76] |

## Bibliography

All entries were accessed on 2026-10-17. Each ends with source type and store grade; "n.d." means the registry holds no date.

[1] Artificial Analysis (n.d.). [Artificial Analysis Intelligence Benchmarking Methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking). method page, B2.
[2] Artificial Analysis (n.d.). [AA methodology (ja) via search snippet](https://artificialanalysis.ai/ja/methodology/intelligence-benchmarking). method page, B3, search summary.
[3] Artificial Analysis (n.d.). [Claude Opus 5 (Adaptive Reasoning, Max Effort) model page](https://artificialanalysis.ai/models/claude-opus-5). official, B3, search summary.
[4] Epoch AI (n.d.). [Epoch AI Benchmarking Hub](https://epoch.ai/benchmarks). official, B2.
[5] LiveBench (n.d.). [LiveBench 2.0](https://livebench.ai/). official, C4.
[6] Aider (n.d.). [Aider LLM Leaderboards](https://aider.chat/docs/leaderboards/). official, B2.
[7] LLM Stats (n.d.). [LLM Stats](https://llm-stats.com/). official, C3.
[8] Vals AI (n.d.). [Vals AI benchmarks](https://www.vals.ai/benchmarks). official, B3.
[9] Terminal-Bench (n.d.). [Terminal-Bench leaderboard](https://www.tbench.ai/leaderboard). official, B3.
[10] SWE-bench (n.d.). [SWE-bench official leaderboards](https://www.swebench.com/). official, C3.
[11] Scale AI (n.d.). [Scale SEAL leaderboard (redirect from scale.com/leaderboard)](https://labs.scale.com/leaderboard). official, F6, page not read.
[12] BenchLM (n.d.). [BenchLM LMArena alternative](https://benchlm.ai/alternatives/lmarena). forum, D5, page not read.
[13] AlphaSignal (n.d.). [LM Arena merges 12 leaderboards into one dashboard](https://alphasignal.ai/news/lm-arena-merges-12-ai-leaderboards-into-one-free-dashboard). news, D4, search summary.
[14] remio.ai (n.d.). [Arena agent results claim, verification lags](https://www.remio.ai/post/arenas-gpt-6-sol-max-agent-arena-results-claim-a-7-7-gain-but-verification-lags). analysis, D4, search summary.
[15] Artificial Analysis (2026-10-17). [Artificial Analysis Intelligence Index v4.3.2 (cost views)](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index). official, B2.
[16] Artificial Analysis (2026-10-17). [AI Coding Agent Benchmarks & Leaderboard](https://artificialanalysis.ai/agents/coding-agents). official, B2.
[17] Artificial Analysis (n.d.). [GLM-5 model page](https://artificialanalysis.ai/models/glm-5). official, B3.
[18] Klu (2026-10-13). [LLM Leaderboard 2026: Compare Quality, Price, and Speed](https://klu.ai/llm-leaderboard). official, C3.
[19] Vellum (2026-09-28). [LLM Leaderboard](https://www.vellum.ai/llm-leaderboard). official, C3.
[20] Scale AI (n.d.). [AI Model Leaderboards & Benchmarks (scale.com)](https://scale.com/leaderboard). official, B3.
[21] LiveBench (n.d.). [LiveBench GitHub repository](https://github.com/LiveBench/LiveBench). official, B3.
[22] Hugging Face (2024-06-30). [Open LLM Leaderboard v1 (archive)](https://huggingface.co/docs/leaderboards/en/open_llm_leaderboard/archive). official, A2.
[23] Hugging Face (n.d.). [Open LLM Leaderboard Space](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard). official, C4.
[24] Thread Reader (2025-03-13). [Clementine Fourrier thread archive](https://threadreaderapp.com/user/clefourrier). forum, C3.
[25] Hugging Face (community article) (2025-12-04). [AI Energy Score v2: Refreshed Leaderboard, now with Reasoning](https://huggingface.co/blog/sasha/ai-energy-score-v2). official, B2.
[26] Hugging Face Optimum (n.d.). [LLM-Perf Leaderboard](https://huggingface.co/spaces/optimum/llm-perf-leaderboard). official, C3.
[27] Arize AI (n.d.). [Cost per successful task: Benchmarking Kimi K3, GPT-5.5, and 8 more AI models](https://arize.com/blog/cost-per-successful-task-a-better-benchmark-for-open-and-frontier-models). analysis, C2.
[28] Arena (LMArena) (2025-01-01). [Arena price-performance blog](https://blog.lmarena.ai/blog/2025/arena-price/). method page, E5, page not read.
[29] BenchLM (2026-10-17). [Best Value LLM Overall (October 2026)](https://benchlm.ai/best/best-value-overall). method page, C2.
[30] BenchLM (n.d.). [LLM price-performance (mirror note)](https://benchlm.ai/llm-price-performance). method page, C3.
[31] TokenCost (n.d.). [LLM Rankings: Every List, With the Method](https://tokencost.app/rankings). method page, B2.
[32] KickLLM (2026-04-07). [LLM Value Index 2026: 40+ Models Ranked by Quality Per Dollar](https://kickllm.com/research/llm-value-index-2026.html). analysis, D3.
[33] Analytical Insider (2026-03-21). [Top 50 LLM Comparison: Price vs Performance 2026](https://analyticalinsider.ai/blog/top-50-llm-comparison-price-performance-2026). analysis, D3.
[34] CostGoat (2026-10-16). [LLM API Pricing Comparison & Cost Guide (Oct 2026)](https://costgoat.com/compare/llm-api). official, C2.
[35] PricePerToken (2026-10-17). [Price Per Token: Compare 300+ AI Model Costs](https://pricepertoken.com). official, C3.
[36] Artificial Analysis (2026-10-17). [Artificial Analysis models](https://artificialanalysis.ai/models). official, B2.
[37] OpenRouter (2026-10-16). [OpenRouter Rankings](https://openrouter.ai/rankings). official, B2.
[38] modelpricewatch.com (2026-10-17). [Model Price Watch rankings](https://modelpricewatch.com/rankings/). method page, C2.
[39] WhatLLM (2026-10-17). [WhatLLM explore](https://whatllm.org/explore). official, C3.
[40] Analyxa LLC (per page) (2026-10-17). [LM Market Cap](https://lmmarketcap.com). official, C3.
[41] AI Model Comparison (n.d.). [AI Model Comparison](https://aimodelcomparison.org). official, C3.
[42] Dervity (2026-09-01). [Benchmark dashboard](https://dervity.com/tools/benchmark-dashboard). official, C3.
[43] Swfte (2026-10-17). [Swfte AI leaderboard](https://swfte.com/ai/leaderboard). official, C3.
[44] aipricing.guru (2026-10-17). [Subscription vs API Cost Calculator](https://www.aipricing.guru/subscription-vs-api/). official, C2.
[45] AIToolsRank (2026-09-01). [API vs ChatGPT Plus / Claude Pro (2026): Cost Math](https://aitoolsrank.io/best/api-vs-subscription/). analysis, D4.
[46] explainx.ai (2026-10-06). [Claude vs ChatGPT Plans: 5x API Value Gap (SemiAnalysis)](https://www.explainx.ai/blog/semianalysis-claude-vs-chatgpt-subscription-api-value-limit-testing-2026). news, C3.
[47] DoiT Cloud Intelligence (2026-08-11). [Cost Per Task, Not Cost Per Token: Claude vs OpenAI Economics](https://www.doit.com/blog/cost-per-task-vs-cost-per-token). analysis, C2.
[48] ailesson.io (llm-price.com redirect) (n.d.). [LLM price comparison](https://ailesson.io/llm-price). official, C3.
[49] Permutable.ai (2025-06-02). [LLM price performance comparison](https://permutable.ai/llm-price-performance-comparison-enterprise-ai/). analysis, D4, search summary.
[50] SemiAnalysis (2026-10-05). [Anthropic subscriptions offer 5x (OpenAI comparison)](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x). analysis, B2.
[51] ml0x (2026-08-28). [Claude Max vs API cost, measured on 33B tokens](https://ml0x.com/research/claude-max-vs-api-cost.html). analysis, C3.
[52] Wokey (2026-10-12). [Claude Usage Limits (October 2026): Pro & Max Weekly Limits, Measured](https://wokey.ai/claude-usage-limits). analysis, C2.
[53] RemakeBench (2026-09-25). [Capacity Index](https://www.remakebench.com/capacity). method page, C3.
[54] RemakeBench (n.d.). [RemakeBench home](https://www.remakebench.com/). official, C3.
[55] AI Models Compared (2026-09-25). [Claude Max vs ChatGPT Pro: What 5x and 20x Actually Mean](https://aimodelscompared.com/claude-max-vs-codex-usage-limits/). analysis, C2.
[56] Explore AI Together (2026-10-14). [LLM Usage Limits 2026: ChatGPT vs Claude vs Gemini vs Grok](https://exploreaitogether.com/llm-usage-limits-comparison/). analysis, C3.
[57] efekoca (GitHub) (n.d.). [ai-usage-tracker](https://github.com/efekoca/ai-usage-tracker). official, C2.
[58] jimdawdy-hub (GitHub) (n.d.). [claude-usage-tracker](https://github.com/jimdawdy-hub/claude-usage-tracker). official, C3.
[59] FuelGauge (2026-03-25). [Claude, ChatGPT, Gemini limits guide](https://fuelgauge.pro/guides/claude-chatgpt-gemini-limits/). analysis, C3.
[60] UseRightAI (2026-10-10). [AI plan limits](https://userightai.com/ai-plan-limits). analysis, C3.
[61] lpm.cx (2026-09-24). [lpm: Claude Code and Codex token usage](https://lpm.cx/claude-code-codex-token-usage). official, C3.
[62] custats.info (n.d.). [CUStats](https://custats.info). official, C3.
[63] claude-monitor.com (n.d.). [Claude Monitor](https://claude-monitor.com). official, C3.
[64] sessionwatcher.com (n.d.). [SessionWatcher](https://sessionwatcher.com). official, C3.
[65] MemoryPlugin (n.d.). [MemoryPlugin blog](https://blog.memoryplugin.com). official, D4, title only.
[66] Product Compass (n.d.). [Claude Code Pricing: Subscriptions vs API](https://www.productcompass.pm/p/claude-code-pricing). analysis, D4, search summary.
[67] Princeton (n.d.). [Holistic Agent Leaderboard (HAL)](https://hal.cs.princeton.edu/). official, B2.
[68] arXiv (Kapoor et al.) (n.d.). [AI Agents That Matter](https://arxiv.org/abs/2407.01502). paper, B2.
[69] arXiv (2025-04-17). [Cost-of-Pass: economic framework for LM evaluation](https://arxiv.org/abs/2504.13359). paper, B2.
[70] Epoch AI (2025-03-12). [LLM inference price trends](https://epoch.ai/data-insights/llm-inference-price-trends). analysis, B2.
[71] arXiv (2025-11). [The Price of Progress: Price Performance and the Future of AI](https://arxiv.org/abs/2511.23455). paper, B2.
[72] arXiv (2025-10). [Beyond Benchmarks: The Economics of AI Inference](https://arxiv.org/abs/2510.26136). paper, C3.
[73] arXiv (2026-05). [SWE Atlas](https://arxiv.org/abs/2605.08366). paper, C3.
[74] arXiv (2026-01). [ChipBench](https://arxiv.org/abs/2601.21448). paper, C3.
[75] Cloudchipr (2026-05-04). [LLM token costs benchmarked](https://www.cloudchipr.com/blog/llm-token-costs-benchmarked). analysis, C3.
[76] CLUE (n.d.). [SuperCLUE](https://www.superclueai.com/). official, C3, title only.
[77] Shanghai AI Lab (n.d.). [OpenCompass CompassRank](https://rank.opencompass.org.cn/leaderboard-llm). official, C3, title only.
[78] ifeng tech (2026-07). [SuperCLUE token cost quadrant report](https://tech.ifeng.com/c/8tUSdMxc0Fp). news, C3, search summary.
[79] DeepLearning.AI The Batch (n.d.). [Reasoning LLMs Are Pricey to Test](https://www.deeplearning.ai/the-batch/reasoning-llms-are-pricey-to-test). news, B3, search summary.
[80] Stanford CRFM (n.d.). [HELM](https://crfm.stanford.edu/helm/). official, C3, title only.
[81] 经济参考报 via 东方财富网 (2026-07-04). [成本最高相差近20倍 “大模型热”催生词元管理新市场](https://finance.eastmoney.com/a/202607033793885685.html). news, B2.
[82] OpenCompass (n.d.). [OpenCompass司南 - 评测榜单](https://opencompass.org.cn/leaderboard-llm). official, C3, title only.
[83] OpenCompass / Shanghai AI Lab (n.d.). [OpenCompass GitHub README](https://github.com/open-compass/opencompass). method page, A2.
[84] Stanford HAI (2025-04-07). [The 2025 AI Index Report](https://hai.stanford.edu/ai-index/2025-ai-index-report). official, A1.
[85] Stanford HAI (2025-04-07). [Technical Performance, 2025 AI Index](https://hai.stanford.edu/ai-index/2025-ai-index-report/technical-performance). official, A1.
[86] METR (2025-03-19). [Measuring AI Ability to Complete Long Software Tasks](https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/). method page, A1.
[87] GitHub (n.d.). [llm-leaderboard topic](https://github.com/topics/llm-leaderboard). forum, C3.
[88] arXiv authors (n.d.). [OckBench: Measuring the Efficiency of LLM Reasoning](https://arxiv.org/pdf/2511.05722). paper, B3.
[89] tooldirectory.ai (2026-07-08). [Not Diamond (LLM Gateways & Serving)](https://tooldirectory.ai/tools/not-diamond). forum, D4, search summary.
[90] LiveBench (2026-06-25). [LiveBench release data 2026-06-25 (table, cost and categories CSV/JSON)](https://github.com/livebench/new-livebench/commit/7be9f746f36a6f007dd78461f67cb7d06cfe2304). official, A2.
[91] Ālo Labs (2026-10-08). [ValueRank methodology (v1.9.6)](https://valuerank.alolabs.dev/methodology/). method page, A1.
[92] AiZolo (2026-09-11). [ChatGPT vs Claude vs Gemini Cost 2026: Full Pricing Breakdown](https://aizolo.com/blog/chatgpt-vs-claude-vs-gemini-cost-2026/). analysis, D4.
[93] Vortenza (2026-05-13). [ChatGPT Plus vs Claude Pro vs Gemini: Which Is Worth $20? (2026)](https://vortenza.com/guides/chatgpt-plus-vs-claude-pro-vs-gemini). analysis, E5.
[94] Altai Tools (2026-10-14). [ChatGPT Plus vs Claude Pro vs Gemini Pro (2026)](https://altaitools.com/chatgpt-plus-vs-claude-pro-vs-gemini-pro/). analysis, D4.
[95] Tech Insider (2026-08-21). [ChatGPT vs Gemini vs Claude Pro: 2M Token Gap (2026)](https://tech-insider.org/chatgpt-vs-gemini-vs-claude-pro-2026/). analysis, E5.
[96] BSWEN (personal dev blog) (2026-03-13). [ChatGPT Plus vs Claude Pro vs Gemini: Which AI Subscription Should Developers Choose in 2026?](https://docs.bswen.com/blog/2026-03-13-chatgpt-claude-gemini-comparison/). forum, E5.
[97] AionX (2026-10-15). [AI chatbot rate limits compared: Head-to-Head Comparison](https://aionx.co/ai-comparisons/ai-chatbot-rate-limits-compared/). analysis, D4.
[98] Morph (n.d.). [Best AI Coding Agents 2026](https://www.morphllm.com/best-ai-coding-agents-2026). analysis, F6, page not read.
[99] Morph (n.d.). [Cursor vs Copilot (2026)](https://www.morphllm.com/comparisons/cursor-vs-copilot). analysis, F6, search summary.
[100] Tembo (2026-06-01). [Best LLM for Coding in 2026: Ranked by Benchmarks](https://www.tembo.io/blog/best-llm-for-coding). analysis, C3.
[101] MemoryPlugin (2026-10-13). [ChatGPT Plus vs Claude Pro vs Google AI Pro (2026)](https://blog.memoryplugin.com/chatgpt-plus-vs-claude-pro-vs-google-ai-pro/). analysis, C3.
[102] Fast.io (2026-06-14). [AI Model Comparison 2026: Benchmarks, Pricing, Rankings](https://fast.io/resources/ai-model-comparison-2026/). analysis, D4.
[103] Fello AI (2026-10-14). [How Much Does AI Cost in 2026? Complete Pricing Comparison](https://felloai.com/ai-pricing-comparison/). analysis, D4.
[104] Analytical Insider (n.d.). [Analytical Insider (home page)](https://analyticalinsider.ai/). analysis, F6.
[105] WhatLLM.org (2026-09-06). [LLM Comparison Methodology | Data Sources & Intelligence Index Explained](https://whatllm.org/methodology). method page, B2.
[106] BenchLM.ai (n.d.). [BenchLM Methodology](https://benchlm.ai/methodology). method page, B2.
[107] RemakeBench (2026-09-25). [Subscription Capacity Index](https://remakebench.com/capacity). analysis, B2.
[108] RemakeBench (2026-09-25). [Claude Max 20x capacity detail](https://remakebench.com/capacity/plans/claude-max-20x). analysis, B2.
[109] RemakeBench (2026-10-08). [Opus 5.5 vs GPT-6 Astra vs Sonnet 5.5 vs GPT-6.1 Sol (Launch 006)](https://remakebench.com/opus-5-5-vs-gpt-6-astra-vs-sonnet-5-5-vs-gpt-6-1-sol). analysis, B2.
[110] GitHub Docs (n.d.). [Plans for GitHub Copilot](https://docs.github.com/en/copilot/get-started/plans). official, A1.
[111] GitHub Docs (n.d.). [Requests in GitHub Copilot (legacy)](https://docs.github.com/en/copilot/concepts/billing/copilot-requests). official, A1.
[112] CloudZero (n.d.). [GitHub Copilot Cost](https://www.cloudzero.com/blog/github-copilot-cost). analysis, C3.
[113] PricePerToken (2026-06-01). [Cursor vs GitHub Copilot: Pricing & Which to Choose](https://pricepertoken.com/coding-assistants/compare/cursor-vs-github-copilot). analysis, D4.
[114] Cursor (Anysphere/X) (n.d.). [Cursor Pricing](https://cursor.com/pricing). official, A1.
[115] Cursor (n.d.). [Cursor Docs: Models & Pricing](https://cursor.com/docs/models-and-pricing). official, A1.
[116] Inventive HQ (author Sean) (2026-10-04). [How Much Codex Does a ChatGPT Plan Buy? I Measured It](https://inventivehq.com/blog/codex-subscription-usage-measured). forum, C3.
[117] Hacker News (2026-07-18). [HN comment by Tiberium on Codex Pro 20x allowance](https://news.ycombinator.com/item?id=48963639). forum, D4.
[118] Hacker News (aray07) (2026-03-26). [Show HN: I tried to reverse engineer Claude Code usage limits](https://news.ycombinator.com/item?id=47536655). forum, C3.
[119] Hacker News (2026-04-24). [HN comment by crazylogger on Claude Code usage limit generosity](https://news.ycombinator.com/item?id=47886827). forum, D4.
[120] Reddit Sentiment Analyzer / Sentinel Team (mirror) (2026-04-09). [Reddit r/ClaudeAI snapshot 'Options' (archived by third party)](https://reddit.sentinel-team.org/posts/1sdwkbe/snapshots/2026-04-09T16%3A41%3A00.47446Z). forum, D5.
[121] Reddit Sentiment Analyzer / Sentinel Team (mirror) (2026-01-28). [Reddit snapshot: 'Claude Subscriptions are up to 36x cheaper than API' (archived)](https://reddit.sentinel-team.org/posts/1qpcj8q/snapshots/2026-01-28T18%3A37%3A33.056349Z). forum, D5.
[122] CodePick (2026-08-19). [Claude Max Plan Value Analysis (2026): Is the 5x or 20x Tier Worth It?](https://codepick.dev/en/guides/claude-max-plan-value-analysis/). analysis, D4.
[123] CodePick (2026-05-19). [国内 Coding API 横评 2026 (China coding API roundup)](https://codepick.dev/zh/guides/china-coding-api-roundup-2026/). analysis, D4.
[124] Z.ai (Zhipu) docs (n.d.). [GLM Coding Plan Overview](https://docs.z.ai/devpack/overview.md). official, A1.
[125] IT之家 (ITHome) (2026-04-22). [智谱：GLM Coding Plan 老套餐（无周限额版本）4 月 30 日停止自动续订](https://www.ithome.com/0/941/977.htm). news, B2.
[126] Alibaba Cloud Developer Community (2026-04-13). [阿里云 Coding Plan 指南：是什么？售罄怎么办？价格与用量额度一次说清](https://developer.aliyun.com/article/1726011). official, B3.
[127] KuCoin Flash (relaying BlockBeats) (2026-09-18). [Kimi Launches New Subscription Tiers After Two-Month Pause](https://www.kucoin.com/news/flash/kimi-launches-new-subscription-tiers-after-two-month-pause-kimi-code-not-sold-separately). news, C4.
[128] Moonshot AI (n.d.). [Kimi Code (Moonshot AI official)](https://www.kimi.com/code). official, B3.
[129] Artificial Analysis (2026-09-15). [Website Terms of Use](https://artificialanalysis.ai/terms-of-use). official, A1.
[130] Artificial Analysis (n.d.). [Artificial Analysis Free Data API documentation](https://artificialanalysis.ai/api-reference). official, A1.
[131] LiveBench (GitHub) (n.d.). [LiveBench README](https://raw.githubusercontent.com/LiveBench/LiveBench/main/README.md). official, B2.

## Methodology Appendix

**Process.** Phases followed the nested flow in the deep-research skill: scope, plan, retrieve (four angles plus a lead scan, then a second pass of 40 sources and 55 evidence rows after the first critique, all with host web tools because search-cli was unavailable), triangulate, outline, synthesize, critique (two cycles, 24 deltas, five high severity) and refine. Triangulation recorded per core claim the evidence rows, source grades, independent-confirmation status and escalation outcome, and logged sixteen contradictions. The refine pass added F8 to F10, rewrote F4 and the overlap finding, and moved Limitations ahead of Recommendations, as the assembly guide orders them.

**Grading.** Sources carry a letter for reliability and a digit for credibility; a core claim needs one A or B1/B2 source or three C sources. Evidence confidence values (0 to 1) assigned by the retrieval agents are noted where they limit a statement. The store grades are the retrieval agents' own; where a single-window page carries a B2 grade (RemakeBench), the text states the limitation.

**Counting.** Weekly equivalents in Tables 3 and 3b are the analyst's arithmetic: a month is four weeks (the RemakeBench convention) or 4.33 weeks; implied monthly multiples are the weekly figure times four divided by the $200 fee; percent differences use the larger figure over the smaller. Counts of aggregators and practices are tallies over Table 2 and the register in `triangulation.md`, not source figures.

**Trust boundary.** Web and PDF content was treated as data; no instruction found in any page was followed. Future-named models (for example Claude Opus 5.5, GPT-6.1 Sol, Qwen3.7 Flash, Ling 3.1 Flash) are reproduced as the pages state them.

**Companion artefacts.** `triangulation.md`, `outline.md`, `claims.jsonl`, `critique.md` (with the refine disposition) and the logs in `validation/`.

## Report Metadata

| Field | Value |
|---|---|
| Run | 2026-10-17-value-ranking-sites-landscape |
| Mode | deep |
| Research type | default |
| Retrieval date | 2026-10-17 (two passes) |
| Refine date | 2026-10-17 |
| Sources registered | 131 (99 publisher labels) |
| Evidence rows | 273 |
| Core claims triangulated | 28 |
| Critique deltas | 24 (5 high), all dispositioned in `critique.md` |
| Claim support | 62 supported, 43 partial, 5 needs review, 0 unsupported of 110 active claims (6 superseded rows retained) |
| Citations checked | 126 of 131 URLs reachable; 5 unverified (two Morph pages with HTTP 429, three Hacker News items whose servers reject HEAD with HTTP 405), 0 suspicious |
| Baseline conflict of interest | ValueRank methodology (source 91) is owner-commissioned |
