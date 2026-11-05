from pathlib import Path
from fractions import Fraction as F
from decimal import Decimal,localcontext
import json,subprocess
Q=Path(__file__).resolve().parent
face=[];tri=[]
with localcontext() as ctx:
 ctx.prec=70
 points={(i,[4,8,12,24,48][i%5]) for i in range(1001)}
 points.update((i,d) for i in [0,1,250,499,500,501,750,999,1000] for d in [4,8,12,24,48])
 for i,d in sorted(points):
  a=F(i,4000);r=F(1,4)+a;old=[r,F(5,4),F(11,12)+2*a/3];quad=[r,1+2*a];ordinary=[F(1),2*r]
  power=lambda e:Decimal(10)**(Decimal(d)*Decimal(e.numerator)/Decimal(e.denominator))
  op=max(old);qp=max(quad);historical=min(op,qp);np=max(ordinary);current=min(historical,np)
  assert np==current==1
  face.append(dict(a=float(a),d=d,old=list(map(float,old)),quad=list(map(float,quad)),ordinary=list(map(float,ordinary)),historical=float(historical),current=float(current),ordinarySum=float(sum(map(power,ordinary))),currentSum=float(min(sum(map(power,old)),sum(map(power,quad)),sum(map(power,ordinary))))) )
 for i in range(91):
  for j in range(91-i):
   x=F(3*i,4*90);y=F(3*j,8*90);rr=x+y;m=max(x,y);old=[rr,1+rr-m,F(2,3)+rr-m/3];ordinary=[F(1),2*rr];best=min(max(old),max(ordinary))
   assert best<=F(7,6)
   tri.append(dict(x=float(x),y=float(y),old=list(map(float,old)),ordinary=list(map(float,ordinary)),best=float(best),capacity=float(x+2*y)))
 assert max(c['best'] for c in tri)==float(F(7,6))
(Q/'expectations.json').write_text(json.dumps(dict(face=face,triangle=tri),separators=(',',':'))+'\n')
subprocess.run(['node',str(Q/'numeric-check.mjs')],check=True)
