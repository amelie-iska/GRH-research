from pathlib import Path
from fractions import Fraction as F
import argparse,json,hashlib,time,math
import mpmath as mp
mp.mp.dps=110
ROOT=Path('/home/iska/Documents/LaTeX-projects/GRH-from-Mac-20261104')
FAMILIES={3:(1,[0,1,-1]),4:(1,[0,1,0,-1]),5:(0,[0,1,-1,-1,1])}
def frac(d):return F(int(d['numerator']),int(d['denominator']))
def number(x):return mp.mpf(x.numerator)/x.denominator
def endpoint(d):return F(int(d['lo']),1<<d['dyadic_bits']),F(int(d['hi']),1<<d['dyadic_bits'])
def contained(box,z):
 for k,x in [('real',z.real),('imag',z.imag)]:
  lo,hi=endpoint(box[k]);assert number(lo)<=x<=number(hi),(k,float(x),float(lo),float(hi))
def radius(box):
 return sum(((endpoint(box[k])[1]-endpoint(box[k])[0])/2 for k in ['real','imag']),F())
def target(q,s):
 a,chi=FAMILIES[q];return (q/mp.pi)**((s+a)/2)*mp.gamma((s+a)/2)*mp.dirichlet(s,chi)
def main(directory):
 data=json.loads((directory/'oracle-certificates.json').read_text());assert data['GRH_proved'] is False and data['new_Lean_declarations']==0
 for name,h in data['source_sha256'].items():assert hashlib.sha256((directory/name).read_bytes()).hexdigest()==h
 rows=data['samples'];assert len(rows)==192
 max_abs=mp.mpf(0);max_ratio=mp.mpf(0);max_node_width=F();component_checks=0
 grouped={q:[] for q in FAMILIES}
 for row in rows:
  q,j,m=row['q'],row['node_index'],row['node_count'];assert q in FAMILIES and type(j)is int and m==64
  z=mp.exp(2j*mp.pi*j/m);s=mp.mpf(1)/2+mp.mpf(6)/5*z;contained(row['root_box'],z);contained(row['node_box'],s)
  max_node_width=max(max_node_width,radius(row['node_box']));center=mp.mpc(number(frac(row['center_real'])),number(frac(row['center_imag'])));actual=abs(target(q,s)-center);bound=frac(row['radius']);assert actual<=number(bound),(q,j,float(actual),float(bound))
  max_abs=max(max_abs,actual);max_ratio=max(max_ratio,actual/number(bound))
  raw=radius(row['quadrature_sum_box']);parts=raw+sum(frac(row[k]) for k in ['n_tail','time_tail','quadrature','discard']);assert bound>=parts and bound-parts<F(1,1<<180)
  assert frac(row['interval_radius'])>=raw
  assert all(frac(row[k])>=0 for k in ['radius','interval_radius','n_tail','time_tail','quadrature','discard']);component_checks+=8;grouped[q].append(row)
 polynomials=[]
 for model in data['readouts']:
  q=model['q'];grouped[q].sort(key=lambda r:r['node_index']);assert [r['node_index'] for r in grouped[q]]==list(range(64));degree=model['degree'];assert degree==28 and model['steps']==180
  eta=max(frac(r['radius']) for r in grouped[q]);u=F(7,12);v=F(7,24);w=F(1,2)**64;M=model['M_r_integer_bound'];assert M=={3:4,4:10,5:6}[q]
  raw_parts={'oracle':eta*(1-u**(degree+1))/(1-u),'alias':M*w/(1-w)*(1-v**(degree+1))/(1-v),'Taylor':M*v**(degree+1)/(1-v)}
  for k,raw in raw_parts.items():assert frac(model[k])>=raw and frac(model[k])-raw<F(1,1<<180)
  # Independently compute DFT/GD coefficients with high-precision complex arithmetic.
  labels=[mp.mpc(number(frac(r['center_real'])),number(frac(r['center_imag']))) for r in grouped[q]]
  coefficients=[];factor=1-(mp.mpf(3)/4)**180
  for n,record in enumerate(model['coefficients']):
   exact_iteration=factor*sum(y*mp.exp(-2j*mp.pi*j*n/64) for j,y in enumerate(labels))/64;contained(record['exact_GD_coefficient_enclosure'],exact_iteration);coefficients.append(mp.mpc(number(frac(record['real'])),number(frac(record['imag']))))
  arithmetic=sum(radius(c['exact_GD_coefficient_enclosure'])*u**n for n,c in enumerate(model['coefficients']));assert frac(model['coefficient_arithmetic'])>=arithmetic
  pieces=sum(frac(model[k]) for k in ['optimization','oracle','alias','Taylor','coefficient_arithmetic']);budget=frac(model['compact_uniform_bound'])
  assert budget>=pieces,'Printed budget below exported component sum'
  observed=mp.mpf(0)
  for j in range(48):
   z=mp.mpf(7)/10*mp.exp(2j*mp.pi*j/48);s=mp.mpf(1)/2+z;prediction=sum(c*(z/(mp.mpf(6)/5))**n for n,c in enumerate(coefficients));error=abs(prediction-target(q,s));assert error<=number(budget);observed=max(observed,error)
  polynomials.append({'q':q,'uniform_certificate':float(budget),'observed_48_boundary_error':float(observed),'all_coefficient_enclosures_contain_independent_DFT':True})
 report={'passed':True,'directory':str(directory),'source_sha256':data['source_sha256'],'sample_count':len(rows),'sample_component_checks':component_checks,'all_circle_nodes_contain_highprecision_reference':True,'max_sample_reference_error':float(max_abs),'max_observed_error_to_certified_radius':float(max_ratio),'max_node_box_L1_radius':float(max_node_width),'polynomials':polynomials,'reference_mpmath_version':mp.__version__,'diagnostic_comparisons_not_interval_proofs':True}
 out=ROOT/'outputs/checks/2026-11-04-validated-oracle/review';out.mkdir(parents=True,exist_ok=True);p=out/('full-dataset-independent-'+str(time.time_ns())+'.json');p.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({'report':str(p),**report}))
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--directory',type=Path,required=True);main(p.parse_args().directory)
