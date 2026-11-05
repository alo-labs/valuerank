# Internal review I39 — Claude Sonnet 5.5 (effort medium) on draft r98

## 0. Read check

- First line: "# ValueRank methodology — draft r98"
- Last line (the final folded line of the Known limitations paragraph): "configuration (O54, E252). Instruction following has no weight while Surge's Complex Constraints is excluded (O53). On the Plan basis the MiMo multiples are provider-derived quota ceilings, not measurements (O46)."
- Last 12 words of the last paragraph: "Plan basis the MiMo multiples are provider-derived quota ceilings, not measurements (O46)."
- Also read: `reviewer-prompt.md`; the whole folded draft (941 lines, in chunks); `ledger-brief.md`; `ledger.md` from "## Internal review I28" to the end (through I38 and O56-O58, E247-E263); `AGENTS.md`.
- Checked against repository data: `data/scores.json` (v3 and v3Tracks.aicd: bars, anchors and exchange rates, rank separability and bands, noise margin, clip-gate listed rows, cost influence, drift, measured-only Plan view, `aaPlottedNames`), `data/aa_frontier_capture.json` and `data/aa_reconciliation_inventory.json` (recomputed the cohort: 18 frontier + 11 near, gaps as stated, no missed near point), `data/swe_tracks.json`, and the age gates in `valuerank/*.py`. Every "today" figure I recomputed or looked up matches the data: 29 / 18 / 11 cohort, 9 and 15 ranked, 20 ranked at least once and 9 in neither, bars 49.76 / 60.72 / 62.12 and 38.00 / 49.24 / 57.16, bar reach 7/5/3 and 12/8/5, exchange rates 3.04 / 2.44 / 2.83 / 1.89, separability medians, counts and grids, all band ranges, the 4.02 and 5.87 noise margins and the bars plus margin, the O58 listed-row factors, variance allocations (65%, 2%, about -90%, -26%), the E242 tolerances (2.35, 5.28), and the E258 pair counts (15 and 30).

## 1. Findings by severity

**Critical**

None

**High**

None

**Medium**

1. **No freshness or capture-clock rule for the non-AA evidence that supplies 28% (max-effort) and 22% (AI Coding Daily) of quality, and for the gap-fill sources.**
   - Issue: The Governance paragraph "Freshness, by artifact (E216)" bounds only the AA model-page snapshot (45 days), the price records (7 days), the AA chart and catalog capture (E211, 7 days) and their mutual gap (E217, 7 days). The artifacts that carry Bug Hunt, Vals (Vibe Code Bench and Code Migration), LiveBench 2.0, AI Coding Daily, Cognition's FrontierCode board and tbench.ai have only "each artifact's capture time is in the evidence bundle; change-triggered refresh; monthly cadence". The build enforces nothing for them: `valuerank/value_v3.py` and `capture_aa.py` gate only the AA artifacts, the report search and the missing-leaf search log. The 7-day gate on the leaf search log (O36) covers leaves that are missing. It does not cover a leaf that is present but may since have been revised or superseded. Examples: Bug Hunt's E206 "largest-sample mean" selection reads a pinned scoreboard capture, so a new owner run of the same model and effort would not be seen. A Vals or AI Coding Daily record can be re-run. LiveBench ships new releases. A stale capture would silently pick the wrong record under rules the draft states exactly.
   - Related point: `data/swe_tracks.json` carries `capturedAt` 2026-10-23T08:00:00Z, which is 94 minutes after the release cutoff 2026-10-23T06:26:23Z that O47 sets and E213 says governs every gate. The draft names "published after the cutoff" as a rejection reason for open-web candidates (E240) but never says whether a non-AA capture taken after V may feed the release. The source "updated" dates (10-18 to 10-21) are before the cutoff, so no score is affected today, but a faithful implementer could reasonably either reject this artifact or accept it.
   - Why it hurts: this is a stated-but-unenforced evidence clock for a large share of quality weight, the same kind of gap the ledger treated as real for the AA snapshot (I-round entry adopted as E216). It is new since r88, because the added leaves and the Vals, LiveBench and AI Coding Daily sources entered with O53. Two faithful implementers would resolve it differently (no gate versus a 7-, 30- or 45-day gate; post-cutoff captures allowed or not).
   - Change: extend E216 with one row per non-AA source (Bug Hunt scoreboard, Vals boards, LiveBench release table, AI Coding Daily leaderboard, Cognition board, tbench.ai leaderboard, Xiaomi tier pages for the O46 ceilings). Each gets a maximum capture age at the release cutoff (suggest 7 days, matching the cohort capture and the search log, or 30 days, matching the report window; the owner or editor picks one) and a rule that the capture instant is at or before V. The build fails otherwise. Print the capture instants beside the leaf-source table. Re-stamp `swe_tracks.json` with the true capture instant (the value 08:00:00Z looks nominal). Either the cutoff moves or the capture is repeated at or before V.

