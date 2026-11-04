# Independent review: hybrid measured-marginal diffusion and flow

Reviewed 2026-11-04, read only: `examples/learned_frontier/generative.py`,
`check_generative.py`, saved `generative-20261104-v1/record.json`, four checkpoint
files and `outputs/checks/2026-11-04-learned-frontier/generative-checks.json`.
Only this review is written by this reviewer. No SSH, GPU job, dependency change,
checkpoint load/execution, or production-source edit was performed.

**Verdict:** the physical teacher, noise-prediction oracle and conditional-flow
oracle are mathematically consistent with the stated finite hybrid experiment.
The experiment generates classical real vectors from a dequantized measured
two-spin marginal. It does not generate a coherent quantum state, reproduce a
full quantum flow-matching method, establish quantum advantage or speedup, or
address the arithmetic determinant/GRH bridge. The code's scope statements
correctly retain these distinctions. One important sampler qualification below
should remain visible in book/web prose.

## Teacher and retained observable

For m=5, label retained black spins0,1 and white spins2,…,6. The code implements

    H = −0.50 Z0 Σj Zj+2 −0.35 Z1 Σj (−1)^j Zj+2
        −0.12 Z0 +0.072 Z1 −Σj wj Zj+2 −0.55 Σq Xq,
    wj = 0.045 cos(1.7j)+0.02j/5,  β=1.

This is a transverse-field quantum spin Hamiltonian on the actual seven-vertex
clean-dessin incidence graph K_(2,5). Its ten incidence edges are not the five
edges of the contracted dessin, and it is not a faithful action of the infinite
order algebra. The genus-two description refers to the specified dessin
embedding, not a genus determined by an unembedded interaction matrix alone.

The matrix is real symmetric; the bit-flip entries implement each Xq with the
same most-significant-bit ordering as `spins`. Dense spectral decomposition and
normalized exp(−βE) give ρ=exp(−βH)/Tr exp(−βH). Subtracting the lowest energy
inside the softmax cancels upon normalization. With tensor ordering black0,
black1,then white spins, reshaping as (4,32,4,32) and summing `rho[a,i,b,i]`
is the correct partial trace. Taking its diagonal gives the four retained Z
outcome probabilities. This is exact finite-dimensional coarse graining up to
floating-point arithmetic; it is not a learned RG approximation.

I independently rebuilt all seven Pauli X and Z operators with NumPy Kronecker
products, constructed the 128×128 Hamiltonian, diagonalized it, and performed
the white trace by explicit sums over32 indices. The maximum difference from
the saved reduced density is **2.04×10⁻¹⁰**; the maximum difference from the saved
float32 probabilities is **7.41×10⁻⁹**. This uses ideal float64 scalar coefficients;
the source mixes integer/default-float ramp arithmetic with float64 fields, so
bit-identical coefficient evaluation is not asserted. An initially stricter
2×10⁻¹² comparison did not pass; the reported errors, rather than a claim of
bitwise agreement, describe the actual independent evidence.

The saved retained state is positive with minimum eigenvalue0.0806414323 and
off-diagonal Frobenius norm0.3005508454. Its distribution is approximately
(0.30372509,0.26505437,0.17706090,0.25415963). These probabilities alone cannot
recover that density matrix. The checker explicitly conjugates the state by
Z⊗I and obtains a different coherent state with the same diagonal. Thus even a
perfect sampler of the target distribution would not establish tomography or
recovery of coherence.

The displayed channel Dt(ρ)=e^(−t)ρ+(1−e^(−t))I4/4 is a valid global two-qubit
depolarizing CPTP semigroup for t≥0. It is an illustrative quantum channel with
stationary state I4/4, not a Gibbs-preserving thermalization of this H, the reverse
diffusion sampler, or a learned coherent denoiser.

## Diffusion oracle: checked by conditional Gaussian expectation

Let S∈{±1}² have probabilities p, ξ,Z be independent standard normal vectors,
σ=0.2 and X0=S+σξ. For cumulative diffusion coefficient a=ᾱk,

    Xk=√a X0+√(1−a) Z,
    Xk | S=s ~ Normal(√a s, vk I),  vk=aσ²+1−a.

All mixture components have the same variance, so the posterior responsibility
is softmax(log p_s−||x−√a s||²/(2vk)); its common determinant normalization
cancels. Gaussian conditioning gives

    E[Z | Xk=x,S=s] = √(1−a) (x−√a s)/vk.

Averaging over the responsibilities gives exactly the implementation's oracle
noise predictor. Equivalently, it equals −√(1−a)∇x log pk(x). The training target
is the actual forward-noise vector, so mean squared loss has this population
conditional expectation as its minimizer. The empirical16,384-sample training
pool has a different finite empirical conditional law; comparison against the
population oracle is an informative separate metric, not an assertion that its
irreducible held-out loss vanishes.

**Sampler qualification:** the generation loop is the usual approximate Gaussian
ancestral DDPM update with mean defined by the predicted noise and variance

    β̃k = βk (1−ᾱk−1)/(1−ᾱk).

Even with the exact oracle, this is generally **not** the exact reverse transition
of this non-Gaussian mixture. Conditioned additionally on X0, the forward Gaussian
posterior has mean ck X0+dk Xk and covariance β̃k I, where
ck=√ᾱk−1 βk/(1−ᾱk). After integrating out X0, its true covariance contains

    β̃k I + ck² Cov(X0 | Xk),

