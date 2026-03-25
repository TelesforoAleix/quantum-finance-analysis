---
aliases:
- Portfolio optimization with digitized counterdiabatic quantum algorithms
- Portfolio optimization digitized counterdiabatic
authors:
- N. N. Hegade
- P. Chandarana
- K. Paul
- Xi Chen
- F. Albarrán-Arriagada
- E. Solano
auto_detected: true
classification: ''
contradiction_flags:
- contradiction:classical-vs-quantum
- contradiction:scalability
doi: 10.1103/PhysRevResearch.4.043204
evidence_type: ''
idea_tags:
- idea:quantum-advantage
- idea:near-term-feasibility
- idea:hybrid-approach
journal_or_venue: Physical Review Research
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
step1_date: '2026-03-25T15:57:05.035331'
step1_model: gpt-5.1
step2_date: '2026-03-25T15:57:12.867354'
step2_model: gpt-5.1
step3_date: '2026-03-25T15:57:41.626102'
step3_model: gpt-5.4
step4_date: '2026-03-25T15:58:09.088156'
step4_model: gpt-5.4
step5_date: '2026-03-25T15:58:41.636900'
step5_model: gpt-5.4
step6_date: '2026-03-25T15:58:52.721261'
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
title: Portfolio optimization with digitized counterdiabatic quantum algorithms
topic_tags:
- portfolio-optimisation
year: 2022
zotero_key: ''
---

## Abstract summary
The paper applies digitized-counterdiabatic quantum computing methods to a discrete mean-variance Markowitz portfolio optimization problem, encoding it into an Ising Hamiltonian and studying performance on gate-based quantum algorithms. The authors derive local and approximate counterdiabatic terms variationally and show, via simulations and a trapped-ion emulator, that these terms substantially enhance ground-state success probabilities compared to standard digitized adiabatic evolution and to QAOA. They also introduce and test a digitized-counterdiabatic QAOA variant (DC-QAOA), demonstrating improved performance on small portfolio instances relevant to financial applications in the NISQ era.
## Methodology
The paper presents a peer-reviewed empirical study of discrete mean-variance portfolio optimization formulated as an unconstrained single-period Markowitz problem and mapped to a QUBO, then to an Ising Hamiltonian whose ground state encodes the optimal portfolio. The main methodology evaluates digitized-counterdiabatic quantum computing (DCQC) for solving this optimization problem by combining digitized adiabatic quantum computing with approximate counterdiabatic (CD) driving. The authors derive local CD and approximate CD terms variationally by minimizing an action based on the adiabatic gauge potential, then implement the resulting time evolution through first-order Trotterization. They test many randomly generated portfolio instances across different numbers of assets and budget partitions, comparing success probabilities with and without CD terms under ideal simulation and under noisy emulation using Quantinuum's trapped-ion emulator. In addition, they benchmark hybrid variational approaches by comparing standard QAOA against DC-QAOA, where a CD-inspired unitary is added to the ansatz and parameters are optimized classically. Performance is assessed primarily through ground-state success probability and derived enhancement metrics, with comparisons across system sizes, instance hardness, and algorithmic variants.

**Algorithms used:** Digitized Adiabatic Quantum Computing, Digitized-Counterdiabatic Quantum Computing, QAOA, DC-QAOA
**Frameworks:** Quantinuum H1 emulator, Azure Quantum

**Experimental setup:** The study uses ideal numerical simulations and noisy emulation. For DCQC, the adiabatic evolution from an initial transverse-field Hamiltonian to the portfolio Ising Hamiltonian is digitized using first-order Trotter-Suzuki decomposition. Simulations cover up to N = 14 qubits and include 1000 random portfolio instances for several settings. Representative experiments use N = 12 qubits with total evolution time T = 1 and step size Δt = 0.05 (20 Trotter steps), and additional time-sweep experiments use Δt = 0.1 over 40 random instances. A noisy experiment is run on the Quantinuum System Model H1 emulator for a 6-qubit instance (n = 3, g = 2), with all qubits initialized in |+> states, native ZZ two-qubit gates, T = 0.3, Δt = 0.1, and 500 shots. For variational benchmarking, QAOA and DC-QAOA are tested on 10 instances of a 6-qubit problem, with 20 random initializations per instance and layer-wise comparisons.

