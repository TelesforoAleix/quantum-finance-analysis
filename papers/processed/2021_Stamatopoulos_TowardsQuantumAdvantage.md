---
aliases:
- Towards Quantum Advantage in Financial Market Risk using Quantum Gradient Algorithms
- Towards Quantum Advantage Financial
authors:
- Nikitas Stamatopoulos
- Guglielmo Mazzola
- Stefan Woerner
- William J. Zeng
auto_detected: true
classification: ''
contradiction_flags:
- contradiction:scalability
- contradiction:classical-vs-quantum
doi: ''
evidence_type: ''
idea_tags:
- idea:quantum-advantage
- idea:hybrid-approach
journal_or_venue: Quantum
methodology_tags:
- amplitude-estimation
- quantum-simulation
- classical-simulation
paper_type: ''
quantum_advantage_claim: theoretical
related_papers: []
relevance_phase1: high
relevance_phase3: high
source_type: peer-reviewed-empirical
source_type_confidence: high
step1_date: '2026-03-25T15:56:12.741396'
step1_model: gpt-5.1
step2_date: '2026-03-25T15:56:17.341710'
step2_model: gpt-5.1
step3_date: '2026-03-25T15:57:11.272539'
step3_model: gpt-5.4
step4_date: '2026-03-25T15:57:57.612806'
step4_model: gpt-5.4
step5_date: '2026-03-25T15:58:31.014711'
step5_model: gpt-5.4
step6_date: '2026-03-25T15:58:44.143023'
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
- method/quantum-simulation
- method/classical-simulation
- idea/quantum-advantage
- idea/hybrid-approach
- contradiction/scalability
- contradiction/classical-vs-quantum
title: Towards Quantum Advantage in Financial Market Risk using Quantum Gradient Algorithms
topic_tags:
- derivatives-pricing
- risk-modelling
year: 2022
zotero_key: ''
---

## Abstract summary
The paper develops and analyzes quantum algorithms for computing market risk measures (greeks) of financial derivatives using quantum gradient estimation techniques. Building on quantum amplitude estimation–based pricing, the authors show how quantum gradient methods can yield additional quadratic improvements in scaling with the number of greeks compared to classical and semi-classical finite-difference approaches, and they numerically study resource requirements on vanilla and path-dependent options. They also introduce a simulation-free second-order quantum gradient construction, combine it with maximum likelihood estimation for tighter confidence intervals, and update prior resource estimates, arguing that quantum advantage for risk calculations could be achieved with substantially lower logical clock rates than those needed for pricing alone.
## Methodology
The paper presents a peer-reviewed empirical and algorithmic study of quantum methods for computing financial market risk (greeks) of derivatives. The authors extend quantum derivative pricing based on quantum amplitude estimation (QAE) by incorporating quantum gradient estimation methods, primarily Jordan’s gradient algorithm, the higher-order Gilyén-Arunachalam-Wiebe (GAW) framework, and a newly proposed Simulation-Free Quantum Gradient (SFQG) method. The methodology combines theoretical complexity analysis with numerical emulation of quantum circuits for practical derivative contracts. Two financial case studies are used: (1) a European call option under the Black-Scholes-Merton model with closed-form price and exact greeks for benchmarking, and (2) a path-dependent basket knock-in option on three assets priced via Monte Carlo as a realistic practical use case without closed-form solution. Because full circuit simulation is too costly, the authors emulate the quantum gradient algorithm by classically constructing the phase-encoded amplitude array, applying a classical inverse Fourier transform, and sampling the resulting probability distribution; Hamiltonian simulation phase error is modeled by adding uniform random phase perturbations. They compare quantum gradient methods against classical finite-difference Monte Carlo, classical finite difference with common random numbers (CRN), and semi-classical quantum finite-difference methods using QAE. Evaluation focuses on oracle/query complexity, success probability of estimating greeks within target additive error, parameter choices such as finite-difference order and spacing, and resource estimates including T-depth, logical qubits, and logical clock-rate thresholds for quantum advantage. They also apply maximum likelihood estimation (MLE) as a classical post-processing step to improve gradient readout and derive confidence intervals.

