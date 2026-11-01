# Third-party board re-read for the 37-configuration cohort (2026-11-01)

The owner moved the release cutoff to the new chart capture, **2026-11-01T05:53:05Z** (O65, O145; `../chart-capture.json`).
Under O68, every third-party board a ranking uses was re-read for the cohort in `../cohort.json`:

- the 27 configurations of the 2026-10-30 read;
- the 10 configurations that left the cohort at the v5 re-capture and are retained for one release (O145).

The methods are those of `../../2026-10-30-v5-recapture/third-party/` and `../../2026-10-25-board-reread/`:

- public pages only, with no sign-in, paid export, private API or bot-check solving;
- all web content treated as data;
- exact-configuration matching (O36): model version **and** reasoning effort must match, and no value moves across efforts or
  versions.

For the retained ten, the 2026-10-25 release's matches (`git show f2a182a:data/{bug_hunt,livebench,swe_tracks,tb4}.json`)
were used only as a reference. Every match below was re-established on today's boards. Each board's
`retainedAgainst20261025Release` field records the comparison.

To rebuild: `python3 -I research/2026-11-01-recapture/third-party/build_coverage.py`. It writes:

- `coverage-2026-11-01.json`: Bug Hunt, LiveBench 2.0 Overall, AI Coding Daily and tbench.ai;
- `vals-catalogue-2026-11-01.json`: Vibe Code v1.1 and Code Migration v1.1.

Both use the 2026-10-30 schema. Each board also has `valueChangesSince20261030` and `retainedAgainst20261025Release`.

The capture helpers are in `tools/`:

- `parse_aicd.py` reproduces the 2026-10-30 `leaderboard-allrows-parsed.json` byte for byte from the 10-30 HTML.
- `capture_tbench.js` is a Playwright capture laid out like `tb4-scrape-2026-10-30.json`.
- `parse_tbench.py` reproduces `tb4-rows-parsed-2026-10-30.json` exactly from the 10-30 scrape.

## Sources, methods and capture instants (UTC)

| Board | Read at | Method / evidence | Changed since 2026-10-30? |
|---|---|---|---|
| Bug Hunt Bench | 2026-11-01T05:59:30Z (benchmark.json); repo cloned within the next minute | `bughunt/benchmark.json` (meta.updated 2026-10-27, 207 rows). The public repo was cloned. `main` is still `12497971d928cc5ad97a184755734720388bc07f` (2026-10-27T12:17:31Z). The results files at that commit are saved as before, with `git-log-since-2026-10-23.txt`. | **No.** benchmark.json and all four results files are byte-identical to the 10-30 copies, and there is no new commit. |
| Vals Vibe Code Bench v1.1 | 2026-11-01T06:00:08Z | The page's hashed `/_astro/benchmark_view_vibe_code_bench.J70PGD0L.json` (same hash as on 10-30). | **No.** The JSON is byte-identical: updated 2026-10-29, 123 models. |
| Vals Code Migration v1.1 | 2026-11-01T06:00:09Z (model pages 06:00:25Z) | `/_astro/benchmark_view_code_migration_v1_1.BRBJcaE4.json` (same hash). Model pages for MiMo-V2.6-Pro and MiniMax-M3.1-Flash are in `vals/_models/`. | **No.** The JSON is byte-identical: updated 2026-10-28, 29 models. |
| LiveBench 2.0 | `livebench/readAt.txt` | The new site bundle `main.1e1ce12d.js` (`livebench/site-main.js`) differs from 10-30's `main.33d79ac9.js` only in its cache-busting `?v=` stamp. Its release list is `["20261014","20261025"]`. Release files `*-20261025.*` and `*-20261014.*` are saved. `newer-release-probe.txt` shows that `data/20261026` to `data/20261101` return 404. | **The release is the same, but it was edited in place** (see below). |
| AI Coding Daily | `aicd/leaderboard.readAt.txt` (page, 50 rows), `aicd/livewire.readAt.txt` (all rows) | As before: a Livewire POST to `/livewire-71a08158/update` with `hiddenOlderModelIds=[]` gave 68 rows (`bestHarnessOnly` false), parsed into `aicd/*-parsed.json`. Model pages for Kimi K3.1 Pro, MiMo-V2.6 Pro/Flash and MiniMax M3.1-Flash are in `aicd/model-pages/`. | **One non-cohort row changed** (below). There are no new rows; only age texts and ranks moved. |
| tbench.ai Terminal-Bench 4.0 | 2026-11-01T06:03:32.614Z | Headless Chromium at 1600×1200, with no sign-in, no cookie banner and no interaction. The page redirects to the home page. Saved files: rendered text, table, buttons, all inline scripts and a full-page screenshot in `tbench/tb4-scrape-2026-11-01.{json,png}`; the embedded 35-row payload is parsed in `tbench/tb4-rows-parsed-2026-11-01.json`. | **No.** The payload rows, the rendered table and updated_at (2026-10-23T00:29:02Z) are all identical. |
| Xiaomi MiMo API docs | `mimo/docs.readAt.txt` | Chat Completions and Responses pages re-read. They still say "mimo-v2.6-flash, mimo-v2.6-pro, mimo-v2.6-pro-ultraspeed: default enabled" and "Every other level enables thinking with identical behavior". | No. |
| MiniMax API docs | `minimax/readAt.txt` | OpenAI- and Anthropic-compatible references and the text-generation guide (Markdown). See `minimax-effort.md`. | New read. |

