"""Defensive log/process watcher. Patterns modeled on Sigma (DRL) + fail2ban-style regexes.
Sigma rule concepts cited: failed SSH auth, invalid users, web probes, reverse shell indicators.
No exploitation. Read-only."""
from __future__ import annotations
import ipaddress, os, re, subprocess, time
from collections import defaultdict
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Iterable

IP_RE = re.compile(r"\b(?:(?:25[0-5]|2[0-4]\d|[01]?\d?\d)\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d?\d)\b")

# fail2ban-style / Sigma-inspired patterns (cite: SigmaHQ sshd_brute.yml, web_shell_probe ideas)
PATTERNS = [
    ("bruteforce", re.compile(r"Failed password for (?:invalid user )?(\S+) from (?P<ip>\d+\.\d+\.\d+\.\d+)", re.I)),
    ("invalid_user", re.compile(r"Invalid user (\S+) from (?P<ip>\d+\.\d+\.\d+\.\d+)", re.I)),
    ("ssh_connection", re.compile(r"Connection (?:from|closed by) (?P<ip>\d+\.\d+\.\d+\.\d+)", re.I)),
    ("firewall_block", re.compile(r"(?:UFW BLOCK|iptables|DROP).*SRC=(?P<ip>\d+\.\d+\.\d+\.\d+).*DPT=(?P<port>\d+)", re.I)),
    ("web_probe", re.compile(r"(?P<ip>\d+\.\d+\.\d+\.\d+).*(?:wp-login\.php|\.env|phpmyadmin|/etc/passwd|shell\?cmd=|union\s+select|nikto|sqlmap)", re.I)),
    ("suspicious_command", re.compile(r"(?:curl|wget).*(?:\| *bash|\| *sh|/payload|/malware)|COMMAND=/bin/bash|nc\s+-e\s+/bin", re.I)),
]

BRUTE_THRESHOLD = 5          # failed pw in window
SCAN_THRESHOLD = 10          # distinct ports or rapid connections from one IP
BLOCK_PORT_THRESHOLD = 3     # distinct blocked ports

PRIVATE = (
    ipaddress.ip_network("10.0.0.0/8"),
    ipaddress.ip_network("172.16.0.0/12"),
    ipaddress.ip_network("192.168.0.0/16"),
    ipaddress.ip_network("127.0.0.0/8"),
    ipaddress.ip_network("169.254.0.0/16"),
)

def is_public(ip: str) -> bool:
    try:
        a = ipaddress.ip_address(ip)
    except ValueError:
        return False
    return not any(a in n for n in PRIVATE)

@dataclass
class Finding:
    kind: str
    ip: str | None
    detail: str
    source: str
    count: int = 1
    ports: list = field(default_factory=list)
    feed_hits: list = field(default_factory=list)
    asn: str | None = None
    country: str | None = None
    pattern: str | None = None
    severity: str = "medium"

    def to_dict(self):
        return asdict(self)

def scan_log_text(text: str, source: str = "log") -> list[Finding]:
    """Scan text for attack patterns; aggregate by IP+kind."""
    failed: dict[str, int] = defaultdict(int)
    invalid: dict[str, int] = defaultdict(int)
    conns: dict[str, int] = defaultdict(int)
    blocked_ports: dict[str, set] = defaultdict(set)
    web: dict[str, list] = defaultdict(list)
    findings: list[Finding] = []
    sus_cmds: list[str] = []

    for line in text.splitlines():
        matched = False
        for kind, rx in PATTERNS:
            m = rx.search(line)
            if not m:
                continue
            matched = True
            ip = m.groupdict().get("ip")
            if kind == "bruteforce" and ip:
                failed[ip] += 1
            elif kind == "invalid_user" and ip:
                invalid[ip] += 1
            elif kind == "ssh_connection" and ip:
                conns[ip] += 1
            elif kind == "firewall_block" and ip:
                port = m.groupdict().get("port")
                if port:
                    blocked_ports[ip].add(port)
            elif kind == "web_probe" and ip:
                web[ip].append(line.strip()[:200])
            elif kind == "suspicious_command":
                sus_cmds.append(line.strip()[:240])
            break

    for ip, n in failed.items():
        if n >= BRUTE_THRESHOLD:
            findings.append(Finding("bruteforce", ip, f"{n} failed passwords", source, n, pattern="sshd_failed_password", severity="high"))
        elif n > 0:
            findings.append(Finding("failed_auth", ip, f"{n} failed passwords (below threshold)", source, n, pattern="sshd_failed_password", severity="low"))

    for ip, n in invalid.items():
        if n >= 2:
            findings.append(Finding("invalid_user", ip, f"{n} invalid users", source, n, pattern="sshd_invalid_user", severity="medium"))

    for ip, n in conns.items():
        if n >= SCAN_THRESHOLD:
            findings.append(Finding("port_scan_burst", ip, f"{n} rapid SSH connections", source, n, pattern="connection_burst", severity="high"))

    for ip, ports in blocked_ports.items():
        if len(ports) >= BLOCK_PORT_THRESHOLD:
            findings.append(Finding("firewall_block_burst", ip, f"blocked on {len(ports)} ports", source, len(ports), ports=sorted(ports), pattern="ufw_block_multiport", severity="high"))
        else:
            findings.append(Finding("firewall_block", ip, f"blocked ports {sorted(ports)}", source, len(ports), ports=sorted(ports), pattern="ufw_block", severity="low"))

    for ip, lines in web.items():
        findings.append(Finding("web_probe", ip, f"{len(lines)} probe(s): {lines[0][:80]}", source, len(lines), pattern="web_shell_or_admin_probe", severity="high"))

    for cmd in sus_cmds:
        ip_m = IP_RE.search(cmd)
        ip = ip_m.group(0) if ip_m else None
        findings.append(Finding("suspicious_command", ip, cmd, source, 1, pattern="pipe_to_shell_or_root_bash", severity="critical"))

    return findings

