#!/usr/bin/env python3
"""Offline tests for the SHEPHERD terms gate. No network."""

import ast
import copy
import json
import socket
import unittest
from pathlib import Path

import check_terms

ROOT = Path(__file__).resolve().parent
ALLOWLIST = ROOT / "sources.json"
NETWORK_CALLS = []


def _block_network(*_args, **_kwargs):
    NETWORK_CALLS.append("connect")
    raise AssertionError("check_terms must not open a socket")


class CheckTermsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.document = json.loads(ALLOWLIST.read_text(encoding="utf-8"))

    def test_shipped_allowlist_passes(self):
        results = check_terms.check_document(self.document)
        self.assertTrue(all(item["ok"] for item in results), results)
        self.assertEqual(
            [item["id"] for item in results],
            [source["id"] for source in self.document["sources"]],
        )

    def test_one_source_per_allowed_kind(self):
        kinds = [source["kind"] for source in self.document["sources"]]
        self.assertEqual(sorted(kinds), sorted(check_terms.ALLOWED_KINDS))

    def test_missing_license_terms_or_rate_limit_is_rejected(self):
        for field, reason in (
            ("license", "missing license"),
            ("terms_url", "missing terms URL"),
            ("rate_limit", "missing rate limit"),
        ):
            source = copy.deepcopy(self.document["sources"][0])
            source.pop(field)
            reasons = check_terms.check_source(source)
            self.assertIn(reason, reasons)

    def test_blank_and_placeholder_license_is_rejected(self):
        source = copy.deepcopy(self.document["sources"][0])
        source["license"] = "TBD"
        self.assertIn("missing license", check_terms.check_source(source))
        source["license"] = "  "
        self.assertIn("missing license", check_terms.check_source(source))

    def test_auth_required_is_rejected(self):
        source = copy.deepcopy(self.document["sources"][0])
        source["auth_required"] = True
        self.assertIn("requires auth", check_terms.check_source(source))

    def test_token_api_and_account_sources_are_rejected(self):
        source = copy.deepcopy(self.document["sources"][0])
        for flag in ("api_key_required", "token_required", "account_required", "oauth_required"):
            flagged = copy.deepcopy(source)
            flagged[flag] = True
            self.assertIn("requires auth", check_terms.check_source(flagged), flag)
        source["api_key"] = "example"
        self.assertIn("requires auth", check_terms.check_source(source))
        source.pop("api_key")
        source["access"] = "authenticated"
        self.assertIn("requires auth", check_terms.check_source(source))

    def test_omitted_auth_flag_is_rejected(self):
        source = copy.deepcopy(self.document["sources"][0])
        source.pop("auth_required")
        self.assertIn("requires auth", check_terms.check_source(source))

    def test_rate_limit_evasion_is_rejected(self):
        source = copy.deepcopy(self.document["sources"][0])
        source["rate_limit"]["extra_machines"] = True
        self.assertIn("rate-limit evasion is refused", check_terms.check_source(source))
        source = copy.deepcopy(self.document["sources"][0])
        source["scrape"] = True
        self.assertIn("rate-limit evasion is refused", check_terms.check_source(source))

    def test_invented_numeric_cap_is_rejected(self):
        source = copy.deepcopy(next(item for item in self.document["sources"] if item["id"] == "osm-planet-diffs"))
        source["rate_limit"]["max_requests"] = 100
        source["rate_limit"]["per_seconds"] = 1
        reasons = check_terms.check_source(source)
        self.assertIn("numeric rate was set where the publisher published none", reasons)

    def test_credentials_in_endpoint_are_rejected(self):
        source = copy.deepcopy(self.document["sources"][0])
        source["endpoint"] = "https://user:pass@export.arxiv.org/oai2"
        self.assertIn("endpoint contains credentials", check_terms.check_source(source))

    def test_unknown_kind_is_rejected(self):
        source = copy.deepcopy(self.document["sources"][0])
        source["kind"] = "html-scrape"
        self.assertIn("kind is not on the keyless allowlist", check_terms.check_source(source))

    def test_module_does_not_import_a_client(self):
        tree = ast.parse(Path(check_terms.__file__).read_text(encoding="utf-8"))
        imported = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                imported.update(alias.name.split(".")[0] for alias in node.names)
            elif isinstance(node, ast.ImportFrom) and node.module:
                imported.add(node.module.split(".")[0])
        self.assertTrue(imported.isdisjoint({"urllib", "requests", "http", "socket", "ftplib"}))

    def test_check_does_not_touch_the_network(self):
        NETWORK_CALLS.clear()
        original = socket.socket.connect
        socket.socket.connect = _block_network
        try:
            check_terms.check_document(self.document)
            rejected = copy.deepcopy(self.document["sources"][0])
            rejected["auth_required"] = True
            check_terms.check_source(rejected)
        finally:
            socket.socket.connect = original
        self.assertEqual(NETWORK_CALLS, [])


if __name__ == "__main__":
    unittest.main()
