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
journal_or_venue: QUEST-IS 2025, Communications in Computer and Information Science
  (CCIS 2743)
methodology_tags:
- amplitude-estimation
- classical-simulation
paper_type: ''
quantum_advantage_claim: theoretical
related_papers:
- 2021_Rebentrost_QuantumAlgorithmsFinance
relevance_phase1: high
relevance_phase3: high
source_type: peer-reviewed-empirical
source_type_confidence: high
step1_date: '2026-03-25T16:13:47.681880'
step1_model: gpt-5.1
step2_date: '2026-03-25T16:13:55.564398'
step2_model: gpt-5.1
step3_date: '2026-03-25T16:14:27.442739'
step3_model: gpt-5.4
step4_date: '2026-03-25T16:14:47.498840'
step4_model: gpt-5.4
step5_date: '2026-03-25T16:15:11.926788'
step5_model: gpt-5.4
step6_date: '2026-03-25T16:15:21.797815'
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
The paper investigates how practical variants of Quantum Amplitude Estimation, specifically Iterative Amplitude Estimation and Maximum Likelihood Amplitude Estimation, perform when used to price European call options on Apple stock using historical market data. The authors build a full Qiskit-based pipeline including log-normal state preparation, quantum payoff encoding, and amplitude estimation, and compare the quantum estimates to Black–Scholes and Monte Carlo benchmarks. They find that under realistic qubit and discretization constraints, the quantum methods systematically return zero expected payoff, highlighting limitations of current encoding resolution and the need for improved state-preparation strategies for financial applications.
## Methodology
The paper presents an empirical case study of European call option pricing using practical variants of Quantum Amplitude Estimation (QAE) and compares them against classical pricing methods. The authors build a Qiskit-based pipeline that starts from historical Apple (AAPL) market data, extracts option-pricing inputs including spot price, strike, volatility, maturity, and risk-free rate, and parameterizes a Black-Scholes-consistent log-normal model for terminal asset prices. The terminal price distribution is discretized into 2^n bins and encoded into a quantum state using Qiskit Finance's LogNormalDistribution. The European call payoff max(ST-K,0) is then mapped into amplitudes through Qiskit's LinearAmplitudeFunction using piecewise linear controlled rotations on an objective qubit, supported by ancilla qubits and a scaling factor to keep amplitudes in [0,1]. Two QAE variants, Iterative Amplitude Estimation (IAE) and Maximum Likelihood Amplitude Estimation (MLAE), are applied to estimate the amplitude corresponding to expected payoff. The resulting amplitude is rescaled to recover the expected payoff and compared with two classical baselines: an exact discretized Black-Scholes-style dot-product expectation and Monte Carlo simulation. Experiments are conducted in a simulated quantum environment under realistic qubit constraints, with analysis focused on whether QAE can reproduce classical option-pricing outputs and on identifying deviations caused by coarse discretization, limited Grover depth, and state-preparation resolution.

**Algorithms used:** Quantum Amplitude Estimation, Iterative Amplitude Estimation, Maximum Likelihood Amplitude Estimation, Black-Scholes, Monte Carlo simulation
**Frameworks:** Qiskit, Qiskit Finance, Yahoo Finance API, yfinance

**Experimental setup:** Experiments were run in a simulated quantum environment using Qiskit rather than on a real QPU. The option-pricing circuit used 6 uncertainty qubits to encode the terminal asset-price distribution into 64 bins, 3 objective qubits for payoff approximation, and 3 ancilla qubits for piecewise linear payoff logic. The study reports noiseless simulator conditions while noting transpilation overheads; circuit sizes mentioned include about 172,000 gates for IAE and 12,600 gates for MLAE. Classical reference computations included a discretized exact expectation and Monte Carlo with 100,000 samples.

