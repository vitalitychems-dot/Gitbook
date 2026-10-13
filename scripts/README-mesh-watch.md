# mesh-watch + shallow-work (Lane: disk-cleaner)

## mesh-watch.sh — no-token PR watcher
Plain bash + curl + jq. No LLM runs, so it costs no tokens. Every run it watches `vitalitychems-dot/TESSERA` and `vitalitychems-dot/Gitbook`:
- `GET /pulls?state=open` (1 call per repo) gives each PR's head SHA
- `GET /issues/comments?since=<last run>` (1 call per repo) counts new comments that contain `GATE`
- `GET /pulls/<n>` only for PRs that disappeared since the last run, to tell merged from closed

It compares the results against `/workspace/mesh/state.json` (written to a temp file, then `mv`) and appends **only changes** to `/workspace/mesh/changes.jsonl`:
```json
{"ts":"…Z","repo":"Gitbook","pr":111,"event":"opened|pushed|gate_comment|merged|closed|DONE","sha":"…"}
```
A PR that closes as merged gets a `merged` line and then a `DONE` line. The first run only seeds the state and writes no lines. A run that finds nothing new writes nothing.
Optional `GITHUB_TOKEN` is read from the env (the repos are private, so unauthenticated calls return 404). A 403 or 429 rate-limit response ends the run cleanly and keeps the previous state. `flock` stops runs from overlapping.

Sample crontab (**not installed**; Tessera gates first):
```
*/10 * * * * GITHUB_TOKEN=... /workspace/Gitbook/scripts/mesh-watch.sh >>/workspace/mesh/watch.log 2>&1
```

## How bots read changes.jsonl (offset-file pattern)
Bots stop polling GitHub. On their own timer, each bot reads only the bytes added since its last read:
```bash
F=/workspace/mesh/changes.jsonl; OFF=/workspace/mesh/.offset-<lane>
o=$(cat "$OFF" 2>/dev/null || echo 0); s=$(stat -c%s "$F" 2>/dev/null || echo 0)
[ "$s" -lt "$o" ] && o=0                        # file rotated
if [ "$s" -gt "$o" ]; then
  tail -c +$((o+1)) "$F" | head -c $((s-o)) | jq -c 'select(.repo=="Gitbook")'   # act on these
  echo "$s" > "$OFF.tmp" && mv "$OFF.tmp" "$OFF"
fi
```
If the offset hasn't moved, there is nothing to do, so the bot doesn't wake an LLM turn.

## shallow-work.sh — throwaway clones
```bash
d=$(SW_SPARSE="scripts" scripts/shallow-work.sh <lane> https://github.com/vitalitychems-dot/Gitbook.git main)
# …work, commit, push…
scripts/shallow-work.sh finish "$d" <branch>   # rm -rf only if HEAD == ls-remote origin <branch> and the tree is clean
```
Guards: the target must be a direct child of `/workspace/tmp/`. Anything matching `/workspace/scan`, `/workspace/secscan` or `agent-data` is refused, both before and after symlinks are resolved.