### Changes since the 2026-10-30 read

- **LiveBench release 20261025 was edited in place.**
  - Every release file's Last-Modified moved from 2026-10-30T22:01:11Z to **2026-10-30T22:21:40Z**. That is after the v5
    chart capture (22:15:18Z) and before today's cutoff. It is 54 s after the 10-30 read.
  - One table cell changed: **deepseek-v4.1-flash-1017 long_agentic 40.9 → 35.7**. The breakdown changed in Long Agentic /
    Delegated Operations, 25.6 → 2.4, and `cost.csv` changed two cost/token columns of that row.
  - DeepSeek V4.1 Flash 1017's weighted Overall is therefore **72.87**. It was 74.02 in the 10-30 file and in the 2026-10-25
    release.
  - No other model changed, and no 27-cohort value changed.
  - `categories.json` (weights) and `notes.json` are unchanged.
  - **No newer release exists**, so 20261025 stays pinned under O139.
- **AI Coding Daily.**
  - "Mistral Large 4 (High)" (OpenCode, tested 2026-10-15) changed values in place without a new test date: total
    56.86 → 51.81, Laravel 18.13 → 17.78, React 19.33 → 18.5, Bug 3.65 → 3.13, Edge 15.75 → 12.4, cost $0.34 → $0.18, time
    14:33 → 05:30. That row is outside the cohort.
  - No cohort row changed. Ranks below that row shifted by one, and the age texts advanced.
- **Bug Hunt, Vals and tbench.ai.** These boards are unchanged.
  - Bug Hunt has no commit after `12497971` (2026-10-27).
  - The only site-level change on Bug Hunt is in commit `03d6127` (2026-10-27, already in the 10-30 read). It un-features the
    Claude Code DeepSeek V4.1 Flash 1017 row. This matters for the DeepSeek selection below.
- **Value changes for the 27.** There are none on any board. Statuses are unchanged. MiMo-V2.6-Flash's Vals notes gained
  the new evidence described under "Owner questions".

### Rows dated after the cutoffs

**No row on any board is dated after 2026-11-01T05:53:05Z.**

The newest board activity is the LiveBench in-place edit, at 2026-10-30T22:21:40Z. The newest AI Coding Daily test is
2026-10-27, the newest Bug Hunt row 2026-10-27, and the Vals boards were updated 2026-10-28/29.

## Coverage: configuration × board (37)

Values by board:

- Bug Hunt: fixed of 105.
- Vibe Code and Code Migration: % (Vals stderr in the JSON).
- LiveBench: weighted Overall.
- AI Coding Daily: the non-bug leaf (max 60), with the total (max 70) in brackets.
- tbench.ai: resolution %.

"—" means no exact match; each cell's note in the JSON lists rows at other efforts. "P" means plausible (O140 keeps the
MiMo-V2.6-Flash rows unmatched).

