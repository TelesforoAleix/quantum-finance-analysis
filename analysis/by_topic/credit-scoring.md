# Credit Scoring

**Papers:** 17 | **Empirical:** 4 | **Theoretical:** 5 | **Review:** 2

## Papers

| Paper | Year | Source Type | Methods | QA Claim | Relevance |
|-------|------|-------------|---------|----------|-----------|
| [[2026_DECCANINTERNATIONALACADEMICPUBLISHERS_QuantumComputingAlgorithms]] | 2026 | other | grover, variational, quantum-simulation, classical-simulation, quantum-ML | speculative | medium |
| [[2026_Dehn_ExtrapolationMethodOptimize]] | 2026 | peer-reviewed-empirical | QAOA, QUBO, variational, classical-simulation | theoretical | high |
| [[2026_Nawaz_ExploringQuantumMachine]] | 2026 | peer-reviewed-theoretical | QAOA, VQE, quantum-ML, quantum-SVM, grover, variational, quantum-simulation | theoretical | high |
| [[2024_Ghysels_QuantumFinance]] | 2025 | other | quantum-annealing, QUBO, quantum-simulation | speculative | high |
| [[2025_Berkowitz_QuantumComputingMeets]] | 2025 | other | quantum-annealing, QUBO | speculative | high |
| [[2025_Hlatshwayo_TechnicalReviewQuantum]] | 2025 | preprint | HHL, grover, quantum-walk, amplitude-estimation, quantum-simulation, quantum-ML | speculative | high |
| [[2025_JETIR_QuantumFinance]] | 2025 | peer-reviewed-theoretical | QAOA, VQE, quantum-ML, amplitude-estimation, variational, classical-simulation | theoretical | high |
| [[2025_Jiang_RasenganTransitionHamiltonian]] | 2025 | conference-paper | variational, QAOA, VQE, quantum-annealing, QUBO | theoretical | high |
| [[2025_NeelotpalDey_QuantumComputingFinancial]] | 2025 | peer-reviewed-theoretical | QAOA, VQE, quantum-ML, amplitude-estimation, QUBO, variational, classical-simulation | theoretical | high |
| [[2025_ThirumalGunasekaran_ExploringRevolutionaryPotential]] | 2025 | peer-reviewed-theoretical | grover, quantum-ML, quantum-simulation | theoretical | high |
| [[2025_Vangibhuratha_QuantumMachineLearning]] | 2025 | peer-reviewed-theoretical | quantum-ML, quantum-SVM, variational, quantum-annealing, QAOA, HHL, quantum-simulation, classical-simulation | theoretical | high |
| [[2026_Mahmod_StateQuantumComputing]] | 2025 | review-article | HHL, QAOA, VQE, quantum-annealing, grover, quantum-ML, quantum-SVM, variational, QUBO, quantum-simulation | theoretical | high |
| [[2023_Thakkar_ImprovedFinancialForecasting]] | 2024 | peer-reviewed-empirical | quantum-ML, variational, quantum-SVM | speculative | high |
| [[2025_Deshmukh_QuantumMachineLearning]] | 2024 | peer-reviewed-empirical | quantum-ML, quantum-SVM, VQE, QAOA, variational | speculative | high |
| [[2023_Markna_UnveilingAdvancedComputational]] | 2023 | review-article | QAOA, quantum-annealing, HHL, quantum-ML, quantum-SVM, amplitude-estimation, QUBO, variational, grover, quantum-simulation, classical-simulation | speculative | high |
| [[2022_Sen_VariationalQuantumClassifiers]] | 2022 | peer-reviewed-empirical | quantum-ML, variational | speculative | medium |
| [[2020_Kommadi_QuantumComputingSolutions]] | 2020 | technical-report | QAOA, grover, quantum-ML, quantum-SVM, quantum-annealing, variational, quantum-walk, quantum-simulation, classical-simulation | speculative | high |

## Key Findings

