# Third-party board re-read for the 45-configuration cohort (2026-11-26)

Every third-party board a ValueRank ranking uses was re-read for the new cohort in `../cohort.json`, against the chart
capture of **2026-11-26T02:18:20Z** (`../chart-capture.json`, AA Intelligence Index v5.0.2). The cohort has 45
configurations: 20 frontier, 11 near and 14 retained. Its families are GPT-6.2 Sol and GPT-6.2 Astra (new), Claude Fable
5.2 (new), Gemini 4 Neon (new), Muse Ember (new), GPT-6.1 Sol and Terra, GPT-6 Luna and Astra, Claude Haiku 5.5, Opus 5.5
and Sonnet 5.5, Gemini 4 Carbon, and MiMo-V2.6-Flash (retained).

The methods are those of `../../2026-11-01-recapture/third-party/` (and, before it, `2026-10-30-v5-recapture` and
`2026-10-25-board-reread`):

- public pages only: no sign-in, paid export, private API or bot-check solving;
- all web content treated as data, never as instructions; scripts were read as text and never executed;
- exact-configuration matching (O36): the source row must name the same model version **and** the same reasoning effort as
  the AA configuration. No value moves across efforts or versions. Where a board labels a row without an effort, the
  cell is `plausible`, not `exact`, and says why.

To rebuild (from the repository root):

```
python3 -I research/2026-11-26-recapture/third-party/build_coverage.py
```

It writes `coverage-2026-11-26.json` (Bug Hunt, LiveBench 2.0 Overall, AI Coding Daily, tbench.ai),
`vals-catalogue-2026-11-26.json` (Vibe Code v1.1, Code Migration v1.1) and `cognition/frontiercode-2.0-2026-11-26.json`
(Cognition FrontierCode 2.0, the E234 cross-check source), prints exact / plausible / absent counts per board, and exits 0.
The schema is that of 2026-11-01. `absent` is that schema's word for "no exact match, reason recorded in `note`"; no cell
uses the word `none`. Each board also carries `valueChangesSince20261101` (cohort ids that existed on 2026-11-01, matched
through the id change `gpt-6.1-*` to `gpt-6-1-*` and `claude-haiku-5-5` to `claude-haiku-5-5-xhigh`) and
`configurationsNotInThe20261101Cohort`.

`cohort.json` is not tracked in git at the commit this folder was built on. `cohort-snapshot.json` is a byte copy of the
file as read (sha256 `c2606b26575c3d788369cc78256340314ad99d0b79f4e5224cf35cda6e7ccc27`). The build uses `../cohort.json`
when it exists and stops if its ids differ from the script's; otherwise it uses the snapshot.

The capture helpers are in `tools/`:

- `capture_aicd.py` (new): the AI Coding Daily page plus the Livewire all-rows read, with no cookie written to disk.
- `parse_aicd.py`: now also parses the 13-cell row layout (adds `python` and `penalty`). It still reproduces the
  2026-11-01 `leaderboard-allrows-parsed.json` byte for byte from the 2026-11-01 HTML.
- `capture_tbench.js`: the board URL is an optional third argument, and playwright resolves from `PLAYWRIGHT_DIR` too.
- `parse_tbench.py`: unchanged.

## Sources, methods and capture instants (UTC)

