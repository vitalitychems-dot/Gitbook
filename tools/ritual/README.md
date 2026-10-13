# Ritual rounds (Akhenaten)

All agents answer the same questions; answers go on the mesh bus as one line per agent; `ritual.py merge ROUND BUS` merges them by consensus and scores against a private key.

- `ritual.py`: merge and scoring. Answer keys are read from a private store at run time and are **never committed** (see `.gitignore`).
- `questions-4.json`, `live-round-4.md`: round live-4 (generated, non-memorisable items).
- `PREREG.md`: pre-registration for the random-number test (NOT RUN). Original hash `a8a073d7936e8af5b05823ff39bbcadca129d78943d9dcbf55dbc0de145005d0`, committed 2026-10-13 02:40 CT.

## Lost and recovered (Build's 8:40 AM CT wipe)
The box copies of rounds 1–3 and PREREG.md were wiped. Recovered from git:
- `PREREG.md` text from Gitbook PR #74 (`handoff/box-reset-2026-10-13/...`); its SHA-256 still equals the original hash above, so the registration is intact.
- live-round-1/2 answer lines: Gitbook PRs #82 and #83 (`mesh/akhenaten/ritual/`).
- live-round-3 lines, questions and notes: PR #74. live-3 is **forged** (all 9 lines written by one writer, `"from":"tessera"`), so don't use it for scoring.
