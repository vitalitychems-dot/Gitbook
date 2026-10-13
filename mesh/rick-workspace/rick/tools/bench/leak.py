"""Leak guard: exclude held-out / self-referential paths from retrieval hits."""
from __future__ import annotations
import re

# Paths that must never appear in retrieved context for a fair held-out test.
LEAK_PATTERNS = (
    r"qa_set",
    r"/cycles/",
    r"/tools/fraction/",
    r"/tools/bench/",
    r"allsee/rounds",
    r"synapse",
)
LEAK_RE = re.compile("|".join(LEAK_PATTERNS))


def is_leak(path: str) -> bool:
    return bool(path and LEAK_RE.search(path))


def filter_hits(hits):
    """Drop hits whose path (or any alias) matches a leak pattern."""
    out = []
    for h in hits or []:
        path = h.get("path", "") if isinstance(h, dict) else ""
        aliases = h.get("aliases", []) if isinstance(h, dict) else []
        if is_leak(path) or any(is_leak(a) for a in aliases):
            continue
        out.append(h)
    return out
