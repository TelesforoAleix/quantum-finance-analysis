---
aliases:
- Improved Quantum Approximate Optimization Algorithm based on Conditional Value-at-Risk
  for Portfolio Optimization
- Improved Quantum Approximate Optimization
authors:
- Qingqing Yu
- Rong Jin
auto_detected: true
classification: ''
contradiction_flags:
- contradiction:scalability
- contradiction:classical-vs-quantum
doi: 10.21203/rs.3.rs-4582391/v1
evidence_type: ''
idea_tags:
- idea:quantum-advantage
- idea:near-term-feasibility
- idea:hybrid-approach
journal_or_venue: Research Square
methodology_tags:
- QAOA
- QUBO
- variational
- classical-simulation
paper_type: ''
quantum_advantage_claim: speculative
related_papers: []
relevance_phase1: high
relevance_phase3: high
source_type: preprint
source_type_confidence: high
step1_date: '2026-03-25T16:06:16.439861'
step1_model: gpt-5.1
step2_date: '2026-03-25T16:06:21.229514'
step2_model: gpt-5.1
step3_date: '2026-03-25T16:07:04.276817'
step3_model: gpt-5.4
step4_date: '2026-03-25T16:07:30.450895'
step4_model: gpt-5.4
step5_date: '2026-03-25T16:07:58.658976'
step5_model: gpt-5.4
step6_date: '2026-03-25T16:08:13.065967'
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
- method/QAOA
- method/QUBO
- method/variational
- method/classical-simulation
- idea/quantum-advantage
- idea/near-term-feasibility
- idea/hybrid-approach
- contradiction/scalability
- contradiction/classical-vs-quantum
title: Improved Quantum Approximate Optimization Algorithm based on Conditional Value-at-Risk
  for Portfolio Optimization
topic_tags:
- portfolio-optimisation
- risk-modelling
year: 2024
zotero_key: ''
---

## Abstract summary
The paper proposes an enhanced variant of the Quantum Approximate Optimization Algorithm (QAOA) for discrete Markowitz portfolio optimization, incorporating Conditional Value-at-Risk (CVaR) as the objective to emphasize tail-risk in the loss distribution. It introduces a modified QAOA ansatz with an additional problem-agnostic entangling layer that balances circuit depth and solution quality, and uses CVaR-based cost evaluation to guide the classical optimization. Using historical Nasdaq data for portfolios up to 16 assets, the study compares standard QAOA, CVaR-QAOA, and the improved CVaR-QAOA, showing that the proposed method converges faster and attains higher probabilities of optimal solutions, especially for larger portfolios.
## Methodology
This preprint presents an empirical study of portfolio optimization using an improved variant of the Quantum Approximate Optimization Algorithm (QAOA) combined with a Conditional Value-at-Risk (CVaR) objective. The authors formulate discrete mean-variance portfolio optimization as a QUBO problem with binary buy/hold decisions, then transform it into an Ising Hamiltonian encoded as a cost Hamiltonian for QAOA. They compare standard QAOA, CVaR-QAOA, and an improved CVaR-QAOA ansatz that augments a standard p-layer QAOA circuit with an additional problem-agnostic entangling ZZ layer over adjacent qubits and an extra X-mixer layer, using shared parameters for the added gates to keep circuit depth shallow. Historical Nasdaq stock data over a five-year period are used to construct portfolio instances of 10, 12, 14, and 16 assets. The variational parameters are optimized with the classical COBYLA optimizer, and performance is evaluated via exact quantum state simulation in TensorCircuit rather than on real quantum hardware. The study varies the CVaR confidence level alpha from 0.01 to 1.0 and tests QAOA depths p = 1 and p = 2, though only p = 1 results are reported because p = 2 did not outperform p = 1. Outcomes are assessed mainly by convergence speed, achieved cost values, and probability of obtaining the optimal measurement outcome, with comparisons across algorithm variants and problem sizes. As a preprint, this work has not been peer reviewed.

**Algorithms used:** QAOA, CVaR-QAOA, Improved CVaR-QAOA, COBYLA
**Frameworks:** TensorCircuit

**Experimental setup:** Experiments were conducted using exact quantum state simulations in the TensorCircuit open-source quantum circuit simulator. Portfolio instances with 10, 12, 14, and 16 qubits/assets were evaluated. The authors tested CVaR-QAOA and an improved CVaR-QAOA for seven alpha values (0.01, 0.05, 0.1, 0.25, 0.5, 0.75, 1) and considered QAOA depths p = 1 and p = 2, but only p = 1 results were presented because p = 2 did not outperform p = 1. A callback function recorded parameters during optimization.

