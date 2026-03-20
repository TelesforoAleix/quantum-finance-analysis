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
- variational
- QUBO
- classical-simulation
paper_type: ''
quantum_advantage_claim: speculative
related_papers: []
relevance_phase1: high
relevance_phase3: high
source_type: peer-reviewed-empirical
source_type_confidence: high
step1_date: '2026-03-19T23:05:59.871913'
step1_model: Mistral-Large-3
step2_date: '2026-03-19T23:06:03.184232'
step2_model: Mistral-Large-3
step3_date: '2026-03-19T23:06:51.952973'
step3_model: Mistral-Large-3
step4_date: '2026-03-19T23:08:00.072432'
step4_model: Mistral-Large-3
step5_date: '2026-03-19T23:08:10.219868'
step5_model: Mistral-Large-3
step6_date: '2026-03-19T23:08:57.708404'
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
- method/variational
- method/QUBO
- method/classical-simulation
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
This paper introduces Ascending-CVaR, an evolving objective function for variational quantum algorithms aimed at solving combinatorial optimization problems. The authors extend prior work on Conditional Value-at-Risk (CVaR) objective functions by dynamically adjusting the risk parameter during optimization. The method is tested on Max-Cut, Number Partitioning, and Portfolio Optimization problems, demonstrating improved convergence speed and higher overlap with optimal solutions compared to fixed CVaR or standard expectation value approaches.
## Methodology
The paper introduces an evolving objective function called Ascending-CVaR for variational quantum optimization algorithms, extending prior work on Conditional Value-at-Risk (CVaR) objective functions. The study empirically evaluates this method using three combinatorial optimization problems: Max-Cut, Number Partitioning, and Portfolio Optimization. The research employs the Variational Quantum Eigensolver (VQE) with a hardware-efficient ansatz and the Quantum Approximate Optimization Algorithm (QAOA). The authors test multiple instances of varying sizes in an emulation environment, comparing Ascending-CVaR against standard objective functions and constant CVaR. The methodology involves initializing the objective function with a small CVaR value and gradually increasing it during the optimization process to avoid local minima and improve convergence to near-optimal solutions.

**Algorithms used:** VQE, QAOA
**Frameworks:** Qiskit

**Experimental setup:** Experiments were conducted using IBM's Qiskit Aer simulator in a noiseless environment. The study tested instances with up to 20 qubits for problems like Max-Cut, Number Partitioning, and Portfolio Optimization. The experimental setup included a maximum of 66 times the number of parameters as optimization iterations, with random initialization of parameters consistent across different objective functions.

**Dataset:** The datasets used include random non-regular unweighted graphs for Max-Cut, sets of positive integers for Number Partitioning, and random portfolios with varying assets for Portfolio Optimization. Specific sets for Number Partitioning were N1 = {0, ..., 200}, N2 = {0, ..., 500}, and N3 = {0, ..., 750}.
## Findings
- [supported] The Ascending-CVaR objective function outperforms standard objective functions and the 'constant' CVaR approach across Max-Cut, Number Partitioning, and Portfolio Optimization problems, achieving up to ten times greater overlap with the ideal state in Portfolio Optimization and Number Partitioning, and an 80% improvement in Max-Cut.
- [supported] Ascending-CVaR achieves higher success rates in finding the correct solution: 95% success rate for hard instances of the Number Partitioning problem, compared to 60% for CVaR and near-total failure for standard objective functions.
- [supported] Ascending-CVaR demonstrates faster convergence, particularly in hard instances, by dynamically adjusting the CVaR parameter (α) during optimization, avoiding sub-optimal minima that trap constant CVaR methods.
- [supported] Results are derived from classical numerical simulations (emulation environment) using up to 20 qubits, with no claims of performance on real quantum hardware.
- [speculative] The authors suggest that Ascending-CVaR could be particularly advantageous for larger problem sizes (e.g., ~50 qubits) where harder instances benefit from sigmoid-based ascending functions.
- [speculative] The method’s performance improvements are argued to be generic across combinatorial optimization problems, potentially bringing 'useful' quantum advantage closer for financial and other applications.

