---
aliases:
- Solving General QUBOs with Warm-Start QAOA via a Reduction to Max-Cut
- Solving General QUBOs Warm
authors:
- Bikrant Bhattacharyya
- Michael Capriotti
- Reuben Tate
auto_detected: true
classification: ''
contradiction_flags:
- contradiction:classical-vs-quantum
- contradiction:scalability
doi: ''
evidence_type: ''
idea_tags:
- idea:near-term-feasibility
- idea:hybrid-approach
journal_or_venue: ACM Transactions on Quantum Computing
methodology_tags:
- QAOA
- QUBO
- classical-simulation
paper_type: ''
quantum_advantage_claim: not-applicable
related_papers: []
relevance_phase1: high
relevance_phase3: medium
source_type: peer-reviewed-empirical
source_type_confidence: high
step1_date: '2026-03-25T16:06:51.678886'
step1_model: gpt-5.1
step2_date: '2026-03-25T16:06:57.683072'
step2_model: gpt-5.1
step3_date: '2026-03-25T16:07:43.955375'
step3_model: gpt-5.4
step4_date: '2026-03-25T16:08:20.526391'
step4_model: gpt-5.4
step5_date: '2026-03-25T16:08:50.097094'
step5_model: gpt-5.4
step6_date: '2026-03-25T16:09:04.988108'
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
- idea/near-term-feasibility
- idea/hybrid-approach
- contradiction/classical-vs-quantum
- contradiction/scalability
title: Solving General QUBOs with Warm-Start QAOA via a Reduction to Max-Cut
topic_tags:
- portfolio-optimisation
year: 2025
zotero_key: ''
---

## Abstract summary
The paper studies how to apply semidefinite-programming-based warm-start strategies for QAOA to general QUBO problems by first reducing them to Max-Cut instances. The authors empirically compare this Max-Cut-based warm-start approach against a direct QUBO relaxation warm-start across several classes of QUBOs, including random instances and structured problems like TSP, maximum independent set, and portfolio optimization. They show that performance depends strongly on the problem type and discuss how the auxiliary variable introduced by the QUBO-to-Max-Cut mapping can be exploited to improve warm-start heuristics.
## Methodology
The paper presents an empirical benchmarking study of warm-started QAOA for general QUBO problems by introducing a reduction from an n-variable QUBO to an equivalent (n+1)-vertex Max-Cut instance and then applying semidefinite-programming-based warm starts originally developed for Max-Cut. The authors compare this QUBO-to-Max-Cut warm-start strategy against a direct QUBO-relaxation warm-start baseline. They evaluate several warm-start variants derived from semidefinite relaxations, specifically Goemans-Williamson projected to 2 or 3 dimensions (GW2, GW3) and Burer-Monteiro relaxations in 2 or 3 dimensions (BM2, BM3), as well as the QUBO-relaxed initialization. For Max-Cut-based warm starts, they also test vertex-at-top rotation choices (first qubit, last/auxiliary qubit, or no rotation). Experiments are conducted on multiple classes of QUBO instances up to 16 variables: random continuous and discrete QUBOs, traveling salesman problem, portfolio optimization, and maximum independent set on two graph ensembles. For each problem class, 1000 instances are generated and evaluated at depth p=0, and 10 of those instances are further run for QAOA depths 1 through 5. Performance is assessed using two normalized metrics: an instance-specific approximation ratio and the probability of sampling an optimal solution. Results are reported as averages with shaded bands of ±0.25 standard deviations, and comparisons are made across warm-start families, rotation choices, and for QUBO-relaxed, different numbers of random initializations (10 vs 50).

**Algorithms used:** QAOA, Warm-start QAOA, Goemans-Williamson relaxation, Burer-Monteiro relaxation, QUBO-relaxation, L-BFGS-B, COBYLA

