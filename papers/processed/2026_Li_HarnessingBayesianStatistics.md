---
aliases:
- Harnessing Bayesian Statistics to Accelerate Iterative Quantum Amplitude Estimation
- Harnessing Bayesian Statistics Accelerate
authors:
- Qilin Li
- Atharva Vidwans
- Yazhen Wang
- Micheline B. Soley
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
journal_or_venue: Quantum
methodology_tags:
- VQE
- amplitude-estimation
- classical-simulation
paper_type: ''
quantum_advantage_claim: theoretical
related_papers: []
relevance_phase1: medium
relevance_phase3: low
source_type: peer-reviewed-empirical
source_type_confidence: high
step1_date: '2026-03-25T16:15:16.060558'
step1_model: gpt-5.1
step2_date: '2026-03-25T16:15:21.551743'
step2_model: gpt-5.1
step3_date: '2026-03-25T16:15:54.482945'
step3_model: gpt-5.4
step4_date: '2026-03-25T16:16:39.156557'
step4_model: gpt-5.4
step5_date: '2026-03-25T16:17:17.591904'
step5_model: gpt-5.4
step6_date: '2026-03-25T16:17:30.454027'
step6_model: gpt-5.4
steps_completed:
- 1
- 2
- 3
- 4
- 5
- 6
tags:
- method/VQE
- method/amplitude-estimation
- method/classical-simulation
- idea/quantum-advantage
- idea/near-term-feasibility
- idea/hybrid-approach
- contradiction/classical-vs-quantum
- contradiction/scalability
title: Harnessing Bayesian Statistics to Accelerate Iterative Quantum Amplitude Estimation
topic_tags: []
year: 2026
zotero_key: ''
---

## Abstract summary
The paper develops a unified statistical framework for several quantum amplitude estimation (QAE) algorithms and uses it to introduce Bayesian Iterative Quantum Amplitude Estimation (BIQAE), which injects Bayesian inference into Iterative QAE. The authors analyze BIQAE theoretically via asymptotic mean squared error and normal approximations, and implement both normal- and beta-prior variants to quantify how Bayesian updating reduces quantum sample complexity relative to existing QAE methods. Numerical simulations on generic amplitudes and on molecular ground-state energy estimation show that BIQAE achieves a consistent constant-factor reduction in oracle calls compared to IQAE and other state-of-the-art QAE schemes, highlighting the role of Bayesian statistics in lowering measurement costs in quantum algorithms.
## Methodology
The paper develops and empirically evaluates Bayesian Iterative Quantum Amplitude Estimation (BIQAE), a Bayesian enhancement of Iterative Quantum Amplitude Estimation (IQAE). Methodologically, the study combines formal statistical analysis with numerical simulation. It first formulates Classical QAE, Amplified Amplitude Estimation (AAE), and IQAE in a unified asymptotic mean squared error and normal-approximation framework, then injects Bayesian inference into IQAE to create BIQAE. Two implementations are studied: Normal-BIQAE, using normal priors and delta-method prior propagation, and Beta-BIQAE, using beta priors with conjugate beta-binomial updates and stage-to-stage prior preparation via transformed posterior sampling and MLE fitting. The empirical part benchmarks BIQAE against Canonical QAE, Classical QAE, IQAE variants, Bayesian Amplitude Estimation (BAE), MLQAE, FQAE, and QAES on amplitude-estimation tasks and on molecular ground-state energy estimation. Performance is assessed primarily through quantum sample complexity versus target accuracy/error, interval radius, coverage rate, and regression-based scaling analysis. For chemistry experiments, molecular Hamiltonians are generated classically, ground states are prepared with VQE, and QAE methods are then used for expectation-value/energy estimation. The study is simulation-based rather than hardware-executed, with repeated trials used to compute summary statistics and robustness across amplitudes, accuracies, molecules, bond lengths, and Pauli terms.

**Algorithms used:** BIQAE, IQAE, Classical QAE, AAE, Canonical QAE, BAE, MLQAE, FQAE, QAES, VQE
**Frameworks:** Qiskit, Qiskit Nature, PySCF

