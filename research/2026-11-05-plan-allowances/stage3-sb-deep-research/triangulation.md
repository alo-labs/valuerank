# Triangulation (DR-TRIANGULATE)

Admiralty-style grades are recorded in `sources.jsonl` (`reliability_code`). Source numbers refer to the bibliography in `research_report.md`. A claim is "triangulated" when at least two independent observers or one primary ledger plus an independent arithmetic check support it.

## Core claims cross-checked

| # | Claim | Independent support | Result |
|---|---|---|---|
| T1 | Oleg-125 (Plus, Sol, 5h) prices to about $3.58-3.69, not $3.6-7.4 | Primary page re-read through the fetch tool [12]; arithmetic: 232,120 x $2 + 14,130,560 x $0.10 + 55,692 x $10 = $2.434 over 67 points (66-68 with rounding) = $3.58-3.69. Stage 2 reached the same range from a rendered copy | Confirmed (three-way: stage 2, fetch, arithmetic) |
| T2 | jbdamask Max 20x week = $2,277-2,341 | Tweet text and table image read directly [1]; $831 / 0.355..0.365. Cross-observer: simon83 "1% about $20" (model unstated) [10] gives about $2,000, and UberMouse says he averages about $3k per week on 20x (HN 50299481, no meter fraction) | Confirmed; independent models-unstated reports bracket it |
| T3 | deepfoundationdesign Max 5x week = $1,360-1,495 | Issue re-read [2]; arithmetic $877.0-949.6 / 0.635..0.645. Cross-observer: ruuurbag "$1300-1400 per week" and Unlikely-Peace1268 "$55 for 3-4%" (both model unstated; stage 2) | Confirmed; lower-bound corroboration only |
| T4 | Entrypoint changes the meter rate | douflou 1.95x on the 5h meter [4]; ricardoraposo 1.14-1.32x on the weekly meter [5]; jyongchulwp 1.36x warm and 2.5-7.2x cold on Google agy [25] | Three independent controlled tests, two vendors |
| T5 | Faheem_Anis1 and Ultimitehand are one Google AI Pro observation | Identical token counts (185,443 / 1,684,364 / 19,961), identical "$0.72" and "$12" lines, Reddit copy dated 2026-10-23 15:01Z, forum copy stamped 2026-10-26 04:48Z [21][22] | Confirmed by text identity (observer identity itself inferred) |
| T6 | Google Ultra 5x Argon: $50 per 5h and $200 per week at $2/$10 | Yiji_Kong $49.2-50.0 [18]; jamie950315 $199.9-200.1 [19]; blog values $50 and $200 [23] | Three sources agree (the blog is derivative) |
| T7 | Google Pro raised about 1.5x near 2026-10-21/22 | Blog $10 -> $15 per week [23]; Alpler $8.47 on 10-19 [20] vs Faheem/Ultimitehand $12 on 10-23 [21][22] (ratio 1.42); Google docs show no change [24] | Candidate only: one third-party claim plus a consistent dispersion; no primary confirmation |
| T8 | Kimi legacy 5h window did not double 10-25 -> 11-03 | Astralyn coefficients 0.2810 -> 0.2814 (input) and 2.247 -> 2.229 (output) [26]; no Kimi announcement found; the only doubling claim is one untiered Reddit comment (stage 2) | Contradicted by a primary retest |
| T9 | moondrinker-allegretto = astralyn-allegretto | locdd 103607 is a mirror of LINUX DO 3071240: identical title, post bodies map one-to-one with reassigned pseudonyms; the original topic (title now updated 11/03) is directly readable [26][31] | Confirmed (also: locdd pseudonym "DolphinLover" quotes the same declaration, so locdd names carry no identity) |

## Contradictions flagged

- **Pro 5h dispersion (Opus 5.5, Claude Pro):** sergiokapone $14.1-17.7 (10-27) [9]; x2v $25.0-33.3 (11-04, headless) [7]; SchachiOnReddit about $33 and Fast-and-Pythonic about $42 (stage 1, model unstated or fitted); smaug42 about $200 (11-02) [8]. The x2v rows themselves rise from $26.2 to $32.7 per 5-hour window as the mix shifts to cache reads (A1 $2.88/11 points, B2 $9.16/28 points), which shows that list-priced value per meter point is mix-dependent. Verdict: no concordance; do not pool.
- **Ultra weekly (P4 after 10-30):** Coriatel $797-819, BoboThePirate about $1,600 (mixed), CalypsoTheKitty about $1,600 (mixed), z4k3ru about $667, ricardoraposo $1,560-3,087, perfektcrash derived about $2,400 (stage 1). A 3.9x spread. Verdict: the post-10-30 meter is unstable; the cell stays open.
- **OpenAI Pro after 2026-10-29:** aiplans Astra $978-1,630 per week (Pro 200, provisional) [14] against 2026-11-05 user tallies of about $1,200 (Pro 200) and $640 (Pro 100) [16]. The latter are self-tallied with no token split. Verdict: a possible limit change on 11-04/05, unverified.
- **Argon price basis:** reports are priced at the introductory $2/$10; the same ledgers priced at the $4/$20 post-introductory price double [19]. This is a basis choice, not a contradiction, but it changes the Google rows from 2026-12-01.

## Single-sourced claims (not triangulated)

- x2v Claude Pro 5h and weekly values (one account, one day, headless) [6][7].
- The Team 1x black-box test and its Terra multiplier of 1.9x (original post not located) [17].
- Defiant-Pepper's Kimi Plus 5h = 13% of month (a second user, rubenthechadestj, says the same without tokens; stage 2) [32].
- The Google quota raise date (blog only) [23].
