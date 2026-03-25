# High Frequency Trading

**Papers:** 8 | **Empirical:** 2 | **Theoretical:** 2 | **Review:** 1

## Papers

| Paper | Year | Source Type | Methods | QA Claim | Relevance |
|-------|------|-------------|---------|----------|-----------|
| [[2026_C_AdvancingStockPrice]] | 2026 | peer-reviewed-empirical | quantum-ML, quantum-SVM, quantum-annealing, variational, classical-simulation | demonstrated | high |
| [[2025_Benamer_VariationalQuantumAlgorithms]] | 2025 | preprint | QAOA, VQE, quantum-ML, variational | speculative | high |
| [[2025_JETIR_QuantumFinance]] | 2025 | peer-reviewed-theoretical | QAOA, VQE, quantum-ML, amplitude-estimation, variational, classical-simulation | theoretical | high |
| [[2026_Mahmod_StateQuantumComputing]] | 2025 | review-article | HHL, QAOA, VQE, quantum-annealing, quantum-ML, quantum-SVM, variational, grover | speculative | medium |
| [[2024_KrishnaPasupuleti_QuantumAlgorithmsSolving]] | 2024 | peer-reviewed-theoretical | QAOA, VQE, quantum-annealing, amplitude-estimation, variational | theoretical | high |
| [[2025_Deshmukh_QuantumMachineLearning]] | 2024 | peer-reviewed-empirical | QAOA, VQE, quantum-ML, quantum-SVM, variational | speculative | medium |
| [[2021_Pistoia_QuantumMachineLearning]] | 2021 | preprint | HHL, quantum-ML, quantum-SVM, quantum-annealing, QUBO, variational, amplitude-estimation | speculative | high |
| [[2020_Kommadi_QuantumComputingSolutions]] | 2020 | other | QAOA, VQE, quantum-annealing, HHL, quantum-ML, quantum-SVM, variational, grover, quantum-walk, classical-simulation | speculative | medium |

## Key Findings

