# Independent computational and QNN review

2026-11-03. Read-only independent review, except for this requested report. No source, model, experiment output, environment, cache, web asset or manuscript was changed. No dependency was added. The new isolated CPU environment already existed and was authorized before this review.

## Scope and result

Reviewed `examples/quantum/surface_models.py`, `train_renormalization.py`, `train_pennylane.py`, `train_photonic.py`, `backend_adapters.py`, saved experiment JSON in the three renormalization/photonic output directories, `web/app.js`, and the types and proofs of `lean-analytic/BookInterfaces.lean`. Read the corresponding focused Lean log. This is not an independent rereading of the entire book or an experimental hardware validation. Newly added ToricGT hybrid code, if any, is outside this snapshot.

The three finite qubit experiments have valid target equations and updates under their stated assumptions. Their saved results support a successful small CPU training demonstration. There is no basis here for quantum advantage, a Wilson RG fixed point, a faithful representation of a completed surface order, or a GRH proof. One concrete photonic description needs correction, and the checkpoint visualization needs a final-weight label; both were reported to the parent before this report.

Snapshot SHA256 values:

| Source | SHA256 |
|---|---|
| surface_models.py | d2bb5105d86cb45113d98298d73dc2c7fd3b5fd53095ffcfdd464547da6bbae0 |
| train_renormalization.py | 9d11cd8ce3fbb9bea84652b548355e4c2d64c9714e3c721fb98c96651b5c387b |
| train_pennylane.py | 1ac311fd9f191705d6d2a385fb562990a97178b4fe232fea382a38845f549061 |
| train_photonic.py | 136876a01383e47ea1f711ae51fce1f841c0f08e7ff4efeadaf914c559f5436c |
| backend_adapters.py | 05176361d70421a4a0de194837716a8fddedf321c93e6f7f64f276d922715634 |

## Exact target derivations

### Chain decimation

Summing a central spin s in a zero-field three-site Ising chain gives

    W(s1,s2) = 2 cosh(K1 s1 + K2 s2).

The effective coefficient is

    K_eff = (1/2) log(cosh(K1+K2)/cosh(K1-K2))
          = atanh(tanh(K1) tanh(K2)).

A spin-independent constant is also present; the regression experiment explicitly predicts the coupling, not the entire partition function. The code's positive coupling domain lies strictly inside the finite atanh domain. No field or longer-range interaction is silently incorporated.

### Star-to-triangle decimation

After summing one hidden spin coupled to three boundary spins, set

    L(s1,s2,s3) = log(2 cosh(K1 s1+K2 s2+K3 s3)).

Global spin-flip invariance removes odd Walsh coefficients. With only three spins, the remaining expansion is exactly

    L = C + J12 s1 s2 + J23 s2 s3 + J20 s3 s1,
    Jij = (1/8) sum_s L(s) si sj.

These are precisely the three target columns computed by the attention experiment. No missing three-body term occurs in this zero-field three-boundary-spin case. A nonzero hidden field or more boundary spins would require different targets.

Independent random tests, with review seed 1703, reconstructed 100 star logweights with maximum residual 4.440892098500626e-16 and 100 chain logweights with maximum residual 8.881784197001252e-16. Those finite tests corroborate the displayed uniform algebraic identities.

## Gradients, circuits and backend agreement

Each trainable coordinate of `ansatz` occurs in exactly one Ry or Rz gate. Its generator has eigenvalues ±1/2. The ordinary two-term parameter shift with offsets ±pi/2 therefore gives the exact derivative of each expectation. The convolution loss correctly applies the chain rule through its affine readout; its affine-head gradients also have the correct mean normalization. The QCNN loss is a linear expectation, so shifting its loss expectation is valid directly. The nonlinear attention objective uses central finite differences of the complete objective, rather than incorrectly applying a simple parameter-shift formula to softmax or squared loss.

I independently compared every circuit parameter's shifted derivative to a central finite difference at nontrivial random complex input states:

| Circuit | Maximum difference |
|---|---:|
| n=2, all 8 parameters | 2.1746232592434467e-10 |
| n=4, all 16 parameters | 1.422473458467799e-10 |

`reduced_keep` reshapes the pure state as a bipartite coefficient matrix and returns A A*, the correct partial trace over the final wires. The QCNN probability projector selects the final two qubits in 00 under the stated most-significant-first convention.

The PennyLane experiment genuinely executes state preparation, unitary evolution and expectation evaluation through `default.qubit`. It builds the unitary matrix with the shared NumPy helper and uses manually shifted/finite-difference gradients; it does not claim native PennyLane autograd or a hardware-compiled gate training run. That distinction should remain in the computational chapter.

