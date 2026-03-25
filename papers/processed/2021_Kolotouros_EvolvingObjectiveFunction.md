---
aliases:
- An evolving objective function for improved variational quantum optimisation
- evolving objective function improved
authors:
- Ioannis Kolotouros
- Petros Wallden
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
relevance_phase3: medium
source_type: preprint
source_type_confidence: high
step1_date: '2026-03-25T15:54:13.034380'
step1_model: gpt-5.1
step2_date: '2026-03-25T15:54:16.739012'
step2_model: gpt-5.1
step3_date: '2026-03-25T15:54:59.172312'
step3_model: gpt-5.4
step4_date: '2026-03-25T15:55:33.835738'
step4_model: gpt-5.4
step5_date: '2026-03-25T15:56:02.435652'
step5_model: gpt-5.4
step6_date: '2026-03-25T15:56:12.924363'
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
- method/VQE
- method/QUBO
- method/variational
- method/classical-simulation
- idea/quantum-advantage
- idea/near-term-feasibility
- idea/hybrid-approach
- contradiction/classical-vs-quantum
- contradiction/scalability
title: An evolving objective function for improved variational quantum optimisation
topic_tags:
- portfolio-optimisation
- risk-modelling
year: 2022
zotero_key: ''
---

## Abstract summary
The paper proposes an evolving objective function, termed Ascending-CVaR, for variational quantum algorithms applied to optimisation problems. Instead of using a fixed Conditional Value-at-Risk (CVaR) parameter, the method gradually increases the fraction of low-energy measurement outcomes included in the cost function during optimisation, interpolating from a small-tail CVaR to the full energy expectation. Through classical simulations on Max-Cut, Number Partitioning, and Portfolio Optimisation using both VQE with hardware-efficient ansätze and QAOA, the authors show that Ascending-CVaR improves convergence speed, increases overlap with the optimal solution, and helps avoid suboptimal local minima compared to standard expectation-value and fixed-CVaR objectives.
## Methodology
This preprint presents a hybrid theoretical-and-empirical study proposing a new evolving objective function, Ascending-CVaR, for variational quantum optimization. The authors extend the fixed Conditional Value-at-Risk (CVaR) objective by gradually increasing the tail parameter alpha during optimization, using either linear or sigmoid schedules, motivated by propositions about shared global minima and changing local minima across CVaR landscapes. Empirically, they evaluate the method via classical numerical simulation/emulation on three combinatorial optimization case studies relevant to finance and optimization: Max-Cut, Number Partitioning, and Portfolio Optimization. They benchmark both VQE with a hardware-efficient ansatz and QAOA against fixed-CVaR baselines (alpha = 0.1, 0.2, 0.5) and the standard expectation-value objective (alpha = 1). Experiments are run on multiple problem instances of varying sizes up to 20 qubits, with performance assessed primarily by overlap with the optimal solution, success rate defined as achieving at least 10% overlap, and normalized optimizer iterations/time to reach that threshold. The study reports that Ascending-CVaR improves convergence behavior and avoids suboptimal minima, especially on harder instances, and includes code availability via GitHub.

**Algorithms used:** VQE, QAOA, CVaR, Ascending-CVaR, COBYLA
**Frameworks:** Qiskit Aer, NetworkX

**Experimental setup:** Experiments were conducted in a classical emulation/numerical simulation environment using IBM's Qiskit Aer noiseless multi-shot simulator. The study tested VQE with a hardware-efficient ansatz and QAOA on problem instances up to 20 qubits. For VQE, depth p = 1 was used; for QAOA, depths p = 1 to 6 were tested. All runs used a gradient-free COBYLA optimizer, random initialization of variational parameters, and a maximum budget of 66 times the number of ansatz parameters in optimizer iterations. Circuit evaluations used K = 1000 shots, scaled to K/alpha for fixed CVaR and analogously with time-varying alpha_t for Ascending-CVaR.

