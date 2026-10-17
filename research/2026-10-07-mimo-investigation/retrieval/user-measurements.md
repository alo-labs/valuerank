# MiMo V2.6 user measurement retrieval — 2026-10-07

Contract: Retrieve actual end-user API-priced usage measurements for Xiaomi Token Plan after the launch of MiMo-V2.6-Pro and MiMo-V2.6-Flash. Exact variants, user tier, fee, report date and measurement window are required. Provider quotas and theoretical full-quota conversions cannot supply the numerator. This agent owns retrieval only; parent orchestrates Silver Bullet Ultradeep phases and critique cycles.

## Launch and eligibility

Direct built-in browser DOM inspection of https://mimo.xiaomi.com/mimo-v2-6 returned the publication date **September 22nd, 2026** and explicit availability of both models that day. The candidate interval is therefore September 22–October 7, 2026, inside the preceding-month September 7–October 7 requirement. A September 22 report is only conditionally eligible: no precise launch time was published in the observed announcement, so same-day measurement cannot yet be proven to occur after launch.

Official API rates per million tokens on the announcement: Flash cache hit $0.0028, miss $0.14, output $0.28; Pro cache hit $0.0036, miss $0.435, output $0.87. These establish API pricing only.

## Primary Reddit source: empirically calibrated quota conversion

Source: https://www.reddit.com/r/opencode/comments/1wn27ra/mimo_26_flash_vs_pro_latency_mimo_token_plan/

Author **ConsiderationNo9952**, post datetime observed from DOM: **2026-09-22T06:58:33.188Z**. User describes probe results as measuring against the Token Plan dashboard and OpenCode session metrics. Exact tested variants are `mimo-v2.6-flash` (reasoning default/off) and `mimo-v2.6-pro` (reasoning default). Follow-up https://www.reddit.com/r/opencode/comments/1wn27ra/comment/pbc2wax/ at **2026-09-22T09:52:30.017Z** confirms deduction inference from dashboard before/after and OpenCode token reporting, with uncertainty.

User inferred credits/token (cache hit, miss, output plus reasoning): Flash **2, 100, 200**; Pro **2.5, 300, 600**. The post subsequently links official documentation as agreeing with these inferred ratios. User explicitly excludes the off-peak discount from their API-value table.

| Tier | Credits quota quoted by user | Monthly fee quoted by user | Annual monthly equivalent quoted by user | Flash API value quoted by user | Pro API value quoted by user |
|---|---:|---:|---:|---:|---:|
| Lite | 4.1B | $6 | $5.28 | $5.74 | $5.95 |
| Standard | 11B | $16 | $14.08 | $15.40 | $15.95 |
| Pro | 38B | $50 | $44 | $53.20 | $55.10 |
| Max | 82B | $100 | $88 | $114.80 | $118.90 |

**Disposition:** useful direct user evidence of measured credit conversion, but **ineligible as an actual allowance-value numerator** under the project policy. The API-value amounts are full-quota conversions for all tiers; the author does not identify their purchased tier, publish probe token totals or API-priced consumed amount, or report exhaustion of any quota. A derived multiple would describe an empirically calibrated theoretical quota conversion, not observed subscription consumption. Do not transfer the table into the strict ValueRank actual-use metric.

## Other primary user reports

Source: https://www.reddit.com/r/opencode/comments/1wphykw/i_tried_xiaomi_mimo_token_plan_and_i_really_dont/

Author **AppleHuman8535**, **2026-09-25T00:16:15.290Z**. Reports buying the **$5 Lite** plan, experience equivalent to **$5 worth of credits**, 3–4% of plan consumed per approximately one-hour medium task, 50% of plan left. Praises V2.6 Pro and criticizes Flash; exact consumed-model mix not given. https://www.reddit.com/r/opencode/comments/1wphykw/comment/pbvix6j/ (**2026-09-25T00:20:39.698Z**) explicitly describes the assertion as speculation. https://www.reddit.com/r/opencode/comments/1wphykw/comment/pbvntrq/ (**2026-09-25T00:46:43.763Z**) says usage is only off-peak.

**Disposition:** firsthand plan experience, suggestive approximately 1x impression at provider/plan level, but not explicitly API-priced actual usage. No raw ledger or API-price calculation, and denominator conflicts with the $6 standard monthly fee quoted elsewhere. Do not publish a measured model-level multiple.

