---
aliases:
- A Hybrid Quantum-Classical Model for Stock Price Prediction Using Quantum-Enhanced
  Long Short-Term Memory
- Hybrid Quantum Classical Model
authors:
- Kimleang Kea
- Dongmin Kim
- Chansreynich Huot
- Tae-Kyung Kim
- Youngsun Han
auto_detected: true
classification: ''
contradiction_flags:
- contradiction:classical-vs-quantum
- contradiction:scalability
doi: 10.3390/e26110954
evidence_type: ''
idea_tags:
- idea:quantum-advantage
- idea:near-term-feasibility
- idea:hybrid-approach
journal_or_venue: Entropy
methodology_tags:
- quantum-ML
- variational
- classical-simulation
paper_type: ''
quantum_advantage_claim: speculative
related_papers: []
relevance_phase1: medium
relevance_phase3: medium
source_type: peer-reviewed-empirical
source_type_confidence: high
step1_date: '2026-03-25T16:03:44.488835'
step1_model: gpt-5.1
step2_date: '2026-03-25T16:03:49.168213'
step2_model: gpt-5.1
step3_date: '2026-03-25T16:04:18.578771'
step3_model: gpt-5.4
step4_date: '2026-03-25T16:04:42.545871'
step4_model: gpt-5.4
step5_date: '2026-03-25T16:05:15.322023'
step5_model: gpt-5.4
step6_date: '2026-03-25T16:05:23.894777'
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
- idea/quantum-advantage
- idea/near-term-feasibility
- idea/hybrid-approach
- contradiction/classical-vs-quantum
- contradiction/scalability
title: A Hybrid Quantum-Classical Model for Stock Price Prediction Using Quantum-Enhanced
  Long Short-Term Memory
topic_tags:
- asset-pricing
year: 2024
zotero_key: ''
---

## Abstract summary
The paper proposes a hybrid quantum-classical LSTM architecture (QLSTM) for stock price prediction, where the classical LSTM gates are replaced by variational quantum circuits. The authors test the model on Apple stock price time series using IBM quantum simulators (noiseless and noisy) and an actual IBM quantum device, and compare performance against classical LSTM and several specialized time-series models. They show that, in simulation, QLSTM achieves lower RMSE and higher accuracy than the classical baselines, while performance on real quantum hardware is currently limited by noise and device constraints.
## Methodology
The paper presents a peer-reviewed empirical study of a hybrid quantum-classical stock price prediction model called QLSTM, which replaces the gate computations of a classical LSTM with variational quantum circuits (VQCs). The authors use Apple Inc. stock time-series data and preprocess the data by normalization to the range [-1, 1], then split the dataset into 70% training and 30% testing. The QLSTM architecture contains six VQCs corresponding to forget, input, update, output, hidden-state transformation, and output transformation functions. Classical inputs are encoded into quantum states using Hadamard initialization followed by angle encoding with Ry and Rz rotations based on arctan(x) and arctan(x^2), then processed through variational layers with trainable single-qubit rotations and cyclic CNOT entanglement. Parameters are optimized using gradient-based learning with parameter-shift rules, Adam optimizer, and MSE loss over 50 epochs. Experiments compare QLSTM against a parameter-matched classical LSTM and several classical time-series/anomaly models (USAD, DAGMM, MSCRED, MTAD_GAT), and also reference QSVM results from prior work. The study evaluates performance using RMSE and a prediction accuracy metric, and tests the model in three quantum environments: noiseless IBM simulator, noisy IBM simulator, and real IBM quantum hardware (IBM Nazca) for inference. Additional experiments analyze the effect of qubit count on performance.

**Algorithms used:** QLSTM, LSTM, Variational Quantum Circuit, parameter-shift rule, Adam, USAD, DAGMM, MSCRED, MTAD_GAT, QSVM
**Frameworks:** PyTorch, PennyLane, IBM Quantum

**Experimental setup:** The QLSTM model was implemented in PyTorch and PennyLane. Training and simulation were performed on an IBM noiseless simulator and a noisy IBM simulator that incorporates noise characteristics from real quantum devices. Due to queue-time limitations, training was not conducted on real hardware; instead, prediction/inference was additionally run on an actual IBM quantum computer, IBM Nazca, accessed through the IBM Quantum cloud platform. The classical LSTM baseline was designed to have a similar parameter count to QLSTM for fair comparison.

**Dataset:** Apple Inc. stock price data from 1 January 2022 to 1 January 2023, consisting of 251 weekday observations with columns Date, Open, High, Low, and Close.
## Experiment details
### Input
Single-company stock time-series dataset from Apple Inc. covering 1 January 2022 to 1 January 2023; 251 observations collected on weekdays; features include Date, Open, High, Low, and Close. Data were preprocessed by normalization/scaling to the range [-1, 1] for numerical stability and faster convergence. The dataset was split into 70% training and 30% testing.

