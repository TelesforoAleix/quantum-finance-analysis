---
aliases:
- 'QAMOO: Quantum Approximate Multi-Objective Optimization for Portfolio Management'
- QAMOO Quantum Approximate Multi
authors:
- Jahangir Khan
auto_detected: true
classification: ''
contradiction_flags:
- contradiction:scalability
- contradiction:classical-vs-quantum
doi: ''
evidence_type: ''
idea_tags:
- idea:quantum-advantage
- idea:near-term-feasibility
- idea:hybrid-approach
journal_or_venue: ''
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
step1_date: '2026-03-25T16:15:05.698171'
step1_model: gpt-5.1
step2_date: '2026-03-25T16:15:08.523521'
step2_model: gpt-5.1
step3_date: '2026-03-25T16:15:44.233264'
step3_model: gpt-5.4
step4_date: '2026-03-25T16:16:12.484273'
step4_model: gpt-5.4
step5_date: '2026-03-25T16:16:36.982279'
step5_model: gpt-5.4
step6_date: '2026-03-25T16:16:54.326940'
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
title: 'QAMOO: Quantum Approximate Multi-Objective Optimization for Portfolio Management'
topic_tags:
- portfolio-optimisation
- risk-modelling
year: 2026
zotero_key: ''
---

## Abstract summary
The paper proposes Qamoo, a quantum computing framework based on QAOA for solving multi-objective portfolio optimization problems involving return, risk, transaction costs, and diversification entropy. It uses Dirichlet-sampled scalarization weights, correlation-aware cost encoding, and portfolio-structured mixers with pre-trained parameters to efficiently approximate the Pareto frontier. The authors validate the approach on IBM Quantum hardware and compare it against classical multi-objective algorithms such as NSGA-II and MOEA/D in terms of hypervolume coverage, sample efficiency, and out-of-sample trading performance.
## Methodology
This January 2026 preprint presents an empirical quantum-finance framework, QAMOO, for multi-objective portfolio optimization and explicitly should be treated as a preprint. The method formulates portfolio selection as a binary optimization problem over a 10-asset technology-sector universe with four objectives: maximize expected return, minimize risk, minimize transaction costs, and maximize diversification entropy. These objectives are combined through stochastic weighted-sum scalarization, where weight vectors are sampled from a Dirichlet(1,1,1,1) distribution to explore the Pareto frontier. For each sampled weight vector, the scalarized problem is converted into a QUBO and then mapped to an Ising Hamiltonian. The optimization is solved using QAOA with fixed pre-trained variational parameters rather than per-instance training, relying on parameter transfer across similar portfolio instances. The circuit uses cost and mixer layers tailored to portfolio structure, including correlation-aware cost encoding and portfolio-structured mixers, and is designed to match IBM heavy-hex connectivity. The paper reports experiments on IBM Quantum hardware (ibm_fez and ibm_brisbane) and compares QAMOO against classical multi-objective baselines including NSGA-II, MOEA/D, epsilon-constraint, and randomized weighted-sum methods. Evaluation focuses on Pareto frontier quality and efficiency, using hypervolume, IGD, number of non-dominated solutions, runtime, and out-of-sample backtest metrics such as return, max drawdown, Sharpe, Sortino, and Calmar ratios.

**Algorithms used:** QAOA, QUBO, Ising Hamiltonian mapping, NSGA-II, MOEA/D, epsilon-constraint method, randomized weighted-sum method, Non-dominated sorting
**Frameworks:** IBM Quantum

**Experimental setup:** Experiments were conducted on IBM Quantum superconducting processors, specifically ibm_fez (156 qubits, Heron r2) and ibm_brisbane (127 qubits, Eagle r3), with circuits designed for heavy-hex topology compatibility. A 42-qubit subgraph is mentioned for portfolio optimization. The study also reports comparison to an MPS simulation as a noise-free or reduced-noise reference, including bond dimensions chi=50 and chi=20 in figures. The main empirical setup uses a 10-asset technology-sector portfolio, 5,000 randomly sampled Dirichlet weight vectors, and 5,000 shots per circuit execution.

