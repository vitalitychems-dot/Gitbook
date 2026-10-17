# Tessera UI/theme retirement assessment

**Snapshot:** 2026-10-15 10:29–10:31 UTC, based on fetched GitHub `origin/main` trees and exact live PR records. This is a path/metadata assessment, not approval to delete files.

## Executive conclusion

The user has asked to remove theme/UI files from TESSERA and Gitbook. **No files were deleted in this pass.** The proposed blanket removal still conflicts with the objective of a working full-stack app, which needs a usable frontend. Before implementing a removal, the product owner must resolve whether the intention is to replace only the current theme layer while retaining a minimal frontend, or to intentionally leave the app without a frontend until a replacement is ready.

TESSERA PR #372 was merged by the repository owner `vitalitychems-dot` at 2026-10-15 10:25:58 UTC, producing merge commit `564811dc5f74073802e38c701ec98b4c32402bc3`. This session did not merge it. The PR-head checks were successful; the merge-commit CI, secret scan, and provenance workflows also succeeded. PR #367 was closed unmerged at 10:26:01 UTC. The only open TESSERA PR now observed is #361; it is conflicting with the current base, has no review decision, and contains broad deletions plus changes to active UI paths. Do not merge it based on its title or the broad deletion request alone.

No TESSERA, GitMesh, or Box source content was copied or changed. A redacted path-only census is proposed for the Gitbook handoff; it is not a dependency graph or deletion list. The Gitbook handoff remains a PR proposal until its exact current head passes CI and normal review.

## Exact repository snapshots

| Repository | Ref and commit | Tracked paths | Path-only finding |
|---|---|---:|---|
| TESSERA | `origin/main` — `564811dc5f74073802e38c701ec98b4c32402bc3` | 3,641 | 547 paths have UI-source-like extensions; 337 are outside paths named archive/history/handoff. Main candidate areas: `artifacts/tessera` (218), `artifacts/mockup-sandbox` (64), `preview/src` (47), `artifacts/console` (2), plus `preview/index.html` and other paths. Candidates for dependency review only. |
| Gitbook | `origin/main` — `17cdbdbae3e98001cca1b2365b834ab10431ac54` | 14,690 | 906 UI-source-extension paths, all under historical roots: 858 under `archive`, 48 under `handoff`. Preserve as historical evidence; no active app UI surface was identified by this path heuristic. |
| GitMesh | `origin/main` — `602d6559c7d3d912e8cc5b43914d1193700c02b0` | 28 | One `index.html`; no path-named theme/style files. GitMesh remains a separate proposal surface. |

The path census used NUL-delimited `git ls-tree -r -z --name-only` output. It treated `.html`, `.htm`, `.css`, `.scss`, `.sass`, `.less`, `.tsx`, `.jsx`, `.vue`, and `.svelte` as UI-like extensions. This is a heuristic, **not** a build/dependency graph. A path outside an archive folder is not necessarily production code; a path inside an archive is not disposable.

A redacted path-only inventory is available at [UI-THEME-PATH-INVENTORY-2026-10-15.tsv](UI-THEME-PATH-INVENTORY-2026-10-15.tsv). It has 1,422 rows; 32 sensitive or ambiguous pathnames are withheld. Rows are marked review-only or preserve; none is an approved deletion.

## Current non-archive theme/style-named paths in TESSERA

The path-name scan found 11 matches; names alone do not establish that any are unused:

1. `.agents/skills/remotion-best-practices/rules/tailwind.md` — reference guidance.
2. `.agents/skills/ui-ux-pro-max/data/stacks/html-tailwind.csv` — reference data.
3. `.agents/skills/ui-ux-pro-max/data/styles.csv` — reference data.
4. `artifacts/tessera/src/lib/theme-constants.ts` — app source; imported by active UI.
5. `artifacts/tessera/src/styles/tessera-next.css` — active production theme layer introduced by merged PR #372.
6. `artifacts/v2/src/brain/creator/style.mjs` — V2/creator code; not assumed to be current app styling.
7. `preview/src/components/tessera/theme-view.tsx` — preview component.
8. `preview/src/lib/tessera/themes.test.ts` — preview test.
9. `preview/src/lib/tessera/themes.ts` — preview source.
10. `preview/src/styles.css` — preview stylesheet.
11. `scripts/tessera-next-theme.test.mjs` — test file for the production theme.

