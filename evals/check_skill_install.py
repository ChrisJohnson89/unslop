#!/usr/bin/env python3
"""Exercise the distributed skill outside the repo and reject unsafe/stale layouts."""
from __future__ import annotations

import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import unittest
import zipfile

from _check_support import ROOT
sys.path.insert(0, str(ROOT / "tools"))
from package_skill import build, runtime_files  # noqa: E402


class SkillDistribution(unittest.TestCase):
    def test_native_metadata_and_routes(self):
        text = (ROOT / "SKILL.md").read_text()
        self.assertRegex(text, r"\A---\nname: unslop\n")
        self.assertNotIn("user-invocable:", text)
        self.assertNotIn("argument-hint:", text)
        routes = set(re.findall(r"references/commands/(\w+)\.md", text))
        self.assertEqual(routes, {"rewrite", "cleanup", "teach", "mimic"})
        self.assertEqual(routes, {p.stem for p in (ROOT / "references/commands").glob("*.md")})
        self.assertIn('$unslop', (ROOT / 'agents/openai.yaml').read_text())

    def test_all_local_reference_links_resolve(self):
        for path in runtime_files():
            if path.suffix != ".md":
                continue
            for link in re.findall(r"\]\(([^)]+)\)", path.read_text()):
                if "://" in link or link.startswith("#"):
                    continue
                target = (path.parent / link.split("#")[0]).resolve()
                self.assertIn(ROOT.resolve(), target.parents, (path, link))
                self.assertTrue(target.is_file(), (path, link))

    def test_archive_is_reproducible_and_runtime_only(self):
        with tempfile.TemporaryDirectory() as directory:
            one = build(Path(directory) / "one.skill")
            two = build(Path(directory) / "two.skill")
            self.assertEqual(one.read_bytes(), two.read_bytes())
            with zipfile.ZipFile(one) as archive:
                expected = {"unslop/" + p.relative_to(ROOT).as_posix() for p in runtime_files()}
                self.assertEqual(set(archive.namelist()), expected)
                self.assertIn("unslop/assets/silhouette-reference.json", expected)
                self.assertFalse(any("/evals/" in n or "/.unslop/" in n or "/.git/" in n for n in expected))

    def test_installed_checks_work_away_from_repo(self):
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            with zipfile.ZipFile(build(base / "unslop.skill")) as archive:
                archive.extractall(base / "installed")
            skill = base / "installed/unslop"
            source = base / "source.txt"
            output = base / "output.txt"
            text = "The lease holder renews the lease every 30 seconds."
            source.write_text(text)
            output.write_text(text)
            for script, args in (
                ("banned_phrase_scan.py", [str(source)]),
                ("structure_scan.py", [str(source)]),
                ("silhouette_scan.py", [str(source)]),
                ("readability_metrics.py", [str(source)]),
                ("extract_constraints.py", [str(source)]),
                ("validate_preservation.py", [str(source), str(output)]),
                ("diff_check.py", [str(source), str(output)]),
            ):
                proc = subprocess.run([sys.executable, str(skill / "scripts" / script), *args],
                                      cwd=base, text=True, capture_output=True, timeout=15)
                self.assertEqual(proc.returncode, 0, (script, proc.stdout, proc.stderr))
                self.assertIsInstance(json.loads(proc.stdout), dict)
            dirty = subprocess.run([sys.executable, str(skill / "scripts/banned_phrase_scan.py")],
                                   input="Here's the thing: this is a game-changer.",
                                   cwd=base, text=True, capture_output=True, timeout=15)
            self.assertEqual(dirty.returncode, 1)
            self.assertGreater(json.loads(dirty.stdout)["total_violations"], 0)
            output.write_text("The lease holder renews the lease every 300 seconds.")
            loss = subprocess.run([sys.executable, str(skill / "scripts/validate_preservation.py"),
                                   str(source), str(output)], cwd=base, capture_output=True, text=True)
            self.assertEqual(loss.returncode, 1)
            self.assertEqual(source.read_text(), text)

    def test_symlink_resources_are_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'SKILL.md').write_text('skill')
            (root / 'references').mkdir()
            (root / 'references/secret.md').symlink_to(ROOT / 'README.md')
            with self.assertRaises(ValueError):
                build(root / 'out.skill', root)

    def test_output_cannot_replace_source(self):
        with self.assertRaises(ValueError):
            build(ROOT / 'SKILL.md')

    def test_measurement_identity_and_equivalent_units(self):
        sys.path.insert(0, str(ROOT / 'scripts'))
        from extract_constraints import extract_constraints
        from validate_preservation import validate_preservation
        for quantity in ('30 seconds', '5 years', '3GB', '12 em', '30 degrees Celsius', '30 degrees C'):
            with self.subTest(quantity=quantity):
                source = f'The measurement is {quantity}.'
                self.assertTrue(any(c['type'] == 'measurement' for c in extract_constraints(source)))
                self.assertTrue(validate_preservation(source, source)['passed'])
        self.assertTrue(validate_preservation('The delay is 30 seconds.', 'The delay is 30 s.')['passed'])
        self.assertTrue(validate_preservation('It reached 30 degrees Celsius.', 'It reached 30 °C.')['passed'])

    def test_behavioral_cases_remain_reviewable(self):
        cases = json.loads((ROOT / 'evals/adversarial-evals.json').read_text())["evals"]
        ids = [case['id'] for case in cases]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertGreaterEqual(len(ids), 18)
        for case in cases:
            self.assertEqual(case['target'], 'skill')
            self.assertTrue(case['prompt'])
            self.assertTrue(case['correct_behavior'])
            self.assertTrue(case['assertions'])
            self.assertTrue(all(a['type'] == 'judge' and a['check'] for a in case['assertions']))


def main() -> int:
    result = unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(SkillDistribution))
    return 0 if result.wasSuccessful() else 1


if __name__ == '__main__':
    raise SystemExit(main())
