# Coding Agent ValueRank — Benchmark Landscape
**Research provenance: Run 2 (ultradeep, 2 parallel agents, April 27, 2026)**

← [README](README.md) · [Methodology](methodology.md) · [Limitations](limitations.md)

---

## Overview

This document catalogues every benchmark evaluated during research as a candidate for inclusion in Coding Agent ValueRank. Two benchmarks are currently active (producing ranked lists). All others are classified below with the specific reason they are not currently scored.

---

## Active Benchmarks (Producing Ranked Lists)

### Terminal-Bench 2.0

| Property | Detail |
|---|---|
| URL | tbench.ai/leaderboard/terminal-bench/2.0 |
| Tasks | 89 tasks — software engineering, biology, security, gaming |
| Environment | Docker containers; time-based execution (not turn-based) |
| Evaluation | Automated correctness via human-written reference solutions |
| Submissions | 124 total as of April 27, 2026 (post-integrity update) |
| Agent-scaffold-level | ✅ Yes — each submission is a specific (agent, model) pair |
| Cohort entries | 11 |
| Primary source | tbench.ai — confirmed primary leaderboard |

**Why primary:** The only major benchmark explicitly designed for terminal/CLI-native autonomous agents. Tests long-horizon multi-step execution in real environments. Strongest anti-gaming infrastructure (ATIF trajectory requirements). Post-integrity-update scores are cleaned.

---

### SWE-bench Verified

| Property | Detail |
|---|---|
| URL | swebench.com/verified.html |
| Tasks | 500 human-validated GitHub issue resolution tasks |
| Environment | Python repositories (12 popular repos) |
| Evaluation | Fail-to-pass test execution after agent patch |
| Submissions | 100+ as of April 2026 |
| Agent-scaffold-level | ✅ Yes — submissions identify specific agent configurations |
| Cohort entries | 13 |
| Primary source | swebench.com — confirmed primary leaderboard (JS-rendered) |
| Agent-level tracker | awesomeagents.ai — third-party aggregator (~) |

**Contamination notice:** OpenAI confirmed training data leakage; same models score ~11 pp lower on SWE-bench Pro. Scores above ~65% should be interpreted with caution. See limitations.md §14.1.

---

## Pending — Insufficient Cohort Entries

These benchmarks are agent-scaffold-level and have active leaderboards, but fewer than 4 current cohort (agent, model) pairs have submitted. They will activate as additional ranked lists when the threshold is met.

### SWE-bench Pro

| Property | Detail |
|---|---|
| URL | labs.scale.com/leaderboard/swe_bench_pro_public |
| Tasks | 1,865 tasks — Python, Go, TypeScript, JavaScript (41 repos) |
| Contamination resistance | High — held-out tasks, not in training data |
| Cohort entries | 2 (Augment Code ~51.8%~, Amazon Q 28.8%) |
| Activation threshold | ≥4 cohort entries |
| Priority | **High** — primary anti-contamination signal |

The 11 pp gap between SWE-V and SWE-Pro scores for the same models is the clearest quantitative evidence of SWE-V contamination. SWE-Pro is the intended successor signal.

### SWE-bench Multilingual

| Property | Detail |
|---|---|
| URL | swebench.com/multilingual-leaderboard.html |
| Tasks | 300 tasks across 9 programming languages |
| Cohort entries | 0 |
| Activation threshold | ≥4 cohort entries |
| Priority | **High** — cross-lingual generalization signal |

Documented gap: SWE-agent + Claude 3.7 Sonnet scores 63% on SWE-bench Verified but only 43% on Multilingual — a 20 pp scaffold-level Python specialization penalty.

### Multi-SWE-bench

| Property | Detail |
|---|---|
| URL | multi-swe-bench.github.io |
| Tasks | 1,632 instances — Java, TypeScript, JavaScript, Go, Rust, C, C++ |
| Source | arXiv:2504.02605 (ByteDance) |
| Cohort entries | 0 |
| Activation threshold | ≥4 cohort entries |
| Priority | **Medium** — enterprise language coverage |

Particularly relevant for Java-heavy enterprise deployments where SWE-bench Verified's Python focus provides no signal.

---

## Watch List — Paper-Only, No Live Leaderboard

These benchmarks are agent-scaffold-level and provide important capability signals, but have no open submission portal. Scores exist only for the specific (agent, model) pairs evaluated in the originating papers. They will activate when either a community leaderboard launches or cohort entries are directly evaluated against the benchmark tasks.

**Data policy:** Scores from these benchmarks are not incorporated into ranked lists under the current exact-(agent, model)-match requirement. They are documented here and in insights.md §12.5 as capability context.

