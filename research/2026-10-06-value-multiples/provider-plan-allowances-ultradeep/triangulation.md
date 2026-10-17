# Triangulation

## Identity joins

The ranking roster was first fixed to the 13 IDs and ranks in `scores.md` and `raw-data.md` (E01). Plan-product names and API names were then joined independently. Exact matches are kept distinct from consumer labels or similarly named API variants:

- OpenAI's consumer and Codex materials name GPT-6 Sol, while the visible API price row is `gpt-6.1-sol`; it is not assigned to `gpt-6-sol`.
- xAI's consumer page lists Grok 4.6 while the API tariff lists both Grok 4.6 and 4.7; API availability alone does not prove subscription access for 4.7.
- Google's consumer support page says Gemini 3 Flash; the API model directory separately lists `gemini-3.8-flash`. No crosswalk connecting the app quota to that API ID was found.
- Kimi help pages use Andante/Moderato/Allegretto/Allegro, while the Code document uses Go/Plus/Pro. The official pages do not provide a tier crosswalk, and differ on the weekly Code reset.
- Alibaba's Token Plan and Alibaba Cloud Model Studio are separate products. The former publishes credits; the latter publishes API rates for exact `qwen3.8-max`.

These joins prevent an API price, model-family name, app entitlement, and plan meter from being mistaken for one another.

## Allowance-unit comparison

Six of seven providers expose allowance units that lack a deterministic public conversion to exact-model API dollars:

| Provider | Published plan unit | Missing for an API-dollar equivalent |
|---|---|---|
| OpenAI | Shared Work/Codex meter, five-hour messages or uncapped five-hour Pro tiers, plus weekly controls | Exact token/cache mix and total window quota for each plan/model |
| Anthropic | Relative Pro/Max session allowance plus shared weekly cap | Absolute per-model tokens/API-dollar ceiling |
| xAI | Shared flexible weekly pool | Absolute pool size and per-model share |
| Google | Compute-based app allowance and relative plan multipliers | Exact app/API model mapping and compute-to-token conversion |
| Moonshot AI | Shared monthly credits/estimated task uses plus Code rate windows | Tier crosswalk, resolved reset rule, and model-specific credits per token |
| Alibaba | Monthly Token Plan credits | Qwen3.8 Max credits per token by input/cache/output/thinking/tool component |

Z.AI publishes GLM-5.3 credit coefficients and matching API rates. That permits a *theoretical, mix-bounded* price-equivalent usage range. It is the only computation in `calculations.csv`; it does not measure user consumption, and it is not inserted into the end-user value-multiple table.

## Price and time basis

Prices remain in the currency displayed by the local or first-party page: AUD for the Australia-localized OpenAI/Google pages, USD for the specified API rates and USD plan pages, and CNY for Moonshot/Alibaba membership pages. No FX conversion or cross-provider price rank is asserted.

Current sale prices are recorded separately from list prices. The Qwen night discount and GLM-5.3-Flash credit campaign are time-bounded or provider-controlled adjustments and are excluded from steady-state API-equivalent estimates. The Google API schedule effective 2027-01-01 is reported separately from rates current on the retrieval date.

## Reconciliation result

First-party information is sufficient to identify plan tiers, advertised prices, most product/model links, reset structures, and exact API tariffs. For most providers it is not sufficient to calculate a comparable subscription API-dollar allowance. Their plan rows therefore retain the published units and explicit N/C values instead of borrowing user reports, provider claims from another product, or third-party routes.
