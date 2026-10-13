#!/usr/bin/env python3
"""Build V2-FEATURE-MAP.csv from inventory + public lookups. Never guess licenses."""
import csv, re, os
from pathlib import Path

ROOT = Path("/workspace/build-plan-2026-10-12")
INV = ROOT / "REPO-INVENTORY.csv"
LOOKUP = ROOT / "v2work" / "lookup2.tsv"
OUT = ROOT / "V2-FEATURE-MAP.csv"

# name -> (public_full, license, purpose)
look = {}
if LOOKUP.exists():
    for line in LOOKUP.read_text().splitlines():
        parts = line.split("\t")
        if len(parts) < 2:
            continue
        key = parts[0]
        short = key.split("/")[-1].lower()
        if parts[1] == "UNKNOWN" or "message" in parts[1]:
            look[short] = ("", "UNKNOWN", "")
        elif len(parts) >= 4:
            look[short] = (parts[1], parts[2] or "NONE", parts[3])
        elif len(parts) == 3:
            look[short] = (parts[1], parts[2] or "NONE", "")

PERMISSIVE = {
    "MIT", "Apache-2.0", "BSD-2-Clause", "BSD-3-Clause", "BSD-3-Clause-Clear",
    "ISC", "MPL-2.0", "0BSD", "Unlicense", "CC0-1.0", "Zlib", "BlueOak-1.0.0",
}

# exclusion patterns (name or purpose)
EXCL = [
    (r"captcha|2captcha|anticaptcha|capsolver|hcaptcha|recaptcha", "excluded: captcha solving"),
    (r"cf[-_]?bypass|cloudflare[-_]?(bypass|scrape)|cfscrape|playwright-cf|puppeteer-cf|flaresolverr", "excluded: Cloudflare/bot-detection bypass"),
    (r"stealth|antidetect|multilogin|gologin|undetected|browserless-stealth|puppeteer-extra-plugin-stealth", "excluded: antidetect/stealth browser"),
    (r"hashcat|john[-_]?the[-_]?ripper|password[-_]?crack|hash[-_]?crack", "excluded: credential cracking"),
    (r"\bmev\b|arbitrage|pumpfun|trading[-_]?bot|defi[-_]?bot|sniper|frontrun|sandwich", "excluded: MEV/DeFi/trading bots"),
    (r"wallet|private[-_]?key|seed[-_]?phrase|hd[-_]?wallet", "excluded: wallets"),
    (r"plaid|paddle|lemon[-_]?squeezy|stripe|payment|checkout|billing|gumroad|shopify", "excluded: payments"),
    (r"\bmining\b|miner|hashrate", "excluded: mining"),
    (r"\bnft\b|opensea|mint", "excluded: NFT"),
    (r"vitalitychems|vitality[-_]?store|fleet-moss|wholesale|affiliate", "excluded: vitality store / commerce"),
    (r"^1[Tt]$|/1[Tt]|natal-vault|knowledge[-_]?vault|\bvault\b", "excluded: 1T/vault"),
]

# capability category by name/purpose keywords (first match wins)
CATS = [
    (r"agent|orchestr|foreman|crew|swarm|multi[-_]?agent|autogen|langgraph|crewai", "agents-studio"),
    (r"memory|rag|vector|embedding|knowledge[-_]?graph|graphiti|mem0|lancedb|chroma|qdrant", "knowledge-memory"),
    (r"offline|mesh|p2p|webrtc|ipfs|kiwix|service[-_]?worker|local[-_]?first|sneakernet|lora|meshtastic", "offline-mesh"),
    (r"api[-_]?anything|adapter|sdk|client|wrapper|mcp|openapi|graphql", "adapters"),
    (r"token|prompt|compress|context|cache|summar", "token-efficiency"),
    (r"sandbox|container|docker|isolate|compute|worker", "compute-sandbox"),
    (r"gitbook|docs|documentation|gitmesh|markdown|mdx", "docs"),
    (r"search|index|elastic|meili|typesense|fuse", "search-index"),
    (r"chat|messaging|room|discord|slack|telegram", "comms"),
    (r"auth|oauth|sso|passport|clerk|lucia", "auth"),
    (r"queue|job|bull|temporal|workflow|cron", "jobs-queue"),
    (r"test|playwright|vitest|jest|cypress", "testing"),
    (r"ui|react|next|vite|frontend|dashboard|chamber|board", "ui"),
    (r"fingerprint|creepjs|fingerprintjs", "browser-fingerprint"),  # often dual-use; review
    (r"scrape|crawler|cheerio|puppeteer|playwright(?!-cf)", "web-fetch"),
    (r"llm|openai|anthropic|xai|grok|ollama|vllm|model", "llm-runtime"),
    (r"security|shepherd|protocol|opsec|encrypt|age\b|sops|vault", "security-protocols"),
    (r"learn|train|rl|reinforcement", "learning"),
    (r"monitor|observ|metric|otel|prometheus|sentry", "observability"),
    (r"tessera|tesseract|sovereign", "tessera-core"),
]

