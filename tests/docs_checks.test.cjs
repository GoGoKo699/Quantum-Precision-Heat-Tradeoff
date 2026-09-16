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
test('a coherent desktop-width formula passes while an oversized line is rejected', () => {
  const desktop = inspectMarkdown('```math\nx=' +
    Array.from({length: 10}, (_, i) => `a_{${i + 1}}`).join('+') + '.\n```\n');
  assert.deepEqual(desktop.issues, []);
  assert.ok(desktop.formulas[0].width_px > 310);
  assert.ok(desktop.formulas[0].width_px < 760);
  assert.ok(inspect('bad_width.md').issues.some(issue => issue.kind === 'width'));
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
test('raw prose regressions from the reported screenshots are rejected', () => {
  for (const text of [
    'For eigenpairs (p_i,u_i) and (q_j,v_j) of tau_0 and tau_1, define',
    'A term with p_i = q_j = 0 contributes zero.',
    'The second weighted sum is delta_0 + delta_1.',
    'Here Delta S_S = J(s), and the entropy is in nats.',
  ]) {
    assert.ok(inspectMarkdown(text).issues.some(issue => issue.kind === 'raw-math'), text);
  }
});
test('the raw-prose guard also covers powers, braced indices, and visible link labels', () => {
  for (const text of ['The scale is s^2.', 'The entry is r_{ij}.', '[tau_0](#state)']) {
    assert.ok(inspectMarkdown(text).issues.some(issue => issue.kind === 'raw-math'), text);
  }
  const doc = inspectMarkdown('The first line is prose.\nThe second has tau_0.');
  assert.equal(doc.issues.find(issue => issue.kind === 'raw-math').line, 2);
});
test('proper inline math and actual code stay outside the raw-prose guard', () => {
  const doc = inspectMarkdown([
    'Use $`\\tau_0`$, $`p_i=q_j=0`$, and $`\\Delta S_S=J(s)`$.',
    'The code identifiers `tau_0`, `S_S`, and `p_i` are literal code.',
    '', '```python', 'tau_0 = p_i + q_j', '```',
    '', '    delta_0 = delta_1',
  ].join('\n'));
  assert.deepEqual(doc.issues, []);
  assert.equal(doc.formulas.length, 3);
});
test('URLs, destinations, filenames, paths, and raw HTML do not become prose math', () => {
  const doc = inspectMarkdown([
    '[Source](https://example.org/tau_0) and <https://example.org/p_i>.',
    'The URL https://example.org/q_j and path docs/tau_0.md are references.',
    'Files p_i.csv and ../data/q_j.json are artifacts.',
    'Directory (docs/tau_0) and email <p_i@example.org> are references.',
    '<span data-state="tau_0">p_i = q_j</span> and <code>S_S</code>.',
    '<br>Normal text.',
    '', '<div>', 'delta_0 + delta_1', '</div>',
  ].join('\n'));
  assert.deepEqual(doc.issues, []);
});
test('ordinary prose and longer code identifiers do not require a math wrapper', () => {
  assert.deepEqual(inspectMarkdown(
    'The input_state, error_bound, check_docs, and delta_scale identifiers are names. ' +
    'Version 2.1 and a low-temperature bath are ordinary prose.'
  ).issues, []);
});
