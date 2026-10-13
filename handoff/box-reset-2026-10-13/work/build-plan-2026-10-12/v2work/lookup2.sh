#!/bin/bash
set -u
out=v2work/lookup2.tsv
: >| "$out"
# reuse good rows already
awk -F'\t' 'NF>=4 && $2!="UNKNOWN" && $2!~/message/{print}' v2work/lookup.tsv >| "$out" 2>/dev/null || true
done_names=$(cut -f1 "$out" 2>/dev/null | while read r; do echo "${r##*/}"; done | sort -u)
while read n; do
  echo "$done_names" | grep -qx "$n" && continue
  # exact public name match, highest stars, not fork
  d=$(gh api -X GET search/repositories -f "q=${n} in:name fork:false" -f sort=stars -f per_page=10 \
    --jq "[.items[]|select(.name|ascii_downcase==\"$(echo "$n"|tr A-Z a-z)\")][0]|select(.)|[.full_name,(.license.spdx_id//\"NONE\"),(.description//\"\")]|@tsv" 2>/dev/null) || d=""
  if [ -z "$d" ]; then
    printf "%s\tUNKNOWN\n" "name/$n" >> "$out"
  else
    printf "%s\t%s\n" "name/$n" "$d" >> "$out"
  fi
  sleep 1.1
done < v2work/names.txt
echo DONE
