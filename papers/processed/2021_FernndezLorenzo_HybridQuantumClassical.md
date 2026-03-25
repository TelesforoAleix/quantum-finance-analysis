---
aliases:
- Hybrid quantum-classical optimization with cardinality constraints and applications
  to ﬁnance
- Hybrid quantum classical optimization
authors:
- Samuel Fernández-Lorenzo
- Diego Porras
- Juan José García-Ripoll
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
- QAOA
- VQE
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
step1_date: '2026-03-25T15:53:53.136039'
step1_model: gpt-5.1
step2_date: '2026-03-25T15:53:57.913437'
step2_model: gpt-5.1
step3_date: '2026-03-25T15:54:38.539741'
step3_model: gpt-5.4
step4_date: '2026-03-25T15:55:17.257614'
step4_model: gpt-5.4
step5_date: '2026-03-25T15:55:51.933258'
step5_model: gpt-5.4
step6_date: '2026-03-25T15:56:04.896541'
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
- method/VQE
- method/QUBO
- method/variational
- method/classical-simulation
- idea/quantum-advantage
- idea/near-term-feasibility
- idea/hybrid-approach
- contradiction/classical-vs-quantum
- contradiction/scalability
title: Hybrid quantum-classical optimization with cardinality constraints and applications
  to ﬁnance
topic_tags:
- portfolio-optimisation
year: 2021
zotero_key: ''
---

## Abstract summary
The paper proposes a hybrid quantum-classical framework for solving quadratic optimization problems with cardinality constraints, where only a limited number of variables can be nonzero. The authors introduce a k-step pruning algorithm that iteratively reduces the variable set via quantum (or quantum-inspired) combinatorial optimization combined with classical convex optimization, and they study both hard and soft constraint encodings (including a chemical-potential-like regularization) for controlling sparsity. Using an index tracking problem based on the PHLX Oil Service Sector (OSX) index as a benchmark, they compare several variational quantum ansätze and classical optimizers, and analyze their performance and resource requirements on NISQ-relevant problem sizes.
## Methodology
This preprint presents an empirical/numerical study of a hybrid quantum-classical method for continuous optimization problems with cardinality constraints, using financial index tracking as the benchmark application. The core methodological contribution is a heuristic k-step pruning algorithm (k-PA) that alternates between (1) classical convex optimization to estimate continuous asset weights and (2) binary combinatorial optimization to select which assets remain active, progressively reducing the universe size until the target portfolio cardinality is reached. The paper studies both a one-step pruning variant and a multi-step pruning schedule, and compares hard-constraint QUBO formulations against a soft-constraint formulation using a Lagrange-multiplier/"chemical potential" term to control sparsity. For the combinatorial subproblem, the authors evaluate several variational quantum optimization approaches—VQE with an Ry hardware-efficient ansatz, QAOA, and a SWAP-based number-conserving ansatz—combined with classical optimizers such as COBYLA and SciPy dual annealing; they also compare against classical simulated annealing via dimod. The benchmark task is index tracking on real intraday financial data from the PHLX Oil Service Sector (OSX) index with 15 assets, where the objective is to minimize tracking error under nonnegativity, budget, and cardinality constraints. Performance is assessed numerically by comparing heuristic and variational solutions to exact brute-force optima using relative error, probability of recovering the optimum, number of function evaluations, runtime, and statistical significance tests (Wilcoxon rank-sum). The paper is explicitly a preprint.

**Algorithms used:** QAOA, VQE, SWAP ansatz, COBYLA, dual annealing, simulated annealing, heuristic k-step pruning (k-PA), 1-SA, 1-PA
**Frameworks:** SciPy, dimod, IBM-Q

**Experimental setup:** Numerical simulations were performed on a small benchmark instance of the index tracking problem with N = 15 assets from the PHLX Oil Service Sector (OSX) index. The quantum part was simulated rather than executed on hardware in the reported experiments, although the paper states the method could be executed on NISQ devices such as IBM-Q. Variational wavefunctions were sampled with Nmeas = 100 measurements in all numerical experiments. The combinatorial optimization stage was encoded as a QUBO/Ising problem and solved using VQE, QAOA, or a SWAP-based ansatz, with classical optimization by COBYLA or SciPy dual annealing. Classical simulated annealing using dimod was used as a baseline. Exact brute-force search/diagonalization was used to compute optimal reference solutions for the small 15-asset benchmark.

