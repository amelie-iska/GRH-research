"""Executed half-density/Koopman bridges for constructed dynamical models.

The nonlinear triad is an energy-controlled finite reference, not measured flow.
The Cayley matrix is an exactly unitary finite discretization, not an assertion
that discretization error is zero. --gpu uses genuine cuStateVec on four qubits.
"""
from __future__ import annotations
import argparse,hashlib,json,math,sys
from pathlib import Path
import numpy as np

ROOT=Path(__file__).resolve().parents[1]
COEFFICIENTS=np.array([1.,-.5,-.5])
LAMBDAS=np.array([1.,2.,4.])
FORCING=np.array([.03,-.02,.05])
VISCOSITY=.13


def field(u,nu=VISCOSITY,forcing=FORCING):
    u=np.asarray(u,dtype=float);f=np.asarray(forcing,dtype=float)
    if u.shape!=(3,)or f.shape!=(3,)or not np.all(np.isfinite(u))or not np.all(np.isfinite(f))or not math.isfinite(nu)or nu<0:raise ValueError('Finite three-component state and nonnegative viscosity required')
    x,y,z=u;a,b,c=COEFFICIENTS
    return np.array([a*y*z,b*x*z,c*x*y])-nu*LAMBDAS*u+f


def jacobian(u,nu=VISCOSITY):
    x,y,z=np.asarray(u,dtype=float);a,b,c=COEFFICIENTS
    return np.array([[-nu*LAMBDAS[0],a*z,a*y],[b*z,-nu*LAMBDAS[1],b*x],[c*y,c*x,-nu*LAMBDAS[2]]])


def flow(u,time):
    from scipy.integrate import solve_ivp
    u=np.asarray(u,dtype=float)
    if u.shape!=(3,)or not np.all(np.isfinite(u))or np.linalg.norm(u)>20 or not math.isfinite(time)or abs(time)>2:raise ValueError('Bounded validation domain required')
    if time==0:return u.copy(),np.eye(3),0.
    def ode(t,v):
        x=v[:3];j=v[3:12].reshape(3,3)
        power=-VISCOSITY*np.dot(LAMBDAS*x,x)+np.dot(FORCING,x)
        return np.concatenate((field(x),(jacobian(x)@j).ravel(),[power]))
    initial=np.concatenate((u,np.eye(3).ravel(),[0.]))
    result=solve_ivp(ode,(0.,float(time)),initial,method='DOP853',rtol=1e-11,atol=1e-13)
    if not result.success or not np.all(np.isfinite(result.y[:,-1])):raise ValueError('ODE validation failed')
    final=result.y[:,-1];return final[:3],final[3:12].reshape(3,3),float(final[-1])


def cayley(side=16,dt=.1):
    if type(side)is not int or not 4<=side<=128 or not math.isfinite(dt)or abs(dt)>1:raise ValueError('Bounded periodic discretization required')
    x=np.arange(side)*2*math.pi/side;h=2*math.pi/side;D=np.zeros((side,side))
    for i in range(side):D[i,(i+1)%side]=1/(2*h);D[i,(i-1)%side]=-1/(2*h)
    B=np.diag(np.sin(x));A=(B@D+D@B)/2
    U=np.linalg.solve(np.eye(side)+dt*A/2,np.eye(side)-dt*A/2)
    return x,A,U


