"""Independent Fraction reconstruction and guarded-domain checks for v4."""
from pathlib import Path
from fractions import Fraction
import hashlib,importlib.util,json,math
ROOT=Path(__file__).resolve().parents[3]

def main():
    folder=ROOT/'outputs/experiments/2026-11-04-rational-learning-v4'
    path=folder/'rational-constants.json';saved=json.loads(path.read_text())
    source=ROOT/'examples/synthetic_training/certify_learning_constants.py'
    digest=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
    assert digest(source)==digest(folder/'generation_source.py')==saved['source_sha256']
    assert path.read_bytes()==(ROOT/'web/data/synthetic-training/analytic-v1/rational-constants.json').read_bytes()
    def fraction(record):
        num,den=int(record['numerator']),int(record['denominator'])
        assert den>0 and math.gcd(num,den)==1
        value=Fraction(num,den);assert record['display_float_not_certificate']==float(value)
        return value
    assert fraction(saved['center']['real'])==Fraction(1,2) and fraction(saved['center']['imag'])==0
    R,rho,r=[fraction(saved['radii'][key]) for key in ['R','rho','r']]
    assert (R,rho,r)==(Fraction(7,10),Fraction(6,5),Fraction(12,5)) and saved['sample_count']==64
    records=[]
    for item in saved['records']:
        q,a=item['conductor'],item['parity'];d=Fraction(3,q);n0,L=8,16
        # Independent integer ceiling, recursive integration-by-parts coefficients.
        exponent=(1+Fraction(1,2)+r+a)/2-1
        k=max(0,-((-exponent.numerator)//exponent.denominator))
        def Q(x):
            answer=Fraction(1,x);term=answer
            for j in range(1,k+1):term*=Fraction(k-j+1,x);answer+=term
            return answer
        def U(x):return Fraction(L,L+x)**L
        C=Fraction(1) if a==0 else (d+1)/(2*d)
        assert C*C*d>=1 if a==1 else C==1
        assert 0<U(d*n0)<1
        prefix=sum((n**a*U(d*n*n)*Q(d*n*n) for n in range(1,n0)),Fraction())
        tail=C*Q(d*n0*n0)*U(d*n0*n0/2)/(1-U(d*n0))
        M=2*(prefix+tail)
        assert M==fraction(item['M_r'])
        con=item['construction'];assert (con['k'],con['n0'],con['L'])==(k,n0,L)
        for key,value in [('d_lower',d),('C',C),('prefix',prefix),('one_integral_tail',tail)]:assert fraction(con[key])==value
        ceiling=(M.numerator+M.denominator-1)//M.denominator
        assert item['integer_growth_bound']==ceiling=={3:4,4:10,5:6}[q]
        assert M<ceiling
        for model in item['models']:
            N=model['degree'];u,v,w=R/rho,R/r,(rho/r)**64
            assert fraction(model['oracle_assuming_eta_1e_minus12'])==Fraction(1,10**12)*sum((u**j for j in range(N+1)),Fraction())
            assert fraction(model['alias'])==M*w/(1-w)*sum((v**j for j in range(N+1)),Fraction())
            assert fraction(model['Taylor'])==M*v**(N+1)/(1-v)
        records.append(dict(conductor=q,parity=a,integer_growth_bound=ceiling,all_exact_terms_match=True))
    spec=importlib.util.spec_from_file_location('rational_review_generator',source);module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    invalid=[('zero_x',lambda:module.exponential_upper(Fraction(0))),('negative_x',lambda:module.exponential_upper(Fraction(-1))),
             ('floating_x',lambda:module.exponential_upper(.5)),('zero_L',lambda:module.exponential_upper(Fraction(1),0)),
             ('negative_L',lambda:module.exponential_upper(Fraction(1),-1)),('floating_L',lambda:module.exponential_upper(Fraction(1),16.)),
             ('small_conductor',lambda:module.growth(2,1)),('floating_conductor',lambda:module.growth(3.,1)),
             ('invalid_parity',lambda:module.growth(3,2)),('floating_parity',lambda:module.growth(3,1.)),
             ('zero_cutoff',lambda:module.growth(3,1,0)),('floating_cutoff',lambda:module.growth(3,1,8.))]
    controls=[]
    for name,call in invalid:
        try:call()
        except (AssertionError,TypeError,ValueError):controls.append(name)
        else:raise AssertionError('Invalid API accepted: '+name)
    assert not saved['full_sample_oracle_certified'] and not saved['GRH_proved'] and saved['new_Lean_declarations']==0
    for version in ['v1','v2','v3']:
        old=json.loads((ROOT/f'outputs/experiments/2026-11-04-rational-learning-{version}/rational-constants.json').read_text())
        for before,after in zip(old['records'],saved['records']):
            assert before['M_r']==after['M_r'] and before['models']==after['models']
    result=dict(passed=True,version='v4',exact_fraction_reconstruction=records,negative_domain_controls=controls,
        source_snapshot_hash_matches=True,web_copy_byte_identical=True,earlier_numeric_certificates_preserved=True,
        full_sample_oracle_certified=False,new_Lean_declarations=0,GRH_proved=False,
        scope='Exact rational growth/alias/Taylor arithmetic and assumed-eta term; no certified sample evaluation or coefficient rounding')
    out=ROOT/'outputs/checks/2026-11-04-synthetic-training/review';out.mkdir(parents=True,exist_ok=True)
    (out/'rational-constants-review.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))

if __name__=='__main__':main()
