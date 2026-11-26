# Handoff: O71 stage 3, Terra and Carbon (FS-SILVER_DEEP_RESEARCH → AF-DOCUMENT → AF-VALIDATE)

## For the coordinator
- **Output:** `research/2026-10-31-plan-allowances-v5-entrants/stage3-sb-deep-research/`. No other repository file was edited, and nothing was committed. Raw dumps are in `raw/`, the SouthWindKnows screenshots in `raw/images/`, and the logs in `validation/`.
- **Verdicts:**
  - Terra × Plus × 5h passes O11 at about $5.3–6.1 per 5h, on three reports: pensuke89, IndividualPlus2011 and SouthWindKnows (new).
  - Every other Terra cell fails, as does every Carbon cell.
  - Carbon is not available on consumer plans.
- **Candidate for `partitionSplits` or flags:** none new. Two items are recorded as flags only:
  - the 10-27 ~17:23 UTC metering shift (dennisvoss1978; Chinese users report a morning slowdown);
  - the unverified report that the CLI bills Terra as Sol.

## Owner-actionable leads (ranked)
1. **Theo's weekly API-equivalent chart** (X, about 10-29/30). It has Terra line items for Pro $200 and $500 after the doubling, but only the Sol values were transcribed (Fei2411 #161). X was unreachable here.
2. **SunnyDoll's LINUX DO black-box post** ("10月27日更新 gpt-6.1-terra 计费，隐藏倍率高达 1.9x"). linux.do returns 403 and the post is not mirrored. It is a Team plan, so useful for metering only.
3. **YouTube** (metadata only here):
   - Unhallucinated, "Codex Power Users Lost Up to 88% vs October" (pT3nNc5npY4);
   - Kai, "Your $200 ChatGPT Plan is now worth less!" (P0i3vYuJZH8);
   - BENIBIX, "Codex usage limits: 5-hour and weekly, day by day" (0I6CwC5gdgI).
4. **Recruit** Terra-only full-week measurements after 2026-10-29 on Plus, Pro $100 and Pro $200, with a cached/uncached/output split and the speed mode stated.

## Tooling notes
- search-cli is absent and no Task/Agent tool was available, so the run used host fallback, sequentially.
- The new routes that worked are locdd.com (LINUX DO mirror), api.bsky.app and Yahoo! JAPAN real-time search. Future runs should use them.
- verify_claim_support.py links bibliography entries only through http(s) URLs. The local-document citations [35]–[39] were backfilled into claims.jsonl before verification; the method is recorded in vloop-rollup.json.
