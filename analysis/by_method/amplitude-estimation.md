# Amplitude Estimation

**Papers:** 16 | **Empirical:** 4 | **Theoretical:** 4 | **Review:** 1

## Papers

| Paper | Year | Source Type | Topics | QA Claim | Relevance |
|-------|------|-------------|--------|----------|-----------|
| [[2026_Barbaresco_QuantumAmplitudeEstimation]] | 2026 | peer-reviewed-empirical | derivatives-pricing | disputed | high |
| [[2026_Gnal_ScenarioBasedMacroeconomic]] | 2026 | peer-reviewed-theoretical | risk-modelling, market-simulation, regulatory-compliance | theoretical | high |
| [[2026_Prasad_QuantumAlgorithmsStochastic]] | 2026 | preprint | derivatives-pricing, risk-modelling, asset-pricing, market-simulation | speculative | high |
| [[2025_Benamer_VariationalQuantumAlgorithms]] | 2025 | preprint | portfolio-optimisation, risk-modelling, derivatives-pricing, asset-pricing, quantum-ML, market-simulation | speculative | high |
| [[2025_Cibrario_AutocallableOptionsPricing]] | 2025 | conference-paper | derivatives-pricing | speculative | high |
| [[2025_Hlatshwayo_TechnicalReviewQuantum]] | 2025 | preprint | portfolio-optimisation, risk-modelling, derivatives-pricing, fraud-detection, credit-scoring, high-frequency-trading, asset-pricing, quantum-cryptography, market-simulation | speculative | high |
| [[2025_JETIR_QuantumFinance]] | 2025 | peer-reviewed-theoretical | portfolio-optimisation, risk-modelling, derivatives-pricing, fraud-detection, asset-pricing, market-simulation | theoretical | high |
| [[2025_NeelotpalDey_QuantumComputingFinancial]] | 2025 | peer-reviewed-theoretical | portfolio-optimisation, risk-modelling, derivatives-pricing, fraud-detection, asset-pricing, quantum-cryptography | speculative | high |
| [[2025_ThirumalGunasekaran_ExploringRevolutionaryPotential]] | 2025 | peer-reviewed-theoretical | portfolio-optimisation, risk-modelling, derivatives-pricing, fraud-detection, credit-scoring, quantum-cryptography, regulatory-compliance, market-simulation | theoretical | high |
| [[2024_KI_QuantumFinance]] | 2024 | peer-reviewed-empirical | portfolio-optimisation, asset-pricing | theoretical | high |
| [[2023_Markna_UnveilingAdvancedComputational]] | 2023 | review-article | portfolio-optimisation, risk-modelling, derivatives-pricing, quantum-cryptography, market-simulation | speculative | high |
| [[2021_Stamatopoulos_TowardsQuantumAdvantage]] | 2022 | peer-reviewed-empirical | risk-modelling, derivatives-pricing | theoretical | high |
| [[2022_Doriguello_QuantumAlgorithmStochastic]] | 2022 | conference-paper | derivatives-pricing, risk-modelling | theoretical | high |
| [[2022_Saha_IntermediateQutritBased]] | 2022 | peer-reviewed-empirical | derivatives-pricing | theoretical | high |
| [[2020_Miyamoto_ReductionQubitsQuantum]] | 2020 | preprint | risk-modelling, derivatives-pricing | theoretical | high |
| [[2018_Rebentrost_QuantumComputationalFinance]] | 2018 | preprint | derivatives-pricing | theoretical | high |

## Topics Using This Method

| Topic | Papers |
|-------|--------|
| derivatives-pricing | 14 |
| risk-modelling | 11 |
| market-simulation | 7 |
| portfolio-optimisation | 7 |
| asset-pricing | 6 |
| fraud-detection | 4 |
| quantum-cryptography | 4 |
| regulatory-compliance | 2 |
| credit-scoring | 2 |
| quantum-ML | 1 |
| high-frequency-trading | 1 |

## Key Findings

