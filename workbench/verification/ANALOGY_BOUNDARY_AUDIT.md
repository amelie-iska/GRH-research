# Directed analogy and deduction boundary audit

Base reviewed: `e30d393420c05e66144b8fd8edbe979d38cd134d`.

Two false acceptances were reproduced on the published source. A source edge
could map to a two-edge target path whose intermediate vertex was absent from
the declared target graph. A retrieval item with an empty leakage-group set
could also enter the shortlist. The former was not a witness in the declared
graph; the latter lacked the provenance required to decide group exclusion.

The repair validates every declared edge endpoint, including unused edges;
checks bounded node types, relation words and paths; and requires explicit
nonempty memory groups and unique memory identities. Malformed keys, arithmetic
overflow, ambiguous identities, unknown branches and stale encoder identifiers
are rejected. Empty eligible retrieval returns no candidates, not a fabricated
negative. Optional exact integer orders require both source and target witnesses
and strictly increasing edges. They establish an ordered graph condition, not
physical causality. Boundary types and licensed relation words do not replace a
relation-specific semantic or chain-map theorem.

Ground-rule replay now requires explicit premise sets and bounded named rules,
with sequential availability of every premise. The caller's rules and initial
premises remain assumptions. An empty-premise rule is explicitly permitted as a
supplied axiom; retrieval similarity is never promoted to a deduction.

The new regression module has twenty test methods. Execution results belong in
the subsequent verification receipt; this source note does not assert a run.
The measured-data study uses its separately described frozen-embedding adapter,
not this standalone checker, so the existing model predictions and measured
results are unchanged. The historical dataset revision remains a reproducible
record and must not be silently described as containing this repair.
