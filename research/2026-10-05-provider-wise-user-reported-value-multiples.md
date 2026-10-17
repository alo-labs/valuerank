> **Historical snapshot:** This 2026-10-05 table is superseded by the [2026-10-06 provider-wise API-priced multiples table](2026-10-06-provider-wise-user-reported-value-multiples.md). Its pre-window Claude rows and Mistral rows are not in the current table.

# Provider-wise user-reported subscription value multiples

**As of:** 2026-10-05  
**Eligible report and measurement window:** 2026-09-05 through 2026-10-05, inclusive.

This is a provider-first view of individual end-user reports. Provider groups are sorted by their highest qualifying multiple; rows within each provider are sorted high to low. Repeated rows can come from one person reporting separate periods. They are not averaged and do not represent a typical-user estimate.

| Provider | Plan | Value Multiple | Reference |
|---|---|---:|---|
| Anthropic (Claude) | Max 20x — Sep 5–12 | **≈58.84×** — one account reports $2,715.63 API-list-price-equivalent use at about 100% of the weekly meter; annualized to a month. | [Sep 5–12 account-log datapoint](https://www.reddit.com/r/ClaudeCode/comments/1wfb1x8/lower_usage_limits_kicking_in_early_and_large/) |
| Anthropic (Claude) | Max 20x — Sep 17 reset, first 28 hours | **≈50.9×** — partial-week estimate: $1,222 at 52% of the meter, extrapolated by the user to about $2,350/week, then annualized to a month. | [u/Siigari’s partial-week datapoint](https://www.reddit.com/r/ClaudeCode/comments/1wk3zq5/i_audited_my_session_logs_against_the_usage_meter/) |
| Anthropic (Claude) | Max 20x — Sep 12–13, about 23.3 hours | **≈44.1×** — partial-period estimate from $529.50 API-equivalent use at 26% of the weekly meter; the source table totals $529.57. | [Sep 12–13 account-log datapoint](https://www.reddit.com/r/ClaudeCode/comments/1wfb1x8/lower_usage_limits_kicking_in_early_and_large/) |
| Anthropic (Claude) | Max 5x — Sep 15 onward, partial week | **≈20.3×** — the user’s ~$469/week estimate used about two days and 29 meter points; the author says it is preliminary. | [Max 5x partial-week datapoint](https://www.reddit.com/r/ClaudeAI/comments/1why2zx/a_lot_of_talk_about_reduced_weekly_limits_but_a/) |
| Anthropic (Claude) | Max 5x — Sep 5–14, +50% promotion period | **≈18.2×** — the user’s account estimate is about $421/week at API list prices; this is the earlier, promotional allowance period. | [Max 5x promotional-period datapoint](https://www.reddit.com/r/ClaudeAI/comments/1why2zx/a_lot_of_talk_about_reduced_weekly_limits_but_a/) |
| Mistral | Edu Pro annual — monthly Vibe allowance | **≈29.1×** — user reports €127/month in included Vibe credits and a $60/year subscription; the fee is converted to euros at the ECB rate noted below. | [u/73td’s Edu Pro account datapoint](https://www.reddit.com/r/MistralAI/comments/1wl9rx5/comment/pax2iit/) |
| Mistral | Pro — monthly Vibe allowance | **≈14.2×** — user reports a €255 monthly allowance and about €50 used on day one; calculation uses Mistral’s France-facing €17.99/month price including tax because the user’s billing country is not stated. | [u/Acou’s Pro account datapoint](https://www.reddit.com/r/MistralAI/comments/1wl9rx5/comment/paxxtrw/) |

## Calculation and source policy

- **Value Multiple** = API-price-equivalent monthly allowance ÷ effective monthly subscription fee. Claude’s reported weekly amounts are annualized using `52 ÷ 12`. Values derived from partial meter readings or estimates are marked as such and rounded to avoid implying more precision than the reports provide.
- The allowance numerator comes only from the linked end-user account, transcript, or log report. No provider-published allowance estimate, marketing multiple, or plan-quota claim is used as a numerator. Published plan prices are used only for the fee denominator.
- Anthropic lists Max 5x at $100/month and Max 20x at $200/month in its [Max-plan pricing help page](https://support.claude.com/en/articles/11049741-what-is-the-max-plan).
- Mistral Edu Pro’s reported $60/year is treated as $5/month and converted using the ECB’s [Sep 2026 EUR/USD reference table](https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/eurofxref-graph-usd.en.html): on Sep 18, the last business day before the Sep 20 Reddit report, €1 = $1.1460. Thus `(€127 ÷ ($60 ÷ 12 ÷ 1.1460)) = 29.11×`.
- Mistral Pro’s denominator is the €17.99/month price displayed for France, including tax, on the [Mistral plans page](https://mistral.ai/pricing). The reporter’s billing country is not stated, so that multiple is conditional on this displayed price.

## Coverage limits

These are individual reported periods, not guaranteed current entitlements or cross-provider measurements under a common workload. Claude’s account-meter weighting is opaque, and its API-list-price figures are user-calculated proxies.

The reviewed in-window material produced no qualifying numeric Codex datapoint on the TiboTattle homepage. The Cursor estimate was not included because its usage cycle began Sep 2 and the post does not isolate Sep 5 onward. Kimi’s $128.35 figure is reported usage consumed over an unclear period, not a full allowance datapoint. Other reports based only on percentages, token counts, request counts, or unsplit model-point mixes were not converted into multiples.
