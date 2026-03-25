---
aliases:
- Evaluating a quantum-classical quantum Monte Carlo algorithm with Matchgate shadows
- Evaluating quantum classical quantum
authors:
- Benchen Huang
- Yi-Ting Chen
- Brajesh Gupt
- Martin Suchara
- Anh Tran
- Sam McArdle
- Giulia Galli
auto_detected: true
classification: ''
contradiction_flags:
- contradiction:scalability
- contradiction:classical-vs-quantum
doi: 10.1103/PhysRevResearch.6.043063
evidence_type: ''
idea_tags:
- idea:near-term-feasibility
- idea:hybrid-approach
journal_or_venue: Physical Review Research
methodology_tags:
- VQE
- variational
- classical-simulation
paper_type: ''
quantum_advantage_claim: not-applicable
related_papers:
- 2021_McArdle_QuantumChemistry
relevance_phase1: low
relevance_phase3: low
source_type: peer-reviewed-empirical
source_type_confidence: high
step1_date: '2026-03-25T16:03:38.236524'
step1_model: gpt-5.1
step2_date: '2026-03-25T16:03:43.830792'
step2_model: gpt-5.1
step3_date: '2026-03-25T16:04:45.198663'
step3_model: gpt-5.4
step4_date: '2026-03-25T16:05:27.603864'
step4_model: gpt-5.4
step5_date: '2026-03-25T16:05:59.046498'
step5_model: gpt-5.4
step6_date: '2026-03-25T16:06:11.463566'
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
- contradiction/classical-vs-quantum
title: Evaluating a quantum-classical quantum Monte Carlo algorithm with Matchgate
  shadows
topic_tags: []
year: 2024
zotero_key: ''
---

## Abstract summary
The paper experimentally and numerically evaluates a hybrid quantum-classical auxiliary-field quantum Monte Carlo (QC-AFQMC) algorithm that uses Matchgate-based classical shadows to compute overlaps between quantum trial states and Monte Carlo walker states. The authors analyze the noise resilience of overlap ratios obtained from Matchgate shadows, extend robust shadow protocols to partially mitigate state-preparation noise, and demonstrate end-to-end QC-AFQMC calculations for small molecular and defect systems on superconducting and trapped-ion hardware. They find that while the method is inherently robust to several types of noise, the classical postprocessing cost for Matchgate shadows scales with a high-degree polynomial and already requires hours on thousands of CPUs for very small systems, posing a major challenge for scalability.
## Methodology
The paper presents a peer-reviewed empirical evaluation of a hybrid quantum-classical auxiliary-field quantum Monte Carlo method (QC-AFQMC/QC-QMC) in which overlap amplitudes between a quantum-prepared trial state and classical Slater-determinant walkers are estimated using Matchgate classical shadows instead of Clifford shadows. The study combines theoretical analysis, numerical simulation, and hardware experiments. Methodologically, the authors: (1) formulate QC-AFQMC using Matchgate shadows for efficient postprocessing of overlap amplitudes; (2) extend robust shadow protocols to partially mitigate state-preparation noise; (3) experimentally test noise resilience of overlap amplitudes and overlap ratios on real hardware; and (4) run end-to-end QC-AFQMC calculations for two quantum chemistry/defect problems. The AFQMC component propagates walkers in imaginary time under the phaseless approximation, with local energies and force-bias terms computed from overlap ratios involving the quantum trial state. Matchgate circuits are sampled from the discrete Clifford-Matchgate/Borel ensemble, and classical postprocessing uses Pfaffian/polynomial-interpolation-based formulas. Empirical validation is performed on IBM superconducting hardware for H2 and on IonQ trapped-ion hardware for an NV-center effective Hamiltonian, with comparisons against noiseless simulations and classical reference energies (FCI). Additional noisy simulations on water are used to study robustness under asymmetric Pauli noise. The main evaluation focuses on mean absolute error of overlap amplitudes/ratios, convergence of AFQMC energies, agreement with FCI/noiseless references, and practical runtime/scalability of classical postprocessing.

**Algorithms used:** QC-AFQMC, AFQMC, phaseless AFQMC, Matchgate classical shadows, robust Matchgate shadows, VQE, UCCSD
**Frameworks:** Amazon Braket, IBM Quantum, PennyLane

