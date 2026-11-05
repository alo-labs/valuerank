# DR-CRITIQUE — adversarial review (deep mode: 2 cycles)

Angles per cycle: steelman, contradiction hunt, missing stakeholder, failure mode. Personas: cycle 1 "Skeptical
Practitioner", cycle 2 "Adversarial Reviewer". Claim ids refer to report sections (claims.jsonl is regenerated after
refine). The stopping rule is no remaining `high` delta or 2 cycles.

## Cycle 1 — Skeptical Practitioner

```json
[
 {"delta_type":"unsupported_inference","claim_id":"finding_1:K45SLE-range","description":"The Pro verdict leans on K45SLE's whole-percent range ($210-300). The batch moved the weekly meter only 4 points, so quantisation error is +/-12-25%. A practitioner would ask whether the cell also fails at the point value. It does: without #124, 321 / 262.5 = 1.22. The report must say so explicitly so the verdict does not look like an artefact of range handling.","severity":"medium","loopback":false},
 {"delta_type":"unsupported_inference","claim_id":"finding_2:leaflava-challenge","description":"The challenge assumes Opus output shares of 16.5-22.8%. Max-effort runs with many short-lived agents could have a higher output share. Steelman: even at a 50% output share the run is $1,200 and the week about $1,714. Only an output share near 75% reproduces $800, which no full Claude Code ledger shows. Add this sensitivity; the ruling stays 'challenged, indicative only'.","severity":"medium","loopback":false},
 {"delta_type":"missing_source_class","claim_id":"limitations:youtube-x","description":"YouTube (bot check) and X (HTTP 402) were unreachable. Candidate videos with likely numbers: Binh Dad of 3 Monkeys (Max 20x test 4 days ago; Max 5x '$987 of Claude at API prices' last week), Iris Ludd ('ran 29 real coding jobs on GPT-6.1 Sol and GPT-6 Astra' on the $200 Codex plan, which is the only lead for Pro $200 new 10x), Receipts Please, TreeCityWes. Companion write-ups were searched and not found. Record these as owner-actionable leads in handoff.md.","severity":"medium","loopback":true},
 {"delta_type":"decision_risk","claim_id":"finding_5:kimi-cn","description":"Treating CN legacy Kimi fits (MoonDrinker $48.6/week against Astralyn $55.9/week, 1.15x) as reference only could hide a passing pair. It is not a cohort cell: the CN and USD pages publish different multipliers, so stage 2's rule 7 holds. Keep it as reference and say explicitly that the pair would pass if ValueRank ever lists legacy Allegretto.","severity":"low","loopback":false}
]
```

Loopback (cycle 1): delta-queries for the YouTube leads (companion pages, the channels' blogs, web search on video
titles) found nothing extractable within the time box. The Iris Ludd search returned no companion page. The gap is
recorded, not resolved.

## Cycle 2 — Adversarial Reviewer

```json
[
 {"delta_type":"contradiction","claim_id":"executive_summary:four-measurers","description":"'Four public measurers corroborate a tightening around 10-17' overstates the evidence. Randomblock1 is model-unstated and his week straddles the split. push42 (Max 5x) attributes his window-to-week ratio change to 'the promotion has ended', which may refer to a different, earlier change. Rephrase: two direct per-token measurements (NicoAica, kakki-1), plus Randomblock1's and push42's consistent but weaker observations.","severity":"high","loopback":false},
 {"delta_type":"contradiction","claim_id":"finding_3:dhadaptive-pro500","description":"Provider-originated evidence missed by stages 1-2: an OpenAI support e-mail, quoted by Vanja Petreski, says 'an error prevented your weekly Codex and Work usage allowance from increasing' on Pro 200 -> Pro 500 upgrades, 'Your account kept the allowance from your previous plan', and 'We corrected the error on October 16.' DhAdaptive's Pro $500 figure (std-eq $919-964/week, 0.90-0.95x of his 20x figure) was measured on 10-09, the day of his upgrade, inside the error period, and matches the error's signature. Under eligibility condition 5 (no provider-acknowledged accounting fault) it must be excluded. GPT-6.1 Sol on Pro $500 then has no eligible report. totorofly's Pro $500 Astra report (10-11) must be flagged, since his upgrade history is unknown.","severity":"high","loopback":true},
 {"delta_type":"unsupported_inference","claim_id":"introduction:*","description":"Introduction and methodology sentences that state O11 and the stage-2 rules have no linked evidence (verify_claim_support: unsupported). Link them to evidence rows drawn from the stage files (O71 README, stage-2 report), registered as local documentation sources.","severity":"medium","loopback":false},
 {"delta_type":"missing_stakeholder","claim_id":"synthesis","description":"Provider perspectives are thin: no Anthropic or Google statement exists, and the only OpenAI items are Sottiaux's tracker posts and the support e-mail. The report should state that the Claude split remains user-evidenced and that asking the providers directly is the highest-value next step.","severity":"low","loopback":false},
 {"delta_type":"decision_risk","claim_id":"finding_2:nicoaica-p1","description":"NicoAica's own pre-split value ($1,294-1,681, 10-15..17) is already far below the Kanttz/Theo cluster. Either the change began before 10-17, or accounts differ (SemiAnalysis's per-account A/B finding explains at most about 20%). The 10-17 split point is therefore uncertain. This does not change the verdict, since both partitions fail.","severity":"medium","loopback":false}
]
```

Loopback (cycle 2): one targeted delta-query on the OpenAI upgrade-entitlement admission found the Vanja Petreski post
(vanja.io), which quotes the support e-mail verbatim. Its scope (how many accounts) is unverified. A Reddit post of
2026-10-20 (r/codex 1xay01g) shows a screenshot of a similar admission. The finding is incorporated in DR-REFINE.

## Stopping decision
After cycle 2, both `high` deltas have concrete repairs (rephrasing; exclusion with the provider evidence cited) and no
open high-severity delta remains after refine. Max cycles reached (2). Residual risks are carried to decision-record.md:
the user-evidenced Claude split, the unreachable YouTube/X channels, and the credibility class of the evidence.
