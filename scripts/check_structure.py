#!/usr/bin/env python3
"""Check the canonical layout and retained source records, not theorem truth."""
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]


def digest(data):
    return hashlib.sha256(data).hexdigest()


def main():
    for name in ('science/README.md', 'science/theorem.md', 'learning/MILESTONES.md',
                 'learning/SCHUMACHER_WESTMORELAND_BRIDGE.md', 'references/bibliography.json',
                 'verification/README.md'):
        assert (ROOT/name).is_file(), name
    assert not (ROOT/'docs').exists(), 'Superseded documentation tree remains'
    assert not (ROOT/'manuscript').exists()
    record = json.loads((ROOT/'verification/source_map.json').read_text())
    for name, expected in record['protected_files'].items():
        assert digest((ROOT/name).read_bytes()) == expected, f'Protected source changed: {name}'
    for item in record['preserved_equations']:
        content = '\n'.join((ROOT/name).read_text() for name in item['destinations'])
        expressions = re.findall(r'```math\n(.*?)```', content, re.S)
        inline = re.findall(r'\$`(.*?)`\$', content, re.S)
        actual = digest(json.dumps([expressions, inline], ensure_ascii=False).encode())
        assert actual == item['math_sha256'], f'Mathematical source changed: {item["destinations"]}'
    targets = re.findall(r'^\*\*Understanding target:\*\* (.+)$',
                         (ROOT/'learning/MILESTONES.md').read_text(), re.M)
    assert len(targets) == 30
    assert digest(json.dumps(targets, ensure_ascii=False).encode()) == record['milestone_targets_sha256']
    entries = json.loads((ROOT/'references/bibliography.json').read_text())['entries']
    assert len(entries) >= 35 and len({e['id'] for e in entries}) == len(entries)
    print(f'PASS: canonical layout, {len(record["protected_files"])} protected files, '
          f'{len(record["preserved_equations"])} mathematical source records, {len(entries)} bibliography labels.')


if __name__ == '__main__':
    main()
