---
aliases:
- Portfolio Optimization with Digitized-Counterdiabatic Quantum Algorithms
- Portfolio Optimization Digitized Counterdiabatic
authors:
- N. N. Hegade
- P. Chandarana
- K. Paul
- X. Chen
- F. Albarrán-Arriagada
- E. Solano
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
step1_date: '2026-03-25T15:54:01.510234'
step1_model: gpt-5.1
step2_date: '2026-03-25T15:54:05.581152'
step2_model: gpt-5.1
step3_date: '2026-03-25T15:54:53.339530'
step3_model: gpt-5.4
step4_date: '2026-03-25T15:55:21.472296'
step4_model: gpt-5.4
step5_date: '2026-03-25T15:55:48.112692'
step5_model: gpt-5.4
step6_date: '2026-03-25T15:55:59.380282'
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
- contradiction/scalability
- contradiction/classical-vs-quantum
title: Portfolio Optimization with Digitized-Counterdiabatic Quantum Algorithms
topic_tags:
- portfolio-optimisation
year: 2021
zotero_key: ''
---

## Abstract summary
The paper applies digitized-counterdiabatic quantum computing techniques to a discrete mean-variance Markowitz portfolio optimization problem, encoding it into an Ising Hamiltonian and studying ground-state preparation under NISQ constraints. The authors derive and implement local and approximate counterdiabatic terms to enhance finite-time adiabatic evolutions and compare performance across many randomly generated portfolio instances. They also extend the approach to a digitized-counterdiabatic variant of QAOA (DC-QAOA), showing improved success probabilities over standard QAOA for small portfolio instances.
## Methodology
This preprint presents an empirical quantum-algorithm study of discrete mean-variance portfolio optimization framed as an unconstrained Markowitz problem. The authors encode integer asset allocations into binary variables, transform the objective with budget penalty into a QUBO, and then map it to an Ising Hamiltonian whose ground state represents the optimal portfolio. They evaluate digitized-counterdiabatic quantum computing (DCQC) approaches for ground-state preparation by starting from a transverse-field initial Hamiltonian and evolving toward the problem Hamiltonian under a finite-time adiabatic schedule. To mitigate nonadiabatic errors, they add approximate counterdiabatic (CD) terms derived variationally: a local CD ansatz using single-qubit Y terms and a higher-order approximate CD term from a first-order nested-commutator ansatz. The time evolution is digitized via first-order Trotterization and assessed over many randomly generated portfolio instances. They compare success probabilities with and without CD driving, define enhancement metrics, and study scaling across system sizes. In addition, they test hybrid variational methods by comparing standard QAOA against DC-QAOA, where an additional CD-inspired unitary is inserted into the ansatz and parameters are optimized classically using Adagrad. The paper is explicitly a preprint and appears to rely on numerical simulation rather than execution on physical quantum hardware.

**Algorithms used:** Digitized-counterdiabatic quantum computing (DCQC), Digitized adiabatic quantum computing (DAdQC), QAOA, DC-QAOA, Local counterdiabatic driving (LCD), Approximate counterdiabatic driving (ACD)

**Experimental setup:** Numerical simulations of gate-based digitized adiabatic and variational quantum algorithms on Ising-encoded portfolio optimization instances. The adiabatic/DCQC part uses finite-time evolution from an initial transverse-field Hamiltonian to the portfolio Ising Hamiltonian, digitized with first-order Trotter-Suzuki decomposition. Main experiments include 1000 randomly generated instances for systems up to N = 14 qubits, with detailed histograms shown for N = 12. For DCQC examples, total evolution time is typically T = 1 with step size Delta t = 0.05 (20 Trotter steps), and an additional sweep over T uses Delta t = 0.1 for 40 instances. The QAOA/DC-QAOA part uses a small system of N = 6 qubits (n = 3 assets, g = 2), with circuit depths p = 1, 3, 5, and repeated random parameter initializations.

**Dataset:** Synthetic/randomly generated financial market data intended to mimic real-world trends, consisting of expected returns m_i (daily return data) and covariance matrices rho_ij for portfolio instances. No named real financial dataset is used.
## Experiment details
### Input
Input instances are randomly generated portfolio optimization problems defined by expected asset returns m_i and covariance matrix rho_ij. The discrete Markowitz formulation uses n assets and g budget slices, with integer asset variables encoded into g-bit binary strings, giving total qubit count N = n*g. Reported settings include N = 12 with (n = 12, g = 1), (n = 6, g = 2), and larger-slice cases g = 3 and g = 4; scaling studies go up to N = 14. The authors state that 1000 random instances are generated to mimic real-world trends. Lagrange multipliers are fixed at theta1 = 0.3, theta2 = 0.5, theta3 = 0.2 so the budget constraint has greater importance. No explicit time period, source database, or preprocessing pipeline for real market data is provided.

