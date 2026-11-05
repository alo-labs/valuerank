subscription fee plus declared additional cash, F_gross) and the selected multiple's API-priced amount M × F_gross so light users can judge fit, typed by the selected measurement object (E166): amount_kind measured-workload capacity / observed eligible consumption, capacity not established / assumed API-equivalent consumption (owner-named transfer, donor named) / API-equivalent consumption measured on the same model at another effort (O88, O90, donor named) / identified target-workload capacity (bound to W) / provider quota ceiling, the full quota at API rates (O46, full use assumed), with the capacity status (E139), valuation status (E138) and an interpretation label generated from those fields; API-fallback rows print no Plan amount, and the amount is never called capacity unless the measurement establishes it. Amount lineage (E168): every amount records amount_target (measured-workload consumption / measured-workload capacity / assumed consumption / target-workload capacity / full-quota consumption for an O46 ceiling; an O88 same-model route, graded measured under O90, records measured-workload consumption, its donor's target), workload_id, measurement_object_id, capacity_solution_id, cash_object_id, purchase_policy_id and derivation (direct observation / solver projection / authorised assumption, a donor's measured multiple / same-model measurement, the multiple measured at another effort (O88, O90) / quota ceiling, the tier's credits at the provider's API rate / valid multiplication). M × F reproduces an amount only within one object: the measurement record U_obs = M_obs × F_obs, or fixed positive cash U_W* = M_W × F_0. A target-workload capacity is the capacity solver's U_W* (bounds are the projections of the joint solution set, never products of separately projected multiple and cash endpoints; the displayed lower-bound multiple is a scoring convention), and is never the displayed multiple times cash from another object; when the target solution's cash lineage is not established, the measured amount stays publishable and no target capacity is manufactured (fixtures: fixed cash reproduces target capacity; consumption-dependent cash rejects cross-object multiplication; set identification by projection; missing target cash lineage)."

Wait! Look at the typing of amount_kind vs amount_target in E166 and E168:
In E166:
amount_kind:

measured-workload capacity

observed eligible consumption, capacity not established

assumed API-equivalent consumption (owner-named transfer, donor named)

API-equivalent consumption measured on the same model at another effort (O88, O90, donor named)

identified target-workload capacity (bound to W)

provider quota ceiling, the full quota at API rates (O46, full use assumed)

In E168:
amount_target:

measured-workload consumption

measured-workload capacity

assumed consumption

target-workload capacity

full-quota consumption for an O46 ceiling

Notice that in E166, the second kind is called "observed eligible consumption, capacity not established", but in E168, the target is called "measured-workload consumption".
And for O88, E168 says: "an O88 same-model route, graded measured under O90, records measured-workload consumption, its donor's target".
While E166 has a dedicated amount_kind ("API-equivalent consumption measured on the same model at another effort (O88, O90, donor named)").
That distinction is well-defined: amount_kind is the external reporting taxonomy, and amount_target is the internal derivation target.

Now let's check:
Look at Valuation-basis gate (E170 / O29) in Part 14:
Let's read again:
"A compatibility join of each observation's basis with the price records in force at V (E141) returns exactly one of four outcomes:
(1) compatible as captured;
(2) compatible after evidenced revaluation, which is exact only when every priced category and band with positive demand in the component moves by one common factor k (then C' = k·C for any demand mix; a category has zero demand only where a published category total shows it) or when E157's valuation sufficiency supplies the component's demand by category and band;
(3) AA's applied price not in force at V (O29): the row keeps AA's cost at the price AA applied, flagged "AA cost at superseded price" ... it earns no interval label of its own and competes in other rows' interval outputs over the hull of its published record and its current-tariff bound below, so it can block but never enable another row's label; its scenario outputs use its published record and carry the flag; it is never a reference in anchor derivation (E160) or in the measured-evidence calibration (E164); and its Plan cost divides only by a multiple valued on the same basis (E138's statuses are evaluated against the row's basis: an exact measurement valued at the new tariff is revalued to the row's basis under outcome 2 or is diagnostic-only; an owner-named transfer or an O88 same-model route needs a donor measurement valued on price records in force during the applied price's effective dates; when no route survives, the row falls back to API cost, flagged, O13)...
(4) Valuation basis unverified (E202): AA's cost reconciles with neither its displayed prices nor a registered price record, or AA displays no complete price vector. The row is flagged and stays ranked. It is anchor-ineligible and never earns a label. Competes at its published record (E222): when it has FullCost on W, it enters R_W at its published point (cost and quality bounds, no tariff hull) with its interval box marked label-denied, so it can deny another row a confirmed label but never receives one; like a blocker's, its own frontier and bar statuses read "withheld"."

Wait! Look at how Outcome (3) and Outcome (4) treat anchor derivation and labels:
In Outcome (3):

Row is flagged "AA cost at superseded price"

Stays ranked

Earns no interval label of its own

Competes in other rows' interval outputs as a blocker over the hull of its published record and its current-tariff bound

Never a reference in anchor derivation (E160)

Plan cost divides only by a multiple valued on the same basis

In Outcome (4):

Row is flagged "valuation basis unverified"

Stays ranked

Anchor-ineligible

Never earns a label

Competes at published record (E222) if it has FullCost on W, with interval box marked label-denied, so it can deny another row a label but never receives one.

Now, look at what happens in Outcome (3) when a Plan measurement is valued at a new tariff:
"its Plan cost divides only by a multiple valued on the same basis (E1