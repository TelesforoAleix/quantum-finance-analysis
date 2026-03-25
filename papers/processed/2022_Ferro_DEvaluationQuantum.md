---
aliases:
- 'D5.4: Evaluation of quantum algorithms for pricing and computation of VaR'
- D Evaluation quantum algorithms
authors:
- Gonzalo Ferro
- Alberto Manzano
- Andrés Gómez
- Alvaro Leitao
- María R. Nogueiras
- Carlos Vázquez
auto_detected: true
classification: ''
contradiction_flags:
- contradiction:scalability
doi: ''
evidence_type: ''
idea_tags:
- idea:quantum-advantage
- idea:near-term-feasibility
journal_or_venue: NEASQC Consortium
methodology_tags:
- amplitude-estimation
- grover
- classical-simulation
paper_type: ''
quantum_advantage_claim: theoretical
related_papers: []
relevance_phase1: high
relevance_phase3: high
source_type: technical-report
source_type_confidence: high
step1_date: '2026-03-25T15:56:36.847148'
step1_model: gpt-5.1
step2_date: '2026-03-25T15:56:41.900304'
step2_model: gpt-5.1
step3_date: '2026-03-25T15:56:51.109973'
step3_model: gpt-5.4
step4_date: '2026-03-25T15:57:17.918797'
step4_model: gpt-5.4
step5_date: '2026-03-25T15:57:46.180478'
step5_model: gpt-5.4
step6_date: '2026-03-25T15:57:58.585746'
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
- method/classical-simulation
- idea/quantum-advantage
- idea/near-term-feasibility
- contradiction/scalability
title: 'D5.4: Evaluation of quantum algorithms for pricing and computation of VaR'
topic_tags:
- derivatives-pricing
- risk-modelling
year: 2022
zotero_key: ''
---

## Abstract summary
This technical report from the NEASQC project evaluates quantum algorithms for pricing financial derivatives and computing Value at Risk using Quantum Accelerated Monte Carlo techniques. It introduces a new data encoding protocol that can handle payoffs and prices that take negative values, and a Real Quantum Amplitude Estimation (RQAE) algorithm that is sensitive to the sign of amplitudes. The report benchmarks these methods against existing amplitude estimation algorithms via simulation, discusses their performance and limitations on current hardware, and documents an accompanying quantum finance software library (QQuantLib).
## Methodology
This technical report presents the scope, technical design, and evaluation framework for quantum algorithms for derivatives pricing and Value at Risk (VaR) within the NEASQC project. The report analyzes classical Monte Carlo pricing based on stochastic differential equation simulation via Euler-Maruyama and contrasts it with Quantum Accelerated Monte Carlo (QAMC), where path probabilities are encoded into quantum states and payoff or indicator functions are loaded into amplitudes for estimation through amplitude estimation routines. The main technical contributions are twofold: a new encoding protocol that can represent derivative payoffs with negative values, and a new amplitude estimation method, Real Quantum Amplitude Estimation (RQAE), designed to recover signed amplitudes rather than only probabilities. The report also documents a software stack, QQuantLib, implemented in Python 3.9.9 on top of Atos Quantum Learning Machine (QLM) 1.5.1, with modules for data loading, amplitude amplification, phase estimation, amplitude estimation, finance applications, and benchmarking. The scope of analysis includes pricing of European call, put, digital options, futures, and VaR formulations under a Black-Scholes setting, with benchmarking across several amplitude estimation variants. As a technical report, it emphasizes algorithmic specifications, oracle constructions, circuit/register layouts, software architecture, and benchmark configuration rather than a formal peer-reviewed methods section.

**Algorithms used:** Quantum Accelerated Monte Carlo, Amplitude Amplification, Amplitude Estimation, Maximum Likelihood Amplitude Estimation, Iterative Quantum Amplitude Estimation, Classical Quantum Phase Estimation, Iterative Quantum Phase Estimation, Real Quantum Amplitude Estimation, Euler-Maruyama
**Frameworks:** QQuantLib, Atos Quantum Learning Machine (QLM), Python 3.9.9, Jupyter notebooks, SciPy

