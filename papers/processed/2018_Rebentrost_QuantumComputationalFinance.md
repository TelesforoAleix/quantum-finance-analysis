---
aliases:
- 'Quantum computational ﬁnance: Monte Carlo pricing of ﬁnancial derivatives'
- Quantum computational nance Monte
authors:
- Patrick Rebentrost
- Brajesh Gupt
- Thomas R. Bromley
auto_detected: true
classification: ''
contradiction_flags:
- contradiction:classical-vs-quantum
- contradiction:scalability
doi: ''
evidence_type: ''
idea_tags:
- idea:quantum-advantage
journal_or_venue: arXiv
methodology_tags:
- amplitude-estimation
- grover
- quantum-simulation
- classical-simulation
paper_type: ''
quantum_advantage_claim: theoretical
related_papers: []
relevance_phase1: high
relevance_phase3: high
source_type: preprint
source_type_confidence: high
step1_date: '2026-03-25T15:51:43.564560'
step1_model: gpt-5.1
step2_date: '2026-03-25T15:51:48.028582'
step2_model: gpt-5.1
step3_date: '2026-03-25T15:52:24.392878'
step3_model: gpt-5.4
step4_date: '2026-03-25T15:52:58.825995'
step4_model: gpt-5.4
step5_date: '2026-03-25T15:53:30.203036'
step5_model: gpt-5.4
step6_date: '2026-03-25T15:53:41.161717'
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
- topic/risk-modelling
- method/amplitude-estimation
- method/grover
- method/quantum-simulation
- method/classical-simulation
- idea/quantum-advantage
- contradiction/classical-vs-quantum
- contradiction/scalability
title: 'Quantum computational ﬁnance: Monte Carlo pricing of ﬁnancial derivatives'
topic_tags:
- derivatives-pricing
- risk-modelling
year: 2018
zotero_key: ''
---

## Abstract summary
The paper develops a quantum algorithm for Monte Carlo pricing of financial derivatives, focusing on encoding stochastic asset dynamics and payoff functions into quantum circuits. By preparing the relevant probability distributions in superposition and using amplitude estimation, the authors show how to estimate option prices with a quadratic reduction in the number of samples compared to classical Monte Carlo. They illustrate the approach for European and Asian options within the Black–Scholes–Merton framework and analyze the associated quantum resource requirements and error behavior via theoretical bounds and numerical simulations.
## Methodology
This preprint is primarily theoretical with supporting numerical simulation. It develops a quantum Monte Carlo framework for pricing financial derivatives under the Black-Scholes-Merton setting by encoding risk-neutral probability distributions into quantum superposition, implementing payoff functions as reversible quantum circuits, and estimating expected discounted payoffs via amplitude estimation to obtain a quadratic speedup over classical Monte Carlo in error dependence. The paper formalizes the approach for European call options and extends the construction conceptually to Asian options. Methodologically, it specifies how to discretize Gaussian Brownian motion, prepare the corresponding quantum state using the Grover-Rudolph state-preparation method, compute option payoffs through reversible arithmetic circuits, and apply amplitude estimation/phase estimation to recover the expectation value. It also provides theorem-based complexity analysis and error bounds, including discretization error and estimation error. Empirical support is limited to classical numerical simulations of the phase-estimation scaling behavior, where the authors compare the error-versus-sample complexity of the quantum estimation procedure against standard classical Monte Carlo using analytically known Black-Scholes prices as benchmark inputs rather than executing full experiments on quantum hardware.

**Algorithms used:** Amplitude Estimation, Quantum Phase Estimation, Quantum Monte Carlo, Grover-Rudolph state preparation
**Frameworks:** Strawberry Fields, ProjectQ

**Experimental setup:** No real quantum hardware experiments were performed. The paper reports classical numerical simulations to illustrate the scaling of the proposed quantum method. Although the authors note that the phase-estimation subroutine could in principle be simulated with Strawberry Fields and ProjectQ, the reported numerics instead use a simplified single-qubit phase estimation model with a known phase corresponding to the analytically computed European call option price. Quantum and classical Monte Carlo estimates are compared in terms of error scaling versus number of Monte Carlo steps/applications of the unitary.

