#!/usr/bin/env python3
"""Independent focused wild-prime-power/full-modulus Gauss and byte audit.
The infinite sieve/global theorem is reviewed in prose, not proved by this run.
"""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
from fractions import Fraction as F
import hashlib,json
ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/'outputs/checks/2026-11-05-arithmetic-learning/review-mixed/acceptance-v1.json'
if OUT.exists():raise FileExistsError(OUT)
PH=((1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1))
EW=((1,0),(1,1),(0,1),(-1,0),(-1,-1),(0,-1))
def add(x,y):return x[0]+y[0],x[1]+y[1]
def mul(x,y):return x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0]+x[1]*y[1]
def conj(x):return x[0]+x[1],-x[1]
def abs2(x):return x[0]*x[0]+x[0]*x[1]+x[1]*x[1]
def omega_mul(x,y):return x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0]-x[1]*y[1]
def total(xs):
 out=(0,0)
 for x in xs:out=add(out,x)
 return out
log2={(1,0):0,(0,1):1,(1,1):2}
log3={tuple(t%3 for t in z):e for e,z in enumerate(EW)}
checks=[];freqs=0
for modulus in (2,3,6):
 residues=[(a,b) for a in range(modulus) for b in range(modulus)]
 powers=[(s,j) for s in ((1,2) if modulus in (2,6) else (0,)) for j in ((1,2,4,5) if modulus in (3,6) else (0,))]
 for s,j in powers:
  def chi(z):
   a,b=z;e=0
   if modulus in (2,6):
    z2=(a%2,b%2)
    if z2==(0,0):return (0,0)
    e+=2*s*log2[z2]
   if modulus in (3,6):
    z3=(a%3,b%3)
    if z3 not in log3:return (0,0)
    e+=j*log3[z3]
   return PH[e%6]
  # For integer f=modulus, Tr((a+b omega)/(delta f))=b/f.
  assert 6%modulus==0
  def additive(z):return PH[(6//modulus*z[1])%6]
  tau=total(mul(chi(x),additive(x)) for x in residues)
  assert abs2(tau)==modulus**2
  nonunit=0
  for z in residues:
   G=total(mul(chi(x),additive(omega_mul(z,x))) for x in residues)
   expected=mul(conj(chi(z)),tau)
   assert G==expected,(modulus,s,j,z,G,expected)
   if chi(z)==(0,0):nonunit+=1;assert G==(0,0)
   freqs+=1
  checks.append(dict(generator=[modulus,0],ideal_norm=modulus**2,local_character_powers=[s,j],Gauss_zeta6=tau,Gauss_squared_norm=abs2(tau),nonunit_frequency_zeros=nonunit))
# Symbolic logarithmic slack coefficients, for the two max-pivot branches.
# C-2r+m, with branch x2>=x1 contributing x2-x1.
assert [j-2+(1 if j==1 else 0) for j in range(1,7)]==[0,0,1,2,3,4]
assert [j-2+(1 if j==2 else 0) for j in range(1,7)]==[-1,1,1,2,3,4]
# 2C+m-3r=(m-x1)+x2+3x3+5x4+7x5+9x6.
assert [2*j-3 for j in range(1,7)]==[-1,1,3,5,7,9]
witnesses=[]
for x in [(F(5,12),F(1,6),F(0),F(0),F(0),F(0)),(F(3,4),F(0),F(0),F(0),F(0),F(0))]:
 C=sum((j+1)*v for j,v in enumerate(x));r=sum(x);m=max(x[:2]);q=r-x[5]
 old=max(r,1+r-m,F(2,3)+r-m/3)
 ordinary=max(1+x[5],x[5]+2*q)
 assert C==F(3,4) and min(old,ordinary)==F(7,6)
 witnesses.append(dict(coordinates=list(map(str,x)),capacity=str(C),old=str(old),ordinary=str(ordinary),combined=str(min(old,ordinary))))
paths={
 'proposal_core':'planning/arithmetic-learning-20261105/mixed-attempt/mixed-conductor-core-proposal.tex',
 'proposal_details':'planning/arithmetic-learning-20261105/mixed-attempt/mixed-conductor-details-proposal.tex',
 'production_core':'papers/mixed-conductor-core.tex',
 'production_details':'papers/mixed-conductor-details.tex',
 'accepted_BGL_core':'papers/uniform-cutoff-moment-core.tex',
 'accepted_BGL_details':'papers/uniform-cutoff-moment-details.tex',
 'BGL_source':'planning/analytic-oracle/arithmetic-review/adversarial-sources/1112.1650v1.txt',
 'GL_source':'planning/weighted-moment-20261104/attempt/primary/1112.1642v2.txt',
 'author_draft':'planning/arithmetic-learning-20261105/mixed-attempt/MIXED_RADICAL_ATTEMPT.md',
 'prior_independent_draft_review':'planning/arithmetic-learning-20261105/mixed-attempt/REVIEW.md',
 'source_pins':'planning/arithmetic-learning-20261105/mixed-attempt/source-pins-v1.json',
 'review_check':'planning/arithmetic-learning-20261105/review-mixed/check_review_v1.py',
 'review':'planning/arithmetic-learning-20261105/review-mixed/REVIEW-v1.md'}
raw={key:(ROOT/p).read_bytes() for key,p in paths.items()}
assert hashlib.sha256(raw['proposal_core']).hexdigest()=='aebdea3c68f703a891f48dd481cfecd9bc5b734d50ecb3f8241643cb009a96ff'
assert hashlib.sha256(raw['proposal_details']).hexdigest()=='2362bd5def75d9b9dedc9e64d719f8f98546fb6f8685670fc0cfee88fd79763c'
old=b'block bound~\\eqref{wc:block}. With';new=b'block bound from Section~\\ref{wc:core}. With'
assert raw['proposal_core'].count(old)==1
assert raw['production_core']==raw['proposal_core'].replace(old,new)
assert raw['production_details']==raw['proposal_details']
assert b'\\label{wc:core}' in raw['accepted_BGL_core']
assert b'Lemma 2.1' in raw['BGL_source'] and b'Definition 1' in raw['GL_source']
receipt=dict(verdict='PASS',scope='Exact-byte independent mathematical prose review of the ordinary all-character conductor application and normalized residue-subtracted envelope; no Lean or GRH claim',Gauss_checks=checks,frequency_identities_checked=freqs,prime_power_scope='Actual Eisenstein ideals(2),(3),(6): inert/wild, ramified-prime-power, and composite full moduli; includes all nonunit-frequency zeros for every tested primitive character',symbolic_capacity_branches_checked=2,upper_envelope_witnesses=witnesses,mathematical_objections=[],production_core_only_change='eqref{wc:block} replaced by Section ref{wc:core}; exact byte equality after this single substitution verified',files={key:dict(path=paths[key],bytes=len(value),sha256=hashlib.sha256(value).hexdigest()) for key,value in raw.items()},not_run='No author checker/grid rerun; no production edits/build/browser/dependency/auth/Lean action. Infinite theorem acceptance is the independent derivation audit in REVIEW-v1.md, not inferred from finite checks.')
OUT.parent.mkdir(parents=True,exist_ok=True)
with OUT.open('x') as f:json.dump(receipt,f,indent=2);f.write('\n')
print(json.dumps(dict(verdict='PASS',frequency_identities_checked=freqs,Gauss_characters=len(checks),files={key:receipt['files'][key] for key in ('proposal_core','proposal_details','production_core','production_details')}),indent=2))
