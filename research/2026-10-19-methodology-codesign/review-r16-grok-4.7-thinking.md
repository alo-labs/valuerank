I'll review the draft against its objective and check the public benchmark, cost, and plan-quota claims it depends on.
The draft cannot yet answer its objective: the rule that defines “recommended” is jointly unsatisfiable, and the check that is supposed to tie cost to the quality vector can price a different workload than the one being scored.

1. Findings by severity
Critical

The recommended contest is unsatisfiable once any rival lacks a certifiable edge. Certified(i; J) requires a certified win against every other member of J. A subset-cost row has no certifiable edges (E14). A Plan row without an identified M_W cannot be certified. O21 says a gate failure or unevaluable comparison never removes that rival from J, and the eligibility algorithm that is allowed to exclude it is not specified. On the current capture, 3 of 19 rows have no exact Coding Agent Index cost, and any not-yet-admitted component is not the problem — the 3 missing rows are, once that component is admitted under E26. One such row inside J means nobody can be “recommended,” including fully evidenced rows. That blocks the headline the objective asks for.

Change: In Normative definitions, define the headline contest before margins as:

𝐽
=
{
𝑖
:
full 
𝐶
𝑖
,
𝑊
 identified
∧
not provisional
∧
(
API
∨
𝑀
𝑊
 identified
)
}
J={i:full C
i,W
	​

 identified∧not provisional∧(API∨M
W
	​

 identified)}

Subset-cost and workload-unmatched rows stay in the table and are outside J. Add a release test: inserting a subset-cost row into the cohort does not change any certificate inside J.

The value-margin blocker can price a different slice than the quality it protects. Δ_ij scores renormalised quality on common support B_ij. The blocking alt-cost is a quality-weighted mixture over a release-level priced panel B that need not intersect B_ij. The 40% gate is on B, not on B∩B_ij, and it has no SWE gate. A pair can therefore be certified because both models are cheap on AutomationBench, GDP.pdf, or SciCode, while the quality edge that entered Δ_ij was DeepSWE and Terminal-Bench. That certifies “cheap on whatever happens to be priced,” not “cheap for the value.”

Change: For each pair, set B_ij^price = B∩B_ij. Require Σ w ≥ 0.40 and the E16 SWE gate on that intersection; otherwise the alt check is unidentified and the edge is not certified. Compute both C_alt and the alt quality term only on B_ij^price, with w' renormalised on that intersection. Keep one feasibility matrix, but store the pair-level intersection weight in the E27 record.

High

The basket-sum identity does not match the public Index, and the Coding Agent cost unit is ambiguous. Intelligence Index v4.3.2 has 10 evaluations, not 7: the draft’s seven plus HLE, CritPt, and AA-Omniscience. AA’s published “cost to run” uses token prices across the Index evaluations, excluding repeats. A sum of the seven cannot equal that total unless the three excluded evaluations cost nothing. Treating a failed <0.002% check as a release identity will either hold every release or force a false reconciliation. Separately, the Coding Agent Index publishes pooled per-task-attempt average API cost, not a documented total, and drops tasks with missing telemetry from the average rather than marking them missing. mean × 303 is then either one pass, three passes, or an average inflated over tasks that had no cost. DeepSWE, Terminal-Bench 4.0, and SWE-Atlas-QnA are each 3 attempts.
artificialanalysis
+3

Change: Stop calling the seven-sum “AA total.” Publish C_index = C_7 + C_HLE + C_Omniscience + C_CritPt and reconcile that to the chart. C_W uses only admitted components. For the Coding Agent Index, store the AA field name and a fixture: one configuration where published average × count of tasks included in that average is shown, with repeats either divided out or not, matching E9. Tasks excluded from AA’s average are missing components, not charged at the mean.

Plan capacity is not the quota Claude actually sells. Paid Claude plans have a rolling 5-hour session limit, starting at first use, plus a weekly limit, shared across Claude and Claude Code. Fable on Max is not a separate Opus-style pool: it may consume up to 50% of the same weekly limit and burns that limit faster; other models draw the same pool. The governing LP, as written, can be implemented as two aggregate buckets. That overstates capacity when use is bursty, and an Opus 5.5 multiple transferred to Fable (O4/O7) does not identify Fable’s M_W.
support.claude
+1

