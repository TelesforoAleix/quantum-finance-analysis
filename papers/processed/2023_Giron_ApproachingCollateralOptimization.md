---
aliases:
- Approaching Collateral Optimization for NISQ and Quantum-Inspired Computing
- Approaching Collateral Optimization NISQ
authors:
- MEGAN C. GIRON
- GEORGIOS KORPAS
- WAQAS PARVAIZ
- PRASHANT MALIK
- JOHANNES ASPMAN
auto_detected: true
classification: ''
contradiction_flags:
- contradiction:classical-vs-quantum
- contradiction:scalability
doi: 10.1109/TQE.2023.3314839
evidence_type: ''
idea_tags:
- idea:near-term-feasibility
- idea:hybrid-approach
- idea:quantum-advantage
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
- Pusey-Nazzaro_etal
relevance_phase1: high
relevance_phase3: medium
source_type: peer-reviewed-empirical
source_type_confidence: high
step1_date: '2026-03-18T22:52:50.400710'
step1_model: Mistral-Large-3
step2_date: '2026-03-18T22:53:45.538158'
step2_model: Mistral-Large-3
step3_date: '2026-03-18T22:53:49.241500'
step3_model: Mistral-Large-3
step4_date: '2026-03-18T22:53:59.137610'
step4_model: Mistral-Large-3
step5_date: '2026-03-18T22:54:04.731139'
step5_model: Mistral-Large-3
step6_date: '2026-03-18T22:54:52.785550'
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
- idea/near-term-feasibility
- idea/hybrid-approach
- idea/quantum-advantage
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
This paper explores collateral optimization in financial services, a combinatorial problem involving the efficient allocation of assets to minimize costs while meeting transaction obligations. The authors present both mixed-integer linear programming and quadratic unconstrained binary optimization (QUBO) formulations to address the problem, targeting hybrid-quantum and noisy intermediate-scale quantum (NISQ) computing approaches. The study tests small-scale implementations and discusses the potential of quantum and quantum-inspired methods for large-scale optimization challenges in finance.
## Methodology
The paper presents a study on collateral optimization in financial services, initially formulating the problem as a mixed-integer linear programming (MILP) model. The authors then convert this into a quadratic unconstrained binary optimization (QUBO) formulation to explore hybrid-quantum and NISQ-era quantum computing approaches. The research involves small-scale computational tests using various software development kits to evaluate the performance of QUBO-based methods compared to classical MILP solvers. The study also surveys alternative quantum and quantum-inspired methods for combinatorial optimization, including variational quantum algorithms (VQAs) like QAOA, quantum annealing (QA), and quantum-inspired techniques such as simulated annealing (SA) and digital annealing. The methodology focuses on comparing different QUBO encodings for small instances of the knapsack problem to inform the collateral optimization problem, with experiments conducted using classical solvers (HiGHS, GLPK) and QUBO solvers (ToQUBO.jl, Qiskit, PyQUBO, Fujitsu’s digital annealer).

**Algorithms used:** QAOA, Quantum Annealing, Simulated Annealing, Mixed-Integer Linear Programming (MILP)
**Frameworks:** Qiskit, ToQUBO.jl, PyQUBO, Fujitsu Digital Annealer, HiGHS, GLPK

**Experimental setup:** Experiments were conducted using small-scale problem instances. Classical MILP solvers (HiGHS, GLPK) were used for baseline comparisons. QUBO formulations were tested using open-source libraries (ToQUBO.jl, Qiskit’s optimization module, PyQUBO) and Fujitsu’s digital annealer emulator. The study did not use real quantum processing units (QPUs) but relied on simulators and emulators for quantum and quantum-inspired approaches.

**Dataset:** A small knapsack problem instance with 10 items was used to test QUBO formulations. For collateral optimization, the paper does not specify a particular dataset but discusses the problem in the context of financial institutions managing pools of assets with associated costs and risks.
## Findings
- [supported] The QUBO-based approaches for collateral optimization (ColOpt) failed to find global optima in small-scale experiments but achieved solutions reasonably close to the optimal, suggesting potential for large instances [simulation-based results].
- [supported] Mixed-integer linear programming (MILP) formulations successfully solved small-scale collateral optimization problems, serving as a benchmark for quantum and quantum-inspired methods.
- [supported] Quantum-inspired formulations (e.g., simulated annealing, digital annealing) performed well on small-scale Knapsack problem instances, matching known optimal solutions [simulation-based results].
- [speculative] The authors suggest that QUBO formulations may provide computational or business advantage for large-scale collateral optimization problems on real quantum or quantum-inspired hardware.
- [speculative] Quantum advantage in collateral optimization is implied to be achievable in the near term, given the suitability of NISQ-era devices for financial use cases.
- [disputed] The paper acknowledges that prior work (e.g., Pusey-Nazzaro et al.) found quantum annealing (D-Wave) and simulated annealing to perform poorly compared to classical branch-and-bound methods for certain NP-hard problems.
- [disputed] The lack of transparent computational advantage in variational quantum algorithms (VQAs) due to local minima and noise bias is noted, contradicting some claims in the literature.