**Experimental setup:** All experiments were simulation-based using a custom QAOA simulator. QUBO instances had 16 binary variables; after reduction to Max-Cut, corresponding graphs had 17 vertices/qubits. Depth-0 experiments were run on 1000 instances per problem class; 10 selected instances per class were then run for QAOA depths p=1 to 5. QAOA parameter optimization used COBYLA, with 10 optimization restarts per circuit. For p=1, all 10 initial parameter settings were drawn uniformly; for p>1, 9 were random and 1 was seeded from the best solution at depth p-1. The final circuit parameters were chosen as the best-cost result among the 10 runs. Warm-start generation used GW2, GW3, BM2, BM3, and QUBO-relaxed methods, with vertex-at-top rotations tested on the first qubit, last auxiliary qubit, or none.

**Dataset:** Synthetic benchmark instances only. These include 16-variable random QUBOs with entries sampled either continuously from Uniform[-1,1] or discretely from {-1,1}; 5-city TSP instances generated from random points in [-1,1]^2; portfolio optimization instances generated from simulated geometric Brownian motion stock prices for 16 assets over 250 time steps; and maximum independent set instances on 16-node Erdős-Rényi and Newman-Watts-Strogatz random graphs.
## Findings
- [supported] The paper empirically evaluates warm-start QAOA for general QUBOs by reducing them to Max-Cut and finds that the best warm-start strategy is strongly problem-dependent across random QUBOs, traveling salesman, portfolio optimization, and maximum independent set instances.
- [supported] Among SDP-based warm-starts tested, Goemans-Williamson projected to 2 dimensions (GW2) was the best overall performer, with BM2/BM3 achieving similar approximation ratios but significantly lower optimal sampling probabilities.
- [supported] For most problem classes except TSP, applying the vertex-at-top rotation to the auxiliary qubit introduced by the QUBO-to-Max-Cut mapping gave the best GW2 performance; the ranking was typically last-qubit rotation > first-qubit rotation > no rotation.
- [supported] For random QUBOs, GW2 achieved better instance-specific approximation ratios than QUBO-Relaxed, but worse optimal sampling probabilities, indicating GW2 often concentrates amplitude on high-quality but not necessarily optimal solutions.
- [supported] For portfolio optimization, GW2 outperformed QUBO-Relaxed on both metrics tested, with very high approximation ratios and high optimal sampling probabilities.
- [supported] For MIS instances, GW2 performance was intermediate between QUBO-Relaxed with 10 and 50 random initializations, and usually within 0.25 standard deviations of QUBO-Relaxed with 50 initializations.
- [supported] For TSP, GW2 produced the best optimal sampling probability among compared methods, but QUBO-Relaxed with 50 initializations achieved better approximation ratio.
- [supported] Increasing QUBO-Relaxed local-optimizer restarts from 10 to 50 generally improved performance, with the largest gains observed on constrained problems such as TSP and MIS.
- [supported] Portfolio optimization is a special case where the QUBO relaxation is convex/efficiently solvable because the QUBO matrix is negative semidefinite, so QUBO-Relaxed does not depend on the number of random initializations for the warm-start construction.
- [supported] All reported results are from classical simulation of QAOA circuits on problem sizes up to 16 QUBO variables (17 vertices after reduction), not from real quantum hardware.
- [speculative] The authors suggest that larger QUBO-Relaxed problems would likely require more optimizer iterations/random initializations because the underlying nonconvex relaxation has no performance guarantees.

**Results summary:** This peer-reviewed empirical study benchmarks warm-start QAOA for general QUBOs by mapping them to Max-Cut and comparing SDP-based warm-starts (GW2, GW3, BM2, BM3) against a direct QUBO-Relaxed warm-start. Experiments were run in classical simulation on 1000 instances per problem class at depth p=0 and on 10 selected instances for depths 1 to 5, using 16-variable QUBOs. The main empirical conclusion is that no single warm-start dominates across all tasks, but GW2 is the strongest SDP-based method overall. The auxiliary-qubit vertex-at-top rotation usually improves performance and is often the best rotation choice. GW2 tends to deliver stronger approximation ratios on random QUBOs and clearly outperforms QUBO-Relaxed on portfolio optimization, while QUBO-Relaxed can be competitive or better on constrained problems depending on the metric and number of optimizer restarts. The study does not demonstrate quantum advantage; results are simulation-based and compare warm-start heuristics within QAOA rather than against best classical solvers at scale.

