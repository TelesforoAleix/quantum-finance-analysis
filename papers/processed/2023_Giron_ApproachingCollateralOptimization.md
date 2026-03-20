---
aliases:
- Approaching Collateral Optimization for NISQ and Quantum-Inspired Computing
- Approaching Collateral Optimization NISQ
authors:
- Megan C. Giron
- Georgios Korpas
- Waqas Parvaiz
- Prashant Malik
- Johannes Aspman
auto_detected: true
classification: ''
contradiction_flags:
- contradiction:classical-vs-quantum
- contradiction:scalability
doi: 10.1109/TQE.2023.3314839
evidence_type: ''
idea_tags:
- idea:quantum-advantage
- idea:near-term-feasibility
- idea:hybrid-approach
journal_or_venue: IEEE Transactions on Quantum Engineering
methodology_tags:
- QAOA
- quantum-annealing
- QUBO
- variational
- classical-simulation
paper_type: ''
quantum_advantage_claim: speculative
related_papers:
- 2022_Pusey_Nazzaro_QuantumAnnealingNPHard
relevance_phase1: high
relevance_phase3: high
source_type: peer-reviewed-empirical
source_type_confidence: high
step1_date: '2026-03-19T23:30:48.128706'
step1_model: Mistral-Large-3
step2_date: '2026-03-19T23:30:52.105617'
step2_model: Mistral-Large-3
step3_date: '2026-03-19T23:31:07.504954'
step3_model: Mistral-Large-3
step4_date: '2026-03-19T23:31:34.573415'
step4_model: Mistral-Large-3
step5_date: '2026-03-19T23:31:45.976777'
step5_model: Mistral-Large-3
step6_date: '2026-03-19T23:31:50.338234'
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
- method/quantum-annealing
- method/QUBO
- method/variational
- method/classical-simulation
- idea/quantum-advantage
- idea/near-term-feasibility
- idea/hybrid-approach
- contradiction/classical-vs-quantum
- contradiction/scalability
title: Approaching Collateral Optimization for NISQ and Quantum-Inspired Computing
topic_tags:
- portfolio-optimisation
- risk-modelling
year: 2023
zotero_key: ''
---

## Abstract summary
This paper explores the application of quantum and quantum-inspired computing techniques to collateral optimization in financial services. The authors formulate the collateral optimization problem as a mixed-integer linear programming (MILP) model and then convert it into a quadratic unconstrained binary optimization (QUBO) framework suitable for noisy intermediate-scale quantum (NISQ) devices. The study conducts small-scale computational tests to assess the performance of these formulations, highlighting their potential for large-scale financial optimization problems despite current hardware limitations.
## Methodology
The paper presents a study on collateral optimization (ColOpt) in financial services, focusing on formulating the problem as a mixed-integer linear programming (MILP) model and subsequently as a quadratic unconstrained binary optimization (QUBO) model. The goal is to minimize the cost of posting collateral while satisfying exposure requirements and other constraints. The authors explore both balanced and unbalanced QUBO formulations, leveraging slack variables and penalization techniques. Small-scale computational tests are conducted using various software development kits, including Qiskit, PyQUBO, ToQUBO.jl, and Fujitsu’s digital annealer emulator. The study also surveys alternative approaches for solving combinatorial optimization problems, such as quantum annealing (QA), variational quantum algorithms (VQAs), and quantum-inspired methods like simulated annealing (SA). The MILP formulation serves as a baseline, while QUBO formulations are tested for their potential applicability on near-term quantum and quantum-inspired hardware.

**Algorithms used:** QAOA, Quantum Annealing, Simulated Annealing
**Frameworks:** Qiskit, PyQUBO, ToQUBO.jl, Fujitsu Digital Annealer

**Experimental setup:** The experiments involve small-scale problem instances of collateral optimization and the knapsack problem. The QUBO formulations are tested using emulators of quantum and quantum-inspired solvers, including D-Wave’s simulated annealer (via the neal package), Qiskit’s optimization module, and Fujitsu’s digital annealer. The MILP formulations are solved using classical solvers like HiGHS and GLPK. The study focuses on algorithmic reformulation and heuristic evaluation rather than hardware-specific performance.

