#!/usr/bin/env python3
"""Keep the retired DeepSeek V4 Flash identity separate from V4.1 Flash."""
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))

def read_jsonl(path):
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]

def write_json(path, data):
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

def write_jsonl(path, data):
    path.write_text("".join(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n" for row in data), encoding="utf-8")

data = read_json(ROOT / "routes.json")
removed = [r for r in data["candidates"] if r["modelId"] == "deepseek-v4-flash"]
data["candidates"] = [r for r in data["candidates"] if r["modelId"] != "deepseek-v4-flash"]
data["selected_route_by_model"].pop("deepseek-v4-flash", None)
for model in data["roster"]:
    if model["modelId"] == "deepseek-v4-flash":
        model["status"] = "uncertain_exact_variant_identity_no_qualified_route"
        model["selectedRoute"] = None
        model["candidateProviders"] = ["OpenCode", "Ollama"]
        model["comparabilityGap"] = ("The roster's exact DeepSeek V4 Flash variant is not established as a current subscription route. "
            "DeepSeek states the previous-generation V4 Flash was retired and its legacy API name is temporarily routed to V4.1 Flash. "
            "OpenCode separately lists V4 Flash and V4.1 Flash with different Go caps ($30 vs $60), but does not document the upstream variant behind its legacy catalog row; Ollama's listed route is V4.1 Flash. "
            "The value multiple is unavailable because no current route is evidenced for the exact benchmark variant; no sibling entitlement or tariff is transferred.")
        model["exactVariantNotes"] = "ValueRank raw-data identifies the AA evaluation as DeepSeek V4 Flash 0731; provider-side retirement and aliasing do not establish that the current route serves that exact evaluated version."
        model["unqualifiedComparators"] = [
            {"provider":"OpenCode","routeModels":["DeepSeek V4 Flash","DeepSeek V4.1 Flash"],"reason":"Separate provider catalog rows; upstream version served by the legacy label is not stated."},
            {"provider":"Ollama","routeModels":["DeepSeek V4.1 Flash"],"reason":"Distinct sibling route; no evidence maps Ollama's plan allowance to the roster's V4 Flash 0731 variant."}
        ]
        model["sourceIds"] = ["S01","S02","S03","S07"]

# Remove all V4.1 plan rows previously attached to the V4 Flash roster ID.
for filename in ("route-tiers.csv", "model-coverage.csv"):
    path = ROOT / filename
    with path.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
        fields = list(rows[0])
    if filename == "route-tiers.csv":
        rows = [r for r in rows if r["model_id"] != "deepseek-v4-flash"]
    else:
        row = next(r for r in rows if r["model_id"] == "deepseek-v4-flash")
        for field in ("selected_provider","provider_route_model","plan_tier","billing_term","plan_fee_per_period","period_months","effective_monthly_fee_usd","annual_effective_monthly_price_usd","published_allowance","allowance_basis","baseline_api_equivalent_usd_P1","baseline_api_equivalent_usd_P2","baseline_api_equivalent_usd_P3","baseline_value_multiple_P1","baseline_value_multiple_P2","baseline_value_multiple_P3","snapshot_api_equivalent_usd_P1","snapshot_api_equivalent_usd_P2","snapshot_api_equivalent_usd_P3","snapshot_value_multiple_P1","snapshot_value_multiple_P2","snapshot_value_multiple_P3","snapshot_subscription_cost_per_api_equivalent_usd_P1","snapshot_subscription_cost_per_api_equivalent_usd_P2","snapshot_subscription_cost_per_api_equivalent_usd_P3","current_promotion"):
            row[field] = ""
        row["status"] = "uncertain_exact_variant_identity_no_qualified_route"
        row["selected_route_scope"] = "none qualified; V4.1 sibling rows excluded"
        row["provider_comparison_gap"] = "DeepSeek retired V4 Flash and routes its legacy API ID to V4.1 Flash; OpenCode's separate catalog rows have distinct Go caps ($30 vs $60) but do not document the legacy row's served version. Ollama lists V4.1 Flash only."
        row["exact_variant_and_unknown_rationale"] = "Raw-data names the evaluated V4 Flash 0731 version. The current exact version cannot be tied to a subscription route; API-equivalent value/multiple are not computable for the evaluated version. No V4.1 sibling price, cap, or quota is transferred."
        row["candidate_providers"] = "OpenCode;Ollama (unqualified identity/sibling routes)"
        row["source_ids"] = "S01;S02;S03;S07"
        row["source_links"] = "../../raw-data.md;https://opencode.ai/v2/docs/console/go;https://ollama.com/pricing;https://api-docs.deepseek.com/updates/"
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields, quoting=csv.QUOTE_ALL, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)

# Keep the eight relevant-but-unqualified catalog tiers visible without ranking them.
exceptions = []
def add_exception(provider, route, tier, term, fee, months, allowance, identity, reason, source_ids, source_links):
    exceptions.append({"roster_model_id":"deepseek-v4-flash","roster_version":"DeepSeek V4 Flash 0731 (AA raw-data)","provider":provider,"provider_route_model":route,"plan_tier":tier,"billing_term":term,"plan_fee_per_period":fee,"period_months":months,"effective_monthly_fee_usd":round(fee/months,6),"currency":"USD","provider_published_allowance":allowance,"api_equivalent_for_roster_variant":"not computed — route identity not qualified","identity_class":identity,"eligible_for_route_selection":"false","exclusion_reason":reason,"source_ids":source_ids,"source_links":source_links})
reason = "OpenCode separately publishes the V4 Flash label, but DeepSeek says the previous-generation V4 Flash is retired and OpenCode does not state the underlying version for its legacy catalog row."
for tier, fee, allowance in (("Go",10,"$30/month by model"),("Go Plus",40,"$120/month by model")):
    add_exception("OpenCode","DeepSeek V4 Flash",tier,"monthly",fee,1,allowance,"exact label; underlying variant unresolved",reason,"S02;S07","https://opencode.ai/v2/docs/console/go;https://api-docs.deepseek.com/updates/")
reason = "V4.1 Flash is a distinct sibling route; its plan allowance cannot be transferred to the roster's V4 Flash 0731 variant."
for provider, route, tiers in (("OpenCode","DeepSeek V4.1 Flash",[("Go",10,1,"$60/month by model"),("Go Plus",40,1,"$120/month by model")]),("Ollama","DeepSeek V4.1 Flash",[("Pro",20,1,"$60 credits/month"),("Pro",200,12,"$60 credits/month"),("Max",100,1,"$300 credits/month"),("Team",500,1,"$1,000 shared credits/month")])):
    for tier, fee, months, allowance in tiers:
        add_exception(provider,route,tier,"annual" if months==12 else "monthly",fee,months,allowance,"sibling V4.1 Flash",reason,"S02;S07" if provider=="OpenCode" else "S03;S07","https://opencode.ai/v2/docs/console/go;https://api-docs.deepseek.com/updates/" if provider=="OpenCode" else "https://ollama.com/pricing;https://api-docs.deepseek.com/updates/")
with (ROOT / "route-exceptions.csv").open("w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=list(exceptions[0]), quoting=csv.QUOTE_ALL, lineterminator="\n")
    writer.writeheader()
    writer.writerows(exceptions)

tier_path = ROOT / "tier-register.md"
tier_lines = [line for line in tier_path.read_text(encoding="utf-8").splitlines() if not line.startswith("| deepseek-v4-flash |")]
tier_lines[2] = "The register includes every published paid tier/cadence route row in the quantified candidate set (60 rows). DeepSeek V4 Flash's identity ambiguity and eight adjacent catalog tier rows are recorded separately in [route-exceptions.csv](route-exceptions.csv), with V4.1 allowances excluded from the roster route. Quarterly Z.AI plan access is documented, but the inspected public price page did not disclose its current quarterly fee; those allowance/API-equivalent rows are retained with price and fee multiple marked not computable."
tier_path.write_text("\n".join(tier_lines) + "\n", encoding="utf-8")

table_path = ROOT / "table.md"
table_lines = table_path.read_text(encoding="utf-8").splitlines()
for i, line in enumerate(table_lines):
    if "(deepseek-v4-flash)" in line:
        table_lines[i] = "| | DeepSeek V4 Flash (deepseek-v4-flash) | max | **Uncertain — no qualified exact-version route** | — | — | Not computable | ValueRank raw-data identifies DeepSeek V4 Flash 0731. DeepSeek retired V4 Flash and routes its legacy API ID to V4.1 Flash; OpenCode separately publishes V4 Flash ($30 Go) and V4.1 Flash ($60 Go) caps but does not state the served version behind its legacy row. Ollama lists V4.1 Flash only. No sibling allowance is transferred. [S01](../../raw-data.md) [S02](https://opencode.ai/v2/docs/console/go) [S03](https://ollama.com/pricing) [S07](https://api-docs.deepseek.com/updates/) See [route exceptions](route-exceptions.csv). |"
table_path.write_text("\n".join(table_lines) + "\n", encoding="utf-8")

evidence = read_jsonl(ROOT / "evidence.jsonl")
if not any(e["evidence_id"] == "E17" for e in evidence):
    evidence.append({"evidence_id":"E17","source_ids":["S02","S07","S03"],"claim":"OpenCode separately catalogs DeepSeek V4 Flash and V4.1 Flash with different Go monthly caps ($30 and $60), while DeepSeek's 2026-09-10 notice says the prior V4 Flash is retired and its legacy API ID is temporarily served by V4.1 Flash. OpenCode does not state which upstream model its separately listed legacy catalog row serves; Ollama's listed route is V4.1 Flash.","scope":"ValueRank deepseek-v4-flash exact-version route eligibility","method":"Compared current DeepSeek official alias/retirement notice with each provider's own exact catalog label and allowance rows; retained all mismatched allowance rows only in route-exceptions.csv.","date":"2026-10-05"})
if not any(e["evidence_id"] == "E18" for e in evidence):
    evidence.append({"evidence_id":"E18","source_ids":["S01"],"claim":"The ValueRank raw-data comparison maps the DeepSeek V4 Flash cohort row to AA's DeepSeek V4 Flash 0731 evaluated variant; the legacy model ID does not erase that version identity.","scope":"ValueRank deepseek-v4-flash evaluated variant","method":"Read the exact DeepSWE chart configuration/model-variant mapping and selected ValueRank roster rows in raw-data.md.","date":"2026-10-05"})
write_jsonl(ROOT / "evidence.jsonl", evidence)
claims = read_jsonl(ROOT / "claims.jsonl")
for claim in claims:
    if claim["claim_id"] == "C10":
        claim["claim"] = "OpenCode separately lists DeepSeek V4 Flash and V4.1 Flash; its plan caps are not interchanged, and the upstream legacy-alias notice alone does not prove which version OpenCode serves through its legacy catalog entry."
        if "E17" not in claim["evidence_ids"]:
            claim["evidence_ids"].append("E17")
if not any(c["claim_id"] == "C13" for c in claims):
    claims.append({"claim_id":"C13","claim":"No exact-version subscription route is selected for the roster's DeepSeek V4 Flash 0731 row because the current subscription variant behind legacy catalog/alias routes is not established; V4.1 Flash allowances are not transferred.","evidence_ids":["E18","E10","E15","E17"],"status":"uncertain_variant_identity_no_route_selected"})
else:
    next(c for c in claims if c["claim_id"] == "C13")["evidence_ids"] = ["E18","E10","E15","E17"]
write_jsonl(ROOT / "claims.jsonl", claims)
data["evidence"] = evidence
data["claims"] = claims
data["sources"] = read_jsonl(ROOT / "sources.jsonl")
write_json(ROOT / "routes.json", data)

for filename in ("README.md", "research_report.md"):
    path = ROOT / filename
    text = path.read_text(encoding="utf-8")
    text = text.replace("Twelve rows have at least one quantified exact route in the candidate set; thirteen remain", "Eleven rows have at least one quantified exact route in the candidate set; fourteen remain")
    text = text.replace("all 66 tier/cadence candidate rows", "all 60 qualified tier/cadence rows and eight unqualified DeepSeek catalog exception rows")
    text = text.replace("all 66 relevant provider tier/cadence routes", "all 60 qualified provider tier/cadence routes")
    text = text.replace("Seventeen source records", "Fifteen source records").replace("Fourteen source records", "Fifteen source records")
    if filename == "README.md":
        text = text.replace("66 model × provider × tier × cadence rows", "60 qualified model × provider × tier × cadence rows")
        lines = text.splitlines()
        for i, line in enumerate(lines):
            if line.startswith("- [route-tiers.csv]"):
                lines[i] = "- [route-tiers.csv](route-tiers.csv): 60 qualified model × provider × tier × cadence rows with denominators, profile calculations, source links, and unknown fields. [route-exceptions.csv](route-exceptions.csv) retains eight DeepSeek V4/V4.1 catalog tier rows excluded from exact-version ranking."
        text = "\n".join(lines) + "\n"
    else:
        old = "OpenCode's DeepSeek V4.1 Flash catalog route is used for the ValueRank legacy ID only because DeepSeek's September 10 notice explicitly says `deepseek-v4-flash` is temporarily routed to V4.1 Flash. The separate OpenCode DeepSeek V4 Flash row is excluded; its allowance is not transferred.[2][7]"
        new = "DeepSeek V4 Flash is left unranked at the exact-version level. ValueRank raw-data identifies the evaluated version as V4 Flash 0731; DeepSeek's September 10 notice says the previous V4 Flash was retired and the legacy API name is temporarily routed to V4.1 Flash. OpenCode separately lists V4 Flash and V4.1 Flash with different Go caps, but does not disclose the upstream version served by its legacy catalog row; Ollama lists V4.1 Flash. The eight adjacent catalog tier rows and their prices/allowances are retained in `route-exceptions.csv` solely to document the gap, and no V4.1 sibling allowance is applied to the roster row.[1][2][3][7]"
        text = text.replace(old, new)
    path.write_text(text, encoding="utf-8")

print(json.dumps({"removed_sibling_rows":len(removed),"route_tier_rows_remaining":60,"exception_rows":len(exceptions),"claims":len(claims),"evidence":len(evidence)}))
