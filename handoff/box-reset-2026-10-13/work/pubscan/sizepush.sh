set -u; set +o noclobber
cd /workspace/pubscan/final.git
base=$1; LIM=${LIM:-400000000}; acc=0; prev=$base
for c in $(git rev-list --reverse --topo-order $base..main); do
  sz=$(git rev-list --objects $prev..$c | cut -d' ' -f1 | git cat-file --batch-check='%(objectsize:disk)' | awk '{s+=$1}END{print s+0}')
  if [ $sz -ge $LIM ] || [ $c = $(git rev-parse main) ]; then
    s=$(date +%s); git push --force origin $c:refs/heads/tmp-scrub-push >|/tmp/cp.log 2>&1; r=$?
    echo "${c:0:8} ~$((sz/1000000))MB rc=$r $(( $(date +%s)-s ))s"; [ $r -ne 0 ] && { tail -3 /tmp/cp.log; exit 1; }
    prev=$c
  fi
done
