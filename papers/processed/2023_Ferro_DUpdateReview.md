---
aliases:
- 'D5.7: Update of review of state-of-the-art for Pricing and Computation of VaR'
- D Update review state
authors:
- Gonzalo Ferro
- Alberto Manzano
- Andrés Gómez
- Carlos Vázquez
- María R. Nogueiras
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
journal_or_venue: NExt ApplicationS of Quantum Computing (NEASQC) Project, Horizon
  2020
methodology_tags:
- amplitude-estimation
- grover
- quantum-ML
- quantum-walk
- quantum-simulation
paper_type: ''
quantum_advantage_claim: theoretical
related_papers:
- 2022_Gomez_D53
relevance_phase1: high
relevance_phase3: high
source_type: technical-report
source_type_confidence: high
step1_date: '2026-03-25T16:00:21.819002'
step1_model: gpt-5.1
step2_date: '2026-03-25T16:00:28.260634'
step2_model: gpt-5.1
step3_date: '2026-03-25T16:00:41.216802'
step3_model: gpt-5.4
step4_date: '2026-03-25T16:01:35.605804'
step4_model: gpt-5.4
step5_date: '2026-03-25T16:02:26.489798'
step5_model: gpt-5.4
step6_date: '2026-03-25T16:02:47.237529'
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
- topic/asset-pricing
- method/amplitude-estimation
- method/grover
- method/quantum-ML
- method/quantum-walk
- method/quantum-simulation
- idea/quantum-advantage
- idea/near-term-feasibility
- idea/hybrid-approach
- contradiction/classical-vs-quantum
- contradiction/scalability
title: 'D5.7: Update of review of state-of-the-art for Pricing and Computation of
  VaR'
topic_tags:
- derivatives-pricing
- risk-modelling
- asset-pricing
year: 2023
zotero_key: ''
---

## Abstract summary
This technical report from the NEASQC project updates a prior survey on quantum computing methods for derivatives pricing and Value at Risk, with a focus on developments since 2022. It reviews advances in quantum-accelerated Monte Carlo, including state initialization and amplitude estimation techniques, as well as quantum algorithms for PDE-based pricing and other approaches such as quantum reinforcement learning and quantum-inspired asset pricing models. The authors particularly emphasize the practical constraints of NISQ hardware and the impact of noise on realizing theoretical speedups in financial applications.
## Methodology
This technical report is an updated state-of-the-art review produced within the NEASQC project on quantum computing methods for derivatives pricing and Value at Risk (VaR). Its methodology is a structured literature review scoped to publications appearing after the consortium’s earlier deliverable D5.3 (Gomez et al., 2022), with emphasis on methods relevant to NISQ hardware. The report organizes the surveyed literature into three main technical domains: (1) Quantum Accelerated Monte Carlo (QAMC), including its core pipeline of probability-distribution loading oracle construction, payoff encoding, and amplitude-estimation-based readout; (2) quantum algorithms for solving PDE-based pricing models; and (3) other approaches such as quantum machine learning, quantum-inspired financial modeling, martingale asset pricing, and quantum assets. Within QAMC, the report further classifies work into initialization/state-preparation methods and amplitude estimation methods, and subdivides amplitude estimation into parallel algorithms, sequential/iterative algorithms, and generalized-Grover approaches. The report synthesizes technical specifications such as asymptotic query complexity, circuit depth/width trade-offs, auxiliary-qubit requirements, noise sensitivity, and NISQ suitability, and includes a comparative performance table for amplitude estimation algorithms in terms of oracle-call complexity as a function of target precision and confidence. The scope of analysis is explicitly non-exhaustive but focused on recent advances, practical implementability, and the gap between fault-tolerant theoretical speedups and current noisy hardware constraints.

**Algorithms used:** Quantum Accelerated Monte Carlo, Amplitude Amplification, Amplitude Estimation, Maximum Likelihood Amplitude Estimation, Iterative Quantum Amplitude Estimation, Real Quantum Amplitude Estimation, Adaptive Quantum Amplitude Estimation, Faster Amplitude Estimation, QoPrime AE, Random Quantum Amplitude Estimation, Variational Quantum Amplitude Estimation, Quantum Phase Estimation, Quantum Singular Value Transformation, Quantum Fourier Transform, Quantum Signal Processing, SWAP test, qGAN, Split Step Quantum Walk, Quantum Binomial Tree, Low-Rank State Preparation, Bounded Approximation Algorithm, Grover-Rudolph state preparation, Matrix Product State state preparation, Variational Hilbert space evolution, Quantum zero-sum game algorithm, Quantum simplex algorithm, Quantum pseudoinverse algorithms
**Frameworks:** Qiskit, QQuantLib, QLM
## Experiment details
<!-- Step 3 output — experiment replication details -->

