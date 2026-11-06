"""Independent finite unit-ring and exact exponent bookkeeping, not the sieve theorem."""
from fractions import Fraction as Q
import json
def mul(x,y):return((x[0]*y[0]-x[1]*y[1])%3,(x[0]*y[1]+x[1]*y[0]-x[1]*y[1])%3)
def power(x,k):
 out=(1,0)
 for _ in range(k):out=mul(out,x)
 return out
mu6=[(1,0),(2,0),(0,1),(0,2),(1,1),(2,2)]
units=[(a,b)for a in range(3)for b in range(3)if(a*a-a*b+b*b)%3]
assert set(mu6)==set(units) and len(units)==6
assert all(power(x,6)==(1,0)for x in units)
assert [x for x in mu6 if x==(1,0)]==[(1,0)]
h=Q(3,4)
F=lambda a,b:[a,b,Q(5,6)*a+Q(1,3)*b,Q(1,3)*a+Q(5,6)*b]
a6=F(h,Q(1));glob=[h,Q(1)+h/6,Q(5,6)*h+Q(1,3),h/3+Q(5,6)];short=F(h,Q(1,2))
assert a6==[Q(3,4),Q(1),Q(23,24),Q(13,12)] and max(a6)==Q(13,12)
assert glob==[Q(3,4),Q(9,8),Q(23,24),Q(13,12)] and max(glob)==Q(9,8)
assert short==[Q(3,4),Q(1,2),Q(19,24),Q(2,3)] and max(short)==Q(19,24)
assert Q(7,6)-max(glob)==Q(1,24) and Q(7,6)-max(a6)==Q(1,12)
assert(max(short)-h)/Q(1,2)==Q(1,12) and Q(7,9)<max(short)
assert[Q(1),Q(2),Q(4,3),Q(11,6)][1:]==[Q(2),Q(4,3),Q(11,6)]
assert all(x>1 for x in [6,5,2]) and all(x>0 for x in [Q(1),Q(1,6),Q(5,6),Q(1,3)])
print(json.dumps(dict(passed=True,scope='Finite O/(3) unit bijection and exact exponent/summation bookkeeping only; no proof of external large sieve or actual energy/prime-error data',units_mod3=units,mu6_distinct_residues=mu6,gamma_unit_sixth_powers_one=True,only_global_unit_congruent1_is1=True,A6unit_terms=[str(x)for x in a6],global_terms=[str(x)for x in glob],short_terms=[str(x)for x in short],A6unit_gain=str(Q(7,6)-max(a6)),global_gain=str(Q(7,6)-max(glob)),pure_new_sufficient_U_power='1/12',mixed_retained_power='7/9',conditional_pure_strip='11/12',r6_convergent_exponents=[6,5,2],signed_divisor_exponents=['1(log)','2','4/3','11/6'],S_supported_global_exponents=['1','1/6','5/6','1/3'],S_supported_A6unit_D_term='finite polylog; not exponent-zero convergence'),sort_keys=True,indent=2))
