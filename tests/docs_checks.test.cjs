'use strict';
const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const {inspectMarkdown, checkLinks} = require('../scripts/check_docs.cjs');
const fixtures = path.join(__dirname, 'fixtures', 'docs');
function inspect(name) {
  return inspectMarkdown(fs.readFileSync(path.join(fixtures, name), 'utf8'), name);
}
for (const [name, kind] of [
  ['bad_math.md', 'math'], ['bad_fence.md', 'fence'],
  ['bad_width.md', 'width'], ['bad_image.md', 'image-alt'],
  ['bad_reference.md', 'reference'], ['bad_environment.md', 'environment'],
  ['duplicate_anchor.md', 'anchor'],
]) {
  test(`deliberately broken ${name} is rejected as ${kind}`, () => {
    assert.ok(inspect(name).issues.some(issue => issue.kind === kind));
  });
}
test('missing Markdown fragment and nonexistent image are rejected', () => {
  const docs = [inspect('bad_anchor.md'), inspect('bad_image.md')];
  checkLinks(docs, fixtures);
  assert.ok(docs[0].issues.some(issue => /Missing Markdown anchor/.test(issue.message)));
  assert.ok(docs[1].issues.some(issue => /Missing or outside/.test(issue.message)));
});
test('source-code line range beyond the target file is rejected', () => {
  const doc = inspect('bad_code_line.md');
  checkLinks([doc], fixtures);
  assert.ok(doc.issues.some(issue => /Code line fragment/.test(issue.message)));
});
test('valid Markdown, duplicate heading suffix, explicit anchor, math forms, and code link pass', () => {
  const doc = inspect('valid.md');
  checkLinks([doc], fixtures);
  assert.deepEqual(doc.issues, []);
  assert.equal(doc.formulas.length, 4);
  assert.ok(doc.anchors.has('repeated-1'));
  assert.ok(doc.anchors.has('stable-place'));
});
test('unmatched inline delimiter and incomplete Markdown link cannot evade parsing', () => {
  assert.ok(inspectMarkdown('Bad $x').issues.some(issue => issue.kind === 'math'));
  assert.ok(inspectMarkdown('[bad](missing.md').issues.some(issue => issue.kind === 'markdown'));
});
test('math compilation distinguishes a compact multiline equation from a wide line', () => {
  const doc = inspectMarkdown('```math\n\\begin{aligned}\na&=b+c,\\\\\nd&=e+f.\n\\end{aligned}\n```\n');
  assert.deepEqual(doc.issues, []);
  assert.ok(doc.formulas[0].width_px < 310);
});
