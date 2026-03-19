---
aliases:
- Evolving objective function for improved variational quantum optimization
- Evolving objective function improved
authors:
- Ioannis Kolotouros
- Petros Wallden
auto_detected: true
classification: ''
contradiction_flags: []
doi: 10.1103/PhysRevResearch.4.023225
evidence_type: ''
idea_tags:
- idea:quantum-advantage
- idea:near-term-feasibility
- idea:hybrid-approach
journal_or_venue: Physical Review Research
methodology_tags:
- VQE
- QAOA
- variational
- classical-simulation
paper_type: ''
quantum_advantage_claim: speculative
related_papers: []
relevance_phase1: high
relevance_phase3: high
source_type: peer-reviewed-empirical
source_type_confidence: high
step1_date: '2026-03-19T12:19:22.001371'
step1_model: Mistral-Large-3
step2_date: '2026-03-19T12:19:27.394579'
step2_model: Mistral-Large-3
step3_date: '2026-03-19T12:19:40.061562'
step3_model: Mistral-Large-3
step4_date: '2026-03-19T12:20:36.437592'
step4_model: Mistral-Large-3
step5_date: '2026-03-19T12:21:04.658591'
step5_model: Mistral-Large-3
step6_date: '2026-03-19T12:21:43.851725'
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
- method/classical-simulation
- idea/quantum-advantage
- idea/near-term-feasibility
- idea/hybrid-approach
title: Evolving objective function for improved variational quantum optimization
topic_tags:
- portfolio-optimisation
- risk-modelling
year: 2022
zotero_key: ''
---

## Abstract summary
This paper introduces an evolving objective function, termed ascending-CVaR, for variational quantum algorithms aimed at solving combinatorial optimization problems. The authors build on prior work using conditional value at risk (CVaR) as an objective function and propose dynamically adjusting the risk parameter during optimization to avoid local minima and improve convergence. The method is tested on MaxCut, number partitioning, and portfolio optimization problems, demonstrating significant improvements in both the speed of convergence and the quality of solutions compared to fixed CVaR or standard expectation value approaches.
## Methodology
The paper presents an empirical study on improving variational quantum optimization algorithms by introducing an evolving objective function called ascending-CVaR. The research focuses on three combinatorial optimization problems: MaxCut, number partitioning, and portfolio optimization. The authors extend prior work on conditional value at risk (CVaR) objective functions by dynamically adjusting the CVaR parameter (α) during the optimization process. This dynamic adjustment aims to avoid local minima and improve convergence speed and accuracy. The study employs variational quantum eigensolver (VQE) with a hardware-efficient ansatz and the quantum approximate optimization algorithm (QAOA). Experiments are conducted using classical numerical simulations (emulation environment) with up to 20 qubits. Performance is evaluated based on overlap with the optimal solution, success rate, and convergence speed, with comparisons made against standard objective functions and constant CVaR approaches.

**Algorithms used:** VQE, QAOA
**Frameworks:** Qiskit

**Experimental setup:** Experiments were conducted using IBM's Qiskit Aer simulator in a noiseless multishot execution environment. The number of circuit executions (shots) was set to K = 1000, scaling up as K/α with the choice of α. The COBYLA optimizer was used for all instances. The study tested problem sizes ranging from 15 to 20 qubits for different combinatorial optimization problems. The ascending-CVaR method was implemented with both linear and sigmoid ascending functions, with ascending factors λ tuned for each problem type.

**Dataset:** The study used synthetic datasets for three combinatorial optimization problems: (1) MaxCut on random non-regular unweighted graphs with 15-19 vertices, generated using the NetworkX library; (2) Number partitioning with 17-20 integers randomly sampled from sets N1 = {0,..., 200}, N2 = {0,..., 500}, and N3 = {0,..., 750}; (3) Portfolio optimization with up to 18 assets, involving expected returns and covariances for simulated financial data.
## Findings
- [supported] The ascending-CVaR objective function outperforms standard objective functions, constant CVaR, and expectation value methods in variational quantum optimization across MaxCut, number partitioning, and portfolio optimization problems.
- [supported] Ascending-CVaR achieves up to ten times greater overlap with the ideal state in portfolio optimization and number partitioning, and an 80% improvement in MaxCut compared to prior methods.
- [supported] For hard instances of the number partitioning problem, standard objective functions fail to find the correct solution in almost all cases, CVaR finds it in 60% of cases, while ascending-CVaR succeeds in 95% of cases.
- [supported] Ascending-CVaR avoids suboptimal minima by dynamically adjusting the objective function during optimization, as demonstrated in simulations with up to 20 qubits.
- [supported] Results are derived from classical numerical simulations (emulation environment) using VQE with hardware-efficient ansatz and QAOA, not real quantum hardware.
- [speculative] The authors suggest that ascending-CVaR could be a heuristic for avoiding suboptimal minima in variational quantum algorithms, but this claim is not empirically validated beyond the tested problem instances.
- [speculative] The paper implies potential scalability to larger problem sizes, but no empirical evidence is provided for instances beyond 20 qubits.

