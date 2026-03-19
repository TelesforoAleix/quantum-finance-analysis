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
- classical-simulation
paper_type: ''
quantum_advantage_claim: speculative
related_papers: []
relevance_phase1: high
relevance_phase3: high
source_type: preprint
source_type_confidence: high
step1_date: '2026-03-18T23:17:00.291038'
step1_model: Mistral-Large-3
step2_date: '2026-03-18T23:17:03.252486'
step2_model: Mistral-Large-3
step3_date: '2026-03-18T23:17:35.909386'
step3_model: Mistral-Large-3
step4_date: '2026-03-18T23:18:42.675403'
step4_model: Mistral-Large-3
step5_date: '2026-03-18T23:18:47.851016'
step5_model: Mistral-Large-3
step6_date: '2026-03-18T23:18:51.687396'
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
title: An evolving objective function for improved variational quantum optimisation
topic_tags:
- portfolio-optimisation
- risk-modelling
year: 2022
zotero_key: ''
---

## Abstract summary
This preprint introduces Ascending-CVaR, an evolving objective function for variational quantum algorithms designed to improve convergence and solution accuracy in optimization problems. The authors extend prior work on Conditional Value-at-Risk (CVaR) by dynamically adjusting the objective function during optimization, testing its performance on Max-Cut, Number Partitioning, and Portfolio Optimization problems. The approach aims to enhance the efficiency of hybrid quantum-classical algorithms in the NISQ era by avoiding sub-optimal minima and achieving higher overlap with ideal solutions.
## Methodology
The paper introduces an evolving objective function called Ascending-CVaR for variational quantum optimization algorithms, extending prior work on Conditional Value-at-Risk (CVaR) objective functions. The methodology involves testing the proposed Ascending-CVaR function on three combinatorial optimization problems: Max-Cut, Number Partitioning, and Portfolio Optimization. The research employs two variational quantum algorithms, the Variational Quantum Eigensolver (VQE) with a hardware-efficient ansatz and the Quantum Approximate Optimization Algorithm (QAOA). The study uses classical numerical simulations (emulation environment) with problem sizes up to 20 qubits. The performance of Ascending-CVaR is evaluated by comparing it to standard objective functions and the fixed CVaR approach, focusing on metrics such as overlap with the ideal solution, success rate in finding the correct solution, and convergence speed. The evolving objective function dynamically adjusts the parameter α during the optimization process, starting from a small value and gradually increasing it to improve convergence and accuracy.

**Algorithms used:** VQE, QAOA

**Experimental setup:** The experiments were conducted using classical numerical simulations (emulation environment) with up to 20 qubits. The study tested multiple instances of different sizes for each optimization problem, analyzing performance with both VQE and QAOA algorithms.

**Dataset:** The study used three combinatorial optimization problems as case studies: Max-Cut (graph instances), Number Partitioning (sets of positive integers), and Portfolio Optimization (assets with expected returns and covariances). Specific datasets or financial data sources are not explicitly detailed beyond the problem definitions.
## Findings
- [supported] Ascending-CVaR objective function outperforms standard objective functions and constant CVaR in all tested cases (Max-Cut, Number Partitioning, Portfolio Optimisation) in simulation, achieving up to ten times greater overlap with the ideal state in Portfolio Optimisation and Number Partitioning, and an 80% improvement in Max-Cut.
- [supported] Ascending-CVaR finds the correct solution in 95% of hard instances for the Number Partitioning problem, compared to 60% for constant CVaR and near-total failure for standard objective functions.
- [supported] The proposed method demonstrates faster convergence and higher accuracy in simulation, using VQE with hardware-efficient ansatz and QAOA on problem sizes up to 20 qubits.
- [speculative] Ascending-CVaR may offer greater advantage in harder instances of combinatorial optimisation problems, where other methods frequently fail.
- [speculative] The method could be extended to problems with ~50 qubits, with sigmoid ascending functions potentially performing better in such cases.
- [speculative] Quantum advantage for variational quantum algorithms in optimisation problems may emerge in the NISQ era, though large fault-tolerant quantum computers are still required for broader advantage.

