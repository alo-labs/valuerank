# MiMo official token plans and pay-as-you-go API rates (MiMo-V2.6-Pro / MiMo-V2.6-Flash), as of 2026-10-23

Observation method: the official Xiaomi MiMo documentation pages were downloaded with curl on 2026-10-23 and their HTML text was extracted locally, so the figures below are read from the page text, not from a summariser. The English (`en-US`) and Chinese (`zh-CN`) versions match on every price and quota. Third-party and reseller pages were read with WebFetch or WebSearch and are labelled as such.

Labelling rule used throughout:
- **FEE / RATE CARD (provider)**: subscription fees and per-token API prices published by Xiaomi. These may serve as denominators or API rates.
- **PROVIDER CLAIM**: Xiaomi's own statements of allowance, quota, "N× usage", "approximately N rounds of tasks" and similar. These may **never** serve as a measured usage numerator under AGENTS.md.
- **RESELLER CLAIM**: allowance or value statements by OpenCode, OpenRouter or similar resellers. Also not a measured numerator.

## 1. Which MiMo Token Plan tiers exist today, at what fees, and which models do they include?

### Takeaway
As of 2026-10-23 the MiMo Token Plan has four individual tiers: Lite at $6 or ¥39 a month, Standard at $16 or ¥99, Pro at $50 or ¥329 and Max at $100 or ¥659. Annual versions cost about 12% less than twelve monthly payments. A per-seat Team edition offers Standard, Pro and Max at the same prices. Every tier covers mimo-v2.6-pro and mimo-v2.6-flash plus the ASR and TTS models. No tier lists the UltraSpeed model. MiMo-V2.5-Pro and MiMo-V2.5 were retired on 2026-10-21 10:00 (UTC+8). Separately, Xiaomi sells a different subscription for the MiMo Desktop app, launched with V2.6 on 2026-09-22, at ¥59, ¥179, ¥599 or ¥1,199 a month.

### Cited Findings
**Token Plan, individual edition (FEE, provider). Pages state "Update Time October 21, 2026" and were observed 2026-10-23.**

| Tier | Monthly fee | Monthly fixed quota (PROVIDER CLAIM) | Annual fee | Annual fixed quota (PROVIDER CLAIM) |
|---|---|---|---|---|
| Lite (individual only) | $6/month, ¥39/month | 4.1 billion Credits | $63.36/year, ¥408/year | 49.2 billion Credits |
| Standard | $16/month, ¥99/month | 11 billion Credits | $168.96/year, ¥1044/year | 132 billion Credits |
| Pro | $50/month, ¥329/month | 38 billion Credits | $528.00/year, ¥3468/year | 456 billion Credits |
| Max | $100/month, ¥659/month | 82 billion Credits | $1,056.00/year, ¥6,948/year | 984 billion Credits |

