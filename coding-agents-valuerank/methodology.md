# Coding Agent ValueRank — Methodology
**Stable reference | Updates only on formula/protocol changes**

← [README](README.md) · [Raw Data](raw-data.md) · [Scores](scores.md)

---

## 1. What This Ranking Is — and Is Not

Coding Agent ValueRank publishes **two separate ranked lists**:

1. **Terminal-Bench 2.0 Ranking** — agents that have submitted to tbench.ai
2. **SWE-bench Verified Ranking** — agents that have submitted to swebench.com/verified

These are not combined into a composite score. The data does not support cross-benchmark comparison: as of v1.0, only 1 of 22 cohort entries (Factory Droid + GPT-5.3-Codex) has real scores on both benchmarks, and even that SWE-V score is from a secondary source. Merging two largely disjoint populations into a single number would encode a weight-based preference as if it were an empirical finding. It is not.

**What the two lists answer:** "Among agents that have submitted to TB2.0, which performs best?" and "Among agents that have submitted to SWE-V, which performs best?" These are meaningful questions. "Is Codex better than Augment Code overall?" is not answerable from current data.

**Cross-benchmark view:** A Pareto frontier analysis — which agents are not dominated on either axis — is provided in insights.md §12.7 as the most honest cross-benchmark statement the data supports.

---

## 2. Scoring Formula

Within each ranked list, all entries use rank-based normalization:

```
Normalized Score = ((n − rank) / (n − 1)) × 100
```

Where `n` is the number of (agent, model) pairs with real data on that benchmark. Scale-invariant: percentage resolution rates normalize identically regardless of benchmark. Rank 1 (best) always scores 100; rank n (worst) always scores 0.

**Missing data:** Entries without published results receive a neutral score of **50** (midpoint), marked **⊘**. Neither rewarded nor penalized for absence.

**Tied ranks:** Entries with identical raw scores receive the average of their tied ranks. Example: two entries both at 78.4% at ranks 5–6 each receive rank 5.5 → `((n−5.5)/(n−1)) × 100`.

---

## 3. Unit of Ranking

ValueRank for Coding Agents ranks **(agent, model) pairs**, not bare agent frameworks or base models.

The same scaffold with different base models produces meaningfully different results. ForgeCode + GPT-5.4 and ForgeCode + Claude Opus 4.6 are distinct ranked entries. This mirrors the Terminal-Bench 2.0 leaderboard convention and reflects the operational reality that deploying a coding agent always means choosing both the scaffold and the base model.

**Consequence:** A single vendor (e.g., Antinomy/ForgeCode) may appear multiple times in the same ranked list with different base models. The ranking answers "which complete agent system should I deploy?" not "which framework is best in the abstract."

---

## 4. Benchmark Coverage

| Benchmark | Status | Leaderboard | What It Measures |
|---|---|---|---|
| **Terminal-Bench 2.0** | **Active** (n=11) | tbench.ai | Terminal-native autonomy: 89 tasks across SWE, biology, security, gaming in Docker containers |
| **SWE-bench Verified** | **Active** (n=13) | swebench.com/verified | GitHub issue resolution: 500 human-validated tasks, Python repositories |
| SWE-bench Pro | Pending — <4 cohort entries | labs.scale.com | Contamination-resistant issue resolution, multi-language |
| SWE-bench Multilingual | Pending — 0 cohort entries | swebench.com/multilingual | Cross-lingual generalization (9 languages) |
| Multi-SWE-bench | Pending — 0 cohort entries | multi-swe-bench.github.io | Enterprise-language resolution (Java/Go/TS/Rust) |

Full benchmark landscape — including paper-only benchmarks, model-level benchmarks, and long-horizon capability research — is documented in [benchmarks.md](benchmarks.md).

---

## 5. Benchmark Activation Protocol

A new benchmark activates (gains its own ranked list) when **all three** conditions are met:

1. **≥4 cohort (agent, model) pairs** have published scores with exact agent+model identification
2. Scores come from a primary leaderboard or the benchmark's official paper with reproducible methodology
3. At least one pair currently in the top-5 of either active list has a confirmed score