**Dataset:** Synthetic/generated optimization instances rather than a conventional dataset. Max-Cut used 100 random non-regular unweighted graphs with 15-19 vertices sampled from graph classes via NetworkX. Number Partitioning used randomly generated integer sets of size 17-20 drawn uniformly from ranges N1={0,...,200}, N2={0,...,500}, N3={0,...,750}, and for some QAOA tests M={0,...,50}. Portfolio Optimization used 100 random portfolio instances with 16-20 assets, random budgets drawn uniformly from {0,...,n}, and varying risk factors q; expected returns and covariance inputs are treated as generated/random portfolio parameters.
## Findings
- [supported] The paper introduces Ascending-CVaR, an evolving objective function that gradually increases the CVaR tail parameter during variational optimization, intended to avoid suboptimal local minima.
- [supported] In classical emulation/simulation up to 20 qubits, Ascending-CVaR outperformed both the standard expectation-value objective and fixed-α CVaR across Max-Cut, Number Partitioning, and Portfolio Optimization instances.
- [supported] Ascending-CVaR achieved higher overlap with the optimal state in all tested problem classes, with up to 10x greater average overlap for Portfolio Optimization and Number Partitioning and about 80% improvement for Max-Cut relative to the expectation-value baseline.
- [supported] For hard Number Partitioning instances, standard objective functions found the correct solution in almost none of the cases, fixed CVaR succeeded in about 60% of cases, and Ascending-CVaR succeeded in 95% of cases.
- [supported] For 100 random non-regular Max-Cut instances (15-19 vertices) using VQE, Ascending-CVaR was successful in 96 instances versus 84, 81, 68, and 53 for fixed α=0.1, 0.2, 0.5, and expectation value respectively.
- [supported] For Max-Cut VQE on those random graph instances, average overlap was 64.69% for Ascending-CVaR versus 12.13%, 21.45%, 39.28%, and 36.24% for fixed α=0.1, 0.2, 0.5, and expectation value respectively.
- [supported] For Number Partitioning VQE, Ascending-CVaR consistently improved both success rate and average overlap across three instance sets, including the hardest set where a sigmoid schedule was used.
- [supported] For the hardest Number Partitioning set, Ascending-CVaR achieved 95 successful runs out of 100 with 56.85% average overlap, versus 58, 24, 9, and 0 successful runs for fixed α=0.1, 0.2, 0.5, and expectation value respectively.
- [supported] For Portfolio Optimization VQE on 100 random portfolios with 16-20 assets, Ascending-CVaR succeeded on all 100 instances and achieved 63.25% average overlap, compared with 13.35%, 24.74%, 9.42%, and 0.64% for fixed α=0.1, 0.2, 0.5, and expectation value respectively.
- [supported] Ascending-CVaR often reached the 10% overlap threshold in fewer normalized optimizer iterations than fixed-CVaR baselines, indicating improved convergence speed in addition to better final overlap.
- [supported] The paper reports that VQE with a hardware-efficient ansatz performed much better than shallow-depth QAOA for the tested optimization problems, regardless of objective function.
- [supported] In QAOA experiments, Ascending-CVaR still improved overlap relative to fixed objectives in some instances, but shallow-depth QAOA generally produced low-overlap states and remained less effective than VQE.
- [speculative] The authors argue that varying α changes the optimization landscape and can erase false local minima while preserving the true global minimum under certain overlap conditions.
- [supported] The paper states and uses propositions showing that CVaR objectives with different α values share the same global minimum under overlap condition α≤κ, while local minima can differ across α values.
- [speculative] The authors suggest that dynamic objective functions like Ascending-CVaR could help bring variational algorithms closer to useful quantum advantage for practical optimization problems.
- [speculative] Claims about practical quantum advantage are not demonstrated because all reported results are from noiseless classical simulation/emulation rather than real quantum hardware or classical runtime comparisons.

**Results summary:** This preprint proposes Ascending-CVaR, a dynamic objective function for variational quantum optimization that starts with a low-tail CVaR objective and gradually increases toward the full expectation value. The method is evaluated in noiseless classical emulation using VQE with a hardware-efficient ansatz and shallow-depth QAOA on Max-Cut, Number Partitioning, and Portfolio Optimization problems up to 20 qubits/assets. Across all three problem classes, the authors report that Ascending-CVaR improves success rates, overlap with the optimal solution, and often convergence speed relative to both fixed-α CVaR and the standard expectation-value objective. The strongest gains are reported for VQE, especially on harder Number Partitioning and Portfolio Optimization instances, while QAOA remains comparatively weak at the tested depths. Because the study is a preprint and all evidence comes from simulation rather than real hardware or end-to-end classical benchmarking, any broader quantum advantage implications remain speculative.

