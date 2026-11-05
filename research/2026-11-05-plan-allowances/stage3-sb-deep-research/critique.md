# Critique (DR-CRITIQUE): two adversarial cycles (mode deep)

Method per `reference/adversarial-review.md`: attack the strongest claims, record the loopback decision, repair or downgrade.

## Cycle 1

| # | Attack | Finding | Disposition |
|---|---|---|---|
| 1 | GitHub comment text came through a summarising fetch tool, so quotes may be altered | The Oleg-125 comment was read twice through the tool with different prompts and matches the independent stage-2 rendering word for word on "67% of the 5h allowance consumed" and the telemetry line | Keep; record in Limitations that no byte-exact copy of GitHub pages exists |
| 2 | Is "Faheem_Anis1 = Ultimitehand" an over-reach? | Texts and numbers are identical, but different accounts on two sites. They could be one person or one copying the other | Reworded as "one observation" (the measurement is single either way); identity not asserted |
| 3 | The Google quota-raise date rests on one blog | Docs and the Google staff reply show no change; the 1.42 ratio could come from different accounts or pools | Downgraded to "candidate, not a confirmed split"; added the alternative explanation |
| 4 | The Kimi "no doubling" finding uses the same author's fit | Astralyn's retest is a primary API-reading calibration, but the same person produced the original fit, and the Reddit doubling claim is untiered and may concern the new subscription system | Scoped to the legacy Allegretto plan only; added to Limitations |
| 5 | x2v: list-priced "$26-33" hides a mix dependency and a cache-write TTL choice | Rows rise from $26.2 to $32.7 per 5-hour window as cache reads grow; $8 write price assumed | Reported as a range; sensitivity noted; labelled provisional |
| 6 | Reclassifying sergiokapone from "no" (stage 2) to "provisional" | Haiku 4.5 (22 requests, about 13k output) and one Sonnet 5.5 request are small, but the rule says mixed use stays at plan level | Kept as provisional and not counted toward any Opus 5.5 cell; flagged as a proposal, not a record change |
| 7 | Did the sweep miss non-English or video sources? | Zhihu, YouTube, Bluesky and X search were not run; r/ChatGPTPro was not swept | Recorded as gaps |

Loopback decision: repair and rerun validation (no new retrieval required).

## Cycle 2 (after repairs)

| # | Attack | Finding | Disposition |
|---|---|---|---|
| 8 | The O11 margin test on Plus x Sol x 5h passes only if jitendersingh0411 is treated as one range | His two readings are $7.5 and $2.9; counted as two points, 7.41 > 1.2 x 3.69 = 4.43 and the cell would fail | Stated in the decision record as a risk; the stage 1 and 2 convention (one observer, one range) is kept |
| 9 | Do the after-cutoff Claude tests contradict the in-window ones? | douflou Max 5x interactive $204 per 5h sits above Fuduntu $158 and rbartoli $155-169; Ultra $1,560-3,087 spans Coriatel $808 | Not contradictions for the same window; reported as instability evidence and queued, not counted |
| 10 | Entrypoint evidence for Anthropic reports in the window is absent | jbdamask, deepfoundationdesign and Coriatel do not state it; headless could understate by 1.14-1.95x | Added as a caveat on each row and a recommendation to store an entrypoint field |
| 11 | Pro 5h dispersion hides a possible Anthropic metering change | sergiokapone (10-27) to smaug42 (11-02) differs by 14x | Left unresolved; flagged to the O167 freshness check |
| 12 | Any unsupported factual claims? | See `validation/verify_claim_support.log` | Repairs applied where partial |

Gap thresholds: no blocking gaps. Remaining gaps (X search, Zhihu, YouTube, unread GitHub comment threads, locdd identity) are recorded in `handoff.md`.
