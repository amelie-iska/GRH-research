# Requested-tolerance rational readout and executed training trace

Continuation of approved P11; all implementation and checks run on Linux.
The preserved theta/Mellin certificates remain immutable. No dependency or
infrastructure change, GPU work, zero-location theorem or Lean declaration.

## Design and acceptance
Use the fixed, source-pinned 192 validated labels at 64 true circle nodes.
Construct outward Fourier coefficient rectangles through degree63 using the
existing pinned dyadic arithmetic. Pick exact rational midpoint targets.
Train the explicit quadratic Fourier-coordinate objective by literal rational
updates from zero, recording every iterate and exact objective. Distinguish
this midpoint-target objective from the true-circle least-squares objective;
their gradients differ by the certified coefficient rectangles.

For requested rational epsilon>0, compute the oracle, alias, Taylor and DFT
arithmetic budget at all64 admissible degrees. Select the first degree whose
base budget is strictly smaller than epsilon and execute updates until the
optimization residual makes the total no larger than epsilon. If no degree
qualifies, refuse with the exact minimum computed certificate floor. This is
a bounded, fixed-label API, not an arbitrary-accuracy theta oracle.

1. Add focused tests before implementation: known exact first update;
   replay and geometric loss descent; independent exact five-budget sum;
   fixed-label floor refusal; input/provenance/output protection.
2. Implement examples/analytic_oracle/adaptive_readout.py without changing
   dyadic.py or theta_oracle.py or the accepted final-v5 artifacts.
3. Generate fresh 1e-12 and 1e-15 examples for conductors3/4/5, plus a 1e-18
   refusal. Independently review exact arithmetic, budgets and wording.
4. Add a source-backed interactive training/error-budget replay, proof text,
   and synchronized research/checkpoint records after acceptance.
5. Build PDF/native HTML into new staging, check representative visual and
   mobile output, and promote only valid artifacts. Publish only a verified
   substantive release using the authorized existing Mac login as transport.

Review focus: coefficient normalization; midpoint vs true-root gradient;
source-hash tampering; exact budget sum and requested tolerance; requests
below the fixed-label certificate floor. No full-program completion inferred.
