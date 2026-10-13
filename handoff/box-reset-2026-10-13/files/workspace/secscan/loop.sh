prev=-1; stable=0
for i in $(seq 1 8); do
 cd /workspace/rea-batch
 for r in */; do r=${r%/}; case $r in *1T*|*vault*|b2-out) continue;; esac; m=$(stat -c %Y $r); [ -f /workspace/secscan/out/$r.ok ] && [ $(stat -c %Y /workspace/secscan/out/$r.ok) -gt $m ] && continue; /workspace/secscan/scan.sh /workspace/rea-batch/$r /workspace/secscan/out; done
 c=$(ls -d */ | wc -l); echo "$(date +%H:%M) pass=$i dirs=$c"; [ $c = $prev ] && stable=$((stable+1)) || stable=0; prev=$c; [ $stable -ge 3 ] && break; sleep 180
done; echo LOOPDONE
