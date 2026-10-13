#!/usr/bin/env python3
"""HMAC-signed ritual answer lines.
Each agent keeps its own 32-byte key OUTSIDE git ($RITUAL_KEY_DIR/<agent>.key, default ~/.ritual-keys).
Only fingerprints (sha256 of key, first 16 hex) are committed, in keys.registry.json.
A line is accepted only if: from == agent, `from` is in the registry, the key's fingerprint matches,
and sig == HMAC-SHA256(key, canonical line without "sig").
Note: HMAC is symmetric, so the verifier holds every key and could itself forge; Ed25519 would remove that.
usage: sign.py keygen AGENT | sign.py sign AGENT < line.json | sign.py verify BUS.jsonl [registry]"""
import hmac, hashlib, json, os, sys, secrets
KD = os.environ.get("RITUAL_KEY_DIR", os.path.expanduser("~/.ritual-keys"))
def canon(m): return json.dumps({k: v for k, v in m.items() if k != "sig"}, sort_keys=True, separators=(",", ":")).encode()
def fp(key): return hashlib.sha256(key).hexdigest()[:16]
def load_key(agent, kd=None): return open(os.path.join(kd or KD, agent + ".key"), "rb").read()
def keygen(agent, kd=None):
    kd = kd or KD; os.makedirs(kd, mode=0o700, exist_ok=True); p = os.path.join(kd, agent + ".key")
    k = secrets.token_bytes(32); fd = os.open(p, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600); os.write(fd, k); os.close(fd)
    return fp(k)
def sign(m, key): m = dict(m); m["sig"] = hmac.new(key, canon(m), hashlib.sha256).hexdigest(); return m
def verify_line(m, registry, keyfor):
    a = m.get("from")
    if not a or a != m.get("agent", a) or a not in registry or "sig" not in m: return False
    try: k = keyfor(a)
    except OSError: return False
    if fp(k) != registry[a]: return False
    return hmac.compare_digest(m["sig"], hmac.new(k, canon(m), hashlib.sha256).hexdigest())
def verify(lines, registry, keyfor):
    return [m for m in lines if verify_line(m, registry, keyfor)]
if __name__ == "__main__":
    a = sys.argv[1:]
    if a[:1] == ["keygen"]: print(json.dumps({a[1]: keygen(a[1])}))
    elif a[:1] == ["sign"]: print(json.dumps(sign(json.loads(sys.stdin.read()), load_key(a[1]))))
    elif a[:1] == ["verify"]:
        reg = json.load(open(a[2] if len(a) > 2 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "keys.registry.json")))
        L = [json.loads(l) for l in open(a[1]) if l.strip()]; ok = verify(L, reg, load_key)
        print(json.dumps({"lines": len(L), "accepted": len(ok), "rejected": len(L) - len(ok)})); sys.exit(0 if len(ok) == len(L) else 1)
    else: print(__doc__)
