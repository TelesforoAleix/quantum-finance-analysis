---
aliases:
- 'Extrapolation method to optimize linear-ramp quantum approximate optimization algorithm
  parameters: Evaluation of runtime scaling'
- Extrapolation method optimize linear
authors:
- Vanessa Dehn
- Martin Zaefferer
- Gerhard Hellstern
- Karthik Jayadevan
- Florentin Reiter
- Thomas Wellens
auto_detected: true
classification: ''
contradiction_flags:
- contradiction:classical-vs-quantum
- contradiction:scalability
doi: 10.1103/l5r4-zcqv
evidence_type: ''
idea_tags:
- idea:quantum-advantage
- idea:near-term-feasibility
- idea:hybrid-approach
journal_or_venue: Physical Review A
methodology_tags:
- QAOA
- QUBO
- variational
- classical-simulation
paper_type: ''
quantum_advantage_claim: speculative
related_papers:
- 2022_Herman_QuantumAdvantageLimits
relevance_phase1: high
relevance_phase3: high
source_type: peer-reviewed-empirical
source_type_confidence: high
step1_date: '2026-03-25T16:14:25.181573'
step1_model: gpt-5.1
step2_date: '2026-03-25T16:14:39.923737'
step2_model: gpt-5.1
step3_date: '2026-03-25T16:15:12.957404'
step3_model: gpt-5.4
step4_date: '2026-03-25T16:15:45.000805'
step4_model: gpt-5.4
step5_date: '2026-03-25T16:16:10.141904'
step5_model: gpt-5.4
step6_date: '2026-03-25T16:16:27.061095'
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
title: 'Extrapolation method to optimize linear-ramp quantum approximate optimization
  algorithm parameters: Evaluation of runtime scaling'
topic_tags:
- portfolio-optimisation
year: 2026
zotero_key: ''
---

## Abstract summary
The paper proposes an extrapolation-based method to set the parameters of the linear-ramp variant of QAOA without full variational optimization, by learning parameter trends on small subproblems and extrapolating them to larger instances. The authors apply this approach to portfolio optimization, feature selection, clustering, and weighted MaxCut, and compare quantum runtime scaling (via total circuit depth needed to reach the optimum on a noiseless emulator) against several classical solvers. They find indications of a scaling advantage for portfolio optimization, while for the other problems the quantum scaling is comparable to or worse than that of a strong classical heuristic.
## Methodology
The paper presents a peer-reviewed empirical study evaluating an extrapolation-based parameter-setting method for linear-ramp QAOA (LR-QAOA) on combinatorial optimization problems, including portfolio optimization, feature selection, clustering, and weighted MaxCut. Each problem is formulated as a QUBO and solved classically and quantumly to compare runtime scaling. The quantum method replaces standard variational QAOA optimization with a fixed linear-ramp schedule parameterized by only three variables: Δγ, Δβ, and circuit depth p. For each original instance of size N (typically 12 to 28 qubits for quantum experiments), the authors generate random subinstances of smaller sizes Ñ = 4, 6, 8, 10, perform grid search over log-scaled Δγ and Δβ values at a chosen depth p, fit the resulting success-probability landscape with a multivariate skew Gaussian, and extrapolate the fitted optimal parameters and success probability to the larger instance using linear fits on a log-log scale. They then optimize p by minimizing total quantum depth D = d × Nshots, where d is circuit depth and Nshots is the median number of repetitions needed to observe the optimal solution based on the measured optimal-solution probability Popt. Experiments are run on a noiseless quantum emulator rather than real hardware. Performance is assessed via runtime scaling exponents from exponential fits of total depth versus problem size and compared against classical baselines including CPLEX, GUROBI, MQLib/Burer2002, and Goemans-Williamson, with MQLib/Burer2002 used as the main benchmark for quantum comparison. For portfolio optimization, the study reports better scaling for LR-QAOA than the chosen classical heuristic up to 28 qubits; for the other tasks, quantum scaling is similar or worse unless universal parameter scaling is used, which improves robustness.

**Algorithms used:** QAOA, linear-ramp QAOA, Goemans-Williamson, MQLib/Burer2002
**Frameworks:** Qiskit, CPLEX, GUROBI, MQLib, scikit-learn

