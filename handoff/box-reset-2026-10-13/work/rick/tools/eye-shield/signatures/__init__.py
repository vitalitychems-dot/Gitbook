"""Defensive signature pack: recognize scanners / OSINT / surveillance-tool probes in OUR logs."""
from .matcher import SignatureMatcher, SignatureHit, load_catalog

__all__ = ["SignatureMatcher", "SignatureHit", "load_catalog"]
