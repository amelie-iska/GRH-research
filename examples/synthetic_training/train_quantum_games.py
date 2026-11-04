"""CPU finite nonlocal-game learners; no Connes-separation claim."""
import argparse,json,math
from pathlib import Path
import numpy as np
import torch
from common import fresh,write_json,sha
torch.set_num_threads(1);torch.set_default_dtype(torch.float64)
I=torch.eye(2,dtype=torch.complex128);X=torch.tensor([[0,1],[1,0]],dtype=torch.complex128);Y=torch.tensor([[0,-1j],[1j,0]]);Z=torch.diag(torch.tensor([1.,-1.])).to(torch.complex128)
square=[[torch.kron(Z,I),torch.kron(I,Z),torch.kron(Z,Z)],[torch.kron(I,X),torch.kron(X,I),torch.kron(X,X)],[torch.kron(Z,X),torch.kron(X,Z),torch.kron(Y,Y)]]
CN=torch.tensor([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]],dtype=torch.complex128)

def bell_values(p,alpha):
    state=torch.stack([torch.cos(p[0]),p[0]*0,p[0]*0,torch.sin(p[0])]).to(torch.complex128)
    A=[torch.cos(p[i])*Z+torch.sin(p[i])*X for i in [1,2]];B=[torch.cos(p[i])*Z+torch.sin(p[i])*X for i in [3,4]]
    E=torch.stack([torch.vdot(state,torch.kron(a,b)@state).real for a in A for b in B]).reshape(2,2);marginal=torch.vdot(state,torch.kron(A[0],I)@state).real
    return alpha*marginal+E[0,0]+E[0,1]+E[1,0]-E[1,1],E,state,A,B

def localU(p):
    U=torch.eye(4,dtype=torch.complex128)
    for layer in range(2):
        for wire in range(2):
            a,b,c=p[layer,wire];rz1=torch.diag(torch.exp(torch.stack([-.5j*a,.5j*a])));ry=torch.stack([torch.stack([torch.cos(b/2),-torch.sin(b/2)]),torch.stack([torch.sin(b/2),torch.cos(b/2)])]).to(torch.complex128);rz2=torch.diag(torch.exp(torch.stack([-.5j*c,.5j*c])));gate=rz2@ry@rz1
            U=(torch.kron(gate.contiguous(),I) if wire==0 else torch.kron(I,gate.contiguous()))@U
        U=CN@U
    return U

def magic_values(p):
    UA=localU(p[0]);UB=localU(p[1]);A=[[UA@O@UA.conj().T for O in row] for row in square];B=[[UB@O.T@UB.conj().T for O in row] for row in square]
    E=torch.stack([torch.trace(A[i][j].T@B[i][j]).real/4 for i in range(3) for j in range(3)]).reshape(3,3)
    return .5+E.mean()/2,E,A,B

def moments(state,operators):
    vectors=torch.stack([state]+[O@state for O in operators],1);G=vectors.conj().T@vectors;e=torch.linalg.eigvalsh(G).real;assert float(e.min())>-1e-10
    return dict(real=G.real.detach().numpy().tolist(),imag=G.imag.detach().numpy().tolist(),eigenvalues=e.detach().numpy().tolist(),scope='Actual finite-strategy word Gram matrix; not a solved full NPA hierarchy or a Connes counterexample')

