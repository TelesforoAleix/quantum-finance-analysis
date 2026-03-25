# Market Simulation

**Papers:** 12 | **Empirical:** 2 | **Theoretical:** 6

## Papers

| Paper | Year | Source Type | Methods | QA Claim | Relevance |
|-------|------|-------------|---------|----------|-----------|
| [[2026_Gnal_QuantumComputingApproaches]] | 2026 | peer-reviewed-theoretical | quantum-annealing, VQE, QUBO, variational | theoretical | high |
| [[2026_Gnal_ScenarioBasedMacroeconomic]] | 2026 | peer-reviewed-theoretical | quantum-annealing, quantum-ML, amplitude-estimation, variational | theoretical | high |
| [[2026_Prasad_QuantumAlgorithmsStochastic]] | 2026 | preprint | HHL, amplitude-estimation, quantum-simulation, variational, quantum-ML, classical-simulation | speculative | high |
| [[2025_Chawla_QuantumComputingUnderlying]] | 2025 | peer-reviewed-theoretical | QAOA, VQE, quantum-ML, quantum-SVM, amplitude-estimation, grover | theoretical | medium |
| [[2025_Ganguly_HybridClassicalQuantum]] | 2025 | conference-paper | quantum-ML, QUBO, variational, classical-simulation | speculative | high |
| [[2025_Hlatshwayo_TechnicalReviewQuantum]] | 2025 | preprint | QAOA, VQE, quantum-annealing, HHL, quantum-ML, quantum-SVM, amplitude-estimation, QUBO, variational, grover, quantum-walk, quantum-simulation | speculative | high |
| [[2025_NeelotpalDey_QuantumComputingFinancial]] | 2025 | peer-reviewed-theoretical | QAOA, VQE, quantum-ML, amplitude-estimation, variational | theoretical | high |
| [[2024_Mustafa_QuantumGraphNeural]] | 2024 | peer-reviewed-empirical | quantum-ML, variational, classical-simulation | not-applicable | medium |
| [[2022_Albareti_StructuredSurveyQuantum]] | 2022 | preprint | QAOA, VQE, quantum-annealing, HHL, amplitude-estimation, QUBO, variational, classical-simulation | speculative | high |
| [[2022_Herbert_QuantumMonteCarlo]] | 2022 | peer-reviewed-theoretical | amplitude-estimation, quantum-simulation | theoretical | high |
| [[2021_Coyle_QuantumVersusClassical]] | 2021 | peer-reviewed-empirical | quantum-ML, variational, classical-simulation | speculative | high |
| [[2021_Kubo_VariationalQuantumSimulations]] | 2021 | peer-reviewed-theoretical | variational, amplitude-estimation, quantum-simulation, classical-simulation | theoretical | high |

## Key Findings

