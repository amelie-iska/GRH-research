# Actual infinite-dessin branch modules

Run `.tools/book-quantum-cpu/bin/python examples/relations/check_relations.py`
and `node examples/relations/check_model.mjs` from the project root. The first
uses the existing pinned SymPy environment and exact rational arithmetic;
neither command installs anything. No randomness is used.

Primary algebra: the genuinely infinite locally gentle algebra of the clean
dessin on y²=x^m−1, beta=x^m, m=5/9, genus2/4. Representations are left
quiver representations, with arrows in their direction of travel. The full
subcategory has b=0 and all a except a0 invertible; its finite-dimensional
objects are equivalent to finite endomorphisms via a0=T. It is not the whole
module category, a lattice category or a derived equivalence.

The exact checker validates8 module cases,10 full quiver Hom systems,
full source-graph ranks and corrected gf/fg kernels, mixed Fitting dimensions,
nilpotent block multiplicities, nonzero coefficient maps, cyclic transport
determinants and a nonsplit string self-extension. It checks two admissible
successors for every direct/inverse letter in the actual closed quivers.
Generated evidence is `outputs/checks/2026-11-03-linear-relations/exact.json`
and the web copy `web/data/relations.json`; no source data is modified.

The web tool's projected coefficient graph has nodes (quiver vertex,basis
coordinate). It is not a uniformizing surface. Basis vectors lying in each
kernel/image are displayed for the supplied Jordan/block examples; arbitrary
subspaces need not have a coordinate basis. The tool distinguishes polynomial
bands, continuous finite u-torsion over the completion, and nonzero lattices.

Eleven Lean statements use actual Submodule relations and LinearMaps, including
full graph composition, inverse relation, semiconjugacy, both filtration
directions, finite-space Fitting/stabilization and annihilation by units.
Full categorical equivalence, Jordan/Hom classification, Cantor coding,
determinant identity, completion topology and general infinite-string
classification remain prose/external theorem inputs. No arithmetic GRH bridge
or positivity certificate follows. Exact primary scopes and hashes are in
planning/LINEAR_RELATIONS_SOURCES.json and the independent review.
