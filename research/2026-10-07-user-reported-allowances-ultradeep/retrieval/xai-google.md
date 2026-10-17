# xAI and Google user-reported allowance retrieval

**Retrieved:** 2026-10-07  
**Measurement/report window:** 2026-09-07 through 2026-10-07 inclusive  
**Result:** No qualifying subscription value-multiple numerator found in this pass.

## Scope and qualification

The ranked variants in [`model-coverage.csv`](../../2026-10-06-value-multiples/roster-coverage/model-coverage.csv) are rank 5, xAI **Grok 4.7** (`grok-4.7`) and rank 9, Google DeepMind **Gemini 3.8 Flash** (`gemini-3.8-flash`). The retrieval followed the subscription-allowance policy in [`AGENTS.md`](../../../AGENTS.md): count actual end-user personal usage measured and priced at API rates; preserve exact variant, plan tier/fee, report date, and measurement window. Provider quotas and usage multipliers are not API-priced numerators.

I found reports of subscription quota burn, a standalone API-priced Grok workload, and one secondary estimate of a large Grok subscription allowance. None joins the required personal subscription measurement, API-priced amount, exact ranked variant, tier/fee, report date, and measurement period. **There are zero qualifying datapoints and no value multiple should be calculated from this retrieval.**

Dates shown as “N days ago” on Reddit/Hacker News were captured on 2026-10-07; approximate calendar dates below are inferred from those relative labels and are marked accordingly. The source itself did not show an absolute date for those comments.

## Relevant reports and near-misses

### xAI / Grok 4.7

