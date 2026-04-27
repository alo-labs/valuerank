# Coding Agent ValueRank — v1.0
**April 27, 2026 | 22 entries | 2 active benchmark lists**

---

## Document Index

| File | Contents |
|---|---|
| **README.md** ← you are here | Overview, ranking snapshots, executive summary |
| [methodology.md](methodology.md) | Normalization formula, two-list approach, activation protocol |
| [scores.md](scores.md) | TB2.0 and SWE-V ranked lists with derivation tables, Pareto frontier |
| [raw-data.md](raw-data.md) | All raw benchmark data, agent inventory, source citations |
| [profiles.md](profiles.md) | Full profiles for all 22 (agent, model) pairs |
| [insights.md](insights.md) | Strategic findings, Pareto analysis, scaffold premium, capability cliff |
| [limitations.md](limitations.md) | Known gaps, data caveats, benchmark integrity reference |
| [benchmarks.md](benchmarks.md) | Benchmark landscape: all evaluated benchmarks, classification, activation status |
| [research.md](research.md) | Research provenance, source verification, confidence classification |

---

## Executive Summary

Coding Agent ValueRank v1.0 publishes **two separate ranked lists** — one for Terminal-Bench 2.0, one for SWE-bench Verified — rather than a composite score. The data does not support merging them: of 22 cohort entries, only Factory Droid + GPT-5.3-Codex has real scores on both benchmarks (and even that SWE-V score is from a secondary source). The two leaderboards attract entirely different agent populations testing entirely different capabilities. Combining them into a single number would encode a weight-based preference as if it were an empirical finding.

**TB2.0** tests terminal-native autonomy across 89 tasks: software engineering, biology, security, and gaming in live Docker containers with time-based execution. Its top agents are CLI-first systems built for long-running process management and system-level work. **SWE-bench Verified** tests GitHub issue resolution across 500 Python repository tasks. Its top agents are code-repair specialists tuned for structured file editing and test execution.

The single most actionable empirical finding: **scaffold engineering accounts for ~10 percentage points of performance at the frontier**, independent of base model. ForgeCode + Gemini 3.1 Pro scores 78.4% on TB2.0 while Google's own direct Gemini 3.1 Pro submission scores ~68.5% on the same benchmark — same model weights, different scaffold. On SWE-V, Claude Opus 4.6 scores 72.0% inside Augment Code's scaffold and 68.4% inside OpenHands'. Model capability is necessary but not sufficient.

A second critical finding: **current benchmark scores systematically overstate real-world capability on complex tasks**. Three research benchmarks (FeatureBench, DevOps-Gym, SWE-EVO) document a long-horizon capability cliff — the same agents scoring 65–74% on SWE-V score 11–25% on multi-file feature development and sustained software evolution. No publicly ranked agent has demonstrated adequate performance on "implement this 3-week feature across 15 files."

---

## TB2.0 Ranking (11 entries)

*Terminal-native agents — CLI/Docker environments, multi-step system tasks*

| Rank | (Agent + Model) | Developer | TB2.0 Score |
|---|---|---|---|
| 🥇 1 | **Codex + GPT-5.5** | OpenAI | 82.0% |
| 🥈 2 | **ForgeCode + GPT-5.4†** | Antinomy | 81.8% |
| 🥉 3 | **TongAgents + Gemini 3.1 Pro** | ByteDance SE Lab | 80.2% |
| 4 | ForgeCode + Claude Opus 4.6† | Antinomy | 79.8% |
| 5–6 | SageAgent + GPT-5.3-Codex | Unknown | 78.4% |
| 5–6 | ForgeCode + Gemini 3.1 Pro† | Antinomy | 78.4% |
| 7 | Factory Droid + GPT-5.3-Codex | Factory AI | 77.3% |
| 8 | Junie CLI + Multiple | JetBrains | 71.0% |
| 9 | Factory Droid + Claude Opus 4.6 | Factory AI | 69.9% |
| 10 | Claude Code + Claude Opus 4.6 | Anthropic | 58.0% |
| 11 | OpenHands v2 + Claude Opus 4.5 | All Hands AI | 51.9% |

**†** Post-correction scores per tbench.ai's April 19, 2026 integrity ruling (reward hacking classification). **Note:** Ranks 1–7 have overlapping confidence intervals and are statistically indistinguishable at 1σ.

---

## SWE-V Ranking (13 entries)

*Code-repair agents — GitHub issue resolution, Python repositories*

