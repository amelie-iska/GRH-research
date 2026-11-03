# Diagnostic attempts and accepted evidence

The initial focused candidate failed on inference of Fin1's successor,
a malformed one-line tactic block and a nonexistent submodule lemma name.
Explicit index arguments, structured proof bullets and the lattice lemma
fixed those elaboration failures; the core sequence then compiled.

The subsequent Hom extension exposed an action-instance boundary. After
introducing the residue field action, global MvPolynomial.module inference
could choose the induced coefficientwise action on the polynomial ring.
The maps had correctly used multiplication before that extension; the
composition failed rather than accepting mixed actions. An explicit local
regularModule=Semiring.toModule before all free-module definitions fixes
multiplication throughout, and separate regular_action/residue_action
identities guard the choice. Ordinary-linear composition notation supplies
all scalar identity homomorphisms explicitly. Final19 focused declarations
and the full262-report suite pass with warnings as errors and standard
foundations only. Failed logs contain Lean's error-recovery placeholders;
they are diagnostics, not accepted proofs. Final logs and independent review
are the verification evidence.

The first new browser attempt exhausted its short startup polling window
before isolated Chrome became ready under concurrent compilation load.
The known profile later responded normally; no preview/source was altered.
The test now uses a bounded20-second startup deadline and per-fetch timeout.
Reusing that known test browser passed all controls and literal on-page
Lean-source equality; it closed its own profile normally. Profiles and the
failed attempt log are preserved. There were no product runtime exceptions.
