0. Read check
Part 1: research/2026-10-19-methodology-codesign/perplexity/parts-r181/draft-r181-part-1-of-15.md

First line: # ValueRank methodology — draft r181

Final sentence: A change of AA chart or field is a versioned methodology migration, never a silent refresh.

Part 2: research/2026-10-19-methodology-codesign/perplexity/parts-r181/draft-r181-part-2-of-15.md

First line: ## Cohort and configuration (fixed policy)

Final sentence: Today the excluded configurations (O38: neither ranking's set) are frontier-family primaries Claude Opus 5.5 (xhigh), GPT-6 Astra (xhigh), Gemini 4 Carbon (high) and MiMo-V2.6-Flash, near-family primaries none, frontier families' near points none and non-primary points on the rendered frontier Claude Haiku 5.5 (low), GPT-6 Luna (low), GPT-6.1 Sol (xhigh) and GPT-6.1 Terra (low) near families' other near points none and configurations retained one release under O145 Claude Haiku 5.5 (xhigh), Claude Sonnet 5.5 (xhigh), GPT-5.6 Luna (low) and MiniMax-M3.1-Flash (max) (six classes that partition the excluded set; the build checks it); a family with an excluded primary may have other efforts ranked.

Part 3: research/2026-10-19-methodology-codesign/perplexity/parts-r181/draft-r181-part-3-of-15.md

First line: - Configuration rule (E188, amended by E193 and E251): a **family** is AA's model identity, the plotted model name without its effort and fallback qualifiers; it must equal the selected catalog model's display name, and MiMo-V2.6-Pro and MiMo-V2.6-Flash are separate families.

Final sentence: Both priced executions stay in the basket as the owner listed them; the overlap is disclosed.

1. Findings by severity
Critical

None.

High

Unbounded Directional Tolerance at Anchor Bounds Under Infeasible Domain Limits

Issue: In Part 1 under Transfer tolerance (E242), directional tolerance for clipped cost scores states: "a row at cost 
𝐶
C above the high anchor 
𝑐
𝐻
c
H
	​

 needs its multiple multiplied by 
(
𝐶
/
𝑐
𝐻
)
⋅
2
𝑡
/
𝑑
(C/c
H
	​

)⋅2
t/d
, and one below the low anchor 
𝑐
𝐿
c
L
	​

 needs it divided by 
(
𝑐
𝐿
/
𝐶
)
⋅
2
𝑡
/
𝑑
(c
L
	​

/C)⋅2
t/d
, and neither exists when 
2
𝑡
/
𝑑
2
t/d
 exceeds 
𝑐
𝐻
/
𝑐
𝐿
c
H
	​

/c
L
	​

". However, if 
𝐶
>
𝑐
𝐻
C>c
H
	​

 and the multiple moves upward (making cost smaller, shifting back into the anchor box), dividing cost by a factor 
(
𝐶
/
𝑐
𝐻
)
⋅
2
𝑡
/
𝑑
(C/c
H
	​

)⋅2
t/d
 requires that the cost shift within the box is unclipped, which requires 
2
𝑡
/
𝑑
≤
𝑐
𝐻
/
𝑐
𝐿
2
t/d
≤c
H
	​

/c
L
	​

. But for a row already below 
𝑐
𝐿
c
L
	​

 moving upward in cost, or a row above 
𝑐
𝐻
c
H
	​

 moving downward, the draft does not define an explicit fallback status string or numerical indicator when the tolerance is unbounded / nonexistent. In machine-readable outputs (scores.json), having a tolerance that silently fails or is omitted when 
2
𝑡
/
𝑑
>
𝑐
𝐻
/
𝑐
𝐿
2
t/d
>c
H
	​

/c
L
	​

 causes undefined keys or schema breakages.

Why it hurts the objective: Machine-readable consumers and automated validation gates relying on diagnostics.rankSeparability.plan.clippedTolerance will encounter missing values or NaN when anchor ratios are narrow relative to the threshold, preventing reliable automated reporting.

Concrete change: Amend the normative text in E242/E272/E305 to specify a deterministic output schema value when 
2
𝑡
/
𝑑
>
𝑐
𝐻
/
𝑐
𝐿
2
t/d
>c
H
	​

/c
L
	​

: explicitly record clippedTolerance: null accompanied by status: "threshold_exceeds_anchor_span".

Medium

Opacity and Asymmetry in Coding Agent Index Fallback Attempt Re-pricing (O158)

Issue: In Part 3 under Safety refusals (owner decision O63), fallback attempts are re-priced using captured prices from data/fallback_prices.json across the lower and higher of input and output price ratios. However, the draft specifies that "a fallback model without a captured price leaves the row 'unpriced'". If one fallback model in a multi-evaluation run is missing from data/fallback_prices.json, the entire sensitivity diagnostic becomes "unpriced", even if that fallback model accounts for a negligible fraction of attempts.

Why it hurts the objective: Discarding the entire fallback sensitivity diagnostic due to a single missing minor fallback model obscures cost fragility for configurations where fallback behavior could significantly impact user pricing.

Concrete change: Specify that if a fallback model lacks a list price, the re-pricing diagnostic computes a partial bound over priced fallback attempts and labels the coverage percentage (e.g., "priced_fallback_share": 0.92), returning "unpriced" only when the priced fallback share falls below 80%.

Residual Disclosed Status vs. Unregistered Systematic Divergence in Cost Reconciliation (O175)

Issue: Under Accounting identities (Part 3), the draft adopts O175 allowing an Index evaluation residual between 
10
−
6
10
−6
 and 
0.1
%
0.1% to remain marked CompleteCostEvidence, disclosing residualDisclosed. The draft notes that for Claude Opus 5.5, "the reconstructed nine-evaluation total exceeds AA's published Index total" by 0.03–0.04%, but notes "its cause stays unregistered".

Why it hurts the objective: Permitting unexplained discrepancies up to 0.1% without registering the sign and bound in the cost interval allows silent drift or undetected tokenizer changes from upstream aggregators to enter cost scoring unflagged in interval outputs.

Concrete change: Require that whenever residualDisclosed fires, the interval output layer treats the residual directionally: the lower bound of cost uses 
min
⁡
(
𝐶
reconstructed
,
𝐶
published
)
min(C
reconstructed
	​

,C
published
	​

) and the upper bound uses 
max
⁡
(
𝐶
reconstructed
,
𝐶
published
)
max(C
reconstructed
	​

,C
published
	​

), ensuring the interval is strictly enclosure-safe under O25.

Low

Punctuation and Syntax Run-on in Part 2 Excluded Configurations Partition

Issue: In Part 2 under Frontier and near families differ on purpose, the text lists the partition classes without separating commas or semicolons: "Claude Haiku 5.5 (low), GPT-6 Luna (low), GPT-6.1 Sol (xhigh) and GPT-6.1 Terra (low) near families' other near points none and configurations retained one release under O145...".

Why it hurts the objective: The lack of punctuation makes parsing the normative partitioning of the excluded set ambiguous during editorial checks.

Concrete change: Add semicolons between the six partition categories in that sentence to clearly distinguish non-primary points on the rendered frontier from near-family points and retained points.

2. Methodology design recommendations

Deterministic Bounding for residualDisclosed in Interval Outputs (Priority 1)

Design: Formalize the interaction between O175 and O25/E169 by defining the cost evaluation interval for any row exhibiting a non-zero reconciliation residual 
𝜖
≤
0.1
%
ϵ≤0.1% as 
[
𝐶
𝑊
−
∣
𝜖
∣
𝐶
𝑊
,
𝐶
𝑊
+
∣
𝜖
∣
𝐶
𝑊
]
[C
W
	​

−∣ϵ∣C
W
	​

,C
W
	​

+∣ϵ∣C
W
	​

].

Rationale: This preserves the integrity of interval outputs and BlockerSafe tests without holding releases for sub-0.1% rounding/precision discrepancies in AA’s reporting.

Standardized Fallback Model Pricing Registry Gate (Priority 2)

Design: Introduce a pre-build check in value_v3.check_open_web or the evidence bundle validator ensuring that any model appearing in fallbackAttemptCount across the captured Coding Agent Index manifest must have an entry in data/fallback_prices.json.

Rationale: Prevents fallback re-pricing sensitivity from collapsing into an "unpriced" state at release time.

3. Questions for the owner

None.

4. Verdict

VERDICT: HAS FEEDBACK