**Experimental setup:** Quantum experiments were performed on a noiseless quantum emulator/simulator, not on real QPU hardware. The study evaluates LR-QAOA circuits for problem sizes up to 28 qubits. Classical baselines were run using CPLEX, GUROBI, MQLib/Burer2002, and Goemans-Williamson. Quantum runtime was quantified as total circuit depth D = d × Nshots, where d is proportional to QAOA depth p and Nshots is the median number of circuit repetitions required to find the optimal solution. Parameter search used 11×11 grids over log10(Δγ) and log10(Δβ) for subinstances, with subproblem sizes 4, 6, 8, and 10 qubits. Additional validation included direct minimization from extrapolated initial points and a universal parameter-scaling variant.

**Dataset:** Portfolio optimization used annualized returns and covariance matrices from the German DAX 30 (as of 1/2/2021) over 01/01/2016 to 31/12/2020, with random subsets of assets forming instances. Feature selection used the UCI German Credit Data dataset with 20 original features (7 numerical, 13 categorical) and 1000 instances, transformed via one-hot encoding to up to 48 binary features. Clustering used the scikit-learn Moons and Blobs synthetic datasets with 2 features. Weighted MaxCut used fully connected graphs with edge weights drawn uniformly from 0 to 1000 in integer steps.
## Findings
- [supported] The paper proposes an extrapolation-based method to set linear-ramp QAOA parameters from small subproblems (4, 6, 8, 10 qubits) and applies it to portfolio optimization, feature selection, clustering, and weighted MaxCut on a noiseless quantum emulator.
- [supported] For portfolio optimization, the estimated quantum runtime scaling was D ∝ 2^0.219N, compared with the chosen classical benchmark MQLib/Burer2002 scaling of about 2^0.323N, indicating better scaling for the quantum method over the tested range up to 28 qubits.
- [supported] For feature selection, the quantum runtime scaling was about D ∝ 2^0.378N, worse than the classical benchmark scaling of about 2^0.197N.
- [supported] For clustering (Moons), the quantum runtime scaling was about D ∝ 2^0.248N, worse than the classical benchmark scaling of about 2^0.051N.
- [supported] For weighted MaxCut, the quantum runtime scaling was about D ∝ 2^0.235N using instance-specific extrapolated parameters, worse than the classical benchmark scaling of about 2^0.156N.
- [supported] Using universal algebraic parameter scaling across instances improved LR-QAOA stability and removed strong outliers for feature selection, clustering, and MaxCut.
- [supported] With universal parameter scaling, feature selection and weighted MaxCut achieved quantum scaling coefficients close to the classical benchmark, while clustering remained worse than classical.
- [supported] With universal parameter scaling, portfolio optimization retained a favorable quantum scaling coefficient of about 0.215 versus the classical 0.323 benchmark.
- [supported] The extrapolated LR-QAOA parameters were empirically close to directly optimized parameters for tested instances, suggesting the extrapolation scheme is effective for parameter initialization.
- [supported] The study's quantum results are entirely based on noiseless simulation/emulation rather than real quantum hardware.
- [speculative] The authors interpret the portfolio optimization result as an indication of quantum scaling advantage, but not a definitive proof of quantum advantage.
- [speculative] The authors suggest that if the observed near-constant success probability and algebraically growing circuit depth persist for larger N, polynomial median quantum runtime could be possible for some problem ensembles.
- [speculative] The paper argues that extrapolation and universal parameter scaling may be promising tools for making LR-QAOA scalable beyond variational optimization bottlenecks.

**Results summary:** This peer-reviewed empirical study evaluates an extrapolation method for setting linear-ramp QAOA parameters and measures runtime scaling on four combinatorial optimization tasks, including portfolio optimization relevant to finance. All quantum results were obtained on a noiseless quantum emulator, with problem sizes up to 28 qubits. Runtime was measured as total circuit depth needed to find the optimal solution, and compared against classical solvers, with MQLib/Burer2002 used as the main benchmark. For portfolio optimization, the authors report quantum scaling D ∝ 2^0.219N using instance-specific extrapolated parameters and about 2^0.215N using universal parameter scaling, versus classical scaling about 2^0.323N, which they present as evidence of superior scaling over the tested range. For feature selection, clustering, and weighted MaxCut, the initial quantum scaling was worse than classical, though universal parameter scaling improved results substantially, bringing feature selection and MaxCut close to classical scaling while clustering remained worse. The paper does not demonstrate quantum advantage on hardware and frames the portfolio result as an indication rather than proof of advantage.