- [supported] The linear-ramp QAOA (LR-QAOA) with extrapolation-based parameter optimization demonstrates superior runtime scaling compared to classical MQLib/Burer2002 for portfolio optimization problems up to 28 qubits, with quantum scaling exponent α = 0.219 vs. classical α = 0.323 — [[2026_Dehn_ExtrapolationMethodOptimize]]
- [supported] For portfolio optimization, the quantum runtime (total circuit depth D) scales as 2^0.219N, while the classical runtime scales as 2^0.323N, indicating a potential quantum scaling advantage [supported] — [[2026_Dehn_ExtrapolationMethodOptimize]]
- [supported] The extrapolation method for LR-QAOA parameters (Δγ, Δβ, p) from smaller subproblems (4-10 qubits) to larger problems (up to 28 qubits) yields results close to direct optimization minima, validating the approach [supported] — [[2026_Dehn_ExtrapolationMethodOptimize]]
- [supported] Universal parameter scaling (algebraic fits for Δγ, Δβ, p across instances) reduces outliers and improves runtime scaling for feature selection, clustering, and MaxCut problems, achieving near-parity with classical benchmarks [supported] — [[2026_Dehn_ExtrapolationMethodOptimize]]
- [supported] The probability of measuring the optimal solution (P_opt) remains above 0.1 on average for all problem classes, with portfolio optimization and MaxCut showing near-constant or slightly increasing P_opt with problem size [supported] — [[2026_Dehn_ExtrapolationMethodOptimize]]
- [supported] The study provides a unified comparative framework for QML algorithms, highlighting their optimization capabilities, practical feasibility, and limitations within a single analytical structure — [[2026_Nawaz_ExploringQuantumMachine]]
- [supported] Key challenges hindering real-world deployment of QML include quantum noise, scalability constraints, hardware limitations, and algorithmic performance trade-offs — [[2026_Nawaz_ExploringQuantumMachine]]
- [supported] Quantum annealing hardware is currently the most reliable scaled hardware for optimization tasks in finance — [[2024_Ghysels_QuantumFinance]]
- [supported] MIDAS (mixed-data sampling) methods are regression-based techniques for combining financial data at different frequencies — [[2025_Berkowitz_QuantumComputingMeets]]
- [supported] Rasengan improves accuracy by 4.12× compared to state-of-the-art QAOA (Choco-Q) on constrained binary optimization problems across 2000 cases from five domains (facility location, k-partition, job scheduling, set covering, and graph coloring). — [[2025_Jiang_RasenganTransitionHamiltonian]]
- [supported] Rasengan reduces circuit depth by 1.96× compared to prior variational quantum algorithms (VQAs) in noise-free simulations. — [[2025_Jiang_RasenganTransitionHamiltonian]]
- [supported] On real-world quantum hardware (IBM Kyiv and Brisbane), Rasengan achieves a 379× improvement in solution quality over the mean quality of feasible solution baselines, marking the first quantum algorithm to outperform this baseline. — [[2025_Jiang_RasenganTransitionHamiltonian]]
- [supported] Rasengan’s Hamiltonian simplification and pruning techniques reduce circuit depth by over 94.6%, making it deployable on current NISQ devices (e.g., reducing depth from ~7000 to ~50 for a 24-variable graph coloring problem). — [[2025_Jiang_RasenganTransitionHamiltonian]]
- [supported] Rasengan’s error mitigation technique improves accuracy by more than 303× on noisy hardware by purifying infeasible solutions after each segment. — [[2025_Jiang_RasenganTransitionHamiltonian]]
- [supported] Rasengan achieves lower approximation ratio gaps (ARG) than HEA, penalty-term-based QAOA (P-QAOA), and commute-Hamiltonian-based QAOA (Choco-Q) across all tested benchmarks, with ARG values as low as 0.01 for small-scale problems. — [[2025_Jiang_RasenganTransitionHamiltonian]]
- [supported] Rasengan’s segmented execution strategy partitions transition Hamiltonians into segments with depths as low as 34n (where n is the number of qubits), enabling execution on NISQ devices while preserving solution quality. — [[2025_Jiang_RasenganTransitionHamiltonian]]
- [supported] Early experiments using IBM’s quantum devices show QSVM success in binary classification tasks for financial applications, such as distinguishing bullish/bearish markets or asset risk profiles — [[2025_Vangibhuratha_QuantumMachineLearning]]
- [supported] Quantum computing has demonstrated practical applications across multiple industries, including agriculture, defense, energy, finance, healthcare, infrastructure, manufacturing, and technology, with quantified performance improvements in specific use cases — [[2026_Mahmod_StateQuantumComputing]]
- [supported] Google's Willow quantum chip achieved real-time error correction on a superconducting system with 105 qubits, completing a computation in under five minutes that would take the world's fastest supercomputer an estimated 10^25 years — [[2026_Mahmod_StateQuantumComputing]]
- [supported] D-Wave’s Advantage2 hybrid solver demonstrated the ability to solve problems with up to 2 million variable constraints, accessible via cloud service from over 40 countries as of 2025 — [[2026_Mahmod_StateQuantumComputing]]

## Methodologies Used

| Method | Papers |
|--------|--------|
| variational | 13 |
| quantum-ML | 13 |
| QAOA | 10 |
| quantum-simulation | 9 |
| grover | 7 |
| classical-simulation | 7 |
| QUBO | 7 |
| quantum-SVM | 7 |
| quantum-annealing | 7 |
| VQE | 6 |
| HHL | 4 |
| amplitude-estimation | 4 |
| quantum-walk | 2 |

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
