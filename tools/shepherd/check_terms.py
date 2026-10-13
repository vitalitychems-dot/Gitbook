#!/usr/bin/env python3
"""Offline terms gate for the SHEPHERD-RELAY allowlist.

Rejects a source that lacks a license, a terms URL, or a published rate
limit, or that requires authentication. This module does not open a
network connection, does not scrape, and does not raise a published cap.
Bundle signing and encryption are out of scope.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

SCHEMA = "shepherd-allowlist/v1"
ALLOWED_KINDS = (
    "rss-atom",
    "wikimedia-dumps",
    "arxiv-oai-pmh",
    "medlineplus-xml",
    "pmc-oa",
    "noaa",
    "osm-diffs",
    "github-public-releases",
)
PLACEHOLDER_LICENSES = {"", "unknown", "tbd", "n/a", "na", "none", "null", "todo"}
EVASION_KEYS = {
    "evade_rate_limit",
    "bypass_rate_limit",
    "circumvent_rate_limit",
    "ignore_rate_limit",
    "extra_machines",
    "multi_ip",
    "scrape",
    "html_scrape",
}
AUTH_FLAG_KEYS = {
    "api_key_required",
    "token_required",
    "account_required",
    "oauth_required",
    "requires_auth",
}
SECRET_KEYS = {"api_key", "token", "password", "client_secret", "access_token"}


def default_allowlist_path() -> Path:
    return Path(__file__).with_name("sources.json")


def load_document(path: Path) -> dict:
    with path.open(encoding="utf-8") as handle:
        document = json.load(handle)
    if not isinstance(document, dict):
        raise ValueError("allowlist must be a JSON object")
    return document


def check_document(document: dict) -> list[dict]:
    """Return one result per source. A document with no sources fails once."""
    if document.get("schema") != SCHEMA:
        return [_result(None, [f"schema must be {SCHEMA}"])]
    sources = document.get("sources")
    if not isinstance(sources, list) or not sources:
        return [_result(None, ["sources must be a non-empty list"])]
    results = []
    seen_ids = set()
    seen_kinds = set()
    for source in sources:
        if not isinstance(source, dict):
            results.append(_result(None, ["source must be an object"]))
            continue
        source_id = source.get("id")
        reasons = check_source(source)
        if isinstance(source_id, str) and source_id in seen_ids:
            reasons.append(f"duplicate id {source_id}")
        if isinstance(source_id, str) and source_id:
            seen_ids.add(source_id)
        kind = source.get("kind")
        if isinstance(kind, str) and kind in seen_kinds:
            reasons.append(f"duplicate kind {kind}")
        if isinstance(kind, str) and kind:
            seen_kinds.add(kind)
        results.append(_result(source_id if isinstance(source_id, str) else None, reasons))
    return results


def check_source(source: dict) -> list[str]:
    reasons = []
    if not isinstance(source, dict):
        return ["source must be an object"]

    source_id = source.get("id")
    if not isinstance(source_id, str) or not source_id.strip():
        reasons.append("missing id")

    kind = source.get("kind")
    if kind not in ALLOWED_KINDS:
        reasons.append("kind is not on the keyless allowlist")

    license_name = source.get("license")
    if not isinstance(license_name, str) or license_name.strip().lower() in PLACEHOLDER_LICENSES:
        reasons.append("missing license")

    if not _is_http_url(source.get("terms_url")):
        reasons.append("missing terms URL")

    reasons.extend(_rate_limit_reasons(source.get("rate_limit")))
    reasons.extend(_auth_reasons(source))
    reasons.extend(_evasion_reasons(source))
    if _url_has_userinfo(source.get("endpoint")):
        reasons.append("endpoint contains credentials")
    return reasons


def _rate_limit_reasons(rate_limit) -> list[str]:
    if not isinstance(rate_limit, dict):
        return ["missing rate limit"]
    reasons = []
    published = rate_limit.get("published")
    if not isinstance(published, str) or not published.strip():
        reasons.append("missing rate limit")
    if not _is_http_url(rate_limit.get("citation")):
        reasons.append("missing rate-limit citation")

    has_requests = "max_requests" in rate_limit
    has_window = "per_seconds" in rate_limit
    if has_requests or has_window:
        requests = rate_limit.get("max_requests")
        window = rate_limit.get("per_seconds")
        if not _positive_number(requests) or not _positive_number(window):
            reasons.append("rate limit numbers must be positive")
        elif isinstance(requests, bool) or isinstance(window, bool):
            reasons.append("rate limit numbers must be positive")
    if rate_limit.get("numeric_request_rate_published") is False and has_requests:
        reasons.append("numeric rate was set where the publisher published none")

    for key in ("concurrency", "max_connections_per_ip", "retry_interval_seconds"):
        if key in rate_limit and not _positive_int(rate_limit.get(key)):
            reasons.append(f"{key} must be a positive integer")
    if "retry_interval_seconds" in rate_limit and not _is_http_url(rate_limit.get("retry_citation")):
        reasons.append("missing retry-limit citation")
    return reasons


def _auth_reasons(source: dict) -> list[str]:
    reasons = []
    if source.get("auth_required") is not False:
        reasons.append("requires auth")
    access = source.get("access")
    if access is not None and access != "unauthenticated":
        reasons.append("requires auth")
    for key in AUTH_FLAG_KEYS:
        if source.get(key) is True:
            reasons.append("requires auth")
    for key in SECRET_KEYS:
        value = source.get(key)
        if value not in (None, "", False):
            reasons.append("requires auth")
    quota = source.get("rate_limit")
    if isinstance(quota, dict) and quota.get("quota") == "authenticated":
        reasons.append("requires auth")
    return reasons


def _evasion_reasons(source: dict) -> list[str]:
    reasons = []
    blobs = [source]
    rate_limit = source.get("rate_limit")
    if isinstance(rate_limit, dict):
        blobs.append(rate_limit)
    for blob in blobs:
        for key in EVASION_KEYS:
            if blob.get(key) is True:
                reasons.append("rate-limit evasion is refused")
    return reasons


def _result(source_id: str | None, reasons: list[str]) -> dict:
    unique = list(dict.fromkeys(reasons))
    return {"id": source_id, "ok": not unique, "reasons": unique}


def _is_http_url(value) -> bool:
    if not isinstance(value, str):
        return False
    text = value.strip()
    lowered = text.lower()
    if not (lowered.startswith("https://") or lowered.startswith("http://")):
        return False
    if any(char.isspace() for char in text):
        return False
    return not _url_has_userinfo(text)


def _url_has_userinfo(value) -> bool:
    if not isinstance(value, str) or "://" not in value:
        return False
    host = value.split("://", 1)[1].split("/", 1)[0]
    return "@" in host


def _positive_number(value) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool) and value > 0


def _positive_int(value) -> bool:
    return isinstance(value, int) and not isinstance(value, bool) and value > 0


def summarize(results: list[dict]) -> dict:
    accepted = [item["id"] for item in results if item["ok"]]
    rejected = [item for item in results if not item["ok"]]
    return {
        "accepted": len(accepted),
        "rejected": len(rejected),
        "accepted_ids": accepted,
        "rejected_ids": [item["id"] for item in rejected],
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Check a SHEPHERD allowlist offline.")
    parser.add_argument("path", nargs="?", type=Path, default=default_allowlist_path())
    parser.add_argument("--report", action="store_true", help="Print accepted and rejected counts.")
    args = parser.parse_args(argv)
    document = load_document(args.path)
    results = check_document(document)
    summary = summarize(results)
    if args.report:
        print(json.dumps(summary, indent=2))
    else:
        for item in results:
            if item["ok"]:
                print(f"PASS {item['id']}")
            else:
                print(f"FAIL {item['id']}: {'; '.join(item['reasons'])}")
        print(f"accepted {summary['accepted']} rejected {summary['rejected']}")
    return 0 if summary["rejected"] == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
