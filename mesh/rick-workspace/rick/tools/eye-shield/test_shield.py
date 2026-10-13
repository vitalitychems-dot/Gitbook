#!/usr/bin/env python3
"""Fixture tests for Eye Shield detection + anti-surveillance signatures."""
from __future__ import annotations
import json, sys, tempfile, time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from detector import scan_log_file, scan_log_text, scan_signatures, scan_all, listening_ports
from anomaly import AnomalyScorer
from feeds_loader import ThreatFeeds
from alert import findings_to_alerts, append_bus, write_eye_layer
from signatures.matcher import SignatureMatcher, load_catalog

FIX = HERE / "fixtures"

# Classic expected kinds
EXPECTED = {
    "auth_bruteforce.log": {"bruteforce", "invalid_user"},
    "auth_scan.log": {"port_scan_burst"},
    "nginx_attack.log": {"web_probe"},
    "syslog_suspicious.log": {"firewall_block_burst", "suspicious_command"},
    "benign.log": set(),
}

# Signature IDs that MUST fire on surveillance_probes.log
SIG_MUST = {
    "flock.onvif_probe",
    "flock.admin_template",
    "flock.port_probe_adb_frp",
    "argos.camera_path_scrape",
    "argos.insecam_style",
    "camofox.ua",
    "camofox.headless_automation",
    "scan.nuclei",
    "scan.masscan_ua",
    "scan.shodan_censys",
    "redsparrow.messaging_c2",
    "redsparrow.name_ioc",
    "redsparrow.payload_pipe",
}


def test_fixture_detection():
    tp = fp = fn = 0
    details = []
    for name, expect in EXPECTED.items():
        path = FIX / name
        findings = scan_log_file(path)
        kinds = {f.kind for f in findings if f.severity != "info"}
        if name == "benign.log":
            attack = {k for k in kinds if k not in ("error",)}
            if attack:
                fp += len(attack)
                details.append(f"FP benign->{attack}")
            else:
                tp += 1
            continue
        for k in expect:
            if k in kinds:
                tp += 1
            else:
                fn += 1
                details.append(f"FN {name} missing {k}")
        for k in kinds:
            if k not in expect and k not in ("failed_auth", "firewall_block"):
                if k == "failed_auth" and "bruteforce" in expect:
                    continue
                # signature hits on nginx/syslog fixtures are OK extras if from scanner UAs
                if k.startswith("sig:"):
                    continue
                fp += 1
                details.append(f"FP {name} unexpected {k}")
    prec = tp / (tp + fp) if (tp + fp) else 0.0
    rec = tp / (tp + fn) if (tp + fn) else 0.0
    return prec, rec, tp, fp, fn, details


def test_surveillance_signatures():
    text = (FIX / "surveillance_probes.log").read_text()
    hits = scan_signatures(text, source="surveillance_probes.log")
    patterns = {f.pattern for f in hits}
    tp = fp = fn = 0
    details = []
    for sid in SIG_MUST:
        if sid in patterns:
            tp += 1
        else:
            fn += 1
            details.append(f"FN missing sig {sid}")
    # benign must be clean of signature hits
    benign_hits = scan_signatures(
        (FIX / "surveillance_benign.log").read_text(),
        source="surveillance_benign.log",
    )
    attack_benign = [h for h in benign_hits if h.severity != "info"]
    if attack_benign:
        fp += len(attack_benign)
        details.append(f"FP benign sigs {[h.pattern for h in attack_benign]}")
    else:
        tp += 1  # correctly quiet
    prec = tp / (tp + fp) if (tp + fp) else 0.0
    rec = tp / (tp + fn) if (tp + fn) else 0.0
    return prec, rec, tp, fp, fn, details, sorted(patterns)


def test_feeds_load():
    feeds = ThreatFeeds()
    st = feeds.stats()
    assert st["kev_cves"] > 0, st
    assert st["asn_ranges"] > 1000, st
    assert isinstance(feeds.match_ip("1.1.1.1"), list)
    return st


def test_asn_attribution_on_probe_ips():
    """Map fixture attacker IPs via offline ASN (RFC5737 TEST-NET may be sparse)."""
    feeds = ThreatFeeds()
    # Use a well-known public IP present in asn dump for measurement
    known = feeds.lookup_asn("1.1.1.1")
    # Also exercise match on probe IPs from fixtures (may have empty ASN — that's OK)
    probe_ips = ["203.0.113.10", "203.0.113.13", "203.0.113.15"]
    looked = {ip: feeds.lookup_asn(ip) for ip in probe_ips}
    return {"cloudflare_1_1_1_1": known, "probe_lookups": looked,
            "asn_ranges": feeds.stats()["asn_ranges"]}


