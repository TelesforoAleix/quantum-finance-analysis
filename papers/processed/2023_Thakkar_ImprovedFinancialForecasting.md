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
doi: ''
evidence_type: ''
idea_tags:
- idea:quantum-advantage
- idea:near-term-feasibility
- idea:hybrid-approach
journal_or_venue: arXiv
methodology_tags:
- quantum-ML
- variational
- classical-simulation
paper_type: ''
quantum_advantage_claim: speculative
related_papers: []
relevance_phase1: high
relevance_phase3: high
source_type: preprint
source_type_confidence: high
step1_date: '2026-03-25T16:01:52.618789'
step1_model: gpt-5.1
step2_date: '2026-03-25T16:01:57.704345'
step2_model: gpt-5.1
step3_date: '2026-03-25T16:03:15.353938'
step3_model: gpt-5.4
step4_date: '2026-03-25T16:03:54.058874'
step4_model: gpt-5.4
step5_date: '2026-03-25T16:04:24.656719'
step5_model: gpt-5.4
step6_date: '2026-03-25T16:04:41.675766'
step6_model: gpt-5.4
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
- method/classical-simulation
- idea/quantum-advantage
- idea/near-term-feasibility
- idea/hybrid-approach
- contradiction/classical-vs-quantum
- contradiction/scalability
title: Improved Financial Forecasting via Quantum Machine Learning
topic_tags:
- fraud-detection
- credit-scoring
- risk-modelling
year: 2024
zotero_key: ''
---

## Abstract summary
The paper investigates how quantum-inspired and quantum machine learning methods can improve forecasting tasks in financial services, using real use cases from Itaú Unibanco. For churn prediction, the authors augment Random Forests with determinantal point process (DPP) sampling, including a quantum DPP variant, to increase diversity in training subsets and show higher precision and better capture of withdrawal amounts than a production Random Forest model. For credit risk assessment, they design quantum neural network architectures based on orthogonal and compound layers that can be efficiently simulated classically, demonstrating comparable or slightly better performance than classical fully connected networks while using substantially fewer trainable parameters, and they also explore running these models on current quantum hardware with error mitigation.
## Methodology
This preprint reports two empirical studies in financial services using quantum-inspired and quantum machine learning methods. First, for churn prediction, the authors propose a Determinantal Point Process-enhanced Random Forest (DPP-RF) that replaces uniform row/feature subsampling with DPP-based diverse sampling. Because full-dataset DPP sampling is expensive, they use a batched procedure: split the training set into batches, sample rows from each batch via d-DPP, sample features via DPP, train a first group of trees on these patches, aggregate sampled rows, resample features, train a second group of trees, and ensemble both groups. They evaluate on a proprietary bank churn dataset and additional OpenML tabular datasets, comparing against a production Random Forest baseline using precision at low recall, training time, withdrawals captured, and ROC-AUC. They also run a reduced-scale quantum hardware experiment for DPP sampling using IBM hardware on PCA-reduced small batches, comparing uniform sampling, quantum DPP simulation, and quantum DPP hardware via F1 score. Second, for credit risk prediction, they design neural networks with quantum orthogonal and compound layers inspired by parameterized quantum circuits built from RBS gates. These models are classically trained and simulated on a proprietary SME credit-default dataset and OpenML benchmarks, and compared against classical residual/feed-forward neural networks using Gini and ROC-AUC. Finally, they perform quantum hardware inference for classically trained models on IBM hardware, assessing degradation from noise and improvements from transpilation optimization, dynamical decoupling, and measurement error mitigation. As a preprint, the work is not peer reviewed.

**Algorithms used:** Determinantal Point Process, d-DPP sampling, Random Forest, DPP-Random Forest, PCA, Decision Tree, Quantum DPP sampling, Variational Quantum Classifier, Quantum orthogonal neural network, Compound neural network, Expectation-per-subspace compound layer, Bayesian ridge regression imputation
**Frameworks:** DPPy, JAX, ray-tune, scikit-learn, Qiskit, Qiskit Runtime, OpenML

