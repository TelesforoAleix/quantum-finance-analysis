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
step1_date: '2026-03-19T11:37:47.941789'
step1_model: Mistral-Large-3
step2_date: '2026-03-19T11:37:54.230251'
step2_model: Mistral-Large-3
step3_date: '2026-03-19T11:38:10.794316'
step3_model: Mistral-Large-3
step4_date: '2026-03-19T11:38:34.588077'
step4_model: Mistral-Large-3
step5_date: '2026-03-19T11:38:59.877625'
step5_model: Mistral-Large-3
step6_date: '2026-03-19T11:39:16.354514'
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
This preprint introduces a heuristic adiabatic quantum algorithm designed to mitigate inefficiencies in adiabatic quantum optimization caused by anticrossings with exponentially small energy gaps. The algorithm iteratively adjusts the initial Hamiltonian to penalize pathways leading to local minima, using information gathered from non-adiabatic evolution. The approach is tested on challenging 64-qubit instances of the maximum independent set problem, demonstrating its effectiveness in eliminating perturbative crossings within a few iterations.
## Methodology
The paper presents a heuristic adiabatic quantum algorithm designed to eliminate exponentially small gaps caused by anticrossings between eigenstates corresponding to local and global minima of the problem Hamiltonian in adiabatic quantum optimization (AQO). The methodology involves an iterative process where information about local minima reached after non-adiabatic evolution is used to adjust the initial Hamiltonian by penalizing pathways to these local minima. The algorithm targets the Maximum Independent Set (MIS) problem, generating 64-qubit random instances skewed to be extremely hard, with between 10^5 and 10^6 highly-degenerate local minima. Quantum Monte Carlo (QMC) simulations are employed to simulate the algorithm's performance, sampling computation basis states to approximate the ground state of the system. The iterative adjustments of single-qubit tunneling energies (∆i) are guided by sampled data to reduce the curvature of local minima eigenstates without significantly affecting the global minimum. The success of the algorithm is evaluated based on the adiabatic time scale and the probability of states descending to the global minimum.

**Algorithms used:** Adiabatic Quantum Optimization (AQO), Quantum Monte Carlo (QMC)

**Experimental setup:** The experimental setup involves Quantum Monte Carlo (QMC) simulations to sample computation basis states proportional to their appearance in the ground state of the system. The simulations use energy scales extracted from superconducting flux qubits, with 500 repetitions per iteration and an annealing time of 0.08 µs per computation. The algorithm is tested on 64-qubit random instances of the Maximum Independent Set problem, generated using a targeted approach to ensure extremely small minimum gaps. The feasible range for ∆i values is set between 1/4 and 8, with rescaling applied in each iteration to maintain these bounds.

**Dataset:** Randomly generated 64-qubit instances of the Maximum Independent Set (MIS) problem, skewed to have between 10^5 and 10^6 highly-degenerate local minima and a unique global minimum. The graph instances are created using a depth-first search method to ensure the presence of perturbative crossings and small minimum gaps.
## Findings
- [supported] The proposed iterative adiabatic quantum algorithm successfully eliminates exponentially small gaps caused by anticrossings in the system Hamiltonian for 64-qubit random instances of the maximum independent set problem, solving all 50 test instances within 13 iterations.
- [supported] Quantum Monte Carlo simulations demonstrate that the algorithm solves extremely hard problem instances (with 10^5 to 10^6 highly degenerate local minima) in an average of 3.0 iterations.
- [speculative] The algorithm's approach to penalizing pathways to local minima by adjusting single-qubit tunneling energies (∆i) may generalize to other NP-hard problems beyond the maximum independent set problem.
- [speculative] The authors suggest that the algorithm could avoid first-order quantum phase transitions in adiabatic quantum optimization, potentially overcoming previously claimed inefficiencies for NP-complete problems.
- [speculative] The use of a weighted geometric average for ∆i updates (β = 1/(κ+1)) is claimed to robustly balance penalization of new local minima while retaining memory of previous iterations, though this is not empirically validated beyond the 64-qubit simulations.
- [disputed] The paper challenges prior theoretical claims (e.g., Altshuler et al., 2010) that adiabatic quantum optimization is inherently inefficient for NP-complete problems due to perturbative crossings, arguing that such claims rely on overly restrictive assumptions (e.g., uniform ∆i, non-degenerate minima).

**Results summary:** The paper presents a heuristic adiabatic quantum algorithm designed to eliminate exponentially small energy gaps in the system Hamiltonian, which are known to render adiabatic quantum optimization (AQO) inefficient. Using quantum Monte Carlo simulations, the authors demonstrate that their algorithm can solve 64-qubit random instances of the maximum independent set problem—engineered to be extremely hard with 10^5 to 10^6 degenerate local minima—in an average of 3 iterations. All 50 test instances were solved within 13 iterations, with 30 instances resolved in just 2 iterations. The algorithm works by iteratively penalizing pathways to clusters of local minima through adjustments to single-qubit tunneling energies (∆i), leveraging information gathered from non-adiabatic runs. While the results are derived from simulations rather than real quantum hardware, they suggest that AQO may be more robust to perturbative crossings than previously theorized, provided certain assumptions (e.g., uniform ∆i, non-degenerate minima) are relaxed.

