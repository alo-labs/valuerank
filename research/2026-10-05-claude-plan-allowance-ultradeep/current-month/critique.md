# Adversarial critique and refinement record

The Ultradeep package uses three manual critique passes, matching the configured maximum of three cycles. The slash command itself was not invoked. Findings were written down as claim-level deltas and addressed by narrowing claims, retrieving the missing recent posts, or documenting a blocker.

## Cycle 1 — Skeptical practitioner

```json
{"delta_type":"unsupported_inference","claim_id":"C-C02","description":"Early draft treated plan labels and current meter reports too loosely; dollar pricing can invite inference of Pro tier and unmatched tasks can look like evidence of a reduction.","severity":"high","loopback":true,"repair":"Preserved exact plan language, including '$20 plan btw' and 'not stated'; qualified unmatched comparisons and rejected averaging."}
```

```json
{"delta_type":"missing_source_class","claim_id":"C-C02","description":"The first draft omitted newly found October 1, October 5, and September 23 Reddit reports and lacked one account-reset report's precise publication date.","severity":"medium","loopback":true,"repair":"Added S-C16 through S-C20 with exact/available post dates, exact plan wording, observation caveats, and inline source IDs."}
```

## Cycle 2 — Adversarial evidence reviewer

```json
{"delta_type":"unsupported_inference","claim_id":"C-C02","description":"S10's full-week account totals and separate post-reset partial window were conflated; S12's historical 23 August comparator could leak into a current estimate.","severity":"high","loopback":true,"repair":"Expanded E-C05 with exact publication and full/partial observation windows, complete reported counts, pricing method, and caveats. Split S12's 22 September current point (E-C12) from its 23 August excluded comparator (E-C22)."}
```

```json
{"delta_type":"missing_source_class","claim_id":"C-C06","description":"The September 23 Console-credit event concerns API billing/routing, not subscription allowance, and was not represented in the first ledger.","severity":"medium","loopback":true,"repair":"Added S-C21/E-C19 as an incident-only source and excluded it from allowance synthesis."}
```

## Cycle 3 — Red-team and implementation engineer

```json
{"delta_type":"decision_risk","claim_id":"C-C02","description":"A research package could be misapplied to claim that ValueRank's shared Claude Opus 5.5 40x route currently works at the reported rate; the package contains no exact-route controlled evidence.","severity":"high","loopback":true,"repair":"Added explicit exact-model route limitation and excluded the unrelated 1-15 October Artifacts promotion."}
```

```json
{"delta_type":"decision_risk","claim_id":"C-C07","description":"The required SB workflow and validator execution status were described too generally; that could imply the slash command or formal gates ran.","severity":"medium","loopback":true,"repair":"Loaded the Silver Bullet workflow contract via LeanCTX and documented the phase artifacts. The slash command was not invoked; each formal validator's actual result is recorded in validation/ and the manifest."}
```

## Loopback and residual risk

The loopbacks repaired dates, tier labels, evidence mappings, S10/S12 intervals, the unrelated promotion scope, and workflow status. The final measurement-window pass applies the Sep6–Oct6 start-date cutoff, excludes S-C03/S-C04 pre-window intervals, preserves the eligible partial estimates including the explicit $2,350 Max20x week projection, and excludes provider claims and S-C05's non-isolatable $12,751 aggregate from per-plan numerators. A separate blocker remains for ValueRank route applicability: no controlled current Opus 5.5 40x shared-route evidence exists here. Resolving that requires a live, controlled route observation, not more general Reddit search. Search coverage remains bounded and community reports remain nonrepresentative.
