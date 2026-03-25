---
aliases:
- The Potential of Quantum Techniques for Stock Price Prediction
- Potential Quantum Techniques Stock
authors:
- Naman Srivastava
- Gaurang Belekar
- Neel Shahakar
- Aswath Babu H.
auto_detected: true
classification: ''
contradiction_flags:
- contradiction:classical-vs-quantum
- contradiction:scalability
doi: ''
evidence_type: ''
idea_tags:
- idea:near-term-feasibility
- idea:hybrid-approach
journal_or_venue: arXiv
methodology_tags:
- quantum-annealing
- QUBO
- quantum-ML
- quantum-SVM
- classical-simulation
paper_type: ''
quantum_advantage_claim: speculative
related_papers: []
relevance_phase1: medium
relevance_phase3: medium
source_type: preprint
source_type_confidence: high
step1_date: '2026-03-25T16:01:07.800504'
step1_model: gpt-5.1
step2_date: '2026-03-25T16:01:11.741318'
step2_model: gpt-5.1
step3_date: '2026-03-25T16:01:47.542826'
step3_model: gpt-5.4
step4_date: '2026-03-25T16:02:13.555850'
step4_model: gpt-5.4
step5_date: '2026-03-25T16:02:34.830109'
step5_model: gpt-5.4
step6_date: '2026-03-25T16:02:49.384097'
step6_model: gpt-5.4
steps_completed:
- 1
- 2
- 3
- 4
- 5
- 6
tags:
- topic/asset-pricing
- method/quantum-annealing
- method/QUBO
- method/quantum-ML
- method/quantum-SVM
- method/classical-simulation
- idea/near-term-feasibility
- idea/hybrid-approach
- contradiction/classical-vs-quantum
- contradiction/scalability
title: The Potential of Quantum Techniques for Stock Price Prediction
topic_tags:
- asset-pricing
year: 2023
zotero_key: ''
---

## Abstract summary
The paper investigates how various quantum computing methods can be used for stock price prediction, focusing on transforming the task into a binary classification of next-day price movements. The authors construct technical indicators from real stock data, apply quantum annealing and PCA for dimensionality reduction, and then compare quantum SVM classifiers against a range of classical machine learning models. The study evaluates performance across four major stocks and discusses where quantum approaches, particularly quantum annealing for feature selection, may offer benefits and where quantum SVMs currently show limited advantage over classical methods.
## Methodology
This preprint reports an empirical quantum-enhanced stock prediction study. The authors collect daily stock data for four companies (Apple, Visa, Johnson & Johnson, and Honeywell) from yfinance over 25 Dec 2020 to 25 Dec 2022, then engineer technical indicators including moving averages, RSI, MACD, stochastic oscillator, ATR, and Aroon. They convert next-day stock movement into a binary classification target indicating whether price at day T+1 exceeds price at day T. To address limited quantum resources, they apply two dimensionality-reduction approaches: classical PCA and quantum annealing-based feature selection formulated as a QUBO problem for execution on D-Wave annealers. Reduced datasets with 3, 5, and 8 features are created for each method (PCA3/5/8 and QA3/5/8). On these datasets, they train a Quantum Support Vector Classifier using Qiskit's quantum kernel approach with a ZZFeatureMap under four entanglement schemes (linear, circular, full, pairwise), and compare performance against multiple classical machine learning baselines including SVM, decision tree, random forest, KNN, logistic regression, naive Bayes, gradient boosting, and XGBoost. Evaluation is based primarily on accuracy and F-score, reported by company and dimensionality-reduction setting. The paper also notes computational limitations in simulating QSVC on 8-feature datasets.

**Algorithms used:** Quantum Annealing, QUBO, PCA, QSVM, QSVC, SVM, Decision Tree, Random Forest, KNN, Logistic Regression, Naive Bayes, Gradient Boosting, XGBoost
**Frameworks:** Qiskit, scikit-learn, yfinance, D-Wave

**Experimental setup:** Experiments were conducted using both classical and quantum hardware/simulation according to the abstract, though the implementation details are mixed. Quantum annealing-based feature selection is described as running QUBO formulations on D-Wave quantum annealing computers. QSVC is implemented via Qiskit using ZZFeatureMap quantum kernels, but the paper indicates that some QSVC runs failed due to insufficient computational power for simulating feature-map circuits, suggesting at least part of the QSVC evaluation was performed in simulation rather than on a gate-based QPU. Classical baselines were trained on reduced and unreduced datasets.

