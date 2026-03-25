---
aliases:
- Warm-starting quantum optimization
- Warm starting quantum optimization
authors:
- Daniel J. Egger
- Jakub Mareček
- Stefan Woerner
auto_detected: true
classification: ''
contradiction_flags:
- contradiction:classical-vs-quantum
- contradiction:scalability
doi: 10.22331/q-2021-07-01-479
evidence_type: ''
idea_tags:
- idea:quantum-advantage
- idea:near-term-feasibility
- idea:hybrid-approach
journal_or_venue: Quantum
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
source_type: peer-reviewed-empirical
source_type_confidence: high
step1_date: '2026-03-25T15:53:45.384298'
step1_model: gpt-5.1
step2_date: '2026-03-25T15:53:50.076229'
step2_model: gpt-5.1
step3_date: '2026-03-25T15:54:24.494326'
step3_model: gpt-5.4
step4_date: '2026-03-25T15:54:59.204766'
step4_model: gpt-5.4
step5_date: '2026-03-25T15:55:31.189712'
step5_model: gpt-5.4
step6_date: '2026-03-25T15:55:50.448954'
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
- method/variational
- method/classical-simulation
- idea/quantum-advantage
- idea/near-term-feasibility
- idea/hybrid-approach
- contradiction/classical-vs-quantum
- contradiction/scalability
title: Warm-starting quantum optimization
topic_tags:
- portfolio-optimisation
year: 2021
zotero_key: ''
---

## Abstract summary
The paper proposes and analyzes "warm-start" variants of QAOA and recursive QAOA that initialize the quantum algorithm from solutions of classical continuous relaxations, such as quadratic and semidefinite programs, or from randomized-rounding schemes like Goemans–Williamson. The authors show how to construct corresponding initial states and mixer Hamiltonians so that the quantum algorithms can inherit classical approximation guarantees, and they study these methods numerically on portfolio optimization and MAXCUT instances. Their simulations indicate that warm-starting is particularly beneficial at low circuit depth and on noisy hardware, often outperforming standard QAOA and, in some regimes, matching or improving on Goemans–Williamson-based approaches.
## Methodology
The paper proposes and empirically evaluates warm-started quantum optimization, primarily warm-start QAOA (WS-QAOA) and warm-start recursive QAOA (WS-RQAOA), by initializing the quantum state from solutions of classical relaxations of combinatorial optimization problems. For continuous warm-starting, the authors solve a convex quadratic relaxation of QUBO portfolio optimization instances, map the relaxed solution c* into qubit rotation angles for the initial state, and replace the standard X-mixer with a custom mixer whose ground state matches the warm-start state; they also introduce a regularization parameter epsilon to avoid reachability issues and interpolate between WS-QAOA and standard QAOA. For rounded warm-starting, they use Goemans-Williamson (GW) semidefinite-program rounding to generate MAXCUT warm starts and adapt the mixer so the variational circuit can recover the GW solution while exploring nearby states. Empirical studies compare warm-started versus standard QAOA on portfolio optimization and MAXCUT, including recursive elimination in RQAOA. Experiments are simulation-based, using exact statevector simulation for portfolio optimization and efficient classical simulation of depth-1 RQAOA/WS-RQAOA for MAXCUT. Performance is assessed via optimized energy relative to exact optimum, probability of sampling the optimal solution, and cut quality relative to the maximum cut, with comparisons against standard QAOA/RQAOA, GW cuts, and a recursive classical GW-based heuristic.

**Algorithms used:** QAOA, WS-QAOA, RQAOA, WS-RQAOA, Goemans-Williamson randomized rounding, COBYLA
**Frameworks:** Qiskit, IBM ILOG CPLEX

**Experimental setup:** All reported empirical results are simulation-based rather than run on real quantum hardware. Portfolio optimization experiments use the Qiskit statevector simulator, so there is no sampling noise; randomness comes only from random initial parameter guesses for the classical optimizer. Continuous relaxations are solved classically with IBM ILOG CPLEX 12.10.0. MAXCUT warm-start experiments use classical simulation of depth-1 WS-QAOA/WS-RQAOA, including an efficient correlator-based simulation for depth-1 recursive QAOA. Additional annealing-style simulations are performed by Trotterizing the time evolution under the mixer and cost Hamiltonians. No real QPU is used.

