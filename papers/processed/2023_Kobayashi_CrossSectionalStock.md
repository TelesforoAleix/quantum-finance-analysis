---
aliases:
- The cross-sectional stock return predictions via quantum neural network and tensor
  network
- cross sectional stock return
authors:
- Nozomu Kobayashi
- Yoshiyuki Suimon
- Koichi Miyamoto
- Kosuke Mitarai
auto_detected: true
classification: ''
contradiction_flags: []
doi: 10.48550/arXiv.2304.12501
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
relevance_phase1: high
relevance_phase3: medium
source_type: preprint
source_type_confidence: high
step1_date: '2026-03-19T23:32:37.984207'
step1_model: Mistral-Large-3
step2_date: '2026-03-19T23:32:40.846948'
step2_model: Mistral-Large-3
step3_date: '2026-03-19T23:32:51.629798'
step3_model: Mistral-Large-3
step4_date: '2026-03-19T23:32:56.795079'
step4_model: Mistral-Large-3
step5_date: '2026-03-19T23:33:02.256686'
step5_model: Mistral-Large-3
step6_date: '2026-03-19T23:33:06.350797'
step6_model: Mistral-Large-3
steps_completed:
- 1
- 2
- 3
- 4
- 5
- 6
tags:
- topic/portfolio-optimisation
- topic/asset-pricing
- method/quantum-ML
- method/variational
- method/classical-simulation
- idea/near-term-feasibility
- idea/hybrid-approach
- idea/quantum-advantage
title: The cross-sectional stock return predictions via quantum neural network and
  tensor network
topic_tags:
- portfolio-optimisation
- asset-pricing
year: 2024
zotero_key: ''
---

## Abstract summary
This preprint explores the application of quantum and quantum-inspired machine learning algorithms for predicting stock returns in financial markets. The authors compare quantum neural networks and tensor networks against classical models like linear regression and neural networks, focusing on their performance in portfolio construction and investment returns. The study demonstrates that tensor networks outperform classical benchmarks, while quantum neural networks show potential in capturing non-linear relationships in recent market conditions.
## Methodology
The paper presents an empirical study comparing quantum and quantum-inspired machine learning algorithms for stock return predictions in the Japanese stock market. The authors evaluate a quantum neural network (specifically quantum circuit learning) and a tensor network model against classical benchmarks, including linear regression and neural networks. The methodology involves constructing portfolios based on predicted returns and measuring investment performance through backtesting over a 10-year period (June 2008 to May 2021). The study employs a cross-sectional approach, where stock returns are predicted using firm-specific features. The models are trained on three-year historical data and tested on the subsequent one-year data, with this process rolled forward monthly. Performance metrics such as annualized excess return, tracking error, and information ratio are used to evaluate the models.

**Algorithms used:** Quantum Circuit Learning, Tensor Network (Matrix Product State), Linear Regression, Neural Network
**Frameworks:** Qulacs, TensorFlow, TensorNetwork

**Experimental setup:** The experiments were conducted using quantum circuit simulators and classical computational frameworks. The quantum circuit learning model was implemented using the Qulacs simulator in a noiseless setting. TensorFlow was used for implementing neural networks and the optimization procedure for all models. The tensor network model was implemented using the TensorNetwork library alongside TensorFlow.

**Dataset:** Japanese stocks that are constituents of the TOPIX500 index. The dataset includes 10 features such as Book-Value to Price Ratio, Earning to Price Ratio, Return on Equity, Momentum (1-month, 3-month, 6-month, 12-month), Market Capitalization, and Beta.
## Findings
- [supported] The tensor network (TN) model achieves superior performance in stock return prediction compared to classical benchmark models (linear regression and neural networks) in the Japanese stock market, with an annualized excess return (ER) of 3.71% and an information ratio (IR) of 0.69
- [supported] The quantum neural network (QCL) model attains a lower risk-adjusted excess return than classical neural network models over the entire backtesting period (June 2008 - May 2021), with an ER of 1.35% and IR of 0.22
- [supported] Both QCL and TN models outperform classical models in the latest market environment (post-2016), suggesting their ability to capture non-linearity between input features (ER of 2.63% for QCL and 4.20% for TN from 2016 onward)
- [speculative] Quantum neural networks may have better control over the overfitting problem compared to classical neural networks, as implied by their sustained performance in recent market environments
- [speculative] The superior performance of the TN model, despite having fewer parameters, suggests it may have effective architectures for learning financial data, though further investigation is needed for larger feature sets
- [speculative] Quantum machine learning techniques could be applicable to other asset classes (e.g., bonds, currencies) or markets (e.g., U.S., global) beyond the Japanese stock market
- [speculative] Quantum recurrent neural networks could be explored for time-series stock return prediction, building on classical recurrent neural network approaches