**Dataset:** Daily stock market data for four companies: Apple (AAPL), Visa (VISA), Johnson & Johnson (JNJ), and Honeywell (HON), obtained via the yfinance API. Raw fields include daily closing price, highest price, and lowest price, from 25 December 2020 to 25 December 2022. Additional technical indicators were computed from these raw prices.
## Experiment details
### Input
Input data consisted of daily stock prices for AAPL, VISA, JNJ, and HON from yfinance, covering 25 Dec 2020 to 25 Dec 2022. Raw variables included closing, high, and low prices for each day. From these, the authors derived technical indicators: moving averages (SMA/EMA implied), RSI, MACD, stochastic oscillator, ATR, and Aroon indicators. The prediction target was a binary label 'Change' defined as 1 if Price_T < Price_T+1 and 0 otherwise. Dimensionality reduction produced six reduced datasets per stock: PCA3, PCA5, PCA8 and QA3, QA5, QA8. No exact sample counts, train/test split, or normalization details are reported in the provided text.

### Process
1. Collect daily stock data for four firms using yfinance. 2. Compute technical indicators from historical prices, including MA, RSI, MACD, stochastic oscillator, ATR, and Aroon. 3. Define the binary classification label based on whether the next day's price is higher than the current day's price. 4. Apply PCA to generate reduced feature sets with 3, 5, and 8 components. 5. Apply quantum annealing-based feature selection by formulating feature selection as a QUBO, where binary variables indicate whether a feature is selected, and optimize this on D-Wave to produce 3-, 5-, and 8-feature subsets. 6. Train multiple classical classifiers on the original and reduced datasets. 7. Train QSVC models on reduced datasets using Qiskit's quantum kernel method with ZZFeatureMap. 8. For QSVC, evaluate four entanglement schemes: linear, circular, full, and pairwise. 9. Compare models using accuracy and F-score across companies and dimensionality-reduction settings. 10. Note that QSVC on 8-feature datasets could not be trained because of insufficient computational power for circuit simulation.

### Output
Outputs are classification performance results reported as accuracy (including average accuracy across settings) and F-score. Results are presented overall and separately for each company, with best-performing model, dimensionality-reduction method, and for QSVC the entanglement scheme. Baseline comparisons include unreduced classical ML, PCA-reduced classical ML, QA-selected classical ML, and QSVC on PCA/QA reduced datasets. The study concludes that quantum annealing feature selection often outperformed PCA for feature reduction, while QSVM did not show a significant advantage over classical SVM on these datasets.

### Parameters
- stocks: ['AAPL', 'VISA', 'JNJ', 'HON']
- time_period: 2020-12-25 to 2022-12-25
- reduced_feature_counts: [3, 5, 8]
- qsvc_feature_map: ZZFeatureMap
- qsvc_entanglement_schemes: ['linear', 'circular', 'full', 'pairwise']
- target_definition: 1 if Price_T < Price_T+1 else 0
- evaluation_metrics: ['accuracy', 'F-score']

### Hardware
Quantum annealing feature selection is described as executed on D-Wave quantum annealing computers. Gate-based quantum classification uses Qiskit QSVC with ZZFeatureMap, but the specific backend, simulator name, QPU model, cloud provider, number of shots, and transpilation settings are not reported. The paper explicitly mentions insufficient computational power for simulating QSVC models with 8 features.

### Reproducibility
Partial reproducibility. Data source (yfinance) and date range are provided, along with the feature-engineering and model-comparison logic. However, key implementation details are missing, including exact sample sizes after preprocessing, train/test split or cross-validation protocol, PCA settings, QUBO coefficients/objective construction details, D-Wave solver configuration, QSVC backend/simulator settings, and hyperparameters for both quantum and classical models. No code repository is mentioned in the provided text.
## Findings
- [supported] Across the evaluated stock datasets, classical machine learning with quantum-annealing-based feature selection on 5 features (QA-5) achieved the best average performance among the compared pipelines, with 60.26% average accuracy and 62.24% average F-score.
- [supported] QSVM did not show a significant performance advantage over classical SVM or other classical baselines on the binary stock-movement classification task in these experiments.
- [supported] Quantum-annealing-based feature selection outperformed PCA on average in the reported experiments, suggesting better feature subset quality for this task.
- [supported] QSVM models on 8-feature datasets could not be trained in the authors' setup because simulation of the quantum feature-map circuits required insufficiently available computational resources.
- [supported] The study used real stock data for Apple, Visa, Johnson & Johnson, and Honeywell from 25 Dec 2020 to 25 Dec 2022, but the quantum classification results were obtained via simulated quantum circuits rather than a demonstrated hardware quantum advantage.
- [speculative] The paper argues that quantum annealing can more efficiently explore large feature-combination spaces than classical methods for feature selection.
- [speculative] The paper suggests quantum computing may eventually improve financial analysis and stock prediction, but the present evidence does not demonstrate such an advantage.