**Performance claims:**
- Simulation/emulation up to 20 qubits
- Up to 10x greater average overlap for Portfolio Optimization and Number Partitioning versus expectation-value objective
- About 80% improvement in overlap for Max-Cut versus expectation-value objective
- Hard Number Partitioning instances: standard objective succeeds in almost 0% of cases, fixed CVaR in 60%, Ascending-CVaR in 95%
- Max-Cut VQE, 100 random non-regular graphs (15-19 vertices): successful instances = 96 (Ascending-CVaR) vs 84 (α=0.1) vs 81 (α=0.2) vs 68 (α=0.5) vs 53 (expectation value)
- Max-Cut VQE average overlap: 64.69% (Ascending-CVaR) vs 12.13% (α=0.1) vs 21.45% (α=0.2) vs 39.28% (α=0.5) vs 36.24% (expectation value)
- Number Partitioning VQE, set N1: successful instances = 87 vs 85 vs 66 vs 16 vs 2; average overlap = 54.17% vs 11.50% vs 16.56% vs 7.94% vs 0.99%
- Number Partitioning VQE, set N2: successful instances = 80 vs 69 vs 29 vs 11 vs 0; average overlap = 48.33% vs 10.24% vs 7.56% vs 5.88% vs 0.4%
- Number Partitioning VQE, hardest set N3: successful instances = 95 vs 58 vs 24 vs 9 vs 0; average overlap = 56.85% vs 8.24% vs 5.84% vs 3.45% vs 0.16%
- Portfolio Optimization VQE, 100 random portfolios (16-20 assets): successful instances = 100 vs 100 vs 100 vs 16 vs 1
- Portfolio Optimization VQE average overlap: 63.25% (Ascending-CVaR) vs 13.35% (α=0.1) vs 24.74% (α=0.2) vs 9.42% (α=0.5) vs 0.64% (expectation value)
- Average normalized iterations to reach 10% overlap: Portfolio Optimization 9.64 (Ascending-CVaR) vs 11.13 (α=0.1) vs 16.29 (α=0.2)
- Average normalized iterations to reach 10% overlap: Number Partitioning N1 12.1 vs 19.76 vs 25.09; N2 14.73 vs 24.13 vs 28.86; N3 27.12 vs 25.12 vs 33.62
- Average normalized iterations to reach 10% overlap: Max-Cut 8.75 (Ascending-CVaR) vs 9.3 (α=0.1) vs 10.8 (α=0.2)
- In one Max-Cut QAOA example, Ascending-CVaR achieved 7% overlap while all fixed objectives stayed below 3%
- In one Number Partitioning QAOA example, Ascending-CVaR achieved roughly 100% higher overlap than other objective functions
## Quantum advantage claim
**Classification:** speculative

