---
aliases:
- Reduction of Qubits in Quantum Algorithm for Monte Carlo Simulation by Pseudo-random
  Number Generator
- Reduction Qubits Quantum Algorithm
authors:
- Koichi Miyamoto
- Kenji Shiohara
auto_detected: true
classification: ''
contradiction_flags:
- contradiction:scalability
- contradiction:classical-vs-quantum
doi: ''
evidence_type: ''
idea_tags:
- idea:quantum-advantage
- idea:near-term-feasibility
- idea:hybrid-approach
journal_or_venue: arXiv
methodology_tags:
- amplitude-estimation
- classical-simulation
paper_type: ''
quantum_advantage_claim: speculative
related_papers: []
relevance_phase1: high
relevance_phase3: high
source_type: preprint
source_type_confidence: high
step1_date: '2026-03-25T15:52:13.695713'
step1_model: gpt-5.1
step2_date: '2026-03-25T15:52:17.905936'
step2_model: gpt-5.1
step3_date: '2026-03-25T15:52:50.262288'
step3_model: gpt-5.4
step4_date: '2026-03-25T15:53:20.311268'
step4_model: gpt-5.4
step5_date: '2026-03-25T15:53:57.964673'
step5_model: gpt-5.4
step6_date: '2026-03-25T15:54:09.334463'
step6_model: gpt-5.4
steps_completed:
- 1
- 2
- 3
- 4
- 5
- 6
tags:
- topic/risk-modelling
- method/amplitude-estimation
- method/classical-simulation
- idea/quantum-advantage
- idea/near-term-feasibility
- idea/hybrid-approach
- contradiction/scalability
- contradiction/classical-vs-quantum
title: Reduction of Qubits in Quantum Algorithm for Monte Carlo Simulation by Pseudo-random
  Number Generator
topic_tags:
- risk-modelling
year: 2020
zotero_key: ''
---

## Abstract summary
The paper proposes a way to reduce the number of qubits required for quantum Monte Carlo algorithms, particularly for high-dimensional problems in quantitative finance such as credit risk measurement. Instead of allocating a separate quantum register for each random variable, the authors implement a pseudo-random number generator (specifically PCG) on a quantum circuit to sequentially generate random numbers and compute the integrand, then use amplitude estimation to obtain the sample average with quadratic speedup over classical Monte Carlo. They detail circuit constructions for the PRNG, discuss the trade-off between qubit count and circuit depth, show how to apply the method to the Merton credit risk model, and demonstrate it on a small multi-variable integration using simulation.
## Methodology
This preprint is primarily a theoretical/method-development paper with a small proof-of-concept simulation. It proposes a qubit-reduction approach for quantum Monte Carlo by replacing the standard register-per-random-variable encoding with sequential generation of pseudo-random numbers (PRNs) on a reusable quantum register, while still using quantum amplitude estimation to recover a quadratic speedup over classical Monte Carlo. The paper formalizes the method under assumptions that the integrand can be computed sequentially and that a pseudo-random number generator can be implemented as quantum gates for sequence progression and jump-ahead initialization. It develops a concrete implementation based on the permuted congruential generator (PCG), describing quantum circuits for modular arithmetic, permutation operations such as random rotation and xorshift, and analyzes the qubit-depth tradeoff. The method is then specialized to credit risk measurement under the Merton model, where portfolio loss is computed sequentially across obligors using PRNs and conditional default thresholds. In addition, the paper includes a proof-of-concept empirical demonstration on a simple multivariable trigonometric integration problem, implemented in simulation using Qiskit, where likelihood-based amplitude estimation is used to estimate the integral from repeated measurements of circuits parameterized by Grover-like iterate counts.

**Algorithms used:** Quantum Monte Carlo, Quantum Amplitude Estimation, Amplitude Estimation without Phase Estimation, Permuted Congruential Generator (PCG), Linear Congruential Generator (LCG), Random rotation permutation, Xorshift
**Frameworks:** Qiskit

**Experimental setup:** The paper is a preprint and mostly theoretical, but includes a proof-of-concept numerical experiment run on the IBM Qiskit quantum circuit simulator. The demonstration estimates a 2-variable trigonometric integral using a small LCG-based PRNG implemented as a quantum circuit. No real QPU is used; the experiment is simulator-based.

