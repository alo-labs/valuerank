# Plan value-multiple application — October 8, 2026

The Plan route snapshot in `.refresh/v1.4/plan_cost_routes.json` now applies the latest [October 7 provider-wise research](2026-10-07-provider-wise-user-reported-value-multiples.md) and [selected SemiAnalysis source update](2026-10-07-semianalysis-subscription-update.md). The snapshot is dated October 8. It contains nine eligible routes, fourteen preserved historical/excluded routes, and five provider-level evidence records that do not attach a numerator to an unsupported ranked model variant.

This note records the route-data changes. Ranking generation, helper/UI behavior and publication belong to the parent task and require their own execution evidence.

## Applied routes

| Model scope | Plan | Monthly fee | Applied value multiple | Original evaluated model / evidence |
|---|---|---:|---:|---|
| All six current GPT model IDs | ChatGPT Plus | $20 | 8.10× | GPT-6 Astra; user-authorized common application |
| All six current GPT model IDs | ChatGPT Pro 100 | $100 | 10.55× | GPT-6.1 Sol; user-authorized common application |
| All six current GPT model IDs | ChatGPT Pro 200 | $200 | 10.42× | GPT-6.1 Sol; user-authorized common application |
| All six current GPT model IDs | ChatGPT Pro 500 | $500 | 10.772× | GPT-6.1 Sol; user-authorized common application |
| `claude-opus-5-5` only | Claude Pro | $20 | 58.90× | Opus 5.5; controlled account measurements with workload projection |
| `claude-opus-5-5` only | Claude Max 5x | $100 | 57.25× | Opus 5.5; controlled account measurements with workload projection |
| `claude-opus-5-5` only | Claude Max 20x | $200 | 58.63× | Opus 5.5; controlled account measurements with workload projection |
| `grok-4.7`, required XHigh variant | SuperGrok Heavy | $300, account owner reported | ≈5.79× (stored 5.785×) | Grok 4.7 XHigh; account receipts and partial-interval projection |
| `mimo-v2-6-pro` and `mimo-v2-6-flash` | Provisional MiMo assumption | Unavailable | 1.50× | User assumption; no measured numerator or public plan source |

The shared GPT scope comprises `gpt-6-astra`, `gpt-5.6-sol`, `gpt-5.6-luna`, `gpt-5.5`, `gpt-6-sol` and `gpt-6-luna`. The user explicitly authorized the same ChatGPT plan multiples for all GPT models. ValueRank selected the conservative lower reported conditional figure for each plan as its stated implementation assumption: Astra for Plus and GPT-6.1 Sol for the three Pro tiers. The broader model scope is user-authorized; the user did not expressly select this numerical column. It is labeled `user_assumption`, `provisional`, and `user-authorized cross-model application`. The current roster has no GPT-6.1 Sol row; the source variant remains in metadata and is not silently renamed to GPT-6 Sol. Every current GPT row therefore has the same candidate set, whose highest multiple is Pro $500 at 10.772×.

The source for the seven Anthropic/OpenAI routes is [SemiAnalysis, published October 6, 2026](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x), expressly selected by the user on October 7. Its controlled subscription-account measurements with agentic workload projections are the authorized exception to the default API-priced end-user report rule. All thirteen original chart figures, including both GPT variants and Fable 5.1, remain in `sourceEvidence.semianalysis.modelConditionalFigures`. GPT route `apiEquivalentUsd` is labeled an applied estimate for the broader model scope; it does not claim that every GPT variant was measured.

SemiAnalysis's monthly projection already has a monthly time basis: divide the chart amount by the matched monthly fee once. The source agentic workload is 0.4% fresh input, 96.6% cached input, 2.6% cache writes and 0.3% output; rounded shares sum to 99.9%. These shares differ from ValueRank's retained billed-3 task-cost mix. Applying a capacity multiple to task cost is an estimate, not an independent workload-specific allowance measurement. The source reports a roughly ±5% rate-estimation target; rounded chart labels and arithmetic decimals do not establish additional precision. Exact experiment timestamps and complete public token ledgers are unavailable, so the route measurement interval is null and explicitly qualified. Current Codex figures use the post-September 29 allocation regime. Eligible pre-cut Pro $200 accounts retaining older allowances until October 29 are outside this current column.

For Opus 5.5, Claude Pro's 58.90× is numerically highest among the three tiers. No Opus estimate transfers to Opus 5, Opus 4.8, Fable 5, Sonnet 5 or another unsupported Claude variant. The Fable 5.1 Max estimates remain provider-level because the ranked Fable model is 5.0. Their 50% shared weekly-pool allocation is an alternative model allocation and must not be added to the all-Opus projection.

