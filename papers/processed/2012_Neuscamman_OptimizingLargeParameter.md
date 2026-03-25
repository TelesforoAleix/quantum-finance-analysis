---
aliases:
- Optimizing large parameter sets in variational quantum Monte Carlo
- Optimizing large parameter sets
authors:
- Eric Neuscamman
- C. J. Umrigar
- Garnet Kin-Lic Chan
auto_detected: true
classification: ''
contradiction_flags: []
doi: 10.1103/PhysRevB.85.045103
evidence_type: ''
idea_tags:
- idea:hybrid-approach
- idea:near-term-feasibility
journal_or_venue: Physical Review B
methodology_tags:
- variational
- classical-simulation
paper_type: ''
quantum_advantage_claim: not-applicable
related_papers: []
relevance_phase1: low
relevance_phase3: low
source_type: peer-reviewed-empirical
source_type_confidence: high
step1_date: '2026-03-25T15:50:03.191480'
step1_model: gpt-5.1
step2_date: '2026-03-25T15:50:06.909408'
step2_model: gpt-5.1
step3_date: '2026-03-25T15:50:33.748045'
step3_model: gpt-5.4
step4_date: '2026-03-25T15:51:16.505466'
step4_model: gpt-5.4
step5_date: '2026-03-25T15:51:40.390268'
step5_model: gpt-5.4
step6_date: '2026-03-25T15:51:46.302758'
step6_model: gpt-5.4
steps_completed:
- 1
- 2
- 3
- 4
- 5
- 6
tags:
- method/variational
- method/classical-simulation
- idea/hybrid-approach
- idea/near-term-feasibility
title: Optimizing large parameter sets in variational quantum Monte Carlo
topic_tags: []
year: 2012
zotero_key: ''
---

## Abstract summary
The paper introduces an approach to optimize very large numbers of variational parameters in variational quantum Monte Carlo by using iterative Krylov subspace solvers instead of explicitly constructing Hamiltonian and overlap matrices. The authors develop accelerated versions of the stochastic reconfiguration and linear methods, and demonstrate the technique using a correlator product state with a Pfaffian reference on several strongly correlated lattice and molecular systems. The work focuses on the optimization methodology rather than detailed physical analysis, showing that accurate energies can be obtained with up to hundreds of thousands of parameters.
## Methodology
The paper presents an empirical computational study in variational quantum Monte Carlo (VMC), focused on improving optimization of very large variational parameter sets by replacing explicit construction of stochastic reconfiguration (SR) and linear method (LM) matrices with iterative Krylov-subspace solvers. The main implemented method is accelerated SR using the conjugate gradient (CG) solver, where overlap-matrix vector products are computed on-the-fly during Monte Carlo sampling rather than storing the full overlap matrix; the paper also derives, but does not numerically implement, an accelerated LM using a generalized Davidson solver. The variational ansatz used in experiments is a correlator product state (CPS) tensor-network wave function with a Pfaffian reference (CPS-Pfaffian). The method is evaluated on four benchmark many-body systems: a 4x4 fermionic Hubbard model, an 8x8 fermionic Hubbard model with twist-averaged boundary conditions, a 4x4 hydrogen lattice in the STO-3G basis, and free base porphin in a 24-orbital active space. Performance is assessed through convergence behavior, total energies, relative energy error versus exact diagonalization or full configuration interaction (FCI), recovered correlation energy, and singlet-triplet gap accuracy versus density matrix renormalization group (DMRG) or exact references. The study is classical quantum Monte Carlo for electronic structure/condensed matter simulation rather than quantum computing on gate-model hardware.

**Algorithms used:** Variational Quantum Monte Carlo, Stochastic Reconfiguration, Conjugate Gradient, Generalized Davidson, Linear Method
**Frameworks:** MOLPRO