| Board | Read at | Method / evidence | Changed since 2026-11-01? |
|---|---|---|---|
| Bug Hunt Bench | `bughunt/benchmark.json` 03:03:40Z; repo `git ls-remote` 03:03:19Z; results clone 03:03:32Z | `benchmark.json` from the site (byte-identical to the repo file at HEAD). `main` is `3be9acdb221b8127e181fa20f0c5a87647d7550e` (2026-11-25T10:42:17Z, "Gemini 4 Neon (xhigh effort, Antigravity CLI 1.5.16) - mean of 3 (61/105)"); meta.updated 2026-11-25, 226 rows. The four results files at that commit and `git-log-since-2026-10-23.txt` (51 commits) are saved as before. | **Yes**: 19 more rows. 14 DeepSeek V4.1 Flash 1017 rows moved out of `runs` into a new top-level `harness_comparison_runs`. No existing row's value was edited. 11 rows changed `featured`. |
| Vals Vibe Code Bench v1.1 | page 03:04:22Z; JSON 03:04:33Z | The page's hashed `/_astro/benchmark_view_vibe_code_bench.DVjiQ-hd.json` (was `.J70PGD0L.json`): updated 2026-11-19, 134 models. Model pages for Gemini 4 Neon, Claude Fable 5.2, Muse Ember (03:05:37Z) and MiMo-V2.6-Pro (03:14:51Z) are in `vals/_models/`. | **Yes**: 11 model keys added, none of the existing cohort rows changed. **The page now says v1.1 is archived and superseded by v1.1.1** (below). |
| Vals Code Migration v1.1 | page 03:04:22Z; JSON 03:04:33Z | `/_astro/benchmark_view_code_migration_v1_1.B5SvaXI-.json` (was `.BRBJcaE4.json`): updated 2026-11-19, 31 models. | **Yes**: Claude Fable 5.2 and Inkling Mini added; no value changed. The page carries no "superseded" banner. |
| LiveBench 2.0 | release files 03:06:24Z; bundle 03:06:12Z; probe 03:07:22Z | Site bundle `main.099aad9b.js` (was `main.1e1ce12d.js`) lists releases `["20261014","20261025","20261106"]`. **20261106 is pinned (O211).** Saved: breakdown, categories, cost, notes, table for 20261106, 20261025 and 20261014; `llm_time-20261106.csv` (a new file); `weights-*.json` (derived from `categories.json`'s `_overall_weights`, as before). `data/20261107` to `data/20261126` return 404. | **Yes**: a new release, with many category scores re-scored (below). Release 20261025's `breakdown.json` was also edited in place (one sub-score). |
| AI Coding Daily | page and Livewire all-rows 03:08:19Z | `tools/capture_aicd.py`: the page (67 rows) and the Livewire update with `hiddenOlderModelIds=[]` (87 rows, `bestHarnessOnly` false), parsed into `aicd/*-parsed.json`. The methodology and effort-levels articles (03:08:58Z) and the Muse Ember, MiMo-V2.6 Flash, Gemini 4 Neon and Fable 5.2 model pages (03:09:53Z) are saved. | **Yes, the board changed method** (below). |
| tbench.ai Terminal-Bench | 4.1: 03:11:03.572Z; 4.0 view: 03:11:45.848Z | `tools/capture_tbench.js` (headless Chromium 1600x1200, no interaction). `/leaderboard/terminal-bench/4.1` redirects to the home page, which is now **Terminal-Bench 4.1**. Files: `tbench/tbench-scrape-2026-11-26.{json,png}` and `tbench-rows-parsed-2026-11-26.json` (67 payload rows; 54 in the rendered table). A reference capture of `/?version=4.0` is `tbench/tbench-v40-scrape-2026-11-26.{json,png}`. | **Yes**: the board is now 4.1, a new leaderboard object (below). |
| Cognition FrontierCode 2.0 | 03:12:28Z | `cognition/`: the page, `data.json` (`/data/frontier-code-2.0/data.json`), the old `frontiercode-leaderboard` data, the blog and the 20 page chunks, with HTTP headers. `frontiercode-2.0-2026-11-26.json` is the compiled capture (rows, exact cohort mapping, artifact sha256). | **Yes**: 36 models (was 26), and every score was rescored on 2026-11-11 (below). |
| Xiaomi MiMo docs, MiniMax docs, Anthropic pricing | not re-read | Out of scope for this read (those families left the cohort) except that **MiMo-V2.6-Flash is still in `cohort.json` as retained**, so it is covered on every board. Its effort mapping (O135/O140/O149) relies on the 2026-11-01 read of Xiaomi's docs, which was not repeated. Vals' MiMo-V2.6-Pro page was re-read, and still says "We evaluated them with reasoning enabled". | n/a |

### Rows dated after the cutoff

**No row on any board is dated after 2026-11-26T02:18:20Z.** The newest are the Bug Hunt Gemini 4 Neon 1.5.16 reruns
(2026-11-25, commit 10:42Z), the AI Coding Daily Gemini 4 Carbon row (2026-11-25), Cognition's `data.json` (HTTP
Last-Modified 2026-11-25T23:58:54Z, board changelog 2026-11-24), the LiveBench release files (Last-Modified
2026-11-24T00:11:21Z) and the Vals boards (2026-11-19, and 2026-11-21 for v1.1.1). The build stops on a Bug Hunt or AI
Coding Daily row dated after the capture day.

## What changed since 2026-11-01

