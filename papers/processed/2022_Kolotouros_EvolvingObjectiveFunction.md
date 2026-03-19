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
step1_date: '2026-03-18T23:24:09.247405'
step1_model: Mistral-Large-3
step2_date: '2026-03-18T23:24:12.101841'
step2_model: Mistral-Large-3
step3_date: '2026-03-18T23:25:14.413252'
step3_model: Mistral-Large-3
step4_date: '2026-03-18T23:25:23.169940'
step4_model: Mistral-Large-3
step5_date: '2026-03-18T23:25:32.725768'
step5_model: Mistral-Large-3
step6_date: '2026-03-18T23:26:18.565665'
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
This paper introduces an evolving objective function, called ascending-CVaR, to enhance variational quantum algorithms for optimization problems. The authors test this approach on three combinatorial optimization problems—MaxCut, number partitioning, and portfolio optimization—using both variational quantum eigensolvers and quantum approximate optimization algorithms. The study demonstrates that their method improves convergence speed and solution accuracy compared to existing techniques, particularly in challenging problem instances.
## Methodology
The paper presents an empirical study on improving variational quantum optimization by introducing an evolving objective function called ascending-CVaR. The research focuses on three combinatorial optimization problems: MaxCut, number partitioning, and portfolio optimization. The authors extend prior work on conditional value at risk (CVaR) objective functions by dynamically adjusting the CVaR parameter (α) during the optimization process, starting from a small tail fraction and gradually increasing it to the full expectation value. The methodology involves testing the proposed ascending-CVaR objective function using classical numerical simulations with up to 20 qubits. The variational quantum eigensolver (VQE) with a hardware-efficient ansatz and the quantum approximate optimization algorithm (QAOA) are employed to evaluate performance. The study compares the proposed method against standard objective functions and the constant CVaR approach, analyzing metrics such as overlap with the ideal solution, success rate, and convergence speed across multiple problem instances and sizes.

**Algorithms used:** VQE, QAOA

**Experimental setup:** The experiments were conducted using classical numerical simulations in an emulation environment, with problem sizes of up to 20 qubits. The variational quantum algorithms (VQE and QAOA) were implemented with a hardware-efficient ansatz. The simulations focused on evaluating the performance of the ascending-CVaR objective function compared to standard and constant CVaR approaches.

**Dataset:** The study used synthetic datasets for three combinatorial optimization problems: MaxCut (graph instances with varying weights), number partitioning (sets of positive integers), and portfolio optimization (assets with expected returns and covariances, budget constraints). Specific instances of these problems were generated for testing, including both easy and hard cases.
## Findings
- [supported] The ascending-CVaR objective function achieves up to ten times greater overlap with the ideal state in portfolio optimization and number partitioning problems compared to standard objective functions or constant CVaR.
- [supported] Ascending-CVaR achieves an 80% improvement in overlap with the ideal state for the MaxCut problem compared to standard objective functions.
- [supported] For hard instances of the number partitioning problem, standard objective functions fail to find the correct solution in almost all cases (0%), constant CVaR succeeds in 60% of cases, while ascending-CVaR finds the correct solution in 95% of cases.
- [supported] Ascending-CVaR performs better than standard objective functions or constant CVaR across all tested problems (MaxCut, number partitioning, and portfolio optimization) in terms of convergence speed and solution accuracy, as demonstrated in emulation environments with up to 20 qubits.
- [supported] The proposed method avoids suboptimal minima by dynamically adjusting the objective function during optimization, leveraging the fact that local minima differ for varying α values in CVaR.
- [speculative] The authors suggest that ascending-CVaR could be a promising approach for achieving useful quantum advantage in combinatorial optimization problems, though this is not empirically validated on real hardware.

**Results summary:** The paper introduces an evolving objective function, termed ascending-CVaR, for variational quantum algorithms applied to combinatorial optimization problems. Tested via classical numerical simulations on MaxCut, number partitioning, and portfolio optimization problems, the method demonstrates superior performance over standard objective functions and constant CVaR. Specifically, ascending-CVaR achieves significantly higher overlap with the ideal solution (up to ten times greater in some cases) and improves success rates, particularly in hard problem instances. The results are derived from emulation environments using up to 20 qubits, with no experiments conducted on real quantum hardware.

