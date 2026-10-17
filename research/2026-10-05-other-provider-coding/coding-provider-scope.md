# Coding-provider supplement scope

**Snapshot date:** 2026-10-05  
**Eligible community publication/data window:** 2026-09-05 through 2026-10-05 inclusive  
**Audience:** ValueRank researchers comparing subscription allowance visibility and user-reported coding usage.

## Research questions

1. Which first-party or third-party apps expose account-level coding-plan allowances for GitHub Copilot, Cursor, Windsurf/Codeium, OpenCode Go, Kimi Code, Z.AI/GLM Coding Plan, and Ollama Cloud?
2. What recent user-reported consumption observations surfaced in Reddit, Hacker News, GitHub/community forums, and developer communities?
3. Which observations are provider-meter readings, provider-published quotas, local usage-log estimates, or API-cost equivalents?
4. Which observations can support current-window statements without crossing the date cutoff or changing products/plans mid-interval?

## Scope and exclusions

- Include coding-oriented subscription plans and account meters for the seven provider/product families listed above. OpenCode Go is included as a subscription product; the OpenCode editor itself is treated as a client/harness unless the post specifically reports Go or Zen.
- Search Reddit, Hacker News, GitHub/community discussions, and provider/developer forums. Use current first-party policy and meter documentation only as policy/context evidence, separate from community reports.
- Exclude local Ollama inference from paid-plan allowance evidence. Ollama Cloud is included.
- Do not transfer Devin reports to Windsurf. Preserve the product named by the user/source even when a subreddit or account previously used another brand.
- Treat a parent post and a dated in-window reply as separate publication/data dates. A dated reply in the eligible window may be included even when the parent post is older, but identify the older parent.
- Exclude an aggregate usage interval that begins before 2026-09-05 unless its post-cutoff segment is separately isolated. Publication date and measurement interval remain separate fields.
- A missing model, date, plan, or measurement detail stays missing. Every user-reported datapoint must state the exact tier/name supplied by the author or the literal value `not stated`; do not infer a tier from price, employer status, subreddit, or provider documentation.

## Measurement classes

- `provider_account_meter`: percentage, credits, quota window, or reset state the user says was shown in the provider account/plan surface.
- `published_provider_quota`: a provider’s documented plan allowance or policy. It is not a user’s observed use.
- `local_usage_log_estimate`: a user/tool-derived request or token count, projection, or local log total. It is not a provider-meter value unless the source says so.
- `api_cost_equivalent`: usage converted to public API/list-rate cost or compared with direct API spend. It is not the subscription’s allowance or cash paid to the subscription provider.
- `synthetic_example`: demonstration output not tied to a real account; excluded from consumption claims.

Do not merge these classes or turn one into another. A single post may yield multiple evidence rows when it reports different measurement classes.

## Acceptance criteria

- Source, evidence, and claims registries use stable IDs and valid crosswalks.
- Query log records exact executed web queries, outcomes, and direct pages opened.
- Report citations link directly to sources; each user datapoint has a distinct date, exact plan-or-`not stated`, model/task/window where available, class, eligibility, and caveat.
- Old addendum source/evidence/claim/query counts are independently checked; search-outcome rows are separated from direct sources.
- Critique and validation logs record the limitations, automated checks, counts, and any failed or excluded items.
