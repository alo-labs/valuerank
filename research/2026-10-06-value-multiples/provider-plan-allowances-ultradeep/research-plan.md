# Ultradeep research plan

## Workflow contract

This run follows Silver Bullet `WF-SILVER-DEEP-RESEARCH`, `AF-DECIDE`, `FS-SILVER_DEEP_RESEARCH`, mode `ultradeep`. The phase sequence is Scope → Plan → Retrieve → Triangulate → Outline → Synthesize → Critique (three cycles) → Refine → Package. The deliverables are being assembled to the Silver Bullet artifact contract; do not claim the slash command was invoked unless an execution record proves it.

## Retrieval method

- Use the Codex built-in in-app browser through `cua_repl` only for browser lookup. Do not use Chrome, Edge, `web.run`, `curl`, `wget`, raw HTTP/fetch, or external search APIs.
- Search each first-party provider's official help, pricing and developer documentation; record the exact visible search query and each opened direct URL in `query_log.jsonl`.
- Reopen and inspect primary source pages for current price, dated promotions, quota rules, API rates, and exact model access. Search results are discovery evidence only; direct first-party page content governs.
- Retrieval/as-of date is 2026-10-06. User-report publication/measurement dates are independently constrained to 2026-09-06–2026-10-06.
- Record inaccessible or login-gated pricing as `not publicly verified`, not as evidence that no plan or price exists.

## Branch plan

1. OpenAI: current Codex/Work plan availability, Plus and Pro tier pricing, usage windows/model-specific guidance, paid credit/reset mechanics, and the five exact OpenAI API model rows.
2. Anthropic: Pro/Max plan pricing, Claude Code access, per-session and weekly limits, newly introduced usage-credit/top-up mechanics, and exact Opus 5/5.5 API rates.
3. xAI: SuperGrok consumer plans, shared weekly-pool rules and top-ups, Grok 4.6/4.7 app/API identity, and exact model API rates.
4. Google DeepMind: Google AI consumer tiers/prices, Gemini app quota/multipliers/reset rules and model names, exact Gemini 3.8 Flash API pricing and scheduled price changes.
5. Moonshot AI: Kimi Code current and legacy membership tiers, exact K3 eligibility, rolling/monthly/weekly quota rules, public price availability, extra usage, and exact K3 API rates.
6. Z.AI: Lite/Pro/Max prices, exact GLM-5.3 plan quota and credit formula, current date-bounded credit promotions, and exact GLM-5.3 API prices.
7. Alibaba: Qwen personal Token Plan tiers/prices/credits, Qwen3.8-Max eligibility and quota consumption rules, and a same-product/channel exact-model API price if published.

## Triangulation and calculation

For every model, cross-check the plan-product label against the exact ValueRank ID and the matching first-party API rate. Compare plan price, allowance unit, reset window, and API price separately. Compute a USD API-equivalent allowance only when the provider explicitly links a numeric quota to a deterministic same-model price basis. For a variable token mix, provide a bounded component-composition range with the method and never characterize it as observed use. Do not annualize a five-hour or weekly cap into a user-reported value multiple.

## Three critique passes

- **Cycle 1 — identity and source authority:** exact plan/model/version, correct provider, current URL/date, primary vs search-result discovery, and whether app label equals API model ID.
- **Cycle 2 — allowance and arithmetic:** quota unit, nested windows, rollover/reset, cost/price currency, promotional cutoff, cache/model/context components, and any API-equivalent calculation.
- **Cycle 3 — adversarial synthesis:** consumer plan vs API service mismatch, regional price ambiguity, missing tiers or login-gated terms, estimates presented as guarantees, and unsupported transfer across model variants.

Each cycle must produce concrete findings, and material findings must trigger a retrieval loopback or an explicit residual limitation.

## Package and validation

Produce `sources.jsonl`, `evidence.jsonl`, `claims.jsonl`, `query_log.jsonl`, `model_coverage.csv`, `plan_allowances.csv`, calculations/exclusions, report, triangulation, outline, critique, decision record, handoff, and rollup. Run the Silver Bullet Ultradeep phase gate, report validator, citation verifier, claim-support validator, and a deterministic CSV/ledger arithmetic crosswalk. Record exact validator outcomes.

## Ultradeep retrieval thresholds

Use the workflow thresholds from Silver Bullet `phases.yaml`: target source budget 30, maximum 40 sources, and average source credibility at least 75. A time-based triage point is permitted after 15 minutes; record the achieved source count and credibility basis, and keep searching when material provider/model gaps remain. This package prioritizes first-party plan, help, and API documentation; Google search pages are logged as discovery queries only and do not support factual claims. Three critique cycles are required, with a retrieval loopback for material findings.
