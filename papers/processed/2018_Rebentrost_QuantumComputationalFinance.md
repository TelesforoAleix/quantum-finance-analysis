---
aliases:
- 'Quantum computational finance: Monte Carlo pricing of financial derivatives'
- Quantum computational finance Monte
authors:
- Patrick Rebentrost
- Brajesh Gupt
- Thomas R. Bromley
auto_detected: true
classification: ''
contradiction_flags: []
doi: 10.48550/arXiv.1805.00109
evidence_type: ''
idea_tags:
- idea:quantum-advantage
- idea:near-term-feasibility
- idea:hybrid-approach
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
step1_date: '2026-03-19T22:48:29.517953'
step1_model: Mistral-Large-3
step2_date: '2026-03-19T22:48:33.122323'
step2_model: Mistral-Large-3
step3_date: '2026-03-19T22:48:48.427432'
step3_model: Mistral-Large-3
step4_date: '2026-03-19T22:49:34.472194'
step4_model: Mistral-Large-3
step5_date: '2026-03-19T22:49:43.746122'
step5_model: Mistral-Large-3
step6_date: '2026-03-19T22:49:50.025142'
step6_model: Mistral-Large-3
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
- idea/near-term-feasibility
- idea/hybrid-approach
title: 'Quantum computational finance: Monte Carlo pricing of financial derivatives'
topic_tags:
- derivatives-pricing
- risk-modelling
year: 2018
zotero_key: ''
---

## Abstract summary
This preprint introduces a quantum algorithm for Monte Carlo pricing of financial derivatives, leveraging quantum superposition and amplitude estimation to achieve a quadratic speedup over classical methods. The paper demonstrates how probability distributions relevant to financial models can be encoded in quantum states, and how derivative payoffs can be computed and measured using quantum circuits. The approach is applied to European and Asian options, showing potential for significant computational advantages in financial modeling and risk management.
## Methodology
The paper presents a quantum algorithm for Monte Carlo pricing of financial derivatives, specifically focusing on achieving a quadratic speedup over classical methods. The methodology involves encoding relevant probability distributions (e.g., Brownian motion for stock prices) into quantum superpositions, implementing payoff functions via quantum circuits, and extracting derivative prices through quantum measurements. The core technique is the amplitude estimation algorithm, which provides a quadratic speedup in the number of steps required to estimate the price with high confidence. The paper details the preparation of quantum states representing financial models (e.g., Black-Scholes-Merton), the implementation of arithmetic operations for payoff calculations, and the use of phase estimation to achieve the speedup. Numerical simulations are conducted to validate the quadratic speedup for European and Asian call options, comparing the quantum algorithm's performance against classical Monte Carlo methods.

**Algorithms used:** Amplitude Estimation, Quantum Monte Carlo, Grover's Search

**Experimental setup:** Numerical simulations were performed to validate the quadratic speedup. The quantum algorithm's phase estimation was simulated using a single qubit rotated according to a predetermined phase derived from the analytical price of a European call option. The classical Monte Carlo method was used as a baseline for comparison. Simulations were designed to ensure similar confidence levels (>99.5%) for both quantum and classical estimates.

**Dataset:** Theoretical financial models (e.g., Black-Scholes-Merton) were used to generate probability distributions for stock prices. No real-world datasets were employed; instead, synthetic data based on geometric Brownian motion and log-normal distributions were utilized.
## Findings
- [supported] The quantum algorithm for Monte Carlo pricing of financial derivatives achieves a quadratic speedup in the number of steps required to estimate the price with high confidence, demonstrated via numerical simulations (Fig. 3).
- [supported] The amplitude estimation algorithm provides a quadratic improvement in the number of measurements needed for a given accuracy, reducing the dependency from O(1/ϵ²) classically to O(1/ϵ) quantumly.
- [speculative] The quadratic speedup is theoretically argued to hold for complex derivatives like Asian options, assuming efficient preparation of probability distributions and computability of payoff functions.
- [supported] Numerical simulations show the quantum algorithm's error scaling exponent ζ_Q ≈ -0.982, nearly twice the classical exponent ζ_C = -0.5, confirming the quadratic speedup.
- [speculative] The framework could extend to risk management applications like XVA calculations, potentially reducing overnight computations to real-time analysis.
- [speculative] Continuous variable (CV) quantum computing may simplify Gaussian state preparation for probability distributions, offering further advantages in financial contexts.

