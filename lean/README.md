# Exact Lean verification

Pinned toolchain: Lean 4.24.0, commit `797c613eb9b6d4ec95db23e3e00af9ac6657f24b`.
No mathlib or external packages are required. Run from project root:

```sh
sh scripts/check_lean.sh
```

The project-local binary is under `.tools/lean-4.24.0-darwin_aarch64/bin/`; the directory is ignored by Git. The official release archive was downloaded from `https://github.com/leanprover/lean4/releases/download/v4.24.0/lean-4.24.0-darwin_aarch64.tar.zst`. Its verified SHA256 is `17ee554702c199fc03f37b1c3708245671c93f5d932dcff55a03fa6cdb5e5adf`, matching GitHub's release asset digest. No shell startup files or existing Lean environments were changed. On another platform install this exact official toolchain independently, then run `lake build` and `lake env lean GRHResearch.lean` here.

## What is checked

- `no_integral_trace_norm_two`: no integer t satisfies 2t²=9. The prose derivation linking this to geodesic norm two is not formalized.
- `cyclicDegrees_even` and `no_integral_cyclic_induction_degree_one`: arbitrary finite integer combinations of even degrees cannot have degree one. The finite-group character interpretation is in the paper, not in this Lean model.
- `symmetrization_changes_determinant`: exact determinants in the finite counterexample. The function mapping an arbitrary transfer to its Hermitian part is not formalized.
- `unipotence_does_not_bound_exponent`: the displayed unipotent integer matrix does not square to identity. This is one witness against the source's proposed degree/exponent implication.
- `iwahori_shift_witness`: the integral matrix identity after clearing denominators. Order membership and fraction-field conjugation are in prose.

`#print axioms` reports only `propext` and `Quot.sound` for the omega proofs, and no axioms for the three finite calculations. There are no project-specific axioms, admissions, external tactics that bypass the kernel, or assumed GRH bridges. See `outputs/checks/lean-build.log` and `lean-verification.log`.

## What is not checked

The analytic spectral criterion, normal-family continuation, prime-tail divergence, general prime-power obstruction, Hadamard factorization, zeta nonvanishing at 1/2, and GRH remain outside this small formalization. This build is not a formal proof of the papers in full or of GRH.

Upstream `math/lean` pins Lean 4.34.1 and many external packages. Its actual solution modules and comparator challenge files have different roles; a comparator's `sorry` is not evidence of an admission in its solution. We have not built that upstream dependency graph and do not represent this local build as verifying it.
