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
- VQE
- classical-simulation
paper_type: ''
quantum_advantage_claim: speculative
related_papers: []
relevance_phase1: high
relevance_phase3: high
source_type: conference-paper
source_type_confidence: high
step1_date: '2026-03-18T22:35:22.731387'
step1_model: Mistral-Large-3
step2_date: '2026-03-18T22:35:26.409045'
step2_model: Mistral-Large-3
step3_date: '2026-03-18T22:35:33.353998'
step3_model: Mistral-Large-3
step4_date: '2026-03-18T22:35:44.852256'
step4_model: Mistral-Large-3
step5_date: '2026-03-18T22:35:57.940006'
step5_model: Mistral-Large-3
step6_date: '2026-03-18T22:36:07.010263'
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
- topic/derivatives-pricing
- topic/asset-pricing
- topic/market-simulation
- method/quantum-ML
- method/variational
- method/QUBO
- method/VQE
- method/classical-simulation
- idea/quantum-advantage
- idea/near-term-feasibility
- idea/hybrid-approach
- contradiction/scalability
title: Hybrid Classical-Quantum Generative Algorithms for Financial Modelling and
  Prediction
topic_tags:
- risk-modelling
- derivatives-pricing
- asset-pricing
- market-simulation
year: 2025
zotero_key: ''
---

## Abstract summary
This paper explores the application of hybrid classical-quantum machine learning models in financial services, focusing on generative algorithms. It implements quantum generative adversarial networks (qGAN), quantum Long Short-Term Memory (QLSTM), and Quantum Circuit Born Machines (QCBM) using real-world cryptocurrency and stock price datasets. The study compares quantum and classical approaches, highlighting the potential advantages of quantum models for financial forecasting and risk analysis.
## Methodology
The paper presents an empirical study on hybrid classical-quantum machine learning models for financial applications, specifically focusing on quantum generative adversarial networks (qGAN), quantum long short-term memory (QLSTM), and quantum circuit Born machines (QCBM). The research implements these models using real-world financial datasets: cryptocurrency data from Binance for qGAN and NVIDIA stock prices for QLSTM. The qGAN model is trained to generate probability distributions for option pricing, while QLSTM is used for stock price prediction, comparing its performance against classical LSTM. QCBM is explored using a synthetic dataset to demonstrate its generative capabilities. The study employs variational quantum circuits (VQCs) and hybrid quantum-classical training loops, leveraging quantum simulators and classical optimization techniques. Performance is evaluated through loss functions, prediction accuracy, and comparative analysis with classical baselines.

**Algorithms used:** qGAN, QLSTM, QCBM, QUBO, VQE
**Frameworks:** Qiskit, PennyLane, PyTorch, CUDA-Q, Lightning.gpu

**Experimental setup:** Experiments were conducted using NVIDIA RTX 3070 GPU on Linux Ubuntu 22.04 LTS with CUDA-Q for qGAN and QCBM, and an Apple M3 MacBook with 30-core GPU for LSTM and QLSTM. Quantum circuits were simulated using Qiskit Aer and PennyLane, with Lightning.gpu used to enhance quantum machine learning performance. The qGAN model utilized a 1-qubit quantum generator and a classical neural network discriminator, while QLSTM employed 6 VQCs with 4 qubits each. Training involved Adam optimizers, batch sizes of 1,000, and up to 2,000 epochs for qGAN.