**Dataset:** Synthetic/randomly generated financial portfolio instances designed to mimic real-world trends. Inputs consist of expected daily returns m_i and covariance matrices ρ_ij for assets in discrete mean-variance portfolio optimization problems. No named public financial dataset is used.
## Experiment details
### Input
Input data are randomly generated portfolio instances parameterized by expected returns m_i and covariance matrix ρ_ij, intended to mimic real market behavior. The optimization problem distributes a budget b across n assets with granularity g, where each asset allocation is encoded using g binary bits, giving total qubit count N = n*g. The paper reports experiments for settings including N = 12 with (n = 12, g = 1), (n = 6, g = 2), and larger g values such as 3 and 4; simulations extend up to N = 14 qubits. Fixed Lagrange multipliers are θ1 = 0.3, θ2 = 0.5, and θ3 = 0.2 to emphasize the budget constraint. For QAOA/DC-QAOA, the benchmark uses N = 6 qubits with n = 3 and g = 2 across 10 random instances. No explicit time period, source market, or preprocessing pipeline beyond random generation is reported.

### Process
For DCQC, the authors: (1) formulate the discrete Markowitz portfolio problem as a QUBO and map it to an Ising Hamiltonian Hp; (2) define an adiabatic interpolation Had(λ) = (1-λ)Hi + λHp with initial transverse-field Hamiltonian Hi and initial state |+>^⊗N; (3) derive local CD terms A~_λ = Σ_i α_i(t)σ_i^y variationally by minimizing S = Tr[G_λ^2], and also derive approximate CD terms from a first-order nested-commutator ansatz; (4) choose a scheduling function λ(t) whose first and second derivatives vanish at the boundaries; (5) digitize the total evolution using first-order Trotterization with step size Δt = T/M; (6) execute the circuit with and without CD terms and compute the final ground-state success probability; and (7) aggregate results over many random instances, also computing enhancement ratio and success-probability enhancement. For noisy emulation, they run a 6-qubit instance on the Quantinuum H1 emulator, initialize all qubits in |+>, use native ZZ gates, evolve for T = 0.3 with three Trotter steps, measure in the computational basis, and estimate output probabilities from 500 shots. For QAOA, they apply p alternating layers of mixer and problem unitaries to |+>^⊗N and optimize the expectation value of Hp. For DC-QAOA, they add a CD-inspired unitary UD(α) = exp[-iα Σ_i h_i σ_i^y], with the operator chosen from a nested-commutator-derived pool A^(2)_λ = {σ^y, σ^zσ^y, σ^yσ^z, σ^xσ^y, σ^yσ^x}. Parameters (γ, β, α) are optimized using the Adagrad stochastic gradient descent optimizer with step size 0.1. For each of 10 instances, 20 random initial parameter seeds are tried and the best output is retained.

### Output
The main reported output is ground-state success probability, i.e., the probability of measuring the bitstring corresponding to the optimal portfolio. The paper compares success probabilities for naive digitized adiabatic evolution versus evolution with local CD and approximate CD terms, and also compares QAOA versus DC-QAOA. Additional reported metrics include enhancement ratio R_enh = I/I0, where I is the number of instances improved by CD terms, and success-probability enhancement P_enh = P/P0. Results are shown as histograms over 1000 instances, average enhancement with standard deviation across system sizes, success probability as a function of total evolution time, output probability distributions for the noisy emulator, and mean success probability versus number of QAOA layers with error bars.

### Parameters
- qubits: {'simulations_up_to': 14, 'representative_cases': [6, 12]}
- assets_n: [3, 6, 12]
- granularity_g: [1, 2, 3, 4]
- lagrange_multipliers: {'theta1': 0.3, 'theta2': 0.5, 'theta3': 0.2}
- dcqc_total_evolution_time: [1.0, 0.3]
- trotter_step_size: [0.05, 0.1]
- trotter_order: 1
- trotter_steps: {'for_T_1_dt_0.05': 20, 'for_T_0.3_dt_0.1': 3}
- shots: 500
- qaoa_optimizer: Adagrad
- qaoa_step_size: 0.1
- qaoa_instances: 10
- random_initializations_per_instance: 20
- dc_term_types: ['local CD', 'approximate CD via first-order nested commutator']

### Hardware
Ideal simulations are supplemented by noisy emulation on Quantinuum System Model H1, an all-to-all connected trapped-ion quantum computing emulator with 20 qubits, accessed via Azure Quantum credits. The implementation uses the device's native two-qubit ZZ(θ) gate to realize interaction terms efficiently without standard CNOT decomposition. The noisy demonstration uses the H1 emulator rather than a real QPU. No transpilation settings are reported.