**Experimental setup:** All results are obtained via numerical simulations/classical emulation rather than on a real QPU. For amplitude-scaling experiments, the authors use a simplified single-qubit mock circuit with an oracle A and a mock Grover operator implemented via a single RY(2kθ) rotation to emulate Q^k while accounting analytically for oracle-call complexity and circuit depth. For molecular experiments, electronic Hamiltonians are generated classically and ground states are prepared with VQE before applying QAE-based expectation estimation. Experiments are repeated 200 times for most benchmark studies and 1000 times for some robustness analyses.

**Dataset:** Two types of inputs are used: (1) synthetic/specified quantum amplitudes, especially a benchmark amplitude a = 0.5 and sweeps over a in [0,1], for quantum sample complexity studies; and (2) molecular electronic structure data for H2, LiH, HF, and BeH2 across equilibrium and nonequilibrium bond lengths, with Hamiltonians generated at the Hartree-Fock level under the Born-Oppenheimer approximation and decomposed into Pauli terms for energy estimation.
## Experiment details
### Input
Amplitude-estimation benchmarks use prescribed amplitudes, primarily a = 0.5, plus sweeps over a in [0,1] and target accuracies spanning roughly 10^-2 to 10^-8. Molecular experiments use four molecules (H2, LiH, HF, BeH2); Hamiltonians are generated at the Hartree-Fock level with frozen core orbitals, Born-Oppenheimer approximation, Jordan-Wigner mapping and qubit tapering in the main text (appendix also notes parity mapping via Qiskit Nature, with Jordan-Wigner for H2), and expectation values of Pauli strings are estimated. Equilibrium bond lengths are assumed unless otherwise stated, and bond-length sweeps are included. Qubit counts after tapering are reported as H2: 4, LiH: 6, HF: 6, BeH2: 7.

### Process
For BIQAE, the algorithm proceeds in stages. At each stage t, a circuit with k_t Grover applications is measured; outcomes are mapped to Bernoulli samples and aggregated. In Normal-BIQAE, a normal prior over the amplified probability p_k is updated using a normal-approximated likelihood; in Beta-BIQAE, a beta prior is updated exactly via the beta-binomial conjugate posterior. A credible interval for p_k is computed from posterior quantiles, transformed into an interval for theta, and used to determine the next feasible Grover count k via a linear search as in standard-scheduled IQAE. When moving to a new stage, the posterior is transformed into the next-stage prior; for Beta-BIQAE this is done by drawing R = 1000 posterior samples, transforming them through the stage transition map, and fitting a beta distribution by MLE. Relevant hyperparameters include confidence level alpha = 0.05 and incremental shot batch size N_incre = 10. For amplitude benchmarks, each method is run repeatedly and compared on sample complexity versus median absolute error/target accuracy. For molecular experiments, Hamiltonians are generated classically, the ground-state wavefunction is prepared with VQE using an efficient SU(2) ansatz with full entanglement and SLSQP optimization, and then Classical QAE, IQAE-CP, and Beta-BIQAE are used to estimate Pauli-term expectation values and total energies. Molecular results are averaged over 200 repetitions; some robustness analyses use 1000 repetitions.

### Output
Outputs include quantum sample complexity (oracle calls or Grover-weighted shots), median absolute error, interval/credible interval radius, coverage rate, fitted log-log scaling slopes/intercepts/R^2 from linear regression, and percentage improvement of BIQAE over baselines. Baselines include Canonical QAE, Classical QAE, IQAE-CP, IQAE-CH, BAE, MLQAE (EIS and LIS), FQAE, and QAES for amplitude estimation; and Classical QAE and IQAE-CP for molecular energy estimation. Molecular outputs include estimated ground-state energies, interval centers and error bars, Pauli-string-level sample complexities, and comparisons against exact diagonalization energies and against competing QAE methods.

