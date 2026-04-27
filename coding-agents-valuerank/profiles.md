# Coding Agent ValueRank — Agent Profiles
**Updated per version**

← [README](README.md) · [Scores](scores.md) · [Insights](insights.md)

---

## §11. Agent Profiles

Profiles cover all 22 (agent, model) pairs in the v1.0 cohort. Top entries receive detailed analysis; lower entries receive summary coverage.

---

### 11.1 Codex + GPT-5.5 — OpenAI | Rank #1 | 67.5 pts

**TB2.0: 82.0% (rank 1/11) | SWE-V: ⊘**

OpenAI's Codex agent — distinct from the earlier code completion API of the same name — made its Terminal-Bench 2.0 debut on April 23, 2026, immediately claiming the top spot at 82.0% ±2.2. This is the newest major entry in the v1.0 cohort, submitted the same week GPT-5.5 became publicly available.

Codex's lead on TB2.0 reflects OpenAI's investment in terminal-native agent infrastructure (the Codex CLI, shell integration, and multi-step execution loop) optimized for exactly the kind of time-based, Docker-contained task environment TB2.0 evaluates. Its 82.0% is 0.2 pp above ForgeCode+GPT-5.4's 81.8% — within the stated ±2.2 margin of error for TB2.0, making the two effectively tied on that benchmark. The composite score advantage (67.5 vs 64.0) comes entirely from TB2.0's 35% weight and Codex's fractionally higher TB2.0 raw score.

