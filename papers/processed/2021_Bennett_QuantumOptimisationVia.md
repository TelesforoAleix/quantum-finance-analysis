---
aliases:
- Quantum optimisation via maximally ampliﬁed states
- Quantum optimisation via maximally
authors:
- T. Bennett
- J. B. Wang
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
- QUBO
- grover
- quantum-walk
- classical-simulation
paper_type: ''
quantum_advantage_claim: speculative
related_papers: []
relevance_phase1: high
relevance_phase3: medium
source_type: preprint
source_type_confidence: high
step1_date: '2026-03-25T15:52:56.156910'
step1_model: gpt-5.1
step2_date: '2026-03-25T15:53:01.882321'
step2_model: gpt-5.1
step3_date: '2026-03-25T15:53:47.621454'
step3_model: gpt-5.4
step4_date: '2026-03-25T15:54:18.744078'
step4_model: gpt-5.4
step5_date: '2026-03-25T15:54:51.326825'
step5_model: gpt-5.4
step6_date: '2026-03-25T15:55:04.420540'
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
- method/QUBO
- method/grover
- method/quantum-walk
- method/classical-simulation
- idea/quantum-advantage
- idea/near-term-feasibility
- idea/hybrid-approach
- contradiction/classical-vs-quantum
- contradiction/scalability
title: Quantum optimisation via maximally ampliﬁed states
topic_tags:
- portfolio-optimisation
year: 2022
zotero_key: ''
---

## Abstract summary
The paper introduces the Maximum Amplification Optimisation Algorithm (MAOA), a near-term quantum algorithm for combinatorial optimisation that focuses on maximally amplifying optimal solutions under a fixed circuit-depth constraint. By using a binary marking function on a complete graph and analytically chosen Grover-like parameters, MAOA avoids the costly variational optimisation used in QAOA/QWOA while achieving maximal amplitude amplification of high-quality solutions for a given number of iterations. The authors compare MAOA against a restricted Grover adaptive search (RGAS) and classical random sampling on vehicle routing, portfolio optimisation, and large normally distributed test problems, showing substantial speedups over classical sampling and consistent outperformance of RGAS, with an analytically derived linear-in-depth speedup bound relative to random sampling.
## Methodology
This preprint presents a new quantum optimization method, the Maximum Amplification Optimisation Algorithm (MAOA), and evaluates it primarily through theoretical derivation plus extensive numerical simulation rather than hardware experiments. The paper frames MAOA within the Quantum Walk Optimisation Algorithm (QWOA) formalism, then derives that under restricted circuit depth, maximal amplification of high-quality solutions is achieved by applying a binary marking function over a complete graph with repeated fixed parameters equivalent to truncated Grover search. The authors compare MAOA against Grover Adaptive Search (GAS), a restricted-depth variant they introduce called RGAS, and classical random sampling. Their empirical evaluation uses simulated combinatorial optimization tasks: a capacitated vehicle routing problem (CVRP), a portfolio optimization problem based on the Markowitz model, and an abstract arbitrarily large problem with normally distributed solution qualities. Performance is assessed via repeated Monte Carlo-style simulations (10,000 runs per setting) that use precomputed or analytically specified quality distributions and Grover probability formulas to model marked-state measurement outcomes. Success probability is plotted against computational effort, where effort is defined by the number of objective-function calls, with each amplified-state preparation/measurement costing 2r+1 for rotation count r. The study also includes numerical optimization analyses of graph structure, degeneracy, and parameter landscapes using random initializations and Nelder-Mead optimization to justify the MAOA design and to compare amplification behavior with QWOA-like alternatives.

**Algorithms used:** MAOA, QWOA, QAOA, Grover adaptive search, RGAS, Grover search, Nelder-Mead

**Experimental setup:** All results are based on numerical simulation and analytical modeling; no real quantum hardware is used. The paper simulates truncated Grover/QWOA-style amplitude amplification under restricted circuit depth. For benchmark curves, 10,000 simulations are run per setting. Additional optimization-landscape studies generate many random parameter initializations and refine them with Nelder-Mead. The work also notes use of Pawsey Supercomputing Centre resources.

