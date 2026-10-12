# LoRa / Meshtastic — research note (doc only, GOAL)

Status: GOAL. No code, no hardware bought. Written 2026-10-12 for the offline-internet track (`mesh/offline-internet.md`, O8).

## What it could do
- Carry short text "drops" (board lines, yes/no answers, sync heads) between houses with no internet, over km range.
- Meshtastic nodes (ESP32/nRF52 + LoRa radio) relay small encrypted packets; payloads are tiny (~200 bytes), low bitrate.

## What it cannot do
- Carry pages, images, or git packs. Only pointers (path + sha) and short text.

## Possible shape (later, needs Father yes + hardware)
1. A bridge on one install reads Meshtastic text over USB serial and turns `TESSERA:<path>:<sha>` lines into "want page" requests for the local mesh node (O10).
2. Outgoing: only short board lines the owner already approved.
3. Same gates: owner toggle on, no keys beyond node identity, no wallet code.

## Open questions
- Region band (US 915 MHz) and duty-cycle rules.
- Which board (e.g. Heltec V3, RAK4631) — none chosen.