**Results summary:** The paper introduces Ascending-CVaR, an evolving objective function for variational quantum optimisation algorithms, tested via classical simulations on Max-Cut, Number Partitioning, and Portfolio Optimisation problems. The method dynamically adjusts the CVaR parameter (α) during optimisation, starting from a small tail of the energy distribution and gradually including the full distribution. Results show that Ascending-CVaR consistently outperforms standard objective functions and constant CVaR in terms of overlap with the ideal solution, convergence speed, and success rate, particularly in hard problem instances. The findings are supported by numerical simulations but remain unvalidated on real quantum hardware.

**Performance claims:**
- Up to ten times greater overlap with the ideal state in Portfolio Optimisation and Number Partitioning
- 80% improvement in overlap for Max-Cut
- 95% success rate in finding the correct solution for hard Number Partitioning instances (vs. 60% for constant CVaR)
- Faster convergence in simulation compared to standard and constant CVaR objective functions
## Quantum advantage claim
**Classification:** speculative

The claimed advantages are based on classical simulations of quantum algorithms (VQE and QAOA) and are not demonstrated on real quantum hardware. While the results suggest potential for improved performance in optimisation problems, any quantum advantage remains speculative until empirically validated on NISQ devices or fault-tolerant systems.
## Limitations
- Experiments conducted only in emulation environments, not on real quantum hardware [inferred]
- Limited to 20 qubits, which may not be sufficient to demonstrate scalability to larger problem sizes
- Performance tested only on synthetic instances of Max-Cut, Number Partitioning, and Portfolio Optimization; real-world financial data not used [inferred]
- Lack of peer review as the paper is a preprint [inferred]
- No comparison with state-of-the-art classical optimization solvers for the tested problems [inferred]
- Dependence on hyperparameters (e.g., ascending factor λ) whose optimal values may vary across problem instances and sizes
- Assumption that the ansatz can achieve a maximum overlap κ with the optimal solution, which may not hold for all problem instances
- No noise mitigation techniques applied, which may affect performance on real NISQ devices [inferred]
- The evolving objective function (Ascending-CVaR) introduces additional complexity in tuning the ascending function (linear vs. sigmoid)
- Results may not generalize to other combinatorial optimization problems beyond the three tested cases
## Open questions
- How does Ascending-CVaR perform on real quantum hardware with noise and decoherence?
- What is the scalability of the method for problem sizes beyond 20 qubits?
- How does the method compare with classical solvers for large-scale instances of the tested problems?
- What is the impact of different ansatz choices on the performance of Ascending-CVaR?
- Can the method be extended to constrained optimization problems without penalty terms?
- How does the choice of ascending function (linear vs. sigmoid) affect performance for harder instances (e.g., ~50 qubits)?
- What is the minimum overlap threshold (ϵ) required to ensure solution quality while truncating the optimization process?

**Future work:**
- Test Ascending-CVaR on real quantum hardware (e.g., IBM Eagle or Rigetti processors)
- Extend the method to larger problem sizes (e.g., 50+ qubits) to assess scalability
- Compare performance with state-of-the-art classical optimization solvers for the tested problems
- Apply noise mitigation techniques to improve robustness on NISQ devices
- Explore adaptive strategies for dynamically selecting the ascending factor λ during optimization
- Investigate the performance of Ascending-CVaR on other combinatorial optimization problems (e.g., traveling salesman, knapsack)
- Develop hybrid quantum-classical approaches that combine Ascending-CVaR with classical post-processing
- Study the impact of different ansatz designs (e.g., problem-specific vs. hardware-efficient) on solution quality
- Optimize the ascending function (e.g., sigmoid vs. linear) for specific problem classes or instances
## Key ideas
- #idea:quantum-advantage — Ascending-CVaR objective function achieves up to ten times greater overlap with the ideal solution in portfolio optimization compared to standard and fixed CVaR approaches in simulation
- #idea:near-term-feasibility — The method is proposed as a NISQ-era solution to improve convergence and accuracy in variational quantum algorithms for optimization problems
- #idea:hybrid-approach — Hybrid quantum-classical algorithms (VQE and QAOA) are used with classical numerical simulations to demonstrate the potential of Ascending-CVaR
- #limitation:simulation-only — Results are based on classical simulations (emulation) with up to 20 qubits, not real quantum hardware
- #limitation:noise — No noise mitigation techniques are applied, which may affect performance on real NISQ devices
- #limitation:qubit-count — Limited to 20 qubits, insufficient for demonstrating scalability to larger, real-world financial problems
## Contradictions
<!-- Step 6 output — where this paper contradicts others -->

## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
