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
methodology_tags: []
paper_type: ''
quantum_advantage_claim: not-applicable
related_papers: []
relevance_phase1: medium
relevance_phase3: low
source_type: conference-paper
source_type_confidence: high
step1_date: '2026-03-25T16:03:26.739552'
step1_model: gpt-5.1
step2_date: '2026-03-25T16:03:30.362697'
step2_model: gpt-5.1
step3_date: '2026-03-25T16:04:04.681157'
step3_model: gpt-5.4
step4_date: '2026-03-25T16:04:20.466561'
step4_model: gpt-5.4
step5_date: '2026-03-25T16:04:42.278266'
step5_model: gpt-5.4
step6_date: '2026-03-25T16:04:51.949839'
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
- topic/risk-modelling
- idea/near-term-feasibility
- idea/hybrid-approach
- contradiction/classical-vs-quantum
- contradiction/scalability
title: Qutrit-based Quantum-inspired Optimization Model on Real-world Portfolio Optimization
topic_tags:
- portfolio-optimisation
- risk-modelling
year: 2024
zotero_key: ''
---

## Abstract summary
The paper proposes a quantum-inspired portfolio optimization model that uses a qutrit-based ternary encoding to represent long-selling, short-selling, and non-investment decisions within a single hybrid strategy. Building on Global Best Guided Quantum-inspired Tabu Search, the authors adapt the update mechanism to handle three-state encoding and incorporate a trend ratio metric to favor stable upward portfolio performance. Using real-world DJIA data, they show that the hybrid qutrit-based strategy can reduce risk and improve trend performance compared to separate long-only or short-only strategies.
## Methodology
This conference paper presents an empirical, quantum-inspired optimization approach for portfolio selection using a qutrit-inspired ternary encoding rather than an actual quantum algorithm on quantum hardware. The method extends Global Best Guided Quantum-inspired Tabu Search (GQTS) into a qutrit-based GQTS that represents each asset with three possible states: non-investment, long-selling (LS), and short-selling (SS). The authors modify the GQTS update mechanism by adjusting two boundary parameters (beta_j1 and beta_j2) with a fine-tuned step size theta according to the global-best and local-worst states, enabling search over a ternary solution space. The optimization objective incorporates the trend ratio metric, defined as return per unit risk based on a regression trend line, to favor stable upward-trending portfolios. Empirically, the model is evaluated on real-world Dow Jones Industrial Average (DJIA) data from 2013 to 2022 using a sliding-window protocol with 13 window types and 830 periods. The proposed hybrid strategy is compared against standalone LS and SS strategies, with comparative targets run using EL-GNQTS under settings from prior work. Performance is assessed primarily through risk and trend ratio, with repeated runs used to evaluate robustness.

**Algorithms used:** Global Best Guided Quantum-inspired Tabu Search (GQTS), Qutrit-based GQTS, EL-GNQTS

**Experimental setup:** Experiments were conducted on a classical computer using a quantum-inspired optimization model rather than a real quantum processor. The portfolio universe is the DJIA with a ternary search space of 3^30. The initial fund is 10 million USD. Data from 2013 to 2022 were split using a sliding window method into 13 types of windows, yielding 830 periods. Population size was 10. Each period was tested 50 times, and each run executed 10,000 iterations.

**Dataset:** Real-world financial data from the U.S. Dow Jones Industrial Average (DJIA) index covering the investment period 2013-2022.
## Findings
- [supported] The paper proposes a qutrit-inspired quantum-inspired optimization (QIO) model for portfolio optimization that uses ternary encoding to represent non-investment, long-selling (LS), and short-selling (SS).
- [supported] On real-world DJIA data from 2013 to 2022, the proposed hybrid strategy achieved lower risk than LS-only and SS-only portfolios across all 13 sliding-window settings tested.
- [supported] The proposed hybrid strategy achieved higher trend ratio than LS-only and SS-only strategies in the reported experiments across the 13 sliding-window settings.
- [supported] The authors report that LS and SS fluctuations were highly symmetric and complementary in the hybrid portfolio, which reduced portfolio risk and produced a more stable upward trend.
- [supported] The experiments were conducted on a classical computer using a quantum-inspired algorithm rather than on quantum hardware.
- [speculative] The qutrit-based method is argued to benefit from a larger solution space and more efficient search due to quantum-inspired behavior, but no direct computational speedup versus classical optimization baselines is quantified.
- [speculative] The authors suggest the approach has significant potential for mitigating investment risk and supporting investor decision-making in volatile markets.