### Process
For the DCQC/DAdQC experiments: (1) formulate the discrete mean-variance portfolio optimization objective with budget penalty; (2) encode integer asset allocations into binary variables and map the QUBO to an Ising Hamiltonian Hp; (3) define the adiabatic interpolation Had(lambda) = (1-lambda)Hi + lambda Hp with Hi = -sum_i h_x sigma_x^i and initial state |+>^⊗N; (4) derive approximate counterdiabatic terms variationally by minimizing the action S = Tr[G_lambda^2], using either a local ansatz A~_lambda = sum_i alpha_i(t) sigma_y^i or a first-order nested-commutator ansatz yielding 2-local ACD terms; (5) choose a schedule lambda(t) = sin^2[(pi/2) sin^2(pi t / 2T)] so lambda-dot and lambda-double-dot vanish at the boundaries; (6) digitize the time evolution with first-order Trotter-Suzuki decomposition, using step size Delta t and total time T; (7) compute final-state ground-state success probability with and without CD terms over many random instances; (8) summarize improvements using enhancement ratio R_enh = I/I0 and success-probability enhancement P_enh = P/P0. For QAOA/DC-QAOA: (1) prepare |+>^⊗N; (2) apply p alternating layers of mixer and problem unitaries for QAOA, and add a CD-inspired unitary U_D(alpha) = exp[-i alpha sum_i h_i sigma_y^i] for DC-QAOA; (3) optimize parameters (gamma, beta) or (gamma, beta, alpha) using the Adagrad stochastic gradient optimizer with step size 0.1 to minimize the expectation of Hp; (4) run 20 random parameter initializations per instance and report averages over the best 10 runs for p = 1, 3, 5.

### Output
Primary output is ground-state success probability for the portfolio Ising Hamiltonian. For DCQC, results are reported as histograms across 1000 instances, success probability versus total evolution time T, average success-probability enhancement P_enh, and enhancement ratio R_enh, with error bars given as standard deviations. Comparisons are made between naive digitized adiabatic evolution without CD, local CD (LCD), and approximate CD (ACD). For variational experiments, output is average success probability P_s as a function of QAOA layer number p, comparing QAOA versus DC-QAOA across four instances, again with standard deviation error bars. No classical portfolio-optimization baseline is reported; baselines are quantum-method variants without CD assistance.

### Parameters
- qubits: {'tested_up_to': 14, 'examples': [6, 12]}
- assets_n: [3, 6, 12]
- budget_slices_g: [1, 2, 3, 4]
- lagrange_multipliers: {'theta1': 0.3, 'theta2': 0.5, 'theta3': 0.2}
- dcqc_total_evolution_time_T: [1]
- dcqc_time_step_delta_t: [0.05, 0.1]
- dcqc_trotter_order: 1
- dcqc_trotter_steps: 20
- instances_dcqc: 1000
- instances_time_sweep: 40
- qaoa_layers_p: [1, 3, 5]
- qaoa_optimizer: Adagrad
- qaoa_optimizer_step_size: 0.1
- qaoa_random_initializations: 20
- qaoa_reported_best_runs: 10
- dc_qaoa_cd_operator_pool: ['sigma_y', 'sigma_z sigma_y', 'sigma_y sigma_z', 'sigma_x sigma_y', 'sigma_y sigma_x']
- schedule: lambda(t) = sin^2[(pi/2) sin^2(pi t / 2T)]

### Hardware
{'hardware_type': 'Classical numerical simulation', 'simulator': 'Not explicitly named', 'qpu_used': False, 'noise_model': 'Not specified', 'transpilation_settings': 'Not specified'}

