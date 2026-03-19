---
aliases:
- Solving General QUBOs with Warm-Start QAOA via a Reduction to Max-Cut
- Solving General QUBOs Warm
authors:
- Bikrant Bhattacharyya
- Michael Capriotti
- Reuben Tate
auto_detected: true
classification: ''
contradiction_flags: []
doi: XXXXXXX.XXXXXXX
evidence_type: ''
idea_tags:
- idea:near-term-feasibility
- idea:hybrid-approach
journal_or_venue: ACM Transactions on Quantum Computing
methodology_tags:
- QAOA
- QUBO
- classical-simulation
paper_type: ''
quantum_advantage_claim: not-applicable
related_papers: []
relevance_phase1: medium
relevance_phase3: not-yet-assessed
source_type: peer-reviewed-empirical
source_type_confidence: high
step1_date: '2026-03-18T22:51:31.854974'
step1_model: Mistral-Large-3
step2_date: '2026-03-18T22:51:34.883946'
step2_model: Mistral-Large-3
step3_date: '2026-03-18T22:51:39.910991'
step3_model: Mistral-Large-3
step4_date: '2026-03-18T22:51:52.815156'
step4_model: Mistral-Large-3
step5_date: '2026-03-18T22:52:41.759088'
step5_model: Mistral-Large-3
step6_date: '2026-03-18T22:52:46.533307'
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
- method/QAOA
- method/QUBO
- method/classical-simulation
- idea/near-term-feasibility
- idea/hybrid-approach
title: Solving General QUBOs with Warm-Start QAOA via a Reduction to Max-Cut
topic_tags:
- portfolio-optimisation
year: 2025
zotero_key: ''
---

## Abstract summary
This paper explores an approach to improve the Quantum Approximate Optimization Algorithm (QAOA) by warm-starting it with solutions derived from semidefinite programming relaxations of Max-Cut problems. The authors propose a method to transform general Quadratic Unconstrained Binary Optimization (QUBO) problems into Max-Cut instances, enabling the use of existing warm-start techniques. The study empirically compares this approach with a direct QUBO relaxation method across various problem types, assessing performance in terms of approximation quality and solution optimality.
## Methodology
The paper presents an empirical study comparing two warm-start approaches for the Quantum Approximate Optimization Algorithm (QAOA) to solve Quadratic Unconstrained Binary Optimization (QUBO) problems. The first approach relaxes the QUBO directly (QUBO-Relaxed), while the second maps QUBO instances to Max-Cut problems and applies a semidefinite programming (SDP) relaxation-based warm-start. The study evaluates these approaches on various QUBO instances, including randomly generated QUBOs and specific problems like the traveling salesman problem, maximum independent set, and portfolio optimization. The warm-start initial states are constructed using solutions from classical relaxations (SDP or QUBO relaxations) and encoded into quantum states via Bloch sphere representations. The QAOA parameters are optimized classically, and performance is measured using approximation ratios and optimal sampling probabilities. Experiments are conducted on quantum simulators, with problem sizes up to 16 variables and QAOA depths up to 5.

**Algorithms used:** QAOA

**Experimental setup:** Experiments were conducted using quantum simulators (no real QPU mentioned). The study tested QUBO instances with up to 16 variables, corresponding to 17-qubit Max-Cut instances. For each problem type, 1000 instances were generated, with 10 selected for deeper analysis at QAOA depths from 1 to 5. Classical optimizations for warm-starts were performed using stochastic perturbations and local optimizations. The vertex-at-top heuristic was applied to test the impact of different rotations on the warm-start initial state.

