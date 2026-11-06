#!/usr/bin/env python3
"""NEW finite-cutoff Schur/Perron consistency controls; no old table rerun."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
import json,hashlib,itertools
import mpmath as mp
ROOT=Path(__file__).resolve().parents[3]
HELPER=ROOT/'examples/profile_uniformity/ideal_tower.py'
sys.path.insert(0,str(HELPER.parent))
import ideal_tower as I
mp.mp.dps=55
checks=[]
def ck(label,ok,**data):
    checks.append(dict(label=label,passed=bool(ok),**data))
    if not ok:raise AssertionError(label)
def st(z):return str(z)
def P(c,T,x):
    ell=mp.log(x)
    assert ell
    return mp.im(mp.ei(ell*(c+1j*T)))/mp.pi+(1 if ell<0 else 0)
def aug(fs,U):
    value=0
    for assignment in itertools.product(range(3),repeat=len(fs)):
        nr=ns=1;sign=1
        for norm,t in zip(fs,assignment):
            if t==1:nr*=norm;sign=-sign
            if t==2:ns*=norm;sign=-sign
        if nr<=U and ns<=U:value+=sign
    return value
def h(fs,v,w):
    out=1
    for n in fs:out*=1-mp.power(n,-v)-mp.power(n,-w)
    return out
def normop(m):
    return max(mp.svd(m,compute_uv=False)) if m.rows and m.cols else mp.mpf(0)
# Independent direct real-integral check of the Ei branch.
for U,n in [(5,1),(5,5),(5,6),(5,11),(11,5),(11,11),(11,12),(11,19)]:
    c=mp.mpf('0.2');T=mp.mpf(23);x=(mp.mpf(U)+mp.mpf('.5'))/n;ell=mp.log(x)
    fun=lambda t:(c*mp.cos(t*ell)+t*mp.sin(t*ell))/(c*c+t*t)
    val=x**c/mp.pi*mp.quad(fun,[0,c,1,3,7,13,T])
    ev=P(c,T,x)
    ck('Ei_vs_real_integral',abs(val-ev)<mp.mpf('1e-45'),U=U,n=n,error=st(abs(val-ev)))
ideals=[a for a in I.canonical_ideals(97) if a['good_S'] and a['squarefree']]
for a in ideals:
    a['keys']={tuple(f['generator']) for f in a['factors']}
    a['fns']=[f['norm'] for f in a['factors']]
rows=[a for a in ideals if a['norm']<=43]
cols=ideals
cases=[]
for X,U in [(242,11),(578,17),(1058,23)]:
    D=mp.mpf(X)/2;c=1/mp.log(4*X);T=mp.mpf(8*X);u=mp.mpf(U)+mp.mpf('.5')
    ck('highwindow',U*U==D and 2*D<=7*U*U,X=X,U=U)
    K=mp.matrix(len(rows),len(cols));AK=mp.matrix(len(rows),len(cols));ATK=mp.matrix(len(rows),len(cols));WK=mp.matrix(len(rows),len(cols))
    states=[];cache={};supported=0;inert=0
    for i,d in enumerate(rows):
      for j,a in enumerate(cols):
        nd=d['norm'];na=a['norm'];allowed=not (d['keys']&a['keys']) and nd*na<=X
        if not allowed:
            states.append(dict(i=i,j=j,mask=0));continue
        fs=d['fns']+a['fns'];phase=I.direct_symbol([(tuple(f['generator']),f['exponent']) for f in a['factors']],tuple(d['generator_omega']))
        ck('raw_cubic_mask',phase is not None,X=X,i=i,j=j)
        phase=(2*phase)%6
        kval=mp.e**(mp.pi*1j*phase/3);K[i,j]=kval
        exact=aug(fs,U);approx=mp.mpc(0)
        for ass in itertools.product(range(3),repeat=len(fs)):
            nr=ns=1;sgn=1
            for n,t in zip(fs,ass):
                if t==1:nr*=n;sgn=-sgn
                if t==2:ns*=n;sgn=-sgn
            for n in (nr,ns):
                if n not in cache:
                    x=u/n;val=P(c,T,x);target=int(n<=U)
                    bound=2*x**c/(mp.pi*T*abs(mp.log(x)))
                    ck('Perron_error',abs(val-target)<=bound+mp.mpf('1e-45'),X=X,n=n,error=st(abs(val-target)),bound=st(bound))
                    ck('half_integer_gap',abs(mp.log(x))>=1/mp.mpf(3*X),X=X,n=n)
                    cache[n]=val
            approx+=sgn*cache[nr]*cache[ns]
        err=abs(approx-exact);bound=18*mp.mpf(X)/T*3**len(fs)
        ck('double_cutoff_error',err<=bound,X=X,i=i,j=j,error=st(err),bound=st(bound))
        v=c+mp.mpf('.71')*1j;w=c-mp.mpf('.34')*1j
        ck('coprime_polynomial_factor',abs(h(fs,v,w)-h(d['fns'],v,w)*h(a['fns'],v,w))<mp.mpf('1e-45'),X=X,i=i,j=j)
        AK[i,j]=exact*kval;ATK[i,j]=approx*kval
        x=mp.mpf(nd*na)/D
        wp=((x-1)*(2-x))**3*mp.e**(1j*x/7) if 1<x<2 else 0
        WK[i,j]=wp*AK[i,j]
        supported+=1;inert+=any(int(mp.sqrt(n))**2==n for n in fs)
        states.append(dict(i=i,j=j,mask=1,phase6=phase,Nd=nd,Na=na,A_U=exact,A_T_real=st(mp.re(approx)),A_T_imag=st(mp.im(approx)),W_real=st(mp.re(wp)),W_imag=st(mp.im(wp))))
    kn=normop(K);an=normop(AK);atn=normop(ATK);ern=normop(AK-ATK);wn=normop(WK)
    G=max(3**len(a['fns']) for a in rows)*max(3**len(a['fns']) for a in cols)
    lt=mp.asinh(T/c)/mp.pi
    main=G*mp.e**2*lt**2
    rem=G*32*mp.power(X,mp.mpf('1.5'))/T
    ck('finite_integral_operator_bound',atn<=main*kn,X=X,norm=st(atn),bound=st(main*kn))
    ck('Frobenius_residual_bound',ern<=rem*kn,X=X,norm=st(ern),bound=st(rem*kn))
    ck('actual_AU_operator_bound',an<=(main+rem)*kn,X=X,norm=st(an),bound=st((main+rem)*kn))
    B=mp.mpf(1)/64
    wp1=mp.mpf(3)/16+B/7
    wp2=mp.mpf(15)/8+mp.mpf(3)/56+B/49
    JW=mp.log(2)/mp.pi*(B+2*wp1+4*wp2)
    ck('common_complex_W_operator_bound',wn<=JW*(main+rem)*kn,X=X,norm=st(wn),bound=st(JW*(main+rem)*kn),J_bound=st(JW))
    cases.append(dict(X=X,D=st(D),U=U,T=st(T),shape=[len(rows),len(cols)],supported=supported,raw_zero_states=len(rows)*len(cols)-supported,inert_factor_entries=inert,G=G,K_norm=st(kn),AU_K_norm=st(an),AU_T_K_norm=st(atn),residual_norm=st(ern),W_AU_K_norm=st(wn),states=states))
out=ROOT/'outputs/checks/2026-11-06-coherent-band/root/finite-schur-controls-v1';out.mkdir(parents=True,exist_ok=True)
p=out/'controls-v1.json';assert not p.exists()
data=dict(passed=True,count=len(checks),checks=checks,cases=cases,scope='NEW actual-good-ideal finite auxiliary cubic matrices and analytic Perron consistency controls; not complete original physical-row-family data, interval enclosures or proof by numerics',interval_enclosures=False,dps=mp.mp.dps,no_randomness=True,no_old_tables_or_accepted_controls_rerun=True,mpmath=mp.__version__,helper_path=str(HELPER.relative_to(ROOT)),helper_sha256=hashlib.sha256(HELPER.read_bytes()).hexdigest(),proof_note_sha256=hashlib.sha256((ROOT/'planning/coherent-band-20261106/root/FINITE_CUTOFF_SCHUR-v1.md').read_bytes()).hexdigest(),script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
p.write_text(json.dumps(data,indent=2)+'\n')
print(json.dumps(dict(passed=True,assertion_entries=len(checks),case_shapes=[c['shape'] for c in cases],sha256=hashlib.sha256(p.read_bytes()).hexdigest())))
