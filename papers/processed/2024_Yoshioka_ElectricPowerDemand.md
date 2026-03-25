---
aliases:
- Electric Power Demand Portfolio Optimization by Fermionic QAOA with Self-Consistent
  Local Field Modulation
- Electric Power Demand Portfolio
authors:
- Takuya Yoshioka
- Keita Sasada
- Yuichiro Nakano
- Keisuke Fujii
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
journal_or_venue: arXiv
methodology_tags:
- QAOA
- variational
- classical-simulation
paper_type: ''
quantum_advantage_claim: speculative
related_papers: []
relevance_phase1: medium
relevance_phase3: medium
source_type: preprint
source_type_confidence: high
step1_date: '2026-03-25T16:05:52.047954'
step1_model: gpt-5.1
step2_date: '2026-03-25T16:05:58.461375'
step2_model: gpt-5.1
step3_date: '2026-03-25T16:06:38.728145'
step3_model: gpt-5.4
step4_date: '2026-03-25T16:07:17.077182'
step4_model: gpt-5.4
step5_date: '2026-03-25T16:07:40.948814'
step5_model: gpt-5.4
step6_date: '2026-03-25T16:07:50.853877'
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
- method/variational
- method/classical-simulation
- idea/quantum-advantage
- idea/near-term-feasibility
- idea/hybrid-approach
- contradiction/scalability
- contradiction/classical-vs-quantum
title: Electric Power Demand Portfolio Optimization by Fermionic QAOA with Self-Consistent
  Local Field Modulation
topic_tags:
- portfolio-optimisation
- risk-modelling
year: 2025
zotero_key: ''
---

## Abstract summary
The paper introduces FQAOA-SCLFM, an improved fermionic QAOA variant tailored to electric power demand portfolio optimization, where an aggregator aims to procure a target amount of negawatt with minimal risk. The authors reformulate the variance-based portfolio problem with a quadratic penalty on deviations from the target power and embed this soft constraint into a Hartree–Fock-type driver Hamiltonian with self-consistent local field modulation. Using noiseless simulations on small residential demand data, they compare FQAOA-SCLFM against XY-QAOA and the original FQAOA, showing consistently better cost performance and more stable satisfaction of the power procurement constraint across time periods.
## Methodology
This preprint presents an empirical simulation study of a new constrained quantum optimization method, FQAOA-SCLFM, for electric power demand portfolio optimization in negawatt trading. The authors formulate the task as a binary portfolio selection problem over demand-response participants, minimizing a cost that combines a risk term based on negawatt covariance and a soft penalty term enforcing procurement close to a target power level, under a hard cardinality constraint on the number of selected participants. They map the problem to a fermionic cost Hamiltonian with particle-number conservation and propose a modified fermionic QAOA ansatz in which the driver Hamiltonian includes self-consistent local field modulation derived from a Hartree-Fock approximation. The Hartree-Fock driver is solved iteratively to obtain a self-consistent initial state and local fields, after which variational parameters of the QAOA circuit are optimized classically using BFGS. The method is evaluated in noiseless simulation and compared against XY-QAOA and the authors' prior FQAOA across multiple time-period instances. Performance is assessed through expected total negawatt, variance of total negawatt, probability distributions over portfolio costs, and normalized expected excess cost relative to the optimal solution.

**Algorithms used:** QAOA, FQAOA, FQAOA-SCLFM, XY-QAOA, Hartree-Fock, BFGS
**Frameworks:** Qulacs

**Experimental setup:** All experiments were conducted as noiseless numerical simulations using the Qulacs quantum circuit simulator. The study evaluates the proposed FQAOA-SCLFM against XY-QAOA and prior FQAOA on electric power demand portfolio optimization instances with 20 demand-response participants. Simulations were run for multiple time periods T = 0, 3, 6, 9, 12, 15, 18, 21, with each period including three reference times. Results are reported for QAOA depths p = 0, 1, and 10, with additional depth sweeps shown for expected cost. No real QPU or noise model was used.

**Dataset:** Historical residential electricity usage data from a public database, following prior work, was used to estimate expected negawatt supply and covariance among 20 residences. Specifically, electricity usage from 20 residences during September 1-15, 2003 was treated as the amount of negawatt each participant could supply, with water-heater usage excluded to remove singular midnight peaks.
## Experiment details
### Input
Input data consisted of residential electricity usage records from 20 residences obtained from the Niigata University residential energy consumption database, using data from September 1-15, 2003. The authors estimated expected negawatt E[pt,l] and covariance terms sigma_t,l,l' for each participant and time point following the procedure of Ref. [8]. The optimization instances were defined over L = 20 participants, with time periods T = 3i for i = 0,...,7, each containing three times t = T, T+1, T+2. Fixed problem settings included target procurement midpoint P'_{t,proc} = 1.5 kWh, corresponding to P_{t,proc} = 1 kWh and delta = 1 kWh in one passage and delta = 11 kWh in another passage of the text, and a cardinality constraint M_T = 5 selected participants. Water-heater loads were removed as preprocessing.

