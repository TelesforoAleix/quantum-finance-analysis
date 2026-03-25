---
aliases:
- Portfolio Optimization on Classical and Quantum Computers Using PortFawn
- Portfolio Optimization Classical Quantum
authors:
- Moein Owhadi-Kareshk
- Pierre Boulanger
auto_detected: true
classification: ''
contradiction_flags:
- contradiction:classical-vs-quantum
- contradiction:scalability
doi: ''
evidence_type: ''
idea_tags:
- idea:quantum-advantage
- idea:near-term-feasibility
- idea:hybrid-approach
journal_or_venue: arXiv
methodology_tags:
- quantum-annealing
- QUBO
paper_type: ''
quantum_advantage_claim: speculative
related_papers: []
relevance_phase1: high
relevance_phase3: medium
source_type: preprint
source_type_confidence: high
step1_date: '2026-03-25T15:55:07.711816'
step1_model: gpt-5.1
step2_date: '2026-03-25T15:55:11.833826'
step2_model: gpt-5.1
step3_date: '2026-03-25T15:55:53.396992'
step3_model: gpt-5.4
step4_date: '2026-03-25T15:56:17.492663'
step4_model: gpt-5.4
step5_date: '2026-03-25T15:56:48.767391'
step5_model: gpt-5.4
step6_date: '2026-03-25T15:57:02.107616'
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
- idea/quantum-advantage
- idea/near-term-feasibility
- idea/hybrid-approach
- contradiction/classical-vs-quantum
- contradiction/scalability
title: Portfolio Optimization on Classical and Quantum Computers Using PortFawn
topic_tags:
- portfolio-optimisation
year: 2021
zotero_key: ''
---

## Abstract summary
The paper presents PortFawn, an open-source Python library for constructing and backtesting mean-variance portfolios under a variety of objectives and constraints. It supports both classical optimization with real-valued weights and quantum annealing formulations using QUBO with binary weights, enabling experimentation with quantum hardware for portfolio selection. The authors describe the architecture and capabilities of the tool and illustrate its use through a backtesting study on ETF portfolios over several years.
## Methodology
This preprint presents PortFawn, an open-source Python library for constructing and backtesting mean-variance portfolios on both classical and quantum computing platforms. Methodologically, the paper is primarily an empirical software-and-demonstration study built on the Markowitz framework. The workflow implemented by the library consists of: collecting historical asset prices for a user-specified universe of securities; computing returns, covariance/correlation statistics, and expected return/risk estimates; solving portfolio optimization problems under several objectives; and evaluating the resulting portfolios through rolling-window backtesting. On the classical side, the library supports equal-weighted, minimum-volatility, maximum-return, and maximum-Sharpe-ratio portfolios with real-valued long-only weights and full-investment constraints. On the quantum side, the paper reformulates a multi-objective portfolio optimization problem as a QUBO and solves a binary long-only asset-selection version, called Binary Multi-Objective Portfolio (BMOP), using quantum annealing. The empirical illustration uses nine iShares ETFs from 2015-01-01 to 2020-12-31, with 40-day training windows and 5-day out-of-sample testing windows in overlapping rolling backtests. The study compares cumulative returns, return distributions, correlations, and risk-return positioning of the resulting portfolios, mainly to demonstrate the functionality of the PortFawn framework rather than to establish a rigorous quantum advantage. As a preprint, it should be treated as non-peer-reviewed.

**Algorithms used:** Mean-Variance Portfolio Optimization, Minimum Volatility Portfolio (MVP), Maximum Return Portfolio (MRP), Maximum Sharpe Ratio Portfolio (MSRP), Equal-Weighted Portfolio (EWP), Market Capitalization Portfolio (MCP), Multi-Objective Portfolio (MOP), Binary Multi-Objective Portfolio (BMOP), QUBO, Quantum Annealing
**Frameworks:** PortFawn, Python, D-Wave Ocean, yfinance

**Experimental setup:** The paper evaluates the PortFawn library in a rolling backtesting scenario comparing classical portfolio optimization methods with a quantum-annealing-based binary portfolio formulation. Historical ETF price data are collected via yfinance, processed within PortFawn classes (MarketData, ExpectedStats, Portfolio, BackTest), and portfolios are generated repeatedly over overlapping windows. The authors state that they used a D-Wave quantum computer through a developer account and the Ocean software infrastructure as part of the evaluation. Classical optimization is used for real-valued portfolios, while the quantum setup solves a QUBO-based binary portfolio selection problem.