**Experimental setup:** Experiments combined real quantum hardware, noiseless simulation, and noisy simulation. Matchgate-shadow circuits were executed on IBM Quantum Hanoi (superconducting qubits) for 4-qubit H2 experiments and on IonQ Aria (trapped ions, accessed via Amazon Braket/AWS) for a 4-qubit NV-center calculation. Water-molecule robustness tests were run on the PennyLane simulator with asymmetric Pauli noise. Classical AFQMC propagation and shadow postprocessing were parallelized across thousands of CPU cores, typically one core per walker; hydrogen used 4800 CPU cores and NV-center used 4800 physical cores. For hydrogen overlap/noise studies, 16,000 Matchgate circuits were used, each with 1024 shots; robust-shadow calibration used an additional 16,000 circuits. For NV-center QC-AFQMC, 4000 shadow circuits with 100 shots each were used. The authors note that classical postprocessing dominated runtime, requiring minutes per walker per time step for hydrogen and about 1.5 hours total for 400 time steps in the NV-center case.

**Dataset:** No conventional tabular dataset was used. The study used quantum chemistry and materials Hamiltonians derived from: (1) the hydrogen molecule H2 in the minimal STO-3G basis at five bond distances from 0.75 to 2.75 angstrom; (2) a water molecule at equilibrium geometry in a (4e,4o) active space for noisy simulation tests; and (3) an effective Hamiltonian for a negatively charged nitrogen-vacancy (NV) center in diamond obtained via quantum defect embedding theory (QDET), using a minimal (4e,3o) active space. Classical references included FCI energies and noiseless emulations.
## Experiment details
### Input
Hydrogen: H2 in STO-3G, mapped to 4 qubits via Jordan-Wigner, evaluated at five bond lengths (0.75-2.75 Å); restricted Hartree-Fock orbitals used as input, with trial states from noisy VQE and a two-determinant form alpha|1100> + beta|0011>. Overlap-noise experiments used 16 randomly sampled Slater determinants, yielding 120 possible overlap ratios. Water: equilibrium geometry, (4e,4o) active space, 8 qubits, restricted Hartree-Fock canonical orbitals, used only for noisy robustness simulation. NV center: QDET-derived effective Hamiltonian for negatively charged NV center in diamond, minimal (4e,3o) active space mapped to 4 qubits; ground state has 3A2 symmetry. Trial states in hardware studies were intentionally imperfect VQE/UCCSD states with energies about 30-80 mHa above FCI for H2/NV cases. No external financial dataset is involved.

### Process
1. Prepare a quantum trial state satisfying VT|Psi_I> = |Psi_T> and VT|0> = |0>, typically using a tailored UCCSD-style ansatz. 2. Prepare an equal superposition (|0> + |Psi_T>)/sqrt(2). 3. Apply a randomly sampled Matchgate circuit UQ from the discrete Borel/Clifford-Matchgate ensemble and measure in the computational basis to obtain classical shadows. 4. For robust-shadow calibration, run modified circuits (without the initial Hadamard) to estimate noisy Matchgate-channel eigenvalues f~_{2l}; in hydrogen this used 16,000 additional circuits. 5. Classically reconstruct overlap amplitudes <Psi_T|phi> for Slater-determinant walker states using Matchgate-shadow formulas and Pfaffian/polynomial interpolation. 6. Run phaseless AFQMC: initialize walkers in the Hartree-Fock state, sample auxiliary fields, compute force bias from overlap ratios, propagate walkers in imaginary time, update weights using the phaseless approximation, and compute local energies. 7. Aggregate walker energies to estimate the ground-state energy and compare against noiseless simulation and FCI. Key AFQMC settings reported include 4800 walkers and time step Delta tau = 0.005 Ha^-1 for H2, and 4800 walkers with Delta tau = 0.4 Ha^-1 for the NV center. Hydrogen overlap/noise experiments varied the number of Matchgate circuits from 40 to 10,000 while drawing from a total pool of 16,000 circuits. NV-center production runs used 4000 shadow circuits with 100 shots each and 400 time steps. Water robustness simulations used asymmetric single-qubit Pauli noise with X/Z/Y error rates of 1%/3%/2%, including state-preparation noise.

### Output
Reported outputs include mean absolute error (MAE) of overlap amplitudes and overlap ratios versus noiseless reference as a function of the number of Matchgate circuits; AFQMC ground-state energies and dissociation curves; imaginary-time convergence trajectories; agreement with FCI reference energies; comparison between raw noisy hardware results, robust-shadow-corrected results, and noiseless simulations; and practical runtime/scalability estimates for classical postprocessing. Baselines/comparators include noiseless classical emulation, FCI reference values, noisy versus robust Matchgate shadows, and discussion of prior Clifford-shadow and Hadamard-test approaches. For H2 and NV-center, the final energies on hardware converged to within computational accuracy or about 0.1 mHa of classical reference/noiseless results.

