#!/usr/bin/env node
/* Local markdown-it + MathJax SVG checks. This is NOT GitHub's live renderer.
 * Widths use MathJax TeX font geometry at 16px, ex=8px, not browser font metrics.
 * Browser screenshots and DOM overflow inspection remain a separate gate.
 */
'use strict';
const fs = require('node:fs');
const path = require('node:path');
const MarkdownIt = require('markdown-it');
const parse5 = require('parse5');
const GithubSlugger = require('github-slugger').default;
const {mathjax} = require('mathjax-full/js/mathjax.js');
const {TeX} = require('mathjax-full/js/input/tex.js');
const {SVG} = require('mathjax-full/js/output/svg.js');
const {liteAdaptor} = require('mathjax-full/js/adaptors/liteAdaptor.js');
const {RegisterHTMLHandler} = require('mathjax-full/js/handlers/html.js');
require('mathjax-full/js/input/tex/ams/AmsConfiguration.js');
require('mathjax-full/js/input/tex/newcommand/NewcommandConfiguration.js');
require('mathjax-full/js/input/tex/boldsymbol/BoldsymbolConfiguration.js');

const ROOT = path.resolve(__dirname, '..');
const WIDTH = 310;
const adaptor = liteAdaptor();
RegisterHTMLHandler(adaptor);
const tex = new TeX({packages: ['base', 'ams', 'newcommand', 'boldsymbol'],
  formatError: (_jax, error) => {throw new Error(error.message);}});
const output = new SVG({fontCache: 'local'});
const mathDocument = mathjax.document('', {InputJax: tex, OutputJax: output});
const escape = value => String(value).replace(/[&<>"']/g,
  char => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[char]));
const slash = value => value.split(path.sep).join('/');

function markdownFiles(root) {
  const ignored = new Set(['.git', 'node_modules', 'build', 'dist', '.venv', 'tests']);
  const found = [];
  function visit(dir) {
    for (const entry of fs.readdirSync(dir, {withFileTypes: true})) {
      if (ignored.has(entry.name) || entry.name.startsWith('.')) continue;
      const file = path.join(dir, entry.name);
      if (entry.isDirectory()) visit(file);
      else if (entry.name.endsWith('.md')) found.push(file);
    }
  }
  visit(root);
  return found.sort();
}

function parser() {
  const md = new MarkdownIt({html: true, linkify: false, typographer: false});
  md.inline.ruler.before('escape', 'inline_math', (state, silent) => {
    const start = state.pos;
    if (state.src[start] !== '$') return false;
    const backtick = state.src[start + 1] === '`';
    const delimiter = backtick ? '`$' : '$';
    const contentStart = start + (backtick ? 2 : 1);
    let end = contentStart;
    while ((end = state.src.indexOf(delimiter, end)) !== -1) {
      let escapes = 0;
      for (let i = end - 1; i >= contentStart && state.src[i] === '\\'; i--) escapes++;
      if (escapes % 2 === 0) break;
      end += delimiter.length;
    }
    if (silent) return end !== -1;
    const token = state.push(end === -1 ? 'math_error' : 'math_inline', 'math', 0);
    token.content = end === -1 ? 'Unclosed inline math delimiter' : state.src.slice(contentStart, end);
    state.pos = end === -1 ? state.posMax : end + delimiter.length;
    return true;
  });
  // Repository display convention is fenced math. Parse the other GitHub form
  // as math too, so introducing $$ cannot evade actual compilation.
  md.block.ruler.before('fence', 'dollar_math', (state, start, end, silent) => {
    const line = state.src.slice(state.bMarks[start] + state.tShift[start], state.eMarks[start]);
    if (line.trim() !== '$$') return false;
    if (silent) return true;
    let close = start + 1;
    while (close < end && state.src.slice(state.bMarks[close], state.eMarks[close]).trim() !== '$$') close++;
    const token = state.push(close === end ? 'math_error' : 'math_block', 'math', 0);
    token.block = true;
    token.content = close === end ? 'Unclosed display math delimiter' : state.getLines(start + 1, close, state.blkIndent, false);
    token.map = [start, Math.min(close + 1, end)];
    state.line = Math.min(close + 1, end);
    return true;
  });
  return md;
}

