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
  '25)
methodology_tags:
- variational
- QAOA
- VQE
- quantum-annealing
- QUBO
paper_type: ''
quantum_advantage_claim: theoretical
related_papers: []
relevance_phase1: high
relevance_phase3: high
source_type: conference-paper
source_type_confidence: high
step1_date: '2026-03-20T00:29:20.569861'
step1_model: Mistral-Large-3
step2_date: '2026-03-20T00:29:24.214426'
step2_model: Mistral-Large-3
step3_date: '2026-03-20T00:29:36.563889'
step3_model: Mistral-Large-3
step4_date: '2026-03-20T00:30:27.509332'
step4_model: Mistral-Large-3
step5_date: '2026-03-20T00:30:37.542891'
step5_model: Mistral-Large-3
step6_date: '2026-03-20T00:30:45.458242'
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
- method/VQE
- method/quantum-annealing
- method/QUBO
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
This paper introduces Rasengan, a novel variational quantum algorithm designed to solve constrained binary optimization problems with high precision and low circuit complexity. Unlike traditional methods that shrink the search space from a superposition of all possible solutions, Rasengan expands the feasible solution space from a single feasible solution using a transition Hamiltonian. This approach ensures that the algorithm remains within the feasible solution space while exponentially exploring all valid solutions, improving accuracy and deployability on near-term quantum devices.
## Methodology
The paper introduces Rasengan, a novel variational quantum algorithm designed to solve constrained binary optimization problems. The core methodology involves an expansion-based approach using a transition Hamiltonian, which starts from a single feasible solution and exponentially explores the entire feasible solution space via homogeneous basis vectors. This contrasts with traditional variational quantum algorithms (VQAs) that shrink the search space from a superposition of all possible states. The transition Hamiltonian is formulated to ensure that quantum state evolution remains within the feasible solution space, leveraging quantum parallelism for efficient exploration. The paper also proposes three optimization techniques to enhance deployability on noisy quantum hardware: Hamiltonian simplification and pruning to reduce circuit complexity, segmented execution to manage circuit depth, and solution purification for error mitigation. The algorithm is evaluated on both simulators and real quantum devices, demonstrating significant improvements in accuracy and latency over existing VQAs like QAOA and HEA.

**Algorithms used:** QAOA, VQE

**Experimental setup:** Experiments were conducted using both noise-free simulators (DDSim) and real quantum devices (IBM Kyiv and Brisbane). The classical optimization part was executed on an AMD EPYC 9554 64-core server with 1TB RAM, while quantum simulations were accelerated using DDSim for Rasengan and CUDA-quantum for QAOA/HEA on an A100 GPU. The evaluation covered five problem domains: facility location, k-partition, job scheduling, set cover, and graph coloring problems, with 400 cases compiled for each domain.

**Dataset:** The paper evaluates Rasengan on synthetic and real-world benchmarks from five problem domains: facility location problem (FLP), k-partition problem (KPP), job scheduling problem (JSP), set cover problem (SCP), and graph coloring problem (GCP). Each domain includes 400 cases with varying numbers of variables (qubits) and constraints, as detailed in Table 2 of the paper.
## Findings
- [supported] Rasengan improves accuracy by 4.12× compared to state-of-the-art QAOA (Choco-Q) on constrained binary optimization problems across 2000 cases from five domains (facility location, k-partition, job scheduling, set covering, and graph coloring).
- [supported] Rasengan reduces circuit depth by 1.96× compared to prior variational quantum algorithms (VQAs) in noise-free simulations.
- [supported] On real-world quantum hardware (IBM Kyiv and Brisbane), Rasengan achieves a 379× improvement in solution quality over the mean quality of feasible solution baselines, marking the first quantum algorithm to outperform this baseline.
- [supported] Rasengan’s Hamiltonian simplification and pruning techniques reduce circuit depth by over 94.6%, making it deployable on current NISQ devices (e.g., reducing depth from ~7000 to ~50 for a 24-variable graph coloring problem).
- [supported] Rasengan’s error mitigation technique improves accuracy by more than 303× on noisy hardware by purifying infeasible solutions after each segment.
- [supported] Rasengan achieves lower approximation ratio gaps (ARG) than HEA, penalty-term-based QAOA (P-QAOA), and commute-Hamiltonian-based QAOA (Choco-Q) across all tested benchmarks, with ARG values as low as 0.01 for small-scale problems.
- [supported] Rasengan’s segmented execution strategy partitions transition Hamiltonians into segments with depths as low as 34n (where n is the number of qubits), enabling execution on NISQ devices while preserving solution quality.
- [speculative] Rasengan’s transition Hamiltonian approach could theoretically scale to larger problem sizes (e.g., 100+ qubits) due to its polynomial circuit depth complexity (O(nm²), where m is the number of homogeneous basis vectors).
- [speculative] The authors claim that Rasengan’s expansion-based methodology avoids the expressivity limits of traditional VQAs, which are prone to trapping in suboptimal solutions due to their shrinking search space approach.
- [disputed] The paper claims Rasengan is the first quantum algorithm to beat the mean quality of feasible solution baseline on real hardware, but this may depend on the specific baseline definition and problem instances used.

