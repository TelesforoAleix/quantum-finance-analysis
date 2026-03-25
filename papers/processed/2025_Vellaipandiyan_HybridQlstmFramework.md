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
- idea:quantum-advantage
- idea:near-term-feasibility
- idea:hybrid-approach
journal_or_venue: 2025 4th International Conference on Innovative Mechanisms for Industry
  Applications (ICIMIA)
methodology_tags:
- quantum-ML
- variational
paper_type: ''
quantum_advantage_claim: speculative
related_papers: []
relevance_phase1: medium
relevance_phase3: medium
source_type: peer-reviewed-empirical
source_type_confidence: high
step1_date: '2026-03-25T16:12:34.285029'
step1_model: gpt-5.1
step2_date: '2026-03-25T16:12:38.555569'
step2_model: gpt-5.1
step3_date: '2026-03-25T16:13:02.849909'
step3_model: gpt-5.4
step4_date: '2026-03-25T16:13:35.120726'
step4_model: gpt-5.4
step5_date: '2026-03-25T16:14:06.187375'
step5_model: gpt-5.4
step6_date: '2026-03-25T16:14:18.055957'
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
- idea/quantum-advantage
- idea/near-term-feasibility
- idea/hybrid-approach
- contradiction/classical-vs-quantum
- contradiction/scalability
title: Hybrid QLSTM Framework for Time Series Forecasting in Dynamic Financial Markets
topic_tags:
- asset-pricing
year: 2025
zotero_key: ''
---

## Abstract summary
The paper proposes a hybrid quantum-classical LSTM (QLSTM) framework for financial time series forecasting, focusing on stock price prediction for Apple Inc. using Yahoo Finance data. It combines a classical LSTM with a quantum neural network layer, systematically testing different feature map and ansatz circuit configurations to identify an effective quantum circuit design. The study then empirically compares the resulting QLSTM model against a purely classical LSTM, showing that the tuned hybrid model can better capture nonlinear patterns and improve predictive performance on stock closing prices.
## Methodology
The paper presents an empirical hybrid quantum-classical time-series forecasting study for stock-price prediction using Apple (AAPL) market data. Historical daily data were collected from Yahoo Finance through the yfinance Python library, covering 1,508 trading-day observations from 2019-06-03 to 2025-05-30. The authors performed exploratory data analysis on closing-price trends, moving averages, yearly trading volume, quarterly OHLC trends, and gain/loss day counts. For modeling, they selected Open, High, Low, Close, and Volume columns, removed missing and non-numeric rows, normalized values to the [0,1] range, used Close as the prediction target, and excluded it from the input features. A sliding-window formulation was applied with 20 prior days used to predict the next-day close, and the data were split chronologically into training (48%), validation (32%), and test (20%) sets to avoid leakage. The proposed architecture consists of a classical LSTM layer that encodes temporal dependencies, followed by a dense projection from a 16-dimensional hidden state to a 4-dimensional vector, tanh activation to map values into [-1,1], a quantum neural network layer operating on 4 qubits, and a final classical dense output layer for regression. The quantum layer was implemented as a variational circuit using feature-map/ansatz combinations, with the main reported best design being ZZFeatureMap with 2 repetitions and RealAmplitudes with 2 layers and full entanglement. The model was trained using RMSprop and MSE loss with early stopping. The study also empirically compared multiple quantum circuit configurations in the QNN layer and benchmarked the final QLSTM against a classical LSTM baseline using regression metrics including MSE, MAE, RMSE, R2, and explained variance.

**Algorithms used:** LSTM, QLSTM, QNN, ZZFeatureMap, PauliFeatureMap, ZFeatureMap, RealAmplitudes, EfficientSU2
**Frameworks:** yfinance

