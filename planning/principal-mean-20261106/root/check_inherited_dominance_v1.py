"""Guard the retracted novelty claim against the already accepted fixed-s comparison."""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib
R=Path('/home/iska/Documents/LaTeX-projects/GRH-from-Mac-20261104');O=R/'outputs/checks/2026-11-06-principal-mean/root/mixed-band-budget-v1'
old=O/'certificate.json';assert hashlib.sha256(old.read_bytes()).hexdigest()=='e59bfccf2cc1d7b2ef8a9b7d7fe23820527aaa6ea33d969bed3ff540fa621098'
# Monomials of the direct INHERITED actual-sector bound (R/D)V F6(X/V6,D).
def inherited(x):return[x-F(5,4),F(3,4),5*x/6-F(3,4),x/3+F(1,4)]
left=inherited(F(1));right=inherited(F(3,2))
assert right==[F(1,4),F(3,4),F(1,2),F(3,4)]
assert all(y<=F(3,4)for y in left+right)
assert F(3,2)>F(10,9)
# High virtual-prime-d, fixed bounded residuals: O(D) pairs, not O(D²).
# Pure top-sector absolute exponent r + x/6 -1 = -3/16, already below target.
assert F(3,4)+F(3,8)/6-1==F(-3,16)
x=dict(passed=True,classification='CORRECTION: no new actual-sector exponent gain',prior_formal_certificate_sha256=hashlib.sha256(old.read_bytes()).hexdigest(),source='Accepted UB01 Eq12 at9d0ec518, not a new sieve or signed estimate',inherited_actual_band='|P_V|/D <=B²eps(R/D)V F6(X/V6,D), via fixed goods plus S-supported sixthparts; constantD uses finitepolylog',critical_mixed_direct_terms_at_x_threehalves=list(map(str,right)),old_operator_certificate_extent='3/2',proposed_M_plus_error_extent='10/9',corrected_conclusion='The integrated mean norm is a valid derived corollary, but its 10/9 actual-sector consequence is weaker than the inherited fixed-s theorem. No new range or saving; the attempted novelty inference FAILED. Preserve original certificate as a historical arithmetic check only.',prime_d_diagnostic='For bounded residuals, the auxiliary virtual-prime-d sector has at mostO(D) pairs; absolute bound R V Z/D, pure top power-3/16, so fixed-family prime cancellation there is not the missing low-d saving.',no_actual_energy_lower_bound=True,old_numeric_data_rerun=False,producer_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
p=O/'dominance-addendum-v1.json'
with p.open('x')as f:json.dump(x,f,indent=2,sort_keys=True);f.write('\n')
print(json.dumps(dict(passed=True,sha256=hashlib.sha256(p.read_bytes()).hexdigest(),no_new_gain=True)))