- **SuperGrok week-of-use report — near-miss.** [Hacker News comment by jmaker](https://news.ycombinator.com/item?id=49812720), displayed as 13 days ago (approximately 2026-09-24). The user says a SuperGrok allowance lasts about 20–30 simple coding or code-review prompts in Grok Build and then is exhausted for the week; they explicitly say they did not properly measure the plan's burn rate. The parent discussion is [“Grok 4.7 (x.ai)”](https://news.ycombinator.com/item?id=49788838), but this comment does not say which Grok variant those prompts used. **Exclude:** no API-rate-priced amount, no stated fee, and no exact-model match; the user also disclaims a proper measurement.

- **SuperGrok daily-use report — near-miss.** [Hacker News comment by artdigital](https://news.ycombinator.com/item?id=49796557), displayed as 14 days ago (approximately 2026-09-23). The user says their SuperGrok usage, including app questions once or twice daily, nearly exhausts a seven-day quota. The comment says Grok 4.6/4.7 were not yet in the app at that time. The user mentions a hypothetical willingness to pay $100/month, but does not state that as the fee for their active SuperGrok tier. **Exclude:** no API-priced usage value and the comment explicitly does not identify Grok 4.7 as the model consumed.

- **SuperHeavy extra-credit report — near-miss.** [Hacker News comment by andreyvit](https://news.ycombinator.com/item?id=49790864), displayed as 14 days ago (approximately 2026-09-23). The user identifies a $300 Grok SuperHeavy subscription and reports spending $50 in extra credits over two hours after running out, with the subscription otherwise covering about a week's work. **Exclude:** the extra-credit spend is not an API-rate-priced estimate of subscription usage; there is no token ledger or exact Grok variant. The two-hour extra-credit episode and roughly one-week subscription-use period are not a model-specific API-dollar measurement window.

- **Standalone API-priced Grok 4.7 workload — near-miss.** [Hacker News comment by jjcm](https://news.ycombinator.com/item?id=49792549), displayed as 14 days ago (approximately 2026-09-23). It reports about 20M cached-read, 1M input, and 100K output tokens for a workload, pricing Grok 4.7 at $12.60. **Exclude:** this is a workload cost comparison, not a subscription allowance report; there is no subscription tier/fee or stated measurement interval. It therefore cannot be treated as a subscription numerator despite having an exact model and API-priced token counts.

- **Secondary ~$12,000 / 40× claim — not an end-user datapoint.** [Hacker News comment by daquisu](https://news.ycombinator.com/item?id=49792007), displayed as 14 days ago (approximately 2026-09-23), claims maximum Grok subscription use equates to around $12,000 at API prices on a $300 plan. In a direct [follow-up](https://news.ycombinator.com/item?id=49794733), the same commenter says they did the research but had never used Grok themselves. **Exclude:** it is a secondary aggregation rather than an end-user's measured personal use. The follow-up disqualifies it under the project evidence policy.

- **Three-month SuperGrok offer — near-miss.** [Reddit post by u/CuChuliannAlter](https://www.reddit.com/r/grok/comments/1whx22f/3_month_offer_is_up_bye_bye_grok/), displayed as 21 days ago (approximately 2026-09-16). The poster says they bought a three-month SuperGrok deal on July 16 and that it had ended. That purchase date and the displayed report date are only about two months apart, so the source's timeline is internally inconsistent. No fee, exact model, or API-priced usage amount is given. **Exclude:** membership duration is not a measured usage window or allowance value.

### Google / Gemini 3.8 Flash

- **Google AI Pro / 3.8 Flash High quota exhaustion — near-miss.** [Reddit post by u/No-Flower-8521](https://www.reddit.com/r/GoogleAntigravityIDE/comments/1wxj4ry/did_gemini_38_flash_quotas_rate_limits_get/), displayed as 3 days ago (approximately 2026-10-04). The user identifies **Google AI Pro**, Gemini 3.8 Flash, and the **High** agent setting, and says that identical workloads had drained the five-hour rolling baseline quota after about one hour over the preceding 24–48 hours. **Exclude:** this is personal, current-window quota-use reporting for the exact model/effort and a named plan, but it supplies no token count or API-priced amount and does not state the plan fee. Quota exhaustion cannot serve as the API-dollar numerator. I opened this lead in the in-app browser after it was supplied by the parent task; the originating search query was not available to this retrieval log.

- **Antigravity quota-to-time report — near-miss.** [Reddit comment by alsaud21](https://www.reddit.com/r/google_antigravity/comments/1ws9ig9/comment/pcs7cbb/) on a September 28 weekly support thread; the comment displayed as 8 days ago (approximately 2026-09-29). The commenter says Gemini's weekly quota is six times its five-hour quota, and that “3.8 high” makes the five-hour limit last about one hour, so the weekly quota lasts six to eight hours. They identify “Pro Tier,” but give no fee. **Exclude:** this is time-to-quota and a quota ratio, not tokens or an API-dollar estimate; the plan/product mapping and fee are unspecified. The reported quota itself cannot be the numerator.

- **Gemini 3.8 medium context-use report — near-miss, effort differs.** [Reddit comment by seedlord](https://www.reddit.com/r/google_antigravity/comments/1ws9ig9/comment/pcn09t3/) on the same support thread, displayed as 9 days ago (approximately 2026-09-28). It says “3.8 med” used about 25% of a weekly Pro-plan limit during a session whose context grew from 100K to 140K. **Exclude:** it reports provider-plan quota consumption rather than API-priced value, gives no fee, and identifies medium rather than the roster's high effort setting.

- **Antigravity/Ultra quota-drain report — near-miss.** [Google AI Developers Forum post by SlaterBBurn](https://discuss.ai.google.dev/t/gemini-3-8-flash-in-antigravity-severe-latency-command-looping-quota-drain-api-503-billing-issues/183550), dated 2026-09-18. The author names Gemini 3.8 Flash and reports quota burnout on high-tier/Ultra usage after command loops across seven sessions in one evening. The post separately says external Gemini API calls returning 503s still registered quota/usage charges, without giving a priced amount. **Exclude:** no measured API-dollar estimate for the subscription allowance, no fee, and the Antigravity allowance and API failures are separate usage paths.

- **Daily-troubleshooting / Pro account report — near-miss.** [Hacker News comment by gcy](https://news.ycombinator.com/item?id=49915424), displayed as 6 days ago (approximately 2026-10-01), says the user uses Gemini 3.8 Flash for daily troubleshooting and has “sufficient quota with pro account.” **Exclude:** no measured amount, API pricing, plan fee, or usage period is stated; the exact paid product/tier is not clear.

## Other searched results excluded by scope or date

- [Reddit's Grok weekly-quota post](https://www.reddit.com/r/grok/comments/1ujd49c/with_weekly_quota_you_get_roughly_4_daily_quotas/) is displayed as about three months old, outside the requested window. It discusses SuperGrok quota ratios and image/video generation, not API-priced text-model usage.
- [Reddit's Grok subscription thread](https://www.reddit.com/r/grok/comments/1vlr46s/its_my_last_day_after_paying_for_a_grok/) is displayed as about two months old, outside the window; its comments do not establish an in-window API-priced Grok 4.7 subscription measurement.
- [Reddit's “Pro Is Still Better” thread](https://www.reddit.com/r/GeminiAI/comments/1wz7i09/pro_is_still_better/) was current (displayed as 16 hours old) but compares model quality and provides no allowance measurement.

## Search log

All searches below were run on 2026-10-07 using Google Search in the Codex built-in in-app browser, opening results there. Reddit was searched first, followed by Hacker News and developer forums. Search-result snippets were used for discovery; the cited result pages/comments above were opened and checked before classification.

| Community | Exact query entered | Outcome |
|---|---|---|
| Reddit | `site:reddit.com/r/grok "Grok 4.7" "SuperGrok" usage API pricing September 2026` | Found the three-month SuperGrok post; no allowance measure. |
| Reddit | `site:reddit.com/r/grok SuperGrok measured usage "API" tokens September 2026` | Found an older quota-ratio post, outside the window. |
| Reddit | `site:reddit.com "Gemini 3.8 Flash" "AI Pro" usage measured September 2026` | Found a September Antigravity weekly-quota discussion and the “3.8 high” / Pro Tier comment. |
| Reddit | `site:reddit.com Gemini "3.8 Flash" "Google AI Ultra" API usage September 2026` | Found current quality discussion, no allowance measurement. |
| Reddit | `site:reddit.com/r/grok "4.7" weekly quota usage September 2026 API` | Found quota complaints, but no qualifying API-priced estimate; one related subscription post was outside the window. |
| Hacker News | `site:news.ycombinator.com Grok 4.7 SuperGrok API usage allowance September 2026` | Found the Grok 4.7 discussion and the near-misses detailed above. |
| Hacker News | `site:news.ycombinator.com "Gemini 3.8 Flash" "AI Pro" quota allowance API September 2026` | Found a current Gemini thread; its Pro-account quota comment has no API-priced amount or measured period. |
| Google AI Developers Forum | `site:discuss.ai.google.dev "Gemini 3.8 Flash" "API" quota subscription September 2026` | Found the September 18 Antigravity quota-drain report; no subscription API-dollar measurement. |
| xAI community | `site:community.x.ai "Grok 4.7" SuperGrok measured API usage September 2026` | Google Search returned no results for this domain/query. |

## Limitation

This is a targeted search pass, not a census of private communities or unindexed posts. It establishes only that the searched public Reddit, Hacker News, Google AI Developers Forum, and indexed xAI community pages produced no source meeting the full ValueRank qualification rule during this retrieval.
