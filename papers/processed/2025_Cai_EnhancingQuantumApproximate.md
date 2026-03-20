---
aliases:
- Enhancing quantum approximate optimization with CNN-CVaR integration
- Enhancing quantum approximate optimization
authors:
- Pengnian Cai
- Kang Shen
- Tao Yang
- Yuanming Hu
- Bin Lv
- Liuhuan Fan
- Zeyu Liu
- Qi Hu
- Shixian Chen
- Yunlai Zhu
- Zuheng Wu
- Yuehua Dai
- Fei Yang
- Jun Wang
- Zuyu Xu
auto_detected: true
classification: ''
contradiction_flags: []
doi: 10.1007/s11128-025-04655-3
evidence_type: ''
idea_tags:
- idea:quantum-advantage
- idea:near-term-feasibility
- idea:hybrid-approach
journal_or_venue: Quantum Information Processing
methodology_tags:
- QAOA
- quantum-ML
- variational
- classical-simulation
paper_type: ''
quantum_advantage_claim: theoretical
related_papers: []
relevance_phase1: high
relevance_phase3: medium
source_type: peer-reviewed-empirical
source_type_confidence: high
step1_date: '2026-03-20T00:11:54.503397'
step1_model: Mistral-Large-3
step2_date: '2026-03-20T00:11:58.145361'
step2_model: Mistral-Large-3
step3_date: '2026-03-20T00:12:08.784023'
step3_model: Mistral-Large-3
step4_date: '2026-03-20T00:12:17.761369'
step4_model: Mistral-Large-3
step5_date: '2026-03-20T00:12:27.611663'
step5_model: Mistral-Large-3
step6_date: '2026-03-20T00:12:30.175585'
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
- method/quantum-ML
- method/variational
- method/classical-simulation
- idea/quantum-advantage
- idea/near-term-feasibility
- idea/hybrid-approach
title: Enhancing quantum approximate optimization with CNN-CVaR integration
topic_tags:
- portfolio-optimisation
- risk-modelling
year: 2025
zotero_key: ''
---

## Abstract summary
This paper introduces a novel hybrid approach, CNN-CVaR-QAOA, that combines convolutional neural networks (CNNs) with conditional value at risk (CVaR) to enhance the performance of the quantum approximate optimization algorithm (QAOA). The study focuses on improving QAOA's ability to solve combinatorial optimization problems, such as Max-Cut, by leveraging CNNs for variational parameter optimization and CVaR to refine the objective function. The method is empirically validated on Erdos–Renyi random graphs, demonstrating improved approximation ratios and smoother optimization landscapes compared to traditional techniques.
## Methodology
The paper presents a novel combinatorial optimization strategy, CNN-CVaR-QAOA, which integrates a convolutional neural network (CNN) with conditional value at risk (CVaR) to optimize quantum approximate optimization algorithm (QAOA) circuits. The research focuses on solving the Max-Cut problem using Erdos-Renyi random graphs. The methodology involves replacing the traditional loss function in QAOA with CVaR to prioritize better outcomes and leveraging a CNN for variational quantum parameter optimization. The CNN model learns a mapping function from QAOA parameters of depth p to those of depth p+1, using a noiseless state vector simulator from the Qiskit platform. The study investigates the impact of the CVaR parameter (α) on algorithm performance, demonstrating that lower α values lead to smoother objective functions and improved approximation ratios.

**Algorithms used:** QAOA, CNN-CVaR-QAOA
**Frameworks:** Qiskit

**Experimental setup:** Experiments were conducted using the noiseless state vector simulator from the Qiskit platform. The quantum circuits were executed with 1024 measurements to ensure data adequacy and reliability. The CNN model architecture included up-sampling and down-sampling components with convolutional layers, ReLU activation functions, and the Adam optimizer for training.

