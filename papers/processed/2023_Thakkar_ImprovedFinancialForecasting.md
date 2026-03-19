---
aliases:
- Improved Financial Forecasting via Quantum Machine Learning
- Improved Financial Forecasting via
authors:
- Sohum Thakkar
- Skander Kazdaghli
- Natansh Mathur
- Iordanis Kerenidis
- André J. Ferreira–Martins
- Samurai Brito
auto_detected: true
classification: ''
contradiction_flags:
- contradiction:classical-vs-quantum
- contradiction:scalability
doi: 10.48550/arXiv.2306.12965
evidence_type: ''
idea_tags:
- idea:near-term-feasibility
- idea:hybrid-approach
journal_or_venue: arXiv
methodology_tags:
- quantum-ML
- variational
- quantum-SVM
paper_type: ''
quantum_advantage_claim: speculative
related_papers:
- 2022_Rebentrost_QuantumMachineLearning
- 2021_Herman_QuantumAlgorithmsFinance
relevance_phase1: high
relevance_phase3: high
source_type: peer-reviewed-empirical
source_type_confidence: high
step1_date: '2026-03-19T12:46:34.779991'
step1_model: Mistral-Large-3
step2_date: '2026-03-19T12:47:28.981858'
step2_model: Mistral-Large-3
step3_date: '2026-03-19T12:48:13.367647'
step3_model: Mistral-Large-3
step4_date: '2026-03-19T12:49:21.488882'
step4_model: Mistral-Large-3
step5_date: '2026-03-19T12:50:07.930534'
step5_model: Mistral-Large-3
step6_date: '2026-03-19T12:50:31.069982'
step6_model: Mistral-Large-3
steps_completed:
- 1
- 2
- 3
- 4
- 5
- 6
tags:
- topic/credit-scoring
- topic/fraud-detection
- method/quantum-ML
- method/variational
- method/quantum-SVM
- idea/near-term-feasibility
- idea/hybrid-approach
- contradiction/classical-vs-quantum
- contradiction/scalability
title: Improved Financial Forecasting via Quantum Machine Learning
topic_tags:
- credit-scoring
- fraud-detection
year: 2024
zotero_key: ''
---

## Abstract summary
This paper explores the application of quantum machine learning techniques to enhance financial forecasting, focusing on two key use cases: churn prediction and credit risk assessment for Itaú Unibanco. The authors introduce quantum-enhanced methods, such as Determinantal Point Processes (DPPs) for Random Forest models and quantum neural networks with orthogonal and compound layers, to improve model precision and efficiency. The study demonstrates that these quantum-inspired approaches can outperform classical methods in specific scenarios, offering potential advantages both as classical ML solutions today and as scalable quantum solutions in the future.
## Methodology
The paper presents an empirical study on improving financial forecasting using quantum machine learning techniques. The research is divided into two main use cases: churn prediction and credit risk assessment. For churn prediction, the authors enhance Random Forest models using Determinantal Point Processes (DPP) sampling, both classically and via quantum algorithms. The classical DPP-Random Forest (DPP-RF) model is evaluated on a large-scale churn dataset from Itaú Unibanco, demonstrating improved precision and financial impact over baseline models. Quantum DPP sampling is tested on a scaled-down dataset using IBM's quantum processor (ibmq guadalupe), though performance degrades with increasing problem size due to hardware noise. For credit risk assessment, the authors design quantum neural network architectures with orthogonal and compound layers, which match classical performance with fewer parameters. These models are evaluated on a real-world credit risk dataset and public benchmarks. The quantum neural networks are trained classically and tested on both simulators and IBM's quantum hardware (ibm hanoi), with error mitigation techniques applied to improve results. The study highlights the potential of quantum-inspired classical methods and the challenges of current quantum hardware.

**Algorithms used:** Determinantal Point Processes (DPP), Quantum DPP Sampling, Orthogonal Neural Networks, Compound Neural Networks, Variational Quantum Classifiers (VQC)
**Frameworks:** DPPy, Qiskit, JAX, scikit-learn, ray-tune

**Experimental setup:** The experiments involve both classical and quantum computational environments. Classical DPP sampling is performed using the DPPy library on a standard CPU (Intel Core i5-8350U). Quantum DPP sampling is implemented on IBM's 16-qubit quantum processor (ibmq guadelupe) for small-scale datasets. Quantum neural networks are trained classically using JAX and tested on IBM's 27-qubit quantum processor (ibm hanoi) for inference. Simulators are used for noiseless comparisons. Error mitigation techniques, such as correlated readout mitigation and Qiskit Runtime's Sampler primitive, are applied to improve quantum hardware results.