**Dataset:** Synthetic financial portfolio data and synthetic graph instances. For portfolio optimization, the authors generate random 6-asset instances by simulating asset price time series via geometric Brownian motion, then compute expected returns and covariance matrices. For MAXCUT, they generate random weighted graphs: fully connected graphs with random integer weights in {-10,...,10}, and Erdos-Renyi-like graphs with edge probability 1/2 and edge weights in {-1,1}; graph sizes include 6, 20, and 30 nodes depending on the experiment.
## Experiment details
### Input
Portfolio optimization: synthetic daily price series for n=6 assets over N=250 days generated from geometric Brownian motion with initial price Si,0=1, asset drifts mu_i sampled uniformly from [-5%, 5%], volatilities sigma_i sampled uniformly from [-20%, 20%], returns computed as ri,k = Si,k/Si,k-1 - 1, covariance matrix and mean returns estimated from the simulated series. Optimization problem uses risk-return parameter q=2, budget B=3, and quadratic penalty lambda=3 to enforce the budget constraint. MAXCUT: random graphs including (i) 10 fully connected 30-node graphs with edge weights uniformly sampled from {-10,-9,...,10} for epsilon sweeps; (ii) 100 graphs each for n=20 and n=30 with edge probability pE=1/2 and weights in {-1,1}; (iii) 100 fully connected graphs each for n=20 and n=30 with weights uniformly sampled from {-10,...,10}; and (iv) one fully connected 6-node graph with weights in {-10,...,10} for p>1 landscape analysis. Exact optima are obtained by diagonalization or CPLEX depending on the experiment.

### Process
Continuous warm-start portfolio experiments: (1) formulate portfolio selection with budget constraint as QUBO/Ising Hamiltonian; (2) solve the continuous quadratic relaxation with CPLEX to obtain c*; (3) encode c* into initial qubit Y-rotation angles theta_i and construct a warm-start mixer matched to c*; (4) run QAOA/WS-QAOA at depths p=1 to 5; (5) optimize variational parameters beta and gamma using COBYLA, initialized from random guesses drawn uniformly from ±2pi; (6) evaluate optimized state energy and probability of sampling the optimal bitstring; (7) compare against standard QAOA and a hybrid variant using warm-start initial state with standard mixer; (8) repeat over 250 random instances for depth-1 benchmarking. Annealing study: simulate Trotterized annealing with schedules beta_k = 2 dt (1 - i/N) and gamma_k = 2 i dt / N, where dt = T/N, varying total anneal time T and number of steps N, and compare warm-start versus equal-superposition mixers. Rounded warm-start MAXCUT experiments: (1) solve SDP-based GW relaxation and generate multiple GW cuts; (2) use the best unique cuts to initialize WS-QAOA with regularization epsilon; (3) for depth-1 WS-QAOA, perform a grid search over 25 equally spaced gamma_1 values in [-2pi, 2pi], evaluate energies at beta_1 in {3pi/4, 3pi/8}, fit a sin(2 beta_1)+b sin(4 beta_1) surrogate, and pass the best (beta_1, gamma_1) to COBYLA; (4) sweep epsilon to study cut quality; (5) for WS-RQAOA, at each recursion generate N=10 GW cuts, retain the best M=5 unique cuts, run M depth-1 WS-QAOA solvers with epsilon=0.25, aggregate bitstring probabilities/correlations, eliminate one variable using the largest correlation, and recurse until n_stop = n/2, then solve the reduced problem exactly; (6) compare against standard RQAOA and a recursive classical GW-based elimination heuristic. For p>1, run 30 WS-QAOA optimizations per depth p=1,...,6 on a 6-node graph with random initial beta in [0,2pi] and gamma in ±2pi, then record energy and probability of sampling the maximum cut.