**Performance claims:**
- 1000 instances per problem type evaluated at depth p=0; 10 of those 1000 evaluated at depths 1<=p<=5
- Problem size: 16 QUBO variables, mapped to 17-vertex Max-Cut instances
- For continuous random QUBOs at p=5, GW2 last-rotation achieved alpha=0.9315±0.2107 and P=0.1938±0.2107
- For discrete random QUBOs at p=5, GW2 last-rotation achieved alpha=0.9311±0.2182 and P=0.2238±0.2182
- For TSP at p=5, GW2 no-rotation achieved P=0.0026±0.0037, while GW2 last-rotation achieved alpha=0.9488±0.0020
- For portfolio optimization at p=5, GW2 last-rotation achieved alpha=0.9993±0.2266 and P=0.9215±0.2266
- For MIS-GNP at p=5, GW2 last-rotation achieved alpha=0.9222±0.1458 and P=0.1134±0.1458
- For MIS-NWS at p=5, GW2 first-rotation achieved alpha=0.8851±0.0475 and P=0.1139±0.1429; GW2 last-rotation achieved alpha=0.8672±0.1057 and P=0.0699±0.1057
- For portfolio optimization, QUBO-Relaxed BM2 baseline values were alpha=0.9684±0.0075 and P=0.0016±0.0075, substantially below GW2 on P
- The paper reports shaded uncertainty bands of ±0.25 standard deviations in depth plots rather than confidence intervals
## Quantum advantage claim
**Classification:** not-applicable

The paper does not demonstrate or rigorously claim quantum advantage. It compares warm-start variants of simulated QAOA on small instances and reports heuristic performance differences, without showing superiority over state-of-the-art classical optimization methods or using real quantum hardware.
## Limitations
- Experiments are limited to QUBO instances with up to 16 variables (and 17 vertices after the QUBO-to-Max-Cut mapping), restricting conclusions about larger-scale problems.
- Only 10 of the 1000 generated instances per problem class were evaluated at QAOA depths 1 through 5, limiting statistical strength for depth-dependent performance claims.
- The study uses simulation rather than real quantum hardware, so decoherence, gate errors, readout noise, and calibration drift are not empirically assessed.
- The QUBO-to-Max-Cut reduction introduces an additional auxiliary qubit/variable, increasing resource requirements and potentially worsening scalability.
- For general QUBOs, the QUBO-relaxed warm-start relies on solving a nonconvex relaxation with local optimization, which has no performance guarantees.
- Performance of the QUBO-relaxed approach is strongly dependent on the number of random initial conditions tested, making results sensitive to optimizer budget and initialization choices.
- The paper only studies shallow depths up to p = 5, so behavior at larger depths and asymptotic trends remain unclear.
- Benchmarking is restricted to a narrow set of synthetic or generated problem families (random QUBOs, small TSP, simulated portfolio optimization, MIS), limiting external validity to real financial production instances.
- Portfolio optimization experiments are based on simulated geometric Brownian motion price series rather than real market data.
- The TSP benchmark is especially small (5 cities), so conclusions for constrained combinatorial problems may not transfer to more realistic sizes.
- The study reports that the best warm-start is highly problem- and metric-dependent, which limits the ability to recommend a universally effective method.
- The vertex-at-top heuristic can incur O(n) overhead if multiple candidate vertices are tested.
- [inferred] No comparison is provided against strong state-of-the-art classical optimization baselines for the underlying QUBO instances, so practical quantum advantage is not established.
- [inferred] Because all results are simulator-based, the claimed low-depth benefits may not survive hardware noise or connectivity constraints on NISQ devices.
- [inferred] The use of custom simulation and multiple heuristic choices (optimizer settings, random bases, random initializations) may make exact reproducibility sensitive to implementation details and random seeds.
- [inferred] The added auxiliary qubit and SDP-based preprocessing may create classical and quantum overheads that reduce production scalability for financial services use cases.
- [inferred] The paper does not evaluate runtime, wall-clock cost, or end-to-end hybrid workflow efficiency, which matters for deployment in financial settings.
## Open questions
- How do the relative advantages of GW-based versus QUBO-relaxed warm-starts scale beyond 16-variable QUBOs?
- Why is warm-start performance so strongly dependent on problem type and on the chosen success metric (approximation ratio versus optimal sampling probability)?
- Under what structural conditions does the auxiliary qubit become the best choice for the vertex-at-top heuristic?
- How many random initializations are needed for the QUBO-relaxed warm-start to remain competitive as problem size grows?
- Will the observed simulator-based improvements persist on noisy quantum hardware?
- How does the QUBO-to-Max-Cut reduction affect circuit depth, routing overhead, and error accumulation on hardware with limited connectivity?
- Can these warm-start methods handle realistic financial portfolio optimization instances built from real market data, larger asset universes, and richer constraints?
- How do these methods compare with advanced classical heuristics and exact solvers on the same benchmark instances?
- What is the trade-off between better initialization quality and the extra classical preprocessing cost of SDP-based warm-starts?
- Do the conclusions hold for deeper QAOA circuits or alternative ansätze and mixer choices?

