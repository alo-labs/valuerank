# Decision record

**Date:** 2026-10-06 Australia/Sydney  
**Workflow:** Silver Bullet Deep Research / Ultradeep  
**Decision:** Treat first-party plan allowance research as a separate evidence class from end-user-reported value multiples.

## Decisions

1. Keep the 13 ranked ValueRank IDs and rank order unchanged; exclude Mistral and any sibling model not present in the ranked roster.
2. Record all seven first-party provider plan families, displayed fee/currency, published quota units, reset rules, and exact-model API tariffs in the CSV/JSONL package.
3. Mark plan/API equivalents N/C unless the provider publishes a deterministic, exact-model conversion. Z.AI GLM-5.3 alone qualifies for an analyst-derived bounded range using its own posted coefficients and API rates.
4. Do not infer OpenAI gpt-6-sol pricing from gpt-6.1-sol; do not infer Grok 4.7 subscription access from the Grok 4.6 plan listing; do not infer a Google app/API model crosswalk; preserve Kimi's conflicting first-party pages; and do not turn Alibaba Token Plan credits into API dollars without its model coefficient.
5. Preserve local subscription currency and USD API prices independently. Do not produce a cross-provider cheapest-plan/value ranking from heterogeneous units or unconverted currencies.
6. Keep provider claims out of the four-column user-reported Value Multiple table. Any user-reported data must satisfy the separate 2026-09-06–2026-10-06 publication/measurement window and exact plan-tier provenance.

## Rationale

Published API prices do not establish included subscription usage. For most plans the public allowance is a task meter, relative multiplier, compute budget, shared pool, or dynamic credits with missing model-level conversion. Treating those units as dollars would require unsupported assumptions and could turn provider claims into apparent user observations.

## Consequences

The provider-by-plan report is complete as a transparent source-backed map of published facts and gaps. The value table remains restricted to end-user reports. Open N/C fields can be revised if providers publish the exact missing conversions or access crosswalks.
