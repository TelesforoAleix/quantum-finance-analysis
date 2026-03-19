# Asset Pricing

**Papers:** 24 | **Empirical:** 4 | **Theoretical:** 4 | **Review:** 1

## Papers

| Paper | Year | Source Type | Methods | QA Claim | Relevance |
|-------|------|-------------|---------|----------|-----------|
| [[2026_DECCANINTERNATIONALACADEMICPUBLISHERS_QuantumComputingAlgorithms]] | 2026 | other | grover, variational, quantum-simulation, classical-simulation, quantum-ML | speculative | medium |
| [[2026_Dechant_ErrorResourceEstimates]] | 2026 | preprint | variational, VQE, classical-simulation | speculative | high |
| [[2026_Nawaz_ExploringQuantumMachine]] | 2026 | peer-reviewed-theoretical | QAOA, VQE, quantum-ML, quantum-SVM, grover, quantum-simulation, variational, classical-simulation | theoretical | high |
| [[2026_Prasad_QuantumAlgorithmsStochastic]] | 2026 | preprint | HHL, amplitude-estimation, quantum-simulation, variational, quantum-ML, classical-simulation | speculative | high |
| [[2024_Ghysels_QuantumFinance]] | 2025 | other | quantum-annealing, quantum-simulation | speculative | high |
| [[2025_Benamer_VariationalQuantumAlgorithms]] | 2025 | preprint | VQE, QAOA, quantum-ML, variational, quantum-annealing, quantum-SVM, amplitude-estimation, QUBO, classical-simulation | speculative | high |
| [[2025_Berkowitz_QuantumComputingMeets]] | 2025 | other | quantum-annealing, QUBO, quantum-simulation | speculative | high |
| [[2025_Chaudhary_PracticalQuantumSolver]] | 2025 | conference-paper | variational, quantum-simulation, classical-simulation | speculative | high |
| [[2025_Ganguly_HybridClassicalQuantum]] | 2025 | conference-paper | quantum-ML, variational, QUBO, classical-simulation | speculative | high |
| [[2025_Hlatshwayo_TechnicalReviewQuantum]] | 2025 | preprint | HHL, QAOA, grover, quantum-walk, amplitude-estimation, quantum-simulation, quantum-ML | speculative | high |
| [[2025_JETIR_QuantumFinance]] | 2025 | peer-reviewed-theoretical | QAOA, VQE, quantum-ML, amplitude-estimation, variational, quantum-simulation | theoretical | high |
| [[2025_Malhotra_ComparativeStudyQuantum]] | 2025 | conference-paper | QAOA, grover, quantum-ML, classical-simulation | speculative | medium |
| [[2025_NeelotpalDey_QuantumComputingFinancial]] | 2025 | peer-reviewed-theoretical | QAOA, VQE, quantum-ML, amplitude-estimation, variational, classical-simulation | speculative | high |
| [[2025_Springer_QuantumFinance]] | 2025 | conference-paper | VQE, grover, QAOA, variational | speculative | medium |
| [[2025_Vangibhuratha_QuantumMachineLearning]] | 2025 | peer-reviewed-theoretical | quantum-ML, quantum-SVM, variational, quantum-annealing, QAOA, quantum-simulation, classical-simulation | theoretical | high |
| [[2025_Vellaipandiyan_HybridQlstmFramework]] | 2025 | conference-paper | quantum-ML, variational | speculative | high |
| [[2026_Mahmod_StateQuantumComputing]] | 2025 | review-article | HHL, QAOA, VQE, quantum-annealing, grover, quantum-ML, quantum-SVM, variational, QUBO, quantum-simulation, classical-simulation | speculative | high |
| [[2023_Kobayashi_CrossSectionalStock]] | 2024 | preprint | quantum-ML, variational, classical-simulation | speculative | high |
| [[2024_KI_QuantumFinance]] | 2024 | peer-reviewed-empirical | HHL, amplitude-estimation, quantum-simulation, quantum-walk | theoretical | high |
| [[2024_M_OptimizingMutualFund]] | 2024 | conference-paper | quantum-ML, variational | speculative | medium |
| [[2024_Mustafa_QuantumGraphNeural]] | 2024 | conference-paper | quantum-ML, variational, quantum-simulation, classical-simulation | speculative | high |
| [[2023_Vishwakarma_QuantumComputingAlgorithms]] | 2023 | peer-reviewed-empirical | QAOA, VQE, variational, quantum-ML, hybrid-approach, classical-simulation | speculative | high |
| [[2022_Zhao_QuantumInspiredVariational]] | 2022 | peer-reviewed-empirical | variational, quantum-simulation, classical-simulation | not-applicable | high |
| [[2021_Martin_TowardPricingFinancial]] | 2021 | peer-reviewed-empirical | quantum-simulation, quantum-ML, HHL, variational | speculative | high |

