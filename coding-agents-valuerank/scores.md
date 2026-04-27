# Coding Agent ValueRank — Scores
**Updated every version | Primary calculation file**

← [README](README.md) · [Raw Data](raw-data.md) · [Methodology](methodology.md)

---

## §1. Methodology Recap

Within each ranked list, (agent, model) pairs are ranked 1–n (best to worst raw score). Normalized score = `((n − rank) / (n − 1)) × 100`. Missing data = **50⊘**. Tied ranks receive the average of their tied positions.

No cross-benchmark composite is computed. See [methodology.md §1](methodology.md) for rationale.

---

## §2. Terminal-Bench 2.0 Ranking

**n = 11 real scorers | Formula: `((11 − rank) / 10) × 100`**

Source: tbench.ai/leaderboard/terminal-bench/2.0 (primary, confirmed)
Integrity update: April 19, 2026 — ForgeCode entries carry † (specific trials zeroed for reward hacking; displayed scores are post-correction). OB-1 and QuantFlow permanently removed.

### §2.1 Derivation Table

| Rank | (Agent + Model) | TB2.0 Raw | CI | Norm Score |
|---|---|---|---|---|
| 1 | Codex + GPT-5.5 | 82.0% | ±2.2 | **100.0** |
| 2 | ForgeCode + GPT-5.4† | 81.8% | ±2.0 | **90.0** |
| 3 | TongAgents + Gemini 3.1 Pro | 80.2% | ±2.6 | **80.0** |
| 4 | ForgeCode + Claude Opus 4.6† | 79.8% | ±1.6 | **70.0** |
| 5–6 | SageAgent + GPT-5.3-Codex | 78.4% | ±2.2 | **55.0** |
| 5–6 | ForgeCode + Gemini 3.1 Pro† | 78.4% | ±1.8 | **55.0** |
| 7 | Factory Droid + GPT-5.3-Codex | 77.3% | ±2.2 | **40.0** |
| 8 | Junie CLI + Multiple | 71.0% | ±2.9 | **30.0** |
| 9 | Factory Droid + Claude Opus 4.6 | 69.9% | ±2.5 | **20.0** |
| 10 | Claude Code + Claude Opus 4.6 | 58.0% | ±2.9 | **10.0** |
| 11 | OpenHands v2 + Claude Opus 4.5 | 51.9% | ±2.9 | **0.0** |

**†** tbench.ai integrity ruling (April 19, 2026): ForgeCode's AGENTS.md curled solutions during flagged trials; those trials zeroed. Displayed scores are the post-correction official figures. See limitations.md §14.3.

**Statistical note:** The top 7 entries have overlapping confidence intervals. Codex [79.8%, 84.2%] overlaps with ForgeCode+GPT-5.4 [79.8%, 83.8%], which overlaps with TongAgents [77.6%, 82.8%], continuing down through Factory Droid+GPT-5.3 [75.1%, 79.5%]. Ordinal ranks 1–7 are statistically indistinguishable at 1σ. See limitations.md §14.11.

**Junie CLI note:** Listed as "Multiple" base models — this entry does not conform to the (agent, model) pair convention. See limitations.md §14.12.

### §2.2 TB2.0 Final Ranking

| Rank | (Agent + Model) | Developer | TB2.0 Score | Norm |
|---|---|---|---|---|
| 🥇 1 | **Codex + GPT-5.5** | OpenAI | 82.0% | 100.0 |
| 🥈 2 | **ForgeCode + GPT-5.4†** | Antinomy | 81.8% | 90.0 |
| 🥉 3 | **TongAgents + Gemini 3.1 Pro** | ByteDance SE Lab | 80.2% | 80.0 |
| 4 | ForgeCode + Claude Opus 4.6† | Antinomy | 79.8% | 70.0 |
| 5–6 | SageAgent + GPT-5.3-Codex | Unknown | 78.4% | 55.0 |
| 5–6 | ForgeCode + Gemini 3.1 Pro† | Antinomy | 78.4% | 55.0 |
| 7 | Factory Droid + GPT-5.3-Codex | Factory AI | 77.3% | 40.0 |
| 8 | Junie CLI + Multiple | JetBrains | 71.0% | 30.0 |
| 9 | Factory Droid + Claude Opus 4.6 | Factory AI | 69.9% | 20.0 |
| 10 | Claude Code + Claude Opus 4.6 | Anthropic | 58.0% | 10.0 |
| 11 | OpenHands v2 + Claude Opus 4.5 | All Hands AI | 51.9% | 0.0 |

---

## §3. SWE-bench Verified Ranking

**n = 13 real scorers | Formula: `((13 − rank) / 12) × 100`**

Source: swebench.com/verified.html (primary leaderboard). Agent-level tracking via awesomeagents.ai~ (third-party aggregator, April 19, 2026). Scores sourced from awesomeagents.ai carry ~ regardless of whether individual entries are labeled differently in older documents — the aggregator is not a primary leaderboard.

### §3.1 Derivation Table

