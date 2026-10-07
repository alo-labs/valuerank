# ValueRank project instructions

## Required model inclusion

- Include every model represented on Artificial Analysis' Pareto frontier of Intelligence Index score versus the total USD cost to run the Intelligence Index benchmarks. Use total benchmark cost, not cost per task or token price.
- Capture the complete selected catalog and retain exact model identities, reasoning efforts, observation dates, and direct owner links in the reconciliation inventory. Reconcile frontier entrants on each routine refresh; a manually maintained roster or missing supplementary benchmark must not silently exclude a frontier model.
- Preserve configuration-specific evidence. Do not transfer benchmark results between reasoning efforts or model versions. Report missing benchmark coverage explicitly and apply the documented scoring policy.

## Subscription allowance value-multiple evidence

- For providers other than the explicitly selected Anthropic/Codex SemiAnalysis comparison below, count only actual end-user-reported usage measurements priced at API rates as the value-multiple numerator. Accept the user's API-priced estimate as a reported estimate even when the raw token ledger is not published; label what cannot be independently reproduced.
- Never use a model provider's published allowance, quota, usage multiplier, or marketing estimate as the numerator. First-party information may establish subscription fees or API rate cards, but not the measured allowance value.
- Match reported API-priced usage to the exact model variant(s) the user says they used. Keep mixed-model or unidentified use at provider/plan level; do not transfer it to a specific ValueRank model.
- Record the end user's plan tier and report date for every data point, plus the measurement window where stated. Use reports from the preceding month and exclude measurements that fall outside that window when the report isolates them.
- For Anthropic and Codex, use the latest SemiAnalysis analysis explicitly selected by the user on 2026-10-07: https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x. This authorization supersedes TiboTattle-only sourcing for the current Anthropic/Codex comparison. Label SemiAnalysis results as controlled subscription-account measurements with workload projections, not individual crowdsourced reports or provider claims. Preserve exact model, plan, workload, publication date and allocation regime. Historical TiboTattle data remain aggregates of installation/account tracks, not individual-user observations; do not mix them into current SemiAnalysis figures.
- Keep subscription fee evidence separate from allowance evidence. A provider's published price can be the denominator only when the reported tier and price mapping are supported.

## Subagents

- For work in this project, launch subagents with GPT-6.1 Sol at Medium reasoning effort (`model: gpt-6.1-sol`, `reasoning_effort: medium`). The user escalated from GPT-6 Luna Max to Sol Low; Sol Low's first 10 recorded assessments also averaged below 4.75, triggering the next effort level under the assessment policy. This preference applies only to ValueRank and must not be copied into global Codex instructions. Continue the assessment-based effort adjustment policy using actual completed-run scores.
- Give each subagent an explicit bounded scope, required inputs, deliverable, and file ownership where edits are involved. Tell agents to preserve changes made by others.
- Independently inspect and validate every completed subagent result against its sources, files, or execution evidence. Rework material deficits with the same required model and effort.
- After each completed subagent run, provide a concise user-facing micro-report naming the model and effort, task and result, independently verified evidence, defects or omissions, what remains unverified, and whether rework is needed.
- Maintain `subagent-model-scores.csv` at the ValueRank project root (`/Users/shafqat/valuerank`) for this project only. Preserve existing rows; after each completed run is independently assessed, append a row with exactly four columns: `timestamp,model_slug,reasoning_effort,score`. Use an ISO 8601 UTC timestamp, exact model slug, actual effort in lowercase, and an integer score from 0 to 5. Record each follow-up or rework run separately. Do not invent historical scores or duplicate a run.
