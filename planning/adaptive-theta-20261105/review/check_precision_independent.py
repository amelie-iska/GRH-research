"""Independent exact reconstruction and negative controls; no external packages."""
from pathlib import Path
from fractions import Fraction as F
import sys,json,hashlib,itertools,math,time
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'examples/analytic_oracle'))
import precision as p
OUT=ROOT/'outputs/checks/2026-11-05-adaptive-theta/review'
source=Path(p.__file__).read_bytes();checks=0;failures=[];widths=[]
def check(ok,label):
 global checks
 checks+=1
 if not ok:failures.append(label)
def rejects(fn,label):
 try:fn()
 except (ValueError,TypeError,ZeroDivisionError):check(True,label)
 else:check(False,label)
def ends(x):return [F(x.lo,x.context.scale),F(x.hi,x.context.scale)]
def subset(box,lo,hi):return ends(box)[0]<=lo<=hi<=ends(box)[1]
def atan_bracket(x,bits):
 total=F();n=0
 while True:
  term=x**(2*n+1)/F(2*n+1)
  if term<F(1,1<<(bits+40)):
   return min(total,total+(-1)**n*term),max(total,total+(-1)**n*term)
  total+=(-1)**n*term;n+=1
def log_bracket(x,bits):
 k=0
 while x>=2:x/=2;k+=1
 while x<1:x*=2;k-=1
 def reduced(v):
  z=(v-1)/(v+1);n=0;total=F()
  while True:
   tail=2*z**(2*n+1)/(F(2*n+1)*(1-z*z))
   if tail<F(1,1<<(bits+40)):return total,total+tail
   total+=2*z**(2*n+1)/F(2*n+1);n+=1
 a,b=reduced(x);u,v=reduced(F(2))
 return (a+k*u,b+k*v) if k>=0 else (a+k*v,b+k*u)
def mul(x,y):return x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0]
def exp_bracket(x,y,bits):
 # Direct Taylor at the original rational point, independently of producer scaling.
 A=abs(x)+abs(y);term=(F(1),F());total=term;n=0
 while True:
  if n+2>A:
   tail=A**(n+1)/F(math.factorial(n+1))/(1-A/F(n+2))
   if tail<F(1,1<<(bits+40)):return [(v-tail,v+tail) for v in total]
  n+=1;term=tuple(v/n for v in mul(term,(x,y)));total=tuple(a+b for a,b in zip(total,term))
for bits in [32,80,160,320]:
 c=p.Context(bits);widths.append(c.pi().radius())
 for lo,hi in [(-7,-3),(-3,2),(0,0),(1,9),(-1,1)]:
  for den in [1,3,11]:
   a=c.bounds(F(lo,den),F(hi,den))
   for bl,bh in [(-8,-2),(-2,5),(2,7)]:
    b=c.bounds(F(bl,7),F(bh,7))
    for x,y in itertools.product(ends(a),ends(b)):
     for op,name in [(lambda:a+b,'add'),(lambda:a-b,'subtract'),(lambda:a*b,'multiply')]:
      exact={'add':x+y,'subtract':x-y,'multiply':x*y}[name];check(op().contains(exact),f'{bits} {name} corner')
     if not b.lo<=0<=b.hi:check((a/b).contains(x/y),f'{bits} divide corner')
   for divisor in [-5,-1,1,3]:
    for x in ends(a):check((a/divisor).contains(x/divisor),f'{bits} signed integer division')
 check(c.real(F(-1,2*c.scale))==p.Real(c,-1,0),f'{bits} negative half-ulp')
 for x in [F(1,5),F(1,239),F(3,4)]:
  lo,hi=atan_bracket(x,bits);check(subset(c.atan(x),lo,hi),f'{bits} independent atan bracket {x}')
 lo1,hi1=atan_bracket(F(1,5),bits);lo2,hi2=atan_bracket(F(1,239),bits)
 check(subset(c.pi(),16*lo1-4*hi2,16*hi1-4*lo2),f'{bits} independent Machin bracket')
 for x in [F(1,1024),F(1,2),F(3,5),F(1),F(9,8),F(2),F(15,4),F(124),F(1024)]:
  lo,hi=log_bracket(x,bits);check(subset(c.log(x),lo,hi),f'{bits} independent log bracket {x}')
  z=c.exp(c.complex(c.log(x)));check(z.re.contains(x) and z.im.contains(0),f'{bits} exp-log exact identity {x}')
 for x,y in [(F(),F()),(F(1),F()),(F(-3),F()),(F(3,7),F(-9,4)),(F(),F(7)),(F(-17,3),F(13,7)),(F(1,2),F(1,1<<bits))]:
  box=c.exp(c.complex(x,y));brackets=exp_bracket(x,y,bits)
  check(subset(box.re,*brackets[0]) and subset(box.im,*brackets[1]),f'{bits} independent direct exp bracket {x}+i{y}')
 z=c.exp(c.complex(0,c.pi()));check(z.re.contains(-1) and z.im.contains(0),f'{bits} Euler identity')
 for bad in [0.0,1.0,.1,True,False,complex(1,2)]:
  for fn,name in [(lambda:c.real(bad),'real'),(lambda:c.complex(bad),'complex'),(lambda:c.real(1)+bad,'add'),(lambda:c.real(1)/bad,'divide')]:rejects(fn,f'{bits} reject {name} {bad!r}')
  c.log(F(1));rejects(lambda:c.log(bad),f'{bits} log typed-cache {bad!r}')
 for bad in [0.0,False,True]:rejects(lambda:c.complex(c.complex(1),bad),f'{bits} reused complex imaginary {bad!r}')
 for fn,label in [(lambda:c.real(1)+p.Context(bits+1).real(2),'mixed real'),(lambda:c.complex(1)+p.Context(bits+1).complex(2),'mixed complex'),(lambda:c.real(1)/c.bounds(-1,1),'zero reciprocal'),(lambda:p.Complex(c.real(1),p.Context(bits+1).real(2)),'mixed constructor')]:rejects(fn,f'{bits} {label}')
for bad in [True,False,0,31,32.0,64.0]:rejects(lambda:p.Context(bad),f'context rejects {bad!r}')
check(all(a>b for a,b in zip(widths,widths[1:])),'Machin widths strictly refine')
for value in [0,1,-1,10**8,10**9,10**9+1,(1<<15000)+12345,-((1<<15000)+12345)]:
 text=p.decimal_integer(value);magnitude=abs(value);digits=[]
 while magnitude:magnitude,digit=divmod(magnitude,10);digits.append(str(digit))
 independent=('-' if value<0 else '')+(''.join(reversed(digits)) if digits else '0')
 check(text==independent,'chunked decimal equals independent digit-wise encoding')
 check(p.parse_integer(text)==value,'chunked decimal roundtrip')
for bad in [True,False,1.0,F(1)]:rejects(lambda:p.decimal_integer(bad),'decimal rejects noninteger')
for bad in ['',True,123,'--1','+','1.0','１','1 2']:rejects(lambda:p.parse_integer(bad),'decimal parser lexical guards')
check(source==Path(p.__file__).read_bytes(),'source stable during check')
report={'passed':not failures,'checks':checks,'failures':failures,'precision_source_sha256':hashlib.sha256(source).hexdigest(),'bits':[32,80,160,320],'independent_exact_brackets':True,'mpmath_used':False}
out=OUT/('precision-independent-'+str(time.time_ns())+'.json');out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({'report':str(out),**report}))
if failures:raise SystemExit(1)
