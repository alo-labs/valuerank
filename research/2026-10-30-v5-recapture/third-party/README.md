# Third-party board re-read for the v5 cohort (2026-10-30)

These are the added-leaf boards for the 27-configuration AA Intelligence Index v5 cohort (`../cohort.json`, O132). They
were re-read with the 2026-10-25 methods (`../../2026-10-25-board-reread/`):

- public pages only, with no sign-in, paid export or private API;
- all web content treated as data;
- exact-configuration matching (O36): model version **and** reasoning effort must match, and no value moves across efforts.

MiMo-V2.6-Flash is matched at Xiaomi's documented default under O135 (`mimo-flash-effort.md`). FrontierCode and the
Terminal-Bench leaf come from AA and are not covered here; tbench.ai was read for reference.

To rebuild: `python3 -I research/2026-10-30-v5-recapture/third-party/build_coverage.py`. It writes:

- `coverage-2026-10-30.json`: Bug Hunt, LiveBench 2.0 Overall, AI Coding Daily and tbench.ai, laid out like
  `other-coverage-2026-10-25.json`;
- `vals-catalogue-2026-10-30.json`: Vibe Code v1.1 and Code Migration v1.1, laid out like `vals-catalogue-2026-10-25.json`.

## Sources, methods and capture instants (UTC)

| Board | Read at | Method / evidence | Board's own date |
|---|---|---|---|
| Bug Hunt Bench | 2026-10-30T22:19:18Z (benchmark.json); repo cloned within the next 2 min | `bughunt/benchmark.json` from bughunt.productcompass.pm/data/benchmark.json. The public repo was cloned (`git clone`); the GitHub API is not enabled for this session. `results/` files are saved at HEAD `12497971d928cc5ad97a184755734720388bc07f` (2026-10-27T12:17:31Z) as `combined-…csv`, `run-notes-…md`, `runs-…csv` and `coverage-…csv`, with `git-log-since-2026-10-23.txt`. Matching uses the current (non-superseded) row, which is the owner's mean when repeated runs exist. | meta.updated 2026-10-27 |
| Vals Vibe Code Bench v1.1 | 2026-10-30T22:19:54Z | The page's hashed `/_astro/benchmark_view_vibe_code_bench.J70PGD0L.json` was saved as `vals/vibe-code.json`. | updated 2026-10-29; 123 models |
| Vals Code Migration v1.1 | 2026-10-30T22:19:55Z | `/_astro/benchmark_view_code_migration_v1_1.BRBJcaE4.json` was saved as `vals/code-migration-v1-1.json`. Model pages (MiMo Flash, Terra, Carbon) are in `vals/_models/`, read 22:20:23Z. | updated 2026-10-28; 29 models |
| LiveBench 2.0 | 2026-10-30T22:20:46Z | The site bundle (`livebench/site-main.js`, main.33d79ac9.js) was read, and the release files were saved as `livebench/*-20261025.*` and `*-20261014.*`. Effort comes from the bundle's model metadata. Overall uses the release's `_overall_weights` (Long Agentic 2, Coding 1.5, Design 1.5, others 1), as O67. | release 20261025 ("25 October 2026"); files Last-Modified 2026-10-30T22:01:11Z |
| AI Coding Daily | page 2026-10-30T22:21:36Z; all rows 22:21:52Z | `aicd/leaderboard.html` (50 rows shown). A Livewire POST to `/livewire-71a08158/update` with `hiddenOlderModelIds=[]` gave `aicd/leaderboard-allrows.html` (68 rows; `bestHarnessOnly` false). Parsed rows, with the harness, test date and age text for each, are in `aicd/*-parsed.json`. The MiMo Flash model page is in `aicd/model-pages/`. | no board date; latest row 2026-10-27 |
| tbench.ai Terminal-Bench 4.0 | 2026-10-30T22:22:49Z | Headless Chromium 1600×1200 with no sign-in; there was no cookie banner. The page redirects to the home page. Saved files: rendered text, table and screenshot in `tbench/tb4-scrape-2026-10-30.{json,png}`; the page's embedded 35-row leaderboard payload parsed in `tbench/tb4-rows-parsed-2026-10-30.json`. | leaderboard updated_at 2026-10-23T00:29:02Z (unchanged) |
| Xiaomi MiMo API docs | 2026-10-30T22:23:55Z to 22:24:15Z | Saved in `mimo/` (see `mimo-flash-effort.md`). | — |

### Changes since the 2026-10-25 read