function walk(node, fn) {
  fn(node);
  for (const child of node.childNodes || []) walk(child, fn);
}

function compileMath(source, display) {
  if (!source.trim()) throw new Error('Empty math expression');
  if (/\\(?:newcommand|renewcommand|providecommand|def|gdef|let|require|tag|label)\b/.test(source))
    throw new Error('Custom macros, extensions, and equation tags are not permitted');
  tex.reset();
  const node = mathDocument.convert(source, {display, em: 16, ex: 8, containerWidth: WIDTH});
  const html = adaptor.outerHTML(node);
  if (/data-mjx-error|<merror\b/.test(html)) throw new Error('MathJax reported a TeX error');
  const svg = adaptor.firstChild(node);
  const viewBox = (adaptor.getAttribute(svg, 'viewBox') || '').split(/\s+/).map(Number);
  if (viewBox.length !== 4 || !Number.isFinite(viewBox[2])) throw new Error('No finite MathJax SVG geometry');
  const width = adaptor.getAttribute(svg, 'width');
  const height = adaptor.getAttribute(svg, 'height');
  if (!/^\d+(?:\.\d+)?ex$/.test(width) || !/^\d+(?:\.\d+)?ex$/.test(height))
    throw new Error('Expected finite MathJax SVG dimensions in ex units');
  // MathJax emits intrinsic dimensions in ex. Use the declared ex=8px estimate;
  // the preview/browser may differ with its actual surrounding font metrics.
  return {html, width_px: parseFloat(width) * 8, height_px: parseFloat(height) * 8};
}

function inspectMarkdown(source, name = 'fixture.md') {
  const md = parser();
  const environment = {};
  const tokens = md.parse(source, environment);
  const issues = [], formulas = [], links = [], anchors = new Set();
  const slugger = new GithubSlugger();
  const lines = source.split('\n');
  const issue = (kind, line, message) => issues.push({file: name, line, kind, message});
  if (/(?:sandbox:|file:\/\/|\/workspace\/|\/home\/oai\/|\/mnt\/data\/|\bturn\d+(?:search|view|fetch|file)\d*|\bfile_[0-9a-f]{12,}|\blibfile_|\ue200|\ue202)/i.test(source))
    issue('environment', 1, 'Environment-specific path or citation');
  let heading = false, nestedDisplay = 0;
  function recordMath(token, line, display) {
    if (heading) issue('heading', line, 'Use plain-text headings with stable anchors');
    if (display && nestedDisplay) issue('math-context', line, 'Display math cannot be placed in tables or block quotes');
    try {
      const rendered = compileMath(token.content, display);
      token.meta = rendered;
      const entry = {file: name, line, display, tex: token.content.trim(),
        width_px: Number(rendered.width_px.toFixed(3)), height_px: Number(rendered.height_px.toFixed(3))};
      formulas.push(entry);
      if (entry.width_px > WIDTH) issue('width', line,
        `MathJax SVG geometry ${entry.width_px}px exceeds ${WIDTH}px reading column`);
    } catch (error) {issue('math', line, error.message);}
  }
  let currentLine = 1;
  for (let index = 0; index < tokens.length; index++) {
    const token = tokens[index];
    if (token.map) currentLine = token.map[0] + 1;
    const line = currentLine;
    if (token.type === 'heading_open') {
      heading = true;
      const content = tokens[index + 1]?.children || [];
      const plain = content.filter(child => !['html_inline', 'softbreak'].includes(child.type)).map(child => child.content).join('');
      const slug = slugger.slug(plain);
      anchors.add(slug);
      token.attrSet('id', slug);
    }
    if (token.type === 'heading_close') heading = false;
    if (['blockquote_open', 'table_open'].includes(token.type)) nestedDisplay++;
    if (['blockquote_close', 'table_close'].includes(token.type)) nestedDisplay--;
    if (token.type === 'fence') {
      const closing = lines[token.map[1] - 1] || '';
      const marker = token.markup[0];
      const closePattern = new RegExp(`^ {0,3}${marker}{${token.markup.length},}\\s*$`);
      if (!closePattern.test(closing)) issue('fence', line, 'Unclosed fenced code block');
      if (token.info.trim() === 'math') recordMath(token, line, true);
    }
    if (token.type === 'math_block') recordMath(token, line, true);
    if (token.type === 'math_error') issue('math', line, token.content);
    for (const child of token.children || []) {
      if (child.type === 'math_inline') recordMath(child, line, false);
      if (child.type === 'math_error') issue('math', line, child.content);
      if (child.type === 'text' && /\[[^\]\n]+\]\s*\[[^\]\n]+\]/.test(child.content))
        issue('reference', line, 'Unresolved Markdown reference link');
      if (child.type === 'text' && /\[[^\]\n]+\]\(/.test(child.content))
        issue('markdown', line, 'Malformed Markdown link');
    }
  }
  const originalFence = md.renderer.rules.fence;
  const renderMath = token => token.meta?.html || `<strong class="math-error">${escape(token.content)}</strong>`;
  md.renderer.rules.math_inline = (list, i) => renderMath(list[i]);
  md.renderer.rules.math_block = (list, i) => `<div class="math-display">${renderMath(list[i])}</div>`;
  md.renderer.rules.math_error = (list, i) => `<strong class="math-error">${escape(list[i].content)}</strong>`;
  md.renderer.rules.fence = (list, i, opts, env, self) => list[i].info.trim() === 'math'
    ? `<div class="math-display">${renderMath(list[i])}</div>\n` : originalFence(list, i, opts, env, self);
  const html = md.renderer.render(tokens, md.options, environment);
  const fragment = parse5.parseFragment(html);
  walk(fragment, node => {
    const attrs = Object.fromEntries((node.attrs || []).map(attr => [attr.name, attr.value]));
    if (attrs.id && !/^h[1-6]$/.test(node.tagName || '')) {
      if (anchors.has(attrs.id)) issue('anchor', 1, `Duplicate anchor: ${attrs.id}`);
      anchors.add(attrs.id);
    }
    if (node.tagName === 'a' && attrs.name) anchors.add(attrs.name);
    if (node.tagName === 'a' && attrs.href) links.push({url: attrs.href, image: false});
    if (node.tagName === 'img') {
      if (!attrs.alt?.trim()) issue('image-alt', 1, `Image has no meaningful alt text: ${attrs.src || '(missing src)'}`);
      if (!attrs.src) issue('image', 1, 'Image has no source');
      else links.push({url: attrs.src, image: true});
    }
  });
  return {name, html, anchors, formulas, links, issues};
}

