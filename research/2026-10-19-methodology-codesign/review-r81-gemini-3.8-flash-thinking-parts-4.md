0. Read check

Read all three listed files to their ends through the GitHub connector, in order, at commit 0aedd96ddfb5c1e86ba1487bc7845bfe301e946d. This review covers only parts 4–6.

Part 4

First line:

Plan cost input (full-utilisation effective cost, labelled) = API cost input ÷ Value Multiple of the selected route. Computed per model–plan tier–surface–configuration route (tier and fee are part of route identity and published). Measurement objects (E111): each controlled measurement and each complete concordant report partition (E107) is a measurement object m = (route ID, partition ID, report IDs, measurement workload, valuation basis, allocation regime, measurement dates, identification object); …

The physical first line continues through the entire opening paragraph, ending “API-fallback rows are shown but excluded from Plan frontier and bar outputs.” The quotation above is its opening, not the complete physical line.

Last 12 words:

for other Claude models; the transfers keep their assumption label and caution.

Part 5

First line: empty.

First non-empty line begins:

Report window (E194, O32, E201a): the report window is the closed day interval [V − 30 days, V], and for each model × plan cell it ends instead at that cell's latest staged search, so it never claims days nobody searched

Last 12 words:

identify M_W. A schema change moves the route to the possibly-superseded stage.

Part 6

First line begins:

Value Multiple = API-priced usage a plan delivers over a stated fee period ÷ fee for that period.

Last 12 words:

value; no epsilon is introduced. Domain validity is separate from evidence completeness.

Source references below identify the retrieved part and its named rule. The connector returned file contents and Git blob SHAs, but no source-citation identifiers.

1. Findings by severity
Critical

None.

High

None.

Medium

The demand-accounting equation does not explicitly include the independently admitted ITBench-AA component. Issue: Part 6, E130, exhaustively describes two conserved populations: the nine Intelligence Index executions and the Coding Agent Index. It then defines the scored vector as

𝑑
𝑖
𝑊
=
∑
𝑒
∈
𝑆
𝑑
𝑖
𝑒
+
𝑑
𝑖
𝐴
.
d
iW
	​

=
e∈S
∑
	​

d
ie
	​

+d
iA
	​

.

Under the current basket decision O137 supplied in the ledger, ITBench-AA is also an independently admitted component. The equation is therefore incomplete unless 
𝑆
S includes that separate execution—but the immediately preceding population description scopes those 
𝑒
e variables to the Intelligence Index. Why it hurts the objective: This registry is supposed to establish the basket’s demand region for workload matching and eventual Plan transport. An omitted execution can make the demand object represent a different workload from the scored cost basket. Dollar reconciliation within each existing population would not necessarily detect that missing population. Concrete change: Define the scored demand by the admitted execution manifest rather than an enumeration of two current populations:

𝑑
𝑖
𝑊
=
∑
𝑗
∈
𝐽
𝑊
𝑑
𝑖
𝑗
,
d
iW
	​

=
j∈J
W
	​

∑
	​

d
ij
	​

,

where each admitted cost component maps to its own execution and accounting-population IDs. Explicitly include ITBench-AA and require set equality between the scored cost-component manifest and the demand registry’s component manifest. Missing category telemetry should produce unconstrained or publicly constrained demand variables, not an omitted component. What is new: This is not a request to add a benchmark or change O137. It concerns the demand equation’s closure after that already-adopted basket migration.
Source: part 6, “Identification roadmap and demand registry,” E124/E130; current basket decision O137 in the supplied ledger.

The report-window specification retains mutually incompatible cutoff requirements after the cell-specific search amendment. Issue: Part 5 first says that each cell’s window ends at its latest staged search. The same paragraph then says the build fails when the registry’s window does not end at release timestamp 
𝑉
V. Later, the section says reports after the all-provider search cutoff were not searched, although it also describes a later supplementary search for particular models. These statements can be reconciled by distinguishing a global release envelope from cell-specific admission windows, but the normative wording currently calls both “the report window.” Why it hurts the objective: Two implementations could admit different reports while each follows an explicit sentence: one admits through 
𝑉
V, another through the all-provider search, and another through the cell’s latest search. That difference can change source count, concordance and the selected Plan route. Concrete change: Define distinct fields and their exact relationship:

releaseReportEnvelope: 
[
date
⁡
(
𝑉
)
−
30
,
date
⁡
(
𝑉
)
]
[date(V)−30,date(V)].

searchedThrough[cell]: the latest completed three-stage search covering that cell.

newReportAdmissionWindow[cell]: the release envelope intersected with dates no later than searchedThrough[cell].

previouslyAdmittedReports[cell]: retained separately under O127, subject to clocks and schema eligibility.

Specify explicitly whether O161 changes only the upper endpoint or shifts the entire 31-date window. Replace the blanket “reports dated after the search cutoff were not searched” with a statement about the all-provider search and disclose supplementary cell coverage separately. What is new: O161’s cell-specific search endpoint is already adopted. This finding concerns the remaining release-cutoff assertion and summary language that do not distinguish it from the global envelope.
Source: part 5, “Report window,” “One release cutoff,” “Search age,” supplementary entrant research, and the concluding current-window description.

Low

None.

2. Methodology design recommendations

Prioritise executable closure between cost and demand manifests. Use one admitted execution manifest as the source of truth for both the cost sum and demand-region construction. For every execution, publish:

Cost component and execution IDs.

Accounting-population ID.

Available category-demand constraints.

Telemetry and aggregation compatibility.

Whether demand is observed, structurally bounded or unresolved.

Require:

{
scored cost executions
}
=
{
demand-region executions
}
.
{scored cost executions}={demand-region executions}.

An execution may have unresolved demand while retaining its owner-authorised displayed cost. This preserves the existing no-imputation and unidentified-transport policies rather than manufacturing a category mix. Add a fixture in which ITBench-AA is admitted without category telemetry: its cost must enter the basket, its demand variables must enter the registry, and its missing telemetry must remain visible.
Basis: part 6, E124, E130, E157 and E131.

Compile report admission from a typed temporal object. Make the global envelope, per-cell search coverage, observation dates, previous admission dates, schema partitions and age stages separate inputs. Publish a per-report admission trace showing which predicate admitted or excluded it. Add boundary fixtures for:

A report after the all-provider search but before a later search covering its cell.

A report after its cell’s latest search but before 
𝑉
V.

A report exactly 30 calendar days before 
𝑉
V.

A previously admitted report outside the new-report window.

A supplementary search covering one model but not another on the same provider.

These fixtures implement O161 and O127 without changing concordance, evidence grades, or owner-authorised routes.
Basis: parts 4–5, E151, E194, E213, O127 and O161.

3. Questions for the owner

None. Both recommendations are implementation clarifications of adopted policy, not requests to reopen the ranking weights, evidence thresholds or Plan assumptions.

4. Verdict

The reviewed sections carefully separate observed consumption, established capacity, workload transport and valuation compatibility. The remaining material issues are specification closure: the demand equation should cover every admitted execution, and report admission should have one unambiguous temporal interpretation.

VERDICT: HAS FEEDBACK