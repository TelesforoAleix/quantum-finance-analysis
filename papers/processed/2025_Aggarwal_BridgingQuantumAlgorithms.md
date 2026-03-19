---
aliases:
- 'Bridging Quantum Algorithms and Classical Finance: Portfolio Optimization Using
  QAOA and QUBO Framework'
- Bridging Quantum Algorithms Classical
authors:
- Arnav Aggarwal
- Prerna Agarwal
- Pranav Shrivastava
- Rajneesh Kler
auto_detected: true
classification: ''
contradiction_flags: []
doi: 10.1109/UPWIECON67212.2025.11390104
evidence_type: ''
idea_tags:
- idea:quantum-advantage
- idea:near-term-feasibility
- idea:hybrid-approach
journal_or_venue: 2025 1st IEEE Uttar Pradesh Section Women in Engineering International
  Conference on Electrical Electronics and Computer Engineering (UPWIECON)
methodology_tags:
- QAOA
- QUBO
- classical-simulation
paper_type: ''
quantum_advantage_claim: speculative
related_papers: []
relevance_phase1: high
relevance_phase3: medium
source_type: conference-paper
source_type_confidence: high
step1_date: '2026-03-19T13:04:33.790869'
step1_model: Mistral-Large-3
step2_date: '2026-03-19T13:04:38.118190'
step2_model: Mistral-Large-3
step3_date: '2026-03-19T13:04:44.630063'
step3_model: Mistral-Large-3
step4_date: '2026-03-19T13:04:54.484971'
step4_model: Mistral-Large-3
step5_date: '2026-03-19T13:05:07.239016'
step5_model: Mistral-Large-3
step6_date: '2026-03-19T13:05:37.864885'
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
- method/QAOA
- method/QUBO
- method/classical-simulation
- idea/quantum-advantage
- idea/near-term-feasibility
- idea/hybrid-approach
title: 'Bridging Quantum Algorithms and Classical Finance: Portfolio Optimization
  Using QAOA and QUBO Framework'
topic_tags:
- portfolio-optimisation
year: 2025
zotero_key: ''
---

## Abstract summary
This paper investigates the application of quantum computing techniques, specifically the Quantum Approximate Optimization Algorithm (QAOA), to portfolio optimization in financial services. By reformulating the classical mean-variance optimization problem into a Quadratic Unconstrained Binary Optimization (QUBO) framework, the authors demonstrate how binary asset selection constraints can be integrated and optimized using quantum-inspired solvers. The study uses real-world data from the National Stock Exchange of India to compare quantum and classical approaches, highlighting the potential of hybrid quantum-classical models for improving financial decision-making under uncertainty.
## Methodology
The paper presents an empirical study integrating quantum computing techniques with classical portfolio optimization frameworks. The research employs the Quantum Approximate Optimization Algorithm (QAOA) within a Quadratic Unconstrained Binary Optimization (QUBO) framework to solve a binary asset selection problem derived from the classical mean-variance optimization model. The methodology involves transforming the continuous mean-variance objective into a QUBO problem by encoding expected returns and covariance-based risk profiles into a QUBO matrix. Binary decision variables are used to represent asset inclusion. The study utilizes monthly turnover data from the National Stock Exchange of India (NSE) for equity derivatives, including Index Futures, Index Options, Stock Futures, and Stock Options. Data preprocessing involved handling missing values and computing monthly returns. The QUBO problem is solved using both a classical brute-force solver and a quantum-inspired solver via QAOA implemented in Qiskit. The results from both approaches are compared, focusing on risk-adjusted performance metrics such as the Sharpe ratio.

**Algorithms used:** QAOA, QUBO
**Frameworks:** Qiskit

**Experimental setup:** The experimental setup involves a hybrid quantum-classical approach where the QAOA algorithm is implemented using the Qiskit framework. The experiments are conducted on a quantum simulator, as the paper does not specify the use of real quantum processing units (QPUs). The classical brute-force solver is used as a benchmark to validate the quantum-inspired results.

**Dataset:** Monthly turnover data from the National Stock Exchange of India (NSE) covering equity derivatives such as Index Futures, Index Options, Stock Futures, and Stock Options. The dataset spans several monthly observations, from which asset returns and covariance matrices are computed.
## Findings
- [supported] The QUBO-based portfolio optimization using QAOA and classical solvers identified that combinations including Index Futures and Index Options exhibit superior risk-adjusted performance with a Sharpe Ratio of approximately 0.286
- [supported] The hybrid quantum-classical approach using QAOA was validated against classical brute-force solvers, confirming the optimal binary asset selection for small portfolios
- [supported] Stock Options showed the highest expected monthly return (0.804489), while Index Options exhibited the lowest individual variance (4.592590) in the covariance matrix
- [speculative] The authors suggest that quantum-enhanced models may provide competitive advantages in financial decision-making, even in constrained domains, as quantum hardware matures
- [speculative] The QUBO-QAOA framework could be extended to larger asset universes and multi-objective criteria, including transaction costs and regulatory constraints
- [speculative] Quantum advantage may emerge with the scalability of quantum hardware, enabling more complex portfolio optimization models