ACCESSIBLE_META = {
    "vitalitychems-dot/TESSERA": ("NONE", "Unified Tessera monorepo: web/API, preview, mesh, agents", "tessera-core", "y", "current v2 base; package.json says MIT, GitHub license field empty"),
    "vitalitychems-dot/Gitbook": ("NONE", "Tessera docs, intake, review, agent collaboration ledger", "docs", "y", "docs home; idea+content reusable, confirm LICENSE file"),
    "vitalitychems-dot/GitbookAI": ("NONE", "Public git-carried mesh room (renamed GitMesh)", "offline-mesh", "y", "mesh drops; renamed to GitMesh"),
    "vitalitychems-dot/vitality": ("NONE", "Vitality Supply store + archives", "commerce", "excluded", "excluded: vitality store"),
    "collink1007/z": ("NONE", "Historical Zz / tesseract archive checkout", "tessera-core", "n", "idea-only / archive; license NONE; wallet/secret paths stay out"),
    "collink1007/XXX": ("MIT", "Historical XXX tess client/server (lattice-mesh, SW, offline)", "offline-mesh", "y", "MIT in package.json; reuse offline pieces only, exclude wallet/income routes"),
    "collink1007/amber-flame-tiger-sand": ("NONE", "Grok app template with TESSERA seed docs", "ui", "n", "license NONE; idea-only; already partly in Gitbook archive"),
    "collink1007/fleet-moss-monarch-rapid": ("NONE", "Vitality storefront migrations", "commerce", "excluded", "excluded: vitality store"),
    "thetesseractai/18": ("MIT", "Tessera Sovereign System v18 multi-agent consolidation", "tessera-core", "y", "MIT package; prior TESSERA lineage; secrets in .replit stay out"),
    "TheTesseractAI/18": ("MIT", "Tessera Sovereign System v18 multi-agent consolidation", "tessera-core", "y", "MIT package; prior TESSERA lineage; secrets in .replit stay out"),
}

def categorize(name, purpose):
    blob = f"{name} {purpose}".lower()
    for pat, reason in EXCL:
        if re.search(pat, blob, re.I):
            return "excluded", "excluded", reason
    for pat, cat in CATS:
        if re.search(pat, blob, re.I):
            return cat, None, None
    return "misc", None, None

def include_for(license, cat, excl_reason, accessible, purpose):
    if excl_reason:
        return "excluded", excl_reason
    if cat == "browser-fingerprint":
        return "excluded", "excluded: fingerprinting dual-use (Security hold)"
    if cat == "commerce":
        return "excluded", "excluded: vitality store / commerce"
    if accessible == "y":
        if license in PERMISSIVE or license == "NONE":
            # NONE on our own repos: still include as base/archive with reason
            if license == "NONE":
                return "n", "idea/code review only until LICENSE clarified; own repo"
            return "y", "permissive license; capability reusable"
        return "n", f"license {license} not permissive; idea-only clean-room"
    # inaccessible
    if license in PERMISSIVE:
        return "y", f"public match under {license}; prefer dependency or clean attribution"
    if license == "UNKNOWN":
        return "n", "no public match found; idea-only from name/description"
    if license in ("NONE", "NOASSERTION", ""):
        return "n", "public match has no SPDX license; idea-only clean-room"
    return "n", f"license {license} not permissive; idea-only clean-room"