### Process
1. Formulate the electric power demand portfolio optimization problem as a constrained binary optimization minimizing average cost over a 3-time-step period, where cost combines covariance-based risk and a quadratic penalty for deviation from target procurement. 2. Map the binary variables to a fermionic Hamiltonian with number operators and impose the hard constraint as fixed particle number M_T = 5. 3. Construct the proposed FQAOA-SCLFM ansatz using alternating applications of the cost Hamiltonian and a Hartree-Fock-based driver Hamiltonian. 4. Compute the Hartree-Fock driver self-consistently: initialize the fermion distribution uniformly as n_l,0 = 1/M_T, iteratively solve for the Hartree-Fock ground state, update occupations using linear mixing n_{l,i+1} = (1-alpha)n_{l,i} + alpha n^{out}_{l,i+1}, and continue until stabilization; Appendix A studies alpha values and notes stable convergence for alpha <= 0.6. 5. Use the converged Hartree-Fock quantities to define the local field terms in the driver and prepare the initial state. 6. Optimize QAOA variational parameters (gamma, beta) by minimizing the expectation value of the cost Hamiltonian with the BFGS classical optimizer. 7. Evaluate the optimized state by computing the probability of each bitstring, expected total negawatt, variance of total negawatt, cost distribution D_T(E), and normalized expected excess cost Delta E_T / W_T. 8. Repeat the procedure for QAOA levels p = 0, 1, and 10 and compare against XY-QAOA and prior FQAOA under the same instances.

### Output
Reported outputs include expected total negawatt P_{t,tot}, total negawatt variance sigma^2_{t,tot}, probability distributions over portfolio cost D_T(E), and normalized expected excess cost Delta E_T / W_T relative to the minimum cost for each time period. The main baselines are XY-QAOA and the authors' previous FQAOA. Results are presented across time periods T = 0, 3, 6, 9, 12, 15, 18, 21 and QAOA levels p = 0, 1, 10, with tables and plots showing that FQAOA-SCLFM achieves lower expected cost and more stable procurement than both baselines in all studied instances.

### Parameters
- participants: 20
- time_periods: [0, 3, 6, 9, 12, 15, 18, 21]
- times_per_period: 3
- selected_participants_constraint: 5
- qaoa_levels_evaluated: [0, 1, 10]
- optimizer: BFGS
- simulator: Qulacs
- environment: noiseless simulation
- target_procurement_midpoint_kWh: 1.5
- target_procurement_kWh: 1.0
- hartree_fock_initial_distribution: uniform, n_l,0 = 1/M_T
- hartree_fock_mixing_parameter_alpha: varied; stable for alpha <= 0.6
- qubits: 20

### Hardware
{'hardware_type': 'simulator', 'simulator_name': 'Qulacs', 'noise_model': 'none', 'qpu_used': False}

### Reproducibility
Preprint empirical study. The data source is public and the paper provides the mathematical formulation, dataset provenance, problem size, baselines, optimizer, and key parameter settings. However, no code repository, exact implementation details for all optimization settings, stopping criteria for BFGS/HF convergence, or full hyperparameter configuration are provided, so replication appears partially feasible but not fully turnkey.
## Findings
- [supported] The paper proposes FQAOA-SCLFM, a variant of fermionic QAOA that incorporates a soft procurement-balance penalty into the driver Hamiltonian via self-consistent local field modulation based on a Hartree-Fock approximation.
- [supported] In noiseless simulation on a 20-participant electric power demand portfolio optimization problem with a fixed-cardinality constraint (M_T = 5), FQAOA-SCLFM achieved lower expected normalized cost than both XY-QAOA and prior FQAOA for every studied time period and QAOA depth reported.
- [supported] At QAOA depth p = 10, FQAOA-SCLFM produced the lowest normalized expected cost in all eight time periods T = 0, 3, 6, 9, 12, 15, 18, 21, with values 0.018, 0.027, 0.017, 0.036, 0.019, 0.012, 0.007, and 0.007 respectively.
- [supported] The largest relative gains of FQAOA-SCLFM over prior FQAOA occur in the harder evening periods, especially T = 18 and T = 21, where normalized expected cost at p = 10 drops from 0.030 to 0.007 in both cases.
- [supported] FQAOA-SCLFM yields a better initial state than prior FQAOA because its Hartree-Fock driver already biases the solution toward the target procurement level at p = 0, particularly in difficult periods such as T = 18.
- [supported] Simulation plots indicate that as p increases, the expected total negawatt approaches the target-adjusted procurement level P'_{t,proc} and the variance decreases, with the paper stating that by p = 10 the balance condition is roughly satisfied and procurement becomes more stable.
- [supported] The cost distribution at T = 18 and p = 1 is more concentrated near the minimum-energy region for FQAOA-SCLFM than for XY-QAOA or prior FQAOA, indicating improved solution quality in simulation.
- [supported] The additional circuit overhead of FQAOA-SCLFM relative to prior FQAOA is stated to be only pL extra single-qubit Z-rotation-type operations from the local-field unitary term.
- [supported] Hartree-Fock self-consistent iteration is numerically stable for mixing parameters alpha <= 0.6, while alpha = 0.8 shows faster energy decrease but oscillatory behavior in the reported example at T = 18.
- [speculative] The authors argue that the proposed algorithm should be applicable beyond this use case to other combinatorial optimization problems that combine hard and soft constraints in a form similar to their cost function.
- [speculative] The paper suggests quantum computation has potential to efficiently solve such constrained combinatorial optimization problems in power systems, but this is not demonstrated against classical state-of-the-art solvers in the study.

