# Internal review I37 — Claude Sonnet 5.5 (effort medium) on draft r96

## 0. Read check

- First line of the draft: "# ValueRank methodology — draft r96".
- Last line of the draft: "configuration (O54, E252). Instruction following has no weight while Surge's Complex Constraints is excluded (O53). On the Plan basis the MiMo multiples are provider-derived quota ceilings, not measurements (O46)."
- Last 12 words of the last paragraph: "Plan basis the MiMo multiples are provider-derived quota ceilings, not measurements (O46)."
- Also read: `reviewer-prompt.md`; the whole folded draft (934 lines, in chunks, to the end); `ledger-brief.md`; `ledger.md` from "## Internal review I28" (line 1170) to the end (I28 to I36, O45 to O58, E246 to E262); `AGENTS.md`.
- Checked against repository data and code: `data/scores.json` (`v3` and `v3Tracks.aicd`: bar ladders, bar currency, displayed-cheapest and margin companions, anchors and workload hashes, admission objects, clip gates and `listedBeyondAnchors`, rank separability, bands, cost influence, indicative values of the listed families, family-primary diagnostic, near-frontier families), `valuerank/value_v3.py` (`SAMPLING_TASKS`, `sampling_sd`, `quality_sd`, `quality_margin`, `rank_separability`, `rank_bands`), `valuerank/basket.py`. I recomputed the ladder positions (n = 9, 15, 32), the two-bar-plus-margin levels, the 2^(threshold/doubling) tolerances, the exchange rates 3.04/4.06 and 2.83/3.77, the Plan row counts (27 and 50), the leaf-weight sums (60 in each ranking), the source-share percentages (72/28, 78/22), the 86.7% basket-scope weight, the SemiAnalysis age-stage dates, the fixture "91.5% uniform / 86.7% arcsine" (Monte Carlo 0.8675) and the Omniscience test vectors. All of these agree with the draft except the point in M1 below.

## 1. Findings by severity

**Critical**

None.

**High**

None.

**Medium**

**M1. The sample size n of AI Coding Daily's task-sampling noise (S1T) is ambiguous: six or sixty.**

