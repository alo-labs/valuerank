# MiMo token plans sell API credit near par

**As of 2026-10-23, no measured value multiple exists for Xiaomi's MiMo Token Plans for either MiMo-V2.6-Pro or MiMo-V2.6-Flash at any tier.** No subscriber has published a full billing period of model-attributed usage priced at API rates. The in-window evidence (2026-09-22 to 2026-10-23) is partial. The strongest fragments are:
- a V2.6-Pro Lite subscriber who used about **0.56–0.70× of the fee** part-way through a period;
- a Pro-tier subscriber with mixed or unidentified models who had consumed about **0.42–0.45× of the list fee** within the first days of a period;
- a one-day V2.6-Pro token ledger worth **$8.72** at API rates, on an unnamed tier that must be Standard or above.

No V2.6-Flash-specific plan usage report exists at all. The binding fact comes from Xiaomi's own rate cards: plan Credits are priced at par with pay-as-you-go API rates. Each tier's full quota is therefore worth only about **0.96–1.24× its monthly fee** at peak rates. Night-time and purchase discounts can lift that to roughly 1.7×. This ceiling is arithmetic on provider claims, not a measurement, and no user can realise more than it. For ValueRank, the MiMo Plan route is effectively prepaid API at a small discount. It should be recorded as "value multiple not identified by end-user measurement," with the quota-implied ceiling kept separately as a provider claim.

## No subscriber has published a full V2.6 billing period

Every data point found in the window fails at least one requirement: a completed billing window, an exact model, a known fee, or an API-priceable quantity. The table keeps those gaps visible rather than smoothing them over.

A conversion makes these fragments priceable. Xiaomi's credit deduction table charges mimo-v2.6-pro 2.5 / 300 / 600 Credits and mimo-v2.6-flash 2 / 100 / 200 Credits per cache-hit input, cache-miss input and output token ([MiMo Token Plan](https://mimo.mi.com/docs/en-US/price/token-plan)). Divided by the domestic rate card of ¥0.025 / ¥3 / ¥6 and ¥0.02 / ¥1 / ¥2 per million tokens ([MiMo Pay-As-You-Go](https://mimo.mi.com/docs/en-US/price/pay-as-you-go)), this gives **100M Credits = ¥1 of API value exactly**, whatever the model or token mix. At overseas USD rates, 1B Credits equals about **$1.45 of V2.6-Pro** or **$1.40 of V2.6-Flash** usage. A V2EX user stated the same rule independently: "1 亿 credits 等效 1 元" ([V2EX t/1243834 #60](https://www.v2ex.com/t/1243834)). A user's dashboard credit reading can therefore be priced at API rates without a token split. Two caveats apply. Off-peak usage (Beijing 00:00–08:00, 0.8× coefficient) burns fewer Credits than its API value, so credit-derived values are lower bounds. The multiple also needs the actual fee paid, which most reports omit.

**In-window data points (report dated 2026-09-22 to 2026-10-23)**