**Results summary:** This preprint introduces FQAOA-SCLFM, a fermionic QAOA variant for electric power demand portfolio optimization in negawatt trading. The method embeds a soft target-procurement penalty into a Hartree-Fock-based driver Hamiltonian through self-consistent local field modulation. Using noiseless simulations in Qulacs on a 20-participant problem derived from residential electricity-use data, the authors compare XY-QAOA, prior FQAOA, and FQAOA-SCLFM across eight 3-hour time periods and depths p = 0, 1, and 10. FQAOA-SCLFM consistently achieves the lowest normalized expected cost in every tested instance, with especially strong improvements in harder evening periods such as T = 18 and T = 21. The simulations also show that increasing p moves the expected total negawatt closer to the target procurement level while reducing variance. However, all evidence is from noiseless simulation rather than real quantum hardware, and no classical baseline demonstrating quantum advantage is provided.

**Performance claims:**
- Normalized expected cost DeltaE_T/W_T for FQAOA-SCLFM at p = 10: T=0 0.018, T=3 0.027, T=6 0.017, T=9 0.036, T=12 0.019, T=15 0.012, T=18 0.007, T=21 0.007
- Normalized expected cost DeltaE_T/W_T for prior FQAOA at p = 10: T=0 0.026, T=3 0.029, T=6 0.018, T=9 0.037, T=12 0.023, T=15 0.015, T=18 0.030, T=21 0.030
- Normalized expected cost DeltaE_T/W_T for XY-QAOA at p = 10: T=0 0.033, T=3 0.037, T=6 0.024, T=9 0.053, T=12 0.033, T=15 0.021, T=18 0.052, T=21 0.056
- At p = 1, normalized expected cost DeltaE_T/W_T for FQAOA-SCLFM: T=0 0.046, T=3 0.076, T=6 0.039, T=9 0.116, T=12 0.058, T=15 0.032, T=18 0.014, T=21 0.018
- At p = 1, normalized expected cost DeltaE_T/W_T for prior FQAOA: T=0 0.066, T=3 0.082, T=6 0.056, T=9 0.123, T=12 0.076, T=15 0.051, T=18 0.096, T=21 0.121
- At p = 1, normalized expected cost DeltaE_T/W_T for XY-QAOA: T=0 0.073, T=3 0.082, T=6 0.060, T=9 0.129, T=12 0.088, T=15 0.058, T=18 0.115, T=21 0.142
- At p = 0, normalized expected cost DeltaE_T/W_T for FQAOA-SCLFM: T=0 0.074, T=3 0.107, T=6 0.061, T=9 0.197, T=12 0.107, T=15 0.056, T=18 0.025, T=21 0.032
- At p = 0, normalized expected cost DeltaE_T/W_T for prior FQAOA: T=0 0.168, T=3 0.123, T=6 0.162, T=9 0.222, T=12 0.177, T=15 0.156, T=18 0.275, T=21 0.305
- At p = 0, normalized expected cost DeltaE_T/W_T for XY-QAOA: T=0 0.165, T=3 0.117, T=6 0.162, T=9 0.220, T=12 0.177, T=15 0.155, T=18 0.276, T=21 0.307
- Problem setup uses 20 DR participants, time windows of length 3 hours, target-adjusted procurement P'_{t,proc} = 1.5 kWh, and cardinality constraint M_T = 5
- The paper states FQAOA-SCLFM adds only pL extra gate operations relative to prior FQAOA
## Quantum advantage claim
**Classification:** speculative

