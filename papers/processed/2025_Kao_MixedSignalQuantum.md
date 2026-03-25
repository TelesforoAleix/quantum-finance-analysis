---
aliases:
- Mixed-Signal Quantum Circuit Design for Option Pricing Using Design Compiler
- Mixed Signal Quantum Circuit
authors:
- Yu-Ting Kao
- Yeong-Jar Chang
- Ying-Wei Tseng
auto_detected: true
classification: ''
contradiction_flags:
- contradiction:scalability
doi: ''
evidence_type: ''
idea_tags:
- idea:quantum-advantage
- idea:near-term-feasibility
- idea:hybrid-approach
journal_or_venue: ''
methodology_tags:
- amplitude-estimation
- quantum-simulation
- classical-simulation
paper_type: ''
quantum_advantage_claim: theoretical
related_papers:
- 2021_JP_Morgan_OptionPricingCircuit
relevance_phase1: high
relevance_phase3: medium
source_type: peer-reviewed-empirical
source_type_confidence: high
step1_date: '2026-03-25T16:10:01.509011'
step1_model: gpt-5.1
step2_date: '2026-03-25T16:10:04.453069'
step2_model: gpt-5.1
step3_date: '2026-03-25T16:10:28.724211'
step3_model: gpt-5.4
step4_date: '2026-03-25T16:10:57.729336'
step4_model: gpt-5.4
step5_date: '2026-03-25T16:11:24.119812'
step5_model: gpt-5.4
step6_date: '2026-03-25T16:11:32.136951'
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
- method/quantum-simulation
- method/classical-simulation
- idea/quantum-advantage
- idea/near-term-feasibility
- idea/hybrid-approach
- contradiction/scalability
title: Mixed-Signal Quantum Circuit Design for Option Pricing Using Design Compiler
topic_tags:
- derivatives-pricing
year: null
zotero_key: ''
---

## Abstract summary
The paper proposes a mixed-signal quantum circuit framework for option pricing that integrates analog components with digitally synthesized logic using Synopsys Design Compiler. It introduces three techniques—exponential data pre-processing, digital calibration of rotation gates, and a Monte Carlo price simulation architecture—to reduce gate count and depth while improving noise tolerance compared to an existing J.P. Morgan option pricing circuit. The work focuses on linear components and averaging as an intermediate validation step, with nonlinear payoff and exponential blocks left for future implementation.
## Methodology
The paper presents a peer-reviewed empirical circuit-design study for quantum option pricing that combines quantum-financial modeling with classical electronic design automation. The methodology centers on a mixed-signal quantum circuit framework with three main components: (1) exponential data pre-processing, where Synopsys Design Compiler is used to synthesize and restructure state-preparation/rotation logic so that input encoding complexity is reduced from exponential to polynomial/linear scaling; (2) digital calibration, where lookup-table-based arcsine correction is applied to compensate for analog rotation-gate nonlinearity and improve noise tolerance; and (3) Monte Carlo price simulation, where asset-price fluctuations are modeled through random walk increments accumulated by a single-qubit price accumulator, with the possibility of either classical-style direct measurement or Quantum Amplitude Estimation (QAE) for averaging. The study uses JP Morgan's option pricing circuit as the main baseline and evaluates a 12-qubit case study, reporting reductions in gate count, circuit depth, and maximum error. The implementation is only partial for the full option-pricing workflow: nonlinear components such as exponential and payoff functions are not yet implemented, so experiments validate the linear averaging portion and compare the resulting distributions/averages against classical Monte Carlo behavior and the prior JP Morgan design.

**Algorithms used:** Quantum Amplitude Estimation, Monte Carlo simulation
**Frameworks:** Qiskit, Synopsys Design Compiler

**Experimental setup:** A 12-qubit case study is used to compare the proposed mixed-signal circuit against JP Morgan's option pricing circuit. Circuit synthesis and optimization are performed using Synopsys Design Compiler from RTL descriptions. Quantum analysis includes statevector-based evaluation and histogram visualization in Qiskit; the paper explicitly states that figures were generated from the statevector rather than random measurement shots. The design includes Hadamard-based random number generation for Monte Carlo simulation and a single-qubit accumulator for price aggregation. The reported implementation validates only the linear portion of the option-pricing circuit, not the nonlinear exponential/payoff blocks.