**Experimental setup:** All experiments are classical simulations in variational quantum Monte Carlo; no quantum processor is used. The implemented optimization method is stochastic reconfiguration accelerated with conjugate gradient iterations and Monte Carlo sampling of matrix-vector products. Numerical studies use a CPS-Pfaffian wave-function ansatz on four systems: 4x4 and 8x8 fermionic Hubbard lattices, a 4x4 hydrogen lattice in STO-3G, and free base porphin in a 6-31G basis with a 24-orbital active space. The paper mentions distributed storage of derivative ratios across processors but does not provide a full computing-environment specification.

**Dataset:** No external dataset is used. Inputs are synthetic/physics-model systems: (1) 4x4 half-filled periodic fermionic Hubbard lattice with varying U/t; (2) 8x8 Hubbard lattice with twist-averaged boundary conditions using 12 random twists at U=4, t=1 and varying hole density; (3) 4x4 square hydrogen lattice at multiple H-H distances in the STO-3G basis; (4) free base porphin in the 6-31G basis with frozen core and a 24 out-of-plane 2p orbital active space containing 26 electrons.
## Experiment details
### Input
Model-system inputs rather than observational financial data. 4x4 Hubbard: half filling, periodic boundary conditions, U/t values from 1 to 16; one experiment used two translationally invariant 3x3 correlators with 524,784 variational parameters, another used all 2x2 squares and all long-range pair correlators with 5,488 parameters. 8x8 Hubbard: twist-averaged boundary conditions with 12 randomly chosen twists, U=4, t=1, translationally invariant 2x2 and long-range pair correlators on each sublattice, varying hole fraction h to compute hole energy. 4x4 hydrogen lattice: STO-3G basis, open boundary conditions, nearest-neighbor distances from 0.6 to 3.0 Angstrom, all 2x2 and long-range pair correlators, 4,048 variational parameters. Free base porphin: 6-31G basis; 1s and sigma bonding orbitals frozen as closed shell from RHF; 24 localized out-of-plane 2p orbitals (Pipek-Mezey localization) forming an active space with 26 electrons; correlators include all pairs plus selected three-orbital elbows and five-orbital rings; 9,064 variational parameters.

### Process
1. Define the CPS-Pfaffian variational wave function for each benchmark system. 2. Sample configurations in VMC from the wave-function probability distribution, restricting samples to the correct electron number and total Sz where applicable. 3. For SR optimization, solve the linear system associated with imaginary-time evolution in the derivative subspace using conjugate gradient rather than explicitly constructing the overlap matrix; matrix-vector products are evaluated stochastically during sampling. 4. Update variational parameters iteratively using the SR solution and repeat until energy convergence. 5. In practice, add a small diagonal shift to the overlap matrix multiplication to remove linear dependencies from redundant parameters or stochastic noise. 6. For the 4x4 Hubbard convergence study, compare steepest descent against SR using 10 and 100 CG iterations per parameter-update step, with step size tau=0.01 and an unrestricted Hartree-Fock initial guess with slightly randomized molecular orbitals. 7. For benchmark evaluation, compute total energies, relative errors, hole energy curves, recovered correlation energy, and singlet-triplet gaps, and compare against exact diagonalization, FCI, CP-AFQMC, RHF, or DMRG references depending on the system. The generalized Davidson-based accelerated LM is derived theoretically but not numerically tested in this paper.

### Output
Reported outputs include total ground-state energies, relative energy error ((E_exact - E)/E_exact) for the 4x4 Hubbard model, convergence of total energy versus number of parameter-update iterations for steepest descent and SR, hole energy e_h(h) versus hole fraction for the 8x8 Hubbard model to infer phase separation, total energy curves for the 4x4 hydrogen lattice compared with RHF and FCI, percentage of correlation energy recovered, and the singlet-triplet gap of free base porphin compared with spin-adapted DMRG. Baselines/reference methods include exact diagonalization (4x4 Hubbard), steepest descent optimization, constrained-path auxiliary-field QMC (8x8 Hubbard), RHF and FCI (hydrogen lattice), and DMRG (porphin).

