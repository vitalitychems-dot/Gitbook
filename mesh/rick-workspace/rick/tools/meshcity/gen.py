#!/usr/bin/env python3
"""Mesh City generator: builds city.json from real local data (read-only, stdlib)."""
import json, os, re, subprocess, sys, hashlib
W = "/workspace"
AGENTS = {  # name -> (workspace dir prefixes it plausibly owns, mention regex)
 "Tessera": (["TESSERA-ro"], r"tessera"),
 "Command Center": (["command-center"], r"command[ -]center"),
 "Mesh Cloud": (["mesh-cloud", "gitmesh"], r"mesh[ -]cloud"),
 "Security": (["security"], r"\bsecurity\b"),
 "Build": (["build-gate", "build-o", "build-plan-2026-10-12"], r"\bbuild\b"),
 "Gitbook Moderator": (["moderator-tools"], r"moderator"),
 "Gitbook Cordnation": (["gitbook-cordnation"], r"cordnation"),
 "Rick": (["rick"], r"\brick\b"),
}
TEXT = (".md", ".txt", ".ts", ".py", ".json", ".mjs", ".js")
def count_files(d, cap=20000):
    n = 0
    for _, _, fs in os.walk(d):
        n += len(fs)
        if n >= cap: return cap
    return n
def mentions(rx, roots, cap_files=3000):
    r = re.compile(rx, re.I); hits = 0; seen = 0
    for root in roots:
        for dp, dn, fs in os.walk(root):
            dn[:] = sorted(x for x in dn if x not in (".git", "node_modules", "__pycache__"))
            for f in sorted(fs):
                if not f.endswith(TEXT): continue
                seen += 1
                if seen > cap_files: return hits
                try:
                    with open(os.path.join(dp, f), errors="ignore") as fh:
                        if r.search(fh.read(200000)): hits += 1
                except OSError: pass
    return hits
def run_json(cmd):
    try: return json.loads(subprocess.run(cmd, capture_output=True, text=True, timeout=120).stdout)
    except Exception: return None
def run_lines(cmd):
    try: return subprocess.run(cmd, capture_output=True, text=True, timeout=120).stdout
    except Exception: return ""
def build(disk=None, rooms_text=None, now=None):
    mroots = [p for p in (f"{W}/TESSERA-ro", f"{W}/gitbook-gate-1e3bb50", f"{W}/rick") if os.path.isdir(p)]
    buildings = []
    for i, (name, (dirs, rx)) in enumerate(AGENTS.items()):
        owned = [d for d in dirs if os.path.isdir(f"{W}/{d}")]
        files = sum(count_files(f"{W}/{d}") for d in owned)
        m = mentions(rx, mroots)
        buildings.append({"id": "agent:" + name, "kind": "agent", "name": name,
            "files": files if owned else None, "owned_dirs": owned, "mentions": m,
            "unknown": [] if owned else ["owned files: no local dir found"],
            "height": round(2 + min(30, (files or 0) ** 0.4 + m ** 0.5), 2)})
    for base, kind in ((f"{W}/rick/tools", "workshop"),):
        for t in sorted(os.listdir(base)) if os.path.isdir(base) else []:
            p = f"{base}/{t}"
            if os.path.isdir(p):
                f = count_files(p); buildings.append({"id": "tool:" + t, "kind": "workshop", "name": t,
                    "files": f, "path": p, "height": round(1.5 + f ** 0.6, 2)})
    q = f"{W}/rick/qlab"
    if os.path.isdir(q):
        f = count_files(q); buildings.append({"id": "tool:qlab", "kind": "workshop", "name": "qlab",
            "files": f, "path": q, "height": round(1.5 + f ** 0.6, 2)})
    if rooms_text is None:
        rooms_text = run_lines([sys.executable, f"{W}/rick/tools/palace/palace.py", "rooms"])
    for line in rooms_text.splitlines():
        mm = re.match(r"\s*(\d+)\s+(\S+)", line)
        if mm:
            n = int(mm.group(1)); buildings.append({"id": "room:" + mm.group(2), "kind": "library",
                "name": mm.group(2), "docs": n, "height": round(1 + n ** 0.5, 2)})
    if disk is None:
        disk = run_json([sys.executable, f"{W}/rick/tools/diskguard/diskguard.py", "--json"]) or {}
    pct = disk.get("percent")
    ground = {"percent": pct, "free_bytes": disk.get("free"), "generated": disk.get("generated"),
              "level": "unknown" if pct is None else ("red" if pct >= 95 else "amber" if pct >= 90 else "green")}
    # deterministic layout: grid per district
    off = {"agent": (0, 0), "workshop": (0, 14), "library": (14, 0)}
    cnt = {}
    for b in buildings:
        k = cnt.get(b["kind"], 0); cnt[b["kind"]] = k + 1
        ox, oz = off[b["kind"]]; b["x"] = ox + (k % 4) * 3; b["z"] = oz + (k // 4) * 3
    return {"schema": "meshcity/1", "ground": ground, "buildings": buildings}
def dumps(c): return json.dumps(c, indent=1, sort_keys=True)
if __name__ == "__main__":
    c = build(); s = dumps(c)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "city.json")
    open(out, "w").write(s)
    # embed into html
    h = os.path.join(os.path.dirname(out), "index.html")
    if os.path.exists(h):
        t = open(h).read()
        t = re.sub(r"(<script id=\"city\" type=\"application/json\">).*?(</script>)",
                   lambda m: m.group(1) + s.replace("</", "<\\/") + m.group(2), t, flags=re.S)
        open(h, "w").write(t)
    print(f"buildings={len(c['buildings'])} ground={c['ground']['level']} sha={hashlib.sha256(s.encode()).hexdigest()[:12]}")