**Dataset:** No external dataset is used. The empirical demonstration uses a synthetic numerical integration task based on a two-variable trigonometric function. The credit risk application is illustrative and based on the Merton model, but no real portfolio dataset is reported.
## Findings
- [speculative] The paper proposes a quantum Monte Carlo approach that replaces per-random-number quantum registers with a pseudo-random number generator (PRNG) implemented on a quantum circuit to reduce qubit requirements while retaining quadratic Monte Carlo speedup.
- [speculative] The method estimates the average over sampled integrand values generated by a PRNG (Esamp) rather than the exact expectation over all random-number configurations (Etrue), making the quantum procedure closer to classical Monte Carlo.
- [speculative] Under the authors' error model, the proposed method preserves the O(1/N) amplitude-estimation scaling for estimating Esamp, while the sampling error from finite pseudo-random samples remains O(Nsamp^-1/2).
- [speculative] For a target additive error epsilon, the authors claim the proposed method requires Norac proportional to 1/epsilon after choosing a sufficiently large sample count Nsamp proportional to 1/epsilon^2, implying quadratic speedup over classical Monte Carlo in oracle complexity.
- [speculative] The approach trades qubit reduction for increased circuit depth because random numbers are generated sequentially rather than in parallel.
- [speculative] The authors identify permuted congruential generator (PCG) as a suitable PRNG for quantum circuits because it combines modest memory use with implementable update and jump-ahead operations.
- [speculative] For PCG with r-bit output and n-bit background LCG, the dominant resource cost of the PRNG circuit is claimed to come from modular multiplication, giving O(n) ancilla qubits and O(n^2) circuit depth.
- [speculative] The paper outlines how the PRNG-based method can be applied to credit portfolio risk measurement under the Merton model by sequentially accumulating obligor losses using pseudo-random draws for idiosyncratic risk factors.
- [supported] In a small proof-of-concept simulation of a 2-variable trigonometric integral using Qiskit, the quantum estimate closely matched the exact average over the chosen pseudo-random sample points.
- [speculative] The authors argue that partial parallelization between full parallel random-number registers and full sequential PRNG generation may be a practical memory-depth trade-off for future large-scale quantum Monte Carlo in finance.

**Results summary:** This preprint proposes a qubit-saving variant of quantum Monte Carlo in which pseudo-random numbers are generated sequentially on a quantum circuit and the quantum computer estimates the average of sampled integrand values rather than the exact expectation over all random inputs. The main claim is that this can substantially reduce qubit requirements for high-dimensional financial Monte Carlo problems, such as credit risk, while preserving the usual quadratic oracle-complexity advantage of amplitude estimation, at the cost of deeper circuits. The paper gives a concrete PRNG construction based on PCG, analyzes rough qubit-depth scaling, sketches an application to Merton-model credit risk, and provides a small simulator-based proof of concept on a 2D trigonometric integration task. Because the paper is a preprint and the empirical evidence is limited to a toy simulation rather than financial-scale experiments or hardware runs, the broader quantum advantage claims remain speculative.

**Performance claims:**
- Quantum Monte Carlo estimation error scales as O(N^-1) in computational steps versus O(N^-1/2) classically
- Proposed method error bound: Delta_our ≈ c*sigma*2^(-nsamp/2) + 2*pi*d*sqrt(Esamp(1-Esamp))/Norac
- To achieve additive error epsilon, sufficient settings claimed are Nsamp ≈ (c*sigma/epsilon)^2 and Norac ≈ 2*pi*d*sqrt(Esamp(1-Esamp))/epsilon
- Classical Monte Carlo requires Norac ≈ (c*sigma/epsilon)^2 for additive error epsilon
- Example from Figure 2 discussion: when nsamp >= 20, the proposed method reaches the same error order as classical Monte Carlo at Norac = 10^3 versus 10^6 classically
- Credit-risk motivation example: number of obligors and required random numbers can be O(10^6) in large portfolios
- Typical practical sample count mentioned for credit risk: Nsamp = 10^6
- PRNG period example discussed: 2^64, with practical Nran*Nsamp around 10^12 ≈ 2^40
- PCG resource estimate: dominant PRNG contribution O(n) ancilla qubits and O(n^2) circuit depth
- Proof-of-concept integration setting: theta = pi/6, Nvar = 2, LCG parameters a = 11, c = 0, m = 31, seed = 1, 5-bit PRN, period 30, Nsamp = 8, using 16 PRN elements
- Amplitude-estimation experiment setting: M = 8, Nk = 100, mk = 2^k
- Toy integration results: exact original integral = 0.074578, exact average on sample points = 0.078394, quantum estimate = 0.078391
## Quantum advantage claim
**Classification:** speculative