The [SuperGrok Heavy September 25 experiment](https://www.remakebench.com/capacity/plans/supergrok-heavy) matches ranked Grok 4.7 XHigh. Calibration covers September 23–25 and uses $76.09728984 in deduplicated API-equivalent receipts as the meter rises from 56% to 75%. The source projects approximately $400.5/week: `$400.5 × 52 ÷ 12 ÷ $300 = 5.785×`. The overall experiment reports $124.85507688 across seventeen runs. The monthly numerator is projected capacity, not full-month consumption. Shared product pools, possible unlogged activity, interrupted runs and un-reproduced linked receipt files keep confidence low. The $300 fee is account-owner reported. The route also records `requiredVariant: xhigh`; it does not support ranked Grok 4.6 Medium.

The MiMo instruction establishes only a provisional 1.5× multiplier for the two MiMo candidate variants. Both `planPriceUsd` and `apiEquivalentUsd` are null. No fee, measured consumption, plan tier, benchmark claim or public source URL is invented. Its source reference is the user's October 8 instruction in this chat. A provisional cost assumption does not supply missing quality benchmark evidence or make a candidate eligible for a complete ranking.

## Evidence retained without exact-model application

| Evidence | Publication and measurement window | Reason it remains provider-level |
|---|---|---|
| [Standard SuperGrok local-account estimate](https://modeldial.com/en/subscriptions/grok), ≈6.54× | Page updated Oct 2; Sep 23 sample at 30% weekly meter | Grok 4.7 thinking effort unspecified. Raw sample dollars and token ledger unpublished. [xAI pricing](https://x.ai/pricing) supports the $30 denominator only. |
| [Z.AI Lite mixed-model report](https://www.reddit.com/r/ZaiGLM/comments/1wstrqy/lite_plan_18mo_gave_me_102_of_api_usage_568x_a_1/), ≈5.68× | Posted approximately Sep 29; Aug 29–Sep 29 measurement | GLM 5.3 and GLM 5.3 Flash usage is not split by model. User-estimated $102.17 ÷ owner-stated $18. Token-price ledger cannot be independently reproduced. |
| [Old Kimi Allegretto K3-256 report](https://www.reddit.com/r/kimi/comments/1wqjghr/i_just_measured_kimi_quota_for_coding_on/), ≈4.0× | Posted Sep 27; five-hour session, exact session date unspecified | K3-256 differs from ranked standard K3. $7.20 at 20% weekly meter projects $36/week; `$36 × 52 ÷ 12 ÷ $39 = 4×`. |
| Fable 5.1 Max 5x, 12.73× | [SemiAnalysis Oct 6](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x); exact experiment interval unavailable | No exact ranked Fable 5.1 variant; 50% shared-pool allocation. |
| Fable 5.1 Max 20x, 12.425× | [SemiAnalysis Oct 6](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x); exact experiment interval unavailable | No exact ranked Fable 5.1 variant; 50% shared-pool allocation. |

The October 8 reporting window is September 8–October 8. The Z.AI whole-period report crosses the start boundary and does not isolate outside-window use; it remains explicitly qualified at provider level with the complete interval. No precision is invented for the approximate Z.AI publication date or Kimi session date.

## Preserved exclusions and interface requirements

All fourteen prior route objects retain their original figures, model IDs, source URLs and notes under `excludedRoutes`, with `excludedOn` and a specific reason. This includes three old ChatGPT routes, unsupported Claude 40× high-water evidence, Kimi Vivace scaling, three modeled Google routes, two provider-credit-derived Z.AI routes, Ollama published-credit allowance and three OpenCode internal-usage allocations. None are eligible Plan routes: provider quotas/credit marketing cannot supply the numerator, unsupported model variants cannot inherit another variant's result, and the old ChatGPT evidence is superseded for this selected comparison. Models without an eligible supported route use the existing API fallback.

The route schema retains `planPriceUsd` and `apiEquivalentUsd`. The helper and emitter should preserve `evidenceClass`, `sourceEvidenceClass`, `provisional`, `numeratorKind`, `sourceModel`, source publication date and allocation regime. A null MiMo fee or numerator must render as unavailable. GPT and MiMo routes need visible provisional-assumption wording; SemiAnalysis needs controlled-account/workload-projection wording and the selected-source exception. Grok route matching should respect its required XHigh effort. Keeping all four GPT plans in the candidate table makes the common selection reviewable. Future GPT roster additions need the same explicit policy applied or model IDs refreshed; current coverage is the six IDs above.

## Scope of verification

This update used the existing local source reports and current roster information supplied by the parent. It did not perform new network research or run tests. The parent independently validates the final JSON against source reports and regenerates/reviews the ranking and site outputs before any completion/publication claim.

### Parent integration record

The v1.9.5 scoring, AA reconciliation and publication builds succeeded. Independent parsing of the generated 13-model ranking data confirmed the shared 10.772× selected GPT route, Opus 5.5's 58.9× route, Grok 4.7 XHigh's 5.785× route, and no changes to API-mode primary ranks or scores. The generated all-candidate Plan comparison retains both unranked MiMo models at 1.5×: Flash $72.94 and Pro $137.77, with unknown fees and unmeasured allowance numerators. Rounded AA intelligence labels preserve source precision. The route helper enforces required evaluated variants, and unavailable plan costs cannot be rendered as zero. No tests were run. Publication and live-browser confirmation are reported in the completion response.