**Dataset:** Historical stock data downloaded from Nasdaq for 16 selected stocks over five years, from 2019-04-22 to 2024-04-18. The paper lists the 16 stocks used, including BABA, ANPDF, BIDU, JD, SNPMF, AMZN, HTHIY, MSBHF, SIEGY, TSLA, AAPL, GE Aerospace, MSFT, QCOM, NKE, and ADDYY.
## Experiment details
### Input
Historical Nasdaq stock data for 16 named stocks spanning 2019-04-22 to 2024-04-18. From this universe, portfolio optimization instances of size 10, 12, 14, and 16 assets were generated. The optimization uses binary buy/hold variables and budget constraints reported in figures as B=7 for 10 stocks, B=8 for 12 stocks, B=10 for 14 stocks, and B=10 for 16 stocks. The paper implies expected returns and covariance matrices were computed from historical data for Markowitz-style mean-variance optimization, but preprocessing details are not fully specified.

### Process
1. Download five years of historical stock data from Nasdaq for 16 selected stocks. 2. Construct discrete mean-variance portfolio optimization instances with binary decision variables and fixed budget constraints. 3. Convert the portfolio optimization objective into QUBO form and then into an Ising Hamiltonian. 4. Build standard QAOA circuits with cost and X-mixer layers, and build an improved ansatz by appending an additional nearest-neighbor ZZ entangling layer plus an extra X-mixer layer with shared parameters. 5. Initialize variational parameters gamma in [0, 2pi) and beta in [0, pi); for the improved ansatz use 2(p+1) parameters. 6. Evaluate the objective using either the standard expectation value (alpha = 1) or CVaR over the lower alpha-tail of sampled energies for alpha in {0.01, 0.05, 0.1, 0.25, 0.5, 0.75, 1}. 7. Optimize parameters using the COBYLA classical optimizer, while recording parameter trajectories via a callback function. 8. Run experiments for p = 1 and p = 2, but report only p = 1 because p = 2 did not improve performance. 9. Compare standard QAOA, CVaR-QAOA, and improved CVaR-QAOA by convergence iterations, achieved cost values, and probability of obtaining the optimal solution.

### Output
Reported outputs include convergence curves of cost/loss versus optimization iterations, the number of iterations required to reach the optimal cost value, optimal cost values for each portfolio size, and qualitative statements about the probability of obtaining the correct or optimal measurement outcome. Baseline comparisons are made against original QAOA (alpha = 1) and standard CVaR-QAOA. Table 2 reports convergence iterations for 10, 12, 14, and 16 stock cases, showing faster convergence for CVaR-QAOA and especially the improved method.

### Parameters
- qubits: [10, 12, 14, 16]
- qaoa_depth_tested: [1, 2]
- reported_qaoa_depth: 1
- alpha_values: [0.01, 0.05, 0.1, 0.25, 0.5, 0.75, 1.0]
- optimizer: COBYLA
- budget_constraints: {'10_stocks': 7, '12_stocks': 8, '14_stocks': 10, '16_stocks': 10}
- ansatz_variant: Standard p-layer QAOA plus one additional nearest-neighbor ZZ layer and one extra X-mixer layer with shared parameters
- parameter_ranges: {'gamma': '[0, 2pi)', 'beta': '[0, pi)'}
- iterations_to_optimal: {'original_qaoa': {'10_stocks': 500, '12_stocks': 550, '14_stocks': 600, '16_stocks': 700}, 'cvar_qaoa_alpha_0.1': {'10_stocks': 100, '12_stocks': 50, '14_stocks': 150, '16_stocks': 200}, 'improved_method_alpha_0.1': {'10_stocks': 100, '12_stocks': 30, '14_stocks': 100, '16_stocks': 100}, 'cvar_qaoa_alpha_0.01': {'10_stocks': 40, '12_stocks': 30, '14_stocks': 30, '16_stocks': 50}, 'improved_method_alpha_0.01': {'10_stocks': 30, '12_stocks': 30, '14_stocks': 25, '16_stocks': 35}}
- optimal_cost_values: {'10_stocks': -64.1406, '12_stocks': -82.6233, '14_stocks': -126.593, '16_stocks': -126.9287}

### Hardware
{'hardware_type': 'Simulator', 'simulator': 'TensorCircuit exact quantum state simulator', 'qpu_used': False, 'noise_model': 'Not reported'}

