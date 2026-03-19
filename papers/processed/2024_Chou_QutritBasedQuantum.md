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
- idea:near-term-feasibility
- idea:hybrid-approach
journal_or_venue: 2024 IEEE International Conference on Quantum Computing and Engineering
  (QCE)
methodology_tags:
- classical-simulation
- variational
paper_type: ''
quantum_advantage_claim: speculative
related_papers: []
relevance_phase1: medium
relevance_phase3: not-yet-assessed
source_type: conference-paper
source_type_confidence: high
step1_date: '2026-03-18T23:04:59.912267'
step1_model: Mistral-Large-3
step2_date: '2026-03-18T23:05:03.914437'
step2_model: Mistral-Large-3
step3_date: '2026-03-18T23:05:33.457336'
step3_model: Mistral-Large-3
step4_date: '2026-03-18T23:05:40.453849'
step4_model: Mistral-Large-3
step5_date: '2026-03-18T23:05:49.357571'
step5_model: Mistral-Large-3
step6_date: '2026-03-18T23:06:38.109402'
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
- method/variational
- idea/near-term-feasibility
- idea/hybrid-approach
- contradiction/classical-vs-quantum
- contradiction/scalability
title: Qutrit-based Quantum-inspired Optimization Model on Real-world Portfolio Optimization
topic_tags:
- portfolio-optimisation
year: 2024
zotero_key: ''
---

## Abstract summary
This paper introduces a quantum-inspired optimization model using qutrits (three-level quantum systems) to enhance portfolio optimization in financial services. The authors propose a ternary encoding mechanism that incorporates long-selling, short-selling, and non-investment strategies to reduce risk and improve investment efficiency. The study applies this approach to real-world financial data, demonstrating its potential to outperform traditional binary decision methods in volatile market conditions.
## Methodology
The paper proposes a quantum-inspired optimization (QIO) model for portfolio optimization using a qutrit-based hybrid strategy. The methodology leverages ternary encoding inspired by qutrit quantum states (|0⟩, |1⟩, |2⟩) to represent three investment strategies: non-investment, long-selling (LS), and short-selling (SS). The Global Best Guided Quantum-inspired Tabu Search (GQTS) algorithm is adapted to support qutrit-based encoding, enabling the model to explore hybrid portfolios that combine LS and SS strategies to mitigate risk. The trend ratio metric is used to evaluate portfolio performance, focusing on return per unit of risk. The experimental approach involves simulating the qutrit-based QIO on a classical computer, applying it to real-world financial data from the DJIA index (2013-2022) using a sliding window method for training and testing. The model's performance is compared against single-strategy portfolios (LS and SS) implemented via EL-GNQTS, with risk and trend ratio as key evaluation metrics.

**Algorithms used:** Global Best Guided Quantum-inspired Tabu Search (GQTS), EL-GNQTS

**Experimental setup:** The experiments were conducted on a classical computer. The model was applied to the Dow Jones Industrial Average (DJIA) index with a solution space of 330 stocks and an initial fund of 10 million dollars. The investment period spanned from 2013 to 2022, using a sliding window method to split training and testing data. The population size was set to 10, with each experiment tested 50 times per period and each test running for 10,000 iterations. The parameter θ was fine-tuned to 0.0003.

**Dataset:** Real-world financial data from the Dow Jones Industrial Average (DJIA) index, covering the period from 2013 to 2022.
## Findings
- [supported] The qutrit-based quantum-inspired optimization (QIO) model demonstrates superior portfolio performance compared to single long-selling (LS) or short-selling (SS) strategies when applied to real-world financial data (DJIA index, 2013-2022)
- [supported] The hybrid strategy combining LS and SS reduces investment risk and achieves a higher trend ratio (return per unit of risk) than either strategy alone, as shown in 13 sliding window experiments
- [supported] The proposed qutrit-based encoding mechanism enables simultaneous search for LS, SS, and non-investment strategies, mitigating risk through complementary fluctuations between LS and SS portfolios
- [speculative] The qutrit-based approach leverages quantum behavior in a large solution space to efficiently search for potential solutions, potentially offering advantages over binary qubit-based methods
- [speculative] The authors suggest that qutrit systems may be favorable for quantum error correction in the NISQ era due to their high-fidelity operations
- [speculative] The hybrid strategy could provide stable uptrend portfolios regardless of bull or bear market conditions

**Results summary:** The paper presents a qutrit-based quantum-inspired optimization model for portfolio optimization, implemented on classical hardware. The model uses ternary encoding to represent long-selling, short-selling, and non-investment strategies simultaneously. Experimental results on the DJIA index (2013-2022) demonstrate that the hybrid strategy outperforms single-strategy approaches in both risk reduction and trend ratio (return per unit of risk). The complementary fluctuations between LS and SS strategies effectively mitigate risk, producing more stable uptrend portfolios. While the results are promising, they are derived from classical simulations rather than real quantum hardware.

