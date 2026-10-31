# DR-CRITIQUE: adversarial review (deep mode, 2 cycles)

Each cycle covers four angles: steelman, contradiction hunt, missing stakeholder, failure mode. Personas: cycle 1 is the "Skeptical Practitioner" and cycle 2 the "Adversarial Reviewer". Stopping rule: stop when no `high` delta remains or after 2 cycles.

## Cycle 1: Skeptical Practitioner

```json
[
 {"delta_type":"unsupported_inference","claim_id":"finding_1:SouthWindKnows-pricing","description":"The $4.70 comes from the reporter's own usage tool, and the tool does not show the per-model split of input and output. Stage 2 rejected ayudha90 for an undisclosed pricing basis. The difference here is that tokens, cache share and a dollar figure are all shown. Feasibility at list prices was checked: 0.60-1.30M uncached input and 0.12-0.26M output reproduce $4.70 at a 97.5-98.5% cache share. The tool's author was updating the tool's price table that day. Keep the report as qualifying and disclose that it is tool-priced.","severity":"medium","loopback":false},
 {"delta_type":"contradiction","claim_id":"finding_1:77-vs-73","description":"The 5h panel shows 77% used (23% remaining), but the chart reads 'today -73%' because its first sample (about 09:35 CST) is already at about 96%. If the window's tokens matched only the 73% fall, the value would be $6.44 and the margin test would fail narrowly (6.44 > 6.40). The window ran from about 06:20 to 11:25 CST, inside one CST day, and the tool counts the whole day's local logs (57.54M = the day's Terra plus auto-review). So 77% is the matching fraction. Add the timing and the sensitivity to the report.","severity":"high","loopback":true},
 {"delta_type":"missing_source_class","claim_id":"finding_4:pro","description":"Pro readings are the top priority, but X (Theo's chart with Terra lines; @Nonosam2 and @NimadFlow screenshots) and YouTube transcripts were unreachable. Delta-retrieve through the remaining routes: Fei2411 issues (done: #149, #161), Yahoo! JAPAN real-time X snippets (done), locdd Pro threads (done), the OpenAI forum after 10-29 (done). Nothing priceable was found. Record these as owner-actionable leads.","severity":"medium","loopback":true},
 {"delta_type":"decision_risk","claim_id":"finding_2:ratio-method","description":"The ratio argument uses Sol anchors from other accounts ($7.8 and $8.3-8.7) to convert el-rocho's and dennisvoss1978's readings into dollars. This shows consistency only. Those readings stay ineligible and are not counted. State this explicitly.","severity":"low","loopback":false}
]
```

Loopback (cycle 1):
- Delta-retrieval re-ran the locdd searches ("terra pro", "codex pro 周", "额度用满预估") and the forum's "pro weekly after:2026-10-29" query. Neither found a priced Pro Terra reading.
- The SouthWindKnows chart was re-read from a cropped screenshot (window reset line at about 06:20; "6m" at 11:19). Finding 1, the counterevidence register and the limitations now carry the window timing and the 73%/77% sensitivity.
- Finding 2 already states that the ratio method only reconciles ineligible readings ("Both fall inside the priced cluster"). The register lists el-rocho as provisional and dennisvoss1978 as not qualifying.

## Cycle 2: Adversarial Reviewer

```json
[
 {"delta_type":"contradiction","claim_id":"finding_2:SunnyDoll-1.9x","description":"A Team black-box test claims a 1.9x hidden multiplier for Terra. Read as a meter weight, it would imply a Terra/Sol token ratio near 1.05, against the 1.25-1.53 found here. It is on Team (out of cohort), truncated, and its original is unreachable (linux.do 403; not mirrored). Keep it in the counterevidence register; it does not move any cell.","severity":"medium","loopback":false},
 {"delta_type":"unsupported_inference","claim_id":"finding_1:independence","description":"Steelman for dependence: all three admitting reports are from launch week, and two (pensuke89, IndividualPlus2011) comment on each other's threads. They are separate measurements on separate accounts. SouthWindKnows is on a different platform and uses a different tool. One observer is one report. Independence holds.","severity":"low","loopback":false},
 {"delta_type":"missing_stakeholder","claim_id":"finding_1:fast-mode","description":"No Plus 5h reporter states standard or Fast mode. Fast mode would multiply the value by 2.5 (O76). The three values agree, and Fast is 2.5x the meter cost, so a Fast reading would sit far below the others. That makes Fast unlikely, but it is unverified. Already listed in Limitations.","severity":"low","loopback":false},
 {"delta_type":"decision_risk","claim_id":"finding_5:el-balad","description":"A news article (El-Balad, 10-28) claims Carbon is available to Pro and Ultra subscribers. It cites no Google source and contradicts the blog and three changelogs. A Hacker News comment about Antigravity availability replies to a comment about Argon. Rejecting both is justified, and both are listed in the counterevidence register.","severity":"low","loopback":false}
]
```

No `high` delta remains after cycle 2, so the critique stops here.
