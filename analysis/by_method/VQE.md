# VQE

**Papers:** 16 | **Empirical:** 6 | **Theoretical:** 3 | **Review:** 2

## Papers

| Paper | Year | Source Type | Topics | QA Claim | Relevance |
|-------|------|-------------|--------|----------|-----------|
| [[2026_Barbaresco_QPortQuantum]] | 2026 | peer-reviewed-empirical | portfolio-optimisation | speculative | high |
| [[2026_Dechant_ErrorResourceEstimates]] | 2026 | preprint | derivatives-pricing, asset-pricing | speculative | high |
| [[2026_Nawaz_ExploringQuantumMachine]] | 2026 | peer-reviewed-theoretical | portfolio-optimisation, risk-modelling, derivatives-pricing, fraud-detection, credit-scoring, high-frequency-trading, asset-pricing, quantum-cryptography, regulatory-compliance, market-simulation | theoretical | high |
| [[2025_Benamer_VariationalQuantumAlgorithms]] | 2025 | preprint | portfolio-optimisation, risk-modelling, derivatives-pricing, asset-pricing, quantum-ML, market-simulation | speculative | high |
| [[2025_Gibadullin_QuantumAlgorithmsSolving]] | 2025 | conference-paper | portfolio-optimisation, risk-modelling, high-frequency-trading | speculative | medium |
| [[2025_Innan_QuantumPortfolioOptimization]] | 2025 | conference-paper | portfolio-optimisation | speculative | high |
| [[2025_JETIR_QuantumFinance]] | 2025 | peer-reviewed-theoretical | portfolio-optimisation, risk-modelling, derivatives-pricing, fraud-detection, asset-pricing, market-simulation | theoretical | high |
| [[2025_NeelotpalDey_QuantumComputingFinancial]] | 2025 | peer-reviewed-theoretical | portfolio-optimisation, risk-modelling, derivatives-pricing, fraud-detection, asset-pricing, quantum-cryptography | speculative | high |
| [[2025_Springer_QuantumFinance]] | 2025 | conference-paper | asset-pricing, portfolio-optimisation, risk-modelling | speculative | medium |
| [[2026_Mahmod_StateQuantumComputing]] | 2025 | review-article | portfolio-optimisation, risk-modelling, derivatives-pricing, fraud-detection, credit-scoring, high-frequency-trading, asset-pricing, quantum-cryptography, regulatory-compliance, market-simulation | speculative | high |
| [[2025_Deshmukh_QuantumMachineLearning]] | 2024 | peer-reviewed-empirical | portfolio-optimisation, risk-modelling, fraud-detection, credit-scoring, quantum-cryptography, market-simulation | speculative | high |
| [[2023_Fernandes_SystematicLiteratureReview]] | 2023 | review-article | portfolio-optimisation, risk-modelling | speculative | high |
| [[2023_Vishwakarma_QuantumComputingAlgorithms]] | 2023 | peer-reviewed-empirical | portfolio-optimisation, risk-modelling, asset-pricing, high-frequency-trading | speculative | high |
| [[2021_Kolotouros_EvolvingObjectiveFunction]] | 2022 | peer-reviewed-empirical | portfolio-optimisation, risk-modelling | speculative | high |
| [[2022_Kolotouros_EvolvingObjectiveFunction]] | 2022 | peer-reviewed-empirical | portfolio-optimisation, risk-modelling | speculative | high |
| [[2022_Saha_IntermediateQutritBased]] | 2022 | peer-reviewed-empirical | derivatives-pricing | theoretical | high |

## Topics Using This Method

| Topic | Papers |
|-------|--------|
| portfolio-optimisation | 14 |
| risk-modelling | 12 |
| asset-pricing | 8 |
| derivatives-pricing | 7 |
| fraud-detection | 5 |
| market-simulation | 5 |
| high-frequency-trading | 4 |
| quantum-cryptography | 4 |
| credit-scoring | 3 |
| regulatory-compliance | 2 |
| quantum-ML | 1 |

## Key Findings

