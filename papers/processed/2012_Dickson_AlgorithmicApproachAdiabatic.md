---
aliases:
- Algorithmic approach to adiabatic quantum optimization
- Algorithmic approach adiabatic quantum
authors:
- Neil G. Dickson
- Mohammad H. Amin
auto_detected: true
classification: ''
contradiction_flags:
- contradiction:classical-vs-quantum
doi: 10.48550/arXiv.1108.3303
evidence_type: ''
idea_tags:
- idea:quantum-advantage
- idea:near-term-feasibility
- idea:hybrid-approach
journal_or_venue: arXiv
methodology_tags:
- quantum-annealing
- quantum-simulation
- classical-simulation
paper_type: ''
quantum_advantage_claim: speculative
related_papers:
- 2010_Altshuler_AdiabaticQuantumOptimization
relevance_phase1: medium
relevance_phase3: not-yet-assessed
source_type: preprint
source_type_confidence: high
step1_date: '2026-03-19T22:44:04.118558'
step1_model: Mistral-Large-3
step2_date: '2026-03-19T22:44:08.132553'
step2_model: Mistral-Large-3
step3_date: '2026-03-19T22:44:25.063720'
step3_model: Mistral-Large-3
step4_date: '2026-03-19T22:45:17.238477'
step4_model: Mistral-Large-3
step5_date: '2026-03-19T22:45:27.833416'
step5_model: Mistral-Large-3
step6_date: '2026-03-19T22:45:34.310416'
step6_model: Mistral-Large-3
steps_completed:
- 1
- 2
- 3
- 4
- 5
- 6
tags:
- topic/portfolio-optimisation
- method/quantum-annealing
- method/quantum-simulation
- method/classical-simulation
- idea/quantum-advantage
- idea/near-term-feasibility
- idea/hybrid-approach
- contradiction/classical-vs-quantum
title: Algorithmic approach to adiabatic quantum optimization
topic_tags:
- portfolio-optimisation
year: 2011
zotero_key: ''
---

## Abstract summary
This preprint introduces a heuristic adiabatic quantum algorithm designed to mitigate inefficiencies in adiabatic quantum optimization caused by exponentially small energy gaps. The algorithm iteratively adjusts single-qubit tunneling energies to penalize pathways leading to local minima, using information gathered from non-adiabatic evolution. The approach is tested on hard instances of the maximum independent set problem, demonstrating its ability to eliminate perturbative crossings in a small number of iterations.
## Methodology
The paper presents a heuristic adiabatic quantum algorithm designed to eliminate exponentially small gaps caused by anticrossings between eigenstates corresponding to local and global minima of the problem Hamiltonian in adiabatic quantum optimization (AQO). The algorithm iteratively gathers information about local minima reached after non-adiabatic evolution and uses this to penalize pathways to these local minima by adjusting the initial Hamiltonian's single-qubit tunneling energies (∆i). The study focuses on the maximum independent set (MIS) problem, generating 64-qubit random instances skewed to be extremely hard, with 10^5 to 10^6 highly-degenerate local minima. Quantum Monte Carlo (QMC) simulations are employed to test the algorithm's efficacy, demonstrating that it can solve all generated instances within approximately 10 iterations.

**Algorithms used:** Adiabatic Quantum Optimization (AQO), Quantum Monte Carlo (QMC)

**Experimental setup:** The experimental setup involves simulating the adiabatic quantum algorithm using Quantum Monte Carlo (QMC) methods. The simulations are performed on 64-qubit random instances of the maximum independent set problem, designed to be extremely challenging with a high number of degenerate local minima. The energy scales A(s) and B(s) are derived from superconducting flux qubits, and the annealing time per computation is set to 0.08 µs with 500 repetitions per iteration.

