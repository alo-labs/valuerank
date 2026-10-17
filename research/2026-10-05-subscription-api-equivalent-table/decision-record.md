# Decision record — AF-DECIDE

## Decision

Deliver the 25-model evidence-bounded comparison with selected routes only for exact variants that have a comparable published denominator. Label results “best quantified route” unless the task's evidence supports a broader claim. Do not publish a single universal token value or global cheapest-provider claim for the full roster.

## Alternatives considered

- **Infer monthly tokens from quota percentages or plan multipliers:** rejected because percentages/relative multiples do not identify exact model/token/cache mix.
- **Use request-count estimates as a token denominator:** rejected because requests vary and do not share a declared token profile.
- **Use user anecdotes as stable allowances:** rejected because observations are user-/task-specific, may omit exact plan tier, and do not normalize input/cache/output.
- **Transfer a sibling model's plan cap/API price:** rejected. DeepSeek's dated alias notice establishes its direct API target only; OpenCode's separate V4 Flash/V4.1 Flash subscription rows do not say which version the legacy catalog row serves, and Ollama lists V4.1 Flash only. DeepSeek V4 Flash stays unqualified; no sibling allowance is applied.
- **Assume a quarterly discount for Z.AI:** rejected; the current official fee was not displayed in the inspected page.
- **Treat the best quantified route as a global market winner:** rejected where a provider's exact-model route has an opaque subscription denominator.

## Evidence summary

First-party OpenCode and Ollama pages directly join paid-tier prices, usage allowances, and route API rates. Z.AI's separate first-party plan, formula, pricing, and promotion pages support profile- and time-dependent calculations. DeepSeek's change log supports an official direct API alias target, but does not verify a third-party subscription's underlying version; the exception register preserves that gap. Alibaba's official Token Plan material confirms Qwen3.8 Max access and plan terms while leaving the conversion coefficient missing. Current research packages establish the 25-model roster, one-month report window, and permitted TiboTattle-only Codex crowd boundary.

## Tradeoffs, risks, and confidence

Confidence is high in arithmetic that directly divides published dollar credits or applies the published Z.AI formula to the declared profiles. The DeepSeek V4 Flash subscription match is explicitly uncertain because an upstream API alias does not resolve the third-party catalog route's served version. Confidence is low for a global-market ranking across plans with opaque denominators; those outcomes remain explicitly unknown.

Important risks are price changes, route/catalog changes, limited-region access, context-size brackets, mixed peak/off-peak schedules, shared Team usage, hidden tool charges, and short promotion expiry. No user reported allowance is used as if it were a provider contract.

## Downstream handoff

Parent reviewer should inspect `table.md`, `tier-register.md`, `route-tiers.csv`, `routes.json`, the identity/denominator claims, and validation logs. No project-level verification or independent parent sign-off is claimed in this decision record.