**Performance claims:**
- Portfolio optimization: quantum runtime scaling D ∝ 2^0.219N versus classical MQLib/Burer2002 scaling ≈ 2^0.323N (instance-specific extrapolated parameters)
- Portfolio optimization with universal parameters: quantum scaling ≈ 2^0.215N versus classical ≈ 2^0.323N
- Feature selection: quantum scaling ≈ 2^0.378N versus classical ≈ 2^0.197N
- Clustering (Moons): quantum scaling ≈ 2^0.248N versus classical ≈ 2^0.051N
- Weighted MaxCut: quantum scaling ≈ 2^0.235N versus classical ≈ 2^0.156N
- Weighted MaxCut on selected classically hard instances: quantum scaling coefficient α ≈ 0.103 with the paper's universal parameters, versus α ≈ 0.100 using parameters from prior work
- Classical optimality verification with CPLEX found only small numbers of instances without proof of global optimality: portfolio 1/270, feature selection 18/940, clustering (Moons) 2/1980, clustering (Blobs) 4/1980, MaxCut 0/190
- For all classical verification cases, the relative gap between best-found solution and lower bound was < 10^-6
- The extrapolation method used subproblems of sizes 4, 6, 8, and 10 qubits to predict parameters for problems up to 28 qubits
- For the universal-parameter experiments, average single-run success probabilities Popt remained above 0.1 across all four problem classes
## Quantum advantage claim
**Classification:** speculative

The paper reports better empirical scaling than a selected classical benchmark for portfolio optimization up to 28 qubits, but all quantum results are from noiseless emulation rather than real hardware, and the authors describe the result as an indication rather than proof of quantum advantage.
## Limitations
- Experiments are performed on a noiseless quantum emulator rather than real quantum hardware, so decoherence, gate errors, connectivity constraints, and measurement noise are not assessed.
- Problem sizes are limited to at most 28 qubits, which restricts conclusions about asymptotic scaling and practical large-scale applicability.
- The benchmark problems are explicitly described by the authors as simplified compared with real-world business and industry problems.
- For portfolio optimization, the formulation uses simplifying assumptions such as historic return as expected return, covariance as risk measure, binary portfolio fractions, fixed budget, and omission of subtleties like short-selling, integer asset fractions, transaction costs, and sophisticated risk measures.
- The extrapolation method is based on optimizations over very small subproblems (Ñ = 4, 6, 8, 10), which may not fully capture structure present in larger instances.
- The authors state that they do not currently have a theoretical justification for the assumed algebraic scaling used in the extrapolation procedure.
- The clustering case shows instability of the extrapolation scheme, with some strong outliers and failures to provide good circuit parameters for certain instances.
- Runtime is quantified via total circuit depth rather than wall-clock execution on hardware, so hardware-specific overheads and scheduling effects are abstracted away.
- The comparison focuses on the MQLib/Burer2002 heuristic as the classical benchmark, while other classical methods are excluded from the final comparison for methodological reasons.
- The study concentrates on median runtime and does not analyze other percentiles or full runtime distributions.
- Although most classical reference solutions are likely optimal, for a small number of instances global optimality was not formally proven.
- [inferred] The claimed scaling advantage for portfolio optimization is only an indication based on fitted trends over a narrow size range, not definitive evidence of quantum advantage.
- [inferred] Results may be sensitive to instance selection, as shown by the dependence of scaling behavior on dataset choice and on selecting classically hard MaxCut instances.
- [inferred] The use of annualized returns and covariance matrices from a specific DAX 30 time window limits external validity for broader financial markets and regimes.
- [inferred] The study does not evaluate reproducibility of performance across different simulators, hardware backends, compiler settings, or random seeds beyond sampled instances.
- [inferred] No direct comparison is made against state-of-the-art finance-specific classical portfolio optimization pipelines used in production settings.
- [inferred] Scalability to production financial services is unclear because the tested portfolio instances are small, stylized, and omit operational constraints common in practice.
- [inferred] The optimization cost for finding QAOA parameters is largely separated from the reported runtime objective, which may understate end-to-end deployment cost.
## Open questions
- Whether and under what conditions QAOA or linear-ramp QAOA can offer an advantage over classical algorithms remains unresolved.
- How suitable values of the linear-ramp parameters and depth can be found in an efficient and scalable way for large problem sizes.
- Whether the observed nondecreasing success probability for portfolio optimization and MaxCut persists for larger N beyond 28.
- Whether quantum optimization can achieve polynomial-time solutions for some combinatorial optimization instances that classically require exponential time.
- How the runtime scaling behaves for larger problem sizes beyond those accessible in this study.
- What structural properties of combinatorial optimization problems determine hardness for classical versus quantum methods.
- How robust the universal parameter scaling is across broader instance distributions and more realistic financial datasets.
- How the method performs on real, fault-tolerant or noisy quantum hardware rather than in noiseless simulation.
- How sensitive the reported scaling results are to the choice of classical benchmark and to instance-selection procedures.