**Low**

1. **Review-convergence wording (Governance, O56).** The draft says the work "completes after two clean rounds". O56 (ledger) says each ladder rung and each Perplexity model is done after two *consecutive* clean rounds, and a non-clean round is answered with a new draft before the next round. Add "consecutive" and "per rung and per model".
2. **Stale scope of "C_W" in the accounting-identities bullet.** "C_W takes the seven SDLC evaluations; C_Index = C_7 + … reconciled … and that residual never enters C_W" predates the Coding Agent Index. In the max-effort ranking C_W is eight components (the Cost bullet's own definition, "Σ over admitted basket components", governs). Reword to "C_W takes the Index's seven SDLC evaluations plus any admitted Coding Agent Index".
3. **Noise-margin sentence is ambiguous about what "today 4.0 and 5.9" is.** In the O44 bullet the margin is 1.96 × √2 × median SD, and "today 4.0 points … 5.9" sits inside the parenthesis that describes the SD. From the data, 4.02 and 5.87 are the *margin*; the median quality SD is about 1.45 and 2.07. Say "the margin is today 4.0 points … 5.9".
4. **E214 matching gap for an explicit "without fallback" record.** The rule says a record that states no fallback matches by model and effort, and the build stops on a with/without twin. It does not say what happens when a third-party record explicitly states "without fallback" for a model AA plots only "with fallback" (Opus 5.5 and Sonnet 5.5 today). Add one clause (no match without a dated decision, or match with a flag).
5. **Same-configuration plan rows: two statements read as different rules.** One bullet says a configuration's plan rows "separate whenever their values differ" (scenario counting), and E258 says the same pairs are "counted apart" and excluded from the separability statistics. Both are right in their contexts, but a pointer from the first to E258, or "in scenario shares" in the first, would remove the apparent conflict.

## 2. Methodology design recommendations

1. **(Priority 1, implementable now) Source-capture clocks table.** Implement Medium 1 as a data-driven check. Put every evidence artifact in `run_manifest.json` with `capturedAt`, `maxAgeDays` and `source`, and have `assemble` fail when `capturedAt > V` or `V - capturedAt > maxAgeDays`. This costs a few lines beside the existing gates.
2. **(Priority 2) Figure lint.** A stale "today" statement was the Medium in three recent rounds (I29 M1, I34 M1, I38 M1); this round found none, so the manual sync currently holds. A small `check_draft_figures` step could read the draft's quoted figures from a generated figures manifest (bars, exchange rates, separability medians, band ranges, row counts) and diff them against `scores.json` at publish time. It would not change any score, only keep the draft honest.
3. **(Priority 3) Bug Hunt noise reading.** S1T treats Bug Hunt's mean of N runs as n = 105 bugs. For rows with N of 3 to 7 runs this overstates the spread if bug outcomes are independent across runs, and understates it if bugs cluster in two repositories. As with AI Coding Daily (E263), publish the √N-scaled reading beside the plug-in one as a sensitivity. It is labelled and changes no score or label.
4. **(Priority 4) DeepSeek V4.1 Flash 1017 (max) Bug Hunt tie.** The harness choice (DeepSeek's own agent, 42.7, against Claude Code, 39.1) is an editor reason "for owner review". Publish the quality and value delta if the other harness were chosen (about 0.34 quality points at a 10% weight, 0.4 at 12%) beside the leaf, so the owner can see it is below the 4.0 noise margin without opening the record. No change to the rule.

## 3. Questions for the owner

1. If Medium 1 is accepted: which maximum capture age for non-AA evidence (7 days to match the cohort capture and the search log, or 30 days to match the report window)? The answer changes how often the Vals, LiveBench, AI Coding Daily, Bug Hunt and Cognition captures must be refreshed before each release.

## 4. Verdict

VERDICT: HAS FEEDBACK