**Experimental setup:** The study combines classical ML experiments, classical simulation of quantum-inspired neural layers, and quantum hardware runs. Classical churn experiments were run on a machine with Intel Core i5-8350U CPU at 1.70 GHz, 24 GB RAM, Windows 10 21H2. Classical DPP sampling used an SVD-based algorithm from DPPy. Quantum DPP hardware experiments used reduced train/test subsets, PCA to 2 or 3 dimensions, small batch sizes of 4, 5, 6, or 8, and IBM's 16-qubit ibmq_guadalupe processor with adjacent-qubit-compatible diagonal and semi-diagonal Clifford loaders. Credit-risk neural networks were trained classically in JAX for 500 epochs with hyperparameter tuning via ray-tune. Quantum inference experiments for trained orthogonal/compound models used IBM's 27-qubit ibm_hanoi backend and Qiskit Runtime Sampler with optimization and error mitigation/suppression.

**Dataset:** Two proprietary Itaú Unibanco datasets plus public OpenML benchmarks. Churn dataset: 304,000 anonymized and standardized customer-month observations with 153 features, target indicating whether the customer churned in at least one of the next three months. Credit-risk dataset: about 141,500 anonymized and standardized SME credit observations with 32 features (31 numerical, 1 categorical), target indicating default behavior. Additional public classification datasets from OpenML include madelon, credit-default, house-pricing, jannis, eye movements, bank-marketing, wine, and california.
## Findings
- [supported] A DPP-enhanced Random Forest (DPP-RF) improved churn-prediction precision at 6% recall from 71.6% to 77.5%, an increase of 5.9 percentage points on the bank dataset.
- [supported] On the churn use case, DPP-RF increased the average share of total withdrawals captured among the top 500 flagged customers from 61.42% to 62.77%, a gain of 1.35 percentage points over 11 test months.
- [supported] On the same churn task, DPP-RF increased the average share of maximum possible withdrawals captured from 69.18% to 70.72%, a gain of 1.54 percentage points.
- [supported] The classical DPP-RF model trained much more slowly than the benchmark Random Forest, taking 54 minutes versus 311 seconds, with DPP sampling identified as the computational bottleneck.
- [supported] On several OpenML tabular classification benchmarks, DPP-RF sometimes modestly outperformed standard Random Forest in ROC-AUC, but gains were dataset-dependent and not universal.
- [supported] Quantum DPP sampling executed on IBM hardware produced classifier performance similar to simulator-based DPP sampling only for small matrix sizes up to about (6,2), while performance degraded for larger dimensions due to hardware noise.
- [speculative] The paper claims quantum DPP sampling could reduce sampling complexity relative to classical methods and eventually accelerate DPP-RF training, but this was not demonstrated at application scale.
- [supported] For SME credit-risk prediction, the orthogonal quantum-inspired neural network (OrthoResNN) matched or slightly exceeded the classical residual network's test Gini while using far fewer trainable parameters: 54.29% Gini with 13 parameters versus 54.20% with 64 parameters.
- [supported] The expectation-per-subspace compound model (ExpResNN) achieved similar but slightly worse credit-risk performance than the classical baseline, with 53.95% test Gini using 13 parameters.
- [supported] Across several OpenML datasets, orthogonal neural networks (OrthoFNN) often matched or modestly exceeded classical FNN ROC-AUC with fewer parameters, though results were mixed across datasets.
- [supported] On IBM quantum hardware, inference for the classically trained OrthoResNN on a 300-point subsample achieved Gini 50.19%, versus 54.19% in noiseless simulation; with optimization and error mitigation this improved to 53.68%, narrowing the gap to 0.53 percentage points.
- [supported] Hardware inference for the more complex compound model was substantially more noise-sensitive: ExpFNN achieved Gini 40.20% on hardware versus 53.90% in noiseless simulation.
- [speculative] The authors argue that quantum-inspired classical ML methods are useful today and that better future quantum hardware could make these methods faster and potentially more effective, but this future benefit is not empirically established in the paper.

**Results summary:** This preprint studies two financial ML use cases at Itaú Unibanco: churn prediction and SME credit-risk assessment. For churn, a classical DPP-enhanced Random Forest improved precision at low recall and modestly improved business-oriented withdrawal-capture metrics relative to a production Random Forest, but at substantially higher training cost. Small-scale quantum DPP sampling experiments on IBM hardware reproduced simulator behavior only for very small instances and deteriorated as circuit size increased because of noise. For credit risk, quantum-inspired orthogonal and compound neural-network layers were classically simulated; the orthogonal model matched or slightly exceeded the classical residual baseline while using many fewer trainable parameters, whereas the compound model was similar but slightly worse. Hardware inference for the orthogonal model was reasonably close to noiseless simulation after error mitigation, while the compound model remained strongly noise-limited. Overall, the paper presents empirical evidence for useful quantum-inspired modeling ideas today, but any claim of quantum computational advantage remains speculative because the strongest gains come from classical implementations and hardware results are limited to small noisy experiments.