**Dataset:** Historical Apple Inc. (AAPL) market and option-related data collected via the Yahoo Finance API, covering January 2, 2022 to February 13, 2024. Extracted features included spot price, strike price, implied volatility, time to maturity, and risk-free rate. The study evaluated two market scenarios derived from this period.
## Findings
- [supported] In two empirical AAPL European call option case studies, both Iterative Amplitude Estimation (IAE) and Maximum Likelihood Amplitude Estimation (MLAE) returned an expected payoff of 0.00 USD, while classical benchmarks produced positive expected payoffs.
- [supported] For the 2023–2024 scenario, the classical exact benchmark estimated a payoff of 17.5987 USD and Monte Carlo estimated 17.8259 USD, whereas both IAE and MLAE estimated 0.0000 USD.
- [supported] For the 2022–2023 scenario, the classical exact benchmark estimated a payoff of 17.0597 USD and Monte Carlo estimated 17.2799 USD, whereas both IAE and MLAE estimated 0.0000 USD.
- [supported] Monte Carlo results with 100,000 samples were within about 1% of the classical exact discretized benchmark in both scenarios.
- [supported] Quantum-estimated asset prices were systematically lower than classical estimates: 185.3681 USD vs 198.0063 USD exact (and 198.1746 USD MC) in 2023–2024, and about 179.69 USD vs 191.9414 USD exact (and 192.1046 USD MC) in 2022–2023.
- [supported] The paper attributes the quantum underestimation to coarse state encoding with 6 uncertainty qubits (64 bins), which failed to resolve low-probability in-the-money tail events that materially contribute to expected payoff.
- [supported] The experiments were conducted in a simulated quantum environment using Qiskit rather than on real quantum hardware.
- [supported] Even under noiseless simulation and expressive compiled circuits, the main limitation was the encoded probability landscape rather than circuit depth; the paper reports transpiled circuit sizes of about 172,000 gates for IAE and 12,600 gates for MLAE.
- [supported] Both IAE and MLAE matched the realized market outcome of zero payoff in the tested cases, suggesting usefulness for binary threshold or event-detection tasks under coarse resolution.
- [speculative] The authors argue that improved encoding strategies such as more qubits, nonuniform/adaptive binning near the strike, or variational encoding could improve QAE performance for financial expectation estimation.
- [speculative] The theoretical quadratic speedup of QAE over classical Monte Carlo is acknowledged, but this advantage was not realized in the reported practical experiments.

**Results summary:** This peer-reviewed empirical study evaluates QAE-based option pricing on historical Apple (AAPL) data using Qiskit simulation, comparing IAE and MLAE against classical exact discretized pricing and Monte Carlo. In two one-year European call option scenarios with strike set 5% above the initial asset price, classical methods estimated positive expected payoffs of about 17.06–17.83 USD, while both quantum estimators returned 0.00 USD in all cases. Monte Carlo with 100,000 samples closely matched the classical exact benchmark, deviating by less than 1%. The authors conclude that the failure of QAE in these experiments is due to limited resolution from using only 6 uncertainty qubits (64 bins), which cannot adequately encode low-probability but financially important in-the-money tail events. Results are from noiseless simulation, not real hardware, and the paper presents these findings as evidence of current practical limitations rather than quantum advantage.

**Performance claims:**
- 2023–2024 scenario: Classical exact expected payoff = 17.5987 USD; Monte Carlo = 17.8259 USD; IAE = 0.0000 USD; MLAE = 0.0000 USD
- 2023–2024 scenario asset price estimates: Classical exact = 198.0063 USD; Monte Carlo = 198.1746 USD; IAE = 185.3681 USD; MLAE = 185.3681 USD
- 2022–2023 scenario: Classical exact expected payoff = 17.0597 USD; Monte Carlo = 17.2799 USD; IAE = 0.0000 USD; MLAE = 0.0000 USD
- 2022–2023 scenario asset price estimates: Classical exact = 191.9414 USD; Monte Carlo = 192.1046 USD; IAE = 179.6903 USD; MLAE = 179.6749 USD
- Monte Carlo used 100,000 samples and deviated by less than 1% from the classical exact benchmark
- Quantum encoding used 6 uncertainty qubits (64 bins), 3 objective qubits, and 3 ancilla qubits
- IAE configuration: precision = 0.01, confidence level alpha = 0.05, maximum 3 Grover iterations
- MLAE evaluation schedule: {0, 1, 3, 7}
- Reported transpiled circuit sizes: about 172,000 gates for IAE and 12,600 gates for MLAE
## Quantum advantage claim
**Classification:** theoretical

