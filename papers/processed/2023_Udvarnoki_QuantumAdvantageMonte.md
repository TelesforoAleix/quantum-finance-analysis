---
aliases:
- Quantum advantage of Monte Carlo option pricing
- Quantum advantage Monte Carlo
authors:
- Zoltán Udvarnoki
- Gábor Fáth
- Norbert Fogarasi
auto_detected: true
classification: ''
contradiction_flags:
- contradiction:classical-vs-quantum
- contradiction:scalability
doi: 10.1088/2399-6528/acd2a4
evidence_type: ''
idea_tags:
- idea:quantum-advantage
- idea:near-term-feasibility
- idea:hybrid-approach
journal_or_venue: Journal of Physics Communications
methodology_tags:
- amplitude-estimation
- grover
- classical-simulation
paper_type: ''
quantum_advantage_claim: theoretical
related_papers:
- 2022_Rebentrost_QuantumSpeedup
relevance_phase1: high
relevance_phase3: high
source_type: peer-reviewed-empirical
source_type_confidence: high
step1_date: '2026-03-25T16:02:05.677092'
step1_model: gpt-5.1
step2_date: '2026-03-25T16:02:10.330640'
step2_model: gpt-5.1
step3_date: '2026-03-25T16:02:41.489499'
step3_model: gpt-5.4
step4_date: '2026-03-25T16:03:03.800867'
step4_model: gpt-5.4
step5_date: '2026-03-25T16:03:40.118588'
step5_model: gpt-5.4
step6_date: '2026-03-25T16:03:54.840098'
step6_model: gpt-5.4
steps_completed:
- 1
- 2
- 3
- 4
- 5
- 6
tags:
- topic/derivatives-pricing
- method/amplitude-estimation
- method/grover
- method/classical-simulation
- idea/quantum-advantage
- idea/near-term-feasibility
- idea/hybrid-approach
- contradiction/classical-vs-quantum
- contradiction/scalability
title: Quantum advantage of Monte Carlo option pricing
topic_tags:
- derivatives-pricing
year: 2023
zotero_key: ''
---

## Abstract summary
The paper investigates when and how quantum-accelerated Monte Carlo methods can outperform classical Monte Carlo for European option pricing. The authors develop a unified error framework that combines statistical, systematic, and hardware-induced noise, introduce a quantitative metric for quantum advantage, and compare a Fourier-series-based payoff approximation to a traditional rescaling approach. Using simulations with realistic noise models, they show that achieving a practical quantum advantage requires very low two-qubit gate error rates (below about 10⁻⁶), but only a modest number of logical qubits (around 20), with the Fourier method consistently yielding better performance than rescaling.
## Methodology
The paper presents a peer-reviewed empirical and simulation-based study of quantum-accelerated Monte Carlo (QAMC) for European call option pricing under the Black-Scholes-Merton model. The methodology decomposes the pricing workflow into state preparation, payoff/function application, and quantum amplitude estimation (QAE), and explicitly models both statistical and systematic errors. The underlying log-normal asset-price distribution is truncated to a finite interval around the expected terminal price and discretized into 2^n bins, then loaded exactly into amplitudes using an arbitrary-state preparation circuit. The option payoff is implemented using a comparator plus two alternative approximation schemes: a traditional rescaling-based linear approximation and a Fourier-series-based approximation adapted from prior work and extended for the call-option payoff. The authors introduce a quantum advantage metric comparing total pricing error of quantum and classical Monte Carlo at fixed sample count or runtime, and optimize free parameters jointly over statistical and systematic error contributions. They derive/compute statistical error using the Cramér-Rao bound for noisy QAE and correct it using maximum-likelihood simulations, while systematic error is decomposed into truncation, discretization, and function-approximation components. Experiments are conducted numerically in Qiskit under depolarizing noise, with noisy circuit simulation, transpilation to IBM-native gates, fitting of an effective Grover-operator coherence parameter, and extrapolation to larger qubit counts when direct simulation becomes infeasible. Performance is evaluated by the quantum advantage metric, error ratios, and gate-error thresholds required for quantum advantage, with comparisons against classical Monte Carlo and between the Fourier and rescaling payoff-approximation methods across a grid of option parameters.

**Algorithms used:** Quantum Amplitude Estimation, Quantum-accelerated Monte Carlo, Maximum Likelihood Estimation, Classical Monte Carlo
**Frameworks:** IBM Qiskit SDK

