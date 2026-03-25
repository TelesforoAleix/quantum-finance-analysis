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
contradiction_flags:
- contradiction:classical-vs-quantum
- contradiction:scalability
doi: ''
evidence_type: ''
idea_tags:
- idea:quantum-advantage
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
step1_date: '2026-03-25T16:00:32.981988'
step1_model: gpt-5.1
step2_date: '2026-03-25T16:00:41.678257'
step2_model: gpt-5.1
step3_date: '2026-03-25T16:01:18.888824'
step3_model: gpt-5.4
step4_date: '2026-03-25T16:01:59.190115'
step4_model: gpt-5.4
step5_date: '2026-03-25T16:02:23.341444'
step5_model: gpt-5.4
step6_date: '2026-03-25T16:02:34.640339'
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
title: The cross-sectional stock return predictions via quantum neural network and
  tensor network
topic_tags:
- asset-pricing
year: 2024
zotero_key: ''
---

## Abstract summary
The paper studies whether quantum and quantum-inspired machine learning methods can improve cross-sectional stock return prediction in a real-world setting. Using Japanese equities (TOPIX500) and 10 standard equity factors, the authors compare a quantum circuit learning model (quantum neural network) and a tensor network model against linear regression and classical neural networks via a long-only portfolio backtest over about a decade. They find that the tensor network delivers the highest excess return and information ratio, while the quantum model is broadly comparable to neural networks overall and appears to perform relatively better in more recent market conditions, suggesting some ability to capture nonlinear factor interactions and potential robustness to overfitting.
## Methodology
This preprint reports an empirical backtesting study comparing quantum and quantum-inspired machine learning methods for cross-sectional stock return prediction in the Japanese equity market. The authors formulate monthly one-step-ahead return prediction as a supervised regression problem using 10 firm-level features per stock, and compare four model classes: ordinary linear regression, feed-forward neural networks, quantum circuit learning (used as a quantum neural network), and a tensor-network model based on matrix product states. All models are trained to minimize mean squared error using stochastic gradient descent-style optimization, with Adam used for the machine learning models and parameter-shift gradients for the quantum circuit learning model. The empirical evaluation uses a rolling-window portfolio backtest on TOPIX500 constituents: an initial 3-year training window is used to train each model, the subsequent 1-year period is used for testing, and this process is rolled forward annually from June 2008 to May 2021. At each month, stocks are ranked by predicted returns, the top quintile is selected into an equal-weight long portfolio, and performance is evaluated relative to the TOPIX500 benchmark using annualized excess return (ER), tracking error (TE), and information ratio (IR). The quantum model is implemented on a noiseless simulator rather than real hardware, while the tensor-network and neural-network models are implemented with classical ML libraries.

**Algorithms used:** Quantum Circuit Learning, Quantum Neural Network, Tensor Network, Matrix Product State, Linear Regression, Feed-forward Neural Network, Stochastic Gradient Descent, Adam, Parameter-shift rule
**Frameworks:** Qulacs, TensorFlow, TensorNetwork

**Experimental setup:** Empirical monthly backtesting on Japanese equities in the TOPIX500 universe over June 2008 to May 2021. Models were trained on rolling 3-year windows and tested on the following 1-year window, with model re-estimation performed annually rather than monthly to reduce computational cost. The quantum circuit learning model used 10 qubits and was simulated in a noiseless setting with Qulacs. Neural networks and tensor networks were implemented in TensorFlow/TensorNetwork. Portfolio construction used monthly ranking of predicted returns and equal-weight investment in the top quintile of stocks.