**Dataset:** No external empirical dataset is used. Inputs are synthetic/analytical option-pricing parameters under the Black-Scholes-Merton model, with European call option parameters such as initial stock price, strike price, risk-free rate, volatility, and maturity. The benchmark price is computed analytically from the Black-Scholes formula.
## Findings
- [speculative] The paper presents a quantum Monte Carlo framework for pricing financial derivatives by preparing risk-neutral probability distributions in superposition, encoding payoff functions into quantum circuits, and estimating prices via quantum measurement.
- [speculative] Under the assumption that the martingale/risk-neutral distribution can be prepared efficiently and the payoff function can be computed efficiently, amplitude estimation yields a quadratic improvement in error scaling from classical Monte Carlo's O(1/epsilon^2) sample complexity to quantum O(1/epsilon) dependence.
- [speculative] For [0,1]-bounded random variables, the paper claims amplitude estimation can estimate expectations to additive error epsilon using O(1/epsilon) applications, versus O(1/epsilon^2) repetitions for straightforward sampling.
- [speculative] For bounded-variance payoffs, the paper claims an almost quadratic speedup with resource scaling O((lambda/epsilon) polylog(lambda/epsilon)) in oracle uses, where lambda bounds payoff standard deviation.
- [speculative] The authors show how Gaussian/Brownian-motion distributions relevant to Black-Scholes-Merton pricing can be discretized and prepared on qubits using the Grover-Rudolph state-preparation method.
- [speculative] The paper derives that European call option pricing can be implemented with discretization error nu = O(2^-n) using n qubits for the payoff/distribution approximation.
- [speculative] The approach is extended conceptually to Asian options, including arithmetic-average Asian calls, by preparing product distributions over Brownian increments and computing path-dependent averages reversibly.
- [supported] Classical numerical simulations of the phase-estimation subroutine show error scaling close to O(1/k) for the quantum estimator, compared with O(1/sqrt(k)) for classical Monte Carlo, consistent with the claimed quadratic improvement in estimation overhead.
- [supported] In the reported simulation for a European call option with S0=$100, K=$50, r=0.05, sigma=0.2, T=1, and confidence boosted with D≈24 repetitions, the fitted quantum error exponent was zeta_Q = -0.982 versus classical zeta_C = -0.5.
- [supported] Across a range of strike prices, the ratio of fitted quantum to classical scaling exponents remained near 2, which the authors interpret as robust near-quadratic improvement in estimation scaling.
- [speculative] The paper argues that the method could be relevant for computationally intensive financial tasks such as XVA/risk calculations, potentially reducing overnight Monte Carlo workloads to much shorter runtimes if fault-tolerant quantum hardware becomes available.

**Results summary:** This preprint proposes a quantum algorithm for Monte Carlo pricing of financial derivatives in the Black-Scholes-Merton setting and related models. The core claim is theoretical: by encoding the pricing expectation value into a quantum amplitude and applying amplitude estimation, derivative prices can be estimated with O(1/epsilon) scaling in target additive error, compared with O(1/epsilon^2) for classical Monte Carlo. The paper details circuit constructions for preparing discretized Gaussian risk-neutral distributions, implementing payoff functions such as European call options, and extending the framework to path-dependent Asian options. Empirical evidence is limited to classical numerical simulations of the phase-estimation behavior rather than execution on quantum hardware; these simulations show quantum error scaling with fitted exponent about -0.982 versus the classical -0.5 benchmark, consistent with the predicted quadratic improvement. Because this is a preprint and the evidence is simulation-based, the quantum advantage claim is theoretical/speculative rather than demonstrated in practice.

**Performance claims:**
- Classical Monte Carlo requires k = O(lambda^2/epsilon^2) samples for additive error epsilon under bounded payoff variance.
- Naive quantum sampling of the ancilla also scales as O(mu(1-mu)/epsilon^2) repetitions.
- Amplitude estimation theorem gives error |a_hat - a| <= 2*pi*sqrt(a(1-a))/t + pi^2/t^2 with success probability at least 8/pi^2.
- For [0,1]-bounded expectations, additive error epsilon can be achieved with t = O(1/epsilon) oracle uses (for fixed success probability).
- For bounded-variance random variables, the paper claims O((lambda/epsilon) log^(3/2)(lambda/epsilon) log log(lambda/epsilon)) uses of U and O(log(lambda/epsilon) log log(lambda/epsilon)) copies of the state.
- European option discretization error is stated as nu = O(2^-n) using n qubits.
- Total European option pricing error is bounded as |mu_hat - E_Q[f(ST)]| <= epsilon + nu.
- Total number of applications of U for European option pricing is summarized as O~(lambda/epsilon), suppressing polylogarithmic factors.
- Simulation example: analytical European call price Pi = $10.5 for S0=$100, K=$50, r=0.05, sigma=0.2, T=1.
- Simulation fit: quantum error scaling exponent zeta_Q = -0.982 versus classical zeta_C = -0.5.
- Simulation confidence setting used about D ≈ 24 independent phase-estimation runs to achieve >99.5% confidence.
## Quantum advantage claim
**Classification:** theoretical

