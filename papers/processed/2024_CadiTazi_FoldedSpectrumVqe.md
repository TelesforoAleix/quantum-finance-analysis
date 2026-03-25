---
aliases:
- 'Folded Spectrum VQE: A Quantum Computing Method for the Calculation of Molecular
  Excited States'
- Folded Spectrum VQE Quantum
authors:
- Lila Cadi Tazi
- Alex J. W. Thom
auto_detected: true
classification: ''
contradiction_flags:
- contradiction:scalability
doi: 10.1021/acs.jctc.3c01378
evidence_type: ''
idea_tags:
- idea:near-term-feasibility
- idea:hybrid-approach
journal_or_venue: Journal of Chemical Theory and Computation
methodology_tags:
- VQE
- variational
- classical-simulation
paper_type: ''
quantum_advantage_claim: not-applicable
related_papers: []
relevance_phase1: low
relevance_phase3: low
source_type: peer-reviewed-empirical
source_type_confidence: high
step1_date: '2026-03-25T16:02:53.143556'
step1_model: gpt-5.1
step2_date: '2026-03-25T16:02:57.126665'
step2_model: gpt-5.1
step3_date: '2026-03-25T16:03:42.976952'
step3_model: gpt-5.4
step4_date: '2026-03-25T16:04:23.226207'
step4_model: gpt-5.4
step5_date: '2026-03-25T16:05:01.707644'
step5_model: gpt-5.4
step6_date: '2026-03-25T16:05:13.186846'
step6_model: gpt-5.4
steps_completed:
- 1
- 2
- 3
- 4
- 5
- 6
tags:
- method/VQE
- method/variational
- method/classical-simulation
- idea/near-term-feasibility
- idea/hybrid-approach
- contradiction/scalability
title: 'Folded Spectrum VQE: A Quantum Computing Method for the Calculation of Molecular
  Excited States'
topic_tags: []
year: 2024
zotero_key: ''
---

## Abstract summary
The paper introduces a folded spectrum variant of the variational quantum eigensolver (FS-VQE) to compute molecular excited states on quantum computers using the same ansatz circuit as for ground-state calculations. By minimizing the variance-based folded spectrum operator and applying Pauli reduction and grouping, the authors reduce the otherwise prohibitive measurement cost associated with the squared Hamiltonian. They demonstrate chemical-accuracy excited-state potential energy curves for H2 and LiH on simulators and show that combining FS-VQE with error mitigation techniques improves accuracy under realistic noise models.
## Methodology
The paper presents an empirical study of a folded-spectrum variational quantum eigensolver (FS-VQE) for computing molecular excited states. The approach extends standard VQE by minimizing the folded-spectrum cost function <(H-ω)^2> so that the eigenstate nearest a target energy ω becomes the variational optimum. Molecular electronic Hamiltonians are built in second quantization, mapped to qubits using the Jordan-Wigner transformation, and evaluated as sums of Pauli strings. To reduce the otherwise large measurement cost of the squared Hamiltonian, the authors apply Pauli reduction and qubit-wise commuting (QWC) Pauli grouping so multiple terms can be measured simultaneously. The ansatz is a unitary coupled cluster singles and doubles (UCCSD) circuit with first-order Trotterization (p=1) and a specific excitation ordering from prior work. Reference states for excited states are chosen from singly/doubly excited determinants and spin-symmetrized combinations. Optimization is hybrid quantum-classical, using SPSA for shot-based simulations, an increasing shot scheduler during optimization, and post-optimization refinement via quadratic fitting and parameter rounding. Experiments are conducted on ideal and noisy simulators rather than real QPUs. The method is evaluated on small molecules H2 and LiH by comparing computed potential energy curves and excited-state energies against exact full configuration interaction (FCI) obtained by classical diagonalization. Additional noisy-simulation experiments assess robustness under an IBM-inspired noise model and test combined SPAM mitigation and zero-noise extrapolation (ZNE), with performance judged primarily by absolute energy error and whether chemical accuracy is achieved.

**Algorithms used:** VQE, FS-VQE, UCCSD, Jordan-Wigner mapping, SPSA, Zero Noise Extrapolation, SPAM error mitigation
**Frameworks:** Qiskit, PySCF

