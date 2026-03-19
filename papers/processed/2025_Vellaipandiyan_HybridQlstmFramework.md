---
aliases:
- Hybrid QLSTM Framework for Time Series Forecasting in Dynamic Financial Markets
- Hybrid QLSTM Framework Time
authors:
- Solaimurugan Vellaipandiyan
- Shib Kumar Saraf
- Abishek DG
- S Prayla Shyry
- Priya Gopal
- Akash Antony J
auto_detected: true
classification: ''
contradiction_flags:
- contradiction:classical-vs-quantum
- contradiction:scalability
doi: 10.1109/ICIMIA67127.2025.11200988
evidence_type: ''
idea_tags:
- idea:near-term-feasibility
- idea:hybrid-approach
- idea:quantum-advantage
journal_or_venue: Proceedings of the 4th International Conference on Innovative Mechanisms
  for Industry Applications (ICIMIA-2025)
methodology_tags:
- quantum-ML
- variational
paper_type: ''
quantum_advantage_claim: speculative
related_papers: []
relevance_phase1: high
relevance_phase3: medium
source_type: conference-paper
source_type_confidence: high
step1_date: '2026-03-18T22:19:48.849049'
step1_model: Mistral-Large-3
step2_date: '2026-03-18T22:19:52.687702'
step2_model: Mistral-Large-3
step3_date: '2026-03-18T22:20:00.671929'
step3_model: Mistral-Large-3
step4_date: '2026-03-18T22:20:08.172330'
step4_model: Mistral-Large-3
step5_date: '2026-03-18T22:21:18.358847'
step5_model: Mistral-Large-3
step6_date: '2026-03-18T22:21:22.713776'
step6_model: Mistral-Large-3
steps_completed:
- 1
- 2
- 3
- 4
- 5
- 6
tags:
- topic/asset-pricing
- topic/high-frequency-trading
- method/quantum-ML
- method/variational
- idea/near-term-feasibility
- idea/hybrid-approach
- idea/quantum-advantage
- contradiction/classical-vs-quantum
- contradiction/scalability
title: Hybrid QLSTM Framework for Time Series Forecasting in Dynamic Financial Markets
topic_tags:
- asset-pricing
- high-frequency-trading
year: 2025
zotero_key: ''
---

## Abstract summary
This paper introduces a hybrid quantum-classical framework combining Long Short-Term Memory (LSTM) networks with Quantum Neural Networks (QNNs) to improve time series forecasting in financial markets. The study evaluates multiple quantum feature maps and circuit designs to optimize the QLSTM model, aiming to leverage quantum computing's parallel processing capabilities for better pattern recognition in dynamic and noisy financial data. The proposed approach seeks to enhance prediction accuracy while reducing reliance on large datasets compared to classical methods.
## Methodology
The paper presents a hybrid quantum-classical framework for financial time series forecasting, specifically stock price prediction. The methodology involves combining a classical Long Short-Term Memory (LSTM) network with a Quantum Neural Network (QNN) to leverage both temporal pattern recognition and quantum computing advantages. The process begins with data acquisition from Yahoo Finance for Apple Inc. stock (AAPL ticker) spanning June 2019 to May 2025, followed by exploratory data analysis to identify trends and patterns. Data preprocessing includes normalization, handling missing values, and creating sliding windows of 20 days for input sequences. The hybrid model architecture consists of a classical LSTM layer to capture temporal dependencies, a dense layer to reduce dimensionality, and a QNN layer using quantum circuits with feature maps and ansatz designs. Multiple quantum circuit configurations (e.g., ZZFeatureMap, PauliFeatureMap, RealAmplitudes) were evaluated to determine the optimal design. The model was trained using RMSprop optimizer with Mean Squared Error (MSE) loss and early stopping to prevent overfitting. Performance was evaluated using metrics such as MSE, MAE, RMSE, R², and Explained Variance, with comparisons made between the hybrid QLSTM and classical LSTM models.

