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
- idea:hybrid-approach
- idea:near-term-feasibility
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
step1_date: '2026-03-20T00:10:04.268324'
step1_model: Mistral-Large-3
step2_date: '2026-03-20T00:10:08.958862'
step2_model: Mistral-Large-3
step3_date: '2026-03-20T00:10:21.762896'
step3_model: Mistral-Large-3
step4_date: '2026-03-20T00:10:51.114088'
step4_model: Mistral-Large-3
step5_date: '2026-03-20T00:10:59.467445'
step5_model: Mistral-Large-3
step6_date: '2026-03-20T00:11:01.937508'
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
- idea/hybrid-approach
- idea/near-term-feasibility
title: Solving General QUBOs with Warm-Start QAOA via a Reduction to Max-Cut
topic_tags:
- portfolio-optimisation
year: 2025
zotero_key: ''
---

## Abstract summary
This paper introduces a method to solve Quadratic Unconstrained Binary Optimization (QUBO) problems using the Quantum Approximate Optimization Algorithm (QAOA) by reducing them to Max-Cut problems. The authors leverage semidefinite programming (SDP) relaxations to warm-start QAOA, aiming to improve approximation ratios at lower circuit depths. The study empirically compares this approach with a direct QUBO relaxation method across various QUBO instances, including random QUBOs and specific problems like the traveling salesman problem and portfolio optimization. The findings highlight that the optimal warm-start strategy depends on the problem type and performance metric.
## Methodology
The paper presents an empirical study comparing two warm-start approaches for the Quantum Approximate Optimization Algorithm (QAOA) applied to Quadratic Unconstrained Binary Optimization (QUBO) problems. The first approach, QUBO-Relaxed, relaxes the QUBO constraints directly and uses the relaxed solution to initialize the QAOA. The second approach maps QUBO instances to Max-Cut problems and applies a semidefinite programming (SDP) relaxation-based warm-start, specifically using the Goemans-Williamson (GW) and Burer-Monteiro (BM) relaxations. The study evaluates these approaches on various QUBO instances, including randomly generated QUBOs, traveling salesman problems (TSP), portfolio optimization, and maximum independent set (MIS) problems. The experiments involve generating 1000 problem instances for each type, running QAOA at depths from 0 to 5, and comparing performance metrics such as approximation ratio and optimal sampling probability.

**Algorithms used:** QAOA

**Experimental setup:** The experiments were conducted using a custom QAOA simulator based on prior work. The QAOA parameters were optimized using the COBYLA optimizer. For each circuit, the optimization loop was run 10 times with different initial parameter settings. Simulations were performed for QUBO problems with up to 16 variables, corresponding to 17-vertex graphs for Max-Cut instances.

**Dataset:** The datasets include randomly generated QUBOs (both continuous and discrete), QUBOs derived from specific combinatorial optimization problems such as the traveling salesman problem (TSP), portfolio optimization, and maximum independent set (MIS) on Erdős–Rényi (GNP) and Newman–Watts–Strogatz (NWS) graphs.
## Findings
- [supported] The warm-start QAOA approach using a reduction to Max-Cut achieves higher approximation ratios and optimal sampling probabilities for specific QUBO problems (e.g., portfolio optimization) compared to the QUBO-relaxation approach, with results dependent on the problem type and warm-start method.
- [supported] The Goemans-Williamson (GW2) warm-start with a vertex-at-top rotation on the auxiliary qubit (last qubit) consistently outperforms other rotation choices (first qubit or no rotation) across most problem instances, including random QUBOs, portfolio optimization, and maximum independent set (MIS).
- [supported] For the traveling salesman problem (TSP), the GW2 warm-start with no rotation achieves the highest optimal sampling probability, while the QUBO-relaxation approach performs better in terms of approximation ratio.
- [supported] The QUBO-relaxation warm-start's performance improves with more random initializations (50 vs. 10), particularly for constrained optimization problems like TSP and MIS, but remains problem-dependent.
- [supported] The GW2 warm-start achieves approximation ratios above 0.9 for portfolio optimization and MIS problems at depth p=5, with optimal sampling probabilities within ±0.25 standard deviations of QUBO-relaxation results.
- [speculative] The auxiliary qubit introduced in the QUBO-to-Max-Cut mapping may inherently possess a different structural role, making it the optimal choice for vertex-at-top rotations.
- [speculative] Quantum advantage for QAOA in solving QUBO problems may emerge at larger problem sizes (beyond 16 variables), where the warm-start techniques could provide more pronounced benefits over classical methods.

