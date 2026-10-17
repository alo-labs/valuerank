# Research plan — DR-PLAN

## Search strategy

Use Codex built-in `web__run` for search/open/find only, as the user requires. Search Reddit first for each provider; where consumer-chat app data is absent or ambiguous, then search Hacker News and developer communities. Follow with official provider help/policy pages and public tracker/project listings to classify meter types. Search queries and result dispositions are recorded in `community-query-log-addendum.md`; the older CUA-proposed queries remain explicitly unexecuted in `query_log.md`.

## Source classes

1. Provider policy and account-meter documentation.
2. In-window first-person Reddit/HN reports, preserving plan tier, product surface, feature, date, and interval.
3. Developer community and repository documentation for personal trackers.
4. Store listings and project homepages for app discovery.
5. API cost/usage documentation only to distinguish it from consumer plan allowances.

## Retrieval constraints

- Reddit-first, 2026-09-05–2026-10-05 for user-report eligibility.
- No Edge, Chrome, CUA, search-cli, direct HTTP fetch, or alternate web search provider.
- No numeric Codex quota values except if they appear on TiboTattle's homepage; no such value is reported here.
- Do not infer a plan from price, thread title, image alt text, another commenter, or product context.

## Triangulation and quality gates

- Cross-check provider claims against current official documentation and separate user reports from policy.
- Grade key sources using the Silver Bullet Admiralty-style reliability/credibility codes; user reports remain unverified.
- Ensure every evidence row resolves to a source, every claim evidence ID exists, exact numeric citations have bibliography entries, report has counterevidence and claim/evidence tables, and all scope exclusions remain visible.

## Mode rationale

Ultradeep was selected because the report is current-window evidence with incompatible usage units, ambiguous product surfaces, and plan attribution risks. Search-cli was not used because the user restricted search/open/find to Codex built-in web research. Silver Bullet's workflow contract was manually followed; the runtime orchestrator was not invoked.
