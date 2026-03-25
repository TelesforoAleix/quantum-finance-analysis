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
contradiction_flags:
- contradiction:classical-vs-quantum
- contradiction:scalability
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
step1_date: '2026-03-25T16:06:28.276386'
step1_model: gpt-5.1
step2_date: '2026-03-25T16:06:31.672904'
step2_model: gpt-5.1
step3_date: '2026-03-25T16:07:10.491410'
step3_model: gpt-5.4
step4_date: '2026-03-25T16:07:33.462029'
step4_model: gpt-5.4
step5_date: '2026-03-25T16:07:57.007252'
step5_model: gpt-5.4
step6_date: '2026-03-25T16:08:06.596343'
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
- method/QAOA
- method/QUBO
- method/classical-simulation
- idea/quantum-advantage
- idea/near-term-feasibility
- idea/hybrid-approach
- contradiction/classical-vs-quantum
- contradiction/scalability
title: 'Bridging Quantum Algorithms and Classical Finance: Portfolio Optimization
  Using QAOA and QUBO Framework'
topic_tags:
- portfolio-optimisation
year: 2025
zotero_key: ''
---

## Abstract summary
The paper formulates a classical mean-variance portfolio optimization problem as a QUBO model and applies the Quantum Approximate Optimization Algorithm (QAOA), implemented via Qiskit, to optimize binary asset selection among NSE derivative instruments. Using expected returns and covariance-based risk from monthly turnover data, the authors compare quantum-inspired solutions with classical brute-force and convex solvers, showing that portfolios including Index Futures and Index Options achieve the best risk-adjusted performance. The work is positioned as a practical template for hybrid quantum-classical portfolio optimization under current quantum hardware constraints.
## Methodology
This conference paper presents an empirical, hybrid classical-quantum-inspired portfolio optimization study based on reformulating a classical mean-variance portfolio selection problem as a Quadratic Unconstrained Binary Optimization (QUBO) model and then solving it with both classical and QAOA-based approaches. The authors use binary asset-selection variables instead of continuous portfolio weights, with the objective combining covariance-based risk and expected returns under a risk-aversion parameter. The financial universe consists of four NSE derivative asset classes—Index Futures, Index Options, Stock Futures, and Stock Options—using monthly turnover data to derive month-over-month percentage returns, expected return vector, and covariance matrix. After preprocessing the data by removing or imputing missing/non-numeric values, the QUBO matrix is constructed and evaluated using two validation routes: exhaustive classical brute-force enumeration of all feasible 2-asset combinations and a quantum-inspired QAOA implementation in Qiskit. The study reports portfolio-level expected return, variance/risk, QUBO objective value, and Sharpe ratio, and compares the selected portfolios across all possible combinations. The paper appears to be a conference paper rather than a workshop short abstract, but it does not provide a detailed formal experimental section with implementation hyperparameters or actual execution on quantum hardware.

**Algorithms used:** QAOA, QUBO, brute force enumeration, binary integer quadratic programming
**Frameworks:** Qiskit, CVXPY

**Experimental setup:** The study uses a hybrid setup consisting of a classical brute-force solver and a QAOA-based quantum-inspired implementation via Qiskit to solve a 4-asset QUBO portfolio optimization problem. A classical CVXPY formulation is also described for solving the binary quadratic program. No real quantum processing unit is reported; the paper frames the QAOA component as quantum-inspired and discusses current hardware limitations, implying simulation/software-based experimentation rather than execution on actual quantum hardware.

