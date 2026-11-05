from pathlib import Path
from fractions import Fraction as F
import sys,json,hashlib,time
ROOT=Path('/home/iska/Documents/LaTeX-projects/GRH-from-Mac-20261104');sys.path.insert(0,str(ROOT/'examples/analytic_oracle'))
import dyadic as d,theta_oracle as t
cases=[];s=d.C(d.real(F(1,2)),d.real(0))
def reject(name,call):
 try:call()
 except (ValueError,TypeError,ZeroDivisionError):cases.append(name)
 else:raise AssertionError('Accepted invalid request: '+name)
# Prime a cache, then attack equality/hash aliases with distinct input types.
d.log_fraction(F(1));t.circle_node(0,64);t.analytic_error(3,12)
reject('cached-log-float-one',lambda:d.log_fraction(1.0))
reject('cached-log-int-one',lambda:d.log_fraction(1))
reject('cached-circle-float-index',lambda:t.circle_node(0.0,64))
reject('cached-circle-float-count',lambda:t.circle_node(0,64.0))
reject('cached-analytic-float-q',lambda:t.analytic_error(3.0,12))
reject('cached-analytic-float-order',lambda:t.analytic_error(3,12.0))
for k in [-2,-1,2.0]:reject('bad-quadrature-order-'+str(k),lambda k=k:t.integrate(3,s,k))
reject('unsupported-conductor',lambda:t.integrate(7,s))
reject('float-conductor',lambda:t.integrate(3.0,s))
reject('nonrectangle-input',lambda:t.integrate(3,complex(.5,0)))
reject('real-domain-left',lambda:t.integrate(3,d.C(d.R(-d.S-1,-d.S),d.real(0))))
reject('real-domain-right',lambda:t.integrate(3,d.C(d.R(2*d.S,2*d.S+1),d.real(0))))
reject('imag-domain',lambda:t.integrate(3,d.C(d.real(0),d.real(F(3,2)))))
for args in [(-1,64),(64,64),(0,0)]:reject('bad-circle-'+str(args),lambda args=args:t.circle_node(*args))
for degree,steps in [(-1,180),(64,180),(1.0,180),(28,-1),(28,180.0)]:reject('bad-readout-order-'+str((degree,steps)),lambda degree=degree,steps=steps:t.readout([None]*64,64,degree,steps))
reject('empty-readout',lambda:t.readout([],0,0,0))
report={'passed':True,'negative_controls':len(cases),'cases':cases,'source_sha256':{n:hashlib.sha256((ROOT/'examples/analytic_oracle'/n).read_bytes()).hexdigest() for n in ['dyadic.py','theta_oracle.py']},'scope':'Domain/order/type guards including lru-cache cross-type aliases'}
out=ROOT/'outputs/checks/2026-11-04-validated-oracle/review';out.mkdir(parents=True,exist_ok=True);p=out/('guards-independent-'+str(time.time_ns())+'.json');p.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({'report':str(p),**report}))