Owner decision challenge (O4/O7): a transfer across a different burn rate is not the same capacity object. Keep the transfer only if a measured burn coefficient, or a directional bound that includes it, is in the transport object. Otherwise Fable’s M_W stays unidentified.

Change: The only legal 5-hour constraint is sliding: for every start t in the fee period, consumption in (t, t+5h] ≤ B. Add a fixture where two bursts one hour apart, each 60% of the 5-hour cap, are infeasible, and two bursts six hours apart are feasible. Encode Fable as a 50% sub-cap on the weekly pool plus a model-specific burn a_wk. If that burn is not publicly measured, do not fill it from another Claude model.

Unrepriceable multiples contradict the normative price-list bind. Normative text binds M_W to the release price-list version. Prose says that if receipts cannot be repriced, the old valuation is kept and flagged, and the row can still be scored. C_plan = C_API / M then mixes two price lists. After a price move, Plan rank is not plan cost of workload W.

Change: Delete the prose exception. No reprice onto the release list means M_W is unidentified. The row stays scored only under O16, flagged, and outside J.

Owner decision challenge (O15): MMMU-Pro does not belong in an SDLC basket. AA lists it as an additional evaluation, 1,730 ten-option academic items, not part of Index v4.3.2. Admitting it at question-level multiplicity would swamp the basket (AutomationBench is 657 tasks; SciCode is 288 subproblems). ITBench-AA is a real DevOps eval (59 Kubernetes scenarios) but is also outside the Index. Terminal-Bench is already inside both the Index and the Coding Agent Index, and the quality leaf is a third execution, the tbench.ai board. SWE-Atlas-QnA is one-third of the Coding Agent Index and 0% of the quality vector. The basket as named prices work the quality score does not treat as value.
tbench
+2

Change: Do not reverse the basket-sum score if O15 stands, but do not admit MMMU-Pro. Retire any target component still “pending capture” after two monthly releases via a versioned workload migration. Disclose Terminal-Bench as two cost executions and a third quality execution, and do not let the extra execution into C_W unless it is the quality leaf’s own priced pass.

Medium

The Omniscience “AA weights them 1:1” sentence is false. In Index v4.3.2, AA contributes accuracy at 10% and non-hallucination at 5% — 2:1, the same ratio this draft uses. The separate Omniscience Index is a different estimand: correct answers rewarded, incorrect answers penalised, abstention neutral, range −100 to 100. The hallucination-rate definition and the test vector (c,p,i,a)=(60,0,10,30) → z=65 match AA. An implementer who “corrects” the leaf to 1:1 would be leaving AA’s Index practice, not joining it.
artificialanalysis
+2

Change: Say the 2:1 ratio matches current Index integration weights, and that the comparison field is the Omniscience Index, not a 1:1 blend of A and N.

Bug Hunt’s written estimand does not match the public source. The board’s own method says each repo gets one round, but a published row is often the mean of N identical runs, run-level CSVs are public, and a single run is not a model measurement: the same configuration has moved by 9 bugs out of 105. The draft’s n=1 path plus O19 makes that leaf either an unidentified quantity or, if a point is smuggled in, falsely certain. Because the pair SWE gate needs a second SWE leaf beside DeepSWE’s 30%, Bug Hunt sits in common support for the pairs that can be certified. Unidentified Bug Hunt then makes those pairs unevaluable.
github

Change: Estimand = mean of published runs for the exact model, effort, and harness. Θ uses those runs as public repeated runs. If n=1, certificate_role = unidentified; display the point, but the pair is unevaluable while Bug Hunt remains in B_ij. Do not invent a repeatability band for Θ_ij.

The printed exchange rate does not govern “recommended,” and the sentence that defines it is not implementable. It glues the anchor marginal rate to 0.25×SD(S_C) versus 0.75×SD(S_Q). Those are different objects. Under E8, pair quality is divided by p_ij and the cost term is not. At the pair-gate floor p_ij=0.70, a quality gap offsets about 1.43× as much cost as the printed headline rate. Close calls are exactly where the certificate matters. This is not a request to reverse E8.

Change: Publish two named quantities: anchor exchange rate 100·β·ln2 / ln(c_H/c_L), and within-cohort influence 0.25·SD(S_C) versus 0.75·SD(S_Q). Add p_ij and the pair’s implied cost-doubling offset to the E27 record. Flag a release when cost’s share of within-cohort score SD is under 10%, without changing β.

