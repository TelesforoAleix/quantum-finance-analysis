---
aliases:
- End-to-end resource analysis for quantum interior point methods and portfolio optimization
- End end resource analysis
authors:
- Alexander M. Dalzell
- B. David Clader
- Grant Salton
- Mario Berta
- Cedric Yen-Yu Lin
- David A. Bader
- Nikitas Stamatopoulos
- Martin J. A. Schuetz
- Fernando G.S.L. Brand˜ ao
- Helmut G. Katzgraber
- William J. Zeng
auto_detected: true
classification: ''
contradiction_flags:
- contradiction:classical-vs-quantum
- contradiction:scalability
doi: ''
evidence_type: ''
idea_tags:
- idea:quantum-advantage
journal_or_venue: arXiv
methodology_tags:
- HHL
- classical-simulation
paper_type: ''
quantum_advantage_claim: speculative
related_papers: []
relevance_phase1: high
relevance_phase3: high
source_type: preprint
source_type_confidence: high
step1_date: '2026-03-25T15:56:20.781619'
step1_model: gpt-5.1
step2_date: '2026-03-25T15:56:29.682957'
step2_model: gpt-5.1
step3_date: '2026-03-25T15:57:30.002267'
step3_model: gpt-5.4
step4_date: '2026-03-25T15:58:11.682139'
step4_model: gpt-5.4
step5_date: '2026-03-25T15:58:47.898898'
step5_model: gpt-5.4
step6_date: '2026-03-25T15:58:58.566093'
step6_model: gpt-5.4
steps_completed:
- 1
- 2
- 3
- 4
- 5
- 6
tags:
- topic/portfolio-optimisation
- method/HHL
- method/classical-simulation
- idea/quantum-advantage
- contradiction/classical-vs-quantum
- contradiction/scalability
title: End-to-end resource analysis for quantum interior point methods and portfolio
  optimization
topic_tags:
- portfolio-optimisation
year: 2024
zotero_key: ''
---

## Abstract summary
The paper presents a detailed, circuit-level resource analysis of quantum interior point methods for second-order cone programs, focusing on portfolio optimization as a key financial use case. The authors integrate state-of-the-art quantum linear system solvers, QRAM-based block-encodings, and quantum state tomography into a full end-to-end algorithm, and then numerically estimate instance-dependent parameters such as condition numbers and required tomographic precision using historical stock data. Their estimates show that, even for modest portfolio sizes, the logical qubit counts and T-gate resources are astronomically large, leading them to conclude that substantial conceptual and algorithmic improvements are needed before such quantum methods can yield practical advantage over classical interior point methods.
## Methodology
This preprint presents an end-to-end resource analysis of a quantum interior point method (QIPM) for second-order cone programming (SOCP), using portfolio optimization as the main financial use case. The work is primarily theoretical with supporting numerical simulation. The authors formulate a Markowitz-style portfolio optimization problem with budget, non-negativity, and transaction constraints as an SOCP, then analyze a fault-tolerant quantum implementation of the corresponding QIPM at the quantum-circuit level. The methodology combines: (1) formal derivation of the SOCP and self-dual embedding; (2) specification of the Newton linear systems solved at each interior-point iteration; (3) use of a quantum linear systems solver (QLSS) based on the discrete adiabatic theorem, together with block-encoding via QRAM and pure-state quantum tomography to recover classical solutions; (4) explicit logical resource estimation in terms of logical qubits, T-count, and T-depth, including constant factors; and (5) numerical simulations of small portfolio instances built from historical stock data to empirically estimate instance-dependent parameters such as the Frobenius condition number and required tomography precision. The simulations do not run on quantum hardware; instead, the quantum linear solve is emulated classically by solving the Newton system exactly and injecting multinomial tomography noise. The study compares several QIPM variants (inexact-infeasible and inexact-feasible forms), includes simple row-normalization preconditioning, and uses adaptive tomography precision to test whether iterates remain in the neighborhood of the central path. The main outputs are asymptotic and concrete resource estimates, scaling fits for condition number and tomography precision versus portfolio size, and qualitative identification of bottlenecks preventing practical quantum advantage.

**Algorithms used:** Quantum Interior Point Method (QIPM), Quantum Linear Systems Solver (QLSS), Discrete adiabatic theorem-based QLSS, Quantum state tomography, Block-encoding, Quantum Signal Processing (QSP), Quantum Singular Value Transformation (QSVT), Classical Interior Point Method (CIPM), Randomized Kaczmarz, Gaussian elimination, QR decomposition, Cholesky decomposition, Preconditioning