### Parameters
- confidence_level_alpha: 0.05
- incremental_shot_batch_size_N_incre: 10
- beta_prior_sampling_R: 1000
- repetitions_main: 200
- repetitions_robustness: 1000
- benchmark_amplitude: 0.5
- target_accuracy_range_amplitude: approximately 1e-2 to 1e-8
- molecular_target_accuracy: {'default': 0.001, 'HF': 0.0001}
- molecules: ['H2', 'LiH', 'HF', 'BeH2']
- qubits_after_tapering: {'H2': 4, 'LiH': 6, 'HF': 6, 'BeH2': 7}
- vqe_ansatz: efficient SU(2) ansatz with full entanglement
- vqe_optimizer: SLSQP
- vqe_max_iterations: {'H2': 300, 'LiH': 300, 'HF': 300, 'BeH2': 500}
- vqe_ansatz_layers: {'H2': 12, 'LiH': 12, 'HF': 12, 'BeH2': 15}

### Hardware
{'execution_type': 'classical numerical simulation; no real QPU used', 'amplitude_benchmark_circuit': 'single-qubit mock circuit using RY(2kθ) to emulate Q^k', 'chemistry_estimation_backend': 'Qiskit Runtime Estimator primitive with zero shots for classical expectation evaluation during VQE', 'noise_model': 'none applied in experiments; noise discussed only conceptually for future work'}

### Reproducibility
Code is reported as publicly available on GitHub for BIQAE, and benchmark BAE code is also available with minor modifications. The paper provides substantial algorithmic detail, pseudocode, parameter settings, benchmark definitions, molecule list, ansatz/optimizer choices, and repetition counts, making replication largely feasible. Data are generated from standard public chemistry software workflows rather than a fixed external dataset. Some implementation details are complex and there is minor mapping-description inconsistency between main text and appendix, but overall reproducibility is good.
## Findings
- [supported] The paper introduces Bayesian Iterative Quantum Amplitude Estimation (BIQAE) and reports that Beta-BIQAE has lower quantum sample complexity than all other QAE methods evaluated, including IQAE-CP, IQAE-CH, BAE, MLQAE, Canonical QAE, FQAE, QAES, and Classical QAE, in numerical simulations.
- [supported] For benchmark amplitude estimation at a = 0.5, Beta-BIQAE maintained an advantage over competing methods across five orders of magnitude in median absolute error in simulation.
- [supported] Linear regression on log-log scaling for a = 0.5 gave Beta-BIQAE slope -1.0088, intercept 0.0211, R^2 = 0.9999, versus Classical QAE slope -1.9821, intercept -1.1693, R^2 = 0.9996, consistent with quadratic improvement in sample complexity over Classical QAE.
- [supported] Relative to IQAE-CP, Beta-BIQAE reduced quantum sample complexity by about 14% across six orders of magnitude in target accuracy in simulation.
- [supported] Across amplitudes a in [0,1] at fixed target accuracy epsilon = 1e-8, Beta-BIQAE improved over IQAE-CP by approximately 12% to 15% in quantum sample complexity in simulation.
- [supported] For molecular ground-state energy estimation of H2, LiH, HF, and BeH2, Beta-BIQAE produced significantly smaller interval estimates than Classical QAE at fixed quantum sample complexity, with average interval-width reduction factors of 14.2x for H2, 12.13x for LiH, 32.84x for HF, and 12.16x for BeH2.
- [supported] At fixed quantum sample complexity, Beta-BIQAE interval centers were on average closer to exact diagonalization than Classical QAE by 0.020 Hartree for H2, 0.004 Hartree for LiH, 0.137 Hartree for HF, and 0.002 Hartree for BeH2.
- [supported] For molecular energy estimation at target accuracy epsilon = 1e-3 (and epsilon = 1e-4 for HF), Beta-BIQAE required two to three orders of magnitude fewer samples than Classical QAE across bond lengths considered; HF at epsilon = 1e-4 showed a three-order-of-magnitude reduction.
- [supported] For molecular energy estimation, Beta-BIQAE consistently required 8% to 13% lower sample complexity than IQAE-CP across all molecular tests considered.
- [supported] For individual Pauli-term expectation estimation, Beta-BIQAE reduced average quantum sample complexity relative to Classical QAE by up to three orders of magnitude for epsilon = 1e-3 and up to four orders of magnitude for epsilon = 1e-4.
- [supported] For individual Pauli terms, Beta-BIQAE improved over IQAE-CP by average percentages of 10.16% for H2, 10.72% for LiH, 11.4% for HF, and 10.5% for BeH2.
- [supported] Beta-based methods (Beta-BIQAE and IQAE-CP) outperformed normal-based variants in the small per-stage sample regime; Beta-BIQAE and IQAE-CP achieved the target 0.95 coverage rate across tested accuracies, while Normal-BIQAE and Normal-IQAE did not.
- [supported] The authors report that Beta-BIQAE's measurement-cost reduction over IQAE-CP was achieved without a significant increase in circuit depth, as the average number of Grover operators in the last stage was similar between the two methods in simulations.
- [speculative] The authors argue that Bayesian inference is the direct source of the observed speedup and suggest this may indicate a broader route to accelerating quantum algorithms beyond QAE.
- [speculative] The paper suggests BIQAE could be adapted for near-term noisy hardware using noise-aware schedules or restrictions on Grover-operator counts, but this was not empirically demonstrated on hardware in this study.
- [speculative] The paper frames the BIQAE improvement as a 'proof of the quantum speedup offered by Bayesian statistics,' but the evidence is based on mathematical analysis and classical numerical simulation rather than demonstrated hardware-level quantum advantage.