The paper claims retained quadratic quantum speedup in oracle complexity via amplitude estimation, but this is argued theoretically and supported only by a small simulator-based toy example rather than strong empirical evidence on real hardware or realistic financial workloads. As a preprint, advantage claims should be treated as speculative.
## Limitations
- Lack of peer review: the work is a preprint and its claims have not been independently validated through peer review.
- The proposed qubit reduction comes at the cost of increased circuit depth; the authors explicitly note that full reduction may be impractical.
- Without quantum error correction, the deep circuits required by the sequential PRNG-based approach are unlikely to be executable on near-term hardware.
- Even with error correction, long runtimes for fault-tolerant gates may limit practical speed advantages.
- The method relies on a restrictive assumption that the integrand can be computed sequentially in the form y_n = f_n(y_{n-1}, x_n); the authors state that not all functions satisfy this.
- The approach estimates the sample average Esamp rather than the true expectation Etrue, introducing an additional sampling error term beyond amplitude-estimation error.
- The method requires choosing a PRNG that supports both efficient stepwise progression and jump-ahead operations on a quantum circuit, which may limit generator choices.
- The authors acknowledge statistical concerns when using consecutive subsequences of PRNs in high-dimensional spaces, especially for large Nran.
- The proof-of-concept simulation uses a very small-scale setup: a 5-bit LCG with period 30 and only 8 sample points, which is not representative of realistic financial workloads.
- The demonstration is performed only on a simulator, not on real quantum hardware, so hardware noise, calibration drift, and execution constraints are not assessed.
- The financial application to credit risk is presented as a circuit construction, but no end-to-end empirical benchmark is provided for realistic portfolio sizes.
- Implementation of key subroutines is assumed rather than fully developed in this paper, including distribution transforms and function evaluation gates such as Yi.
- The practical utility depends on available qubit-memory trade-offs and machine specifications that do not yet exist for the target large-scale use cases.
- [inferred] No direct comparison is provided against state-of-the-art classical Monte Carlo variance reduction methods or optimized classical risk engines.
- [inferred] No resource estimates are given for realistic fault-tolerant implementations of the full credit risk workflow, beyond asymptotic discussion.
- [inferred] The claimed quadratic speedup may be offset in practice by large constant factors from arithmetic, modular multiplication, and PRNG circuitry.
- [inferred] The statistical quality of PCG in the specific quantum Monte Carlo sampling context is not empirically validated for financial risk metrics.
- [inferred] The analysis focuses mainly on oracle-call complexity and does not fully quantify total gate counts, T-count/T-depth, or ancilla overhead for complete applications.
- [inferred] Reproducibility is limited because the paper does not provide full implementation details, code, or benchmark configurations for the larger proposed finance use cases.
## Open questions
- How practical is the qubit-depth trade-off on realistic quantum hardware for large-scale financial Monte Carlo tasks?
- For which classes of financial integrands does the sequential computation assumption hold well enough to make the method broadly applicable?
- How large can Nran and Nsamp become before PRNG statistical weaknesses materially affect estimation accuracy in high-dimensional finance problems?
- How does the proposed PRNG-based approach compare empirically with previous quantum Monte Carlo constructions in total runtime and accuracy?
- What is the best balance between partial parallelism and sequential PRNG generation under realistic hardware memory constraints?
- How well does PCG perform, relative to other PRNGs, when embedded in quantum circuits for finance-specific Monte Carlo estimation?
- Can the method deliver practical advantage once fault-tolerant overheads and arithmetic costs are included?
- How robust is the approach to noise and decoherence when implemented on actual quantum devices?
- What are the resource requirements for realistic credit portfolios with very large numbers of obligors?
- How should one choose PRNG parameters, sample counts, and discretization levels to control both statistical and quantum estimation errors in practice?