**Algorithms used:** Quantum Amplitude Estimation, Jordan's quantum gradient algorithm, GAW quantum gradient algorithm, Simulation-Free Quantum Gradient, Maximum Likelihood Estimation, Classical finite difference, Classical finite difference with common random numbers, Semi-classical quantum gradient, Hamiltonian simulation, Automatic differentiation, Multi-objective QAE

**Experimental setup:** Experiments are numerical simulations/emulations rather than runs on real quantum hardware. The authors emulate quantum gradient estimation by classically initializing the phase-encoded state amplitudes for k*2^n grid points, applying a classical inverse Fourier transform, and analyzing the resulting output probability distribution before measurement. For GAW simulations, Hamiltonian simulation phase error is injected as a random perturbation uniformly sampled from [-epsilon_phase, epsilon_phase]. Resource estimation also includes logical-level fault-tolerant cost analysis (T-depth, logical qubits, logical clock rate) based on oracle constructions from prior derivative pricing work.

**Dataset:** Synthetic/model-based financial data generated from analytical and stochastic derivative pricing models rather than an external dataset. Case studies include a European call option under Black-Scholes-Merton and a path-dependent basket knock-in option on three assets undergoing geometric Brownian motion. For the basket option, Monte Carlo simulation with 10^6 paths is used to estimate benchmark prices/greeks.
## Findings
- [supported] Numerical simulations of quantum gradient estimation on a European call option and a path-dependent basket option successfully estimated greeks with at least 85% probability at the target discretization errors studied.
- [supported] For the vanilla option, numerically optimized GAW parameters reduced query complexity far below theorem-based estimates: for k=4 greeks and target error ϵ=2×10^-2, numerical query cost was 4,904 oracle calls versus 833,296 from the theoretical parameter choice.
- [supported] For the vanilla option, the practical spacing parameter l could be increased by more than two orders of magnitude relative to theorem-based settings, contributing to an approximately 200× lower query complexity than theoretical estimates.
- [supported] For the path-dependent basket option with four greeks and target error ϵ≤0.0625, the numerically simulated GAW method required 1,600 oracle calls, versus 201,528 implied by theorem-based settings, about 125× lower.
- [supported] For the same basket-option task, the Simulation-Free Quantum Gradient (SFQG) method required 201 oracle calls, lower than semi-classical quantum gradients (256), GAW numerical simulation (1,600), CFD-CRN (32,000 Monte Carlo paths), and CFD (400,000 Monte Carlo paths).
- [supported] The paper introduces an explicit second-order accurate Simulation-Free Quantum Gradient method that avoids block encoding and Hamiltonian simulation and is empirically cheaper to construct than the Hamiltonian-based method for the studied derivative case.
- [supported] Maximum likelihood estimation (MLE) post-processing improved gradient extraction and provided concrete confidence intervals; in the illustrated basket-option example, using 30 accepted samples yielded an estimate error of about 4×10^-3 despite a grid spacing of 0.0625.
- [supported] Using SFQG plus MLE, the estimated total T-depth for computing four greeks to error ϵ≤2×10^-3 at confidence level 0.68 was 5.5×10^7, with about 12,000 logical qubits and code distance sufficient for 10^8 logical operations.
- [supported] Based on these resource estimates, the required logical clock rate for quantum advantage in the studied market-risk task drops from 50 MHz for pricing alone to about 7 MHz for four-greek risk computation, a factor of about 7 reduction.
- [supported] If 60 QPUs are available in parallel, the authors estimate the same overall runtime could be achieved with about 100 kHz logical clock rate per device for the studied task.
- [speculative] The authors argue that quantum gradient methods can provide an additional quadratic advantage in the number of greeks, improving from O(k/ϵ) semi-classical scaling to O(√k/ϵ) under smoothness conditions.
- [speculative] The paper claims a quadratic error-scaling advantage in market-risk computation inherited from amplitude estimation, relative to classical Monte Carlo scaling.
- [speculative] The authors suggest practical derivative pricing functions may be smoother than the worst-case class used in Theorem 1, potentially enabling better-than-theorem resource behavior in finance applications.
- [speculative] The paper suggests that for some smoother functions, scaling better than O(√k/ϵ) may be possible, and mentions an upper-bound speedup of O(k) over classical Monte Carlo in favorable polynomial-like cases.
- [speculative] The appendix proposes that combining automatic differentiation with multi-objective QAE could yield runtime independent of gradient dimension k, but this is not empirically validated in the paper.