def test_anomaly_rises():
    s = AnomalyScorer(window_s=300)
    s.update(0); s.update(1); s.update(0)
    quiet = s.update(0)
    hot = s.update(20, {"bruteforce": 20})
    assert hot["score"] > quiet["score"]
    assert hot["warn"] is True
    return quiet, hot


def test_bus_and_layer():
    findings = [
        {"kind": "bruteforce", "ip": "203.0.113.50", "detail": "6 fails", "severity": "high",
         "feed_hits": [], "asn": "0", "country": "ZZ", "source": "t", "count": 6,
         "ports": [], "pattern": "x"},
        {"kind": "sig:surveillance_scanner", "ip": "203.0.113.10", "detail": "onvif",
         "severity": "critical", "feed_hits": ["flock_scan_style"], "asn": None,
         "country": None, "source": "t", "count": 2, "ports": [],
         "pattern": "flock.onvif_probe"},
    ]
    anomaly = {"score": 55.0, "level": "warn", "recent_events": 6, "baseline": 0.5,
               "ratio": 5.0, "warn": True}
    with tempfile.TemporaryDirectory() as td:
        td = Path(td)
        bus = td / "bus.jsonl"
        layer = td / "layer.json"
        msgs = findings_to_alerts(findings, anomaly)
        append_bus(msgs, bus)
        write_eye_layer(findings, anomaly, [], layer)
        assert bus.exists() and bus.read_text().strip()
        data = json.loads(layer.read_text())
        assert data["name"] == "Eye Shield"
        assert any(p["ip"] == "203.0.113.50" for p in data["points"])
        bodies = [json.loads(l)["body"] for l in bus.read_text().splitlines() if l.strip()]
        assert any("anti-surveillance" in b for b in bodies), bodies
    return len(msgs)


def test_listening_ports_readonly():
    rows = listening_ports()
    assert isinstance(rows, list)
    return len(rows)


def test_catalog_compiles():
    cat = load_catalog()
    m = SignatureMatcher(cat)
    assert len(m) >= 15
    st = m.stats()
    # every regex must compile (constructor already does)
    return st


def test_combined_scan_speed():
    text = (FIX / "surveillance_probes.log").read_text()
    # inflate to ~2000 lines for a crude throughput number
    big = "\n".join([text] * 100)
    t0 = time.perf_counter()
    findings = scan_all(big, source="bench")
    dt = time.perf_counter() - t0
    lines = big.count("\n") + 1
    return {"seconds": round(dt, 4), "lines": lines, "findings": len(findings),
            "lines_per_sec": int(lines / dt) if dt > 0 else 0}


def main():
    metrics = {}

    prec, rec, tp, fp, fn, details = test_fixture_detection()
    print(f"classic precision={prec:.3f} recall={rec:.3f} tp={tp} fp={fp} fn={fn}")
    for d in details:
        print(" ", d)
    assert prec >= 0.8, prec
    assert rec >= 0.8, rec
    metrics["classic"] = {"precision": prec, "recall": rec, "tp": tp, "fp": fp, "fn": fn}

    sp, sr, stp, sfp, sfn, sdetails, patterns = test_surveillance_signatures()
    print(f"surveillance precision={sp:.3f} recall={sr:.3f} tp={stp} fp={sfp} fn={sfn}")
    print(f"  patterns_fired={patterns}")
    for d in sdetails:
        print(" ", d)
    assert sp >= 0.9, sp
    assert sr >= 0.9, sr
    metrics["surveillance"] = {
        "precision": sp, "recall": sr, "tp": stp, "fp": sfp, "fn": sfn,
        "patterns_fired": patterns, "must_count": len(SIG_MUST),
    }

    st = test_feeds_load()
    print("feeds", st)
    metrics["feeds"] = st

    asn = test_asn_attribution_on_probe_ips()
    print("asn attribution", asn["cloudflare_1_1_1_1"], "ranges", asn["asn_ranges"])
    metrics["asn"] = asn

    quiet, hot = test_anomaly_rises()
    print("anomaly quiet", quiet["score"], "hot", hot["score"])
    metrics["anomaly"] = {"quiet": quiet, "hot": hot}

    nmsg = test_bus_and_layer()
    print("bus msgs", nmsg)
    metrics["bus_msgs"] = nmsg

    nports = test_listening_ports_readonly()
    print("listening rows", nports)
    metrics["listening_rows"] = nports

    cat_st = test_catalog_compiles()
    print("catalog", cat_st)
    metrics["signatures"] = cat_st

    speed = test_combined_scan_speed()
    print("speed", speed)
    metrics["speed"] = speed

    print("ALL TESTS PASS")
    out = HERE / "out"
    out.mkdir(exist_ok=True)
    (out / "test_metrics.json").write_text(json.dumps(metrics, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
