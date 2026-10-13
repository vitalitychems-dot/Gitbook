#!/usr/bin/env python3
"""Fail if any TESSERA_ENABLE_* flag looks default-on in source/config.
Flags: `TESSERA_ENABLE_X ?? "1"|true`, `|| "1"`, `!== "0"` (on unless explicitly off),
`TESSERA_ENABLE_X=1|true` in .env.example / *.env / Dockerfile / workflow env / .replit.
Tests, archives and docs are skipped. Usage: check_enable_defaults.py [ROOT] [--files f1 f2 ...]"""
import os, re, sys

PATS = [
    re.compile(r"TESSERA_ENABLE_\w+['\"\]]?\s*(\?\?|\|\|)\s*['\"]?(1|true|on|yes)['\"]?", re.I),
    re.compile(r"TESSERA_ENABLE_\w+['\"\]]?\s*!==?\s*['\"](0|false|off)['\"]", re.I),
    re.compile(r"^\s*(export\s+)?-?\s*TESSERA_ENABLE_\w+\s*[:=]\s*['\"]?(1|true|on|yes)['\"]?\s*$", re.I | re.M),
]
SKIP_DIRS = {"node_modules", ".git", "archive", "archives", "dist", "test", "tests", "__tests__", "docs"}
EXTS = (".ts", ".tsx", ".mjs", ".js", ".cjs", ".json", ".yml", ".yaml", ".toml", ".env", ".example", ".replit", "Dockerfile")

def scan(path):
    hits = []
    try: text = open(path, encoding="utf-8", errors="ignore").read()
    except OSError: return hits
    if "TESSERA_ENABLE_" not in text: return hits
    for p in PATS:
        for m in p.finditer(text):
            ln = text.count("\n", 0, m.start()) + 1
            hits.append(f"{path}:{ln}: {m.group(0).strip()}")
    return hits

def main(argv):
    if "--files" in argv:
        files = argv[argv.index("--files") + 1:]
    else:
        root = argv[0] if argv else "."
        files = []
        for d, dirs, fs in os.walk(root):
            dirs[:] = [x for x in dirs if x not in SKIP_DIRS]
            files += [os.path.join(d, f) for f in fs if f.endswith(EXTS) and ".test." not in f]
    hits = [h for f in files if os.path.isfile(f) for h in scan(f)]
    for h in hits: print("default-on TESSERA_ENABLE flag:", h)
    print(f"checked {len(files)} files, {len(hits)} default-on flag(s)")
    return 1 if hits else 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
