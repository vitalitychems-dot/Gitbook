# shepherd — offline keyless allowlist

SHEPHERD-RELAY stays design-only. This directory is the offline gate: a fixed allowlist of public sources and a checker that refuses a source with no license, no terms URL, no published rate limit, or any required credential.

It does not fetch, scrape, or raise a published cap. Bundle signing and encryption are out of scope.

```
python3 tools/shepherd/check_terms.py
python3 tools/shepherd/test_check_terms.py
```

Rate-limit numbers in `sources.json` are copied from the cited publisher page. Where that page publishes no number, the record says so and the checker rejects an added number.