**Dataset:** 64-qubit random instances of the maximum independent set problem, specifically generated to have a unique maximum independent set and between 10^5 and 10^6 highly-degenerate local minima.
## Findings
- [supported] The proposed adiabatic quantum algorithm successfully eliminates exponentially small gaps caused by anticrossings in the system Hamiltonian for 64-qubit random instances of the maximum independent set (MIS) problem, solving all instances within ~10 iterations using quantum Monte Carlo simulations.
- [supported] The algorithm leverages non-adiabatic evolution to sample local minima, then penalizes pathways to these minima by adjusting single-qubit tunneling energies (∆i), demonstrating convergence in an average of 3.0 iterations for the tested instances.
- [speculative] The authors suggest that perturbative crossings, which render adiabatic quantum optimization inefficient, can be systematically avoided by tuning Hamiltonian parameters, though this claim is validated only via simulation and not real hardware.
- [speculative] The algorithm's success on 64-qubit problems implies potential scalability to larger problem sizes, but this remains untested empirically.
- [supported] Quantum Monte Carlo (QMC) simulations show that the algorithm reduces the adiabatic time scale (ta) below 16 µs for all tested instances, enabling high-probability (>92%) success in identifying the global minimum within 500 runs per iteration.
- [disputed] The paper challenges prior findings (e.g., Altshuler et al. 2010) that NP-complete problems cannot be solved efficiently via adiabatic quantum optimization, by demonstrating that perturbative crossings can be mitigated through heuristic parameter tuning.

**Results summary:** The paper introduces a heuristic adiabatic quantum algorithm designed to eliminate exponentially small energy gaps (anticrossings) in the Hamiltonian of hard optimization problems. Using quantum Monte Carlo simulations, the authors demonstrate that the algorithm can solve 64-qubit random instances of the maximum independent set problem—characterized by 10^5 to 10^6 highly degenerate local minima—within an average of 3 iterations. The approach involves non-adiabatic evolution to sample local minima, followed by penalization of pathways to these minima via adjustments to single-qubit tunneling energies. All 50 tested instances were solved within 13 iterations, with 30 solved in just 2 iterations. The results suggest that perturbative crossings, previously thought to limit adiabatic quantum optimization, can be mitigated through iterative parameter tuning, though the findings are derived from simulations rather than real quantum hardware.

**Performance claims:**
- All 50 tested 64-qubit MIS instances solved within 13 iterations
- Average of 3.0 iterations required for convergence
- 30 out of 50 instances solved in 2 iterations
- Adiabatic time scale (ta) reduced below 16 µs for all instances, enabling >92% success probability per iteration
- Algorithm runtime per iteration: O(rn^2) on a single classical processor (r = 500 samples, n = 64 qubits)
## Quantum advantage claim
**Classification:** speculative

The paper claims that the proposed algorithm can mitigate inefficiencies in adiabatic quantum optimization caused by perturbative crossings, but this advantage is demonstrated only via quantum Monte Carlo simulations and not on real quantum hardware. The scalability and practical feasibility of the approach remain unvalidated empirically, and the results do not conclusively demonstrate a quantum advantage over classical methods for the tested problem instances.
## Limitations
- Lack of peer review as the paper is a preprint [inferred]
- Algorithm tested only on synthetic 64-qubit instances of the maximum independent set problem, not real-world financial services problems [inferred]
- Experiments limited to quantum Monte Carlo (QMC) simulations; no validation on actual quantum hardware
- Assumptions about the Hamiltonian structure (e.g., uniform ∆i, non-degenerate states) may not hold in practical scenarios
- Algorithm relies on perturbative crossings being eliminable via tuning of ∆i, which may not generalize to all problem types
- Test instances were artificially skewed to be extremely hard, which may not reflect typical problem distributions in financial services [inferred]
- No comparison with state-of-the-art classical optimization methods for the maximum independent set problem [inferred]
- Scalability beyond 64 qubits is untested; performance on larger problem sizes remains unclear
- Algorithm requires multiple iterations (up to 13 in tests), which may limit practical applicability in time-sensitive financial applications [inferred]
- Dependence on QMC simulations for sampling may not fully capture noise and decoherence effects present in real quantum hardware [inferred]
- Feasible range of ∆i values (1/4 to 8) is hardware-specific and may not apply to other quantum computing platforms [inferred]
## Open questions
- How does the algorithm perform on problem instances with degenerate global minima, which are more common in real-world scenarios?
- What is the impact of hardware noise and decoherence on the algorithm's performance when run on actual quantum devices?
- Can the algorithm be extended to other NP-hard problems relevant to financial services, such as portfolio optimization or risk analysis?
- How does the algorithm scale with problem size beyond 64 qubits?
- What is the trade-off between the number of iterations required and the quality of the solution?
- How sensitive is the algorithm to the choice of β and other hyperparameters?
- Can the algorithm be combined with other quantum optimization techniques (e.g., QAOA) to improve performance?
- What is the minimum gap size that the algorithm can effectively eliminate in practice?
- How does the algorithm perform on real-world financial datasets, which may have different structural properties than the synthetic instances tested?