- [supported] Increasing qubits per stock offers negligible precision gains compared to classical Mean-Variance Optimization (MVO) in quantum portfolio optimization, as demonstrated in simulations with 3-stock and 4-stock configurations using QAOA and VQE. — [[2026_Barbaresco_QPortQuantum]]
- [supported] Encoding multiple stocks per qubit significantly improves efficiency with minimal precision loss, enabling scalable quantum portfolio optimization under NISQ-era limitations, as shown in 12-stock experiments. — [[2026_Barbaresco_QPortQuantum]]
- [supported] QAOA consistently ranks the classically optimal MVO solution higher than VQE, particularly at lower circuit depths, across both multi-qubit and multi-stock encoding strategies. — [[2026_Barbaresco_QPortQuantum]]
- [supported] Multi-qubit representations per stock (2-3 qubits) degrade solution quality unless accompanied by deeper circuits, increasing resource demands without proportional performance benefits. — [[2026_Barbaresco_QPortQuantum]]
- [supported] Multi-stock encoding per qubit (2-3 stocks) maintains competitive rankings of the MVO-optimal solution, especially with QAOA and deeper circuits, despite reduced qubit usage. — [[2026_Barbaresco_QPortQuantum]]
- [supported] The paper provides rigorous error and resource estimates for variational quantum algorithms (VQAs) solving differential equations (DEs) using Runge-Kutta methods (RKMs), accounting for truncation errors and shot noise in quantum measurements. — [[2026_Dechant_ErrorResourceEstimates]]
- [supported] Higher-order RKMs (e.g., order 4 for a 1D ODE and order 2 for option pricing via the Black-Scholes equation) minimize the total number of quantum circuit evaluations required to achieve a target error. — [[2026_Dechant_ErrorResourceEstimates]]
- [supported] The total error in VQAs for solving DEs is bounded by the sum of the parameter error (from RKM truncation and shot noise) and the representation error (from the quantum ansatz), with the former analyzed in detail. — [[2026_Dechant_ErrorResourceEstimates]]
- [supported] The number of quantum circuit evaluations scales quadratically with the number of variational parameters (NV), highlighting a significant resource bottleneck for large-scale problems. — [[2026_Dechant_ErrorResourceEstimates]]
- [supported] The paper derives analytical bounds for the local truncation error (LTE) of RKMs, showing that the LTE scales as O(Δτ^(p+1)) for a p-th order RKM, where Δτ is the time step size. — [[2026_Dechant_ErrorResourceEstimates]]
- [supported] The shot noise error in quantum measurements scales as O(1/√N_meas), where N_meas is the number of measurements, and the paper provides a framework to minimize this error for a given target accuracy. — [[2026_Dechant_ErrorResourceEstimates]]
- [supported] The study provides a unified comparative framework for QML optimization algorithms, highlighting their practical feasibility and identifying key research gaps hindering real-world deployment — [[2026_Nawaz_ExploringQuantumMachine]]
- [supported] Challenges such as quantum noise, scalability, and hardware limitations remain significant barriers to the practical deployment of QML algorithms — [[2026_Nawaz_ExploringQuantumMachine]]
- [supported] VQE achieved chemical accuracy (< 1.6 mHa) for small molecules like H2, LiH, and BeH2 using hardware-efficient ansätze on superconducting qubits — [[2025_Benamer_VariationalQuantumAlgorithms]]
- [supported] VQE demonstrated a dissociation energy error of (8 ± 5) × 10^-4 Hartree for H2, within chemical accuracy — [[2025_Benamer_VariationalQuantumAlgorithms]]
- [supported] QAOA on 20-node Max-Cut problems achieved an approximation ratio of ~0.755 at depth p=1, outperforming random guessing (0.5) — [[2025_Benamer_VariationalQuantumAlgorithms]]
- [supported] Advanced QAOA variants with tailored mixer Hamiltonians at depth p=2 achieved approximation ratios >0.9 under ideal simulation conditions, surpassing the classical Goemans–Williamson bound (~0.878) — [[2025_Benamer_VariationalQuantumAlgorithms]]
- [supported] Quantum Neural Networks (QNNs) achieved 94.3% classification accuracy in thoracic CT scans, 8.2% higher than classical CNNs, with 60% fewer parameters — [[2025_Benamer_VariationalQuantumAlgorithms]]
- [supported] QNNs in quantum portfolio optimization attained 30% improved Sharpe ratios relative to classical Markowitz models — [[2025_Benamer_VariationalQuantumAlgorithms]]
- [supported] QNNs reduced Value-at-Risk calculation time from hours to minutes for derivative portfolios with >500 assets — [[2025_Benamer_VariationalQuantumAlgorithms]]