**Performance claims:**
- Churn precision at 6% recall improved from 71.6% to 77.5% (+5.9 percentage points)
- Average total withdrawals captured improved from 61.42% to 62.77% (+1.35 percentage points) over 11 test months
- Average maximum possible withdrawals captured improved from 69.18% to 70.72% (+1.54 percentage points)
- Training time increased from 311 seconds to 54 minutes for DPP-RF versus benchmark RF
- OpenML ROC-AUC: madelon 0.916 to 0.941, jannis 0.866 to 0.870, eye movements 0.704 to 0.710, wine 0.901 to 0.906, california 0.962 to 0.963; no gain on credit-default 0.856 to 0.856 and bank-marketing 0.881 to 0.881; worse on house-pricing 0.948 to 0.939
- Credit-risk test Gini: ResNN 54.20% with 64 trainable parameters
- Credit-risk test Gini: OrthoResNN 54.29% with 13 trainable parameters
- Credit-risk test Gini: ExpResNN 53.95% with 13 trainable parameters
- OpenML ROC-AUC for OrthoFNN vs FNN: madelon 0.636 vs 0.624, house-pricing 0.781 vs 0.780, jannis 0.797 vs 0.791, bank-marketing 0.850 vs 0.847, wine 0.640 vs 0.553, california 0.668 vs 0.634; worse on credit-default 0.634 vs 0.647 and eye movements 0.578 vs 0.580
- Quantum hardware OrthoResNN inference Gini: 50.19% on hardware vs 54.19% noiseless simulation on a 300-point subsample
- Error-mitigated OrthoResNN hardware inference Gini improved to 53.68%, only 0.53 percentage points below ideal noiseless execution
- Quantum hardware ExpFNN inference Gini: 40.20% on hardware vs 53.90% noiseless simulation
- Claimed quantum DPP sampling complexity: gate complexity O(nd) and circuit depth O(d log n) for orthogonal matrices, versus cited classical sampling time O(d^3) after preprocessing
## Quantum advantage claim
**Classification:** speculative