**Results summary:** This peer-reviewed empirical paper presents BIQAE, a Bayesian enhancement of iterative quantum amplitude estimation, and evaluates it primarily through analytical derivations and classical numerical simulations rather than real quantum hardware. The strongest empirical result is that Beta-BIQAE consistently lowers quantum sample complexity relative to benchmark QAE methods. For benchmark amplitude estimation at a = 0.5, Beta-BIQAE showed the best simulated performance across five orders of magnitude in error, with scaling consistent with O(1/epsilon) and a lower constant factor than alternatives. Compared with IQAE-CP, Beta-BIQAE achieved a near-constant sample-complexity reduction of about 14% across six orders of magnitude in target accuracy and about 12% to 15% across the full amplitude range at epsilon = 1e-8. In molecular ground-state energy estimation for H2, LiH, HF, and BeH2, Beta-BIQAE produced much tighter intervals than Classical QAE at equal sample budgets and required two to three orders of magnitude fewer samples than Classical QAE to reach target accuracy, while also improving over IQAE-CP by roughly 8% to 13%. All reported empirical results are simulation-based; no real-hardware demonstration is provided.

**Performance claims:**
- Beta-BIQAE log-log scaling for a = 0.5: slope -1.0088, intercept 0.0211, R^2 = 0.9999
- Classical QAE log-log scaling for a = 0.5: slope -1.9821, intercept -1.1693, R^2 = 0.9996
- IQAE-CP log-log scaling: slope -1.0044, intercept 0.1253, R^2 = 0.9999
- BAE log-log scaling: slope -1.0137, intercept 0.1089, R^2 = 0.9996
- Beta-BIQAE has an intercept about 5x lower than IQAE-CP in the fitted scaling comparison
- Approximately 14% lower quantum sample complexity for Beta-BIQAE versus IQAE-CP across six orders of magnitude in target accuracy
- Observed interval radius ratio epsilon_(t-1)/epsilon_t approximately 2.5, corresponding to about 16% predicted improvement
- Approximately 12% to 15% lower quantum sample complexity for Beta-BIQAE versus IQAE-CP across amplitudes a in [0,1] at epsilon = 1e-8
- Average interval-size reduction versus Classical QAE at fixed sample complexity: 14.2x for H2, 12.13x for LiH, 32.84x for HF, 12.16x for BeH2
- Average improvement in interval-center closeness to exact diagonalization versus Classical QAE: 0.020 Hartree for H2, 0.004 Hartree for LiH, 0.137 Hartree for HF, 0.002 Hartree for BeH2
- Two to three orders of magnitude lower sample complexity than Classical QAE for molecular energy estimation at epsilon = 1e-3; three orders for HF at epsilon = 1e-4
- 8% to 13% lower sample complexity than IQAE-CP across all molecular tests
- For individual Pauli terms, up to 3 orders of magnitude lower sample complexity than Classical QAE at epsilon = 1e-3
- For individual Pauli terms, up to 4 orders of magnitude lower sample complexity than Classical QAE at epsilon = 1e-4
- Average percent improvement over IQAE-CP for Pauli terms: 10.16% (H2), 10.72% (LiH), 11.4% (HF), 10.5% (BeH2)
- Coverage-rate comparison: Beta-BIQAE and IQAE-CP achieved target coverage 0.95 across tested accuracies, while Normal-BIQAE and Normal-IQAE did not
## Quantum advantage claim
**Classification:** theoretical

