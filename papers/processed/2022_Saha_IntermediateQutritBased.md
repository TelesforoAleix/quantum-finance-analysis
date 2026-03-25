---
aliases:
- Intermediate Qutrit-based Improved Quantum Arithmetic Operations with Application
  on Financial Derivative Pricing
- Intermediate Qutrit based Improved
authors:
- Amit Saha
- Turbasu Chatterjee
- Anupam Chattopadhyay
- Amlan Chakrabarti
auto_detected: true
classification: ''
contradiction_flags:
- contradiction:classical-vs-quantum
- contradiction:scalability
doi: ''
evidence_type: ''
idea_tags:
- idea:quantum-advantage
- idea:near-term-feasibility
- idea:hybrid-approach
journal_or_venue: arXiv
methodology_tags:
- amplitude-estimation
- VQE
- classical-simulation
paper_type: ''
quantum_advantage_claim: speculative
related_papers:
- Chakrabarti_DerivativePricing
relevance_phase1: high
relevance_phase3: medium
source_type: preprint
source_type_confidence: high
step1_date: '2026-03-25T15:58:02.270447'
step1_model: gpt-5.1
step2_date: '2026-03-25T15:58:06.107106'
step2_model: gpt-5.1
step3_date: '2026-03-25T15:58:42.821763'
step3_model: gpt-5.4
step4_date: '2026-03-25T15:59:09.641499'
step4_model: gpt-5.4
step5_date: '2026-03-25T15:59:34.123235'
step5_model: gpt-5.4
step6_date: '2026-03-25T15:59:51.527604'
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
- method/VQE
- method/classical-simulation
- idea/quantum-advantage
- idea/near-term-feasibility
- idea/hybrid-approach
- contradiction/classical-vs-quantum
- contradiction/scalability
title: Intermediate Qutrit-based Improved Quantum Arithmetic Operations with Application
  on Financial Derivative Pricing
topic_tags:
- derivatives-pricing
year: 2022
zotero_key: ''
---

## Abstract summary
The paper develops more resource-efficient quantum arithmetic circuits (addition, multiplication, square root, exponential, arcsine) by using intermediate qutrit levels instead of ancilla qubits to decompose Toffoli gates. The authors then plug these improved arithmetic blocks into a known quantum derivative pricing algorithm based on re-parameterization and amplitude estimation, and show substantial reductions in gate count and circuit depth, particularly eliminating T gates. They also analyze noise and decoherence under realistic error models, arguing that despite accessing higher energy levels, the overall error probability is reduced due to shorter, shallower circuits.
## Methodology
This preprint is primarily a theoretical/resource-estimation study with limited numerical simulation. The authors decompose a previously proposed quantum derivative pricing workflow into its arithmetic subroutines and redesign the core arithmetic circuits—addition/subtraction, multiplication/division, square root, exponential, and arcsine—using intermediate qutrits for ancilla-free Toffoli decomposition. Their central methodological move is to replace standard qubit-only Toffoli decompositions with a 3-gate generalized ternary-CNOT construction that temporarily accesses the qutrit |2> level, thereby reducing gate count, circuit depth, T-count, and ancilla usage. They analytically derive new resource formulas for each arithmetic primitive and propagate these improvements to the derivative pricing application based on amplitude estimation and the re-parameterization method described in prior work. The paper also includes a worked multiplier example (5 x 3), simulated on Google Colab, to verify correctness of the intermediate-qutrit construction, and a numerical error analysis comparing success probabilities of the proposed Toffoli decomposition against conventional decompositions under gate-error and amplitude-damping noise models using Kraus-operator formalism. The derivative pricing case study itself appears to be evaluated through comparative resource analysis rather than full end-to-end execution on quantum hardware.

**Algorithms used:** Quantum Amplitude Estimation, Iterative Quantum Amplitude Estimation, Quantum Phase Estimation, Quantum Fourier Transform, Variational Quantum Eigensolver, Monte Carlo, Re-parameterization method
**Frameworks:** Google Colab

**Experimental setup:** The work is mainly analytical and simulation-based. A quantum multiplier circuit using intermediate qutrit decomposition was simulated on Google Colab to verify a 5 x 3 multiplication example. The paper also performs numerical success-probability analysis for Toffoli decompositions under assumed noise parameters rather than running on a real QPU. Hardware references to IBM devices are used only to motivate assumed error rates and relaxation times, not as execution platforms for the main experiments.