Although the paper reports empirical gains from quantum-inspired classical methods and small hardware demonstrations, it does not show end-to-end quantum advantage on a practical financial task. Hardware experiments are limited to reduced problem sizes and are noise-constrained, while complexity-based speedup claims for quantum DPP sampling and compound-layer inference remain theoretical or prospective.
## Limitations
- Quantum DPP experiments were performed only on a scaled-down version of the churn dataset; the full dataset was not feasible for quantum sampling experiments.
- The IBM quantum processor gave similar results only for small batch dimensions and faltered as dimensions grew due to hardware noise.
- Current open-source DPP sampling implementations are too slow to sample from the full churn dataset efficiently, forcing the use of a novel batched approximation procedure instead of full-dataset DPP sampling.
- The DPP-RF model has substantially longer training time than the benchmark Random Forest (54 minutes vs 311 seconds), limiting practicality.
- Hyperparameter search for DPP-RF was constrained by runtime, with batch size restricted to less than 1000 because larger values dramatically increased runtime.
- Quantum hardware experiments for DPP-RF were limited to very small matrix sizes such as (4,2), (5,2), (5,3), (6,2), and (8,2) due to qubit and connectivity constraints.
- To fit hardware constraints in the quantum DPP experiment, the authors reduced the feature dimension from 153 to 2 or 3 using PCA, which may omit important information.
- The hardware-ready quantum DPP procedure was simplified to training one decision tree on aggregated sampled patches rather than the full proposed Random Forest-style pipeline.
- For the hardware DPP experiment, evaluation used F1 score on simplified single-tree models rather than the main business metrics used in the full churn study, limiting comparability.
- For credit risk, compound layers increase classical simulation complexity exponentially, making larger-scale classical experiments difficult.
- Inference on quantum hardware for credit-risk models was tested only on a small subsample of 300 test points because of job-size limitations on the IBM machine.
- The more complex ExpFNN/compound model performed poorly on hardware because it uses the full 2^n-dimensional Hilbert space and lacks the natural error-rejection available to the orthogonal model.
- Error mitigation and suppression techniques introduce classical/quantum pre- and post-processing overhead, and some do not scale efficiently to larger circuits.
- The paper explicitly states that present-day quantum hardware is not powerful enough to provide real improvements or conclusive large-scale benchmarks.
- The primary datasets and some models are proprietary and not publicly available, limiting reproducibility.
- The paper is a preprint and has not undergone peer review.
- [inferred] There is no comparison against stronger state-of-the-art classical tabular models beyond Random Forests and relatively simple neural baselines, so the claimed advantage may be overstated.
- [inferred] The churn and credit-risk results are based on data from a single bank, which may limit external validity and generalization to other financial institutions or markets.
- [inferred] The practical business impact is only partially validated, since withdrawals captured depend on downstream intervention success and profit-per-dollar-AUM, which were not modeled.
- [inferred] The use of anonymized proprietary real-world data prevents independent replication and detailed auditing of preprocessing choices.
- [inferred] The quantum advantage claims remain indirect because most strong results come from quantum-inspired classical implementations or classical simulation rather than end-to-end quantum execution at realistic scale.
- [inferred] The simplified hardware experiments may not faithfully represent performance of the full proposed methods in production settings.
## Open questions
- Can quantum DPP sampling provide practical speed or quality advantages on full-scale financial datasets once hardware improves?
- How well does the DPP-RF approach scale to larger batch sizes and full-dataset sampling with improved classical or quantum samplers?
- What is the performance of quantum DPP-based methods on larger matrix dimensions beyond the small cases tested on current hardware?
- How robust are the observed churn-prediction gains across other banks, customer populations, and time periods?
- Can compound neural network layers outperform orthogonal layers or classical layers when larger Hilbert spaces become accessible on better hardware?
- Which quantum circuit ansatz choices are best for financial machine learning tasks, given the paper's note that there is little consensus on good architectures?
- To what extent can error mitigation close the gap between noisy and ideal quantum inference for more complex models such as compound layers?
- Will the lower parameter count of orthogonal/compound layers translate into better generalization consistently across broader financial datasets and tasks?
- How much of the observed improvement comes from diversity-aware sampling or orthogonality itself versus other implementation and preprocessing choices?
- Can the methods deliver end-to-end production benefits once inference/training costs, latency, and operational constraints are considered?

