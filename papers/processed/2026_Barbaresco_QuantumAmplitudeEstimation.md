---
aliases:
- 'Quantum Amplitude Estimation in Practice: A Case Study in Option Pricing'
- Quantum Amplitude Estimation Practice
authors:
- Nouhaila Innan
- Muhammad Kashif
- Alberto Marchisio
- Muhammad Moonis Usman
- Muhammad Shafique
auto_detected: true
classification: ''
contradiction_flags:
- contradiction:classical-vs-quantum
- contradiction:scalability
doi: 10.1007/978-3-032-13852-1_35
evidence_type: ''
idea_tags:
- idea:near-term-feasibility
- idea:hybrid-approach
journal_or_venue: QUEST-IS 2025, CCIS 2743
methodology_tags:
- amplitude-estimation
- classical-simulation
paper_type: ''
quantum_advantage_claim: disputed
related_papers:
- 2021_Rebentrost_QuantumAlgorithmsFinance
relevance_phase1: high
relevance_phase3: high
source_type: peer-reviewed-empirical
source_type_confidence: high
step1_date: '2026-03-19T13:59:18.471419'
step1_model: Mistral-Large-3
step2_date: '2026-03-19T13:59:22.696748'
step2_model: Mistral-Large-3
step3_date: '2026-03-19T13:59:31.052545'
step3_model: Mistral-Large-3
step4_date: '2026-03-19T13:59:45.736762'
step4_model: Mistral-Large-3
step5_date: '2026-03-19T13:59:58.675110'
step5_model: Mistral-Large-3
step6_date: '2026-03-19T14:00:05.337546'
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
- method/classical-simulation
- idea/near-term-feasibility
- idea/hybrid-approach
- contradiction/classical-vs-quantum
- contradiction/scalability
title: 'Quantum Amplitude Estimation in Practice: A Case Study in Option Pricing'
topic_tags:
- derivatives-pricing
year: 2026
zotero_key: ''
---

## Abstract summary
This paper investigates the practical performance of Quantum Amplitude Estimation (QAE) algorithms—specifically Iterative Amplitude Estimation (IAE) and Maximum Likelihood Amplitude Estimation (MLAE)—for pricing European call options using historical Apple market data. The study benchmarks these quantum methods against classical approaches like Black-Scholes and Monte Carlo simulations, revealing that current quantum implementations struggle to capture low-probability, high-impact events due to limited qubit resolution, despite correctly identifying realized market outcomes.
## Methodology
The study evaluates the performance of Quantum Amplitude Estimation (QAE) algorithms, specifically Iterative Amplitude Estimation (IAE) and Maximum Likelihood Amplitude Estimation (MLAE), for pricing European call options using historical Apple market data. The methodology involves a four-stage pipeline: (1) preprocessing historical market data to extract relevant features such as spot price, strike price, volatility, and risk-free rate; (2) modeling the terminal asset price using a log-normal distribution encoded into a quantum state via Qiskit's LogNormalDistribution component; (3) encoding the European call option payoff function as a piecewise linear transformation using controlled rotations on an ancilla qubit; and (4) applying IAE and MLAE to estimate the expected payoff. The quantum results are benchmarked against classical methods, including the Black-Scholes (BS) model and Monte Carlo (MC) simulation, using the same discretized price space for fair comparison. The study investigates the impact of limited qubit resolution on the accuracy of quantum estimates, particularly in capturing low-probability, high-payoff events.

**Algorithms used:** Quantum Amplitude Estimation (QAE), Iterative Amplitude Estimation (IAE), Maximum Likelihood Amplitude Estimation (MLAE), Black-Scholes, Monte Carlo Simulation
**Frameworks:** Qiskit, Qiskit Finance

**Experimental setup:** The experiments were conducted using Qiskit on a quantum simulator. The setup involved 6 uncertainty qubits to discretize the terminal asset price into 64 bins, 3 objective qubits for payoff approximation, and 3 ancilla qubits for conditional logic. IAE was configured with a maximum of 3 Grover iterations, precision of 0.01, and confidence level of 0.05. MLAE used an evaluation schedule of {0, 1, 3, 7} Grover powers. Classical benchmarks included a dot-product-based expected value from the discretized payoff distribution (BS) and MC simulation with 100,000 samples. The study used historical Apple (AAPL) market data from January 2, 2022, to February 13, 2024, with parameters adjusted to simulate bullish market scenarios.

**Dataset:** Historical market data for Apple Inc. (AAPL) from January 2, 2022, to February 13, 2024, collected via the Yahoo Finance API. The dataset included spot price, strike price, implied volatility, time to maturity, and risk-free rate. Data was filtered for quality and maturity length, and a 5% shift was applied to mean log returns to simulate a bullish scenario. Volatility was clipped to a minimum of 0.20, and the strike price was set to 5% above the initial asset value.
## Findings
- [supported] Quantum Amplitude Estimation (QAE) variants (IAE and MLAE) returned an expected payoff of zero for European call options, while classical methods (Black-Scholes and Monte Carlo) yielded significantly positive values ($17.60 and $17.06 in two scenarios).
- [supported] The failure of QAE to capture non-zero expected payoffs is attributed to limited resolution from 6 uncertainty qubits (64 bins), which inadequately encodes small-amplitude, in-the-money price regions.
- [supported] Quantum circuits correctly identified the realized market outcome (zero payoff) but failed to capture the full expectation implied by the distribution tail.
- [supported] Classical benchmarks (Black-Scholes and Monte Carlo) aligned closely, with Monte Carlo deviations below 1% from analytical values.
- [supported] Quantum estimates for asset prices were lower than classical benchmarks ($185 vs. $198 in 2023–2024; $179 vs. $192 in 2022–2023), further highlighting resolution limitations.
- [speculative] Enhanced encoding strategies (e.g., nonuniform binning, adaptive amplitude shaping) may improve QAE performance for financial applications.
- [speculative] QAE could still be useful for binary classification or threshold-detection tasks in near-term quantum devices.

