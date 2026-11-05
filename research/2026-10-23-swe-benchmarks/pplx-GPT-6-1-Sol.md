Recommendation: do not add another mandatory SWE leaf yet. The strongest independent candidates are AI Coding Daily, Vals’ Vibe Code Bench v1.1, Code Migration v1.1, and LiveBench’s coding evaluations—but I could not establish near-complete, exact-configuration coverage for any of them. AI Coding Daily explicitly omits several important effort variants; Vals has broad model coverage but incomplete effort provenance and some fallback-assisted results; LiveBench currently exposes conflicting release views. Those are eligibility problems under O36, not merely documentation inconveniences.
livebench
+4

The most promising additional AA-supplied benchmark is SWE-Atlas-QnA-AA, which adds repository comprehension rather than another patch-generation test. Its current methodology is well specified, but its complete 51-configuration coverage was not verifiable from the captured results, and it would not diversify evaluator dependence.
artificialanalysis

1. What this audit establishes—and what it does not

I treated the supplied roster and O36 as binding. I did not substitute nearby versions, transfer scores between efforts, or treat an unqualified model name as “default.”

The attached evidence files contain:

An observed-results CSV with scores, reported efforts, source labels, provenance, and qualifications.

A roster-coverage CSV crossing all 51 supplied configurations with the 18 benchmark/release views for which I captured roster-related observations.

A coverage summary and an audit README.

These are evidence inventories, not certified headline inputs. “No result observed” means absent from the sources captured here—not proof that a result does not exist.

Two important identity limitations

The brief specifies efforts for only some roster entries. For example, “GPT-6 Astra,” “Claude Opus 5.5,” and “GPT-6 Luna” do not state their required efforts. Their externally reported efforts can be listed, but an exact match cannot be certified without the AA configuration mapping.

The priority list includes Haiku 5.5 xhigh, whereas the enumerated 51-row roster includes max/high/medium/low/default, not xhigh. I preserved the 51-row roster rather than silently adding a configuration.

Consequently, the useful distinction throughout this report is:

Model-label coverage: a recognizable version or candidate alias appears.

Effort-label coverage: that result explicitly names the required effort.

Eligible exact-configuration coverage: version, effort, benchmark release, harness, task split, and fallback provenance all pass validation.

None of the counts below should be mistaken for the third category.

2. Coverage-first shortlist

The following counts refer to distinct roster-model labels captured in this audit, out of the roster’s 37 distinct model names—not out of its 51 configurations. Dated revisions and aliases remain conditional where noted.

Benchmark/release	Captured roster-model labels	Exact-effort situation	O36 disposition
AI Coding Daily, current 70-point board	22	Explicit efforts, but important variants missing; harness differs by model	Strong diagnostic; not a new mandatory leaf
Vibe Code Bench v1.1	37 candidate labels	Broadest apparent coverage; most table rows omit effort; announcement settings need binding to individual runs	First independent provider to pursue for coverage completion
Code Migration v1.1	18	Mostly one unlabeled-effort row per model	Useful complement, insufficient coverage
LiveBench legacy 2026-06-25 Coding	25	Many explicit max/xhigh/high labels; no broad effort sweep	Diagnostic only
LiveBench legacy Agentic Coding	25	Same limitation	Diagnostic only
LiveBench 2.0 Coding	30 candidate labels	Captured table omits effort; different release and scores	Hold pending release/configuration reconciliation
SWE-bench Multimodal, Vals	16 candidate labels	Mostly unspecified effort; several frontier models absent	Diagnostic only
ProgramBench, Vals	34 candidate labels	Mostly unspecified effort; strict scores heavily floor-compressed	Diagnostic only
IOI v2, Vals	30 candidate labels	Mostly unspecified effort; leaders already at 100%	Low-priority coding diagnostic
Vibe Code Bench 1–100	19 candidate labels	Mostly unspecified effort; important current models absent	Excellent task complement, poor current coverage
CyberBench v1.1	30 candidate labels	Effort and fallback qualifications; not broad SWE	Security diagnostic
SRE Bench, Vals	26 candidate labels	Effort/fallback qualifications; reverse engineering, not site reliability	Not a DevOps leaf
Terminal-Bench 4.0, Vals	34 candidate labels	Independent execution, but same underlying benchmark already weighted	Cross-check, not an additional task-diversity leaf

Sources for these inventories are the corresponding captured leaderboards; the full model/value lists are in the attached CSVs.
livebench
+11

