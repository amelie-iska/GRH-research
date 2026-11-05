"""Requested-tolerance readouts from immutable validated Dirichlet labels.

The literal rational GD trace trains a Fourier-midpoint quadratic objective.
It is NOT a replay of upstream neural/quantum training, nor an arbitrary-
accuracy theta oracle. All mathematical endpoints use Fraction, not floats.
"""
from fractions import Fraction as F
from pathlib import Path
from functools import lru_cache
import argparse
import hashlib
import json
from dyadic import R, C, real, complex_box, BITS

ROOT = Path(__file__).resolve().parents[2]
FROZEN = ROOT / 'outputs/experiments/2026-11-04-validated-oracle-final-v5/oracle-certificates.json'
FROZEN_SHA = '85e3bed76ad4067084ab5f8413b7159e4c5169e5d7cef0469d36164e82dfbca8'
DYADIC_SHA = '82e995ae9f67395980cec3f06bf493931de0413c7ce024562283882c01425170'
M = {3: 4, 4: 10, 5: 6}
U, V, W = F(7, 12), F(7, 24), F(1, 2**64)

class ToleranceNotCertified(ValueError):
    def __init__(self, floor):
        self.floor = floor
        super().__init__('Requested tolerance not certified by this fixed-label budget; minimum base budget=' + str(floor))

def fraction(value):
    return F(int(value['numerator']), int(value['denominator']))