def game_bell(alpha,seed,steps):
    torch.manual_seed(seed);p=torch.nn.Parameter(torch.randn(5));opt=torch.optim.Adam([p],lr=.035);history=[]
    for k in range(steps+1):
        score,E,state,A,B=bell_values(p,alpha)
        if k%20==0 or k==steps:history.append(dict(step=k,score=float(score.detach()),parameters=p.detach().numpy().tolist(),correlations=E.detach().numpy().tolist()))
        if k<steps:opt.zero_grad();(-score).backward();assert torch.isfinite(p.grad).all();opt.step()
    score,E,state,A,B=bell_values(p,alpha);bound=math.sqrt(8+2*alpha*alpha);assert float(score)<bound+1e-9
    O=[torch.kron(a,I) for a in A]+[torch.kron(I,b) for b in B]
    theta=.5*math.asin(math.sqrt((4-alpha*alpha)/(4+alpha*alpha)));mu=math.atan(math.sin(2*theta));analytic=torch.tensor([theta,0.,math.pi/2,mu,-mu]);s,*_=bell_values(analytic,alpha);assert abs(float(s)-bound)<1e-12
    return dict(id=('CHSH' if alpha==0 else f'tilted-CHSH-{alpha}')+f'-seed{seed}',kind='bell',alpha=alpha,seed=seed,steps=steps,history=history,score=float(score.detach()),classical_bound=2+alpha,quantum_bound=bound,analytic_optimal_parameters=analytic.tolist(),moment_matrix=moments(state,O),word_labels=['1','A0','A1','B0','B1'],
        state_real=state.real.detach().numpy().tolist(),state_imag=state.imag.detach().numpy().tolist(),scope='Two-qubit real-plane local observables; offline shared training, no communication during game. Universal tilted bound is the separately cited SOS result.')

def game_magic(seed,steps):
    torch.manual_seed(seed);p=torch.nn.Parameter(torch.randn(2,2,2,3)*.35);opt=torch.optim.Adam([p],lr=.025);history=[]
    for k in range(steps+1):
        score,E,A,B=magic_values(p)
        if k%20==0 or k==steps:history.append(dict(step=k,score=float(score.detach()),parameters=p.detach().numpy().tolist(),correlations=E.detach().numpy().tolist()))
        if k<steps:opt.zero_grad();(-score).backward();assert torch.isfinite(p.grad).all();opt.step()
    score,E,A,B=magic_values(p);assert float(score)<=1+1e-10
    for i in range(3):assert torch.max(abs(A[i][0]@A[i][1]@A[i][2]-torch.eye(4)))<1e-10
    for j in range(3):assert torch.max(abs(B[0][j]@B[1][j]@B[2][j]-(1 if j<2 else -1)*torch.eye(4)))<1e-10
    state=torch.eye(4,dtype=torch.complex128).reshape(16)/2;I4=torch.eye(4,dtype=torch.complex128);operators=[torch.kron(a.contiguous(),I4) for row in A for a in row]+[torch.kron(I4,b.contiguous()) for row in B for b in row]
    return dict(id=f'magic-square-seed{seed}',kind='magic',seed=seed,steps=steps,history=history,score=float(score.detach()),classical_bound=8/9,quantum_bound=1.,moment_matrix=moments(state,operators),word_labels=['1']+[f'A{i}{j}' for i in range(3) for j in range(3)]+[f'B{i}{j}' for i in range(3) for j in range(3)],
        scope='Two Bell pairs; local Rz/Ry/CNOT measurement-frame learners preserve row/column commutation and parity. Actual finite strategy, not the finite-versus-commuting separation.')

def main(out,steps):
    out=fresh(out);games=[]
    for alpha in [0.,1.,1.5]:
        for seed in [17,29,43]:
            r=game_bell(alpha,seed,steps);games.append(r);print(r['id'],r['score'],flush=True)
    for seed in [17,29,43]:
        r=game_magic(seed,steps);games.append(r);print(r['id'],r['score'],flush=True)
    write_json(out/'games.json',dict(games=games,device='CPU',framework='PyTorch '+torch.__version__,classical_controls='CHSH enumerate16 deterministic outputs; magic-square parity obstruction and8/9 construction',
        interpretation='Finite tensor-product strategies cannot witness the MIP*=RE separation Cqa != Cqc; external theorem and embedding scopes remain distinct'))
    write_json(out/'manifest.json',dict(source_sha256=sha(__file__),files={p.name:dict(sha256=sha(p),bytes=p.stat().st_size) for p in out.iterdir() if p.is_file()}))
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);p.add_argument('--steps',type=int,default=1500);a=p.parse_args();main(a.output,a.steps)
