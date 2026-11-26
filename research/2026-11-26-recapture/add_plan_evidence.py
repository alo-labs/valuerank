"""Fold the 2026-11-26 plan-allowance research record (research/2026-11-26-plan-allowances/) into the plan data.

    PYTHONPATH=. python3 research/2026-11-26-recapture/add_plan_evidence.py

Writes (idempotent): data/plan_reports.json (the research's report records, in the engine's schema, one per id),
data/plan_cost_routes.json (the three-stage search log entry, the registered change records and the announced-change items).
The recorder's own reading of each report is kept in the record's `recorderReading`; the engine's admission rules decide.
"""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

HERE = Path(__file__).parent
ROOT = HERE.parent.parent
RECORD = ROOT / "research" / "2026-11-26-plan-allowances"
ISO = re.compile(r"^\d{4}-\d{2}-\d{2}(T\d{2}:\d{2}(:\d{2})?(Z|[+-]\d{2}:\d{2})?)?")
ENGINE_FLAGS = ("provisional", "mixedModel", "modelUnstated", "tierUnstated", "lowerBound", "aggregator", "challenged", "derived", "anomaly")


def iso(text):
    match = ISO.match(text) if isinstance(text, str) else None
    return match.group(0) if match else None


def convert(item: dict) -> dict:
    flags = {key: bool(item["flags"].get(key)) for key in ENGINE_FLAGS}
    notes = []
    if item["flags"].get("nonInteractiveEntrypoint"):
        flags["anomaly"] = True
        notes.append("headless entrypoint: the five-hour meter runs about 1.95x faster than the interactive terminal (recorder's reading)")
    archive = [entry for entry in item.get("archive") or [] if entry.get("sha256") and entry.get("byteExact", True)]
    primary = archive[0] if archive else None
    window_end = iso(item.get("windowEnd")) or item["reportDate"]
    window_start = iso(item.get("windowStart"))
    record = {
        "id": item["id"], "provider": item["provider"], "plan": item["plan"], "modelId": item["modelId"], "stage": item["stage"],
        "windowStart": window_start, "windowStated": bool(item.get("windowStated")) and window_start is not None or bool(item.get("windowStated")),
        **flags, "observer": item["observer"], "effort": item.get("effort"), "url": item["url"], "reportDate": item["reportDate"],
        "windowEnd": window_end, "unit": item["unit"], "valueLower": item["valueLower"], "valueUpper": item["valueUpper"],
        "note": "; ".join(filter(None, [item.get("quotedSpan"), item.get("derivation"), *notes, f"speed mode: {item['speedMode']}" if item.get("speedMode") else None])),
        "source": ["research/2026-11-26-plan-allowances/reports.json"],
        "recorderReading": item.get("reading"),
    }
    if item.get("speedMode"):
        record["speedMode"] = item["speedMode"]
    if primary:
        record["archive"] = {"url": primary["url"], "fetchedAt": primary["fetchedAt"], "sha256": primary["sha256"],
                             "file": "research/2026-11-26-plan-allowances/" + primary["file"], "span": (item.get("quotedSpan") or "")[:300]}
        if len(archive) > 1:
            record["archiveFiles"] = [{"file": "research/2026-11-26-plan-allowances/" + entry["file"], "sha256": entry["sha256"], "url": entry["url"]} for entry in archive[1:]]
    return record