def encode(value):
    if isinstance(value, F):
        try:
            display = float(value)
        except OverflowError:
            display = None
        return {'numerator': str(value.numerator), 'denominator': str(value.denominator), 'display': display}
    if isinstance(value, dict):
        return {k: encode(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [encode(v) for v in value]
    return value

def load_frozen(path=FROZEN):
    data = Path(path).read_bytes()
    if hashlib.sha256(data).hexdigest() != FROZEN_SHA:
        raise ValueError('Frozen certificate hash mismatch')
    if hashlib.sha256(Path(__file__).with_name('dyadic.py').read_bytes()).hexdigest() != DYADIC_SHA:
        raise ValueError('Reviewed dyadic source hash mismatch')
    return json.loads(data)

def rectangle(value):
    def component(c):
        if c['dyadic_bits'] != BITS:
            raise ValueError('Unexpected interval scale')
        return R(int(c['lo']), int(c['hi']))
    return C(component(value['real']), component(value['imag']))

@lru_cache(maxsize=3, typed=True)
def fourier(q):
    validate(q, F(1))
    data = load_frozen()
    rows = sorted((s for s in data['samples'] if s['q'] == q), key=lambda s: s['node_index'])
    if len(rows) != 64 or any(s['node_index'] != j or s['node_count'] != 64 for j, s in enumerate(rows)):
        raise ValueError('Complete ordered64-node conductor required')
    labels = [C(real(fraction(s['center_real'])), real(fraction(s['center_imag']))) for s in rows]
    roots = [rectangle(s['root_box']) for s in rows]
    roots = [C(z.re, -z.im) for z in roots]
    powers = [complex_box(1) for _ in rows]
    bounds = []
    for n in range(64):
        bounds.append(sum((labels[j] * powers[j] for j in range(64)), complex_box(0)) / 64)
        powers = [z * root for z, root in zip(powers, roots)]
    return tuple(bounds), max(fraction(s['radius']) for s in rows)

def validate(q, epsilon):
    if type(q) is not int or q not in M:
        raise ValueError('Only integer conductors3,4,5 supported')
    if not isinstance(epsilon, F):
        raise TypeError('Requested error must be an exact Fraction')
    if epsilon <= 0:
        raise ValueError('Requested error must be positive')

def base_budgets(bounds, eta, q, degree):
    return {
        'oracle': eta * (1 - U**(degree + 1)) / (1 - U),
        'alias': M[q] * W / (1 - W) * (1 - V**(degree + 1)) / (1 - V),
        'Taylor': M[q] * V**(degree + 1) / (1 - V),
        'coefficient_arithmetic': sum((b.radius() * U**n for n, b in enumerate(bounds[:degree + 1])), F()),
    }

def train(targets, residual_budget):
    """Execute exact updates for J(b)=1/2 sum |b_n-target_n|^2.

    This objective is explicitly the rational Fourier-midpoint objective.
    Its target perturbation from true-root LS is budgeted separately.
    """
    if not isinstance(residual_budget, F) or residual_budget <= 0:
        raise ValueError('Positive exact residual budget required')
    if not isinstance(targets, (list, tuple)) or not targets or any(not isinstance(t, (list, tuple)) or len(t) != 2 or any(not isinstance(x, F) for x in t) for t in targets):
        raise TypeError('Nonempty exact rational complex targets required')
    state = [(F(), F()) for _ in targets]
    trace = []
    while True:
        differences = [(x - a, y - b) for (x, y), (a, b) in zip(state, targets)]
        residual = sum(((abs(x) + abs(y)) * U**n for n, (x, y) in enumerate(differences)), F())
        objective = sum((x*x + y*y for x, y in differences), F()) / 2
        trace.append({'iteration': len(trace), 'coefficients': state, 'objective': objective, 'residual': residual})
        if residual <= residual_budget:
            return trace
        state = [((3*x + a)/4, (3*y + b)/4) for (x, y), (a, b) in zip(state, targets)]

def certify(data, q, epsilon):
    validate(q, epsilon)
    # Pin the supplied data as well as the independent disk loader: callers
    # cannot replace label radii while borrowing the frozen provenance claim.
    if data != load_frozen():
        raise ValueError('Input differs from reviewed frozen certificate')
    bounds, eta = fourier(q)
    bases = [base_budgets(bounds, eta, q, d) for d in range(64)]
    totals = [sum(b.values(), F()) for b in bases]
    floor_degree = min(range(64), key=lambda d: totals[d])
    eligible = [d for d in range(64) if totals[d] < epsilon]
    if not eligible:
        raise ToleranceNotCertified(totals[floor_degree])
    degree = eligible[0]
    targets = [(b.re.midpoint(), b.im.midpoint()) for b in bounds[:degree + 1]]
    trace = train(targets, epsilon - totals[degree])
    budget = dict(bases[degree], optimization=trace[-1]['residual'])
    total = sum(budget.values(), F())
    assert total <= epsilon
    return {
        'q': q, 'requested_tolerance': epsilon, 'sample_count': 64,
        'degree': degree, 'steps': len(trace) - 1, 'gradient_step': F(1,4),
        'objective': 'J(b)=1/2 sum_n |b_n-t_n|^2; rational Fourier-midpoint targets t, real Euclidean gradient b-t',
        'original_gradient_relation': 'True-circle label LS optimum lies in B_n; gradient perturbation <= radius1(B_n). This is not its exact optimizer trajectory.',
        'coefficient_basis': '((s-1/2)/(6/5))^n', 'compact_radius': F(7,10),
        'targets': targets, 'target_rectangles': [b.encode() for b in bounds[:degree + 1]],
        'trace': trace, 'coefficients': trace[-1]['coefficients'], 'budget': budget,
        'compact_uniform_bound': total, 'minimum_base_budget': totals[floor_degree],
        'minimum_base_degree': floor_degree, 'all_degree_base_budgets': totals,
        'input_certificate_sha256': FROZEN_SHA,
        'scope': 'Fixed q3/4/5 and frozen64-circle labels. Exact rational executed surrogate GD plus validated target perturbation. Not arbitrary-accuracy sampling, quantum advantage, zero-location, GRH or Lean.'
    }

def run(output, epsilon):
    if not isinstance(output, Path):
        raise TypeError('Path output required')
    validate(3, epsilon)
    if output.exists():
        raise FileExistsError('Preserve previous output')
    names = ['adaptive_readout.py', 'dyadic.py']
    source = {n: Path(__file__).with_name(n).read_bytes() for n in names}
    data = load_frozen()
    results = [certify(data, q, epsilon) for q in M]
    assert all(Path(__file__).with_name(n).read_bytes() == b for n, b in source.items()), 'Source changed during run'
    output.mkdir(parents=True)
    for n, b in source.items():
        (output/n).write_bytes(b)
    record = {'readouts': results, 'source_sha256': {n: hashlib.sha256(b).hexdigest() for n, b in source.items()},
              'input_certificate_sha256': FROZEN_SHA, 'GRH_proved': False, 'new_Lean_declarations': 0}
    (output/'readout-certificates.json').write_text(json.dumps(encode(record), indent=2)+'\n')
    print(json.dumps([{'q': r['q'], 'degree': r['degree'], 'steps': r['steps'], 'bound': float(r['compact_uniform_bound'])} for r in results]))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--tolerance', type=F, required=True)
    args = parser.parse_args()
    run(args.output, args.tolerance)