**Experimental setup:** All results are obtained via numerical simulation in IBM Qiskit rather than on real quantum hardware. Noisy simulations use one- and two-qubit depolarizing channels applied after gates (except RZ), with circuits transpiled using Qiskit's built-in transpiler at maximum optimization into the basis gate set {CX, X, SX, RZ}. Density-matrix simulation is used where possible to obtain exact noisy expectation values. The coupling map is primarily all-to-all, with checks against linear coupling. Because direct simulation beyond 13 qubits was infeasible, the authors extrapolate effective Grover-operator coherence to larger qubit counts using a fitted formula based on CX-gate counts.

**Dataset:** No empirical market dataset is used. Inputs are synthetic/analytical option-pricing instances generated from the Black-Scholes-Merton model for European call options, using log-normal terminal asset-price distributions and a grid of option parameters. The study also uses analytically known Black-Scholes prices and variances as references for error calculation and classical Monte Carlo benchmarking.
## Experiment details
### Input
Synthetic European call option instances under Black-Scholes-Merton. Baseline setup uses maturity T = 1 and at-the-money options with S0 = K = 2. A parameter grid is evaluated with risk-free rates r = {0.05, 0.1, 0.2} and volatilities nu = {0.1, 0.2, 0.3, 0.4}, yielding 12 combinations, though one outlier option was omitted in one averaged comparison, leaving 11 options. The terminal price distribution is assumed known in functional form, truncated to [E(ST) - w Var(ST), E(ST) + w Var(ST)] and discretized into 2^n bins. No historical time period, real-world sample size, or feature engineering is involved.

### Process
1. Formulate European call option pricing as an expected payoff under the Black-Scholes log-normal terminal distribution. 2. Truncate the continuous distribution using free parameter w and discretize it into 2^n bins, where n is the number of state-preparation qubits. 3. Prepare the discretized distribution exactly with an arbitrary-state preparation circuit. 4. Apply the payoff using a comparator circuit plus either (a) the rescaling technique with parameter c or (b) a Fourier-series-based approximation with truncation level l_max and smooth periodic continuation. 5. Run QAE using a Grover schedule; for reported results the main schedule is exponential with base 2 (m0 = 0, mk = 2^(k-1) for k > 0), though a linear schedule mk = {0,1,2,...,20} is used for fitting the effective coherence parameter in noise analysis. 6. Model hardware noise with depolarizing channels after one- and two-qubit gates, fit an effective Grover coherence probability eta_Q from gate-level noisy simulations, and use this in the noisy QAE likelihood model. 7. Estimate statistical error via the Cramér-Rao bound and correct finite-sample effects using maximum-likelihood simulations repeated 1000 times on a simple 2-qubit case. 8. Compute systematic errors separately from truncation, discretization, and function approximation, then combine them quadratically. 9. Define and optimize a quantum-advantage metric Q over parameter grids for n, w, c, l_max, and schedule length, while constraining total quantum relative error below a threshold epsilon_thr. 10. Compare the optimized quantum method against classical Monte Carlo and compare Fourier versus rescaling across option settings and gate-error levels.

### Output
Outputs include the total quantum pricing error (combining statistical and systematic components), the classical Monte Carlo error, the quantum advantage metric Q (ratio of classical to quantum error at fixed sample count or runtime), the ratio of systematic to statistical error, and estimated gate-error thresholds for achieving quantum advantage. Comparisons are made against classical Monte Carlo and between two payoff-approximation baselines: Fourier-series-based approximation versus the traditional rescaling method. Reported findings include average Q across option instances, per-option comparisons at selected CX error rates, optimal qubit counts and parameter ranges, and the conclusion that quantum advantage typically requires CX error rates around 10^-6 to 10^-7, with Fourier consistently outperforming rescaling.