The paper claims a speedup from injecting Bayesian inference into IQAE and provides mathematical sample-complexity analysis plus simulation evidence showing lower oracle/sample complexity than competing QAE methods. However, results are not demonstrated on real quantum hardware, so this is best classified as theoretical rather than demonstrated quantum advantage.
## Limitations
- The method is validated primarily through analytical results and numerical simulations rather than execution on real quantum hardware.
- Practical implementation on current near-term quantum computers requires accounting for realistic noise conditions; a naive BIQAE implementation would likely be impacted similarly to IQAE at high Grover-operator counts.
- Under the noise model discussed, measurement outcome probabilities decay exponentially toward 1/2 as the number of Grover operators increases, creating a tradeoff between stochastic noise reduction and biased noise amplification in the absence of error correction.
- This tradeoff presently prevents IQAE from fully achieving its predicted efficiency gains, implying BIQAE may also fail to realize its theoretical gains on NISQ hardware without modification.
- Normal-BIQAE relies on normal approximations and variance estimation accuracy; its performance deteriorates for small per-stage sample sizes, increasing both quantum sample complexity and loss of nominal coverage.
- Normal-based methods can suffer from zero-variance estimates and diminished coverage in small-sample regimes, requiring a minimum sample size safeguard in implementation.
- The exact prior distribution after posterior-to-prior transformation is no longer normal or beta, so both Normal-BIQAE and Beta-BIQAE rely on approximation when preparing the next-stage prior.
- Beta-BIQAE does not admit a closed-form prior update and instead uses a sampling-based approximation with finite sample size (e.g., R = 1000), introducing approximation error.
- The authors note that although the fitted beta prior is asymptotically optimal within the beta family, it is not guaranteed to be close to the exact transformed prior.
- A rigorous theoretical justification that beta distributions can closely approximate the transformed priors encountered in BIQAE is explicitly left unresolved.
- The analytical sample-complexity improvement is derived for Normal-BIQAE; the paper does not provide an analogous closed-form analytical result for Beta-BIQAE despite Beta-BIQAE being the practically superior variant.
- Some theoretical guarantees depend on assumptions such as large-sample normality or Assumption 2 for the base-3 schedule, limiting direct applicability of those derivations.
- Molecular experiments are limited to a small set of benchmark molecules (H2, LiH, HF, BeH2), which constrains evidence for broader scalability.
- Ground-state energy experiments use classically prepared/simulated workflows (e.g., VQE state preparation and classical simulation settings), not end-to-end fault-tolerant quantum execution.
- The target accuracy for HF had to be restricted to 10^-4 because estimation error grows with the number and coefficient magnitude of Pauli terms, indicating scaling challenges for more complex systems.
- [inferred] No experiments are reported on finance-specific datasets or financial workloads despite the paper motivating QAE as important for finance.
- [inferred] The study does not benchmark against state-of-the-art classical Monte Carlo or statistical estimation baselines for end-use applications, limiting assessment of practical quantum advantage.
- [inferred] Reproducibility is aided by open-source code, but results may still depend on implementation choices such as hyperparameters, stopping criteria, and prior-fitting sample size.
- [inferred] Scalability to production financial services is untested because the work focuses on subroutine-level amplitude estimation rather than full financial pipelines under operational constraints.
- [inferred] Resource requirements beyond oracle-call/sample complexity—such as wall-clock runtime, classical optimization overhead, memory use, and fault-tolerant logical qubit costs—are not fully quantified.
## Open questions
- How can BIQAE be modified for robust implementation on current and future quantum computers under realistic noise conditions?
- Can noise-aware schedules and restrictions on the number of Grover operators be designed specifically for BIQAE to preserve its gains on NISQ hardware?
- Will BIQAE retain its theoretical advantage over IQAE and BAE when executed on real superconducting or trapped-ion devices?
- Can Bayesian inference be injected not only at the interval-estimation level but also at the level of hyperparameter selection or (K,N)-scheduling decisions for further gains?
- What is the best Bayesian-informed schedule for BIQAE, and how does it compare empirically and theoretically with the IQAE-style schedule used here?
- Can the transformed prior distributions encountered in Beta-BIQAE always be well approximated by beta distributions in practice, and under what formal conditions?
- Can a closed-form or rigorous sample-complexity theory be developed for Beta-BIQAE analogous to the Normal-BIQAE bound?
- What explains the repeated deviations from ideal scaling laws at similar amplitude values across target accuracies observed in the appendix experiments?
- How does BIQAE perform for larger, more chemically or financially realistic problem instances with many more terms and tighter accuracy requirements?
- [inferred] How much of the reported improvement survives when full application overheads, including state preparation and data loading, are included?
- [inferred] For financial services use cases, does BIQAE improve end-to-end tasks such as option pricing, VaR, CVA, or risk aggregation enough to matter in production settings?

