1. Findings by severity
Critical

None.

High

The five-category token ontology is insufficient for request-dependent tariffs. Issue: E131 represents demand using five mutually exclusive token categories, while E84 requires reconciliation through 
𝑝
release
⋅
𝑑
=
𝐶
p
release
	​

⋅d=C. That representation works when each category has a constant unit price. It does not generally work when the price of input and output tokens depends on the request’s context-length band. Google’s published pricing, for example, distinguishes prompts at or below 200,000 tokens from longer prompts and changes both input and output prices. Two execution ledgers can therefore have identical five-category totals but different API valuations.
paste.txt
google
 Why it hurts the objective: This affects more than a displayed cost caveat. It can invalidate a demand–cost reconciliation, a report’s revaluation to the release tariff, or an assertion that Plan cost is invariant to repricing. E141 already recognises tariff applicability and a known long-context omission; the new argument is that the underlying demand representation cannot express this class of tariff even after its effective date and applicability are recorded.
paste.txt
 Concrete change: Make tariff applicability part of the demand coordinates. Permit category-only vectors only after certifying that category totals are sufficient for the applicable billing rule. Otherwise require token totals partitioned by evidenced billing band, a compatible request ledger, or conservative bounds. Where none exists, retain the owner-required displayed cost but mark tariff-corrected valuation or transport unidentified. Do not fit an effective price merely to force reconciliation.

Medium

The buyer-facing cost boundary is less explicit than the mathematical workload boundary. Issue: The draft precisely defines which benchmark executions enter 
𝐶
𝑊
C
W
	​

, but the headline “API cost” and objective’s “lowest cost … in practice” do not consistently distinguish contestant-model token charges from other execution costs. The matched-cost diagnostic explicitly excludes sandbox, environment-setup and verifier compute; AA also documents evaluations whose reported costs exclude judge calls, PDF preparation and OCR. These are different cost boundaries, even when all underlying numbers are correctly captured.
paste.txt
artificialanalysis
 Why it hurts the objective: A buyer can reasonably read “USD to run this workload” as an execution budget rather than a model-token subtotal. Expenditure concentration and matched-cost diagnostics do not resolve which necessary services are excluded. Concrete change: Add a cost-boundary object for every component and label the primary dollar column “contestant-model API token cost for the benchmark basket.” State beside the headline that it is not total agent or workflow operating cost. Publish separately evidenced non-token charges only as a diagnostic; leave unknown charges unknown. What is new relative to E17 and the existing limitations: This is not a request to change O15’s basket, remove the two Terminal-Bench executions, or add estimated infrastructure costs. It makes the already-selected accounting boundary explicit in the primary claim and validates it component by component.
paste.txt

Registry versioning does not yet guarantee preservation of the source evidence needed to rebuild a release. Issue: The source contract records chart identity, fields, timestamps, revisions and configuration manifests, and several derived objects have hashes. It does not explicitly require retaining the underlying public payloads or captured evidence bytes and the extraction procedure that produced each scored observation. A snapshot timestamp identifies when a page was seen; it does not preserve what was seen.
paste.txt
 Why it hurts the objective: Monthly refreshes can remain internally reproducible while older releases become externally unauditable when a leaderboard, embedded dataset, methodology page or report changes. This is particularly consequential for completeness markers, exact-effort matching and the frozen Plan report partitions. Concrete change: Require an immutable evidence bundle for each release: publicly retrievable source payloads or permitted captures, content hashes, extraction-code version, source-field locations, and a mapping from each observation to its evidence artifact. Where redistribution is restricted, retain the permitted capture and publish its hash and a precise evidence locator. What is new relative to the source contract and E63: The addition is source-artifact preservation and extraction replay—not another registry field list or another active-rules manifest.
paste.txt

Low

None.

2. Methodology design recommendations
Priority 1 — Replace the universal category-price identity with a tariff-aware valuation contract

Keep the current five token categories as the semantic ontology, but distinguish them from the sufficient statistics required for billing.

For tariffs that are linear after partitioning by billing band, use:

𝐶
𝑖
𝑒
=
∑
𝑏
∈
𝐵
𝑖
∑
𝑘
∈
𝐾
𝑝
𝑖
𝑏
𝑘
 
𝑑
𝑖
𝑒
𝑏
𝑘
,
C
ie
	​

