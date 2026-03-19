# High Frequency Trading

**Papers:** 13 | **Empirical:** 1 | **Theoretical:** 3 | **Review:** 1

## Papers

| Paper | Year | Source Type | Methods | QA Claim | Relevance |
|-------|------|-------------|---------|----------|-----------|
| [[2026_Azfar_ShallowRobustQaoa]] | 2026 | preprint | QAOA, quantum-annealing, variational, QUBO, grover | speculative | medium |
| [[2026_DECCANINTERNATIONALACADEMICPUBLISHERS_QuantumComputingAlgorithms]] | 2026 | other | grover, variational, quantum-simulation, classical-simulation, quantum-ML | speculative | medium |
| [[2026_Nawaz_ExploringQuantumMachine]] | 2026 | peer-reviewed-theoretical | QAOA, VQE, quantum-ML, quantum-SVM, grover, quantum-simulation, variational, classical-simulation | theoretical | high |
| [[2025_Gibadullin_QuantumAlgorithmsSolving]] | 2025 | conference-paper | VQE, QAOA, grover, variational, classical-simulation | speculative | medium |
| [[2025_Hlatshwayo_TechnicalReviewQuantum]] | 2025 | preprint | HHL, QAOA, grover, quantum-walk, amplitude-estimation, quantum-simulation, quantum-ML | speculative | high |
| [[2025_Jiang_RasenganTransitionHamiltonian]] | 2025 | conference-paper | variational, QAOA, quantum-annealing, QUBO, quantum-simulation | speculative | high |
| [[2025_Malhotra_ComparativeStudyQuantum]] | 2025 | conference-paper | QAOA, grover, quantum-ML, classical-simulation | speculative | medium |
| [[2025_Vangibhuratha_QuantumMachineLearning]] | 2025 | peer-reviewed-theoretical | quantum-ML, quantum-SVM, variational, quantum-annealing, QAOA, quantum-simulation, classical-simulation | theoretical | high |
| [[2025_Vellaipandiyan_HybridQlstmFramework]] | 2025 | conference-paper | quantum-ML, variational | speculative | high |
| [[2026_Mahmod_StateQuantumComputing]] | 2025 | review-article | HHL, QAOA, VQE, quantum-annealing, grover, quantum-ML, quantum-SVM, variational, QUBO, quantum-simulation, classical-simulation | speculative | high |
| [[2023_Vishwakarma_QuantumComputingAlgorithms]] | 2023 | peer-reviewed-empirical | QAOA, VQE, variational, quantum-ML, hybrid-approach, classical-simulation | speculative | high |
| [[2020_Kommadi_QuantumComputingSolutions]] | 2020 | technical-report | QAOA, grover, quantum-annealing, quantum-ML, quantum-SVM, quantum-walk, variational, classical-simulation | speculative | medium |
| [[2016_Petrosyan_GroverSearchAlgorithm]] | 2015 | peer-reviewed-theoretical | grover | theoretical | medium |

## Key Findings