The decisive finding is that a leaderboard with 118 rows can still fail O36: those rows may cover older models, alternate harnesses, or only one effort for each current version. Vals’ Vibe Code Bench illustrates this particularly clearly.
vals

3. AI Coding Daily: valuable independent evidence, incomplete effort coverage
What it measures

Povilas Korop’s benchmark evaluates ticket-sized changes to existing applications—not greenfield competitive programming and not multi-agent orchestration. The methodology describes seven projects and 27 prompts spanning Laravel/PHP, React/TypeScript, Flutter/Dart, and Go. Each prompt starts from a fresh project copy, with no human coaching; prompts are repeated to reduce dependence on a lucky run. Hidden evaluator tests and scoring rubrics are withheld from the implementer.
aicodingdaily

The current board totals 70 points:

Laravel code quality: 20.

React/TypeScript code quality: 20.

Bug finding: 10.

Edge-case testing across four projects: 20.
aicodingdaily

These are weighted rubric/project points, not “percentage of issues resolved.” A prospective ValueRank transform would therefore be 
100
×
points
/
70
100×points/70, tied to this exact scoring revision—not to older 80-point pages.

Current roster-related results

All values below are points out of 70. These are observed configurations, not an assertion that the unspecified AA roster efforts match.

Roster model	Explicitly reported efforts and scores
Claude Opus 5.5	high 67.26; medium 65.28; low 60.50
GPT-6 Astra	high 66.35; medium 66.03
GPT-6.1 Sol	high 66.00; medium 65.05; low 61.45
Claude Sonnet 5.5	high 64.31; medium 60.54
DeepSeek V4.1 Flash 1017	max 61.20 in DeepSeek Harness; max 60.97 in OpenCode; high 55.21 in OpenCode
Claude Fable 5.1	medium 61.03
Grok 4.7	high 60.09
GPT-6 Sol	high 59.92; medium 56.32
GPT-6 Luna	max 59.07; xhigh 56.40; high 53.04; medium 43.74
Claude Haiku 5.5	high 58.63; medium 58.20
Gemini 4 Argon	high 57.09
Kimi K3	high 56.89
Grok 4.6	high 56.71—not the explicitly rostered xhigh configuration
GLM-5.3	high 54.82
MiniMax-M3.1-Flash	max 54.48
MiMo-V2.6-Pro	high 53.81
MiMo-V2.6-Flash	high 53.29
Muse Spark 1.3	max 53.01
DeepSeek V4 Pro candidate	source says V4-Pro-0813: max 50.35; high 48.34
GLM-5.3 Flash	max 47.51
Gemini 3.8 Flash	high 47.09
Qwen3.8 Max candidate	source says Qwen 3.8 Max 0902: high 53.39

All entries are from the current leaderboard. The dated DeepSeek and Qwen revisions require explicit AA mapping.
aicodingdaily

Coverage failures that matter most

Among explicitly effort-qualified roster entries, the current table supplies label matches for GPT-6.1 Sol high/medium/low, Haiku high/medium, Sonnet high/medium, and Muse Spark 1.3 max. It does not show GPT-6.1 max/xhigh; Haiku max/low/default; Sonnet max/xhigh/low; Muse Spark 1.3 xhigh; or Grok 4.6 xhigh. Hidden historical rows might extend older-model coverage, but they do not establish these missing current effort results.
aicodingdaily

Provenance, freshness, capture, and methodology risks

Runner and independence: benchmark owner; independent of AA.

Harness: Claude Code, Codex CLI, OpenCode, Cursor, Devin, Antigravity, and a DeepSeek harness appear. This measures a model–agent stack, not a standardized model-only treatment.

Identity: useful version and effort labels; immutable API snapshot IDs and agent-version pins were not established.

Freshness: leaderboard last updated October 21, 2026, with frequent release-driven additions and retests.

Capture: the HTML table is extractable; I did not establish a public JSON/CSV/API feed.

Contamination: hidden tests help, but reused projects and publicly discussed prompts do not demonstrate training-time cleanliness.

Saturation: the leading score is 67.26/70, with several leaders perfect on the edge-case component.

Version drift: the main board says 70 points, while an individual model page captured an 80-point layout and different leading scores. Store the entire scoring schema with each snapshot; do not merge those pages indiscriminately.
aicodingdaily
+2

Disposition: retain as a high-value independent diagnostic. A future 5-percentage-point quality leaf is defensible only after exact-effort completion and explicit acceptance of the varying-harness estimand.