- **LiveBench.**
  - The release pinned on 2026-10-25, **20261023, is withdrawn.** It is no longer in the bundle's release list
    (`["20261014","20261025"]`), and every `data/20261023/` file returns 404 (`livebench/release-20261023-404/`).
  - A **newer release, 20261025, exists** and is used here. Its table equals 20261023's for every shared model, except
    three Nemotron browser cells.
  - It adds `gpt-6.1-terra` (effort max) and `mistral-large-4-0`, and drops `beam-1.0`.
  - Every cohort LiveBench value is unchanged from the leaf (for example GPT-6 Luna max 64.59 and Opus 5.5 max 85.14).
  - Owner note: this release swap needs an O67-style decision.
  - `notes-20261025.json` still says "Overall is the mean of the suites… Every suite counts equally", while
    `categories.json` carries `_overall_weights`. The weighted mean is used, as before.
- **Vals.**
  - Vibe Code added `google/gemini-4-carbon` (reasoning_effort high) and `openai/gpt-6.1-terra` (max).
  - No cohort value or stderr changed; rows only gained `turn_metrics` fields.
  - Code Migration added no cohort model.
- **Bug Hunt.** It added GPT-6.1 Terra low/medium/high/xhigh/max, each a mean of 3 on Codex CLI, dated 2026-10-26/27. No
  other cohort row changed.
- **AI Coding Daily.** It added GPT-6.1-Terra Max, Xhigh, High and Medium. No other row's values changed.
- **tbench.ai.** No change.

### Rows dated after the cutoffs

**No row on any board is dated after 2026-10-30T22:15:18Z** (the v5 chart capture). The LiveBench release files'
Last-Modified is 22:01:11Z, which is earlier. No AI Coding Daily row shows an "N hours/minutes ago" age; the ages are
"3 days ago" and older.

These rows are dated after the old 2026-10-25 cutoff:

- Bug Hunt GPT-6.1 Terra rows: max, xhigh and high on 2026-10-26; medium and low on 2026-10-27.
- AI Coding Daily GPT-6.1-Terra rows: Max and Xhigh tested 2026-10-27 ("3 days ago"); High and Medium tested 2026-10-26
  ("4 days ago").
- LiveBench release 20261025.
- Vals boards updated 2026-10-28/29 (Vals dates the Terra model 2026-10-26 and Carbon 2026-10-28).

## Coverage: configuration × board

Values by board:

- Bug Hunt: fixed of 105.
- Vibe Code and Code Migration: % (Vals stderr in the JSON).
- LiveBench: weighted Overall.
- AI Coding Daily: the non-bug leaf (Laravel + React-TS + Edge-case, max 60), with the total (max 70) in brackets.
- tbench.ai: resolution %.

"—" = no exact match; non-matching rows at other efforts are listed in each cell's note in the JSON. "P" = plausible
(model matches, effort not confirmable; owner check under O135).

