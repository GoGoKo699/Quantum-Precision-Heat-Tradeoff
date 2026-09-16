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
  ['bad_literal_braces.md', 'math-delimiter'], ['bad_emphasis.md', 'math-context'],
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
test('protected inline syntax preserves literal-brace source without changing the formula', () => {
  const ordinary = inspectMarkdown('The label is $x\\in\\{0,1\\}$.');
  const protectedMath = inspectMarkdown('The label is $`x\\in\\{0,1\\}`$.');
  assert.ok(ordinary.issues.some(issue => issue.kind === 'math-delimiter'));
  assert.deepEqual(protectedMath.issues, []);
  assert.equal(ordinary.formulas[0].tex, protectedMath.formulas[0].tex);
  assert.equal(protectedMath.formulas[0].inline_syntax, 'protected');
});
test('emphasis guard covers italic, bold, protected math, and explicit HTML wrappers', () => {
  for (const text of ['*Caption $F(0)=1$.*', '**Caption $F(0)=1$.**',
    '*Caption $`F(0)=1`$.*', '<em>Caption $`F(0)=1`$.</em>']) {
    assert.ok(inspectMarkdown(text).issues.some(issue => issue.kind === 'math-context'), text);
  }
  assert.deepEqual(inspectMarkdown('*Caption.* The endpoint is $`F(0)=1`$.').issues, []);
});
test('local MathJax glyph ids cannot validate Markdown fragment links', () => {
  const doc = inspect('valid.md');
  const generatedId = doc.html.match(/id="(MJX-[^"]+)"/)[1];
  assert.ok(!doc.anchors.has(generatedId));
  assert.ok(![...doc.anchors].some(anchor => anchor.startsWith('MJX-')));
  doc.links.push({url: '#' + generatedId, image: false});
  checkLinks([doc], fixtures);
  assert.ok(doc.issues.some(issue => issue.kind === 'link' && issue.message.includes(generatedId)));
});