**Results summary:** The paper presents a quantum algorithm for Monte Carlo pricing of financial derivatives, demonstrating a quadratic speedup in the number of computational steps required to estimate prices with high confidence. The algorithm leverages amplitude estimation to achieve this speedup, reducing the error dependency from O(1/ϵ²) classically to O(1/ϵ) quantumly. Numerical simulations validate the theoretical claims, showing near-quadratic improvement in error scaling for European call options. The authors extend the framework to Asian options and suggest broader applications in financial risk management, though these remain speculative without empirical validation. The work assumes efficient preparation of probability distributions and computability of payoff functions, which may limit practical implementation on current quantum hardware.

**Performance claims:**
- Quadratic speedup in the number of steps: O(1/ϵ) quantumly vs. O(1/ϵ²) classically for a given accuracy ϵ.
- Error scaling exponent ζ_Q ≈ -0.982 for the quantum algorithm, compared to ζ_C = -0.5 for classical Monte Carlo.
- Numerical simulations demonstrate the quantum algorithm's error upper bound ϵ_Q scales as O(1/k_Q), where k_Q is the number of quantum steps.
## Quantum advantage claim
**Classification:** theoretical

The paper claims a theoretical quadratic speedup in Monte Carlo pricing via amplitude estimation, supported by numerical simulations on classical hardware. However, the advantage is not demonstrated on real quantum hardware, and the scalability to practical problem sizes remains speculative. The speedup is contingent on efficient state preparation and payoff function implementation, which are not empirically validated in this preprint.
## Limitations
- The paper is a preprint and has not undergone peer review [inferred]
- Assumes the distribution of underlying random variables (martingale measure) is known and corresponding quantum states can be prepared efficiently
- Assumes efficient computability of the derivative payoff function within a quantum circuit
- Numerical simulations are limited to a single-qubit phase estimation rather than full quantum hardware implementation [inferred]
- Discretization of probability density and function approximation introduce errors (ν = O(2^-n))
- Variance bounds for options pricing rely on specific model assumptions (e.g., Black-Scholes-Merton framework)
- The quadratic speedup is demonstrated theoretically and via simulations, but not validated on real quantum hardware
- Resource estimates (qubit count, gate depth) are not explicitly quantified for practical implementation
- The Grover-Rudolph algorithm for state preparation assumes efficient sampling of integrals for log-concave distributions, which may not hold for all financial models [inferred]
- The paper focuses on European and Asian options; applicability to more complex derivatives (e.g., path-dependent or multi-asset options) is not explored
## Open questions
- How does the algorithm perform with more complex stochastic models beyond the Black-Scholes-Merton framework (e.g., fat-tailed distributions, Levy processes)?
- What are the practical resource requirements (qubit count, gate depth, coherence time) for implementing the algorithm on near-term quantum hardware?
- How does the algorithm compare to state-of-the-art classical Monte Carlo methods in terms of absolute runtime and accuracy for real-world financial datasets?
- Can the quadratic speedup be maintained when accounting for quantum hardware noise and error rates?
- How can the algorithm be extended to price derivatives with path-dependent payoffs or multiple underlying assets?
- What are the implications of discretization errors for high-dimensional financial models?
- How does the algorithm perform under non-Gaussian or non-log-concave distributions, where the Grover-Rudolph state preparation may not be efficient?

