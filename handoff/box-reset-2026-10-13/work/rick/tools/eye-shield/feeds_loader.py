"""Load public threat-intel feeds into IP/CIDR sets. Keyless, read-only."""
from __future__ import annotations
import csv, gzip, ipaddress, json, os, re
from pathlib import Path

HERE = Path(__file__).resolve().parent
FEEDS = HERE / "feeds"
IP_RE = re.compile(r"\b(?:(?:25[0-5]|2[0-4]\d|[01]?\d?\d)\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d?\d)\b")

def _ips_from_text(text: str) -> set[str]:
    out = set()
    for m in IP_RE.finditer(text):
        out.add(m.group(0))
    return out

def _cidrs_from_lines(lines) -> list[ipaddress.IPv4Network]:
    nets = []
    for line in lines:
        line = line.strip()
        if not line or line.startswith("#") or line.startswith(";"):
            continue
        # Spamhaus DROP: "1.2.3.0/24 ; SBL..."
        tok = line.split(";")[0].split()[0] if line.split() else ""
        if "/" in tok:
            try:
                nets.append(ipaddress.ip_network(tok, strict=False))
            except ValueError:
                pass
        elif IP_RE.fullmatch(tok):
            try:
                nets.append(ipaddress.ip_network(tok + "/32", strict=False))
            except ValueError:
                pass
    return nets

class ThreatFeeds:
    def __init__(self, feed_dir: Path | None = None):
        self.dir = Path(feed_dir or FEEDS)
        self.by_source: dict[str, set[str]] = {}
        self.cidrs: dict[str, list] = {}
        self.kev_cves: set[str] = set()
        self.asn_ranges: list[tuple[int, int, str, str]] = []  # start,end,asn,cc
        self._load()

    def _load(self):
        # Feodo IP blocklist
        p = self.dir / "feodo.txt"
        if p.exists():
            self.by_source["feodo"] = _ips_from_text(p.read_text(errors="ignore"))

        # Tor exits
        p = self.dir / "tor.txt"
        if p.exists():
            self.by_source["tor_exit"] = _ips_from_text(p.read_text(errors="ignore"))

        # FireHOL level1 (CIDRs + IPs)
        p = self.dir / "firehol1.netset"
        if p.exists():
            nets = _cidrs_from_lines(p.read_text(errors="ignore").splitlines())
            self.cidrs["firehol_level1"] = nets

        # Spamhaus DROP
        p = self.dir / "drop.txt"
        if p.exists():
            self.cidrs["spamhaus_drop"] = _cidrs_from_lines(p.read_text(errors="ignore").splitlines())

        # URLhaus IP-bearing rows (trimmed)
        p = self.dir / "urlhaus_ip.csv"
        if p.exists():
            ips = set()
            for line in p.read_text(errors="ignore").splitlines():
                if line.startswith("#"):
                    continue
                ips |= _ips_from_text(line)
            self.by_source["urlhaus"] = ips

        # ThreatFox recent IP:port CSV
        p = self.dir / "threatfox.csv"
        if p.exists():
            ips = set()
            text = p.read_text(errors="ignore")
            for line in text.splitlines():
                if line.startswith("#"):
                    continue
                ips |= _ips_from_text(line)
            self.by_source["threatfox"] = ips

        # CISA KEV (CVE catalog; used for pattern tags, not IPs)
        p = self.dir / "kev.json"
        if p.exists():
            try:
                data = json.loads(p.read_text())
                for v in data.get("vulnerabilities", []):
                    cve = v.get("cveID")
                    if cve:
                        self.kev_cves.add(cve)
            except json.JSONDecodeError:
                pass

        # ip2asn offline (iptoasn.com free TSV.gz)
        p = self.dir / "asn.tsv.gz"
        if p.exists():
            self._load_asn(p)

    def _load_asn(self, path: Path):
        # Columns: range_start range_end AS_number country_code AS_description
        ranges = []
        with gzip.open(path, "rt", errors="ignore") as f:
            for line in f:
                parts = line.rstrip("\n").split("\t")
                if len(parts) < 4:
                    continue
                try:
                    a = int(ipaddress.IPv4Address(parts[0]))
                    b = int(ipaddress.IPv4Address(parts[1]))
                except Exception:
                    continue
                asn = parts[2]
                cc = parts[3]
                ranges.append((a, b, asn, cc))
        ranges.sort()
        self.asn_ranges = ranges

    def match_ip(self, ip: str) -> list[str]:
        hits = []
        try:
            addr = ipaddress.ip_address(ip)
        except ValueError:
            return hits
        if addr.version != 4:
            return hits
        for src, ips in self.by_source.items():
            if ip in ips:
                hits.append(src)
        for src, nets in self.cidrs.items():
            for net in nets:
                if addr in net:
                    hits.append(src)
                    break
        return hits

    def lookup_asn(self, ip: str) -> dict:
        if not self.asn_ranges:
            return {}
        try:
            n = int(ipaddress.IPv4Address(ip))
        except Exception:
            return {}
        lo, hi = 0, len(self.asn_ranges) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            a, b, asn, cc = self.asn_ranges[mid]
            if n < a:
                hi = mid - 1
            elif n > b:
                lo = mid + 1
            else:
                return {"asn": asn, "country": cc}
        return {}

    def stats(self) -> dict:
        return {
            "sources": {k: len(v) for k, v in self.by_source.items()},
            "cidrs": {k: len(v) for k, v in self.cidrs.items()},
            "kev_cves": len(self.kev_cves),
            "asn_ranges": len(self.asn_ranges),
        }
