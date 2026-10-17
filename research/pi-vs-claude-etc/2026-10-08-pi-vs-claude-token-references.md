# Pi coding agent vs Claude: token-consumption references (Sept–Oct 2026)

Compiled 2026-10-08 from a 14-round, six-model Perplexity thread plus my own source checks.
Thread: https://www.perplexity.ai/search/814b6c66-eefc-44ed-bb93-62eff604919b
Notes and process log: `perplexity-notes.md` (same folder).

Window = 2026-09-01 to 2026-10-08. "Older" = before that.
Verification: **V** opened by a model in the thread; **ME** also opened by me directly; **R** republication/mirror; **S** snippet or paywall only; **P** carried from an earlier fetch.

## Bottom line

The claim "Pi consumes much fewer tokens than Claude" is **supported only in narrow forms**:

| Form of the claim | Verdict | Best evidence |
|---|---|---|
| Fixed per-request / initial context | **Strongly supported** (about 10–16×) | Arena HarnessTax >10× across 7 models; hibench 20,556 vs 1,264; heyuan110 31,012 vs 1,358 |
| Whole-task context/input traffic | **Supported on some workloads** (about 3×) | Databricks via The Register: 742,000 vs 236,999 tokens/task on Opus 4.8 (July, older) |
| Whole-task cost | **Often lower for Pi, not always** (about 1.5–2× in Arena) | Arena 2.0×/1.5×; NTU: Pi cheaper on 2 of 3 suites, costlier on Terminal-Bench 4 |
| Whole-task **total tokens** | **Mixed; not reliably lower** | NVIDIA Opus 5: stock Pi 2.3697B vs Claude Code 2.0045B (Pi more) |

No September–October source shows stock Pi using *much fewer whole-task tokens* than Claude Code on a Claude model. No Pi 1.0 vs current Claude Code ledger on a Claude model was found. The "10×" figure holds for the first request, not for a finished task.

## Part A — references supporting "Pi uses fewer tokens"