function checkLinks(documents, root) {
  const byName = new Map(documents.map(doc => [doc.name, doc]));
  let checked = 0;
  for (const doc of documents) {
    for (const link of doc.links) {
      const problem = message => doc.issues.push({file: doc.name, line: 1, kind: 'link', message});
      if (/^(?:https?:|mailto:)/i.test(link.url)) continue;
      if (/^[a-z][a-z\d+.-]*:/i.test(link.url) || link.url.startsWith('//')) {
        problem(`Unsupported local-link scheme: ${link.url}`); continue;
      }
      let target, fragment;
      try {
        const hash = link.url.indexOf('#');
        target = decodeURIComponent((hash < 0 ? link.url : link.url.slice(0, hash)).split('?')[0]);
        fragment = hash < 0 ? '' : decodeURIComponent(link.url.slice(hash + 1));
      } catch {problem(`Malformed URL escape: ${link.url}`); continue;}
      let resolved = target ? path.resolve(root, path.dirname(doc.name), target) : path.resolve(root, doc.name);
      if (!resolved.startsWith(root + path.sep) || !fs.existsSync(resolved)) {
        problem(`Missing or outside-repository destination: ${link.url}`); continue;
      }
      checked++;
      if (fs.statSync(resolved).isDirectory()) {
        if (fragment) problem(`Directory link cannot have a document fragment: ${link.url}`);
        continue;
      }
      if (!fragment) continue;
      const targetName = slash(path.relative(root, resolved));
      const targetDoc = byName.get(targetName);
      if (targetDoc) {
        if (!targetDoc.anchors.has(fragment)) problem(`Missing Markdown anchor: ${link.url}`);
      } else if (/^L\d+(?:-L\d+)?$/.test(fragment)) {
        const [first, last = first] = fragment.match(/\d+/g).map(Number);
        const length = fs.readFileSync(resolved, 'utf8').trimEnd().split('\n').length;
        if (first < 1 || last < first || last > length) problem(`Code line fragment outside file: ${link.url}`);
      } else if (/\.(?:svg|html?)$/i.test(resolved)) {
        const ids = new Set();
        walk(parse5.parseFragment(fs.readFileSync(resolved, 'utf8')), node => {
          for (const attr of node.attrs || []) if (attr.name === 'id') ids.add(attr.value);
        });
        if (!ids.has(fragment)) problem(`Missing HTML/SVG anchor: ${link.url}`);
      } else problem(`Unsupported file fragment (use GitHub line anchors for code): ${link.url}`);
    }
  }
  return checked;
}