rows_in = list(csv.DictReader(open(INV)))
out_rows = []
for r in rows_in:
    repo = r["repo"]
    short = repo.split("/")[-1]
    acc = "y" if r.get("accessible") == "y" else "n"
    status = r.get("status", "")

    if repo in ACCESSIBLE_META or repo.replace("thetesseractai", "TheTesseractAI") in ACCESSIBLE_META:
        key = repo if repo in ACCESSIBLE_META else repo.replace("thetesseractai", "TheTesseractAI")
        lic, purpose, cat, incl, reason = ACCESSIBLE_META[key]
        # re-check excl on vitality etc already set
        if incl == "excluded":
            incl = "excluded"
        out_rows.append({
            "repo": repo,
            "accessible": acc,
            "license": lic,
            "purpose": purpose.replace(",", ";"),
            "capability_category": cat,
            "include": incl,
            "reason": reason.replace(",", ";"),
            "public_match": "",
        })
        continue

    # archived-in-gitbook special
    if "ARCHIVED" in status.upper():
        cat, _, ex = categorize(short, status)
        out_rows.append({
            "repo": repo,
            "accessible": "n",
            "license": "UNKNOWN",
            "purpose": "archived folder in Gitbook/TESSERA; live repo unreachable",
            "capability_category": cat if not ex else "excluded",
            "include": "excluded" if ex else "n",
            "reason": ex or "archive-only; live repo BLOCKED; use archived tree under license review",
            "public_match": "",
        })
        continue

    pub_full, lic, purpose = look.get(short.lower(), ("", "UNKNOWN", ""))
    if not purpose:
        purpose = f"mentioned in logs as {repo}; no description available" if lic == "UNKNOWN" else purpose
    cat, _, ex = categorize(short, purpose)
    if ex:
        incl, reason = "excluded", ex
    else:
        incl, reason = include_for(lic, cat, None, acc, purpose)
    out_rows.append({
        "repo": repo,
        "accessible": acc,
        "license": lic or "UNKNOWN",
        "purpose": (purpose or "UNKNOWN").replace(",", ";")[:200],
        "capability_category": cat,
        "include": incl,
        "reason": reason.replace(",", ";"),
        "public_match": pub_full,
    })

# also add api-anything and agentcraft as external tools
for repo, lic, purpose, cat, incl, reason in [
    ("goodnight000/api-anything", "MIT", "Local website-to-operation recorder/replayer; MCP call_operation", "adapters", "y", "MIT; adapter layer for public no-login sites after Security review"),
    ("blendi-remade/agentcraft", "MIT", "Lead+workers in git worktrees; Minecraft studio view; Foreman orchestrator", "agents-studio", "y", "MIT; reuse Foreman patterns clean-room or with attribution; web 2D/3D studio instead of Minecraft"),
]:
    out_rows.append({
        "repo": repo, "accessible": "n", "license": lic, "purpose": purpose,
        "capability_category": cat, "include": incl, "reason": reason, "public_match": repo,
    })

fields = ["repo","accessible","license","purpose","capability_category","include","reason","public_match"]
with open(OUT, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fields)
    w.writeheader()
    w.writerows(out_rows)

from collections import Counter
c = Counter(r["include"] for r in out_rows)
acc_y = sum(1 for r in out_rows if r["accessible"]=="y")
pub = sum(1 for r in out_rows if r["public_match"] and r["accessible"]!="y")
unk = sum(1 for r in out_rows if r["license"]=="UNKNOWN" and r["accessible"]!="y")
print("rows", len(out_rows))
print("accessible", acc_y)
print("public_match_found", pub)
print("unknown_license_inacc", unk)
print("include counts", dict(c))
print("lookup2 lines", sum(1 for _ in open(LOOKUP)) if LOOKUP.exists() else 0)