**Results summary:** The paper introduces Ascending-CVaR, an evolving objective function for variational quantum optimization that dynamically adjusts the CVaR parameter (α) during the optimization process. Tested on three combinatorial problems—Max-Cut, Number Partitioning, and Portfolio Optimization—using VQE and QAOA in a noiseless simulation environment, Ascending-CVaR consistently outperforms both standard expectation-value-based methods and fixed-α CVaR approaches. Key improvements include higher overlap with optimal solutions (up to 10x in some cases), faster convergence, and significantly better success rates in hard instances (e.g., 95% success for Ascending-CVaR vs. 60% for CVaR in Number Partitioning). The method’s advantage stems from its ability to avoid local minima by leveraging varying energy landscapes associated with different α values. While results are simulation-based, the authors posit that Ascending-CVaR could scale to larger problem sizes, particularly with sigmoid-based ascending functions for harder instances.

**Performance claims:**
- Up to ten times greater overlap with the ideal state in Portfolio Optimization and Number Partitioning problems
- 80% improvement in overlap for Max-Cut problems
- 95% success rate in finding correct solutions for hard Number Partitioning instances (vs. 60% for CVaR and near-total failure for standard methods)
- Faster convergence to 10% overlap threshold in all tested problems
- Higher probability of sampling optimal solutions (e.g., 70% overlap in some Max-Cut instances vs. near-zero for other methods)
## Quantum advantage claim
**Classification:** speculative

While the paper demonstrates empirical improvements in simulation, quantum advantage is not explicitly claimed. The results are derived from classical emulation (up to 20 qubits), and no evidence is provided for performance on real NISQ hardware. The authors speculate that the method could contribute to 'useful' quantum advantage for larger problem sizes, but this remains unvalidated.
## Limitations
- Experiments conducted in a noiseless emulation environment (IBM Qiskit Aer simulator), limiting applicability to real NISQ devices with hardware noise [inferred]
- Qubit count constrained to 20 qubits, restricting scalability to larger problem instances [inferred]
- Performance evaluated only on synthetic datasets (e.g., random graphs, synthetic portfolios), not real-world financial data [inferred]
- Dependence on hyperparameter tuning (e.g., ascending factor λ) for optimal performance, which may vary across problem instances and sizes [inferred]
- Limited depth of QAOA (p ≤ 6) and VQE (p = 1) due to noise and decoherence constraints, potentially underestimating performance at higher depths [inferred]
- No comparison with state-of-the-art classical optimizers (e.g., Goemans-Williamson for Max-Cut) to benchmark quantum advantage [inferred]
- Reproducibility challenges due to random initialization of parameters and reliance on gradient-free optimizers (COBYLA) [inferred]
- Assumption of maximum overlap κ with the optimal solution may not hold for all problem instances, particularly in hard regimes [inferred]
- Fixed number of shots (K = 1000) may not be sufficient for accurate estimation of objective functions in larger or harder instances [inferred]
- Lack of noise mitigation techniques, which could significantly impact results on real quantum hardware [inferred]
## Open questions
- How does the Ascending-CVaR method perform on real quantum hardware with noise and decoherence?
- What is the scalability of the method beyond 20 qubits, and how does it compare to classical solvers for larger problem instances?
- How sensitive is the method to the choice of ascending function (e.g., linear vs. sigmoid) and ascending factor λ across different problem domains?
- Can the method be extended to constrained optimization problems without relying on penalty terms (e.g., for portfolio optimization)?
- What is the impact of different classical optimizers (e.g., gradient-based vs. gradient-free) on the performance of Ascending-CVaR?
- How does the method perform on real-world financial datasets compared to synthetic data?
- Is there a theoretical connection between Ascending-CVaR and adiabatic quantum computing that could guide hyperparameter selection?
- What are the trade-offs between the number of shots, accuracy, and convergence speed in the Ascending-CVaR method?
- How does the method handle degeneracy in the ground state of problem Hamiltonians?
- Can the method be generalized to other variational quantum algorithms beyond VQE and QAOA?

