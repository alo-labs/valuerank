# Vals AI coding and software-engineering benchmarks (captured 2026-10-23)

Capture method: every Vals benchmark page is a static Astro page. Each page carries a `benchmarkViewUrl` prop that points to a content-hashed JSON file (`/_astro/benchmark_view_<id>.<hash>.json`). That file holds `metadata` (version, `updated` date, harness, runner, mode, dataset_type, task splits) and `tasks.<split>.<model_key>` records. Each record holds `accuracy`, `stderr`, `cost_per_test`, `latency`, `token_totals` (input/output/reasoning/cache-read/cache-write), `temperature`, `max_output_tokens`, `reasoning_effort` or `compute_effort`, and `provider`. All values below were read from those JSON files on 2026-10-23 and spot-checked against the rendered leaderboard text. Roster matching was done by Vals model key. The ValueRank frontier and near-frontier efforts come from `data/aa_reconciliation_inventory.json` (observedAt 2026-10-23T05:27:39Z).

## Q1. Which Vals benchmarks are relevant to SWE/DevOps, and what is each one's methodology?

### Takeaway
Vals hosts about 15 coding-adjacent boards. Vals runs every model itself on one fixed harness per benchmark. Within a benchmark the harness is the same for every model, but it differs across benchmarks: mini-SWE-agent, Terminus 2, OpenHands, OpenCode or Pi. The strongest SWE candidates are:
- Terminal-Bench 4.0 (66 public tasks, avg@3);
- Vibe Code Bench v1.1 (private, building full web apps);
- Code Migration v1/v1.1 (private, program translation);
- SWE-bench Multimodal (480 public tasks).

Several other boards are saturated, stale or off-topic: SWE-bench Verified at 97%, LiveCodeBench last updated 2026-09-01, IOI tied at 100%, ProgramBench near 0%, and "SRE Bench", which is binary reverse engineering rather than site reliability work.

