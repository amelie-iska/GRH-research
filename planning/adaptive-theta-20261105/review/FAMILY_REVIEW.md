# Independent end-to-end adaptive family acceptance

5 November 2026, remote-only on iska-linux-vscode. The reviewer wrote only the
assigned new planning/output review namespaces. Existing data, environments,
producer files, historical certificates and publication targets were preserved.
No dependencies, GPU/model work, authentication, MCP activation, production
writes or publishing were used for this review.

## Accepted object and final source

Accepted: examples/analytic_oracle/adaptive_family.py, SHA256
b87cdabcbf701fd8c98cbaef3cfa507d843247fe854f8ba47652f0c25a0a0a56,
and the final experiment outputs/experiments/2026-11-05-adaptive-family-1e-24-final-v2/.
Its family-certificates.json has SHA256
e69f6d1bf99d6642ff0157d860c4ccac3b5d9bb37ba7bb2bd5b086633c384b01.
All six copied producer sources match their recorded hashes; accepted fixed
sources dyadic.py, theta_oracle.py and adaptive_readout.py retain their old
independently reviewed pins. The sampler acceptance is recorded separately in
REVIEW.md and sampler-final-acceptance.json.

This implements a requested-error approximation algorithm for the three fixed
primitive quadratic completed Dirichlet functions, on the fixed compact
abs(s-1/2)<=7/10. Mathematical finite termination assumes unbounded resources
and the explicitly inherited primitive theta/Mellin identity and accepted
conductor-specific growth proof. Practical extreme-tolerance runtime is not
claimed. Unlike the earlier fixed-label readout, the new driver selects new
sample truncations/precision, sample-circle size, degree, Fourier arithmetic
and optimization stopping point. No general-conductor, zero-location,
positive arithmetic determinant, real-rootedness, quantum advantage, Lean or
GRH result follows.

The four production proof files were read in full and agree with the accepted
source semantics: papers/adaptive-theta-core.tex, adaptive-theta-details.tex,
adaptive-family-core.tex and adaptive-family-details.tex. Their exact hashes
are bound in final-acceptance.json. The corrected details distinguish entry
refusals without artifacts from uncertified failure metadata written after an
output directory has been created.

## Analytic and arithmetic construction

Let u=7/12 and v=7/24. The driver chooses degree d with
10*v^(d+1)/(1-v)<=epsilon/8 and m>d with
10*2^-m/((1-2^-m)*(1-v))<=epsilon/8, then rounds m upward to a multiple of8.
The accepted exact growth constants Mq=4,10,6 remain valid. The requested
sample error is eta=epsilon*(1-u)/8. All m actual circle nodes and labels are
new certified samples. The actual maximum sample radius contributes
eta_actual*sum(u^n,n=0..d), which is at most epsilon/8.

Outward Fourier rectangles enclose the exact true-root DFT of the rational
sample midpoint labels. Their midpoint perturbation contributes
sum(radius1(Bn)*u^n), accepted only at epsilon/8 or less. This term concerns
finite coefficient arithmetic and node uncertainty. It does not omit or
absorb the analytic sample error. If it is too large the driver regenerates
all nodes and samples at higher precision; it does not just relabel a fixed
box with more bits. For fixed finite d,m, shrinking primitive/node widths and
continuity give termination of this additional retry.

The exact rational loop trains J(b)=1/2 sum abs(b_n-t_n)^2 for the rational
Fourier-midpoint target vector t, from zero with gradient step1/4. Its real
Euclidean gradient is b-t. It stops at the first state with weighted L1
residual sum(abs(b_n-t_n)_1*u^n)<=epsilon/4. The true-circle least-squares
target differs from t by the already budgeted sample and rectangle errors;
the code does not claim to execute that different ideal target trajectory.

The producer calls the accepted actual vector-update loop. After execution,
it extracts each state's exact common scale relative to t, checks every
coordinate, and stores that scale, objective, residual and canonical full-
state hash. All states are recovered exactly from this lossless encoding.
The mathematical recurrence and exact reconstruction establish this claim;
the hash is an integrity aid. A zero target vector has the single zero state.

Oracle, alias, Taylor and coefficient-arithmetic allocations are each at most
epsilon/8; optimization is at most epsilon/4. The raw sum is at most
3epsilon/4. Upward rounding of the five separately reported components at a
request-dependent scale B with5*2^-B<=epsilon/8 gives a literal exact sum at
most7epsilon/8. The actual exported polynomial uses the normalized basis
((s-1/2)/(6/5))^n. Every source and output endpoint remains exact rational;
decimal display projections are not proof inputs.

## Independent final-v2 evidence

check_family_exact.py imports neither the producer nor its arithmetic. It
rebuilds integer outward rectangle operations, all264 sample component
certificates, all147 Fourier rectangles/targets, exact growth majorants,
all five raw and rounded readout terms, and all optimizer states. It performs
7157 checks. The three models have degree48 and88 samples each, with
196/197/197 executed updates, respectively. There are590 executed vector
updates,593 complete recorded states and29057 recorded complex coefficient
states. Every state is independently generated by the recurrence, then
checked against its stored scale/hash/objective/residual and first-stop test.
No closed-form state producer is imported by the checker.

Final exact uniform bounds:
q3:21/77371252455336267181195264
q4:63/154742504910672534362390528
q5:13/38685626227668133590597632
Each is strictly below the requested1e-24.

Exact receipt:
family-exact-2026-11-05-adaptive-family-1e-24-final-v2-1793883182627155551.json

check_family_diagnostics.py, using only the already installed mpmath1.4.1 at
130digits, passes1230 secondary diagnostic checks: all264 true roots/nodes
and independently evaluated completed-function values are inside their saved
enclosures; all147 exact-root DFT values of the rational midpoint labels are
inside the Fourier rectangles; and all144 compact-boundary comparisons fit
the global certificates. The maximum observed boundary errors are about
1.91e-25,2.49e-25,2.40e-25. These observations are diagnostics and do not
replace the larger exact uniform bounds or the analytic proof.

Diagnostic receipt:
family-diagnostics-2026-11-05-adaptive-family-1e-24-final-v2-1793883188481319222.json

check_family_guards.py passes279 controls including16 independently detected
mutations of degree, normalization, sample q/radius/budget, Fourier rectangle,
target, scale, objective, residual, full-state hash, stopping count/state,
final coefficient, reported component and total. It checks malformed inputs,
float/bool aliases, concrete nonempty rows, compressed zero/nonzero training,
all three stale-import source refusals, old-source pin refusal, source drift,
uncertified failure metadata and byte-preservation of existing outputs.

A forced wider but still valid first Fourier enclosure exercises the retry
path with actual theta evaluations. Every node/sample is generated again at
higher initial precision and the actual asymmetric root width strictly
shrinks; the final family remains certified. Source changes in guard tests
are simulated return values or temporary in-memory mocks, never file edits.

Guard receipt:
family-guards-1793883181709821595.json

All receipts reside in outputs/checks/2026-11-05-adaptive-theta/review/.
No unresolved correctness defect remains within the reviewed implementation,
proof and final certificate scope. The display/UI review and production
integration are separate from this scientific acceptance.