**Dataset:** No empirical financial dataset is used. The derivative pricing application is based on a theoretical benchmark case from prior work: a basket autocallable with 3 underlyings and 5 payment dates, and a knock-in put option with 20 barrier dates. The paper also uses a toy arithmetic input example for multiplier verification (5 x 3).
## Findings
- [supported] The paper proposes implementing core quantum arithmetic operations for derivative pricing using intermediate qutrit-based Toffoli decompositions, replacing ancilla-assisted qubit-only decompositions with 3 generalized ternary CNOT gates and no T gates.
- [supported] The proposed intermediate-qutrit Toffoli decomposition reduces per-Toffoli circuit depth from 7 to 3 and reported gate count from 25 to 3 relative to the conventional decomposition cited from prior work.
- [supported] Under the paper's resource model, the proposed approach makes T-depth and T-cost for the arithmetic subroutines effectively zero because no T gates are used in the decomposition.
- [supported] The authors derive revised resource formulas for addition/subtraction, multiplication/division, square root, exponential, and arcsine circuits when intermediate qutrit decompositions are substituted into prior arithmetic constructions.
- [supported] For the derivative pricing benchmark inherited from prior work (basket autocallable with 3 underlyings, 5 payment dates, and knock-in put with 20 barrier dates), the paper reports reducing overall circuit depth from at least 378 million to 162 million while setting reported T-cost and T-depth from 12 billion and 54 million to zero under their accounting.
- [supported] The paper presents a simulated example of a qutrit-based quantum multiplier for 5 x 3 and reports obtaining the correct output 15.
- [supported] The error analysis argues that although accessing higher qutrit levels increases per-gate error susceptibility, the lower gate count and shallower depth can improve total success probability relative to the conventional qubit-only decomposition.
- [supported] In the paper's numerical noise study for Toffoli-count-30 circuits, the intermediate-qutrit decomposition achieves about 0.4 success probability versus about 0.01 for the conventional decomposition, corresponding to an approximately 40% decrease in probability of error as stated by the authors.
- [speculative] The paper suggests that these arithmetic improvements can lower the cost of full quantum derivative pricing and improve robustness for future fault-tolerant quantum finance applications.
- [speculative] Claims that derivative pricing may exhibit quantum advantage and that the proposed arithmetic improvements help realize that advantage remain indirect in this paper because no end-to-end quantum advantage is empirically demonstrated.

**Results summary:** This preprint develops intermediate-qutrit versions of key arithmetic building blocks used in quantum derivative pricing, motivated by the resource bottleneck identified in prior finance algorithms. The main technical contribution is replacing standard ancilla- and T-gate-heavy Toffoli decompositions with a 3-gate generalized ternary CNOT construction that uses temporary qutrit states. Using this substitution, the authors provide updated resource estimates for addition, multiplication, square root, exponential, and arcsine circuits, and propagate these estimates to a previously studied derivative-pricing benchmark. They report large reductions in circuit depth and elimination of T-gate cost under their model, plus improved simulated success probabilities in a noise analysis despite the added vulnerability of higher-dimensional states. Evidence is based on analytical resource estimation, a small simulated multiplier example, and simulated/noise-model comparisons rather than real quantum hardware or end-to-end derivative-pricing execution, so broader claims about practical quantum finance impact remain speculative.

**Performance claims:**
- Per-Toffoli decomposition depth reduced from 7 to 3
- Per-Toffoli gate count reduced from 25 to 3
- T-depth becomes 0 for the proposed arithmetic constructions
- T-cost becomes 0 for the proposed arithmetic constructions
- Derivative pricing benchmark in prior work: 12 billion T-cost, 54 million T-depth, at least 378 million overall circuit depth
- Proposed method for same benchmark: 162 million ternary CNOT-cost / overall circuit depth reported
- Simulated multiplier example computes 5 x 3 = 15
- For Toffoli count 30, success probability approximately 0.4 for proposed decomposition versus approximately 0.01 for conventional decomposition
- Authors report approximately 40% decrease in probability of error for Toffoli count 30
## Quantum advantage claim
**Classification:** speculative

