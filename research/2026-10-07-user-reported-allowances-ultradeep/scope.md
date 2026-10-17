# Scope: current-month user-reported subscription value multiples

## Question

Which non-Anthropic ValueRank model providers (excluding Mistral, which is not featured in ValueRank) have a current-window end-user report of actual subscription use that can be priced at API rates and matched to a paid plan tier? What defensible provider-wise value multiples can be shown from those reports?

## Window and cutoff

- Snapshot date: 2026-10-07.
- Eligible report publication dates: 2026-09-07 through 2026-10-07, inclusive.
- Record the measured usage window separately. A recent report whose measurement period crosses the cutoff may be retained only as its full-period user estimate when no in-window subtotal is isolated; disclose the exact interval and do not describe the use as entirely in-window. Exclude separately isolated measurements outside the window.

## Binding evidence rules

- A numerator must be an actual end-user-reported measurement of personal plan usage priced at API rates. A user's API-priced estimate is acceptable only when tied to their measured usage; label what cannot be independently reproduced.
- Provider-published allowance, quota, cap, reset rule, “X-times” multiplier, or marketing estimate can never supply the numerator.
- Provider plan prices may support the denominator only when the user's reported plan tier and fee are matched. Provider API rate cards may support pricing of the user's measured use, but do not count as allowance evidence.
- The report publication date must fit the current-month window. Preserve exact model variant, product surface, plan tier, report date, measurement interval, currency, stated API-priced amount, and source permalink. Mixed or unnamed model usage remains provider/plan-level and cannot be transferred to a specific ranked model.
- For OpenAI/Codex, only the TiboTattle homepage is allowed as the numeric crowd-data source. Its raw plan-group aggregates are permitted and must remain aggregates of installation/account tracks, with historical period and model-identification limits. Do not treat them as individual end-user datapoints or use normalized Pro20x figures as the raw smaller-plan numerator.

## In scope

- The six non-Anthropic providers represented in the current ValueRank roster: OpenAI, xAI, Google DeepMind, Moonshot AI/Kimi, Z.AI, and Alibaba/Qwen, using the exact ranked variants from the project coverage map.
- Reddit first, followed by Hacker News and relevant developer communities/forums. For OpenAI crowd numbers, check only TiboTattle homepage.
- User-reported subscription usage observations, candidate qualifications and near-misses, source/query logs, and updates to the four-column provider-wise report and research index.

## Out of scope

- Provider-published allowance/quota or marketing data as a numerator.
- API-only usage, benchmark/provider test claims, hypothetical usage, unrelated subscription tiers, or reports outside the window.
- Assigning mixed-model or unidentified usage to one ranked model.
- Mistral and new provider plan claims unless needed only to establish a price denominator for a qualifying user datapoint.

## Success criteria

- Search and coverage artifacts clearly distinguish qualifying reports from near-misses and bounded gaps.
- Any published number has a direct source link, exact tier, model scope, report date, measurement interval, pricing basis, and transparent calculation. The permitted TiboTattle aggregates reference the homepage because individual datapoint permalinks are unavailable. Publication date determines report recency; any measurement interval crossing the cutoff is disclosed.
- The provider-wise table retains exactly `Provider, Plan, Value Multiple, Reference`, sorted by each provider's highest included multiple.
- The index and report state the search window, evidence policy, limitations, and Silver Bullet runtime invocation status accurately.
