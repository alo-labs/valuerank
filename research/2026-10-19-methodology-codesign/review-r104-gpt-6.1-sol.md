0. Read check

I opened all 16 parts through the GitHub connector, in order, at commit 3bc659365d3bbe31b6541b955dd88e44d16611ea, and read each response to its end. Some parts end inside a sentence or table; those endings are identified below rather than represented as complete sentences.

First line:

ValueRank methodology — draft r186

Part 1:

A change of AA chart or field is a versioned methodology migration, never a silent refresh.

Part 2:

Today the excluded configurations (O38: neither ranking's set) are frontier-family primaries Claude Opus 5.5 (xhigh), GPT-6 Astra (xhigh), Gemini 4 Carbon (high) and MiMo-V2.6-Flash; near-family primaries none; frontier families' near points none; non-primary points on the rendered frontier Claude Haiku 5.5 (low), GPT-6 Luna (low), GPT-6.1 Sol (xhigh) and GPT-6.1 Terra (low); near families' other near points none; and configurations retained one release under O145 Claude Haiku 5.5 (xhigh), Claude Sonnet 5.5 (xhigh), GPT-5.6 Luna (low) and MiniMax-M3.1-Flash (max) (six classes that partition the excluded set; the build checks it); a family with an excluded primary may have other efforts ranked.

Part 3:

Both priced executions stay in the basket as the owner listed them; the overlap is disclosed.

Part 4:

These warnings test the API cost shape only; on the Plan basis the workload question is the M_W identification status.

Part 5:

Fable 5.1's Max multiples (12.4–12.7x against Opus 5.5's 57–59x) reflect Fable's own tighter allowance in Claude plans, so they are not used to illustrate how far the Opus 5.5 transfers could miss for other Claude models; the transfers keep their assumption label and caution.

Part 6 ends inside a sentence continued in part 7. Its final sentence-fragment is:

Report admission is computed (owner decision O81, 2026-10-26): a passing cell's value is the geometric mean of its non-provisional reports' midpoints (the E33 pool), each midpoint first clipped to the concordance band [largest lower bound ÷ 1.20, 1.20 × smallest upper bound] so a wide report cannot pull the pool beyond what O86 admitted, the band, taken over the same reports as the range test, being published (owner decision O115, 2026-10-29; the symmetric band leaves concordant point reports unchanged, E271), with the observers whose midpoint it moved (bandMoved, on reviewer 95), so a value the band decides is visible; owner decision O159, on reviewer 78: the range test reads the non-provisional reports, plus a provisional report only once its inferred tier or model has been re-checked against them and the check logged with the report (inferenceRechecked), so a wrongly scoped provisional report cannot fail a cell;

Part 7:

Evidence rules unchanged except for two owner exceptions, the O46 MiMo quota ceilings and the O76 speed-mode conversion of a user report (no provider marketing quotas otherwise; end-user API-priced reports or SemiAnalysis controlled measurements).

Part 8:

Domain validity is separate from evidence completeness.

Part 9 ends inside the quality table. Its final row is:

| | Code Migration v1.1 (Vals AI; code porting graded by hidden tests, 130 tasks; Pi agent harness for every model) | 6% | — | — | hidden-test pass rate (%), anchors 0–100; Vals' standard error recorded |

Part 10:

Only a genuine deployment-policy mismatch between the quality figure and the priced attempts is reconciled (as a bias bound in the identification layer); repetitions are not a bias.

Part 11:

Where public evidence cannot separate them the route is labelled "measurement and transport not separable" and its S0 result is not described as target-workload support.

Part 12:

The population is the ranking's ranked rows that are not provisional and have a displayed quality (every leaf of the ranking, O36; a listed row never sets a bar), ordered by displayed quality ascending, then configuration ID.

Part 13:

Each ranking's outputs compare that ranking's rows only, so a configuration ranked only in the other ranking is outside them too; the summary says these outputs compare ranked configurations only and names the listed configurations.

Part 14:

A new observed price under an unchanged price rule is a data refresh; changing a rule is a methodology migration; a benchmark-version change triggers a comparability review with dual-run where feasible.

