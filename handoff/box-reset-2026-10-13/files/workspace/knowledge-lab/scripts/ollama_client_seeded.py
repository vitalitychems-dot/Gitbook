"""Ollama client with per-call seed (for self-consistency diversity)."""
from __future__ import annotations
import json, time, urllib.request
from typing import Any

OLLAMA_HOST = "http://127.0.0.1:11434"
DEFAULT_MODEL = "qwen2.5:3b-instruct"

def generate(prompt: str, *, model: str = DEFAULT_MODEL, system: str | None = None,
             temperature: float = 0.0, num_predict: int = 256, num_ctx: int = 2048,
             seed: int = 42, timeout: int = 180) -> dict[str, Any]:
    body: dict[str, Any] = {
        "model": model,
        "prompt": prompt,
        "stream": False,
        "keep_alive": "60m",
        "options": {
            "temperature": temperature,
            "num_predict": num_predict,
            "num_ctx": num_ctx,
            "seed": seed,
        },
    }
    if system:
        body["system"] = system
    data = json.dumps(body).encode()
    req = urllib.request.Request(
        f"{OLLAMA_HOST}/api/generate",
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    t0 = time.time()
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        out = json.loads(resp.read().decode())
    out["_wall_s"] = time.time() - t0
    ec = out.get("eval_count") or 0
    ed = out.get("eval_duration") or 0
    out["_tok_s"] = (ec / (ed / 1e9)) if ed else None
    return out
