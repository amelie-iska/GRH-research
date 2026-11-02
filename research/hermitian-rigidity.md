# Holomorphic Hermitian rigidity and dilation

Research pass2026-11-02. Target: test whether pointwise Hermitian extraction or Hermitian dilation can provide the missing holomorphic arithmetic self-adjoint bridge. Result: the proposed shortcuts have a precise obstruction. This is a classical complex-analysis deduction, not a novelty claim or a GRH proof.

## Rigidity theorem

On a connected open U in C, an entrywise holomorphic matrix H(z), with fixed index space and inner product, that is Hermitian at every complex z is constant. For each fixed v, v*H(z)v is real-valued holomorphic, hence constant by open mapping. Polarization recovers entries. Alternatively the real-valued holomorphic functions H_ij+H_ji and i(H_ij−H_ji) determine every entry. The Lean proof uses this second argument and actual mathlib matrix/Hermitian definitions.

This also implies that either Hermitian or skew-Hermitian part of a nonconstant holomorphic T cannot remain holomorphic: if one were, it would be constant, and the other holomorphic part would then be constant by the same rigidity after multiplication by i.

## Dilation does not solve it

For square T of dimension d, K=[[0,T],[T*,0]] is Hermitian. SVD gives eigenvalues ±sigma_j(T), det(lambdaI−K)=product_j(lambda²−sigma_j²), and det(−K)=(−1)^d|detT|². The prime-diagonal model therefore produces ±|chi(p)|p^(−Re(s)), losing imaginary-s and character-phase information. For nonconstant holomorphic scalar f, |f|² cannot be holomorphic.

Caveats: a nonconstant T can have constant determinant (diag(expz,exp(−z)) is a witness). A nonholomorphic matrix can have an accidentally holomorphic scalar determinant, so matrix rigidity alone does not refute every composed scalar expression. No unbounded variable-domain operator theorem is claimed.

## Permitted architectures and source references

Fixed self-adjoint H_N independent of spectral s remains permitted and is the hypothesis of the existing closure theorem. Holomorphic pencils Hermitian only for real t are permitted, but need a separate zero-location argument: h(t)=t²+1 is real on R while z−h(z) has nonreal roots. Reflection symmetry is therefore weaker than the required spectral theorem.

Pinned surface source212ff730: lines11465–11484 perform the s-dependent transfer/Hamiltonian passage; lines12200–12215 switch between fixed eigenvalues and extraction from T(s); lines13636–13643 explicitly take (T−T*)/(2i). The numerical implementation at12541–12570 fixes an evaluation point and is a different operation; do not apply this theorem to it without the missing holomorphy assumption.

Independent read-only review confirmed the theorem, SVD formulas, scope caveats and references. Source clones remain unchanged. Next step: investigate fixed-operator or properly reflected pencil constructions, rather than insisting on simultaneous complex holomorphy and pointwise Hermitian values. The arithmetic determinant identity and GRH zero-location bridge are still open.