### Parameters
- variational_parameters_range: 4e3 to 5e5
- 4x4_hubbard_large_ansatz_parameters: 524784
- 4x4_hubbard_convergence_ansatz_parameters: 5488
- 4x4_hydrogen_parameters: 4048
- porphin_parameters: 9064
- cg_iterations_tested: [10, 100]
- sr_step_size_tau: 0.01
- 8x8_hubbard_twists: 12
- 8x8_hubbard_U: 4
- 8x8_hubbard_t: 1
- porphin_active_orbitals: 24
- porphin_active_electrons: 26
- diagonal_shift: small diagonal shift added to overlap-matrix multiplication; exact value not specified

### Hardware
{'hardware_type': 'classical computing only', 'quantum_hardware': 'none', 'simulator': 'variational quantum Monte Carlo simulation', 'parallelization_notes': 'derivative-ratio storage can be divided across processors', 'software': ['MOLPRO (for FCI reference calculations)']}

### Reproducibility
No code or public implementation is mentioned. System definitions, ansatz choices, parameter counts, and several numerical settings are reported, but Monte Carlo sampling details (e.g., sample counts, stopping criteria, diagonal-shift magnitude, full optimizer settings, and computational environment) are incomplete. Reference data are reproducible in principle from the described model systems, but replication would require substantial implementation effort.
## Findings
- [supported] The paper introduces an accelerated variational quantum Monte Carlo optimization approach using iterative Krylov subspace solvers that avoids explicit construction and storage of Hamiltonian and overlap matrices, enabling optimization of roughly 4×10^3 to 5×10^5 variational parameters.
- [supported] For stochastic reconfiguration, replacing explicit overlap-matrix construction with conjugate gradient reduces the stated computational cost from at least O(ns nv^2) to O(ns nv) per matrix-vector product when derivative ratios are precomputed.
- [supported] For the linear method with a nonrelativistic Born-Oppenheimer Hamiltonian, the authors claim the matrix-vector product cost scales as O(ns no^4) versus O(ns no^6) for explicit Hamiltonian-matrix construction, i.e., a system-size-squared reduction in cost.
- [supported] On the 4×4 half-filled Hubbard model with periodic boundary conditions and 524,784 variational parameters, the CPS-Pfaffian ansatz recovered ground-state energies with relative error below 1% for all tested U/t values from 1 to 16.
- [supported] On a 4×4 Hubbard model convergence test with 5,488 variational parameters, stochastic reconfiguration converged in roughly one-fifth as many parameter-update iterations as steepest descent, even when only 10 conjugate-gradient iterations were used per update.
- [supported] Increasing conjugate-gradient iterations from 10 to 100 produced no visible improvement in convergence in the reported 4×4 Hubbard test, indicating few Krylov iterations were sufficient relative to parameter dimension.
- [supported] On the 8×8 Hubbard model with twist-averaged boundary conditions, U=4, and 12 random twists, the method predicted phase separation with a critical hole density between 0.14 and 0.15.
- [supported] For the same 8×8 Hubbard setting at half filling, the twist-averaged energy per site was reported as -0.855 ± 0.002, closely matching the cited CP-AFQMC benchmark of -0.856.
- [supported] For a 4×4 hydrogen lattice in the STO-3G basis with 4,048 variational parameters, the method recovered at least 98% of the correlation energy across all tested geometries.
- [supported] For free base porphin in a 24-orbital active space with 9,064 variational parameters, the computed singlet-triplet gap was 1.77 eV, within 0.02 eV of the benchmark DMRG value of 1.75 eV.
- [speculative] The authors suggest that these algorithmic advances provide a powerful new method for modeling challenging quantum chemical and solid-state systems more broadly, beyond the specific benchmarks tested.
- [speculative] This paper is about classical variational quantum Monte Carlo for many-body physics and does not study quantum computing hardware or quantum algorithms for financial services.

