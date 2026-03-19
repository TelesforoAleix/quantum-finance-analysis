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
related_papers: []
relevance_phase1: high
relevance_phase3: high
source_type: peer-reviewed-empirical
source_type_confidence: high
step1_date: '2026-03-18T23:15:45.944571'
step1_model: Mistral-Large-3
step2_date: '2026-03-18T23:15:49.647640'
step2_model: Mistral-Large-3
step3_date: '2026-03-18T23:16:32.627575'
step3_model: Mistral-Large-3
step4_date: '2026-03-18T23:16:43.274516'
step4_model: Mistral-Large-3
step5_date: '2026-03-18T23:16:51.554418'
step5_model: Mistral-Large-3
step6_date: '2026-03-18T23:16:57.609644'
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
This paper investigates the practical performance of Quantum Amplitude Estimation (QAE) for pricing European call options, focusing on two near-term variants: Iterative Amplitude Estimation (IAE) and Maximum Likelihood Amplitude Estimation (MLAE). Using historical Apple market data, the study compares quantum estimates against classical benchmarks like Black-Scholes and Monte Carlo simulations to assess whether QAE can replicate classical pricing outcomes under current hardware constraints. The work highlights key limitations in encoding resolution and quantum circuit depth that affect accuracy in financial applications.
## Methodology
The study evaluates the performance of Quantum Amplitude Estimation (QAE) algorithms, specifically Iterative Amplitude Estimation (IAE) and Maximum Likelihood Amplitude Estimation (MLAE), for pricing European call options using historical Apple market data. The methodology involves a four-stage pipeline: (1) preprocessing historical market data to extract relevant features such as spot price, strike price, volatility, and risk-free rate; (2) modeling the terminal asset price using a log-normal distribution encoded into a quantum circuit via Qiskit's LogNormalDistribution; (3) encoding the European call option payoff function as a piecewise linear transformation using controlled rotations on an ancilla qubit; and (4) applying IAE and MLAE to estimate the expected payoff. The quantum results are benchmarked against classical methods, including the Black-Scholes (BS) model and Monte Carlo (MC) simulation, using the same discretized price space for fair comparison. The study highlights the impact of limited qubit resolution on the accuracy of quantum estimates, particularly in capturing low-probability, high-payoff events.

**Algorithms used:** Quantum Amplitude Estimation (QAE), Iterative Amplitude Estimation (IAE), Maximum Likelihood Amplitude Estimation (MLAE), Black-Scholes, Monte Carlo Simulation
**Frameworks:** Qiskit, Qiskit Finance

**Experimental setup:** Experiments were conducted using Qiskit on a quantum simulator. The setup included 6 uncertainty qubits to discretize the terminal asset price into 64 bins, 3 objective qubits for payoff approximation, and 3 ancilla qubits for conditional logic. IAE was configured with a maximum of 3 Grover iterations, precision of 0.01, and confidence level of 0.05. MLAE used an evaluation schedule of {0, 1, 3, 7}. Classical benchmarks were computed using a dot-product-based expected value (BS) and MC simulation with 100,000 samples. The study used historical Apple (AAPL) market data from January 2, 2022, to February 13, 2024, with parameters adjusted to simulate bullish market scenarios.

**Dataset:** Historical market data for Apple Inc. (AAPL) from January 2, 2022, to February 13, 2024, collected via the Yahoo Finance API. The dataset included spot price, strike price, implied volatility, time to maturity, and risk-free rate. Data was filtered for quality and maturity length, with a 5% shift applied to mean log returns and volatility clipped to a minimum of 0.20 to ensure realistic risk estimates.
## Findings
- [supported] Quantum Amplitude Estimation (QAE) variants (IAE and MLAE) returned an expected payoff of zero for European call options, while classical methods (Black-Scholes and Monte Carlo) yielded significantly positive values ($17.60 and $17.06 in two scenarios) [supported]
- [supported] The failure of QAE to capture non-zero expected payoffs is attributed to limited resolution from 6 uncertainty qubits (64 bins), which inadequately encodes small-amplitude, in-the-money price regions [supported]
- [supported] Quantum circuits correctly identified the realized market outcome (zero payoff) but failed to capture the full expectation implied by the distribution [supported]
- [supported] Classical benchmarks (Black-Scholes and Monte Carlo) aligned closely, with deviations below 1% in expected payoff estimates [supported]
- [speculative] Enhanced encoding strategies, such as non-uniform binning or adaptive state preparation, could improve QAE's ability to resolve low-probability, high-payoff events [speculative]
- [speculative] QAE may still offer utility in binary classification or threshold-detection tasks despite current limitations in expectation estimation [speculative]

**Results summary:** The study empirically evaluates Quantum Amplitude Estimation (QAE) for pricing European call options using historical Apple market data. Results from simulations show that QAE variants (IAE and MLAE) consistently returned an expected payoff of zero, failing to match classical benchmarks (Black-Scholes and Monte Carlo) that produced positive values. This discrepancy is traced to coarse discretization (6 qubits, 64 bins), which inadequately captures low-probability, in-the-money price regions. While quantum circuits correctly predicted the realized market outcome, they underperformed in estimating the full expected payoff, highlighting current limitations in resolution and encoding strategies for financial applications.

