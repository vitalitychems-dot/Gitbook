# Security / safety / shepherd / protocol inventory
**Scope:** vitalitychems-dot/TESSERA + Gitbook (incl. archive/moved). 1T and vault paths skipped. No secret values printed.  
**Date:** 2026-10-12 ~5:15 PM CT. Sources: clones + REA-RUN-LOG + b2-out stats.

## Live code (TESSERA)

| Piece | Path | What it does | Label | o11 reuse |
|---|---|---|---|---|
| Gate identity (Ed25519 JWT) | `preview/src/lib/auth/gate-identity.server.ts` (+ `gate-identity.test.ts`) | Verifies preview gate JWTs via JWKS, OKP/Ed25519 only | TESTED | Same curve family as node keys; o11 uses Node `crypto` Ed25519 for message signing, not JWTs |
| Sovereign fetch guard | `artifacts/api-server/src/lib/sovereign-fetch-guard.ts` (+ test) | Wraps `globalThis.fetch`; external calls need Shepherd context; loopback allowed | TESTED | OPSEC default: o11 transports must never call fetch outside owner opt-in + shepherd-style audit |
| Shepherd outbound audit | `artifacts/api-server/src/lib/shepherd-outbound.ts` | Classifies callers (shepherd / conscious-agent / system); JSONL audit of allow/refuse/reroute | REPORTED (used by guard; unit coverage via guard tests) | o11 logs encrypt/decrypt/publish/reject with the same outcome vocabulary where it fits |
| Safe fetch (allowlist) | `artifacts/api-server/src/lib/safe-fetch.ts` | HTTPS GET only to fixed hosts (arxiv, wikipedia, NASA); no cookies/auth | REPORTED | Pattern for "no surprise egress"; o11 has no built-in internet transport |
| Secure external wrapper | `artifacts/api-server/src/lib/secureExternalWrapper.ts` | Domain allowlist + timeout + audit log rows | REPORTED | Same spirit: pluggable transports are explicit; no silent WAN |
| Sovereign cipher | `artifacts/api-server/src/lib/sovereign-cipher.ts` | AES-256-GCM + HKDF; symbol remaps / sacred alphabet / colonial master secret | REPORTED (crypto exists; sacred/colonial layers are product-specific) | **Reuse AES-256-GCM + HKDF shape only.** Do not pull colonial secrets, sacred remaps, or auto-rotation into the mesh |
| Omniversal cipher | `artifacts/api-server/src/lib/omniversal-cipher.ts` | Layered AES-256-GCM envelopes; process-local key if env unset (won't decrypt after restart) | REPORTED | Envelope fields (iv, tag, ct) inform o11 packet shape; **no** layered sacred/astro keys |
| Sigil cipher | `artifacts/api-server/src/lib/sigil-cipher.ts` | Glyph/gematria + AES helpers; father-key fingerprint hooks | REPORTED | Out of scope for mesh (sigil/father paths are HYB-011 adjacent). Not imported |
| Address / private-host guard | `preview/src/lib/tessera/address-guard.ts` | Detects private/loopback/link-local hosts (IPv4 tricks expanded) | REPORTED (used by learning vows) | OPSEC: o11 default transport is in-memory or LAN-only; public IPs need an honest gateway |
| O10 mesh node | `preview/src/lib/mesh-node/` (local branch `o10-node-per-install`) | Opt-in node ID + Ed25519 keypair (0600), LAN multicast hello, signed page sync, agent join/decline, on-demand triggers | TESTED (local) | **o11 sits on top:** same identity file, encrypt payloads before sync/publish; discovery stays O10 |
| Duplicate / board guard | `preview/src/lib/tessera/duplicate-guard.ts`, `github-desk.ts` | Refuse repeated first lines on board posts | TESTED | Orthogonal; keep |
| Quarantine design | `docs/superpowers/specs/2026-10-01-external-dependency-isolation-design.md` | Draft: research worker isolation, no secrets, allowlisted egress, quarantine before promotion | REPORTED (doc) | Align: untrusted peer frames land in a quarantine buffer until signature+key check passes |
| Mesh ops roles | Gitbook `operations/mesh-speed-collaboration.md`, `functional-combine-hybrid-b.md` | Security lane = harden/scrub/quarantine; never Heretic/GEV | REPORTED | o11 PR goes through Security → Build → Father bulk yes |
| Content-addressed trees (historical) | Gitbook `merge/hyb-007-z-app.md` (Z23) | Zz `imports/trees` + manifest — REPORTED / REJECTED → HYB-009 | REPORTED | o11 content-ids are sha256 of plaintext; no nested tree import |

## UI / naming (not crypto)

| Piece | Path | Label | Note for o11 |
|---|---|---|---|
| Shepherd Agents panel | `artifacts/tessera/src/pages/SettingsPage.tsx` | REPORTED | Mission/harvest counters; not a crypto protocol |
| Shepherd Audit nav | `artifacts/tessera/src/components/Sidebar.tsx` → `/shepherd-audit` | REPORTED | UI route for the audit log |
| "Sentinel" / agent names | lingua, world, ChatCommands | REPORTED | Role labels, not protocols |
| "shepherd children" | agent-drill, train-pass | TESTED | Fatima recall drill — unrelated |

## Archive (Gitbook `archive/moved`)

| Piece | Path | Label | o11 |
|---|---|---|---|
| Lattice mesh IndexedDB | XXX `tess/client/src/lib/lattice-mesh.ts` (also live TESSERA artifacts) | REPORTED | Offline queue already covered by O2; o11 encrypts what the queue/sync carries |
| Service worker | XXX `tess/client/src/main.tsx` + `/sw.js` | REPORTED | Covered by O3; no crypto |
| Cipher / noise / nacl in archive | search under XXX/olive (excl. trees) | UNKNOWN→none found as live modules | No Noise Protocol or libsodium implementation to port |

## REA batch 2 flags (from REA-RUN-LOG)

- Secret-shaped fixtures in tests (`github-desk.test.ts`, `learning-memory.test.ts`) — Security to confirm placeholders; o11 must not embed raw key material in tests (use `generateKeyPairSync` per test).
- HYB-011 route names already listed in item 12; o11 must not add wallet/payment/key-export routes.
- No Noise/X25519/NaCl library packages showed up as first-class app code in the scanned trees.

## Gaps o11 fills

1. **E2E encryption of mesh payloads** — ciphers today are sacred/colonial/omniversal product crypto, not mesh peer E2E.
2. **Content addressing** — no live sha256 content-id for pages/messages (Zz trees were historical/rejected).
3. **IP-less pub/sub** — O10 discovery still uses LAN multicast + HTTP URLs; o11 adds topic hashes and pluggable transports so the logical layer does not require knowing peer IPs.
4. **OPSEC defaults** — pull together: owner toggle (O10), no WAN by default, shepherd-style audit, quarantine until verify.
5. **Honest gateway** — document that any WAN / Tor / public relay is a separate, opt-in gateway with metadata leakage; not built in o11.

## Do not import into o11

- Colonial master secret / father-key / natal / wallet / income / arbitrage paths (HYB-011).
- Sacred alphabet remaps, ephemeris keying, glyph encoding as a security layer.
- Wholesale XXX/olive copies.
- 1T / vault.