**Dataset:** Synthetic small-scale datasets for the knapsack problem and collateral optimization problem. The knapsack problem instance includes 10 items with predefined weights and values. The collateral optimization problem involves hypothetical assets and accounts with parameters such as asset quantity, market value, tier, haircut, and exposure requirements.
## Findings
- [supported] The QUBO-based approaches for collateral optimization (ColOpt) failed to find global optima in small-scale experiments but produced solutions reasonably close to the optimal, suggesting potential for large instances [supported]
- [supported] The mixed-integer linear programming (MILP) formulation of ColOpt was successfully implemented and used as a benchmark for QUBO formulations [supported]
- [supported] Small-scale tests using quantum-inspired methods (e.g., simulated annealing, digital annealing) demonstrated promising performance for QUBO formulations of ColOpt, though results were heuristic and limited by emulator constraints [supported]
- [speculative] Quantum or quantum-inspired solvers may provide computational or business advantage for large-scale ColOpt instances in the near term [speculative]
- [speculative] The unbalanced penalization QUBO formulation could reduce resource requirements and search space, but its constraints are less strict, potentially leading to suboptimal solutions [speculative]
- [disputed] The paper notes that prior work (e.g., Pusey-Nazzaro et al.) found quantum annealing (D-Wave) and classical simulated annealing failed to outperform branch-and-bound methods for certain NP-hard problems, contradicting claims of quantum advantage [disputed]
- [supported] The study found that off-the-shelf QUBO converters (e.g., ToQUBO.jl, Qiskit) and custom slack-based formulations successfully solved small Knapsack problem instances, but required more runs than classical solvers [supported]
- [speculative] The authors suggest that hybrid quantum-classical approaches (e.g., QAOA, quantum annealing) could be viable for ColOpt once hardware capabilities improve [speculative]

**Results summary:** The paper presents a mixed-integer linear programming (MILP) formulation for collateral optimization (ColOpt) and reformulates it as a quadratic unconstrained binary optimization (QUBO) problem to explore hybrid quantum and quantum-inspired solutions. Small-scale experiments using quantum-inspired methods (e.g., simulated annealing, digital annealing) demonstrated that QUBO approaches, while failing to find global optima, produced solutions close to optimal, indicating potential for larger instances. The study highlights the limitations of current quantum hardware and emulators but suggests that quantum or quantum-inspired solvers could offer advantages for large-scale ColOpt problems in the future. The paper also surveys alternative QUBO formulations and solvers, noting their trade-offs in resource requirements and solution quality.

**Performance claims:**
- QUBO-based approaches achieved near-optimal solutions in small-scale ColOpt experiments, though global optima were not reached
- Off-the-shelf QUBO converters (ToQUBO.jl, Qiskit) and custom slack-based formulations solved small Knapsack problem instances with known optimal solutions
- Simulated annealing and digital annealing required more runs than classical MILP solvers to reach optimal solutions for small instances
## Quantum advantage claim
**Classification:** speculative

The paper suggests that quantum or quantum-inspired solvers may provide computational or business advantage for large-scale ColOpt instances, but this claim is based on heuristic results from small-scale simulations and emulations. No empirical demonstration of quantum advantage on real hardware was provided, and prior literature (e.g., Pusey-Nazzaro et al.) disputes such claims for similar problems.
## Limitations
- Small-scale experiments limit the generalizability of findings to larger, real-world collateral optimization problems
- QUBO-based approaches failed to find global optima in small-scale experiments, only achieving near-optimal solutions
- Experiments conducted using software development kits and emulators, not real quantum hardware, limiting assessment of real-world performance [inferred]
- Hardware noise and qubit count constraints in NISQ devices may significantly degrade solution quality for larger problem instances [inferred]
- Lack of comparison with state-of-the-art classical MILP solvers (e.g., IBM CPLEX, Gurobi) for benchmarking performance [inferred]
- Limited dataset size and use of synthetic data rather than real market data for collateral optimization tests
- Reproducibility challenges due to heuristic nature of quantum and quantum-inspired solvers (e.g., simulated annealing, digital annealing)
- Scalability to production-level collateral optimization problems remains untested due to small problem instance sizes
- Unbalanced penalization approaches may softly break constraints (e.g., weight limits in knapsack problems), leading to infeasible solutions [inferred]
- Internal validity concerns due to reliance on emulators and lack of real quantum hardware validation
- Potential bias in noise of circuits implementing variational quantum algorithms (VQAs) may unfavorably affect convergence ratios [inferred]
- Resource-intensive hyperparameter tuning required for QUBO formulations, which may not be feasible for large-scale problems [inferred]
- Limited exploration of alternative QUBO encodings (e.g., one-hot encoding) due to high bit requirements for large problem instances
- Lack of empirical validation for theoretical advantages of quantum approaches in financial optimization
## Open questions
- How do QUBO-based approaches perform on real quantum hardware compared to classical MILP solvers for collateral optimization?
- What is the impact of decoherence and hardware noise on solution quality for larger problem instances?
- Can hybrid quantum-classical approaches (e.g., QAOA, quantum annealing) achieve computational advantage for large-scale collateral optimization?
- How does the performance of quantum-inspired methods (e.g., digital annealing) scale with problem size compared to classical solvers?
- What are the trade-offs between solution accuracy and resource usage (e.g., qubit count, runtime) for different QUBO formulations?
- How do alternative approaches (e.g., GNNs, SQA, quantum hybrid Frank–Wolfe) compare to traditional QUBO solvers for financial optimization?
- What is the minimum qubit count required to achieve practical advantage for real-world collateral optimization problems?
- How can constraint violations in unbalanced penalization approaches be minimized or mitigated?
- What are the implications of relaxing exposure constraints (e.g., from inequality to equality) on solution feasibility and optimality?
- How do different binary encodings (e.g., log encoding vs. one-hot encoding) affect solution quality and resource requirements?