The paper claims a quadratic quantum speedup in Monte Carlo derivative pricing via amplitude estimation, improving error dependence from O(1/epsilon^2) to O(1/epsilon) under efficient state-preparation and payoff-oracle assumptions. However, evidence is limited to theory plus classical simulations of the scaling behavior, with no real quantum hardware demonstration; as a preprint, practical advantage remains speculative.
## Limitations
- As a preprint, the work has not undergone peer review.
- The claimed speedup is shown under strong assumptions: the martingale/risk-neutral distribution is known, the corresponding quantum states can be prepared efficiently, and the derivative payoff is efficiently computable in a quantum circuit.
- The paper provides classical numerical evidence for the quadratic speedup but does not implement the full algorithm on quantum hardware.
- The numerical demonstration of phase estimation uses a single-qubit simulation with a predetermined phase derived from the analytical Black-Scholes price, rather than an end-to-end simulation including state preparation and payoff encoding.
- Resource estimates focus mainly on query/sample complexity; full gate-level costs, circuit depth, ancilla overhead, and fault-tolerance requirements are not comprehensively quantified.
- The main worked examples are European call options and Asian options within the Black-Scholes-Merton framework, limiting demonstrated applicability to more realistic market models.
- The Black-Scholes-Merton model itself relies on restrictive assumptions such as constant parameters, continuous trading, no transaction costs, unlimited fractional trading, and no dividends.
- The authors explicitly note that they do not consider the differential equation for the option price over the interval 0 ≤ t ≤ T and instead focus only on the present-day option price.
- For Asian options, the discussion is largely constructive/theoretical and does not include detailed empirical benchmarking.
- [inferred] No comparison is provided against advanced classical variance-reduction Monte Carlo methods, so the practical advantage over state-of-the-art classical pricing is unclear.
- [inferred] The paper does not address noise, decoherence, finite sampling overhead on NISQ hardware, or error-mitigation, which could substantially erode the theoretical speedup.
- [inferred] Efficient state preparation may be a major bottleneck in practice; if loading/calibrating realistic financial distributions is costly, the end-to-end advantage may diminish.
- [inferred] The discretization and truncation of continuous distributions introduce approximation error, but there is limited practical guidance on how these errors scale for realistic contracts and parameter regimes.
- [inferred] No experiments are performed on real market data or institution-scale portfolios, limiting evidence for production relevance.
- [inferred] Reproducibility is limited because the paper does not provide a full implementation of all circuits and benchmarks needed to replicate end-to-end resource claims.
## Open questions
- How efficiently can realistic risk-neutral distributions, especially those obtained from market calibration, be prepared on a quantum computer?
- Do the theoretical quadratic speedups survive once full state-preparation, arithmetic, and fault-tolerant overheads are included?
- How well does the approach extend to more complicated stochastic models beyond Black-Scholes-Merton, such as stochastic volatility, correlated assets, fat-tailed processes, or jump processes?
- Can the method be adapted effectively to complex payoff functions used in practice at major financial institutions?
- What are the true resource requirements for institution-scale XVA and portfolio risk calculations?
- How does the algorithm perform relative to sophisticated classical Monte Carlo methods with variance reduction, quasi-Monte Carlo, or problem-specific approximations?
- Can continuous-variable quantum computing provide a practically better route than qubit-based implementations for financial Monte Carlo?
- How large are the constants and hidden polylogarithmic factors in the asymptotic complexity for realistic pricing tasks?
- What is the impact of hardware noise and imperfect controlled applications of the amplitude-estimation operator on pricing accuracy?
- How should one balance discretization error versus amplitude-estimation error in practical implementations?

**Future work:**
- Extend the approach to complex payoff functions often used at leading financial institutions.
- Address more complicated stochastic models for underlying asset dynamics.
- Investigate applications to risk-management workloads such as valuation adjustments (XVA), including CVA and broader portfolio risk analysis.
- Study continuous-variable quantum computing implementations, where Gaussian state preparation may be more straightforward than Grover-Rudolph state preparation.
- Explore the advantages of the continuous-variable setting in more detail for financial applications.
- Apply the framework to a broader class of derivatives whose payoffs depend on arithmetic operations and averages over multiple time windows.
- [inferred] Validate the algorithm with full end-to-end implementations rather than simulations using analytically known phases.
- [inferred] Benchmark against state-of-the-art classical pricing and risk engines on realistic datasets and portfolios.
- [inferred] Develop hardware-aware, noise-robust versions of amplitude-estimation-based pricing algorithms.
- [inferred] Provide detailed gate-count, qubit-count, and fault-tolerance analyses for practically relevant contracts.
## Key ideas
- #idea:quantum-advantage — Uses amplitude estimation to claim quadratic Monte Carlo speedup for derivative pricing, improving error scaling from O(1/epsilon^2) classically to O(1/epsilon) under efficient oracle/state-preparation assumptions.
- #idea:quantum-advantage — Encodes Black-Scholes-Merton risk-neutral distributions and option payoffs into quantum circuits for European calls and conceptually Asian options.
- #idea:quantum-advantage — Classical simulations of a simplified phase-estimation surrogate show fitted error scaling near O(1/k), consistent with the theoretical amplitude-estimation claim.
- #limitation:simulation-only — Evidence is based on classical simulation rather than execution of the full pricing algorithm on a real QPU.
- #limitation:no-empirical-validation — Numerical support uses a single-qubit known-phase surrogate instead of end-to-end state preparation, payoff computation, and estimation.
- #limitation:data-encoding — Practical advantage depends critically on efficient preparation of calibrated risk-neutral distributions and reversible payoff encoding, which are assumed rather than demonstrated.
- #limitation:noise — The analysis assumes ideal operations and does not quantify the impact of hardware noise, decoherence, or fault-tolerant overhead.
- #limitation:qubit-count — Realistic derivatives and path-dependent products would likely require substantial qubit and arithmetic resources beyond the demonstrated setting.
## Contradictions
- The paper claims quantum advantage in asymptotic sample complexity, but this is contradicted in practice by its own lack of end-to-end hardware validation and reliance on a simplified classical simulation; thus superiority over classical pricing is theoretical rather than demonstrated.
- The paper suggests relevance to large-scale pricing and XVA/risk workloads, but this is in tension with unquantified state-preparation, arithmetic-circuit, qubit, and fault-tolerance costs, creating a scalability contradiction for real financial problems.
- The claimed quadratic speedup is only against baseline classical Monte Carlo and not against advanced classical variance-reduction or quasi-Monte Carlo methods, so practical classical-vs-quantum superiority remains unresolved.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->

