"""Exact Eisenstein residue-field/correlation checks. No floating-point arithmetic."""
from pathlib import Path
import json

# Twice the coordinates a+b*sqrt(-3) of the six powers of 1+omega.
ROOTS = ((2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1))
def value(hist):
    return tuple(sum(n*r[j] for n,r in zip(hist,ROOTS)) for j in (0,1))
def rootvalue(exponent, scalar=1):
    return tuple(scalar*x for x in ROOTS[exponent%6])
def emul(x,y):
    a,b=x;c,d=y
    return a*c-b*d,a*d+b*c-b*d

class ResidueField:
    """O/(pi): split norms7,13,19 or the genuine inert field O/(5), size25."""
    def __init__(self,p,omega=None):
        self.p=p;self.omega=omega;self.q=p if omega is not None else p*p
        self.zeta=(1+omega)%p if omega is not None else 1+p
        self.inv=[0]+[self.power(x,self.q-2) for x in range(1,self.q)]
        assert all(self.mul(x,self.inv[x])==1 for x in range(1,self.q))
        roots=[self.power(self.zeta,e) for e in range(6)]
        assert len(set(roots))==6 and self.power(self.zeta,6)==1
        self.phase=[None]+[roots.index(self.power(x,(self.q-1)//6)) for x in range(1,self.q)]
        assert set(self.phase[1:])==set(range(6))
    def add(self,x,y):
        p=self.p
        if self.omega is not None:return (x+y)%p
        return (x%p+y%p)%p+p*((x//p+y//p)%p)
    def neg(self,x):
        p=self.p
        if self.omega is not None:return -x%p
        return (-(x%p))%p+p*((-(x//p))%p)
    def mul(self,x,y):
        p=self.p
        if self.omega is not None:return x*y%p
        a,b=x%p,x//p;c,d=y%p,y//p
        return (a*c-b*d)%p+p*((a*d+b*c-b*d)%p)
    def power(self,x,n):
        out=1
        while n:
            if n%2:out=self.mul(out,x)
            x=self.mul(x,x);n//=2
        return out
    def corr(self,a,b,k,c):
        hist=[0]*6
        if a:
            for y in range(1,self.q):
                x=self.mul(self.inv[a],self.add(k,self.mul(b,y)))
                if x:hist[(c*(self.phase[x]-self.phase[y]))%6]+=1
        elif b:
            y=self.mul(self.inv[b],self.neg(k))
            if y:
                for x in range(1,self.q):hist[(c*(self.phase[x]-self.phase[y]))%6]+=1
        elif k==0:
            for x in range(1,self.q):
                for y in range(1,self.q):hist[(c*(self.phase[x]-self.phase[y]))%6]+=1
        return value(hist)
    def raw_corr(self,a,b,k,c):
        hist=[0]*6
        for x in range(1,self.q):
            for y in range(1,self.q):
                if self.add(self.mul(a,x),self.neg(self.mul(b,y)))==k:
                    hist[(c*(self.phase[x]-self.phase[y]))%6]+=1
        return value(hist)
    def formula(self,a,b,k,c):
        principal=c%6==0
        if a and b:
            phase=c*self.phase[self.mul(b,self.inv[a])]
            scalar=self.q-1 if k==0 else self.q-2 if principal else -1
            return rootvalue(phase,scalar)
        if a or b:return (2*(self.q-1),0) if k and principal else (0,0)
        return (2*(self.q-1)**2,0) if k==0 and principal else (0,0)

def hensel_omega(p,base,c):
    r=base;mod=p
    for _ in range(1,c):
        r=next(r+mod*t for t in range(p) if ((r+mod*t)**2+(r+mod*t)+1)%(mod*p)==0)
        mod*=p
    return r

def run():
    fields=[ResidueField(7,2),ResidueField(13,3),ResidueField(5)]
    cases=0;raw_cases=0
    for f in fields:
        for c in range(1,7):
            for a in range(f.q):
                for b in range(f.q):
                    for k in range(f.q):
                        result=f.corr(a,b,k,c)
                        assert result==f.formula(a,b,k,c),(f.q,c,a,b,k,result)
                        if f.q==7:
                            assert result==f.raw_corr(a,b,k,c)
                            raw_cases+=1
                        cases+=1
    f=fields[0];lifting=0;overlap=0
    for c in (1,2,6):
        mod=7**c;r=hensel_omega(7,2,c);pi=(1+3*r)%mod
        assert emul((1,3),(1,3))==(-8,-3)
        for a,b in ((1,2),(1,pi)):
            inva=pow(a,-1,mod)
            for k in (0,1,2,7):
                hist=[0]*6
                for y in range(mod):
                    x=inva*(k+b*y)%mod
                    if x%7 and y%7:hist[(c*(f.phase[x%7]-f.phase[y%7]))%6]+=1
                assert value(hist)==tuple(7**(c-1)*v for v in f.formula(a%7,b%7,k%7,c))
                lifting+=1
        # Actual u=pi^(c+1), v=pi^c. Divide their congruence by pi^c.
        big=7**(c+1);rbig=hensel_omega(7,2,c+1);pibig=(1+3*rbig)%big
        for k in (0,1,2,7):
            hist=[0]*6
            for y in range(mod):
                x=(k+pibig*y)%big
                if x%7 and y%7:hist[((c+1)*f.phase[x%7]-c*f.phase[y%7])%6]+=1
            expected=(0,0) if k%7==0 or c%6 else rootvalue(f.phase[k%7],7**(c-1)*6)
            assert value(hist)==expected
            overlap+=1
    # Full common-factor CRT test with actual primary generators.
    C=(1,3);n1=(4,3);n2=(-2,3)
    u=emul(C,n1);v=emul(C,n2);qu,qv=7*13,7*19;total=qu*qv
    mods=(49,13,19);roots=(hensel_omega(7,2,2),3,7)
    omega=sum(r*(total//m)*pow(total//m,-1,m) for m,r in zip(mods,roots))%total
    assert (omega*omega+omega+1)%total==0
    ev=lambda z:(z[0]+z[1]*omega)%total
    f7,f13,f19=fields[0],fields[1],ResidueField(19,7)
    def phase_mod(x,fs):
        ps=[f.phase[x%f.q] for f in fs]
        return None if None in ps else sum(ps)%6
    c7=lambda z:(z[0]+2*z[1])%7
    c13=lambda z:(z[0]+3*z[1])%13
    c19=lambda z:(z[0]+7*z[1])%19
    reciprocity=(f19.phase[c19(n1)]-f13.phase[c13(n2)])%6
    crt=[]
    for k in ((0,0),(1,0),(-1,0),n1,n2,(2,1)):
        j=emul(C,k);hist=[0]*6
        for x in range(qu):
            ax=phase_mod(x,(f7,f13))
            if ax is None:continue
            for y in range(qv):
                ay=phase_mod(y,(f7,f19))
                if ay is not None and (ev(v)*x-ev(u)*y-ev(j))%total==0:
                    hist[(ax-ay)%6]+=1
        result=value(hist)
        p1=f13.phase[c13(k)];p2=f19.phase[(-c19(k))%19]
        if p1 is None or p2 is None:expected=(0,0)
        else:
            phase=p1-p2+reciprocity+f7.phase[c7(n1)*pow(c7(n2),-1,7)%7]
            expected=rootvalue(phase,6 if c7(k)==0 else -1)
        assert result==expected,(k,result,expected)
        crt.append({'k':list(k),'twice_Qsqrt_minus3_coordinates':list(result)})
    assert f7.corr(0,0,0,6)==(72,0)  # genuine36, artificial0;36>7
    report={'status':'passed','finite_field_cases':cases,'independent_raw_pair_cases':raw_cases,
            'residue_fields':[{'primary':'1+3omega','norm':7},{'primary':'4+3omega','norm':13},
                              {'primary':'-5','norm':25,'model':'F5[omega]/(omega^2+omega+1)'}],
            'prime_power_lift_cases':lifting,'overlapping_residual_prime_cases':overlap,
            'complete_common_factor_CRT_cases':crt,'principal_off_locus_corner':36,
            'arithmetic':'exact integers and sixth-root coordinates; no randomness',
            'scope':'Finite arithmetic diagnostics complement the universal Lean field proofs; not a Gram, reflection, moment or GRH proof.'}
    out=Path(__file__).resolve().parents[1]/'outputs/checks/2026-11-02-finite-correlation/certificate.json'
    out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))

if __name__=='__main__':run()