**Dataset:** Synthetic/discretized financial model inputs rather than an external dataset. The report uses Black-Scholes model parameters and discretized payoff/probability grids for derivative pricing and VaR benchmark problems, including European call, European put, digital call, digital put, and futures contracts with multiple strike ratios.
## Experiment details
### Input
Synthetic option pricing instances under a Black–Scholes underlying with S0 = 1.0, maturity T = 1.0, volatility σ = 0.5, and risk-free rate r = 0.05. The underlying price domain is discretized from x0 = 0.01 to xf = 5.0 using nqbits = 5 qubits (32 intervals). Payoffs include: European Call (K/S0 = 0.5, V(S) = max(0, S − K)), European Put (K/S0 = 1.5, V(S) = max(0, K − S)), Digital Call (K/S0 = 0.5, V(S) = 1 if S ≥ K else 0), Digital Put (K/S0 = 1.5, V(S) = 1 if S ≤ K else 0), and Futures with K/S0 ∈ {0.5, 1.0, 1.5}, V(S) = S − K. The probability distribution p(T, S) is the discretized Black–Scholes terminal distribution; it is loaded into quantum amplitudes using either the standard encoding (square-root probabilities and payoffs) or the new encoding (direct probabilities and payoffs).

### Process
For each option type and strike configuration, the process is: (1) Define the Black–Scholes terminal distribution p(T, S) and payoff V(S). (2) Discretize the price domain into 2^n intervals and construct the corresponding probability and payoff arrays. (3) Build the quantum oracle using either: (a) standard encoding: apply Up to load sqrt(p(xi)) into amplitudes and UV to load sqrt(V(xi)) into an ancilla qubit as in Eq. (2.11); or (b) new encoding: apply a Walsh–Hadamard transform on an index register, then US and UV that load p(xi) and V(xi) directly into separate ancilla qubits, followed by another Walsh–Hadamard to obtain an amplitude proportional to the Riemann sum as in Eq. (3.7). (4) Construct the corresponding Grover-like operator Q from the oracle using the amplitude amplification package. (5) Run one of the AE algorithms (MLAE, IQAE, CQPEAE, IQPEAE, or RQAE) with specified hyperparameters (e.g., schedules for MLAE, epsilon/alpha for IQAE, epsilon/gamma and amplification ratio q for RQAE, number of auxiliary qubits or classical bits for QPE-based methods, and number of shots). (6) For each configuration, perform multiple repetitions (typically 5–10, up to 100 for IQAE and RQAE in new-encoding tests) and record the estimated expectation (or amplitude) and the effective number of oracle calls Noracle. (7) Compute the absolute error between the quantum estimate and the classical Riemann sum benchmark and plot error vs. Noracle for each payoff and AE algorithm.

### Output
Outputs are the estimated option prices (or normalized expectations) derived from amplitude estimates, along with the absolute error |∑ p(Si)V(Si) − p|0⟩| (or its normalized variant) as a function of the number of oracle calls Noracle. Results are presented in log–log plots for different payoffs and AE algorithms, comparing convergence rates and stability. For the new encoding and RQAE, additional plots show performance on payoffs with negative values (e.g., futures with K > S0), highlighting that RQAE uniquely converges to the correct signed expectation. No explicit comparison to classical Monte Carlo runtimes is implemented beyond theoretical error–cost scaling.

### Parameters
- discretization_qubits: 5
- domain_start: 0.01
- domain_end: 5.0
- intervals: 32
- auxiliary_qubits_CQPEAE: [10, 12, 14, 16]
- classical_bits_IQPEAE: [10, 12, 14]
- epsilon_IQAE: [0.01, 0.001, 0.0001, 1e-05]
- alpha_IQAE: 0.05
- epsilon_RQAE: [0.001, 0.0001, 1e-05]
- gamma_RQAE: 0.05
- q_RQAE: [1.2, 1.5, 2, 5, 10, 20]
- shots_per_run: 100
- MLAE_schedules_count: 5
- MLAE_ns: 10000
- MLAE_delta: 1e-07
- repetitions_standard_encoding: {'CQPEAE': 10, 'IQPEAE': 5, 'IQAE': 10, 'MLAE': 10}
- repetitions_new_encoding: {'CQPEAE': 10, 'IQPEAE': 5, 'IQAE': 100, 'MLAE': 10, 'RQAE': 100}

