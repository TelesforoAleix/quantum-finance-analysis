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
step1_date: '2026-03-18T23:33:16.888417'
step1_model: Mistral-Large-3
step2_date: '2026-03-18T23:33:21.186811'
step2_model: Mistral-Large-3
step3_date: '2026-03-18T23:33:28.240030'
step3_model: Mistral-Large-3
step4_date: '2026-03-18T23:33:37.254482'
step4_model: Mistral-Large-3
step5_date: '2026-03-18T23:33:46.777654'
step5_model: Mistral-Large-3
step6_date: '2026-03-18T23:34:14.017803'
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
- method/quantum-ML
- method/variational
- method/classical-simulation
- idea/near-term-feasibility
- idea/hybrid-approach
title: The cross-sectional stock return predictions via quantum neural network and
  tensor network
topic_tags:
- asset-pricing
- portfolio-optimisation
year: 2024
zotero_key: ''
---

## Abstract summary
This paper explores the application of quantum and quantum-inspired machine learning algorithms for predicting cross-sectional stock returns in financial markets. The authors compare the performance of quantum neural networks and tensor networks—both designed to handle complex, non-linear relationships—against classical models like linear regression and neural networks. Through empirical analysis on Japanese stock market data, the study assesses the investment performance of portfolios constructed from these predictions, highlighting the potential advantages of quantum-inspired approaches in capturing feature interactions and improving predictive accuracy.
## Methodology
The paper investigates the application of quantum and quantum-inspired machine learning algorithms for stock return predictions in the Japanese stock market. The authors evaluate the performance of a quantum neural network (quantum circuit learning) and a tensor network model against classical models such as linear regression and neural networks. The study employs a cross-sectional approach for stock return prediction, using firm-specific features like value, quality, momentum, size, and market factors. The models are trained on three years of historical data and tested on the subsequent year, with this process rolled forward over a 10-year backtesting period (2008-2021). Portfolio performance is measured using metrics such as annualized excess return (ER), tracking error (TE), and information ratio (IR). The quantum circuit learning model uses a parameterized quantum circuit with 10 qubits and a depth of 3, while the tensor network model employs a matrix product state (MPS) with a bond dimension of 2. Both quantum models are implemented and simulated using classical frameworks due to current computational limitations of quantum hardware.

**Algorithms used:** Quantum Circuit Learning, Tensor Network (Matrix Product State)
**Frameworks:** Qulacs, TensorFlow, TensorNetwork

**Experimental setup:** The experiments were conducted using classical simulators for quantum circuits and tensor networks. Specifically, the quantum circuit learning model was simulated using the Qulacs quantum circuit simulator in a noiseless setting with 10 qubits. The tensor network model was implemented using the TensorNetwork library alongside TensorFlow. The neural network models were also implemented using TensorFlow. The optimization for all models was performed using the Adam optimizer with 20 epochs. The quantum circuit learning model used the parameter-shift rule for gradient calculation.

**Dataset:** The dataset consists of Japanese stocks that are constituents of the TOPIX500 index. The input features include 10 financial factors: Book-Value to Price Ratio, Earning to Price Ratio, Sales to Price Ratio, Return on Equity, Momentum (1-month, 3-month, 6-month, 12-month), Market Capitalization, and Beta. The data spans from June 2008 to May 2021, with a monthly frequency for investment decisions.
## Findings
- [supported] The tensor network (TN) model achieves superior performance in stock return prediction compared to classical benchmark models (linear regression and neural networks) in the Japanese stock market, with an annualized excess return (ER) of 3.71% and an information ratio (IR) of 0.69
- [supported] The quantum neural network (QCL) model attains a lower risk-adjusted excess return than classical neural network models over the entire backtesting period (2008-2021), with an ER of 1.35% and an IR of 0.22
- [supported] Both QCL and TN models outperform classical models in the latest market environment (post-2016), suggesting their ability to capture non-linearity between input features
- [speculative] Quantum neural networks may have better control over the overfitting problem compared to classical neural networks
- [speculative] The superior performance of TN and QCL models could scale to other markets (e.g., U.S. or global markets) or asset classes (e.g., bonds or currencies)
- [speculative] Quantum machine learning techniques could be applied to time-series stock return prediction using quantum recurrent neural networks