- **Bug Hunt.**
  - All exact cells of configurations that were already in the 2026-11-01 cohort are unchanged.
  - 33 rows were added: GPT-6.2 Sol (5), GPT-6.2 Astra (6), Fable 5.2 (5), Gemini 4 Neon (8, including the superseded 1.5.11 rows), Gemini 4 Carbon (3), Gemini 4 Hydrogen (5) and GLM-5.4 (1). The 14 removed rows are exactly the 14 now in `harness_comparison_runs`.
  - **Gemini 4 Neon was re-run on 2026-11-25** on Antigravity CLI 1.5.16. The board marks the 2026-11-19 rows (1.5.11, xhigh 63, high 57, medium 47.7) `superseded`; the current rows are xhigh 61, high 56, medium 48.3. The leaf is the current row. `combined-scoreboard.csv` still lists both.
  - Fable 5.2 high, medium and low are means of 2; GPT-6.2 Astra xhigh and high are means of 5 (the xhigh mean of 3 is superseded).
  - **No Muse Ember row exists**, and the name appears nowhere in the board, scoreboard, runs or run notes.
  - The build cross-checks every exact cell against `combined-scoreboard.csv` (42 of 42 agree).
- **Vals.**
  - Vibe Code Bench v1.1 is **archived**. Its page now carries the banner "Archived Benchmark: Vibe Code Bench v1.1 has been superseded by v1.1.1, which upgrades the grader, requires every substep to pass, and fixes ambiguous tests. Previous results are preserved here."
  - v1.1 values stay the leaf (owner instruction); v1.1.1 facts are below.
  - Code Migration v1.1 is not marked superseded.
  - **Vals' JSON names Gemini 4 Neon `google/cobalt-c-high-1p00`**, a pre-release codename (reasoning_effort xhigh). Its pages label the same row "Gemini 4 Neon" and link `/models/google_gemini-4-neon`. The build checks that the rendered row's score and cost equal the JSON key's before it matches, and the Neon model page records "Reasoning Effort: xhigh". That row is the Gemini 4 Neon (xhigh) Vibe Code cell.
  - **Claude Fable 5.2 was run at compute effort `high` only** (model page: "Compute Effort: high"), so on Vals it matches Fable 5.2 (high), a near-tier configuration, and not max or xhigh.
  - Claude Haiku 5.5 was run at max only, which the cohort no longer has, so all four Haiku configurations are unmatched on Vals.
- **LiveBench 2.0 (release 20261106, O211).**
  - New models: Claude Fable 5.2, Gemini 4 Carbon, Hydrogen and Neon, GPT-6.2 Astra and Sol, Inkling 2 Mini and Small, Qwen4-Max.
  - **Existing models were re-scored in four suites.** Of the 32 models in both releases, Coding changed for all 32 (fell for 31; range -28.7 to +0.6, median -13.9), Research for all 32 (rose for 28; -6.3 to +19.3, median +3.4), Long Agentic for 29 (-9.3 to +22.4) and Design for 30 (-6.4 to 0). Reasoning, Browser and Data Analysis are identical.
  - Cohort Overalls moved: GPT-6 Luna 64.59 to 60.42, GPT-6.1 Sol 84.07 to 81.17, GPT-6 Astra 85.64 to 84.25, Opus 5.5 85.14 to 83.44, Sonnet 5.5 80.04 to 76.79, GPT-6.1 Terra 77.79 to 78.57. Each cell carries `previousPinOverall` (the 20261025 value).
  - The Overall is still the weighted mean of seven categories (Long Agentic 2.0, Coding 1.5, Design 1.5, the rest 1.0). `notes.json` still says "Every suite counts equally", but the site's own Overall for Claude Fable 5.2, 84.9, equals the weighted mean (84.88), not the unweighted one (85.56), so the weighted method is the board's own.
  - **Claude Fable 5.2 is shown at xhigh only.** The site's metadata says "Shown at xhigh effort: the max-effort run scored lower overall (84.2 against 84.9)". No row or category scores exist for the max run. Fable 5.2 (xhigh) is exact at 84.88. Fable 5.2 (max) is `absent` with the stated 84.2 carried as `siteNoteOverallAtMax` (see Owner questions).
  - Release 20261025: every file is byte-identical to the 2026-11-01 copies except `breakdown-20261025.json`, where the GPT-6 Astra Coding "Product & UX" sub-score went from 94.5 to 94.4. The table is unchanged. `llm_time.csv` exists only for 20261106.
