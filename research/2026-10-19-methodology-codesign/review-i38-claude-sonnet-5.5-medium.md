# Internal review I38 — Claude Sonnet 5.5 (effort medium) on draft r97

## 0. Read check

- First line of the draft: "# ValueRank methodology — draft r97".
- Last line of the draft (line 939): "...medium efforts), so neither ranking covers the cohort: the max-effort ranking ranks 9 of the 29 cohort configurations, ... Instruction following has no weight while Surge's Complex Constraints is excluded (O53). On the Plan basis the MiMo multiples are provider-derived quota ceilings, not measurements (O46)."
- Last 12 words of the last paragraph: "Plan basis the MiMo multiples are provider-derived quota ceilings, not measurements (O46)."
- Also read: `reviewer-prompt.md`; the whole folded draft (lines 1-939, in chunks); `ledger-brief.md`; `ledger.md` from "## Internal review I28" (line 1170) to the end (I28-I37, O45-O58, E240-E263); `AGENTS.md`.
- Checked against repository data: `data/aa_frontier_capture.json` (18 vertices, 11 near points, the 189 plotted points, the near-gap rule recomputed over all 189), `data/scores.json` (both rankings: bars, ladders, anchors and exchange rates, cost influence and variance allocations, separability medians, grids, bands, tolerances, qualityMargin, the O58 listed-beyond-anchors list, basket readiness and cost shares, gap-fill and cross-source diagnostics), `data/bug_hunt.json`, `data/swe_tracks.json` task counts, `data/plan_cost_routes.json` (O46 ceilings), `valuerank/emit_docs.py` (coding-share computation). The artefact paths the draft cites (open-web discovery file, before-O47 frozen anchors, `add_track_searches.py`, `build_swe_tracks.py`, `value_v3.check_open_web`) exist.
- Arithmetic re-done and found correct: weight sums (60 / 14 and 11 leaves), ladder positions and fixtures, reach counts (7/5/3 of 9; 12/8/5 of 15), exchange rates (3.04 / 2.44 / 2.83 / 1.89 from the stated padded anchors), the E242 tolerances (2.35, 5.28), the noise margins (4.0, 5.9) and their bar sums, ⌈2N/3⌉, the 255 and 127 feasible alternatives, the plan-row counts (27, 50) and transfer counts (14, 48), the band ranges, the age-stage dates, the Omniscience and Bug Hunt vectors, and the fixture with 91.5% uniform draws.

## 1. Findings by severity

**Critical**

None.

**High**

None.

**Medium**

M1. The Fallback paragraph (E214) states a fact about AA's chart that is false for part of the cohort. The draft says "AA plots every Claude configuration only 'with fallback', so the qualifier names AA's serving setting rather than a second configuration", and the leaf-evidence paragraph repeats the premise ("A Claude record without a fallback qualifier matches AA's 'with fallback' configuration"). The 2026-10-23 capture (`data/aa_frontier_capture.json`) plots Claude Haiku 5.5 at all five efforts with no fallback qualifier (medium, high and xhigh are rendered-frontier points; low and max are near points). Only Claude Opus 5.5, Claude Sonnet 5.5 and Claude Fable 5.1 carry "with fallback". That is five of the 29 cohort rows. Why it matters: E214 is a normative matching rule, and a rule whose stated premise is false gives an implementer or auditor two readings. One is that Haiku rows must be matched to a nonexistent "with fallback" twin. The other is that the premise is simply wrong and the operative rule (match by model and effort; stop the build on a with/without twin) is all that binds. The operative rule still works today, because no model and effort is plotted both ways. This is the same stated-fact class as I30 M1 and I34 M1, which earlier rounds counted as Medium. Change: restate the premise as observed. For example: "On 2026-10-23 AA plots Claude Opus 5.5, Sonnet 5.5 and Fable 5.1 only 'with fallback' and Claude Haiku 5.5 without a qualifier; no model and effort is plotted both ways. A fallback-silent third-party record matches by model and effort, and the build fails if AA ever plots a twin." Also change the leaf-evidence sentence to "matches AA's configuration of the same model and effort, with or without the 'with fallback' qualifier". Have the build print the per-family fallback state so the sentence stays checkable.

**Low**

L1. The draft reports the cost-influence flags that are clear today but says nothing about the group-drift flag (E114), and one fires. In the AI Coding Daily ranking the knowledge group's spread share is 4.6% against a nominal 10% (below 0.5 × W_g), so the group is flagged. Max-effort has no flag but marks AA-LCR non-discriminating (SD under 3 points). The release flags are informational, so no rule is wrong. A reader of the methodology alone cannot tell that one group flag is live. Add one sentence of today's drift and non-discriminating results beside the E114 paragraph.

L2. A subset-workload stratum with exactly two rows (DeepSeek V4.1 Flash 1017 and MiMo-V2.6-Pro in the max-effort ranking) is "defined" under E180, because the rule is undefined only below two rows. It prints a cost variance allocation of about 5.4 and a quality allocation of about -4.4 (`costInfluence.api.subsetStrata`). These are formally correct but uninformative. Consider a minimum of three rows for printing a variance allocation, and "insufficient panel" below that. The SD ratio can stay at two.

L3. The separability medians are quoted at two precisions: "4.45" in Output 1 and "4.4" in the n = 60 sentence for the same 4.4467. Pick one convention (two decimals).

L4. Output 1 is a single bullet of about 35 lines, carrying rank separability, the grid, tolerance, bands, today's band lists, both exchange-rate quantities, the influence panel, dispersion convention, variance allocation, nominal-weight disclosure and basket labels. Every item is cross-checked and consistent with the data. The structure makes review and implementation harder than it needs to be. Split Output 1 into labelled sub-bullets (ranking; separability and bands; cost-weight disclosures; basket label) without changing any text.

L5. The Terminal-Bench closed agent list includes Grok Build and Muse Code, which were observed for models that left the cohort at O51. It is harmless, because the list is a closed registry, but "observed for cohort rows" is no longer literally true. Say "observed on the captured leaderboard".

## 2. Methodology design recommendations

1. (Priority 1, goes with M1.) Make every statement about AA's plotted names a build-generated line (fallback state per family, effort-less families such as MiMo-V2.6-Pro, MiMo-V2.6-Flash and MiniMax-M3.1-Flash) rather than prose. The fallback sentence went stale when Haiku 5.5 entered the cohort. The effort-less list (O54) is the next place a similar sentence could go stale.
2. (Priority 2.) Add a one-line "flags live today" summary to the active-rules manifest text in the methodology: drift flags, non-discriminating leaves, cost or quality not discriminating, partial and subset flags. Today these are spread across sections, and the one live drift flag (AICD knowledge group) is absent from the prose.
3. (Priority 3.) For the two-row subset stratum, print the SD ratio and the allocation only above a minimum panel size (see L2).

No change to any score, weight, anchor or owner decision is recommended.

## 3. Questions for the owner

None.

## 4. Verdict

VERDICT: HAS FEEDBACK
