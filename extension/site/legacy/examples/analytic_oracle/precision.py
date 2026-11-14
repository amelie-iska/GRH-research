"""Immutable variable-precision outward dyadic rectangles, standard library only.

Exact rational inputs. Each context carries its precision into interval
objects/caches; no mutable global precision or fixed transcendental tail.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from functools import lru_cache
import math
from pathlib import Path
SOURCE_AT_IMPORT=Path(__file__).read_bytes()

def ceildiv(a,b):return -((-a)//b)

def decimal_integer(value):
    """Exact decimal serialization without changing Python's global limits."""
    if type(value) is not int:raise TypeError('Integer required')
    if not value:return '0'
    sign='-' if value<0 else '';value=abs(value);chunks=[]
    while value:value,last=divmod(value,10**9);chunks.append(last)
    return sign+str(chunks[-1])+''.join(f'{n:09d}' for n in reversed(chunks[:-1]))

def parse_integer(text):
    """Inverse chunked decimal parser for exact serialized endpoints."""
    if type(text) is not str or not text:raise TypeError('Decimal string required')
    sign=-1 if text.startswith('-') else 1;digits=text[1:] if text[:1] in '+-' else text
    if not digits or any(c<'0' or c>'9' for c in digits):raise ValueError('Invalid decimal integer')
    value=0
    for start in range(0,len(digits),9):
        chunk=digits[start:start+9];value=value*10**len(chunk)+int(chunk)
    return sign*value