**Future work:**
- Test QUBO formulations on real quantum hardware (e.g., IBM Eagle, D-Wave Advantage) for collateral optimization
- Extend experiments to larger problem instances to assess scalability and performance
- Benchmark quantum and quantum-inspired approaches against state-of-the-art classical MILP solvers (e.g., IBM CPLEX, Gurobi)
- Explore noise mitigation techniques to improve solution quality on NISQ devices
- Investigate hybrid quantum-classical algorithms (e.g., QAOA) for collateral optimization with real market data
- Develop automated approaches for hyperparameter tuning in QUBO formulations to reduce resource overhead
- Apply alternative QUBO encodings (e.g., unbalanced penalization) to larger problem instances and assess constraint adherence
- Compare performance of quantum-inspired methods (e.g., digital annealing, simulated annealing) with classical solvers for financial optimization
- Explore the use of graph neural networks (GNNs) and other machine learning techniques for QUBO-based collateral optimization
- Assess the feasibility of quantum advantage for collateral optimization in production environments
- Investigate the impact of different constraint formulations (e.g., equality vs. inequality) on solution quality and feasibility
- Develop frameworks for integrating quantum and classical solvers in hybrid optimization pipelines
## Key ideas
- #idea:hybrid-approach — Hybrid quantum-classical methods (QUBO + MILP) are proposed as a practical path for collateral optimization in NISQ-era devices
- #idea:near-term-feasibility — The paper argues for the suitability of NISQ-era devices for financial optimization problems like collateral allocation
- #idea:quantum-advantage — Speculative claim that QUBO formulations may provide computational or business advantage for large-scale collateral optimization
- #limitation:no-empirical-validation — Quantum advantage claims are not empirically validated on real quantum hardware, only simulated environments
- #limitation:simulation-only — Results are derived from classical simulations and emulators, not real QPUs
- #idea:hybrid-approach — Quantum-inspired methods (e.g., simulated annealing, digital annealing) performed well on small-scale problems, suggesting hybrid potential
## Contradictions
- #contradiction:classical-vs-quantum — The paper acknowledges prior work (Pusey-Nazzaro et al.) showing quantum annealing and simulated annealing perform poorly compared to classical branch-and-bound for NP-hard problems, contradicting its own speculative advantage claims
- #contradiction:scalability — Claims of near-term quantum advantage for large-scale problems are contradicted by the paper's own limitations (small-scale experiments, lack of real hardware validation, and untested scalability)
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->

## Experiment details
### Input
{'knapsack_problem': {'source': 'Synthetic dataset from literature', 'size': '10 items', 'features': ['weight', 'value'], 'preprocessing': 'Binary encoding of decision variables, slack variable representation for constraints'}, 'collateral_optimization': {'source': 'Hypothetical financial data', 'size': 'Small-scale instances with a few assets and accounts', 'features': ['asset quantity', 'market value', 'tier', 'haircut', 'exposure requirement', 'account duration'], 'preprocessing': 'Discretization of fractional allocations into binary variables, constraint binarization'}}

### Process
1. Formulate the collateral optimization problem as an MILP. 2. Convert the MILP into a QUBO model using both balanced (slack-based) and unbalanced penalization approaches. 3. Encode decision variables into binary representations. 4. Implement QUBO formulations using software development kits (Qiskit, PyQUBO, ToQUBO.jl, Fujitsu Digital Annealer). 5. Run heuristic optimizers (simulated annealing, digital annealing) to solve the QUBO instances. 6. Compare results against classical MILP solvers (HiGHS, GLPK) for optimality and constraint satisfaction.

### Output
{'metrics_reported': ['Objective function value (cost of collateral)', 'Constraint satisfaction (exposure, consistency, limits)', 'Solution optimality (comparison to MILP baseline)'], 'comparison_baselines': ['Classical MILP solvers (HiGHS, GLPK)', 'Balanced vs. unbalanced QUBO formulations'], 'output_format': 'Optimal asset allocations, objective function values, constraint violation metrics'}

### Parameters
- qubit_count: None
- circuit_depth: None
- shots: None
- optimizer: Simulated Annealing (neal), Digital Annealing (Fujitsu)
- learning_rate: None
- hyperparameters: {'penalty_weights': ['λ0', 'λ1', 'λ2', 'λ3'], 'binary_precision': 'B (number of bits for discretization)', 'slack_variable_encoding': ['log encoding', 'one-hot encoding']}

### Hardware
{'simulator': 'D-Wave simulated annealer (neal), Fujitsu Digital Annealer emulator, Qiskit Aer simulator', 'QPU_model': None, 'cloud_provider': None, 'transpilation_settings': None}

### Reproducibility
The paper provides detailed formulations and parameter settings for both MILP and QUBO models. Code and data are not explicitly linked, but the methodology descriptions are sufficiently detailed to replicate the small-scale experiments. The use of synthetic datasets ensures reproducibility for the tested instances.