const CSS = `:root{color-scheme:light dark;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;font-size:16px;line-height:1.6;color:#1f2328;background:#fff}*{box-sizing:border-box}body{margin:0}main{max-width:1012px;padding:24px 32px;margin:auto}h1,h2{border-bottom:1px solid #d0d7de;padding-bottom:.3em}h1{font-size:2em}h2{font-size:1.5em}a{color:#0969da}img{max-width:100%;height:auto}p,li{overflow-wrap:break-word}pre{padding:16px;overflow:auto;background:#f6f8fa;border-radius:6px}code{font-family:ui-monospace,monospace;font-size:.85em}table{display:block;width:max-content;max-width:100%;overflow:auto;border-collapse:collapse}td,th{border:1px solid #d0d7de;padding:6px 10px;min-width:110px}tr:nth-child(2n){background:#f6f8fa}.math-display{margin:1em 0;text-align:center}.math-display mjx-container{display:block;margin:0}mjx-container svg{max-width:none}mjx-container:not([display="true"]){display:inline-block}.renderer-note{font-size:12px;color:#57606a;border-bottom:1px solid #d0d7de;padding:8px 20px}.math-error{color:#b42318}@media(max-width:600px){main{padding:16px 20px}h1{font-size:1.8em}}@media(prefers-color-scheme:dark){:root{color:#e6edf3;background:#0d1117}a{color:#58a6ff}pre,tr:nth-child(2n){background:#161b22}td,th,h1,h2,.renderer-note{border-color:#30363d}.renderer-note{color:#8b949e}}html[data-theme="dark"]{color:#e6edf3;background:#0d1117}html[data-theme="dark"] a{color:#58a6ff}html[data-theme="dark"] pre,html[data-theme="dark"] tr:nth-child(2n){background:#161b22}html[data-theme="dark"] td,html[data-theme="dark"] th,html[data-theme="dark"] h1,html[data-theme="dark"] h2{border-color:#30363d}`;