4. LiveBench: incorporate both coding categories, but separate the releases
A material source conflict

The supplied root URL returned LiveBench 2.0, released October 14 and last updated October 18, with seven suites including Coding and a broader Agentic suite. A separate indexed LiveBench URL returned the legacy June 25 release, with Coding and Agentic Coding explicitly separated. The published June CSV contains fewer recent models than that legacy rendered page.
livebench
+2

These views cannot safely be combined into one leaf:

Legacy Coding and Agentic Coding are not interchangeable with 2.0 Coding and Agentic.

A max effort named on the legacy board cannot establish the effort of a similarly named 2.0 row.

The legacy CSV’s release date is not its model-evaluation date.

Legacy Coding and Agentic Coding

The category JSON defines Coding as code_generation plus code_completion, and Agentic Coding as JavaScript, Python, and TypeScript tasks. The repository changelog says coding questions stopped being sourced from LiveCodeBench in April 2025 and moved to realistic library-use questions. Thus, the original LiveBench paper’s LiveCodeBench description is outdated for this release.
livebench
+1

Agentic Coding uses real repository issues and the Multi-SWE-Bench evaluation harness. In October 2025 the agent changed from SWE-Agent to mini-SWE-agent, with a 250-step rather than 50-step limit; all models were reportedly rerun for that change.
github

Selected legacy results:

Configuration	Coding	Agentic Coding
Claude Opus 5.5 max	89.3	71.7
Claude Fable 5.1 max	86.4	66.1
GPT-6 Astra max	80.4	57.3
GPT-6 Sol max	81.8	52.9
GPT-6 Luna max	79.0	51.2
GPT-5.6 Luna max	82.9	48.4
Muse Spark 1.3 xhigh	81.1	64.1
Gemini 3.8 Flash high	72.5	54.2
Grok 4.7 xhigh	77.2	54.0

The complete captured roster-related legacy list is in the observations CSV. These scores belong only to the legacy release.
livebench

The captured primary materials did not establish a clean, current per-category question count. “23 tasks” on the legacy page denotes task types across all categories, not 23 individual coding problems. I would not invent a coding denominator from it.
livebench

LiveBench 2.0

The 2.0 table has current model names, including Opus 5.5, Sonnet 5.5, Haiku 5.5, GPT-6.1 Sol, DeepSeek V4.1 Flash 1017, and MiniMax M3.1 Flash. However, the captured rows omit reasoning effort. For example:

Model label, effort unspecified	2.0 Coding
Claude Opus 5.5	96.3
GPT-6.1 Sol	96.0
DeepSeek V4.1 Flash 1017	96.0
Claude Sonnet 5.5	94.7
GPT-6 Astra	93.7
Claude Haiku 5.5	91.4
GPT-6 Luna	84.5
MiniMax M3.1 Flash	83.9
MiMo V2.6 Pro	81.5

MiMo V2.6 Flash was not present in the captured 2.0 table. Nor does one unlabeled Haiku or Sol row cover the roster’s multiple efforts.
livebench

Operational assessment

Runner: LiveBench’s evaluation project; the repository also enables reproducible outside runs. Per-row submission provenance still needs validation.

Scoring: legacy emphasizes objective, programmatically verifiable ground truth; do not transfer that blanket description to every 2.0 suite without its current methodology.

Capture: legacy category JSON and subtask CSV are directly accessible; current 2.0 machine-readable results and effort metadata were not established.

Cadence: legacy page says six-month refreshes, whereas the older changelog describes monthly releases. Use the selected release’s actual contract, not a generic “monthly” claim.

Contamination: refreshing questions reduces exposure, but publicly released questions become exposed; “contamination-free” is not an unconditional guarantee.

Saturation: legacy Agentic Coding retains substantial headroom; 2.0 Coding already has several scores in the mid-to-high 90s.
livebench
+4

Disposition: independently useful, but not presently ingestible as a complete exact-configuration leaf. Require a pinned release, category denominators, current harness definition, and per-run effort identities first.

5. Surge AI ComplexConstraints: incorporate, but not as SWE quality
What can be verified from primary sources

The public harness describes 75 expert-written prompts, each with 10–40 rubric criteria, totaling 1,559 criteria. Models answer once without tools or an agent. An LLM judge grades one criterion at a time. The harness reports:

all_pass/mean: tasks satisfying every criterion.

mean_criteria/mean: average fraction of criteria satisfied.

It also supports repeated epochs and pass@k/reliability reducers. These metrics must not be mixed.
github

