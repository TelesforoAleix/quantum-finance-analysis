---
aliases:
- Autocallable Options Pricing with Integration-Based Exponential Amplitude Loading
- Autocallable Options Pricing Integration
authors:
- Francesca Cibrario
- Ron Cohen
- Emanuele Dri
- Christian Mattia
- Or Samimi Golan
- Tamuz Danzig
- Giacomo Ranieri
- Hanan Rosemarin
- Davide Corbelletto
- Amir Naveh
- Bartolomeo Montrucchio
auto_detected: true
classification: ''
contradiction_flags:
- contradiction:scalability
doi: 10.1109/QCE65121.2025.00267
evidence_type: ''
idea_tags:
- idea:quantum-advantage
- idea:near-term-feasibility
- idea:hybrid-approach
journal_or_venue: 2025 IEEE International Conference on Quantum Computing and Engineering
  (QCE)
methodology_tags:
- amplitude-estimation
- classical-simulation
paper_type: ''
quantum_advantage_claim: theoretical
related_papers: []
relevance_phase1: high
relevance_phase3: high
source_type: conference-paper
source_type_confidence: high
step1_date: '2026-03-25T16:08:02.102079'
step1_model: gpt-5.1
step2_date: '2026-03-25T16:08:06.983064'
step2_model: gpt-5.1
step3_date: '2026-03-25T16:08:55.102167'
step3_model: gpt-5.4
step4_date: '2026-03-25T16:09:20.330659'
step4_model: gpt-5.4
step5_date: '2026-03-25T16:09:38.265176'
step5_model: gpt-5.4
step6_date: '2026-03-25T16:09:47.812191'
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
- idea/quantum-advantage
- idea/near-term-feasibility
- idea/hybrid-approach
- contradiction/scalability
title: Autocallable Options Pricing with Integration-Based Exponential Amplitude Loading
topic_tags:
- derivatives-pricing
year: 2025
zotero_key: ''
---

## Abstract summary
The paper presents a full quantum algorithm for pricing single-asset autocallable options, built around an improved integration-based exponential amplitude loading scheme that encodes payoffs into quantum amplitudes with reduced circuit depth. The authors analyze T-depth complexity, show that their method substantially lowers the payoff component’s T-depth compared to Quantum Signal Processing-based approaches, and implement and simulate the circuits (up to 33 qubits) using the Classiq platform and HPC resources. They also benchmark against several classical models to demonstrate convergence toward classical Monte Carlo pricing under comparable discretization and precision constraints.
## Methodology
This conference paper presents an end-to-end quantum methodology for pricing single-asset autocallable options, with complexity analysis generalized to the multi-asset case. The approach is based on quantum amplitude estimation for expected discounted payoff estimation, specifically using Iterative Quantum Amplitude Estimation (IQAE), combined with a re-parameterization method that loads standard Gaussian distributions for each time step and then applies affine transformations and in-place accumulation to obtain log-returns. The main methodological contribution is an improved integration-based exponential amplitude loading scheme that encodes the payoff without full quantum arithmetic conversion from log-return space to return space, thereby improving normalization and reducing circuit depth relative to prior methods such as QSP-based payoff loading. The paper provides a formal algorithmic pipeline, T-depth complexity analysis of Gaussian preparation, arithmetic, comparators, and amplitude-loading modules, and compares the proposed payoff-loading component against prior state-of-the-art. Experimental validation is performed via simulation rather than real quantum hardware, using circuits synthesized in Classiq/Qmod and executed on multiple simulators and HPC infrastructure. The empirical study is framed as a proof of concept: the authors validate small instances of a 3-time-step single-asset autocallable by comparing quantum-simulator outputs against several classical benchmarks, including traditional Monte Carlo, discretized Monte Carlo, and closed-form models with matching discretization and arithmetic precision constraints, and they analyze convergence behavior as the number of Gaussian discretization qubits and arithmetic precision qubits increases.

**Algorithms used:** Quantum Amplitude Estimation, Iterative Quantum Amplitude Estimation, integration-based exponential amplitude loading, exact amplitude amplification, Gaussian state preparation
**Frameworks:** Classiq, Qmod, Cirq, cuQuantum, Nvidia simulator