**Experimental setup:** No real quantum hardware was used. The paper performs circuit-level fault-tolerant resource estimation and classical numerical simulation of the QIPM. Quantum subroutines are modeled analytically using explicit logical circuits for block-encoding, state preparation, QLSS, and tomography. For numerical experiments, the authors simulate the full QIPM classically on small portfolio instances, replacing the quantum linear solve with an exact classical linear-system solve and adding multinomial sampling noise to emulate tomography. They study portfolios up to n = 120 assets and report logical qubit, T-count, and T-depth estimates for a representative n = 100 case.

**Dataset:** Historical stock data from the Dow Jones U.S. Total Stock Market Index (DWCF) were used to generate random portfolio optimization instances. Stocks were randomly sampled from the index, and historical returns over selected time epochs were used to construct the mean return vector and covariance-related matrix for the SOCP formulation.
## Experiment details
### Input
Financial input consists of randomly sampled stock portfolios from the Dow Jones U.S. Total Stock Market Index (DWCF). Portfolio sizes studied include n in the range 10 to 120, with detailed plots for n = 60, 80, 100, and 120 and an example instance at n = 30. For each instance, m = 2n time epochs (days) of returns were used to construct the average return vector u-hat and an m x n matrix M such that M^T M = Sigma. In the example simulation, n = 30 stocks and m = 60 days were used. Additional problem parameters were set as q = 1, zeta = 0.05 * 1, and the initial portfolio w-bar was chosen proportional to market capitalization. The SOCP formulation included budget, non-negativity, and maximum transaction constraints. Across scaling experiments, 128 random portfolio samples were generated for each portfolio size.

### Process
The experimental process has two layers. First, the portfolio optimization problem is reformulated as an SOCP and embedded into a self-dual form suitable for an interior point method. At each IPM iteration, the Newton system is formed from the current primal-dual iterate. The authors study three variants: II-QIPM (inexact-infeasible), IF-QIPM, and IF-QIPM-QR, though the main text focuses on II-QIPM. A simple preconditioner is applied by normalizing each row of the Newton matrix. The quantum subroutine is specified as: construct block-encodings of the Newton matrix and state-preparation for the right-hand side, run a discrete-adiabatic QLSS with QSP/QSVT-based eigenstate filtering, then perform pure-state tomography to recover a classical approximation to the normalized solution vector. In numerical simulation, instead of executing the quantum circuit, the Newton system is solved exactly classically and tomography is emulated by drawing samples from the corresponding multinomial distribution; sign estimation in tomography is assumed correct for simplicity. Tomography precision is chosen adaptively: start from xi = 1/2 and repeatedly halve it until the updated iterate remains within the neighborhood of the central path. The IPM uses sigma = 1 - 1/(20*sqrt(2)*sqrt(r)) and gamma = 1/10, and iterates until the duality gap reaches the target epsilon. For resource estimation, the authors use the maximum observed Frobenius condition number and minimum observed tomography precision across iterations, and instantiate detailed logical resource formulas. They also fit power-law models to empirical scaling of condition number, inverse tomography precision squared, and the combined runtime factor n^1.5 * kappa_F / xi^2.

### Output
Outputs include: empirical trajectories of duality gap, infeasibility, distance to the central path, and required tomography precision over IPM iterations; distributions and median trends of the Frobenius condition number kappa_F and inverse tomography precision squared versus portfolio size and duality gap; fitted power-law exponents for these quantities; and end-to-end logical resource estimates in terms of number of logical qubits, T-depth, and T-count. The paper also compares QIPM scaling conceptually against classical approaches such as Gaussian elimination-based IPMs and randomized Kaczmarz-based iterative solvers. A representative concrete estimate is given for n = 100 and epsilon = 10^-7, yielding approximately 8 x 10^6 logical qubits, 2 x 10^24 T-depth, and 7 x 10^29 T-count.

### Parameters
- portfolio_sizes_n: [10, 30, 60, 80, 100, 120]
- time_epochs_m_relation: m = 2n
- random_instances_per_size: 128
- risk_aversion_q: 1
- transaction_limit_zeta: 0.05 * 1 vector
- initial_portfolio_w_bar: proportional to market capitalization
- ipm_sigma: 1 - 1/(20*sqrt(2)*sqrt(r))
- central_path_gamma: 0.1
- target_duality_gap_example: 1e-07
- duality_gaps_analyzed_for_scaling: [0.1, 0.001, 1e-05, 1e-07]
- tomography_failure_probability_delta: 0.1
- adaptive_tomography_initial_xi: 0.5
- tomography_update_rule: halve xi until iterate remains in neighborhood
- qlss_success_probability: at least 1/2 after eigenstate filtering
- resource_focus: ['logical qubits', 'T-depth', 'T-count']
- representative_resource_estimate_n: 100
- representative_kappa_F_at_n_100: 1.6 x 10^4
- representative_observed_tomography_samples_k: 3.3 x 10^8
- estimated_iterations_at_n_100: about 8 x 10^3

