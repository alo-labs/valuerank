# Coding Agent ValueRank — Research Provenance
**Archival | Documents all data sources**

← [README](README.md) · [Raw Data](raw-data.md) · [Limitations](limitations.md)

---

## Research Runs

| Run | Mode | Date | Focus | Agents Used |
|---|---|---|---|---|
| 1 | Parallel (3 agents) | 2026-04-27 | Initial landscape: SWE-bench leaderboard, TB2.0 leaderboard, agent inventory | swe-bench-researcher, terminal-bench-researcher, agent-inventory-researcher |
| 2 | Parallel ultradeep (2 agents) | 2026-04-27 | Benchmark discovery: all agent-level coding benchmarks beyond TB2.0 and SWE-bench | benchmark-discovery-1, benchmark-discovery-2 |

Total web searches: 80+ | Total WebFetch calls: 25+ | Primary leaderboards fetched: 15

---

## Run 1 — Initial Landscape Research

### Sources: SWE-bench Leaderboard Data

| Claim | Source | Confidence |
|---|---|---|
| Augment Code + Opus 4.6: 72.0% SWE-V | awesomeagents.ai/leaderboards/swe-bench-coding-agent-leaderboard/ | Confirmed |
| OpenHands CodeAct v3 + Opus 4.6: 68.4% SWE-V | awesomeagents.ai; openhands.dev/blog | Confirmed |
| Cursor Background Agent + Sonnet 4.6: 65.7% SWE-V | awesomeagents.ai | Confirmed |
| Composio SWE-Kit + Sonnet 4.6: 62.3% SWE-V | awesomeagents.ai | Confirmed |
| Cline + Sonnet 4.6: 59.8% SWE-V | awesomeagents.ai | Confirmed |
| Devin 2.0 + Proprietary: 45.8% SWE-V | cognition.ai/blog/swe-bench-technical-report | Confirmed |
| SWE-agent v1 + Sonnet 4.5: 43.2% SWE-V | awesomeagents.ai | Confirmed |
| AutoCodeRover v2 + GPT-5.2: 38.6% SWE-V | awesomeagents.ai | Confirmed |
| Agentless v2 + Sonnet 4.5: 34.2% SWE-V | awesomeagents.ai | Confirmed |
| Aider + Sonnet 4.5: 31.4% SWE-V | swebench.com | Confirmed |
| Amazon Q Developer (Apr 2025): 66.0% SWE-V | awesomeagents.ai | Confirmed (version unspecified) |
| Amazon Q Developer (v20240719): 38.8% SWE-V | aws.amazon.com/blogs/devops | Confirmed |
| Factory Droid + GPT-5.3-Codex: ~58.1% SWE-V | Third-party aggregator | Secondary (~) |
| OpenHands v2 + Opus 4.5: ~44.7% SWE-V | Third-party aggregator | Secondary (~) |
| SWE-bench Verified total entries: ~100+ | swebench.com | Confirmed |
| SWE-bench contamination (OpenAI audit, 2025) | Multiple sources; epoch.ai | Confirmed |

### Sources: Terminal-Bench 2.0 Leaderboard Data

