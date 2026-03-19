---
aliases:
- 'Extrapolation method to optimize linear-ramp quantum approximate optimization algorithm
  parameters: Evaluation of runtime scaling'
- Extrapolation method optimize linear
authors:
- Vanessa Dehn
- Martin Zaefferer
- Gerhard Hellstern
- Karthik Jayadevan
- Florentin Reiter
- Thomas Wellens
auto_detected: true
classification: ''
contradiction_flags: []
doi: 10.1103/l5r4-zcqv
evidence_type: ''
idea_tags:
- idea:quantum-advantage
- idea:near-term-feasibility
- idea:hybrid-approach
journal_or_venue: Physical Review A
methodology_tags:
- QAOA
- QUBO
- classical-simulation
paper_type: ''
quantum_advantage_claim: theoretical
related_papers: []
relevance_phase1: high
relevance_phase3: high
source_type: peer-reviewed-empirical
source_type_confidence: high
step1_date: '2026-03-19T14:03:54.243811'
step1_model: Mistral-Large-3
step2_date: '2026-03-19T14:03:59.907507'
step2_model: Mistral-Large-3
step3_date: '2026-03-19T14:04:50.851262'
step3_model: Mistral-Large-3
step4_date: '2026-03-19T14:05:10.419791'
step4_model: Mistral-Large-3
step5_date: '2026-03-19T14:05:25.097930'
step5_model: Mistral-Large-3
step6_date: '2026-03-19T14:05:56.999342'
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
- method/QAOA
- method/QUBO
- method/classical-simulation
- idea/quantum-advantage
- idea/near-term-feasibility
- idea/hybrid-approach
title: 'Extrapolation method to optimize linear-ramp quantum approximate optimization
  algorithm parameters: Evaluation of runtime scaling'
topic_tags:
- portfolio-optimisation
- risk-modelling
year: 2026
zotero_key: ''
---

## Abstract summary
This paper introduces an extrapolation method to optimize parameters for the linear-ramp quantum approximate optimization algorithm (QAOA), aiming to address the bottleneck of parameter optimization in standard QAOA. The authors propose a technique to estimate suitable QAOA parameters by extrapolating from smaller to larger problem sizes, applied to financial and combinatorial optimization problems like portfolio optimization and feature selection. The study evaluates quantum runtime scaling against classical methods, suggesting potential quantum advantages in specific cases such as portfolio optimization.
## Methodology
The paper presents an empirical study evaluating the runtime scaling of the linear-ramp Quantum Approximate Optimization Algorithm (QAOA) for combinatorial optimization problems in financial services, specifically portfolio optimization, feature selection, clustering, and weighted MaxCut. The research design involves formulating these problems as Quadratic Unconstrained Binary Optimization (QUBO) tasks. For classical optimization, the study benchmarks several solvers (CPLEX, GUROBI, MQLib/Burer2002 Heuristic, and Goemans-Williamson algorithm) to establish runtime scaling baselines. For quantum optimization, the linear-ramp QAOA is employed with parameters optimized through an extrapolation method. This method involves creating subproblems of smaller sizes (4 to 10 qubits), performing grid searches to find optimal parameters for these subproblems, fitting the results with a multivariate skew Gaussian function, and extrapolating these parameters to larger problem sizes (up to 28 qubits). The quantum runtime is quantified by the total depth of quantum circuits executed to find the optimal solution, using a noiseless quantum emulator. The study compares the quantum runtime scaling against classical benchmarks to assess potential quantum advantages.

**Algorithms used:** QAOA
**Frameworks:** Qiskit

**Experimental setup:** The experiments were conducted using a noiseless quantum emulator. The quantum circuits were implemented with the linear-ramp QAOA, where parameters were determined through an extrapolation scheme from smaller subproblems (4 to 10 qubits) to larger problem sizes (up to 28 qubits). The classical optimization benchmarks were run on standard computational hardware using established solvers available in IBM's Qiskit.