**Dataset:** Erdos-Renyi random graphs generated using the Python NetworkX package for the Max-Cut problem. Graph configurations varied in size (6 to 22 nodes), node degrees (3 to 8), and edge probabilities (0.5 to 0.7).
## Findings
- [supported] CNN-CVaR-QAOA achieves superior approximation ratios compared to random initialization (RI-QAOA), interpolation (INTERP-QAOA), standalone CNN-QAOA, and standalone CVaR-QAOA on Erdos–Renyi random graphs with varying node sizes (6–16 qubits), degrees (3–8), and edge probabilities (0.5–0.7).
- [supported] CNN-CVaR-QAOA with α = 0.5 improves approximation ratios by 0.06–0.2 over competing methods at circuit depth p = 2.
- [supported] CNN-CVaR-QAOA converges to optimal solutions at shallower circuit depths (e.g., p = 3) compared to standalone CNN-QAOA or INTERP-QAOA (e.g., p = 7 for similar performance).
- [supported] Lower CVaR parameter α (e.g., 0.1) yields smoother objective functions and higher approximation ratios, with improvements of 4.0–13.7% over higher α values (0.3–1.0) on 10–16 node 3-regular graphs.
- [supported] CNN-CVaR-QAOA maintains a 93% approximation ratio on 22-qubit systems (3-regular graphs, p = 3), demonstrating scalability.
- [supported] The method generalizes to other combinatorial problems (e.g., exact cover), where lower α values (e.g., 0.01) enable convergence to optimal solutions.
- [supported] Results are derived from noiseless state vector simulations (Qiskit) with 1024 measurements per circuit, not real quantum hardware.
- [speculative] The authors suggest CNN-CVaR-QAOA could enhance QAOA optimization across diverse domains in the NISQ era, though empirical validation on real hardware is lacking.

**Results summary:** The paper empirically demonstrates that CNN-CVaR-QAOA, a hybrid quantum-classical algorithm integrating convolutional neural networks (CNNs) with conditional value at risk (CVaR), outperforms existing QAOA optimization methods (e.g., random initialization, interpolation, standalone CNN, and standalone CVaR) on Max-Cut problems using Erdos–Renyi random graphs. Key results include improved approximation ratios (0.06–0.2 higher than baselines), faster convergence at shallower circuit depths (e.g., p = 3 vs. p = 7 for competitors), and enhanced performance with lower CVaR α values (e.g., α = 0.1). The method scales to 22 qubits with a 93% approximation ratio and generalizes to other combinatorial problems (e.g., exact cover). All findings are based on noiseless simulations, with no validation on real quantum hardware.

**Performance claims:**
- Approximation ratio improvement of 0.06–0.2 over RI-QAOA, INTERP-QAOA, CNN-QAOA, and CVaR-QAOA (α = 0.5, p = 2).
- 4.0–13.7% higher approximation ratios with α = 0.1 vs. α = 0.3–1.0 on 10–16 node 3-regular graphs (p = 2).
- 93% approximation ratio on 22-qubit 3-regular graphs (p = 3).
- Convergence to optimal solutions at p = 3 (vs. p = 4 for CVaR-QAOA and p = 7 for CNN-QAOA/INTERP-QAOA) on 8–12 node graphs.
- Expectation value convergence to theoretical minimum (e.g., -7.0 for α = 0.1 vs. -5.886 for α = 1.0) on 14-node 3-regular graphs.
## Quantum advantage claim
**Classification:** theoretical

The paper claims theoretical advantages for CNN-CVaR-QAOA, including improved approximation ratios and shallower circuit depths, but all results are derived from noiseless simulations. No empirical demonstration of quantum advantage over classical methods or real hardware validation is provided, leaving claims of practical quantum advantage speculative.
## Limitations
- Experiments conducted using a noiseless state vector simulator (Qiskit), which does not account for hardware noise or decoherence [inferred]
- Limited to small-scale quantum systems (up to 22 qubits), which may not reflect performance on larger, more practical problems
- Experiments primarily focused on Max-Cut and exact cover problems; generalizability to other combinatorial optimization problems not fully explored [inferred]
- Dataset size constrained to Erdos–Renyi random graphs and small regular graphs, limiting the diversity of problem instances
- Performance evaluated using approximation ratio, but no direct comparison with state-of-the-art classical solvers (e.g., Goemans–Williamson algorithm) [inferred]
- CNN model training requires extensive pretraining on problem instances, which may not be feasible for all problem types or larger scales [inferred]
- CVaR parameter (α) tuning is critical; suboptimal α values may degrade performance, and optimal α may vary across problem instances
- Scalability to production-level problems (e.g., >50 qubits) not demonstrated due to computational overhead and circuit depth constraints
- Reproducibility may be limited by the stochastic nature of the QN-SPSA optimizer and random initialization of parameters
- No noise mitigation techniques applied, which could affect performance on real quantum hardware [inferred]
- Circuit depth limited to p=10 layers, which may not be sufficient for achieving quantum advantage in more complex problems [inferred]
## Open questions
- How does the CNN-CVaR-QAOA method perform on real quantum hardware with noise and decoherence?
- What is the impact of hardware noise on the approximation ratio and convergence of the algorithm?
- Can the method be extended to larger-scale problems (e.g., >50 qubits) without significant performance degradation?
- How does the performance of CNN-CVaR-QAOA compare to state-of-the-art classical solvers for Max-Cut and other combinatorial problems?
- What is the optimal CVaR parameter (α) for different problem types and sizes, and can it be dynamically adjusted?
- How does the method generalize to other combinatorial optimization problems beyond Max-Cut and exact cover?
- What are the computational trade-offs between circuit depth, qubit count, and approximation ratio for larger problem instances?
- Can the CNN model be trained more efficiently to reduce the overhead of pretraining on large datasets?

