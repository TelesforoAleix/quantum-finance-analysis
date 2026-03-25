---
aliases:
- Quantum Algorithms for Portfolio Optimization
- Quantum Algorithms Portfolio Optimization
authors:
- Iordanis Kerenidis
- Anupam Prakash
- Dániel Szilágyi
auto_detected: true
classification: ''
contradiction_flags: []
doi: 10.1145/3318041.3355465
evidence_type: ''
idea_tags:
- idea:quantum-advantage
- idea:near-term-feasibility
- idea:hybrid-approach
journal_or_venue: 'AFT ''19: Proceedings of the 1st ACM Conference on Advances in
  Financial Technologies'
methodology_tags:
- HHL
- quantum-simulation
- variational
paper_type: ''
quantum_advantage_claim: theoretical
related_papers: []
relevance_phase1: high
relevance_phase3: high
source_type: conference-paper
source_type_confidence: high
step1_date: '2026-03-25T15:51:47.565699'
step1_model: gpt-5.1
step2_date: '2026-03-25T15:51:52.393447'
step2_model: gpt-5.1
step3_date: '2026-03-25T15:52:30.380626'
step3_model: gpt-5.4
step4_date: '2026-03-25T15:52:58.541551'
step4_model: gpt-5.4
step5_date: '2026-03-19T22:52:55.821918'
step5_model: Mistral-Large-3
step6_date: '2026-03-19T22:52:59.667052'
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
- method/HHL
- method/quantum-simulation
- method/variational
- idea/quantum-advantage
- idea/near-term-feasibility
- idea/hybrid-approach
title: Quantum Algorithms for Portfolio Optimization
topic_tags:
- portfolio-optimisation
year: 2019
zotero_key: ''
---

## Abstract summary
The paper presents a quantum algorithm for the constrained portfolio optimization problem, including positivity and budget constraints, by reducing it to a second-order cone program and applying a quantum interior-point method. The authors analyze the algorithm’s runtime in terms of problem-dependent conditioning parameters and show that, under reasonable assumptions, it offers a polynomial speedup over classical interior-point solvers. They also report numerical experiments on real financial data suggesting that these parameters behave favorably in practice, leading to an approximate O(n) speedup for large portfolios compared to classical methods.
## Methodology
This conference paper is primarily a peer-reviewed theoretical/algorithmic study with supporting numerical experiments. The authors formulate constrained portfolio optimization in the Markowitz setting with positivity and budget constraints, estimate the mean return vector and covariance structure from historical asset returns, and then reformulate the quadratic portfolio problem as a second-order cone program (SOCP). They build their approach on a quantum short-step interior-point method for SOCPs, itself relying on quantum linear system solving, block encodings, QRAM-based data structures, norm estimation, and quantum state tomography to approximately solve the Newton systems arising at each interior-point iteration. The paper provides formal runtime and convergence guarantees, including dependence on the number of assets, number of constraints, condition number, tomography precision, and a block-encoding parameter. In addition to the theoretical analysis, the authors run classical simulations intended to estimate problem-dependent factors in the runtime bound, especially the Newton-system condition number and tomography precision behavior. These experiments use historical S&P 500 stock data, solve simplified constrained portfolio instances, inject Gaussian noise to emulate tomography error in the quantum algorithm, compare simulated classical and quantum interior-point trajectories, and fit empirical scaling laws for the observed complexity.

**Algorithms used:** HHL, quantum linear system solver, quantum short-step interior-point method, SOCP interior-point method, quantum state tomography, block encoding
**Frameworks:** QRAM

**Experimental setup:** The empirical component consists of numerical simulations rather than execution on real quantum hardware. The authors simulate the quantum algorithm by solving the portfolio optimization problem classically while adding Gaussian noise calibrated to the tomography precision required by their convergence theorem. They compare this noisy 'quantum' simulation against the corresponding classical short-step interior-point method, track duality gap, tomography precision, and Newton-matrix condition number across iterations, and estimate average-case complexity from observed parameter values.

**Dataset:** Historical stock data from the cvxportfolio repository, containing daily data for S&P 500 companies over 2007-2016. For one main experiment, the dataset was subsampled to 50 companies and the first 100 trading days were used. For scaling experiments, random subsets of 100 companies and random time windows of 10 to 500 days were sampled.
## Findings
- [supported] The paper presents the first quantum algorithm for constrained portfolio optimization, with a running time of e^O(n√r ζ κ / δ² log(1/ϵ)), where n is the number of assets, r is the number of constraints, and ζ, κ, δ are problem-dependent parameters.
- [supported] The quantum algorithm achieves a polynomial speedup over classical algorithms, which have a complexity of e^O(n^ω √r log(1/ϵ)) (ω ≈ 2.373 theoretically, closer to 3 in practice).
- [speculative] The authors suggest that for most instances, the quantum algorithm can achieve an O(n) speedup over classical counterparts, based on experimental observations.
- [supported] The algorithm reduces the constrained portfolio optimization problem to Second Order Cone Programs (SOCP) and uses a quantum interior point method for SOCPs, enabling the handling of positivity and budget constraints.
- [supported] Experimental results indicate that the condition number κ of the Newton matrix does not grow significantly with problem size, and the factor 1/δ² grows roughly linearly with n.
- [supported] The duality gap decreases multiplicatively by a factor of σ = (1 - α/√r) per iteration, with α close to the classical constant χ = 0.1, suggesting similar convergence rates for quantum and classical algorithms.
- [speculative] The paper claims that quantum computers could offer significant speedups for large-scale portfolio optimization problems where the number of assets n is large and the number of constraints r is small.
- [supported] The quantum algorithm ensures that the solution satisfies inequality constraints (x ≥ 0) and equality constraints to precision δ, with infeasibility bounded by δ ∥A∥.

