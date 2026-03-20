# VQE

**Papers:** 16 | **Empirical:** 4 | **Theoretical:** 3 | **Review:** 2

## Papers

| Paper | Year | Source Type | Topics | QA Claim | Relevance |
|-------|------|-------------|--------|----------|-----------|
| [[2026_Barbaresco_QPortQuantum]] | 2026 | conference-paper | portfolio-optimisation | speculative | high |
| [[2026_Dechant_ErrorResourceEstimates]] | 2026 | preprint | derivatives-pricing, asset-pricing | speculative | high |
| [[2026_Nawaz_ExploringQuantumMachine]] | 2026 | peer-reviewed-theoretical | portfolio-optimisation, risk-modelling, derivatives-pricing, fraud-detection, credit-scoring, high-frequency-trading, asset-pricing, quantum-cryptography | theoretical | high |
| [[2025_Benamer_VariationalQuantumAlgorithms]] | 2025 | preprint | portfolio-optimisation, risk-modelling, derivatives-pricing, asset-pricing, market-simulation | speculative | high |
| [[2025_Gibadullin_QuantumAlgorithmsSolving]] | 2025 | conference-paper | portfolio-optimisation, risk-modelling, high-frequency-trading | speculative | medium |
| [[2025_Innan_QuantumPortfolioOptimization]] | 2025 | conference-paper | portfolio-optimisation | speculative | high |
| [[2025_JETIR_QuantumFinance]] | 2025 | peer-reviewed-theoretical | portfolio-optimisation, risk-modelling, derivatives-pricing, fraud-detection, credit-scoring, high-frequency-trading, quantum-cryptography | theoretical | high |
| [[2025_Jiang_RasenganTransitionHamiltonian]] | 2025 | conference-paper | portfolio-optimisation, risk-modelling, derivatives-pricing, fraud-detection, credit-scoring, high-frequency-trading | theoretical | high |
| [[2025_NeelotpalDey_QuantumComputingFinancial]] | 2025 | peer-reviewed-theoretical | portfolio-optimisation, risk-modelling, derivatives-pricing, fraud-detection, credit-scoring, high-frequency-trading, quantum-cryptography, regulatory-compliance, market-simulation | theoretical | high |
| [[2025_Springer_QuantumFinance]] | 2025 | conference-paper | asset-pricing, portfolio-optimisation, risk-modelling | speculative | medium |
| [[2026_Mahmod_StateQuantumComputing]] | 2025 | review-article | portfolio-optimisation, risk-modelling, derivatives-pricing, fraud-detection, credit-scoring, high-frequency-trading, asset-pricing, quantum-cryptography, regulatory-compliance, market-simulation | theoretical | high |
| [[2025_Deshmukh_QuantumMachineLearning]] | 2024 | peer-reviewed-empirical | fraud-detection, credit-scoring, portfolio-optimisation, risk-modelling, high-frequency-trading, quantum-cryptography | speculative | high |
| [[2023_Fernandes_SystematicLiteratureReview]] | 2023 | review-article | portfolio-optimisation | speculative | high |
| [[2023_Vishwakarma_QuantumComputingAlgorithms]] | 2023 | peer-reviewed-empirical | portfolio-optimisation, risk-modelling, asset-pricing, high-frequency-trading | speculative | high |
| [[2021_Kolotouros_EvolvingObjectiveFunction]] | 2022 | peer-reviewed-empirical | portfolio-optimisation, risk-modelling | speculative | high |
| [[2022_Kolotouros_EvolvingObjectiveFunction]] | 2022 | peer-reviewed-empirical | portfolio-optimisation, risk-modelling | speculative | high |

## Topics Using This Method

| Topic | Papers |
|-------|--------|
| portfolio-optimisation | 15 |
| risk-modelling | 12 |
| high-frequency-trading | 8 |
| derivatives-pricing | 7 |
| asset-pricing | 6 |
| fraud-detection | 6 |
| credit-scoring | 6 |
| quantum-cryptography | 5 |
| market-simulation | 3 |
| regulatory-compliance | 2 |

## Key Findings

