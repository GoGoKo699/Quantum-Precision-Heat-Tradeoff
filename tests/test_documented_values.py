"""A deliberate documentation-number corruption must not pass scientific QA."""
from pathlib import Path
import importlib.util
import json
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('check_repository', ROOT/'scripts'/'check_repository.py')
CHECKER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CHECKER)


class DocumentedValueChecks(unittest.TestCase):
    def test_corrupted_canonical_benchmark_is_rejected(self):
        values = json.loads((ROOT/'results'/'reference.json').read_text())['calculations']
        text = (ROOT/'docs'/'FINITE_BENCHMARK.md').read_text()
        text = text.replace('0.498044180', '0.498044181')
        with self.assertRaisesRegex(AssertionError, 'strict lower bound'):
            CHECKER.check_displayed_values(values, {'docs/FINITE_BENCHMARK.md': text})

    def test_corrupted_secondary_precise_summary_is_rejected(self):
        values = json.loads((ROOT/'results'/'reference.json').read_text())['calculations']
        pages = {'docs/FINITE_BENCHMARK.md': (ROOT/'docs'/'FINITE_BENCHMARK.md').read_text(),
                 'example.md': 'The strict lower bound is 0.498044181.'}
        with self.assertRaisesRegex(AssertionError, 'example.md'):
            CHECKER.check_displayed_values(values, pages)