**Dataset:** Real intraday price data for the PHLX Oil Service Sector (OSX) index, consisting of 15 oil-services-sector companies. Prices were sampled every 20 minutes over several days; look-back windows corresponded to a single day, and results were averaged over multiple days/random dates.
## Experiment details
### Input
Financial input consists of intraday prices P_j(t) for 15 assets in the PHLX Oil Service Sector (OSX) index and benchmark index returns over single-day look-back windows. Sampling interval was 20 minutes. From these prices, asset returns r_j(t_n) and benchmark returns r_I(t_n) were computed, then used to build the quadratic matrix Sigma_ij = sum_n r_i(t_n) r_j(t_n), linear term g_j = sum_n r_j(t_n) r_I(t_n), and offset epsilon_0 = sum_n r_I(t_n)^2. The optimization imposed nonnegative portfolio weights, an L1 budget constraint ||w||_1 = 1, and target cardinality d, with experiments mainly exploring d in [5,10] and final target d = 5 in some pruning tests. No extensive preprocessing beyond return construction and formation of Sigma/g is described.

### Process
The experimental pipeline is: (1) formulate index tracking as minimization of mean squared tracking error under budget, nonnegativity, and cardinality constraints; (2) solve a full classical convex optimization to obtain provisional continuous weights w_opt; (3) build a binary selection problem using these weights, either with hard cardinality penalties in a QUBO or with a soft regularization/chemical-potential term lambda; (4) map the QUBO to an Ising Hamiltonian and optimize it with a variational quantum algorithm (VQE, QAOA, or SWAP ansatz) or classical simulated annealing; (5) for variational methods, initialize parameters randomly, optimize circuit parameters with COBYLA or dual annealing, then sample the final variational state 100 times and keep the lowest-energy bitstring satisfying the cardinality constraint when applicable; (6) solve the reduced classical convex optimization on the selected subset to update weights; (7) for k-step pruning, repeat the prune-and-reoptimize cycle with decreasing universe size according to a step size s and repetition schedule r <- r0 + alpha*r until the target portfolio size is reached. For hard-constraint experiments, the authors compared VQE(COBYLA), QAOA(COBYLA), SWAP(COBYLA), and QAOA(dual annealing), plus dimod simulated annealing with 100 reads. For soft-constraint experiments, lambda was tuned empirically to produce an average portfolio size close to the target d, and performance was analyzed as a function of deviation |<d> - d|. QAOA used 1-3 layers in some tests; VQE and SWAP layer counts were also varied. COBYLA used tol = 0.01 and a maximum of 2000 iterations; dual annealing used bounded parameter domains gamma in [0, 2pi], beta in [0, pi], and maxiter = 10 based on observed plateau behavior.

### Output
Outputs are reported as tracking-error or QUBO-energy quality relative to exact optima, primarily using relative error Delta = (T_err - T_err^opt)/T_err^opt or Delta = (P_err - P_err^opt)/P_err^opt. Additional outputs include Pearson correlation between heuristic and exact solutions, probability of achieving error below thresholds, probability of sampling the global optimum, average portfolio size under soft constraints, number of function evaluations, and runtime/time consumed. Baselines/comparators include exact brute-force optimization/diagonalization, classical simulated annealing via dimod, and comparisons across ansatz/optimizer combinations (VQE, QAOA, SWAP; COBYLA vs dual annealing). Statistical comparisons were performed using the Wilcoxon rank-sum test with reported p-values.

### Parameters
- assets: 15
- sampling_interval_minutes: 20
- measurements_per_variational_state: 100
- portfolio_size_range_tested: [5, 10]
- example_target_portfolio_size: 5
- vqe_ansatz: Ry hardware-efficient ansatz with local rotations and nearest-neighbor CZ entanglers
- qaoa_ansatz: Standard QAOA with p layers, cost Hamiltonian and global X-mixer
- swap_ansatz: Number-conserving ansatz with Z rotations and sqrt(SWAP) gates
- qaoa_layers_tested: [1, 2, 3]
- optimizer_cobyla_tol: 0.01
- optimizer_cobyla_maxiter: 2000
- dual_annealing_maxiter: 10
- qaoa_gamma_bounds: [0, 6.283185307179586]
- qaoa_beta_bounds: [0, 3.141592653589793]
- simulated_annealing_reads: 100
- pruning_comparison_total_repetitions: 120
- pruning_schedules: {'1-PA': {'r0': 120, 'alpha': 0}, '2-PA': {'r0': 120, 'alpha': 4}, '3-PA': {'r0': 20, 'alpha': 1}}

### Hardware
{'execution_mode': 'Classical simulation of variational quantum circuits for reported experiments', 'quantum_hardware_mentioned': ['IBM-Q'], 'simulator_details': 'Specific simulator backend not named; experiments described as classically simulating small quantum variational circuits', 'other_platforms_mentioned': ['D-Wave quantum annealers']}

