---
aliases:
- Quantum Algorithm for Local-Volatility Option Pricing via the Kolmogorov Equation
- Quantum Algorithm Local Volatility
authors:
- Nikita Guseynov
- Mikel Sanz
- Ángel Rodríguez-Rozas
- Nana Liu
- Javier Gonzalez-Conde
auto_detected: true
classification: ''
contradiction_flags:
- contradiction:scalability
doi: ''
evidence_type: ''
idea_tags:
- idea:quantum-advantage
- idea:near-term-feasibility
journal_or_venue: arXiv
methodology_tags:
- quantum-simulation
paper_type: ''
quantum_advantage_claim: speculative
related_papers: []
relevance_phase1: high
relevance_phase3: high
source_type: preprint
source_type_confidence: high
step1_date: '2026-03-25T16:09:17.882172'
step1_model: gpt-5.1
step2_date: '2026-03-25T16:09:24.655091'
step2_model: gpt-5.1
step3_date: '2026-03-25T16:09:48.649965'
step3_model: gpt-5.4
step4_date: '2026-03-25T16:10:21.665550'
step4_model: gpt-5.4
step5_date: '2026-03-25T16:10:57.708552'
step5_model: gpt-5.4
step6_date: '2026-03-25T16:11:08.336892'
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
- method/quantum-simulation
- idea/quantum-advantage
- idea/near-term-feasibility
- contradiction/scalability
title: Quantum Algorithm for Local-Volatility Option Pricing via the Kolmogorov Equation
topic_tags:
- derivatives-pricing
year: 2025
zotero_key: ''
---

## Abstract summary
The paper proposes an end-to-end quantum algorithmic framework for pricing European options under local-volatility models by solving the Kolmogorov forward (Fokker–Planck) partial differential equation. Using the Schrödingerisation technique, the forward PDE is mapped to a Hamiltonian simulation problem, with explicit prescriptions for state preparation, time evolution, and option-price extraction via a swap test. The authors argue that this forward formulation enables more efficient recovery of prices, yields a polynomial advantage in grid size for single-asset problems, and offers exponential scaling benefits in high-dimensional settings such as basket options compared to classical methods.
## Methodology
This paper is a preprint and is primarily theoretical with an algorithmic resource-analysis component rather than an empirical benchmark study. It proposes an end-to-end quantum input-processing-output framework for pricing European vanilla options under a local-volatility model by solving the Kolmogorov forward (Fokker-Planck) PDE instead of the backward pricing PDE. The core methodology maps the non-unitary forward PDE to a Hamiltonian-simulation problem using the Schrödingerisation technique, then removes explicit time dependence by introducing an additional clock dimension so the dynamics can be represented by a time-independent enlarged Hamiltonian. The option-price distribution is amplitude-encoded on a discretized spatial grid, with local volatility assumed to admit a polynomial approximation and, for implementability, a low-rank separable representation in space and time. The paper specifies how to prepare the initial state for the price register, the Schrödingerisation auxiliary register, and the clock register; discretizes position and momentum operators using finite-difference schemes with periodic boundary conditions; derives sparse/block-encoded Hamiltonian simulation costs; and recovers the final option price by preparing a payoff state and estimating overlaps via a swap test. The work emphasizes complexity-theoretic analysis, including query and gate complexity, comparison with classical finite-difference and matrix-exponential methods, and extension to multi-asset settings where the authors argue polynomial scaling in dimension for their framework and potential mitigation of the classical curse of dimensionality. No actual hardware experiments or numerical benchmark runs are described in the provided text.

**Algorithms used:** Hamiltonian simulation, Schrödingerisation, Swap test, Quantum Fourier Transform, Inverse Quantum Fourier Transform, Block-encoding, LCU
## Experiment details
<!-- Step 3 output — experiment replication details -->

