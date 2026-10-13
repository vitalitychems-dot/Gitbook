#!/usr/bin/env python3
"""Mesh bus: one append-only JSONL file of typed envelopes (proposed Gitbook mesh/bus/YYYY-MM-DD.jsonl).
usage: bus.py validate FILE | digest FILE [--lane L]"""
import json, sys, re, collections
LANES = {"tessera", "command-center", "mesh-cloud", "security", "build", "moderator", "cordnation", "rick", "father", "all"}
KINDS = {"claim", "release", "handoff", "ask", "result", "gate", "block", "note"}
GATES = ["moderator", "tessera", "security", "build", "father"]
REQ = ("id", "ts", "from", "to", "kind", "ref", "body")
def check(m, seen):
    e = [f"missing {k}" for k in REQ if k not in m]
    if e: return e
    if m["from"] not in LANES or m["from"] == "all": e.append("bad from")
    if any(t not in LANES for t in (m["to"] if isinstance(m["to"], list) else [m["to"]])): e.append("bad to")
    if m["kind"] not in KINDS: e.append("bad kind")
    if not re.fullmatch(r"\d{4}-\d\d-\d\dT\d\d:\d\d(:\d\d)?([+-]\d\d:\d\d|Z)", m["ts"]): e.append("ts needs zone")
    if m["id"] in seen: e.append("duplicate id")
    if m["kind"] == "gate" and (m.get("gate") not in GATES or m.get("verdict") not in ("PASS", "changes needed")): e.append("gate needs gate+verdict (gates never set BLOCKED)")
    if m["kind"] == "block" and m["from"] not in ("tessera", "father") and not m.get("owner"): e.append("only owner/tessera/father may block")
    if re.search(r"\d+(\.\d+)?\s*%", m["body"]) and not m.get("evidence"): e.append("% claim without evidence")
    if m["from"] != "tessera" and "father" in (m["to"] if isinstance(m["to"], list) else [m["to"]]) and not m.get("direct"): e.append("only tessera messages father")
    for d in m.get("needs", []):
        if d not in seen: e.append(f"needs unknown {d}")
    return e
def load(path):
    out, seen, errs = [], set(), []
    for n, line in enumerate(open(path), 1):
        if not line.strip(): continue
        try: m = json.loads(line)
        except json.JSONDecodeError: errs.append((n, ["not json"])); continue
        e = check(m, seen); seen.add(m.get("id")); out.append(m)
        if e: errs.append((n, e))
    return out, errs
def digest(msgs, lane=None):
    st = {}  # ref -> latest state
    for m in msgs:
        r = st.setdefault(m["ref"], {"ref": m["ref"], "owner": None, "gates": {}, "open_asks": 0, "last": m["ts"]})
        r["last"] = m["ts"]
        if m["kind"] == "claim": r["owner"] = m["from"]
        if m["kind"] == "release": r["owner"] = None
        if m["kind"] == "handoff": r["owner"] = m["to"]
        if m["kind"] == "gate": r["gates"][m["gate"]] = m["verdict"]
        if m["kind"] == "ask": r["open_asks"] += 1
        if m["kind"] == "result" and m.get("answers"): r["open_asks"] = max(0, r["open_asks"] - 1)
    rows = []
    for r in st.values():
        nxt = next((g for g in GATES if r["gates"].get(g) != "PASS"), "done")
        if lane and r["owner"] != lane and nxt != lane: continue
        rows.append(f'{r["ref"]}: owner={r["owner"]} next_gate={nxt} asks={r["open_asks"]} last={r["last"]}')
    return rows
if __name__ == "__main__":
    a = sys.argv[1:]
    if not a: print(__doc__); sys.exit(0)
    msgs, errs = load(a[1])
    if a[0] == "validate":
        for n, e in errs: print(f"line {n}: {'; '.join(e)}")
        print(f"{len(msgs)} msgs, {len(errs)} bad"); sys.exit(1 if errs else 0)
    print("\n".join(digest(msgs, a[3] if len(a) > 3 else None)))
