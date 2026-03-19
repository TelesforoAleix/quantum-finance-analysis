# Fraud Detection

**Papers:** 16 | **Empirical:** 3 | **Theoretical:** 6 | **Review:** 1

## Papers

| Paper | Year | Source Type | Methods | QA Claim | Relevance |
|-------|------|-------------|---------|----------|-----------|
| [[2026_DECCANINTERNATIONALACADEMICPUBLISHERS_QuantumComputingAlgorithms]] | 2026 | other | grover, variational, quantum-simulation, classical-simulation, quantum-ML | speculative | medium |
| [[2026_Nawaz_ExploringQuantumMachine]] | 2026 | peer-reviewed-theoretical | QAOA, VQE, quantum-ML, quantum-SVM, grover, quantum-simulation, variational, classical-simulation | theoretical | high |
| [[2025_Ganguly_HybridClassicalQuantum]] | 2025 | conference-paper | quantum-ML, variational, QUBO, classical-simulation | speculative | high |
| [[2025_Hlatshwayo_TechnicalReviewQuantum]] | 2025 | preprint | HHL, QAOA, grover, quantum-walk, amplitude-estimation, quantum-simulation, quantum-ML | speculative | high |
| [[2025_JETIR_QuantumFinance]] | 2025 | peer-reviewed-theoretical | QAOA, VQE, quantum-ML, amplitude-estimation, variational, quantum-simulation | theoretical | high |
| [[2025_Jiang_RasenganTransitionHamiltonian]] | 2025 | conference-paper | variational, QAOA, quantum-annealing, QUBO, quantum-simulation | speculative | high |
| [[2025_NeelotpalDey_QuantumComputingFinancial]] | 2025 | peer-reviewed-theoretical | QAOA, VQE, quantum-ML, amplitude-estimation, variational, classical-simulation | speculative | high |
| [[2025_ThirumalGunasekaran_ExploringRevolutionaryPotential]] | 2025 | peer-reviewed-theoretical | grover, quantum-ML, amplitude-estimation, quantum-simulation | theoretical | high |
| [[2025_Vangibhuratha_QuantumMachineLearning]] | 2025 | peer-reviewed-theoretical | quantum-ML, quantum-SVM, variational, quantum-annealing, QAOA, quantum-simulation, classical-simulation | theoretical | high |
| [[2026_Mahmod_StateQuantumComputing]] | 2025 | review-article | HHL, QAOA, VQE, quantum-annealing, grover, quantum-ML, quantum-SVM, variational, QUBO, quantum-simulation, classical-simulation | speculative | high |
| [[2023_Thakkar_ImprovedFinancialForecasting]] | 2024 | peer-reviewed-empirical | quantum-ML, variational, quantum-SVM | speculative | high |
| [[2025_Deshmukh_QuantumMachineLearning]] | 2024 | peer-reviewed-empirical | quantum-ML, quantum-SVM, VQE, QAOA, variational, classical-simulation | speculative | high |
| [[2022_Biesner_SolvingSubsetSum]] | 2022 | preprint | QUBO, classical-simulation | speculative | medium |
| [[2022_Sen_VariationalQuantumClassifiers]] | 2022 | peer-reviewed-empirical | quantum-ML, variational, QAOA | speculative | medium |
| [[2020_Kommadi_QuantumComputingSolutions]] | 2020 | technical-report | QAOA, grover, quantum-annealing, quantum-ML, quantum-SVM, quantum-walk, variational, classical-simulation | speculative | medium |
| [[2016_Petrosyan_GroverSearchAlgorithm]] | 2015 | peer-reviewed-theoretical | grover | theoretical | medium |

## Key Findings

