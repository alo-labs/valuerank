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
