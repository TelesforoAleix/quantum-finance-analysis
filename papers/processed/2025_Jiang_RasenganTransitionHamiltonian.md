---
aliases:
- 'Rasengan: A Transition Hamiltonian-based Approximation Algorithm for Solving Constrained
  Binary Optimization Problems'
- Rasengan Transition Hamiltonian based
authors:
- Qifan Jiang
- Liqiang Lu
- Debin Xiang
- Tianyao Chu
- Tianze Zhu
- Jingwen Leng
- Yun Liang
- Xiaoming Sun
- Jianwei Yin
auto_detected: true
classification: ''
contradiction_flags:
- contradiction:classical-vs-quantum
- contradiction:scalability
doi: 10.1145/3725843.3756107
evidence_type: ''
idea_tags:
- idea:quantum-advantage
- idea:near-term-feasibility
- idea:hybrid-approach
journal_or_venue: 58th IEEE/ACM International Symposium on Microarchitecture (MICRO
  ’25)
methodology_tags:
- variational
- QAOA
- quantum-annealing
- QUBO
- quantum-simulation
paper_type: ''
quantum_advantage_claim: speculative
related_papers: []
relevance_phase1: high
relevance_phase3: high
source_type: conference-paper
source_type_confidence: high
step1_date: '2026-03-19T13:39:55.793698'
step1_model: Mistral-Large-3
step2_date: '2026-03-19T13:40:07.737184'
step2_model: Mistral-Large-3
step3_date: '2026-03-19T13:41:19.056379'
step3_model: Mistral-Large-3
step4_date: '2026-03-19T13:41:29.910578'
step4_model: Mistral-Large-3
step5_date: '2026-03-19T13:42:29.991027'
step5_model: Mistral-Large-3
step6_date: '2026-03-19T13:42:38.566520'
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
- topic/derivatives-pricing
- topic/fraud-detection
- topic/credit-scoring
- topic/high-frequency-trading
- method/variational
- method/QAOA
- method/quantum-annealing
- method/QUBO
- method/quantum-simulation
- idea/quantum-advantage
- idea/near-term-feasibility
- idea/hybrid-approach
- contradiction/classical-vs-quantum
- contradiction/scalability
title: 'Rasengan: A Transition Hamiltonian-based Approximation Algorithm for Solving
  Constrained Binary Optimization Problems'
topic_tags:
- portfolio-optimisation
- risk-modelling
- derivatives-pricing
- fraud-detection
- credit-scoring
- high-frequency-trading
year: 2025
zotero_key: ''
---

## Abstract summary
This conference paper introduces Rasengan, a novel variational quantum algorithm designed to solve constrained binary optimization problems with high precision and low circuit complexity. Unlike traditional methods that shrink the search space from a superposition of all possible solutions, Rasengan expands the space from a single feasible solution using a transition Hamiltonian, ensuring all explored states remain feasible. The paper also presents optimization techniques to reduce circuit depth and improve deployability on noisy quantum hardware.
## Methodology
The paper introduces Rasengan, a novel variational quantum algorithm designed to solve constrained binary optimization problems, which are prevalent in financial services and other domains. The methodology employs a transition Hamiltonian-based approach that expands the search space from an initial feasible solution rather than shrinking the entire solution space, as done in traditional variational quantum algorithms (VQAs) like QAOA and HEA. The transition Hamiltonian is formulated to explore the feasible solution space using homogeneous basis vectors derived from linear algebra, ensuring that all generated solutions adhere to the problem constraints. The algorithm incorporates three key optimization techniques to enhance deployability on noisy intermediate-scale quantum (NISQ) devices: Hamiltonian simplification and pruning to reduce circuit complexity, segmented execution to manage circuit depth, and solution purification for error mitigation. The experimental evaluation compares Rasengan against state-of-the-art VQAs (HEA, P-QAOA, Choco-Q) using benchmarks from facility location, k-partition, job scheduling, set covering, and graph coloring problems. The study includes both noise-free simulations and real-world quantum hardware experiments on IBM Quantum platforms (Kyiv and Brisbane). Evaluation metrics include approximation ratio gap (ARG), circuit depth, number of parameters, and in-constraints rate.

**Algorithms used:** Transition Hamiltonian, Variational Quantum Algorithm (VQA), QAOA, HEA
**Frameworks:** Qiskit

