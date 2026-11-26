# Internal review I31 — Claude Sonnet 5.5 (effort low) on draft r90

## 0. Read check

- First line of the draft: "# ValueRank methodology — draft r90".
- Last line of the draft (line 911 of the folded copy): "Surge's Complex Constraints is excluded (O53). On the Plan basis the MiMo multiples are provider-derived quota ceilings, not measurements (O46)."
- Last 12 words of the last paragraph: "Plan basis the MiMo multiples are provider-derived quota ceilings, not measurements (O46)."
- Also read: `reviewer-prompt.md` in full; the whole folded draft (911 lines, in chunks); `ledger-brief.md`; `ledger.md` from "## Internal review I28" (line 1170) to the end (line 1231), including the O45–O56 and E247–E258 records and how I29 and I30 were handled; `AGENTS.md`.
- Checked against repository data (read-only):
  - `data/scores.json` (`v3` and `v3Tracks.aicd`): exchange rates, anchor ratios, bar ladders and bar currency, separability medians, counts and correlation grids, noise bands, value-variance allocations, family-primary diagnostic, gap-fill sensitivity, cheapest rows, margin companions, admission counts.
  - `data/aa_reconciliation_inventory.json`: the 18 frontier rows and 11 near rows, including the near points of the frontier families.
- Result of the numerical check: every figure I recomputed matches the draft.
  - Cohort and plan-row counts: 18 + 11 = 29; 27 and 50 plan rows; 14 of 27 and 48 of 50 rows on a transfer or the O46 ceiling.
  - Separability: 3.01 / 1 of 8, 4.45 / 1 of 14, Plan 3.01 / 2 of 11 and 4.54 / 1 of 19, the 15 and 30 same-configuration pairs, grid 1/1/2 and 2/2/2, 1/1/1 and 1/1/1.
  - E242 tolerances: 2^(3.0129/2.44) = 2.35 and 2^(4.54/1.89) = 5.28.
  - Exchange rates from the anchor ratios: 3.04, 2.44, 2.83 and 1.89 value points; offsets of 4.06 and 3.77 quality points.
  - Ladder positions: floor((n−1)k/4) for n = 9 and n = 15.
  - Bar currency: 5/7/3 of 9 and 8/12/5 of 15.
  - Noise margins of 4.0 and 5.9; bars plus margin of 64.7 / 53.8 / 66.1 and 55.1 / 43.9.
  - Family-primary diagnostic: 7 rows with ladder 60.7 / 49.8 / 61.1; the AI Coding Daily changes (API 8 rows move, largest 2; Plan 7 rows, largest 3).
  - Admission: 255 and 127 feasible subsets; thresholds 6 and 10.
  - Weights: 60% software engineering in both rankings; independent-weight shares 28% and 22%; basket-scope retention 86.7%.
  - Evidence clock dates (2026-11-05, 2027-01-05, 2027-02-04).
  - MiMo ceilings: the Pro/Flash ratio of 1.0286 equals $1.44/$1.40.

## 1. Findings by severity

**Critical**

None.

**High**

None.

**Medium**

None.

**Low**

1. **The value-variance allocation can be negative, and the draft does not say how the headline prints it (Outputs, E189/E196).** The draft defines the allocation as Cov(0.25·S_C, V)/Var(V) and Cov(0.75·Q, V)/Var(V), "which sum to 1". It illustrates the E196 headline wording only for the max-effort ranking ("65% of API and 2% of Plan value variance"). The generated data for the AI Coding Daily ranking gives cost −0.90 (API) and −0.26 (Plan), with quality 1.90 and 1.26. That is mathematically valid. It happens because expensive configurations score higher on quality, so cost spread offsets quality spread. But E196 says the headline prints this number "beside" the 25% nominal weight, so the second ranking would read "25% cost score (nominal weight; −90% of API value variance)". Two implementers could clip to 0, print "n/a" or print the raw negative. Change: add one sentence to E189/E196 saying that an allocation outside 0–100% is printed as computed, with a note that the cost score's spread offsets quality's spread. Also give the AI Coding Daily figures next to the max-effort illustration. This is presentation only, and no score or rank changes.

