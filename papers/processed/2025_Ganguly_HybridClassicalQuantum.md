---
aliases:
- Hybrid Classical-Quantum Generative Algorithms for Financial Modelling and Prediction
- Hybrid Classical Quantum Generative
authors:
- Santanu Ganguly
- Xing Liang
- Dimitrios Makris
auto_detected: true
classification: ''
contradiction_flags:
- contradiction:classical-vs-quantum
- contradiction:scalability
doi: 10.1109/IC363308.2025.10956507
evidence_type: ''
idea_tags:
- idea:quantum-advantage
- idea:near-term-feasibility
- idea:hybrid-approach
journal_or_venue: 2025 International Conference on Intelligent Control, Computing
  and Communications (IC3)
methodology_tags:
- quantum-ML
- variational
- QUBO
- classical-simulation
paper_type: ''
quantum_advantage_claim: speculative
related_papers:
- 2022_Herman_QuantumMonteCarlo
- 2023_Smith_DeepLearningFinance
relevance_phase1: high
relevance_phase3: medium
source_type: conference-paper
source_type_confidence: high
step1_date: '2026-03-20T00:18:26.693719'
step1_model: Mistral-Large-3
step2_date: '2026-03-20T00:18:30.342923'
step2_model: Mistral-Large-3
step3_date: '2026-03-20T00:18:51.261941'
step3_model: Mistral-Large-3
step4_date: '2026-03-20T00:19:05.116727'
step4_model: Mistral-Large-3
step5_date: '2026-03-20T00:19:15.807321'
step5_model: Mistral-Large-3
step6_date: '2026-03-20T00:19:31.813819'
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
- topic/portfolio-optimisation
- topic/risk-modelling
- topic/high-frequency-trading
- topic/fraud-detection
- method/quantum-ML
- method/variational
- method/QUBO
- method/classical-simulation
- idea/quantum-advantage
- idea/near-term-feasibility
- idea/hybrid-approach
- contradiction/classical-vs-quantum
- contradiction/scalability
title: Hybrid Classical-Quantum Generative Algorithms for Financial Modelling and
  Prediction
topic_tags:
- asset-pricing
- portfolio-optimisation
- risk-modelling
- high-frequency-trading
- fraud-detection
year: 2025
zotero_key: ''
---

## Abstract summary
This conference paper explores the application of hybrid classical-quantum machine learning models in financial services, focusing on quantum generative adversarial networks (qGAN), quantum long short-term memory (QLSTM), and quantum circuit Born machines (QCBM). The authors implement these models using real-world cryptocurrency and stock price datasets to assess their predictive capabilities compared to classical counterparts. The study demonstrates the potential advantages of quantum-enhanced models for financial forecasting, particularly in handling volatile and non-linear financial data.
## Methodology
The paper presents an empirical study on hybrid classical-quantum machine learning algorithms applied to financial modeling and prediction. It implements three quantum algorithms: Quantum Generative Adversarial Networks (qGAN), Quantum Long Short-Term Memory (QLSTM), and Quantum Circuit Born Machine (QCBM). For qGAN, real-world cryptocurrency data from Binance was used to train a quantum generator with a classical discriminator, aiming to model uncertainty in option pricing. The QLSTM model was applied to NVIDIA stock price data spanning 210 days, comparing its performance against a classical LSTM for time-series prediction. QCBM was tested using a synthetic bars and stripes (BAS) dataset to demonstrate generative modeling capabilities. The experiments were conducted using quantum simulators, leveraging frameworks such as Qiskit and PennyLane, with GPU acceleration for training efficiency. The study evaluates the algorithms based on training and test loss, prediction accuracy, and computational performance across different hardware setups.

**Algorithms used:** qGAN, QLSTM, QCBM
**Frameworks:** Qiskit, PennyLane, PyTorch, CUDA-Q, Lightning.gpu

