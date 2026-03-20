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
- variational
paper_type: ''
quantum_advantage_claim: speculative
related_papers: []
relevance_phase1: high
relevance_phase3: medium
source_type: conference-paper
source_type_confidence: high
step1_date: '2026-03-19T23:52:29.434633'
step1_model: Mistral-Large-3
step2_date: '2026-03-19T23:52:33.071094'
step2_model: Mistral-Large-3
step3_date: '2026-03-19T23:53:31.577602'
step3_model: Mistral-Large-3
step4_date: '2026-03-19T23:54:34.967044'
step4_model: Mistral-Large-3
step5_date: '2026-03-19T23:54:39.604669'
step5_model: Mistral-Large-3
step6_date: '2026-03-19T23:54:42.453179'
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
This paper introduces a quantum-inspired optimization model using qutrits—three-level quantum systems—to enhance portfolio optimization in financial services. Unlike traditional binary approaches, the proposed method encodes long-selling, short-selling, and non-investment strategies simultaneously, leveraging quantum-inspired techniques to reduce investment risk and improve stability. The study applies this model to real-world financial data, demonstrating its potential to outperform single-strategy portfolios in volatile markets.
## Methodology
The paper proposes a quantum-inspired optimization (QIO) model for portfolio optimization using a qutrit-based encoding mechanism. Unlike traditional binary qubit approaches, this method leverages the three-level qutrit system to encode three investment strategies: long-selling (LS), short-selling (SS), and non-investment. The study adopts the Global Best Guided Quantum-inspired Tabu Search (GQTS) algorithm, enhanced with a ternary update mechanism to adjust probabilities based on global best and local worst selections. The trend ratio metric is used to evaluate portfolio performance, aiming for a stable uptrend. The methodology is implemented on a classical computer, simulating quantum behavior to explore a hybrid portfolio strategy that mitigates investment risk by combining LS and SS strategies.

**Algorithms used:** Global Best Guided Quantum-inspired Tabu Search (GQTS)

**Experimental setup:** The experiments are conducted on a classical computer using a qutrit-inspired QIO model. The solution space is set to 330, with an initial fund of 10 million dollars. The sliding window (SW) method is used to split training and testing data over an investment period from 2013 to 2022.

**Dataset:** Dow Jones Industrial Average (DJIA) index in the U.S. from 2013 to 2022.
## Findings
- [supported] The qutrit-based quantum-inspired optimization (QIO) model demonstrates superior portfolio performance compared to single long-selling (LS) or short-selling (SS) strategies using real-world financial data from the DJIA index (2013-2022).
- [supported] The hybrid strategy combining LS and SS reduces portfolio risk and achieves a higher trend ratio (return per unit of risk) than individual strategies across 13 sliding window periods.
- [supported] The proposed qutrit-based encoding mechanism enables simultaneous search for LS, SS, and non-investment strategies, mitigating risk through complementary fluctuations in a volatile market.
- [speculative] Qutrit-based systems may offer advantages for quantum error correction and high-fidelity operations in the NISQ era, though these claims are not empirically validated in this study.
- [speculative] The qutrit-inspired approach could leverage quantum behavior in large solution spaces to enhance search efficiency, but results are derived from classical simulations rather than real quantum hardware.
- [supported] The Global Best Guided Quantum-inspired Tabu Search (GQTS) with ternary encoding outperforms EL-GNQTS in risk reduction and trend ratio improvement, as shown in comparative experiments.

**Results summary:** The paper presents a qutrit-based quantum-inspired optimization model for portfolio optimization, implemented on classical hardware. The model encodes three investment strategies (long-selling, short-selling, and non-investment) using ternary qutrit states, enabling hybrid portfolio construction. Experimental results on DJIA data (2013-2022) show that the hybrid strategy consistently reduces risk and improves trend ratios compared to single-strategy approaches. The study demonstrates the practical utility of quantum-inspired techniques for financial applications, though all results are derived from simulations rather than real quantum devices.

**Performance claims:**
- Hybrid strategy achieves lower risk than LS or SS in all 13 sliding window periods (Fig. 2a).
- Hybrid strategy outperforms LS and SS in trend ratio across all tested periods (Fig. 2b).
- Solution space of 3^30 (≈205 trillion) for 30-stock portfolios, leveraging qutrit encoding.
- Experiments conducted over 830 periods with 50 trials per period, each running 10,000 iterations.
## Quantum advantage claim
**Classification:** speculative

