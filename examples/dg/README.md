# Actual nodal DG model and endpoint-sensitive theta extensions

Open http://127.0.0.1:8765/dg.html or the canonical book laboratory at
http://127.0.0.1:8765/book/main.html#lab-dg.

Over a field k, R=k[ξ,η] and K=R⊕Rε has ε in degree−1, ε²=0,
dε=ξη. It resolves the actual infinite nodal dessin algebra R/(ξη).
The completed branch pullback is treated coefficientwise in the chapter;
completion/derived category objects are not yet fully formalized.
The original unit-boundary example dε=1 is contractible, with dh+hd=1.

`NodalDG.lean` uses the actual exterior-line coefficient algebra and
polynomial modules. It checks20 algebra/differential/sign-Leibniz/homotopy/
augmentation/ambient-resolution/semilinear-clock identities. The clock theorem
accepts an actual coefficient automorphism e with e(f)=f; concrete q rescaling
and its completed topology are proved in prose and checked symbolically,
not packaged as a fully formal graded/topological DG category.

The viewer's monomial boxes are finite **k-linear subcomplexes**, not
R-submodules or finite DG subalgebras. For dε=ξη the source has i,j≤N−1
and the target i,j≤N; the exact rank is N² and H0 dimension2N+1. The full
parent algebra remains infinite. Unit and zero-differential comparisons use
the same box in both degrees. BigInt finite-field ranks independently confirm
the displayed counts; phase weights match on differential arrows.

The theta table uses actual dart inputs for the rational/spherical and
elliptic theta dessins, retaining their different α involutions. The Python
checker iterates forbidden words; the viewer independently computes the proved
closed formulas. These are Ext endpoint data from the existing exact
projective resolution, not AR components or intersection formulas. Neither
example has self Ext1 dimension2. Topological/derived equivalences need more.

```sh
.tools/book-quantum-cpu/bin/python examples/dg/check_nodal_dg.py
node scripts/check_dg_model.mjs
python3 scripts/launch_inspector_browser.py
node scripts/check_dg_browser.mjs
```

The exact checks are deterministic: no random seed or training. The existing
approved CPU environment is used without installations. Primary Keller v2 and
Stacks snapshot hashes are in planning/DG_SOURCES.json. The book
keeps physical interpretations separate from algebra: phase rescaling is
semilinear over R, usually fails to preserve diagonal k[[u]], and is not a
*-automorphism for self-adjoint branch loops at nonreal phase. The finite
phase drawing does not supply arithmetic spectrum, determinant matching or GRH.

`nodal.sage` supplies the same ambient matrices and genuine nodal quotient
in Sage syntax. It is explicitly **unexecuted** because the existing Sage
launcher lacks its target app; no installation or upgrade was attempted.
The SymPy and Node exact checks ran in the existing approved environment.