**Dataset:** 1. Churn Prediction Dataset: 304,000 datapoints with 153 features each, representing banking customers over time, split into training (174,000) and test (130,000) sets based on time periods. The target variable is a binary flag indicating customer churn. 2. Credit Risk Dataset: Approximately 141,500 observations with 32 features (31 numerical, 1 categorical), representing SME customers, split into training (74,700) and test (66,800) sets based on time periods. The target variable indicates credit default behavior. 3. Public Benchmark Datasets: Multiple datasets from OpenML (e.g., madelon, credit-default, house-pricing, jannis, eye movements, bank-marketing, wine, california) used for further benchmarking.
## Findings
- [supported] Quantum-enhanced Determinantal Point Processes (DPP) improved Random Forest precision for churn prediction by 5.9% (from 71.6% to 77.5%) on a real-world banking dataset of 174,000 training points [confidence: exact metrics reported].
- [supported] DPP-Random Forest captured 1.35% more total withdrawals (62.77% vs. 61.42%) and 1.54% more maximum possible withdrawals (70.72% vs. 69.18%) compared to the classical benchmark, demonstrating tangible business impact.
- [supported] Quantum DPP sampling on IBM quantum hardware (ibmq_guadalupe) matched classical DPP performance for small batch dimensions (e.g., 4x2 matrices) but degraded as dimensions increased due to hardware noise [simulation vs. real hardware comparison].
- [supported] Quantum orthogonal neural networks (OrthoResNN) matched classical fully-connected neural networks in credit risk assessment (Gini score: 54.29% vs. 54.20%) while using only 13 trainable parameters instead of 64 [parameter efficiency demonstrated].
- [supported] Expectation-per-subspace compound layers (ExpResNN) achieved comparable performance to classical models (Gini score: 53.95%) with the same parameter efficiency as orthogonal layers (13 parameters).
- [supported] On public datasets, orthogonal neural networks (OrthoFNN) outperformed or matched classical feed-forward networks in 6/8 cases (e.g., wine dataset: 0.640 vs. 0.553 ROC-AUC) [cross-dataset validation].
- [speculative] Quantum DPP sampling may offer runtime advantages for large datasets (O(nd) gate complexity vs. O(d3) classical) once hardware noise is mitigated.
- [speculative] Compound layers could explore exponential Hilbert spaces more efficiently on fault-tolerant quantum hardware, potentially unlocking quantum advantage for high-dimensional financial data.
- [disputed] The paper claims quantum circuits for DPP sampling have lower complexity (O(nd) gate count), but this is disputed by classical DPP sampling advances (e.g., O(poly(d)) runtime for exact sampling [32]).

**Results summary:** The paper presents two empirical applications of quantum machine learning in finance: (1) DPP-enhanced Random Forests for churn prediction, showing 5.9% precision improvement and 1.35-1.54% gains in withdrawal capture on real banking data, with quantum DPP sampling matching classical performance only for small-scale problems due to hardware limitations; and (2) quantum neural networks for credit risk assessment, where orthogonal and compound layers matched classical performance with 5-20x fewer parameters. Results are primarily from classical simulations, with quantum hardware experiments limited to small-scale validation (≤8 qubits). The work demonstrates quantum-inspired classical improvements today, with speculative advantages for future hardware.

**Performance claims:**
- 5.9% precision improvement for churn prediction (77.5% vs. 71.6%)
- 1.35% increase in total withdrawals captured (62.77% vs. 61.42%)
- 1.54% increase in maximum possible withdrawals captured (70.72% vs. 69.18%)
- Training time: 54 minutes (DPP-RF) vs. 311 seconds (classical RF)
- OrthoResNN Gini score: 54.29% (vs. 54.20% classical) with 13 vs. 64 parameters
- ExpResNN Gini score: 53.95% with 13 parameters
- Quantum DPP sampling F1 scores comparable to classical for (4,2) and (5,2) matrices on IBM hardware
- ROC-AUC improvements on public datasets (e.g., wine: 0.640 vs. 0.553)
## Quantum advantage claim
**Classification:** speculative