## Findings
- [supported] The report concludes that there have been no major breakthroughs in quantum computing for derivatives pricing and VaR since the prior 2022 review; most recent work is incremental and focused on adapting established methods to NISQ constraints.
- [speculative] Quantum Accelerated Monte Carlo (QAMC) is presented as the main research direction for pricing and VaR, with a theoretical quadratic reduction in computational steps relative to classical Monte Carlo.
- [supported] The report emphasizes that many proposed pricing and VaR algorithms require more qubits, lower noise, and deeper circuits than current hardware can support, making practical deployment difficult on present-day devices.
- [supported] For state initialization, no reviewed algorithm satisfies all desirable properties simultaneously (efficiency, robustness to noise, controllable precision, determinism, efficient compilation, phase preservation, and low ancilla use).
- [supported] Under NISQ constraints, approximate or variational state-preparation methods can outperform exact loading methods in practice because shorter circuits reduce noise accumulation.
- [supported] The report identifies noise, rather than qubit count alone, as the dominant practical limitation in many real-hardware experiments for finance-relevant quantum algorithms.
- [supported] The review states that when all error sources in QAMC are considered, a clean quadratic improvement over ideal classical Monte Carlo is not guaranteed by current analyses, though this does not definitively rule out practical speedups because the comparison conditions are asymmetric.
- [supported] Parallel amplitude estimation methods are generally more flexible in controlling circuit depth and are therefore considered more suitable for NISQ devices, while sequential methods tend to offer stronger theoretical guarantees.
- [supported] Simulations and hardware studies reviewed in the report indicate that noise can prevent amplitude-estimation-based methods from realizing their asymptotic quadratic speedup on realistic devices.
- [supported] Brown et al. are summarized as showing that even low-strength noise can destroy the quadratic speedup of exponential-schedule MLAE, and that a linear schedule may outperform other schedules under noise.
- [supported] The report notes that a speedup over classical Monte Carlo for linear-schedule MLAE would require per-CNOT noise around 10^-5, roughly three orders of magnitude better than the best hardware cited in the review.
- [supported] Benchmarking reviewed in the report shows that on IBM hardware, MLAE error stopped improving beyond seven Grover applications for a two-qubit circuit, and for four qubits with three Grover applications MLAE had significantly higher error than classical Monte Carlo.
- [supported] The report summarizes empirical work indicating that generalized-Grover and noise-tailoring approaches can reduce bias and RMSE relative to Monte Carlo in simulations under moderate coherent noise, but these are not presented as end-to-end demonstrations of financial quantum advantage.
- [speculative] Quantum PDE-based pricing methods may offer stronger-than-quadratic, potentially exponential, speedups only in very specific cases, which the report argues limits their attractiveness for practitioners.
- [supported] In the PDE line, the report highlights that extracting a single derivative price from a high-dimensional quantum state can erase the apparent exponential advantage unless reformulated through expectations or other indirect readout strategies.
- [supported] The report recommends moderating expectations for realistic financial applications: near-term value may come more from reduced energy consumption than from speed improvements, while long-term prospects remain uncertain.
- [speculative] The report suggests that even with fault-tolerant quantum computers, error-correction overhead may render the problem sizes needed for practical quadratic speedups in pricing and VaR unrealistically large.
- [speculative] Quantum-inspired financial modeling approaches, including quantum asset markets and Schrödinger-style pricing models, are exploratory and not supported by compelling evidence that market dynamics are fundamentally quantum.

**Results summary:** This technical report provides an updated review of quantum computing methods for derivatives pricing and Value at Risk, with emphasis on NISQ-era feasibility. Its main technical conclusion is that the field has advanced incrementally rather than through major breakthroughs, with most work refining Quantum Accelerated Monte Carlo, amplitude estimation, and state-preparation subroutines. The report reiterates the theoretical appeal of QAMC's quadratic query complexity improvement over classical Monte Carlo, but stresses that practical realization is heavily constrained by state initialization costs, circuit depth, noise, and readout overhead. Across the reviewed literature, noise is identified as the main bottleneck on current hardware, and several cited studies indicate that realistic noise can eliminate the expected quadratic speedup. The report also reviews PDE-based quantum pricing methods and alternative approaches, noting that stronger speedups are theoretically possible only under restrictive assumptions and that output extraction can negate complexity gains. Overall, the report's recommendations are cautious: expectations for near-term financial quantum advantage should be moderated, NISQ work should prioritize noise-aware and depth-limited methods, and any practical benefit in the short term may come more from energy efficiency than raw speed.