**Experimental setup:** Experiments were conducted using both noise-free quantum simulators and real quantum processing units (QPUs) on IBM Quantum platforms (Kyiv and Brisbane with 127-qubit Eagle r3 processors). The classical optimization part was executed on an AMD EPYC 9554 64-core server with 1TB RAM, and quantum circuit simulations were accelerated using the DDSim simulator for Rasengan and CUDA-quantum for QAOA/HEA on an NVIDIA A100 GPU. The evaluation involved 2000 cases across five problem domains, with benchmarks ranging from 6 to 28 qubits. The experimental setup included comparisons with baseline VQAs (HEA, P-QAOA, Choco-Q) using identical layer repetitions and optimization iterations. Circuit depths and gate counts were analyzed post-compilation for real hardware deployment.

**Dataset:** The study utilized synthetic benchmarks from five problem domains: facility location problem (FLP), k-partition problem (KPP), job scheduling problem (JSP), set covering problem (SCP), and graph coloring problem (GCP). Each domain included 400 cases compiled from relevant literature, with problem sizes ranging from 6 to 24 variables (qubits) and varying constraint complexities. Specific datasets were not named but were designed to represent real-world scenarios in financial services and other optimization fields.
## Findings
- [supported] Rasengan improves accuracy by 4.12× compared to the state-of-the-art QAOA (Choco-Q) on constrained binary optimization problems across 2000 cases from five domains (facility location, k-partition, job scheduling, set cover, and graph coloring).
- [supported] Rasengan achieves a 379× improvement in solution quality over baseline methods on real-world quantum platforms (IBM Kyiv and Brisbane).
- [supported] Rasengan reduces circuit depth by 1.96× compared to prior variational quantum algorithms (VQAs) and by 49× compared to Choco-Q, making it deployable on NISQ devices.
- [supported] Rasengan is the first quantum algorithm to outperform the mean quality of feasible solution baselines on real hardware, achieving an approximation ratio gap (ARG) as low as 0.01 for small-scale problems.
- [supported] Hamiltonian simplification and pruning techniques reduce circuit depth by over 94.6%, while probability-preserving segmented execution further reduces depth to ~50, suitable for current quantum hardware.
- [supported] Error mitigation via solution purification improves accuracy by more than 303× on noisy hardware.
- [speculative] Rasengan’s transition Hamiltonian-based approach may theoretically scale to larger problem sizes (100+ qubits) due to its exponential exploration of feasible solution spaces.
- [speculative] The authors claim that Rasengan eliminates the need for encoding objective Hamiltonians in higher-order problems, offering greater generality than QAOA.
- [supported] Rasengan maintains a 100% in-constraints rate (feasible solutions) on real hardware, unlike penalty-term-based QAOA, which often violates constraints.
- [disputed] The paper claims Rasengan achieves quantum advantage on real hardware, but this is disputed as the results are compared to classical baselines and not demonstrated against the best classical solvers for the tested problems.

**Results summary:** The paper introduces Rasengan, a transition Hamiltonian-based variational quantum algorithm for constrained binary optimization problems in financial services and other domains. Rasengan outperforms state-of-the-art QAOA (Choco-Q) and hardware-efficient ansatz (HEA) methods in both accuracy (4.12× improvement) and circuit depth (1.96×–49× reduction). Key innovations include exponential exploration of feasible solution spaces, Hamiltonian simplification/pruning, segmented execution, and error mitigation via purification. On real quantum hardware (IBM Kyiv/Brisbane), Rasengan achieves a 379× improvement in solution quality and is the first quantum algorithm to surpass feasible solution baselines. However, quantum advantage claims remain speculative as the paper does not compare against optimized classical solvers.

**Performance claims:**
- 4.12× accuracy improvement over Choco-Q (QAOA) on 2000 cases across five domains
- 379× improvement in solution quality on real quantum hardware (IBM platforms)
- 1.96×–49× reduction in circuit depth compared to prior VQAs
- 94.6% reduction in circuit depth via Hamiltonian simplification/pruning
- 303× accuracy improvement via error mitigation on noisy hardware
- 100% in-constraints rate (feasible solutions) on real hardware
- ARG as low as 0.01 for small-scale problems (e.g., facility location with 6 qubits)
## Quantum advantage claim
**Classification:** speculative

