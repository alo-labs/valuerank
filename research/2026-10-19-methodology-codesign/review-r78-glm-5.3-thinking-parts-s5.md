Both parts are read. Before writing the review, I'm doing one targeted web check on the claim these parts lean on for exempting ChatGPT transfers from bracketing (that Codex subscription credits are priced per model at API parity), since it's a factual pricing claim that drives a whole exemption family.
0. Read check

Part 5 (draft-r160-part-5-of-14.md) — read to its end.

First line:

Report window (E194, O32, E201a): the report window is the closed day interval [V − 30 days, V], compared as UTC calendar dates (date(V) − 30 days ≤ d ≤ date(V), with a timestamped E194 date truncated to its UTC date; reports are recorded by date, not time, so for the report window E213's cutoff is V's UTC date, whole: a report dated that day counts whatever its hour), both end days included, so the window spans 31 calendar dates (a report dated exactly 30 days before the cutoff is in, one dated 31 days before is out), published as the registry's reporting window, which is AGENTS.md's "preceding month".

Last 12 words: "(no provider marketing quotas otherwise; end-user API-priced reports or SemiAnalysis controlled measurements)."

Part 6 (draft-r160-part-6-of-14.md) — read to its end.

First line:

Assumptions: only the owner-named model-to-model transfers (Opus 5.5's measured Claude multiples to other Claude models; the GPT rule of O45) and the owner's MiMo quota ceilings (O46) stay in the official Plan ranking, labelled, a transfer with its donor measurement identified; neither identifies M_W.

Last 12 words: "best value; no epsilon is introduced. Domain validity is separate from evidence completeness."

1. Findings by severity

Critical

None.

High

H1 — O144's ChatGPT bracket exemption rests on an unrecorded, un-checked parity premise. Part 6 exempts all ChatGPT transfers from route brackets on the single sentence "Codex credits are priced per model at API parity," with no registry object, capture date, build check, or change-detection hook — unlike every neighbouring claim in these parts (the O46 MiMo ceilings, by contrast, get a recomputation tolerance of 5 × 10⁻⁵ and E261 rate captures). This hurts the objective because every non-Sol/Astra GPT row's Plan score is a labelled lower-of transfer (O45), and brackets exist precisely to bound that assumption's error; exempting the largest transfer family removes the published bound exactly where the ranking is most assumption-driven. The premise is publicly corroborated today — OpenAI's meter prices Codex models in credits per million tokens, and the credit rate card runs at a uniform 25 credits per dollar against API list prices (GPT-6.1 Terra $1/$5 → 25/125; GPT-6 Astra $10/$50 → 250/1,250) — but it is fragile: separately purchased Codex-only credits have run about 37% above API rates, some public sources state there is no public dollar price per credit, and OpenAI reserves the right to price credits differently by plan, region or contract. Recommendation: add a registry object (e.g., evidencePolicy.modelCreditRates) holding the per-model credit rate card with captures dated ≤ 7 days at V (E216-style, build-checked), a parity test comparing credit-rate ratios to the API price-list ratios within a stated tolerance, and typed change detection on per-model credit rates (O83/O99 currently key only to plan-level limits and prices); bracket GPT transfers whenever parity fails the check.
justinmckelvey
+3

Medium

M1 — an announced future change to the ChatGPT meter is not captured. OpenAI has been reported (2026-10-31, one day before the 2026-11-01T06:10Z cutoff) as unifying ChatGPT and Codex allocations from December 2026 into one shared credit pool measured in credits per million tokens, with plan limits still differing. If OpenAI itself announced this before the cutoff, it is a provider announcement of an allocation change that O77 arguably triggers, and it changes the shared-meter structure (O79-style: chat usage will compete with Codex usage on every affected plan), which will invalidate cross-product utilisation assumptions at the next release. Why it hurts: change detection as drafted records only implemented changes, so a dated, announced structural change to the meter of the Plan ranking's largest provider would enter the registry only after it breaks measurements. Recommendation: verify the announcement date against the cutoff; record announced-but-not-yet-effective changes as typed registry entries with effective dates (a futureChange flag), and state in the release whether any current route's regime ends on a known date.
diariobitcoin

M2 — cache writes are excluded from the O144/O146 bracket token mix. The bracket ratio r uses "the registry's shared token mix (cache writes excluded)," but cache writes are metered consumption priced at model-specific multipliers (E131 lists them as a category; E157 prices them per tariff), and they are a large share of coding workloads. Donor/target cache-write price ratios can diverge from the rest of the mix, so the published bracket can understate the transfer error precisely on the coding-heavy usage the basket measures. Recommendation: compute per-category ratios r_k over all five categories (cache writes included) and publish a second, wider bracket [M · min_k min(1, r_k), M · max_k max(1, r_k)] beside the shared-mix bracket; keep the shared-mix bracket as the headline sensitivity.

M3 — the O71 staged search cannot reach the primary venues for end-user reports. Part 5's search log discloses that reddit.com (mirrors only), X, Zhihu, LINUX DO search, GitHub search and YouTube video pages were unreachable from the build environment — these are the main venues where the ≥2 concordant end-user reports O71 exists to find would surface. The disclosure is honest, but there is no mitigation protocol or coverage gate, so the measured-evidence pathway that O71/O72 were adopted to build is structurally starved and Plan rows keep resting on owner-authorised assumptions. Recommendation: define per-venue retrieval protocols that work from the build environment (Reddit's public JSON endpoints, the archive mirrors already in use, GitHub search via the API rather than the web UI, YouTube transcript endpoints), publish a per-venue coverage status with each release's search log, and escalate to an owner review when a venue is unreachable across consecutive releases.