### Parameters
- qubit_count_total: 2n + 1 qubits, where n is the number of state-preparation qubits and n additional ancilla qubits are used for the comparator
- state_preparation_qubits_n: optimized over 1 to 14 in direct simulations; typical optimal values in the quantum-advantage region are 5-10; extrapolation suggests about 20 logical qubits may suffice
- simulatable_qubit_limit: 13
- grover_schedule_reported_results: exponential schedule with base 2: m0 = 0, mk = 2^(k-1)
- grover_schedule_noise_fit: linear schedule mk = {0,1,2,...,20}
- shots_per_grover_step: 100
- parameter_grid_n: 1 to 14, step 1
- parameter_grid_w: 30 evenly spaced values in [0.5, 10]
- parameter_grid_c: 30 logarithmically spaced values in [1e-5, 100]
- parameter_grid_l_max: 0 to 59, step 1
- schedule_max_range: maximum of exponential schedule varied from 0 to 2^23
- error_threshold_constraint: relative error epsilon_thr = 1% in key comparison plots
- noise_model: depolarizing noise after one- and two-qubit gates except RZ
- one_to_two_qubit_error_ratio: epsilon_2 / epsilon_1 = 30
- basis_gates: ['CX', 'X', 'SX', 'RZ']
- transpilation_optimization: maximum optimization
- ml_simulation_repetitions: 1000
- example_gate_errors_for_noise-fit_figure: {'one_qubit_error': 2e-05, 'two_qubit_error': 0.0006}

### Hardware
No real QPU was used. Simulations were run in IBM Qiskit with noisy gate-level models and density-matrix simulation where feasible. Circuits were transpiled to IBM-native basis gates {CX, X, SX, RZ} using Qiskit's built-in transpiler with maximum optimization. Depolarizing noise was applied after all one- and two-qubit gates except RZ. The main assumed topology was all-to-all coupling, with additional checks under linear coupling. Effective Grover-operator coherence eta_Q was fitted from noisy simulation results, and larger-qubit behavior was extrapolated analytically from CX-count scaling.

