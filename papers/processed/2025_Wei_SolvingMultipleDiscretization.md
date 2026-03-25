---
aliases:
- Solving Multiple Discretization Portfolio Optimization Problem with Quantum-Classical
  Hybrid Algorithms
- Solving Multiple Discretization Portfolio
authors:
- Haijing Wei
- Yanbo J. Wang
- Haoxiang Yang
- Xuan Yang
- Mingming Cao
- Qi Xu
- Minglei Cai
- Yiduo Wang
- Zhichao Mao
- Xiaofeng Cao
- Quanxin Mei
- Jie Wang
- Xiaojun Zhou
- Lin Yao
- Wending Zhao
auto_detected: true
classification: ''
contradiction_flags:
- contradiction:scalability
doi: 10.1007/s10614-025-11061-5
evidence_type: ''
idea_tags:
- idea:quantum-advantage
- idea:near-term-feasibility
- idea:hybrid-approach
journal_or_venue: Computational Economics
methodology_tags:
- quantum-annealing
- QUBO
paper_type: ''
quantum_advantage_claim: speculative
related_papers: []
relevance_phase1: high
relevance_phase3: high
source_type: peer-reviewed-empirical
source_type_confidence: high
step1_date: '2026-03-25T16:12:37.148356'
step1_model: gpt-5.1
step2_date: '2026-03-25T16:12:44.061237'
step2_model: gpt-5.1
step3_date: '2026-03-25T16:13:15.656464'
step3_model: gpt-5.4
step4_date: '2026-03-25T16:13:46.877789'
step4_model: gpt-5.4
step5_date: '2026-03-25T16:14:11.696059'
step5_model: gpt-5.4
step6_date: '2026-03-25T16:14:20.763089'
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
- contradiction/scalability
title: Solving Multiple Discretization Portfolio Optimization Problem with Quantum-Classical
  Hybrid Algorithms
topic_tags:
- portfolio-optimisation
year: 2025
zotero_key: ''
---

## Abstract summary
The paper develops a QUBO-based model for portfolio optimization that can handle multiple types of discrete and non-fungible assets and embeds realistic constraints such as limits on the number of invested assets. The authors implement a quantum-classical hybrid annealing algorithm on a D-Wave quantum annealer, compare it against pure quantum annealing and several classical optimization methods on two financial datasets, and evaluate performance using standard risk–return metrics. The study shows that the hybrid approach can outperform both classical solvers and standalone quantum annealing at comparable problem scales, and examines how increasing qubit counts affect solution quality.
## Methodology
The study develops a QUBO-based formulation of a multiple-discretization portfolio optimization problem extending the Markowitz mean-variance model to mixed asset types: fungible continuous, fungible discrete, and non-fungible assets. Historical closing prices are used to compute return vectors and covariance matrices, and portfolio constraints such as budget and optional cardinality bounds on the number of invested assets are incorporated through quadratic penalty terms and slack variables. The resulting QUBO is solved using a quantum-classical hybrid annealing approach (QCHA) on D-Wave hardware, alongside pure quantum annealing (QA) and four classical benchmark solvers: Gurobi, simulated annealing, tabu search, and steepest descent. The hybrid method partitions large QUBOs into smaller correlated subproblems using an impact-index-based decomposition, solves subQUBOs on the D-Wave Advantage 4.1 annealer, stitches subsolutions into a global candidate, and refines them with classical local search iteratively until convergence. Empirical evaluation is conducted on two short-horizon financial datasets with backtesting, comparing algorithms on daily NAV trajectories and end-of-period financial metrics including RET, ACC, Sharpe ratio, and Sortino ratio. Additional experiments analyze the effect of qubit count/discretization level and the inclusion of asset-count constraints.

**Algorithms used:** Quantum-Classical Hybrid Annealing (QCHA), Quantum Annealing (QA), Simulated Annealing (SA), Tabu Search (TS), Steepest Descent (SD)
**Frameworks:** D-Wave cloud, dwave-samplers, Gurobi, Python 3.10.13

