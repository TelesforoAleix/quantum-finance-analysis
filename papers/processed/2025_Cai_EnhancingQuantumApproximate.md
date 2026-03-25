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
contradiction_flags:
- contradiction:classical-vs-quantum
- contradiction:scalability
doi: 10.1007/s11128-025-04655-3
evidence_type: ''
idea_tags:
- idea:near-term-feasibility
- idea:hybrid-approach
- idea:quantum-advantage
journal_or_venue: Quantum Information Processing
methodology_tags:
- QAOA
- quantum-ML
- variational
- classical-simulation
paper_type: ''
quantum_advantage_claim: speculative
related_papers: []
relevance_phase1: low
relevance_phase3: low
source_type: peer-reviewed-empirical
source_type_confidence: high
step1_date: '2026-03-25T16:07:34.522591'
step1_model: gpt-5.1
step2_date: '2026-03-25T16:07:45.865751'
step2_model: gpt-5.1
step3_date: '2026-03-25T16:08:09.506468'
step3_model: gpt-5.4
step4_date: '2026-03-25T16:08:54.163126'
step4_model: gpt-5.4
step5_date: '2026-03-25T16:09:31.233004'
step5_model: gpt-5.4
step6_date: '2026-03-25T16:09:43.183328'
step6_model: gpt-5.4
steps_completed:
- 1
- 2
- 3
- 4
- 5
- 6
tags:
- method/QAOA
- method/quantum-ML
- method/variational
- method/classical-simulation
- idea/near-term-feasibility
- idea/hybrid-approach
- idea/quantum-advantage
- contradiction/classical-vs-quantum
- contradiction/scalability
title: Enhancing quantum approximate optimization with CNN-CVaR integration
topic_tags: []
year: 2025
zotero_key: ''
---

## Abstract summary
The paper proposes CNN-CVaR-QAOA, a variant of the Quantum Approximate Optimization Algorithm that combines a convolutional neural network for parameter prediction with a Conditional Value at Risk-based objective function. Using simulations on Erdos–Renyi and regular graphs for Max-Cut and an exact cover problem, the authors show that this approach can achieve higher approximation ratios and reach near-optimal solutions at lower circuit depths than standard QAOA initialization and optimization schemes, with performance strongly influenced by the choice of the CVaR parameter α.
## Methodology
The paper presents an empirical evaluation of a hybrid quantum-classical optimization method called CNN-CVaR-QAOA for combinatorial optimization, primarily the Max-Cut problem. The approach combines QAOA with a convolutional neural network that predicts variational parameters for depth p+1 from parameters at depth p, and replaces the standard expectation-value objective with a Conditional Value at Risk (CVaR) objective to bias optimization toward better measurement outcomes. Experiments were conducted on Erdős–Rényi random graphs and regular graph instances of varying sizes and degrees, with additional applicability tests on exact cover instances. QAOA circuits were executed in simulation using Qiskit's noiseless statevector simulator, while initial depth-1 parameters were generated using the QN-SPSA optimizer. The CNN was trained using supervised learning with pretrained embeddings, MSE loss, Adam optimization, batch size 6, and 50 epochs. Performance was assessed mainly through approximation ratio and expectation value, and compared against four baselines: random initialization QAOA, interpolation-based QAOA, CNN-QAOA without CVaR, and CVaR-QAOA without CNN. The study also includes sensitivity analysis over the CVaR parameter alpha, circuit depth, graph size, degree, and edge probability, reporting that smaller alpha values generally smooth the objective and improve approximation ratios.

**Algorithms used:** QAOA, CVaR-QAOA, CNN-CVaR-QAOA, QN-SPSA, Adam
**Frameworks:** Qiskit, NetworkX

**Experimental setup:** All QAOA circuits were run on the noiseless Qiskit statevector simulator. The number of circuit measurements was set to 1024. Problem instances were generated as Erdős–Rényi graphs using Python NetworkX, with additional tests on regular graphs and exact cover instances. The CNN architecture used two up-sampling convolutional layers with 2x2 kernels, stride 1, ReLU activation, and zero-padding, followed by one down-sampling convolutional layer with a 64x3x2 filter. Initial p=1 QAOA parameters were randomly initialized using the QN-SPSA optimizer. Training used batch size 6, 50 epochs, Adam optimizer, and learning rate 0.0001.

