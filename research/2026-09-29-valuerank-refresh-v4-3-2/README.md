# ValueRank v1.9.2 refresh record

- Initial source capture: 2026-09-29; Claude Opus 5.5 inclusion follow-up: 2026-09-30
- Benchmark source: Artificial Analysis Intelligence Index v4.3.2
- Model universe: 22 AA-mapped ValueRank comparison candidates
- Primary ranked cohort: 10 candidates with exact AA DeepSWE v1.1 and Bug Hunt owner results; 12 remain source-only
- Current main rank: 12 zero-gap dimensions, including DeepSWE v1.1 and Bug Hunt

This refresh updates every generated ValueRank ranking view from pinned source snapshots and the 2026-09-30 Claude Opus 5.5 follow-up. Graphify orientation identified the dependency path from the model roster and source adapters through `.refresh/v1.4/build_scores.py`, the cost routes, and the Markdown and site emitters.

## Source changes and evidence boundaries

- The final DeepSWE v1.1 result source is AA's [Coding Agent Index v1.5 chart](https://artificialanalysis.ai/agents/coding-agents?coding-agents-performance-chart=deep-swe-v1.1), read in the built-in browser. It shows 25 of 25 agent/model configurations over 113 tasks, with scores averaging pass@1 over three attempts per task. The full capture is pinned in `.refresh/v1.4/aa_deepswe.json`. The earlier DeepSWE Best page snapshot is retained only as historical audit material and is not used for current scores.
- Artificial Analysis v4.3.2 replaces v4.2 as the current index input. Its current official component list includes AA-Briefcase v1.1, GDPval-AA v2.1, AutomationBench-AA, Terminal-Bench 4.0, SciCode, HLE, GDP.pdf, CritPt, AA-Omniscience Accuracy, AA-Omniscience Non-Hallucination, and AA-LCR v1.1. The captured first-party model payloads are pinned in `.refresh/v1.4/aa/aa_v432_snapshot.json`.
- Claude Opus 5.5 is included using its exact AA model profile and max-effort benchmark variant. AA's DeepSWE v1.1 chart records Claude Code / Opus 5.5 / max at 68% pass@1. The Bug Hunt owner board records Claude Code / Opus 5.5 / max at a mean 41.7/105 across three runs. The AA profile identifies the evaluated configuration as max effort with fallback.
- Gemini 3.7 Flash’s AA Index is marked as an owner estimate because the selected page identifies it as estimated. AA Omniscience reports hallucination rate; ValueRank derives Non-Hallucination as 1 minus that rate.
- LiveBench uses the official 2026-06-25 release data pinned at commit `7be9f746f36a6f007dd78461f67cb7d06cfe2304`. The release predates Claude Opus 5.5, so its unavailable Instruction Following result remains missing and that dimension is excluded from the zero-gap composite.
- The Terminal-Bench 4.0 official view is a built-in-browser snapshot. Official leaderboard rows and provider claims are presented separately. The owner table directly matches 11 of 22 ValueRank models. DeepSeek’s 31.2% Terminal-Bench 4.0 provider claim raises eligible current-route coverage to 12/22; ten rows remain unavailable. The provider result is for V4.1-Flash, and DeepSeek states the `deepseek-v4-flash` API name currently routes to that model. It is not a direct measurement of retired V4 Flash.
- Google DeepMind’s 34.0% GDP.pdf claim and 30.4% AutomationBench private-set claim are recorded as audit-only. The model card does not establish the exact selected effort and AA evaluation implementation needed to place either claim in a ValueRank model cell.

## Benchmark evidence policy

When a benchmark owner has not published a result for a model, use a model-provider-published result when available. Preserve the result as a provider claim with a direct source citation; require the same benchmark version and evaluated model variant; do not transfer across versions or variants. Keep an unmatched or underspecified claim audit-only. Replace the claim with the benchmark owner's result when that result becomes available. This policy was added to the global agent instructions on 2026-09-29.

## Ranking and cost decisions

