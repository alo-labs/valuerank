I'll treat coverage of the exact 2026 roster as the binding constraint and start from the three owner-named leaderboards plus Vals, then check which other SWE benchmarks actually publish per-configuration results.
The three named boards are live, but Surge did not return a page. Next I’ll pull methodology and machine-readable results, then map exact-effort coverage.
Coverage is the blocker, so I’m pulling the scoring pages and the SWE boards that actually name effort, not just model families.
Do not add a new mandatory SWE leaf. No candidate has near-complete results for the exact model version and reasoning effort across the 51-configuration roster, so under O36 a new gating leaf would drop most of the ranking.

Recommendation

Keep the current SWE split: FrontierCode 1.1 at 25, Terminal-Bench 4.0 (Artificial Analysis) at 20, and Bug Hunt Bench at 15. Add nothing to the quality score until a source publishes the missing effort rows. The least-bad future leaf is AI Coding Daily, and only after those rows exist and the harness is pinned. A defensible later weight is 8 points inside the existing 60, taken as 4 from FrontierCode and 4 from Terminal-Bench, not by raising software engineering above 60. Vals is the right hub for a second, fixed-harness leaf, but only Vibe Code Bench v1.1 plus Code Migration v1.1, and only after effort is on the row. LiveBench and Surge cannot carry weight today.

Owner-named sources
AI Coding Daily

Povilas Korop runs one coding agent per prompt on existing repositories, with no subagents and no human coaching. The August 21 methodology page says 7 projects and 27 prompts across Laravel/PHP, React/TypeScript, Flutter/Dart, and Go, each prompt repeated in a fresh copy, with a median runtime of 4–11 minutes. The live board, last updated October 21, 2026, does not match that page. It scores four columns out of 70: Laravel code quality (20), React-TS code quality (20), bug finding (10), and edge-case testing across 4 projects (20). Repeat count is not stated. There is no public JSON or CSV.
aicodingdaily
+1

The harness is part of the result. Opus and Sonnet run in Claude Code, GPT models in Codex CLI, Gemini 4 Argon in Devin, Gemini 3.8 Flash in Antigravity, and most open models in OpenCode. DeepSeek V4.1 Flash 1017 at Max is listed twice: 61.2 on the DeepSeek harness with no API cost, and 60.97 on OpenCode at $0.07. That is a model-plus-scaffold score, not an exact model configuration. The 10-point bug-finding column also overlaps Bug Hunt Bench; if this board is ever used, score the other 60 points only.
aicodingdaily

Effort is named, which is rare. Visible rows that match the roster:

Configuration	Total / 70	Harness
Opus 5.5 high / medium / low	67.26 / 65.28 / 60.50	Claude Code
GPT-6 Astra high / medium	66.35 / 66.03	Codex CLI
GPT-6.1 Sol high / medium / low	66.00 / 65.05 / 61.45	Codex CLI
Sonnet 5.5 high / medium	64.31 / 60.54	Claude Code
DeepSeek V4.1 Flash 1017 max / high	61.20 and 60.97 / 55.21	DeepSeek harness; OpenCode
Fable 5.1 medium	61.03	Claude Code
Grok 4.7 high	60.09	Cursor
GPT-6 Sol high / medium	59.92 / 56.32	Codex CLI
GPT-6 Luna max / xhigh / high / medium	59.07 / 56.40 / 53.04 / 43.74	Codex CLI
Haiku 5.5 high / medium	58.63 / 58.20	Claude Code
Gemini 4 Argon high	57.09	Devin
Kimi K3 high; Grok 4.6 high; GLM-5.3 high	56.89 / 56.71 / 54.82	OpenCode or Cursor
MiniMax-M3.1-Flash max	54.48	OpenCode
MiMo-V2.6-Pro high; MiMo-V2.6-Flash high	53.81 / 53.29	OpenCode
Qwen3.8 Max 0902 high; Muse Spark 1.3 max	53.39 / 53.01	OpenCode
GLM-5.3 Flash max; Gemini 3.8 Flash high	47.51 / 47.09	OpenCode; Antigravity
DeepSeek V4 Pro 0813 max / high	50.35 / 48.34	OpenCode

