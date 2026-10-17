# Decision record

| ID | Decision | Reason |
|---|---|---|
| D1 | Include user reports only when the post or comment is dated 2026-09-05 through 2026-10-05. | Matches the requested window. |
| D2 | Store plan tier as explicitly named or `not stated`; do not infer from usage window or tier policy. | Prevents plan assignment errors, especially Copilot comments and Kimi legacy/new plans. |
| D3 | Separate account meters, published quota policy, local logs, user extrapolations, and API-cost equivalents. | These quantities have different denominators and provenance. |
| D4 | Keep CP-E14 out of eligible evidence and all quantitative claims. | The original post's rough Hermes estimate has no stated plan, meter, defined window, or reproducible method. |
| D5 | Exclude out-of-window HN results, unrelated Devin usage, and synthetic tracker demo values. | They do not answer the in-window plan-usage question. |
| D6 | Treat absence of Windsurf/Z.ai/HN usage anecdotes as a bounded search result. | Search-return coverage is not exhaustive. |
| D7 | Do not compute a provider ranking, typical monthly burn, or cost multiple. | Sample, tasks, plans, models, and measurement surfaces are not comparable. |
| D8 | Apply the Silver Bullet Ultradeep nine-phase artifacts manually and document no command invocation. | Skill/workflow were available, but an actual `/sb ultradeep` orchestration invocation is not in the execution record. |
