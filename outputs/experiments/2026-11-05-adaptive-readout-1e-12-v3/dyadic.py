"""Outward fixed-dyadic rectangle arithmetic. No binary floating input accepted."""
from fractions import Fraction as F
from dataclasses import dataclass
from functools import lru_cache
BITS=224
S=1<<BITS

def ceildiv(a,b):return -((-a)//b)
@dataclass(frozen=True,slots=True)
class R:
 lo:int
 hi:int
 def __post_init__(self):
  if type(self.lo) is not int or type(self.hi) is not int or self.lo>self.hi:raise ValueError('Invalid dyadic interval')
 @staticmethod
 def frac(x):
  if type(x) is int:x=F(x)
  if not isinstance(x,F):raise TypeError('Exact integer or Fraction input required')
  return R(x.numerator*S//x.denominator,ceildiv(x.numerator*S,x.denominator))
 @staticmethod
 def bounds(a,b):
  if a>b:raise ValueError('Reversed bounds')
  return R(R.frac(a).lo,R.frac(b).hi)
 def __add__(a,b):
  b=real(b);return R(a.lo+b.lo,a.hi+b.hi)
 __radd__=__add__
 def __neg__(a):return R(-a.hi,-a.lo)
 def __sub__(a,b):return a+-real(b)
 def __rsub__(a,b):return real(b)+-a
 def __mul__(a,b):
  b=real(b);v=[a.lo*b.lo,a.lo*b.hi,a.hi*b.lo,a.hi*b.hi];return R(min(v)//S,ceildiv(max(v),S))
 __rmul__=__mul__
 def __truediv__(a,b):
  if type(b) is int:
   if not b:raise ZeroDivisionError()
   return R(a.lo//b,ceildiv(a.hi,b)) if b>0 else -R(a.lo//(-b),ceildiv(a.hi,-b))
  b=real(b)
  if b.lo<=0<=b.hi:raise ZeroDivisionError('Denominator contains zero')
  return a*R((S*S)//b.hi,ceildiv(S*S,b.lo))
 def __rtruediv__(a,b):return real(b)/a
 def magnitude(a):return F(max(abs(a.lo),abs(a.hi)),S)
 def midpoint(a):return F(a.lo+a.hi,2*S)
 def radius(a):return F(a.hi-a.lo,2*S)
 def contains(a,x):
  x=F(x);return F(a.lo,S)<=x<=F(a.hi,S)
 def encode(a):return dict(lo=str(a.lo),hi=str(a.hi),dyadic_bits=BITS)

def real(x):return x if isinstance(x,R) else R.frac(x)
@dataclass(frozen=True,slots=True)
class C:
 re:R
 im:R
 def __post_init__(self):
  if not isinstance(self.re,R) or not isinstance(self.im,R):raise TypeError('Real intervals required')
 def __add__(a,b):
  b=complex_box(b);return C(a.re+b.re,a.im+b.im)
 __radd__=__add__
 def __neg__(a):return C(-a.re,-a.im)
 def __sub__(a,b):return a+-complex_box(b)
 def __rsub__(a,b):return complex_box(b)+-a
 def __mul__(a,b):
  b=complex_box(b);return C(a.re*b.re-a.im*b.im,a.re*b.im+a.im*b.re)
 __rmul__=__mul__
 def __truediv__(a,b):
  if isinstance(b,C):raise TypeError('Complex reciprocal not needed or implemented')
  return C(a.re/b,a.im/b)
 def magnitude(a):return a.re.magnitude()+a.im.magnitude()
 def radius(a):return a.re.radius()+a.im.radius()
 def midpoint(a):return C(real(a.re.midpoint()),real(a.im.midpoint()))
 def encode(a):return dict(real=a.re.encode(),imag=a.im.encode())

def complex_box(x):return x if isinstance(x,C) else C(real(x),real(0))

def atan_fraction(x,N):
 if not isinstance(x,F) or not 0<x<1 or type(N) is not int or N<1:raise ValueError('Invalid alternating-series parameters')
 total=sum(((-1)**j*x**(2*j+1)/F(2*j+1) for j in range(N)),F())
 nxt=total+(-1)**N*x**(2*N+1)/F(2*N+1)
 return R.bounds(min(total,nxt),max(total,nxt))

@lru_cache(maxsize=None,typed=True)
def pi():
 p=16*atan_fraction(F(1,5),60)-4*atan_fraction(F(1,239),60)
 assert p.lo>3*S and p.hi<F(22,7)*S
 return p

def log_series(x,N=92):
 if not isinstance(x,F) or not 1<=x<=2:raise ValueError('Log series requires x in[1,2]')
 z=(x-1)/(x+1);total=2*sum((z**(2*j+1)/F(2*j+1) for j in range(N)),F())
 tail=2*z**(2*N+1)/(F(2*N+1)*(1-z*z))
 return R.bounds(total,total+tail)

@lru_cache(maxsize=None,typed=True)
def log_fraction(x):
 if not isinstance(x,F) or x<=0:raise ValueError('Positive exact Fraction required')
 k=0;v=x
 while v>=2:v/=2;k+=1
 while v<1:v*=2;k-=1
 return log_series(v)+k*log_series(F(2))

def exp_box(z):
 z=complex_box(z);A=z.magnitude();k=0
 while A>F(1,2):A/=2;k+=1
 w=z/(1<<k);term=complex_box(1);total=term;N=60
 for j in range(1,N+1):term=term*w/j;total=total+term
 tail=A**(N+1)/__import__('math').factorial(N+1)/(1-A/F(N+2))
 error=real(tail);total=C(R(total.re.lo-error.hi,total.re.hi+error.hi),R(total.im.lo-error.hi,total.im.hi+error.hi))
 for _ in range(k):total=total*total
 return total