### Hardware
{'hardware_type': 'No physical QPU; fault-tolerant logical circuit model and classical simulation', 'quantum_execution': 'Analytical resource estimation only', 'simulated_quantum_components': ['block-encoding via QRAM-style circuits', 'state preparation', 'discrete adiabatic QLSS', 'QSP/QSVT eigenstate filtering', 'pure-state tomography'], 'fault_tolerance_basis': 'Clifford+T logical gate model with emphasis on T-count and T-depth', 'qram_assumption': 'Large QRAM assumed as part of block-encoding construction; costs included in logical resource analysis'}

### Reproducibility
Preprint. The paper provides extensive mathematical detail, pseudocode, circuit constructions, parameter definitions, and dataset provenance (DWCF historical stock data), which supports partial replication of the analysis. However, no code repository is mentioned in the provided text, and some implementation details for data extraction and simulation may require reconstruction. Reproducibility is moderate for the theoretical/resource-analysis components and moderate-to-limited for the full numerical pipeline without accompanying code.
## Findings
- [supported] The paper provides an end-to-end logical resource analysis of a quantum interior point method (QIPM) for second-order cone programming applied to portfolio optimization, including explicit circuit-level estimates for logical qubits, T-count, and T-depth.
- [supported] For a portfolio optimization instance with n = 100 assets and target precision ϵ = 10^-7, the authors estimate about 8 × 10^6 logical qubits, 7 × 10^29 total T gates, and 2 × 10^24 T-depth layers.
- [supported] The authors conclude that the analyzed QIPM is far from practical and would require fundamental improvements before yielding practical quantum advantage, citing large constant prefactors, poorly conditioned linear systems, and costly quantum state tomography.
- [supported] Numerical simulations on portfolio instances up to n = 120 suggest that both the Frobenius condition number κ_F and the inverse tomography precision ξ^-1 tend to grow with problem size n.
- [supported] The numerical experiments were performed by classical simulation of the algorithm and tomography noise, not on real quantum hardware.
- [supported] A simple row-normalization preconditioning scheme reduced the effective condition number by more than an order of magnitude for the portfolio optimization instances studied.
- [supported] The authors observed that the infeasible QIPM variant empirically performed similarly to feasible variants, despite lacking the same theoretical convergence guarantees.
- [supported] Contrary to worst-case theoretical expectations, the simulations did not show κ_F or ξ^-1 diverging as the optimization tolerance approached zero in the tested instances.
- [supported] The tomography method analyzed requires, to leading order, at most 115 L ln(L) / ξ^2 state-preparation queries to learn an L-dimensional pure state to error ξ.
- [supported] The paper reports that the QIPM runtime is dominated by repeated block-encodings, large condition numbers, and tomography overhead, with tomography contributing the largest multiplicative repetition factor.
- [speculative] The authors note that asymptotic quantum speedup for QIPMs may exist only in restricted parameter regimes where κ_F is neither too large nor too small, but their experiments do not establish such an advantage for portfolio optimization.
- [speculative] The paper suggests that improved tomography, better preconditioning, specialized QRAM hardware, or structural changes to QIPMs might reduce costs, but none of these improvements are demonstrated end-to-end here.
- [supported] The authors estimate that even under a favorable hypothetical dedicated-QRAM scenario running at 4 GHz, solving the n = 100 instance would still take on the order of ten thousand years due to the total number of QRAM calls.
- [supported] The study emphasizes that end-to-end resource analysis can overturn optimistic asymptotic expectations by exposing large hidden constants and data-loading/readout bottlenecks.

**Results summary:** This preprint performs a full end-to-end resource analysis of a fault-tolerant quantum interior point method for second-order cone programming, using portfolio optimization as the main financial-services use case. The authors combine explicit circuit constructions for block-encoding, quantum linear system solving, and tomography with numerical simulations of small portfolio instances based on historical stock data. Their main empirical conclusion is negative: for n = 100 assets and optimization precision ϵ = 10^-7, the estimated requirements are about 8 million logical qubits, 7 × 10^29 T gates, and 2 × 10^24 T-depth, making the approach impractical by many orders of magnitude. Simulations up to n = 120 indicate that key parameters such as the Frobenius condition number and tomography precision worsen with problem size, while simple preconditioning helps but does not qualitatively change the outlook. The paper therefore argues that practical quantum advantage for this QIPM-based portfolio optimization approach is not currently supported and would require fundamental algorithmic improvements. Because this is a preprint and the evidence is based on simulation/resource estimation rather than hardware demonstration, any quantum advantage implication remains speculative.

