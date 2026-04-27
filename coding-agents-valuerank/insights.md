# Coding Agent ValueRank — Strategic Insights
**Updated per version**

← [README](README.md) · [Scores](scores.md) · [Limitations](limitations.md)

---

## §12. Strategic Insights

### 12.1 TB2.0 vs SWE-V: Two Distinct Agent Populations

The most structurally significant finding of v1.0: Terminal-Bench 2.0 and SWE-bench Verified have almost no agent overlap. Of 22 cohort entries, only **Factory Droid + GPT-5.3-Codex** has confirmed real scores on both benchmarks. This is the primary reason ValueRank publishes two separate ranked lists rather than a composite score.

This is not a data collection artifact — it reflects a genuine bifurcation in the agent landscape:

**TB2.0 cluster:** ForgeCode, TongAgents, SageAgent, Codex, Junie, Factory Droid. These agents are built for terminal-native, CLI-first workflows with long-running process monitoring, Docker environments, and multi-step system administration. Their scaffold engineering is optimized for real-terminal execution feedback loops.

**SWE-V cluster:** Augment Code, OpenHands, Cursor, Composio, Cline, Devin. These agents are optimized for GitHub-style code repair: understanding issue descriptions, navigating Python repositories, writing patches, and passing test suites. Their scaffolds are heavily tuned for code navigation, BM25 retrieval, and structured file editing.

**Practical implication:** "Best coding agent" depends entirely on which workflow you're optimizing for. If your team works in terminal/CLI environments building systems software, the TB2.0 ranking is more predictive. If your team primarily resolves GitHub issues in Python repositories, the SWE-V ranking is more relevant. A team that does both would be best served by Factory Droid + GPT-5.3-Codex, the only v1.0 entry with demonstrated competence in both.

---

### 12.2 Scaffold Engineering Premium: 10 pp at the Frontier

**The single most important lesson from Terminal-Bench 2.0:** identical base models produce radically different agent performance depending on the scaffold.

The starkest example: ForgeCode + Gemini 3.1 Pro scored **78.4%** on TB2.0; Google's own Gemini 3.1 Pro submission scored approximately **68.5%** on the same benchmark using the same model weights. That 10-percentage-point gap is not a model difference — it is a scaffold difference.

This premium compounds across the field. On SWE-bench Verified, the same Claude Opus 4.6 scores:
- **72.0%** inside Augment Code's custom scaffold (with BM25 + code-graph retrieval)
- **68.4%** inside OpenHands CodeAct v3
- Presumably less inside a generic scaffold

**Why it matters for selection:** Choosing "the best model" does not automatically give you the best agent performance. The scaffold determines whether the model can effectively navigate a codebase, retry on failure, interpret error messages, and manage context across long tasks. Model capability is necessary but not sufficient. A weaker model in a better-designed scaffold can match or beat a stronger model in a generic scaffold.

**v1.0 limitation acknowledged:** Because most cohort entries are single-benchmark, we cannot directly test whether a scaffold that excels on TB2.0 also excels on SWE-V. Factory Droid's dual presence (TB2.0 rank 7, SWE-V rank 7) suggests their scaffold generalizes across benchmark types — a rare and valuable property.

---

### 12.3 Open-Source Agents Are Highly Competitive on SWE-V

Three of the top six SWE-V entries use open-source agent frameworks (all BYOK, zero agent overhead cost):

- **OpenHands v3 + Claude Opus 4.6** (SWE-V rank 2, 68.4%): within 3.6 pp of the commercial leader (Augment Code 72.0%)
- **Cline + Claude Sonnet 4.6** (SWE-V rank 6, 59.8%): using a model one tier below the leaders
- **Aider + Claude Sonnet 4.5** (SWE-V rank 13, 31.4%): the OG open-source coding agent; this submission used an older base model — likely substantially higher with Sonnet 4.6 or Opus 4.6

**The open-source parity argument:** OpenHands achieves 68.4% vs. Augment Code's 72.0% on the same Claude Opus 4.6 base model. The 3.6 pp gap is the cost of Augment's proprietary scaffold engineering (BM25 + code-graph retrieval). For teams unwilling to pay platform subscription fees, OpenHands is the rational choice — near-parity performance with full BYOK economics.

**Cline as the dark horse:** At SWE-V rank 6 with a mid-tier model (Claude Sonnet 4.6 vs. Opus 4.6 used by leaders), Cline's 59.8% suggests its scaffold is punching above the model tier. If Cline + Opus 4.6 were submitted, it would plausibly rank above Composio (62.3%) and possibly compete with Cursor (65.7%).

---

### 12.4 Devin 2.0 Underperforms Its Brand Positioning

**Devin 2.0** (SWE-V rank 8, 45.8%) holds a singular position as the most commercially prominent coding agent — Cognition AI's $25B valuation (reported in talks), heavy media coverage since the original 2024 debut — yet sits at rank 8 on SWE-V, below seven other entries including three open-source systems (OpenHands v3, Cline, and SWE-agent rank above it).

Its 45.8% SWE-V score is below the open-source SOTA (OpenHands 68.4%) by 22.6 percentage points. Devin's differentiation is not benchmark performance but product experience: full browser-based autonomous execution, task queuing, GitHub integration, and professional team workflows. The benchmark-to-product gap is among the largest in the cohort.

**Not on TB2.0:** Devin 2.0 has not submitted to Terminal-Bench 2.0 (confirmed absence). If Devin submitted and performed at a level consistent with its SWE-V tier (~45%), it would rank near the bottom of the TB2.0 list. A strong TB2.0 submission would require Devin's terminal-native capabilities to substantially exceed its code-repair tier — which is possible but undemonstrated.