The paper describes a larger, approximately 1,000-prompt dataset used for evaluation/training research. That is not evidence that the public leaderboard evaluates 1,000 tasks. Its historical table is also not the current roster’s leaderboard.
arxiv

Coverage and retrieval limitation

The owner-named primary leaderboard URL did not return usable content through repeated fetch attempts. I therefore cannot certify its current rows, efforts, last-update date, judge configuration, or data endpoint.

A secondary mirror lists, among others, GPT-6 Astra 57.7, Gemini 4 Argon 53.3, Muse Spark 1.3 51.9, GPT-6 Sol 50.8, GPT-5.6 Sol 50.5, Opus 5.5 49.9, and Grok 4.7 48.9. It does not expose their efforts or dependable row-level evaluation dates. Those observations are explicitly marked secondary-only in the CSV, not admitted as exact-configuration evidence.
atlas.kevinhu

Fit and methodological issues

It measures dense, interdependent instruction following—not code execution, repository repair, or infrastructure remediation.

It is independent of AA.

The public harness is machine-runnable and produces Inspect logs, but that does not establish a machine-readable current leaderboard.

The judge is configurable; reproducing the published board requires its precise judge and settings.

The harness explicitly warns that nonstandard model names can silently prevent reasoning-effort settings from mapping correctly.

Public prompts and the dataset’s explicit use for RL training make training-exposure controls important.

Historical low perfect-task rates do not establish current non-saturation.
github
+1

Disposition: 0% of SWE quality. Consider it for an instruction-following diagnostic or an appropriately defined non-SWE component, after primary coverage verification.

6. Vals AI: the best independent coverage-development partner

Vals states that it runs its own evaluations. That makes it genuinely independent execution evidence, not simply a hub of vendor claims. Its catalogue is current through October 22 and identifies active versus archived benchmarks.
vals
+1

However, its pages expose three recurring problems for ValueRank:

Most benchmark tables omit effort.

Model announcement settings do not automatically prove the settings of every later rerun.

Some published scores include server-side fallback models.
vals

6.1 The most useful benchmark designs
Benchmark	Tasks, languages, and agentic setup	Metric and principal controls
Vibe Code Bench v1.1	End-to-end web applications; 50 applications are referenced in the run diagnostics; 20–60 tests per app; modified OpenHands, sandbox services, browser and terminal; up to five hours/1,000 turns	Average app score; a UI test passes when at least 90% of substeps succeed. Browser Use evaluates behavior. Hidden specifications/tests improve resistance, but evaluator reliability matters. 
vals
+1

Code Migration v1.1	120 CLI migrations from 30 repositories across Python/Java/Kotlin/Rust/C++, plus 10 COBOL→Java tasks; fixed Pi harness	Hidden behavioral-test pass rate; source repositories equally weighted, giving CLI/COBOL 75%/25%. Anti-cheat checks reject wrappers, hardcoding, and wrong-language submissions. Not comparable with v1’s mini-SWE-agent results. 
vals

Vibe Code Bench 1–100	50 test scenarios plus 50 validation scenarios; up to ten dependent requests per app; persistent conversation/code; modified OpenHands; ten-hour shared generation budget	Mean fraction of consecutive iterations completed before first failure; every workflow must pass, including selected regressions. Private tests, but browser-agent grading and selective regression coverage remain limitations. 
vals

SWE-bench Multimodal	480 tasks from 11 JavaScript repositories; image-dependent issue repair; fixed mini-SWE-agent; one run	Percentage resolved; screenshots attached before run; no internet; upstream repository tests. Public issue/patch exposure remains a training-time risk. 
vals

ProgramBench	200 public CLI reconstruction tasks; executable plus specification; fixed mini-SWE-agent; 1,000 steps/six hours; offline	Fully Resolved requires all tests; Almost Resolved requires ≥95%; raw test pass rate also reported. Execute-only binary, no decompilers/wrapping. 
vals

IOI v2	18 C++ problems across three contest years; fixed OpenCode; offline; no grader feedback during generation	Official subtask points, averaged across problems/years. Two leaders already score 100%; tiny public task set and potential exposure limit usefulness. 
vals

CyberBench v1.1	60 PoC tasks and 56 patch tasks on OSS-Fuzz-style native-code vulnerabilities; mini-SWE-agent; offline	Crash reproduction and behavior-preserving patches against hardened checks. Distinguish tracks; refusal/fallback handling materially affects results. 
vals

