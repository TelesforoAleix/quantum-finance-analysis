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
paper_type: ''
quantum_advantage_claim: speculative
related_papers: []
relevance_phase1: high
relevance_phase3: medium
source_type: conference-paper
source_type_confidence: high
step1_date: '2026-03-19T12:43:19.307561'
step1_model: Mistral-Large-3
step2_date: '2026-03-19T12:43:33.016396'
step2_model: Mistral-Large-3
step3_date: '2026-03-19T12:43:56.363554'
step3_model: Mistral-Large-3
step4_date: '2026-03-19T12:44:25.229105'
step4_model: Mistral-Large-3
step5_date: '2026-03-19T12:45:45.073270'
step5_model: Mistral-Large-3
step6_date: '2026-03-19T12:46:10.669242'
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
This paper explores the application of quantum annealing algorithms to portfolio optimization in financial services, leveraging quantum tunneling effects to improve solution efficiency. The authors propose a quantum computing-based framework to model and solve portfolio investment problems, integrating modern portfolio theory with quantum annealing techniques to optimize stock price trends. The study demonstrates the approach through simulations and compares its performance with traditional methods.
## Methodology
The paper proposes a quantum annealing (QA) algorithm for solving the portfolio optimization problem within the framework of Modern Portfolio Theory (MPT). The methodology involves modeling the portfolio optimization as a Quadratic Unconstrained Binary Optimization (QUBO) problem, where the objective function balances return and risk. The quantum annealing algorithm is implemented through a simulated process that leverages quantum tunneling to escape local optima. The algorithm constructs a quantum Hamiltonian to represent the optimization problem, incorporating quantum potential and kinetic energy terms. The process involves iterative steps to adjust the transverse field strength, simulating annealing to reach the global optimum. Constraints such as investment budget are enforced using penalty functions. The approach is tested using Python simulations for two portfolio strategies (risk-seeking and risk-averse) and compared against the DOW index and stochastic measures.

**Algorithms used:** Quantum Annealing
**Frameworks:** PyQUBO

**Experimental setup:** The quantum annealing algorithm was simulated using Python. The experimental setup involved constructing portfolio strategies with an investment budget of 1000, a risk-free interest rate of 2%, and varying smoothness indices for risk-seeking (200) and risk-averse (0.2) portfolios. The results were compared with the DOW index and stochastic buying strategies.

**Dataset:** Real stock price trends from financial markets were used to construct the portfolio optimization model. Specific datasets or stock symbols are not explicitly mentioned, but the DOW index was used as a baseline for comparison.
## Findings
- [supported] The quantum annealing algorithm was simulated in Python to optimize portfolio strategies for risk-seeking and risk-averse investors, with results showing superior performance compared to the DOW index and stochastic buying approaches
- [supported] The optimized portfolio data significantly outperformed the original data, demonstrating the effectiveness of the quantum annealing approach in portfolio optimization
- [speculative] Quantum annealing algorithms may excel in both speed and stability compared to simulated annealing algorithms when the data size is sufficiently large
- [speculative] The paper suggests that as quantum computing technology advances, quantum annealing devices could offer new possibilities for solving various optimization problems, though their genuine potential remains an open question
- [speculative] The authors propose exploring web crawling techniques to retrieve stock-related data for predictive investment portfolio strategies, though the current model is insufficient for such predictions due to the complexity of stock price influences

**Results summary:** The paper presents a quantum annealing-based framework for portfolio optimization, leveraging quantum tunnelling effects to escape local optima. Simulated results demonstrate that the proposed method outperforms classical benchmarks (DOW index and stochastic buying) in terms of returns and stability for both risk-seeking and risk-averse strategies. While the model shows promise, the authors acknowledge unresolved challenges, including parameter tuning and the conditions under which quantum annealing consistently outperforms simulated annealing. The work is entirely simulation-based, with no empirical validation on real quantum hardware.

**Performance claims:**
- Optimized portfolio strategies (risk-seeking and risk-averse) outperformed the DOW index and stochastic buying in simulated tests
- Investment budget set at 1000 with a risk-free interest rate of 2%
- Smoothness index for risk-seeking portfolio: 200; for risk-averse portfolio: 0.2
## Quantum advantage claim
**Classification:** speculative

The paper claims potential speed and stability advantages of quantum annealing over simulated annealing for large datasets, but these claims are theoretical and based on simulation results only. No empirical demonstration on real quantum hardware is provided.
## Limitations
- The paper relies on simulations rather than real quantum hardware, limiting validation of quantum advantages [inferred]
- Experiments are conducted with a small investment budget (K = 1000) and synthetic or simplified data, which may not reflect real-world market conditions [inferred]
- The binary variable representation (ix ∈ {0,1}) restricts portfolio allocation to discrete choices (buy/no-buy), ignoring fractional shares or continuous allocation strategies [inferred]
- No comparison is made with state-of-the-art classical portfolio optimization methods (e.g., convex optimization, genetic algorithms) to benchmark performance [inferred]
- The paper does not address hardware noise or decoherence effects, which are critical for real quantum annealing devices [inferred]
- The quantum annealing algorithm's superiority over simulated annealing is claimed only for 'sufficiently large' data sizes, but no threshold or scalability analysis is provided
- Parameter tuning (e.g., smoothness index L, penalty coefficient λ) is arbitrary and lacks quantitative strategies, limiting reproducibility
- The model does not account for transaction costs, liquidity constraints, or dynamic market conditions, which are essential for practical portfolio optimization [inferred]
- Results are limited to a single dataset (DOW index) and lack validation across diverse market conditions or asset classes [inferred]
- The paper does not discuss the impact of quantum annealing's adiabatic evolution time on solution quality or practical runtime [inferred]
- Conference paper page limits may have constrained detailed discussion of methodology or results [inferred]
## Open questions
- How can parameters (e.g., smoothness index L, penalty coefficient λ) be quantitatively optimized for different investor risk preferences?
- Under what specific conditions (e.g., problem size, noise levels) do quantum annealing algorithms consistently outperform simulated annealing?
- What is the minimum qubit count or hardware fidelity required to achieve practical advantages for portfolio optimization?
- How does the algorithm perform with real-world constraints (e.g., transaction costs, liquidity, regulatory limits)?
- Can the binary variable approach be extended to continuous or fractional allocation strategies without sacrificing quantum advantage?
- What are the trade-offs between solution quality and adiabatic evolution time in quantum annealing for large-scale portfolio problems?
- How can the model incorporate dynamic market data (e.g., news sentiment, real-time pricing) to improve predictive capabilities?

**Future work:**
- Validate the algorithm on real quantum hardware (e.g., D-Wave systems) to assess performance under noise and decoherence
- Compare the quantum annealing approach with classical state-of-the-art methods (e.g., convex optimization, genetic algorithms) across diverse datasets
- Develop quantitative strategies for parameter tuning (e.g., smoothness index L, penalty coefficient λ) to adapt to varying investor risk profiles
- Extend the model to incorporate transaction costs, liquidity constraints, and dynamic market conditions
- Explore hybrid quantum-classical approaches to handle continuous or fractional portfolio allocation
- Investigate the use of web crawling techniques to integrate real-time news or trading data into the optimization model
- Assess scalability by testing the algorithm on larger portfolios (e.g., >100 assets) and diverse market conditions
- Study the impact of adiabatic evolution time on solution quality and practical runtime for large-scale problems
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