**Dataset:** A technology sector portfolio comprising 10 assets, characterized by expected returns, individual volatilities, covariance matrix entries, and previous portfolio weights for transaction-cost calculation. The paper also reports out-of-sample backtest results for January 2026, but does not specify the exact data vendor, ticker list, sampling frequency, or training period.
## Experiment details
### Input
Financial input consists of stock data S = {(mu_i, sigma_i, Sigma_ij)} for a 10-asset technology-sector portfolio, plus previous portfolio weights for transaction-cost objective computation. Features include expected returns, covariance/correlation structure, and transaction-cost terms. The paper states out-of-sample evaluation in January 2026 but does not provide the exact source, asset identities, sample size beyond 10 assets, preprocessing pipeline, return estimation window, or covariance estimation period.

### Process
1. Define four portfolio objectives: expected return, risk, transaction cost, and diversification entropy. 2. Sample a multi-objective weight vector c from Dirichlet(1,1,1,1). 3. Build a scalarized objective F(w;c). 4. Convert the scalarized portfolio problem into a QUBO. 5. Map the QUBO to an Ising Hamiltonian using x_i = (1 - z_i)/2. 6. Construct a QAOA circuit of depth p using pre-trained parameter sets (beta*, gamma*) rather than optimizing parameters per instance. 7. Execute the circuit on IBM Quantum hardware with K=5,000 shots per sampled weight vector. 8. Decode measured bitstrings into binary asset-selection portfolios and normalize weights as w = x / ||x||_1. 9. Evaluate all four objectives for each sampled portfolio. 10. Aggregate all sampled solutions into an archive. 11. Apply non-dominated sorting to approximate the Pareto frontier. 12. Compare the resulting frontier against classical baselines using hypervolume, IGD, number of solutions, runtime, and out-of-sample portfolio performance. The paper also studies the effect of QAOA depth p from 2 to 6, with practical depth limited to p <= 6 by coherence constraints.

### Output
Reported outputs include Pareto frontier approximations, hypervolume, inverted generational distance (IGD), number of non-dominated solutions, runtime, hypervolume convergence plots, return-risk frontier visualizations, and a three-objective Pareto surface. Baseline comparisons are made against NSGA-II, MOEA/D, epsilon-constraint, randomized weighted-sum, and DPA-a in tables/figures. Out-of-sample backtest outputs include portfolio return, maximum drawdown, Sharpe ratio, Sortino ratio, and Calmar ratio for conservative, moderate, and aggressive QAMOO portfolios, compared with equal-weight and S&P 500 benchmarks.

### Parameters
- assets: 10
- objectives: 4
- weight_sampling_distribution: Dirichlet(1,1,1,1)
- samples_M: 5000
- shots_K: 5000
- qaoa_depths_evaluated: [2, 3, 4, 5, 6]
- practical_depth_limit: 6
- pretrained_parameters: {'p=3': {'beta': [0.393, 0.583, 0.261], 'gamma': [0.618, 0.423, 0.195], 'approx_ratio': 0.872}, 'p=4': {'beta': [0.401, 0.573, 0.312, 0.189], 'gamma': [0.624, 0.445, 0.287, 0.143], 'approx_ratio': 0.891}, 'p=5': {'beta': [0.398, 0.561, 0.324, 0.202, 0.134], 'gamma': [0.631, 0.458, 0.301, 0.178, 0.092], 'approx_ratio': 0.908}, 'p=6': {'beta': [0.395, 0.554, 0.332, 0.215, 0.148, 0.089], 'gamma': [0.627, 0.463, 0.312, 0.195, 0.118, 0.065], 'approx_ratio': 0.921}}
- mps_bond_dimensions_reported: [20, 50]
- qubit_subgraph: 42

### Hardware
IBM Quantum hardware is explicitly used: ibm_fez (156-qubit Heron r2) and ibm_brisbane (127-qubit Eagle r3), both superconducting devices with heavy-hex topology. The paper states circuits are designed to exploit heavy-hex connectivity and that sparse connectivity allows Rzz gates to be scheduled in three non-overlapping layers per QAOA round, reducing the need for SWAP gates. A 42-qubit subgraph is referenced for portfolio optimization. MPS simulation with bond dimension chi=50 is used as a comparison/noise-free limit. No detailed transpilation settings, error mitigation settings, compiler versions, or cloud execution configuration are provided.