**Results summary:** This peer-reviewed empirical paper studies quantum algorithms for computing market-risk sensitivities (greeks) of financial derivatives, with results obtained from numerical simulation rather than real quantum hardware. The authors benchmark several methods: classical finite differences, classical finite differences with common random numbers, semi-classical quantum gradients based on amplitude estimation, the GAW quantum gradient algorithm, and a new Simulation-Free Quantum Gradient (SFQG) method. In simulated experiments on a European call option and a path-dependent basket option, the quantum gradient methods estimated greeks with at least 85% success probability at the target errors considered. For the vanilla option, practical GAW resource requirements were dramatically smaller than theorem-based estimates; for k=4 greeks at error 2×10^-2, 4,904 oracle calls were needed numerically versus 833,296 from theoretical settings. For the basket option with four greeks at error at most 0.0625, GAW required 1,600 oracle calls numerically, while SFQG required only 201, compared with 256 for semi-classical quantum gradients and 32,000 for the best classical finite-difference baseline with common random numbers. The paper further shows that MLE post-processing can sharpen estimates and provide confidence intervals. Using these simulated algorithmic results plus fault-tolerant resource estimation, the authors estimate that quantum advantage for the studied risk task could require about 5.5×10^7 T-depth, around 12,000 logical qubits, and a logical clock rate of about 7 MHz, or about 100 kHz per device if parallelized across 60 QPUs.

