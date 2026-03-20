---
aliases:
- 'Shallow and Robust QAOA: Improving Feasibility and Hardware Performance via Linear-Chain
  and Ramp Schedules'
- Shallow Robust QAOA Improving
authors:
- Talha Azfar
- Ruimin Ke
auto_detected: true
classification: ''
contradiction_flags:
- contradiction:scalability
doi: 10.21203/rs.3.rs-8297477/v1
evidence_type: ''
idea_tags:
- idea:quantum-advantage
- idea:near-term-feasibility
- idea:hybrid-approach
journal_or_venue: Research Square (preprint)
methodology_tags:
- QAOA
- QUBO
- variational
- grover
- quantum-simulation
- classical-simulation
paper_type: ''
quantum_advantage_claim: speculative
related_papers: []
relevance_phase1: medium
relevance_phase3: high
source_type: preprint
source_type_confidence: high
step1_date: '2026-03-20T00:44:29.637010'
step1_model: Mistral-Large-3
step2_date: '2026-03-20T00:44:33.946128'
step2_model: Mistral-Large-3
step3_date: '2026-03-20T00:44:47.626080'
step3_model: Mistral-Large-3
step4_date: '2026-03-20T00:44:58.339316'
step4_model: Mistral-Large-3
step5_date: '2026-03-20T00:45:44.256839'
step5_model: Mistral-Large-3
step6_date: '2026-03-20T00:46:46.753583'
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
- topic/high-frequency-trading
- method/QAOA
- method/QUBO
- method/variational
- method/grover
- method/quantum-simulation
- method/classical-simulation
- idea/quantum-advantage
- idea/near-term-feasibility
- idea/hybrid-approach
- contradiction/scalability
title: 'Shallow and Robust QAOA: Improving Feasibility and Hardware Performance via
  Linear-Chain and Ramp Schedules'
topic_tags:
- portfolio-optimisation
- high-frequency-trading
year: 2026
zotero_key: ''
---

## Abstract summary
This preprint explores hardware-aware adaptations of the Quantum Approximate Optimization Algorithm (QAOA) to address challenges in near-term quantum computing, such as constraint handling and circuit depth limitations. The authors introduce a linear-ramp parameter schedule and a Linear-Chain (LC) ansatz that restricts interactions to nearest neighbors, reducing swap overhead and improving noise robustness. The study benchmarks these methods against standard QAOA variants on small Vehicle Routing Problem (VRP) instances, demonstrating improved feasibility and solution quality across simulations and real hardware runs.
## Methodology
The paper presents an empirical study comparing five variants of the Quantum Approximate Optimization Algorithm (QAOA) for solving the Vehicle Routing Problem (VRP). The variants include Standard QAOA, Two-Step QAOA, Grover-Mixer QAOA, Linear-Ramp Initialized QAOA (LRI-QAOA), and Linear-Chain QAOA (LC-QAOA). The research employs a hardware-aware co-design approach, focusing on a linear-ramp parameter schedule and a Linear-Chain ansatz to reduce circuit depth and improve noise robustness. The study benchmarks these variants across ideal simulation, Aer simulation, and real quantum hardware (IBM Eagle and Heron processors). The methodology involves formulating the VRP as a Quadratic Unconstrained Binary Optimization (QUBO) problem, converting it to an Ising Hamiltonian, and implementing the QAOA variants using the Qiskit SDK. The evaluation metrics include feasibility of solutions, solution quality (finding the known optimum route), quantum circuit depth, gate requirements, and robustness to noise on real hardware. The experiments use a small VRP instance with a single depot, three customer nodes, and two vehicles, and a larger 30-qubit instance to test scalability. Error suppression techniques like dynamical decoupling (XpXm) and Conditional Value at Risk (CVaR) are also explored to enhance performance.

**Algorithms used:** QAOA, Two-Step QAOA, Grover-Mixer QAOA, Linear-Ramp Initialized QAOA (LRI-QAOA), Linear-Chain QAOA (LC-QAOA)
**Frameworks:** Qiskit