**Performance claims:**
- Estimated resources at n = 100, ϵ = 10^-7: 8 × 10^6 logical qubits
- Estimated resources at n = 100, ϵ = 10^-7: 7 × 10^29 total T gates
- Estimated resources at n = 100, ϵ = 10^-7: 2 × 10^24 T-depth
- Estimated number of individual quantum circuits at n = 100: about 6 × 10^12
- Tomography query bound: at most 115 L ln(L) / ξ^2 state-preparation queries to learn an L-dimensional pure state to error ξ
- Leading-order QIPM qubit complexity: 4L^2
- Leading-order QIPM T-depth complexity: (5 × 10^8) κ_F L √r ξ^-2 log2(ϵ^-1) log2(L) log2(κ_F L^(14/27) ξ^-1)
- Leading-order QIPM T-count complexity: (1 × 10^8) κ_F L^3 √r ξ^-2 log2(ϵ^-1) log2(L) log2(κ_F ξ^-1)
- Portfolio-specific leading-order logical qubits: 800 n^2
- Portfolio-specific leading-order T-depth: (1 × 10^10) κ_F n^1.5 ξ^-2 log2(n) log2(ϵ^-1) log2(κ_F n^(14/27) ξ^-1)
- Portfolio-specific leading-order T-count: (5 × 10^11) κ_F n^3.5 ξ^-2 log2(n) log2(ϵ^-1) log2(κ_F ξ^-1)
- At n = 100, a single QLSS subroutine estimate uses about 3 × 10^11 T-depth and 1 × 10^17 T-count
- Observed median condition number used in resource estimate at n = 100 and duality gap 10^-7: κ_F = 1.6 × 10^4
- Observed median tomography repetition factor used in resource estimate: k = 3.3 × 10^8
- Preconditioning reduced κ_F by more than an order of magnitude in the studied portfolio instances
- Classical laptop baseline claim: n = 100 portfolio optimization can be solved in seconds classically
## Quantum advantage claim
**Classification:** speculative

Although QIPMs are discussed as potentially offering asymptotic speedups, this preprint does not demonstrate quantum advantage. Its simulation-based resource analysis instead argues that the analyzed approach is impractical for portfolio optimization and would need fundamental improvements before any practical advantage could emerge.
## Limitations
- The paper is a preprint and has not undergone peer review.
- Numerical results only simulate small portfolio optimization instances (up to about 120 stocks), which are not large enough to make conclusive statements about asymptotic scaling.
- Resource estimates depend on instance-specific parameters such as the Frobenius condition number and tomography precision, whose scaling is uncertain and variable across instances.
- The analysis stops at the logical-resource level and does not include a full physical-level fault-tolerant implementation.
- The estimated resources are extremely large even for modest problem sizes (e.g., n = 100), making practical deployment infeasible with foreseeable hardware.
- The QIPM fundamentally relies on costly pure-state quantum tomography, which dominates runtime and is a major bottleneck.
- The algorithm assumes access to large QRAM, whose practical realization and cost remain uncertain.
- The numerical study uses simulated quantum subroutines rather than execution on real quantum hardware, so hardware noise and control errors are not empirically validated.
- The infeasible QIPM variant emphasized in the main analysis does not enjoy the stronger O(sqrt(r)) convergence guarantee; allowing infeasible intermediate points weakens theoretical guarantees.
- For feasible QIPM variants, obtaining a null-space basis via QR decomposition incurs a large one-time classical cost that could dominate runtime.
- The hand-constructed null-space basis for the feasible variant is ill-conditioned, leading to a large condition number of the reduced Newton system.
- The portfolio optimization formulation uses a specific SOCP encoding and specific constraints; conclusions may not generalize to all portfolio optimization formulations.
- The covariance construction uses historical stock data over a number of time epochs that must grow with the number of assets, which may itself be restrictive.
- The authors note that their reported numbers should not be interpreted as the final word because further optimizations may exist.
- [inferred] No direct benchmark against state-of-the-art production classical portfolio optimizers beyond broad runtime comparisons on laptops/iterative solvers is provided.
- [inferred] The study uses randomly sampled historical-stock instances from one market index, which may limit external validity across asset classes, market regimes, and institutional portfolio constraints.
- [inferred] Reproducibility may be limited because some performance conclusions depend on implementation choices, heuristics, and adaptive precision settings rather than fully standardized benchmarks.
- [inferred] The work focuses on fault-tolerant resource estimates, so it does not assess whether any near-term or NISQ approximation of the method could be useful.
## Open questions
- How do the key parameters kappa_F and xi scale for larger, industrially relevant problem sizes beyond those simulated?
- Why do kappa_F and xi^-1 appear to plateau rather than diverge as the duality gap approaches zero in the tested instances?
- Can fundamental changes to QIPMs remove or substantially reduce the tomography bottleneck?
- Can more advanced tomography methods, such as newer O(L log L / xi) approaches, materially improve end-to-end practicality once full gate overhead is included?
- Can better preconditioning significantly reduce the effective condition number in realistic portfolio optimization instances?
- Would alternative QLSS implementations with better constants outperform the chosen discrete-adiabatic solver in practice?
- Can dedicated QRAM hardware make data loading practical enough to change the overall feasibility of the approach?
- Under what conditions, if any, can QIPMs achieve a practical quantum advantage over strong classical interior-point or iterative linear-system solvers?
- How general are the observed empirical trends across other SOCP applications beyond portfolio optimization?
- Do infeasible-intermediate-point QIPMs perform comparably to feasible variants more broadly, despite weaker theory?
- Can additional parts of the interior-point pipeline be quantized to avoid repeated classical readout and reconstruction?
- [inferred] How sensitive are the results to different portfolio models, covariance estimators, transaction constraints, and market datasets?

