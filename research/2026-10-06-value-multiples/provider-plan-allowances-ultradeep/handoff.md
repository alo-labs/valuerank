# Handoff

## Deliverables

- `research_report.md`: provider-by-provider first-party plan and API findings.
- `model_coverage.csv`: all 13 ranked model IDs, exact provider/product/API identity, and remaining mapping gaps.
- `plan_allowances.csv`: paid tiers, prices, currencies, units, reset/overage terms, and API-equivalent status.
- `calculations.csv`: reproducible GLM-5.3 plan-credit/API-rate range.
- `sources.jsonl`, `evidence.jsonl`, `claims.jsonl`, `query_log.jsonl`, `exclusions.jsonl`: provenance and claim/evidence package.
- `triangulation.md`, `outline.md`, `critique.md`, `decision-record.md`, and `vloop-rollup.json`: Ultradeep phase artifacts.

## Remaining evidence gaps

1. OpenAI: an exact API rate row for `gpt-6-sol` and `gpt-5.6-luna`, plus exact subscription token/API-dollar budgets by model and tier.
2. Anthropic: absolute Opus 5/5.5 included usage under Pro/Max and the shared weekly cap.
3. xAI: absolute weekly pool size and first-party subscription eligibility for Grok 4.7.
4. Google: app/API model mapping for Gemini 3 Flash versus `gemini-3.8-flash`, and conversion of compute limits to exact API token components.
5. Moonshot: crosswalk from Andante/Moderato/Allegretto/Allegro to Go/Plus/Pro, authoritative current Kimi Code weekly-window policy, and K3 credits-per-token mapping.
6. Alibaba: qwen3.8-max-specific Token Plan credit coefficients for input, cache, output, reasoning, and tools.

## Interpretation guardrails

- A plan allowance marked N/C is unknown, not zero.
- The Z.AI USD intervals are theoretical composition bounds from provider-published plan/API inputs; they are not user-measured value multiples.
- Plan costs remain in source currency. No FX or all-provider plan ranking is included.
- The Oct 6 user-reported Value Multiple table is a separate deliverable and accepts only end-user reports in its stated one-month window. TiboTattle is the only permitted OpenAI crowdsourced numerical source; homepage aggregates cannot be misrepresented as individual user source points.

## Validation and publication

The final handoff will include the four Silver Bullet validator logs and a deterministic ledger/CSV crosswalk result after they run. The Silver Bullet workflow was followed manually: `automated_sb_command_invoked` remains false because the slash command was not executed. This report is local research; publishing or deploying the ValueRank site is a separate release step and is not asserted here.