Bounds and bar tests disagree with the formulas that govern them. Q_i^L = p_i Q̄_i is the missing-at-0 bound at the point estimate only. It ignores measurement intervals, which the next sentence says extend the bound. The outputs section certifies a bar with Q_i^L ≥ Q_r^U and also with Q_i^L ≥ bar. The normative test is min_θ(Q_i(θ)−Q_r(θ)) ≥ 0. Normative text governs, so the outputs section will be implemented inconsistently.

Change: Delete the short equality. Define Q_i^L as the minimum of the full-composite expression over measurement intervals and missing-at-0. Make the outputs section cite only the joint normative test. If the bar must be a stable pin, publish it as a frozen scalar, distinct from Q_r(θ).

Two AA fields are unnamed, so the leaf can move without a migration. AutomationBench’s Index metric is objective completion with any guardrail violation zeroing the task, not “tasks completed.” GDP.pdf publishes both an all-pass headline and a task-macro mean pass, over 5 repeats. GPQA Diamond is no longer in the Index. A 1.25% leaf with no current AA series is not routinely refreshable.
artificialanalysis
+1

Change: Pin AutomationBench-AA Score and one GDP.pdf field in the leaf table. Drop GPQA at the next quality-version migration unless a public exact-variant series with a refresh URL is named in the registry.

Expired Plan rows re-enter the Plan table on API cost without the cross-estimand rule used for subset baskets. Governance puts API fallback in the official Plan ranking. The cost section excludes those rows from winner, frontier, and threshold claims, but not from displayed order. A reader can rank a plan-cost row against an API-cost row. Same defect as O17, different label.

Change: Apply “cross-estimand ordering not identified,” give them no Plan rank integer, and keep them in a side table. They stay outside J.

Low

Concordance is defined on the pooled value it is supposed to justify. max pairwise deviation ≤ 20% of the geometric mean is slightly circular and can be gamed by adding a third report. Pre-declare the check on the unpooled reports, then pool.

“Long context & science” is the wrong name for HLE, GPQA, SciCode, and CritPt. Rename the group. No weight change.

AA’s published cost is not the eval-run invoice. AA replaces the run’s cache rate with a live typical cache-hit rate before publishing cost. The scenario cache draw should be a named stress branch around that published protocol, not an independent redraw on top of a point that already embeds a cache assumption. Store AA’s cache date beside the cost field, as the registry already starts to do.
artificialanalysis

2. Methodology design recommendations

Write the eligibility predicate into the normative spec. J is full-workload, non-provisional, and, on the Plan basis, M_W-identified. Compute it before any margin. “Recommended” is outgoing certification inside that J only. That is the minimum change that makes the headline possible without weakening O21.

Align the blocker with the quality term. B_ij^price = B∩B_ij, SWE gate on that intersection, both sides of Δ_ij,alt on that intersection, result stored per pair. Below 40%, unidentified, not a pass.

Split the accounting identities. Index residual (HLE + Omniscience + CritPt) is a reconciliation item, never part of C_W. Coding Agent cost is average × tasks included in the average, repeats divided out once, missing telemetry left missing. One arithmetic fixture per source in the release tests.

Make Plan identification mechanical. Sliding 5-hour constraint, shared weekly pool, Fable 50% sub-cap and burn coefficient, price-list version match. Any missing piece means unidentified, not a borrowed multiple. Workday LP stays diagnostic under O3.

Pin leaves to the fields a monthly job can refetch. Bug Hunt = mean of results/runs.csv for the exact configuration. AutomationBench = Score. GDP.pdf = one named field. Omniscience disclosure corrected to AA’s 2:1 Index split. GPQA dropped until a live source exists. MMMU-Pro not admitted. Pending O15 components retire after two uncaptured releases.
artificialanalysis
+1

Publish the exchange rate the certificate actually uses. Headline anchor rate and SD influence as separate columns; E27 gets p_ij and the pair-specific cost-doubling offset. Do not leave the current compound sentence as the spec.

3. Questions for the owner

Should a subset-cost row, or a Plan row without identified M_W, be inside the contest that “recommended” quantifies over? If yes, the certificate quantifier has to change and the label cannot stay “against every rival in J.” If no, the eligibility predicate above is the fix. The rest of the recommendations do not depend on this answer.

4. Verdict

VERDICT: HAS FEEDBACK