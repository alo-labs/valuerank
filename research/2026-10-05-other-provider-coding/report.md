# Coding subscription allowances and trackers

**Research snapshot:** 2026-10-05. **Current community-report window:** published 2026-09-05 through 2026-10-05. **Scope:** Google Gemini / AI Pro and Ultra (including Gemini CLI/Antigravity), GitHub Copilot, Cursor, and Windsurf/Codeium. Codex and Claude allowance research are excluded.

## Findings

Provider policy pages and their own usage meters are the strongest current evidence. Gemini limits are compute-based, vary by model and workload, refresh every five hours subject to a weekly cap, and publish plan multipliers rather than a stable prompt count. Copilot's current individual-plan policy uses AI credits and dynamic rate limits without a universal numeric monthly quota; the old monthly request counts are limited to qualifying grandfathered annual seats. Cursor reports two pools in its Spending dashboard. Windsurf reports model-weighted token budgets with daily and weekly resets.

Recent community evidence is uneven. The most detailed Cursor Ultra report was published Sept. 30 and describes a cycle beginning Sept. 2, using a CSV plus usage-summary API and translating values at public API list rates. Because the interval crosses the Sept. 5 cutoff and the author did not provide an isolated post-cutoff interval, its reported dollar-equivalent values are excluded from current measurement estimates. Recent Gemini and Copilot reports describe user-visible credit consumption or limit experiences, but omit enough workload, exact model/version, or full reset-window detail to support comparable numeric estimates. An Oct. 4 Copilot Pro+ discussion includes conflicting credit figures (including an employer-provided 7,000-credit monthly allowance and a reply describing 150,000 credits with 24,000 consumed); these are individual account claims, not a representative Copilot allowance. The date-filtered Windsurf Reddit query found no matching results. See the supplemental community search for the additional current-window report records and date handling.

**Trackers:** OpenUsage and Pulse are active local, per-account quota monitors relevant to several assigned products. They are not public crowdsourced comparison databases. Their adapter support varies: Pulse says some integrations have not been tested against a live account. Gemini CLI integrations should be treated as stale for personal AI Pro/Ultra because Google ended individual-account service through Gemini CLI on 2026-06-18. TiboTattle is a current Codex-focused allowance monitor, so it is outside this assignment.

## Current provider policy

| Provider | Official policy context | Live meter / interpretation |
|---|---|---|
| Gemini Apps | Compute-based limits; five-hour refresh plus weekly cap. AI Pro is 4x standard; AI Ultra is 5x or 20x Pro, depending on subscription. Complexity, model, features, chat length and thinking level affect consumption. | Gemini Apps gives near-limit and refresh feedback. Google AI credits for some products are a separate balance. |
| Gemini CLI | Personal free/Pro/Ultra requests through Gemini CLI ended June 18, 2026; Google announced transition to Antigravity CLI. | Check the current Antigravity account surface. Third-party saved-login readers for Gemini CLI should not be assumed to read current personal-plan quotas. |
| GitHub Copilot | Current individual policy refers to AI credits and dynamic rate limits but gives no universal numeric monthly quota. Legacy Pro/Pro+ request limits of 300/1,500 monthly apply only to qualifying grandfathered annual seats. | Use GitHub account billing/usage. Keep current credits separate from legacy requests. |
| Cursor | Separate Cursor Models and Other Models usage; monthly billing-cycle reset, no carryover, with on-demand usage available. | Spending tab provides real-time remaining usage by pool. |
| Windsurf | Token-based, model-cost-weighted usage with daily and weekly budgets and resets. | Plan meter shows remaining quota and reset. Older credit-era reports do not establish current allowance. |

## Eligible community reports

