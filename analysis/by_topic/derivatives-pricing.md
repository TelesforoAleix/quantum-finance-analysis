# Derivatives Pricing

**Papers:** 25 | **Empirical:** 5 | **Theoretical:** 4 | **Review:** 2

## Papers

| Paper | Year | Source Type | Methods | QA Claim | Relevance |
|-------|------|-------------|---------|----------|-----------|
| [[2026_Barbaresco_QuantumAmplitudeEstimation]] | 2026 | peer-reviewed-empirical | amplitude-estimation, classical-simulation | disputed | high |
| [[2026_DECCANINTERNATIONALACADEMICPUBLISHERS_QuantumComputingAlgorithms]] | 2026 | other | grover, variational, quantum-simulation, classical-simulation, quantum-ML | speculative | medium |
| [[2026_Dechant_ErrorResourceEstimates]] | 2026 | preprint | variational, VQE, classical-simulation | speculative | high |
| [[2026_Nawaz_ExploringQuantumMachine]] | 2026 | peer-reviewed-theoretical | QAOA, VQE, quantum-ML, quantum-SVM, grover, quantum-simulation, variational, classical-simulation | theoretical | high |
| [[2026_Prasad_QuantumAlgorithmsStochastic]] | 2026 | preprint | HHL, amplitude-estimation, quantum-simulation, variational, quantum-ML, classical-simulation | speculative | high |
| [[2024_Ghysels_QuantumFinance]] | 2025 | other | quantum-annealing, quantum-simulation | speculative | high |
| [[2025_Benamer_VariationalQuantumAlgorithms]] | 2025 | preprint | VQE, QAOA, quantum-ML, variational, quantum-annealing, quantum-SVM, amplitude-estimation, QUBO, classical-simulation | speculative | high |
| [[2025_Berkowitz_QuantumComputingMeets]] | 2025 | other | quantum-annealing, QUBO, quantum-simulation | speculative | high |
| [[2025_Chaudhary_PracticalQuantumSolver]] | 2025 | conference-paper | variational, quantum-simulation, classical-simulation | speculative | high |
| [[2025_Cibrario_AutocallableOptionsPricing]] | 2025 | conference-paper | amplitude-estimation, quantum-simulation, classical-simulation | speculative | high |
| [[2025_Hlatshwayo_TechnicalReviewQuantum]] | 2025 | preprint | HHL, QAOA, grover, quantum-walk, amplitude-estimation, quantum-simulation, quantum-ML | speculative | high |
| [[2025_JETIR_QuantumFinance]] | 2025 | peer-reviewed-theoretical | QAOA, VQE, quantum-ML, amplitude-estimation, variational, quantum-simulation | theoretical | high |
| [[2025_Jiang_RasenganTransitionHamiltonian]] | 2025 | conference-paper | variational, QAOA, quantum-annealing, QUBO, quantum-simulation | speculative | high |
| [[2025_Malhotra_ComparativeStudyQuantum]] | 2025 | conference-paper | QAOA, grover, quantum-ML, classical-simulation | speculative | medium |
| [[2025_NeelotpalDey_QuantumComputingFinancial]] | 2025 | peer-reviewed-theoretical | QAOA, VQE, quantum-ML, amplitude-estimation, variational, classical-simulation | speculative | high |
| [[2025_ThirumalGunasekaran_ExploringRevolutionaryPotential]] | 2025 | peer-reviewed-theoretical | grover, quantum-ML, amplitude-estimation, quantum-simulation | theoretical | high |
| [[2026_Mahmod_StateQuantumComputing]] | 2025 | review-article | HHL, QAOA, VQE, quantum-annealing, grover, quantum-ML, quantum-SVM, variational, QUBO, quantum-simulation, classical-simulation | speculative | high |
| [[2023_Markna_UnveilingAdvancedComputational]] | 2023 | review-article | QAOA, quantum-annealing, HHL, quantum-ML, amplitude-estimation, QUBO, quantum-SVM, quantum-walk | speculative | high |
| [[2021_Stamatopoulos_TowardsQuantumAdvantage]] | 2022 | peer-reviewed-empirical | amplitude-estimation, grover, quantum-simulation, classical-simulation | theoretical | high |
| [[2022_Doriguello_QuantumAlgorithmStochastic]] | 2022 | conference-paper | amplitude-estimation, quantum-simulation, quantum-ML | theoretical | high |
| [[2022_Saha_IntermediateQutritBased]] | 2022 | peer-reviewed-empirical | amplitude-estimation, VQE, grover, quantum-simulation, classical-simulation | theoretical | high |
| [[2022_Zhao_QuantumInspiredVariational]] | 2022 | peer-reviewed-empirical | variational, quantum-simulation, classical-simulation | not-applicable | high |
| [[2021_Martin_TowardPricingFinancial]] | 2021 | peer-reviewed-empirical | quantum-simulation, quantum-ML, HHL, variational | speculative | high |
| [[2020_Miyamoto_ReductionQubitsQuantum]] | 2020 | preprint | amplitude-estimation, quantum-simulation, classical-simulation | theoretical | high |
| [[2018_Rebentrost_QuantumComputationalFinance]] | 2018 | preprint | amplitude-estimation, grover, quantum-simulation, classical-simulation | theoretical | high |

