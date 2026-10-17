# Community search log addendum

**Run date:** 2026-10-05. Search route: built-in `web__run` Internet search/open. Publication cutoff used for community allowance reports: 2026-09-05 through 2026-10-05 inclusive. The queries below were run to broaden the previous provider-specific Reddit/Hacker News/developer-community searches. Results are bounded by search-engine retrieval and the returned top matches; “not found” means no qualifying match surfaced in that result set.

## Exact provider-specific Reddit queries

| ID | Query | Outcome in surfaced results |
|---|---|---|
| Q01 | `site:reddit.com/r/GithubCopilot after:2026-09-05 Copilot premium requests credits usage limit September October 2026` | Found Oct 4 Pro+ credit discussion, Sep 6 legacy quota-wipe allegation (quantified events were before cutoff), Sep 10 credit-exhaustion complaint with an underspecified window, and older posts. |
| Q02 | `site:reddit.com/r/cursor after:2026-09-05 Cursor usage limit credits billing model October 2026` | Found Sep 27 quota discussion with a reply claiming one Opus 5.5 High prompt used 25% monthly Other Models; other returned results included older reports. |
| Q03 | `site:reddit.com/r/Windsurf OR site:reddit.com/r/Codeium after:2026-09-05 Windsurf quota prompt credits usage October 2026` | No Windsurf-only current-plan allowance report surfaced in returned matches; found a Sep 18 r/windsurf post that explicitly concerns a paid Devin plan converted from Windsurf. Devin evidence is kept separate. |
| Q04 | `site:reddit.com/r/google_antigravity after:2026-09-05 weekly quota usage reset limits October 2026` | Found community support/issue posts; no controlled normalized consumption report from this query alone. Follow-up Google developer-forum results are separately logged below. |
| Q05 | `site:reddit.com/r/cursor after:2026-09-05 "usage" Cursor credits September 2026 limits` | Found Sep 30 Ultra one-cycle CSV/API report; its cycle began Sep 2, so cumulative value is excluded as mixed-window. Also returned older August plan-limit post, discovery-only. |
| Q06 | `site:reddit.com/r/cursor "September" "2026" "Cursor Ultra" usage limits` | Found Sep 17 Ultra/Fable 5.1 single-question claim and Sep 27 quota discussion; claims are anecdotal with incomplete account/task controls. |
| Q07 | `site:reddit.com/r/Windsurf OR site:reddit.com/r/Codeium after:2026-09-05 usage quota credits` | Returned Devin weekly-quota report and older Windsurf posts. No eligible Windsurf-only current-plan allowance measurement surfaced. |
| Q08 | `site:reddit.com/r/google_antigravity after:2026-09-05 quota reset percentage weekly limit` | Returned Antigravity quota-support report; no independently measured allowance series surfaced. |

## Exact Hacker News query batch

| ID | Query | Outcome in surfaced results |
|---|---|---|
| Q09 | `site:news.ycombinator.com Gemini AI Pro Ultra quota allowance usage September October 2026` | Returned an Antigravity transition/billing discussion and older policy discussion, not a post-cutoff measured allowance report. |
| Q10 | `site:news.ycombinator.com GitHub Copilot AI credits quota usage allowance September October 2026` | Returned older billing-change/pricing threads; no eligible post-cutoff measured report surfaced. |
| Q11 | `site:news.ycombinator.com Cursor usage credits Ultra Pro quota September 2026` | No post-cutoff measured Cursor allowance report surfaced in returned matches. |
| Q12 | `site:news.ycombinator.com Windsurf Codeium quota credits usage Devin September 2026` | Returned an older March Windsurf quota-policy comment and older product history; no eligible current Windsurf allowance report surfaced. |

These HN results support only bounded absence for these exact searches and result pages. One result with a recent crawl date can still be an older thread; the thread’s publication date was checked before excluding it.

## Google developer forum and GitHub/community routes

