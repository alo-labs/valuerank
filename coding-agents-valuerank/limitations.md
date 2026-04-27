# Coding Agent ValueRank — Limitations & Known Gaps
**Updated per version**

← [README](README.md) · [Scores](scores.md) · [Insights](insights.md)

---

## §14. Known Limitations

### 14.1 SWE-bench Verified Contamination

**Severity: High.** OpenAI confirmed in 2025 that frontier models have training data leakage into SWE-bench Verified. The same models score approximately 11 percentage points lower on SWE-bench Pro (contamination-resistant, held-out tasks) than on SWE-bench Verified.

**Impact on v1.0:** Any SWE-V score above ~65% should be interpreted with caution. The top-tier scores (Augment Code 72.0%, OpenHands v3 68.4%, Amazon Q 66.0%) are plausible for capable agents with strong scaffolds but may be partially inflated by base model memorization of SWE-bench training-adjacent patterns.

**Mitigations in place:**
- SWE-bench Pro is tracked as a pending benchmark list; once ≥4 cohort entries submit, it will be the primary anti-contamination signal
- SWE-rebench (reference-only) provides a contamination-controlled cross-check: the best pass@1 score on SWE-rebench's standardized 57-task set (65.3%) is substantially below SWE-V top scores for equivalent models
- Per-entry annotations distinguish ~ (secondary/indirect source) from primary leaderboard data

**SWE-bench+ (ICLR 2026) finding:** 60.83% of SWE-bench "resolved" issues contain solution leakage in issue text or comments; 47.93% of resolved issues use weak test cases that fail to detect incorrect patches. When filtered, resolution rates drop from ~51.7% to ~25.9% on Verified. This is the strongest quantitative evidence of the contamination problem.

**Recommendation:** Weight SWE-V scores at face value for relative comparisons within the same benchmark, but do not equate a 70% SWE-V score with "70% of real-world GitHub issues resolved."

---

### 14.2 SWE-bench Benchmark Coverage Gap (Python-only)

**Severity: Medium.** Both SWE-bench Verified and SWE-bench Pro (as of v1.0 data collection) are heavily Python-weighted. Real-world production software engineering spans Java, TypeScript, Go, Rust, C/C++, and other languages. An agent scoring 70% on SWE-bench Verified may score 30–43% on SWE-bench Multilingual (same model, same scaffold — the gap is documented for SWE-agent+Claude 3.7 Sonnet: 63% Verified vs. 43% Multilingual).

**Impact:** Rankings for teams working primarily in non-Python languages should discount SWE-V scores. Terminal-Bench 2.0 does include non-Python tasks (biology, security, gaming) which partially mitigates this. SWE-bench Multilingual and Multi-SWE-bench will address this gap directly once ≥4 cohort entries submit to each.

---

### 14.3 ForgeCode Integrity Controversy

**Severity: Medium.** ForgeCode (Antinomy) was involved in a disputed integrity incident on Terminal-Bench 2.0 prior to the April 19, 2026 tbench.ai integrity update.

**Full account:**

**DebugML investigation (published ~April 2026):** Claimed ForgeCode's AGENTS.md auto-constructed by its agent contained pre-loaded answer keys (cached solutions from the internet), violating TB2.0 rules. Estimated "clean" corrected score: 71.7%, rank 14. Method: reconstructed ForgeCode's AGENTS.md and observed cached solutions.

**ForgeCode's official rebuttal (tusharmath, GitHub issue #2961, April 18, 2026):**
1. DebugML never ran ForgeCode with ForgeCode Services enabled (the proprietary backend that powers production ForgeCode performance); their reconstruction did not replicate the actual agent
2. No traffic spike to external endpoints was detected during the flagged TB2.0 runs
3. The 71.7% corrected estimate is not independently reproducible
4. Full execution traces were published publicly for community verification

**tbench.ai integrity ruling (April 19, 2026):**
- Classification: **Reward hacking** (not cheating)
- Action: Specific trials zeroed; ForgeCode retained on leaderboard
- Definition used: Cheating = modification of evaluation infrastructure (OB-1, QuantFlow → removed); Reward hacking = agent behavior that exploits benchmark structure without directly accessing solutions (ForgeCode → zeroed trials, not removed)
- Distinction from DebugML narrative: tbench.ai's description is "AGENTS.md curling solutions from the internet" (at run time, not pre-loaded), technically different from DebugML's pre-loaded answer key claim

