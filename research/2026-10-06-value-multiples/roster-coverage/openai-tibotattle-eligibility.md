# OpenAI / Codex: TiboTattle eligibility audit

**Conclusion:** The TiboTattle homepage displays community-derived API-price-equivalent allowance estimates, but its own documentation says every chart compares a full Pro 20x-equivalent week—not each plan's actual allowance or the amount paid. Under the project's rule requiring actual user-reported allowance measurements priced at API rates, these normalized plan-group aggregates are not a defensible per-plan measurement or individual datapoint. Keep them as source-labeled context only; do not calculate a Value Multiple from them.

## Current homepage evidence

On **2026-10-06**, the [TiboTattle homepage](https://tibotattle.com/) showed activity through **2026-10-04** in the selected **30d** range and **By plan** view. Its unit label was **“API-equivalent USD / Pro 20x week.”** The displayed plan groups were:

| Homepage plan group | Displayed API-equivalent amount | Contribution-source count |
|---|---:|---:|
| Plus | $88 | 5 |
| Pro 5x | $353 | 8 |
| Pro 20x | $1,464 | 6 |

The homepage describes a source as an installation/account track, not a unique person; separate installations may overlap. These counts therefore describe contribution tracks, not verified distinct end users. The chart is a TiboTattle-computed aggregate over contributing tracks, rather than a set of linked, individually inspectable user reports.

## What qualifies, and at what level

The displayed values are presented by TiboTattle from community contributions, not as an OpenAI-published allowance claim. However, the [TiboTattle documentation](https://tibotattle.com/docs) says all three chart modes compare a full Pro 20x-equivalent weekly allowance at API prices, not each plan's actual allowance or money paid. Its [publication disclosure](https://tibotattle.com/privacy#publication) says the public figures are daily API-price-equivalent allowance estimates and may rely on a single source. The aggregate is therefore useful context about TiboTattle's estimates, but it does not disclose an actual allowance measurement for an individual plan holder.

The homepage's USD/API-equivalent label is the published pricing basis for this display. The by-plan view does not expose source-level model/token mix or rate inputs, so the exact API-price calculation cannot be independently reconstructed from the homepage. Treat the amounts as TiboTattle's reported API-equivalent aggregation, not as individually verified API invoices or per-source calculations.

That aggregate eligibility does not make the values individual cases. The homepage does not reveal each source's measured amount, exact contribution dates, paid fee, or user identity. Because tracks may overlap, do not reinterpret the source counts as unique users or as the number of independent personal reports. The selected 30-day range shows activity through Oct 4, but does not provide a source-level period that can be paired with any one user's fee.

The by-plan view also does not attribute the aggregate to any specific OpenAI model or ranked model variant. Keep it separate from model-level rows; do not transfer a plan-group result to GPT-6 Sol, GPT-5.6 Sol, or another model.

## Value Multiple decision

**No Value Multiple is defensible from this homepage view.** TiboTattle normalizes the published figures to a Pro 20x-equivalent week rather than each plan's actual allowance, and the page does not expose a source-level measured period, model/token mix, or the contributor's paid fee. A numerator-to-subscription-fee ratio would therefore turn a normalized crowd aggregate into an actual plan measurement and pair it with an unmatched denominator.

Use these figures only as source-labeled aggregate context. Do not turn them into individual user reports, unique-person sample sizes, current plan prices, or model-specific usage. Revisit a Value Multiple only if the homepage makes the contributor's plan tier/fee and date-bounded API-priced allowance evidence defensible for the same user and period.

## Correction to the prior draft

The earlier draft described a cached page, a failed service request, and a September 28 publication. That observation is superseded by the current homepage inspection: this audit uses the live by-plan view with activity through October 4 and does not rely on the earlier cached figures or dates.