**Dataset:** Historical daily price data for nine iShares ETFs listed in the U.S., covering January 1, 2015 to December 31, 2020. The assets span U.S. equities, small-cap equities, global ex-U.S. equities, emerging markets, global REITs, U.S. real estate, corporate bonds, aggregate bonds, and gold.
## Experiment details
### Input
Input data consist of daily historical prices for 9 ETFs: IVV, IJR, ACWX, IEMG, REET, IYR, HYG, AGG, and IAU, from 2015-01-01 to 2020-12-31, sourced via yfinance. Returns are computed from price changes using simple returns. The backtest uses overlapping rolling windows with 40 trading days for portfolio construction/training and 5 days for out-of-sample evaluation. Expected returns and covariance can be estimated using one of three modes supported by the library: full-sample mean/covariance, random subwindow aggregation via median, or weighted random subwindow aggregation emphasizing recent returns. In the illustrative example, daily returns are used, risk-free rate is set to 0%, target return is 20.0%, target volatility is 5.0%, and asset weight bounds are 2.0% to 98.0%.

### Process
1. Select a universe of 9 ETFs and a backtesting period from 2015-01-01 to 2020-12-31. 2. Download and cache historical price data using the MarketData class and compute daily returns, cumulative returns, covariance, and correlation statistics. 3. Estimate expected returns and risks from the training window using the library's expected-statistics module. 4. Construct portfolios under different objectives: equal-weighted (EWP), minimum volatility (MVP), maximum return (MRP), maximum Sharpe ratio (MSRP), and a binary multi-objective portfolio (BMOP). 5. For classical portfolios, solve the corresponding constrained mean-variance optimization problems with real-valued long-only weights summing to one. 6. For the quantum portfolio, map the multi-objective formulation to a QUBO with diagonal terms Qii = -lambda*ri and off-diagonal terms Qij = sigma_ij, set lambda = 1 for simplicity, and solve the binary asset-selection problem using quantum annealing on D-Wave; constraints are handled by weight normalization after selection. 7. Repeat portfolio formation and out-of-sample testing over overlapping rolling windows using 40-day training and 5-day testing periods. 8. Aggregate and visualize results through cumulative return plots, return-distribution plots, portfolio correlation matrices, and expected-return-versus-volatility charts including the efficient frontier.

### Output
The outputs are portfolio performance summaries and visual comparisons rather than formal statistical tests. Reported outputs include cumulative portfolio returns over time, distributions of daily portfolio returns, correlations among portfolio return series, and annualized volatility versus expected return plots for both assets and portfolios. The study compares EWP, MRP, MVP, MSRP, and BMOP. Qualitative findings reported include that MRP has the highest returns, MVP has the lowest volatility, MSRP provides a balance between return and risk, and BMOP performs well despite binary weights. No formal hypothesis testing, runtime benchmarking, or quantum-versus-classical optimality-gap analysis is reported.

### Parameters
- assets_count: 9
- training_window_days: 40
- testing_window_days: 5
- backtesting_start_date: 2015-01-01
- backtesting_end_date: 2020-12-31
- returns_frequency: daily
- risk_free_rate: 0.0
- target_return: 0.2
- target_volatility: 0.05
- lower_bound_asset_weight: 0.02
- upper_bound_asset_weight: 0.98
- quantum_formulation: QUBO
- quantum_lambda: 1
- weight_type_classical: real-valued
- weight_type_quantum: binary

### Hardware
Quantum experiments were run using a D-Wave quantum computer via a developer account, with the D-Wave Ocean software infrastructure. The paper does not specify the exact QPU model, topology, number of reads/shots, embedding strategy, annealing schedule, chain strength, or other solver/transpilation settings. Classical computations were performed within the PortFawn Python environment, but no CPU/GPU specifications are given.

