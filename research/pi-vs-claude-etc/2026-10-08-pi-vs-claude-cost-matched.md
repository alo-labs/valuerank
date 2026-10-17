# Does Pi cost less than Claude Code at the same model, effort and tasks? (Sept 1 – Oct 8, 2026 only)

Compiled 2026-10-08. Perplexity thread (rounds 15–16, Sol and GLM) plus my own source checks:
https://www.perplexity.ai/search/814b6c66-eefc-44ed-bb93-62eff604919b

**Inclusion rules:** measurement published/dated 1 Sep–8 Oct 2026; same model in both harnesses; same requested reasoning effort; same tasks; cost reported in dollars. Everything else is listed under Exclusions.

## Answer

**Usually yes, by about 1.5–2× per attempt on SWE-style and agentic tasks, but not everywhere.** Pi was cheaper on most matched cells, indistinguishable on some, and clearly more expensive on one hard-terminal suite. Only two studies meet all three conditions.

| Study | Setting | Pi cost vs Claude Code |
|---|---|---|
| HarnessTax (Arena/UC Berkeley, 16 Sep) | 7 models, SWE-bench Lite + Terminal-Bench 2.0, high effort | Claude Code ≈ **2.0×** Pi on SWE-bench Lite, ≈ **1.5×** on TB2.0 (geomean over models) |
| NTU arXiv 2610.00917 (1 Oct) | Claude Opus 5, both request "high" | Pi **38.2% cheaper** (TUA-Bench), **43.3% cheaper** (ALE-CLI), **63.7% MORE expensive** (Terminal-Bench 4) |

## 1. HarnessTax — https://arena.ai/blog/coding-agents-harness-tax (also https://harnesstax.github.io/)

- Authors: Pan, Yang, Arabzadeh, Chiang, Stoica, Zaharia. Published 16 Sep, updated 18 Sep.
- Models: Fable 5, Opus 4.8, Sonnet 4.6, Haiku 4.5, GPT-5.6 Sol, GPT-5.6 Luna, Kimi K3. Harnesses: Pi, Codex, Claude Code.
- Same 30 sampled tasks per benchmark, 3 attempts each (90 per pairing), 100-turn cap, each harness at its own native "high" (Kimi: single thinking mode).
- Cost = mean token cost per attempt at a fixed 1 Sep direct-API price list. Not an invoice, not subscription spend, not cost per success. 95% bootstrap CIs exist but I could not read them.
- Versions (secondary, from Codearia): Claude Code 2.1.224, Pi 0.85.1.
- Authors state effort settings follow each harness's own definitions, so "same effort" means same label, not proven same thinking budget.

**Claude-model per-attempt cost, Pi vs Claude Code ("CC/Pi" is the ratio):**

| Benchmark / model | Pi | Claude Code | CC/Pi | Pi / CC success | Provenance |
|---|---|---|---|---|---|
| SWE-bench Lite / Fable 5 | $0.666 | $1.329 | 2.00× | 96.7% / 97.8% | Primary text + Codearia (**ME**) |
| SWE-bench Lite / Haiku 4.5 | $0.374 | $0.426 | 1.14× | 60.0% / 52.2% | Codearia (**ME**) + SpecPi |
| SWE-bench Lite / Opus 4.8 | $0.473 | $0.976 | 2.06× | 82.2% / 86.7% | **Single source** (SpecPi) |
| SWE-bench Lite / Sonnet 4.6 | $0.679 | $0.669 | 0.99× | 64.4% / 66.7% | **Single source**; indistinguishable, CI unread |
| Terminal-Bench 2.0 / Fable 5 | $1.079 | $1.554 | 1.44× | 71.1% / 75.6% | Single source |
| Terminal-Bench 2.0 / Opus 4.8 | $0.758 | $0.899 | 1.19× | 72.2% / 68.9% | Single source |
| Terminal-Bench 2.0 / Sonnet 4.6 | $0.614 | $0.669 | 1.09× | 65.6% / 62.2% | Single source |
| Terminal-Bench 2.0 / Haiku 4.5 | $0.250 | $0.263 | 1.05× | 47.8% / 41.1% | Single source |

Non-Claude rows for context (GPT-5.6 Sol: 3.49× SWE, 3.22× TB2; Luna 5.07× / 2.18×; Kimi K3 1.72× / 1.36×). Sol's TB2 row is confirmed by Codearia; the rest are single-source.

Reading it: the savings are large for Fable 5 and Opus 4.8 on SWE-bench, shrink to roughly 5–20% on Terminal-Bench 2.0, and vanish for Sonnet 4.6 on SWE-bench. Success rates are within a few points either way.

## 2. NTU "Finding the Right Fit" — https://arxiv.org/abs/2610.00917 (data: https://huggingface.co/datasets/yixuanli97/finding-the-right-fit)

