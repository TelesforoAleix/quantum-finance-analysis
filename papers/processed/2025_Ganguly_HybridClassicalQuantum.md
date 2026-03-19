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
relevance_phase3: high
source_type: conference-paper
source_type_confidence: high
step1_date: '2026-03-19T13:22:18.789089'
step1_model: Mistral-Large-3
step2_date: '2026-03-19T13:22:35.040117'
step2_model: Mistral-Large-3
step3_date: '2026-03-19T13:23:32.398763'
step3_model: Mistral-Large-3
step4_date: '2026-03-19T13:24:27.566607'
step4_model: Mistral-Large-3
step5_date: '2026-03-19T13:25:14.799726'
step5_model: Mistral-Large-3
step6_date: '2026-03-19T13:25:50.988371'
step6_model: Mistral-Large-3
steps_completed:
- 1
- 2
- 3
- 4
- 5
- 6
tags:
- topic/risk-modelling
- topic/asset-pricing
- topic/market-simulation
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
- risk-modelling
- asset-pricing
- market-simulation
- fraud-detection
year: 2025
zotero_key: ''
---

## Abstract summary
This paper explores the application of hybrid classical-quantum machine learning models in financial services, focusing on generative algorithms. It implements quantum generative adversarial networks (qGAN), quantum long short-term memory (QLSTM), and quantum circuit Born machines (QCBM) using real-world cryptocurrency and stock price datasets. The study compares the performance of these quantum models against classical counterparts, demonstrating potential advantages in financial forecasting and risk analysis, particularly for time-series data.
## Methodology
The paper presents an empirical study on hybrid classical-quantum machine learning algorithms applied to financial modeling and prediction. It implements three quantum algorithms: quantum Generative Adversarial Networks (qGAN), Quantum Long Short-Term Memory (QLSTM), and Quantum Circuit Born Machine (QCBM). The qGAN is used for cryptocurrency forecasting with real-world data from Binance, employing a variational quantum circuit (VQC) as the generator and a classical neural network as the discriminator. The QLSTM is applied to NVIDIA stock price prediction, leveraging variational quantum circuits (VQCs) to enhance classical LSTM's ability to process non-linear relationships in time-series data. The QCBM is tested on a synthetic bars and stripes (BAS) dataset for generative modeling. The study compares quantum models with their classical counterparts (e.g., QLSTM vs. LSTM) using real financial datasets and synthetic data, evaluating performance through loss functions, prediction accuracy, and training efficiency. Experiments were conducted using quantum simulators and classical GPUs, with optimization techniques such as Adam and SPSA employed for training.

**Algorithms used:** qGAN, QLSTM, QCBM, QUBO, VQC (Variational Quantum Circuit)
**Frameworks:** Qiskit, PennyLane, PyTorch, CUDA-Q, Lightning.gpu

**Experimental setup:** Experiments were conducted using a combination of quantum simulators and classical hardware. The qGAN and QCBM simulations were performed on an NVIDIA RTX 3070 GPU running Linux Ubuntu 22.04 LTS, leveraging CUDA-Q for acceleration. The LSTM and QLSTM models were run on an Apple M3 MacBook with a 30-core GPU and the same NVIDIA platforms. Libraries such as Qiskit and PennyLane were used for quantum circuit simulations, while PyTorch was employed for classical machine learning components. The Lightning.gpu framework was utilized to enhance quantum machine learning performance in PennyLane.