## Experiment details
### Input
Synthetic Black-Scholes-Merton option-pricing inputs rather than a dataset. Main simulation parameters for the reported scaling experiment: European call option with S0 = 100, K = 50, r = 0.05, sigma = 0.2, T = 1, and D = 24 independent phase-estimation runs to boost confidence. The analytical option price is computed as Pi = 10.5 and transformed into a phase theta via 1 - 2mu = cos(theta/2) / equivalent rescaling described in Eq. (24). Additional robustness analysis varies strike price K while keeping other parameters fixed.

### Process
1. Derive the analytical European call option price from the Black-Scholes-Merton formula. 2. Map the target expectation value/price to a phase parameter theta using the amplitude-estimation relationship. 3. Simulate quantum estimation using a single-qubit phase estimation routine with repeated applications of a z-rotation unitary exp(-i theta sigma_z / 2), treating the total number of unitary applications k_Q as the quantum Monte Carlo step count. 4. Repeat phase estimation D approximately 24 times and use the median/aggregation to obtain high confidence (>99.5%). 5. Independently run standard classical Monte Carlo pricing and record estimation error as a function of the number of samples k. 6. Compute absolute pricing error |Pi_hat - Pi| for both methods. 7. Fit the error curves to a power law Error = a k^zeta to estimate scaling exponents for quantum and classical methods. 8. Repeat the analysis while varying strike price to test robustness of the speedup ratio zeta_Q / zeta_C. Separately, the theoretical algorithm pipeline is: discretize the Gaussian Brownian motion distribution over 2^n points, prepare the superposition using Grover-Rudolph state preparation, compute the payoff with reversible arithmetic circuits, rotate an ancilla according to the payoff, and apply amplitude estimation/phase estimation to estimate the expected payoff.

### Output
Primary outputs are absolute pricing error versus number of Monte Carlo steps and fitted scaling exponents. The paper reports classical Monte Carlo scaling exponent zeta_C = -0.5 and fitted quantum scaling exponent zeta_Q = -0.982 for the main European call simulation, alongside a theoretical quantum upper-bound curve with exponent -1. A second output is the ratio zeta_Q / zeta_C across varying strike prices, showing an almost quadratic advantage. The analytical Black-Scholes price serves as the benchmark baseline for both methods.

### Parameters
- option_type: European call option
- S0: 100
- K: 50
- r: 0.05
- sigma: 0.2
- T: 1
- D_independent_phase_estimation_runs: 24
- analytical_price_Pi: 10.5
- classical_scaling_exponent: -0.5
- fitted_quantum_scaling_exponent: -0.982
- theoretical_quantum_scaling_exponent: -1
- confidence: >99.5%

### Hardware
{'hardware_type': 'Classical simulation only', 'quantum_hardware_used': 'None', 'simulator_description': 'Simplified single-qubit phase estimation simulation with known phase; no full-stack quantum circuit execution reported', 'mentioned_software_not_used_for_reported_results': ['Strawberry Fields', 'ProjectQ']}

### Reproducibility
As a preprint, the paper provides substantial mathematical detail, algorithm derivations, and explicit simulation parameters for the main numerical example, so the conceptual method is reproducible. However, no code repository or executable implementation is provided in the text, and the reported numerics use a simplified single-qubit phase-estimation surrogate rather than a full circuit-level implementation. Replication is feasible but would require reconstructing the simulation from the paper.
