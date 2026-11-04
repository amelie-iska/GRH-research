"""Independent finite analytic-bound and Gaussian-integral diagnostics."""
from pathlib import Path
import ast,json,math
import numpy as np
from scipy.integrate import quad
from scipy.special import erf

ROOT=Path(__file__).resolve().parents[3]

def main():
    rng=np.random.default_rng(20261104);R,rho,r=.7,1.2,1.8;N,m=5,9;gamma=1.3;eta=1e-4
    theta=2*np.pi*np.arange(m)/m;A=np.exp(1j*theta[:,None]*np.arange(N+1));F=lambda z:1/(1-z/2.4)
    errors=rng.normal(size=m)+1j*rng.normal(size=m);errors*=eta/np.maximum(abs(errors),1e-30)
    y=F(rho*np.exp(1j*theta))+errors;bopt=A.conj().T@y/m;b=rng.normal(size=N+1)+1j*rng.normal(size=N+1);initial=b.copy()
    M=1/(1-r/2.4);u,v,w=R/rho,R/r,(rho/r)**m;z=R*np.exp(2j*np.pi*np.arange(2048)/2048)
    rows=[]
    for k in range(16):
        observed=float(abs(np.polynomial.polynomial.polyval(z/rho,b)-F(z)).max())
        parts=[abs(1-gamma)**k*np.linalg.norm(initial-bopt)/np.sqrt(1-u*u),eta*(1-u**(N+1))/(1-u),M*w/(1-w)*(1-v**(N+1))/(1-v),M*v**(N+1)/(1-v)]
        assert observed<=sum(parts)+1e-12
        assert np.linalg.norm(b-bopt-(1-gamma)**k*(initial-bopt))<1e-12
        rows.append(dict(step=k,observed=observed,four_term_budget=float(sum(parts))))
        b-=gamma*(A.conj().T@(A@b-y)/m)
    r0=1.5;beta=.25;n=np.arange(512);lam=(rho/r0)**(2*n);error0=(r0/2.4)**n
    ratio=(r0/r)*(r0/rho)**(2*beta);B=M/np.sqrt(1-ratio**2);flow=[]
    for t in [.01,1.,100.,1e6]:
        norm=np.linalg.norm(np.exp(-lam*t)*error0);bound=B*(beta/(math.e*t))**beta
        assert norm<=bound;flow.append(dict(time=t,coefficient_error=float(norm),source_condition_bound=float(bound)))
    # Check the two Mellin-term tail majorants independently with direct quadrature.
    tails=[]
    for q,a in [(3,1),(4,1),(5,0)]:
        d=np.pi/q;k=2;Q=lambda x:sum(math.factorial(k)/math.factorial(k-j)/x**(j+1) for j in range(k+1))
        for n0 in [2,4]:
            actual=sum(n**a*quad(lambda t:t**k*np.exp(-d*n*n*t),1,np.inf,epsabs=1e-13)[0] for n in range(n0,20))
            C=1 if a==0 else 1/np.sqrt(d*math.e)
            bound=C*Q(d*n0*n0)*np.exp(-d*n0*n0/2)/(1-np.exp(-d*n0))
            assert actual<=bound+1e-13;tails.append(dict(q=q,a=a,n0=n0,direct_tail=actual,majorant=bound))
    # AST-load only the actual analytic integral function, with no image writes.
    p=ROOT/'examples/synthetic_training/electron_clouds.py';defs=[x for x in ast.parse(p.read_text()).body if isinstance(x,ast.FunctionDef) and x.name=='gaussian_integrals']
    ns=dict(np=np,erf=erf);exec(compile(ast.Module(body=defs,type_ignores=[]),str(p),'exec'),ns)
    centers=np.repeat([[-1.,0,0],[1.,0,0]],3,axis=0);alpha=np.tile([.3,1.2,4.8],2)
    S,L,H=ns['gaussian_integrals'](centers,alpha,centers[[0,3]],[1,1]);integral_error=0.
    # Integration by parts kinetic form and a separate Laplace Coulomb integral.
    nodes,weights=np.polynomial.hermite.hermgauss(3)
    for i,j in [(0,0),(0,3),(1,2),(2,5)]:
        a,b=alpha[i],alpha[j];p=a+b;mu=a*b/p;P=(a*centers[i]+b*centers[j])/p
        pref=(2*a/np.pi)**.75*(2*b/np.pi)**.75*np.exp(-mu*np.sum((centers[i]-centers[j])**2));kinetic=0.
        for ix,x in enumerate(nodes):
            for iy,y in enumerate(nodes):
                for iz,z in enumerate(nodes):
                    position=P+np.array([x,y,z])/np.sqrt(p)
                    kinetic+=weights[ix]*weights[iy]*weights[iz]*2*a*b*np.dot(position-centers[i],position-centers[j])
        kinetic*=pref/p**1.5;potential=0.
        for nucleus in centers[[0,3]]:
            distance=np.sum((P-nucleus)**2)
            potential-=quad(lambda u:2/np.sqrt(np.pi)*pref*(np.pi/(p+u*u))**1.5*np.exp(-p*u*u*distance/(p+u*u)),0,np.inf,epsabs=1e-12)[0]
        integral_error=max(integral_error,abs(kinetic+potential-H[i,j]))
    assert integral_error<1e-10 and abs(L@S@L-np.eye(6)).max()<1e-10
    # The displayed initial Lowdin coefficients indeed produce the first Gaussian.
    e,V=np.linalg.eigh(S);sqrtS=(V*np.sqrt(e))@V.T;C0=sqrtS[:,0];C0/=np.linalg.norm(C0)
    initial_error=float(abs(L@C0-np.eye(6)[:,0]).max());assert initial_error<1e-12
    result=dict(passed=True,finite_bound_diagnostics=rows,infinite_source_condition_diagnostics=flow,
        primitive_theta_tail_diagnostics=tails,Gaussian_integral_max_error=integral_error,
        Lowdin_overlap_error=float(abs(L@S@L-np.eye(6)).max()),initial_local_Gaussian_error=initial_error,
        scope='Ordinary NumPy/SciPy diagnostic computations, not interval certification or proof of GRH')
    out=ROOT/'outputs/checks/2026-11-04-synthetic-training/review';out.mkdir(parents=True,exist_ok=True)
    (out/'holomorphic-cloud-review.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if not isinstance(v,list)},indent=2))

if __name__=='__main__':main()
