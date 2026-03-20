---
aliases:
- Quantum optimisation via maximally amplified states
- Quantum optimisation via maximally
authors:
- T. Bennett
- J. B. Wang
auto_detected: true
classification: ''
contradiction_flags:
- contradiction:classical-vs-quantum
doi: 10.48550/arXiv.2111.00796
evidence_type: ''
idea_tags:
- idea:quantum-advantage
- idea:near-term-feasibility
- idea:hybrid-approach
journal_or_venue: arXiv
methodology_tags:
- grover
- quantum-walk
- QAOA
- variational
paper_type: ''
quantum_advantage_claim: theoretical
related_papers: []
relevance_phase1: high
relevance_phase3: high
source_type: peer-reviewed-theoretical
source_type_confidence: high
step1_date: '2026-03-19T23:03:36.641787'
step1_model: Mistral-Large-3
step2_date: '2026-03-19T23:03:39.452295'
step2_model: Mistral-Large-3
step3_date: '2026-03-19T23:03:44.099480'
step3_model: Mistral-Large-3
step4_date: '2026-03-19T23:05:43.445643'
step4_model: Mistral-Large-3
step5_date: '2026-03-19T23:05:52.918722'
step5_model: Mistral-Large-3
step6_date: '2026-03-19T23:05:56.027371'
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
- method/grover
- method/quantum-walk
- method/QAOA
- method/variational
- idea/quantum-advantage
- idea/near-term-feasibility
- idea/hybrid-approach
- contradiction/classical-vs-quantum
title: Quantum optimisation via maximally amplified states
topic_tags:
- portfolio-optimisation
year: 2022
zotero_key: ''
---

## Abstract summary
This paper introduces the Maximum Amplification Optimisation Algorithm (MAOA), a quantum algorithm designed for combinatorial optimisation problems under near-term quantum computing constraints. The MAOA maximally amplifies optimal solutions within a restricted circuit depth, avoiding the computationally expensive variational procedures of other near-term algorithms like QAOA. The authors also present a restricted Grover adaptive search (RGAS) for comparison and demonstrate the MAOA's superior performance on problems such as vehicle routing and portfolio optimisation, showing substantial speedup over classical random sampling.
## Methodology
The paper introduces the Maximum Amplification Optimisation Algorithm (MAOA), a novel quantum algorithm for combinatorial optimisation problems under restricted circuit depth conditions typical of near-term quantum computing. The methodology is theoretical and focuses on maximizing the amplification of optimal solutions within a quantum state, leveraging the Quantum Walk Optimisation Algorithm (QWOA) framework. The MAOA avoids the computationally expensive variational procedure of algorithms like QAOA by using a binary marking function on a complete graph and applying analytically derived optimal parameters (γ = π and t = π/N) repeatedly. The paper also introduces a restricted Grover adaptive search (RGAS) as a comparative baseline. Theoretical foundations include the exploration of amplitude amplification, the impact of graph structure and quality degeneracy, and the connection between the MAOA and Grover’s search. Numerical simulations are conducted on a capacitated vehicle routing problem, a portfolio optimisation problem, and an arbitrarily large problem with normally distributed solution qualities to demonstrate the algorithm's performance and speedup over classical random sampling and RGAS.

**Algorithms used:** MAOA, QAOA, Grover Adaptive Search (GAS), Restricted Grover Adaptive Search (RGAS), Quantum Walk Optimisation Algorithm (QWOA)

**Dataset:** The paper uses three types of datasets/problems: (1) a capacitated vehicle routing problem with 10 locations, (2) a portfolio optimisation problem, and (3) an arbitrarily large problem with normally distributed solution qualities. For the vehicle routing problem, a randomly generated dataset with specific cost matrices and vehicle capacities is used. The portfolio optimisation problem and the normally distributed problem are theoretical constructs with precomputed quality distributions.
## Findings
- [supported] The Maximum Amplification Optimisation Algorithm (MAOA) achieves maximum amplification of optimal solutions in combinatorial optimization problems under restricted circuit depth, outperforming Quantum Approximate Optimisation Algorithm (QAOA) and Quantum Walk Optimisation Algorithm (QWOA) in simulation.
- [supported] MAOA avoids the computationally expensive variational procedure of QAOA by using a binary marking function on a complete graph with analytically derived optimal parameters (γ = π and t = π/N), repeated for r iterations.
- [supported] The MAOA demonstrates substantial speedup over classical random sampling in finding optimal solutions for vehicle routing, portfolio optimization, and normally distributed solution quality problems, with numerical convergence to a theoretically derived upper bound.
- [supported] A binary marking function on a complete graph produces the highest amplification of a single marked (optimal) solution, with maximum amplification achieved by repeated application of the same phase-shift and walk-time parameters.
- [supported] The MAOA's threshold-finding process reliably navigates to the low-convergence regime of the threshold response curve, ensuring maximum amplification (2r + 1)^2 of marked solutions for a given restricted circuit depth r.
- [speculative] The MAOA may provide a practical quantum advantage for near-term quantum devices by maximizing solution amplification under restricted circuit depths, though this claim is not empirically validated on real hardware.
- [disputed] The paper argues that optimizing for expectation value of quality (as in QAOA) does not maximize amplification of optimal solutions, instead favoring sub-optimal solutions due to their numerical superiority in the solution space.

