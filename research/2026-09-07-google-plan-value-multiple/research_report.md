# Google Gemini subscription Value Multiple

Date: 2026-09-07

## Executive Summary

ValueRank now models the current Google coding-plan routes as three tiers for the
same Gemini cohort. The selected highest-value route is the $199.99 AI Ultra
20x-quota tier at a ValueRank-derived 10.6x multiple. The estimate is explicitly
low confidence because Google publishes relative quota, not a fixed API-dollar
allowance. The report keeps the modeled range and confidence label visible so the
UI can show the estimate without implying a provider guarantee.

## Introduction

The site's Plan Costs view needs an effective cost for Gemini models that reflects
the subsidy embedded in a paid coding subscription. The research question is
therefore not “what is the sticker price?” but “how much API-priced Gemini work
does each plan tier represent per dollar of subscription price?” This supplement
covers the four Gemini IDs in the current ValueRank cohort and preserves API
Costs as the unchanged fallback and comparison basis.

## Main Analysis

Google's [current consumer subscription page](https://gemini.google/us/subscriptions/?hl=en)
lists AI Pro at $19.99/month, AI Ultra at $99.99/month with 5x the Pro usage
limits, and AI Ultra at $199.99/month with 20x the Pro usage limits. Google's
[Gemini Apps limits documentation](https://support.google.com/gemini/answer/16275805)
lists Gemini Flash and Pro access for both Pro and Ultra, while the
[Antigravity plan-change announcement](https://antigravity.google/blog/changes-to-antigravity-plans)
describes the coding-agent quota as shared across models and drawn down using
API-pricing-relative token economics.
[1][2][3]

The [Antigravity plans documentation](https://antigravity.google/docs/plans)
adds the operational caveat: limits refresh on five-hour and weekly windows,
usage depends on the work performed, and quotas may change. Google therefore
does not provide the fixed monthly token-dollar pool needed for an exact
subscription subsidy factor. The [Gemini API pricing page](https://ai.google.dev/gemini-api/docs/pricing)
remains the API list-price reference used by ValueRank for the underlying task
costs.
[4][5]

The strongest current public absolute estimate found was 5dive's
[Token Maxxing Gemini AI Pro model](https://5dive.ai/tokenmaxxing): a modeled
3.0x-9.5x range with a 5.3x headline estimate. It is a community model rather
than provider billing telemetry, so ValueRank records it as low confidence.
The current prices and relative tiers are independently cross-checked by
[AgentPlans](https://agentplans.fyi/compare/google/) and
[RoninForge's Pro-versus-Ultra analysis](https://roninforge.org/antigravity-credits/pro-vs-ultra/),
but neither publishes a stronger absolute token-dollar measurement.
[9][10][11]

### Route calculation

| Route | Monthly price | Google-published quota relative to Pro | ValueRank multiple | Modeled API-equivalent value | Confidence |
| --- | ---: | ---: | ---: | ---: | --- |
| Google AI Pro | $19.99 | 1x | 5.3x | $105.95 | Low |
| Google AI Ultra, 5x quota tier | $99.99 | 5x | 5.3x | $529.95 | Low |
| Google AI Ultra, 20x quota tier | $199.99 | 20x | 10.6x | $2,119.89 | Low |

Using the Pro baseline and preserving quota-per-dollar economics:

```text
Pro       = 5.3x
Ultra 5x  = 5.3 × [5 ÷ ($99.99 ÷ $19.99)] ≈ 5.3x
Ultra 20x = 5.3 × [20 ÷ ($199.99 ÷ $19.99)] ≈ 10.6x
```

The modeled sensitivity range is 3.0x-9.5x for Pro and the 5x tier, and
approximately 6.0x-19.0x for the 20x tier. The API-equivalent values are plan
price multiplied by the selected Value Multiple; they are normalization values
for the site's cost model, not a promise that Google will serve exactly that
many dollars of API tokens.

## Claims-Evidence Table

| Claim | Evidence | Treatment |
| --- | --- | --- |
| Google exposes $19.99 Pro, $99.99 Ultra 5x, and $199.99 Ultra 20x tiers | Official subscription, limits, and Antigravity pages [1][2][3] | Supported fact |
| No fixed API-dollar allowance is published | Antigravity documentation plus community quota analysis [4][11][12] | Supported limitation |
| Pro baseline is 5.3x with a 3.0x-9.5x modeled range | 5dive Token Maxxing [9] | Community model, low confidence |
| Ultra route multiples are 5.3x and 10.6x | Official relative tiers combined with the Pro model [1][3][9] | ValueRank derivation |

## Counterevidence Register

- AgentPlans presents an approximately equal 5.5x estimate across Google tiers
  [10]. It is retained as a cross-check but not adopted because it does not
  preserve the published 5x/20x quota-per-price distinction required for tiered
  subsidy modeling.
- Community posts report different absolute quota experiences. They are not
  promoted to the baseline because Google says usage varies by task and window
  [2][4].
- Google Developer Program credits are a separate API/Cloud credit benefit [6],
  not evidence of the embedded Antigravity quota, so they remain excluded.

## Synthesis

The 20x quota tier is the highest-subsidized route and is therefore the route
selected by default for every Gemini model currently in the ValueRank cohort.
The $99.99 tier has more absolute headroom than Pro, but its roughly 5x price
matches its 5x relative quota, so it does not improve the modeled value per
dollar. The $199.99 tier is different: its 20x quota is about 10x the Pro
price, producing roughly twice the per-dollar multiple of the lower tiers.

This result is a ValueRank inference from a modeled Pro baseline plus official
relative quota disclosures. It should not be presented as a Google-published
10.6x guarantee, and it should be refreshed when Google changes prices, quota
rules, or the coding surface.
[7][8]

## Limitations

- The route covers the four Gemini model IDs in the current ValueRank cohort:
  `gemini-3.8-flash`, `gemini-3.7-flash`, `gemini-3.6-flash`, and
  `gemini-3.5-flash`.
- The route uses the current coding surface (Antigravity) after Google's June
  2026 consumer-plan transition. Google's
  [transition announcement](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)
  is the reason historical Gemini CLI figures are not used as the current
  embedded plan-value source.
- The [Gemini CLI quota documentation](https://github.com/google-gemini/gemini-cli/blob/main/docs/resources/quota-and-pricing.md)
  contains request limits for a distinct CLI/API surface and explicitly does
  not provide the current embedded plan's API-dollar allowance.
- Google quota is dynamic, task-dependent, refreshed on multiple windows, and
  subject to change; the 5dive range is a model, not account-level telemetry.
- [Google Developer Program Premium credits](https://blog.google/innovation-and-ai/technology/developers-tools/gdp-premium-ai-pro-ultra/)
  ($10/month for Pro and $100/month for Ultra) are a separate Cloud-credit
  benefit that can be applied to API or Vertex AI billing; they are excluded
from the embedded coding-plan route.
[6][12]

## Recommendations

The canonical route records are in `.refresh/v1.4/plan_cost_routes.json`. All
three Google routes retain the same four model IDs, and the route selector
chooses the highest multiple, so Gemini rows use the $199.99 AI Ultra 20x route
in Plan Costs while API Costs remain unchanged. Keep the low-confidence badge
and range visible in future plan-cost documentation, and re-research the
baseline before treating this estimate as a provider guarantee.

## Methodology

The research used official Google and Antigravity pages first, then current
community modeling and comparison pages for the otherwise-unpublished absolute
baseline. Claims were recorded in `claims.jsonl`, source observations in
`evidence.jsonl`, and source metadata in `sources.jsonl`. The implementation
formula uses the existing ValueRank billed token mix and divides each model's
API-priced task cost by the selected route multiple; the monthly sticker price
is not added to each task cost. Route selection and tier preservation are
covered by the focused unit tests.
[10][11]

## Bibliography

[1] [Google AI Pro and Ultra subscriptions](https://gemini.google/us/subscriptions/?hl=en)
[2] [Gemini Apps usage limits](https://support.google.com/gemini/answer/16275805)
[3] [Changes to Antigravity plans](https://antigravity.google/blog/changes-to-antigravity-plans)
[4] [Antigravity plans documentation](https://antigravity.google/docs/plans)
[5] [Gemini API pricing](https://ai.google.dev/gemini-api/docs/pricing)
[6] [Google Developer Program Premium benefits](https://blog.google/innovation-and-ai/technology/developers-tools/gdp-premium-ai-pro-ultra/)
[7] [Transitioning Gemini CLI to Antigravity CLI](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)
[8] [Gemini CLI quota and pricing](https://github.com/google-gemini/gemini-cli/blob/main/docs/resources/quota-and-pricing.md)
[9] [5dive Token Maxxing](https://5dive.ai/tokenmaxxing)
[10] [AgentPlans Google comparison](https://agentplans.fyi/compare/google/)
[11] [RoninForge Antigravity Pro versus Ultra](https://roninforge.org/antigravity-credits/pro-vs-ultra/)
[12] [RoninForge Antigravity weekly quota lockout](https://roninforge.org/antigravity-credits/weekly-quota-lockout/)
