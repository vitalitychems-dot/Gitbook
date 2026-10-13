#!/usr/bin/env python3
"""Unpredictable gate timing + nonce-bound signed PASS (Gitbook #72 / Security).
Entropy: OS CSPRNG only (secrets). Never derived from commit SHA, time or run_id."""
import secrets,time
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey,Ed25519PublicKey
from cryptography.exceptions import InvalidSignature
def jitter(n_max,timeout_s,margin_s=60):
    """Uniform sleep in [0, min(n_max, timeout-margin)) seconds."""
    cap=min(n_max,timeout_s-margin_s)
    if cap<=0: raise ValueError("jitter cap must be below job timeout")
    return secrets.randbelow(cap)
def nonce(): return secrets.token_hex(16)  # 128-bit
def pass_msg(sha,n,ts): return f"PASS {sha} {n} {ts}".encode()
def sign(sk,sha):
    n,ts=nonce(),int(time.time()); return pass_msg(sha,n,ts),sk.sign(pass_msg(sha,n,ts))
class Verifier:
    def __init__(self,pubkeys,ttl=3600): self.keys=pubkeys;self.ttl=ttl;self.seen={}
    def check(self,msg,sig,want_sha,now=None):
        now=int(time.time()) if now is None else now
        for (t,n) in list(self.seen):
            if t<now-self.ttl: del self.seen[(t,n)]  # expire old nonces
        try: kw,sha,n,ts=msg.decode().split(" ");ts=int(ts)
        except Exception: return "REJECT malformed"
        if kw!="PASS" or sha!=want_sha: return "REJECT sha"
        if len(n)!=32: return "REJECT nonce"
        if not (now-self.ttl<=ts<=now+60): return "REJECT stale"
        if n in self.seen.values(): return "REJECT replay"
        for k in self.keys:
            try: k.verify(sig,msg);break
            except InvalidSignature: pass
        else: return "REJECT sig"
        self.seen[(ts,n)]=n; return "ACCEPT"
