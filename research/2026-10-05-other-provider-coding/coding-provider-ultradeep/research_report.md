# Coding-oriented AI plan allowances: community reports and meter apps

**Evidence window:** 2026-09-05 to 2026-10-05 inclusive. **Retrieved:** 2026-10-05.  
**Purpose:** a provider-focused supplement to ValueRank's ongoing allowance research.

## Report Metadata

| Field | Value |
|---|---|
| Research mode | Ultradeep phase artifact package; phase work recorded manually |
| Subject | Coding-oriented AI subscription allowance apps and user-reported use |
| Evidence period | 2026-09-05 through 2026-10-05, inclusive |
| Source records | 22: 19 direct post/documentation/repository pages and 3 bounded search-outcome records |
| Evidence records | 13 eligible user observations, 1 excluded user estimate, and 6 provider policy observations |
| Exact retained search strings | 47; earlier official-search literals were not preserved |
| Retrieval | Codex built-in `web__run`; direct-source links listed in Bibliography |

The [canonical evidence ledger](evidence.jsonl) carries the machine-readable crosswalk used here: find each `CP-E##` or `CP-P##` label in `report_evidence_id`. Every user-observation row exposes `plan_tier_as_reported` (including the literal `not stated`), `reporter_label`, and `source_id`; follow `source_id` in [canonical sources](sources.jsonl) to the direct source. Provider-policy rows are marked separately and have no subscriber tier.

## Executive Summary

The in-window search found 13 eligible user-reported observations across a small, heterogeneous set of Cursor, Copilot, Kimi Code, OpenCode Go, and Ollama Cloud accounts. The observations do not support a typical burn rate, a cross-plan capacity ranking, or a normalized “hours of coding” estimate. Workloads, model routes, reset windows, and provider meter units differ; some exact subscription tiers were not stated.

I separate four requested measurement types—provider account meters, provider-published quota rules, local usage-log estimates, and API-cost equivalents—and label one additional category, user extrapolation, for a subscriber's projection based on a meter and approximate request count. Official pages explain meter semantics; they do not corroborate a user's reported consumption.

## Introduction

This supplement audits account-meter anecdotes and allowance-monitoring apps for coding-focused providers. It preserves the larger research package's earlier provider findings and does not fold these reports into them as equivalent measurements.

## Main Analysis

## Eligible user reports

### Cursor