| # | Source (URL) | Date / window | Claim (metric named) | Models / versions | Caveats | Status |
|---|---|---|---|---|---|---|
| A1 | Arena HarnessTax — https://arena.ai/blog/coding-agents-harness-tax | 16 Sep (upd. 18 Sep), **in window** | Claude Code mean initial context >10× Pi's across 7 models. Cost per attempt (geomean): Claude Code ~2.0× Pi on SWE-bench Lite, ~1.5× on Terminal-Bench 2.0. Fable 5: 97.8%/$1.33 vs 96.7%/$0.67, 15.3 vs 15.4 turns | 21 model–harness pairs; Pi 0.85.1, CC 2.1.224 (secondary) | Cost per attempt, not tokens. Haiku 4.5 gap is only ~1.14× ($0.426 vs $0.374, via Codearia). Traces unreleased. My own fetch was truncated | V (Sol, GLM, Kimi); not ME |
| A2 | The Register on Databricks — https://www.theregister.com/ai-and-ml/2026/07/13/the-price-is-wrong-ai-cost-calculation-has-to-consider-task-completion-rates-not-just-token-costs/5270683 ; Databricks post https://www.databricks.com/blog/benchmarking-coding-agents-databricks-multi-million-line-codebase | 13 Jul / 8 Jul, older | Opus 4.8: Claude Code 742,000 vs Pi 236,999 context tokens/task (~3.2×); Databricks: ~3× less context per turn, >2× cost gap, same quality | Opus 4.8, matched effort | Private tasks; 742k figure is The Register's report, not in the Databricks prose. Sonnet (r8) wrongly said The Register lacked it; Sol and GLM refuted that | V (Sol, GLM) |
| A3 | hibench — https://hibench.dev/compare/claude-code-vs-pi/ | data 7 Jul, older | First request (o200k_base): Claude Code 20,556 vs Pi 1,264 (16.3×); 25 vs 4 tools | CC 2.1.202, Pi 0.80.3 | No model run; not billed usage | V |
| A4 | Carmelo Daniele — https://c-daniele.github.io/en/posts/2026-05-18-coding-harness-comparison/ | 18 May, older | Same Haiku 4.5, first turn: Claude Code 28,407 input/$0.0391 vs Pi 2,768/$0.0031 | Haiku 4.5 via Bedrock | One cold turn; see warm-cost counterpoint in Part B | V |
| A5 | Bruce (heyuan110), PONG test — https://www.heyuan110.com/posts/ai/2026-09-06-pi-coding-agent-review/ | 6 Sep, **in window** | One-word prompt: Pi 1,358 input tokens vs Claude Code 31,012 (20,884 cache write + 10,126 cache read + 2). Tasks a/b: Pi 75k/86k vs 132k/219k input | Pi 0.85.1 on Gemini 3.1 Pro vs CC 2.1.268 on Fable 5.1 | Different models; task c reverses (Part B) | **ME** (numbers match) |
| A6 | Harrison Guo — https://harrisonsec.com/blog/system-prompt-token-floor/ | 11 Sep, **in window** | Pi source floor 1,138 tokens (550 prose + 588 tool schemas) | Pi source at 1 Sep | Reconstruction, not API capture | V |
| A7 | Composio Kimi K3 — https://composio.dev/content/best-ai-agent-harnesses | 4 Aug, older | Same Kimi K3: Pi fewest tokens (~316k/task), 18/25, $0.57/success vs Claude Code 19/25, $1.96/success | Kimi K3 via OpenRouter | **Not a Claude model.** CC's token total not printed | V (Grok) |
| A8 | Composio six-harness thread — https://x.com/composio/status/2083161873357111297 | 31 Jul, older | Avg cost/task $0.40 Pi vs $1.47 Claude Code (median $0.29 vs $0.72) | Kimi K3, 26 tasks | Cost only | P |
| A9 | Composio DeepSeek Flash — https://composio.dev/content/best-agent-harness-deepseek-v4-flash and https://composio.dev/content/pi-agent-vs-claude-code | 11 Aug / 4 Sep | Runtime tokens/task: Pi 558,885 vs Claude Code 741,659 (-25%); $0.028 vs $0.195 per success; 20/30 vs 16/30 | DeepSeek V4 Flash | Pi on high reasoning, others max; two providers; **Claude Code cache share 1.5%** vs ~57–70% others, so the cost gap is not a token result | **ME** (numbers match) |
| A10 | Systima — https://systima.ai/blog/claude-code-vs-opencode-token-overhead | 12 Jul, older | Claude Code first call ~32,800 tokens (~24k tool schemas) vs OpenCode ~6,900 | CC 2.1.207, Sonnet 4.5 | No Pi tested; gateway envelope subtracted | V |
| A11 | Reddit r/LocalLLaMA — https://www.reddit.com/r/LocalLLaMA/comments/1v7d8px/harness_showdown_claude_code_vs_opencode_vs_pi/ | 26 Jul, older | Initial tokens: Pi 1,340, OpenCode 7,197, Claude Code 23,132 | Local DeepSeek | Community capture | V |
| A12 | Portkey — https://portkey.ai/blog/the-harness-tax/ | 13–17 Apr, older | ~27,000 vs 2,600 input tokens/request; short sessions 83,487 vs 8,650 | Model/version unstated | Trivial task; vendor | V |
| A13 | Execute Automation (YouTube) — https://www.youtube.com/watch?v=_u4PLnc13ME | 2 May, older | Local Gemma 4: ~113k vs ~15k tokens on two questions | Not Claude | Screen demo, no ledger | V transcript |
| A14 | Kaitchup (Benjamin Marie), Qwen3.8 27B — https://kaitchup.substack.com/p/qwen38-27b-for-long-horizon-agentic | 10 Sep, **in window** | Compares output tokens, total tokens, tool calls for Pi / Claude Code / Mini-SWE | Qwen3.8 27B | **Paywalled, tables unread**; do not cite numbers | S |

## Part B — references that qualify or contradict

