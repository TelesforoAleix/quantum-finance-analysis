---
aliases:
- Comparative analysis of loan risk forecasting using quantum machine learning and
  classical machine learning models
- Comparative analysis loan risk
authors:
- Adamu Mohammed Mustapha
- Peter Nimbe
- Abdul Razak Nuhu
auto_detected: true
classification: ''
contradiction_flags:
- contradiction:classical-vs-quantum
- contradiction:scalability
doi: 10.21203/rs.3.rs-7907390/v1
evidence_type: ''
idea_tags:
- idea:quantum-advantage
journal_or_venue: Research Square
methodology_tags:
- quantum-ML
- quantum-SVM
- classical-simulation
paper_type: ''
quantum_advantage_claim: speculative
related_papers: []
relevance_phase1: high
relevance_phase3: medium
source_type: preprint
source_type_confidence: high
step1_date: '2026-03-25T16:11:12.031087'
step1_model: gpt-5.1
step2_date: '2026-03-25T16:11:15.626421'
step2_model: gpt-5.1
step3_date: '2026-03-25T16:11:48.686486'
step3_model: gpt-5.4
step4_date: '2026-03-25T16:12:14.313872'
step4_model: gpt-5.4
step5_date: '2026-03-25T16:12:47.250241'
step5_model: gpt-5.4
step6_date: '2026-03-25T16:12:57.233452'
step6_model: gpt-5.4
steps_completed:
- 1
- 2
- 3
- 4
- 5
- 6
tags:
- topic/credit-scoring
- topic/risk-modelling
- method/quantum-ML
- method/quantum-SVM
- method/classical-simulation
- idea/quantum-advantage
- contradiction/classical-vs-quantum
- contradiction/scalability
title: Comparative analysis of loan risk forecasting using quantum machine learning
  and classical machine learning models
topic_tags:
- credit-scoring
- risk-modelling
year: 2025
zotero_key: ''
---

## Abstract summary
The paper compares classical Support Vector Machines (SVM) with Quantum Support Vector Machines (QSVM) for forecasting loan default risk using a Kaggle credit risk dataset with 12,638 records and 12 features. The authors implement both models with appropriate preprocessing, hyperparameter choices, and evaluation metrics, then analyze learning curves, confusion matrices, and ROC curves. They find that QSVM slightly outperforms SVM in terms of true positive/negative rates and AUC, suggesting quantum-enhanced models may offer advantages for loan risk prediction, especially as dataset size grows.
## Methodology
This preprint reports an empirical comparative study of classical and quantum machine learning for loan risk forecasting, explicitly comparing a classical Support Vector Machine (SVM) with a Quantum Support Vector Machine / Quantum Support Vector Classifier (QSVM/QSVC). The authors used a Kaggle credit-risk dataset and performed preprocessing in a Jupyter environment: missing numerical values were imputed with column means, categorical missing values with the mode, categorical variables were transformed using label encoding, and features were normalized with Min-Max scaling to the [0,1] range. The dataset was split into 80% training and 20% testing. For the classical baseline, an SVM with an RBF kernel was trained. For the quantum model, the study used a 12-qubit setup corresponding to 12 features, a ZFeatureMap with two repetitions to encode classical data into quantum states, a quantum kernel, and a QSVC classifier with regularization parameter C=10. The quantum experiments were run on Qiskit's statevector simulator rather than real quantum hardware, providing a noise-free simulated environment. Model performance was assessed using confusion-matrix-derived measures and classification metrics including accuracy, precision, recall, F1-score, ROC curve, and AUC, along with learning-curve analysis and cross-validation behavior. The paper is a preprint and should be treated as non-peer-reviewed.

**Algorithms used:** SVM, QSVM, QSVC
**Frameworks:** Qiskit, Jupyter

**Experimental setup:** The study was conducted in a Jupyter notebook environment using a Kaggle credit-risk dataset. Two models were implemented: a classical SVM with RBF kernel and a quantum SVM/QSVC using a quantum kernel derived from a ZFeatureMap. Data were split into 80% training and 20% testing. The quantum model used 12 qubits and was executed on Qiskit's statevector_simulator, i.e., a classical simulation of quantum circuits in a noise-free environment.

