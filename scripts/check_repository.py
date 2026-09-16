#!/usr/bin/env python3
"""Check local links, math-source hygiene, metadata, and reference calculations."""
from pathlib import Path
import json
import re
import sys
import tomllib
from urllib.parse import unquote

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


def main():
    checked_links = 0
    for file in sorted(ROOT.rglob('*.md')):
        if any(part.startswith('.') for part in file.relative_to(ROOT).parts[:-1]):
            continue
        text = file.read_text()
        if len(re.findall(r'^```', text, re.M)) % 2:
            raise AssertionError(f'Unbalanced code fences: {file}')
        if any(token in text for token in [r'\[', r'\]', r'\operatorname', 'sandbox:/', 'turn0search']):
            raise AssertionError(f'Unsupported or environment-specific markup: {file}')
        for block in re.findall(r'```math\n(.*?)```', text, re.S):
            clean = re.sub(r'\\[{}]', '', block)
            if clean.count('{') != clean.count('}'):
                raise AssertionError(f'Unbalanced TeX braces: {file}')
        urls = re.findall(r'\[[^\]\n]+\]\(([^\s)]+)', text)
        urls += re.findall(r'^\[[^\]]+\]:\s*(\S+)', text, re.M)
        for url in urls:
            if re.match(r'^[a-z]+:', url) or url.startswith('#'):
                continue
            destination = unquote(url.split('#', 1)[0])
            resolved = (file.parent/destination).resolve()
            if not resolved.is_relative_to(ROOT) or not resolved.exists():
                raise AssertionError(f'Broken local link in {file.relative_to(ROOT)}: {url}')
            checked_links += 1
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
    print(f'PASS: {checked_links} local link destinations, math-source checks, metadata, and reference values.')


if __name__ == '__main__':
    main()