**Experimental setup:** Experiments were conducted using a combination of quantum simulators and classical computing resources. The qGAN and QCBM implementations utilized an NVIDIA RTX 3070 GPU on Linux Ubuntu 22.04 LTS with CUDA-Q for acceleration. The QLSTM and LSTM models were run on both an NVIDIA RTX 3070 GPU and an Apple M3 MacBook with a 30-core GPU. Libraries such as Qiskit and PennyLane were employed for quantum circuit simulation and training, while PyTorch was used for classical machine learning components.

**Dataset:** Three datasets were used: (1) Real-world cryptocurrency data from Binance for five cryptocurrencies (BNBBTC, ETHBTC, LTCBTC, NEOBTC, QTUMETH) with over 5000 samples, filtered to reduce qubit requirements. (2) Real-life NVIDIA stock price data spanning 210 days for time-series prediction. (3) A synthetic bars and stripes (BAS) dataset for QCBM evaluation.
## Findings
- [supported] QLSTM test predictions for NVIDIA stock data were slightly superior to classical LSTM, particularly around volatile peaks, indicating better alignment with real-life data
- [supported] QLSTM demonstrated earlier prediction of turning points in stock market trends compared to classical LSTM, potentially offering advantages in forecasting market movements
- [supported] QLSTM training loss exhibited smoothing over time, unlike classical LSTM where loss spikes appeared more pronounced toward the end of training
- [supported] qGAN successfully modeled cryptocurrency data distributions with fewer iterations than classical GANs, achieving equilibrium in generator and discriminator loss functions
- [supported] qGAN combined with QUBO optimization predicted BNBBTC as the optimal cryptocurrency investment based on real-world Binance data
- [supported] QCBM with SPSA optimization closely approximated the target probability distribution for the synthetic BAS dataset, outperforming other optimizers like Cobyla
- [supported] Training time for QLSTM was highly dependent on GPU type, with NVIDIA RTX 3070 showing a 50% reduction in training time per epoch compared to RTX 3060 (780s vs. 1600s)
- [supported] CUDA-Q acceleration significantly improved QLSTM training performance, reducing training time per epoch from 780s to 18s on an RTX 3070
- [speculative] Hybrid quantum-classical models (qGAN, QLSTM, QCBM) may offer quantum advantage in financial forecasting and risk analysis when combined and scaled to larger datasets
- [speculative] Quantum generative models like qGAN and QCBM could deliver quantum advantage on NISQ devices due to their inherent probabilistic nature and expressive power
- [speculative] QLSTM's performance advantages may become more pronounced with larger datasets and further integration with qGAN and QCBM for temporal financial data analysis
- [speculative] The combination of qGAN, QLSTM, and QCBM could lead to robust financial models with improved accuracy and efficiency in stock prediction and portfolio optimization
- [disputed] The paper claims that QLSTM's test predictions are 'slightly superior' to classical LSTM, but the RMSE values (15.09 × 10⁻³ for QLSTM vs. 12.8 × 10⁻³ for LSTM) suggest classical LSTM may outperform QLSTM in some metrics

**Results summary:** The paper presents empirical results from three hybrid quantum-classical models applied to financial datasets: qGAN, QLSTM, and QCBM. For qGAN, the model successfully trained on real-world cryptocurrency data, achieving equilibrium in generator and discriminator loss functions and predicting BNBBTC as the optimal investment. QLSTM demonstrated marginally better test predictions than classical LSTM for NVIDIA stock data, particularly around volatile peaks, though it required significantly longer training times. GPU acceleration, especially with CUDA-Q, substantially improved QLSTM training efficiency. QCBM, tested on a synthetic BAS dataset, showed promising results with SPSA optimization closely approximating the target distribution. While the models show potential for quantum advantage in financial applications, all results are derived from simulations rather than real quantum hardware.

