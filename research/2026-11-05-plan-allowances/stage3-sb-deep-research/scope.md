# Scope (DR-SCOPE): plan-allowance user reports, stage 3 of the November 2026 release

## Bounded question

Which user-reported measurements of subscription-plan allowances, expressed as the dollar value of API-priced usage consumed per rate-limit window (5-hour, weekly, monthly), were published or updated since about 2026-10-19 for the coding-agent plans below, which of them satisfy the O11 qualification rule, and which entries in the stage-1 (plain web search) and stage-2 (Claude Deep Research) records are wrong, incomplete, or contradicted?

## In scope

| Provider | Plans | Models (as named by the task) | Surfaces |
|---|---|---|---|
| Anthropic | Pro, Max 5x ("Max" after 2026-10-30), Max 20x ("Ultra" after 2026-10-30) | Opus 5.5 (Sonnet 5.5, Haiku 5.5 checked) | Claude Code |
| OpenAI | ChatGPT Plus, Pro 100, Pro 200, Pro 500, Business/Team | GPT-6.1 Sol, GPT-6.1 Terra, GPT-6 Astra (Luna checked) | Codex |
| Google | AI Pro, AI Ultra 5x, AI Ultra 20x | Gemini 4 Argon (Carbon checked) | Antigravity, Gemini CLI (agy) |
| Moonshot | Kimi legacy Allegretto/Allegro (CN), new Plus/Pro/Max/Ultra | K3.1 Pro | Kimi Code |
| Xiaomi | MiMo Token Plan Lite/Standard/Pro/Max | MiMo-V2.6-Pro, -Flash | OpenCode, Claude Code compatible |
| MiniMax | M Plan Go/Explore/Build, legacy Token Plan | MiniMax-M3.1-Flash | MiniMax CLI, OpenCode |

Venues: Reddit (through the Arctic Shift mirror), Hacker News (Algolia), GitHub issues, X (posts reached through fxtwitter and links), LINUX DO (through the locdd.com mirror and one directly readable topic), V2EX, Google AI developer forum, blogs, ccusage-style dumps, aiplans.dev reports.

## O11 qualification rule (applied as written in the task)

A report counts only if it states (1) plan tier, (2) window, (3) the measured token or dollar consumption to the limit (or per meter fraction), and (4) how the dollar figure was computed. Reports missing one element are labelled provisional or excluded. Concordance for a cell: largest lower bound <= 1.20 x smallest upper bound across at least two independent, non-provisional reports in one partition (O86). Controlled measurements by SemiAnalysis are out of scope for this stage (they are a separate owner-selected route).

## Out of scope

- Provider-published allowances, marketing multipliers, and aggregator figures as numerator (Wokey, modeldial, codexradar): cross-check only.
- Editing any ValueRank data file, `plan_reports.json`, or anything under `/home/user/silver-bullet`.
- Reports measured wholly before 2026-10-19 (listed only where they explain a partition).
- Rows for other providers (DeepSeek has no first-party plan; Z.ai/GLM not requested).

## Window and cutoff handling

- Window opens 2026-10-19; priority 2026-10-25 .. 2026-11-05.
- Release cutoff from stages 1 and 2: 2026-11-01T06:10Z. Reports measured after it (to 2026-11-05) are retrieved because the question runs to the current date, but are labelled "after cutoff".

## Assumptions

1. Prices are the API list prices stage 1 used (see `run_manifest.json`). Where a provider's published price changes (Argon introductory pricing ends 2026-11-30), the dollar figure is stated with the price basis.
2. A meter percentage is a rounded integer, so each reading carries +-0.5 percentage points at each end (the range method used by stage 1 and 2).
3. Observer independence cannot be verified on locdd.com (pseudonyms are reassigned per post); every locdd-sourced report carries that caveat.

## Success criteria for this run

- Every row in `decision-record.md` names provider, plan, window, report URL, date, dollar range, qualification label, and any correction to the existing record.
- New qualifying reports, corrections, contradictions, and blocked sources are each listed explicitly.
- Validation scripts run against this directory.
