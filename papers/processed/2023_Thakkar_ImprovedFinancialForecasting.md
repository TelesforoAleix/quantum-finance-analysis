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
related_papers: []
relevance_phase1: high
relevance_phase3: medium
source_type: peer-reviewed-empirical
source_type_confidence: high
step1_date: '2026-03-19T23:36:01.693281'
step1_model: Mistral-Large-3
step2_date: '2026-03-19T23:36:06.198116'
step2_model: Mistral-Large-3
step3_date: '2026-03-19T12:48:13.367647'
step3_model: Mistral-Large-3
step4_date: '2026-03-19T23:36:38.836547'
step4_model: Mistral-Large-3
step5_date: '2026-03-19T23:46:57.563527'
step5_model: Mistral-Large-3
step6_date: '2026-03-19T23:47:01.927648'
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
This paper explores the application of quantum machine learning techniques to enhance financial forecasting, specifically in churn prediction and credit risk assessment for Itaú Unibanco. The authors introduce quantum-enhanced methods, such as Determinantal Point Processes (DPPs) for Random Forest models and quantum neural networks with orthogonal and compound layers, to improve model precision and efficiency. The study demonstrates that these quantum-inspired approaches can achieve comparable or superior performance to classical methods while using fewer parameters, highlighting their potential for future quantum hardware advancements.
## Methodology
The paper presents an empirical study on improving financial forecasting using quantum machine learning techniques. The research is divided into two main use cases: churn prediction and credit risk assessment. For churn prediction, the authors enhance Random Forest models using Determinantal Point Processes (DPP) sampling, both classically and via quantum algorithms. The classical DPP-Random Forest (DPP-RF) model is evaluated on a large-scale churn dataset from Itaú Unibanco, demonstrating improved precision and financial impact over baseline models. Quantum DPP sampling is tested on a scaled-down dataset using IBM's quantum processor (ibmq guadalupe), though performance degrades with increasing problem size due to hardware noise. For credit risk assessment, the authors design quantum neural network architectures with orthogonal and compound layers, which match classical performance with fewer parameters. These models are evaluated on a real-world credit risk dataset and public benchmarks. The quantum neural networks are trained classically and tested on both simulators and IBM's quantum hardware (ibm hanoi), with error mitigation techniques applied to improve results. The study highlights the potential of quantum-inspired classical methods and the challenges of current quantum hardware.

**Algorithms used:** Determinantal Point Processes (DPP), Quantum DPP Sampling, Orthogonal Neural Networks, Compound Neural Networks, Variational Quantum Classifiers (VQC)
**Frameworks:** DPPy, Qiskit, JAX, scikit-learn, ray-tune

**Experimental setup:** The experiments involve both classical and quantum computational environments. Classical DPP sampling is performed using the DPPy library on a standard CPU (Intel Core i5-8350U). Quantum DPP sampling is implemented on IBM's 16-qubit quantum processor (ibmq guadelupe) for small-scale datasets. Quantum neural networks are trained classically using JAX and tested on IBM's 27-qubit quantum processor (ibm hanoi) for inference. Simulators are used for noiseless comparisons. Error mitigation techniques, such as correlated readout mitigation and Qiskit Runtime's Sampler primitive, are applied to improve quantum hardware results.

