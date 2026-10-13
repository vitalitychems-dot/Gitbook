#!/bin/bash
# runs scripts, v2, gitai tests on node22; prints summary
export PATH=/home/box/.npm/_npx/52027bd8fc0022aa/node_modules/node/bin:$PATH
cd ${1:-.}
r=0
for d in scripts artifacts/v2 artifacts/gitai; do
  out=$(cd $d && timeout 600 node --experimental-strip-types --disable-warning=ExperimentalWarning --test --test-force-exit $( [ $d = scripts ] && echo ./suite-policy.test.mjs ./historical-merge-gate.test.mjs ./eval/write-result.test.mjs || echo test/*.test.mjs) 2>&1)
  echo "$d: $(echo "$out" | grep -E '^# (pass|fail)' | tr '\n' ' ')"
  echo "$out" | grep -E "^not ok" | head
  echo "$out" | grep -q '^# fail 0' || r=1
done
exit $r