- Li, Zhou, Teng, Yang, Deng, Lyu, Dong, Chen, An (NTU). arXiv preprint, submitted 1 Oct.
- Model: Claude Opus 5 (`anthropic/claude-opus-5`, Anthropic-pinned). Pi 0.84.4, Claude Code 2.1.251.
- Effort: §3.2, "Every harness requests high reasoning effort", with the caveat that the label need not mean the same thinking budget (**ME**, quoted).
- Cost = total agent-model API cost at OpenRouter prices, including auxiliary calls, excluding evaluator calls; one counted run per task (**ME**).

| Suite (tasks) | Pi total | Claude Code total | Per task Pi / CC | CC/Pi | Score Pi / CC |
|---|---|---|---|---|---|
| TUA-Bench (120) | $70.28 | $113.73 | $0.586 / $0.948 | 1.62× | 0.5821 / 0.6889 (partial credit) |
| ALE-CLI (99) | $323.34 | $570.21 | $3.27 / $5.76 | 1.76× | 0.5022 / 0.5428 (partial credit) |
| Terminal-Bench 4 (63) | $1,277.48 | $780.15 | $20.28 / $12.38 | 0.61× | 19/63 (30.2%) / 31/63 (49.2%) |

Totals and scores verified directly (**ME**, Table 6); per-task figures and percentages are calculated. On Terminal-Bench 4, Pi spent about $67 per solved task vs about $25 for Claude Code (derived). Pi scored lower on all three suites. The "119M vs 184M uncached tokens, 3,888 vs 4,472 calls" in the paper compare Pi with OpenHands, not Claude Code.

## 3. Exclusions

**In window, excluded:**
- NVIDIA SoL-Pi (arXiv 2609.20519, 17 Sep). Same Opus 5, same 51 EdgeBench tasks: stock Pi $1,741 vs Claude Code $2,535 (31% cheaper, scores 44.756 vs 43.689). **Excluded because no reasoning effort is documented for the Opus 5 comparison** in the paper or the NVlabs/SoL-Pi repo (Sol and GLM both checked). Fixed 17 Aug price sheet. It points the same direction as the two included studies.
- Composio Pi vs Claude Code (4 Sep): Pi high vs Claude Code max, mixed routing, repeats an August run.
- Bruce/heyuan110 (6 Sep): Gemini 3.1 Pro vs Fable 5.1, different models.
- capocasa GLM bench (7 Sep): effort unstated, author flags a flawed setup.
- Kaitchup/Benjamin Marie (10 Sep): paywalled, no verifiable dollar figures.
- AGI Hunt/zainhas (19 Sep): qualitative, no cost.
- Codearia, SpecPi, social posts: retellings of HarnessTax, not independent.
- Pi 1.0 release and coverage (1–2 Oct): Pi vs older Pi only. Harbor: infrastructure only.

**Older than 1 Sep (excluded by your rule):** Databricks (8 Jul), The Register 742k/237k (13 Jul), PointFive (2 Aug), Systima, hibench, Portkey, Daniele, the Composio July–August posts, Execute Automation.

Searches of Terminal-Bench, Vals, Artificial Analysis, SWE-bench, Kaitchup, Reddit and X found no third qualifying study. Artificial Analysis's harness comparison is "coming soon" with no Pi row; Vals uses Mini-SWE-agent.

## 4. Caveats

- "Same effort" is the same requested label in both studies, not proven equal thinking budget. Anthropic's own docs say effort changes Claude Code's behavior and cost.
- Costs are API-equivalent (list or OpenRouter prices), not subscription spend. Neither study shows Pi beats a Claude Pro/Max plan.
- Cheaper per attempt is not cheaper per quality. NTU shows Pi scoring lower on every suite.
- 9 of the 14 Claude-model cells above rest on a single secondary transcription; treat the Opus 4.8 and Sonnet 4.6 numbers as provisional.
- NTU is a preprint, not peer-reviewed. Neither study tested Pi 1.0.

## 5. Open items

- HarnessTax raw traces/chart data (promised, unreleased) would settle the single-source cells and the Sonnet 4.6 tie.
- NTU's dataset holds per-run cost and tokens for both harnesses; I have not downloaded or aggregated it.
- A `plurnk/harnesstax-evidence` repo mentioned by GLM returned 404 and is dropped.
- No study prices Pi 1.0 against a current Claude Code build.

## Process

Rounds 15 (Sol) and 16 (GLM) in the existing thread. I did **not** run the full six-model, two-cycle roster this time: the two models agreed on the qualifying set and my own fetches confirmed the key numbers, so I stopped. Grok/Kimi/Gemini/Sonnet and a final synthesis were skipped.