**Dataset:** 1. Churn Prediction Dataset: 304,000 datapoints with 153 features each, representing banking customers over time, split into training (174,000) and test (130,000) sets based on time periods. The target variable is a binary flag indicating customer churn. 2. Credit Risk Dataset: Approximately 141,500 observations with 32 features (31 numerical, 1 categorical), representing SME customers, split into training (74,700) and test (66,800) sets based on time periods. The target variable indicates credit default behavior. 3. Public Benchmark Datasets: Multiple datasets from OpenML (e.g., madelon, credit-default, house-pricing, jannis, eye movements, bank-marketing, wine, california) used for further benchmarking.
## Findings
- [supported] Classical DPP-enhanced Random Forest models improved precision for churn prediction by 5.9% (from 71.6% to 77.5%) compared to baseline Random Forest models on a real-world banking dataset
- [supported] DPP-RF models captured 1.35% more total withdrawals and 1.54% more maximum possible withdrawals than benchmark models, demonstrating tangible business impact
- [supported] DPP-RF models achieved comparable or better ROC-AUC scores than Random Forest models across 8 public classification datasets, with the largest improvement (0.916 to 0.941) on the madelon dataset
- [supported] Quantum DPP sampling on IBM hardware (ibmq guadalupe) matched classical DPP performance for small matrix dimensions (up to (6,2)) but degraded for larger dimensions due to hardware noise
- [supported] Quantum orthogonal neural networks (OrthoResNN) matched classical fully-connected neural networks in credit risk prediction (Gini score of 54.29% vs 54.20%) while using only 13 trainable parameters instead of 64
- [supported] Quantum compound neural networks (ExpResNN) achieved similar performance to classical networks (Gini score of 53.95%) with the same parameter efficiency as orthogonal networks (13 parameters)
- [supported] Orthogonal neural networks outperformed classical fully-connected networks on 5 of 8 public datasets, with the largest improvement (0.553 to 0.640 ROC-AUC) on the wine dataset
- [supported] Quantum hardware inference (ibm hanoi) for OrthoResNN achieved a Gini score of 50.19% (vs 54.19% in noiseless simulation), while ExpFNN achieved only 40.20% (vs 53.90% in simulation) due to noise sensitivity
- [speculative] Quantum DPP sampling could reduce runtime complexity from O(d^3) classically to O(d log(n)) on quantum hardware for large datasets
- [speculative] Compound neural networks may offer advantages for larger datasets when better quantum hardware becomes available, despite current classical simulation limitations

**Results summary:** The paper presents empirical results from two financial use cases: churn prediction and credit risk assessment. For churn prediction, classical DPP-enhanced Random Forest models demonstrated measurable improvements in precision (5.9% increase) and business metrics (1.35-1.54% improvement in withdrawals captured) over baseline Random Forest models, though with longer training times (54 minutes vs 311 seconds). Quantum DPP sampling on real hardware showed promise for small problem sizes but was limited by current hardware noise. For credit risk assessment, quantum orthogonal and compound neural networks matched classical performance while using significantly fewer parameters (13 vs 64), with orthogonal networks showing more robust performance on quantum hardware (50.19% vs 40.20% Gini score). The results suggest that quantum-inspired classical algorithms can provide immediate benefits, while quantum hardware implementations remain constrained by current NISQ limitations.

**Performance claims:**
- 5.9% precision improvement in churn prediction (71.6% to 77.5%)
- 1.35% improvement in total withdrawals captured (61.42% to 62.77%)
- 1.54% improvement in maximum possible withdrawals captured (69.18% to 70.72%)
- Training time increase from 311 seconds to 54 minutes for DPP-RF models
- ROC-AUC improvement from 0.916 to 0.941 on madelon dataset
- Gini score of 54.29% for OrthoResNN vs 54.20% for classical ResNN with 13 vs 64 parameters
- Quantum hardware Gini score of 50.19% for OrthoResNN (vs 54.19% in simulation)
- Quantum hardware Gini score of 40.20% for ExpFNN (vs 53.90% in simulation)
## Quantum advantage claim
**Classification:** speculative