def cpu_report():
    from scipy.integrate import quad
    rng=np.random.default_rng(32027);rows=[]
    for u in rng.normal(size=(5,3)):
        for t in (-.5,.25,.75):
            end,J,work=flow(u,t);back,_,_=flow(end,-t);half,_,_=flow(u,t/2);composed,_,_=flow(half,t/2)
            det=np.linalg.det(J);exact=math.exp(-VISCOSITY*LAMBDAS.sum()*t)
            row=dict(initial=u.tolist(),time=t,final=end.tolist(),jacobian_determinant=float(det),exact_determinant=exact,determinant_error=abs(det-exact),inverse_error=float(np.linalg.norm(back-u)),composition_error=float(np.linalg.norm(composed-end)),energy_balance_error=abs(.5*np.dot(end,end)-.5*np.dot(u,u)-work))
            if max(row[k]for k in ['determinant_error','inverse_error','composition_error','energy_balance_error'])>2e-9:raise ValueError('Flow, Jacobian or energy certificate failed')
            rows.append(row)
    a=.3;t=1.2
    density=lambda x:math.exp(a*t)*math.exp(-math.exp(2*a*t)*x*x)/math.sqrt(math.pi)
    mass=quad(density,-np.inf,np.inf,epsabs=1e-12)[0]
    moment=quad(lambda x:x*x*density(x),-np.inf,np.inf,epsabs=1e-12)[0]
    naive=quad(lambda x:math.exp(-math.exp(2*a*t)*x*x)/math.sqrt(math.pi),-np.inf,np.inf,epsabs=1e-12)[0]
    if abs(mass-1)>1e-11 or abs(moment-.5*math.exp(-2*a*t))>1e-11:raise ValueError('Half-density normalization failed')
    x,A,_=cayley();H=-1j*A;lam,V=np.linalg.eigh(H);T=.5;exact=(V*np.exp(-1j*T*lam))@V.conj().T;refinement=[]
    for steps in (10,20,40):
        _,_,U=cayley(16,T/steps);evolution=np.linalg.matrix_power(U,steps)
        refinement.append(dict(steps=steps,dt=T/steps,error=float(np.linalg.norm(evolution-exact,2)),unitarity_error=float(np.linalg.norm(evolution.T@evolution-np.eye(16),2))))
    orders=[math.log(refinement[i]['error']/refinement[i+1]['error'],2)for i in range(2)]
    if not all(1.98<q<2.02 for q in orders):raise ValueError('Cayley time-refinement order failed')
    return dict(status='passed',triad=rows,gaussian=dict(rate=a,time=t,norm_squared=mass,second_moment=moment,exact_second_moment=.5*math.exp(-2*a*t),naive_pullback_norm_squared=naive,exact_naive_norm_squared=math.exp(-a*t)),cayley=dict(dimension=16,qubits=4,skew_residual=float(np.linalg.norm(A+A.T)),time=T,refinement=refinement,measured_orders=orders),scope='Constructed finite mathematical references and numerical convergence checks, separate from measured data. Continuous half-density unitarity is established by the written change-of-variables proof.')


def gpu_report():
    import cupy as cp
    from cuquantum import ComputeType,cudaDataType
    from cuquantum.bindings import custatevec as csv
    sys.path.insert(0,str(ROOT/'extension/quantum'))
    from gpu_experiments import environment
    x,_,_=cayley();states=[np.exp(-2*(x-math.pi)**2).astype(complex),np.exp(1j*x)*(1+.2*np.cos(2*x))]
    rows=[];handle=csv.create()
    try:
        for dt in (.01,.1,.3):
            _,_,U=cayley(16,dt);matrix=np.ascontiguousarray(U,dtype=np.complex128)
            for index,psi in enumerate(states):
                psi=psi/np.linalg.norm(psi);state=cp.asarray(psi,dtype=cp.complex128)
                size=csv.apply_matrix_get_workspace_size(handle,cudaDataType.CUDA_C_64F,4,matrix.ctypes.data,cudaDataType.CUDA_C_64F,csv.MatrixLayout.ROW,0,4,0,ComputeType.COMPUTE_64F)
                workspace=cp.cuda.alloc(size)if size else None
                csv.apply_matrix(handle,state.data.ptr,cudaDataType.CUDA_C_64F,4,matrix.ctypes.data,cudaDataType.CUDA_C_64F,csv.MatrixLayout.ROW,0,[0,1,2,3],4,[],[],0,ComputeType.COMPUTE_64F,0 if workspace is None else workspace.ptr,size)
                cp.cuda.runtime.deviceSynchronize();result=state.get();expected=matrix@psi;error=float(np.max(abs(result-expected)));norm=float(np.vdot(result,result).real)
                if error>2e-13 or abs(norm-1)>2e-13:raise ValueError('cuStateVec Cayley gate mismatch')
                rows.append(dict(dt=dt,input=index,amplitude_error=error,norm_squared=norm,workspace_bytes=size))
        return dict(status='passed',backend='NVIDIA cuStateVec complex128',qubits=4,rows=rows,environment=environment(),scope='Actual application of a dense four-qubit unitary matrix. This is a general-unitary backend check, not an efficient elementary-gate synthesis or hardware run.')
    finally:csv.destroy(handle)


def main():
    p=argparse.ArgumentParser();p.add_argument('--gpu',action='store_true');p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    result=dict(schema='grh.half-density-realization.v1',script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),result=gpu_report()if a.gpu else cpu_report())
    a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