### Reproducibility
Preprint. Data source is public in principle (Nasdaq historical stock data) and the stock list and date range are provided, but the paper does not provide code, exact data extraction details, full preprocessing steps, sampling settings, or complete optimizer configuration. Replication is partially feasible but not fully specified.
## Findings
- [supported] The paper proposes an improved CVaR-QAOA variant for mean-variance portfolio optimization by combining a CVaR-based objective with an additional problem-agnostic ansatz layer containing nearest-neighbor ZZ entanglers and an extra X-mixer layer.
- [supported] In exact quantum state simulation on portfolio instances with 10, 12, 14, and 16 assets, the improved CVaR-QAOA converged to lower cost values faster than both standard QAOA and baseline CVaR-QAOA.
- [supported] For the 16-stock instance, standard QAOA reportedly required 700 iterations to reach the optimal cost value, while the improved CVaR-QAOA with alpha = 0.01 reached the optimal value in 35 iterations.
- [supported] Across the reported experiments, CVaR-based optimization generally converged faster than the original expectation-value QAOA case corresponding to alpha = 1.
- [supported] The authors report that small CVaR tail fractions, especially alpha in the range 0.01 to 0.1, gave the best performance in most tested portfolio optimization instances.
- [supported] The paper states that the improved method's advantage becomes more pronounced as the number of stocks increases from 10 to 16 in the tested simulations.
- [supported] The experiments found that p = 2 did not outperform p = 1 for the tested setups, so only p = 1 results were presented.
- [supported] The reported optimal cost values for the tested instances were -64.1406 for 10 stocks, -82.6233 for 12 stocks, -126.593 for 14 stocks, and -126.9287 for 16 stocks.
- [speculative] The authors suggest the improved CVaR-QAOA is promising for practical financial-industry portfolio optimization applications as portfolio size grows.
- [speculative] Claims of higher probability of obtaining the correct measurement outcome and better scalability are based on simulator experiments rather than real quantum hardware.

**Results summary:** This preprint studies portfolio optimization formulated as a QUBO/Ising problem and evaluates an improved QAOA variant that replaces the standard expectation objective with CVaR and adds a shallow problem-agnostic entangling layer to the ansatz. Using historical Nasdaq stock data from 2019-04-22 to 2024-04-18 and exact statevector simulation in TensorCircuit, the authors test 10-, 12-, 14-, and 16-asset instances. They report that CVaR-based QAOA converges faster than standard QAOA, and that their improved CVaR-QAOA converges faster still, especially for larger instances. The strongest numerical result is for 16 stocks, where standard QAOA reportedly needs 700 iterations to reach the optimal cost, baseline CVaR-QAOA with alpha = 0.01 needs 50 iterations, and the improved CVaR-QAOA with alpha = 0.01 needs 35 iterations. However, all evidence is from simulation, so any broader claims about practical quantum advantage remain speculative.

**Performance claims:**
- 16-stock instance: standard QAOA required 700 iterations to reach the optimal cost value; improved CVaR-QAOA (alpha = 0.01) required 35 iterations
- 16-stock instance: baseline CVaR-QAOA (alpha = 0.01) required 50 iterations; improved CVaR-QAOA (alpha = 0.01) required 35 iterations
- 14-stock instance: standard QAOA 600 iterations; CVaR-QAOA (alpha = 0.01) 30 iterations; improved CVaR-QAOA (alpha = 0.01) 25 iterations
- 12-stock instance: standard QAOA 550 iterations; CVaR-QAOA (alpha = 0.01) 30 iterations; improved CVaR-QAOA (alpha = 0.01) 30 iterations
- 10-stock instance: standard QAOA 500 iterations; CVaR-QAOA (alpha = 0.01) 40 iterations; improved CVaR-QAOA (alpha = 0.01) 30 iterations
- For alpha = 0.1, iteration counts were: CVaR-QAOA 100/50/150/200 and improved CVaR-QAOA 100/30/100/100 for 10/12/14/16 stocks respectively
- Reported optimal cost values: -64.1406 (10 stocks), -82.6233 (12 stocks), -126.593 (14 stocks), -126.9287 (16 stocks)
- Tested alpha values: 0.01, 0.05, 0.1, 0.25, 0.5, 0.75, 1.0
- Historical data window used: 5 years from 2019-04-22 to 2024-04-18
## Quantum advantage claim
**Classification:** speculative