Part 15 ends inside a sentence continued in part 16. Its final sentence-fragment is:

One AA state (E217): the model-page snapshot, the chart capture, the Coding Agent Index capture and the cost-chart capture are each at most 7 days from the snapshot, the build tests each of the last three against the release cutoff and the snapshot itself defines it (O65), and the build fails otherwise, and capture proximity alone does not show one AA revision, so the chart is also reconciled with the model pages on the fields both publish: each chart point linked to a captured page must carry that page's total Index cost (within 1%) and its displayed Index (the page's unrounded Index within half a display unit), and a mismatch stops the build for a re-capture of both (scores.json aaStateReconciliation, E322, on reviewer 87);

Part 16:

Revision history: omitted from this review copy (not normative); it is in draft-r186.md in the same folder of the repository.

The findings below concern the draft’s internal mathematical and policy consistency. References identify the parts and rule numbers read directly; this review does not assert that the implementation has the same defects.

1. Findings by severity
Critical

None.

High

None.

Medium
M1. The explanation of the transfer bracket reverses the price-ratio direction

Issue. In part 8, “Route brackets,” the draft first defines 
𝑟
r as target price per metered token divided by donor price per metered token and brackets the multiple between 
𝑀
M and 
𝑟
𝑀
rM. It then states:

The direction of the displayed figure's error is known where r > 1: on a token meter a dearer target exhausts the same allowance sooner, so its displayed multiple overstates its Plan value and its Plan cost is understated;

That explanation does not follow from the stated token-meter premise or the preceding bracket.

For a fixed, equally attainable token allowance and the same category mix, a higher API price makes those tokens worth more API-equivalent dollars. It does not make a raw-token allowance expire sooner. Under precisely that conditional comparison,

𝑀
target
=
𝑟
𝑀
donor
.
M
target
	​

=rM
donor
	​

.

Consequently, when 
𝑟
>
1
r>1, retaining 
𝑀
donor
M
donor
	​

 understates the target’s multiple relative to that conditional valuation—not overstates it. Its displayed 
𝐶
target
/
𝑀
donor
C
target
	​

/M
donor
	​

 is higher, not lower, than 
𝐶
target
/
(
𝑟
𝑀
donor
)
C
target
	​

/(rM
donor
	​

).

Why it hurts the objective. ValueRank’s objective depends on distinguishing actual subscription economics from labelled transfer arithmetic. This sentence gives readers the opposite interpretation of whether the displayed Plan value is optimistic or conservative. It also contradicts the same paragraph’s statement that the bracket’s low end is the conservative reading.

Concrete change. Keep O181’s donor multiple and the existing sensitivity bracket, but correct the explanation:

Conditional on an equal attainable raw-token allowance and the stated common token mix, 
𝑟
>
1
r>1 makes the donor multiple the lower end of the price-adjusted multiple bracket: retaining it gives a higher effective Plan cost than using 
𝑟
𝑀
rM. This conditional valuation does not establish equal allowances, equal attainment, or target-workload transport.

If a plan actually decrements its allowance using model-specific burn coefficients or API-valued credits, the direction must instead be derived from those coefficients; “token meter” alone does not establish it.

What is new relative to the ledger. This is not another request to replace the donor multiple, which O181 rejected. It identifies a sign inconsistency between the adopted bracket formula, its “conservative” description, and the newly added explanation. Correcting the explanation leaves the owner’s displayed-score decision intact.

Low
L1. “Known limitations” still says the AI Coding Daily ranking keeps labels that O182 now withholds

Issue. Part 16 says:

The AI Coding Daily ranking keeps its interval and scenario labels meanwhile, and its summary discloses the admitted basket and both pending units with their coverage (owner decision O133, 2026-10-30).

But part 12 states that its workload cross-check is currently 
0.35
0.35, below 
0.5
0.5, and that O182 withholds confirmed-cheapest interval labels and scenario-supported cheapest labels under that condition.

Why it hurts the objective. A reader reaching the limitations section receives a conflicting account of which cheapest-above-bar conclusions ValueRank currently supports. The earlier normative passage resolves the policy conflict, but the public explanation should not require readers to reconstruct amendment precedence.