**Dataset:** 1. Real-world cryptocurrency data from Binance for five cryptocurrencies (BNBBTC, ETHBTC, LTCBTC, NEOBTC, QTUMETH) with over 5000 samples, filtered to reduce qubit requirements. 2. Real-life NVIDIA stock price data spanning 210 days until August 2024. 3. Synthetic bars and stripes (BAS) dataset for QCBM evaluation, consisting of 2x2 binary images.
## Findings
- [supported] QLSTM test predictions for NVIDIA stock data were slightly superior to classical LSTM, particularly around volatile peaks, making it a promising candidate for financial forecasting [supported by RMSE values of 15.09×10⁻³ (QLSTM) vs. 12.8×10⁻³ (LSTM) on test data].
- [supported] QLSTM demonstrated earlier prediction of turning points in stock market trends compared to classical LSTM, potentially offering an advantage in foreseeing market movements.
- [supported] qGAN successfully modeled cryptocurrency data (BNBBTC, ETHBTC, etc.) with fewer iterations than classical GANs, achieving equilibrium in generator/discriminator loss functions (~0.6931 at optimal equilibrium).
- [supported] QCBM with SPSA optimization closely approximated target probability distributions for synthetic BAS datasets, outperforming Cobyla and Nelder-Mead optimizers.
- [supported] QLSTM training time was highly dependent on GPU hardware, with NVIDIA CUDA-Q reducing per-epoch training time from 780s (RTX 3070) to 18s (RTX 3070 with CUDA-Q).
- [speculative] Hybrid quantum-classical models (qGAN, QLSTM, QCBM) may deliver quantum advantage in financial applications when combined, particularly for temporal data analysis.
- [speculative] Quantum advantage in financial modeling could emerge with improved hardware (e.g., NVIDIA DGX Quantum stack) and larger-scale implementations.
- [speculative] QCBM’s expressive power may enable efficient representation of distributions intractable for classical models like Random Boltzmann Machines (RBMs).
- [disputed] The claim that QLSTM’s test predictions are 'slightly superior' to LSTM is nuanced; while QLSTM showed better alignment with real data in volatile regions, classical LSTM achieved lower RMSE (12.8×10⁻³ vs. 15.09×10⁻³) and faster training times.

**Results summary:** The paper presents empirical evaluations of three hybrid quantum-classical algorithms (qGAN, QLSTM, QCBM) for financial applications. QLSTM outperformed classical LSTM in test prediction accuracy for NVIDIA stock data, particularly in volatile regions, though with longer training times. qGAN demonstrated efficient modeling of cryptocurrency distributions, while QCBM showed promise in approximating synthetic datasets. All results were obtained via simulation, with hardware dependence (e.g., GPU acceleration) significantly impacting performance. The authors speculate on potential quantum advantage through algorithmic integration and hardware advancements but acknowledge current limitations in scalability and empirical validation.

**Performance claims:**
- QLSTM test RMSE: 15.09×10⁻³ (vs. LSTM’s 12.8×10⁻³)
- QLSTM training RMSE: 19.05×10⁻³ (vs. LSTM’s 7.5×10⁻³)
- QLSTM training time per epoch: 18s (RTX 3070 with CUDA-Q) vs. 780s (RTX 3070 without CUDA-Q)
- LSTM training time per epoch: 0.04s (RTX 3070 with CUDA-Q)
- qGAN generator/discriminator loss equilibrium at ~0.6931 after 2000 epochs
- QCBM with SPSA optimizer achieved close approximation to target probability distributions for BAS datasets
## Quantum advantage claim
**Classification:** speculative

The paper suggests potential quantum advantage through hybrid algorithms (qGAN, QLSTM, QCBM) but provides no empirical demonstration on real hardware. Claims are based on simulation results showing marginal improvements in specific tasks (e.g., QLSTM’s test predictions) or theoretical advantages (e.g., QCBM’s expressive power). The authors acknowledge that quantum advantage remains speculative pending hardware improvements (e.g., NISQ devices with 100+ qubits) and further integration of algorithms.
## Limitations
- Experiments conducted on quantum simulators rather than real quantum hardware, limiting assessment of noise and decoherence effects [inferred]
- Qubit count constraints (e.g., 1-qubit state for qGAN, 4 qubits for QLSTM VQCs) limit practical applicability to larger financial datasets
- QLSTM training time significantly longer than classical LSTM, with strong dependence on GPU hardware (e.g., 1600 sec/epoch on RTX 3060 vs. 0.05 sec/epoch for LSTM)
- Datasets used are limited in scope: cryptocurrency data (5 assets), NVIDIA stock (210 days), and synthetic BAS dataset (2×2 images)
- No comparison with state-of-the-art classical machine learning models beyond basic LSTM [inferred]
- Lack of noise mitigation techniques in quantum circuit implementations may affect real-hardware performance [inferred]
- Page-limit constraints typical of conference papers may have restricted detailed discussion of methodology and results [inferred]
- Statistical significance testing (paired t-test on RMSE) shows marginal differences between QLSTM and LSTM, limiting claims of quantum advantage
- QCBM results rely on synthetic data (BAS dataset) rather than real financial data, reducing practical relevance [inferred]
- Optimizer choice (SPSA vs. Cobyla) for QCBM may introduce bias in performance evaluation [inferred]
## Open questions
- How do hybrid quantum-classical models perform on larger, more complex financial datasets (e.g., multi-asset portfolios with >100 assets)?
- What is the impact of quantum noise and decoherence on QLSTM and qGAN performance in real quantum hardware?
- Can quantum advantage be demonstrated for financial forecasting tasks beyond marginal improvements in test loss?
- How do hybrid models scale with increasing qubit counts and circuit depths?
- What are the optimal quantum data encoding strategies for financial time-series data?
- How do hybrid models compare to advanced classical techniques (e.g., Transformers, XGBoost) for financial prediction?
- What are the computational trade-offs between quantum simulation speedups (e.g., CUDA-Q) and classical hardware?
- Can qGAN, QLSTM, and QCBM be effectively combined into a unified framework for financial modeling?
- What are the implications of quantum randomness for risk management and regulatory compliance in finance?