### Reproducibility
The paper provides the mathematical formulation, Hamiltonians, CD ansatzes, key hyperparameters, system sizes, optimizer choice, and representative evolution settings, which supports partial replication. However, no code repository or explicit data-generation procedure is provided, and the portfolio data are synthetic rather than from a public named dataset. Reproducibility is moderate but not fully turnkey.
## Findings
- [supported] Digitized-counterdiabatic quantum computing (DCQC) substantially improves ground-state success probability for discrete mean-variance portfolio optimization instances compared with digitized adiabatic evolution without counterdiabatic terms.
- [supported] Across 1000 randomly generated portfolio instances on 12-qubit systems, local counterdiabatic (LCD) driving gave strong success-probability improvements for low slicing values (e.g., n=12, g=1 and n=6, g=2), while approximate counterdiabatic (ACD) terms performed better for larger slicing values (e.g., g=3 and g=4).
- [supported] For harder instances with larger slicing parameter g, first-order nested-commutator approximate counterdiabatic terms improved success probabilities where local CD terms became less effective.
- [supported] The authors report that both LCD and ACD can yield at least up to an order-of-magnitude enhancement in success probability over naive digitized adiabatic evolution.
- [supported] For fixed g=2 across multiple system sizes, the ACD enhancement ratio was reported as 1, meaning all tested instances showed improved success probability when ACD was included.
- [supported] Simulation results indicate that the benefit from counterdiabatic terms increases with system size, based on the reported average success-probability enhancement trends.
- [supported] In noisy emulation on Quantinuum's H1 trapped-ion emulator for a 6-qubit instance (n=3, g=2), ACD produced a much higher probability of the correct ground-state bitstring than evolution without CD, even with only three Trotter steps.
- [supported] In hybrid variational optimization, DC-QAOA achieved higher mean success probability than standard QAOA for all 10 tested 6-qubit portfolio instances.
- [supported] The empirical results in this paper are primarily from ideal classical simulation and noisy hardware emulation rather than execution on physical quantum hardware.
- [speculative] The paper frames digitized-counterdiabatic methods as a route toward quantum advantage for industrial finance applications in the NISQ era, but does not empirically demonstrate quantum advantage over classical algorithms.

**Results summary:** The paper studies discrete Markowitz portfolio optimization encoded as an Ising Hamiltonian and evaluates digitized-counterdiabatic quantum methods on this problem. Using ideal simulations over many randomly generated instances and a noisy Quantinuum H1 emulator for a small case, the authors find that adding counterdiabatic terms markedly increases the probability of preparing the ground state compared with standard digitized adiabatic evolution. For 12-qubit systems, local counterdiabatic driving works especially well for easier low-slicing instances, while approximate counterdiabatic terms derived from a first-order nested-commutator ansatz perform better on harder higher-slicing instances. The paper reports improvements of up to an order of magnitude in success probability and an ACD enhancement ratio of 1 for tested instances at fixed g=2. In a separate variational study on 10 six-qubit instances, DC-QAOA consistently outperformed standard QAOA in mean success probability. Results are based on simulation and noisy emulation, not real-hardware demonstrations of advantage over classical solvers.

**Performance claims:**
- 1000 randomly chosen portfolio instances evaluated for 12-qubit systems
- System sizes studied up to N=14 qubits
- For Fig. 1 experiments: total evolution time T=1, Trotter step size Δt=0.05, 20 Trotter steps
- Authors state success-probability enhancement of at least up to an order of magnitude with CD terms
- For fixed g=2, ACD enhancement ratio Renh = 1 across tested system sizes
- Noisy emulator test used N=6 qubits with n=3, g=2
- Noisy emulator test used total evolution time T=0.3 and step size δt=0.1, i.e., 3 Trotter steps
- Noisy emulator test used 500 measurement shots
- QAOA/DC-QAOA comparison used 10 instances on N=6 qubits (n=3, g=2)
- For each QAOA/DC-QAOA instance, 20 random initializations were tested
- Adagrad optimizer step size was 0.1 in the QAOA/DC-QAOA experiments
## Quantum advantage claim
**Classification:** speculative

