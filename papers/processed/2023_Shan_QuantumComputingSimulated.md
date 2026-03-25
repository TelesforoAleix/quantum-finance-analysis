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
step1_date: '2026-03-25T16:01:46.512126'
step1_model: gpt-5.1
step2_date: '2026-03-25T16:01:51.046160'
step2_model: gpt-5.1
step3_date: '2026-03-25T16:02:15.251603'
step3_model: gpt-5.4
step4_date: '2026-03-25T16:02:29.104437'
step4_model: gpt-5.4
step5_date: '2026-03-25T16:02:49.681193'
step5_model: gpt-5.4
step6_date: '2026-03-25T16:03:02.051385'
step6_model: gpt-5.4
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
The paper develops a quantum annealing based modelling and solution framework for portfolio optimization grounded in modern portfolio theory. It formulates the portfolio selection problem as a QUBO, incorporates budget and risk constraints via penalty terms, and implements the approach in Python to construct risk-seeking and risk-averse strategies. The authors compare these quantum-annealing-derived portfolios to benchmarks such as the DOW index and random strategies, and discuss open issues around parameter tuning and conditions under which quantum annealing outperforms classical simulated annealing.
## Methodology
This conference paper presents a modelling study for portfolio optimization using a quantum annealing-inspired approach formulated as a QUBO problem under modern portfolio theory. The authors define stock return as the relative change between purchase and sale prices, model portfolio return as a weighted sum over binary stock-selection variables, and model risk using pairwise stock covariances. These are combined into a scalar objective that trades off return and risk through a smoothness index L, then augmented with a quadratic penalty term to enforce an investment budget constraint, yielding a QUBO-style objective. The paper also outlines a generic quantum annealing procedure based on a Hamiltonian composed of potential and kinetic terms, with iterative state perturbation, energy-difference-based acceptance, and gradual reduction of transverse field strength. For implementation, the authors state that Python was used to simulate the quantum annealing algorithm and generate two portfolio strategies corresponding to risk-seeking and risk-averse investors. The resulting portfolio return and asset trend time series were compared visually against a DOW index investment strategy and a stochastic buying strategy. The paper appears to be a conference paper and is primarily a simulation/modeling study rather than an experiment on real quantum hardware.

**Algorithms used:** Quantum Annealing, QUBO
**Frameworks:** Python

**Experimental setup:** The study used a Python-based simulation of the quantum annealing algorithm. No real quantum processing unit, annealer, or named simulator platform is reported. Two simulated portfolio strategies were constructed: risk-seeking and risk-averse.

**Dataset:** Real stock price trends from financial markets are referenced, and results are compared with the DOW index and a stochastic buying strategy. However, the paper does not clearly specify the exact stock universe, source, sample size, or time horizon of the stock data.
## Findings
- [supported] The paper formulates portfolio optimization as a QUBO-style objective combining return, covariance-based risk, a budget penalty term, and a risk-free rate term.
- [supported] The implementation was performed in Python as a simulation of a quantum annealing algorithm rather than on real quantum hardware.
- [supported] The study constructed two portfolio strategies by varying the smoothness index: a risk-seeking portfolio with L=200 and a risk-averse portfolio with L=0.2.
- [supported] In the reported experiment, the investment budget was set to K=1000 and the risk-free interest rate to r=2%.
- [supported] The authors report that the optimized portfolio data outperformed the original data and that parameter changes could reflect different investor preferences, but they do not provide numerical performance metrics.
- [speculative] The paper argues that quantum annealing can use quantum tunnelling to escape local optima and improve the chance of reaching a global optimum in portfolio optimization.
- [speculative] The authors suggest that quantum annealing may significantly improve the efficiency and effectiveness of portfolio optimization solutions.
- [speculative] The conclusion claims quantum annealing appears superior to simulated annealing in speed and stability when data size is sufficiently large, but no direct benchmark results are reported in the paper.
- [supported] The authors explicitly note unresolved issues, including how to choose parameters quantitatively and under what conditions quantum annealing is consistently superior to simulated annealing.
- [supported] The paper states that the current optimization model is not sufficient for predictive investment strategy generation because stock prices are influenced by many factors.