**Experimental setup:** QCHA and QA were executed on the D-Wave Advantage system 4.1 via the D-Wave cloud. Classical benchmark algorithms (Gurobi, SA, TS, SD) and the classical coordination/local-search parts of QCHA were run on a quad-core Intel i5-8265U laptop under 64-bit Windows 11. The study tested multiple problem sizes/discretizations, including 50 binary variables for Dataset-1, 128 binary variables for Dataset-2, and additional qubit-count sweeps (20-50 for Dataset-1; 45, 91, 128 for Dataset-2). QA could not be applied to Dataset-2 because the required qubit count exceeded hardware capacity.

**Dataset:** Two empirical financial datasets were used. Dataset-1 contains 10 publicly traded stocks from the Shanghai and Shenzhen exchanges over roughly four months (September 1, 2021 to December 31, 2021), with daily closing prices collected from exchange websites. Dataset-2 contains 15 assets spanning 5 stocks, 5 public mutual funds, and 5 private equity funds over a short 2024 window (main text: January 1, 2024 to April 18, 2024, 57 trading days; appendix gives January 19, 2024 to April 9, 2024), sourced from WIND and stock exchanges. Stocks were modeled as fungible continuous assets, mutual funds as fungible discrete assets, and private equity as non-fungible assets; interpolation was used for private equity values to ensure consistency.
## Experiment details
### Input
Input data consisted of historical daily closing prices for selected assets. Dataset-1: 10 randomly selected stocks from diverse industries, sampled from larger industry-specific pools, covering 2021-09-01 to 2021-12-31; returns were computed from daily prices and used to estimate expected returns and covariance matrices. Each stock was discretized with 4-5 binary variables in different experiments, with the main comparison using 5 bits per stock (50 binary variables total). Dataset-2: 15 assets (5 stocks, 5 public funds, 5 private equity funds) from diverse sectors, sourced from WIND and exchange data, covering a short 2024 period with 57 trading days in the main text; returns and covariance matrices were computed similarly. Private equity values were interpolated for consistency. Main Dataset-2 experiments used 128 binary variables; additional runs used 45 and 91 variables. Optional preprocessing included binary encoding of asset values by asset type and construction of QUBO coefficients with penalty terms for budget and cardinality constraints.

### Process
1. Collect daily closing prices for preselected assets. 2. Compute daily returns, expected return vector, and covariance matrix. 3. Formulate the portfolio optimization objective as a Markowitz-style QUBO with binary encodings for fungible continuous, fungible discrete, and non-fungible assets. 4. Add budget and, in some experiments, asset-count constraints using squared penalty terms and slack variables. 5. Solve the QUBO using six methods where applicable: QCHA, QA, Gurobi, SA, TS, and SD. 6. For QCHA, initialize a global binary solution, compute impact indices for variables, partition the large QUBO into correlated subQUBOs, solve each subQUBO on D-Wave Advantage 4.1, stitch subsolutions into a global candidate, apply classical local search (e.g., tabu search or greedy descent), update the incumbent best solution, and repeat until convergence based on objective function value. 7. For QA, submit the full QUBO directly to D-Wave when hardware capacity permits. 8. For classical baselines, tune hyperparameters and retain best-performing settings. Gurobi tuning included time_limit and cuts; TS, SA, and SD tuning included initial_states and num_reads; SA additionally tuned beta_range schedules such as (0.1, 4.2), (0.2, 3.8), (0.3, 3.5), (0.4, 3.2), and (0.5, 3.0). 9. Backtest the resulting portfolio strategies by opening positions at the start of the trading period and assuming no trading during the period. 10. Evaluate daily NAV trajectories and end-of-period metrics. 11. Run sensitivity analyses varying qubit count/discretization and adding cardinality constraints (e.g., 3 < N < 8 for Dataset-1).

