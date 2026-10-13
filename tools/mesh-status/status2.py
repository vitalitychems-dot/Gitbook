#!/usr/bin/env python3
"""status2: Rick's status.py plus improvements 4,5,15,18,19,20,21,23 and P2/P5 lint. Files only, no network, no model."""
import datetime as dt, json, pathlib, re, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import status as base
table, strip_links, DONE = base.table, base.strip_links, base.DONE
LEASE_S = 6 * 3600
EV = re.compile(r"\b[0-9a-f]{7,40}\b|PR #\d+|#\d+|pull/\d+")
NEEDS_EVIDENCE = {"in review", "tested locally", "stale"}

def lease_flags(tasks, now):
    out = []
    for t in tasks:
        if t.get("status") != "claimed" or t.get("pr"): continue
        try:
            ca = dt.datetime.fromisoformat(str(t.get("claimed_at")).replace("Z", "+00:00"))
            if ca.tzinfo is None: raise ValueError
        except Exception:
            out.append((t["id"], None, f"{t['id']} claim has bad/naive claimed_at {t.get('claimed_at')!r} -> fix")); continue
        age = (now - ca).total_seconds()
        if age > LEASE_S: out.append((t["id"], age, f"{t['id']} claim by {t.get('claimed_by')} is older than 6h with no PR -> re-queue"))
    return out

def release(tasks, now, log):
    """P3/I5: actually re-queue stale claims; append-only log."""
    for tid, age, _ in lease_flags(tasks, now):
        if age is None: continue
        t = next(x for x in tasks if x["id"] == tid)
        log.append({"at": now.isoformat(), "id": tid, "from": t["claimed_by"], "age_s": int(age), "event": "released"})
        t.update(status="queued", claimed_by=None, claimed_at=None)
    return tasks

def completeness(r):
    nxt = r.get("Next step (owner)", ""); st = r["State"].lower()
    return {"next": nxt not in ("", "—", "-"), "link": r.get("Link", "") not in ("", "—", "-"),
            "owner_in_next": "(" in nxt or r["Lane"] == "Father" or nxt.startswith("Same as") or "Father" in nxt,
            "evidence": r["Lane"] == "Father" or st not in NEEDS_EVIDENCE or bool(EV.search(" ".join([r["Id"], r["Where it was left"], r["Link"]])))}

def lane_lint(items, tasks, lanes):
    canon = set(lanes); alias = {a: c for c, al in lanes.items() for a in al}
    bad = []
    for r in items:
        for p in [x.strip() for x in re.sub(r"\([^)]*\)", "", strip_links(r["Lane"])).split(",")]:
            if p in ("none", "", "—"): bad.append((r["Id"], "no owner"))
            elif p in alias: bad.append((r["Id"], f"alias {p}->{alias[p]}"))
            elif p not in canon: bad.append((r["Id"], f"unknown lane {p}"))
    for t in tasks:
        if t["lane"] in alias: bad.append((t["id"], f"alias {t['lane']}"))
        elif t["lane"] not in canon: bad.append((t["id"], f"unknown lane {t['lane']}"))
    return bad

def gates(root, items):
    """23: gate column from gate files (mesh/gates/*.md 'ID: PASS|FAIL'), falling back to PASS/FAIL words in the row."""
    g = {}
    for f in sorted((root / "mesh/gates").glob("*.md")) if (root / "mesh/gates").exists() else []:
        for m in re.finditer(r"^([A-Z]+-\d{3}|PR #\d+):\s*(PASS|FAIL)", f.read_text(), re.M): g[m.group(1)] = m.group(2)
    for r in items:
        if r["Id"] not in g:
            w = re.findall(r"\b(PASS|FAIL)\b", r["Where it was left"])
            if w: g[r["Id"]] = "FAIL" if "FAIL" in w else "PASS"
    return g

def ledger(root, agents, today):
    p = root / "mesh/ledger/tokens.tsv"; tot = {}
    if p.exists():
        for ln in p.read_text().splitlines()[1:]:
            d, a, n = ln.split("\t")[:3]
            if d == today: tot[a] = tot.get(a, 0) + int(n)
    return tot, sorted(set(agents) - set(tot))