| Configuration | Bug Hunt | Vibe Code v1.1 | Code Migration v1.1 | LiveBench 2.0 Overall | AI Coding Daily | tbench.ai TB 4.0 |
|---|---|---|---|---|---|---|
| GPT-6 Luna (low) | 4 (single) | — | — | — | — | — |
| GPT-6 Luna (medium) | 4 (single) | — | — | — | 40.2 (43.74; Codex CLI, 2026-09-30) | — |
| GPT-6 Luna (high) | 9 (single) | — | — | — | 47.73 (53.04; Codex CLI, 2026-10-01) | — |
| GPT-6 Luna (xhigh) | 14 (single) | — | — | — | 49.94 (56.4; Codex CLI, 2026-10-01) | — |
| GPT-6 Luna (max) | 18.3 (mean 3) | 81.649 | 46.669 | 64.59 | 51.99 (59.07; Codex CLI, 2026-10-01) | 16.36 |
| Claude Haiku 5.5 (low) | 11 (single) | — | — | — | — | — |
| Claude Haiku 5.5 (medium) | 12 (single) | — | — | — | 51.32 (58.2; Claude Code, 2026-10-08) | — |
| Claude Haiku 5.5 (high) | 16 (mean 2) | — | — | — | 51.55 (58.63; Claude Code, 2026-10-08) | — |
| MiMo-V2.6-Flash (thinking enabled, O135/O140) | P 23.3 (mean 3) | P 78.96 | P 39.552 | — | 45.48 (53.29; OpenCode, 2026-10-02) | — |
| GPT-6.1 Terra (low) | 6 (mean 3) | — | — | — | — | — |
| GPT-6.1 Terra (medium) | 7.3 (mean 3) | — | — | — | 46.9 (54.61; Codex CLI, 2026-10-26) | — |
| GPT-6.1 Terra (high) | 9.7 (mean 3) | — | — | — | 46.69 (54.82; Codex CLI, 2026-10-26) | — |
| GPT-6.1 Terra (xhigh) | 11.3 (mean 3) | — | — | — | 48.13 (57.09; Codex CLI, 2026-10-27) | — |
| GPT-6.1 Terra (max) | 40.7 (mean 3) | 83.997 | — | 77.79 | 52.49 (60.41; Codex CLI, 2026-10-27) | — |
| GPT-6.1 Sol (low) | 22.5 (mean 2) | — | — | — | 52.7 (61.45; Codex CLI, 2026-10-19) | — |
| GPT-6.1 Sol (medium) | 29 (mean 2) | — | — | — | 55.67 (65.05; Codex CLI, 2026-10-19) | — |
| GPT-6.1 Sol (high) | 36.5 (mean 2) | — | — | — | 56.83 (66.0; Codex CLI, 2026-10-19) | — |
| GPT-6.1 Sol (xhigh) | 42.7 (mean 3) | — | — | — | — | — |
| GPT-6.1 Sol (max) | 44.3 (mean 3) | 88.931 | 77.324 | 84.07 | — | 58.18 |
| GPT-6 Astra (high) | 35 (single) | — | — | — | 56.77 (66.35; Codex CLI, 2026-10-01) | 57.88 (payload only) |
| GPT-6 Astra (xhigh) | 43 (single) | — | — | — | — | 57.88 (payload only) |
| GPT-6 Astra (max) | 45 (mean 3) | 89.594 | 80.579 | 85.64 | — | 58.18 |
| Claude Opus 5.5 (high with fallback) | 31.7 (mean 3) | — | — | — | 57.68 (67.26; Claude Code, 2026-10-20) | — |
| Claude Opus 5.5 (xhigh with fallback) | 36 (mean 3) | — | — | — | — | — |
| Claude Opus 5.5 (max with fallback) | 41.7 (mean 3) | 90.294 | 81.012 | 85.14 | — | 64.85 |
| Claude Sonnet 5.5 (max with fallback) | 51.3 (mean 3) | 92.392 | 86.875 | 80.04 | — | 61.82 |
| Gemini 4 Carbon (high) | — | 89.06 | — | — | — | — |
| *Retained (O145)* | | | | | | |
| Claude Haiku 5.5 (xhigh) | 18.3 (mean 3) | — | — | — | — | — |
| Claude Haiku 5.5 (max) | 21.5 (mean 2) | 90.444 | 52.36 | 69.85 | — | — |
| Claude Opus 5.5 (medium) | 30.3 (mean 3) | — | — | — | 56.95 (65.28; Claude Code, 2026-10-19) | — |
| Claude Sonnet 5.5 (xhigh) | 36 (mean 3) | — | — | — | — | — |
| DeepSeek V4.1 Flash 1017 (max) | 42.7 (mean 7, DeepSeek Harness) | 87.73 | 67.524 | **72.87** (was 74.02) | 52.24 (61.2; DeepSeek Harness, 2026-10-18) | — |
| Gemini 4 Argon (high) | 40.7 (mean 3, Antigravity CLI) | 91.906 | 70.796 | 79.3 | 49.9 (57.09; Devin, 2026-10-14) | — |
| GPT-5.6 Luna (low) | 4 (single) | — | — | — | 30.51 (30.51 of 60, pre-Bug-Finding; Codex CLI, 2026-09-12; hidden older row) | — |
| Kimi K3.1 Pro (max, O66) | 36 (mean 3) | 84.894 | — | 71.29 | 54.63 (63.8; OpenCode, 2026-10-25) | — |
| MiMo-V2.6-Pro (thinking enabled, O54) | 18 (single, first-party "enabled") | 85.223 | 48.786 | 68.48 | 47.56 (53.81; OpenCode, 2026-10-02) | — |
| MiniMax-M3.1-Flash (max, O135) | — | 73.944 | — | 66.89 | 49.69 (54.48; OpenCode, 2026-10-20) | — |