# Change records the engine registers (O99, O105, O112): in-force availability, metering and reset events at plan level. Limit, price and credit
# records need a provider announcement or two independent reports (E18, O79, O196): the research found none in force, so none is registered;
# the single-observer limit claims and the contested Anthropic shrink stay in the research record.
REGISTER = {
    "anthropic-fable52-on-claude-plans": {"provider": "Anthropic", "meterFamily": "Claude", "date": "2026-11-09", "type": "availability",
                                          "basis": "Claude Fable 5.2 launched on the Claude plans: Max and Ultra inside the weekly pool (up to 50% of the weekly limit), Pro on usage credits (Claude help centre, archived in research/2026-11-26-plan-allowances/)"},
    "google-carbon-gemini-app-ultra": {"provider": "Google", "plans": ["Google AI Ultra 5x", "Google AI Ultra 20x"], "date": "2026-11-10", "type": "availability",
                                       "basis": "Gemini 4 Carbon offered on Google AI Ultra (research/2026-11-26-plan-allowances/, google-carbon-gemini-app-ultra)"},
    "openai-gpt62-on-chatgpt-plans": {"provider": "OpenAI", "plans": ["ChatGPT Plus", "ChatGPT Pro 100", "ChatGPT Pro 200", "ChatGPT Pro 500"], "date": "2026-11-17", "type": "availability",
                                      "basis": "GPT-6.2 Sol and Astra offered in ChatGPT Work and Codex on the plans (OpenAI release notes; research/2026-11-26-plan-allowances/)"},
    "openai-gpt62-speed-metering": {"provider": "OpenAI", "plans": ["ChatGPT Plus", "ChatGPT Pro 100", "ChatGPT Pro 200", "ChatGPT Pro 500"], "date": "2026-11-17", "type": "metering",
                                    "basis": "GPT-6.2's speed modes meter at Fast 2x and Ultrafast 6x (GPT-6.1 and GPT-6: 2.5x and 8x); a metering announcement is logged, it does not split (O99)"},
    "google-reset": {"provider": "Google", "plans": ["Google AI Pro", "Google AI Ultra 5x", "Google AI Ultra 20x"], "date": "2026-11-17", "type": "reset",
                     "basis": "Antigravity quota reset for all users (research/2026-11-26-plan-allowances/, google-antigravity-reset-first-birthday)"},
    "google-neon-launch": {"provider": "Google", "plans": ["Google AI Pro", "Google AI Ultra 5x", "Google AI Ultra 20x"], "date": "2026-11-18", "type": "availability",
                           "basis": "Gemini 4 Neon launched in Antigravity and the Gemini app on Google AI Pro and Ultra (research/2026-11-26-plan-allowances/)"},
    "google-antigravity-cache-22pct-and-reset": {"provider": "Google", "plans": ["Google AI Pro", "Google AI Ultra 5x", "Google AI Ultra 20x"], "date": "2026-11-21", "type": "metering",
                                                 "basis": "Antigravity caching gain announced with a reset; metering is logged, not split (O99)"},
    "google-carbon-on-ai-pro-and-reset": {"provider": "Google", "plans": ["Google AI Pro"], "date": "2026-11-23", "type": "availability",
                                          "basis": "Gemini 4 Carbon offered on paid Google AI Pro in Antigravity (research/2026-11-26-plan-allowances/)"},
}
# Announced changes that take effect after this release cutoff (recorded when seen; they flag nothing until in force).
ANNOUNCED = [
    {"provider": "Anthropic", "plans": ["Claude Pro", "Claude Max 5x", "Claude Max 20x"], "announcedOn": "2026-11-26", "effective": "2026-12-07",
     "change": "purchased usage credits expire after 12 months (plan allowances untouched)", "source": "research/2026-11-26-plan-allowances/changes.json (anthropic-usage-credit-expiry)", "status": "announced, not in force"},
    {"provider": "OpenAI", "plans": ["ChatGPT Plus", "ChatGPT Pro 100", "ChatGPT Pro 200", "ChatGPT Pro 500"], "announcedOn": "2026-10-31", "effective": "December 2026 (no day stated)",
     "change": "the shared ChatGPT and Codex token allowance is still announced, not in force on 2026-11-26 (help article updated 2026-11-25, no sizes)",
     "source": "research/2026-11-26-plan-allowances/changes.json (openai-december-shared-allowance)", "status": "announced, not in force at the 2026-11-26 cutoff"},
    {"provider": "Google", "plans": ["Google AI Pro", "Google AI Ultra 5x", "Google AI Ultra 20x"], "announcedOn": "2026-11-23", "effective": "2026-11-30 and 2026-12-01",
     "change": "Gemini 4 Argon and Carbon API prices rise from $2/$10 to $4/$20 and Argon, Gemini 3.8 Flash, GPT-OSS-120b and Claude 4.6 leave Antigravity",
     "source": "research/2026-11-26-plan-allowances/changes.json (google-30-nov-removals-and-carbon-price)", "status": "announced, not in force at the 2026-11-26 cutoff"},
]