### FeatureBench

| Property | Detail |
|---|---|
| URL | github.com/LiberCoders/FeatureBench |
| Source | arXiv:2602.10975 (ICLR 2026) |
| Tasks | Multi-file feature development from natural language descriptions |
| Agent-scaffold-level | ✅ Yes — tested Claude Code, OpenHands, Codex (OpenAI framework), Gemini-CLI |
| Cohort matches (exact) | 1 — OpenHands v2 + Opus 4.5 → 10.5% |

**Key finding — the long-horizon cliff:**

| Agent + Model | SWE-V Score | FeatureBench Score | Drop |
|---|---|---|---|
| Claude Code + Opus 4.5 | 74.4% | **11.0%** | −63.4 pp |
| Codex + GPT-5.1-Codex | ~70% | **12.5%** | −57.5 pp |
| OpenHands + Opus 4.5 | ~68% | **10.5%** | −57.5 pp |
| Gemini-CLI + Gemini-3-Pro-Preview | ~60% | **5.0%** | −55 pp |

FeatureBench is the strongest evidence that SWE-V and TB2.0 scores do not generalize to multi-file, sustained development tasks. All tested agents collapse to 5–13% regardless of their SWE-V tier.

**Activation blocker:** No open submission infrastructure; paper-only data. Exact cohort match count: 1 (insufficient for a ranked list requiring n≥2).

---

### DevOps-Gym

| Property | Detail |
|---|---|
| URL | devops-gym.com |
| Source | arXiv:2601.20882 (ICLR 2026) |
| Tasks | Java/Go DevOps — Build & Config, Monitoring, Issue Resolving, Test Generation |
| Agent-scaffold-level | ✅ Yes — tested Claude Code, OpenHands (5 models), mini-SWE-Agent, Aider |
| Cohort matches (exact) | 0 — paper used Claude-4-Sonnet; cohort entries use Opus 4.6 or Sonnet 4.5 |

**Selected scores (Issue Resolving task, most relevant):**

| Agent + Model | Issue Resolving Score |
|---|---|
| Claude Code + Claude-4-Sonnet | 23.87% |
| OpenHands + Claude-4-Sonnet | 23.87% |
| mini-SWE-Agent + Claude-4-Sonnet | 5.16% |
| Aider + Claude-4-Sonnet | 9.67% |

**End-to-end pipeline (all 4 stages sequentially):** 0% for all agents tested.

**Activation blocker:** No open submission infrastructure. No exact (agent, model) cohort matches — paper used Claude-4-Sonnet throughout; cohort entries use different model tiers or versions.

---

### SWE-EVO

| Property | Detail |
|---|---|
| URL | github.com/SWE-EVO/SWE-EVO |
| Source | arXiv:2512.18470 |
| Tasks | 48 long-horizon software evolution tasks |
| Agent-scaffold-level | ✅ Yes — tested OpenHands (CodeActAgent) and SWE-agent across 18 models |
| Cohort matches (exact) | 0 — OpenHands+GPT-5.4 and SWE-agent+GPT-5.2 tested; cohort has different pairings |

**Selected scores:**

| Agent + Model | SWE-EVO Score |
|---|---|
| OpenHands + GPT-5.4 | 25.0% |
| SWE-agent + GPT-5.2 | 22.92% |
| glm-4p7 + SWE-agent | **39.58%** (highest on leaderboard) |

**Note:** glm-4p7 + SWE-agent leads SWE-EVO despite neither appearing in the TB2.0 or SWE-V top tiers — a further illustration of benchmark-specific specialization.

**Activation blocker:** No open submission infrastructure. No exact cohort matches.

---

## Watch List — Access-Restricted

These benchmarks exist and have published results but cannot be openly evaluated against.

### MLE-bench

| Property | Detail |
|---|---|
| URL | github.com/openai/mle-bench; mlebench.com |
| Source | arXiv:2410.07095 (ICLR 2025) |
| Tasks | Kaggle ML competitions — medal-rate scoring |
| Agent-scaffold-level | ✅ Yes — tested AIDE, OpenHands, MLAB |
| Cohort matches (exact) | 0 — tested with GPT-4o; cohort uses Opus 4.5/4.6 |
| Status | Submissions frozen as of April 2026 (pending v2 overhaul) |

**Selected scores (any-medal rate, Low-difficulty competitions):**

| Agent + Model | Any Medal (Low) | Medium | High |
|---|---|---|---|
| AIDE + o1-preview | 35.91% | 8.45% | 11.67% |
| OpenHands + GPT-4o | 12.12% | 1.75% | 2.22% |

