# Asset Pricing

**Papers:** 22 | **Empirical:** 3 | **Theoretical:** 2 | **Review:** 2

## Papers

| Paper | Year | Source Type | Methods | QA Claim | Relevance |
|-------|------|-------------|---------|----------|-----------|
| [[2026_DECCANINTERNATIONALACADEMICPUBLISHERS_QuantumComputingAlgorithms]] | 2026 | other | grover, variational, quantum-simulation, classical-simulation, quantum-ML | speculative | medium |
| [[2026_Dechant_ErrorResourceEstimates]] | 2026 | preprint | variational, VQE, quantum-simulation | speculative | high |
| [[2026_Nawaz_ExploringQuantumMachine]] | 2026 | peer-reviewed-theoretical | QAOA, VQE, quantum-ML, quantum-SVM, grover, variational, quantum-simulation | theoretical | high |
| [[2026_Prasad_QuantumAlgorithmsStochastic]] | 2026 | preprint | HHL, amplitude-estimation, quantum-simulation, variational, quantum-ML, classical-simulation | speculative | high |
| [[2024_Ghysels_QuantumFinance]] | 2025 | other | quantum-annealing, QUBO, quantum-simulation | speculative | high |
| [[2025_Benamer_VariationalQuantumAlgorithms]] | 2025 | preprint | VQE, QAOA, quantum-ML, variational, amplitude-estimation | speculative | high |
| [[2025_Berkowitz_QuantumComputingMeets]] | 2025 | other | quantum-annealing, QUBO | speculative | high |
| [[2025_Chaudhary_PracticalQuantumSolver]] | 2025 | conference-paper | variational, quantum-simulation, classical-simulation | theoretical | high |
| [[2025_Ganguly_HybridClassicalQuantum]] | 2025 | conference-paper | quantum-ML, variational, QUBO, classical-simulation | speculative | high |
| [[2025_Hlatshwayo_TechnicalReviewQuantum]] | 2025 | preprint | HHL, grover, quantum-walk, amplitude-estimation, quantum-simulation, quantum-ML | speculative | high |
| [[2025_Springer_QuantumFinance]] | 2025 | conference-paper | VQE, grover, QAOA, variational, quantum-simulation, classical-simulation | speculative | medium |
| [[2025_Vangibhuratha_QuantumMachineLearning]] | 2025 | peer-reviewed-theoretical | quantum-ML, quantum-SVM, variational, quantum-annealing, QAOA, HHL, quantum-simulation, classical-simulation | theoretical | high |
| [[2025_Vellaipandiyan_HybridQlstmFramework]] | 2025 | conference-paper | quantum-ML, variational | speculative | high |
| [[2026_Mahmod_StateQuantumComputing]] | 2025 | review-article | HHL, QAOA, VQE, quantum-annealing, grover, quantum-ML, quantum-SVM, variational, QUBO, quantum-simulation | theoretical | high |
| [[2023_Kobayashi_CrossSectionalStock]] | 2024 | preprint | quantum-ML, variational, classical-simulation | speculative | high |
| [[2024_M_OptimizingMutualFund]] | 2024 | conference-paper | quantum-ML, variational | speculative | medium |
| [[2024_Mustafa_QuantumGraphNeural]] | 2024 | conference-paper | quantum-ML, variational, classical-simulation | speculative | high |
| [[2023_Markna_UnveilingAdvancedComputational]] | 2023 | review-article | QAOA, quantum-annealing, HHL, quantum-ML, quantum-SVM, amplitude-estimation, QUBO, variational, grover, quantum-simulation, classical-simulation | speculative | high |
| [[2023_Vishwakarma_QuantumComputingAlgorithms]] | 2023 | peer-reviewed-empirical | QAOA, VQE, variational, quantum-ML, hybrid-approach | speculative | high |
| [[2022_Zhao_QuantumInspiredVariational]] | 2022 | peer-reviewed-empirical | variational, quantum-ML, quantum-simulation, classical-simulation | theoretical | high |
| [[2021_Martin_TowardPricingFinancial]] | 2021 | peer-reviewed-empirical | quantum-simulation, quantum-ML, variational, classical-simulation | speculative | high |
| [[2020_Kommadi_QuantumComputingSolutions]] | 2020 | technical-report | QAOA, grover, quantum-ML, quantum-SVM, quantum-annealing, variational, quantum-walk, quantum-simulation, classical-simulation | speculative | high |