---

### 12.5 The Long-Horizon Capability Cliff

Both active benchmarks test relatively contained, well-defined tasks: TB2.0's 89-task set and SWE-bench Verified's single-issue resolution tasks. Three independent research benchmarks reveal what happens when task complexity increases:

| Benchmark | Agent + Model | Contained Score | Long-Horizon Score |
|---|---|---|---|
| FeatureBench | Claude Code + Opus 4.5 | 74.4% SWE-V | **11.0%** (−63.4 pp) |
| FeatureBench | Codex + GPT-5.1-Codex | ~70% SWE-V | **12.5%** (−57.5 pp) |
| SWE-EVO (48 tasks) | OpenHands + GPT-5.4 | ~65% SWE-V | **25.0%** (−40 pp) |
| DevOps-Gym | Claude Code + Claude Sonnet | ~65% SWE-V | **23.87%** (−41 pp) |

The top agents on SWE-V score 68–72% on contained issue-resolution tasks. Their performance on multi-file feature development, sustained software evolution, and enterprise-language DevOps tasks is likely in the 10–25% range based on these proxy measurements.

**What this means for users:** Current benchmark scores predict performance on discrete, contained code repair tasks — the equivalent of resolving a specific bug report. They do not predict performance on "implement this 3-week feature across 15 files" or "upgrade this Spring Boot monorepo from v2 to v3." For those use cases, no publicly ranked agent has demonstrated sufficient capability.

**Why these benchmarks are not scored:** FeatureBench, DevOps-Gym, and SWE-EVO have no exact (agent, model) pair matches to the current v1.0 cohort (model versions and scaffold combinations differ). They are documented here as capability context, not as scored dimensions. See [benchmarks.md](benchmarks.md) for full landscape.

---

### 12.6 Pareto Frontier: The Honest Cross-Benchmark View

Without a composite score, the Pareto frontier is the only defensible cross-benchmark comparison. A strict Pareto analysis across two axes (higher TB2.0 = better, higher SWE-V = better) reveals which entries are not dominated by any other entry on both dimensions simultaneously.

| (Agent + Model) | TB2.0 | SWE-V | Pareto Status |
|---|---|---|---|
| **Codex + GPT-5.5** | 82.0% | — | **✓ Frontier** (TB2.0 #1) |
| **Augment Code + Opus 4.6** | — | 72.0%~ | **✓ Frontier** (SWE-V #1) |
| **Factory Droid + GPT-5.3-Codex** | 77.3% | 58.1%~ | **✓~ Frontier** (only dual-benchmark entry) |
| ForgeCode + GPT-5.4 | 81.8% | — | ✗ Dominated on TB2.0 by Codex; no SWE-V data |
| TongAgents + Gemini 3.1 Pro | 80.2% | — | ✗ Dominated by Codex on TB2.0; no SWE-V data |
| OpenHands v3 + Opus 4.6 | — | 68.4%~ | ✗ Dominated by Augment Code on SWE-V; no TB2.0 data |

Only three entries cannot be strictly dominated: Codex+GPT-5.5 (TB2.0 leader), Augment Code+Opus4.6 (SWE-V leader), and Factory Droid+GPT-5.3-Codex (the only agent with meaningful data on both axes). Factory Droid's Pareto status is provisional (~) because its SWE-V score is from a secondary source.

**Practical selection rule:** TB2.0-type work → Codex+GPT-5.5. SWE-V-type work → Augment Code+Opus4.6. Both → Factory Droid+GPT-5.3-Codex (and monitor v1.1 when primary-source SWE-V data arrives).

---

### 12.7 ForgeCode TB2.0 Sensitivity to Integrity Decision

DebugML estimated ForgeCode+GPT-5.4's "clean" TB2.0 score at 71.7% after removing allegedly pre-cached solutions. tbench.ai's official ruling used a different characterization (AGENTS.md curling solutions at run time, not pre-loaded) and zeroed only affected trials, resulting in the displayed 81.8%. ValueRank uses the tbench.ai post-correction score as authoritative.

If DebugML's 71.7% were used instead, the TB2.0 ranking shifts as follows:

**With ForgeCode+GPT-5.4 at 71.7%** (drops below Factory Droid+GPT-5.3 at 77.3%, Junie CLI at 71.0% is now below it):

| TB2.0 Rank | Official | If DebugML Used | Change |
|---|---|---|---|
| 1 | Codex (82.0%) | Codex (82.0%) | — |
| 2 | **ForgeCode+GPT-5.4 (81.8%)** | TongAgents (80.2%) | ForgeCode drops to rank 7 |
| 3 | TongAgents (80.2%) | ForgeCode+Opus4.6 (79.8%) | moves up 1 |
| 4 | ForgeCode+Opus4.6 (79.8%) | SageAgent (78.4%) tied | moves up 1 |
| 5–6 | SageAgent / ForgeCode+Gemini (78.4%) | ForgeCode+Gemini (78.4%) tied | moves up 1 |
| 7 | Factory Droid+GPT-5.3 (77.3%) | Factory Droid+GPT-5.3 (77.3%) | moves up 1 |
| — | — | **ForgeCode+GPT-5.4 (71.7%)** | enters at rank 7 |
| 8 | Junie CLI (71.0%) | Junie CLI (71.0%) | — |

**Key effect:** ForgeCode+GPT-5.4 drops from TB2.0 rank 2 to rank 7 — a 5-position fall. ForgeCode+Opus4.6 and ForgeCode+Gemini both move up one position each (cascade re-ranking). The Pareto frontier is unchanged: Codex remains TB2.0 leader regardless of which ForgeCode+GPT-5.4 score is used.