### Reproducibility
Preprint with moderate but incomplete reproducibility. The paper provides the high-level algorithm, mathematical formulation, pseudocode, hardware names, shot count, sample count, and pre-trained QAOA parameters for depths 3-6. However, no code repository is given, the exact 10 assets and data source are not specified, preprocessing and train/test split details are missing, and implementation details for baselines and circuit compilation are incomplete. Replication would be difficult without additional supplementary material.
## Findings
- [supported] On a 10-asset technology-sector portfolio, Qamoo on IBM hardware (ibm_fez) reports hypervolume 0.847 versus 0.821 for NSGA-II, 0.815 for MOEA/D, and 0.831 for the epsilon-constraint baseline.
- [supported] Qamoo (ibm_fez) reports inverted generational distance (IGD) of 0.0123 versus 0.0187 for NSGA-II, 0.0203 for MOEA/D, and 0.0156 for the epsilon-constraint method.
- [supported] Qamoo (ibm_fez) reports 156 Pareto solutions in 4.2 minutes, compared with 127 solutions in 12.4 minutes for NSGA-II, 98 in 8.7 minutes for MOEA/D, and 134 in 10.0 minutes for the epsilon-constraint method.
- [supported] The paper reports that hardware execution on ibm_fez slightly outperformed its own MPS simulation baseline in hypervolume (0.847 vs 0.842) and IGD (0.0123 vs 0.0131).
- [supported] Out-of-sample backtests for Qamoo portfolios report Sharpe ratios of 0.68 (conservative), 0.72 (moderate), and 0.65 (aggressive), all above equal-weight (0.51) and S&P 500 (0.42) in the reported January 2026 test period.
- [supported] The reported out-of-sample returns are 8.2%, 12.4%, and 18.7% for conservative, moderate, and aggressive Qamoo portfolios, respectively, versus 10.1% for equal weight and 6.8% for the S&P 500 over the stated test period.
- [speculative] The authors claim Qamoo discovers the complete Pareto frontier through quantum parallel exploration and adaptive Dirichlet weight sampling.
- [speculative] The paper claims QAOA with fixed pre-trained parameters can generate both supported and non-supported Pareto-optimal solutions for portfolio optimization.
- [speculative] The authors argue that correlation-aware cost encoding and portfolio-structured mixer Hamiltonians improve financial relevance and constraint handling, but no ablation study isolates these contributions.
- [speculative] The paper claims parameter transfer learning eliminates expensive per-instance optimization and generalizes across portfolio instances, but direct comparative evidence is limited in the presented experiments.
- [speculative] The authors claim practical quantum advantage in solution quality and computational efficiency for institutional portfolio management, but the evidence is limited to a small 10-asset case study and lacks rigorous scaling validation.
- [speculative] The claim that Qamoo requires 10x fewer objective function evaluations than NSGA-II is asserted in the abstract and discussion, but the paper does not provide a transparent accounting table for evaluation counts.
- [speculative] The claim that Qamoo is 66% faster for portfolios with n >= 15 assets is not directly supported by the reported experiments, which are described for a 10-asset portfolio.
- [speculative] The paper attributes hardware outperformance over simulation to beneficial noise increasing sampling diversity, but this causal explanation is not experimentally isolated.
- [speculative] The authors suggest that quantum-enhanced multi-objective optimization will yield greater advantages for larger portfolio universes and more complex objectives as hardware improves.

**Results summary:** This preprint presents Qamoo, a QAOA-based framework for multi-objective portfolio optimization over return, risk, transaction cost, and diversification. The reported experiments use IBM Quantum hardware (127-156 qubits) and compare against classical multi-objective baselines on a 10-asset technology-sector portfolio. Empirically, the paper reports better Pareto-front quality for Qamoo than NSGA-II and MOEA/D using hypervolume and IGD, with shorter runtime than the listed classical baselines in the presented setup. It also reports out-of-sample backtest metrics with Sharpe ratios between 0.65 and 0.72 for selected Qamoo portfolios. However, because this is a preprint and several broader claims about complete Pareto discovery, practical quantum advantage, beneficial noise, and scaling to larger portfolios are not fully substantiated by the limited experimental scope, those broader advantage claims should be treated as speculative.