**Results summary:** The paper empirically evaluates warm-start QAOA techniques for solving QUBO problems via a reduction to Max-Cut. The study compares the Goemans-Williamson (GW2) warm-start, Burer-Monteiro (BM2/BM3) warm-starts, and QUBO-relaxation warm-starts across six problem types: continuous and discrete random QUBOs, traveling salesman problem (TSP), portfolio optimization, and maximum independent set (MIS) on two graph ensembles. Results demonstrate that the GW2 warm-start with a vertex-at-top rotation on the auxiliary qubit generally outperforms other methods, particularly for portfolio optimization and MIS. The QUBO-relaxation approach shows improved performance with more initializations but remains problem-dependent. Performance metrics (approximation ratio and optimal sampling probability) vary significantly across problem types, with constrained problems like TSP posing greater challenges. All results are derived from simulations, not real quantum hardware.

**Performance claims:**
- GW2 warm-start with last-qubit rotation achieves approximation ratios >0.9 for portfolio optimization at depth p=5
- GW2 warm-start with last-qubit rotation achieves optimal sampling probabilities within 0.25 standard deviations of QUBO-relaxation (50 initializations) for MIS problems
- QUBO-relaxation with 50 initializations outperforms GW2 in approximation ratio for TSP by >0.25 standard deviations
- GW2 warm-start with no rotation achieves the highest optimal sampling probability for TSP (though still low in absolute terms)
- GW2 warm-start outperforms QUBO-relaxation in approximation ratio for random QUBOs by >0.25 standard deviations
- Portfolio optimization (a QUBO-relaxed problem) shows the highest approximation ratios (>0.95) across all warm-start methods
## Quantum advantage claim
**Classification:** speculative

The paper does not demonstrate quantum advantage on real hardware. All results are from simulations of up to 17 qubits (16-variable QUBOs). While the warm-start QAOA shows promise in improving approximation ratios and sampling probabilities, the claimed advantages are theoretical and problem-specific. No comparison to state-of-the-art classical solvers is provided to validate quantum advantage.
## Limitations
- Experiments limited to QUBOs with up to 16 variables (17 qubits for Max-Cut reduction) due to computational constraints
- Performance evaluation conducted only on synthetic or randomly generated problem instances (e.g., random QUBOs, synthetic portfolio data, simulated TSP instances)
- [inferred] No comparison with state-of-the-art classical optimization solvers (e.g., Gurobi, CPLEX) to benchmark quantum advantage
- [inferred] Limited exploration of noise mitigation techniques, which may affect performance on real quantum hardware
- [inferred] No assessment of the impact of hardware noise or decoherence on the proposed warm-start QAOA approaches
- QUBO-Relaxed warm-start performance is highly dependent on the number of random initializations, lacking guarantees for general QUBOs
- Vertex-at-top rotation heuristic introduces an O(n) overhead, which may not scale efficiently for larger problem sizes
- Empirical results show strong problem-dependent performance, limiting generalizability of findings
- [inferred] No analysis of how the proposed methods perform under varying qubit connectivity constraints (e.g., NISQ-era hardware limitations)
- Portfolio optimization results may not generalize to real-world financial datasets with non-stationary or noisy asset returns
## Open questions
- How does the performance of warm-start QAOA scale with problem size beyond 16 variables?
- What is the impact of hardware noise and decoherence on the proposed warm-start approaches when executed on real quantum devices?
- Can the observed problem-dependent performance differences between warm-start methods be theoretically explained or predicted?
- How do the proposed warm-start QAOA methods compare to classical optimization solvers in terms of solution quality and runtime?
- What is the trade-off between the overhead of vertex-at-top rotations and the performance gains in practical applications?
- How does the auxiliary qubit introduced in the QUBO-to-Max-Cut mapping affect the algorithm's robustness to noise?
- Can the warm-start approaches be extended or adapted to handle constrained optimization problems more effectively?
- What are the implications of the skewed α-distributions for QAOA performance on constrained problems like TSP and MIS?
- How does the choice of hyperparameters (e.g., ε in QUBO-Relaxed, step size η in BM relaxations) affect the stability and performance of the warm-start methods?