**Dataset:** Three main data settings are used: (1) a synthetic 10-location capacitated vehicle routing problem with randomly generated package demands, cost matrix, and vehicle capacity; (2) a portfolio optimization dataset built from daily adjusted close prices for 20 ASX.20 stocks from 01/01/2019 to 31/12/2020; and (3) an analytically defined arbitrarily large problem whose solution qualities follow the standard normal distribution.
## Findings
- [supported] The paper introduces the Maximum Amplification Optimisation Algorithm (MAOA), a near-term quantum optimization method that seeks to maximize amplification of optimal or near-optimal solutions under restricted circuit depth.
- [speculative] The authors argue that optimizing amplification of optimal solutions is a more appropriate objective than optimizing expectation value of solution quality for large combinatorial optimization problems.
- [supported] Numerical simulations indicate that MAOA consistently outperforms the restricted Grover adaptive search (RGAS) on the tested vehicle routing, portfolio optimization, and synthetic normally distributed optimization problems.
- [supported] Numerical simulations indicate that both MAOA and RGAS outperform classical random sampling in finding optimal solutions on the tested instances.
- [supported] For binary marking on a complete graph with small marked-solution ratio, the authors derive that a single iteration achieves maximum amplification of 9 at parameters gamma = pi and t = pi/N.
- [supported] The paper claims that repeated application of gamma = pi and t = pi/N on a binary-marked complete graph reproduces truncated Grover search behavior, yielding marked-state amplification of (2r + 1)^2 in the low-convergence regime.
- [supported] Simulations on a complete graph with N = 10^8 and 10 marked solutions show that binary partitioning amplifies marked solutions more effectively than 3-, 5-, or 10-part partitions.
- [supported] The authors report numerical convergence of MAOA performance to the theoretically derived upper bound corresponding to amplification (2r + 1)^2.
- [speculative] The paper argues that MAOA avoids the computationally expensive variational optimization required by QAOA/QWOA and therefore may provide more practical speedup in near-term settings.
- [speculative] The authors claim MAOA represents the upper limit of speedup available at a given restricted circuit depth within deterministic amplitude-amplification-based algorithms.
- [supported] In the large-problem analysis, the paper derives a success-probability model for MAOA, PQ(e, mu, r) = 1 - (1 - mu(2r + 1)^2)^(e/(2r + 1)), and simulation results on synthetic normally distributed spaces are reported to match this prediction in the small-target-ratio regime.
- [speculative] The paper claims MAOA can support multi-stage optimization in multidimensional problems, illustrated by fixing a risk threshold and optimizing return in portfolio optimization.
- [speculative] The paper claims repeated MAOA sampling can yield a useful set of near-optimal solutions, potentially beneficial when multiple high-quality alternatives are desired.
- [speculative] The paper states that MAOA can produce optimal solutions faster than classical exhaustive search, but this claim is based on simulation/analysis rather than real hardware experiments.

**Results summary:** This preprint proposes MAOA, a quantum optimization algorithm for restricted-depth, near-term settings. The core idea is to use binary marking and complete-graph mixing so that repeated applications of fixed parameters become equivalent to truncated Grover search, maximizing amplification of marked high-quality solutions rather than optimizing expected quality as in QAOA/QWOA. The paper provides theoretical derivations showing amplification of (2r + 1)^2 in the low-convergence regime and supports these with numerical simulations. On simulated vehicle routing, portfolio optimization, and synthetic normally distributed problem instances, MAOA consistently outperforms a restricted Grover adaptive search baseline and classical random sampling. However, all evidence is simulation- and theory-based, so any broader quantum advantage claim remains speculative for this preprint.

**Performance claims:**
- Single-iteration amplification reaches 9 for binary marking on a complete graph at gamma = pi and t = pi/N
- Low-convergence marked-state amplification scales as (2r + 1)^2
- Low-convergence approximation is stated to be accurate within 1% when amplified probability is less than 1/40
- In simulations on a complete graph with N = 10^8 and 10 marked solutions, binary partitioning outperformed 3-, 5-, and 10-part partitions across iterations up to r = 30
- For the 10-location CVRP instance, solution-space size was N = 58,941,091 and unrestricted Grover complete-convergence rotation count was rc = 6,029
- For the portfolio optimization instance with 20 assets and net position I = 7, solution-space size was N = 61,757,600 and unrestricted Grover complete-convergence rotation count was rc = 6,172
- Portfolio optimization simulations used restricted rotation counts r in {32, 64, 128, 256, 512}
- CVRP simulations used restricted rotation counts r in {8, 16, 32, 64, 128}
- For synthetic normally distributed problems at r = 64, the MAOA final marked-solution ratio was approximated as rho(r) = 1 / (40(2r + 1)^2) and reported numerically as about 1.5 x 10^-6
- The asymptotic speedup over classical random sampling is derived as 2r + 1 in the small-target-ratio limit
## Quantum advantage claim
**Classification:** speculative