and its distribution is generally non-Gaussian. The implemented transition uses
the conditional mean and only the first covariance term. At k=1 the injected
variance is zero and exact-oracle output is E[X0|X1], rather than a draw from
the full posterior. The near-Gaussian terminal initialization is also an
approximation for finite schedule length. Consequently the oracle sampler
control measures reverse-kernel approximation, finite schedule effects and
Monte Carlo error; it is not an exact teacher sampler with only model error
removed. The source's broad phrase "sampler/time-discretization error" is
compatible with this, but "exact oracle samples" would overstate the result.

## Flow oracle: checked by conditional Gaussian regression

The flow training coupling is independent endpoints:

    X1=S+σξ, X0=Z, Xt=(1−t)Z+tX1, V=X1−Z.

Conditioned on S=s, Xt has mean ts and variance
vt=(1−t)²+t²σ². Its covariance with V is
ct=tσ²−(1−t), while E[V|S=s]=s. Thus

    E[V | Xt=x,S=s] = s+(ct/vt)(x−ts).

Averaging against softmax(log p_s−||x−ts||²/(2vt)) produces exactly the code's
flow oracle. This derivation directly checks its sign, variance, dequantization
term and endpoint convention. In particular, v0(x)=E[S]−x and v1(x)=x for
this coupling; σ>0 makes both endpoint formulas regular. The learned field is a
classical velocity field in R². `generate` uses an explicit128-step Heun solver;
the oracle control still has finite numerical-integration and sample error.

There is no mismatch between interpolation direction and generation direction:
t=0 is the standard Gaussian base and t=1 is the dequantized measured target.

## Circuit and independent checks

The feature map starts in |0000>, applies input-dependent Ry then Rz gates in
two layers, and optionally an ordered ring of four CNOTs after each layer.
`apply_gate` respects its stated tensor ordering; indexing with each CNOT's
permutation implements that self-inverse gate. The15 observables are all
nonidentity diagonal Z products, with masks indexed by least-significant bits.
This ordering need not coincide with the gate qubit label ordering, but the
complete mask set and independent literal implementation agree.

The product ablation retains the same circuit parameters and neural network
dimensions and removes just the CNOT ring. The full hybrid has5,810 nominal
trainable parameters, including a classical encoder/head; quantum circuit
parameters are a small subset. Some final diagonal phase parameters are
unobservable under this diagonal readout, so nominal parameter matching is not
a proof of equal effective expressivity. In either architecture the exact
features are evaluated by classical Torch statevector arithmetic on the GPU;
the experiment is not hardware quantum execution. The final samples remain
classical vectors, even when the intermediate four-qubit feature state is
entangled.

The saved checker independently builds dense NumPy tensor-product gate matrices
and explicit CNOT action. Its recorded CUDA results are:

- Circuit maximum errors3.11×10⁻⁷ and5.76×10⁻⁷ for product/entangled variants.
- Autograd versus finite-difference discrepancies1.16×10⁻⁴ and1.59×10⁻⁴.
- Six independent mixture-log-density/oracle checks, maximum4.16×10⁻⁷.
- Depolarizing semigroup error2.79×10⁻¹⁷; bit-index regression passes.

These saved execution results were inspected, not rerun by this reviewer:
the existing local scientific environment has NumPy/SymPy but no Torch. No
dependency was installed to bypass that limitation. The independent NumPy
teacher reconstruction above was run locally and freshly. All four checkpoint
SHA256 values also match the actual checkpoint files; untrusted Torch pickle
loading was unnecessary for those integrity checks.

## What the four recorded runs establish

The saved record reports RTX4090, Torch2.8.0+cu128, seed20261104,2,000 optimizer
steps, batch512,16,384 training draws,4,096 held-out draws and4,096 generated
samples per run. Source code and records agree on these sizes and5,810 parameters.

| model | oracle-field MSE | measured TV | empirical sliced W1 |
|---|---:|---:|---:|
| diffusion/product |0.01118|0.02728|0.04271|
| diffusion/entangled |0.00971|0.03044|0.07930|
| flow/product |0.02077|0.01443|0.04100|
| flow/entangled |0.02192|0.01467|0.03721|

The independent target-sampling control has measured TV0.00709 and sliced
W1≈0.01654; these metrics have a nonzero sampling floor. The diffusion oracle
control has TV0.00832 and sliced W1≈0.02854; the flow oracle control has
TV0.01105 and sliced W1≈0.01827. Different metrics favor different variants.
Entangled diffusion improves the field MSE but worsens TV and sliced W1 on
this run. The tiny flow TV difference does not establish a performance ranking.
One seed, a product-circuit ablation and these small empirical discrepancies
support no statistical, computational or quantum advantage claim. Wall times
are experiment timings, not an asymptotic speedup comparison.

`sliced_W1_16directions` is a finite-direction empirical projected distance against
a fresh independent target draw, not the full multidimensional Wasserstein
distance or a certified transport bound. `dequantization_MSE` measures squared
distance from each coordinate's nearest ±1 center; it is not denoising target
MSE. At σ=0.2 its teacher scale is nearσ²=0.04. Thresholded generated samples
are compared with the original spin probabilities; Gaussian dequantization can
flip signs, but its two-coordinate union bound is2Φ(−5)<5.74×10⁻⁷, negligible
relative to the observed sampling errors. The training and held-out pools are
independent draws, although their discrete spin outcomes can of course repeat.

The population marginal, its exact finite teacher, finite circuit differentiation
and actual GPU training are useful concrete evidence. Coherent quantum state
generation, full quantum RG equivalence, general quantum flow matching,
infinite-width behavior, HMS, anabelian reconstruction and GRH remain outside
the conclusions of this experiment.
