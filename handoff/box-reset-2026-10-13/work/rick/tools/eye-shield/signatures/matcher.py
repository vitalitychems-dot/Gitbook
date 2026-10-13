"""Apply public defensive signatures to log lines. Read-only, no network, no exploits."""
from __future__ import annotations
import json, re
from dataclasses import dataclass, asdict, field
from pathlib import Path
from typing import Iterable

HERE = Path(__file__).resolve().parent
CATALOG = HERE / "catalog.json"
IP_RE = re.compile(
    r"\b(?:(?:25[0-5]|2[0-4]\d|[01]?\d?\d)\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d?\d)\b"
)

@dataclass
class SignatureHit:
    sig_id: str
    family: str
    tool: str
    severity: str
    ip: str | None
    detail: str
    source: str
    cite: str
    line: str = ""
    count: int = 1

    def to_dict(self) -> dict:
        return asdict(self)


def load_catalog(path: Path | None = None) -> dict:
    p = Path(path or CATALOG)
    return json.loads(p.read_text())


class SignatureMatcher:
    def __init__(self, catalog: dict | None = None):
        data = catalog or load_catalog()
        self.citations = list(data.get("citations") or [])
        self.raw = list(data.get("signatures") or [])
        self._compiled: list[tuple[dict, re.Pattern]] = []
        for sig in self.raw:
            try:
                rx = re.compile(sig["regex"])
            except re.error as e:
                raise ValueError(f"bad regex in {sig.get('id')}: {e}") from e
            self._compiled.append((sig, rx))

    def __len__(self) -> int:
        return len(self._compiled)

    def match_line(self, line: str, source: str = "log") -> list[SignatureHit]:
        hits: list[SignatureHit] = []
        where_hint = self._guess_where(line)
        for sig, rx in self._compiled:
            want = sig.get("where") or "any"
            if want != "any" and where_hint not in (want, "any"):
                # allow 'any' lines; for http/syslog restrict when we know
                if where_hint != "unknown" and want != where_hint:
                    continue
            m = rx.search(line)
            if not m:
                continue
            # python-requests alone is noisy — require a probe-ish path
            if sig["id"] == "scan.python_requests_probe":
                if not re.search(
                    r"(?i)/(?:\.env|\.git|wp-login|phpmyadmin|onvif|admin|actuator|cgi-bin)",
                    line,
                ):
                    continue
            ip_m = IP_RE.search(line)
            hits.append(
                SignatureHit(
                    sig_id=sig["id"],
                    family=sig["family"],
                    tool=sig["tool"],
                    severity=sig.get("severity", "medium"),
                    ip=ip_m.group(0) if ip_m else None,
                    detail=f"{sig['id']} matched ({sig['tool']})",
                    source=source,
                    cite=sig.get("cite", ""),
                    line=line.strip()[:240],
                )
            )
        return hits

    def scan_text(self, text: str, source: str = "log") -> list[SignatureHit]:
        """Aggregate hits by (sig_id, ip)."""
        bucket: dict[tuple[str, str | None], SignatureHit] = {}
        for line in text.splitlines():
            if not line.strip():
                continue
            for h in self.match_line(line, source=source):
                key = (h.sig_id, h.ip)
                if key in bucket:
                    bucket[key].count += 1
                    if len(bucket[key].line) < 200:
                        bucket[key].line = h.line
                else:
                    bucket[key] = h
        return list(bucket.values())

    def scan_file(self, path: Path) -> list[SignatureHit]:
        try:
            text = Path(path).read_text(errors="ignore")
        except OSError as e:
            return [
                SignatureHit(
                    sig_id="error.read",
                    family="error",
                    tool="eye-shield",
                    severity="info",
                    ip=None,
                    detail=str(e),
                    source=str(path),
                    cite="",
                )
            ]
        return self.scan_text(text, source=str(path))

    @staticmethod
    def _guess_where(line: str) -> str:
        if re.search(r'"(?:GET|POST|HEAD|PUT|DELETE) ', line) or "HTTP/" in line:
            return "http"
        if re.search(r"(?i)(?:UFW BLOCK|IPTABLES|kernel:|sshd\[|sudo:)", line):
            return "syslog"
        return "unknown"

    def stats(self) -> dict:
        families: dict[str, int] = {}
        for sig, _ in self._compiled:
            families[sig["family"]] = families.get(sig["family"], 0) + 1
        return {
            "signature_count": len(self._compiled),
            "families": families,
            "citations": len(self.citations),
        }
