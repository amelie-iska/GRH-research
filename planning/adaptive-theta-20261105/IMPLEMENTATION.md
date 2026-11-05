# Adaptive validated theta sampling implementation

Continuation of approved P11, all implementation/checks on Linux. Existing
fixed dyadic/theta/readout sources and accepted certificates stay immutable.
No new dependency, GPU job, authentication or Lean declaration.

Acceptance: a separate variable-precision interval context with exact guarded
inputs and precision-keyed immutable caches; adaptive N,J,K/discard choices
from exact positive tail inequalities; circle-node re-evaluation on precision
retry; exact serialized radius<=requested positive rational sample error.
All five sample error terms must be recorded separately, with no fixed180-bit
serialization floor. Provide practical samples below old floor and an optional
complete-circle/readout experiment only when independently checked.

Tasks: (1) focused tests before source, (2) implement precision primitives and
adaptive sampler in fresh modules, (3) immutable new experiment outputs and
independent primitive/tail/sample/guard review, (4) integrate accepted proofs
and examples into staged book/site/artifacts, (5) narrow verified publication.
A precision search must refine actual point/node enclosures; it cannot shrink
an arbitrary fixed input rectangle. Fixed conductors/disk/theta identity and
no zero-location/GRH inference remain explicit.
