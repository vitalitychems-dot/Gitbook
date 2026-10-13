#!/usr/bin/env python3
"""Read-only duplicate file scanner: size then sha256. Never deletes/moves/hardlinks."""
from __future__ import annotations

import hashlib
import json
import os
import time
from collections import defaultdict
from pathlib import Path

ROOTS = ["/workspace", "/home/box"]
PRUNE_DIR_NAMES = {".git", "proc", "sys", "dev"}
MIN_SIZE = 1
HASH_CHUNK = 1024 * 1024
OUT_DIR = Path("/workspace/dedupe")
PROGRESS_EVERY = 10000


def iter_files(roots):
    for root in roots:
        if not os.path.isdir(root):
            continue
        for dirpath, dirnames, filenames in os.walk(root, followlinks=False):
            # Prune .git (entire tree incl objects), proc/sys/dev
            dirnames[:] = [d for d in dirnames if d not in PRUNE_DIR_NAMES]
            for fn in filenames:
                fp = os.path.join(dirpath, fn)
                try:
                    st = os.lstat(fp)
                except OSError:
                    continue
                if not stat_is_reg(st) or os.path.islink(fp):
                    continue
                if st.st_size < MIN_SIZE:
                    continue
                yield fp, st.st_size, st.st_ino, st.st_dev


def stat_is_reg(st):
    import stat
    return stat.S_ISREG(st.st_mode)


def sha256_file(path: str):
    h = hashlib.sha256()
    try:
        with open(path, "rb") as f:
            while True:
                chunk = f.read(HASH_CHUNK)
                if not chunk:
                    break
                h.update(chunk)
        return h.hexdigest()
    except (OSError, IOError):
        return None


def top_level_bucket(path: str) -> str:
    parts = path.strip("/").split("/")
    if path.startswith("/workspace/"):
        return "/workspace/" + parts[1] if len(parts) >= 2 else "/workspace"
    if path.startswith("/home/box/"):
        return "/home/box/" + parts[2] if len(parts) >= 3 else "/home/box"
    return "/" + parts[0] if parts else path


def is_node_modules(path: str) -> bool:
    return "/node_modules/" in path or path.endswith("/node_modules")


def human(n: int) -> str:
    units = ["B", "KB", "MB", "GB", "TB"]
    x = float(n)
    for u in units:
        if abs(x) < 1024 or u == units[-1]:
            if u == "B":
                return f"{int(x)} {u}"
            return f"{x:.2f} {u}"
        x /= 1024
    return f"{n} B"


def main():
    t0 = time.time()
    print("Phase 1: indexing by size...", flush=True)
    by_size = defaultdict(list)
    n_files = 0
    total_bytes = 0
    nm_files = 0
    nm_bytes = 0
    for fp, size, ino, dev in iter_files(ROOTS):
        by_size[size].append((fp, ino, dev))
        n_files += 1
        total_bytes += size
        if is_node_modules(fp):
            nm_files += 1
            nm_bytes += size
        if n_files % PROGRESS_EVERY == 0:
            print(f"  indexed {n_files} files ({human(total_bytes)})...", flush=True)

    candidates = {s: paths for s, paths in by_size.items() if len(paths) > 1}
    cand_files = sum(len(v) for v in candidates.values())
    print(
        f"Indexed {n_files} files ({human(total_bytes)}). "
        f"{len(candidates)} sizes with >1 file ({cand_files} files to hash).",
        flush=True,
    )
    print(f"node_modules among indexed: {nm_files} files, {human(nm_bytes)}.", flush=True)

    print("Phase 2: hashing size-colliding files (skip hardlink clones)...", flush=True)
    by_hash = defaultdict(list)
    hashed = 0
    hardlink_skips = 0
    for size, entries in candidates.items():
        seen_ino = set()
        for fp, ino, dev in entries:
            key = (dev, ino)
            if key in seen_ino:
                hardlink_skips += 1
                continue
            seen_ino.add(key)
            digest = sha256_file(fp)
            hashed += 1
            if digest is None:
                continue
            by_hash[digest].append((fp, size))
            if hashed % 5000 == 0:
                print(f"  hashed {hashed} (skipped {hardlink_skips} hardlinks)...", flush=True)

    groups = []
    for digest, items in by_hash.items():
        if len(items) < 2:
            continue
        size = items[0][1]
        paths = sorted(p for p, _ in items)
        wasted = (len(paths) - 1) * size
        nm_count = sum(1 for p in paths if is_node_modules(p))
        groups.append({
            "sha256": digest,
            "size": size,
            "count": len(paths),
            "wasted": wasted,
            "paths": paths,
            "all_node_modules": nm_count == len(paths),
            "any_node_modules": nm_count > 0,
            "nm_count": nm_count,
        })

    groups.sort(key=lambda g: -g["wasted"])
    total_reclaimable = sum(g["wasted"] for g in groups)
    reclaimable_excl_nm = sum(g["wasted"] for g in groups if not g["all_node_modules"])
    reclaimable_nm_only = sum(g["wasted"] for g in groups if g["all_node_modules"])

    folder_waste = defaultdict(int)
    folder_dup_bytes = defaultdict(int)
    for g in groups:
        for p in g["paths"][1:]:
            folder_waste[top_level_bucket(p)] += g["size"]
        for p in g["paths"]:
            folder_dup_bytes[top_level_bucket(p)] += g["size"]

    elapsed = time.time() - t0
    summary = {
        "elapsed_sec": round(elapsed, 1),
        "files_indexed": n_files,
        "bytes_indexed": total_bytes,
        "node_modules_files": nm_files,
        "node_modules_bytes": nm_bytes,
        "hardlink_skips": hardlink_skips,
        "files_hashed": hashed,
        "duplicate_groups": len(groups),
        "total_reclaimable_bytes": total_reclaimable,
        "reclaimable_excl_all_nm_groups": reclaimable_excl_nm,
        "reclaimable_all_nm_groups": reclaimable_nm_only,
        "top_groups": groups[:30],
        "folder_waste": dict(sorted(folder_waste.items(), key=lambda x: -x[1])),
        "folder_dup_bytes": dict(sorted(folder_dup_bytes.items(), key=lambda x: -x[1])),
    }

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    with open(OUT_DIR / "scan-summary.json", "w") as f:
        json.dump(summary, f, indent=2)
    with open(OUT_DIR / "all-groups.jsonl", "w") as f:
        for g in groups:
            f.write(json.dumps(g) + "\n")

    print(
        f"DONE in {elapsed:.1f}s. Groups={len(groups)} "
        f"reclaimable={human(total_reclaimable)} "
        f"(excl all-nm groups: {human(reclaimable_excl_nm)})",
        flush=True,
    )


if __name__ == "__main__":
    main()
