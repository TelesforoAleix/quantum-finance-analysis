---
aliases:
- 'HQNN-FSP: A Hybrid Classical-Quantum Neural Network for Regression-Based Financial
  Stock Market Prediction'
- HQNN FSP Hybrid Classical
authors:
- Prashant Kumar Choudhary
- Nouhaila Innan
- Muhammad Shafique
- Rajeev Singh
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
- idea:quantum-advantage
journal_or_venue: arXiv
methodology_tags:
- quantum-ML
- variational
- classical-simulation
paper_type: ''
quantum_advantage_claim: speculative
related_papers: []
relevance_phase1: medium
relevance_phase3: medium
source_type: preprint
source_type_confidence: high
step1_date: '2026-03-25T16:07:47.954315'
step1_model: gpt-5.1
step2_date: '2026-03-25T16:07:59.660755'
step2_model: gpt-5.1
step3_date: '2026-03-25T16:08:33.846150'
step3_model: gpt-5.4
step4_date: '2026-03-25T16:09:05.675027'
step4_model: gpt-5.4
step5_date: '2026-03-25T16:09:30.847692'
step5_model: gpt-5.4
step6_date: '2026-03-25T16:09:43.285654'
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
- method/quantum-ML
- method/variational
- method/classical-simulation
- idea/near-term-feasibility
- idea/hybrid-approach
- idea/quantum-advantage
- contradiction/classical-vs-quantum
- contradiction/scalability
title: 'HQNN-FSP: A Hybrid Classical-Quantum Neural Network for Regression-Based Financial
  Stock Market Prediction'
topic_tags:
- asset-pricing
year: 2025
zotero_key: ''
---

## Abstract summary
The paper proposes hybrid quantum-classical neural network architectures for stock market prediction, combining recurrent deep learning models with parameterized quantum circuits. It introduces a custom QNN regressor and two hybrid schemes: one where classical models first extract temporal features before quantum processing, and another where classical and quantum components are trained jointly end-to-end. Using historical stock data with technical indicators and cross-validation-based evaluation, the study compares standalone quantum, hybrid, and classical models, finding that hybrid approaches improve over pure quantum models but still lag behind state-of-the-art classical recurrent networks in accuracy and efficiency.
## Methodology
This preprint presents an empirical study of hybrid quantum-classical stock price forecasting. The authors build and compare three quantum-enhanced models: a standalone customized quantum neural network (CustomQNN), a sequential hybrid model (HybridQNN1) in which classical recurrent feature extraction precedes quantum regression, and a jointly optimized hybrid model (HybridQNN2) that fuses classical LSTM-derived and quantum features end-to-end. Historical stock price data are enriched with technical indicators including RSI, MACD, ADX, and moving averages, then split chronologically into train/test sets. Feature selection is performed using SelectKBest, sequences are created with a lookback window, and inputs are normalized using MinMaxScaler. The quantum component uses angle encoding with RY and RZ rotations and a custom parameterized ansatz with single-qubit rotations and entangling CNOT/CZ gates, motivated by a Hamiltonian formulation. Models are trained with the Adam optimizer using MSE loss, early stopping, and learning-rate scheduling. Evaluation uses both TimeSeriesSplit and k-fold cross-validation, with RMSE as the primary metric, supplemented by error-distribution analysis, training-time comparisons, qubit-count sensitivity analysis, and SHAP-based interpretability. The study is explicitly a preprint and not peer reviewed in the provided text.

**Algorithms used:** Quantum Neural Network (QNN), Parameterized Quantum Circuit (PQC), HybridQNN1, HybridQNN2, LSTM, RNN, BiLSTM, GRU, Adam
**Frameworks:** Qiskit, scikit-QULACS, QULACS, TensorFlow, scikit-learn, SHAP, Slurm, CUDA