**Dataset:** 1. Portfolio optimization: Annualized returns and covariance matrices for the German DAX 30 (as of 1/2/2021) between 01/01/2016 and 31/12/2020. For each problem size, instances were created by randomly selecting N out of the 30 DAX assets.
2. Feature selection: 'German Credit Data' with 20 features (7 numerical and 13 categorical) and an imbalanced binary target variable. After one-hot encoding, up to 48 binary features were used.
3. Clustering: 'Moons' and 'Blobs' datasets from Scikit-learn with two features.
4. Weighted MaxCut: Randomly weighted graphs with edge weights drawn from a uniform discrete distribution between 0 and 1000.
## Findings
- [supported] The linear-ramp QAOA (LR-QAOA) with extrapolation-based parameter optimization demonstrates superior runtime scaling compared to classical MQLib/Burer2002 for portfolio optimization problems up to 28 qubits, with quantum scaling exponent α = 0.219 vs. classical α = 0.323
- [supported] For portfolio optimization, the quantum runtime scaling advantage is observed in noiseless quantum emulator simulations, with total depth D ∝ 2^0.219N vs. classical runtime ∝ 2^0.323N
- [supported] The extrapolation method for LR-QAOA parameters (Δ1γ, Δ1β, p) from smaller subproblems (N=4,6,8,10) to larger problems (N=28) yields near-optimal parameters, as validated by grid search comparisons
- [supported] Universal parameter scaling (algebraic fits for Δ1γ, Δ1β, p) reduces outliers and improves runtime scaling for feature selection, clustering, and MaxCut problems, achieving scaling exponents comparable to classical benchmarks
- [supported] The probability P_opt of measuring the optimal solution remains above 0.1 on average for all problem classes, with portfolio optimization and MaxCut showing constant or slightly increasing P_opt with problem size N
- [speculative] The authors suggest that combining the extrapolation method with other fixed-parameter QAOA schedules (e.g., Fourier heuristic, Trotterized quantum annealing) could further improve runtime scaling advantages
- [speculative] The observed quantum scaling advantage for portfolio optimization may extend to larger problem sizes beyond 28 qubits, though this remains untested in the study

**Results summary:** The paper presents an extrapolation method for optimizing linear-ramp QAOA parameters, demonstrating a quantum runtime scaling advantage for portfolio optimization problems up to 28 qubits. Using noiseless quantum emulator simulations, the authors show that LR-QAOA with extrapolated parameters achieves a scaling exponent of α = 0.219, outperforming the classical MQLib/Burer2002 heuristic (α = 0.323). The extrapolation method, which derives parameters for larger problems from smaller subproblems, is validated through grid search comparisons and reduces the need for expensive variational optimization. For other problem classes (feature selection, clustering, MaxCut), universal parameter scaling improves quantum runtime scaling, though only portfolio optimization shows a clear advantage over classical methods. The probability of measuring the optimal solution remains above 0.1 on average, suggesting potential for subexponential scaling with problem size.

**Performance claims:**
- Quantum runtime scaling exponent α = 0.219 for portfolio optimization (vs. classical α = 0.323)
- Total depth D ∝ 2^0.219N for quantum vs. 2^0.323N for classical portfolio optimization
- Extrapolation method achieves near-optimal parameters with 10-20x fewer circuit evaluations than grid search for N=28
- Universal parameter scaling reduces runtime scaling exponents to α = 0.16-0.22 across all problem classes
- Average P_opt > 0.1 for all problem classes, with portfolio optimization and MaxCut showing constant or increasing P_opt with N
## Quantum advantage claim
**Classification:** theoretical

