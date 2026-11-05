"""End-to-end requested-error analytic readouts with fresh adaptive samples.

Fixed primitive quadratic conductors and compact, not a zero-location result.
Exact executed midpoint-objective GD states are losslessly compressed by a
shared target vector and per-iterate rational scale, with full-state hashes.
"""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json,argparse,time
import precision
import adaptive_theta as theta
import adaptive_readout as old_readout
import theta_oracle as old_theta
from precision import Context,Complex,parse_integer,decimal_integer
SOURCE_AT_IMPORT=Path(__file__).read_bytes()
U,V=F(7,12),F(7,24)
M={3:4,4:10,5:6}
OLD_PINS={'dyadic.py':'82e995ae9f67395980cec3f06bf493931de0413c7ce024562283882c01425170','theta_oracle.py':'c50857831de0fc5faa6829cf539c7d31dc32958b76412c27689235aeba95d2c1','adaptive_readout.py':'dc64e37cdadac8ffadaa666cdd0e6a0941580f89f3674817c803e8c89ee7e274'}

def choices(epsilon):
    if not isinstance(epsilon,F):raise TypeError('Positive exact Fraction tolerance required')
    if epsilon<=0:raise ValueError('Tolerance must be positive')
    degree=0
    while 10*V**(degree+1)/(1-V)>epsilon/8:degree+=1
    count=degree+1
    while 10*F(1,2**count)/(1-F(1,2**count))/(1-V)>epsilon/8:count+=1
    # A small deterministic alignment makes circle quadrants inspectable.
    count=8*((count+7)//8)
    return degree,count,epsilon*(1-U)/8

def fraction(row):return F(parse_integer(row['numerator']),parse_integer(row['denominator']))

def rectangle(ctx,row):
    def part(p):return ctx.bounds(F(parse_integer(p['lo']),1<<p['dyadic_bits']),F(parse_integer(p['hi']),1<<p['dyadic_bits']))
    return Complex(part(row['real']),part(row['imag']))

def fourier(rows,degree,bits):
    if type(degree) is not int or degree<0 or not isinstance(rows,(tuple,list)) or not rows:raise ValueError('Nonempty circle and nonnegative integer degree required')
    if type(bits) is not int or bits<32:raise ValueError('Integer Fourier precision >=32 required')
    count=len(rows);ctx=Context(bits)
    if degree>=count or any(r['target_kind']!='true_circle_node' or r['node_index']!=j or r['node_count']!=count or r['q']!=rows[0]['q'] for j,r in enumerate(rows)):raise ValueError('Complete ordered homogeneous circle required')
    labels=[ctx.complex(r['center_real'],r['center_imag']) for r in rows]
    roots=[rectangle(ctx,r['root_box']) for r in rows];roots=[Complex(z.re,-z.im) for z in roots]
    powers=[ctx.complex(1) for _ in rows];bounds=[]
    for n in range(degree+1):
        bounds.append(sum((labels[j]*powers[j] for j in range(count)),ctx.complex(0))/count)
        powers=[a*b for a,b in zip(powers,roots)]
    return tuple(bounds)

def state_hash(state):
    text=';'.join(','.join(decimal_integer(x.numerator)+'/'+decimal_integer(x.denominator) for x in pair) for pair in state)
    return hashlib.sha256(text.encode('ascii')).hexdigest()

def compressed_train(targets,residual_budget):
    trace=old_readout.train(targets,residual_budget)
    anchor=next(((n,j) for n,pair in enumerate(targets) for j,x in enumerate(pair) if x),None)
    result=[]
    for row in trace:
        state=row['coefficients'];scale=state[anchor[0]][anchor[1]]/targets[anchor[0]][anchor[1]] if anchor else F()
        assert all(x==scale*a and y==scale*b for (x,y),(a,b) in zip(state,targets))
        result.append({'iteration':row['iteration'],'coefficient_scale':scale,'objective':row['objective'],'residual':row['residual'],'coefficient_state_sha256':state_hash(state)})
    return result

def family(q,epsilon):
    theta.validate(q,epsilon);degree,count,eta=choices(epsilon)
    assert old_theta.growth_majorant(q)<M[q]
    bits=32*((max(128,eta.denominator.bit_length()-eta.numerator.bit_length()+64)+31)//32);attempts=[]
    while True:
        rows=[theta.circle(q,j,count,eta,initial_bits=bits) for j in range(count)]
        actual=max(r['bits'] for r in rows);bounds=fourier(rows,degree,actual+32)
        arithmetic=sum((b.radius()*U**n for n,b in enumerate(bounds)),F())
        attempts.append({'initial_bits':bits,'max_sample_bits':actual,'Fourier_bits':actual+32,'Fourier_radius_sum':arithmetic})
        if arithmetic<=epsilon/8:break
        # Regenerate nodes as well as samples: lifting fixed boxes alone cannot
        # remove their inherited uncertainty.
        bits=2*actual
    targets=[b.midpoint() for b in bounds];trace=compressed_train(targets,epsilon/4)
    w=F(1,2**count);eta_actual=max(r['radius'] for r in rows)
    parts={'oracle':eta_actual*(1-U**(degree+1))/(1-U),'alias':M[q]*w/(1-w)*(1-V**(degree+1))/(1-V),'Taylor':M[q]*V**(degree+1)/(1-V),'coefficient_arithmetic':arithmetic,'optimization':trace[-1]['residual']}
    B=max(32,epsilon.denominator.bit_length()-epsilon.numerator.bit_length()+8)
    while F(5,1<<B)>epsilon/8:B+=1
    def up(x):return F(-(-x.numerator*(1<<B)//x.denominator),1<<B)
    budget={k:up(x) for k,x in parts.items()};total=sum(budget.values(),F());assert total<=epsilon
    return {'q':q,'requested_tolerance':epsilon,'degree':degree,'sample_count':count,'requested_sample_error':eta,'compact_radius':F(7,10),'circle_radius':F(6,5),'growth_radius':F(12,5),'growth_integer_bound':M[q],'growth_exact_majorant':old_theta.growth_majorant(q),
        'sample_precision_attempts':attempts,'samples':rows,'targets':targets,'target_rectangles':[b.encode() for b in bounds],
        'gradient_step':F(1,4),'objective':'J(b)=1/2 sum_n |b_n-t_n|^2, rational Fourier-midpoint targets; true-root LS target perturbation explicitly budgeted',
        'trace_encoding':'Actual exact GD updates, lossless shared target vector times per-iterate extracted rational coefficient_scale; full exact coefficient_state_sha256. Not a closed-form-only training producer.',
        'trace':trace,'steps':len(trace)-1,'coefficients':[(trace[-1]['coefficient_scale']*x,trace[-1]['coefficient_scale']*y) for x,y in targets],
        'coefficient_basis':'((s-1/2)/(6/5))^n','budget':budget,'budget_rounding_bits':B,'compact_uniform_bound':total,
        'scope':'Requested-error construction for fixed q3/q4/q5 and fixed compact using classical theta/growth inputs. No runtime bound, all-conductor uniformity, quantum advantage, real-rootedness, Lean or GRH claim.'}

def run(output,epsilon,conductors=(3,4,5)):
    choices(epsilon)
    if not isinstance(output,Path):raise TypeError('Path output required')
    if output.exists():raise FileExistsError('Preserve previous experiment')
    if not isinstance(conductors,(tuple,list)) or not conductors or len(set(conductors))!=len(conductors):raise ValueError('Distinct supported conductors required')
    for q in conductors:theta.validate(q,epsilon)
    names=('precision.py','adaptive_theta.py','adaptive_family.py','adaptive_readout.py','theta_oracle.py','dyadic.py');sources={n:Path(__file__).with_name(n).read_bytes() for n in names}
    assert sources['precision.py']==precision.SOURCE_AT_IMPORT and sources['adaptive_theta.py']==theta.SOURCE_AT_IMPORT and sources['adaptive_family.py']==SOURCE_AT_IMPORT,'Loaded/new source snapshot mismatch'
    assert all(hashlib.sha256(sources[n]).hexdigest()==h for n,h in OLD_PINS.items()),'Accepted historical source changed'
    output.mkdir(parents=True)
    for n,b in sources.items():(output/n).write_bytes(b)
    readouts=[];started=time.monotonic()
    try:
        for q in conductors:
            readouts.append(family(q,epsilon));r=readouts[-1]
            print(json.dumps({'q':q,'degree':r['degree'],'nodes':r['sample_count'],'updates':r['steps'],'bound':float(r['compact_uniform_bound']),'seconds':round(time.monotonic()-started,3)}),flush=True)
        assert all(Path(__file__).with_name(n).read_bytes()==b for n,b in sources.items()),'Source changed during run'
        result={'readouts':readouts,'source_sha256':{n:hashlib.sha256(b).hexdigest() for n,b in sources.items()},'sample_oracle_validated':True,'coefficient_certificate':True,'new_Lean_declarations':0,'GRH_proved':False}
        (output/'family-certificates.json').write_text(json.dumps(theta.encode(result),indent=2)+'\n')
    except Exception as error:
        (output/'failure.json').write_text(json.dumps({'error_type':type(error).__name__,'error':str(error),'completed_families':len(readouts),'coefficient_certificate':False},indent=2)+'\n');raise

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path,required=True);p.add_argument('--tolerance',type=F,required=True);p.add_argument('--q',action='append',type=int);a=p.parse_args();run(a.output,a.tolerance,tuple(a.q or(3,4,5)))
