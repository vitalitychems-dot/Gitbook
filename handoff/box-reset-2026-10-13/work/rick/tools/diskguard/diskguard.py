#!/usr/bin/env python3
"""Disk guardian: read-only disk usage reporter. NEVER deletes anything."""
import argparse, json, os, shutil, subprocess, sys, time
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
THRESHOLDS = (95, 90, 85)
PROTECTED = ("ollama", "node22", "backups")  # toolchains/backups: never suggested for cleanup
LANE_HINTS = {"rea": "REA scan", "gitmesh": "GitMesh", "pubscan": "public-repo scan",
              "gb06": "GB work", "sec": "Security", "build": "Build", "backup": "backups",
              "ollama": "local model", "rick": "Rick", "tess": "Tessera", "qlab": "Rick/qlab",
              "historical": "Historical Analysis", "hyb": "Historical Analysis", "mesh": "Mesh Cloud"}

def warn_level(pct):
    for t in THRESHOLDS:
        if pct >= t:
            return t
    return None

def scan_dir(path):
    """Return (bytes, newest_mtime) walking without following symlinks."""
    total, newest = 0, 0.0
    stack = [path]
    while stack:
        d = stack.pop()
        try:
            st = os.lstat(d); newest = max(newest, st.st_mtime)
            with os.scandir(d) as it:
                for e in it:
                    try:
                        s = e.stat(follow_symlinks=False)
                    except OSError:
                        continue
                    newest = max(newest, s.st_mtime)
                    if e.is_dir(follow_symlinks=False):
                        stack.append(e.path)
                    else:
                        total += getattr(s, "st_blocks", 0) * 512 or s.st_size
        except OSError:
            continue
    return total, newest

def git(path, *args):
    try:
        r = subprocess.run(["git", "-C", path, *args], capture_output=True, text=True, timeout=15)
        return r.stdout.strip() if r.returncode == 0 else None
    except Exception:
        return None

def git_info(path):
    if not os.path.isdir(os.path.join(path, ".git")):
        return None
    remote = git(path, "remote", "get-url", "origin")
    dirty = git(path, "status", "--porcelain")
    unpushed = git(path, "log", "--branches", "--not", "--remotes", "--oneline")
    return {"remote": remote, "clean": dirty == "", "pushed": unpushed == ""}

def guess(path, gi):
    low = path.lower()
    owner = next((v for k, v in LANE_HINTS.items() if k in low), "unknown")
    lane = os.path.basename(path)
    if gi and gi.get("remote"):
        lane = gi["remote"].rstrip("/").split("/")[-1].removesuffix(".git")
    return owner, lane

def human(n):
    for u in ("B", "K", "M", "G", "T"):
        if n < 1024 or u == "T":
            return f"{n:.1f}{u}" if u != "B" else f"{n}B"
        n /= 1024

def collect(roots, stale_hours, top, now=None):
    now = now or time.time()
    rows = []
    for root in roots:
        try:
            entries = [e for e in os.scandir(root) if e.is_dir(follow_symlinks=False)]
        except OSError:
            continue
        for e in entries:
            size, newest = scan_dir(e.path)
            gi = git_info(e.path)
            owner, lane = guess(e.path, gi)
            age_h = (now - newest) / 3600 if newest else None
            reasons = []
            if age_h is not None and age_h >= stale_hours:
                reasons.append(f"no writes for {age_h:.1f}h")
            if gi and gi["clean"] and gi["pushed"]:
                reasons.append("git clone clean and fully pushed")
            protected = any(k in e.name.lower() for k in PROTECTED)
            if protected:
                reasons = [f"PROTECTED (toolchain/backup), {r}" for r in reasons]
            rows.append({"path": e.path, "bytes": size, "size": human(size),
                         "last_write": datetime.fromtimestamp(newest).strftime("%Y-%m-%d %H:%M") if newest else None,
                         "age_hours": round(age_h, 2) if age_h is not None else None,
                         "owner_guess": owner, "lane_guess": lane, "git": gi,
                         "finished": bool(reasons) and not protected, "protected": protected, "reasons": reasons})
    rows.sort(key=lambda r: r["bytes"], reverse=True)
    return rows[:top]