The NumPy and PennyLane histories agree closely with identical seed and function-call order:

| Architecture | Max history difference | Max final parameter difference |
|---|---:|---:|
| Four-qubit compression | 4.64e-14 | 6.47e-9 |
| Shared convolution | 1.61e-15 | 1.27e-10 |
| Quantum-feature attention | 3.70e-10 | 1.98e-5 |

Do not assert bit-identical attention checkpoints. Finite-difference noise and flat directions give a modest parameter discrepancy while the reported losses agree. The saved actual PennyLane checkpoint is the proper artifact for its run.

## Data splits and experimental meaning

Training and held-out indices are disjoint. The updates use only training indices; held-out losses are logged but do not enter gradients or a checkpoint-selection rule. Epoch counts and hyperparameters are fixed in the code. I found no test-split gradient leakage. The global RNG seed and function call order jointly determine the generated data and initializations, so reproducibility requires the whole declared run order, not an isolated function call after arbitrary RNG consumption.

PennyLane final results:

| Architecture | Final train loss | Final held-out loss | Constant held-out baseline |
|---|---:|---:|---:|
| Four-qubit compression | 0.2145898748 | 0.2397254998 | not supplied |
| Shared convolution | 0.0001507875 | 0.0001258965 | 0.1179650153 |
| Quantum-feature attention | 0.0018387291 | 0.0020447710 | 0.0582155469 |

The QCNN loss is discarded-register failure probability. Its final held-out error is about 24%; report the substantial residual rather than suggesting lossless compression. The four-spin ring is an auxiliary finite TFIM benchmark; by itself it is not the quiver of the infinite theta or elliptic-square order, nor a cellular torus dessin. Any identification with a particular order representation needs an explicit carrier/action map. Current broad finite-model disclaimers are appropriate.

The graph convolution is a shared two-qubit patch feature map with a classical affine coupling readout. The graph attention model aggregates three shared edge-pair features on a labelled star. These are meaningful small hybrid architectures; they do not yet train a scalable message-passing network on arbitrary dessins. Only positive-coupling, zero-field in-distribution generalization is measured. No matched classical MLP/kernel ablation, multiple-seed confidence interval, shot/noise robustness or quantum advantage study was conducted. Retain those limitations.

## Strawberry Fields

The Gaussian circuit prepares two opposite squeezings and applies consecutive real beamsplitters with total angle alpha=source_angle+theta. In the stated hbar=2 convention,

    Var(x0)+Var(p1)
      = 2 [exp(-2r) cos(alpha)^2 + exp(2r) sin(alpha)^2].

Its minima occur at theta=-source_angle modulo pi. The reported optimum -0.47 is the chosen minimum in the trained basin. The saved final angle differs from that value by 8.565370634983083e-13, and held-out objectives match 2 exp(-2r) to numerical precision.

**Description correction:** the reviewed script docstring says "retained output momentum variance plus discarded output position variance." Its actual covariance indices 0,0 and 3,3, in order x0,x1,p0,p1, are output-0 position plus output-1 momentum. Keep the calculation and change the description. The optimizer trains a one-parameter Gaussian principal-axis layer, not an interacting RG fixed point or a deep photonic neural network. The script measures its pooling proxy; it does not explicitly reconstruct a reduced-output covariance dataset. Such an output would be useful if claiming a complete learned Gaussian channel interface.

## Independent SDK execution

I freshly invoked `run` from the adapter module in the approved isolated environment for the four available CPU SDKs. It uses Fourier preparation before clock/shift, so this is not the vacuous clock-on-|0> test.

| Backend | Comparison error |
|---|---:|
| Cirq 1.4.1 | 0.0 |
| Qiskit 1.3.3 | 0.0 |
| PennyLane 0.40.0 | 0.0 |
| Strawberry Fields 0.23.0 | 5.078117559639666e-16 |

The SF comparison uses the full one-photon density block, including off-diagonal phases, and agrees with the same four-level carrier. It correctly handles SF returning a density state after Fock preparation. Passive photon-number-preserving gates stay inside that one-photon sector at cutoff 2. The nonfatal pkg_resources deprecation warning is an environment compatibility notice, not a simulation failure.

cuQuantum/CUDA-Q adapters were read but not executed. No CUDA/GPU capability or successful GPU run is certified here. Backend-specific gate ordering, target selection and version compatibility still need tests on an appropriate supported local machine. A source fork/clone is not a trained GPU experiment.

## Web and formalization boundaries