- **AI Coding Daily changed its method** (board text of 2026-11-26 and the methodology article of 2026-11-11).
  - Each model now gets 8 projects and 33 prompts. The **total is out of 90** (was 70): Laravel 20, React-TS 20, Bug Finding 10, **Python Code Quality 20 (new)**, Edge-case Testing 20 (4 projects, as before), less a new per-project **Consistency Penalty** shown in its own column. The check `total = columns + penalty` holds on all 87 rows.
  - Almost every row was **re-dated 2026-11-13/14** (44 of the 62 rows present in both reads moved date; the board gives no reason, but the dates fit the Python project being run then). The leaf columns are mostly unchanged: of the 62, the Bug Finding score changed on most rows and the Laravel, React-TS or Edge-case score on only two. **Claude Haiku 5.5 (High) has React-TS 17 to 18, so its non-bug leaf moved from 51.55 to 52.55.** The other is Beam (not in the cohort).
  - **The ValueRank leaf is unchanged here: `value` = Laravel + React-TS + Edge-case (max 60).** Each cell also carries `python`, `nonBugWithPython` (max 80), `bug`, `penalty` and `total` (max 90). Which of these the owner wants as the leaf is an open question.
  - 25 rows were added (GPT-6.2 Sol/Astra, Fable 5.2 Medium, Gemini 4 Neon/Hydrogen/Carbon, Muse Ember 1.0, MAI Code 2, Inkling 2, Qwen4-Max, Hy4 and others). 6 rows were removed from the all-rows list (all outside the cohort).
  - The cohort's earlier rows were not kept alongside the new ones: for example GPT-6.1 Sol (High) on Codex CLI, which was tested 2026-10-19, now reads 2026-11-13 and total 83.86. The board has no Fable 5.2 high, xhigh or max row (Medium only) and no Gemini 4 Carbon High row (Medium only).
- **tbench.ai** is now **Terminal-Bench 4.1**.
  - The embedded payload holds one leaderboard: id `947c0b13-1d0f-43e0-bd7b-7e5d8c16187a`, name `4-1-0`, title "Terminal-Bench 4.1", created 2026-11-03 and updated 2026-11-20T16:07:10Z, with 67 rows. The payload has no per-row version field, so every row is a 4.1 row and every cell carries `version: "4.1"`.
  - The 4.0 board is still served with `/?version=4.0` (44 rendered rows; 3.0 with `?version=3.0`). Its rows are fetched client-side, so the embedded payload of that capture is still 4.1's. The 4.0 capture is reference only.
  - **4.0 values are never used.** The same model and effort scores differently on the two versions, for example Opus 5.5 (max) 64.85 on 4.0 and 65.76 on 4.1, GPT-6 Astra (max) 58.18 and 60.3, Sonnet 5.5 (max) 61.82 and 63.94, GPT-6 Luna (max) 16.36 and 15.15. Each affected cell's note records the 4.0 figure it does not use.
  - New 4.1 matches: Gemini 4 Carbon (high), GPT-6.1 Terra (max), GPT-6.2 Sol and Astra (max), Fable 5.2 (max), Gemini 4 Neon (xhigh), Muse Ember (xhigh).
- **Cognition FrontierCode 2.0.**
  - **Every result was rescored on 2026-11-11** (changelog: "Updated the cheating scanner to remove false positives: it now combines rule-based checks with a filtering judge. All results are rescored."). Of the 96 (model, effort) rows in both reads, 85 changed (82 up, 3 down; -0.7 to +5.1), for example GPT-6.1 Sol (max) 39.0 to 39.6, Opus 5.5 (max) 45.5 to 47.3 and Gemini 4 Carbon (high) 37.5 to 42.6. The per-row changes are in `valueChangesSince20261101` of the compiled capture.
  - New models: Fable 5.2, GPT-6.2 Sol and Astra, Gemini 4 Neon and Hydrogen, Kimi K3.1 Pro, Inkling 2 Small, SWE-2 Flash and 2.1, Muse Spark Open; DeepSeek V4.1 Flash is now DeepSeek V4.1 Flash 1017.
  - Gemini 4 Carbon moved to the Antigravity CLI harness (low, medium and high).
  - **GPT-6.1 Sol, GPT-6 Astra and Fable 5.1 are now "lineage" models** in the board's JS (shown in the lineage animation on hover, excluded from the default list). Their rows are in `data.json`; the cohort mapping marks them with a caveat.
  - The harness map now holds display labels ("Codex") where it held raw keys ("codex").
  - The page's ld+json top 10 equals `data.json`'s best-effort scores (checked: 10 of 10).
  - There are no Muse Ember, GPT-6.1 Terra or MiMo rows.

## Coverage: configuration x board (45)

Values by board:

- Bug Hunt: planted bugs fixed of 105, with the sample.
- Vibe Code and Code Migration: % (Vals stderr is in the JSON).
- LiveBench: weighted Overall (release 20261106).
- AI Coding Daily: the non-bug leaf (max 60), then the new total (max 90), harness and test date.
- tbench.ai: resolution % on Terminal-Bench 4.1.
- Cognition: FrontierCode 2.0 score %. "(lineage)" means the board shows that model only in its lineage animation.

