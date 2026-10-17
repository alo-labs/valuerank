# Research plan

## Source classes

1. First-party plan and API pricing pages for OpenCode Go, Ollama, Z.AI Coding Plan, Alibaba Token Plans, and DeepSeek identity/API updates.
2. First-party model catalogs and migration notices to match exact variants or explicit aliases.
3. Current-window repository research packages for OpenAI/Codex, other provider chat services, and coding plans. The OpenAI crowdsourced allowance rule is restricted to the TiboTattle homepage.
4. Project-local raw-data and README files to define roster identity, effort, and roster coverage.

## Retrieval strategy

Search and page inspection used Codex built-in `web__run` only. Direct official pages were opened for current plan, quota, API tariff, and identity evidence. Search queries were used only to locate official pages and to check whether a quarterly Z.AI fee was exposed; third-party snippets were not treated as pricing evidence.

Research angles: (1) exact roster/variant IDs; (2) provider catalog exact names and version aliases; (3) plan pricing and cadence for every selected provider; (4) included credits/quotas and reset periods; (5) corresponding API tariffs and cache/peak/off-peak rates; (6) exact conversion formula and workload mix; (7) active promotions and expiry; (8) opaque plans and unsupported variants; (9) current-window user-report policy and allowed Codex source; (10) adversarial check for sibling transfer and false global-minimum claims.

## Comparability gates

A candidate is included only if its provider page names the exact route or a first-party notice documents a one-to-one alias, its paid tier is current, the denominator is published, and route API prices are published. For Z.AI, the published credit formula is combined with the same-model public API tariff. A plan with relative credits and no absolute conversion or a quota percentage with no token basis is recorded as a gap, not a guessed value.

## Workload profiles and validation plan

Use P1 50% uncached input / 25% cached input / 25% output; P2 75% uncached input / 0% cached input / 25% output; P3 20% uncached input / 60% cached input / 20% output. Cache-write share is 0% to avoid inventing a cache-write burden; tool calls are excluded. Validate model count and uniqueness, provider/tier row counts, candidate-to-selection links, all source/evidence/claim foreign keys, no cross-variant rate transfer, profile arithmetic, and explicit unknown-fee behavior.

## Mode rationale

Ultradeep is appropriate because the question spans 25 exact variants, live prices, incomparable quota systems, identity migrations, and temporary promotions. The phase artifacts include three adversarial cycles; the automated Silver Bullet validators remain unrun due to a documented LeanCTX execution issue.