**Performance claims:**
- QLSTM test RMSE: 15.09 × 10⁻³ (vs. LSTM test RMSE: 12.8 × 10⁻³)
- QLSTM training RMSE: 19.05 × 10⁻³ (vs. LSTM training RMSE: 7.5 × 10⁻³)
- QLSTM training loss: 7.2 × 10⁻³ (vs. LSTM training loss: 4.5 × 10⁻³)
- QLSTM test loss: 5.5 × 10⁻³ (vs. LSTM test loss: 6.8 × 10⁻³)
- QLSTM training time per epoch: 780s on RTX 3070 (vs. 12s for LSTM)
- QLSTM training time per epoch with CUDA-Q: 18s on RTX 3070 (vs. 0.04s for LSTM)
- qGAN achieved equilibrium in generator and discriminator loss functions within 2000 training epochs
- QCBM with SPSA optimization closely approximated target probability distribution for BAS dataset
## Quantum advantage claim
**Classification:** speculative

The paper suggests potential quantum advantage for hybrid quantum-classical models (qGAN, QLSTM, QCBM) in financial applications, particularly in generative modeling and time-series forecasting. However, all results are derived from simulations on classical hardware, and no empirical evidence of quantum advantage on real quantum devices is provided. The claimed advantages remain theoretical and are contingent on future scaling and integration of these models.
## Limitations
- Experiments conducted on quantum simulators rather than real quantum hardware, limiting assessment of noise and decoherence effects [inferred]
- Qubit count constraints (e.g., 1-qubit state for qGAN, 4 qubits for QLSTM VQCs) restrict scalability to larger financial datasets
- QLSTM training time is significantly longer than classical LSTM (e.g., 780 sec/epoch on RTX 3070 vs. 12 sec/epoch for LSTM), limiting practical deployment
- QCBM evaluation limited to synthetic BAS dataset (2×2 binary images), not real financial data [inferred]
- Lack of noise mitigation techniques in quantum circuit implementations may affect performance on NISQ devices [inferred]
- Page-limit constraints of conference paper may have omitted detailed hyperparameter tuning or ablation studies [inferred]
- No comparison with state-of-the-art classical generative models (e.g., Transformer-based time-series models) for financial forecasting [inferred]
- Statistical significance testing (paired t-test on RMSE) shows marginal differences between QLSTM and LSTM, raising questions about quantum advantage
- QUBO optimization for qGAN used classical solvers (CLARABEL), not quantum annealing, limiting assessment of quantum speedup [inferred]
- Data preprocessing for qGAN (discarding outliers) may introduce bias in cryptocurrency distribution modeling [inferred]
- Limited dataset sizes (e.g., 210 days for NVIDIA stock, 5000 samples for cryptocurrencies) may not capture long-term market dynamics
- Assumption of quantum advantage in generative models (qGAN, QCBM) remains unproven for financial applications without empirical validation on hardware
## Open questions
- How do hybrid quantum-classical models (qGAN, QLSTM, QCBM) perform on real quantum hardware with noise and decoherence?
- What is the minimum qubit count required for quantum advantage in financial time-series forecasting?
- Can QLSTM outperform classical LSTM for longer time horizons (e.g., multi-year stock predictions) or higher-dimensional datasets?
- How does the performance of QCBM scale with larger synthetic datasets or real financial distributions?
- What noise mitigation techniques (e.g., error correction, dynamical decoupling) are most effective for financial QML models?
- Can hybrid models (e.g., qGAN + QLSTM) improve robustness in volatile market conditions?
- What are the computational trade-offs between quantum simulation (e.g., CUDA-Q) and classical GPU acceleration for QML?
- How does the choice of optimizer (e.g., SPSA vs. Cobyla) impact QCBM convergence for financial data?
- What are the implications of quantum randomness in generative models for risk management and regulatory compliance?