**Dataset:** Monthly turnover data for equity derivatives from the National Stock Exchange of India (NSE), covering four derivative instruments: Index Futures, Index Options, Stock Futures, and Stock Options.
## Findings
- [supported] The paper formulates a 4-asset portfolio selection problem on NSE derivative instruments as a QUBO using expected monthly returns and the covariance matrix with a risk-aversion parameter λ = 0.5.
- [supported] Using classical exhaustive evaluation/CVXPY on all 2-asset combinations, the portfolio consisting of Index Futures and Index Options ([1,1,0,0]) achieved the lowest QUBO objective value of 19.02987.
- [supported] The Index Futures + Index Options portfolio produced expected monthly return 1.2747, portfolio variance 19.8423, and Sharpe ratio about 0.28616.
- [supported] Among individual assets, Stock Options had the highest expected monthly return (0.804489), while Index Options had the lowest individual variance (4.592590).
- [supported] The Stock Futures + Stock Options pair had the highest expected return (1.5748) but also the highest risk (32.3735) and a lower Sharpe ratio (0.276777), illustrating the return-risk trade-off.
- [supported] The highest Sharpe ratio in the comparison table is for the Index Options + Stock Options portfolio ([0,1,0,1]) at 0.287923, although the paper also emphasizes Index Futures + Index Options as the best by QUBO objective and near-top Sharpe ratio.
- [supported] The study's reported results are based on classical brute-force/CVXPY evaluation and a quantum-inspired QAOA workflow implemented via Qiskit; no execution on real quantum hardware is reported.
- [speculative] The authors argue that the QUBO-QAOA framework provides a practical template for scalable asset selection as quantum hardware matures.
- [speculative] The paper suggests quantum-enhanced or quantum-inspired models may improve financial decision-making and could offer competitive advantages in constrained portfolio optimization settings.
- [speculative] Claims about future gains in speed, quality, and scalability of portfolio optimization from QAOA depend on larger problem instances and more capable quantum hardware, which are not empirically demonstrated here.

**Results summary:** This conference paper applies a QUBO formulation of mean-variance portfolio optimization to four NSE derivative asset classes: Index Futures, Index Options, Stock Futures, and Stock Options. Using monthly turnover-derived returns and covariance estimates, the authors compare all six possible 2-asset portfolios with classical brute-force/CVXPY optimization and describe a QAOA-based quantum-inspired implementation in Qiskit. Empirically, the Index Futures + Index Options portfolio has the lowest QUBO objective (19.02987) with expected return 1.2747, variance 19.8423, and Sharpe ratio 0.28616, while Stock Futures + Stock Options has the highest return (1.5748) but also the highest risk (32.3735). The reported evidence supports feasibility of the QUBO modeling approach on a very small simulated/classically validated problem, but does not demonstrate quantum advantage or real-hardware performance.

**Performance claims:**
- Stock Options expected monthly return = 0.804489
- Stock Futures expected monthly return = 0.770428
- Index Futures expected monthly return = 0.651131
- Index Options expected monthly return = 0.623624
- Index Options individual variance = 4.592590 (lowest among assets)
- Stock Options individual variance = 8.244593 (highest among assets)
- Covariance between Stock Futures and Stock Options = 8.085391
- Risk-aversion parameter used in QUBO = 0.5
- Index Futures + Index Options: expected return = 1.2747, variance = 19.8423, QUBO objective = 19.02987, Sharpe ratio = 0.28616
- Index Options + Stock Futures: expected return = 1.3940, variance = 23.9519, QUBO objective = 22.98028, Sharpe ratio = 0.284835
- Index Options + Stock Options: expected return = 1.4280, variance = 24.5982, QUBO objective = 23.57861, Sharpe ratio = 0.287923
- Index Futures + Stock Futures: expected return = 1.4215, variance = 26.3644, QUBO objective = 25.35407, Sharpe ratio = 0.276846
- Index Futures + Stock Options: expected return = 1.4555, variance = 26.9691, QUBO objective = 25.90986, Sharpe ratio = 0.280272
- Stock Futures + Stock Options: expected return = 1.5748, variance = 32.3735, QUBO objective = 31.1335, Sharpe ratio = 0.276777
## Quantum advantage claim
**Classification:** speculative

