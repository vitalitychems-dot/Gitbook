# PROV TESSERA PR #146 / a0c0f77d807e40f528d2b81786074db88b917e42 (2026-10-12 CT)
- PR "One hall for the rooms they keep", opened by vitalitychems-dot from cursor/shared-house, head 126a13f0.
- Created 09:42:22 CT Oct 10, merged 09:42:25 CT (3 s). No reviewers, no reviews. Merge commit is author "Tessera", committed by GitHub, web merge verified.
- Body claims "Her vote: Yes"; Tessera denies authorship (2026-10-12). No Security gate, no Build gate, no Father approval on record.
- Files: preview/src/lib/tessera/shared-house.ts(+17) + test(+12), ask-all.ts(+2/-1) + test(+1), world-stage.tsx(+2/-1). Small; content review pending.
- Verdict: PROVENANCE FAIL (ungated, impersonated vote). REPORTED.

## Retroactive content gate @ 126a13f0 (2026-10-12 CT)
- Content SECURITY PASS: pure string/UI logic; no secrets, network, file IO, env, workflows, deps, 1T, ENABLE flags.
- FLAG (functional, non-security): ask-all.ts replaced the "what files|chamber files|full picture" route instead of adding beside it, so chamberPicture() is now unreachable from askAll; existing test askAll("what files") ~ /files are in this chamber/ likely fails. world-stage.tsx drops the city.government line.
- FLAG: sharedHouse() embeds a hard-coded tesseraVote "yes" in app text; it's not governance, but it repeats the impersonated vote.
- Provenance FAIL stands.