The paper claims substantial speedup over classical random sampling and superiority to QAOA-like approaches, but evidence is based on theoretical derivations and numerical simulations only, with no real-hardware demonstration or peer-reviewed empirical validation.
## Limitations
- This is a preprint and has not undergone peer review.
- Results are based on numerical simulations rather than execution on real quantum hardware.
- The study does not account for hardware noise, decoherence, gate errors, or error-mitigation performance, despite motivating the work by near-term device limitations.
- Performance claims are made in a restricted-circuit-depth setting, but no end-to-end hardware implementation or resource estimate is provided for actual devices.
- The speedup analysis is benchmarked primarily against classical random sampling/exhaustive-search-style baselines rather than stronger state-of-the-art classical optimization heuristics.
- The authors explicitly note that the computational effort of the quantum walk/mixing process is not included in the speedup accounting; only objective-function calls are counted.
- The claimed speedup is therefore only partial, since full circuit synthesis and execution costs are omitted.
- The unrestricted Grover adaptive search is acknowledged by the authors as unlikely to be implementable on near-term devices because it requires large rotation counts of O(sqrt(N)).
- The MAOA speedup is characterized as maximal only within the class of amplitude-amplification algorithms, not necessarily among all quantum optimization approaches.
- The large-problem analysis assumes solution qualities are approximately normally distributed and, in the asymptotic analysis, approximately continuous.
- The analytical large-problem success expressions assume sampling with repeats and require the target ratio to satisfy mu >> 1/N.
- The threshold-finding procedure depends on being able to estimate and navigate threshold response curves; its robustness outside the studied distributions is not fully validated.
- For multidimensional portfolio optimization, the problem is simplified by fixing the risk threshold at the lowest 10% and then optimizing return, which restricts generality.
- The portfolio optimization experiments use one specific dataset of 20 ASX stocks over 2019-2020, limiting empirical breadth.
- The vehicle routing experiment uses one randomly generated 10-location instance, limiting evidence across instance classes and scales.
- The optimization and amplification studies rely on precomputed full quality distributions for the tested problems, which is not feasible for truly classically intractable instances.
- [inferred] No reproducible implementation details such as code, seeds, or full simulation artifacts are provided in the excerpt, limiting reproducibility.
- [inferred] No explicit qubit-count, ancilla, connectivity, or gate-depth resource estimates are given for implementing the marking oracle and complete-graph mixer on realistic hardware.
- [inferred] The assumption that complete-graph-based mixing is efficient may hide substantial compilation overhead on sparse-connectivity hardware.
- [inferred] The comparison excludes direct empirical benchmarking against QAOA/QWOA under matched implementation budgets, relying instead on theoretical/qualitative arguments.
- [inferred] The threshold navigation algorithm may itself incur nontrivial overhead and sensitivity to hyperparameters (e.g., sample size, step size, stopping rules), which is not systematically analyzed.
- [inferred] The method's practical advantage for finance may depend heavily on oracle construction for portfolio constraints and objective evaluation, which is not costed.
## Open questions
- How does MAOA perform on real noisy quantum hardware under realistic decoherence and gate-error conditions?
- What are the full resource requirements, including qubits, ancillas, oracle cost, and compiled circuit depth, for practical financial optimization instances?
- How does MAOA compare against strong classical baselines such as branch-and-bound, simulated annealing, tabu search, genetic algorithms, or modern portfolio optimizers?
- How robust is the threshold-finding procedure when the solution-quality distribution is highly irregular, multimodal, heavy-tailed, or poorly sampled?
- Can the method maintain its advantage when the cost of implementing the complete-graph mixer and binary marking oracle is fully included?
- How well does MAOA scale beyond the simulated problem sizes and beyond the assumption of approximately normal quality distributions?
- What is the impact of imperfect knowledge of the distribution tail on selecting thresholds in the low-convergence regime?
- Can MAOA be generalized effectively to genuinely multidimensional financial objectives without reducing them to staged one-dimensional thresholding?
- How sensitive is performance to the chosen fixed risk threshold in the portfolio optimization example?
- Under what conditions do alternative non-amplitude-amplification quantum methods outperform MAOA in restricted-depth settings?
- How does the algorithm behave when there are many near-optimal solutions versus a unique optimum?
- Can the threshold-response navigation be made provably efficient and robust across broad classes of combinatorial optimization problems?

