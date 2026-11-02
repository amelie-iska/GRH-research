# Independent review: finite arithmetic zero certificate

2026-11-02. Read-only adversarial review by the project_review agent, independent of the authoring agent.

The reviewer reproduced the logarithm intervals, Gaussian-rational exponential sums, error bounds and strict comparisons using a separate exact Fraction implementation. It then inspected and executed the literal certificate arithmetic in scripts/check_arithmetic_zero.py in memory, without writing its outputs. All comparisons passed. The rounded log5 value lies above the true logarithm; its symmetric certified interval correctly covers it. Taylor degree120 includes terms0through120, and the first omitted term has index121.

The reviewer checked the perturbation and derivative bounds, signs in f and f′, the disk second-derivative bound, and the Rouché comparison. It found no substantive mathematical or implementation defect. The local determinant obstruction is correctly limited to the fifth partial sum and a nowhere-zero scalar normalization. The suggested wording clarification, “factor times the determinant of a fixed positive Hermitian pencil,” was applied.

Both ArithmeticZeroDisk.lean theorem types were independently compiled with warnings as errors. Their axiom reports contain only propext, Classical.choice and Quot.sound. They establish the actual disk location and exact positive comparison margin; they do not formalize the analytic enclosures or root existence. The finite off-line zero is not a zero of the full L-function and is not a GRH counterexample.

The pinned source clones were inspected as clean. This review is an independent project check, not external peer review or certification of GRH.