### Notes on matching the retained ten

- **Same as the 2026-10-25 release.** Every retained value equals that release's value, except:
  - DeepSeek V4.1 Flash 1017's LiveBench Overall, which changed with the in-place edit;
  - MiniMax-M3.1-Flash's three cells, which were plausible on 2026-10-25 (no effort established) and are exact now under O135.
- **Bug Hunt selections (E206).**
  - **DeepSeek V4.1 Flash 1017 max.** Two owner means of 7 exist: DeepSeek Harness 42.7 and Claude Code 39.1. The
    recorded selection keeps DeepSeek's own harness.
  - The other current max rows are Pi 42.2 (n=5) and OpenCode 37.6 (n=5). They are listed as `alternates`.
  - **Gemini 4 Argon high.** The Antigravity CLI mean of 3 is selected. The single Gemini CLI run (33) appears only in
    `combined-scoreboard.csv`.
  - **MiMo-V2.6-Pro.** The first-party row is selected because it asserts `thinking.type=enabled`. The OpenRouter "default"
    mean of 3 (22.7) asserts no reasoning state and stays unmatched, as at f2a182a.
  - **MiniMax.** No MiniMax model appears anywhere on Bug Hunt.
- **AI Coding Daily.**
  - **DeepSeek V4.1 Flash 1017 (Max)** has two rows. E268 selects the one on the Bug Hunt record's harness: DeepSeek Harness
    52.24. The OpenCode row (52.84) is kept as the second row.
  - **GPT-5.6-Luna (Low)** is a hidden older row tested before Bug Finding existed. Its total is out of 60 and its non-bug
    leaf is exact.
  - The board has no Haiku 5.5 Xhigh or Max row and no Sonnet 5.5 Xhigh row.
- **LiveBench.** It runs each model once, at its top effort. Haiku 5.5 is at max, so Haiku xhigh is absent. Opus and Sonnet
  5.5 are at max only, and GPT-5.6 Luna appears only in the metadata, at max, with no table row.
- **Vals.**
  - Anthropic models run at compute_effort max only.
  - GPT-5.6 Luna runs at max only.
  - Kimi K3.1 Pro has no Code Migration v1.1 row; only Kimi K3 does.
  - MiniMax-M3.1-Flash has no Code Migration v1.1 row.
- **tbench.ai.** None of the ten has a row at its effort. GPT-5.6 Luna is listed at max only.

## Owner questions

1. **LiveBench in-place edit (O139).**
   - Release 20261025 changed after the 10-30 read: DeepSeek V4.1 Flash 1017 Long Agentic went from 40.9 to 35.7, and
     Overall from 74.02 to 72.87.
   - This build uses today's file. The owner should confirm that the pinned release means its current content, not the
     10-30 bytes.
   - The edit affects only the retained DeepSeek row.
2. **MiniMax-M3.1-Flash effort (O135).** MiniMax documents low to max with **max the default** (`minimax-effort.md`). The
   rows labelled max are taken as exact. The owner should confirm this, as O140 did for MiMo-V2.6-Flash.
3. **MiMo-V2.6-Flash on Vals (O140).**
   - Vals' MiMo-V2.6-Pro model page, in its 2026-09-22 update covering both models, says "We evaluated them with reasoning
     enabled" through the official Xiaomi API.
   - O140 kept Flash's Vals rows unmatched because Vals stated no reasoning setting. This sentence may change that.
   - The quoted figures are Vibe Code 85.22 and the older Code Migration v1, 43.01. It is not certain that the sentence also
     covers the later Code Migration v1.1 runs. The status is unchanged (plausible) pending the owner.
4. **DeepSeek Bug Hunt selection.** The editor's DeepSeek Harness choice (2026-10-23) still stands. Its recorded reason
   said both n=7 rows were featured; the owner has since un-featured the Claude Code row.
