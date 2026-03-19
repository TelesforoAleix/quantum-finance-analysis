# Quantum Annealing

**Papers:** 14 | **Empirical:** 1 | **Theoretical:** 2 | **Review:** 3

## Papers

| Paper | Year | Source Type | Topics | QA Claim | Relevance |
|-------|------|-------------|--------|----------|-----------|
| [[2026_Azfar_ShallowRobustQaoa]] | 2026 | preprint | portfolio-optimisation, high-frequency-trading | speculative | medium |
| [[2026_Gnal_ScenarioBasedMacroeconomic]] | 2026 | peer-reviewed-theoretical | risk-modelling, market-simulation, regulatory-compliance | theoretical | high |
| [[2024_Ghysels_QuantumFinance]] | 2025 | other | portfolio-optimisation, asset-pricing, risk-modelling, derivatives-pricing | speculative | high |
| [[2025_Benamer_VariationalQuantumAlgorithms]] | 2025 | preprint | portfolio-optimisation, risk-modelling, derivatives-pricing, asset-pricing, quantum-ML, market-simulation | speculative | high |
| [[2025_Berkowitz_QuantumComputingMeets]] | 2025 | other | portfolio-optimisation, asset-pricing, derivatives-pricing, risk-modelling, credit-scoring | speculative | high |
| [[2025_Jiang_RasenganTransitionHamiltonian]] | 2025 | conference-paper | portfolio-optimisation, risk-modelling, derivatives-pricing, fraud-detection, credit-scoring, high-frequency-trading | speculative | high |
| [[2025_Vangibhuratha_QuantumMachineLearning]] | 2025 | peer-reviewed-theoretical | portfolio-optimisation, risk-modelling, fraud-detection, asset-pricing, high-frequency-trading, quantum-cryptography | theoretical | high |
| [[2026_Mahmod_StateQuantumComputing]] | 2025 | review-article | portfolio-optimisation, risk-modelling, derivatives-pricing, fraud-detection, credit-scoring, high-frequency-trading, asset-pricing, quantum-cryptography, regulatory-compliance, market-simulation | speculative | high |
| [[2023_Fernandes_SystematicLiteratureReview]] | 2023 | review-article | portfolio-optimisation, risk-modelling | speculative | high |
| [[2023_Giron_ApproachingCollateralOptimization]] | 2023 | peer-reviewed-empirical | portfolio-optimisation | speculative | high |
| [[2023_Markna_UnveilingAdvancedComputational]] | 2023 | review-article | portfolio-optimisation, risk-modelling, derivatives-pricing, quantum-cryptography, market-simulation | speculative | high |
| [[2023_Shan_QuantumComputingSimulated]] | 2023 | conference-paper | portfolio-optimisation | speculative | high |
| [[2020_Kommadi_QuantumComputingSolutions]] | 2020 | technical-report | portfolio-optimisation, risk-modelling, fraud-detection, credit-scoring, quantum-cryptography, high-frequency-trading, regulatory-compliance | speculative | medium |
| [[2012_Dickson_AlgorithmicApproachAdiabatic]] | 2011 | preprint | portfolio-optimisation | speculative | medium |

## Topics Using This Method

| Topic | Papers |
|-------|--------|
| portfolio-optimisation | 13 |
| risk-modelling | 10 |
| derivatives-pricing | 6 |
| high-frequency-trading | 5 |
| asset-pricing | 5 |
| market-simulation | 4 |
| credit-scoring | 4 |
| fraud-detection | 4 |
| quantum-cryptography | 4 |
| regulatory-compliance | 3 |
| quantum-ML | 1 |

## Key Findings

