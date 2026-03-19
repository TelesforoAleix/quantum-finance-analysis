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
step1_date: '2026-03-18T23:22:48.143570'
step1_model: Mistral-Large-3
step2_date: '2026-03-18T23:22:54.171617'
step2_model: Mistral-Large-3
step3_date: '2026-03-18T23:23:06.427212'
step3_model: Mistral-Large-3
step4_date: '2026-03-18T23:23:15.178567'
step4_model: Mistral-Large-3
step5_date: '2026-03-18T23:23:24.688555'
step5_model: Mistral-Large-3
step6_date: '2026-03-18T23:23:28.885123'
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
This paper investigates the application of quantum computing techniques, specifically the Quantum Approximate Optimization Algorithm (QAOA), to portfolio optimization in financial services. By reformulating the classical mean-variance portfolio problem into a Quadratic Unconstrained Binary Optimization (QUBO) framework, the authors demonstrate how binary asset selection constraints can be optimized using quantum-inspired solvers. The study uses real-world data from the National Stock Exchange of India to compare quantum and classical approaches, highlighting the potential of hybrid quantum-classical models to enhance financial decision-making under uncertainty.
## Methodology
The paper presents an empirical study integrating quantum computing techniques with classical portfolio optimization frameworks. Specifically, it employs the Quantum Approximate Optimization Algorithm (QAOA) within a Quadratic Unconstrained Binary Optimization (QUBO) framework to solve a binary asset selection problem in portfolio optimization. The classical mean-variance optimization model is reformulated into a QUBO problem by replacing continuous asset weights with binary decision variables. The study uses monthly turnover data from the National Stock Exchange of India (NSE) for equity derivatives, including Index Futures, Index Options, Stock Futures, and Stock Options, to compute expected returns and covariance matrices. The QUBO matrix is constructed by encoding expected returns and risk profiles, modulated by a risk aversion parameter. The methodology involves solving the QUBO problem using both a classical brute-force solver and a quantum-inspired solver (QAOA implemented via Qiskit). The results from both approaches are compared to validate the quantum-enhanced method's effectiveness in optimizing risk-adjusted returns (Sharpe Ratio).

**Algorithms used:** QAOA
**Frameworks:** Qiskit

**Experimental setup:** The QAOA algorithm was implemented using the Qiskit framework. The experiments were conducted on a quantum simulator, as the paper does not mention the use of real quantum processing units (QPUs). The classical brute-force solver was used as a benchmark to validate the quantum-inspired results.

**Dataset:** Monthly turnover data from the National Stock Exchange of India (NSE) for equity derivatives, including Index Futures, Index Options, Stock Futures, and Stock Options. The dataset was preprocessed to compute monthly returns, expected returns (μ), and covariance matrices (Σ).
## Findings
- [supported] The QUBO framework successfully reformulates the mean-variance portfolio optimization problem into a binary decision space, enabling integration with quantum algorithms like QAOA
- [supported] Combinations of Index Futures and Index Options exhibit superior risk-adjusted performance with a Sharpe Ratio of ≈0.286, the highest among evaluated portfolios
- [supported] The hybrid quantum-classical approach using QAOA (simulated via Qiskit) produced results consistent with classical brute-force solvers for small portfolios (4 assets, 2-asset combinations)
- [supported] The QUBO matrix effectively encodes both expected returns and covariance-based risk, with lower values indicating more optimal asset combinations for portfolio selection
- [speculative] Quantum-enhanced models may provide competitive advantages in portfolio optimization, even in constrained domains, as quantum hardware matures
- [speculative] The QUBO-QAOA framework could scale to larger asset universes with multi-objective criteria (e.g., transaction costs, regulatory constraints) as quantum hardware improves
- [speculative] Dynamic portfolio rebalancing using time-evolving QUBO matrices could be feasible with real-time implementation on quantum hardware

**Results summary:** The paper demonstrates a practical integration of quantum computing techniques (QAOA) with classical portfolio optimization via the QUBO framework. Using monthly turnover data from the NSE, the authors encode expected returns and covariance-based risk into a QUBO matrix and solve the binary asset selection problem using both classical brute-force methods and quantum-inspired solvers. Results show that Index Futures and Index Options combinations yield the best risk-adjusted returns (Sharpe Ratio ≈0.286). While the quantum approach (simulated) matches classical solver performance for small portfolios, the authors argue that quantum-enhanced models could offer advantages in scalability and complexity handling as hardware improves.