The paper claims improved convergence and better performance for portfolio optimization, but results are based on exact quantum circuit simulation rather than real hardware and do not demonstrate a clear advantage over state-of-the-art classical optimization methods. As a preprint, any quantum advantage implication should be treated as speculative.
## Limitations
- The paper is a preprint and has not undergone peer review, so claims and experimental methodology have not yet been independently validated
- The authors explicitly state uncertainty about which definite CVaR parameter α yields the best performance across problems
- Performance appears sensitive to parameter tuning, and the authors note the need for a model that is not overly reliant on or sensitive to parameter adjustments
- Experiments are limited to small problem sizes of 10, 12, 14, and 16 qubits/stocks
- Evaluation is performed using exact statevector simulation in TensorCircuit rather than on real quantum hardware
- [inferred] No assessment of hardware noise, decoherence, gate errors, or measurement error is provided, so NISQ practicality is untested
- [inferred] The claimed practical applicability to financial services is not demonstrated because results are only shown in simulation on small instances
- Only one historical dataset is used: 16 selected Nasdaq stocks over a five-year period
- [inferred] The asset universe is narrow and manually selected, which may limit generalizability to broader markets, other asset classes, or different market regimes
- The experiments only report results for p = 1 because p = 2 did not outperform p = 1, leaving limited exploration of circuit depth effects
- [inferred] No systematic explanation is given for why p = 2 underperforms p = 1 in these experiments
- [inferred] No comparison is made against strong state-of-the-art classical portfolio optimization or QUBO solvers, only against QAOA variants
- [inferred] The study uses a simplified binary buy/hold formulation with wi in {0,1}, which omits realistic portfolio features such as continuous weights, transaction costs, cardinality/turnover constraints, and short selling
- [inferred] Budget settings are fixed per experiment and sensitivity to different budget constraints is not systematically analyzed
- [inferred] Reproducibility is limited because the paper does not provide enough implementation detail about initialization, shot settings, stopping criteria, random seeds, or callback traces to fully replicate results
- [inferred] Statistical robustness is unclear because there is no reporting of repeated runs, confidence intervals, or variance across optimizer initializations
- [inferred] The improved ansatz adds parameters and entangling structure, but there is no resource analysis of gate counts, depth scaling, or trainability as problem size grows
## Open questions
- Which CVaR confidence level α consistently gives the best performance for portfolio optimization problems?
- Can a self-adaptive method be developed to choose α automatically for different portfolio instances?
- Why does the improved CVaR-QAOA show increasing advantages as the number of stocks grows within the tested range?
- Will the observed convergence and success-probability improvements persist on larger portfolios beyond 16 assets?
- How will the method perform on real noisy quantum hardware rather than ideal simulators?
- How sensitive are results to optimizer choice, parameter initialization, and sampling noise?
- Why does p = 2 fail to outperform p = 1 in the reported experiments?
- How does the proposed method compare with strong classical baselines in runtime, solution quality, and scalability?
- Can the approach handle more realistic portfolio models with continuous allocations, transaction costs, and additional financial constraints?
- How robust is the method across different datasets, market regimes, and asset universes?

**Future work:**
- Develop a self-adaptive approach to choose the best α parameter automatically
- Design a model that is high-performance and stable without being overly reliant on sensitive parameter adjustments
- Test the method on larger portfolio optimization instances with more assets
- Evaluate the approach on real quantum hardware or realistic noisy simulations to assess NISQ feasibility
- Investigate the relationship between ansatz design, circuit depth, and optimization quality
- Study why higher-depth settings such as p = 2 do not improve performance in this setup
- Benchmark against advanced classical portfolio optimization and QUBO solvers
- Extend the formulation to more realistic financial settings beyond binary buy/hold portfolios
- Perform broader empirical validation across different markets, datasets, and time periods
- Improve reproducibility by releasing code, parameter settings, and experimental protocols
## Key ideas
- #idea:hybrid-approach — Discrete Markowitz portfolio optimisation is formulated as a QUBO/Ising problem and solved with a hybrid QAOA loop using COBYLA.
- #idea:near-term-feasibility — The paper proposes a shallow improved CVaR-QAOA ansatz with an added problem-agnostic nearest-neighbour ZZ entangling layer and extra X-mixer to improve solution quality without large depth increases.
- #idea:near-term-feasibility — CVaR is used as the optimisation objective to focus the variational search on low-energy tail outcomes, linking portfolio optimisation to tail-risk-aware objectives.
- #idea:quantum-advantage — In exact simulations on 10–16 asset instances, improved CVaR-QAOA converges faster and reaches higher optimal-solution probability than standard QAOA, with the strongest reported gain being 35 vs 700 iterations on the 16-asset case.
- #idea:quantum-advantage — The authors suggest that the relative benefit of the improved method increases with portfolio size within the tested range.
## Contradictions
- The paper implies potential quantum performance gains and practical relevance, but it does not compare against strong classical portfolio optimisation or QUBO baselines; this weakens any superiority claim beyond comparisons to other QAOA variants.
- The paper suggests improved scalability and practical promise for larger portfolio problems, yet evidence is limited to noiseless exact simulation on only 10–16 assets, creating a contradiction between the strength of the scalability claim and the small-scale evaluation.
- The work is framed as NISQ-oriented via shallow circuits, but no hardware runs or noise-aware experiments are provided, so near-term feasibility remains unverified.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