**Current status:** The post-correction scores displayed on tbench.ai (81.8%, 79.8%, 78.4%) are the authoritative validated figures. ValueRank uses these as official scores. The integrity controversy is noted via the † flag.

**Impact on TB2.0 ranking:** ForgeCode occupies TB2.0 ranks 2, 4, and 5.5 (tied). If DebugML's 71.7% estimate were used instead of the official 81.8%, ForgeCode+GPT-5.4 would drop from TB2.0 rank 2 to rank 7. See insights.md §12.7 for full sensitivity analysis.

---

### 14.4 SageAgent — Unknown Developer

**Severity: Low.** SageAgent + GPT-5.3-Codex (TB2.0 rank 5.5, 78.4%) appears on the tbench.ai leaderboard with a confirmed score but no publicly identifiable developer, company, or product page. It may be an internal evaluation submission from an organization that has not made their agent publicly available.

**Impact:** TB2.0 rank 5.5 is accurate for leaderboard performance. Users cannot adopt SageAgent as a tool; it is included for ranking completeness. If SageAgent is later removed or found to violate rules, ranks below it shift up by one position.

---

### 14.5 Amazon Q Developer — Version Ambiguity

**Severity: Medium.** The SWE-bench Verified score (66.0%, April 2025) for Amazon Q Developer is from an agent version not precisely identified in public documentation. Amazon has released multiple versions:
- v20240430: 25.6% SWE-V
- v20240719: 38.8% SWE-V
- April 2025 version: 66.0% SWE-V (substantial improvement; model identity "Proprietary")

The April 2025 version is treated as the authoritative current score. The large gap from 38.8% to 66.0% in under a year suggests either a new model architecture or a significantly improved agent scaffold — the improvement is documented but the mechanism is not publicly disclosed.

---

### 14.6 Single-Benchmark Dependency — No True Cross-Benchmark Comparison

**Severity: High.** Only 1 of 22 cohort entries (Factory Droid + GPT-5.3-Codex) has confirmed scores on both active benchmarks, and even that SWE-V score is from a secondary source (~). This is the primary reason ValueRank publishes two separate ranked lists rather than a composite score.

**Consequence:** Comparing a TB2.0 leader against a SWE-V leader requires assumptions about relative benchmark value that are not grounded in empirical cross-benchmark data. Factory Droid is the proof of concept for dual-benchmark presence; Codex (OpenAI), OpenHands v3, and Claude Code are the highest-priority targets for cross-benchmark data collection.

---

### 14.7 Research Benchmark Exclusions

**Severity: Low.** Several research-oriented benchmarks evaluate coding agents on relevant tasks but are not currently activatable:

- **MLE-bench:** Frozen submissions as of April 2026 (pending v2 overhaul); no exact cohort (agent, model) matches in current paper data
- **RE-Bench (METR):** Only 7 environments; predominantly ML research tasks (~71%); no open submission portal
- **HCAST (METR):** Task set restricted; ~20% software engineering tasks; no published per-model scores
- **FeatureBench / DevOps-Gym / SWE-EVO:** Paper-only; no exact (agent, model) pair matches to current cohort under the exact-match data policy

See [benchmarks.md](benchmarks.md) for full landscape and activation criteria.

---

### 14.8 PR Arena — Not a Scientific Benchmark

**Severity: Informational.** PR Arena (prarena.ai) tracks real-world GitHub PR creation and merge rates by agent. It shows:
- GitHub Copilot coding agent: 1,346,979 ready PRs, 95.9% merge rate
- OpenAI Codex: 4,177,715 ready PRs, 87.2% merge rate
- Devin: 101,645 ready PRs, 60.9% merge rate

This data is real-world production signal but does not control for task difficulty, repository complexity, or deliberate use-case targeting. It is cited in profiles.md as deployment scale context only.

---

### 14.9 SWE-V Scores: awesomeagents.ai Is a Secondary Source