**Performance claims:**
- Classical Monte Carlo amplitude estimation sample complexity: N_A^MC >= (1 / (2 * epsilon_a^2)) * log(2 / delta)
- Quantum Phase Estimation-based AE: N_A = O(1 / epsilon_a)
- MLAE-LIS: N_A = O(1 / epsilon_a^(4/3))
- MLAE-EIS: N_A = O(1 / epsilon_a)
- PLAE: N_A = O(1 / epsilon_a^(1+beta)), depth d = O(1 / epsilon_a^(1-beta))
- Improved MLAE: N_A = O((1 / epsilon_a) * (1 / d) * log(1 / delta)), with d = 2^(q-2)
- IQAE: N_A < (50 / epsilon_a) * log((2 / delta) * log2(pi / (4 * epsilon_a)))
- Modified IQAE: N_A < (123 / epsilon_a) * log(6 / delta)
- QCoin: N_A = O((1 / a) * (1 / epsilon_a) * log(1 / delta))
- QoPrime: N_A < C * ceil(k/q) * (1 / epsilon_a^(1+q/k)) * log((4 / delta) * ceil(k/q)), depth d = O(1 / epsilon_a^(1-q/k))
- FasterAE: N_A < (4.1 x 10^3 / epsilon_a) * log((4 / delta) * log2(2pi / (3 * epsilon_a)))
- AdaptiveAE: N_A < (1 / epsilon_a) * log(pi^2(T+1) / (3delta)), T = ceil(log(pi / (K * epsilon_a)) / log K)
- RQAE: N_A < (70pi / (6 * arcsin(epsilon_a) + 1)) * log(3.3 / delta * log2(pi / (2 * arcsin(2 * epsilon_a))))
- For 8 qubits and a normal distribution, the multicontrolled Grover-Rudolph method used less than 13% of the gates of the original Grover-Rudolph algorithm while achieving fidelity 0.99961
- A reinforcement-learning state-preparation experiment on 2 qubits achieved a minimum of 15 gates with only modest fidelity
- Genetic-algorithm state preparation for 5 qubits reported maximum fidelities below 0.8 while reducing CNOT count
- Split Step Quantum Walk state loading for a European call option produced a reasonable result with 5 qubits in less than 20 seconds
- MPS-based loading was reported to give valid results only up to 20 qubits with one MPS layer
- Linear-schedule MLAE would require per-CNOT noise of about 10^-5 to outperform classical Monte Carlo, around three orders of magnitude better than the best hardware cited
- On IBM hardware, MLAE error did not improve beyond 7 Grover applications for a 2-qubit circuit
- On IBM hardware, increasing to 4 qubits and 3 Grover applications led MLAE to show significantly higher error than classical Monte Carlo
- Nakaji's Faster Amplitude Estimation is reported as reducing oracle calls by a factor of about 100 relative to original IQAE
- AdaptiveQAE is reported as approximately 40 times faster on average than IQAE and MLAE, although with slightly higher oracle-call counts
- Quantum deep hedging experiments used trapped-ion hardware with circuits up to 16 qubits
- The PDE-based multi-asset derivative method is summarized as having complexity poly(epsilon^-1, d) instead of (epsilon^-1)^(O(d))
## Quantum advantage claim
**Classification:** theoretical