## Key Findings

- [supported] Quantum Amplitude Estimation (QAE) variants (IAE and MLAE) returned an expected payoff of zero for European call options, while classical methods (Black-Scholes and Monte Carlo) yielded significantly positive values ($17.60 and $17.06 in two scenarios). — [[2026_Barbaresco_QuantumAmplitudeEstimation]]
- [supported] The failure of QAE to capture non-zero expected payoffs is attributed to limited resolution from 6 uncertainty qubits (64 bins), which inadequately encodes small-amplitude, in-the-money price regions. — [[2026_Barbaresco_QuantumAmplitudeEstimation]]
- [supported] Quantum circuits correctly identified the realized market outcome (zero payoff) but failed to capture the full expectation implied by the distribution tail. — [[2026_Barbaresco_QuantumAmplitudeEstimation]]
- [supported] Classical benchmarks (Black-Scholes and Monte Carlo) aligned closely, with Monte Carlo deviations below 1% from analytical values. — [[2026_Barbaresco_QuantumAmplitudeEstimation]]
- [supported] Quantum estimates for asset prices were lower than classical benchmarks ($185 vs. $198 in 2023–2024; $179 vs. $192 in 2022–2023), further highlighting resolution limitations. — [[2026_Barbaresco_QuantumAmplitudeEstimation]]
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

## Methodologies Used

| Method | Papers |
|--------|--------|
| quantum-simulation | 19 |
| classical-simulation | 16 |
| amplitude-estimation | 14 |
| quantum-ML | 13 |
| variational | 12 |
| grover | 9 |
| QAOA | 9 |
| VQE | 7 |
| quantum-annealing | 6 |
| HHL | 5 |
| QUBO | 5 |
| quantum-SVM | 4 |
| quantum-walk | 2 |

## Open Questions

- How can quantum amplitude estimation be adapted to better resolve low-probability, high-payoﬀ events with limited qubits? — [[2026_Barbaresco_QuantumAmplitudeEstimation]]
- What is the minimum qubit count required to achieve accurate expected payoff estimates for realistic financial distributions? — [[2026_Barbaresco_QuantumAmplitudeEstimation]]
- How do noise and decoherence on real quantum hardware affect the performance of IAE and MLAE in option pricing? — [[2026_Barbaresco_QuantumAmplitudeEstimation]]
- Can nonuniform binning or adaptive encoding strategies improve the resolution of tail events in quantum state preparation? — [[2026_Barbaresco_QuantumAmplitudeEstimation]]
- What are the trade-offs between circuit depth, qubit count, and estimation accuracy in near-term quantum devices for financial applications? — [[2026_Barbaresco_QuantumAmplitudeEstimation]]
- How do quantum amplitude estimation methods perform under non-log-normal or more complex asset price distributions? — [[2026_Barbaresco_QuantumAmplitudeEstimation]]
- What is the impact of varying strike prices, maturities, and volatilities on the accuracy of quantum estimators? — [[2026_Barbaresco_QuantumAmplitudeEstimation]]
- Increase qubit counts to improve distribution resolution and capture low-probability events — [[2026_Barbaresco_QuantumAmplitudeEstimation]]
- Develop advanced encoding strategies, such as nonuniform bin spacing or variational encoding, to better resolve tail events — [[2026_Barbaresco_QuantumAmplitudeEstimation]]
- Test on real quantum hardware to assess performance under noise and error conditions — [[2026_Barbaresco_QuantumAmplitudeEstimation]]