### Output
Outputs include optimal portfolio allocation proportions, objective/Hamiltonian values, daily NAV curves over the backtest period, and end-of-period financial metrics: RET, ACC, Sharpe ratio, and Sortino ratio. Comparisons were made against classical baselines (Gurobi, SA, TS, SD) and pure QA where feasible. For Dataset-1, all six methods were compared; for Dataset-2, QA was excluded due to hardware limits. The paper also reports comparative performance under different qubit counts and under constrained vs unconstrained formulations. Equal-weight portfolio backtests are described in the appendix as contextual reference, but the main algorithmic baselines are the classical and quantum optimization solvers.

### Parameters
- dataset_1_main_qubits: 50
- dataset_1_qubit_sweep: [20, 40, 50]
- dataset_2_qubit_sweep: [45, 91, 128]
- dataset_2_main_qubits: 128
- dataset_1_assets: 10
- dataset_2_assets: 15
- dataset_2_asset_types: {'stocks': 5, 'public_funds': 5, 'private_equity_funds': 5}
- bits_per_asset_dataset_1: {'main_experiment': 5, 'constraint_experiments': [4, 5]}
- constraint_range_dataset_1: 3 < N < 8
- risk_free_rate_sharpe: 0.03
- risk_free_rate_sortino: 0.0
- classical_hyperparameters_tuned: {'Gurobi': ['time_limit', 'cuts'], 'TS': ['initial_states', 'num_reads'], 'SA': ['initial_states', 'num_reads', 'beta_range'], 'SD': ['initial_states', 'num_reads']}
- sa_beta_ranges_tested: [[0.1, 4.2], [0.2, 3.8], [0.3, 3.5], [0.4, 3.2], [0.5, 3.0]]
- convergence_basis: objective function value / cost Hamiltonian expectation analogue

### Hardware
Quantum runs used the D-Wave Advantage system 4.1 accessed through the D-Wave cloud and D-Wave software stack (including dwave-samplers). QCHA solved partitioned subQUBOs on the annealer; QA attempted full-QUBO submission when feasible. Classical computations were performed on a quad-core Intel i5-8265U laptop running 64-bit Windows 11. No detailed annealing schedule, embedding, chain strength, shot/read count, or noise/transpilation settings were reported in the provided text.

