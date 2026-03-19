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
step1_date: '2026-03-19T12:36:24.689538'
step1_model: Mistral-Large-3
step2_date: '2026-03-19T12:36:28.676321'
step2_model: Mistral-Large-3
step3_date: '2026-03-19T12:37:20.486908'
step3_model: Mistral-Large-3
step4_date: '2026-03-19T12:37:33.271201'
step4_model: Mistral-Large-3
step5_date: '2026-03-19T12:37:51.047167'
step5_model: Mistral-Large-3
step6_date: '2026-03-19T12:39:28.674670'
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
title: The cross-sectional stock return predictions via quantum neural network and
  tensor network
topic_tags:
- portfolio-optimisation
- asset-pricing
year: 2024
zotero_key: ''
---

## Abstract summary
This preprint explores the application of quantum and quantum-inspired machine learning algorithms for predicting stock returns in financial markets. The authors compare the performance of quantum neural networks and tensor networks against classical models like linear regression and neural networks, using portfolio construction and backtesting on Japanese stock market data. The study aims to assess whether quantum techniques can capture non-linear relationships in financial data and outperform traditional methods in real-world investment scenarios.
## Methodology
The paper investigates the application of quantum and quantum-inspired machine learning algorithms for stock return predictions in the Japanese stock market. The study employs a cross-sectional approach to predict one-month future stock returns using quantum neural network (quantum circuit learning) and tensor network models, comparing their performance against classical models such as linear regression and neural networks. The methodology involves constructing portfolios based on predicted returns and conducting backtesting over a 10-year period (June 2008 to May 2021) to evaluate investment performance. The dataset consists of constituents of the TOPIX500 index, with 10 financial features used as input variables. The models are trained using a three-year rolling window and tested on the subsequent one-year period, with performance metrics including annualized excess return, tracking error, and information ratio.

**Algorithms used:** Quantum Circuit Learning, Tensor Network, Linear Regression, Neural Network
**Frameworks:** Qulacs, TensorFlow, TensorNetwork

**Experimental setup:** The experiments were conducted using quantum circuit simulators (Qulacs) in a noiseless setting. The quantum circuit learning model utilized 10 qubits corresponding to the 10 input features, with a parameterized quantum circuit depth of 3. The tensor network model employed a matrix product state (MPS) with a bond dimension of 2. Classical models (neural networks) were implemented using TensorFlow. The optimization for all models was performed using the stochastic gradient descent technique with the Adam optimizer over 20 epochs.

**Dataset:** The dataset comprises constituents of the TOPIX500 index (Japanese stocks) with 10 financial features, including value factors (e.g., Book-Value to Price Ratio), quality factors (e.g., Return on Equity), momentum factors (e.g., 1-month to 12-month returns), size (Market Capitalization), and market beta. Features and returns were cross-sectionally ranked at each time step as preprocessing. The backtesting period spanned from June 2008 to May 2021.
## Findings
- [supported] The tensor network (TN) model achieves superior performance in stock return prediction compared to classical benchmark models (linear regression and neural networks) in the Japanese stock market, with an annualized excess return (ER) of 3.71% and an information ratio (IR) of 0.69
- [supported] The quantum neural network (QCL) model shows lower risk-adjusted excess return than classical neural network models over the entire backtesting period (2008-2021), but outperforms them in the latest market environment (2016-2021), suggesting better adaptability to non-linearity and reduced overfitting
- [supported] The tensor network model outperforms all other models even with the lowest number of parameters, indicating potential for effective learning of financial data structures
- [speculative] Quantum neural network and tensor network models may capture non-linear and interaction effects among features, offering potential advantages over conventional models in return predictions
- [speculative] Quantum techniques could provide better control of the overfitting problem compared to classical neural networks
- [speculative] The observed performance differences between quantum and classical models in recent market environments may be linked to market instability and model adaptability