"—" means no exact match; each cell's note in the JSON lists the rows at other efforts. "P" means plausible: MiMo-V2.6-Flash's
Bug Hunt run is the provider default through OpenRouter, and tbench.ai labels its row effort `none` (O140 keeps these
unmatched).

| Configuration | Bug Hunt | Vibe Code v1.1 | Code Migration v1.1 | LiveBench 2.0 Overall | AI Coding Daily | tbench.ai TB 4.1 | Cognition FC 2.0 |
|---|---|---|---|---|---|---|---|
| *Frontier (20)* | | | | | | | |
| GPT-6 Luna (low) | 4 (single) | — | — | — | — | — | 4.0 |
| GPT-6 Luna (medium) | 4 (single) | — | — | — | 40.2 (56.7/90; Codex CLI, 2026-11-14) | — | 16.1 |
| Claude Haiku 5.5 (low) | 11 (single) | — | — | — | — | — | 10.6 |
| GPT-6 Luna (high) | 9 (single) | — | — | — | 47.73 (67.33/90; Codex CLI, 2026-11-14) | — | 16.5 |
| Claude Haiku 5.5 (medium) | 12 (single) | — | — | — | 51.32 (75.84/90; Claude Code, 2026-11-14) | — | 14.1 |
| Muse Ember (xhigh) | — | — | — | — | — | 30.61 | — |
| Muse Ember (max) | — | 83.703 | — | — | 47.32 (64.52/90; OpenCode, 2026-11-14) | — | — |
| GPT-6.1 Terra (medium) | 7.3 (mean 3) | — | — | — | 46.9 (68.22/90; Codex CLI, 2026-11-14) | — | — |
| GPT-6.2 Sol (low) | 36 (mean 3) | — | — | — | 56.76 (83.08/90; Codex CLI, 2026-11-18) | — | 33.1 |
| GPT-6.1 Terra (high) | 9.7 (mean 3) | — | — | — | 46.69 (69.31/90; Codex CLI, 2026-11-13) | — | — |
| GPT-6.1 Sol (medium) | 29 (mean 2) | — | — | — | 55.67 (83.04/90; Codex CLI, 2026-11-13) | — | 30.3 (lineage) |
| GPT-6.2 Sol (medium) | 45.7 (mean 3) | — | — | — | 57.49 (83.1/90; Codex CLI, 2026-11-18) | — | 38.3 |
| GPT-6.2 Sol (high) | 49.7 (mean 3) | — | — | — | 57.34 (83.53/90; Codex CLI, 2026-11-20) | — | 39.7 |
| GPT-6.2 Sol (xhigh) | 49 (mean 3) | — | — | — | — | — | 39.8 |
| GPT-6.2 Sol (max) | 54.7 (mean 3) | 87.616 | — | 80.31 | — | 61.52 | 43.8 |
| GPT-6.2 Astra (high) | 59.6 (mean 5) | — | — | — | 58.56 (84.48/90; Codex CLI, 2026-11-18) | — | 43.6 |
| GPT-6.2 Astra (xhigh) | 60.2 (mean 5) | — | — | — | — | — | 44.1 |
| GPT-6.2 Astra (max) | 62.7 (mean 3) | 89.898 | — | 84.87 | — | 62.12 | 44.2 |
| Claude Fable 5.2 (xhigh) | 49 (mean 3) | — | — | 84.88 | — | — | 50.2 |
| Claude Fable 5.2 (max) | 58 (mean 3) | — | — | — | — | 65.76 | 48.2 |
| *Near (11)* | | | | | | | |
| Claude Fable 5.2 (high) | 43 (mean 2) | 93.771 | 83.265 | — | — | — | 46.2 |
| Gemini 4 Neon (xhigh) | 61 (mean 3) | 93.698 | — | 87.44 | 54.33 (80.05/90; Antigravity, 2026-11-20) | 61.21 | 44.8 |
| Gemini 4 Carbon (high) | 57.3 (mean 3) | 89.06 | — | 83.33 | — | 64.55 | 42.6 |
| Gemini 4 Neon (high) | 56 (mean 3) | — | — | — | 54.05 (78.87/90; Antigravity, 2026-11-22) | — | 46.2 |
| Claude Opus 5.5 (max) | 41.7 (mean 3) | 90.294 | 81.012 | 83.44 | — | 65.76 | 47.3 |
| GPT-6.2 Astra (medium) | 50.3 (mean 3) | — | — | — | 57.59 (84.06/90; Codex CLI, 2026-11-18) | — | 42.2 |
| Gemini 4 Neon (medium) | 48.3 (mean 3) | — | — | — | 52.45 (77.34/90; Antigravity, 2026-11-19) | — | 38.2 |
| GPT-6.1 Sol (max) | 44.3 (mean 3) | 88.931 | 77.324 | 81.17 | — | 60.91 | 39.6 (lineage) |
| GPT-6.1 Terra (xhigh) | 11.3 (mean 3) | — | — | — | 48.13 (71.99/90; Codex CLI, 2026-11-13) | — | — |
| Claude Haiku 5.5 (xhigh) | 18.3 (mean 3) | — | — | — | — | — | 22.9 |
| GPT-6 Luna (xhigh) | 14 (single) | — | — | — | 49.94 (70.75/90; Codex CLI, 2026-11-14) | — | 18.4 |
| *Retained (14)* | | | | | | | |
| MiMo-V2.6-Flash | P 23.3 (mean 3) | 78.96 | 39.552 | — | 45.48 (64.39/90; OpenCode, 2026-11-14) | P 16.06 | — |
| GPT-6.1 Terra (low) | 6 (mean 3) | — | — | — | — | — | — |
| Claude Haiku 5.5 (high) | 16 (mean 2) | — | — | — | 52.55 (76.3/90; Claude Code, 2026-11-13) | — | 19.3 |
| GPT-6.1 Sol (high) | 36.5 (mean 2) | — | — | — | 56.83 (83.86/90; Codex CLI, 2026-11-13) | — | 35.1 (lineage) |
| GPT-6.1 Sol (xhigh) | 42.7 (mean 3) | — | — | — | — | — | 33.0 (lineage) |
| GPT-6 Astra (high) | 35 (single) | — | — | — | 56.77 (84.25/90; Codex CLI, 2026-11-13) | 60 | 38.8 (lineage) |
| GPT-6 Astra (xhigh) | 43 (single) | — | — | — | — | 59.7 | 41.7 (lineage) |
| Claude Opus 5.5 (xhigh) | 36 (mean 3) | — | — | — | — | — | 44.7 |
| GPT-6 Luna (max) | 18.3 (mean 3) | 81.649 | 46.669 | 60.42 | 51.99 (73.06/90; Codex CLI, 2026-11-14) | 15.15 | 22.7 |
| GPT-6.1 Sol (low) | 22.5 (mean 2) | — | — | — | 52.7 (78.8/90; Codex CLI, 2026-11-13) | — | 25.7 (lineage) |
| GPT-6.1 Terra (max) | 40.7 (mean 3) | 83.997 | — | 78.57 | 52.49 (77.67/90; Codex CLI, 2026-11-13) | 53.33 | — |
| Claude Opus 5.5 (high) | 31.7 (mean 3) | — | — | — | 57.68 (84.95/90; Claude Code, 2026-11-13) | — | 36.3 |
| GPT-6 Astra (max) | 45 (mean 3) | 89.594 | 80.579 | 84.25 | — | 60.3 | 44.0 (lineage) |
| Claude Sonnet 5.5 (max) | 51.3 (mean 3) | 92.392 | 86.875 | 76.79 | — | 63.94 | 42.2 |

