"""Actual completed Dirichlet-L readout experiments; not interval certificates.

The accompanying theorem is conditional on certified oracle/rounding bounds.
These high-precision diagnostic evaluations are labelled numerical throughout.
"""
from pathlib import Path
import argparse,math,json
import numpy as np
import mpmath as mp
from common import fresh,write_json,sha
mp.mp.dps=65
FAMILIES=[dict(q=3,a=1,chi=[0,1,-1]),dict(q=4,a=1,chi=[0,1,0,-1]),dict(q=5,a=0,chi=[0,1,-1,-1,1])]

def theta_completed(s,family,terms=12):
    q=family['q'];a=family['a'];s=mp.mpc(s);root=sum(family['chi'][n%q]*mp.exp(2j*mp.pi*n/q) for n in range(q))/(1j**a*mp.sqrt(q));result=0
    for n in range(1,terms+1):
        value=family['chi'][n%q]
        if not value:continue
        x=mp.pi*n*n/q;u=(s+a)/2;v=(1-s+a)/2
        result+=value*n**a*(mp.gammainc(u,x,mp.inf)/x**u+root*mp.gammainc(v,x,mp.inf)/x**v)
    return complex(result)

def size_bound(family,c,r,n0=13):
    d=math.pi/family['q'];a=family['a'];k=max(0,math.ceil((1+abs(c.real)+r+a)/2-1))
    Q=lambda x:sum(math.factorial(k)/math.factorial(k-j)/x**(j+1) for j in range(k+1));C=1 if a==0 else 1/math.sqrt(d*math.e)
    tail=C*Q(d*n0*n0)*math.exp(-d*n0*n0/2)/(1-math.exp(-d*n0));prefix=sum(n**a*math.exp(-d*n*n)*Q(d*n*n) for n in range(1,n0))
    return 2*(prefix+tail),2*tail

def main(out):
    out=fresh(out);result=[];center=.5+0j;rho=1.2;r=2.4;R=.7;m=64;eta=1e-12;theta=np.arange(m)*2*np.pi/m;z=rho*np.exp(1j*theta)
    for family in FAMILIES:
        y=np.array([theta_completed(center+x,family) for x in z]);M,tail=size_bound(family,center,r)
        direct=[]
        for s in [.37+.8j,1.7+.2j]:
            value=(family['q']/mp.pi)**((s+family['a'])/2)*mp.gamma((s+family['a'])/2)*mp.dirichlet(s,family['chi']);direct.append(abs(theta_completed(s,family)-complex(value)))
        assert max(direct)<1e-12
        test=R*np.exp(1j*np.linspace(0,2*np.pi,48,endpoint=False));truth=np.array([theta_completed(center+x,family) for x in test]);models=[]
        for degree in [4,8,12,20]:
            A=np.exp(1j*theta[:,None]*np.arange(degree+1));gram=A.conj().T@A/m;assert np.max(abs(gram-np.eye(degree+1)))<1e-13
            optimum=A.conj().T@y/m;b=np.zeros(degree+1,complex);history=[];alpha=.25;u=R/rho;v=R/r;w=(rho/r)**m
            oracle=eta*(1-u**(degree+1))/(1-u);alias=M*w/(1-w)*(1-v**(degree+1))/(1-v);trunc=M*v**(degree+1)/(1-v)
            for k in range(121):
                if k%4==0:
                    prediction=np.polynomial.polynomial.polyval(test/rho,b);observed=float(max(abs(prediction-truth)));optimization=(1-alpha)**k*np.linalg.norm(optimum)/math.sqrt(1-u*u);budget=float(optimization+oracle+alias+trunc)
                    assert observed<budget+3e-13
                    history.append(dict(step=k,observed_holdout_error=observed,conditional_uniform_budget=budget,optimization=float(optimization),oracle=oracle,alias=alias,Taylor=trunc,
                        coefficient_distance=float(np.linalg.norm(b-optimum))))
                if k<120:b-=alpha*(A.conj().T@(A@b-y)/m)
            models.append(dict(degree=degree,history=history,coefficients_real=b.real.tolist(),coefficients_imag=b.imag.tolist(),unwhitened_slowest_mode_rate=(rho/1.8)**(2*degree)))
        result.append(dict(**family,center=[center.real,center.imag],rho=rho,r=r,R=R,sample_count=m,M_r_bound=M,theta_truncation_bound=tail,
            assumed_sample_error=eta,direct_Hurwitz_crosscheck_max_error=max(direct),models=models,sample_target_real=y.real.tolist(),sample_target_imag=y.imag.tolist(),
            scope='Primitive nonprincipal Dirichlet completed functions; high-precision numerical diagnostic, not an interval-certified oracle or zero-location result'))
        print('primitive conductor',family['q'],'models',len(models),flush=True)
    write_json(out/'holomorphic-learning.json',dict(families=result,optimizer='Exact-feature complex last-layer gradient descent, step1/4,120 actual updates; zero initialization',
        guarantee='Theorem with certified evaluation and coefficient-arithmetic budgets; this demonstration uses unvalidated high precision and ordinary floating linear algebra',
        GRH_proved=False,all_conductor_uniformity=False,new_Lean_declarations=0))
    write_json(out/'manifest.json',dict(source_sha256=sha(__file__),files={p.name:dict(sha256=sha(p),bytes=p.stat().st_size) for p in out.iterdir() if p.is_file()}))
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);a=p.parse_args();main(a.output)