**Future work:**
- Extend the analysis to a larger range of problem sizes beyond N = 28.
- Use high-performance classical simulation and advanced simulation techniques to study larger circuits.
- Test the approach on real fault-tolerant quantum hardware with roughly 50 to 100+ qubits.
- Perform more elaborate statistical analyses beyond the median runtime, including scaling of different percentiles.
- Develop improved methods for extrapolation and scaling of circuit parameters with increasing problem size.
- Investigate more deeply the structural features of combinatorial optimization problems that govern classical and quantum hardness.
- Explore whether runtime scalings from related QAOA approaches can be improved by combining them with the adaptive-depth and extrapolation ideas introduced here.
- [inferred] Incorporate realistic hardware noise, error mitigation, and device constraints into the evaluation.
- [inferred] Validate the approach on more realistic financial portfolio models including transaction costs, richer constraints, and alternative risk measures.
- [inferred] Assess end-to-end runtime including parameter-finding overhead to determine practical production viability.
## Key ideas
- #idea:quantum-advantage — Extrapolated linear-ramp QAOA shows better empirical scaling than the selected classical benchmark for portfolio optimisation up to 28 qubits in noiseless simulation (about 2^0.219N vs 2^0.323N).
- #idea:near-term-feasibility — Learning QAOA parameter trends from 4–10 qubit subproblems avoids full variational optimisation on each larger instance and is presented as a practical NISQ-oriented parameter-setting strategy.
- #idea:hybrid-approach — The method is explicitly quantum-classical: classical subproblem fitting, extrapolation, and depth selection are used to configure LR-QAOA circuits for larger QUBO instances.
- #idea:near-term-feasibility — Universal parameter scaling improves robustness and reduces outliers across problem classes, suggesting a more stable route than instance-by-instance optimisation.
- #idea:quantum-advantage — The paper frames the portfolio result as an indication of possible quantum scaling advantage rather than definitive proof, with stronger results in finance than in the non-financial benchmark tasks.
## Contradictions
- The paper suggests a quantum scaling advantage for portfolio optimisation, but this is weakened by the fact that all evidence comes from noiseless simulation and a selected classical benchmark rather than real hardware or broader state-of-the-art classical finance baselines; this conflicts with stronger claims of quantum superiority.
- The paper's positive portfolio result contrasts with its own findings on feature selection, clustering, and MaxCut, where LR-QAOA is comparable to or worse than classical methods, indicating that any advantage is highly problem-dependent rather than general.
- Claims about scalability are contradicted by the limited evaluation range (up to 28 qubits), instability on some instances, and the absence of theoretical justification for the extrapolation law; related skepticism is noted against broader quantum-advantage claims such as in 2022_Herman_QuantumAdvantageLimits.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->

## Experiment details
### Input
Portfolio optimization: annualized returns and covariance matrices for DAX 30 assets from 2016-01-01 to 2020-12-31; instances created by randomly selecting N assets from 30 total; risk preference q = 1 for the reported scaling study; budget B = N/2 for even N or (N-1)/2 for odd N; penalty term A chosen using a routine from prior work. Feature selection: German Credit Data with 1000 samples, 20 original features (7 numerical, 13 categorical), binary target with 700 nondefault and 300 default cases; categorical variables one-hot encoded to yield up to 48 binary features; weighting parameter φ = 0.9. Clustering: scikit-learn Moons and Blobs datasets in R^2, each data point mapped to one binary decision variable. MaxCut: fully connected weighted graphs with edge weights sampled uniformly from {0,1,...,1000}. For quantum experiments, original instances had N from 12 to 28 qubits, and random subinstances of sizes 4, 6, 8, and 10 were generated for extrapolation.