### Reproducibility
Moderate reproducibility. The paper provides mathematical formulations, algorithm pseudocode, dataset identity, key hyperparameters, ansatz definitions, optimizer settings, and evaluation metrics. It also names the dimod and SciPy tools used. However, no code repository is provided in the text, the exact data source/access procedure for the intraday OSX data is not fully specified, and some implementation details (e.g., exact simulator/backend, all random seeds, full pruning schedules/step sizes in every experiment) are incomplete. Replication appears feasible in principle but not turnkey.
## Findings
- [supported] The paper proposes a hybrid quantum-classical heuristic k-step pruning algorithm (k-PA) for quadratic optimization with cardinality constraints, separating continuous weight optimization (classical convex optimization) from binary variable selection (QUBO-style combinatorial optimization).
- [supported] On the 15-asset PHLX Oil Service Sector (OSX) index-tracking benchmark, the single-step pruning algorithm (1-PA) outperformed the single-step selection algorithm (1-SA), with Pearson correlation to the exact optimum of 0.92 versus 0.68.
- [supported] On the same benchmark, 1-PA achieved relative error Δ ≤ 20% in 62.5% of runs, compared with 17.7% for 1-SA.
- [supported] In simulated-annealing-based experiments, increasing the number of pruning steps in k-PA reduced median relative error and also reduced runtime, indicating that multi-step pruning improved both accuracy and speed on the tested small instances.
- [supported] An example 3-step pruning run reduced the universe from 15 to 5 assets and achieved final relative error Δ = 1.3% relative to the exact optimum.
- [supported] Under hard-constraint QUBO encoding, the SWAP ansatz achieved the lowest average relative error among tested variational methods, with average relative error about 4%, followed by QAOA with dual annealing at about 6%, QAOA with COBYLA at about 16%, and VQE at about 31%.
- [supported] For hard constraints, SWAP outperformed QAOA with dual annealing in average error at statistical significance according to a Wilcoxon rank-sum test (p = 0.0072, α = 0.05).
- [supported] QAOA with dual annealing required fewer function evaluations than SWAP while maintaining reasonably low error, suggesting a speed-accuracy tradeoff favorable to QAOA in some settings.
- [supported] For the hardest tested hard-constraint case (portfolio size d = 5 out of N = 15), SWAP and QAOA had a higher probability of finding the global optimum than classical simulated annealing, with Wilcoxon p-values 8.3×10^-5 and 2.7×10^-3 respectively; for d > 7, no statistical difference was found.
- [supported] The authors found that hard-constraint penalty formulations create rougher optimization landscapes that hinder local optimizers such as COBYLA, especially for low-depth QAOA.
- [supported] Under soft-constraint encoding using a regularization parameter λ ('chemical potential'), the average selected portfolio size showed a monotonic relationship with λ and remained fairly stable across dates and random initializations on the tested dataset.
- [supported] Soft-constraint encoding substantially improved optimization behavior relative to hard constraints on the benchmark, according to the authors' comparisons of relative error, sampling success, and optimizer behavior.
- [supported] With soft constraints, QAOA became more robust to deviations from the tuned λ* than VQE, while VQE had a higher probability of sampling the global optimum when λ was tuned close to λ*.
- [supported] For soft constraints, adding QAOA layers slightly improved results; the paper reports Wilcoxon p-values of 1.5×10^-4 between first and second layer distributions and 0.024 between second and third layer distributions.
- [supported] Under soft constraints, VQE required about 8 times more function evaluations than QAOA while achieving a higher probability of sampling the global optimum near the optimal λ*.
- [speculative] The authors argue that the pruning framework is well suited to NISQ devices because it concentrates the hard combinatorial part into a binary optimization stage and may require fewer qubits than direct discretization of continuous weights.
- [speculative] The paper suggests that for applications with hundreds or thousands of variables, quantum computers may offer an advantage over classical QUBO solvers in the variable-selection stage.
- [speculative] The authors claim their approach could extend beyond gate-based NISQ devices to quantum annealers and quantum-inspired optimizers.
- [speculative] The paper suggests the method could be useful in broader applications such as portfolio selection, regression subset selection, sparse PCA, QBoost-style model selection, compressed sensing, and facility location.

