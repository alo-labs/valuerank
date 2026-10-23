# Internal review I8 — Claude Sonnet 5.5, effort low, on draft r67

(Saved from the subagent's report; the reviewer read all 849 folded lines.)

## 0. Read check
First line: "# ValueRank methodology — draft r67"
Last 12 words of the last paragraph: "covers two-thirds of ranked rows jointly with the admitted components (E95, E101)." The folded copy's literal line 849 is only "(E95, E101).", so I quote the sentence it ends. I read all 849 lines in three chunks, and the ledger brief first. For decisions I suspected were already settled, I grepped the full ledger for E98, E201 and E203, and for a "v2" bar policy.

I did not run web searches. The draft cites sources dated 2026-10 that I can't check from here, so the findings below come from reading the draft's internal logic, not from outside facts.

## 1. Findings by severity

**Critical**
None.

**High**
None.

**Medium**

M1. The cohort rule leaves one class of point unclassified, which can silently drop a model.
- Passage: "Cohort rule (executable)": "A point cheaper than every rendered-frontier point has no F(c) and is not near-frontier; at that cost it would be on the frontier itself."
- The rationale holds only if AA's rendered line always starts at the cheapest plotted point. The draft never checks that, and frontier membership is "the rendered line as observed".
- If AA's line starts at a dearer point (filtered series, an open-weights or other display rule, or a cheap point above a threshold), the cheaper model is neither frontier nor near. It is dropped with no dated roster decision. AGENTS.md says a manually maintained rule must not silently exclude a frontier model.
- The E195 build check covers only points that sit on the path. It does not cover points left of the path.
- Fix:
  - Add a build step that lists every plotted point cheaper than the first path vertex as "left of rendered frontier".
  - Require a dated, reasoned roster decision for each such point, and fail the build if one has no decision.
  - The same step should confirm that the first vertex is the cheapest plotted point in the captured series.

M2. The exact-match key for retention (DeepSWE plus Bug Hunt) is not defined, so two implementers can roster different rows.
- Passages: the "Retained configurations" and "Roster check" bullets, and the Bug Hunt leaf, "exact model, effort and harness".
- Retention decides which rows exist, so it moves anchors, bars and ranks. The only matching rule stated is that a scoreboard name "may add only a version number".
- Left open:
  - how effort labels map between AA and the Bug Hunt scoreboard (xhigh versus max, "default" effort);
  - whether harness is part of the key, given that Bug Hunt runs vendor CLIs and DeepSWE runs AA's harness;
  - how fallback and snapshot identity are matched;
  - what happens when a Bug Hunt model appears under two harnesses.
- Fix: add a versioned match table to the evidence bundle with these fields:
  - key = (AA model ID, effort token, Bug Hunt model string, Bug Hunt effort string, harness ID);
  - an explicit effort-synonym table;
  - the harness policy for multiple harnesses;
  - a fixture for each ambiguous case.

M3. The bar ladder, anchors and influence statistics count rows, not families, so a family's weight depends on how many efforts have evidence.
- Passages: the O33 and O34 text, and the bar population ("35 configurations").
- Three families (GPT-6.1 Sol, Haiku 5.5, Sonnet 5.5) contribute five efforts each, which is 15 of 35 bar-population rows. The ladder positions are floor((n−1)k/4) over rows.
- A family with many evidenced efforts therefore moves the three bars, the anchor extremes (O33 already moved the low anchors from $66.43 to $35.76 for API and from $2.48 to $0.61 for Plan), and the cohort SDs.
- Measuring more efforts of a model can change every other model's cheapest-above-bar answer. E199 tests only the frontier-families subset, which changes both the rows and the family weighting at once.
- Owner decision challenge to O33 and O34: this is a consequence of those decisions, not a challenge to the O33 rule itself. Keep every effort as a ranked row, but add a diagnostic that recomputes the ladder, the anchors and the influence statistics with one row per family (the primary row), beside E199. The effect of effort multiplicity is then separable from the effect of narrowing the cohort.

M4. The cheapest-above-bar output is close to vacuous for confirmed labels, and the fallback is not a claim.
- Passages: "Label reach (E201)" (5 confirmed against 21 possible qualifiers), and "Confirmed cheapest", which needs every possibly qualifying competitor to be strictly dearer in every θ.
- Rows with low coverage count as possible competitors. So the unique confirmed label is almost unattainable, and the scenario label also fails whenever missing-leaf draws let a cheaper row qualify.
- The displayed-record cheapest (E203) is explicitly "not a claim". The headline question is then answered by no claim-grade output. This is disclosed, but it is a gap against the objective, not just a limitation.
- Fix: see Recommendation R2 below (a coverage-restricted universe, labelled as such).

**Low**

L1. Stale policy version.
- Passage: E50 parenthesis, "the v2 frozen level is a constant".
- The bar policy is version 3 and E192 replaced "v1". No v2 appears in the ledger. Change the reference to "the v3 frozen level" or delete it.

L2. Concordance reading of O11's "±20%" is stricter than the plain reading (E98).
- Passage: "100 and 120 pass, 80 and 120 fail".
- Two reports at ±20% of a centre of 100 fail the draft's test. A plain reading would call them concordant.
- E98 was adopted in the ledger as "O11's ±20% kept", so I am not re-raising it as a defect. The new point is the concrete fixture: 80 and 120 are each exactly ±20% of 100 yet fail. Put this to the owner (Question Q1). It affects only report-based routes.

L3. The set-identified scoring convention penalises better evidence.
- Passage: E74. A set-identified M_W enters at its lower bound L.
- An unidentified route scores at its observed multiple. For example, a set-identified [10, 30] scores at 10, while an unidentified route with an observed 25 scores better, despite weaker evidence.
- Comparator key 1 prefers identified routes only within a single model's route choice, not across models. Nothing is identified today, so there is no current effect.
- Fix: before the first identified route appears, publish the upper-bound and midpoint rank sensitivity beside the L score, and print a flag whenever an identified row scores below an unidentified one because of the L convention.

L4. The draft is hard for outside readers to use.
- The text interleaves normative definitions with 200 or more E-tags, revision history and dated fixtures. That raises the risk that a reader (or a second implementation) misses a governing rule.
- Fix: publish a short normative core, a rule-ID index (one line per rule with its governing section), and move dated "today" numbers to a generated appendix.

## 2. Methodology design recommendations (prioritised)

R1. Add the left-of-frontier classification and the Bug Hunt match table from M1 and M2 to the build, with fixtures. Both are cheap and make cohort membership reproducible.

R2. Add a coverage-restricted universe for the bar outputs.
- Publish the confirmed and scenario-supported cheapest on the rows with full quality coverage, labelled "among full-coverage rows".
- State that rows outside the universe are omitted competitors (the E38 listing already exists).
- This gives the owner's published-record target (O25) a usable claim-grade output without changing any row's evidence.

R3. Add the one-row-per-family sensitivity from M3 (bar ladder, anchors, exchange rate, influence).

R4. Before the first identified Plan route is published, add the L3 upper-bound and midpoint sensitivity and its flag.

R5. Split the document into a normative core and an appendix (L4).

## 3. Questions for the owner

Q1. Should O11's "±20%" mean each report within 20% of the others (80 and 120 around 100 concordant), or the current max ≤ 1.2 × min? The answer changes which report pairs admit a Plan route.

Q2. If AA's rendered line ever starts above the cheapest plotted point, should that cheaper model be treated as frontier (included) or excluded by a dated roster decision? This decides the M1 behaviour.

## 4. Verdict
VERDICT: HAS FEEDBACK