2. **The Plan noise-band extension rule (E248) can contradict the band invariant in its general form (Outputs, O42/E248).** The draft says "every row is inseparable from its band's first row". It also says a band that starts at one of a configuration's plan rows "extends over its other plan rows, because a row between them cannot be told apart from either". The justification holds only when the configuration's plan rows lie within the separability threshold of each other. Today they do (plan rows of one configuration differ by about 2 value points against thresholds of 3.0–4.5). If a configuration's plan rows ever spanned more than the threshold, an intermediate row of another configuration would be separable from the band's first row yet fall inside the extended band. The implementation text in `scores.json` is sequential ("a row of the band's first configuration on another plan stays in the band"), which differs slightly from the draft's "extends over" wording. Change: state the rule once, as a single procedure. For example: walk the rows in value order; a row joins the open band if it is inseparable from the band's first row or belongs to the band's first configuration; otherwise it opens a new band. Then say that the invariant is "inseparable from the first row, except same-configuration plan rows". No present output changes.

3. **The anchor figures in the re-freeze paragraph do not say which quantity they are (Cost, "Re-freeze at the moved cutoff").** The text gives "API $62.86 to $18,703.43 on 7 references", "Plan $5.84 to $7,115.53" and similar figures. The same section defines c_L as the minimum reference cost ÷ 2 and c_H as the maximum × 2. A reader would take these ranges as the references' own costs. Recomputing the exchange rate (17.33/ln(18703.43/62.86) = 3.04) shows they are the padded c_L and c_H, which are the frozen anchors. The same applies to the measured anchors of E249 ($57.24 to $812.57, ratio 14.2). Change: write "anchors c_L = … and c_H = …" and, if useful, give the cheapest and dearest reference cost beside them.

4. **E254's per-ranking reading of "two-thirds of the cohort" turns on AGENTS.md's literal wording, and the draft's own flag could be stronger (Cohort; Cost, Admission).** I30 L1 was adopted and the draft now says the owner can reverse the reading, so I do not repeat that finding. One point is new. AGENTS.md says each ranking has "its own anchors, bars and scenario run"; it does not say "its own basket admission". Admission is the only item in the draft's list of per-ranking objects (line 49) that the owner's text does not name. The reading decides whether the headline ranking is scored on eight or seven components, which moves all 9 rows' cost scores. The draft already discloses the effect (Coding Agent Index v2.0 priced for 7 of 9 rows but 7 of 29 cohort configurations). The remaining improvement is procedural: raise it as an explicit owner question at the next owner contact instead of leaving it as a standing "can reverse". Low, because it is disclosed and reversible, and because the draft's precedence rule (an editor record never overrides an owner decision) is respected.

## 2. Methodology design recommendations

Priority order. None is required by this round.

1. Apply the one-sentence fix in Low 1 to E189/E196 and print both rankings' allocations in the headline illustration. Cost-share reporting then stays informative where cost and quality are strongly negatively related, as in the AI Coding Daily ranking, whose cohort holds several efforts of the same families.
2. Rewrite E248 as the single sequential procedure in Low 2, so the band rule has one executable form and the invariant is stated once with its exception.
3. Label anchors as c_L and c_H wherever they are quoted (Low 3), and add the reference-cost minimum and maximum beside them so the ln 2 padding is visible to a reader.
4. Add a short "owner-reversible readings in force" list to the readiness table or the active-rules manifest, with E254 as its first entry. A future reviewer or owner then sees at once which readings are editor choices that change a headline result.

## 3. Questions for the owner

None. (Low 4 suggests putting the E254 reading to the owner, but its answer would not change any recommendation here, so I do not treat it as a blocking question.)

## 4. Verdict

This round raises no Critical, High or Medium finding (O56): four Low findings, all presentation or procedural wording. The numbers I recomputed from `data/scores.json` and the reconciliation inventory match the draft, and I found no rule that contradicts AGENTS.md or an owner decision.

VERDICT: NO FURTHER FEEDBACK
