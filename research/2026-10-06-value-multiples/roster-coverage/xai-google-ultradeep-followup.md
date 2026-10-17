# xAI and Google usage-value eligibility and search-coverage follow-up

**Audit date:** 2026-10-06 (Australia/Sydney)  
**Measurement window:** 2026-09-06 through 2026-10-06  
**Targets:** Grok 4.6, Grok 4.7, and Gemini 3.8 Flash

## Finding

There are **zero qualifying user-reported API-priced usage measurements** for these targets in the retained community-evidence package plus the direct sources inspected for this follow-up. This is a bounded audit, not an exhaustive claim about all public posts.

Eligibility requires an end-user's actual use in the measurement window, linked to the exact model variant and plan tier, with the usage amount priced at API rates. A subscription meter, quota, provider allowance, theoretical/API-equivalent quota value, or an Artificial Analysis task average is not an observed user API-cost numerator. None of the recent candidate reports supplies both a measured user amount and its API-rate valuation. Plan fees are included below only when the user directly states them; no unstated tier-to-price mapping is inferred.

## Candidate audit

| Direct source and date | User-reported tier / fee | Exact variant and interval | Reported amount and API pricing | Eligibility |
|---|---|---|---|---|
| [Reddit: “Grok 4.7 feels like a huge token sink…”](https://www.reddit.com/r/cursor/comments/1wu9jj0/grok_47_feels_like_a_huge_token_sink_with_barely/), 2026-09-30 16:29:42 UTC | User says “the $200 plan”; product tier and fee period are not named in the post. Subreddit context is Cursor, but it does not establish a specific Cursor tier. | Heavy Grok 4.7 use “this week,” followed by switching to Grok 4.6; earlier use was Grok 4.6 plus Composer 2.5. Mixed-model interval. | User says consumption “skyrocketed” and describes reaching 90% of included limits, then buying On-Demand Usage. No token count, dollar amount for personal use, or API-rate calculation. | Near-miss: current-window use, but no API-priced measurement and not a single exact variant. |
| [Reddit: “Grok 4.7 is about 2.5 times as expensive as 4.6”](https://www.reddit.com/r/cursor/comments/1wmswj9/grok_47_is_about_25_times_as_expensive_as_46/), 2026-09-21 23:23:12 UTC | User says Cursor Ultra; post gives no plan fee. | Same task over two days, Grok 4.6 and 4.7 at xhigh/no Fast. The author reports percent-meter depletion times for each. | Grok 4.7 meter drops of 1% in 34–55 minutes; Grok 4.6 drops of 1% in 101–133 minutes. The “about 2.5x” assertion references Artificial Analysis averages of $8.82 and $3.53 per task, not the author's own token ledger or API-priced spend. No user API cost is calculated. | Near-miss: current-window, model-specific comparative meter observations, but not user usage priced at API rates. |
| [Hacker News comment 49796557](https://news.ycombinator.com/item?id=49796557), 2026-09-22 03:41:28 UTC | SuperGrok; no fee stated. | Commenter says their app use was once or twice a day and the weekly limit was nearly gone at day seven. They speculate about 4.6 and 4.7; neither exact variant is established as the source of the reported meter use. | Approximate weekly meter depletion only; no tokens or API-rate valuation. | Near-miss: interval and tier are discussed, but exact model attribution and API-priced amount are absent. |
| [Hacker News comment 49790170](https://news.ycombinator.com/item?id=49790170), 2026-09-21 17:12:15 UTC | SuperGrok; no fee stated. | No exact model variant or measurement interval given. | “Very generous” usage impression only; no amount, tokens, or API-rate calculation. | Near-miss: no measurable usage amount. |
| [Hacker News comment 49812720](https://news.ycombinator.com/item?id=49812720), 2026-09-23 07:20:40 UTC | SuperGrok; no fee stated. | Grok Build, with no exact Grok variant identified; roughly 20–30 simple coding/code-review prompts before the weekly allowance ran out. | Prompt count and allowance exhaustion; commenter says they did not properly measure burn rate. No token total or API pricing. | Near-miss: observed app-limit event, not an API-priced amount or exact variant. |
| [Hacker News comment 49797006](https://news.ycombinator.com/item?id=49797006), 2026-09-22 05:09:11 UTC | Cursor account from before the acquisition; exact tier and fee not given. | Says high/xhigh Cursor use and mentions Grok 4.6/4.7, without isolating one model's use. | Qualitative claim that paying API rates would produce a higher token drain than some alternatives; no personal amount, token data, or calculation. | Near-miss: exact variants are mentioned but personal API-priced usage is not measured. Newly identified in this follow-up. |
| [Hacker News comment 49793655](https://news.ycombinator.com/item?id=49793655), 2026-09-21 21:23:46 UTC | User says they bought “a month” for $100; product/tier is not specified. | Early impressions of Grok 4.6; interval is one month of access, not a usage-measurement interval. | $100 is a stated access purchase, not a measured API-priced usage amount. No tokens or personal API-rate costing. | Near-miss: current-window purchase and exact model mention, but no measured use valued at API rates. Newly identified in this follow-up. |
| [Reddit: “Super Grok weekly limit”](https://www.reddit.com/r/grok/comments/1wv16o6/super_grok_weekly_limit/), 2026-10-02 (date in retained audit) | SuperGrok; no fee stated. | Exact Grok variant not stated; commenter reports 40–50% of weekly limit remained on Friday. | Meter remainder only; no tokens or API-rate cost. | Near-miss retained from the package; exact variant and API-priced amount absent. |
| [Reddit: “Increase usage limits”](https://www.reddit.com/r/GrokBot/comments/1wu2ax2/increase_usage_limits/), 2026-10-01 (date in retained audit) | The post describes an Ultra plan, but does not state its fee. | Exact model variant not stated; shared weekly pool exhausted in two days. | Time to quota exhaustion only; no tokens or API-rate cost. | Near-miss retained from the package; exact variant and API-priced amount absent. |
| [Hacker News comment 49913755](https://news.ycombinator.com/item?id=49913755), 2026-09-30 20:16:58 UTC | No consumer/API plan tier or fee identified. | Commenter recalls an experience “ten days ago” using Gemini 3.8 Flash with agy; the activity date is approximate, around 2026-09-20. | Qualitative technical task description; no usage amount, token count, or API-rate pricing. | Near-miss: exact variant and recent use are named, but no cost measurement. |
| [Hacker News comment 49913854](https://news.ycombinator.com/item?id=49913854), 2026-09-30 20:23:24 UTC | No tier or fee identified. | Mixed Fable, Opus, and Gemini Flash/agy workflow; no isolated Gemini 3.8 Flash interval. | No measured amount, tokens, or API-rate calculation. | Near-miss: mixed models and no quantitative usage. |
| [Hacker News comment 49915424](https://news.ycombinator.com/item?id=49915424), 2026-09-30 22:42:32 UTC | Says “Pro account”; exact Google plan name and fee are not stated. | Gemini 3.8 Flash with playwright-cli; no defined measurement interval. | Says quota was sufficient; no consumed amount, tokens, or API-rate pricing. | Near-miss: exact variant and broad plan class are stated, but no measurement. Newly identified in this follow-up. |
| [Reddit: “Gemini 3.8 Flash cost and use”](https://www.reddit.com/r/SillyTavernAI/comments/1wneueb/gemini_38_flash_cost_and_use/), shown as 13 days old on retrieval (approximately 2026-09-23) | Commenters discuss NanoGPT subscription versus OpenRouter/Vertex; no single Google consumer plan or fee is tied to a measured user. | Discussion includes `google/gemini-3.8-flash:floor`; provider route is OpenRouter, not a Google consumer subscription. The date shown was relative, not an exact timestamp captured in this audit. | One comment compares a hypothetical $12 allowance with roughly 17 million input tokens, excluding output; another compares credits for role-play. Neither supplies personal measured tokens/API spend. | Near-miss: model route appears exact, but evidence is tariff arithmetic or qualitative credit comparison, not a user measurement matched to plan tier. |

### Historical / out-of-window leads

- [Reddit: Gemini 3.8 Flash is awesome as the main agent](https://www.reddit.com/r/hermesagent/comments/1w5jj6w/gemini_38_flash_is_awesome_as_the_main_agent/) was posted 2026-09-02 18:57:03 UTC, before the window. The author says they used free Google AI Studio credits; no measured API-priced amount is reported.
- [Comment in that Reddit thread](https://www.reddit.com/r/hermesagent/comments/1w5jj6w/comment/p7l7llg/) is dated 2026-09-03 14:55:08 UTC, also before the window. It says three Hermes interactions cost €2 in API fees. The exact model variant, API model ID, subscription tier/fee, and calculation are not established in that comment. Even if treated as Gemini 3.8 Flash, it is out of window and cannot qualify for this report.
- [Cursor quota post](https://www.reddit.com/r/cursor/comments/1vxcvlx/cursor_ultras_new_824_usage_limits_500_for/) was posted 2026-08-24 19:30:04 UTC, before the window. The author says Cursor Ultra costs $200/month and reports purported monthly usage values for Cursor/Grok 4.6 and other models. These are allowance/quota-equivalent claims, not actual user consumption priced at API rates; Composer is mixed in and Grok 4.6 is not isolated.
- The retained package also has Gemini app-limit anecdotes from [2026-09-13](https://www.reddit.com/r/GeminiAI/comments/1wfhxlh/have_the_limits_lowered_yet_again/) and [2026-09-09](https://www.reddit.com/r/GeminiAI/comments/1wb5d55/what_is_up_with_the_limits_all_of_a_sudden/). They involve mixed consumer-app models or image-generation limits, not measured Gemini 3.8 Flash API-priced use.

## xAI Hacker News date and permalink reconciliation

Direct Hacker News pages distinguish the Grok 4.7 story root, [49788838](https://news.ycombinator.com/item?id=49788838) (2026-09-21 15:50:15 UTC), from its separate comment permalinks. The direct comment pages inspected resolve as follows: 49790170 is 2026-09-21 17:12:15 UTC; 49793655 is 2026-09-21 21:23:46 UTC; 49796557 is 2026-09-22 03:41:28 UTC; 49797006 is 2026-09-22 05:09:11 UTC; and 49812720 is 2026-09-23 07:20:40 UTC. Thus, citations to the root must not be substituted for these comment links. The retained community audit's previously approximate or missing dates for 49796557 and 49790170 are resolved by these direct timestamps. No direct-source ID/content mismatch was found in the links above.

## Search coverage and remaining gaps

### Retained package coverage

- The retained `community-followup-search-log.md` records broad Reddit queries for `Grok "API cost" allowance` and `Gemini "API cost" subscription allowance`. They do not target Grok 4.6, Grok 4.7, or Gemini 3.8 Flash specifically.
- The retained `query_log.jsonl` entries Q03 and Q04 cover first-party xAI and Google plan/API information; they are not community-user measurement searches.
- The retained `model-coverage.csv` identifies only provider-level xAI Reddit/HN reports, with no exact Grok 4.6/4.7 query/result log or documented exact-variant no-hit. Its Google row has qualitative HN/app evidence but no exact-model query/result coverage for Gemini 3.8 Flash.
- The retained community audit listed the SuperGrok weekly-limit and Ultra exhaustion Reddit posts, HN comments 49796557 and 49790170, HN 49913755, and mixed Gemini app-limit reports. Direct inspection adds xAI HN comments 49797006, 49793655, and 49812720, plus Google HN comment 49913854 and 49915424. These additions remain ineligible for the reasons above.

### Targeted in-app browser searches performed for this follow-up

The five Google-search queries were run in the Codex built-in IAB on 2026-10-06; relevant Reddit/HN source pages were then opened directly in the same browser:

1. `site:reddit.com/r/cursor "Grok 4.7" API tokens usage price`
2. `"Grok 4.6" "API cost" user usage Cursor tokens Reddit`
3. `"Gemini 3.8 Flash" usage "API" cost user Reddit`
4. `site:reddit.com/r/SillyTavernAI "Gemini 3.8 Flash cost and use"`
5. `site:reddit.com "Grok 4.7" ("API cost" OR "API price" OR tokens) plan after:2026-09-06`

The xAI searches surfaced the 4.7 meter-comparison discussion and [a Cursor discussion where a commenter reports 1.3–1.5B tokens/month on an unnamed $200 plan](https://www.reddit.com/r/cursor/comments/1wpd3mm/i_hate_to_admit_it_but_grok_sucks/). The latter gives no model/token breakdown or API-priced amount and does not attribute the use to Grok 4.7. The Gemini query surfaced consumer-app discussions; the exact SillyTavernAI thread above provided route/tariff comparisons but not a measured user case. Search-result snippets and generated summaries were not treated as source evidence. These searches do not constitute a no-hit proof: remaining gaps include exact-variant searches on Hacker News and other relevant communities, additional query formulations around invoices/token ledgers/paid API usage, and a wider page/result audit for both Google and xAI.

## First-party plan and API sources

These sources establish plan/API context only; they cannot supply the missing user-measured numerator:

- xAI plan page: [xAI pricing](https://x.ai/pricing). The retained package notes consumer plan names and mentions Grok 4.6, not a user-specific fee or usage measurement.
- xAI allowance context: [Grok FAQ](https://docs.x.ai/grok/faq). The retained evidence describes a flexible shared weekly pool rather than a model-specific user amount.
- xAI API rate card: [xAI developer pricing](https://docs.x.ai/developers/pricing), including API prices for Grok 4.6/4.7.
- Google subscription context: [Gemini subscriptions](https://gemini.google/subscriptions/) and [Gemini Apps usage limits](https://support.google.com/gemini/answer/16275805). App limits are not API usage amounts.
- Google API evidence: [Gemini API pricing](https://ai.google.dev/gemini-api/docs/pricing) and [model catalog](https://ai.google.dev/gemini-api/docs/models), which distinguish the API model ID `gemini-3.8-flash` from consumer Gemini app model naming.

## Method limitation

The requested Silver Bullet Deep Research Ultradeep skill file at `/Users/shafqat/projects/silver-bullet/repo/skills/silver-deep-research/SKILL.md` could not be read through the active LeanCTX allowlist because it is outside this task's configured ValueRank root. A direct read attempt was blocked; I did not bypass the block or use a disallowed browser/HTTP path. This follow-up therefore uses the available local evidence package and the permitted IAB searches, but cannot attest to full compliance with the skill's detailed Ultradeep procedure.