**Results summary:** The paper evaluates quantum and quantum-inspired machine learning algorithms (quantum neural network and tensor network) against classical models (linear regression and neural networks) for stock return prediction in the Japanese stock market. The tensor network model demonstrates the best overall performance, achieving the highest annualized excess return (3.71%) and information ratio (0.69). The quantum neural network model, while underperforming classical neural networks over the full backtesting period, shows superior performance in the latest market environment (2016-2021), suggesting potential advantages in capturing non-linearity and mitigating overfitting. All results are derived from simulations, not real quantum hardware, and are based on a 10-year backtesting period with monthly investment decisions.

**Performance claims:**
- Tensor network model: ER = 3.71%, TE = 5.41%, IR = 0.69 (full period); ER = 4.20%, TE = 5.14%, IR = 0.82 (2016 onward)
- Quantum neural network model: ER = 1.35%, TE = 6.18%, IR = 0.22 (full period); ER = 2.63%, TE = 5.85%, IR = 0.45 (2016 onward)
- Neural network models: ER = 1.27%-1.76%, TE = 3.79%-4.28%, IR = 0.34-0.41 (full period); ER = 0.18%-0.56%, TE = 3.48%-4.31%, IR = 0.04-0.16 (2016 onward)
- Linear regression model: ER = -0.28%, TE = 6.64%, IR = -0.04 (full period); ER = -0.12%, TE = 7.82%, IR = -0.02 (2016 onward)
## Quantum advantage claim
**Classification:** speculative

The claimed advantages of quantum and quantum-inspired models (e.g., non-linearity capture, overfitting control) are based on simulation results only. No empirical validation on real quantum hardware is provided, and the observed performance improvements in recent market environments are not conclusively attributed to quantum properties.
## Limitations
- Experiments conducted on a quantum circuit simulator (Qulacs) in a noiseless setting, which does not account for hardware noise or decoherence effects [inferred]
- Quantum neural network (QCL) limited to 10 qubits due to computational intensity of simulating quantum circuits, restricting the number of input features
- Small number of features (10) used compared to typical machine learning models for stock return predictions, which may limit expressibility and accuracy [inferred]
- Backtesting experiment limited to the Japanese stock market (TOPIX500), with no evaluation in other markets (e.g., U.S. or global markets) [inferred]
- Lack of peer review as the paper is a preprint
- Quantum circuit learning model (QCL) shows higher tracking error (TE) compared to classical models, resulting in inferior risk-adjusted return (IR)
- No comparison with state-of-the-art classical machine learning models beyond linear regression and basic neural networks [inferred]
- Optimization of tensor network models performed using gradient descent instead of the more sophisticated density matrix renormalization group (DMRG) method, which may affect performance [inferred]
- Data not publicly available due to licensing agreements, limiting reproducibility and independent validation [inferred]
- No noise mitigation techniques applied, which may be necessary for real quantum hardware deployment [inferred]
- Limited exploration of different quantum circuit architectures for QCL, which may impact performance [inferred]
## Open questions
- Whether the superior performance of tensor network models holds when increasing the number of features and parameters
- How quantum models perform in other markets (e.g., U.S. or global markets) beyond the Japanese stock market
- Whether quantum machine learning can be applied to other asset classes (e.g., bonds or currencies)
- Whether quantum techniques can effectively control the overfitting problem compared to classical models
- How transfer learning in quantum models compares to classical models for cross-market investment strategies
- The impact of using different quantum circuit architectures on the performance of quantum neural networks
- Whether the use of DMRG for tensor network optimization would yield better performance than gradient descent
- How quantum recurrent neural networks perform in time-series financial predictions compared to classical recurrent networks

**Future work:**
- Examine the applicability of quantum and quantum-inspired models in other countries' stock markets (e.g., U.S.) or global markets
- Apply quantum machine learning to other asset classes such as bonds or currencies
- Explore the use of quantum recurrent neural networks for time-series return predictions
- Investigate the effectiveness of transfer learning in quantum models for cross-market investment strategies
- Test the performance of quantum models with a larger number of features and parameters
- Evaluate the impact of different quantum circuit architectures on the performance of quantum neural networks
- Compare the performance of tensor network models optimized using DMRG versus gradient descent
- Conduct experiments on real quantum hardware to assess the impact of noise and decoherence on model performance
- Explore the potential of quantum models to mitigate overfitting in financial predictions
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
