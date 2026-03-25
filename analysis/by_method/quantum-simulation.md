# Quantum Simulation

**Papers:** 22 | **Empirical:** 3 | **Theoretical:** 6

## Papers

| Paper | Year | Source Type | Topics | QA Claim | Relevance |
|-------|------|-------------|--------|----------|-----------|
| [[2026_DECCANINTERNATIONALACADEMICPUBLISHERS_QuantumComputingAlgorithms]] | 2026 | other | — | speculative | low |
| [[2026_Prasad_QuantumAlgorithmsStochastic]] | 2026 | preprint | derivatives-pricing, asset-pricing, market-simulation | speculative | high |
| [[2024_Ghysels_QuantumFinance]] | 2025 | other | portfolio-optimisation, asset-pricing, risk-modelling, derivatives-pricing, credit-scoring | speculative | high |
| [[2024_Tancara_HighDimensionalCounterdiabatic]] | 2025 | preprint | portfolio-optimisation | speculative | high |
| [[2025_Chuvakov_FactoringDecisionSupport]] | 2025 | peer-reviewed-theoretical | risk-modelling | theoretical | high |
| [[2025_Frana_QuantumSpeedUps]] | 2025 | preprint | portfolio-optimisation, risk-modelling, asset-pricing | speculative | high |
| [[2025_Guseynov_QuantumAlgorithmLocal]] | 2025 | preprint | derivatives-pricing | speculative | high |
| [[2025_Hlatshwayo_TechnicalReviewQuantum]] | 2025 | preprint | portfolio-optimisation, risk-modelling, derivatives-pricing, fraud-detection, credit-scoring, asset-pricing, quantum-cryptography, market-simulation | speculative | high |
| [[2025_Springer_QuantumFinance]] | 2025 | conference-paper | asset-pricing, portfolio-optimisation, risk-modelling | speculative | medium |
| [[2025_Zhang_QuantumComputingQuantum]] | 2025 | peer-reviewed-empirical | — | speculative | low |
| [[2024_KI_QuantumFinance]] | 2024 | peer-reviewed-theoretical | portfolio-optimisation | theoretical | high |
| [[2023_Ferro_DUpdateReview]] | 2023 | technical-report | derivatives-pricing, risk-modelling, asset-pricing | theoretical | high |
| [[2021_Stamatopoulos_TowardsQuantumAdvantage]] | 2022 | peer-reviewed-empirical | derivatives-pricing, risk-modelling | theoretical | high |
| [[2022_Herbert_QuantumMonteCarlo]] | 2022 | peer-reviewed-theoretical | risk-modelling, derivatives-pricing, market-simulation | theoretical | high |
| [[2022_Wolf_QuantumAlgorithmPricing]] | 2022 | peer-reviewed-theoretical | derivatives-pricing | theoretical | high |
| [[2021_Kubo_VariationalQuantumSimulations]] | 2021 | peer-reviewed-theoretical | derivatives-pricing, market-simulation | theoretical | high |
| [[2021_Lu_AlgorithmsQuantumSimulation]] | 2021 | peer-reviewed-theoretical | — | theoretical | low |
| [[2020_Milek_QuantumImplementationRisk]] | 2020 | preprint | risk-modelling | speculative | high |
| [[2019_Kerenidis_QuantumAlgorithmsPortfolio]] | 2019 | conference-paper | portfolio-optimisation | theoretical | high |
| [[2019_Li_ResearchQuantumComputing]] | 2019 | conference-paper | quantum-cryptography | speculative | medium |
| [[2018_Rebentrost_QuantumComputationalFinance]] | 2018 | preprint | derivatives-pricing, risk-modelling | theoretical | high |
| [[2025_Kao_MixedSignalQuantum]] | — | peer-reviewed-empirical | derivatives-pricing | theoretical | high |

## Topics Using This Method

| Topic | Papers |
|-------|--------|
| derivatives-pricing | 11 |
| risk-modelling | 10 |
| portfolio-optimisation | 7 |
| asset-pricing | 6 |
| market-simulation | 4 |
| credit-scoring | 2 |
| quantum-cryptography | 2 |
| fraud-detection | 1 |

## Key Findings