**Future work:**
- Implement and test MAOA on real near-term quantum devices.
- Include the computational cost of the quantum walk/mixing process in full speedup analyses.
- Study larger and more realistic combinatorial optimization problems, especially those beyond classically enumerable solution spaces.
- Extend evaluation to broader classes of financial optimization problems beyond the specific portfolio setup used here.
- Investigate MAOA for multidimensional optimization using multi-stage thresholding strategies.
- Develop more rigorous analyses of threshold-finding and adaptive-search procedures.
- Benchmark MAOA against additional quantum approaches, including methods outside the amplitude-amplification framework such as filtering variational quantum algorithms.
- Explore whether circuit ansatz outside amplitude amplification can project into high-quality states with less depth and lower overhead.
- Analyze the practical implementation of complete-graph mixing and binary marking under realistic hardware connectivity constraints.
- Test robustness across different underlying quality distributions, especially cases that deviate from normality in the tails.
- [inferred] Provide open-source code, simulation details, and standardized benchmarks to improve reproducibility.
- [inferred] Derive explicit fault-tolerant and NISQ-era resource estimates for finance-relevant portfolio sizes.
- [inferred] Compare against state-of-the-art classical financial optimization pipelines on real market datasets.
- [inferred] Investigate noise-aware or error-mitigated variants of MAOA suitable for NISQ hardware.
## Key ideas
- #idea:quantum-advantage — MAOA claims linear-in-depth speedup over classical random sampling and stronger performance than restricted Grover adaptive search on simulated portfolio optimisation and other combinatorial tasks.
- #idea:near-term-feasibility — The method is explicitly designed for restricted-depth NISQ settings by avoiding variational parameter training and using fixed analytically derived parameters.
- #idea:hybrid-approach — Threshold selection and adaptive search are handled through a quantum-classical workflow combining analytical Grover-style amplification with classical threshold navigation and simulation-based tuning.
- #idea:quantum-advantage — For the portfolio case, the paper reframes optimisation as amplifying optimal or near-optimal feasible portfolios rather than maximizing expectation value as in QAOA/QWOA-style approaches.
- #idea:near-term-feasibility — The portfolio example uses staged optimisation by fixing a low-risk subset and then amplifying the highest-return portfolio within that subset.
## Contradictions
- The paper argues that expectation-value optimisation in QAOA/QWOA is less suitable than direct amplification of optimal states, which conflicts with prior portfolio-optimisation papers that report useful QAOA-style performance on finance instances.
- The paper presents near-term speedup claims, but its own limitations undermine scalability: results rely on classical simulation, omit oracle/mixer compilation costs, use precomputed full quality distributions, and provide no realistic hardware resource estimates for finance-scale deployment.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->

## Experiment details
### Input
CVRP: synthetic instance with l=10 locations, solution-space size N=58,941,091; package vector sampled from integers in [5,30], symmetric depot-to-location costs from [10,20], inter-location costs from [1,15], vehicle capacity 20; integer costs chosen to increase degeneracy. Portfolio optimization: 20 ASX.20 stocks (AMP, ANZ, AMC, BHP, BXB, CBA, CSL, IAG, MQG, GMG, NAB, RIO, SCG, S32, TLS, WES, BKL, CMW, HUB, ALU), daily adjusted close prices from 01/01/2019 to 31/12/2020; Markowitz-style expected returns and covariance matrix computed; ternary positions zi in {-1,0,1} with net position I=7, giving N=61,757,600 feasible portfolios. Large-problem simulation: standard normal distribution used directly as the quality distribution; marked-solution ratio rho(T) taken as the standard normal CDF at threshold T.

