# Internal review I66 — Claude Opus 5.5 (effort low) on draft r125

## 0. Read check

- First line of the draft: `# ValueRank methodology — draft r125`
- Last line of the draft (line 174): the revision-history paragraph, beginning "Revision history: r16–r24 fixed the published-record interval target…" and ending "…pools a cell by the E33 geometric mean and ties a report route to its cell's reports. Every change is recorded with its rationale in the ledger."
- Last 12 words of the last paragraph: "cell's reports. Every change is recorded with its rationale in the ledger."

What I read: `reviewer-prompt.md`; `ledger-brief.md`; `ledger.md` from "## Internal review I28" to the end, with close reading of O63–O83, E269–E270, the O71 outcome and the I56–I65 resolutions; `AGENTS.md` (the O71–O83 passage in full); `review-i65-claude-sonnet-5.5-max.md`; and `draft-r125.md` in full, in seven chunks.

What I verified:
- `python3 -m valuerank.draft_figures check` exits 0. `tests/test_plan_reports_provenance.py`, `tests/test_plan_admission.py` and `tests/test_draft_figures.py` pass (caches and bytecode off). `git status` is clean apart from this file.
- `valuerank/plan_admission.py` in full: E270 exclusions, partition and instant/date split handling, fault days, the O82 5-hour refusal, the geometric-mean cell value and `check_routes`.
- `data/plan_reports.json`: 107 rows and 93 `notTabulated` entries; the flag counts; the `rule` text; the fcten, waximabbax, kojimako, okarin and Weibo rows against the Kimi split.
- The registry's `reportEligibilityProfile` (`partitionSplits`, `accountingFaultDays`) and `changeDetection` in `data/plan_cost_routes.json`, compared with the draft's line 55 and with O83.
- `scores.json` `planAllowanceCells`: 52 cells per ranking, none passes. I re-ran `plan_admission.evaluate` with the Kimi split limited to the plans its detection covers. No cell's status changes.
- The quality-source shares (66/34 and 78/22) against the leaf table. The O82/O83 dates in the draft against the ledger, the registry and the commit dates.

Not verified: live web pages, the paywalled SemiAnalysis article, the Monte Carlo outputs, the full test suite. I also did not re-derive the cohort, the ladders, the anchors or the MiMo ceilings. I64 and I65 recomputed them on data that r125 did not change.

## 1. Findings by severity

### Critical

None.

### High

None.

### Medium

None.

### Low

**L1. The Kimi partition split is wider than O83 and than the draft's own rule (line 55; registry `partitionSplits`).**

O83 says a detected change splits the partition "for the plans it covers". The draft says "a change that flags a route also splits the report partitions for the same plans". The Kimi E18 outcome covers two CN plans only: Kimi Allegro (legacy, CN) and Kimi Max (new, CN). It flags no route, because no Kimi route rests on a report. Even so, the split entry has no `plans` field, so `plan_admission.applies` splits every Kimi plan, global Kimi Plus included. The registry admits this ("no global-plan report shows it, but the report partition splits for every Kimi plan (O83)"), but O83 does not say that. O79 widens a split only across a shared meter, and nothing records that the CN and global plans share one. Today this excludes waximabbax (Kimi Plus, 2026-10-24) as "spans a partition split" instead of giving the true reason (a 5-hour figure, O82).

Why Low: I re-ran the cells with the split limited to the two CN plans and no status changes.

What is new: I65 L4 asked only that Kimi's detection be recorded, and r125 recorded it. The scope question is new.

Change: add `plans` to the Kimi split, or record an owner or editor decision that a regional detection splits every plan of the provider. Also make the draft's sentence match whichever is chosen.

**L2. "A report route must carry exactly the cell's admitting reports, so the cell and the route cannot disagree" overstates `check_routes` (line 55).**