## Findings
- [speculative] The paper proposes an end-to-end quantum algorithmic framework for pricing European vanilla options under a local-volatility model by solving the Kolmogorov forward (Fokker-Planck) PDE via Schrödingerisation and Hamiltonian simulation.
- [speculative] The authors argue that solving the forward PDE is advantageous over the backward PDE in a quantum setting because the option price can be recovered efficiently through an expected-value computation implemented with a swap test.
- [speculative] The framework specifies the full input-processing-output pipeline: classical data encoding into quantum states, Hamiltonian simulation of the forward PDE, and classical option-price extraction.
- [speculative] For a single option-pricing instance, the authors claim a polynomial quantum advantage in grid size or number of qubits relative to classical PDE solvers.
- [speculative] The paper claims the main potential benefit appears in high-dimensional basket-option pricing, where the method is argued to offer exponential speedup in dimension and mitigate the classical curse of dimensionality.
- [supported] In the Black-Scholes analysis presented in the paper, the overlap between normalized backward-PDE solution states and their initial states remains very high (reported as exceeding 0.99), whereas the forward-PDE overlap decays rapidly with maturity, motivating the forward formulation for quantum implementation.
- [speculative] The local-volatility surface is assumed to be representable or approximable by a low-rank separable form so that current 1D oracle and LCU techniques can implement the volatility dependence without multivariate QSVT.
- [speculative] The Schrödingerisation-based simulation of the non-unitary PDE dynamics is claimed to have near-optimal or optimal dependence on simulation precision, depending on the smooth cutoff used for the auxiliary register.
- [speculative] The dominant limitation on speedup is identified as the discretized momentum-squared term, whose norm scales as 2^(2n), restricting the grid-size speedup to polynomial unless further effective low-energy refinements are used.
- [speculative] The authors claim that in multi-asset settings the gate complexity of one time-evolution step scales polynomially with dimension, specifically as O(d^5), while payoff-state preparation can scale linearly in d for factorized or short-LCU payoff structures.
- [speculative] The paper concludes that quantum computing could become transformative for computational finance, especially for high-dimensional derivatives and potentially for more complex products such as basket, American, and Asian options.

**Results summary:** This preprint presents a theoretical quantum algorithm for local-volatility option pricing based on solving the Kolmogorov forward PDE rather than the backward pricing PDE. The method maps the non-unitary forward PDE to a Hamiltonian-simulation problem using Schrödingerisation, adds a clock register to handle time dependence, and uses amplitude encoding plus a swap test to recover option prices. The paper includes analytical and complexity arguments, along with illustrative Black-Scholes overlap analysis showing that forward-state evolution is more distinguishable from the initial state than backward evolution in their encoding. The main claims are complexity-theoretic: polynomial improvement in grid size for single-instance pricing and potential exponential improvement with respect to dimension for high-dimensional basket options. However, these quantum-advantage claims are theoretical and not empirically demonstrated on real hardware; the paper does not report benchmark experiments against classical solvers beyond asymptotic complexity comparisons.

**Performance claims:**
- Backward-PDE solution-state fidelity with the initial state exceeds 0.99 in the Black-Scholes analysis, while forward-state overlap decays rapidly with maturity.
- Schrödingerisation retrieval success probability: P_succ ≈ L_+(ψ) ||p(T)||^2 / ||p(0)||^2.
- Schrödingerisation query complexity: O(log(1/epsilon_Schr) * ||p(0)||^2 / ||p(T)||^2), improvable to O(log(1/epsilon_Schr) * ||p(0)|| / ||p(T)||) with amplitude amplification.
- Initial state preparation for Gaussian approximation has circuit complexity O(n log n * (log(1/epsilon_prep)+log(1/omega)) / log(1+2 omega log(1/epsilon_prep))).
- Sparse-Hamiltonian simulation query complexity: O((gamma + log(gamma/epsilon_evol)) / log log(gamma/epsilon_evol)), where gamma = s ||H||_max t.
- For the chosen discretization, Hamiltonian sparsity is stated as s = 5.
- Hamiltonian norm scaling is claimed as ||H||_max ~ sigma_max^2 max(|a|,|b|)^2 2^(2n).
- Block-encoding gate complexity is given as O(((s ||H||_max T + log(1/epsilon_evol)) / log(e + log(1/epsilon_evol)/(s ||H||_max T))) * (D_s n log n + s n + n_w log n_w + D_t n_y log n_y)).
- Quantum gate complexity is summarized as O(N^2 log N log log N) versus classical O(N^3) for the discretized PDE problem, with N = 2^n.
- Multidimensional time-evolution cost is claimed to scale as O(d^5) in the number of assets d.
- Initial-condition preparation in d dimensions is claimed to scale as O(d n).
- Swap-test overlap estimation requires O(1/epsilon_st^2 * log(1/delta)) copies.
- Swap-test circuit cost is stated as 7n CNOT operations.
- Payoff-state construction complexity is stated as 6n^2 - 4n + 6 CNOTs and n - 1 ancillas.
- Information-retrieval relative error is stated to scale as O(1/sqrt(N_shots)) + O(Delta x).
## Quantum advantage claim
**Classification:** speculative