The paper discusses QAOA and quantum-inspired optimization as promising for scalable portfolio selection, but the reported study is a tiny 4-asset case validated mainly with classical brute-force/CVXPY and Qiskit-based quantum-inspired methods. No real quantum hardware results, no runtime or scaling advantage over classical baselines, and no demonstrated quantum speedup are provided.
## Limitations
- Practical implementation is restricted to relatively tiny portfolios due to the limited qubit capacity of present-day quantum hardware.
- The study uses only four derivative instruments (Index Futures, Index Options, Stock Futures, Stock Options), resulting in a very small asset universe.
- Validation is performed using classical brute-force enumeration, which is only feasible for small problem sizes and does not demonstrate scalability.
- The optimization is based on monthly turnover-derived returns from NSE derivatives only, limiting generalizability across asset classes, markets, and frequencies.
- The portfolio formulation uses binary asset inclusion rather than continuous portfolio weights, which simplifies the real portfolio construction problem.
- The model considers a fixed risk-aversion parameter (λ = 0.5), so results may be sensitive to this choice and not robust across investor preferences.
- The paper does not report experiments on real quantum hardware; the implementation is described as quantum-inspired/Qiskit-based rather than demonstrating hardware execution.
- [inferred] No explicit discussion of hardware noise, decoherence, gate errors, or error mitigation is provided, leaving practical NISQ performance unclear.
- [inferred] No quantitative comparison of QAOA solution quality, runtime, approximation ratio, or convergence against strong classical heuristics beyond brute force/CVXPY is provided.
- [inferred] The empirical dataset size appears limited to several monthly observations, which may make estimated expected returns and covariance matrices unstable.
- [inferred] The study relies on historical turnover changes as a proxy for returns, which may not reflect investable payoff dynamics of the derivative instruments.
- [inferred] Transaction costs, liquidity constraints, slippage, taxes, and market impact are omitted, reducing practical realism for financial deployment.
- [inferred] The analysis is effectively static and single-period, so it does not capture rebalancing, path dependence, or changing market regimes.
- [inferred] Reproducibility is limited because the paper does not provide enough implementation detail such as QAOA circuit depth, mixer/cost Hamiltonian settings, optimizer choice, initialization, shot count, or random seeds.
- [inferred] There is no out-of-sample or backtesting evaluation, so the reported portfolio quality may reflect in-sample fitting rather than robust performance.
- [inferred] The claim of a 'robust template for scalable asset selection' is not empirically demonstrated on larger instances.
- [inferred] As a conference paper, page-limit constraints may have reduced methodological detail, ablation studies, and robustness analysis.
## Open questions
- How well does the QUBO-QAOA approach scale to larger asset universes beyond the four-asset example studied here?
- Will QAOA provide any practical advantage over advanced classical optimization heuristics for realistic portfolio sizes?
- How sensitive are the results to the choice of risk-aversion parameter and the exact QUBO encoding?
- How would the method perform when transaction costs, diversification rules, and regulatory constraints are included?
- Can the approach work effectively on real quantum hardware under noise and limited qubit connectivity?
- How robust are the findings across different markets, asset classes, and market regimes?
- Would dynamic or multi-period portfolio optimization materially change the relative value of the quantum approach?
- How should derivative-specific features such as leverage, expiry, and non-linear payoffs be incorporated into the optimization framework?
- Does using turnover-based return proxies produce economically meaningful portfolios compared with price- or P&L-based return definitions?
- What QAOA parameterization, depth, and classical optimizer choices are most effective for financial QUBO instances?