Missing from the visible table, and not confirmed in the hidden older-model list: GPT-6.1 Sol max and xhigh; Haiku 5.5 max, low, and default; Sonnet 5.5 max, xhigh, and low; Muse Spark 1.3 xhigh; Grok 4.6 xhigh; Muse Wonder and Wonder Full; and the older cohort (GPT-5.6 Sol, GPT-5.6 Luna, GPT-5.5, Opus 5, Fable 5, Opus 4.8, Sonnet 5, the older Gemini Flashes, GLM-5.2, DeepSeek V4 Flash, Muse Spark 1.2). July 26 cleanup removed some of those names. Coverage is the best of the three required sources and still fails O36.
aicodingdaily

LiveBench

LiveBench 2.0, release 2026-10-14 and last updated October 18, 2026, is an independent long-horizon board. The public table has seven suites: Agentic, Reasoning, Coding, Browser Use, Data Analysis, Research, and Design. Overall is the mean of suites with a score. The site says models do real work, including bug fixes and apps that run for hours, and that grading is of the artifact handed back. Task counts for the 2.0 Coding and Agentic suites are not on the page. The GitHub README and changelog still describe the older six-category suite and stop at January 8, 2026, including an agentic-coding task run with mini-SWE-agent. Treat 2.0 task counts, languages, and the harness as unpublished. No reasoning effort is on any row. No 2.0 JSON export was found; the old repo can emit CSV for older releases.
livebench
+2

Coding is saturated at the frontier. Agentic still separates models. Roster hits, one row each, effort unknown:

Model	Coding	Agentic
Claude Fable 5 / Fable 5.1	98.3 / 97.7	53.2 / 80.8
Claude Opus 5.5 / Opus 5 / Sonnet 5.5 / Sonnet 5 / Haiku 5.5	96.3 / 90.8 / 94.7 / 74.7 / 91.4	85.0 / 62.1 / 78.8 / 39.0 / 57.6
GPT-6 Astra / GPT-6.1 Sol / GPT-6 Sol / GPT-6 Luna	93.7 / 96.0 / 93.1 / 84.5	82.4 / 73.0 / 66.9 / 48.1
GPT-5.6 Sol / GPT-5.6 Luna / GPT-5.5	89.7 / 73.6 / 85.1	48.5 / 30.4 / 44.6
Gemini 4 Argon / 3.8 Flash / 3.7 Flash	89.7 / 82.2 / 80.5	69.9 / 30.1 / 28.3
DeepSeek V4.1 Flash 1017 / V4.1 Flash	96.0 / 90.2	50.9 / 40.1
Grok 4.6 / 4.7; MiMo V2.6 Pro; MiniMax M3.1 Flash	89.1 / 84.5; 81.5; 83.9	40.7 / 50.1; 47.5; 34.7
Muse Spark 1.3 / 1.2; Muse Wonder 1.0; GLM-5.3 / 5.3 Flash; Kimi K3; Qwen3.8 Max	90.2 / 78.2; 86.2; 82.8 / 80.6; 59.3; 60.3	40.4 / 21.3; 53.2; 35.9 / 28.4; 42.8; 42.3

Absent: MiMo-V2.6-Flash, Muse Wonder Full, Gemini 3.6 Flash, Gemini 3.5 Flash, GLM-5.2, DeepSeek V4 Pro, DeepSeek V4 Flash, and every effort variant. Coding should not be a leaf. Agentic is more informative but is not a software-engineering score.
livebench

Surge ComplexConstraints

This is not a software-engineering benchmark. It is 75 single-turn instruction-following prompts, CIF-001 to CIF-075, with 1,559 expert rubric criteria. The model answers once, with no tools. An LLM judge scores each criterion alone. The leaderboard metric is all-criteria task pass rate; mean criteria satisfied is also reported. The dataset is claimed as CC-BY-4.0 CSV on Hugging Face, but the viewer could not load the file. The public leaderboard page did not return on October 23.
github
+1

