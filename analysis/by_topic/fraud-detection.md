# Fraud Detection

**Papers:** 13 | **Empirical:** 2 | **Theoretical:** 5 | **Review:** 2

## Papers

| Paper | Year | Source Type | Methods | QA Claim | Relevance |
|-------|------|-------------|---------|----------|-----------|
| [[2026_Nawaz_ExploringQuantumMachine]] | 2026 | review-article | QAOA, VQE, quantum-ML, quantum-SVM, variational, grover | theoretical | medium |
| [[2025_Akinyemi_BigDataFinancial]] | 2025 | peer-reviewed-theoretical | — | speculative | medium |
| [[2025_Chawla_QuantumComputingUnderlying]] | 2025 | peer-reviewed-theoretical | QAOA, VQE, quantum-ML, quantum-SVM, amplitude-estimation, grover | theoretical | medium |
| [[2025_Hlatshwayo_TechnicalReviewQuantum]] | 2025 | preprint | QAOA, VQE, quantum-annealing, HHL, quantum-ML, quantum-SVM, amplitude-estimation, QUBO, variational, grover, quantum-walk, quantum-simulation | speculative | high |
| [[2025_JETIR_QuantumFinance]] | 2025 | peer-reviewed-theoretical | QAOA, VQE, quantum-ML, amplitude-estimation, variational, classical-simulation | theoretical | high |
| [[2025_NeelotpalDey_QuantumComputingFinancial]] | 2025 | peer-reviewed-theoretical | QAOA, VQE, quantum-ML, amplitude-estimation, variational | theoretical | high |
| [[2025_ThirumalGunasekaran_ExploringRevolutionaryPotential]] | 2025 | peer-reviewed-theoretical | grover, quantum-ML, classical-simulation | theoretical | high |
| [[2023_Thakkar_ImprovedFinancialForecasting]] | 2024 | preprint | quantum-ML, variational, classical-simulation | speculative | high |
| [[2024_Gujju_QuantumMachineLearning]] | 2024 | review-article | quantum-ML, quantum-SVM, VQE, variational | disputed | high |
| [[2024_Mitsuda_ApproximateComplexAmplitude]] | 2024 | peer-reviewed-empirical | quantum-ML, variational, classical-simulation | speculative | high |
| [[2025_Deshmukh_QuantumMachineLearning]] | 2024 | peer-reviewed-empirical | QAOA, VQE, quantum-ML, quantum-SVM, variational | speculative | medium |
| [[2021_Pistoia_QuantumMachineLearning]] | 2021 | preprint | HHL, quantum-ML, quantum-SVM, quantum-annealing, QUBO, variational, amplitude-estimation | speculative | high |
| [[2020_Kommadi_QuantumComputingSolutions]] | 2020 | other | QAOA, VQE, quantum-annealing, HHL, quantum-ML, quantum-SVM, variational, grover, quantum-walk, classical-simulation | speculative | medium |

## Key Findings

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
- [supported] The review identifies an area of disagreement across the literature: while many studies claim speedups or improved optimization behavior, the paper also notes that classical methods remain competitive in several domains and that practical quantum benefit is often hardware-dependent. — [[2026_Nawaz_ExploringQuantumMachine]]
- [supported] The review identifies future research priorities as scalable hardware, improved qubit coherence, advanced error correction, better hybrid models, and new quantum heuristics tailored to sectors such as banking, healthcare, and logistics. — [[2026_Nawaz_ExploringQuantumMachine]]
- [supported] The paper's main supported conclusions concern big data rather than quantum computing: big data and real-time analytics can improve speed, precision, and comprehensiveness of financial risk management when paired with strong governance and compliance controls. — [[2025_Akinyemi_BigDataFinancial]]
- [supported] The paper reports illustrative case-study claims that real-time analytics reduced fraud response time to within two seconds, saved $4.5 million, reduced complaints by 65%, predicted liquidity issues up to 48 hours ahead, and saved $12 million during a crisis, though these are not quantum-related results. — [[2025_Akinyemi_BigDataFinancial]]
- [supported] A DPP-enhanced Random Forest (DPP-RF) improved churn-prediction precision at 6% recall from 71.6% to 77.5%, an increase of 5.9 percentage points on the bank dataset. — [[2023_Thakkar_ImprovedFinancialForecasting]]
- [supported] On the churn use case, DPP-RF increased the average share of total withdrawals captured among the top 500 flagged customers from 61.42% to 62.77%, a gain of 1.35 percentage points over 11 test months. — [[2023_Thakkar_ImprovedFinancialForecasting]]
- [supported] On the same churn task, DPP-RF increased the average share of maximum possible withdrawals captured from 69.18% to 70.72%, a gain of 1.54 percentage points. — [[2023_Thakkar_ImprovedFinancialForecasting]]
- [supported] The classical DPP-RF model trained much more slowly than the benchmark Random Forest, taking 54 minutes versus 311 seconds, with DPP sampling identified as the computational bottleneck. — [[2023_Thakkar_ImprovedFinancialForecasting]]
- [supported] On several OpenML tabular classification benchmarks, DPP-RF sometimes modestly outperformed standard Random Forest in ROC-AUC, but gains were dataset-dependent and not universal. — [[2023_Thakkar_ImprovedFinancialForecasting]]

## Methodologies Used

| Method | Papers |
|--------|--------|
| quantum-ML | 12 |
| variational | 10 |
| VQE | 8 |
| QAOA | 7 |
| quantum-SVM | 7 |
| grover | 5 |
| amplitude-estimation | 5 |
| classical-simulation | 5 |
| quantum-annealing | 3 |
| HHL | 3 |
| QUBO | 2 |
| quantum-walk | 2 |
| quantum-simulation | 1 |

## Open Questions

- When and under what conditions will QML deliver practical quantum advantage over classical optimization methods in real-world settings such as finance and logistics? — [[2026_Nawaz_ExploringQuantumMachine]]
- How can QML algorithms be scaled beyond current NISQ-era qubit and coherence limitations? — [[2026_Nawaz_ExploringQuantumMachine]]
- What are the most effective noise-mitigation and error-correction strategies for optimization-focused QML algorithms? — [[2026_Nawaz_ExploringQuantumMachine]]
- How should hybrid quantum-classical workflows be designed to minimize communication overhead and maximize optimization efficiency? — [[2026_Nawaz_ExploringQuantumMachine]]
- What ansatz designs are most effective for different classes of optimization problems? — [[2026_Nawaz_ExploringQuantumMachine]]
- How can barren plateaus, vanishing gradients, and trainability issues in QNNs be mitigated at larger qubit counts? — [[2026_Nawaz_ExploringQuantumMachine]]
- How can QML models be regularized to avoid overfitting and improve generalization on unseen data? — [[2026_Nawaz_ExploringQuantumMachine]]
- Which industries and problem classes are most likely to benefit first from domain-specific quantum algorithms? — [[2026_Nawaz_ExploringQuantumMachine]]
- For finance specifically, how well do QML methods perform on realistic portfolio optimization problems with market uncertainty, regulatory constraints, and large asset universes? — [[2026_Nawaz_ExploringQuantumMachine]]
- How robust are reported QML advantages when compared against strong modern classical heuristics and optimization solvers? — [[2026_Nawaz_ExploringQuantumMachine]]