**Results summary:** This conference paper presents a simulated quantum annealing framework for portfolio optimization based on modern portfolio theory and a QUBO-like formulation. The model combines stock returns, covariance-based risk, and a budget constraint enforced through a penalty term. The authors implemented the approach in Python simulation and generated two portfolio strategies corresponding to risk-seeking and risk-averse preferences by changing the smoothness index. They compare portfolio return trends visually against the DOW index and a stochastic buying strategy, and conclude qualitatively that the optimized data outperformed the original data and can reflect investor preferences. However, the paper does not report quantitative benchmark metrics, confidence intervals, or direct empirical comparisons against simulated annealing or real quantum hardware.

**Performance claims:**
- Python simulation of quantum annealing with investment budget K=1000
- Risk-free interest rate set to r=2%
- Risk-seeking smoothness index L=200
- Risk-averse smoothness index L=0.2
## Quantum advantage claim
**Classification:** speculative

The paper suggests quantum annealing may improve efficiency, stability, and speed, especially for large datasets, but provides no quantitative benchmark against classical methods and uses simulation rather than real quantum hardware.
## Limitations
- Determining how to adjust model parameters or provide quantitative parameter-setting strategies remains unresolved
- It is unclear under what conditions quantum annealing algorithms are consistently superior to simulated annealing algorithms
- The model is not yet sufficient for predicting investment portfolio strategies because stock prices are influenced by many factors
- The paper only reports a Python simulation of the quantum annealing algorithm rather than execution on actual quantum annealing hardware
- [inferred] No empirical comparison against strong classical portfolio optimization baselines is provided beyond DOW index and stochastic buying references
- [inferred] Experimental evaluation appears limited in scale, with no evidence of large asset universes, long horizons, or stress tests for scalability
- [inferred] The study uses a simplified binary stock-selection formulation, which may not capture realistic portfolio allocation with continuous weights, transaction costs, turnover, liquidity, or cardinality constraints
- [inferred] The choice of key hyperparameters such as the smoothness index and penalty coefficient is not systematically justified, which may affect internal validity
- [inferred] No discussion of hardware noise, embedding constraints, qubit count limits, or chain breaks is included, limiting practical relevance to near-term quantum devices
- [inferred] Reproducibility is limited because the paper does not provide sufficient implementation details, datasets, code, or exact experimental settings
- [inferred] Results appear to rely on a narrow experimental setup and possibly a single market context, limiting generalizability
- [inferred] The conference-paper format may have constrained methodological detail, experimental reporting, and ablation analysis
## Open questions
- How should the model parameters be adjusted in a principled and quantitative way for different investor preferences and market conditions?
- Under what conditions are quantum annealing algorithms consistently better than simulated annealing algorithms?
- What is the genuine practical potential of increasingly sophisticated quantum annealing devices for portfolio optimization and other optimization problems?
- Can quantum-computing-based portfolio optimization be extended from fitting historical data to producing reliable predictive investment strategies?
- How can external information such as news or trading data be incorporated effectively into the optimization framework?
- [inferred] How does the approach perform on larger and more realistic portfolio instances with many assets and constraints?
- [inferred] Would any observed advantage remain after comparison with state-of-the-art classical solvers and heuristics?
- [inferred] How robust are the results to different choices of penalty weights, budget levels, risk-free rates, and smoothness parameters?
- [inferred] How well would the QUBO formulation map to real quantum annealers with limited connectivity and noisy hardware?

