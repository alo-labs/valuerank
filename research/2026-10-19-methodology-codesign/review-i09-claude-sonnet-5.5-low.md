# Internal review I9 — Claude Sonnet 5.5, effort low, on draft r68

(Saved from the subagent's report; the reviewer read all 862 folded lines.)

## 0. Read check
- First line: "# ValueRank methodology — draft r68"
- Last 12 words of the last line: "covers two-thirds of ranked rows jointly with the admitted components (E95, E101)."
- I read all 862 lines in three chunks. I read ledger-brief.md first, then grepped ledger.md for burn, lifetime, staleness, E201 and window-straddling. I did not read the I7/I8 sections in full.

Checks I did:
- I recomputed the following and found them correct:
  - the Omniscience vectors (z = 98.5, 99, 75, 82 and 66 for the retired formula)
  - the Bug Hunt vector 52/105 → 49.52
  - the exchange-rate formula
  - the ladder positions (zero-based 8, 17, 25 for n = 35; ⌈n/2⌉ for odd and even n)
  - both admission fixtures
  - the Clopper–Pearson endpoints (δ/2)^(1/n)
  - the 70%-coverage kernel fixture (91.5% uniform, 86.8% arcsine by simulation; the draft says 86.7%)
  - the quality-weight sums (100%)
  - the basket-scope retained weight (86.7%)
  - the independent-weight share (20%)
- I did not web-check the 2026-dated AA, tbench.ai and Bug Hunt pages the draft cites. They post-date my knowledge and I did not fetch them.
- The only external fact I leaned on is the AA Omniscience Index definition (correct minus incorrect over total, abstentions count zero, range −100 to 100; artificialanalysis.ai/evaluations/omniscience, from memory). It matches the draft.
- scipy's exact-method interval takes `confidence_level` (scipy.stats.binomtest(...).proportion_ci), as E150 says.

## 1. Findings by severity

**Critical**

None.

**High**

None.

**Medium**

M1. "Complete cost evidence" is used in two incompatible senses (Capture status; E37; E170 outcome 4; anchor eligibility).
- E37 defines CompleteCostEvidence by AA's missing- or declined-task marker alone.
- The Capture status says the seven Index evaluations are "complete for 35, because Claude Fable 5.1's AA costs do not reconcile". By E37, Fable has exact cost and no marker, so it is complete.
- Admission uses P(S) of "complete cost evidence" and states a 33-row panel. That figure only works if Fable is excluded from completeness. The arithmetic: 37 rows, minus 3 without a Coding Agent Index cost, minus Fable, gives 33.
- Anchor eligibility is written as "complete cost evidence ... and an E170 outcome of 1 or 2". That wording treats the gate as a separate filter, so Fable would be complete but gated, giving panel 34 and anchors 33.
- Today both counts happen to clear ⌈2N/3⌉ = 25. The reference-panel hash, K_ie matrix, admission object and anchor references still differ between the two readings.
- Fix: state whether an outcome-(4) row's components are "published, basis unverified" or "unresolved". State whether they enter K_ie and P_K. Either say K_ie is gate-aware (and amend E37's definition), or keep K_ie marker-only and give the admission panel as 34 with 33 anchor references.

M2. The token-mix test compares with an undefined "AA's" mix (Plan cost: "the measurement's category mix is compared with AA's: L1 distance > 0.30").
- The only AA category mix published is Index-wide. It is dominated by Omniscience (6,000 questions) and HLE (2,158), which are excluded from W by O15. It also excludes the Coding Agent Index.
- E124 and E130 state that per-evaluation category splits are not public and that W's demand is the set-identified region D_iW.
- Two implementations will therefore flag different routes "mix-unmatched": one using Index totals, one using W's region.
- Fix: define the distance as L1 between the measured mix and the nearest point of D_iW's category-share projection (zero inside the region), using the published per-component output tokens, cost identities and Index totals.
- If D_iW is not constructible, the flag should read "mix unidentified" and never default to Index-wide shares.