**Performance claims:**
- Sharpe Ratio ≈0.286 for Index Futures + Index Options portfolio (highest among evaluated combinations)
- QUBO objective value of 19.03 for the optimal portfolio (lowest among all 2-asset combinations)
- Portfolio risk (variance) of 19.8423 for the optimal portfolio
- Expected monthly return of 1.2747 for the optimal portfolio
- Consistency between QAOA (simulated) and classical brute-force results for 4-asset, 2-asset selection problems
## Quantum advantage claim
**Classification:** speculative

The paper does not demonstrate quantum advantage empirically; all quantum results are from simulation (Qiskit). The claimed advantage is theoretical, based on the potential scalability of QAOA for larger portfolios as quantum hardware improves. No comparison with state-of-the-art classical methods for larger problem sizes is provided.
## Limitations
- Experiments limited to a small portfolio size (4 assets) due to computational constraints of brute-force enumeration and quantum simulation
- No real quantum hardware was used; results are based on quantum-inspired solvers and simulations [inferred]
- Dataset is limited to monthly turnover data from NSE derivatives, which may not generalize to other asset classes or markets
- Binary asset selection constraints (0/1) may oversimplify real-world portfolio optimization where fractional asset weights are common
- Risk aversion parameter (λ = 0.5) is arbitrarily chosen and may not reflect varying investor preferences
- No noise mitigation techniques were applied, which could affect performance on real quantum hardware [inferred]
- Page-limit constraints of the conference paper may have restricted detailed discussion of methodology and results [inferred]
- Lack of comparison with state-of-the-art classical optimization techniques beyond brute-force enumeration [inferred]
- No empirical validation of QAOA performance on actual quantum processors (e.g., IBM Q, D-Wave) [inferred]
- Covariance matrix and expected returns are based on historical data, which may not predict future performance
## Open questions
- How does the QAOA-QUBO framework perform with larger asset universes (e.g., 20+ assets)?
- What is the impact of quantum hardware noise and decoherence on the solution quality of QAOA for portfolio optimization?
- Can the framework handle dynamic portfolio rebalancing with time-evolving QUBO matrices?
- How would transaction costs, regulatory constraints, or sectoral diversification affect the QUBO formulation and QAOA performance?
- What are the computational advantages of QAOA over classical solvers for portfolio optimization in terms of speed and scalability?
- How transferable is the quantum-financial framework across different markets (e.g., developed vs. emerging markets) with varying volatility and liquidity conditions?

**Future work:**
- Extend the QUBO-QAOA framework to larger asset universes
- Incorporate multi-objective criteria such as transaction costs, diversification, and regulatory constraints
- Investigate dynamic portfolio rebalancing using time-evolving QUBO matrices
- Explore real-time implementation on quantum simulators or hardware (e.g., IBM Q, D-Wave)
- Apply quantum machine learning to develop adaptive and self-improving portfolio optimization models
- Conduct comparative studies across different markets to assess the transferability of the framework
- Benchmark QAOA performance against state-of-the-art classical optimization techniques
- Validate the framework on real quantum hardware to assess noise resilience and practical applicability
## Key ideas
- #idea:hybrid-approach — Reformulates mean-variance portfolio optimization into a QUBO framework, enabling integration with QAOA for binary asset selection
- #idea:quantum-advantage — Speculates that QAOA could scale to larger asset universes with multi-objective criteria as quantum hardware matures, despite current simulation-only results
- #idea:near-term-feasibility — Demonstrates consistency between QAOA (simulated) and classical brute-force solvers for small portfolios (4 assets), suggesting near-term applicability in constrained domains
- #idea:hybrid-approach — Uses classical preprocessing (e.g., covariance matrix computation) to reduce qubit requirements for quantum-enhanced portfolio optimization
- #limitation:simulation-only — All quantum results are derived from Qiskit simulations, with no empirical validation on real quantum hardware
## Contradictions
<!-- Step 6 output — where this paper contradicts others -->

## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
