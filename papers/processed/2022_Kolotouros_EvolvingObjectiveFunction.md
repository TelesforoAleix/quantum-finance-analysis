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
journal_or_venue: PHYSICAL REVIEW RESEARCH
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
step1_date: '2026-03-19T23:17:41.963604'
step1_model: Mistral-Large-3
step2_date: '2026-03-19T23:18:41.995002'
step2_model: Mistral-Large-3
step3_date: '2026-03-19T12:19:40.061562'
step3_model: Mistral-Large-3
step4_date: '2026-03-19T23:19:10.260604'
step4_model: Mistral-Large-3
step5_date: '2026-03-19T23:19:21.090692'
step5_model: Mistral-Large-3
step6_date: '2026-03-19T23:19:24.235919'
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
title: Evolving objective function for improved variational quantum optimization
topic_tags:
- portfolio-optimisation
- risk-modelling
year: 2022
zotero_key: ''
---

## Abstract summary
This paper introduces an evolving objective function, termed ascending-CVaR, for variational quantum algorithms aimed at solving combinatorial optimization problems. The authors build on prior work using conditional value at risk (CVaR) as an objective function and propose dynamically adjusting the CVaR parameter during optimization to avoid local minima and improve convergence. The method is tested on three optimization problems—MaxCut, number partitioning, and portfolio optimization—demonstrating enhanced performance in terms of solution accuracy and speed compared to fixed CVaR and standard expectation value approaches.
## Methodology
The paper presents an empirical study on improving variational quantum optimization algorithms by introducing an evolving objective function called ascending-CVaR. The research focuses on three combinatorial optimization problems: MaxCut, number partitioning, and portfolio optimization. The authors extend prior work on conditional value at risk (CVaR) objective functions by dynamically adjusting the CVaR parameter (α) during the optimization process. This dynamic adjustment aims to avoid local minima and improve convergence speed and accuracy. The study employs variational quantum eigensolver (VQE) with a hardware-efficient ansatz and the quantum approximate optimization algorithm (QAOA). Experiments are conducted using classical numerical simulations (emulation environment) with up to 20 qubits. Performance is evaluated based on overlap with the optimal solution, success rate, and convergence speed, with comparisons made against standard objective functions and constant CVaR approaches.

**Algorithms used:** VQE, QAOA
**Frameworks:** Qiskit

**Experimental setup:** Experiments were conducted using IBM's Qiskit Aer simulator in a noiseless multishot execution environment. The number of circuit executions (shots) was set to K = 1000, scaling up as K/α with the choice of α. The COBYLA optimizer was used for all instances. The study tested problem sizes ranging from 15 to 20 qubits for different combinatorial optimization problems. The ascending-CVaR method was implemented with both linear and sigmoid ascending functions, with ascending factors λ tuned for each problem type.

**Dataset:** The study used synthetic datasets for three combinatorial optimization problems: (1) MaxCut on random non-regular unweighted graphs with 15-19 vertices, generated using the NetworkX library; (2) Number partitioning with 17-20 integers randomly sampled from sets N1 = {0,..., 200}, N2 = {0,..., 500}, and N3 = {0,..., 750}; (3) Portfolio optimization with up to 18 assets, involving expected returns and covariances for simulated financial data.
## Findings
- [supported] The ascending-CVaR objective function outperforms standard objective functions, constant CVaR, and expectation value methods in variational quantum optimization across MaxCut, number partitioning, and portfolio optimization problems.
- [supported] Ascending-CVaR achieves up to ten times greater overlap with the ideal state in portfolio optimization and number partitioning, and an 80% improvement in MaxCut compared to constant CVaR.
- [supported] For hard instances of the number partitioning problem, standard objective functions fail to find the correct solution in almost all cases (0-16% success), constant CVaR succeeds in 60% of cases, while ascending-CVaR succeeds in 95% of cases.
- [supported] Ascending-CVaR avoids suboptimal local minima by dynamically adjusting the objective function during optimization, as demonstrated in simulations with up to 20 qubits.
- [supported] The method is tested in an emulation environment (simulation) and shows consistent improvements across multiple problem sizes and instances.
- [speculative] The authors suggest that ascending-CVaR could be a heuristic for avoiding suboptimal minima in variational quantum algorithms, but this is not empirically validated beyond the tested instances.
- [speculative] The paper implies potential for quantum advantage in financial optimization problems like portfolio optimization, but this remains unproven on real hardware.