**Experimental setup:** Experiments were run using the QULACS quantum simulator and an HPC environment. Classical and hybrid models were trained on the PARAM Shivay supercomputer at IIT (BHU) using GPU nodes. Validation used both TimeSeriesSplit and k-fold cross-validation. The study evaluated 3-, 4-, and 5-qubit configurations, corresponding to 3, 4, and 5 selected features in the classical comparison models.

**Dataset:** Historical stock price data from the Kaggle dataset 'Stock Market Data - Nifty 100 Stocks (5 min) data', using stock variables such as open, close, high, low, and date. The dataset was augmented with technical indicators including RSI, MACD, ADX, and moving averages (SMA5/SMA20).
## Experiment details
### Input
Input data consisted of historical stock prices with raw features open, close, high, low, and date from a Kaggle Nifty 100 5-minute stock dataset. Additional engineered features included RSI (14-day), MACD (12-day and 26-day EMAs with 9-day signal line), ADX (14-day), and moving averages such as SMA5 and SMA20. Missing values were handled and date-time conversion was applied. Feature selection used SelectKBest, with examples showing top features such as ['open', 'RSI', 'MACD', 'sma5', 'ADX']. Data were split chronologically into 80% training and 20% testing. Sequential samples were created with lookback = 2, producing input tensors of shape (samples, lookback, 5). Features were normalized with MinMaxScaler: [0,1] scaling for classical components and [-1,1] scaling indicated for quantum inputs in the pipeline figure.

### Process
1. Load stock CSV data with error handling. 2. Preprocess by computing technical indicators (RSI, MACD, ADX, SMA5/SMA20), handling missing values, and converting date-time fields. 3. Apply SelectKBest feature selection to retain the most informative predictors for the closing price target. 4. Split data in temporal order into 80% train and 20% test sets. 5. Create time-series sequences using a lookback window of 2. 6. Normalize features and target values using MinMaxScaler. 7. Train baseline classical models (RNN, LSTM, BiLSTM, GRU) and three quantum-enhanced models. For CustomQNN, encode classical features into qubits using angle encoding with RY(arcsin(f(x_i))) and RZ(arccos(g(x_i))) gates, then apply a custom variational ansatz with parameterized single-qubit rotations and entangling CNOT/CZ operations, followed by measurement-based regression. For HybridQNN1, first extract temporal features with a classical deep model/LSTM, then pass the transformed representation into a QNN regressor using the same encoding and variational circuit. For HybridQNN2, feed preprocessed data in parallel to an LSTM-based classical branch and a QNN branch, fuse their outputs, and jointly optimize the full model end-to-end. 8. Optimize all trainable parameters using Adam on MSE loss with backpropagation; the paper mentions GradientTape and gradient synchronization for the integrated hybrid model. 9. Use TimeSeriesSplit and k-fold cross-validation with n_splits = 5, early stopping with patience = 10, learning-rate scheduling, and up to 500 iterations. 10. Evaluate using RMSE, error histograms with Gaussian fits, violin plots, training-time analysis, qubit-count comparisons, and SHAP KernelExplainer for feature importance.

### Output
Primary outputs are RMSE values for CustomQNN, HybridQNN1, HybridQNN2, and classical baselines (LSTM, RNN, BiLSTM, GRU), along with training times in seconds. Additional outputs include prediction-vs-actual plots, residual/error histograms with Gaussian fits, violin plots of error distributions, qubit-count sensitivity tables, cross-validation comparisons between TimeSeriesSplit and k-fold, and SHAP feature-importance visualizations. Baseline comparisons show hybrid models outperform standalone QNNs but remain worse than classical recurrent models in RMSE.

### Parameters
- qubits: [3, 4, 5]
- circuit_depth: 10
- lookback_period: 2
- batch_size: 32
- max_iterations: 500
- optimizer: Adam
- loss_function: MSE
- early_stopping: True
- early_stopping_patience: 10
- validation_methods: ['TimeSeriesSplit', 'k-fold cross-validation']
- n_splits: 5
- train_test_split: 80% train / 20% test
- classical_hidden_units: 100
- classical_recurrent_layers: 5
- feature_selection_method: SelectKBest
- selected_feature_counts: [3, 4, 5]