- The issue. The S1T rule says each binomial leaf is redrawn with SD = 100·√(p̃(1−p̃)/n), "where n is the leaf's published task count", with p̃ = (k + ½)/(n + 1) and k = p·n. For AI Coding Daily the draft says "AI Coding Daily's six graded projects as a binomial share of 60 points, an assumption" (S1T paragraph, and again in the added-leaves bullet: "judged points over its six graded projects are read as a binomial share of 60 points"). "Six graded projects" gives n = 6, while "a binomial share of 60 points" is naturally read as n = 60 (k = points out of 60). The built code uses n = 6 (`SAMPLING_TASKS["aiCodingDaily"] = 6`, p = z/100). Two faithful implementers following only the draft would get SDs that differ by a factor of √10 on a 10%-weight leaf.
- Why it hurts. The choice is not cosmetic. With n = 6 the AI Coding Daily leaf has an SD of about 20 z-points at a mid-range score, which is about 2 quality points on its 10% weight and dominates the row's quality SD. The data show it: every AI Coding Daily row's value SD is 1.5 to 1.8, against 1.0 to 1.1 in the max-effort ranking, where no such leaf exists. That SD sets the AI Coding Daily ranking's separability median (4.45 value points API, 4.54 Plan), its bands (API 1–8, 9–14, 15), its separable-rank counts and grid, the E242 tolerance (5.28), and the O44 noise margin (5.9 quality points) and therefore every margin-companion cheapest row printed beside its bars. With n = 60 the row SD would fall by roughly a third and all of these would change. These are published outputs that AGENTS.md (O39, O42, O44) requires, so the number must be reproducible from the text.
- Recommended change. State the rule in one sentence, e.g. "AI Coding Daily: n = 6 (its graded projects), p = points ÷ 60, SD = 100·√(p̃(1−p̃)/6) on the z scale, an assumption; the six project scores are treated as six independent Bernoulli-like trials of the share, which overstates the variance of a mean of six bounded scores and is therefore wide." Use the same wording in the S1T paragraph, the added-leaves bullet and `methodology.md`. If the board publishes per-project points, say that the sample SD ÷ √6 would replace the Bernoulli form once captured (as the draft already does for GDPval-AA's per-row interval). Publish, as for GDPval-AA, a named sensitivity at n = 60 (the "narrow" reading) with the separable-rank count and the median, so a reader sees how much of the AI Coding Daily ranking's noise statement rests on this assumption.

**Low**

**L1. The O44 margin's "median row" is not tied to a row set.** `quality_margin` takes the median over the ranking's configurations (the API rows), and the same margin serves the API and Plan bases. On the Plan basis a "row" is a plan row (O48), and a median over plan rows would weight configurations by their number of plans (27 plan rows for 9 configurations; 50 for 15). Say "median over the ranking's configurations (one value per configuration, the same on both bases)". This is a one-clause fix and nothing in today's figures changes.

**L2. The O58 "today" sentence marks the factor-2 and rendered-frontier status for one listed row only.** The sentence flags GPT-6 Luna (low) (API, 4.75) as a rendered-frontier point past the factor-2 limit. The data (`gates.listedBeyondAnchors`) also have three Plan rows past factor 2 (Claude Haiku 5.5 (low) 3.41, a near point; Claude Haiku 5.5 (medium) 2.09 and GPT-6 Luna (low) 2.09, both rendered-frontier points). The draft's Plan list ends "all below" and a reader cannot tell which pass the limit. Add "past the factor-2 limit: Plan Claude Haiku 5.5 (low), Claude Haiku 5.5 (medium), GPT-6 Luna (low); all but Claude Haiku 5.5 (low) are rendered-frontier points".

**L3. Output 1 describes today's Plan ranking as "displayed arithmetic on owner-named transfers and unidentified observed multiples".** Today's Plan rows also include the O46 provider-derived quota ceilings (MiMo-V2.6-Pro) and SemiAnalysis's own measured figures for GPT-6.1 Sol (max), GPT-6 Astra (max) and Claude Opus 5.5 (max), all with unidentified M_W. "Owner-named transfers, the O46 quota ceilings and unidentified measured multiples" is accurate and matches the 14 of 27 and 48 of 50 counts given a few lines later.

**L4. One workload hash, two anchor objects.** The max-effort ranking's subset workload and the AI Coding Daily ranking's main workload are the same seven Index evaluations and share the hash `1453a9a0576b02ea`, but their anchors differ (API $39.78–$12,078.25 on 9 references against $10.35–$4,764.19 on 15). The draft says anchor objects are "versioned per basis and workload hash" and that each ranking has its own anchor version, so the identity is (anchor version, basis, workload hash). Say so in one sentence so that nobody reads the equal hash as a shared anchor object or as a cross-ranking comparability statement.

## 2. Methodology design recommendations

1. (Priority 1, answers M1.) Fix the AI Coding Daily sampling unit in the text, label it an upper-variance Bernoulli reading, publish the n = 60 sensitivity beside it, and replace it with the sample SD of the six project scores if the board's per-project points are captured. This keeps O39's "labelled approximation" honest for the one leaf whose noise currently drives a whole ranking's separability statement.
2. (Priority 2.) When the next refresh adds more AI Coding Daily or LiveBench rows, report beside each ranking's separability median the share of the median row's quality variance that comes from each leaf (the existing covariance-allocation machinery on the S1T variances). Today the reader of the AI Coding Daily ranking cannot see that one assumed leaf supplies most of the noise. This is a diagnostic only and changes no score.
3. (Priority 3.) Apply L1 to L4 as wording changes in the next draft.

I found no rule that is wrong, contradicts an owner decision or AGENTS.md, or cannot be implemented as written. Every stated figure I recomputed from the repository data matched, apart from the n ambiguity above.

## 3. Questions for the owner

None.

## 4. Verdict

VERDICT: HAS FEEDBACK
