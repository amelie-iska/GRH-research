"""Independent matrix/Born/exhaustive parity and graph-rank review."""
from pathlib import Path
from itertools import product
import json,math
import numpy as np
ROOT=Path(__file__).resolve().parents[3]
def main():
    I=np.eye(2,dtype=complex);X=np.array([[0,1],[1,0]],complex);Y=np.array([[0,-1j],[1j,0]]);Z=np.diag([1.,-1.]).astype(complex)
    O=[[np.kron(Z,I),np.kron(I,Z),np.kron(Z,Z)],[np.kron(I,X),np.kron(X,I),np.kron(X,X)],[np.kron(Z,X),np.kron(X,Z),np.kron(Y,Y)]]
    for i in range(3):
        assert np.array_equal(O[i][0]@O[i][1]@O[i][2],np.eye(4))
        assert np.array_equal(O[0][i]@O[1][i]@O[2][i],(-1 if i==2 else 1)*np.eye(4))
        for a,b in product(range(3),repeat=2):
            assert np.array_equal(O[i][a]@O[i][b],O[i][b]@O[i][a])
            assert np.array_equal(O[a][i]@O[b][i],O[b][i]@O[a][i])
    outputs=lambda p:[(a,b,p*a*b) for a,b in product([-1,1],repeat=2)]
    best=0
    for alice in product(outputs(1),repeat=3):
        for bob in product(outputs(1),outputs(1),outputs(-1)):
            best=max(best,sum(alice[i][j]==bob[j][i] for i,j in product(range(3),repeat=2)))
    assert best==8
    tilted=[];SOSerror=0.;rng=np.random.default_rng(20261104)
    for alpha in [0.,.5,1.,1.5,2.]:
        theta=.5*np.arcsin(np.sqrt((4-alpha*alpha)/(4+alpha*alpha)));mu=np.arctan(np.sin(2*theta))
        state=np.array([np.cos(theta),0,0,np.sin(theta)],complex);A=[Z,X];B=[np.cos(mu)*Z+np.sin(mu)*X,np.cos(mu)*Z-np.sin(mu)*X]
        operator=alpha*np.kron(A[0],I)+np.kron(A[0],B[0]+B[1])+np.kron(A[1],B[0]-B[1])
        value=float(np.vdot(state,operator@state).real);assert abs(value-np.sqrt(8+2*alpha*alpha))<1e-12
        classical=max(alpha*a0+a0*b0+a0*b1+a1*b0-a1*b1 for a0,a1,b0,b1 in product([-1,1],repeat=4));assert classical==2+alpha
        tilted.append(dict(alpha=alpha,attained=value,classical=classical))
    for _ in range(12):
        angle=rng.normal(size=4);A0,A1=[np.kron(np.cos(t)*Z+np.sin(t)*X,I) for t in angle[:2]];B0,B1=[np.kron(I,np.cos(t)*Z+np.sin(t)*X) for t in angle[2:]]
        operator=A0@(B0+B1)+A1@(B0-B1);Q0=A0-(B0+B1)/np.sqrt(2);Q1=A1-(B0-B1)/np.sqrt(2)
        err=float(abs(2*np.sqrt(2)*np.eye(4)-operator-(Q0@Q0+Q1@Q1)/np.sqrt(2)).max());SOSerror=max(SOSerror,err);assert err<1e-12
    fixtures=json.loads((ROOT/'outputs/checks/2026-11-04-synthetic-training/review/games-browser-fixtures.json').read_text())
    CN=np.array([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]],complex)
    def unitary(parameters):
        U=np.eye(4,dtype=complex)
        for layer in parameters:
            for q,(a,b,c) in enumerate(layer):
                rz=lambda t:np.diag(np.exp(np.array([-.5j,.5j])*t));ry=np.array([[np.cos(b/2),-np.sin(b/2)],[np.sin(b/2),np.cos(b/2)]])
                g=rz(c)@ry@rz(a);U=(np.kron(g,I) if q==0 else np.kron(I,g))@U
            U=CN@U
        return U
    probabilityerror=momenterror=spectrumerror=scoreerror=0.
    for f in fixtures['fixtures']:
        visibility=f['visibility'];moments=[]
        if f['kind']=='bell':
            p=f['parameters'];state=np.array([np.cos(p[0]),0,0,np.sin(p[0])],complex)
            A=[np.cos(t)*Z+np.sin(t)*X for t in p[1:3]];B=[np.cos(t)*Z+np.sin(t)*X for t in p[3:]]
            rho=visibility*np.outer(state,state.conj())+(1-visibility)*np.eye(4)/4
            ops=[np.eye(4)]+[np.kron(a,I) for a in A]+[np.kron(I,b) for b in B]
            score=f['alpha']*np.trace(rho@np.kron(A[0],I)).real
            for i,j in product(range(2),repeat=2):
                score+=(1 if i*j==0 else -1)*np.trace(rho@np.kron(A[i],B[j])).real
                actual=np.array([[np.trace(rho@np.kron((I+a*A[i])/2,(I+b*B[j])/2)).real for b in [-1,1]] for a in [-1,1]])
                probabilityerror=max(probabilityerror,float(abs(actual-np.array(f['joints'][i][j])).max()))
        else:
            UA,UB=[unitary(p) for p in f['parameters']];A=[[UA@o@UA.conj().T for o in row] for row in O];B=[[UB@o.T@UB.conj().T for o in row] for row in O]
            state=np.zeros(16,complex);state[[0,5,10,15]]=.5;rho=visibility*np.outer(state,state.conj())+(1-visibility)*np.eye(16)/16
            ops=[np.eye(16)]+[np.kron(o,np.eye(4)) for row in A for o in row]+[np.kron(np.eye(4),o) for row in B for o in row];score=0.
            for i,j in product(range(3),repeat=2):
                entry=f['joints'][i][j];actual=np.empty((4,4))
                for a,aa in enumerate(entry['alice']):
                    PA=np.eye(4,dtype=complex)
                    for k in range(3):PA=PA@(np.eye(4)+aa[k]*A[i][k])/2
                    for b,bb in enumerate(entry['bob']):
                        PB=np.eye(4,dtype=complex)
                        for k in range(3):PB=PB@(np.eye(4)+bb[k]*B[k][j])/2
                        actual[a,b]=np.trace(rho@np.kron(PA,PB)).real
                        if aa[j]==bb[i]:score+=actual[a,b]/9
                probabilityerror=max(probabilityerror,float(abs(actual-np.array(entry['probability'])).max()))
        moment=np.array([[np.trace(rho@a.conj().T@b) for b in ops] for a in ops])
        saved=np.array(f['moment']['real'])+1j*np.array(f['moment']['imag']);momenterror=max(momenterror,float(abs(moment-saved).max()))
        spectrumerror=max(spectrumerror,float(abs(np.linalg.eigvalsh(moment)-f['spectrum']).max()));scoreerror=max(scoreerror,abs(float(score)-f['score']))
    assert max(probabilityerror,momenterror,spectrumerror,scoreerror)<1e-9
    graphs=[]
    for item in fixtures['drawings']:
        m=item['m'];boundary=np.zeros((m+2,2*m),int)
        for j in range(m):
            for b in [0,1]:boundary[b,2*j+b]=-1;boundary[2+j,2*j+b]=1
        rank=np.linalg.matrix_rank(boundary);assert 2*m-rank==item['H1']==m-1
        face=[((i-1)%m)+(m if i<m else 0) for i in range(2*m)];assert face==item['face']
        assert len(item['cycles'])==1 and len(item['cycles'][0])==2*m
        assert item['euler']==1-item['H1']+item['H2']
        graphs.append(dict(m=m,filled=item['filled'],incidence_rank=int(rank),H1=item['H1'],H2=item['H2']))
    result=dict(passed=True,CHSH_SOS_error=SOSerror,tilted_attainment=tilted,magic_square_exact_parities=True,magic_square_classical_maximum_numerator=best,
        browser_independent_probability_error=probabilityerror,browser_independent_moment_error=momenterror,browser_spectrum_error=spectrumerror,browser_score_error=scoreerror,
        drawings=graphs,scope='Finite game matrices and exact dessin/rank checks; no NPA solver, Connes separation reproduction, HoTT formalization or GRH inference')
    out=ROOT/'outputs/checks/2026-11-04-synthetic-training/review';(out/'games-hubs-review.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
