# Coding Agent ValueRank — Raw Data
**Updated every version | Primary data collection file**

← [README](README.md) · [Methodology](methodology.md) · [Scores](scores.md)

---

## §1. Agent Inventory

| # | Agent | Base Model | Developer | Type | Deployment | Version/Date |
|---|---|---|---|---|---|---|
| 1 | Codex | GPT-5.5 | OpenAI | Commercial | Cloud SaaS / CLI | Apr 2026 |
| 2 | ForgeCode | GPT-5.4 | Antinomy (antinomyhq) | Commercial (open-source agent) | CLI / API | Mar 2026 |
| 3 | TongAgents | Gemini 3.1 Pro | ByteDance SE Lab | Research | Internal | Mar 2026 |
| 4 | ForgeCode | Claude Opus 4.6 | Antinomy | Commercial | CLI / API | Mar 2026 |
| 5 | SageAgent | GPT-5.3-Codex | Unknown | Unknown | Unknown | Mar 2026 |
| 6 | ForgeCode | Gemini 3.1 Pro | Antinomy | Commercial | CLI / API | Mar 2026 |
| 7 | Factory Droid | GPT-5.3-Codex | Factory AI | Commercial | Cloud SaaS | Feb 2026 |
| 8 | Junie CLI | Multiple | JetBrains | Commercial | CLI / IDE | Mar 2026 |
| 9 | Factory Droid | Claude Opus 4.6 | Factory AI | Commercial | Cloud SaaS | Feb 2026 |
| 10 | Augment Code (Auggie) | Claude Opus 4.6 | Augment | Commercial | IDE extension | 2025–2026 |
| 11 | OpenHands CodeAct v3 | Claude Opus 4.6 | All Hands AI | Open Source | Cloud / Self-hosted | 2025 |
| 12 | Amazon Q Developer | Proprietary | Amazon (AWS) | Commercial | Cloud SaaS / IDE | Apr 2025 ver. |
| 13 | Cursor Background Agent | Claude Sonnet 4.6 | Anysphere | Commercial | IDE (Cursor) | 2025–2026 |
| 14 | Composio SWE-Kit | Claude Sonnet 4.6 | Composio | Commercial | Cloud / API | 2025–2026 |
| 15 | Cline | Claude Sonnet 4.6 | Community (saoudrizwan) | Open Source | VS Code extension | 2025–2026 |
| 16 | Devin 2.0 | Proprietary | Cognition AI | Commercial | Cloud SaaS | 2025 |
| 17 | SWE-agent v1 | Claude Sonnet 4.5 | Princeton NLP | Research | CLI (open-source) | 2025 |
| 18 | AutoCodeRover v2 | GPT-5.2 | NUS (Singapore) | Research | CLI (open-source) | 2024–2025 |
| 19 | Agentless v2 | Claude Sonnet 4.5 | Academic | Research | Open-source | 2025 |
| 20 | Aider (architect mode) | Claude Sonnet 4.5 | Community (paul-gauthier) | Open Source | CLI | 2025 |
| 21 | Claude Code | Claude Opus 4.6 | Anthropic | Commercial | CLI | Feb 2026 |
| 22 | OpenHands CodeAct v2 | Claude Opus 4.5 | All Hands AI | Open Source | Cloud / Self-hosted | 2025 |

**Notes:**
- Entries 1–9 appear primarily on Terminal-Bench 2.0.
- Entries 10–22 appear primarily on SWE-bench Verified.
- ForgeCode appears three times (entries 2, 4, 6) with different base models — each is a distinct product configuration.
- Factory Droid appears twice (entries 7, 9). Entry 7 has cross-benchmark data; entry 9 is TB2.0-only.
- OpenHands appears twice: CodeAct v3 + Opus 4.6 (SWE-V data) and CodeAct v2 + Opus 4.5 (TB2.0 + SWE-V).
- TongAgents (ByteDance SE Lab): limited public information; appears on TB2.0 leaderboard with confirmed score.
- SageAgent: no confirmed developer or public product page; confirmed TB2.0 leaderboard entry only.
- Amazon Q Developer: "Proprietary" model = AWS in-house model, not a public API model.

---

## §2. Dimension 1: Terminal-Bench 2.0 (Primary Signal)

**Leaderboard:** tbench.ai/leaderboard/terminal-bench/2.0
**Tasks:** 89 tasks — software engineering, biology, security, gaming; Docker containers; time-based execution
**Evaluation:** Automated correctness check via human-written solutions
**Submissions:** 124 total as of April 27, 2026 (post-integrity update)
**Integrity update (April 19, 2026):** Two agents permanently removed (OB-1/OpenBlock, Pilot/QuantFlow) for cheating. ForgeCode retained but specific trials zeroed for reward hacking. Current scores are post-correction. See limitations.md §14.3.