### Reproducibility
Code is publicly available on GitHub under the MIT License, and the paper states that documentation, logging, unit tests, and integration tests are provided. Data are obtainable from public market sources via yfinance, so the dataset is largely reproducible. However, exact replication of the quantum results may be limited because the paper omits important D-Wave solver settings (e.g., QPU model, annealing parameters, reads, embedding details). Overall reproducibility is moderate: strong for the software pipeline and classical backtest, weaker for the quantum execution details.
## Findings
- [supported] The paper introduces PortFawn, an open-source Python library for creating and backtesting mean-variance portfolios using both classical optimization with real-valued weights and quantum annealing with binary weights.
- [supported] PortFawn implements a full workflow including market data collection, expected return/risk estimation, portfolio construction, backtesting, logging, visualization, and testing infrastructure.
- [supported] The illustrative experiment uses nine iShares ETFs from 2015-01-01 to 2020-12-31 with rolling windows of 40 training days and 5 testing days.
- [supported] In the backtest, the minimum-volatility portfolio exhibited lower volatility than the other portfolios, while the maximum-return portfolio exhibited the highest returns among the classical mean-variance portfolios.
- [supported] The binary multi-objective portfolio (BMOP) solved via D-Wave quantum annealing produced strong cumulative-return performance in the illustrative example and is described as having among the highest returns in the plotted results.
- [speculative] The authors suggest that BMOP's performance shows potential for using quantum computers in portfolio optimization.
- [speculative] The paper claims quantum solvers have a higher chance of finding global minima than classical solvers because of quantum tunneling, but this is not empirically validated in the paper.
- [supported] Equal-weighted portfolios delivered acceptable return and volatility in the example, suggesting a simple baseline can remain competitive in some scenarios.
- [supported] The paper identifies that aggregate bonds and gold had relatively low correlation with the other selected assets, making them useful diversifiers in the example dataset.
- [supported] The paper emphasizes several practical limitations of standard mean-variance optimization, including unrealistic assumptions about liquidity, transaction costs, i.i.d. returns, omission of dividends, and concentration in a few assets.

**Results summary:** This preprint presents PortFawn, an open-source research library for classical and quantum-annealing-based mean-variance portfolio optimization and backtesting. In an illustrative backtest on nine ETFs over 2015-2020 using rolling 40-day training and 5-day testing windows, the expected qualitative behavior of the portfolio types was observed: the minimum-volatility portfolio had the lowest volatility, the maximum-return portfolio had the highest classical returns, and the maximum-Sharpe portfolio provided a balance between risk and return. A binary multi-objective portfolio implemented as a QUBO and run on D-Wave hardware also performed well in the example, but the paper does not provide rigorous benchmarking against classical solvers, statistical significance tests, or evidence of quantum advantage. Overall, the contribution is primarily a software/tooling framework and demonstration rather than a validated performance study of quantum computing in finance.

**Performance claims:**
- Backtest period: 2015-01-01 to 2020-12-31
- Number of assets: 9 ETFs
- Training window: 40 days
- Testing window: 5 days
- Risk-free rate used for Sharpe ratio: 0.0%
- Target return for minimum-volatility formulation: 20.0%
- Target volatility for maximum-return formulation: 5.0%
- Lower bound asset weight: 2.0%
- Upper bound asset weight: 98.0%
- Portfolio return correlations shown include MSRP-EWP: 0.75, EWP-MRP: 0.97, MSRP-BMOP: 0.87, EWP-BMOP: 0.85, MRP-BMOP: 0.79, MVP-BMOP: 0.70
- Asset return correlations shown include Global REIT-U.S. Real Estate: 0.94, Aggregate Bond-S&P 500: -0.02, Gold-Aggregate Bond: 0.35
## Quantum advantage claim
**Classification:** speculative

