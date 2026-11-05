# English-language end-user reports of actual usage on Xiaomi MiMo Token Plans (MiMo-V2.6-Pro / V2.6-Flash), as of 2026-10-23

Researcher notes, compiled 2026-10-23. Scope: actual subscriber-reported usage on MiMo Token Plans that could support a value multiple (API-priced value of usage / plan fee). Provider quotas and marketing are kept separate and are not treated as measurements.

Provenance note for Reddit items: reddit.com could not be read directly. Its search JSON returned HTTP 403 and WebFetch refuses old.reddit.com. Every Reddit item below was retrieved from the Pullpush Reddit archive (`api.pullpush.io`). The text and UTC timestamp are the archived copy, and the permalink is the one the archive gives. I did not check live whether a comment has since been edited or deleted. The archive results I received end at 2026-10-13 01:38 UTC, so Reddit from 2026-10-13 to 2026-10-23 is effectively unsearched (see Gaps).

## Which subscribers report concrete usage on a MiMo plan (tokens/credits/requests, limits hit, own API-priced estimates), with tier, price, date, window, model, split and link?

### Takeaway
No in-window English report (2026-09-22 to 2026-10-23) gives a complete billing-window measurement for MiMo-V2.6-Pro or V2.6-Flash: no full-month token ledger, no input/output/cached split, and no measured API-priced total. The window has four usable fragments, all V2.6-Pro and none V2.6-Flash:
- a Max-plan dashboard reading of 55.0M of 82B credits after one morning (posted 2026-09-21 22:44 UTC, about an hour before the window opens);
- a Lite user at 50% of quota, at 3–4% per one-hour task;
- the same Lite user's own estimate that the plan "gives you $5 worth of credits" (about 1x, which he labels speculation);
- one user who checked the dashboard credit change against OpenCode's token counts and found the plan's value about equal to pay-as-you-go API pricing.

Fuller ledgers exist only for the older MiMo-V2.5 generation (June–July 2026), and V2.5 cannot be transferred to V2.6.

### Cited Findings

**A. In-window or at-window reports (V2.6 era; V2.6 released 2026-09-21)**