The paper demonstrates a theoretical quantum advantage in runtime scaling for portfolio optimization, with results derived from noiseless quantum emulator simulations. The advantage is quantified through exponential scaling exponents (α = 0.219 quantum vs. α = 0.323 classical), but remains untested on real quantum hardware or for problem sizes beyond 28 qubits.
## Limitations
- Experiments conducted on a noiseless quantum emulator, not real quantum hardware [inferred]
- Hardware noise and decoherence effects are not accounted for in the runtime scaling analysis [inferred]
- Qubit count constraints limit the problem sizes to 28 qubits, which may not be sufficient to demonstrate practical scalability
- Extrapolation method relies on small subproblems (up to 10 qubits) to predict parameters for larger problems, which may not generalize [inferred]
- Dataset size and diversity are limited (e.g., portfolio optimization uses only 30 DAX assets, feature selection uses one dataset with 48 features)
- Reproducibility may be affected by random sampling of subinstances and problem instances
- Classical benchmarks (e.g., MQLib/Burer2002) may not fully represent state-of-the-art classical solvers for all problem types [inferred]
- Universal parameter scaling assumes algebraic behavior, which may not hold for all problem instances or larger sizes [inferred]
- Outliers in clustering results suggest instability in the extrapolation method for certain problem types
- No comparison with other quantum optimization algorithms (e.g., QAOA with different schedules, VQE) [inferred]
- Runtime scaling analysis does not account for quantum gate execution times or hardware-specific constraints [inferred]
## Open questions
- Can the observed quantum scaling advantage for portfolio optimization be maintained on real quantum hardware with noise?
- How does the extrapolation method perform for problem sizes beyond 28 qubits?
- What is the impact of decoherence and hardware noise on the probability of measuring the optimal solution (P_opt)?
- Are there problem instances where the universal parameter scaling fails to provide good circuit parameters?
- How does the quantum runtime scaling compare with more advanced classical heuristics or hybrid quantum-classical approaches?
- Can the algebraic scaling of circuit parameters (Δ1γ, Δ1β, p) be theoretically justified?
- What is the minimum probability P_opt required to achieve a practical quantum advantage for real-world financial problems?
- How does the choice of subproblem sampling affect the accuracy of the extrapolation method?
- Are there combinatorial optimization problems in finance where LR-QAOA consistently outperforms classical methods?

**Future work:**
- Test the extrapolation method on real quantum hardware (e.g., IBM Eagle processor) to validate noise resilience
- Extend the analysis to larger problem sizes (beyond 28 qubits) to assess scalability
- Incorporate noise mitigation techniques (e.g., error correction, dynamical decoupling) into the runtime scaling analysis
- Compare LR-QAOA with other quantum optimization algorithms (e.g., standard QAOA, VQE) for financial use cases
- Develop theoretical models to justify the algebraic scaling of circuit parameters with problem size
- Apply the method to more realistic financial datasets (e.g., larger asset universes, multi-period optimization)
- Explore hybrid quantum-classical approaches to improve solution quality and runtime
- Investigate the impact of different subproblem sampling strategies on extrapolation accuracy
- Assess the method's performance on other combinatorial optimization problems relevant to finance (e.g., option pricing, risk management)
## Key ideas
- #idea:quantum-advantage — LR-QAOA with extrapolated parameters demonstrates superior runtime scaling (α = 0.219) compared to classical MQLib/Burer2002 (α = 0.323) for portfolio optimization up to 28 qubits in noiseless emulation
- #idea:near-term-feasibility — Extrapolation method reduces QAOA parameter optimization overhead by deriving parameters for larger problems from smaller subproblems (4-10 qubits), improving near-term applicability
- #idea:hybrid-approach — Linear-ramp QAOA schedule simplifies parameter optimization by reducing free parameters to two, enabling more efficient quantum-classical hybrid workflows
- #limitation:simulation-only — Quantum advantage claims are based on noiseless emulation, not real quantum hardware, limiting empirical validation
- #limitation:qubit-count — Problem sizes limited to 28 qubits, insufficient for real-world financial applications requiring larger asset universes
- #limitation:noise — No noise mitigation techniques applied, which could degrade performance on real quantum devices and invalidate scaling advantages
- #limitation:data-encoding — Extrapolation method relies on small subproblems (4-10 qubits) to predict parameters for larger problems, with untested generalization to real-world datasets
## Contradictions
<!-- Step 6 output — where this paper contradicts others -->

## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