**Results summary:** This preprint introduces a hybrid quantum-classical pruning framework for continuous optimization problems with cardinality constraints and evaluates it on a small real-data index-tracking benchmark using 15 assets from the PHLX Oil Service Sector index. The main empirical result is that the proposed pruning formulation (1-PA) is substantially better than a simpler selection heuristic (1-SA), and that multi-step pruning improves both solution quality and runtime when paired with simulated annealing. For the combinatorial subproblem, the authors compare VQE, QAOA, and a SWAP-based cardinality-preserving ansatz under both hard-constraint and soft-constraint QUBO encodings. On these small simulated experiments, SWAP gives the lowest average error under hard constraints, while QAOA with dual annealing uses fewer function evaluations and performs competitively. Soft constraints improve the optimization landscape relative to hard penalties: QAOA is more robust to imperfect tuning of the regularization parameter, whereas VQE can sample the global optimum more often when the parameter is well tuned but at much higher evaluation cost. All results are based on classical simulation and small benchmark instances rather than demonstrated quantum hardware advantage.

**Performance claims:**
- 1-PA Pearson correlation with exact optimum: 0.92
- 1-SA Pearson correlation with exact optimum: 0.68
- Probability of achieving relative error Δ ≤ 20%: 62.5% for 1-PA vs 17.7% for 1-SA
- Example 3-step pruning final relative error: Δ = 1.3%
- Hard-constraint average relative error: SWAP ≈ 4%
- Hard-constraint average relative error: QAOA with dual annealing ≈ 6%
- Hard-constraint average relative error: QAOA with COBYLA ≈ 16%
- Hard-constraint average relative error: VQE ≈ 31%
- Wilcoxon rank-sum p-value comparing SWAP vs QAOA with dual annealing: p = 0.0072
- For hardest hard-constraint case d = 5, SWAP vs simulated annealing p = 8.3×10^-5
- For hardest hard-constraint case d = 5, QAOA vs simulated annealing p = 2.7×10^-3
- QAOA dual annealing plateau observed around maxiter = 10 for one-layer QAOA with d = 5
- Soft-constraint QAOA layer comparison p-values: 1.5×10^-4 (1 vs 2 layers), 0.024 (2 vs 3 layers)
- Soft-constraint VQE required about 8× more function evaluations than QAOA
- Variational wavefunctions were sampled with Nmeas = 100 measurements
## Quantum advantage claim
**Classification:** speculative

The paper argues that the hybrid pruning approach may enable useful NISQ applications and that quantum methods may help on larger combinatorial finance problems, but the evidence is limited to small N=15 benchmark instances, largely classically simulated variational experiments, and comparisons that do not demonstrate a clear practical quantum advantage over best classical methods at scale.
## Limitations
- The study is conducted on a very small index-tracking instance with only N = 15 assets, which the authors explicitly note can be solved efficiently by brute force and is used only as a workbench.
- Numerical validation is limited to a single dataset based on the PHLX Oil Service Sector (OSX) index, reducing evidence of generality across asset classes, market regimes, and larger financial universes.
- The experiments use short look-back windows corresponding to a single day of intraday data and average over several days, which may not capture longer-horizon portfolio behavior.
- The index-tracking formulation is simplified and omits realistic constraints such as capital concentration/diversification constraints, even though the authors acknowledge these may matter in practice.
- The formulation assumes continuous portfolio weights, whereas real trading often requires discrete lot sizes; the authors note this is only an approximation.
- The soft-constraint approach cannot predict a priori the selected portfolio size d(λ), requiring empirical tuning of the regularization parameter λ.
- The pruning algorithm depends on hyperparameters such as step size s, repetition schedule, and pruning schedule, and the authors state that the optimal value of s must be determined for each problem empirically.
- The hard-constraint QUBO formulation creates rough energy landscapes in which local optimizers such as COBYLA can get trapped in local minima.
- The reported quantum results are based on numerical simulations of variational circuits with Nmeas = 100 rather than large-scale demonstrations on real noisy hardware.
- Although the paper states the pruning method can be executed on NISQ devices such as IBM-Q, the presented benchmarks do not provide extensive real-hardware performance evidence under noise, decoherence, and calibration drift.
- The study compares against limited classical baselines, mainly simulated annealing and brute force on small instances, rather than a broad set of state-of-the-art classical mixed-integer, convex-relaxation, or specialized index-tracking solvers.
- [inferred] No end-to-end demonstration is provided on realistic production-scale instances with hundreds or thousands of securities, despite the paper motivating that regime as the target use case.
- [inferred] No evidence of quantum advantage is established; the work demonstrates heuristic promise on toy-scale problems rather than superiority over best classical methods.
- [inferred] Reproducibility may be limited because the paper does not provide full implementation details, code, random seeds, or exhaustive hyperparameter-search protocols.
- [inferred] The use of a single sector-specific index with highly correlated assets may bias results toward problem structures favorable to the proposed heuristics.
- [inferred] Transaction costs, turnover, rebalancing frequency, and out-of-sample tracking performance are not empirically evaluated, limiting practical financial relevance.
- [inferred] The claim that the method extends to quantum annealers or quantum-inspired optimizers is not directly validated in the experiments.
- [inferred] As a preprint, the work has not undergone peer review, so methodological choices and conclusions should be treated as provisional.
## Open questions
- How well does the heuristic k-step pruning algorithm scale to realistic financial universes with hundreds or thousands of assets?
- What is the best pruning schedule, including the step size s and repetition schedule, for different classes of cardinality-constrained optimization problems?
- How robust is the method on real NISQ hardware when noise, finite sampling, decoherence, and gate errors are included?
- Under what conditions does soft-constraint tuning produce a stable monotonic relationship between λ and the average selected portfolio size?
- Can the regularization parameter λ be predicted automatically from problem structure rather than tuned empirically?
- How do different ansatz choices behave as problem size grows beyond the small simulated instances studied here?
- Will the observed relative advantages of SWAP, QAOA, and VQE persist on larger and more realistic financial datasets?
- How does the method perform when realistic portfolio constraints such as concentration limits, sector caps, turnover constraints, or transaction costs are added?
- What is the out-of-sample tracking performance of portfolios selected by the proposed method, rather than only in-sample optimization error?
- How sensitive are the results to the choice of benchmark index, market regime, and asset-correlation structure?
- Can the pruning framework be combined effectively with stronger classical optimizers or exact methods in a way that changes the quantum-classical tradeoff?
- Does the method offer any practical advantage over state-of-the-art classical solvers on industrially relevant instances?