### Hardware
Quantum experiments used the QULACS simulator, with frameworks including Qiskit and scikit-QULACS. Training was performed on the PARAM Shivay supercomputer at IIT (BHU) using GPU nodes with 2 x Intel Xeon Skylake 6148 CPUs (20 cores at 2.4 GHz each), 192 GB RAM, and 2 x NVIDIA Tesla V100 GPUs (5120 CUDA cores, 16 GB HBM2). Execution was parallelized with CUDA and scheduled using Slurm over a 100 Gbps InfiniBand EDR network. No real QPU or transpilation settings were reported.

### Reproducibility
Preprint empirical study. Data source is publicly identified (Kaggle Nifty 100 stock dataset), and many pipeline details are reported, including preprocessing, feature engineering, validation strategy, optimizer, qubit counts, and hardware. However, no public code repository or exact implementation details for all circuit parameters, optimizer settings, and model architectures are provided in the excerpt, so replication appears partially feasible but not fully straightforward.
## Findings
- [supported] The proposed hybrid quantum-classical models (HybridQNN1 and HybridQNN2) achieved lower RMSE than the standalone CustomQNN across all tested qubit settings on simulator-based experiments.
- [supported] HybridQNN2 achieved the best RMSE among the quantum-enhanced models, with average RMSE values of 0.02312, 0.01959, and 0.01920 for 3, 4, and 5 qubits respectively under TimeSeriesSplit.
- [supported] HybridQNN1 achieved average RMSE values of 0.02605, 0.02161, and 0.01740 for 3, 4, and 5 qubits respectively, outperforming CustomQNN but with higher training cost at 5 qubits.
- [supported] The standalone CustomQNN performed substantially worse than the hybrid variants, with average RMSE values of 0.07603, 0.05528, and 0.06120 for 3, 4, and 5 qubits respectively.
- [supported] Classical benchmark models outperformed all quantum and hybrid models in this study, with RMSE around 0.00649-0.00781 depending on architecture and feature count.
- [supported] All three quantum-related models showed reasonable overlap with actual prices during a relatively stable regime (Phase 1) but failed to track a sharp downward regime shift in Phase 2.
- [supported] Error distribution analysis indicated that HybridQNN1 and HybridQNN2 had narrower error distributions and lower variance than CustomQNN, suggesting more stable predictions.
- [supported] Increasing qubit count generally improved predictive accuracy for the hybrid models, but also increased training time, revealing a clear accuracy-computation trade-off.
- [supported] HybridQNN2 was more computationally efficient than HybridQNN1 across the tested settings, with notably lower training times while maintaining the best hybrid RMSE.
- [supported] The experiments were conducted on a quantum simulator (QULACS) and HPC infrastructure rather than real quantum hardware.
- [speculative] The custom ansatz and hybrid integration may improve feature representation through entanglement and higher-dimensional quantum feature spaces for financial forecasting.
- [speculative] The authors suggest hybrid quantum-classical models could become more competitive as quantum hardware, noise mitigation, and scalable architectures improve.
- [speculative] Claims that quantum-assisted learning offers practical benefits for financial forecasting remain preliminary because the reported gains are only relative to a standalone QNN, not to state-of-the-art classical models.

**Results summary:** This preprint proposes a standalone QNN regressor and two hybrid quantum-classical stock forecasting models, HybridQNN1 and HybridQNN2, evaluated on historical stock data with technical indicators using TimeSeriesSplit and k-fold cross-validation. In simulator-based experiments, both hybrid models consistently outperformed the standalone CustomQNN in RMSE and error stability, with HybridQNN2 delivering the best overall hybrid performance and lower training time than HybridQNN1. However, all quantum-enhanced models remained clearly worse than classical baselines such as LSTM, RNN, BiLSTM, and GRU. The models performed better in relatively stable market periods but failed to adapt to abrupt downward regime shifts. Overall, the paper supports that hybridization improves over a pure QNN in this setup, but it does not demonstrate quantum advantage over classical methods, and any broader advantage claims are speculative.