**Results summary:** The paper introduces an evolving objective function, ascending-CVaR, for variational quantum optimization and demonstrates its superiority over fixed CVaR and standard expectation value methods through classical simulations. The method achieves significantly higher overlap with optimal solutions across MaxCut, number partitioning, and portfolio optimization problems, particularly in hard instances where prior methods fail. Performance improvements are quantified, with up to tenfold increases in overlap and 95% success rates in challenging scenarios. However, all results are derived from simulations, and no real quantum hardware experiments are reported.

**Performance claims:**
- Up to ten times greater overlap with the ideal state in portfolio optimization and number partitioning
- 80% improvement in overlap for MaxCut problems
- 95% success rate in finding correct solutions for hard number partitioning instances (vs. 60% for CVaR and near 0% for standard methods)
- Faster convergence to 10% overlap threshold compared to fixed CVaR and expectation value methods
## Quantum advantage claim
**Classification:** speculative

The paper claims improved performance and convergence for variational quantum algorithms using ascending-CVaR, but all results are from classical simulations. No quantum advantage is demonstrated on real hardware, and the scalability to larger, practical problem sizes remains untested.
## Limitations
- Experiments conducted only in emulation environments, not on real quantum hardware [inferred]
- Limited to 20 qubits due to classical simulation constraints
- Performance tested only on synthetic datasets (e.g., synthetic portfolio data, random graphs) rather than real-world financial data [inferred]
- Hardware noise and decoherence effects not considered in simulations [inferred]
- Scalability to larger qubit counts (beyond 20 qubits) not demonstrated
- Reproducibility may be affected by random initialization of parameters and optimizer stochasticity
- Dependence on hyperparameter tuning (e.g., ascending factor λ) for optimal performance
- No comparison with state-of-the-art classical optimization solvers for the tested problems [inferred]
- Limited depth of QAOA (p ≤ 6) may not fully capture the potential of the algorithm
- Internal validity concerns due to reliance on specific ansatz families (hardware-efficient ansatz for VQE, QAOA with limited depth)
## Open questions
- How does the ascending-CVaR method perform on real quantum hardware with noise and decoherence?
- What is the impact of larger qubit counts (e.g., 50+ qubits) on the scalability and performance of the method?
- Can the method be extended to other combinatorial optimization problems beyond MaxCut, number partitioning, and portfolio optimization?
- How does the choice of ascending function (linear vs. sigmoid) affect performance across different problem classes?
- What is the theoretical relationship between the ascending-CVaR method and adiabatic quantum computing?
- How does the method compare to classical optimization techniques in terms of solution quality and runtime?
- What are the optimal hyperparameters (e.g., ascending factor λ) for different problem sizes and types?
- Can the method be combined with noise mitigation techniques to improve performance on NISQ devices?
- How does the method perform on real-world financial datasets compared to synthetic data?

**Future work:**
- Test the ascending-CVaR method on real quantum hardware (e.g., IBM Eagle processor)
- Extend the analysis to larger qubit counts (e.g., 50+ qubits) to assess scalability
- Apply the method to additional combinatorial optimization problems relevant to financial services
- Investigate the theoretical connection between ascending-CVaR and adiabatic quantum computing
- Compare the performance of ascending-CVaR with state-of-the-art classical optimization solvers
- Develop adaptive strategies for selecting the ascending function and hyperparameters based on problem characteristics
- Combine the method with noise mitigation techniques to improve performance on NISQ devices
- Evaluate the method on real-world financial datasets (e.g., portfolio optimization with real asset data)
- Explore the use of machine learning to optimize the ascending-CVaR parameters dynamically
- Extend the method to multi-period portfolio optimization and other dynamic financial problems
## Key ideas
- #idea:quantum-advantage — Ascending-CVaR objective function achieves up to ten times greater overlap with the ideal state in portfolio optimization compared to standard or constant CVaR approaches, suggesting potential quantum advantage in combinatorial optimization.
- #idea:near-term-feasibility — The method demonstrates improved convergence speed and solution accuracy in emulation environments (up to 20 qubits), indicating near-term applicability for NISQ-era devices.
- #idea:hybrid-approach — The evolving objective function (ascending-CVaR) dynamically adjusts during optimization, leveraging classical preprocessing to enhance quantum algorithm performance.
- #limitation:simulation-only — All results are derived from classical numerical simulations, with no empirical validation on real quantum hardware.
- #limitation:noise — Hardware noise and decoherence effects are not considered, which may degrade performance on actual NISQ devices.
- #limitation:qubit-count — Limited to 20 qubits due to classical simulation constraints, insufficient for practical financial problems.
- #limitation:data-encoding — Performance tested only on synthetic datasets, not real-world financial data.
## Contradictions
<!-- Step 6 output — where this paper contradicts others -->

## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