**Experimental setup:** Experiments were conducted entirely in simulation. Quantum circuits were synthesized with the Classiq platform, with width minimization used to reduce qubit count for simulator execution. Small circuits up to 25 qubits were run on the default Classiq exact shot-based simulator; circuits up to 30 qubits were run on an Nvidia simulator using a single GPU; larger circuits exceeding 30 qubits were executed on the LEONARDO pre-exascale HPC system using the Cirq simulator on top of a cuQuantum appliance with multiple GPUs. The reported experiments used up to 33 qubits. No real QPU execution was used because current hardware coherence and fidelity were deemed insufficient for the circuit sizes required.

**Dataset:** No external empirical market dataset was used. The experiments used a synthetic/autocallable pricing instance parameterized by financial model inputs: notional value 18 USD, 3 annual time steps, annual volatility 0.2382, annual average log-return 0.1274, put barrier 0.7, put strike return 1, risk-free rate 4%, two binary option strikes both 1.1, binary payoffs 2 and 5, and Gaussian truncation parameter smin = 3.
## Findings
- [supported] The paper presents an end-to-end quantum algorithm for pricing single-asset autocallable options and validates it through simulation rather than real quantum hardware execution.
- [supported] The main technical contribution is an improved integration-based exponential amplitude loading method that avoids degradation of the normalization factor relative to the prior approach in [7].
- [supported] In the authors' complexity analysis for a relevant setting, the proposed payoff-loading approach reduces T-depth for the payoff component by about 50x relative to prior state-of-the-art methods.
- [supported] The amplitude loading module depth is reported to decrease from about 2.1e3 T-depth to about 40 T-depth when parallelization of partial exponential state preparation is considered.
- [supported] Simulations were carried out for small autocallable instances with up to 33 qubits using Classiq simulators, an Nvidia GPU simulator, and the LEONARDO HPC supercomputer.
- [supported] The simulated quantum-circuit outputs fell within the confidence interval produced by iterative quantum amplitude estimation when compared against a classical model constrained to the same Gaussian discretization and arithmetic precision.
- [supported] Increasing the number of qubits used for Gaussian discretization and arithmetic precision made the quantum-model behavior converge toward classical benchmark values, supporting consistency of the implementation.
- [supported] The authors show empirically that classical models with the same discretization constraints overlap with closed-form discretized calculations, and that these discretized models converge toward traditional Monte Carlo as precision increases.
- [speculative] The proposed methodology is described as a step toward efficient pricing of complex derivative products and toward eventual quantum utility in finance.
- [speculative] The paper reiterates the standard theoretical claim that quantum amplitude estimation offers quadratic asymptotic speedup over classical Monte Carlo, with O(1/epsilon) versus O(1/epsilon^2) query complexity, but this advantage is not demonstrated experimentally here.
- [supported] The authors conclude that current circuit sizes remain too large for meaningful real-hardware validation, making simulators necessary even for small-scale examples.

**Results summary:** This conference paper introduces a quantum algorithm for pricing autocallable options using an improved integration-based exponential amplitude loading technique. The main claimed advance is lower circuit depth for the payoff-loading component, with a complexity analysis indicating roughly a 50x T-depth reduction versus prior approaches and a drop in amplitude-loading depth from about 2.1e3 to about 40 T-depth in the analyzed setting. The implementation was validated only through simulation, including exact shot-based simulators, Nvidia GPU simulation, and LEONARDO HPC runs, with experiments reaching up to 33 qubits. For a small single-asset, 3-time-step autocallable example, the simulated quantum results matched a classical benchmark subject to the same discretization and arithmetic constraints and were reported to lie within the confidence interval of iterative quantum amplitude estimation. The paper does not demonstrate quantum advantage on hardware; its advantage claims remain theoretical and complexity-based.

**Performance claims:**
- ~50x reduction in T-depth for the payoff component relative to previous methods
- Amplitude loading module reduced from ~2.1 x 10^3 T-depth to ~40 T-depth
- Experiments conducted with up to 33 qubits
- Target IQAE settings: epsilon = 0.001 and alpha = 0.002
- Comparison setting for complexity analysis: T = 20 time steps, d = 3 assets, total estimation error epsilon = 2 x 10^-3
- Classical Monte Carlo convergence rate stated as 1/sqrt(M)
- Quantum amplitude estimation convergence/query complexity stated as O(1/epsilon) versus classical O(1/epsilon^2)
## Quantum advantage claim
**Classification:** theoretical