| Claim | Source | Confidence |
|---|---|---|
| Codex + GPT-5.5: 82.0% ±2.2 (2026-04-23, rank 1) | tbench.ai leaderboard | Confirmed |
| ForgeCode + GPT-5.4: 81.8% ±2.0 (rank 2, post-correction) | tbench.ai leaderboard | Confirmed |
| TongAgents + Gemini 3.1 Pro: 80.2% ±2.6 (rank 3) | tbench.ai leaderboard | Confirmed |
| ForgeCode + Claude Opus 4.6: 79.8% ±1.6 (rank 4) | tbench.ai leaderboard | Confirmed |
| SageAgent + GPT-5.3-Codex: 78.4% ±2.2 (rank 5) | tbench.ai leaderboard | Confirmed |
| ForgeCode + Gemini 3.1 Pro: 78.4% ±1.8 (rank 6) | tbench.ai leaderboard | Confirmed |
| Factory Droid + GPT-5.3-Codex: 77.3% ±2.2 (rank 7) | tbench.ai leaderboard | Confirmed |
| Junie CLI + Multiple: 71.0% ±2.9 (rank 15) | tbench.ai leaderboard | Confirmed |
| Factory Droid + Opus 4.6: 69.9% ±2.5 (rank 17) | tbench.ai leaderboard | Confirmed |
| Claude Code + Opus 4.6: 58.0% ±2.9 (rank 40) | tbench.ai leaderboard | Confirmed |
| OpenHands + Opus 4.5: 51.9% ±2.9 (rank 51) | tbench.ai leaderboard | Confirmed |
| TB2.0 total entries: 124 (post-integrity update) | tbench.ai | Confirmed |
| OB-1/OpenBlock and Pilot/QuantFlow: removed for cheating | tbench.ai/news/leaderboard-integrity-update | Confirmed |
| ForgeCode: retained, reward hacking classification | tbench.ai/news/leaderboard-integrity-update | Confirmed |
| ForgeCode official rebuttal: tusharmath, GitHub issue #2961 | github.com/tailcallhq/forgecode/issues/2961 | Confirmed |
| Scaffold premium: ForgeCode+Gemini 78.4% vs Google Gemini ~68.5% | forgecode.dev/blog; tbench.ai data | Confirmed |
| Google's Gemini 3.1 Pro direct entry: ~68.5% | morphllm.com terminal-bench analysis | Secondary (~) |

### Sources: Agent Inventory

| Agent | Primary Source | Status |
|---|---|---|
| ForgeCode | antinomyhq/forgecode (GitHub), forgecode.dev | Confirmed (open-source, commercial) |
| OpenHands | all-hands-ai/openhands (GitHub), openhandsai.com | Confirmed (open-source) |
| Augment Code | augmentcode.com, augmentcode.com/blog/auggie-tops-swe-bench-pro | Confirmed (commercial) |
| Cursor Background Agent | cursor.com | Confirmed (commercial) |
| Claude Code | anthropic.com/claude-code | Confirmed (commercial) |
| Devin 2.0 | cognition.ai/blog/swe-bench-technical-report | Confirmed (commercial) |
| Factory Droid | factory.ai/news/code-droid-technical-report | Confirmed (commercial) |
| Amazon Q Developer | aws.amazon.com/q/developer | Confirmed (commercial) |
| SWE-agent | github.com/SWE-agent/SWE-agent | Confirmed (research/open-source) |
| Aider | aider.chat, github.com/paul-gauthier/aider | Confirmed (open-source) |
| AutoCodeRover | github.com/AutoCodeRoverSG/auto-code-rover | Confirmed (research/open-source) |
| Cline | github.com/saoudrizwan/claude-dev | Confirmed (open-source) |
| Agentless | github.com/OpenAutoCoder/Agentless | Confirmed (research/open-source) |
| Junie CLI | jetbrains.com | Confirmed (commercial) |
| Composio SWE-Kit | composio.dev | Confirmed (commercial) |
| TongAgents | ByteDance SE Lab publications | Confirmed leaderboard presence; no public product |
| SageAgent | tbench.ai leaderboard only | No developer confirmed |

---

## Run 2 — Benchmark Discovery Research

### Key Findings and Sources

| Benchmark | URL | Relevance | Source for Claim |
|---|---|---|---|
| SWE-bench Pro | labs.scale.com/leaderboard/swe_bench_pro_public | Reserved (priority) | morphllm.com/swe-bench-pro; Scale AI labs |
| SWE-bench Multilingual | swebench.com/multilingual-leaderboard.html | Reserved | swebench.com official |
| Multi-SWE-bench | multi-swe-bench.github.io | Reserved | arXiv:2504.02605 (ByteDance) |
| SWE-rebench | swe-rebench.com | Reference (model-level scaffold) | swe-rebench.com leaderboard |
| SWE-bench-Live | swe-bench-live.github.io | Watch list | NeurIPS 2025 paper; GitHub |
| SWE-EVO (48 tasks) | github.com/SWE-EVO/SWE-EVO | Watch list | arXiv:2512.18470 |
| FeatureBench | github.com/LiberCoders/FeatureBench | Watch list | arXiv:2602.10975 (ICLR 2026) |
| DevOps-Gym | devops-gym.com | Watch list | arXiv:2601.20882 (ICLR 2026) |
| MLE-bench | mlebench.com; github.com/openai/mle-bench | Watch list (frozen) | arXiv:2410.07095 (ICLR 2025) |
| RE-Bench | metr.org/blog/2024-11-22; github.com/METR/RE-Bench | Watch list (restricted) | arXiv:2411.15114 |
| HCAST | metr.org/hcast.pdf | Watch list (restricted) | arXiv:2503.17354 |
| PR Arena | prarena.ai | Reference (deployment signal) | prarena.ai live data |
| SWE-bench+ (contamination) | openreview.net/forum?id=R40rS2afQ3 | Methodology input | ICLR 2026 submission |
| Aider Polyglot | aider.chat/docs/leaderboards | Excluded (model-level) | aider.chat |
| BigCodeBench | bigcode-bench.github.io | Excluded (model-level) | bigcode-bench.github.io |
| LiveCodeBench | livecodebench.github.io | Excluded (model-level) | livecodebench.github.io |