**Future work:**
- Develop quantitative strategies for tuning model parameters
- Investigate the conditions under which quantum annealing outperforms simulated annealing
- Explore the feasibility of using web crawling to retrieve stock-related news information or trading data
- Adjust stock values based on positive or negative external information to support predictive portfolio strategies
- Continue modelling studies to better understand the use of quantum computing techniques for complex financial optimization problems
- [inferred] Validate the method on actual quantum annealing hardware rather than only in Python simulation
- [inferred] Benchmark against stronger classical optimization methods and simulated annealing baselines on standardized datasets
- [inferred] Extend the portfolio model to include more realistic financial constraints and objectives, such as transaction costs, rebalancing, and continuous allocations
- [inferred] Test the framework on larger, real-world datasets across multiple market regimes to assess scalability and robustness
- [inferred] Improve reproducibility by releasing code, data sources, and full experimental settings
## Key ideas
- #idea:hybrid-approach — The paper formulates modern portfolio optimization as a QUBO with return, covariance-based risk, and budget-penalty terms, then solves it via a simulated quantum annealing workflow.
- #idea:near-term-feasibility — The study presents a Python-based annealing simulation to generate risk-seeking and risk-averse portfolio strategies, positioning the approach as an early practical exploration rather than a hardware demonstration.
- #idea:quantum-advantage — The authors argue that quantum annealing could exploit tunnelling to escape local optima and potentially outperform simulated annealing in speed, stability, and solution quality on large portfolio problems.
## Contradictions
- The paper suggests quantum annealing may be superior to simulated annealing, but this is not empirically established because the study reports only Python simulation results, no direct benchmark against strong classical solvers, and no real QPU execution.
- The paper implies scalability to larger portfolio problems, yet the evaluation uses a simplified binary stock-selection model with limited experimental detail, no evidence of large asset universes, and no demonstration of mapping to real annealing hardware constraints.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->

## Experiment details
### Input
Input consists of stock purchase prices, sale prices over time, binary stock-selection variables, and covariance estimates between stocks. The paper references real market stock price trends and comparison to the DOW index, but does not provide the data source, number of stocks, observation period, feature count, or preprocessing details.

### Process
1. Define stock returns from purchase and sale prices. 2. Compute portfolio return as a sum over binary stock-selection variables. 3. Compute portfolio risk using pairwise covariance terms. 4. Form a combined objective balancing return and risk via smoothness index L. 5. Add a quadratic penalty term to enforce the investment budget constraint and obtain a QUBO-style objective. 6. Simulate a quantum annealing procedure in Python using Hamiltonian-based state updates, random perturbations, energy-difference acceptance criteria, and annealing of the transverse field strength until termination. 7. Run the model under two parameter settings representing risk-seeking and risk-averse investors. 8. Compare resulting portfolio return and trend series against DOW index investing and stochastic buying. The paper does not report iteration counts, stopping tolerances beyond the generic algorithm description, or sampling/shots.

### Output
Outputs are portfolio return and rate-of-return time series for risk-seeking and risk-averse strategies, shown graphically and compared against a DOW index fund strategy and a stochastic buying baseline. The paper claims the optimized data significantly outperformed the original data, but does not report standard quantitative evaluation metrics such as Sharpe ratio, volatility, drawdown, or statistical significance.

### Parameters
- investment_budget_K: 1000
- risk_free_interest_rate_r: 0.02
- smoothness_index_risk_seeking_Ls: 200
- smoothness_index_risk_averse_La: 0.2
- max_steps: mentioned symbolically as MaxSteps, exact value not reported
- transverse_field_strength: Gamma, annealed during optimization; initial value not reported
- penalty_coefficient: lambda, included in objective but numeric value not reported

### Hardware
{'hardware_type': 'classical simulation', 'implementation_environment': 'Python', 'qpu_model': None, 'simulator_name': None, 'cloud_provider': None, 'transpilation_settings': None}

### Reproducibility
Reproducibility is limited. The paper provides the mathematical formulation and some parameter values (budget, risk-free rate, smoothness indices), but omits key details such as the exact dataset, stock universe, time period, covariance estimation procedure, annealing schedule values, iteration settings, and source code. No code or data repository is mentioned.
