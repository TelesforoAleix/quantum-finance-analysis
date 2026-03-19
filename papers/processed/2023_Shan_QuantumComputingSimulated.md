---
aliases:
- Quantum Computing Simulated Annealing Algorithm Applying in Portfolio Optimization
  Problem
- Quantum Computing Simulated Annealing
authors:
- Baoyuan Shana
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
step1_date: '2026-03-18T22:30:57.797307'
step1_model: Mistral-Large-3
step2_date: '2026-03-18T22:31:01.050060'
step2_model: Mistral-Large-3
step3_date: '2026-03-18T22:31:09.270376'
step3_model: Mistral-Large-3
step4_date: '2026-03-18T22:31:14.583289'
step4_model: Mistral-Large-3
step5_date: '2026-03-18T22:31:24.820777'
step5_model: Mistral-Large-3
step6_date: '2026-03-18T22:31:28.036783'
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
This paper explores the application of quantum annealing algorithms to portfolio optimization in financial services. The authors propose a quantum computing-based framework to model and solve portfolio investment problems, leveraging quantum tunneling effects to escape local optima and improve solution efficiency. The study integrates modern portfolio theory and demonstrates the approach using real stock price trends, aiming to enhance investment decision-making for individual investors with limited funds.
## Methodology
The paper proposes a quantum annealing (QA) algorithm for solving the portfolio optimization problem within the framework of Modern Portfolio Theory (MPT). The methodology involves modeling the portfolio optimization as a Quadratic Unconstrained Binary Optimization (QUBO) problem, where binary variables represent the inclusion or exclusion of stocks in the portfolio. The quantum annealing algorithm is used to escape local optima via quantum tunneling, leveraging the quantum adiabatic theorem to find the global optimum. The objective function combines return and risk metrics, adjusted by a smoothness index to reflect investor risk preferences. Constraints such as investment budget limits are incorporated using penalty functions. The algorithm is implemented via simulation in Python, and its performance is evaluated against baseline strategies, including the DOW index and stochastic buying approaches, under varying risk preferences (risk-seeking and risk-averse).

**Algorithms used:** Quantum Annealing
**Frameworks:** PyQUBO

**Experimental setup:** The quantum annealing algorithm was simulated using Python. The experiments involved constructing portfolio strategies with an investment budget of 1000, a risk-free interest rate of 2%, and varying smoothness indices for risk-seeking (200) and risk-averse (0.2) portfolios. The simulation compared the quantum annealing-based strategies with the DOW index and stochastic buying approaches.

**Dataset:** Real stock price trends from financial markets were used, though specific datasets (e.g., stock symbols, time periods) are not explicitly mentioned. The DOW index was used as a benchmark for comparison.
## Findings
- [supported] The quantum annealing algorithm was simulated in Python to optimize portfolio strategies for risk-seeking and risk-averse investors, with results showing superior performance compared to the DOW index and stochastic buying approaches
- [supported] The optimized portfolio data significantly outperformed the original data, demonstrating the effectiveness of the quantum annealing framework in portfolio optimization
- [speculative] Quantum annealing algorithms may excel in both speed and stability compared to simulated annealing algorithms when the data size is sufficiently large
- [speculative] The authors suggest that as quantum computing technology advances, quantum annealing devices could offer new possibilities for solving various optimization problems, though their genuine potential remains an open question
- [speculative] The model framework could be extended to incorporate web-crawled news or trading data to adjust stock values and provide predictive investment strategies, though this is not yet validated
- [disputed] The claim that quantum annealing algorithms are consistently superior to simulated annealing algorithms is not empirically validated in this paper and remains unclear under what conditions this holds

**Results summary:** The paper presents a quantum annealing-based framework for portfolio optimization, simulating its application for risk-seeking and risk-averse investors. The results, derived from Python simulations, show that the optimized portfolios outperformed benchmarks like the DOW index and stochastic strategies. The authors propose that quantum annealing may offer speed and stability advantages over classical simulated annealing for large datasets, though this claim is not empirically demonstrated. The study also highlights unresolved challenges, such as parameter tuning and the lack of clear conditions for quantum advantage. The framework is theoretical and simulation-based, with no real hardware validation.

**Performance claims:**
- Optimized portfolio strategies outperformed the DOW index and stochastic buying approaches in simulated tests
- Investment budget set at 1000, risk-free interest rate at 2%, with smoothness indices of 200 (risk-seeking) and 0.2 (risk-averse)
## Quantum advantage claim
**Classification:** speculative