**Dataset:** Synthetic combinatorial optimization instances rather than financial data: Erdős–Rényi random graphs, random regular graphs for Max-Cut, and small exact cover problem instances. Graphs varied in node count, degree, and edge probability; all edge weights were set to 1 for Max-Cut.
## Findings
- [supported] The paper proposes CNN-CVaR-QAOA, combining a convolutional neural network for QAOA parameter prediction with CVaR as the optimization objective, and reports better Max-Cut solutions than CNN-QAOA, RI-QAOA, INTERP-QAOA, and CVaR-QAOA alone on Erdős–Rényi graph instances.
- [supported] All reported quantum results were obtained on a noiseless Qiskit statevector simulator with 1024 measurement shots per circuit; no real quantum hardware experiments were reported.
- [supported] For depth p=2 on ER random graphs, CNN-CVaR-QAOA with α=0.5 improved approximation ratios by 0.06 to 0.2 relative to the four comparison methods across tested graph configurations.
- [supported] On 8-node 3-regular graphs, CNN-CVaR-QAOA with α=0.5 reached the optimal solution at depth 3, whereas CVaR-QAOA without CNN reached the optimal result at depth 4.
- [supported] On 12-node 3-regular graphs, CNN-CVaR-QAOA with α=0.1 reached optimality at depth 4; CVaR-QAOA with α=0.1 also reached the optimum at depth 4 but underperformed at shallower depths.
- [supported] On 12-node 3-regular graphs, CNN-CVaR-QAOA with α=0.1 at depth 2 achieved performance comparable to CNN-QAOA and INTERP-QAOA at depth 7, indicating improved depth efficiency in simulation.
- [supported] On a 14-node 3-regular graph, the CNN-CVaR joint optimization produced the lowest final expectation values among the tested methods at depths 2 and 3, and at depth 3 converged very close to the theoretical minimum.
- [supported] Lower CVaR parameter values α produced smoother objective landscapes and better optimization outcomes; the authors report that decreasing α shifts measurements toward lower-energy states and improves approximation ratios.
- [supported] For depth p=2 on 10-node 3-regular graphs, CNN-CVaR-QAOA with α=0.1 improved approximation ratio by about 4.0%, 8.8%, 12.6%, and 13.7% over α=0.3, 0.5, 0.8, and 1.0 respectively; similar trends were observed on 12-, 14-, and 16-node 3-regular graphs and on other regular/ER graph settings.
- [supported] In a 14-node degree-3 ER graph at depth 2, decreasing α from 1 to 0.1 moved the final circuit expectation value closer to the brute-force optimum, with apparent saturation around α=0.1.
- [supported] On a 6-node degree-3 ER graph, the final overall expectation values under CVaR optimization were -5.886, -6.513, and -7.0 for three decreasing α settings, showing concentration toward lower-eigenvalue states as α decreased.
- [supported] In scalability tests on 3-regular graphs with fixed depth 3, the method maintained a reported approximation ratio of 93% on a 26-qubit system, though the authors note computational overhead increases substantially with qubit count.
- [supported] The method was also tested on exact cover instances, where reducing α enabled convergence to optimal or top solutions in the reported examples, suggesting applicability beyond Max-Cut.
- [speculative] The paper suggests the method could be broadly useful for larger-scale NISQ optimization problems and diverse combinatorial optimization domains, but this was not validated beyond small simulated instances.