SRE Bench	262 binary-analysis instances from 19 in-house programs; six tasks each, 1,572 total	Fully Solved requires all six; Capability Score is individual-task completion. Clean-room construction offers strong exposure resistance. This is software reverse engineering, not site reliability engineering. 
vals

Terminal-Bench 4.0	66 tasks; fixed mini-SWE-agent; three full runs; eight-hour agent limit; GPU tasks included	Mean of three pass@1 runs, strict verifier success. Independent execution of the same task set already in ValueRank—not a new benchmark dimension. 
vals

For Vibe Code Bench, pin the standalone test roster explicitly: Vals’ index methodology also describes a 22-task VCB subset. A standalone score and index-component score must not be assumed identical.
vals

6.2 Important frontier results

These are published scores, not automatically eligible pure-model observations. “Announcement effort” refers to Vals’ model-level reporting; it still needs to be tied to the particular benchmark run/revision.

Model	Announcement effort	VCB v1.1	Migration v1.1	Multimodal	ProgramBench
GPT-6 Astra	Not verified here	89.59	80.58	43.33	5.50
GPT-6.1 Sol	Not verified here	88.93	77.32	43.54	3.00
GPT-6 Luna	max	81.65	46.67	37.50	0.50
Claude Opus 5.5	max, except specified benchmark exceptions	90.29	81.01	70.21	18.50
Claude Sonnet 5.5	max, except specified benchmark exceptions	92.39	86.88	58.33	6.50
Claude Haiku 5.5	max	90.44	52.36	43.96	2.50
Gemini 4 Argon	high	91.91	70.80	56.04	2.50
MiMo-V2.6-Pro	reasoning enabled; not an AA effort equivalence	85.22	48.79	41.25	0.50
MiMo-V2.6-Flash	reasoning enabled; not an AA effort equivalence	78.96	39.55	—	0.50
DeepSeek V4.1 Flash 1017	Not verified here	87.73	67.52	—	—
MiniMax-M3.1-Flash	max	73.94	—	—	—

Scores come from the current standalone pages; settings come from Vals’ model announcements. A dash means no result observed in that captured table, not zero.
vals
+4

The attached observations enumerate the other roster-related results. In particular, VCB has candidate labels spanning all 37 model names, but it does not provide the corresponding five-effort sweeps for Haiku, Sonnet, and GPT-6.1 Sol.
vals

6.3 Fallbacks are a substantive exact-configuration problem

Vals reports that Opus 5.5 used Opus 5/4.8 fallbacks. In its announcement snapshot:

VCB changes from 90.29% to 83.34% when fallback-assisted tasks count as failures.

SRE Bench changes from 33.59% to 5.34%.

Sonnet 5.5’s SRE result changes from 30.15% to 19.08%.
vals

VCB 1–100 separately reports Fable 5.1 fallback use on 14 of 50 tasks, primarily to Opus 5, with occasional Opus 4.8 turns.
vals

A result completed by another model violates the brief’s pure exact-configuration interpretation unless the configuration explicitly includes that fallback policy. Conversely, “fallback-as-failure” is a conservative alternate score—not necessarily what a complete no-fallback rerun would produce, especially in a persistent multi-iteration task.

6.4 Freshness and capture
Benchmark	Standalone page update
VCB v1.1	October 20
Code Migration v1.1	October 19; catalogue says October 20
VCB 1–100	October 14; catalogue says October 17
SWE-bench Multimodal	October 16
ProgramBench	October 12
IOI v2	October 20
CyberBench v1.1	October 12
SRE Bench	October 14
Terminal-Bench 4.0	October 22

These discrepancies should be recorded, not silently resolved by choosing the fresher date. The pages are extractable HTML tables; I did not verify a documented public result API or complete downloadable run manifest. Updates appear release-driven rather than governed by a published fixed service-level cadence.
vals
+9

There are also internal editorial inconsistencies: ProgramBench’s table credits Opus 5.5 with 37 fully resolved tasks, while nearby prose says only 13 tasks are fully solved by any model. Use run-level artifacts to resolve such conflicts before ingestion.
vals

Disposition: prioritize VCB and Code Migration for evidence completion. Prefer VCB 1–100 as a later maintenance/reliability complement rather than immediately weighting several correlated Vals web-app benchmarks.

7. SWE-bench, SWE-Atlas, and ITBench
SWE-bench Verified and Multilingual

Official SWE-bench distinguishes:

Verified: 500 human-filtered Python issues.

