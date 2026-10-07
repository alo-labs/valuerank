# GPT-6.1 Sol coding benchmark evidence

Captured 2026-10-08 (Australia/Sydney) through the Codex built-in browser. Canonical inclusion variant: **GPT-6.1 Sol (max)**. Max and XHigh are separately evaluated configurations and their scores must not be transferred.

## Artificial Analysis / DeepSWE v1.1

- Owner page: https://artificialanalysis.ai/agents/coding-agents?coding-agents-performance-chart=deep-swe-v1.1&agents=codex-gpt-6-1-sol-max
- Owner chart displays **70** for **Codex — GPT-6.1 Sol (max)**. This is the public chart's rounded score, not a reconstructed decimal result.
- Benchmark: DeepSWE **v1.1**, 113 software engineering tasks. Page states average pass@1 over three attempts per task.
- Run specifications identify **Codex 0.154.0**, provider OpenAI, with 3/3 benchmark coverage. The adjacent release-date field says **Unknown**; that is not an evaluation date.
- The full model selector contains 31 configurations. Max is outside the initial featured selection, but becomes visible when selected. Owner absence must therefore not be inferred from the featured chart.
- All GPT-6.1 Sol owner chart configurations: low **68**, medium **72**, high **71**, xhigh **73**, max **70**. These are each rounded public chart values and remain separate.
- The chart's Download data button opens an Artificial Analysis Pro **Get Access** modal. No public export or extra numerical precision was retrieved, and no paywall bypass was attempted. Evaluation/publication date for the AA row was not exposed in the inspected public run specification.
- The coding chart's 31-model picker has **no MiMo Pro or MiMo Flash configuration**. Their coding coverage remains absent from this owner surface as observed today.

### Full 31 configuration public chart capture

Every score below is the public chart's rounded value. Selecting all 31 showed these labels and values in descending chart order.

| Agent and exact model configuration | DeepSWE v1.1 public chart |
| --- | ---: |
| Antigravity CLI — Gemini 4 Argon | 79 |
| Muse Code — Muse Spark 1.3 (xhigh) | 73 |
| Codex — GPT-6.1 Sol (xhigh) | 73 |
| Grok Build — Grok 4.7 (xhigh) | 73 |
| Codex — GPT-5.6 Sol (max) | 72 |
| Claude Code — Sonnet 5.5 (max) | 72 |
| Codex — GPT-6.1 Sol (medium) | 72 |
| Muse Code — Muse Spark 1.3 (max) | 72 |
| Codex — GPT-6.1 Sol (high) | 71 |
| Codex — GPT-6.1 Sol (max) | 70 |
| Codex — GPT-6 Sol (max) | 69 |
| Kimi Code CLI — Kimi K3 | 68 |
| Claude Code — Opus 5.5 (max) | 68 |
| Claude Code — Sonnet 5.5 (xhigh) | 68 |
| Codex — GPT-6 Astra (max) | 68 |
| Codex — GPT-6.1 Sol (low) | 68 |
| Devin Fusion CLI — GPT-6 Astra XHigh + SWE-2 Medium | 67 |
| Claude Code — Sonnet 5.5 (high) | 67 |
| Codex — GPT-5.6 Luna (max) | 66 |
| Antigravity SDK — Gemini 3.8 Flash (high) | 66 |
| Claude Code — Sonnet 5.5 (medium) | 65 |
| Grok Build — Grok 4.6 (xhigh) | 65 |
| Claude Code — Fable 5.1 (max) (with fallback) | 64 |
| Codex — GPT-6 Luna (max) | 64 |
| Devin Fusion CLI — Claude Fable 5.1 XHigh + SWE-2 Medium | 63 |
| Claude Code — Opus 5 (max) | 63 |
| Claude Code — Sonnet 5.5 (low) | 62 |
| Opencode — GLM-5.3 | 61 |
| Codex — DeepSeek V4 Pro 0813 (max) | 57 |
| Codex — DeepSeek V4 Flash 0731 (max) | 54 |
| Claude Code — Qwen3.8 Max | 51 |

## Bug Hunt Bench

- Owner leaderboard: https://bughunt.productcompass.pm/?preset=featured
- Board update date: **2026-10-07**. Two repos contain **105** planted bugs; extras are tracked separately and never scored.
- Immutable owner notes: https://github.com/phuryn/bug-hunt-bench/blob/931c1ff9b9aaced865aaf56eaf744b7b1f182fc2/results/run-notes.md#user-content-gpt-61-sol-max-effort---mean-of-3
- Exact configuration: **GPT-6.1 Sol (max effort)**, OpenAI's **Codex CLI 0.159.0**, through a ChatGPT account, code mode off; blinded **grok-4.7** judge.
- Owner result: **44.3 / 105**, mean of **three independent runs**, dated **2026-09-30**. The individual scores are **44, 42, 47**, observed range **5**. Repo means are 22.3/45 and 22/60.
- Reported unplanted fixes: **65.3** mean, never included in score. Owner reported wall: **139.3 min**; list-rate API cost estimate **$5.88**, not an invoice. Raw run notes list walls 112.4, 175.1, 130.5 min and costs $6.56, $6.16, $4.92.
- Caveats: Max is below the account's Ultra tier; this row is not the model's ceiling. The newer CLI was required because the older client refused this model, so comparisons to earlier OpenAI rows combine model and client differences. Some laptop load may inflate wall time. No retained request reached the long-context surcharge threshold. An earlier sandbox-blocked attempt was voided; it is excluded from the reported score.
- Separate XHigh row: **42.7 / 105**, n=3, dated 2026-09-30, runs 41,43,44 (range3), same Codex 0.159.0 / ChatGPT route / grok-4.7 judge. Board wall98.7min, list estimate$4.35. This is not the Max numerator.

## Provider-claim policy decision

Both required coding owner results exist for the exact Max variant. Provider fallback is unnecessary for these results. Preserve any existing provider claims for other benchmarks/variants, and do not import GPT-6 Sol results into GPT-6.1 Sol.

## Source freshness

All 31 AA public chart labels and scores were recaptured on 2026-10-08. The source file carries that current observedAt while retained rows preserve previouslyObservedAt 2026-09-29 and previousSourceOrder. Every row identifies the score as rounded_public_chart. Only the Max GPT-6.1 Sol row maps to the canonical model; the other four effort rows are retained as alternate_effort_excluded. The Bug Hunt file is a selective GPT-6.1 Sol addition: its other model records and original snapshot dates remain historical.