**Dataset:** No external financial market dataset is reported. Inputs are synthetic/procedural distributions and simulated asset-price fluctuations: a discretized lognormal probability distribution encoded into 32 output levels over 4096 input states for the 12-qubit case, plus random-walk price distributions for 1-day and 2-day simulations used to compare quantum Monte Carlo and classical Monte Carlo outputs.
## Experiment details
### Input
Synthetic experiment inputs rather than historical financial data. For state preparation, the paper uses an encoded lognormal probability distribution discretized into 32 output levels (0-31) with inputs ranging from 0 to 4095, corresponding to 12 qubits / 4096 quantum states. For Monte Carlo validation, the circuit simulates daily asset-price fluctuations from a predefined probability distribution, including 1-day and 2-day random-walk generators; one validation setting assigns zero probability to unchanged asset prices (+0%). No sample size, real-data source, feature count, or time period from financial markets is provided.

### Process
1. Encode a discretized lognormal probability distribution in RTL and synthesize the circuit with Synopsys Design Compiler to reduce state-preparation complexity. 2. Apply digital calibration via lookup tables using r = arcsin(sqrt(x)) so that rotation-gate outputs sin(r) match the desired sqrt(x) weighting; compare calibrated and uncalibrated error behavior. 3. Build a mixed-signal Monte Carlo circuit in which Hadamard gates plus measurement act as a quantum random number generator for price increments. 4. Accumulate multi-step price changes using a single-qubit price accumulator, with the exponential/payoff stage deferred because nonlinear blocks are not yet implemented. 5. Evaluate averaging behavior either by direct measurement in a Monte Carlo style or conceptually via QAE for fewer measurements. 6. Compare resulting distributions/averages with classical Monte Carlo and with the JP Morgan option-pricing circuit. 7. Use Qiskit statevector analysis to generate histograms for visual comparison rather than shot-based sampling. The paper also reports an empirically selected analog-scaling factor improved from a heuristic m=2 to m=1.57 (approximately pi/2) to minimize approximation error.

### Output
Reported outputs include circuit-complexity metrics and accuracy comparisons: gate count reduction from 4095 to 392, circuit depth reduction from 2048 to 6, and maximum calculation error reduction from 25.86% to 1.64%. Monte Carlo validation outputs are price-distribution histograms for 1-day and 2-day random walks and qualitative consistency with classical Monte Carlo analysis. The main baselines are JP Morgan's option pricing circuit and classical Monte Carlo simulation; the paper also contrasts calibrated versus uncalibrated rotation behavior.

### Parameters
- qubits: 12
- input_states: 4096
- distribution_output_levels: 32
- gate_count_baseline: 4095
- gate_count_proposed: 392
- depth_baseline: 2048
- depth_proposed: 6
- max_error_baseline_percent: 25.86
- max_error_proposed_percent: 1.64
- rotation_angle_range_calibrated: 0 to pi/2 radians
- angle_tolerance_approx: 0.05 radians
- analog_scaling_factor_heuristic: 2
- analog_scaling_factor_optimized: 1.57
- random_number_generator_bits_example: 4
- major_qubits_qae_example: 20
- parallel_runs_qae_example: 1048576

### Hardware
No real QPU is reported. The study appears to rely on circuit synthesis and simulation tools: Synopsys Design Compiler for RTL/circuit synthesis and Qiskit for histogram/statevector analysis. The paper explicitly notes that some figures are generated from the statevector rather than measurement shots. No simulator backend name, noise model, cloud provider, transpilation settings, or physical quantum hardware model is specified.

