#!/usr/bin/env python3
"""Compare scores/*.json (after) against a baseline dir (before).
Fails (exit 1) if, for any suite: pass count drops, fail count rises, a suite disappears,
(minus tests listed as removed), or a previously passing test name is gone/failing unless listed under 'removed-tests:' in
the PR body (file given with --pr-body). Writes a markdown table to --summary (e.g. $GITHUB_STEP_SUMMARY).
Missing baseline => prints a notice and exits 0 (bootstrap)."""
import argparse, glob, json, os, re, sys

def load(d):
    out = {}
    for p in glob.glob(os.path.join(d, "**", "*.json"), recursive=True):
        try:
            j = json.load(open(p))
        except Exception:
            continue
        if isinstance(j, dict) and "suite" in j and "pass" in j:
            out[j["suite"]] = j
    return out

def removed_tests(body):
    """Lines after a 'removed-tests:' line, as '- name' bullets, until a blank line."""
    names, on = set(), False
    for line in body.splitlines():
        if re.match(r"^\s*removed-tests:\s*$", line, re.I):
            on = True; continue
        if on:
            m = re.match(r"^\s*[-*]\s+(.+?)\s*$", line)
            if m: names.add(m.group(1))
            elif line.strip() == "": break
    return names

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--before", required=True); ap.add_argument("--after", required=True)
    ap.add_argument("--pr-body"); ap.add_argument("--summary")
    a = ap.parse_args()
    before, after = load(a.before), load(a.after)
    allowed = removed_tests(open(a.pr_body).read()) if a.pr_body and os.path.exists(a.pr_body) else set()
    lines = ["| suite | pass before → after | fail before → after | skip | verdict |", "|---|---|---|---|---|"]
    problems = []
    if not before:
        msg = "No baseline scores found; skipping score-drop comparison (bootstrap run)."
        print(msg)
        if a.summary: open(a.summary, "a").write(msg + "\n")
        return 0
    for s in sorted(set(before) | set(after)):
        b, f = before.get(s), after.get(s)
        if f is None:
            problems.append(f"{s}: suite missing in this run"); lines.append(f"| {s} | {b['pass']} → – | {b['fail']} → – | – | FAIL |"); continue
        if b is None:
            lines.append(f"| {s} | new → {f['pass']} | new → {f['fail']} | {f['skip']} | new |"); continue
        bad = []
        ok_removed = (set(b.get("tests", [])) - set(f.get("tests", []))) & allowed
        if f["pass"] < b["pass"] - len(ok_removed): bad.append(f"pass {b['pass']}→{f['pass']}")
        if f["fail"] > b["fail"]: bad.append(f"fail {b['fail']}→{f['fail']}")
        gone = sorted(set(b.get("tests", [])) - set(f.get("tests", [])) - allowed)
        if gone: bad.append(f"{len(gone)} passing test(s) gone: " + "; ".join(gone[:10]))
        problems += [f"{s}: {x}" for x in bad]
        lines.append(f"| {s} | {b['pass']} → {f['pass']} | {b['fail']} → {f['fail']} | {f['skip']} | {'FAIL' if bad else 'ok'} |")
    report = "\n".join(["### Score comparison", *lines, "", *(f"- ❌ {p}" for p in problems)]) + "\n"
    print(report)
    if a.summary: open(a.summary, "a").write(report)
    return 1 if problems else 0

if __name__ == "__main__":
    sys.exit(main())
