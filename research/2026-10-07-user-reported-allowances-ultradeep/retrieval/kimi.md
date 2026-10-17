# Kimi / Moonshot AI current-window allowance retrieval

**Local-audit date:** 2026-10-07  
**Requested report / measurement window:** 2026-09-07 through 2026-10-07 inclusive  
**Fresh community search status:** Blocked; browser unavailable in this task context.  
**Local retained-case result:** One user-reported Kimi / old Allegretto estimate qualifies at provider/plan level (about 4×); it does not qualify for the ranked standard `kimi-k3` model row because the user measured K3-256. Two other quota anecdotes are not API-priceable.

## Browser blocker and search coverage

This task required the Codex in-app browser through `cua_repl` and prohibited fallback search tools. My `cua.getState()` inventory showed browser-extension Microsoft Edge surfaces but no in-app browser. The parent task reported the browser ID as `4`; trying `cua.getBrowser({id: "4"})` in this task context returned **“Browser is not available: 4.”** I did not use Edge, `web.run`, direct HTTP, or another search route.

As a result, I did not run fresh searches on Reddit, Hacker News, or developer communities for this assignment. The search entries below are preserved from the existing local log and are not new searches in this retrieval. The local retained-case audit is dated 2026-10-06, so there is no local coverage of reports posted on 2026-10-07.

The parent task separately inspected the Oct 4 Reddit source below in its Codex in-app browser and relayed the relevant post details for inclusion. I did not access that page in this task context; this supplied source does not make the current retrieval a fresh or exhaustive search.

## Ranked variant

The existing coverage roster identifies the ranked Kimi row as **`kimi-k3` / Kimi K3** ([local model coverage](../../2026-10-06-value-multiples/roster-coverage/model-coverage.csv)). It treats standard K3 as distinct from K3-256. A K3-256 report or estimate cannot be reassigned to the standard K3 row.

## Provider/plan-level eligible evidence; model-row near miss

