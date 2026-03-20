# High Frequency Trading

**Papers:** 16 | **Empirical:** 2 | **Theoretical:** 4 | **Review:** 2

## Papers

| Paper | Year | Source Type | Methods | QA Claim | Relevance |
|-------|------|-------------|---------|----------|-----------|
| [[2026_Azfar_ShallowRobustQaoa]] | 2026 | preprint | QAOA, QUBO, variational, grover, quantum-simulation, classical-simulation | speculative | medium |
| [[2026_DECCANINTERNATIONALACADEMICPUBLISHERS_QuantumComputingAlgorithms]] | 2026 | other | grover, variational, quantum-simulation, classical-simulation, quantum-ML | speculative | medium |
| [[2026_Nawaz_ExploringQuantumMachine]] | 2026 | peer-reviewed-theoretical | QAOA, VQE, quantum-ML, quantum-SVM, grover, variational, quantum-simulation | theoretical | high |
| [[2025_Ganguly_HybridClassicalQuantum]] | 2025 | conference-paper | quantum-ML, variational, QUBO, classical-simulation | speculative | high |
| [[2025_Gibadullin_QuantumAlgorithmsSolving]] | 2025 | conference-paper | VQE, QAOA, grover, variational | speculative | medium |
| [[2025_Hlatshwayo_TechnicalReviewQuantum]] | 2025 | preprint | HHL, grover, quantum-walk, amplitude-estimation, quantum-simulation, quantum-ML | speculative | high |
| [[2025_JETIR_QuantumFinance]] | 2025 | peer-reviewed-theoretical | QAOA, VQE, quantum-ML, amplitude-estimation, variational, classical-simulation | theoretical | high |
| [[2025_Jiang_RasenganTransitionHamiltonian]] | 2025 | conference-paper | variational, QAOA, VQE, quantum-annealing, QUBO | theoretical | high |
| [[2025_NeelotpalDey_QuantumComputingFinancial]] | 2025 | peer-reviewed-theoretical | QAOA, VQE, quantum-ML, amplitude-estimation, QUBO, variational, classical-simulation | theoretical | high |
| [[2025_Vangibhuratha_QuantumMachineLearning]] | 2025 | peer-reviewed-theoretical | quantum-ML, quantum-SVM, variational, quantum-annealing, QAOA, HHL, quantum-simulation, classical-simulation | theoretical | high |
| [[2025_Vellaipandiyan_HybridQlstmFramework]] | 2025 | conference-paper | quantum-ML, variational | speculative | high |
| [[2026_Mahmod_StateQuantumComputing]] | 2025 | review-article | HHL, QAOA, VQE, quantum-annealing, grover, quantum-ML, quantum-SVM, variational, QUBO, quantum-simulation | theoretical | high |
| [[2025_Deshmukh_QuantumMachineLearning]] | 2024 | peer-reviewed-empirical | quantum-ML, quantum-SVM, VQE, QAOA, variational | speculative | high |
| [[2023_Markna_UnveilingAdvancedComputational]] | 2023 | review-article | QAOA, quantum-annealing, HHL, quantum-ML, quantum-SVM, amplitude-estimation, QUBO, variational, grover, quantum-simulation, classical-simulation | speculative | high |
| [[2023_Vishwakarma_QuantumComputingAlgorithms]] | 2023 | peer-reviewed-empirical | QAOA, VQE, variational, quantum-ML, hybrid-approach | speculative | high |
| [[2016_Petrosyan_GroverSearchAlgorithm]] | 2015 | preprint | grover | speculative | medium |

## Key Findings