**Performance claims:**
- HybridQNN2 average RMSE: 0.02312 (3 qubits), 0.01959 (4 qubits), 0.01920 (5 qubits)
- HybridQNN1 average RMSE: 0.02605 (3 qubits), 0.02161 (4 qubits), 0.01740 (5 qubits)
- CustomQNN average RMSE: 0.07603 (3 qubits), 0.05528 (4 qubits), 0.06120 (5 qubits)
- HybridQNN2 training time: 69841.69 s (3 qubits), 92337.84 s (4 qubits), 118833.32 s (5 qubits)
- HybridQNN1 training time: 121020.84 s (3 qubits), 155336.05 s (4 qubits), 227781.18 s (5 qubits)
- CustomQNN training time: 120765.63 s (3 qubits), 155362.05 s (4 qubits), 139337.06 s (5 qubits)
- LSTM average RMSE: 0.00781 (3 features), 0.00670 (4 features), 0.00649 (5 features)
- RNN average RMSE: 0.00772 (3 features), 0.00671 (4 features), 0.00659 (5 features)
- BiLSTM average RMSE: 0.00775 (3 features), 0.00715 (4 features), 0.00669 (5 features)
- GRU average RMSE: 0.00781 (3 features), 0.00687 (4 features), 0.00669 (5 features)
- Data split: 80% training, 20% testing
- Validation setup: TimeSeriesSplit and k-fold cross-validation with n_splits=5
- Lookback period: 2, batch size: 32, max iterations: 500, qubits tested: 3/4/5
## Quantum advantage claim
**Classification:** speculative

As a preprint, advantage claims default to speculative. The paper shows simulator-based improvements of hybrid models over a standalone QNN, but classical baselines still outperform all quantum-enhanced models by a wide margin, and no real-hardware or strong empirical quantum advantage is demonstrated.
## Limitations
- The study is a preprint and has not undergone peer review.
- Experiments were conducted on a quantum simulator (QULACS) rather than real quantum hardware, limiting conclusions about practical deployment on actual devices.
- Performance is constrained by the current state of Noisy Intermediate-Scale Quantum (NISQ) devices.
- All models struggle with rapid market transitions and abrupt regime shifts; predictions failed to capture the sharp downward trend in Phase 2.
- Hybrid models, while better than standalone quantum models, still fall short of classical deep learning baselines such as LSTM and BiLSTM in RMSE.
- Quantum circuit execution is resource-intensive, with very long training times compared to classical models.
- Increasing qubit count improves accuracy but significantly increases computational cost, especially for HybridQNN1 at 5 qubits.
- The evaluation only considers small qubit configurations (3, 4, and 5 qubits), limiting evidence for scalability.
- The lookback period is fixed at 2, which may be insufficient to capture longer-term temporal dependencies in financial time series.
- The dataset appears limited to historical stock OHLC data plus a small set of technical indicators, which may not capture broader market drivers.
- The paper uses a single stock dataset/source (Wipro stock data from a Kaggle dataset in the methodology figure), limiting generalizability across assets and markets.
- [inferred] No direct experiments on noisy hardware were reported, so claims about noise resilience and practical feasibility remain unvalidated.
- [inferred] No comparison is provided against stronger non-recurrent or modern time-series baselines (e.g., transformers, gradient boosting, temporal convolutional models), so the benchmark set may be incomplete.
- [inferred] The use of k-fold cross-validation on time-series data risks information leakage, which may inflate some reported performance estimates.
- [inferred] The paper does not establish any quantum advantage; observed gains are only relative to the standalone QNN, not to state-of-the-art classical methods.
- [inferred] Reproducibility may be limited because the full implementation details, random seeds, and exact hyperparameter search space are not fully specified in the provided text.
- [inferred] The study focuses on RMSE and predictive error analysis, but does not evaluate downstream financial utility such as trading returns, transaction costs, or risk-adjusted performance.
- [inferred] The conceptual figures motivating quantum benefits are explicitly not outputs from actual quantum models, so some motivation is illustrative rather than empirically demonstrated.
## Open questions
- Can hybrid quantum-classical models become competitive with or surpass classical deep learning models for stock forecasting as quantum hardware improves?
- How well do these models scale to larger qubit counts, deeper circuits, and larger financial datasets?
- How would the proposed models perform on real quantum hardware under realistic noise and decoherence conditions?
- Can adaptive mechanisms improve responsiveness to abrupt market changes and regime shifts?
- Which quantum encoding schemes are most effective for financial time-series representation?
- How can circuit depth and qubit utilization be optimized to balance predictive accuracy and computational efficiency?
- To what extent can quantum error mitigation improve reliability and forecasting performance in financial applications?
- How well do the proposed methods generalize across different stocks, sectors, markets, and time periods?
- Do additional financial indicators or alternative data sources materially improve hybrid model performance?
- Is there any genuine quantum-enhanced representation benefit in this setting beyond what strong classical models can achieve?

