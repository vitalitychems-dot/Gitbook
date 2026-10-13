#!/bin/bash
# public lookup for inaccessible names; exact-name match, highest stars
out=v2work/lookup.tsv; : >| $out
awk -F, 'NR>1 && $3!="y"{print $1}' REPO-INVENTORY.csv | sort -u | while read r; do
  n=${r#*/}
  d=$(gh api "repos/$r" --jq '[.full_name,(.license.spdx_id//"NONE"),(.description//"")]|@tsv' 2>/dev/null) || d=""
  if [ -z "$d" ]; then
    d=$(gh api -X GET search/repositories -f q="$n in:name" -f sort=stars -f per_page=20 --jq "[.items[]|select(.name|ascii_downcase==\"$(echo $n|tr A-Z a-z)\")|select(.fork==false)][0]|select(.)|[.full_name,(.license.spdx_id//\"NONE\"),(.description//\"\")]|@tsv" 2>/dev/null) || d=""
    sleep 2.2
  fi
  printf "%s\t%s\n" "$r" "${d:-UNKNOWN}" | tr -d '\r' >> $out
done
echo DONE
