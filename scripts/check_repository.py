#!/usr/bin/env python3
"""Check retained calculations, displayed values, metadata, and parsed/rendered docs.

Install runtime requirements and run ``npm ci`` before this command. The Node
checker uses actual MathJax compilation; its width estimate is local SVG font
geometry, not a claim about live GitHub or browser layout.
"""
from pathlib import Path
import json
import re
import shutil
import subprocess
import sys
import tomllib

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT/'scripts'))
from reproduce import calculate


def compare(expected, actual, path='calculations'):
    if isinstance(expected, dict):
        if expected.keys() != actual.keys():
            raise AssertionError(f'Different keys at {path}')
        for key in expected:
            compare(expected[key], actual[key], f'{path}.{key}')
    elif isinstance(expected, list):
        if len(expected) != len(actual):
            raise AssertionError(f'Different lengths at {path}')
        for index, value in enumerate(expected):
            compare(value, actual[index], f'{path}[{index}]')
    elif isinstance(expected, (int, float)):
        if abs(expected-actual) > 1e-10*max(1, abs(expected)):
            raise AssertionError(f'Numerical mismatch at {path}: {expected} vs {actual}')
    elif expected != actual:
        raise AssertionError(f'Value mismatch at {path}')


def check_displayed_values(calculations, pages):
    """Compare the canonical benchmark's printed precision with retained data.

    Across active pages also reject unexplained six-or-more decimal numbers in
    (0,1): these are benchmark/crossover outputs, not independent datasets.
    Coarse rounded summaries and scientific prose still require human review.
    """
    required = {
        'strict lower bound': (calculations['strict_lower_bound'], 9),
        'relaxed heat': (calculations['relaxed_device']['heat'], 9),
        'charged return lower bound': (calculations['strict_with_return_allowance'], 9),
        'thermal gap': (calculations['relaxed_device']['gap_over_kBT'], 9),
        'auxiliary allowance': (calculations['auxiliary_entropy_allowance_bits'], 12),
    }
    benchmark = pages['docs/FINITE_BENCHMARK.md']
    for label, (value, digits) in required.items():
        token = f'{value:.{digits}f}'
        if not re.search(r'(?<![\d.])' + re.escape(token) + r'(?!\d)', benchmark):
            raise AssertionError(f'Canonical benchmark missing retained {label}: {token}')

    values = []
    def collect(value):
        if isinstance(value, dict):
            for item in value.values():
                collect(item)
        elif isinstance(value, list):
            for item in value:
                collect(item)
        elif isinstance(value, (float, int)):
            values.append(value)
    collect(calculations)
    values.append(1-calculations['relaxed_device']['minimum_initial_bath_population'])
    checked = 0
    for name, text in pages.items():
        # Omit URLs, including arXiv and DOI identifiers.
        text = re.sub(r'https?://\S+', '', text)
        for match in re.finditer(r'(?<![\w.])0\.(\d{6,})(?!\w|\.\d)', text):
            token = match.group(0)
            digits = len(match.group(1))
            if not any(token == f'{value:.{digits}f}' for value in values):
                raise AssertionError(f'Unmatched high-precision result in {name}: {token}')
            checked += 1
    return checked


def main():
    metadata = tomllib.loads((ROOT/'pyproject.toml').read_text())
    assert metadata['project']['name'] == 'quantum-precision-heat-tradeoff'
    citation = (ROOT/'CITATION.cff').read_text()
    assert 'cff-version: 1.2.0' in citation and 'given-names: Ruge' in citation
    readme = (ROOT/'README.md').read_text()
    assert 'Manuscript preparation is currently on hold.' in readme
    assert 'mailto:gogoko699@gmail.com' in readme
    assert 'Copyright (c) 2026 Ruge Lin' in (ROOT/'LICENSE').read_text()
    reference = json.loads((ROOT/'results'/'reference.json').read_text())
    compare(reference['calculations'], calculate())
    excluded = {'tests', 'node_modules', 'build', 'dist', '.venv'}
    pages = {file.relative_to(ROOT).as_posix(): file.read_text()
             for file in ROOT.rglob('*.md')
             if not any(part.startswith('.') or part in excluded
                        for part in file.relative_to(ROOT).parts[:-1])}
    checked_values = check_displayed_values(reference['calculations'], pages)
    print(f'PASS: metadata, retained calculations, and {checked_values} displayed high-precision values.', flush=True)
    node = shutil.which('node')
    if node is None or not (ROOT/'node_modules'/'mathjax-full').is_dir():
        raise SystemExit('Documentation checks require Node.js >=22.12 and `npm ci`.')
    subprocess.run([node, '--test', 'tests/docs_checks.test.cjs'], cwd=ROOT, check=True)
    subprocess.run([node, 'scripts/check_docs.cjs'], cwd=ROOT, check=True)


if __name__ == '__main__':
    main()
