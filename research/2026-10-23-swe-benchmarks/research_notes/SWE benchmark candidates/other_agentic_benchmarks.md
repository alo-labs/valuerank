# Other agentic-coding and software-engineering benchmarks (excluding Vals AI, AI Coding Daily, LiveBench, Surge AI, FrontierCode, Terminal-Bench, Bug Hunt Bench, DeepSWE)

Research date: 2026-10-23. Researcher: Claude Opus 5.5 subagent. Scope: candidates named in the brief plus others found in passing. Web content was treated as data. Two primary data files were downloaded and parsed locally:
- Epoch AI Benchmarking Hub bulk data, `https://epoch.ai/data/benchmark_data.zip` (CC-BY; CSVs time-stamped 2026-10-23 05:16), referred to below as **[Epoch zip]**. Its files include Epoch's own runs (`swe_bench_verified.csv`, `mirrorcode.csv`) and mirrors of external leaderboards (`cursorbench_external.csv`, `webdev_arena_external.csv`, `frontierswe_external.csv`, `gso_external.csv`, `weirdml_v3_external.csv`, `metr_time_horizons_external.csv`, `aider_polyglot_external.csv`, `posttrainbench_external.csv`). Effort suffixes such as `_max` or `_unknown` are Epoch's labels.
- SWE-bench's own leaderboard file, `https://raw.githubusercontent.com/SWE-bench/swe-bench.github.io/master/data/leaderboards.json`, referred to as **[SWE-bench JSON]**.

Two AA captures already in the repository were also read (not edited): `data/aa/aa_v432_snapshot.json` (AA model pages, capturedAt 2026-10-23T06:26:23Z), referred to as **[AA snapshot]**, and `research/2026-10-23-refresh/coding-agents-v2.0-capture-2026-10-23.json` (AA Coding Agents page, capturedAt 2026-10-23T05:31:41Z), referred to as **[AA CAI v2.0 capture]**.

"Exact match" means the benchmark row names the same model version and the same reasoning effort as the ValueRank/AA roster identity (for example "Claude Haiku 5.5 (xhigh)" or "GPT-6.1 Sol (max)"). "Frontier set" means the brief's 19 frontier and near-frontier configurations: GPT-6 Luna; Claude Haiku 5.5 low/medium/high/xhigh/max; MiMo-V2.6-Flash; MiMo-V2.6-Pro; GPT-6.1 Sol medium/high/xhigh/max; Claude Opus 5.5; Claude Sonnet 5.5; GPT-5.6 Luna; Gemini 4 Argon (high); GPT-6 Astra; DeepSeek V4.1 Flash 1017; MiniMax-M3.1-Flash.

## Q1. Which candidate benchmarks are live in late 2026, and which are stale or saturated?

### Takeaway
Most of the classic SWE leaderboards are **stale for the 2026 roster**. Official SWE-bench (all tracks, including bash-only/mini-SWE-agent and Multilingual), Aider Polyglot, LiveCodeBench, METR time-horizon, Scale's standardized SWE-bench Pro board, SWE-rebench, CodeClash, SWE-Lancer and Multi-SWE-bench have **no results, or no exact-effort results, for the H2-2026 roster models**. The benchmarks with current (Sept–Oct 2026) roster results are **CursorBench 4.0** (Cursor), **Arena Code Arena WebDev and Agent Arena**, **FrontierSWE V2** (Proximal), AA's **SWE-Atlas-QnA-AA** and **ITBench-AA**, Epoch's **MirrorCode**, and (ML-coding, not SWE) **WeirdML v3**. Scale's own **SWE Atlas** boards were last updated 2026-07-28 and cover only a few roster models.