### Reproducibility
Code and supporting data are openly available via the provided GitHub repository (https://github.com/udvzol/option_pricing), and the paper gives substantial methodological detail on circuits, noise model, parameter grids, schedules, and optimization procedure. Inputs are synthetic and analytically specified, which aids replication. Reproducibility is good, though some implementation details of exact state preparation and optimization workflow may still require consulting the repository.
## Findings
- [supported] In noisy simulations of quantum-accelerated Monte Carlo (QAMC) for European call option pricing, consistent quantum advantage over classical Monte Carlo generally required two-qubit (CX) gate error rates around 10^-6 to 10^-7.
- [supported] The study found that the Fourier-series-based payoff approximation outperformed the traditional rescaling method across the tested option set and across a wide range of CX error rates.
- [supported] Systematic errors were highly variable and could behave unpredictably as option and algorithm parameters changed, making consistent quantum advantage difficult on current noisy hardware.
- [supported] The ratio of systematic to statistical error at the optimum was around 0.7 for the rescaling approach, while for the Fourier approach it was lower by nearly an order of magnitude.
- [supported] The authors estimate that relatively few logical qubits, about 20, may be sufficient to observe quantum advantage for this option-pricing task, provided noise is low enough.
- [supported] Typical optimized parameter ranges in the quantum-advantage regime were 5-10 state-preparation qubits, truncation parameter w around 5-10, rescaling parameter c around 10^-2, Fourier truncation l_max around 10-30, and schedule length around 10-20.
- [supported] The effective-noise model at the Grover-operator level fit gate-level depolarizing-noise simulations well; in one illustrated case with one-qubit error 2x10^-5 and two-qubit error 6x10^-4, the fitted Grover coherence probability was 0.941.
- [supported] The maximum-likelihood amplitude-estimation simulations used to calibrate finite-sample effects were repeated 1000 times per setting, and an exponential correction was fit to the ratio between realized standard deviation and the Cramér-Rao lower bound.
- [speculative] The paper frames QAE as offering quadratic Monte Carlo speedup in principle, but the practical realization of this advantage depends on achieving very low hardware noise and controlling systematic errors.
- [supported] All reported results are based on numerical simulation with IBM Qiskit noise models and extrapolation beyond directly simulable qubit counts; no real quantum hardware demonstration of advantage is provided.

**Results summary:** This peer-reviewed empirical study evaluates quantum-accelerated Monte Carlo option pricing for European call options under realistic noisy conditions using numerical simulation rather than real hardware. The authors jointly model statistical and systematic errors, introduce a quantum-advantage metric, and optimize algorithm parameters under an error threshold. Their main empirical result is that practical quantum advantage is not robust on current noisy devices: for most tested options, QAMC only outperforms classical Monte Carlo when CX gate errors fall to roughly 10^-6 to 10^-7, far below current IBM hardware levels of about 10^-2 to 10^-3. The Fourier-series-based payoff approximation consistently performs better than the standard rescaling approach, mainly by reducing systematic error. The study also suggests that the qubit count needed for advantage may be modest, on the order of 20 logical qubits, if sufficiently low noise can be achieved. Overall, the paper supports the theoretical promise of quadratic speedup but shows that, in this financial application, hardware noise and systematic approximation errors are the dominant barriers to realizing it in practice.

**Performance claims:**
- Quantum advantage over classical Monte Carlo generally appears only when CX error rates are around 10^-6 to 10^-7 for most tested options
- Current IBM CX error rates are cited as roughly 10^-2 to 10^-3, well above the required threshold
- About 20 logical qubits may be sufficient to observe quantum advantage in this setting
- Systematic-to-statistical error ratio at the optimum is around 0.7 for the rescaling method
- Systematic-to-statistical error ratio for the Fourier method is lower by nearly one order of magnitude than for rescaling
- Typical optimized state-preparation qubit counts in the advantage region are 5-10
- Typical optimized Fourier truncation l_max values are about 10-30
- Typical optimized schedule lengths are about 10-20
- Typical optimized truncation parameter w is about 5-10
- Typical optimized rescaling parameter c is around 10^-2
- Illustrative gate-level noise simulation with one-qubit error 2x10^-5 and two-qubit error 6x10^-4 yielded fitted Grover coherence probability eta_Q = 0.941
- Finite-sample maximum-likelihood calibration repeated 1000 times per setting
## Quantum advantage claim
**Classification:** theoretical

The paper empirically studies conditions for advantage using noisy simulation and finds that advantage is achievable in simulation only at very low gate-error rates; it does not demonstrate quantum advantage on real hardware. Thus the underlying advantage is theoretically grounded and simulation-supported, but not experimentally demonstrated.
## Limitations
- Consistent quantum advantage is difficult on current hardware because systematic errors are unpredictable and can vary strongly with option and algorithm parameters.
- The estimated hardware requirement for advantage is extremely stringent: two-qubit gate error rates below 10^-6 are needed, far below current IBM hardware levels of roughly 10^-2 to 10^-3.
- State preparation has exponential computational cost in the number of qubits, making it one of the most costly and problematic parts of the approach.
- Function application must be approximated rather than implemented exactly on NISQ devices, introducing systematic error.
- The probability distribution must be truncated and discretized to fit finite qubit registers, which introduces truncation and discretization errors.
- The implementation assumes the underlying probability distribution is already known and available in functional form; a full general QAMC pipeline for generating this distribution is not included.
- Only the standard QAE/Grover-based algorithm was considered; potentially better adaptive or modified variants were explicitly left out of scope.
- The noise analysis relies primarily on a depolarizing noise model and an effective Grover-level coherence fit rather than full hardware-realistic noise tracking.
- Other noise models were not explored in depth because the authors note they can only be treated numerically.
- The study could not simulate circuits beyond 13 qubits due to computational cost, so larger-qubit conclusions rely on extrapolation rather than direct simulation.
- Extrapolation of effective coherence probability to larger qubit counts is based on a simple fitted formula, which may not fully capture scaling behavior.
- The Cramér-Rao bound is used for variance estimation, which is only exact in the asymptotic N → ∞ limit; finite-sample behavior required empirical correction.
- The Fourier approach increases the number of circuit applications/queries because multiple amplitude estimation tasks are required.
- The analysis is restricted to European call option pricing under the Black-Scholes-Merton setting, limiting generality to more complex derivatives or market dynamics.
- The experiments focus on at-the-money options with simplified parameter choices such as T = 1, which narrows empirical coverage.
- [inferred] No experiments were run on actual quantum hardware; results are based on simulation and fitted noise models, so real-device performance remains unvalidated.
- [inferred] The all-to-all coupling assumption used in main simulations is optimistic relative to many real devices and may understate routing overheads.
- [inferred] Exact arbitrary-state preparation circuits are assumed in simulation, but these may be impractical at scale and may overstate feasibility.
- [inferred] The benchmark compares against classical Monte Carlo but does not appear to compare against advanced classical variance-reduction or quasi-Monte Carlo methods commonly used in finance.
- [inferred] The study does not address end-to-end production constraints such as latency, throughput, integration with pricing systems, or regulatory validation.
- [inferred] Reproducibility is helped by open code, but some results depend on numerical optimization choices, fitted corrections, and extrapolation assumptions that may be sensitive to implementation details.
## Open questions
- Can quantum advantage for option pricing be realized on real fault-tolerant hardware at the predicted gate-error threshold around 10^-6?
- How accurate is the extrapolation from simulations up to 13 qubits to the approximately 20 logical qubits suggested as sufficient for quantum advantage?
- How would the conclusions change under more realistic hardware noise models beyond depolarizing noise?
- Can adaptive measurements or modified Grover operators improve Fisher information enough to materially lower the resource threshold for advantage?
- What is the best trade-off between systematic and statistical errors for different option parameters and algorithm settings?
- How robust is the Fourier-based function approximation advantage across broader classes of derivatives and payoff functions?
- How should state preparation be implemented efficiently when the distribution is not known in closed form but generated by a stochastic process, as in practical finance workflows?
- Would quantum generative adversarial networks or other approximate loading methods reduce total cost enough to offset the new systematic errors they introduce?
- If quantum arithmetic becomes practical, will the reduction in systematic error outweigh the increase in circuit depth and noise?
- How do these results extend beyond European calls and Black-Scholes assumptions to path-dependent, multi-asset, or early-exercise products?
- [inferred] How would the quantum approach compare against state-of-the-art classical pricing stacks using variance reduction, control variates, low-discrepancy sampling, or GPUs?
- [inferred] What are the true logical-qubit, T-gate, and error-correction overheads required for production-scale financial option pricing?

**Future work:**
- Explore quantum generative adversarial networks to reduce the computational cost of state preparation, while characterizing the additional systematic error they introduce.
- Investigate implementations using quantum arithmetic so that probability distribution evaluation and function evaluation can be performed directly on the quantum computer.
- Study adaptive-measurement approaches based on quantum Fisher information to potentially obtain tighter error bounds.
- Examine modified versions of the Grover operator that may yield higher classical Fisher information and better estimation performance.
- Explore other types of noise models beyond depolarizing noise.
- Extend the analysis beyond the standard algorithm considered here to alternative QAE schedules or variants that may be more noise-robust.
- [inferred] Validate the simulation-based findings on real quantum hardware and compare them with hardware-specific transpilation and connectivity constraints.
- [inferred] Test scalability on larger qubit counts without relying solely on extrapolation.
- [inferred] Extend the study to more realistic financial products, including exotic, path-dependent, and multi-asset derivatives.
- [inferred] Benchmark against stronger classical baselines used in industry, not only plain classical Monte Carlo.
- [inferred] Analyze full fault-tolerant resource estimates and production deployment feasibility for financial services use cases.
## Key ideas
- #idea:quantum-advantage — The paper defines a unified quantum-advantage metric comparing QAE-based quantum Monte Carlo against classical Monte Carlo for European call option pricing while jointly accounting for statistical and systematic errors.
- #idea:quantum-advantage — Noisy simulations suggest quantum advantage is only achievable when two-qubit gate errors are reduced to roughly 10^-6 to 10^-7.
- #idea:near-term-feasibility — Current NISQ-era hardware is insufficient for advantage in this setting despite the estimated logical qubit requirement being modest at around 20 qubits.
- #idea:hybrid-approach — The workflow is effectively hybrid, with classical truncation, discretization, parameter optimization, and payoff approximation shaping the quantum amplitude-estimation task.
- #idea:near-term-feasibility — A Fourier-series payoff approximation consistently outperforms the standard rescaling method by reducing systematic error.
- #idea:quantum-advantage — Systematic errors from truncation, discretization, and function approximation are major determinants of whether any practical speedup survives hardware noise.
## Contradictions
- The paper argues that quantum advantage may be possible with about 20 logical qubits for simplified European option pricing, which contrasts with more pessimistic resource estimates for realistic financial workloads such as 2022_Rebentrost_QuantumSpeedup; the discrepancy appears to come from the simplified Black-Scholes single-asset setting and extrapolated simulation assumptions.
- The paper frames advantage relative to standard classical Monte Carlo, but this may not hold against stronger classical baselines such as variance-reduction, quasi-Monte Carlo, or GPU-accelerated pricing, creating a contradiction with broad claims of quantum superiority.
- Although the paper discusses quantum advantage in principle, all evidence comes from noisy classical simulation with extrapolation beyond 13 qubits, which tempers any superiority claim and conflicts with stronger practical-advantage interpretations.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