**Future work:**
- Test hybrid models on real quantum hardware (e.g., IBM Eagle, Rigetti Aspen) to evaluate noise resilience
- Extend QLSTM to multi-asset stock prediction and portfolio optimization tasks
- Combine qGAN, QLSTM, and QCBM into a unified framework for financial time-series analysis
- Explore advanced quantum data encoding techniques (e.g., amplitude encoding) for larger datasets
- Benchmark against state-of-the-art classical models (e.g., Transformers, ensemble methods) for financial forecasting
- Investigate noise mitigation techniques (e.g., error mitigation, dynamical decoupling) for real-hardware implementations
- Apply hybrid models to other financial tasks (e.g., fraud detection, credit risk analysis, algorithmic trading)
- Leverage NVIDIA CUDA-Q and DGX Quantum hardware for faster quantum simulations
- Develop hybrid models for multi-period financial forecasting and scenario analysis
- Explore quantum kernel methods for financial data classification and clustering
## Key ideas
- #idea:hybrid-approach — Hybrid quantum-classical models (QLSTM, qGAN, QCBM) leverage classical optimization to enhance quantum circuit training for financial forecasting and generative tasks
- #idea:quantum-advantage — QLSTM demonstrated marginally better test prediction accuracy than classical LSTM for NVIDIA stock prices, particularly in volatile regions, suggesting potential quantum advantage in time-series forecasting
- #idea:near-term-feasibility — qGAN successfully trained on real-world cryptocurrency data, generating synthetic distributions with convergence at equilibrium, indicating near-term applicability despite hardware limitations
- #idea:hybrid-approach — QUBO optimization post-qGAN training identified the highest-return cryptocurrency (BNBBTC), showcasing hybrid quantum-classical pipelines for asset selection
- #limitation:noise — No noise mitigation techniques were applied, limiting the robustness of results for real NISQ devices
- #limitation:qubit-count — Experiments used limited qubit counts (1-qubit for qGAN, 4-qubits for QLSTM), restricting scalability to larger financial datasets
- #limitation:simulation-only — All quantum results were derived from classical simulations (Qiskit, PennyLane), with no validation on real quantum hardware
## Contradictions
- The paper claims potential quantum advantage for generative models (qGAN, QCBM) and time-series forecasting (QLSTM), but these claims are speculative and lack empirical validation on real hardware. This contradicts prior work (e.g., 2022_Herman_QuantumMonteCarlo) that highlights the impracticality of achieving quantum advantage with current NISQ devices for financial applications due to noise and qubit limitations.
- The QLSTM model showed slightly better test prediction accuracy than classical LSTM in volatile regions, but classical LSTM achieved lower RMSE (12.8×10⁻³ vs. 15.09×10⁻³) and significantly faster training times (0.04s vs. 18s per epoch). This contradicts classical benchmarks (e.g., 2023_Smith_DeepLearningFinance) where classical LSTM remains dominant in production due to lower computational overhead.
- #contradiction:scalability — While QCBMs are theorized to outperform classical RBMs (single-run sampling vs. ~10⁴ iterations), empirical validation is lacking, and scalability to real-world financial data remains unproven, contradicting the paper's speculative claims about quantum advantage.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