- [supported] Linear-Ramp LC-QAOA improves convergence and feasibility compared to standard QAOA, Two-Step QAOA, and Grover-Mixer QAOA in noiseless and shot-based simulations on small VRP instances. — [[2026_Azfar_ShallowRobustQaoa]]
- [supported] Linear-Chain (LC) QAOA reduces two-qubit gate depth and boosts noise robustness, achieving the shallowest circuits on IBM Eagle/Heron hardware. — [[2026_Azfar_ShallowRobustQaoa]]
- [supported] On real hardware (IBM Eagle/Heron), LC-QAOA with XpXm dynamical decoupling more than doubles feasibility (from <1% to >2%) and recovers the optimal VRP solution in several trials. — [[2026_Azfar_ShallowRobustQaoa]]
- [supported] Grover-Mixer QAOA and Two-Step QAOA show high feasibility in simulation (e.g., 21% for GM-QAOA at p=8) but are hampered by deeper circuits, making them less effective on real hardware. — [[2026_Azfar_ShallowRobustQaoa]]
- [supported] Linear-ramp initialization (LRI-QAOA) concentrates probability on feasible solutions, outperforming random initialization in simulations (e.g., 47.6% feasibility vs. 2% for standard QAOA at p=8). — [[2026_Azfar_ShallowRobustQaoa]]
- [supported] Dynamical decoupling (XpXm) improves hardware performance (e.g., optimal solution rank improved from 235 to 15 on IBM Rensselaer), while heavier error mitigation (e.g., ZNE, Pauli twirling) degrades performance due to circuit distortion. — [[2026_Azfar_ShallowRobustQaoa]]
- [supported] LC-QAOA scales efficiently to larger VRP instances (30 qubits), reliably recovering the optimal route at depths p>16 on both IBM Eagle and Heron, with higher success on lower-error devices. — [[2026_Azfar_ShallowRobustQaoa]]
- [supported] CVaR (Conditional Value at Risk) objective improves optimization by biasing search toward high-quality solutions, enabling reliable performance at larger scales. — [[2026_Azfar_ShallowRobustQaoa]]
- [supported] The study provides a unified comparative framework for QML optimization algorithms, highlighting their practical feasibility and identifying key research gaps hindering real-world deployment — [[2026_Nawaz_ExploringQuantumMachine]]
- [supported] Challenges such as quantum noise, scalability, and hardware limitations remain significant barriers to the practical deployment of QML algorithms — [[2026_Nawaz_ExploringQuantumMachine]]
- [supported] The Variational Quantum Eigensolver (VQE) algorithm is proposed as an effective tool for minimizing the energy function of time-varying dynamic control systems, demonstrating potential for quantum acceleration in optimization tasks. — [[2025_Gibadullin_QuantumAlgorithmsSolving]]
- [supported] Quantum algorithms, including VQE, Grover’s algorithm, and QAOA, are applied to dynamic control problems, showing numerical optimization results for differential equation-based systems. — [[2025_Gibadullin_QuantumAlgorithmsSolving]]
- [supported] The paper presents pseudocode and numerical results for optimizing control actions in a dynamic system described by nonlinear differential equations, achieving a minimal objective function value of 0.4047 for a linear system and 2.619e-08 for a nonlinear system. — [[2025_Gibadullin_QuantumAlgorithmsSolving]]
- [supported] Rasengan improves accuracy by 4.12× compared to the state-of-the-art QAOA (Choco-Q) on constrained binary optimization problems across 2000 cases from five domains (facility location, k-partition, job scheduling, set cover, and graph coloring). — [[2025_Jiang_RasenganTransitionHamiltonian]]
- [supported] Rasengan achieves a 379× improvement in solution quality over baseline methods on real-world quantum platforms (IBM Kyiv and Brisbane). — [[2025_Jiang_RasenganTransitionHamiltonian]]
- [supported] Rasengan reduces circuit depth by 1.96× compared to prior variational quantum algorithms (VQAs) and by 49× compared to Choco-Q, making it deployable on NISQ devices. — [[2025_Jiang_RasenganTransitionHamiltonian]]
- [supported] Rasengan is the first quantum algorithm to outperform the mean quality of feasible solution baselines on real hardware, achieving an approximation ratio gap (ARG) as low as 0.01 for small-scale problems. — [[2025_Jiang_RasenganTransitionHamiltonian]]
- [supported] Hamiltonian simplification and pruning techniques reduce circuit depth by over 94.6%, while probability-preserving segmented execution further reduces depth to ~50, suitable for current quantum hardware. — [[2025_Jiang_RasenganTransitionHamiltonian]]
- [supported] Error mitigation via solution purification improves accuracy by more than 303× on noisy hardware. — [[2025_Jiang_RasenganTransitionHamiltonian]]
- [supported] Rasengan maintains a 100% in-constraints rate (feasible solutions) on real hardware, unlike penalty-term-based QAOA, which often violates constraints. — [[2025_Jiang_RasenganTransitionHamiltonian]]

## Methodologies Used

| Method | Papers |
|--------|--------|
| QAOA | 10 |
| variational | 10 |
| grover | 9 |
| quantum-ML | 9 |
| classical-simulation | 8 |
| quantum-simulation | 6 |
| quantum-annealing | 5 |
| VQE | 4 |
| quantum-SVM | 4 |
| QUBO | 3 |
| HHL | 2 |
| quantum-walk | 2 |
| amplitude-estimation | 1 |
| hybrid-approach | 1 |

## Open Questions

- How does the algorithm perform with more than 5 nodes or 2 vehicles in hardware experiments? — [[2026_Azfar_ShallowRobustQaoa]]
- What is the impact of decoherence and gate errors on solution quality at higher depths (p > 20)? — [[2026_Azfar_ShallowRobustQaoa]]
- Can the linear-ramp schedule and LC-QAOA maintain performance on larger, more constrained problems (e.g., capacitated VRP)? — [[2026_Azfar_ShallowRobustQaoa]]
- How do the proposed methods compare to quantum annealing or hybrid quantum-classical approaches for the same problem instances? — [[2026_Azfar_ShallowRobustQaoa]]
- What is the minimum hardware fidelity required to achieve >10% feasibility for VRP instances? — [[2026_Azfar_ShallowRobustQaoa]]
- Can adaptive schedules or parameter transfer techniques improve performance across diverse problem instances? — [[2026_Azfar_ShallowRobustQaoa]]
- How does the choice of penalty weight (λ) affect feasibility and solution quality in larger instances? — [[2026_Azfar_ShallowRobustQaoa]]
- What are the trade-offs between qubit count, circuit depth, and solution quality for industry-relevant problem sizes? — [[2026_Azfar_ShallowRobustQaoa]]
- Can hardware-aware compilation (e.g., qubit placement, chain orientation) further reduce circuit depth without sacrificing performance? — [[2026_Azfar_ShallowRobustQaoa]]
- Expand problem realism by incorporating capacities, time windows, and multi-objective costs (e.g., emissions) into VRP benchmarks — [[2026_Azfar_ShallowRobustQaoa]]
