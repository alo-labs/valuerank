No third-party benchmark currently covers all 51 roster configurations at their exact reasoning efforts to satisfy owner decision O36 as an independent leaf. Adopting any evaluated external leaderboard as a standalone mandatory metric would disqualify over 40% of the frontier roster, necessitating either a synthetic pooled leaf or commissioned evaluations on a unified harness.
aicodingdaily
+2

Evaluation of Owner-Named Benchmarks

The three owner-mandated benchmarks provide strong empirical signal, but exhibit structural limitations in reasoning-effort granularity, harness parity, and domain relevance.

Benchmark	What It Measures	Runner & Harness	Reasoning Effort Granularity	Roster Coverage (51 Configs)	Update Cadence & Freshness	Machine Readability

AI Coding Daily
 
aicodingdaily
	Multi-file code quality, bug finding, and edge cases across 7 projects (Laravel, React/TS, Flutter, Go); 27 prompts; max 70 points 
aicodingdaily
+1
	Independent (Povilas Korop); harness varies by model (Claude Code, Codex CLI, OpenCode, Cursor, Devin) 
aicodingdaily
+1
	High for top models (Low, Medium, High, Max tagged) 
aicodingdaily
	~26 of 51 configurations; lacks full effort ladders (missing GPT-6.1 Sol Max/XHigh, Sonnet 5.5 Max/Low) 
aicodingdaily
	Weekly continuous; updated October 21, 2026 
aicodingdaily
	Rendered HTML table; easily scrapable DOM 
aicodingdaily


LiveBench 2.0
 
livebench
	Coding (algorithmic generation from LeetCode/AtCoder and completion) 
livebench
; Agentic (long-horizon apps, bug fixes, research); 0–100 score 
livebench
	LiveBench consortium; standardized automated test sandbox 
livebench
	Coarse; reports single default/peak configuration per model name 
livebench
	~38 of 51 models, but 0% multi-effort ladder coverage 
livebench
	Bi-weekly/monthly; updated October 18, 2026 
livebench
	Native CSV export and JSON category endpoints 
livebench
+1

Surge AI ComplexConstraints 
arxiv
	Interlocking, conditional instruction following; 75 prompts, 1,559 rubric criteria; LLM-as-a-judge (all-pass %) 
github
+1
	Surge AI; single-turn completion (no tools, non-agentic) 
github
	Sparse; isolated tags (e.g., Astra Max, Argon High) 
theaggregate
+1
	~22 of 51 configurations; lacks open-weights and effort sweeps 
atlas.kevinhu
	Static/periodic; last refreshed mid-2026 
arxiv
+1
	HuggingFace CSV dataset; rendered leaderboard 
arxiv
+1

AI Coding Daily offers the closest match to real developer workflows because tasks start from existing codebases rather than blank files. Scored roster models include Claude Opus 5.5 High (67.26), GPT-6 Astra High (66.35), GPT-6.1 Sol High (66.00), DeepSeek V4.1 Flash 1017 Max (61.20), Gemini 4 Argon High (57.09), Grok 4.7 High (60.09), and MiMo-V2.6 Pro High (53.81). The critical defect is scaffolding variation: pairing Anthropic models with Claude Code while routing Chinese open-weight models through OpenCode introduces harness bias. Furthermore, it tests only two or three effort tiers per model, omitting required extremes like GPT-6.1 Sol Max and Haiku 5.5 Low.
aicodingdaily
+1

LiveBench 2.0 delivers strong contamination resistance through fresh monthly problem sourcing. Coding top scores include Claude Fable 5.1 (97.7), Opus 5.5 (96.3), GPT-6.1 Sol (96.0), and DeepSeek V4.1 Flash 1017 (96.0). Agentic scores show healthier differentiation, led by Opus 5.5 (85.0) and GPT-6 Astra (82.4). However, LiveBench 2.0 completely obscures reasoning effort, reporting a single aggregated row per model, which directly violates ValueRank's exact-configuration mandate.
livebench
+1

Surge AI's ComplexConstraints benchmark should be rejected on validity grounds. While top models like GPT-6 Astra Max score 57.7% and Gemini 4 Argon High scores 53.3%, the benchmark evaluates general instruction following rather than software engineering. The tasks span scheduling, administrative workflows, and film production without a terminal execution sandbox.
atlas.kevinhu
+2

Vals AI Benchmark Hub Analysis

Vals AI
 operates 36 domain-specific evaluations running on a unified Valkyrie cloud harness, providing superior comparability across agentic coding tasks.
vals
+1

Vibe Code Bench v1.1: Measures end-to-end web application generation across 100 specifications using Docker Compose and browser-based verification. It includes 118 models, with Claude Sonnet 5.5 at 92.39%, Gemini 4 Argon at 91.91%, and Claude Haiku 5.5 at 90.44%. While technically rigorous, top frontier models are rapidly saturating the benchmark above the 90% threshold.
vals
+2

