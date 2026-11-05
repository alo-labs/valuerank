# Broadening ValueRank's software-engineering benchmarks (2026-10-23)

## Question

After O49 the software-engineering leaves are FrontierCode 1.1 (AA, 25%), Terminal-Bench 4.0 (AA, 20%) and Bug Hunt Bench (15%). The owner asked which other SWE benchmarks ValueRank can add. Three sources were named as must-incorporate: AI Coding Daily, LiveBench and Surge's Complex Constraints. Vals.ai was named as an example hub.

The binding constraint is O36: only configurations with every leaf are ranked, and nothing is transferred across efforts or versions. A new mandatory leaf is therefore only usable if it covers every cohort configuration at its exact effort. The cohort is the 29 configurations AA plots on or near its frontier (O51); 27 of them are ranked.

## Method

- Claude deep research: three researchers covered the owner-named sources, Vals.ai, and other agentic benchmarks. Notes are in `research_notes/SWE benchmark candidates/`. They read primary data where it existed: LiveBench's `table.csv` and model metadata, Epoch's benchmark archive, CursorBench and the AA captures.
- Perplexity, Search mode with Thinking: GPT-6.1 Sol, Grok 4.7 and Gemini 3.8 Flash each ran the same brief (`brief.md`). Outputs are in `pplx-*.md`.
- Silver Bullet's multi-model deep research (`skills/multi-ai-deep-research`) could not run. It dispatches through opencode-go models, and opencode has no provider credentials in this environment (`opencode auth list`: 0 credentials). The same thing blocked it during the MiMo research.
- The brief listed the earlier 51-configuration roster. The coverage below is re-counted against the current 29-configuration cohort.

## Findings

### Exact-effort coverage of the 29-configuration cohort

| Source | What it measures | Effort on the row | Cohort configurations with an exact result |
|---|---|---|---|
| AI Coding Daily (updated 2026-10-21) | Code quality on existing repos (Laravel, React-TS), bug finding, edge-case tests; 70 points | Yes | 13. Opus 5.5 high, medium; Astra high; Sol high, medium; Luna max, xhigh, high, medium; Haiku high, medium; Argon high; DeepSeek V4.1 Flash 1017 max. Three more are plausible but not exact, because AA plots these models without an effort: MiMo-V2.6-Pro high, MiMo-V2.6-Flash high, MiniMax-M3.1-Flash max. |
| LiveBench 2.0 (release 2026-10-14) | Coding (29 tasks), Long Agentic (18 tasks) | One effort per model, from the site's model metadata | About 10, one effort per family: Opus, Sonnet and Haiku 5.5 max; Sol, Astra and Luna max; Argon high; MiMo-Pro; MiniMax; DeepSeek 1017. LiveBench v1 has xhigh rows for four families, but it is a different benchmark version. |
| CursorBench 4.0 (task version 2026-09-10) | Cursor's agentic coding tasks | Yes | 9: Opus 5.5 max; Haiku 5.5 at all five efforts; Sonnet 5.5 max and xhigh; Argon high. There are no GPT-6, MiMo, DeepSeek or MiniMax rows. |
| Arena Code Arena WebDev | Pairwise human preference (Elo), not task success | Labelled by Arena | About 10 at one effort each, and values for 4 of those could not be read (arena.ai returned HTTP 403). |
| Vals: Vibe Code Bench v1.1, Code Migration v1.1, Vibe Code 1-100, ProgramBench | App building, code porting, iterative change, program reconstruction; Vals' own harness | No (only some launch posts state it) | 0 exact. Vibe Code v1.1 is saturated near 90% at the top. Vals also found the fix in git history in 1,795 of 2,698 MiMo-V2.6 coding environments. |
| Surge Complex Constraints | Single-turn instruction following with rubric criteria and an LLM judge. Not software engineering | Yes | About 3–4: Astra max, Argon high, Opus 5.5 max, and possibly DeepSeek 1017 max (the snapshot is unconfirmed). |
| FrontierSWE V2, SWE-bench family, SWE-Bench Pro, SWE-rebench, Aider, METR, LiveCodeBench, CodeClash, KernelBench, SWE-Lancer | Various | Mostly no; most are stale (before July 2026) or vendor-reported | 0–5 exact |

The union of AI Coding Daily, CursorBench and Arena would reach 24 of 29. The result would be a different benchmark for different configurations, which is not one leaf. Five configurations have no exact result anywhere: Opus 5.5 xhigh, Astra xhigh, Sol xhigh, Luna low and GPT-5.6 Luna low.

