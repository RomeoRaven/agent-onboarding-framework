"""Behavior tests for the optional static onboarding preflight."""
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "check-onboarding.py"


class StaticPreflightTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(dir=Path(__file__).parent)
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)

    def run_check(self, *args):
        return subprocess.run([sys.executable, str(SCRIPT), *map(str, args)],
                              capture_output=True, text=True, check=False)

    def test_missing_package_reference_fails_with_location(self):
        (self.root / "README.md").write_text("Read `workflows/missing.md`.\n")
        result = self.run_check("--package", self.root)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("README.md:1", result.stdout)
        self.assertIn("workflows/missing.md", result.stdout)

    def test_existing_package_reference_passes(self):
        (self.root / "README.md").write_text("Read `workflows/valid.md`.\n")
        (self.root / "workflows").mkdir()
        (self.root / "workflows" / "valid.md").write_text("# Valid\n")
        result = self.run_check("--package", self.root)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_placeholder_in_completed_manifest_fails(self):
        manifest = self.root / "ONBOARDING-MANIFEST.md"
        manifest.write_text("Framework: `<exact revision>`\n")
        result = self.run_check("--manifest", manifest)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("ONBOARDING-MANIFEST.md:1", result.stdout)

    def test_completed_manifest_without_placeholder_passes(self):
        manifest = self.root / "ONBOARDING-MANIFEST.md"
        manifest.write_text("Framework: reviewed revision abc123\n")
        result = self.run_check("--manifest", manifest)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_template_placeholders_are_not_package_failures(self):
        (self.root / "README.md").write_text("Read `templates/MANIFEST.md`.\n")
        (self.root / "templates").mkdir()
        (self.root / "templates" / "MANIFEST.md").write_text("Owner: `<owner>`\n")
        result = self.run_check("--package", self.root)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_missing_root_document_reference_fails(self):
        (self.root / "README.md").write_text("Use `ACCEPTANCE.md` to verify.\n")
        result = self.run_check("--package", self.root)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("README.md:1", result.stdout)
        self.assertIn("ACCEPTANCE.md", result.stdout)

    def test_missing_markdown_link_fails(self):
        (self.root / "README.md").write_text("[Guide](guides/MISSING.md)\n")
        result = self.run_check("--package", self.root)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("guides/MISSING.md", result.stdout)

    def test_fenced_example_is_not_checked(self):
        (self.root / "README.md").write_text("```text\n`workflows/example.md`\n```\n")
        result = self.run_check("--package", self.root)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