The paper makes theoretical claims of polynomial advantage in grid size and exponential speedup in dimension, but these are asymptotic and based on algorithmic complexity analysis rather than strong empirical validation or real-hardware demonstration. As a preprint, the quantum advantage claims should be treated as speculative.
## Limitations
- The paper is a preprint and has not undergone peer review.
- The claimed quantum advantage for a single option-pricing instance is only polynomial, and the authors explicitly note that this holds 'without further refinement in studying effective regimes'.
- The implementation cannot realize a generic fully bivariate local-volatility function σ(s,t) directly; instead it requires a small-rank separable approximation σ_lr(s,t), which is an additional modeling assumption.
- The approach assumes the local volatility can be approximated by polynomial or low-rank separable basis expansions, which may not capture all realistic market volatility surfaces accurately.
- The framework assumes deterministic interest rates ('sometimes assumed to be deterministic, as we do in this manuscript'), limiting realism for settings with stochastic rates.
- The method is developed only for European vanilla options in the main treatment, so applicability to more complex derivatives is not demonstrated.
- The algorithm relies on discretization of the PDE on a finite grid and periodic boundary conditions, justified by choosing a sufficiently wide domain; this may introduce approximation error or boundary artifacts if tails are not negligible.
- The initial Dirac-delta condition is not directly implementable and must be approximated numerically/quantumly by a computational basis state or sharply peaked Gaussian.
- The Schrödingerisation-based simulation requires post-selection, with success probability proportional to ||p(T)||^2 / ||p(0)||^2, which can create overhead.
- The Hamiltonian norm is dominated by the discretized momentum-squared term, scaling like 2^(2n), which the authors identify as the most restrictive factor limiting quantum advantage.
- The multidimensional scaling is only polynomial in dimension for the full simulation cost; despite claims of mitigating the curse of dimensionality, the detailed theorem gives O(d^5) dependence for time evolution.
- The final information retrieval via swap tests has sampling complexity O(1/ε_V0^2), so output extraction can be costly.
- The paper does not report experiments on real quantum hardware; the work is algorithmic/resource-theoretic rather than empirically validated on NISQ devices.
- [inferred] No hardware noise, decoherence, gate error, or noise-mitigation analysis is provided, so practical performance on current quantum devices is unknown.
- [inferred] No end-to-end benchmark against state-of-the-art classical solvers on realistic financial datasets is presented, making practical advantage claims unverified.
- [inferred] The resource estimates appear asymptotic and may hide large constants from state preparation, block encoding, ancilla registers, and post-selection overheads.
- [inferred] The use of amplitude encoding assumes efficient loading of classical financial inputs into quantum states; in practice, data-loading costs may reduce or erase the claimed advantage.
- [inferred] The claim of exponential speedup for baskets/high dimensions depends on assumptions about payoff/state preparation and oracle access that may be difficult to satisfy in realistic production settings.
- [inferred] The manuscript focuses on computational complexity but does not address calibration error, market data noise, or robustness of the local-volatility surface construction from observed option prices.
- [inferred] Reproducibility may be limited because the excerpt does not indicate released code, circuit implementations, or numerical benchmark scripts.
## Open questions
- Under what effective regimes can the single-instance Schrödingerisation methodology yield stronger-than-polynomial practical advantage?
- How should the parameters N_τ and N_θ in related variational forward-PDE methods scale with model characteristics such as local volatility, payoff discontinuities, and stiffness?
- How accurate is the low-rank separable approximation of σ(s,t) for realistic market-implied local-volatility surfaces, and what rank R is needed in practice?
- Can the dominant Hamiltonian-norm bottleneck from the momentum-squared term be reduced enough to improve scaling beyond the current polynomial-in-grid-size advantage?
- How does the algorithm perform for high-dimensional basket options when all state-preparation, payoff-encoding, and readout costs are included?
- What is the practical crossover point at which the quantum method outperforms classical PDE or Monte Carlo solvers?
- How robust is the method to discretization choices, domain truncation, and boundary-condition approximations?
- Can the post-selection overhead in Schrödingerisation be reduced or avoided in a practically meaningful way?
- How well does the framework generalize from European vanilla options to path-dependent, early-exercise, or exotic derivatives?
- What are the effects of realistic hardware noise and finite-depth constraints on the proposed Hamiltonian simulation and swap-test readout?
- How sensitive are the results to errors in constructing the local-volatility surface from market option prices?
- Does the claimed mitigation of the curse of dimensionality persist after accounting for all oracle, encoding, and measurement costs in realistic implementations?