@dataclass(frozen=True,slots=True)
class Context:
    bits:int
    def __post_init__(self):
        if type(self.bits) is not int or self.bits<32:raise ValueError('Integer precision >=32 required')
    @property
    def scale(self):return 1<<self.bits
    @property
    def series_budget(self):return F(1,1<<(self.bits+16))
    def real(self,x):
        if isinstance(x,Real):
            if x.context!=self:raise TypeError('Mixed precision contexts')
            return x
        if type(x) is int:x=F(x)
        if not isinstance(x,F):raise TypeError('Exact int/Fraction input required')
        return Real(self,x.numerator*self.scale//x.denominator,ceildiv(x.numerator*self.scale,x.denominator))
    def bounds(self,a,b):
        if a>b:raise ValueError('Reversed endpoints')
        return Real(self,self.real(a).lo,self.real(b).hi)
    def complex(self,x=0,y=0):
        if isinstance(x,Complex):
            if (type(y) is not int and not isinstance(y,F)) or y!=0 or x.context!=self:raise TypeError('Mixed complex context or nonexact imaginary argument')
            return x
        return Complex(self.real(x),self.real(y))
    def atan(self,x):
        if not isinstance(x,F) or not 0<x<1:raise ValueError('Exact rational argument in(0,1) required')
        n=0;power=x;total=F()
        while True:
            term=power/F(2*n+1)
            if term<=self.series_budget:return self.bounds(min(total,total+(-1)**n*term),max(total,total+(-1)**n*term))
            total+=(-1)**n*term;power*=x*x;n+=1
    @lru_cache(maxsize=None,typed=True)
    def pi(self):return self.atan(F(1,5))*16-self.atan(F(1,239))*4
    def log_reduced(self,v):
        if not isinstance(v,F) or not 1<=v<=2:raise ValueError('Reduced logarithm argument in[1,2] required')
        z=(v-1)/(v+1);power=z;total=F();n=0
        while True:
            tail=2*power/(F(2*n+1)*(1-z*z))
            if tail<=self.series_budget:return self.bounds(total,total+tail)
            total+=2*power/F(2*n+1);power*=z*z;n+=1
    @lru_cache(maxsize=None,typed=True)
    def log(self,x):
        if not isinstance(x,F) or x<=0:raise ValueError('Positive exact rational logarithm argument required')
        k=0;v=x
        while v>=2:v/=2;k+=1
        while v<1:v*=2;k-=1
        return self.log_reduced(v)+k*self.log_reduced(F(2))
    def exp(self,z):
        z=self.complex(z);A=z.magnitude();k=0
        while A>F(1,2):A/=2;k+=1
        w=z/(1<<k);n=0
        while A**(n+1)/F(math.factorial(n+1))/(1-A/F(n+2))>self.series_budget:n+=1
        total=self.complex(1);term=total
        for j in range(1,n+1):term=term*w/j;total+=term
        tail=A**(n+1)/F(math.factorial(n+1))/(1-A/F(n+2))
        error=self.real(tail).hi
        total=Complex(Real(self,total.re.lo-error,total.re.hi+error),Real(self,total.im.lo-error,total.im.hi+error))
        for _ in range(k):total=total*total
        return total

@dataclass(frozen=True,slots=True)
class Real:
    context:Context
    lo:int
    hi:int
    def __post_init__(self):
        if not isinstance(self.context,Context) or type(self.lo) is not int or type(self.hi) is not int or self.lo>self.hi:raise ValueError('Invalid dyadic interval')
    def __add__(a,b):
        b=a.context.real(b);return Real(a.context,a.lo+b.lo,a.hi+b.hi)
    __radd__=__add__
    def __neg__(a):return Real(a.context,-a.hi,-a.lo)
    def __sub__(a,b):return a+-a.context.real(b)
    def __rsub__(a,b):return a.context.real(b)+-a
    def __mul__(a,b):
        b=a.context.real(b);v=[a.lo*b.lo,a.lo*b.hi,a.hi*b.lo,a.hi*b.hi];s=a.context.scale
        return Real(a.context,min(v)//s,ceildiv(max(v),s))
    __rmul__=__mul__
    def __truediv__(a,b):
        if type(b) is int:
            if not b:raise ZeroDivisionError()
            return Real(a.context,a.lo//b,ceildiv(a.hi,b)) if b>0 else -Real(a.context,a.lo//(-b),ceildiv(a.hi,-b))
        b=a.context.real(b)
        if b.lo<=0<=b.hi:raise ZeroDivisionError('Denominator interval contains zero')
        s=a.context.scale
        return a*Real(a.context,s*s//b.hi,ceildiv(s*s,b.lo))
    def __rtruediv__(a,b):return a.context.real(b)/a
    def magnitude(a):return F(max(abs(a.lo),abs(a.hi)),a.context.scale)
    def midpoint(a):return F(a.lo+a.hi,2*a.context.scale)
    def radius(a):return F(a.hi-a.lo,2*a.context.scale)
    def contains(a,x):
        if type(x) is int:x=F(x)
        if not isinstance(x,F):raise TypeError('Exact point required')
        return F(a.lo,a.context.scale)<=x<=F(a.hi,a.context.scale)
    def encode(a):return {'lo':decimal_integer(a.lo),'hi':decimal_integer(a.hi),'dyadic_bits':a.context.bits}

@dataclass(frozen=True,slots=True)
class Complex:
    re:Real
    im:Real
    def __post_init__(self):
        if not isinstance(self.re,Real) or not isinstance(self.im,Real) or self.re.context!=self.im.context:raise TypeError('Same-context real rectangles required')
    @property
    def context(self):return self.re.context
    def __add__(a,b):
        b=a.context.complex(b);return Complex(a.re+b.re,a.im+b.im)
    __radd__=__add__
    def __neg__(a):return Complex(-a.re,-a.im)
    def __sub__(a,b):return a+-a.context.complex(b)
    def __rsub__(a,b):return a.context.complex(b)+-a
    def __mul__(a,b):
        b=a.context.complex(b);return Complex(a.re*b.re-a.im*b.im,a.re*b.im+a.im*b.re)
    __rmul__=__mul__
    def __truediv__(a,b):
        if isinstance(b,Complex):raise TypeError('Complex reciprocal unsupported')
        return Complex(a.re/b,a.im/b)
    def magnitude(a):return a.re.magnitude()+a.im.magnitude()
    def radius(a):return a.re.radius()+a.im.radius()
    def midpoint(a):return a.re.midpoint(),a.im.midpoint()
    def encode(a):return {'real':a.re.encode(),'imag':a.im.encode()}