**Results summary:** The paper evaluates quantum and quantum-inspired machine learning algorithms (quantum neural network/QCL and tensor network/TN) for cross-sectional stock return prediction in the Japanese stock market. The tensor network model outperforms all classical benchmarks, including linear regression and neural networks, in both excess return and risk-adjusted performance. The quantum neural network model shows competitive but riskier performance compared to classical neural networks over the full backtesting period (2008-2021) but outperforms them in the latest market environment (post-2016). The results suggest that quantum and quantum-inspired models can capture non-linear relationships in financial data, though the quantum advantage remains speculative due to simulation-based results and limited feature dimensions.

**Performance claims:**
- Tensor network (TN) model: ER = 3.71%, TE = 5.41%, IR = 0.69 (best performance)
- Quantum neural network (QCL) model: ER = 1.35%, TE = 6.18%, IR = 0.22
- Neural network (NN2) model: ER = 1.76%, TE = 4.28%, IR = 0.41
- Linear regression model: ER = -0.28%, TE = 6.64%, IR = -0.04
- Post-2016 performance: QCL ER = 2.63%, TN ER = 4.20%
## Quantum advantage claim
**Classification:** speculative

The claimed advantage of quantum and quantum-inspired models is based on simulation results only, with no demonstration on real quantum hardware. The superior performance of TN and QCL in capturing non-linearity is suggestive but not conclusive of quantum advantage, as the study is limited to 10 features and a specific market context.
## Limitations
- Experiments conducted using a quantum circuit simulator in a noiseless setting, which does not account for hardware noise and decoherence effects on real quantum devices [inferred]
- Quantum circuit learning (QCL) model limited to 10 qubits due to computational intensity of simulations, restricting the number of input features and scalability
- Backtesting performed only on the Japanese stock market (TOPIX500), limiting generalizability to other markets or asset classes [inferred]
- Dataset size constrained by computational resources, with only 10 features used compared to typical machine learning models that employ tens to hundreds of features
- Lack of peer review as the paper is a preprint, which may affect the robustness and validity of the findings [inferred]
- Quantum circuit learning model shows higher tracking error (TE) compared to classical neural networks, indicating higher risk in predictions
- No comparison with state-of-the-art classical machine learning models beyond linear regression and basic neural networks [inferred]
- Optimization of tensor network models performed using gradient descent instead of the more sophisticated density matrix renormalization group (DMRG) method, which may limit performance [inferred]
- Investment strategy re-estimates models only once a year to avoid computationally intensive updates, which may not capture market dynamics effectively [inferred]
- No noise mitigation techniques applied, which could be critical for real-world quantum hardware deployment [inferred]
## Open questions
- How would the quantum neural network and tensor network models perform in other markets (e.g., U.S. or global markets) or with different asset classes (e.g., bonds or currencies)?
- Can quantum machine learning models effectively address the overfitting problem better than classical models, as speculated in the paper?
- What is the impact of using more sophisticated optimization techniques (e.g., DMRG) on the performance of tensor network models?
- How would the models perform with a larger number of features and parameters, especially in the context of quantum circuit learning?
- Is transfer learning effective for quantum machine learning models in financial predictions across different markets?
- What is the performance of quantum recurrent neural networks in time-series stock return predictions?
- How do quantum models compare with advanced classical models (e.g., recurrent neural networks or ensemble methods) in terms of prediction accuracy and risk-adjusted returns?

**Future work:**
- Extend the analysis to other markets (e.g., U.S. or global markets) and asset classes (e.g., bonds or currencies)
- Investigate the performance of quantum models with a larger number of features and parameters
- Apply noise mitigation techniques and test the models on real quantum hardware to evaluate practical applicability
- Explore the use of more sophisticated optimization techniques (e.g., DMRG) for tensor network models
- Compare quantum models with advanced classical machine learning models (e.g., recurrent neural networks or ensemble methods)
- Study the effectiveness of transfer learning for quantum machine learning models in financial predictions
- Develop and test quantum recurrent neural networks for time-series stock return predictions
- Examine the overfitting problem in quantum models and their adaptability to changing market environments
## Key ideas
- #idea:near-term-feasibility — Quantum-inspired tensor networks outperform classical models in stock return prediction, demonstrating potential for near-term applicability in financial markets
- #idea:hybrid-approach — Quantum neural networks and tensor networks are simulated classically, suggesting a hybrid approach for practical deployment given current hardware limitations
- #limitation:simulation-only — Quantum advantage claims are speculative due to reliance on classical simulations rather than real quantum hardware
- #limitation:qubit-count — Quantum circuit learning model is limited to 10 qubits, restricting feature dimensions and scalability for real-world applications
- #limitation:noise — Noiseless simulation does not account for hardware noise, which could degrade performance on real quantum devices
## Contradictions
<!-- Step 6 output — where this paper contradicts others -->

## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