**Experimental setup:** A hybrid QLSTM-QNN regression model was evaluated for next-day stock closing-price prediction. The classical component used an LSTM with hidden size 16 over 20-day input sequences of four features (Open, High, Low, Volume). The LSTM output was reduced by a dense layer to 4 dimensions, passed through tanh, and fed into a 4-qubit quantum neural network. Several feature-map/ansatz combinations were tested, and the best-performing setup used ZZFeatureMap (reps=2) with RealAmplitudes (2 layers, full entanglement). Training used RMSprop, MSE loss, 100 epochs, and early stopping. The paper does not clearly specify whether experiments were run on a simulator or real quantum hardware.

**Dataset:** Historical Apple Inc. (AAPL) stock data from Yahoo Finance accessed via the yfinance Python library, with 1,508 daily trading observations from 2019-06-03 to 2025-05-30. Variables include Open, High, Low, Close, Adjusted Close, and Volume; the model used Open, High, Low, and Volume as inputs and Close as the target.
## Findings
- [supported] On Apple stock daily data (1,508 observations from 2019-06-03 to 2025-05-30), the hybrid QLSTM outperformed the classical LSTM on next-day closing-price forecasting using a 20-day sliding window.
- [supported] The best QLSTM configuration used 4 qubits, hidden size 16, learning rate 0.01, RMSprop optimizer, and 100 training epochs, achieving R² = 0.83, MSE = 85.16, MAE = 7.49, RMSE = 9.23, and explained variance = 0.89.
- [supported] The classical LSTM baseline achieved lower predictive performance, with R² = 0.54, MSE = 235.74, MAE = 13.53, and RMSE = 15.35.
- [supported] Among tested quantum circuit designs, ZZFeatureMap + RealAmplitudes and PauliFeatureMap + RealAmplitudes performed best in the QNN layer, each with MSE = 0.0018 and RMSE = 0.0424 on the normalized evaluation, with R² values of 0.8372 and 0.8347 respectively.
- [supported] Quantum circuit choices using EfficientSU2 or ZFeatureMap performed substantially worse, including negative R² values (e.g., -9.9449, -22.0447, -31.9975, -45.3378), indicating unstable or poor predictions.
- [supported] The authors report smoother training and validation loss convergence for QLSTM than for classical LSTM, interpreting this as better generalization and faster learning in their experiment.
- [supported] The study's empirical results are based on a hybrid quantum-classical model with simulated quantum circuits/software-based QNN components rather than evidence from real quantum hardware execution.
- [speculative] The authors argue that the quantum layer improves expressiveness by capturing nonlinear dependencies in Hilbert space that classical models struggle to represent, but this mechanism is inferred from comparative performance rather than directly validated.
- [speculative] The paper suggests hybrid quantum-classical forecasting may provide a practical route for handling complex financial time series more effectively, but evidence is limited to a single-stock case study.

**Results summary:** The paper evaluates a hybrid QLSTM framework for forecasting Apple stock prices using 1,508 daily observations from Yahoo Finance. The model uses a classical LSTM to encode 20-day temporal windows, a dense projection to 4 dimensions, and a 4-qubit QNN layer built from feature-map and ansatz circuits. In the main comparison, the best QLSTM configuration outperformed a classical LSTM baseline, achieving R² = 0.83 versus 0.54, with lower errors (MSE 85.16 vs 235.74, MAE 7.49 vs 13.53, RMSE 9.23 vs 15.35). The authors also benchmarked multiple quantum circuit designs and found ZZFeatureMap + RealAmplitudes and PauliFeatureMap + RealAmplitudes to be the strongest options, while several alternatives produced strongly negative R² values. No confidence intervals or statistical significance tests are reported. Results appear to come from simulation/hybrid software execution rather than real quantum hardware.