**Performance claims:**
- Hypervolume: Qamoo (ibm_fez) 0.847 vs Qamoo (MPS chi=50) 0.842 vs NSGA-II 0.821 vs MOEA/D 0.815 vs epsilon-constraint 0.831
- IGD: Qamoo (ibm_fez) 0.0123 vs Qamoo (MPS chi=50) 0.0131 vs NSGA-II 0.0187 vs MOEA/D 0.0203 vs epsilon-constraint 0.0156
- Pareto solutions found: Qamoo (ibm_fez) 156 vs Qamoo (MPS chi=50) 148 vs NSGA-II 127 vs MOEA/D 98 vs epsilon-constraint 134
- Runtime: Qamoo (ibm_fez) 4.2 min vs NSGA-II 12.4 min vs MOEA/D 8.7 min vs epsilon-constraint 10.0 min vs DPA-a 8.0 min
- Reported hypervolume improvement over NSGA-II: 3.2%
- Reported objective-function-evaluation reduction: 10x fewer than NSGA-II
- Reported runtime improvement: 66% faster for portfolios with n >= 15 assets
- Quantum hardware used: ibm_fez (156 qubits, Heron r2) and ibm_brisbane (127 qubits, Eagle r3)
- Experimental sampling: 5,000 random weight vectors and 5,000 shots per circuit
- Out-of-sample Sharpe ratios: 0.68 (conservative), 0.72 (moderate), 0.65 (aggressive), vs 0.51 (equal weight) and 0.42 (S&P 500)
- Out-of-sample returns: 8.2%, 12.4%, 18.7% for Qamoo conservative/moderate/aggressive vs 10.1% equal weight and 6.8% S&P 500
- Out-of-sample max drawdowns: -6.4%, -11.2%, -19.8% for Qamoo conservative/moderate/aggressive vs -14.3% equal weight and -8.9% S&P 500
- Pre-trained QAOA approximate ratios by depth: p=3 0.872, p=4 0.891, p=5 0.908, p=6 0.921
## Quantum advantage claim
**Classification:** speculative

The paper explicitly claims practical quantum advantage and includes hardware results, but it is a preprint with evidence limited to a small 10-asset experiment, incomplete support for some headline claims (e.g., 10x fewer evaluations, 66% faster for n>=15), and no rigorous demonstration of scalable advantage over best classical methods. Therefore the advantage claim is best classified as speculative.
## Limitations
- Coherence times limit practical circuit depth to p ≤ 6
- Portfolio representation uses binary asset selection; continuous weights require post-processing
- Hardware connectivity constraints require circuit transpilation
- Experiments are limited to a 10-asset technology-sector portfolio
- [inferred] Validation appears restricted to a narrow problem setting, making generalization to broader asset universes, other sectors, and different market regimes unclear
- [inferred] Out-of-sample evaluation is reported only for January 2026, which is too short to establish robustness across market cycles
- [inferred] The claim of production readiness is not fully supported by large-scale production deployment evidence
- [inferred] Comparisons are made against selected classical baselines, but there is no clear comparison to stronger modern portfolio optimization solvers or commercial-grade optimizers
- [inferred] The use of pre-trained QAOA parameters assumes transferability across portfolio instances, but robustness of this assumption is not thoroughly validated
- [inferred] The weighted-sum scalarization approach may bias frontier discovery despite claims of complete Pareto recovery, especially in higher-dimensional objective spaces
- [inferred] Reported hardware advantage may be sensitive to noise, calibration state, and shot budget, reducing reproducibility
- [inferred] The paper does not provide enough implementation detail, code, or data access information to ensure reproducibility
- [inferred] The beneficial-noise interpretation is speculative and may not generalize across devices or runs
- [inferred] The study does not quantify transaction costs, slippage, turnover, and execution frictions in a realistic institutional setting
- [inferred] Lack of peer review; as a preprint, the claims and experimental results have not yet undergone independent scholarly validation
## Open questions
- How does Qamoo scale beyond 10 assets and to the claimed regime of n ≥ 15 assets or much larger institutional portfolios?
- Will the reported hypervolume and runtime advantages persist under different market conditions, sectors, and longer backtest horizons?
- How robust are the pre-trained QAOA parameters across different portfolio distributions and objective formulations?
- Can the method reliably recover the full Pareto frontier in practice for four-objective financial problems, including non-supported solutions?
- To what extent are the results driven by hardware noise, and when does noise become harmful rather than beneficial?
- How sensitive is performance to the Dirichlet weight-sampling scheme and the choice of scalarization distribution?
- What is the impact of estimation error in expected returns and covariance matrices on solution quality?
- How would the framework perform with realistic portfolio constraints such as lot sizes, leverage, sector caps, and regulatory rules?
- Can continuous portfolio weights be incorporated natively rather than through post-processing?
- How reproducible are the results across repeated runs, different IBM devices, and different calibration windows?

