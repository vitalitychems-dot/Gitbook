#!/usr/bin/env python3
"""Hardlink exact duplicate groups. Keep oldest path; re-hash before link."""
from __future__ import annotations

import hashlib
import json
import os
import subprocess
import sys
import time
from pathlib import Path

GROUPS = Path("/workspace/dedupe/all-groups.jsonl")
LOG = Path("/workspace/dedupe/hardlink-run.log")
SKIP_LOG = Path("/workspace/dedupe/hardlink-skipped.log")
SUMMARY = Path("/workspace/dedupe/hardlink-summary.json")

NOW = time.time()
MIN_AGE_SEC = 30 * 60
CHUNK = 8 * 1024 * 1024

def is_forbidden(path: str) -> str | None:
    if "/.git/" in path or path.endswith("/.git"):
        return ".git"
    if path == "[REDACTED-PATH] or path.startswith("[REDACTED-PATH]
        return "secrets"
    for part in path.split("/"):
        if not part:
            continue
        pl = part.lower()
        if pl == "vault" or pl == "1t":
            return "vault"
        if pl.startswith("vault-") or pl.endswith("-vault"):
            return "vault"
    return None

def sha256_file(path: str) -> str | None:
    h = hashlib.sha256()
    try:
        with open(path, "rb") as f:
            while True:
                b = f.read(CHUNK)
                if not b:
                    break
                h.update(b)
        return h.hexdigest()
    except OSError:
        return None

def same_inode(a: str, b: str) -> bool:
    try:
        sa, sb = os.stat(a), os.stat(b)
        return sa.st_ino == sb.st_ino and sa.st_dev == sb.st_dev
    except OSError:
        return False

_git_dirty: dict[str, set[str] | None] = {}
_git_root_cache: dict[str, str | None] = {}

def git_root(path: str) -> str | None:
    d = os.path.dirname(path)
    if d in _git_root_cache:
        return _git_root_cache[d]
    cur = d
    found = None
    while True:
        if os.path.isdir(os.path.join(cur, ".git")):
            found = cur
            break
        parent = os.path.dirname(cur)
        if parent == cur:
            break
        cur = parent
    _git_root_cache[d] = found
    return found

def is_uncommitted(path: str) -> bool:
    """Skip only tracked files with uncommitted modifications (not untracked)."""
    root = git_root(path)
    if not root:
        return False
    if root not in _git_dirty:
        dirty: set[str] = set()
        try:
            r = subprocess.run(
                ["git", "-C", root, "status", "--porcelain", "-uno"],
                capture_output=True, text=True, timeout=90,
            )
            if r.returncode == 0:
                for line in r.stdout.splitlines():
                    if len(line) < 4:
                        continue
                    if line.startswith("??"):
                        continue
                    rest = line[3:]
                    if " -> " in rest:
                        rest = rest.split(" -> ", 1)[1]
                    dirty.add(os.path.join(root, rest.strip('"')))
        except Exception:
            dirty = set()
        _git_dirty[root] = dirty if dirty else None
    dset = _git_dirty[root]
    if not dset:
        return False
    if path in dset:
        return True
    for dp in dset:
        if path.startswith(dp + os.sep):
            return True
    return False

def hardlink_replace(keeper: str, path: str) -> None:
    tmp = path + ".dedupe-tmp-hl"
    if os.path.exists(tmp):
        os.unlink(tmp)
    try:
        os.link(keeper, tmp)
        os.replace(tmp, path)
    except OSError:
        if os.path.exists(tmp):
            try:
                os.unlink(tmp)
            except OSError:
                pass
        os.unlink(path)
        os.link(keeper, path)

def main() -> int:
    if SKIP_LOG.exists():
        SKIP_LOG.unlink()
    linked = 0
    bytes_saved = 0
    groups_done = 0
    groups_skipped = 0
    skip_reasons: dict[str, int] = {}
    errors = 0
    already_linked = 0

    def skip(reason: str, msg: str = "") -> None:
        nonlocal groups_skipped
        groups_skipped += 1
        skip_reasons[reason] = skip_reasons.get(reason, 0) + 1
        with open(SKIP_LOG, "a") as sf:
            sf.write(f"{reason}\t{msg}\n")

    with open(LOG, "w") as log, open(GROUPS) as gf:
        log.write(f"start {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        log.flush()
        for lineno, line in enumerate(gf, 1):
            line = line.strip()
            if not line:
                continue
            try:
                g = json.loads(line)
            except json.JSONDecodeError:
                skip("bad_json", str(lineno))
                continue
            expect = g.get("sha256")
            size = int(g.get("size") or 0)
            paths = list(g.get("paths") or [])
            if not expect or len(paths) < 2:
                skip("too_few", str(lineno))
                continue

            candidates = []
            for path in paths:
                if is_forbidden(path):
                    continue
                if not os.path.isfile(path):
                    continue
                try:
                    st = os.stat(path)
                except OSError:
                    continue
                if NOW - st.st_mtime < MIN_AGE_SEC:
                    continue
                if is_uncommitted(path):
                    continue
                candidates.append((st.st_mtime, path, st))

            if len(candidates) < 2:
                skip("lt2_after_filter", expect[:12] if expect else str(lineno))
                continue

            candidates.sort(key=lambda x: (x[0], x[1]))

            verified = []
            for mtime, path, st in candidates:
                if st.st_size != size:
                    continue
                dig = sha256_file(path)
                if dig != expect:
                    continue
                verified.append((mtime, path, st))

            if len(verified) < 2:
                skip("hash_mismatch", expect[:12])
                continue

            keeper = verified[0][1]
            group_linked = 0
            for _, path, st in verified[1:]:
                if same_inode(keeper, path):
                    already_linked += 1
                    continue
                try:
                    hardlink_replace(keeper, path)
                    linked += 1
                    group_linked += 1
                    bytes_saved += size
                    log.write(f"OK {size} {path} -> {keeper}\n")
                except OSError as e:
                    errors += 1
                    log.write(f"ERR {path}: {e}\n")
            groups_done += 1
            if groups_done % 100 == 0:
                msg = f"progress groups={groups_done} linked={linked} saved_gb={bytes_saved/(1024**3):.3f} errors={errors}\n"
                log.write(msg)
                log.flush()
                print(msg, end="", flush=True)

        summary = {
            "groups_done": groups_done,
            "groups_skipped": groups_skipped,
            "skip_reasons": skip_reasons,
            "files_hardlinked": linked,
            "already_hardlinked": already_linked,
            "bytes_saved_est": bytes_saved,
            "bytes_saved_gb": round(bytes_saved / (1024**3), 3),
            "errors": errors,
            "ended": time.strftime("%Y-%m-%d %H:%M:%S"),
        }
        SUMMARY.write_text(json.dumps(summary, indent=2) + "\n")
        log.write(json.dumps(summary) + "\n")
        print(json.dumps(summary, indent=2))
        return 0

if __name__ == "__main__":
    sys.exit(main())
