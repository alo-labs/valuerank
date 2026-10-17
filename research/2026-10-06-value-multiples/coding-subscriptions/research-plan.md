# Research plan

## Mode rationale

Ultradeep is appropriate because this is a high-precision, multi-model comparison with strict identity, time-window, price, and numerator requirements. False matches across model versions or plan tiers could produce materially wrong multiples.

## Retrieval boundary

Use only Codex In-app Browser through `cua_repl`, as requested. Search Reddit first, then Hacker News, then developer communities such as GitHub discussions/issues and provider forums. Capture exact queries and visible search outcomes in `query_log.jsonl`; open candidate direct pages and verify dates, author/comment identity, plan, model, measured interval, and consumption units. Do not use Edge or Chrome extension browsers, `web.run`, search APIs, `curl`, `wget`, or raw HTTP/fetch.

The initial CUA browser inventory exposed two Edge extension surfaces and did not expose the required `iab` browser; the first `createBrowserTab("iab", ...)` attempt returned `Browser is not available: iab`. This is recorded as an access check, not a research no-hit. Discovery remains pending unless the Codex in-app browser becomes available.

## Search branches

1. For each target model, search Reddit for exact model name plus `Go`, `Go Plus`, `Z.AI Code`, `Ollama`, `subscription`, `usage`, `tokens`, `credits`, `limit`, and the date window.
2. Search Reddit by provider/plan for measured per-model logs, account screens, token counts, context/output breakdown, and references to API-cost comparisons.
3. Search Hacker News for exact model/version and subscription/usage terms; record bounded no-hits separately from Reddit results.
4. Search developer communities for first-person issue/discussion posts that include the plan tier and actual measured use.
5. For any candidate, verify exact model API rates and plan cost from dated primary sources; these establish prices only and cannot supply the use numerator.
6. Re-run targeted searches for every model still lacking candidate or bounded no-hit coverage.

## Eligibility and calculations

Apply `scope.md` literally. Record source post evidence separately from official API-rate and plan-price evidence. For each eligible record, calculate only the observed interval's priced use, with a transparent rate/denominator trail. Do not annualize, scale by provider-published caps, substitute artificial benchmark tokens, or infer the users' price tier. Keep non-computable reports in exclusions with the exact missing field(s).

## Triangulation and critique

Cross-check every potentially eligible user observation against the direct post and matching primary pricing source. Adversarial review asks whether identity/model strings are ambiguous, whether token fields double-count hidden reasoning or cache tokens, whether logs are local rather than billing meters, whether reported subscription price belongs to the author, and whether reporting/measurement dates cross the cutoff. Ultradeep requires three critique cycles and a documented retrieval loopback or residual blocker.

## Package and gates

Produce source, evidence, claim, exact query, model-coverage, calculation, and exclusion ledgers plus a concise report and handoff. Run Silver Bullet report, citation, claim-support, and nine-phase validators. Add a small deterministic validator for model coverage and arithmetic/crosswalks. Preserve raw validator outputs and record unavailable routes without describing them as workflow unavailability.
