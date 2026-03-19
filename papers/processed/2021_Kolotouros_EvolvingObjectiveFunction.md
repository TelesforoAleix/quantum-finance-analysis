---
aliases:
- An evolving objective function for improved variational quantum optimisation
- evolving objective function improved
authors:
- Ioannis Kolotouros
- Petros Wallden
auto_detected: true
classification: ''
contradiction_flags: []
doi: 10.48550/arXiv.2105.11766
evidence_type: ''
idea_tags:
- idea:quantum-advantage
- idea:near-term-feasibility
- idea:hybrid-approach
journal_or_venue: arXiv
methodology_tags:
- VQE
- QAOA
- QUBO
- variational
paper_type: ''
quantum_advantage_claim: speculative
related_papers:
- 2019_Barkoutsos_CVaR
relevance_phase1: high
relevance_phase3: high
source_type: peer-reviewed-empirical
source_type_confidence: high
step1_date: '2026-03-19T12:03:00.699087'
step1_model: Mistral-Large-3
step2_date: '2026-03-19T12:03:56.265330'
step2_model: Mistral-Large-3
step3_date: '2026-03-19T12:04:08.339207'
step3_model: Mistral-Large-3
step4_date: '2026-03-19T12:05:19.802408'
step4_model: Mistral-Large-3
step5_date: '2026-03-19T12:05:38.864948'
step5_model: Mistral-Large-3
step6_date: '2026-03-19T12:05:46.893528'
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
- topic/risk-modelling
- method/VQE
- method/QAOA
- method/QUBO
- method/variational
- idea/quantum-advantage
- idea/near-term-feasibility
- idea/hybrid-approach
title: An evolving objective function for improved variational quantum optimisation
topic_tags:
- portfolio-optimisation
- risk-modelling
year: 2022
zotero_key: ''
---

## Abstract summary
This paper introduces Ascending-CVaR, a dynamic objective function for variational quantum algorithms aimed at solving combinatorial optimization problems. Building on prior work that used Conditional Value-at-Risk (CVaR) as a fixed objective function, the authors propose a method where the CVaR parameter evolves during optimization. The approach is tested on Max-Cut, Number Partitioning, and Portfolio Optimization problems, demonstrating improved convergence speed and higher overlap with optimal solutions compared to static CVaR or standard expectation value methods.
## Methodology
The paper presents an empirical study on an evolving objective function called Ascending-CVaR for variational quantum optimization algorithms, specifically Variational Quantum Eigensolver (VQE) and Quantum Approximate Optimization Algorithm (QAOA). The research evaluates the performance of Ascending-CVaR against standard objective functions and the fixed Conditional Value-at-Risk (CVaR) approach introduced by Barkoutsos et al. The methodology involves mapping combinatorial optimization problems (Max-Cut, Number Partitioning, and Portfolio Optimization) to Quadratic Unconstrained Binary Optimization (QUBO) problems, which are then translated into Ising Hamiltonians. The study employs hardware-efficient ansatz for VQE and tests QAOA with varying depths. The Ascending-CVaR objective function dynamically adjusts the CVaR parameter α during the optimization process, starting from a small value and gradually increasing to 1. The experiments are conducted using classical numerical simulations with up to 20 qubits, and performance is evaluated based on overlap with the optimal solution, success rate, and convergence speed. The COBYLA optimizer is used for classical optimization, and the evaluation metrics include the probability of sampling the optimal solution and the time taken to reach a fixed overlap threshold.

**Algorithms used:** VQE, QAOA
**Frameworks:** Qiskit

**Experimental setup:** Experiments were conducted using IBM's Qiskit Aer simulator in a noiseless multi-shot execution environment. The number of circuit executions (shots) was set to K = 1000, scaling up as K/α with the choice of α. The maximum number of optimizer iterations was set to 66 times the number of parameters in the ansatz. The hardware-efficient ansatz for VQE and QAOA with depths from p = 1 to p = 6 were tested. The COBYLA optimizer was used for all instances.

**Dataset:** The study used synthetic datasets for three combinatorial optimization problems: (1) Max-Cut on unweighted graphs with 15-19 vertices, sampled using the NetworkX library; (2) Number Partitioning with 17-20 integers drawn from sets N1 = {0, ..., 200}, N2 = {0, ..., 500}, and N3 = {0, ..., 750}; (3) Portfolio Optimization with 16-20 assets, a budget drawn uniformly from {0, ..., n} where n is the number of assets, and various risk factors q.
## Findings
- [supported] Ascending-CVaR achieves up to ten times greater overlap with the ideal state compared to standard objective functions and constant CVaR in Portfolio Optimization and Number Partitioning problems, and an 80% improvement in Max-Cut problems, based on simulation results with up to 20 qubits
- [supported] Ascending-CVaR finds the correct solution in 95% of hard instances for the Number Partitioning problem, compared to 60% for constant CVaR and near-total failure for standard objective functions
- [supported] Ascending-CVaR outperforms constant CVaR and standard expectation value methods in success rate and overlap with optimal solutions across Max-Cut, Number Partitioning, and Portfolio Optimization problems, with results derived from classical numerical simulations
- [supported] The linear and sigmoid Ascending-CVaR functions perform better than exponential and logarithmic variants, with linear ascending generally faster and sigmoid potentially better for harder instances (~50 qubits)
- [speculative] Ascending-CVaR may offer greater advantage for harder problem instances where other methods frequently fail, based on observed performance in Number Partitioning and Max-Cut problems
- [speculative] The method's performance improvement is attributed to dynamically changing the energy landscape during optimization, which helps avoid local minima that trap constant CVaR approaches