### Counts per board

| Board | exact | plausible | absent |
|---|---|---|---|
| Bug Hunt | 42 | 1 | 2 |
| Vals Vibe Code v1.1 | 13 | 0 | 32 |
| Vals Code Migration v1.1 | 7 | 0 | 38 |
| LiveBench 2.0 Overall (20261106) | 11 | 0 | 34 |
| AI Coding Daily | 25 | 0 | 20 |
| tbench.ai Terminal-Bench 4.1 | 14 | 1 | 30 |
| Cognition FrontierCode 2.0 (cross-check) | 37 | 0 | 8 |

### New-model matches

| Family | Bug Hunt | Vibe Code | Code Migration | LiveBench | AI Coding Daily | tbench.ai 4.1 | Cognition |
|---|---|---|---|---|---|---|---|
| GPT-6.2 Sol | low to max (5) | max | none | max | low, medium, high | max | low to max (5) |
| GPT-6.2 Astra | medium to max (4) | max | none | max | medium, high | max | medium to max (4) |
| Claude Fable 5.2 | high, xhigh, max | **high** | **high** | **xhigh** | none (Medium only) | max | high, xhigh, max |
| Gemini 4 Neon | medium, high, xhigh | xhigh (codename key) | none | xhigh | medium, high, xhigh | xhigh | medium, high, xhigh |
| Muse Ember | none | max | none | none | max ("Muse Ember 1.0") | **xhigh** | none |

## Non-matches, with the reasons

Each non-match is recorded in the JSON cell's `note`. Nothing is filled across efforts or versions.

