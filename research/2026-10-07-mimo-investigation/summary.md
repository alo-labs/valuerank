# MiMo omission and user-reported Token Plan value

Snapshot: October 7, 2026. Models: MiMo V2.6 Pro and V2.6 Flash. Eligible reports: after their September 22 launch through October 7, within the preceding-month window.

## Why the models were omitted

Both exact models are on the displayed [AA Intelligence Index versus total benchmark-cost Pareto line](https://artificialanalysis.ai/models), independently checked using the total-cost axis and both model selections. ValueRank omitted them at ingestion: its 25-model selected AA source roster contains neither identity. `npm run refresh` captures and rebuilds that fixed roster; it does not discover new AA models or reconcile frontier entrants. They never reached the primary ranking's exact DeepSWE/Bug Hunt gate and are absent from its exclusions. A missing-coverage explanation would be unsupported. See [repository audit](omission-audit.md) and [independent verification](retrieval/parent-verification-delta.md).

The repository's own Pareto set compares its weighted quality composite against normalized AA execution cost inside its primary cohort. It does not implement the full AA Intelligence Index/cost frontier. The correction path is to ingest both exact identities, retrieve their current benchmarks, record any actual coverage gaps, and reconcile future AA frontier entrants explicitly.

## Provider-wise allowance findings

| Provider | Plan | Value Multiple | Reference |
|---|---|---|---|
| Xiaomi MiMo | Lite, recurring monthly | **Full allowance multiple not established.** One exact V2.6 Pro personal ledger records $3.400899 of consumed API value in a single day; this is **0.5668× the regular $6 monthly fee**, a partial-use comparison only. Actual paid fee is undisclosed. No qualified Flash value. | [Personal Pro/Lite token ledger](https://github.com/FeiZhuLulu/real-api-pricing/blob/main/data/research/mimo-token-plan-panel-round2-2026-09-23.json), [September 23 publication history](https://github.com/FeiZhuLulu/real-api-pricing/commits/main/data/research/mimo-token-plan-panel-round2-2026-09-23.json), [fee and rate verification](retrieval/parent-verification-delta.md) |
| Xiaomi MiMo | Standard | **Not established** for either exact model; no qualifying personal measured/API-priced allowance located. | [Inspected sources and exclusions](retrieval/user-measurements.md), [Chinese community evidence](retrieval/chinese-user-measurements.md), [parent retrieval delta](retrieval/parent-verification-delta.md) |
| Xiaomi MiMo | Pro | **Not established** for either exact model; no qualifying personal measured/API-priced allowance located. | [Inspected sources and exclusions](retrieval/user-measurements.md), [Chinese community evidence](retrieval/chinese-user-measurements.md), [parent retrieval delta](retrieval/parent-verification-delta.md) |
| Xiaomi MiMo | Max | **Not established** for either exact model; no qualifying personal measured/API-priced allowance located. | [Inspected sources and exclusions](retrieval/user-measurements.md), [Chinese community evidence](retrieval/chinese-user-measurements.md), [parent retrieval delta](retrieval/parent-verification-delta.md) |

Unknown allowance is not zero. These rows are not added to the current numeric provider ranking as comparable monthly allowances.

## Reproducible partial-use calculation

The maintainer reports their own **Lite recurring monthly / mimo-v2.6-pro** account; collection and first public commit September 23; measured usage day September 22. Their ledger has 73,716,343 tokens. [Xiaomi's published API rates](https://mimo.mi.com/) value these actual reported token categories:

| Category | Reported tokens | USD per million tokens | API-priced value |
|---|---:|---:|---:|
| Cached input | 67,848,448 | $0.0036 | $0.2442544128 |
| Fresh input | 4,479,135 | $0.435 | $1.9484237250 |
| Output | 1,388,760 | $0.87 | $1.2082212000 |
| Total | 73,716,343 | — | **$3.4008993378** |

`$3.4008993378 ÷ $6 regular monthly Lite fee = 0.5668165563×`.

The [regular Lite monthly fee](https://platform.xiaomimimo.com/token-plan) is verified, but the user's paid price and discount are not published. The source reports 53.43% credit consumption; scaling the day's value to 100% would produce approximately 1.06×. That is an extrapolation, not actual measured full allowance, and is excluded from the allowance table's numeric comparisons. The report was published after launch; within-day ordering on September 22 is not independently established because the launch and ledger do not expose exact timestamps. Referenced account screenshots are not included in the inspected public file.

## Research and exclusions

Silver Bullet Deep Research, **Ultradeep**, uses the actual authorized workflow with nine phase artifacts, source/evidence/claim records, and three critique rounds in [the research package](allowance-ultradeep/research_report.md). Retrieval covers twelve executed focused search angles across Reddit, Hacker News, GitHub, Linux.do, V2EX, NodeSeek and X, plus direct tracker and author-comment follow-ups. This is a bounded public-source search, not an exhaustive no-hit proof.

- Reddit's all-tier Pro/Flash table prices published quotas. Its author does not disclose a purchased tier or consumed dollar numerator; it is excluded.
- A $5 Lite experience post calls its approximately 1× interpretation speculation and supplies no API-priced ledger; it is excluded.
- The maintainer's second client sample has an unidentified exact model and no tier; it cannot supply a Flash observation or independent user replication.
- Third-party OpenCode Go/CommandCode reports remain separate from Xiaomi Token Plan.
- The linked pricing tracker uses credit pools and assumed request patterns; its approximately 0.99–1.19× figures are excluded from user-measured allowance.
- Public local tracking tools may help users collect future evidence. Their existence does not supply a plan-tier allowance measurement.

The ranking omission is diagnosed; this investigation has not modified or republished ranking data.