| # | Source and date | Tier, fee | Window | Model | Reported usage | API-priced value (method) | Partial value ÷ fee | Qualifies? |
|---|---|---|---|---|---|---|---|---|
| 1 | dancyuser, [openai/codex#53752](https://github.com/openai/codex/issues/53752), 2026-10-13 | "Xiaomi MiMo Token Plan (Singapore)"; tier and fee not stated | One day (2026-10-13) | **mimo-v2.6-pro** | Xiaomi dashboard: 19,829,403 cache-miss input, 4,441,344 cache-hit input, 89,906 output (24,360,653 total). Local logs agree within about 1% | **$8.72** (miss × $0.435 + hit × $0.0036 + out × $0.87 per M), or ¥60.14 at CNY rates. About 6.01B Credits at peak, which exceeds Lite's 4.1B, so the tier is Standard or above | One day equals 0.55× of Standard ($16), 0.17× of Pro ($50) or 0.087× of Max ($100) | No: fee and tier unknown, single day |
| 2 | LazyGatto, [OmniRoute#15753](https://github.com/diegosouzapw/OmniRoute/issues/15753), 2026-10-07 | Pro (`planCode: pro`, limit 38,000,000,000). Upgraded from Lite, so the amount paid was an upgrade difference and is unknown | Period ending 2026-11-05 23:59:59, still open | Unidentified (plan level) | 14,954,038,035 Credits used (`percent: 0.3935`) | ≥ ¥149.54 at the CNY peg; ≥ $21.68 if all V2.6-Pro or ≥ $20.94 if all Flash | ≥ 0.45× of ¥329, or 0.42–0.43× of $50 list, so far | No: period incomplete, model mix unknown, paid fee unknown |
| 3 | AppleHuman8535, [r/opencode](https://www.reddit.com/r/opencode/comments/1wphykw/i_tried_xiaomi_mimo_token_plan_and_i_really_dont/), 2026-09-25 | Lite, "$5" (consistent with the $5.28 first-purchase price) | From purchase (date unstated) to the post | **V2.6-Pro** ("the only working model") | "I still have 50% left"; 3–4% per one-hour task; used only off-peak ([detail](https://www.reddit.com/r/opencode/comments/1wphykw/i_tried_xiaomi_mimo_token_plan_and_i_really_dont/pbvntrq/)) | 2.05B Credits ≈ $2.97 peak-equivalent, or ≈ $3.72 because off-peak credits buy 1.25× the tokens | **0.56–0.70×** part-way through the window | No: window open and undated. Best model-matched fragment |
| 4 | mimiga, [V2EX t/1243834 #57](https://www.v2ex.com/t/1243834), 2026-09-22 | Lite, ¥39 | One session (project analysis and edits) | Unstated; V2.6 launch-day thread | Dashboard "52,841,980 / 4,100,000,000 已使用 1.0%"; "Token 总消耗 1,542,683 Tokens" | ¥0.53 at the CNY peg | 0.014× for one session | No: single session, model unstated |
| 5 | TheVoyant, [r/opencode](https://www.reddit.com/r/opencode/comments/1wmoiaw/mimo_v_26_pro_and_flash_released/pb9av31/), 2026-09-21 22:44 UTC (2026-09-22 06:44 Beijing) | Max, $100 list, "like 25% off" ([fee](https://www.reddit.com/r/opencode/comments/1wmoiaw/mimo_v_26_pro_and_flash_released/pb9irrl/)) | One morning, three tasks | V2.6-Pro per the thread; the dashboard figure is not labelled by model | "55,026,944 / 82,000,000,000 Used 0.0%"; "I've never used a full monthly amount on the $100 plan" | ≈ $0.08 | ≈ 0.001× | No: partial morning |
| 6 | Kei001, CosmoLau, dko, [V2EX t/1243835](https://www.v2ex.com/t/1243835), 2026-09-22 | Max ¥659; Pro ¥329 (promo-acquired); Standard ¥99 (inferred) | Billing month ending at the 2026-09-22 renewal (V2.5 era) | Unstated, pre-V2.6 | Zero use (renewal ¥0.00); renewal charge ¥10; renewal charge "十几块" | ≈ ¥0; ≈ ¥11.6 under the plan-price offset rule; ≈ ¥11–21 under the last-paid-price rule | ≈ 0×; ≈ 0.04×; ≈ 0.11–0.21× | No: measurement window predates V2.6 and falls outside the target month. Shown for context only |

ConsiderationNo9952 compared the dashboard before and after against OpenCode's token counts. He concluded the per-token credit rates hold, so pay-as-you-go comes out about level with the Standard plan. He added that "there is additional 20% discount on off peak times so that probably brings the plan back ahead" ([r/opencode](https://www.reddit.com/r/opencode/comments/1wn27ra/mimo_26_flash_vs_pro_latency_mimo_token_plan/pbc2wax/)). That is the only user-side check of the credit peg. It gives no numbers, tier or window, and it mixes Pro and Flash. In-window subscribers who gave no quantities are not data points. They include an annual-Standard buyer who found "no more surplus or extra credits" ([r/opencode](https://www.reddit.com/r/opencode/comments/1wphykw/i_tried_xiaomi_mimo_token_plan_and_i_really_dont/pbz73wv/)) and a five-month Standard subscriber who called V2.6 "unusable right now" ([r/opencodeCLI](https://www.reddit.com/r/opencodeCLI/comments/1wughtd/is_it_the_same_on_opencode_too_mimo_v26_pro/pdan6uq/)). AppleHuman8535 also guessed that Lite "basically just gives you $5 worth of credits", which he labelled "just speculating" ([r/opencode](https://www.reddit.com/r/opencode/comments/1wphykw/i_tried_xiaomi_mimo_token_plan_and_i_really_dont/pbvix6j/)). That is an opinion about the quota, not a measure of what he consumed, so it is not a numerator.

The resulting answer per tier and model is blunt:

| Tier (individual and team, monthly and annual) | MiMo-V2.6-Pro measured multiple | MiMo-V2.6-Flash measured multiple |
|---|---|---|
| Lite | **Not established.** Partial: 0.56–0.70× part-way (row 3) | **Not established.** No report |
| Standard | **Not established.** Row 1 may be Standard (one day ≈ 0.55×) | **Not established.** No report |
| Pro | **Not established.** Plan-level partial ≥ 0.42–0.45× (row 2, model unknown) | **Not established.** No report |
| Max | **Not established.** Row 5 is about 0.001× for one morning | **Not established.** No report |

V2.6-Flash has no measurement at any tier. Users in the window mostly report rejecting Flash on the plan: AppleHuman8535 said it "can't even use it as a subagent". Others used it free through OpenCode Zen instead ([Kingy.ai](https://kingy.ai/blog/mimo-v2-6-pro-free-access-pricing-setup/)).

## Older V2.5-era ledgers show heavy users reaching the ceiling

Before V2.6, more users posted consumption, and several exhausted their pools quickly. These reports used the same post-2026-05-27 credit regime: V2.5-Pro and V2.5 had the same per-token Credit and API rates that V2.6-Pro and V2.6-Flash inherited ([MiMo-V2.6 news](https://mimo.mi.com/docs/en-US/news/latest/v2-6)). They are a different model generation, so none of them transfers to V2.6. They are listed only to show what realised multiples looked like.

| Source and date | Tier, fee | Window | Model | Reported usage | API-priced value ÷ fee |
|---|---|---|---|---|---|
| ZombieHomster, [r/hermesagent](https://www.reddit.com/r/hermesagent/comments/1v39jq6/need_help_picking_a_model/oz1cp00/), 2026-07-22 | Pro, $50 | about 2026-07-01 to 07-20 | MiMo-V2.5 | 741.21M cache-hit, 122.82M miss and 2.84M output tokens over 4,820 requests (stats obtained "through Perplexity") | ≈ $20.1 (≈ 14.3B Credits), **≈ 0.40×** in about 20 days |
| starwaves1, [r/openclaw](https://www.reddit.com/r/openclaw/comments/1txo5cu/which_ai_models_are_cheap_and_worth_it/oq10saf/), 2026-06-06 | Standard, $16 | "the last few days" | MiMo 2.5 | 346M tokens; 75% of quota | ≈ 8.25B Credits ≈ $11.6, **≈ 0.72×** in days |
| One-Trainer2235, [r/hermesagent](https://www.reddit.com/r/hermesagent/comments/1uclfcf/hermes_agent_manifest_llm_router/), 2026-06-22 | Lite, $6 | 2 days | Unstated | "2 days to spend all 4 billions credits" | ≈ $5.7–6.0, **≈ 0.96–0.99×**, then service suspends |
| purize420, [r/MiniMax_AI](https://www.reddit.com/r/MiniMax_AI/comments/1ty0anz/trying_to_be_patient_but_also_anyone_switch_to/oqav57v/), 2026-06-07 | Lite (4.1B) | under 1.5 h | V2.5 era | 94% used, "only 40m tokens" | **≈ 0.9×** within hours |
| Wide_Big_6969, [r/LocalLLM](https://www.reddit.com/r/LocalLLM/comments/1u9gohq/open_source_is_starting_to_beat_frontier_on/osrglb1/), 2026-06-20 | Annual Standard, $168.96 | "so far" (undated) | Mixed V2.5-Pro and V2.5 | 300M+ tokens, about 3k requests, about 9.6B Credits | ≈ $13.4–13.9; window unclear |
| dunxuan, [linux.do t/2258823](https://linux.do/t/topic/2258823), 2026-05-28 | Pro, ¥329 | 2026-05-01 to 05-27 | V2.5-Pro | 350M tokens ≈ 47亿 Credits under the new formula | ≈ ¥47, **≈ 0.14×** |
| maweirdos, [linux.do t/2412590](https://linux.do/t/topic/2412590), 2026-06-16 | Pro (granted on application) | "用了几天" (a few days) | Unstated | 8% used | ≈ ¥30.4; grant, not a paid fee |

The pattern is clear even without V2.6 data. Light users realise a small fraction of the fee. Heavy agent users can hit 0.7–1.0× within days and are then cut off, because "When the monthly total quota of the package is used up, the system will suspend the service" ([MiMo Token Plan](https://mimo.mi.com/docs/en-US/price/token-plan)). Pre-May reports (for example 1.6B Credits in 11 days on V2-Omni, [r/openclaw](https://www.reddit.com/r/openclaw/comments/1sp179n/mimo_v2_vs_opus_46/oh1f7qn/)) used an older, roughly 50× smaller credit scale and are not comparable. Free "100T" grants are excluded because they have no fee. They include the V2EX user whose Claude Code tally priced a V2.5-Pro session at $1.25 ([V2EX t/1209234 #55](https://www.v2ex.com/t/1209234)).

## Xiaomi's fees and rate cards are settled

Fees and API rates are not in doubt. Xiaomi's pages, updated 2026-10-21 and read on 2026-10-23, agree across English and Chinese. All three Perplexity answers reproduce them. **Fees can serve as denominators.**

**Token Plan fees (provider, individual edition; Team has Standard, Pro and Max per seat at identical prices, minimum two seats, no Lite)** ([Token Plan, en-US](https://mimo.mi.com/docs/en-US/price/token-plan); [zh-CN](https://mimo.mi.com/docs/zh-CN/price/token-plan); [Individual Subscription](https://mimo.mi.com/docs/en-US/tokenplan/Token%20Plan/subscription))

| Tier | Monthly | Annual (auto-renew, about 12% off) | Billing period |
|---|---|---|---|
| Lite (individual only) | $6 / ¥39 | $63.36 / ¥408 | month; annual quota 12× monthly |
| Standard | $16 / ¥99 | $168.96 / ¥1,044 | month |
| Pro | $50 / ¥329 | $528 / ¥3,468 | month |
| Max | $100 / ¥659 | $1,056 / ¥6,948 | month |

USD and CNY are separate regional schedules. The official CNY annual prices are not exactly 12 × 0.88 of the monthly price (Lite would be ¥411.84), so the published figures should be used. Other provider terms on the same pages:
- A one-time 12% discount on the first individual purchase, which does not stack with annual billing.
- Team annual seats reset their quota monthly.
- The quota is restricted to coding tools, and service suspends when it is exhausted.
- mimo-v2.6-pro-ultraspeed is not covered.
- MiMo-V2.5-Pro and MiMo-V2.5 were retired 2026-10-21 10:00 UTC+8.

The upgrade price is "新套餐价格 −（原套餐剩余额度/原套餐总额度）× 原套餐价格" ([subscription doc, zh-CN](https://mimo.mi.com/docs/zh-CN/tokenplan/Token%20Plan/subscription)). Users report that renewals likewise credit unused quota against the next charge ([V2EX t/1243835](https://www.v2ex.com/t/1243835)), which is why renewal charges reveal usage. A separate MiMo Desktop membership launched with V2.6 on 2026-09-22 ([MiMo-V2.6 news](https://mimo.mi.com/docs/en-US/news/latest/v2-6)). It costs ¥59 / ¥179 / ¥599 / ¥1,199 a month, read from the [pricing page's](https://mimo.xiaomimimo.com/pricing/) JavaScript bundle and not yet confirmed in a browser. It is app-bound, so it is not the Token Plan route.

**Pay-as-you-go real-time API rates (provider, per million tokens, no context-length tiers; cache write free for a limited time; batch at half price)** ([Pay-As-You-Go, en-US](https://mimo.mi.com/docs/en-US/price/pay-as-you-go); [zh-CN](https://mimo.mi.com/docs/zh-CN/price/pay-as-you-go))

| Model | Cache-hit input | Cache-miss input | Output |
|---|---|---|---|
| mimo-v2.6-pro, overseas | $0.0036 | $0.435 | $0.87 |
| mimo-v2.6-pro, China | ¥0.025 | ¥3.00 | ¥6.00 |
| mimo-v2.6-flash, overseas | $0.0028 | $0.14 | $0.28 |
| mimo-v2.6-flash, China | ¥0.02 | ¥1.00 | ¥2.00 |

These rates have held since V2.6's 2026-09-22 launch, which "adopts the same API pricing as the V2.5 series" ([MiMo-V2.6 news](https://mimo.mi.com/docs/en-US/news/latest/v2-6)). OpenRouter lists identical USD prices for both models ([OpenRouter V2.6-Pro](https://openrouter.ai/xiaomi/mimo-v2.6-pro); [V2.6-Flash](https://openrouter.ai/xiaomi/mimo-v2.6-flash)). One Perplexity answer dated the English page "October 08, 2026". The notes observed "October 21, 2026". The rates are the same either way.

## Provider claims cap any realised multiple near 1.2×

Everything in this section is a **provider claim** or arithmetic on one. None of it is a measured numerator, and none of it can be presented as a value multiple under the project's evidence rules.

Xiaomi's monthly quotas are **4.1B, 11B, 38B and 82B Credits** for Lite, Standard, Pro and Max. Using mimo-v2.6-flash as the baseline, it estimates **about 200, 1,600, 5,600 and 12,800 "rounds of medium-to-complex tasks"** a month, without defining a round ([MiMo Token Plan](https://mimo.mi.com/docs/en-US/price/token-plan)). Its launch messaging promised "No 5-hour limits. No throttling." ([Xiaomi MiMo on X](https://x.com/XiaomiMiMo/status/2039918061025972358)). The 2026-05-27 reform claimed "usage increased to 5-8 times the original" ([V2.5 price update](https://mimo.mi.com/docs/en-US/news/latest/v2.5-price-update)). Xiaomi's V2.6 pricing cards, shown in user screenshots, frame tiers as multiples of Lite: Standard "2.7 x", Pro "9.3 x" and Max "20 x" ([V2EX t/1243835](https://www.v2ex.com/t/1243835)).

Because Credits are pegged to the API price, the quota fixes a **full-utilisation ceiling**. This is the most any subscriber could realise, and it is not what any subscriber did:

| Tier | Quota at CNY peg ÷ CNY fee | All-V2.6-Pro at USD rates ÷ USD fee | All-V2.6-Flash at USD rates ÷ USD fee |
|---|---|---|---|
| Lite | ¥41 / ¥39 = 1.05× | $5.95 / $6 = 0.99× | $5.74 / $6 = 0.96× |
| Standard | ¥110 / ¥99 = 1.11× | $15.95 / $16 = 1.00× | $15.40 / $16 = 0.96× |
| Pro | ¥380 / ¥329 = 1.16× | $55.10 / $50 = 1.10× | $53.20 / $50 = 1.06× |
| Max | ¥820 / ¥659 = 1.24× | $118.90 / $100 = 1.19× | $114.80 / $100 = 1.15× |

Using the whole quota off-peak raises each figure by up to 1.25×, and annual or first-purchase pricing by about 1.14×. The theoretical maximum is therefore about 1.7× for an annual Max subscriber running entirely at night. Third parties reached the same ceiling independently: linux.do's lanvent ([t/2254166](https://linux.do/t/topic/2254166)), Kingy.ai's $5.95 and $15.95 estimates ([Kingy.ai](https://kingy.ai/blog/mimo-v2-6-pro-free-access-pricing-setup/)), and the awesome-coding-plan list's "1.12" ([GitHub](https://github.com/mahonzhan/awesome-coding-plan)). These are all quota arithmetic. Reseller claims belong in the same category. OpenCode Go states monthly limits of $15 of MiMo-V2.6-Pro and $60 of Flash on its $10 plan, and $60 and $120 on its $40 Go Plus ([OpenCode Go docs](https://opencode.ai/docs/go/)). That implies 1.5× for Pro and 3–6× for Flash, but it is a reseller claim about a different route.

The ceiling matters even though it cannot be the numerator, because it bounds every measurement. A realised multiple equals the ceiling multiplied by the share of quota actually consumed, and unused Credits expire. A buyer cannot reach the 3–10× multiples that Claude and Codex subscriptions are measured at, however heavily they use the plan. The Gemini 3.8 Flash answer describes the 1.05–1.24× band as "measured". That is wrong: it is the quota arithmetic above.

## Methodology: three research tracks, three Perplexity models and one failed dispatch

This report synthesises three internal research notes compiled on 2026-10-23.

**Official track.** Xiaomi's English and Chinese pricing and Token Plan pages were downloaded with curl and their text extracted locally. Prices are therefore read from page text, not from a summariser. OpenRouter's model API and the OpenCode Go docs were used as cross-checks.

**Chinese end-user track.** This covered V2EX (via the sov2ex index), Bilibili's search API, linux.do topic pages and general web search.

**English end-user track.** Reddit could only be read through the Pullpush archive, and those results end at 2026-10-13 01:38 UTC. Hacker News was searched through Algolia, and DataCamp, Kingy.ai and similar pages were fetched directly.

The brief described four Perplexity answers, but the folder holds three. They come from GPT-6.1 Sol, Grok 4.7 and Gemini 3.8 Flash, each run in Search mode on the same brief, and they were triangulated as independent secondary research. All three reached the same headline: no qualifying measurement exists. They agreed with the internal notes on every fee and rate. They added three new in-window leads, which I checked against the primary pages on 2026-10-23:
- The Grok 4.7 answer surfaced the openai/codex#53752 token ledger and the OmniRoute#15753 Pro-plan reading. Both were confirmed by fetching the GitHub issues (rows 1 and 2).
- The Gemini 3.8 Flash answer surfaced mimiga's V2EX dashboard reading, confirmed by downloading the thread (row 4). Its own "1.0%" label differs from the credit arithmetic (52.8M of 4.1B is 1.29%). The dashboard's percentage display appears coarse.

The GPT-6.1 Sol answer cited three leads, but its file gave no URL for any of them. None could be confirmed, so all are excluded:
- a linux.do post by sun_omg ("关于mimo-2.6计费", 2026-09-28) giving a ¥17 AI-computed API estimate for a month of Telegram auto-replies, with tier and model unconfirmed (that use may also breach the coding-only terms);
- a MiMo-Code GitHub issue #2482 with V2.6-Flash generation counts but no fee;
- the trick77/llmwire repository's Token Plan probes, about $0.065 and $0.034 of API-equivalent test traffic. The repository README is reachable but mentions only V2.5 pricing.

The Grok 4.7 answer gives MiMo Desktop USD prices of $20, $60, $200 and $400 without a primary URL; these remain unconfirmed. GPT-6.1 Sol's statement that V2.5 IDs auto-routed to V2.6 from 2026-10-14 has a third-party source only ([coding-plan.org](https://coding-plan.org/plans/xiaomi)) and remains unconfirmed.

**The project's Silver Bullet multi-model dispatch could not run.** It depends on opencode-go models, and this environment has no opencode provider credentials, so no answers from that model panel are included.

Several coverage gaps remain:
- Reddit after 2026-10-13 is unsearched, because Pullpush rate-limited and Arctic Shift and reddit.com returned errors.
- X search returned HTTP 451.
- linux.do search was behind a Cloudflare challenge, and the GitHub search API was blocked from this session.
- The bodies of Bilibili videos, including "用完一个月 mimo Token Plan，可以使用多少Token？" ([BV1w1T36oEXg](https://www.bilibili.com/video/BV1w1T36oEXg/)), could not be read.

The first full V2.6 billing month only closed around 2026-10-22, so a qualifying report may surface soon after this cut-off.

## Conclusion

The search for a measured MiMo multiple is not mainly limited by missing data. The structure of the product makes a large multiple impossible. Xiaomi priced its Credit at exact parity with its own API, so the plan is a prepaid API wallet with a 5–24% bonus, plus up to 25% more for night use. It is not a subsidised allowance of the Anthropic or OpenAI kind. A measured MiMo figure can only fall between zero and that ceiling. In-window evidence shows the plan's main risk for a buyer is under-use. Light users realise a few percent of the fee, while heavy agent users run into the monthly cutoff within days. The plan's real advantages over pay-as-you-go are the absence of 5-hour or weekly caps and the renewal credit for unused quota, not value per yuan.

For ValueRank, the honest record today is "Plan route: value multiple not identified by end-user measurement; provider-claimed full-utilisation ceiling 0.96–1.24× (peak, monthly), labelled as a provider claim." Under O3 the Plan basis uses the multiple at full utilisation. Using this ceiling would substitute a provider claim for a measurement, so it needs an explicit owner decision rather than silent adoption. Flash should carry no plan multiple at all. The next refresh should target the threads above for end-of-cycle follow-ups. Rows 2 and 3 are partial windows whose owners could close them, and row 1's author could name a tier. Reddit after 2026-10-13 and Bilibili's month-long test also remain to be checked.

## Source index

Official (fees, rate cards, provider claims): [MiMo Token Plan, en-US](https://mimo.mi.com/docs/en-US/price/token-plan) · [Token Plan, zh-CN](https://mimo.mi.com/docs/zh-CN/price/token-plan) · [Individual Subscription, en-US](https://mimo.mi.com/docs/en-US/tokenplan/Token%20Plan/subscription) · [Individual Subscription, zh-CN](https://mimo.mi.com/docs/zh-CN/tokenplan/Token%20Plan/subscription) · [Pay-As-You-Go, en-US](https://mimo.mi.com/docs/en-US/price/pay-as-you-go) · [Pay-As-You-Go, zh-CN](https://mimo.mi.com/docs/zh-CN/price/pay-as-you-go) · [MiMo-V2.6 news](https://mimo.mi.com/docs/en-US/news/latest/v2-6) · [Model updates](https://mimo.mi.com/docs/en-US/updates/model) · [V2.5 price update](https://mimo.mi.com/docs/en-US/news/latest/v2.5-price-update) · [Token Plan launch news](https://mimo.mi.com/docs/en-US/news/latest/token-plan-release) · [MiMo Desktop pricing](https://mimo.xiaomimimo.com/pricing/) · [Xiaomi MiMo on X](https://x.com/XiaomiMiMo/status/2039918061025972358)

Resellers and third parties: [OpenRouter V2.6-Pro](https://openrouter.ai/xiaomi/mimo-v2.6-pro) · [OpenRouter V2.6-Flash](https://openrouter.ai/xiaomi/mimo-v2.6-flash) · [OpenCode Go docs](https://opencode.ai/docs/go/) · [Kingy.ai](https://kingy.ai/blog/mimo-v2-6-pro-free-access-pricing-setup/) · [codingplan.org](https://codingplan.org/plans/xiaomi) · [coding-plan.org](https://coding-plan.org/plans/xiaomi) · [awesome-coding-plan](https://github.com/mahonzhan/awesome-coding-plan) · [linux.do t/2254166](https://linux.do/t/topic/2254166)

End-user reports, in window: [openai/codex#53752](https://github.com/openai/codex/issues/53752) · [OmniRoute#15753](https://github.com/diegosouzapw/OmniRoute/issues/15753) · [V2EX t/1243834](https://www.v2ex.com/t/1243834) · [V2EX t/1243835](https://www.v2ex.com/t/1243835) · [r/opencode 1wphykw](https://www.reddit.com/r/opencode/comments/1wphykw/i_tried_xiaomi_mimo_token_plan_and_i_really_dont/) · [r/opencode 1wmoiaw](https://www.reddit.com/r/opencode/comments/1wmoiaw/mimo_v_26_pro_and_flash_released/pb9av31/) · [r/opencode 1wn27ra](https://www.reddit.com/r/opencode/comments/1wn27ra/mimo_26_flash_vs_pro_latency_mimo_token_plan/pbc2wax/) · [r/opencodeCLI 1wughtd](https://www.reddit.com/r/opencodeCLI/comments/1wughtd/is_it_the_same_on_opencode_too_mimo_v26_pro/pdan6uq/)

End-user reports, older: [r/hermesagent 1v39jq6](https://www.reddit.com/r/hermesagent/comments/1v39jq6/need_help_picking_a_model/oz1cp00/) · [r/openclaw 1txo5cu](https://www.reddit.com/r/openclaw/comments/1txo5cu/which_ai_models_are_cheap_and_worth_it/oq10saf/) · [r/hermesagent 1uclfcf](https://www.reddit.com/r/hermesagent/comments/1uclfcf/hermes_agent_manifest_llm_router/) · [r/MiniMax_AI 1ty0anz](https://www.reddit.com/r/MiniMax_AI/comments/1ty0anz/trying_to_be_patient_but_also_anyone_switch_to/oqav57v/) · [r/LocalLLM 1u9gohq](https://www.reddit.com/r/LocalLLM/comments/1u9gohq/open_source_is_starting_to_beat_frontier_on/osrglb1/) · [linux.do t/2258823](https://linux.do/t/topic/2258823) · [linux.do t/2412590](https://linux.do/t/topic/2412590) · [r/openclaw 1sp179n](https://www.reddit.com/r/openclaw/comments/1sp179n/mimo_v2_vs_opus_46/oh1f7qn/) · [V2EX t/1209234](https://www.v2ex.com/t/1209234) · [Bilibili BV1w1T36oEXg](https://www.bilibili.com/video/BV1w1T36oEXg/)