**Results summary:** The paper introduces a quantum algorithm for constrained portfolio optimization, leveraging a quantum interior point method for Second Order Cone Programs (SOCP). The algorithm demonstrates a polynomial speedup over classical methods, with a theoretical running time of e^O(n√r ζ κ / δ² log(1/ϵ)). Experimental results suggest that the quantum algorithm can achieve an O(n) speedup for most problem instances, particularly when the number of assets is large and constraints are few. The condition number κ and tomography precision δ were observed to behave favorably, with κ not growing significantly with problem size and 1/δ² scaling linearly with n. The duality gap convergence rate is comparable to classical methods, indicating practical viability. The algorithm is notable for its ability to handle complex constraints like positivity and budget limits, which are common in real-world portfolio optimization.

**Performance claims:**
- Running time: e^O(n√r ζ κ / δ² log(1/ϵ)) for the quantum algorithm
- Classical algorithm complexity: e^O(n^ω √r log(1/ϵ)) (ω ≈ 2.373 theoretically, closer to 3 in practice)
- Observed O(n) speedup over classical algorithms for most instances
- Duality gap reduction by a factor of (1 - α/√r) per iteration, with α close to 0.1
- Condition number κ growth observed as O(1/ν^α) for α < 0.5 over T iterations
- 1/δ² grows roughly linearly with problem size n
## Quantum advantage claim
**Classification:** theoretical

The quantum advantage is claimed based on theoretical complexity analysis and experimental simulations, showing a polynomial speedup over classical algorithms. The advantage is not demonstrated on real quantum hardware but is supported by numerical experiments and theoretical guarantees. The speedup is contingent on problem-dependent parameters like condition number κ and tomography precision δ, which were observed to behave favorably in simulations.
## Limitations
- Theoretical speedup assumes bounded condition number κ of the Newton matrices, which may not hold in all practical scenarios [inferred]
- Algorithm relies on quantum linear system solvers, which require efficient block encoding of matrices; constructing these encodings may be non-trivial for arbitrary financial datasets [inferred]
- Experiments limited to synthetic or subsampled real-world data (50 companies over 100 days), which may not generalize to full-scale financial datasets [inferred]
- Quantum algorithm's performance depends on problem-dependent parameters (δ, κ, ζ) that are not fully characterized for all portfolio optimization instances
- Tomography errors in quantum state reconstruction lead to approximate solutions, with equality constraints satisfied only to precision δ
- No empirical validation on real quantum hardware; experiments are classical simulations with added Gaussian noise to mimic tomography errors [inferred]
- Conference paper page limits may have constrained detailed discussion of failure cases or edge conditions [inferred]
- Algorithm assumes direct access to the square root of the covariance matrix (M), which may not be readily available in all financial datasets [inferred]
- Theoretical speedup is contingent on the number of constraints (r) being small relative to the number of assets (n), limiting applicability to highly constrained problems [inferred]
- No comparison with state-of-the-art classical solvers (e.g., commercial QP solvers) to benchmark practical speedups [inferred]
- Assumes existence of strictly feasible solutions for the SOCP formulation, which may not hold for all real-world portfolio problems [inferred]
## Open questions
- How does the quantum algorithm perform when the number of constraints (r) scales with the number of assets (n)?
- What is the impact of hardware noise and decoherence on the algorithm's convergence and solution quality on near-term quantum devices?
- Can the algorithm be adapted to handle dynamic or time-varying constraints (e.g., real-time portfolio rebalancing)?
- How do the problem-dependent parameters (κ, ζ, δ) behave for large-scale, real-world financial datasets?
- What are the trade-offs between tomography precision (δ) and the algorithm's runtime for practical applications?
- Can the quantum speedup be maintained when incorporating transaction costs or other real-world frictions?
- How does the algorithm compare to classical methods in terms of robustness to input data noise or missing data?
- What are the implications of the algorithm's approximate constraint satisfaction for regulatory compliance in financial applications?