**Future work:**
- Test the CNN-CVaR-QAOA method on real quantum hardware (e.g., IBM Eagle or Rigetti processors) to evaluate noise resilience
- Extend the method to larger-scale problems (e.g., >50 qubits) and assess scalability
- Compare the performance of CNN-CVaR-QAOA with state-of-the-art classical solvers for Max-Cut and other combinatorial problems
- Explore dynamic tuning of the CVaR parameter (α) to optimize performance across different problem instances
- Apply the method to a broader range of combinatorial optimization problems (e.g., traveling salesman, graph coloring)
- Investigate hybrid quantum-classical approaches to reduce the computational overhead of CNN training and parameter prediction
- Develop noise mitigation techniques to improve performance on NISQ-era devices
- Evaluate the impact of circuit depth on approximation ratio and convergence for deeper QAOA circuits (p > 10)
- Assess the reproducibility of results across different quantum hardware platforms and simulators
## Key ideas
- #idea:hybrid-approach — CNN-CVaR-QAOA integrates convolutional neural networks (CNNs) with CVaR to optimize QAOA parameters, reducing circuit depth requirements for combinatorial problems like Max-Cut, with potential applicability to portfolio optimization and risk modelling
- #idea:quantum-advantage — CNN-CVaR-QAOA achieves higher approximation ratios (0.06–0.2 improvement) and faster convergence at shallower circuit depths (p=3 vs. p=7) compared to baseline methods, suggesting potential quantum advantage for combinatorial optimization in finance
- #idea:near-term-feasibility — The method demonstrates improved performance on near-term quantum simulators (up to 22 qubits), though scalability and real-world financial applicability remain untested
- #limitation:noise — Performance evaluated only on noiseless state vector simulators; real quantum hardware effects (e.g., noise, decoherence) not assessed, limiting claims of near-term feasibility
- #limitation:qubit-count — Experiments limited to 22 qubits, constraining direct applicability to larger financial optimization problems (e.g., large-scale portfolio optimization)
- #limitation:data-encoding — Reliance on synthetic Erdos–Renyi graphs; performance on real-world financial datasets (e.g., portfolio optimization, risk modelling) not demonstrated, reducing practical relevance
## Contradictions
<!-- Step 6 output — where this paper contradicts others -->

## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->

## Experiment details
### Input
{'source': 'Erdos-Renyi random graphs generated using Python NetworkX package', 'size': 'Graphs with 6 to 22 nodes (qubits)', 'features': 'Node degrees ranging from 3 to 8, edge probabilities from 0.5 to 0.7', 'preprocessing_steps': 'Graphs encoded into problem Hamiltonians for Max-Cut, parameters initialized using QN-SPSA optimizer'}

### Process
1. Encode Max-Cut problem into a Hamiltonian. 2. Initialize QAOA parameters using QN-SPSA optimizer for depth p=1. 3. Use CNN to predict parameters for depth p+1. 4. Apply CVaR optimization with varying α values (0.1 to 1) to replace the objective function. 5. Execute quantum circuits with 1024 shots per evaluation. 6. Train CNN using Adam optimizer with a learning rate of 0.0001 over 50 epochs, using mean squared error (MSE) as the loss function.

### Output
{'metrics_reported': ['Approximation ratio', 'Expectation value of the circuit'], 'comparison_baselines': ['Random initialization (RI-QAOA)', 'Interpolation (INTERP-QAOA)', 'CNN-QAOA', 'CVaR-QAOA'], 'output_format': 'Visualization of approximation ratios and expectation values across different graph configurations and circuit depths'}

### Parameters
- qubit_count: 6 to 22 qubits
- circuit_depth: 2 to 10 layers
- shots: 1024
- optimizer: Adam (learning rate: 0.0001), QN-SPSA for initialization
- CVaR_alpha_values: [0.1, 0.3, 0.5, 0.8, 1]
- batch_size: 6
- epochs: 50
- loss_function: Mean squared error (MSE)

### Hardware
{'simulator': 'Qiskit Aer statevector simulator (noiseless)', 'QPU_model': 'Not applicable (simulator used)', 'transpilation_settings': 'Not specified'}

### Reproducibility
Code and dataset generation methodology described in detail. Data generated using NetworkX package, which is publicly available. Sufficient detail provided to replicate experiments, though no explicit mention of code availability.