The paper suggests potential speed and stability advantages of quantum annealing over simulated annealing for large datasets, but these claims are theoretical and based on simulation results only. No empirical validation on real quantum hardware is provided.
## Limitations
- The study relies on simulations rather than real quantum hardware, limiting insights into hardware-specific noise and decoherence effects [inferred]
- Experiments are conducted with a small investment budget (K = 1000) and synthetic parameters, which may not scale to real-world portfolio sizes or constraints [inferred]
- Binary variables (0 or 1) for stock selection restrict the model to discrete asset allocation, ignoring fractional investments common in practice [inferred]
- The paper does not compare quantum annealing performance against state-of-the-art classical optimization methods (e.g., convex solvers or heuristic algorithms) [inferred]
- Parameter tuning (e.g., smoothness index L, penalty coefficient λ) is arbitrary and lacks quantitative guidelines for investor-specific preferences
- The model assumes static stock prices and covariance matrices, ignoring dynamic market conditions and non-stationary correlations [inferred]
- No noise mitigation techniques (e.g., error correction or readout error suppression) are applied, which could degrade performance on real quantum devices [inferred]
- The study is limited to a single dataset (DOW index) and does not validate generalizability across different markets or asset classes [inferred]
- Page-limit constraints of the conference paper may have omitted detailed discussions on algorithmic convergence, failure modes, or edge cases [inferred]
- The quantum annealing framework is tailored for QUBO problems, which may not capture all constraints (e.g., transaction costs, liquidity) in real-world portfolio optimization [inferred]
## Open questions
- Under what conditions (e.g., problem size, noise levels) do quantum annealing algorithms consistently outperform simulated annealing or classical solvers?
- How can parameters (e.g., smoothness index L, penalty coefficient λ) be quantitatively optimized for investor-specific risk preferences?
- What is the impact of decoherence and hardware noise on the stability and accuracy of quantum annealing solutions for portfolio optimization?
- Can the binary asset selection model be extended to continuous or fractional allocation without sacrificing quantum advantage?
- How does the algorithm perform with larger, real-world datasets (e.g., >100 assets) or dynamic market conditions?
- What are the trade-offs between quantum annealing speedup and the overhead of embedding portfolio constraints into QUBO formulations?

**Future work:**
- Validate the model on real quantum hardware (e.g., D-Wave systems) to assess performance under noise and decoherence
- Extend the framework to multi-period portfolio optimization, incorporating dynamic rebalancing and transaction costs
- Develop adaptive parameter tuning strategies (e.g., machine learning-based) for investor-specific risk-return profiles
- Compare quantum annealing against classical solvers (e.g., Gurobi, CPLEX) and hybrid quantum-classical approaches
- Incorporate real-time market data (e.g., via web crawling) to improve predictive capabilities for stock price movements
- Explore alternative quantum algorithms (e.g., QAOA) for portfolio optimization to identify the most suitable approach
- Investigate the scalability of the model to larger asset universes and its robustness to non-stationary covariance matrices
## Key ideas
- #idea:quantum-advantage — Quantum annealing is proposed to escape local optima via quantum tunneling, potentially outperforming classical simulated annealing for large datasets
- #idea:near-term-feasibility — The paper demonstrates near-term applicability of quantum annealing for portfolio optimization using simulations, though real hardware validation is lacking
- #idea:hybrid-approach — The framework integrates classical preprocessing (e.g., QUBO formulation) with quantum annealing, suggesting a hybrid path for practical implementation
- #limitation:simulation-only — Results are derived from classical simulations, not real quantum hardware, limiting insights into noise and scalability
- #limitation:qubit-count — Binary asset selection and small investment budget (K=1000) may not scale to real-world portfolio sizes or constraints
- #limitation:no-empirical-validation — Claims of quantum advantage over simulated annealing are speculative and not empirically validated
## Contradictions
- #contradiction:classical-vs-quantum — The paper speculates that quantum annealing may outperform simulated annealing for large datasets, but this claim is disputed due to lack of empirical validation and unclear conditions for superiority (e.g., problem size, noise levels).
- #contradiction:scalability — The study uses a small investment budget and binary asset selection, which may not reflect real-world scalability challenges (e.g., fractional investments, larger asset universes).
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