**Results summary:** This peer-reviewed empirical paper presents a classical variational quantum Monte Carlo optimization method accelerated with iterative Krylov subspace solvers. The main empirical evidence comes from simulations of condensed-matter and quantum-chemistry benchmark systems, not from quantum hardware. The method avoids explicit matrix construction and is demonstrated on wave functions with up to 524,784 parameters. On a 4×4 Hubbard lattice, reported relative energy errors were below 1% across U/t=1 to 16. In a convergence comparison, stochastic reconfiguration required about one-fifth as many update iterations as steepest descent, with little difference between 10 and 100 conjugate-gradient iterations. On an 8×8 Hubbard lattice with twist averaging, the method predicted phase separation at hole density 0.14<hc<0.15 and matched a cited benchmark half-filled energy per site (-0.855 ± 0.002 vs -0.856). For a 4×4 hydrogen lattice, the approach recovered at least 98% of correlation energy at all geometries tested, and for free base porphin it produced a singlet-triplet gap of 1.77 eV, within 0.02 eV of a benchmark 1.75 eV result.

**Performance claims:**
- Optimization demonstrated for approximately 4×10^3 to 5×10^5 variational parameters
- Stochastic reconfiguration overlap handling reduced from at least O(ns nv^2) to O(ns nv) per matrix-vector product
- Linear method Hamiltonian handling reduced from O(ns no^6) to O(ns no^4), a factor of system size squared
- 4×4 Hubbard model: relative energy error <1% for all tested U/t values from 1 to 16
- 4×4 Hubbard energies (CPS-Pfaffian vs exact, units of t): U/t=1: -1.29871(1) vs -1.299602; 2: -1.12340(2) vs -1.126098; 4: -0.84539(4) vs -0.851366; 6: -0.65326(4) vs -0.659514; 8: -0.52440(4) vs -0.529305; 10: -0.43689(2) vs -0.439313; 12: -0.37281(2) vs -0.374514; 14: -0.32434(1) vs -0.325925; 16: -0.28697(1) vs -0.288241
- Convergence test: stochastic reconfiguration converged in roughly one-fifth as many iterations as steepest descent
- Convergence test used 10 CG iterations per update with no visible improvement from increasing to 100 CG iterations
- 8×8 Hubbard model: predicted phase separation with critical hole density 0.14<hc<0.15
- 8×8 Hubbard half-filled twist-averaged energy per site: -0.855 ± 0.002, compared with cited CP-AFQMC value -0.856
- 4×4 hydrogen lattice: recovered 98% or more of correlation energy at all geometries
- 4×4 hydrogen example energies (Eh): at R=0.6 Å, -3.4541(4) vs FCI -3.460659; 1.0 Å, -7.7765(2) vs -7.785104; 1.4 Å, -7.8914(1) vs -7.903634; 1.8 Å, -7.6767(1) vs -7.684200; 2.2 Å, -7.53726(3) vs -7.539753; 2.6 Å, -7.48167(3) vs -7.486036; 3.0 Å, -7.46921(1) vs -7.470067
- Free base porphin singlet-triplet gap: 1.77 eV vs benchmark 1.75 eV, error 0.02 eV
## Quantum advantage claim
**Classification:** not-applicable