### Reproducibility
Partial reproducibility only. The paper describes the circuit ideas, provides some mathematical relations, architecture figures, and key numerical results, but does not provide code, detailed Qiskit/DC scripts, full circuit listings, shot settings, backend configuration, or complete Monte Carlo parameterization. Data are synthetic and could in principle be recreated, but the implementation details are insufficient for straightforward full replication.
## Findings
- [supported] In a 12-qubit case study benchmarked against the JP Morgan option-pricing circuit, the proposed mixed-signal design reduced gate count from 4095 to 392.
- [supported] In the same 12-qubit comparison, circuit depth was reduced from 2048 to 6.
- [supported] The paper reports that digital calibration reduced maximum calculation error from 25.86% to 1.64%.
- [supported] The digital calibration method expanded the usable rotation-gate range to 0 to π/2 radians and was reported to tolerate angle deviations of about 0.05 radians without significant degradation.
- [supported] Simulation results showed that the proposed Monte Carlo price-simulation circuit produced average estimates consistent with classical Monte Carlo analysis for the linear portion of the workflow.
- [supported] The current implementation validates only linear computations; nonlinear components needed for full option pricing, including exponential and payoff functions, were not implemented.
- [supported] The reported Monte Carlo validation and histogram comparisons were generated from Qiskit statevector simulation rather than random measurement shots or real quantum hardware.
- [speculative] The authors claim exponential data pre-processing can reduce complexity from 2^n-1 gates to O(n^2) and depth from 2^n/2 to O(n), but the paper empirically demonstrates this only through a 12-qubit case study rather than broad asymptotic validation.
- [speculative] The authors argue that applying QAE to the proposed circuit could yield quantum advantages by requiring fewer measurements, but this was not empirically demonstrated in the reported experiments.
- [speculative] The paper claims the architecture is practical and extensible for real-world financial option pricing once nonlinear components are added, but full end-to-end option pricing was not implemented.

**Results summary:** This peer-reviewed empirical paper presents a mixed-signal quantum circuit design for option pricing and evaluates it primarily through simulation and circuit-level benchmarking rather than real-hardware execution. In a 12-qubit comparison against the JP Morgan option-pricing circuit, the authors report major reductions in gate count (4095 to 392), depth (2048 to 6), and maximum calculation error (25.86% to 1.64%) using exponential data pre-processing and digital calibration. The Monte Carlo component uses a single-qubit accumulator and is validated only for the linear averaging portion of the workflow; the required nonlinear exponential and payoff blocks for full option pricing are explicitly not implemented. Consistency with classical Monte Carlo is shown via statevector-based simulation outputs, indicating functional agreement for the tested linear subproblem. Claims of quantum advantage rely on the prospective use of QAE and remain theoretical/speculative in this paper.

**Performance claims:**
- 12-qubit case study: gate count reduced from 4095 to 392
- 12-qubit case study: circuit depth reduced from 2048 to 6
- Maximum calculation error reduced from 25.86% to 1.64%
- Rotation-gate usable range expanded to 0 to π/2 radians
- Approximate tolerance to angle deviations up to 0.05 radians without significant degradation
- Example scale discussed: 12 qubits / 4095 thread IDs or states in the synthesized design
- Example QAE parallelism claim discussed: 20 major qubits corresponding to 2^20 runs, with 4 Hadamard gates giving 2^24 total states evaluated simultaneously
## Quantum advantage claim
**Classification:** theoretical

