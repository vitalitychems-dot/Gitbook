#!/usr/bin/env python3
"""Turn node:test TAP output or a vitest JSON report into scores/<suite>.json.
Usage: make_scores.py --suite NAME --tap FILE | --vitest FILE  --out scores/NAME.json
Output: {"suite","pass","fail","skip","total","tests":[passing test names],"failed":[names]}"""
import argparse, json, re, sys

def from_tap(text):
    res = {"pass": [], "fail": [], "skip": []}
    stack = []  # (indent, name) for nested subtests
    for line in text.splitlines():
        m = re.match(r"^(\s*)(not ok|ok) \d+ - (.*?)(\s+#\s*(SKIP|TODO).*)?$", line)
        if not m:
            continue
        indent, status, name, _, directive = m.groups()
        depth = len(indent) // 4
        # A parent "ok" line follows its children; count only leaves.
        is_parent = any(s[0] > depth for s in stack)   # children were seen since last line at this depth
        stack = [s for s in stack if s[0] < depth]
        stack.append((depth, name))
        if is_parent:
            continue
        key = "skip" if directive else ("pass" if status == "ok" else "fail")
        res[key].append(name.strip())
    return res

def from_vitest(data):
    res = {"pass": [], "fail": [], "skip": []}
    for f in data.get("testResults", []):
        for t in f.get("assertionResults", []):
            name = " > ".join(t.get("ancestorTitles", []) + [t.get("title", "")])
            st = t.get("status")
            res["pass" if st == "passed" else "fail" if st == "failed" else "skip"].append(name)
        if f.get("status") == "failed" and not f.get("assertionResults"):
            res["fail"].append(f"[file failed to load] {f.get('name','?')}")
    return res

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--suite", required=True)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--tap"); g.add_argument("--vitest")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    r = from_tap(open(a.tap).read()) if a.tap else from_vitest(json.load(open(a.vitest)))
    out = {"suite": a.suite, "pass": len(r["pass"]), "fail": len(r["fail"]), "skip": len(r["skip"]),
           "total": sum(len(v) for v in r.values()), "tests": sorted(r["pass"]), "failed": sorted(r["fail"])}
    json.dump(out, open(a.out, "w"), indent=2)
    print(f"{a.suite}: pass={out['pass']} fail={out['fail']} skip={out['skip']} total={out['total']}")

if __name__ == "__main__":
    main()