**Results summary:** The paper introduces an evolving objective function, ascending-CVaR, for variational quantum algorithms and demonstrates its superiority over fixed CVaR and standard expectation value methods through classical simulations. The method achieves significantly higher overlap with optimal solutions and faster convergence across three combinatorial optimization problems: MaxCut, number partitioning, and portfolio optimization. Notably, ascending-CVaR succeeds in 95% of hard number partitioning instances where other methods fail. Results are derived from noiseless simulations with up to 20 qubits, using VQE with hardware-efficient ansatz and QAOA. The approach dynamically adjusts the objective function to avoid local minima, but all performance claims are based on simulation rather than real quantum hardware.

**Performance claims:**
- Up to 10x greater overlap with the ideal state in portfolio optimization and number partitioning
- 80% improvement in overlap for MaxCut compared to constant CVaR
- 95% success rate in hard number partitioning instances (vs. 60% for constant CVaR and 0-16% for standard methods)
- Faster convergence to 10% overlap threshold in all tested problems
- Higher success rates across 100 random non-regular MaxCut instances (96% vs. 53-84% for other methods)
## Quantum advantage claim
**Classification:** speculative

The paper demonstrates improved performance of ascending-CVaR in simulations, but does not claim or demonstrate quantum advantage on real hardware. All results are from classical emulation, and while the method shows promise for near-term quantum devices, any advantage over classical methods remains theoretical and unvalidated in practice.
## Limitations
- Experiments conducted only in emulation environments, not on real quantum hardware [inferred]
- Limited to small qubit counts (up to 20 qubits) due to classical simulation constraints
- Performance tested only on synthetic instances of MaxCut, number partitioning, and portfolio optimization problems, not real-world financial datasets [inferred]
- No noise mitigation techniques applied, which may affect results on real NISQ devices [inferred]
- Dependence on hyperparameter tuning (e.g., ascending factor λ) for optimal performance, which may vary across problem instances and sizes
- No comparison with state-of-the-art classical optimization solvers for the tested problems [inferred]
- Reproducibility limited by the use of random initial parameters and gradient-free optimization (COBYLA)
- Scalability to larger problem sizes (beyond 20 qubits) not demonstrated due to classical simulation limitations
- Hardware-efficient ansatz and QAOA depth limited to p=6, which may not be sufficient for harder instances
- Lack of theoretical guarantees for the performance of ascending-CVaR across all problem types [inferred]
## Open questions
- How does the ascending-CVaR method perform on real quantum hardware with noise and decoherence?
- What is the optimal choice of ascending function (linear, sigmoid, etc.) and ascending factor λ for different problem classes and sizes?
- Can the method be extended to constrained optimization problems beyond QUBO formulations?
- How does the performance scale with problem size beyond 20 qubits?
- What is the impact of different classical optimizers on the convergence and success rate of ascending-CVaR?
- Can the method be combined with other techniques (e.g., warm-starting, reinforcement learning) to further improve performance?
- What are the theoretical connections between ascending-CVaR and adiabatic quantum computing?
- How does the method perform on other combinatorial optimization problems not tested in this paper?
- What is the trade-off between the number of shots (K) and the performance of ascending-CVaR?

**Future work:**
- Test ascending-CVaR on real quantum hardware (e.g., IBM Eagle processor) to evaluate noise resilience
- Extend the method to larger problem sizes (beyond 20 qubits) using more efficient classical simulators or hybrid quantum-classical approaches
- Investigate the optimal choice of ascending function and ascending factor λ for different problem classes
- Combine ascending-CVaR with other optimization techniques (e.g., warm-starting, reinforcement learning) to improve convergence
- Apply the method to real-world financial datasets for portfolio optimization and other financial use cases
- Explore the use of ascending-CVaR for constrained optimization problems beyond QUBO formulations
- Develop theoretical frameworks to explain the performance improvements observed with ascending-CVaR
- Benchmark the method against state-of-the-art classical solvers for the tested problems
- Investigate the impact of different classical optimizers on the performance of ascending-CVaR
- Extend the analysis to other combinatorial optimization problems (e.g., traveling salesman problem, vehicle routing)
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
