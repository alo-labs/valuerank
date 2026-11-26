# O36/O38 open-web step for AA leaves AA no longer publishes (2026-11-26)

AA's Intelligence Index v5.0.2 no longer runs GDPval-AA or AA-LCR; its model pages still carry them for models evaluated before the change (the pages' `gdpval` and `lcr` fields) and carry nothing for the newest ones. For each cohort configuration whose page lacks a leaf, the exhaustive search logged in `data/leaf_evidence.json` is: the model's AA page (captured 2026-11-26, `data/aa/aa_v432_snapshot.json`), then a plain web search per family, below, dated 2026-11-26.

Queries (WebSearch, standard mode):
1. "GPT-6.2 Sol" GDPval-AA Artificial Analysis
2. "Gemini 4 Neon" GDPval-AA OR "AA-LCR" Artificial Analysis
3. "Muse Ember" GDPval-AA OR "AA-LCR" long context reasoning score
4. "GPT-6.2 Astra" "AA-LCR" OR GDPval Artificial Analysis Intelligence Index
5. Gemini 4 Carbon AA-LCR (covered by query 2's AA results and the Carbon page itself)

Findings: no source reports GDPval-AA or AA-LCR for these configurations. The AA pages for GPT-6.2 Sol and Astra state that the current Index (v5.0.x) has nine evaluations and includes GDP.pdf, not GDPval-AA or AA-LCR; Gemini 4 Argon's AA-LCR scores (80%, 79%) and GPT-6 Sol-era GDPval-AA remarks belong to other models; Meta's Muse Ember evaluation report gives neither score; AA's AA-LCR leaderboard page does not list Muse Ember. Every candidate was rejected as not the exact configuration or as another benchmark (GDP.pdf is a different evaluation, O210).