### Reproducibility
Preprint with substantial mathematical and procedural detail, including Hamiltonian construction, scheduling function, Trotterization order, key hyperparameters, and optimizer choice. However, no code repository, simulator specification, random seed policy, or exact synthetic data-generation procedure is provided, so replication is only partially supported.
## Findings
- [supported] In simulations of discrete mean-variance portfolio optimization mapped to an Ising Hamiltonian, adding approximate counterdiabatic (CD) terms to digitized adiabatic evolution increased ground-state success probabilities relative to evolution without CD terms.
- [supported] For 12-qubit instances with fewer budget slices, local counterdiabatic (LCD) terms produced a drastic improvement in success probability for most of the 1000 randomly generated problem instances studied.
- [supported] As the number of budget slices g increased, the effectiveness of simple LCD terms decreased, and first-order approximate counterdiabatic (ACD) terms from a nested-commutator ansatz provided stronger improvements.
- [supported] The paper reports an enhancement ratio of 1 for ACD at fixed g = 2 across the tested system sizes, meaning every tested instance showed improved success probability versus the no-CD baseline in their simulations.
- [supported] Average success-probability enhancement with CD driving increased with system size over the simulated range up to 14 qubits, although variability across instances was large for LCD.
- [supported] Success probability versus total evolution time T improved substantially for most of 40 sampled instances when either LCD or ACD terms were included, compared with no-CD evolution.
- [supported] In small simulated QAOA experiments for a 6-qubit portfolio instance class (n = 3, g = 2), DC-QAOA achieved higher average success probabilities than standard QAOA for all four tested instances and for p = 1, 3, 5 layers.
- [supported] The authors note that random parameter initialization makes optimization for both QAOA and DC-QAOA difficult because of a highly non-convex landscape and sensitivity to initialization.
- [speculative] The work argues that digitized-counterdiabatic quantum computing is a promising NISQ-era approach for finance applications such as portfolio optimization.
- [speculative] The paper suggests that extending to higher-order CD terms could yield further performance gains beyond the 2-local terms studied.
- [speculative] The authors suggest that combining digital-analog encoding with digitized-counterdiabatic methods may help approach quantum advantage for industrial finance use cases in the NISQ era.

**Results summary:** This preprint studies discrete Markowitz portfolio optimization by encoding the problem as an Ising Hamiltonian and solving it with digitized adiabatic and variational quantum algorithms augmented by approximate counterdiabatic driving. All reported results are simulation-based rather than demonstrations on quantum hardware. Across 1000 randomly generated instances and system sizes up to 14 qubits, adding local or approximate counterdiabatic terms generally increased the probability of preparing the ground state compared with naive digitized adiabatic evolution, with stronger gains from local CD at low slicing granularity and from first-order approximate CD at higher granularity. The authors also compare QAOA with DC-QAOA on small 6-qubit cases and report consistently higher average success probabilities for DC-QAOA across tested instances and circuit depths. While the paper frames these methods as relevant for NISQ finance applications, any broader quantum advantage claim remains speculative because the evidence is limited to small-scale simulations.

**Performance claims:**
- 1000 randomly generated portfolio instances evaluated for the digitized adiabatic/CD comparisons
- System sizes simulated up to N = 14 qubits
- For Fig. 1 experiments: N = 12 qubits, T = 1, step size Δt = 0.05, 20 Trotter steps
- For ACD at fixed g = 2, enhancement ratio Renh = 1 across the tested system sizes
- For success-probability-vs-time experiments: 40 random instances with n = 6, g = 2, N = 12, Δt = 0.1
- For QAOA/DC-QAOA comparison: N = 6 qubits with n = 3, g = 2, tested at p = 1, 3, 5 layers
- QAOA/DC-QAOA results averaged over the best 10 of 20 random parameter initializations
- One reported DC-QAOA/QAOA instance reached success probability around Ps = 0.60, while most instances were around Ps = 0.10
## Quantum advantage claim
**Classification:** speculative