**Results summary:** The paper demonstrates a practical integration of quantum computing techniques (QAOA) with classical portfolio optimization using a QUBO framework. The study uses monthly turnover data from the National Stock Exchange of India to construct a QUBO matrix encoding expected returns and risk profiles. The results show that portfolios combining Index Futures and Index Options achieve the best risk-adjusted returns (Sharpe Ratio ≈ 0.286). The hybrid quantum-classical approach was validated against classical brute-force solvers, confirming its viability for small-scale portfolio optimization. While the findings are promising, the authors acknowledge the limitations of current quantum hardware and suggest future scalability as hardware improves.

**Performance claims:**
- Sharpe Ratio ≈ 0.286 for the optimal portfolio (Index Futures and Index Options)
- Expected Monthly Return = 1.2747 for the optimal portfolio
- Portfolio Risk (Variance) = 19.8423 for the optimal portfolio
- QUBO Objective = 19.02987 for the optimal portfolio
- Highest expected return: Stock Options (0.804489)
- Lowest individual variance: Index Options (4.592590)
## Quantum advantage claim
**Classification:** speculative

The paper does not demonstrate quantum advantage on real hardware; all results are from simulations. The authors speculate that competitive advantages may emerge as quantum hardware scales, but this remains unvalidated empirically.
## Limitations
- Experiments limited to a small portfolio size (4 assets) due to computational constraints of brute-force enumeration and quantum-inspired solvers [inferred]
- No real quantum hardware was used; results are based on simulations and quantum-inspired classical solvers
- Dataset is limited to monthly turnover data from NSE derivatives, which may not generalize to other asset classes or markets [inferred]
- Binary asset selection constraints simplify real-world portfolio optimization, which often involves continuous weights and additional constraints (e.g., transaction costs, regulatory limits) [inferred]
- Risk aversion parameter (λ = 0.5) is arbitrarily chosen and may not reflect varying investor preferences [inferred]
- No noise mitigation techniques were applied, which would be necessary for real quantum hardware implementations [inferred]
- Page-limit constraints of the conference paper may have restricted detailed discussion of methodology and results [inferred]
- No comparison with state-of-the-art classical optimization techniques (e.g., advanced heuristic or metaheuristic methods) [inferred]
- Limited empirical validation of QAOA's performance against classical solvers for larger portfolios [inferred]
- Sharpe ratio calculations assume normal distribution of returns, which may not hold for financial derivatives [inferred]
## Open questions
- How does the QAOA-QUBO framework perform with larger asset universes (e.g., 20+ assets) where brute-force enumeration is infeasible?
- What is the impact of quantum hardware noise and decoherence on the solution quality of QAOA for portfolio optimization?
- Can the QAOA-QUBO approach outperform classical solvers in terms of computational time or solution quality for real-world portfolio sizes?
- How sensitive are the results to the choice of risk aversion parameter (λ), and how can it be optimized for different investor profiles?
- What are the implications of using binary asset selection for real-world portfolio management, where partial asset allocations are common?
- How can transaction costs, regulatory constraints, or sectoral diversification be incorporated into the QUBO framework without significantly increasing qubit requirements?
- What is the scalability of the proposed method when extended to multi-period portfolio optimization?
- How do quantum-inspired solvers compare to pure quantum simulations or real quantum hardware in terms of solution quality and runtime?

**Future work:**
- Extend the QUBO-QAOA framework to larger asset universes and evaluate scalability
- Incorporate multi-objective criteria such as transaction costs, sectoral diversification, and regulatory constraints into the QUBO formulation
- Investigate dynamic portfolio rebalancing using time-evolving QUBO matrices
- Implement the framework on real quantum hardware (e.g., IBM Q or D-Wave) and compare performance with simulations
- Explore hybrid quantum-classical approaches for adaptive and self-improving portfolio optimization models using quantum machine learning
- Conduct comparative studies across different markets (developed vs. emerging) to assess the transferability of the quantum-financial framework under varying volatility and liquidity conditions
- Develop noise mitigation strategies for QAOA to improve solution quality on near-term quantum devices
- Benchmark the QAOA-QUBO approach against advanced classical optimization techniques (e.g., genetic algorithms, simulated annealing) for larger portfolios
## Key ideas
- #idea:hybrid-approach — Reformulates mean-variance portfolio optimization into a QUBO framework, enabling integration with QAOA for binary asset selection
- #idea:quantum-advantage — Speculates that QAOA could scale to larger asset universes with multi-objective criteria as quantum hardware matures, despite current simulation-only results
- #idea:near-term-feasibility — Demonstrates consistency between QAOA (simulated) and classical brute-force solvers for small portfolios (4 assets), suggesting near-term applicability in constrained domains
- #idea:hybrid-approach — Uses classical preprocessing (e.g., covariance matrix computation) to reduce qubit requirements for quantum-enhanced portfolio optimization
- #limitation:simulation-only — All quantum results are derived from Qiskit simulations, with no empirical validation on real quantum hardware
- #limitation:qubit-count — Experiments limited to small portfolio sizes (4 assets) due to computational constraints of brute-force enumeration and quantum-inspired solvers
- #limitation:noise — No noise mitigation techniques were applied, which would be necessary for real quantum hardware implementations
## Contradictions
<!-- Step 6 output — where this paper contradicts others -->

## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
