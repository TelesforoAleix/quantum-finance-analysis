---
aliases:
- Qutrit-based Quantum-inspired Optimization Model on Real-world Portfolio Optimization
- Qutrit based Quantum inspired
authors:
- Yao-Hsin Chou
- Yun-Ting Lai
- Ming-Ho Chang
- Yu-Chi Jiang
- Shu-Yu Kuo
auto_detected: true
classification: ''
contradiction_flags:
- contradiction:classical-vs-quantum
- contradiction:scalability
doi: 10.1109/QCE60285.2024.10403
evidence_type: ''
idea_tags:
- idea:hybrid-approach
- idea:near-term-feasibility
journal_or_venue: 2024 IEEE International Conference on Quantum Computing and Engineering
  (QCE)
methodology_tags:
- classical-simulation
paper_type: ''
quantum_advantage_claim: speculative
related_papers: []
relevance_phase1: medium
relevance_phase3: not-yet-assessed
source_type: conference-paper
source_type_confidence: high
step1_date: '2026-03-19T12:56:39.449234'
step1_model: Mistral-Large-3
step2_date: '2026-03-19T12:56:55.758848'
step2_model: Mistral-Large-3
step3_date: '2026-03-19T12:57:20.903933'
step3_model: Mistral-Large-3
step4_date: '2026-03-19T12:57:56.192811'
step4_model: Mistral-Large-3
step5_date: '2026-03-19T12:58:26.737171'
step5_model: Mistral-Large-3
step6_date: '2026-03-19T12:58:32.621427'
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
- method/classical-simulation
- idea/hybrid-approach
- idea/near-term-feasibility
- contradiction/classical-vs-quantum
- contradiction/scalability
title: Qutrit-based Quantum-inspired Optimization Model on Real-world Portfolio Optimization
topic_tags:
- portfolio-optimisation
year: 2024
zotero_key: ''
---

## Abstract summary
This paper introduces a quantum-inspired optimization model using qutrits—three-level quantum systems—to enhance portfolio optimization in financial services. The authors propose a ternary encoding mechanism that incorporates long-selling, short-selling, and non-investment strategies to reduce risk and improve investment stability. The approach leverages quantum-inspired techniques on classical computers to efficiently explore large solution spaces and generate hybrid portfolios with superior performance compared to traditional binary strategies.
## Methodology
The paper proposes a quantum-inspired optimization (QIO) model for portfolio optimization using a qutrit-based hybrid strategy. The methodology introduces a ternary encoding scheme inspired by qutrits (three-level quantum systems) to represent three investment strategies: long-selling (LS), short-selling (SS), and non-investment. The Global Best Guided Quantum-inspired Tabu Search (GQTS) algorithm is adapted to support qutrit-based encoding, enabling the model to explore a larger solution space efficiently. The trend ratio metric is incorporated to evaluate portfolio performance, focusing on return per unit of risk. The experimental framework involves simulating the qutrit-based QIO on classical computers, applying it to real-world financial data from the DJIA index (2013-2022) using a sliding window method for training and testing. The model's performance is compared against traditional LS and SS strategies using risk and trend ratio as evaluation metrics.

**Algorithms used:** Global Best Guided Quantum-inspired Tabu Search (GQTS)

**Experimental setup:** The experiments were conducted on classical computers, simulating qutrit-based quantum-inspired optimization. The solution space was set to 3^30, with an initial fund of 10 million dollars. The sliding window method was used to split training and testing data across 830 periods. The population size was 10, with each experiment run 50 times per period for ten-thousand iterations. The parameter θ was fine-tuned to 0.0003.

**Dataset:** Real-world financial data from the Dow Jones Industrial Average (DJIA) index spanning 2013 to 2022, with investment periods segmented using the sliding window method.
## Findings
- [supported] The qutrit-based quantum-inspired optimization (QIO) model demonstrates superior portfolio performance compared to single long-selling (LS) or short-selling (SS) strategies using real-world financial data from the DJIA index (2013-2022).
- [supported] The hybrid strategy combining LS and SS significantly reduces investment risk and improves the trend ratio, as measured by the regression trend line metric.
- [supported] The proposed qutrit-based Global Best Guided Quantum-inspired Tabu Search (GQTS) effectively encodes three investment states (non-investment, LS, SS) and adjusts probabilities to stabilize portfolio performance.
- [speculative] Qutrit-based systems may offer advantages for quantum error correction and high-fidelity operations in the NISQ era, though these claims are not empirically validated in this study.
- [speculative] The qutrit-inspired ternary encoding could enable more efficient solution space exploration for portfolio optimization, but quantum advantage is not demonstrated on real hardware.
- [supported] The hybrid strategy's symmetric fluctuations between LS and SS portfolios eliminate risk and create a stable uptrend, as shown in run charts for specific investment periods.

**Results summary:** The paper presents a qutrit-based quantum-inspired optimization model for portfolio optimization, leveraging ternary encoding to simulate quantum behavior on classical computers. The hybrid strategy, which combines long-selling (LS) and short-selling (SS) portfolios, is shown to outperform single-strategy approaches in terms of risk reduction and trend ratio improvement using real-world DJIA index data. The study demonstrates empirical results from simulations, with the qutrit-based GQTS algorithm achieving lower risk and higher trend ratios across 13 sliding window periods. However, the work remains theoretical with respect to quantum advantage, as all experiments were conducted on classical hardware.