**Performance claims:**
- Classical finite difference complexity: O(k/ϵ^3)
- Classical finite difference with common random numbers complexity: O(k/ϵ^2)
- Semi-classical quantum gradient complexity: O(k/ϵ)
- Jordan/GAW low-order quantum gradient complexity: O(√k/ϵ^2)
- GAW higher-order quantum gradient complexity under smoothness assumptions: O(√k/ϵ)
- Asymptotic benchmark for k=1000 greeks and ϵ=10^-3: classical finite difference 10^12 oracle calls, CFD-CRN 10^9, semi-classical 10^6, GAW 10^7
- Vanilla option, k=2: numerical GAW m=1, l=0.65, 1,976 oracle calls vs theoretical m=5, l=0.0028, 570,592 oracle calls
- Vanilla option, k=3: numerical GAW m=3, l=0.65, 4,664 oracle calls vs theoretical m=5, l=0.0022, 712,008 oracle calls
- Vanilla option, k=4: numerical GAW m=3, l=0.58, 4,904 oracle calls vs theoretical m=5, l=0.0019, 833,296 oracle calls
- Vanilla option target: ϵ=2×10^-2 with probability ≥85%
- Basket option GAW numerical: 1,600 oracle calls, m=1, l=0.25, for four greeks with ϵ≤0.0625 and probability ≥85%
- Basket option GAW theoretical: 201,528 oracle calls, m=4, l=0.0018
- Basket option SFQG: 201 oracle calls, m=1, l=0.25
- Basket option semi-classical quantum gradient: 256 oracle calls
- Basket option CFD-CRN: 32,000 Monte Carlo paths
- Basket option CFD: 400,000 Monte Carlo paths
- For the basket option, numerical GAW query complexity is about 125× smaller than theorem-based estimates
- For the basket option, SFQG query complexity is about 20× smaller than the best classical finite-difference baseline (32,000 vs 201, or about 10× if doubling for the method's 50% discard probability)
- MLE example on basket-option vega: estimate error about 4×10^-3 using 30 accepted samples, despite grid spacing 0.0625
- SFQG with MLE for four greeks at ϵ≤2×10^-3 and confidence level 0.68: total T-depth 5.5×10^7
- Estimated logical qubits for the above SFQG resource estimate: 12,000
- Required code distance supports about 10^8 logical operations
- Estimated logical clock rate for quantum advantage in the studied risk task: 7 MHz, down from 50 MHz for pricing-only estimates
- Parallelization across up to 60 QPUs could reduce required per-device logical clock rate to about 100 kHz
## Quantum advantage claim
**Classification:** theoretical

The paper makes explicit quantum advantage claims in complexity and fault-tolerant resource estimates, including quadratic improvements in error scaling and in the number of greeks under smoothness assumptions, plus lower estimated clock-rate thresholds for financial risk tasks. However, the evidence is based on numerical simulation and resource estimation rather than execution on real quantum hardware, so advantage is not empirically demonstrated.
## Limitations
- Numerical validation is limited to only two example derivatives: a European call option and a path-dependent basket option, which may not generalize to the broader range of financial products used in practice.
- The practical simulations of the quantum gradient algorithms are restricted to at most k = 4 greeks for realistic use cases due to the computational cost of classically emulating the quantum circuits.
- The authors explicitly note that for most relevant financial models of interest, closed-form solutions are unavailable, so they cannot verify whether the smoothness assumptions required by Theorem 1 hold.
- Resource estimates for the GAW method assume the smoothness conditions of Theorem 1 with smoothness parameter c = 1 as a best-case scenario, which may be overly optimistic for real financial pricing functions.
- The asymptotic theoretical analysis is based on bounds and parameter choices that the authors acknowledge may be loose in practice and highly dependent on function smoothness.
- The path-dependent basket option benchmarks use classical Monte Carlo with 10^6 paths to define reference gradients rather than exact analytical values, so the validation target itself is approximate.
- The simulation-free quantum gradient (SFQG) method has an inherent 50% shot discard rate due to unwanted terms in the constructed state, increasing effective sampling cost.
- The SFQG method as presented only provides a second-order accurate construction (m = 1), not the higher-order phase oracles needed to guarantee the full O(sqrt(k)/epsilon) scaling more generally.
- The updated quantum advantage estimates rely on logical-resource assumptions such as 7 MHz clock rates, 12k logical qubits, and error-corrected execution, which are far beyond current hardware capabilities.
- The paper's evidence for quantum advantage is based on numerical simulation and logical resource estimation rather than execution on real quantum hardware.
- [inferred] No experiments are performed on noisy NISQ hardware, so the impact of decoherence, gate errors, crosstalk, and readout noise on gradient estimation performance is untested.
- [inferred] No noise-mitigation or fault-tolerance overhead sensitivity analysis is provided beyond logical-level estimates, limiting internal validity of the claimed practical advantage.
- [inferred] Scalability to production settings is uncertain because practical market risk systems often require hundreds or thousands of greeks, whereas the empirical demonstrations only cover up to four.
- [inferred] Reproducibility may be limited because the study depends on numerical emulation choices, oracle constructions, and financial contract parameterizations that may be difficult to replicate exactly without code and implementation details.
- [inferred] Comparisons against classical methods are limited; while finite-difference and CRN baselines are included, there is no full empirical benchmark against state-of-the-art industrial adjoint algorithmic differentiation pipelines.
- [inferred] The classical runtime comparison assumes derivative pricing by Monte Carlo in about 1 second and greeks via second-order finite differences, which may not reflect optimized production risk engines.
## Open questions
- Which classes of practical financial derivatives satisfy the smoothness conditions required for the GAW quantum gradient algorithm to achieve the claimed O(sqrt(k)/epsilon) scaling?
- How does the practical scaling of the GAW algorithm behave for much larger numbers of greeks, such as the hundreds or thousands encountered in industry?
- Can the simulation-free construction be extended to higher-order phase oracles (m > 1) so that it applies more generally while retaining lower resource costs?
- To what extent can quantum gradient methods outperform classical adjoint automatic differentiation methods in realistic financial workloads?
- How much quantum speedup is achievable for different derivative price functions, given that the advantage appears highly dependent on problem structure and smoothness?
- Can additional quantum advantage be obtained for higher-level risk tasks beyond greeks, such as portfolio value-at-risk and other aggregation calculations?
- What are the true end-to-end resource requirements once full fault-tolerant overheads and realistic hardware constraints are incorporated?
- [inferred] How robust are the proposed algorithms to realistic hardware noise and imperfect oracle implementations on actual quantum devices?
- [inferred] Will the favorable numerical behavior observed for small examples persist for more complex contracts, richer stochastic models, and real market data distributions?

**Future work:**
- Study in more detail whether and which practical financial derivatives satisfy the smoothness conditions underlying the quantum gradient speedup guarantees.
- Extend the simulation-free phase-oracle construction to higher-order methods (m > 1).
- Perform a detailed comparison between quantum gradient algorithms and classical automatic differentiation methods.
- Investigate the quantum automatic differentiation construct proposed in Appendix B, including its memory requirements and how to automate reversible quantum arithmetic differentiation.
- Explore the use of quantum gradient and pricing subroutines for higher-level financial risk metrics such as portfolio value-at-risk.
- Analyze scaling to larger-dimensional gradient problems with many more greeks relevant to production market risk.
- Refine resource estimates using more realistic models of derivative price-function structure and cross-dependence.
- [inferred] Validate the proposed methods on real or realistic fault-tolerant hardware stacks once available, including noise-aware implementations.
- [inferred] Benchmark against stronger industrial classical baselines, especially adjoint algorithmic differentiation and optimized risk engines.
- [inferred] Test the methods on a broader set of derivative contracts and market models to assess generalizability.
## Key ideas
- #idea:quantum-advantage — The paper extends amplitude-estimation-based derivative pricing to compute greeks, claiming quadratic improvement in error scaling and an additional advantage in the number of greeks under smoothness assumptions.
- #idea:quantum-advantage — A new Simulation-Free Quantum Gradient construction avoids Hamiltonian simulation/block encoding overhead and is numerically cheaper than the studied Hamiltonian-based gradient method on the basket-option case.
- #idea:hybrid-approach — Classical maximum-likelihood post-processing is combined with quantum gradient outputs to sharpen estimates and confidence intervals.
- #idea:quantum-advantage — Fault-tolerant resource estimates suggest lower logical clock-rate thresholds for risk calculations than for pricing alone, with a reported drop from about 50 MHz to 7 MHz for the studied task.
## Contradictions
- The paper claims quantum advantage over classical risk computation, but the evidence is based on classical emulation and logical resource estimates rather than execution on real quantum hardware, weakening the superiority claim.
- Theoretical scaling claims rely on smoothness assumptions that the authors cannot verify for most practical derivatives, creating tension between asymptotic advantage claims and applicability to real financial products.
- Although the paper argues for favorable scaling in the number of greeks, empirical demonstrations only cover up to k=4, so the claimed scalability to industry-scale hundreds or thousands of greeks remains unvalidated.
- The paper reports quantum improvements relative mainly to finite-difference baselines, but it does not empirically benchmark against strong industrial adjoint/automatic-differentiation pipelines, so the practical classical-vs-quantum comparison is incomplete.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->

## Experiment details
### Input
Two main inputs were used. (1) Vanilla European call option under Black-Scholes-Merton with parameters evaluated at (S, r, sigma, T) = (99.5, 1%, 20%, 0.1) and strike K = 100; greeks studied were delta, rho, vega, and theta. Target gradient error was epsilon = 2e-2, requiring n = 6 qubits per gradient dimension. (2) Path-dependent basket knock-in option on three GBM assets with spot prices (2.0, 2.0, 2.0), volatilities (20%, 20%, 10%), risk-free rate 1%, maturity T = 3 years, basket weights (0.5, 0.3, 0.2), five observation dates t_B = [T/5 * i] for i = 1..5, strike K = 1.0, barrier B = 2.5. Greeks studied were the three deltas and vega with respect to the first asset. Since no closed form exists, benchmark values were estimated using classical Monte Carlo with 10^6 paths. For classical baseline estimation in one section, 3000 Monte Carlo replications were used to search for path counts achieving the target confidence/error.

### Process
The experimental process consisted of: (1) defining derivative pricing functions and target greeks; (2) constructing or analyzing quantum pricing oracles based on QAE; (3) for GAW, selecting finite-difference order m and spacing l, then emulating the quantum gradient algorithm by classically computing the phase-encoded amplitudes over a discretized hypercube, applying a classical inverse Fourier transform, and obtaining the output probability distribution; (4) injecting Hamiltonian simulation error by adding random phase noise uniformly in [-epsilon_phase, epsilon_phase]; (5) searching over m and l to find the largest spacing and lowest oracle cost that still achieved an epsilon-close estimate with at least 85% success probability for each greek; (6) comparing numerical query complexity against theoretical GAW bounds and against classical finite difference, CRN, and semi-classical QAE-based finite difference; (7) for SFQG, constructing a second-order m = 1 phase oracle directly from pricing oracles without block encoding/Hamiltonian simulation, simulating the resulting distribution, and accounting for a 50% discard rate due to unwanted branches; (8) applying maximum likelihood estimation to repeated circuit samples to refine gradient estimates and derive confidence intervals; and (9) translating oracle/query counts into fault-tolerant resource estimates such as T-depth, logical qubits, and required logical clock rates. Key settings reported include epsilon_phase = 1e-4 for GAW simulations, success threshold >= 85%, and MLE using 30 accepted samples (60 expected shots for SFQG due to 50% discard probability) in one resource-estimation example.

### Output
Outputs include estimated greek probability distributions, success probabilities, oracle/query complexity counts, optimal algorithm parameters (finite-difference order m and spacing l), and logical resource estimates. Metrics reported include additive gradient error epsilon, probability of obtaining an epsilon-close estimate (typically >= 85%), number of oracle calls/query complexity No, comparison to theoretical asymptotic bounds, and comparison against classical finite difference, classical finite difference with CRN, and semi-classical quantum gradient baselines. For resource estimation, outputs also include T-depth, logical qubit counts, code-distance-supported logical operations, and required logical clock rates for quantum advantage. MLE outputs include refined point estimates and confidence intervals at specified confidence levels.

### Parameters
- GAW_hamiltonian_phase_error: 0.0001
- vanilla_option_target_error: 0.02
- vanilla_option_qubits_per_dimension: 6
- vanilla_option_success_probability_threshold: 0.85
- basket_option_target_error: 0.0625
- basket_option_qubits_per_dimension: 4
- basket_option_success_probability_threshold: 0.85
- GAW_vanilla_numerical_parameters: {'k_2': {'m': 1, 'l': 0.65, 'No': 1976}, 'k_3': {'m': 3, 'l': 0.65, 'No': 4664}, 'k_4': {'m': 3, 'l': 0.58, 'No': 4904}}
- basket_option_parameters: {'GAW_numerical': {'m': 1, 'l': 0.25, 'No': 1600}, 'GAW_theoretical': {'m': 4, 'l': 0.0018, 'No': 201528}, 'SFQG': {'m': 1, 'l': 0.25, 'No': 201}, 'SQG': {'No': 256}, 'CFD_CRN': {'No': 32000}, 'CFD': {'No': 400000}}
- MLE_parameters: {'accepted_samples_example': 30, 'expected_total_shots_SFQG_example': 60, 'confidence_level_example': 0.68, 'target_error_example': 0.002}
- resource_estimation: {'pricing_clock_rate_prior_work_MHz': 50, 'risk_clock_rate_estimate_MHz': 7, 'parallel_QPUs': 60, 'parallel_clock_rate_estimate_kHz': 100, 'SFQG_total_T_depth_times_shots': 55000000, 'logical_qubits': 12000, 'logical_operations_supported': 100000000}

### Hardware
{'hardware_type': 'Classical numerical simulation/emulation; no real QPU used', 'simulator_description': 'Custom classical emulation of quantum gradient estimation via phase-array construction and classical inverse Fourier transform', 'fault_tolerant_resource_model': 'Logical-level resource estimates based on T-depth, logical qubits, and logical clock rates; discusses possible parallelization across up to 60 QPUs', 'real_qpu': False}

### Reproducibility
No code repository is mentioned in the provided text. The paper gives substantial mathematical detail, derivative parameters, target errors, and reported parameter settings (m, l, epsilon_phase), so the numerical experiments appear partially reproducible in principle. However, implementation details of the custom emulation, search procedure over parameters, and exact Monte Carlo setup are not fully specified here, so replication would require some reconstruction.