- [supported] Linear-Ramp LC-QAOA improves convergence and feasibility compared to standard QAOA, Two-Step QAOA, and Grover-Mixer QAOA in noiseless and shot-based simulations on small VRP instances. — [[2026_Azfar_ShallowRobustQaoa]]
- [supported] Linear-Chain (LC) QAOA reduces two-qubit gate depth and boosts noise robustness, achieving the shallowest circuits on IBM Eagle/Heron hardware. — [[2026_Azfar_ShallowRobustQaoa]]
- [supported] On real hardware (IBM Eagle/Heron), LC-QAOA with XpXm dynamical decoupling more than doubles feasibility (from <1% to >2%) and recovers the optimal VRP solution in several trials. — [[2026_Azfar_ShallowRobustQaoa]]
- [supported] Grover-Mixer QAOA and Two-Step QAOA show high feasibility in simulation (e.g., 21% for GM-QAOA at p=8) but are hampered by deeper circuits, making them less effective on real hardware. — [[2026_Azfar_ShallowRobustQaoa]]
- [supported] Linear-ramp initialization (LRI-QAOA) concentrates probability on feasible solutions, outperforming random initialization in simulations (e.g., 47.6% feasibility vs. 2% for standard QAOA at p=8). — [[2026_Azfar_ShallowRobustQaoa]]
- [supported] Dynamical decoupling (XpXm) improves hardware performance (e.g., optimal solution rank improved from 235 to 15 on IBM Rensselaer), while heavier error mitigation (e.g., ZNE, Pauli twirling) degrades performance due to circuit distortion. — [[2026_Azfar_ShallowRobustQaoa]]
- [supported] LC-QAOA scales efficiently to larger VRP instances (30 qubits), reliably recovering the optimal route at depths p>16 on both IBM Eagle and Heron, with higher success on lower-error devices. — [[2026_Azfar_ShallowRobustQaoa]]
- [supported] CVaR (Conditional Value at Risk) objective improves optimization by biasing search toward high-quality solutions, enabling reliable performance at larger scales. — [[2026_Azfar_ShallowRobustQaoa]]
- [supported] Current quantum hardware limitations (noise, limited qubit counts, error propagation) constrain the scalability and reliability of quantum-enhanced forecasting models in the NISQ era — [[2026_Gnal_ScenarioBasedMacroeconomic]]
- [supported] Integrating quantum outputs into established econometric frameworks requires methodological transparency and interpretability to ensure policy relevance — [[2026_Gnal_ScenarioBasedMacroeconomic]]
- [supported] MIDAS (mixed-data sampling) methods are regression-based techniques for combining data at different frequencies in econometrics — [[2024_Ghysels_QuantumFinance]]
- [supported] VQE achieved chemical accuracy (< 1.6 mHa) for small molecules like H2, LiH, and BeH2 using hardware-efficient ansätze on superconducting qubits — [[2025_Benamer_VariationalQuantumAlgorithms]]
- [supported] VQE demonstrated a dissociation energy error of (8 ± 5) × 10^-4 Hartree for H2, within chemical accuracy — [[2025_Benamer_VariationalQuantumAlgorithms]]
- [supported] QAOA on 20-node Max-Cut problems achieved an approximation ratio of ~0.755 at depth p=1, outperforming random guessing (0.5) — [[2025_Benamer_VariationalQuantumAlgorithms]]
- [supported] Advanced QAOA variants with tailored mixer Hamiltonians at depth p=2 achieved approximation ratios >0.9 under ideal simulation conditions, surpassing the classical Goemans–Williamson bound (~0.878) — [[2025_Benamer_VariationalQuantumAlgorithms]]
- [supported] Quantum Neural Networks (QNNs) achieved 94.3% classification accuracy in thoracic CT scans, 8.2% higher than classical CNNs, with 60% fewer parameters — [[2025_Benamer_VariationalQuantumAlgorithms]]
- [supported] QNNs in quantum portfolio optimization attained 30% improved Sharpe ratios relative to classical Markowitz models — [[2025_Benamer_VariationalQuantumAlgorithms]]
- [supported] QNNs reduced Value-at-Risk calculation time from hours to minutes for derivative portfolios with >500 assets — [[2025_Benamer_VariationalQuantumAlgorithms]]
- [supported] QAOA solved Markowitz’s mean-variance optimization problem for n=20 assets using 6 qubits, achieving solutions within 92% of classical benchmarks — [[2025_Benamer_VariationalQuantumAlgorithms]]
- [supported] Variational quantum circuits for Value-at-Risk (VaR) calculations reduced calculation variance by 40% compared to classical Monte Carlo methods — [[2025_Benamer_VariationalQuantumAlgorithms]]