**Results summary:** The paper presents a mixed-integer linear programming (MILP) formulation for collateral optimization (ColOpt) and explores its conversion to quadratic unconstrained binary optimization (QUBO) for hybrid quantum-classical approaches. Small-scale experiments using quantum-inspired methods (simulated annealing, digital annealing) and QUBO formulations demonstrated near-optimal solutions for the Knapsack problem, a simplified proxy for ColOpt. However, QUBO-based approaches did not achieve global optima for ColOpt, though their proximity to optimal solutions suggests potential scalability. The study highlights the limitations of current quantum and quantum-inspired methods compared to classical MILP solvers but argues for further investigation into larger problem instances.

**Performance claims:**
- QUBO formulations matched the known optimal solution (objective value = 309) for a small Knapsack problem instance using simulated annealing and digital annealing [simulation-based].
- Log-encoding and one-hot encoding slack variable approaches successfully found optimal solutions for the Knapsack problem with varying penalty weights [simulation-based].
- Unbalanced penalization QUBO formulations reduced variable requirements and achieved optimal solutions for the Knapsack problem [simulation-based].
## Quantum advantage claim
**Classification:** speculative

The paper suggests that quantum or quantum-inspired methods may provide computational or business advantage for large-scale collateral optimization, but all results are derived from simulations. No empirical demonstration of quantum advantage on real hardware is provided, and prior literature disputes similar claims for other NP-hard problems.
## Limitations
- Small-scale experiments limit the generalizability of results to real-world collateral optimization problems
- QUBO-based approaches failed to find global optima in small-scale tests, only achieving near-optimal solutions
- Experiments conducted using software development kits and emulators, not real quantum hardware [inferred]
- Hardware noise and qubit count constraints of NISQ devices were not explicitly addressed in the empirical tests
- Dataset size and complexity were limited, focusing only on simplified instances of the knapsack problem to inform collateral optimization
- Lack of comparison with state-of-the-art classical MILP solvers for larger problem instances [inferred]
- Reproducibility may be limited due to heuristic nature of quantum-inspired solvers and lack of detailed noise characterization
- No empirical validation of performance on real-world financial datasets, only synthetic or toy problem instances
- Scalability to production-level collateral optimization problems remains untested due to resource constraints
- Internal validity concerns due to reliance on emulators and simulated annealing, which may not reflect real quantum hardware behavior [inferred]
- Potential bias in results due to proprietary solvers (e.g., Fujitsu’s digital annealer) with undisclosed implementation details [inferred]
## Open questions
- How do QUBO-based approaches perform on large-scale collateral optimization problems with hundreds or thousands of assets?
- What is the impact of hardware noise and decoherence on solution quality for real quantum devices?
- Can quantum-inspired or hybrid quantum-classical methods outperform classical MILP solvers for practical collateral optimization instances?
- How does the choice of QUBO formulation (e.g., balanced vs. unbalanced penalization) affect solution quality and resource requirements?
- What are the trade-offs between solution accuracy and computational time for quantum vs. classical approaches in financial optimization?
- How do different quantum algorithms (e.g., QAOA, quantum annealing) compare for collateral optimization problems?
- What is the minimum qubit count and coherence time required to achieve a practical advantage for collateral optimization?
- How sensitive are the results to variations in problem constraints (e.g., nonlinearities, regulatory requirements)?

**Future work:**
- Test QUBO formulations on real quantum hardware (e.g., IBM Eagle, D-Wave Advantage) for larger problem instances
- Extend the study to multi-period collateral optimization with dynamic constraints
- Compare quantum and quantum-inspired approaches with state-of-the-art classical solvers for large-scale problems
- Investigate noise mitigation techniques to improve solution quality on NISQ devices
- Develop hybrid quantum-classical algorithms tailored for collateral optimization
- Explore alternative QUBO encodings to reduce qubit requirements and improve solution accuracy
- Apply the methodology to real-world financial datasets from large institutions
- Benchmark performance across different quantum computing platforms (gate-based, annealing, quantum-inspired)
- Study the impact of regulatory constraints (e.g., Basel III, Dodd-Frank) on quantum optimization formulations
- Investigate the potential for quantum advantage in collateral optimization through resource estimation and complexity analysis
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