ProgramBench: Evaluates cleanroom reconstruction of command-line programs from compiled binaries and behavioral specifications across 200 tasks. It utilizes a standardized Mini-SWE-agent harness with bash-only sandboxing. Current frontier scores reflect high headroom: Claude Opus 5.5 leads at 18.50%, Claude Fable 5.1 scores 7.00%, and Claude Sonnet 5.5 achieves 6.50%.
vals
+1

Terminal-Bench 4.0: Evaluates 66 frontier terminal tasks across operations, ML pipelines, and software maintenance. Claude Opus 5.5 achieves 65.15%, Claude Sonnet 5.5 scores 64.14%, and GPT-6 Astra reaches 59.60%. Because Artificial Analysis already supplies an in-house run of Terminal-Bench 4.0 for ValueRank, incorporating Vals AI's run would introduce double-counting.
vals

Vibe Code Bench 1-100: Tests code evolution and regression resistance by requiring agents to modify existing applications across successive user requests. Wonder Full leads at 33.98%, followed by Claude Opus 5.5 at 30.36%. However, coverage is restricted to 26 models, lacking the required reasoning effort variants.
vals
+1

SRE Bench: Assesses binary reverse engineering and site-reliability troubleshooting across 35 models. It is led by GPT-6 Astra, GPT-6.1 Sol, and Gemini 4 Argon. It represents an ideal DevOps leaf, but suffers from insufficient cohort coverage.
vals

Vals AI provides an open execution harness via its Valkyrie orchestrator and public model library, but its public leaderboards do not publish the complete 51-configuration reasoning matrix.
vals
+1

Broader SWE and DevOps Benchmarks

The broader software evaluation ecosystem exhibits severe saturation or outdated cohort coverage.

SWE-bench Verified: The historical 500-task benchmark has saturated among 2026 frontier models. Claude Opus 5 reached 97.00%, DeepSeek V4 Pro reached 96.40%, and GPT-5.6 Sol scored 96.20% before Vals AI archived the board in September 2026. The benchmark lacks discrimination for the current frontier roster.
swebench
+1

LiveCodeBench: Archived by multiple tracking aggregators. Its focus on competitive programming and algorithmic snippets does not reflect modern repo-level agentic engineering.
vals

Aider Polyglot Leaderboard: Maintained independently with strict Git-diff scoring, but updates are sporadic and lack systematic sweeps across reasoning-effort ladders for Chinese open-weight models like MiMo-V2.6 and GLM-5.3.
aicodingdaily

METR Time-Horizon Evaluations: Highly informative for catastrophic risk and autonomous task duration, but run on small model batches with irregular update schedules that do not match ValueRank's release velocity.

Multi-SWE-bench and SWE-PolyBench: Multi-language extensions offer good linguistic breadth, but independent runner support has stalled, leaving recent configurations unmeasured.

Leaf Recommendations and Weight Allocation

Enforcing owner decision O36 means that adding an incomplete benchmark will drop crucial models like GPT-6.1 Sol Max and Claude Haiku 5.5 Low from ValueRank's rankings. Three viable implementation paths address this constraint:
aicodingdaily

Commission In-House Runs on Vals AI's ProgramBench: Adopt ProgramBench as a dedicated 15% leaf. ProgramBench has high ceiling headroom and a standardized Mini-SWE-agent harness. ValueRank should execute the missing roster configurations directly through Valkyrie to achieve 100% cohort coverage before making it a binding leaf.
github
+1

Form an Imputed External SWE Pool: Aggregate AICodingDaily (code editing/quality) and LiveBench 2.0 (agentic coding) into a single 15% composite leaf. For configurations where AICodingDaily lacks intermediate reasoning efforts (e.g., Sol Medium to High), linearly interpolate scores between adjacent tested levels or inherit baseline model scores to prevent cohort disqualification.
livebench
+1

Re-weight Existing Leaves: If execution budgets cannot fund custom runs and imputed scores are rejected under O36, retain the current three leaves and adjust their weights to absorb the retired DeepSWE allocation: FrontierCode 1.1 at 30%, Terminal-Bench 4.0 at 20%, and Bug Hunt Bench at 10%.

text
Proposed SWE Weight Distribution (Option 1 - Commissioned ProgramBench):
├── FrontierCode 1.1 (AA Run)......................... 25%
├── Terminal-Bench 4.0 (AA Run)....................... 20%
├── Bug Hunt Bench (Independent)...................... 15%
└── ProgramBench (Vals AI Harness, Commissioned)...... 15%
Total SWE Category Weight: 60% of Quality

If synthetic imputation is disallowed under decision O36, state whether ValueRank has compute budget to execute the missing roster configurations directly on Vals AI's open harness.
github