M3. The frozen bar has no staleness trigger, though anchors do (the clip gate).
- E156 and the ledger say the bar is re-selected "only at a versioned re-freeze, the same lifecycle as the anchors". The draft never says when a re-freeze is triggered, and the policy object's `lifetime` field has no value.
- Anchors have a held-release gate. The bar has only a vacuity label ("comparison vacuous" below two qualifiers).
- Bar 3 asks "cheapest above a quality level". As newer, stronger models enter, a bar frozen at 56.7 will be reached by most of the cohort. The answer then degenerates to "cheapest row overall", with no flag.
- I found no staleness trigger in the ledger greps; this is a new argument, not a repeat.
- Fix: publish each release the current-population percentile of the frozen Q̄ and the share of rows reaching it. Raise an informational flag (not a hold, not a score change) when Q̄ falls below the current lower quartile or above the current upper quartile. Register the lifetime as "until the next anchor re-freeze or methodology version, whichever is first", and have the flag name the re-freeze as the remedy.

M4. The Plan basis rests on one untested donor-model assumption, and the one public calibration pair is not used.
- Transfers (O4/O7 and the 2026-10-18 authorisation) apply Opus 5.5's multiples to the other Claude rows. By the plan-cost identity C/M = F/λ, this implies quota burn proportional to API price across models.
- Today these rows include Haiku 5.5 and Sonnet 5.5 at five efforts each.
- Fable 5.1 (SemiAnalysis, 12.4–12.7x on the same plans, per AGENTS.md) is now ranked (O31). This is the only public pair showing how far a Claude donor multiple can miss.
- The earlier O4/O7 challenge was rejected when Fable "is not in the ranked roster" (ledger line 281), so this is a new argument.
- The draft only offers transfers on/off and an unquantified "directional bias bound".
- Fix (a diagnostic, not a score change): a transfer-calibration sensitivity that rescoring every transfer-dependent Claude row with the Fable 5.1 per-plan multiple. Publish rank changes and label it "donor-error illustration from the only measured pair". It enters no Θ and no scenario stream, consistent with O19.

**Low**

L1. E201 is cited for three unrelated rules without sub-labels: window-straddling reports (Report set), label reach and unevaluated siblings (bar). The header says a record holding several rules labels them. Add sub-labels (E201a/b/c) or split the IDs.

L2. Under O32 only reports dated in the last 30 days count, and report partitions are rebuilt each release. The E151 partition-stage logic for reports (an older member's stage, a "demoted report leaves", expiry under 90 days plus grace) can then only be reached through scoped change detection. The fixtures describing a demoted report leaving a pair are partly unreachable. Say so, so implementers don't build dead branches.

L3. "Ranked configuration" means a cohort row at line 104 but "has a rank" at line 102 (Muse Wonder Full has none). The bar-population sentence at line 608 says "non-provisional ranked configurations". Use "cohort row" there; the counts paragraph already fixes the meaning.

## 2. Methodology design recommendations
1. (From M3) Add the bar staleness indicator and the lifetime rule. It is cheap, uses only published values and touches no score.
2. (From M2) Replace the Index-wide mix comparison with a distance to D_iW's category-share region, using the quantities E124 already registers.
3. (From M1) Add a single "cost-evidence status" enum: complete / complete, basis unverified / confirmed incomplete / missing. Define K_ie, P_K and anchor eligibility over it. This removes the count ambiguity at the source.
4. (From M4) Add the Fable-calibration transfer sensitivity. Optionally extend it with a second published bracket, "burn proportional to API price" against "burn equal per token", labelled analyst sensitivity under O19.

## 3. Questions for the owner
1. Is a donor-error illustration from the Opus 5.5 / Fable 5.1 pair acceptable as a published diagnostic, given the O4/O7 challenge was closed when Fable was unranked? It would change M4 from "diagnostic" to "do nothing" if not.
2. Should a bar-staleness flag be informational only, as recommended, or should it hold a release like the clip gate? This is an editor-level default, so only the owner's preference would change R1.

## 4. Verdict
VERDICT: HAS FEEDBACK