- [supported] Linear-Ramp LC-QAOA improves convergence and feasibility compared to standard QAOA, Two-Step QAOA, and Grover-Mixer QAOA on small Vehicle Routing Problem (VRP) instances in noiseless simulations. — [[2026_Azfar_ShallowRobustQaoa]]
- [supported] Linear-Chain (LC) QAOA reduces two-qubit gate depth and boosts noise robustness, achieving the shallowest circuit depth on IBM Eagle/Heron hardware. — [[2026_Azfar_ShallowRobustQaoa]]
- [supported] On real hardware (IBM Eagle/Heron), LC-QAOA with XpXm dynamical decoupling more than doubles feasibility (<1% to >2%) and recovers the optimum in several trials. — [[2026_Azfar_ShallowRobustQaoa]]
- [supported] Linear-ramp initialization (LRI-QAOA) concentrates probability on feasible solutions, improving feasibility rates from ~2% (standard QAOA) to ~47.6% in statevector simulations. — [[2026_Azfar_ShallowRobustQaoa]]
- [supported] Grover-Mixer QAOA yields high feasibility in simulations (21% at p=8) but is hampered by deep circuits on hardware, failing to compile for p > 5. — [[2026_Azfar_ShallowRobustQaoa]]
- [supported] Two-Step QAOA improves feasibility over standard QAOA in simulations (5.6% vs. 2.4% at p=4) but struggles with constraint leakage and deeper circuits. — [[2026_Azfar_ShallowRobustQaoa]]
- [supported] Dynamical decoupling (XpXm) improves hardware performance, boosting feasibility from 1.14% to 1.60% and improving optimal solution rank from 16 to 6 on IBM Fez. — [[2026_Azfar_ShallowRobustQaoa]]
- [supported] Heavy error mitigation (e.g., Pauli twirling, ZNE) underperforms compared to lightweight dynamical decoupling, reducing feasibility from 1.80% to 0.60%. — [[2026_Azfar_ShallowRobustQaoa]]
- [supported] LC-QAOA scales to larger VRP instances (30 qubits), reliably recovering the optimal route at p > 16 on IBM Eagle/Heron, with CVaR objective further improving results. — [[2026_Azfar_ShallowRobustQaoa]]
- [supported] The study provides a unified comparative framework for QML algorithms, highlighting their optimization capabilities, practical feasibility, and limitations within a single analytical structure — [[2026_Nawaz_ExploringQuantumMachine]]
- [supported] Key challenges hindering real-world deployment of QML include quantum noise, scalability constraints, hardware limitations, and algorithmic performance trade-offs — [[2026_Nawaz_ExploringQuantumMachine]]
- [supported] QLSTM test predictions for NVIDIA stock data were slightly superior to classical LSTM, particularly around volatile peaks, indicating better alignment with real-life data — [[2025_Ganguly_HybridClassicalQuantum]]
- [supported] QLSTM demonstrated earlier prediction of turning points in stock market trends compared to classical LSTM, potentially offering advantages in forecasting market movements — [[2025_Ganguly_HybridClassicalQuantum]]
- [supported] QLSTM training loss exhibited smoothing over time, unlike classical LSTM where loss spikes appeared more pronounced toward the end of training — [[2025_Ganguly_HybridClassicalQuantum]]
- [supported] qGAN successfully modeled cryptocurrency data distributions with fewer iterations than classical GANs, achieving equilibrium in generator and discriminator loss functions — [[2025_Ganguly_HybridClassicalQuantum]]
- [supported] qGAN combined with QUBO optimization predicted BNBBTC as the optimal cryptocurrency investment based on real-world Binance data — [[2025_Ganguly_HybridClassicalQuantum]]
- [supported] QCBM with SPSA optimization closely approximated the target probability distribution for the synthetic BAS dataset, outperforming other optimizers like Cobyla — [[2025_Ganguly_HybridClassicalQuantum]]
- [supported] Training time for QLSTM was highly dependent on GPU type, with NVIDIA RTX 3070 showing a 50% reduction in training time per epoch compared to RTX 3060 (780s vs. 1600s) — [[2025_Ganguly_HybridClassicalQuantum]]
- [supported] CUDA-Q acceleration significantly improved QLSTM training performance, reducing training time per epoch from 780s to 18s on an RTX 3070 — [[2025_Ganguly_HybridClassicalQuantum]]
- [supported] Numerical experiments demonstrated that the proposed dynamic control model using quantum-inspired optimization achieved a minimal objective function value of 0.4047, indicating effective system management — [[2025_Gibadullin_QuantumAlgorithmsSolving]]

## Methodologies Used

| Method | Papers |
|--------|--------|
| variational | 14 |
| quantum-ML | 12 |
| QAOA | 11 |
| grover | 8 |
| VQE | 8 |
| quantum-simulation | 7 |
| classical-simulation | 7 |
| QUBO | 6 |
| quantum-SVM | 5 |
| HHL | 4 |
| amplitude-estimation | 4 |
| quantum-annealing | 4 |
| quantum-walk | 1 |
| hybrid-approach | 1 |

## Open Questions

- How does LC-QAOA perform on larger, more realistic VRP instances (e.g., 20+ nodes) with real-world constraints? — [[2026_Azfar_ShallowRobustQaoa]]
- What is the trade-off between circuit depth and solution quality for LC-QAOA at scale? — [[2026_Azfar_ShallowRobustQaoa]]
- Can adaptive schedules (e.g., gradient-based) outperform fixed linear-ramp initialization? — [[2026_Azfar_ShallowRobustQaoa]]
- How do hardware-aware compilation techniques (e.g., qubit placement, chain orientation) impact performance? — [[2026_Azfar_ShallowRobustQaoa]]
- What is the minimal qubit count and gate fidelity required for QAOA to outperform classical solvers on VRP? — [[2026_Azfar_ShallowRobustQaoa]]
- How does the performance of QAOA variants compare to quantum annealing or hybrid quantum-classical methods? — [[2026_Azfar_ShallowRobustQaoa]]
- What is the impact of different penalty weights (λ) on feasibility and solution quality? — [[2026_Azfar_ShallowRobustQaoa]]
- Can error mitigation techniques be co-designed with QAOA to improve robustness without increasing circuit depth? — [[2026_Azfar_ShallowRobustQaoa]]
- How does the choice of mixer Hamiltonian (e.g., XY vs. Grover) affect feasibility and convergence? — [[2026_Azfar_ShallowRobustQaoa]]
- What is the role of warm-starting (e.g., classical heuristics) in improving QAOA performance? — [[2026_Azfar_ShallowRobustQaoa]]
