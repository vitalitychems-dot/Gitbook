# Offline internet — inventory + proposal (2026-10-12, REA batch 2 lane)

**Scope (Father, 4:56 PM CT):** only `vitalitychems-dot/TESSERA` and `vitalitychems-dot/Gitbook`. Rows below cite paths in those two repos only.

Static read only. No builds, no pushes. Search terms: offline, mesh network, kiwix, local-first, sneakernet, LoRa, cache, sync, P2P, service worker, IndexedDB, IPFS, WebRTC, zim. 1T / vault paths excluded.

## What exists

| # | Piece | Path | What it does | Label |
|---|---|---|---|---|
| 1 | "git mesh" concept | `TESSERA/preview/src/lib/tessera/mesh-net.ts` (`MESH.needsWeb:false`, carried by git) | The mesh is a git repo; a clone is readable without the web. Referenced programs admit/carry/spin/tie/pass live in the separate GitbookAI repo (out of scope) | REPORTED |
| 2 | file-mesh | `TESSERA/preview/src/lib/tessera/file-mesh.ts` (+ `file-mesh.test.ts`) | Searches a **hard-coded 3-entry** `SAVED` list; answers "no address was used". Wired from `ask-all.ts:55` on "no wifi / offline mesh / search the files" | TESTED (has a unit test) but a stub — 3 pages only |
| 3 | mesh-net | `TESSERA/preview/src/lib/tessera/mesh-net.ts` (+ `mesh-net.test.ts`) | Describes the GitbookAI mesh (`needsWeb:false`), gates posts through `public-gate.ts` | TESTED (unit test), descriptive |
| 4 | P2P rooms | `TESSERA/preview/src/lib/multiplayer/p2p.ts` | Full-mesh WebRTC, signaling via `/api/rtc` polling; needs a server + STUN, so LAN-only at best | REPORTED |
| 5 | Lattice mesh (IndexedDB) | `TESSERA/artifacts/tessera/src/lib/lattice-mesh.ts`; archived copy `Gitbook/archive/moved/collink1007-XXX/tess/client/src/lib/lattice-mesh.ts` | IndexedDB stores: peers, messages, apiCache, **offlineQueue**, latticeSites, knowledgeVault (name only — not opened) | REPORTED |
| 6 | Service worker | `Gitbook/archive/moved/collink1007-XXX/tess/client/src/main.tsx` registers `/sw.js` | Only service worker found; **not present in current TESSERA** | REPORTED |
| 7 | Offline access page | `Gitbook/archive/moved/collink1007-XXX/tess/public/sovereign-offline-access.html` (14 KB) | Static page, uses localStorage only — no SW/cache API | REPORTED |
| 8 | Hardware / mesh plans | `TESSERA/artifacts/tessera/src/pages/BuildPage.tsx:16-18,68` | Text plans: Raspberry Pi micro-server, "Sovereign Networking", 3–5 Pi mesh cluster, P2P WebSocket "Mesh Lattice" | REPORTED (prose only) |
| 9 | UI status | `TESSERA/artifacts/tessera/src/components/MeshStatusBadge.tsx`, `SplashScreen.tsx`, `CommandCenterPage.tsx:59` | Offline badge / cosmetic log lines | REPORTED (cosmetic) |
| 10 | Kiwix / LoRa / Meshtastic / IPFS mentions | `Gitbook/archive/moved/collink1007-XXX/x/tess/server/{routes.ts,tessera-omnibus.ts}` | Mentions in prompts/knowledge text only. **No Kiwix/ZIM reader, no LoRa code** | UNKNOWN→REPORTED (text only) |
| 11 | Policy | `Gitbook/posts/2026-10-07-rea-deep-scan.md:72`, `2026-10-07-external-rea-adoption.md:24` | "local-first" policy stated | REPORTED |

**Bottom line:** the only TESTED offline pieces are two tiny stubs (file-mesh, mesh-net). Real offline caching (IndexedDB queue, service worker) lives only in archived XXX code; nothing serves Wikipedia-class content offline.

## Proposed improvements (bulk-list candidates — each needs Moderator→Tessera→Security→Build→Father yes)

| # | Improvement | Size | Target | Test that makes it TESTED |
|---|---|---|---|---|
| O1 | Replace file-mesh's 3-entry `SAVED` with a build-time index generated from a GitbookAI/Gitbook clone (paths + first 2 KB text) | S | TESSERA `preview/src/lib/tessera/file-mesh.ts` + small gen script | unit test: ≥50 indexed pages, query hits a real Gitbook page with `live:false` |
| O2 | Port lattice-mesh `offlineQueue` + `apiCache` (drop `knowledgeVault` store name per vault rule) into current TESSERA preview | M | TESSERA `preview/src/lib/offline/queue.ts` | test with fake-indexeddb: queued POST replays once on reconnect, no dupes |
| O3 | Add a service worker (vite-plugin-pwa / Workbox) precaching the app shell + Gitbook pages | M | TESSERA `preview` | Build check: `sw.js` emitted; Playwright offline mode loads shell |
| O4 | Kiwix/ZIM read-only lookup: optional local `kiwix-serve` URL in config; ask-all routes "offline wiki" queries to it; no download in CI | M | TESSERA api-server + `ask-all.ts` | test with mocked kiwix HTTP; disabled by default |
| O5 | Sneakernet bundle: `git bundle` export/import doc + script for GitbookAI mesh (USB carry) | S | Gitbook page `mesh/sneakernet.md` + TESSERA `scripts/` | test: bundle → clone → `mesh/index.json` sha matches |
| O6 | LAN-only P2P: allow p2p.ts with empty ICE servers + local signaling, document LAN mode | S–M | TESSERA `preview/src/lib/multiplayer/p2p.ts` | unit test for config; two-tab e2e on localhost |
| O7 | Real online/offline badge from `navigator.onLine` + queue length instead of cosmetic | S | TESSERA `MeshStatusBadge.tsx` | component test |
| O8 | Gitbook page "Offline Internet" consolidating this table + policy | S | Gitbook `mesh/offline-internet.md` | link check |
| O9 | LoRa/Meshtastic: research note only (text-message bridge to mesh drops), no code until hardware exists | S (doc) | Gitbook `review/` | n/a — GOAL |

Excluded: anything wallet/income/arbitrage in the same XXX files; `knowledgeVault` store contents; 1T.