**Experimental setup:** Experiments were run on simulators only. Ideal calculations used Qiskit's QASM simulator for shot-based noiseless sampling and Qiskit's Statevector simulator for exact statevector evaluation. Noisy experiments used a tunable IBM-inspired noise model including depolarizing gate errors, thermal relaxation/dephasing (T1/T2), and readout error. Hamiltonians and molecular orbitals were precomputed classically, with state tracking along potential energy surfaces using previous optimized parameters and energies as initialization.

**Dataset:** Synthetic quantum chemistry benchmark systems rather than financial datasets: H2 in the STO-3G basis and LiH in a minimal s-orbitals-only basis, evaluated across potential energy curves. Additional noisy benchmark experiments were performed for the S2 excited state of H2 at bond length 0.74 Å.
## Experiment details
### Input
Input systems were molecular electronic structure instances. H2 was represented in STO-3G with 4 spin-orbitals mapped to 4 qubits; potential energy curves were computed for the ground state and three excited states (T1, S1, S2). LiH was represented in a minimal basis containing only s orbitals, giving 6 spin-orbitals mapped to 6 qubits; multiple singlet and triplet excited-state potential energy curves were computed. Molecular orbital coefficients were generated with PySCF for each geometry, and phase continuity between neighboring geometries was enforced for state tracking. For noisy tests, the S2 state of H2 at 0.74 Å was simulated under varying noise scale factor λ.

### Process
1. Build the molecular Hamiltonian in second quantization and map it to qubits with Jordan-Wigner. 2. Construct the folded-spectrum operator (H-ω)^2 for excited-state targeting. 3. Apply Pauli reduction and qubit-wise commuting grouping to reduce measurement cost. 4. Prepare a reference state appropriate for the target excited state. 5. Use a UCCSD ansatz with first-order Trotterization (p=1) and a prescribed excitation ordering. 6. Evaluate grouped Pauli expectation values by basis rotations and repeated measurements. 7. Optimize variational parameters with SPSA in shot-based runs; use state tracking along the PES by initializing each geometry from the previous geometry's optimized parameters and energy target. 8. Use an inverse-exponential shot scheduler from 1,000 to 10,000 shots during optimization, then perform a final 30,000-shot evaluation. 9. Apply post-optimization quadratic fitting around each parameter and parameter rounding to values near 0 or fractions of π when beneficial. 10. Compare resulting energies to exact FCI from classical diagonalization. 11. For noisy experiments, simulate IBM-style noise, apply SPAM mitigation via confusion-matrix inversion, and apply ZNE by unitary folding with noise factors 1, 3, 5, and 7 and quadratic extrapolation to zero noise.

### Output
Outputs are molecular ground- and excited-state energies and potential energy curves, reported against exact FCI energies. Main evaluation metrics are absolute energy error relative to FCI and whether results achieve chemical accuracy (1 kcal/mol). The paper also reports measurement-cost statistics such as number of Pauli strings and number of QWC groups for Hamiltonians and folded-spectrum operators. In noisy simulations, mitigated and unmitigated FS-VQE energies are compared as a function of noise level λ.

### Parameters
- mapping: Jordan-Wigner
- ansatz: UCCSD
- trotter_order: 1
- optimizer: SPSA
- optimization_gradient_threshold: 1e-09
- shot_scheduler_min: 1000
- shot_scheduler_max: 10000
- final_shots: 30000
- noisy_experiment_shots_per_circuit: 20000
- zne_folding_factors: [1, 3, 5, 7]
- zne_fit_model: quadratic
- continuity_regularization_eta: 0.1
- h2_qubits: 4
- lih_qubits: 6
- h2_uccsd_compiled_depth: 71
- h2_uccsd_cnot_count: 44
- lih_uccsd_depth: 311
- lih_uccsd_cnot_count: 212
- noise_model_lambda_examples: {'1': {'T1_us': 290, 'T2_us': 145, 't_gate1_ns': 35, 't_gate2_ns': 300, 'p1': 0.0001, 'p2': 0.001, 'p_SPAM': 0.01}, '0.4': {'T1_us': 924, 'T2_us': 461, 't_gate1_ns': 14, 't_gate2_ns': 120, 'p1': 4e-05, 'p2': 0.0004, 'p_SPAM': 0.004}, '0': {'T1_us': 'infinite', 'T2_us': 'infinite', 't_gate1_ns': 0, 't_gate2_ns': 0, 'p1': 0, 'p2': 0, 'p_SPAM': 0}}

