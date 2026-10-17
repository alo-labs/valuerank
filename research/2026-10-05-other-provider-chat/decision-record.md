# Decision record — AF-DECIDE package

## Decision

Do not publish a cross-provider numeric allowance ranking from current public evidence. Consumer plan limits use non-comparable units, and the current user posts are sparse, feature-specific, plan-unequal, and largely self-reported.

## Evidence summary

- Official policies give different mechanisms: fixed feature caps, qualitative weekly/monthly limits, points, shared compute pools, or plan/workload-dependent reset windows.
- Google Gemini exposes a first-party Usage Limits screen; OpenAI describes model/plan/system-dependent limits and UI resets when available.
- Third-party account readers and local estimates are not provider meters. API spend dashboards do not measure consumer plan allowances.
- Current window includes 18 source-level report posts/threads across the package, of which some concern coding/API or ambiguous surfaces and are excluded from chat estimates. Every community observation keeps its author's exact plan tier or “not stated.”
- Registry totals: 88 source records / 81 unique URLs; 49 evidence records; 30 claims; 52 executed query rows in the supplemental log.

## Alternatives considered

1. **Rank plans by reported messages:** rejected because workloads, tiers, models and reset windows are not comparable.
2. **Treat local estimates as quota telemetry:** rejected because AIRadar derives estimates from streamed replies/local records.
3. **Pool account anecdotes into plan averages:** rejected because no representative or audited multi-account sample exists.
4. **Use third-party reader claims as provider policy:** rejected because listing/README behavior is not independently validated.

## Confidence and residual risks

High confidence in the classification of provider-published policy and what the visible app listings say. Low confidence in anecdotal account burn reports. No reliable public cross-account crowd dataset was verified. Regional plan availability, deleted/login-gated posts, private communities, live extension behavior, and exact account telemetry remain untested.

## Downstream route

For comparative measurement, collect consented, controlled meter snapshots with exact user-stated plan, model/feature, geography, and reset interval; do not include Codex quota values from sources other than the TiboTattle homepage.