## Key Findings

- [supported] The paper provides rigorous error and resource estimates for variational quantum algorithms (VQAs) solving differential equations (DEs) using Runge-Kutta methods (RKMs), accounting for truncation errors and shot noise in quantum measurements. — [[2026_Dechant_ErrorResourceEstimates]]
- [supported] Higher-order RKMs (e.g., order 4 for a 1D ODE and order 2 for option pricing via the Black-Scholes equation) minimize the total number of quantum circuit evaluations required to achieve a target error. — [[2026_Dechant_ErrorResourceEstimates]]
- [supported] The total error in VQAs for solving DEs is bounded by the sum of the parameter error (from RKM truncation and shot noise) and the representation error (from the quantum ansatz), with the former analyzed in detail. — [[2026_Dechant_ErrorResourceEstimates]]
- [supported] The number of quantum circuit evaluations scales quadratically with the number of variational parameters (NV), highlighting a significant resource bottleneck for large-scale problems. — [[2026_Dechant_ErrorResourceEstimates]]
- [supported] The paper derives analytical bounds for the local truncation error (LTE) of RKMs, showing that the LTE scales as O(Δτ^(p+1)) for a p-th order RKM, where Δτ is the time step size. — [[2026_Dechant_ErrorResourceEstimates]]
- [supported] The shot noise error in quantum measurements scales as O(1/√N_meas), where N_meas is the number of measurements, and the paper provides a framework to minimize this error for a given target accuracy. — [[2026_Dechant_ErrorResourceEstimates]]
- [supported] The study provides a unified comparative framework for QML optimization algorithms, highlighting their practical feasibility and identifying key research gaps hindering real-world deployment — [[2026_Nawaz_ExploringQuantumMachine]]
- [supported] Challenges such as quantum noise, scalability, and hardware limitations remain significant barriers to the practical deployment of QML algorithms — [[2026_Nawaz_ExploringQuantumMachine]]
- [supported] For linear and semilinear SDEs with Lipschitz coefficients, quantum algorithms can estimate relevant quantities (option prices, expected hitting times, moments) to accuracy ε in time ˜O(poly(d) polylog(1/ε)), versus classical O(poly(d)/ε²) — [[2026_Prasad_QuantumAlgorithmsStochastic]]
- [supported] Numerical simulations on small instances (e.g., 2D Black-Scholes with 10 qubits) demonstrate polynomial-to-super-polynomial empirical speedups in accuracy for fixed runtime — [[2026_Prasad_QuantumAlgorithmsStochastic]]
- [supported] Theorem 1 proves a quantum complexity of ˜O(poly(d) polylog(1/ε)) for estimating expectations in linear SDEs, compared to classical O(poly(d)/ε²) — [[2026_Prasad_QuantumAlgorithmsStochastic]]
- [supported] Theorem 2 shows quantum simulation of Fokker-Planck PDEs achieves accuracy ε in time ˜O(d·log(1/ε)), versus classical O(n^(d+1)) for spatial grid size n — [[2026_Prasad_QuantumAlgorithmsStochastic]]
- [supported] Simulated quantum algorithms for 2D Black-Scholes show ~3x speedup over classical Monte Carlo for 0.1% accuracy, with estimated 10-20x speedup on real hardware — [[2026_Prasad_QuantumAlgorithmsStochastic]]
- [supported] Quantum simulation of Langevin dynamics for 3D coarse-grained systems shows ~100x speedup in sampling rare events due to superposition over trajectories — [[2026_Prasad_QuantumAlgorithmsStochastic]]
- [supported] MIDAS (mixed-data sampling) methods are regression-based techniques for combining data at different frequencies in econometrics — [[2024_Ghysels_QuantumFinance]]
- [supported] VQE achieved chemical accuracy (< 1.6 mHa) for small molecules like H2, LiH, and BeH2 using hardware-efficient ansätze on superconducting qubits — [[2025_Benamer_VariationalQuantumAlgorithms]]
- [supported] VQE demonstrated a dissociation energy error of (8 ± 5) × 10^-4 Hartree for H2, within chemical accuracy — [[2025_Benamer_VariationalQuantumAlgorithms]]
- [supported] QAOA on 20-node Max-Cut problems achieved an approximation ratio of ~0.755 at depth p=1, outperforming random guessing (0.5) — [[2025_Benamer_VariationalQuantumAlgorithms]]
- [supported] Advanced QAOA variants with tailored mixer Hamiltonians at depth p=2 achieved approximation ratios >0.9 under ideal simulation conditions, surpassing the classical Goemans–Williamson bound (~0.878) — [[2025_Benamer_VariationalQuantumAlgorithms]]
- [supported] Quantum Neural Networks (QNNs) achieved 94.3% classification accuracy in thoracic CT scans, 8.2% higher than classical CNNs, with 60% fewer parameters — [[2025_Benamer_VariationalQuantumAlgorithms]]