**Future work:**
- Use improved classical DPP sampling techniques to reduce runtime and expand the feasible hyperparameter range, especially batch size.
- Leverage future quantum techniques and better quantum hardware to accelerate DPP sampling and improve performance on larger problems.
- Test larger compound layers that explore much larger portions of the Hilbert space as hardware improves.
- Perform larger-scale and more conclusive quantum benchmarks when quantum hardware becomes more powerful.
- Apply the proposed methods to other finance use cases and domains beyond churn prediction and credit risk assessment.
- Further investigate error mitigation and suppression techniques to improve NISQ hardware inference performance.
- [inferred] Validate the methods on additional real-world financial datasets from multiple institutions to assess generalizability.
- [inferred] Compare against stronger modern classical baselines for tabular learning, such as gradient-boosted trees and advanced deep tabular models.
- [inferred] Evaluate full end-to-end business impact, including intervention effectiveness and economic outcomes, rather than only predictive metrics.
- [inferred] Study scalability of the full quantum-enhanced pipelines under realistic production constraints, including latency, retraining frequency, and hardware access.
## Key ideas
- #idea:near-term-feasibility — Quantum-inspired DPP-enhanced Random Forest improved bank churn prediction precision and withdrawal-capture metrics on a real industrial dataset, showing immediate practical value without requiring full quantum advantage.
- #idea:hybrid-approach — The strongest results come from hybrid/quantum-inspired workflows: classical training and simulation of quantum-inspired models, plus limited quantum hardware inference or sampling experiments.
- #idea:near-term-feasibility — Orthogonal quantum-inspired neural networks matched or slightly exceeded classical credit-risk baselines while using far fewer trainable parameters, suggesting parameter-efficient models for tabular finance tasks.
- #idea:quantum-advantage — The paper advances speculative complexity-based claims that quantum DPP sampling and future quantum inference could eventually accelerate financial ML pipelines.
- #idea:near-term-feasibility — Error mitigation substantially narrowed the gap between noisy hardware and noiseless simulation for the orthogonal credit model, indicating some NISQ-era viability for constrained inference tasks.
- #idea:hybrid-approach — The paper positions quantum-inspired classical ML as useful today, with future quantum hardware potentially serving as an accelerator rather than replacing classical pipelines outright.
## Contradictions
- The paper suggests prospective quantum speedups for DPP sampling, but its own empirical results show that the practical gains in churn prediction come from classical DPP-based methods, not from quantum hardware; this supports #contradiction:classical-vs-quantum.
- The paper discusses future quantum acceleration, yet the hardware DPP experiments only work comparably to simulation on very small instances and degrade beyond about (6,2) because of noise, contradicting any near-term scaling claim (#contradiction:scalability).
- The paper frames quantum methods as promising for financial ML, but most reported credit-risk gains are obtained via classically simulated quantum-inspired architectures rather than end-to-end quantum execution, weakening any direct superiority claim over classical methods (#contradiction:classical-vs-quantum).
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->

## Experiment details
### Input
Churn prediction input: proprietary bank dataset with 304,000 datapoints and 153 features per datapoint; each datapoint is a customer at a month, features summarize previous 6 months, target is churn in following 3 months. Data anonymized and standardized; split by time into 174,000 training and 130,000 test points with no significant covariate shift. Quantum DPP hardware subset used about 1,000 training points from 03/2019 and about 10,000 test points from 04/2019; PCA reduced 153 columns to d=2 or d=3, then batches of n=4,5,6,8 points were formed. Credit-risk input: about 141,500 SME observations with 32 features (31 numerical, 1 categorical), anonymized and standardized; split by time into about 74,700 training observations over 12 months and about 66,800 test observations over the subsequent 8 months. Missing values were imputed, with best results from scikit-learn IterativeImputer using Bayesian ridge regression. For hardware inference, a 300-point test subsample was selected from the credit-risk test set. OpenML benchmark datasets were preprocessed as in prior work for tree models; for NN benchmarks, datasets were used for binary classification with train/validation/test splits.

### Process
Churn DPP-RF pipeline: (1) divide training set uniformly into smaller batches; (2) sample rows S1 from each batch using d-DPP on X_batch X_batch^T; (3) sample features S2 using d-DPP on X_S1^T X_S1; (4) train first group G1 of N1 decision trees on sampled patches; (5) aggregate sampled patches into X_agg; (6) repeat N2 times feature sampling S3 from X_agg^T X_agg to create larger datasets; (7) train second group G2 of N2 trees; (8) aggregate G1 and G2 predictions. Hyperparameters were selected by grid search with 5-fold cross-validation over n_estimators, max_depth, min_samples_leaf, min_samples_split, max_features, max_samples, and DPP batch_size, with batch_size constrained below 1000. Evaluation emphasized precision at fixed low recall (6%), training time, and business withdrawal capture metrics. OpenML tree benchmarks used train/validation/test splits and 400 random hyperparameter configurations, selecting best validation model and reporting test ROC-AUC. Quantum DPP hardware experiment: apply PCA to d=2 or 3, divide into batches of n=4,5,6,8, sample rows from each batch using quantum DPP circuits, aggregate sampled patches, train one decision tree, repeat for multiple trees, and compute F1 for each tree; compare uniform sampling, quantum simulator, and quantum processor. Adjacent-only diagonal and semi-diagonal Clifford loaders were used; outputs with incorrect Hamming weight were discarded as error mitigation. Credit-risk NN pipeline: build 3-layer models with 32x8 linear encoder plus tanh, 8x8 experimental layer, and 8x2 classification head plus softmax. ResNN used a classical residual linear layer; OrthoResNN used an orthogonal layer with semi-diagonal loader and X circuit plus skip connection and tanh; ExpResNN used an expectation-per-subspace compound layer with H-loader and X circuit plus tanh. Models were trained in JAX for 500 epochs; hyperparameters searched over learning rate, learning-rate-halving points, and batch size using ray-tune. Public NN benchmarks used a 16-dimensional encoding layer with GeLU, a 16x16 experiment layer with tanh, and binary classification head; OrthoFNN used a pyramid circuit and FNN used a linear layer; both trained for 500 epochs with batch size 128 and learning rate 1e-4. Quantum hardware inference: classically train OrthoResNN and ExpFNN/ExpResNN variant, construct circuits with learned parameters, run inference on ibm_hanoi for a 300-point subsample, compute Gini from ROC. For OrthoResNN, unary-basis postselection rejected invalid outputs. Additional mitigation used correlated readout mitigation, then Qiskit Runtime Sampler with optimization level 3, dynamical decoupling, and M3 measurement mitigation.

### Output
For churn, outputs include precision-recall curves, precision at 6% recall, training time, amount of withdrawals captured among top 500 flagged customers, percentage of total withdrawals captured, percentage of maximum possible withdrawals captured, and ROC-AUC on OpenML benchmarks. Reported proprietary churn results compare benchmark RF vs DPP-RF: precision 71.6% vs 77.5%, total withdrawals captured 61.42% vs 62.77%, maximum possible withdrawals captured 69.18% vs 70.72%, and training time 311 s vs 54 min. Quantum DPP hardware outputs are F1-score distributions for decision trees under uniform sampling, simulator-based quantum DPP, and hardware quantum DPP. For credit risk, outputs include test Gini on proprietary SME data and ROC-AUC on OpenML datasets, with parameter-count comparisons: ResNN 64 params and 54.20% Gini, OrthoResNN 13 params and 54.29% Gini, ExpResNN 13 params and 53.95% Gini. Hardware inference outputs are ROC curves and Gini scores: OrthoResNN noiseless simulator about 54.19%, hardware 50.19%, mitigated hardware 53.68%; ExpFNN noiseless simulator 53.90%, hardware 40.20%. Baselines are production/classical Random Forests, uniform sampling, classical residual/feed-forward neural networks, and noiseless simulator results.

### Parameters
- churn_dataset_size: 304000
- churn_train_size: 174000
- churn_test_size: 130000
- churn_features: 153
- fixed_recall_for_precision: 0.06
- flagged_customers_per_month: 500
- classical_training_time_benchmark_seconds: 311
- classical_training_time_dpp_rf_minutes: 54
- classical_cpu: Intel Core i5-8350U 1.70 GHz
- classical_ram_gb: 24
- dpp_rf_batch_size_constraint: <1000
- cv_folds: 5
- openml_hyperparameter_trials_tree_models: 400
- quantum_dpp_pca_dimensions: [2, 3]
- quantum_dpp_batch_sizes: [4, 5, 6, 8]
- quantum_dpp_train_subset_size: 1000
- quantum_dpp_test_subset_size: 10000
- credit_dataset_size: 141500
- credit_train_size: 74700
- credit_test_size: 66800
- credit_features: 32
- credit_encoder_layer: 32x8 + tanh
- credit_experimental_layer_size: 8x8
- credit_classification_head: 8x2 + softmax
- training_epochs: 500
- nn_benchmark_batch_size: 128
- nn_benchmark_learning_rate: 0.0001
- orthonn_trainable_parameters: 13
- resnn_trainable_parameters: 64
- orthofnn_trainable_parameters: 120
- fnn_trainable_parameters: 256
- hardware_inference_test_subsample: 300
- qiskit_runtime_optimization_level: 3
- sampler_resilience_level: 1

### Hardware
Classical churn training ran on Intel Core i5-8350U CPU, 24 GB RAM, Windows 10 21H2. Quantum DPP sampling experiments used IBM Quantum ibmq_guadalupe, a 16-qubit processor, limited to small matrix dimensions such as (4,2), (5,2), (5,3), (6,2), (8,2). Because the backend supports only adjacent-qubit RBS interactions, the authors used diagonal and semi-diagonal Clifford loader architectures instead of the ideal loader. Invalid-measurement postselection based on expected Hamming weight was applied. Quantum neural-network inference used IBM Quantum ibm_hanoi, a 27-qubit machine. Qiskit Runtime Sampler was used with transpilation optimization level 3, including layout/routing heuristics, 1-qubit gate optimization, commutative cancellation, and 2-qubit KAK optimization. Error suppression used dynamical decoupling; error mitigation used correlated readout mitigation in one experiment and M3 measurement mitigation via Sampler resilience level 1 in later runs.

### Reproducibility
Partial reproducibility. The paper provides substantial methodological detail, algorithm outlines, model architectures, preprocessing descriptions, metrics, and hardware/backend names. Public benchmark datasets are available via OpenML, and standard libraries/frameworks are named. However, the main proprietary Itaú/QC Ware datasets and production model are not publicly available, and no code repository is provided in the text. Replication of benchmark experiments is plausible; full replication of proprietary-data results is not possible from the paper alone.