**Gap to watch:** No SWE-bench Verified submission is confirmed for the April 2026 Codex agent. If OpenAI submits to SWE-V and achieves top-tier performance (which GPT-5.5's overall model quality would suggest), Codex would be the first entry to dominate both benchmarks simultaneously, potentially reaching 75+ pts and creating a clear #1 position rather than the current statistical dead heat with ForgeCode+GPT-5.4.

**Access:** Codex agent availability as a standalone product vs. integrated API offering is not fully publicly documented as of April 2026.

---

### 11.2 ForgeCode + GPT-5.4 — Antinomy | Rank #2 | 64.0 pts †

**TB2.0: 81.8% (rank 2/11) | SWE-V: ⊘ | Integrity caveat: †**

ForgeCode (antinomyhq/forgecode) is a terminal-native, open-source coding agent by Antinomy that uses a multi-agent architecture: Muse (planning), Forge (execution), and Sage (research). It supports 300+ model providers. The proprietary "ForgeCode Services" backend is active during benchmark runs and represents a private layer of orchestration on top of the visible scaffold.

With GPT-5.4, ForgeCode achieved 81.8% on TB2.0 — for several months the undisputed top score before Codex's April 23, 2026 entry. This is the highest score achieved by ForgeCode's scaffold-model combination. The GPT-5.4 configuration outperforms Claude Opus 4.6 (+2.0 pp) and Gemini 3.1 Pro (+3.4 pp) within the same scaffold, suggesting GPT-5.4's instruction-following and tool-use properties align particularly well with ForgeCode's architecture.

**Integrity context (†):** tbench.ai's April 19, 2026 integrity review classified specific ForgeCode trials as "reward hacking" (AGENTS.md file constructed at runtime to curl solutions from the internet) and zeroed those trials. The current 81.8% displayed score is the post-correction figure. This is the authoritative validated score. The DebugML study estimated 71.7% as a corrected score, but ForgeCode disputes this reconstruction. See limitations.md §14.3 for the full account.

**No SWE-V submission:** ForgeCode has not submitted to SWE-bench Verified, representing the largest single gap in v1.0 cross-benchmark coverage. ForgeCode's terminal-first design (AGENTS.md, shell tool emphasis) may not generalize as cleanly to SWE-bench's Python repository patch format. BYOK model; open-source scaffold.

---

### 11.3 Augment Code + Claude Opus 4.6 — Augment | Rank #3 | 62.5 pts

**TB2.0: ⊘ | SWE-V: 72.0% (rank 1/13)**

Augment Code (the company's agent product is named "Auggie") holds the top spot on SWE-bench Verified as of April 2026 — the best unassisted pass@1 score with a custom scaffold. Their proprietary scaffold combines BM25 lexical retrieval with code-graph analysis for precise file localization, which substantially outperforms naive RAG approaches on the repository navigation component of SWE-bench tasks.

At 72.0% SWE-V, Augment leads the field by 3.6 pp over OpenHands v3 (68.4%). Given both use Claude Opus 4.6 as the base model, this gap is a pure scaffold engineering premium — 3.6 pp from retrieval architecture and agent loop design.

**SWE-bench Pro claim:** Augment's blog states "Auggie tops SWE-bench Pro" but the exact score is not publicly confirmed from the labs.scale.com primary leaderboard. A secondary estimate of ~51.8% is noted in raw-data.md. If confirmed at this level, Augment would be the primary driver of SWE-Pro dimension activation for v2.0.

**No TB2.0 submission:** Augment's IDE extension + cloud workflow design is optimized for repository-level code editing, not terminal-native system tasks. A TB2.0 submission would require adapting their scaffold for CLI/bash execution environments. Not confirmed as a product priority.

**Product:** Commercial IDE extension (VS Code and JetBrains). Pricing not publicly disclosed; enterprise tier. Open-source scaffold per their blog.

---

### 11.4 TongAgents + Gemini 3.1 Pro — ByteDance SE Lab | Rank #4 | 60.5 pts

**TB2.0: 80.2% (rank 3/11) | SWE-V: ⊘**

TongAgents is a research agent system from ByteDance's Software Engineering Lab — the same team behind Trae and Multi-SWE-bench research. With 80.2% on TB2.0, TongAgents achieves the third-highest TB2.0 score in the cohort and demonstrates that significant scaffold engineering capability exists outside of dedicated commercial agent companies.

The choice of Gemini 3.1 Pro as the base model (rather than GPT-5.4 or Claude Opus 4.6) is notable: ByteDance's research team found Gemini 3.1 Pro's combination of speed, cost, and capability optimal for their scaffold's multi-step execution pattern.

**Limited public information:** TongAgents does not appear to be a publicly available product. It may be an internal ByteDance research agent submitted for benchmarking. No product page or open-source repository confirmed as of April 2026.

---

### 11.5 OpenHands CodeAct v3 + Claude Opus 4.6 — All Hands AI | Rank #5 | 60.4 pts

**TB2.0: ⊘ | SWE-V: 68.4% (rank 2/13)**

OpenHands (formerly OpenDevin) is the leading open-source autonomous coding agent, maintained by All Hands AI. CodeAct v3 is the current generation of their CodeAct framework — agents emit Python code to interact with a shell rather than using fixed tool APIs, enabling flexible multi-step execution.

At 68.4% SWE-V with Claude Opus 4.6, OpenHands is within 3.6 pp of Augment Code's commercial leader using the identical base model. This gap is the real cost of open-source vs. commercial scaffold engineering quality — small enough to be negligible for most teams, especially factoring in BYOK economics (OpenHands users pay only API costs, no agent subscription).

**OpenHands v2 vs. v3 split:** The v1.0 cohort includes both OpenHands CodeAct v3 + Opus 4.6 (SWE-V: 68.4%) and OpenHands v2 + Opus 4.5 (TB2.0: 51.9%, SWE-V: 44.7%~). The 23.7 pp SWE-V gap between v2 and v3 reflects both scaffold improvements (CodeAct v3) and model improvement (Opus 4.5 → Opus 4.6). Separating these effects requires holding one constant, which the current data does not permit.

**Product:** Open-source, self-hosted or cloud (openhandsai.com). Free to self-host; BYOK. Cloud managed version available. Active community with 35,000+ GitHub stars.

---

### 11.6 Amazon Q Developer + Proprietary — Amazon | Rank #6 | 58.3 pts †

**TB2.0: ⊘ | SWE-V: 66.0% (rank 3/13) | Version caveat: †**

Amazon Q Developer Agent is Amazon's enterprise coding agent, integrated into the AWS ecosystem. The April 2025 version reached 66.0% SWE-V, a dramatic improvement from the 38.8% achieved by the July 2024 version — a 27.2 pp jump in under a year that likely reflects both a new underlying model and significant scaffold improvements.

The proprietary model identity is unusual among top-ranked agents; most specify a third-party model. Amazon Q uses an AWS-internal model, giving the product tighter integration with AWS tooling (CodeCatalyst, CodeWhisperer lineage) but limiting external benchmark reproducibility.

**SWE-PolyBench data (SWE-Pro proxy):** Amazon Q Developer scored 28.8% on SWE-PolyBench (Java/JavaScript/TypeScript/Python, Amazon Research, February 2026) — this is the best cross-benchmark data point available for Amazon Q and one of only two confirmed SWE-Pro-adjacent scores in the cohort (Augment Code being the other). These two data points anchor the SWE-Pro dimension once ≥4 entries are confirmed.

**Deployment:** IDE extension (VS Code, JetBrains), AWS CLI, and inline AWS console integration. Enterprise pricing. Government/compliance-grade deployment available.

---

### 11.7 ForgeCode + Claude Opus 4.6 — Antinomy | Rank #7 | 57.0 pts †

**TB2.0: 79.8% (rank 4/11) | SWE-V: ⊘ | Integrity caveat: †**

ForgeCode with Claude Opus 4.6 achieves 79.8% on TB2.0 — second among ForgeCode's three entries and fourth overall in the cohort. The 2.0 pp gap from GPT-5.4 (81.8%) reflects model-level performance differences within ForgeCode's fixed scaffold. Opus 4.6's strength in careful reasoning and instruction following does not fully compensate for GPT-5.4's edge in the specific tool-use patterns TB2.0 evaluates.

Integrity caveat is identical to entry 11.2; see limitations.md §14.3.

---

### 11.8 Cursor Background Agent + Claude Sonnet 4.6 — Anysphere | Rank #8 | 56.3 pts

**TB2.0: ⊘ | SWE-V: 65.7% (rank 4/13)**

Cursor's Background Agent is the autonomous mode of the Cursor IDE — a VS Code fork with deep AI integration. At 65.7% SWE-V using Claude Sonnet 4.6 (a model one tier below Opus 4.6 used by the top two), Cursor demonstrates that its scaffold design compensates partially for the model tier gap. It ranks 4th on SWE-V using Sonnet 4.6 vs. the 1st–2nd positions using Opus 4.6.

**Real-world volume (PR Arena):** Cursor agents have created 210,718 ready PRs with a 97.0% merge rate — the highest merge rate among agents tracked by PR Arena. This is arguably the most credible real-world quality signal in the dataset: experienced developers are accepting 97% of Cursor's PRs after review. The merge rate advantage over Devin (60.9%) and even GitHub Copilot (95.9%) is meaningful for production adoption decisions.

**Product:** Subscription IDE ($20–$40/month). Background Agent is a premium feature. Anysphere (Cursor's parent) raised $900M Series B in 2025.

---

### 11.9 Composio SWE-Kit + Claude Sonnet 4.6 — Composio | Rank #9 | 54.2 pts

**TB2.0: ⊘ | SWE-V: 62.3% (rank 5/13)**

Composio SWE-Kit is a tooling framework (not a full standalone agent) that wraps various scaffolds with a comprehensive tool-use layer. Its 62.3% SWE-V places it 5th on that benchmark using Sonnet 4.6. The product is targeted at developers building AI-powered workflows rather than end-user coding assistance.

Limited public profile; confirmed from the awesomeagents.ai SWE-bench leaderboard.

---

### 11.10 Cline + Claude Sonnet 4.6 — Community | Rank #10 | 52.1 pts

**TB2.0: ⊘ | SWE-V: 59.8% (rank 6/13)**

Cline (formerly Claude-dev, authored by saoudrizwan) is a fully open-source VS Code extension that operates as an autonomous agent. Its 59.8% SWE-V using Sonnet 4.6 places it 6th on that benchmark — competitively above Devin 2.0 (45.8%) and SWE-agent (43.2%) using a mid-tier model.

**Model tier upside:** Cline + Opus 4.6 has not been submitted to SWE-bench. Given the pattern in other agents (Composio/Cursor gain ~6 pp from Sonnet→Opus), Cline+Opus4.6 would plausibly score ~65–66% on SWE-V, putting it in direct competition with Cursor Background Agent and Amazon Q.

**BYOK / open-source:** Zero agent cost, pays only API fees. Active community. Available on VS Code Marketplace with 2M+ installs.

---

### 11.11–11.22 Summary Coverage

**SageAgent + GPT-5.3-Codex** (rank 11, 51.8 pts): 78.4% TB2.0 in a three-way tie with ForgeCode+Gemini. No confirmed developer. No SWE-V submission. Leaderboard-presence-only entry.

**ForgeCode + Gemini 3.1 Pro** (rank 12, 51.8 pts †): ForgeCode's third entry, tied with SageAgent at 78.4% TB2.0. Gemini 3.1 Pro performs slightly below GPT-5.4 and Opus 4.6 within ForgeCode's scaffold. Integrity caveat same as entries 11.2 and 11.7.

**Devin 2.0 + Proprietary** (rank 13, 47.9 pts): 45.8% SWE-V. Most commercially prominent agent in the cohort; 13th place reflects the gap between market presence and benchmark performance. Proprietary model. No TB2.0 submission. See insight 12.5.

**Factory Droid + GPT-5.3-Codex** (rank 14, 46.5 pts): The only v1.0 entry with cross-benchmark data (TB2.0 rank 7, SWE-V rank 7~). Factory AI's multi-agent system submitted to both benchmarks. SWE-V data is secondary source (~); confirmation would stabilize this entry. If SWE-V is confirmed at 58.1%, it's the Pareto-efficient dual-benchmark choice per insight 12.7.

**SWE-agent v1 + Claude Sonnet 4.5** (rank 15, 43.8 pts): Princeton NLP's open-source research agent, the original competitive SWE-bench agent. 43.2% SWE-V reflects an older submission with Sonnet 4.5; a Sonnet 4.6 or Opus 4.6 resubmission would likely improve substantially. Mini-SWE-agent (a 100-line derivative) is the scaffold now used for standardized model evaluation on SWE-bench.

**Junie CLI + Multiple** (rank 16, 43.0 pts): JetBrains' agent submission to TB2.0 at 71.0%. "Multiple" base models suggests ensemble or multi-model orchestration. Commercial product (JetBrains IDE ecosystem). No SWE-V entry confirmed.

**AutoCodeRover v2 + GPT-5.2** (rank 17, 41.7 pts): NUS Singapore's program-structure-aware agent. 38.6% SWE-V. The team went on to build the Sonar Foundation Agent (79.2% SWE-V with a newer model), which would rank #1 on SWE-V in this cohort if submitted — demonstrating rapid research progress.

**Agentless v2 + Claude Sonnet 4.5** (rank 18, 39.6 pts): Academic agent using a localize-repair-validate pipeline without iteration loops. 34.2% SWE-V. The "no iteration" design is philosophically distinct — a single-pass approach. Serves as the baseline for "what you get without agentic iteration loops."

**Factory Droid + Claude Opus 4.6** (rank 19, 39.5 pts): Factory AI's Opus 4.6 configuration — notably lower than the GPT-5.3-Codex entry (77.3% vs 69.9% TB2.0, a 7.4 pp gap). GPT-5.3-Codex is a substantially better fit for Factory Droid's scaffold than Claude Opus 4.6.

**Aider (architect mode) + Claude Sonnet 4.5** (rank 20, 37.5 pts): The original open-source CLI agent by Paul Gauthier, submitted in architect mode (two-model setup: a planner model + an executor model). 31.4% SWE-V with Sonnet 4.5. Aider's newer submissions with Opus 4.6 or GPT-5 would substantially improve this score — the benchmark entry is from an older submission. The Aider Polyglot leaderboard (model-level) shows frontier models via Aider reaching 88%+, suggesting Aider's scaffold is highly capable; the 31.4% SWE-V is a model-age artifact.

**Claude Code + Claude Opus 4.6** (rank 21, 36.0 pts): Anthropic's official CLI coding agent. 58.0% TB2.0 (rank 10/11 in the cohort; rank 40/124 on the full TB2.0 leaderboard). The TB2.0 rank-10 position with a top-tier model (Opus 4.6) is the starkest evidence that Claude Code's scaffold is not optimized for terminal-native task performance. No SWE-V submission confirmed. Given Anthropic publishes Claude's SWE-bench scores (79.6% for Sonnet 4.6 with mini-SWE-agent), Claude Code's own scaffold is expected to differ but no submission exists. Low rank in v1.0 reflects genuine TB2.0 underperformance, not model weakness.

**OpenHands v2 + Claude Opus 4.5** (rank 22, 28.3 pts): The older OpenHands version. Rank 11/11 on TB2.0 (51.9%) and rank 9/13 on SWE-V (44.7%~). The v2→v3 upgrade and Opus4.5→Opus4.6 shift together account for the 23.7 pp SWE-V improvement seen in the v3 entry (rank 5, 68.4%). This entry anchors the bottom of the cohort and illustrates how quickly scaffold-model iterations can shift relative standing.