| Rank | (Agent + Model) | Developer | SWE-V Score |
|---|---|---|---|
| 🥇 1 | **Augment Code + Claude Opus 4.6** | Augment | 72.0%~ |
| 🥈 2 | **OpenHands v3 + Claude Opus 4.6** | All Hands AI | 68.4%~ |
| 🥉 3 | **Amazon Q Developer + Proprietary†** | Amazon | 66.0%~ |
| 4 | Cursor Background Agent + Sonnet 4.6 | Anysphere | 65.7%~ |
| 5 | Composio SWE-Kit + Sonnet 4.6 | Composio | 62.3%~ |
| 6 | Cline + Claude Sonnet 4.6 | Community | 59.8%~ |
| 7 | Factory Droid + GPT-5.3-Codex | Factory AI | 58.1%~ |
| 8 | Devin 2.0 + Proprietary | Cognition AI | 45.8% |
| 9 | OpenHands v2 + Claude Opus 4.5 | All Hands AI | 44.7%~ |
| 10 | SWE-agent v1 + Claude Sonnet 4.5 | Princeton | 43.2%~ |
| 11 | AutoCodeRover v2 + GPT-5.2 | NUS | 38.6%~ |
| 12 | Agentless v2 + Claude Sonnet 4.5 | Academic | 34.2%~ |
| 13 | Aider + Claude Sonnet 4.5 | Community | 31.4% |

**~** Score from awesomeagents.ai (third-party aggregator) — secondary source. Primary leaderboard is swebench.com/verified.html. Only Devin 2.0 (cognition.ai/blog) and Aider (swebench.com) have primary-source scores. **†** Amazon Q: April 2025 version; model identity unspecified.

---

## Cross-Benchmark Pareto Frontier

The most honest cross-benchmark statement the data supports. Three entries are not dominated:

| (Agent + Model) | TB2.0 | SWE-V | Status |
|---|---|---|---|
| **Codex + GPT-5.5** | 82.0% | — | **✓ Frontier** — TB2.0 leader |
| **Augment Code + Claude Opus 4.6** | — | 72.0%~ | **✓ Frontier** — SWE-V leader |
| **Factory Droid + GPT-5.3-Codex** | 77.3% | 58.1%~ | **✓~ Frontier** — only dual-benchmark entry |

All other entries are dominated on at least one axis by one of these three. Selection rule: TB2.0 work → Codex. SWE-V work → Augment Code. Both → Factory Droid (monitor for primary-source SWE-V confirmation).

---

## Methodology Summary

Two separate ranked lists. No composite score.

**Scoring formula** (within each list): `Score = ((n − rank) / (n − 1)) × 100`

Missing data = neutral **50⊘**. Tied ranks receive the average of their tied positions.

**Active benchmarks:**

| Benchmark | n | Leaderboard |
|---|---|---|
| Terminal-Bench 2.0 | 11 entries | tbench.ai |
| SWE-bench Verified | 13 entries | swebench.com/verified |

**Ranking unit:** (agent, model) pairs — the same scaffold with a different base model is a distinct entry. Pure autonomous agents only.

**Why no composite:** TB2.0 and SWE-V test different capabilities with almost no agent overlap. A weighted merge would encode weight-choice preference as ranking, not empirical performance comparison. Full rationale: [methodology.md §1](methodology.md).

Full methodology: [methodology.md](methodology.md) · Benchmark landscape: [benchmarks.md](benchmarks.md)

---

## Agent Inventory (22 Entries, v1.0)

