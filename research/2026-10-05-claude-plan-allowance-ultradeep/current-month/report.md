# Claude plan-allowance reports: measurements in the current window

**Research checked:** 6 October 2026  
**Audited measurement-date window:** 6 September–6 October 2026, inclusive  
**Retrieval dates:** 6 October 2026 for the final search addendum; source-specific dates are stated where applicable. Publication dates are provenance, not measurement eligibility.

## Executive Summary

This report applies a 6 September–6 October 2026 window to measurement start dates; Reddit post dates are provenance and do not establish eligibility. Only actual end-user-reported usage valued at API prices can support an exploratory numerator. User-derived estimates from actual logs are retained as estimates with their formula and reproducibility limits; provider quota/allowance statements and meter-only reports are context only, never numerator. Anthropic's help pages publish relative per-session usage and separate weekly limits, but no fixed consumer token or API-dollar entitlement. Its published plan prices are used only as supported fee denominators. [S-C01](https://support.claude.com/en/articles/11049741-what-is-the-max-plan) [1] [S-C02](https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work) [2]

Three in-window end-user estimates are eligible for clearly labeled exploratory API-price multiples: a Max 20x itemized estimate of $529.57 at 26% meter (the author's prose says about $529.50; calculations use the itemized total), a separate Max 20x estimate of $1,222 at 52% meter (the author projects about $2,350 per week), and a Max 5x estimate of about $469 per week. The resulting ratios are 44.1×, 50.9×, and 20.3×, calculated from the users' own API-priced estimates and published plan fees; none is a raw completed-week total or independently reproduced from source logs. The separate $12,751 S-C05 full-week amount is an API-priced two-account aggregate with a 30% top-up and cannot isolate one included plan allowance. S-C14's 65/95 is a user-defined throughput ratio and not an API-priced allowance numerator. [S-C03](https://www.reddit.com/r/ClaudeCode/comments/1wfb1x8/lower_usage_limits_kicking_in_early_and_large/) [3] [S-C04](https://www.reddit.com/r/ClaudeAI/comments/1why2zx/a_lot_of_talk_about_reduced_weekly_limits_but_a/) [4] [S-C05](https://www.reddit.com/r/ClaudeCode/comments/1wk3zq5/i_audited_my_session_logs_against_the_usage_meter/) [5] [S-C14](https://www.reddit.com/r/ClaudeAI/comments/1wn0xn9/max20x_is_now_just_15_times_better_than-max5x/) [14]

Other Reddit posts through 5 October are retained with each reporting user's exact tier wording, including “not stated,” but meter-only and hypothesis posts do not enter the numerator. The 6 October Reddit-first search addendum surfaced no qualifying new report in its indexed results; this is bounded coverage, not proof that no such post exists. GitHub and Reddit billing anomalies remain separate. S11 and S12's 23 August comparator are pre-window exclusions. [S-C16](https://www.reddit.com/r/ClaudeCode/comments/1wv2uto/did-limits-get-slashed-quietly/) [16] [S-C18](https://www.reddit.com/r/ClaudeAI/comments/1wy25jj/did-weekly-limits-get-secretly-reduced-on-pro-plan/) [18] [S-C19](https://www.reddit.com/r/ClaudeAI/comments/1wy1i2q/does-claude-burn-through-usage-faster-during-us/) [19]

The package does not validate ValueRank's provisional shared Claude Opus 5.5 40x route for exact-model current use. The Anthropic Artifacts promotion dated 1–15 October is outside this Claude Code allowance scope. The search covers indexed public English-language sources and is nonrepresentative; no universal Pro/Max allowance number is defensible from these reports.

## Introduction

The question is whether current-window measurements support an allowance estimate useful to ValueRank or validate its provisional shared route. The analysis treats publication date, measurement interval, retrieval date, user-stated plan, model, workload, and method as separate fields. Reddit is searched first. Measurement eligibility depends on interval start date; publication date alone never qualifies a report.

## Main Analysis

### Findings

Anthropic's current support material describes relative per-session usage, separate five-hour resets and shared weekly limits; usage depends on model, effort, features, conversation length and task complexity. Provider statements and meter percentages are context only, never numerator. A user-reported API-priced estimate from actual logs may support a provisional value multiple only when its measurement starts in-window, exact plan wording is retained, and the estimate is labeled as such. [S-C01](https://support.claude.com/en/articles/11049741-what-is-the-max-plan) [1] [S-C02](https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work) [2]

The current-window reports below do not establish one defensible universal Pro or Max allowance figure. The three qualifying exploratory multiples remain individual user estimates with different workloads and methods.

### User reports reviewed; segment eligibility by measurement date

“Plan as stated” preserves the reporting user's own tier wording. The audited window applies to the measurement interval start, not publication date. “Estimate” means an author-derived API-price value based on actual log/meter observations; “not independently reproducible” means source logs and pricing calculations were not supplied for this audit.

| Published | Plan as stated | Observation interval | Report and method | Limits on interpretation |
|---|---|---|---|---|
| 13 Sep | “Max 20x” | Sep 5 12:00 ET–Sep 12 12:00 ET begins before cutoff; separate Sep 12 12:00 ET–Sep 13 about 11:00 ET (≈23.3h) begins in-window | Local transcript/token logs plus server meter; pre-window week: about $2,715.63 API-price estimate at ≈100%. In-window segment: $529.57 itemized total (author's prose: about $529.50) and 26% of weekly meter. [S-C03](https://www.reddit.com/r/ClaudeCode/comments/1wfb1x8/lower_usage_limits_kicking_in_early_and_large/) [3] | Exclude the Sep 5-start week. The in-window partial estimate qualifies as user-reported API-priced log value; $529.57 ÷ 0.26 ≈ $2,036.81/week, but it is an estimate, not a completed-week measured total, and cannot be independently reproduced from public raw logs. |
| 16 Sep | “Max 5x” | Sep 5–14 baseline begins before cutoff; separate new partial period began Sep 15 and was ≈2 days / 29 weekly-meter points by the post | Transcript accounting and server-meter polling; baseline estimate about $421/week, new partial-period estimate about $469/week (also ≈$52 per five-hour meter). [S-C04](https://www.reddit.com/r/ClaudeAI/comments/1why2zx/a_lot_of_talk_about_reduced_weekly_limits_but_a/) [4] | Exclude the baseline. The in-window $469/week estimate qualifies as user-reported API-priced value derived from actual transcript/meter observations, not a full-week raw total; it is not independently reproducible and does not prove a controlled before/after change. |
| 18 Sep, 22:07:53 UTC | “two Max 20x accounts” | Full Sep 10–17 period is in-window; separate one-account segment starts at Sep 17 11:00 PT reset and runs ≈28h through the post | Author parsed/deduplicated Claude Code JSONL from two machines/accounts and priced input/output/cache categories at API list rates. Full period: 55,878 calls; 23.5B cache-read, 46.9M uncached-input, 86.4M cache-write, 11.1M output tokens; $12,751 modeled API cost; both accounts reached 100% weekly meter, one had a 30% top-up, combined meter use 230%. Partial one-account period: 5,600 calls, 2.1B cache reads, $1,222 modeled API cost at 52%; author explicitly estimates about $2,350 per Max 20x week. [S-C05](https://www.reddit.com/r/ClaudeCode/comments/1wk3zq5/i_audited_my_session_logs_against_the_usage_meter/) [5] | The full-week $12,751 is a measured/log-priced aggregate but is not isolatable to one included plan because it combines two accounts and includes a top-up; do not use it as a per-plan numerator. The separate partial estimate qualifies: $1,222 ÷ 0.52 = $2,350/week by the author's extrapolation. It is not a completed week or independently reproducible from raw logs; author says about 95% of tokens were cache reads and meter weighting cannot be proven. |
| 22 Sep, 05:45:33 UTC | “Max20x” and “Max5x” | Current point reported 22 Sep; comparison point is 23 Aug and is historical | The author of a subscription-pooling tool normalizes observed weekly consumption by assumed session capacity (Pro=1, Max5=5, Max20=20). They report the current Max20x-to-Max5x ratio as 65/95, about 1.5x, compared with 47/118, about 2.5x, on 23 Aug. [S-C14](https://www.reddit.com/r/ClaudeAI/comments/1wn0xn9/max20x_is_now_just_15_times_better_than-max5x/) [14] | This is a user-defined throughput ratio, not a measurement of absolute token units or proof that the value of a quota unit changed. The post does not specify models, workload, or account count. Only the 22 Sep point is current-window evidence; the 23 Aug point is historical context. |
| 23 Sep, 16:39:25 UTC | “Pro x5 plan” | Current weekly meter at time of post; precise start time not stated | The author says they were already 50% through the weekly limit while asking whether a one-time reset could be used. [S-C20](https://www.reddit.com/r/ClaudeAI/comments/1wob3p1/has_anyone_used_their_reset_yet/) [20] | No model, work volume, start point, or reset outcome; this is a single status report, not a weekly-cap measurement. |
| 24 Sep | “$20 Pro plan” (title wording) | Two five-hour checks; exact timestamps not stated | The author says the five-hour limit was 13.333% of weekly allowance in two observations. [S-C06](https://www.reddit.com/r/ClaudeCode/comments/1wowd1p/currently_the_5h_limit_is_13333_of_the_weekly/) [6] | One account, n=2, rounded server-meter relation; no basis for a plan-wide conversion. |
| 30 Sep | “Max20x” | One sequence of windows; exact dates within the sequence not given | The author describes a Fable/Opus/Sonnet workflow with a free reset, weekly usage, and partial five-hour sessions, then infers fewer than four full sessions. [S-C07](https://www.reddit.com/r/ClaudeAI/comments/1wtxx70/weekly_limit_is_less_than_five_5hour_sessions/) [7] | Qualitative one-account sequence; multiple products/models and no standardized denominator. |
| 1 Oct | “$20 plan btw” (author's exact wording) | “Earlier this week” comparison against “today”; post published 1 Oct | For Opus 5.5 Medium, the author contrasts 60–70% of a limit after 3–4 hours earlier in the week with 45% after 30 minutes “today.” [S-C16](https://www.reddit.com/r/ClaudeCode/comments/1wv2uto/did_limits_get_slashed_quietly/) [16] | The exact tier is not stated beyond “$20 plan btw”; the meter type is unclear and the tasks are not matched. Do not infer Pro from the price. |
| 1 Oct | “not stated” | A recent session; the post also says the account had been idle 22h38m | The author says three Opus 5.5 Medium questions used 42% of the session limit. [S-C17](https://www.reddit.com/r/ClaudeCode/comments/1wuuxws/what_on_earth_is_going_on_with_the_usage/) [17] | No plan, task details, prompt sizes, or account meter baseline; the idle interval does not establish a cause. |
| 5 Oct, 07:15:35 UTC | “pro plan” (title wording) | The author's comparison is to a prior pattern of 9–10 full five-hour sessions; the reported new estimate was described as “last week” | The author says a 5%-per-hour to 1%-per-week relationship would leave about five five-hour sessions, and says they hit the weekly limit for the first time in a long time. [S-C18](https://www.reddit.com/r/ClaudeAI/comments/1wy25jj/did_weekly_limits_get_secretly_reduced_on_pro_plan/) [18] | The post does not provide a matched workload or raw meter series. “pro plan” is preserved from its title; this is one user's report, not evidence of a universal reduction. |
| 5 Oct | “not stated” | Author says they had watched usage “for about a week”; exact dates and comparable tasks are not given | The author suspects usage falls faster at U.S. peak hours, while acknowledging that task length, model, and effort could explain the difference. [S-C19](https://www.reddit.com/r/ClaudeAI/comments/1wy1i2q/does_claude_burn_through_usage_faster_during_us/) [19] | The author did not compare identical tasks. Treat as a hypothesis/question, not a measured peak-hour effect. |

### API-priced end-user estimates that qualify for an exploratory multiple

These values use only in-window end-user reports that price actual logged usage. The numerator is the user's API-price estimate/extrapolation; it is not an Anthropic quota claim or subscription entitlement. The fee denominator uses the published Max plan fee on S-C01. The calculations annualize a weekly estimate to a monthly equivalent with 52 ÷ 12.

| User-stated plan and in-window segment | Estimate status | Calculation | Result |
|---|---|---|---:|
| Max 20x, Sep 12–13, about 23.3 hours (S-C03) | API-priced log estimate from a partial segment; not independently reproducible | ($529.57 ÷ 0.26) × (52 ÷ 12) ÷ $200/month | **≈44.1×** |
| Max 20x, Sep 17 reset, first ≈28 hours (S-C05) | Author's explicit estimate from $1,222 / 52%; not a completed-week raw measurement and not independently reproducible | ($1,222 ÷ 0.52) × (52 ÷ 12) ÷ $200/month | **≈50.9×** |
| Max 5x, Sep 15 onward partial period (S-C04) | Author's ≈$469/week estimate from about two days/29 meter points; not independently reproducible | $469 × (52 ÷ 12) ÷ $100/month | **≈20.3×** |

These are provisional, individual, author-reported API-price estimates. Do not average them, treat them as current provider entitlements, or transfer the mixed-use figures to a specific model. The pre-window Sep 5-start $2,715.63 S-C03 week and Sep 5–14 S-C04 baseline are excluded even though their posts were published later. S-C05's $12,751 two-account/top-up total is retained as measured context but is not an isolated included-plan numerator.
### Incidents, not allowance estimates

Two in-window Claude Code GitHub posts describe individual meter or consumption anomalies: issue #93596 (11 Sep) reports a Max 5x user's change in thinking/output consumption; issue #94581 (15 Sep) reports a five-hour meter reaching 33% after an 18-minute idle interval and was marked duplicate. Neither has a verified general cause or establishes a plan-wide allowance change. [S-C08](https://github.com/anthropics/claude-code/issues/93596) [8] [S-C09](https://github.com/anthropics/claude-code/issues/94581) [9]

A 23 Sep Reddit post says a user on a “Max 20x plan” saw about $150 in Console API credits consumed over two hours, with about 144M tokens recorded from 08:00–10:00 UTC; the author says local transcript counts roughly matched and that extra usage was enabled. This is a reported billing/routing anomaly, not subscription allowance evidence, and its cause is unknown. [S-C21](https://www.reddit.com/r/ClaudeAI/comments/1wo2afv/claude_code_on_my_max_20x_plan_billed_150_to_my/) [21]

### Current policy and tracker context

Anthropic defines Max 5x and Max 20x as five and twenty times Pro's per-session usage allowance, with a separate five-hour reset and shared weekly allowance; its usage explanation names model, effort, features, conversation length, and complexity as consumption factors. The pages were checked on 5 Oct 2026 and do not give a fixed absolute token/API-dollar cap. [S-C01](https://support.claude.com/en/articles/11049741-what-is-the-max-plan) [1] [S-C02](https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work) [2]

Claude Tuner's public stats page showed loading/placeholders when checked 5 Oct, so no numeric crowd estimate could be extracted. Its privacy page describes collection/storage of usage and account metadata; that is a maintainer disclosure, not an independent operational audit. [S-C10](https://claudetuner.com/stats/) [10] [S-C11](https://claudetuner.com/privacy/) [11]

Two selected projects illustrate the distinction between personal-quota monitors and local-log analysis: cc-hdrm describes a personal server-quota display, while ccusage analyzes local Claude Code logs and estimates token/API-price totals. Neither page supplies a normalized public crowd allowance dataset. This is a bounded discovery, not a complete tool or security audit. [S-C12](https://github.com/rajish/cc-hdrm) [12] [S-C13](https://github.com/ccusage/ccusage) [13]

### Exclusions and ValueRank applicability

Root-register report S11 was published 24 Aug 2026 and edited 31 Aug 2026, and its described empirical readings start before the 6 Sep measurement cutoff; it is excluded from current synthesis. Its one-account / partially typed meter observations remain explicitly historical context only. [S-C15](https://www.reddit.com/r/ClaudeAI/comments/1vx0k69/lifting-the-curtain-the-max-x5-and-max-x20-usage/) [15]

S12's 23 Aug comparison is also pre-window and is not used as current evidence; its separately identified 22 Sep observation is in-window context but is a user-normalized ratio, not API-priced allowance value. [S-C14](https://www.reddit.com/r/ClaudeCode/comments/1wn0xn9/max20x_is_now_just_15_times_better_than-max5x/) [14]

ValueRank's provisional shared Claude Opus 5.5 40x route is unvalidated here for exact-model current use. This package contains no controlled, current Opus 5.5 40x evidence for that shared route. The Anthropic Artifacts promotion dated 1–15 Oct is outside this Claude Code allowance assessment and is not counted as a Claude Code quota observation.

### Search coverage and workflow status

Reddit was searched first; GitHub issues, official plan pages, and selected tracker repositories followed. Search strings, direct-source checks, and bounded coverage notes are in [`query_log.md`](query_log.md). Publication dates, observed dates, retrieval dates, plans as stated, methods, caveats, and claim mappings are in [`sources.jsonl`](sources.jsonl), [`evidence.jsonl`](evidence.jsonl), and [`claims.jsonl`](claims.jsonl).

The Silver Bullet Deep Research Ultradeep contract was reviewed through LeanCTX and its nine phases were applied manually; the slash command was not invoked. Validator execution status is based on logs in validation/. The search is English-language and limited to indexed public material; deleted, private, login-only, or differently worded reports may be missing.


## Synthesis

Current-window evidence includes three author-reported API-priced estimates with identifiable plan tiers, but each is extrapolated from a partial log/meter interval and is not independently reproduced. The Max20x 44.1× and 50.9× and Max5x 20.3× values are exploratory individual ratios only. S-C05's $12,751 two-account/top-up total cannot isolate one included allowance. Meter-only reports, provider statements, S-C14's normalized ratio, and incidents are context, never numerator. No common workload, plan denominator, or verified meter calibration supports a universal allowance, and no evidence establishes that a policy change occurred.

## Limitations

The Reddit evidence is self-selected and author-reported. The three included estimates come from actual logs/meter readings but are author-calculated, partial-period estimates whose source logs and full price calculations were not independently reproduced here. Other reports omit API-priced logs and therefore remain context only. Search indexing may omit deleted, private, login-only, or differently worded posts.

## Recommendations

- Do not use these community numbers as fixed Pro/Max value, monthly tokens, or a comparison benchmark.
- Treat the exact Opus 5.5 40x route as unvalidated until a controlled workload, plan, account scope, and current meter record are captured.
- For a later refresh, apply the then-current measurement-date window to interval starts, preserve publication dates separately, and recheck Reddit-first sources directly.

## Counterevidence Register

- Anthropic's current documentation says consumption depends on several workload variables, so community claims that a plan-wide allowance changed cannot be confirmed from meter anecdotes alone. [S-C01](https://support.claude.com/en/articles/11049741-what-is-the-max-plan) [1] [S-C02](https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work) [2]
- S12's 22 September ratio is about 1.5x after the author's normalization, which challenges a simple assumption that plan multipliers translate linearly into realized throughput. It is not an absolute token comparison and its denominator is user-defined. [S-C14](https://www.reddit.com/r/ClaudeAI/comments/1wn0xn9/max20x_is_now_just_15_times_better_than-max5x/) [14]
- October reports point in different directions and do not match workload or meter definitions: the Oct 1 author reports three questions at 42%, while the Oct 5 author describes a prior 9–10-session pattern and a weekly-limit event. These are not controlled comparisons and neither establishes the size or cause of a policy change. [S-C17](https://www.reddit.com/r/ClaudeCode/comments/1wuuxws/what-on-earth-is-going-on-with-the-usage/) [17] [S-C18](https://www.reddit.com/r/ClaudeAI/comments/1wy25jj/did-weekly-limits-get-secretly-reduced-on-pro-plan/) [18]

## Claims-Evidence Table

| Claim ID | Evidence ledger records | Report citations |
|---|---|---|
| C-C01 provider policy | E-C01, E-C02 | [1] [2] |
| C-C02 heterogeneous current reports | E-C03–E-C07, E-C12, E-C14–E-C18, E-C23–E-C25 | [3] [4] [5] [6] [7] [14] [16] [17] [18] [19] [20] |
| C-C03 Claude Tuner page state | E-C10 | [10] |
| C-C04 selected project types | E-C20, E-C21 | [12] [13] |
| C-C05 GitHub anomaly reports | E-C08, E-C09 | [8] [9] |
| C-C06 Reddit Console credit incident | E-C19 | [21] |
| C-C07 measurement-date exclusions | E-C03–E-C04, E-C13, E-C22 | [3] [4] [14] [15] |
| C-C08 Claude Tuner privacy disclosure | E-C11 | [11] |
| C-C09 S-C03 Max 20x partial API-price estimate | E-C23 | [3]; fee denominator [1] |
| C-C10 S-C05 Max 20x explicit $2,350/week projection | E-C25 | [5]; fee denominator [1] |
| C-C11 S-C04 Max 5x partial API-price estimate | E-C24 | [4]; fee denominator [1] |

## Bibliography

[1] Anthropic Help Center. “What is the Max plan?” Current policy page checked 5 October 2026. https://support.claude.com/en/articles/11049741-what-is-the-max-plan (S-C01)  
[2] Anthropic Help Center. “How do usage and length limits work?” Current policy page checked 5 October 2026. https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work (S-C02)  
[3] Reddit r/ClaudeCode. “Lower usage limits kicking in early and large than expected.” 13 September 2026. https://www.reddit.com/r/ClaudeCode/comments/1wfb1x8/lower_usage_limits_kicking_in_early_and_large/ (S-C03)  
[4] Reddit r/ClaudeAI. “A lot of talk about reduced weekly limits but a lack of data - so here's some actual numbers.” 16 September 2026. https://www.reddit.com/r/ClaudeAI/comments/1why2zx/a_lot_of_talk_about_reduced_weekly_limits_but_a/ (S-C04)  
[5] Reddit r/ClaudeCode. “I audited my session logs against the usage meter.” 18 September 2026. https://www.reddit.com/r/ClaudeCode/comments/1wk3zq5/i_audited_my_session_logs_against_the_usage_meter/ (S-C05)  
[6] Reddit r/ClaudeCode. “Currently, the 5h limit is 13.333% of the weekly limit on a $20 Pro plan.” 24 September 2026. https://www.reddit.com/r/ClaudeCode/comments/1wowd1p/currently_the_5h_limit_is_13333_of_the_weekly/ (S-C06)  
[7] Reddit r/ClaudeAI. “Weekly limit is less than five 5-hour sessions.” 30 September 2026. https://www.reddit.com/r/ClaudeAI/comments/1wtxx70/weekly_limit_is_less_than_five_5hour_sessions/ (S-C07)  
[8] GitHub anthropics/claude-code. Issue #93596, “Abnormal Claude Code thinking/output growth and faster usage draw.” Opened 11 September 2026. https://github.com/anthropics/claude-code/issues/93596 (S-C08)  
[9] GitHub anthropics/claude-code. Issue #94581, “Idle account meter moved rapidly.” Opened 15 September 2026. https://github.com/anthropics/claude-code/issues/94581 (S-C09)  
[10] Claude Tuner. “Aggregate statistics.” Retrieved 5 October 2026. https://claudetuner.com/stats/ (S-C10)  
[11] Claude Tuner. “Privacy policy.” Retrieved 5 October 2026. https://claudetuner.com/privacy/ (S-C11)  
[12] GitHub repository rajish/cc-hdrm. Retrieved 5 October 2026. https://github.com/rajish/cc-hdrm (S-C12)  
[13] GitHub repository ccusage/ccusage. Retrieved 5 October 2026. https://github.com/ccusage/ccusage (S-C13)  
[14] Reddit r/ClaudeAI, canonical redirect to r/ClaudeCode. “Max20x is now just 1.5 times better than Max5x.” Published 22 September 2026. https://www.reddit.com/r/ClaudeAI/comments/1wn0xn9/max20x_is_now_just_15_times_better_than-max5x/ (S-C14)  
[15] Reddit r/ClaudeAI. “Lifting the curtain: the Max x5 and Max x20 usage.” Published 24 August 2026; edited 31 August 2026; historical exclusion only. https://www.reddit.com/r/ClaudeAI/comments/1vx0k69/lifting-the-curtain-the-max-x5-and-max-x20-usage/ (S-C15)  
[16] Reddit r/ClaudeCode. “Did limits get slashed quietly?” 1 October 2026. https://www.reddit.com/r/ClaudeCode/comments/1wv2uto/did-limits-get-slashed-quietly/ (S-C16)  
[17] Reddit r/ClaudeCode. “What on earth is going on with the usage?” 1 October 2026. https://www.reddit.com/r/ClaudeCode/comments/1wuuxws/what-on-earth-is-going-on-with-the-usage/ (S-C17)  
[18] Reddit r/ClaudeAI. “Did weekly limits get secretly reduced on pro plan?” 5 October 2026. https://www.reddit.com/r/ClaudeAI/comments/1wy25jj/did-weekly-limits-get-secretly-reduced-on-pro-plan/ (S-C18)  
[19] Reddit r/ClaudeAI. “Does Claude burn through usage faster during US peak hours, or am I imagining it?” 5 October 2026. https://www.reddit.com/r/ClaudeAI/comments/1wy1i2q/does-claude-burn-through-usage-faster-during-us/ (S-C19)  
[20] Reddit r/ClaudeAI. “Has anyone used their reset yet?” 23 September 2026. https://www.reddit.com/r/ClaudeAI/comments/1wob3p1/has-anyone-used-their-reset-yet/ (S-C20)  
[21] Reddit r/ClaudeAI. “Claude Code on my Max 20x plan billed $150 to my Console API credits in two hours.” 23 September 2026. https://www.reddit.com/r/ClaudeAI/comments/1wo2afv/claude_code_on_my_max_20x_plan_billed_150_to_my/ (S-C21)

## Methodology

This manual run follows the silver-deep-research contract: scope, plan, retrieve, triangulate, outline, synthesize, critique, refine, and package. The selected depth is ultradeep because the task asks for comprehensive, date-sensitive account evidence and contains contradictory readings. The critique records three manual adversarial passes and the refinement decisions. Search was Reddit-first; the official search executable was probed via LeanCTX and not found, so Codex built-in web search and source opening were used as the fallback. No external browser was used.

Silver Bullet's slash command itself was not invoked. The available direct validator script validate_report.py was executed via LeanCTX; its initial run failed on missing report sections, numeric citations, bibliography, and metadata. That failure prompted this structure/citation repair. Citation, claim-support, and phase-gate statuses appear in the validation log files and should be read as execution results, not inferred from this report.

## Report Metadata

- Run ID: 2026-10-05-claude-plan-allowance-current-month
- Workflow ID: WF-SILVER-DEEP-RESEARCH
- Atomic flow: AF-DECIDE
- Flow step: FS-SILVER_DEEP_RESEARCH
- Mode: ultradeep
- Research type: default
- Measurement window: 2026-09-06 through 2026-10-06 inclusive; eligibility uses measurement start date
- Browser/search route: Codex built-in web