**Results summary:** The paper evaluates quantum and quantum-inspired machine learning algorithms (quantum neural network/QCL and tensor network/TN) for cross-sectional stock return prediction in the Japanese stock market. Through a 10-year backtesting period, the TN model demonstrates superior performance over classical models (linear regression and neural networks), achieving the highest annualized excess return (3.71%) and information ratio (0.69). The QCL model shows competitive but riskier performance compared to neural networks, with notable outperformance in recent market conditions (post-2016). Both quantum models appear to capture non-linear relationships between features, with potential advantages in mitigating overfitting. Results are based on simulations, not real quantum hardware.

**Performance claims:**
- Tensor network (TN) model: ER = 3.71%, TE = 5.41%, IR = 0.69 (best performance)
- Quantum neural network (QCL) model: ER = 1.35%, TE = 6.18%, IR = 0.22
- Neural network (NN2) model: ER = 1.76%, TE = 4.28%, IR = 0.41
- Linear regression model: ER = -0.28%, TE = 6.64%, IR = -0.04
- Post-2016 performance: QCL ER = 2.63%, TN ER = 4.20% (outperforming classical models)
## Quantum advantage claim
**Classification:** speculative

The paper suggests potential quantum advantage in capturing non-linear relationships and mitigating overfitting, but all results are from simulations (no real hardware). Claims of superiority are based on empirical backtesting rather than theoretical complexity advantages, and no direct quantum speedup is demonstrated.
## Limitations
- Experiments conducted using a quantum circuit simulator (Qulacs) in a noiseless setting, not on real quantum hardware [inferred]
- Quantum circuit learning (QCL) limited to 10 qubits due to computational intensity of simulations
- Small number of features (10) used in models, which is fewer than typical machine learning models for stock return predictions (tens to hundreds of features)
- Backtesting limited to the Japanese stock market (TOPIX500), with no evaluation in other markets (e.g., U.S. or global markets)
- No noise mitigation techniques applied, which may affect performance on real NISQ devices [inferred]
- Quantum circuit learning model (QCL) shows higher tracking error (TE) compared to classical models, resulting in inferior risk-adjusted returns
- Lack of peer review as the paper is a preprint [inferred]
- No comparison with state-of-the-art classical machine learning models beyond linear regression and basic neural networks [inferred]
- Optimization of tensor network models used gradient descent instead of the more sophisticated density matrix renormalization group (DMRG) approach
- Limited exploration of different quantum circuit architectures for QCL, which may impact performance [inferred]
- Dataset not publicly available due to licensing agreements, limiting reproducibility [inferred]
- Backtesting re-estimates models only once a year to avoid computational intensity, which may not capture shorter-term market dynamics [inferred]
## Open questions
- Can quantum models (QCL and tensor networks) perform well in markets outside Japan, such as the U.S. or global markets?
- How would the models perform with a larger number of features (e.g., tens or hundreds) commonly used in classical machine learning for stock return predictions?
- What is the impact of noise and decoherence on the performance of QCL when run on real quantum hardware?
- Would the use of DMRG for tensor network optimization improve performance compared to gradient descent?
- Can quantum models effectively handle the overfitting problem better than classical models in unstable market environments?
- How would quantum recurrent neural networks perform in time-series stock return predictions compared to classical recurrent networks?
- Is transfer learning effective for quantum models in financial applications, similar to classical models?
- Can quantum machine learning models be applied to other asset classes, such as bonds or currencies?
- What is the scalability of QCL and tensor network models when increasing the number of qubits or bond dimensions?

