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
step1_date: '2026-03-20T00:48:04.051777'
step1_model: Mistral-Large-3
step2_date: '2026-03-20T00:48:07.483017'
step2_model: Mistral-Large-3
step3_date: '2026-03-20T00:48:16.470698'
step3_model: Mistral-Large-3
step4_date: '2026-03-20T00:48:22.045922'
step4_model: Mistral-Large-3
step5_date: '2026-03-20T00:48:28.608628'
step5_model: Mistral-Large-3
step6_date: '2026-03-20T00:49:03.627606'
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
The study evaluates the performance of Quantum Amplitude Estimation (QAE) algorithms, specifically Iterative Amplitude Estimation (IAE) and Maximum Likelihood Amplitude Estimation (MLAE), for pricing European call options using historical Apple market data. The methodology involves a four-stage pipeline: (1) data preparation from historical market data, (2) modeling asset price uncertainty using a log-normal distribution, (3) encoding the payoff function into a quantum circuit, and (4) estimating the expected payoff using IAE and MLAE. The quantum circuits are constructed using Qiskit, with the log-normal distribution encoded into state qubits, the payoff function implemented via controlled rotations on an objective qubit, and ancilla qubits supporting conditional logic. The results are benchmarked against classical methods, including the Black-Scholes (BS) model and Monte Carlo (MC) simulation, to assess the accuracy and limitations of the quantum approaches under current hardware constraints.

**Algorithms used:** QAE, IAE, MLAE
**Frameworks:** Qiskit

**Experimental setup:** The experiments are conducted using Qiskit's quantum simulator with 6 uncertainty qubits, 3 objective qubits, and 3 ancilla qubits. The payoff function is approximated using a piecewise linear transformation. The amplitude estimation routines are configured with specific parameters for IAE (precision = 0.01, confidence level α = 0.05, max 3 Grover iterations) and MLAE (evaluation schedule {0, 1, 3, 7}). Classical benchmarks include a dot-product-based expected value from the discretized payoff distribution (BS) and a Monte Carlo estimate using 100,000 samples.

**Dataset:** Historical option and market data for Apple (AAPL) from January 2, 2022, to February 13, 2024, collected via the Yahoo Finance API. The dataset includes spot price, strike price, implied volatility, time to maturity, and risk-free rate.
## Findings
- [supported] Quantum Amplitude Estimation (QAE) variants (IAE and MLAE) returned an expected payoff of zero for European call options, while classical methods (Black-Scholes and Monte Carlo) yielded significantly positive values ($17.60 and $17.06 in two scenarios).
- [supported] The failure of QAE to capture non-zero expected payoffs is attributed to limited resolution from 6 uncertainty qubits (64 bins), which inadequately encode small-amplitude, in-the-money price regions.
- [supported] Quantum methods correctly identified the realized market outcome (zero payoff) but failed to capture the full expectation implied by the distribution tail.
- [supported] Classical benchmarks (Black-Scholes and Monte Carlo with 100,000 samples) showed <1% deviation from analytic values, confirming their accuracy for the same discretized price space.
- [supported] Quantum estimates for terminal asset prices were lower than classical benchmarks ($185 vs. $198 in 2023–2024; $179 vs. $192 in 2022–2023), further highlighting resolution limitations.
- [speculative] Enhanced encoding strategies (e.g., nonuniform binning, adaptive amplitude shaping) may improve QAE performance for financial applications.
- [speculative] QAE could still be useful for binary classification or threshold-detection tasks even with coarse resolution.

**Results summary:** The paper empirically evaluates Quantum Amplitude Estimation (QAE) for pricing European call options using historical Apple market data. Results from simulations show that QAE variants (IAE and MLAE) fail to produce non-zero expected payoffs, returning zero in scenarios where classical methods (Black-Scholes and Monte Carlo) yield positive values. This discrepancy is traced to the limited resolution of 6 uncertainty qubits, which cannot adequately represent low-probability, high-payoff events in the distribution tail. While quantum circuits correctly identified the realized market outcome, they underperformed in capturing the full expectation. The study underscores the current practical limitations of QAE under realistic constraints and suggests that improved encoding strategies are needed for future quantum financial applications.

**Performance claims:**
- QAE (IAE/MLAE) returned expected payoff = $0.00 vs. classical benchmarks of $17.60 (2023–2024) and $17.06 (2022–2023).
- Classical Monte Carlo simulation achieved <1% deviation from analytic Black-Scholes values with 100,000 samples.
- Quantum asset price estimates were ~6–7% lower than classical benchmarks (e.g., $185 vs. $198).
- IAE used up to 172,000 gates; MLAE used up to 12,600 gates in noiseless simulation.
## Quantum advantage claim
**Classification:** disputed

