"""round3 shared harness: real data = allsee.db (read-only), c1 qa_set test/dev split.
No writes to allsee/palace. token = len/4 proxy (same as allsee/rounds.py)."""
import sys, os, re, time, json, sqlite3, statistics, collections, math
sys.path.insert(0, "/workspace/rick/tools/allsee"); import allsee
QA = json.load(open("/workspace/rick/cycles/c1/qa_set.json"))
TEST = [x for x in QA if x["split"] == "test"]; DEV = [x for x in QA if x["split"] == "dev"]
DB = allsee.DB
def con(): return sqlite3.connect(f"file:{DB}?mode=ro", uri=True)
tok = allsee.tok
T = lambda s: max(1, len(s) // 4)
NUM = r"\b\d+(?:\.\d+)?%?"
def answer(q, hits):
    best = None; qt = set(tok(q))
    for rank, h in enumerate(hits):
        for s in re.split(r"(?<=[.!?])\s+|\n", h["body"]):
            ov = len(qt & set(tok(s))) / max(1, len(qt))
            for n in re.findall(NUM, s):
                if best is None or ov / (1 + rank) > best[0]: best = (ov / (1 + rank), n)
    return best and best[1]
def recall(hits, x): return any(x["file"] == h["path"] or x["file"] in h.get("aliases", []) for h in hits)