The only primary score table is the paper’s June 3, 2026 snapshot. The best model passes 40.4% of tasks. Roster overlap is five older rows: GPT-5.5 38.7, Gemini 3.5 Flash 36.9, Claude Opus 4.8 34.9, DeepSeek V4 Pro 26.7, DeepSeek V4 Flash 16.4. Nothing from the October frontier is in that table. Headroom is real and the judge is a methodological risk, but the board is four months behind the cohort. Weight in SWE: zero until Surge republishes exact-effort rows for this roster.
arxiv

Vals coding boards

Vals runs its own evaluations and is independent of Artificial Analysis. That independence is the reason to look here. It is not a reason to add a leaf. Rows name the model and, for Terminal-Bench, the harness. They do not name reasoning effort. Effort appears only in launch posts, and those posts are older than the current tables, so the two must not be mixed. Anthropic runs often use a server-side fallback; counting fallback-assisted tasks as failures moves scores, sometimes by a lot on security work. Results are HTML tables, not a public results API.
vals

Vibe Code Bench v1.1, updated October 20, 2026, asks an OpenHands agent to build a web app from a one-page spec, up to 5 hours or 1,000 turns, with Supabase, Stripe test mode, and MailHog. A browser agent grades workflows. An application passes a test when at least 90% of substeps pass; the model score is the mean across applications. The paper describes 100 specs, 50 public and 50 held out. The top is tight and high: Sonnet 5.5 92.39%, Gemini 4 Argon 91.91%, Haiku 5.5 90.44%, Fable 5 90.35%, Opus 5.5 90.29%. Useful roster points below that include GPT-6.1 Sol 88.93%, Astra 89.59%, DeepSeek V4.1 Flash 1017 87.73%, MiMo Pro 85.22%, GPT-6 Luna 81.65%, MiMo Flash 78.96%, GPT-5.6 Luna 77.06%, MiniMax-M3.1-Flash 73.94%. One row per model. Launch posts pin some efforts (Argon high, several Claude and OpenAI rows max, Grok 4.7 xhigh, MiniMax max), but the board itself does not.
vals
+1

Code Migration v1.1, updated October 19, uses the Pi harness and hidden behavior tests. Thirty repositories are each ported into four other languages among Python, Java, Kotlin, Rust, and C++, plus 10 COBOL-to-Java systems. The headline is hidden-test pass rate, with CLI weighted three times COBOL. Anti-cheat zeroes wrapped binaries and hardcoded outputs. This is the best unsaturated Vals coding task: Sonnet 5.5 86.88%, Opus 5.5 81.01%, Astra 80.58%, GPT-6.1 Sol 77.32%, Argon 70.80%, DeepSeek 1017 67.52%, Haiku 5.5 52.36%, MiMo Pro 48.79%, GPT-6 Luna 46.67%, MiMo Flash 39.55%. Twenty-six models. Missing MiniMax-M3.1-Flash, GPT-5.6 Luna, Muse Spark, Grok 4.6, and every effort split.
vals

Vibe Code Bench 1-100, updated October 14, starts from a passing v1.1 app and applies up to 10 dependent product requests. The score is the fraction of the planned sequence completed before the first failed iteration, mean across 50 test scenarios. The same OpenHands environment is used, with a 10-hour budget. Nothing is saturated: Wonder Full 33.98%, Opus 5.5 30.36%, Astra 27.64%, GPT-5.6 Luna 22.59%, Argon 21.20%, Haiku 5.5 20.41%. Missing GPT-6.1 Sol, GPT-6 Luna, Sonnet 5.5, both MiMo models, MiniMax-M3.1-Flash, and DeepSeek 1017. Right construct, wrong coverage.
vals

Vals Terminal-Bench 4.0, updated October 22, is 66 new tasks, avg@3, pass/fail, mini-SWE-agent, 8-hour limit. About three quarters of the tasks are outside ordinary software engineering. Artificial Analysis also runs Terminal-Bench 4.0 on mini-SWE-agent. This is a second measurement of an existing leaf, not a new one. Do not add it. Vals SWE-bench Verified was archived September 1 at 97% for Opus 5 and does not contain the October roster.
artificialanalysis
+2

