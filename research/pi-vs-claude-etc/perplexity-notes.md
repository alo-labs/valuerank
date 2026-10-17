# Perplexity task notes

Task: Exhaustively search and find references showing the Pi coding agent consumes much less tokens than Claude as of Sept–Oct 2026.

Roster available in picker (2026-10-08): Sonnet 5.5, GPT-6.1 Sol, GLM 5.3, Kimi K3, Gemini 3.8 Flash. Grok NOT offered (noted).
Working order: Sonnet 5.5 -> Sol 6.1 -> GLM 5.3 -> Kimi K3 -> Gemini 3.8 Flash.

Thread URL: https://www.perplexity.ai/search/814b6c66-eefc-44ed-bb93-62eff604919b
Browser: built-in browser, tab "seed". No attachments.
Workaround: composer submit arrow only activates after typing a real space key after execCommand insertText; first click on the mic/voice icon does nothing useful.

## Progress
- Round 1 + 1b (Sonnet 5.5): DONE, model explicitly closed ("no further material additions" except unreachable X/YouTube/full Reddit thread).
- Sol 6.1 (round 2): DONE. Said further additions remain only in inaccessible/raw data. Corrected Sonnet: same-model Claude comparisons DO exist.
- Grok 4.7 Thinking IS in picker once inside a thread (new-chat picker was shorter). Order: Sonnet, Sol, GLM, Kimi, Gemini, Grok(last).
- Next: GLM 5.3 (round 3), Kimi K3 (4), Gemini 3.8 Flash (5), Grok 4.7 (6) -> Grok unified answer -> 2nd cycle all models -> Grok final synthesis.
- Prompt builder: window.__mk(round, model) (page global; lost on reload). Template: "CROSS-MODEL REVIEW (round N; reviewer: M). Treat yourself as a NEW reviewer. Read the ENTIRE conversation..., research independently, verify sources, correct errors, add missing evidence, examine fixed-overhead vs whole-task, return COMPLETE revised master reference list (URL, date, claim, design, numbers, caveats, confidence, Sept-Oct vs older), state whether further additions remain, single answer."
- Submit trick: real click composer, ctrl+End, type ' ', then click arrow at ~(680,565).

