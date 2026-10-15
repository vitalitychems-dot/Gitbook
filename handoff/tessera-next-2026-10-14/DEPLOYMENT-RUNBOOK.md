# Tessera deployment runbook — gated, not yet executable

**Current status:** NOT DEPLOYED. No provider/project is selected or authorized, no immutable release exists, no production URL exists, no database migration is recorded, and no production secret has been entered. The GitHub record confirms no deployments, releases, or Pages site. This runbook is a readiness checklist, not evidence of publication.

## Architecture constraints

- Tessera is a full-stack application: serve the frontend and Node API server together or use an explicitly approved supported backend origin. The entry gate posts credentials to `/api/admin/session`; successful authentication uses an HttpOnly session cookie. A static-only GitHub Pages deployment is not a valid current architecture.
- `TESSERACT_ADMIN_KEY` must be created directly in the selected host's encrypted server-side secret manager. Never place its value in chat, an issue, a PR, Gitbook, a repository, a frontend build variable, local build logs, or browser storage.
- Database integration validation requires a dedicated disposable test database. Production schema/migration, backups, restore, logging, rate limits, monitoring, TLS, CORS, cookie attributes, health endpoint, and rollback must be documented for the chosen host before release.

## Approval required before execution

The user/hosting owner must identify and authorize all of the following as one deployment target:

1. Provider and exact connected account/project identifier (not merely a provider name).
2. Runtime/service type and region; exact merged Git commit SHA to deploy.
3. Public hostname/custom-domain and TLS ownership, allowed origins, and backend/API origin.
4. Database provider/instance, migration and backup/restore procedure, and whether it is managed by the host.
5. Host-native secret-store path for `TESSERACT_ADMIN_KEY`; the secret value itself is entered only by the user in that UI and is never collected by the agent.
6. Health-check route, logs/metrics/alerts, release immutability, rollback mechanism, and the person authorized to approve production rollout.

A hosting connector activation that was previously refused will not be proposed again unless the user explicitly requests it. The only next approval request is to name an already-authorized provider/project and the above operational choices.

## Release gates after a reviewed merge

1. Record the merge commit SHA; verify it is the exact source of the release artifact. Build an immutable image/artifact and retain its digest.
2. Run typechecks, full unit suites, route-manifest validation, dependency and secret scans, API integration tests against a disposable test database, and production build. Record commands/environment class/time/result/commit SHA.
3. Deploy to a non-production environment first. Configure TLS, backend origin, CORS, `Secure`/`HttpOnly`/appropriate `SameSite` cookie settings, server-side secret name, database migration, least-privilege networking, logs, health, rate limits, backups and rollback.
4. User enters the production or non-production test secret only in the host secret UI. Verify only the secret **name/configuration state**, never read or echo the value.
5. Verify unauthenticated protected-route denial; invalid credential denial; authorized test access after a non-production secret is configured; session expiry/logout behavior; API connectivity; browser-storage fallback; desktop/mobile behavior; and absence of secret leakage in client bundles, logs, responses and repository scans.
6. Obtain owner/security approval. Promote the immutable candidate. Capture exact deployment ID, URL, timestamp, provider/project ID, health responses, migration state, monitoring state, and rollback target in Gitbook.
7. Verify public HTTPS, health endpoint, API session behavior, protected-route denial/authorized test, responsive behavior, domain/TLS, logs/alerts and rollback readiness from the public URL. If any gate fails, roll back or halt.

## Required publication receipt

Do not mark HYB-023 complete or call Tessera published until the release record contains: merged SHA; immutable release/deployment ID; public HTTPS URL; provider/project identifier; deployment timestamp; health evidence; security review; migration/backup status; known limitations; rollback target; and exact Gitbook handoff link. None of those production receipts exists as of this snapshot.