### Hardware
All quantum experiments are executed on simulators. The primary backend is the Atos Quantum Learning Machine (QLM) 1.5.1 quantum circuit simulator (up to 30 qubits, 96 CPU cores, 1.5 TB RAM). Additional simulations are run on FinisTerrae III (FT3) HPC nodes (Intel Xeon Ice Lake 835Y, 64 cores, 256 GB RAM) using QLM as the simulation engine. No real quantum processing units (QPUs) or noise models are used; circuits are simulated noiselessly.

### Reproducibility
The methodology is highly reproducible: the full QQuantLib library and Financial Applications repository, including source code, tests, benchmark scripts, and Jupyter notebooks, are publicly available on GitHub (https://github.com/NEASQC/FinancialApplications) with online documentation (https://neasqc.github.io/FinancialApplications/). All model parameters, discretization settings, and AE hyperparameters are tabulated, and the hardware/simulator environment is clearly specified. Since only synthetic Black–Scholes data are used, there are no data access restrictions. A knowledgeable reader with access to QLM or an equivalent simulator can replicate the experiments closely.
## Findings
- [supported] The report concludes that quantum accelerated Monte Carlo (QAMC) offers a theoretical quadratic error-cost improvement over classical Monte Carlo, with error scaling as O(1/C) versus O(1/sqrt(C)) under the stated oracle assumptions.
- [supported] The proposed new encoding protocol enables pricing of derivative products with negative payoffs, including payoffs of the form V(x)=x-K, where the standard encoding fails to converge to the correct value.
- [supported] The standard encoding estimates the sum of absolute contributions and therefore cannot correctly price derivatives with negative payoffs; this failure is illustrated experimentally for futures-style payoffs.
- [supported] The new encoding protocol experimentally converges to the Riemann-sum target even when payoffs take negative values, which the authors present as a novel capability relative to prior methods.
- [supported] The new Real Quantum Amplitude Estimation (RQAE) algorithm is designed to recover signed amplitudes and phase/sign information, allowing pricing of financial products with negative expected values.
- [supported] In the reported experiments, RQAE is the only tested amplitude estimation method that converges to the exact solution when the derivative price becomes negative.
- [supported] RQAE shows performance comparable to state-of-the-art amplitude estimation methods in the simulator benchmarks, although it is not consistently the best-performing method in practice.
- [speculative] The report cites tighter convergence bounds for RQAE than existing methods, but this claim relies on external theoretical work rather than empirical validation within this report.
- [supported] The new encoding protocol has worse performance than the standard encoding because of an Npaths multiplicative factor, which can reduce or eliminate the practical speedup.
- [supported] The reported evaluations were performed on simulators and classical compute platforms (Atos QLM and FinisTerrae III), not on fault-tolerant quantum hardware.
- [supported] The proposed algorithms are not yet applicable to current NISQ architectures because required oracle implementations use too many qubits, amplitude-estimation circuits are too deep, and gate-error requirements exceed current hardware capabilities.
- [supported] For standard nonnegative-payoff benchmarks, MLAE gives the best performance when carefully tuned, while IQAE is reported as the most stable choice without fine tuning; CQPEAE and IQPEAE are generally more stable but less accurate.
- [supported] The report recommends future work on more efficient SDE/oracle implementations to reduce both circuit depth and qubit count, as these are the main barriers to practical quantum finance advantage.
- [supported] A QLM-based software library (QQuantLib) was released implementing both encoding protocols and multiple amplitude estimation algorithms for pricing and VaR workflows.

**Results summary:** This technical report evaluates quantum algorithms for derivative pricing and Value at Risk using simulator-based experiments. It benchmarks several amplitude estimation methods and introduces two main contributions: a new encoding protocol and a new Real Quantum Amplitude Estimation (RQAE) algorithm. The new encoding resolves a key limitation of standard quantum finance encodings by allowing negative payoffs, while RQAE enables estimation of signed amplitudes so that negative-valued financial products can be priced. Experimental plots show that standard encoding fails on payoffs such as S_T-K, whereas the new encoding converges, and RQAE is the only tested method that converges when the target price is negative. However, the new encoding introduces an Npaths factor that can negate practical speedup, and the overall approach remains unsuitable for current NISQ hardware due to qubit, depth, and error-rate constraints. The report therefore frames the work as a technical advance and recommends further research on more efficient oracle/SDE implementations before practical quantum advantage in finance is achievable.

**Performance claims:**
- Classical Monte Carlo error scales as O(1/sqrt(C)) while QAMC error scales as O(1/C), where C is the number of Euler-Maruyama evaluations.
- Riemann truncation/discretization error is stated to scale as O(1/2^nqb) for payoffs depending only on terminal asset price.
- Amplitude-estimation sampling error is stated to scale as O(1/Noracle).
- Benchmark discretization used x0=0.01, xf=5.0, nqbits=5, giving 32 intervals.
- Underlying model parameters in experiments: Black-Scholes with S0=1.0, maturity=1.0, volatility=0.5, risk-free rate=0.05.
- CQPEAE used 10, 12, 14, 16 auxiliary qubits in benchmarks.
- IQPEAE used 10, 12, 14 classical bits in benchmarks.
- IQAE used epsilon values 1e-2, 1e-3, 1e-4, 1e-5 with alpha=0.05.
- RQAE used epsilon values 1e-3, 1e-4, 1e-5 with gamma=0.05 and amplification ratio q in {1.2, 1.5, 2, 5, 10, 20}.
- Most benchmark figures sweep Noracle roughly from 10^4 up to 10^7 for standard tests and up to about 10^10 for some new-encoding/RQAE tests.
## Quantum advantage claim
**Classification:** theoretical

The report claims a theoretical quadratic speedup of QAMC over classical Monte Carlo based on complexity/error scaling, but explicitly states that this advantage is not achievable on current NISQ hardware and all evaluations are simulator-based rather than demonstrations on real quantum devices.
## Limitations
- The proposed algorithms are not yet applicable to current NISQ architectures.
- The new encoding algorithm performs worse than the standard encoding algorithm.
- The new encoding introduces a factor Npaths that can overshadow or even eliminate the theoretical quantum speedup depending on the setup.
- The delivered quantum algorithm is not yet competitive with classical algorithms when executed on NISQ hardware.
- Deep circuits required by amplitude estimation and Grover-like routines are not feasible on current QPUs without error correction.
- Implementing the oracle US as described requires an excessively large number of qubits.
- The combined gate count of oracle construction and Grover-like routines would require gate fidelities beyond current technology.
- Direct translation of classical SDE simulation circuits into quantum circuits would require a number of qubits far beyond current NISQ capabilities.
- The evaluation was performed using simulators rather than real quantum hardware.
- The report scope is limited to pricing and VaR/expected shortfall via Monte Carlo-style methods, not broader financial services tasks.
- As a technical report tied to the NEASQC use case, the work is constrained by the project mandate and focuses mainly on UC5 objectives rather than a broader independent assessment.
- The experiments use a narrow set of financial products and one underlying model setup (primarily Black-Scholes with fixed parameters), limiting generality.
- The discretization used in experiments is small (5 qubits, 32 intervals), which limits evidence about scalability.
- [inferred] No validation on real market data or institution-scale portfolios is reported.
- [inferred] No end-to-end runtime comparison against strong state-of-the-art classical pricing/VaR engines is provided; comparisons are mainly theoretical or against Riemann sums.
- [inferred] Hardware noise, calibration drift, and error-mitigation effects are not empirically characterized because experiments are simulator-based.
- [inferred] The report does not establish reproducible performance under heterogeneous hardware/software stacks beyond QLM and selected compute nodes.
- [inferred] The data and assumptions may be time-bound to the 2022 project context, so conclusions about current hardware competitiveness may already be partially outdated.
## Open questions
- How can these algorithms be improved so they can execute on current QPUs despite deep-circuit requirements?
- How can the depth and qubit requirements of SDE-solving oracles be reduced enough to make quantum pricing practical?
- Can a new encoding method remove or reduce the harmful Npaths factor while still supporting negative payoffs?
- Under what practical conditions, if any, can the theoretical quadratic speedup of QAMC survive oracle-loading overheads?
- How does RQAE perform relative to other amplitude estimation methods on larger and more realistic financial instances?
- What is the best trade-off for the RQAE amplification ratio q between circuit depth and convergence speed on realistic hardware?
- Can the sign-sensitive estimation approach be extended efficiently to broader classes of financial products and risk measures?
- How robust are the proposed methods under realistic noise, decoherence, and finite gate fidelity on actual hardware?
- [inferred] At what problem sizes and hardware error rates would these methods become competitive with industrial classical Monte Carlo systems?
- [inferred] How well do the methods generalize beyond Black-Scholes-style settings to multi-asset, path-dependent, or stochastic-volatility models?

**Future work:**
- Develop new encoding methods to overcome the performance caveat introduced by the Npaths factor.
- Focus research efforts on techniques that efficiently solve the SDE associated with the pricing problem.
- Reduce both the circuit depth and the number of qubits required to implement the oracle.
- Adapt or redesign algorithms so they can run on current QPUs or future fault-tolerant devices.
- Continue improving methods for pricing derivatives and computing VaR when payoffs or expected values can be negative.
- Further benchmark RQAE and other amplitude estimation algorithms under broader experimental settings.
- [inferred] Validate the proposed methods on real quantum hardware with noise-aware implementations and error mitigation.
- [inferred] Extend evaluation to more realistic financial datasets, larger portfolios, and more complex derivative structures.
- [inferred] Perform stronger classical baselines and cost-benefit analyses to determine practical quantum advantage thresholds.
- [inferred] Update the assessment with newer hardware and software stacks to account for the currency limitations of this 2022 technical report.
## Key ideas
- #idea:quantum-advantage — Formalizes Quantum Accelerated Monte Carlo for derivatives pricing and VaR, claiming theoretical quadratic error-cost improvement over classical Monte Carlo via amplitude estimation.
- #idea:quantum-advantage — Introduces a new encoding protocol that supports negative payoffs/expectations, addressing a failure mode of standard square-root payoff encoding.
- #idea:quantum-advantage — Proposes Real Quantum Amplitude Estimation (RQAE) to estimate signed amplitudes, enabling correct pricing of futures-like products with negative values in simulation.
- #idea:near-term-feasibility — Benchmarks are entirely simulator-based using Atos QLM/QQuantLib; no real QPU or noise-aware hardware validation is provided.
- #idea:near-term-feasibility — Concludes current NISQ hardware is insufficient because oracle loading, Grover-like amplitude estimation depth, and qubit requirements are too large.
- #idea:near-term-feasibility — Provides a reproducible software stack (QQuantLib) for pricing and VaR benchmarking, useful for future comparative studies.
## Contradictions
- The paper claims theoretical quantum advantage for Monte Carlo-style pricing/VaR, but also shows that the new encoding required for negative payoffs introduces an Npaths factor and deeper circuits that can erase the practical speedup.
- The report confirms favorable asymptotic amplitude-estimation scaling in noiseless simulation, yet concludes the approach is not deployable on current NISQ hardware due to qubit count, circuit depth, and fidelity constraints.
- Although positioned as a route to faster financial Monte Carlo, the study does not provide end-to-end empirical runtime comparisons against strong classical pricing or VaR engines, weakening broad superiority claims.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