**Future work:**
- Test hybrid models on real quantum hardware (e.g., IBM Eagle, Rigetti Aspen) to assess noise resilience
- Extend QLSTM to multi-asset stock prediction and portfolio optimization
- Combine qGAN, QLSTM, and QCBM into a unified framework for financial forecasting and risk analysis
- Evaluate QCBM on real financial datasets (e.g., option pricing, credit risk distributions)
- Optimize quantum circuit architectures (e.g., ansatz design) for financial QML tasks
- Benchmark hybrid models against state-of-the-art classical methods (e.g., Transformers, XGBoost) on large-scale datasets
- Explore quantum annealing for QUBO-based optimization in qGAN workflows
- Investigate explainability and interpretability of quantum generative models for regulatory reporting
- Develop noise-aware training protocols for NISQ-era financial QML
- Leverage NVIDIA DGX Quantum stack with CUDA-Q for accelerated quantum simulation
## Key ideas
- #idea:hybrid-approach — Hybrid quantum-classical models (QLSTM, qGAN, QCBM) leverage classical optimization to enhance quantum circuit training for financial forecasting and generative tasks
- #idea:quantum-advantage — QLSTM demonstrated marginally better test prediction accuracy than classical LSTM for NVIDIA stock prices, particularly in volatile regions, suggesting potential quantum advantage in time-series forecasting
- #idea:near-term-feasibility — qGAN successfully trained on real-world cryptocurrency data, generating synthetic distributions with convergence at equilibrium, indicating near-term applicability despite hardware limitations
- #idea:hybrid-approach — QUBO optimization post-qGAN training identified the highest-return cryptocurrency (BNBBTC), showcasing hybrid quantum-classical pipelines for asset selection
- #limitation:noise — No noise mitigation techniques were applied, limiting the robustness of results for real NISQ devices
- #limitation:qubit-count — Experiments used limited qubit counts (1-qubit for qGAN, 4-qubits for QLSTM), restricting scalability to larger financial datasets
- #limitation:simulation-only — All quantum results were derived from classical simulations (Qiskit, PennyLane), with no validation on real quantum hardware
## Contradictions
- #contradiction:classical-vs-quantum — The paper claims potential quantum advantage for QLSTM, but classical LSTM achieved lower RMSE (12.8×10⁻³ vs. 15.09×10⁻³) and significantly faster training times (0.04s vs. 18s per epoch), contradicting the practical superiority of quantum models in this context (cf. 2023_Smith_DeepLearningFinance).
- #contradiction:scalability — The paper speculates about quantum advantage for QCBMs, but scalability to real-world financial data remains unproven, contradicting the feasibility of quantum generative models for large-scale applications (cf. 2022_Herman_QuantumMonteCarlo).
- #contradiction:classical-vs-quantum — While QLSTM showed slightly better test prediction accuracy in volatile regions, the overall performance metrics (RMSE, training time) favor classical LSTM, raising doubts about the claimed quantum advantage.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->

## Experiment details
### Input
{'qGAN': {'source': 'Binance API', 'size': 'Over 5000 samples for five cryptocurrencies', 'preprocessing': 'Samples smaller than 5% percentile and larger than 95% percentile were discarded. Data was discretized into 32 values (2^5) for quantum representation.', 'features': 'Price data for cryptocurrencies'}, 'QLSTM': {'source': 'Real-life NVIDIA stock price data', 'size': '210 days of data', 'preprocessing': 'Classical data encoded into quantum states using rotational gates (RY and RZ) for quantum circuit input.', 'features': 'Time-series stock price data'}, 'QCBM': {'source': 'Synthetic bars and stripes (BAS) dataset', 'size': 'Binary images of size 2x2', 'preprocessing': 'Basis encoding used to convert images into quantum states, with each pixel represented as a qubit.', 'features': 'Binary pixel values (0 or 1)'}}

