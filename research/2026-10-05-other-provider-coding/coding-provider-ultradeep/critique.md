# Adversarial critique log

Three cycles were completed as document reviews. They were performed manually; no separate agent review or `/sb critique` command was run. Each cycle records the issue found, the repair, and residual risk.

## Cycle 1 — tier transfer and author identity

**Challenge:** The Copilot Pro+ plan and 7,000-credit allocation belong to the thread author, while the 150,000-credit/24,000-use report is a comment. The same attribution error can occur in a multi-user Ollama thread.

**Repair:** Evidence is split by reporter and observation. Every eligible user row carries `plan_tier_as_reported`; unspecified plans are written exactly `not stated`. Ollama's Sep 10 grandfathered Pro author and Sep 15 Ollama Pro author remain separate; the latter's grandfathering state remains unknown.

**Residual risk:** Usernames and comment permalink IDs were not retained in the captured evidence, so distinct commenter identities are represented as date/role labels, not cross-thread deduplicated accounts.

## Cycle 2 — metric conflation and false normalization

**Challenge:** Cursor's USD 5–7 equivalent, Ollama's local token counters, Go/Cursor account percentages, provider published quotas, and request-count projections do not measure the same thing. The 1,200-request Ollama value could be mistaken for an observed cap; the 400M cache-read count could be mistaken for provider-billed tokens.

**Repair:** Added separate classes `provider_account_meter`, `published_provider_quota`, `local_usage_log_estimate`, `user_extrapolation`, and `api_cost_equivalent`. CP-E10 is now explicitly a user extrapolation from a meter and approximate request count, not a local log measurement. CP-E11 is only an external API cost comparison. CP-E13 is local OpenCode telemetry and is not claimed to be provider billed.

**Residual risk:** Authors' screenshots or underlying account exports are unavailable; the review trusts the text they posted while assigning low confidence where relevant.

## Cycle 3 — temporal eligibility, weak sources, and tool claims

**Challenge:** Search snippets and older HN material can be wrongly counted as in-window usage. Tracker demo numbers or README feature claims can be misrepresented as subscriber observations. A missing hit can be overstated as proof of absence.

**Repair:** Evidence records separate publication date from measurement interval. Older HN results and synthetic `zai-usage --demo` data are excluded from user evidence. The vague Sep 8 Ollama OP estimate is retained as CP-E14 with plan `not stated` and `excluded_uncorroborated_context`. HN, Windsurf, and Z.ai findings are reported only as bounded search outcomes.

**Residual risk:** Search coverage is not exhaustive, the exact query literals for a small earlier official-document search set were not preserved, and the validator capacity issue below limits runtime automation evidence.

## Reviewer conclusion

The strongest supported statements are attributed meter or local-log reports, not cross-plan capacity conclusions. Any roll-up must maintain the exclusions and measurement classes in the ledgers. The remaining search-coverage and source-authentication limits are material and are retained in the report.
