# Amplitude Estimation

**Papers:** 13 | **Empirical:** 2 | **Theoretical:** 3 | **Review:** 1

## Papers

| Paper | Year | Source Type | Topics | QA Claim | Relevance |
|-------|------|-------------|--------|----------|-----------|
| [[2026_Barbaresco_QuantumAmplitudeEstimation]] | 2026 | peer-reviewed-empirical | derivatives-pricing | disputed | high |
| [[2026_Gnal_ScenarioBasedMacroeconomic]] | 2026 | peer-reviewed-theoretical | risk-modelling, market-simulation, regulatory-compliance | theoretical | high |
| [[2026_Prasad_QuantumAlgorithmsStochastic]] | 2026 | preprint | derivatives-pricing, asset-pricing, market-simulation | speculative | high |
| [[2025_Benamer_VariationalQuantumAlgorithms]] | 2025 | preprint | portfolio-optimisation, risk-modelling, derivatives-pricing, asset-pricing, market-simulation | speculative | high |
| [[2025_Cibrario_AutocallableOptionsPricing]] | 2025 | conference-paper | derivatives-pricing | speculative | high |
| [[2025_Hlatshwayo_TechnicalReviewQuantum]] | 2025 | preprint | portfolio-optimisation, risk-modelling, derivatives-pricing, fraud-detection, credit-scoring, high-frequency-trading, asset-pricing, quantum-cryptography, regulatory-compliance, market-simulation | speculative | high |
| [[2025_JETIR_QuantumFinance]] | 2025 | peer-reviewed-theoretical | portfolio-optimisation, risk-modelling, derivatives-pricing, fraud-detection, credit-scoring, high-frequency-trading, quantum-cryptography | theoretical | high |
| [[2025_NeelotpalDey_QuantumComputingFinancial]] | 2025 | peer-reviewed-theoretical | portfolio-optimisation, risk-modelling, derivatives-pricing, fraud-detection, credit-scoring, high-frequency-trading, quantum-cryptography, regulatory-compliance, market-simulation | theoretical | high |
| [[2023_Markna_UnveilingAdvancedComputational]] | 2023 | review-article | portfolio-optimisation, risk-modelling, derivatives-pricing, fraud-detection, credit-scoring, high-frequency-trading, asset-pricing, quantum-cryptography, regulatory-compliance, market-simulation | speculative | high |
| [[2021_Stamatopoulos_TowardsQuantumAdvantage]] | 2022 | peer-reviewed-empirical | derivatives-pricing, risk-modelling | theoretical | high |
| [[2022_Doriguello_QuantumAlgorithmStochastic]] | 2022 | conference-paper | derivatives-pricing, risk-modelling | theoretical | high |
| [[2020_Miyamoto_ReductionQubitsQuantum]] | 2020 | preprint | risk-modelling, derivatives-pricing | theoretical | high |
| [[2018_Rebentrost_QuantumComputationalFinance]] | 2018 | preprint | derivatives-pricing, risk-modelling | theoretical | high |

## Topics Using This Method

| Topic | Papers |
|-------|--------|
| derivatives-pricing | 12 |
| risk-modelling | 10 |
| market-simulation | 6 |
| portfolio-optimisation | 5 |
| regulatory-compliance | 4 |
| asset-pricing | 4 |
| fraud-detection | 4 |
| credit-scoring | 4 |
| high-frequency-trading | 4 |
| quantum-cryptography | 4 |

## Key Findings

