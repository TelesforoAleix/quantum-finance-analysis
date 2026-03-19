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
- idea:quantum-advantage
- idea:near-term-feasibility
- idea:hybrid-approach
journal_or_venue: ACM Transactions on Quantum Computing
methodology_tags:
- QAOA
- QUBO
- variational
- classical-simulation
paper_type: ''
quantum_advantage_claim: speculative
related_papers: []
relevance_phase1: high
relevance_phase3: medium
source_type: peer-reviewed-empirical
source_type_confidence: high
step1_date: '2026-03-19T13:10:27.304445'
step1_model: Mistral-Large-3
step2_date: '2026-03-19T13:11:21.843755'
step2_model: Mistral-Large-3
step3_date: '2026-03-19T13:11:31.394608'
step3_model: Mistral-Large-3
step4_date: '2026-03-19T13:11:50.790008'
step4_model: Mistral-Large-3
step5_date: '2026-03-19T13:12:36.567117'
step5_model: Mistral-Large-3
step6_date: '2026-03-19T13:12:42.142943'
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
- method/variational
- method/classical-simulation
- idea/quantum-advantage
- idea/near-term-feasibility
- idea/hybrid-approach
title: Solving General QUBOs with Warm-Start QAOA via a Reduction to Max-Cut
topic_tags:
- portfolio-optimisation
year: 2025
zotero_key: ''
---

## Abstract summary
This paper introduces a method to solve Quadratic Unconstrained Binary Optimization (QUBO) problems using the Quantum Approximate Optimization Algorithm (QAOA) by transforming QUBO instances into Max-Cut problems. The authors leverage semidefinite programming (SDP) relaxations to warm-start QAOA, aiming to improve approximation ratios at lower circuit depths. The study empirically compares this approach with a direct QUBO relaxation method across various QUBO instances, including random QUBOs and specific problems like the traveling salesman problem and portfolio optimization. The findings highlight that the effectiveness of warm-start techniques is highly dependent on the problem type.
## Methodology
The paper presents an empirical study comparing two warm-start approaches for the Quantum Approximate Optimization Algorithm (QAOA) applied to Quadratic Unconstrained Binary Optimization (QUBO) problems. The first approach involves a QUBO-relaxation that relaxes integer constraints to interval constraints and uses the relaxed solution to generate a warm-started quantum state. The second approach maps arbitrary QUBOs to Max-Cut instances and applies a semidefinite programming (SDP) relaxation-based warm-start, specifically leveraging the Goemans-Williamson (GW) and Burer-Monteiro (BM) relaxations. The study evaluates these methods on various QUBO instances, including randomly generated QUBOs, traveling salesman problems, portfolio optimization, and maximum independent set problems. The experimental setup involves generating 1000 problem instances for each QUBO type, running QAOA at different depths (p=0 to p=5), and comparing performance using approximation ratio and optimal sampling probability metrics. The warm-start initial states are constructed using solutions from classical relaxations and encoded into quantum states via Bloch sphere representations.

**Algorithms used:** QAOA

**Experimental setup:** The experiments were conducted using quantum simulators. The QUBO problems were mapped to equivalent Max-Cut instances, and warm-start initial states were generated using SDP relaxations (GW and BM) and QUBO-relaxation techniques. The QAOA circuit parameters were optimized classically for each problem instance. The study tested QUBO instances with up to 16 variables, corresponding to 17-vertex Max-Cut graphs. Different vertex-at-top rotation heuristics were applied to assess their impact on performance.