### Process
Method development proceeds in two stages: first, derive analytically that binary marking on a complete graph with repeated parameters gamma=pi and t=pi/N is equivalent to truncated Grover search and maximizes amplification in the low-convergence regime; second, numerically evaluate the resulting MAOA. For threshold selection, MAOA starts near the median quality, navigates threshold-response curves by doubling the Grover rotation count r, and moves from the high-convergence peak of one response curve to the next until the target restricted depth is reached; then a fixed-depth adaptive search refines the threshold into the low-convergence regime. The paper provides pseudocode for FinalThreshold, FindPeak, ThresholdForAS, and AdaptiveSearch. Benchmark simulations assume: (1) threshold T induces marked ratio rho(T), (2) marked measurement probability follows P(r,rho(T)) from Grover theory, (3) successful marked measurements are uniformly sampled from the marked set, and (4) each amplified-state preparation/measurement costs 2r+1 objective-function calls. For CVRP and portfolio tasks, success-probability-versus-effort curves are estimated from 10,000 simulations for MAOA, GAS, RGAS, and classical random sampling. CVRP uses MAOA/RGAS rotation counts r in {8,16,32,64,128}; unrestricted GAS uses r_max=6029. Portfolio optimization fixes the risk threshold at the lowest 10% of solutions and optimizes return within that subspace; MAOA/RGAS use r in {32,64,128,256,512}; unrestricted GAS uses r_max=6172. For the abstract large-problem study, MAOA and RGAS are simulated at fixed r=64 over target ratios mu in {1e-6,1e-7,1e-8,1e-9,1e-10}. Supporting numerical studies of graph/parameter behavior include: for 24-vertex circulant graphs, 48 random quality distributions, 10,000 random initial parameter sets, selecting the top 10 starts for Nelder-Mead optimization; for partitioned complete graphs with N=10^8 and 10 marked vertices, 10,000 random parameter sets per trial, top 3 passed to Nelder-Mead, repeated 24 times, with the best of 72 optimized results retained.

### Output
Primary outputs are success probability as a function of computational effort and probability amplification of optimal/marked solutions. Comparisons are made against classical random sampling, unrestricted Grover adaptive search (GAS), and restricted Grover adaptive search (RGAS). Additional outputs include threshold-response curves, amplification curves versus QWOA iteration count, optimization-landscape statistics (mean and standard deviation of amplified probabilities across local optima), and analytical speedup expressions. In the portfolio case, success is defined as finding the single highest-return portfolio among the lowest 10% risk portfolios; in the CVRP case, success is finding one of the 12 lowest-cost solutions.

### Parameters
- cvpr_problem_size: 58941091
- portfolio_problem_size: 61757600
- cvpr_rotation_counts_tested: [8, 16, 32, 64, 128]
- portfolio_rotation_counts_tested: [32, 64, 128, 256, 512]
- large_problem_rotation_count: 64
- gas_rmax_cvpr: 6029
- gas_rmax_portfolio: 6172
- simulations_per_setting: 10000
- maoa_fixed_parameters: {'gamma': 'pi', 't': 'pi/N'}
- peak_detection_success_streak: 20
- adaptive_search_stop_count: 40
- partitioned_complete_graph_N: 100000000
- partitioned_complete_graph_marked_vertices: 10
- random_initial_parameter_sets_partition_study: 10000
- nelder_mead_repetitions_partition_study: 24
- random_initial_parameter_sets_graph_study: 10000
- top_starts_graph_study: 10
- graph_study_vertices: 24
- portfolio_net_position_I: 7
- portfolio_low_risk_fraction_fixed: 0.1

### Hardware
{'type': 'classical numerical simulation', 'quantum_hardware': 'none', 'simulator': 'custom analytical/numerical simulation based on Grover/QWOA probability formulas', 'compute_resources': 'Pawsey Supercomputing Centre resources acknowledged'}

### Reproducibility
Preprint status. The paper provides substantial methodological detail, equations, assumptions, parameter values, and pseudocode for the MAOA threshold-finding routine, which supports partial replication. Financial data source and date range are specified, and synthetic CVRP generation rules are described. However, no public code repository is mentioned in the provided text, and some implementation details of the simulation environment are not fully specified, so reproducibility is moderate rather than complete.