**Results summary:** This conference paper presents a qutrit-inspired portfolio optimization model implemented as a quantum-inspired optimization algorithm on a classical computer. The method extends binary portfolio encoding to a ternary representation covering long-selling, short-selling, and non-investment, and integrates this encoding into a Global Best Guided Quantum-inspired Tabu Search framework. Using DJIA data from 2013 to 2022, 13 sliding-window configurations, 830 periods, 50 runs per period, and 10,000 iterations per run, the authors report that the hybrid LS/SS strategy consistently produced lower risk and higher trend ratio than LS-only and SS-only comparison strategies. The empirical evidence supports improved portfolio stability from combining LS and SS, but the work does not demonstrate quantum advantage because it is quantum-inspired, classically executed, and does not provide a quantified runtime or complexity advantage over strong classical baselines.

**Performance claims:**
- Experiments used DJIA data with a solution space of 3^30
- Investment period covered 2013 to 2022
- 830 periods evaluated across 13 types of sliding windows
- Population size set to 10
- 50 test runs per period
- 10,000 iterations per test run
- Theta parameter set to 0.0003
- Lower risk than LS-only and SS-only portfolios in all 13 sliding-window settings
- Higher trend ratio than LS-only and SS-only portfolios across the reported 13 sliding-window settings
## Quantum advantage claim
**Classification:** not-applicable

The paper studies a quantum-inspired optimization method executed on a classical computer, not a quantum algorithm on quantum hardware. While it claims benefits from qutrit-inspired encoding and larger solution space exploration, it does not demonstrate or rigorously establish quantum advantage.
## Limitations
- The method is quantum-inspired and executed on a classical computer rather than demonstrated on actual quantum or qutrit hardware.
- Experiments are limited to the 30-stock DJIA universe, which constrains generalizability to larger and more diverse portfolios.
- Evaluation uses data from a single market index (U.S. DJIA) over 2013–2022, so robustness across other asset classes, regions, and market regimes is not established.
- The comparison baseline is limited to long-selling and short-selling portfolios run by EL-GNQTS; broader comparisons with state-of-the-art classical portfolio optimization methods are not reported.
- The study optimizes primarily via the trend ratio and emphasizes risk reduction, leaving broader objective formulations only partially explored.
- Parameter choices such as population size, 10,000 iterations, and theta = 0.0003 appear fixed, with limited discussion of sensitivity or robustness to hyperparameter settings.
- [inferred] No transaction costs, borrowing fees, short-sale constraints, slippage, taxes, or liquidity effects are modeled, which may materially affect real-world portfolio performance.
- [inferred] The assumption that long-selling and short-selling fluctuations can complement each other may weaken under realistic market frictions and imperfect hedging conditions.
- [inferred] The paper does not report statistical significance tests or confidence intervals, so it is unclear whether the observed improvements are statistically robust across windows and runs.
- [inferred] Reproducibility is limited because implementation details beyond high-level settings are sparse, which is common in conference papers with page-limit constraints.
- [inferred] Scalability beyond the reported 3^30 search space is not empirically demonstrated, so practical performance on larger institutional portfolios remains uncertain.
- [inferred] Missing empirical validation on live or paper-trading deployment leaves the gap between backtest results and production use unresolved.
## Open questions
- How well does the qutrit-inspired hybrid strategy scale to portfolios with substantially more than 30 assets?
- Will the reported risk reduction and trend-ratio gains persist in other stock markets, asset classes, or cross-market portfolios?
- How sensitive is performance to the sliding-window design, parameter theta, population size, and iteration budget?
- How does the method compare against stronger classical baselines such as mean-variance optimization, robust optimization, mixed-integer formulations, or modern metaheuristics?
- What is the impact of realistic trading frictions, especially short-selling costs and constraints, on the hybrid strategy's profitability and stability?
- Can the ternary qutrit-inspired encoding provide advantages beyond this specific portfolio setting, or are the gains mainly due to the added strategy flexibility?
- Would the approach retain its benefits if implemented on future qutrit-capable quantum hardware rather than simulated classically?
- How stable are the complementary LS/SS fluctuation patterns during extreme market stress or structural breaks?

