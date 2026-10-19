#!/usr/bin/env python3
"""Inspect the actual GitHub renderer at one immutable repository revision."""
import json
import os
from pathlib import Path
from playwright.sync_api import sync_playwright

SHA = os.environ['QPH_INSPECTION_SHA']
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT/'build'/'hosted-inspection'
OUT.mkdir(parents=True, exist_ok=True)
PAGES = [
    ('README.md', True),
    ('learning/README.md', False),
    ('learning/SCHUMACHER_WESTMORELAND_BRIDGE.md', True),
    ('learning/02_device.md', True),
    ('learning/MILESTONES.md', True),
    ('science/theorem.md', True),
    ('science/kinematics.md', True),
    ('science/environment_information.md', True),
    ('science/heat_bound.md', True),
    ('science/channel_accuracy.md', True),
    ('science/exact_outputs.md', True),
]
report = {'revision': SHA, 'renderer': 'Actual github.com blob pages in Chromium',
          'viewport': {'width': 1440, 'height': 1000}, 'pages': [], 'errors': []}
with sync_playwright() as p:
    browser = p.chromium.launch()
    context = browser.new_context(viewport=report['viewport'], device_scale_factor=1)
    for index, (name, needs_math) in enumerate(PAGES):
        page = context.new_page()
        url = f'https://github.com/GoGoKo699/Quantum-Precision-Heat-Tradeoff/blob/{SHA}/{name}'
        row = {'file': name, 'url': url}
        try:
            response = page.goto(url, wait_until='domcontentloaded', timeout=60000)
            row['http_status'] = response.status if response else None
            if row['http_status'] != 200:
                raise RuntimeError(f'HTTP {row["http_status"]}')
            article = page.locator('article.markdown-body').first
            if not article.count():
                article = page.locator('.markdown-body').first
            article.wait_for(state='visible', timeout=30000)
            # GitHub enriches mathematical expressions after its initial HTML.
            if needs_math:
                page.wait_for_function('''() => {
                  function all(root) {
                    const nodes = [...root.querySelectorAll('*')];
                    return nodes.concat(nodes.flatMap(n => n.shadowRoot ? all(n.shadowRoot) : []));
                  }
                  return all(document).some(n => n.matches('mjx-container, .MathJax, math'));
                }''', timeout=45000)
            page.wait_for_timeout(1500)
            row.update(article.evaluate('''el => {
              function all(root) {
                const nodes = [...root.querySelectorAll('*')];
                return nodes.concat(nodes.flatMap(n => n.shadowRoot ? all(n.shadowRoot) : []));
              }
              const nodes=all(el), math=nodes.filter(n=>n.matches('mjx-container, .MathJax, math'));
              const failures=nodes.filter(n=>n.matches('merror,[data-mjx-error]')).map(n=>n.textContent);
              const text=el.innerText;
              const oversized=math.filter(n=>n.getBoundingClientRect().width>el.clientWidth+4)
                .map(n=>({width:n.getBoundingClientRect().width,available:el.clientWidth,text:n.textContent.slice(0,160)}));
              const images=[...el.querySelectorAll('img')].map(n=>({alt:n.alt,loaded:n.complete&&n.naturalWidth>0}));
              return {article_width:el.clientWidth,rendered_math_count:math.length,math_errors:failures,
                raw_protected_delimiters:text.includes('$`'),oversized_math:oversized,images,
                title:el.querySelector('h1')?.innerText};
            }'''))
            if row['math_errors'] or row['raw_protected_delimiters'] or row['oversized_math']:
                raise RuntimeError('Rendered mathematical error or desktop overflow')
            if any(not image['loaded'] for image in row['images']):
                raise RuntimeError('Unloaded content image')
            filename = f'{index:02d}-' + name.replace('/', '-').removesuffix('.md')
            page.screenshot(path=str(OUT/f'{filename}.png'), full_page=True)
            # A second viewport centers the first mathematical block where available.
            first = page.locator('math-renderer, mjx-container, .MathJax').first
            if first.count():
                first.scroll_into_view_if_needed()
            page.screenshot(path=str(OUT/f'{filename}-detail.png'))
            row['screenshot'] = filename + '.png'
            row['status'] = 'passed'
            print(json.dumps(row, ensure_ascii=False), flush=True)
        except Exception as exc:
            row['status'] = 'blocked' if row.get('http_status') != 200 else 'failed'
            row['error'] = str(exc)
            report['errors'].append({'file': name, 'error': str(exc)})
            page.screenshot(path=str(OUT/f'failure-{index:02d}.png'))
            print(json.dumps(row, ensure_ascii=False), flush=True)
        finally:
            report['pages'].append(row)
            page.close()
    browser.close()
(OUT/'report.json').write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n')
print('HOSTED_RENDER_RESULT=' + ('PASS' if not report['errors'] else 'NOT_VERIFIED'), flush=True)
raise SystemExit(bool(report['errors']))
