# Credit Scoring

**Papers:** 12 | **Empirical:** 1 | **Theoretical:** 3

## Papers

| Paper | Year | Source Type | Methods | QA Claim | Relevance |
|-------|------|-------------|---------|----------|-----------|
| [[2024_Ghysels_QuantumFinance]] | 2025 | other | quantum-annealing, QUBO, quantum-simulation | speculative | high |
| [[2025_Chawla_QuantumComputingUnderlying]] | 2025 | peer-reviewed-theoretical | QAOA, VQE, quantum-ML, quantum-SVM, amplitude-estimation, grover | theoretical | medium |
| [[2025_Hlatshwayo_TechnicalReviewQuantum]] | 2025 | preprint | QAOA, VQE, quantum-annealing, HHL, quantum-ML, quantum-SVM, amplitude-estimation, QUBO, variational, grover, quantum-walk, quantum-simulation | speculative | high |
| [[2025_JETIR_QuantumFinance]] | 2025 | peer-reviewed-theoretical | QAOA, VQE, quantum-ML, amplitude-estimation, variational, classical-simulation | theoretical | high |
| [[2025_Minati_QuantumPoweredCredit]] | 2025 | preprint | quantum-ML, variational, classical-simulation | speculative | high |
| [[2025_Mustapha_ComparativeAnalysisLoan]] | 2025 | preprint | quantum-ML, quantum-SVM, classical-simulation | speculative | high |
| [[2025_NeelotpalDey_QuantumComputingFinancial]] | 2025 | peer-reviewed-theoretical | QAOA, VQE, quantum-ML, amplitude-estimation, variational | theoretical | high |
| [[2026_Barbaresco_IqnnCsInterpretable]] | 2025 | preprint | quantum-ML, variational, classical-simulation | not-applicable | high |
| [[2023_Thakkar_ImprovedFinancialForecasting]] | 2024 | preprint | quantum-ML, variational, classical-simulation | speculative | high |
| [[2025_Deshmukh_QuantumMachineLearning]] | 2024 | peer-reviewed-empirical | QAOA, VQE, quantum-ML, quantum-SVM, variational | speculative | medium |
| [[2021_Pistoia_QuantumMachineLearning]] | 2021 | preprint | HHL, quantum-ML, quantum-SVM, quantum-annealing, QUBO, variational, amplitude-estimation | speculative | high |
| [[2020_Kommadi_QuantumComputingSolutions]] | 2020 | other | QAOA, VQE, quantum-annealing, HHL, quantum-ML, quantum-SVM, variational, grover, quantum-walk, classical-simulation | speculative | medium |

## Key Findings