**Future work:**
- Extend the algorithm to more complex financial derivatives (e.g., path-dependent options, multi-asset options)
- Validate the algorithm on real quantum hardware to assess practical performance and noise resilience
- Explore continuous-variable quantum computing for more efficient state preparation of Gaussian distributions
- Investigate the algorithm's applicability to risk management tasks (e.g., XVA calculations) in financial institutions
- Develop hybrid quantum-classical approaches to mitigate discretization and approximation errors
- Benchmark the algorithm against classical methods using real-world financial data
- Study the impact of quantum error correction and noise mitigation techniques on the algorithm's performance
- Extend the framework to stochastic volatility models and other advanced financial models
## Key ideas
- #idea:quantum-advantage — Amplitude estimation achieves quadratic speedup (O(1/ϵ) vs. O(1/ϵ²)) for Monte Carlo pricing of European and Asian call options, demonstrated via numerical simulations
- #idea:near-term-feasibility — Theoretical framework for quantum Monte Carlo pricing is proposed, with potential extensions to risk management (e.g., XVA) and continuous-variable quantum computing
- #idea:hybrid-approach — Future work suggests hybrid quantum-classical approaches to address real-world financial data and hardware limitations
- #limitation:no-empirical-validation — Quadratic speedup is supported by numerical simulations but lacks validation on real quantum hardware
- #limitation:noise — Assumes ideal quantum operations, ignoring hardware noise and decoherence in NISQ devices
- #limitation:data-encoding — Discretization and binary approximation of payoff functions introduce errors (O(2^-n)) that may affect accuracy
## Contradictions
<!-- Step 6 output — where this paper contradicts others -->

## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->

## Experiment details
### Input
Input parameters for the simulations included initial stock price (S0), strike price (K), risk-free rate (r), volatility (σ), and maturity time (T). For example, one simulation used S0 = $100, K = $50, r = 0.05, σ = 0.2, and T = 1. The Brownian motion was discretized and encoded into quantum states using the Grover-Rudolph algorithm.

### Process
1. Encode the probability distribution of the underlying asset (e.g., Brownian motion) into a quantum superposition using the Grover-Rudolph algorithm. 2. Implement the payoff function (e.g., European call option) via quantum arithmetic circuits. 3. Apply a conditional rotation to an ancilla qubit to encode the payoff value. 4. Use amplitude estimation and phase estimation to extract the expectation value of the payoff. 5. Repeat the process for a sufficient number of shots to achieve the desired accuracy (e.g., 10^6 steps for quantum phase estimation). 6. Compare the quantum algorithm's error scaling against classical Monte Carlo methods.

### Output
The output included the estimated price of financial derivatives (e.g., European and Asian call options) and the error scaling as a function of the number of Monte Carlo steps. The quantum algorithm demonstrated a quadratic speedup in error reduction, with a scaling exponent of approximately -0.982 compared to the classical exponent of -0.5. The results were benchmarked against analytical solutions (e.g., Black-Scholes-Merton formula) for validation.

### Parameters
- qubits_for_distribution: Variable (e.g., n qubits for 2^n discretization points)
- qubits_for_payoff: Variable (e.g., m qubits for floating-point precision)
- phase_estimation_qubits: Single qubit for simplified simulations; m qubits for full phase estimation
- shots: Variable (e.g., 10^6 steps for quantum phase estimation)
- discretization_points: 2^n for Brownian motion distribution
- error_threshold: Additive error ϵ (e.g., ϵ < 4λ for variance bound λ^2)
- confidence_level: >99.5% (achieved via D ≈ 24 independent runs)

### Hardware
Simulations were performed on classical hardware to emulate quantum phase estimation. The paper does not specify the use of real quantum processing units (QPUs) or simulators (e.g., Qiskit Aer). The quantum circuits were theoretically designed for universal quantum computers (qubit model).

### Reproducibility
The paper provides sufficient theoretical detail to replicate the quantum algorithm, including the Grover-Rudolph state preparation, quantum arithmetic circuits, and phase estimation steps. Numerical simulations are described in detail, but no code or data repositories are referenced. The use of synthetic data based on theoretical models ensures reproducibility of the results.