## Methodologies Used

| Method | Papers |
|--------|--------|
| variational | 19 |
| quantum-ML | 17 |
| classical-simulation | 15 |
| quantum-simulation | 14 |
| QAOA | 10 |
| VQE | 8 |
| grover | 6 |
| amplitude-estimation | 6 |
| HHL | 5 |
| quantum-annealing | 5 |
| quantum-SVM | 4 |
| QUBO | 4 |
| quantum-walk | 2 |
| hybrid-approach | 1 |

## Open Questions

- How do quantum algorithms for financial services perform under real-world noise and decoherence conditions? — [[2026_DECCANINTERNATIONALACADEMICPUBLISHERS_QuantumComputingAlgorithms]]
- What are the specific hardware requirements (e.g., qubit count, error rates) for achieving quantum advantage in financial applications? — [[2026_DECCANINTERNATIONALACADEMICPUBLISHERS_QuantumComputingAlgorithms]]
- How do quantum approaches compare to state-of-the-art classical methods in terms of speed, accuracy, and cost for financial use cases? — [[2026_DECCANINTERNATIONALACADEMICPUBLISHERS_QuantumComputingAlgorithms]]
- What are the data preprocessing and encoding challenges for applying quantum algorithms to real financial datasets? — [[2026_DECCANINTERNATIONALACADEMICPUBLISHERS_QuantumComputingAlgorithms]]
- How can hybrid quantum-classical frameworks be optimized for financial services applications? — [[2026_DECCANINTERNATIONALACADEMICPUBLISHERS_QuantumComputingAlgorithms]]
- What are the limitations of current quantum cloud platforms for deploying financial algorithms at scale? — [[2026_DECCANINTERNATIONALACADEMICPUBLISHERS_QuantumComputingAlgorithms]]
- Conduct empirical studies to validate the performance of quantum algorithms in financial services on real hardware — [[2026_DECCANINTERNATIONALACADEMICPUBLISHERS_QuantumComputingAlgorithms]]
- Develop noise-resilient quantum algorithms tailored for financial optimization and risk analysis — [[2026_DECCANINTERNATIONALACADEMICPUBLISHERS_QuantumComputingAlgorithms]]
- Explore hybrid quantum-classical approaches for near-term financial applications — [[2026_DECCANINTERNATIONALACADEMICPUBLISHERS_QuantumComputingAlgorithms]]
- Investigate the scalability of quantum algorithms for large-scale financial datasets — [[2026_DECCANINTERNATIONALACADEMICPUBLISHERS_QuantumComputingAlgorithms]]