- [supported] Quantum annealing hardware is currently the most reliable scaled hardware for optimization tasks in finance — [[2024_Ghysels_QuantumFinance]]
- [supported] The paper proposes and implements a hybrid quantum-classical deep neural network with row-type dependent predictive analysis (HyQuC-DeepNN-RTDPA) for credit risk assessment on separate agriculture and personal loan categories. — [[2025_Minati_QuantumPoweredCredit]]
- [supported] Experiments use a proprietary bank dataset with over 25,000 samples and 81 attributes, split into agriculture and personal loan segments with strong class imbalance. — [[2025_Minati_QuantumPoweredCredit]]
- [supported] Due to quantum simulator limitations, the experiments reduced the feature space to only the first 5 principal components, despite PCA suggesting 43 components for personal loans and 38 for agriculture loans. — [[2025_Minati_QuantumPoweredCredit]]
- [supported] On personal loans, the reported test accuracy is 0.834764, weighted F1-score is 0.875073, and Cohen's kappa is 0.334187. — [[2025_Minati_QuantumPoweredCredit]]
- [supported] On personal loans, class-wise performance is uneven: Standard loans achieve precision 0.995968 and recall 0.851724, while Sub Standard loans achieve precision 0.117647 and recall 0.250000, indicating weak minority-class detection. — [[2025_Minati_QuantumPoweredCredit]]
- [supported] On personal loans, the Doubtful class has high recall (0.966667) but low precision (0.241667), suggesting many false positives despite good sensitivity. — [[2025_Minati_QuantumPoweredCredit]]
- [supported] On agriculture loans, the reported test accuracy is 0.8112, weighted F1-score is 0.8625, and Cohen's kappa is 0.4578. — [[2025_Minati_QuantumPoweredCredit]]
- [supported] On agriculture loans, class-wise performance is also uneven: Standard loans achieve precision 0.9753 and recall 0.8516, while Sub Standard loans achieve precision 0.0552 and recall 0.6000, and Loss loans achieve precision 0.2356 and recall 0.7735. — [[2025_Minati_QuantumPoweredCredit]]
- [supported] Training and validation loss curves suggest instability and possible overfitting or weak generalization, especially for agriculture loans where validation metrics fluctuate across epochs. — [[2025_Minati_QuantumPoweredCredit]]
- [supported] The authors explicitly state that the work focuses on feasibility and performance of the hybrid framework rather than claiming transformative industry-wide impacts. — [[2025_Minati_QuantumPoweredCredit]]
- [supported] The study acknowledges major limitations including lack of confidence intervals, limited hyperparameter tuning, severe class imbalance, restricted interpretability, and computational constraints from running on a 16 GB RAM, 8-core CPU system. — [[2025_Minati_QuantumPoweredCredit]]
- [supported] The reported results are obtained under quantum simulation constraints rather than on scalable fault-tolerant quantum hardware, and the paper notes current hardware limitations in qubit count, coherence, error rates, and connectivity. — [[2025_Minati_QuantumPoweredCredit]]
- [supported] On a Kaggle loan-risk dataset with 12,638 records and 12 features, QSVM slightly outperformed classical SVM on the reported test metrics for loan default classification. — [[2025_Mustapha_ComparativeAnalysisLoan]]
- [supported] The classical SVM achieved 0.90 accuracy on 2,528 test samples, with class-0 precision/recall/F1 of 0.88/0.92/0.90 and class-1 precision/recall/F1 of 0.92/0.87/0.89. — [[2025_Mustapha_ComparativeAnalysisLoan]]
- [supported] The QSVM achieved 0.90 accuracy on 2,528 test samples, with class-0 precision/recall/F1 of 0.88/0.93/0.91 and class-1 precision/recall/F1 of 0.93/0.88/0.90. — [[2025_Mustapha_ComparativeAnalysisLoan]]
- [supported] The paper reports that QSVM had a higher true positive rate for defaults (93.2%) than SVM (92.5%) and a higher true negative rate for non-defaults (87.6%), indicating marginally better classification performance. — [[2025_Mustapha_ComparativeAnalysisLoan]]
- [supported] The SVM ROC AUC was reported as 0.898, while the QSVM ROC AUC was reported as 1.0. — [[2025_Mustapha_ComparativeAnalysisLoan]]
- [supported] The QSVM implementation used 12 qubits, a ZFeatureMap with 2 repetitions, regularization parameter C=10, and a Qiskit statevector_simulator backend. — [[2025_Mustapha_ComparativeAnalysisLoan]]
- [supported] The quantum results were obtained on a noise-free classical simulator rather than real quantum hardware. — [[2025_Mustapha_ComparativeAnalysisLoan]]

## Methodologies Used

| Method | Papers |
|--------|--------|
| quantum-ML | 11 |
| variational | 9 |
| QAOA | 6 |
| VQE | 6 |
| quantum-SVM | 6 |
| classical-simulation | 6 |
| amplitude-estimation | 5 |
| quantum-annealing | 4 |
| QUBO | 3 |
| grover | 3 |
| HHL | 3 |
| quantum-simulation | 2 |
| quantum-walk | 2 |

## Open Questions

- When will quantum computers achieve commercially viable applications in finance? — [[2024_Ghysels_QuantumFinance]]
- How can quantum algorithms be adapted to handle time-varying volatility in asset-pricing models without significant loss of accuracy? — [[2024_Ghysels_QuantumFinance]]
- What are the trade-offs between problem fidelity and quantum hardware constraints in portfolio optimization? — [[2024_Ghysels_QuantumFinance]]
- How will quantum computing impact the accuracy and speed of credit risk and derivative-pricing computations in real-world scenarios? — [[2024_Ghysels_QuantumFinance]]
- What are the long-term implications of discretizing continuous-time financial models for quantum implementation? — [[2024_Ghysels_QuantumFinance]]
- How can quantum information theory better address ambiguity in risk factors for asset pricing? — [[2024_Ghysels_QuantumFinance]]
- Develop quantum algorithms that can handle stochastic volatility models without excessive discretization — [[2024_Ghysels_QuantumFinance]]
- Explore hybrid quantum-classical approaches to bridge the gap between theoretical quantum speedups and practical financial applications — [[2024_Ghysels_QuantumFinance]]
- Investigate the use of hidden-Markov-chain models for quantum implementation in derivative pricing and credit risk — [[2024_Ghysels_QuantumFinance]]
- Expand financial-engineering programs to include quantum computing fundamentals alongside traditional finance education — [[2024_Ghysels_QuantumFinance]]
