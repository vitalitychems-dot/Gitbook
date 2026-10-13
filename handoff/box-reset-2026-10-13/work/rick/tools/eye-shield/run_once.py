#!/usr/bin/env python3
"""Run Eye Shield once against the real box (defensive, read-only)."""
from __future__ import annotations
import argparse, json, sys
from pathlib import Path

from feeds_loader import ThreatFeeds
from detector import (
    scan_log_file, scan_log_text, scan_log_file_all, scan_all,
    discover_logs, listening_ports,
    remote_peers_from_proc, Finding,
)
from anomaly import AnomalyScorer
from alert import findings_to_alerts, append_bus, write_eye_layer

HERE = Path(__file__).resolve().parent
OUT = HERE / "out"

def enrich(findings: list[Finding], feeds: ThreatFeeds) -> list[dict]:
    out = []
    for f in findings:
        d = f.to_dict()
        prior = list(d.get("feed_hits") or [])  # may hold signature tool tags
        if f.ip:
            intel = feeds.match_ip(f.ip)
            # keep tool tags + threat-intel source names, de-duped
            merged = list(dict.fromkeys(prior + intel))
            d["feed_hits"] = merged
            d["tool_tags"] = prior
            d["intel_hits"] = intel
            asn = feeds.lookup_asn(f.ip)
            d["asn"] = asn.get("asn")
            d["country"] = asn.get("country")
            if intel and d["severity"] in ("low", "medium"):
                d["severity"] = "high"
        out.append(d)
    return out

def peer_feed_findings(feeds: ThreatFeeds) -> list[Finding]:
    findings = []
    for ip in remote_peers_from_proc():
        hits = feeds.match_ip(ip)
        if hits:
            findings.append(Finding(
                kind="threat_feed_peer",
                ip=ip,
                detail=f"established peer matches feeds: {','.join(hits)}",
                source="/proc/net/tcp",
                feed_hits=hits,
                pattern="threat_intel_match",
                severity="high",
            ))
    return findings

def main(argv=None):
    ap = argparse.ArgumentParser(description="Eye Shield defensive scan (once)")
    ap.add_argument("--fixtures", action="store_true", help="also scan fixtures/")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args(argv)

    feeds = ThreatFeeds()
    from signatures.matcher import SignatureMatcher
    sigm = SignatureMatcher()
    findings: list[Finding] = []

    logs = discover_logs()
    for path in logs:
        findings.extend(scan_log_file_all(path))

    if args.fixtures:
        for p in sorted((HERE / "fixtures").glob("*.log")):
            findings.extend(scan_log_file_all(p))

    findings.extend(peer_feed_findings(feeds))

    ports = listening_ports()
    # Flag unexpected world-facing listeners (informational)
    for row in ports:
        local = row.get("local") or ""
        if local.startswith("0.0.0.0:") or local.startswith("[::]:"):
            port = local.rsplit(":", 1)[-1]
            if port not in ("22", "80", "443"):  # common; still report all 0.0.0.0
                findings.append(Finding(
                    "listening_port", None,
                    f"world-facing listener {local} {row.get('process','')}",
                    "ss -tlnp", pattern="new_or_open_listener", severity="info",
                ))

    enriched = enrich(findings, feeds)

    scorer = AnomalyScorer()
    # seed a quiet baseline then score current
    scorer.update(0)
    scorer.update(0)
    kinds = {}
    for f in enriched:
        kinds[f["kind"]] = kinds.get(f["kind"], 0) + 1
    # count only attack-like for anomaly (exclude info listening_port noise partially)
    attackish = sum(1 for f in enriched if f["severity"] in ("medium", "high", "critical"))
    anomaly = scorer.update(attackish, kinds)

    OUT.mkdir(exist_ok=True)
    report = {
        "feeds": feeds.stats(),
        "signatures": sigm.stats(),
        "logs_scanned": [str(p) for p in logs],
        "findings": enriched,
        "anomaly": anomaly,
        "listening_ports": ports,
        "defensive_only": True,
    }
    (OUT / "last_scan.json").write_text(json.dumps(report, indent=2))
    layer_path = write_eye_layer(enriched, anomaly, ports)
    msgs = findings_to_alerts(enriched, anomaly)
    bus_path = append_bus(msgs)

    if args.json:
        print(json.dumps(report, indent=2))
    else:
        print(f"Eye Shield scan complete")
        print(f"  logs: {logs or '(none readable)'}")
        print(f"  findings: {len(enriched)}")
        print(f"  anomaly: {anomaly}")
        print(f"  feeds: {feeds.stats()}")
        print(f"  signatures: {sigm.stats()}")
        print(f"  layer: {layer_path}")
        print(f"  bus: {bus_path} (+{len(msgs)} msgs)")
        for f in enriched:
            if f["severity"] in ("high", "critical", "medium"):
                print(f"  [{f['severity']}] {f['kind']} ip={f.get('ip')} feeds={f.get('feed_hits')} asn={f.get('asn')}/{f.get('country')} :: {f['detail'][:100]}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