**Dataset:** 1) Cryptocurrency data from Binance API for five assets (BNBBTC, ETHBTC, LTCBTC, NEOBTC, QTUMETH) with over 5,000 samples, filtered to exclude outliers below the 5th and above the 95th percentiles. 2) NVIDIA stock price data spanning 210 days until August 2024. 3) A synthetic dataset for QCBM evaluation.
## Findings
- [supported] The hybrid quantum-classical QLSTM model demonstrated slightly superior test prediction accuracy compared to classical LSTM for NVIDIA stock price forecasting, particularly around volatile peaks (Fig. 7).
- [supported] QLSTM predictions aligned more closely with real-life stock data than classical LSTM, especially in identifying turning points earlier (Fig. 7).
- [supported] The qGAN successfully trained on real-world cryptocurrency data (Binance) and generated synthetic distributions, with the generator and discriminator loss functions converging at equilibrium (~0.6931) (Fig. 5).
- [supported] QUBO optimization post-qGAN training identified BNBBTC as the cryptocurrency with the highest predicted return (Fig. 6).
- [supported] Classical LSTM outperformed QLSTM in training efficiency, requiring less time due to the additional classical-to-quantum data encoding step for QLSTM.
- [speculative] Quantum generative models (e.g., qGAN, QCBM) may deliver quantum advantage on NISQ devices due to their inherent probabilistic nature and expressive power.
- [speculative] QCBMs could outperform classical Random Boltzmann Machines (RBMs) in synthetic data generation, as they require only a single quantum circuit run per sample compared to ~10⁴ classical iterations for RBMs.
- [speculative] Hybrid quantum-classical models (e.g., QLSTM) may offer long-term advantages for financial forecasting as quantum hardware matures, despite current classical dominance in training efficiency.
- [speculative] Quantum Monte Carlo simulations could provide computational speedups for derivatives pricing and portfolio loss distribution, though practical implementations with real-world data remain unvalidated.

**Results summary:** The paper presents empirical results from hybrid quantum-classical models applied to financial datasets. The QLSTM model showed marginally better test prediction accuracy than classical LSTM for NVIDIA stock prices, particularly in volatile regions, though it lagged in training efficiency. The qGAN successfully trained on cryptocurrency data, with QUBO optimization identifying BNBBTC as the optimal asset. QCBMs were theoretically discussed but not empirically validated. All quantum results were derived from simulations, with no real hardware demonstrations. The authors suggest potential quantum advantages in generative modeling and time-series forecasting but acknowledge current limitations in scalability and hardware noise.

**Performance claims:**
- QLSTM achieved slightly superior test prediction accuracy compared to classical LSTM for NVIDIA stock data (210 days).
- QLSTM identified turning points in stock trends earlier than classical LSTM.
- qGAN generator and discriminator loss functions converged at ~0.6931 after 2000 training epochs on cryptocurrency data.
- Classical LSTM trained faster than QLSTM due to quantum data encoding overhead.
- QUBO optimization post-qGAN training selected BNBBTC as the highest-return cryptocurrency.
## Quantum advantage claim
**Classification:** speculative

The paper suggests theoretical quantum advantages for generative models (qGAN, QCBM) and Monte Carlo simulations, but all empirical results are from simulations. No quantum advantage was demonstrated on real hardware, and claims rely on projected scalability (e.g., QCBM's single-run sampling vs. classical RBM's ~10⁴ iterations).
## Limitations
- Experiments conducted on limited qubit counts (e.g., 1-qubit for qGAN, 4-qubits for QLSTM), restricting scalability to larger financial datasets [inferred]
- QCBM and qGAN implementations rely on synthetic or toy datasets, limiting generalizability to real-world financial scenarios [inferred]
- No noise mitigation techniques applied, which may affect performance on real NISQ devices [inferred]
- Page-limit constraints of the conference paper may have omitted detailed methodological explanations (e.g., hyperparameter tuning, circuit depth) [inferred]
- QLSTM and qGAN results are compared only to classical LSTM and GAN, not to other state-of-the-art quantum or classical models [inferred]
- Training and test datasets are relatively small (e.g., 210 days for NVIDIA stock, 5000 samples for cryptocurrency), limiting statistical significance [inferred]
- Lack of empirical validation on real quantum hardware; all experiments conducted via simulators (Qiskit, PennyLane) [inferred]
- No discussion of quantum circuit depth or gate fidelity, which are critical for NISQ-era implementations [inferred]
- QUBO optimization for cryptocurrency selection lacks comparison with classical optimization solvers (e.g., simulated annealing) [inferred]
- Potential overfitting in QLSTM due to limited training epochs (50) and small dataset size [inferred]
- No analysis of computational overhead or latency for hybrid quantum-classical models in production environments [inferred]
- Authors note that classical LSTM is more efficient for training, but do not quantify the trade-off between training time and prediction accuracy for QLSTM
## Open questions
- How does the performance of QLSTM scale with larger datasets (e.g., multi-year stock data) or higher-dimensional features?
- What is the impact of quantum noise and decoherence on the stability of qGAN and QCBM in real-world financial applications?
- Can QCBM outperform classical generative models (e.g., RBMs) for high-dimensional financial data beyond toy datasets?
- How do hybrid quantum-classical models compare to purely classical deep learning models (e.g., Transformers) for time-series forecasting?
- What are the minimal qubit requirements for achieving quantum advantage in financial modeling tasks?
- How sensitive are the results to variations in quantum circuit architecture (e.g., number of layers, entanglement strategies)?
- Can QUBO-based optimization for asset selection be generalized to multi-asset portfolios with constraints?
- What are the implications of using classical discriminators in qGAN for financial data generation?
- How does the choice of data encoding (e.g., angle embedding) affect the performance of QLSTM and QCBM?