| Source (URL) | Date / window | What it shows | Status |
|---|---|---|---|
| NTU "Finding the Right Fit", arXiv 2610.00917 — https://arxiv.org/abs/2610.00917 ; data https://huggingface.co/datasets/yixuanli97/finding-the-right-fit | Submitted 1 Oct, **in window** | Claude Opus 5, total cost at OpenRouter prices (Table 6): ALE-CLI Pi $323.34 (score 0.5022) vs Claude Code $570.21 (0.5428); TUA-Bench $70.28 (0.5821) vs $113.73 (0.6889); **Terminal-Bench 4 Pi $1,277.48 (0.3016) vs Claude Code $780.15 (0.4921)**. Pi 0.84.4 vs CC 2.1.251 (post-July prompt cut). Pi lower-scoring on all three. Text figures 119M vs 184M uncached input and 3,888 vs 4,472 calls are **Pi vs OpenHands**, not Claude Code | **ME** (table values and abstract) |
| NVIDIA SoL-Pi, arXiv 2609.20519 — https://arxiv.org/html/2609.20519v1 | 17 Sep, **in window** | Opus 5, EdgeBench: stock Pi 2.3697B tokens/$1,741/44.756 vs Claude Code 2.0045B/$2,535/43.689 (Pi +18% tokens, -31% cost). SoL-Pi Efficiency 1.3101B/$1,158/42.224. "+ObservationPack" Pi row: 1.4418B tokens, score 47.047 (cost cell garbled in my fetch; no dollar figure) | **ME** (table, ObservationPack row) |
| Composio DeepSeek Pro — https://composio.dev/content/pi-vs-opencode | 21 Aug, older | Pi 924,990 tokens/task, 16.3 turns vs Claude Code 649,900, 12.1 turns (Pi most tokens of six) | V |
| Bruce, task c and skills | 6 Sep, in window | Task c Pi 316k vs Claude Code 245k input (21 vs 8 turns); 48 skills raise Pi PONG from 1,358 to 10,787 | **ME** (task table) |
| Daniele warm-cost estimate | 18 May, older | Warm prefix ~$0.00312 CC vs ~$0.00310 Pi: Pi's 2,768-token prefix is under Haiku's 4,096 cache threshold | V |
| PointFive, arXiv 2608.01347 — https://arxiv.org/html/2608.01347v1 | Aug 2, older | Pi prefix 1,147–1,642 vs CC 15,983–20,330; native Sonnet 5 no-cache cost/success ~$0.027 vs $0.41 (billed Sonnet arm $8.81) | Preprint; small tasks; no-cache is not the invoice |
| capocasa GLM bench — https://capocasa.dev/10-task-glm-5-3-harness-bench-claude-opencode-pi-zcode-hermes-and-3code | 7 Sep, in window | Pi runner-up on tokens, 6/10 solved | Author flags a flawed setup; Low |
| AGI Hunt / zainhas — https://agihunt.info/en/p/1a0b81f919cf8a543f138991e73 | 19 Sep, in window | Kimi K3: Claude Code token-hungry, "Pi outputs a lot of tokens" | Chart unread; Low |
| Reddit context-mode — https://www.reddit.com/r/PiCodingAgent/comments/1ugk8hi/contextmode_is_adding_15k_tokens_to_every_request/ | 9 Jul, older | A Pi extension reportedly injects ~15k tokens | S |

## Part C — official and mechanism sources

- Zechner (30 Nov 2025): prompt+tools <1,000 tokens, four tools; score-only benchmark — https://mariozechner.at/posts/2025-11-30-pi-coding-agent/
- Pi 1.0.0 (1 Oct, in window): Codemode request ~5,300 → ~3,300 tokens (~40%, Pi vs older Pi); the 1.1–2.8k floor is **pre-1.0** — https://github.com/earendil-works/pi/releases/tag/v1.0.0
- The Register (2 Oct): Pi 1.0 adds MCP, Codemode, cache warming — https://www.theregister.com/ai-and-ml/2026/10/02/pi-coding-agent-pulls-a-180-and-adds-mcp-support/5300678
- pi.dev ("very token efficient", unquantified; MCP now built in) — https://pi.dev/ ; compaction — https://pi.dev/docs/latest/compaction
- Anthropic (24 Jul): >80% of Claude Code system prompt removed for Claude 5-gen models, prose only — https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models
- Anthropic (24 Sep): context/request +2.6×, cache-missing input -50% — https://claude.com/blog/claude-opus-5-5-built-for-coding-sessions-that-use-more-context
- Claude Code cost docs (MCP deferred; ~7× is agent teams in plan mode) — https://code.claude.com/docs/en/costs
- Ronacher (31 Jan): OpenClaw's engine is Pi, **OpenClaw ≠ Pi** — https://lucumr.pocoo.org/2026/1/31/pi/
- Harbor (3 Sep, in window), common evaluator for Pi and Claude Code, no savings result — https://arxiv.org/abs/2609.04298