**Future work:**
- Extend empirical evaluations to larger problem sizes (e.g., 30+ variables) to assess scalability
- Test the proposed warm-start QAOA methods on real quantum hardware to evaluate noise resilience and practical applicability
- Compare the performance of warm-start QAOA with state-of-the-art classical solvers for benchmark problems
- Explore hybrid quantum-classical approaches that combine warm-start QAOA with classical post-processing techniques
- Investigate adaptive warm-start strategies that dynamically select the best relaxation method based on problem characteristics
- Develop noise mitigation techniques tailored to warm-start QAOA to improve performance on NISQ devices
- Extend the QUBO-to-Max-Cut mapping to other combinatorial optimization problems beyond those tested in this work
- Analyze the theoretical underpinnings of the observed problem-dependent performance differences between warm-start methods
- Optimize the vertex-at-top rotation heuristic to reduce overhead while maintaining performance gains
- Apply the proposed methods to real-world financial datasets (e.g., portfolio optimization with market data) to validate practical utility
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

## Experiment details
### Input
{'random_qubos': {'source': 'Synthetically generated', 'size': '16 variables', 'number_of_features': 'Symmetric matrix Q ∈ R^16x16', 'preprocessing_steps': 'Matrix elements sampled from uniform distributions: continuous [-1, 1], discrete {-1, 1}'}, 'tsp': {'source': 'Synthetically generated points in [−1, 1]^2', 'size': '5 cities', 'number_of_features': 'Adjacency matrix A ∈ R^5x5 based on Euclidean distances', 'preprocessing_steps': 'Encoded as QUBO with constraints using Lagrange multiplier λ = 1.1 max(A_ij)'}, 'portfolio_optimization': {'source': 'Simulated using Geometric Brownian Motion', 'size': '16 assets, 250 time steps', 'number_of_features': 'Covariance matrix Σ ∈ R^16x16, mean return vector μ ∈ R^16', 'preprocessing_steps': 'Returns computed, budget constraint B = 8, risk parameter q = 0.5'}, 'mis': {'source': 'Synthetically generated graphs (GNP and NWS models)', 'size': '16 vertices', 'number_of_features': 'Adjacency matrix for unweighted graphs', 'preprocessing_steps': 'Encoded as QUBO with penalty term c = 1.1'}}

### Process
1. Generate QUBO instances for each problem type. 2. For each instance, apply warm-start approaches: QUBO-Relaxed (with 10 and 50 random initializations) and SDP-based (GW and BM relaxations with k=2,3). 3. Encode warm-start initial states into quantum circuits. 4. Run QAOA with depths p=0 to 5, optimizing parameters using COBYLA. 5. For each depth, evaluate approximation ratio (α) and optimal sampling probability (P). 6. Compare results across different warm-start approaches and vertex-at-top rotations.

### Output
{'metrics_reported': ['Approximation ratio (α)', 'Optimal sampling probability (P)'], 'comparison_baselines': ['QUBO-Relaxed with 10 and 50 initializations', 'Different vertex-at-top rotations (first, last, none) for SDP-based warm-starts'], 'output_format': 'Average values and standard deviations of α and P for each problem type and QAOA depth'}

### Parameters
- qubit_count: 17
- circuit_depth: Varied from 0 to 5
- shots: None
- optimizer: COBYLA
- learning_rate: None
- hyperparameters: {'ε': 0.1, 'η': 0.05, 'λ (TSP)': '1.1 * max(A_ij)', 'c (MIS)': 1.1, 'q (Portfolio Optimization)': 0.5, 'B (Portfolio Optimization)': 8}

### Hardware
Simulations were performed using a custom QAOA simulator without noise modeling.

### Reproducibility
Code for generating data and running simulations is available at a provided GitHub repository. Problem instances are synthetically generated, allowing for replication. Sufficient methodological detail is provided to replicate the experiments.
