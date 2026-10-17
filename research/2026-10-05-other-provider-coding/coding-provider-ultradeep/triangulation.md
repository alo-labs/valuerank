# Triangulation and evidence grading

## Corpus shape

- 22 source records: 8 Reddit threads, 6 official provider documentation pages, 5 tracker repositories, and 3 bounded-search outcome records. The 19 posts/docs/repos are opened direct pages; the three outcome records summarize limited searches and do not function as affirmative usage evidence.
- 14 candidate user observations: 13 eligible observations and one excluded, low-confidence context estimate.
- 6 official provider-policy observations.
- 8 reporter/source clusters are represented by the 13 eligible rows; identity deduplication across different threads cannot be verified.
- 5 named tracker repositories describe account-specific meters or local logs. None of the opened READMEs publishes a public cross-subscriber consumption dataset.

## Provider-by-provider corroboration

| Provider | Eligible report evidence | Published policy/tool context | Assessment |
|---|---|---|---|
| Cursor | Cursor Pro post reports 100% of Cursor Models and 23% of Other Models at end of one day (CP-E01). Cursor Ultra post reports 5% third-party pool use and a separate author's USD 5–7 API equivalent (CP-E02/E03). | Official docs identify separate monthly pools and a live Spending meter (CP-P01). | Policy corroborates what the meter categories mean, not the post's task or cost estimate. Cursor Ultra UI action may contain many API turns, so do not treat “one question” as one request. |
| GitHub Copilot | A commenter with plan `not stated` reports 24,000 of 150,000 monthly credits consumed during migration (CP-E04); a separate author with plan `not stated` reports two generations used the monthly allowance plus almost USD 8 (CP-E05). | Official billing expresses AI credits at USD 0.01 each and states allocations are plan-specific (CP-P02). | The first thread's employer-provided Pro+ / 7,000-credit allowance belongs to the OP, who asks about capacity and reports no actual consumption. Do not transfer Pro+ to the 150,000-credit commenter. |
| Kimi Code | One author with plan `not stated` says the five-hour limit was exhausted within minutes on a small task using the default/basic model (CP-E06). | Official documentation distinguishes new and legacy memberships, rolling five-hour/monthly quota, and legacy weekly quota (CP-P03). | The observed reset window does not identify the user's membership tier. |
| OpenCode Go | One named OpenCode Go user reports a full daily pool at 20% monthly (CP-E07); another Go author reports 12% current month after several heavy coding days, with a previous period's 100% report not separately date-bounded (CP-E08). | Official Go page publishes estimated five-hour requests and model-specific monthly use values (CP-P04). | Reports are account meter snapshots and differ by models/workloads/promotions; they do not establish a typical monthly amount. |
| Ollama Cloud | Grandfathered Pro user reports 724 DeepSeek V4 Flash requests at 60% weekly, then estimates exhaustion near 1,200 requests; a different `Ollama Pro` user reports 36.7% weekly meter after two days plus local OpenCode counters (CP-E09–E13). | Current pricing describes new monthly token credits and migration effects on legacy session/weekly limits (CP-P05). | Tier states and measurement methods differ. CP-E10 is a user extrapolation; CP-E11 is an external API cost-equivalent; CP-E13 is a local log estimate. None is merged into the provider meter. |
| Z.ai / GLM Coding Plan | No eligible individual usage report was verified in the returned in-window results. The Sep 12 `zai-usage` example is explicitly synthetic demo data and excluded. | ZCode docs distinguish local App Usage from remote Coding Plan account meters (CP-P06); third-party apps claim account-level monitoring. | Tool presence does not establish reported quota burn. |
| Windsurf | No eligible Windsurf-plan usage report was verified. A Sep 18 paid Devin report is a different plan and excluded. | No Windsurf allowance record was added from non-user search snippets. | Search outcome only; not evidence that no such report exists. |
| Hacker News | Targeted searches mainly returned June–August 2026 material, outside the cutoff. | Not applicable. | Bounded result set; no exhaustive absence claim. |

## Cross-measurement checks

1. Provider documentation labels official meter windows but does not validate individual reports.
2. Local OpenCode counts and API-cost estimates are kept apart from provider percentage meters.
3. Tracker README features are attributable to maintainers; they are not test results, actual-account screenshots, or aggregate usage evidence.
4. No mean, percentile, “hours per subscription,” or cross-provider normalized burn rate is calculated: tasks, model routing, plan rules, activity windows, and meter definitions differ.