Multilingual: 300 issues from 42 repositories across nine languages.

Multimodal: 480 image-dependent issues.

A default Bash Only Verified comparison using mini-SWE-agent. Scores are percentage resolved, and the official board marks runs performed or directly checked by its team.
swebench

That distinction matters: the general leaderboard includes heterogeneous agents and submissions; “on the official board” does not mean every row was run centrally with the same scaffold.

Vals archived Verified on September 1 because of saturation. Its leading rows are Opus 5 97.0%, DeepSeek V4 Pro 0813 96.4%, and GPT-5.6 Sol 96.2%. It therefore misses the subsequent frontier releases that matter most here. The CSV preserves the captured historical roster rows, but they are not useful coverage for new versions or efforts.
vals

For Multilingual, this audit did not establish a current exact-effort roster manifest. Its attractive language diversity does not overcome that missing evidence.

Disposition: no new Verified leaf; Multilingual remains a coverage-development candidate, not an established addition.

SWE-bench Pro: distinguish original, V2 Full, V2 HARD, and private results

Scale’s V2 refresh contains 642 public tasks across 11 repositories; HARD is a selected 51-task subset. It removes invalid tasks, corrects instruction/test contradictions, locks networking, and regrades patches on pristine images. These controls address real integrity problems, but not training-time memorization. Scale itself notes that near-ceiling public results may reflect exposure and maintains private results for that reason.
scale
+1

The captured current HARD view includes:

Configuration	HARD score
Opus 5, Claude Code, xhigh	98.00
Fable 5.1, Claude Code, high	92.20
Gemini 4 Argon, mini-swe-agent, high	92.16
GPT-6 Astra, Codex, high	90.20
Muse Wonder 1.0, mini-swe-agent, xhigh	90.20
Kimi K3, mini-swe-agent, max	88.20
Sonnet 5, Claude Code, xhigh	88.20
GLM-5.3, mini-swe-agent, max	84.30
GPT-5.6 Sol, Codex, xhigh	82.40
Sonnet 5.5, mini-swe-agent, xhigh	70.59
Gemini 3.8 Flash, mini-swe-agent, high	58.80
Haiku 5.5, mini-swe-agent, high	52.94

The page also distinguishes capped 50-turn runs from other 250-turn runs. Capture the row-specific budget flags. These are not 642-task Full scores.
scale

A secondary mirror reports materially different V2 Full scores; I did not substitute them for the primary HARD view. Original Pro, V2 Full, HARD, private, and provider claims must remain separate datasets.
scale
+2

Disposition: insufficient roster coverage, variable scaffolds/budgets, and public-set saturation. Do not add merely because Pro has a “harder benchmark” reputation.

SWE Atlas Codebase QnA, Scale-run

This measures agentic understanding rather than patching: 124 questions over 11 production repositories in Go, Python, C, and TypeScript. Agents trace execution, run experiments, and answer technical questions. The metric requires satisfying all rubric items, with an LLM judge; tracked source-code modifications fail the task.
scale

Scale uses mini-SWE-agent plus native agents for selected frontier models. It also increased mini-swe-agent’s step allowance from 250 to 500 for newer models in July, so not all historical rows have identical budgets. Current observed roster-related results include Opus 5 xhigh 63.17, Fable 5.1 xhigh 59.95, Astra xhigh 59.14, Opus 4.8 xhigh 57.26, GPT-5.6 Sol xhigh 46.00, and GPT-5.5 xhigh 45.43. The captured board does not supply broad coverage of the newest effort variants.
scale

Its public dataset, rubric judging, scaffold variation, and historical budget change are the main qualifications. The “copyleft therefore contamination-resistant” argument is a risk-reduction claim, not proof that training exposure did not occur.

SWE-Atlas-QnA-AA

AA’s current methodology makes this a distinct grading revision:

Same 124 tasks.

1,306 rubric criteria, including 127 reworded criteria.

GPT-6 Luna xhigh judge, five votes per criterion.

Three attempts per task.

Binary task resolution; tracked-file changes fail.

Dataset and judge configuration published on Hugging Face.
artificialanalysis

It is an excellent construct complement, but not independent execution from AA. Moreover, the captured AA agent leaderboard still displayed v1.5/old QnA text while its methodology described v2.0/QnA-AA. Old QnA values must not be imported under the new grading identity.
artificialanalysis
+1

Disposition: first AA benchmark to verify for a possible 5-point leaf; no claim of complete coverage until the v2.0 exact-row manifest is captured.

