# Two-repository source map

## Target layout

| Destination | Role | Canonical input |
|---|---|---|
| `vitalitychems-dot/TESSERA` | Active code, tests, reviewed app workspace, provenance and validation records | `tessera-unified` |
| `vitalitychems-dot/Gitbook` | Agent instructions, intake, coordination, review records, screenshots/transcripts, TODOs, and merge evidence | `Gitbook` plus selected readable records from coordination and handoff repositories |

## Disposition rules

- **Canonical application code:** use `tessera-unified` as the reviewed code base.
- **Documentation:** use `Gitbook` as the single documentation home.
- **Secrets and private data:** never copy.
- Historical sources include `1T` (protected vault — do not inspect/copy).