The paper references the theoretical quadratic speedup of QAE over classical Monte Carlo, but its own empirical results are simulation-based and show no practical advantage; instead, QAE underperformed classical methods in the tested option-pricing cases.
## Limitations
- Six uncertainty qubits (64 bins) provide insufficient distribution resolution to capture low-probability in-the-money tail events, causing both IAE and MLAE to return zero expected payoff.
- Limited iteration counts in amplitude estimation (IAE max 3 Grover iterations; MLAE schedule {0,1,3,7}) constrain estimation precision.
- Experiments were conducted in a simulated quantum environment rather than on real quantum hardware, so hardware noise, decoherence, and calibration effects were excluded.
- The study uses only a single underlying asset (AAPL) and two historical scenarios, limiting generalizability across assets, regimes, and option types.
- Only a subset of the historical data was used after filtering by data quality and maturity length, narrowing empirical coverage.
- The terminal price distribution is assumed log-normal and aligned with Black-Scholes assumptions, which may not hold in real markets.
- The support of the distribution is truncated to three standard deviations around the mean, which may omit relevant tail mass for option pricing.
- The payoff is approximated via a piecewise linear mapping and scaled into [0,1], introducing approximation error.
- The market setup includes hand-crafted preprocessing choices such as a +5% shift to mean log returns and a volatility floor of 0.20, which may affect internal validity.
- Classical benchmarking uses the same discretized price space for direct comparison, which may not fully reflect continuous-model benchmark performance.
- The study evaluates only European call options with one-year maturity and strike fixed at 5% above spot, limiting scope.
- Although transpilation overhead is considered, the reported circuits are very large (e.g., IAE with 172,000 gates), raising concerns about feasibility on near-term hardware.
- [inferred] No experiments assess sensitivity to qubit count, binning strategy, or objective-qubit precision beyond the single chosen configuration.
- [inferred] No comparison is provided against state-of-the-art classical variance-reduction or advanced numerical pricing methods beyond Black-Scholes and standard Monte Carlo.
- [inferred] Reproducibility may be limited because the paper does not report full implementation details such as random seeds, exact filtered dataset instances, or complete circuit/transpilation settings.
- [inferred] Scalability to production financial workloads is unproven, especially for larger asset universes, more complex derivatives, or real-time pricing requirements.
- [inferred] The empirical evaluation is based on a very small sample of scenarios, so conclusions about QAE performance may be unstable across different market conditions.
## Open questions
- How many uncertainty qubits are needed before QAE-based option pricing begins to align with classical expected-payoff estimates?
- Can nonuniform or adaptive binning around the strike resolve low-probability but financially significant tail events more effectively than uniform discretization?
- Would alternative state-preparation or payoff-encoding strategies allow IAE and MLAE to recover nonzero expected payoffs under realistic qubit budgets?
- How robust are IAE and MLAE to real hardware noise when applied to option pricing circuits of this size?
- Can QAE methods provide practical advantage for expectation estimation in finance before fault-tolerant quantum hardware becomes available?
- Are QAE methods more suitable for binary event detection or threshold classification than for full expectation estimation in near-term financial applications?
- How sensitive are the results to modeling assumptions such as log-normal returns, volatility clipping, and the imposed bullish return shift?
- Would increasing objective qubits or changing payoff approximation schemes materially improve pricing accuracy?
- How do the findings extend to other assets, maturities, strikes, and option classes such as puts, American options, or path-dependent derivatives?
- What is the trade-off between circuit depth, qubit count, and estimation accuracy for financially relevant tail-sensitive payoffs?

**Future work:**
- Increase qubit counts to obtain finer amplitude granularity and better resolve in-the-money tail regions.
- Develop enhanced state-preparation and payoff-mapping methods to better capture low-amplitude but significant payoff states.
- Use nonuniform or adaptive bin spacing, especially around strike regions, to improve tail-event resolution.
- Explore variational encoding strategies for more expressive and efficient distribution representation.
- Benchmark future QAE improvements using the presented pipeline as a testbed.
- Test the methods under more realistic hardware conditions, including noise and device constraints.
- Investigate targeted amplitude distributions or amplitude shaping techniques to improve expectation recovery.
- Extend the approach toward accurate and scalable quantum financial analytics as quantum technology matures.
- [inferred] Perform systematic ablation studies over uncertainty qubits, objective qubits, Grover schedules, and payoff-scaling choices.
- [inferred] Validate on broader datasets spanning multiple assets, market regimes, and derivative products.
- [inferred] Compare against stronger classical baselines and hybrid quantum-classical methods to better assess practical value.
- [inferred] Evaluate execution on real quantum hardware with error mitigation to determine whether simulator findings persist in practice.
## Key ideas
- #idea:near-term-feasibility — Practical QAE variants (IAE and MLAE) were tested for European call option pricing on AAPL, but under realistic qubit/discretization limits they failed to recover nonzero expected payoffs.
- #idea:hybrid-approach — The paper suggests improved encoding strategies such as adaptive/nonuniform binning or variational encoding as a practical path to make quantum expectation estimation more useful.
- #contradiction:classical-vs-quantum — In both empirical scenarios, QAE returned 0.00 USD expected payoff while classical exact and Monte Carlo benchmarks produced positive values around 17 USD, directly undermining practical quantum superiority claims.
- #contradiction:scalability — Even in noiseless simulation with only a single-asset European call setup, coarse encoding and large compiled circuits prevented accurate pricing, casting doubt on scaling to realistic derivatives workloads.
## Contradictions
- The paper contradicts practical quantum-advantage narratives for derivatives pricing: despite the theoretical quadratic speedup of amplitude estimation over Monte Carlo, its own QAE pipeline underperformed classical exact and Monte Carlo baselines, returning zero payoff estimates in both AAPL case studies.
- The findings challenge idealized finance papers such as 2021_Rebentrost_QuantumAlgorithmsFinance by showing that asymptotic QAE advantages do not survive realistic state-preparation and discretization constraints in a concrete option-pricing workflow.
- The paper also contradicts implicit scalability claims: if QAE fails on a small, single-asset European call problem under noiseless simulation, then extension to larger or more complex derivatives appears unproven.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->