def history_update(hist_path, used, total, now):
    entries = []
    if os.path.exists(hist_path):
        with open(hist_path) as f:
            entries = [json.loads(l) for l in f if l.strip()]
    entries.append({"ts": now, "used": used, "total": total})
    with open(hist_path, "a") as f:
        f.write(json.dumps(entries[-1]) + "\n")
    return growth(entries)

def growth(entries, window_h=24):
    """Bytes/hour over the last window, and hours until full (None if not growing)."""
    if len(entries) < 2:
        return None, None
    last = entries[-1]
    old = [e for e in entries if last["ts"] - e["ts"] <= window_h * 3600]
    first = old[0] if old[0] is not last else entries[-2]
    dt = (last["ts"] - first["ts"]) / 3600
    if dt <= 0:
        return None, None
    rate = (last["used"] - first["used"]) / dt
    eta = (last["total"] - last["used"]) / rate if rate > 0 else None
    return rate, eta

def render(d):
    L = [f"# Disk guardian report", f"Generated {d['generated']} (box time, CT). Read-only: nothing was deleted.", "",
         f"**Disk:** {human(d['used'])} used of {human(d['total'])} ({d['percent']:.1f}%), {human(d['free'])} free."]
    if d["warning"]:
        L.append(f"\n> ⚠️ **WARNING: disk at or above {d['warning']}%.**")
    r, e = d["growth_bytes_per_hour"], d["hours_until_full"]
    L.append(f"\n**Growth:** {('%s/hour' % human(abs(r)) + (' shrinking' if r < 0 else '')) if r is not None else 'need 2+ history points'}; "
             f"**hours until full:** {f'{e:.1f}' if e is not None else 'n/a (not growing or no data)'}.")
    L += ["", "## Top folders", "", "| Size | Path | Last write | Owner (guess) | Lane (guess) | Finished? |", "|---|---|---|---|---|---|"]
    for x in d["folders"]:
        L.append(f"| {x['size']} | `{x['path']}` | {x['last_write']} | {x['owner_guess']} | {x['lane_guess']} | {'; '.join(x['reasons']) or '—'} |")
    fin = [x for x in d["folders"] if x["finished"]]
    L += ["", "## Suggested cleanup (owners only, after confirming)", "",
          "Diskguard never deletes. Owners: check the folder is yours and finished, then run:", ""]
    for x in fin:
        L.append(f"- {x['size']} — `rm -rf -- '{x['path']}'`  ({'; '.join(x['reasons'])})")
    if not fin:
        L.append("- No folders look finished.")
    return "\n".join(L) + "\n"

def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--roots", nargs="+", default=["/workspace", "/tmp"])
    p.add_argument("--disk", default="/workspace")
    p.add_argument("--stale-hours", type=float, default=6)
    p.add_argument("--top", type=int, default=20)
    p.add_argument("--report", default=os.path.join(HERE, "REPORT.md"))
    p.add_argument("--history", default=os.path.join(HERE, "history.jsonl"))
    p.add_argument("--json", action="store_true")
    a = p.parse_args(argv)
    now = time.time()
    du = shutil.disk_usage(a.disk)
    pct = du.used / du.total * 100
    rate, eta = history_update(a.history, du.used, du.total, now)
    d = {"generated": datetime.fromtimestamp(now).strftime("%Y-%m-%d %H:%M"), "total": du.total, "used": du.used,
         "free": du.free, "percent": round(pct, 2), "warning": warn_level(pct),
         "growth_bytes_per_hour": rate, "hours_until_full": eta,
         "folders": collect(a.roots, a.stale_hours, a.top, now)}
    with open(a.report, "w") as f:
        f.write(render(d))
    print(json.dumps(d, indent=2) if a.json else render(d))
    return 2 if d["warning"] else 0

if __name__ == "__main__":
    sys.exit(main())