**Future work:**
- Expand the model to consider multiple objectives, such as both risk and return.
- Include investments across various stock markets.
- [inferred] Benchmark against a wider set of classical and quantum-inspired portfolio optimization methods.
- [inferred] Test the approach on larger portfolios and broader financial universes to assess scalability.
- [inferred] Incorporate realistic market constraints and frictions, including transaction costs, liquidity limits, and short-selling restrictions.
- [inferred] Perform sensitivity analyses and ablation studies on encoding choices, update rules, and hyperparameters.
- [inferred] Explore implementation on actual quantum/qutrit hardware when feasible to assess the gap between inspiration and hardware realization.
- [inferred] Validate the strategy in out-of-sample, paper-trading, or live-trading settings to evaluate production readiness.
## Key ideas
- #idea:hybrid-approach — Uses a ternary qutrit-inspired encoding to jointly model non-investment, long-selling, and short-selling within one portfolio optimisation framework.
- #idea:hybrid-approach — The hybrid LS/SS portfolio is reported to reduce risk and improve trend ratio relative to separate LS-only and SS-only strategies on DJIA data.
- #idea:near-term-feasibility — Demonstrates a practically executable quantum-inspired approach on classical hardware using real financial data and extensive backtesting windows.
- #idea:near-term-feasibility — Frames qutrit-inspired search as a way to explore a larger ternary portfolio decision space without requiring actual quantum hardware.
## Contradictions
- The paper suggests benefits from qutrit-inspired search and larger solution-space exploration, but this does not establish quantum superiority because the method is entirely classical and no quantum hardware or quantum speedup is demonstrated.
- The reported empirical gains are limited to a 30-stock DJIA setting and comparisons against LS-only/SS-only variants, so claims or implications about broader scalability to realistic institutional portfolio sizes remain unproven.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->

## Experiment details
### Input
DJIA stock market data from the U.S. over 2013-2022, apparently covering 30 index constituents as implied by the 3^30 solution space. The data were partitioned using a sliding window method into 13 sliding-window types and 830 periods to keep training data fresh. The paper also assumes an initial investment fund of 10 million USD. Specific feature definitions, exact train/test window lengths, and preprocessing details beyond the sliding-window split are not fully reported.

### Process
1. Encode each stock in a ternary qutrit-inspired state: 0 = non-investment, 1 = long-selling, 2 = short-selling. 2. Initialize a population of candidate portfolios for qutrit-based GQTS. 3. Update each asset's ternary state probabilities using the modified GQTS rule based on the global-best and local-worst selections, adjusting beta_j1 and beta_j2 by theta. 4. Evaluate candidate portfolios using the trend ratio objective, which captures return relative to risk via the regression trend line. 5. Repeat the search for 10,000 iterations per run. 6. Apply the procedure across sliding-window train/test periods. 7. Repeat each experiment 50 times per period. 8. Compare the resulting hybrid strategy portfolio against LS-only and SS-only portfolios, with comparative targets run by EL-GNQTS using parameter settings from the cited prior paper.

### Output
Reported outputs include portfolio risk and trend ratio across 13 sliding-window settings, along with run charts showing standardized portfolio funds over time and corresponding trend lines. The main comparisons are between the proposed hybrid strategy portfolio and LS-only and SS-only portfolios. Results are presented graphically, showing lower risk and higher trend ratio for the hybrid strategy.

### Parameters
- solution_space: 3^30
- initial_fund_usd: 10000000
- population_size: 10
- runs_per_period: 50
- iterations_per_run: 10000
- theta: 0.0003
- sliding_window_types: 13
- periods: 830

### Hardware
{'hardware_type': 'classical computer', 'qpu_used': False}

### Reproducibility
No code repository or implementation link is mentioned in the provided text. The data source (DJIA market data) is identifiable and likely obtainable, and several key parameters are reported, but exact sliding-window definitions, data preprocessing details, and full implementation specifics are insufficient for straightforward replication.