The paper discusses quantum advantage in derivative pricing by citing prior amplitude-estimation-based literature, but this preprint itself does not demonstrate end-to-end advantage on real hardware or with full empirical benchmarking. Its contribution is resource-estimation and simulated robustness improvements for arithmetic subroutines, so any advantage implication is speculative.
## Limitations
- Lack of peer review, as the work is presented as an arXiv preprint
- The approach requires access to higher energy levels (intermediate qutrits), making the design more prone to errors
- The paper acknowledges that higher-dimensional quantum systems introduce additional error beyond the standard truncation, discretization, amplitude-estimation, and arithmetic errors
- The analysis relies on resource estimation and numerical simulation rather than implementation on actual qutrit-based hardware
- The authors note the lack of mature qudit/qutrit hardware and explicitly state that explicit relaxation-time values are not broadly available except limited reported values, constraining realism of the error analysis
- Error and success-probability analysis assumes specific gate-error probabilities and coherence times rather than experimentally validated device parameters for the target application
- The paper does not optimize the total number of logical qubits for derivative pricing beyond removing ancillas used in Toffoli decomposition; it states that no other logical-qubit optimization is presented
- The financial application is demonstrated through decomposition and resource estimates for derivative pricing rather than end-to-end pricing experiments on real market data
- [inferred] The claimed improvement is largely at the arithmetic-subroutine level, so overall application-level quantum advantage for derivative pricing remains unproven
- [inferred] No direct benchmark against state-of-the-art classical derivative pricing methods is provided, limiting assessment of practical financial relevance
- [inferred] The derivative-pricing case study appears tied to assumptions from prior work (e.g., re-parameterization, fixed-point arithmetic, specific payoff structures), which may limit generality across broader financial products
- [inferred] The multiplier implementation is only illustrated on a very small toy example (5 x 3), which does not establish scalability to large arithmetic instances
- [inferred] The work assumes availability of generalized ternary gates with sufficient fidelity and compilation support, which may not hold on near-term production hardware
- [inferred] Reproducibility is partial: although code is mentioned for the multiplier simulation, full reproducible artifacts for all arithmetic circuits and derivative-pricing resource analyses are not clearly provided
## Open questions
- How well do intermediate-qutrit arithmetic circuits perform on real qutrit or qudit hardware rather than in simulation and analytical estimates?
- Will the reduction in gate count and circuit depth continue to outweigh the higher physical error rates associated with accessing higher energy levels at larger scales?
- What are the true hardware-specific fidelities, coherence properties, and calibration overheads for the generalized ternary gates required by this approach?
- How do these qutrit-based arithmetic improvements translate into end-to-end performance for full derivative-pricing workflows under realistic fault-tolerant or noisy conditions?
- Can the approach be generalized effectively to other quantum finance tasks beyond the derivative-pricing setting studied here?
- What is the crossover point at which qutrit-based arithmetic yields practical advantage over qubit-only arithmetic once compilation, control, and hardware overheads are included?
- How scalable are the proposed circuits for larger register sizes, more assets, more timesteps, and more complex path-dependent derivatives?
- How sensitive are the reported success-probability gains to the assumed noise model and to different device architectures?

**Future work:**
- Carry out more detailed time-improvement estimates using intermediate qudits
- Study decomposition with intermediate qudits for other quantum circuits beyond the arithmetic and derivative-pricing circuits considered
- Investigate the proposed arithmetic operations and derivative-pricing circuits on actual higher-dimensional quantum hardware when available
- Develop more realistic error analyses using experimentally validated qutrit/qudit noise parameters
- Explore further optimizations beyond gate count and depth, including logical-qubit reduction and broader circuit-level improvements
- Extend the intermediate-qutrit methodology to additional financial applications and more complex derivative products
- [inferred] Perform end-to-end empirical validation of derivative pricing, including real-data or realistic synthetic financial benchmarks
- [inferred] Compare against strong classical baselines and full-stack quantum implementations to assess practical advantage
## Key ideas
- #idea:quantum-advantage — The paper claims qutrit-based arithmetic can substantially reduce resource costs in amplitude-estimation-based derivative pricing by cutting Toffoli depth and eliminating T-gates in the accounting model.
- #idea:near-term-feasibility — By removing ancilla-heavy qubit-only decompositions and shortening circuits, the authors position intermediate-qutrit arithmetic as a more practical route for NISQ or early fault-tolerant finance circuits.
- #idea:hybrid-approach — The derivative-pricing workflow builds on re-parameterization/path-loading methods linked to VQE-style hybrid quantum-classical components rather than a fully standalone quantum pipeline.
- #idea:quantum-advantage — The contribution is primarily at the arithmetic-subroutine level: improved addition, multiplication, square root, exponential, and arcsine blocks are propagated into lower estimated derivative-pricing costs.
- #idea:near-term-feasibility — Noise analysis argues that despite higher-dimensional operations being individually riskier, total success probability may improve because the circuit is much shorter and shallower.
## Contradictions
- The paper gestures toward quantum advantage in derivative pricing, but its own evidence is simulation/resource-estimation only and includes no end-to-end benchmark against strong classical pricing methods; this weakens any superiority claim and supports #contradiction:classical-vs-quantum.
- The paper suggests improved practicality via qutrit-based arithmetic, yet it simultaneously acknowledges immature qutrit hardware, assumed rather than measured device parameters, and only a toy 5x3 multiplier demonstration; this undercuts claims of scalability to realistic financial workloads and supports #contradiction:scalability.
- Relative to prior derivative-pricing work such as Chakrabarti_DerivativePricing, this paper reports large reductions in estimated quantum resources, but those gains depend on a different gate model using generalized ternary operations that are not available or validated on comparable hardware, making direct practical comparisons uncertain.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->

