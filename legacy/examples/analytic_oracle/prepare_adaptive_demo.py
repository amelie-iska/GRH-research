"""Display-only projection of the accepted fresh-sampling family certificate."""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib,argparse
from precision import parse_integer
ROOT=Path(__file__).resolve().parents[2]
def rational(x):return F(parse_integer(x['numerator']),parse_integer(x['denominator']))
def display(x):
 if isinstance(x,dict):
  if {'numerator','denominator','display'}==set(x):return x['display']
  return {k:display(v) for k,v in x.items()}
 if isinstance(x,list):return [display(v) for v in x]
 return x

def run(output):
 if output.exists():raise FileExistsError('Preserve prior display output')
 path=ROOT/'outputs/experiments/2026-11-05-adaptive-family-1e-24-final-v2/family-certificates.json'
 data=path.read_bytes();source=json.loads(data);models=[]
 for r in source['readouts']:
  shown=display(r);targets=[tuple(map(rational,p)) for p in r['targets']]
  base=sum((rational(v) for k,v in r['budget'].items() if k!='optimization'),F())
  rounding_margin=rational(r['budget']['optimization'])-rational(r['trace'][-1]['residual'])
  assert rounding_margin>=0
  for original,row in zip(r['trace'],shown['trace']):
   scale=rational(original['coefficient_scale']);row['coefficients']=[[float(scale*a),float(scale*b)] for a,b in targets]
   row['gradient']=[[float((scale-1)*a),float((scale-1)*b)] for a,b in targets]
   row['uniform_bound']=float(base+rational(original['residual'])+rounding_margin)
  assert shown['trace'][-1]['uniform_bound']==shown['compact_uniform_bound']
  shown['adaptive_sampling']=True;models.append(shown)
 result={'requested_tolerance':'1e-24','certificate_path':str(path.relative_to(ROOT)),'certificate_sha256':hashlib.sha256(data).hexdigest(),'producer_sha256':source['source_sha256'],'readouts':models,'scope':'Display-only decimal projections; exact rational certificate and lossless trace encoding are authoritative.'}
 output.parent.mkdir(parents=True,exist_ok=True);output.write_text(json.dumps(result,separators=(',',':'))+'\n')
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);a=p.parse_args();run(a.output)
