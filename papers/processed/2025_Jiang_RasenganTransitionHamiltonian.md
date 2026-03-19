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
contradiction_flags: []
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
paper_type: ''
quantum_advantage_claim: theoretical
related_papers: []
relevance_phase1: high
relevance_phase3: high
source_type: conference-paper
source_type_confidence: high
step1_date: '2026-03-18T23:34:16.485550'
step1_model: Mistral-Large-3
step2_date: '2026-03-18T23:34:20.229516'
step2_model: Mistral-Large-3
step3_date: '2026-03-18T23:34:23.946852'
step3_model: Mistral-Large-3
step4_date: '2026-03-18T23:34:29.890350'
step4_model: Mistral-Large-3
step5_date: '2026-03-18T23:34:35.524311'
step5_model: Mistral-Large-3
step6_date: '2026-03-18T23:34:41.354014'
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
- idea/quantum-advantage
- idea/near-term-feasibility
- idea/hybrid-approach
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
This paper introduces Rasengan, a novel variational quantum algorithm designed to solve constrained binary optimization problems, which are prevalent in finance, engineering, and scheduling. The approach leverages a transition Hamiltonian to expand the search space from a feasible solution, ensuring high precision and low circuit complexity. The authors propose algorithm-hardware co-design optimizations to enhance deployability on noisy quantum devices, addressing key limitations of existing variational quantum algorithms.
## Methodology
The paper introduces Rasengan, a novel variational quantum algorithm designed to solve constrained binary optimization problems, which are prevalent in financial services and other domains. The methodology leverages a transition Hamiltonian to exponentially explore the feasible solution space starting from an arbitrary feasible solution, rather than shrinking the entire solution space as in traditional variational quantum algorithms (VQAs) like QAOA and HEA. The transition Hamiltonian is formulated to ensure that the quantum state evolution remains confined to feasible solutions by utilizing homogeneous basis vectors derived from linear algebra. The algorithm incorporates three key optimization techniques to enhance deployability on noisy quantum hardware: (1) Hamiltonian simplification and pruning to reduce circuit complexity, (2) segmented execution to partition and individually execute sequences of transition Hamiltonians, and (3) solution purification for error mitigation by removing infeasible solutions after each segment. The approach is evaluated through rigorous experiments on both simulators and real-world quantum devices, demonstrating significant improvements in accuracy and latency compared to state-of-the-art methods.

**Algorithms used:** Transition Hamiltonian-based Approximation, QAOA, HEA
**Frameworks:** Qiskit

**Experimental setup:** Experiments were conducted using both noise-free simulators and real-world quantum platforms, specifically IBM Quantum devices. The evaluation involved a 12-qubit noise-free simulator for benchmarking against prior VQA designs and real quantum hardware for testing deployability and accuracy under noise. The circuit depth was reduced from approximately 7000 to 50 to ensure compatibility with current quantum devices. The experimental setup included segmented execution of transition Hamiltonians and error mitigation techniques to purify noisy solutions.

**Dataset:** The paper evaluates the algorithm on 2000 cases from five domains, including the set covering problem as a representative constrained binary optimization problem. Specific financial datasets are not explicitly mentioned, but the methodology is applicable to financial investment problems and other constrained optimization tasks in financial services.
## Findings
- [supported] Rasengan improves accuracy by 4.12× compared to the state-of-the-art QAOA on constrained binary optimization problems, as demonstrated across 2000 cases from five domains using a noise-free simulator
- [supported] Rasengan achieves a 379× improvement in solution quality over prior quantum algorithms on real-world quantum hardware, being the first to surpass the mean quality of feasible solution baseline
- [supported] Rasengan reduces circuit depth by 1.96× compared to prior works at the algorithmic level and by over 94.6% through Hamiltonian simplification, pruning, and segmented execution techniques
- [supported] The transition Hamiltonian approach exponentially explores the entire feasible solution space from a single feasible solution, ensuring all combinations of homogeneous basis vectors are covered
- [supported] Hamiltonian simplification and pruning techniques reduce the number of nonzero elements in homogeneous basis vectors, lowering circuit complexity from ~7000 to ~50 depth for deployability on NISQ devices
- [supported] Segmented execution strategy partitions transition Hamiltonians into segments, reducing circuit depth to ~50 and enabling execution on current quantum platforms
- [supported] Error mitigation technique improves solution accuracy by more than 303× by purifying noisy outputs after each segment
- [speculative] Rasengan’s transition Hamiltonian-based approach may offer a general solution for constrained binary optimization problems beyond the tested domains, including financial services
- [speculative] The polynomial circuit depth cost (upper bound of 34nm² CX gates) suggests Rasengan could scale to larger problem sizes with improved quantum hardware

**Results summary:** The paper introduces Rasengan, a novel variational quantum algorithm for constrained binary optimization problems, leveraging a transition Hamiltonian to exponentially explore the feasible solution space from a single feasible solution. Experimental results demonstrate significant improvements over prior methods, including a 4.12× accuracy gain and 1.96× circuit depth reduction in simulations, and a 379× solution quality improvement on real quantum hardware. The algorithm incorporates three key optimizations—Hamiltonian simplification and pruning, segmented execution, and error mitigation—to achieve deployability on NISQ devices, reducing circuit depth by over 94.6% and improving accuracy by more than 303×. Rasengan is the first quantum algorithm to outperform the mean quality of feasible solutions in real-world tests.

