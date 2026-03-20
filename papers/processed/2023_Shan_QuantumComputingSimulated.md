---
aliases:
- Quantum Computing Simulated Annealing Algorithm Applying in Portfolio Optimization
  Problem
- Quantum Computing Simulated Annealing
authors:
- Baoyuan Shan
- Zucheng Shang
auto_detected: true
classification: ''
contradiction_flags:
- contradiction:classical-vs-quantum
- contradiction:scalability
doi: 10.4108/eai.1-9-2023.2338767
evidence_type: ''
idea_tags:
- idea:quantum-advantage
- idea:near-term-feasibility
- idea:hybrid-approach
journal_or_venue: ICPDI 2023
methodology_tags:
- quantum-annealing
- QUBO
- classical-simulation
paper_type: ''
quantum_advantage_claim: speculative
related_papers: []
relevance_phase1: high
relevance_phase3: medium
source_type: conference-paper
source_type_confidence: high
step1_date: '2026-03-19T23:34:57.963251'
step1_model: Mistral-Large-3
step2_date: '2026-03-19T23:35:00.144239'
step2_model: Mistral-Large-3
step3_date: '2026-03-19T23:35:05.694876'
step3_model: Mistral-Large-3
step4_date: '2026-03-19T23:35:47.810176'
step4_model: Mistral-Large-3
step5_date: '2026-03-19T23:35:54.698419'
step5_model: Mistral-Large-3
step6_date: '2026-03-19T23:35:57.974055'
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
- method/quantum-annealing
- method/QUBO
- method/classical-simulation
- idea/quantum-advantage
- idea/near-term-feasibility
- idea/hybrid-approach
- contradiction/classical-vs-quantum
- contradiction/scalability
title: Quantum Computing Simulated Annealing Algorithm Applying in Portfolio Optimization
  Problem
topic_tags:
- portfolio-optimisation
year: 2023
zotero_key: ''
---

## Abstract summary
This paper explores the application of quantum annealing algorithms to portfolio optimization in financial services. It proposes a quantum computing-based framework to model and solve portfolio investment problems, leveraging quantum tunneling effects to improve optimization efficiency. The study integrates modern portfolio theory with quantum annealing techniques, demonstrating how quantum properties can enhance traditional optimization approaches for real-world stock price trends.
## Methodology
The paper proposes a quantum annealing (QA) algorithm for portfolio optimization within the framework of Modern Portfolio Theory (MPT). The methodology involves modeling the portfolio optimization problem as a Quadratic Unconstrained Binary Optimization (QUBO) problem, where binary variables represent the inclusion or exclusion of stocks in the portfolio. The quantum annealing algorithm is used to escape local optima via quantum tunneling, leveraging the quantum adiabatic theorem to find the global optimum. The objective function combines return and risk metrics, adjusted by a smoothness index to reflect investor risk preferences. Constraints such as investment budget are incorporated using penalty functions. The algorithm is simulated using Python, and two portfolio strategies (risk-seeking and risk-averse) are constructed and compared against the DOW index and stochastic measures.

**Algorithms used:** Quantum Annealing

**Experimental setup:** The quantum annealing algorithm was simulated using Python. The experimental setup involved constructing portfolio strategies based on investor risk preferences, with specific parameters for investment budget, risk-free interest rate, and smoothness indices for risk-seeking and risk-averse portfolios.

**Dataset:** Real stock price trends from financial markets, though specific datasets (e.g., stock symbols, time periods) are not explicitly mentioned.
## Findings
- [supported] The quantum annealing algorithm was simulated in Python to optimize portfolio strategies for risk-seeking and risk-averse investors, with results showing superior performance compared to the DOW index and stochastic buying approaches
- [supported] The optimized portfolio data outperformed baseline strategies (DOW index and random selection) in terms of return and stability, as demonstrated in Fig. 1
- [speculative] Quantum annealing algorithms may excel in both speed and stability over simulated annealing algorithms when the data size is sufficiently large
- [speculative] The paper suggests that quantum annealing could provide new possibilities for solving complex optimization problems as quantum computing technology advances
- [disputed] The claim that quantum annealing is consistently superior to simulated annealing is unresolved, with no empirical validation provided in this paper
- [speculative] The authors propose future exploration of web crawling techniques to adjust stock values based on news sentiment for predictive investment strategies

**Results summary:** The paper presents a quantum annealing-based framework for portfolio optimization, modeled using Quadratic Unconstrained Binary Optimization (QUBO). Simulations in Python demonstrated that the algorithm outperformed classical benchmarks (DOW index and stochastic buying) for both risk-seeking and risk-averse strategies. While the results show improved returns and stability, the paper acknowledges unresolved questions about the conditions under which quantum annealing surpasses classical methods like simulated annealing. The work is purely simulation-based, with no real hardware validation.

**Performance claims:**
- Portfolio strategies optimized via quantum annealing outperformed the DOW index and stochastic buying in simulated tests
- Risk-seeking and risk-averse portfolios were constructed with an investment budget of 1000 and risk-free rate of 2%
## Quantum advantage claim
**Classification:** speculative