| (Agent + Model) | TB2.0 Score | Date | Source | Notes |
|---|---|---|---|---|
| Codex + GPT-5.5 | **82.0%** ±2.2 | 2026-04-23 | tbench.ai | New #1 post-integrity update |
| ForgeCode + GPT-5.4 | **81.8%** ±2.0 | 2026-03-12 | tbench.ai | Post-correction score; reward hacking caveat resolved |
| TongAgents + Gemini 3.1 Pro | **80.2%** ±2.6 | 2026-03-13 | tbench.ai | ByteDance SE Lab |
| ForgeCode + Claude Opus 4.6 | **79.8%** ±1.6 | 2026-03-12 | tbench.ai | Post-correction score |
| SageAgent + GPT-5.3-Codex | **78.4%** ±2.2 | 2026-03-13 | tbench.ai | No confirmed developer identity |
| ForgeCode + Gemini 3.1 Pro | **78.4%** ±1.8 | 2026-03-02 | tbench.ai | Post-correction score |
| Factory Droid + GPT-5.3-Codex | **77.3%** ±2.2 | 2026-02-24 | tbench.ai | |
| Junie CLI + Multiple | **71.0%** ±2.9 | 2026-03-07 | tbench.ai | JetBrains; multiple base models |
| Factory Droid + Claude Opus 4.6 | **69.9%** ±2.5 | 2026-02-05 | tbench.ai | |
| Claude Code + Claude Opus 4.6 | **58.0%** ±2.9 | 2026-02-07 | tbench.ai | Rank 40/124 |
| OpenHands + Claude Opus 4.5 | **51.9%** ±2.9 | 2026-01 | tbench.ai | Rank 51/124 |

**Not on TB2.0 leaderboard (confirmed absence):** Augment Code, Cursor Background Agent, Composio SWE-Kit, Cline, Devin 2.0, SWE-agent, AutoCodeRover, Agentless, Aider.

**Scaffold engineering premium:** ForgeCode's Gemini 3.1 Pro entry (78.4%) vs. Google's direct Gemini 3.1 Pro submission (~68.5%) shows a ~10 pp scaffold advantage. The same model produces very different results depending on the agent wrapping it.

---

## §3. Dimension 2: SWE-bench Verified (Secondary Signal)

**Leaderboard:** swebench.com/verified.html
**Tasks:** 500 human-validated GitHub issue resolution tasks; Python repositories
**Evaluation:** Fail-to-pass test execution after agent-submitted patch
**Submissions:** 100+ total as of April 2026
**Contamination notice (2025):** OpenAI confirmed training data leakage in frontier models. Scores above ~65% on SWE-bench Verified should be interpreted with caution. SWE-bench Pro (see §4, reserved) is the recommended successor. See limitations.md §14.1.

**Source for agent-level rankings:** awesomeagents.ai/leaderboards/swe-bench-coding-agent-leaderboard/ (April 2026)

| (Agent + Model) | SWE-V Score | Date | Source | Notes |
|---|---|---|---|---|
| Augment Code + Claude Opus 4.6 | **72.0%** | 2025–2026 | awesomeagents.ai | Best unassisted pass@1 with custom scaffold |
| OpenHands CodeAct v3 + Claude Opus 4.6 | **68.4%** | 2025 | awesomeagents.ai | Open-source SOTA; CodeAct framework |
| Amazon Q Developer + Proprietary | **66.0%** | Apr 2025† | awesomeagents.ai | Peak score; exact model version unspecified |
| Cursor Background Agent + Claude Sonnet 4.6 | **65.7%** | 2025–2026 | awesomeagents.ai | IDE-integrated autonomous mode |
| Composio SWE-Kit + Claude Sonnet 4.6 | **62.3%** | 2025–2026 | awesomeagents.ai | |
| Cline + Claude Sonnet 4.6 | **59.8%** | 2025–2026 | awesomeagents.ai | Open-source VS Code extension |
| Factory Droid + GPT-5.3-Codex | **58.1%** ~ | 2025–2026 | 3rd-party aggregator | Cross-benchmark entry; ~ secondary source |
| Devin 2.0 + Proprietary | **45.8%** | 2025 | cognition.ai/blog | Unassisted; older baseline post–2024 launch |
| OpenHands CodeAct v2 + Claude Opus 4.5 | **44.7%** ~ | 2025 | 3rd-party aggregator | Earlier OpenHands version |
| SWE-agent v1 + Claude Sonnet 4.5 | **43.2%** | 2025 | awesomeagents.ai | Princeton open-source agent |
| AutoCodeRover v2 + GPT-5.2 | **38.6%** | 2025 | awesomeagents.ai | Program-structure-aware agent |
| Agentless v2 + Claude Sonnet 4.5 | **34.2%** | 2025 | awesomeagents.ai | No iteration loop; localize-repair-validate |
| Aider (architect mode) + Claude Sonnet 4.5 | **31.4%** | 2025 | swebench.com | Community CLI agent |

