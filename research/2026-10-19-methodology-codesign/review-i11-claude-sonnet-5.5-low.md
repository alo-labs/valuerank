# Internal review I11 — Claude Sonnet 5.5, effort low, on draft r70

(Saved from the subagent's report; the reviewer read all 899 folded lines.)

## 0. Read check
First line: `# ValueRank methodology — draft r70`.
Last line (line 899) is only `(E95, E101).` The last 12 words of the document are: "covers two-thirds of ranked rows jointly with the admitted components (E95, E101)."
I read all 899 lines in three chunks, plus ledger-brief.md.

Verification: I did not web-search. The sources the draft relies on (AA pages, SemiAnalysis, tbench.ai, Bug Hunt Bench, dated October 2026) are not something I can independently check. I re-computed these draft claims and they hold:
- The Omniscience vectors, including the retired (2A+N)/3 scoring 82 and 66.
- The Bug Hunt vector 52/105 → 49.52.
- The ladder positions for n = 35 (zero-based 8, 17 and 25), and the reach counts 18, 27 and 10.
- The Clopper–Pearson endpoints, including the closed forms (δ/2)^(1/n).
- The exchange-rate algebra.
- The 70%-coverage fixture. The uniform case gives 91.5% and the arcsine case gives 86.7%, which I confirmed by simulation.
- The cohort arithmetic: 10 + 27 = 37, 36 scored, 35 in the bar population, 33 on the admission panel.

## 1. Findings by severity

**Critical**
None.

**High**
None.

**Medium**

M1. Fallback is part of configuration identity, but no rule says how it matches third-party leaf records.
- Where: the Objective names "model version, effort, fallback, route" as the identity. The Bug Hunt match key is "roster name, effort token, harness and route", with no fallback. The Terminal-Bench leaf is chosen for "exact model+effort". The cohort already contains AA points such as "Claude Sonnet 5.5 (max with fallback)" and Opus "(Max, Default Fallback)". Sibling rows are named "Family (effort)", which cannot tell max from max-with-fallback.
- Why it hurts: two faithful implementations can attach one Bug Hunt or tbench.ai record to both fallback variants (a transfer), to one only, or to neither. They can also collide on display names. This touches the "no transfer between configurations" policy.
- Change: add one normative sentence per leaf. For example, "a third-party record that does not state a fallback matches only the configuration whose fallback state the owner documents, otherwise the leaf is missing for fallback-qualified configurations." Include the fallback token in sibling names. Add a fixture with both variants plotted.

M2. The "unrewarded share" disclosure (E203) understates cost that buys work with no quality leaf.
- Where: the Capture status paragraph reports 15% as the median share on AA-Briefcase and GDP.pdf only. The Coding Agent Index is DeepSWE (113 tasks), SWE-Atlas QnA (124) and Terminal-Bench v4 (66), and the quality table credits only DeepSWE and, indirectly, the tbench.ai leaf. SWE-Atlas QnA is 124 of 303 tasks, about 41% of that unit's tasks, with no quality leaf.
- Why it hurts: the headline claims the cost side is "mostly coding work". Part of that coding spend is a codebase-Q&A task family the SWE quality leaves do not measure. The disclosure meant to show this omits the largest instance. E172 cannot isolate it because the Coding Agent Index is one admission unit.
- Change: extend E203 to count any admitted cost component or sub-component with no quality leaf (SWE-Atlas QnA, plus ITBench-AA once admitted). Where AA publishes per-sub-benchmark cost, add a within-unit removal diagnostic. Otherwise label the share "not separable" rather than omitting it.

M3. Three cutoffs are used but their relation is never stated.
- Where: E194 defines the report window as the 30 days ending on the "evidence search cutoff". E170 and E151 use the "release cutoff", which is the valuation timestamp V and the cutoff that governs evidence clocks. E211 measures capture age at "the release cutoff".
- Why it hurts: if the search cutoff precedes the release cutoff, a report's in-window status, the 30-day "possibly superseded" test and the 7-day capture gate can each flip depending on which cutoff an implementation reads.
- Change: state that they are the same timestamp. If they are not, define their order and which gate reads which. Add this to the registry fields.

M4. The provisional rule's SWE condition is ambiguous in prose.
- Where: "observed SWE weight ≥ 40% of quality". This can mean 40 points of the total 100 nominal weight, or 40% of the row's observed weight p_i. The code (quality.py, MIN_SWE_WEIGHT = 0.40 against a /100 total) uses the absolute reading.
- Why it hurts: a row with 60% coverage and all of it SWE passes the relative reading and fails the absolute one. Provisional status controls unique-cheapest eligibility.
- Change: write "observed SWE nominal weight ≥ 40 of the 100 quality points". The rule as written is also nearly redundant with the DeepSWE-required clause, so say that DeepSWE (30) plus one other SWE leaf is the minimum.

**Low**

L1. The bar ladder is degenerate at its stated minimum population. With n = 2, floor((n−1)k/4) = 0 for all k, so the lower quartile, headline and upper quartile bars are the same level and every row reaches it. Raise the minimum population to something that gives three distinct positions (n ≥ 5 gives positions 1, 2 and 3), or publish "ladder degenerate".

L2. Unexplained count differences.
- Bar currency says 18 rows reach the headline bar, while the displayed-record cheapest says 17. The likely cause is Muse Wonder Full, which has no cost and is therefore not scored. State this.
- The E205 diagnostic's "22 bar-population rows" (over 24 families) is easily confused with the 35 elsewhere. Label it "one-row-per-family population".

L3. E-number reuse. The header says each E number is one record, but the draft uses E198 for the bar-compare count and the displayed-level test, E184 for anchor availability and anchor eligibility, and E177 for the swing bridge and the swing gate. This is only a lookup risk. Give amendments suffixes (E198a and so on), as was done for E201a, b and c.

## 2. Methodology design recommendations

1. Run-count exposure. Publish Bug Hunt run count N beside each row and flag rows whose bar or frontier label changes if Bug Hunt is removed. The draft already has the standing Bug Hunt removal column. Under O25 the run-to-run noise stays outside the interval outputs, but a reader should see that a row rests on a single run. All of this data is public.
2. A leaf-source exposure line per ranked row. Retention now depends on one maintainer's benchmark (105 bugs, 2 repositories) and this decides which non-frontier configurations enter the cohort and set anchors and the bar. The diagnostics E199 and E205 cover the anchors and the bar. Add the retained-row share of the cohort to the headline, not only to a diagnostic.
3. Implement M2 (the extended unrewarded-share disclosure). It is cheap and bears directly on the objective of lowest cost for value.

## 3. Questions for the owner
1. Is the "common GPT multiple" and the "MiMo 1.5×" transfer authorised in a dated record? AGENTS.md records only the 2026-10-18 Opus 5.5 to other-Claude authorisation, and the draft calls MiMo 1.5× "an owner assumption without a donor measurement". If the 1.5× comes from a provider statement, it conflicts with the numerator rule. The answer would change whether those two routes are shown at all.
2. Should a configuration with a fallback qualifier inherit a third-party record that states no fallback (M1)? This decides between the "transfer" and "missing" outcomes.

## 4. Verdict
VERDICT: HAS FEEDBACK