**Future work:**
- Extend the framework to stochastic volatility dynamics.
- Extend the methodology to more general payoffs.
- Apply the framework to risk-management applications.
- Study more complex financial derivatives such as American options.
- Study more complex financial derivatives such as Asian options.
- Refine the analysis to identify effective energy regimes that could improve the speedup beyond the current baseline.
- Investigate alternative representations, such as second-quantized descriptions of position and momentum operators, to alleviate the Hamiltonian-norm bottleneck.
- Explore high-dimensional basket-option pricing further, motivated by the better scaling with dimension.
- [inferred] Validate the algorithm with numerical benchmarks against strong classical baselines on realistic market data.
- [inferred] Implement and test the method on fault-tolerant resource estimates and, where possible, on near-term hardware with noise analysis.
- [inferred] Develop more efficient state-preparation and payoff-encoding methods to make the end-to-end advantage more realistic.
- [inferred] Analyze robustness to calibration uncertainty and noisy implied-volatility surfaces derived from market data.
## Key ideas
- #idea:quantum-advantage — Proposes an end-to-end quantum framework for European option pricing under local volatility by mapping the Kolmogorov forward PDE to Hamiltonian simulation via Schrödingerisation.
- #idea:quantum-advantage — Claims polynomial improvement in grid size for single-asset pricing relative to classical PDE solvers through sparse/block-encoded Hamiltonian simulation.
- #idea:quantum-advantage — Argues that the forward-PDE formulation is more quantum-friendly than the backward PDE because option values can be extracted efficiently as overlaps with payoff states using a swap test.
- #idea:quantum-advantage — Claims potential exponential benefit in high-dimensional basket-option settings by mitigating the classical curse of dimensionality under separable/low-rank assumptions.
- #idea:near-term-feasibility — Presents a full input-processing-output quantum pipeline, but only as a theoretical resource-analysis framework with no hardware or numerical benchmark validation.
- #idea:near-term-feasibility — The required Hamiltonian simulation, ancilla/clock registers, post-selection, and swap-test readout imply fault-tolerant rather than NISQ-era applicability.
## Contradictions
- The paper claims strong scaling benefits, including polynomial speedup in grid size and possible exponential improvement in dimension, but also states that the dominant momentum-squared term causes the Hamiltonian norm to scale as 2^(2n), which materially weakens practical scalability and limits the single-instance advantage to polynomial at best.
- The paper argues mitigation of the curse of dimensionality for basket options, yet its own detailed multidimensional evolution cost scales as O(d^5) and depends on favorable assumptions about low-rank separable volatility and efficient payoff/state preparation, creating tension with broader claims of high-dimensional advantage.
- The paper presents an end-to-end pricing algorithm, but the absence of empirical benchmarks, hardware runs, and realistic data-loading/readout cost validation contradicts any strong interpretation of demonstrated quantum superiority.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