### Reproducibility
Partial reproducibility. The paper provides substantial methodological detail on the QUBO formulation, datasets, evaluation metrics, and broad QCHA workflow, and states that data and source code are available upon request. However, full replication may be difficult because key implementation details are missing or incomplete in the provided text, including exact D-Wave annealing/read parameters, decomposition settings, stopping criteria, penalty coefficient values, and final hyperparameter settings for all benchmark solvers. Data sources are mostly public or accessible (exchange sites, WIND), but not fully packaged.
## Findings
- [supported] The paper proposes a QUBO-based portfolio optimization model that supports multiple discretization types of assets (fungible continuous, fungible discrete, and non-fungible) and solves it using a quantum-classical hybrid annealing approach on D-Wave hardware.
- [supported] Results are based on real quantum annealing hardware (D-Wave Advantage 4.1) for QCHA and QA, with classical benchmarks run on a conventional PC; they are not simulation-only results.
- [supported] On Dataset-1 (10 stocks, 50 binary variables), QCHA achieved the best reported end-of-period metrics among all tested methods: RET 0.890, ACC 1.227, Sharpe 3.130, and Sortino 6.242.
- [supported] On Dataset-1, QCHA outperformed Gurobi on most reported metrics: RET 0.890 vs 0.812, ACC 1.227 vs 1.211, Sharpe 3.130 vs 2.974, while Sortino was slightly lower than Tabu Search (6.242 vs 6.491).
- [supported] On Dataset-1, QCHA also outperformed standalone quantum annealing (QA): RET 0.890 vs 0.781, ACC 1.227 vs 1.204, Sharpe 3.130 vs 2.728, though QA had a marginally higher Sortino ratio (6.246 vs 6.242).
- [supported] On Dataset-2 (15 assets across stocks, mutual funds, and private equity; 128 binary variables), QCHA achieved the best Sortino ratio (4.253) and near-best ACC and Sharpe metrics, with ACC 1.089 vs Gurobi 1.094 and Sharpe 1.976 vs SA 1.986.
- [supported] On Dataset-2, QCHA outperformed Gurobi on downside-risk-adjusted performance (Sortino 4.253 vs 4.051) but not on all metrics, since Gurobi had slightly higher RET (0.487 vs 0.460) and ACC (1.094 vs 1.089).
- [supported] Standalone QA could not be run on Dataset-2 because the required qubit count exceeded D-Wave hardware capacity, whereas QCHA handled the larger problem by decomposition into subproblems.
- [supported] Increasing the number of qubits/discrete variables improved QCHA performance: on Dataset-1, the authors report that QCHA with 40 qubits already surpassed the 50-variable Gurobi benchmark on ACC and Sharpe, and performance improved further up to 50 qubits.
- [supported] On Dataset-2, QCHA performance improved approximately linearly as qubit count increased from 45 to 91 to 128, and at 128 variables it achieved a higher Sharpe ratio than Gurobi at the same scale.
- [supported] When cardinality constraints on the number of invested assets were added (3 < N < 8 on Dataset-1), all methods showed some degradation, but the paper reports that QCHA's performance drop was smaller than that of Gurobi and Tabu Search.
- [supported] Relative to naive equal-weight allocation, optimized portfolios were substantially better on both datasets; for example on Dataset-1 equal-weight backtest metrics were RET 0.172, ACC 1.052, Sharpe 0.639, Sortino 1.245, all well below QCHA's reported values.
- [speculative] The authors argue that quantum-classical hybrid methods are a promising scalable direction for larger financial combinatorial optimization tasks as hardware qubit counts and fidelity improve.
- [speculative] The paper suggests that the advantages of QCHA become more evident as the number of discrete variables/qubits increases, implying future scaling benefits beyond the tested problem sizes.

**Results summary:** This peer-reviewed empirical study formulates multi-discretized portfolio optimization as a QUBO and evaluates a quantum-classical hybrid annealing algorithm (QCHA) on D-Wave Advantage 4.1 against standalone quantum annealing (QA), Gurobi, simulated annealing, tabu search, and steepest descent. Using two real financial datasets, the authors report that QCHA produced the strongest overall performance. On Dataset-1 (10 stocks, 50 binary variables), QCHA achieved the best reported RET (0.890), ACC (1.227), and Sharpe ratio (3.130), with a Sortino ratio of 6.242 that was near the best. On Dataset-2 (15 mixed asset types, 128 variables), QCHA achieved the best Sortino ratio (4.253) and was close to the top on ACC and Sharpe, though Gurobi slightly exceeded it on RET and ACC. The study also reports that QCHA scales to larger instances that standalone QA could not fit on hardware, and that increasing qubit count improved QCHA results. No confidence intervals, hypothesis tests, or error bars are reported, so findings are based on point estimates from backtests rather than statistical inference.