- **Bug Hunt.**
  - Muse Ember (xhigh and max): no row for the model anywhere in the board's files. The board's Meta rows are Muse Spark 1.2 and 1.3 and Muse Wonder (Full) 1.0, which are other models.
  - MiMo-V2.6-Flash is `plausible` (23.3, mean of 3): the board ran the provider default through OpenRouter and does not assert a reasoning state (O140 keeps it unmatched).
  - The retained GPT-6.1 Terra, Sol, GPT-6 Astra and Luna rows are exact at their own efforts and unchanged.
- **Vals Vibe Code and Code Migration.** Vals ran each model at one effort.
  - At max: GPT-6 Luna, GPT-6.1 Sol and Terra, GPT-6.2 Sol and Astra, GPT-6 Astra, Muse Ember, Opus 5.5, Sonnet 5.5 and Haiku 5.5.
  - Fable 5.2 at high, Gemini 4 Carbon at high, Gemini 4 Neon at xhigh.
  - Every other effort of those models is `absent`, and so are all four Haiku 5.5 configurations (the cohort has no Haiku max).
  - Code Migration v1.1 has no row at all for GPT-6.1 Terra, GPT-6.2 Sol or Astra, Gemini 4 Neon or Carbon, or Muse Ember.
  - MiMo-V2.6-Flash is `exact` on both under O149 (Vals: "evaluated with reasoning enabled").
- **LiveBench 2.0.** One run per model at its top effort.
  - Max for the GPT-6 family, Opus 5.5 and Sonnet 5.5; **xhigh for Fable 5.2 and Gemini 4 Neon**; high for Gemini 4 Carbon.
  - Haiku 5.5 is at max only, which the cohort lacks. There is no Muse Ember or MiMo-V2.6-Flash row, nor any MiMo-V2.6-Flash model metadata.
  - Fable 5.2 (max) has no row (see the Fable note above).
- **AI Coding Daily.** One row per model and effort; the board did not test every effort. Efforts on the board:
  - GPT-6 Luna: Medium, High, Xhigh, Max. GPT-6.1 Terra: Medium, High, Xhigh, Max.
  - GPT-6.1 Sol and GPT-6.2 Sol: Low, Medium, High. GPT-6.2 Astra and GPT-6 Astra: Medium, High.
  - Claude Haiku 5.5 and Sonnet 5.5: Medium, High. Opus 5.5: Low, Medium, High.
  - Gemini 4 Neon: Medium, High, Xhigh. Fable 5.2 and Gemini 4 Carbon: **Medium only** (the cohort has Fable high, xhigh and max, and Carbon high).
  - Muse Ember: Max only, labelled "Muse Ember 1.0" while the other boards say "Muse Ember"; read as the same model and flagged. MiMo-V2.6 Flash: High.
  - Every cohort effort outside these lists is `absent`.
- **tbench.ai 4.1.**
  - Only the efforts the board shows: GPT-6 Astra has high, xhigh and max in the payload (high and xhigh are not in the default rendered table). GPT-6 Luna, GPT-6.1 Sol and Terra, GPT-6.2 Sol and Astra, Opus 5.5, Sonnet 5.5 and Fable 5.2 are max only. Haiku 5.5 is max only, which the cohort lacks. Gemini 4 Neon is xhigh only, Muse Ember xhigh only, and Gemini 4 Carbon high only.
  - MiMo V2.6 Flash's one row is labelled effort `none` on mini-swe-agent, so it is `plausible` and unmatched.
- **Cognition.** No row for GPT-6.1 Terra (five configurations), Muse Ember (two) or MiMo-V2.6-Flash.

## Vals Vibe Code Bench v1.1.1 (reference note)

Vals' Vibe Code Bench page for v1.1 is now labelled an archived benchmark and points to **v1.1.1** (slug
`vibe-code-v1-1-1`, updated 2026-11-21, 51 models, harness OpenHands, JSON
`benchmark_view_vibe_code_bench_v1_1_1.CpJZFzHs.json`). Per the banner, v1.1.1 "upgrades the grader, requires every substep
to pass, and fixes ambiguous tests". Facts from the capture (`vals/vibe-code-v1-1-1.*`):

- All 51 v1.1.1 model keys also exist on v1.1 and have an identical cost per test, so the runs look reused and re-graded. Accuracy falls by 0.7 to 25.7 points (mean 14.7).
- Its top rows are Claude Fable 5.2 83.52, Claude Sonnet 5.5 80.88 and Gemini 4 Neon 80.23. On v1.1 they were 93.77, 92.39 and 93.70, and Neon was second.
- v1.1.1 uses the same Vals keys, so the effort matches are the same set as on v1.1 (the same Neon codename key, `google/cobalt-c-high-1p00`).
- The cohort configurations whose Vals effort equals AA's, with both values:

| Configuration | v1.1 (leaf) | v1.1.1 (reference only) |
|---|---|---|
| Muse Ember (max) | 83.703 | 63.962 ± 4.164 |
| GPT-6.2 Sol (max) | 87.616 | 79.483 ± 3.658 |
| GPT-6.2 Astra (max) | 89.898 | 78.567 ± 3.47 |
| Claude Fable 5.2 (high) | 93.771 | 83.519 ± 3.25 |
| Gemini 4 Neon (xhigh) | 93.698 | 80.228 ± 3.248 |
| Gemini 4 Carbon (high) | 89.06 | 75.772 ± 3.601 |
| Claude Opus 5.5 (max) | 90.294 | 78.49 ± 3.328 |
| GPT-6.1 Sol (max) | 88.931 | 75.101 ± 3.466 |
| GPT-6 Luna (max) | 81.649 | 65.315 ± 4.632 |
| GPT-6.1 Terra (max) | 83.997 | 75.52 ± 4.113 |
| GPT-6 Astra (max) | 89.594 | 77.535 ± 3.808 |
| Claude Sonnet 5.5 (max) | 92.392 | 80.88 ± 3.27 |

These v1.1.1 values are stored once, in the vals catalogue's `successorReference` of the Vibe Code board, and never under
`coverage`. Code Migration v1.1 has no successor banner on 2026-11-26.

## Owner questions and flags

1. **MiMo-V2.6-Flash is still in `cohort.json`** (retained, id `mimo-v2-6-flash`), although the brief said the MiMo family
   left the cohort. It is covered on every board with the 2026-11-01 mapping (O135/O140/O149): Vals `exact` (both boards),
   AI Coding Daily `exact` at the High row, Bug Hunt and tbench.ai `plausible`, LiveBench and Cognition `absent`. Xiaomi's
   docs were not re-read. If the cohort drops it, those cells are unused.
2. **Vibe Code v1.1 is archived by Vals.** v1.1 stays the leaf as instructed; the owner may want to move to v1.1.1. For
   the 12 matching configurations its values are 8 to 20 points lower, and the order changes in places: Gemini 4 Neon is
   above Claude Sonnet 5.5 on v1.1 (93.70 against 92.39) and below it on v1.1.1 (80.23 against 80.88).
3. **Gemini 4 Neon on Vals sits under a codename key** (`google/cobalt-c-high-1p00`). The match rests on the page label,
   an identical rendered score and cost, and the model page's xhigh. Vals lists no `google/gemini-4-neon` key.
4. **LiveBench Fable 5.2 (max).** The only figure is 84.2 in `notes.json` and the site metadata (the xhigh run is 84.9).
   It is stored as `siteNoteOverallAtMax` on an `absent` cell. Accepting it is an owner decision (same metric and effort,
   but a note, not a row, with one decimal).
5. **AI Coding Daily's leaf.** The total is now out of 90 and includes Python and a penalty. The cell value is still
   Laravel + React-TS + Edge-case (max 60). The Python-inclusive alternative (max 80) and the totals are in each row.
   Haiku 5.5 (High)'s leaf moved from 51.55 to 52.55 (its React-TS score is 18 now, 17 on 2026-11-01, and the row is
   re-dated 2026-11-13); the board does not say why.
6. **Muse Ember 1.0 on AI Coding Daily** is matched to AA's "Muse Ember" (no version): no second Muse Ember version
   appears on any board, but O36 asks for the same version.
7. **tbench.ai values are 4.1.** Seven cohort configurations that had 4.0 values on 2026-11-01 now carry different 4.1
   values (cell notes quote the 4.0 figures as not used). AA's Index runs 4.1. The board no longer shows 4.0 by default.
8. **Cognition (cross-check) rescoring.** Every FrontierCode 2.0 score moved on 2026-11-11, so any AA-Cognition
   agreement statistic from the 2026-11-01 read is stale. The compiled capture leaves the AA side empty (`aaFrontierCode20`)
   for the release build to fill. GPT-6.1 Sol and GPT-6 Astra rows are lineage-only on the board and carry a caveat.
9. **Bug Hunt Gemini 4 Neon.** The 1.5.16 rerun supersedes the 1.5.11 rows on the board (xhigh 63 to 61, high 57 to 56,
   medium 47.7 to 48.3); the leaf follows the board's current row. The superseded rows are listed in
   `supersededRowsOnBoard`.