**Dataset:** The datasets included: (1) Randomly generated QUBOs with matrix elements sampled uniformly from [-1, 1] or discretely from {-1, 1}; (2) Traveling Salesman Problem (TSP) instances with 5 cities randomly placed in [-1, 1]^2; (3) Portfolio optimization problems with 16 assets, simulated using geometric Brownian motion for price data; (4) Maximum Independent Set (MIS) problems on Erdős–Rényi (GNP) and Newman–Watts–Strogatz (NWS) random graphs with 16 vertices.
## Findings
- [supported] Warm-start QAOA using a reduction to Max-Cut achieves higher approximation ratios and optimal sampling probabilities for specific QUBO problems (e.g., portfolio optimization, maximum independent set) compared to QUBO-relaxation approaches, with performance strongly dependent on problem type and warm-start method.
- [supported] The Goemans-Williamson (GW) warm-start projected onto 2 dimensions (GW2) with a vertex-at-top rotation on the auxiliary qubit (last qubit) consistently outperforms other warm-start methods (GW3, BM2, BM3) in terms of approximation ratio and optimal sampling probability for most problem instances, including random QUBOs and portfolio optimization.
- [supported] For the Traveling Salesman Problem (TSP), the GW2 warm-start with no vertex-at-top rotation achieves the highest optimal sampling probability, while QUBO-relaxation methods yield better approximation ratios, indicating problem-specific trade-offs between warm-start techniques.
- [supported] The QUBO-relaxation warm-start's performance is highly sensitive to the number of random initializations, with 50 initializations generally outperforming 10 initializations, particularly for constrained optimization problems like TSP and maximum independent set (MIS).
- [supported] The auxiliary qubit introduced in the QUBO-to-Max-Cut mapping often serves as the optimal choice for the vertex-at-top rotation, reducing the overhead of testing multiple rotations from O(n) to O(1).
- [supported] At QAOA depth p=5, the GW2 warm-start with last-qubit rotation achieves average approximation ratios within ±0.25 standard deviations of QUBO-relaxation with 50 initializations for MIS problems, but outperforms QUBO-relaxation for portfolio optimization and random QUBOs.
- [supported] BM2 and BM3 warm-starts yield comparable approximation ratios to GW warm-starts but significantly lower optimal sampling probabilities, likely due to finding high-cost but suboptimal solutions.
- [speculative] The observed performance differences between warm-start methods may stem from structural properties of the QUBO problems, such as convexity (e.g., portfolio optimization) or constraint density (e.g., TSP), which influence the effectiveness of classical relaxations and quantum initial states.
- [speculative] Quantum advantage for warm-start QAOA in financial services (e.g., portfolio optimization) may emerge at larger problem sizes (e.g., 50+ qubits), where the reduction in circuit depth enabled by warm-starts could mitigate decoherence and gate errors on near-term hardware.

**Results summary:** The paper empirically evaluates warm-start QAOA methods for solving QUBO problems via a reduction to Max-Cut, comparing Goemans-Williamson (GW), Burer-Monteiro (BM), and QUBO-relaxation warm-starts across six problem types (random QUBOs, TSP, portfolio optimization, MIS). Results from simulations (up to 16 qubits) show that GW2 warm-starts with vertex-at-top rotations on the auxiliary qubit consistently achieve the highest approximation ratios and optimal sampling probabilities for most problems, though performance is problem-dependent. QUBO-relaxation methods perform well for constrained problems (e.g., TSP) but require more initializations. The study highlights the importance of problem-specific warm-start selection and suggests that auxiliary qubits in QUBO-to-Max-Cut mappings can reduce computational overhead.

**Performance claims:**
- GW2 warm-start with last-qubit rotation achieves an average approximation ratio of ~0.95 for portfolio optimization at p=5, outperforming QUBO-relaxation (~0.90).
- GW2 warm-start with last-qubit rotation achieves an optimal sampling probability of ~0.5 for portfolio optimization at p=5, within 0.25 standard deviations of QUBO-relaxation (~0.45).
- For random QUBOs, GW2 warm-start with last-qubit rotation achieves an approximation ratio of ~0.85 (continuous) and ~0.75 (discrete) at p=5, compared to QUBO-relaxation's ~0.75 and ~0.65, respectively.
- For TSP, GW2 warm-start with no rotation achieves an optimal sampling probability of ~0.015 at p=5, outperforming QUBO-relaxation (~0.010 with 10 initializations).
- For MIS-GNP, GW2 warm-start with last-qubit rotation achieves an approximation ratio of ~0.85 at p=5, comparable to QUBO-relaxation with 50 initializations (~0.87).
- BM2 and BM3 warm-starts achieve approximation ratios within 0.1 of GW2 but optimal sampling probabilities <0.1 for all problems at p=5.
## Quantum advantage claim
**Classification:** speculative

