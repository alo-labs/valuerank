# Research plan (DR-PLAN)

## Mode rationale

Mode `deep`: the output feeds a value ranking that publishes dollar-per-window figures, the evidence conflicts across observers (for example Pro 5h readings from $14 to $200), and two prior stages already exist. Two critique cycles are run (`critique.md`).

## Source classes

| Class | Use | Examples |
|---|---|---|
| Primary user report with ledger | Qualifying numerator | GitHub issue comments with token tables, aiplans JSON ledgers, forum posts with raw counters |
| Primary user report, summary only | Provisional | Reddit comments quoting ccusage totals |
| Secondary aggregator or blog | Cross-check, change signals | ooo.run blog, aiplans guides, locdd quotes |
| Provider documentation | Change detection only, never the numerator | antigravity.google/docs/plans |

## Search strategy

1. Re-read every stage-1 and stage-2 candidate that qualified or nearly qualified, from the primary page, and recompute the dollar arithmetic independently.
2. Sweep for reports the earlier stages missed:
   - Reddit comments by day, 2026-10-19 .. 2026-11-05, in r/ClaudeAI and r/ClaudeCode (keywords ccusage, equivalent, API, Opus) and 2026-10-26 .. 2026-11-05 in r/codex, r/google_antigravity, r/GeminiAI, r/kimi, r/MiniMax_AI, r/XiaomiMiMo (keywords tokens, cached, weekly, 5h); filtered for dollar, token and percentage content.
   - Hacker News comments and stories since 2026-10-19 for 17 plan and provider queries.
   - GitHub issue pages (anthropics/claude-code, openai/codex) through rendered pages, including the issues listing created after 2026-11-01.
   - Google AI developer forum: search for Argon quota topics, then raw posts.
   - locdd.com (LINUX DO mirror): 26 search queries, 38 recent topics read, and the original LINUX DO topic 3071240 where directly readable.
   - V2EX: 8 queries through sov2ex and the topic API.
   - aiplans.dev sitemap and report paths for newer reports.
3. For change detection: provider documentation pages and changelogs (Antigravity), third-party blog claims, and cross-observer dispersion.
4. Triangulate: for each cell, list reports with partition, entrypoint, model purity, and price basis; apply the O11 margin test.

## Provider manifest

`search-cli`: not installed. Fallback: host WebSearch (US-only, 6 calls, low yield) and WebFetch plus direct fetches. Missing provider classes (recorded per the skill): no Exa-style semantic search, no X search, no YouTube, no Zhihu.

## Blocked or constrained venues (recorded, not worked around)

- linux.do search and latest endpoints: Cloudflare "Just a moment" challenge. Not automated. (One topic JSON, 3071240, returned content on a plain request and was used.)
- GitHub REST/GraphQL for openai/codex and anthropics/claude-code: repository not enabled for this session. Issue pages were read through WebFetch.
- A reader-proxy fetch of GitHub (a third-party rendering service) was refused by the permission layer and not retried.
- X search: no login; only posts linked from other pages.
- Arctic Shift: 100-result cap per query and intermittent 422/timeouts; daily slicing used.

## Validation plan

`validate_report.py`, `verify_citations.py`, `verify_claim_support.py`, and `phase_gate.py --mode deep` against this directory; up to 3 repair loops.