### Process
1. Formulate each task as a QUBO. 2. For each original instance of size N, generate 10 random subinstances for each reduced size Ñ in {4, 6, 8, 10}. 3. For Ñ = 4, perform an 11×11 grid search over log10(Δγ) and log10(Δβ) at initial depth p0 = 6; compute the probability Popt of measuring the optimal solution for each subinstance and average over the 10 subinstances. 4. Fit the resulting 2D probability landscape with a multivariate skew Gaussian to estimate the center, widths, and maximum probability. 5. Recenter and shrink the search grid for the next subproblem size using the fitted optimum and covariance widths; repeat until Ñ = 10. 6. Extrapolate log10(Δγ,opt), log10(Δβ,opt), and log10(Popt,max) from Ñ = 4, 6, 8, 10 to the full problem size N using linear fits on a log-log scale. 7. Search over a logarithmically spaced set of QAOA depths p, starting from the previous optimal p or p0 = 6, and choose the p minimizing estimated total depth D = d × Nshots, with Nshots = log(1/2)/log(1 - Popt). 8. Evaluate the LR-QAOA circuit on the full instance using the extrapolated parameters and compute actual Popt and total depth D. 9. Fit exponential scaling models D ∝ 2^(αN) across problem sizes. 10. Compare against classical runtimes from CPLEX, GUROBI, MQLib/Burer2002, and Goemans-Williamson. 11. In a second variant, derive universal algebraic parameter scalings Δγ(N), Δβ(N), and p(N) from weighted averages across instances and re-evaluate all instances, including additional random instances for robustness.

### Output
Primary outputs are the optimal-solution probability Popt for LR-QAOA, total quantum depth D as a proxy for runtime, and exponential scaling coefficients α from fits of D ∝ 2^(αN). The study also reports optimized/extrapolated LR-QAOA parameters (Δγ, Δβ, p), geometric means of D across instances, and comparisons to direct parameter minimization. Classical outputs are wall-clock runtimes and scaling exponents for CPLEX, GUROBI, MQLib/Burer2002, and Goemans-Williamson, with optimality checks from CPLEX where available. For portfolio optimization, the reported quantum scaling exponent is about 0.219 versus classical MQLib/Burer2002 at about 0.323, indicating superior scaling up to 28 qubits; for feature selection, clustering, and MaxCut, quantum scaling is initially worse, though universal parameter scaling improves feature selection and MaxCut to near classical parity.

### Parameters
- qubits: {'subproblem_sizes': [4, 6, 8, 10], 'full_problem_sizes_quantum': '12 to 28'}
- qaoa_schedule: linear-ramp
- qaoa_parameters: ['Δγ', 'Δβ', 'p']
- initial_depth_p0: 6
- grid_search_size: 11x11
- grid_variables: ['log10(Δγ)', 'log10(Δβ)']
- subinstances_per_subproblem_size: 10
- portfolio_instances_per_N: 10
- feature_selection_instances_per_N: 10
- clustering_instances_per_N: 10
- maxcut_instances_per_N: 10
- portfolio_budget: B = N/2 for even N, (N-1)/2 for odd N
- portfolio_risk_preference_q: 1
- feature_selection_phi: 0.9
- shots_formula: Nshots = log(1/2) / log(1 - Popt)
- classical_repetitions: {'portfolio': 20, 'feature_selection': 10, 'clustering_moons': 10, 'clustering_blobs': 10, 'maxcut': 20}
- classical_instance_counts: {'portfolio': 10, 'feature_selection': 20, 'clustering_moons': 20, 'clustering_blobs': 20, 'maxcut': 10}
- classical_N_ranges: {'portfolio': '2 to 28', 'feature_selection': '2 to 48', 'clustering_moons': '2 to 100', 'clustering_blobs': '2 to 100', 'maxcut': '11 to 29'}

### Hardware
Noiseless quantum emulator/simulator; no real QPU used. The paper does not specify a simulator backend name, cloud provider, noise model, transpilation settings, or gate-level hardware configuration. Classical solvers included CPLEX, GUROBI, MQLib/Burer2002, and Goemans-Williamson; Qiskit is mentioned as providing access to several classical optimization methods.

### Reproducibility
Data availability is explicitly stated: the supporting dataset is openly available on Zenodo. The paper provides substantial methodological detail on QUBO formulations, parameter search, extrapolation, and evaluation, making conceptual replication feasible. However, no code repository is explicitly provided in the excerpt, and some implementation details of the emulator/backend and optimization routines are not fully specified, so exact reproduction may require additional reconstruction.