**Activation blocker:** Submissions frozen. No exact cohort matches. Will reactivate when OpenAI opens v2 submission process.

### RE-Bench (METR)

| Property | Detail |
|---|---|
| URL | metr.org/blog/2024-11-22 |
| Source | arXiv:2411.15114 |
| Tasks | 7 environments — ~71% ML research engineering, ~29% software engineering |
| Agent-scaffold-level | ✅ Yes — METR evaluated Claude 3.5 Sonnet with tool access |
| Cohort matches | 0 — no named agent scaffold; basic bash/file/Python tools only |
| Status | METR-internal only; no open submission portal |

**Why not activated:** Task composition is predominantly ML research (not SWE); no open submission infrastructure; no named agent scaffold tested.

### HCAST (METR)

| Property | Detail |
|---|---|
| URL | metr.org/hcast.pdf |
| Source | arXiv:2503.17354 |
| Tasks | 189 tasks — ML Engineering (~31%), SWE (~21%), Data Science (~25%), Other |
| Cohort matches | 0 — GPT-4o and Claude 3.5/3.7 Sonnet evaluated; no named scaffolds |
| Status | Task set restricted to prevent gaming; no published per-model numeric scores |

**Why not activated:** ~21% SWE tasks (insufficient signal); no per-model scores published; restricted access.

---

## Excluded — Model-Level (Not Agent-Scaffold-Level)

These benchmarks test base model capability using a standardized or fixed scaffold. They cannot differentiate between different agent scaffolds using the same model, which is the core signal ValueRank measures.

| Benchmark | URL | Why Excluded |
|---|---|---|
| **SWE-rebench** | swe-rebench.com | Standardized 128K ReAct scaffold for all submissions — tests models, not scaffolds. ForgeCode and Cline would get identical scaffolds. |
| **Aider Polyglot** | aider.chat/docs/leaderboards | Aider is the fixed scaffold; leaderboard tests which model Aider should use, not which agent is best. |
| **BigCodeBench** | bigcode-bench.github.io | Pure model-level function completion; no agent scaffolding component. |
| **LiveCodeBench** | livecodebench.github.io | Competitive programming style; model-level, no agent scaffold. |

---

## Reference Only — Deployment Signal

### PR Arena

| Property | Detail |
|---|---|
| URL | prarena.ai |
| Update frequency | Every 3 hours |
| Data | Real-world GitHub PR creation and merge rates by agent |

**Selected data (April 27, 2026):**

| Agent | Ready PRs | Merge Rate |
|---|---|---|
| GitHub Copilot | 1,346,979 | 95.9% |
| OpenAI Codex | 4,177,715 | 87.2% |
| Cursor | ~980,000 | ~91.4% |
| Devin | 101,645 | 60.9% |

**Why reference-only:** Does not control for task difficulty, repository complexity, or deliberate use-case targeting (Copilot users likely submit simpler tasks). High merge rate may reflect easy task selection, not agent quality. Real-world deployment scale signal only.

---

## Benchmark Activation Summary

| Benchmark | Type | Cohort Entries | Activation Status |
|---|---|---|---|
| Terminal-Bench 2.0 | Agent-level | 11 | ✅ **Active** |
| SWE-bench Verified | Agent-level | 13 | ✅ **Active** |
| SWE-bench Pro | Agent-level | 2 | ⏳ Pending — need ≥4 |
| SWE-bench Multilingual | Agent-level | 0 | ⏳ Pending — need ≥4 |
| Multi-SWE-bench | Agent-level | 0 | ⏳ Pending — need ≥4 |
| FeatureBench | Agent-level | 1 (exact match) | 🚫 No live leaderboard; 1 match |
| DevOps-Gym | Agent-level | 0 (exact match) | 🚫 No live leaderboard; 0 matches |
| SWE-EVO | Agent-level | 0 (exact match) | 🚫 No live leaderboard; 0 matches |
| MLE-bench | Agent-level | 0 (exact match) | 🚫 Submissions frozen |
| RE-Bench | Agent-level | 0 | 🚫 METR-internal only |
| HCAST | Agent-level | 0 | 🚫 Restricted; <25% SWE tasks |
| SWE-rebench | Model-level | — | ❌ Wrong granularity |
| Aider Polyglot | Model-level | — | ❌ Wrong granularity |
| BigCodeBench | Model-level | — | ❌ Wrong granularity |
| LiveCodeBench | Model-level | — | ❌ Wrong granularity |
| PR Arena | Deployment signal | — | 📊 Reference only |