**Dataset:** Japanese stock market data for constituents of the TOPIX500 index, covering the 500 most liquid and largest-cap stocks listed on the Tokyo Stock Exchange. Ten cross-sectional firm features were used: book-to-price, earnings-to-price, sales-to-price, return on equity, 1-month momentum, 3-month momentum, 6-month momentum, 12-month momentum, market capitalization, and market beta. Returns and features were cross-sectionally ranked each month.
## Findings
- [supported] In a 10-year monthly backtest on Japanese TOPIX500 stocks, the tensor network (TN) model achieved the best overall investment performance among the tested models, with higher annualized excess return and information ratio than linear regression, classical neural networks, and quantum circuit learning.
- [supported] The TN model produced an annualized excess return of 3.71%, tracking error of 5.41%, and information ratio of 0.69 over the full backtest period, outperforming the best classical neural network benchmark (NN2: 1.76% ER, 4.28% TE, 0.41 IR).
- [supported] The quantum circuit learning / quantum neural network (QCL) model underperformed the classical neural network models on a risk-adjusted basis over the full sample, with 1.35% annualized excess return, 6.18% tracking error, and 0.22 information ratio.
- [supported] In the post-2016 subperiod, both QCL and TN outperformed the classical benchmarks in the reported backtest, with QCL achieving 2.63% annualized excess return and 0.45 information ratio, and TN achieving 4.20% annualized excess return and 0.82 information ratio.
- [supported] The authors report that before 2016, QCL performed approximately similarly to linear regression, while after 2016 it outperformed linear regression and, in the reported backtest, also exceeded the classical neural network models.
- [speculative] The stronger recent-period performance of QCL and TN suggests these models may better capture nonlinear and interaction effects among stock features than linear regression.
- [speculative] The authors suggest the weaker recent performance of the classical neural networks may reflect overfitting to prior market environments, while quantum and quantum-inspired models may be less prone to such overfitting.
- [supported] All quantum results were obtained using a noiseless simulator (Qulacs) with 10 qubits and circuit depth d=3 rather than on real quantum hardware.
- [supported] The study restricted inputs to 10 stock features partly because the QCL architecture required one qubit per feature and larger simulations were computationally expensive.
- [speculative] The paper argues that quantum and quantum-inspired models have potential usefulness for stock return prediction beyond conventional models, but this is not established as a scalable quantum advantage.

**Results summary:** This preprint evaluates stock return prediction using a quantum circuit learning (QCL) model and a tensor network (TN) model against linear regression and two classical neural networks on Japanese TOPIX500 stocks. Using 10 cross-sectional features, annual model retraining on rolling 3-year windows, and monthly portfolio backtesting from June 2008 to May 2021, the authors find that the tensor network model delivers the strongest empirical investment performance. Over the full sample, TN achieved 3.71% annualized excess return and 0.69 information ratio, exceeding all classical benchmarks. QCL was competitive in raw excess return but had higher risk and lower risk-adjusted performance than the classical neural networks over the full period. In a post-2016 subperiod, both TN and QCL outperformed the classical models in the reported backtest. However, because the paper is a preprint and the quantum model was evaluated only in noiseless simulation rather than on hardware, any implication of quantum advantage remains speculative rather than demonstrated.

**Performance claims:**
- Full backtest (TOPIX500, June 2008-May 2021): Linear ER -0.28%, TE 6.64%, IR -0.04
- Full backtest: NN1 ER 1.27%, TE 3.79%, IR 0.34
- Full backtest: NN2 ER 1.76%, TE 4.28%, IR 0.41
- Full backtest: QCL ER 1.35%, TE 6.18%, IR 0.22
- Full backtest: TN ER 3.71%, TE 5.41%, IR 0.69
- Post-2016 backtest: Linear ER -0.12%, TE 7.82%, IR -0.02
- Post-2016 backtest: NN1 ER 0.56%, TE 3.48%, IR 0.16
- Post-2016 backtest: NN2 ER 0.18%, TE 4.31%, IR 0.04
- Post-2016 backtest: QCL ER 2.63%, TE 5.85%, IR 0.45
- Post-2016 backtest: TN ER 4.20%, TE 5.14%, IR 0.82
- QCL configuration: 10 qubits, depth d=3, 90 trainable parameters, noiseless simulation
- TN configuration: bond dimension m=2, 76 trainable parameters
- NN1 configuration: 92 trainable parameters; NN2: 93 trainable parameters
- Training setup: rolling 3-year train / 1-year test, monthly predictions, 20 epochs with Adam optimizer
## Quantum advantage claim
**Classification:** speculative

