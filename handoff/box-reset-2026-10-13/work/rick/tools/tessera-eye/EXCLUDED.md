# Tessera's Eye — EXCLUDED (Father decides later)

Saved 2026-10-13 (America/Chicago). These items from Father's photo/repo study and related tools are **documented here but NOT wired into Tessera's Eye**. Eye v5 includes only safe public layers. Do not enable the items below without a fresh Security review and Father's explicit go-ahead.

| Item | Source | Why excluded now | Kept for later |
|---|---|---|---|
| CCTV / public camera map | Argos Atlas (~172k cameras) | Watches people; person surveillance | Study notes in `/workspace/rick/REA-PHOTOS.md` |
| ALPR / license-plate reading | Flock SCAN-style / any ALPR | Vehicle+person identification | Eye Shield signatures only (`tools/eye-shield/signatures/`) |
| Face recognition | any | Biometric ID of people | not adopted |
| Per-vehicle tracks | — | Tracks people via cars | not adopted |
| Per-aircraft tracks (ADS-B) | Argos / flight layers | Individual aircraft tracking | Aggregate satellite census only (CelesTrak) |
| Per-ship tracks (AIS) | Argos / ship layers | Individual vessel tracking | not adopted |
| Red Sparrow | malware / RAT family | Remote-control malware; running it endangers our box | Defensive signatures in Eye Shield only |
| Camoufox / camofox-browser | github.com/jo-inc/camofox-browser | Built to evade site anti-bot protections | Defensive signatures in Eye Shield only |
| Argos Atlas camera layer | argosatlas.com | Camera surveillance of people | Flight/ship ideas rejected; satellite ideas already covered by CelesTrak in Eye |
| Open Generative AI "unrestricted" studio | github.com/Anil-matcha/Open-Generative-AI | Deepfake / NSFW risk | not adopted |
| Vibe-Trading live trading | github.com/HKUDS/Vibe-Trading | Trading off-limits | Debate-ensemble idea kept in simons prototype only |
| Coolify on this box | github.com/coollabsio/coolify | Needs Docker; Security: do not use open Docker port 2375 | documented |
| Mapillary street photos | mapillary.com | Needs access token; keyless call fails | KartaView (keyless) is used instead |
| Firewall inbound blocks | Eye Shield proposal | Security REJECTED (would lock out agents) | alerts-only path kept |

## What IS included in Eye v5 (safe)

USGS quakes, NASA EONET, NASA FIRMS fire cells (1° counts), NWS severe alerts, Open-Meteo city weather, CelesTrak satellites (SGP4 current positions / census), NOAA SWPC Kp, Simons 10° quake heatmap, tesseract forecast cones, Eye Shield probe points (IP→country centroid or unlocated placeholder; **no people/vehicles**), KartaView street photos (position/date/image only), Esri / USGS / NASA GIBS imagery tiles, live refresh every 5 minutes for browser-CORS feeds.

## Rule

Father may decide later to expand scope. Until then: study and signatures for defense are fine; wiring CCTV, ALPR, faces, per-vehicle/aircraft/ship tracks, malware, or stealth browsers into the Eye is not.
