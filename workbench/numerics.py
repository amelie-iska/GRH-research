"""Finite-size diagnostics, not continuum or physical-topology certificates."""
from __future__ import annotations
import argparse,json,math
from fractions import Fraction
from pathlib import Path


def heat_mode(n:int,nu:float,t:float,steps:int|None=None,kx:int=1,ky:int=1)->dict:
    if type(n)is not int or n<4 or n>4096 or not all(math.isfinite(v) for v in (nu,t)) or nu<=0 or t<=0:
        raise ValueError('Positive finite physical parameters and bounded grid required')
    if any(type(k)is not int or abs(k)*2>=n for k in (kx,ky)):raise ValueError('Modes must be below Nyquist')
    h=2*math.pi/n;lam=-4*(math.sin(kx*h/2)**2+math.sin(ky*h/2)**2)/h**2
    continuum=math.exp(-nu*(kx*kx+ky*ky)*t);semi=math.exp(nu*lam*t)
    result=dict(n=n,h=h,domain_side=2*math.pi,time=t,nu=nu,mode=[kx,ky],continuum_amplitude=continuum,semidiscrete_amplitude=semi,spatial_error=abs(semi-continuum),semidiscrete_eigenvalue=lam)
    if steps is not None:
        if type(steps)is not int or not 1<=steps<=10**7:raise ValueError('Invalid step budget')
        dt=t/steps;r=nu*dt/h**2
        if r>.25:raise ValueError('Nonpositive heat stencil outside r <= 1/4')
        factor=1+nu*lam*dt;discrete=factor**steps
        result.update(steps=steps,dt=dt,r=r,discrete_amplitude=discrete,temporal_error=abs(discrete-semi),total_error=abs(discrete-continuum),signed_total_error=discrete-continuum)
    return result


def refinement()->dict:
    nu=.08;t=1.5
    spatial=[heat_mode(n,nu,t) for n in (16,32,64)]
    temporal=[heat_mode(32,nu,t,steps) for steps in (100,200,400)]
    coupled=[heat_mode(n,nu,t,max(1,math.ceil(t*nu/(.1*(2*math.pi/n)**2)))) for n in (16,32,64)]
    def orders(rows,key):return [math.log(rows[i][key]/rows[i+1][key],2) for i in range(len(rows)-1)]
    return dict(spatial=spatial,spatial_orders=orders(spatial,'spatial_error'),temporal=temporal,temporal_orders=orders(temporal,'temporal_error'),coupled=coupled,scope='Analytic Fourier-mode diagnostic for periodic heat, applicable to the diffusion amplitude in Taylor-Green. Richardson orders are measured diagnostics, not universal bounds for nonlinear fluids. Spatial and temporal errors may cancel.')


def flux(q:int,n:int)->dict:
    if type(q)is not int or type(n)is not int or not 2<=n<=4096:raise ValueError('Integer flux/grid required')
    theta=2*math.pi*q/(n*n);principal=math.atan2(math.sin(theta),math.cos(theta))
    total=n*n*principal/(2*math.pi)
    return dict(n=n,flux_sector=q,plaquette_angle=theta,principal_angle=principal,inferred_flux=total,branch_margin=math.pi-abs(theta),admissible=abs(theta)<math.pi,alias_error=total-q,
                scope='Uniform periodic U(1) plaquette-holonomy toy sector. A strict branch margin is needed for this reconstruction; no continuum gauge-field or mass-gap theorem.')


def rank(rows,p=None):
    if not rows or any(len(row)!=len(rows[0]) for row in rows):raise ValueError('Nonempty rectangular matrix required')
    if any(type(v)is not int for row in rows for v in row):raise ValueError('Exact integer entries required')
    if p is not None and (type(p)is not int or p<2 or any(p%d==0 for d in range(2,math.isqrt(p)+1))):raise ValueError('Prime modulus required')
    a=[[Fraction(v) if p is None else v%p for v in row] for row in rows];r=0
    for j in range(len(a[0])):
        i=next((i for i in range(r,len(a)) if a[i][j]),None)
        if i is None:continue
        a[r],a[i]=a[i],a[r];inv=1/a[r][j] if p is None else pow(a[r][j],-1,p)
        a[r]=[v*inv if p is None else v*inv%p for v in a[r]]
        for i in range(len(a)):
            if i!=r:
                c=a[i][j];a[i]=[x-c*y if p is None else (x-c*y)%p for x,y in zip(a[i],a[r])]
        r+=1
        if r==len(a):break
    return r


def report():
    return dict(schema='grh.finite-size.v1',heat=refinement(),gauge=[flux(3,n) for n in (2,4,8,16)],rank_counterexample=dict(matrix=[[1,0],[0,2]],rational_rank=rank([[1,0],[0,2]]),mod2_rank=rank([[1,0],[0,2]],2)),limitations=['No finite-volume extrapolation was inferred from fixed-domain refinement.','The numerical lab does not establish topological identification of measured fields.','Finite-field rank can drop at bad primes; it is not interchangeable with rational or real rank.'])

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path);a=p.parse_args();text=json.dumps(report(),indent=2)
    if a.output:a.output.write_text(text+'\n')
    else:print(text)