When a benchmark activates:
- A new ranked list is published alongside the existing two
- Cross-benchmark Pareto analysis is updated
- Version increments (e.g., v1.0 → v1.1 for minor additions; v2.0 for new benchmark activation)

---

## 6. Agent Cohort Protocol

### What Qualifies as a "Pure Autonomous Agent"

An (agent, model) pair qualifies if the agent:

1. **Operates without human-in-the-loop** for individual code changes — receives a task, delivers a change, without mid-task approval requests
2. **Uses tool calls** to navigate the codebase (file reads, searches, terminal execution) rather than pure code completion
3. **Has at least one confirmed score** on a currently active benchmark

**Excluded categories:**
- IDE copilots requiring human approval for each edit (GitHub Copilot, Tabnine)
- Frontend/app generation tools (v0, Bolt.new, Lovable)
- Base model API calls without an agent scaffold

### Adding a New (Agent, Model) Pair

1. Verify the agent qualifies (§6 criteria)
2. Collect all available benchmark scores from primary sources
3. Mark unavailable benchmarks as ⊘
4. Full renormalization within each active benchmark: recompute all ranks → recompute all normalized scores
5. Increment minor version (v1.0 → v1.1)

### Removing an (Agent, Model) Pair

Removed if the agent is discontinued and no longer publicly accessible. Historical scores preserved in version history (scores.md §10).

---

## 7. Cost — Reference Only in v1.0

Cost per resolved task is tracked in raw-data.md but is **not a scored dimension in v1.0**.

**Why not scored:** Fewer than 4 cohort agents have published per-task cost estimates. Including cost with 18+ entries at neutral-50 would be non-differentiating.

**Activation threshold:** ≥4 cohort pairs publish average cost per resolved issue from official documentation, leaderboard metadata, or HAL Princeton per-problem cost tracking.

---

## 8. Notation

| Symbol | Meaning |
|---|---|
| **⊘** | Missing data; neutral score 50.0 applied |
| **~** | Secondary source (third-party tracker, aggregator, indirect report); probable confidence |
| **†** | Special annotation; see dimension-specific notes in raw-data.md |

---

## 9. Appendix

### 9A. Normalization Examples

**TB2.0 (n=11, April 2026)** — Formula: `((11−rank)/10) × 100`
- Codex + GPT-5.5: rank 1 → (10/10)×100 = **100.0**
- SageAgent & ForgeCode+Gemini tied at rank 5.5 → (5.5/10)×100 = **55.0** each
- OpenHands v2 + Opus 4.5: rank 11 → (0/10)×100 = **0.0**

**SWE-V (n=13, April 2026)** — Formula: `((13−rank)/12) × 100`
- Augment Code + Opus 4.6: rank 1 → (12/12)×100 = **100.0**
- Factory Droid + GPT-5.3-Codex: rank 7 → (6/12)×100 = **50.0** (coincides with neutral-50 value; this is a real score)
- Aider + Sonnet 4.5: rank 13 → (0/12)×100 = **0.0**

### 9B. Scheduled Review Cadence

| Trigger | Action |
|---|---|
| New major agent release | Add to cohort within 7 days; publish updated list within 14 days |
| New benchmark score confirmed | Update dimension n; full renormalization |
| Benchmark activation threshold met | Add new ranked list; increment major version |
| Quarterly | Verify all scores against primary leaderboards; update stale entries |

### 9C. (Agent, Model) Pairs vs. Agent Tiers

Some informal comparisons collapse model configurations into a single per-agent score. ValueRank does not.

**Why pairs?** The same OpenHands scaffold with different base models produces systems at different performance levels and price points. Collapsing them requires implicitly weighting model options in a way that is not shared across users. Explicit pairs let each user match the row to their intended deployment.

**Trade-off acknowledged:** A vendor with multiple model options (e.g., ForgeCode × 3) occupies multiple rows. This is accurate: ForgeCode + GPT-5.4 and ForgeCode + Gemini 3.1 Pro are genuinely different deployment choices.