### Parameters
- hydrogen_qubits: 4
- water_qubits: 8
- nv_center_qubits: 4
- hydrogen_basis: STO-3G
- hydrogen_bond_distances_angstrom: [0.75, 2.25, 2.75]
- hydrogen_total_bond_distances_studied: 5
- hydrogen_overlap_test_slater_determinants: 16
- hydrogen_overlap_ratios_total: 120
- hydrogen_matchgate_circuits_total: 16000
- hydrogen_shots_per_circuit: 1024
- hydrogen_robust_shadow_extra_circuits: 16000
- hydrogen_afqmc_walkers: 4800
- hydrogen_delta_tau_Ha_inverse: 0.005
- nv_shadow_circuits: 4000
- nv_shots_per_circuit: 100
- nv_afqmc_walkers: 4800
- nv_delta_tau_Ha_inverse: 0.4
- nv_time_steps: 400
- water_noise_model: single-qubit asymmetric Pauli noise
- water_pauli_error_rates: {'X': 0.01, 'Y': 0.02, 'Z': 0.03}
- trial_ansatz: tailored UCCSD / effective double-excitation circuits
- mapping: Jordan-Wigner

### Hardware
Real hardware included IBM Quantum Hanoi for hydrogen experiments and IonQ Aria for NV-center experiments. IBM Hanoi used 4 physical qubits; reported calibration snapshots include qubit sets [1,2,3,5] and [6,7,10,12], with T1/T2, CNOT error rates, single-qubit X error rates, and readout error rates listed in the appendix. IonQ Aria is described as having all-to-all connectivity, average single-qubit gate fidelity 99.97%, two-qubit gate fidelity 98.6%, and readout fidelity 99.55%. IonQ access was facilitated through Amazon Braket/AWS. Simulations used PennyLane for noisy water experiments and noiseless classical emulation for comparison. Matchgate circuits were implemented using open-source code cited by the authors; no explicit transpilation settings or noise model for IBM Aer are reported.

### Reproducibility
Partial reproducibility. The paper provides substantial methodological detail: Hamiltonian construction, ansatz structure, qubit mappings, shot counts, walker counts, time steps, hardware platforms, and even hardware calibration tables. It cites open-source code for fermionic classical shadows and names the simulation platforms. However, no dedicated repository for the full experimental/QC-AFQMC workflow is explicitly provided in the text excerpt, and some implementation details (full code, exact random seeds, complete circuit-generation scripts, and all preprocessing artifacts for QDET/NV Hamiltonians) are not directly bundled. Reproduction appears feasible for experts but nontrivial, especially for the large-scale classical postprocessing and embedded-defect calculations.
## Findings
- [supported] Matchgate shadows in QC-AFQMC were experimentally observed to be inherently noise robust on quantum hardware, including for overlap ratios that drive AFQMC.
- [supported] For hydrogen on IBM Hanoi, noisy overlap amplitudes showed significant error, while robust Matchgate shadows reduced this error; accounting for state-preparation noise improved correction further.
- [supported] For hydrogen overlap ratios, the paper reports that when the number of shadow circuits exceeded about 100, noisy, robust, and noiseless ratio estimates approximately agreed, indicating practical noise resilience of the ratios.
- [supported] QC-AFQMC reproduced the hydrogen dissociation curve on IBM Hanoi with convergence to within computational accuracy of FCI at five bond lengths, even without explicit error mitigation.
- [supported] For hydrogen at 0.75 Å, the difference between noisy hardware QC-AFQMC and noiseless classical emulation was about 1e-4 Hartree, with little observable difference during imaginary-time evolution.
- [supported] For an NV center in diamond on IonQ Aria, QC-AFQMC hardware results agreed with noiseless reference and converged to the classical FCI limit with errors on the order of 0.1 mHa.
- [supported] Although Matchgate shadows remove the exponential postprocessing bottleneck of Clifford shadows asymptotically, the authors found classical postprocessing still required hours on thousands of CPUs even for the smallest chemical systems studied.
- [supported] For hydrogen, postprocessing 16,000 shadow circuits took about 1 minute per walker per time step, and full AFQMC evolution could take hours to days because steps must be performed sequentially.
- [supported] The local-energy evaluation in the implemented Matchgate-shadow QC-AFQMC pipeline scales as O(n^8), and the paper identifies this as the dominant practical scalability bottleneck.
- [supported] The paper reports a sampling-complexity scaling close to O(n^2.95) for determining noisy Matchgate-channel coefficients used in robust shadows.
- [speculative] Practical quantum advantage may be possible only if vanishing-overlap issues can be mitigated at larger system sizes (e.g., around 100 orbitals), but this was not tested here.
- [speculative] QC-AFQMC could act as an error-mitigation layer for VQE by correcting ansatz and noise errors through imaginary-time evolution.
- [supported] The authors explicitly state that their hardware demonstrations do not establish an advantage over classical QMC for the small systems studied.

