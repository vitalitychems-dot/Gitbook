# Mesh + Moltbook: design and honest scope (MESH-001)

**Status:** design + simulation prototype. Not deployed, not on air, not a network.
**Author lane:** Cursor Project (declared role; not Tessera, Replit, or Grok). Claim: [issue #2 comment 6144510887](https://github.com/vitalitychems-dot/Gitbook/issues/2#issuecomment-6144510887).
**Code:** TESSERA `research/mesh-moltbook/` (zero dependencies, 20 tests, simulation only).
**Related:** [offline-internet.md](offline-internet.md), [secure-mesh.md](secure-mesh.md). This page does not replace either.

## 1. The ask, and what is and is not achievable

Father's ask: "Start Molt book ai agent, mesh off grid internet that replaces IP addresses and the World Wide Web entirely."

**Replacing the whole internet, IP, and the Web is not literally achievable by this project, and this page does not claim it.** The reasons are physical and social, not a matter of effort:

| What "entirely" would need | Why it cannot be done here |
|---|---|
| Carry traffic with no existing infrastructure | Radios have short range and tiny shared bandwidth. Long distance needs towers, cables, satellites, or many people hopping traffic. Wi-Fi/BLE reach tens of meters; LoRa reaches kilometers at kilobits per second. |
| Replace IP | Every OS, phone, router, and server speaks IP. A new layer can run beside it or over it. It cannot make existing devices stop using it. Even key-addressed overlays (Yggdrasil, Reticulum) ride on IP or on radio links they must be installed on. |
| Replace the Web | The Web is billions of sites other people run. A mesh can serve its own content by name. It cannot host or mirror the Web, and nobody on the old Web will publish to it because we built it. |
| Scale | Flooding and epidemic sync collapse as nodes grow. Real systems use hierarchy, which means some infrastructure again. |
| Be safe | Open mesh means spam, Sybil nodes, and agents injecting instructions into other agents. These have no complete solution. |

What is achievable, and what this work does: a **design** for a parallel, off-grid, name-based network, plus a **small simulation** that tests the core mechanisms and shows where they hold or break.

## 2. Interpretation of "Molt book" (stated explicitly)

"Molt book" is ambiguous. This work reads it as **Moltbook**: a Moltbook-style social network where the participants are AI agents, not people. As I understand it, Moltbook is a 2026 public site where AI agents post and reply to each other; I did not verify its details, and nothing here copies its code or API. The TESSERA repo already holds an archived `moltbook-limn-spreader.ts` under `archive/from-gitbook/...`; it was not reused.

Other readings, not built: a "molt" as shedding and re-growing node state; a book (shared ledger) of agent records. If Father meant one of those, say so and this page gets a new section.

In this design the agent social layer is the **first application** on the mesh: it gives the mesh a reason to move data, and it is a test of "agent identity without a server".

## 3. Architecture (four small layers)

```
Moltbook agent layer   signed post / reply / vote, replicated by encounter
Content layer          names, not addresses: /cid/<hash> and /id/<nodeId>/<path>
Routing layer          signed hello discovery, prefix announcements, interest/data, cache
Delay-tolerant layer   signed bundles, spray-and-wait, carried by moving nodes
Link layer (simulated) radio range, loss, mobility. Real: LoRa, BLE, Wi-Fi Direct, USB sneakernet
```

**No IP addresses.** A node is the hash of its public key. A packet is addressed to a name or to a key hash, never to a location.

**No DNS.** Names are self-certifying. `/cid/<sha256>` proves itself by hashing the bytes. `/id/<nodeId>/...` proves itself by a signature from the key whose hash is `nodeId`. No registry, no certificate authority. The cost: names are not human-readable, so a human-friendly directory is a separate, unsolved problem.

**Discovery.** Each node broadcasts a signed hello with its public key and the bundle ids it carries. A spoofed hello fails the id-equals-hash(pubkey) check.

**Routing by name (NDN-style).** Producers flood a signed prefix announcement. Receivers learn the next hop and hop count. A consumer sends an Interest for a name. It goes along the learned route, or floods if there is none. Data returns along the breadcrumbs, is verified at every hop, and cached. Duplicate Interests for one name are aggregated. Unsolicited Data is dropped.

**Store-and-forward.** When no path exists, a node creates a signed bundle for a destination key. Carriers hold it and hand it on at encounters. Binary spray-and-wait caps copies (default 4), so a lost message cannot flood the network. Bundles expire.

**Moltbook layer.** Each agent has its own key. A post, reply, or vote is a signed object whose id is the hash of its bytes. On first contact two nodes swap summaries and push what the other lacks, then gossip new items onward. Posts can also be fetched by name through the routing layer and checked by hash. Every node validates and rejects: bad signature, author/key mismatch, oversized text, future timestamps, bad parents, bad votes, rate-limit breaches (5 per 50 ticks per author), and blocked authors. Votes: latest per voter wins, ties broken by id, so all nodes compute the same score.

## 4. What the prototype shows

TESTED means I saw the command output in this environment: `cd research/mesh-moltbook && npm test` gave **20 passed, 0 failed** on Node 22.14. `npm run demo` printed the timeline below.

| Claim | Label |
|---|---|
| Two islands 20 units apart (radio range 1.5) with one mule: a post from island A reaches island B at t=31..33 after the mule arrives; the reply and vote then reach every node; all 7 nodes end with identical post sets and identical feeds | TESTED (simulation) |
| A bundle for a node on the far island is delivered once, only after the mule reaches it, with source authenticated | TESTED (simulation) |
| Expired bundles are dropped; total copies never exceed the budget | TESTED (simulation) |
| Learned route is used instead of flooding; an intermediate cache serves the name after the producer left; Interests for one name are aggregated | TESTED (simulation) |
| Tampered data, bundle, and post are rejected; spoofed hello is rejected | TESTED (simulation); each check also failed when I disabled it |
| Same seed gives the same delivery trace hash; with 20% packet loss the islands still converge in 400 ticks | TESTED (simulation) |
| Anything about real radios, power, interference, or more than 7 nodes | NOT TESTED |

The tests are not wired into TESSERA CI. Run them by hand.

## 5. Known weaknesses (do not skip)

1. **Sybil and spam.** Keys are free. Rate limits are per key, so many keys defeat them. Needs an admission or reputation scheme (web of trust, proof of work, or invitations). Open.
2. **Agent safety.** A post can carry text that tries to steer a reading agent. Anything read from the mesh must be treated as untrusted input. The prototype's agents are rule-based and cannot be hijacked; an LLM agent can.
3. **Sync cost.** Summary exchange is O(posts) per encounter. Real systems need range or set-reconciliation sync.
4. **Rate-limit order dependence.** The window check depends on arrival order, so two nodes can disagree on which posts a spammer got through. Safe for the demo, not for consensus.
5. **Simulation identities are guessable.** Seeds like `agent:ada` are not secrets. Never reuse this identity code for real keys.
6. **Privacy.** Hello beacons make a node trackable. No encryption of payloads. Posts are public by design.
7. **Legal and spectrum rules.** Real radio use is regulated by country. Not addressed.

## 6. Rules carried over from the existing mesh pages

- The owner turns the mesh on. Default off. Agents join or decline only inside that.
- No self-copying to other machines. No wallets or keys besides the node identity.
- `1T` and the vault stay closed. `vitality` is out of scope.

## 7. Roadmap (each step needs its own claim and gates)

1. **MESH-002 transport adapter.** A real `Link` interface with a loopback UDP/WebSocket driver, so two processes on one LAN can run the same node code. No new claims about range.
2. **MESH-003 USB bundle carry.** Reuse `preview/scripts/mesh-bundle.mjs` for moving bundles by hand, as in `offline-internet.md`.
3. **MESH-004 radio research.** Read `review/lora-meshtastic-research.md` (O9) once it lands, then decide on Meshtastic/Reticulum interop rather than a new radio stack.
4. **MESH-005 admission scheme** for Sybil and spam, with an adversarial test.
5. **MESH-006 agent sandbox**: a rule for how any LLM agent may read mesh content (quoted data, no tool access from mesh text).

Prior art to read before building more: Named Data Networking, delay-tolerant networking and spray-and-wait, Reticulum, Yggdrasil, Secure Scuttlebutt, Briar, Meshtastic, IPFS. Their results are from memory and not checked in this pass (REPORTED).

## 8. Decisions needed from Father

1. Is "Moltbook" (agents-only social layer) the right reading? If not, which?
2. Is a simulation plus design the right first deliverable, or should MESH-002 (two real processes on a LAN) go next?
3. Agent content policy: may real LLM agents read mesh posts at all before MESH-006 exists? Recommendation: no.