**Performance claims:**
- 4.12× accuracy improvement over SOTA QAOA in simulations
- 379× solution quality improvement on real quantum hardware
- 1.96× circuit depth reduction at the algorithmic level
- Over 94.6% reduction in circuit depth through optimizations
- More than 303× accuracy improvement via error mitigation
- Circuit depth reduced from ~7000 to ~50 for NISQ deployability
- Approximation ratio gap (ARG) of 0.70 compared to ~1000 for penalty-term-based QAOA
## Quantum advantage claim
**Classification:** theoretical

The quantum advantage is claimed based on the exponential exploration of the feasible solution space via transition Hamiltonians, which is theoretically more efficient than classical exhaustive search. However, while results are demonstrated on both simulators and real hardware, the advantage is not explicitly quantified in terms of speedup or resource efficiency over classical methods for the same problem size. The advantage remains theoretical due to the lack of direct comparison with state-of-the-art classical solvers on large-scale problems.
## Limitations
- Experiments conducted on a 12-qubit noise-free simulator, which may not reflect performance on real noisy quantum hardware [inferred]
- Algorithm tested only on the set covering problem; generalizability to other constrained binary optimization problems in finance (e.g., portfolio optimization) is not demonstrated
- Circuit depth reduction techniques (e.g., Hamiltonian simplification) may not preserve solution quality under all noise conditions [inferred]
- Page-limit constraints of the conference paper may have omitted detailed analysis of failure cases or edge conditions [inferred]
- Performance improvements (4.12× accuracy, 379× on real hardware) are relative to prior VQAs (e.g., QAOA), but no direct comparison with state-of-the-art classical solvers is provided
- Theoretical upper bound of m³ for transition Hamiltonian simulations may still be impractical for large-scale financial problems [inferred]
- Error mitigation technique (solution purification) assumes noise patterns are predictable, which may not hold for all quantum devices [inferred]
- Initialization requires a pre-calculated feasible solution, which may be non-trivial for complex financial constraints [inferred]
- Latency measurements exclude data communication time, which could dominate in real-world financial applications [inferred]
- Homogeneous basis reconstruction (Algorithm 1) has O(m²n) complexity, potentially limiting scalability for high-dimensional problems
## Open questions
- How does Rasengan perform on real-world financial datasets (e.g., portfolio optimization with >20 assets) compared to classical methods?
- What is the impact of decoherence and gate errors on the transition Hamiltonian’s ability to maintain feasible solution spaces?
- Can the segmented execution strategy be optimized further to reduce circuit depth without sacrificing accuracy?
- How sensitive is the algorithm to the choice of initial feasible solution, and does this affect convergence to the global optimum?
- What are the trade-offs between circuit depth, accuracy, and problem size for financial applications beyond the set covering problem?
- How does Rasengan compare to hybrid quantum-classical approaches (e.g., QAOA with warm-start) for constrained optimization?
- What noise thresholds (e.g., gate error rates) make Rasengan’s error mitigation techniques ineffective?

**Future work:**
- Extend Rasengan to multi-period portfolio optimization and other dynamic financial problems
- Test on larger-scale quantum hardware (e.g., IBM Heron or Google Sycamore processors) with >50 qubits
- Develop adaptive error mitigation techniques tailored to specific quantum hardware noise profiles
- Compare Rasengan’s performance with state-of-the-art classical solvers (e.g., Gurobi, CPLEX) on real financial datasets
- Explore hybrid quantum-classical approaches to reduce reliance on pre-calculated feasible solutions
- Investigate the use of Rasengan for other NP-hard problems in finance (e.g., option pricing, risk analysis)
- Optimize the homogeneous basis reconstruction algorithm to reduce computational overhead for large problems
- Integrate Rasengan with quantum machine learning frameworks for financial forecasting
## Key ideas
- #idea:quantum-advantage — Rasengan achieves 4.12× accuracy improvement over QAOA for constrained binary optimization problems, with exponential exploration of feasible solution spaces via transition Hamiltonians
- #idea:near-term-feasibility — Algorithm-hardware co-design optimizations (Hamiltonian simplification, segmented execution, error mitigation) reduce circuit depth by 94.6% for NISQ deployability
- #idea:hybrid-approach — Classical preprocessing (feasible solution initialization) and quantum execution (transition Hamiltonian) form a hybrid pipeline for constrained optimization
- #limitation:qubit-count — Experiments limited to 12-qubit simulators; scalability to larger financial problems (e.g., portfolio optimization with >20 assets) untested
- #limitation:noise — Error mitigation assumes predictable noise patterns, which may not hold across all quantum devices
- #limitation:data-encoding — Homogeneous basis reconstruction has O(m²n) complexity, potentially limiting scalability for high-dimensional financial problems
## Contradictions
<!-- Step 6 output — where this paper contradicts others -->

## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