**Experimental setup:** Experiments were implemented using Qiskit SDK (version 2.1.1) within the Qiskit Runtime environment. The setup included classical simulators (statevector and Aer simulator) and real quantum processors (IBM Eagle and Heron). The VRP instances were formulated as QUBO problems, converted to Ising Hamiltonians, and optimized using the COBYQA optimizer. Each QAOA variant was evaluated for feasibility, solution quality, circuit depth, and noise robustness.

**Dataset:** A representative Vehicle Routing Problem (VRP) instance comprising a single depot, three customer nodes, and two vehicles for small-scale experiments. A larger 30-qubit instance (5 nodes, 2 vehicles) was used for scaling tests. Customer locations were randomly distributed on a 2D Euclidean plane, with edge weights computed as squared Euclidean distances.
## Findings
- [supported] Linear-Ramp LC-QAOA improves convergence and feasibility compared to standard QAOA, Two-Step QAOA, and Grover-Mixer QAOA on small Vehicle Routing Problem (VRP) instances in noiseless simulations.
- [supported] Linear-Chain (LC) QAOA reduces two-qubit gate depth and boosts noise robustness, achieving the shallowest circuit depth on IBM Eagle/Heron hardware.
- [supported] On real hardware (IBM Eagle/Heron), LC-QAOA with XpXm dynamical decoupling more than doubles feasibility (<1% to >2%) and recovers the optimum in several trials.
- [supported] Linear-ramp initialization (LRI-QAOA) concentrates probability on feasible solutions, improving feasibility rates from ~2% (standard QAOA) to ~47.6% in statevector simulations.
- [supported] Grover-Mixer QAOA yields high feasibility in simulations (21% at p=8) but is hampered by deep circuits on hardware, failing to compile for p > 5.
- [supported] Two-Step QAOA improves feasibility over standard QAOA in simulations (5.6% vs. 2.4% at p=4) but struggles with constraint leakage and deeper circuits.
- [supported] Dynamical decoupling (XpXm) improves hardware performance, boosting feasibility from 1.14% to 1.60% and improving optimal solution rank from 16 to 6 on IBM Fez.
- [supported] Heavy error mitigation (e.g., Pauli twirling, ZNE) underperforms compared to lightweight dynamical decoupling, reducing feasibility from 1.80% to 0.60%.
- [supported] LC-QAOA scales to larger VRP instances (30 qubits), reliably recovering the optimal route at p > 16 on IBM Eagle/Heron, with CVaR objective further improving results.
- [speculative] Hardware-aligned ansätze and structured schedules (e.g., linear-ramp) may enable quantum advantage for combinatorial optimization at larger scales.
- [speculative] Co-design of algorithm, compilation, and hardware could unlock reliable performance at the edge of current NISQ capabilities.
- [disputed] The paper claims that Grover-Mixer and Two-Step QAOA are theoretically promising but practically limited by circuit depth, contradicting prior work emphasizing their feasibility-preserving benefits.

**Results summary:** The paper presents a hardware-aware co-design of the Quantum Approximate Optimization Algorithm (QAOA) for the Vehicle Routing Problem (VRP), demonstrating that linear-ramp parameter schedules and Linear-Chain (LC) ansätze significantly improve feasibility and noise robustness. In simulations, LC-QAOA and Linear-Ramp Initialized QAOA (LRI-QAOA) outperform standard QAOA, Two-Step QAOA, and Grover-Mixer QAOA in feasibility and solution quality. On real hardware (IBM Eagle/Heron), LC-QAOA achieves the shallowest circuit depth and, combined with dynamical decoupling, doubles feasibility rates and recovers optimal solutions. However, heavy error mitigation techniques degrade performance, while lightweight suppression (e.g., XpXm) enhances results. The study also shows that LC-QAOA scales to larger instances (30 qubits) with CVaR objective, suggesting a practical path for near-term quantum optimization.

**Performance claims:**
- 47.6% feasibility for LRI-QAOA in statevector simulations (vs. ~2% for standard QAOA)
- 21% feasibility for Grover-Mixer QAOA at p=8 in simulations
- 5.6% feasibility for Two-Step QAOA at p=4 (vs. 2.4% for standard QAOA)
- >2% feasibility on IBM Eagle hardware with LC-QAOA and XpXm (vs. <1% without mitigation)
- Optimal solution rank improved from 16 to 6 on IBM Fez with XpXm decoupling
- Feasibility improved from 1.14% to 1.60% on IBM Fez with XpXm decoupling
- LC-QAOA achieves the shallowest two-qubit gate depth (e.g., significantly lower than Grover-Mixer QAOA, which fails to compile for p > 5)
- LC-QAOA recovers the optimal route at p > 16 for 30-qubit VRP instances on IBM Eagle/Heron
## Quantum advantage claim
**Classification:** speculative

