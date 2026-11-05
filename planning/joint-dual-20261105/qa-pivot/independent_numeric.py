"""Independent exact exponent and 70-digit Decimal monomial expectations."""
from pathlib import Path
from fractions import Fraction as F
from decimal import Decimal,localcontext
import json,subprocess
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
cases=[]
points={(i,[4,8,12,24,48][i%5]) for i in range(1001)}
points.update((i,d) for i in [0,1,250,499,500,501,750,999,1000] for d in [4,8,12,24,48])
with localcontext() as ctx:
 ctx.prec=70
 for i,d in sorted(points):
  a=F(i,4000);exponents=[a,a,F(1,4)-a,F(0),F(0),F(0)]
  r=sum(exponents);weighted=sum((j+1)*v for j,v in enumerate(exponents));m=max(exponents[:2]);q=exponents[2]
  old=[r,1+r-m,F(2,3)+r-m/3];quad=[r,1+r-q]
  op=max(old);qp=max(quad);rp=min(op,qp)
  assert weighted==F(3,4)
  assert op==F(5,4)
  assert rp==min(F(5,4),1+2*a)
  assert (op-rp>0)==(a<F(1,8))
  assert rp>F(3,4)
  def power(e):return Decimal(10)**(Decimal(d)*Decimal(e.numerator)/Decimal(e.denominator))
  aj=list(map(power,exponents));ot=list(map(power,old));qt=list(map(power,quad))
  cases.append(dict(a=float(a),dLog=d,Aj=list(map(float,aj)),D=float(power(F(1))),H=float(power(F(3,4))),A=float(aj[0]),B=float(aj[2]),R=float(power(r)),capacity=float(power(weighted)),oldPowers=list(map(float,old)),quadPowers=list(map(float,quad)),oldTerms=list(map(float,ot)),quadTerms=list(map(float,qt)),oldPower=float(op),quadPower=float(qp),refinedPower=float(rp),saving=float(op-rp),targetGap=float(rp-F(3,4)),oldSum=float(sum(ot)),quadSum=float(sum(qt)),refinedSum=float(min(sum(ot),sum(qt))),strictSaving=a<F(1,8)))
(HERE/'independent-expectations.json').write_text(json.dumps(dict(method='Fraction exponents; 70-digit Decimal monomial evaluations; no import of production JavaScript',cases=cases),separators=(',',':'))+'\n')
subprocess.run(['node',str(HERE/'numeric-check.mjs')],cwd=ROOT,check=True)