- [supported] For linear and semilinear SDEs with Lipschitz coefficients, quantum algorithms estimate relevant quantities (option prices, expected hitting times, moments) to accuracy ε in time ˜O(poly(d)polylog(1/ε)), versus classical O(poly(d)/ε²). — [[2026_Prasad_QuantumAlgorithmsStochastic]]
- [supported] Quantum simulation of the Fokker-Planck equation achieves accuracy ε in time ˜O(d · log(1/ε)), compared to classical finite-difference solvers at O(n^{d+1}_s). — [[2026_Prasad_QuantumAlgorithmsStochastic]]
- [supported] Numerical simulations on small instances (e.g., 2D Black-Scholes, 3D Langevin) demonstrate polynomial-to-super-polynomial empirical speedups in accuracy for fixed runtime. — [[2026_Prasad_QuantumAlgorithmsStochastic]]
- [supported] Resource requirements for d-dimensional SDEs: ~150 qubits for d=10, ε=10⁻³, and δx=10⁻² in finance applications. — [[2026_Prasad_QuantumAlgorithmsStochastic]]
- [supported] Quantum annealing hardware is currently the most reliable scaled hardware for optimization tasks in finance — [[2024_Ghysels_QuantumFinance]]
- [supported] The paper extends digitized counterdiabatic quantum computing from qubits to qutrits for quadratic optimization problems by deriving qutrit Hamiltonian encodings and approximate counterdiabatic drivings based on the first-order nested-commutator adiabatic gauge potential. — [[2024_Tancara_HighDimensionalCounterdiabatic]]
- [supported] Across 1000 random instances each of multiway number partitioning, max 3-cut, and portfolio optimization, qutrit encodings generally achieved higher success probability than qubit encodings under the studied simulated dynamics. — [[2024_Tancara_HighDimensionalCounterdiabatic]]
- [supported] For max 3-cut on 6-node random graphs, qutrits outperformed qubits in all 1000 tested instances for the reported evolution times. — [[2024_Tancara_HighDimensionalCounterdiabatic]]
- [supported] The largest reported improvement was for max 3-cut, where some instances achieved success-probability enhancement P3/2 greater than 90 relative to qubits. — [[2024_Tancara_HighDimensionalCounterdiabatic]]
- [supported] Mean success-probability enhancement for max 3-cut was reported as 35.34 at T = 0.1ω0^-1, 30.41 at T = 1ω0^-1, and 6.99 at T = 10ω0^-1. — [[2024_Tancara_HighDimensionalCounterdiabatic]]
- [supported] For multiway number partitioning, mean success-probability enhancement was modest but above 1 on average: 1.31 at T = 0.1ω0^-1, 1.23 at T = 1ω0^-1, and 1.07 at T = 10ω0^-1. — [[2024_Tancara_HighDimensionalCounterdiabatic]]
- [supported] For multiway number partitioning, the fraction of instances with qutrit improvement over qubits was 84.6% at T = 0.1ω0^-1, 79.8% at T = 1ω0^-1, and 74.8% at T = 10ω0^-1. — [[2024_Tancara_HighDimensionalCounterdiabatic]]
- [supported] For portfolio optimization, qutrits improved over qubits in all tested instances at T = 0.1ω0^-1 and T = 1ω0^-1, with mean enhancement 3.56 and 1.54 respectively; at T = 10ω0^-1, more than 80% of instances improved with mean enhancement 1.12. — [[2024_Tancara_HighDimensionalCounterdiabatic]]
- [supported] In illustrative portfolio optimization examples using yfinance data for six assets from 2020-2023, qutrit performance was visibly better than qubits over the simulated evolution, although one tested setting still remained far from the adiabatic regime. — [[2024_Tancara_HighDimensionalCounterdiabatic]]
- [supported] The authors attribute qutrit performance gains to more efficient problem codings that reduce redundant states and lower the density of near-ground-state level crossings during evolution compared with qubit encodings. — [[2024_Tancara_HighDimensionalCounterdiabatic]]
- [supported] The article constructs explicit quantum circuit designs for interest-rate risk based on bounded trinomial trees derived from mean-reverting short-rate models such as Vasicek. — [[2025_Chuvakov_FactoringDecisionSupport]]
- [supported] The article constructs explicit quantum circuit designs for reduced-form credit-risk models in which survival/default over discrete time steps is encoded with one qubit per step. — [[2025_Chuvakov_FactoringDecisionSupport]]
- [supported] End-to-end QMC/QAE schemes are presented that combine scenario generation, risk-measure encoding, and amplitude estimation for financial risk analysis. — [[2025_Chuvakov_FactoringDecisionSupport]]
- [supported] Using a quantum emulator, the authors report that measured values converge to expected values and that estimation error tends toward zero as the number of output qubits increases. — [[2025_Chuvakov_FactoringDecisionSupport]]
- [supported] The quantum algorithm based on matrix multiplicative weights achieves a runtime of O(n^k ε^{-4} + n^{k/2} ε^{-5}) for approximating Lasserre’s hierarchy values for polynomial optimization under specific conditions (e.g., optimal value attained within an ℓ1-ball or simplex constraints). — [[2025_Frana_QuantumSpeedUps]]