### Hardware
No real QPU was used. Ideal shot-based simulations used Qiskit QASM simulator; exact simulations for LiH used Qiskit Statevector simulator. Noisy runs used a custom tunable noise model based on IBM device calibrations, including one- and two-qubit depolarizing errors, thermal relaxation/dephasing with T1/T2, gate durations, and per-qubit readout error. SPAM confusion matrices were derived directly from the noise model parameters rather than measured on hardware.

### Reproducibility
The paper provides substantial methodological detail: ansatz choice, mapping, optimizer, shot schedule, noise model, mitigation procedure, qubit counts, circuit depths, and benchmark systems are described clearly enough for partial replication. Data are generated from standard molecular benchmarks and FCI references, with PySCF and Qiskit explicitly named. However, no public code repository is mentioned in the provided text, and some implementation details (exact geometry grids, optimizer hyperparameters beyond SPSA choice, and full circuit construction specifics) may require reconstruction.
## Findings
- [supported] The folded-spectrum VQE (FS-VQE) method computed all electronic excited states of H2 and LiH studied in the paper with chemical accuracy on ideal quantum simulators.
- [supported] For H2 in STO-3G, FS-VQE recovered the complete potential energy curves for three excited states (T1, S1, S2) with all points within chemical accuracy (1 kcal/mol) relative to FCI.
- [supported] For LiH in a minimal s-orbitals-only basis, FS-VQE reproduced multiple excited-state potential energy curves with errors reported as within chemical accuracy relative to FCI on a statevector simulator.
- [supported] Pauli grouping substantially reduced the number of measurement groups required for the folded-spectrum operator compared with measuring Pauli strings individually.
- [supported] For H2, the Hamiltonian had 15 Pauli strings reducible to 5 qubit-wise commuting groups (2 with general commutativity), while the folded-spectrum operator had 24 Pauli strings reducible to 9 qubit-wise groups (3 with general commutativity).
- [supported] For larger benchmark molecules, Pauli grouping reduced folded-spectrum measurement groups far below the raw number of Pauli strings; e.g., LiH/STO-3G had 25,542 folded-spectrum Pauli strings but 2,216 qubit-wise groups under Jordan-Wigner mapping.
- [supported] Error mitigation improved noisy-simulator excited-state energies: for the H2 S2 state at 0.74 Å, combined SPAM mitigation and zero-noise extrapolation achieved chemical accuracy for noise scale λ < 0.4, whereas without mitigation only the noiseless case λ = 0 was below 1 kcal/mol.
- [supported] The noisy-simulation study suggests that about an order-of-magnitude hardware performance improvement over current devices could make chemically accurate small-system FS-VQE feasible with the mitigation scheme used.
- [supported] All empirical results in the paper were obtained on simulators rather than real quantum hardware: QASM shot-based ideal simulation, statevector simulation, and noisy simulation with IBM-inspired noise models.
- [speculative] The authors argue that FS-VQE may be useful for highly excited states and photochemical applications because it can target states near a chosen energy without sequentially computing lower excited states.
- [speculative] The paper suggests the number of circuit evaluations for the FS method scales as O(N^6) after Pauli reduction/grouping, but acknowledges that more formal and larger-scale analyses are needed.
- [speculative] The authors propose that error mitigation will remain important in the early fault-tolerant era, but this is not demonstrated beyond the small noisy-simulator experiments presented.
- [speculative] The paper argues that FS-VQE could become practical for larger systems if challenges in reference-state preparation, Pauli reduction/grouping, and measurement cost are overcome.

**Results summary:** This peer-reviewed empirical study evaluates folded-spectrum VQE as a method for molecular excited states using quantum simulation rather than real hardware. On ideal simulators, the method reproduced all targeted excited states of H2 (STO-3G) and LiH (minimal s-only basis) with chemical accuracy relative to full configuration interaction, including full potential energy curves for H2 and several LiH excited states. The paper also quantified measurement-cost reductions from Pauli grouping, showing substantial compression of the folded-spectrum operator into fewer commuting measurement groups. In noisy IBM-inspired simulations for the H2 S2 state, combining SPAM mitigation with zero-noise extrapolation improved accuracy enough to reach chemical accuracy for moderate simulated noise levels (λ < 0.4), whereas unmitigated runs did not except in the noiseless limit. The work presents proof-of-concept evidence for FS-VQE on small systems but does not demonstrate quantum advantage or real-hardware performance.