**Future work:**
- Extend the QUBO-QAOA framework to larger asset universes.
- Add multi-objective criteria such as transaction costs, sectoral diversification, and regulatory constraints.
- Investigate dynamic portfolio rebalancing using time-evolving QUBO matrices.
- Explore real-time implementation on quantum simulators or quantum hardware such as IBM Q or D-Wave.
- Incorporate quantum machine learning to build adaptive and self-improving portfolio optimization models.
- Conduct comparative studies across developed and emerging markets to assess transferability under different volatility and liquidity conditions.
- Develop more complex portfolio models with multi-period decision making.
- [inferred] Benchmark against stronger classical baselines and heuristics on larger instances to assess whether any quantum advantage exists.
- [inferred] Evaluate performance under realistic hardware noise and apply error-mitigation strategies.
- [inferred] Perform out-of-sample testing and historical backtesting to validate financial usefulness in practice.
- [inferred] Study sensitivity to hyperparameters such as risk aversion, QAOA depth, optimizer settings, and constraint penalties.
## Key ideas
- #idea:hybrid-approach — Mean-variance portfolio selection is reformulated as a QUBO for binary asset selection and paired with QAOA in a hybrid classical-quantum workflow.
- #idea:near-term-feasibility — On a very small 4-asset NSE derivatives example, the simulated QAOA/QUBO setup is presented as a practical template under current hardware constraints.
- #idea:hybrid-approach — Classical preprocessing computes expected returns and covariance matrices, while the quantum component targets the combinatorial asset-selection step.
- #idea:quantum-advantage — The paper speculates that QAOA-based portfolio optimisation could become more scalable and competitive as quantum hardware matures.
## Contradictions
- The paper suggests future quantum advantage for portfolio optimisation, but its own evidence is simulation-only on a 4-asset problem and relies on classical brute-force/CVXPY validation, contradicting any present claim of quantum superiority.
- The paper frames the QUBO-QAOA approach as a scalable template, yet the study is restricted to six 2-asset combinations from four instruments, so the empirical setup contradicts strong scalability implications.
- Although Index Futures + Index Options is emphasized as the best portfolio by QUBO objective, the reported highest Sharpe ratio belongs to Index Options + Stock Options, indicating tension between objective-optimality and risk-adjusted-performance interpretation.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->

## Experiment details
### Input
Input data consists of monthly NSE derivatives turnover observations for 4 asset classes (Index Futures, Index Options, Stock Futures, Stock Options). The exact number of months and time period are not specified. Preprocessing included removal or imputation of non-numeric and missing values. Month-over-month percentage changes in turnover were used to compute monthly returns, from which the expected returns vector and covariance matrix were estimated.

### Process
1. Start from the classical mean-variance portfolio objective balancing covariance-based risk and expected return. 2. Replace continuous portfolio weights with binary asset-selection variables. 3. Impose a cardinality constraint selecting k assets, with the reported experiments evaluating 2-asset portfolios. 4. Compute monthly returns from month-over-month turnover changes. 5. Estimate expected returns vector and covariance matrix from the processed data. 6. Construct the QUBO matrix using risk and return terms with risk-aversion parameter lambda = 0.5. 7. Solve the QUBO classically by exhaustive evaluation of all possible 2-asset combinations and also formulate it as a binary quadratic program in CVXPY. 8. Apply a QAOA-based quantum-inspired solver in Qiskit that iteratively adjusts circuit parameters to minimize the QUBO objective. 9. Compare resulting portfolios using expected return, variance, QUBO objective, and Sharpe ratio.

### Output
Outputs include the expected returns table for the 4 assets, the covariance matrix, the derived QUBO matrix, and comparative results for all 6 possible 2-asset portfolios. Reported evaluation metrics are expected monthly return, portfolio risk/variance, QUBO objective value, and Sharpe ratio. The classical optimal solution is reported as binary vector [1,1,0,0] (Index Futures + Index Options), with expected monthly return 1.2747, portfolio variance 19.8423, QUBO objective 19.02987, and Sharpe ratio about 0.286. Baseline comparison is against classical brute-force/CVXPY solutions rather than against other quantum algorithms.

### Parameters
- assets: 4
- portfolio_cardinality_k: 2
- risk_aversion_lambda: 0.5
- number_of_portfolio_combinations_evaluated: 6

### Hardware
N/A

### Reproducibility
No code repository or data link is provided. The data source (NSE monthly turnover data) and high-level preprocessing/optimization steps are described, and key matrices/results are reported, but critical implementation details for QAOA are missing, including simulator/backend, circuit depth, optimizer, shots, and convergence settings. Partial reproducibility is possible for the classical analysis, but the quantum-inspired component is not fully replicable from the paper alone.