The paper discusses digitized-counterdiabatic methods as a route to 'approach quantum advantage' for finance applications, but the evidence is based on small-scale simulations and relative comparisons against other quantum heuristics rather than against best classical methods or real-hardware demonstrations.
## Limitations
- Lack of peer review: the work is a preprint and its claims have not been independently validated through peer review.
- Experiments are based on simulations rather than execution on real quantum hardware, so hardware noise, calibration errors, and connectivity constraints are not empirically assessed.
- Problem instances use randomly generated data intended to mimic real-world trends rather than real market datasets.
- System sizes are limited to small simulations, with results reported up to about 12-14 qubits, constraining conclusions about large-scale financial relevance.
- Only short-time evolution and first-order Trotterization are considered, introducing digitization error of order O(Δt^2).
- The study considers only 2-local counterdiabatic terms; higher-order terms are not implemented.
- For larger partition counts g, local counterdiabatic terms lose effectiveness, requiring approximate higher-order terms.
- QAOA and DC-QAOA parameter optimization is challenging under random initialization because of a highly non-convex landscape with many local minima.
- QAOA/DC-QAOA tests are performed only on a very small system (N = 6, n = 3, g = 2), limiting generalizability.
- [inferred] No direct benchmark against state-of-the-art classical portfolio optimization solvers is provided, so practical quantum advantage is not established.
- [inferred] The claim that classical computers cannot solve such problems efficiently for industrial purposes is overstated for the specific small discrete instances studied.
- [inferred] The portfolio model is restricted to unconstrained single-period discrete mean-variance optimization, omitting realistic features such as transaction costs, turnover, cardinality, liquidity, and multi-period dynamics.
- [inferred] The use of binary encoding may introduce scaling overhead in qubit count as granularity increases, which may limit practical applicability.
- [inferred] Reproducibility is limited because the exact random instance generation process and full experimental setup details are not fully specified in the excerpt.
- [inferred] Success probability is the main evaluation metric; solution quality relative to optimal objective value, approximation ratio, and runtime/resource trade-offs are not deeply analyzed.
- [inferred] Although the paper mentions swap overhead for nearest-neighbor devices, this overhead is not quantitatively evaluated.
## Open questions
- How well do digitized-counterdiabatic methods perform on real NISQ hardware under realistic noise and limited connectivity?
- How does performance scale with the number of assets, budget granularity, and qubit count beyond the small simulated instances studied?
- To what extent do higher-order counterdiabatic terms improve success probability relative to their added circuit depth and implementation cost?
- Can DCQC or DC-QAOA outperform strong classical optimization methods on realistic portfolio optimization benchmarks?
- How sensitive are the results to the choice of Lagrange multipliers, scheduling function, and encoding scheme?
- What initialization or training strategies can reliably avoid poor local minima in QAOA and DC-QAOA for larger financial instances?
- How robust are the observed gains when using real financial data with nonstationarity, estimation error, and market constraints?
- What is the trade-off between Trotter step size, circuit depth, and final solution fidelity in practical implementations?
- Can the approach be extended effectively to more realistic portfolio formulations such as constrained, mixed-integer, or multi-period optimization?
- [inferred] Does the improvement in success probability translate into economically meaningful gains in portfolio quality after accounting for realistic market frictions?

**Future work:**
- Extend the present study beyond 2-local counterdiabatic terms to higher-order terms, which the authors expect to provide further enhancement.
- Develop a digital-analog quantum computing encoding combined with the digitized-counterdiabatic algorithm for the same portfolio optimization problem.
- Further investigate CD-assisted hybrid quantum-classical algorithms for hard portfolio optimization instances.
- [inferred] Validate the methods on real quantum hardware with noise-aware compilation and error mitigation.
- [inferred] Benchmark against classical baselines such as mixed-integer optimization, heuristics, and commercial portfolio solvers.
- [inferred] Test the approach on real financial datasets rather than randomly generated synthetic instances.
- [inferred] Explore alternative encodings and constraint formulations to reduce qubit overhead and improve scalability.
- [inferred] Study better parameter initialization and optimizer strategies for DC-QAOA/QAOA to address non-convex training landscapes.
- [inferred] Extend the framework to richer financial settings, including transaction costs, cardinality constraints, and multi-period portfolio optimization.
## Key ideas
- #idea:near-term-feasibility — Digitized-counterdiabatic driving improves ground-state preparation success for Ising-encoded discrete Markowitz portfolio instances in small NISQ-like simulations.
- #idea:hybrid-approach — DC-QAOA augments standard QAOA with a counterdiabatic-inspired unitary and achieves higher average success probabilities than vanilla QAOA on 6-qubit portfolio cases.
- #idea:near-term-feasibility — The paper uses a QUBO-to-Ising mapping for discrete mean-variance portfolio optimization and shows that shallow, finite-time digitized adiabatic evolution can be improved with local or approximate CD terms.
- #idea:quantum-advantage — The authors speculate that counterdiabatic methods, potentially combined with digital-analog encodings, could help approach quantum advantage for industrial portfolio optimization.
- #idea:hybrid-approach — Classical optimization remains central, as DC-QAOA parameters are tuned with Adagrad and performance is sensitive to initialization.
## Contradictions
- The paper suggests a path toward quantum advantage, but its evidence is limited to noiseless classical simulations on small instances up to 14 qubits, so this conflicts with stronger superiority claims absent real-hardware or classical-baseline comparisons.
- The framing implies scalability toward industrial portfolio optimization, yet the study only evaluates simplified unconstrained Markowitz instances with synthetic data and no benchmark against strong classical solvers, undermining any practical quantum-over-classical claim.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
