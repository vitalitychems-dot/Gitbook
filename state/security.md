# Security
Instructions: read-only gates on TESSERA, Gitbook and Origin. Verdicts are pinned to the full head SHA and logged in gates/security.md. Never merges or deletes. No 1T or natal access. Findings record file:line only, never values. FAILs and HIGH findings ping Tessera.
Current (2026-10-13 ~9:00 AM CT): PASS on TESSERA #314, #316, #317, #318 and #310; Gitbook #90 and #91; GB-072 rev2; GB-073 rev2. Process FAIL on #319–#322. Re-gating Gitbook #92 @7ed7edb0.
Open: refs/pull/302 purge; key rotation; 44 gitleaks hits in Gitbook archive/ and history/; /tmp/gb-scan deletion (needs Father's yes); no-bypass protection on main; an Einstein token with no merge rights; CODEOWNERS for tools/gate/** and direction/**.
Next: Rick's Security Actions gate PR.
