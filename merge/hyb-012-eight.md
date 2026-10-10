# HYB-012 eight non-quantum duplicates

Status: triaged. Not deleted.

The first mounted module answers. The second registration stays, because the inventory test pins the collision. Removing one would fail that test. A later deletion has to update the allow list in the same change.

| Method and path | Answers | Shadowed |
|---|---|---|
| GET /consciousness/state | sovereign-engines.ts | legacy-engines.ts |
| GET /consensus/proposals | governance-consensus.ts | legacy-engines.ts |
| GET /dual-brain/state | sovereign-engines.ts | legacy-engines.ts |
| GET /emotional/profile | sovereign-engines.ts | legacy-engines.ts |
| GET /universe/metrics | system-runtime.ts | universe.ts |
| POST /consensus/propose | governance-consensus.ts | legacy-engines.ts |
| POST /improvement/cycle | improvement.ts | legacy-engines.ts |
| POST /universe/simulate | system-runtime.ts | legacy-engines.ts |

The two quantum routes stay on the existing allow list. No route file was edited.

Checked 2026-10-10 against TESSERA `artifacts/api-server/src/__tests__/route-inventory.test.ts` on main.