### Critical Benchmark Findings

| Finding | Source | Impact on Framework |
|---|---|---|
| SWE-V contamination: same models score ~11 pp lower on SWE-Pro | OpenAI internal audit (2025); morphllm.com | SWE-Pro elevated to 20% weight (reserved) |
| FeatureBench: Claude Opus 4.5 scores 74.4% SWE-V but only 11.0% FeatureBench | arXiv:2602.10975 (ICLR 2026) | Documented in limitations.md §14.1; watch list |
| DevOps-Gym: OpenHands+Claude scores 70.4% SWE-V but only 23.87% on Java/Go DevOps | arXiv:2601.20882 (ICLR 2026) | Documented in limitations.md §14.2; watch list |
| SWE-EVO: GPT-5+OpenHands scores ~65% SWE-V but 21% on long-horizon evolution | arXiv:2512.18470 | Documented in insights.md §12.6 |
| PR Arena: Codex has 4.17M PRs (87.2% merge); Devin has 101K PRs (60.9% merge) | prarena.ai (live, April 27, 2026) | Reference signal in insights.md §12.8 |
| MLE-bench submissions frozen pending v2 process | mlebench.com (April 24, 2026) | Watch list; cannot activate until v2 opens |
| SWE-rebench uses standardized scaffold → model-level, not agent-level | swe-rebench.com methodology | Excluded from scored dimensions; reference-only |
| Aider Polyglot: Aider is fixed scaffold; tests models, not agents | aider.chat/docs/leaderboards | Excluded from cohort (model-level benchmark) |

---

## Data Confidence Classification

| Level | Symbol | Definition | Usage |
|---|---|---|---|
| Confirmed | (no symbol) | Score appears on primary named leaderboard or in official agent/developer publication | Full weight in scoring |
| Secondary | ~ | Score from third-party aggregator, indirect reference, or secondary report; not verified at primary leaderboard | Included in scoring with ~ annotation; verify at primary before removing ~ |
| Provisional | † | Official score with a specific caveat requiring explanation (integrity ruling, version ambiguity) | Included in scoring; caveat documented in limitations.md |
| Missing | ⊘ | No data available | Neutral-50 applied |
| Reserved | (dim. ⊘) | Dimension not activated; entire dimension at neutral-50 | Flat 20.0 pts (non-differentiating) |

---

## Key URLs for Ongoing Verification

| Resource | URL | Update Frequency |
|---|---|---|
| Terminal-Bench 2.0 leaderboard | tbench.ai/leaderboard/terminal-bench/2.0 | Continuous |
| SWE-bench Verified leaderboard | swebench.com/verified.html | Continuous |
| SWE-bench Pro leaderboard | labs.scale.com/leaderboard/swe_bench_pro_public | As submissions arrive |
| SWE-bench Multilingual leaderboard | swebench.com/multilingual-leaderboard.html | As submissions arrive |
| Multi-SWE-bench leaderboard | multi-swe-bench.github.io | As submissions arrive |
| Awesome Agents SWE-bench tracker | awesomeagents.ai/leaderboards/swe-bench-coding-agent-leaderboard/ | Weekly |
| TB2.0 integrity news | tbench.ai/news/ | As incidents arise |
| PR Arena live data | prarena.ai | Every 3 hours |
| HAL cost tracking | hal.cs.princeton.edu | As benchmarks are evaluated |
