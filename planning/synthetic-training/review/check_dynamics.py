"""Electronic/BdG review using independent explicit fermionic Fock evolution."""
import ast,json,math
from pathlib import Path
import numpy as np
from scipy.linalg import expm

ROOT=Path(__file__).resolve().parents[3]

def ann(n,i):
    out=np.zeros((2**n,2**n),complex)
    for b in range(2**n):
        if b>>i&1:out[b^(1<<i),b]=(-1)**((b&((1<<i)-1)).bit_count())
    return out

def main():
    # Load only the two pure NumPy functions: local PyArrow/RDKit are absent.
    source=ROOT/'examples/synthetic_training/dynamics.py'
    tree=ast.parse(source.read_text());selected=[n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name in ['electronic','hubbard']]
    ns=dict(np=np,math=math);exec(compile(ast.Module(body=selected,type_ignores=[]),str(source),'exec'),ns)
    electronic,hubbard=ns['electronic'],ns['hubbard']
    n=4;cs=[ann(n,i) for i in range(n)];cd=[c.conj().T for c in cs]
    number=[cd[i]@cs[i] for i in range(n)]
    rng=np.random.default_rng(20261104)
    h=np.diag([-.7,.3,-.2,.8]).astype(complex)
    for i in range(n-1):h[i,i+1]=-.6+.1j*(i+1);h[i+1,i]=h[i,i+1].conjugate()
    pair=rng.normal(size=(n,n))*.13+1j*rng.normal(size=(n,n))*.08;pair=pair-pair.T
    rows=[]
    for bdg in [False,True]:
        Delta=pair if bdg else np.zeros_like(pair)
        H=np.block([[h,Delta],[Delta.conj().T,-h.T]]) if bdg else h
        record=electronic(H,bdg)
        initial=h+np.diag([.7]+[0.]*(n-2)+[-.3]);_,v=np.linalg.eigh(initial)
        state=np.zeros(2**n,complex);state[0]=1
        for k in range(n//2):state=sum(v[i,k]*cd[i] for i in range(n))@state
        assert abs(np.linalg.norm(state)-1)<1e-12
        Fock=sum(h[i,j]*(cd[i]@cs[j]) for i in range(n) for j in range(n))
        Fock+=.5*sum(Delta[i,j]*(cd[i]@cd[j])+Delta[i,j].conjugate()*(cs[j]@cs[i]) for i in range(n) for j in range(n))
        es,W=np.linalg.eigh(Fock);coefficient=W.conj().T@state
        occerr=currenterr=coverr=sourceerr=0.
        for k,t in enumerate(record['time']):
            psi=W@(np.exp(-1j*es*t)*coefficient)
            P=np.array([[np.vdot(psi,cd[j]@cs[i]@psi) for j in range(n)] for i in range(n)])
            F=np.array([[np.vdot(psi,cs[i]@cs[j]@psi) for j in range(n)] for i in range(n)])
            occupations=np.array([np.vdot(psi,ni@psi).real for ni in number])
            occerr=max(occerr,float(abs(occupations-record['occupation'][k]).max()))
            covariance=np.array([np.vdot(psi,number[0]@nj@psi).real-occupations[0]*occupations[j] for j,nj in enumerate(number)])
            coverr=max(coverr,float(abs(covariance-record['connected_density_correlation_with_orbital0'][k]).max()))
            current=[-2*np.imag(h[i,j]*P[j,i]) for i,j in record['bond_edges']]
            currenterr=max(currenterr,float(abs(np.array(current)-record['bond_current'][k]).max()))
            independent_source=-2*np.imag(np.diag(Delta@F.conj().T))
            sourceerr=max(sourceerr,float(abs(independent_source-record['pair_source'][k]).max()))
        assert max(occerr,currenterr,coverr,sourceerr)<1e-11
        rows.append(dict(bdg=bdg,max_occupation_error=occerr,max_bond_current_error=currenterr,
            max_connected_correlation_error=coverr,max_independent_pair_source_error=sourceerr))
    dimer=[]
    for ratio,t in [(2,.7),(8,1.),(16,1.)]:
        result=hubbard(ratio,t);indices=[b for b in range(16) if b.bit_count()==2]
        # Full 16-state construction independently restricts to its N=2 block.
        H=-t*(cd[0]@cs[2]+cd[2]@cs[0]+cd[1]@cs[3]+cd[3]@cs[1])
        H+=ratio*t*(number[0]@number[1]+number[2]@number[3])
        sub=H[np.ix_(indices,indices)];assert abs(sub-np.array(result['hamiltonian_real'])).max()<1e-12
        es,V=np.linalg.eigh(H);state=np.zeros(16,complex);state[9]=1;coeff=V.conj().T@state
        occerr=currenterr=coverr=swaperr=0.
        J=[-1j*t*(cd[i]@cs[j]-cd[j]@cs[i]) for i,j in [(0,2),(1,3)]]
        for k,time in enumerate(result['time']):
            psi=V@(np.exp(-1j*es*time)*coeff);occ=np.array([np.vdot(psi,ni@psi).real for ni in number])
            cov=np.array([np.vdot(psi,number[0]@nj@psi).real-occ[0]*occ[j] for j,nj in enumerate(number)])
            current=np.array([np.vdot(psi,op@psi).real for op in J])
            occerr=max(occerr,float(abs(occ-result['occupation'][k]).max()))
            currenterr=max(currenterr,float(abs(current-result['bond_current'][k]).max()))
            coverr=max(coverr,float(abs(cov-result['connected_density_correlation_with_orbital0'][k]).max()))
            swaperr=max(swaperr,abs(float(abs(psi[6])**2)-result['spin_swap_probability'][k]))
        assert max(occerr,currenterr,coverr,swaperr)<1e-10
        dimer.append(dict(U_over_t=ratio,t=t,max_occupation_error=occerr,max_current_error=currenterr,
            max_connected_correlation_error=coverr,max_spin_swap_error=swaperr))
    # Independently second-quantize the exported adjacent Givens circuit.
    visual=ROOT/'examples/synthetic_training/visual_examples.py'
    definitions=[x for x in ast.parse(visual.read_text()).body if isinstance(x,ast.FunctionDef) and x.name in ['givens_circuit','wavelet']]
    vs=dict(np=np);exec(compile(ast.Module(body=definitions,type_ignores=[]),str(visual),'exec'),vs)
    circuit=vs['givens_circuit'](h,1.2);actual=np.eye(16,dtype=complex)
    for gate in circuit['gates']:
        step=np.eye(16,dtype=complex)
        if gate['kind']=='orbital phase':
            q=gate['wires'][0]
            for b in range(16):step[b,b]=np.exp(1j*gate['angle']*((b>>q)&1))
        else:
            i,j=gate['wires'];B=np.array(gate['matrix_real'])+1j*np.array(gate['matrix_imag'])
            for b in range(16):
                oi,oj=(b>>i)&1,(b>>j)&1
                if oi and oj:step[b,b]=np.linalg.det(B)
                elif oi or oj:
                    other=b^((1<<i)|(1<<j));column=0 if oi else 1
                    step[b,b]=B[column,column];step[other,b]=B[1-column,column]
        actual=step@actual
    manybody=sum(h[i,j]*(cd[i]@cs[j]) for i in range(n) for j in range(n))
    circuit_error=float(abs(actual-expm(-1j*manybody*1.2)).max());assert circuit_error<1e-11
    wave=vs['wavelet'](4,[(0,1),(1,2),(2,3)]);e=np.array(wave['eigenvalues']);V=np.array(wave['eigenvectors'])
    for scale in [.1,1.,10.]:assert abs((V@(scale*e*np.exp(-scale*e)*V[0])).sum())<1e-12
    result=dict(passed=True,pure_function_source='AST-selected electronic/hubbard/visual helpers, without PyArrow import',
        gaussian_explicit_Fock_comparisons=rows,exact_Hubbard_comparisons=dimer,
        givens_full_Fock_recomposition_error=circuit_error,graph_wavelets_zero_sum=True,
        scope='Normal Slater/BdG dynamics, exact Hubbard dimer, Givens circuit and graph wavelets; no nuclear MD or ab-initio chemistry validation')
    out=ROOT/'outputs/checks/2026-11-04-synthetic-training/review';out.mkdir(parents=True,exist_ok=True)
    (out/'dynamics-review.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))

if __name__=='__main__':main()