The AR selector labels module, stable, smooth-support and quotient categories separately and does not relabel the HLS grid as a derived AR component. Its signed central HLS window and node text agree with the reviewed constructions. The clock display computes the expected finite carrier phases: after U^k followed by V^l, basis index j has phase zeta^(k(j-l)); all probabilities remain 1/d. The higher-genus view is explicitly a branched-sheet projection; it must not be called an injective 3D embedding or a uniformization metric.

**Visualization correction:** the checkpoint slider changes loss history, but the example record always uses final trained parameters. Label examples "final weights" rather than implying that the displayed prediction came from the selected checkpoint. Genuine per-checkpoint prediction controls require storing the parameter history or recomputing from a checkpoint.

The eight BookInterfaces Lean statements have the stated actual matrix types. In particular, `kraus_pool_positive` proves positivity of a finite rectangular Kraus sum, and `kraus_pool_trace` proves trace preservation under the explicit completeness premise. They do not by themselves formalize the trained parameters, all tensor ampliations of complete positivity, the partial-trace Python implementation, the general AR theory, continuum QFT or the arithmetic GRH comparison. The focused log has exit code 0 and only standard foundational axiom dependencies. I read the proof types and log; I did not rerun the full analytic suite in this independent pass.

## Recommended disposition

Accept the finite training and four CPU backend demonstrations with the scopes above, after the two description/visualization fixes. Keep the actual PennyLane checkpoints, generated inputs reproducible from seed/order, complete curves, final predictions and baseline values. A future stronger learning claim needs matched classical ablations, multiple independent seeds, held-out surface families, shot/noise tests, and an explicit exact-certificate interface. Learned proposals can guide research; none of these losses supplies the missing arithmetic determinant theorem.

## Additional review: finite ToricGT hybrid and exact certificate repair

Reviewed the later `examples/quantum/toricgt_hybrid.py` snapshot SHA256 `208bccbd86503ff0f38dacfb14f4984008d70574ebc86e48faff8c0baeaff81e` and its saved `outputs/experiments/toricgt-hybrid/training.json`. This additional pass changed only this report. It imported the module without invoking its `main`, so training outputs were not overwritten.

The actual upstream ToricGT clone is clean at `a5199bc989a6fb170e21220e5e87bf95bc2fc0b4`, matching `book/toricgt-pins.json` and the experiment metadata. Its shift is the downward shift, giving VU=i UV at theta=1/4. This differs from the forward-shift convention of `surface_models.clock_shift`, where UV=i VU. The adapter checks the actual upstream relation rather than conflating the two conventions.

The finite real Hermitian target is

    H(lambda) = [[2,lambda,0,lambda],
                 [lambda,0,lambda,0],
                 [0,lambda,-2,lambda],
                 [lambda,0,lambda,0]].

This example is exactly soluble. In the orthonormal basis

    w=(e0+e2)/sqrt(2), z=(e0-e2)/sqrt(2),
    u=(e1+e3)/sqrt(2), v=(e1-e3)/sqrt(2),

one has Hw=2z+2lambda*u, Hz=2w, Hu=2lambda*w and Hv=0. Therefore

    char_H(t) = t^2 (t^2-4(1+lambda^2)),
    E_min(lambda) = -2 sqrt(1+lambda^2).

An independent symbolic determinant check agreed. This is a useful analytically controlled benchmark, not a new unknown spectral problem or an arithmetic L-function operator. The loss labels are **E_min/6**, so displayed errors must retain that normalization. Recomputing the final saved PennyLane checkpoint against the analytic labels reproduces its training and held-out losses (approximately 4.39320125e-5 and 4.01904747e-5 respectively). The constant held-out baseline is approximately 0.0106641. The random 75/25 split is disjoint and only the first 75 samples enter gradients. The loss-gradient parameter-shift reasoning from the earlier convolution audit applies unchanged.

### Exact principal-minor verification

`exact_h` constructs this real symmetric matrix with rational coefficients. `minors` enumerates every nonempty principal subset: 4+6+4+1=15 minors. This is the complete positive-semidefiniteness criterion, not the insufficient test of only leading minors. The determinant routine uses exact Fraction Gaussian elimination with row pivoting and determinant sign changes. It leaves eliminated left entries unstored, but these entries are never used again, so that optimization is valid.

I independently compared `determinant` to a separate Leibniz-permutation implementation on 600 random rational matrices of sizes one through four, including singular and zero-pivot examples; all agreed. I rechecked all six saved certificates, recalculated all 15 minors at each saved lower bound, and obtained exact equality with their serialized values.

