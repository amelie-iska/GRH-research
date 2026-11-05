# The exact middle-cutoff sign window

For every squarefree integral ideal m and real U>=1,

    A_U(m)=mu(m)  if Nm<=U,
    A_U(m)=-mu(m) if U<Nm<=U^2.

The first case was already in the cutoff proof. The second is a direct disjoint-support convolution identity, with no analytic assumption or statement about zeros.

Proof. The unrestricted sum of mu(a)mu(b) over disjoint a,b with ab|m is mu(m). Subtract assignments with Na>U. In that part every divisor b of m/a automatically satisfies Nb<=Nm/Na<U, because Nm<=U^2. Hence summing mu(b) over all b|m/a vanishes unless a=m. This excluded part is exactly mu(m), since Nm>U. The symmetric excluded Nb>U part is also mu(m). There is no overlap: Na>U and Nb>U would give Na Nb>U^2>=Nm, impossible for ab|m. The actual truncated sum is therefore mu(m)-mu(m)-mu(m)=-mu(m).

The identity may help explain the actual signed coefficient transitions and appropriate support-shifted Mobius examples. Under the presently stated W support[1,2] and U^2<=D, it must not be silently substituted across all length-D columns: those columns generally have Nm>U^2. No GRH/critical-strip convergence/mean-square consequence is inferred.

The finite diagnostic uses norms of actual distinct Eisenstein prime ideals 7,13,19,31 and the inert norm25 ideal. It checks the combinatorial norm restrictions, not their sextic symbols or an infinite theorem. The full proof is the disjoint-support argument above.
