> **Historical snapshot:** This 2026-10-05 index is superseded by the [2026-10-06 allowance research index](2026-10-06-allowance-research-index.md). Use the newer table and current-month eligibility rule.

# AI subscription allowance research index

**Research snapshot:** 5 October 2026 (UTC)  
**Eligible community-report publication window:** 5 September–5 October 2026, inclusive.

## Requested comparative deliverable

The requested output is a provider-wise table of individual qualifying end-user-reported value multiples. Use exactly these columns: **Provider, Plan, Value Multiple, Reference**. Group rows by provider and sort provider groups by each provider's highest qualifying in-window multiple; sort datapoints high to low within a provider. Every Reference links directly to the individual source datapoint. Use end-user account, transcript, or log reports for allowance numerators; provider-published allowance or marketing claims are not eligible. Published plan fees and API prices may support the fee denominator or a clearly labeled conversion. Keep reports within the stated one-month window, identify the exact plan tier (or say when it is inferred/not stated), and label partial periods and estimates. Preserve separate observations rather than averaging them into a provider score.

## Cutoff and evidence rules

- Community allowance reports published before 5 September 2026 are retained only as discovery/history and do not support current allowance estimates.
- A report published inside the window is used as current measurement evidence only when its measurement interval is also inside the window or a post-cutoff segment can be isolated. Mixed or unclear intervals are explicitly excluded from numeric current estimates.
- Current provider policy pages and app documentation are reported separately as policy/discovery context. Their retrieval date does not turn them into allowance measurements.
- Keep plan, product surface, model/action, publication date, measurement interval, reset window, currency/unit, and source type attached to every claim. Do not convert percent meters, API-price equivalents, points, credits, or account anecdotes into a universal allowance.
- For OpenAI Codex, numerical crowdsourced claims are restricted to the TiboTattle app homepage. Other sites and projects are used only to identify comparable tools, not as Codex allowance sources.

## Packages

| Topic | Primary report | Evidence and notes |
|---|---|---|
| Claude plans and trackers | [Claude current-month report](2026-10-05-claude-plan-allowance-ultradeep/current-month/report.md) | [Scope](2026-10-05-claude-plan-allowance-ultradeep/current-month/scope.md), [query log](2026-10-05-claude-plan-allowance-ultradeep/current-month/query_log.md), and current-month source/evidence/claim ledgers in the same folder. The old package-level report and ledgers remain historical audit material; do not use pre-cutoff reports in current estimates. |
| OpenAI Codex and TiboTattle | [TiboTattle research](2026-10-05-tibotattle-openai/report.md) | Codex allowance evidence uses only the TiboTattle homepage. The checked page showed a loading/checking state without a usable crowd estimate; no numerical Codex allowance is inferred from other sources. Other tracker apps are discovery-only. |
| Other chat providers | [Chat allowance report](2026-10-05-other-provider-chat/report.md) and [current-month community addendum](2026-10-05-other-provider-chat/community-research-addendum.md) | Covers Perplexity, Grok, Mistral Le Chat, DeepSeek, Poe, and Meta AI; the supplemental search adds provider-specific Reddit-first queries and Hacker News/developer app research. Several account-level figures are retained as unverified claims; none provides a reproducible, normalized cross-account allowance. |
| Coding-agent subscriptions and trackers | [Coding-provider Ultradeep supplement](2026-10-05-other-provider-coding/coding-provider-ultradeep/research_report.md), [prior provider report](2026-10-05-other-provider-coding/report.md), and [community addendum](2026-10-05-other-provider-coding/community-research-addendum.md) | The current-window supplement contains 13 eligible user observations, one excluded context observation, six provider-policy records, and 47 retained query strings. It separates provider meters, extrapolations, local logs, and API-cost comparisons. The [canonical evidence ledger](2026-10-05-other-provider-coding/coding-provider-ultradeep/evidence.jsonl) now records each user row's exact tier or `not stated`, reporter, and source crosswalk. No typical-use rate or provider ranking is supported; HN, Windsurf-only, and Z.ai/GLM non-findings are bounded to returned searches. |
| Provider-wise user-reported value multiples | [End-user-reported plan multiples table](2026-10-05-provider-wise-user-reported-value-multiples.md) | Includes the selected user-reported datapoints, with provider groups sorted by their highest included in-window multiple. User account data supplies the allowance numerator; provider-published allowance/marketing multiples are excluded. Derived and partial-period estimates, plan-fee assumptions, and non-qualifying reports are labeled. |
| Supplemental model subscription/API-equivalent comparison | [25-model plan-tier table](2026-10-05-subscription-api-equivalent-table/table.md) and [method/results report](2026-10-05-subscription-api-equivalent-table/research_report.md) | Retained as supporting research, not the requested comparative deliverable. It covers all 25 roster IDs and 60 priced plan-tier records across OpenCode, Ollama, and Z.AI; routes are the best quantified among evidenced candidates, not a full vendor-market census. |

## Synthesis

The inspected provider documentation generally publishes qualitative limits, model/action-specific credits or account meters rather than comparable plan-wide token allowances. Recent community reports include plan-specific anecdotes, partial observation windows, API-equivalent cost calculations, and disputed account figures. These support questions for future controlled measurement, not a universal “value multiple.”

Tracker discovery found several personal quota readers and local usage dashboards. Claude Tuner is the clearest discovered Claude-side public aggregation candidate, but its current statistics page returned placeholders during the check. TiboTattle is the only source used for Codex crowdsourced allowance data, and it did not expose a usable number at retrieval. No other independently verifiable provider-wide crowd dataset was established in these bounded searches.

## Research limitations

The built-in web research route was used; external browsers were not used. The Silver Bullet Deep Research Ultradeep workflow was accessible and used; package-level nine-phase gates passed, with three critique cycles recorded in each applicable report. No native `/sb:deep-research` orchestration command was exposed in this task surface, so the documented workflow was run through its project artifacts and validation gates. Separate LeanCTX routing or sandbox execution limits did not indicate a Silver Bullet workflow failure. The Claude, TiboTattle, other-chat-provider, coding-provider, and model/API-equivalent packages have completed report, citation, claim-support, and phase-gate validation as documented in their package logs. Searches cover indexed public material and cannot establish literal absence of private, deleted, regional, login-gated, or differently worded reports. App privacy, security, and live adapter behavior were not independently audited.
