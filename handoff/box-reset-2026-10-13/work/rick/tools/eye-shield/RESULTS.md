# Eye Shield — Anti-Surveillance Expansion RESULTS

**When:** 2026-10-13 (America/Chicago, UTC-5)
**Scope:** Defensive detection only. Read our logs, fingerprint probes/scanners/OSINT/surveillance tools that hit *us*, map attacker IP→ASN/country from offline free feeds, alert on mesh bus.
**Hard limits kept:** no malware installed, no outbound scanning of others, no camera feeds, no firewall rule changes (Security REJECTED firewall plan earlier).

## What was added

| Path | Role |
|---|---|
| `signatures/catalog.json` | 20 public defensive signatures (7 citations) |
| `signatures/matcher.py` | Regex matcher, aggregate by (sig_id, ip) |
| `detector.scan_signatures` / `scan_all` | Wire signatures into classic detector |
| `fixtures/surveillance_probes.log` | 17-line attack fixture (Flock-style, Argos-style, Camofox, scanners, Red Sparrow C2) |
| `fixtures/surveillance_benign.log` | Clean control log |
| `alert.py` | Extra mesh bus alert for anti-surveillance signature hits |
| `run_once.py` | Uses `scan_log_file_all`, reports signature stats, merges tool tags + intel |

## Public sources studied (defense only)

1. **FLOCK_SCAN** (github.com/ekomsSavior/FLOCK_SCAN README) — ONVIF `GetDeviceInformation`, `admin_page_template.html`, ADB:5555, FRP:7000–7500, ONVIF:8899, flocksafety.com strings. We detect those *probes against us*.
2. **Camoufox / CamoFox Browser** (daijro/camoufox, redf0x1/camofox-browser) — project-name UA + leftover HeadlessChrome/Playwright/Puppeteer leaks.
3. **Red Sparrow** (Iankulani/red-sparrow README) — C2 over Discord/Slack/Telegram webhook/bot APIs; name IOC; fetch-piped-to-shell.
4. **Argos Atlas** (argosatlas.com) — class of public-camera URL aggregators; we detect scrapers hitting *our* camera-shaped paths (`/mjpg/`, `/axis-cgi/`, `SnapshotJPEG`, insecam-style markers).
5. **Common scanners** — nmap, masscan, zgrab, nuclei, nikto/sqlmap, Shodan/Censys UAs (Sigma/fail2ban-adjacent).

Nothing from those projects was installed or run. Catalog stores detection regexes only.

## Measured test numbers (`python3 test_shield.py`)

| Metric | Value |
|---|---|
| Classic fixture precision | **1.000** (tp=7 fp=0) |
| Classic fixture recall | **1.000** (fn=0) |
| Surveillance signature precision | **1.000** (tp=14 fp=0) |
| Surveillance signature recall | **1.000** (fn=0) |
| Required signature IDs that fired | **13 / 13** |
| Extra benign-safe patterns also fired on attack fixture | probe.honeypot_paths, probe.path_traversal_admin, scan.python_requests_probe |
| Signature catalog size | **20** rules in **6** families |
| Offline ASN ranges loaded | **539,096** |
| Threat-intel IP/CIDR (approx unique) | feodo 5 + tor 1,207 + urlhaus 6,569 + threatfox 2,908 + firehol 4,635 CIDRs + spamhaus DROP 1,677 |
| CISA KEV CVEs | **1,739** |
| ASN lookup check (1.1.1.1) | ASN **13335**, country **US** |
| Anomaly scorer (quiet → hot) | **48.4 → 100.0** (warn=True on hot) |
| Mesh bus messages from alert test | **3** (high findings + anti-surveillance + anomaly warn) |
| Combined scan throughput | **11,738 lines/s** (1,800 lines → 119 findings in 0.1533 s) |
| Listening ports snapshot (read-only `ss`) | **57** rows |
| Fixture scan findings (`run_once.py --fixtures`) | **37** findings, **24** Eye layer points |
| Tree size | **13 MB** (limit 30 MB) |

## Signature families (catalog)

| Family | Count | Examples |
|---|---|---|
| scanner | 7 | nmap, masscan, zgrab, nuclei, nikto/sqlmap, shodan/censys, python-requests+probe-path |
| surveillance_scanner | 4 | flock ONVIF / admin template / API hosts / ADB-FRP port blocks |
| stealth_browser | 2 | Camoufox UA, HeadlessChrome/Playwright |
| osint_scraper | 2 | Argos-style camera paths, insecam-style |
| c2_framework | 3 | Red Sparrow–style messaging C2, name IOC, pipe-to-shell |
| web_probe | 2 | path traversal/admin, honeypot admin paths |

## Mesh bus

Alerts append to `/workspace/rick/tools/collab/eye-shield-bus.jsonl` (Eye Shield's own JSONL; not the gated Gitbook mesh schema). Anti-surveillance hits use `ref=eye-shield-antisurveillance`, `to=security`. Eye layer JSON: `out/eye-shield-layer.json`.

## What we did **not** do

- Did not install Red Sparrow, Camofox, Flock_SCAN, or Argos.
- Did not scan external hosts or camera networks.
- Did not ingest live camera feeds.
- Did not apply firewall rules (Security gate: REJECTED; port 2375 remains platform-internal MEDIUM).
- Did not change Docker or open outbound C2 channels.

## How to re-run

```bash
cd /workspace/rick/tools/eye-shield
python3 test_shield.py
python3 run_once.py --fixtures
# live box (read-only logs if readable):
python3 run_once.py
```

## Note on fixture IPs

RFC5737 documentation ranges (203.0.113.0/24, 198.51.100.0/24, 192.0.2.0/24) appear in FireHOL level1 via adjacent CIDRs (e.g. 203.0.112.0/23). Offline ASN maps them to ASN 0 / country None. Real public attacker IPs get real ASN/CC from `feeds/asn.tsv.gz` (iptoasn.com free dump).