The paper discusses DCQC as a path toward quantum advantage and shows improved success probabilities versus other quantum heuristics (digitized adiabatic evolution, QAOA, DC-QAOA variants), but it does not demonstrate an advantage over classical algorithms. Results are from ideal simulation and noisy emulation, not a real-hardware quantum advantage experiment.
## Limitations
- Experiments are limited to small problem sizes, with simulations up to N = 14 qubits and QAOA/DC-QAOA tests on N = 6 qubits, constraining conclusions about large-scale financial instances
- The study uses randomly generated portfolio instances intended to mimic real-world trends rather than real market datasets, limiting external validity for practical financial deployment
- No demonstration on actual quantum hardware is provided; noisy results are obtained on Quantinuum's H1 emulator rather than a physical device
- The digitized adiabatic approach requires many gates, which the paper notes reduces fidelity and remains impractical for NISQ devices without error correction
- Only first-order Trotterization is used, introducing approximation error of order O(Δt^2)
- The noisy emulator demonstration is restricted to a single 6-qubit instance with only 3 Trotter steps and 500 shots, limiting the breadth of empirical validation under noise
- The paper considers only 2-local counterdiabatic terms in the main study, which may be insufficient for harder instances
- Performance of local counterdiabatic terms degrades as the slicing parameter g increases, indicating limited robustness on harder, more strongly coupled instances
- QAOA and DC-QAOA parameter optimization is described as challenging because of a highly nonconvex cost landscape
- Hybrid quantum-classical methods may suffer from local minima and noise-induced barren plateaus
- Higher-order counterdiabatic terms, while potentially beneficial, may substantially increase circuit depth and induce more errors
- [inferred] The paper does not benchmark against strong state-of-the-art classical portfolio optimization solvers, so practical quantum advantage is not established
- [inferred] Reproducibility is limited because the exact randomly generated datasets/instances and full experimental seeds are not provided in the text
- [inferred] The study focuses on unconstrained single-period discrete mean-variance optimization, excluding many realistic portfolio features such as multi-period dynamics, transaction costs, and richer institutional constraints
- [inferred] Claims about scalability and increasing enhancement with system size are based on small-scale simulations and may not hold in production-scale settings
## Open questions
- How well do digitized-counterdiabatic methods perform on larger portfolio instances beyond 14 qubits?
- Will the observed success-probability improvements persist on real quantum hardware with full device noise and calibration drift?
- How much benefit can higher-order counterdiabatic terms provide relative to their added circuit-depth cost?
- What is the best choice of counterdiabatic operator pool for hard portfolio optimization instances?
- How sensitive are QAOA and DC-QAOA results to initialization strategy, optimizer choice, and optimizer hyperparameters?
- Can these methods handle realistic financial formulations with transaction costs, multiple periods, inequality constraints, or mixed-integer features?
- At what problem size, if any, do these methods outperform competitive classical optimization approaches in wall-clock time or solution quality?
- How does limited qubit connectivity on other hardware platforms affect implementation cost compared with the all-to-all trapped-ion setting?
- What is the trade-off between Trotter step size, circuit depth, and solution quality under realistic noise?
- How robust are the results when using real historical return and covariance data rather than synthetic/randomly generated instances?

**Future work:**
- Extend the approach to higher-order counterdiabatic terms to seek further enhancement in success probability
- Develop digital-analog quantum computing encodings combined with digitized-counterdiabatic algorithms for the same portfolio optimization problem
- Investigate broader application of counterdiabatic methods to other combinatorial optimization problems beyond portfolio optimization
- Study harder instances more systematically, including the use of higher-order counterdiabatic terms in DC-QAOA
- Explore improved strategies for finding optimal QAOA/DC-QAOA parameters, including better initialization and optimizer design
- Validate the methods on real quantum hardware rather than only ideal simulation and emulator-based noise models
- [inferred] Evaluate the algorithms on real financial datasets and more realistic portfolio constraints
- [inferred] Benchmark against advanced classical solvers to assess whether any practical quantum advantage is achievable
- [inferred] Test scalability on larger qubit counts and production-relevant portfolio sizes as hardware improves
## Key ideas
- #idea:hybrid-approach — The paper formulates discrete mean-variance Markowitz portfolio optimization as a QUBO/Ising problem and shows that adding counterdiabatic-inspired terms to quantum optimization workflows improves solution success probability.
- #idea:quantum-advantage — Digitized-counterdiabatic evolution and DC-QAOA outperform baseline quantum approaches such as naive digitized adiabatic evolution and standard QAOA on small portfolio instances.
- #idea:near-term-feasibility — A noisy trapped-ion emulator experiment on a 6-qubit instance suggests counterdiabatic methods may be usable in NISQ settings for very small portfolio problems.
- #idea:hybrid-approach — DC-QAOA combines a CD-inspired unitary with classical parameter optimization via Adagrad, yielding higher mean success probability than standard QAOA across all tested 6-qubit instances.
## Contradictions
- The paper frames the method as a route toward quantum advantage, but its evidence only shows improvement over other quantum heuristics, not over classical portfolio optimization methods; this supports #contradiction:classical-vs-quantum.
- The paper suggests benefits may grow with system size, yet experiments are limited to simulations up to 14 qubits and a single 6-qubit noisy emulator case, so claims about scaling to realistic financial problems remain unverified; this supports #contradiction:scalability.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
