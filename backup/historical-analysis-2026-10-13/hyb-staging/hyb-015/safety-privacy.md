# Safety and privacy

Status: DRAFT (HYB-015, staged locally). The full exclusion list is in `merge/HYB-011-EXCLUSION-MANIFEST.md`. It is linked here, not repeated.

- `1T` is never opened, copied, or added to TESSERA. (HYB-006 C18; HYB-007 Z17, Z19; HYB-011.)
- Father's natal data stays an env secret (`artifacts/api-server/src/lib/father-natal.ts`). It is never written into source or prompts. (HYB-006 C5; HYB-007 Z20.)
- Runtime `data/` (ingest, school, drive, inbox), held-packet and study-log bodies, and imports objects are not product code. (HYB-007 Z18, Z22–Z24 → HYB-009/011.)
- Outbound HTTP only via the allowlist guard. Execution by tool name (`execFile`) was rejected. (HYB-007 Z12, Z25.)
- Advisory handling: `braces` GHSA-vfj7-8cjw-p6xm accepted and mitigated (HYB-005).

## Provenance

- `merge/hyb-006-grok-ready.md` @ Gitbook `cd8faa0` (sources Grok-ready `9e3fbca`, TESSERA `fec56eb`)
- `merge/hyb-007-z-app.md` @ Gitbook `cd8faa0` (sources Zz `150d4ec`, TESSERA `fec56eb`)
- `merge/hyb-008-olive.md`, `merge/hyb-017-storefront.md` @ Gitbook `cd8faa0`
- `intake/HYBRID-CONSOLIDATION-BACKLOG.md` @ Gitbook `cd8faa0`