**Performance claims:**
- Expected payoff: $0.00 (IAE/MLAE) vs. $17.60 (Black-Scholes) and $17.83 (Monte Carlo) in 2023–2024 scenario
- Expected payoff: $0.00 (IAE/MLAE) vs. $17.06 (Black-Scholes) and $17.28 (Monte Carlo) in 2022–2023 scenario
- Asset price estimates: ~$185 (quantum) vs. ~$198 (classical) in 2023–2024 scenario
- Asset price estimates: ~$180 (quantum) vs. ~$192 (classical) in 2022–2023 scenario
- Monte Carlo deviation from Black-Scholes: <1% in expected payoff
## Quantum advantage claim
**Classification:** disputed

Theoretical quantum advantage (O(1/ε) scaling) is not demonstrated in practice due to resolution limitations. Results contradict the asymptotic advantage claim under current hardware constraints, as classical methods outperformed QAE in expectation estimation.
## Limitations
- Limited resolution due to only 6 uncertainty qubits (64 bins), which inadequately encodes small-amplitude, in-the-money price regions
- Failure to capture low-probability, high-payoff events that dominate the expected payoff, leading to zero-valued estimates despite classical methods yielding positive values
- Coarse discretization of the log-normal distribution, which misses subtle but financially significant amplitudes above the strike price
- No noise mitigation techniques applied, as experiments were conducted in a noiseless simulator [inferred]
- Limited Grover iterations (max 3 for IAE) may constrain the accuracy of amplitude estimation
- No comparison with other quantum amplitude estimation variants or hybrid quantum-classical approaches [inferred]
- Experiments conducted only on historical Apple (AAPL) data, limiting generalizability to other assets or market conditions [inferred]
- Fixed time to maturity (1 year) and strike price (5% above initial asset value) may not reflect diverse real-world scenarios [inferred]
- No evaluation of the impact of hardware noise or decoherence on algorithm performance [inferred]
- High gate count (e.g., 172,000 gates for IAE) may pose challenges for near-term quantum hardware [inferred]
## Open questions
- How can quantum amplitude estimation (QAE) be adapted to better resolve low-probability, high-payoff events with limited qubits?
- What encoding strategies (e.g., nonuniform binning, adaptive discretization) can improve the resolution of tail events in financial distributions?
- How does the performance of QAE variants (IAE, MLAE) scale with increased qubit counts and deeper circuits?
- What is the trade-off between circuit depth, qubit count, and estimation accuracy in real-world financial applications?
- Can hybrid quantum-classical approaches (e.g., variational methods) bridge the gap between current quantum capabilities and classical benchmarks?
- How do noise and decoherence affect the stability and accuracy of QAE in option pricing on near-term quantum hardware?
- What are the minimal qubit requirements for QAE to outperform classical methods in realistic financial scenarios?

**Future work:**
- Increase qubit counts to improve distribution resolution and capture low-probability events
- Explore advanced encoding schemes, such as nonuniform bin spacing around strike regions or variational encoding
- Test adaptive binning strategies to better resolve tail events in financial distributions
- Evaluate QAE performance on real quantum hardware with noise mitigation techniques
- Extend the pipeline to multi-asset options or more complex financial instruments
- Investigate hybrid quantum-classical approaches to enhance scalability and accuracy
- Benchmark QAE against other quantum algorithms (e.g., quantum Monte Carlo) for financial expectation tasks
- Assess the impact of hardware noise and decoherence on QAE performance in option pricing
- Develop targeted amplitude shaping techniques to improve the representation of small but significant payoff states
## Key ideas
- #idea:near-term-feasibility — QAE variants (IAE/MLAE) are evaluated for near-term applicability in option pricing, but current hardware constraints limit their effectiveness
- #idea:hybrid-approach — Speculative suggestion that hybrid quantum-classical approaches or advanced encoding strategies could improve QAE performance for financial applications
- #limitation:qubit-count — Limited to 6 uncertainty qubits (64 bins), which inadequately captures low-probability, high-payoff events critical for accurate option pricing
- #limitation:data-encoding — Coarse discretization of log-normal distributions fails to resolve subtle but financially significant amplitudes above the strike price
- #limitation:no-empirical-validation — Results are derived from noiseless simulations, with no evaluation of hardware noise or decoherence impacts
- #contradiction:classical-vs-quantum — QAE fails to match classical benchmarks (Black-Scholes/Monte Carlo) in expectation estimation, contradicting theoretical quantum advantage claims
## Contradictions
- This paper contradicts theoretical claims of quantum advantage for QAE in derivatives pricing by demonstrating that classical methods (Black-Scholes/Monte Carlo) outperform QAE under current hardware constraints. The zero-valued payoff estimates from QAE (vs. positive classical values) highlight scalability and resolution limitations that undermine asymptotic advantage arguments (e.g., O(1/ε) scaling). Related work (e.g., 2021_Rebentrost_QuantumAlgorithmsFinance) may assume idealized conditions not reflected in this empirical study.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