function render(documents, root, destination, report) {
  fs.mkdirSync(destination, {recursive: true});
  const themeScript = `<script>if(new URLSearchParams(location.search).get('theme')==='dark')document.documentElement.dataset.theme='dark';</script>`;
  for (const doc of documents) {
    const target = path.join(destination, doc.name.replace(/\.md$/, '.html'));
    fs.mkdirSync(path.dirname(target), {recursive: true});
    const fragment = parse5.parseFragment(doc.html);
    walk(fragment, node => {
      for (const attr of node.attrs || []) {
        if (attr.name === 'href' && !/^[a-z]+:/i.test(attr.value)) attr.value = attr.value.replace(/\.md(?=#|$)/, '.html');
      }
    });
    fs.writeFileSync(target, `<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>${escape(doc.name)} — local QA</title><style>${CSS}</style>${themeScript}<body><div class="renderer-note">Local QA: markdown-it 14.1.0 + MathJax 3.2.2 SVG, repository CSS. This is not live GitHub rendering.</div><main>${parse5.serialize(fragment)}</main></body></html>\n`);
    for (const link of doc.links) {
      if (/^[a-z]+:/i.test(link.url) || link.url.startsWith('#')) continue;
      const relative = decodeURIComponent(link.url.split('#')[0]);
      const source = path.resolve(root, path.dirname(doc.name), relative);
      if (source.startsWith(root + path.sep) && fs.existsSync(source) && fs.statSync(source).isFile() && !source.endsWith('.md')) {
        const copy = path.join(destination, path.relative(root, source));
        fs.mkdirSync(path.dirname(copy), {recursive: true});
        fs.copyFileSync(source, copy);
      }
    }
  }
  const options = documents.map(doc => `<option value="${escape(doc.name.replace(/\.md$/, '.html'))}">${escape(doc.name)}</option>`).join('');
  const controls = `<label>Page <select id="page">${options}</select></label> <label>Width <select id="width">${[350,390,430,1280,1440].map(n=>`<option>${n}</option>`).join('')}</select></label> <label>Theme <select id="theme"><option>light</option><option>dark</option></select></label> <button id="measure">Measure browser overflow</button><pre id="metrics"></pre><iframe id="frame" title="Local document render" style="height:2200px;border:1px solid #888"></iframe>`;
  const script = `<script>const frame=document.querySelector('#frame'),page=document.querySelector('#page'),width=document.querySelector('#width'),theme=document.querySelector('#theme');function update(){frame.style.width=width.value+'px';frame.src=page.value+'?theme='+theme.value}for(const el of [page,width,theme])el.onchange=update;document.querySelector('#measure').onclick=()=>{try{const d=frame.contentDocument,r=d.documentElement;const wide=[...d.querySelectorAll('mjx-container,table,pre,img')].filter(e=>e.getBoundingClientRect().right>r.clientWidth||e.scrollWidth>e.clientWidth+1).map(e=>({tag:e.tagName,width:e.getBoundingClientRect().width,scrollWidth:e.scrollWidth,clientWidth:e.clientWidth}));document.querySelector('#metrics').textContent=JSON.stringify({renderer:'local markdown-it/MathJax SVG; not GitHub',viewportWidth:r.clientWidth,pageScrollWidth:r.scrollWidth,theme:theme.value,wideElements:wide},null,2)}catch(e){document.querySelector('#metrics').textContent='DOM measurement blocked by file-origin policy: '+e.message}};update();</script>`;
  fs.writeFileSync(path.join(destination, 'index.html'), `<!doctype html><html lang="en"><meta charset="utf-8"><title>Local documentation QA</title><body><h1>Local documentation QA</h1><p>Standalone iframe widths are local viewport simulations; these are not live GitHub screenshots.</p>${controls}${script}</body></html>`);
  fs.writeFileSync(path.join(destination, 'manifest.json'), JSON.stringify(report, null, 2)+'\n');
}

function inspectRepository(root = ROOT, destination = null) {
  const documents = markdownFiles(root).map(file => inspectMarkdown(fs.readFileSync(file, 'utf8'), slash(path.relative(root, file))));
  const links = checkLinks(documents, root);
  const report = {renderer: 'markdown-it 14.1.0 + MathJax 3.2.2 SVG; repository CSS; not live GitHub',
    measurements: 'MathJax SVG intrinsic ex units at 8 px/ex (16 px text); not browser pixel layout',
    stress_viewport_px: 350, reading_column_px: WIDTH,
    preview_viewports_px: [350, 390, 430, 1280, 1440],
    pages: documents.map(doc => ({file: doc.name, html: doc.name.replace(/\.md$/, '.html'), formulas: doc.formulas.length, anchors: [...doc.anchors]})),
    checked_local_links: links, formulas: documents.flatMap(doc => doc.formulas), issues: documents.flatMap(doc => doc.issues)};
  if (destination) render(documents, root, destination, report);
  return report;
}

if (require.main === module) {
  const args = process.argv.slice(2);
  let destination = null;
  if (args.length) {
    if (args.length !== 2 || args[0] !== '--render') throw new Error('Usage: node scripts/check_docs.cjs [--render directory]');
    destination = path.resolve(ROOT, args[1]);
  }
  const result = inspectRepository(ROOT, destination);
  for (const item of result.issues) console.error(`${item.file}:${item.line}: ${item.kind}: ${item.message}`);
  console.log(`${result.issues.length ? 'FAIL' : 'PASS'}: ${result.pages.length} Markdown pages, ${result.checked_local_links} local destinations/fragments, ${result.formulas.length} compiled math expressions; local ${WIDTH}px SVG-geometry width gate.`);
  if (destination) console.log(`Local HTML, all-page manifest, and per-formula widths: ${slash(path.relative(ROOT, destination))}`);
  process.exitCode = result.issues.length ? 1 : 0;
}
module.exports = {inspectMarkdown, checkLinks, inspectRepository, compileMath, markdownFiles};