=
b∈B
i
	​

∑
	​

k∈K
∑
	​

p
ibk
	​

d
iebk
	​

,

where:

𝐾
K contains the existing five mutually exclusive token categories.

𝐵
𝑖
B
i
	​

 contains the applicable, publicly documented billing bands.

𝑑
𝑖
𝑒
𝑏
𝑘
d
iebk
	​

 is token demand in category 
𝑘
k, assigned to band 
𝑏
b using the source’s request-level applicability rule.

𝑝
𝑖
𝑏
𝑘
p
ibk
	​

 is the applicable release tariff.

For a billing rule that cannot be represented this way, use an explicit request-level billing function:

𝐶
𝑖
𝑒
=
∑
𝑟
∈
𝑅
𝑖
𝑒
Bill
⁡
𝑖
,
𝑡
(
𝑟
)
.
C
ie
	​

=
r∈R
ie
	​

∑
	​

Bill
i,t
	​

(r).

This is necessary because publicly documented tariffs can depend on prompt length, not merely total input and output consumption.
google

Add three registry fields:

valuation_sufficiency: category totals sufficient / tariff-stratified totals sufficient / request ledger required / unresolved.

billing_rule_id: versioned rule and applicability evidence.

tariff_allocation_support: observed / structurally bounded / unavailable.

Implement four regression tests:

Identical five-category totals with different request-length allocations can produce different costs.

Splitting a token category into billing bands preserves the original total token count.

Reconciliation rejects a category-only vector when the tariff requires unavailable band allocation.

The current scalar uniform-price-scaling cancellation still holds where its assumptions actually hold.

If billing-band allocations are unavailable, bound them using only public constraints. Do not rescale demand or infer allocations from cohort averages. This preserves exact-variant evidence and O27’s displayed cost convention while preventing an unsupported transport identification. The immediate benefit is a correct identification contract; it does not manufacture identified Plan routes where the required public evidence is absent.
paste.txt

Priority 2 — Add a typed cost-boundary matrix without changing the primary basket

For each execution component, record each relevant charge class as:

included;

excluded;

not applicable;

unknown.

Charge classes should cover contestant-model tokens, other model calls, external tools, execution environments, preparation/OCR, and grading or verification. Add a role field distinguishing deployment-required costs from evaluation-only costs; a benchmark judge is not automatically a buyer’s production expense.

The primary basket remains unchanged:

𝐶
𝑊
primary
=
𝐶
𝑊
contestant-model tokens
.
C
W
primary
	​

=C
W
contestant-model tokens
	​

.

A supplementary operating-cost figure should be published only where its included services, public prices and measured quantities are evidenced for the exact execution. Otherwise publish the boundary matrix without a synthetic total.

This is implementable from public methodologies and run documentation. AA already distinguishes contestant-model costs from excluded preparation and judging costs in relevant evaluation documentation.
artificialanalysis

Priority 3 — Make historical rebuilds consume frozen evidence, not live sources

Define the release artifact as:

Release
=
(
method version
,
registry
,
evidence bundle
,
extractor version
,
outputs
)
.
Release=(method version,registry,evidence bundle,extractor version,outputs).

For each observation, retain:

evidence artifact ID and content hash;

retrieval time and any separately known observation time;

field path, table cell or chart-series locator;

original published value and precision;

applicable completeness or declined-task marker;

extraction transformation and resulting canonical value.

Add a release test: rebuilding from the frozen bundle must reproduce admitted components, route selection, anchors, scalar scores and deterministic interval statuses without consulting current pages. Scenario outputs must additionally reproduce under the recorded RNG implementation, seed and draw order.

This extends the draft’s existing hashes and reproducibility rules to the evidence acquisition boundary, where the current contract remains incomplete.
paste.txt

3. Questions for the owner

Is the intended buyer-facing claim limited to contestant-model token spend, or should ValueRank eventually estimate total deployment-required execution spend? The former needs clearer primary labelling; the latter also needs a separately governed cost-expansion roadmap.

Are source payloads and extraction artifacts already preserved in the repository under a binding release rule omitted from this draft? If so, the archival recommendation reduces to incorporating that rule by reference and adding the rebuild test.

4. Verdict

VERDICT: HAS FEEDBACK