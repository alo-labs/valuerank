# DR-PLAN — Research plan

**Mode rationale.** `deep`: the answer shapes ValueRank's positioning (hard to reverse once published), vendor pages overstate their own rigour (conflicting evidence expected), and the landscape is fast-moving (recency risk). `ultradeep` is not needed: no strategic commitment or high blast radius follows directly from this record.

## Source classes

| Class | Examples | Role | Expected grade |
|---|---|---|---|
| Primary: the sites themselves | leaderboard pages, methodology/FAQ pages, pricing pages, changelogs | What each site actually ranks and how it treats cost | B1–B2 (official but self-interested) |
| Primary: benchmark owners | Artificial Analysis, LMArena, Epoch AI, Scale SEAL, Vals.ai, LiveBench, SWE-bench, Terminal-Bench, Aider | Cost views and methodology | A2–B2 |
| Secondary: independent analyses | SemiAnalysis, Epoch AI reports, academic papers on cost-aware evaluation, developer blogs with measurements | Validation of claims, allowance measurements | B2–C2 |
| Tertiary: community and press | Hacker News, Reddit, X threads, newsletters, product directories | Discovery of lesser-known sites, user perception | C3–D3 (discovery only) |
| Local | ValueRank's own methodology, plan route evidence, research ledgers | Baseline for comparison | A1 for the baseline |

## Search strategy (parallel)

1. **Core semantic**: "LLM ranking by value", "best AI model for the money ranking", "price performance leaderboard LLM".
2. **Technical/keyword**: "cost per task leaderboard", "intelligence per dollar", "tokens per dollar benchmark", "Pareto frontier LLM cost quality".
3. **Recent (2025–2026)**: new leaderboards and indices with cost axes; changes at Artificial Analysis, LMArena, Epoch, Scale, Vals, OpenRouter.
4. **Subscription plans**: "ChatGPT vs Claude plan value comparison", "usage limits tracker", "Claude Max allowance measured", "subscription API equivalent".
5. **Coding-agent value**: "coding agent cost per task leaderboard", "SWE-bench cost", "Terminal-Bench cost", "Aider leaderboard cost".
6. **Critical analyses**: criticisms of price-performance rankings, benchmark contamination, cost measurement pitfalls.
7. **Directories**: lists of LLM leaderboards and comparison sites (to catch long-tail sites).
8. **Non-US perspectives**: Chinese leaderboards (OpenCompass, SuperCLUE) and European comparisons with cost.

Retrieval agents (four, in parallel) each own one angle and return structured evidence; the lead runs the broad scan and merges.

## Triangulation approach

- Each site's cost treatment is confirmed from its own page (primary) and, where it feeds a core claim, from one independent description or measurement.
- Contradictions (for example, a site claiming "value" while ranking on list price only) are recorded in `triangulation.md` with grades.
- Allowance measurements are graded by evidence class consistent with ValueRank's policy (controlled measurement, user report, provider claim, assumption).

## Quality gates

- FFS threshold for deep mode: 25+ sources with average credibility > 70, or the full search set completed.
- Core claims require an A/B source or three C sources.
- Two adversarial critique cycles (skeptic, reviewer) before refine.
- Validation: `validate_report.py`, `verify_citations.py`, `verify_claim_support.py`, `phase_gate.py --mode deep`.

## Effort estimate

Retrieval 1–2 hours of agent time in parallel; triangulation, outline and synthesis one pass; critique two cycles; packaging and validation one pass with up to three repair loops.
