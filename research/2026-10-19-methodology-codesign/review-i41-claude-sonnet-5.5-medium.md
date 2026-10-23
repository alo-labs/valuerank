# Internal review I41 — Claude Sonnet 5.5 (effort medium) on draft r100

## 0. Read check

- First line of the draft: "# ValueRank methodology — draft r100"
- Last line of the draft (the folded copy's final line, 949): "configuration (O54, E252). Instruction following has no weight while Surge's Complex Constraints is excluded (O53). On the Plan basis the MiMo multiples are provider-derived quota ceilings, not measurements (O46)."
- Last 12 words of the last paragraph: "Plan basis the MiMo multiples are provider-derived quota ceilings, not measurements (O46)."
- Also read in full: `reviewer-prompt.md`, `ledger-brief.md`, `ledger.md` from "## Internal review I28" (line 1170) to the end (through I40 and O59/O60), the whole folded draft (949 lines, in chunks), the root `AGENTS.md`, and the previous review `review-i40-claude-sonnet-5.5-medium.md` (to avoid repeating its points).
- Checked against repository data and code, not just prose:
  - `data/scores.json`: bar ladders, bar currency, exchange rates, cost-influence and value-variance allocations, rank separability (medians, counts, correlation grids, bands, E242 tolerances), plan rows and the selected Sol and Astra multiples, MiMo ceilings, displayed-record and noise-margin cheapest rows, identification yield, Terminal-Bench and FrontierCode cross-source panels, drift flags, source shares, `aaPlottedNames`, the frontier selection, `releaseHold`, the cohort object.
  - `data/swe_tracks.json` (saturation statements, harness and effort records), `valuerank/value_v3.py` (`rank_bands`) and `valuerank/build_scores.py` (cohort fields).
  - That the research artifacts the draft cites exist (`add_track_searches.py`, `build_swe_tracks.py`, `open-web-discovery-2026-10-23.json`, `v3-frozen-2026-10-21-before-o47.json`, the SWE candidates report, the MiMo research folder).
- Recomputed by hand and found correct:
  - exchange rates 3.04 / 4.06, 2.44 / 3.25, 2.83 / 3.77, 1.89 / 2.52 from the stated anchors;
  - quartile positions floor((n − 1)k/4) for n = 4, 9, 15, 32 and the ⌈n/2⌉ headline position;
  - the noise margins 4.0 and 5.9 (1.96 × √2 × median SD) and their relation to the 3.01 and 4.45 thresholds;
  - the bar-plus-margin levels 64.7 / 53.8 / 66.1 and 55.1 / 43.9 / 63.0;
  - the E242 tolerances 2.35 and 5.28; the 255 and 127 feasible-alternative counts; the two admission fixtures;
  - the 72 / 28 and 78 / 22 source shares; the 27 and 50 plan-row decompositions and the 14 and 48 transfer-resting rows;
  - the Omniscience vectors and the 98/1/1 and 99/1/0 examples; the Clopper–Pearson per-look δ = 0.05/16;
  - the Plan evidence-clock dates (age 30 on 2026-11-05, expiry 2027-01-05, demotion 2027-02-04) and the 31-date report window.

I found no Medium or higher finding. The r100 edits (separability count per pair, source-clock arithmetic, "at most one per family") are stated consistently with the build and with the ledger. Three Low observations follow.

## 1. Findings by severity

**Critical**

None.

**High**

None.

**Medium**

None.

I looked for the kinds of finding that made earlier rounds non-clean: a stale or wrong "today" figure, a rule that disagrees with the build, a contradiction with AGENTS.md or an owner decision, and a rule two faithful implementers would read differently. Every figure I checked against `scores.json` matched, including the ones I did not see checked in I40: the setter-is-cheapest counts (1 of 6 and 2 of 6, recomputed from the rows' displayed qualities), the Plan margin cheapest rows, the two Sol and Astra selected routes (10.772× on Pro 500, 14.485× on Pro 200), the MiMo ceilings (0.984 / 0.99 / 1.0944 / 1.1808), the Plan variance allocations (2% and −26%), the Vibe Code and LiveBench saturation statements (top values 92.4 and 96.3), the AA plotted-name state, and the unit-consistent anchor pair (the two rankings' Plan high anchor 3,715.87 is the same dearest-reference cost on the shared seven-evaluation workload). Nothing contradicts AGENTS.md. Two points I examined and found sound:

- The E248 band-extension sentence next to the "bands are built forward only" sentence could be read as letting a band started by one configuration reach back over a later, much lower plan row of that configuration after another band has begun. `rank_bands` shows the intended reading (a same-configuration row joins the current band only; after a new band starts, the later row is compared with that band's first row as usual), and the draft's closing clause ("so the invariant … holds for every row of another configuration") matches it. Nothing turns on it today.
- The bar-setter wart (the row whose displayed quality equals the frozen level can be a possible but never a confirmed qualifier, so a setter that is the cheapest row at its bar cannot be confirmed cheapest) is disclosed in E201b and answered by the O44 companion. It is owner policy (O34), not a new finding.

**Low**

- **L1. `scores.json` still carries two cohort fields whose meaning belongs to the withdrawn retention route.** I40 L4 was adopted and the cohort object now names the frontier capture as its source (`source`, `sourceUpdatedOn` 2026-10-23T05:27:39Z), and `deepsweStatus` reads "withdrawn by AA (O49), kept as raw data, not scored (E250)". But the same object still has `sourceN` = 61 and `exactBenchmarkOverlapN` = 17 (`build_scores.py` lines around 1410 and 1542, `len(rows)` and `len(overlap_primary_ids)`). Under O51 there is no retention route and no "exact benchmark overlap" concept (the draft says so in the Cohort section), and neither number appears in the draft. A reader of the JSON cannot tell what 61 and 17 count next to a cohort of 29 and 20 ranked. No score depends on them. Recommendation: rename them to say what they count (for example the all-catalog row count and the legacy overlap set), or drop them from the published cohort object, and add a one-line note in the Cohort section if they stay.
- **L2. The revision history occupies the first 42 lines of the document, before the objective.** Lines 7–48 are one italic paragraph of about 3,000 words. The objective, the claim scope and the cohort rules begin only at line 50. The history is useful to the ledger, but a first-time reader of `methodology.md` meets 40 review rounds before the question the page answers. Recommendation: keep one sentence ("r100; every change is recorded with its rationale in the ledger") at the top and move the per-revision list into a closing "Revision history" section, or leave it to the ledger. Wording and layout only.
- **L3. AGENTS.md and the draft give different reasons for leaving CursorBench out.** AGENTS.md lists Surge's Complex Constraints, CursorBench, Surge sudo L7, MirrorCode, SWE-bench-Live and SWE-PolyBench together as "not used (too few exact configurations)". The draft is accurate to the owner's decisions (O53, O54): CursorBench has 13 cohort configurations at exact effort and sudo L7 has 5, and both were excluded by the owner, while Complex Constraints (3 of 29), MirrorCode (3), SWE-bench-Live and SWE-PolyBench fall to coverage. The draft's text is the more precise of the two, so nothing in the draft needs changing. The inconsistency is in AGENTS.md's one-line summary, which is the owner's file. Recommendation: if the owner next edits AGENTS.md, add "or excluded by the owner (O54)" after "too few exact configurations".

## 2. Methodology design recommendations

In priority order, all optional and none needed for a clean round:

1. **Tidy the two JSON fields (L1)** with a build assertion that no field of the published cohort object is named for the withdrawn retention route.
2. **Move the revision history below the body (L2).** No rule changes.
3. **Carry forward, not for this round:**
   - A Bug Hunt √N sensitivity. The DeepSeek V4.1 Flash 1017 (max) tie of 7 runs each (DeepSeek's harness 42.7, Claude Code 39.1) moves its Bug Hunt z by about 3.4 points, about 0.34 quality points at weight 10 and 0.41 at weight 12. It is small, and the draft already flags the editor's choice for owner review.
   - Splitting Output 1 into sub-bullets (I38 L4, rejected for now).
   - When AA next adds Claude Opus 5.5 efforts to a SemiAnalysis article, check that Plan rows for Opus (high) and (medium) in the AI Coding Daily ranking move from transfers to their own figures only if the article names an effort (E246 binds an unsuffixed figure to max). That is an operational note for the weekly watch, not a draft change.

## 3. Questions for the owner

None.

## 4. Verdict

VERDICT: NO FURTHER FEEDBACK