## Part D — derivative / low reliability (kept for completeness)

Codearia write-up of Arena (secondary source for 27,011 vs 1,972 first-call means and Haiku row): https://academy.codearia.com/en/articles/harness-tax-claude-code-vs-codex-vs-pi · HN 49733726 (HarnessTax), 48837696 (Databricks), 48883275 (Systima) · Gigazine https://gigazine.net/gsc_news/en/20260917-harnesstax-ai-coding-agents/ · Towards AI https://pub.towardsai.net/claude-code-costs-2x-pi-longer-tasks-dont-fix-it-5c85f2cbdc64 · The Decoder / ai-tldr (SoL-Pi retellings) · note.com (retells Portkey) · **byteiota** https://byteiota.com/pi-coding-agent-minimal-harness/ (uninstrumented "900 vs 7–10k" claim, do not use for ratios) · opinion pieces (Dotzlaw, Urvil Joshi, Mejba, KSPL, InsiderLLM, Alex Dunlop, hillock, esc.sh, Cole Medin, Owain Lewis).

## Corrections made during the thread (do not reintroduce)

- 61k median tokens belongs to **Kimi Code**, not Pi (Composio 29 Jul thread had no Pi). Pi's figure is ~316k in the 4 Aug eight-harness run.
- OpenClaw's ~26k startup tax and 292k tokens/solved task are **not Pi's**. The New Stack's June benchmark has no stock Pi.
- NVIDIA and PointFive papers are **arXiv preprints, not peer-reviewed** (Kimi and Gemini overstated).
- Composio's ~7× cost/success is confounded by Claude Code's 1.5% cache share; do not call it token efficiency.
- Terminal-Bench 4 leaderboard: official page renders empty without JavaScript, so "Pi has no row" is **unverified**.
- PointFive compression study is July 2026 (10 Aug was a promotion); NVIDIA's 51 EdgeBench tasks split 11 acceptance / 40 final.

## Unresolved

- r/PiCodingAgent "Does Pi's minimalism actually pay off…" thread: never opened by any model; contents unknown.
- NTU dataset (6,204 runs): per-run input/cached/output tokens for Pi and Claude Code on Claude Opus 5 exist but **nobody has summed them**. This is the single most useful missing number. Doing it needs a dataset download (~`results/task_level.parquet`), which I have not done without your go-ahead.
- Arena raw traces unreleased; PointFive and Systima repos did not load; Kaitchup tables paywalled.
- Exact Claude Code release carrying the July prompt cut unidentified.
- No Pi 1.0 vs post-cut Claude Code run on a Claude model with full token categories.

## Process and model-quality notes

- Roster used in order: Sonnet 5.5, GPT-6.1 Sol, GLM 5.3, Kimi K3, Gemini 3.8 Flash, Grok 4.7 (Nemotron skipped). Unified answer and final synthesis by Grok. Cycle 1 = rounds 1–6 (plus 1b); unified = round 7; cycle 2 = rounds 8–13; final synthesis = round 14.
- Strongest contributions: Sol (found HarnessTax, NVIDIA, Databricks, PointFive, same-model Claude data), GLM (adjudicated the Register dispute, found NTU), Gemini (NTU dataset lead), Grok (corrected the Kimi Code/OpenClaw/preprint errors).
- Weak runs: Sonnet cycle-2 artifact truncated and wrongly rejected the Register figure; Kimi cycle-2 mirrored GLM's findings under a "GLM 5.3" header after an intro-only first reply; Gemini mislabeled the Pi-vs-OpenHands tokens as Claude Code's.
- Round 7's unified answer silently dropped several valid references; cycle 2 caught and restored them.
- Model agreement is not proof; items marked ME were checked by me against the live source.
