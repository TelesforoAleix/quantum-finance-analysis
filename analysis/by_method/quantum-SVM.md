# Quantum SVM

**Papers:** 14 | **Empirical:** 2 | **Theoretical:** 3 | **Review:** 3

## Papers

| Paper | Year | Source Type | Topics | QA Claim | Relevance |
|-------|------|-------------|--------|----------|-----------|
| [[2026_C_AdvancingStockPrice]] | 2026 | peer-reviewed-empirical | high-frequency-trading, risk-modelling | demonstrated | high |
| [[2026_Nawaz_ExploringQuantumMachine]] | 2026 | review-article | portfolio-optimisation, risk-modelling, derivatives-pricing, fraud-detection | theoretical | medium |
| [[2025_Chawla_QuantumComputingUnderlying]] | 2025 | peer-reviewed-theoretical | portfolio-optimisation, risk-modelling, fraud-detection, credit-scoring, quantum-cryptography, market-simulation | theoretical | medium |
| [[2025_Hlatshwayo_TechnicalReviewQuantum]] | 2025 | preprint | portfolio-optimisation, risk-modelling, derivatives-pricing, fraud-detection, credit-scoring, asset-pricing, quantum-cryptography, market-simulation | speculative | high |
| [[2025_Mustapha_ComparativeAnalysisLoan]] | 2025 | preprint | credit-scoring, risk-modelling | speculative | high |
| [[2025_Vangibhuratha_QuantumMachineLearning]] | 2025 | peer-reviewed-theoretical | portfolio-optimisation | theoretical | high |
| [[2026_Mahmod_StateQuantumComputing]] | 2025 | review-article | quantum-cryptography, high-frequency-trading | speculative | medium |
| [[2024_Bhasin_EnhancingQuantumMachine]] | 2024 | conference-paper | portfolio-optimisation, risk-modelling, asset-pricing | speculative | high |
| [[2024_Gujju_QuantumMachineLearning]] | 2024 | review-article | fraud-detection, derivatives-pricing | disputed | high |
| [[2024_Unknown_QuantumMachineLearning]] | 2024 | peer-reviewed-theoretical | — | theoretical | medium |
| [[2025_Deshmukh_QuantumMachineLearning]] | 2024 | peer-reviewed-empirical | portfolio-optimisation, risk-modelling, fraud-detection, credit-scoring, high-frequency-trading | speculative | medium |
| [[2023_S_PotentialQuantumTechniques]] | 2023 | preprint | asset-pricing | speculative | medium |
| [[2021_Pistoia_QuantumMachineLearning]] | 2021 | preprint | asset-pricing, fraud-detection, credit-scoring, high-frequency-trading, derivatives-pricing, risk-modelling | speculative | high |
| [[2020_Kommadi_QuantumComputingSolutions]] | 2020 | other | portfolio-optimisation, risk-modelling, derivatives-pricing, fraud-detection, credit-scoring, high-frequency-trading, asset-pricing, quantum-cryptography | speculative | medium |

## Topics Using This Method

| Topic | Papers |
|-------|--------|
| risk-modelling | 9 |
| portfolio-optimisation | 7 |
| fraud-detection | 7 |
| credit-scoring | 6 |
| high-frequency-trading | 5 |
| derivatives-pricing | 5 |
| asset-pricing | 5 |
| quantum-cryptography | 4 |
| market-simulation | 2 |

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
- [supported] The review identifies QAOA, VQE, QNNs, QSVMs, Grover-based methods, QPCA, and quantum k-means as the main QML approaches studied for optimization across finance, logistics, AI, and chemistry. — [[2026_Nawaz_ExploringQuantumMachine]]
- [supported] Across the reviewed literature, the paper finds a broad theme that QML methods show potential for exploring large solution spaces, faster convergence, and improved optimization performance relative to some classical approaches, but this is not established as a general empirical superiority. — [[2026_Nawaz_ExploringQuantumMachine]]
- [supported] The review concludes that QAOA and VQE are the most prominent optimization-oriented QML methods, with QAOA emphasized for combinatorial optimization and VQE for energy/molecular optimization. — [[2026_Nawaz_ExploringQuantumMachine]]
- [supported] The review identifies portfolio optimization in finance as a key application area, arguing that QAOA, VQE, and Grover-style search are being explored for asset allocation, risk management, and option-pricing-related tasks. — [[2026_Nawaz_ExploringQuantumMachine]]
- [supported] A consensus theme in the reviewed literature is that current practical deployment is constrained by NISQ-era limitations, especially quantum noise, decoherence, limited qubit counts, and shallow-circuit requirements. — [[2026_Nawaz_ExploringQuantumMachine]]
- [supported] The review finds that hybrid quantum-classical approaches are the dominant practical strategy in current QML optimization work and are presented as the most feasible near-term path to real-world use. — [[2026_Nawaz_ExploringQuantumMachine]]
- [supported] The review highlights scalability as a major unresolved issue, with larger real-world optimization problems still difficult to handle because qubit availability, coherence time, and error-correction overhead remain insufficient. — [[2026_Nawaz_ExploringQuantumMachine]]
- [supported] The review identifies noise sensitivity and error accumulation as recurring limitations for iterative variational methods such as QAOA and VQE, reducing reliability on current hardware. — [[2026_Nawaz_ExploringQuantumMachine]]
- [supported] The review notes that algorithm design issues, including ansatz selection, parameter tuning, and quantum-classical interface overhead, materially affect optimization quality and convergence. — [[2026_Nawaz_ExploringQuantumMachine]]
- [supported] The review finds that QNNs and QSVMs are frequently positioned for learning-based optimization and classification tasks, but their practical value is limited by trainability issues, barren plateaus, and hardware instability. — [[2026_Nawaz_ExploringQuantumMachine]]
- [supported] The review reports that QPCA and Grover-based methods are commonly associated with theoretical speedup claims, but their practical usefulness is limited by hardware requirements and implementation difficulty. — [[2026_Nawaz_ExploringQuantumMachine]]
