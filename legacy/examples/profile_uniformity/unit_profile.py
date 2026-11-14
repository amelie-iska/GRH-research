#!/usr/bin/env python3
"""Exact varying-profile unit-row experiment; no fixed-profile/GRH counterexample."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
from fractions import Fraction as Q
from collections import Counter
from math import isqrt
import argparse,datetime,hashlib,json,types
import ideal_tower as Tower

ROOT=Path(__file__).resolve().parents[2];HERE=Path(__file__).resolve().parent
DEFAULT_D=(256,1024,4096,16384,65536,262144)
HELPERS=('scripts/check_finite_correlation.py','scripts/check_reciprocity_period.py','scripts/check_mobius_split.py','examples/arithmetic_cutoff/exact_recombination.py')
SOURCE_FILES=('examples/profile_uniformity/unit_profile.py','examples/profile_uniformity/test_profile.py','examples/profile_uniformity/ideal_tower.py','examples/profile_uniformity/README.md',*HELPERS)
SCOPE=('Finite exact full norm-group arithmetic at principal nu=1, S above2and3, '
       'actual order6 nonprincipal unit epsilon=1+omega, its raw-masked ideal sixth-power towers, real-minus-one witness and D-dependent common smooth '
       'profiles. This tests a supremum-only varying-profile claim. It is not '
       'a counterexample to a fixed-W target, derivative-dependent estimate or GRH; '
       'finite observations alone do not prove an asymptotic density lower bound.')
PH_OMEGA=((1,0),(1,1),(0,1),(-1,0),(-1,-1),(0,-1))

def digest(raw):return hashlib.sha256(raw).hexdigest()
def encode(x):
    if isinstance(x,Q):return str(x)
    raise TypeError(type(x).__name__)
def json_bytes(x):return (json.dumps(x,indent=2,sort_keys=True,default=encode)+'\n').encode()
def write_new(path,value):
    with path.open('xb') as f:f.write(json_bytes(value))
def refuse_existing(path):
    if path.exists():raise FileExistsError('Preserve existing output: '+str(path))
def current_source_hashes():return {name:digest((ROOT/name).read_bytes()) for name in SOURCE_FILES}
def check_source_hashes(expected,reader=None):
    reader=reader or (lambda p:p.read_bytes())
    changed=[name for name,h in expected.items() if digest(reader(ROOT/name))!=h]
    if changed:raise RuntimeError('Source bytes changed: '+', '.join(changed))
    return True

def validate_D(D):
    if type(D) is not int:raise TypeError('D must be an exact integer')
    if D<=1 or isqrt(D)**2!=D:raise ValueError('D must be an integer square greater than1')
    return isqrt(D)

def sieve_spf(limit):
    if type(limit) is not int or limit<2:raise ValueError('positive sieve range required')
    spf=list(range(limit+1));spf[1]=1
    for p in range(2,isqrt(limit)+1):
        if spf[p]==p:
            for n in range(p*p,limit+1,p):
                if spf[n]==n:spf[n]=p
    return spf

def factorize(n,spf):
    if type(n) is not int or not 1<=n<len(spf):raise ValueError('integer outside SPF range')
    out=[]
    while n>1:
        p=spf[n];e=0
        while n%p==0:n//=p;e+=1
        out.append((p,e))
    return out

def character_minus_one_by_norm(N):
    if N%6!=1:raise ValueError('good Eisenstein ideal norms are1mod6')
    return -1 if ((N-1)//6)%2 else 1

def ideal_norm_group(N,spf):
    factors=factorize(N,spf)
    if any(p in (2,3) for p,e in factors):return None,'S_prime_2_or_3'
    mult=1;ideal_norms=[]
    for p,e in factors:
        if p%3==1:
            if e>2:return None,'split_exponent_above_2'
            ideal_norms.extend([p]*e)
            if e==1:mult*=2
        else:
            if e!=2:return None,'inert_exponent_not_2'
            ideal_norms.append(p*p)
    divs=[1]
    for n in ideal_norms:divs=divs+[d*n for d in divs]
    divs.sort()
    return dict(norm=N,rational_prime_factors=factors,ideal_prime_norms=ideal_norms,ideal_multiplicity=mult,mu=(-1)**len(ideal_norms),divisor_norms=divs),None

def long_factor_count(divisor_norms,N,U):
    return sum(d>U and N//d>U for d in divisor_norms)

def profile_integer_node(n,nodal_values):return nodal_values.get(n,0)

def compute_case(D,spf):
    U=validate_D(D);assert 2*D-1<len(spf);rows=[];rejected={}
    for N in range(D+1,2*D):
        g,why=ideal_norm_group(N,spf)
        if why:rejected.setdefault(why,[]).append(N);continue
        r=long_factor_count(g['divisor_norms'],N,U);A=g['mu']*(r-1);chi=character_minus_one_by_norm(N)
        assert r%2==0 and A!=0 and abs(A)%2==1
        sign=1 if A*chi>0 else -1
        phase=((N-1)//6)%6;wphase=(-phase+(3 if A<0 else 0))%6
        g.update(r_U=r,A_U=A,chi_minus_one=chi,chi_epsilon_exponent=phase,order6_profile_node_exponent=wphase,order6_profile_node_zeta6=Tower.PH_ZETA[wphase],real_minus_one_profile_node=sign,unsigned_nodal_comparator_node=1)
        assert A*chi*sign==abs(A);rows.append(g)
    assert rows and len(rows)+sum(map(len,rejected.values()))==D-1
    M=sum(g['ideal_multiplicity'] for g in rows)
    S=sum(g['ideal_multiplicity']*abs(g['A_U']) for g in rows)
    T=sum(g['ideal_multiplicity']*g['A_U']*g['chi_minus_one'] for g in rows)
    direct=sum(g['ideal_multiplicity']*g['A_U']*g['chi_minus_one']*g['real_minus_one_profile_node'] for g in rows)
    assert direct==S and S>=M
    data=dict(schema='profile-unit-norm-groups-v1',scope=SCOPE,D=D,U=U,cutoff_relation='U^2=D',annulus='D<Nm<2D; endpoints are zero for the stated common profile',S='prime ideals above2and3',nu='principal',literal_row=[1,1],literal_row_norm=1,retained_real_witness=[-1,0],seed=None,arithmetic='integers and exact Fraction; deterministic SPF and complete norm-group enumeration',real_minus_one_signed_profile=dict(name='W_D',varies_with_D=True,common_to_all_ideal_columns=True,formula='W_D(y)=sum_(active N) sign(A_U(N)*chi4(N))*phi(4*(D*y-N)); phi(t)=exp(1-1/(1-t^2)) on |t|<1 and0otherwise',supnorm=1,derivative_bound='For fixed k, ||W_D^(k)||_infinity <= (4D)^k ||phi^(k)||_infinity; disjoint supports',integer_nodes='exact stated sign at each active N/D; zero at every other integer norm divided by D'),unsigned_nodal_comparator=dict(name='V_D',varies_with_D=True,fixed_profile_baseline=False,formula='V_D(y)=sum_(active N) phi(4*(D*y-N)); same D-dependent support, every active nodal value+1',supnorm=1,derivative_bound='For fixed k, ||V_D^(k)||_infinity <= (4D)^k ||phi^(k)||_infinity'),active_norm_groups=rows,rejected_integer_norms=rejected)
    complex_sum=tuple(sum(g['ideal_multiplicity']*g['A_U']*Tower.PH_ZETA[g['chi_epsilon_exponent']][j] for g in rows) for j in (0,1))
    data['order6_signed_profile']=dict(name='W_epsilon_D',varies_with_D=True,common_to_all_ideal_columns=True,supnorm=1,formula='sum_activeN sign(A_U(N))*conjugate(zeta6^((N-1)/6))*phi(4*(D*y-N))',integer_nodes='exact mu6 exponents and zeta6-basis pairs stored per norm; zero at every other integer node',derivative_bound='For fixed k, <=(4D)^k ||phi^(k)||_infinity',primitive_order=6,all_nontrivial_powers_nonprincipal=True,exact_conductor_claim=False)
    data['main_profile']='order6_signed_profile'
    data['real_minus_one_signed_profile']['name']='W_minus_one_D'
    data['signed_profile']=data['order6_signed_profile']
    data['ideal_tower_family']=Tower.family(rows,D)
    summary=dict(D=D,U=U,active_norm_groups=len(rows),active_squarefree_ideal_columns=M,sum_abs_A_over_ideals=S,unsigned_real_minus_one_nodal_sum_over_ideals=T,unit_amplitude_exact=f'{S}/sqrt({D})',unsigned_real_minus_one_nodal_amplitude_exact=f'{T}/sqrt({D})',unit_row_energy=Q(S*S,D),energy_divided_by_D=Q(S*S,D*D),count_only_energy_lower_bound=Q(M*M,D),column_count_divided_by_D=Q(M,D),unsigned_real_minus_one_nodal_comparator_energy=Q(T*T,D),principal_residue=0,principal_residue_reason='nu=1 and kappa_-1 is nonprincipal: its value at either norm7 prime ideal is-1',r_U_norm_group_histogram=dict(Counter(g['r_U'] for g in rows)),A_U_norm_group_histogram=dict(Counter(g['A_U'] for g in rows)),real_minus_one_profile_node_histogram=dict(Counter(g['real_minus_one_profile_node'] for g in rows)),nonzero_A_all_columns=True,asymptotic_claim_proved_by_finite_run=False,lower_bound_scope='Exact E_-1=I_-1 and sum_(0<Nu<=H)|E_u|^2 >= this energy for every H>=1. The asymptotic >=cD requires the separate squarefree-ideal count proof.',comparator_scope='V_D also varies with D; it is NOT a fixed-profile baseline')
    summary['main_order6_unit_omega']=[1,1]
    summary['main_order6_profile_energy']=Q(S*S,D)
    summary['unsigned_order6_nodal_sum_zeta6']=complex_sum
    a,b=complex_sum;summary['unsigned_order6_nodal_comparator_energy']=Q(a*a+a*b+b*b,D)
    summary['unsigned_nodal_comparator_energy']=summary['unsigned_order6_nodal_comparator_energy']
    summary['order6_profile_node_exponent_histogram']=dict(Counter(g['order6_profile_node_exponent'] for g in rows))
    summary['principal_residue_reason']='Main epsilon witness is nonprincipal of order6; powers1..5 have phases1..5 at norm7. Real-minus-one witness separately has value-1 at norm7.'
    summary['order6_principal_residue']=0
    summary['order6_nonprincipal_witness']='chi_(norm7)(epsilon)=zeta6; powers1..5 all nonprincipal'
    summary['tower_cumulative_caps']=data['ideal_tower_family']['caps']
    summary['capacity_matched_tower']=data['ideal_tower_family']['capacity_matched']
    return data,summary

def _fresh_helpers(expected):
    """Execute captured source bytes, avoiding silent cached bytecode/checkpoints."""
    check_source_hashes(expected)
    loaded={}
    for name in HELPERS:
        path=ROOT/name;raw=path.read_bytes();assert digest(raw)==expected[name]
        module_name=path.stem;module=types.ModuleType(module_name);module.__file__=str(path);module.__package__='';sys.modules[module_name]=module
        exec(compile(raw,str(path),'exec'),module.__dict__)
        loaded[module_name]=module
    check_source_hashes(expected)
    return loaded

def _norm_omega(z):a,b=z;return a*a-a*b+b*b

def _direct_minus_one(factors):
    out=1
    for (a,b),e in factors:
        assert e==1
        q=a*a-a*b+b*b
        if b==0:
            p=abs(a);value=pow(p-1,(q-1)//6,p)
        else:
            p=q;omega=(-a*pow(b,-1,p))%p;zeta=(1+omega)%p
            value=pow(p-1,(p-1)//6,p)
            assert pow(zeta,3,p)==p-1
        assert value in (1,p-1)
        out*=1 if value==1 else -1
    return out

def explicit_crosschecks(D_values,expected):
    h=_fresh_helpers(expected);ideals=h['check_mobius_split'];original=h['exact_recombination']
    count=0;normgroups=0;tower_count=0;checks=[]
    for D in D_values:
        U=validate_D(D);spf=sieve_spf(2*D-1);data,summary=compute_case(D,spf)
        all_ideals,index,divs,primes=ideals.universe(2*D)
        selected=[i for i,row in enumerate(all_ideals) if row['sf'] and D<row['q']<2*D]
        seen=Counter();S=T=0;columns=[]
        expected_rows={g['norm']:g for g in data['active_norm_groups']}
        for i in selected:
            m=all_ideals[i];N=m['q'];g=expected_rows[N];ds=sorted(all_ideals[d]['q'] for d in divs[i])
            assert ds==g['divisor_norms'] and m['mu']==g['mu'] and long_factor_count(ds,N,U)==g['r_U']
            factor_norms=[_norm_omega(p) for p,e in m['f']];labelled=[]
            for mask in range(1<<len(factor_norms)):
                value=1
                for j,n in enumerate(factor_norms):
                    if mask>>j&1:value*=n
                labelled.append(value)
            beta,A=original.coefficient_tables(labelled,U);assert A[-1]==g['A_U']
            direct=_direct_minus_one(m['f']);phase=ideals.scalar_symbol(m['f'],(-1,0))
            assert phase in (0,3) and direct==(1 if phase==0 else -1)==g['chi_minus_one']
            eps=Tower.direct_symbol(m['f'],(1,1));assert eps==ideals.scalar_symbol(m['f'],(1,1))==g['chi_epsilon_exponent']
            columns.append((m,A[-1],{p for p,e in m['f']},g['order6_profile_node_exponent']))
            seen[N]+=1;S+=abs(A[-1]);T+=A[-1]*direct;count+=1
        assert dict(seen)=={N:g['ideal_multiplicity'] for N,g in expected_rows.items()}
        assert S==summary['sum_abs_A_over_ideals'] and T==summary['unsigned_real_minus_one_nodal_sum_over_ideals']
        vchecks=[]
        for v in data['ideal_tower_family']['rows']:
            support={tuple(f['generator']) for f in v['factors']};total=0;allowed=[];zeros=0
            for m,A,fs,wphase in columns:
                u=tuple(v['literal_row_omega']);raw=ideals.scalar_symbol(m['f'],u);independent=Tower.direct_symbol(m['f'],u)
                assert raw==independent
                if fs.isdisjoint(support):
                    assert raw==((m['q']-1)//6)%6
                    z=Tower.PH_ZETA[(raw+wphase)%6];assert (A*z[0],A*z[1])==(abs(A),0)
                    total+=abs(A);allowed.append((fs,abs(A)))
                else:assert raw is None;zeros+=1
                tower_count+=1
            assert total==v['T_v'] and len(allowed)==v['allowed_ideal_columns']
            h1=sum(a*b for fs,a in allowed for gs,b in allowed if fs.isdisjoint(gs))
            assert 0<=h1<=total*total
            vchecks.append(dict(generator_omega=v['generator_omega'],norm=v['norm'],good_S=v['good_S'],T_v=total,raw_zero_columns=zeros,h1_ordered_pair_numerator=h1,h1_selected_row_contribution=Q(h1,D)))
        capchecks=[]
        for X in (2,4,8,16,64):
            vs=[v for v in vchecks if v['good_S'] and v['norm']<=X]
            capchecks.append(dict(X=X,H=X**6,rows=len(vs),selected_h1_contribution=sum((v['h1_selected_row_contribution'] for v in vs),Q(0)),scope='Selected good-S cumulative rows only. Not a lower bound for the h1 component over unselected rows.'))
        checks.append(dict(D=D,enumerated_ideal_columns=len(selected),active_norm_groups=len(seen),signed_profile_energy=Q(S*S,D),unsigned_real_nodal_energy=Q(T*T,D),tower_rows=vchecks,cumulative_goodS_selected_h1=capchecks))
        normgroups+=len(seen)
    assert ideals.scalar_symbol((((1,3),1),),(-1,0))==3
    assert ideals.scalar_symbol((((1,3),1),),(1,1))==1
    check_source_hashes(expected)
    return dict(passed=True,D_values=D_values,explicit_ideal_columns=count,original_A_checks=count,direct_symbol_checks=count,order6_unit_symbol_checks=count,tower_raw_symbol_checks=tower_count,norm_group_multiplicities_match=True,active_norm_groups_checked=normgroups,raw_character_at_norm7=-1,raw_epsilon_character_at_norm7_phase=1,all_nontrivial_epsilon_powers_nonprincipal=True,exact_conductor_claim=False,cases=checks,independence='Fresh full primary-ideal enumeration, original A_U helper, independent split/inert finite-field exponentiation and literal epsilon*beta_v^6 raw masks; all small-D ordered coprime column pairs computed directly. No old15-column fixture read.')

def freeze_source_pin(path):
    path=Path(path);refuse_existing(path)
    allowed=ROOT/'planning/signed-profile-20261105/implementation'
    assert path.resolve().is_relative_to(allowed.resolve())
    hashes=current_source_hashes();check_source_hashes(hashes)
    pin=dict(schema='profile-source-freeze-v1',frozen_before_accepted_run=True,utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),source_sha256=hashes,default_D=list(DEFAULT_D),nu='principal',S='above2and3',scope=SCOPE,seed=None,helper_loading='compile captured exact source bytes; no cached bytecode or checkpoint import')
    path.parent.mkdir(parents=True,exist_ok=True);write_new(path,pin);return pin

def run(output,pin_path,D_values=DEFAULT_D):
    output=Path(output);refuse_existing(output);D_values=list(D_values)
    assert len(D_values)==len(set(D_values)) and D_values
    for D in D_values:validate_D(D)
    pin_path=Path(pin_path).resolve();pin=json.loads(pin_path.read_text());assert pin['frozen_before_accepted_run'] is True
    expected=pin['source_sha256'];assert set(expected)==set(SOURCE_FILES);check_source_hashes(expected)
    spf=sieve_spf(2*max(D_values)-1)
    # Fresh small cases, not an old fixture or an accepted old training replay.
    independent=explicit_crosschecks([D for D in (256,1024) if D in D_values],expected)
    output.mkdir(parents=True,exist_ok=False);write_new(output/'source-pin.json',pin)
    artifacts={};summaries=[]
    for D in D_values:
        data,summary=compute_case(D,spf);input_name=f'norm-groups-D{D}.json';summary_name=f'summary-D{D}.json'
        write_new(output/input_name,data);summary['input_sha256']=digest((output/input_name).read_bytes());summary['source_pin_sha256']=digest(pin_path.read_bytes());write_new(output/summary_name,summary)
        artifacts[input_name]=digest((output/input_name).read_bytes());artifacts[summary_name]=digest((output/summary_name).read_bytes());summaries.append(summary)
        print(json.dumps({k:encode(v) if isinstance(v,Q) else v for k,v in summary.items() if k in ('D','U','active_norm_groups','active_squarefree_ideal_columns','sum_abs_A_over_ideals','unit_row_energy','energy_divided_by_D','unsigned_nodal_comparator_energy')}),flush=True)
    write_new(output/'independent-small-checks.json',independent);artifacts['independent-small-checks.json']=digest((output/'independent-small-checks.json').read_bytes())
    # Freeze copies of all exact code/helper bytes as provenance, never moving sources.
    for name,digest_expected in expected.items():
        target=output/'source-snapshot'/name;target.parent.mkdir(parents=True,exist_ok=True);raw=(ROOT/name).read_bytes();assert digest(raw)==digest_expected
        with target.open('xb') as f:f.write(raw)
        artifacts[str(target.relative_to(output))]=digest_expected
    check_source_hashes(expected);artifacts['source-pin.json']=digest((output/'source-pin.json').read_bytes())
    manifest=dict(schema='profile-uniformity-run-v1',passed=True,scope=SCOPE,D_values=D_values,U_values=[isqrt(D) for D in D_values],row=[1,1],retained_real_witness=[-1,0],nu='principal',S='above2and3',source_pin_path=str(pin_path.relative_to(ROOT)),source_pin_sha256=digest(pin_path.read_bytes()),source_sha256=expected,artifact_sha256=artifacts,all_norm_groups_and_rejections_saved=True,source_data_immutable=True,seed=None,exact_arithmetic=True,minimum_observed_energy_over_D=min(s['energy_divided_by_D'] for s in summaries),minimum_observed_column_count_over_D=min(s['column_count_divided_by_D'] for s in summaries),asymptotic_density_claim_proved_by_run=False,unsigned_comparator_also_varies_with_D=True,not_fixed_W_counterexample=True,GRH_claim=False,scientific_outputs_only_in_fresh_directory=True)
    write_new(output/'manifest.json',manifest);verify_run(output,check_current_sources=True)
    print(json.dumps(dict(passed=True,output=str(output),D_values=D_values,manifest_sha256=digest((output/'manifest.json').read_bytes()))),flush=True)
    return manifest

def verify_run(output,check_current_sources=True):
    output=Path(output);m=json.loads((output/'manifest.json').read_text())
    if check_current_sources:check_source_hashes(m['source_sha256'])
    for name,sha in m['artifact_sha256'].items():
        if digest((output/name).read_bytes())!=sha:raise RuntimeError('Artifact bytes changed: '+name)
    for D in m['D_values']:
        d=json.loads((output/f'norm-groups-D{D}.json').read_text());s=json.loads((output/f'summary-D{D}.json').read_text())
        assert digest((output/f'norm-groups-D{D}.json').read_bytes())==s['input_sha256']
        assert len(d['active_norm_groups'])+sum(map(len,d['rejected_integer_norms'].values()))==D-1
        S=sum(g['ideal_multiplicity']*abs(g['A_U']) for g in d['active_norm_groups'])
        assert Q(s['unit_row_energy'])==Q(S*S,D)
    return True

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);g=p.add_mutually_exclusive_group(required=True)
    g.add_argument('--freeze-source-pin',type=Path);g.add_argument('--output',type=Path);g.add_argument('--verify',type=Path)
    p.add_argument('--source-pin',type=Path);p.add_argument('--D',type=int,action='append')
    a=p.parse_args()
    if a.freeze_source_pin:
        result=freeze_source_pin(a.freeze_source_pin);print(json.dumps(dict(frozen=True,path=str(a.freeze_source_pin),source_files=len(result['source_sha256']))))
    elif a.verify:verify_run(a.verify);print('Source/input/artifact binding and exact summary energies verified')
    else:
        if a.source_pin is None:p.error('--output requires --source-pin frozen before the run')
        run(a.output,a.source_pin,a.D or DEFAULT_D)
