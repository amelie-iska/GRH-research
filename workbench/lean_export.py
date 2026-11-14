"""Emit and optionally kernel-check fixed Lean templates; never run supplied code."""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import subprocess
import tempfile
from contracts import replay, digest, rational

ROOT=Path(__file__).resolve().parent
TEMPLATE=ROOT/'lean/FiniteContracts.lean'


def pair(s: str) -> str:
    q=rational(s)
    return f'({q.numerator}, {q.denominator})'


def qlist(xs: list[str]) -> str:
    return '['+', '.join(pair(x) for x in xs)+']'


def lean_source(cert: dict) -> str:
    c=replay(cert);i=c['inputs'];o=c['claim'];kind=c['kind']
    if kind=='heat': expression=f"heatValid {pair(i['r'])}"
    elif kind=='gain': expression='gainValid ['+', '.join(qlist(row) for row in i['matrix'])+f"] {qlist(i['weights'])} {pair(i['rate'])}"
    elif kind=='rank': expression=f"rankValid {i['draws']} {i['exceedances']} {pair(o['p'])} {pair(o['resolution'])}"
    elif kind=='risk': expression=f"riskValid {i['tests']} {pair(i['per_test'])} {pair(i['drift'])} {pair(i['alpha'])} {pair(o['upper_bound'])}"
    else: expression=f"mutationValid {json.dumps(i['matrix'])} {qlist(i['seed'])} {i['vertex']} {json.dumps(o['matrix'])} {qlist(o['seed'])}"
    name='payload_'+digest(c)
    return TEMPLATE.read_text()+f'\nnamespace WorkbenchFinite\n-- Certificate SHA-256: {digest(c)}\ntheorem {name} :\n    {expression} = true := by decide\n#check {name}\n#print axioms {name}\nend WorkbenchFinite\n'


def check(cert: dict, lean: Path, timeout: float=30) -> dict:
    source=lean_source(cert)
    lean=lean.resolve(strict=True)
    version=subprocess.run([str(lean),'--version'],capture_output=True,text=True,timeout=5,check=True).stdout.strip()
    if 'version 4.24.0,' not in version:
        raise ValueError('Use the explicitly pinned Lean 4.24.0 compiler')
    with tempfile.TemporaryDirectory(prefix='grh-finite-') as tmp:
        path=Path(tmp)/'Certificate.lean';path.write_text(source)
        try:
            result=subprocess.run([str(lean),str(path)],cwd=tmp,capture_output=True,text=True,timeout=timeout)
            log=result.stdout+result.stderr
            name='WorkbenchFinite.payload_'+digest(cert)
            axiom_free=f"'{name}' does not depend on any axioms" in log
            ok=result.returncode==0 and axiom_free and 'sorryAx' not in log and 'warning:' not in log
            status='kernel_checked' if ok else 'rejected'
        except subprocess.TimeoutExpired:
            result=None;log='Lean verification exceeded the bounded time budget.';status='timeout';axiom_free=False
    return {'schema':'grh.workbench.receipt.v1','status':status,'certificate_sha256':digest(cert),
            'lean_source_sha256':hashlib.sha256(source.encode()).hexdigest(),
            'template_sha256':hashlib.sha256(TEMPLATE.read_bytes()).hexdigest(),
            'exporter_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'contracts_sha256':hashlib.sha256((ROOT/'contracts.py').read_bytes()).hexdigest(),
            'compiler_sha256':hashlib.sha256(lean.read_bytes()).hexdigest(),
            'lean_version':version,'axiom_free':axiom_free,
            'exit_code':None if result is None else result.returncode,
            'checked_at_utc':datetime.now(timezone.utc).isoformat(),'log':log[-8000:],
            'scope':cert['scope'],'authentication':'Local process receipt, not a signed remote attestation.'}


def strict_json(text: str) -> dict:
    def pairs(items):
        out={}
        for k,v in items:
            if k in out: raise ValueError('Duplicate JSON key')
            out[k]=v
        return out
    def constant(_): raise ValueError('Nonfinite JSON token')
    if len(text.encode('utf8'))>65536: raise ValueError('JSON body too large')
    value=json.loads(text,object_pairs_hook=pairs,parse_constant=constant)
    replay(value)
    return value

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('certificate',type=Path);p.add_argument('--lean',type=Path)
    p.add_argument('--source',type=Path);p.add_argument('--receipt',type=Path)
    a=p.parse_args();c=strict_json(a.certificate.read_text())
    if a.source: a.source.write_text(lean_source(c))
    if a.lean:
        r=check(c,a.lean)
        if a.receipt: a.receipt.write_text(json.dumps(r,indent=2)+'\n')
        print(json.dumps(r,indent=2));raise SystemExit(0 if r['status']=='kernel_checked' else 1)
    if not a.source: print(lean_source(c))
