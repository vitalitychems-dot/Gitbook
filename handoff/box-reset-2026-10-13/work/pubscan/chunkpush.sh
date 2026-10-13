set -u
cd /workspace/pubscan/final.git
mapfile -t C < <(git rev-list --first-parent --reverse main)
N=${N:-15}; n=${#C[@]}
for ((i=N-1;i<n;i+=N)); do
  s=$(date +%s); git push --force origin ${C[$i]}:refs/heads/tmp-scrub-push >/tmp/cp.log 2>&1; r=$?
  echo "idx $i ${C[$i]:0:8} rc=$r $(( $(date +%s)-s ))s"; [ $r -ne 0 ] && { tail -5 /tmp/cp.log; exit 1; }
done
s=$(date +%s); git push --force origin ${C[$((n-1))]}:refs/heads/tmp-scrub-push >/tmp/cp.log 2>&1; echo "tip rc=$? $(( $(date +%s)-s ))s"