def build(root, now, gitmesh=None):
    root = pathlib.Path(root)
    _, warn = base.build(root, now, gitmesh)
    warn = [w for w in warn if "older than 6h" not in w]
    h = (root / "mesh/HANDOFF.md").read_text(); items = table(h, "Id")
    arch = [r for f in sorted((root / "mesh/archive").glob("*/HANDOFF-done.md")) for r in table(f.read_text(), "Id")] if (root / "mesh/archive").exists() else []
    allstate = {r["Id"]: r["State"].lower() for r in items + arch}
    tasks = json.loads((root / "mesh/queue/TASKS.json").read_text())["tasks"]
    warn += [m for _, _, m in lease_flags(tasks, now)]
    # contradictions for every id family (Rick's checks GB-### only) and for rows already archived
    for t in tasks:
        if t["status"] in ("queued", "claimed"):
            for gid in sorted(set(re.findall(r"\b(?:GB|HYB|SITE)-\d{3}\b", t["title"]))):
                m = f"{t['id']} is '{t['status']}' but {gid} is '{allstate.get(gid)}' in HANDOFF.md -> close or re-scope"
                if allstate.get(gid) in DONE and m not in warn: warn.append(m)
    lanes = json.loads((root / "mesh/lanes.json").read_text()) if (root / "mesh/lanes.json").exists() else None
    g = gates(root, items)
    rep = [r["Id"] for r in items if "REPORTED" in " ".join(r.values())]
    comp = {r["Id"]: [k for k, v in completeness(r).items() if not v] for r in items if r["State"].lower() not in DONE}
    ownerless = [r for r in items if strip_links(r["Lane"]).strip() in ("none", "") and r["State"].lower() not in DONE]
    out = [f"# Mesh status\n\nBuilt {now.strftime('%Y-%m-%d %H:%M')} CT by status2.py from files only (0 model tokens).\n",
           f"REPORTED rows: {len(rep)} of {len(items)} ({', '.join(rep)})  ",
           f"Complete open rows: {sum(not v for v in comp.values())} of {len(comp)}\n", "## Needs attention\n"]
    out += [f"- OWNERLESS {r['Id']}: {strip_links(r['Next step (owner)'])}" for r in ownerless]
    out += [f"- {w}" for w in warn] or ["- none"]
    out += [f"- {i}: incomplete ({', '.join(m)})" for i, m in comp.items() if m]
    if lanes is not None: out += [f"- lane lint {i}: {m}" for i, m in lane_lint(items, tasks, lanes)]
    agents = sorted(lanes) if lanes else []
    tot, missing = ledger(root, agents, now.strftime("%Y-%m-%d"))
    out.append("\n## Lanes: doing and next\n\n| Lane | Item | State | Gate | Next |\n|---|---|---|---|---|")
    for r in sorted(items, key=lambda r: (strip_links(r["Lane"]) not in ("none",), strip_links(r["Lane"]))):
        if r["State"].lower() not in DONE:
            out.append(f"| {strip_links(r['Lane'])} | {r['Id']} | {r['State']} | {g.get(r['Id'], '')} | {strip_links(r['Next step (owner)'])} |")
    out.append("\n## Queue\n\n| Task | Lane | Status | Title |\n|---|---|---|---|")
    out += [f"| {t['id']} | {t['lane']} | {t['status']} | {t['title'][:90]} |" for t in tasks]
    out.append("\n## Token ledger (today)\n"); out += [f"- {a}: {n}" + (" OVER CAP" if n > 20000 else "") for a, n in sorted(tot.items())] or ["- no entries"]
    if missing: out.append(f"- no ledger line today: {', '.join(missing)}")
    done = [r for r in items if r["State"].lower() in DONE]
    out.append("\n## Can be cleaned up\n")
    out += [f"- {r['Id']}: done with next 'none' -> archive" for r in done if r["Next step (owner)"].strip().lower() == "none"]
    out += [f"- {r['Id']}: stale -> {strip_links(r['Next step (owner)'])}" for r in items if r["State"].lower() == "stale"]
    return "\n".join(out) + "\n", warn

if __name__ == "__main__":
    import argparse; a = argparse.ArgumentParser(); a.add_argument("root"); a.add_argument("--now"); a.add_argument("--out"); a.add_argument("--gitmesh")
    o = a.parse_args(); now = dt.datetime.fromisoformat(o.now) if o.now else dt.datetime.now().astimezone()
    t, _ = build(o.root, now, o.gitmesh); p = pathlib.Path(o.out or pathlib.Path(o.root) / "mesh/STATUS.md"); p.write_text(t); print(t)
