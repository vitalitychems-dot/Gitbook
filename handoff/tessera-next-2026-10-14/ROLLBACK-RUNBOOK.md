# Tessera rollback runbook — gated, not yet executable

**Current status:** No deployment or prior immutable production artifact has been verified; therefore there is **no current production rollback target**. This document defines the future procedure and does not claim a rollback system is configured.

## Before first production deployment

- The selected host must support immutable versioned releases, health checks, logs, immediate traffic rollback, and a documented prior-release selector.
- Record the exact previous known-good artifact digest and source merge SHA before promotion. Keep secrets in the host secret manager; rollback must not print or export them.
- Take a verified database backup/snapshot and record its time, encryption/retention policy, restore procedure, and owner. Classify schema migrations as backward-compatible, reversible, or restore-required.
- Confirm the public health route, API origin, domain/TLS and operator with authority to halt traffic.

## Rollback triggers

Halt or roll back if any production gate fails: HTTPS/domain/TLS, health endpoint, API connectivity, session gate, protected-route access control, unauthorized access, database migration/data integrity, secret leakage, responsive behavior, monitoring/alerting or release-artifact identity.

## Procedure after an approved deployment exists

1. Stop further promotion; preserve failing logs and exact deployment ID/commit/artifact digest without secrets.
2. If application-only and the prior image is compatible with current schema, route traffic to the prior immutable deployment using the host-native rollback control. Verify public HTTPS, health, API, session gate and protected-route denial.
3. If a migration is involved, do **not** blindly downgrade. Follow the migration's reviewed backward-compatibility plan. If destructive or irreversible, pause writes and restore the approved database snapshot under the owner's direction; verify consistency before reopening traffic.
4. Reconfirm secret names/configuration without revealing values, TLS, CORS, cookie behavior, logs/alerts and any background worker state.
5. Record trigger, start/end time, operator, old/new release IDs, source SHAs, data action/backup ID, health results, user impact, and corrective PR in Gitbook. Do not label resolved until the restored release passes the required gates.

## Current stop condition

Because there is no selected provider/project, no release ID, no production URL, and no database or monitoring evidence, do not attempt a host-specific command or invent a rollback target. Select and authorize the exact host first; then fill in and test its native steps in a reviewed deployment record.