### Output
Reported outputs include: optimized expectation value of the cost Hamiltonian, normalized by the exact minimum energy E0 for portfolio optimization; probability of sampling the optimal portfolio bitstring; histograms of normalized energies over 250 random portfolio instances; normalized energy gap ratio Delta_warm/Delta_cold as a function of overlap between continuous and discrete optima; annealing energy trajectories and final normalized energies as functions of total anneal time and Trotter steps; for MAXCUT, cut energy/cut size normalized by the exact maximum cut, median and interquartile ranges across graphs and warm starts, histograms of cut-size percentages, and counts of exact maximum cuts found. Baselines include standard QAOA, standard RQAOA, best GW cut out of 10, GW itself at epsilon=0, a recursive classical GW heuristic, and a warm-start initial state combined with the standard mixer.

### Parameters
- portfolio_optimization: {'assets': 6, 'time_steps_days': 250, 'risk_return_parameter_q': 2, 'budget_B': 3, 'budget_penalty_lambda': 3, 'qaoa_depths': [1, 2, 3, 4, 5], 'optimizer': 'COBYLA', 'initial_parameter_range': 'beta, gamma initialized uniformly from ±2pi', 'num_random_instances_depth1': 250}
- annealing_simulation: {'schedule': 'beta_k = 2 dt (1 - i/N), gamma_k = 2 i dt / N', 'dt': 'T/N', 'varied_parameters': ['total anneal time T', 'number of Trotter steps N']}
- maxcut_epsilon_sweep: {'graph_count': 10, 'nodes': 30, 'graph_type': 'fully connected', 'edge_weights': '{-10,...,10}', 'gw_cuts_per_graph': 10, 'best_unique_cuts_used': 5, 'qaoa_depth': 1, 'gamma_grid_points': 25, 'gamma_range': '[-2pi, 2pi]', 'beta_candidates_for_fit': ['3pi/4', '3pi/8']}
- ws_rqaoa: {'graph_counts_per_setting': 100, 'node_sizes': [20, 30], 'graph_types': ['edge probability 1/2 with weights in {-1,1}', 'fully connected with weights in {-10,...,10}'], 'gw_cuts_N': 10, 'best_unique_cuts_M': 5, 'qaoa_depth': 1, 'epsilon': 0.25, 'stopping_size_nstop': 'n/2', 'optimizer': 'COBYLA'}
- p_greater_than_1_maxcut: {'nodes': 6, 'graph_type': 'fully connected', 'edge_weights': '{-10,...,10}', 'depths_tested': [1, 2, 3, 4, 5, 6], 'runs_per_depth': 30, 'beta_init_range': '[0, 2pi]', 'gamma_init_range': '±2pi', 'epsilon': 0.25}

### Hardware
{'quantum_hardware': 'No real quantum hardware used', 'simulator': 'Qiskit statevector simulator for portfolio experiments; classical efficient simulation for depth-1 RQAOA/WS-RQAOA correlators', 'classical_solvers': ['IBM ILOG CPLEX 12.10.0', 'COBYLA'], 'noise_model': 'None reported'}

