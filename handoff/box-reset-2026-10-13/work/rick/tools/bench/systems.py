"""Built-in systems for the bench harness + loader for module:function callables.

Built-ins:
  raw      — allsee.search k=5 (no brief transform)
  valve    — Tesla valvular line filter (#1)
  stack25  — #2 free-energy T=1.5 on #5 dedup_lines(valve)  [= deployable brief stack]

No Python-level hit cache: latency must reflect real end-to-end cost.
SQLite page cache still warms naturally across queries.
"""
from __future__ import annotations
import importlib.util
import os
import re
import sqlite3
import sys

ALLSEE = "/workspace/rick/tools/allsee"
sys.path.insert(0, ALLSEE)
import allsee  # noqa: E402

_NUM = r"\b\d+(?:\.\d+)?%?"
_conn = None


def _con():
    global _conn
    if _conn is None:
        _conn = sqlite3.connect(f"file:{allsee.DB}?mode=ro", uri=True)
        # Match qinvent #15 mmap path when available (harmless if unsupported)
        try:
            _conn.execute("PRAGMA mmap_size=268435456")
            _conn.execute("PRAGMA cache_size=-65536")
        except sqlite3.Error:
            pass
    return _conn


def _tok(s):
    return allsee.tok(s)


def _T(s):
    return max(1, len(s or "") // 4) if s else 0


def _sents(b):
    return [s for s in re.split(r"(?<=[.!?])\s+|\n", b) if s.strip()]


def _hits(q, k=8):
    return allsee.search(q, k, _con(), {})


def valve(q, hs):
    qs = set(_tok(q))
    out = []
    for h in hs:
        b = "\n".join(l for l in h["body"].splitlines() if qs & set(_tok(l))) or h["body"][:300]
        out.append({**h, "body": b})
    return out


def dedup_lines(hs):
    seen = set()
    out = []
    for h in hs:
        keep = []
        for l in h["body"].splitlines():
            k = " ".join(_tok(l))
            if k and k in seen:
                continue
            seen.add(k)
            keep.append(l)
        out.append({**h, "body": "\n".join(keep)})
    return out


def free_energy(q, hs, Temp=1.5):
    qs = set(_tok(q))
    w = {t: allsee.idf(_con(), t) for t in qs}
    covered = set()
    out = []
    for h in hs:
        keep = []
        for s in _sents(h["body"]):
            st = set(_tok(s))
            gain = sum(w[t] for t in (st & qs) - covered)
            hasnum = bool(re.search(_NUM, s))
            info = gain + (0.5 * sum(w[t] for t in st & qs) if hasnum else 0)
            if info > Temp * _T(s) ** 0.5:
                keep.append(s)
                covered |= st & qs
        out.append({**h, "body": "\n".join(keep) or h["body"][:120]})
    return out


def make_raw(k=5):
    def system(q):
        return _hits(q, max(k, 8))[:k]
    system.__name__ = "raw"
    return system


def make_valve(k=5):
    def system(q):
        return valve(q, _hits(q, max(k, 8))[:k])
    system.__name__ = "valve"
    return system


def make_stack25(k=5, Temp=1.5):
    """#2+#5 deployable brief stack: free_energy(dedup_lines(valve(hits)))."""
    def system(q):
        hs = _hits(q, max(k, 8))[:k]
        return free_energy(q, dedup_lines(valve(q, hs)), Temp)
    system.__name__ = "stack25"
    return system


BUILTINS = {
    "raw": make_raw,
    "valve": make_valve,
    "stack25": make_stack25,
}


def load_system(spec: str):
    """Load a system by builtin name or 'path/to/file.py:function'."""
    if spec in BUILTINS:
        return BUILTINS[spec]()
    if ":" not in spec:
        raise ValueError(f"Unknown system {spec!r}; use a builtin {list(BUILTINS)} or path.py:fn")
    mod_part, fn_name = spec.rsplit(":", 1)
    if mod_part.endswith(".py") or os.path.sep in mod_part or mod_part.startswith("."):
        path = os.path.abspath(mod_part)
        name = "bench_sys_" + os.path.splitext(os.path.basename(path))[0]
        spec_ = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec_)
        spec_.loader.exec_module(mod)
    else:
        mod = importlib.import_module(mod_part)
    fn = getattr(mod, fn_name)
    if not callable(fn):
        raise TypeError(f"{spec} is not callable")
    return fn


def clear_cache():
    """API compat; no Python hit cache to clear. Resets DB connection."""
    global _conn
    if _conn is not None:
        try:
            _conn.close()
        except Exception:
            pass
        _conn = None
