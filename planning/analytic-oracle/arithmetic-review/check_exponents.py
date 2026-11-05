from fractions import Fraction as F
import json
rows=[]
for delta in [F(1,100),F(1,10),F(1,4),F(49,100)]:
 for a in [F(0),F(1,20),F(1,8),F(1,4),F(1,2)]:
  old=F(3,8)+F(5,4)*delta+(2-4*delta)*a
  new=2*delta+(2-4*delta)*a
  gain=old-new
  assert gain==F(3,8)-F(3,4)*delta and gain>0
  assert new>0
  rows.append(dict(delta=str(delta),a=str(a),old_upper_excess=str(old),conditional_average_excess=str(new),gain=str(gain)))
report=dict(passed=True,cases=rows,arithmetic_moment_proved=False,AFM_is_explicit_input=True,GRH_proved=False,new_Lean_declarations=0)
print(json.dumps(report,indent=2))