**Future work:**
- Better understand the mechanisms behind the problem- and metric-dependent performance differences between GW2 warm-starts and QUBO-relaxed warm-starts.
- Study larger problem instances, especially since the authors expect more iterations to be needed for larger non-QUBO-relaxed problems.
- Investigate scalability of the proposed QUBO-to-Max-Cut warm-start approach beyond the small instances tested here.
- Evaluate the methods on real quantum hardware to assess robustness to noise and hardware constraints.
- Test the approach on more realistic and larger financial optimization datasets, including real portfolio data.
- Develop improved strategies for selecting or learning the best vertex-at-top rotation rather than relying on heuristic choices.
- Explore more efficient or more reliable optimization methods for the nonconvex QUBO-relaxed warm-start.
- Benchmark against stronger classical baselines and measure end-to-end computational cost.
- Examine whether the auxiliary-variable insight can be generalized to other reductions and other combinatorial optimization problems.
- Assess performance at greater QAOA depths and with alternative warm-start constructions such as GW3 and Burer-Monteiro variants on larger benchmarks.
## Key ideas
- #idea:hybrid-approach — The paper proposes a hybrid workflow where classical SDP-based relaxations (especially GW2) are used to warm-start QAOA for general QUBO problems, including portfolio optimization.
- #idea:hybrid-approach — Reducing QUBO to Max-Cut allows reuse of Max-Cut warm-start heuristics, and the auxiliary qubit introduced by the reduction can be exploited via vertex-at-top rotation.
- #idea:near-term-feasibility — Warm-started QAOA is benchmarked at shallow depths p=0 to 5 on small portfolio-optimization QUBOs, showing that low-depth heuristic improvements are observable in simulation.
- #idea:hybrid-approach — For portfolio optimization specifically, GW2 warm-start outperforms the direct QUBO-relaxed warm-start on both approximation ratio and optimal-solution sampling probability in the tested simulator setting.
## Contradictions
- The extracted notes label one key idea as #idea:quantum-advantage, but the paper itself explicitly does not demonstrate or rigorously claim quantum advantage; all results are simulator-based and only compare warm-start heuristics within QAOA rather than against strong classical solvers. This supports contradiction:classical-vs-quantum.
- Although the paper reports strong portfolio-optimization performance on 16-variable instances, its own limitations state that conclusions do not yet scale to realistic financial problems because the study is restricted to tiny simulated instances, adds an auxiliary qubit through the Max-Cut reduction, and does not assess runtime or hardware overhead. This supports contradiction:scalability.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->

## Experiment details
### Input
Problem inputs were synthetically generated as follows: (1) Random QUBOs: symmetric 16x16 matrices with upper-triangular entries sampled independently either from Uniform[-1,1] or from {-1,1}, then symmetrized. (2) TSP: 5 points sampled uniformly from [-1,1]^2; edge weights set to Euclidean distances; rotational symmetry removed to obtain a 16-variable QUBO; penalty parameter lambda set to 1.1*max(A_ij). (3) Portfolio optimization: 16 assets simulated via geometric Brownian motion for N=250 time steps with initial price 1, drifts sampled uniformly from [-0.05,0.05], volatilities from [-0.20,0.20], returns used to compute mean vector and covariance matrix; budget B=8 and risk-aversion q=0.5; penalty lambda=sum(|Sigma|)+sum(|mu|). (4) MIS: 16-node graphs from Erdős-Rényi G(n=16,p=0.25) and Newman-Watts-Strogatz (n=16,k=3,p=0.5), with rejection sampling to ensure connectivity; penalty coefficient c=1.1. For each problem class, 1000 instances were generated for p=0 analysis, and 10 instances were selected for p=1..5 runs.