**Future work:**
- Develop further schemes that capitalize on Bayesian inference in QAE and reduce measurement cost from a Bayesian rather than frequentist perspective.
- Inject Bayesian inference into BIQAE at the level of hyperparameters or (K,N)-scheduling decisions.
- Use Bayesian optimization to tune BIQAE hyperparameters such as per-stage sample size Nt and incremental shot batch size Nincre.
- Replace the schedule used for direct comparison with IQAE by a Bayesian-informed schedule such as that used in BAE.
- Modify BIQAE for implementation on current near-term intermediate-scale quantum computers.
- Design and test noise-aware schedules and restrictions on the number of Grover operators to make BIQAE robust under realistic noise.
- Leverage strategies from prior QAE implementations on superconducting and trapped-ion hardware, including NISQ accommodations from RAE and BAE.
- Demonstrate BIQAE on far-term fault-tolerant quantum computers with sufficiently reliable logical qubits and low-error gates.
- Apply BIQAE to facilitate identification of molecular excited states in conjunction with quantum tomography techniques.
- Explore broader use of Bayesian inference to accelerate other frequentist tasks in quantum algorithms.
- Provide rigorous theoretical justification for the quality of beta-family approximations to transformed priors in Beta-BIQAE.
- Investigate the amplitude-dependent deviations from scaling laws observed in numerical experiments.
- [inferred] Extend evaluation to real hardware experiments and finance-specific QAE applications to test practical relevance in financial services.
## Key ideas
- #idea:quantum-advantage — BIQAE, especially Beta-BIQAE, is presented as reducing oracle/sample complexity versus IQAE and Classical QAE, with simulated O(1/ε) scaling and constant-factor gains over IQAE-CP.
- #idea:hybrid-approach — The method is a hybrid quantum-classical scheme combining amplitude estimation with classical Bayesian posterior updating and adaptive scheduling.
- #idea:near-term-feasibility — The paper suggests BIQAE may be adapted to NISQ hardware using noise-aware schedules and bounded Grover depth, though this is only proposed and not demonstrated.
- #idea:quantum-advantage — In simulated molecular energy-estimation experiments, BIQAE reduces measurement cost relative to Classical QAE and modestly improves over IQAE-CP, indicating potential value for QAE subroutines used in finance.
- #limitation:simulation-only — All empirical evidence comes from classical numerical simulation/emulation rather than execution on a real QPU.
- #limitation:noise — Realistic hardware noise is not experimentally modeled; the paper itself notes that noise may erase predicted gains at high Grover counts.
- #limitation:no-empirical-validation — The work does not validate BIQAE on finance-specific tasks such as option pricing, VaR, or CVA despite motivating relevance to finance.
## Contradictions
- The paper frames BIQAE as evidence of quantum speedup, but benchmarks are only against other QAE variants under classical simulation and not against strong classical Monte Carlo baselines, weakening any claim of practical quantum superiority.
- The paper suggests near-term applicability, yet its own limitations state that noise amplification at larger Grover counts may prevent BIQAE and IQAE from realizing theoretical gains on NISQ hardware.
- Scalability to realistic financial workloads is implied through QAE relevance, but the experiments are limited to synthetic amplitudes and small molecular benchmarks rather than end-to-end finance applications.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