**Performance claims:**
- H2/STO-3G: all excited-state points within chemical accuracy (1 kcal/mol) relative to FCI on an ideal shot-based simulator
- LiH/minimal s-only basis: all reported excited-state points within chemical accuracy relative to FCI on a statevector simulator
- H2 UCCSD circuit: depth 71 with 44 CNOT gates on 4 qubits
- LiH minimal-basis UCCSD circuit: depth 311 with 212 CNOT gates on 6 qubits
- Final measurement shots: 30,000 for ideal shot-based H2 evaluations
- Noisy-mitigation experiment: 20,000 shots per circuit evaluation for H2 S2 at 0.74 Å
- H2 Hamiltonian measurement reduction: 15 Pauli strings to 5 QWC groups or 2 GC groups
- H2 folded-spectrum operator reduction: 24 Pauli strings to 9 QWC groups or 3 GC groups
- LiH minimal basis Hamiltonian reduction (JW): 118 Pauli strings to 29 QWC groups
- LiH minimal basis folded-spectrum reduction (JW): 417 Pauli strings to 65 QWC groups
- LiH STO-3G folded-spectrum reduction (JW): 25,542 Pauli strings to 2,216 QWC groups
- BeH2 STO-3G folded-spectrum reduction (JW): 47,171 Pauli strings to 8,933 QWC groups
- H2O STO-3G folded-spectrum reduction (JW): 111,615 Pauli strings to 20,393 QWC groups
- With mitigation, H2 S2 energy reached chemical accuracy for simulated noise scale λ < 0.4; without mitigation, only λ = 0 was below 1 kcal/mol
- ZNE implementation overhead: approximately 4x more shots, using folded circuits with noise-scaling factors γ = 1, 3, 5, 7
## Quantum advantage claim
**Classification:** not-applicable

The paper does not demonstrate quantum advantage over classical methods. Results are proof-of-concept studies on ideal and noisy simulators for very small molecules, benchmarked against exact classical FCI, with no empirical speedup or scaling advantage shown on real hardware.
## Limitations
- Experiments are restricted to very small molecules and active spaces (H2 and LiH), because current NISQ hardware is too limited in quantum volume and gate fidelity for reasonable real-device FS-VQE results.
- Results demonstrating chemical accuracy are obtained primarily on ideal or noisy simulators rather than on real quantum hardware.
- The main limitation of the FS method is the need to evaluate the squared Hamiltonian, which greatly increases the number of Pauli terms and measurements relative to standard VQE.
- Although Pauli reduction empirically improves scaling, the authors note that more formal analyses are required to consolidate the effective scaling and assess feasibility for larger systems.
- The Pauli reduction of the FS operator is described as a difficult classical task that would need further investigation to become scalable.
- Pauli grouping is a crucial bottleneck because finding an optimal partition is NP-hard, and the practicality of FS-VQE depends strongly on this step.
- The number of shots required for large systems remains prohibitive on quantum hardware even after Pauli grouping.
- The classical part of the hybrid algorithm may retain intractable stages for large systems, including the number of measurements, classical storage of measurement results, and precomputation of the qubit Hamiltonian and FS operator.
- Optimization becomes increasingly difficult as system size grows, including due to barren plateaus.
- The method depends on preparing suitable reference states for excited states; the authors identify this as a major challenge for scalability, especially for systems with strong multireference character.
- For larger systems, the UCCSD ansatz is not expected to reach FCI accuracy; it is expected to recover only coupled-cluster-level accuracy.
- The noise model used is approximate and excludes leakage and crosstalk, so it may not be suitable for devices where these effects are significant.
- SPAM mitigation assumes that SPAM noise remains constant over nearby experiments in time, which may not always hold.
- ZNE assumes that circuit folding effectively scales the relevant noise and that gate noise is the dominant source; this assumption is not always valid, especially because SPAM noise is not scaled by folding.
- Error mitigation introduces substantial overhead: the implemented ZNE uses four times more shots and deeper folded circuits (gamma = 1, 3, 5, 7).
- The LiH study uses a minimal s-orbitals-only basis, which the authors note is a poor approximation for lithium and does not aim for physically accurate results.
- State tracking can still suffer from jumps between nearby electronic states, especially when omega becomes closer to another state or when states are quasi-degenerate.
- Some regularization and hyperparameter choices (e.g., continuity penalty eta = 0.1, shot schedule, parameter scaling) are based on empirical trials, which may limit robustness and reproducibility across problems.
- [inferred] No benchmarking is provided against state-of-the-art classical excited-state solvers beyond comparison to exact diagonalization/FCI on tiny systems, so practical advantage over classical methods is unestablished.
- [inferred] Reproducibility may be limited because performance depends on optimizer behavior, stochastic shot noise, heuristic grouping, and empirically tuned settings, while no standardized end-to-end benchmark suite is reported.
- [inferred] The study does not demonstrate scalability to production-scale or finance-relevant problem sizes; conclusions are proof-of-concept only.
## Open questions
- Whether FS-VQE remains feasible and scalable for larger molecular systems.
- What the true scaling of the number of terms and evaluations for the FS operator is after Pauli reduction and grouping.
- How to make Pauli reduction of the FS operator scalable in practice.
- How to design efficient heuristic Pauli grouping methods that preserve scalability for FS-VQE.
- How to systematically and scalably determine good reference states for larger and multireference systems.
- Whether the increasing density of states in larger systems can make excited-state search easier by allowing convergence to local minima near the target energy.
- How effective error mitigation can be for FS-VQE in more detailed and extensive settings beyond the proof-of-concept shown here.
- Whether chemical accuracy can be achieved on near-term or early fault-tolerant hardware for larger systems with realistic noise.
- How much the classical preprocessing and storage costs limit end-to-end scalability of FS-VQE.
- How robust the method is to quasi-degeneracies and state crossings when tracking a specific excited state along a potential energy surface.
- [inferred] At what problem size, if any, FS-VQE could outperform competitive classical excited-state methods in wall-clock time or resource efficiency.
- [inferred] How sensitive the method is to ansatz choice, optimizer choice, and hyperparameter tuning across different problem classes.

