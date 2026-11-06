"""NEW exact combinatorial/exponent controls only; no arithmetic fixture or old checker."""
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations
import hashlib,json,os,subprocess
R=Path(__file__).resolve().parents[3];P=Path(__file__).resolve().parent;O=R/'outputs/checks/2026-11-05-coherent-mertens/lane-b'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def main():
 if hasattr(os,'sched_setaffinity'):os.sched_setaffinity(0,{min(os.sched_getaffinity(0))})
 frozen=json.loads((O/'precheck-freeze-v1.json').read_bytes())
 assert sha(P/'JOINT_STIELTJES_ATTEMPT-v1.md')==frozen['note_sha256'] and sha(Path(__file__))==frozen['checker_sha256']
 pins=json.loads((O/'source-pins-v1.json').read_bytes())
 for n,h in pins['source_sha256'].items():assert sha(R/n)==h,n
 # Formal IDEAL supports retain conjugates with the same norm as distinct IDs.
 norms={'7a':7,'7b':7,'13a':13,'31a':31};U=19
 def norm(g):
  n=1
  for p in g:n*=norms[p]
  return n
 def divisors(g):
  seq=sorted(g)
  return [frozenset(c)for k in range(len(seq)+1)for c in combinations(seq,k)]
 full=[frozenset(c)for k in range(len(norms)+1)for c in combinations(norms,k)];active=[g for g in full if norm(g)<7*U]
 pairs=0
 for g in active:
  for h in active:
   common=g&h;kernel=sum((-1)**len(f)for f in divisors(common)if all(norms[p]<=U for p in f));expected=int(not common)+int(g==h and len(g)==1 and norm(g)>U);assert kernel==expected,(g,h);pairs+=1
 assert frozenset({'7a'})!=frozenset({'7b'}) and norm(frozenset({'7a'}))==norm(frozenset({'7b'}))
 assert not(frozenset({'7a'})&frozenset({'7b'}))
 # Outside the actual short range, a shared rough prime need not be a diagonal.
 g=frozenset({'31a'});h=frozenset({'31a','7a'});assert norm(h)==217 and norm(h)>7*U
 kernel=sum((-1)**len(f)for f in divisors(g&h)if all(norms[p]<=U for p in f));wrong=int(not(g&h))+int(g==h and len(g)==1 and norm(g)>U);assert kernel==1 and wrong==0
 for g in active:
  if len(g)==1 and norm(g)>U:assert [f for f in divisors(g)if all(norms[p]<=U for p in f)]==[frozenset()]
 H=F(3,4);X=F(1,2);cases=[]
 for name,a1,a2,expected in [('pure',F(3,4),F(0),[F(3,4),F(1,2),F(5,6)]),('mixed',F(5,12),F(1,6),[F(7,12),F(2,3),F(7,9)])]:
  assert a1+2*a2==H
  r=a1+a2;m=max(a1,a2);terms=[r,X+r-m,F(2,3)*X+r-m/3];assert terms==expected
  first=max(terms);second=max(X,2*r);assert second>first
  deficit=first-H;alpha=deficit/X;assert alpha==({'pure':F(1,6),'mixed':F(1,18)}[name])
  cases.append(dict(name=name,A1=str(a1),A2=str(a2),H=str(H),X0=str(X),monomials=[str(x)for x in terms],first_bound=str(first),second_bound=str(second),deficit_D_power=str(deficit),conditional_d2_U_decay=str(alpha)))
 # L2 scaling in a dyad: E amplitude T^(1-alpha) has d2 exponent -alpha.
 for alpha in [F(0),F(1,6),F(1,18)]:assert (2*(1-alpha)+1)/2-F(3,2)==-alpha
 states=[]
 for x in pins['protected11states']:
  head=subprocess.check_output(['git','-C',x['path'],'rev-parse','HEAD'],env={**os.environ,'GIT_OPTIONAL_LOCKS':'0'}).decode().strip();assert head==x['HEAD'] and sha(Path(x['index_path']))==x['index_sha256'];states.append(x)
 record=dict(passed=True,scope='Exact NEW formal-support kernel/domain and Fraction budget controls; not actual-character data, arithmetic estimate, theorem proof or scientific rerun',note_sha256=sha(P/'JOINT_STIELTJES_ATTEMPT-v1.md'),checker_sha256=sha(Path(__file__)),source_pins_sha256=sha(O/'source-pins-v1.json'),formal_good_prime_ideal_norms=norms,U=U,short_bound_exclusive=7*U,active_supports=len(active),ordered_kernel_controls=pairs,equal_norm_conjugate_IDs_retained=True,outside_short_domain_negative=dict(g_norm=31,h_norm=217,true_kernel=1,invalid_diagonal_only_prediction=0),critical_budget_cases=cases,mean_not_centered=True,randomness=None,CPU_affinity_count=len(os.sched_getaffinity(0)),protected11states_unchanged=len(states),no_old_evaluator_or_tables=True)
 with (O/'controls-v1.json').open('x')as f:json.dump(record,f,sort_keys=True,indent=2);f.write('\n')
 print(json.dumps(dict(passed=True,output=str(O/'controls-v1.json'),sha256=sha(O/'controls-v1.json'),kernel_pairs=pairs,states=len(states))))
if __name__=='__main__':main()