### Reproducibility
Reproducibility is moderate to good. The paper provides substantial methodological detail, including problem formulations, warm-start state preparation, mixer definitions, parameter ranges, graph/data generation procedures, and optimization routines. It explicitly states that an implementation of WS-QAOA is available in Qiskit/qiskit-optimization, which supports partial reproducibility. Data are synthetic and can be regenerated from the described procedures. However, full replication may still require implementation details for all experiment scripts, exact random seeds, and some omitted appendix-level coding specifics.
## Findings
- [supported] In simulation on 6-asset portfolio optimization instances, warm-start QAOA (WS-QAOA) produced a probability of sampling the optimal binary solution that was more than 5x higher than standard QAOA for depths p = 1 to 5.
- [supported] In the same 6-asset portfolio example, WS-QAOA achieved lower optimized energy than standard QAOA across tested depths, indicating better solution quality relative to the exact ground-state energy.
- [supported] Using the warm-start initial state without the modified warm-start mixer degraded performance: energies did not converge to the minimum energy, and optimal-solution sampling probability was between warm-start and standard QAOA with high sensitivity to optimizer initialization.
- [supported] Across 250 random portfolio optimization instances at depth p = 1, WS-QAOA produced optimized states much closer to the minimum energy than standard QAOA, whose solutions poorly approximated the ground state.
- [supported] For the 250 portfolio instances, WS-QAOA tended to improve more when the overlap between the optimal discrete solution and the continuous relaxation solution was closer to 1.
- [supported] In Trotterized annealing simulations for the portfolio problem, the warm-start mixer required less total annealing time T and fewer Trotter steps N than the equal-superposition mixer to minimize energy, indicating faster convergence in simulation.
- [supported] For MAXCUT on 10 fully connected 30-node random-weight graphs, depth-1 WS-QAOA initialized from Goemans-Williamson (GW) cuts had median normalized energy 0.907 at ε = 0, matching the GW warm start, and this worsened to 0.929 at ε = 0.25 after first improving at intermediate ε values.
- [supported] The non-monotonic dependence on regularization ε for MAXCUT suggests an empirically favorable regime around ε ≈ 0.15 for depth-1 WS-QAOA on the tested graphs.
- [supported] In recursive MAXCUT experiments on 100 graphs per setting, WS-RQAOA systematically outperformed standard RQAOA across graph sizes and graph types tested, including 20- and 30-node sparse random graphs and fully connected random-weight graphs.
- [supported] In the same recursive MAXCUT experiments, a recursive classical baseline based on averaging correlations from the five best GW cuts outperformed standard RQAOA but was slightly worse than WS-RQAOA.
- [supported] For a 6-node fully connected MAXCUT instance, increasing WS-QAOA depth from p = 1 to 6 increased the probability of sampling the maximum cut and decreased the optimized energy.
- [speculative] The authors argue that warm-starting allows quantum optimization algorithms to inherit classical approximation guarantees from the underlying relaxation and rounding scheme.
- [speculative] The paper claims that for MAXCUT a warm start can preserve the Goemans-Williamson approximation ratio at any depth p, but this is presented as an analytical argument rather than an empirical demonstration in the reported experiments.
- [speculative] The authors suggest warm-started quantum optimization may outperform GW randomized rounding in some settings, based on observed ε-dependent behavior in simulation rather than a formal demonstrated advantage.
- [speculative] The paper argues that warm-starting is particularly beneficial at low circuit depth and may be broadly applicable to other combinatorial optimization and integer programming problems.

**Results summary:** This peer-reviewed empirical paper studies warm-starting QAOA and recursive QAOA using solutions from classical relaxations, with all reported experiments performed in simulation rather than on real quantum hardware. For a 6-asset portfolio optimization problem, WS-QAOA outperformed standard QAOA across depths 1 to 5, yielding more than a 5x higher probability of sampling the optimal solution and lower optimized energies; on 250 random portfolio instances at depth 1, WS-QAOA consistently produced energies closer to the exact optimum. Trotterized annealing simulations also showed that the warm-start mixer reached low energies with less annealing time and fewer steps than the standard mixer. For MAXCUT, depth-1 WS-QAOA warm-started from Goemans-Williamson cuts on 30-node fully connected random-weight graphs showed best performance at intermediate regularization, with median normalized energy 0.907 at ε = 0 and 0.929 at ε = 0.25. In recursive experiments on 100 graphs per setting, WS-RQAOA outperformed standard RQAOA and slightly exceeded a recursive classical GW-based baseline. On a 6-node MAXCUT instance, increasing depth improved both energy and probability of sampling the maximum cut. The paper makes theoretical claims that warm-starting can preserve classical approximation guarantees, but no quantum advantage over classical methods is empirically demonstrated.