The paper discusses bringing variational algorithms closer to useful quantum advantage, but all evidence is from noiseless classical simulation/emulation rather than real quantum hardware or rigorous classical runtime advantage benchmarks. As a preprint, any quantum advantage claim is therefore speculative.
## Limitations
- Experiments are conducted only in a noiseless emulation environment (Qiskit Aer simulator), not on real quantum hardware
- Simulations are limited to relatively small problem sizes, using up to 20 qubits
- The study focuses on shallow circuits: VQE only at depth p = 1 and QAOA up to p = 6
- Performance depends sensitively on the ascending factor λ and the choice of ascending function, requiring tuning
- The authors note that if problem sizes increase or the problem class changes, the hyperparameter λ would need to be readjusted
- Theoretical investigation of how to choose the ascending factor and ascending function is left out of scope
- The connection between the proposed method and adiabatic quantum computing is not developed and is deferred
- QAOA performs poorly on the tested problems at small depth, especially for portfolio optimisation, limiting conclusions for that ansatz
- For harder Number Partitioning instances, the method required switching from linear to sigmoid ascent, suggesting limited robustness of a single schedule across instances
- The evaluation uses a fixed success threshold of 10% overlap, which the authors acknowledge is somewhat arbitrary
- The study uses a fixed shot budget design (K = 1000, scaled as K/α), so conclusions may depend on this measurement setting
- Only three combinatorial optimisation problems are tested: Max-Cut, Number Partitioning, and Portfolio Optimisation
- The portfolio optimisation formulation is restricted to a specific mean-variance model with cardinality/budget constraint, not broader financial optimisation settings
- [inferred] No experiments on real financial market datasets are described for portfolio optimisation; practical financial relevance is therefore only partially validated
- [inferred] No comparison is made against state-of-the-art classical optimisation baselines for the tested instances, beyond discussion of prior literature
- [inferred] Claims about bringing quantum advantage closer are not supported by runtime or end-to-end comparisons against strong classical solvers
- [inferred] Results rely on random initialisations and heuristic optimisation (COBYLA), which may affect reproducibility and stability despite code availability
- [inferred] The use of hardware-efficient ansatz may limit interpretability and may not reflect the best ansatz choice for each problem
- [inferred] Scalability to production-scale financial problems is untested given the small qubit counts and simulator-only setup
- [inferred] Resource overhead from CVaR-style objectives, which require more measurements as α decreases, may become significant at larger scales
- [inferred] As a preprint, the work has not undergone peer review
## Open questions
- How should the ascending factor λ be selected systematically based on the problem class and instance features?
- Which ascending schedule (linear, sigmoid, or other) is best for different optimisation problems and instance hardness levels?
- Can the method be theoretically connected to adiabatic quantum computing in a principled way?
- How well does Ascending-CVaR perform on larger problem instances beyond 20 qubits?
- Will the observed improvements persist on real noisy NISQ hardware with decoherence and gate errors?
- Can the method improve QAOA substantially at greater depths, or is its benefit mainly limited to VQE-like settings?
- What is the trade-off between improved optimisation landscapes and the increased shot cost induced by small α values?
- Can the optimisation be truncated at some α < 1 without sacrificing solution quality, and how should that threshold be chosen?
- How general is the method beyond the three tested combinatorial problems?
- For portfolio optimisation, does the method remain effective on realistic financial datasets and more complex portfolio models such as dynamic or multi-period settings?
- [inferred] How does Ascending-CVaR compare against strong classical heuristics and exact solvers on the same benchmark instances?
- [inferred] How robust are the results to different optimisers, ansatz choices, shot budgets, and random seeds?
- [inferred] Does the method mitigate barren plateaus or only local-minimum trapping, and under what conditions?

**Future work:**
- Generalise the approach by studying how to set the hyperparameter λ and the α-increase function more systematically
- Explore systematic rules for fixing the extra degrees of freedom according to the problem and specific instance characteristics
- Investigate other dynamic objective functions beyond Ascending-CVaR
- Study the theoretical choice of ascending factor and ascending function for different optimisation problems
- Investigate possible connections between Ascending-CVaR and adiabatic quantum computing in subsequent work
- Consider truncating the optimisation before α reaches 1 to reduce iterations while maintaining useful overlap
- [inferred] Validate the method on real quantum hardware with noise mitigation
- [inferred] Benchmark against stronger classical baselines and larger-scale instances
- [inferred] Extend evaluation to more realistic financial applications, including real market data and dynamic portfolio optimisation
## Key ideas
- #idea:hybrid-approach — Proposes Ascending-CVaR, a dynamic CVaR objective for hybrid variational optimisation, used with VQE and QAOA plus classical COBYLA optimisation.
- #idea:near-term-feasibility — Frames Ascending-CVaR as a NISQ-relevant improvement to variational algorithms by improving convergence and reducing trapping in suboptimal local minima on small instances.
- #idea:quantum-advantage — Reports substantially better simulated optimisation performance than fixed-CVaR and expectation objectives, including up to 10x higher average overlap on portfolio optimisation instances.
- #idea:hybrid-approach — Portfolio optimisation is formulated as a QUBO/Ising problem and solved via variational quantum circuits with an evolving objective rather than changing the ansatz itself.
- #idea:near-term-feasibility — VQE with a hardware-efficient ansatz performed markedly better than shallow QAOA in the tested portfolio and combinatorial optimisation settings.
- #idea:quantum-advantage — The paper argues that changing the CVaR tail parameter during training can preserve the global optimum while altering local minima, thereby improving trainability.
## Contradictions
- The paper suggests progress toward useful quantum advantage, but its evidence is entirely from noiseless classical simulation on up to 20 qubits with no runtime comparison against strong classical solvers; this contradicts any strong claim of demonstrated quantum superiority.
- The paper presents improved optimisation outcomes for portfolio optimisation, yet scalability to realistic financial problem sizes is untested and explicitly limited by simulator-only experiments on small synthetic instances, contradicting implications of near-term deployment on real finance workloads.
- The paper positions the method as NISQ-relevant, but it does not test noise or real hardware; this creates tension with the practical near-term applicability narrative because noise sensitivity remains unresolved.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->