**Future work:**
- Further examine the algorithm to uncover optimizations that reduce resource costs.
- Develop fundamental improvements to multiple aspects of the QIPM rather than superficial optimizations.
- Investigate improved pure-state tomography methods with better asymptotic query complexity and quantify their full finite-resource overhead.
- Pursue stronger preconditioning methods to reduce the condition number of the Newton systems.
- Explore alternative QLSS implementations, including approaches based on variable-time amplitude amplification or other methods with better practical constants.
- Study adaptive step-size strategies and other heuristic modifications that may reduce the number of IPM iterations.
- Better understand empirically and theoretically why kappa_F and xi^-1 do not diverge in the tested portfolio instances.
- Explore whether structural changes to QIPMs can circumvent or eliminate the need for costly tomography.
- Investigate whether additional components of the IPM can be quantized to improve overall performance.
- Develop specialized or dedicated QRAM hardware and exploit matrix structure to reduce data-loading overhead.
- Extend end-to-end resource analyses of this type to other quantum algorithms and applications that rely on QRAM, QLSS, and tomography.
- Perform larger-scale studies and simulations on more realistic, classically challenging portfolio sizes if feasible.
- [inferred] Validate the conclusions under peer review and with independent reproductions.
- [inferred] Benchmark against stronger classical baselines, including modern commercial SOCP/IPM solvers and iterative preconditioned methods, on matched datasets.
## Key ideas
- #idea:quantum-advantage — The paper evaluates a quantum interior-point approach motivated by possible asymptotic speedups for portfolio optimisation, but finds no practical advantage in the studied regime.
- #contradiction:classical-vs-quantum — End-to-end resource estimates show the quantum method is vastly less practical than classical interior-point solvers for n=100 portfolio instances, which can be solved classically in seconds.
- #contradiction:scalability — Empirical scaling suggests condition number and tomography precision requirements worsen with portfolio size, undermining optimistic scalability assumptions for QIPM-based finance applications.
- #limitation:simulation-only — All results come from logical resource estimation and classical emulation of the quantum subroutines rather than execution on a real QPU.
- #limitation:no-empirical-validation — Quantum performance claims are not validated experimentally on hardware; the quantum linear solve is replaced by exact classical solves plus simulated tomography noise.
- #limitation:qubit-count — Representative n=100 instance requires about 8×10^6 logical qubits, making the approach impractical.
- #limitation:data-encoding — The method depends on QRAM-based block-encoding and repeated state preparation/readout, with data access and tomography dominating costs.
## Contradictions
- The paper contradicts optimistic quantum-superiority narratives for portfolio optimisation by showing that a full end-to-end quantum interior-point implementation would require astronomically large logical resources and be far slower in practice than classical solvers.
- The paper contradicts scalability claims from earlier QIPM-style analyses by finding that the Frobenius condition number κ_F grows with portfolio size in the tested instances, which worsens rather than preserves the prospects for scalable quantum advantage.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