### Process
{'qGAN': {'steps': ['1. Load cryptocurrency data and preprocess to filter outliers.', '2. Define quantum generator circuit with trainable parameters.', '3. Train qGAN using Adam optimizer with data batches of 1000 samples for 2000 epochs.', '4. Use a classical neural network as the discriminator for binary classification.', '5. Optimize trained generator output using QUBO for cryptocurrency selection.'], 'parameters': {'batch_size': 1000, 'epochs': 2000, 'optimizer': 'Adam', 'quantum_circuit_layers': 'Variational form with entanglement'}}, 'QLSTM': {'steps': ['1. Encode classical stock price data into quantum states using rotational gates.', '2. Implement QLSTM with 6 variational quantum circuits (VQCs), each with 4 qubits.', '3. Train QLSTM and classical LSTM using Adam optimizer for 50 epochs.', '4. Compare training and test predictions against real stock price data.'], 'parameters': {'epochs': 50, 'optimizer': 'Adam', 'qubits_per_VQC': 4, 'number_of_VQCs': 6, 'hidden_size': 7, 'parameters_size': 292}}, 'QCBM': {'steps': ['1. Generate synthetic BAS dataset and encode into quantum states.', '2. Define QCBM circuit with 5 layers of adjustable and fixed gates.', '3. Train QCBM using optimizers (Cobyla, SPSA, Nelder-Mead) to minimize cost function.', '4. Compare simulated probability distribution with real distribution.'], 'parameters': {'layers': 5, 'optimizer': 'SPSA', 'qubits': 'Dependent on dataset size (2x2 images)'}}}

### Output
{'qGAN': {'metrics': ['Generator and discriminator loss functions', 'Histogram distributions of cryptocurrency data'], 'baselines': 'Comparison with classical GAN performance and QUBO optimization results', 'output_format': 'Predicted best cryptocurrency for investment (BNBBTC)'}, 'QLSTM': {'metrics': ['Training and test loss', 'Root Mean Square Error (RMSE)', 'Prediction accuracy'], 'baselines': 'Classical LSTM model', 'output_format': 'Stock price predictions plotted against real data'}, 'QCBM': {'metrics': ['Cost function minimization', 'Probability distribution similarity'], 'baselines': 'Comparison with optimizers (Cobyla, SPSA, Nelder-Mead)', 'output_format': 'Simulated probability distribution compared to real distribution'}}

### Parameters
- qGAN: {'qubits': 1, 'circuit_depth': 'Variational (dependent on layers)', 'shots': 1000, 'optimizer': 'Adam', 'learning_rate': 'Default Adam settings'}
- QLSTM: {'qubits': 4, 'circuit_depth': 'Dependent on VQC layers', 'shots': 'Not specified (simulator-based)', 'optimizer': 'Adam', 'epochs': 50, 'hidden_size': 7}
- QCBM: {'qubits': 4, 'layers': 5, 'optimizer': 'SPSA', 'cost_function': 'Negative log-likelihood with perturbation'}

### Hardware
{'qGAN': {'simulator': 'Qiskit Aer', 'GPU': 'NVIDIA RTX 3070 with CUDA-Q', 'platform': 'Linux Ubuntu 22.04 LTS'}, 'QLSTM': {'simulator': 'PennyLane and Qiskit', 'GPU': ['NVIDIA RTX 3070', 'Apple M3 30-core GPU'], 'platform': ['Linux Ubuntu 22.04 LTS', 'macOS']}, 'QCBM': {'simulator': 'Qiskit', 'GPU': 'NVIDIA RTX 3070 with CUDA-Q', 'platform': 'Linux Ubuntu 22.04 LTS'}}

### Reproducibility
The paper provides detailed descriptions of the algorithms, datasets, and experimental setups, including preprocessing steps and parameter choices. Code references are made to libraries such as Qiskit, PennyLane, and PyTorch, which are publicly available. However, the paper does not explicitly provide links to repositories or raw datasets. The use of synthetic data for QCBM and public APIs (Binance) for qGAN suggests partial reproducibility, but full replication would require access to the exact preprocessing scripts and hardware configurations.