The code compares sorted observer names only. It does not compare report IDs, values, dates or the route's multiple with the cell's `multiple`. The I65 ledger entry says as much: "observers are exactly the cell's admitting observers". So a route whose reports carry the right observers but other values, or another unit or partition, passes the check.

The lookup is also keyed by (plan, model), while cells are keyed by (plan, model, unit, region). If week and month cells for one plan and model both pass, one overwrites the other in the dict.

Why Low: no cell passes, and the check fails safe on observer mismatch. I65's recommendation 1 is recorded as not adopted. This is a wording finding about r125's new sentence, not a repeat of that recommendation.

Change: either say "carries exactly the cell's admitting observers", or compare report IDs and require the route's pooled multiple to equal the cell's within storage precision, keying on the cell's unit too.

**L3. The O82 and O83 dates in the draft disagree with the ledger and the registry.**

Line 55 says "(owner decision O83, 2026-10-28)". The Value Multiple bullet says "owner decision O82, 2026-10-28". The ledger heading is "Owner decisions O82–O83 (2026-10-26)". The registry's `o72Application` says "O72-O83 (2026-10-26)" and the profile version is "2026-10-26". The r125 commit is dated 2026-10-28, so one of the two dates is wrong.

These are hand-typed dates in bold-free rule text, which the E265 lint does not police for decisions.

Change: give the decision one date everywhere (ledger, registry, draft, AGENTS.md if dated).

**L4. Two small wording mismatches in the Plan passages.**

- (a) The Known limitations say "most routed plan rows rest on a route flagged possibly superseded (21 of 27 and 44 of 51)". The denominators are all plan rows, including the 2 and 3 API-fallback rows that have no route. They should be "of 25" and "of 48", or the word "routed" should go. The count is `planFlaggedRows`, which also counts `expired`. Output 1 was corrected to "possibly superseded or expired" at I65 L5, but the limitations sentence was not.
- (b) Line 55 says "every priced report the O71 record holds for a cohort model, eligible or not, is a row". The table's own `rule` limits rows to a "priced, dated allowance figure", and it lists the rest in `notTabulated`. That list includes priced but undated figures such as Fun-Freedom-2313's ≈$2,725/week and issue #65's ≈$1,410/week. The draft should say "priced and dated" and mention `notTabulated`.

Why Low: both are true in substance today, and no output depends on them.

## 2. Methodology design recommendations

1. **Scope every split by plan in the registry (closes L1).** Make `plans` mandatory on each `partitionSplits` entry and build-check it against the matching `changeDetection` outcome or the O77 announcement's plans. Then a split can never reach plans its evidence does not cover, unless an owner shared-meter record (O79) lists them.
2. **Bind route to cell by identity (closes L2).** Key `passing` by the full cell key. Compare report IDs, and compare the route's pooled multiple with the cell's `multiple` within 0.0005, as the O46 ceiling check does. Add a fixture: same observers, different values, which must fail.
3. **Bring owner-decision dates under the figures lint (closes L3).** Read the ledger's decision headings into a decision→date map. Fail the check when a draft sentence prints a different date beside an O-number.

## 3. Questions for the owner

- **Q1 (L1).** Should a change detected on Kimi's China-region plans split the report partition for Kimi's global plans too? If yes, it should be recorded as a decision (it is outside O83's "plans it covers" and O79's shared-meter rule). If no, the registry split takes the two CN plans only.

## 4. Verdict

No Critical, High or Medium finding; four Low. The figure check exits 0, and the plan-admission, provenance and figure tests pass. r125 implements O82, the geometric-mean cell value and the re-transcribed report table with its provenance test as the ledger describes. What remains is narrow:
- a Kimi split that reaches plans its detection does not cover (L1);
- a route-to-cell tie described as stronger than the code (L2);
- a decision date that disagrees between documents (L3);
- two wording mismatches (L4).

None changes a score, rank, label, cell status or gate outcome today. Under O56 this is a clean round.

VERDICT: NO FURTHER FEEDBACK