- [supported] For linear and semilinear SDEs with Lipschitz coefficients, quantum algorithms estimate relevant quantities (option prices, expected hitting times, moments) to accuracy ε in time ˜O(poly(d)polylog(1/ε)), versus classical O(poly(d)/ε²). — [[2026_Prasad_QuantumAlgorithmsStochastic]]
- [supported] Quantum simulation of the Fokker-Planck equation achieves accuracy ε in time ˜O(d · log(1/ε)), compared to classical finite-difference solvers at O(n^{d+1}_s). — [[2026_Prasad_QuantumAlgorithmsStochastic]]
- [supported] Numerical simulations on small instances (e.g., 2D Black-Scholes, 3D Langevin) demonstrate polynomial-to-super-polynomial empirical speedups in accuracy for fixed runtime. — [[2026_Prasad_QuantumAlgorithmsStochastic]]
- [supported] Resource requirements for d-dimensional SDEs: ~150 qubits for d=10, ε=10⁻³, and δx=10⁻² in finance applications. — [[2026_Prasad_QuantumAlgorithmsStochastic]]
- [supported] On NVIDIA stock data over 210 days, QLSTM achieved lower test loss than classical LSTM (5.5×10^-3 vs 6.8×10^-3), while LSTM achieved lower training loss (4.5×10^-3 vs 7.2×10^-3). — [[2025_Ganguly_HybridClassicalQuantum]]
- [supported] On the same stock task, QLSTM had worse RMSE than LSTM on both training and test sets according to the reported table (training RMSE 19.05×10^-3 vs 7.5×10^-3; test RMSE 15.09×10^-3 vs 12.8×10^-3), which conflicts with the paper's narrative that QLSTM predictions were more accurate. — [[2025_Ganguly_HybridClassicalQuantum]]
- [supported] QLSTM training was substantially slower than classical LSTM across hardware platforms; per-epoch training times without CUDA-Q were 1600s vs 18s on RTX 3060, 780s vs 12s on RTX 3070, and 22s vs 0.05s on Apple M3. — [[2025_Ganguly_HybridClassicalQuantum]]
- [supported] CUDA-Q acceleration greatly reduced simulated QLSTM training time, e.g., from 780s to 18s per epoch on RTX 3070 and from 1600s to 500s on RTX 3060. — [[2025_Ganguly_HybridClassicalQuantum]]
- [supported] The qGAN was trained on real Binance cryptocurrency data from five pairs with over 5000 samples, using batches of 1000 and 2000 training epochs, and the generator/discriminator losses reportedly behaved as expected and approached equilibrium. — [[2025_Ganguly_HybridClassicalQuantum]]
- [supported] After qGAN-based distribution learning and subsequent QUBO optimization, the method selected BNBBTC as the cryptocurrency predicted to offer the maximum return in the studied snapshot. — [[2025_Ganguly_HybridClassicalQuantum]]
- [supported] For the QCBM experiment on a synthetic 2×2 bars-and-stripes dataset, SPSA produced a simulated distribution visually close to the target distribution. — [[2025_Ganguly_HybridClassicalQuantum]]
- [supported] The QCBM comparison found that SPSA gave the closest simulated distribution to the real distribution, while the text also states COBYLA gave better optimizer results overall, indicating some ambiguity in optimizer ranking. — [[2025_Ganguly_HybridClassicalQuantum]]
- [supported] The proposed hybrid quantum-classical graph neural network (QGNN) was implemented and evaluated entirely on a noiseless Pennylane simulator rather than real quantum hardware. — [[2024_Mustafa_QuantumGraphNeural]]
- [supported] On the Cora benchmark, the best QGNN variant (strongly entangled layers) achieved 59.6% test accuracy with training cross-entropy loss 1.4246, underperforming comparable classical GCN baselines that achieved 65.2% and 79.0% accuracy. — [[2024_Mustafa_QuantumGraphNeural]]
- [supported] On PCA-reduced Cora data, QGNN variants performed substantially worse than classical GCNs: amplitude encoding reached 45.4% accuracy, strongly entangled QGNN 45.8%, and simple entangled QGNN 39.1%, versus 79.1% for both classical GCN baselines. — [[2024_Mustafa_QuantumGraphNeural]]
- [supported] For NIFTY50 stock-movement direction prediction, QGNN variants produced F1 scores broadly similar to classical baselines, with the strongly entangled QGNN outperforming the GCN in sparse and balanced graph settings on F1 score. — [[2024_Mustafa_QuantumGraphNeural]]
- [supported] In the sparse stock graph, the strongly entangled QGNN achieved F1 score 0.5879 and ROC-AUC 0.5385 versus GCN F1 score 0.5787 and ROC-AUC 0.4800. — [[2024_Mustafa_QuantumGraphNeural]]
- [supported] In the balanced stock graph, the strongly entangled QGNN achieved F1 score 0.5817 and ROC-AUC 0.4959 versus GCN F1 score 0.5630 and ROC-AUC 0.4900. — [[2024_Mustafa_QuantumGraphNeural]]
- [supported] In the dense stock graph, the classical GCN achieved the highest F1 score at 0.5983, exceeding the strongly entangled QGNN at 0.5887, although the QGNN had higher ROC-AUC (0.5302 vs 0.4811). — [[2024_Mustafa_QuantumGraphNeural]]
- [supported] The authors conclude that the hybrid model is viable for financial time-series forecasting but does not clearly outperform classical methods overall. — [[2024_Mustafa_QuantumGraphNeural]]

## Methodologies Used

| Method | Papers |
|--------|--------|
| variational | 10 |
| quantum-ML | 8 |
| amplitude-estimation | 8 |
| classical-simulation | 6 |
| VQE | 5 |
| quantum-annealing | 4 |
| QUBO | 4 |
| quantum-simulation | 4 |
| QAOA | 4 |
| HHL | 3 |
| quantum-SVM | 2 |
| grover | 2 |
| quantum-walk | 1 |

## Open Questions

- Under what conditions can hybrid quantum-classical methods outperform advanced classical portfolio optimization techniques in practice? — [[2026_Gnal_QuantumComputingApproaches]]
- How much of the theoretical quantum advantage survives when realistic hardware noise and limited qubit resources are taken into account? — [[2026_Gnal_QuantumComputingApproaches]]
- Can quantum-enhanced sampling materially improve estimation of tail-risk measures such as VaR and CVaR for realistic portfolios? — [[2026_Gnal_QuantumComputingApproaches]]
- How scalable are QUBO-based and variational formulations when the asset universe grows to hundreds or thousands of securities? — [[2026_Gnal_QuantumComputingApproaches]]
- What are the most effective ways to encode portfolio constraints and uncertainty scenarios into quantum optimization frameworks? — [[2026_Gnal_QuantumComputingApproaches]]
- How should interpretability and transparency be ensured so that quantum-generated portfolio decisions satisfy regulatory and governance requirements? — [[2026_Gnal_QuantumComputingApproaches]]
- Which classes of market uncertainty or dependency structures are most likely to benefit from quantum methods? — [[2026_Gnal_QuantumComputingApproaches]]
- What validation standards and benchmarking protocols are needed for financial institutions to trust quantum-assisted optimization outputs? — [[2026_Gnal_QuantumComputingApproaches]]
- Develop and test practical hybrid quantum-classical portfolio optimization architectures. — [[2026_Gnal_QuantumComputingApproaches]]
- Address NISQ-era limitations such as hardware noise and limited scalability to improve feasibility. — [[2026_Gnal_QuantumComputingApproaches]]
