"""Independent complete-ideal/direct-pair checker; stdlib only, no accepted-checker imports."""
from pathlib import Path
from itertools import product
from math import isqrt
from functools import lru_cache
import json,hashlib
PH=((1,0),(1,1),(0,1),(-1,0),(-1,-1),(0,-1))
ZERO=(0,0)
def add(x,y):return x[0]+y[0],x[1]+y[1]
def mul(x,y):return x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0]-x[1]*y[1]
def conj(z):return z[0]-z[1],-z[1]
def norm(z):return z[0]*z[0]-z[0]*z[1]+z[1]*z[1]
def scale(z,k):return z[0]*k,z[1]*k
def quotient(z,w):
 a,b=mul(z,conj(w));n=norm(w)
 return (a//n,b//n)if a%n==b%n==0 else None
def prime(n):return n>=2 and all(n%d for d in range(2,isqrt(n)+1))
def primary(cap):
 bound=isqrt(4*cap//3)+1
 return sorted(((a,b)for a in range(-bound,bound+1)for b in range(-bound,bound+1)if a%3==1 and b%3==0 and 0<norm((a,b))<=cap and norm((a,b))%2 and norm((a,b))%3),key=lambda g:(norm(g),g))
def divisors(fs):
 out=[]
 for bits in product((0,1),repeat=len(fs)):
  ds=tuple(p for p,b in zip(fs,bits)if b);g=(1,0)
  for p in ds:g=mul(g,p)
  out.append((g,frozenset(ds),(-1)**len(ds)))
 return out
def local_phase(pi,u):
 Q=norm(pi);inert=pi[1]==0;p=abs(pi[0])if inert else Q
 root=None if inert else (-pi[0]*pow(pi[1],-1,p))%p
 def embed(z):return(z[0]%p,z[1]%p)if inert else((z[0]+z[1]*root)%p,0)
 def times(x,y):return embed(mul(x,y))
 x=embed(u)
 if x==ZERO:return None
 n=(Q-1)//6;v=(1,0)
 while n:
  if n%2:v=times(v,x)
  x=times(x,x);n//=2
 roots={embed(z):i for i,z in enumerate(PH)};assert len(roots)==6
 return roots[v]
def raw(fs,u):
 es=[local_phase(p,u)for p in fs]
 return ZERO if None in es else PH[sum(es)%6]
def original_coefficients(fs,U):
 ds=divisors(fs);A=C=0
 for a,fa,ma in ds:
  for b,fb,mb in ds:
   if fa&fb:continue
   if norm(a)<=U and norm(b)<=U:A+=ma*mb
   if norm(a)>U and norm(b)>U:C+=ma*mb
 mu=(-1)**len(fs);assert A==C-mu
 return(A,C,mu)