The paper relies on the standard theoretical quadratic speedup of quantum amplitude estimation over classical Monte Carlo and reports circuit-depth improvements versus prior quantum methods, but all validation is via simulation and no end-to-end quantum advantage is empirically demonstrated on real hardware.
## Limitations
- Experiments are limited to simulation on HPC and GPU-based simulators rather than execution on real quantum hardware, because current devices have insufficient coherence times and fidelity for the proposed circuits.
- The implementation is explicitly presented as a proof of concept rather than a production-ready pricing system.
- Validation uses a small instance of the autocallable pricing problem, specifically a single-asset product with three time steps and two binary options.
- The full algorithm implementation used the method from Section III-A rather than the improved problem-dependent strategy from Section III-B, in order to avoid implementing different problem-dependent models.
- The main challenge remains the considerable size of the circuits even for small-scale examples, which limits practical testing and near-term applicability.
- The paper notes that potential tests on real hardware are currently less interesting because of the large circuit sizes required.
- Benchmarking against classical methods is indirect: a fair direct comparison with traditional Monte Carlo on current simulators is stated to be infeasible because accuracy-constrained quantum circuits exceed simulator capabilities.
- The study relies on discretized Gaussian models and finite arithmetic precision, and part of the validation is against classical models constrained by the same discretization and precision assumptions.
- The approach is fully detailed for single-asset autocallables, while multi-asset best-of/worst-of extensions are discussed as extensible but not empirically implemented.
- Other volatility models are only mentioned as possible extensions; the implemented and analyzed setting is centered on Black-Scholes-style assumptions.
- The paper is a conference paper, so some implementation, experimental, and reproducibility details may be abbreviated due to page-limit constraints.
- [inferred] No empirical comparison is provided against state-of-the-art classical pricing engines on realistic market-scale autocallable books or real bank production workloads.
- [inferred] No experiments quantify the impact of hardware noise or error mitigation, so practical performance on NISQ devices remains unvalidated.
- [inferred] Resource claims focus heavily on T-depth reductions for subroutines, but end-to-end fault-tolerant resource feasibility and time-to-solution at production scale remain unresolved.
- [inferred] Reproducibility may be limited by dependence on the Classiq platform and synthesis engine, where circuit generation choices may be tool-specific.
- [inferred] The use of historical mean and volatility parameters in a simplified setup may not capture calibration complexity and model risk encountered in real structured-product desks.
## Open questions
- Can the proposed pricing algorithm be reduced enough in circuit size to become meaningful on real quantum hardware?
- How well will the method perform under realistic hardware noise once executed on actual devices rather than simulators?
- Will the observed subroutine-level T-depth reduction translate into a meaningful end-to-end quantum utility or quantum advantage for autocallable pricing?
- How does the approach scale with more time steps, more complex payoff structures, and larger multi-asset baskets?
- What is the best way to extend the methodology from the demonstrated single-asset case to best-of and worst-of multi-asset autocallables?
- How sensitive are pricing accuracy and resource requirements to Gaussian discretization choices and arithmetic precision settings?
- What are the trade-offs between the Section III-A and Section III-B loading strategies across different problem instances and payoff ranges?
- How effective will error mitigation techniques be in preserving output quality for this class of large derivative-pricing circuits?
- Can the methodology be adapted efficiently to local-volatility or stochastic-volatility models while keeping resource requirements manageable?
- [inferred] How does the method compare with advanced classical variance-reduction and structured-product pricing methods, not just baseline Monte Carlo?

**Future work:**
- Further optimize the algorithm to reduce overall circuit size.
- Initiate a campaign of tests on real quantum hardware.
- Leverage error mitigation techniques in real-hardware experiments to preserve output quality.
- Extend the methodology to more complex volatility models.
- Adapt the implementation to obtain optimal rescaling for given problem parameters using the different exponential state-preparation strategies.
- Pursue improvements in other components of the quantum algorithm beyond amplitude loading, since further gains are unlikely to come from that module alone.
- [inferred] Implement and empirically validate the multi-asset best-of/worst-of autocallable extension.
- [inferred] Evaluate the method on more realistic, larger-scale financial instances with longer maturities and more observation dates.
- [inferred] Perform end-to-end resource estimation including fault-tolerant overheads and wall-clock comparisons with classical baselines.
## Key ideas
- #idea:quantum-advantage — The paper proposes a full quantum autocallable-pricing pipeline using IQAE and argues theoretical quadratic speedup over classical Monte Carlo, while also reporting about 50x lower T-depth for the payoff-loading subroutine versus prior quantum approaches.
- #idea:hybrid-approach — Practical validation relies on a quantum-classical workflow: circuits are synthesized with Classiq/Qmod and executed on classical GPU/HPC simulators, then benchmarked against discretized and closed-form classical pricing references.
- #idea:near-term-feasibility — The work demonstrates proof-of-concept end-to-end pricing for a small single-asset, 3-time-step autocallable instance up to 33 qubits, showing convergence toward classical benchmarks under matched discretization and precision assumptions.
## Contradictions
- The paper makes theoretical quantum-advantage claims via amplitude estimation, but its evidence is simulation-only and does not demonstrate end-to-end superiority over classical pricing in practice.
- The reported T-depth improvements are subroutine-level and context-specific; the paper itself notes that overall circuit sizes remain too large for real hardware, which tempers broader claims about scalability to realistic multi-asset or longer-horizon autocallables.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->