## Experiment details
### Input
Inputs consist of (1) symbolic/arithmetic circuit specifications for addition, multiplication, square root, exponential, and arcsine; (2) a toy multiplier instance encoding 5 and 3 into qubit registers for circuit verification; and (3) benchmark derivative-pricing resource parameters inherited from prior work, including a basket autocallable with 3 underlyings and 5 payment dates and a knock-in put with 20 barrier dates. For noise analysis, assumed gate-error probabilities are used: one-qubit error 10^-4, two-qubit error 10^-2, two-qutrit error treated at the same nominal scale in the comparison, with relaxation times T11 = 100 microseconds and T12 = 30 microseconds.

### Process
1. Start from the derivative pricing algorithm of prior work and identify arithmetic subroutines required for path loading and payoff computation, especially square root and arcsine. 2. Replace conventional qubit-only Toffoli decompositions with an intermediate-qutrit decomposition using three generalized ternary CNOT gates and no ancilla or T gates. 3. Re-express resource formulas for addition/subtraction, multiplication/division, square root, exponential, and arcsine in terms of ternary CNOT count and reduced circuit depth. 4. Demonstrate the construction concretely on a quantum multiplier example for 5 x 3, initializing input qubits, applying Toffoli-based multiplication logic, decomposing all Toffoli gates via intermediate qutrits, and measuring output qubits to verify the result 15. 5. Compare the resulting arithmetic and derivative-pricing resource estimates against the baseline from Chakrabarti et al. [6], focusing on T-count, T-depth, overall depth, and gate count. 6. Perform error analysis using Kraus-operator noise models for gate errors and amplitude damping, and compute probability of success for repeated Toffoli decompositions as a function of Toffoli count, including a comparison at Toffoli count 30.

### Output
Outputs are analytical resource estimates and comparative performance figures rather than predictive financial metrics. Reported outputs include formulas for generalized ternary-CNOT counts for arithmetic operations, reduced circuit depth for Toffoli decomposition (3 vs. 7), elimination of T-depth/T-count, derivative-pricing benchmark resource totals (e.g., baseline 12 billion T-cost and 54 million T-depth versus proposed zero T-cost/T-depth and 162 million overall circuit depth), and numerical success-probability/error comparisons under noise. The multiplier simulation outputs the correct arithmetic result 15 for the 5 x 3 example. Comparisons are made primarily against the prior state-of-the-art derivative pricing implementation and conventional Toffoli decomposition methods.

### Parameters
- toffoli_decomposition_depth_proposed: 3
- toffoli_decomposition_depth_baseline: 7
- toffoli_gate_count_proposed: 3
- toffoli_gate_count_baseline: 25
- two_qutrit_gates_per_toffoli: 3
- ancilla_qubits_for_proposed_toffoli: 0
- t_depth_proposed: 0
- toy_multiplier_example: 5 x 3
- noise_parameters: {'one_qubit_gate_error': 0.0001, 'two_qubit_gate_error': 0.01, 'assumed_two_qutrit_gate_error_scale': 0.01, 'T11_microseconds': 100, 'T12_microseconds': 30}
- benchmark_derivative_pricing_case: {'basket_autocallable_underlyings': 3, 'basket_autocallable_payment_dates': 5, 'knock_in_put_barrier_dates': 20}

### Hardware
{'execution_environment': 'Google Colab simulation for multiplier example', 'real_qpu_used': False, 'simulator_details': 'Not explicitly named', 'hardware_references_for_noise_assumptions': ['IBM Quantum devices (for representative qubit error rates and T1)', 'qutrit relaxation time from prior experimental work']}

### Reproducibility
Partial reproducibility. The paper provides substantial analytical detail and explicit resource formulas, and states that code for the multiplier simulation is available at a GitHub repository (https://github.com/LegacYFTw/NTU). However, no full end-to-end derivative pricing implementation, simulator configuration, or comprehensive experimental scripts are described, so the arithmetic/resource-analysis portions are more reproducible than the full application-level claims.
