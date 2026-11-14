"""Explicit integral-order, stochastic-channel and surface-spin realizations.

These constructions share typed algebraic data but retain their distinct scalar
rings, metrics and physical meanings. The finite spin gap is not a continuum
Yang--Mills gap; the quantum channel realizes probability diffusion, not every
Navier--Stokes velocity evolution.
"""
from __future__ import annotations
from fractions import Fraction as Q
import argparse,itertools,json,math
from pathlib import Path
import numpy as np
from quantum_surface import MODEL,DEFAULT,cpu_state,observable


def order_multiply(x,y,pi):
    if len(x)!=4 or len(y)!=4:raise ValueError('Four integral coordinates required')
    a,b,c,d=map(Q,x);e,f,g,h=map(Q,y);p=Q(pi)
    return (a*e+p*b*g,a*f+b*h,c*e+d*g,p*c*f+d*h)


def order_matrix(x,pi):
    a,b,c,d=map(Q,x);return [[a,b],[Q(pi)*c,d]]


def matrix_multiply(a,b):return [[sum(a[i][k]*b[k][j]for k in range(2))for j in range(2)]for i in range(2)]


def heat_transition(side=3,r=Q(1,8)):
    if type(side)is not int or not 3<=side<=8:raise ValueError('Side must be in [3,8]')
    r=Q(r)
    if not 0<=r<=Q(1,4):raise ValueError('Positive heat stencil requires r in [0,1/4]')
    n=side*side;p=[[Q(0)for _ in range(n)]for _ in range(n)]
    for y in range(side):
        for x in range(side):
            j=y*side+x;p[j][j]+=1-4*r
            for u,v in [((x+1)%side,y),((x-1)%side,y),(x,(y+1)%side),(x,(y-1)%side)]:p[v*side+u][j]+=r
    if any(sum(row)!=1 for row in p)or any(sum(p[i][j]for i in range(n))!=1 for j in range(n)):raise ValueError('Bistochastic identity failed')
    return p


def quantum_diffusion(p,rho):
    p=np.asarray(p,dtype=float);rho=np.asarray(rho,dtype=complex);n=len(p)
    if p.shape!=(n,n)or rho.shape!=(n,n)or not np.all(np.isfinite(p))or not np.all(np.isfinite(rho))or np.min(p)<0 or not np.allclose(p.sum(0),1,atol=1e-14):raise ValueError('Valid column-stochastic channel required')
    # Independent Kraus multiplication, not only the known diagonal formula.
    output=np.zeros_like(rho);completeness=np.zeros_like(rho)
    for i,j in zip(*np.nonzero(p)):
        k=np.zeros_like(rho);k[i,j]=math.sqrt(p[i,j]);output+=k@rho@k.conj().T;completeness+=k.conj().T@k
    return output,completeness


def torus_spectrum(model,Jx=Q(1),Jz=Q(1)):
    Jx,Jz=Q(Jx),Q(Jz)
    if model['id']!='torus3x3' or Jx<=0 or Jz<=0:raise ValueError('Declared checked torus and positive couplings required')
    v=len(model['x_checks']);f=len(model['z_checks']);n=model['n']
    # This formula applies after the connected closed surface rank/commutation
    # certificate, checked independently by topology tests and the source manifest.
    rows={}
    for a in range(0,v+1,2):
        for b in range(0,f+1,2):
            energy=-Jx*(v-2*a)-Jz*(f-2*b);multiplicity=4*math.comb(v,a)*math.comb(f,b)
            rows[energy]=rows.get(energy,0)+multiplicity
    energies=sorted(rows);ground=-Jx*v-Jz*f
    if sum(rows.values())!=2**n or energies[0]!=ground or energies[1]-ground!=4*min(Jx,Jz):raise ValueError('Spectral combinatorics failed')
    return dict(ground=str(ground),gap=str(energies[1]-ground),ground_degeneracy=rows[ground],dimension=2**n,levels=[dict(energy=str(e),multiplicity=rows[e])for e in energies])


def project_ground(model,state):
    indices=np.arange(state.size,dtype=np.uint32);v=state.copy()
    for c in model['x_checks']:
        mask=sum(1<<q for q in c['qubits']);v=(v+v[indices^mask])/2
    for c in model['z_checks']:
        sign=np.ones(state.size)
        for q in c['qubits']:sign*=1-2*((indices>>q)&1).astype(np.int8)
        v*=((1+sign)/2)
    return v


def report():
    e1=(1,0,0,0);u=(0,1,0,0);v=(0,0,1,0);e2=(0,0,0,1);order=[]
    for p in (2,3,5,7):
        uv=order_multiply(u,v,p);vu=order_multiply(v,u,p)
        order.append(dict(uniformizer=p,uv=list(map(str,uv)),vu=list(map(str,vu)),special_fiber_uv=[int(x)%p for x in uv],special_fiber_vu=[int(x)%p for x in vu],trace_pairing_determinant=-p*p))
    rng=np.random.default_rng(9401);P=heat_transition();n=len(P);psi=rng.normal(size=n)+1j*rng.normal(size=n);psi/=np.linalg.norm(psi);rho=np.outer(psi,psi.conj())
    output,comp=quantum_diffusion(P,rho);diagonal=np.diag(np.asarray(P,dtype=float)@np.real(np.diag(rho)))
    model=json.loads(MODEL.read_text());state=cpu_state(model,DEFAULT);projected=project_ground(model,state);pg=float(np.vdot(projected,projected).real)
    energy=-sum(observable(state,c['qubits'],'X')for c in model['x_checks'])-sum(observable(state,c['qubits'],'Z')for c in model['z_checks'])
    error=float(np.linalg.norm(output-diagonal));completeness=float(np.linalg.norm(comp-np.eye(n)))
    if error>1e-14 or completeness>1e-14 or energy+18+1e-12<4*(1-pg):raise ValueError('Realization check failed')
    return dict(schema='grh.realization-bridges.v1',integral_order=order,
        quantum_heat=dict(dimension=n,stencil='r=1/8 on periodic 3x3 grid',kraus_completeness_error=completeness,diagonal_transport_error=error,trace=float(np.trace(output).real),minimum_eigenvalue=float(np.linalg.eigvalsh(output).min()),scope='CPTP realization of finite probability diffusion; coherent off-diagonal inputs are dephased.'),
        surface_spectrum=torus_spectrum(model),
        energy_certificate=dict(energy=energy,ground_energy=-18,gap=4,ground_space_probability=pg,excess_energy=energy+18,gap_lower_bound=4*(1-pg),slack=energy+18-4*(1-pg)),
        scope='Exact finite algebra/spectrum and independent numerical channel/state checks. Scalar specialization and physical interpretation are explicit.')

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path);a=p.parse_args();r=report();text=json.dumps(r,indent=2)
    if a.output:a.output.write_text(text+'\n')
    print(text)
