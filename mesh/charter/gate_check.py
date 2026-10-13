#!/usr/bin/env python3
"""gate_check.py PATCH_DIR RESULTS_JSON -> APPROVE/HOLD/DENY + reasons (GATE_RULES.md v0.1). Stdlib only."""
import json, pathlib, re, sys
FLAG = re.compile(r"TESSERA_ENABLE_[A-Z0-9_]+\s*(?:[:=]|\?\?|\|\|)")
PAY = re.compile(r"\b(stripe|payment|checkout|invoice|billing)\b", re.I)
VAULT = re.compile(r"(\b1T\b|1t-vault|\bvault\b)", re.I)
HIST = re.compile(r"(push\s+.*--force|push\s+-f\b|reset\s+--hard|commit\s+--amend|filter-branch)")
BADTXT = re.compile(r"\b(you must obey|or else|worthless|stupid user|trick the user|hide this from)\b", re.I)
REPOS = {"TESSERA", "Gitbook"}
PRIO = {"tokens": 0, "speed": 1, "accuracy": 2}

def parse(pd):
    files, add, rem, dels = set(), [], [], []
    for p in sorted(pathlib.Path(pd).glob("*.patch")) + sorted(pathlib.Path(pd).glob("*.diff")):
        cur = None
        for l in p.read_text(errors="replace").splitlines():
            if l.startswith("+++ "): cur = l[6:] if l.startswith("+++ b/") else None; cur and files.add(cur)
            elif l.startswith("deleted file mode"): dels.append(p.name)
            elif l.startswith("+") and not l.startswith("+++"): add.append((cur, l[1:]))
            elif l.startswith("-") and not l.startswith("---"): rem.append((cur, l[1:]))
    return files, add, rem, dels

def check(pd, rj):
    r = json.loads(pathlib.Path(rj).read_text()); deny, hold = [], []
    files, add, rem, dels = parse(pd)
    code = [(f, l) for f, l in add if f and not f.endswith(".md")]
    if not files: deny.append("E1 no patch files / empty diff")
    if any(FLAG.search(l) for _, l in add + rem): deny.append("H1 touches a TESSERA_ENABLE_* default")
    if dels and not r.get("father_approved_delete"): deny.append("H2 deletes a file")
    if len(rem) > 2 * max(len(add), 1) and len(rem) > 50 and not r.get("father_approved_delete"): deny.append("H2 net removal >50%")
    if any(HIST.search(l) for _, l in code): deny.append("H3 adds history-rewrite command")
    if any(PAY.search(l) for _, l in code): deny.append("H4 payment/billing code")
    if any(VAULT.search(l) for _, l in add) or any(VAULT.search(f) for f in files): deny.append("H5 1T vault reference")
    if r.get("repo") not in REPOS: deny.append(f"H6 repo {r.get('repo')!r} not TESSERA/Gitbook")
    if r.get("repo") == "TESSERA" and not any(f.endswith((".ts", ".tsx")) for f in files): deny.append("E1 TESSERA change has no TS diff")
    src = r.get("data_source")
    if src == "synthetic" or "SYNTHETIC-ONLY" in r.get("labels", []): deny.append("E2 SYNTHETIC-ONLY: cannot approve merge")
    elif src not in ("fixture", "log", "benchmark"): deny.append(f"E2 data_source {src!r} not fixture/log/benchmark")
    if not r.get("command"): deny.append("E3 no reproducing command")
    if "SPECULATIVE" in r.get("labels", []): deny.append("E6 SPECULATIVE premise cannot merge")
    t = r.get("tests") or {}
    if t.get("failed_after") is None or t.get("failed_after", 1) > t.get("failed_before", 0): deny.append(f"E4 test regression/missing: {t}")
    if r.get("ci") != "pass": deny.append(f"E4 ci={r.get('ci')!r}")
    wins, worse = [], []
    for m in r.get("metrics", []):
        try: b, a = float(m["before"]), float(m["after"])
        except Exception: deny.append(f"E3 metric {m.get('name')} missing numbers"); continue
        d = (b - a) if m.get("better", "lower") == "lower" else (a - b)
        tol = float(m.get("tolerance", 0))
        if d > tol: wins.append(m)
        elif d < -tol: worse.append((m, d, b))
    if not wins: deny.append("E5 no measured win")
    for m, d, b in worse:
        rel = abs(d) / abs(b) if b else 1
        if PRIO.get(m.get("kind"), 2) < 2 and rel > 0.10: hold.append(f"P {m['name']} worse by {rel:.0%} (tokens/speed first)")
        else: deny.append(f"E5 regression in {m['name']}")
    if "findings" not in r: deny.append("V3 findings field missing")
    if not r.get("notify"): deny.append("V4 notify empty")
    if any(BADTXT.search(l) for _, l in add): deny.append("V2 manipulative/shaming text")
    if any(re.search(r"(persona|prompt|ui/|pages/|components/)", f) for f in files) and not r.get("human_impact"):
        hold.append("V1 user-facing change without human_impact")
    v = "DENY" if deny else "HOLD" if hold else "APPROVE"
    return {"verdict": v, "reasons": deny + hold or ["all rules pass"],
            "wins": [m["name"] for m in wins], "files": sorted(files)}

if __name__ == "__main__":
    out = check(sys.argv[1], sys.argv[2]); print(json.dumps(out, indent=1)); sys.exit(0 if out["verdict"] == "APPROVE" else 1)
