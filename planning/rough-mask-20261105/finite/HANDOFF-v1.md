# Fresh exact rough-prime mask controls: AA only

PASS, frozen. This new diagnostic uses complete squarefree good ideal columns and actual nonprincipal row blocks at D200/U10, D512/U16 and D900/U30. It does not rerun/read D144/576/D60000 or the U7/D100 control, accepted raw tables, UI, published233index or604bundle. Only captured hash-pinned pure ideal_tower arithmetic and literal finite-field symbols were executed; accepted roughv3 was captured as proof-definition text. No analytic estimate, GRH, training, all-nine-channel replacement or positivity of h1 is claimed.

One common fixed smooth profile has delta1/4096, with exact value1 at every strict integer norm node for integerD<=1024 and0 at endpoints. The fixed derivative cost is O_k4096^k, potentially large. No floating smoothstep evaluation occurs. nu1, S above2,3, primary1mod3 ideals and literal unit1 are explicit. Every row has a v1-prime valuation1 outsideS. Randomness is unused; the enumeration and arithmetic are deterministic.

|Case|Actual row block/capacity|Full SF ideal columns/rows|
|---|---|---|
|D200/U10|pure v1 in[13,26), others1, H53=floorD^.75|52/5|
|D512/U16|pure v1 in[19,38), others1, H107=floorD^.75|139/7|
|D900/U30|mixed v1,v2 in[7,14), coprime; u=v1*v2²; H384 DECLARED|250/2|

MixedH384 is notfloorD^.75 or a growth-fit point. The two mixed rows are the ordered conjugate norm7 pairs, Nu343. Both row primes are belowU, so the rough-row correction is exactly0. Pure blocks include actual row prime ideals aboveU, including inert norm25 (underlying rationalprime5), illustrating why roughness uses IDEAL norm.

## Exact quantities and normalization

Let T_f,p sum original A_U(fa)chi_a(u) over every goodSF residual a coprime to f with active W(Nf Np Na/D); T^(p) also removes p|a. The same original(f,u)=1 mask and mu(f) remain in both K_T and K_S. K_T uses p coprime to u and T^(p); K_S extends to all rough goodp and fullT. These whole K sums are signed because mu(f) remains.

The disjoint row correction uses p|u and full|T|². The residual correction uses p∤u and f1, exactly2Re(T_1p conjugate(zp))-|zp|² with zp=chi_p(u)W(P²/D). Support forces every removed residual to f1,a=p. Its extended fpa=p² is an auxiliary NONSQUAREFREE ideal, never admitted as an original column. The minus|z|² term is the a=b=p intersection. Raw row/residual overlap is kept and vanishes by the literal zero when p|u. Distinct conjugate ideal primes of the same rational norm are never merged.

All following numbers are RAW NUMERATORS, prior to division byD:

|D|K0 smooth|KT masked|KS S-only|Erow|Eres|Delta=KS-KT|Ctwo|Original AA|
|---|---:|---:|---:|---:|---:|---:|---:|---:|
|200|339|209|235|20|6|26|21|151|
|512|366|711|781|48|22|70|89|-256|
|900|436|366|410|0|44|44|28|98|

OriginalAA=K0-KT+Ctwo. S-only with unit correction is K0-KS+Ctwo. Their difference is Delta=Erow+Eres. Thus normalizedDelta is13/100,35/256,11/225 respectively, divided byD ONCE. The cleaner main(K0-KS)/D is13/25,-415/512,13/450; OriginalAA/D minus that cleanmain is(Delta+Ctwo)/D=47/200,159/512,2/25. The read-only derived normalization tables use distinct raw_numerators and normalized_exactly_once names, avoiding any ambiguity from raw-key suffixes inside the original normalized container.

The residual intersection subtractions are8,18,8. Omitting them changes the correction. The unchanged original unit-residual two-rough-prime corrections are21,89,28, over unordered DISTINCT prime ideals with all row masks. Allowing repeated p=q adds false terms8,18,8. Ctwo is nonnegative but is not a lower bound for h1: D512 has OriginalAA/D=-1/2 while Ctwo/D=89/512>0.

## Frozen source, states and checks

Main source planning/rough-mask-20261105/finite/check_masks_v1.py SHAc705fbb0985d69475f55d59241b27577134b826745a4dc2aa6f55fc77898f7ce. Helper ideal_tower SHA77dc26658a188ff6669bf577fcb8298b875ab2a5e4f8e0bfe628b94c9b9430d4, acceptedroughv3 SHA039548240acab66f883b6fc0d9bcee0e42a84fec5c390472ad501ef045e862c6. All source/input bytes were captured before execution, checked unchanged after, and stored in source-snapshot. Output directories refuse overwrite; failure.json would preserve any failed new run. This run passed on the first attempt.

outputs/checks/2026-11-05-rough-mask/finite/run-v1/manifest.json SHAd8ebdc9410e0e24c3dfd999ea33c10864d28b4e9f008913e08d26233217268cf; summary SHAd78dd82fd5a345028b84c4e308177130b6a8ef0f5b5082d88abd74dba516aeca. All artifact hashes/bytes were recomputed. Total outputs2725968bytes; runtime0.319381145s; peakRSS27472KiB; standard-library CPU1/nice15. SourceHEADdba37ff/index0ef1af unchanged. Each D-case JSON retains every good ideal/SF flag/factorization, original column ID, row, SF residual raw character, smooth/rough T state, auxiliary extended generator, mask, direct pair decomposition/intersection, unit pair and per-row raw/normalized total.

The main check independently performs literal ordered coprime original-column pairs and full ideal-divisor inversion, then compares both to smooth-minus-masked-prime-plus-unit and S-only-plus-disjoint-corrections. Direct residual-pair expansion checks each AA complex orientation, including nonreal samples, instead of only one scalar total. Counts:485/1771/898 rough states;10/21/8 auxiliary nonSF terms;225/840/446 stored unit-residual states with support lowerL in(1/2,1); the mixed case has100 nontrivial f-masked states. Rational-norm mask negative controls retain the allowed conjugate prime of the same norm.

A separate read-only saved-output check, check_phase_transfer_v1.py, imports no arithmetic helper/evaluator and reruns no raw case. Its phase-transfer-and-normalization-v1.json SHA640979b5120a4d6f5a0b38233db6dc1a804e3764ad397384e3c3d33a81c21ba8 verifies3353 FULL COMPLEX Fd=chi_f chi_p T^(p) transfers,2471 original coefficient/phase products and39 auxiliary nonSF terms. This rules out a false mu(p) coefficient sign that could otherwise leave an AA square norm unchanged; the negative control records identical norms but different complex bucket values. It also emits separate raw and normalized tables with cleanmain/unit-correction bookkeeping.

A final analytic mask-correction note477b148c... was coordinated after the kernel definition; its bounds remain an independent analytic review, not something inferred or fitted from these finite values. No UI/canonical/publication work was done here. External independent reconstruction of this new dataset remains a separate acceptance step if root requests it.