The paper claims potential advantages of qutrit-based systems for quantum error correction and large solution space exploration, but these are not demonstrated empirically. All results are from classical simulations of quantum-inspired algorithms, with no real hardware validation. Quantum advantage is implied theoretically but remains unproven in this work.
## Limitations
- The study uses a quantum-inspired optimization (QIO) model simulated on classical computers, not real quantum hardware, limiting validation of quantum advantages [inferred]
- Experiments are conducted on a limited solution space (3^30) and a single market index (DJIA), which may not generalize to larger or more diverse financial datasets [inferred]
- The proposed qutrit-based model is compared only to classical-inspired methods (EL-GNQTS) and not to state-of-the-art classical portfolio optimization techniques [inferred]
- Page-limit constraints of the conference paper may have restricted detailed discussion of noise resilience, scalability, or failure cases [inferred]
- The trend ratio metric, while useful, does not fully capture all dimensions of portfolio risk (e.g., tail risk, liquidity risk) [inferred]
- The study does not address the computational overhead of simulating qutrit states on classical hardware, which may limit practical scalability [inferred]
- No empirical validation on real quantum hardware (e.g., superconducting qutrits) to test fidelity or error correction assumptions
- The hybrid strategy assumes symmetric fluctuations between long-selling and short-selling, which may not hold in all market conditions (e.g., asymmetric volatility regimes) [inferred]
- Parameter tuning (e.g., θ = 0.0003) is fixed and may not be optimal for other datasets or market conditions [inferred]
## Open questions
- How would the qutrit-based model perform on fault-tolerant quantum hardware compared to NISQ-era simulations?
- What is the scalability of the proposed method for larger portfolios (e.g., >100 assets) or multi-asset classes (e.g., stocks, bonds, commodities)?
- How does the model handle non-stationary market conditions where historical trends may not predict future performance?
- Can the qutrit encoding be extended to incorporate additional investment strategies (e.g., options, leverage) without exponential complexity growth?
- What are the trade-offs between the computational cost of qutrit simulations and the performance gains over classical methods?
- How sensitive is the hybrid strategy to parameter choices (e.g., θ, population size) across different market regimes?

**Future work:**
- Extend the model to multi-objective optimization (e.g., balancing risk, return, and liquidity)
- Test the qutrit-based QIO on real quantum hardware to validate quantum advantages
- Expand experiments to include multiple global stock markets and asset classes
- Incorporate dynamic parameter adaptation to improve robustness across market conditions
- Explore hybrid quantum-classical approaches to mitigate classical simulation overhead
- Investigate the integration of quantum error correction techniques to enhance fidelity in qutrit operations
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

## Experiment details
### Input
{'source': 'DJIA index', 'time_period': '2013-2022', 'sliding_window_types': 13, 'periods': 830, 'initial_fund': '10 million dollars', 'preprocessing_steps': 'Sliding window method used to maintain training data freshness. Positive fund trend utilized for short-selling to align with long-selling trends.'}

### Process
1. Encode portfolio strategies (LS, SS, non-investment) using qutrit-based ternary encoding. 2. Apply GQTS with a population size of 10. 3. Adjust probabilities using global best (P_Gb) and local worst (P_Lw) states with a fine-tuned parameter θ = 0.0003. 4. Run 50 tests per period, each with 10,000 iterations. 5. Evaluate portfolio performance using the trend ratio metric.

### Output
{'metrics': ['Trend ratio', 'Risk (volatility)'], 'comparison_baselines': ['Long-selling (LS) strategy', 'Short-selling (SS) strategy', 'EL-GNQTS'], 'visualizations': 'Risk comparison (Fig. 2a), trend ratio comparison (Fig. 2b), and portfolio fund run charts (Fig. 3)'}

### Parameters
- population_size: 10
- iterations_per_test: 10000
- tests_per_period: 50
- theta: 0.0003
- sliding_window_types: 13
- solution_space: 330

### Hardware
Classical computer simulation of qutrit-based QIO; no quantum hardware or simulator specified.

### Reproducibility
The paper provides detailed parameter settings and methodological steps, but no code or dataset is explicitly made available. Sufficient detail is provided to replicate the experiments, though access to the DJIA dataset is required.