This is a preprint with results based entirely on noiseless simulation, not real hardware, and it does not show superiority over classical optimization methods. The paper demonstrates improvement over other quantum heuristics (XY-QAOA and prior FQAOA), but any broader quantum advantage claim remains speculative.
## Limitations
- The study reports only noiseless simulation results and does not evaluate performance on real quantum hardware or under realistic noise models.
- The optimization problem is tested on a small-scale instance with 20 DR participants and fixed settings (e.g., MT = 5), limiting evidence for scalability.
- The proposed alternative cost function replaces the original inequality constraint with a penalty term and explicitly allows violation of the original balance condition.
- The Hartree-Fock driver Hamiltonian relies on an approximation of the soft-constraint term, so solution quality depends on the accuracy of the self-consistent mean-field approximation.
- The forecasting model is based on historical electricity usage from 20 residences over a limited period, which may not represent broader or current demand-response markets.
- The experiments consider only a narrow set of time windows and parameter choices, so robustness across different procurement targets, penalty settings, and market conditions is not established.
- Classical optimization of variational parameters uses BFGS, but sensitivity to initialization, local minima, and optimizer choice is not systematically analyzed.
- [inferred] As a preprint, the work has not yet undergone peer review.
- [inferred] No comparison is provided against strong classical optimization baselines, so practical quantum advantage is not demonstrated.
- [inferred] The claim that the method is suitable within current hardware limitations is not backed by hardware experiments, resource estimates at scale, or error-mitigation studies.
- [inferred] Reproducibility may be limited because the paper does not provide full implementation details such as code, random seeds, or complete hyperparameter settings for all experiments.
- [inferred] The study focuses on average expected cost and sampled distributions but does not quantify runtime, sample complexity, or end-to-end computational overhead versus classical methods.
- [inferred] The self-consistent HF iteration may introduce convergence and stability issues, as oscillations are shown for larger mixing parameters.
## Open questions
- How well does FQAOA-SCLFM perform on noisy intermediate-scale quantum hardware compared with noiseless simulation?
- How does the method scale as the number of DR participants, time periods, and constraint complexity increase?
- To what extent does the Hartree-Fock approximation affect final optimization quality relative to the exact driver with the full soft-constraint term?
- How sensitive is performance to the choice of penalty formulation, procurement target P't,proc, and the number of requested participants MT?
- Can the method maintain its advantage over XY-QAOA and prior FQAOA when benchmarked against state-of-the-art classical solvers for portfolio optimization?
- What is the circuit depth, shot requirement, and optimization cost needed for useful performance on real devices?
- How robust is the approach when applied to more realistic demand-response data with nonstationarity, forecasting errors, and larger participant heterogeneity?
- Does the observed improvement persist for other combinatorial optimization problems with both hard and soft constraints, beyond the specific electricity-demand setting studied?

**Future work:**
- Evaluate FQAOA-SCLFM on actual QPU experiments and under realistic noise conditions.
- Test the method on larger-scale electricity demand portfolio optimization instances with more participants and more complex market settings.
- Investigate improved self-consistent or beyond-Hartree-Fock driver constructions to better capture the soft-constraint term.
- Benchmark against stronger classical optimization methods and hybrid classical-quantum baselines.
- Study parameter-optimization strategies, initialization schemes, and convergence behavior for deeper QAOA levels.
- Extend the approach to other combinatorial optimization problems of the same form involving both hard and soft constraints.
- Analyze hardware resource requirements, gate counts, and error-mitigation techniques needed for practical deployment.
- Use more realistic and diverse datasets, including updated market data and broader demand-response scenarios, to validate generalizability.
## Key ideas
- #idea:hybrid-approach — Proposes FQAOA-SCLFM, combining a fermionic QAOA ansatz with a classically computed Hartree-Fock self-consistent driver and classical BFGS parameter optimization.
- #idea:near-term-feasibility — Embeds the soft procurement constraint into the driver with only pL additional single-qubit local-field operations, positioning the method as compatible with shallow variational circuits.
- #idea:quantum-advantage — In noiseless simulation, FQAOA-SCLFM consistently outperforms XY-QAOA and prior FQAOA on 20-participant negawatt portfolio instances in normalized expected cost and procurement stability.
- #idea:near-term-feasibility — Reformulates the procurement problem using a quadratic penalty and fixed-cardinality particle-number constraint to make constrained portfolio optimization more amenable to QAOA-style treatment.
- #idea:hybrid-approach — Uses Hartree-Fock mean-field information to bias the initial state toward target procurement, improving p=0 and shallow-depth behavior relative to prior fermionic QAOA.
## Contradictions
- The paper suggests practical promise and broader applicability of FQAOA-SCLFM, but this is contradicted by the evidence base: all results are from noiseless classical simulation on only 20 participants, with no hardware validation and no scaling study (#contradiction:scalability).
- The paper implies potential quantum advantage through superiority over XY-QAOA and prior FQAOA, but it provides no comparison against strong classical optimization baselines, so claims of quantum superiority over classical methods are unsupported (#contradiction:classical-vs-quantum).
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