**Future work:**
- Investigate practical adjustment of calculation settings by exploiting the memory-speed trade-off between qubit count and circuit depth.
- Apply the method to large-scale Monte Carlo simulations in future quantum computing environments with constrained memory resources.
- Explore partial parallelization strategies where only subsets of random numbers are generated simultaneously and partial integrand results are merged.
- Implement the method for realistic credit risk measurement workflows once larger quantum machines become available.
- Use larger and more realistic PRNG configurations, such as wider-output PCG settings with recommended parameters, instead of the toy proof-of-concept setup.
- Develop concrete implementations of required arithmetic and distribution-conversion subroutines for end-to-end financial applications.
- Validate the approach on real quantum hardware when sufficient qubits and error-corrected execution become available.
- [inferred] Benchmark against strong classical Monte Carlo baselines, including variance reduction and production-grade financial risk systems.
- [inferred] Provide full resource estimation studies for fault-tolerant implementations, including gate counts, depth, and logical qubit requirements.
- [inferred] Empirically study the statistical impact of different PRNG choices and parameterizations on finance-specific quantum Monte Carlo outputs.
- [inferred] Extend the framework to broader financial applications such as derivative pricing and other high-dimensional stochastic simulations.
## Key ideas
- #idea:quantum-advantage — Proposes a qubit-saving quantum Monte Carlo scheme that retains amplitude-estimation-based quadratic oracle-complexity speedup for estimating Monte Carlo sample averages.
- #idea:near-term-feasibility — Reuses a small quantum register via an in-circuit PRNG to reduce qubit requirements for high-dimensional finance applications such as credit risk under the Merton model.
- #idea:hybrid-approach — Frames practical deployment as a memory-depth trade-off, including partial parallelization between fully sequential PRNG generation and fully parallel random-number registers.
- #idea:quantum-advantage — Specializes the framework to credit portfolio risk measurement by sequentially accumulating obligor losses from pseudo-random draws.
- #idea:near-term-feasibility — Uses likelihood-based amplitude estimation without phase estimation in a simulator proof of concept, suggesting a more implementation-oriented variant than textbook QAE.
## Contradictions
- The paper claims retained quadratic quantum advantage in oracle complexity, but its own evidence is limited to a tiny simulator-only toy integration and no realistic financial benchmark, contradicting strong practical superiority claims.
- The paper motivates qubit reduction as enabling large-scale finance use cases, yet it also acknowledges substantially increased circuit depth, restrictive sequential-integrand assumptions, and likely impracticality on near-term hardware, creating a scalability contradiction.
- The method estimates the pseudo-random sample average Esamp rather than the true expectation Etrue, which weakens direct claims of superiority over classical Monte Carlo for the original financial estimation problem.
- No comparison is provided against optimized classical Monte Carlo methods or variance-reduction baselines, so the claimed advantage over classical approaches is not empirically established.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->

## Experiment details
### Input
Synthetic input only: estimation of the integral I = (1/theta^Nvar) ∫_0^theta ... ∫_0^theta sin^2(sum_i x_i) dx_1...dx_Nvar with theta = pi/6 and Nvar = 2. PRNG input uses an LCG with parameters a = 11, c = 0, m = 31 and seed = 1, producing 5-bit pseudo-random numbers with period 30. The experiment uses Nsamp = 8 sample points, consuming 16 PRN sequence elements. No preprocessing or time period applies.

### Process
1. Construct a quantum circuit that prepares an equal superposition over sample indices using Hadamard gates. 2. Initialize the starting PRN values via a jump-ahead operation and then sequentially advance the PRNG register using the progression gate. 3. For the integration demo, encode the sampled integrand indirectly by sequentially rotating an ancilla qubit Rrot with controlled Ry gates according to each PRN value, so that the probability of measuring |1> equals the Monte Carlo estimate of the integral. 4. Build the amplitude-estimation-style operator Q = -A S0 A^-1 Sχ, where A is the full state-preparation circuit, S0 flips phase on the all-zero state, and Sχ flips phase when the ancilla is |1>. 5. For likelihood-based amplitude estimation, prepare states Q^m A|0> for m_k = 2^k, k = 0,...,8. 6. For each m_k, perform N_k = 100 measurements and record h_k, the number of ancilla-|1> outcomes. 7. Estimate the amplitude parameter theta_a by maximizing the likelihood function over the collected counts, then convert this to the estimated integral value. The paper also provides a stepwise circuit design for credit risk measurement under the Merton model, but does not report numerical experiments for that application.

### Output
The output is an estimated scalar integral value. The paper reports three values for comparison: (i) exact value of the original integral = 0.074578, (ii) exact average over the selected sample points = 0.078394, and (iii) estimate from the proposed quantum-simulation method = 0.078391. The comparison is therefore against the exact analytical integral and the exact Monte Carlo sample average induced by the chosen PRNG/sample set, rather than against a classical optimization baseline.

### Parameters
- Nvar: 2
- theta: pi/6
- prng_type: LCG
- lcg_a: 11
- lcg_c: 0
- lcg_m: 31
- seed: 1
- prng_bits: 5
- prng_period: 30
- samples: 8
- prn_elements_used: 16
- amplitude_estimation_M: 8
- measurements_per_m: 100
- m_values: 2^k for k=0,...,8

### Hardware
{'hardware_type': 'simulator', 'simulator': 'IBM Qiskit quantum circuit simulator', 'qpu_used': False, 'cloud_provider': 'IBM', 'noise_model': 'not specified', 'transpilation_settings': 'not specified'}

### Reproducibility
No code repository is mentioned in the provided text. The simulator platform, toy problem, PRNG parameters, and key amplitude-estimation settings are described, so the proof-of-concept experiment is partially reproducible. However, implementation details are incomplete for exact replication, especially low-level circuit construction and simulator configuration.