- [supported] The proposed hybrid QML-HFT framework reports 92.5% prediction accuracy, outperforming the baselines listed in the paper: QSVM at 85.4%, QA at 83.5%, and PCA at 82.1%. — [[2026_C_AdvancingStockPrice]]
- [supported] The framework reports 93.57% execution speed/latency improvement, compared with 41.2% for QSVM, 57.8% for QA, and 64.3% for PCA in the paper's comparison table. — [[2026_C_AdvancingStockPrice]]
- [supported] The framework reports 95.15% risk management efficiency, exceeding the paper's reported baseline values of 43.59% (QSVM), 63.79% (QA), and 84.15% (PCA). — [[2026_C_AdvancingStockPrice]]
- [supported] In the ablation study, QNN-only achieved 90.1% accuracy with 5.8 seconds processing time, QSVM-only achieved 85.4% accuracy with 6.2 seconds, and QA-only achieved 83.5% accuracy with 8.1 seconds; the full hybrid model achieved the best reported accuracy at 92.5%. — [[2026_C_AdvancingStockPrice]]
- [supported] The authors report that QSVM achieved 92.5% accuracy versus 87.3% for an LSTM baseline, and state that the difference in accuracy and speed was statistically significant with paired t-test p = 0.01. — [[2026_C_AdvancingStockPrice]]
- [supported] The paper reports a paired t-test p-value of 0.02 for improvement in execution speed and accuracy between quantum and conventional models, and an ANOVA p-value of 0.03 across models, indicating statistical significance at the 95% confidence level. — [[2026_C_AdvancingStockPrice]]
- [supported] Results were obtained using both simulation and real hardware: IBM Qiskit simulator on a classical Intel Core i7/32 GB RAM system, and IBM Falcon 5-qubit and IBM Eagle 16-qubit quantum processors. — [[2026_C_AdvancingStockPrice]]
- [supported] The study used a Kaggle stock market dataset with OHLC, adjusted close, and volume data; preprocessing included forward-filling missing values, Z-score-based outlier removal, technical indicators such as MA and RSI, Min-Max scaling for price features, log scaling for volume, and an 80/20 train-test split. — [[2026_C_AdvancingStockPrice]]
- [supported] The paper claims the hybrid model combines linear separability from QSVM, nonlinear feature extraction from QNN, and optimization from QA, and that this combination produced the strongest reported performance in the study. — [[2026_C_AdvancingStockPrice]]
- [supported] The review identifies finance as one of the major industry domains where quantum computing applications have emerged by 2025, alongside agriculture, defense, energy, healthcare, infrastructure, manufacturing, and technology. — [[2026_Mahmod_StateQuantumComputing]]
- [supported] In financial services, the review highlights two main themes in the cited literature: quantum-secure transaction infrastructure via quantum tokens/QKD and quantum-enhanced trading optimization for bond markets. — [[2026_Mahmod_StateQuantumComputing]]
- [supported] The review reports that Quantinuum and Mitsui demonstrated transmission of quantum tokens over a 10 km fiber-optic network in Tokyo for ultra-secure transaction verification, positioning no-cloning-based token schemes as a potential anti-forgery and anti-double-spending mechanism. — [[2026_Mahmod_StateQuantumComputing]]
- [supported] The review reports that HSBC and IBM presented a quantum-enabled algorithm for algorithmic bond trading in European corporate bond markets, using IBM Heron hardware with Qiskit and classical computing on production-scale trading data. — [[2026_Mahmod_StateQuantumComputing]]
- [supported] Across reviewed application areas, the paper’s synthesis suggests that near-term quantum use in industry is predominantly hybrid quantum-classical rather than fully quantum. — [[2026_Mahmod_StateQuantumComputing]]
- [supported] The review suggests that many practical quantum applications across sectors, including finance, currently focus on optimization, machine learning, and secure communications rather than fault-tolerant large-scale quantum computation. — [[2026_Mahmod_StateQuantumComputing]]
- [supported] A recurring theme across the reviewed literature is that current demonstrations are often proof-of-concept, pilot, or early commercial deployments rather than mature large-scale production systems. — [[2026_Mahmod_StateQuantumComputing]]
- [supported] The review finds broad consensus that quantum computing remains constrained by high development cost, limited accessibility, hardware scaling challenges, and shortage of specialized workforce. — [[2026_Mahmod_StateQuantumComputing]]
- [supported] The review identifies cryptography and privacy disruption as a major ethical concern, with Shor-type threats to conventional encryption motivating quantum-safe and quantum-secure financial communication approaches. — [[2026_Mahmod_StateQuantumComputing]]
- [supported] The review notes strong global public-sector momentum behind quantum technology, citing worldwide government investment exceeding $55.7 billion by 2025 and multiple international cooperation agreements. — [[2026_Mahmod_StateQuantumComputing]]
- [supported] The paper reports Quantum Neural Networks (QNNs) achieved 95% accuracy on the Fashion-MNIST dataset. — [[2025_Deshmukh_QuantumMachineLearning]]

## Methodologies Used

| Method | Papers |
|--------|--------|
| variational | 8 |
| quantum-ML | 7 |
| QAOA | 6 |
| VQE | 6 |
| quantum-SVM | 5 |
| quantum-annealing | 5 |
| classical-simulation | 3 |
| amplitude-estimation | 3 |
| HHL | 3 |
| grover | 2 |
| QUBO | 1 |
| quantum-walk | 1 |

## Open Questions

- How well do the proposed QSVM/QNN-based methods scale as qubit counts increase and larger financial datasets are used? — [[2026_C_AdvancingStockPrice]]
- To what extent do quantum noise, error rates, and limited coherence times degrade prediction accuracy and execution performance on real hardware? — [[2026_C_AdvancingStockPrice]]
- Can the reported gains be maintained on genuine high-frequency data such as tick-by-tick order book streams rather than daily stock data? — [[2026_C_AdvancingStockPrice]]
- How much of the observed performance improvement comes from simulator-based execution versus real quantum hardware? — [[2026_C_AdvancingStockPrice]]
- Will hybrid quantum-classical models outperform purely classical systems consistently under realistic production trading constraints? — [[2026_C_AdvancingStockPrice]]
- Can quantum reinforcement learning produce adaptive trading strategies that remain robust under rapidly changing market conditions? — [[2026_C_AdvancingStockPrice]]
- What level of quantum error correction or noise mitigation is required before these methods become reliable for production financial services? — [[2026_C_AdvancingStockPrice]]
- How reproducible are the results across different quantum backends, repeated runs, and alternative preprocessing choices? — [[2026_C_AdvancingStockPrice]]
- Do the proposed methods generalize across more assets, other financial instruments, and different market regimes? — [[2026_C_AdvancingStockPrice]]
- Is the claimed quantum advantage still present when compared against stronger modern classical baselines and realistic transaction-cost models? — [[2026_C_AdvancingStockPrice]]