**Results summary:** This peer-reviewed empirical study provides the first end-to-end experimental evaluation of Matchgate-shadow-based QC-AFQMC. On real hardware, the authors tested hydrogen on IBM Hanoi and an NV center in diamond on IonQ Aria. They found that overlap ratios estimated with Matchgate shadows are naturally noise resilient in practice, even though individual overlap amplitudes can be noisy; robust Matchgate shadows further improved individual overlap estimates, especially when state-preparation noise was included in calibration. For hydrogen, QC-AFQMC matched FCI across five bond lengths and differed from noiseless emulation by about 1e-4 Hartree at 0.75 Å. For the NV center, hardware and noiseless simulations both converged to the FCI reference with about 0.1 mHa error. However, all results are for small systems, and the study emphasizes that classical postprocessing remains a severe bottleneck: even the formally polynomial Matchgate-shadow approach required substantial HPC resources, with local-energy evaluation scaling as O(n^8). Results combine real-hardware experiments and supporting noiseless/noisy simulations; no quantum advantage is demonstrated.

**Performance claims:**
- For overlap ratios, noisy, robust, and noiseless estimates approximately agreed once the number of Matchgate shadow circuits exceeded ~100
- Hydrogen QC-AFQMC used 16,000 Matchgate shadow circuits per bond length; rigorous bounds suggested ~1.1e5 circuits for epsilon=1e-2 and >=99.99% confidence, but 16,000 were sufficient empirically for the small system
- Hydrogen QC-AFQMC used 4,800 walkers and time step Delta tau = 0.005 Ha^-1
- For hydrogen at 0.75 Å, noisy hardware QC-AFQMC differed from noiseless emulation by ~1e-4 Ha
- For hydrogen, postprocessing 16,000 circuits took approximately 1 minute per walker per time step
- Hydrogen full evolution could take hours to days due to sequential AFQMC time steps
- NV-center QC-AFQMC used 4,000 shadow circuits with 100 shots each, 4,800 walkers, and Delta tau = 0.4 Ha^-1
- For the NV center, converged hardware and noiseless results had errors on the order of 0.1 mHa relative to FCI
- NV-center computation for 400 time steps required approximately 1.5 hours on 4,800 physical CPU cores
- Robust-shadow noisy-coefficient estimation showed empirical sampling-complexity scaling close to O(n^2.95)
- Implemented local-energy evaluation scales as O(n^8)
- Extrapolated classical postprocessing scaling for QC-AFQMC is reported as O(n^8.5 log^2 n) in the discussion
## Quantum advantage claim
**Classification:** not-applicable