The paper suggests quantum and quantum-inspired models may better capture nonlinearities and possibly resist overfitting, but the quantum model was tested only in noiseless simulation and did not outperform the best tensor-network result or all classical baselines across the full sample. No clear quantum computational advantage is demonstrated.
## Limitations
- The study is a preprint and has not undergone peer review.
- Experiments are limited to the Japanese stock market (TOPIX500 universe), so generalizability to other countries or global markets is untested.
- Only 10 input features are used, which the authors note is smaller than typical machine learning stock prediction studies.
- The feature count is constrained by the quantum circuit learning architecture requiring one qubit per feature and by the computational cost of simulating larger quantum circuits.
- Quantum circuit learning was evaluated only on a simulator, not on real quantum hardware.
- The numerical experiments for the quantum circuit learning model were conducted in a noiseless setting.
- Models are re-estimated only once a year rather than monthly because estimation for quantum circuit learning on a simulator is computationally intensive.
- The paper does not explore alternative quantum circuit architectures or encoding schemes, and explicitly leaves the effect of different circuit choices for future investigation.
- Tensor network optimization uses gradient descent instead of the more standard DMRG approach, which the authors acknowledge may be more sophisticated.
- The dataset is not publicly available due to licensing agreements, limiting reproducibility.
- [inferred] No direct evidence of quantum advantage is shown, since the quantum model underperforms the tensor network model and is only comparable to classical neural networks in some settings.
- [inferred] The use of a quantum simulator rather than hardware means practical deployment feasibility under NISQ noise and latency constraints remains unclear.
- [inferred] The backtest uses a single market, single asset class, and monthly long-only top-quintile strategy, which narrows the scope of conclusions.
- [inferred] The study does not report transaction costs, market impact, turnover, or slippage, so real-world investability of the backtest is uncertain.
- [inferred] Hyperparameter exploration appears limited; model depth, bond dimension, and architecture choices may materially affect results.
- [inferred] The claim that recent QCL performance may relate to reduced overfitting is speculative and not causally validated.
- [inferred] Benchmarking is limited; there is no comparison against stronger modern classical baselines such as tree ensembles, boosting, transformers, or larger regularized deep models.
- [inferred] Statistical significance testing of performance differences is not reported, so it is unclear whether observed return differences are robust.
- [inferred] The sample period, though spanning about 10 years, may still be limited relative to regime variability in financial markets.
## Open questions
- Do quantum models for stock return prediction generalize to other countries such as the United States or to global equity markets?
- Can transfer learning be effective for quantum models across different financial markets?
- Are quantum machine learning methods applicable to other asset classes such as bonds or currencies?
- How effective would quantum machine learning be for time-series return prediction, as opposed to the cross-sectional approach used here?
- Can quantum counterparts of recurrent neural networks improve financial forecasting tasks?
- Does the apparent resilience of quantum models in the latest market environment truly reflect better control of overfitting?
- How sensitive is performance to the choice of quantum data encoding and parameterized circuit architecture?
- Would the tensor network model remain superior if the number of features and model parameters were increased?
- How much would tensor network performance change if optimized with DMRG rather than gradient descent?
- [inferred] How would the quantum circuit learning model perform on real noisy hardware with limited connectivity and gate fidelity?
- [inferred] Are the reported excess returns statistically significant after accounting for estimation uncertainty and multiple model comparisons?
- [inferred] How robust are the results to transaction costs, turnover constraints, and alternative portfolio construction rules?

**Future work:**
- Examine whether quantum models work in other countries, such as the United States, or in global markets.
- Investigate transfer learning for quantum models across different markets.
- Apply quantum machine learning to other asset classes, including bonds and currencies.
- Study time-series return prediction with quantum machine learning, beyond the cross-sectional setting.
- Explore quantum counterparts of recurrent neural networks for financial analysis.
- Further examine whether quantum techniques help control overfitting, as hypothesized by the authors.
- Investigate the effects of using different quantum circuit architectures and encoding schemes.
- Test whether tensor network superiority persists when increasing the number of features and parameters.
- Compare tensor network optimization via gradient descent with DMRG-based optimization.
- [inferred] Validate the methods on real quantum hardware and assess robustness under realistic noise.
- [inferred] Expand benchmarking to stronger classical baselines and broader portfolio construction methods.
- [inferred] Evaluate out-of-sample robustness with transaction costs, turnover controls, and additional market regimes.
## Key ideas
- #idea:near-term-feasibility — The paper studies quantum circuit learning for cross-sectional stock return prediction in a realistic decade-long TOPIX500 backtest, making it directly relevant to practical financial ML.
- #idea:hybrid-approach — The quantum model is trained with classical optimization and evaluated via classical simulation, reflecting a hybrid quantum-classical workflow rather than standalone quantum execution.
- #idea:quantum-advantage — QCL appears to outperform classical baselines in the post-2016 subperiod, suggesting possible benefits in capturing nonlinear factor interactions and resisting overfitting, though this remains speculative.
- #idea:near-term-feasibility — A tensor-network quantum-inspired model outperforms both classical neural networks and the quantum circuit model, indicating that quantum-inspired methods may be more immediately useful than actual quantum models.
- #idea:quantum-advantage — The paper explicitly frames any advantage claim as potential rather than demonstrated, since the quantum model does not win over the full sample and no computational speedup is shown.
## Contradictions
- The paper hints at quantum advantage in recent market regimes, but its own full-sample results contradict strong superiority claims: the QCL model underperforms the tensor-network model and has worse risk-adjusted performance than the best classical neural network.
- Any implication of scalable quantum benefit is contradicted by the implementation constraints: the model uses only 10 qubits, one qubit per feature, and larger problems are limited by simulation cost, undermining claims of applicability to realistic high-dimensional financial prediction.
- Claims about practical quantum usefulness are weakened by the fact that all quantum results come from noiseless classical simulation rather than real hardware, contradicting any strong inference about deployable NISQ-era advantage.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->