### Process
1. Formulate each benchmark problem as a 16-variable QUBO. 2. Either solve directly with a QUBO-relaxed warm start or map the QUBO to an equivalent 17-vertex Max-Cut instance by adding one auxiliary variable/qubit. 3. Construct warm-start initial states using one of the following: QUBO-relaxed initialization from a continuous relaxation; GWk warm starts from semidefinite relaxation followed by random projection to k=2 or 3 dimensions; or BMk warm starts from low-rank Burer-Monteiro relaxations with k=2 or 3. 4. For GWk, sample 50 random orthonormal bases and choose the projection maximizing tr(J^T Y~^T Y~). 5. For BMk, optimize the low-rank relaxation using randomized stochastic perturbations with step size eta=0.05. 6. For QUBO-relaxed, estimate the relaxed solution yc using L-BFGS-B with 100 iterations and either 10 or 50 random initial conditions for nonconvex cases; for portfolio optimization, solve the convex relaxation directly. 7. Apply optional vertex-at-top rotation to the first qubit, last auxiliary qubit, or none for Max-Cut-based warm starts. 8. Run QAOA at depths p=0..5 with custom warm-start mixer/initial state construction. 9. Optimize QAOA angles using COBYLA with 10 restarts per circuit; for p>1, include the best parameters from depth p-1 as one initialization. 10. Select the best parameter set by achieved cost and compute performance metrics.

### Output
Outputs are the instance-specific approximation ratio alpha and the optimal sampling probability P, both normalized to [0,1]. Results are reported by problem class and QAOA depth, typically as average values with shaded regions corresponding to ±0.25 standard deviations. Comparisons are made against a no-warmstart baseline, across warm-start families (GW2, GW3, BM2, BM3), across vertex-at-top rotation choices, and against QUBO-relaxed with 10 versus 50 random initializations. The study emphasizes relative performance by problem type and by metric (approximation ratio versus optimal-solution sampling probability).

### Parameters
- qubo_variables: 16
- maxcut_vertices_after_reduction: 17
- qaoa_depths: [0, 1, 2, 3, 4, 5]
- instances_per_problem_for_p0: 1000
- instances_per_problem_for_p1_to_p5: 10
- qaoa_optimizer: COBYLA
- qaoa_optimizer_restarts_per_circuit: 10
- warmstart_methods: ['GW2', 'GW3', 'BM2', 'BM3', 'QUBO-relaxed']
- vertex_at_top_options: ['first', 'last', 'none']
- qubo_relaxed_epsilon: 0.1
- qubo_relaxed_optimizer: L-BFGS-B
- qubo_relaxed_iterations: 100
- qubo_relaxed_random_initializations_compared: [10, 50]
- bm_step_size_eta: 0.05
- gw_random_bases_sampled: 50
- portfolio_time_steps: 250
- portfolio_assets: 16
- portfolio_budget_B: 8
- portfolio_risk_aversion_q: 0.5
- tsp_cities: 5
- mis_gnp_n: 16
- mis_gnp_p: 0.25
- mis_nws_n: 16
- mis_nws_k: 3
- mis_nws_p: 0.5

### Hardware
No real quantum hardware was used. All simulations were performed with a custom QAOA simulator based on prior fast simulation work cited as reference [35]. The paper does not report use of a specific commercial SDK, QPU, cloud provider, shots setting, or noise model.

### Reproducibility
The paper states that all code used to generate the data is available at reference [34], which supports reproducibility. Synthetic data generation procedures and key hyperparameters are described in detail. Replication appears feasible, although some implementation details of the custom simulator and exact instance-selection procedure for the 10 deeper runs may require consulting the linked code.