| Rank | (Agent + Model) | SWE-V Raw | Source | Norm Score |
|---|---|---|---|---|
| 1 | Augment Code + Claude Opus 4.6 | 72.0% | awesomeagents.ai~ | **100.0** |
| 2 | OpenHands v3 + Claude Opus 4.6 | 68.4% | awesomeagents.ai~ | **91.7** |
| 3 | Amazon Q Developer + Proprietary† | 66.0% | awesomeagents.ai~ | **83.3** |
| 4 | Cursor Background Agent + Sonnet 4.6 | 65.7% | awesomeagents.ai~ | **75.0** |
| 5 | Composio SWE-Kit + Sonnet 4.6 | 62.3% | awesomeagents.ai~ | **66.7** |
| 6 | Cline + Claude Sonnet 4.6 | 59.8% | awesomeagents.ai~ | **58.3** |
| 7 | Factory Droid + GPT-5.3-Codex | 58.1% | 3rd-party aggregator~ | **50.0** |
| 8 | Devin 2.0 + Proprietary | 45.8% | cognition.ai/blog | **41.7** |
| 9 | OpenHands v2 + Claude Opus 4.5 | 44.7% | 3rd-party aggregator~ | **33.3** |
| 10 | SWE-agent v1 + Claude Sonnet 4.5 | 43.2% | awesomeagents.ai~ | **25.0** |
| 11 | AutoCodeRover v2 + GPT-5.2 | 38.6% | awesomeagents.ai~ | **16.7** |
| 12 | Agentless v2 + Claude Sonnet 4.5 | 34.2% | awesomeagents.ai~ | **8.3** |
| 13 | Aider + Claude Sonnet 4.5 | 31.4% | swebench.com | **0.0** |

**~** All awesomeagents.ai-sourced scores are secondary (~). awesomeagents.ai is a third-party aggregator that compiles from official sources; swebench.com/verified.html is the primary leaderboard. The only SWE-V score verified directly from a primary source in this cohort is Aider (swebench.com) and Devin 2.0 (cognition.ai/blog).

**† Amazon Q Developer:** 66.0% from April 2025 agent version; model identity unspecified. Earlier versions scored 38.8% (v20240719) and 25.6% (v20240430). See limitations.md §14.5.

**Factory Droid note:** Normalized score of 50.0 coincides numerically with the missing-data neutral value but is a real rank-7 score, not absent data.

### §3.2 SWE-V Final Ranking

| Rank | (Agent + Model) | Developer | SWE-V Score | Norm |
|---|---|---|---|---|
| 🥇 1 | **Augment Code + Claude Opus 4.6** | Augment | 72.0%~ | 100.0 |
| 🥈 2 | **OpenHands v3 + Claude Opus 4.6** | All Hands AI | 68.4%~ | 91.7 |
| 🥉 3 | **Amazon Q Developer + Proprietary†** | Amazon | 66.0%~ | 83.3 |
| 4 | Cursor Background Agent + Sonnet 4.6 | Anysphere | 65.7%~ | 75.0 |
| 5 | Composio SWE-Kit + Sonnet 4.6 | Composio | 62.3%~ | 66.7 |
| 6 | Cline + Claude Sonnet 4.6 | Community | 59.8%~ | 58.3 |
| 7 | Factory Droid + GPT-5.3-Codex | Factory AI | 58.1%~ | 50.0 |
| 8 | Devin 2.0 + Proprietary | Cognition AI | 45.8% | 41.7 |
| 9 | OpenHands v2 + Claude Opus 4.5 | All Hands AI | 44.7%~ | 33.3 |
| 10 | SWE-agent v1 + Claude Sonnet 4.5 | Princeton | 43.2%~ | 25.0 |
| 11 | AutoCodeRover v2 + GPT-5.2 | NUS | 38.6%~ | 16.7 |
| 12 | Agentless v2 + Claude Sonnet 4.5 | Academic | 34.2%~ | 8.3 |
| 13 | Aider + Claude Sonnet 4.5 | Community | 31.4% | 0.0 |

**~** on the rank header = that entry's raw score sourced from awesomeagents.ai (secondary). Devin 2.0 and Aider have primary-source scores.

---

## §4. Cross-Benchmark: Pareto Frontier

The only honest cross-benchmark statement available from current data. An entry is Pareto-non-dominated if no other entry has both a higher TB2.0 score and a higher SWE-V score.

| (Agent + Model) | TB2.0 | SWE-V | Pareto Status |
|---|---|---|---|
| **Codex + GPT-5.5** | 82.0% | — | **✓ Frontier** (TB2.0 #1, SWE-V absent) |
| **Augment Code + Claude Opus 4.6** | — | 72.0% | **✓ Frontier** (SWE-V #1, TB2.0 absent) |
| **Factory Droid + GPT-5.3-Codex** | 77.3% | 58.1%~ | **✓~ Frontier** (only dual-benchmark entry; SWE-V secondary) |
| ForgeCode + GPT-5.4 | 81.8% | — | ✗ Dominated on TB2.0 by Codex; no SWE-V data |
| OpenHands v3 + Opus 4.6 | — | 68.4% | ✗ Dominated on SWE-V by Augment Code |
| All others | one axis only | — | ✗ Dominated or absent on at least one axis |

Three entries cannot be strictly dominated. Factory Droid's Pareto status is provisional (~) because its SWE-V score is from a secondary source.

**Practical selection rule:** Need TB2.0-type performance → Codex + GPT-5.5. Need SWE-V-type performance → Augment Code + Claude Opus 4.6. Need both → Factory Droid + GPT-5.3-Codex (with caveat on secondary SWE-V source).

---

## §5. Version History

| Version | Date | Change | TB2.0 n | SWE-V n |
|---|---|---|---|---|
| v1.0 | 2026-04-27 | Initial release — two separate ranked lists | 11 | 13 |

*Priority for v1.1: confirm primary-source SWE-V scores for top-ranked entries (verify against swebench.com directly); collect TB2.0 or SWE-V cross-submissions for Codex and OpenHands v3; resolve Junie CLI model identity.*
