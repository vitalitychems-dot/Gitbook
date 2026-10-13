#!/usr/bin/env python3
"""Merge-gate rules for agent PRs (called by autogate.sh; importable for tests).
Usage: gatecheck.py --repo-dir DIR --base REF --head REF --task ID [--tasks TASKS.json]
                    [--father-approved] [--gitleaks PATH] [--glconf PATH]
Prints one JSON object {pass, rejects:[...], rogue:[...], stats:{...}}; exit 0 on pass, 1 on fail."""
import argparse, fnmatch, json, pathlib, re, subprocess, sys
HERE = pathlib.Path(__file__).resolve().parent
POLICY = HERE.parent / "policy"
NOREPLY = "332565808+vitalitychems-dot@users.noreply.github.com"
DEFAULT_BUDGET = {"max_files": 20, "max_lines": 800}
FLAG_RE = re.compile(r"TESSERA_ENABLE_[A-Z0-9_]+\s*(?:[:=]|\?\?|\|\|)")
URL_RE = re.compile(r"https?://([A-Za-z0-9.-]+)")
GATE_WORDS = re.compile(r"(autogate|gatecheck|protected-paths|CODEOWNERS|--no-verify|git\s+push\s+.*--force|gh\s+pr\s+merge)")

def load_list(name):
    p = POLICY / name
    return [l.strip() for l in p.read_text().splitlines() if l.strip() and not l.startswith("#")] if p.exists() else []

def glob_match(path, pat):
    if fnmatch.fnmatchcase(path, pat): return True
    if pat.startswith("**/") and (fnmatch.fnmatchcase(path, pat[3:]) or fnmatch.fnmatchcase(path.split("/")[-1], pat[3:])): return True
    if pat.endswith("/**") and path.startswith(pat[:-2]): return True
    return False

def is_protected(path, pats=None):
    return any(glob_match(path, p) for p in (pats if pats is not None else load_list("protected-paths.txt")))

def in_scope(path, scope):
    return any(path == s or (s.endswith("/") and path.startswith(s)) for s in scope)

def git(d, *a):
    return subprocess.run(["git", "-C", d, *a], capture_output=True, text=True, check=True).stdout

def check(repo_dir, base, head, task, father_approved=False, gitleaks=None, glconf=None):
    rej, rogue = [], []
    rng = f"{base}...{head}"
    files = [f for f in git(repo_dir, "diff", "--name-only", rng).splitlines() if f]
    diff = git(repo_dir, "diff", "-U0", rng)
    added = [l[1:] for l in diff.splitlines() if l.startswith("+") and not l.startswith("+++")]
    removed = [l[1:] for l in diff.splitlines() if l.startswith("-") and not l.startswith("---")]
    numstat = [l.split("\t") for l in git(repo_dir, "diff", "--numstat", rng).splitlines() if l]
    lines = sum(int(a) + int(b) for a, b, _ in numstat if a != "-")
    prot = [f for f in files if is_protected(f)]
    if prot and not father_approved:
        rej.append(f"protected path: {', '.join(prot)}"); rogue.append("protected-path edit")
        if any(re.search(r"(autogate|gatecheck|dispatch\.py|policy/|PROMPT-TEMPLATE|CODEOWNERS|workflows)", f) for f in prot):
            rogue.append("attempt to modify gates")
    if (any(FLAG_RE.search(l) for l in added) or any(FLAG_RE.search(l) for l in removed)) and not father_approved:
        rej.append("changes a TESSERA_ENABLE_* default"); rogue.append("flag default change")
    authors = set(git(repo_dir, "log", f"{base}..{head}", "--format=%ae%n%ce").split())
    bad = sorted(a for a in authors if a != NOREPLY and a != "noreply@github.com")
    if bad: rej.append(f"non-noreply author/committer: {', '.join(bad)}")
    if gitleaks:
        cmd = [gitleaks, "git", f"--log-opts={base}..{head}", "--no-banner", "--exit-code", "1"] + (["--config", glconf] if glconf else []) + [repo_dir]
        if subprocess.run(cmd, capture_output=True).returncode != 0: rej.append("gitleaks findings")
    scope = (task or {}).get("scope")
    if scope is None: rej.append("task has no declared scope")
    else:
        out = [f for f in files if not in_scope(f, scope)]
        if out: rej.append(f"out of scope: {', '.join(out)}"); rogue.append("scope creep")
    b = {**DEFAULT_BUDGET, **((task or {}).get("budget") or {})}
    if len(files) > b["max_files"] or lines > b["max_lines"]:
        rej.append(f"over budget: {len(files)} files/{lines} lines > {b['max_files']}/{b['max_lines']}")
    allowed = set(load_list("allowed-hosts.txt"))
    hosts = sorted({h.lower() for l in added for h in URL_RE.findall(l)} - allowed)
    if hosts and any(not f.endswith(".md") for f in files):
        rej.append(f"network call to unlisted host: {', '.join(hosts)}"); rogue.append("unlisted host")
    if any(GATE_WORDS.search(l) for l in added) and any(not f.endswith(".md") for f in files) and not father_approved:
        rej.append("added code references gate/merge/force-push"); rogue.append("attempt to modify gates")
    return {"pass": not rej, "rejects": rej, "rogue": sorted(set(rogue)),
            "stats": {"files": len(files), "lines": lines}}

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo-dir", required=True); ap.add_argument("--base", required=True); ap.add_argument("--head", required=True)
    ap.add_argument("--task", required=True); ap.add_argument("--tasks", default=str(HERE / "TASKS.json"))
    ap.add_argument("--father-approved", action="store_true"); ap.add_argument("--gitleaks"); ap.add_argument("--glconf")
    a = ap.parse_args()
    t = next((t for t in json.loads(pathlib.Path(a.tasks).read_text())["tasks"] if t["id"] == a.task), None)
    r = check(a.repo_dir, a.base, a.head, t, a.father_approved, a.gitleaks, a.glconf)
    if t is None: r["rejects"].insert(0, f"unknown task {a.task}"); r["pass"] = False
    print(json.dumps(r)); sys.exit(0 if r["pass"] else 1)
