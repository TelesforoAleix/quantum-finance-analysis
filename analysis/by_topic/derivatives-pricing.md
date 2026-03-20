# Derivatives Pricing

**Papers:** 25 | **Empirical:** 4 | **Theoretical:** 5 | **Review:** 2

## Papers

| Paper | Year | Source Type | Methods | QA Claim | Relevance |
|-------|------|-------------|---------|----------|-----------|
| [[2026_Barbaresco_QuantumAmplitudeEstimation]] | 2026 | peer-reviewed-empirical | amplitude-estimation, classical-simulation | disputed | high |
| [[2026_DECCANINTERNATIONALACADEMICPUBLISHERS_QuantumComputingAlgorithms]] | 2026 | other | grover, variational, quantum-simulation, classical-simulation, quantum-ML | speculative | medium |
| [[2026_Dechant_ErrorResourceEstimates]] | 2026 | preprint | variational, VQE, quantum-simulation | speculative | high |
| [[2026_Nawaz_ExploringQuantumMachine]] | 2026 | peer-reviewed-theoretical | QAOA, VQE, quantum-ML, quantum-SVM, grover, variational, quantum-simulation | theoretical | high |
| [[2026_Prasad_QuantumAlgorithmsStochastic]] | 2026 | preprint | HHL, amplitude-estimation, quantum-simulation, variational, quantum-ML, classical-simulation | speculative | high |
| [[2024_Ghysels_QuantumFinance]] | 2025 | other | quantum-annealing, QUBO, quantum-simulation | speculative | high |
| [[2025_Benamer_VariationalQuantumAlgorithms]] | 2025 | preprint | VQE, QAOA, quantum-ML, variational, amplitude-estimation | speculative | high |
| [[2025_Berkowitz_QuantumComputingMeets]] | 2025 | other | quantum-annealing, QUBO | speculative | high |
| [[2025_Chaudhary_PracticalQuantumSolver]] | 2025 | conference-paper | variational, quantum-simulation, classical-simulation | theoretical | high |
| [[2025_Cibrario_AutocallableOptionsPricing]] | 2025 | conference-paper | amplitude-estimation, quantum-simulation, classical-simulation | speculative | high |
| [[2025_Hlatshwayo_TechnicalReviewQuantum]] | 2025 | preprint | HHL, grover, quantum-walk, amplitude-estimation, quantum-simulation, quantum-ML | speculative | high |
| [[2025_JETIR_QuantumFinance]] | 2025 | peer-reviewed-theoretical | QAOA, VQE, quantum-ML, amplitude-estimation, variational, classical-simulation | theoretical | high |
| [[2025_Jiang_RasenganTransitionHamiltonian]] | 2025 | conference-paper | variational, QAOA, VQE, quantum-annealing, QUBO | theoretical | high |
| [[2025_NeelotpalDey_QuantumComputingFinancial]] | 2025 | peer-reviewed-theoretical | QAOA, VQE, quantum-ML, amplitude-estimation, QUBO, variational, classical-simulation | theoretical | high |
| [[2025_ThirumalGunasekaran_ExploringRevolutionaryPotential]] | 2025 | peer-reviewed-theoretical | grover, quantum-ML, quantum-simulation | theoretical | high |
| [[2026_Mahmod_StateQuantumComputing]] | 2025 | review-article | HHL, QAOA, VQE, quantum-annealing, grover, quantum-ML, quantum-SVM, variational, QUBO, quantum-simulation | theoretical | high |
| [[2023_Markna_UnveilingAdvancedComputational]] | 2023 | review-article | QAOA, quantum-annealing, HHL, quantum-ML, quantum-SVM, amplitude-estimation, QUBO, variational, grover, quantum-simulation, classical-simulation | speculative | high |
| [[2021_Stamatopoulos_TowardsQuantumAdvantage]] | 2022 | peer-reviewed-empirical | amplitude-estimation, quantum-simulation, variational, quantum-ML | theoretical | high |
| [[2022_Doriguello_QuantumAlgorithmStochastic]] | 2022 | conference-paper | amplitude-estimation, quantum-simulation, quantum-ML | theoretical | high |
| [[2022_Saha_IntermediateQutritBased]] | 2022 | peer-reviewed-theoretical | quantum-simulation, variational | theoretical | high |
| [[2022_Zhao_QuantumInspiredVariational]] | 2022 | peer-reviewed-empirical | variational, quantum-ML, quantum-simulation, classical-simulation | theoretical | high |
| [[2021_Martin_TowardPricingFinancial]] | 2021 | peer-reviewed-empirical | quantum-simulation, quantum-ML, variational, classical-simulation | speculative | high |
| [[2020_Kommadi_QuantumComputingSolutions]] | 2020 | technical-report | QAOA, grover, quantum-ML, quantum-SVM, quantum-annealing, variational, quantum-walk, quantum-simulation, classical-simulation | speculative | high |
| [[2020_Miyamoto_ReductionQubitsQuantum]] | 2020 | preprint | amplitude-estimation, quantum-simulation, classical-simulation | theoretical | high |
| [[2018_Rebentrost_QuantumComputationalFinance]] | 2018 | preprint | amplitude-estimation, grover, quantum-simulation, classical-simulation | theoretical | high |