**Future work:**
- Develop fault-tolerant implementations
- Support continuous portfolio weights via quantum-enhanced gradient methods
- Extend the framework to multi-period dynamic optimization
- [inferred] Evaluate on larger and more diverse asset universes, including multi-sector and real institutional-scale portfolios
- [inferred] Conduct longer-horizon out-of-sample backtests across multiple market regimes
- [inferred] Benchmark against stronger state-of-the-art classical optimizers and hybrid quantum-classical baselines
- [inferred] Study robustness of parameter transfer learning across datasets, objectives, and market environments
- [inferred] Investigate noise mitigation and systematically characterize when hardware noise helps or hurts Pareto discovery
- [inferred] Improve reproducibility by releasing code, circuits, datasets, and detailed experimental protocols
- [inferred] Incorporate more realistic trading frictions and operational constraints into the optimization and backtesting pipeline
## Key ideas
- #idea:quantum-advantage — QAMOO uses QAOA on IBM hardware to approximate a four-objective portfolio Pareto frontier and reports better hypervolume, IGD, runtime, and number of non-dominated solutions than NSGA-II, MOEA/D, and epsilon-constraint on a 10-asset case.
- #idea:hybrid-approach — The workflow is hybrid: classical Dirichlet weight sampling, scalarization, QUBO/Ising construction, and non-dominated sorting are combined with quantum QAOA sampling for each scalarized portfolio instance.
- #idea:near-term-feasibility — The method is explicitly designed for NISQ hardware, using heavy-hex-compatible circuits, a 42-qubit subgraph, shallow depths up to p=6, and execution on ibm_fez and ibm_brisbane.
- #idea:near-term-feasibility — Pre-trained QAOA parameters are transferred across many scalarized portfolio instances to avoid per-instance variational training, presented as a practical runtime-saving strategy.
- #idea:quantum-advantage — The paper claims practical quantum advantage for institutional portfolio management, including improved Pareto-front quality and favorable January 2026 backtest metrics versus equal-weight and S&P 500 benchmarks.
- #idea:quantum-advantage — The authors further suggest hardware noise may have improved sampling diversity because ibm_fez slightly outperformed the MPS simulation baseline on reported hypervolume and IGD.
## Contradictions
- The paper claims practical quantum advantage, 10x fewer objective evaluations, and faster performance for larger portfolios, but the evidence is limited to a single 10-asset preprint case study; this creates a #contradiction:scalability between headline claims and demonstrated scope.
- The paper presents quantum superiority over selected classical baselines, yet it does not benchmark against stronger modern or commercial portfolio optimizers and provides incomplete accounting for evaluation counts and runtime fairness; this supports #contradiction:classical-vs-quantum.
- The claim of complete Pareto frontier recovery conflicts with the use of weighted-sum scalarization, which is known to risk missing non-supported Pareto points in multi-objective optimization; this is an internal methodological tension tied to #contradiction:classical-vs-quantum.
- The suggestion that hardware noise is beneficial because ibm_fez slightly outperforms MPS simulation is not experimentally isolated and may contradict the broader expectation that noise degrades variational algorithm performance.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
