# Repository deletion manifest — awaiting confirmation

**Prepared:** 2026-10-05  
**Destination repositories verified:**

- [`vitalitychems-dot/TESSERA`](https://github.com/vitalitychems-dot/TESSERA) — `216e4e89f40956225431eb1f774c522baaf9a330`
- [`vitalitychems-dot/Gitbook`](https://github.com/vitalitychems-dot/Gitbook) — `eefbe2fd53eba6a917c4a078dac15e5beade69da`

Deletion is irreversible. This manifest is a review gate, not an authorization. No repository in the candidate list has been deleted.

## Candidate repositories for deletion

The following **19** repositories are the exact account-level candidates remaining after the two destination repositories were published:

| Repository | Reason staged as candidate | Special review note |
|---|---|---|
| `1` | Repeated application/archive snapshot | Contains an unrelated-history branch that was not imported wholesale. |
| `1T` | Protected vault duplicate/candidate | Contents were not inspected; **do not delete unless explicitly confirmed as intended**. |
| `5t` | Repeated application snapshot | Branch-only memory/audit/screenshot deltas remain unmerged. |
| `Everything` | Coordination/source starter snapshot | Historical handoff material was represented in Gitbook where safe. |
| `Grok-ready` | Prior application baseline | Open unreviewed PRs and legacy refs were not treated as merged. |
| `T44` | Repeated application snapshot | Branch-only agent-memory delta remains unmerged. |
| `TESS` | Repeated application snapshot | No distinct reviewed application role retained. |
| `TX` | Coordination/source snapshot | Branch-only instruction material remains unmerged. |
| `Tessera-main` | Empty/placeholder destination | No active default branch was reported. |
| `Zz` | Repeated application/source snapshot | Historical source index represented in Gitbook. |
| `olive-giant-ever-glade` | Repeated private application snapshot | Non-main default branch `cycle/chamber-text`; review links/refs before deletion. |
| `tessera-complete-archives` | Archive/handoff repository | Handoff summary represented in Gitbook; raw archive is not copied into active docs. |
| `tessera-coordination` | Coordination repository | Coordination records represented in Gitbook. |
| `tessera-gitbook` | Duplicate documentation repository | Documentation represented in Gitbook. |
| `tessera-grok-handoff` | Handoff repository | Privacy-screened summary represented in Gitbook. |
| `tessera-grok-handoff-complete` | Handoff/archive repository | Readable operating/handoff summaries represented in Gitbook. |
| `tessera-replit` | Empty/placeholder repository | No distinct active code retained. |
| `tessera-unified` | Source of the canonical reviewed code | Its tree is now represented in `TESSERA`; preserve source history only if desired. |
| `z` | Source-index/archive repository | Safe index records represented in Gitbook. |

## Required confirmation payload

Before deletion, confirm one of these exact scopes:

1. **Delete all 19 candidates above**, including the protected/uninspected `1T` vault and all non-main branches in the candidate repositories.
2. **Delete a smaller exact subset**, naming every repository to delete and every repository to retain.
3. **Do not delete yet**; keep all candidates archived while the owner reviews the source branches, open PRs, and protected vault.

The deletion operation will be run only against the exact confirmed names and will not touch `TESSERA` or `Gitbook`.