- [supported] Quantum Amplitude Estimation (QAE) variants (IAE and MLAE) returned an expected payoff of zero for European call options, while classical methods (Black-Scholes and Monte Carlo) yielded significantly positive values ($17.60 and $17.06 in two scenarios). — [[2026_Barbaresco_QuantumAmplitudeEstimation]]
- [supported] The failure of QAE to capture non-zero expected payoffs is attributed to limited resolution from 6 uncertainty qubits (64 bins), which inadequately encodes small-amplitude, in-the-money price regions. — [[2026_Barbaresco_QuantumAmplitudeEstimation]]
- [supported] Quantum circuits correctly identified the realized market outcome (zero payoff) but failed to capture the full expectation implied by the distribution tail. — [[2026_Barbaresco_QuantumAmplitudeEstimation]]
- [supported] Classical benchmarks (Black-Scholes and Monte Carlo) aligned closely, with Monte Carlo deviations below 1% from analytical values. — [[2026_Barbaresco_QuantumAmplitudeEstimation]]
- [supported] Quantum estimates for asset prices were lower than classical benchmarks ($185 vs. $198 in 2023–2024; $179 vs. $192 in 2022–2023), further highlighting resolution limitations. — [[2026_Barbaresco_QuantumAmplitudeEstimation]]
- [supported] Current quantum hardware limitations (noise, limited qubit counts, error propagation) constrain the scalability and reliability of quantum-enhanced forecasting models in the NISQ era — [[2026_Gnal_ScenarioBasedMacroeconomic]]
- [supported] Integrating quantum outputs into established econometric frameworks requires methodological transparency and interpretability to ensure policy relevance — [[2026_Gnal_ScenarioBasedMacroeconomic]]
- [supported] For linear and semilinear SDEs with Lipschitz coefficients, quantum algorithms can estimate relevant quantities (option prices, expected hitting times, moments) to accuracy ε in time ˜O(poly(d) polylog(1/ε)), versus classical O(poly(d)/ε²) — [[2026_Prasad_QuantumAlgorithmsStochastic]]
- [supported] Numerical simulations on small instances (e.g., 2D Black-Scholes with 10 qubits) demonstrate polynomial-to-super-polynomial empirical speedups in accuracy for fixed runtime — [[2026_Prasad_QuantumAlgorithmsStochastic]]
- [supported] Theorem 1 proves a quantum complexity of ˜O(poly(d) polylog(1/ε)) for estimating expectations in linear SDEs, compared to classical O(poly(d)/ε²) — [[2026_Prasad_QuantumAlgorithmsStochastic]]
- [supported] Theorem 2 shows quantum simulation of Fokker-Planck PDEs achieves accuracy ε in time ˜O(d·log(1/ε)), versus classical O(n^(d+1)) for spatial grid size n — [[2026_Prasad_QuantumAlgorithmsStochastic]]
- [supported] Simulated quantum algorithms for 2D Black-Scholes show ~3x speedup over classical Monte Carlo for 0.1% accuracy, with estimated 10-20x speedup on real hardware — [[2026_Prasad_QuantumAlgorithmsStochastic]]
- [supported] Quantum simulation of Langevin dynamics for 3D coarse-grained systems shows ~100x speedup in sampling rare events due to superposition over trajectories — [[2026_Prasad_QuantumAlgorithmsStochastic]]
- [supported] VQE achieved chemical accuracy (< 1.6 mHa) for small molecules like H2, LiH, and BeH2 using hardware-efficient ansätze on superconducting qubits — [[2025_Benamer_VariationalQuantumAlgorithms]]
- [supported] VQE demonstrated a dissociation energy error of (8 ± 5) × 10^-4 Hartree for H2, within chemical accuracy — [[2025_Benamer_VariationalQuantumAlgorithms]]
- [supported] QAOA on 20-node Max-Cut problems achieved an approximation ratio of ~0.755 at depth p=1, outperforming random guessing (0.5) — [[2025_Benamer_VariationalQuantumAlgorithms]]
- [supported] Advanced QAOA variants with tailored mixer Hamiltonians at depth p=2 achieved approximation ratios >0.9 under ideal simulation conditions, surpassing the classical Goemans–Williamson bound (~0.878) — [[2025_Benamer_VariationalQuantumAlgorithms]]
- [supported] Quantum Neural Networks (QNNs) achieved 94.3% classification accuracy in thoracic CT scans, 8.2% higher than classical CNNs, with 60% fewer parameters — [[2025_Benamer_VariationalQuantumAlgorithms]]
- [supported] QNNs in quantum portfolio optimization attained 30% improved Sharpe ratios relative to classical Markowitz models — [[2025_Benamer_VariationalQuantumAlgorithms]]
- [supported] QNNs reduced Value-at-Risk calculation time from hours to minutes for derivative portfolios with >500 assets — [[2025_Benamer_VariationalQuantumAlgorithms]]
