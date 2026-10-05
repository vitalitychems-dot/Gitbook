# Two-repository source map

## Target layout

| Destination | Role | Canonical input |
|---|---|---|
| `vitalitychems-dot/TESSERA` | Active code, tests, reviewed app workspace, provenance and validation records | `tessera-unified` |
| `vitalitychems-dot/Gitbook` | Agent instructions, intake, coordination, review records, screenshots/transcripts, TODOs, and merge evidence | `Gitbook` plus selected readable records from coordination and handoff repositories |

## Disposition rules

- **Canonical application code:** use `tessera-unified` as the reviewed code base. It already documents its app boundaries, deduplication ledger, validation workflow, secrets guidance, and source-branch omissions.
- **Documentation:** use `Gitbook` as the single documentation home. The staged merge adds readable coordination, pen, handoff, screenshot-index, OCR, validation, source-manifest, and duplicate-ledger material under explicit categories.
- **Historical code snapshots:** do not copy repeated application trees into either destination. Their provenance is represented by the audit and source-manifest records; the reviewed canonical code remains in `TESSERA`.
- **Raw archive parts:** do not copy raw or unreviewed archive parts into Gitbook. The handoff summaries and screenshot inventory are retained; raw archives remain in their source repositories pending owner review.
- **Secrets and private data:** never copy. Existing source notes that mention them are retained only when they describe a review boundary or rotation requirement, not the secret values.
- **Empty or placeholder repositories:** no application content to import; record only in the audit.

## Historical sources reviewed

The earlier audit inventory contained 20 repositories; the current account check contains 21 after destination activity. The groups below are functional, not a claim that every historical file is safe or needed:

- Code/application snapshots: `tessera-unified`, `Grok-ready`, `1`, `1T`, `5t`, `T44`, `TESS`, `Zz`, `olive-giant-ever-glade`.
- Documentation and coordination: `Gitbook`, `tessera-gitbook`, `tessera-coordination`, `TX`, `z`, `Everything`.
- Handoff/archive material: `tessera-grok-handoff`, `tessera-grok-handoff-complete`, `tessera-complete-archives`.
- Empty or near-empty placeholders: `TESSERA`, `Tessera-main`, `tessera-replit`.

The exact commit IDs, file counts, byte counts, and root files are in [`repo-audit.tsv`](repo-audit.tsv). Exact content groups are in [`exact-duplicates.tsv`](exact-duplicates.tsv). These are audit evidence, not an instruction to delete anything.