**Future work:**
- Test quantum models on real quantum hardware to evaluate performance under noise and decoherence
- Extend the analysis to other markets (e.g., U.S. or global markets) to assess generalizability
- Increase the number of features in models to evaluate scalability and performance with more complex datasets
- Explore different quantum circuit architectures for QCL to optimize performance
- Apply density matrix renormalization group (DMRG) for tensor network optimization and compare with gradient descent
- Investigate the use of quantum recurrent neural networks for time-series stock return predictions
- Study transfer learning in quantum models for financial applications across different markets
- Apply quantum machine learning models to other asset classes, such as bonds or currencies
- Evaluate the performance of quantum models in multi-period portfolio optimization
- Compare quantum models with state-of-the-art classical machine learning models for stock return predictions
## Key ideas
- #idea:near-term-feasibility — Tensor network models outperform classical benchmarks (linear regression, neural networks) in stock return prediction, demonstrating potential for near-term applicability in financial markets
- #idea:hybrid-approach — Quantum neural networks and tensor networks are simulated classically, suggesting a hybrid quantum-classical approach is necessary for practical deployment given current hardware limitations
- #idea:quantum-advantage — Quantum neural networks show superior performance in recent market environments (2016-2021), hinting at potential advantages in capturing non-linearity and mitigating overfitting (though claims remain speculative)
- #limitation:simulation-only — Quantum advantage claims are unvalidated due to reliance on classical simulations (Qulacs) rather than real quantum hardware
- #limitation:qubit-count — Quantum circuit learning model is limited to 10 qubits, restricting feature dimensions and scalability for real-world financial applications
- #limitation:noise — Noiseless simulation does not account for hardware noise, which could degrade performance on real quantum devices
- #limitation:data-encoding — Limited exploration of feature scaling or encoding methods for quantum models, which may impact expressibility
## Contradictions
<!-- Step 6 output — where this paper contradicts others -->

## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->

## Experiment details
### Input
{'source': 'TOPIX500 index constituents, Japanese stock market', 'size': 'Stocks available monthly from June 2008 to May 2021', 'number_of_features': 10, 'preprocessing_steps': 'All features and returns were cross-sectionally ranked at each time step. Features were normalized to the range [−1, 1] for quantum circuit learning.', 'time_period': 'June 2008 to May 2021'}

### Process
1. Data preprocessing: Features and returns were cross-sectionally ranked and normalized. 2. Model training: Models were trained on three-year historical data using stochastic gradient descent with Adam optimizer for 20 epochs. 3. Prediction: One-month future returns were predicted using the trained models. 4. Portfolio construction: Stocks were sorted based on predicted returns, and the top quintile stocks were selected for equal-weight long positions. 5. Backtesting: The process was rolled forward monthly, re-estimating models annually to avoid computational intensity. 6. Performance evaluation: Metrics such as annualized excess return, tracking error, and information ratio were computed.

### Output
Portfolio performance metrics including annualized excess return (ER), tracking error (TE), and information ratio (IR). The results were compared against benchmarks such as the TOPIX500 index and classical models (linear regression and neural networks).

### Parameters
- quantum_circuit_learning: {'qubits': 10, 'circuit_depth': 3, 'optimizer': 'Adam', 'epochs': 20, 'parameter_count': 90}
- tensor_network: {'bond_dimension': 2, 'parameter_count': 76, 'optimizer': 'Adam', 'epochs': 20}
- neural_networks: {'NN1_layers': [10, 7, 1], 'NN2_layers': [10, 5, 4, 1], 'activation_function': 'ReLU', 'optimizer': 'Adam', 'epochs': 20, 'parameter_count_NN1': 92, 'parameter_count_NN2': 93}

### Hardware
Quantum circuit learning experiments were conducted using the Qulacs quantum circuit simulator in a noiseless setting. Classical computations were performed on standard computational hardware using TensorFlow and TensorNetwork libraries.

### Reproducibility
The paper provides detailed descriptions of the models and experimental setup, but the dataset is not publicly available due to licensing agreements. The code for the quantum circuit learning model (Qulacs) and tensor network (TensorNetwork) implementations is not explicitly mentioned as available, which may limit reproducibility.
