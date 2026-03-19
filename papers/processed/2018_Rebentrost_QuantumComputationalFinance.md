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
step1_date: '2026-03-19T11:45:03.356389'
step1_model: Mistral-Large-3
step2_date: '2026-03-19T11:45:10.191891'
step2_model: Mistral-Large-3
step3_date: '2026-03-19T11:45:22.060599'
step3_model: Mistral-Large-3
step4_date: '2026-03-19T11:45:39.322158'
step4_model: Mistral-Large-3
step5_date: '2026-03-19T11:46:03.361028'
step5_model: Mistral-Large-3
step6_date: '2026-03-19T11:46:11.813255'
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
year: 2018
zotero_key: ''
---

## Abstract summary
This preprint introduces a quantum algorithm for pricing financial derivatives using Monte Carlo methods. The authors demonstrate how quantum superposition can encode probability distributions relevant to financial models, and how quantum circuits can implement payoff functions. By applying amplitude estimation, the paper achieves a quadratic speedup in the number of computational steps required for high-confidence price estimates compared to classical Monte Carlo methods. The work lays groundwork for exploring quantum computing applications in finance, particularly for derivative pricing.
## Methodology
The paper presents a quantum algorithm for Monte Carlo pricing of financial derivatives, specifically focusing on achieving a quadratic speedup over classical methods. The methodology involves encoding probability distributions of financial models into quantum superpositions, implementing payoff functions via quantum circuits, and extracting derivative prices through quantum measurements. The core technique is the amplitude estimation algorithm, which provides a quadratic speedup in the number of steps required to estimate the price with high confidence. The study specializes the quantum algorithm for European and Asian call options, detailing the preparation of Brownian motion distributions and the quantum circuits for option payoffs. Numerical simulations are conducted to demonstrate the quadratic speedup, comparing the error scaling of the quantum algorithm against classical Monte Carlo methods.

**Algorithms used:** Amplitude Estimation, Grover-Rudolph algorithm

**Experimental setup:** Numerical simulations were performed to showcase the quadratic speedup of the quantum algorithm. The phase estimation subroutine was simulated using a single qubit rotated according to a predetermined phase derived from the analytical price of a European call option. The simulations compared the error scaling of the quantum algorithm with classical Monte Carlo methods, demonstrating an almost quadratic advantage in estimation overhead.

**Dataset:** The study uses synthetic data based on the Black-Scholes-Merton model, including parameters such as initial stock price (S0), strike price (K), risk-free rate (r), volatility (σ), and maturity time (T). Sample evolutions of stock prices under geometric Brownian motion were generated for illustrative purposes.
## Findings
- [supported] The quantum algorithm for Monte Carlo pricing of financial derivatives achieves a quadratic speedup in the number of steps required to estimate the price with high confidence, demonstrated via numerical simulations (Fig. 3).
- [supported] The amplitude estimation algorithm provides a quadratic improvement in the error dependency from ϵ² to ϵ for estimating expectation values, as formalized in Theorems 2 and 3.
- [supported] Numerical simulations show the quantum algorithm's error scaling exponent ζ_Q ≈ -0.982, nearly twice the classical Monte Carlo exponent ζ_C = -0.5, confirming the quadratic speedup.
- [speculative] The quadratic speedup is argued to hold theoretically for complex derivatives (e.g., Asian options) under assumptions of efficient state preparation and computable payoff functions.
- [speculative] The authors suggest that quantum computing could significantly reduce overnight risk management calculations (e.g., XVA) to near real-time, enabling faster reactions to market changes.
- [speculative] The framework may extend to continuous variable (CV) quantum computation, simplifying Gaussian state preparation for probability distributions.
- [supported] The quantum algorithm's performance is validated for European call options, with analytical benchmarks confirming the quadratic advantage in simulations.

**Results summary:** The paper presents a quantum algorithm for Monte Carlo pricing of financial derivatives, demonstrating a quadratic speedup in the number of computational steps required to estimate prices with high confidence. This speedup is achieved via amplitude estimation, reducing the error dependency from ϵ² (classical) to ϵ (quantum). The algorithm is specialized for European and Asian options, with numerical simulations confirming near-quadratic error scaling (ζ_Q ≈ -0.982 vs. ζ_C = -0.5). Theoretical extensions to complex derivatives and risk management (e.g., XVA) are proposed, though empirical validation is limited to simulations. The work assumes efficient preparation of quantum states and computable payoff functions, with results derived from classical numerical calculations rather than real hardware.