**Performance claims:**
- All 50 test instances of 64-qubit maximum independent set problems solved within 13 iterations
- Average of 3.0 iterations required to solve instances with 10^5 to 10^6 highly degenerate local minima
- 30 out of 50 instances solved in 2 iterations
- Algorithm succeeds with 500 samples per iteration and an annealing time of 0.08 µs per sample
## Quantum advantage claim
**Classification:** speculative

The claimed advantage is based on simulation results only, with no empirical validation on real quantum hardware. The authors argue that their algorithm could overcome inefficiencies in adiabatic quantum optimization for NP-hard problems, but this remains theoretical and untested at scale. The paper does not demonstrate a provable quantum speedup over classical methods.
## Limitations
- Algorithm tested only on 64-qubit instances of the maximum independent set problem, limiting generalizability to larger or different problem types [inferred]
- Experiments conducted using quantum Monte Carlo (QMC) simulations rather than real quantum hardware, which may not fully capture hardware-specific noise and decoherence effects
- Lack of peer review as this is a preprint, raising questions about methodological rigor and reproducibility [inferred]
- Algorithm assumes a closed quantum system, whereas real quantum hardware operates in open systems with environmental interactions
- Test instances were artificially generated to be extremely hard (with 10^5 to 10^6 highly-degenerate local minima), which may not represent real-world problem distributions [inferred]
- The algorithm's success is defined by a specific criterion (ta < 16 µs or probability > 0.005), which may not align with practical requirements for financial services applications [inferred]
- Assumes precise control over single-qubit tunneling energies (∆i), which may be challenging to implement on near-term quantum hardware
- The iterative approach requires multiple runs (500 per iteration), leading to high computational overhead [inferred]
- No comparison with state-of-the-art classical solvers for the maximum independent set problem, leaving performance benchmarks unclear [inferred]
- The algorithm's effectiveness is demonstrated only for problems with a unique global minimum, which may not cover all relevant financial optimization scenarios [inferred]
## Open questions
- How does the algorithm perform on problems with multiple global minima or highly symmetric solutions?
- What is the impact of hardware noise and decoherence on the algorithm's performance in real-world quantum devices?
- Can the algorithm be extended to other NP-hard problems relevant to financial services, such as portfolio optimization or risk analysis?
- How does the algorithm scale with problem size beyond 64 qubits, particularly for industry-relevant instances?
- What are the trade-offs between the number of iterations required and the quality of the solution in practical settings?
- How sensitive is the algorithm to the choice of parameters (e.g., β, feasible range of ∆i) for different problem types?
- Can the algorithm be adapted to leverage hybrid quantum-classical approaches for improved efficiency?

**Future work:**
- Test the algorithm on real quantum hardware to validate simulation results and assess noise resilience
- Extend the algorithm to larger problem instances (e.g., 100+ qubits) to evaluate scalability
- Apply the algorithm to other combinatorial optimization problems relevant to financial services, such as portfolio optimization or fraud detection
- Explore hybrid quantum-classical approaches to reduce the number of iterations or improve solution quality
- Investigate the impact of different annealing schedules (A(s) and B(s)) on algorithm performance
- Develop methods to dynamically adjust the feasible range of ∆i based on problem characteristics
- Compare the algorithm's performance with state-of-the-art classical solvers to establish practical benchmarks
- Study the algorithm's robustness to hardware imperfections, such as qubit connectivity constraints or calibration errors
## Key ideas
- #idea:quantum-advantage — Proposes a heuristic adiabatic quantum algorithm to mitigate inefficiencies from exponentially small energy gaps in hard optimization problems, demonstrated on 64-qubit MIS instances (relevant to portfolio-optimisation via QUBO formulations)
- #idea:near-term-feasibility — Algorithm shows potential for near-term applicability in solving NP-hard problems with degenerate local minima, though validated only via simulations
- #idea:hybrid-approach — Iterative adjustment of initial Hamiltonian parameters (e.g., single-qubit tunneling energies) suggests a hybrid quantum-classical tuning mechanism for optimization
- #limitation:no-empirical-validation — Claims of mitigating AQO inefficiencies are speculative and lack real hardware validation or comparison with classical solvers
- #limitation:simulation-only — Results are derived from Quantum Monte Carlo simulations, not actual quantum processing units (QPUs)
- #contradiction:classical-vs-quantum — Challenges prior theoretical assumptions (e.g., Altshuler et al., 2010) about AQO inefficiency for NP-complete problems, arguing they rely on overly restrictive assumptions
## Contradictions
- The paper disputes prior theoretical claims (e.g., Altshuler et al., 2010) that adiabatic quantum optimization is inherently inefficient for NP-complete problems due to perturbative crossings, arguing that such claims assume uniform ∆i or non-degenerate minima. However, the contradiction is not empirically validated beyond simulation results.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