**Results summary:** The paper introduces Rasengan, a novel variational quantum algorithm for constrained binary optimization problems, which leverages a transition Hamiltonian to exponentially explore the feasible solution space from an initial feasible solution. Unlike traditional VQAs that shrink the search space from a superposition of all states, Rasengan expands the space while ensuring all generated solutions remain feasible. The algorithm demonstrates significant improvements in accuracy (4.12× over Choco-Q) and circuit depth (1.96× reduction) in noise-free simulations across 2000 cases from five domains. On real quantum hardware, Rasengan achieves a 379× improvement in solution quality over baseline methods, with circuit depth reductions of over 94.6% through Hamiltonian simplification, pruning, and segmented execution. Error mitigation techniques further enhance accuracy by 303× on noisy devices. Rasengan’s polynomial circuit depth complexity and deployability on NISQ devices position it as a promising approach for practical quantum optimization.

**Performance claims:**
- 4.12× improvement in accuracy over Choco-Q (state-of-the-art QAOA) across 2000 cases
- 1.96× reduction in circuit depth compared to prior VQAs
- 379× improvement in solution quality on real quantum hardware (IBM Kyiv/Brisbane)
- 94.6% reduction in circuit depth via Hamiltonian simplification and pruning
- 303× improvement in accuracy on noisy hardware via error mitigation
- ARG as low as 0.01 for small-scale problems (e.g., facility location with 6 variables)
- Circuit depth reduced from ~7000 to ~50 for a 24-variable graph coloring problem
- Segmented execution with depths as low as 34n (n = number of qubits)
## Quantum advantage claim
**Classification:** theoretical

Rasengan demonstrates a theoretical quantum advantage through its transition Hamiltonian approach, which exponentially explores the feasible solution space with polynomial circuit depth (O(nm²)). While the paper provides empirical results from simulations and real hardware showing superior accuracy and circuit efficiency compared to classical and quantum baselines, the claimed advantage is not yet demonstrated at scale (e.g., 100+ qubits) or for problems where classical methods are intractable. The advantage is supported by algorithmic design and small-scale empirical results but remains theoretical for larger problem instances.
## Limitations
- Experiments conducted on noise-free simulators and small-scale real quantum hardware (IBM Kyiv and Brisbane), limiting assessment of performance under realistic NISQ conditions [inferred]
- Circuit depth reduction techniques (e.g., Hamiltonian simplification and pruning) may not generalize equally well across all problem types, particularly those with complex constraint topologies
- Scalability analysis limited to facility location problems (FLP); performance on other benchmarks (e.g., graph coloring) may vary due to differing constraint structures [inferred]
- Segmented execution strategy assumes probability preservation across segments, which may degrade under high noise levels or deep circuits [inferred]
- Error mitigation via purification introduces classical overhead, though minimal, which could become significant for very large problem sizes [inferred]
- Maximum evaluated problem size (105 variables) may not reflect performance on industrial-scale financial optimization problems (e.g., portfolio optimization with thousands of assets) [inferred]
- Comparison with classical solvers (e.g., state-of-the-art heuristics or exact methods) is missing, leaving quantum advantage unclear [inferred]
- Conference paper page limits may have constrained detailed discussion of failure cases or edge conditions [inferred]
- Theoretical upper bound of m³ transition Hamiltonians for non-unimodular matrices may lead to impractical circuit depths for certain problems [inferred]
- Initialization complexity for feasible solutions varies by problem type (e.g., O(d) for FLP vs. O(g) for GCP), potentially limiting applicability to problems with hard-to-find feasible solutions [inferred]
## Open questions
- How does Rasengan perform on financial optimization problems with non-linear constraints (e.g., risk parity portfolios)?
- What is the impact of different noise models (e.g., amplitude damping, phase flip) on solution quality across problem domains?
- Can the segmented execution strategy be optimized further to minimize probability distortion in high-noise environments?
- How does the algorithm scale when the number of homogeneous basis vectors grows exponentially with problem size?
- What are the trade-offs between circuit depth, shot count, and solution quality in real-world deployment?
- How does Rasengan compare to hybrid quantum-classical approaches (e.g., QAOA with warm-start initialization) for large-scale problems?
- What is the minimal qubit coherence time required for Rasengan to outperform classical methods on industrially relevant problems?
- How sensitive is the algorithm to the choice of initial feasible solution, and can this be automated for arbitrary problems?

