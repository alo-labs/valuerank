# ValueRank v1.7.0 refresh record

- Capture date: 2026-09-29
- Benchmark source: Artificial Analysis Intelligence Index v4.3.2
- Cohort: all 21 models on the current DeepSWE Best page

This refresh updates every generated ValueRank ranking view from source snapshots captured on 2026-09-29 or the latest pinned benchmark release available on that date. Graphify orientation identified the dependency path from the model roster and source adapters through `.refresh/v1.4/build_scores.py`, the cost routes, and the Markdown and site emitters.

## Source changes and evidence boundaries

- DeepSWE Best was read in the built-in browser. The page showed 113 tasks, 91 repositories, five languages, and a source update of 2026-09-22. The current 21-row Best roster is retained in its page order and at its displayed effort.
- Artificial Analysis v4.3.2 replaces v4.2 as the current index input. Its current official component list includes AA-Briefcase v1.1, GDPval-AA v2.1, AutomationBench-AA, Terminal-Bench 4.0, SciCode, HLE, GDP.pdf, CritPt, AA-Omniscience Accuracy, AA-Omniscience Non-Hallucination, and AA-LCR v1.1. The captured first-party model payloads are pinned in `.refresh/v1.4/aa/aa_v432_snapshot.json`.
- Gemini 3.7 Flash’s AA Index is marked as an owner estimate because the selected page identifies it as estimated. AA Omniscience reports hallucination rate; ValueRank derives Non-Hallucination as 1 minus that rate.
- LiveBench uses the official 2026-06-25 release data pinned at commit `7be9f746f36a6f007dd78461f67cb7d06cfe2304`. The live release date is older than this capture date; the source commit and release date are recorded separately.
- The Terminal-Bench 4.0 official view is a built-in-browser snapshot. Official leaderboard rows and provider claims are presented separately. The owner table directly matches 11 of 21 ValueRank models. DeepSeek’s 31.2% Terminal-Bench 4.0 provider claim raises eligible current-route coverage to 12/21; nine rows remain unavailable. The provider result is for V4.1-Flash, and DeepSeek states the `deepseek-v4-flash` API name currently routes to that model. It is not a direct measurement of retired V4 Flash.
- Google DeepMind’s 34.0% GDP.pdf claim and 30.4% AutomationBench private-set claim are recorded as audit-only. The model card does not establish the exact selected effort and AA evaluation implementation needed to place either claim in a ValueRank model cell.

## Benchmark evidence policy

When a benchmark owner has not published a result for a model, use a model-provider-published result when available. Preserve the result as a provider claim with a direct source citation; require the same benchmark version and evaluated model variant; do not transfer across versions or variants. Keep an unmatched or underspecified claim audit-only. Replace the claim with the benchmark owner's result when that result becomes available. This policy was added to the global agent instructions on 2026-09-29.

## Ranking and cost decisions

- Keep all 21 current DeepSWE models; do not collapse families, use proxy models, or neutral-fill missing values.
- Retain only zero-gap primary dimensions. LiveBench Instruction Following is eligible because the pinned release covers the entire roster. AA Speed has only 20/21 numeric values and is excluded. Terminal-Bench 4.0 and AutomationBench-AA have incomplete eligible coverage and remain supplemental.
- AA total evaluation cost is missing for one selected page, so the primary cost dimension uses one cohort-wide DeepSWE cost basis. Captured AA costs remain visible as raw source data.
- Preserve v1.5.0 ranks in `.refresh/v1.4/ranking_history_v1.5.json` before writing v1.6.0 ranks to the site history.
- Cost rankings retain both API Costs and Plan Costs views. The ChatGPT Pro allowance multiplier is an estimate based on a community-observed allowance, not an official OpenAI quota; current subscription access and the pause on new sign-ups/upgrades are separately attributed. OpenCode Go’s GLM-5.3 Flash route reflects the current $60 monthly usage quota.
- Provider inputs, plan routes, selected variants, and source values remain in the machine-readable refresh files.

## Reproduction

Use the pinned snapshots and project builders in this order:

```sh
python3 .refresh/v1.4/build_deepswe_v14.py .refresh/v1.4/deepswe-browser-2026-09-29.json .refresh/v1.4/deepswe.json
python3 .refresh/v1.4/build_aa_metrics.py
python3 .refresh/v1.4/fetch_livebench.py
python3 .refresh/v1.4/build_tb4.py .refresh/v1.4/tb4-browser-2026-09-29.json .refresh/v1.4/tb4.json
python3 .refresh/v1.4/build_scores.py
python3 .refresh/v1.4/emit_v14_docs.py
python3 scripts/generate_tb4_page.py
```

The captured TB4 and DeepSWE snapshots were made with the built-in browser. AA page payloads and the pinned LiveBench release data are preserved locally. The refresh script that launches a separate Playwright browser is intentionally not part of this reproduction sequence.
