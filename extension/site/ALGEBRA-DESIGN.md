# Algebra companion: calculation and interface contract

This page extends the existing research-atlas design rather than introducing a
separate application or an external runtime. It reuses `styles.css` typography,
colors, navigation, buttons, focus rings, and paper/white surfaces. Page-specific
layout is in `algebra.css`; the algebra and DOM interface are in `algebra.js`.
There are no network data requests, external scripts, generated mathematical
images, timers, or background animation loops.

## Mathematical contracts

1. **Minors.** Eight editable integers in [-9,9] define a 2-by-4 matrix. All six
   minors and the Plücker residual are computed with JavaScript BigInt. Rank is
   over the rationals: a nonzero minor gives rank two; otherwise any nonzero
   entry gives rank one. The identity itself is a universal polynomial identity.
   The zero wedge is explicitly excluded from projective Grassmannian points.
2. **Tableaux.** Enumerate all 243 fillings of shape (3,2) by entries 1,2,3 and
   retain exactly those with weak rows and strict columns. The result is fifteen
   tableaux. Every tableau is available both through a native select and a
   labelled gallery button. The displayed weight counts its entries. Hook
   lengths and contents are calculated independently, yielding 360/24=15.
   Integral rank is distinguished from characteristic-zero irreducibility and
   semisimple splitting.
3. **Gentle modules.** Dimensions p,q,r range from zero to six. The selected
   pair satisfies u<=p, v<=r and u+v<=q. Actual canonical U,V matrices use disjoint
   middle identity blocks, and their product is computed exactly. The five
   multiplicities are (u,v,p-u,q-u-v,r-v). All allowable pairs are selectable.
   The basis-point diagram and the matrix tables describe the same maps.
   Presets distinguish the irreducible (1,2,1) quadric from the two components of
   the (1,1,1) nodal equation. Zero-dimensional cases remain valid.
4. **Matching semigroup.** Eight exponent controls range from zero to twelve.
   Their images in ten underlying exponent coordinates use BigInt arithmetic.
   Y1Y2 reduces to B1X1X2 and Z1Z2 to B1B2. Both reductions preserve all ten
   coordinates and the four matching equations. The output can have exponents
   larger than twelve. The weighted degree uses degrees (2,2,4,4,3,3,4,2), not
   a false uniform degree-one grading. The incorrect B2 alternative in the
   arXiv-v1 printed first relation is displayed with its unequal vectors.

The proof specifications are `standard-monomials.tex` and `gentle-invariants.tex`.
These executable checks accompany the proofs; they are not Lean formalizations
of the entire Schur or invariant-theory constructions.

## Interaction and accessibility

Native inputs, selects, and buttons are the authoritative controls. Every input
has a visible label or explicit accessible name. Invalid or incomplete integers
pause calculation, set `aria-invalid`, and explain that previous valid results
remain displayed. Dimension changes can clamp ranks to the allowable set; the
status announces that adjustment. Rank-pair replacement restores focus to the
new selected button. Gallery selection remains keyboard accessible.

The page has four anchored sections, a skip link, source links, a 4D-complex
laboratory link, and a link to the actual quantum companion. The ten-coordinate
table scrolls in its own labelled container on narrow screens. Essential
information is also text: row/column inequalities, exact ranks, decomposition,
normal forms, and every balance residual. Color never supplies the only check.

## Completed computational verification

Run `node extension/site/verify-algebra.cjs` from the repository root.

- All 6,561 matrices with entries in {-1,0,1} satisfy the computed Plücker
  relation; fixed full-rank, dependent, and zero examples also have known values.
- The fifteen tableaux match an independent enumeration by strict columns.
- All 2,478 allowed dimension/rank cases with p,q,r in 0..6 have zero composite;
  independent modular row elimination checks their two ranks in characteristics
  two and seven, and summand dimensions reconstruct the input dimensions.
- All 6,561 generator-exponent inputs in {0,1,2}^8 preserve coordinates and
  grading; normal forms are idempotent and agree on every collision among the
  4,529 distinct underlying exponent vectors.
- Both corrected relations hold, the printed B2 alternative fails, and invalid
  mathematical inputs are rejected.
- The HTML has unique IDs and every literal DOM lookup in the script resolves.

These are finite software checks. The manuscript's proofs establish the
unbounded statements.

Parent integration performs browser QA: desktop and narrow-screen layout,
no document-level horizontal overflow, editable minors, invalid inputs, all
fifteen tableau selections, zero-dimensional complexes, nodal rank choices,
CW relation presets, focus behavior, navigation, and console errors. The existing
site design supplies the visual reference; no new raster concept is needed for
these exact, code-native mathematical controls.