- **Gemini AI Plus:** one Sept. 29 user says a task consumed 58% of the weekly allowance. Missing exact model and workload details make this an anecdote, not a plan estimate.
- **Copilot:** recent users report remaining monthly credits or hitting monthly/short-window limits. Captured posts do not disclose a comparable plan/model/workload protocol.
- **Copilot Pro+ (Oct. 4):** a current discussion contains differing credit-allocation and consumption figures, including one employer-provided 7,000-credit monthly allowance and a reply describing a 150,000-credit allocation with 24,000 consumed. Accounts, plans and measurement intervals differ; do not treat either as a standard plan quota. [Discussion](https://www.reddit.com/r/GithubCopilot/comments/1wxfp92/copilot_pro_usage_limits/)
- **Cursor Ultra:** a Sept. 30 post identifies a cycle beginning Sept. 2, exports CSV and usage-summary API information, and converts model usage using API list rates. Its interval crosses the publication cutoff and no separately identifiable post-cutoff measurement was supplied, so it is discovery/method context only.
- **Windsurf:** no matching Reddit results in the after-2026-09-05 search. Older posts are discovery-only.

No community estimate is promoted as provider policy. Evidence and claim records preserve source, date, method, plan/model scope, confidence and limitations.

## Tracker landscape

- **OpenUsage** (S32): active macOS menu-bar app; project page lists Cursor, Copilot, Antigravity/Devin and Gemini CLI support. Its Gemini CLI saved-login reader is read-only, and personal Gemini CLI support has ended.
- **Pulse** (S33): active macOS overlay/menu-bar app; README lists Cursor, Copilot, Windsurf, Antigravity and Gemini CLI. It distinguishes provider-reported values from estimates and states some adapters have not been verified against live accounts.
- **Other candidates:** quota-tracker (Copilot/Gemini), CodexBar, and an Antigravity quota extension were surfaced. Their inclusion records discovery, not proof of live operation for every adapter.
- **TiboTattle** (S37): current product scope is Codex allowance accounting, not the four assigned provider families.

**Answer:** live personal quota monitors exist, especially OpenUsage and Pulse. This search pass did not identify a verified public crowd database publishing comparable, method-tagged measurements across Gemini, Copilot, Cursor and Windsurf. This is a bounded “not found,” not proof none exists.

## Explicit search/query/source log

Built-in browser only. Discovery was Reddit-first, then Hacker News, official provider docs, GitHub discussions/issues, and tracker repositories. The parent follow-up adds 21 source records, 13 evidence records, and 9 linked cutoff/scope claims; two source URLs overlap the core 39-record registry, giving 58 unique URLs across both packages. See [`community-research-addendum.md`](community-research-addendum.md), [`community-query-log-addendum.md`](community-query-log-addendum.md), and [`community-claims-addendum.jsonl`](community-claims-addendum.jsonl) for the expanded provider searches and report-level cutoff classifications.

| # | Surface and exact query / route | Outcome |
|---:|---|---|
| 1 | Reddit/Google: `Gemini CLI usage limits AI Pro Ultra Reddit GitHub tracker quota` | Gemini discussion and tracker discovery. |
| 2 | Reddit/Google: `site:reddit.com/r/GeminiCLI quota tracker usage limit AI Pro Ultra` | No current personal CLI measurement established. |
| 3 | Reddit/Google: `Gemini AI Pro Ultra quota usage September 2026 Reddit GeminiCLI` | Recent AI Plus anecdote and model-access threads. |
| 4 | Reddit/Google: `site:reddit.com/r/cursor after:2026-09-05 usage limits Pro Ultra credits` | Recent pool reports; directly opened the Ultra CSV/API report and balance-vs-percent post. |
| 5 | Reddit/Google: `site:reddit.com/r/windsurf after:2026-09-05 quota allowance usage` | No matching documents. |
| 6 | Reddit/Google: `site:reddit.com/r/GithubCopilot after:2026-09-05 credits quota usage limits` | Recent credit-use/limit posts; opened one. |
| 7 | HN/Google: `site:news.ycombinator.com Gemini CLI AI Pro quota limits 2026` | Recent Gemini discussions and older CLI transition history; qualitative only. |
| 8 | HN/Google: `site:news.ycombinator.com GitHub Copilot credits quota limits usage 2026` | Mostly tangential results; discussion retained as context only. |
| 9 | GitHub/Google: `site:github.com/google-gemini/gemini-cli Gemini CLI personal accounts June 18 2026 announcement` | Official service transition and traffic-policy material. |
| 10 | Official search: `official Gemini CLI quotas Google AI Pro Ultra request limit 2026 site:support.google.com OR site:gemini.google` | Gemini dynamic policy and separate credit policy. |
| 11 | Windsurf/Google: `site:windsurf.com plans usage quotas Windsurf 2026 official` | Official transition and current quota docs. |
| 12 | GitHub/Google: `usage tracker quota monitor site:github.com Cursor Copilot Gemini CLI Windsurf 2026` | OpenUsage, Pulse and tracker candidates. |
| 13 | Google: `quota tracker TiboTattle Cursor Gemini Copilot Windsurf tracker apps` | Quota-tracker, Antigravity extension and TiboTattle candidates; search AI Overview itself not used as evidence. |
| 14 | Direct pages listed in sources.jsonl | Official provider policy pages, selected community pages, and tracker repositories inspected. |

## Coverage and limitations

- This package used systematic query decomposition, Reddit-first search, date filtering, source inspection, and explicit source/query logging, but it did not complete or validate the full Silver Bullet Ultradeep artifact contract. Parent verification confirmed the Silver Bullet skill is accessible through LeanCTX when the repository root is registered in the session and reads use the `repo` selector; the earlier worker's invocation/access limitation was local and should not be generalized. No automated `/sb:deep-research` command or Silver Bullet validators are claimed for this package yet. Its Silver Bullet phase artifacts and three critique cycles remain follow-up work. The separate `ctx_execute` language-dispatch error is recorded independently.
- Search covered public, Google-indexed pages. Private, deleted, unindexed, regional and login-only sources may be absent. This is not a literal exhaustive census.
- Community allowance observations published before 2026-09-05 are labeled discovery-only and are excluded from current figures. Official policy pages are presented separately.
- Many community posts omit exact model/version, effort, plan, workload or full reset window. Those reports remain anecdotes and are not merged into a numeric estimate.
- Tracker README support does not prove that every adapter works against each live account or region.

## Artifacts

- `sources.jsonl`: 39 distinct core source records with type/date/scope and eligibility notes.
- `evidence.jsonl`: 20 core evidence records with method, publication date, measurement interval and eligibility.
- `claims.jsonl`: 14 claims linked to evidence and limitations.
- `run_manifest.json`: scope, date cutoff, search log, degradation and crosswalk validation.
- `community-sources-addendum.jsonl` / `community-evidence-addendum.jsonl`: 21 supplemental source rows and 13 dated evidence rows; the addendum explicitly excludes mixed/pre-cutoff Copilot and Cursor measurements.
- `community-claims-addendum.jsonl`: nine atomic claims linked to each supplemental evidence row, including cutoff, interval, and product-scope exclusions.
