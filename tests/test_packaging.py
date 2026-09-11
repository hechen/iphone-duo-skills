import importlib.util
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


def module(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / "scripts" / (name + ".py"))
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


installer = module("install")
validator = module("validate")


class PackagingTests(unittest.TestCase):
    def test_repository(self):
        self.assertEqual(validator.validate(ROOT), [])

    def test_all_skills_validate_without_openai_metadata(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            installer.install(ROOT / "skills", root / "skills", [])
            for metadata in (root / "skills").glob("*/agents/openai.yaml"):
                metadata.unlink()
            self.assertEqual(validator.validate(root), [])

    def test_present_vendor_metadata_is_still_validated(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            installer.install(ROOT / "skills", root / "skills", ["iphone-duo-layout"])
            metadata = root / "skills/iphone-duo-layout/agents/openai.yaml"
            metadata.write_text("interface: []\n")
            self.assertTrue(any("interface mapping" in e for e in validator.validate(root)))

    def test_install_preserves_contents_and_references(self):
        with tempfile.TemporaryDirectory() as directory:
            dest = Path(directory) / "skills"
            paths = installer.install(ROOT / "skills", dest, [])
            self.assertEqual(len(paths), 7)
            for target in paths:
                source = ROOT / "skills" / target.name
                for file in source.rglob("*"):
                    if file.is_file():
                        self.assertEqual(file.read_bytes(), (target / file.relative_to(source)).read_bytes())

    def test_conflict_prevents_all_writes(self):
        with tempfile.TemporaryDirectory() as directory:
            dest = Path(directory)
            existing = dest / "iphone-duo-layout"
            existing.mkdir()
            marker = existing / "SKILL.md"
            marker.write_text("local customization")
            with self.assertRaises(ValueError):
                installer.install(ROOT / "skills", dest, ["iphone-duo-camera", "iphone-duo-layout"])
            self.assertEqual(marker.read_text(), "local customization")
            self.assertFalse((dest / "iphone-duo-camera").exists())

    def test_unknown_or_duplicate_selection_writes_nothing(self):
        with tempfile.TemporaryDirectory() as directory:
            dest = Path(directory) / "new"
            for names in [["../escape"], ["iphone-duo-layout", "iphone-duo-layout"]]:
                with self.assertRaises(ValueError):
                    installer.install(ROOT / "skills", dest, names)
                self.assertFalse(dest.exists())

    def test_broken_symlink_is_not_overwritten(self):
        with tempfile.TemporaryDirectory() as directory:
            dest = Path(directory)
            link = dest / "iphone-duo-layout"
            link.symlink_to(dest / "absent")
            with self.assertRaises(ValueError):
                installer.install(ROOT / "skills", dest, ["iphone-duo-layout"])
            self.assertTrue(link.is_symlink())

    def test_validator_detects_broken_and_cross_skill_links(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            installer.install(ROOT / "skills", root / "skills", [])
            entry = root / "skills/iphone-duo-layout/SKILL.md"
            with entry.open("a") as stream:
                stream.write("\n[Missing](references/missing.md)\n[Other](../iphone-duo-camera/SKILL.md)\n")
            errors = validator.validate(root)
            self.assertTrue(any("broken link" in e for e in errors))
            self.assertTrue(any("escapes package" in e for e in errors))


if __name__ == "__main__":
    unittest.main()