- [supported] The study provides a unified comparative framework for QML optimization algorithms, highlighting their practical feasibility and identifying key research gaps hindering real-world deployment — [[2026_Nawaz_ExploringQuantumMachine]]
- [supported] Challenges such as quantum noise, scalability, and hardware limitations remain significant barriers to the practical deployment of QML algorithms — [[2026_Nawaz_ExploringQuantumMachine]]
- [supported] QLSTM test predictions for NVIDIA stock data were slightly superior to classical LSTM, particularly around volatile peaks, making it a promising candidate for financial forecasting [supported by RMSE values of 15.09×10⁻³ (QLSTM) vs. 12.8×10⁻³ (LSTM) on test data]. — [[2025_Ganguly_HybridClassicalQuantum]]
- [supported] QLSTM demonstrated earlier prediction of turning points in stock market trends compared to classical LSTM, potentially offering an advantage in foreseeing market movements. — [[2025_Ganguly_HybridClassicalQuantum]]
- [supported] qGAN successfully modeled cryptocurrency data (BNBBTC, ETHBTC, etc.) with fewer iterations than classical GANs, achieving equilibrium in generator/discriminator loss functions (~0.6931 at optimal equilibrium). — [[2025_Ganguly_HybridClassicalQuantum]]
- [supported] QCBM with SPSA optimization closely approximated target probability distributions for synthetic BAS datasets, outperforming Cobyla and Nelder-Mead optimizers. — [[2025_Ganguly_HybridClassicalQuantum]]
- [supported] QLSTM training time was highly dependent on GPU hardware, with NVIDIA CUDA-Q reducing per-epoch training time from 780s (RTX 3070) to 18s (RTX 3070 with CUDA-Q). — [[2025_Ganguly_HybridClassicalQuantum]]
- [supported] Industry adoption by firms like JPMorgan Chase, Goldman Sachs, and Nasdaq demonstrates measurable improvements in computational performance using hybrid quantum-classical models for tasks like option pricing and fraud detection — [[2025_JETIR_QuantumFinance]]
- [supported] Rasengan improves accuracy by 4.12× compared to the state-of-the-art QAOA (Choco-Q) on constrained binary optimization problems across 2000 cases from five domains (facility location, k-partition, job scheduling, set cover, and graph coloring). — [[2025_Jiang_RasenganTransitionHamiltonian]]
- [supported] Rasengan achieves a 379× improvement in solution quality over baseline methods on real-world quantum platforms (IBM Kyiv and Brisbane). — [[2025_Jiang_RasenganTransitionHamiltonian]]
- [supported] Rasengan reduces circuit depth by 1.96× compared to prior variational quantum algorithms (VQAs) and by 49× compared to Choco-Q, making it deployable on NISQ devices. — [[2025_Jiang_RasenganTransitionHamiltonian]]
- [supported] Rasengan is the first quantum algorithm to outperform the mean quality of feasible solution baselines on real hardware, achieving an approximation ratio gap (ARG) as low as 0.01 for small-scale problems. — [[2025_Jiang_RasenganTransitionHamiltonian]]
- [supported] Hamiltonian simplification and pruning techniques reduce circuit depth by over 94.6%, while probability-preserving segmented execution further reduces depth to ~50, suitable for current quantum hardware. — [[2025_Jiang_RasenganTransitionHamiltonian]]
- [supported] Error mitigation via solution purification improves accuracy by more than 303× on noisy hardware. — [[2025_Jiang_RasenganTransitionHamiltonian]]
- [supported] Rasengan maintains a 100% in-constraints rate (feasible solutions) on real hardware, unlike penalty-term-based QAOA, which often violates constraints. — [[2025_Jiang_RasenganTransitionHamiltonian]]
- [supported] Current quantum hardware is limited by high error rates, short coherence times, and high costs, restricting the complexity of QML models that can be executed effectively — [[2025_Vangibhuratha_QuantumMachineLearning]]
- [supported] Quantum computing has demonstrated experimental and commercial applications across diverse industries including agriculture, defense, energy, finance, healthcare, infrastructure, manufacturing, and technology as of 2025 — [[2026_Mahmod_StateQuantumComputing]]
- [supported] Google’s Sycamore and Willow quantum processors have shown quantum advantage in specific tasks, with Willow completing a computation in under five minutes that would take the world’s fastest supercomputer an estimated 10^25 years — [[2026_Mahmod_StateQuantumComputing]]
- [supported] D-Wave’s Advantage2 quantum computer can solve problems with up to 2 million variable constraints via hybrid solver, accessible online from over 40 countries — [[2026_Mahmod_StateQuantumComputing]]
- [supported] Caltech researchers built an array of 6,100 neutral atom qubits with 99.98% fidelity in single-qubit operations and 13 seconds of quantum coherence, showing progress toward scalable quantum computers — [[2026_Mahmod_StateQuantumComputing]]

## Methodologies Used

| Method | Papers |
|--------|--------|
| quantum-ML | 13 |
| variational | 12 |
| QAOA | 10 |
| classical-simulation | 9 |
| quantum-simulation | 8 |
| grover | 7 |
| quantum-SVM | 6 |
| VQE | 5 |
| QUBO | 4 |
| amplitude-estimation | 4 |
| quantum-annealing | 4 |
| HHL | 2 |
| quantum-walk | 2 |

## Open Questions

- How do quantum algorithms for financial services perform under real-world noise and decoherence conditions? — [[2026_DECCANINTERNATIONALACADEMICPUBLISHERS_QuantumComputingAlgorithms]]
- What are the specific hardware requirements (e.g., qubit count, error rates) for achieving quantum advantage in financial applications? — [[2026_DECCANINTERNATIONALACADEMICPUBLISHERS_QuantumComputingAlgorithms]]
- How do quantum approaches compare to state-of-the-art classical methods in terms of speed, accuracy, and cost for financial use cases? — [[2026_DECCANINTERNATIONALACADEMICPUBLISHERS_QuantumComputingAlgorithms]]
- What are the data preprocessing and encoding challenges for applying quantum algorithms to real financial datasets? — [[2026_DECCANINTERNATIONALACADEMICPUBLISHERS_QuantumComputingAlgorithms]]
- How can hybrid quantum-classical frameworks be optimized for financial services applications? — [[2026_DECCANINTERNATIONALACADEMICPUBLISHERS_QuantumComputingAlgorithms]]
- What are the limitations of current quantum cloud platforms for deploying financial algorithms at scale? — [[2026_DECCANINTERNATIONALACADEMICPUBLISHERS_QuantumComputingAlgorithms]]
- Conduct empirical studies to validate the performance of quantum algorithms in financial services on real hardware — [[2026_DECCANINTERNATIONALACADEMICPUBLISHERS_QuantumComputingAlgorithms]]
- Develop noise-resilient quantum algorithms tailored for financial optimization and risk analysis — [[2026_DECCANINTERNATIONALACADEMICPUBLISHERS_QuantumComputingAlgorithms]]
- Explore hybrid quantum-classical approaches for near-term financial applications — [[2026_DECCANINTERNATIONALACADEMICPUBLISHERS_QuantumComputingAlgorithms]]
- Investigate the scalability of quantum algorithms for large-scale financial datasets — [[2026_DECCANINTERNATIONALACADEMICPUBLISHERS_QuantumComputingAlgorithms]]
