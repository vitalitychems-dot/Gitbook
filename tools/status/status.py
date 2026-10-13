#!/usr/bin/env python3
"""Build mesh/STATUS.md from repo files only. No model calls, no network.

usage: status.py ROOT [--now 2026-10-13T15:00-05:00] [--out ROOT/mesh/STATUS.md] [--gitmesh PATH]
Reads: mesh/HANDOFF.md (table), mesh/queue/TASKS.json, intake/log.md, optional GitMesh checkout.
"""
import argparse, datetime as dt, json, pathlib, re, sys

class _Done(set):
    """Done states; a qualified state like 'published: merged without passing gates' counts by its prefix."""
    def __contains__(self, s): return set.__contains__(self, str(s).split(":")[0].strip())
DONE = _Done({"published", "done", "merged"})
ACTIVE = {"in review", "tested locally", "open", "ready", "claimed", "launched", "running", "in_review"}
WAIT = {"held", "blocked", "stale", "unclaimed", "conflicted", "queued"}

def table(md, first_col):
    rows, hdr = [], None
    for ln in md.splitlines():
        if not ln.startswith("|"): continue
        cells = [c.strip() for c in ln.strip().strip("|").split("|")]
        if cells and cells[0] == first_col: hdr = cells; continue
        if hdr and set(cells[0]) <= set("-: "): continue
        if hdr and len(cells) >= len(hdr): rows.append(dict(zip(hdr, cells)))
    return rows

def strip_links(s): return re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", s)

def gitmesh_drift(gitmesh):
    """Return (folders missing from index, index entries with no folder)."""
    gm = pathlib.Path(gitmesh)
    idx = {p["path"] for p in json.loads((gm / "mesh/index.json").read_text())["projects"]}
    dirs = {f"projects/{d.name}" for d in (gm / "projects").iterdir() if d.is_dir()}
    return sorted(dirs - idx), sorted(idx - dirs)

def build(root, now, gitmesh=None):
    root = pathlib.Path(root); out, warn = [], []
    h = (root / "mesh/HANDOFF.md").read_text()
    asof = re.search(r"\*\*As of:\*\*\s*([0-9-]+)", h)
    items = table(h, "Id")
    q = json.loads((root / "mesh/queue/TASKS.json").read_text())["tasks"]
    log = (root / "intake/log.md").read_text() if (root / "intake/log.md").exists() else ""
    log_rows = table(log, "ID")
    state = {r["Id"]: r["State"].lower() for r in items}

    # staleness of the handoff page itself
    if asof:
        age = (now.date() - dt.date.fromisoformat(asof.group(1))).days
        if age >= 1: warn.append(f"HANDOFF.md 'As of' is {age} day(s) old ({asof.group(1)})")
    # queue tasks that point at items the handoff already marks done
    for t in q:
        if t["status"] in ("queued", "claimed"):
            for gid in sorted(set(re.findall(r"GB-\d{3}", t["title"]))):
                if state.get(gid) in DONE:
                    warn.append(f"{t['id']} is '{t['status']}' but {gid} is '{state[gid]}' in HANDOFF.md -> close or re-scope")
        if t["status"] == "claimed" and t.get("claimed_at"):
            try:
                ca = dt.datetime.fromisoformat(t["claimed_at"].replace("Z", "+00:00"))
                if ca.tzinfo is None: raise ValueError("no timezone")
            except ValueError as e:
                warn.append(f"{t['id']} has an unreadable claimed_at '{t['claimed_at']}' ({e}) -> fix the timestamp"); continue
            if (now - ca).total_seconds() > 6 * 3600 and not t.get("pr"):
                warn.append(f"{t['id']} claim by {t['claimed_by']} is older than 6h with no PR -> re-queue")
    # handoff rows missing parts
    for r in items:
        miss = [k for k in ("Lane", "Next step (owner)", "Link") if r.get(k, "").strip() in ("", "—", "-")]
        if miss and r["State"].lower() not in DONE: warn.append(f"{r['Id']}: missing {', '.join(miss)}")
    # log vs handoff disagreement
    logstate = {r["ID"]: r["Status"].lower() for r in log_rows}
    for gid, s in state.items():
        if gid in logstate and (s in DONE) != (logstate[gid] in DONE):
            warn.append(f"{gid}: HANDOFF says '{s}', intake log says '{logstate[gid]}'")
    # GitMesh index drift
    if gitmesh:
        extra, missing = gitmesh_drift(gitmesh)
        for d in extra: warn.append(f"GitMesh: {d} exists but is not in mesh/index.json")
        for d in missing: warn.append(f"GitMesh: index lists {d} but the folder is missing")

    lanes = {}
    for r in items:
        lanes.setdefault(strip_links(r["Lane"]), []).append(r)
    out.append(f"# Mesh status\n\nBuilt {now.strftime('%Y-%m-%d %H:%M')} CT by status.py from files only (0 model tokens). Source: HANDOFF.md as of {asof.group(1) if asof else '?'}, TASKS.json, intake/log.md.\n")
    out.append("## Needs attention\n"); out += [f"- {w}" for w in warn] or ["- none"]
    out.append("\n## By lane: doing and next\n\n| Lane | Item | State | Next | Link |\n|---|---|---|---|---|")
    for lane in sorted(lanes):
        for r in lanes[lane]:
            if r["State"].lower() not in DONE:
                out.append(f"| {lane} | {r['Id']} | {r['State']} | {strip_links(r['Next step (owner)'])} | {r.get('Link', '')} |")
    out.append("\n## Queue (mesh/queue/TASKS.json)\n\n| Task | Lane | Status | Title |\n|---|---|---|---|")
    for t in q:
        out.append(f"| {t['id']} | {t['lane']} | {t['status']} | {t['title'][:90]} |")
    done = [r for r in items if r["State"].lower() in DONE]
    out.append("\n## Done\n"); out += [f"- {r['Id']} ({strip_links(r['Lane'])}): {strip_links(r['Where it was left'])[:100]}" + (f" ({r['Link']})" if r.get('Link', '').strip() not in ('', '—', '-') else '') for r in done]
    out.append("\n## Can be cleaned up\n")
    clean = [f"- {r['Id']}: done with next step 'none' -> move line to archive" for r in done if r["Next step (owner)"].strip().lower() == "none"]
    clean += [f"- {r['Id']}: stale -> {strip_links(r['Next step (owner)'])}" for r in items if r["State"].lower() == "stale"]
    out += clean or ["- none"]
    return "\n".join(out) + "\n", warn

if __name__ == "__main__":
    a = argparse.ArgumentParser(); a.add_argument("root"); a.add_argument("--now"); a.add_argument("--out"); a.add_argument("--gitmesh"); a.add_argument("--drift-only", action="store_true")
    o = a.parse_args()
    if o.drift_only:
        extra, missing = gitmesh_drift(o.gitmesh or o.root)
        print(json.dumps({"not_in_index": extra, "missing_folder": missing})); sys.exit(1 if extra or missing else 0)
    now = dt.datetime.fromisoformat(o.now) if o.now else dt.datetime.now().astimezone()
    text, _ = build(o.root, now, o.gitmesh)
    p = pathlib.Path(o.out or pathlib.Path(o.root) / "mesh/STATUS.md"); p.write_text(text); print(text)