## Experiment details
### Input
Input universe: TOPIX500 constituent stocks in Japan. Time period: backtest from June 2008 to May 2021, with monthly observations. Features: 10 per stock — book-value to price, earnings to price, sales to price, return on equity, momentum over 1/3/6/12 months, market capitalization, and 60-month market beta versus TOPIX. Target: one-month-ahead stock return. Preprocessing: at each month, all features and returns were cross-sectionally ranked and transformed to rank/(N_t - 1); QCL inputs were required to lie in [-1, 1]. Training/test split: rolling 3-year training window followed by 1-year test window, advanced annually.

### Process
1. Define monthly cross-sectional return prediction task for TOPIX500 stocks. 2. For each month, compute 10 firm features and one-month-ahead returns. 3. Preprocess features and returns by cross-sectional ranking at each time step. 4. Train each model on the most recent 3 years of monthly data, then test on the subsequent 1 year; repeat this rolling procedure annually through the sample. 5. Linear model estimated by ordinary least squares benchmark. 6. Neural networks (NN1 and NN2) trained with ReLU activations and Adam for 20 epochs. 7. QCL model: encode each 10-dimensional input into a 10-qubit state using per-qubit RZ(cos^-1(x_j^2)) and RY(sin^-1(x_j)) rotations; apply a parameterized circuit of depth d=3 consisting of random Hamiltonian evolution gates and trainable RX-RZ-RX rotations on each qubit; measure expectation value of Z on the first qubit as prediction; optimize parameters using gradient-based learning with parameter-shift gradients. 8. Tensor network model: map each scalar feature x_j to phi(x_j)=(1, x_j), form a tensor-product feature map, and learn an MPS regression tensor with bond dimension 2 using gradient descent/Adam-style optimization rather than DMRG. 9. During testing, rank stocks by predicted next-month returns, select the top quintile, and form an equal-weight long portfolio. 10. Compute monthly excess returns over TOPIX500 and summarize performance using annualized excess return, tracking error, and information ratio.

### Output
Primary outputs are portfolio-level backtest metrics: annualized excess return (ER), tracking error (TE), and information ratio (IR), plus cumulative return and cumulative excess return plots. Baseline comparisons include linear regression (Linear) and two classical neural networks (NN1, NN2), against quantum circuit learning (QCL) and tensor network (TN). Reported full-period results show TN with the best ER and IR, while QCL is competitive on ER but worse on risk-adjusted performance due to higher TE.

### Parameters
- features: 10
- backtest_start: 2008-06
- backtest_end: 2021-05
- rebalancing_frequency: monthly
- training_window_years: 3
- test_window_years: 1
- model_refit_frequency: annually
- portfolio_selection: top quintile by predicted return
- portfolio_weighting: equal weight
- optimizer: Adam
- epochs: 20
- qcl_qubits: 10
- qcl_depth_d: 3
- qcl_observable: Pauli Z on first qubit
- qcl_parameters: 90
- qcl_random_hamiltonian_coefficients: a_j and J_jk sampled uniformly from [-1,1] and fixed
- tn_bond_dimension: 2
- tn_parameters: 76
- nn1_layers: 3
- nn1_nodes: [10, 7, 1]
- nn1_parameters: 92
- nn2_layers: 4
- nn2_nodes: [10, 5, 4, 1]
- nn2_parameters: 93
- activation_function: ReLU
- loss_function: mean squared error

### Hardware
Quantum experiments were not run on real QPU hardware. The QCL model was executed on the Qulacs quantum circuit simulator in a noiseless simulation setting. Classical models used TensorFlow and TensorNetwork; no further CPU/GPU/cloud or transpilation details are reported.

### Reproducibility
Preprint empirical study. No code repository is mentioned. Data are not publicly available due to licensing restrictions. The paper provides substantial methodological detail on model architectures, rolling-window design, features, and evaluation metrics, so partial replication is possible with equivalent proprietary market data, but full reproducibility is limited by unavailable data and missing low-level training hyperparameters (e.g., learning rate, batch size, evolution time tau, random seeds).