The paper suggests theoretical advantages in speed and stability for quantum annealing over simulated annealing for large datasets, but these claims are not empirically validated. All results are derived from simulations, not real quantum hardware.
## Limitations
- The paper relies on simulations rather than real quantum hardware, limiting validation of quantum advantage [inferred]
- Experiments are conducted with a small investment budget (K = 1000) and synthetic or simplified data, which may not scale to real-world portfolio sizes [inferred]
- Binary variables (0 or 1) are used to represent stock purchases, which oversimplifies real-world portfolio allocation (e.g., fractional shares or continuous weights) [inferred]
- No comparison with state-of-the-art classical portfolio optimization methods (e.g., convex optimization, genetic algorithms) to benchmark performance [inferred]
- The paper does not address hardware noise or decoherence effects, which are critical for real quantum annealing devices [inferred]
- Parameter tuning (e.g., smoothness index L, penalty coefficient λ) is arbitrary and lacks a quantitative strategy, as noted by the authors
- The study does not explore the impact of varying qubit counts or problem sizes on algorithm performance [inferred]
- Constraints are enforced via penalty functions, which may not guarantee feasibility in all cases and could introduce suboptimality [inferred]
- The paper does not validate the model on real market data, relying instead on simulated or historical trends [inferred]
- Page-limit constraints of the conference paper may have restricted detailed discussion of methodology or results [inferred]
## Open questions
- Under what conditions (e.g., problem size, noise levels) do quantum annealing algorithms consistently outperform simulated annealing?
- How can parameters (e.g., smoothness index L, penalty coefficient λ) be quantitatively optimized for different investor risk profiles?
- What is the scalability of the proposed method for large-scale portfolios (e.g., >100 assets) on current or near-term quantum hardware?
- How does the algorithm perform when extended to multi-period portfolio optimization or dynamic rebalancing?
- What is the impact of quantum noise and error rates on solution quality in real quantum annealing devices?
- Can the model incorporate real-time data (e.g., news sentiment, trading volumes) to improve predictive accuracy, as suggested in the future work?

**Future work:**
- Test the algorithm on real quantum hardware (e.g., D-Wave systems) to validate performance under noise and hardware constraints
- Extend the model to handle continuous or fractional portfolio weights instead of binary decisions
- Compare the quantum annealing approach with classical optimization methods (e.g., convex solvers, genetic algorithms) to benchmark quantum advantage
- Develop quantitative strategies for parameter tuning (e.g., smoothness index L, penalty coefficient λ) based on investor risk preferences
- Incorporate real-time data (e.g., web-crawled news or trading data) to adjust stock valuations dynamically and improve predictive capabilities
- Explore multi-period portfolio optimization to account for time-varying market conditions
- Investigate hybrid quantum-classical approaches to mitigate hardware limitations (e.g., qubit count, noise)
## Key ideas
- #idea:quantum-advantage — Quantum annealing leverages quantum tunneling to escape local optima, potentially outperforming classical simulated annealing for large datasets in portfolio optimization
- #idea:near-term-feasibility — The paper demonstrates near-term applicability of quantum annealing for portfolio optimization using simulations, though real hardware validation is pending
- #idea:hybrid-approach — The framework integrates classical preprocessing (QUBO formulation) with quantum annealing, suggesting a hybrid path for practical implementation
- #limitation:simulation-only — Results are derived from classical simulations, not real quantum hardware, limiting insights into noise and scalability
- #limitation:qubit-count — Binary asset selection and small investment budget (K=1000) may not scale to real-world portfolio sizes or constraints
- #limitation:no-empirical-validation — Claims of quantum advantage over simulated annealing are speculative and lack empirical validation on real quantum devices
## Contradictions
- #contradiction:classical-vs-quantum — The paper speculates quantum annealing may outperform simulated annealing for large datasets, but this is disputed due to lack of empirical validation and unclear conditions for superiority (e.g., problem size, noise levels).
- #contradiction:scalability — The study uses a small investment budget and binary asset selection, which may not reflect real-world scalability challenges (e.g., fractional investments, larger asset universes).
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->

## Experiment details
### Input
Stock purchase and sale prices, binary variables for stock inclusion, covariance matrices for risk calculation, and predefined parameters such as investment budget (K = 1000), risk-free interest rate (r = 2%), and smoothness indices (L_s = 200 for risk-seeking, L_a = 0.2 for risk-averse).

### Process
1. Formulate the portfolio optimization problem as a QUBO objective function combining return and risk. 2. Encode constraints (e.g., investment budget) using penalty functions. 3. Simulate quantum annealing to find the optimal portfolio configuration. 4. Adjust parameters (e.g., smoothness index) to reflect risk preferences. 5. Compare portfolio performance against benchmarks (DOW index and stochastic measures).

### Output
Time series of portfolio returns and rates of return for risk-seeking and risk-averse strategies, compared against the DOW index and a stochastic buying approach. Metrics include portfolio return trends and relative performance.

### Parameters
- investment_budget: 1000
- risk_free_interest_rate: 0.02
- smoothness_index_risk_seeking: 200
- smoothness_index_risk_averse: 0.2
- penalty_coefficient: λ (unspecified value)
- binary_variables: x_i ∈ {0, 1} for stock inclusion

### Hardware
Simulated quantum annealing using Python; no specific hardware (QPU or simulator) mentioned.

### Reproducibility
The paper provides a detailed description of the quantum annealing algorithm and the QUBO formulation, but no code or dataset is explicitly made available. The methodology is sufficiently described for replication, though specific implementation details (e.g., Python libraries used) are omitted.