The paper does not demonstrate quantum advantage on real hardware; all results are from simulations. The claimed advantage (e.g., reduced circuit depth via warm-starts) is theoretical and problem-dependent, with no empirical validation of speedup or accuracy improvements over classical methods for large-scale problems. Quantum advantage remains speculative until demonstrated on real hardware with larger qubit counts.
## Limitations
- Experiments limited to QUBO instances with up to 16 variables (17 qubits after reduction to Max-Cut), restricting scalability to larger financial problems [inferred]
- Empirical evaluation conducted only on synthetic or randomly generated problem instances (e.g., random QUBOs, synthetic portfolio data), not real-world financial datasets
- Performance of warm-start approaches is highly problem-dependent, with no single method consistently outperforming others across all QUBO types
- QUBO-Relaxed warm-start relies on non-convex optimization for general QUBOs, lacking performance guarantees and requiring multiple random initializations
- No noise mitigation techniques applied, which may affect results on real quantum hardware [inferred]
- Circuit depth limited to p=5, which may not be sufficient to observe convergence behavior for all problem types
- Vertex-at-top heuristic introduces O(n) overhead for testing all possible rotations, though auxiliary qubit often reduces this in practice
- No comparison with state-of-the-art classical solvers (e.g., Gurobi, CPLEX) to benchmark quantum advantage [inferred]
- Portfolio optimization experiments assume geometric Brownian motion for asset prices, which may not capture real market dynamics [inferred]
- Lack of empirical validation on real quantum hardware; all results obtained via classical simulation
## Open questions
- How does the performance of warm-start QAOA scale with qubit counts beyond 17 qubits for financial applications?
- What is the impact of hardware noise and decoherence on the solution quality of warm-start QAOA for QUBO problems?
- Can the observed problem-dependent performance of warm-start approaches be predicted a priori based on QUBO structure?
- How does the QUBO-to-Max-Cut reduction affect the robustness of solutions under noise compared to direct QUBO approaches?
- What is the minimal circuit depth required for warm-start QAOA to outperform classical heuristics in financial optimization tasks?
- How do constrained optimization problems (e.g., TSP, MIS) behave under warm-start QAOA when mapped to QUBOs with large penalty terms?
- Can the auxiliary qubit in the QUBO-to-Max-Cut reduction be leveraged further to improve warm-start performance?
- What is the trade-off between the number of random initializations in QUBO-Relaxed warm-starts and solution quality for large-scale problems?

**Future work:**
- Test warm-start QAOA on real quantum hardware (e.g., IBM Eagle processor) to evaluate noise resilience and practical performance
- Extend empirical evaluation to larger QUBO instances (e.g., 50+ variables) to assess scalability
- Compare warm-start QAOA with state-of-the-art classical solvers for financial optimization problems
- Investigate hybrid quantum-classical approaches that combine warm-start QAOA with classical post-processing techniques
- Develop problem-specific warm-start strategies tailored to financial applications (e.g., portfolio optimization, risk analysis)
- Explore adaptive warm-start techniques that dynamically adjust initial states based on problem structure
- Apply noise mitigation techniques (e.g., error mitigation, dynamical decoupling) to improve performance on NISQ devices
- Study the impact of different penalty weights in constrained QUBO formulations (e.g., TSP, MIS) on warm-start QAOA performance
- Extend the QUBO-to-Max-Cut reduction to other combinatorial optimization problems relevant to finance (e.g., option pricing, credit risk modeling)
- Develop theoretical bounds on the approximation ratio of warm-start QAOA for specific QUBO classes
## Key ideas
- #idea:quantum-advantage — GW2 warm-start QAOA achieves higher approximation ratios (~0.95) for portfolio optimization at p=5 compared to QUBO-relaxation (~0.90), suggesting potential quantum advantage for specific problem types
- #idea:hybrid-approach — Warm-starting QAOA with classical SDP relaxations (e.g., Goemans-Williamson) improves performance for portfolio optimization and other QUBO problems
- #idea:hybrid-approach — Mapping QUBO to Max-Cut enables leveraging classical optimization techniques to enhance quantum algorithm performance
- #idea:near-term-feasibility — Demonstrates feasibility of warm-start QAOA for small-scale (16-variable) portfolio optimization on simulators, though scalability is untested
- #limitation:simulation-only — All results are from classical simulations, with no empirical validation on real quantum hardware
- #limitation:qubit-count — Experiments limited to 16-variable QUBOs (17 qubits), insufficient for practical financial applications
- #limitation:data-encoding — Performance is highly problem-dependent, with synthetic datasets limiting generalizability to real-world financial scenarios
## Contradictions
<!-- Step 6 output — where this paper contradicts others -->

## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