ITBench-AA and actual DevOps coverage

ITBench-AA is directly relevant to DevOps: 59 Kubernetes root-cause-analysis incidents, comprising 40 public and 19 private tasks, each repeated three times. A Stirrup agent inspects offline alerts, metrics, traces, events, and topology and writes a JSON diagnosis. The score is precision only when recall is complete; otherwise zero. It is diagnosis from snapshots, not live-cluster remediation.
artificialanalysis

The captured primary text explicitly exposes GPT-5.6 Sol max 56.2% and Gemini 3.8 Flash high 52.5%; the chart advertises 45 models, but its full exact-configuration rows were not extractable here. A secondary 14-row mirror is not a substitute for that manifest.
artificialanalysis
+1

IBM’s upstream ITBench spans SRE, FinOps, and CISO scenarios and has an open repository/leaderboard ecosystem, but those results are not interchangeable with AA’s offline 59-task implementation.
artificialanalysis
+1

Disposition: best conceptual DevOps addition, but exact cohort coverage remains unestablished and AA dependence remains.

8. Other named candidates: screened out on current evidence
Candidate	Measures, count, metric	Runner/harness/data and freshness	Why not a leaf now
Aider Polyglot	225 Exercism exercises across C++, Go, Java, JavaScript, Python, Rust; editing with test-feedback repair; headline percent correct after allowed repair, not single-shot pass@1	Owner board exposes commands, effort, edit format, dates, commits, and detailed run statistics. Captured leading rows are 2025-era GPT-5/o3/Gemini 2.5. Harness version/edit format vary. Public exercises create exposure risk. 
aider
+1
	No current roster results established; transparent metadata does not solve stale coverage
LiveCodeBench	Fresh contest programming, plus repair/execution/output-prediction scenarios; pass@1; count depends on selected window	Owner board captured 454 problems for August 2024–May 2025, led by o4-mini/o3-era models. Submission PRs are accepted; not every row is necessarily centrally run. Public dated problems permit post-cutoff windows, but an old window is not clean for a new model. 
livecodebench
+1
	No current roster coverage established; Vals also archives its implementation
SWE-Lancer	More than 1,400 real freelance tasks, including implementation and management decisions; dollar-value/task-success interpretations require split-specific care	Captured secondary board has four older models, not this cohort. Current primary effort/run manifest not established. 
llm-stats
	Insufficient current evidence; do not pool vendor launch claims
SWE-PolyBench	2,110 repository issues in Java, JavaScript, TypeScript, Python; percentage resolved	Owner page shows older Aider-PB/SWE-agent-PB results; public data/code. Separate Verified split exists and must not be merged with Full. 
amazon-science
+1
	No current roster effort coverage established
Multi-SWE-bench	1,632 multilingual repository issues; percentage resolved	Owner page exposes dated agent/model rows, logs/trajectories where available; captured leaders are 2025 Gemini 2.5/Claude 3.7 runs. 
multi-swe-bench
	Stale observed coverage; provider-reported modern numbers are not standardized replacements
KernelBench	PyTorch→CUDA/DSL optimization; base levels contain 100+100+50 problems, with an additional full-model level; fast_p requires correctness and speedup above threshold 
𝑝
p	Open toolkit, not a centrally validated universal model board. GPU, precision, PyTorch baseline, DSL, iteration budget, and scaffold matter. Owner explicitly disclaims validation of individual reported kernels/results. 
github
	No standardized current 51-configuration dataset; specialized workload and hardware confounding
CodeClash	Competitive goal-directed coding across six arenas; Elo; published study reports eight models and 1,680 tournaments of 15 rounds	Owner leaderboard last says November 3, 2025; a later CC:Ladder variant exists. Tournament composition affects Elo; public game solutions may be exposed. 
codeclash
+2
	No current roster coverage; not directly comparable with pass-rate leaves
METR time horizons	Software/ML/cybersecurity tasks; fitted human-task duration at 50% or 80% model success, not an ordinary accuracy percentage	Raw data and analysis code linked. Scaffold elicited per model; six runs/task. Last updated September 8, 2026 and explicitly no longer actively maintained; last listed model additions are much older than this frontier roster. Estimates above 16 hours flagged unreliable. 
metr
	Coverage failure, model-specific elicitation, and different metric requiring an owner-approved transform

For these candidates, “last crawled October 2026” on an aggregator is not evidence of an October 2026 evaluation. Where the primary site did not state a dependable latest evaluation date or cadence, I have left it unresolved rather than inferring freshness.