- GLM 5.3 (round 3): DONE. Verified HarnessTax via arena.ai blog (published 16 Sep, updated 18 Sep): CC initial context >10x Pi; CC 2.0x/1.5x cost; Fable 5 97.8% vs 96.7%, $1.33 vs $0.67, 15.3 vs 15.4 turns. No Pi rows on Terminal-Bench 4.0 public leaderboard (Oct 6). Said more additions remain (Arena traces, inaccessible Reddit thread, repos).
- Kimi K3 (round 4): DONE. New: Composio Kimi K3 X threads (Jul 29/31) + blog Aug 4: avg cost/task Pi $0.40 vs CC $1.47 (3.7x), Pi fastest, 'Pi used fewest tokens' (no Pi token number given; CC median 340k); capocasa GLM 5.3 bench (Sep 7; Pi runner-up on tokens, 6/10 solved); AGI Hunt K3 bench (Sep 19); Harbor arXiv 2609.04298; Melissa Pan X Sep 16. CAUTION: Kimi called NVIDIA paper 'peer-reviewed' - it is arXiv preprint. Kimi's claims not verified by me.
- Gemini 3.8 Flash (round 5): DONE; closed explicitly. Errors found by me/Grok: attributed Kimi Code's 61k median to Pi; described unread Reddit thread; treated OpenClaw as Pi; 'peer-reviewed'.
- Grok 4.7 (round 6): DONE. Verified corrections: 61k = Kimi Code (Pi ~316k tokens/task, Composio Aug 4 K3 blog, composio.dev/content/best-ai-agent-harnesses); OpenClaw = product built on Pi (Ronacher 2026-01-31), startup tax ~26k, 292k/solved task is OpenClaw not Pi; arXiv preprints.
- Grok unified answer (round 7): DONE. In same thread, last message. DROPPED some valid refs (Harbor arXiv 2609.04298, AGI Hunt Sep 19 bench, The Register Oct 2, Codearia, HN items, byteiota unreliable flag, Reddit registry) -> raise in cycle 2.
- CYCLE 2 (review unified answer, complete revised artifact, each model): Sonnet (r8) -> Sol (r9) -> GLM (r10) -> Kimi (r11) -> Gemini (r12) -> Grok (r13) -> Grok final synthesis (r14).
- Cycle 2 progress:
  - r8 Sonnet DONE (6m18s; artifact truncated mid-table, findings complete). Findings accepted for final synthesis: (C1) Composio DeepSeek Flash 7x cost is mostly cache effect (CC drew only 1.5% of input from cache vs ~57-70% others per New Stack); (C2) Terminal-Bench 'no Pi row' unverified (tbench.ai JS-only), drop 8.0B/19.4B figures or mark carried; (C3) Databricks 742k/237k per-task press numbers only in aggregator kblip, not Register - rate low-moderate; Arena 2.0x is cross-model geomean; per-model Haiku 4.5 = 1.14x ($0.426/52.2% vs $0.374/60.0%), Fable 5 2.0x; Pi 1.0+Codemode request ~3.3k not 1.1-2.8k; AGI Hunt (zainhas X Sep 19: CC token hungry, Pi outputs a lot of tokens); capocasa self-flagged setup flaw (low); New Stack read in full: no Pi in the June 12-config benchmark; Aug 4 Composio blog author is Sunil Kumar Dash (not Shrijal); Harbor has no token results; restore dropped refs with V/S/C verification codes.
  - r9 Sol DONE. ADJUDICATION: The Register DOES report 742,000 vs 236,999 (Sonnet r8 was wrong on that); confirmed Composio Flash 1.5% CC cache share (Pi's share not given), Haiku 0.426 vs 0.374, Pi1.0 ~3.3k request, capocasa flaw, New Stack June exp has no stock Pi (EuropeSays English republication, Janakiram MSV). NEW: NVIDIA ObservationPack-only Pi 1.4418B @47.047 vs CC 2.0045B @43.689 (-28%, Pi extension). Corrections: 'plan mode 7x' is actually agent teams in plan mode; PointFive study dated July (promo Aug 10); NVIDIA 51 tasks = 11 acceptance + 40 final; Arena TB board unverifiable (empty table) -> don't claim Pi absent; Composio authors: Sunil Kumar Dash (Aug benchmark articles), Shrijal (two Pi comparison articles); distinguish cost denominators; two-dimension confidence (source verification vs evidentiary strength). Readiness: qualified evidence review, not exhaustive.
  - r10 GLM DONE (3m15s). Adjudicated Register: Sol right (verbatim: 742,000 vs 236,999 context tokens/task, ~3.2x; Codex 1,235,000 vs Pi 665,000; Zaharia '2x less cost'). NEW study: NTU 'Finding the Right Fit: Model-Harness Interactions across Agent Tasks' arXiv 2610.00917 (submitted Oct 1 2026; Pi 0.84.4 vs Claude Code 2.1.251; OpenHands/DSH/Pi/openJiuwen; 66 configs; Claude Opus 5 36/63 via OpenHands vs 19/63 via Pi on TB4; GPT-6 Astra via Pi $293.30/60.32% vs DSH $1,256.48/52.38%) - I VERIFIED existence/abstract via arXiv abs. GLM said ObservationPack row unconfirmed -> I VERIFIED row exists in NVIDIA Table 4: '+ObservationPack' Opus 5 = 1.4418B tokens, score 47.047 (cost cell garbled '$1.3960', probably $1,396; Sol/GLM quoted $1,176 - unresolved, omit cost).
  - r11 Kimi DONE after re-prompt (first reply intro-only; composer model had silently reset to Sonnet - reselected Kimi). Output mislabeled '(GLM 5.3)' and mirrored GLM's findings; no new evidence; still called ObservationPack numbers unverified despite my note. LOW independence/value. No per-harness NTU token ledger found.
  - r12 Gemini DONE (13s research, 24k chars). Valuable: NTU details + HF dataset lead (huggingface.co/datasets/yixuanli97/finding-the-right-fit: 6,204 scored runs; columns model_calls,input_tokens,cached_tokens,output_tokens,cost_usd (OpenRouter prices); harnesses OpenHands,DSH,PI,openJiuwen,Codex,Claude Code; models Opus 5, GPT-6 Astra, GLM-5.3, Kimi K3, DeepSeek V4 Pro; results/task_level.parquet). Gemini mislabeled: 119M/184M uncached input & $323/$498 are Pi vs OpenHands, NOT Claude Code.
  - MY VERIFIED NTU (arXiv 2610.00917, Table 6, Claude Opus 5, total cost; scores): ALE-CLI(99): Pi $323.34 (0.5022) vs CC $570.21 (0.5428) vs OpenHands $498.26, DSH $352.20, openJiuwen $484.45. TUA-Bench(120): Pi $70.28 (0.5821) vs CC $113.73 (0.6889). TB4(63): Pi $1,277.48 (0.3016) vs CC $780.15 (0.4921) -> Pi MORE expensive on TB4. Token-level Pi-vs-CC not tabulated in text (Appendix C figures; parquet has it). Pi 0.84.4 / CC 2.1.251. Aggregating the parquet would require downloading -> OFFER to user, not done.
  - r13 Grok DONE: consolidated; new: Kaitchup/Benjamin Marie Qwen3.8 27B Sep 10 (paywalled, unread). r14 Grok FINAL SYNTHESIS DONE (22k chars).
  - STATUS: COMPLETE. Deliverable: 2026-10-08-pi-vs-claude-token-references.md (same folder). Open offer to user: sum NTU HF parquet token columns (needs download permission).

## Sol round 2 key new evidence (my verification status)
- NVIDIA SoL-Pi arXiv 2609.20519 (2026-09-17) Table 2 Opus 5: CC 2.0045B tokens/$2,535; stock Pi 2.3697B/$1,741 -> Pi MORE tokens, LOWER cost. VERIFIED by me via WebFetch.
- HarnessTax (UC Berkeley/Arena, Sep 16 2026, harnesstax.github.io): CC initial context >10x Pi; CC cost ~2.0x Pi SWE-bench Lite, 1.5x Terminal-Bench 2.0 (geomean). NOT verified by me (JS page).
- Databricks 2026-07-08: Pi ~3x less context/turn, >2x cost diff same model; Register: Opus 4.8 742k vs 237k tokens/task (older than Sept).
- PointFive arXiv 2608.01347 (Aug 2): Pi prefix 1.1-1.6k vs CC 16-20k; Sonnet 5 native $0.027 vs $0.41/success.
- Composio Flash & heyuan110 numbers VERIFIED by me via WebFetch.
- Pi 1.0 (Oct 1-2): MCP+Codemode now built in; ~40% fewer prompt tokens vs older Pi.
- c-daniele: same Haiku 4.5; warm-prefix cost ~equal (Pi prefix below cache threshold).

## Sonnet round 1 key findings (citations to verify)
- Fixed overhead: Pi ~1.4-2.8k tokens vs Claude Code ~20-32k (heyuan110 2026-09-06: 1,358 vs 31,012 PONG; Pi 10,787 with 48 skills; different models).
- Whole-task: NOT consistently lower. Composio Pi vs CC (2026-09-04, DeepSeek V4 Flash): Pi 558,885 vs CC 741,659 tokens/task (-25%), cost/success $0.028 vs $0.195. Composio Pi vs OpenCode (2026-08-21, DeepSeek V4 Pro): Pi 924,990, OpenCode 710,140, CC 649,900 (Pi MORE).
- Systima 2026-07-12: CC 2.1.207 ~32.8k first turn vs OpenCode 6.9k (no Pi).
- No same-model Claude comparison of Pi vs CC found.
- Anthropic cut CC system prompt >80% for Claude 5-gen (2026-07-24) - vendor claim.

## Source URLs seen
https://mariozechner.at/posts/2025-11-30-pi-coding-agent/
https://pi.dev/
https://www.heyuan110.com/posts/ai/2026-09-06-pi-coding-agent-review/
https://composio.dev/content/pi-agent-vs-claude-code
https://composio.dev/content/pi-vs-opencode
https://c-daniele.github.io/en/posts/2026-05-18-coding-harness-comparison/
https://note.com/snake_dragon/n/ndacf0867110e
https://www.reddit.com/r/LocalLLM/comments/1t40xz2/is_migrating_over_to_pi_excessive_for_token/
https://insiderllm.com/guides/claude-code-vs-pi-agent-local-ai/
https://pi.dev/docs/latest/compaction
https://dotzlaw.com/insights/claude-code-10-pi-comparison/
https://www.reddit.com/r/PiCodingAgent/comments/1u3nsh8/does_pis_minimalism_actually_pay_off_on/
http://ai-tldr.dev/tools/sol-pi/
https://the-decoder.com/nvidias-sol-pi-system-cuts-coding-agent-token-usage-nearly-in-half-by-optimizing-the-harness/
https://www.developersdigest.tech/blog/pi-1-0-release-guide-mcp-codemode-pi-durable
https://systima.ai/blog/claude-code-vs-opencode-token-overhead
https://www.digitaltoday.co.kr/en/view/81376/claude-code-sends-33000-tokens-before-questions-in-real-use-up-to-75000
https://github.com/earendil-works/pi/issues/3372
https://github.com/earendil-works/pi/issues/6057
https://claude.com/resources/articles/claude-opus-5-5-built-for-coding-sessions-that-use-more-context

## Prompt template (round 1)
RESEARCH REQUEST (round 1; model: Claude Sonnet 5.5). Task: Exhaustively search for and list references (primary sources preferred: GitHub repos and issues, official docs, benchmark reports, blog posts, X/Reddit/HN threads, YouTube, papers) showing that the Pi coding agent (the minimal terminal coding agent "pi" / pi-coding-agent by Mario Zechner, badlogic/pi-mono, shittycodingagent.ai) consumes much fewer tokens than Claude (Claude Code and/or Claude models) as of September-October 2026. For each reference give: URL, title, author, publication date, the exact quantitative or qualitative claim, what is compared (Pi vs Claude Code, same or different underlying model, task type, tokens in/out/cached, cost), method and reproducibility, and your confidence. Explain the mechanisms cited (e.g. tiny system prompt, few tools, no MCP overhead, no subagents/plan mode, caching). Distinguish evidence from assumptions, flag conflicts, and also include any credible counter-evidence where Pi uses equal or more tokens, plus reports that are older than September 2026 (label them). Cite sources for every factual claim, flag uncertainties, and return the complete answer in a single response.