**Not on SWE-V agent leaderboard (confirmed or probable absence):** ForgeCode (all three entries), TongAgents, SageAgent, Junie CLI.

**Notes:**
- **†** Amazon Q Developer's 66.0% reflects an April 2025 update; the original 2024 submissions scored 38.8% (v20240719) and 25.6% (v20240430). Model version for the 66% submission not confirmed publicly.
- **~** Secondary source: not verified from the primary swebench.com leaderboard directly.
- Droid + GPT-5.3-Codex SWE-V score (58.1%~): appears on third-party aggregator; the Factory Droid technical report does not detail this specific SWE-V submission.

---

## §4. Dimension 3: SWE-bench Pro (Reserved — Pending Activation)

**Leaderboard:** labs.scale.com/leaderboard/swe_bench_pro_public
**Tasks:** 1,865 tasks across Python, Go, TypeScript, JavaScript (41 repos); contamination-resistant
**Status:** Reserved pending ≥4 cohort entries. Reference data collected below.
**Activation expected:** v2.0, when Augment Code, Amazon Q, OpenHands, and SWE-agent entries are confirmed (≥4 threshold).

| (Agent + Model) | SWE-Pro Score | Date | Source | Notes |
|---|---|---|---|---|
| Augment Code (Auggie) + Claude Opus 4.6 | **~51.8%** ~ | 2026 | augmentcode.com/blog | Blog-reported; tops Pro leaderboard; awaiting primary leaderboard confirmation |
| Amazon Q Developer + Proprietary | **28.8%** | 2025-09-18 | amazon-science SWE-PolyBench | Confirmed in SWE-PolyBench evaluation |
| GPT-5.3-Codex (standardized scaffold) | **56.8%** | 2026 | labs.scale.com | Model-level SEAL standardized run, not a named commercial agent |
| Claude Opus 4.5 (SEAL standardized) | **45.9%** | 2025 | labs.scale.com | Model-level standardized run |

*Note: Most SWE-bench Pro entries use standardized scaffolds (SEAL methodology), making them model-level rather than agent-scaffold-level. Named commercial agent systems (Augment Code, Amazon Q) have submitted custom agents. Await ≥4 custom-agent submissions for dimension activation.*

---

## §5. Dimension 4: SWE-bench Multilingual (Reserved — Pending Activation)

**Leaderboard:** swebench.com/multilingual-leaderboard.html
**Tasks:** 300 tasks across 9 languages (C, C++, Go, Java, JS/TS, PHP, Ruby, Rust)
**Status:** Reserved. ~24 entries on the leaderboard but most appear to be model-via-standardized-scaffold, not named commercial agents.
**Reference data:**

| Entry | SWE-ML Score | Notes |
|---|---|---|
| Claude Mythos Preview | 87.3% | Model-level; not a named commercial agent |
| SWE-agent + Claude 3.7 Sonnet | ~43% | Research agent; prior-generation model |

*No cohort (agent, model) pairs confirmed on SWE-ML as of April 2026. Will activate when ≥4 cohort agents submit.*

---

## §6. Dimension 5: Multi-SWE-bench (Reserved — Pending Activation)

**Leaderboard:** multi-swe-bench.github.io / HuggingFace
**Tasks:** 1,632 instances across Java, TypeScript, JavaScript, Go, Rust, C, C++ (7 languages)
**Status:** Reserved. Growing leaderboard, but no cohort agents confirmed as of April 2026.
**Reference data:**

| Entry | Language | Score | Notes |
|---|---|---|---|
| IBM iSWE-Agent + Claude 4.5 Sonnet | Java | 33% | IBM Research; not in cohort |
| Gemini 2.5 Pro (prior best) | Java | 28.9% | Model-level |

---

## §7. Cost — Reference Only (Not Scored in v1.0)

Cost is tracked as orientation data. Will activate as a scored dimension when ≥4 cohort pairs report per-task cost.

