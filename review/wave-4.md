# Fourth twenty

The test passed. These are function results, not a new ability.

- A scaled action of -1 between 0 and 10 is 0. A scaled 1 is 10. Unscaling 10 returns 1.
- `dir/note.in` becomes `note`. `note.txt` becomes nothing.
- Version `1.0.0` matches. `nope` does not.
- Warmup of 0.5 at epoch 2 of 4 is 0.25.
- A leak of 1 with input 0.2 and beta 0.9 is 1.1.
- A hard reset of a spike is 0. A soft reset is 1.
- An average of 2 then 4 is 3. Hidden rewards 3 then 2 sum to 5.
- A last step discounts by 0. A middle step discounts by 1.
- Hunger 0.5 becomes 0.6. Fatigue 0.5 becomes 0.55.
- A permutation with a zero roll stays ordered: index 0 is 0, index 255 is 255.
- The skew matches `0.5 * (sqrt(3) - 1)`.

GitHub main of TESSERA received `preview/src/lib/tessera/wave-4.ts` in the same pass. This page does not claim the other waves are on main.
