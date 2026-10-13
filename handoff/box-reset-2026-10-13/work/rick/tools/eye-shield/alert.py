"""Post Eye Shield alerts as mesh bus messages + Eye layer JSON."""
from __future__ import annotations
import json, uuid
from datetime import datetime, timezone, timedelta
from pathlib import Path

CT = timezone(timedelta(hours=-5))
HERE = Path(__file__).resolve().parent
OUT = HERE / "out"
BUS = HERE.parent / "collab" / "eye-shield-bus.jsonl"
EYE_LAYER = HERE / "out" / "eye-shield-layer.json"

def _now_iso() -> str:
    return datetime.now(CT).strftime("%Y-%m-%dT%H:%M:%S-05:00")

def bus_message(kind: str, body: str, ref: str = "eye-shield", to: str = "security", extra: dict | None = None) -> dict:
    msg = {
        "id": f"es-{uuid.uuid4().hex[:10]}",
        "ts": _now_iso(),
        "from": "rick",
        "to": to,
        "kind": kind,
        "ref": ref,
        "body": body,
        "paths": ["tools/eye-shield"],
    }
    if extra:
        msg["extra"] = extra
    return msg

def append_bus(msgs: list[dict], path: Path | None = None) -> Path:
    path = path or BUS
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a") as f:
        for m in msgs:
            f.write(json.dumps(m, ensure_ascii=False) + "\n")
    return path

def write_eye_layer(findings: list[dict], anomaly: dict, ports: list[dict], path: Path | None = None) -> Path:
    """Layer file Tessera's Eye can ingest: points + alerts + anomaly score."""
    path = path or EYE_LAYER
    path.parent.mkdir(parents=True, exist_ok=True)
    points = []
    for f in findings:
        if not f.get("ip"):
            continue
        points.append({
            "type": "threat_ip",
            "ip": f["ip"],
            "kind": f["kind"],
            "severity": f["severity"],
            "country": f.get("country"),
            "asn": f.get("asn"),
            "feeds": f.get("feed_hits") or [],
            "detail": f.get("detail"),
        })
    layer = {
        "name": "Eye Shield",
        "version": 1,
        "updated": _now_iso(),
        "anomaly": anomaly,
        "listening_ports": ports,
        "findings_count": len(findings),
        "points": points,
        "findings": findings,
        "defensive_only": True,
    }
    path.write_text(json.dumps(layer, indent=2))
    return path

def findings_to_alerts(findings: list[dict], anomaly: dict) -> list[dict]:
    msgs = []
    high = [f for f in findings if f.get("severity") in ("high", "critical")]
    if high:
        summary = "; ".join(f"{f['kind']}@{f.get('ip') or '?'}" for f in high[:8])
        msgs.append(bus_message(
            "alert",
            f"Eye Shield: {len(high)} high/critical finding(s): {summary}",
            extra={"count": len(high), "anomaly": anomaly},
        ))
    surv = [f for f in findings if str(f.get("kind", "")).startswith("sig:")
            and f.get("severity") in ("high", "critical", "medium")]
    if surv:
        tools = sorted({(f.get("tool_tags") or f.get("feed_hits") or ["?"])[0] for f in surv})
        ips = sorted({f["ip"] for f in surv if f.get("ip")})
        msgs.append(bus_message(
            "alert",
            f"Eye Shield anti-surveillance: {len(surv)} signature hit(s) "
            f"tools={','.join(tools[:10])} ips={','.join(ips[:10])}",
            to="security",
            ref="eye-shield-antisurveillance",
            extra={"count": len(surv), "tools": tools, "ips": ips,
                   "patterns": [f.get("pattern") for f in surv[:20]]},
        ))
    if anomaly.get("warn"):
        msgs.append(bus_message(
            "warn",
            f"Eye Shield early warning: anomaly score {anomaly.get('score')} ({anomaly.get('level')}), "
            f"recent_events={anomaly.get('recent_events')}",
            to="father",
            extra={"anomaly": anomaly},
        ))
    if not msgs:
        msgs.append(bus_message(
            "note",
            f"Eye Shield scan clean: {len(findings)} finding(s), anomaly={anomaly.get('score')} ({anomaly.get('level')})",
            to="tessera",
        ))
    return msgs
