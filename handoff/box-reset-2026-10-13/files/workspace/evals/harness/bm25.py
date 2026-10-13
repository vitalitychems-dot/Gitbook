#!/usr/bin/env python3
"""Tiny BM25 over markdown chunks (no external deps)."""
from __future__ import annotations
import math, re
from collections import Counter
from pathlib import Path

TOKEN = [REDACTED](r"[a-z0-9_./#+-]+", re.I)

def tokenize(text: str) -> list[str]:
    return [t.lower() for t in TOKEN.findall(text)]

def chunk_markdown(path: Path, text: str, max_chars: int = 900) -> list[dict]:
    # Split on headings / blank lines
    parts = re.split(r"(?=\n#{1,3}\s)|\n{2,}", text)
    chunks = []
    buf = ""
    for p in parts:
        p = p.strip()
        if not p:
            continue
        if len(buf) + len(p) + 1 <= max_chars:
            buf = (buf + "\n\n" + p).strip()
        else:
            if buf:
                chunks.append(buf)
            buf = p[:max_chars]
    if buf:
        chunks.append(buf)
    out = []
    for i, c in enumerate(chunks):
        out.append({"id": f"{path.name}#{i}", "path": str(path), "text": c})
    return out

class BM25:
    def __init__(self, docs: list[dict], k1: float = 1.5, b: float = 0.75):
        self.docs = docs
        self.k1 = k1
        self.b = b
        self.N = len(docs)
        self.tokenized = [tokenize(d["text"]) for d in docs]
        self.doc_len = [len(t) or 1 for t in self.tokenized]
        self.avgdl = sum(self.doc_len) / max(self.N, 1)
        df: Counter = Counter()
        for toks in self.tokenized:
            df.update(set(toks))
        self.df = df
        self.idf = {t: math.log(1 + (self.N - df[t] + 0.5) / (df[t] + 0.5)) for t in df}

    def score(self, query: str, top_k: int = 3) -> list[tuple[float, dict]]:
        q = tokenize(query)
        scores = []
        for i, toks in enumerate(self.tokenized):
            tf = Counter(toks)
            s = 0.0
            dl = self.doc_len[i]
            for term in q:
                if term not in tf:
                    continue
                idf = self.idf.get(term, 0.0)
                f = tf[term]
                s += idf * (f * (self.k1 + 1)) / (f + self.k1 * (1 - self.b + self.b * dl / self.avgdl))
            scores.append((s, self.docs[i]))
        scores.sort(key=lambda x: -x[0])
        return scores[:top_k]

def load_corpus(corpus_dir: str | Path) -> BM25:
    docs = []
    for p in sorted(Path(corpus_dir).glob("*.md")):
        text = p.read_text(errors="ignore")
        docs.extend(chunk_markdown(p, text))
    return BM25(docs)