**Performance claims:**
- More than 5x higher probability of sampling the optimal portfolio solution with WS-QAOA than standard QAOA for a 6-asset instance at depths p = 1 to 5
- 250 random portfolio instances evaluated at depth p = 1; WS-QAOA energies were much closer to exact minimum energies than standard QAOA
- Portfolio experiments used n = 6 assets, budget B = 3, and QAOA depths p = 1 to 5
- MAXCUT depth-1 WS-QAOA on 10 fully connected 30-node graphs, using 5 GW warm starts per graph: median normalized energy was 0.907 at ε = 0 and 0.929 at ε = 0.25
- WS-RQAOA benchmarked on 100 graphs for each setting: n = 20 and n = 30, for both sparse random graphs (pE = 1/2, weights ±1) and fully connected graphs (weights uniformly from -10 to 10)
- For GW alone on 30-node graphs, average cut quality was about 85.2% of maximum for sparse random graphs and 83.7% for fully connected random-weight graphs
- For sparse 30-node graphs, generating more than 100 GW cuts found the maximum cut in more than 80 of 100 graphs; for fully connected 30-node graphs, 61 of 100 maximum cuts were found at N = 10^5
- On a 6-node fully connected MAXCUT instance with maximum cut value 27 and initial warm-start cut value 23, increasing WS-QAOA depth from p = 1 to 6 increased maximum-cut sampling probability and lowered energy
## Quantum advantage claim
**Classification:** speculative

The paper reports simulated improvements of warm-started QAOA/RQAOA over standard QAOA/RQAOA and slight gains over a specific recursive classical GW-based baseline, but it does not demonstrate a clear quantum advantage over best-known classical algorithms or on real hardware. Claims about preserving or improving classical approximation guarantees are largely theoretical or suggestive rather than empirically establishing quantum advantage.
## Limitations
- Experiments are primarily simulation-based using Qiskit's state-vector simulator rather than execution on real quantum hardware.
- The portfolio optimization study is limited to very small instances (n = 6 assets), constraining conclusions about scalability.
- MAXCUT studies use relatively small graphs (mainly 20- and 30-node instances, plus a single 6-node graph for p > 1), limiting evidence for larger-scale performance.
- The only source of randomness in the portfolio experiments is the random initialization of COBYLA because noiseless simulation is used, so hardware noise, sampling noise, and readout errors are not assessed.
- Implementing QAOA on noisy quantum hardware is acknowledged as challenging because circuits can be deep and require additional SWAP gates when hardware connectivity mismatches the problem structure.
- Near-term applicability is effectively restricted to low-depth QAOA due to current gate fidelities and hardware limitations.
- For rounded warm-start QAOA on MAXCUT, modifying the mixer to retain the Goemans-Williamson guarantee introduces an inconsistency between the mixer and the initial state.
- Because the modified mixer no longer has the prepared initial state as an eigenstate, the authors cannot use the standard convergence arguments to prove convergence to the global optimum as depth increases.
- The p > 1 WS-RQAOA analysis is only demonstrated on a single graph, so evidence for deeper-circuit behavior is limited.
- The optimization landscape is non-convex with many local minima, making it difficult to find globally optimal variational parameters and potentially affecting internal validity of empirical comparisons.
- The study relies on specific classical optimizers and initialization heuristics (e.g., COBYLA, grid search), so results may be sensitive to optimizer choice and tuning.
- The portfolio benchmark uses synthetic data generated from geometric Brownian motion rather than real financial market datasets.
- Budget constraints in portfolio optimization are enforced via a large quadratic penalty term rather than being built directly into the quantum circuit, which may affect solution quality and generality.
- The work limits itself to the basic SDP relaxation in practice because stronger hierarchies have super-polynomial classical runtime, reducing the scope of warm-start variants actually tested.
- Using SDP-style warm starts directly in quantum state preparation may require O(n^2) or more qubits, which the authors note is impractical in the near term.
- More elaborate representations of SDP solutions have been proposed, but the paper notes it is not yet clear how to implement the related oracles in practice.
- [inferred] No experiments report shot-based sampling uncertainty, confidence intervals over hardware executions, or noise-mitigation performance, limiting reproducibility for NISQ settings.
- [inferred] No direct benchmarking against strong state-of-the-art classical portfolio or MAXCUT heuristics beyond relaxations/rounding is provided, limiting assessment of practical quantum advantage.
- [inferred] The authors are affiliated with IBM Quantum, and the implementation is in Qiskit; while not necessarily problematic, this may introduce ecosystem-specific bias in tooling and evaluation.
- [inferred] Scalability to production financial services workloads is unproven because experiments are confined to toy instances and synthetic settings.
## Open questions
- Can warm-started quantum optimization strictly improve on Goemans-Williamson approximation guarantees, especially if the Unique Games Conjecture is false?
- How do convergence properties change when using a modified mixer that does not have the initial state as an eigenstate?
- How does WS-RQAOA perform at depths p > 1 across a broader range of graph sizes and graph families?
- What is the best choice of regularization parameter epsilon for different problems and instance classes?
- How robust are the reported improvements under realistic hardware noise, limited connectivity, and finite sampling?
- Can stronger relaxations or alternative randomized-rounding schemes yield better warm starts without prohibitive classical overhead?
- How should SDP solutions be encoded efficiently on quantum hardware without requiring impractical qubit counts or hard-to-implement oracle constructions?
- Can continuous warm-start ideas be integrated effectively with RQAOA?
- Will warm-starting remain beneficial as problem size grows beyond the small instances studied here?
- How much of the observed gain comes from the warm start itself versus the classical preprocessing and parameter-initialization heuristics?
- Can warm-start methods be generalized effectively to other combinatorial optimization and integer programming problems relevant to finance?

