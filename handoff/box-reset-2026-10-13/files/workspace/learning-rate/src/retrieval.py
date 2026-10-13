#!/usr/bin/env python3
"""Chunking + BM25 + optional dense embeddings + RRF."""
from __future__ import annotations
import json, math, re, urllib.request
from collections import Counter
from pathlib import Path

TOKEN = [REDACTED](r"[a-z0-9_./#+-]+", re.I)
OLLAMA = "http://127.0.0.1:11434"

def tokenize(text: str) -> list[str]:
    return [t.lower() for t in TOKEN.findall(text)]

def chunk_baseline(path: Path, text: str, max_chars: int = 900) -> list[dict]:
    """Original harness chunking (heading/blank split, no overlap)."""
    parts = re.split(r"(?=\n#{1,3}\s)|\n{2,}", text)
    chunks, buf = [], ""
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
    return [{"id": f"{path.name}#{i}", "path": str(path), "text": c, "heading": ""} for i, c in enumerate(chunks)]

def chunk_heading_overlap(path: Path, text: str, max_chars: int = 700, overlap: int = 120) -> list[dict]:
    """Heading-aware chunks with character overlap and heading prefix on each chunk."""
    # Split keeping headings
    sections = re.split(r"(?=^#{1,3}\s)", text, flags=re.M)
    out = []
    idx = 0
    for sec in sections:
        sec = sec.strip()
        if not sec:
            continue
        m = re.match(r"^(#{1,3}\s+[^\n]+)", sec)
        heading = m.group(1).strip() if m else path.stem.replace("__", " / ")
        body = sec
        if len(body) <= max_chars:
            pieces = [body]
        else:
            pieces = []
            start = 0
            while start < len(body):
                end = min(start + max_chars, len(body))
                # prefer break at newline
                if end < len(body):
                    br = body.rfind("\n", start + max_chars // 2, end)
                    if br > start:
                        end = br
                pieces.append(body[start:end])
                if end >= len(body):
                    break
                start = max(end - overlap, start + 1)
        for p in pieces:
            text_c = p if p.lstrip().startswith("#") else f"{heading}\n\n{p}"
            out.append({"id": f"{path.name}#h{idx}", "path": str(path), "text": text_c, "heading": heading})
            idx += 1
    return out

class BM25:
    def __init__(self, docs: list[dict], k1: float = 1.5, b: float = 0.75):
        self.docs = docs
        self.k1, self.b = k1, b
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

    def rank_ids(self, query: str, top_k: int = 20) -> list[str]:
        return [d["id"] for _, d in self.score(query, top_k=top_k)]

def load_docs(corpus_dir: str | Path, chunker) -> list[dict]:
    docs = []
    for p in sorted(Path(corpus_dir).glob("*.md")):
        if p.name.startswith("_"):
            continue
        docs.extend(chunker(p, p.read_text(errors="ignore")))
    return docs

def rrf_fuse(rank_lists: list[list[str]], k: int = 60, top_k: int = 3) -> list[str]:
    scores: dict[str, float] = {}
    for ranks in rank_lists:
        for r, doc_id in enumerate(ranks, start=1):
            scores[doc_id] = scores.get(doc_id, 0.0) + 1.0 / (k + r)
    return [d for d, _ in sorted(scores.items(), key=lambda x: -x[1])[:top_k]]

def ollama_embed(texts: list[str], model: str = "nomic-embed-text") -> list[list[float]]:
    out = []
    for t in texts:
        body = json.dumps({"model": model, "prompt": t[:8000]}).encode()
        req = urllib.request.Request(f"{OLLAMA}/api/embeddings", data=body,
                                     headers={"Content-Type": "application/json"}, method="POST")
        with urllib.request.urlopen(req, timeout=120) as resp:
            data = json.loads(resp.read().decode())
        out.append(data["embedding"])
    return out

def cosine(a: list[float], b: list[float]) -> float:
    dot = sum(x * y for x, y in zip(a, b))
    na = math.sqrt(sum(x * x for x in a)) or 1e-9
    nb = math.sqrt(sum(x * x for x in b)) or 1e-9
    return dot / (na * nb)

class DenseIndex:
    def __init__(self, docs: list[dict], embeddings: list[list[float]]):
        self.docs = docs
        self.emb = embeddings
        self.by_id = {d["id"]: i for i, d in enumerate(docs)}

    def rank_ids(self, query: str, top_k: int = 20) -> list[str]:
        qe = ollama_embed([query])[0]
        scored = [(cosine(qe, e), i) for i, e in enumerate(self.emb)]
        scored.sort(key=lambda x: -x[0])
        return [self.docs[i]["id"] for _, i in scored[:top_k]]

def build_context(docs_by_id: dict[str, dict], ids: list[str]) -> str:
    parts = []
    for i in ids:
        d = docs_by_id.get(i)
        if d:
            parts.append(f"[{d['id']}]\n{d['text']}")
    return "\n\n---\n\n".join(parts)