**Future work:**
- Explore larger-scale quantum architectures, including noise-resilient quantum processors, to improve scalability and precision.
- Extend the model to larger datasets and incorporate additional financial indicators to improve adaptability and generalization.
- Test real-time applications on actual quantum hardware to assess practical feasibility in financial markets.
- Enhance adaptability through reinforcement learning to better handle market fluctuations.
- Optimize hybrid architectures to reduce circuit depth and improve qubit utilization.
- Explore alternative quantum encoding schemes to improve feature representation.
- Leverage quantum error mitigation techniques to address noise-related challenges and improve model reliability.
- Refine algorithms and training strategies to narrow the performance gap with classical deep learning approaches.
- [inferred] Evaluate the approach across multiple assets, markets, and regimes to establish robustness and external validity.
- [inferred] Compare against stronger state-of-the-art classical forecasting baselines and perform ablation studies to isolate the contribution of the quantum component.
- [inferred] Assess downstream financial usefulness using trading-oriented metrics such as Sharpe ratio, drawdown, and transaction-cost-aware returns.
## Key ideas
- #idea:hybrid-approach — Proposes two hybrid quantum-classical forecasting architectures: sequential LSTM-to-QNN and parallel fused LSTM+QNN for stock price regression.
- #idea:near-term-feasibility — Evaluates small NISQ-style parameterized quantum circuits with 3–5 qubits for financial time-series prediction.
- #idea:near-term-feasibility — Hybrid quantum models outperform the standalone QNN but remain clearly worse than classical LSTM/RNN/GRU/BiLSTM baselines in RMSE and efficiency.
- #idea:near-term-feasibility — All experiments are simulator-based using QULACS on HPC infrastructure, so conclusions do not establish practical real-hardware performance.
- #idea:quantum-advantage — Any quantum advantage claim is explicitly speculative and limited to improvement over a pure QNN rather than over strong classical methods.
- #idea:hybrid-approach — The parallel end-to-end hybrid design (HybridQNN2) is the best-performing quantum-enhanced variant and more efficient than the sequential hybrid.
- #idea:near-term-feasibility — Increasing qubit count modestly improves hybrid accuracy but sharply increases training cost, indicating poor current scalability.
- #idea:near-term-feasibility — Quantum-enhanced and classical models alike struggle with abrupt regime shifts, with hybrid/QNN models especially failing to track sharp downward moves.
## Contradictions
- This paper contradicts optimistic quantum-ML-for-finance claims by showing that hybrid and standalone quantum models do not outperform standard classical recurrent networks on stock forecasting; instead, classical baselines achieve substantially lower RMSE.
- The paper also contradicts implicit scalability optimism in some QML literature: moving from 3 to 5 qubits yields only modest accuracy gains but very large increases in simulated training time, with evidence limited to tiny problem sizes.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