## Experiment details
### Input
Input data consisted of historical AAPL data from Yahoo Finance/yfinance over 2022-01-02 to 2024-02-13. Features used were spot price S, strike price K, implied volatility sigma, time to maturity T, and risk-free rate r. Data were filtered by quality and maturity length. A 5% upward shift was applied to mean log returns to simulate a bullish scenario, and volatility was clipped to a minimum of 0.20. Time to maturity was fixed at 1 year, and strike price was set to 5% above the initial asset value. The terminal asset-price distribution was modeled as log-normal and truncated to a support spanning three standard deviations around the mean, then discretized into 64 bins using 6 uncertainty qubits.

### Process
1. Collect and preprocess AAPL historical market data and derive option-pricing inputs. 2. Parameterize a Black-Scholes-consistent log-normal terminal price distribution using S, sigma, r, and T. 3. Truncate the support to [Smin, Smax] over roughly three standard deviations around the mean. 4. Discretize the distribution into 2^6 = 64 bins and encode it into a quantum state using LogNormalDistribution. 5. Encode the European call payoff max(ST-K,0) with LinearAmplitudeFunction as a piecewise linear controlled-rotation mapping onto objective qubits, with ancilla support and scaling to [0,1]. 6. Apply IAE with target precision 0.01, confidence level alpha = 0.05, and maximum 3 Grover iterations to estimate the payoff amplitude. 7. Apply MLAE on the same circuit using Grover power schedule {0,1,3,7} and classical maximum-likelihood inference. 8. Rescale the estimated amplitude to recover expected payoff. 9. Compute classical baselines using a discretized exact dot-product expectation and Monte Carlo simulation with 100,000 samples on the same discretized price space. 10. Compare expected payoff and estimated asset price outputs across two AAPL scenarios.

### Output
Outputs included expected payoff estimates in USD and estimated asset prices for two AAPL scenarios, along with comparisons to classical exact/discretized Black-Scholes-style values and Monte Carlo estimates. Reported results showed classical expected payoffs of about 17.60 USD and 17.06 USD in the two scenarios, Monte Carlo values within 1% of those references, and both IAE and MLAE returning 0.00 expected payoff in both cases. Asset price estimates were also reported, with classical values near 198 and 192 USD versus quantum estimates around 185 and 179 USD. The main evaluation focus was agreement or deviation relative to classical baselines and interpretation of underestimation due to coarse amplitude resolution.

### Parameters
- assets: ['AAPL']
- date_range: 2022-01-02 to 2024-02-13
- return_shift: +5% mean log returns
- min_volatility: 0.2
- maturity_time: 1 year
- strike_price: 5% above initial asset value
- uncertainty_qubits: 6
- price_bins: 64
- objective_qubits: 3
- ancilla_qubits: 3
- iae_precision: 0.01
- iae_confidence_level_alpha: 0.05
- iae_max_grover_iterations: 3
- mlae_schedule: [0, 1, 3, 7]
- mc_samples: 100000
- mc_passes: single run per trial

### Hardware
Quantum experiments were performed on a noiseless Qiskit simulator rather than real quantum hardware. The paper does not specify a simulator backend name such as Aer statevector or qasm simulator, but explicitly states that noise and hardware effects were excluded while transpilation overheads were considered. No QPU model or cloud provider is reported.

### Reproducibility
Data source is public (Yahoo Finance/yfinance), and the paper provides substantial methodological detail on the pipeline, qubit allocation, and key hyperparameters. However, no code repository or full implementation details are provided, and some simulator/backend and transpilation specifics are omitted. Replication appears partially feasible but not fully turnkey.