This path list is a locator only. It is **not** an exhaustive file list for a user-defined category called “UI,” because many UI files have no theme/style wording in their names.

## GitHub pull-request gates

- [TESSERA PR #372](https://github.com/vitalitychems-dot/TESSERA/pull/372): GitHub records `MERGED` at 2026-10-15 10:25:58 UTC, merger `vitalitychems-dot`, merge commit `564811dc5f74073802e38c701ec98b4c32402bc3`. The six PR checks succeeded. Post-merge [CI run 38720223367](https://github.com/vitalitychems-dot/TESSERA/actions/runs/38720223367), [secret scan 38720223533](https://github.com/vitalitychems-dot/TESSERA/actions/runs/38720223533), and [provenance run 38720223390](https://github.com/vitalitychems-dot/TESSERA/actions/runs/38720223390) all succeeded. This proves the merge and those workflows, not a permanent deployment.
- [TESSERA PR #367](https://github.com/vitalitychems-dot/TESSERA/pull/367): closed unmerged at 2026-10-15 10:26:01 UTC; no merge commit. Its Replit source was unavailable and no code from it was imported.
- [TESSERA PR #361](https://github.com/vitalitychems-dot/TESSERA/pull/361): open at head `e8beb40086cb91dbe2c2ee59fc57ee8cd5b68f45`, based on `00d6dc7ad7b5ebf390ed33345b28c698b89d2056`, `CONFLICTING`, no review decision. GitHub reports 201 changed files, 99 additions, and 60,774 deletions; the diff endpoint exceeds its 20,000-line limit, so this was not a full content review. Path metadata shows it deletes active `ChatFontColorPicker.tsx`, `theme-constants.ts`, preview `theme-view.tsx`, `themes.ts`, and `themes.test.ts`, while also changing other active app/preview files and deleting historical files. Do not merge while conflicting or without a path-level dependency, restoration, and test review.
- [Gitbook PR #123](https://github.com/vitalitychems-dot/Gitbook/pull/123): at the latest pre-follow-up check, open at head `4a9e68ef860a1ab2bf4e713eccffea1b7e5790a4`; [run 38698025357](https://github.com/vitalitychems-dot/Gitbook/actions/runs/38698025357) failed on the previously documented historical JSON-validation blocker. The protected artifact was not touched and validation was not suppressed. Any new documentation commit requires a fresh exact-head check.

## Replit access limitation

The three supplied project URLs were not publicly accessible in the Sandbox browser. The first supplied invitation URL redirected to Replit login; the other invitation URLs were not tested. The user reports that login is not working. No invitation was accepted, no Replit source was read, and no code was imported. The invitation scope could not be verified, so the authorized condition to stop if scope is elevated or unclear remains applicable. The Replit-named PR #367 is closed unmerged and does not prove access to a live Replit session.

## Safe next work

1. Keep TESSERA PR #361 unmerged until its conflicts, active-path effects, historical deletions, and restoration plan have been reviewed on the current base.
2. Resolve the UI scope conflict: a working full-stack app needs some frontend. If the direction is to retire only the newly merged theme layer, trace its imports, route registration, build entrypoints, preferences, tests, API/session dependencies, and replacement behavior first. If all UI is intentionally removed, record that the app will not meet the working-product objective until a replacement ships.
3. Obtain read-only source exports or accessible repository snapshots for the Replit projects. Keep invitation tokens and credentials out of public issues.
4. Distinguish production UI from preview, console, mockups, tests, skills/reference data, archives, and docs. Require a path-by-path dependency/consumer search, behavior replacement, tests, restoration location, and review before any deletion.
5. Keep Gitbook as the cross-agent source of truth; do not copy app source or historical archives into it. The redacted path manifest is metadata only.

## Validation and limitations

The census read tracked path names only at the exact commits above; it did not read all blob contents, run the TESSERA app, build a complete dependency graph, or test deletions. PR #361’s oversized diff was not fully reviewed. Therefore this assessment supports **scope and risk triage only**; it does not establish that any file is safe to remove or that the app is complete, permanently hosted, synchronized, or published.