**Performance claims:**
- Dataset-1, QCHA: RET 0.890, ACC 1.227, Sharpe 3.130, Sortino 6.242
- Dataset-1, Gurobi: RET 0.812, ACC 1.211, Sharpe 2.974, Sortino 6.028
- Dataset-1, QA: RET 0.781, ACC 1.204, Sharpe 2.728, Sortino 6.246
- Dataset-1, TS: RET 0.843, ACC 1.217, Sharpe 2.988, Sortino 6.491
- Dataset-1, SA: RET 0.715, ACC 1.189, Sharpe 2.608, Sortino 5.098
- Dataset-1, SD: RET 0.690, ACC 1.184, Sharpe 2.574, Sortino 5.440
- Dataset-2, QCHA: RET 0.460, ACC 1.089, Sharpe 1.976, Sortino 4.253
- Dataset-2, Gurobi: RET 0.487, ACC 1.094, Sharpe 1.912, Sortino 4.051
- Dataset-2, TS: RET 0.279, ACC 1.057, Sharpe 1.980, Sortino 3.096
- Dataset-2, SA: RET 0.280, ACC 1.057, Sharpe 1.986, Sortino 3.833
- Dataset-2, SD: RET 0.336, ACC 1.068, Sharpe 1.062, Sortino 2.022
- Equal-weight baseline on Dataset-1: RET 0.172, ACC 1.052, Sharpe 0.639, Sortino 1.245
- Equal-weight baseline on Dataset-2: RET 0.005, ACC 1.001, Sharpe -0.159, Sortino 0.051
- QCHA with 40 qubits on Dataset-1 reportedly surpassed the 50-variable Gurobi benchmark on ACC and Sharpe
- QCHA on Dataset-2 improved from 45 to 91 to 128 qubits, with approximately linear improvement and higher Sharpe than Gurobi at 128 variables
## Quantum advantage claim
**Classification:** speculative

The paper presents empirical results on real D-Wave hardware showing QCHA outperforming several classical baselines on selected backtest metrics and problem instances, but it does not establish a rigorous quantum advantage in the standard sense. Results are limited to small benchmark datasets, mixed metrics, and no statistical significance analysis or asymptotic speedup evidence is provided. Thus the advantage claim is best classified as speculative rather than demonstrated.
## Limitations
- Quantum Annealing (QA) could not be applied to Dataset-2 because the required number of qubits exceeded the capacity of the D-Wave system
- Current quantum hardware imposes qubit-count limitations, which restrict the resolution used to encode fungible continuous assets and the overall problem size
- Increasing the number of qubits makes convergence harder on current hardware, creating a trade-off between encoding precision and solvability
- The experiments were conducted on only two datasets, limiting the breadth of empirical validation
- Dataset-1 contains only 10 stocks and Dataset-2 contains 15 assets, so empirical evaluation is limited to relatively small portfolio sizes
- Both datasets use short historical windows (roughly four months / 57 trading days), which may limit robustness across market regimes
- Backtesting assumes positions are opened at the start of the trading period and no trading occurs during the period, which simplifies real portfolio management
- The study relies on historical closing prices and covariance estimates from short windows, which may be unstable in volatile markets
- Private equity values in Dataset-2 were generated using interpolation methods for consistency across asset types, which may reduce realism
- Asset preselection was random from curated pools, which may introduce sampling sensitivity and affect internal validity
- When constraints on the number of invested assets are added, all evaluation metrics decline slightly, indicating added modeling and optimization difficulty
- The authors note that practical large-scale portfolio optimization will require further improvements in gate fidelity and qubit count before real-world deployment
- Data and code are only available upon request rather than openly released, limiting reproducibility
- [inferred] The comparison set omits stronger modern classical baselines commonly used in portfolio optimization, such as mixed-integer quadratic programming formulations beyond the chosen heuristics, advanced metaheuristics, or learning-based methods
- [inferred] No statistical significance tests, confidence intervals, or repeated-run variability analyses are reported, so it is unclear whether observed performance differences are robust
- [inferred] Results are based on backtests over limited periods and do not establish scalability to production trading environments with transaction costs, slippage, liquidity, and rebalancing constraints
- [inferred] The study uses D-Wave annealing and a hybrid decomposition approach, so the reported gains may partly reflect decomposition heuristics and classical post-processing rather than purely quantum advantage
- [inferred] Hardware noise, embedding overhead, and annealer-specific effects are not quantitatively isolated, making it difficult to attribute performance to quantum processing alone
- [inferred] The use of a penalty-based QUBO formulation may be sensitive to penalty coefficient tuning, but robustness to this choice is not systematically analyzed
- [inferred] The benchmark hardware for classical methods is a quad-core Intel i5 laptop, which may not reflect stronger production-grade classical optimization infrastructure
## Open questions
- How well does the proposed hybrid approach scale to much larger portfolios with substantially more assets and constraints?
- At what problem size, if any, does the hybrid quantum approach consistently outperform state-of-the-art classical solvers under realistic compute budgets?
- How sensitive are results to the choice of qubit count and discretization granularity for continuous assets?
- How robust is the method across different market regimes, longer time horizons, and out-of-sample periods?
- How would the algorithm perform when using real-time market data for dynamic portfolio optimization rather than static backtesting?
- What is the impact of hardware improvements in qubit count and gate fidelity on solution quality and practical applicability?
- How does the method behave under more realistic portfolio constraints such as transaction costs, turnover limits, liquidity constraints, and periodic rebalancing?
- Can the approach maintain its advantage when the number and complexity of constraints increase substantially?
- How much of the observed performance gain comes from the quantum annealer versus the classical decomposition and local-search components?
- How reproducible are the results across repeated runs, different random seeds, and different D-Wave hardware calibrations?