**Future work:**
- Test Ascending-CVaR on real quantum hardware (e.g., IBM Eagle processor) to evaluate noise resilience
- Extend the method to larger problem instances (e.g., >50 qubits) and compare with classical solvers
- Investigate adaptive strategies for selecting the ascending function and ascending factor λ based on problem characteristics
- Apply noise mitigation techniques (e.g., error mitigation, dynamical decoupling) to improve performance on NISQ devices
- Explore hybrid quantum-classical approaches combining Ascending-CVaR with classical optimization heuristics
- Evaluate the method on real-world financial datasets (e.g., historical market data for portfolio optimization)
- Develop theoretical frameworks to connect Ascending-CVaR with adiabatic quantum computing or other quantum algorithms
- Optimize the number of shots and circuit repetitions to balance accuracy and computational cost
- Extend the method to multi-period or dynamic optimization problems (e.g., dynamic portfolio optimization)
- Investigate the use of Ascending-CVaR in other domains (e.g., logistics, machine learning) beyond combinatorial optimization
## Key ideas
- #idea:quantum-advantage — Ascending-CVaR achieves up to ten times greater overlap with optimal solutions in portfolio optimization compared to static CVaR or standard expectation value methods, as demonstrated in noiseless simulations
- #idea:near-term-feasibility — Ascending-CVaR is positioned as a NISQ-era improvement for variational quantum algorithms, enhancing convergence and success rates in combinatorial optimization problems like portfolio optimization and risk modelling
- #idea:hybrid-approach — Hybrid quantum-classical frameworks (VQE and QAOA) with classical optimization (COBYLA) are used to implement Ascending-CVaR, showing practical applicability for near-term devices
- #limitation:simulation-only — All results are derived from classical simulations (Qiskit Aer) with no validation on real quantum hardware, limiting claims of quantum advantage
- #limitation:noise — Noise and decoherence effects are not considered, which may degrade performance on NISQ devices despite simulation-based improvements
- #limitation:qubit-count — Experiments are limited to 20 qubits, insufficient for addressing real-world financial problems requiring larger-scale optimization
## Contradictions
<!-- Step 6 output — where this paper contradicts others -->

## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->

## Experiment details
### Input
{'Max-Cut': {'source': 'Random non-regular unweighted graphs generated using NetworkX library', 'size': '15-19 vertices', 'preprocessing': 'Mapping to Quadratic Unconstrained Binary Optimization (QUBO) and then to Ising Hamiltonian'}, 'Number Partitioning': {'source': 'Randomly sampled integers from sets N1, N2, and N3', 'size': '17-20 integers', 'preprocessing': 'Mapping to Ising Hamiltonian'}, 'Portfolio Optimization': {'source': 'Random portfolios with expected returns and covariances', 'size': '16-20 assets', 'preprocessing': 'Mapping to QUBO and then to Ising Hamiltonian with penalty terms for constraints'}}

### Process
1. Encode the optimization problem into a Hamiltonian. 2. Initialize parameters randomly for the variational quantum algorithm (VQE or QAOA). 3. Use COBYLA optimizer to minimize the Ascending-CVaR objective function. 4. Gradually increase the CVaR parameter α from a small initial value (e.g., 0.01) to 1, using either linear or sigmoid functions. 5. Repeat the optimization loop with 1000 shots per circuit evaluation until convergence or maximum iterations are reached.

### Output
Metrics reported include the overlap with the optimal solution, success rate (achieving at least 10% overlap with the optimal solution), and the time (normalized optimizer iterations) to reach the threshold overlap. Comparisons were made against constant CVaR with α = 0.1, 0.2, 0.5, 1, and the expectation value.

### Parameters
- qubits: Up to 20
- shots: 1000
- optimizer: COBYLA
- initial_alpha: 0.01
- ascending_functions: ['linear', 'sigmoid']
- ascending_factors: {'linear': [0.025, 0.045], 'sigmoid': [0.3, 0.4]}
- max_iterations: 66 times the number of parameters

### Hardware
IBM Qiskit Aer simulator, noiseless environment

### Reproducibility
Code for the experiments is available on GitHub. Data for graphs and portfolios are generated using standard libraries (e.g., NetworkX). Sufficient detail is provided to replicate the experiments.