For the specified **nonnegative** lambda domain, Gershgorin gives lo=-2-2lambda. The basis vector e2 has Rayleigh quotient -2, so hi=-2 is an upper bound on the smallest eigenvalue. A candidate E satisfies H-EI positive semidefinite exactly when E<=E_min. Thus:

- an accepted rational trial can safely improve lo;
- a rejected trial below the previous hi can safely improve hi;
- every bisection acceptance improves lo, while rejection improves hi.

All subsequent tests are rational, independent of the neural prediction's correctness. The final lower bound has all principal minors nonnegative; the upper bracket follows either from the Rayleigh bound or a failed PSD test. In this finite model, `numerical_upper_bracket` is therefore actually a rigorously derived rational upper bracket, despite its understated name.

Using the analytic eigenvalue above, I checked each saved bracket without floating square roots: lo<=hi<=-2, lo^2>=4(1+lambda^2), and hi^2<=4(1+lambda^2). I also tested 42 adversarial repairs at six positive rational lambda values with proposals ranging from -100 to +10. Every exact bracket passed these same inequalities. The public helper's Gershgorin initialization is not valid for arbitrary negative lambda as written; document or guard its nonnegative input requirement if exposing it interactively.

### Interpretation and small record improvements

`proposal_accepted` tests the **rounded rational trial** floor(256*proposal)/256, not the raw floating prediction. Record that rational trial explicitly and label the boolean accordingly so a reader can audit the initial acceptance decision directly. Two of the six current rounded proposals are accepted; four are rejected and repaired. The final certificate is never credited to the learner alone.

The learned initial guess may improve a starting bracket, but this experiment does not benchmark certificate runtime, verifier calls, or improvement over the exact closed form/classical baselines beyond a constant predictor. Fixed 16-step bisection succeeds even with deliberately bad predictions. Do not claim that quantum learning is necessary or that it accelerates certification. Its demonstrated role is a finite hybrid proposal/certificate interface. No general number-field positivity statement or GRH bridge follows.

## Additional review: nine-qubit genus-four benchmark and hyperbolic coordinates

Reviewed the new `train_higher_genus_qcnn.py`, saved higher-genus experiment JSON, the literal larger-example paragraphs in `book/chapters/computations.tex`, `examples/hyperbolic_patch.py`, and the three statements/proofs of `HyperbolicCoordinates.lean` with its focused log. Only this review was changed. I did not rerun the full training or overwrite its artifacts.

Snapshot hashes:

- Nine-qubit source: `a2bb07e42cb534f60e850f6f9139c3911ff5d554ee40296f13044a459b256b31`.
- Hyperbolic patch source: `c31ea871da52b69bfcb011f6b7020fccc91999b9a47b9e05121d351f6d3548f5`.
- Hyperbolic Lean source: `7fa278a07a7e11f1198610156beff00b66312adcf80008618b85271f6c5398f7`.

### Nine-qubit model

For m=9 the stated hyperelliptic family has genus four, nine contracted dessin edges/quiver vertices, and completed-order rank 2m^2=162. The physical Hilbert space is instead (C^2) tensor^9, dimension 512. The book correctly separates those ranks and says that edge labels and a permitted cycle motivate the finite Hamiltonian without giving a faithful action of the infinite order.

The sparse matrix implements

    H(h) = -sum_(j mod9) Z_j Z_(j+1) - h sum_j X_j.

Its row/column bit flips and most-significant-first convention are consistent. The twelve positive h values are split into nine training and three held-out indices (0,4,8). The gradients use training indices only. Two local Ry/Rz layers use 2*9*2=36 independent coordinates, each in one gate; cycle CZ and four disjoint CNOT(0,5), (1,6), (2,7), (3,8) gates are unparameterized. The measured projector selects 0000 on discarded wires 5,6,7,8. Tracing those out is a five-qubit channel; the script optimizes the discarded-register vacuum-probability proxy before that trace.

Parameter shift is valid for the same single-use Pauli-generator reason as in the smaller circuits. I independently tested eight parameters spanning first/last gates of both layers against central differences in actual PennyLane native-gate simulation. Maximum discrepancy was 1.9587681476807006e-10.

For an independent label check, I rebuilt all twelve 512-by-512 Hamiltonians densely and used a different Hermitian eigensolver (`scipy.linalg.eigh` with the lowest eigenpair requested), without importing or retraining the source script. Maximum dense eigenpair residual was 2.6160160092318488e-14. The three saved sparse held-out ground energies agreed with dense lowest eigenvalues within 3.552713678800501e-15. Re-evaluating the saved checkpoint on these independently computed states gave training loss 0.5478854021399289 and held-out loss 0.40856404827390624, agreeing with the archived values within 2.7e-10.

