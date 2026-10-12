# Offline internet

How Tessera works with no web. Source survey: REA batch 2, 2026-10-12 (TESSERA + Gitbook only).

## What works today
| Piece | Where | Label |
|---|---|---|
| file-mesh search of saved pages | TESSERA `preview/src/lib/tessera/file-mesh.ts` | TESTED (3 pages only) |
| git mesh description (`needsWeb: false`) | TESSERA `preview/src/lib/tessera/mesh-net.ts` | TESTED |
| WebRTC full-mesh rooms | TESSERA `preview/src/lib/multiplayer/p2p.ts` | REPORTED |
| IndexedDB queue/cache (lattice mesh) | TESSERA `artifacts/tessera/src/lib/lattice-mesh.ts` | REPORTED |
| Raspberry Pi mesh plans | TESSERA `artifacts/tessera/src/pages/BuildPage.tsx` | REPORTED (prose) |

No Kiwix reader and no LoRa code exist yet.

## Open PRs (waiting for the gates)
- O1 offline search index · O2 offline queue · O3 app-shell service worker · O4 optional Kiwix (off by default)
- O5 USB git-bundle carry · O6 LAN-only P2P · O7 real online/offline badge
- O9 LoRa research note (page `review/lora-meshtastic-research.md` once that PR lands)
- O10 opt-in mesh node per install, on-demand when needed

## Rules
- The owner turns the mesh on. Default off. Agents may join or decline only inside that.
- No self-copying to other machines. No wallets or keys besides the node identity.
- 1T and vault stay closed.

## Carry by USB (sneakernet)
`node preview/scripts/mesh-bundle.mjs create <repo> mesh.bundle`, carry the file, then `open mesh.bundle <dir>`.