9. Recommended weighting under O36

All weights below are percentage points of total quality, preserving the 60% SWE allocation.

Policy A: preserve O36 and the existing cohort

For the current release:

Leaf	Weight
FrontierCode 1.1, AA	25
Terminal-Bench 4.0, AA	20
Bug Hunt Bench	15
Additional benchmark leaves	0

Publish the new evidence as diagnostics. This is the only recommendation supported without changing the owner’s missing-leaf policy or establishing additional exact-configuration results.

“Nearly every configuration” is not itself an O36 exception: if even two configurations lack a new mandatory leaf, those two become unrankable unless the owner approves a specific alternative.

Policy B: add independent benchmarks after completing coverage

My preferred future allocation is:

Leaf	Conditional weight
FrontierCode 1.1	20
Terminal-Bench 4.0	15
Bug Hunt Bench	15
Vibe Code Bench v1.1	5
Code Migration v1.1 or AI Coding Daily	5
Total	60

Choose Code Migration for language-porting breadth and a fixed scaffold; choose AI Coding Daily for realistic maintenance/code-quality evidence and explicit effort comparisons. Do not automatically include both merely to increase the benchmark count.

VCB has the best apparent version breadth; Migration has a clean complementary construct; AI Coding Daily has unusually useful explicit effort labels but substantial effort gaps. Those are reasons to prioritize evidence collection—not reasons to waive it.
aicodingdaily
+2

Policy C: a pooled SWE leaf

A fixed 10-point independent pool could replace five points each from FrontierCode and Terminal-Bench:

𝑃
𝑐
=
∑
𝑏
𝛼
𝑏
𝑠
𝑐
,
𝑏
,
∑
𝑏
𝛼
𝑏
=
1.
P
c
	​

=
b
∑
	​

α
b
	​

s
c,b
	​

,
b
∑
	​

α
b
	​

=1.

Under unchanged O36, every configuration must have every constituent required by this fixed pool. Pooling does not solve missingness by itself.

An available-results pool,

𝑃
𝑐
=
∑
𝑏
∈
𝐴
𝑐
𝛼
𝑏
𝑠
𝑐
,
𝑏
∑
𝑏
∈
𝐴
𝑐
𝛼
𝑏
,
P
c
	​

=
∑
b∈A
c
	​

	​

α
b
	​

∑
b∈A
c
	​

	​

α
b
	​

s
c,b
	​

	​

,

does avoid requiring every constituent—but different configurations are then scored on different workloads. It requires an explicit owner decision accepting variable effective weights. It can also leave low-effort configurations uncovered if none of the independent sources tests them.

I would not recommend that variable pool as the headline default. If accepted, register at minimum:

A fixed source universe and weights.

Exact-version/effort matching with no nearest-effort substitution.

Explicit missingness and minimum-coverage rules.

Per-row effective weights.

A deterministic choice among alternate harness results.

A fallback policy.

A common-benchmark sensitivity comparison.

Policy D: prioritize a new capability rather than independence

If the owner prefers broader task coverage while retaining AA as the primary evaluator, investigate a 5-point SWE-Atlas-QnA-AA leaf first. ITBench-AA is the next choice for explicit Kubernetes operations relevance.

Neither should receive weight until the current exact-configuration result manifest is validated; the sources captured here do not establish full coverage. Their conceptual fit is strong, but they do not reduce AA concentration.
artificialanalysis
+1

10. Concrete admission checklist

Before promoting any candidate from diagnostic to weighted leaf, obtain a manifest with one row per required configuration containing:

AA identity and immutable provider model/version identifier.

Actual reasoning-effort parameter, including whether “default” is explicit.

Benchmark release, task split/count, scoring metric, and normalization.

Runner identity and whether the row is owner-run, checked, vendor-submitted, or self-reported.

Harness version, system prompt/tool configuration, limits, and network policy.

Attempt count, evaluation date, source artifact, and capture timestamp.

Refusal, fallback, retry, and integrity-review treatment.

Exact score plus uncertainty or per-task outcomes where available.

The immediate evidence requests should go to Vals for VCB effort sweeps/no-fallback provenance, AI Coding Daily for its missing effort variants and pinned scoring schema, LiveBench for a reconciled current release/configuration export, and AA for the regraded QnA-AA/ITBench exact-row manifests. Those requests target the actual blocker: coverage of the configurations ValueRank ranks, rather than another long list of benchmark names.