## Key Findings

- [supported] The paper provides rigorous error and resource estimates for variational quantum algorithms (VQAs) solving differential equations (DEs) using Runge-Kutta methods (RKMs), accounting for truncation errors and shot noise in quantum measurements. — [[2026_Dechant_ErrorResourceEstimates]]
- [supported] Higher-order RKMs (e.g., order 4 for a 1D ODE and order 2 for option pricing via the Black-Scholes equation) minimize the total number of quantum circuit evaluations required to achieve a target error. — [[2026_Dechant_ErrorResourceEstimates]]
- [supported] The total error in VQAs for solving DEs is bounded by the sum of the parameter error (from RKM approximations) and the representation error (from the quantum Ansatz), with the former analyzed in detail. — [[2026_Dechant_ErrorResourceEstimates]]
- [supported] The minimal number of RKM time steps and measurements per function evaluation is derived for both noiseless and shot-noise scenarios, providing a framework for optimizing quantum resource usage. — [[2026_Dechant_ErrorResourceEstimates]]
- [supported] The paper demonstrates that the variational quantum algorithm can solve both ordinary and partial differential equations (e.g., Black-Scholes equation) by mapping them to imaginary-time Schrödinger equations. — [[2026_Dechant_ErrorResourceEstimates]]
- [supported] The total number of quantum circuit evaluations scales quadratically with the number of variational parameters (NV), highlighting the resource-intensive nature of VQAs for large-scale problems. — [[2026_Dechant_ErrorResourceEstimates]]
- [supported] The study provides a unified comparative framework for QML algorithms, highlighting their optimization capabilities, practical feasibility, and limitations within a single analytical structure — [[2026_Nawaz_ExploringQuantumMachine]]
- [supported] Key challenges hindering real-world deployment of QML include quantum noise, scalability constraints, hardware limitations, and algorithmic performance trade-offs — [[2026_Nawaz_ExploringQuantumMachine]]
- [supported] For linear and semilinear SDEs with Lipschitz coefficients, quantum algorithms estimate relevant quantities (option prices, expected hitting times, moments) to accuracy ε in time ˜O(poly(d)polylog(1/ε)), versus classical O(poly(d)/ε²). — [[2026_Prasad_QuantumAlgorithmsStochastic]]
- [supported] Quantum simulation of the Fokker-Planck equation achieves accuracy ε in time ˜O(d · log(1/ε)), compared to classical finite-difference solvers at O(n^{d+1}_s). — [[2026_Prasad_QuantumAlgorithmsStochastic]]
- [supported] Numerical simulations on small instances (e.g., 2D Black-Scholes, 3D Langevin) demonstrate polynomial-to-super-polynomial empirical speedups in accuracy for fixed runtime. — [[2026_Prasad_QuantumAlgorithmsStochastic]]
- [supported] Resource requirements for d-dimensional SDEs: ~150 qubits for d=10, ε=10⁻³, and δx=10⁻² in finance applications. — [[2026_Prasad_QuantumAlgorithmsStochastic]]
- [supported] Quantum annealing hardware is currently the most reliable scaled hardware for optimization tasks in finance — [[2024_Ghysels_QuantumFinance]]
- [supported] VQE achieved chemical accuracy (< 1.6 mHa) for small molecules like H2, LiH, and BeH2 using hardware-efficient ansätze on superconducting qubits — [[2025_Benamer_VariationalQuantumAlgorithms]]
- [supported] QAOA on 20-node Max-Cut problems achieved an approximation ratio of ~0.755 at depth p=1, outperforming random guessing (0.5) — [[2025_Benamer_VariationalQuantumAlgorithms]]
- [supported] Advanced QAOA variants with tailored mixer Hamiltonians at depth p=2 achieved approximation ratios >0.9 under ideal simulation conditions, surpassing the classical Goemans–Williamson bound (~0.878) — [[2025_Benamer_VariationalQuantumAlgorithms]]
- [supported] Quantum Neural Networks (QNNs) achieved 94.3% classification accuracy in thoracic CT scans, 8.2% higher than classical CNNs, with 60% fewer parameters — [[2025_Benamer_VariationalQuantumAlgorithms]]
- [supported] QNNs in quantum portfolio optimization attained 30% improved Sharpe ratios compared to classical Markowitz models — [[2025_Benamer_VariationalQuantumAlgorithms]]
- [supported] QAOA solved Markowitz’s mean-variance optimization problem for n=20 assets using 6 qubits, achieving solutions within 92% of classical benchmarks — [[2025_Benamer_VariationalQuantumAlgorithms]]
- [supported] Variational quantum circuits for Value-at-Risk (VaR) calculations reduced calculation variance by 40% compared to classical Monte Carlo methods for up to 8 risk factors — [[2025_Benamer_VariationalQuantumAlgorithms]]

