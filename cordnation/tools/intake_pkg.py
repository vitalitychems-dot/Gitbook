#!/usr/bin/env python3
"""intake_pkg.py: refresh intake/log.md rows from the GitHub API and package the diff.

Read-only on GitHub: it uses `gh api` GET calls only. No clone, no push, no PR,
and it never deletes files.
Usage:
  intake_pkg.py --out DIR --gb GB-0NN [--prs 76 70 ...] [--auto] [--prev OLD.diff]
                [--title "..."] [--dry]
--auto scans every log row that names a PR and refreshes whichever ones are stale.
"""
import argparse, base64, datetime as D, hashlib, json, os, re, subprocess, sys, tempfile, time

REPO = "vitalitychems-dot/Gitbook"
CALLS = 0
LOCK_RE = re.compile(r"^\s*\**\s*Moderator (?:locked )?check\b[^\n]*?\b([0-9a-f]{7,40})\b", re.I | re.M)
GATE_RE = re.compile(r"^\s*\**\s*(Moderator|Security|Build|Tessera)\s+(PASS|FAIL)\b(?:[^\n]*?\b([0-9a-f]{7,40})\b)?", re.I | re.M)


def api(path):
    global CALLS
    CALLS += 1
    r = subprocess.run(["gh", "api", "-H", "Accept: application/vnd.github+json", path],
                       capture_output=True, text=True)
    if r.returncode:
        sys.exit(f"gh api {path} failed: {r.stderr.strip()}")
    return json.loads(r.stdout)


def ct(z):
    if not z:
        return None
    t = D.datetime.fromisoformat(z.replace("Z", "+00:00"))
    return (t - D.timedelta(hours=5)).strftime("%H:%M CT %Y-%m-%d")  # CDT (UTC-5)


def pr_info(n):
    p = api(f"repos/{REPO}/pulls/{n}")
    cm = api(f"repos/{REPO}/issues/{n}/comments?per_page=100")
    # gate verdicts and locked checks come from issue comments (/issues/N/comments), keyed by head SHA
    gates, locks = [], []
    for c in cm:
        for m in LOCK_RE.finditer(c["body"] or ""):
            locks.append((m.group(1)[:8], c["id"], ct(c["created_at"])))
        for m in GATE_RE.finditer(c["body"] or ""):
            gates.append((m.group(1).title(), m.group(2).upper(), (m.group(3) or "")[:8], c["id"]))
    checks = api(f"repos/{REPO}/commits/{p['head']['sha']}/check-runs")["total_count"] if p["state"] == "open" else None
    return {"n": n, "checks": checks, "state": "merged" if p.get("merged_at") else p["state"],
            "head": p["head"]["sha"][:8], "merge": (p.get("merge_commit_sha") or "")[:7],
            "merged_at": ct(p.get("merged_at")), "title": p["title"], "gates": gates, "locks": locks}


def row_prs(cells):
    """PR number(s) that a row is about: its id cell, or a 'PR #N' in title/status/evidence."""
    m = re.match(r"\| PR #(\d+)", cells[0])
    if m:
        return [int(m.group(1))]
    # GB rows: only an explicit own-PR phrase counts (e.g. "(PR #65, merged" or "via PR #65"),
    # never a PR that the title merely mentions
    m = re.search(r"(?:\(PR #(\d+), merged|via PR #(\d+))", cells[7])
    return [int(m.group(1) or m.group(2))] if m else []


def refresh(cells, i):
    """Return (new_cells, reason) or (cells, None) when the row is current."""
    c = list(cells)
    st, ev = c[6].strip(), c[7]
    passes = {g for g, v, s, _ in i["gates"] if v == "PASS" and s and i["head"].startswith(s[:7])}
    why = []
    # an open or held row whose PR has since merged or closed
    if i["state"] == "merged" and (st.startswith("open") or st == "in review"):
        if {"Moderator", "Security", "Build"} <= passes:
            c[6] = "published"
        else:
            c[6] = "merged, ungated, retro-review"
        c[7] = ev + f"; Published {i['merge']} (PR #{i['n']}, merged {i['merged_at']}; refreshed from the API)"
        why.append(f"{st} -> {c[6]}")
    elif i["state"] == "closed" and st.startswith("open"):
        c[6] = "closed, not merged"
        why.append(f"{st} -> closed")
    # an open row whose recorded head is stale
    if i["state"] == "open":
        for h in set(re.findall(r"(?:Head |@)([0-9a-f]{8})", " ".join(c))):
            if h != i["head"]:
                # move only the head marker; older evidence stays tied to the old head
                for k in range(len(c)):
                    c[k] = re.sub(rf"(Head |@){h}", rf"\g<1>{i['head']} (was {h})", c[k])
                why.append(f"head {h} -> {i['head']}")
                # tie each older locked-check comment to the head it was made on
                for sha, cid, _ in i["locks"]:
                    if sha == h:
                        for k in range(len(c)):
                            c[k] = re.sub(rf"(comment {cid})(?! on )", rf"\g<1> on {h}", c[k])
                            c[k] = re.sub(rf"(check {cid})(?! on )", rf"\g<1> on {h}", c[k])
        if why:
            new = [(cid, t) for sha, cid, t in i["locks"] if sha == i["head"]]
            if new:
                cid, t = new[-1]
                c[7] += f"; Moderator locked check, PR comment {cid} ({t[:8]}) on {i['head']}: ready for Father's code-owner review"
                c[9] = f"Moderator locked check {cid} on {i['head']} (earlier: {c[9].replace('Moderator locked check ', '')})"
            c[7] += f"; PASS on head {i['head']}: {', '.join(sorted(passes))}" if passes else f"; no gate PASS on head {i['head']}"
            # update the CI phrase in place; never append a second one
            ci = f"{i['checks']} CI check runs on head {i['head']} (API {D.date.today()})"
            c[7], n_ = re.subn(r"\d+ CI check runs on the head", ci, c[7])
            if not n_:
                c[7] += "; " + ci
    return c, ("; ".join(why) or None)