**Results summary:** This peer-reviewed empirical paper evaluates a hybrid CNN-CVaR-QAOA method for combinatorial optimization, primarily Max-Cut, using classical simulation rather than real quantum hardware. All experiments were run on a noiseless Qiskit statevector simulator with 1024 shots. Across Erdős–Rényi and regular graph instances, the method consistently outperformed random initialization, interpolation, CNN-only parameter prediction, and CVaR-only QAOA in terms of approximation ratio or final expectation value. Reported gains include approximation-ratio improvements of 0.06-0.2 at depth 2 versus competing methods, faster convergence to optimal solutions on 8-node and 12-node regular graphs, and depth-efficiency benefits such as depth-2 performance matching other methods at depth 7 in one 12-node case. The study also systematically analyzes the CVaR parameter α, finding that smaller α values produce smoother objective functions and better approximation ratios; for example, α=0.1 improved approximation ratio by 4.0%, 8.8%, 12.6%, and 13.7% over α=0.3, 0.5, 0.8, and 1.0 on 10-node 3-regular graphs. A scalability experiment reports a 93% approximation ratio on a 26-qubit simulated 3-regular graph at depth 3, while noting increased computational cost. No confidence intervals were reported; some figures mention variance/error bars over three non-isomorphic instances or repeated runs.

**Performance claims:**
- Simulation only: noiseless Qiskit statevector simulator, 1024 shots per circuit
- At depth p=2, CNN-CVaR-QAOA (α=0.5) improved approximation ratio by 0.06-0.2 versus CNN-QAOA, RI-QAOA, INTERP-QAOA, and CVaR-QAOA on tested ER graph configurations
- On 8-node 3-regular graphs, CNN-CVaR-QAOA (α=0.5) reached the optimal solution at depth 3; CVaR-QAOA without CNN reached the optimum at depth 4
- On 12-node 3-regular graphs, CNN-CVaR-QAOA (α=0.1) reached optimality at depth 4
- On 12-node 3-regular graphs, CNN-CVaR-QAOA (α=0.1) at depth 2 performed comparably to CNN-QAOA and INTERP-QAOA at depth 7
- On a 14-node 3-regular graph, CNN-CVaR achieved the lowest final expectation value among tested methods at depths 2 and 3, and at depth 3 converged very close to the theoretical minimum
- On 10-node 3-regular graphs at depth p=2, α=0.1 improved approximation ratio by approximately 4.0%, 8.8%, 12.6%, and 13.7% relative to α=0.3, 0.5, 0.8, and 1.0
- On a 6-node degree-3 ER graph, final expectation values under decreasing α settings were -5.886, -6.513, and -7.0
- On a 26-qubit 3-regular graph at fixed depth 3, the method maintained a reported approximation ratio of 93%
## Quantum advantage claim
**Classification:** speculative