**Performance claims:**
- Best QLSTM: R² = 0.83, MSE = 85.16, MAE = 7.49, RMSE = 9.23, explained variance = 0.89
- Classical LSTM: R² = 0.54, MSE = 235.74, MAE = 13.53, RMSE = 15.35
- ZZFeatureMap + RealAmplitudes: MSE = 0.0018, MAE = 0.0336, RMSE = 0.0424, R² = 0.8372, explained variance = 0.897
- PauliFeatureMap + RealAmplitudes: MSE = 0.0018, MAE = 0.0338, RMSE = 0.0424, R² = 0.8347, explained variance = 0.8932
- PauliFeatureMap + EfficientSU2: MSE = 0.1186, MAE = 0.3406, RMSE = 0.3444, R² = -9.9449, explained variance = 0.7589
- ZZFeatureMap + EfficientSU2: MSE = 0.2498, MAE = 0.4921, RMSE = 0.4998, R² = -22.0447, explained variance = 0.2913
- ZFeatureMap + RealAmplitudes: MSE = 0.3577, MAE = 0.5889, RMSE = 0.5981, R² = -31.9975, explained variance = -0.0019
- ZFeatureMap + EfficientSU2: MSE = 0.5023, MAE = 0.7010, RMSE = 0.7087, R² = -45.3378, explained variance = -0.005
- Dataset: 1,508 daily observations; split = 48% train, 32% validation, 20% test
- Model setup: 4 qubits, sequence length = 20, hidden size = 16, learning rate = 0.01, 100 epochs
## Quantum advantage claim
**Classification:** speculative

The paper shows better forecasting metrics for a hybrid QLSTM than a classical LSTM baseline on one dataset, but it does not demonstrate quantum advantage in the strict sense. Results are from a small-scale hybrid/simulated setup, with no real-hardware evidence, no complexity-theoretic speedup, and no statistical uncertainty analysis.
## Limitations
- Experiments use only a single stock (AAPL) from Yahoo Finance, limiting external validity across assets, sectors, and market regimes
- The dataset contains only about 1,508 daily observations over six years, which is relatively small for training and validating deep sequential forecasting models
- The quantum model uses only 4 qubits, constraining representational capacity and limiting conclusions about larger-scale financial forecasting problems
- The study evaluates one-step-ahead forecasting with a 20-day sliding window only, so results may not generalize to longer horizons or different temporal dependencies
- Practical hurdles such as circuit depth, stability, and hardware are acknowledged in the related studies discussion as barriers to widespread adoption
- The paper does not report experiments on real quantum hardware; the QNN appears to be evaluated without demonstrating performance under hardware noise or decoherence
- [inferred] Results are likely obtained in simulation rather than on NISQ devices, so claimed gains may not hold under realistic quantum noise
- [inferred] No noise-mitigation strategy is described, which weakens claims about near-term deployability on actual quantum processors
- [inferred] The comparison baseline is limited mainly to a classical LSTM; there is no benchmarking against stronger classical time-series models such as GRU, Transformer, XGBoost, ARIMA, or modern foundation-style forecasting baselines
- [inferred] Hyperparameter tuning fairness is unclear; the paper reports a tuned QLSTM configuration but does not provide equivalent tuning detail for the classical baseline, which may bias the comparison
- [inferred] Reproducibility is limited because the paper does not provide code, random seeds, circuit execution details, number of runs, confidence intervals, or statistical significance tests
- [inferred] The train/validation/test split (48/32/20) is unusual and no walk-forward or rolling-window backtesting is reported, reducing robustness for financial time-series evaluation
- [inferred] Only one data source and one market variable set are used, with no test on alternative features such as macroeconomic indicators, news, or technical indicators
- [inferred] The paper focuses on predictive error metrics only and does not evaluate trading utility, transaction costs, risk-adjusted returns, or economic significance
- [inferred] Scalability to production is unproven because the study does not discuss inference latency, training cost, integration with live data pipelines, or operational constraints in financial services
- [inferred] The claim that losses become almost zero and that the model generalizes better may indicate possible overfitting or leakage concerns, especially without repeated experiments or stronger validation protocols
## Open questions
- Will the reported QLSTM advantage persist across multiple stocks, indices, asset classes, and different market conditions?
- How does the model perform on larger and more diverse financial datasets than a single-stock daily series?
- How sensitive are results to the number of qubits, circuit depth, feature map choice, ansatz design, and optimizer settings?
- Do the observed gains remain when the model is executed on real quantum hardware with noise and limited coherence times?
- Can the hybrid architecture scale beyond 4 qubits and still remain trainable and computationally efficient?
- How does QLSTM compare against stronger classical baselines under equally rigorous hyperparameter tuning?
- Are the improvements statistically significant across multiple runs and random initializations?
- Would the model remain effective for multi-step forecasting, intraday prediction, volatility forecasting, or regime shifts?
- What is the economic value of the improved forecasts when translated into trading or risk-management decisions?
- Which parts of the performance gain come from the quantum layer itself versus architectural or tuning choices in the classical components?