## Key Findings

- [supported] Quantum Amplitude Estimation (QAE) variants (IAE and MLAE) returned an expected payoff of zero for European call options, while classical methods (Black-Scholes and Monte Carlo) yielded significantly positive values ($17.60 and $17.06 in two scenarios). — [[2026_Barbaresco_QuantumAmplitudeEstimation]]
- [supported] The failure of QAE to capture non-zero expected payoffs is attributed to limited resolution from 6 uncertainty qubits (64 bins), which inadequately encode small-amplitude, in-the-money price regions. — [[2026_Barbaresco_QuantumAmplitudeEstimation]]
- [supported] Quantum methods correctly identified the realized market outcome (zero payoff) but failed to capture the full expectation implied by the distribution tail. — [[2026_Barbaresco_QuantumAmplitudeEstimation]]
- [supported] Classical benchmarks (Black-Scholes and Monte Carlo with 100,000 samples) showed <1% deviation from analytic values, confirming their accuracy for the same discretized price space. — [[2026_Barbaresco_QuantumAmplitudeEstimation]]
- [supported] Quantum estimates for terminal asset prices were lower than classical benchmarks ($185 vs. $198 in 2023–2024; $179 vs. $192 in 2022–2023), further highlighting resolution limitations. — [[2026_Barbaresco_QuantumAmplitudeEstimation]]
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

## Methodologies Used

| Method | Papers |
|--------|--------|
| quantum-simulation | 19 |
| variational | 16 |
| quantum-ML | 15 |
| classical-simulation | 13 |
| amplitude-estimation | 12 |
| grover | 8 |
| QAOA | 8 |
| VQE | 7 |
| quantum-annealing | 6 |
| QUBO | 6 |
| quantum-SVM | 4 |
| HHL | 4 |
| quantum-walk | 2 |

## Open Questions

- How can quantum amplitude estimation be improved to resolve low-probability, high-payoff events with limited qubits? — [[2026_Barbaresco_QuantumAmplitudeEstimation]]
- What is the minimum qubit count required to achieve accurate expected payoff estimation for realistic financial distributions? — [[2026_Barbaresco_QuantumAmplitudeEstimation]]
- How do noise and decoherence on real quantum hardware affect the performance of IAE and MLAE for option pricing? — [[2026_Barbaresco_QuantumAmplitudeEstimation]]
- Can adaptive or nonuniform binning strategies improve the resolution of tail events in quantum state preparation? — [[2026_Barbaresco_QuantumAmplitudeEstimation]]
- What are the trade-offs between circuit depth, qubit count, and estimation accuracy in near-term quantum devices for financial applications? — [[2026_Barbaresco_QuantumAmplitudeEstimation]]
- How do quantum amplitude estimation methods perform in multi-asset or multi-period option pricing scenarios? — [[2026_Barbaresco_QuantumAmplitudeEstimation]]
- Increase qubit counts to improve distribution resolution and capture low-probability events — [[2026_Barbaresco_QuantumAmplitudeEstimation]]
- Explore advanced encoding schemes, such as nonuniform bin spacing or variational encoding, to better resolve tail events — [[2026_Barbaresco_QuantumAmplitudeEstimation]]
- Test on real quantum hardware to assess the impact of noise and decoherence — [[2026_Barbaresco_QuantumAmplitudeEstimation]]
- Extend the pipeline to multi-asset or multi-period option pricing problems — [[2026_Barbaresco_QuantumAmplitudeEstimation]]