**Dataset:** Kaggle credit risk dataset (https://www.kaggle.com/datasets/laotse/credit-risk-dataset), reported as approximately 12,638 records and 12 columns/features, containing demographic and financial loan-application variables and a binary default/non-default target.
## Experiment details
### Input
Kaggle credit risk dataset with about 12,638 rows and 12 columns/features. Variables include age, income, home-related/categorical borrower attributes, loan intent, grade, employment length, loan interest rate, loan amount, loan percentage of income, loan history length, and binary loan status/default label. Numerical missing values were imputed using mean imputation; categorical missing values were imputed using mode. Categorical variables were label-encoded. Features were normalized using Min-Max scaling to the [0,1] range. Data were split into 80% training and 20% testing, yielding a reported test support of 2,528 samples.

### Process
1. Load the Kaggle loan-risk dataset into a Jupyter environment. 2. Inspect the data for inconsistencies and missing values. 3. Impute missing numerical values with column means and missing categorical values with the most frequent category. 4. Encode categorical variables using label encoding. 5. Normalize features using Min-Max scaling. 6. Split the dataset into 80% training and 20% testing. 7. Train a classical SVM using an RBF kernel. 8. Configure the quantum model with 12 qubits, a ZFeatureMap with 2 repetitions, a quantum kernel, regularization parameter C=10, and Qiskit's statevector_simulator backend. 9. Train the QSVC classifier on the processed training data. 10. Evaluate both models on the test set using confusion matrices, classification reports, ROC/AUC, and learning-curve/cross-validation analysis.

### Output
Outputs include confusion matrices, classification reports, learning curves, ROC curves, and AUC values for both SVM and QSVM. Reported SVM results include accuracy of 0.90 and AUC of 0.898, with class-wise precision/recall/F1 shown for both classes. Reported QSVM results include accuracy of 0.90 and AUC of 1.0, with slightly improved recall/true positive and true negative rates relative to SVM. The baseline comparison is direct: classical SVM versus quantum QSVM/QSVC on the same processed dataset.

### Parameters
- train_test_split: 80/20
- svm_kernel: RBF
- qubits: 12
- qsvc_regularization_C: 10
- feature_map: ZFeatureMap
- feature_map_repetitions: 2
- quantum_backend: statevector_simulator

### Hardware
Quantum experiments were not run on a real QPU. They used Qiskit's statevector_simulator backend, a classical simulator providing a noise-free quantum execution environment. No cloud QPU provider, device model, shot count, transpilation settings, or noise model details were reported.

### Reproducibility
Partial reproducibility. The data source is public and explicitly linked via Kaggle, and the paper describes the main preprocessing steps, train/test split, kernel choices, qubit count, feature map, simulator, and regularization parameter. However, no code repository is provided, and several implementation details are missing or ambiguous (e.g., exact feature list after encoding, random seed, cross-validation protocol, optimizer/configuration details for learning curves, and some dataset size inconsistencies), so full replication would require inference.
## Findings
- [supported] On a Kaggle loan-risk dataset with 12,638 records and 12 features, QSVM slightly outperformed classical SVM on the reported test metrics for loan default classification.
- [supported] The classical SVM achieved 0.90 accuracy on 2,528 test samples, with class-0 precision/recall/F1 of 0.88/0.92/0.90 and class-1 precision/recall/F1 of 0.92/0.87/0.89.
- [supported] The QSVM achieved 0.90 accuracy on 2,528 test samples, with class-0 precision/recall/F1 of 0.88/0.93/0.91 and class-1 precision/recall/F1 of 0.93/0.88/0.90.
- [supported] The paper reports that QSVM had a higher true positive rate for defaults (93.2%) than SVM (92.5%) and a higher true negative rate for non-defaults (87.6%), indicating marginally better classification performance.
- [supported] The SVM ROC AUC was reported as 0.898, while the QSVM ROC AUC was reported as 1.0.
- [supported] The QSVM implementation used 12 qubits, a ZFeatureMap with 2 repetitions, regularization parameter C=10, and a Qiskit statevector_simulator backend.
- [supported] The quantum results were obtained on a noise-free classical simulator rather than real quantum hardware.
- [speculative] The authors claim QSVM can continue improving with larger datasets and may be scalable for larger loan-risk forecasting tasks, but this was not directly validated beyond the reported dataset.
- [speculative] The paper argues that QSVM may better capture nonlinear structure in financial data than classical SVM, but this mechanism is inferred rather than rigorously established in the experiments.
- [speculative] The paper suggests quantum-enhanced models could transform financial risk management and loan approval processes, but no real-world deployment or hardware-based evidence is provided.
- [speculative] The paper presents QSVM as demonstrating the viability of quantum algorithms for real-world financial problems, but the evidence is limited to simulator-based benchmarking against a single classical baseline.

**Results summary:** This preprint compares a classical SVM and a QSVM for loan risk forecasting using a Kaggle dataset of 12,638 records and 12 features, with an 80/20 train-test split. Both models achieved 0.90 reported accuracy on the 2,528-sample test set, but QSVM showed slightly better class-wise precision, recall, and F1 scores, along with a reported true positive rate of 93.2% and true negative rate of 87.6%. The paper also reports ROC AUC values of 0.898 for SVM and 1.0 for QSVM. However, the QSVM was run using Qiskit's statevector_simulator in a noise-free simulated environment, so the reported quantum gains are based on simulation rather than real quantum hardware. As a preprint, its broader claims about scalability and quantum advantage in financial services should be treated as speculative.

**Performance claims:**
- Dataset size: 12,638 records, 12 features
- Train/test split: 80%/20%
- Test set size: 2,528 samples
- SVM accuracy: 0.90
- SVM class 0 precision/recall/F1: 0.88/0.92/0.90
- SVM class 1 precision/recall/F1: 0.92/0.87/0.89
- SVM ROC AUC: 0.898
- SVM confusion matrix counts described as 1,176 correctly classified defaults, 96 defaults misclassified as non-default, and 1,095 correctly predicted non-defaults
- QSVM accuracy: 0.90
- QSVM class 0 precision/recall/F1: 0.88/0.93/0.91
- QSVM class 1 precision/recall/F1: 0.93/0.88/0.90
- QSVM true positive rate: 93.2%
- QSVM true negative rate: 87.6%
- QSVM ROC AUC: 1.0
- QSVM confusion matrix counts described as 1,186 correctly predicted defaults out of 1,272 actual defaults
- QSVM false positive rate reported as 6.8%
- QSVM misclassified 156 safe loans as risky
- QSVM used 12 qubits, ZFeatureMap with 2 repetitions, and C=10
## Quantum advantage claim
**Classification:** speculative

The paper claims QSVM outperforms SVM, but evidence comes from a preprint using a noise-free statevector simulator rather than real quantum hardware. The reported gains are modest except for the AUC=1.0 claim, and no robust demonstration of practical quantum advantage over classical methods is established.
## Limitations
- The study uses a Kaggle dataset with 12,638 records and 12 features, which may limit generalizability to broader real-world banking portfolios and more complex credit environments.
- The QSVM was evaluated using Qiskit's statevector_simulator rather than real quantum hardware, so results do not reflect hardware noise, decoherence, gate errors, or limited connectivity.
- The quantum setup required 12 qubits for 12 features, implying growing computational demand as feature dimensionality increases.
- The QSVM learning curve discussion notes initial overfitting on smaller datasets before generalization improves with more data.
- The data required preprocessing for missing values, imbalance, and categorical encoding, meaning results may depend on specific preprocessing choices such as mean/mode imputation and label encoding.
- [inferred] The paper is a preprint and has not undergone peer review, so claims and methodology have not yet been independently validated.
- [inferred] The reported QSVM AUC of 1.0 on a noisy real-world credit task is unusually strong and raises concerns about possible overfitting, leakage, or evaluation issues.
- [inferred] No comparison is made against stronger classical baselines such as gradient boosting, XGBoost, random forests, neural networks, or calibrated credit-scoring models, limiting the strength of the claimed quantum advantage.
- [inferred] The study compares only SVM and QSVM, so conclusions about quantum machine learning superiority are narrow and model-specific.
- [inferred] Because the quantum model was simulated classically, the work does not demonstrate practical quantum speedup or runtime advantage.
- [inferred] The paper claims QSVM scalability and improvement with larger datasets, but no experiments on substantially larger datasets or complexity analysis are provided.
- [inferred] The use of label encoding for categorical variables may impose artificial ordinal relationships that could distort both SVM and QSVM performance.
- [inferred] The paper does not clearly report class distribution, resampling strategy, or cost-sensitive treatment despite describing the data as imbalanced.
- [inferred] The evaluation appears based on a single 80/20 split with limited detail on repeated cross-validation or robustness checks, which may reduce reliability.
- [inferred] There is limited discussion of reproducibility details such as exact hyperparameter search procedure, software versions, random seed handling across all steps, and full code availability.
- [inferred] The dataset includes implausible values such as age up to 144 years and employment length up to 123 years, suggesting possible data quality issues that may affect validity.
- [inferred] The study does not address explainability, fairness, or regulatory suitability, which are critical for financial-services deployment.
- [inferred] No external validation on data from actual banks or different geographies is provided, limiting confidence in production applicability.
## Open questions
- How would QSVM perform on real quantum hardware under realistic noise conditions?
- Does QSVM maintain its performance advantage over SVM and other classical models on larger, more diverse, and institution-specific loan datasets?
- Is the apparent perfect separability implied by the QSVM AUC of 1.0 reproducible across different train/test splits and external datasets?
- How sensitive are the results to preprocessing choices such as imputation, normalization, and categorical encoding?
- What happens to QSVM performance and resource requirements as the number of features and borrowers increases substantially?
- Can QSVM handle severely imbalanced credit datasets better than advanced classical imbalance-handling methods?
- Would other quantum models such as QNN, VQC, or Qk-NN outperform QSVM for loan risk forecasting?
- What is the trade-off between predictive performance and interpretability when using QSVM in regulated lending contexts?
- Can any practical computational advantage be demonstrated once training time and kernel evaluation costs are measured against classical alternatives?
- How robust is QSVM to noisy, missing, drifting, or adversarial financial data over time?

**Future work:**
- Use larger and more complex financial datasets to improve robustness and generalization.
- Explore additional quantum models such as QSVM, QNN, Qk-NN, and VQC for loan risk forecasting.
- Investigate quantum and advanced non-linear models for handling imbalanced loan datasets more effectively.
- Evaluate whether QSVM can better capture complex non-linear relationships in borrower behavior and financial data.
- [inferred] Validate the approach on real quantum hardware and assess the impact of noise and limited qubit resources.
- [inferred] Benchmark QSVM against stronger classical baselines including ensemble and deep learning methods.
- [inferred] Perform external validation using proprietary or real bank datasets from multiple institutions and regions.
- [inferred] Use more rigorous evaluation protocols such as repeated cross-validation, temporal splits, and out-of-sample testing.
- [inferred] Investigate explainability, fairness, and compliance implications of deploying QSVM in lending decisions.
- [inferred] Study scalability in terms of qubit count, circuit depth, runtime, and memory as dataset size and feature count grow.
- [inferred] Test alternative encoding schemes and missing-data treatments to determine how preprocessing affects QSVM outcomes.
- [inferred] Examine hybrid quantum-classical approaches and noise-mitigation techniques for practical financial applications.
## Key ideas
- #idea:quantum-advantage — QSVM is reported to slightly outperform a classical RBF-SVM on loan default prediction, with marginally better class-wise metrics and a reported AUC of 1.0 versus 0.898.
- #idea:quantum-advantage — The paper frames quantum kernel methods as potentially better at capturing nonlinear structure in credit-risk data.
- #idea:quantum-advantage — Authors suggest QSVM performance may improve further as dataset size grows, though this is not empirically validated.
## Contradictions
- The paper suggests quantum superiority in credit-risk classification, but its own evidence is limited to a noise-free statevector simulator and a single classical baseline, undermining any strong practical quantum-advantage claim.
- The paper implies scalability to larger loan-risk problems, yet the 1-feature-per-qubit setup, simulator-based evaluation, and lack of complexity/runtime analysis contradict claims of near-term scaling to realistic financial datasets.
- The reported QSVM AUC of 1.0 on a real-world-style credit dataset appears inconsistent with the otherwise only marginal accuracy gains over classical SVM, raising possible concerns about overfitting, leakage, or evaluation instability.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