The paper claims quantum advantage based on superior performance over other VQAs and classical baselines on real hardware. However, the advantage is speculative because: (1) results are not compared against the best classical solvers for the tested problems, (2) the demonstrated improvements are relative to other quantum algorithms (not absolute speedups), and (3) the hardware used (IBM NISQ devices) is error-prone, limiting generalizability to fault-tolerant quantum computing.
## Limitations
- Experiments conducted on noise-free simulators and small-scale real quantum devices (IBM Kyiv and Brisbane), limiting assessment of performance on larger, noisier hardware [inferred]
- Evaluation limited to 20 benchmarks across five problem domains (FLP, KPP, JSP, SCP, GCP), which may not generalize to all constrained binary optimization problems [inferred]
- Maximum problem size tested is 105 variables (qubits), which may not reflect scalability to industrial-scale financial optimization problems [inferred]
- Initialization of feasible solutions for some problems (e.g., graph coloring) may require linear time, which could be a bottleneck for very large instances [inferred]
- Hamiltonian simplification and pruning techniques reduce circuit depth but introduce offline preprocessing overhead (O(m²n) complexity) [inferred]
- Segmented execution strategy assumes probability preservation between segments, which may not hold under high noise levels [inferred]
- Error mitigation via purification relies on classical post-processing, which may not scale efficiently for very large solution spaces [inferred]
- Comparison with classical solvers is not provided, leaving the quantum advantage unclear [inferred]
- Conference paper page limits may have constrained detailed discussion of certain optimizations or failure cases [inferred]
- Theoretical upper bound of m³ transition Hamiltonian simulations for non-totally unimodular matrices may limit practical applicability for some problem types
- Performance on real hardware (IBM devices) shows significant degradation compared to noise-free simulations, highlighting sensitivity to noise
## Open questions
- How does Rasengan perform on problem instances with non-linear constraints, which are common in financial services?
- What is the impact of different noise profiles (e.g., gate errors, decoherence) on the segmented execution strategy?
- Can the Hamiltonian simplification algorithm be optimized further to reduce preprocessing time for very large problems?
- How does the algorithm handle problems where the feasible solution space is extremely sparse relative to the total search space?
- What are the trade-offs between segment size, shot allocation, and solution quality in segmented execution?
- How does Rasengan compare to state-of-the-art classical solvers (e.g., CPLEX, Gurobi) in terms of solution quality and runtime for large-scale problems?
- Can the transition Hamiltonian approach be extended to handle continuous or mixed-integer optimization problems?
- What is the minimum qubit coherence time required for Rasengan to outperform classical methods on real hardware?

**Future work:**
- Extend Rasengan to handle non-linear constraints and mixed-integer optimization problems
- Develop adaptive noise mitigation techniques tailored to the segmented execution strategy
- Optimize the Hamiltonian simplification algorithm to reduce preprocessing overhead for large-scale problems
- Conduct comparative studies with state-of-the-art classical solvers to quantify quantum advantage
- Explore hybrid quantum-classical approaches that combine Rasengan with classical optimization techniques
- Test Rasengan on larger quantum processors (e.g., 433-qubit IBM Osprey or 1121-qubit IBM Condor) to assess scalability
- Investigate the use of Rasengan for dynamic optimization problems in financial services, such as real-time portfolio rebalancing
- Develop techniques to reduce the number of parameters in Rasengan without sacrificing solution quality
- Apply Rasengan to other NP-hard problems in financial services, such as credit risk assessment or fraud detection
- Explore the integration of Rasengan with quantum machine learning models for enhanced optimization capabilities
## Key ideas
- #idea:quantum-advantage — Rasengan achieves 4.12× accuracy improvement over QAOA (Choco-Q) for constrained binary optimization problems, with exponential exploration of feasible solution spaces via transition Hamiltonians
- #idea:near-term-feasibility — Algorithm-hardware co-design optimizations (Hamiltonian simplification, segmented execution, error mitigation) reduce circuit depth by 94.6% for NISQ deployability
- #idea:hybrid-approach — Classical preprocessing (feasible solution initialization) and quantum execution (transition Hamiltonian) form a hybrid pipeline for constrained optimization
- #limitation:qubit-count — Experiments limited to 28-qubit problems; scalability to larger financial problems (e.g., portfolio optimization with >100 assets) untested
- #limitation:noise — Performance on real hardware (IBM Kyiv/Brisbane) degrades significantly compared to noise-free simulations, highlighting sensitivity to noise
- #limitation:data-encoding — Homogeneous basis reconstruction has O(m²n) complexity, potentially limiting scalability for high-dimensional financial problems
- #limitation:no-empirical-validation — Quantum advantage claims are speculative as Rasengan is not compared against state-of-the-art classical solvers (e.g., CPLEX, Gurobi)
## Contradictions
- #contradiction:classical-vs-quantum — The paper claims quantum advantage on real hardware, but this is disputed as the results are not benchmarked against the best classical solvers for the tested problems (e.g., facility location, job scheduling).
- #contradiction:scalability — The paper speculates Rasengan may scale to 100+ qubits, but experiments are limited to 28 qubits, and no evidence is provided for scalability to industrial-scale financial problems (e.g., large portfolio optimization or risk modeling).
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