## Experiment details
### Input
Synthetic single-asset autocallable option instance with T=3 time steps and two binary observation dates. Inputs include V=18 USD, dt=1 year, sigma=0.2382, mu=0.1274, barrier b=0.7, put strike return K=1, risk-free rate r=4%, binary strikes k1=k2=1.1, binary payoffs f1=2 and f2=5, and standard Gaussian truncation smin=3. The study varies the number of qubits per Gaussian encoding and the number of arithmetic precision qubits (fractional precision p) to study convergence. Gaussian distributions are discretized; arithmetic is implemented in fixed-point form.

### Process
1. Build a high-level quantum model in Qmod/Classiq for the autocallable pricing circuit. 2. For each time step, load a discretized standard Gaussian state. 3. Apply affine transformations to match the desired mean and variance and accumulate log-returns across time steps using in-place arithmetic. 4. Use comparators to detect binary option trigger conditions, barrier crossing, and put in-the-money conditions in log-return space. 5. Encode constant binary payoffs and zero-payoff mapping using controlled Ry rotations. 6. Encode the non-zero put payoff using the proposed integration-based exponential amplitude loading method. 7. Apply IQAE to estimate the probability amplitude corresponding to the expected discounted payoff; the paper states target confidence parameters epsilon = 0.001 and alpha = 0.002. 8. Synthesize circuits with width minimization and execute them on exact shot-based simulators/HPC simulators for selected qubit configurations. 9. Compare simulator outputs against four classical references: traditional Monte Carlo, discretized Monte Carlo using the same Gaussian discretization, closed-form with Gaussian discretization, and closed-form with both Gaussian discretization and fixed-point arithmetic precision matching the quantum model. 10. Analyze convergence as Gaussian discretization qubits and arithmetic precision qubits increase.

### Output
Outputs are expected payoff estimates for the autocallable option. Results are presented as convergence plots showing payoff versus number of Gaussian discretization qubits and arithmetic precision qubits, with quantum simulator outputs compared against classical baselines. The study reports that quantum results fall within the confidence interval of IQAE when benchmarked against the classical model with matching discretization and arithmetic constraints. The paper also reports complexity outputs, notably a roughly 50x reduction in T-depth for the payoff/amplitude-loading component relative to prior methods in a relevant setting, and discusses convergence toward traditional Monte Carlo behavior as precision increases.

### Parameters
- max_qubits_tested: 33
- time_steps: 3
- binary_options: 2
- epsilon: 0.001
- alpha: 0.002
- risk_free_rate: 0.04
- notional_value: 18
- annual_volatility: 0.2382
- annual_average_log_return: 0.1274
- put_barrier: 0.7
- put_strike_return: 1.0
- binary_strikes: [1.1, 1.1]
- binary_payoffs: [2, 5]
- gaussian_truncation_smin: 3
- simulator_regimes: {'up_to_25_qubits': 'Classiq default simulator', 'up_to_30_qubits': 'Nvidia simulator on single GPU', 'above_30_qubits': 'LEONARDO HPC with Cirq + cuQuantum on multiple GPUs'}

### Hardware
Simulation only. Default Classiq exact shot-based simulator used for circuits up to 25 qubits; Nvidia simulator on a single GPU used up to 30 qubits; LEONARDO pre-exascale supercomputer used for larger circuits via Cirq on top of a cuQuantum appliance with multiple GPUs. Circuits were synthesized with width minimization. No real quantum processor, noise model, or transpilation-to-specific-QPU details were reported.

### Reproducibility
Moderate to good reproducibility. The paper provides a detailed algorithm description, explicit model parameters in a reproducibility table, and cites an implementation/code base for the quantum autocallable algorithm and exponential loading strategies. Because the study uses synthetic parameterized inputs rather than proprietary data, data availability is not a major barrier. However, some implementation details such as exact shot counts, all synthesis settings, and full simulator configuration are not fully specified, so exact replication may require access to the referenced code and Classiq environment.