**Future work:**
- Investigate tying budget constraints directly into the WS-QAOA quantum circuit for portfolio optimization.
- Extend WS-RQAOA simulations at depths p > 1 to more graphs with different sizes.
- Explore other warm-starts based on polynomially solvable special cases.
- Consider low-rank approximations of the covariance matrix Sigma or the SDP as alternative warm-start mechanisms.
- Analyze convergence properties when using a modified mixer that does not have the initial state as an eigenstate.
- Investigate RQAOA in the context of the continuous warm-start approach used for portfolio optimization.
- Warm-start quantum optimization from candidate solutions produced by classical solvers such as CPLEX or GUROBI with time-limit termination criteria.
- Apply warm-start methods to other combinatorial optimization and integer programming problems, including those encoded as QUBO, MILO, or PUBO formulations.
- Study warm-start applicability to binary optimization problems where approximate solutions can be found from relaxed problems without randomized rounding.
- [inferred] Validate the approach on real quantum hardware with noise-aware benchmarking and error-mitigation strategies.
- [inferred] Test on larger, more realistic financial datasets and production-scale portfolio instances.
- [inferred] Compare against stronger classical baselines to clarify whether warm-started quantum methods offer practical benefits beyond classical preprocessing.
## Key ideas
- #idea:hybrid-approach — Uses classical QP/SDP relaxations and Goemans–Williamson-style rounding to warm-start QAOA/RQAOA, with custom mixers matched to the warm-start state.
- #idea:near-term-feasibility — Warm-starting improves low-depth QAOA performance on small portfolio instances, which is positioned as useful for NISQ-era constraints.
- #idea:hybrid-approach — Portfolio optimisation is formulated as a Markowitz-style QUBO with budget penalty, and the continuous relaxation solution is encoded into qubit rotations and mixer design.
- #idea:near-term-feasibility — In simulation, WS-QAOA gives substantially better energies and more than 5x higher optimal-solution sampling probability than standard QAOA on 6-asset portfolio instances.
- #idea:quantum-advantage — The paper argues warm-started QAOA may inherit classical approximation guarantees and potentially exceed classical rounding in some regimes, but this remains theoretical/speculative.
- #idea:hybrid-approach — Recursive warm-start QAOA combines classical warm starts with recursive variable elimination, outperforming standard RQAOA in simulated MAXCUT benchmarks.
## Contradictions
- The paper suggests potential quantum advantage via inherited or improved approximation guarantees, but all evidence is simulation-based and does not establish superiority over strong classical state-of-the-art methods; this supports #contradiction:classical-vs-quantum.
- The paper motivates applicability to realistic finance and broader combinatorial optimisation, yet the finance experiments are restricted to synthetic 6-asset portfolio instances and no real hardware runs, which conflicts with broader practical claims and supports #contradiction:scalability.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