**Future work:**
- Integrate real-time market data to enable dynamic portfolio optimization
- Develop a time-series modeling framework tailored to multiple discretization levels
- Optimize larger and more complex portfolios as quantum hardware evolves
- Improve quantum hardware, especially gate fidelity and qubit count, to meet practical application demands
- Combine machine learning with quantum computing for portfolio optimization and related financial applications
- Extend the framework to broader microeconomic and combinatorial optimization problems involving binary and integer decision variables
- [inferred] Evaluate the method on larger, more diverse, and longer-horizon real-world financial datasets
- [inferred] Incorporate realistic trading frictions such as transaction costs, slippage, liquidity, and rebalancing rules
- [inferred] Perform more rigorous reproducibility studies with open code/data releases and repeated-run statistical analysis
- [inferred] Benchmark against stronger classical optimization baselines and production-grade compute environments
- [inferred] Study the effects of noise, embedding choices, and penalty-parameter tuning on solution quality
## Key ideas
- #idea:hybrid-approach — The paper proposes a quantum-classical hybrid annealing workflow that decomposes a large portfolio QUBO into correlated subQUBOs solved on D-Wave and then refines stitched solutions with classical local search.
- #idea:near-term-feasibility — The study demonstrates execution on real D-Wave Advantage 4.1 hardware rather than classical simulation only, showing a practical NISQ/annealing-era implementation for portfolio optimization.
- #idea:near-term-feasibility — The QUBO formulation extends Markowitz-style portfolio optimization to mixed asset types including fungible continuous, fungible discrete, and non-fungible assets, with budget and cardinality constraints.
- #idea:quantum-advantage — The authors claim emerging performance advantages for the hybrid quantum approach because QCHA outperforms pure QA and several classical baselines on selected backtest metrics at comparable tested scales.
- #idea:hybrid-approach — Hybridization is presented as essential for handling larger instances than standalone QA, since QA could not run the 128-variable Dataset-2 while QCHA could via decomposition.
- #idea:near-term-feasibility — Performance reportedly improves as discretization/qubit count increases, suggesting that additional quantum resources may improve portfolio quality on this formulation.
## Contradictions
- The paper suggests favorable scalability and future practical advantage, but its empirical evidence is limited to small portfolios (10–15 assets), short backtest windows, and one annealing platform; this supports the flag contradiction:scalability.
- The paper frames QCHA as outperforming classical methods, yet on Dataset-2 Gurobi slightly exceeds QCHA on RET and ACC, so superiority is metric-dependent rather than universal.
- The paper implies larger qubit counts indicate scaling benefits, but no asymptotic runtime, complexity, or industrial-scale benchmark evidence is provided, making the scaling claim stronger than the evidence.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
