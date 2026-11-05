# Handoff prompt: ValueRank methodology co-design (paused 2026-11-05)

You are taking over a paused multi-AI review of the ValueRank methodology. Read this file, then `research/2026-10-19-methodology-codesign/perplexity/RESUME.md` (its header is stale; the table rows through 154 are current), `ledger.md` (entries to reviewer 153) and `ledger-brief.md`. Repo: alo-labs/valuerank, branch `claude/wizardly-volta-2ppc48`, PR https://github.com/alo-labs/valuerank/pull/2. D = research/2026-10-19-methodology-codesign, P = $D/perplexity.

## Goal
Run the Perplexity six-model panel (GPT-6.1 Sol, Gemini 3.8 Flash, Claude Sonnet 5.5, Kimi K3, GLM 5.3, Grok 4.7) on the current draft until every model says NO FURTHER FEEDBACK. Under O56 a round is clean when it has no Medium-or-higher finding; each model needs two consecutive clean rounds. At convergence: write the research README, update PR #2, close task #10, and report the open owner actions (monthly controlled saturation measurements; the O193 API-migrates-alone path is unbuilt, so `value_v3.freeze` still stops with fewer than two measured Plan references).

## State
- Current draft: **r226** ($D/draft-r226.md, source draft-r226.src.md; review copy and 17 parts in $P/draft-r226.md, $P/parts-r226/, $P/parts-r226.tsv). Unchanged since reviewer 151's triage.
- Done under O56: Claude Sonnet 5.5, Grok 4.7, GPT-6.1 Sol.
- Kimi K3: reviewer 153 CLEAN on r226 (round 1 of 2).
- GLM 5.3: reviewer 154 in progress. Sections 1–4 are saved in $P/partial-r154/ (section 1 has one Low, sections 2–4 NO FURTHER FEEDBACK; untriaged). Sections 5–8 (parts 9–10, 11–12, 13–14, 15–17) were not completed. Its previous round (149) was not clean.
- Gemini 3.8 Flash: last round 151 not clean; needs two consecutive clean rounds.
- Next: finish and triage reviewer 154 (resend sections 5–8, rebuild prompts as below), then Gemini (six sections), then Kimi/GLM/Gemini as needed. If a finding is adopted, create draft r227 (workflow below) and restart that model's clean run.

## Standing rules (verbatim intent)
- Use AskUserQuestion for owner decisions; record them in $D/ledger.md, $D/ledger-brief.md and $P/RESUME.md (and AGENTS.md for broad policies).
- Do not bypass Silver Bullet process enforcement or hooks; never ask to touch trivial or edit quality-gate state files.
- Do not stop until the goal is achieved.
- Never paste tokens or cookies; never print PERPLEXITY_STORAGE_STATE; never ask the user for credentials; do not automate Cloudflare verification.
- Commit messages end with the Co-Authored-By and Claude-Session lines given in your session's attribution reminder. No model IDs in commits or PRs. Never push red CI; after pushing check CI via the PR subscription.

## Triage policy
Adopt verified real defects as code plus tests or as wording; put owner-decision challenges with new arguments to the user; record repeated or settled challenges and design-addition candidates in the ledger as "left candidates, not adopted". Verify reviewer claims against the draft and code before adopting (several earlier claims rested on wrong premises).

## Mechanics
- Regen: `bash $D/../2026-11-01-recapture/regen.sh > /tmp/regen.log; echo EXIT $?` must print `CHECK_OK`. The lint rejects typed registry dates, absence statements without `{{absent:KEY}}`, and unresolved pointers.
- New draft: `cp draft-rN.src.md draft-rN+1.src.md`; `git checkout HEAD -- draft-rN.src.md draft-rN.md`; exact-replace edits; change the title line; add a revision-history entry before "Every change is recorded with its rationale in the ledger."; regen renders draft-rN+1.md.
- Review copy: `python3 $P/tools/review_copy.py $D/draft-rN.md $P/draft-rN.md draft-rN.md`, then `python3 $P/tools/split_draft_26k.py $P/draft-rN.md $P/parts-rN > $P/parts-rN.tsv`. Commit, push (retry with backoff), verify `git ls-remote origin` equals HEAD, then build prompts at that SHA.
- Whole-draft prompt: `python3 /root/.claude/skills/perplexity-multiai-review/scripts/build_linked_prompt.py $D/reviewer-prompt.md $P/draft-rN.md $P/parts-rN.tsv $D/ledger-brief.md alo-labs/valuerank $SHA /tmp/prompt-rXXX.md`; then replace "its last 12 words. If any part could not be read to its end, say which one and stop." with "its final sentence. If a part could not be read to its end, say which one and stop; otherwise go on to the full review." Limit 40,000 characters after replacement (condense ledger-brief.md if over).
- Section prompt: `python3 $P/tools/build_section_prompt.py $D/reviewer-prompt.md $P/draft-rN.md $P/parts-rN.tsv $D/ledger-brief.md alo-labs/valuerank $SHA FIRST LAST out.md`, then `sed -i 's/its last 12 words\./its final sentence./' out.md`. GLM sections: 1–2, 3–4, 5–6, 7–8, 9–10, 11–12, 13–14, 15–17. Gemini: six sections. Kimi: four sections.
- Send: `cd ~/.claude/skills/perplexity-multiai-review/scripts; node ask.mjs ask "<Model>" prompt out.md` (exact names above); run in the background with a DONE marker log. Empty or short output usually means it was not submitted; a GitHub connector 503 on a part means resend that section.
- Code changes: `git add -A; mv data/tb4-scrape.json /tmp/; python3 -m pytest -q -p no:cacheprovider -W ignore --cov > /tmp/pytest.log` (100% coverage required, about 25 minutes; run in background), move tb4-scrape.json back, then `npm run -s test:js`, `npm run -s test:e2e`, commit, `npm run -s verify:docs`. Text-only changes: `pytest tests/test_draft_figures.py tests/test_plan_reports_provenance.py` plus verify:docs.

## Pause note
The user paused all work on 2026-11-05. Resume only when the user says so. Session `session_013z3F7YTZ5T5DAJxAcCmeVV` ("SB") was also told to pause and acknowledged.