**Results summary:** The paper introduces Ascending-CVaR, an evolving objective function for variational quantum optimization algorithms, and demonstrates its superior performance through classical numerical simulations on three combinatorial optimization problems: Max-Cut, Number Partitioning, and Portfolio Optimization. Using VQE with hardware-efficient ansatz and QAOA, the authors show that Ascending-CVaR consistently achieves higher overlap with optimal solutions (up to 10x improvement) and higher success rates (up to 95% in hard instances) compared to constant CVaR and standard expectation value methods. The method's advantage is particularly pronounced in harder problem instances where other approaches frequently fail. Performance metrics include overlap with optimal solutions, success rates (defined as achieving ≥10% overlap), and normalized optimization iterations. All results are derived from noiseless simulations using IBM's Qiskit Aer simulator with up to 20 qubits.

**Performance claims:**
- Up to ten times greater overlap with the ideal state in Portfolio Optimization and Number Partitioning problems
- 80% improvement in overlap for Max-Cut problems
- 95% success rate in finding correct solutions for hard Number Partitioning instances (vs 60% for constant CVaR)
- Higher success rates across all three problem types: 96% for Max-Cut (vs 53-84% for other methods), 80-87% for Number Partitioning (vs 0-69%), and 96% for Portfolio Optimization (vs 60-85%)
- Faster convergence to ≥10% overlap threshold in successful instances
## Quantum advantage claim
**Classification:** speculative

While the paper demonstrates significant performance improvements over classical variational approaches, all results are from classical numerical simulations rather than real quantum hardware. The claimed advantage is based on algorithmic improvements in simulation, with no empirical demonstration of quantum speedup or advantage on actual NISQ devices. The authors speculate that the method could contribute to achieving 'useful' quantum advantage but provide no hardware validation.
## Limitations
- Experiments conducted only in emulation environments, not on real quantum hardware [inferred]
- Limited to 20 qubits due to classical simulation constraints, restricting scalability analysis [inferred]
- Performance tested only on synthetic datasets (e.g., synthetic portfolio data, random graphs), not real-world financial data [inferred]
- Hardware noise and decoherence effects not considered in simulations [inferred]
- Dependence on hyperparameter tuning (e.g., ascending factor λ) for optimal performance, which may vary across problem instances [inferred]
- Reproducibility may be affected by random initialization of parameters and stochastic optimization processes
- QAOA performance limited by shallow circuit depths (p ≤ 6), which may not capture full potential of the algorithm
- No comparison with state-of-the-art classical optimization solvers for benchmarking [inferred]
- Assumption that the optimal solution is a computational basis state, which may not hold for all optimization problems [inferred]
- Limited exploration of noise mitigation techniques, which are critical for NISQ-era devices [inferred]
## Open questions
- How does Ascending-CVaR perform on real quantum hardware with noise and decoherence?
- What is the scalability of Ascending-CVaR for problem sizes beyond 20 qubits?
- How does the choice of ascending function (linear vs. sigmoid) impact performance for different problem classes?
- Can Ascending-CVaR be combined with other optimization techniques (e.g., warm-starting, reinforcement learning) for further improvement?
- What is the theoretical connection between Ascending-CVaR and adiabatic quantum computing?
- How does the performance of Ascending-CVaR compare to classical solvers for large-scale financial optimization problems?
- What are the optimal hyperparameters (e.g., ascending factor λ) for different problem sizes and types?
- How does Ascending-CVaR perform on constrained optimization problems beyond the tested combinatorial problems?
- What is the impact of shot noise and measurement errors on the performance of Ascending-CVaR?

**Future work:**
- Test Ascending-CVaR on real quantum hardware (e.g., IBM Eagle processor) to evaluate noise resilience
- Extend the analysis to larger problem sizes (e.g., 50+ qubits) to assess scalability
- Evaluate performance on real-world financial datasets (e.g., historical market data for portfolio optimization)
- Explore hybrid quantum-classical approaches combining Ascending-CVaR with classical optimization techniques
- Investigate theoretical connections between Ascending-CVaR and adiabatic quantum computing
- Benchmark Ascending-CVaR against state-of-the-art classical solvers for financial optimization problems
- Develop adaptive strategies for selecting the ascending factor λ based on problem characteristics
- Apply Ascending-CVaR to other optimization problems (e.g., logistics, supply chain, machine learning)
- Integrate noise mitigation techniques (e.g., error mitigation, dynamical decoupling) to improve performance on NISQ devices
- Explore the use of Ascending-CVaR in multi-period or dynamic optimization problems (e.g., dynamic portfolio optimization)
## Key ideas
- #idea:quantum-advantage — Ascending-CVaR achieves up to ten times greater overlap with optimal solutions in portfolio optimization compared to static CVaR or standard expectation value methods, as demonstrated in noiseless simulations
- #idea:near-term-feasibility — The paper positions Ascending-CVaR as a NISQ-era improvement for variational quantum algorithms, enhancing convergence and success rates in combinatorial optimization problems
- #idea:hybrid-approach — Hybrid quantum-classical frameworks (VQE and QAOA) are leveraged with classical optimization (COBYLA) to implement Ascending-CVaR, showing practical applicability for near-term devices
- #limitation:simulation-only — All results are derived from classical simulations (Qiskit Aer) with no validation on real quantum hardware, limiting claims of quantum advantage
- #limitation:noise — Noise and decoherence effects are not considered, which may degrade performance on NISQ devices despite simulation-based improvements
- #limitation:qubit-count — Experiments are limited to 20 qubits, insufficient for addressing real-world financial problems requiring larger-scale optimization
## Contradictions
<!-- Step 6 output — where this paper contradicts others -->

## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
