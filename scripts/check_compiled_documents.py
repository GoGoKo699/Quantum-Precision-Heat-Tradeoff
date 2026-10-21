#!/usr/bin/env python3
"""Validate compiler logs after the released TeX Live CI builds (stdlib only)."""
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
STEMS = [ROOT/'paper/Quantum_Precision_Heat_Tradeoff_arXiv',
         ROOT/'learning/report/Quantum_Precision_Heat_Tradeoff_Report',
         ROOT/'build/documents/zip-extract/Quantum_Precision_Heat_Tradeoff_arXiv']


def check(stem):
    log=stem.with_suffix('.log').read_text(errors='replace')
    bad=[s for s in log.splitlines() if ('Overfull' in s or 'Missing character:' in s
         or 'undefined' in s.lower() or 'multiply defined' in s.lower()
         or 'destination with the same identifier' in s
         or 'Rerun to get cross-references right' in s)]
    if bad: raise AssertionError(f'{stem}: '+ '\n'.join(bad))
    match=re.search(r'Output written on .*?\((\d+) pages?,',log,re.S)
    assert match, stem
    pdf=stem.with_suffix('.pdf').read_bytes()
    assert pdf.startswith(b'%PDF-'),stem
    return {'file':str(stem.relative_to(ROOT))+'.pdf','pages':int(match.group(1)),
            'sha256':hashlib.sha256(pdf).hexdigest(),
            'notices':[s for s in log.splitlines() if 'Warning:' in s or 'Underfull' in s]}

if __name__=='__main__':
    results=[check(stem) for stem in STEMS]
    assert results[0]['pages']==results[2]['pages']
    record={'status':'passed','documents':results,
            'scope':'Compiler logs, PDF signatures, and clean-package page counts; visual review is separate.'}
    out=ROOT/'build/documents/ci_build_check.json'
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps(record,indent=2))