M4 — Owner decision challenge (O74/O81): provisional reports can veto a cell and shift its value. An inferred tier or model version counts provisionally, enters the range test, and (under O115) widens the clip band, while being unable to admit a route. A provisional report whose inference is wrong may not belong to the cell at all, yet it can fail the concordance of a cell two solid reports would admit, and it moves the admitted value through the band. This is a new argument against strict all-reports concordance, distinct from the rejected robust-core figure: the problem is evidence scoping, not outlier trimming. Recommendation: before a provisional report can fail a cell, require its inference basis to be re-verified against the cell's non-provisional reports (logged, build-checked); compute the O115 clip band over non-provisional reports only, publishing the all-reports band as a diagnostic.

Low

L1 — singleProvider mark is a misnomer. The 2026-10-31 supplementary search named GPT-6.1 Terra (OpenAI) and Gemini 4 Carbon (Google) — two providers — yet must carry the singleProvider mark to avoid moving the search cutoff; the mark's real semantics is "narrower than all-provider." Rename it (e.g., narrow) or define it in the registry as such, so the build's cutoff logic reads correctly.

L2 — a cross-reference points the wrong way. Part 5 says the flagged GPT routes are "dated in the list below," but the flagged-measurements list (ChatGPT Plus/Pro 100/200/500 for Astra and Sol) appears earlier in the same section. Point the reference at the list above or name the artifact (e.g., scores.json planRows) that carries the dates.

2. Methodology design recommendations

Model-credit-rate registry with a parity gate (fixes H1). evidencePolicy.modelCreditRates: per model, per plan family, the credit cost per 1M tokens by category, captured ≤ 7 days at V; a build check that each model's credit-to-dollar ratio equals its API price within a stored tolerance (mirroring the O46 5 × 10⁻⁵ recomputation rule); GPT transfers bracketed automatically whenever the check fails; a typed change record when a model's credit rate changes, flagging only that model's routes. All inputs are public (OpenAI's rate card and API price list) and refreshable each release.

Category-complete brackets (fixes M2). For each transfer, publish two brackets: the current shared-mix r, and the category-extreme bracket [M · min_k min(1, r_k), M · max_k max(1, r_k)] over the five E131 categories including cache writes. This also covers donor/target mix differences (a reasoning-heavy target), which the shared-mix ratio ignores. Implementable from the same registry prices already captured under E157/E176.

Future-dated announced changes as typed records (fixes M1). Extend the change register with effectiveDate and a futureChange flag; O77/O83 machinery then picks them up on their effective release, and the release summary states which routes' meter regime has a known end date.

Venue-coverage protocol for the staged search (fixes M3). A per-venue retrieval method table (JSON API, archive mirror, transcript endpoint) with a coverage status in the search log; a build note when a venue holding prior cohort evidence (e.g., the claude-code issue used for the 2026-10-17 meter change) is unreachable two releases running.

Provisional-report scoping rule (fixes M4). Inference re-verification before veto power; clip band from non-provisional reports only, with the all-reports band published.

Conditional on Q1: an exchange-rate-matched variant of the E164 calibration diagnostic, holding the official ln(c_H/c_L) fixed and swapping only the anchor rows, to separate assumption effects from exchange-rate effects.

3. Questions for the owner

Do the official Plan anchors use the same c_L = cheapest/2, c_H = dearest×2 padding that E164 applies to the measured-only diagnostic anchors? If not, the calibration diagnostic conflates assumption removal with an exchange-rate change, and I would recommend the matched variant in recommendation 6.

Was OpenAI's reported December 2026 unification of the ChatGPT and Codex allocations announced through a first-party channel before the 2026-11-01T06:10Z cutoff, and if so, why is it absent from the typed change list?
diariobitcoin

Is the per-model Codex credit rate card recorded anywhere in the registry today (e.g., under evidencePolicy.meterDenominations), and is it build-checked? If yes, H1 narrows to adding the parity test and the per-model change hook.

4. Verdict

VERDICT: HAS FEEDBACK