These residuals are floating-point diagnostics. They are not a formal or interval certificate of eigenvalue ordering or a uniform spectral theorem. The code docstring's phrase "sparse exact finite Hamiltonian labels" should be read/reworded as a numerical eigensolver for an explicitly defined finite Hamiltonian, not exact arithmetic eigenvectors. The book's numerical residual wording is appropriate.

The literal book paragraph accurately reports the considerable remaining losses and does not call this accurate lossless coarse graining. Training improves the archived initial loss 0.5971 to 0.5479 and held-out loss 0.4481 to 0.4086. The three final held-out individual losses span approximately 0.0919, 0.3366 and 0.7971, so the last field remains particularly poorly compressed. No generalization beyond this field family, full RG flow, or superiority over a matched classical/untrained baseline is established.

**Reusability correction:** the reviewed source executes training and writes its JSON at module import because its body lacks a `main()` guard. I avoided importing it. Before presenting it as a reusable library/example, wrap execution in an explicit main guard so that inspection/import cannot silently rerun training or overwrite a checkpoint. This is an execution hygiene issue, not a flaw in the saved training equations.

### Infinite hyperbolic tiling window

The regular {7,3} circumradius and the derivation in the book are consistent. The hyperbolic triangle with angles pi/7, pi/3, pi/2 gives cosh R=cot(pi/7)cot(pi/3), and r=tanh(R/2) yields the displayed cosine-ratio formula. The heptagon interior angle is 2pi/3 and curvature-minus-one area is pi/3. This does not identify a compact surface quotient or a Belyi arithmetic structure.

The orthogonal-circle equations are correct: for endpoints a,b, the center c satisfies Re(a conjugate(c))=(|a|^2+1)/2, with squared radius |c|^2-1. Inversion in that circle is the orientation-reversing hyperbolic reflection fixing its geodesic. The separate diameter branch reflects in the Euclidean line through the origin. It requires a nonzero endpoint to normalize the line direction, which holds for the generated tiling edges.

I regenerated the depth-three patch without running its output-writing entry point and obtained the same 85 tiles. Independent checks across their 595 sides/corners gave:

| Diagnostic | Value |
|---|---:|
| Maximum vertex disk radius | 0.9574512250057633 |
| Spread of hyperbolic side lengths | 4.884981308350689e-15 |
| Maximum interior-angle error from 2pi/3 | 1.7763568394002505e-13 |
| Fixed-endpoint reflection residual | 1.7659265502367085e-14 |

Both horizontal and vertical diameter-reflection examples passed separately. Rounded-centroid deduplication, clipping and the tile/depth caps make this a bounded floating visualization, not a certified global enumeration or proof of non-overlap at arbitrary depth. The current output and book explicitly retain that limitation.

### Lean and four-dimensional display scope

The three new Lean statements are actual real-coordinate identities: the rational disk/hyperboloid equation, its inverse defect, and norm preservation under a rotation in one real two-plane of R^4. The focused log has the corresponding types and only standard foundational dependencies. I read their proofs and the successful log; I did not rerun the full analytic suite here.

The hypotheses deliberately prove algebraic identities on a wider domain than the geometric upper sheet. To interpret the forward map as the Poincare disk, require x^2+y^2<1; to interpret the inverse as the disk, require T>0 on the hyperboloid. Nonzero denominators alone do not prove those domain conditions. The actual clipped patch is inside the disk, and the book's displayed optional Lorentz view is consistent with that use. These identities do not yet formalize metric isometry, hyperbolic reflection groups or the infinite tiling theorem.

The R^4 plane rotation preserves the ambient Euclidean norm. It is a viewer coordinate change, not generally a holomorphic automorphism preserving y^2=x^m-1 in the original complex coordinates. Projection to three coordinates can identify distinct points, omit the compact point at infinity and hide sheet changes. The literal book paragraphs explicitly say so. No complete higher-genus 3D embedding or uniformization is asserted.


### Parent resolution after independent review

The photonic quadrature docstring and final-weight sample label are corrected. The larger QCNN is now guarded by main(), its import was checked without changing the saved training JSON, and its labels are described as numerical eigenstate approximations rather than a rigorous lowest-energy certificate. Rational ToricGT trials and rigorous upper brackets are recorded, and the certificate helper rejects negative lambda. The two hyperbolic diameter/reflection and 4D projection cases are explicitly scoped. These are parent implementation resolutions, not claims of an additional independent full training run.