### Source notes

- **AI Coding Daily** is the strongest owner-named source. It names version and effort on every row, is recent, and is independent of AA. Its harness varies by model: Claude Code for Anthropic models, Codex CLI for OpenAI, OpenCode for open models, Devin for Argon and Cursor for Grok. Its 10-point bug-finding column overlaps Bug Hunt. It has no JSON or CSV export.
- **LiveBench 2.0**: Coding is saturated at the frontier (Opus 5.5 96.3, Sol 96.0, DeepSeek 1017 96.0). Long Agentic still separates models (Opus 5.5 85.0, Astra 82.4, Sol 73.0, Luna 48.1). There is one effort per model.
- **Surge Complex Constraints** measures instruction following, not software engineering. Using it as a SWE leaf would mislabel what it measures.
- **Vals** is independent of AA and uses one harness. Its tables give one row per model with no effort, so a result cannot be bound to an exact configuration. Its Terminal-Bench 4.0 run duplicates an existing leaf.
- **SWE-Atlas QnA and ITBench-AA** are AA evaluations, so they would not diversify the sources. SWE-Atlas QnA is in Coding Agent Index v2.0, which prices only 7 of 27 ranked configurations.

### Reviewer agreement

All three Perplexity reviewers and the Claude researchers concluded that no candidate meets O36 as a mandatory leaf.

- GPT-6.1 Sol and Grok 4.7 recommended no new scored leaf today, and a zero-weight evidence panel.
- Grok 4.7 named AI Coding Daily (non-bug points only) as the first leaf to promote once it publishes the missing efforts on a pinned harness. It suggested 8 points taken from FrontierCode and Terminal-Bench.
- Gemini 3.8 Flash suggested imputing missing efforts or commissioning runs. Imputation is a transfer across efforts, which O36 and AGENTS.md forbid.

## Conclusion

No benchmark outside AA covers the cohort at exact effort.

- AI Coding Daily is the best of them, at 13 (up to 16) of 29.
- Making any of them a mandatory leaf would cut the ranking roughly in half.
- Pooling sources would score different configurations on different benchmarks.
- Filling gaps from a neighbouring effort is a forbidden transfer.

Adding one of these benchmarks to the score therefore needs an owner decision: either relax O36 for that leaf, or accept a smaller ranking. The alternative is to show the benchmarks as unscored evidence until their coverage is complete.

Options for the owner:

1. **Unscored SWE evidence panel, with promotion when coverage is complete.** Publish AI Coding Daily (excluding its bug-finding column), LiveBench 2.0 Coding and Long Agentic, CursorBench 4.0 and Vals Code Migration and Vibe Code, at exact effort only. Label Surge Complex Constraints as instruction following. No weight. Recheck coverage on every refresh, and make a source a leaf once it covers every ranked configuration.
2. **Optional leaf.** Score AI Coding Daily (for example 8 points, taken 4 from FrontierCode and 4 from Terminal-Bench) for configurations that have it. Configurations without it are scored on the other leaves. This relaxes O36 for one leaf, and the rows are no longer scored on the same leaves.
3. **Mandatory leaf.** Add AI Coding Daily as a required leaf. About 13 of 29 configurations stay ranked.
4. **Ask for the missing runs.** Ask AI Coding Daily, Cursor and LiveBench to run the missing efforts. Nothing is scored until they do. This can be combined with option 1.

## Addendum after O52: benchmark sets and the configurations they rank

O52 picks the benchmarks first and ranks the configurations that have all of them. Two coverage files were built for it, each from captured primary data:

- `vals-catalogue-2026-10-23.json`: all 61 Vals boards, 37 of them active; raw JSON in `vals-capture/`.
- `other-coverage-2026-10-23.json`: AI Coding Daily, LiveBench 2.0, Surge, CursorBench, Arena, FrontierSWE, SWE-rebench and IFBench; raw captures in `other-capture/`.

`tradeoff.py` counts the configurations each set ranks. The 29-configuration coverage grid (X = exact, p = plausible):