- **Reported plan: Cursor Pro.** One author said that by the end of a day their Cursor Models pool was at 100% and Other Models at 23%. They did not identify the task, model route, or billing-cycle start. This is a provider account-meter reading, not a task-normalized allowance estimate. ([Reddit report](https://www.reddit.com/r/cursor/comments/1wa2h7b/is_it_just_me_or_has_my_cursor_credits_been/); CP-E01.) [1]
- **Reported plan: Cursor Ultra.** One author said a Fable 5.1 use on renewal day consumed 5% of their third-party credit pool. Separately, the same author estimated about USD 5–7 in API cost for that event. The 5% is a Cursor account-meter reading; USD 5–7 is an author-reported API-cost equivalent. A reply points to millions of model tokens behind the apparent one-question action, so it is unsafe to interpret that UI action as one API request. ([Reddit report](https://www.reddit.com/r/cursor/comments/1wilw56/cursor-ultra-thirdparty-model-usage-quota-anomaly/); CP-E02/E03.) [2]
- Cursor's [official usage documentation](https://prod.cursor.com/help/models-and-usage/usage-limits) defines separate monthly Cursor Models and Other Models pools and a live Spending page. It clarifies the meter labels but not either user's workload or consumption. (CP-P01.) [3]

### GitHub Copilot

- **Reported plan: not stated.** A commenter said they received 150,000 monthly AI credits and used 24,000 during a project migration. This is a commenter’s provider account-meter report. The thread author separately mentioned an employer-provided Copilot Pro+ plan with 7,000 credits but asked how much work it would support; that question is not measured use and is not assigned to the commenter. ([Reddit thread](https://www.reddit.com/r/GithubCopilot/comments/1wxfp92/copilot_pro_usage_limits/); CP-E04.) [4]
- **Reported plan: not stated.** A different author said two Sonnet 5.5 max-thinking generations consumed the monthly allowance and almost USD 8. They did not identify the Copilot tier or exact billing-cycle interval. This remains a user-reported account-limit and overage observation, not a normalized API cost. ([Reddit report](https://www.reddit.com/r/GithubCopilot/comments/1ww8p8z/cancelled_my_sub_today/); CP-E05.) [5]
- GitHub's [billing documentation](https://docs.github.com/en/billing/concepts/product-billing/github-copilot-billing) says Copilot uses AI credits, prices one credit at USD 0.01, and varies monthly allocations by plan. That is published policy context, not proof of an individual account's tier or usage. (CP-P02.) [6]

### Kimi Code

- **Reported plan: not stated.** One author said the five-hour limit was exhausted within minutes while using the default/basic model on a small coding task. The post does not identify the membership tier; do not infer it from the five-hour window. ([Reddit report](https://www.reddit.com/r/kimi/comments/1wm92oz/kimi_code_consumed_my_entire_5hour_limit_within/); CP-E06.) [7]
- Kimi's [membership documentation](https://www.kimi.com/code/docs/en/kimi-code/membership.html) distinguishes current and legacy plans: rolling five-hour and monthly quota are documented, with weekly quota retained for legacy plans; the Code Console and `/usage` show an account's consumption. These rules cannot identify this author's tier. (CP-P03.) [8]

### OpenCode Go

- **Reported plan: OpenCode Go.** One author said the daily quota reached 100% on the first attempt while monthly usage showed 20%; the author later named GLM 5.3. This is a provider account-meter snapshot. ([Reddit report](https://www.reddit.com/r/opencode/comments/1wk1gol/extremely-low-limits-in-open-code/); CP-E07.) [9]
- **Reported plan: OpenCode Go.** Another author described several days of heavy coding with DeepSeek V4.1 Flash and current-month usage at 12%. The same author said a previous period had reached 100% while coding three to four hours at night with Hermes, but that previous period is not separately date-bounded and is not treated as a second in-window datapoint. ([Reddit report](https://www.reddit.com/r/opencode/comments/1wozjjf/with-deepseek-v41-flash-it-feels-impossible-to/); CP-E08.) [10]
- The [Go plan page](https://dev.opencode.ai/go) publishes estimated request counts per five-hour window and model-specific monthly use values. Those are provider estimates, sensitive to model and promotion, not measured subscriber burn. (CP-P04.) [11]

### Ollama Cloud

- **Reported plan: Ollama Cloud grandfathered Pro plan.** A Sep 10 commenter said they had made 724 DeepSeek V4 Flash requests and used 60% of the weekly allowance with three days left. The same commenter projected exhaustion around 1,200 requests and compared this with a recalled earlier 1,700–2,000 requests per week while leaving roughly 15% unused. The 60% is the provider account meter; the roughly 1,200 figure is a **user extrapolation**, not an observed cap or a verified local-log total. ([Reddit thread and comment](https://www.reddit.com/r/ollama/comments/1waiu6b/confirmed_ollama_cloud_nerfing_usage_limits_on/); CP-E09/E10.) [12]
- **API-cost equivalent from the same commenter, not Ollama subscription consumption.** The user compared direct DeepSeek API use at CNY 70 for 3,695 requests and estimated that USD 20 could buy roughly 1,700 requests per week. This is an author's price comparison; it must not be merged with Ollama's provider meter. (CP-E11; same [Reddit thread](https://www.reddit.com/r/ollama/comments/1waiu6b/confirmed_ollama_cloud_nerfing_usage_limits_on/).) [12]
- **Reported plan: Ollama Pro.** A different commenter said 36.7% of their weekly session allowance was used after two days. The user did not state whether this was a grandfathered subscription or the newer credit plan. This is a provider account-meter report. (CP-E12; same [Reddit thread](https://www.reddit.com/r/ollama/comments/1waiu6b/confirmed_ollama_cloud_nerfing_usage_limits_on/).) [12]
- **Reported plan: Ollama Pro.** That Sep 15 commenter also described local OpenCode counters: over 400 million cache-read tokens, about 75 million input tokens and 380,000 output tokens over roughly two days. These are **local usage-log counters**, not confirmed provider-billed tokens. The commenter wondered whether cache reads affected the weekly session meter; the post does not establish that. (CP-E13; same [Reddit thread](https://www.reddit.com/r/ollama/comments/1waiu6b/confirmed_ollama_cloud_nerfing_usage_limits_on/).) [12]
- A separate Sep 8 original-poster estimate of roughly 50% lower usage capacity is retained as **excluded context**: no plan tier, counter, period, baseline, or account-meter reading was given. **Reported plan: not stated.** It is not part of the 13 eligible observations. (CP-E14.) [12]
- Ollama's [current pricing page](https://ollama.com/pricing) describes monthly token-priced credits for new plans and notes that switching legacy Pro/Max subscriptions to the new plan changes old session/weekly limits. Policy has moved across plan generations, which is another reason to keep the two commenters separate. (CP-P05.) [13]

## Allowance apps and local usage tools

The opened projects mostly expose an individual subscriber's own account or local telemetry:

- [OpenCode Bar](https://github.com/opgginc/opencode-bar) describes a menu-bar dashboard for connected providers, including Kimi, OpenCode Go, Z.ai, and Copilot account usage. Its README is a maintainer capability claim, not a tested result or public aggregate. [14]
- [opencode-quota](https://github.com/whosydd/opencode-quota) describes per-account Go dashboard scraping and Copilot OAuth usage retrieval; no public cohort data is advertised. [15]
- [OpenUsage's Z.ai adapter](https://github.com/robinebers/openusage/blob/main/docs/providers/zai.md) documents user-key access to undocumented Z.ai endpoints. This is a tool maintainer's claim, not provider documentation or independent runtime verification. [16]
- [zai-usage](https://github.com/LogicIncZo/zai-usage) presents a local meter, but its Sep 12 PRO dashboard is explicitly a synthetic `--demo` example; those values are excluded as user evidence. [17]
- [GitHub Copilot Tracker](https://github.com/kanalive/github-copilot-tracker) describes local OpenTelemetry spans with per-request token/model records and estimated costs. Local traces are not provider account history or crowd data. [18]
- Z.ai's [usage stats documentation](https://zcode.z.ai/en/docs/usage-stats) explicitly distinguishes local App Usage logs from remote Coding Plan account quota. This is useful for interpreting the two categories, but no eligible Z.ai/GLM user-consumption report surfaced in the searched results. [19]

## Claims-Evidence Table

| Report-level claim | Evidence | Assessment |
|---|---|---|
| This sample does not support a typical coding-use burn rate. | CP-E01–E14; dates, intervals, reported tiers, and classes are recorded separately. | Supported as a limitation statement; no pooled estimate is calculated. |
| Provider account meters, published quotas, local logs, projections, and API equivalents are distinct measures. | CP-E01/E02/E04–E09/E12; CP-E10; CP-E11; CP-E13; CP-P01–P06. | Supported by the measurement descriptions and policy pages. |
| Tracker projects monitor an account or local log but do not provide public population usage in the inspected READMEs. | CP-S18–S22. | Supported only for the retrieved repository versions and their stated features. |
| Search did not establish an eligible Windsurf, HN, or Z.ai user-reported usage datapoint. | CP-S09–S11 and the corresponding queries in `query_log.jsonl`. | Bounded non-finding; cannot prove no eligible post exists. |

## Counterevidence Register

- The Cursor Ultra poster calls the high-cost interaction a single “question,” while a reply points to millions of tokens behind the UI action; this weakens any inference that one question equals one request. The report therefore keeps the 5% account-meter reading and USD 5–7 API equivalent separate. [2]
- OpenCode Go reports include both daily quota depletion at 20% monthly and 12% current-month use after several days of heavy work. This variation is a reason to avoid labeling either account typical. [9] [10]
- Ollama's documentation describes a change from grandfathered session/weekly limits to newer token credits, while the two user comments do not identify the same plan state. The differing account meters are not treated as a direct contradiction or merged into one quota. [12] [13]
- Tracker repositories show how individual meters and local logs may be collected, but the `zai-usage` example is explicitly synthetic; none of these projects supplies a user cohort that could independently test the anecdotes. [14] [15] [16] [17] [18]

## Synthesis

The eligible sample contains nine provider-account-meter observations, one author extrapolation from an account meter, one local OpenCode usage-log observation, and two API-cost-equivalent observations. The six provider documentation rows are policy context and do not enter those user-report counts. The excluded CP-E14 estimate is not counted in the sample. These class counts are provenance labels only; they are not comparable units.

The most useful finding for allowance-app research is that the available tools usually show a single subscriber's provider meter or local event/token records. The reviewed projects did not provide public cross-user consumption histories. Consequently, they can help a subscriber inspect their own limits, but they do not fill the evidence gap for typical plan capacity.

## Limitations

Targeted searches on Reddit and Hacker News returned no qualifying Windsurf-only account report; a Sep 18 Devin report is a different paid service. HN hits were mainly from June through August, before this evidence window. Searches for Z.ai/GLM Coding Plan found account-meter software and older discussion, but no verifiable individual in-window consumption report. These are bounded search outcomes, not proof those reports do not exist.

All figures are self-reported. No raw provider exports were captured, no tracker was authenticated against an account, and screenshots mentioned in the Cursor discussion were not independently re-read as pixel evidence. The handful of examples is not representative and should not be used to rank plans or predict an individual developer's monthly coding capacity.

## Recommendations

1. When expanding the main ValueRank comparison, keep these records in a separate coding-provider stratum and aggregate only within the same provider meter, plan generation, and usage interval.
2. For future user reports, capture a dated account-meter screenshot or export, named subscription tier, model/provider route, task window, and whether the figures come from local logs or the provider dashboard.
3. Treat account-monitoring apps as a collection aid. To answer population-level allowance questions, collect opt-in, anonymized meter snapshots with a common task and time window; do not combine them with tracker README claims or synthetic demonstrations.
4. Re-run bounded HN, Windsurf, and Z.ai/GLM searches when new eligible dates accumulate, since the current search return is not exhaustive.

## Methodology

Only Codex's built-in `web__run` was used for web search and page opening. The query log contains 47 exact search strings retained from the captured run history; earlier official-document queries whose literals were not preserved are excluded from that count. Search results were screened by actual post/comment date, named plan tier, reported interval, measurement surface, and reporter identity within a thread. Official documentation and tracker repositories were opened to establish published policy and tool capability, not user consumption. Three documented manual critique cycles checked author/tier transfer, measurement conflation, temporal eligibility, and treatment of synthetic or no-hit results.

## Evidence package

Use [`sources.jsonl`](sources.jsonl), [`evidence.jsonl`](evidence.jsonl), [`claims.jsonl`](claims.jsonl), and [`query_log.jsonl`](query_log.jsonl) for machine-readable records. `scope.md`, `triangulation.md`, `critique.md`, and `decision-record.md` preserve the boundaries and review trail.

## Bibliography

[1] Reddit r/cursor (2026-09-07). "Is it just me or has my cursor credits been running out faster". https://www.reddit.com/r/cursor/comments/1wa2h7b/is_it_just_me_or_has_my_cursor_credits_been/
[2] Reddit r/cursor (2026-09-17). "Cursor Ultra Third-Party Model Usage Quota Anomaly". https://www.reddit.com/r/cursor/comments/1wilw56/cursor-ultra-thirdparty-model-usage-quota-anomaly/
[3] Cursor documentation. "Usage and limits". https://prod.cursor.com/help/models-and-usage/usage-limits
[4] Reddit r/GitHubCopilot (2026-10-04). "Copilot Pro+ Usage Limits". https://www.reddit.com/r/GithubCopilot/comments/1wxfp92/copilot_pro_usage_limits/
[5] Reddit r/GitHubCopilot (2026-10-02). "Cancelled my sub today". https://www.reddit.com/r/GithubCopilot/comments/1ww8p8z/cancelled_my_sub_today/
[6] GitHub Docs. "GitHub Copilot billing". https://docs.github.com/en/billing/concepts/product-billing/github-copilot-billing
[7] Reddit r/kimi (2026-09-21). "Kimi Code consumed my entire 5-hour limit within minutes". https://www.reddit.com/r/kimi/comments/1wm92oz/kimi_code_consumed_my_entire_5hour_limit_within/
[8] Kimi Code documentation. "Membership Benefits". https://www.kimi.com/code/docs/en/kimi-code/membership.html
[9] Reddit r/opencode (2026-09-18). "Extremely low limits in open code". https://www.reddit.com/r/opencode/comments/1wk1gol/extremely-low-limits-in-open-code/
[10] Reddit r/opencode (2026-09-24). "With DeepSeek v4.1 Flash, it feels impossible to burn through the quota". https://www.reddit.com/r/opencode/comments/1wozjjf/with-deepseek-v41-flash-it-feels-impossible-to/
[11] OpenCode. "Go". https://dev.opencode.ai/go
[12] Reddit r/ollama (2026-09-08; comments dated 2026-09-10 and 2026-09-15). "CONFIRMED: Ollama Cloud nerfing usage limits on grandfathered Pro/Max Plans". https://www.reddit.com/r/ollama/comments/1waiu6b/confirmed_ollama_cloud_nerfing_usage_limits_on/
[13] Ollama. "Pricing". https://ollama.com/pricing
[14] OP.GG. "OpenCode Bar". https://github.com/opgginc/opencode-bar
[15] whosydd. "opencode-quota". https://github.com/whosydd/opencode-quota
[16] OpenUsage. "Z.ai provider adapter". https://github.com/robinebers/openusage/blob/main/docs/providers/zai.md
[17] LogicIncZo. "zai-usage". https://github.com/LogicIncZo/zai-usage
[18] kanalive. "GitHub Copilot Tracker". https://github.com/kanalive/github-copilot-tracker
[19] Z.ai. "Usage Stats". https://zcode.z.ai/en/docs/usage-stats
## Evidence package

Use [`sources.jsonl`](sources.jsonl), [`evidence.jsonl`](evidence.jsonl), [`claims.jsonl`](claims.jsonl), and [`query_log.jsonl`](query_log.jsonl) for machine-readable records. `scope.md`, `triangulation.md`, `critique.md`, and `decision-record.md` preserve the boundaries and review trail.
