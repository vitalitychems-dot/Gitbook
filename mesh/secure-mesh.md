# Secure mesh (O11)

How Tessera encrypts and addresses mesh traffic. Built on the security inventory of 2026-10-12 (`SECURITY-PROTOCOLS-INVENTORY.md`).

## What it is
- **E2E envelopes:** AES-256-GCM + HKDF, Ed25519 sender signatures (same curve family as the preview gate identity and O10 node keys).
- **Content addressing:** `cid = sha256(plaintext)`. Topic ids are sha256 of the topic name (IP-less pub/sub).
- **Quarantine:** unknown keys, bad signatures, and GCM failures are refused and kept in a quarantine buffer (shepherd-style `allowed` / `refused` audit).
- **Transports:** pluggable. Default is an in-process memory bus (no sockets, no IPs). O10 LAN discovery can carry these frames later.
- **Owner gate:** O10's mesh toggle stays the outer switch. Nothing publishes while it is off.

## Honest limits
- **Group key, not sealed boxes.** Peer-to-peer sealed boxes need X25519 ECDH. Node's Ed25519 keys do not convert without a new dependency, so this release uses an owner-installed symmetric group key plus signatures. The group key is generated locally and only shared out-of-band with owner approval.
- **No WAN / Tor / public relay is built in.** Any gateway that puts frames on the public internet is a separate, opt-in piece. It would leak metadata (timing, size, who talks to the gateway) even when payloads stay encrypted. That gateway is not this page and not O11.
- **Not the sacred / colonial / omniversal ciphers.** Those product ciphers stay where they are. O11 reuses only the AES-GCM envelope shape.

## Tests (local, recorded on TESSERA#204)
Encrypted round trip · tamper refuse · unknown-key refuse · pub/sub across 3 nodes.

## Related
- Offline internet: `mesh/offline-internet.md` (O8)
- LoRa research (doc only): `review/lora-meshtastic-research.md` (O9)
