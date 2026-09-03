#!/usr/bin/env python3
"""Regression self-tests for tools/validate_protocol.py.

These tests exercise the validator as a black box against temporary copies of
this repository. They intentionally cover a small number of high-value
invariants rather than duplicating the validator implementation.
"""

from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ValidatorRegressionTests(unittest.TestCase):
    def make_copy(self) -> Path:
        temp_dir = tempfile.TemporaryDirectory()
        self.addCleanup(temp_dir.cleanup)
        target = Path(temp_dir.name) / "repo"
        shutil.copytree(
            ROOT,
            target,
            ignore=shutil.ignore_patterns(".git", "__pycache__", ".pytest_cache"),
        )
        return target

    def run_validator(self, root: Path) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, "tools/validate_protocol.py"],
            cwd=root,
            text=True,
            capture_output=True,
            check=False,
        )

    def assert_fails_with(self, result: subprocess.CompletedProcess[str], text: str) -> None:
        output = result.stdout + result.stderr
        self.assertNotEqual(result.returncode, 0, output)
        self.assertIn(text, output)
        self.assertIn("RESULT: FAIL", output)

    def test_current_repository_passes(self) -> None:
        root = self.make_copy()
        result = self.run_validator(root)
        output = result.stdout + result.stderr
        self.assertEqual(result.returncode, 0, output)
        self.assertIn("RESULT: PASS", output)

    def test_documented_bootloader_drift_fails(self) -> None:
        root = self.make_copy()
        setup_path = root / "SETUP.md"
        text = setup_path.read_text(encoding="utf-8")
        needle = "<!-- BOOTLOADER-DOC-START -->\n> Operational Memory:"
        replacement = "<!-- BOOTLOADER-DOC-START -->\n> Altered Operational Memory:"
        self.assertIn(needle, text)
        setup_path.write_text(text.replace(needle, replacement, 1), encoding="utf-8")

        result = self.run_validator(root)
        self.assert_fails_with(result, "documented bootloader does not match")

    def test_missing_main_push_trigger_fails(self) -> None:
        root = self.make_copy()
        workflow_path = root / ".github" / "workflows" / "protocol-validation.yml"
        text = workflow_path.read_text(encoding="utf-8")
        needle = "      - main\n"
        self.assertIn(needle, text)
        workflow_path.write_text(text.replace(needle, "", 1), encoding="utf-8")

        result = self.run_validator(root)
        self.assert_fails_with(result, "push trigger must include canonical main")

    def test_supported_plan_manifest_drift_fails(self) -> None:
        root = self.make_copy()
        manifest_path = root / "PROTOCOL.yaml"
        text = manifest_path.read_text(encoding="utf-8")
        needle = "minimum_supported_chatgpt_plan: plus"
        self.assertIn(needle, text)
        manifest_path.write_text(
            text.replace(needle, "minimum_supported_chatgpt_plan: free", 1),
            encoding="utf-8",
        )

        result = self.run_validator(root)
        self.assert_fails_with(
            result,
            "compatibility.minimum_supported_chatgpt_plan must be 'plus'",
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
