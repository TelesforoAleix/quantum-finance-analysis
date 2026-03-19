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
contradiction_flags: []
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
source_type: preprint
source_type_confidence: high
step1_date: '2026-03-18T22:58:33.958216'
step1_model: Mistral-Large-3
step2_date: '2026-03-18T22:58:37.653536'
step2_model: Mistral-Large-3
step3_date: '2026-03-18T22:59:12.774495'
step3_model: Mistral-Large-3
step4_date: '2026-03-18T22:59:19.309596'
step4_model: Mistral-Large-3
step5_date: '2026-03-18T22:59:32.074460'
step5_model: Mistral-Large-3
step6_date: '2026-03-18T22:59:36.919912'
step6_model: Mistral-Large-3
steps_completed:
- 1
- 2
- 3
- 4
- 5
- 6
tags:
- topic/fraud-detection
- topic/credit-scoring
- topic/risk-modelling
- method/quantum-ML
- method/variational
- method/quantum-SVM
- idea/near-term-feasibility
- idea/hybrid-approach
title: Improved Financial Forecasting via Quantum Machine Learning
topic_tags:
- fraud-detection
- credit-scoring
- risk-modelling
year: 2024
zotero_key: ''
---

## Abstract summary
This preprint explores the application of quantum machine learning techniques to enhance financial forecasting, focusing on two key use cases at Itaú Unibanco: churn prediction and credit risk assessment. The authors introduce quantum-enhanced methods, such as Determinantal Point Processes (DPPs) for Random Forest models and quantum neural networks with orthogonal layers, to improve model performance and efficiency. The work demonstrates how quantum-inspired approaches can yield better results than classical methods, even with current hardware limitations, while laying groundwork for future advancements in quantum computing for finance.
## Methodology
The paper presents two primary use cases for quantum machine learning in financial services: churn prediction and credit risk assessment. For churn prediction, the authors extend the Random Forest algorithm by incorporating Determinantal Point Processes (DPPs) for subsampling rows and columns, aiming to preserve dataset diversity and reduce sampling bias. The DPP-Random Forest (DPP-RF) model is evaluated using classical DPP sampling algorithms and quantum DPP circuits on a scaled-down dataset. The quantum DPP sampling is implemented using Clifford loader circuits on IBM's quantum processor ('ibmq guadalupe'). For credit risk assessment, the authors design quantum neural network architectures with orthogonal and compound layers, leveraging variational quantum classifiers (VQC). These networks use unary, RY, and Hadamard data loaders combined with parameterized quantum circuits composed of RBS gates to enforce orthogonality and reduce parameter redundancy. The models are trained and tested on real-world financial datasets from Itaú Unibanco, with performance evaluated using precision-recall metrics, ROC-AUC, F1 score, and business KPIs such as withdrawals captured.

**Algorithms used:** Determinantal Point Processes (DPP), Random Forest, Quantum DPP Sampling, Variational Quantum Classifier (VQC), Orthogonal Neural Networks, Compound Neural Networks
**Frameworks:** DPPy, Qiskit

**Experimental setup:** For the churn prediction use case, classical DPP sampling was performed using the DPPy library on a classical computer (Intel Core i5-8350U CPU, 24 GB RAM). Quantum DPP sampling experiments were conducted on IBM's 'ibmq guadalupe' 16-qubit quantum processor and its simulator, with matrix dimensions limited to (4,2), (5,2), (5,3), (6,2), and (8,2) due to hardware constraints. Error mitigation involved disregarding results without the expected Hamming weight. For the credit risk assessment use case, quantum neural networks were classically simulated using orthogonal and compound layers with unary, RY, and Hadamard data loaders. Experiments were run on classical hardware for scalability and interpretability.

**Dataset:** The primary dataset for churn prediction consists of 304,000 data points with 153 features each, representing Itaú Unibanco customers over time, with a binary target indicating churn within three months. The dataset was split into training (174,000 points) and test (130,000 points) sets based on time periods. For quantum hardware experiments, reduced datasets of ~1,000 training points and ~10,000 test points were used. For credit risk assessment, a real-world dataset from Itaú Unibanco was used, though specific details are not provided. Additional benchmarking was performed on public classification datasets from OpenML (e.g., madelon, credit-default, house-pricing).
## Findings
- [supported] Quantum-enhanced Determinantal Point Processes (DPP) improved precision by 5.9% (from 71.6% to 77.5%) in churn prediction compared to classical Random Forest models on a real-world banking dataset
- [supported] DPP-Random Forest (DPP-RF) captured 1.35% more total withdrawals and 1.54% more maximum possible withdrawals than the benchmark model, demonstrating business impact
- [supported] Quantum neural networks with orthogonal and compound layers matched classical performance in credit risk assessment while using significantly fewer parameters
- [supported] Classical DPP-RF training time was 54 minutes versus 311 seconds for the benchmark model, with DPP sampling identified as the computational bottleneck
- [supported] Quantum DPP sampling on IBM hardware (ibmq guadalupe) produced results comparable to classical DPP for small matrix dimensions (up to 6x2), but performance degraded for larger dimensions due to hardware noise
- [speculative] Quantum DPP sampling could achieve O(nd) gate complexity and O(d log(n)) circuit depth, offering potential speedup over classical O(d3) sampling for large datasets
- [speculative] Quantum orthogonal and compound neural networks may offer advantages for financial data as quantum hardware improves, though current results are from classical simulation
- [speculative] Improved classical and quantum DPP sampling techniques could dramatically reduce runtime for large-scale financial datasets

