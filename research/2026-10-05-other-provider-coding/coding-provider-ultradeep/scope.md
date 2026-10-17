# Scope and boundaries

## Research question

What subscription allowance applications, provider meters, and user-reported consumption evidence are available for coding-oriented AI subscriptions and providers during 2026-09-05 through 2026-10-05, and what can those reports support about allowance behavior?

## In scope

- User-authored posts and dated comments published from 2026-09-05 through 2026-10-05 inclusive on Reddit, Hacker News, GitHub community discussions, and developer-tool repositories.
- Coding-oriented subscription surfaces including GitHub Copilot, Cursor, Windsurf, OpenCode Go, Kimi Code, Z.ai/GLM Coding Plan, and Ollama Cloud.
- Official provider documentation retrieved on 2026-10-05, used only to label published quota rules and provider meters; policy values are not subscriber usage observations.
- Third-party allowance meters and local usage-log tools, recorded as software capability claims rather than evidence of a population-level usage distribution.

## Out of scope

- Posts outside the date window as usage evidence. Older HN results are retained only as bounded-search context.
- Unrelated providers or paid plans (for example, a Devin account found while searching Windsurf).
- Synthetic tracker demonstrations, self-reported numbers whose measurement period crosses the cutoff without a separable in-window value, and estimates without a clear account or local measurement basis.
- Inferring a plan tier from model name, reset cadence, company reimbursement, or the provider's current policy.

## Date and plan rules

- A user datapoint is eligible only when its post or specific comment date is within the window. The comment date is separate from the containing thread date.
- Every included user datapoint records `plan_tier_as_reported` verbatim as a specific named tier or exactly `not stated`. A plan mentioned by the original poster is not transferred to a commenter.
- When a report says only “Pro,” the evidence preserves “Pro” and records unknown legacy/new status separately; it does not expand the tier name or infer grandfathering.

## Measurement classes

| Class | Meaning |
|---|---|
| `provider_account_meter` | A user's reading of a provider account allowance/usage meter. |
| `published_provider_quota` | Provider-authored allowance, reset, or quota rules; not an individual's consumption. |
| `local_usage_log_estimate` | A user's local app/request/token counters or derived estimate; not automatically the provider's billed counter. |
| `user_extrapolation` | A user's projection derived from an account meter and rough request counts; not an observed limit or local raw log. |
| `api_cost_equivalent` | A user's API price or request-cost comparison; not subscription-meter use. |

## Search and access limits

Search used only Codex built-in `web__run`. The retained query log contains 47 exact query strings from the captured run record. The handoff transcript also referenced an earlier set of official-document searches without retaining their exact literals; those strings are not reconstructed or counted. Results are a discovery sample, not a census. HN, Windsurf-only, and Z.ai/GLM user-report coverage remains bounded to the returned search results.

## Silver Bullet workflow status

The Silver Bullet deep-research skill and its Ultradeep phase contract were read through the registered `silver-bullet` LeanCTX root. The phase artifacts in this directory apply the nine-phase workflow manually. No `/sb ultradeep` orchestration command or phase-gate command was invoked, so this package records workflow compliance at the artifact level and does not claim an actual command invocation. The previous missing-root-registration issue was corrected; current sandbox validator capacity is a separate execution limit.
