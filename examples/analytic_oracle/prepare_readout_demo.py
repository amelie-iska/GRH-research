"""Export display-only views, bound to the full exact readout certificates."""
from pathlib import Path
import hashlib,json,argparse

ROOT=Path(__file__).resolve().parents[2]
def display(v):
    if isinstance(v,dict):
        if set(v)=={'numerator','denominator','display'}:return v['display']
        return {k:display(x) for k,x in v.items()}
    if isinstance(v,list):return [display(x) for x in v]
    return v

def run(target):
    if target.exists():raise FileExistsError('Preserve previous display export')
    records=[]
    for tolerance in ['1e-12','1e-15']:
        path=ROOT/f'outputs/experiments/2026-11-05-adaptive-readout-{tolerance}-v3/readout-certificates.json'
        raw=path.read_bytes();data=json.loads(raw)
        records.append({'requested_tolerance':tolerance,'certificate_path':str(path.relative_to(ROOT)),
            'certificate_sha256':hashlib.sha256(raw).hexdigest(),'producer_sha256':data['source_sha256'],
            'readouts':display(data['readouts'])})
    target.parent.mkdir(parents=True,exist_ok=True)
    target.write_text(json.dumps({'scope':'Display-only decimal projections of exact certificates. Use the linked Fraction endpoints for proofs. No zero-location, arbitrary-precision oracle, quantum-training or Lean claim.','runs':records},separators=(',',':'))+'\n')
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);a=p.parse_args();run(a.output)