The paper suggests that using QAE with the proposed circuit could provide a measurement-efficiency advantage, but the reported results are simulation-based, limited to linear subcircuits, and do not demonstrate end-to-end quantum advantage on real hardware or against classical runtime baselines.
## Limitations
- The current implementation is incomplete: only about 90% of the circuit has been implemented, and nonlinear components for exponential and payoff functions are still under development.
- Current Monte Carlo simulations validate only the linear portions of the circuit; the averaging operation is used for verification rather than full option pricing.
- The nonlinear components are not developed or described in the paper, so the full end-to-end option pricing workflow is not demonstrated.
- Experimental results are reported for a 12-qubit case study, limiting evidence for scalability to larger problem sizes.
- The probability distribution is discretized into 32 output levels with inputs ranging from 0 to 4095, indicating a relatively small and simplified experimental setting.
- Figures 11 and 12 are generated from the Statevector rather than random measurement shots, so the reported results do not fully reflect sampling noise or hardware measurement effects.
- The paper validates consistency against classical Monte Carlo analysis but does not demonstrate execution on real quantum hardware.
- Noise tolerance improvements are reported through digital calibration, but the evaluation appears simulation-based rather than based on noisy hardware experiments.
- The approach depends on classical preprocessing to isolate the relevant payoff region, meaning the quantum circuit cannot independently perform the full payoff calculation.
- The method relies on assumptions and approximations for analog calibration, including a fitted scaling factor (m = 1.57), whose robustness beyond the tested setting is unclear.
- [inferred] No benchmarking is provided against state-of-the-art classical option pricing solvers in terms of runtime, cost, or accuracy.
- [inferred] No reproducibility details such as code, synthesis scripts, parameter settings, or hardware configuration are provided, limiting replicability.
- [inferred] Claims of practical feasibility and industry relevance are not supported by deployment-scale experiments or production-like financial datasets.
- [inferred] The use of Synopsys Design Compiler suggests dependence on commercial tooling, which may hinder independent reproduction.
- [inferred] The study appears to use stylized or synthetic probabilistic models rather than real market data, limiting external validity for financial services applications.
- [inferred] The claimed complexity reductions are demonstrated on circuit design metrics (gate count/depth) but not on full application-level performance including data loading, calibration overhead, and end-to-end pricing accuracy.
## Open questions
- How will the proposed architecture perform once nonlinear exponential and payoff components are fully implemented?
- Can the reported gate-count, depth, and error improvements be maintained for larger qubit counts and more realistic option pricing instances?
- How robust is the digital calibration method under real hardware noise, decoherence, and device-specific imperfections?
- Does the mixed-signal design retain advantages when executed on actual quantum processors rather than statevector simulation?
- How much overhead is introduced by the required classical preprocessing and lookup-table calibration, and does it offset the claimed quantum benefits?
- Can the single-qubit price accumulator support more complex financial products or longer time-horizon simulations without loss of accuracy?
- How does the method compare with advanced classical Monte Carlo and quasi-Monte Carlo methods on realistic pricing tasks?
- What is the impact of discretization choices, such as 32 output levels and 12-qubit encoding, on pricing accuracy and scalability?
- Can the approach handle realistic market features such as stochastic volatility, path dependence, or multi-asset correlations?
- Is the analog calibration factor and LUT design transferable across different circuits, assets, and hardware platforms?

**Future work:**
- Extend the architecture to support nonlinear computations, especially exponential and payoff functions.
- Complete the full implementation of the option pricing circuit beyond the current linear validation stage.
- Reuse most of the proposed circuits with only minor modifications once nonlinear components become available.
- If nonlinear functions remain digital, replace only the Single-Qubit Accumulator while preserving the rest of the architecture.
- If analog implementations of nonlinear functions become feasible, preserve the entire current design and integrate those components.
- Further optimize the mixed-signal quantum design using commercial electronic design automation tools such as Synopsys Design Compiler.
- [inferred] Validate the approach on real quantum hardware with realistic noise and measurement shots.
- [inferred] Test scalability on larger qubit counts, more simulation paths, and more complex financial instruments.
- [inferred] Evaluate the method on real market data and production-relevant financial workloads.
- [inferred] Provide reproducible implementations and more comprehensive benchmarking against classical baselines.
## Key ideas
- #idea:hybrid-approach — Proposes a mixed-signal option-pricing architecture combining classical RTL/EDA synthesis and LUT-based digital calibration with quantum Monte Carlo components.
- #idea:near-term-feasibility — For a 12-qubit linear option-pricing subcircuit, reports major reductions in gate count (4095→392), depth (2048→6), and max error (25.86%→1.64%), suggesting improved NISQ implementability.
- #idea:near-term-feasibility — Demonstrates that the linear averaging/random-walk portion of the pricing workflow can reproduce classical Monte Carlo behavior in statevector simulation.
- #idea:quantum-advantage — Suggests prospective measurement-efficiency gains through Quantum Amplitude Estimation for Monte Carlo averaging, but this remains theoretical in the paper.
- #idea:hybrid-approach — Uses classical preprocessing to simplify state preparation and isolate relevant payoff regions, reducing circuit complexity at the expense of a fully quantum end-to-end workflow.
## Contradictions
- The paper claims scalable polynomial resource reductions for option pricing via preprocessing and calibration, but only linear subcircuits are implemented and validated; the missing nonlinear exponential/payoff blocks mean end-to-end scalability is unproven. This contrasts with the fuller option-pricing framing in 2021_JP_Morgan_OptionPricingCircuit.
- The paper implies potential quantum advantage through QAE-based averaging, yet all reported evidence is from statevector simulation without hardware execution, shot-based sampling, or runtime comparison to advanced classical pricing methods.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