- [supported] Quantum Amplitude Estimation (QAE) variants (IAE and MLAE) returned an expected payoff of zero for European call options, while classical methods (Black-Scholes and Monte Carlo) yielded significantly positive values ($17.60 and $17.06 in two scenarios). — [[2026_Barbaresco_QuantumAmplitudeEstimation]]
- [supported] The failure of QAE to capture non-zero expected payoffs is attributed to limited resolution from 6 uncertainty qubits (64 bins), which inadequately encode small-amplitude, in-the-money price regions. — [[2026_Barbaresco_QuantumAmplitudeEstimation]]
- [supported] Quantum methods correctly identified the realized market outcome (zero payoff) but failed to capture the full expectation implied by the distribution tail. — [[2026_Barbaresco_QuantumAmplitudeEstimation]]
- [supported] Classical benchmarks (Black-Scholes and Monte Carlo with 100,000 samples) showed <1% deviation from analytic values, confirming their accuracy for the same discretized price space. — [[2026_Barbaresco_QuantumAmplitudeEstimation]]
- [supported] Quantum estimates for terminal asset prices were lower than classical benchmarks ($185 vs. $198 in 2023–2024; $179 vs. $192 in 2022–2023), further highlighting resolution limitations. — [[2026_Barbaresco_QuantumAmplitudeEstimation]]
- [supported] Current quantum hardware limitations (noise, qubit counts, error propagation) constrain the scalability and reliability of quantum-enhanced forecasting models in the NISQ era — [[2026_Gnal_ScenarioBasedMacroeconomic]]
- [supported] Integrating quantum outputs into established econometric frameworks requires methodological transparency and interpretability to ensure policy relevance — [[2026_Gnal_ScenarioBasedMacroeconomic]]
- [supported] For linear and semilinear SDEs with Lipschitz coefficients, quantum algorithms estimate relevant quantities (option prices, expected hitting times, moments) to accuracy ε in time ˜O(poly(d)polylog(1/ε)), versus classical O(poly(d)/ε²). — [[2026_Prasad_QuantumAlgorithmsStochastic]]
- [supported] Quantum simulation of the Fokker-Planck equation achieves accuracy ε in time ˜O(d · log(1/ε)), compared to classical finite-difference solvers at O(n^{d+1}_s). — [[2026_Prasad_QuantumAlgorithmsStochastic]]
- [supported] Numerical simulations on small instances (e.g., 2D Black-Scholes, 3D Langevin) demonstrate polynomial-to-super-polynomial empirical speedups in accuracy for fixed runtime. — [[2026_Prasad_QuantumAlgorithmsStochastic]]
- [supported] Resource requirements for d-dimensional SDEs: ~150 qubits for d=10, ε=10⁻³, and δx=10⁻² in finance applications. — [[2026_Prasad_QuantumAlgorithmsStochastic]]
- [supported] VQE achieved chemical accuracy (< 1.6 mHa) for small molecules like H2, LiH, and BeH2 using hardware-efficient ansätze on superconducting qubits — [[2025_Benamer_VariationalQuantumAlgorithms]]
- [supported] QAOA on 20-node Max-Cut problems achieved an approximation ratio of ~0.755 at depth p=1, outperforming random guessing (0.5) — [[2025_Benamer_VariationalQuantumAlgorithms]]
- [supported] Advanced QAOA variants with tailored mixer Hamiltonians at depth p=2 achieved approximation ratios >0.9 under ideal simulation conditions, surpassing the classical Goemans–Williamson bound (~0.878) — [[2025_Benamer_VariationalQuantumAlgorithms]]
- [supported] Quantum Neural Networks (QNNs) achieved 94.3% classification accuracy in thoracic CT scans, 8.2% higher than classical CNNs, with 60% fewer parameters — [[2025_Benamer_VariationalQuantumAlgorithms]]
- [supported] QNNs in quantum portfolio optimization attained 30% improved Sharpe ratios compared to classical Markowitz models — [[2025_Benamer_VariationalQuantumAlgorithms]]
- [supported] QAOA solved Markowitz’s mean-variance optimization problem for n=20 assets using 6 qubits, achieving solutions within 92% of classical benchmarks — [[2025_Benamer_VariationalQuantumAlgorithms]]
- [supported] Variational quantum circuits for Value-at-Risk (VaR) calculations reduced calculation variance by 40% compared to classical Monte Carlo methods for up to 8 risk factors — [[2025_Benamer_VariationalQuantumAlgorithms]]
- [supported] Quantum generative models generated realistic option price distributions using 5-qubit circuits, capturing tail risk more accurately than standard Black-Scholes models — [[2025_Benamer_VariationalQuantumAlgorithms]]
- [supported] The proposed integration-based exponential amplitude loading technique reduces circuit depth compared to state-of-the-art approaches, achieving a ~50x reduction in T-depth for the payoff component relative to previous methods. — [[2025_Cibrario_AutocallableOptionsPricing]]