### Process
1. Collect Apple stock price data and preprocess by scaling values to [-1, 1]. 2. Split data into 70% training and 30% testing. 3. Build a classical LSTM baseline and a QLSTM model with six VQCs replacing LSTM gates. 4. For each VQC, initialize qubits, apply Hadamard gates, encode classical inputs using Ry(arctan(x)) and Rz(arctan(x^2)) rotations, then apply a variational layer with trainable single-qubit rotations and cyclic CNOT entanglement. 5. Measure PauliZ expectation values and use them in the QLSTM cell for hidden-state and output computation. 6. Train models using MSE loss, Adam optimizer, learning rate 0.01, for 50 epochs. 7. Compute gradients for quantum parameters using the parameter-shift rule with positive and negative shifts of pi/2. 8. Evaluate training and prediction performance using RMSE and accuracy. 9. Compare QLSTM under noiseless simulator, noisy simulator, and real IBM hardware inference against classical LSTM and other baselines. 10. Perform an ablation-style analysis varying the number of qubits from 4 to 15.

### Output
Reported outputs include training and prediction RMSE, training and prediction accuracy, training loss curves over 50 epochs, and qualitative prediction plots against actual stock prices. Baseline comparisons include classical LSTM, USAD, DAGMM, MSCRED, MTAD_GAT, and a referenced QSVM result. Key reported results: Noiseless QLSTM achieved prediction accuracy 0.9736 and RMSE 0.0602; Noisy QLSTM achieved 0.9210 and 0.0648; Actual QLSTM achieved 0.7619 and 0.1401; classical LSTM achieved 0.8815 and 0.0693.

### Parameters
- qlstm_vqcs: 6
- qubits: 7
- variational_depth: 2
- rotations_per_variational_layer: 3
- additional_scaling_parameters: 2
- qlstm_parameter_count: 254
- lstm_hidden_size: 7
- lstm_parameter_count: 288
- learning_rate: 0.01
- loss_function: MSE
- optimizer: Adam
- epochs: 50
- train_test_split: 70/30
- qubit_sweep_range: 4 to 15
- gradient_method: parameter-shift
- parameter_shift_amount: pi/2

### Hardware
Quantum experiments used IBM simulators in two modes: a noiseless IBM simulator and a noisy IBM simulator with noise derived from actual quantum devices. Real-hardware inference was run on the IBM Nazca quantum device via the IBM Quantum cloud platform. The paper does not specify shot count, backend configuration details, transpilation settings, or exact simulator backend names.