**Future work:**
- Benchmark the proposed hybrid QLSTM against additional classical and quantum models, as the paper states a goal of benchmarking against classical and quantum models
- Study the impact of different quantum layers, feature maps, and ansatz circuits more systematically, since the paper notes that the impact of quantum layers needs further study
- Develop a more robust and practical model for real-world forecasting, as stated in the paper's motivation
- Extend evaluation to more financial instruments and broader market datasets beyond Apple stock
- Test the framework on real quantum hardware and assess robustness under hardware noise, circuit instability, and NISQ constraints
- Explore larger qubit counts and more expressive circuits while monitoring scalability and trainability
- Use stronger validation protocols such as rolling-window backtesting and repeated trials to improve internal validity
- Assess production readiness by studying latency, computational cost, and deployment feasibility in live financial systems
- Evaluate downstream financial usefulness through trading simulations, portfolio applications, and risk-aware metrics
- Investigate longer forecasting horizons and more complex tasks such as multivariate, multi-asset, and regime-aware forecasting
## Key ideas
- #idea:hybrid-approach — The paper proposes a hybrid QLSTM architecture combining a classical LSTM for temporal feature extraction with a 4-qubit variational QNN layer for next-day stock-price forecasting.
- #idea:quantum-advantage — On a single AAPL daily dataset, the tuned QLSTM outperforms a classical LSTM baseline on regression metrics (e.g., R² 0.83 vs 0.54), suggesting possible quantum-enhanced expressiveness.
- #idea:near-term-feasibility — The model is framed as NISQ-compatible by using only 4 qubits and shallow feature-map/ansatz combinations such as ZZFeatureMap plus RealAmplitudes.
- #idea:hybrid-approach — Circuit design materially affects forecasting quality: ZZFeatureMap + RealAmplitudes and PauliFeatureMap + RealAmplitudes perform well, while several EfficientSU2 and ZFeatureMap variants perform poorly.
- #idea:quantum-advantage — The claimed benefit is empirical and task-specific rather than a strict quantum advantage, since it is based on predictive accuracy against a limited classical baseline rather than complexity-theoretic speedup.
## Contradictions
- The paper suggests quantum superiority via better QLSTM performance than a classical LSTM, but this is weakened by the absence of stronger classical baselines such as GRU, Transformer, XGBoost, or ARIMA; thus the evidence supports at most a narrow model-comparison win rather than broad quantum superiority.
- The paper presents the approach as promising for financial forecasting, yet the evidence is limited to a single-stock AAPL dataset with 4 qubits and one-step-ahead prediction, contradicting any implication of scalability to broader, real-world financial forecasting tasks.
- The paper discusses near-term applicability, but the reported results appear to come from simulated quantum components rather than real noisy hardware, creating tension between NISQ-feasibility claims and practical deployability.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->