def routes_document() -> None:
    path = ROOT / "data" / "plan_cost_routes.json"
    document = json.loads(path.read_text())
    policy = document["evidencePolicy"]
    changes = {item["id"]: item for item in json.loads((RECORD / "changes.json").read_text())["changes"]}
    missing = sorted(set(REGISTER) - set(changes) - {"google-reset"})
    if missing:
        raise ValueError(f"research record lacks change ids {missing}")
    profile = policy["reportEligibilityProfile"]
    have = {(item["provider"], item["date"], item["type"], tuple(item.get("plans") or ()), item.get("meterFamily")) for item in profile["partitionSplits"]}
    for key, record in REGISTER.items():
        marker = (record["provider"], record["date"], record["type"], tuple(record.get("plans") or ()), record.get("meterFamily"))
        if marker not in have:
            profile["partitionSplits"].append(record)
    entry = json.loads((RECORD / "searchlog-entry.json").read_text())
    entry.pop("note", None)
    # The build names the three stages exactly (O71); stage 3 is the owner's Silver Bullet Deep Research, unavailable in this environment, so
    # the record says what ran in its place (Perplexity, three models) and the entry carries the substitution plainly.
    outcomes = ["no new report admitted by this stage alone; 37 searches and about 70 page fetches (stage1/queries-websearch.md)",
                "structured sweeps of 38,996 Reddit posts, 3,919 comments, 1,695 Hacker News items, 341 Bluesky posts and X post JSON; the Google forum, OpenAI community and LINUX DO sweeps were rate-limited and partial (stage2/README.md)",
                "the same prompt to three Perplexity models (Claude Sonnet 5.5, GPT-6.2 Sol, Kimi K3); every claim re-fetched; several of their claims were wrong or unverifiable (stage3/README.md)"]
    names = list(__import__("valuerank.value_v3", fromlist=["O71_STAGES"]).O71_STAGES)
    for stage, name, outcome in zip(entry["stages"], names, outcomes):
        stage["actualStage"] = stage["stage"]
        stage["stage"] = name
        stage["outcome"] = outcome
    entry["stages"][2]["degraded"] = "Silver Bullet's Deep Research is unavailable in this environment; this stage ran through Perplexity (three models), as the record states"
    entry["models"] = ["Claude Fable 5.2", "Claude Opus 5.5", "Claude Sonnet 5.5", "Claude Haiku 5.5", "GPT-6.2 Sol", "GPT-6.2 Astra", "GPT-6.1 Sol", "GPT-6.1 Terra",
                       "GPT-6 Astra", "GPT-6 Luna", "Gemini 4 Neon", "Gemini 4 Carbon", "Muse Ember", "MiMo-V2.6-Flash"]
    policy["searchLog"] = [item for item in policy["searchLog"] if item.get("searchedOn") != entry["searchedOn"]] + [entry]
    policy["searchCutoff"] = entry["searchedOn"]
    document["asOf"] = entry["searchedOn"]
    policy["reportingWindow"] = {"start": "2026-10-27", "end": "2026-11-26"}  # E213: the 30 days ending on the release cutoff
    items = policy["announcedChanges"]["items"]
    for item in ANNOUNCED:
        if item not in items:
            items.append(item)
    source = document["sourceEvidence"]["semianalysis"]
    if not any(item.get("readOn") == "2026-11-26" for item in source["rereads"]):
        source["rereads"].append({
            "readOn": "2026-11-26",
            "result": "the article page was fetched again (public part); the two figures it states in text, $2,485 of Fable 5.1 on Max 20x and $2,897 of GPT-6 Astra on Pro 200, equal the transcription; the other transcribed figures sit in chart images that this read cannot decode, so they are not re-verified; the page still shows the publication date Oct 05, 2026 and dateModified equals datePublished (2026-10-05T20:01:09Z), so no revision note",
            "file": "research/2026-11-26-plan-allowances/semianalysis/anthropic-subscriptions-offer-5x.html",
            "sha256": hashlib.sha256((ROOT / "research/2026-11-26-plan-allowances/semianalysis/anthropic-subscriptions-offer-5x.html").read_bytes()).hexdigest(),
            "fetchedAt": "2026-11-26T13:40:00Z"})
    policy["openCodeGoApplication"] = policy["openCodeGoApplication"].rstrip() + (
        " The page was read again on 2026-11-26T03:10:58Z (SHA-256 40c238db6cfc8ae3dcb3ecef1c309af1e1a376bebd2ca12cf7b85228a971379c, "
        "research/2026-11-26-plan-allowances/opencode-go/): no cohort model's monthly dollar limit or fee changed and none was added or removed.")
    path.write_text(json.dumps(document, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"splitRecords": len(profile["partitionSplits"]), "searchLog": len(policy["searchLog"])}))


def main() -> None:
    incoming = json.loads((RECORD / "reports.json").read_text())["reports"]
    path = ROOT / "data" / "plan_reports.json"
    document = json.loads(path.read_text())
    have = {report["id"] for report in document["reports"]}
    added = [convert(item) for item in incoming if item["id"] not in have]
    document["reports"] += added
    path.write_text(json.dumps(document, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"reportsAdded": len(added), "reports": len(document["reports"])}))
    routes_document()


if __name__ == "__main__":
    main()