**Algorithms used:** QLSTM (Quantum Long Short-Term Memory), LSTM (Long Short-Term Memory), QNN (Quantum Neural Network)
**Frameworks:** Qiskit (implied by use of ZZFeatureMap and RealAmplitudes)

**Experimental setup:** The experiments were conducted using a quantum simulator (no real QPU mentioned). The hybrid QLSTM model utilized 4 qubits for the quantum circuit, with a hidden size of 16 for the LSTM layer. Training was performed for 100 epochs using RMSprop optimizer with a learning rate of 0.01. The quantum circuit configurations tested included combinations of ZZFeatureMap, PauliFeatureMap, ZFeatureMap with RealAmplitudes and EfficientSU2 ansatz circuits. The dataset was split into 48% training, 32% validation, and 20% testing sets chronologically.

**Dataset:** Historical stock data for Apple Inc. (AAPL ticker) obtained via the yfinance Python library, covering the period from June 3, 2019, to May 30, 2025. The dataset includes 1,508 daily observations with features such as opening price, high price, low price, closing price, adjusted closing price, and trading volume. The closing price was used as the target variable for prediction.
## Findings
- [supported] The hybrid QLSTM framework combining classical LSTM with a Quantum Neural Network (QNN) achieved superior performance in stock price prediction, with an R² score of 0.83, MSE of 85.16, MAE of 7.49, and RMSE of 9.23 on AAPL stock data
- [supported] The QLSTM model demonstrated faster and smoother convergence during training compared to classical LSTM, with training and validation losses approaching near-zero values within fewer epochs
- [supported] The optimal quantum circuit configuration for QLSTM was identified as ZZFeatureMap combined with RealAmplitudes ansatz, achieving the lowest error metrics (MSE 0.0018) and highest R² (0.8372) among tested quantum circuit designs
- [supported] QLSTM required fewer trainable parameters and less training data to outperform classical LSTM, which achieved an R² of 0.54, MSE of 235.74, MAE of 13.53, and RMSE of 15.35
- [supported] The hybrid model effectively captured complex nonlinear trends and rapid price fluctuations in stock data, where classical LSTM failed to generalize and exhibited overfitting
- [speculative] Quantum-enhanced models like QLSTM may offer advantages in handling scarce or noisy financial data due to quantum parallelism and richer data representations
- [speculative] The integration of quantum layers in hybrid models could reduce overfitting and improve generalization in time series forecasting tasks
- [disputed] The paper claims quantum advantage in expressiveness and learning capacity, but results are based on simulations and lack comparison with state-of-the-art classical deep learning models (e.g., Transformers or ensemble methods)

**Results summary:** The paper presents a hybrid QLSTM framework for financial time series forecasting, combining classical LSTM with a Quantum Neural Network (QNN). The model was evaluated on AAPL stock data, demonstrating superior performance over classical LSTM in terms of accuracy (R² of 0.83 vs. 0.54), error metrics (MSE of 85.16 vs. 235.74), and generalization capability. The optimal quantum circuit configuration (ZZFeatureMap + RealAmplitudes) was identified through comparative testing. The QLSTM model also showed faster convergence and better handling of nonlinear patterns. However, all results are based on simulations, and the claimed quantum advantage remains speculative without validation on real quantum hardware or comparison with advanced classical baselines.

**Performance claims:**
- R² score of 0.83 for QLSTM vs. 0.54 for classical LSTM
- MSE of 85.16 for QLSTM vs. 235.74 for classical LSTM
- MAE of 7.49 for QLSTM vs. 13.53 for classical LSTM
- RMSE of 9.23 for QLSTM vs. 15.35 for classical LSTM
- QLSTM achieved MSE of 0.0018 with ZZFeatureMap + RealAmplitudes ansatz
- QLSTM required fewer trainable parameters and less training data than classical LSTM
## Quantum advantage claim
**Classification:** speculative