| (Agent + Model) | Developer | Type | TB2.0 | SWE-V |
|---|---|---|---|---|
| Codex + GPT-5.5 | OpenAI | Commercial | ✓ | — |
| ForgeCode + GPT-5.4 | Antinomy | Commercial / OS | ✓ | — |
| TongAgents + Gemini 3.1 Pro | ByteDance SE Lab | Research | ✓ | — |
| ForgeCode + Claude Opus 4.6 | Antinomy | Commercial / OS | ✓ | — |
| SageAgent + GPT-5.3-Codex | Unknown | Unknown | ✓ | — |
| ForgeCode + Gemini 3.1 Pro | Antinomy | Commercial / OS | ✓ | — |
| Factory Droid + GPT-5.3-Codex | Factory AI | Commercial | ✓ | ✓~ |
| Junie CLI + Multiple | JetBrains | Commercial | ✓ | — |
| Factory Droid + Claude Opus 4.6 | Factory AI | Commercial | ✓ | — |
| Claude Code + Claude Opus 4.6 | Anthropic | Commercial | ✓ | — |
| OpenHands v2 + Claude Opus 4.5 | All Hands AI | Open-source | ✓ | ✓~ |
| Augment Code + Claude Opus 4.6 | Augment | Commercial | — | ✓~ |
| OpenHands v3 + Claude Opus 4.6 | All Hands AI | Open-source | — | ✓~ |
| Amazon Q Developer + Proprietary | Amazon | Commercial | — | ✓~ |
| Cursor Background Agent + Sonnet 4.6 | Anysphere | Commercial | — | ✓~ |
| Composio SWE-Kit + Sonnet 4.6 | Composio | Commercial | — | ✓~ |
| Cline + Claude Sonnet 4.6 | Community | Open-source | — | ✓~ |
| Devin 2.0 + Proprietary | Cognition AI | Commercial | — | ✓ |
| SWE-agent v1 + Claude Sonnet 4.5 | Princeton | Research / OS | — | ✓~ |
| AutoCodeRover v2 + GPT-5.2 | NUS | Research / OS | — | ✓~ |
| Agentless v2 + Claude Sonnet 4.5 | Academic | Research / OS | — | ✓~ |
| Aider + Claude Sonnet 4.5 | Community | Open-source | — | ✓ |

**~** = secondary source (awesomeagents.ai aggregator). Full profiles: [profiles.md](profiles.md) · Raw data: [raw-data.md](raw-data.md)

---

## Research Provenance

| Run | Mode | Date | Agents | Focus |
|---|---|---|---|---|
| 1 | Parallel (3 agents) | 2026-04-27 | swe-bench-researcher, terminal-bench-researcher, agent-inventory-researcher | Initial landscape |
| 2 | Parallel ultradeep (2 agents) | 2026-04-27 | benchmark-discovery-1, benchmark-discovery-2 | All agent-level benchmarks beyond TB2.0 and SWE-V |

**Coverage:** 80+ web searches · 25+ WebFetch calls · 15 primary leaderboards fetched

Full benchmark landscape findings (why other benchmarks were not activated): [benchmarks.md](benchmarks.md) · Full source provenance: [research.md](research.md)

---

## Headline Findings

**Two separate agent populations.** TB2.0 and SWE-V have almost no submitter overlap. "Best coding agent" is entirely context-dependent — the TB2.0 leaders are the wrong choice for GitHub issue resolution and vice versa.

**Scaffold premium: ~10 pp.** Same model, different scaffold = 10 percentage point gap at the frontier. Choosing the best model is not enough; the scaffold determines whether the model can effectively navigate a codebase under real execution conditions.

**Open-source near-parity on SWE-V.** OpenHands v3 (68.4%) is within 3.6 pp of Augment Code (72.0%) on the same Claude Opus 4.6 model — the cost of Augment's proprietary BM25 + code-graph retrieval scaffold.

**Long-horizon cliff: 45–63 pp drop.** Agents scoring 65–74% on SWE-V score 11–25% on multi-file feature development tasks. Current benchmark scores predict contained task performance only.

**Devin 2.0 brand vs. benchmark gap.** SWE-V rank 8, below three open-source systems. Differentiation is product experience and team workflow tooling, not benchmark performance.

---

## Next Update Schedule (v1.1 Priorities)

| Priority | Target | Trigger |
|---|---|---|
| **High** | Verify top SWE-V scores at primary source | Scrape swebench.com/verified.html directly |
| **High** | Cross-benchmark: Codex + GPT-5.5 on SWE-V | Submission or authoritative report |
| **High** | Cross-benchmark: OpenHands v3 on TB2.0 | Submission or authoritative report |
| **Medium** | SWE-bench Pro list activation | ≥4 cohort pairs submit to labs.scale.com |
| **Medium** | Resolve Junie CLI model identity | JetBrains disclosure or leaderboard metadata |
| **Medium** | Verify ForgeCode GitHub URL (moved to tailcallhq) | Update profiles.md and research.md links |
| **Low** | Cost list activation | ≥4 agents publish per-task cost data |

**Monitoring:** tbench.ai (continuous) · swebench.com/verified.html (continuous) · prarena.ai (real-world deployment signal, updated every 3 hours)

---

*Version 1.0 · April 27, 2026 · Research: 2 runs, 5 parallel agents, 80+ searches*