The paper studies classical variational quantum Monte Carlo algorithms for simulating quantum many-body systems. Results are from classical simulation/optimization benchmarks, not quantum computing hardware or quantum algorithms, so quantum advantage is not applicable.
## Limitations
- Numerical results are presented only for the accelerated stochastic reconfiguration (SR) method; the accelerated linear method (LM) is derived but not yet implemented or empirically validated in this paper.
- The numerical studies are stated to be primarily concerned with the optimization problem, and a detailed examination of the underlying physics of the example systems is deferred.
- The 4×4 Hubbard benchmark achieves energies within about 1% of exact values rather than exact recovery, indicating residual approximation error from the ansatz and/or optimization.
- The 8×8 Hubbard phase-separation result is described as a qualitative corroboration of prior CP-AFQMC work, suggesting limited quantitative certainty in the predicted critical hole density.
- The hydrogen lattice study uses the minimal STO-3G basis, which the authors note is not large enough to capture all details of electron correlation.
- The porphin calculation is restricted to a 24-orbital active space with frozen core orbitals, so results do not represent the full orbital space treatment.
- The method still relies on stochastic sampling, and the authors note the need for diagonal shifts to address linear dependencies arising from redundant variational parameters or stochastic error.
- [inferred] The work is entirely classical variational quantum Monte Carlo and does not involve quantum hardware, so there is no evidence on qubit limits, noise robustness, or applicability to near-term quantum devices relevant to quantum computing in finance.
- [inferred] Scalability is demonstrated only on a small number of physics/chemistry benchmark systems, with no evidence of production-scale deployment or performance on real financial optimization workloads.
- [inferred] Reproducibility may be limited because implementation details for the accelerated LM are unavailable, some comparison results rely on unpublished software, and no code/data release is mentioned.
- [inferred] External validity is limited because all experiments are on condensed-matter and quantum-chemistry systems rather than financial services datasets or use cases.
- [inferred] Although the method handles up to 5×10^5 variational parameters, the paper does not fully characterize wall-clock scaling, memory bottlenecks, or convergence behavior for million-parameter regimes highlighted as motivating applications.
## Open questions
- How well will the accelerated linear method perform in practice once implemented, and will it outperform accelerated SR on the same problems?
- Can the approach scale efficiently to wave functions with millions of variational parameters, as motivated in the introduction?
- How robust is convergence with respect to stochastic noise, redundant parameters, and the choice of diagonal shift?
- How many Krylov iterations are required as system size and ansatz complexity increase, especially for larger ab initio Hamiltonians?
- What is the true phase-separation behavior and critical hole density of the 2D Hubbard model beyond the qualitative 8×8 evidence shown here?
- How accurate is the method when larger and more realistic one-particle bases are used for ab initio systems?
- Can the CPS-Pfaffian ansatz maintain similar accuracy for larger molecular active spaces and more complex strongly correlated systems?
- [inferred] How transferable are the optimization advances to application domains outside physics and chemistry, including financial optimization problems often discussed in quantum computing for finance?

**Future work:**
- Complete the computer implementation of the accelerated linear method and present numerical results for it in a future publication.
- Carry out detailed investigations of the physics of the example systems, beyond the optimization-focused studies reported here.
- Apply the optimization approach to more sophisticated trial wave functions, such as tensor networks with millions of variational parameters.
- Extend testing to larger and more challenging ab initio and solid-state systems.
- Further study phase separation and other unresolved properties of the 2D Hubbard model using the proposed optimization framework.
- [inferred] Benchmark runtime, convergence, and memory scaling more systematically across larger parameter counts and system sizes.
- [inferred] Improve reproducibility through release of implementations, parameter settings, and benchmark datasets.
- [inferred] Evaluate whether the optimization strategy can be adapted or translated to quantum-computing workflows and finance-relevant optimization tasks.
## Key ideas
- #idea:near-term-feasibility — Krylov-subspace stochastic reconfiguration scales variational optimization to roughly 4e3–5e5 parameters, offering a transferable optimization insight for large variational models even though the work is classical VMC.
- #idea:hybrid-approach — The paper avoids explicit matrix construction by combining Monte Carlo sampling with iterative linear solvers, a pattern potentially relevant to hybrid variational workflows.
- #idea:hybrid-approach — Conjugate-gradient-accelerated stochastic reconfiguration reduces overlap handling from at least O(ns nv^2) to O(ns nv) per matrix-vector product when derivative ratios are precomputed.
- #idea:near-term-feasibility — Empirical benchmarks on Hubbard, hydrogen lattice, and porphin systems show accurate optimization with large parameter counts, but only in physics/chemistry settings.
## Contradictions
<!-- Step 6 output — where this paper contradicts others -->

## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
