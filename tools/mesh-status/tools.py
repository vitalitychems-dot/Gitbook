#!/usr/bin/env python3
"""Local implementations of improvements 6,9,10,11,12,13,14,16,17,18,24. Files only."""
import json, pathlib, re, difflib, datetime as dt, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent)); import status as base

def build_index(gm):  # 6
    gm = pathlib.Path(gm); p = gm / "mesh/index.json"; idx = json.loads(p.read_text())
    have = {x["path"]: x for x in idx["projects"]}; new = []
    for d in sorted(x for x in (gm / "projects").iterdir() if x.is_dir()):
        k = f"projects/{d.name}"
        if k in have: new.append(have[k]); continue
        rd = (d / "README.md").read_text().splitlines() if (d / "README.md").exists() else [d.name]
        first = next((l.lstrip("# ").strip() for l in rd if l.strip() and not l.startswith("#")), d.name)
        mjs = sorted(d.glob("*.mjs"))
        new.append({"name": d.name, "path": k, "run": f"node {mjs[0].name}" if mjs else "", "does": first[:120]})
    idx["projects"] = new; p.write_text(json.dumps(idx, indent=2) + "\n"); return new

def delta(old, new):  # 11
    return "\n".join(difflib.unified_diff(old.splitlines(), new.splitlines(), lineterm="", n=0))
def apply_delta(old, d):
    lines = old.splitlines(); out = []; i = 0; hunks = re.split(r"^@@", d, flags=re.M)[1:]
    for h in hunks:
        hdr, *body = h.split("\n"); m = re.match(r" -(\d+)(?:,(\d+))? \+", hdr)
        s, c = int(m.group(1)), int(m.group(2) or 1); start = s - 1 if c else s
        out += lines[i:start]; i = start + c
        out += [b[1:] for b in body if b.startswith("+")]
    out += lines[i:]; return "\n".join(out) + ("\n" if old.endswith("\n") or True else "")

def legend(text, minlen=30):  # 12: replace repeated table cells with [Lk] + legend
    cells = [c.strip() for l in text.splitlines() if l.startswith("|") for c in l.strip().strip("|").split("|")]
    from collections import Counter
    rep = [c for c, n in Counter(cells).items() if n > 1 and len(c) >= minlen and "[L" not in c]
    rep.sort(key=len, reverse=True); keys = {c: f"[L{i}]" for i, c in enumerate(rep)}
    out = []
    for l in text.splitlines(keepends=True):
        if l.startswith("|"):
            parts = l.split("|")
            parts = [(" " + keys[p.strip()] + " ") if p.strip() in keys else p for p in parts]; l = "|".join(parts)
        out.append(l)
    leg = "\n<!-- LEGEND\n" + "\n".join(f"{v}\t{k}" for k, v in keys.items()) + "\nLEGEND -->\n"
    return "".join(out) + leg
def unlegend(t):
    body, leg = t.rsplit("\n<!-- LEGEND\n", 1); m = dict(l.split("\t", 1) for l in leg.split("\nLEGEND -->")[0].splitlines())
    out = []
    for l in body.splitlines(keepends=True):
        if l.startswith("|"):
            l = "|".join((" " + m[p.strip()] + " ") if p.strip() in m else p for p in l.split("|"))
        out.append(l)
    return "".join(out)

def to_lines(md):  # 13 lossless: one line per row, TAB-joined, links kept
    hdr = None; out = []
    for l in md.splitlines():
        if l.startswith("| Id |"): hdr = l; out.append("#H\t" + l); continue
        if hdr and l.startswith("|") and not set(l) <= set("|-: "): out.append("\t".join(c.strip() for c in l.strip().strip("|").split("|")))
    return "\n".join(out) + "\n"
def from_lines(t):
    L = t.splitlines(); hdr = L[0][3:]; n = hdr.count("|") - 1
    return [hdr, "|" + "---|" * n] + ["| " + " | ".join(l.split("\t")) + " |" for l in L[1:]]

def lane_slice(matrix, lane):  # 14: keep header sections + only table rows mentioning lane
    out = []
    for l in matrix.splitlines():
        if not l.startswith("|") or l.startswith("|---") or re.match(r"\|\s*(Role|Skill|Lane|Agent)\b", l) or lane.lower() in l.lower(): out.append(l)
    return "\n".join(out) + "\n"

def hygiene(root, now, days=7, apply=False):  # 16,17
    root = pathlib.Path(root); m = root / "mesh"; zero = sorted(p for p in m.rglob("*") if p.is_file() and p.stat().st_size == 0)
    dated = []
    for p in m.glob("*.md"):
        d = re.search(r"(\d{4}-\d{2}-\d{2})", p.name)
        if d and (now.date() - dt.date.fromisoformat(d.group(1))).days > days: dated.append(p)
    moved = []
    if apply:
        for p in zero + dated:
            if p.parent != m and p not in dated: continue
            ym = now.strftime("%Y-%m"); dst = m / "archive" / ym / p.name; dst.parent.mkdir(parents=True, exist_ok=True)
            p.rename(dst); p.write_text(f"Moved to archive/{ym}/{p.name} on {now.date()} (Pharaoh, no-deletes rule).\n"); moved.append(p.name)
            idx = m / "archive/INDEX.md"; idx.write_text((idx.read_text() if idx.exists() else "# Archive index\n") + f"- {ym}/{p.name}\n")
    return zero, dated, moved

def archive_done(root, now):  # 18
    p = pathlib.Path(root) / "mesh/HANDOFF.md"; lines = p.read_text().splitlines(keepends=True); keep, gone = [], []
    for l in lines:
        c = [x.strip() for x in l.strip().strip("|").split("|")] if l.startswith("|") else []
        if len(c) >= 6 and c[2].lower() in base.DONE and c[4].lower() == "none": gone.append(l); continue
        keep.append(l)
    p.write_text("".join(keep))
    a = pathlib.Path(root) / f"mesh/archive/{now:%Y-%m}/HANDOFF-done.md"; a.parent.mkdir(parents=True, exist_ok=True)
    a.write_text((a.read_text() if a.exists() else "# Done handoff rows\n\n| Id | Lane | State | Where it was left | Next step (owner) | Link |\n|---|---|---|---|---|---|\n") + "".join(gone))
    return [g.split("|")[1].strip() for g in gone]

def redacted(text):  # 24: counts only
    return "\n".join([l for l in text.splitlines() if l.startswith(("REPORTED rows", "Complete open rows"))] +
                     [f"Needs attention items: {sum(1 for l in text.split('## Lanes')[0].splitlines() if l.startswith('- '))}"]) + "\n"
