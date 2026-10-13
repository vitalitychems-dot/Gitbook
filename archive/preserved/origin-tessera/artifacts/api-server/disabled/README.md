# disabled

These files are out of the API build. `tsconfig.json` includes only `src/`, and nothing under `src/` imports this directory.

Moved here so they cannot start at boot:

- `wallet-observer.ts`
- `income-executor.ts`
- `free-stuff-scraper.ts`
- `code-bounties-real.ts` (bounty refresher)
- `lead-execution.ts` (only caller was the income lead feed)

`income-and-leads.original.ts` is the route file before the cut. The live route file keeps recruit-dossier and shepherd-negotiation routes only. These routes are gone: `/income/wallet`, `/income/wallet/refresh`, `/income/strategies`, `/leads/feed`, `/free-stuff`, `/free-stuff/refresh`, `/code-bounties`, `/code-bounties/:id/attempt`, `/code-bounties/attempts`.

`git revert` of the commit that moved them puts the files back. Wiring them into `src/routes/index.ts` again is a separate decision.