**Future work:**
- Extend Rasengan to handle non-linear constraints and mixed-integer optimization problems relevant to finance
- Evaluate performance on larger-scale quantum hardware (e.g., IBM Heron or future error-corrected devices)
- Develop adaptive segmented execution strategies that dynamically adjust segment size based on real-time noise characterization
- Integrate Rasengan with classical optimization techniques (e.g., branch-and-bound) to create hybrid solvers for industrial-scale problems
- Explore automated methods for generating initial feasible solutions across diverse problem domains
- Conduct comparative studies with state-of-the-art classical solvers to quantify quantum advantage
- Investigate the use of machine learning to optimize Hamiltonian simplification and pruning for specific problem classes
- Apply Rasengan to real-world financial datasets (e.g., portfolio optimization, option pricing) and benchmark against industry standards
- Develop error mitigation techniques tailored to the transition Hamiltonian framework to improve robustness on NISQ devices
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

## Experiment details
### Input
{'source': 'Synthetic benchmarks compiled from relevant literature for each problem domain (FLP, KPP, JSP, SCP, GCP).', 'size': '400 cases per problem domain, with variable counts ranging from 6 to 105 qubits and constraints ranging from 3 to 15.', 'preprocessing_steps': 'Feasible solutions were pre-calculated for initialization. Homogeneous basis vectors were derived from linear constraints, and redundant transition Hamiltonians were pruned. Input states were normalized and encoded as qubit rotations for quantum circuits.', 'features': 'Binary decision variables (0 or 1) with linear equality or inequality constraints transformed into equality constraints using auxiliary variables.'}

### Process
1. Initialize the quantum circuit with an arbitrary feasible solution. 2. Apply transition Hamiltonian simulations sequentially to expand the feasible solution space. 3. Optimize the evolution time parameters using a classical optimizer (COBYLA). 4. Partition the sequence of transition Hamiltonians into segments and execute each segment individually, preserving probability distributions. 5. Apply error mitigation by purifying noisy solutions after each segment. 6. Repeat until convergence or maximum iterations (300 for small-scale, 1000 for large-scale problems). 7. Measure the final quantum state to obtain the optimal feasible solution.

### Output
The primary output metrics include the approximation ratio gap (ARG), in-constraints rate, and latency. ARG measures the gap between the algorithm's solution and the optimal solution, with lower values indicating better performance. The in-constraints rate evaluates the probability that output solutions satisfy the constraints. Latency includes compilation time, circuit execution time, and parameter updating time. Rasengan's performance was compared against HEA, penalty-term-based QAOA (P-QAOA), and commute-Hamiltonian-based QAOA (Choco-Q).

### Parameters
- qubits: Ranged from 6 to 105 depending on the problem scale.
- circuit_depth: Varied from 22 to 102 for Rasengan after optimization, compared to 46 to 3848 for baselines.
- shots: 1024 shots per segment for segmented execution, dynamically adjusted based on probability distributions.
- optimizer: COBYLA (Constrained Optimization by Linear Approximation).
- convergence_threshold: Maximum iterations set to 300 for small-scale and 1000 for large-scale problems.
- hyperparameters: {'evolution_time': 'Tuned by the classical optimizer for each transition Hamiltonian.', 'segments': 'Number of segments dynamically determined based on circuit depth and problem size.', 'penalty_coefficient': 'Not applicable (Rasengan does not use penalty terms).'}

### Hardware
{'simulator': 'DDSim for Rasengan, CUDA-quantum for QAOA/HEA.', 'QPU_model': 'IBM Kyiv and Brisbane (127-qubit Eagle r3).', 'cloud_provider': 'IBM Quantum.', 'transpilation_settings': 'Circuits were transpiled to match the hardware topology of IBM devices, with error rates calibrated from device data (e.g., two-qubit gate error rate of 0.82% for Brisbane).'}

### Reproducibility
Code for Rasengan is publicly available on GitHub (https://github.com/JanusQ/rasengan). The paper provides sufficient detail on the algorithm design, optimization techniques, and experimental setup to replicate the results. Benchmark datasets are synthetic but derived from standard problem formulations in the literature, ensuring reproducibility.