**Results summary:** The paper demonstrates two quantum machine learning applications in financial services. For churn prediction, the DPP-RF model achieved a 5.9% precision improvement over classical Random Forest, with measurable business impact in withdrawal capture. For credit risk assessment, quantum neural networks matched classical performance while reducing model parameters. Quantum DPP sampling was tested on real hardware for small datasets, showing promise but limited by current NISQ device capabilities. All quantum advantage claims remain speculative as they rely on future hardware improvements or are demonstrated only through classical simulation.

**Performance claims:**
- 5.9% precision improvement (71.6% → 77.5%) in churn prediction
- 1.35% increase in total withdrawals captured (61.42% → 62.77%)
- 1.54% increase in maximum possible withdrawals captured (69.18% → 70.72%)
- 54 minutes training time for DPP-RF vs 311 seconds for benchmark
- Quantum DPP sampling comparable to classical for matrix dimensions up to 6x2
- Quantum neural networks achieved similar accuracy with fewer parameters than classical fully-connected networks
## Quantum advantage claim
**Classification:** speculative

While quantum DPP sampling shows theoretical complexity advantages (O(nd) gate complexity vs O(d3) classical), all empirical results are either from classical simulation or limited hardware experiments. The paper demonstrates quantum-inspired classical improvements but no clear quantum advantage on current hardware. Future advantage claims depend on improved quantum devices.
## Limitations
- Experiments on quantum DPP sampling were limited to small matrix dimensions (e.g., (4,2), (5,2), (6,2)) due to hardware constraints of the IBM quantum processor (ibmq guadalupe)
- Quantum DPP sampling performance degrades as matrix dimensions grow due to hardware noise and error rates on current NISQ devices
- The quantum DPP-RF algorithm was tested on a scaled-down version of the churn dataset (∼1000 points) rather than the full dataset (174,000 points), limiting practical applicability [inferred]
- No noise mitigation techniques were applied in quantum DPP sampling experiments, which may affect results on real hardware [inferred]
- The preprint lacks peer review, which may affect the validity and robustness of the findings [inferred]
- Classical DPP sampling remains a computational bottleneck, with training times significantly longer (54 minutes) than traditional Random Forest (311 seconds)
- Quantum neural network experiments were conducted using classical simulators, not real quantum hardware, limiting empirical validation of quantum advantage [inferred]
- The quantum DPP circuit architectures (diagonal and semi-diagonal Clifford loaders) were constrained by IBM's adjacent-qubit connectivity, potentially limiting performance [inferred]
- No comparison with state-of-the-art classical machine learning models (e.g., gradient-boosted trees) was provided to contextualize the quantum methods' performance [inferred]
- The credit risk assessment models were evaluated on a single real-world dataset, limiting generalizability to other financial datasets [inferred]
- The quantum neural network architectures rely on orthogonal and compound layers, which may not be optimal for all types of financial data [inferred]
## Open questions
- How does the quantum DPP-RF algorithm perform on the full churn dataset (174,000 points) compared to the scaled-down version?
- What is the impact of decoherence and gate errors on the quantum DPP sampling performance for larger matrix dimensions?
- Can noise mitigation techniques (e.g., error correction, dynamical decoupling) improve the quantum DPP sampling results on NISQ devices?
- How do quantum neural networks for credit risk assessment compare to classical deep learning models (e.g., transformers) in terms of accuracy and scalability?
- What is the minimum qubit count and coherence time required to achieve a practical quantum advantage for financial forecasting tasks?
- How does the quantum DPP-RF algorithm perform on datasets with higher feature dimensions (e.g., >153 features)?
- What are the trade-offs between quantum circuit depth and sampling accuracy for DPP-based methods?
- Can quantum compound neural networks be extended to multi-class classification problems in finance (e.g., fraud detection)?

**Future work:**
- Test the quantum DPP-RF algorithm on larger datasets and real quantum hardware with higher qubit counts
- Apply noise mitigation techniques to improve quantum DPP sampling performance on NISQ devices
- Extend quantum neural network architectures to other financial use cases (e.g., fraud detection, algorithmic trading)
- Compare quantum machine learning models with state-of-the-art classical models (e.g., XGBoost, deep neural networks) on benchmark datasets
- Develop hybrid quantum-classical algorithms to leverage the strengths of both paradigms for financial forecasting
- Explore alternative quantum circuit ansätze for orthogonal and compound layers to improve scalability and performance
- Investigate the use of quantum DPP sampling for other machine learning tasks (e.g., feature selection, data augmentation)
- Assess the financial impact of quantum-enhanced models in production environments (e.g., cost savings, risk reduction)
- Optimize classical DPP sampling algorithms to reduce training time for large-scale datasets
- Develop quantum algorithms for multi-period portfolio optimization and dynamic risk assessment
## Key ideas
- #idea:near-term-feasibility — Quantum-enhanced DPPs and quantum neural networks show improved performance over classical methods in churn prediction and credit risk assessment, even with current NISQ-era hardware limitations
- #idea:hybrid-approach — Hybrid quantum-classical approaches (e.g., DPP-RF, variational quantum classifiers) are proposed as practical paths for near-term financial applications
- #idea:near-term-feasibility — Quantum DPP sampling on IBM hardware (ibmq guadalupe) produces results comparable to classical DPP for small datasets, demonstrating potential for real-world use cases
- #idea:hybrid-approach — Quantum neural networks with orthogonal layers match classical performance while reducing model parameters, suggesting efficiency gains in hybrid setups
- #limitation:noise — Quantum DPP sampling performance degrades for larger matrix dimensions due to hardware noise, highlighting current NISQ limitations
- #limitation:qubit-count — Experiments are limited to small datasets and matrix dimensions (e.g., 6x2) due to insufficient qubits on current quantum processors
## Contradictions
<!-- Step 6 output — where this paper contradicts others -->

## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