**Results summary:** The paper introduces the Maximum Amplification Optimisation Algorithm (MAOA), a quantum algorithm designed for combinatorial optimization under restricted circuit depths. The MAOA leverages a binary marking function on a complete graph and analytically derived parameters to maximize amplification of optimal solutions without the computationally expensive variational procedure required by QAOA. Simulations on vehicle routing, portfolio optimization, and normally distributed solution quality problems demonstrate that MAOA outperforms classical random sampling and other near-term quantum algorithms (QAOA, RGAS) in speedup and solution quality. The algorithm's performance is quantified by numerical convergence to a theoretical upper bound, and its threshold-finding process ensures reliable navigation to the low-convergence regime for maximum amplification. The paper also introduces a restricted Grover adaptive search (RGAS) as a baseline for comparison.

**Performance claims:**
- MAOA provides substantial speedup over classical random sampling in finding optimal solutions for combinatorial problems.
- MAOA achieves maximum amplification of marked solutions by a factor of (2r + 1)^2 for r iterations, as demonstrated in simulations.
- MAOA consistently outperforms RGAS in all tested problem instances (vehicle routing, portfolio optimization, and normally distributed solution qualities).
## Quantum advantage claim
**Classification:** theoretical

The MAOA claims a theoretical quantum advantage by maximizing solution amplification under restricted circuit depths, with performance validated through simulations. The advantage is derived from the algorithm's ability to avoid the variational overhead of QAOA and achieve near-optimal amplification of solutions. However, the claim is not demonstrated on real quantum hardware, and the advantage is contingent on the algorithm's scalability and practical implementation.
## Limitations
- The MAOA assumes a binary marking function to maximize amplification of optimal solutions, which may not be optimal for problems with non-binary or continuous quality distributions [inferred]
- The algorithm relies on the complete graph structure for quantum walks, which may not be the most efficient or feasible for all problem types or hardware constraints [inferred]
- The theoretical performance of MAOA is derived under the assumption of noise-free quantum operations, which is not realistic for near-term quantum devices
- The paper does not provide empirical validation of the MAOA on real quantum hardware, limiting conclusions to simulated environments
- The comparison with QAOA and other algorithms is based on theoretical and simulated performance, without accounting for practical implementation challenges such as gate fidelity or qubit connectivity
- The MAOA's performance is demonstrated on specific problems (vehicle routing, portfolio optimization), but its generalizability to other combinatorial optimization problems remains untested [inferred]
- The threshold-finding process in MAOA assumes that the quality distribution is sufficiently smooth and continuous, which may not hold for all real-world problems [inferred]
- The computational effort metric (number of calls to the quality function) does not account for the overhead of quantum walk operations, which could be significant in practice [inferred]
- The paper does not address how the MAOA would perform in the presence of noise or decoherence, which are critical factors for near-term quantum devices
- The RGAS and MAOA are compared under the same rotation count restrictions, but the impact of hardware-specific constraints (e.g., gate depth limits) is not explored
## Open questions
- How does the MAOA perform on real quantum hardware with noise and limited qubit counts?
- What is the impact of non-ideal quality distributions (e.g., skewed, multimodal) on the MAOA's threshold-finding process?
- Can the MAOA be adapted to problems where the optimal solution is not well-defined by a binary threshold (e.g., multi-objective optimization)?
- How does the MAOA compare to hybrid quantum-classical approaches (e.g., QAOA with classical post-processing) in terms of practical speedup?
- What are the trade-offs between the MAOA's circuit depth and its robustness to noise?
- How does the MAOA scale with problem size for problems beyond those tested (e.g., larger portfolio optimization or vehicle routing instances)?
- Is the complete graph assumption for quantum walks feasible for large-scale problems on near-term quantum devices?
- What are the implications of the MAOA's reliance on Grover-like amplification for problems with degenerate optimal solutions?
- How does the MAOA perform when the quality distribution is not known a priori and must be estimated dynamically?
- What are the limitations of the MAOA in problems where the solution space is not uniformly distributed or lacks symmetry?

**Future work:**
- Empirical validation of the MAOA on real quantum hardware (e.g., IBM, Rigetti, or IonQ devices)
- Extension of the MAOA to problems with non-binary or continuous quality distributions
- Investigation of noise mitigation techniques to improve the MAOA's performance on near-term devices
- Comparison of the MAOA with hybrid quantum-classical algorithms in practical settings
- Development of adaptive threshold-finding methods for problems with unknown or dynamic quality distributions
- Exploration of alternative graph structures for quantum walks that may improve amplification efficiency
- Application of the MAOA to larger-scale combinatorial optimization problems (e.g., logistics, finance, or machine learning)
- Integration of the MAOA with classical optimization techniques to enhance solution quality
- Analysis of the MAOA's performance under hardware-specific constraints (e.g., qubit connectivity, gate fidelity)
- Development of theoretical bounds for the MAOA's performance in the presence of noise and decoherence
## Key ideas
- #idea:quantum-advantage — MAOA demonstrates substantial speedup over classical random sampling and outperforms QAOA/RGAS in amplifying optimal solutions for portfolio optimisation under restricted circuit depth
- #idea:near-term-feasibility — MAOA is designed for near-term quantum devices, avoiding computationally expensive variational procedures and leveraging restricted circuit depths
- #idea:hybrid-approach — MAOA uses a binary marking function on a complete graph with analytically derived optimal parameters, potentially simplifying hybrid quantum-classical implementations
- #limitation:simulation-only — MAOA's performance is only validated via classical simulations, not real quantum hardware
- #limitation:noise — The paper does not address hardware noise, qubit connectivity constraints, or error mitigation, which may impact MAOA's real-world applicability
- #limitation:data-encoding — MAOA's reliance on a binary marking function may limit its applicability to problems with non-binary or multi-objective quality distributions
## Contradictions
- #contradiction:classical-vs-quantum — The paper claims that optimising for expectation value of quality (as in QAOA) does not maximise amplification of optimal solutions, contradicting prior work supporting QAOA’s effectiveness for portfolio optimisation (e.g., Golden et al. [35])
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