SRE Bench, updated October 14, is binary reverse engineering: 262 private instances and 1,572 deterministic tasks. Astra leads at 56.87% capability score. It is a security diagnostic, not a SWE leaf, and the roster is incomplete. Vals also reported that 1,795 of 2,698 MiMo v2.6 coding environments still contained the fix in Git history, and that MiMo used that leak, including on a Terminal-Bench 4 task. Treat MiMo coding scores as contaminated until the run is audited.
vals
+1

Other candidates

These are current enough to name and not current enough to use.

Benchmark	Why it fails O36
SWE-Bench Pro V2 (Scale, refreshed Sep 22)	642 tasks, resolve rate, effort named, but 16 published systems, mixed harnesses, and a saturated public top: Opus 5 xhigh on Claude Code 98.00, Fable 5.1 high 92.20, Argon high on mini-SWE-agent 92.16. The page still narrates the old 23% result. 
scale

SWE-bench Multilingual (Mercor)	298 issues, 9 languages, six Max rows, 95.4–98.2%. Saturated and tiny. 
mercor

Aider Polyglot	225 Exercism tasks in six languages. The official board’s last cited frontier pass rates are still GPT-5-era; a November 20, 2025 update is the last primary date found. 
aider
+1

METR Time Horizon 1.1	Expanded to 228 tasks on January 29, 2026. Public points found are Opus 4.5/4.6-era, and secondary writeups disagree. Not this roster. 
metr

SWE-Lancer	Four models, newest a GPT-5.1 Codex row, aggregator update August 2026. 
llm-stats

CodeClash	Elo board last updated November 3, 2025, led by Claude Sonnet 4.5. 
codeclash

KernelBench	A five-model October snapshot led by Fable 5. Not a cohort board. 
benchlm

SWE-Atlas-QnA-AA and ITBench-AA are Artificial Analysis evaluations. Adding them would deepen AA dependence, not diversify it. Multi-SWE-bench has no current frontier board that covers this roster.
artificialanalysis

Coverage and weights

O36 is the binding constraint, and every candidate fails it. The important slice is the clearest proof. GPT-6.1 Sol max and xhigh, Haiku 5.5 max, low, and default, and Sonnet 5.5 max, xhigh, and low have no AI Coding Daily row. LiveBench, Vals, Scale, and Surge each collapse those effort variants into one unlabeled or differently labeled row, or omit them. MiMo-V2.6-Flash is missing from LiveBench and from Vibe Code Bench 1-100. MiniMax-M3.1-Flash is missing from Code Migration. Muse Wonder Full is missing from AI Coding Daily and LiveBench. Grok 4.6 xhigh is not the same row as Grok 4.6 high.

A pooled leaf does not fix that. Averaging AI Coding Daily with Vals would mix different harnesses, different scales, and unlabeled efforts, then still leave configs with no exact row. Imputing the missing effort from a neighboring effort is exactly the transfer O36 forbids.

What is usable now is a non-gating evidence panel, with zero quality weight:

AI Coding Daily, non-bug-finding points only, and only where the effort string matches the roster. Do not average the two DeepSeek 1017 Max harnesses.

Vals Vibe Code Bench v1.1 and Code Migration v1.1 as separate columns, tagged “effort unpinned” unless a launch post states it for that run.

LiveBench Agentic as context, not as a SWE score. Ignore LiveBench Coding for ranking.

Do not score any October configuration from the June 3 ComplexConstraints table.

The evidence requests that would change this are specific: AI Coding Daily for the missing effort variants on one pinned harness; Vals for effort on the row and a no-fallback rescore of Vibe Code Bench v1.1 and Code Migration v1.1; LiveBench for a 2.0 task manifest and per-effort export; Surge for a post-June leaderboard export. Until one of those lands, another benchmark name will not make the ranking more complete.