## Experiment details
### Input
Inputs consisted of three classes of optimization instances. Max-Cut: 100 random non-regular unweighted graph instances with 15-19 vertices generated using NetworkX. Number Partitioning: 300 instances with 17-20 integers sampled uniformly from three ranges, N1={0,...,200}, N2={0,...,500}, and N3={0,...,750}; additional QAOA experiments used smaller-range instances M={0,...,50}. Portfolio Optimization: 100 random portfolio instances with 16-20 assets, budget B sampled uniformly from {0,...,n}, and multiple risk factors q; the paper does not specify an external financial data source, suggesting synthetic/randomly generated expected returns and covariance matrices. Problems were mapped to QUBO/Ising Hamiltonians before optimization.

### Process
For each optimization problem, the authors first mapped the classical objective to an Ising Hamiltonian. They then optimized variational circuits using either VQE or QAOA. In VQE, a hardware-efficient ansatz with Ry rotations and CZ entanglers was used; in QAOA, alternating cost and mixer unitaries were applied for p layers. Parameters were randomly initialized and optimized with COBYLA. The key methodological intervention was the objective function: instead of a fixed expectation value or fixed CVaR_alpha, Ascending-CVaR updated alpha during optimization. Two schedules were tested: linear ascending, alpha_{t+1} = alpha_t + lambda, with lambda in [0.025, 0.045], and sigmoid ascending, alpha_t = 1/(1+e^(5-lambda t)), with lambda in [0.3, 0.4]. The initial alpha was typically 0.01. Four ascending functions were initially compared (sigmoid, linear, exponential, logarithmic), and linear/sigmoid were selected. Baselines used fixed alpha values 0.1, 0.2, 0.5, and 1. Each circuit evaluation used 1000 shots, scaled as K/alpha to maintain CVaR estimation accuracy. Optimization stopped when the stopping condition or iteration budget was met; all instances were allowed up to 66 times the number of ansatz parameters in optimizer iterations. Performance was tracked over normalized optimizer iterations and, in an appendix, circuit repetitions.

### Output
Reported outputs included overlap with the optimal solution (probability mass on degenerate ground states), success rate defined as achieving at least 10% overlap, average overlap across instances, and normalized optimizer iterations required to reach 10% overlap. The paper also presents qualitative convergence curves and comparative statistics across methods. Baselines were fixed-CVaR objectives with alpha = 0.1, 0.2, 0.5 and the standard expectation-value objective (alpha = 1). For some tasks, the authors additionally discuss approximation ratio and circuit repetitions, but the main comparative outputs are overlap-based metrics and success/failure counts.

### Parameters
- max_qubits: 20
- vqe_depth: 1
- qaoa_depth_range: 1-6
- shots_base: 1000
- shots_scaling: K/alpha for CVaR; analogous scaling with alpha_t for Ascending-CVaR
- optimizer: COBYLA
- max_optimizer_iterations: 66 x number_of_ansatz_parameters
- vqe_ansatz: hardware-efficient ansatz with Ry rotations and CZ entanglers
- vqe_parameter_count: n(1+p)
- qaoa_parameter_count: 2p
- ascending_initial_alpha: 0.01
- fixed_cvar_alphas: [0.1, 0.2, 0.5, 1.0]
- linear_lambda_range: [0.025, 0.045]
- sigmoid_lambda_range: [0.3, 0.4]
- portfolio_linear_lambda: 0.045
- number_partitioning_linear_lambda: 0.03
- success_threshold_overlap: 0.1

### Hardware
IBM Qiskit Aer simulator; noiseless multi-shot circuit execution in a classical emulation environment. No real QPU was used. The paper does not report a noise model, cloud backend, or transpilation settings.

### Reproducibility
Code is reported as available on GitHub (link provided in the paper). Instance generation procedures are described at a moderate level, and simulator/optimizer settings are mostly specified. However, some details for portfolio data generation (e.g., exact distributions for returns/covariances) are not fully specified in the excerpt, so replication appears feasible but not fully turnkey for all experiments.
