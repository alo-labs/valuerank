# OpenAI/Codex TiboTattle follow-up

**Audit date:** 2026-10-06 (Australia/Sydney)  
**Measurement window required for user reports:** 2026-09-06 through 2026-10-06, inclusive  
**Purpose:** Recheck the existing OpenAI/Codex coverage decision, identify any material omission in direct app evidence, and document the search boundary.

## Finding

The current [OpenAI/Codex eligibility audit](openai-tibotattle-eligibility.md) records the [TiboTattle homepage](https://tibotattle.com/) as the permitted community numeric source, but its aggregate is retained as context rather than an eligible actual per-plan measurement. It says that on Oct 6 the page displayed a **30d / By plan** chart with activity through **Oct 4**, labeled **“API-equivalent USD / Pro 20x week”**:

| TiboTattle plan group | Amount recorded in the Oct 6 audit (USD / Pro 20x-equivalent week) | Source tracks |
|---|---:|---:|
| Plus | $88 | 5 |
| Pro 5x | $353 | 8 |
| Pro 20x | $1,464 | 6 |

These are TiboTattle’s plan-group aggregates, not individual user reports. The Oct 6 audit says the page exposed no contributor permalink or source-level date interval, fee, token/model mix, or model attribution. Its source counts are installation/account tracks, may overlap, and are not a count of unique people. The audit also notes that the API-price calculation cannot be independently reconstructed from the page.

**No OpenAI/Codex user report in the reviewed material meets the requested report-level fields for Sep 6–Oct 6.** The aggregate’s selected 30-day view and latest activity date do not provide a dated interval for any one contributor. Its plan-group labels do not establish a contributor’s exact paid tier or fee. Therefore the aggregate is useful only as source-labeled context. It cannot support an individual Value Multiple or a numerator for any ranked OpenAI model. Provider-published caps, quotas, and allowance multiples remain ineligible as user-measured numerators.

The [model-coverage CSV](model-coverage.csv) correctly repeats the same aggregate context for OpenAI rows, marks exact-variant attribution unavailable, and does not assign a ranked-model numerator. The [coverage summary](model-coverage.md) states that OpenAI numeric community evidence comes only from the TiboTattle homepage. No material change to that eligibility decision is warranted from the local records reviewed here.

## Parent IAB verification, 2026-10-06

In the parent task's Codex in-app browser, I reopened the [TiboTattle homepage](https://tibotattle.com/) and confirmed the Oct 6 30d / By plan amounts and source counts. I opened the [TiboTattle documentation](https://tibotattle.com/docs), which states that all three charts compare a full Pro 20x-equivalent weekly allowance at API prices, not each plan's actual allowance or money paid. The [publication disclosure](https://tibotattle.com/privacy#publication) says daily plan/model estimates may be based on a single source. Under the strict actual-user-measured, API-priced rule, the homepage aggregate remains context only and does not support an OpenAI plan Value Multiple.

## Direct app evidence already documented

The Oct 5 TiboTattle audit contains a bounded inventory of 11 products: TiboTattle plus ten adjacent usage-monitor or tracker apps. It cites direct publisher pages, documentation, repositories, or official app listings for product discovery and publisher-described methods. Those pages establish product features only; the previous audit found no evidence in the reviewed alternative-app sources of a public Codex quota aggregate comparable to TiboTattle’s. They are not numeric allowance evidence and must not be substituted for TiboTattle data.

| Product | Direct product evidence recorded in the Oct 5 audit | Use boundary |
|---|---|---|
| TiboTattle | [Homepage](https://tibotattle.com/), [documentation](https://tibotattle.com/docs), [privacy](https://tibotattle.com/privacy), [repository](https://github.com/adamallcock/tibotattle) | Homepage only for OpenAI/Codex numeric crowd aggregates; no contributor permalink was recorded. |
| OpenUsage | [Product site](https://www.openusage.ai/), [Codex provider guide](https://github.com/robinebers/openusage/blob/main/docs/providers/codex.md), [privacy](https://github.com/robinebers/openusage/blob/main/docs/privacy.md) | Publisher-described account signal and local estimates; no numeric crowd aggregate. |
| CodexBar | [Repository](https://github.com/steipete/CodexBar), [provider documentation](https://github.com/steipete/CodexBar/blob/main/docs/providers.md) | Account-specific/local tracking description; not crowd evidence. |
| CUStats | [Mac App Store listing](https://apps.apple.com/us/app/custats-ai-usage-tracker/id6756333957?mt=12) | Listing-level product evidence; no crowd aggregate. |
| SessionWatcher | [Codex product page](https://sessionwatcher.com/codex), [homepage](https://sessionwatcher.com/) | Publisher-described personal/local tracking; not crowd evidence. |
| AIUsage | [Repository](https://github.com/sylearn/AIUsage), [usage and billing methodology](https://github.com/sylearn/AIUsage/blob/main/docs/USAGE_AND_BILLING.md) | Publisher-described proxy/log pricing; not account-quota crowd evidence. |
| ccusage | [Repository](https://github.com/ccusage/ccusage) | Local usage reporting; not an account-level quota aggregate. |
| VibeCheck | [Mac App Store listing](https://apps.apple.com/us/app/vibecheck-limits-companion/id6759708342) | Publisher listing; no crowd aggregate. |
| Model Usage | [Mac App Store listing](https://apps.apple.com/us/app/model-usage/id6761831599) | Publisher listing; no crowd aggregate. |
| TokenBar Mobile | [App Store listing](https://apps.apple.com/us/app/tokenbar-mobile/id6760548040) | Adjacent product discovery; no Codex crowd aggregate established. |
| Codexex | [App Store listing](https://apps.apple.com/us/app/codexex/id6762058457) | Account-specific companion description; not crowd evidence. |

This inventory is inherited from the Oct 5 report; none of these product pages was newly opened or revalidated during this follow-up.

## Query and search log

### This follow-up

- **Local artifact review:** Read the Oct 5 TiboTattle report and query log, the Oct 6 TiboTattle eligibility audit, the Oct 6 model-coverage summary, and the first OpenAI rows of the model-coverage CSV.
- **IAB availability check:** Attempted a direct IAB navigation to [https://tibotattle.com/](https://tibotattle.com/). The browser returned “IAB visibility is not supported in a subagent thread” before the page loaded. Per the required source rule, external browsing stopped there.
- **External search queries run in this follow-up:** None. No search-engine result, app listing, or external page was inspected in this follow-up.

### Historical searches in the Oct 5 TiboTattle audit

The existing [query log](../../2026-10-05-tibotattle-openai/query_log.md) records these searches; they are historical and were **not rerun** here:

- `site:tibotattle.com Codex allowance estimates`
- `"TiboTattle" Codex Reddit OR Hacker News OR community post`
- `TiboTattle Codex tracker launch post`
- `"TiboTattle" "Codex"`

That prior audit records direct opens of the TiboTattle homepage, docs, privacy overview, and repository, plus the product sources listed above. It describes its product discovery set as bounded, not a census.

## Limits and disposition

- I could not independently re-open the homepage or validate whether its chart changed after the observation recorded on Oct 6. Treat the figures above as transcribed from the existing dated audit, not a fresh live observation.
- IAB navigation is unavailable in this subagent context. I stopped external browsing as instructed; I did not switch to another browser, `web__run`, direct HTTP, or app usage data.
- The required Silver Bullet Ultradeep skill file is outside the active ValueRank read root. LeanCTX blocked the read; registering the Silver Bullet repository as a search root did not enable file reads. The Ultradeep workflow therefore could not be independently read or newly applied in this follow-up.
- The existing Oct 5 app inventory provides direct publisher-source references, but they were not revalidated today. This follow-up cannot claim comprehensive current app coverage or a public-web no-hit.
- No individual OpenAI/Codex report with an in-window measured interval, exact user tier, report date/window, and direct contributor source is added. The homepage’s plan-grouped aggregate remains context only, and no Value Multiple is calculated.