Same thread **singyaeb** comment https://www.reddit.com/r/opencode/comments/1wphykw/comment/pbz73wv/ (**2026-09-25T14:20:35.503Z**) reports a **$14/month annually billed plan** with no surplus/extra credits. Tier and actual API-priced usage absent: qualitative only, excluded.

Same thread **DumbCSundergrad** https://www.reddit.com/r/opencode/comments/1wphykw/comment/pbx0okz/ (**2026-09-25T05:36:49.632Z**) asserts OpenCode Go can deliver $15 from $10 for Pro and $60 for Flash. This is another provider's plan, without personal measurement/window; excluded from Xiaomi Token Plan allowance evidence.

Source: https://www.reddit.com/r/opencode/comments/1wn191t/mimo_26_flash_is_a_beast_and_seems_to_use_very/

Primary post has no numeric token ledger. Visible comments discuss 10x token use versus DeepSeek, loops racking up credits, and OpenCode Go limits. None of the inspected comments specifies Xiaomi Token Plan tier plus API-priced consumed amount. Related-post link exposed the stronger multiplier probe above. Qualitative evidence only; excluded.

## Coverage and limits

Built-in browser only was used. Focused launch query established primary source and Reddit candidates. Focused Reddit query `site:reddit.com "MiMo" "token plan" after:2026-09-22` surfaced the firsthand Lite report, launch thread, Flash efficiency thread, Flash vs GLM thread, and general model discussions. Strongest plan and measurement pages above were directly inspected.

Non-Reddit query `"MiMo" "token plan" "usage" after:2026-09-22 -site:reddit.com` surfaced official docs, price calculators, vendor/news pages and one LinkedIn news/analyst post; visible results did not identify a personal measured allowance source. Chinese query `MiMo 2.6 Token Plan 套餐 实测 after:2026-09-22` surfaced official docs, CSDN model explainer, CC-switch documentation and news. Search AI Overview was excluded as evidence. No eligible personal usage ledger emerged from those visible results.

This is bounded retrieval, not proof that no eligible report exists. At this stage HN, GitHub discussions, V2EX/NodeSeek and app-trackers had not been searched independently; the subsequent combined HN/GitHub query below inspected a GitHub tracker directly. Five distinct queries were completed in total. Separate HN, GitHub-discussion/app, V2EX/NodeSeek and subreddit-specific retrieval remain coverage gaps. One initial Reddit navigation failed with a network change; creating a new IAB tab at the observed candidate URL succeeded. No security warning was bypassed.

## Subsequent GitHub tracker retrieval: partial actual ledger found

Focused query `"MiMo" "token plan" (site:news.ycombinator.com OR site:github.com) after:2026-09-22` surfaced https://github.com/FeiZhuLulu/real-api-pricing, directly inspected. The visible first-page results were GitHub; no HN result was visible. Its README explicitly distinguishes measured usage from standardized quota conversion. Its DECISIONS.md MiMo section dated September 23 links the primary personal measurement file:

https://github.com/FeiZhuLulu/real-api-pricing/blob/main/data/research/mimo-token-plan-panel-round2-2026-09-23.json

This JSON was directly inspected via the rendered GitHub DOM. It reports **maintainer's own recurring monthly Lite account**, exact **mimo-v2.6-pro**, `collectedAt=2026-09-23`, and two personal dashboard screenshots from September 22/23. Day detail is **2026-09-22**:

| Field | Reported actual value |
|---|---:|
| Total tokens | 73,716,343 |
| Cache input | 67,848,448 |
| Fresh input | 4,479,135 |
| Output | 1,388,760 |
| Used credits | 2,190,625,116 |
| Monthly credits | 4,100,000,000 |
| Dashboard percentage | 53.0% |
| Calculated percentage | 53.43% |
| Plan expiry | 2026-10-22 23:59:59 UTC |

API-priced consumed value, calculated from these user-reported actual token categories and independently observed official announcement rates, is:

`(67,848,448 × $0.0036 + 4,479,135 × $0.435 + 1,388,760 × $0.87) / 1,000,000 = $3.4008993378`.