**Dataset:** The datasets included: (1) randomly generated QUBOs with matrix elements drawn uniformly from [-1, 1] or discretely from {-1, 1}; (2) QUBOs derived from specific combinatorial optimization problems, such as the traveling salesman problem (5 cities randomly placed in [-1, 1]²), portfolio optimization (simulated stock prices with covariance and mean return calculations), and maximum independent set problems on Erdős–Rényi and Newman–Watts–Strogatz graphs.
## Findings
- [supported] The warm-start QAOA approach using a reduction to Max-Cut achieves higher approximation ratios and optimal sampling probabilities compared to the QUBO-relaxation approach for most problem types, including portfolio optimization and maximum independent set (MIS).
- [supported] The best warm-start approach (GW2, GW3, BM2, or BM3) is highly problem-dependent, with performance varying based on the metric (e.g., approximation ratio vs. optimal sampling probability).
- [supported] For 16-variable QUBOs, the GW2 warm-start with a 'last qubit' vertex-at-top rotation generally outperforms other rotation choices (first qubit or no rotation) across most problem types, including random QUBOs, portfolio optimization, and MIS.
- [supported] The QUBO-relaxation warm-start performs better with 50 random initializations than with 10, particularly for constrained problems like the traveling salesman problem (TSP) and MIS, where the difference in optimal sampling probability is most pronounced.
- [supported] For portfolio optimization, the GW2 warm-start achieves an instance-specific approximation ratio >0.25 standard deviations higher than the QUBO-relaxation approach, despite both methods yielding high approximation ratios.
- [supported] The optimal sampling probability for TSP remains low (<0.2) for all warm-start approaches, likely due to the large number of constraint terms in the QUBO formulation.
- [supported] The auxiliary qubit introduced in the QUBO-to-Max-Cut mapping is frequently the optimal choice for the vertex-at-top heuristic, reducing the overhead of testing multiple rotations from O(n) to O(1).
- [speculative] The authors suggest that the observed performance differences between warm-start approaches may generalize to larger problem sizes, though this is not empirically validated in the study.
- [speculative] The paper implies that warm-start QAOA could outperform classical methods for certain combinatorial optimization problems at scale, but no direct comparison to classical solvers is provided.

**Results summary:** The paper empirically evaluates two warm-start approaches for QAOA—QUBO-relaxation and a reduction to Max-Cut—across 16-variable QUBO instances derived from random matrices, portfolio optimization, TSP, and MIS problems. Results are obtained via simulation (not real hardware) and show that the Max-Cut reduction (particularly the GW2 warm-start with a 'last qubit' vertex-at-top rotation) generally outperforms QUBO-relaxation in terms of approximation ratio and optimal sampling probability. Performance is problem-dependent, with portfolio optimization and MIS favoring the Max-Cut approach, while TSP exhibits low sampling probabilities for all methods. The QUBO-relaxation approach benefits from more random initializations (50 vs. 10), especially for constrained problems. The study highlights the importance of problem-specific warm-start selection but does not demonstrate quantum advantage over classical methods.

**Performance claims:**
- GW2 warm-start with 'last qubit' rotation achieves an average instance-specific approximation ratio of ~0.9 for portfolio optimization at depth p=5 (vs. ~0.8 for QUBO-relaxation).
- GW2 warm-start with 'last qubit' rotation achieves an optimal sampling probability of ~0.6 for portfolio optimization at depth p=5 (vs. ~0.5 for QUBO-relaxation).
- For MIS problems, GW2 warm-start with 'last qubit' rotation yields an approximation ratio within 0.25 standard deviations of QUBO-relaxation with 50 initializations.
- QUBO-relaxation with 50 initializations improves optimal sampling probability by ~0.1-0.2 over 10 initializations for TSP and MIS problems.
- The auxiliary qubit in the QUBO-to-Max-Cut mapping reduces vertex-at-top rotation overhead from O(n) to O(1).
## Quantum advantage claim
**Classification:** not-applicable

