# Validation report — staged TESSERA build

**Checked:** 2026-10-05, against the staged two-repository build. The earlier 2026-10-02 report remains in the source repository as historical provenance; this page records the current rerun.

## Environment and dependency checks

- Validation ran on Node.js 22 with pnpm 11.25.0. `pnpm install --frozen-lockfile --ignore-scripts` completed for all 9 staged workspace projects.
- `pnpm audit --prod --audit-level=high` is clean. Full-tree audit reports one high-severity transitive `braces@3.0.3` advisory through the dev-only `fast-glob` path in `@workspace/mockup-sandbox`; the advisory reports no patched version. Production dependency exposure is not affected; the advisory remains a TODO for dependency replacement or upstream remediation.
- The `.github/workflows/ci.yml` file parses as YAML and contains push/PR checks with read-only `contents` permission. GitHub-hosted CI has been configured but has not yet run on GitHub.
