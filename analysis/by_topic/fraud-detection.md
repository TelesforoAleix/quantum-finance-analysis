# Fraud Detection

**Papers:** 18 | **Empirical:** 4 | **Theoretical:** 5 | **Review:** 2

## Papers

| Paper | Year | Source Type | Methods | QA Claim | Relevance |
|-------|------|-------------|---------|----------|-----------|
| [[2026_DECCANINTERNATIONALACADEMICPUBLISHERS_QuantumComputingAlgorithms]] | 2026 | other | grover, variational, quantum-simulation, classical-simulation, quantum-ML | speculative | medium |
| [[2026_Dehn_ExtrapolationMethodOptimize]] | 2026 | peer-reviewed-empirical | QAOA, QUBO, variational, classical-simulation | theoretical | high |
| [[2026_Nawaz_ExploringQuantumMachine]] | 2026 | peer-reviewed-theoretical | QAOA, VQE, quantum-ML, quantum-SVM, grover, variational, quantum-simulation | theoretical | high |
| [[2025_Ganguly_HybridClassicalQuantum]] | 2025 | conference-paper | quantum-ML, variational, QUBO, classical-simulation | speculative | high |
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
| [[2022_Biesner_SolvingSubsetSum]] | 2022 | preprint | QUBO, classical-simulation | speculative | medium |
| [[2022_Sen_VariationalQuantumClassifiers]] | 2022 | peer-reviewed-empirical | quantum-ML, variational | speculative | medium |
| [[2020_Kommadi_QuantumComputingSolutions]] | 2020 | technical-report | QAOA, grover, quantum-ML, quantum-SVM, quantum-annealing, variational, quantum-walk, quantum-simulation, classical-simulation | speculative | high |
| [[2016_Petrosyan_GroverSearchAlgorithm]] | 2015 | preprint | grover | speculative | medium |

## Key Findings

- [supported] The linear-ramp QAOA (LR-QAOA) with extrapolation-based parameter optimization demonstrates superior runtime scaling compared to classical MQLib/Burer2002 for portfolio optimization problems up to 28 qubits, with quantum scaling exponent α = 0.219 vs. classical α = 0.323 — [[2026_Dehn_ExtrapolationMethodOptimize]]
- [supported] For portfolio optimization, the quantum runtime (total circuit depth D) scales as 2^0.219N, while the classical runtime scales as 2^0.323N, indicating a potential quantum scaling advantage [supported] — [[2026_Dehn_ExtrapolationMethodOptimize]]
- [supported] The extrapolation method for LR-QAOA parameters (Δγ, Δβ, p) from smaller subproblems (4-10 qubits) to larger problems (up to 28 qubits) yields results close to direct optimization minima, validating the approach [supported] — [[2026_Dehn_ExtrapolationMethodOptimize]]
- [supported] Universal parameter scaling (algebraic fits for Δγ, Δβ, p across instances) reduces outliers and improves runtime scaling for feature selection, clustering, and MaxCut problems, achieving near-parity with classical benchmarks [supported] — [[2026_Dehn_ExtrapolationMethodOptimize]]
- [supported] The probability of measuring the optimal solution (P_opt) remains above 0.1 on average for all problem classes, with portfolio optimization and MaxCut showing near-constant or slightly increasing P_opt with problem size [supported] — [[2026_Dehn_ExtrapolationMethodOptimize]]
- [supported] The study provides a unified comparative framework for QML algorithms, highlighting their optimization capabilities, practical feasibility, and limitations within a single analytical structure — [[2026_Nawaz_ExploringQuantumMachine]]
- [supported] Key challenges hindering real-world deployment of QML include quantum noise, scalability constraints, hardware limitations, and algorithmic performance trade-offs — [[2026_Nawaz_ExploringQuantumMachine]]
- [supported] QLSTM test predictions for NVIDIA stock data were slightly superior to classical LSTM, particularly around volatile peaks, indicating better alignment with real-life data — [[2025_Ganguly_HybridClassicalQuantum]]
- [supported] QLSTM demonstrated earlier prediction of turning points in stock market trends compared to classical LSTM, potentially offering advantages in forecasting market movements — [[2025_Ganguly_HybridClassicalQuantum]]
- [supported] QLSTM training loss exhibited smoothing over time, unlike classical LSTM where loss spikes appeared more pronounced toward the end of training — [[2025_Ganguly_HybridClassicalQuantum]]
- [supported] qGAN successfully modeled cryptocurrency data distributions with fewer iterations than classical GANs, achieving equilibrium in generator and discriminator loss functions — [[2025_Ganguly_HybridClassicalQuantum]]
- [supported] qGAN combined with QUBO optimization predicted BNBBTC as the optimal cryptocurrency investment based on real-world Binance data — [[2025_Ganguly_HybridClassicalQuantum]]
- [supported] QCBM with SPSA optimization closely approximated the target probability distribution for the synthetic BAS dataset, outperforming other optimizers like Cobyla — [[2025_Ganguly_HybridClassicalQuantum]]
- [supported] Training time for QLSTM was highly dependent on GPU type, with NVIDIA RTX 3070 showing a 50% reduction in training time per epoch compared to RTX 3060 (780s vs. 1600s) — [[2025_Ganguly_HybridClassicalQuantum]]
- [supported] CUDA-Q acceleration significantly improved QLSTM training performance, reducing training time per epoch from 780s to 18s on an RTX 3070 — [[2025_Ganguly_HybridClassicalQuantum]]
- [supported] Rasengan improves accuracy by 4.12× compared to state-of-the-art QAOA (Choco-Q) on constrained binary optimization problems across 2000 cases from five domains (facility location, k-partition, job scheduling, set covering, and graph coloring). — [[2025_Jiang_RasenganTransitionHamiltonian]]
- [supported] Rasengan reduces circuit depth by 1.96× compared to prior variational quantum algorithms (VQAs) in noise-free simulations. — [[2025_Jiang_RasenganTransitionHamiltonian]]
- [supported] On real-world quantum hardware (IBM Kyiv and Brisbane), Rasengan achieves a 379× improvement in solution quality over the mean quality of feasible solution baselines, marking the first quantum algorithm to outperform this baseline. — [[2025_Jiang_RasenganTransitionHamiltonian]]
- [supported] Rasengan’s Hamiltonian simplification and pruning techniques reduce circuit depth by over 94.6%, making it deployable on current NISQ devices (e.g., reducing depth from ~7000 to ~50 for a 24-variable graph coloring problem). — [[2025_Jiang_RasenganTransitionHamiltonian]]
- [supported] Rasengan’s error mitigation technique improves accuracy by more than 303× on noisy hardware by purifying infeasible solutions after each segment. — [[2025_Jiang_RasenganTransitionHamiltonian]]

## Methodologies Used

| Method | Papers |
|--------|--------|
| variational | 14 |
| quantum-ML | 14 |
| QAOA | 10 |
| classical-simulation | 9 |
| grover | 8 |
| quantum-simulation | 8 |
| QUBO | 7 |
| quantum-SVM | 7 |
| VQE | 6 |
| quantum-annealing | 5 |
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
