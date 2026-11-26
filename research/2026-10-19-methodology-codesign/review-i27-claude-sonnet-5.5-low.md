# Internal review I27 — Claude Sonnet 5.5 (effort low) on draft r86

## 0. Read check
First line: `# ValueRank methodology — draft r86`. Last 12 words of the last line: "covers two-thirds of cohort rows jointly with the admitted components (E95, E101)."
(All 1067 lines read, plus the ledger brief, the amended AGENTS.md, ledger sections I22–I26 and O39–O42, and `valuerank/value_v3.py` (rank_separability, rank_bands); README.md and data/scores.json read only to test consequences. No web search; source facts (SemiAnalysis multiples, AA task counts, Cognition and Bug Hunt data) are unverified by the reviewer.)

## 1. Findings by severity

**Critical**
None.

**High**

H1. A listed frontier family is not an "omitted competitor" in bar and frontier claims (E38 scope, E190, O38/O41, AGENTS.md "must not silently exclude a frontier model"). MiMo-V2.6-Flash is on the subset workload W_S at $60.37 API with renormalised quality 53.9 over 90% of the weight, so its full-composite quality is at least 48.5 and at most 58.5 whatever its Bug Hunt leaf; ranked W_S comparators cost e.g. $318 (GPT-6.1 Sol (medium)) and $88.6 (GPT-6 Luna (max)). At the lower bar (47.4) it qualifies in every state and is cheaper than the displayed W_S cheapest; at the headline bar (55.3) it can qualify with Bug Hunt ≈ 68+ at about a fifth of Sol (medium)'s W_S cost. W_S "confirmed" and "cheapest" results can thus be contradicted by a required frontier family the claim contract never names. Fix: include listed O38 families with a cost on the output's workload as omitted competitors, tested by structural bounds (missing leaf at 100 / 0, cost lower bound); print "extends to selected cohort: not established" naming them; let them block labels (as E222 rows), never earn one.

H2. **Owner decision challenge (O34), new empirical argument**: "cheapest above a bar" mostly returns the bar's own setter. The setter has the minimum quality among qualifiers and, with cost rising with quality, is usually the cheapest qualifier — the pathology E192 meant to remove. In the README displayed-record lines the cheapest row equals the setter in 5 of 6 results (API 47.4 GPT-6 Luna (max); API 59.6 GPT-6.1 Sol (high); Plan 47.4 GPT-6 Luna (max); Plan 55.3 Claude Sonnet 5.5 (high); Plan 59.6 GPT-6.1 Sol (high); only API 55.3 differs), and interval claims list it as "possibly". The answers hinge on a +0.01 move of the level, while the draft's own noise figure says quality differences below about 4.4 points cannot be resolved. Fix (compatible with O34): companion outputs the setter cannot drive — cheapest with displayed margin to H at least the quality noise threshold, or cheapest at H with the setter excluded — or the cost lower envelope at a grid of levels.

**Medium**

M1. Stale independent-weight statements after O37: lines 668/672 ("leave-AA-out today: 20%"), line 1036 ("≈20% independent weight") and line 940 ("Terminal-Bench: independently executed quality leaf, two further AA executions"); E62 defines Q_ind = (z_BugHunt + z_TB)/2 on rows with both independently executed leaves — that panel is now empty or one leaf. Restate the independent weight as 10%, redefine E62 on Bug Hunt alone (plus tbench.ai gap fills when present), mark it undefined otherwise, correct line 940.

M2. Separability and band definitions are ambiguous or inexact: "1.96 × the root sum of their value SDs" reads as a root of a sum of SDs while the code uses √(SD_i² + SD_j² − 2ρ·SD_i·SD_j); the test is per adjacent pair with the median only a summary; the value SD is analytic from quality leaves only (cost excluded), not a simulated S1T SD. "Band of positions the row cannot be told apart from" misdescribes a partition anchored on the band's first row. Write the formula with ρ, state these choices, and describe bands as "every row is inseparable from the band's top row; adjacent rows in different bands may also be inseparable" (or use per-row windows).

M3. "Conservative" is asserted one-sidedly: omitted sources (run-to-run and harness variance, AA's single cost run, and on Plan the transferred multiples — a 4.6× cost error is about 3.8 Plan value points at 1.73 points per doubling) push the other way. Without estimating the Fable/Opus gap (O35), say "the independence assumption overstates the threshold; omitted sources work the other way; net direction not established", and on Plan print the count of rows on assumed routes with "excludes transfer error".

**Low**

L1. "A 95% interval is never assumed normal … AA fitted-rating intervals keep their source interpretations" now conflicts with S1T's normal reading of GDPval-AA's interval; add the O39 exception.

L2. E204's check covers only points left of the first vertex; a plotted point strictly above-left of a mid-line segment is not stopped. Generalise or state that the near rule covers it.

L3. E216's 45-day model-page limit is dead text given E211 plus E217 (14 days max); delete or label it a backstop.

## 2. Methodology design recommendations (priority order)
1. Implement H1 and H2.
2. Split the normative text into an active core and a dormant appendix (under O36 and E61/E67 large parts of E77, E105–E121, E132–E135 and the E40–E108 solvers are vacuous); consider "rounding-stable" for "confirmed".
3. Publish basket runs per fee period = M·F_gross / C_W per Plan row (GPT-6 Astra on Plus $20 at 8.1× ≈ 0.03 a month; Claude Sonnet 5.5 (max) on Pro $20 at 58.9× ≈ 0.13).
4. A "fill-sensitive" annotation beside any label or displayed-record result that changes under E234's lowered-fill test.

## 3. Questions for the owner
1. Should a listed O38 frontier family act as a label-denying competitor, named in bar and frontier claims (H1)?
2. Would you accept a companion "setter-excluded or margin-above-bar" cheapest result beside the O34 bar (H2)?

VERDICT: HAS FEEDBACK