While the paper demonstrates quantum-inspired classical algorithms that improve performance, quantum advantage claims remain speculative. Quantum DPP sampling showed potential complexity advantages (O(d log(n)) vs O(d^3)) but was only demonstrated on small problem sizes due to hardware limitations. Quantum neural networks matched classical performance with fewer parameters, but this advantage was only shown through classical simulation. Hardware experiments showed significant performance degradation due to noise, particularly for compound networks. The authors suggest future quantum advantage may emerge with better hardware.
## Limitations
- Hardware noise significantly impacts performance, especially as problem dimensions grow (e.g., quantum DPP sampling falters for larger batch dimensions on IBM quantum processors)
- Experiments limited to small-scale datasets due to qubit count constraints (e.g., 16-qubit IBM hardware restricts DPP sampling to matrices of size (4,2), (5,2), etc.)
- Quantum DPP-RF algorithm performance degrades on real hardware compared to classical DPP sampling for larger datasets [inferred]
- Training time for DPP-RF models is significantly longer (54 minutes vs. 311 seconds for classical Random Forest) due to classical DPP sampling bottlenecks
- Quantum neural network (QNN) experiments rely on classical simulation, which does not fully capture hardware noise or scalability challenges [inferred]
- Error mitigation techniques (e.g., M3, dynamical decoupling) introduce classical/quantum overhead, limiting scalability for larger circuits [inferred]
- Orthogonal and compound layers reduce parameter count but may sacrifice expressivity compared to classical fully-connected layers [inferred]
- Hardware connectivity constraints (e.g., nearest-neighbor RBS gates) limit circuit design flexibility on superconducting qubit devices
- Subsampling of datasets (e.g., 300 test points for QNN hardware experiments) may not fully represent real-world performance [inferred]
- Lack of comparison with state-of-the-art classical machine learning models (e.g., gradient-boosted trees) for benchmarking [inferred]
- Reproducibility challenges due to hardware noise variability across quantum processors [inferred]
- Limited exploration of hybrid quantum-classical approaches to mitigate hardware limitations [inferred]
## Open questions
- How does the quantum DPP-RF algorithm perform on real quantum hardware for full-scale datasets (e.g., 174,000 datapoints) without subsampling?
- What is the impact of decoherence and gate errors on QNN performance for larger qubit counts (e.g., >20 qubits)?
- Can quantum orthogonal/compound layers outperform classical models in high-dimensional financial datasets (e.g., >100 features)?
- How do quantum machine learning models compare to classical baselines (e.g., XGBoost) in terms of precision-recall trade-offs for imbalanced datasets?
- What are the scalability limits of quantum DPP sampling for datasets with >1M datapoints?
- How do error mitigation techniques (e.g., M3, dynamical decoupling) scale with increasing circuit depth and qubit count?
- Can quantum neural networks achieve quantum advantage in financial forecasting without error correction?
- What is the minimum qubit count and gate fidelity required to outperform classical models in production settings?

**Future work:**
- Test quantum DPP-RF and QNN models on larger-scale quantum hardware (e.g., IBM Eagle, Osprey processors)
- Develop hybrid quantum-classical algorithms to mitigate hardware noise and improve scalability
- Benchmark quantum models against state-of-the-art classical methods (e.g., XGBoost, deep neural networks) on real-world financial datasets
- Explore advanced error mitigation techniques (e.g., zero-noise extrapolation, probabilistic error cancellation) for QNNs
- Extend quantum orthogonal/compound layers to multi-period financial forecasting (e.g., time-series prediction)
- Investigate quantum transfer learning for financial applications with limited labeled data
- Optimize quantum circuit compilation for financial datasets to reduce gate count and depth
- Develop quantum-inspired classical algorithms for GPU/TPU acceleration to bridge the gap until fault-tolerant quantum hardware is available
- Apply quantum machine learning to other financial use cases (e.g., fraud detection, algorithmic trading)
- Study the impact of quantum data loading techniques (e.g., RY, H-loading) on model performance for high-dimensional data
## Key ideas
- #idea:near-term-feasibility — Quantum-enhanced DPPs improve Random Forest precision by 5.9% (77.5% vs. 71.6%) for churn prediction, demonstrating tangible business impact (1.35-1.54% gains in withdrawal capture).
- #idea:hybrid-approach — Hybrid quantum-classical models (e.g., orthogonal neural networks) match or exceed classical performance with fewer parameters (13 vs. 64), suggesting efficiency gains for near-term deployments.
- #idea:near-term-feasibility — Quantum DPP sampling on IBM hardware (ibmq_guadalupe) matches classical performance for small-scale problems (≤6 qubits), validating NISQ-era applicability for constrained use cases.
- #idea:hybrid-approach — Quantum-inspired classical methods (e.g., orthogonal neural networks) outperform or match classical baselines on 6/8 public datasets, offering immediate deployable improvements.
## Contradictions
- #contradiction:classical-vs-quantum — The paper claims quantum DPP sampling has lower complexity (O(nd) gate count), but this is disputed by classical DPP advances achieving O(poly(d)) runtime for exact sampling [citation needed].
- #contradiction:scalability — The paper speculates quantum DPP may offer runtime advantages for large datasets, but empirical results show performance degradation beyond small dimensions (>6 qubits), contradicting scalability claims.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