Concrete change. Replace the sentence with:

Pending basket components do not themselves remove label eligibility (O133). Separately, the current AI Coding Daily workload cross-check is below 0.5, so O182 withholds confirmed-cheapest interval labels and scenario-supported cheapest labels; evaluated answers, displayed-record answers and diagnostics remain published.

Preserve the distinction between those cheapest labels and frontier or qualification outputs; O182 should not be described as withholding every interval output.

What is new relative to the ledger. O182 is adopted correctly in the governing workload-cross-check section. The remaining issue is its propagation into a current-state statement elsewhere, not a challenge to O133 or O182.

2. Methodology design recommendations
Priority 1: Make the bracket’s explanatory direction an executable invariant

Add a small dimensional and sign fixture beside the existing E23/E335 price tests.

For a single token category, let:

𝐵
>
0
B>0: attainable metered tokens in the period;

𝐹
>
0
F>0: gross cash;

𝑝
𝑑
>
0
p
d
	​

>0: donor API price per token;

𝑝
𝑡
>
0
p
t
	​

>0: target API price per token;

𝑢
>
0
u>0: target workload tokens.

Under an explicitly equal-token-allowance assumption:

𝑀
𝑑
=
𝑝
𝑑
𝐵
𝐹
,
𝑟
=
𝑝
𝑡
𝑝
𝑑
,
𝑀
𝑡
=
𝑟
𝑀
𝑑
.
M
d
	​

=
F
p
d
	​

B
	​

,r=
p
d
	​

p
t
	​

	​

,M
t
	​

=rM
d
	​

.

Then assert:

𝑃
donor figure
=
𝑝
𝑡
𝑢
𝑀
𝑑
,
𝑃
equal-token valuation
=
𝑝
𝑡
𝑢
𝑟
𝑀
𝑑
=
𝐹
𝑢
𝐵
,
P
donor figure
	​

=
M
d
	​

p
t
	​

u
	​

,P
equal-token valuation
	​

=
rM
d
	​

p
t
	​

u
	​

=
B
Fu
	​

,

and hence:

𝑃
donor figure
𝑃
equal-token valuation
=
𝑟
.
P
equal-token valuation
	​

P
donor figure
	​

	​

=r.

The fixture should check both 
𝑟
>
1
r>1 and 
𝑟
<
1
r<1, with 
𝑟
=
1
r=1 as the equality case. Generate the explanatory direction from this relation rather than maintaining a separate hand-written assertion.

This requires no new measurements, no version-to-version evidence transfer, and no change to the official multiple. It tests the interpretation of an already adopted sensitivity.

For any extension involving burn coefficients, keep the assumptions explicit. If 
𝑎
𝑑
a
d
	​

 and 
𝑎
𝑡
a
t
	​

 are evidenced meter units per token against a common budget, the corresponding conditional relation is

𝑀
𝑡
𝑀
𝑑
=
𝑝
𝑡
𝑝
𝑑
𝑎
𝑑
𝑎
𝑡
.
M
d
	​

M
t
	​

	​

=
p
d
	​

p
t
	​

	​

a
t
	​

a
d
	​

	​

.

Do not populate those coefficients from analogy or use this expression to identify 
𝑀
𝑊
M
W
	​

 without the draft’s existing transport requirements.

Priority 2: Generate current label-policy statements from the same gate result

E265 already generates numerical facts, while E63 exposes active-rule status. Extend the consistency check narrowly to the current-state label statements affected by O182:

Compute the workload-cross-check gate once.

Record its label scope: confirmed-cheapest interval and scenario-supported cheapest.

Render the headline, workload-cross-check section and limitations sentence from that result.

Fail the documentation check if a current-state passage says those labels are retained while that gate withholds them.

A fixture should include a ranking with pending components and a cross-check below 
0.5
0.5: pending status does not itself prohibit labels under O133, but the independently active O182 gate does.

No change to weights, normalization, cohort membership, evidence admission or uncertainty streams is warranted by these two findings. The existing distinctions between displayed arithmetic, published-record stability and benchmark-noise stress should remain.

3. Questions for the owner

None.

4. Verdict

VERDICT: HAS FEEDBACK