- **A1. TheVoyant (r/opencode), 2026-09-21 22:44 UTC, about 1h15m before the 2026-09-22 window start.** [Link](https://www.reddit.com/r/opencode/comments/1wmoiaw/mimo_v_26_pro_and_flash_released/pb9av31/)
  - Tier and price: Max, $100/month. He says he got it "like 25% off, nothing crazy", so the fee actually paid was about $75, but the exact amount is not stated ([source](https://www.reddit.com/r/opencode/comments/1wmoiaw/mimo_v_26_pro_and_flash_released/pb9irrl/)).
  - Dashboard quote: "So far this morning, I'm on my third task: 55,026,944 / 82,000,000,000 Used 0.0%".
  - Earlier statement: "I've never used a full monthly amount on the $100 plan".
  - Model: MiMo-V2.6-Pro. The same thread and his follow-up say "Running Pro" ([link](https://www.reddit.com/r/opencode/comments/1wmoiaw/mimo_v_26_pro_and_flash_released/pbgka3p/), 2026-09-22 22:48 UTC). The dashboard figure itself is not explicitly labelled per model, and he partly runs it through Xiaomi's desktop app.
  - Window: one partial morning (three tasks), not a billing window. No token split.
  - Older-era statement in the same thread, with V2.5: "needed heavy work (12 billion tokens a month)" ([link](https://www.reddit.com/r/opencode/comments/1wmoiaw/mimo_v_26_pro_and_flash_released/pb9fpum/)). It is ambiguous whether that means tokens or credits, and it is not V2.6.
- **A2. AppleHuman8535, "I tried Xiaomi Mimo Token Plan and I really don't like it" (r/opencode), 2026-09-25 00:16 UTC.** [Link](https://www.reddit.com/r/opencode/comments/1wphykw/i_tried_xiaomi_mimo_token_plan_and_i_really_dont/)
  - Tier and price: "the $5 Lite plan". The list price is $6, so $5 is consistent with the 12% first-purchase discount ($5.28).
  - His own API-priced estimate: "that basically just gives you $5 worth of credits", which implies about 1.0x. Asked about it, he replied "I'm just speculating this isn't official" ([link](https://www.reddit.com/r/opencode/comments/1wphykw/i_tried_xiaomi_mimo_token_plan_and_i_really_dont/pbvix6j/)).
  - Usage: "A single medium sized task (which usually takes about an hour) eats up 3–4% of the entire plan" and "I still have 50% left on my plan". He used only off-peak hours ([link](https://www.reddit.com/r/opencode/comments/1wphykw/i_tried_xiaomi_mimo_token_plan_and_i_really_dont/pbvntrq/)).
  - Model: V2.6-Pro, which he calls "the only working model". He says V2.6-Flash is "absolute trash … can't even use it as a subagent".
  - Window: since purchase; the purchase date is not stated. No token counts and no split.
- **A3. ConsiderationNo9952, "mimo 2.6 flash vs pro latency | mimo token plan credit multipliers" (r/opencode), 2026-09-22 06:58 UTC.** [Link](https://www.reddit.com/r/opencode/comments/1wn27ra/mimo_26_flash_vs_pro_latency_mimo_token_plan/)
  - He posts the credit table with V2.6 API prices: Flash at $0.0028 cache-hit, $0.14 miss and $0.28 out per M tokens, and 2/100/200 credits per token; Pro at $0.0036, $0.435 and $0.87 per M, and 2.5/300/600 credits per token.
  - Asked whether the API comes out cheaper than the Standard plan, he answered: "based on the dashboard before & after and the opencode token reporting it seems that way. however there is additional 20% discount on off peak times so that probably brings the plan back ahead" ([link](https://www.reddit.com/r/opencode/comments/1wn27ra/mimo_26_flash_vs_pro_latency_mimo_token_plan/pbc2wax/)).
  - This is the only user-side check, from a dashboard delta against harness token counts, that credits are charged at the published per-token rates. He gives no numbers, tier or window, and the model mix covers both V2.6-Pro and V2.6-Flash.
- **A4. Other in-window subscribers who report no numbers. None of these qualifies as a measurement.**
  - Tristsin, 2026-09-22: subscribed to the "5 dollar token plan" and hit Singapore-routing latency from the US ([link](https://www.reddit.com/r/opencode/comments/1wn27ra/mimo_26_flash_vs_pro_latency_mimo_token_plan/pbc43ti/)).
  - singyaeb, 2026-09-25: "$14/month plan billing annually", which matches the annual Standard plan ($168.96/12 = $14.08). He found "no more surplus or extra credits" ([link](https://www.reddit.com/r/opencode/comments/1wphykw/i_tried_xiaomi_mimo_token_plan_and_i_really_dont/pbz73wv/)).
  - New_Guidance_191, 2026-09-29: says the $6 plan "is equivalent to around codex/claude's $20 plan, they don't have 5hr limits". This is qualitative and gives no usage ([link](https://www.reddit.com/r/OpenAI/comments/1wt39kd/the_rug_pull_was_real/pcrsy94/)).
  - Ok-Satisfaction-5236, 2026-10-01: about 5 months on the $16 plan. "The amount of usage I got with MiMo 2.5 was fantastic", but "MiMo 2.6 is unusable right now" ([link](https://www.reddit.com/r/opencodeCLI/comments/1wughtd/is_it_the_same_on_opencode_too_mimo_v26_pro/pdan6uq/)).
  - Pablosky-Muertinez, 2026-10-09: testing both the Qwen and Xiaomi plans and says "xiaomi token plan give you more use for the same money" ([link](https://www.reddit.com/r/hermesagent/comments/1x1fs88/qwen_token_plan_vs_mimo_token_plan_for_hermes/petnl0l/)).
  - SwellJoe (Hacker News), 2026-09-23: "I still have a bunch of tokens on my token plan" ([link](https://news.ycombinator.com/item?id=49820225)).
  - zohebnsr, 2026-10-06: commenting on A2, "A single medium size task consuming 3 to 4% usage of a $5 plan is not a bad deal" ([link](https://www.reddit.com/r/opencode/comments/1wphykw/i_tried_xiaomi_mimo_token_plan_and_i_really_dont/peaspmb/)).
- **Excluded from plan evidence.** phillc73 (HN, 2026-10-06) spent $2.85 of a $10 pay-as-you-go top-up on MiMo-2.6, which is not a plan ([link](https://news.ycombinator.com/item?id=49980909)). Kingy.ai's V2.6 OpenCode test (published 2026-09-22) ran Pro through OpenRouter at about $0.03 and Flash on OpenCode Zen free, with no Token Plan used ([link](https://kingy.ai/blog/mimo-v2-6-pro-free-access-pricing-setup/)).

**B. Older reports, outside the one-month window and not V2.6. Listed for context only; V2.5 and earlier must not be transferred to V2.6.**

Same credit regime as V2.6 (from 2026-05-27: Pro 2.5/300/600 credits, base model 2/100/200):
- **ZombieHomster (r/hermesagent), 2026-07-22.** Pro plan, $50/month, MiMo-V2.5 (non-Pro).
  - Window: about 2026-07-01 to 07-20.
  - Quote: "866.88M tokens in total, of which 741.21M were cache hits, 122.82M were cache misses, and 2.84M were output, across 4,820 requests".
  - The provenance is ambiguous: "I compared my usage stats for this model through Perplexity" ([link](https://www.reddit.com/r/hermesagent/comments/1v39jq6/need_help_picking_a_model/oz1cp00/)).
  - This is the only full split found, and it is for V2.5.
- **Wide_Big_6969 (r/LocalLLM), 2026-06-20.** Annual Standard, $168.96/year for 132B credits.
  - "spent more than 300m tokens so far, roughly 3k api requests, about 9.6b mimo credits".
  - Models: mixed MiMo-V2.5-Pro and V2.5 ([link](https://www.reddit.com/r/LocalLLM/comments/1u9gohq/open_source_is_starting_to_beat_frontier_on/osrglb1/)).
- **starwaves1 (r/openclaw), 2026-06-06.** "I've run 346,000,000 tokens through it in the last few days and it used up 75% of a $16 token plan", on MiMo 2.5 ([link](https://www.reddit.com/r/openclaw/comments/1txo5cu/which_ai_models_are_cheap_and_worth_it/oq10saf/)).
- **purize420 (r/MiniMax_AI).**
  - 2026-06-07, Lite 4.1B: "used 94% in less then 1.5h and it was only 40m tokens" ([link](https://www.reddit.com/r/MiniMax_AI/comments/1ty0anz/trying_to_be_patient_but_also_anyone_switch_to/oqav57v/)).
  - 2026-06-02, same user: "used 20% in under 20min" on MiMo-V2.5-Pro ([link](https://www.reddit.com/r/MiniMax_AI/comments/1ttsu4s/a_quick_benchmark_for_m3_vs_mimo_vs_k26/opa39pm/)).
- **elninost0rm (r/neoliberal), 2026-06-06.** About $5 Lite, MiMo 2.5 Pro: "all morning … I'm at 5% usage for the month" ([link](https://www.reddit.com/r/neoliberal/comments/1tya4ju/discussion_thread/oq40px8/)).
- **One-Trainer2235 (r/hermesagent).** Lite, model unstated.
  - 2026-06-22: "it took 2 days to spend all 4 billions credits" ([link](https://www.reddit.com/r/hermesagent/comments/1uclfcf/hermes_agent_manifest_llm_router/)).
  - 2026-07-05: "mimo plan, it hit its limits within 3 days of use" ([link](https://www.reddit.com/r/hermesagent/comments/1uo4de6/minimax_token_plan_on_hermes_agent/)).
- **Veddit5989 (r/DeepSeek), 2026-09-10.** $5 Lite: "used 346k credits out of 4.1 billion monthly credits just for a hi message" ([link](https://www.reddit.com/r/DeepSeek/comments/1wcsaei/deepseek_is_still_very_expensive/p90h8ol/)).
- **Abid Ali Awan (DataCamp tutorial), 2026-05-19.**
  - Lite at about $4.62 on promotion, MiMo-V2.5-Pro via OpenCode: "reached almost 50% of my Lite plan quota in around three hours".
  - He calls it "roughly 10x cheaper than using normal pay-as-you-go API credit in my case". This predates the 2026-05-27 API price cut, so it compares against the old API prices ([link](https://www.datacamp.com/tutorial/vibe-coding-with-xiaomi-mimo-v2-5-pro)).
- **Not a paid subscription.** the-grand-finale (r/LocalLLaMA), 2026-06-20, got a free Pro-plan grant and had about 24B of 38B credits of MiMo-V2.5-Pro left with 4 days to go ([link](https://www.reddit.com/r/LocalLLaMA/comments/1ub3ocm/no_idea_how_to_finish_my_24b_worth_of_xiaomi/)).

Pre-2026-05-27 credit regime (different credit sizes; not comparable):
- **torrso, 2026-04-19.** "$100 plan's 1.6 billion monthly credits in just 11 days … almost completely only using the cheapest MiMo-V2-Omni"; the dashboard read 1,300,000,000/1,600,000,000 ([link](https://www.reddit.com/r/openclaw/comments/1sp179n/mimo_v2_vs_opus_46/oh1f7qn/)).
- **FearlessGround3155, 2026-05-04.** "10 small tasks … already at 12 or so million credits" ([link](https://www.reddit.com/r/opencode/comments/1t37elv/xiaomi_mimo_coding_plan_is_a_absolute/)).
- **look, 2026-05-10.** Standard (200M credits at that time): "about half the cost of per token API prices", a user estimate of about 2x under old pricing ([link](https://www.reddit.com/r/opencodeCLI/comments/1t93pq0/whats_your_ai_coding_setup_in_2026/okzomh8/)).
- **freakynit (HN), 2026-06-11.** Lowest tier, V2.5 Pro. The dashboard bar showed "152 million tokens" while the table showed "3 million tokens, out of which 2.5 million were cached" ([link](https://news.ycombinator.com/item?id=48493358)). The bar is probably credits, but that is my inference.

**C. Provider claims and quota tables. These are not measurements.**
- Xiaomi's Token Plan page (updated 2026-10-21) lists:
  - Monthly tiers: Lite $6 / 4.1B credits, Standard $16 / 11B, Pro $50 / 38B, Max $100 / 82B.
  - Annual tiers: $63.36 / 49.2B, $168.96 / 132B, $528 / 456B, $1,056 / 984B.
  - Credits per token: mimo-v2.6-pro 2.5 (cache hit), 300 (miss), 600 (output); mimo-v2.6-flash 2, 100, 200.
  - Off-peak (Beijing 00:00–08:00): 0.8x.
  - Discounts: 12% off the first purchase and 12% off annual auto-renew.
  - Service suspends when the quota runs out. MiMo-V2.5 and V2.5-Pro were retired on 2026-10-21.
  - Source: [Xiaomi MiMo Token Plan](https://mimo.mi.com/docs/en-US/price/token-plan).
- Xiaomi's launch post on X advertised "No 5-hour limits. No throttling." ([X post](https://x.com/XiaomiMiMo/status/2039918061025972358)).
- The quota has also been described as restricted to programming tools ([official subscription doc](https://mimo.mi.com/docs/en-US/tokenplan/Token%20Plan/subscription)).
- V2.6 API prices: Pro $0.435 in / $0.87 out per M tokens; Flash $0.14 / $0.28 ([OpenRouter thread quote](https://www.reddit.com/r/opencode/comments/1wmoiaw/mimo_v_26_pro_and_flash_released/pb9cnel/); [Kingy.ai](https://kingy.ai/blog/mimo-v2-6-pro-free-access-pricing-setup/)). Cache-hit prices are $0.0036 (Pro) and $0.0028 (Flash) per M ([ConsiderationNo9952 table](https://www.reddit.com/r/opencode/comments/1wn27ra/mimo_26_flash_vs_pro_latency_mimo_token_plan/)).
- Kingy.ai calculates, from the published rates, that Lite is worth about $5.95 and Standard about $15.95 at API prices ([Kingy.ai](https://kingy.ai/blog/mimo-v2-6-pro-free-access-pricing-setup/)). This is a calculation, not a measurement.

### Inferences
- **Credits track API price almost exactly.** This is derived from the provider rate card, not measured.
  - V2.6-Pro: $0.435/300 = $0.00145 per M credits for miss, $0.87/600 = $0.00145 for output, and $0.0036/2.5 ≈ $0.00144 for cache hit. That gives about **$1.45 of API value per 1B credits**.
  - V2.6-Flash: $0.14/100 = $0.28/200 = $0.0028/2, which gives about **$1.40 per 1B credits**.
  - Because of this, any user-reported credit figure converts to API-priced value whatever the input, output or cache split. A dashboard credit reading is therefore enough for the numerator, provided the model is known.
- **Provider-derived ceiling at full use.** This is NOT a measured multiple; label it as derived from quotas.
  - Monthly, peak, all-Pro: Lite 4.1B × $1.45 = $5.95 on $6 (0.99x); Standard about 1.00x; Pro tier $55.1 on $50 (1.10x); Max $118.9 on $100 (1.19x).
  - All-off-peak multiplies these by 1.25.
  - The annual and first-purchase prices raise them by about 1/0.88 (about 1.14x).
  - The plan therefore never exceeds about 1.2–1.7x API value even at full utilisation. That is consistent with the user verdicts in A2 and A3 ("about $5 worth of credits"; API about equal to plan).
- **A1 converted** (my arithmetic; assumes all-Pro, peak): 55,026,944 credits × $1.45/B ≈ **$0.080** of API-priced use for a morning's three tasks on a $100 (about $75 paid) plan. It is not a billing-window measurement, so no multiple can be computed.
- **A2 converted** (my arithmetic; Pro, off-peak 0.8x):
  - 50% of 4.1B = 2.05B credits ≈ $2.97 at peak-equivalent pricing, or about $3.72 of API-priced tokens because off-peak credits buy 1.25x the tokens.
  - That is roughly 0.56–0.70x of a $5.28 fee so far, part-way through the window.
  - Each 1-hour task at 3–4% is about 123–164M credits, or about $0.18–0.30 of API value.
  - These are partial-window figures, not a value multiple.
- **Model matching.** Every in-window fragment is V2.6-Pro, or mixed and unspecified in A3. There is no V2.6-Flash-specific Token Plan usage report; users mostly report rejecting Flash or using it free on OpenCode Zen.
- **Older V2.5 ledgers.** ZombieHomster's V2.5 split, priced at V2.5 rates (assuming V2.5 cache hit $0.0028, miss $0.14 and output $0.28, which I have not verified), is about $20.1 of API value over 20 days. That equals about 14.3B credits, or 38% of the Pro plan's 38B, giving a period value of about 0.40x of the $50 fee. It is V2.5 and outside the window, so it is context only.

### Gaps
- No in-window report gives tokens or credits for a whole billing window, an input/output/cache split, or the user's own API-priced total for V2.6-Pro or V2.6-Flash. No qualifying full value-multiple data point exists in the English sources I could reach.
- Reddit from 2026-10-13 to 2026-10-23 is unsearched:
  - Pullpush results ended at 2026-10-13 01:38 UTC, and Pullpush then rate-limited me: "Rate limit exceeded… does not provide free scraping resources for agents".
  - Arctic Shift (`arctic-shift.photon-reddit.com/api/{posts,comments}/search?subreddit=…`) returned HTTP 500 or 422 for every subreddit tried.
  - reddit.com/search.json returned HTTP 403 for "mimo token plan", "mimo v2.6 plan" and "xiaomi token plan".
  - WebFetch refuses old.reddit.com.
- X/Twitter: xcancel.com/search returned HTTP 451, and web searches surfaced no user tweets with MiMo plan usage.
- GitHub issues and discussions: `gh api search/issues` was blocked ("sessions are bound to their configured repositories"), so the Cline, Roo, Kilo, OpenCode and Crush issue trackers were not searched.
- YouTube: the AICodeKing video "Mimo V2.5 Pro $6 4B Token Plan (Fully Tested)" (via [daily.dev](https://daily.dev/posts/mimo-v2-5-pro-6-4b-token-plan-fully-tested-this-is-actually-crazy--hhkfgnz8z)) is V2.5. I could not read its transcript, and the aggregator page states no measured usage.
- I could not confirm A1's actual fee paid or whether the dashboard figure was all Pro. A2's purchase date, which sets the measurement window, is not stated.
- Searches run:
  - WebSearch: "MiMo token plan usage reddit"; "Xiaomi MiMo-V2.6-Pro coding plan tokens used limit"; "\"MiMo\" \"token plan\" worth it API value"; "site:reddit.com MiMo token plan credits used"; "MiMo V2.6 token plan review used credits Lite Standard month"; "\"token plan\" mimo x.com usage dashboard billion credits"; "\"MiMo\" token plan Max $100 used credits V2.6 Pro x.com OR twitter"; "MiMo V2.6 Pro token plan review blog October 2026 credits consumed".
  - HN Algolia (comments since 2026-01-01): "xiaomi token plan", "mimo token plan", "mimo credits", "mimo lite plan", "mimo standard plan", "mimo subscription", "mimo coding plan", "mimo quota", "mimo 2.6 plan", "mimo billion credits", "mimo tokenplan", "mimo plan".
  - Pullpush (comments and submissions since 2026-01-01; 1,259 MiMo plan-related hits, filtered and read): "mimo token plan", "mimo plan", "xiaomi token plan", "mimo lite", "mimo credits", "mimo subscription", "mimo quota", "mimo standard plan", "mimo max plan", "mimo v2.6 plan", "tokenplan mimo", "mimo billion credits".
  - Full Pullpush threads pulled for 1wphykw, 1wughtd, 1x1fs88, 1x14vzq, 1wmoiaw and 1wn27ra.
  - Fetched DataCamp, Kingy.ai, daily.dev, codingplans.com and Xiaomi's Token Plan page.

## Are there user comparisons of MiMo plan value vs Claude Max, Codex, GLM Coding Plan, Kimi Code, MiniMax plans that include measured MiMo usage?

### Takeaway
In the window, the comparisons are qualitative or calculated from published quotas. None pairs measured MiMo V2.6 plan usage with measured usage on another plan. The only measured-MiMo comparison is older and for V2.5: ZombieHomster priced his V2.5 ledger at other providers' API rates.

### Cited Findings
- TheVoyant, 2026-09-22, on a $100 OpenAI plan: "Astra has failed and reverted three tasks (at 64% usage after on a $100 plan) Opus 5.5 is at 43% usage, maxing out the 5 hour mark". MiMo Pro completed the same tasks, but he gives no MiMo usage figure beyond A1 ([link](https://www.reddit.com/r/opencode/comments/1wmoiaw/mimo_v_26_pro_and_flash_released/pbgka3p/)).
- New_Guidance_191, 2026-09-29: the $6 MiMo plan "is equivalent to around codex/claude's $20 plan". This is qualitative ([link](https://www.reddit.com/r/OpenAI/comments/1wt39kd/the_rug_pull_was_real/pcrsy94/)).
- DumbCSundergrad, 2026-09-25: "at least with OpenCode Go you can get $15 out of $10 with 2.6 Pro and even $60 with Flash". These are OpenCode Go's stated allowances, not a measurement ([link](https://www.reddit.com/r/opencode/comments/1wphykw/i_tried_xiaomi_mimo_token_plan_and_i_really_dont/pbx0okz/)).
- archerallstars, 2026-09-24: "MiMo is cheap upfront, API. But there's no subsidy in the Token plan … Only MiniMax plans beat Grok in the pricing". This is an opinion ([link](https://www.reddit.com/r/opencodeCLI/comments/1wopbtv/what_muse_spark_14_contributor_is_already_here/pbqjfwn/)).
- asenna987, 2026-09-21: "In my very rough calculations, Token plan is not giving much discount over just paying for the tokens through the API" (imgur calculation) ([link](https://www.reddit.com/r/opencode/comments/1wmoiaw/mimo_v_26_pro_and_flash_released/pb9ijtd/)).
- Firm-Club-8334, 2026-09-11, cross-provider subsidy table: Xiaomi MiMo "**Unclear.** $6/$16/$50/$100 buys 4.1B/11B/38B/82B credits; couldn't verify their dollar equivalent"; Z.ai "Estimated ~3.9–7.8×"; the post asks for real usage figures ([link](https://www.reddit.com/r/ZaiGLM/comments/1wdea79/how_much_are_different_providers_subsidising/)).
- look, 2026-09-08: "If you do the math on the credits to tokens, it works out to be the exact same price as PAYG. The sub only saves you money with the off peak 20% … you get 4.8x more per dollar via Opencode" ([link](https://www.reddit.com/r/MiMo_Xiaomi/comments/1wagogb/should_i_use_mimo_25_through_open_code_or_through/p8igh0f/)).
- Quidenzis, 2026-06-27: "the token plan gives you LESS usage for the same price as if you used the PAYG API. It's about 1%". This is calculated ([link](https://www.reddit.com/r/hermesagent/comments/1twzbc6/why_are_people_not_using_mimo_v25/ou7lbhy/)).
- Older measured-MiMo comparison (V2.5): ZombieHomster, 2026-07-22, priced the V2.5 ledger and said "DeepSeek V4 Flash through OpenRouter would cost about 28 times more, Qwen 3.5 Plus 200 times more, and Kimi K2.6 about 500 times more" ([link](https://www.reddit.com/r/hermesagent/comments/1v39jq6/need_help_picking_a_model/oz1cp00/)). These ratios look implausible next to the published prices; the claim is unverified.
- Older calculation comparisons with OpenCode Go (requests per dollar) come from LongjumpingTear5779, 2026-08-07 ([link](https://www.reddit.com/r/DeepSeek/comments/1vheruw/deepseeks_only_major_advantage_was_its_api/p288zxh/)), and Amarsir, 2026-07-29 ([link](https://www.reddit.com/r/opencodeCLI/comments/1v9v594/i_built_a_site_to_compare_fixedprice_ai_coding/p0ke06w/)). Both are calculations from published quotas.

### Inferences
- The user community has broadly converged on the plan giving about 1x API value. Several users reached this from the rate card, and one (A3) from a dashboard check. In-window users say it is weaker value than OpenCode Go's stated allowances for MiMo. Treat this as consensus opinion plus one dashboard check, not a measured multiple.

### Gaps
- No in-window user pairs measured MiMo V2.6 plan consumption with measured Claude Max, Codex, GLM, Kimi or MiniMax consumption on the same workload.

## Are there reports of hitting rate limits / 5-hour windows on MiMo plans with token counts?

### Takeaway
No. Users and Xiaomi agree that the MiMo Token Plan has no 5-hour or weekly windows, only a monthly credit pool that suspends service when it runs out. The "limit hit" reports are monthly-pool exhaustion, all from the older V2/V2.5 era, and none is in the window or on V2.6.

### Cited Findings
- Xiaomi says: "No 5-hour limits. No throttling." ([X post](https://x.com/XiaomiMiMo/status/2039918061025972358)). The current page says that when the quota runs out, "the system will suspend the service" ([Xiaomi](https://mimo.mi.com/docs/en-US/price/token-plan)). Both are provider claims.
- Users agree: "they don't have 5hr limits" (New_Guidance_191, 2026-09-29, [link](https://www.reddit.com/r/OpenAI/comments/1wt39kd/the_rug_pull_was_real/pcrsy94/)); "Xiaomi doesn't have the separate 5h/weekly limits, you just burn through your monthly credit pool" (LongjumpingTear5779, 2026-08-07, [link](https://www.reddit.com/r/DeepSeek/comments/1vheruw/deepseeks_only_major_advantage_was_its_api/p288zxh/)).
- Pool-exhaustion reports, all older:
  - One-Trainer2235: Lite emptied in 2 days (2026-06-22) and "hit its limits within 3 days" (2026-07-05) ([link](https://www.reddit.com/r/hermesagent/comments/1uclfcf/hermes_agent_manifest_llm_router/); [link](https://www.reddit.com/r/hermesagent/comments/1uo4de6/minimax_token_plan_on_hermes_agent/)).
  - purize420: 94% of Lite in under 1.5h, about 40M tokens, V2.5 era, 2026-06-07 ([link](https://www.reddit.com/r/MiniMax_AI/comments/1ty0anz/trying_to_be_patient_but_also_anyone_switch_to/oqav57v/)).
  - torrso: $100 plan, 1.6B credits in 11 days, V2-Omni, 2026-04-19 ([link](https://www.reddit.com/r/openclaw/comments/1sp179n/mimo_v2_vs_opus_46/oh1f7qn/)).
- In-window, A2 reports 3–4% of Lite per one-hour V2.6-Pro task with 50% remaining, and no exhaustion ([link](https://www.reddit.com/r/opencode/comments/1wphykw/i_tried_xiaomi_mimo_token_plan_and_i_really_dont/)).

### Inferences
- Since there are no rolling windows, a value multiple for MiMo depends only on how much of the monthly credit pool the user actually consumes, which is the utilisation share.

### Gaps
- Reddit from 2026-10-13 to 2026-10-23, X, GitHub issues and YouTube transcripts could not be searched (see the first section's Gaps), so in-window exhaustion reports there are unknown.