**Future work:**
- Test the algorithm on real quantum hardware (e.g., D-Wave systems) to validate simulation results
- Extend the algorithm to handle degenerate global minima and other problem types beyond the maximum independent set problem
- Investigate the scalability of the algorithm to larger problem sizes (e.g., 100+ qubits)
- Compare the algorithm's performance with state-of-the-art classical optimization methods for relevant financial problems
- Explore hybrid quantum-classical approaches to improve the algorithm's efficiency and robustness
- Develop methods to automatically tune hyperparameters (e.g., β, ∆i range) for optimal performance
- Apply the algorithm to real-world financial datasets to assess its practical utility
- Study the impact of noise and error mitigation techniques on the algorithm's performance in real hardware
- Investigate the algorithm's potential for solving multi-period or dynamic optimization problems in finance
## Key ideas
- #idea:quantum-advantage — Proposes a heuristic adiabatic quantum algorithm to mitigate inefficiencies from exponentially small energy gaps in hard optimization problems, demonstrated on 64-qubit MIS instances (relevant to portfolio-optimisation via QUBO formulations)
- #idea:near-term-feasibility — Algorithm shows potential for near-term applicability in solving NP-hard problems with degenerate local minima, though validated only via simulations
- #idea:hybrid-approach — Iterative adjustment of initial Hamiltonian parameters (e.g., single-qubit tunneling energies) suggests a hybrid quantum-classical tuning mechanism for optimization
- #limitation:no-empirical-validation — Claims of mitigating AQO inefficiencies are speculative and lack real hardware validation or comparison with classical solvers
- #limitation:simulation-only — Results are derived from Quantum Monte Carlo simulations, not actual quantum processing units (QPUs)
- #contradiction:classical-vs-quantum — Challenges prior theoretical assumptions (e.g., Altshuler et al., 2010) about AQO inefficiency for NP-complete problems, arguing they rely on overly restrictive assumptions
## Contradictions
- The paper disputes prior theoretical claims (e.g., Altshuler et al., 2010) that adiabatic quantum optimization is inherently inefficient for NP-complete problems due to perturbative crossings, arguing that such claims assume uniform ∆i or non-degenerate minima. However, this contradiction is not empirically validated beyond simulation results.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->

## Experiment details
### Input
The input consists of 64-node graphs with a unique maximum independent set (MIS) of size 20, generated using a targeted approach to ensure extremely small minimum gaps. The graphs have approximately 220 edges and are constructed to include many clusters of local minima connected by 2-bit-flip paths.

### Process
1. Initialize ∆i = 1 for all qubits. 2. Perform quantum annealing r=500 times per iteration, saving each result. 3. If a sufficient result (global minimum) is obtained, terminate the process. 4. Compute µi using QMC sampling to estimate the curvature contributions of local minima. 5. Adjust ∆i values using ∆i,new = ∆1-β_i,old * µ-β_i, where β = 1/(κ + 1) and κ is the iteration number. 6. Rescale ∆i values to remain within a feasible range (1/4 to 8). 7. Repeat the process until the global minimum is found or the maximum iterations are reached.

### Output
The output includes the identification of the global minimum (MIS) of the problem Hamiltonian, the number of iterations required to eliminate perturbative crossings, and visualizations of the ground state expectation values ⟨σ(i)_z⟩ for each qubit across the adiabatic evolution. Success is defined as either achieving an adiabatic time ta < 16 µs or a probability > 0.005 of states descending to the global minimum before a perturbative crossing.

### Parameters
- qubits: 64
- annealing_time: 0.08
- repetitions_per_iteration: 500
- iterations: 13
- feasible_range_∆i: [0.25, 8]
- β: 1/(κ + 1) where κ is the iteration number

### Hardware
Simulations are performed using Quantum Monte Carlo (QMC) methods. The energy scales A(s) and B(s) are modeled after superconducting flux qubits similar to those used in D-Wave systems.

### Reproducibility
The paper provides detailed steps for generating the problem instances and the iterative algorithm, including parameter choices and rescaling methods. However, the specific QMC simulation code and generated datasets are not explicitly made available. The methodology is described in sufficient detail to replicate the study, assuming access to QMC simulation tools.
