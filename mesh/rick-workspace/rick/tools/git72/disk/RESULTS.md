# (5) Disk — autoclean fix
Changed: /workspace/ops/autoclean.sh, step 3 (in place; no second script).
Bug: git pack/loose objects are mode 444 and `jdupes -L` refuses read-only targets ("link target is a read-only file, not linking"). So the dedup step always saved 0 (log: `reclaimed=0G`).
Fix: `hardlink -q -f` (util-linux) over every `*/.git/objects` dir. Filenames are content hashes, so files that match by name and content are safe to share. jdupes still handles archive dirs. Reclaim is now logged in MB, not G.
Fixture (3 copies of a 20-page repo): old 888,832→888,832 B (saved 0); new 888,832→831,488 B (saved 57,344 B, 6.5%); fsck OK.
Live box dry run (`hardlink -n -f`, 173 objects dirs): would save 786 KiB in 0.11 s. Small but not zero. Real gains will come from step 4 and from reaching Father's list, not dedup.
Archive step left unchanged: 94,208 B dir → tar 40,960 → tar.zst -19 1,583 B (~60× vs du).
KEPT.
