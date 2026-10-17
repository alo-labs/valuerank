# OpenAI / Codex crowd-data source check: TiboTattle

## Access and UI state

- **Accessed:** 2026-10-07 09:01 UTC.
- **Browser:** Codex built-in in-app browser, English UI; direct navigation to the TiboTattle homepage. No external browser, web search, or HTTP client used.
- **Homepage:** [TiboTattle](https://tibotattle.com/)
- **Documentation:** [TiboTattle Docs](https://tibotattle.com/docs.html)
- **Publication disclosure:** [TiboTattle Privacy Overview — Community publication](https://tibotattle.com/privacy#publication)
- **Allowance view selections when checked:** `Aggregate` selected; `By plan` and `By model` inspected separately; `30d` selected and `All` unselected.
- The allowance panel displayed `SHOWING CACHED FIGURES` and: “The service could not be reached, so these are the figures this browser last received, 35.5 hours ago. They are not current, and nothing has been estimated to fill the gap.” The homepage therefore did not provide a live/current estimate at access time.
- The homepage showed download version `0.1.26`, while the Docs introduction refers to version `0.1.24`; this version-reference lag is a documentation caveat for interpreting the explanatory text.
- The expanded “Explore the contribution history” section labeled its series “Delayed, aggregate daily totals from optional contributions.” It also displayed `Reported cause: MUTATION BARRIER ACTIVE`.

## Homepage values visible in the cached 30-day view

The allowance chart heading is `PRO 20X-EQUIVALENT ALLOWANCE`; the unit label is `API-equivalent USD / Pro 20× week`.

| View | Displayed value | Counts and labels visible |
|---|---|---|
| Aggregate | **$1,474 per 7 days, API-price equivalent**; plausible range **$1,310–$2,049** (middle 80% of reset fits) | “Latest published estimate (Sep 28, 2026): from 17 contribution sources, 34 qualifying reset fits in the trailing 30 days.” Chart legend: “Central estimate (median of reset fits)”; “Plausible range (middle 80%)”; “Dot size = reset fits behind the day.” |
| By plan — Plus | **$88**; “Pro 20x-equivalent: $1,760/week” | 5 sources |
| By plan — Pro 5× | **$353**; “Pro 20x-equivalent: $1,413/week” | 8 sources |
| By plan — Pro 20× | **$1,464**; “Pro 20x-equivalent: $1,464/week” | 6 sources |
| By model — GPT-6 Astra | **$1,317** | 2 sources |
| By model — GPT-6 Sol | No published estimate yet | — |
| By model — GPT-6 Luna | No published estimate yet | — |
| By model — GPT-5.6 Terra | **$1,487** | 2 sources |
| By model — GPT-5.6 Sol | **$2,299** | 3 sources |
| By model — GPT-5.6 Luna | **$1,188** | 1 source |

These are displayed summaries, not individual account records. I did not find a per-contributor datapoint, user permalink, or raw usage ledger on the homepage.

## What the homepage and its documentation say the fields mean

- The homepage’s “About these sources” note says a **source is an installation/account track**, not a unique person or verified OpenAI account; separate installations may have overlapping history; source identifiers stay private. Counts can be small, including a single source.
- That note says each allowance point combines qualifying reset fits from the trailing 30 days after normalizing supported personal plans to a Pro 20× equivalent: **Pro ×1, Pro 5× ×4, Plus ×20**. It describes the line as the median and the range as the middle 80%; fits must pass shared calibration gates including a 40-point observed-span floor. Unsupported plans are excluded; late data can republish a day.
- The Docs page explicitly says the `Aggregate`, `By plan`, and `By model` views “compare a full Pro 20x-equivalent weekly allowance at API prices, not each plan's actual allowance or money paid.” It says model estimates appear only when the evidence identifies that model’s rate, and sample counts may be as small as one account.
- In the By model view, the page says the statistic represents “A full Pro 20× week spent on one model, at API prices”; the displayed counts are **contribution sources, not reset fits**. This is a model-at-a-time comparison, not a report showing which models a particular user actually used.
- The publication disclosure says the public view publishes daily activity totals and API-price-equivalent allowance estimates, including plan and model comparisons. It says daily estimates and counts may be based on one source, the daily view has no minimum source count or per-source cap, and plan/model comparisons use closed UTC dates while omitting stale, incomplete, or unstable estimates.
- Plan categories (`Plus`, `Pro 5×`, `Pro 20×`) and model names are visible, but no row-level subscription fee, fee currency, individual tier/model pairing, or direct user measurement is exposed. The `Pro 20×-equivalent` label is a normalized comparison basis, not a subscription price.

## Eligibility decision under ValueRank policy

**Not eligible as a ValueRank numerator or as a per-model, per-plan user-reported allowance observation in its current public form.** The homepage provides API-price-equivalent community estimates based on reported reset-fit evidence, but publishes only aggregate medians/ranges and source counts. It does not expose an individual measured-use datapoint or permalink, an individual’s exact model(s) and tier together, or the matching subscription fee. The docs further qualify the figures as normalized full-Pro-20× comparisons rather than each plan’s actual allowance or amount paid. The cached estimate was also explicitly marked stale at retrieval.

For ValueRank purposes, retain this only as contextual, aggregated TiboTattle evidence with the access date, selected 30-day window, source/fits counts, and stale-cache status above. Do not transfer its model-grouped values to an individual model user or treat its normalized plan comparison as an actual plan allowance or subscription fee.