**Cost methodology:** Cost per resolved SWE-bench issue = (average tokens consumed per run) × (API price per MTok). For agent harnesses, this is substantially higher than single-call model benchmarks due to multi-turn tool use, file reads, and shell executions.

| Source | Cost Signal | Notes |
|---|---|---|
| SWE-rebench (standardized scaffold) | $0.62–$1.12 per issue | Contamination-controlled; frontier models Feb–Mar 2026 |
| Sonar Foundation Agent | ~$1.90 per issue | Self-reported; Claude Opus 4.5 based; confirmed SWE-bench Verified 79.2% |
| AutoCodeRover (original) | ~$0.70 per task | Research paper; GPT-4o; 2024 |
| HAL Princeton | Tracked per benchmark run | Most comprehensive cost tracker; benchmark-specific rates |
| Devin 1.0 (launch) | $500/seat/month | Per-seat, not per-task; dropped to $20/month entry tier by 2025 |
| Claude Code | $100–$200/month Max plan | Per-seat subscription; includes raw API cost pass-through |
| OpenHands, Aider, Cline, ForgeCode, SWE-agent | BYOK (bring your own key) | No agent surcharge; user pays API cost directly |

**Observation:** BYOK agents (OpenHands, Aider, ForgeCode, Cline, SWE-agent) have zero agent overhead cost — all expense is API tokens. This makes per-task cost fully determined by base model pricing and token efficiency of the scaffold. Commercial agents (Devin, Cursor, Augment) add a platform surcharge on top of API cost.

---

## §8. Supplementary: SWE-rebench Data (Reference, Not Scored)

SWE-rebench uses a standardized 128K-context ReAct scaffold — identical for all submissions — making it a model-capability benchmark rather than an agent scaffold benchmark. It does not differentiate between different agents using the same base model.

**SWE-rebench top 5 (as of March 2026, standardized scaffold, 57 tasks):**

| Rank | Model | Resolved (Pass@1) | Pass@5 | Cost/Issue |
|---|---|---|---|---|
| 1 | Claude Opus 4.6 | 65.3% | 70.2% | $1.12 |
| 2 | GPT-5.2-medium | 64.4% | 73.7% | $0.62 |
| 3 | GLM-5 | 62.8% | 70.2% | $0.76 |
| 4 | GPT-5.4-medium | 62.8% | 70.2% | $0.63 |
| 5 | GLM-5.1 | 62.7% | 71.9% | $0.76 |

*The 65.3% top score here vs. 80%+ on SWE-bench Verified for the same model is strong evidence of contamination in SWE-bench Verified frontier scores.*

---

## §9. Benchmark Reference Index

| Benchmark | URL | Type | Coding-Specific | Agent-Level | Active Leaderboard |
|---|---|---|---|---|---|
| Terminal-Bench 2.0 | tbench.ai | CLI/terminal tasks | Yes | Yes | Yes (124 entries) |
| SWE-bench Verified | swebench.com/verified | Repo issue resolution | Yes (Python) | Yes | Yes (100+ entries) |
| SWE-bench Pro | labs.scale.com | Repo issue resolution | Yes (multi-lang) | Yes | Yes (~30 entries) |
| SWE-bench Multilingual | swebench.com/multilingual | Repo issue resolution | Yes (9 languages) | Yes | Yes (24 entries) |
| Multi-SWE-bench | multi-swe-bench.github.io | Repo issue resolution | Yes (7 languages) | Yes | Yes (growing) |
| SWE-rebench | swe-rebench.com | Repo issue resolution | Yes (Python) | Model-only scaffold | Yes (15+ entries) |
| MLE-bench | mlebench.com | ML engineering | Yes (ML/Python) | Yes | Frozen (Apr 2026) |
| FeatureBench | github.com/LiberCoders/FeatureBench | Feature development | Yes (Python) | Yes | Paper-only |
| DevOps-Gym | devops-gym.com | DevOps/CI/CD tasks | Yes (Java, Go) | Yes | Paper-only |
| Aider Polyglot | aider.chat/docs/leaderboards | Code editing (6 langs) | Yes | Model-only | Yes (22+ entries) |
| GAIA | huggingface.co/spaces/gaia-benchmark | General assistant | ~30% coding | Yes | Yes |
| PR Arena | prarena.ai | Real-world PRs | Yes | Yes | Live (real-time) |
| Commit-0 | commit-0.github.io | From-scratch generation | Yes (Python) | Yes | Stale (Nov 2024) |
| SWE-EVO | github.com/SWE-EVO | Long-horizon evolution | Yes (Python) | Yes | Paper-only |