## Methodologies Used

| Method | Papers |
|--------|--------|
| variational | 19 |
| quantum-ML | 17 |
| quantum-simulation | 14 |
| classical-simulation | 12 |
| QAOA | 8 |
| grover | 7 |
| VQE | 6 |
| quantum-annealing | 6 |
| quantum-SVM | 5 |
| HHL | 5 |
| QUBO | 5 |
| amplitude-estimation | 4 |
| quantum-walk | 2 |
| hybrid-approach | 1 |

## Open Questions

- How can quantum algorithms for financial applications (e.g., portfolio optimization) be adapted to current NISQ devices with limited qubits and high noise? — [[2026_DECCANINTERNATIONALACADEMICPUBLISHERS_QuantumComputingAlgorithms]]
- What are the specific hardware requirements (qubit count, coherence time, gate fidelity) for quantum computing to achieve practical advantage in financial services? — [[2026_DECCANINTERNATIONALACADEMICPUBLISHERS_QuantumComputingAlgorithms]]
- How do quantum algorithms compare to state-of-the-art classical methods in terms of accuracy, speed, and scalability for real-world financial problems? — [[2026_DECCANINTERNATIONALACADEMICPUBLISHERS_QuantumComputingAlgorithms]]
- What are the most effective error mitigation strategies for quantum financial applications, and how do they impact solution quality? — [[2026_DECCANINTERNATIONALACADEMICPUBLISHERS_QuantumComputingAlgorithms]]
- How can hybrid quantum-classical approaches be optimized for financial use cases, and what are their limitations? — [[2026_DECCANINTERNATIONALACADEMICPUBLISHERS_QuantumComputingAlgorithms]]
- What are the potential risks and ethical considerations of deploying quantum computing in financial services (e.g., cryptography, fraud detection)? — [[2026_DECCANINTERNATIONALACADEMICPUBLISHERS_QuantumComputingAlgorithms]]
- Empirical validation of quantum algorithms on real quantum hardware for financial applications — [[2026_DECCANINTERNATIONALACADEMICPUBLISHERS_QuantumComputingAlgorithms]]
- Development of noise-resilient quantum algorithms tailored for NISQ devices in financial services — [[2026_DECCANINTERNATIONALACADEMICPUBLISHERS_QuantumComputingAlgorithms]]
- Benchmarking quantum solutions against classical methods for specific financial problems (e.g., option pricing, risk analysis) — [[2026_DECCANINTERNATIONALACADEMICPUBLISHERS_QuantumComputingAlgorithms]]
- Exploration of hybrid quantum-classical frameworks for large-scale financial datasets — [[2026_DECCANINTERNATIONALACADEMICPUBLISHERS_QuantumComputingAlgorithms]]