The report reviews theoretical complexity advantages such as QAMC's quadratic query improvement and possible stronger speedups for some PDE methods, but it does not present a demonstrated end-to-end quantum advantage for realistic financial services workloads. It repeatedly stresses that noise, initialization overhead, readout costs, and error-correction overhead currently prevent practical realization.
## Limitations
- The review is explicitly not exhaustive and only covers publications released between the previous report (D5.3 / 2022) and the current one.
- The report focuses primarily on quantum algorithms for accelerating Monte Carlo methods, so other pricing and risk approaches receive less comprehensive treatment.
- Many proposed techniques require far more quantum computational resources than are currently available, including more qubits, greater circuit depth, and lower noise levels.
- The deliverable pays special focus to NISQ computers, which constrains the scope relative to fault-tolerant quantum computing approaches.
- For PDE-based quantum methods, the report notes that exponential speedups can only be attained in very specific cases, reducing practical attractiveness.
- There are no new major breakthroughs since the previous review; most recent work is described as incremental rather than transformative.
- The gap between theory and practice remains large because many theoretical results assume fault-tolerant quantum computers while only NISQ hardware is currently available.
- Noise is identified as the main limiting factor in many real-hardware experiments, more important than qubit count or circuit depth in several cases.
- Even with future error-corrected quantum computers, the report argues that error-correcting overhead may make quadratic speedups ineffective except for impractically large instances.
- No initialization algorithms reviewed fulfill all desired requirements simultaneously (efficiency, robustness to noise, controllable precision, determinism, efficient circuit construction, phase preservation, and low ancilla use).
- Many initialization methods require either too many auxiliary qubits or excessive circuit depth, making them impractical on current processors.
- Some variational initialization methods may introduce arbitrary relative phases in amplitudes, which are difficult to detect at scale because state tomography becomes computationally prohibitive.
- Variational algorithms require difficult training and can get stuck in local minima or barren plateaus.
- For QAMC, one cited error analysis concludes that after accounting for discretization and other errors, a quadratic improvement over ideal classical Monte Carlo cannot be guaranteed under the analyzed assumptions.
- In MLAE-like amplitude estimation, quadratic speedup is reported as not achievable under even low-strength noise for some schedules, and practical advantage may require per-CNOT noise around 10^-5, far beyond current hardware.
- Amplitude estimation performance can saturate beyond a maximum number of oracle calls under noisy conditions, so additional circuit depth may not improve precision.
- MLAE-like methods can suffer from critical points or exceptional amplitude values that induce biased estimators even in noiseless settings.
- Benchmarking results cited in the report show that for larger qubit counts or deeper circuits, MLAE can perform worse than classical Monte Carlo.
- Some proposed methods for state preparation or function loading were only demonstrated on very small systems (e.g., 2 to 6 qubits), limiting evidence of scalability.
- MPS-based loading methods are reported to give valid results only up to about 20 qubits with one MPS layer, even though more layers are needed for good approximation.
- Some experimental papers reviewed provide only qualitative agreement rather than rigorous quantitative metrics for comparing theoretical and experimental distributions.
- Quantum-inspired financial modeling approaches lack compelling justification that market dynamics should follow quantum-mechanical evolution.
- Some quantum finance models discussed violate standard financial properties such as put-call parity or require assumptions that remain unvalidated against market data.
- The deep hedging quantum reinforcement learning approach reviewed is limited by qubit requirements, needing roughly one qubit per time step in the simplest setup.
- The quantum deep hedging implementation reviewed uses only a rough approximation of Black-Scholes dynamics via geometric Brownian motion.
- The martingale asset pricing approach for incomplete markets assumes quantum access to asset prices and payoff matrices, a strong practical assumption.
- [inferred] As a technical report produced under the NEASQC project, the document is partly shaped by project scope and deliverable objectives, which may limit breadth compared with an independent systematic review.
- [inferred] Because the report is dated July 2023 while the contractual deadline is September 2024, the literature coverage is not current to the full project horizon and omits later developments.
- [inferred] The report does not describe a formal systematic-search protocol, inclusion/exclusion criteria, or reproducible screening methodology, limiting reproducibility of the review process.
- [inferred] The report synthesizes prior studies but does not provide a meta-analytic or standardized benchmarking framework across algorithms, hardware platforms, and financial tasks.
## Open questions
- Can quantum algorithms for pricing and VaR deliver practical advantage on NISQ hardware despite current noise levels?
- Will the promised quadratic speedups of QAMC survive once all relevant implementation errors and error-correction overheads are included?
- What noise levels are admissible before an actual quantum speedup becomes achievable in practice?
- Which amplitude estimation variants are most robust to realistic hardware noise and depth constraints?
- How can probability distributions and payoff functions be loaded efficiently while preserving relative phases, limiting ancilla use, and remaining robust to noise?
- Can variational state-preparation methods scale to larger qubit counts without barren plateaus, local minima, or undetected phase errors?
- How should one optimally trade off approximation precision against circuit depth and noise on NISQ devices?
- Are there practical financial problem instances large enough for quantum advantage once fault-tolerant overhead is considered?
- Can PDE-based quantum methods be generalized beyond the very specific cases where exponential speedups are claimed?
- How can one efficiently extract useful pricing information from quantum PDE solvers without losing advantage due to readout of exponentially small amplitudes?
- Do generalized Grover and engineered-likelihood approaches consistently outperform conventional amplitude estimation under realistic coherent and incoherent noise?
- How can critical-point pathologies in MLAE-like algorithms be systematically avoided rather than heuristically mitigated?
- Can quantum reinforcement learning for hedging maintain advantages when moving beyond simplified GBM dynamics and small qubit counts?
- Do quantum-inspired financial models calibrate to market data better than classical models, and if so under what conditions?
- Is there any compelling empirical basis for modeling market dynamics with quantum-mechanical evolution rather than using quantum computers only as accelerators of classical models?
- How should industry evaluate quantum value in finance if near-term benefits come more from energy efficiency than speed?

