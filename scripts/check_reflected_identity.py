"""Exact local diagnostics for reflected arithmetic; no moment/GRH certificate."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json
from check_finite_correlation import ResidueField
from check_reciprocity_period import prime_symbol

OUT=Path(__file__).resolve().parents[1]/'outputs/checks/2026-11-03-reflected-identity'

def phase(f,j,x):
    return None if x==0 else j*f.phase[x]%6

def run():
    columns=0;cross=0;partitions=0
    for f in (ResidueField(7,2),ResidueField(13,3),ResidueField(5)):
        for n,b,j in product(range(f.q),range(f.q),range(6)):
            lhs=phase(f,3*j,f.mul(n,f.power(b,3)))
            assert lhs==phase(f,3*j,f.mul(n,b))
            mark=phase(f,-2*j,f.mul(n,f.power(b,3)))
            rhs=None if b==0 else phase(f,-2*j,n)
            assert mark==rhs
            assert int(f.mul(n,f.power(b,3))==0)==int(n==0)+int(n!=0)*int(b==0)
            columns+=1;partitions+=1
        # Exact scalar extraction with actual sigma=lambda²t and epsilon.
        lam=(1+2*f.omega)%f.p if f.omega is not None else 1+2*f.p
        assert lam!=0
        minus_lam5inv=f.neg(f.inv[f.power(lam,5)])
        for t,j in product(range(1,f.q),range(6)):
            sigma=f.mul(f.power(lam,2),t)
            eps=f.neg(f.inv[f.mul(f.power(lam,5),f.power(t,2))])
            if j==4:
                actual=phase(f,-2,sigma)
                const=phase(f,-4,lam)
            else:
                actual=(phase(f,-2,sigma)+phase(f,-j-2,eps))%6
                const=(phase(f,-4,lam)+phase(f,-j-2,minus_lam5inv))%6
            expected=(const+(2*j+2)*f.phase[t])%6
            assert actual==expected
            cross+=1
    primes=[(1,3),(-2,-3),(4,3),(1,-3),(-2,3),(1,6),(1,-6),(-5,0),(-11,0)]
    pairs=0;moving_nontrivial=0
    for p,q in product(primes,repeat=2):
        if p==q:continue
        a,b=prime_symbol(p,q),prime_symbol(q,p)
        assert 2*a%6==2*b%6
        for j,k in product(range(6),repeat=2):
            actual=((2*j+2)*a+(2*k+2)*b)%6
            expected=2*a*(j+k+2)%6
            assert actual==expected
            pairs+=1
        assert (4*a+2*b)%6==0
        assert (4*a+10*b)%6==2*a%6
        moving_nontrivial+=int(2*a%6!=0)
    # Genuine cross-prime phases: a=chi_7(pi13)=zeta6; b=chi_13(pi7)=zeta6^4.
    p,q=(1,3),(4,3)
    a,b=prime_symbol(p,q),prime_symbol(q,p)
    assert (a,b)==(1,4)
    assert (4*a+2*b)%6==0 and (4*a+10*b)%6==2
    # Frozen Ramanujan extraction retains the entire shared cube factor.
    extractions=0
    for nval,bval,k in product((0,1),range(5),range(-4,6)):
        if nval:
            nf,bf,res_n,res_b=1,0,0,bval
        elif bval:
            nf,bf,res_n,res_b=0,1,0,bval-1
        else:
            continue
        assert nf+res_n+3*(bf+res_b)==nval+3*bval
        # Prime log-power after its q_p^(1/2) divisibility coefficient.
        actual=F(1,2)-F(nval,2)-bval
        expected=-F(bf,2)-F(res_n,2)-res_b
        assert actual==expected
        # Separate ramified exponent contributes -k/3 after the d/sqrt(q_mu) bound.
        assert F(k,6)-F(k,2)==-F(k,3)
        extractions+=1
    result={'zero_preserving_dual_column_cases':columns,
            'ramanujan_partition_cases':partitions,'actual_local_scalar_cases':cross,
            'actual_cross_prime_phase_cases':pairs,
            'nontrivial_moving_j4_prime_pairs':moving_nontrivial,
            'shared_cube_normalization_cases':extractions,
            'moving_j4_witness':{'row_prime':[1,3],'other_prime':[4,3],
                'sextic_exponents':[1,4],'row_mark_phase':0,'row_j4_phase':2},
            'parameters':'fields7,13,25; all character powers0..5 with zero extension; nine primary primes; cube valuations0..4; ramified exponents-4..5; deterministic',
            'scope':'exact local diagnostics and normalization; no theta reflection, common Fourier representation, large-sieve moment or GRH certification'}
    OUT.mkdir(parents=True,exist_ok=True)
    (OUT/'certificate.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':run()