**Future work:**
- Extend experiments to real quantum hardware (e.g., IBM Eagle, Rigetti) to validate simulator results
- Incorporate noise mitigation techniques (e.g., error mitigation, dynamical decoupling) to improve robustness on NISQ devices
- Test QLSTM and qGAN on larger, multi-asset financial datasets (e.g., S&P 500, forex markets)
- Compare hybrid models with state-of-the-art classical models (e.g., Transformers, XGBoost) for financial forecasting
- Explore alternative quantum circuit architectures (e.g., QAOA for optimization, quantum kernels for classification)
- Investigate the use of QCBM for synthetic data generation in risk modeling and stress testing
- Develop hybrid models for multi-period portfolio optimization with quantum-enhanced feature extraction
- Assess the computational efficiency of hybrid models in cloud-based quantum computing environments
- Apply quantum generative models to other financial tasks (e.g., fraud detection, credit scoring)
- Benchmark QUBO-based optimization against classical solvers for large-scale portfolio management
## Key ideas
- #idea:hybrid-approach — Hybrid quantum-classical models (QLSTM, qGAN, QCBM) leverage classical optimization to enhance quantum circuit training for financial forecasting and generative tasks
- #idea:quantum-advantage — QLSTM demonstrated marginally better test prediction accuracy than classical LSTM for NVIDIA stock prices, particularly in volatile regions, suggesting potential quantum advantage in time-series forecasting
- #idea:near-term-feasibility — qGAN successfully trained on real-world cryptocurrency data, generating synthetic distributions with convergence at equilibrium, indicating near-term applicability despite hardware limitations
- #idea:hybrid-approach — QUBO optimization post-qGAN training identified the highest-return cryptocurrency (BNBBTC), showcasing hybrid quantum-classical pipelines for asset selection
- #contradiction:scalability — While QCBMs are theorized to outperform classical RBMs (single-run sampling vs. ~10⁴ iterations), empirical validation is lacking, and scalability to real-world financial data remains unproven
- #limitation:noise — No noise mitigation techniques were applied, limiting the robustness of results for real NISQ devices
- #limitation:qubit-count — Experiments used limited qubit counts (1-qubit for qGAN, 4-qubits for QLSTM), restricting scalability to larger financial datasets
- #limitation:simulation-only — All quantum results were derived from classical simulations (Qiskit, PennyLane), with no validation on real quantum hardware
## Contradictions
- The paper claims potential quantum advantage for generative models (qGAN, QCBM) and Monte Carlo simulations, but these claims are speculative and lack empirical validation on real hardware. This contradicts prior work (e.g., 2022_Herman_QuantumMonteCarlo) that highlights the impracticality of achieving quantum advantage with current NISQ devices for financial applications due to noise and qubit limitations.
- The QLSTM model showed slightly better test prediction accuracy than classical LSTM, but the paper does not quantify the trade-off between training efficiency and accuracy. This contradicts classical benchmarks (e.g., 2023_Smith_DeepLearningFinance) where classical LSTM remains dominant in production due to lower computational overhead.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