As a preprint, claims of quantum benefit default to speculative. The paper uses D-Wave hardware for an illustrative binary portfolio example and reports qualitatively good performance, but it does not demonstrate a rigorous speedup or superior solution quality over classical baselines with controlled benchmarking or statistical evidence.
## Limitations
- The paper is a preprint and has not undergone peer review.
- The mean-variance framework relies on unrealistic assumptions, including i.i.d. normally distributed returns characterized only by means and variances.
- The approach assumes that historical mean returns and covariance estimated over a past window are good predictors of future performance, which the authors note is a very strong generalization and not always valid.
- The original mean-variance model assumes full asset liquidity, which may not hold outside large-cap assets in developed markets.
- The model ignores turnover, transaction, and management costs, which can make backtest performance unrealistic relative to practice.
- The formulation ignores dividends, making return calculations unrealistic for high-dividend assets.
- The optimization tends to produce concentrated portfolios in a small number of assets, which may be undesirable in practice.
- The quantum annealing formulation uses binary asset weights rather than real-valued weights, limiting expressiveness relative to standard portfolio allocation.
- For the quantum version, the paper uses a simplified Binary Multi-Objective Portfolio with λ = 1 for simplicity, reducing generality.
- The illustrative experiment is limited to nine ETFs from 2015 to 2020.
- The backtest uses only 40 training days and 5 testing days, which may be too short to assess robustness across market regimes.
- The empirical evaluation is only a simple showcase intended to demonstrate tool functionality rather than a rigorous benchmark.
- [inferred] No statistical significance testing or robustness analysis is reported for the backtesting results.
- [inferred] No comparison is provided against strong state-of-the-art classical portfolio optimizers or commercial solvers, so relative performance is unclear.
- [inferred] The paper does not quantify any computational advantage, speedup, or solution-quality benefit from quantum annealing over classical methods.
- [inferred] Real quantum hardware limitations such as noise, embedding overhead, chain breaks, and limited connectivity are not analyzed in depth.
- [inferred] Scalability to larger asset universes and production-scale financial problems is not demonstrated.
- [inferred] The use of yfinance data may introduce data-quality or survivorship issues, and these are not discussed.
- [inferred] The risk-free rate is set to 0% for simplicity in the example, which may distort Sharpe-ratio-based evaluation.
- [inferred] The study appears limited to long-only portfolios and does not evaluate short-selling, leverage, or more realistic institutional constraints.
## Open questions
- How well does PortFawn perform on larger and more realistic asset universes beyond nine ETFs?
- Does quantum annealing provide any practical advantage over classical optimization for portfolio construction in terms of runtime, solution quality, or robustness?
- How sensitive are the results to the choice of training window, testing window, and expected return/risk estimation method?
- How would the portfolios perform when transaction costs, turnover constraints, and management fees are explicitly modeled?
- How much do dividends affect the comparative results across portfolio strategies?
- How robust are the results across different market regimes, including crises and high-volatility periods?
- Can binary-weight quantum portfolios remain competitive when compared with continuous-weight classical portfolios under realistic constraints?
- What is the impact of real quantum hardware imperfections on portfolio quality and reproducibility?
- How should the risk-aversion parameter and other hyperparameters be selected for the quantum multi-objective formulation?
- To what extent do concentrated solutions from mean-variance optimization remain acceptable once practical diversification requirements are imposed?

**Future work:**
- Alter the cost functions and constraints of mean-variance optimization to create more realistic portfolios.
- Use PortFawn to implement and evaluate novel ideas in quantum and classical portfolio optimization with minimal development effort.
- Extend portfolio formulations to better address practical limitations such as liquidity, costs, dividends, and concentration.
- Contribute to and expand the open-source PortFawn codebase and documentation.
- [inferred] Benchmark PortFawn systematically against stronger classical baselines and optimization packages.
- [inferred] Evaluate the framework on larger datasets, more assets, and longer historical periods.
- [inferred] Test more realistic institutional constraints such as cardinality, turnover, sector exposure, leverage, and short-selling.
- [inferred] Study the effect of quantum hardware noise and apply error-mitigation or embedding-aware techniques.
- [inferred] Investigate richer quantum encodings that allow fractional or higher-resolution asset weights instead of binary inclusion only.
- [inferred] Perform rigorous out-of-sample and cross-regime validation using real-world financial datasets and statistical tests.
## Key ideas
- #idea:near-term-feasibility — PortFawn provides an end-to-end open-source workflow for mean-variance portfolio construction and rolling backtesting that includes execution on current D-Wave annealing hardware.
- #idea:hybrid-approach — The framework combines classical estimation and continuous-weight portfolio optimizers with a quantum-annealed binary QUBO portfolio formulation, illustrating a practical quantum-classical workflow.
- #idea:quantum-advantage — The paper suggests the D-Wave-solved BMOP performs strongly and may indicate potential benefit from quantum annealing, though this remains speculative.
- #idea:near-term-feasibility — Public code, public market data, and a reproducible software pipeline make the work useful as a research and teaching platform for quantum finance experimentation.
## Contradictions
- The paper implies quantum annealing may find better solutions via tunneling and reports BMOP as performing well, but it does not benchmark against classical QUBO/MIQP solvers or provide runtime/optimality-gap evidence, undermining any superiority claim (#contradiction:classical-vs-quantum).
- The work suggests applicability beyond the toy example, yet all experiments use only 9 ETFs and omit scaling studies, while current annealing hardware is known to face embedding and connectivity constraints for larger portfolio instances (#contradiction:scalability).
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