Sources: [MiMo docs, Pricing › Token Plan (en-US)](https://mimo.mi.com/docs/en-US/price/token-plan); [MiMo docs, 价格 › Token Plan (zh-CN)](https://mimo.mi.com/docs/zh-CN/price/token-plan); [MiMo docs, Token Plan › Individual Subscription](https://mimo.mi.com/docs/en-US/tokenplan/Token%20Plan/subscription).

- **Team edition (FEE, provider):** Standard costs $16 or ¥99 per seat per month, Pro $50 or ¥329, and Max $100 or ¥659. Annual seats cost $168.96 or ¥1,044, $528 or ¥3,468, and $1,056 or ¥6,948. The quota is a "fixed monthly quota per seat" of 11B, 38B or 82B Credits, including on annual billing. There is no Team Lite tier. — [MiMo docs, Token Plan (en-US)](https://mimo.mi.com/docs/en-US/price/token-plan)
- **Models covered (provider):** "all plans support the latest flagship models mimo-v2.6-pro, mimo-v2.6-flash, as well as ASR and TTS models." The subscription page lists six models: "mimo-v2.6-pro, mimo-v2.6-flash, mimo-v2.5-asr, mimo-v2.5-tts-voiceclone, mimo-v2.5-tts-voicedesign, mimo-v2.5-tts". mimo-v2.6-pro-ultraspeed has no Token Plan credit rate, so it is not included. — [Token Plan (en-US)](https://mimo.mi.com/docs/en-US/price/token-plan); [Individual Subscription](https://mimo.mi.com/docs/en-US/tokenplan/Token%20Plan/subscription)
- **V2.5 retirement (provider):** "Xiaomi MiMo-V2.5-Pro and MiMo-V2.5 were retired on Oct 21, 2026, at 10:00 (UTC+8), and their model IDs no longer work. Please update your integrations to use the V2.6 series." No current tier includes the V2.5 language models. — [Token Plan (en-US)](https://mimo.mi.com/docs/en-US/price/token-plan)
- **Discounts (provider), quoted verbatim:**
  - "First Purchase Discount: Users purchasing the Individual Edition for the first time can enjoy a 12% discount, and each account is only eligible for this discount once; the Team Edition is not eligible for this discount."
  - "Annual Subscription (Auto-renewal): Compared with the monthly auto-renewal plan, both the Individual Plan and Team Plan enjoy a 12% discount for annual auto-renewal, and first-purchase offers are not applicable to annual auto-renewal plans."
  - "Night Discount Rate: During off-peak hours (Beijing Time 00:00–08:00, i.e. UTC 16:00–24:00), the consumption coefficient is 0.8x."
  - The page gives no end date for any of these discounts.
  - Source: [Token Plan (en-US)](https://mimo.mi.com/docs/en-US/price/token-plan)
- **Regional pricing (provider):** The plan pages show a single price per tier in both USD and CNY. Xiaomi's launch post labels them "China: ¥39/month. Overseas: $6/month". — [Xiaomi MiMo Token Plan Brand New Release (news page, Update Time June 29, 2026)](https://mimo.mi.com/docs/en-US/news/latest/token-plan-release)
- **Launch date:** QbitAI reported the first Token Plan launch in April 2026 ([QbitAI, 2026/04](https://www.qbitai.com/2026/04/395210.html)). A reseller-promotion page has the URL date 2026-04-03 ([80aj.com](https://www.80aj.com/2026/04/03/mimo-token-subscription-plan/)). Xiaomi's own launch post is undated in its body and shows "Update Time June 29, 2026" ([news](https://mimo.mi.com/docs/en-US/news/latest/token-plan-release)).
- **Quota exhaustion (provider):** "When the monthly total quota of the package is used up, the system will suspend the service and will not continue to deduct from your bonus or account balance." Individual users can then buy an upgrade package or switch to the per-token API. — [Token Plan (en-US)](https://mimo.mi.com/docs/en-US/price/token-plan)
- **MiMo Claw add-on (provider, CN only):** Launched with the MiMo Claw news post (June 2026, page updated 2026-08-19). It costs "Introductory Offer: ¥14.9 per month; Standard Discount: ¥19.9 per month / ¥233.8 per year", is described as "Limited-Time Subscription Pricing" with no end date, and "Overseas subscriptions are not yet available." It can be added to any Token Plan tier. — [MiMo Claw release news](https://mimo.mi.com/docs/en-US/news/latest/mimoclaw)
- **Separate product, MiMo Desktop membership (FEE, provider):** The V2.6 launch post (Update Time 2026-09-22) says: "the MiMo Desktop Client and membership subscription plan have been launched simultaneously ... Subscribing to the membership grants access to the MiMo-V2.6-Pro and Flash models." — [MiMo-V2.6 news](https://mimo.mi.com/docs/en-US/news/latest/v2-6)
  - The pricing page at [mimo.xiaomimimo.com/pricing/](https://mimo.xiaomimimo.com/pricing/) renders client-side. Its tier data was read from the page's JavaScript bundle on 2026-10-23, which defines these CNY products:

    | Tier | Monthly | Annual |
    |---|---|---|
    | MiMo 入门 (basic) | ¥59 | ¥637.2 |
    | MiMo 进阶 (plus) | ¥179 | ¥1,933.2 |
    | MiMo 高阶 (pro) | ¥599 | ¥6,469.2 |
    | MiMo 尊享 (ultra) | ¥1,199 | ¥12,949.2 |

  - The annual prices equal 12 × monthly × 0.9, matching the bundle's "9 折 / Save 10%" label.
  - The pro and ultra tiers carry "专享 MiMo-V2.6-Pro-UltraSpeed / Exclusive MiMo-V2.6-Pro-UltraSpeed".
  - The bundle also defines global ("gl", Waffo payment) product codes, but no USD prices appear in it.
  - Because these figures come from the bundle rather than the visible page text, they should be re-checked in a browser.

### Inferences
- The Token Plan's annual "12% discount" is exact arithmetic: ¥39 × 12 × 0.872 ≈ ¥408 and $6 × 12 × 0.88 = $63.36. The annual quota is exactly 12 times the monthly quota.
- Third-party aggregators show slightly different annual CNY prices. For example, [codingplan.org](https://codingplan.org/plans/xiaomi) (updated 2026-09-24) gives ¥411.84 for Lite, which is 12 × 39 × 0.88. The official page shows ¥408. Use the official figures.
- For ValueRank, the Token Plan is the route that serves mimo-v2.6-pro and mimo-v2.6-flash in coding tools such as Claude Code, OpenCode and OpenClaw. The Desktop membership is a separate app-bound subscription and may not serve third-party coding agents. The docs say only that members can "also configure your own API Key to use the Client."

### Gaps
- No promotional end dates are published for the first-purchase discount, the night rate or the Claw introductory price.
- USD prices for the MiMo Desktop membership could not be confirmed.
- The exact day the Token Plan launched in April 2026 could not be confirmed from a Xiaomi page.

## 2. How are plan allowances expressed? (PROVIDER CLAIMS)

### Takeaway
Token Plan allowances are a fixed monthly pool of Credits. Credits are deducted per token at model-specific rates, with a 0.8x night coefficient. The current official pages show no 5-hour or weekly window. Xiaomi also gives "approximately N rounds of medium-to-complex tasks" estimates. All of these are provider claims. The Desktop membership instead expresses allowance as relative multiples (1×, 6×, 25×, 60×) against a weekly usage limit.

### Cited Findings
- **Credit conversion (PROVIDER CLAIM, Update Time October 21, 2026):** "Language models deduct Credits quota based on the number of tokens".

  | Model | Input (cache hit) per token | Input (cache miss) per token | Output per token |
  |---|---|---|---|
  | mimo-v2.6-pro | 2.5 Credits | 300 Credits | 600 Credits |
  | mimo-v2.6-flash | 2 Credits | 100 Credits | 200 Credits |
  | mimo-v2.5-asr | 30M Credits per input-audio hour | | |

  "TTS series models are free for a limited time and do not consume package Credits." — [Token Plan (en-US)](https://mimo.mi.com/docs/en-US/price/token-plan); identical in [zh-CN](https://mimo.mi.com/docs/zh-CN/price/token-plan)
- **Xiaomi's worked example (PROVIDER CLAIM):** "if you subscribe to the Lite plan (4.1B Credits) ... After you use 10M mimo-v2.6-pro input tokens (cache miss), this is equivalent to consuming 3000 M Credits, and you will still have 1100M ... Credits remaining." This confirms that the rate is per token, not per million tokens. One version of the page says the remainder is "mimo-v2.5-flash" Credits, a typo; the subscription page says mimo-v2.6-flash. — [Token Plan (en-US)](https://mimo.mi.com/docs/en-US/price/token-plan); [Individual Subscription](https://mimo.mi.com/docs/en-US/tokenplan/Token%20Plan/subscription)
- **Task-count claims (PROVIDER CLAIM):** "Using mimo-v2.6-flash as the baseline, it can execute approximately 200 rounds [Lite] / 1600 rounds [Standard] / 5600 rounds [Pro] / 12800 rounds [Max] of medium-to-complex tasks". The annual plan is "approximately 12 times that of the monthly plan". — [Token Plan (en-US)](https://mimo.mi.com/docs/en-US/price/token-plan)
- **No 5-hour limit (PROVIDER CLAIM, original launch):** The launch post says "No 5-hour token usage limit —— Supports concentrated token consumption". The current pages list only "Fixed Monthly Quota" or "Annual Fixed Quota" and mention no 5-hour or weekly window. — [Token Plan launch news](https://mimo.mi.com/docs/en-US/news/latest/token-plan-release); [Token Plan (en-US)](https://mimo.mi.com/docs/en-US/price/token-plan)
  - The third party [codingplan.org](https://codingplan.org/plans/xiaomi) states "无五小时和周限额" (no 5-hour or weekly limits).
- **Desktop membership allowance (PROVIDER CLAIM, from the pricing-page JS bundle observed 2026-10-23):**
  - Tiers are labelled "1× usage quota", "6× usage quota", "25× usage quota" and "60× usage quota".
  - The billing UI shows "Weekly usage limit", "{percent}% left" and "Resets in ~{days} day(s)".
  - No token or credit figures are given. — [MiMo Desktop pricing](https://mimo.xiaomimimo.com/pricing/)

### Inferences
- The Credit unit is pegged exactly to Xiaomi's domestic real-time pay-as-you-go rate card: 1 Credit per token equals ¥0.01 per million tokens. Every entry matches:
  - Pro: 2.5 / 300 / 600 Credits correspond to ¥0.025 / ¥3 / ¥6 per million tokens.
  - Flash: 2 / 100 / 200 Credits correspond to ¥0.02 / ¥1 / ¥2 per million tokens.
  - So 100M Credits equals ¥1 of domestic API list-price usage, whatever the cache or input/output mix. (Derived from the two official pages in sections 2 and 3.)
- Because the Credit pool is a provider-published allowance, any API-equivalent value derived from it is a provider claim. It cannot be the value-multiple numerator under AGENTS.md. See section 4 for the arithmetic, which is for information only.

### Gaps
- Xiaomi publishes no token ledger or definition of a "medium-to-complex task round". The task-count claims cannot be reproduced.
- The Desktop membership's "1×" base is not defined in tokens, Credits or currency.

## 3. Xiaomi pay-as-you-go API rates for MiMo-V2.6-Pro and MiMo-V2.6-Flash

### Takeaway
Xiaomi publishes separate domestic (CNY) and overseas (USD) rate cards, both updated 2026-10-21. MiMo-V2.6-Pro costs ¥3 or $0.435 for cache-miss input, ¥0.025 or $0.0036 for cache-hit input and ¥6 or $0.87 for output, per million tokens. MiMo-V2.6-Flash costs ¥1 or $0.14, ¥0.02 or $0.0028, and ¥2 or $0.28. Batch API is half price, cache writes are free for a limited time, and there are no context-length tiers. OpenRouter lists identical USD prices.

### Cited Findings
**Real-time API (RATE CARD, provider). "Billing Unit: China：RMB / M tokens; Overseas: dollar / M tokens". Update Time October 21, 2026.**

| Model | Domestic cache-hit input | Domestic cache-miss input | Domestic output | Overseas cache-hit input | Overseas cache-miss input | Overseas output |
|---|---|---|---|---|---|---|
| mimo-v2.6-pro | ¥0.025 | ¥3.00 | ¥6.00 | $0.0036 | $0.435 | $0.87 |
| mimo-v2.6-flash | ¥0.02 | ¥1.00 | ¥2.00 | $0.0028 | $0.14 | $0.28 |
| mimo-v2.6-pro-ultraspeed | ¥0.25 | ¥30.00 | ¥60.00 | $0.036 | $4.35 | $8.7 |

**Batch API (RATE CARD, provider)**

| Model | Domestic cache-hit input | Domestic cache-miss input | Domestic output | Overseas cache-hit input | Overseas cache-miss input | Overseas output |
|---|---|---|---|---|---|---|
| mimo-v2.6-pro | ¥0.0125 | ¥1.50 | ¥3.00 | $0.0018 | $0.2175 | $0.435 |
| mimo-v2.6-flash | ¥0.01 | ¥0.50 | ¥1.00 | $0.0014 | $0.07 | $0.14 |

"Not support batch API: mimo-v2.6-pro-ultraspeed."

Sources: [MiMo docs, Pay-As-You-Go API (en-US)](https://mimo.mi.com/docs/en-US/price/pay-as-you-go); [按量计费 API (zh-CN)](https://mimo.mi.com/docs/zh-CN/price/pay-as-you-go)

- **Billing rules (provider):**
  - "Cache Hit: When the requested prefix content hits the Prompt Cache, it will be billed according to the cached hit price."
  - "Cache Write: Limited-time Free". No end date is given.
  - Web search is billed separately at "¥16 /1000 times" domestic and "$5 /1000 times" overseas.
  - Pay-as-you-go "consumes the account balance based on the actual Token usage, which is not interoperable with the Token Plan package quota."
  - Source: [Pay-As-You-Go (en-US)](https://mimo.mi.com/docs/en-US/price/pay-as-you-go)
- **No context tiers:** The current rate card lists none. The 2026-05-27 V2.5 price reform says new pricing "no longer differentiates based on the input length." — [MiMo-V2.5 Price Adjustment Announcement](https://mimo.mi.com/docs/en-US/news/latest/v2.5-price-update); [IT之家, 2026-05-27](https://www.ithome.com/0/955/636.htm)
- **V2.6 launch pricing (provider, Update Time September 22, 2026):** "The MiMo-V2.6 series adopts the same API pricing as the V2.5 series ... the MiMo-V2.6 series has been launched on the Xiaomi MiMo Open Platform, and the API prices remain unchanged." The model changelog dates the release to 2026-09-22. — [MiMo-V2.6 news](https://mimo.mi.com/docs/en-US/news/latest/v2-6); [Model updates](https://mimo.mi.com/docs/en-US/updates/model)
- **OpenRouter cross-check (reseller API, queried 2026-10-23 via `openrouter.ai/api/v1/models`):**

  | OpenRouter model | Input | Output | Cache read |
  |---|---|---|---|
  | xiaomi/mimo-v2.6-pro | $0.435 | $0.87 | $0.0036 |
  | xiaomi/mimo-v2.6-flash | $0.14 | $0.28 | $0.0028 |
  | xiaomi/mimo-v2.6-pro-ultraspeed | $4.35 | $8.70 | $0.036 |

  - Prices are per million tokens, with a 1.05M context (1,048,576 for UltraSpeed).
  - The V2.6 models' `created` timestamps correspond to 2026-09-22.
  - These match Xiaomi's overseas rate card exactly. — [OpenRouter MiMo-V2.6-Pro](https://openrouter.ai/xiaomi/mimo-v2.6-pro); [OpenRouter MiMo-V2.6-Flash](https://openrouter.ai/xiaomi/mimo-v2.6-flash)
- **Older V2.5 prices (historical; V2.5 retired 2026-10-21):**
  - OpenRouter still lists xiaomi/mimo-v2.5-pro at $0.3045 / $0.609 / cache read $0.0028 and xiaomi/mimo-v2.5 at $0.119 / $0.238 / $0.00255 per million tokens. — [OpenRouter API, observed 2026-10-23](https://openrouter.ai/api/v1/models)
  - A pre-cut aggregator listing dated April 2026 gave MiMo-V2.5-Pro at $1.00 input and $3.00 output per million tokens. This was not verified against Xiaomi. — [pricepertoken.com](https://pricepertoken.com/pricing-page/model/xiaomi-mimo-v2.5-pro)
  - Wallstreetcn and IT之家 report that the 2026-05-27 cut left V2.5-Pro uncached input at ¥3 and output at ¥6 per million tokens. — [wallstreetcn](https://wallstreetcn.com/articles/3769203) (via search summary)
- **Reseller rate card (OpenCode Go, undated page observed 2026-10-23):**

  | Model | Input | Output | Cached read |
  |---|---|---|---|
  | MiMo-V2.6-Pro | $0.435 | $0.87 | $0.003625 |
  | MiMo-V2.6-Flash | $0.14 | $0.28 | $0.0028 |

  Prices are per million tokens. — [OpenCode Go docs](https://opencode.ai/docs/go/)

### Inferences
- The overseas USD card is not a straight currency conversion of the CNY card. The implied rate is $0.145 per ¥1 for Pro (0.435/3) and $0.14 per ¥1 for Flash (0.14/1).
- OpenRouter's V2.5 prices are 30% below what Xiaomi now charges for V2.6, even though Xiaomi says V2.6 kept V2.5 pricing. Either OpenRouter discounted V2.5, or Xiaomi's overseas V2.5 card differed. This is unresolved. It does not affect V2.6, where all sources agree.

### Gaps
- No archived copy of the pay-as-you-go page from before 2026-10-21 could be retrieved. Wayback Machine CDX requests were reset by the network proxy. A Sept–Oct 2026 rate change for V2.6 therefore cannot be ruled out from archives, though no source reports one.
- No end date is given for "Cache Write: Limited-time Free".

## 4. Has Xiaomi or a reseller converted plan allowance into API-equivalent value? (PROVIDER / RESELLER CLAIMS)

### Takeaway
Xiaomi publishes no explicit "N× API value" statement. Its Credit unit, however, is defined at exact parity with its own domestic API list price. So the published quota implies an API-equivalent value at full utilisation of about 1.05–1.24× the monthly CNY fee, or about 0.96–1.19× the USD fee at overseas rates. This is a provider-claim-derived figure, not a measurement. OpenCode Go, a reseller, states monthly dollar usage limits for MiMo-V2.6 models of 1.5× to 6× its plan fee.

### Cited Findings
- **Xiaomi value framing (PROVIDER CLAIM):**
  - The 2026-05-27 reform: "Token Plan billing system optimization, with usage increased to 5-8 times the original" and "Increase the quantity without increasing the price". — [MiMo-V2.5 Price Adjustment Announcement (effective 0:00 2026-05-27 Beijing)](https://mimo.mi.com/docs/en-US/news/latest/v2.5-price-update)
  - The plan page describes "a token conversion mechanism with transparent and controllable quota". — [Token Plan (en-US)](https://mimo.mi.com/docs/en-US/price/token-plan)
  - Xiaomi made no explicit API-dollar comparison on any page reviewed.
- **OpenCode Go (RESELLER CLAIM, undated page observed 2026-10-23):**
  - Go costs $10/month and Go Plus $40/month.
  - "Each model has the following usage limits: 5-hour — 20% of the monthly limit; weekly — 50%; and monthly — 100%."
  - Monthly dollar limits on Go: MiMo-V2.6-Pro $15 and MiMo-V2.6-Flash $60. On Go Plus: MiMo-V2.6-Pro $60 and MiMo-V2.6-Flash $120.
  - Estimated requests per month on Go: Pro 16,300 and Flash 150,400. On Go Plus: Pro 65,200 and Flash 300,800. These are "estimates based on typical Go usage patterns".
  - The page says that for some models "you still get a little more than if you paid the model providers directly."
  - Source: [OpenCode Go docs](https://opencode.ai/docs/go/)
- **OpenRouter:** It is a pay-as-you-go reseller and was not found to publish a MiMo plan-to-API value statement.
- **Community analysis (not provider, not a usage measurement):** Linux.do user Qxuan posted on 2026-05-26 that quotas rose from 0.6亿→41亿 (Lite), 2亿→110亿 (Standard), 7亿→380亿 (Pro) and 16亿→820亿 (Max) Credits. Each call now costs more Credits, so usable volume did not rise 51×. A reply disputed the old per-token rates. — [linux.do topic 2251713](https://linux.do/t/topic/2251713?tl=en)

### Inferences
These ratios are arithmetic on provider-published quota and rate cards. They are for information only and are not admissible as a value-multiple numerator.

**CNY, using 100M Credits = ¥1 domestic list price.** Ratio = API-equivalent value ÷ fee.

| Tier | API-equivalent per month | Monthly ratio | First-purchase ratio | Annual ratio |
|---|---|---|---|---|
| Lite | ¥41 | 1.05× (on ¥39) | 1.19× (on ¥34.32) | 1.21× (¥492 on ¥408) |
| Standard | ¥110 | 1.11× (on ¥99) | | 1.26× (¥1,320 on ¥1,044) |
| Pro | ¥380 | 1.16× (on ¥329) | | 1.31× (¥4,560 on ¥3,468) |
| Max | ¥820 | 1.24× (on ¥659) | | 1.42× (¥9,840 on ¥6,948) |

The 0.8x night coefficient stretches Credits by up to 1.25× more for usage between 00:00 and 08:00 Beijing time.

**USD, at Xiaomi's overseas rates.** 1B Credits ≈ $1.45 of Pro usage or $1.40 of Flash usage.

| Tier | Pro usage per month | Flash usage per month | Ratio on monthly fee |
|---|---|---|---|
| Lite | ≈ $5.95 | ≈ $5.74 | 0.99× / 0.96× (on $6) |
| Standard | ≈ $15.95 | ≈ $15.40 | 1.00× / 0.96× (on $16) |
| Pro | ≈ $55.10 | ≈ $53.20 | 1.10× / 1.06× (on $50) |
| Max | ≈ $118.90 | ≈ $114.80 | 1.19× / 1.15× (on $100) |

- On annual billing, Lite comes to 1.13× / 1.09× and Max to 1.35× / 1.30×.
- These ratios are independent of the cache-hit share, because every token class is priced at the same Credit-to-currency peg.
- OpenCode Go's stated limits imply 1.5× ($15/$10) for MiMo-V2.6-Pro and 6× ($60/$10) for Flash on Go. On Go Plus they imply 1.5× ($60/$40) for Pro and 3× ($120/$40) for Flash. These are reseller claims.

### Gaps
- No end-user-measured, API-priced MiMo Token Plan usage data was within this assignment's scope or found here. A measured numerator, as AGENTS.md requires, must come from user reports.

## 5. Did plans or prices change in September–October 2026?

### Takeaway
Yes, though the API prices themselves did not change:
- On 2026-09-22 Xiaomi released the MiMo-V2.6 series at unchanged V2.5 API prices, added the UltraSpeed tier at 10× Pro prices, and launched the separate MiMo Desktop membership.
- On 2026-10-21 Xiaomi retired MiMo-V2.5-Pro and MiMo-V2.5 and updated both pricing pages. The Token Plan now covers only V2.6 language models.
- The Token Plan fees and Credit quotas appear unchanged since the 2026-05-27 reform.
- When the Team edition, annual billing and night rate were introduced could not be dated precisely. They were present by 2026-09-24 according to a third-party snapshot.

### Cited Findings
- **2026-09-22:** "MiMo-V2.6 Series Release" added mimo-v2.6-pro, mimo-v2.6-flash and mimo-v2.6-pro-ultraspeed. "API prices remain unchanged." The MiMo Desktop membership was "launched simultaneously". — [Model updates](https://mimo.mi.com/docs/en-US/updates/model); [MiMo-V2.6 news](https://mimo.mi.com/docs/en-US/news/latest/v2-6)
- **2026-10-21:** "mimo-v2.5-pro and mimo-v2.5 were officially deprecated at 10:00 (Beijing time) on October 21, 2026". Both pricing pages show "Update Time October 21, 2026". — [Pay-As-You-Go](https://mimo.mi.com/docs/en-US/price/pay-as-you-go); [Token Plan](https://mimo.mi.com/docs/en-US/price/token-plan)
- **Snapshot as of 2026-09-24 (third party):** [codingplan.org](https://codingplan.org/plans/xiaomi), "page last updated 2026-09-24", already lists:
  - V2.6 support
  - the per-seat Team edition
  - the 0.8x night rate
  - the annual 88% price
  - the Claw add-on
  - the same 4.1B, 11B, 38B and 82B monthly Credits
- **Earlier history:**
  - **April 2026:** Launch with 60M, 200M, 700M and 1,600M Credits at the same ¥39, ¥99, ¥329 and ¥659 or $6, $16, $50 and $100 fees. Credit rates were per token by model and context: "mimo-v2-omni 256k Context: 1x"; "mimo-v2-pro 256k Context: 2x"; "mimo-v2-pro 256k~1M Context: 4x". — [Token Plan launch news](https://mimo.mi.com/docs/en-US/news/latest/token-plan-release); [QbitAI](https://www.qbitai.com/2026/04/395210.html)
  - **2026-05-27:** The quota reform described in section 4 ("5-8 times"), with all active quotas reset. — [V2.5 price update](https://mimo.mi.com/docs/en-US/news/latest/v2.5-price-update); [linux.do 2026-05-26](https://linux.do/t/topic/2251713?tl=en)

### Inferences
- The Credit-per-token rates for V2.6-Pro (300/600) and V2.6-Flash (100/200) equal the post-May V2.5-Pro and V2.5 rates reported on linux.do on 2026-05-26. Together with the unchanged-price statement, this suggests the Token Plan value proposition did not change with the V2.6 launch.

### Gaps
- Exact introduction dates for the Team edition, the annual billing option and the night discount were not found on a Xiaomi page.
- The Wayback Machine could not be reached from this environment (connection reset), so no archived snapshot from before October could be compared.
- No Xiaomi X, Weibo or WeChat posts were fetched. The X post cited by a third party as a "pricing claim" ([x.com/XiaomiMiMo/status/2102138559952290106](https://x.com/XiaomiMiMo/status/2102138559952290106)) was not retrieved.
- The MiMo Desktop pricing page could not be read as rendered text. Its prices come from the JavaScript bundle and should be confirmed in a browser.