**Performance claims:**
- Up to ten times greater overlap with the ideal state in portfolio optimization and number partitioning problems
- 80% improvement in overlap for MaxCut problems
- 95% success rate in finding correct solutions for hard instances of number partitioning (vs. 60% for constant CVaR and 0% for standard objective functions)
- Faster convergence and higher accuracy across all tested problems (MaxCut, number partitioning, portfolio optimization)
## Quantum advantage claim
**Classification:** speculative

The paper claims potential for useful quantum advantage in combinatorial optimization but provides no empirical demonstration on real hardware. All results are derived from classical emulation environments, and the advantage remains theoretical.
## Limitations
- Experiments conducted in an emulation environment with up to 20 qubits, limiting scalability to real-world quantum hardware [inferred]
- Performance tested only on synthetic instances of MaxCut, number partitioning, and portfolio optimization, not real-world financial datasets [inferred]
- Hardware noise and decoherence effects not considered in simulations, which may degrade performance on actual NISQ devices
- Dependence on hyperparameter choices (e.g., ascending factor λ) for the ascending-CVaR method, which may require problem-specific tuning
- No comparison with state-of-the-art classical optimization solvers to benchmark quantum advantage [inferred]
- Reproducibility of results may be affected by the stochastic nature of variational quantum algorithms and classical optimizers
- Limited exploration of ansatz depth and structure, particularly for QAOA, which may impact solution quality for larger problem sizes [inferred]
- Assumption that the parameterized family of states can achieve a maximum overlap κ with the optimal solution, which may not hold for all problem instances
## Open questions
- How does the ascending-CVaR method perform on larger qubit counts (e.g., 50+ qubits) and more complex problem instances?
- What is the impact of hardware noise and error mitigation techniques on the performance of ascending-CVaR in real quantum devices?
- Can the method be generalized to constrained optimization problems beyond QUBO formulations?
- How does the choice of ascending function (linear vs. sigmoid) affect performance for different classes of optimization problems?
- What is the trade-off between the number of measurements (shots) required and the accuracy of the ascending-CVaR method?
- How does the method compare to other advanced variational quantum algorithms (e.g., warm-starting QAOA, reinforcement learning-assisted optimization)?
- What are the theoretical guarantees for convergence and avoidance of local minima in the ascending-CVaR approach?

**Future work:**
- Test the ascending-CVaR method on real quantum hardware to evaluate performance under noise and decoherence
- Extend the method to larger problem sizes and real-world financial datasets (e.g., portfolio optimization with actual market data)
- Compare the performance of ascending-CVaR with state-of-the-art classical optimization solvers to quantify quantum advantage
- Explore adaptive strategies for dynamically tuning the ascending factor λ during optimization
- Investigate the use of error mitigation techniques to improve performance on NISQ devices
- Apply the method to other combinatorial optimization problems beyond MaxCut, number partitioning, and portfolio optimization
- Develop hybrid quantum-classical approaches that combine ascending-CVaR with classical optimization heuristics
- Analyze the theoretical properties of ascending-CVaR, including convergence guarantees and landscape analysis
## Key ideas
- #idea:quantum-advantage — Ascending-CVaR objective function achieves up to ten times greater overlap with the ideal state in portfolio optimization compared to standard or constant CVaR approaches, suggesting potential quantum advantage in combinatorial optimization.
- #idea:near-term-feasibility — The method demonstrates improved convergence speed and solution accuracy in emulation environments (up to 20 qubits), indicating near-term applicability for NISQ-era devices.
- #idea:hybrid-approach — The evolving objective function (ascending-CVaR) dynamically adjusts during optimization, leveraging classical preprocessing to enhance quantum algorithm performance.
- #limitation:simulation-only — All results are derived from classical numerical simulations, with no empirical validation on real quantum hardware.
- #limitation:noise — Hardware noise and decoherence effects are not considered, which may degrade performance on actual NISQ devices.
## Contradictions
<!-- Step 6 output — where this paper contradicts others -->

## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
