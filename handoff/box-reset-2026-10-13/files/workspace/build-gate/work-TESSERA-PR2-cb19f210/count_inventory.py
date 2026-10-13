#!/usr/bin/env python3
"""Mirror of artifacts/api-server/src/__tests__/route-inventory.ts counting logic."""
import re
from pathlib import Path
from collections import defaultdict

ROUTES = Path(__file__).parent / "routes"
HTTP_METHODS = ["get", "post", "put", "patch", "delete", "options", "head", "all"]

EXPECTED_ALLOW = [
  ("GET", "/consciousness/state"),
  ("GET", "/consensus/proposals"),
  ("GET", "/dual-brain/state"),
  ("GET", "/emotional/profile"),
  ("GET", "/quantum/state"),
  ("GET", "/universe/metrics"),
  ("POST", "/consensus/propose"),
  ("POST", "/improvement/cycle"),
  ("POST", "/quantum/gate"),
  ("POST", "/universe/simulate"),
]

def strip_comments(source: str) -> str:
    out = []
    i = 0
    n = len(source)
    while i < n:
        if source.startswith("/*", i):
            end = source.find("*/", i+2)
            if end == -1: raise ValueError("unterminated block")
            out.append(" ")
            i = end + 2
            continue
        if source.startswith("//", i):
            end = source.find("\n", i)
            if end == -1: break
            out.append("\n")
            i = end + 1
            continue
        q = source[i]
        if q in "\"'`":
            out.append(q); i += 1
            while i < n:
                if source[i] == "\\":
                    out.append(source[i:i+2]); i += 2; continue
                out.append(source[i])
                if source[i] == q:
                    i += 1; break
                i += 1
            continue
        out.append(source[i]); i += 1
    return "".join(out)

def list_mounted():
    source = strip_comments((ROUTES/"index.ts").read_text())
    imports = {}
    for m in re.finditer(r'import\s+(\w+)\s+from\s+"(\./[^"]+)"', source):
        imports[m.group(1)] = m.group(2)
    mounts = []
    for m in re.finditer(r'router\.use\(\s*(?:(["\'][^"\']+["\'])\s*,\s*)?(\w+)\s*\)', source):
        binding = m.group(2)
        spec = imports.get(binding)
        if not spec:
            raise SystemExit(f"no import for {binding}")
        module = spec[2:] + ".ts"
        mounts.append({"mountIndex": len(mounts), "binding": binding, "module": module})
    return mounts

def regs_in_module(mounted):
    path = ROUTES / mounted["module"]
    source = strip_comments(path.read_text())
    if re.search(r'router\.route\s*\(', source):
        raise SystemExit(f"{mounted['module']} uses router.route()")
    pattern = re.compile(r'router\.(' + "|".join(HTTP_METHODS) + r')\(\s*(["\'`])([\s\S]*?)\2')
    found = []
    for m in pattern.finditer(source):
        p = m.group(3)
        if "\n" in p or "${" in p:
            raise SystemExit(f"non-literal path in {mounted['module']}: {p!r}")
        found.append({
            "method": m.group(1).upper(),
            "path": p,
            "module": mounted["module"],
            "mountIndex": mounted["mountIndex"],
        })
    return found

def main():
    mounts = list_mounted()
    missing = [m["module"] for m in mounts if not (ROUTES/m["module"]).exists()]
    if missing:
        print(f"MISSING {len(missing)}/{len(mounts)}: {missing[:10]}...")
        return 2
    regs = []
    for m in mounts:
        regs.extend(regs_in_module(m))
    groups = {}
    order = []
    for r in regs:
        key = f"{r['method']} {r['path']}"
        if key not in groups:
            groups[key] = {"method": r["method"], "path": r["path"], "modules": [r["module"]]}
            order.append(key)
        else:
            groups[key]["modules"].append(r["module"])
    dups = [groups[k] for k in order if len(groups[k]["modules"]) > 1]
    collapsed = len({f"{r['method']} {r['path']}" for r in regs})
    print(f"mounted_modules={len(mounts)}")
    print(f"registrations={len(regs)}")
    print(f"collapsed={collapsed}")
    print(f"duplicates={len(dups)}")
    for d in sorted(dups, key=lambda x: f"{x['method']} {x['path']}"):
        print(f"  DUP {d['method']} {d['path']} -> {d['modules']}")
    live_keys = sorted(f"{d['method']} {d['path']}" for d in dups)
    expected = [f"{m} {p}" for m,p in EXPECTED_ALLOW]
    print(f"live_keys={live_keys}")
    print(f"expected_keys={expected}")
    print(f"keys_match={live_keys == expected}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