**Performance claims:**
- Hybrid strategy reduces risk compared to LS and SS portfolios across 13 sliding window periods (Fig. 2a).
- Hybrid strategy achieves higher trend ratios than LS or SS portfolios (Fig. 2b).
- Solution space of 3^30 explored with 10 million dollar initial fund over 2013-2022 investment period.
- 50 tests per period, each with 10,000 iterations, using θ = 0.0003 for fine-tuning.
## Quantum advantage claim
**Classification:** speculative

The paper suggests potential advantages of qutrit-based systems for quantum error correction and solution space exploration, but all results are derived from classical simulations. No empirical demonstration of quantum advantage on real hardware is provided.
## Limitations
- The study is conducted using quantum-inspired optimization (QIO) on classical computers, not real quantum hardware, limiting insights into actual quantum performance [inferred]
- Experiments are limited to the DJIA index with a solution space of 3^30, which may not generalize to larger or more diverse financial datasets [inferred]
- The proposed model is tested only on historical data from 2013 to 2022, without validation on more recent or volatile market conditions [inferred]
- Page-limit constraints of the conference paper may have restricted detailed discussion of methodology, parameter tuning, or failure cases [inferred]
- The qutrit-based encoding and update mechanism rely on specific assumptions about market behavior (e.g., symmetry of LS and SS fluctuations), which may not hold in all market conditions [inferred]
- No comparison with state-of-the-art classical portfolio optimization methods (e.g., modern portfolio theory or deep learning-based approaches) is provided [inferred]
- The study does not address the impact of noise or decoherence, which would be critical for real quantum hardware implementations [inferred]
- The trend ratio metric, while useful, may not fully capture all dimensions of portfolio risk and return (e.g., tail risk or liquidity constraints) [inferred]
- The population size (10) and iteration count (10,000) may limit the exploration of the solution space, potentially missing globally optimal portfolios [inferred]
- The sliding window method, while maintaining data freshness, may introduce look-ahead bias or overfitting to specific market regimes [inferred]
## Open questions
- How would the qutrit-based QIO model perform on real quantum hardware with current NISQ-era limitations (e.g., qubit count, noise, and gate fidelity)?
- Can the proposed hybrid strategy scale to larger portfolios (e.g., 100+ assets) without significant degradation in performance or computational efficiency?
- What is the robustness of the model to extreme market conditions (e.g., financial crises, black swan events) not captured in the 2013–2022 dataset?
- How does the qutrit-based approach compare to binary qubit-based or higher-dimensional qudit-based methods in terms of solution quality and computational overhead?
- What are the trade-offs between the trend ratio metric and other portfolio evaluation metrics (e.g., Sharpe ratio, Sortino ratio) in guiding optimization?
- Can the model be extended to multi-objective optimization (e.g., balancing risk, return, and transaction costs) without sacrificing stability?
- How sensitive is the model to the choice of hyperparameters (e.g., θ = 0.0003, population size, iteration count) and how can these be optimized?
- What are the implications of using a quantum-inspired approach for regulatory compliance or interpretability in financial applications?

**Future work:**
- Implement and test the qutrit-based QIO model on real quantum hardware to evaluate its performance under NISQ-era constraints
- Extend the model to multi-objective optimization, incorporating both risk and return as explicit objectives
- Apply the hybrid strategy to other financial markets (e.g., forex, commodities, or cryptocurrencies) to assess its generalizability
- Incorporate additional investment strategies (e.g., options, leverage) into the ternary encoding framework to explore more complex portfolios
- Develop noise mitigation techniques to improve the model's resilience to decoherence and gate errors on quantum hardware
- Compare the qutrit-based approach with state-of-the-art classical and quantum portfolio optimization methods to benchmark its advantages
- Explore adaptive parameter tuning mechanisms (e.g., reinforcement learning) to dynamically optimize θ and other hyperparameters
- Investigate the use of higher-dimensional qudits (e.g., ququarts) to encode even more complex investment strategies or market states
- Validate the model on out-of-sample data or synthetic datasets simulating extreme market conditions to test robustness
- Integrate the model with real-time market data feeds to enable dynamic portfolio rebalancing and live trading applications
## Key ideas
- #idea:hybrid-approach — Qutrit-based ternary encoding enables simultaneous long-selling, short-selling, and non-investment strategies, improving risk mitigation in portfolio optimization
- #idea:near-term-feasibility — Quantum-inspired qutrit model demonstrates potential for NISQ-era applicability, though tested only via classical simulation
- #limitation:simulation-only — Results are derived from classical simulations of quantum-inspired algorithms, not real quantum hardware
- #limitation:no-empirical-validation — Claims of quantum advantage are speculative and lack empirical validation on actual quantum devices
## Contradictions
- The paper claims potential advantages of qutrit-based encoding for efficient solution space exploration (#idea:quantum-advantage), but these claims are contradicted by the lack of real quantum hardware testing (#contradiction:classical-vs-quantum).
- While the model shows promise for small-scale portfolio optimization (DJIA index with 3^30 solution space), its scalability to larger or more complex financial datasets remains unproven (#contradiction:scalability).
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