**Performance claims:**
- Hybrid strategy achieves consistently lower risk than LS or SS alone across 13 sliding window experiments
- Hybrid strategy outperforms LS and SS in trend ratio (return per unit of risk) metrics
- Model tested on DJIA index with solution space of 330 and 10 million dollar initial fund
- Experiments conducted over 830 periods with 50 runs per period (10,000 iterations each)
## Quantum advantage claim
**Classification:** speculative

The paper claims potential advantages of qutrit-based encoding for portfolio optimization, including more efficient solution space exploration. However, these claims are based on classical simulations of quantum-inspired algorithms rather than real quantum hardware. The authors suggest future applicability to quantum devices but do not demonstrate quantum advantage empirically.
## Limitations
- The study is conducted using quantum-inspired optimization (QIO) on classical computers, not on actual quantum hardware, limiting insights into real quantum performance [inferred]
- The proposed qutrit-based model is not tested on real quantum devices, which may exhibit noise and decoherence effects not captured in classical simulations
- Experiments are limited to the DJIA index with a solution space of 330, which may not generalize to larger or more diverse financial datasets [inferred]
- The study uses a sliding window method with 13 types of windows, but the impact of different window sizes or alternative data-splitting methods is not explored [inferred]
- The population size is set to 10, and each experiment is tested 50 times per period, which may not be sufficient to capture statistical significance in all market conditions [inferred]
- The fine-tuned parameter θ is set to 0.0003, but the sensitivity of results to this parameter is not thoroughly analyzed [inferred]
- The comparison is made only against EL-GNQTS, and no benchmarking is performed against state-of-the-art classical or other quantum-inspired methods [inferred]
- The study focuses on a single-objective optimization (risk mitigation), while real-world portfolio optimization often involves multi-objective trade-offs (e.g., risk vs. return) [inferred]
- Page-limit constraints of the conference paper may have restricted the depth of analysis or additional experiments [inferred]
- The proposed method is tested on historical data, and its performance in live, real-time market conditions is unproven [inferred]
## Open questions
- How would the qutrit-based hybrid strategy perform on actual quantum hardware with noise and decoherence?
- What is the scalability of the proposed method for larger solution spaces or more complex financial instruments (e.g., derivatives, multi-asset classes)?
- How does the trend ratio metric compare to other established portfolio performance metrics (e.g., Sharpe ratio, Sortino ratio) in terms of robustness?
- Can the qutrit-based encoding be extended to more than three states (e.g., qudits) to capture additional investment strategies or market conditions?
- What is the computational overhead of the qutrit-based QIO compared to classical methods, and is there a clear quantum advantage?
- How sensitive are the results to the choice of θ and other hyperparameters, and can automated tuning methods improve performance?
- Would the hybrid strategy remain effective in extreme market conditions (e.g., financial crises, high volatility periods)?

**Future work:**
- Test the proposed qutrit-based QIO on real quantum hardware to evaluate its performance under noise and decoherence
- Extend the model to multi-objective optimization, incorporating both risk and return as objectives
- Apply the method to other financial markets (e.g., forex, commodities) or larger datasets to assess generalizability
- Benchmark the proposed method against state-of-the-art classical and quantum-inspired portfolio optimization techniques
- Explore the use of qudits (higher-dimensional quantum systems) to encode more complex investment strategies
- Investigate the integration of real-time market data and adaptive learning mechanisms to improve responsiveness to market changes
- Develop automated hyperparameter tuning methods to optimize the performance of the qutrit-based GQTS algorithm
## Key ideas
- #idea:hybrid-approach — Qutrit-based ternary encoding enables simultaneous long-selling, short-selling, and non-investment strategies, improving risk mitigation in portfolio optimization
- #idea:near-term-feasibility — Quantum-inspired qutrit model demonstrates potential for NISQ-era applicability, though tested only via classical simulation
- #limitation:simulation-only — Results are derived from classical simulations of quantum-inspired algorithms, not real quantum hardware
- #limitation:no-empirical-validation — Claims of quantum advantage are speculative and lack empirical validation on actual quantum devices
## Contradictions
- The paper claims potential advantages of qutrit-based encoding for efficient solution space exploration (#idea:quantum-advantage), but these claims are contradicted by the lack of real quantum hardware testing (#contradiction:classical-vs-quantum).
- While the model shows promise for small-scale portfolio optimization (DJIA index with 330 stocks), its scalability to larger or more complex financial datasets remains unproven (#contradiction:scalability).
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