### Cited Findings
**Stale or retired**
- SWE-bench official leaderboards (Verified 180 entries, latest 2026-02-26; Multilingual 13 entries, latest 2026-02-20; Lite latest 2025-09-11; Multimodal latest 2025-11-17). The newest bash-only (mini-SWE-agent v2.0.0) Verified entries are Gemini 3 Pro 69.6% (2026-02-26), GPT 5.2 Codex 72.8%, Claude 4.5 Opus (high) 76.8%, Claude 4.6 Opus 75.6%, GLM 5 (high) 72.8% and MiniMax M2.5 (high) 75.8%. **No roster model appears** in any track. — [SWE-bench JSON](https://raw.githubusercontent.com/SWE-bench/swe-bench.github.io/master/data/leaderboards.json); [swebench.com](https://www.swebench.com/)
- OpenAI stopped evaluating SWE-bench Verified. Its audit found 59.4% of 138 hard tasks it reviewed were flawed, and frontier models could reproduce some original fixes from memory (contamination). OpenAI recommended SWE-bench Pro instead. — [OpenAI, "Why we no longer evaluate SWE-bench Verified"](https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/) (title from search; page text seen only via [the-decoder](https://the-decoder.com/openai-wants-to-retire-the-ai-coding-benchmark-that-everyone-has-been-competing-on/) and [Decrypt](https://decrypt.co/359012/openai-benchmark-measure-ai-coding-supremacy-contaminated))
- Epoch's own SWE-bench Verified runs (Inspect) stop at a run started 2026-06-25 (glm-5.2_max 0.787). The last three: gemini-3.5-flash_high 0.793 (run 2026-06-01), deepseek-v4-pro_max 0.776 (2026-06-18; this is pre-0813, so not the roster's DeepSeek V4 Pro 0813) and qwen3.7-max 0.773. — [Epoch zip](https://epoch.ai/data/benchmark_data.zip) `swe_bench_verified.csv`
- Aider Polyglot: 225 Exercism exercises. Latest entry is DeepSeek-V3.2-Exp on 2025-10-03, the page was last updated 2025-11-20, and the top score is gpt-5 (high) 88.0%. **Stale and near-saturated.** — [Aider leaderboard](https://aider.chat/docs/leaderboards/)
- LiveCodeBench (original): its published data file has 28 models, the newest released mid-2024/2025 (e.g. DeepSeek-R1-0528, Qwen3-235B-A22B). The newest problem dates fall in early April 2025. **Stale.** — [LiveCodeBench performances_generation.json](https://livecodebench.github.io/performances_generation.json); the [leaderboard page](https://livecodebench.github.io/leaderboard.html) renders only through JavaScript
- LiveCodeBench Pro: only aggregator snapshots were found (Gemini 3.1 Pro or Sakana Fugu-Ultra leading), with no roster models. — [BenchLM](https://benchlm.ai/benchmarks/livecodebench-pro); [anotherwrapper](https://anotherwrapper.com/tools/llm-pricing/evals/livecodebench-pro)
- METR time horizon: the results YAML (TH1.1) ends at claude_mythos_preview_early (release 2026-04-07, p50 ≈1045 min). The newest other entries are gpt_5_4 (342 min) and gemini_3_1_pro (384 min). The page says it was clarified on 2026-09-08 as **no longer actively updated**. — [METR time horizons](https://metr.org/time-horizons/); [benchmark_results_1_1.yaml](https://metr.org/assets/benchmark_results_1_1.yaml)
- A search summary claimed METR lists "GPT-5.6 (Sol) at 11 h 18 min (June 2026)" via a Wikipedia copy. That entry is **not in METR's YAML**, so it is treated as unverified. A third-party GitHub PR states Opus 5.5 and GPT-6 Astra have **no METR run** and gives only projections. — [joansam/metr-chart PR #3](https://github.com/joansam/metr-chart/pull/3)
- Scale SWE-Bench Pro, standardized public set (731 tasks; private 276; held-out 858): 25 entries, led by Muse Spark 1.1 61.50 ±3.10, then gpt-5.4 (xHigh) 59.10 and Muse Spark 55.00. Starred rows use mini-swe-agent with a 250-turn limit. **No roster model, and no dates.** — [Scale Labs SWE-Bench Pro](https://labs.scale.com/leaderboard/swe_bench_pro)
- "SWE-bench Pro" numbers for roster models on aggregators are vendor-reported and use mixed scaffolds, e.g. Claude Opus 5.5 89.9%, Sonnet 5.5 81.3%, Fable 5.1 81.2%, Qwen3.8 Max 67.7%, GPT-5.6 Sol 64.6%, GPT-5.6 Luna 62.7%. No efforts are stated, and BenchLM does not mark which scores are provider-reported. — [BenchLM SWE-bench Pro (updated 2026-10-20)](https://benchlm.ai/benchmarks/swe-bench-pro); [LLM Learner](https://llmlearner.com/rankings/swe-bench-pro) calls the 89.9% provider-reported
- BenchLM cites an "OpenAI July 2026 audit" estimating about 30% of the 731-task SWE-bench Pro public split is broken, after which OpenAI withdrew its recommendation. The OpenAI page returned HTTP 403, so this is **unverified**. — [BenchLM](https://benchlm.ai/benchmarks/swe-bench-pro) citing [openai.com/index/separating-signal-from-noise-coding-evaluations](https://openai.com/index/separating-signal-from-noise-coding-evaluations/)
- SWE-rebench (Nebius): the current window is 2026-05-15 to 2026-07-01, with 111 problems from 65 repositories. The last update was **2026-07-01**. Its newest rows are Fable 5 (high) 64.5%, Grok 4.5 (high) 63.8%, Opus 5 (high) 63.4%, GLM-5.2 (high) 62.9%, GPT-5.6 Sol (medium) 62.3%, Sonnet 5 (high) 56.8%, MiniMax M3 47.2%, MiMo V2.5 Pro 46.5%, GPT-5.6 Luna (medium) 43.6% and DeepSeek-V4 Pro (high) 40.2%. Agent rows (Junie, Claude Code, Codex, Cursor) are mixed in. **No post-July model** appears. — [swe-rebench.com](https://swe-rebench.com/)
- CodeClash: only 2025 snapshots were found (Claude Sonnet 4.5 Elo 1389 on top). — [DataLearner](https://www.datalearner.com/en/benchmarks/codeclash); [alphaXiv](https://www.alphaxiv.org/benchmarks/stanford-university/codeclash)
- SWE-Lancer: an aggregator lists 4 models with GPT-5.1 Codex on top. Multi-SWE-bench: an aggregator lists 6 models, last updated July 2026. KernelBench: an aggregator lists 5 models as of 2026-10-15, with Claude Fable 5 on top at 23.5%. All three are aggregator-only, not verified at source, and **stale or thin for the roster**. — [LLM Stats SWE-Lancer](https://llm-stats.com/benchmarks/swe-lancer); [LLM Stats Multi-SWE-bench](https://llm-stats.com/benchmarks/multi-swe-bench); [BenchLM KernelBench](https://benchlm.ai/benchmarks/kernelbench)
- SWE-bench-Live (Microsoft) is monthly-refreshed with MultiLang and Windows splits, and the page mentions an August 2026 trajectory-verification update. Its leaderboard failed to load ("Error loading data"), so **coverage is unknown**. — [SWE-bench-Live](https://swe-bench-live.github.io/)

**Live with H2-2026 roster results**
- CursorBench 4.0: 77 rows. The latest changelog entry is 2026-10-07 (Sonnet 5.5 pricing update), and task version 4.0 dates from 2026-09-10. — [cursor.com/cursorbench](https://cursor.com/cursorbench)
- Arena Code Arena (WebDev, Image-to-WebDev, Fullstack) and Agent Arena: models were added continuously through 2026-10-20 (e.g. DeepSeek-V4.1-Flash-20261017 (Max) on 2026-10-18; MiniMax-M3.1-Flash and Muse Wonder Full (Max) on 2026-10-19). — [Arena leaderboard changelog](https://arena.ai/blog/leaderboard-changelog/)
- FrontierSWE V2 (Proximal): roster rows released up to 2026-10-07 (Claude Haiku 5.5). — [frontierswe.com](https://www.frontierswe.com/); [Epoch zip](https://epoch.ai/data/benchmark_data.zip) `frontierswe_external.csv`
- AA SWE-Atlas-QnA-AA (Coding Agent Index v2.0): 24 agent configurations captured 2026-10-23. — [AA coding agents](https://artificialanalysis.ai/agents/coding-agents); [AA CAI v2.0 capture] `research/2026-10-23-refresh/coding-agents-v2.0-capture-2026-10-23.json`
- AA ITBench-AA: launched May 2026, with 45 models charted. — [AA ITBench-AA](https://artificialanalysis.ai/evaluations/itbench-aa); [AA launch article](https://artificialanalysis.ai/articles/itbench-aa-launch)
- Scale SWE Atlas (Codebase QnA 124 tasks; Test Writing 90; Refactoring 70; 284 in all): the QnA board was last updated 2026-07-28. — [Scale Labs SWE Atlas QnA](https://labs.scale.com/leaderboard/sweatlas-qna); [Scale blog "SWE Atlas complete"](https://scale.com/blog/swe-atlas-complete)
- Epoch MirrorCode (Epoch-run; added to the hub 2026-06-26): the latest run started 2026-10-14 (gemini-4-argon_high). — [Epoch zip](https://epoch.ai/data/benchmark_data.zip) `mirrorcode.csv`, `benchmark_metadata.csv`
- Epoch hub last updated 2026-10-23. — [Epoch benchmarks](https://epoch.ai/benchmarks)

### Inferences
- The SWE-bench family (Verified, bash-only, Multilingual, Lite) is no longer a usable source of roster results. Its maintainers stopped adding entries in February 2026, and its main vendor sponsor has retired Verified for contamination. Epoch also stopped running Verified after June 2026, so even the independent run lags the roster by about four months.
- SWE-bench Pro has no independent, uniform-harness result for any roster model. Using it would mean vendor-reported numbers on vendor-chosen scaffolds. That conflicts with the "same benchmark version, exact configuration, primary source" leaf rule and gives no effort labels.

### Gaps
- SWE-PolyBench (Amazon) was not checked; no time was left after higher-priority candidates.
- The SWE-bench-Live, LiveCodeBench Pro official, KernelBench official (kernelbench.com), CodeClash official, Multi-SWE-bench official and SWE-Lancer official boards were not reached directly. Their staleness rests on aggregator pages or failed loads.
- OpenAI's July 2026 SWE-bench Pro audit could not be read (HTTP 403).

## Q2. Roster coverage at exact model version and reasoning effort (the decisive O36 criterion)

### Takeaway
**No benchmark outside AA covers more than about half of the 51 roster configurations at exact effort, and none covers the GPT-6.1 Sol medium/high/xhigh rows.** CursorBench is the best per-effort source (about 25/51 exact, including all five Haiku 5.5 and all five Sonnet 5.5 efforts). However, it has **no GPT-6-family, MiMo, DeepSeek, MiniMax, Kimi or Qwen rows**. Arena Code Arena WebDev covers about 26/51 at one effort per model, including GPT-6 Luna, GPT-6.1 Sol (max), MiMo-V2.6-Pro/Flash, DeepSeek V4.1 Flash 1017 and MiniMax-M3.1-Flash, but no Haiku 5.5. The two are largely complementary. Frontier-set coverage is about 9/19 for CursorBench, about 9/19 for WebDev, 9/19 for SWE-Atlas-QnA-AA, about 5/19 for FrontierSWE and 3/19 for ITBench-AA.

### Cited Findings
**CursorBench 4.0** (score %, average cost per task; effort is shown in the row name). All rows: [cursor.com/cursorbench](https://cursor.com/cursorbench), mirrored in [Epoch zip](https://epoch.ai/data/benchmark_data.zip) `cursorbench_external.csv`.
- Exact roster matches:
  - Opus 5.5 Max 57.8% ($13.43)
  - Sonnet 5.5: Max 55.5%, XHigh 53.1%, High 47.8%, Medium 39.2%, Low 35.8%
  - Haiku 5.5: Max 48.4% ($1.12), XHigh 44.3% ($0.56), High 42.3% ($0.32), Medium 36.9% ($0.17), Low 30.9% ($0.08)
  - Gemini 4 Argon High 52.9% ($4.57)
  - Fable 5.1 Max 51.8%
  - Muse Wonder Max 50.4%
  - Opus 5 Max 46.6%
  - Grok 4.7 XHigh 46.3%
  - GLM 5.3 Max 42.6%
  - GPT-5.6 Sol Max 41.7%
  - Muse Spark 1.3 Max 41.6% and XHigh 37.5%
  - Grok 4.6 XHigh 41.4% and Medium 36.1%
  - Gemini 3.8 Flash High 39.6%
  - GPT-5.6 Luna Max 35.9% ($1.03)
  - Sonnet 5 Max 34.1%
- GLM 5.3 Flash has Max 36.8%, High 31.1% and Low 26.9%. AA's roster identity "GLM-5.3-Flash" names no effort, so the match is uncertain.
- No rows for GPT-6 Astra, GPT-6 Sol, GPT-6.1 Sol (any effort), GPT-6 Luna, GPT-5.5, MiMo-V2.6-Pro/Flash, DeepSeek V4 Pro/V4 Flash/V4.1 Flash 1017, MiniMax-M3.1-Flash, Kimi K3, Qwen3.8 Max, Gemini 3.5/3.6/3.7 Flash, GLM-5.2, Claude Fable 5, Opus 4.8, Muse Spark 1.2 or Muse Wonder Full. — [cursor.com/cursorbench](https://cursor.com/cursorbench)

**Arena Code Arena WebDev** (Arena score / votes, from Epoch's mirror unless noted). All rows: [Epoch zip](https://epoch.ai/data/benchmark_data.zip) `webdev_arena_external.csv`; additions after the mirror from the [Arena changelog](https://arena.ai/blog/leaderboard-changelog/).
- Exact roster matches:
  - claude-opus-5-5_max 1820.3 / 1887
  - gpt-6-astra_max 1800.3 / 2281
  - gpt-6.1-sol_max 1758.7 / 1264
  - claude-fable-5-1_max 1758.1
  - gpt-6-sol_max 1689.3
  - claude-opus-5_max 1687.0
  - gemini-4-argon_high 1679.5 / 2422
  - kimi-k3_max 1674.3
  - muse-spark-1.3_max 1651.9 and _xhigh 1623.1
  - grok-4.7_xhigh 1637.5
  - mimo-v2.6-pro 1618.4 (no effort label)
  - glm-5.3_max 1614.5
  - glm-5.2_max 1593.3
  - gpt-6-luna_max 1582.0 / 5577
  - gemini-3.8-flash_high 1567.9
  - gemini-3.6-flash_high 1537.0
  - muse-spark-1.2_xhigh 1534.4
  - gemini-3.5-flash_high about 1500
- Sonnet 5.5 is present only at xhigh (1786.3) and high (1698.8). Max, medium and low are absent, so the roster's Sonnet 5.5 (max) row has no exact match.
- Added on Arena after Epoch's mirror, effort as labelled by Arena: mimo-v2.6-flash (2026-10-07), qwen3.8-max-0902 (2026-09-01), DeepSeek-V4.1-Flash-20261017 (Max) (2026-10-18), MiniMax-M3.1-Flash (2026-10-19, no effort label) and Muse Wonder Full (Max) (2026-10-19). Scores were not obtainable because arena.ai returned HTTP 403. — [Arena changelog](https://arena.ai/blog/leaderboard-changelog/)
- Effort mismatches with the roster:
  - gpt-5.6-sol_xhigh (roster: max)
  - gpt-5.6-luna_xhigh 1518.9 (roster: max)
  - claude-sonnet-5_high (roster: max)
  - grok-4.6_high (roster: medium and xhigh)
  - gemini-3.7-flash_high (roster: medium)
  - deepseek-v4-pro-0813_high and deepseek-v4-flash-0731_high (roster: max)
  - claude-opus-4-8_high/none (roster: max)
- Absent from WebDev: Claude Haiku 5.5 (Agent Arena only, at High), GPT-6.1 Sol below max, GPT-5.5 and Muse Wonder (Agent Arena only). — [Arena changelog](https://arena.ai/blog/leaderboard-changelog/); [Epoch zip](https://epoch.ai/data/benchmark_data.zip)

**Arena Agent Arena**
- Roster-relevant additions: GPT 6 Luna (Max), GPT 6.1 Sol (Max), Claude Opus 5.5 (High), Claude Sonnet 5.5 (Max), gemini-4-argon-high, GPT 6 Astra (Max), Claude Haiku 5.5 (High), MiMo V2.6 Pro and Flash, DeepSeek-V4.1-Flash-20261017 (Max), Muse Wonder (Max), Muse Wonder Full (Max), Grok 4.7 (xHigh), GLM 5.3 (Max), Qwen3.8 Max and others. Opus 5.5 appears only at High, which does not match roster max. **Values not obtained** (HTTP 403). — [Arena changelog](https://arena.ai/blog/leaderboard-changelog/)

**FrontierSWE V2** (mean@5). All rows: [frontierswe.com](https://www.frontierswe.com/) and [Epoch zip](https://epoch.ai/data/benchmark_data.zip) `frontierswe_external.csv`.
- Rows, with Epoch's effort labels in brackets:
  - GPT-6 Astra [max] 65.5% ($1,029.65 per trial)
  - Claude Opus 5.5 [max] 62.3% ($98.87)
  - Sonnet 5.5 [max] 61.9%
  - Fable 5.1 [max] 56.3%
  - Gemini 4 Argon [high] 55.0%. FrontierSWE flags a non-production setting with a low cache-hit rate.
  - Opus 5 [max] 52.0%
  - Fable 5 [max] 47.0%
  - Haiku 5.5 [max] 43.8% ($20.55)
  - GPT-5.6 Sol [max] 32.2%
  - GLM-5.3 [max] 30.2%
  - Grok 4.7 [xhigh] 29.5%
  - Kimi K3 [max] 25.9%
  - Muse Spark 1.3 [max] 25.8%
  - Grok 4.6 [xhigh] 25.3%
  - Gemini 3.7 Flash [high] 20.3%
  - Gemini 3.8 Flash [high] 19.6%
  - GLM-5.3 Flash [max] 18.1%
  - Qwen3.8-Max-0902 [xhigh] 17.8%
  - Muse Spark 1.2 [xhigh] 12.0%
- **FrontierSWE's own page states no effort for any model.** The effort labels exist only in Epoch's mirror. — [frontierswe.com](https://www.frontierswe.com/)
- No rows for GPT-6.1 Sol, GPT-6 Luna, GPT-6 Sol, MiMo-V2.6, DeepSeek V4.1 Flash, MiniMax-M3.1 or Haiku 5.5 below max. — [frontierswe.com](https://www.frontierswe.com/)

**AA SWE-Atlas-QnA-AA** (reward = mean over 3 attempts × 124 tasks). Source for all rows: [AA CAI v2.0 capture](https://artificialanalysis.ai/agents/coding-agents) (repository file `research/2026-10-23-refresh/coding-agents-v2.0-capture-2026-10-23.json`).
- Rows, with the agent harness:
  - Muse Wonder Full (max), Muse Code: 0.688
  - Fable 5.1 (max), Claude Code: 0.664
  - Opus 5.5 (max), Claude Code: 0.659
  - Sonnet 5.5 (max), Claude Code: 0.642
  - Grok 4.7 (xhigh), Grok Build: 0.629
  - DeepSeek V4.1 Flash 1017 (max): 0.616 on the DeepSeek Harness; 0.610 for DeepSeek V4.1 Flash (max) on Codex
  - Muse Wonder (max): 0.616
  - GPT-6.1 Sol (max), Codex: 0.599
  - Kimi K3, Kimi Code CLI: 0.599 (effort not stated)
  - GPT-6 Astra (max), Codex: 0.591
  - GLM-5.3 (max), Opencode: 0.586
  - Muse Spark 1.3 (max): 0.586
  - Qwen3.8 Max, Claude Code: 0.562 (effort not stated)
  - Gemini 4 Argon (high), Antigravity CLI: 0.551
  - Gemini 3.8 Flash (high), Antigravity SDK: 0.444
  - GPT-6 Luna (max), Codex: 0.382
  - Haiku 5.5 (max), Claude Code: 0.339
- About 15 exact matches plus 2 with unstated effort. MiMo, MiniMax, GPT-5.6 Luna and every non-max effort row are missing.

**AA ITBench-AA** (AA model pages, field `itBenchSre`). Source for all rows: [AA snapshot](https://artificialanalysis.ai/evaluations/itbench-aa) (repository file `data/aa/aa_v432_snapshot.json`); AA's evaluation page shows GPT-5.6 Sol Max 56.2% and Gemini 3.8 Flash High 52.5%, matching the snapshot.
- 16 roster configurations have values:
  - GPT-5.6 Sol (max) 0.562
  - Gemini 3.8 Flash (high) 0.525
  - GLM-5.3-Flash 0.512
  - Fable 5.1 (max) 0.495
  - GPT-6 Sol (max) 0.494
  - GPT-6 Astra (max) 0.486
  - Kimi K3 (max) 0.477
  - GLM-5.3 (max) 0.461
  - GPT-5.5 (xhigh) 0.458
  - GLM-5.2 (max) 0.427
  - Grok 4.7 (xhigh) 0.421
  - Gemini 3.5 Flash (high) 0.403
  - GPT-5.6 Luna (max) 0.403
  - Qwen3.8 Max (0902) 0.403
  - Opus 5.5 (max) 0.382
  - Muse Spark 1.3 (max) 0.332
- ValueRank's coverage matrix records 16/49 (32.65%). GPT-6.1 Sol, GPT-6 Luna, MiMo, Haiku 5.5, Sonnet 5.5, Gemini 4 Argon and Muse Wonder are among the missing. — repository file `data/coverage_matrix.json`

**Scale SWE Atlas Codebase QnA** (Scale's own board, last updated 2026-07-28). Source: [Scale Labs](https://labs.scale.com/leaderboard/sweatlas-qna).
- Roster-model rows:
  - Opus 5 (Claude Code, xHigh) 63.17
  - Fable-5.1 (Claude Code, xHigh) 59.95
  - GPT 6 Astra (Codex, xHigh) 59.14
  - Opus 4.8 (Claude Code, xhigh) 57.26
  - GLM 5.2 (mini-SWE-agent, effort not stated) 48.12
  - Gemini 3.8 Flash (mini-SWE-agent, effort not stated) 47.04
  - GPT-5.6-Sol (Codex, xHigh) 46.00
  - GPT 5.5 (Codex, xHigh) 45.43
- Only GPT-5.5 (xhigh) is an exact roster match. The others are at xhigh where the roster uses max, or have no stated effort.

**Epoch MirrorCode** (Epoch-run). Source: [Epoch zip](https://epoch.ai/data/benchmark_data.zip) `mirrorcode.csv`.
- 10 models in all. Roster rows:
  - claude-opus-5-5_max 0.774
  - claude-fable-5-1_high 0.733
  - claude-fable-5_high 0.639
  - gemini-4-argon_high 0.589
  - gpt-6-astra_high 0.467
  - gpt-5.6-sol_high 0.200
  - gpt-5.5_high 0.100
- Only Opus 5.5 (max) and Argon (high) match roster efforts exactly.

**WeirdML v3** (ML-engineering coding, run by Håvard Tveit Ihle). Source: [Epoch zip](https://epoch.ai/data/benchmark_data.zip) `weirdml_v3_external.csv`; [htihle.github.io/weirdml](https://htihle.github.io/weirdml.html).
- Mostly xhigh rows:
  - gpt-6-astra_xhigh 0.422
  - gpt-6.1-sol_xhigh 0.383
  - claude-opus-5-5_xhigh 0.312
  - claude-fable-5-1_xhigh 0.260
  - gemini-4-argon_high 0.202
  - claude-sonnet-5-5_xhigh 0.199
  - gpt-6-sol_xhigh 0.197
  - muse-wonder-1.0_xhigh 0.152
  - claude-haiku-5-5_xhigh 0.117
  - grok-4.7_xhigh 0.085
  - gpt-6-luna_xhigh 0.079
  - gemini-3.8-flash_high 0.074
  - muse-spark-1.3_xhigh 0.067
  - deepseek-v4.1-flash_high 0.059
  - gpt-5.6-luna_xhigh 0.052
- About 7 exact roster matches.

**GSO** (software optimization, OpenHands scaffold). Source: [Epoch zip](https://epoch.ai/data/benchmark_data.zip) `gso_external.csv`, source [gso-bench.github.io](https://gso-bench.github.io/index.html).
- 2026 rows: gpt-6-astra 0.794, claude-fable-5-1 0.882, gpt-5.6-sol 0.765, claude-sonnet-5 0.373, claude-fable-5 0.784 and claude-opus-4-8 0.471. **Effort is "unknown" for all of them.**

**PostTrainBench**
- Last roster-relevant rows are July 2026 (Opus 5, Kimi K3, GPT-5.6 Sol (Max), GLM 5.2 (Max), Fable 5 (Max)), run in vendor CLIs (Claude Code, Codex CLI). — [Epoch zip](https://epoch.ai/data/benchmark_data.zip) `posttrainbench_external.csv`

**DevOps/SRE beyond ITBench-AA**
- SRE-World (NeurIPS 2026): 44 live-incident tasks on Kubernetes. Reported GPT 5.6 at 29% pass@1 and GLM 5.3 at 24%; seen only through a search snippet, without exact efforts. — [NeurIPS 2026 SRE-World](https://neurips.cc/virtual/2026/173084)
- SREGym (May 2026): no scores found. — [EmergentMind SREGym](https://www.emergentmind.com/topics/sregym)
- PagerDuty's SRE harness comparison is vendor-run (17 scenarios). — [PagerDuty](https://www.pagerduty.com/?p=101347)

### Inferences
Approximate exact-effort coverage (51 roster configurations / 19 frontier-set configurations). "~" marks an effort-ambiguous match counted as a hit.

| Benchmark | Roster exact | Frontier set exact | Frontier-set holes |
|---|---|---|---|
| CursorBench 4.0 | ~25 (+1~) | 9/19 (Haiku ×5, Opus 5.5, Sonnet 5.5 max, GPT-5.6 Luna max, Argon) | GPT-6 Luna, GPT-6.1 Sol ×4, Astra, MiMo ×2, DeepSeek V4.1, MiniMax |
| Arena WebDev | ~26 (+1~) | 9/19 (GPT-6 Luna, GPT-6.1 Sol max, Opus 5.5, Argon, Astra, MiMo ×2, DeepSeek V4.1 1017, MiniMax~) | Haiku ×5, GPT-6.1 Sol med/high/xhigh, Sonnet 5.5 max, GPT-5.6 Luna max |
| SWE-Atlas-QnA-AA | ~15 (+2~) | 9/19 (GPT-6 Luna, Haiku max, GPT-6.1 Sol max, Opus 5.5, Sonnet 5.5, Argon, Astra, DeepSeek V4.1) | Haiku ×4, GPT-6.1 Sol ×3, MiMo ×2, GPT-5.6 Luna, MiniMax |
| FrontierSWE V2 | ~15 (+3~) | 5/19 (Haiku max, Opus 5.5, Sonnet 5.5, Argon, Astra) | most |
| ITBench-AA | 16 | 3/19 (Opus 5.5, Astra, GPT-5.6 Luna) | most |
| WeirdML v3 | ~7 | ~3/19 (Haiku xhigh, GPT-6.1 Sol xhigh, Argon) | most |
| MirrorCode | 2 | 2/19 | most |
| SWE-bench (any), Aider, LCB, METR, Scale SWE-Bench Pro, SWE-rebench | 0–3 (Epoch Verified: GLM-5.2 max, Gemini 3.5 Flash high) | 0 | all |

- The union of CursorBench and Arena WebDev covers 16/19 frontier-set configurations, missing only GPT-6.1 Sol medium/high/xhigh. However, the two measure different things (task success versus human preference on web apps), so a pooled leaf would be a policy construct, not one benchmark.
- **GPT-6.1 Sol below max is uncovered by every non-AA source found.** Only WeirdML has an xhigh row, and WeirdML is ML-coding, not SWE. Any new leaf would therefore leave four frontier GPT-6.1 Sol rows unranked under O36, unless the leaf's weight is redistributed when missing.
- CursorBench's total absence of the GPT-6 family (and of Chinese open-weight models other than GLM) looks like a publisher selection choice, not a lag. GPT-6 Astra (released 2026-09-03) is missing although later models (Opus 5.5, Argon, Haiku 5.5, Muse Wonder) are present. The coverage hole is therefore unlikely to close by waiting.

### Gaps
- The current Arena WebDev scores for MiMo-V2.6-Flash, MiniMax-M3.1-Flash, DeepSeek-V4.1-Flash-20261017 (Max), Qwen3.8-max-0902 and Muse Wonder Full, and all Agent Arena values, are unknown. arena.ai returned HTTP 403, and Epoch's mirror predates those additions.
- Why CursorBench omits GPT-6-family models was not found on the page.
- AA's roster identity for GLM-5.3-Flash, MiMo, Qwen3.8 Max and MiniMax carries no effort label, so their matches to effort-labelled rows are uncertain.
- The FrontierSWE effort labels come only from Epoch's mirror and are not confirmed on FrontierSWE's page.

## Q3. Methodology: who runs models, harness, effort labelling, data access, contamination/saturation, independence from AA

### Takeaway
The independent, uniformly-run candidates with current data are CursorBench (Cursor-run; harness not disclosed; private tasks from real Cursor sessions), FrontierSWE (Proximal-run "proximus" harness; 34 very long tasks; 5 trials), Epoch MirrorCode (Epoch-run, Inspect logs public) and Arena (crowd preference Elo). AA's SWE-Atlas-QnA-AA and ITBench-AA are AA-run, which adds to ValueRank's existing AA dependence. SWE-Atlas-QnA-AA also uses **vendor-chosen agent harnesses** and **a roster model (GPT-6 Luna xhigh) as judge**. Only CursorBench and Arena publish several efforts per model, and only CursorBench does so systematically.

### Cited Findings
- **CursorBench 4.0**
  - Tasks are "ambiguous, multi-file tasks from real Cursor sessions". Version 4.0 (2026-09-10) added long-horizon editing, refactoring, investigation, intent understanding, job management and design adherence. Earlier versions covered edit/refactor/bugfix (3.0), codebase understanding, bug-finding, planning and code review (3.1), and instruction following and tool use (3.2).
  - The task count and harness are **not stated**, and no contamination controls are described.
  - Cost per task is computed from published per-token prices.
  - The page says small differences may not be significant.
  - There is no download on Cursor's page, but Epoch mirrors the table as CSV (CC-BY).
  - Updates are irregular and versioned by changelog. — [cursor.com/cursorbench](https://cursor.com/cursorbench); [Epoch zip](https://epoch.ai/data/benchmark_data.zip)
- **CursorBench conflict of interest:** Cursor ships its own model (Composer 2.5 is on the board at 27.7%). — [cursor.com/cursorbench](https://cursor.com/cursorbench)
- **FrontierSWE V2**
  - Run by Proximal (repo Proximal-Labs/frontier-swe-v2).
  - 34 tasks "at the edge of human ability", e.g. a Lean 4 kernel type checker in Pascal, a SPICE simulator in Rust and a Quantum ESPRESSO port to Rust.
  - Mean@5 with best/worst@5, 20-hour budget per trial; every model is labelled "proximus".
  - Effort, cadence and a data download are not stated; per-run traces are linked.
  - Cost per trial ranges from $8.57 to $1,029.65. — [frontierswe.com](https://www.frontierswe.com/)
- **Arena Code Arena / Agent Arena**
  - Human pairwise preference Elo.
  - Agent Arena added automated sub-scores: Steerability, revised 2026-09-30, and Bash Reliability, renamed and given an LLM-judge failure detector on 2026-10-12.
  - Arena rebranded from LMArena in January 2026 (per a search summary).
  - The live leaderboard returned HTTP 403 to automated fetch. Epoch mirrors WebDev scores and votes, but the mirror has no confidence intervals and lags additions by days to weeks. — [Arena changelog](https://arena.ai/blog/leaderboard-changelog/); [Epoch zip](https://epoch.ai/data/benchmark_data.zip) `webdev_arena_external.csv`
- **SWE-Atlas-QnA-AA (AA)**
  - 124 repository Q&A tasks, pass/fail aligned with Scale's Task Resolve Rate, mean of 3 attempts.
  - The v2.0 change replaced Scale's grading with **GPT-6 Luna (xhigh) as judge, five votes per criterion, 127 rubric criteria reworded**, published on Hugging Face.
  - Each configuration is an agent product (Claude Code, Codex, Antigravity CLI, Grok Build, Kimi Code CLI, Opencode, DeepSeek Harness, Muse Code, Devin Fusion), so **harness varies by vendor**. — repository files `research/2026-10-23-refresh/coding-agents-methodology-version-history-2026-10-23.txt` and [AA CAI v2.0 capture]; [AA coding agents](https://artificialanalysis.ai/agents/coding-agents)
- **ITBench-AA (AA, with IBM)**
  - Kubernetes incident root-cause analysis on offline snapshots.
  - 59 tasks: 40 from IBM's public release and 19 private ones shared with AA. Each task is run 3 times.
  - Metric: average precision at full recall. A task scores 0 unless every true root cause is found.
  - Harness: AA's open-source Stirrup, uniform, with a 100-turn cap.
  - AA describes it as its own independent implementation. — [AA ITBench-AA](https://artificialanalysis.ai/evaluations/itbench-aa)
- **Scale SWE Atlas**
  - 124 QnA tasks from 11 production repositories in Go, Python, C and TypeScript.
  - Mixed scaffolds: Claude Code, Codex and mini-SWE-agent, with steps raised from 250 to 500 for newer models.
  - Elevated refusal rates for Fable 5 and GPT-5.6 Sol were scored as failures.
  - Native scaffolds score noticeably higher than a generic harness (per search summary). — [Scale Labs SWE Atlas QnA](https://labs.scale.com/leaderboard/sweatlas-qna); [Scale blog](https://scale.com/blog/swe-atlas-complete)
- **Scale SWE-Bench Pro:** licence-restricted (copyleft) public repositories plus private startup codebases for contamination resistance. Scores drop on the private set (e.g. Claude Opus 4.1 22.7% to 17.8%). — [Scale Labs SWE-Bench Pro](https://labs.scale.com/leaderboard/swe_bench_pro)
- **SWE-rebench:** a rolling window of fresh GitHub issues for contamination resistance; data on Hugging Face (`nebius/SWE-rebench-leaderboard`) and Docker images on Docker Hub. — [swe-rebench.com](https://swe-rebench.com/)
- **Epoch:** separates internal runs from external imports. SWE-bench Verified and MirrorCode are internal, with public Inspect logs per run; Aider is external. Data comes as CSV and through the `epochai` Python client. — [Epoch benchmarks](https://epoch.ai/benchmarks); [Epoch zip](https://epoch.ai/data/benchmark_data.zip) `swe_bench_verified.csv` (Log viewer / Logs columns)
- **METR:** publishes YAML of benchmark and per-task results, uses over a hundred software tasks (RE-Bench, HCAST, short tasks), and is no longer actively updated. — [METR time horizons](https://metr.org/time-horizons/)
- **Saturation:**
  - Aider Polyglot tops out at 88.0%. — [Aider](https://aider.chat/docs/leaderboards/)
  - SWE-bench Verified mini-SWE-agent sits at 70–77% with flawed tasks. — [SWE-bench JSON](https://raw.githubusercontent.com/SWE-bench/swe-bench.github.io/master/data/leaderboards.json); [the-decoder](https://the-decoder.com/openai-wants-to-retire-the-ai-coding-benchmark-that-everyone-has-been-competing-on/)
  - Not saturated: CursorBench (top 57.8%), FrontierSWE (top 65.5%), SWE-Atlas-QnA-AA (top 0.688) and ITBench-AA (top 0.562). — sources above

### Inferences
- **Independence from AA.** CursorBench, FrontierSWE, Arena, Epoch MirrorCode and WeirdML are independent of AA. SWE-Atlas-QnA-AA and ITBench-AA are AA-run (ITBench-AA co-sourced with IBM), and adding them would deepen ValueRank's single-source dependence. SWE-Atlas-QnA-AA's judge is itself a ranked roster model (GPT-6 Luna), a potential self-preference concern.
- **Configuration semantics.** SWE-Atlas-QnA-AA and Scale SWE Atlas measure the model plus its vendor agent product. That is a different configuration notion from ValueRank's "model + effort via API", and on AA the efforts are mostly the vendor default (max). Mapping to roster rows is exact only where the effort label coincides.
- **Statistical noise.** FrontierSWE has 34 tasks and Arena WebDev has 1,200–5,600 votes for new models, so per-row noise bands would be wide. CursorBench's undisclosed task count prevents ValueRank's task-sampling noise approximation (O39) from being computed.
- **Machine-readable capture.**
  - Epoch's CC-BY bulk zip is the most practical route for CursorBench, WebDev, FrontierSWE, MirrorCode, GSO and WeirdML. It is refreshed daily (files time-stamped the same morning), but it lags source pages.
  - Cursor and FrontierSWE publish only rendered pages.
  - Arena blocks automated fetch.

### Gaps
- CursorBench's harness, task count and contamination policy are undisclosed.
- What "proximus" is (the harness, or a Proximal run label) is not stated on FrontierSWE's page.
- MirrorCode's task description and count were not retrieved; only Epoch's CSV was read.
- GSO's OPT@1 values for 2026 models (0.77–0.88) are far above its earlier scale (0.23–0.47 for early-2026 models). A metric or version change may lie behind this but was not verified.

## Q4. What this means for adding SWE quality leaves under O36

### Takeaway
**No candidate in this scope can become a stand-alone quality leaf without making many frontier configurations unrankable under O36.** CursorBench is the strongest independent, per-effort, current, unsaturated candidate. But it lacks the whole GPT-6 family (6 frontier-set configurations at current roster efforts: GPT-6 Luna, GPT-6.1 Sol ×4, GPT-6 Astra) plus MiMo ×2, DeepSeek V4.1 Flash 1017 and MiniMax-M3.1-Flash. Arena WebDev complements it on exactly those models but is a preference metric. Everything else is stale, saturated, AA-run, effort-ambiguous or too thin.

### Cited Findings
- CursorBench exact-effort coverage: about 25/51 roster and 9/19 frontier-set configurations, none from the GPT-6 family. — [cursor.com/cursorbench](https://cursor.com/cursorbench); [Epoch zip](https://epoch.ai/data/benchmark_data.zip)
- Arena WebDev coverage: about 26/51 roster and 9/19 frontier-set configurations, with no Haiku 5.5 and no GPT-6.1 Sol below max. — [Epoch zip](https://epoch.ai/data/benchmark_data.zip); [Arena changelog](https://arena.ai/blog/leaderboard-changelog/)
- SWE-Atlas-QnA-AA coverage: about 15/51 roster, 9/19 frontier set, AA-run. ITBench-AA: 16/49 cohort per ValueRank's coverage matrix. — [AA CAI v2.0 capture]; repository file `data/coverage_matrix.json`
- O36 ranks only configurations with every leaf. — `/home/user/valuerank/AGENTS.md`; brief `research/2026-10-23-swe-benchmarks/brief.md`

### Inferences
- **If the editor wants an independent SWE leaf now**, CursorBench is the only candidate whose rows carry exact efforts across efforts. Its use would require either (a) owner acceptance that its weight is redistributed when missing, which conflicts with O36's all-leaves rule as written, or (b) pooling it with Arena WebDev and/or AA's SWE-Atlas-QnA-AA into a "supplementary SWE" leaf that takes whichever exact-configuration source exists. Option (b) still leaves GPT-6.1 Sol medium/high/xhigh uncovered (all three sources lack them) and mixes constructs.
- **Diagnostic only**: FrontierSWE (thin, effort labels only via Epoch, extreme per-trial cost spread), MirrorCode (2 exact matches), WeirdML v3 (ML coding), ITBench-AA (AA-run, 16/51, but the only DevOps/SRE source with a uniform harness and current roster data, which makes it the natural DevOps candidate if AA dependence and coverage were acceptable).
- **Not usable**: SWE-bench Verified/bash-only/Multilingual (stale since Feb 2026, contaminated), SWE-bench Pro (no independent roster results; vendor-reported numbers lack efforts; public split reportedly about 30% broken, unverified), Aider Polyglot, LiveCodeBench, METR time horizon (stopped updating; no roster model), SWE-rebench (no post-July models; efforts mismatch), CodeClash, SWE-Lancer, Multi-SWE-bench, KernelBench (aggregator-only, thin), GSO (effort unknown), PostTrainBench (vendor CLIs; nothing after July 2026), Scale SWE Atlas (1 exact match).
- **Weight suggestion (owner decision needed):** if any of these is admitted, a small weight (e.g. ≤10% of the 60% SWE block) limits the leverage of a source with undisclosed task count (CursorBench) or preference-based scoring (Arena). This is the researcher's inference, not a sourced recommendation.

### Gaps
- Whether Cursor intends to add GPT-6-family, MiMo, DeepSeek or MiniMax rows is unknown, and no public statement was found.
- No source was found that runs GPT-6.1 Sol at medium/high/xhigh on any agentic SWE benchmark outside AA.