**Performance claims:**
- Quadratic speedup in error scaling: ζ_Q ≈ -0.982 (quantum) vs. ζ_C = -0.5 (classical)
- Number of quantum steps: ~O(λ/ϵ) vs. classical ~O(λ²/ϵ²)
- Total error bound: |ˆΠ - Π| ≤ ϵ + ν, where ν = O(2⁻ⁿ) for n qubits
- Numerical validation: Error reduction from 10⁻¹ to 10⁻⁸ with 10⁷ quantum steps (Fig. 3)
## Quantum advantage claim
**Classification:** theoretical

The quadratic speedup is theoretically proven via amplitude estimation (Theorems 1–3) and supported by numerical simulations, but results are derived from classical calculations and simulations rather than real quantum hardware. Claims of advantage for complex derivatives (e.g., Asian options) and risk management remain speculative without empirical validation.
## Limitations
- The paper is a preprint and has not undergone peer review [inferred]
- Assumes the distribution of underlying random variables (martingale measure) is known and can be efficiently prepared as quantum states
- Assumes efficient computability of the derivative payoff function using quantum circuits
- The quadratic speedup is theoretical and relies on idealized quantum hardware without noise or errors [inferred]
- Numerical simulations are limited to simplified scenarios (e.g., single-qubit phase estimation) and do not fully replicate real quantum hardware constraints [inferred]
- Discretization of probability distributions and function approximations introduce errors (ν = O(2^{-n})) that compound with amplitude estimation errors
- The Grover-Rudolph algorithm for state preparation assumes efficient sampling of integrals for log-concave distributions, which may not hold for all financial models [inferred]
- Variance bounds for options (e.g., European call) are derived under the Black-Scholes-Merton framework, which may not generalize to more complex or realistic market models [inferred]
- The paper focuses on European and Asian options, leaving other complex derivatives (e.g., American options, path-dependent options) unaddressed [inferred]
- No empirical validation on real quantum hardware or comparison with state-of-the-art classical Monte Carlo methods [inferred]
- Resource estimates (e.g., qubit count, circuit depth) are theoretical and do not account for practical hardware limitations (e.g., gate fidelities, connectivity) [inferred]
- The continuous-variable (CV) quantum computing model is mentioned as a potential alternative but not explored in detail [inferred]
## Open questions
- How does the algorithm perform for financial derivatives with payoff functions that are not efficiently computable using quantum circuits?
- What are the practical resource requirements (qubit count, gate depth) for implementing the algorithm on near-term quantum hardware?
- How does noise and decoherence in real quantum hardware affect the quadratic speedup claimed by the algorithm?
- Can the algorithm be extended to price American options or other derivatives requiring optimal stopping problems?
- What is the impact of non-Gaussian or fat-tailed distributions (e.g., Lévy processes) on the algorithm's performance?
- How does the algorithm compare to classical Monte Carlo methods in terms of wall-clock time, given the overhead of quantum state preparation and measurement?
- Can the algorithm be adapted to handle stochastic volatility models or other complex market dynamics beyond the Black-Scholes-Merton framework?
- What are the implications of the algorithm for risk management applications (e.g., XVA calculations) in real-world financial institutions?

**Future work:**
- Extend the algorithm to more complex financial derivatives (e.g., American options, path-dependent options)
- Investigate the use of continuous-variable (CV) quantum computing for financial derivative pricing
- Implement and test the algorithm on near-term quantum hardware to assess practical performance and noise resilience
- Develop noise mitigation techniques to preserve the quadratic speedup in real-world quantum devices
- Explore the algorithm's applicability to risk management tasks (e.g., XVA calculations) and other computational finance problems
- Benchmark the algorithm against state-of-the-art classical Monte Carlo methods in terms of accuracy, speed, and resource efficiency
- Generalize the algorithm to handle non-Gaussian distributions and more realistic market models (e.g., stochastic volatility, jump-diffusion processes)
- Investigate hybrid quantum-classical approaches to combine the strengths of both paradigms for financial applications
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