At the **$6 regular monthly Lite fee** (parent must independently confirm official fee), that is **0.5668165563x consumed value / full monthly fee**. It is a single-day partial consumption measurement, **not** a full monthly allowance multiple. The raw ledger can be arithmetically reproduced; screenshots referenced by the reporter are not embedded in the inspected public JSON, so screenshot/account authenticity cannot be independently reproduced here. The evidence filename's collection date is a report date claim; publication commit history still needs independent verification. September 22 launch-time ordering within the day also remains unresolved because the official page exposes a date only.

Full-month extrapolation using the same token mix and credit fraction would be $6.3651636161 or **1.0608606027x** at $6. This is an **inferred projection from partial observed use**, not an actual-use numerator; do not ingest it as the strict measured allowance metric. The JSON's Flash and higher-tier conversions are explicitly extrapolated and lack independent actual-use evidence.

DECISIONS.md says the earlier `measuredMix` adoption decision in this JSON was withdrawn on the same September 23 day, keeping all 32 adopted rows as standardized quota conversions. The raw actual ledger remains usable as a reported observation; the superseded adoption field must not be mistaken for current tracker policy. The decision also identifies a second client sample file, not inspected in this pass, and notes uncertainty about client version.

**Updated result:** one candidate exact-model actual API-priced partial-day observation (Pro / Lite), with fee, report publication and screenshots still requiring parent validation; no measured full-month allowance value and no qualified Flash actual-use numerator in this pass. Retain quota projections and qualitative impressions separately. Do not encode missing observations as a zero multiple.

## Rework handoff and uncompleted retrieval delta

The requested breadth rework could not execute additional searches in this subagent: built-in `createBrowserTab('iab', ...)` returned `Browser is not available: iab`, and the single recovery attempt using the previously observed browser id `4` returned `Browser is not available: 4`. The enabled inventory exposed external Edge extensions only. `open_in_codex` queued a tracker tab to this thread but did not restore callable IAB. Parent confirmed its own IAB remained operational; the retrieval delta was handed back to the parent. No external browser was used. These are tool access observations, not evidence that sources do not exist.

The following are **planned, not executed**, and therefore do not count toward actual query coverage:

1. `site:news.ycombinator.com "MiMo" "token plan" after:2026-09-21` — separate HN search.
2. `site:news.ycombinator.com "MiMo" ("usage" OR "subscription") after:2026-09-21` — HN measurement/tier variant.
3. `site:github.com "mimo-v2.6-pro" ("usage" OR "token plan") after:2026-09-21` — exact Pro ledger/app leads.
4. `site:github.com "mimo-v2.6-flash" ("usage" OR "token plan") after:2026-09-21` — exact Flash ledger/app leads.
5. `site:nodeseek.com "MiMo" ("Token Plan" OR "套餐" OR "实测") after:2026-09-21` — Chinese user plans.
6. `site:v2ex.com "MiMo" ("Token Plan" OR "套餐" OR "实测") after:2026-09-21` — Chinese user plans.
7. `site:reddit.com/r/LocalLLaMA "MiMo" ("token plan" OR "credits" OR "subscription") after:2026-09-21` — subreddit-specific actual-use leads.

Primary-source follow-up leads already observed in browser results/pages:

- Reddit author profile `https://www.reddit.com/user/ConsiderationNo9952/`: inspect comments for their actual purchased tier; this may improve attribution but does not convert full-quota projections into consumed value.
- `https://github.com/FeiZhuLulu/real-api-pricing/blob/main/data/research/mimo-client-sample-round3-2026-09-23.json`: DECISIONS.md reports approximately 35.72M tokens and 95.01% cache; this linked file itself remains uninspected. Exact model, tier, date, amount and client identity must be read before arithmetic or eligibility.
- `https://github.com/FeiZhuLulu/real-api-pricing/commits/main/data/research/mimo-token-plan-panel-round2-2026-09-23.json`: verify public commit timestamp, distinguish it from JSON collection-date assertion, and inspect whether the measured September 22 window has intraday timestamps.
- `https://ai-vendor-price-tracking.all-the.rest/de/mimo`: linked by a user in the Lite thread; inspect methodology and underlying personal measurement sources before retaining any allowance number.

Validation status: arithmetic for the public Pro ledger is reproducible from the quoted token categories; strict post-launch timing, public publication date, account screenshots and denominator mapping remain conditional. Rework acceptance criterion of at least 12 distinct completed focused queries is **not met by this subagent**; parent must append its actual executed query trail. The five completed queries and all existing inspected-source records are preserved.