**Results summary:** This preprint studies a quantum-enhanced pipeline for binary stock-price movement prediction using technical indicators, dimensionality reduction via PCA or quantum annealing feature selection, and classification with classical models and QSVM. Using data from four stocks, the authors report that quantum-annealing-based feature selection generally performed better than PCA in downstream prediction, with the best overall average results coming from classical models on QA-5 datasets (60.26% average accuracy, 62.24% average F-score). However, QSVM did not materially outperform classical SVM or the best classical baselines, and 8-feature QSVM experiments could not be completed due to computational limits in simulating quantum circuits. As a preprint, any broader claims about quantum advantage remain speculative; the empirical evidence here supports limited utility for feature selection but not a demonstrated quantum advantage in stock prediction.

**Performance claims:**
- Average classical ML with no dimensionality reduction: 56.58% accuracy, 58.76% F-score
- Average classical ML with PCA-3: 54.21% accuracy, 56.81% F-score
- Average classical ML with PCA-5: 55.00% accuracy, 58.83% F-score
- Average classical ML with PCA-8: 53.68% accuracy, 57.71% F-score
- Average classical ML with QA-3: 55.26% accuracy, 52.81% F-score
- Average classical ML with QA-5: 60.26% accuracy, 62.24% F-score
- Average classical ML with QA-8: 55.79% accuracy, 57.22% F-score
- Average QSVM with PCA-3: 53.94% accuracy, 58.08% F-score
- Average QSVM with PCA-5: 56.58% accuracy, 59.79% F-score
- Average QSVM with QA-3: 53.94% accuracy, 54.04% F-score
- Average QSVM with QA-5: 55.78% accuracy, 57.45% F-score
- Honeywell best classical result: KNN with QA-5 at 62.10% accuracy and 68.96% F-score
- Honeywell best QSVM result: Linear or Full on PCA-5 at 57.89% accuracy and 65.51% F-score
- Johnson & Johnson best classical result: XGBoost with QA-5 at 56.84% accuracy and 57.73% F-score
- Johnson & Johnson best QSVM result: Circular with QA-5 at 60.00% accuracy and 56.82% F-score
- Apple best classical result: SVM with QA-5 at 58.94% accuracy and 61.38% F-score
- Apple best QSVM result: Circular with QA-5 at 58.94% accuracy and 58.06% F-score
- Visa best classical result: Logistic Regression with no dimensionality reduction at 65.26% accuracy and 63.73% F-score
- Visa best QA-5 classical result: SVM at 63.15% accuracy and 61.53% F-score
- Visa best QSVM result: Circular or Full on PCA-3 at 56.84% accuracy and 61.68% F-score
## Quantum advantage claim
**Classification:** speculative