### Reproducibility
Code is publicly available on GitHub (https://github.com/QCL-PKNU/SPP-QLSTM). The data source is described and appears obtainable from public stock market records, though the exact download source is not explicitly stated in the excerpt. The paper provides substantial architectural and hyperparameter detail, but some implementation specifics such as shot counts, exact backend settings, and full preprocessing pipeline details are missing, so replication is feasible but not fully turnkey.
## Findings
- [supported] The proposed QLSTM achieved better test performance than the classical LSTM on Apple stock closing-price prediction, with prediction RMSE 0.0602 vs. 0.0693 and prediction accuracy 0.9736 vs. 0.8815 in the noiseless simulator setting.
- [supported] In training, noiseless QLSTM reached accuracy 1.00 with RMSE 0.0371, outperforming classical LSTM (training accuracy 0.92, RMSE 0.0567) and the other classical baselines reported.
- [supported] Under a noisy IBM simulator, QLSTM remained competitive, with training accuracy 0.9714, training RMSE 0.0511, prediction accuracy 0.9210, and prediction RMSE 0.0648, still better than the reported classical LSTM test metrics.
- [supported] On real IBM quantum hardware (IBM Nazca), QLSTM prediction performance degraded substantially to accuracy 0.7619 and RMSE 0.1401, underperforming the classical LSTM and simulator-based QLSTM results.
- [supported] Compared with additional classical baselines (USAD, DAGMM, MSCRED, MTAD_GAT), noiseless QLSTM had the best reported prediction metrics; the strongest non-QLSTM baseline shown was MTAD_GAT with prediction RMSE 0.0624 and accuracy 0.8857.
- [supported] The authors report that QLSTM delivered approximately a 10% improvement in prediction accuracy and about a 50% reduction in average RMSE relative to classical models, based on their benchmark table.
- [supported] Results were obtained primarily from simulation during training (noiseless and noisy IBM simulators), while real-hardware validation was limited to prediction/inference only because of queue-time constraints.
- [supported] Increasing the number of qubits from 4 to 15 did not monotonically improve performance; the paper reports cases of degradation (e.g., from 8 to 11 qubits), which the authors attribute to barren plateau effects and increased circuit complexity.
- [speculative] The paper argues that quantum data encoding into higher-dimensional Hilbert spaces improves representation efficiency and helps QLSTM capture temporal dependencies and complex patterns more effectively than classical models.
- [speculative] The authors suggest QLSTM could be extended beyond stock prediction to other time-series domains such as renewable energy, IoT, energy forecasting, and healthcare.
- [speculative] The paper discusses potential quantum efficiency and polynomial-time handling of large-scale high-dimensional data, but this was not empirically demonstrated in the reported experiments.
- [supported] The authors explicitly acknowledge that current state-of-the-art classical ML methods remain strong and that actual quantum hardware performance in this study was worse than classical counterparts.

**Results summary:** This peer-reviewed empirical study evaluates a hybrid quantum-classical QLSTM for stock price prediction using Apple stock data from 2022 (251 weekday observations, 70/30 train-test split). The model was trained on IBM simulators and tested both on simulators and on real IBM quantum hardware. In the noiseless simulator, QLSTM outperformed classical LSTM and several classical time-series baselines, achieving test RMSE 0.0602 and accuracy 0.9736 versus LSTM's 0.0693 and 0.8815. In the noisy simulator, QLSTM still performed well (test RMSE 0.0648, accuracy 0.9210). However, on actual IBM Nazca hardware, performance dropped markedly (RMSE 0.1401, accuracy 0.7619), indicating that the empirical gains are strongest in simulation and are not yet robust on current noisy hardware. The paper therefore provides simulation-backed evidence of improved predictive performance for this small-scale task, but not a demonstrated real-hardware quantum advantage.

**Performance claims:**
- Noiseless QLSTM: training accuracy 1.00, training RMSE 0.0371
- Noiseless QLSTM: prediction accuracy 0.9736, prediction RMSE 0.0602
- Noisy QLSTM: training accuracy 0.9714, training RMSE 0.0511
- Noisy QLSTM: prediction accuracy 0.9210, prediction RMSE 0.0648
- Actual-hardware QLSTM (IBM Nazca): prediction accuracy 0.7619, prediction RMSE 0.1401
- Classical LSTM: training accuracy 0.92, training RMSE 0.0567
- Classical LSTM: prediction accuracy 0.8815, prediction RMSE 0.0693
- USAD: training accuracy 0.9342, training RMSE 0.0708; prediction accuracy 0.8874, prediction RMSE 0.0672
- DAGMM: training accuracy 0.8947, training RMSE 0.0768; prediction accuracy 0.8410, prediction RMSE 0.0721
- MSCRED: training accuracy 0.9342, training RMSE 0.0720; prediction accuracy 0.8828, prediction RMSE 0.0680
- MTAD_GAT: training accuracy 0.9473, training RMSE 0.0668; prediction accuracy 0.8857, prediction RMSE 0.0624
- QSVM baseline from cited prior work: prediction accuracy 0.5894
- QLSTM parameter count 254 vs. classical LSTM parameter count 288
- Training used 50 epochs, learning rate 0.01, Adam optimizer, MSE loss
- Dataset size: 251 observations from Apple stock prices, with 70% training and 30% testing split
- Authors summarize gains as approximately 10% higher accuracy and about 50% lower average RMSE than classical models
## Quantum advantage claim
**Classification:** speculative

The paper reports better predictive metrics for QLSTM than classical baselines, but the strongest results are from noiseless/noisy simulation rather than end-to-end real-hardware training, and real IBM hardware inference performed worse than classical LSTM. Thus, no demonstrated quantum advantage is established; any advantage remains speculative and task-specific.
## Limitations
- Dataset scope is limited to 251 Apple stock-price observations from a single company and a single year, restricting generalizability.
- Due to limitations of quantum simulations and long queue times for IBM hardware, experiments used only a small dataset.
- Model design is narrow: the study uses specific hyperparameters, a specific quantum data-encoding layer, selected rotation gates, and a particular variational layer design.
- Simulation limitations: the study initially employed only a few qubits, limiting assessment of larger-scale behavior.
- Actual quantum hardware performance was worse than classical counterparts, indicating limited current practical utility on real devices.
- Noise in actual quantum machines significantly degrades solution quality through decoherence and related hardware errors.
- The study does not implement quantum error-mitigation techniques; addressing noise is explicitly stated to be beyond the scope of the paper.
- Training on actual IBM quantum hardware was not performed because of prolonged queuing times; only prediction was run on real hardware.
- The authors acknowledge that quantum circuits are not yet fully operational for inference and practical applications.
- The paper notes that state-of-the-art classical ML techniques still steadily outperform QC techniques in practical settings.
- The possibility of classical simulation of certain noisy and noiseless VQCs in polynomial time weakens claims of clear quantum advantage for small to medium problem sizes.
- Increasing qubit count did not consistently improve performance, and in some cases performance degraded due to barren plateau effects.
- [inferred] External validity is limited because only one asset (Apple) was studied rather than multiple stocks, sectors, or market regimes.
- [inferred] The train/test split appears to be a single 70/30 split with no rolling-window or walk-forward validation, which is weak for time-series evaluation.
- [inferred] The dataset excludes exogenous financial drivers such as macroeconomic variables, news, sentiment, and firm fundamentals, limiting realism for stock prediction.
- [inferred] Reproducibility may be incomplete despite code availability because hardware calibration states, queue conditions, and exact noise profiles on IBM devices can vary over time.
- [inferred] Comparison baselines are limited; there is no benchmarking against stronger modern forecasting architectures such as Transformers, TCNs, or advanced financial forecasting pipelines.
- [inferred] The reported accuracy metric is nonstandard or ambiguously defined for regression, which may complicate interpretation and comparison.
- [inferred] No statistical significance testing or repeated-run variance analysis is reported, so robustness of the observed gains is unclear.
- [inferred] Scalability to production financial services is unproven given hardware access delays, noise sensitivity, and limited real-hardware performance.
## Open questions
- Will QLSTM maintain its performance advantage on larger datasets and with more qubits?
- Which quantum circuit designs, gate types, gate counts, and variational depths are most effective for stock-price prediction?
- Where is the boundary at which quantum computation significantly outperforms classical simulation for this task?
- How much can quantum error mitigation improve QLSTM performance on actual hardware?
- Can deeper variational quantum circuits improve expressiveness and generalization without triggering severe barren plateaus?
- Why does increasing the number of qubits sometimes degrade performance rather than improve it?
- How robust is QLSTM across different stocks, markets, time periods, and non-financial time-series domains?
- Can quantum-inspired classical algorithms deliver similar benefits for smaller-scale applications without quantum hardware overhead?
- [inferred] How would the model perform under realistic financial backtesting settings such as rolling forecasts, regime shifts, and transaction-aware decision pipelines?
- [inferred] Are the reported gains stable across repeated runs under stochastic training and changing hardware noise conditions?

**Future work:**
- Expand QLSTM scalability by evaluating with larger datasets and larger qubit numbers.
- Explore more advanced quantum error mitigation techniques to address noise limitations on actual quantum machines.
- Experiment with deeper variational quantum circuits to study their effect on model expressiveness and generalization.
- Investigate diverse quantum circuit designs, including different gate types, gate quantities, and variational-layer depths.
- Identify the regimes in which quantum computation meaningfully outperforms classical simulation.
- Integrate quantum-inspired algorithms to bridge the gap between quantum and classical models and enable quantum-like performance on classical hardware for smaller-scale applications.
- Extend QLSTM beyond stock-price prediction to other time-series domains such as energy forecasting and healthcare.
- [inferred] Validate the approach on multiple assets, broader financial datasets, and longer historical horizons.
- [inferred] Benchmark against stronger state-of-the-art classical forecasting models and conduct more rigorous statistical evaluation.
- [inferred] Test production-oriented deployment feasibility under real-hardware constraints, latency, and reproducibility requirements.
## Key ideas
- #idea:hybrid-approach — Proposes a hybrid QLSTM that replaces classical LSTM gate computations with variational quantum circuits and trains the overall model with classical optimization.
- #idea:quantum-advantage — In noiseless and noisy simulator settings, QLSTM reports better RMSE and accuracy than a parameter-matched classical LSTM and several other classical baselines on Apple stock prediction.
- #idea:near-term-feasibility — Evaluates the model under noiseless simulation, noisy simulation, and limited real-hardware inference, positioning the approach as a NISQ-era hybrid workflow rather than a fully fault-tolerant solution.
- #idea:quantum-advantage — The paper attributes simulator-side gains to richer quantum feature representations via Hilbert-space encoding, but does not provide runtime or complexity evidence for true computational advantage.
- #idea:near-term-feasibility — Real IBM hardware inference shows substantial degradation from simulator performance, highlighting current noise sensitivity and the gap between proof-of-concept and deployment.
## Contradictions
- Simulator-based results suggest QLSTM outperforms classical baselines, but real IBM hardware inference underperforms the classical LSTM, contradicting any practical claim of current quantum superiority (#contradiction:classical-vs-quantum).
- The paper speculates that larger quantum models may scale favorably, yet qubit-scaling experiments are non-monotonic and sometimes worsen performance, contradicting simple scaling narratives (#contradiction:scalability).
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