**Future work:**
- Perform more formal analyses of the scaling of the FS operator after Pauli reduction to assess feasibility for larger systems.
- Develop analytical results on the scaling of the number of evaluations needed for the FS method.
- Investigate more efficient Pauli grouping approaches, including general commutativity partitioning, to further reduce measurements.
- Study and develop scalable methods for preparing better reference states, especially for larger molecules and multireference excited states.
- Carry out larger simulations or experiments to confirm expected accuracy behavior beyond the very small systems studied here.
- Conduct more detailed and extensive analyses of error mitigation techniques within FS-VQE.
- Reduce the overhead introduced by mitigation methods such as ZNE in terms of shots and circuit depth.
- Leverage future improvements in VQE components, ansatz design, and fermion-to-qubit mappings to improve FS-VQE.
- Explore alternative ansatze with more favorable circuit-depth scaling than UCCSD while maintaining accuracy.
- Extend the folded-spectrum procedure to algorithms beyond VQE for excited-state computation.
- Investigate the use of logical-qubit-based error correction for large-scale applications in the long term.
- Improve methods for preventing jumps between electronic states during state tracking along potential energy surfaces.
- [inferred] Validate the method on real quantum hardware as hardware quality improves, rather than relying mainly on simulators.
- [inferred] Benchmark FS-VQE against leading classical excited-state methods on larger, more realistic instances to clarify practical utility.
## Key ideas
- #idea:near-term-feasibility — FS-VQE is presented as a proof-of-concept variational approach for excited-state computation on small NISQ-era benchmark systems, with chemical accuracy shown only in tiny simulated molecules.
- #idea:hybrid-approach — The workflow is explicitly hybrid, combining classical Hamiltonian construction, Pauli reduction/grouping, SPSA optimization, and post-processing with a variational quantum circuit.
- #idea:hybrid-approach — Measurement overhead from the folded-spectrum operator is reduced through Pauli reduction and qubit-wise commuting grouping, which is central to making the approach tractable even on toy instances.
- #idea:near-term-feasibility — Error mitigation via SPAM correction and zero-noise extrapolation improves noisy-simulator accuracy, suggesting limited near-term viability for very small systems if hardware improves.
## Contradictions
- The paper suggests near-term applicability for small excited-state problems, but its own evidence is limited to ideal and noisy simulators on 4- and 6-qubit molecular instances, contradicting any strong implication of scalability to realistic problems.
- Although FS-VQE is framed as potentially practical with measurement reduction and mitigation, the paper also states that squared-Hamiltonian measurement cost, Pauli grouping complexity, shot requirements, reference-state preparation, and optimization difficulty remain major barriers, creating an internal contradiction on scalability.
- Any implicit optimism about practical deployment is contradicted by the absence of real-hardware validation and by the authors' acknowledgment that current NISQ devices are too limited for meaningful FS-VQE experiments.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