The paper does not claim or demonstrate quantum advantage. All results are from simulations, and no comparison to classical state-of-the-art solvers is provided. The focus is on relative performance between warm-start approaches for QAOA.
## Limitations
- Experiments limited to QUBOs with up to 16 variables (17 qubits for Max-Cut reduction) due to hardware constraints and computational feasibility [inferred]
- Only tested on synthetic or randomly generated problem instances (e.g., random QUBOs, synthetic portfolio data, TSP with random city placements, random graphs for MIS), not real-world financial datasets
- Performance metrics (approximation ratio and optimal sampling probability) are instance-specific and highly dependent on problem type, limiting generalizability of findings
- No empirical validation on real quantum hardware; all experiments conducted via classical simulation of QAOA
- Noise and decoherence effects not considered in simulations, which may significantly degrade performance on near-term quantum devices [inferred]
- Vertex-at-top heuristic introduces an O(n) overhead for testing all possible rotations, though the auxiliary qubit in the QUBO-to-Max-Cut mapping reduces this overhead in practice
- QUBO-relaxation warm-start performance is sensitive to the number of random initializations, with no guarantee of optimality for non-convex relaxations
- Portfolio optimization results may not generalize to real-world scenarios due to simplified assumptions (e.g., synthetic price data, fixed budget constraints) [inferred]
- Lack of comparison with state-of-the-art classical solvers (e.g., Gurobi, CPLEX) to benchmark quantum advantage [inferred]
- Depth of QAOA circuits limited to p=5, which may not be sufficient to observe convergence to optimal solutions for larger or more complex problem instances [inferred]
- Optimal sampling probabilities for constrained problems (e.g., TSP, MIS) are relatively low, indicating challenges in identifying feasible solutions
## Open questions
- How does the performance of warm-start QAOA scale with larger problem sizes (e.g., >20 variables) or more complex financial optimization tasks?
- What is the impact of hardware noise and decoherence on the approximation ratio and optimal sampling probability for warm-start QAOA?
- Can the QUBO-to-Max-Cut reduction be optimized further to reduce the overhead of auxiliary qubits or improve solution quality?
- How do warm-start approaches compare to other quantum optimization algorithms (e.g., VQE, QA) for financial applications?
- What problem-specific characteristics (e.g., constraint density, matrix structure) determine the superiority of one warm-start method over another?
- Can hybrid quantum-classical approaches (e.g., combining QAOA with classical post-processing) mitigate the low optimal sampling probabilities observed for constrained problems?
- How does the performance of warm-start QAOA vary across different quantum hardware architectures (e.g., superconducting vs. trapped-ion qubits)?
- What is the trade-off between circuit depth and solution quality for warm-start QAOA in near-term devices?

**Future work:**
- Test warm-start QAOA on real quantum hardware to evaluate performance under noise and decoherence
- Extend experiments to larger problem sizes (e.g., 30+ variables) to assess scalability
- Compare warm-start QAOA with state-of-the-art classical solvers for benchmarking quantum advantage
- Explore adaptive warm-start strategies that dynamically select the best relaxation method (e.g., GW vs. QUBO-relaxation) based on problem type
- Investigate hybrid quantum-classical techniques (e.g., error mitigation, classical post-processing) to improve solution quality for constrained problems
- Apply warm-start QAOA to real-world financial datasets (e.g., portfolio optimization with historical market data, risk management scenarios)
- Develop problem-specific warm-start heuristics for financial applications (e.g., tailored relaxations for portfolio optimization or option pricing)
- Study the impact of different quantum hardware characteristics (e.g., gate fidelity, qubit connectivity) on warm-start QAOA performance
- Extend the QUBO-to-Max-Cut reduction to other combinatorial optimization problems relevant to finance (e.g., credit risk analysis, fraud detection)
## Key ideas
- #idea:hybrid-approach — Warm-starting QAOA with solutions from semidefinite programming (SDP) relaxations of Max-Cut problems improves approximation ratios and optimal sampling probabilities for portfolio optimization.
- #idea:hybrid-approach — Mapping QUBO problems to Max-Cut instances enables leveraging classical relaxation techniques (e.g., GW2 warm-start) to enhance QAOA performance.
- #idea:near-term-feasibility — The study demonstrates the feasibility of warm-start QAOA for small-scale (16-variable) portfolio optimization problems using quantum simulators, though scalability remains untested.
- #limitation:simulation-only — All results are derived from classical simulations of QAOA, with no empirical validation on real quantum hardware.
- #limitation:qubit-count — Experiments are limited to 16-variable QUBOs (17 qubits for Max-Cut), insufficient for practical financial applications.
- #limitation:data-encoding — Performance is highly problem-dependent, with synthetic datasets limiting generalizability to real-world financial scenarios.
## Contradictions
<!-- Step 6 output — where this paper contradicts others -->

## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