The paper suggests that hardware-aligned ansätze and structured schedules could enable quantum advantage for combinatorial optimization, but all results are from simulations or small-scale hardware experiments. No empirical demonstration of quantum advantage is provided, and the scalability claims remain unvalidated on real hardware for larger problem sizes.
## Limitations
- Absolute feasibility on current hardware remains low (<1% without mitigation), limiting practical applicability [inferred]
- Experiments limited to small VRP instances (3-5 nodes) due to hardware constraints, not representative of real-world problem sizes
- Results heavily depend on backend calibration and mapping, introducing variability across devices [inferred]
- No comparison with state-of-the-art classical solvers (e.g., advanced heuristics or metaheuristics) for benchmarking [inferred]
- Lack of peer review as this is a preprint, potentially affecting methodological rigor [inferred]
- Proprietary hardware access (IBM Eagle/Heron) may limit reproducibility for independent researchers [inferred]
- Linear-Chain QAOA sacrifices expressiveness by removing non-adjacent ZZ interactions, potentially missing optimal solutions
- Two-Step QAOA and Grover-Mixer QAOA produce deep circuits that exceed error tolerance of current hardware
- Parameter transfer from simulation to hardware may not generalize across different problem instances [inferred]
- Advanced error mitigation techniques (e.g., ZNE, Pauli twirling) underperformed compared to simple dynamical decoupling, suggesting limited applicability
- CVaR optimization introduces a hyperparameter (α) that requires problem-specific tuning [inferred]
- No exploration of capacitated or time-window VRPs, which are more realistic but complex [inferred]
- Hardware noise and decoherence dominate results, making it difficult to isolate algorithmic performance
- Limited sampling (10,000 shots) may not capture rare high-quality solutions in noisy environments [inferred]
## Open questions
- How does LC-QAOA perform on larger, more realistic VRP instances (e.g., 20+ nodes) with real-world constraints?
- What is the trade-off between circuit depth and solution quality for LC-QAOA at scale?
- Can adaptive schedules (e.g., gradient-based) outperform fixed linear-ramp initialization?
- How do hardware-aware compilation techniques (e.g., qubit placement, chain orientation) impact performance?
- What is the minimal qubit count and gate fidelity required for QAOA to outperform classical solvers on VRP?
- How does the performance of QAOA variants compare to quantum annealing or hybrid quantum-classical methods?
- What is the impact of different penalty weights (λ) on feasibility and solution quality?
- Can error mitigation techniques be co-designed with QAOA to improve robustness without increasing circuit depth?
- How does the choice of mixer Hamiltonian (e.g., XY vs. Grover) affect feasibility and convergence?
- What is the role of warm-starting (e.g., classical heuristics) in improving QAOA performance?