The paper demonstrates quantum-inspired classical improvements (e.g., DPP sampling, orthogonal layers) with empirical support, but quantum advantage claims are speculative. Hardware experiments show quantum DPP sampling matches classical performance only for small problems (≤6 qubits), with no demonstrated advantage. Theoretical complexity advantages (e.g., O(nd) gate count for DPP) are noted but not empirically validated on real hardware. Compound layers' exponential space exploration is proposed as a future advantage contingent on fault-tolerant hardware.
## Limitations
- Experiments on quantum DPP sampling were limited to small batch dimensions (up to (6,2)) due to hardware noise on the IBM quantum processor
- Quantum DPP sampling results degraded as matrix dimensions grew, highlighting current hardware limitations
- Classical DPP-RF model training time was significantly longer (54 minutes) compared to the benchmark Random Forest (311 seconds) due to DPP sampling complexity
- Quantum DPP circuits were tested only on a scaled-down version of the churn dataset (~1000 points) rather than the full dataset (174,000 points)
- Hardware experiments for quantum neural networks were limited to a small test subsample (300 points) instead of the full test set (66,750 points)
- Quantum hardware noise significantly impacted the performance of the ExpFNN model, yielding a Gini score of 40.20% compared to the noiseless simulation score of 53.90%
- [inferred] No comparison with state-of-the-art classical machine learning models beyond Random Forest and standard neural networks
- [inferred] Limited exploration of noise mitigation techniques beyond basic hamming-weight postselection for quantum DPP sampling
- [inferred] Lack of detailed analysis on the impact of decoherence and gate errors on quantum circuit performance
- [inferred] No assessment of the financial cost-benefit trade-off for deploying quantum-enhanced models in production
## Open questions
- How does the quantum DPP-RF algorithm perform on full-scale datasets (e.g., 174,000 points) with improved quantum hardware?
- What is the scalability of quantum neural networks with orthogonal and compound layers for larger feature dimensions (e.g., >32 features)?
- Can quantum machine learning models maintain their performance advantages when trained directly on quantum hardware, rather than via classical simulation?
- What is the impact of different error mitigation techniques on the performance of quantum DPP sampling for larger matrix dimensions?
- How do quantum-enhanced models compare to advanced classical techniques like gradient-boosted trees or transformer-based models for financial forecasting?
- What are the specific hardware requirements (qubit count, coherence time, gate fidelity) for achieving a practical quantum advantage in financial forecasting?
- How does the performance of quantum models degrade with increasing dataset noise or missing values in real-world financial data?
- What are the implications of quantum machine learning for regulatory compliance and explainability in financial services?

**Future work:**
- Test quantum DPP-RF and neural network models on larger datasets with improved quantum hardware (e.g., IBM Eagle or Heron processors)
- Explore hybrid quantum-classical training approaches to leverage the strengths of both paradigms
- Develop more efficient classical simulators for quantum compound layers to enable larger-scale experiments
- Investigate advanced error mitigation techniques (e.g., zero-noise extrapolation, probabilistic error cancellation) for quantum DPP sampling and neural networks
- Extend quantum machine learning models to other financial use cases, such as fraud detection, algorithmic trading, or risk management
- Benchmark quantum models against state-of-the-art classical techniques (e.g., XGBoost, deep learning) on diverse financial datasets
- Assess the financial and operational feasibility of deploying quantum-enhanced models in production environments
- Develop quantum-inspired classical algorithms that retain performance advantages while being deployable on existing infrastructure
- Explore the use of quantum generative models for synthetic data generation in financial forecasting
- Investigate the interpretability and explainability of quantum machine learning models for regulatory compliance
## Key ideas
- #idea:near-term-feasibility — Quantum-enhanced DPPs improve Random Forest precision by 5.9% (77.5% vs. 71.6%) for churn prediction on real-world banking data, demonstrating tangible business impact (1.35-1.54% gains in withdrawal capture).
- #idea:hybrid-approach — Hybrid quantum-classical models (e.g., DPP-RF, orthogonal neural networks) match or exceed classical performance with fewer parameters (13 vs. 64), suggesting efficiency gains in near-term deployments.
- #idea:near-term-feasibility — Quantum DPP sampling on IBM hardware (ibmq_guadalupe) matches classical performance for small-scale problems (≤6 qubits), validating NISQ-era applicability for constrained use cases.
- #limitation:noise — Quantum DPP sampling degrades for larger matrix dimensions due to hardware noise, underscoring current NISQ limitations for scaling to real-world datasets.
- #limitation:qubit-count — Experiments are restricted to small datasets (e.g., 1,000 points) and low-dimensional matrices (6x2) due to insufficient qubits, highlighting hardware constraints for financial applications.
- #idea:hybrid-approach — Quantum-inspired classical methods (e.g., orthogonal neural networks) outperform or match classical baselines on 6/8 public datasets, offering immediate deployable improvements.
## Contradictions
- #contradiction:classical-vs-quantum — The paper claims quantum DPP sampling has lower complexity (O(nd) gate count), but this is disputed by classical DPP advances achieving O(poly(d)) runtime for exact sampling [32].
- #contradiction:scalability — While the paper speculates quantum DPP may offer runtime advantages for large datasets, empirical results show performance degradation beyond small dimensions (e.g., >6 qubits), contradicting scalability claims.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