The paper reports improved QAOA optimization performance over alternative heuristics, but all results are from noiseless classical simulation on small instances and do not demonstrate a quantum speedup or practical quantum advantage over classical state-of-the-art solvers.
## Limitations
- All experiments were performed on the noiseless Qiskit state-vector simulator rather than real quantum hardware, so hardware noise, decoherence, gate errors, and readout errors were not evaluated.
- Problem instances are limited to synthetic Erdos–Renyi and regular graph benchmarks for Max-Cut, plus small exact-cover examples, which restricts external validity to broader optimization settings.
- The study focuses on small-scale systems and shallow circuits; most reported Max-Cut experiments use roughly 6–16 qubits, with some scalability tests up to 22–26 qubits, limiting evidence for larger production-scale instances.
- The authors explicitly note that increasing qubit count significantly increases computational overhead and time complexity, revealing a trade-off between scalability and computational efficiency.
- The method depends on training a CNN on graph examples, implying nontrivial training-data preparation costs and possible retraining burdens for new instance distributions or deeper QAOA settings.
- The paper reports only three instances per configuration and often three runs per setting, which limits statistical power and robustness of the empirical conclusions.
- The number of circuit measurements is fixed at 1024, while the paper notes CVaR estimator variance scales as O(1/(Kα^2)); this may make results sensitive to shot count, especially for small α.
- Performance is demonstrated mainly for Max-Cut and only briefly for exact cover, so generality across other combinatorial optimization problems remains only partially validated.
- The approach requires tuning the CVaR hyperparameter α, and results show strong dependence on α; inappropriate α can bias evaluation or fail to show improvement.
- Data availability is limited because the paper states that supporting data are available only on reasonable request from the corresponding author, which weakens reproducibility.
- [inferred] No experiments on actual NISQ devices were conducted, so claims about suitability for the NISQ era are not empirically validated under realistic hardware constraints.
- [inferred] No explicit comparison is provided against strong classical optimization baselines beyond approximation-ratio references, so the practical advantage over state-of-the-art classical solvers is unclear.
- [inferred] The paper does not report wall-clock runtime, training cost, or end-to-end resource consumption for the CNN-assisted workflow, limiting assessment of production scalability.
- [inferred] Reproducibility is incomplete because the paper does not provide code, trained model artifacts, random seeds, or full implementation details for dataset generation and training splits.
- [inferred] Internal validity may be limited because hyperparameter choices such as batch size, epochs, learning rate, and α appear fixed without broad ablation across training settings.
- [inferred] The use of noiseless simulation may overestimate the benefit of lower-depth circuits and smoother objectives relative to real hardware where sampling noise and control errors interact with optimization.
## Open questions
- How well does CNN-CVaR-QAOA perform on real quantum hardware with realistic noise, limited connectivity, and calibration drift?
- Does the observed advantage persist for substantially larger graphs and deeper QAOA circuits beyond the small and medium simulated instances studied here?
- What is the best strategy for selecting or adapting the CVaR parameter α across different problem classes, graph sizes, and circuit depths?
- How sensitive is the method to shot count, especially when α is very small and CVaR focuses on a small subset of outcomes?
- Can the CNN trained on one graph distribution generalize to different graph families, weighted graphs, or real-world optimization instances without retraining?
- What is the trade-off between CNN training cost and optimization gains compared with simpler initialization heuristics or purely classical solvers?
- How robust is the method to different optimizer choices, random initializations, and training-set compositions?
- Will the approach remain effective when hardware noise, barren plateaus, and parameter concentration effects become more severe at larger depths?
- To what extent can the method be transferred beyond Max-Cut and exact cover to other combinatorial optimization problems with different Hamiltonian structures?
- [inferred] Is the improvement due primarily to the CNN predictor, the CVaR objective, or their interaction, and under what regimes does each component matter most?
- [inferred] How does the method compare against stronger classical baselines such as advanced SDP, local search, branch-and-bound, or learned classical heuristics on the same instances?

**Future work:**
- Further address the trade-off between scalability and computational efficiency as qubit number increases.
- Apply the CNN-CVaR-QAOA strategy to a broader range of optimization problems beyond Max-Cut.
- Explore the method on larger-scale QAOA instances with much greater circuit depth as quantum hardware improves.
- Leverage the approach on future quantum computers with higher qubit counts, where lower-depth high-quality approximations may be especially valuable.
- Further investigate dynamic control of ansatz expressiveness through the CVaR parameter α to improve optimization performance.
- [inferred] Validate the method on real NISQ hardware and study the impact of noise mitigation and finite-shot effects.
- [inferred] Develop adaptive or automated schemes for choosing α rather than fixing it manually.
- [inferred] Improve computational efficiency of the CNN-assisted optimization pipeline to make larger-scale experiments practical.
- [inferred] Expand benchmarking to weighted graphs, real-world datasets, and stronger classical baselines.
- [inferred] Release code, datasets, and trained models to improve reproducibility and enable independent verification.
## Key ideas
- #idea:hybrid-approach — Proposes a hybrid CNN-CVaR-QAOA method where a CNN predicts deeper-layer QAOA parameters and CVaR reshapes the objective toward better low-energy outcomes.
- #idea:near-term-feasibility — Reports shallower-depth performance gains in noiseless simulation, suggesting possible NISQ relevance if lower-depth circuits can offset hardware constraints.
- #idea:quantum-advantage — Claims improved optimization performance over several QAOA-based baselines, but only within simulated quantum heuristic comparisons rather than against strong classical solvers.
- #idea:hybrid-approach — Smaller CVaR alpha values are reported to smooth optimization and improve approximation ratios, indicating the objective design is a major contributor to performance.
## Contradictions
- The paper suggests near-term/NISQ usefulness and improved quantum optimization performance, but this is contradicted by the fact that all results come from noiseless classical simulation with no real-hardware validation, so practical quantum superiority is unproven.
- The paper reports scalability up to 26 qubits with strong approximation ratios, but also notes computational overhead rises substantially with qubit count, contradicting any strong implication that the method already scales to realistic large optimization problems.
- Any implied quantum advantage is contradicted by the absence of comparisons against strong classical state-of-the-art optimization baselines; the reported gains are only versus alternative QAOA initialization/objective variants.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->