- Set DeepSWE v1.1 priority to 25. On the 10-model primary cohort, DeepSWE carries a 22.32% ValueRank weight.
- Include Bug Hunt Bench in the main rank at priority 20 (17.86%). Its owner scoreboard has 17 exact results in the 22-candidate roster; 10 overlap with exact AA DeepSWE model variants and enter the composite.
- Keep a separate Bug Hunt emphasis view at priority 30 (24.59%) for the same 10 exact-overlap models.
- Preserve all 25 AA chart configurations and their agent, model variant, and effort fields. Do not transfer scores across model versions or composite-agent configurations; models lacking the full overlap remain visible without a composite rank.
- Retain only zero-gap dimensions across the 10-model overlap. LiveBench Instruction Following, legacy GPQA Diamond, Terminal-Bench 4.0, and AA Speed have gaps and remain supplemental. The main rank uses 12 dimensions.
- Default/API Costs uses AA total evaluation cost for the fixed index suite; the Plan Costs view divides the same amount by each model's highest eligible Value Multiple. Both inputs cover all 10 primary models. No DeepSWE leaderboard average-cost values enter the current score.
- Preserve only recorded historical ranks in the site history; this follow-up adds the v1.9.2 cost-route snapshot without copying current ranks into unobserved prior versions.
- Cost rankings retain both API Costs and Plan Costs views. GPT-6 Astra uses a 28.3× ChatGPT Pro 20x estimate and GPT-5.6 Sol uses 37.0×, derived from model-specific Plus measurements and OpenAI’s published 20x Pro usage tier. Both are labeled community-observed estimates, not provider-published dollar quotas. The route models the current reduced Pro 200 allowance; eligible grandfathered accounts retain prior allowance through 2026-10-29. GPT-5.6 Sol’s current API price is promotional through at least 2026-11-21. OpenCode Go’s GLM-5.3 Flash route reflects the current $60 monthly usage quota. Claude Opus 5.5 is now eligible for the existing Claude Max 20x route based on Anthropic's plan and model pages; its 40× value remains an independent high-water estimate, not a model-specific allowance measurement.
- Provider inputs, plan routes, selected variants, and source values remain in the machine-readable refresh files.

## Codex allowance update

The September 25 community measurement reports Plus-plan API-equivalent allowances of $283/month for GPT-6 Astra and $370/month for GPT-5.6 Sol. Normalizing each to Pro 20x uses `Plus API equivalent × 20 ÷ $200`, yielding $5,660/month (28.3×) and $7,400/month (37.0×), respectively. The source assumes six fresh five-hour windows per week and reports a single account. OpenAI's current Codex pricing page confirms Pro 20x is 20 times Plus usage and publishes model-specific per-window message ranges; actual consumption varies with task size, context, and model. GPT-6 Luna and GPT-6 Sol measurements are retained as source context only because those exact model IDs are outside this release's ranked cohort. GPT-5.6 Luna is not treated as GPT-6 Luna.

OpenAI's current Pro help page says eligible legacy Pro 200 subscribers retain their previous allowance through 2026-10-29 before moving to the lower allowance. The route estimates represent the current reduced Pro 20x tier and exclude that temporary legacy allowance. OpenAI's API rate card confirms the GPT-5.6 Sol promotional rates used in the Reddit estimate and says they are available at least through 2026-11-21.

## Opus 5.5 inclusion follow-up

The refresh initially omitted Claude Opus 5.5 because the ranking roster was pinned to 21 models. That roster guard is now 22, and the selected Opus 5.5 profile is represented consistently across AA, DeepSWE, Bug Hunt, LiveBench, Terminal-Bench, the scoring history, and publication outputs. Opus 5.5 ranks #3 overall and #1 on the primary quality score; it ranks #3 in the Bug Hunt emphasis view. LiveBench Instruction Following, legacy GPQA Diamond, Terminal-Bench 4.0, and AA Speed remain excluded from the primary composite where the required exact result is unavailable.

## Reproduction

Use the pinned snapshots and project builders in this order:

```sh
python3 .refresh/v1.4/build_aa_metrics.py
python3 .refresh/v1.4/fetch_livebench.py
python3 .refresh/v1.4/build_tb4.py .refresh/v1.4/tb4-browser-2026-09-29.json .refresh/v1.4/tb4.json
python3 .refresh/v1.4/build_scores.py
python3 .refresh/v1.4/emit_v14_docs.py
python3 scripts/generate_tb4_page.py
```

The AA DeepSWE chart capture and TB4 snapshot were made with the built-in browser. AA page payloads, all 25 DeepSWE configurations, the Bug Hunt owner snapshot, and the pinned LiveBench release data are preserved locally. The current scoring and external-source adapters derive the model roster from AA-mapped data; the historical DeepSWE Best snapshot is not required.
