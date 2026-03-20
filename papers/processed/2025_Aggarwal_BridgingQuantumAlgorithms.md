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
- variational
- classical-simulation
paper_type: ''
quantum_advantage_claim: speculative
related_papers: []
relevance_phase1: high
relevance_phase3: medium
source_type: conference-paper
source_type_confidence: high
step1_date: '2026-03-20T00:04:50.642620'
step1_model: Mistral-Large-3
step2_date: '2026-03-20T00:05:19.893466'
step2_model: Mistral-Large-3
step3_date: '2026-03-20T00:05:28.811271'
step3_model: Mistral-Large-3
step4_date: '2026-03-20T00:05:35.277934'
step4_model: Mistral-Large-3
step5_date: '2026-03-20T00:06:26.045509'
step5_model: Mistral-Large-3
step6_date: '2026-03-20T00:06:29.493489'
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
- method/variational
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
This paper investigates the application of quantum computing techniques, specifically the Quantum Approximate Optimization Algorithm (QAOA), to classical portfolio optimization problems in finance. By reformulating the mean-variance optimization framework into a Quadratic Unconstrained Binary Optimization (QUBO) model, the study demonstrates how binary asset selection constraints can be integrated and optimized using both quantum-inspired and classical solvers. The research uses real-world data from the National Stock Exchange of India to evaluate the practical viability of hybrid quantum-classical approaches in improving financial decision-making under uncertainty.
## Methodology
The paper presents an empirical study integrating quantum computing techniques with classical portfolio optimization frameworks. Specifically, it employs the Quantum Approximate Optimization Algorithm (QAOA) within a Quadratic Unconstrained Binary Optimization (QUBO) framework to solve a binary asset selection problem for portfolio optimization. The methodology involves transforming the classical mean-variance optimization problem into a QUBO formulation by replacing continuous asset weights with binary decision variables. The study uses monthly turnover data from the National Stock Exchange of India (NSE) for equity derivatives, including Index Futures, Index Options, Stock Futures, and Stock Options. The data is preprocessed to compute expected returns and covariance matrices, which are then encoded into a QUBO matrix. The QUBO problem is solved using both a classical brute-force solver and a quantum-inspired QAOA solver implemented via Qiskit. The results from both approaches are compared to validate the quantum-enhanced method's effectiveness in optimizing risk-adjusted returns.

**Algorithms used:** QAOA
**Frameworks:** Qiskit

**Experimental setup:** The study uses a hybrid quantum-classical approach to solve the QUBO-based portfolio optimization problem. The QAOA algorithm is implemented using Qiskit, and experiments are conducted on a quantum simulator. The classical brute-force solver is used as a benchmark to validate the quantum approach.

**Dataset:** Monthly turnover data from the National Stock Exchange of India (NSE) for equity derivatives, including Index Futures, Index Options, Stock Futures, and Stock Options.
## Findings
- [supported] The QUBO-based portfolio optimization using QAOA identified that combinations of Index Futures and Index Options exhibit superior risk-adjusted performance with a Sharpe Ratio of ≈0.286
- [supported] The hybrid quantum-classical approach using QAOA was validated against classical brute-force solvers, confirming the optimal binary asset selection for small portfolios
- [supported] The QUBO matrix effectively encoded expected returns and covariance-based risk profiles, with lower QUBO values indicating more efficient portfolio combinations
- [speculative] Quantum-inspired models may offer competitive advantages in financial decision-making under uncertainty, particularly as quantum hardware scales
- [speculative] The QUBO-QAOA framework could be extended to larger asset universes and multi-objective criteria, including transaction costs and regulatory constraints
- [supported] Stock Options exhibited the highest expected monthly return (0.804489) but also the highest individual variance (8.244593), indicating higher volatility
- [supported] Classical solvers confirmed the optimal portfolio ([1, 1, 0, 0]) with an expected return of 1.2747 and portfolio risk (variance) of 19.8423

**Results summary:** The paper demonstrates a practical integration of quantum computing techniques (QAOA) with classical portfolio optimization using the QUBO framework. The study uses monthly turnover data from the National Stock Exchange of India to construct a QUBO matrix encoding expected returns and risk profiles. The results show that portfolios combining Index Futures and Index Options achieve the best risk-adjusted performance (Sharpe Ratio ≈0.286). The hybrid quantum-classical approach was validated against classical brute-force solvers, confirming its viability for small-scale portfolio optimization. While the findings are promising, the authors note that scalability to larger portfolios remains speculative due to current quantum hardware limitations.

