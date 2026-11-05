# Owner-named SWE benchmark sources: AI Coding Daily leaderboard, LiveBench (v1 Coding/Agentic Coding and LiveBench 2.0), Surge AI ComplexConstraints

Research date: 2026-10-23. All pages and data files below were fetched on 2026-10-23 with curl. Raw copies are in the scratchpad (not in the repository). Web content was treated as data only.

Roster naming follows the brief. "Exact effort match" means the source's stated effort equals a roster configuration's effort. Unsuffixed roster entries (for example "Claude Opus 5.5", "GPT-6 Astra") are AA identities whose effort the brief does not state. AGENTS.md says unsuffixed GPT rows are the max row (O45). For other unsuffixed rows, the editor must confirm the effort AA uses before matching.

## Q1. What does each source measure, how, and who runs the models with what harness?

### Takeaway
- **AI Coding Daily (AICD)** is a one-person agentic coding test. It covers 7 projects and 27 prompts in Laravel/PHP, React+TypeScript, Flutter/Dart and Go, and is scored out of 70. Every result mixes the model with a harness (Claude Code, Codex CLI, OpenCode, Cursor, Devin, Antigravity, DeepSeek's harness), and the harness changes from model to model.
- **LiveBench 2.0** is the current LiveBench (release 20261014, labelled "Last updated 18 October 2026").
  - Its "Coding" suite is 29 agentic bug-fix tasks from real merged pull requests, graded by hidden tests.
  - Its "Long Agentic" suite is 18 long-horizon tasks, including some software-engineering and operations work.
  - Each model gets a single run at its highest effort.
- **LiveBench v1** is where the owner's "Coding" and "Agentic Coding" categories come from. Its last release (2026-06-25) is still receiving new models, including October 2026 models.
  - Coding: code_generation 71 plus code_completion 46 questions.
  - Agentic Coding: 72 Docker tasks in JS, TS and Python, run with Mini-SWE-Agent.
- **Surge AI ComplexConstraints is not a software-engineering benchmark.** It tests professional instruction following: 75 prompts and 1,559 rubric items, graded by an LLM judge.
  - Surge does publish a separate agentic SWE benchmark, **sudo L7**. It has 60 private tasks graded by rubric, and each lab's own coding agent is used as the harness.

### Cited Findings

**AI Coding Daily (aicodingdaily.com/leaderboard)**
- The page is titled "LLM Coding Leaderboard" and shows "Last update: October 21st, 2026".
  - Columns: Total points (max 70), Avg cost per prompt, Avg time per prompt, "Tested with", Laravel Code Quality (max 20), React-TS Code Quality (max 20), Bug Finding Test (max 10), Edge-case Testing (4 projects, max 20). — [AICD leaderboard](https://aicodingdaily.com/leaderboard)
- The methodology article is dated August 21, 2026: "Each model receives 7 projects to be tested, with a total of 27 prompts."
  - The projects cover Laravel/PHP, React + TypeScript, Flutter/Dart and Go, and each starts from existing code.
  - "One coding agent (Claude Code, Codex CLI, OpenCode, Cursor…) gets one prompt and a repository, and does the work itself… no subagent swarms… no human feedback."
  - "The median task takes 4–11 minutes."
  - "No retries or coaching. Every prompt starts in a fresh copy of the project, and the model never sees the hidden tests or the scoring rubric."
  - — [AICD methodology](https://aicodingdaily.com/article/llm-coding-leaderboard-my-methodology-and-scoring-formulas)
- The methodology article's tables are embedded as PNG images (read on 2026-10-23). They give:
  - **The 7 projects:**
    1. CSV Import (PHP/Laravel)
    2. Offline Sync (PHP/Laravel)
    3. Bank Feed (Dart/Flutter)
    4. Shipping Quotes (Go)
    5. Equipment Library (PHP/Laravel, "judged on code quality")
    6. Support Inbox (React+TypeScript, "judged on code quality")
    7. Bug Hunt (PHP/Laravel: "report its real bugs, without changing a line")
  - **Scoring table:**

    | Column | Project(s) | Runs per prompt | Max points | Scored by |
    |---|---|---|---|---|
    | Laravel Code Quality | Equipment Library | 3 | 20 | "Judge model with a 100-point rubric" |
    | React-TS Code Quality | Support Inbox | 3 | 20 | Judge model with a 100-point rubric plus hidden tests |
    | Bug Finding Test | Bug Hunt | 1 | 10 | "Bugs matched against a private answer key, minus false claims" |
    | Edge-case Testing | CSV Import, Offline Sync, Bank Feed, Shipping Quotes | 4×5=20 | 20 | "Hidden automated tests" |
    | Total | 7 projects | 27 | 70 | |

  - **Median per-prompt figures:** duration ranges from 4.2 min (Offline Sync) to 10.7 min (Bug Hunt); tool calls range from 10 (Bank Feed) to 78 (Equipment Library). These are medians "across 2,076 runs of all tested models since August 2026".
  - — [AICD methodology images](https://aicodingdaily.com/article/llm-coding-leaderboard-my-methodology-and-scoring-formulas)
- The harness varies by model. The "Tested with" column shows Claude Code (Anthropic models), Codex CLI (OpenAI), OpenCode (most open-weight models), Cursor (Grok 4.6/4.7, Composer), Devin (Gemini 4 Argon, SWE-2), Antigravity (Gemini 3.8 Flash) and "DeepSeek Harness". — [AICD leaderboard](https://aicodingdaily.com/leaderboard)
- The effort-comparison page says: "Each score measures a model-and-harness configuration, not the model in isolation. Prices are calculated with API costs. Models tested on a subscription plan show N/A." — [AICD effort levels](https://aicodingdaily.com/compare/effort-levels)
- The judge model used for the two code-quality columns is not named anywhere in the article text or images I read. — [AICD methodology](https://aicodingdaily.com/article/llm-coding-leaderboard-my-methodology-and-scoring-formulas)
- The scoring has changed over time. The changelog on the leaderboard page records:
  - "July 27th: new v2 version of the leaderboard - with only two (but more complex) projects"
  - "August 31st: New project evaluating CODE QUALITY (max 20 points)"
  - "September 8th: … re-calculate scoring on Code Quality project"
  - "September 12th: Added new project React/Typescript code quality (20 points max)"
  - "October 3rd: Added new project worth 10 points for finding bugs"
  - — [AICD leaderboard](https://aicodingdaily.com/leaderboard)

**LiveBench 2.0 (livebench.ai/#/, release 20261014)**
- The site's JS bundle lists one v2 release, `_e=["20261014"]`, with display constant "18 October 2026". The page renders it as "Last updated 18 October 2026 — the latest release." Eleven v1 releases from 2024-06-24 to 2026-06-25 are kept as history. — [LiveBench bundle main.074b2ee8.js](https://livebench.ai/static/js/main.074b2ee8.js)
- Methodology text in the bundle:
  - "The board has seven suites. Five are agentic: the model works through real end-to-end tasks with tools (plans, edits files, drives apps, runs code)… The other two, Data Analysis and Reasoning, are short sets of single-answer questions."
  - "Each suite is one run per model."
  - "Models run at their highest supported effort setting. Where a different setting was used, the model's expanded row shows it."
  - "A task the run could not measure — it hit a harness or provider fault, and again on its one rerun — scores 0."
  - — [LiveBench methodology (#/methodology, from bundle)](https://livebench.ai/#/methodology)
- **Coding suite.** "Fix a real bug in a large production codebase, frozen at a fixed snapshot. Each task is a bug that a real merged pull request fixed. The model gets a bug report and the repository, and must make the fix… Hidden tests check the fix; a fix that breaks existing behaviour scores 0."
  - The subcategories are LLM API Integration (4), Agent Loop (5), Billing & Limits (4), Cloud Infrastructure (6), Product & UX (6) and Memory & Tools (4), for **29 tasks** in total.
  - — [LiveBench breakdown.json](https://livebench.ai/data/20261014/breakdown.json); [cost.csv nq_coding=29](https://livebench.ai/data/20261014/cost.csv)
- **Long Agentic suite.** "Long-running work where early decisions have to hold up through later turns, months or test cases."
  - The subcategories are Finance & Compliance Apps (4), Operations & Commerce Apps (4), Long-Run Operations (3; "Run an existing codebase through simulated months of data releases, billing closes and change tickets"), Systems Engineering (3; "Build a compiler from a written specification, repair a numerical physics simulator, and keep a service fleet healthy through a stream of incidents") and Performance Optimisation (4). That is **18 tasks**.
  - Grading is "by scripts against hidden reference data, hidden test programs or simulated outcomes."
  - — [LiveBench breakdown.json](https://livebench.ai/data/20261014/breakdown.json); [LiveBench bundle](https://livebench.ai/static/js/main.074b2ee8.js)
- notes.json describes Coding as "bug-fix tasks taken from real merged pull requests on a frozen codebase. Deterministic grading; a fix that breaks existing behaviour scores 0." The Agentic suite is "long-running work… Deterministic grading." — [LiveBench notes.json](https://livebench.ai/data/20261014/notes.json)
- **Cost.** Cost counts "every call the model under test made in the run, priced at the provider's list rates… It leaves out… the harness's own helper calls." — [LiveBench bundle](https://livebench.ai/static/js/main.074b2ee8.js)
- **The v2 agent harness/scaffold is not named** in the bundle, notes or data files. The phrase "the harness's own helper calls" implies a single LiveBench-run harness, but the name is not given. — [LiveBench bundle](https://livebench.ai/static/js/main.074b2ee8.js)

**LiveBench v1 (Coding and Agentic Coding categories)**
- The 2026-06-25 v1 categories file maps "Coding" to code_generation and code_completion, and "Agentic Coding" to javascript, typescript and python. — [categories_2026_06_25.json](https://livebench.ai/v1/categories_2026_06_25.json)
- Task counts from the v1 cost file: code_generation 71, code_completion 46, javascript 22, python 20, typescript 30 (72 agentic coding tasks). — [cost_2026_06_25.csv](https://livebench.ai/v1/cost_2026_06_25.csv)
- **Agentic Coding introduction (2025-05-30).** Models "operate in a multi-turn, realistic development environment to resolve issues from real Github repositories… Python, JavaScript, and TypeScript… Inference is performed using the SWE-Agent framework, and evaluation uses the Multi-SWE-Bench harness." — [LiveBench changelog](https://github.com/LiveBench/LiveBench/blob/main/changelog.md)
- **Harness change (2025-10-03).** The changelog says: "Switched the agent used for agentic coding to Mini-SWE-Agent… consistent interface with all models… updated the step limit to 250 rather than 50. The agentic coding tasks were rerun for all models." The harness is therefore the same for every model. — [LiveBench changelog](https://github.com/LiveBench/LiveBench/blob/main/changelog.md)
- The README says each question "has verifiable, objective ground-truth answers… without the use of an LLM judge," and that agentic coding needs task-specific Docker images (up to 150GB). — [LiveBench README](https://github.com/LiveBench/LiveBench/blob/main/README.md)

**Surge AI ComplexConstraints (surgehq.ai/benchmarks/complex-constraints)**
- The page categorises it under "Instruction Following": "A benchmark for professional instruction following, where constraints depend on each other, fire conditionally, and must be inferred from context." — [Surge ComplexConstraints](https://surgehq.ai/benchmarks/complex-constraints)
- The blog (dated June 3, 2026, updated October 21, 2026) describes the benchmark:
  - "75 expert-crafted prompts with 1,559 evaluation rubrics." Prompts come from "line producers, restaurant managers, teachers, business administrators" (for example film-shoot crisis memos, restaurant staff scheduling and office procurement).
  - "Each prompt has 15-40 rubric items, graded by an LLM judge."
  - None of the examples are coding tasks.
  - — [Surge blog](https://surgehq.ai/blog/complexconstraints-a-benchmark-for-entangled-instruction-following)
- The arXiv paper is "ComplexConstraints and Beyond: Expert Rubrics for RLVR", submitted 8 Jun 2026. It describes "a public 75-prompt benchmark with 1,559 rubric criteria and a disjoint 1,000-prompt training set, with 10-40 atomic criteria per prompt" and discusses "LLM-judge calibration". — [arXiv 2606.09118](https://arxiv.org/abs/2606.09118)
- **The judge model is not named** on the leaderboard page or in the blog. The arXiv abstract mentions calibration but does not name the judge. — [Surge blog](https://surgehq.ai/blog/complexconstraints-a-benchmark-for-entangled-instruction-following); [arXiv 2606.09118](https://arxiv.org/abs/2606.09118)

**Surge AI sudo L7 (related agentic-coding benchmark, same site; not owner-named but directly relevant)**
- "Across 60 tasks, agents must navigate unfamiliar systems, choose architectures, spot hidden risks, and know when technically correct code is still the wrong thing to ship." — [Surge sudo L7](https://surgehq.ai/benchmarks/sudo-l7)
- **Tasks.** "60 tasks authored by professional software engineers… primarily grounded in private production repositories from real companies, alongside open-source projects." Codebases are in Python, TypeScript, JavaScript, Ruby and others.
- **Grading.** "Expert-authored rubrics across eight dimensions"; "Grader models assess the agent's work against those criteria, using unit tests, static analysis, and other executable checks as evidence."
- **Selection bias.** "Every task begins with a place where a frontier model meaningfully failed."
- — [Surge sudo L7 blog (Oct 8, updated Oct 21, 2026)](https://surgehq.ai/blog/sudo-l7)
- The harness varies per model. The leaderboard labels each entry with its agent: [Claude Code], [Codex], [Qwen Code], [Antigravity], [Grok Build], [Muse Code], [OpenCode]. — [Surge sudo L7](https://surgehq.ai/benchmarks/sudo-l7)

### Inferences
- AICD is genuine SWE work: agentic, existing codebases, multiple languages, hidden tests plus an LLM-judged code-quality rubric. But it is very small. Bug Finding is a single run, and each prompt has 1 to 5 runs.
- Because AICD always pairs a model with a harness, a lab-native harness (Claude Code, Codex CLI) is compared against third-party ones (OpenCode, Cursor, Devin). This confounds model quality with harness quality.
  - DeepSeek V4.1 Flash 1017 (Max) has two rows: 61.2 with DeepSeek's harness and 60.97 with OpenCode. That suggests harness effects of at least about 0.2 points even in a near-identical case.
- LiveBench v1 Agentic Coding is the most standardised of the three: one harness for all models, deterministic multi-SWE-bench grading, and 72 tasks.
- The LiveBench 2.0 Coding suite is also deterministic and agentic, but has only 29 tasks from a single run. One task is worth about 3.4 points.
- ComplexConstraints does not measure software engineering. Using it as a SWE leaf would mislabel the evidence. If the owner wants it, it fits a general-professional-work or instruction-following role, not the 60% SWE block.

### Gaps
- AICD judge-model identity, rubric content and inter-run variance are not published.
- AICD's third methodology image ("Starting point → prompt → expected result") was not transcribed.
- I did not establish whether AICD re-runs every model after a scoring change. Many rows show test dates of 1–2 October 2026, just before the 3 October Bug-Hunt addition; why is not explained.
- The LiveBench 2.0 agent harness, step limits and sandbox are not documented in any file I found. The public GitHub changelog stops at 2026-01-08 and has no LiveBench 2.0 entry.
- The ComplexConstraints judge model and its decoding/settings are not given on the page or in the blog. I did not read the full arXiv PDF.
- The size of the sudo L7 rubric and how scores aggregate into a percentage are not published beyond "eight dimensions".

## Q2. Does each result name the exact model version and reasoning effort? Which roster configurations are covered, with values?

### Takeaway
- **AICD** names a version and an explicit effort on every row. It covers about 22 roster families, but usually at Low, Medium, High or Max as tested in the author's chosen harness. Those often differ from the roster's efforts, and there is no max/xhigh for GPT-6.1 Sol, Opus 5.5 or Sonnet 5.5.
  - It has nothing for MiMo-V2.6-Flash at any effort other than High, nothing for Haiku 5.5 low/max, and no current rows for GPT-5.6 Luna, GPT-6 Sol, Opus 5, Sonnet 5 or DeepSeek V4 Flash (these are hidden).
- **LiveBench 2.0** gives one row per model, at the highest effort (or a stated alternative). It covers about 30 roster families but only one effort each, and misses MiMo-V2.6-Flash.
- **LiveBench v1** adds a second effort for a few frontier models (max and xhigh for GPT-6.1 Sol, Opus 5.5, Sonnet 5.5 and Haiku 5.5).
- **ComplexConstraints** labels each model with an effort but omits most frontier configurations: GPT-6.1 Sol, GPT-6 Luna, Haiku 5.5, Sonnet 5.5, both MiMo models, MiniMax-M3.1-Flash and GPT-5.6 Luna.
- **No owner-named source covers the 51-configuration cohort at exact efforts.**

### Cited Findings

**AICD: every row on 2026-10-23, with test date (from the row's date attribute), harness, and Total (max 70).**

Source for all rows: [AICD leaderboard](https://aicodingdaily.com/leaderboard) (effort pages cross-checked against [AICD effort levels](https://aicodingdaily.com/compare/effort-levels)).

| Model (AICD label) | Effort | Total /70 | Date tested | Harness | Laravel Code Quality /20 | React-TS Code Quality /20 | Bug Finding /10 | Edge-case Testing /20 |
|---|---|---|---|---|---|---|---|---|
| Opus 5.5 | High | 67.26 | 2026-10-20 | Claude Code | 18.68 | 19 | 9.58 | 20 |
| Opus 5.5 | Medium | 65.28 | 2026-10-19 | Claude Code | | | | |
| Opus 5.5 | Low | 60.5 | 2026-10-19 | Claude Code | | | | |
| GPT-6-Astra | High | 66.35 | 2026-10-01 | Codex CLI | | | | |
| GPT-6-Astra | Medium | 66.03 | 2026-09-30 | Codex CLI | | | | |
| GPT-6.1-Sol | High | 66 | 2026-10-19 | Codex CLI | | | | |
| GPT-6.1-Sol | Medium | 65.05 | 2026-10-19 | Codex CLI | | | | |
| GPT-6.1-Sol | Low | 61.45 | 2026-10-19 | Codex CLI | | | | |
| Sonnet 5.5 | High | 64.31 | 2026-09-30 | Claude Code | | | | |
| Sonnet 5.5 | Medium | 60.54 | 2026-09-29 | Claude Code | | | | |
| Deepseek-V4.1-Flash-1017 | Max | 61.2 | 2026-10-18 | DeepSeek Harness | | | | |
| Deepseek-V4.1-Flash-1017 | Max | 60.97 | 2026-10-17 | OpenCode | | | | |
| Deepseek-V4.1-Flash-1017 | High | 55.21 | 2026-10-17 | OpenCode | | | | |
| Fable 5.1 | Medium | 61.03 | 2026-10-02 | Claude Code | | | | |
| Grok 4.7 | High | 60.09 | 2026-10-01 | Cursor | | | | |
| GPT-6-Luna | Max | 59.07 | 2026-10-01 | Codex CLI | | | | |
| GPT-6-Luna | Xhigh | 56.4 | 2026-10-01 | Codex CLI | | | | |
| GPT-6-Luna | High | 53.04 | 2026-10-01 | Codex CLI | | | | |
| GPT-6-Luna | Medium | 43.74 | 2026-09-30 | Codex CLI | | | | |
| Haiku 5.5 | High | 58.63 | 2026-10-08 | Claude Code | | | | |
| Haiku 5.5 | Medium | 58.2 | 2026-10-08 | Claude Code | | | | |
| Gemini 4 Argon | High | 57.09 | 2026-10-14 | Devin (subscription; cost N/A) | | | | |
| Kimi K3 | High | 56.89 | 2026-09-29 | OpenCode | | | | |
| Grok 4.6 | High | 56.71 | 2026-09-30 | Cursor | | | | |
| GLM-5.3 | High | 54.82 | 2026-10-01 | OpenCode | | | | |
| MiniMax M3.1-Flash | Max | 54.48 | 2026-10-20 | OpenCode (cost N/A) | | | | |
| MiMo-V2.6 Pro | High | 53.81 | 2026-10-02 | OpenCode | | | | |
| MiMo-V2.6 Flash | High | 53.29 | 2026-10-02 | OpenCode | | | | |
| Qwen 3.8 Max (0902) | High | 53.39 | 2026-10-01 | OpenCode | | | | |
| Muse Spark 1.3 | Max | 53.01 | 2026-10-01 | OpenCode | | | | |
| Deepseek-V4-Pro-0813 | Max | 50.35 | 2026-10-01 | OpenCode | | | | |
| Deepseek-V4-Pro-0813 | High | 48.34 | 2026-10-01 | OpenCode | | | | |
| GLM-5.3-Flash | Max | 47.51 | 2026-10-02 | OpenCode | | | | |
| Gemini-3.8-Flash | High | 47.09 | 2026-10-02 | Antigravity (cost N/A) | | | | |

Per-column sub-scores were captured only for the first row; the rest are in the page table.

- The leaderboard also has non-roster rows, including SWE-2 57.07, Mistral Large 4 56.86, Qwen 3.8 Flash, Tencent Hy3, Gemini-3.1-Pro, Mercury 3, Composer 2.5 and Nemotron. — [AICD leaderboard](https://aicodingdaily.com/leaderboard)
- **Hidden rows.** These models are "hidden from table" as older LLMs: Deepseek-V4-Flash, GPT-5.6-Luna, GPT-5.6-Sol, GPT-5.6-Terra, GPT-6-Sol, Kimi K2.7 Code, Opus 5, Sonnet 5. The page's Livewire state lists hidden IDs [17, 18, 23, 26, 27, 31, 32, 57]. Their values are not in the served HTML and need the UI toggle. — [AICD leaderboard](https://aicodingdaily.com/leaderboard)
- **Removed models.** The changelog records "July 26th: cleanup - removed older models: GPT-5.5, Kimi K2.6, Gemini 3.5 Flash, Sonnet 4.6". Gemini 3.7 Flash ("August 18th: Added Gemini-3.7-Flash tested in Antigravity"), Gemini 3.6 Flash, GLM-5.2, Opus 4.8 and Muse Spark 1.2 were added earlier but are not in the current table. — [AICD leaderboard](https://aicodingdaily.com/leaderboard)
- **AICD roster gaps:**
  - No row at all: Muse Wonder, Muse Wonder Full, Claude Fable 5, Gemini 3.5 Flash, Gemini 3.6 Flash, Gemini 3.7 Flash, GLM-5.2, Opus 4.8, Muse Spark 1.2, GPT-5.5.
  - Missing efforts: GPT-6.1 Sol max/xhigh; Haiku 5.5 max/low/default; Sonnet 5.5 max/xhigh/low; Muse Spark 1.3 xhigh; Grok 4.6 xhigh.
  - Hidden only: GPT-5.6 Luna, GPT-5.6 Sol, GPT-6 Sol, Opus 5, Sonnet 5, DeepSeek V4 Flash.

**LiveBench 2.0 (release 20261014): Coding (29 tasks) and Long Agentic (18 tasks), effort from the bundle's model metadata, one run each.**

Sources: [table.csv](https://livebench.ai/data/20261014/table.csv); [bundle model metadata](https://livebench.ai/static/js/main.074b2ee8.js)

| Model | Effort | Coding | Long Agentic |
|---|---|---|---|
| claude-opus-5.5 | max | 96.3 | 85.0 |
| claude-sonnet-5.5 | max | 94.7 | 78.8 |
| claude-haiku-5.5 | max | 91.4 | 57.6 |
| claude-fable-5.1 | max | 97.7 | 80.8 |
| claude-fable-5 | max | 98.3 | 53.2 |
| claude-opus-5 | max | 90.8 | 62.1 |
| claude-opus-4.8 | max | 77.3 | 48.3 |
| claude-sonnet-5 | max | 74.7 | 39.0 |
| gpt-6.1-sol | max | 96.0 | 73.0 |
| gpt-6-astra | max | 93.7 | 82.4 |
| gpt-6-sol | max | 93.1 | 66.9 |
| gpt-6-luna | max | 84.5 | 48.1 |
| gpt-5.6-sol | max | 89.7 | 48.5 |
| gpt-5.6-luna | max | 73.6 | 30.4 |
| gpt-5.5 | xhigh | 85.1 | 44.6 |
| gemini-4-argon | high | 89.7 | 69.9 |
| gemini-3.8-flash | high | 82.2 | 30.1 |
| gemini-3.7-flash | high | 80.5 | 28.3 |
| mimo-v2.6-pro | high | 81.5 | 47.5 |
| deepseek-v4.1-flash-1017 | max, version "1017" | 96.0 | 50.9 |
| minimax-m3.1-flash | max | 83.9 | 34.7 |
| glm-5.3 | max | 82.8 | 35.9 |
| glm-5.3-flash | max | 80.6 | 28.4 |
| grok-4.7 | xhigh | 84.5 | 50.1 |
| grok-4.6 | xhigh | 89.1 | 40.7 |
| kimi-k3 | max | 59.3 | 42.8 |
| qwen3.8-max | max | 60.3 | 42.3 |
| muse-spark-1.3 | max | 90.2 | 40.4 |
| muse-spark-1.2 | xhigh | 78.2 | 21.3 |
| muse-wonder-1.0 | max | 86.2 | 53.2 |

- **LiveBench 2.0 roster gaps.** Absent: MiMo-V2.6-Flash, DeepSeek V4 Pro, DeepSeek V4 Flash, Gemini 3.6 Flash, Gemini 3.5 Flash, GLM-5.2 and Muse Wonder Full. Only one effort per model, so these are missing: GPT-6.1 Sol xhigh/high/medium/low; Haiku 5.5 high/medium/low/default; Sonnet 5.5 xhigh/high/medium/low; Muse Spark 1.3 xhigh; Grok 4.6 default (if it is not xhigh). — [table.csv](https://livebench.ai/data/20261014/table.csv)

**LiveBench v1 (release 2026-06-25, still receiving models).** Effort is in the model ID. Category values below are my unweighted means of the task columns.

Source: [table_2026_06_25.csv](https://livebench.ai/v1/table_2026_06_25.csv)

| Model ID | Coding | Agentic Coding |
|---|---|---|
| claude-opus-5-5-max-effort | 89.3 | 71.7 |
| claude-opus-5-5-xhigh-effort | 89.3 | 65.4 |
| claude-sonnet-5-5-max-effort | 91.4 | 56.3 |
| claude-sonnet-5-5-xhigh-effort | 88.9 | 39.3 |
| claude-haiku-5-5-max-effort | 77.9 | 57.2 |
| claude-haiku-5-5-xhigh-effort | 76.4 | 51.4 |
| gpt-6.1-sol-max | 80.4 | 54.5 |
| gpt-6.1-sol-xhigh | 80.7 | 56.8 |
| gpt-6-astra-max | 80.4 | 57.3 |
| gpt-6-sol-max | 81.8 | 52.9 |
| gpt-6-luna-max | 79.0 | 51.2 |
| claude-fable-5-1-max-effort | 86.4 | 66.1 |
| claude-fable-5-max-effort | 86.0 | 62.2 |
| claude-opus-5-max-effort | 81.4 | 65.2 |
| claude-opus-4-8-max-effort | 81.8 | 50.5 |
| claude-sonnet-5-xhigh-effort | 80.7 | 59.4 |
| gpt-5.6-sol-max | 83.9 | 56.2 |
| gpt-5.6-luna-max | 82.9 | 48.4 |
| gpt-5.5-xhigh | 82.1 | 54.0 |
| deepseek-v4.1-flash-max | 80.0 | 77.3 |
| deepseek-v4-pro-0813 | 77.2 | 54.9 |
| deepseek-v4-pro | 70.0 | 42.6 |
| deepseek-v4-flash | 69.2 | 37.6 |
| deepseek-v4-flash-0731 | 75.0 | 46.8 |
| gemini-3.8-flash-high | 72.5 | 54.2 |
| gemini-3.7-flash-high | 78.9 | 58.3 |
| gemini-3.6-flash-high | 77.9 | 43.4 |
| gemini-3.5-flash-high | 78.2 | 49.0 |
| glm-5.3 | 79.0 | 60.9 |
| glm-5.3-flash | 79.0 | 56.8 |
| glm-5.2 | 79.7 | 51.8 |
| grok-4.7-xhigh | 77.2 | 54.0 |
| grok-4.6 | 76.8 | 57.0 |
| kimi-k3 | 81.4 | 62.2 |
| qwen3.8-max | 72.9 | 64.6 |
| muse-spark-1.3-xhigh | 81.1 | 64.1 |
| muse-spark-1.2-xhigh | 77.5 | 57.6 |
| muse-wonder-1.0-max | 80.7 | 62.7 |

- Some per-task raw values, as a sample (code_completion, code_generation, javascript, python, typescript):
  - opus-5.5 max: 86.957, 91.549, 81.818, 70.0, 63.333
  - gpt-6.1-sol max: 80.435, 80.282, 63.636, 60.0, 40.0
  - — [table_2026_06_25.csv](https://livebench.ai/v1/table_2026_06_25.csv)
- **LiveBench v1 roster gaps.** Absent from v1: Gemini 4 Argon, MiMo-V2.6-Pro, MiMo-V2.6-Flash, MiniMax-M3.1-Flash and DeepSeek V4.1 Flash 1017 (only the September "deepseek-v4.1-flash-max", version 2026-09-10, is present). Non-max efforts (high/medium/low) are absent for every model. — [table_2026_06_25.csv](https://livebench.ai/v1/table_2026_06_25.csv)

**Surge ComplexConstraints: every roster-relevant row (percent).**

Source: [Surge ComplexConstraints](https://surgehq.ai/benchmarks/complex-constraints)

| Model (Surge label) | Effort label | Score |
|---|---|---|
| GPT 6 Astra | Max reasoning | 57.7 |
| Gemini 4 Argon | High reasoning | 53.3 |
| Muse Spark 1.3 | xHigh reasoning | 51.9 |
| GPT 6 Sol | Max reasoning | 50.8 |
| GPT 5.6 Sol | Max reasoning | 50.5 |
| Claude Opus 5.5 | Adaptive/Max | 49.9 |
| DeepSeek V4.1 Flash | Max reasoning; snapshot not stated, so 1017 is unconfirmed | 49.7 |
| GPT 5.5 | xHigh reasoning | 49.5 |
| Grok 4.7 | xHigh reasoning | 48.9 |
| Gemini 3.8 Flash | High reasoning | 48.4 |
| Qwen 3.8 Max | xHigh reasoning | 45.5 |
| Claude Fable 5.1 | Adaptive/Max | 45.1 |
| Gemini 3.7 Flash | High reasoning | 42.4 |
| DeepSeek V4 Pro | Max reasoning | 42.0 |
| Gemini 3.6 Flash | High reasoning | 40.0 |
| Muse Spark 1.2 | xHigh reasoning | 39.9 |
| Claude Fable 5 | Max reasoning | 38.1 |
| Kimi K3 | Max reasoning | 37.9 |
| Claude Opus 5 | Adaptive/Max | 37.3 |
| Grok 4.6 | xHigh reasoning | 36.5 |
| Claude Opus 4.8 | Max reasoning | 35.6 |
| GLM 5.3 | Max reasoning | 30.5 |
| GLM 5.2 | Max reasoning | 29.3 |
| GLM 5.3 Flash | Max reasoning | 27.6 |

- The board has 45 rows in total. Every row's rank field renders as "1" in the served HTML, a Webflow CMS field value, so it is not a real rank. — [Surge ComplexConstraints](https://surgehq.ai/benchmarks/complex-constraints)
- **ComplexConstraints roster gaps.** Absent: GPT-6.1 Sol (all efforts), GPT-6 Luna, GPT-5.6 Luna, Claude Haiku 5.5, Claude Sonnet 5.5, Claude Sonnet 5, MiMo-V2.6-Pro, MiMo-V2.6-Flash, MiniMax-M3.1-Flash, DeepSeek V4 Flash, Gemini 3.5 Flash, Muse Wonder and Muse Wonder Full. — [Surge ComplexConstraints](https://surgehq.ai/benchmarks/complex-constraints)

**Surge sudo L7: all 15 rows, with harness.**

Source: [Surge sudo L7](https://surgehq.ai/benchmarks/sudo-l7)

| Model | Effort label | Harness | Score |
|---|---|---|---|
| Claude Opus 5.5 | Adaptive/Max | Claude Code | 41.7 |
| Claude Sonnet 5.5 | Adaptive/Max | Claude Code | 41.7 |
| GPT 6 Astra | Max | Codex | 33.9 |
| Claude Fable 5.1 | Adaptive/Max | Claude Code | 31.1 |
| GPT 6.1 Sol | Max | Codex | 28.9 |
| Qwen 3.8 Max | xHigh | Qwen Code | 20.6 |
| Gemini 4 Argon | High | Antigravity | 18.9 |
| Grok 4.7 | xHigh | Grok Build | 15.6 |
| Muse Wonder | Max | Muse Code | 15.6 |
| GLM 5.3 | Max | OpenCode | 14.4 |
| Muse Spark 1.3 | Max | Muse Code | 13.9 |
| Kimi K3 | Max | OpenCode | 13.3 |
| Hy Hy4 Preview | High | OpenCode | 12.8 |
| Gemini 3.8 Flash | High | Antigravity | 11.7 |
| Mistral Large 4 | High | OpenCode | 11.7 |

- The sudo L7 blog text gives different figures: "Opus 5.5 and Sonnet 5.5 lead at 45%, trailed by Astra at 32%" and "GPT-6.1 Sol… succeeds on 30% of assignments at just over $1 per task". The leaderboard shows 41.7 / 41.7 / 33.9 / 28.9. — [Surge sudo L7 blog](https://surgehq.ai/blog/sudo-l7); contradicted by [Surge sudo L7 leaderboard](https://surgehq.ai/benchmarks/sudo-l7)

### Inferences
- **The frontier models the brief prioritises are badly covered at exact efforts by every owner-named source:**
  - **Haiku 5.5:** low/medium/high/xhigh/max are only partly covered. AICD has medium and high; LiveBench v1 has xhigh and max; LiveBench 2.0 has max. These are different instruments, so the results cannot be pooled into one leaf without mixing instruments.
  - **GPT-6.1 Sol:** medium/high/xhigh/max are split the same way. AICD has low/medium/high; LiveBench v1 has max/xhigh; LiveBench 2.0 has max.
  - **MiMo-V2.6-Flash:** only AICD (High) has it.
- **LiveBench 2.0 has the broadest family coverage at a single effort** (about 30 of about 38 families). That fits a "max-effort only" leaf, but not ValueRank's per-effort cohort. Under O36, every non-max configuration (about 16 of the 51) would lack it.
- **AICD has the best multi-effort coverage** for OpenAI and Anthropic models. However, its efforts reflect the author's choices and lab harness settings, and there are no max/xhigh rows for GPT-6.1 Sol, Opus 5.5 or Sonnet 5.5.
- **Unsuffixed roster entries need an AA-effort check before any value is used.** AICD's GPT-6 Astra rows are High/Medium, not the max row bound by O45, and its Opus 5.5 rows are Low/Medium/High only.
- **ComplexConstraints and sudo L7 cover only about 23 and about 12 roster families respectively.** Both miss most cheap frontier configurations.

### Gaps
- Values for AICD's hidden rows (GPT-5.6 Luna, GPT-5.6 Sol, GPT-6 Sol, Opus 5, Sonnet 5, DeepSeek V4 Flash) could not be read from the served HTML. They need the page's "untick" control or a Livewire request.
- LiveBench 2.0 says alternate effort settings appear in an "expanded row". I found effort only in the bundle's per-model `effort` field, and no per-model note text, so the effort values above are taken from that field.
- For LiveBench v1 IDs without an effort suffix (grok-4.6, glm-5.3, kimi-k3, qwen3.8-max), the effort used is not stated in the ID.
- I did not verify whether LiveBench's v1 site computes category scores as the unweighted mean of task columns. The task-weighted Agentic Coding mean differs by about 1–2 points, for example opus-4.8 50.5 unweighted against 48.6 weighted.
- Surge's "DeepSeek V4.1 Flash (Max)" snapshot (original or 1017) is not stated.

## Q3. Last update date, cadence, and machine-readability

### Takeaway
- **AICD** was updated 2026-10-21. It changes several times a week (new models plus occasional re-benchmarks and scoring changes). It is server-rendered HTML through Livewire, with no JSON, CSV or API, although the table is scrapeable.
- **LiveBench** is fully machine-readable as static CSV/JSON. The v2 release is 20261014, labelled updated 18 Oct 2026, and the v1 2026-06-25 file has models added through mid-October.
- **Surge** pages are static Webflow CMS HTML, with no JSON found. The ComplexConstraints blog was updated 2026-10-21. A public dataset and GitHub repo exist, but the leaderboard scores are not published as data.

### Cited Findings

**AI Coding Daily**
- The page reads "Last update: October 21st, 2026". The changelog records near-daily additions, for example:
  - "October 21st: Added Mercury 3"
  - "October 20th: Added MiniMax-M3.1-Flash"
  - "October 20th: Re-benchmarked GPT-6.1-Sol and Opus 5.5"
  - "October 14th: Added Gemini 4 Argon"
  - — [AICD leaderboard](https://aicodingdaily.com/leaderboard)
- "New rankings go out in the weekly AI Coding Daily newsletter." Each row links to a YouTube video of the test, and rows carry an exact test date in a `title` attribute. — [AICD leaderboard](https://aicodingdaily.com/leaderboard)
- The leaderboard is a Laravel Livewire component. Its `wire:snapshot` state holds only UI state (sort settings and hidden model IDs), not the data; the table is in the HTML. — [AICD leaderboard](https://aicodingdaily.com/leaderboard)
- The effort-comparison page shows "Last update: October 20th, 2026". — [AICD effort levels](https://aicodingdaily.com/compare/effort-levels)

**LiveBench**
- The data endpoints are hard-coded in the bundle:
  - LiveBench 2.0: `./data/<release>/table.csv`, `categories.json`, `cost.csv`, `breakdown.json`, `notes.json`
  - v1: `./v1/table_<date>.csv`, `categories_<date>.json`, `cost_<date>.csv`
  - The page says: "Overall and everything derived from it are computed in the browser, never stored."
  - — [LiveBench bundle](https://livebench.ai/static/js/main.074b2ee8.js)
- The live v2 files (all HTTP 200 on 2026-10-23):
  - https://livebench.ai/data/20261014/table.csv
  - https://livebench.ai/data/20261014/categories.json
  - https://livebench.ai/data/20261014/cost.csv (per-suite cost, task counts and token counts)
  - https://livebench.ai/data/20261014/breakdown.json (subcategory scores)
  - https://livebench.ai/data/20261014/notes.json
  - — [LiveBench data](https://livebench.ai/data/20261014/table.csv)
- v1 files: https://livebench.ai/v1/table_2026_06_25.csv (per-task raw scores, 71 models), categories_2026_06_25.json and cost_2026_06_25.csv. — [LiveBench v1 table](https://livebench.ai/v1/table_2026_06_25.csv)
- Release display constant: "Last updated 18 October 2026 — the latest release." — [LiveBench bundle](https://livebench.ai/static/js/main.074b2ee8.js)
- The v1 2026-06-25 table includes models released well after June, such as claude-haiku-5-5, gpt-6.1-sol, mistral-large-4-high and muse-wonder-1.0-max. The v1 release date labels the question set, not when results were added. — [LiveBench v1 table](https://livebench.ai/v1/table_2026_06_25.csv)
- The public GitHub changelog's latest entry is 2026-01-08, and the README still says "The current LiveBench release is 2025-04-25". The repo documentation lags the site. — [LiveBench changelog](https://github.com/LiveBench/LiveBench/blob/main/changelog.md); [LiveBench README](https://github.com/LiveBench/LiveBench/blob/main/README.md)

**Surge**
- Leaderboard rows are Webflow CMS list items (`fs-list-element="list"`, `data-leaderboard-row`). I found no JSON data source. — [Surge ComplexConstraints](https://surgehq.ai/benchmarks/complex-constraints)
- The ComplexConstraints blog is dated "October 21, 2026 / June 3, 2026", which reads as updated and published dates. The sudo L7 blog is dated "October 21, 2026 / October 8, 2026". — [Surge blog](https://surgehq.ai/blog/complexconstraints-a-benchmark-for-entangled-instruction-following); [Surge sudo L7 blog](https://surgehq.ai/blog/sudo-l7)
- The page links to a GitHub repo (https://github.com/surge-ai/complex-constraints) and a Hugging Face dataset (https://huggingface.co/datasets/surgeai/ComplexConstraints). — [Surge ComplexConstraints](https://surgehq.ai/benchmarks/complex-constraints); [Surge blog](https://surgehq.ai/blog/complexconstraints-a-benchmark-for-entangled-instruction-following)

### Inferences
- **LiveBench is the easiest to capture reproducibly.** The release-pinned CSVs can be archived and hashed per refresh.
- **AICD can be captured by HTML scraping.** Its row dates and video links support provenance, but the scoring version changes (v2, +code quality, +bug finding) mean old captures are not comparable to new ones.
- **Surge capture would be HTML scraping of a CMS list** with no per-row dates.

### Gaps
- I could not confirm the GitHub repo metadata or contents for surge-ai/complex-constraints (GitHub API 403 through the proxy).
- The Hugging Face author listing for "surgeai" showed only the DAYJOB and GDP.xlsx datasets, not ComplexConstraints, so the dataset's current availability is unverified.
- I found no stated refresh cadence for LiveBench 2.0 or for the Surge leaderboards.

## Q4. Contamination resistance, saturation, methodological caveats, funding/operator, independence from AA

### Takeaway
- **All three sources are independent of Artificial Analysis.**
  - AICD is run by one educator (Povilas Korop) and funded by premium memberships.
  - LiveBench is sponsored by Abacus.AI.
  - Surge AI is a data vendor that sells training data and RL environments, including companion training sets for its own benchmarks.
- **Contamination resistance:**
  - AICD: strongest in practice (private repositories, hidden tests and rubric).
  - LiveBench 2.0: unclear.
  - ComplexConstraints: weak (public dataset plus a commercial training set).
  - sudo L7: good (mostly private repositories, access on request).
- **Saturation:** LiveBench 2.0 Coding is near-saturated at the top (five roster models at 96–98). AICD's top band is compressed (66–67 of 70, Edge-case 19.5–20 of 20). ComplexConstraints and sudo L7 are not saturated.

### Cited Findings

**AI Coding Daily**
- Operator and funding: "© 2026 AI Coding Daily by Povilas Korop"; "Running dozens of prompts on multiple projects with different LLMs is costly. Help keep it updated: get Premium membership." The site also sells advertising ("Advertise"). — [AICD leaderboard](https://aicodingdaily.com/leaderboard)
- Contamination controls: "the model never sees the hidden tests or the scoring rubric." The bug test uses "a private answer key". — [AICD methodology](https://aicodingdaily.com/article/llm-coding-leaderboard-my-methodology-and-scoring-formulas)
- Saturation at the top: Edge-case Testing is 20/20 for Opus 5.5 High and GPT-6-Astra High and Medium, and 19.5 for GPT-6.1-Sol High and Medium and for Opus 5.5 Medium. The top six totals span 65.05–67.26 of 70. — [AICD leaderboard](https://aicodingdaily.com/leaderboard)
- Cost caveat: subscription-tested rows show cost "N/A" (Gemini 4 Argon via Devin, MiniMax-M3.1-Flash, DeepSeek harness row, Gemini 3.8 Flash). — [AICD leaderboard](https://aicodingdaily.com/leaderboard)

**LiveBench**
- Operator: "LiveBench 2.0 · sponsored by Abacus.AI." The v1 footer reads "LiveBench v1 · sponsored by Abacus.AI · a contamination-free LLM benchmark." — [LiveBench bundle](https://livebench.ai/static/js/main.074b2ee8.js)
- v1 contamination design: "LiveBench is designed to limit potential contamination by releasing new questions monthly… Each question has verifiable, objective ground-truth answers… without the use of an LLM judge." — [LiveBench README](https://github.com/LiveBench/LiveBench/blob/main/README.md)
- The changelog entry for 2025-11-25 says that update "refreshed some existing tasks… to resolve (to some extent) saturation and contamination". — [LiveBench changelog](https://github.com/LiveBench/LiveBench/blob/main/changelog.md)
- The v2 title claims "A challenging, contamination-free long-horizon AI benchmark". However, the v2 Coding suite draws on "a bug that a real merged pull request fixed… frozen at a fixed snapshot", and its examples ("Stop a credit throttle double-counting usage… refuse shared storage buckets in a cloud connector") point to a public codebase. — [LiveBench bundle](https://livebench.ai/static/js/main.074b2ee8.js)
- Saturation: LiveBench 2.0 Coding top scores are Fable 5 98.3, Fable 5.1 97.7, Opus 5.5 96.3, GPT-6.1 Sol 96.0 and DeepSeek V4.1 Flash 1017 96.0. GPT-6.1 Sol scores 100.0 in four of six coding subcategories. — [table.csv](https://livebench.ai/data/20261014/table.csv); [breakdown.json](https://livebench.ai/data/20261014/breakdown.json)
- Noise: "Each suite is one run per model." A task the run could not measure, even after one rerun, "scores 0, the same as a failed task." — [LiveBench bundle](https://livebench.ai/static/js/main.074b2ee8.js)
- Cost scale per suite (USD, whole suite):

  | Model | Coding (29 tasks) | Long Agentic (18 tasks) |
  |---|---|---|
  | claude-opus-5.5 | $145.89 | $684.16 |
  | gemini-4-argon | $147.21 | $249.15 |
  | claude-haiku-5.5 | $25.34 | $186.51 |
  | gpt-6.1-sol | $13.98 | $116.78 |
  | gpt-6-luna | $2.76 | $17.42 |

  — [cost.csv](https://livebench.ai/data/20261014/cost.csv)
- Harness uniformity: since 2025-10-03, v1 Agentic Coding uses Mini-SWE-Agent for all models ("consistent interface with all models"). — [LiveBench changelog](https://github.com/LiveBench/LiveBench/blob/main/changelog.md)

**Surge AI**
- ComplexConstraints is public: "The full ComplexConstraints benchmark is on HuggingFace". Surge also built "a companion training set of 1,000 examples" and reports training a Qwen3-4B on it. — [Surge blog](https://surgehq.ai/blog/complexconstraints-a-benchmark-for-entangled-instruction-following)
- The paper describes "a public 75-prompt benchmark… and a disjoint 1,000-prompt training set". — [arXiv 2606.09118](https://arxiv.org/abs/2606.09118)
- Surge's business: "Frontier data and RL environments, off the shelf". Its blog reports post-training customers' models on Surge data, for example "We post-trained Kimi K2.7 on 1,700 Surge agentic coding tasks… +12.4pp on DeepSWE, and +7.6pp on Terminal-Bench 4", and "How Anthropic uses Surge AI to Train and Evaluate Claude". — [Surge blog index on ComplexConstraints post](https://surgehq.ai/blog/complexconstraints-a-benchmark-for-entangled-instruction-following)
- Saturation: the June blog said "Top models score under 40%". The October leaderboard top is 57.7% (GPT 6 Astra). — [Surge blog](https://surgehq.ai/blog/complexconstraints-a-benchmark-for-entangled-instruction-following); [Surge ComplexConstraints](https://surgehq.ai/benchmarks/complex-constraints)
- sudo L7 is private ("To learn more or request access to the benchmark set, reach out to benchmarks@surgehq.ai"). Its tasks are adversarially selected ("Every task begins with a place where a frontier model meaningfully failed") and LLM-graded ("Grader models assess the agent's work"). — [Surge sudo L7 blog](https://surgehq.ai/blog/sudo-l7)

### Inferences
- **Independence from AA is high for all three.** But each has its own conflict or fragility:
  - AICD: single author, judge-model grading, and harness choice confounded with model.
  - LiveBench: commercial sponsor (Abacus.AI). v2 is new, with an undocumented harness and single runs.
  - Surge: a vendor that sells training data to the labs it ranks, and LLM-judge grading.
- **On O36 coverage alone:**
  - No owner-named source can serve as a ranked leaf for the full 51-configuration cohort at exact efforts.
  - The closest is LiveBench 2.0 Long Agentic plus Coding, which covers about 34 configurations if each roster model's max/high row is treated as exact. It misses MiMo-V2.6-Flash and all non-max efforts.
  - AICD has the best per-effort coverage for OpenAI and Anthropic models, but no max/xhigh for the top Sol/Opus/Sonnet models, and its harness varies.
- **Candidate uses the editor could weigh**, with a caveat: per O36, any leaf without full coverage would exclude configurations from ranking.
  - LiveBench 2.0 Long Agentic or v1 Agentic Coding as a diagnostic or indicative leaf.
  - AICD as a diagnostic cross-check, because it is the only source with low/medium/high splits from a working practitioner.
  - ComplexConstraints only outside the SWE block, if at all.
- **Possible overlap with existing leaves.** AICD's "Bug Hunt" project is distinct from ValueRank's existing Bug Hunt Bench (phuryn/bug-hunt-bench, per the repository's quality code). There is a naming risk but no data overlap.
- **LiveBench 2.0 Coding is near saturation.** At 96–98 for five roster models with 29 tasks, it would separate the frontier poorly. The Long Agentic suite (8.3–85.0 spread) discriminates far better, but its 18 tasks include non-SWE app-maintenance domains such as payroll and tax.

### Gaps
- I found no statement of whether the LiveBench 2.0 Coding codebase or tasks are public, or of how often v2 tasks will be refreshed.
- I found no published confidence intervals or run-to-run variance for AICD, LiveBench 2.0 or Surge. Surge's markup has a "range-track" element, but no CI values were visible.
- Disclosures of funding by model labs for AICD or LiveBench were not found. Abacus.AI sponsorship is the only stated LiveBench funding.
- Whether AA cites or ingests any of these three sources was not checked.