## Experiment details
### Input
Yahoo Finance AAPL daily stock data, 1,508 observations spanning 2019-06-03 to 2025-05-30. Original fields included Open, High, Low, Close, Adjusted Close, and Volume. Selected features were Open, High, Low, Close, and Volume; Close was used as the prediction target and excluded from model inputs. Rows with missing or non-numeric values were removed. All values were normalized to the [0,1] range. A sliding-window preprocessing scheme used 20 previous trading days to predict the next day's closing price. Data were split chronologically into 48% training, 32% validation, and 20% testing.

### Process
1. Download AAPL historical daily data from Yahoo Finance using yfinance. 2. Perform exploratory analysis on closing-price trend, moving averages, yearly volume, quarterly OHLC trends, and gain/loss counts. 3. Select Open, High, Low, Close, and Volume columns; remove missing/non-numeric rows. 4. Normalize values to [0,1]. 5. Construct supervised sequences using a 20-day sliding window, with Open/High/Low/Volume as inputs and next-day Close as target. 6. Split data chronologically into train/validation/test sets (48/32/20). 7. Feed each sequence into a classical LSTM with hidden size 16 to extract temporal features. 8. Project the LSTM hidden state through a dense layer to a 4-dimensional vector and apply tanh to map values into [-1,1]. 9. Encode the 4-dimensional vector into a 4-qubit quantum circuit using candidate feature maps and ansatz circuits. 10. Evaluate multiple quantum circuit combinations including ZZFeatureMap + RealAmplitudes, PauliFeatureMap + RealAmplitudes, PauliFeatureMap + EfficientSU2, ZZFeatureMap + EfficientSU2, ZFeatureMap + RealAmplitudes, and ZFeatureMap + EfficientSU2. 11. Use the QNN output in a final dense layer to predict the closing price. 12. Train the hybrid model with RMSprop optimizer, MSE loss, and early stopping for up to 100 epochs. 13. Compare the selected QLSTM model against a classical LSTM baseline using regression metrics.

### Output
The outputs are regression predictions of next-day AAPL closing price and associated evaluation metrics. Quantum-circuit selection was reported using MSE, MAE, RMSE, R2, and explained variance. The best circuit combinations were ZZFeatureMap + RealAmplitudes and PauliFeatureMap + RealAmplitudes, both with MSE about 0.0018 and R2 about 0.83 in the circuit-comparison table. Final model benchmarking compared QLSTM against a classical LSTM baseline. The QLSTM reportedly achieved R2 = 0.83, MSE = 85.16, MAE = 7.49, RMSE = 9.23, and explained variance = 0.89, while the classical LSTM achieved R2 = 0.54, MSE = 235.74, MAE = 13.53, and RMSE = 15.35. The paper also presents training/validation loss curves and actual-vs-predicted plots as qualitative evidence.

### Parameters
- qubits: 4
- sequence_length: 20
- lstm_hidden_size: 16
- epochs: 100
- learning_rate: 0.01
- optimizer: RMSprop
- loss_function: MSE
- train_split_percent: 48
- validation_split_percent: 32
- test_split_percent: 20
- feature_map_best: ZZFeatureMap
- feature_map_reps_best: 2
- ansatz_best: RealAmplitudes
- ansatz_layers_best: 2
- entanglement_best: full
- activation_before_quantum_layer: tanh
- early_stopping: True

### Hardware
Not clearly reported. The paper describes a 4-qubit QNN layer and variational quantum circuits but does not specify whether execution used a simulator or real QPU, nor does it name a backend, cloud provider, noise model, transpilation settings, or shot count.

### Reproducibility
Partial reproducibility. The data source is public and clearly identified (Yahoo Finance via yfinance), and the paper provides useful preprocessing and architectural details such as sequence length, split ratios, hidden size, optimizer, learning rate, epochs, and candidate quantum circuits. However, no code repository is provided, and key implementation details are missing, including the exact software stack, backend/simulator, shot count, optimizer settings for quantum training, early-stopping criteria, and some metric inconsistencies across tables. Replication is possible only approximately, not exactly.