**Performance claims:**
- Sharpe Ratio ≈0.286 for the optimal portfolio (Index Futures and Index Options)
- Expected monthly return of 1.2747 for the optimal portfolio
- Portfolio risk (variance) of 19.8423 for the optimal portfolio
- Stock Options had the highest expected return (0.804489) and highest variance (8.244593)
- QUBO objective value of 19.02987 for the optimal portfolio
## Quantum advantage claim
**Classification:** speculative

The paper suggests potential competitive advantages of quantum-inspired models in financial decision-making but does not demonstrate quantum advantage empirically. All results are derived from simulations and validated against classical solvers, with no real quantum hardware implementation.
## Limitations
- Experiments conducted only on a small portfolio of 4 assets (Index Futures, Index Options, Stock Futures, Stock Options), limiting scalability insights [inferred]
- No real quantum hardware was used; results are based on quantum-inspired solvers and classical simulations
- Page-limit constraints of the conference paper may have restricted detailed discussion of noise mitigation techniques [inferred]
- Dataset limited to monthly turnover data from NSE derivatives, which may not generalize to other asset classes or markets [inferred]
- Binary asset selection constraints (e.g., fixed number of assets) may not fully capture real-world portfolio optimization scenarios
- No empirical validation on actual quantum hardware (e.g., IBM Q, D-Wave) to assess performance under hardware noise
- Risk aversion parameter (λ = 0.5) was arbitrarily chosen without sensitivity analysis [inferred]
- Lack of comparison with state-of-the-art classical optimization techniques beyond brute-force enumeration [inferred]
- No discussion of quantum circuit depth or gate complexity, which could limit practical implementation on near-term devices [inferred]
- Potential overfitting due to small dataset size (monthly observations) [inferred]
## Open questions
- How does the QAOA-QUBO framework perform with larger asset universes (e.g., 50+ assets)?
- What is the impact of quantum hardware noise (e.g., decoherence, gate errors) on solution quality?
- Can the framework handle dynamic portfolio rebalancing with time-evolving QUBO matrices?
- How do transaction costs, regulatory constraints, or sectoral diversification affect the QUBO formulation?
- What is the trade-off between quantum circuit depth and solution accuracy for this problem?
- How does the performance of QAOA compare to other quantum algorithms (e.g., VQE, Grover Adaptive Search) for portfolio optimization?
- Can quantum machine learning techniques improve adaptive portfolio optimization in this framework?

**Future work:**
- Extend the QUBO-QAOA framework to larger asset universes
- Incorporate multi-objective criteria such as transaction costs, diversification, and regulatory constraints
- Investigate dynamic portfolio rebalancing using time-evolving QUBO matrices
- Explore real-time implementation on quantum simulators or hardware (e.g., IBM Q, D-Wave)
- Apply quantum machine learning to develop adaptive and self-improving portfolio optimization models
- Conduct comparative studies across markets (developed vs. emerging) to assess transferability
- Benchmark against other quantum algorithms (e.g., VQE) and classical solvers (e.g., simulated annealing, genetic algorithms)
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

## Experiment details
### Input
The dataset includes monthly turnover figures for four financial derivative instruments from the NSE. The data spans several months, with non-numeric entries and missing values removed or imputed. Monthly returns are computed as percentage changes in turnover values, resulting in expected returns (μ) and a covariance matrix (Σ). The dataset consists of 4 assets with computed returns and covariance values.

### Process
1. Preprocess the NSE turnover data to compute monthly returns and covariance matrix. 2. Formulate the QUBO matrix by encoding expected returns and covariance-based risk profiles, modulated by a risk aversion parameter (λ = 0.5). 3. Solve the QUBO problem using a classical brute-force solver to evaluate all possible asset combinations. 4. Implement QAOA via Qiskit to solve the QUBO problem iteratively, adjusting quantum circuit parameters to minimize the QUBO objective. 5. Compare the optimal asset combinations identified by both methods.

### Output
The output includes the optimal binary asset selection (e.g., [1, 1, 0, 0] for Index Futures and Index Options), expected portfolio returns, portfolio risk (variance), QUBO objective values, and Sharpe ratios. The results are compared against all possible 2-asset combinations to evaluate risk-adjusted performance.

### Parameters
- risk_aversion_parameter: 0.5
- assets: 4
- portfolio_size_constraint: 2
- optimizer: Not explicitly mentioned, but QAOA typically involves classical optimizers like COBYLA or SPSA

### Hardware
The QAOA implementation is run on a quantum simulator using Qiskit. No specific details about the simulator or hardware (e.g., qubit count, noise model) are provided.

### Reproducibility
The paper provides sufficient detail about the dataset preprocessing, QUBO formulation, and algorithmic steps to replicate the study. However, no explicit mention of code or data availability is made. The use of Qiskit suggests that the quantum implementation could be replicated with additional details on parameters and hardware settings.