| Report date | Direct source | Plan and fee reported by user | Exact model and measured period | Reported usage / API-priced amount | Provider/plan-level eligibility | Standard `kimi-k3` model-row eligibility |
|---|---|---|---|---|---|---|
| 2026-09-27 | [“I just measured Kimi Quota for Coding on Allegretto” — Reddit r/kimi](https://www.reddit.com/r/kimi/comments/1wqjghr/i_just_measured_kimi_quota_for_coding_on/) | Old Allegretto, **$39/month** | User says they measured **K3-256** during a **five-hour OpenCode session** and used 20% of the weekly quota. The session is described as “just measured” in the Sep 27 post; no separate session timestamp is retained locally. | Local audit records OpenCode JSON counts: 531,565 input; 14,409,728 cache-read; 45,089 output; 40,513 reasoning; 0 cache-write tokens. The user explicitly estimates **$7.20 at API prices** for K3-256. In the source, they estimate about **$36 per full week** and **$160/month**, calling the result approximately **4× for K3-256** and **2× for standard K3**. | **Eligible as Moonshot/Kimi — old Allegretto, about 4× (reported estimate).** The user ties the measured API-priced K3-256 usage, 20% weekly quota share, $39/month tier, and report date together. Use the provider/plan-level figure with exact K3-256 attribution. | **Not eligible for `kimi-k3`.** The ValueRank row is standard K3; the user's 2× standard-K3 figure is an extrapolation from measured K3-256, not direct standard-K3 use. Do not transfer it to the model row. |

The details and qualification above come from the existing [2026-10-06 community qualification audit](../../2026-10-06-value-multiples/roster-coverage/community-qualification-audit.md#L24), which accepts the user's estimate without independent arithmetic reconstruction but rejects it for the standard K3 row on variant mismatch.

### Provider-wise table treatment

For a provider-wise table, include **Moonshot AI / Kimi — old Allegretto: approximately 4×**, citing the Sep 27 post above and labeling the measured model **K3-256**. This is an end-user-reported API-priced allowance estimate for the provider/plan; it is not evidence for the standard `kimi-k3` ValueRank model row. Do not use the user's extrapolated 2× standard-K3 figure as a measured model-specific datapoint.

The arithmetic is consistent with the user's rounded estimate: $7.20 for 20% of the weekly allowance implies $36 for a full week ($7.20 ÷ 0.20). The post's approximately $160 monthly estimate divided by the $39/month fee is about 4.1×; annualizing $36 per week gives about $156/month, or 4.0× ($36 × 52 ÷ 12 ÷ $39). Retain the user's rounded **approximately 4×** table figure; these checks are approximate, not an independent reconstruction of the token ledger.

## Other retained Kimi cases: not API-priceable

The existing audit also records a Sep 21 Reddit post, [“Kimi Code consumed my entire 5-hour limit within minutes”](https://www.reddit.com/r/kimi/comments/1wm92oz/kimi_code_consumed_my_entire_5hour_limit_within/). The author says the full five-hour limit ran out within minutes while using the “default/basic model,” but does not identify an exact model variant, membership tier, or fee and provides no token counts or API-priced amount. It is not eligible for the ranked Kimi K3 row.

| Report date | Direct source | Plan and fee reported by user | Model and measured period | Reported usage / API-priced amount | Assessment for `kimi-k3` |
|---|---|---|---|---|---|
| 2026-10-04 | [“Upgraded to Kimi Allegro on an annual plan and get less usable time than before: quota gone in under 2 weeks, every month, with no resets and no usage breakdown” — Reddit r/kimi](https://www.reddit.com/r/kimi/comments/1wxcp3a/upgraded_to_kimi_allegro_on_an_annual_plan_and/) | User says they upgraded from Allegretto to Allegro and paid for a full year; the exact fee is not given. | User says an API request returned a monthly-limit error on Oct 4, and the monthly quota was exhausted in under two weeks. The post says machine logs contained only one script call, with the rest being normal personal work; it does not identify a Kimi model or provide a per-session/request model or feature breakdown. | No token counts, API-priced amount, or auditable model-level usage ledger. | **Not eligible.** This is an in-window end-user quota/usage report, but no exact fee, exact model variant, token usage, API-priced total, or auditable measurement is provided. The author's statement that logs showed one script call does not yield API-priceable Kimi usage. |

## Existing local search-log entries

These entries are from `research/2026-10-05-other-provider-coding/coding-provider-ultradeep/query_log.jsonl`; the local log records them as searched on 2026-10-05. They pertain to Kimi Code allowance discussions, not to the Sep 27 K3-256 measurement. The retained roster audit does not preserve the query that found the K3-256 post.

| Source | Exact prior query in local log | Prior search date | Local relevance |
|---|---|---:|---|
| Reddit | `"Kimi Code" (quota OR limit OR usage) September 2026 Reddit` | 2026-10-05 | General Kimi Code quota/usage discovery. |
| Reddit | `site:reddit.com/r/kimi "Kimi Code" "plan" "limit" after:2026-09-04` | 2026-10-05 | Kimi subreddit plan/limit search. |
| Hacker News | `site:news.ycombinator.com/item Kimi Code quota limit September 2026` | 2026-10-05 | HN Kimi Code quota/limit search; no API-priced Kimi K3 measurement is retained locally. |

The log also includes a developer-community search, `site:github.com Kimi Code quota tracker usage monitor plan 2026`, dated 2026-10-05. It is not a measured-user result.

## Eligibility conclusion and limits

The Sep 27 report is eligible for the **provider-wise Moonshot/Kimi old Allegretto row at approximately 4×**, based on the end user's reported K3-256 usage, API-priced estimate, 20% weekly allowance share, $39/month fee, and in-window post date. It is **not eligible for the standard `kimi-k3` model row**: the user measured K3-256, and the stated 2× standard-K3 value is extrapolated. The Sep 21 Kimi Code anecdote lacks model-level usage data and an API-priced total; the Oct 4 Allegro complaint reports quota exhaustion but no exact fee, model, tokens, API-priced amount, or auditable usage details.

This is a local audit of previously retained files, not a fresh or exhaustive search. No current-window claim is made for Oct 7 reports, and no provider-published quota, allowance, or marketing claim is used as a numerator.