The paper explicitly does not claim demonstrated quantum advantage for the small systems studied. It discusses possible future advantage only conditionally and theoretically, while emphasizing severe classical postprocessing bottlenecks and lack of advantage over classical QMC in these experiments.
## Limitations
- Classical postprocessing, while asymptotically polynomial, still requires hours of runtime on thousands of CPUs even for the smallest chemical systems, fundamentally challenging scalability.
- High-degree polynomial scaling in system size arises from computing the local energy of each QMC walker, creating a major bottleneck.
- Large constant-factor costs from the number of classical shadow samples, QMC walkers, and QMC time steps make the method expensive in practice.
- Experiments and demonstrations are limited to small systems (e.g., H2 and a minimal active-space NV-center model), so practicality for realistic large-scale systems is not established.
- The study explicitly avoids system sizes where exponentially vanishing overlaps become significant, so one major scalability barrier is not empirically addressed.
- The robust Matchgate shadow protocol has limitations: it is only guaranteed under gate-independent, time-stationary, Markovian noise and noiseless state preparation.
- Residual state-preparation noise remains only partially corrected by the enhanced robust protocol, and the authors do not provide a full mathematical characterization of which state-preparation noise models can be mitigated.
- Noise resilience of overlap ratios does not persist for all noise settings, especially coherent state-preparation noise or noise violating GTM assumptions.
- The quantum trial-state preparation circuit must satisfy an additional constraint (e.g., VT|0⟩ = |0⟩), restricting the ansatz choices compared with standard VQE.
- The work does not demonstrate quantum advantage over classical AFQMC; for the small systems studied, classical trial states would also yield accurate energies.
- The sample-complexity bounds used are acknowledged to be overly pessimistic for small systems, leaving uncertainty about realistic resource estimation at larger scales.
- The hydrogen and NV-center hardware studies rely on highly parallel classical resources (thousands of CPU cores), which may limit reproducibility and practical deployment.
- [inferred] The paper is focused on quantum chemistry and condensed-matter benchmark systems rather than financial-services problems, limiting direct domain transferability to quantum finance.
- [inferred] No comparison is made against state-of-the-art classical solvers on realistic large instances in terms of end-to-end wall-clock time, cost, or accuracy beyond small benchmarks.
- [inferred] Hardware validation is performed on only a small number of devices and qubit counts, so robustness across architectures and calibration drift is only partially established.
- [inferred] Some reported hardware results for hydrogen use an alternative exponentially scaling postprocessing method for efficiency on tiny systems, which weakens the end-to-end empirical validation of the scalable Matchgate approach across all reported points.
## Open questions
- Can the vanishing-overlap problem be mitigated sufficiently at larger system sizes to enable practical quantum advantage?
- Can strategies such as more sophisticated walker wave functions be made compatible with classical-shadows-based QC-QMC?
- What kinds of quantum trial states are best suited for QC-AFQMC, especially under low-depth hardware constraints?
- Is trial-state energy the right criterion for selecting QC-AFQMC trial states, or are there better criteria?
- How practical is Matchgate-shadows-based QC-QMC for realistic systems beyond the small benchmarks studied here?
- Can new methods reduce the classical postprocessing cost of local-energy evaluation enough to make the algorithm scalable?
- To what extent does the observed noise resilience generalize across broader noise models, especially coherent state-preparation noise?
- Which state-preparation noise models can be fully or partially mitigated by the enhanced robust Matchgate shadow protocol?
- How does AFQMC perform when driven by unbiased but shot-noisy estimates of overlap ratios at larger scales?
- Can practical quantum advantage be achieved for systems of interest if overlap decay is postponed or alleviated around approximately 100 orbitals?
- [inferred] How would the method perform under production-like constraints where large classical CPU clusters and low-latency orchestration are unavailable?
- [inferred] How reproducible are the reported hardware results across repeated runs, different calibrations, and different hardware backends?

**Future work:**
- Investigate methods for testing and mitigating exponentially vanishing overlaps at larger system sizes.
- Develop new methods for more efficiently computing the local energy in QC-AFQMC with lower classical postprocessing cost.
- Study larger system sizes on real quantum devices to better assess the merits and scalability of QC-AFQMC.
- Explore improved or alternative quantum trial states for QC-AFQMC and better criteria for choosing them.
- Integrate newer approaches such as algorithmic differentiation for local-quantity evaluation to reduce classical postprocessing overhead.
- Further characterize and improve robust Matchgate shadow protocols, especially for state-preparation noise.
- Investigate additional parallelization strategies, including parallelization across shadow circuits, to reduce runtime.
- Examine compatibility of overlap-mitigation strategies with classical-shadows-based QC-QMC.
- Benchmark the method on more realistic and larger molecules/material systems to assess practical utility.
- [inferred] Perform stronger end-to-end comparisons against state-of-the-art classical AFQMC and multi-Slater trial-state methods on larger instances.
- [inferred] Evaluate robustness and scalability on newer hardware with larger qubit counts and improved fidelities.
- [inferred] Assess whether the algorithmic ideas can transfer to other application domains, including optimization and finance, where overlap estimation and hybrid Monte Carlo structures may differ.
## Key ideas
- #idea:hybrid-approach — The paper demonstrates a hybrid quantum-classical workflow where quantum hardware prepares trial states and classical AFQMC plus shadow postprocessing performs the main Monte Carlo computation.
- #idea:near-term-feasibility — Small end-to-end experiments on IBM and IonQ hardware show that NISQ devices can support accurate overlap-ratio estimation and recover near-FCI energies for tiny benchmark systems.
- #idea:hybrid-approach — VQE/UCCSD trial states are used as imperfect inputs that AFQMC can refine, effectively acting as an error-mitigation layer for noisy variational states.
## Contradictions
- The paper explicitly does not demonstrate quantum advantage and states that classical AFQMC remains competitive for the small systems studied, contradicting broad claims of near-term quantum superiority.
- Its own empirical scaling results show severe classical postprocessing overhead (including O(n^8) local-energy evaluation and large CPU requirements), contradicting optimistic narratives that asymptotically improved shadow methods are already scalable.
- The scalability analysis undercuts speculative advantage claims in related quantum chemistry literature such as 2021_McArdle_QuantumChemistry by showing that polynomial postprocessing can still be practically prohibitive.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
