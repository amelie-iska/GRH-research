"""Exact rational growth/alias/Taylor certificates, not a full sample oracle.

For primitive nonprincipal Dirichlet targets, use the proved theta bound,
pi>3, and exp(-x) <= (1+x/L)^(-L). No floating constants enter certificates.
"""
from fractions import Fraction as F
from pathlib import Path
import argparse,json,math,hashlib

def exponential_upper(x,L=16):
    assert isinstance(x,F) and x>0 and isinstance(L,int) and L>0
    return (1+x/L)**(-L)

def Q(k,x):
    return sum((F(math.factorial(k),math.factorial(k-j))/x**(j+1) for j in range(k+1)),F(0))

def growth(q,a,n0=8,L=16):
    assert type(q) is int and q>=3 and type(a) is int and a in (0,1) and type(n0) is int and n0>=1
    c=F(1,2);r=F(12,5);d=F(3,q)
    k=max(0,math.ceil((1+abs(c)+r+a)/2-1))
    C=F(1) if a==0 else (1+1/d)/2
    prefix=sum((n**a*exponential_upper(d*n*n,L)*Q(k,d*n*n) for n in range(1,n0)),F(0))
    tail=C*Q(k,d*n0*n0)*exponential_upper(d*n0*n0/2,L)/(1-exponential_upper(d*n0,L))
    return 2*(prefix+tail),dict(d_lower=d,k=k,n0=n0,L=L,prefix=prefix,one_integral_tail=tail,C=C)

def rational(x):return {'numerator':str(x.numerator),'denominator':str(x.denominator),'display_float_not_certificate':float(x)}

def main(output):
    assert not output.exists(),'Preserve prior certificates; choose a fresh output directory'
    output.mkdir(parents=True);records=[]
    R,rho,r=F(7,10),F(6,5),F(12,5);u=R/rho;v=R/r;m=64;w=(rho/r)**m
    for q,a in [(3,1),(4,1),(5,0)]:
        M,parts=growth(q,a);models=[]
        for N in [4,8,12,20]:
            oracle=F(1,10**12)*(1-u**(N+1))/(1-u)
            alias=M*w/(1-w)*(1-v**(N+1))/(1-v)
            taylor=M*v**(N+1)/(1-v)
            models.append(dict(degree=N,oracle_assuming_eta_1e_minus12=rational(oracle),alias=rational(alias),Taylor=rational(taylor)))
        records.append(dict(conductor=q,parity=a,M_r=rational(M),integer_growth_bound=math.ceil(M),construction={k:rational(x) if isinstance(x,F) else x for k,x in parts.items()},models=models))
    source=Path(__file__).read_bytes();(output/'generation_source.py').write_bytes(source)
    result=dict(source_sha256=hashlib.sha256(source).hexdigest(),records=records,center={'real':rational(F(1,2)),'imag':rational(F(0))},target='Completed Lambda(s,chi)=(q/pi)^((s+a)/2) Gamma((s+a)/2) L(s,chi)',radii={'R':rational(R),'rho':rational(rho),'r':rational(r)},sample_count=m,
        assumptions=['Primitive nonprincipal Dirichlet theta/Mellin identity','pi>3','Certified sample eta and coefficient rounding are separate obligations'],
        size_and_tail_constants_exact_rational=True,full_sample_oracle_certified=False,new_Lean_declarations=0,GRH_proved=False)
    (output/'rational-constants.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'certified_growth_bounds':{str(x['conductor']):x['M_r']['display_float_not_certificate'] for x in records},'full_sample_oracle_certified':False,'GRH_proved':False}))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);main(p.parse_args().output)
