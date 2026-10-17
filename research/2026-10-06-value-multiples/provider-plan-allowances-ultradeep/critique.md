# Ultradeep adversarial critique log

Three cycles were completed across the synthesis. Each cycle used a skeptic, reviewer, and red-team pass; findings and repairs below are recorded rather than presented as independent external sign-off.

## Cycle 1 — model identity and source authority

- **Skeptic:** Could similar model strings be treated as exact? OpenAI's API page uses `gpt-6.1-sol`, not ranked `gpt-6-sol`; Google uses a consumer Gemini 3 Flash label and API `gemini-3.8-flash`; xAI has API prices for Grok 4.7 although its consumer plan page shows Grok 4.6.
- **Reviewer:** The initial plan table needed a current first-party subscription pricing page and stronger evidence for exact Kimi K3 API identity.
- **Red team:** A search snippet or provider API price could be mistaken for proof of plan availability.
- **Loopback and repair:** The Codex built-in browser was used to inspect OpenAI's localized pricing page, Kimi's official membership and K3 quickstart, Google's current API model directory, and Alibaba's exact Qwen3.8 Max model page. Direct source pages replaced discovery snippets; exact mismatches remain explicit in `model_coverage.csv` and `exclusions.jsonl`.

## Cycle 2 — allowance units, resets, and arithmetic

- **Skeptic:** Relative tiers, weekly pools, credits, and app compute are not token counts. Converting them at a single average rate would create false API equivalents.
- **Reviewer:** Kimi's official membership help page says its Code limit is five hours per week, but Kimi Code documentation says new members have no weekly cap and retain a rolling five-hour window plus monthly quota.
- **Red team:** The Alibaba night promotion may be described incorrectly as a 40% discount; Chinese “four-tenths” means 40% of normal credits, not a 40% reduction.
- **Loopback and repair:** Both Kimi first-party pages were reopened side by side and retained as a source conflict. Qwen's plan page and exact API model page were reread; credits depend on model, tokens, thinking, and tools, so API conversion stays N/C. Alibaba's 22:00-08:00 offer is recorded as 40% of ordinary credit consumption and is not projected across a full billing month. The GLM calculations use the exact posted coefficients/rates and weekly-to-monthly factor; campaign and off-peak factors are excluded.

## Cycle 3 — comparative claims and evidence-class leakage

- **Skeptic:** Could a theoretical provider plan/API conversion be misread as end-user-reported usage or a universal value ranking?
- **Reviewer:** Regional AUD, USD, and CNY prices cannot be directly compared without a dated FX basis. Current discounts must not be treated as stable list prices.
- **Red team:** API products and plan products can be different billing channels even when model strings match, especially for Kimi and Alibaba.
- **Loopback and repair:** Provider-plan rows and the user-reported four-column table are separate. Currency is preserved and no cross-provider rank is produced. List and current promotional prices are separate columns; only Z.AI receives a bounded API-dollar interval, labeled provider-input-based analyst derivation. Kimi API account recharge and Alibaba Model Studio API prices are not represented as included subscription balances.

## Residual limitations

The largest unresolved items are exact OpenAI API rates for two ranked IDs, an absolute allowance size for OpenAI/Anthropic/xAI/Google, Google's app-to-API ID mapping, Kimi's tier and reset crosswalk, and Alibaba's model-specific Token Plan conversion. These affect comparability, not the source-backed facts recorded in the package. No claim of external independent review is made here.