Theoretical QAE advantage (O(1/ε) scaling) is not demonstrated in practice due to resolution limitations. Results contradict the asymptotic advantage claim under current hardware constraints, as classical methods outperformed quantum estimators in this empirical study.
## Limitations
- Limited resolution due to only 6 uncertainty qubits (64 bins), which inadequately encodes small-amplitude, in-the-money price regions
- Quantum estimators (IAE and MLAE) returned an expected payoff of zero, failing to capture the full expectation implied by the distribution, unlike classical methods
- Coarse discretization of the price range leads to underestimation of low-probability, high-payoff events that dominate the expected payoff
- Experiments conducted in a noiseless simulator, excluding hardware noise and decoherence effects [inferred]
- Limited Grover iterations (max 3 for IAE) may constrain the accuracy of amplitude estimation
- No real quantum hardware was used; results are based on simulations, which may not reflect practical hardware constraints [inferred]
- Dataset size and diversity are limited to historical Apple market data, which may not generalize to other assets or market conditions [inferred]
- Fixed strike price and maturity time may limit the applicability of findings to other option pricing scenarios [inferred]
- No comparison with other quantum amplitude estimation variants or hybrid quantum-classical approaches [inferred]
## Open questions
- How can quantum amplitude estimation be improved to resolve low-probability, high-payoff events with limited qubits?
- What is the minimum qubit count required to achieve accurate expected payoff estimation for realistic financial distributions?
- How do noise and decoherence on real quantum hardware affect the performance of IAE and MLAE for option pricing?
- Can adaptive or nonuniform binning strategies improve the resolution of tail events in quantum state preparation?
- What are the trade-offs between circuit depth, qubit count, and estimation accuracy in near-term quantum devices for financial applications?
- How do quantum amplitude estimation methods perform in multi-asset or multi-period option pricing scenarios?

**Future work:**
- Increase qubit counts to improve distribution resolution and capture low-probability events
- Explore advanced encoding schemes, such as nonuniform bin spacing or variational encoding, to better resolve tail events
- Test on real quantum hardware to assess the impact of noise and decoherence
- Extend the pipeline to multi-asset or multi-period option pricing problems
- Investigate hybrid quantum-classical approaches to mitigate current limitations of QAE
- Develop adaptive amplitude estimation techniques that dynamically adjust to the probability landscape
- Benchmark against other quantum amplitude estimation variants or classical methods under varying market conditions
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

## Experiment details
### Input
Historical AAPL data covering 2022-01-02 to 2024-02-13, filtered for data quality and maturity length. Key features: spot price (S), strike price (K), implied volatility (σ), time to maturity (T), and risk-free rate (r). A 5% shift is applied to mean log returns to simulate a bullish market scenario, and volatility is clipped to a minimum of 0.20. The terminal asset price is modeled using a log-normal distribution with parameters derived from market inputs. The distribution is discretized into 64 bins using 6 uncertainty qubits.

### Process
1. Preprocess historical data to extract relevant features and parameterize the log-normal model. 2. Encode the discretized log-normal distribution into a quantum state using Qiskit's LogNormalDistribution. 3. Implement the European call payoff function as a piecewise linear transformation using LinearAmplitudeFunction, with controlled rotations on an objective qubit. 4. Apply IAE and MLAE to estimate the amplitude corresponding to the expected payoff. 5. Rescale the estimated amplitude to recover the expected payoff. 6. Compare quantum estimates against classical benchmarks (BS and MC) computed over the same discretized price space.

### Output
Expected payoff in USD and estimated asset price in USD. Metrics include the expected payoff from quantum methods (IAE and MLAE) and classical methods (BS and MC). The quantum methods returned an expected payoff of 0.00 USD in both tested scenarios, while classical methods yielded significantly positive values (~$17.50 USD). The estimated asset prices from quantum methods were also lower than classical benchmarks.

### Parameters
- uncertainty_qubits: 6
- objective_qubits: 3
- ancilla_qubits: 3
- bins: 64
- IAE_precision: 0.01
- IAE_confidence_level: 0.05
- IAE_max_iterations: 3
- MLAE_schedule: [0, 1, 3, 7]
- MC_samples: 100000
- strike_price_offset: 0.05
- return_shift: 0.05
- min_volatility: 0.2
- maturity_time: 1

### Hardware
Qiskit Aer statevector simulator (noiseless). Circuit transpilation reflects realistic overheads, with IAE circuits reaching up to 172,000 gates and MLAE circuits up to 12,600 gates.

### Reproducibility
Code and data details are partially provided. The paper references Qiskit Finance and Yahoo Finance API for data collection. While the experimental setup is described in detail, the exact code implementation is not explicitly linked. Data preprocessing steps are outlined, but raw data availability is not confirmed. Sufficient detail is provided to replicate the study with reasonable effort.