**Future work:**
- Extend to capacitated and time-window VRPs to assess realism and scalability
- Benchmark against advanced classical solvers (e.g., metaheuristics, exact methods) for head-to-head comparisons
- Explore adaptive parameter schedules that adjust to hardware noise and problem structure
- Co-optimize qubit placement, chain orientation, and dynamical decoupling timing for hardware-aware compilation
- Investigate hybrid strategies combining classical decomposition with QAOA subproblem solving
- Study multi-objective optimization (e.g., cost vs. emissions) in VRP using QAOA
- Develop noise-resilient variants of QAOA that integrate error mitigation into the algorithmic design
- Test on larger quantum processors (e.g., 100+ qubits) to evaluate scaling behavior
- Compare LC-QAOA with problem-inspired ansätze (e.g., VQE-style) on the same instances
- Quantify cross-instance parameter transferability at fixed circuit depth (p)
- Explore alternative initial state preparation methods for Grover-Mixer QAOA to reduce circuit depth
- Investigate the impact of different penalty encodings (e.g., QUBO vs. Ising) on feasibility and solution quality
## Key ideas
- #idea:near-term-feasibility — Hardware-aware QAOA variants (e.g., Linear-Chain QAOA) reduce circuit depth and improve noise robustness, making them viable for near-term quantum devices in logistics and potentially financial optimization problems like portfolio-optimisation or high-frequency-trading
- #idea:hybrid-approach — Co-design strategies combining classical optimization (e.g., COBYQA, CVaR) with quantum algorithms enhance solution quality and feasibility for VRP, suggesting potential for hybrid approaches in financial use cases
- #idea:quantum-advantage — Speculative claim that hardware-aligned ansätze and structured schedules may enable quantum advantage for combinatorial optimization, though not empirically validated for financial applications
- #limitation:noise — Feasibility on real hardware remains below 1% for all QAOA variants, highlighting noise as a critical barrier to practical deployment in finance
- #limitation:qubit-count — Study limited to small VRP instances (3 customer nodes, 2 vehicles) due to hardware constraints, raising scalability concerns for larger financial problems (e.g., portfolio-optimisation with many assets)
- #limitation:data-encoding — Linear-Chain QAOA sacrifices expressiveness by restricting ZZ interactions to nearest neighbors, potentially limiting performance on financial problems requiring long-range interactions (e.g., multi-asset correlations)
## Contradictions
- #contradiction:scalability — Paper claims LC-QAOA scales to larger VRP instances (30 qubits) on IBM hardware, but feasibility remains low (<2%), contradicting implied scalability advantages. No comparison to classical solvers (e.g., CPLEX) is provided, which is critical for validating quantum advantage claims in financial optimization.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->

## Experiment details
### Input
{'source': 'Synthetic VRP instances generated for the study', 'size': {'small_instance': '1 depot, 3 customer nodes, 2 vehicles (small-scale)', 'large_instance': '5 nodes, 2 vehicles (30 qubits)'}, 'features': 'Pairwise edge weights as squared Euclidean distances between customer locations', 'preprocessing_steps': 'Conversion from VRP to QUBO using quadratic penalties, normalization of coefficients, transformation to Ising Hamiltonian'}

### Process
1. Formulate VRP as a QUBO problem using DOcplex and convert to QuadraticProgram in Qiskit. 2. Transform QUBO to Ising Hamiltonian. 3. Implement QAOA variants using Qiskit's QAOAAnsatz, EstimatorV2, and SamplerV2 classes. 4. Optimize parameters using COBYQA optimizer targeting low expectation value of the VRP cost Hamiltonian. 5. Sample 10,000 measurement outcomes (shots) per circuit evaluation. 6. Apply error suppression techniques (e.g., dynamical decoupling) and CVaR for larger instances. 7. Transfer optimized parameters from simulation to hardware for execution.

### Output
{'metrics_reported': ['Feasibility percentage', 'Solution quality (optimal route rank)', 'Two-qubit gate depth', 'Noise robustness'], 'comparison_baselines': ['Standard QAOA', 'Two-Step QAOA', 'Grover-Mixer QAOA', 'Classical CPLEX solver for optimal solution validation'], 'output_format': 'Feasibility ratios, optimal solution ranks, circuit depth metrics, and hardware performance statistics'}

### Parameters
- qubit_count: {'small_instance': '12-14 qubits', 'large_instance': '30 qubits'}
- circuit_depth: Varied by QAOA variant and p (number of layers), e.g., p=4 to p=19
- shots: 10000
- optimizer: COBYQA
- learning_rate: Not explicitly stated
- hyperparameters: {'penalty_factor_lambda': '2 * sum of absolute edge weights', 'CVaR_alpha': 'Adjusted based on hardware noise and sampling variance'}

### Hardware
{'simulator': 'Qiskit Aer statevector and QASM simulators', 'QPU_models': ['IBM Eagle (Rensselaer)', 'IBM Heron (Fez)'], 'cloud_provider': 'IBM Quantum', 'transpilation_settings': 'Optimized for heavy-hex topology, nearest-neighbor interactions for LC-QAOA'}

### Reproducibility
Code and data are available on GitHub (links provided). Sufficient methodological detail is provided to replicate the experiments, including problem formulation, QUBO conversion, and parameter optimization steps.