| Configuration | Bug Hunt | Vibe Code v1.1 | Code Migration v1.1 | LiveBench 2.0 Overall | AI Coding Daily | tbench.ai TB 4.0 |
|---|---|---|---|---|---|---|
| GPT-6 Luna low | 4 (single) | — | — | — | — | — |
| GPT-6 Luna medium | 4 (single) | — | — | — | 40.2 (43.74; Codex CLI, 2026-09-30) | — |
| GPT-6 Luna high | 9 (single) | — | — | — | 47.73 (53.04; Codex CLI, 2026-10-01) | — |
| GPT-6 Luna xhigh | 14 (single) | — | — | — | 49.94 (56.4; Codex CLI, 2026-10-01) | — |
| GPT-6 Luna max | 18.3 (mean 3) | 81.649 | 46.669 | 64.59 | 51.99 (59.07; Codex CLI, 2026-10-01) | 16.36 |
| Claude Haiku 5.5 low | 11 (single) | — | — | — | — | — |
| Claude Haiku 5.5 medium | 12 (single) | — | — | — | 51.32 (58.2; Claude Code, 2026-10-08) | — |
| Claude Haiku 5.5 high | 16 (mean 2) | — | — | — | 51.55 (58.63; Claude Code, 2026-10-08) | — |
| MiMo-V2.6-Flash (thinking enabled, O135) | P 23.3 (mean 3, effort "default", OpenRouter) | P 78.96 | P 39.552 | — | **45.48** (53.29; "MiMo-V2.6 Flash (High)", OpenCode, 2026-10-02) | — |
| GPT-6.1 Terra low | 6 (mean 3) | — | — | — | — | — |
| GPT-6.1 Terra medium | 7.3 (mean 3) | — | — | — | 46.9 (54.61; Codex CLI, 2026-10-26) | — |
| GPT-6.1 Terra high | 9.7 (mean 3) | — | — | — | 46.69 (54.82; Codex CLI, 2026-10-26) | — |
| GPT-6.1 Terra xhigh | 11.3 (mean 3) | — | — | — | 48.13 (57.09; Codex CLI, 2026-10-27) | — |
| GPT-6.1 Terra max | 40.7 (mean 3) | 83.997 | — | 77.79 | 52.49 (60.41; Codex CLI, 2026-10-27) | — |
| GPT-6.1 Sol low | 22.5 (mean 2) | — | — | — | 52.7 (61.45; Codex CLI, 2026-10-19) | — |
| GPT-6.1 Sol medium | 29 (mean 2) | — | — | — | 55.67 (65.05; Codex CLI, 2026-10-19) | — |
| GPT-6.1 Sol high | 36.5 (mean 2) | — | — | — | 56.83 (66.0; Codex CLI, 2026-10-19) | — |
| GPT-6.1 Sol xhigh | 42.7 (mean 3) | — | — | — | — | — |
| GPT-6.1 Sol max | 44.3 (mean 3) | 88.931 | 77.324 | 84.07 | — | 58.18 |
| GPT-6 Astra high | 35 (single) | — | — | — | 56.77 (66.35; Codex CLI, 2026-10-01) | 57.88 (payload only) |
| GPT-6 Astra xhigh | 43 (single) | — | — | — | — | 57.88 (payload only) |
| GPT-6 Astra max | 45 (mean 3) | 89.594 | 80.579 | 85.64 | — | 58.18 |
| Claude Opus 5.5 high (fallback) | 31.7 (mean 3) | — | — | — | 57.68 (67.26; Claude Code, 2026-10-20) | — |
| Claude Opus 5.5 xhigh (fallback) | 36 (mean 3) | — | — | — | — | — |
| Claude Opus 5.5 max (fallback) | 41.7 (mean 3) | 90.294 | 81.012 | 85.14 | — | 64.85 |
| Claude Sonnet 5.5 max (fallback) | 51.3 (mean 3) | 92.392 | 86.875 | 80.04 | — | 61.82 |
| Gemini 4 Carbon high | — | 89.06 (reasoning_effort high) | — | — | — | — |

Notes on matching:

- **Bug Hunt.** All rows are Codex CLI for OpenAI models and Claude Code for Anthropic models.
- **Vals.** Vals runs OpenAI models at reasoning_effort max and Anthropic models at compute_effort max only, so lower
  efforts are absent.
- **LiveBench.** LiveBench runs each model once at its top effort.
- **AI Coding Daily.**
  - It lists no Luna Low, Haiku Low, Terra Low, Sol Xhigh/Max, Astra Xhigh/Max, Opus Xhigh/Max, Sonnet Max or Gemini 4
    Carbon row.
  - Each matched configuration has a single row, so no harness tie-break (I50 M2) is needed.
- **tbench.ai.** The rendered table shows each model's best effort only. The Astra high and xhigh rows exist only in the
  page's embedded data.

## Rankings with every third-party leaf

- **Max-effort ranking** (Bug Hunt, Vibe Code, Code Migration, LiveBench 2.0 Overall; plus FrontierCode and
  Terminal-Bench from AA):
  - Complete at exact: **GPT-6 Luna max, GPT-6.1 Sol max, GPT-6 Astra max, Claude Opus 5.5 max, Claude Sonnet 5.5 max**.
  - Missing one leaf: **GPT-6.1 Terra max** has no Code Migration row.
  - Vibe Code only: Gemini 4 Carbon.
  - MiMo-V2.6-Flash has no LiveBench row, and its Bug Hunt and Vals cells are plausible only.
- **AI Coding Daily ranking** (Bug Hunt, AI Coding Daily; plus FrontierCode and Terminal-Bench from AA):
  - Complete at exact:
    - GPT-6 Luna medium, high, xhigh and max;
    - Claude Haiku 5.5 medium and high;
    - GPT-6.1 Terra medium, high, xhigh and max;
    - GPT-6.1 Sol low, medium and high;
    - GPT-6 Astra high;
    - Claude Opus 5.5 high.
  - Pending the owner's O135 check of the Bug Hunt "default" row: **MiMo-V2.6-Flash**, whose AI Coding Daily cell is exact.