**Future work:**
- Test the proposed pruning framework on larger, realistic index-tracking problems involving hundreds or thousands of securities.
- Include additional realistic linear constraints such as capital concentration or diversification constraints within the heuristic pruning framework.
- Extend the formulation to fully combinatorial portfolio construction with discretized weights or lot sizes.
- Integrate the soft-constraint formulation into the multi-step pruning algorithm using a schedule of regularization parameters λ0 ≥ λ1 ≥ ... ≥ λk.
- Use different ansatz families and constraint formulations at different pruning stages, such as soft-constraint VQE in intermediate steps and hard-constraint low-depth QAOA at the end.
- Develop dynamic search strategies that adjust the regularization parameter λ during optimization.
- Potentially train a supervised machine learning model to predict a suitable λ from the QUBO matrix or problem instance.
- Benchmark the approach on other application domains mentioned by the authors, including subset selection in regression, sparse PCA, QBoost, compressed sensing, and facility location.
- Evaluate implementations on actual near-term quantum devices and possibly on quantum annealers or quantum-inspired optimizers.
- [inferred] Compare against stronger classical baselines, including specialized index-tracking heuristics, mixed-integer optimization solvers, and convex-relaxation methods.
- [inferred] Study out-of-sample financial performance, turnover, and transaction-cost-aware rebalancing to assess practical deployability.
- [inferred] Provide open-source code and standardized benchmarks to improve reproducibility and enable fair comparison.
## Key ideas
- #idea:hybrid-approach — Proposes a k-step pruning framework that alternates classical convex weight optimisation with quantum-amenable binary asset-selection subproblems.
- #idea:hybrid-approach — Multi-step pruning improves both solution quality and runtime versus simpler single-step heuristics on the small index-tracking benchmark.
- #idea:near-term-feasibility — The approach is framed as NISQ-friendly because only the combinatorial selection stage is mapped to a QUBO/Ising problem, reducing qubit needs relative to full discretised portfolio formulations.
- #idea:near-term-feasibility — Soft cardinality constraints using a chemical-potential-like regularisation produce smoother optimisation landscapes and better variational behaviour than hard-penalty QUBOs.
- #idea:quantum-advantage — On the hardest tested toy instance, simulated SWAP and QAOA variants outperform classical simulated annealing on some success-probability and error metrics.
- #idea:quantum-advantage — The paper speculates that larger cardinality-constrained finance problems may eventually benefit from quantum variable-selection methods, though this is not empirically established.
## Contradictions
- The paper suggests possible quantum advantage, but its evidence comes entirely from classical simulation on a 15-asset problem and limited comparison against simulated annealing rather than strong state-of-the-art classical solvers, undermining any practical superiority claim.
- The paper argues the pruning framework may scale to realistic portfolios with hundreds or thousands of assets, yet all reported experiments are toy-sized, brute-force-verifiable instances with no convincing scaling or resource study.
- The work promotes NISQ applicability, but no real-hardware validation is provided, so claims about robustness under noise and deployability on IBM-Q-like devices remain untested.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
