#!/usr/bin/env python3
"""Keep mathematical/code spans outside the one-use link migration."""
from pathlib import Path

p = Path(__file__).with_name('refurnish.py')
s = p.read_text()
s = s.replace(", '''", ", r'''").replace("+ '''", "+ r'''")
s = s.replace('def relink(content: str, old: str, new: str) -> str:',
              'def _relink_unprotected(content: str, old: str, new: str) -> str:', 1)
wrapper = r'''def relink(content: str, old: str, new: str) -> str:
    protected = []
    def freeze(match):
        protected.append(match[0])
        return f'QPHPROTECTED{len(protected)-1}END'
    content = re.sub(r'(?ms)^```[^\n]*\n.*?^```[ \t]*$', freeze, content)
    content = re.sub(r'\$`.*?`\$', freeze, content, flags=re.S)
    content = re.sub(r'`[^`\n]+`', freeze, content)
    content = _relink_unprotected(content, old, new)
    for index, value in enumerate(protected):
        content = content.replace(f'QPHPROTECTED{index}END', value)
    return content


'''
s = s.replace('def write(name: str, content: str | bytes) -> None:',
              wrapper + 'def write(name: str, content: str | bytes) -> None:', 1)
s = s.replace("    if name == 'scripts/make_figures.py':",
              "    if name == 'tests/test_documented_values.py':\n"
              "        content = content.replace(\"ROOT/'docs'/'FINITE_BENCHMARK.md'\", \"ROOT/'science'/'finite_benchmark.md'\")\n"
              "    if name == 'scripts/make_figures.py':", 1)
extra = r'''
# Preserve the actual settled scientific understanding targets, not only IDs.
def understanding_targets(value):
    return re.findall(r'^\*\*Understanding target:\*\* (.+)$', value, re.M)
old_targets = understanding_targets(text['docs/tutorial/MILESTONES.md'])
new_targets = understanding_targets((ROOT/'learning/MILESTONES.md').read_text())
assert len(old_targets) == 30 and new_targets == old_targets
print('PASS: all 30 original scientific understanding targets retained verbatim.')
'''
s += '\n' + extra
p.write_text(s)
compile(s, str(p), 'exec')
print('Prepared protected link migration and component-path repair.')