## Experiment details
### Input
Input instances consisted of unweighted Max-Cut graphs sampled from the Erdős–Rényi ensemble and regular graph families. Reported graph sizes included node/qubit counts ranging roughly from 4 to 26, with many experiments on 6-16 nodes, 8-, 10-, 12-, 14-, and 16-node graphs, and scalability tests up to 22/26 qubits. Node degrees varied from 3 to 8 in some experiments; edge probabilities were varied in the range 0.5-0.7, with explicit tests at 0.5, 0.6, and 0.7. Multiple instances were generated per configuration, often three non-isomorphic instances. For Max-Cut, graphs were encoded into Ising cost Hamiltonians with unit edge weights. Additional exact cover experiments used two handcrafted subset-collection instances, one with 6 subsets and one with 14 subsets.

### Process
1. Generate Max-Cut instances from Erdős–Rényi or regular graph ensembles using NetworkX. 2. Encode each graph as a QAOA cost Hamiltonian for Max-Cut. 3. Initialize depth-1 QAOA variational parameters using the QN-SPSA optimizer. 4. Use a CNN to learn a mapping from p-depth parameters to (p+1)-depth parameters, with input tensor size 1x2xp and output size 1x2x(p+1). 5. Train the CNN using pretrained embeddings, MSE loss, Adam optimizer, batch size 6, and 50 epochs. 6. Execute QAOA circuits on the noiseless Qiskit statevector simulator with 1024 measurements. 7. Replace the standard expectation objective with CVaR by sorting measured sample energies and averaging the best alpha fraction of outcomes. 8. Optimize and evaluate across different alpha values, especially 1, 0.8, 0.5, 0.3, 0.1, and in one exact-cover case 0.01. 9. Compare CNN-CVaR-QAOA against CNN-QAOA, RI-QAOA, INTERP-QAOA, and CVaR-QAOA over varying graph sizes, degrees, edge probabilities, and circuit depths. 10. Report approximation ratios, expectation values, convergence behavior, and variance across repeated runs or multiple graph instances.

### Output
The main outputs were approximation ratio for Max-Cut, final converged expectation value of the cost Hamiltonian, convergence/error curves versus circuit depth, CVaR landscapes over gamma and beta, and variance/error bars across sampled instances. Baseline comparisons were made against random initialization QAOA, interpolation-based QAOA, CNN-QAOA, and CVaR-QAOA. The paper reports that CNN-CVaR-QAOA achieved better approximation ratios, especially at low circuit depth, with improvements of about 0.06-0.2 over competing methods in some ER graph settings, and that smaller alpha values generally improved convergence toward optimal or near-optimal solutions.

### Parameters
- shots: 1024
- optimizer_initialization: QN-SPSA
- cnn_optimizer: Adam
- learning_rate: 0.0001
- batch_size: 6
- epochs: 50
- loss_function: MSE
- cnn_activation: ReLU
- cnn_kernels: ['2x2', '64x3x2']
- cnn_stride: 1
- circuit_depths_tested: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
- alpha_values_tested: [1.0, 0.8, 0.5, 0.3, 0.1, 0.01]
- qubit_counts_reported: [4, 6, 8, 10, 12, 14, 16, 22, 26]

### Hardware
Qiskit noiseless statevector simulator; no real QPU was used. The paper states that all QAOA circuits were executed on the Qiskit platform in a noiseless simulated environment with 1024 measurements per circuit. No noise model, cloud backend, or transpilation settings were reported.

### Reproducibility
Partial reproducibility. The paper provides substantial methodological detail on algorithms, simulator, graph generation, CNN architecture, training hyperparameters, shots, and comparison baselines. However, no public code repository is mentioned in the provided text, and the synthetic datasets are generated rather than archived. Data availability is stated as available from the corresponding author upon reasonable request. Replication appears feasible in principle, but some implementation details may still need clarification.
