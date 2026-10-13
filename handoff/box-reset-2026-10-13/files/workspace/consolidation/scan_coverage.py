#!/usr/bin/env python3
"""Read-only blob-SHA coverage scan (Tessera consolidation, 2026-10-05).
Inputs: raw/trees/<repo>.json = GitHub get_git_tree(recursive) output fetched via cursor-github MCP.
A source blob is COVERED when its git blob SHA appears anywhere in TESSERA main or Gitbook main
(git blob SHA equality == byte-identical content). 1T is never fetched or scanned (PROTECTED).
Writes raw/uncovered.json and prints per-repo coverage, plus coverage by dest+all other source repos."""
import json, glob, os
R = os.path.join(os.path.dirname(__file__), 'raw', 'trees')
trees = {os.path.basename(f)[:-5]: [e for e in json.load(open(f))['tree'] if e['type'] == 'blob']
         for f in glob.glob(R + '/*.json')}
dest = {e['sha'] for n in ('TESSERA', 'Gitbook') for e in trees[n]}
src = [n for n in trees if n not in ('TESSERA', 'Gitbook')]
out = {}
for n in sorted(src):
    unc = [e for e in trees[n] if e['sha'] not in dest]
    repo = n.split('__')[0]
    others = {e['sha'] for m in src if m.split('__')[0] != repo for e in trees[m]}
    unc2 = [e for e in unc if e['sha'] not in others]
    print(f"{n}: files={len(trees[n])} covered_by_dest={len(trees[n])-len(unc)} uncovered={len(unc)} "
          f"({sum(e.get('size',0) for e in unc)/1e6:.1f} MB); uncovered_by_dest+siblings={len(unc2)}")
    out[n] = [(e['path'], e.get('size', 0), e['sha']) for e in unc]
json.dump(out, open(os.path.join(os.path.dirname(__file__), 'raw', 'uncovered.json'), 'w'))