def scan_log_file(path: Path) -> list[Finding]:
    try:
        text = path.read_text(errors="ignore")
    except OSError as e:
        return [Finding("error", None, f"cannot read {path}: {e}", str(path), severity="info")]
    return scan_log_text(text, source=str(path))

def listening_ports() -> list[dict]:
    """Read-only snapshot of listening TCP ports via ss."""
    try:
        out = subprocess.check_output(["ss", "-tlnp"], text=True, timeout=10)
    except (subprocess.SubprocessError, FileNotFoundError) as e:
        return [{"error": str(e)}]
    rows = []
    for line in out.splitlines()[1:]:
        parts = line.split()
        if len(parts) < 4:
            continue
        local = parts[3]
        process = parts[-1] if "users:" in line else ""
        rows.append({"local": local, "process": process, "raw": line.strip()})
    return rows

def remote_peers_from_proc() -> list[str]:
    """Read /proc/net/tcp for established remote IPs (defensive attribution)."""
    ips = []
    for proc_path in ("/proc/net/tcp", "/proc/net/tcp6"):
        try:
            lines = Path(proc_path).read_text().splitlines()[1:]
        except OSError:
            continue
        for line in lines:
            cols = line.split()
            if len(cols) < 4:
                continue
            # state 01 = ESTABLISHED
            if cols[3] != "01":
                continue
            remote = cols[2]
            try:
                hip, hport = remote.split(":")
                if len(hip) == 8:  # IPv4 little-endian hex
                    b = bytes.fromhex(hip)
                    ip = ".".join(str(x) for x in b[::-1])
                    if is_public(ip):
                        ips.append(ip)
            except Exception:
                continue
    return sorted(set(ips))

DEFAULT_LOG_CANDIDATES = [
    "/var/log/auth.log",
    "/var/log/secure",
    "/var/log/syslog",
    "/var/log/messages",
    "/var/log/nginx/access.log",
    "/var/log/nginx/error.log",
    "/var/log/apache2/access.log",
    "/var/log/apache2/error.log",
]

def discover_logs() -> list[Path]:
    found = []
    for p in DEFAULT_LOG_CANDIDATES:
        path = Path(p)
        if path.is_file() and os.access(path, os.R_OK):
            found.append(path)
    return found


# --- Anti-surveillance / scanner fingerprint layer (defensive) ---
def scan_signatures(text: str, source: str = "log") -> list[Finding]:
    """Match publicly documented scanner/OSINT/C2 fingerprints in log text."""
    try:
        from signatures.matcher import SignatureMatcher
    except ImportError:
        from signatures import SignatureMatcher  # type: ignore
    matcher = SignatureMatcher()
    findings: list[Finding] = []
    for h in matcher.scan_text(text, source=source):
        if h.severity == "info":
            continue
        findings.append(Finding(
            kind=f"sig:{h.family}",
            ip=h.ip,
            detail=f"{h.detail} :: {h.line[:120]}",
            source=source,
            count=h.count,
            pattern=h.sig_id,
            severity=h.severity,
            feed_hits=[h.tool],
        ))
    return findings


def scan_all(text: str, source: str = "log") -> list[Finding]:
    """Classic patterns + signature fingerprints."""
    return scan_log_text(text, source=source) + scan_signatures(text, source=source)


def scan_log_file_all(path: Path) -> list[Finding]:
    try:
        text = path.read_text(errors="ignore")
    except OSError as e:
        return [Finding("error", None, f"cannot read {path}: {e}", str(path), severity="info")]
    return scan_all(text, source=str(path))