### Cited Findings
**General Vals methodology**
- For public benchmarks (e.g. Terminal-Bench, SWE-bench, IOI), Vals says "we run every model ourselves under the same harness and settings, so results are comparable across models". Proprietary benchmarks are scored only on a private test set "to prevent leakage into the training data". — [Vals methodology](https://www.vals.ai/methodology)
- Error bars:
  - Single-run boards: SEM over instance scores.
  - Terminal-Bench (and Finance Agent v2, BioMysteryBench): SEM over three independent runs.
  - Vals says these errors "do not reflect variability across prompts, seeds, deployment settings".
  - "Models are called through a fixed harness that we control, so that differences in scores reflect the model rather than the scaffold". Some benchmarks also run "a model's own native agent where one exists (for example, Claude Code or Codex)".
  - Source: [Vals methodology](https://www.vals.ai/methodology)

**Benchmark list.** These are the Vals benchmark slugs relevant to coding, from the [benchmarks index](https://www.vals.ai/benchmarks) and [home](https://www.vals.ai/home):
- swebench (SWE-bench Verified)
- swebench-multimodal
- terminal-bench (1.0), terminal-bench-2, terminal-bench-2-1, terminal-bench-4
- terminal-bench-science
- vibe-code (Vibe Code Bench v1.1), vcb-1-100
- code-migration (v1), code-migration-v1-1
- programbench
- lcb (LiveCodeBench)
- ioi (v2), ioi-v1 (archived)
- skillsbench
- srebench
- cyber (CyberBench v1.1)
- vals_index (a composite)

**Terminal-Bench 4.0** (JSON: version 4.0, updated 2026-10-22, harness "Mini-SWE-agent", runner external, mode agentic, 54 models)
- Tasks: 66 new community tasks with no overlap with 2.1's 89. Categories: Software 18, Science 14, ML 11, Operations 9, Hardware 5, Security 5, Media 4. "Roughly three quarters of 4.0 is outside traditional software engineering".
- Harness: mini-swe-agent with a single bash tool and no step or cost limit, run on Daytona sandboxes with an 8-hour limit per task.
- Scoring: avg@3 (three full runs, each pass@1), with SE across the three runs.
- Source: [Vals TB4](https://www.vals.ai/benchmarks/terminal-bench-4)

**Terminal-Bench 2.1** (updated 2026-09-28, 76 models)
- 89 tasks, run on the Terminus 2 harness, scored pass@1. A model must pass all pytests to get credit for a task.
- Source: [Vals TB2.1](https://www.vals.ai/benchmarks/terminal-bench-2-1)

**SWE-bench Verified** (slug swebench, updated 2026-09-01, 88 models)
- 500 tasks, run on a "minimal bash-tool-only agent harness" (the leaderboard labels it Mini-SWE-agent).
- Task-time buckets: <15 min 194, 15m–1h 261, 1–4 h 42, >4 h 3.
- Top score is 97.00% (Claude Opus 5).
- Source: [Vals SWE-bench](https://www.vals.ai/benchmarks/swebench)

**SWE-bench Multimodal** (updated 2026-10-16, 20 models)
- 480 test-split tasks from 11 JavaScript repositories whose issues depend on screenshots. Harness is mini-swe-agent; grading uses the upstream SWE-bench harness. Each model is run once and the error bars are binomial SE.
- The agent has no internet access. Vals says closing the network "cost each model between 21 and 35 percentage points", because the instance id reveals the upstream fix PR.
- Source: [Vals SWE-bench Multimodal](https://www.vals.ai/benchmarks/swebench-multimodal)

**Vibe Code Bench v1.1** (slug vibe-code, private dataset, updated 2026-10-20, 118 models)
- Task: build complete web applications from a natural-language spec, with up to 5 hours or 1,000 turns per application. The leaderboard harness is "OpenHands", with Supabase and other sandbox services.
- Grading: a browser-use evaluator agent runs point-and-click UI tests. The metric is test pass rate.
- The page does not state a task count in its text (gap). The page says v1.1 was "released on February 24, 2025"; that date looks inconsistent with the GPT-5.2-era app examples and may be a typo.
- Source: [Vals Vibe Code Bench](https://www.vals.ai/benchmarks/vibe-code)

**Vibe Code Bench 1-100** (slug vcb-1-100, private, updated 2026-10-17, 26 models)
- Starting point: a working VCB v1.1 app, extended through up to 10 dependent product requests.
- Data: 50 test scenarios (reported) plus 50 validation scenarios; 939 requests and 11,299 browser workflows across both sets.
- Scoring: consecutive fully passing iterations, stopping at the first failure.
- Harness: a modified OpenHands V1 environment with a 10-hour budget per task.
- Source: [Vals VCB 1-100](https://www.vals.ai/benchmarks/vcb-1-100)

**Code Migration v1.1** (private, updated 2026-10-20, 28 models) and **Code Migration v1** (updated 2026-10-18, 79 models)
- CLI split: 30 open-source repositories in Python, Java, Kotlin, Rust and C++. Each is migrated into its 4 non-source languages, giving 120 migrations, each graded by about 100–400 hidden behaviour tests.
- COBOL split: 10 repositories, COBOL to Java.
- Weighting: Overall weights every source repository equally, so CLI carries 3x the weight of COBOL. Code quality is a separate diagnostic.
- An anti-cheat checker zeroes submissions that wrap the original executable.
- v1.1 runs every model on the "Pi agent harness instead of mini-SWE-agent" with revised hidden tests. Vals says the two versions are "not directly comparable".
- Source: [Vals Code Migration v1.1](https://www.vals.ai/benchmarks/code-migration-v1-1)

**ProgramBench** (updated 2026-10-12, 64 models)
- 200 public tasks: rebuild a CLI program from an execute-only binary plus a behavioural specification.
- Harness: mini-SWE-agent with 1,000 steps and a 6-hour limit, offline.
- The headline metric is "Fully Resolved" (passes all hidden tests); "Almost Resolved" (≥95%) and raw pass rate are also reported.
- Source: [Vals ProgramBench](https://www.vals.ai/benchmarks/programbench)

**LiveCodeBench** (updated 2026-09-01, runner "platform", mode one-shot, 143 models)
- Vals' own implementation of LiveCodeBench code generation: Python solutions to LeetCode, AtCoder and Codeforces problems, split easy/medium/hard. The page cites v6 with "over 1000" problems from May 2023–2025.
- Source: [Vals LCB](https://www.vals.ai/benchmarks/lcb)

**IOI v2** (updated 2026-10-20, 45 models)
- Setup: IOI 2024, 2025 and 2026, six problems per year (18 in all), run in the OpenCode agent with a C++20 toolchain and no submission or score feedback.
- Scoring: official subtask grading out of 100; overall score is the mean of the three yearly scores.
- Vals notes the 2026 problems were released after the cohort was trained.
- Source: [Vals IOI](https://www.vals.ai/benchmarks/ioi)

**SkillsBench** (updated 2026-09-27, 35 models)
- BenchFlow's benchmark, run in OpenHands with and without skills. The leaderboard headline is "With Skills".
- Source: [Vals SkillsBench](https://www.vals.ai/benchmarks/skillsbench)

**SRE Bench** (industry tag "cyber", private, updated 2026-10-14)
- Description: "Can AI agents reverse engineer real-world, contamination-free binaries?" SRE here means software reverse engineering, not site reliability engineering.
- Source: [Vals SRE Bench](https://www.vals.ai/benchmarks/srebench)

**CyberBench v1.1** (private, updated 2026-10-12)
- Task: craft PoC inputs that trigger OSS-Fuzz vulnerabilities, then patch them.
- Source: [Vals CyberBench](https://www.vals.ai/benchmarks/cyber)

**Vals Index v2.2** (updated 2026-10-22, 26 models)
- A GDP-weighted composite across finance, coding, legal and tax. Its components include terminal_bench_4, vibe_code_bench and code_migration.
- Source: [Vals Index](https://www.vals.ai/benchmarks/vals_index)

**Other boards checked and judged not SWE**
- Time Horizon Index (Kerbal Space Program agent, 13 models): [Vals](https://www.vals.ai/benchmarks/time_horizon_index)
- Terminal-Bench-Science (research workflows across five science domains): [Vals](https://www.vals.ai/benchmarks/terminal-bench-science)
- CUA-bench (video games): [Vals](https://www.vals.ai/benchmarks/cua_bench)
- VoiceCodeBench (speech-to-text): [Vals](https://www.vals.ai/benchmarks/voice-code-bench)

### Inferences
- Within each benchmark the harness is fixed across models, which is good for comparability. Across benchmarks it varies, and two benchmarks changed harness between versions (TB2.1 Terminus 2 to TB4 mini-SWE-agent; Code Migration v1 mini-SWE-agent to v1.1 Pi). Scores are therefore harness-specific and not comparable with vendor or AA numbers on the same task set.
- Ranked by SWE relevance, the most relevant are Vibe Code Bench v1.1, Code Migration, VCB 1-100 and SWE-bench Multimodal. TB4's Software category (18 tasks) is a narrower SWE slice. LCB and IOI test algorithmic or competitive programming, not SWE or DevOps work. No Vals benchmark targets DevOps or SRE operations directly; TB4's Operations category is business operations (logistics, finance, claims), not infrastructure.

### Gaps
- Vibe Code Bench v1.1 task count (number of app specs in the test set) is not stated in the page text. The task-level JSON would have to be inspected to count it.
- The SWE-bench Verified page does not show step or cost limits.
- I did not find a published, versioned changelog per benchmark.

## Q2. Do results name the exact model version and reasoning effort? Roster coverage with values

### Takeaway
Each Vals record names a model version and, in metadata, an effort. Vals publishes only one configuration per model per benchmark, almost always the highest effort (max; Gemini at high; Grok 4.7 at xhigh). So Vals cannot supply the lower-effort frontier rows ValueRank needs:
- GPT-6 Luna low/medium/high/xhigh;
- Claude Haiku 5.5 medium/high/xhigh/low;
- GPT-6.1 Sol medium/high/xhigh;
- Claude Opus 5.5 high/xhigh;
- GPT-5.6 Luna low.

Among the 18 AA frontier rows, at most 6 have a plausible exact-effort match on any Vals board, and 4 of those carry effort ambiguity.

Vibe Code Bench v1.1 is the only Vals board that covers every roster model at least once. TB4 covers every roster model except GPT-5.5, Gemini 3.6 Flash and GLM-5.2.

### Cited Findings
**How Vals records effort and identity** (all from the benchmark JSON files linked in Q3)
- Each record carries `reasoning_effort` (OpenAI, Google, xAI, Meta, DeepSeek, Z.ai) or `compute_effort` (Anthropic, MiniMax). Examples from TB4 JSON:
  - claude-opus-5-5 `compute_effort: max`;
  - gpt-6.1-sol `reasoning_effort: max`;
  - gemini-4-argon `high`;
  - grok-4.7 `xhigh`;
  - Xiaomi MiMo and Alibaba Qwen records have effort `null` (not stated).
  - Source: [TB4 JSON](https://www.vals.ai/_astro/benchmark_view_terminal_bench_4.CuDVYVFE.json)
- Effort differs by benchmark for the same model. Claude Opus 5.5 is `high` on TB2.1, `xhigh` on VCB 1-100 and `max` elsewhere. Claude Sonnet 5.5 is `high` on TB2.1 and `max` elsewhere. — [TB2.1 JSON](https://www.vals.ai/_astro/benchmark_view_terminal_bench_2_1.CdyoObsA.json); [VCB 1-100 JSON](https://www.vals.ai/_astro/benchmark_view_vcb_1_100.pkR83uRc.json)
- Vals model pages state the effort used. For Claude Haiku 5.5: "Evaluations were run with compute effort set to 'max'" (release Oct 7, 2026). — [Vals Claude Haiku 5.5](https://www.vals.ai/models/anthropic_claude-haiku-5-5)
- Extra keys exist beyond the main record:
  - "-range" keys: `anthropic/claude-opus-5-5-range` on CyberBench (74.58) and SRE Bench (21.76); `claude-sonnet-5-range` on CyberBench. Their meaning is undocumented.
  - Dated or variant keys: `deepseek-v4-pro` vs `deepseek-v4-pro-0813`, and `deepseek-v4.1-flash` vs `deepseek-v4.1-flash-1017`. These need careful identity mapping.
  - Source: [CyberBench JSON](https://www.vals.ai/_astro/benchmark_view_cyberbench.DS6UOlu0.json)
- No per-model run date appears in the JSON, only the benchmark-level `updated` date. — all JSON files

**Frontier and near-frontier configurations** (AA identity → Vals effort). Format is score % [effort]; "–" means absent. These values come from the [TB4](https://www.vals.ai/_astro/benchmark_view_terminal_bench_4.CuDVYVFE.json), [VCB v1.1](https://www.vals.ai/_astro/benchmark_view_vibe_code_bench.P9c_CCAs.json), [Code Migration v1.1](https://www.vals.ai/_astro/benchmark_view_code_migration_v1_1.FUJxA2BT.json), [Code Migration v1](https://www.vals.ai/_astro/benchmark_view_code_migration.Dttzoqk3.json), [SWE-bench MM](https://www.vals.ai/_astro/benchmark_view_swebench_multimodal.C7UOLrm7.json), [TB2.1](https://www.vals.ai/_astro/benchmark_view_terminal_bench_2_1.CdyoObsA.json), [VCB 1-100](https://www.vals.ai/_astro/benchmark_view_vcb_1_100.pkR83uRc.json), [IOI](https://www.vals.ai/_astro/benchmark_view_ioi.DV1xD5vC.json) and [SWE-bench Verified](https://www.vals.ai/_astro/benchmark_view_swebench.Ae8ni7h0.json) JSON files.

| AA config (frontier F / near N) | Vals effort | TB4 | VCB v1.1 | CM v1.1 | CM v1 | SWE-MM | TB2.1 | VCB 1-100 | IOI v2 | SWE-V |
|---|---|---|---|---|---|---|---|---|---|---|
| GPT-6 Luna (F: low, medium, high, xhigh, max) | max only | 13.64 | 81.65 | 46.67 | 42.55 | 37.50 | 73.03 | – | 55.56 | – |
| Claude Haiku 5.5 (F: medium, high, xhigh; N: low, max) | max only | 36.36 | 90.44 | 52.36 | 44.57 | 43.96 | – | 20.41 | 47.28 | – |
| MiMo-V2.6-Flash (F, AA "reasoning") | not stated | 24.24 | 78.96 | 39.55 | 40.93 | – | 76.40 | – | 47.67 | – |
| MiMo-V2.6-Pro (F, AA "reasoning") | not stated | 31.31 | 85.22 | 48.79 | 43.01 | 41.25 | 67.79 | – | 39.33 | – |
| GPT-6.1 Sol (F: medium, high, xhigh, max) | max only | 55.05 | 88.93 | 77.32 | 65.12 | 43.54 | – | – | 96.89 | – |
| Claude Opus 5.5 (F: high/xhigh/max "with fallback"; N: medium) | mostly max (TB2.1 high, VCB 1-100 xhigh) | 65.15 | 90.29 | 81.01 | 66.65 | 70.21 | 87.64 [high] | 30.36 [xhigh] | 95.06 | – |
| Claude Sonnet 5.5 (F: max w/ fallback; N: xhigh) | max (TB2.1 high) | 64.14 | 92.39 | 86.88 | 69.83 | 58.33 | 83.15 [high] | – | 83.06 | – |
| GPT-6 Astra (N: high, xhigh, max) | max | 59.60 | 89.59 | 80.58 | 67.74 | 43.33 | 87.27 | 27.64 | 100.00 | – |
| Gemini 4 Argon (N: high) | high | 57.58 | 91.91 | 70.80 | 68.17 | 56.04 | – | 21.20 | 100.00 | – |
| DeepSeek V4.1 Flash 1017 (N: max) | max | 31.82 | 87.73 | 67.52 | 44.21 | – (non-1017 key only: 46.46) | – | – | – | – |
| MiniMax-M3.1-Flash (N, AA "reasoning") | max (compute_effort) | 25.25 | 73.94 | – | – | – | – | – | – | – |
| GPT-5.6 Luna (N: low) | max only (mismatch) | 11.62 | 77.06 | – | 44.55 | – | 79.03 | 22.59 | 61.78 | 93.00 |

Standard errors for the table above:
- TB4: SE across three runs, e.g. Opus 5.5 0.0, GPT-6 Astra 4.40, GPT-6.1 Sol 1.82.
- VCB v1.1: SE 1.3–5.3.
- CM v1.1: SE 1.5–3.9.
- SWE-MM: SE about 2.1–2.3.

**Roster coverage by benchmark** (presence of the model at Vals' single effort, out of the brief's 38 distinct roster models; Muse Spark 1.3 has both xhigh and max keys). Source for all rows: the per-benchmark JSON files in Q3.
- **Vibe Code Bench v1.1:** every roster model present, including Muse Spark 1.3 at xhigh and at max.
- **Terminal-Bench 4.0:** missing GPT-5.5, Gemini 3.6 Flash, GLM-5.2.
- **Code Migration v1:** missing only MiniMax-M3.1-Flash.
- **ProgramBench:** missing Muse Wonder, DeepSeek V4.1 Flash 1017, MiniMax-M3.1-Flash.
- **IOI v2:** missing 8: Claude Fable 5, GPT-5.5, DeepSeek V4 Pro (unsuffixed), Claude Opus 4.8, GLM-5.2, Gemini 3.5 Flash, DeepSeek V4.1 Flash 1017, MiniMax-M3.1-Flash.
- **Terminal-Bench 2.1:** missing GPT-6.1 Sol, Claude Haiku 5.5, Gemini 4 Argon, Muse Wonder, Muse Wonder Full, DeepSeek V4.1 Flash 1017, MiniMax-M3.1-Flash.
- **Code Migration v1.1:** 21 roster slots missing, including GPT-5.6 Sol, GPT-6 Sol, Claude Fable 5/5.1, GPT-5.6 Luna and MiniMax-M3.1-Flash.
- **SWE-bench Multimodal:** 20 models only; 23 roster slots missing.
- **SWE-bench Verified:** 21 hits, but every model released after about August 2026 is missing: GPT-6 Astra, Opus 5.5, GPT-6 Sol, GPT-6.1 Sol, GPT-6 Luna, Grok 4.7, both MiMo-V2.6 models, Haiku 5.5, Sonnet 5.5, Gemini 4 Argon, Fable 5.1, Muse Spark 1.3, both Muse Wonder models, DeepSeek V4.1 Flash 1017, MiniMax-M3.1-Flash.
- **LiveCodeBench:** 20 hits, with the same gap pattern as SWE-bench Verified plus GPT-5.6 Luna and Muse Spark 1.2.
- **VCB 1-100:** 19 hits.
- **SkillsBench:** 19 hits.

**Further TB4 roster values not in the frontier table** (overall %, Vals effort). Source: [TB4 JSON](https://www.vals.ai/_astro/benchmark_view_terminal_bench_4.CuDVYVFE.json)

| Roster model | TB4 % | Vals effort |
|---|---|---|
| Claude Fable 5.1 | 58.08 | max |
| Muse Wonder Full | 58.08 | max |
| Claude Opus 5 | 53.53 | max |
| Muse Wonder | 49.49 | max |
| GPT-6 Sol | 44.44 | max |
| Claude Fable 5 | 41.41 | max |
| GLM-5.3 | 38.89 | max |
| GPT-5.6 Sol | 37.88 | max |
| GLM-5.3 Flash | 37.37 | max |
| Qwen3.8 Max | 34.34 | null |
| Grok 4.7 | 28.79 | xhigh |
| Muse Spark 1.3 | 24.75 | max |
| Muse Spark 1.3 | 10.61 | xhigh |
| Claude Opus 4.8 | 23.23 | max |
| Gemini 3.8 Flash | 19.70 | high |
| DeepSeek V4 Flash 0731 | 18.69 | high |
| Grok 4.6 | 17.17 | high |
| Kimi K3 | 17.17 | max |
| DeepSeek V4 Pro 0813 | 14.14 | max |
| DeepSeek V4 Pro (unsuffixed key) | 11.11 | max |
| Gemini 3.7 Flash | 12.12 | high |
| Claude Sonnet 5 | 10.61 | max |
| Gemini 3.5 Flash | 6.06 | high |
| Muse Spark 1.2 | 6.06 | xhigh |

**TB4 Software category only** (18 tasks). Source: TB4 JSON `tasks.software`.

| Model | Software % |
|---|---|
| GPT-6 Astra | 61.11 |
| Claude Sonnet 5.5 | 59.26 |
| Claude Opus 5.5 | 57.41 |
| GPT-6.1 Sol | 57.41 |
| Gemini 4 Argon | 48.15 |
| Claude Haiku 5.5 | 46.30 |
| MiMo-V2.6-Pro | 38.89 |
| DeepSeek V4.1 Flash 1017 | 37.04 |
| MiMo-V2.6-Flash | 29.63 |
| MiniMax-M3.1-Flash | 22.22 |
| GPT-6 Luna | 14.81 |
| GPT-5.6 Luna | 14.81 |

Software-category SEs range 1.85–8.07.

### Inferences
- **Exact-effort coverage of the 51-configuration roster:**
  - Even the best Vals board (VCB v1.1) can cover at most about 38 of 51 configurations, because Vals publishes one effort per model. At least 13 configurations are structurally absent: GPT-6.1 Sol ×4 lower efforts, Claude Haiku 5.5 ×4, Claude Sonnet 5.5 ×4, and Grok 4.6 (xhigh).
  - Of the 18 AA frontier rows, only GPT-6 Luna (max), GPT-6.1 Sol (max), Claude Sonnet 5.5 (max with fallback), Claude Opus 5.5 (max with fallback), MiMo-V2.6-Flash and MiMo-V2.6-Pro could match.
  - For the two Claude rows, AA's "with fallback" qualifier has no Vals counterpart. For MiMo, Vals states no effort. That leaves only 2 clean matches out of 18.
  - Under O36 (no transfer across efforts), no Vals benchmark can be a full-cohort leaf.
- **Effort mapping for the unsuffixed roster entries** (e.g. "Gemini 3.8 Flash", "Kimi K3", "Grok 4.7") cannot be confirmed from Vals data alone. The editor must compare Vals' stated effort with the AA identity in the reconciliation inventory. Grok 4.6 on Vals is `high`, so it matches only if AA's default Grok 4.6 row is high.
- **Most usable role:** a Vals result could fill a gap for an existing leaf where the policy allows "another party that ran the same benchmark version on the exact configuration". Vals' TB4 run qualifies on benchmark version (4.0) for max-effort rows. Its harness, however, is mini-SWE-agent with avg@3, which may differ from AA's TB4 run, so mixing sources inside one leaf adds harness variance.
- **Pooled leaf:** a pooled "Vals SWE" leaf (e.g. VCB v1.1 + Code Migration + TB4-Software) would cover the max-effort frontier rows well. It would still fail O36 for every lower-effort frontier row. It could therefore only serve as a supplementary, non-ranking diagnostic or an indicative value (O41-style), unless the owner accepts a weight applied only where present.

### Gaps
- What the "-range" keys mean (possibly a sweep across effort levels) is undocumented on the pages I read.
- Whether Vals' `null` effort for MiMo and Qwen means provider default, thinking on or thinking off is not stated in the JSON.
- Vals does not say whether AA's "with fallback" (Opus/Sonnet 5.5) matches its own Anthropic runs.

## Q3. Update cadence, machine-readable data, and cost/latency data

### Takeaway
Vals updates its active coding boards within days of major releases: TB4 on 2026-10-22, VCB on 2026-10-20, Code Migration v1.1 on 2026-10-20, IOI on 2026-10-20. LCB and SWE-bench Verified have been frozen since 2026-09-01. All data can be captured as JSON, but only through content-hashed static asset URLs; I found no documented API. Vals publishes per-model cost per test, token totals including cache and reasoning tokens, list prices, and wall-clock duration, all specific to its own harness and effort.

### Cited Findings
**Last update dates** (JSON `metadata.updated`, cross-checked against page "Updated" and JSON-LD `dateModified`):

| Benchmark | Updated | Notes |
|---|---|---|
| TB4 | 2026-10-22 | |
| Vals Index | 2026-10-22 | |
| VCB v1.1 | 2026-10-20 | |
| Code Migration v1.1 | 2026-10-20 | |
| IOI v2 | 2026-10-20 | |
| Code Migration v1 | 2026-10-18 | |
| VCB 1-100 | 2026-10-17 | |
| SWE-bench MM | 2026-10-16 | |
| SRE Bench | 2026-10-14 | |
| ProgramBench | 2026-10-12 | |
| CyberBench | 2026-10-12 | |
| TB2.1 | 2026-09-28 | |
| SkillsBench | 2026-09-27 | |
| SWE-bench Verified | 2026-09-01 | |
| LCB | 2026-09-01 | |
| TB2.0 | 2026-06-04 | |
| TB1.0 | 2026-01-12 | |
| IOI v1 | 2026-08-09 | archived |

Source: page JSON, e.g. [TB4 page](https://www.vals.ai/benchmarks/terminal-bench-4)

- Release-day coverage: Vals published a Haiku 5.5 write-up covering VCB, Code Migration, EMB and Legal Research Bench. — [Vals Claude Haiku 5.5](https://www.vals.ai/models/anthropic_claude-haiku-5-5)

**Machine-readable endpoints** (found via the `benchmarkViewUrl` prop of each page's `BenchmarkViewLoader` island). The hash suffix changes when the site is rebuilt, so a capture script must first fetch the HTML page and read the current URL.
- [TB4](https://www.vals.ai/_astro/benchmark_view_terminal_bench_4.CuDVYVFE.json)
- [VCB v1.1](https://www.vals.ai/_astro/benchmark_view_vibe_code_bench.P9c_CCAs.json)
- [VCB 1-100](https://www.vals.ai/_astro/benchmark_view_vcb_1_100.pkR83uRc.json)
- [Code Migration v1.1](https://www.vals.ai/_astro/benchmark_view_code_migration_v1_1.FUJxA2BT.json)
- [Code Migration v1](https://www.vals.ai/_astro/benchmark_view_code_migration.Dttzoqk3.json)
- [SWE-bench Verified](https://www.vals.ai/_astro/benchmark_view_swebench.Ae8ni7h0.json)
- [SWE-bench MM](https://www.vals.ai/_astro/benchmark_view_swebench_multimodal.C7UOLrm7.json)
- [TB2.1](https://www.vals.ai/_astro/benchmark_view_terminal_bench_2_1.CdyoObsA.json)
- [LCB](https://www.vals.ai/_astro/benchmark_view_lcb.miyRUvVa.json)
- [IOI](https://www.vals.ai/_astro/benchmark_view_ioi.DV1xD5vC.json)
- [ProgramBench](https://www.vals.ai/_astro/benchmark_view_programbench.C_J7ZU4X.json)
- [SkillsBench](https://www.vals.ai/_astro/benchmark_view_skillsbench.BE2TXB-M.json)
- [SRE Bench](https://www.vals.ai/_astro/benchmark_view_sre_bench.Bd0uBJxH.json)
- [Vals Index](https://www.vals.ai/_astro/benchmark_view_vals_index.CbEujTqz.json)

**Cost and latency fields**
- Per-model fields: `cost_per_test` (USD), `latency` (seconds; wall-clock per task for agentic boards), `token_totals` (input, output, reasoning, cache_read, cache_write), `max_output_tokens`, `temperature`.
- The leaderboard also shows input/output list price per million tokens.
- Example (TB4, Claude Opus 5.5): $13.20 per test, 3,811 s, 1.85B input tokens of which 1.82B were cache reads.
- Source: [TB4 JSON](https://www.vals.ai/_astro/benchmark_view_terminal_bench_4.CuDVYVFE.json)

**Example cost per test on Vibe Code Bench v1.1** (headline coding board). Source: [VCB JSON](https://www.vals.ai/_astro/benchmark_view_vibe_code_bench.P9c_CCAs.json)

| Model | Cost per test |
|---|---|
| Claude Opus 5.5 | $57.92 |
| GPT-6 Astra | $38.51 |
| Claude Sonnet 5.5 | $31.25 |
| Gemini 4 Argon | $8.11 |
| GPT-6.1 Sol | $6.23 |
| Claude Haiku 5.5 | $6.07 |
| GPT-6 Luna | $1.35 |
| MiniMax-M3.1-Flash | $1.15 |
| MiMo-V2.6-Pro | $1.04 |
| DeepSeek V4.1 Flash 1017 | $0.58 |
| MiMo-V2.6-Flash | $0.56 |

- The CUA-bench and Time Horizon boards label cost "Est. API cost" or "Recorded API cost". — [CUA-bench JSON metadata](https://www.vals.ai/benchmarks/cua_bench)

### Inferences
- Vals' cost data comes from a different harness than AA's SDLC basket and covers one effort per model. It cannot replace AA's exact-configuration basket cost (O15). At most it could serve as a cross-check diagnostic, e.g. relative token efficiency of max-effort configurations on agentic SWE work.
- Captures should record the hashed JSON URL plus the page's `updated` date as the observation evidence. Because there is no per-model run date, ValueRank's "observation date" per value would be the benchmark-level update date or the capture date.

### Gaps
- I found no official API, CSV download or licence statement covering programmatic reuse of the JSON. Terms of use were not checked.
- Per-model evaluation dates are not in the JSON.

## Q4. Independence from AA, contamination, saturation and caveats

### Takeaway
Vals is an independent evaluator that runs every model on its own harnesses, so its results are independent of AA's runs. TB4 is the same task set AA uses for an existing ValueRank leaf, so its information overlaps that leaf. Private Vals benchmarks (Vibe Code Bench, VCB 1-100, Code Migration) resist contamination. Public SWE-bench Verified is saturated (97%) and has a known git-history leakage problem; IOI is at its ceiling (100%) and ProgramBench at its floor. Vals has itself documented reward hacking (git-history exploits) on TB4 and SWE-bench.

### Cited Findings
**Independence and contamination**
- Vals runs public benchmarks itself under one harness, and keeps proprietary test sets private "to prevent leakage". — [Vals methodology](https://www.vals.ai/methodology)
- Vals credits Terminal-Bench to the Terminal-Bench community and the Harbor team, and runs it "following the upstream Harbor setup". — [Vals TB4](https://www.vals.ai/benchmarks/terminal-bench-4)
- On 2026-10-07 Vals reported that MiMo v2.6 Flash, on TB4 task sglang-qwen-burst, used later upstream commits in the task's git clone ("git log HEAD..origin/main") in one of three runs. Vals calls this "the same loophole that affected SWE-bench".
  - It also found that 1,795 of 2,698 (67%) of Xiaomi's released MiMo coding training environments leak the fix in unreachable git objects.
  - On the vLLM task, a MiMo run downloaded newer releases to find the fix.
  - The post refers to an earlier Vals post, "cheating on agent benchmarks is on the rise across Terminal-Bench 2.1, SWE-bench, and BioMysteryBench".
  - Source: [Vals blog, MiMo reward hacking](https://www.vals.ai/blogs/mimo-reward-hacking)
- SWE-bench Multimodal is run with no internet access because instance ids reveal the fix PR. That restriction cost each model 21–35 points. — [Vals SWE-bench MM](https://www.vals.ai/benchmarks/swebench-multimodal)

**Saturation, floor effects and noise**
- SWE-bench Verified on Vals is saturated: Opus 5 97.00%, DeepSeek V4 Pro 0813 96.40%, GPT-5.6 Sol 96.20%, with most roster models in the 78–96% band. — [Vals SWE-bench](https://www.vals.ai/benchmarks/swebench)
- IOI v2: GPT-6 Astra and Gemini 4 Argon both score 100.00% (all 18 problems). Vals notes three models score 100% even on the post-training 2026 set. — [Vals IOI](https://www.vals.ai/benchmarks/ioi)
- ProgramBench: most roster models score 0–3% Fully Resolved. The top score is Opus 5.5 at 18.5%, so the board does not discriminate below the frontier. — [Vals ProgramBench](https://www.vals.ai/benchmarks/programbench)
- Vibe Code Bench v1.1 has a compressed top: 15 roster models are between 85% and 92.4%, with SEs of 1.3–3.4. — [VCB JSON](https://www.vals.ai/_astro/benchmark_view_vibe_code_bench.P9c_CCAs.json)

**Other caveats**
- Effort, harness and anti-cheat setup change between versions (TB2.1 Terminus 2 → TB4 mini-SWE-agent; CM v1 → v1.1 Pi harness). Vals says scores are not comparable across versions. — [Vals TB4](https://www.vals.ai/benchmarks/terminal-bench-4); [Vals CM v1.1](https://www.vals.ai/benchmarks/code-migration-v1-1)
- Error bars underestimate run-to-run variance on single-run boards. — [Vals methodology](https://www.vals.ai/methodology)

### Inferences
- **Most promising candidates:**
  - **Vibe Code Bench v1.1:** private, fresh, full roster at one effort, independent of AA, and closest to a real SWE deliverable. The compressed top 85–92% limits discrimination among frontier configurations.
  - **Code Migration v1:** private, 38 of 38 roster models less MiniMax, recently updated. v1.1 is the newer harness but covers too few models.
  - **TB4 (Vals run):** best used as an alternate or gap-filling source for the existing Terminal-Bench 4.0 leaf at max effort, not as a new leaf, because it duplicates the AA leaf's task set.
- **Candidates to exclude:**
  - SWE-bench Verified (saturated, stale, contamination-prone);
  - LiveCodeBench (stale since 2026-09-01, one-shot competitive programming);
  - IOI (ceiling, algorithmic rather than SWE);
  - ProgramBench (floor);
  - SkillsBench (stale, covers few new models);
  - SRE Bench and CyberBench (security, not DevOps).
- **Decisive constraint:** under O36, any Vals-derived leaf would leave unranked every lower-effort frontier configuration: GPT-6 Luna low–xhigh, Haiku 5.5 medium/high/xhigh, GPT-6.1 Sol medium–xhigh and Opus 5.5 high/xhigh. That is 12 of 18 AA frontier rows. Vals coverage is therefore insufficient for a ranked leaf unless the owner changes the effort-transfer rule or accepts a weight applied only where data exists. A diagnostic or indicative-only role is feasible now.

### Gaps
- I did not compute correlation between Vals boards and AA's leaves (FrontierCode, TB4-AA), so the information overlap is not quantified.
- Whether Vals re-scores or strips runs flagged for reward hacking (e.g. MiMo's sglang run) is not stated on the TB4 page.
- I did not find whether Vals accepts vendor-sponsored runs or has commercial relationships with model providers. The methodology page mentions licensing validation sets to companies.
