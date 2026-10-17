# Report outline and evidence map

1. **Executive summary** — seven first-party providers, 13 exact ranked IDs, what is and is not computable (C01-C10).
2. **Scope and method** — October 6, 2026 as-of date; built-in browser only; exact IDs; separate user-reported workstream (E01, Q01-Q10).
3. **Provider findings**
   - OpenAI plans and exact API ID gaps (E02-E05).
   - Anthropic Pro/Max allowance and Opus API rates (E06-E07, E24).
   - xAI shared weekly pool and Grok access/rates (E08-E10).
   - Google regional prices, compute limits, and API/app identity gap (E11-E12).
   - Moonshot current tiers, contradictory Code windows, and exact K3 API identity/rates (E13-E16).
   - Z.AI plan units and reproducible bounded API conversion (E17-E19).
   - Alibaba Token Plan credits versus separate Model Studio API rates (E20-E22).
4. **13-model coverage matrix** — exact rank-to-provider mapping, tier applicability, API rows, and residual gaps (`model_coverage.csv`).
5. **Provider-by-plan table** — fees, currency, allowance units/windows, and API-equivalent status (`plan_allowances.csv`).
6. **Calculations** — GLM-5.3 credit-to-API range from first-party coefficients and rates (`calculations.csv`).
7. **Limitations and exclusions** — unresolved model identity, private/dynamic quotas, temporary incentives, and strict user/provider evidence split (`exclusions.jsonl`).
8. **Decision and handoff** — no provider-reported plan quantity is put in the end-user value-multiple table; list source changes needed to resolve remaining N/C entries.