The paper claims enhanced expressiveness and learning capacity due to quantum layers, but all results are derived from simulations. No empirical evidence is provided for quantum advantage on real hardware, and the performance comparison is limited to classical LSTM without benchmarking against state-of-the-art classical models. The claimed advantages remain theoretical and unvalidated in practical settings.
## Limitations
- Experiments conducted on a single stock (AAPL) over a limited time period (June 2019 to May 2025), which may not generalize to other stocks or market conditions [inferred]
- Use of only 4 qubits in the Quantum Neural Network (QNN) layer, limiting the model's capacity to capture complex patterns [inferred]
- Evaluation restricted to synthetic or simplified quantum circuit designs (e.g., ZZFeatureMap, RealAmplitudes) without testing on real quantum hardware
- No comparison with state-of-the-art classical time-series models (e.g., Transformer-based architectures, N-BEATS) to benchmark quantum advantage [inferred]
- Lack of noise mitigation techniques, which may affect performance on real NISQ (Noisy Intermediate-Scale Quantum) devices [inferred]
- Page-limit constraints of the conference paper may have omitted details on hyperparameter tuning, training stability, or failure cases [inferred]
- No discussion on the computational overhead of hybrid quantum-classical training compared to classical baselines [inferred]
- Limited exploration of quantum circuit depth and its impact on model performance and trainability
- Potential overfitting due to small dataset size (1,508 daily observations) relative to the complexity of the hybrid model [inferred]
- No empirical validation of the model's robustness to market regime shifts (e.g., crashes, bubbles) [inferred]
## Open questions
- How does the QLSTM framework perform on multi-asset or high-frequency financial data?
- What is the scalability of the hybrid model with increasing qubit counts and circuit depth?
- How does the model's performance degrade under realistic quantum noise conditions?
- Can the hybrid architecture outperform classical models in low-data regimes, and if so, under what conditions?
- What is the impact of different quantum encoding strategies (e.g., amplitude encoding) on prediction accuracy?
- How does the choice of ansatz (e.g., EfficientSU2 vs. RealAmplitudes) affect the model's ability to generalize?
- What are the trade-offs between quantum circuit expressivity and trainability in financial time-series forecasting?
- How can the model be adapted for real-time forecasting in dynamic market environments?

**Future work:**
- Extend the framework to multi-stock or portfolio-level forecasting
- Test the model on real quantum hardware (e.g., IBM Quantum, Rigetti) to evaluate noise resilience
- Compare the QLSTM with advanced classical models (e.g., Temporal Fusion Transformers, Informer) to quantify quantum advantage
- Explore alternative quantum circuit designs (e.g., QAOA-inspired ansatz) for improved performance
- Investigate noise mitigation techniques (e.g., error mitigation, dynamical decoupling) for NISQ-era deployment
- Apply the framework to other time-series domains (e.g., energy demand forecasting, climate modeling)
- Develop hybrid training strategies to reduce computational overhead and improve scalability
- Benchmark the model's performance across different market regimes (e.g., bull/bear markets, high volatility periods)
- Integrate attention mechanisms into the quantum layer to enhance long-range dependency modeling
## Key ideas
- #idea:hybrid-approach — Hybrid QLSTM framework combines classical LSTM with Quantum Neural Networks (QNNs) to leverage temporal pattern recognition and quantum parallelism
- #idea:quantum-advantage — QLSTM outperforms classical LSTM in stock price prediction (R² 0.83 vs. 0.54) with fewer trainable parameters and less training data
- #idea:near-term-feasibility — Proposes a NISQ-era applicable model using 4 qubits and quantum simulators for financial time series forecasting
- #limitation:no-empirical-validation — Quantum advantage claims are speculative and based solely on simulations without real QPU validation
- #limitation:simulation-only — All experiments conducted on quantum simulators, not real quantum hardware
- #limitation:data-encoding — Limited exploration of quantum encoding strategies and their impact on prediction accuracy
## Contradictions
- #contradiction:classical-vs-quantum — Claims quantum advantage over classical LSTM but lacks comparison with state-of-the-art classical models (e.g., Transformers, ensemble methods)
- #contradiction:scalability — Demonstrates performance on a single stock (AAPL) with 4 qubits, but scalability to multi-asset or high-frequency data remains untested
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