def udiff(a, b, path="intake/log.md"):
    with tempfile.TemporaryDirectory() as t:
        pa, pb = os.path.join(t, "a"), os.path.join(t, "b")
        open(pa, "w").write(a); open(pb, "w").write(b)
        r = subprocess.run(["diff", "-u", "--label", f"a/{path}", "--label", f"b/{path}", pa, pb],
                           capture_output=True, text=True)
        return r.stdout


def apply_check(base, diff):
    with tempfile.TemporaryDirectory() as t:
        os.makedirs(f"{t}/intake"); open(f"{t}/intake/log.md", "w").write(base)
        open(f"{t}/p.diff", "w").write(diff)
        f = subprocess.run(["git", "apply", "--check", "p.diff"], cwd=t).returncode == 0
        subprocess.run(["git", "apply", "p.diff"], cwd=t)
        r = subprocess.run(["git", "apply", "-R", "--check", "p.diff"], cwd=t).returncode == 0
        return f, r


def check_rows(text):
    rows = [l for l in text.split("\n") if re.match(r"\| (GB|PR|O)\S* ", l)]
    ids = [l.split(" | ")[0] for l in rows]
    bad = [i for i, l in zip(ids, rows) if len(l.split(" | ")) != 12]
    return bad, sorted({x for x in ids if ids.count(x) > 1})


def main():
    a = argparse.ArgumentParser()
    a.add_argument("--out", required=True); a.add_argument("--gb", required=True)
    a.add_argument("--prs", nargs="*", type=int, default=[]); a.add_argument("--auto", action="store_true")
    a.add_argument("--prev"); a.add_argument("--title", default="Intake auto-refresh from the GitHub API")
    a.add_argument("--dry", action="store_true")
    a.add_argument("--base-ref", default="main", help="ref whose intake/log.md is the base, e.g. an open PR head to stack on")
    o = a.parse_args(); t0 = time.time()
    main_sha = api(f"repos/{REPO}/commits/{o.base_ref}")["sha"]
    f = api(f"repos/{REPO}/contents/intake/log.md?ref={main_sha}")
    base = base64.b64decode(f["content"]).decode()
    lines = base.split("\n")
    want = set(o.prs); idx = {}
    for k, l in enumerate(lines):
        c = l.split(" | ")
        if len(c) == 12 and re.match(r"\| (GB|PR|O)", c[0]):
            for n in row_prs(c):
                if o.auto or n in want:
                    idx.setdefault(n, []).append(k)
    info = {n: pr_info(n) for n in sorted(idx)}
    changes = []
    for n, ks in idx.items():
        for k in ks:
            c = lines[k].split(" | ")
            nc, why = refresh(c, info[n])
            if why:
                lines[k] = " | ".join(nc); changes.append((c[0][2:], n, why))
    missing = sorted(want - set(idx))
    if changes and not any(l.startswith(f"| {o.gb} ") for l in lines):
        last = max(k for k, l in enumerate(lines) if re.match(r"\| (GB|PR|O)\S* ", l))
        lines.insert(last + 1, f"| {o.gb} | {o.title} | Gitbook / Cordnation | {D.date.today()} | GitHub API (intake_pkg.py), base {main_sha[:7]} | TBD | in review |  | Gitbook Moderator | git apply --check on {main_sha[:7]} | Gitbook Moderator reviews (gate 1 of 4) | none |")
    new = "\n".join(lines)
    diff = udiff(base, new)
    fw, rv = apply_check(base, diff) if diff else (True, True)
    bad, dup = check_rows(new)
    rep = {"base_ref": o.base_ref, "base_sha": main_sha, "rows_changed": changes, "prs_without_row": missing, "apply_forward": fw,
           "apply_reverse": rv, "bad_rows": bad, "dup_ids": dup, "api_calls": CALLS,
           "wall_s": round(time.time() - t0, 1), "pr_info": info}
    if not o.dry and diff:
        os.makedirs(o.out, exist_ok=True)
        dp = os.path.join(o.out, f"{o.gb}.diff")
        open(dp, "w").write(diff)
        sha = hashlib.sha256(diff.encode()).hexdigest(); rep["sha256"] = sha
        s = [f"{sha}  {o.gb}.diff"]
        if o.prev and os.path.exists(o.prev):
            # interdiff: apply the old diff to the same base and compare the two results
            with tempfile.TemporaryDirectory() as t:
                os.makedirs(f"{t}/intake"); open(f"{t}/intake/log.md", "w").write(base)
                subprocess.run(["git", "apply", os.path.abspath(o.prev)], cwd=t, check=True)
                inter = udiff(open(f"{t}/intake/log.md").read(), new)
            ip = os.path.join(o.out, f"{o.gb}.interdiff"); open(ip, "w").write(inter)
            s.append(f"{hashlib.sha256(inter.encode()).hexdigest()}  {o.gb}.interdiff")
        open(os.path.join(o.out, "SHA256.txt"), "w").write("\n".join(s) + "\n")
        open(os.path.join(o.out, "report.json"), "w").write(json.dumps(rep, indent=1))
        rep["lines"] = diff.count("\n")
    print(json.dumps({k: v for k, v in rep.items() if k != "pr_info"}, indent=1))


if __name__ == "__main__":
    main()