**Future work:**
- Test the algorithm on real quantum hardware (e.g., IBM Eagle or future processors) to validate theoretical speedups
- Extend the algorithm to handle more complex constraints (e.g., transaction costs, regulatory limits, or multi-period optimization)
- Develop hybrid quantum-classical approaches to mitigate the impact of tomography errors and hardware noise
- Benchmark the algorithm against state-of-the-art classical solvers (e.g., MOSEK, ECOS) on large-scale financial datasets
- Investigate the algorithm's performance on other financial optimization problems (e.g., option pricing, risk management)
- Explore methods to reduce the dependence of runtime on problem-dependent parameters (κ, ζ, δ)
- Develop techniques to ensure strict feasibility of solutions for regulatory compliance
- Apply the algorithm to dynamic portfolio optimization problems with time-varying constraints
- Investigate the use of quantum data structures (e.g., QRAM) for real-time financial data processing
## Key ideas
- #idea:quantum-advantage — Quantum interior point method achieves polynomial speedup (e^O(√r * n * κ * ζ / δ² * log(1/ϵ))) over classical algorithms (e^O(n^ω * √r * log(1/ϵ))) for constrained portfolio optimization with positivity and budget constraints
- #idea:near-term-feasibility — Algorithm is theoretically designed for NISQ-era applicability but requires bounded condition numbers and problem-specific parameters (κ, δ, ζ) for practical speedup
- #idea:hybrid-approach — Quantum linear system solvers and tomography are used iteratively, suggesting potential for hybrid quantum-classical integration to mitigate data encoding and noise challenges
- #limitation:qubit-count — Performance depends on large asset counts (n) and small constraint counts (r), limiting scalability for highly constrained real-world problems
- #limitation:noise — Quantum tomography and linear system solvers introduce errors that may degrade solution feasibility (equality constraints satisfied only to precision δ) and optimality
- #limitation:no-empirical-validation — Claims are theoretical/simulated; no validation on real quantum hardware, only classical simulations with Gaussian noise
- #limitation:data-encoding — Requires QRAM for efficient data encoding, which is not yet available in current quantum hardware
## Contradictions
<!-- Step 6 output — where this paper contradicts others -->

## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->

## Experiment details
### Input
Financial input consists of historical daily returns for S&P 500 stocks from the cvxportfolio dataset (2007-2016). In the first simulation, 50 companies were selected and only the first 100 days were used to compute the mean return vector mu and covariance matrix Sigma for the simplified portfolio problem min x^T Sigma x subject to mu^T x = R and x >= 0. In later scaling experiments, instances were generated by choosing 100 random companies and a random subinterval length t uniformly from 10 to 500 days; the target optimization precision was fixed at epsilon = 0.1. The paper states that mu and Sigma (or equivalently M such that Sigma = M M^T) are computed from the historical returns.

### Process
1. Compute the mean return vector and covariance information from historical asset returns. 2. Formulate the simplified constrained portfolio optimization problem without additional linear budget constraints for the experiments. 3. Solve the problem using the classical short-step interior-point method and, separately, simulate the quantum version by injecting Gaussian noise whose magnitude matches the tomography precision required by the convergence theorem. 4. Across iterations, record the duality gap nu, the tomography precision parameter delta, and the condition number kappa of the Newton matrix. 5. Plot duality gap and tomography precision versus iteration count for classical and simulated quantum runs, and plot condition number versus iteration count. 6. For scaling analysis, repeatedly sample random portfolio instances from the dataset, solve each instance to fixed precision epsilon = 0.1 using the simulated Algorithm 2, and record worst/final values of kappa, delta, and zeta. 7. Fit power-law relationships to empirical observations, including growth of 1/delta^2 with problem size and overall runtime scaling implied by the theoretical complexity expression. No shot counts, variational optimization loops, or QPU execution details are reported because the study is based on theory plus classical simulation.

### Output
Outputs are reported as convergence and complexity diagnostics rather than portfolio performance metrics. The paper reports plots of duality gap and tomography precision versus iteration count for classical and simulated quantum algorithms, plots of Newton-matrix condition number versus iteration count, distributions of condition numbers across sampled instances, empirical growth of 1/delta^2 with problem size, and an estimated average-case runtime scaling of approximately O(n^2.387) with a 95% confidence interval. The main comparison baseline is the classical short-step interior-point method with practical complexity O(n^3.5), against which the authors argue the quantum method could achieve nearly O(n) speedup for most instances.

### Parameters
- assets_main_experiment: 50
- time_horizon_main_experiment_days: 100
- scaling_experiment_companies: 100
- scaling_experiment_time_window_days: {'distribution': 'uniform', 'min': 10, 'max': 500}
- epsilon_scaling_experiments: 0.1
- noise_model: Gaussian noise added to simulate tomography error
- iterations: T iterations of short-step IPM; theoretically O(sqrt(r) log(n/epsilon))
- sigma_classical_ipm: 1 - 0.1/sqrt(r)

### Hardware
{'hardware_type': 'classical simulation only', 'qpu_used': None, 'simulator': 'custom numerical simulation of the quantum algorithm via noisy classical IPM trajectories', 'cloud_provider': None, 'transpilation_settings': None}

### Reproducibility
The paper gives substantial theoretical detail and identifies the data source (cvxportfolio), dataset period, subsampling choices, and key experimental procedure, so the simulations are partially reproducible. However, no code repository, exact random seeds, implementation details, or full parameter settings for all experiments are provided, which limits exact replication.
