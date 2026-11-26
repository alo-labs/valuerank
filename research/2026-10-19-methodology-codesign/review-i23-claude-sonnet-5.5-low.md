# Internal review I23 — Claude Sonnet 5.5 (effort low) on draft r82

## 0. Read check
First line: "# ValueRank methodology — draft r82"
Last 12 words of last line: "covers two-thirds of cohort rows jointly with the admitted components (E95, E101)."
(All 1016 lines read, plus the ledger brief, AGENTS.md and ledger sections I20–I22 and O36–O38; no file edited. One web check: the Omniscience Index definition matches O28 per a third-party mirror of the AA paper (arXiv 2511.13029; AA evaluation page), not confirmed on an official AA page. Future-dated sources could not be checked.)

## 1. Findings by severity

**Critical**
None.

**High**
None.

**Medium**

M1. Stale "today" sentence contradicts the O36 cohort bullet (Cohort, "Precedence (O33)"). It says rows are ranked "today GPT-6.1 Sol, Claude Haiku 5.5 and Claude Sonnet 5.5 at five efforts each, Muse Spark 1.3 at two, and Grok 4.6 at xhigh", while the Full benchmark set bullet lists Grok 4.6 (xhigh) and Muse Spark 1.3 (xhigh) as listed, not ranked; the list predates O36 (ledger line 887). Two implementations or a reader get different ranked sets and counts. Fix: replace with the post-O36 list or generate it, and lint every "today" roster list against the build's ranked set.

M2. The frontier-families bar (E199) has an undefined population. The text says "the non-provisional frontier and near-frontier configurations alone" with "9 configurations" (references "8"), but a sibling "carries the tier of its own plotted point": Haiku 5.5 alone has three frontier vertices, and GPT-6.1 Sol and Sonnet 5.5 carry several efforts, so counting by own plotted tier gives far more than 9. Nine works only as one primary row per family, which is close to E205 (20 rows); the two are easy to conflate and their upper values coincide today (61.0). Fix: state E199's population exactly (primary row of each ranked frontier or near family, or all ranked rows whose own plotted point is frontier or near), print the family list and count, and add a multi-effort fixture.

M3. Gap fills and provider claims have no comparability record. O36 requires "the same benchmark version on the exact configuration", but the draft publishes only source type, publisher, configuration, link and harness, not benchmark version, task set and count, attempts and aggregation, or scoring field. Worst case: MiMo-V2.6-Pro's 30%-weight DeepSWE leaf is a provider claim; E233 only denies labels and E234 covers only third-party fills; the removal sensitivity moves it 6 ranks. Fix: a mandatory, build-checked comparability record for every non-AA fill (version, task set/count, attempts/aggregation, harness, metric field); a mismatch makes the fill inadmissible (row listed under O36). For provider claims, an in-row marker and a rank band across fill-removed and as-claimed.

**Low**

L1. Plan-evidence lifecycle dates are off by one against the draft's strict rule: the fixtures say age 90 is still possibly superseded, 91 expired, 120 expired, 121 demoted, so the first expired day is 2027-01-05 and the first demoted day 2027-02-04; the text gives the last day of the earlier stage. "Current until 2026-11-05" is correct. Fix: say "last day in stage" for all three, or move to 01-05 and 02-04.

L2. E216's 45-day model-page limit can never bind, since E211 and E217 cap the snapshot at 14 days (as Governance admits). Drop it, or define the price records as distinct from the snapshot's displayed prices.

L3. The anchor version string "v3-2026-10-21" was reused across re-freezes with changed anchor values (O33 lowered the low anchors); harmless before release but the identifier does not identify content. Append the anchor-object hash.

## 2. Methodology design recommendations (prioritised)
1. One generated "roster of record" table (ranked, listed, retained, primary vs sibling) from which every "today" statement and count is rendered (about 30 hand-maintained figures today).
2. The gap-fill and provider-claim comparability registry (M3), plus a provider-claim vs independent-run offset table wherever both exist for the same leaf, as a labelled sensitivity bound.
3. Reproducible end-user report search channels: Reddit and X were "unreachable from the build environment"; register discovery channels with API or archive access and a recall audit (known-report probe set) so absence of reports is evidence of absence.
4. A one-line caveat for "confirmed cheapest": with every row complete, Θ collapses to reporting-precision rounding, so "confirmed" means "stable under rounding of the published record"; the README says so but the draft's label wording does not (wording only, not a challenge to O25).

## 3. Questions for the owner
1. Does a frontier family count as satisfied (ranked) when only a retained sibling effort is ranked and its highest rendered point is listed? If yes, the "only way a frontier family goes unranked" text needs to say so; if no, retention must be suppressed for that family.
2. Owner decision challenge (O37): is a provider-claimed leaf on the 30%-weight DeepSWE leaf acceptable for a row shown in the main ranking, or should such rows sit in a separate listed band?

## 4. Verdict
VERDICT: HAS FEEDBACK