| Configuration | AICD (excl. bug finding) | CursorBench 4.0 | LiveBench 2.0 | Vals Vibe Code v1.1 | Vals Code Migration v1.1 | Surge Complex Constraints |
|---|---|---|---|---|---|---|
| Claude Haiku 5.5 (xhigh) | | X | | | | |
| Claude Haiku 5.5 (high) | X | X | | | | |
| Claude Haiku 5.5 (low) | | X | | | | |
| Claude Haiku 5.5 (max) | | X | X | X | X | |
| Claude Haiku 5.5 (medium) | X | X | | | | |
| Claude Opus 5.5 (max) | | X | X | X | X | X |
| Claude Opus 5.5 (high) | X | X | | | | |
| Claude Opus 5.5 (medium) | X | X | | | | |
| Claude Opus 5.5 (xhigh) | | X | | | | |
| Claude Sonnet 5.5 (max) | | X | X | X | X | |
| Claude Sonnet 5.5 (xhigh) | | X | | | | |
| DeepSeek V4.1 Flash 1017 (max) | X | | X | X | X | p |
| Gemini 4 Argon (high) | X | X | X | X | X | X |
| GPT-5.6 Luna (low) | X | X | | | | |
| GPT-6 Astra (max) | | | X | X | X | X |
| GPT-6 Astra (high) | X | | | | | |
| GPT-6 Astra (xhigh) | | | | | | |
| GPT-6 Luna (max) | X | | X | X | X | |
| GPT-6 Luna (high, medium, xhigh) | X | | | | | |
| GPT-6 Luna (low) | | | | | | |
| GPT-6.1 Sol (max) | | | X | X | X | |
| GPT-6.1 Sol (high, medium) | X | | | | | |
| GPT-6.1 Sol (xhigh) | | | | | | |
| MiMo-V2.6-Flash | p | | | p | p | |
| MiMo-V2.6-Pro | p | | p | p | p | |
| MiniMax-M3.1-Flash | p | | p | p | | |

What the coverage supports:

- **The current ten leaves rank 27.**
- **The max-effort group:** LiveBench 2.0 Coding and Long Agentic, Vals Vibe Code Bench v1.1 and Vals Code Migration v1.1 together rank 8 exact (9 with MiMo-V2.6-Pro as plausible). That is one configuration per family, at the vendor's top effort: Opus, Sonnet and Haiku 5.5 max; GPT-6.1 Sol, GPT-6 Astra and GPT-6 Luna max; Gemini 4 Argon high; DeepSeek V4.1 Flash 1017 max. Adding Vals SWE-bench Multimodal drops it to 7.
- **AI Coding Daily alone:** 14 exact, mostly high and medium efforts.
- **AI Coding Daily with the max-effort group:** 3 (Gemini 4 Argon, GPT-6 Luna max, DeepSeek V4.1 Flash 1017).
- **Surge Complex Constraints, if required:** at most 3 exact (GPT-6 Astra max, Gemini 4 Argon high, Claude Opus 5.5 max), plus DeepSeek V4.1 Flash as plausible because its snapshot is unstated. With the max-effort group it stays at 3. With AI Coding Daily it is 1 (Gemini 4 Argon).
- **All three owner-named sources required:** 1 (Gemini 4 Argon).
- **IFBench:** no source publishes it for the cohort. AA dropped it from the Index in v4.1 (2026-06-16), and every cohort row is null in AA's 2026-10-23 snapshot.
- **Vals:** the professional-work boards (Finance Agent v2.1, EMB v1.1, Legal Research, HLAB-Vals-1.1, Tax Agent Bench) reach the same 8-plus-3 ceiling as the SWE boards, and they overlap GDPval-AA, AA-Briefcase and AutomationBench-AA. Vals has no instruction-following board. Vals Terminal-Bench 4.0 is the same task set as the AA-run leaf, on a different harness.

## Check of the three unchecked candidates (O55, 2026-10-23)

Raw captures are in `other-capture/unchecked/` and in Epoch's `mirrorcode.csv`.

- **Epoch MirrorCode** (Epoch's own runs; 13 rows): exact for 3 cohort configurations, Gemini 4 Argon (high) 0.589, Claude Opus 5.5 (max) 0.774 and GPT-6 Astra (high) 0.467. That is 2 in each ranking, so it is not usable as a leaf.
- **SWE-bench-Live** (`reports-0605.jsonl`, 162 submissions, newest 2026-10-20): submissions are agent products paired with a model ("TianxiCode + Deepseek-v4.1-Flash", "Slingshot + GPT-5.6-Sol"), and the harness is chosen by the submitter. No cohort configuration appears with its exact version and effort, so the cohort has 0 exact matches.
- **SWE-PolyBench** (Amazon; leaderboard last dated 2026-08-05): the newest models are Claude Opus 4.8 and GPT-5, so the cohort has 0 matches.

None of the three changes O53–O55.