Although the paper discusses potential quantum benefits and reports that quantum-annealing-based feature selection can help relative to PCA, it does not demonstrate a clear quantum advantage in prediction performance. QSVM did not significantly outperform classical methods, results rely largely on simulation/limited hardware workflow, and this is a preprint, so advantage claims should be treated as speculative.
## Limitations
- Lack of peer review, as the work is presented as an arXiv preprint
- Current quantum hardware is described as highly sensitive and prone to noise-induced errors, which can limit result accuracy
- Limited availability of high-quality qubits constrained the dimensionality of data that could be processed
- QSVC models for datasets with 8 features failed to train due to insufficient computational power for simulating quantum feature-map circuits
- The quantum advantage was not evident for the binary classification task, as QSVM did not significantly outperform classical SVM on the studied datasets
- The study only considered four companies (Apple, Visa, Johnson & Johnson, Honeywell), limiting generalizability across the broader market
- The data covers only a two-year period from 25 December 2020 to 25 December 2022, which may not capture different market regimes
- The prediction task was simplified to binary up/down classification, which limits applicability to richer forecasting settings
- [inferred] Reported accuracies are generally modest, suggesting limited practical predictive value for trading or investment use
- [inferred] No evidence of testing on real quantum hardware for the QSVM pipeline; much of the quantum modeling appears dependent on simulation
- [inferred] No comparison against stronger time-series baselines such as LSTM/transformer-based models, despite discussing them in related work
- [inferred] The feature set is restricted mainly to technical indicators and raw prices, omitting potentially important information such as macroeconomic, fundamental, or news/sentiment data
- [inferred] No detailed discussion of train/test protocol, cross-validation, hyperparameter tuning fairness, or statistical significance testing, which limits reproducibility and internal validity
- [inferred] No transaction costs, execution constraints, or economic utility metrics were evaluated, so financial usefulness remains unclear
- [inferred] Scalability to larger asset universes, higher-frequency data, or production financial systems was not demonstrated
## Open questions
- Under what financial analysis scenarios, if any, can QSVM provide a clear advantage over classical SVM?
- How will quantum stock prediction methods perform as quantum hardware improves in qubit quality, count, and noise levels?
- Can quantum annealing-based feature selection consistently outperform PCA and classical feature selection methods across more datasets and market conditions?
- How do different quantum feature-map entanglement schemes affect QSVM performance across assets and feature sets?
- Will the observed results generalize beyond the four selected companies and beyond the studied 2020-2022 period?
- How well do these methods scale to larger feature spaces when simulation and hardware constraints are relaxed?
- [inferred] Are the small performance differences between quantum and classical methods statistically significant or due to sampling variation?
- [inferred] Would quantum methods show more benefit on multi-class, regression, or multi-horizon forecasting tasks rather than binary direction prediction?
- [inferred] How robust are the results to alternative labeling schemes, different train/test splits, and non-stationary market conditions?
- [inferred] Can any predictive gains translate into economically meaningful trading performance after costs and risk adjustment?

**Future work:**
- Further investigate other potential applications of QSVM in finance
- Continue research and development to better realize the full potential of quantum computing in financial analysis
- Use dimensionality reduction and feature selection strategies to better adapt quantum machine learning pipelines to hardware limitations
- Explore quantum techniques across additional sectors and datasets to identify domain-specific trends
- Pursue future investigations in quantum-enhanced financial analysis and decision-making
- [inferred] Validate the approach on larger and more diverse datasets, including more companies, longer time horizons, and different market regimes
- [inferred] Test the methods on actual quantum hardware with noise mitigation, rather than relying primarily on simulation
- [inferred] Compare against stronger classical baselines and modern deep learning time-series models
- [inferred] Extend beyond binary classification to regression, multi-step forecasting, and portfolio-level financial tasks
- [inferred] Improve reproducibility by reporting detailed experimental protocols, hyperparameters, and statistical testing
## Key ideas
- #idea:hybrid-approach — The strongest reported pipeline is hybrid: quantum-annealing-based QUBO feature selection followed by classical ML, rather than end-to-end quantum prediction.
- #idea:near-term-feasibility — The paper adapts the problem to NISQ constraints by reducing features to 3/5/8 dimensions and testing QSVC with small quantum kernels.
- #idea:near-term-feasibility — Quantum annealing is presented as a practical near-term tool for feature selection on real stock datasets, even though gate-based QSVC remains resource-constrained.
- #contradiction:classical-vs-quantum — QSVM does not significantly outperform classical SVM or other classical baselines on next-day stock direction classification.
- #contradiction:scalability — QSVC experiments could not be completed for 8-feature datasets because simulation of the quantum feature map exceeded available computational resources.
## Contradictions
- The paper discusses possible quantum benefits for stock prediction, but its own empirical results contradict strong quantum-superiority narratives: classical models, especially with QA-5 feature selection, outperform QSVM on average.
- The study suggests quantum methods may help explore feature spaces, yet the gate-based quantum classification pipeline does not scale even to 8-feature cases in the reported setup, contradicting broad claims of readiness for realistic financial ML workloads.
- Any implied quantum advantage is undermined by the fact that QSVM results were obtained largely via simulation rather than demonstrated gate-based hardware performance, while the best predictive results came from classical learners.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
