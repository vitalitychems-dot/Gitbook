#!/usr/bin/env python3
"""Check that relative markdown links resolve to files in the repo.
Usage: check_links.py [--root .] FILE.md ...   (default: SUMMARY.md)
Skips http(s)/mailto/# anchors; strips #fragment and ?query; URL-decodes. Exit 1 on any broken link."""
import argparse, os, re, sys, urllib.parse

LINK = re.compile(r"(?<!!)\[[^\]]*\]\(\s*<?([^)\s>]+)>?(?:\s+\"[^\"]*\")?\s*\)")

def check(root, md):
    bad = []
    try: text = open(os.path.join(root, md), encoding="utf-8").read()
    except FileNotFoundError: return [f"{md}: file not found"]
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    for ln, line in enumerate(text.splitlines(), 1):
        for m in LINK.finditer(line):
            t = m.group(1)
            if re.match(r"^[a-z][a-z0-9+.-]*:", t, re.I) or t.startswith("#"): continue
            p = urllib.parse.unquote(t.split("#")[0].split("?")[0])
            if not p: continue
            full = os.path.normpath(os.path.join(root, p.lstrip("/")) if p.startswith("/") else os.path.join(root, os.path.dirname(md), p))
            if not os.path.exists(full): bad.append(f"{md}:{ln}: broken link -> {t}")
    return bad

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--root", default="."); ap.add_argument("files", nargs="*")
    a = ap.parse_args()
    files = a.files or ["SUMMARY.md"]
    bad = [b for f in files if f.endswith(".md") for b in check(a.root, f)]
    for b in bad: print(b)
    print(f"checked {len(files)} file(s), {len(bad)} broken link(s)")
    return 1 if bad else 0

if __name__ == "__main__":
    sys.exit(main())