**Results summary:** The paper empirically evaluates Quantum Amplitude Estimation (QAE) for pricing European call options using historical Apple market data. Results from simulations show that QAE variants (IAE and MLAE) fail to estimate non-zero expected payoffs, returning zero values despite classical methods (Black-Scholes and Monte Carlo) yielding positive payoffs. This discrepancy is traced to coarse discretization (6 qubits, 64 bins), which cannot resolve low-probability, high-payoﬀ events. While quantum circuits accurately predicted the realized market outcome (zero payoff), they underperformed in capturing the full distribution tail. The study underscores the need for improved encoding strategies to bridge the gap between quantum and classical methods in financial expectation tasks.

**Performance claims:**
- QAE (IAE/MLAE) returned expected payoff = $0.00 vs. classical Black-Scholes = $17.60 (2023–2024) and $17.06 (2022–2023)
- Monte Carlo deviation from Black-Scholes: <1% (100,000 samples)
- Quantum asset price estimates: $185 (2023–2024) and $179 (2022–2023) vs. classical $198 and $192
- IAE circuit depth: 172,000 gates; MLAE circuit depth: 12,600 gates (noise-free simulation)
## Quantum advantage claim
**Classification:** disputed

Theoretical quantum advantage (asymptotic O(1/ε) scaling) is not demonstrated in practice due to resolution limitations. Results contradict the promise of QAE for expectation estimation under current hardware constraints, even in simulation. The paper explicitly states that quantum methods do not outpace classical techniques in this study.
## Limitations
- Limited resolution due to only 6 uncertainty qubits (64 bins), which inadequately encodes small-amplitude, in-the-money price regions, leading to zero expected payoff estimates
- Inability to capture low-probability, high-payoﬀ events that dominate the true expectation due to coarse discretization
- Experiments conducted in a noiseless simulator, excluding hardware noise and decoherence effects [inferred]
- No testing on real quantum hardware, limiting assessment of practical performance under noise and error conditions [inferred]
- Use of synthetic or adjusted historical data (e.g., 5% shift in mean log returns) may not fully represent real-world market conditions [inferred]
- Limited Grover iterations (max 3 for IAE) may constrain the accuracy of amplitude estimation
- Dependence on Qiskit's piecewise linear mapping for payoff encoding, which may not fully capture nonlinearities in real-world payoff functions [inferred]
- No comparison with other quantum amplitude estimation variants or hybrid quantum-classical approaches [inferred]
- Fixed strike price and maturity time may limit generalizability to other option pricing scenarios [inferred]
## Open questions
- How can quantum amplitude estimation be adapted to better resolve low-probability, high-payoﬀ events with limited qubits?
- What is the minimum qubit count required to achieve accurate expected payoff estimates for realistic financial distributions?
- How do noise and decoherence on real quantum hardware affect the performance of IAE and MLAE in option pricing?
- Can nonuniform binning or adaptive encoding strategies improve the resolution of tail events in quantum state preparation?
- What are the trade-offs between circuit depth, qubit count, and estimation accuracy in near-term quantum devices for financial applications?
- How do quantum amplitude estimation methods perform under non-log-normal or more complex asset price distributions?
- What is the impact of varying strike prices, maturities, and volatilities on the accuracy of quantum estimators?

**Future work:**
- Increase qubit counts to improve distribution resolution and capture low-probability events
- Develop advanced encoding strategies, such as nonuniform bin spacing or variational encoding, to better resolve tail events
- Test on real quantum hardware to assess performance under noise and error conditions
- Explore adaptive or hybrid quantum-classical approaches to enhance amplitude estimation accuracy
- Extend the pipeline to multi-asset options or more complex financial instruments
- Investigate the use of error mitigation techniques to improve results on noisy devices
- Compare IAE and MLAE with other quantum amplitude estimation variants or classical-quantum hybrid methods
- Apply the methodology to non-log-normal or empirical asset price distributions for broader applicability
## Key ideas
- #idea:near-term-feasibility — QAE variants (IAE/MLAE) are evaluated for near-term applicability in option pricing, but current hardware constraints (e.g., qubit resolution) limit their effectiveness compared to classical methods
- #idea:hybrid-approach — Speculative suggestion that hybrid quantum-classical approaches or advanced encoding strategies (e.g., nonuniform binning) could improve QAE performance for financial applications
- #limitation:qubit-count — Limited to 6 uncertainty qubits (64 bins), which inadequately captures low-probability, high-payoff events critical for accurate option pricing
- #limitation:data-encoding — Coarse discretization of log-normal distributions fails to resolve subtle but financially significant amplitudes above the strike price, leading to zero-valued payoff estimates
- #limitation:no-empirical-validation — Results are derived from noiseless simulations, with no evaluation of hardware noise or decoherence impacts on real quantum devices
- #contradiction:classical-vs-quantum — QAE fails to match classical benchmarks (Black-Scholes/Monte Carlo) in expectation estimation, contradicting theoretical quantum advantage claims for derivatives pricing
## Contradictions
- This paper contradicts theoretical claims of quantum advantage for QAE in derivatives pricing by demonstrating that classical methods (Black-Scholes/Monte Carlo) outperform QAE under current hardware constraints. The zero-valued payoff estimates from QAE (vs. positive classical values) highlight scalability and resolution limitations that undermine asymptotic advantage arguments (e.g., O(1/ε) scaling). Related work (e.g., 2021_Rebentrost_QuantumAlgorithmsFinance) may assume idealized conditions not reflected in this empirical study.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