- [supported] Multi-qubit representations per stock yield negligible precision gains compared to classical Mean-Variance Optimization (MVO), indicating limited practical benefit — [[2026_Barbaresco_QPortQuantum]]
- [supported] Multi-stock encodings per qubit significantly improve efficiency with minimal precision loss, enabling more scalable quantum portfolio optimization under NISQ-era limitations — [[2026_Barbaresco_QPortQuantum]]
- [supported] QAOA consistently ranks the optimal portfolio solution higher than VQE, particularly at lower circuit depths, across both multi-qubit and multi-stock encoding strategies — [[2026_Barbaresco_QPortQuantum]]
- [supported] Increasing circuit repetitions (layers) generally improves alignment between quantum and classical solutions, with QAOA showing better resilience to compressed encodings than VQE — [[2026_Barbaresco_QPortQuantum]]
- [supported] For 3-stock and 4-stock portfolios, QAOA achieves near-optimal rankings (top positions) even at low circuit depths, while VQE requires deeper circuits to converge — [[2026_Barbaresco_QPortQuantum]]
- [supported] Encoding 2-3 stocks per qubit maintains competitive rankings for QAOA, though VQE exhibits increased variance under aggressive compression — [[2026_Barbaresco_QPortQuantum]]
- [supported] The paper provides rigorous error and resource estimates for variational quantum algorithms (VQAs) solving differential equations (DEs) using Runge-Kutta methods (RKMs), accounting for truncation errors and shot noise in quantum measurements. — [[2026_Dechant_ErrorResourceEstimates]]
- [supported] Higher-order RKMs (e.g., order 4 for a 1D ODE and order 2 for option pricing via the Black-Scholes equation) minimize the total number of quantum circuit evaluations required to achieve a target error. — [[2026_Dechant_ErrorResourceEstimates]]
- [supported] The total error in VQAs for solving DEs is bounded by the sum of the parameter error (from RKM approximations) and the representation error (from the quantum Ansatz), with the former analyzed in detail. — [[2026_Dechant_ErrorResourceEstimates]]
- [supported] The minimal number of RKM time steps and measurements per function evaluation is derived for both noiseless and shot-noise scenarios, providing a framework for optimizing quantum resource usage. — [[2026_Dechant_ErrorResourceEstimates]]
- [supported] The paper demonstrates that the variational quantum algorithm can solve both ordinary and partial differential equations (e.g., Black-Scholes equation) by mapping them to imaginary-time Schrödinger equations. — [[2026_Dechant_ErrorResourceEstimates]]
- [supported] The total number of quantum circuit evaluations scales quadratically with the number of variational parameters (NV), highlighting the resource-intensive nature of VQAs for large-scale problems. — [[2026_Dechant_ErrorResourceEstimates]]
- [supported] The study provides a unified comparative framework for QML algorithms, highlighting their optimization capabilities, practical feasibility, and limitations within a single analytical structure — [[2026_Nawaz_ExploringQuantumMachine]]
- [supported] Key challenges hindering real-world deployment of QML include quantum noise, scalability constraints, hardware limitations, and algorithmic performance trade-offs — [[2026_Nawaz_ExploringQuantumMachine]]
- [supported] VQE achieved chemical accuracy (< 1.6 mHa) for small molecules like H2, LiH, and BeH2 using hardware-efficient ansätze on superconducting qubits — [[2025_Benamer_VariationalQuantumAlgorithms]]
- [supported] QAOA on 20-node Max-Cut problems achieved an approximation ratio of ~0.755 at depth p=1, outperforming random guessing (0.5) — [[2025_Benamer_VariationalQuantumAlgorithms]]
- [supported] Advanced QAOA variants with tailored mixer Hamiltonians at depth p=2 achieved approximation ratios >0.9 under ideal simulation conditions, surpassing the classical Goemans–Williamson bound (~0.878) — [[2025_Benamer_VariationalQuantumAlgorithms]]
- [supported] Quantum Neural Networks (QNNs) achieved 94.3% classification accuracy in thoracic CT scans, 8.2% higher than classical CNNs, with 60% fewer parameters — [[2025_Benamer_VariationalQuantumAlgorithms]]
- [supported] QNNs in quantum portfolio optimization attained 30% improved Sharpe ratios compared to classical Markowitz models — [[2025_Benamer_VariationalQuantumAlgorithms]]
- [supported] QAOA solved Markowitz’s mean-variance optimization problem for n=20 assets using 6 qubits, achieving solutions within 92% of classical benchmarks — [[2025_Benamer_VariationalQuantumAlgorithms]]