| ID | Route / query | Outcome |
|---|---|---|
| Q13 | Google AI Developers Forum search: `site:discuss.ai.google.dev/t/ "Antigravity" "quota" "September" "2026"` | Directly opened Sep 10 Google AI Pro Antigravity 429/frozen-timer case and Sep 28 Antigravity weekly reset moved to Oct 4. Both are diagnostic reports, not clean allowance-consumption measurements. |
| Q14 | Google AI Developers Forum search: `site:discuss.ai.google.dev/t/ "Antigravity" "credits" "quota" "429"` | Directly opened Sep 21 report of 35,000 credits visible alongside repeated 429 errors; no reported burn rate. |
| Q15 | GitHub Community search family: Gemini Antigravity quota/limit, Copilot credits/limit, Cursor forum usage, and Windsurf GitHub issues | Found older Copilot FAQ/discussions and pre-cutoff Copilot reports, retained as discovery/policy only in the main package. No recent Windsurf issue with an eligible measured allowance surfaced in returned results. This is a query family across four routes, not a single exhaustive GitHub query. |
| Q16 | Cursor Forum: direct URL `https://forum.cursor.com/t/change-in-token-usage-billing/170724` | Opened Sep 5 post (new period began that day) and Sep 6–16 replies. The main early-month account report is cutoff-eligible; later replies are discrete dated reports. |

## Tracker discovery searches

| ID | Query | Outcome |
|---|---|---|
| Q17 | `AI subscription usage tracker community crowdsourced Gemini Copilot Cursor Windsurf quota tracker app 2026` | Found current repository listings for AI Limits, Cursor Usage Tracker, Copilot Tracker, onWatch and related local account meters. The opened projects store personal usage locally or query the user’s own account; no shared public measurement corpus was established. |
| Q18 | `site:github.com "Cursor" quota usage tracker dashboard extension credits 2026` | Opened Tendo33 Cursor Usage Tracker; README says it reads local Cursor identity and provider usage endpoints, and labels those endpoints unofficial/subject to change. |
| Q19 | `site:github.com "Copilot" AI credits tracker usage dashboard extension` | Opened kanalive Copilot Usage Tracker; local OpenTelemetry/log/dashboard and optional quota polling, no crowd database. |
| Q20 | `site:github.com Antigravity Gemini weekly quota tracker app` | Opened Antigravity Account Switcher and QuotaChecker-TUI; both describe per-account/local tracking, not a public aggregate dataset. |
| Q21 | `site:github.com "Gemini CLI quota" "Cursor" "Windsurf" tracker 2026 GitHub` | Opened onWatch. README lists Copilot, Cursor, Antigravity and legacy Gemini CLI quota support; local polling/database, not crowd data. |
| Q22 | `AI Usage Meter: Limit Tracker` | Search result points to a Google Play listing updated Sep 8, 2026 claiming local subscription tracking for many providers. Not treated as verified coding-provider coverage or a crowd database because its plan/provider implementation was not independently inspected in this addendum. |

## Coverage limits

- Search was in English and used a bounded set of exact provider/subreddit/route terms. Reddit, HN, and forum indexing can omit deleted, private, unindexed, or differently worded posts.
- Search results were opened directly where used in the report. Reddit relative-time labels conflicted with machine date and some search snippets; exact post dates were taken from `created_utc` when opened via Reddit JSON, otherwise from explicit forum/search publication metadata. All measurement intervals remain separately recorded.
- One source can contain both in-window and out-of-window statements. Only a separately dated, separable in-window segment can support current-period reporting. The Copilot Sep 6 quota-wipe source and Cursor Sep 30 cycle source are retained but excluded for this reason.
- The tracker search was product/repository discovery, not a security or source-code audit. README capability and privacy statements are maintainer claims.
- No result set establishes literal absence of a crowdsourced allowance-reporting app or of eligible posts. The evidence supports only that none was identified in the documented search routes and surfaced results, apart from ordinary unstructured forum/Reddit replies.