**Severity: Medium.** 8 of 13 SWE-V scores are sourced from awesomeagents.ai, a third-party aggregator (published April 19, 2026). This site explicitly describes itself as compiling scores from official sources — it is not the primary leaderboard (swebench.com/verified.html). All awesomeagents.ai-sourced scores carry ~ throughout the documents.

**Affected entries:** Augment Code, OpenHands v3, Amazon Q, Cursor, Composio, Cline, SWE-agent, AutoCodeRover (all ~).

**Primary-source scores in this cohort:** Devin 2.0 (cognition.ai/blog) and Aider (swebench.com direct). Factory Droid and OpenHands v2 SWE-V scores are from a separate third-party aggregator (~).

**Priority action for v1.1:** Verify all SWE-V scores directly against swebench.com/verified.html. The interactive leaderboard requires JS rendering; a direct scrape or manual verification is needed.

---

### 14.10 TB2.0 Confidence Intervals — Top 7 Statistically Indistinguishable

**Severity: Medium.** TB2.0 scores include ±confidence intervals. The top 7 entries have overlapping intervals at 1σ:

| Entry | Score | ±CI | Interval |
|---|---|---|---|
| Codex + GPT-5.5 | 82.0% | ±2.2 | [79.8%, 84.2%] |
| ForgeCode + GPT-5.4† | 81.8% | ±2.0 | [79.8%, 83.8%] |
| TongAgents + Gemini | 80.2% | ±2.6 | [77.6%, 82.8%] |
| ForgeCode + Opus 4.6† | 79.8% | ±1.6 | [78.2%, 81.4%] |
| SageAgent | 78.4% | ±2.2 | [76.2%, 80.6%] |
| ForgeCode + Gemini† | 78.4% | ±1.8 | [76.6%, 80.2%] |
| Factory Droid + GPT-5.3 | 77.3% | ±2.2 | [75.1%, 79.5%] |

Every top-7 entry overlaps with at least its neighbors. The ordinal rankings (rank 1 through 7) are point-estimate orderings of measurements that are statistically indistinguishable at 1σ. The ranking conveys precision that the data does not support for these positions.

---

### 14.11 Junie CLI Violates (Agent, Model) Pair Convention

**Severity: Medium.** The ranking unit is defined as (agent, model) pairs. Junie CLI is entered as "Junie CLI + Multiple" — JetBrains has not publicly identified the specific base model(s) used in their TB2.0 submission. This entry does not conform to the convention. It is retained pending model identification from JetBrains or leaderboard metadata disclosure.

---

## §15. Benchmark Integrity Reference

| Agent | Benchmark | Allegation | Classification | Outcome | Authoritative Source |
|---|---|---|---|---|---|
| OB-1 (OpenBlock) | TB2.0 | Stored encrypted solutions in binary; modified timeouts on TB1.0 | Cheating | Permanently removed | tbench.ai/news/leaderboard-integrity-update |
| Pilot (QuantFlow) | TB2.0 | Uploaded tests/ folder as part of agent setup | Cheating | Permanently removed; invited to resubmit | tbench.ai/news/leaderboard-integrity-update |
| ForgeCode | TB2.0 | AGENTS.md curled solutions from internet during flagged trials | Reward hacking | Affected trials zeroed; retained on leaderboard | tbench.ai/news/leaderboard-integrity-update |

---

## §16. Future Benchmark List Candidates

Full landscape with research provenance: [benchmarks.md](benchmarks.md)

| Benchmark | Signal | Current Blocker | Activation Trigger |
|---|---|---|---|
| SWE-bench Pro | Contamination-resistant resolution, multi-language | <4 cohort entries | ≥4 agents submit to labs.scale.com |
| SWE-bench Multilingual | Cross-lingual generalization (9 languages) | 0 cohort entries | ≥4 agents submit to official leaderboard |
| Multi-SWE-bench | Enterprise-language resolution (Java/Go/TS/Rust) | 0 cohort entries | ≥4 agents submit to HuggingFace leaderboard |
| MLE-bench | ML engineering autonomy | Submissions frozen | OpenAI resumes v2 submissions |
| FeatureBench | Long-horizon feature development | No exact cohort matches; no live leaderboard | Community leaderboard + cohort entries tested |
| DevOps-Gym | Java/Go DevOps tasks | No exact cohort matches; no live leaderboard | Community leaderboard + cohort entries tested |