**Future work:**
- Continue closing the gap between theoretically established quantum finance algorithms and practical implementations on NISQ hardware.
- Develop algorithms better suited for NISQ devices, especially with lower depth and greater noise robustness.
- Investigate the role of noise more deeply, both for current hardware and for future fault-tolerant systems.
- Design improved initialization/state-preparation methods that jointly satisfy efficiency, controllable precision, phase correctness, low ancilla use, and robustness to noise.
- Explore approximate state-preparation approaches that intentionally relax precision to reduce circuit depth and improve overall performance under noise.
- Develop amplitude estimation methods that explicitly model, mitigate, or tailor noise rather than assuming idealized execution.
- Create AE schedules and estimators that control maximum circuit depth while retaining as much quantum advantage as possible.
- Address exceptional-value and critical-point failures in MLAE-like algorithms through improved algorithm design.
- Further study generalized Grover reflections, engineered likelihood functions, and quantum signal processing approaches for more robust amplitude estimation.
- Extend quantum pricing methods to more complex and path-dependent products such as Asian, Bermudan, and American options.
- Improve methods for loading correlated asset distributions and multidimensional probability distributions relevant to realistic financial models.
- Develop practical quantum PDE solvers that avoid the readout bottleneck associated with exponentially small amplitudes.
- Test and calibrate quantum-inspired financial models against real market data to assess whether they outperform classical models.
- Extend quantum deep hedging beyond rough Black-Scholes/GBM approximations and beyond small-qubit demonstrations.
- Investigate whether near-term quantum contributions in finance may come from reduced energy consumption rather than speed improvements.
- [inferred] Establish standardized, reproducible benchmarking across algorithms, hardware platforms, and financial use cases to compare practical utility.
- [inferred] Update the review with post-2023 literature and a more systematic search methodology to maintain currency and reproducibility.
## Key ideas
- #idea:quantum-advantage — The report reviews QAMC and amplitude-estimation methods as the main theoretical route to quadratic Monte Carlo speedups for derivatives pricing and VaR.
- #idea:near-term-feasibility — The review concludes that post-2022 progress is mostly incremental and that no end-to-end practical quantum advantage has been demonstrated for realistic pricing or VaR workloads.
- #idea:near-term-feasibility — Noise is identified as the dominant bottleneck on current hardware, often eliminating the expected AE speedup and causing performance saturation or worse-than-classical results.
- #idea:hybrid-approach — Approximate and variational state-preparation methods are presented as pragmatic NISQ options because reduced circuit depth can outperform exact loading under noise.
- #idea:near-term-feasibility — No existing state-preparation method simultaneously satisfies efficiency, robustness, controllable precision, low ancilla use, phase preservation, and easy compilation.
- #idea:quantum-advantage — PDE-based quantum pricing methods may offer stronger asymptotic gains in highly structured settings, but these are narrow and practically fragile.
- #idea:near-term-feasibility — Readout and data-loading overheads can erase theoretical complexity gains, especially for PDE solvers and QAMC pipelines.
- #idea:hybrid-approach — The report recommends noise-aware, depth-limited, hybrid classical-quantum workflows as the most realistic near-term path.
- #idea:near-term-feasibility — Even fault-tolerant quantum computing may require impractically large instances once error-correction overhead is included.
- #idea:near-term-feasibility — The report suggests that any near-term financial value may come more from energy efficiency than runtime speedup.
## Contradictions
- The report contrasts with common quantum-finance claims of clear quadratic Monte Carlo advantage by concluding that real-hardware amplitude-estimation pipelines for pricing and VaR often fail to outperform, and can underperform, classical Monte Carlo.
- It contradicts optimistic scalability narratives by arguing that once state preparation, readout, noise, and error-correction overhead are included, asymptotic advantages for QAMC and PDE-based pricing may not translate to practical financial workloads.
- Relative to the earlier survey referenced as 2022_Gomez_D53, this update emphasizes that there have been no major breakthroughs since 2022 and that recent work mainly adapts prior methods to NISQ constraints rather than validating quantum superiority.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
