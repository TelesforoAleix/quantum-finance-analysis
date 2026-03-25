---
aliases:
- 'Quantum variational optimization: The role of entanglement and problem hardness'
- Quantum variational optimization role
authors:
- Pablo Díez-Valle
- Diego Porras
- Juan José García-Ripoll
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
- VQE
- QUBO
- variational
- classical-simulation
paper_type: ''
quantum_advantage_claim: speculative
related_papers: []
relevance_phase1: medium
relevance_phase3: medium
source_type: preprint
source_type_confidence: high
step1_date: '2026-03-25T15:53:37.338812'
step1_model: gpt-5.1
step2_date: '2026-03-25T15:53:42.032097'
step2_model: gpt-5.1
step3_date: '2026-03-25T15:54:17.570311'
step3_model: gpt-5.4
step4_date: '2026-03-25T15:54:57.955508'
step4_model: gpt-5.4
step5_date: '2026-03-25T15:55:26.146102'
step5_model: gpt-5.4
step6_date: '2026-03-25T15:55:37.414003'
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
- method/VQE
- method/QUBO
- method/variational
- method/classical-simulation
- idea/quantum-advantage
- idea/near-term-feasibility
- idea/hybrid-approach
- contradiction/classical-vs-quantum
- contradiction/scalability
title: 'Quantum variational optimization: The role of entanglement and problem hardness'
topic_tags:
- portfolio-optimisation
year: 2021
zotero_key: ''
---

## Abstract summary
The paper systematically studies how entanglement structure, variational circuit design, and problem characteristics affect the performance of variational quantum optimization, focusing on VQE applied to QUBO instances on random graphs of varying density. The authors compare different entangling layouts (including graph-matched, linear, random, and product-state Ansätze), standard energy-based VQE versus CVaR-based cost functions, and multiple classical optimizers, using both exact state simulations and finite-shot scenarios. They find that CVaR-based objectives and graph-adapted entanglement can improve performance in some regimes, but also that product-state Ansätze combined with CVaR can be highly competitive and potentially define powerful quantum-inspired classical optimization methods, with problem hardness strongly correlated to the Hamming distance between ground and first-excited states.
## Methodology
This preprint reports an empirical numerical benchmarking study of variational quantum optimization for combinatorial optimization, focusing on VQE and a CVaR-modified VQE applied to QUBO instances mapped to Ising Hamiltonians. The authors generate random graph-based QUBO problems with tunable density, assign random integer edge weights in [-10,10], and compare multiple variational ansatz families: entangled circuits with linear, graph-compatible, or random CZ entangling layers, and a product-state ansatz with no entanglement. They evaluate both exact wavefunction simulations and finite-shot measurement emulations to study the effects of entanglement structure, circuit depth, cost-function choice, optimizer choice, and problem hardness. Classical optimizers are benchmarked first, leading to the use of L-BFGS-B for exact-state simulations and SPSA for finite-shot settings. Performance is assessed over large batches of randomly generated instances using success rate based on overlap with the exact ground state, number of objective-function evaluations to convergence, overlap distributions, and correlations with graph density and Hamming distance between ground and first-excited states. The study is explicitly a preprint and uses ideal classical simulation rather than real quantum hardware.

**Algorithms used:** VQE, CVaR-VQE, SPSA, L-BFGS-B, BFGS, SLSQP, COBYLA, Nelder-Mead, Powell
**Frameworks:** SciPy, NetworkX

**Experimental setup:** All experiments were conducted as classical simulations of an ideal quantum computer. Two simulation regimes were used: (1) exact full-wavefunction evaluation with effectively infinite shots, and (2) finite-shot emulation of measurement-based cost estimation, including cases such as 3000 and 9000 measurements per objective evaluation. Simulations and parameter optimization were run on compute nodes with two Intel Sandybridge E5-2670 processors, each with 8 cores at 2.6 GHz, 20 MB cache, and 64 GB RAM, running CentOS 7.4. No real QPU or noise model was used.

**Dataset:** Synthetic QUBO benchmark instances generated from random regular and unstructured random graphs with tunable density. Edge weights were sampled uniformly as random integers in the interval [-10, 10]. For each configuration of qubit count and graph density, 1600 problem instances were generated; different experiments used separate sets of 1600 instances.
## Experiment details
### Input
Input consists of randomly generated QUBO problems represented as graphs with N vertices/qubits and density D. Graphs were generated using NetworkX as regular or unstructured random graphs, then weighted with uniformly sampled integer edge weights in [-10,10]. Experiments varied problem size (examples include N=6, 9, 12 qubits), graph density (including sparse, intermediate, and dense cases such as D=0.045, 0.258, 0.894), and used Nins=1600 instances per configuration. QUBOs were mapped to Ising Hamiltonians via xi -> (1 + sigma_z_i)/2. No real financial dataset was used.

### Process
1. Generate random graph-based QUBO instances with chosen qubit count N and density D, assigning random integer weights in [-10,10]. 2. Map each QUBO to an Ising Hamiltonian. 3. Choose a variational ansatz: either entangled VQE ansatz with L layers of single-qubit Ry rotations and CZ entangling layers, or a product-state ansatz (L=0). Entanglement patterns tested were linear nearest-neighbor, graph-compatible, and random pairwise entanglement. 4. Initialize parameters with theta_n0 = pi/4 to create a uniform-superposition-like starting state and theta_nl approximately 1e-2 for l >= 1. 5. Optimize either the standard VQE objective (mean energy) or CVaR-VQE objective using a classical optimizer. Seven optimizers were benchmarked; L-BFGS-B was selected for exact wavefunction simulations and SPSA for finite-shot simulations. 6. Evaluate cost either exactly from the full statevector or approximately from sampled measurement outcomes; finite-shot studies included 3000 and 9000 shots per cost evaluation. 7. Repeat over 1600 instances per setting and summarize results with bootstrap-based 95% confidence intervals. 8. Assess performance using overlap with the exact ground state, success indicator S based on overlap threshold beta=0.1, number of objective evaluations to convergence, and analyses versus graph density, circuit depth, and Hamming distance between ground and first-excited manifolds. 9. In CVaR-VQE comparisons, a typical setting used rho = 10%; some analyses compared L=0 and L=3 ansatz depths, while others varied L systematically.

### Output
Reported outputs include success rate (average of binary success indicator over instances), overlap distribution between final variational state and exact solution, number of objective-function evaluations required for convergence, and qualitative comparisons of optimizer robustness. Baseline comparisons include standard VQE versus CVaR-VQE, product-state versus entangled ansatz families, different entanglement topologies (linear, compatible, random), different circuit depths, exact-state versus finite-shot estimation, and multiple classical optimizers. Results are presented as averages over 1600 instances with 95% confidence intervals obtained by bootstrap resampling.

### Parameters
- qubits: [6, 9, 12]
- ansatz_depth_layers: [0, 1, 3]
- entangling_gates: CZ gates
- single_qubit_rotations: Ry rotations
- cvar_rho: 0.1
- shots_tested: [3000, 9000, 'infinite/exact wavefunction']
- instances_per_configuration: 1600
- success_overlap_threshold_beta: 0.1
- initial_theta_n0: pi/4
- initial_theta_nl_for_l_ge_1: approximately 1e-2
- optimizers_benchmarked: ['Powell', 'SLSQP', 'BFGS', 'L-BFGS-B', 'SPSA', 'COBYLA', 'Nelder-Mead']
- optimizer_used_exact_simulation: L-BFGS-B
- optimizer_used_finite_shots: SPSA
- edge_weight_range: [-10, 10]

### Hardware
Ideal classical simulation only; no real quantum processor used. Computational environment: nodes with two Intel Sandybridge E5-2670 CPUs, 8 cores each at 2.6 GHz, 20 MB cache, 64 GB RAM total, running CentOS 7.4. Finite-shot experiments emulate measurement sampling; exact simulations use full wavefunction/state calculation. No noise model or transpilation settings are reported.

### Reproducibility
Preprint with substantial methodological detail on instance generation, ansatz design, initialization, optimizers, shot settings, and evaluation metrics. Uses standard libraries (SciPy 1.3.2, NetworkX), but no code repository is mentioned in the provided text. Synthetic data generation is described well enough for partial replication, though some implementation details (e.g., exact convergence tolerances and SPSA hyperparameters) are not fully specified.
## Findings
- [supported] In ideal classical simulations of QUBO optimization, CVaR-VQE with ρ = 10% outperformed standard VQE in both success rate and convergence speed across tested problem sizes, densities, and ansatz choices.
- [supported] Standard VQE often converged to classical states that were either the exact optimum or nearly orthogonal to it, whereas CVaR-VQE more often converged to superpositions with lower direct overlap but higher probability of recovering the optimum through repeated sampling.
- [supported] Stochastic classical optimizers were more robust than gradient-based optimizers when the cost function was estimated from finite-shot measurements; SPSA, COBYLA, Powell, and Nelder-Mead remained effective, while SLSQP, BFGS, and L-BFGS-B degraded under measurement noise.
- [supported] Matching the entangling-gate pattern to the QUBO graph topology provided only a marginal benefit, mainly for sparse or low-density graphs, and this benefit largely vanished for dense problems.
- [supported] The success probability of CVaR-VQE saturated with relatively shallow circuits, while the number of cost-function evaluations increased with circuit depth.
- [supported] Product-state ansatzes combined with CVaR achieved competitive and sometimes superior practical performance relative to entangled ansatzes, especially when measurement budgets were limited.
- [supported] Under finite-shot conditions, product-state methods showed more stable evaluation costs and could outperform entangled ansatzes at low shot counts such as 3000 shots.
- [supported] The paper finds a strong correlation between optimization hardness and the Hamming distance between the ground-state manifold and first-excited manifold; larger distances were associated with lower success rates and more evaluations.
- [supported] The Hamming-distance-based hardness indicator was more predictive than graph density, with reported success-rate differences up to about 40% in full-wavefunction simulations and about 30% with 9000-shot estimation.
- [speculative] For dense QUBO instances, including those the authors associate with quantum finance scenarios, topology-adapted entanglement does not appear to provide a meaningful advantage.
- [speculative] The results suggest a quantum-inspired classical optimization method based on product states plus CVaR could outperform existing NISQ architectures in some regimes.
- [speculative] Claims that quantum variational optimization can solve optimization problems faster or at larger scale are not demonstrated here; the study instead highlights important limitations and regimes where classical or quantum-inspired alternatives may be preferable.

**Results summary:** This preprint numerically benchmarks VQE and CVaR-VQE on randomly generated QUBO problems defined on graphs with tunable density, using ideal statevector simulation and finite-shot emulation rather than real quantum hardware. Across 1600 instances per configuration, the authors find that CVaR-VQE with ρ = 10% consistently improves over standard VQE in success rate and convergence speed. They also show that graph-compatible entanglement offers only modest gains, mostly for sparse graphs, and that these gains disappear for dense problems. Circuit depth helps only up to a shallow plateau, after which optimization cost rises without commensurate success improvements. A key result is that product-state ansatzes combined with CVaR perform surprisingly well and can be practically preferable, especially under finite-shot noise, suggesting a strong quantum-inspired classical baseline. Finally, the study identifies the Hamming distance between the ground and first-excited manifolds as a stronger predictor of problem hardness than graph density. Because this is a preprint and all evidence is from simulation, any broader quantum advantage implications remain speculative.

**Performance claims:**
- 1600 random QUBO instances per configuration were evaluated, with 95% confidence intervals obtained by bootstrap resampling
- CVaR-VQE used ρ = 10%
- Finite-shot experiments emulated 3000 and 9000 measurements per cost-function evaluation
- Success threshold was β = 0.1 overlap with the target state
- With β = 0.1, 100 measurements of a successful final state imply at least 99.997% probability of obtaining the correct solution
- For hardness stratified by Hamming distance and 3000 shots, product-state success rates were 31%, 22%, and 16% for easy/intermediate/hard groups, versus 31%, 25%, and 20% for entangled ansatzes
- For hardness stratified by Hamming distance and 9000 shots, product-state success rates were 46%, 34%, and 26%, versus 57%, 40%, and 30% for entangled ansatzes
- For full-wavefunction simulations, product-state success rates were 98%, 69%, and 55%, versus 99%, 83%, and 61% for entangled ansatzes
- For 3000 shots, average cost-function evaluations were 335, 274, and 327 for product states versus 496, 538, and 625 for entangled ansatzes across easy/intermediate/hard groups
- For 9000 shots, average cost-function evaluations were 316, 262, and 298 for product states versus 463, 372, and 461 for entangled ansatzes
- For full-wavefunction simulations, average cost-function evaluations were 73, 206, and 288 for product states versus 129, 390, and 560 for entangled ansatzes
- The Hamming-distance hardness effect produced success-rate differences of up to about 40% in full simulations and about 30% with 9000-shot estimation
- At high densities without statistical uncertainty, entangled ansatzes improved success rate only marginally by about 2–3% over product states according to the authors' discussion
- Under finite-shot conditions, entangled ansatzes could improve success rates by 20% or more in some dense-problem settings, though with higher resource demands and no demonstrated end-to-end quantum advantage
## Quantum advantage claim
**Classification:** speculative

The paper does not demonstrate quantum advantage. All results are from classical simulation or finite-shot emulation, not real hardware, and the authors explicitly find regimes where product-state/CVaR methods that are classically simulable can match or outperform entangled variational approaches.
## Limitations
- Results are based on classical simulations of ideal quantum computers rather than experiments on real quantum hardware.
- The benchmark deliberately leaves aside experimental imperfections such as hardware noise and disconnected qubits.
- Problem instances are limited to relatively small sizes (up to 12 qubits in the reported experiments), constraining conclusions about large-scale applicability.
- The study focuses only on QUBO problems on random graphs with tunable density, which may limit generalization to other optimization problem classes.
- Edge weights are randomly sampled integers in the interval [-10, 10], so conclusions may depend on this synthetic problem distribution.
- The analysis uses specific ansatz families (linear, compatible, random entanglement, and product states), so findings may not transfer to other circuit constructions.
- The finite-shot analysis considers selected shot budgets (e.g., 3000 and 9000), leaving broader measurement regimes unexplored.
- The success metric depends on a chosen overlap threshold (beta = 0.1), which is somewhat arbitrary and may affect reported success rates.
- The study uses a limited set of classical optimizers and then fixes L-BFGS-B or SPSA depending on the simulation setting, so optimizer-dependent effects may remain.
- The observed advantage of compatible entanglement is described as marginal and disappears for dense problems, limiting practical significance for dense financial QUBOs.
- The paper identifies correlations between hardness and Hamming distance, but correlation does not establish causation or a complete hardness theory.
- [inferred] No direct comparison is provided against state-of-the-art classical combinatorial optimization solvers, limiting assessment of any practical quantum advantage.
- [inferred] No wall-clock runtime or end-to-end resource analysis on actual quantum systems is given; function-evaluation counts are only a proxy for practical cost.
- [inferred] Scalability to production-relevant financial optimization sizes is unproven given the small simulated instances.
- [inferred] The work does not address embedding, connectivity constraints, calibration drift, or error mitigation that would matter on NISQ hardware.
- [inferred] Because this is a preprint, the findings have not yet been validated through peer review.
- [inferred] Reproducibility may be limited because implementation details for the homemade SPSA optimizer and full experimental pipeline are not exhaustively specified in the excerpt.
## Open questions
- What is the precise role of entanglement and correlations in the success and efficiency of quantum variational optimization?
- When does adapting the entanglement structure to the problem topology provide a meaningful advantage, especially beyond low-dimensional or sparse graphs?
- Why does the success probability saturate with relatively shallow circuits, and what intrinsic algorithmic limitation causes this behavior?
- How do these methods perform on dense optimization problems such as those arising in quantum finance scenarios?
- Can product-state ansatzes combined with CVaR be developed into competitive quantum-inspired classical optimization methods?
- How robust are the reported findings under realistic hardware noise, decoherence, gate errors, and connectivity constraints?
- Does the correlation between problem hardness and the Hamming distance between ground and first-excited states hold more broadly across other problem families?
- Can Hamming distance be turned into a predictive hardness metric for practical benchmark design rather than just an observed correlation?
- What algorithmic mechanisms could enhance macroscopic tunneling between distant low-energy solutions?
- How would the conclusions change for larger qubit counts and larger, more realistic financial optimization instances?
- To what extent are the results sensitive to the choice of classical optimizer, initialization strategy, and CVaR parameter rho?

**Future work:**
- Investigate further quantum-inspired classical optimization methods based on CVaR metrics with product-state ansatzes.
- Study other quantum optimization algorithms, explicitly including QAOA, as alternatives to VQE/CVaR-VQE.
- Engineer benchmarks using the observed relation between hardness and Hamming distance between low-energy states.
- Develop quantum algorithms that enhance the probability of macroscopic tunneling between solutions.
- Extend the analysis to more realistic scenarios with limited resources and, implicitly, real hardware effects.
- [inferred] Validate the conclusions experimentally on real NISQ devices with noise, connectivity constraints, and error mitigation.
- [inferred] Test larger-scale instances and more realistic financial QUBO formulations to assess practical relevance for financial services.
- [inferred] Compare against strong classical baselines to determine whether any quantum or hybrid advantage remains after accounting for classical heuristics.
- [inferred] Explore broader ansatz classes, optimizer choices, and CVaR settings to determine whether the reported trends are architecture-specific.
- [inferred] Analyze resource scaling beyond function-evaluation counts, including circuit depth, shot complexity, and wall-clock runtime.
## Key ideas
- #idea:near-term-feasibility — Classical-simulation benchmark studies VQE and CVaR-VQE on small QUBO instances, showing how ansatz structure, depth, and finite-shot estimation affect optimization performance.
- #idea:quantum-advantage — CVaR-based VQE consistently outperforms standard energy-based VQE in success rate and convergence speed on the tested synthetic QUBO benchmarks.
- #idea:hybrid-approach — Product-state CVaR ansatzes, which are classically simulable, are often competitive with or better than entangled ansatzes, especially under limited-shot budgets, suggesting strong quantum-inspired classical baselines.
- #idea:near-term-feasibility — Graph-matched entanglement provides only marginal benefit and mainly on sparse graphs; for dense QUBOs the benefit largely disappears.
- #idea:near-term-feasibility — Performance saturates at shallow circuit depth while optimization cost rises with deeper circuits, limiting practical NISQ usefulness.
- #idea:near-term-feasibility — SPSA and other stochastic/gradient-free optimizers are more robust than gradient-based methods when objective values are estimated from finite shots.
- #idea:near-term-feasibility — Hamming distance between ground and first-excited manifolds is a stronger predictor of optimization hardness than graph density.
## Contradictions
- The paper contradicts common assumptions that entanglement and deeper variational circuits are necessary for superior QUBO optimization: product-state CVaR methods can match or outperform entangled VQE variants under finite-shot conditions while remaining classically simulable.
- The paper contradicts broad near-term quantum-superiority narratives by showing that quantum-inspired classical baselines may be preferable to NISQ variational approaches on the tested instances.
- The paper raises a scalability contradiction: results are limited to 6–12 qubits in ideal classical simulation, so optimistic claims that current VQE-style methods scale to production-relevant financial QUBOs are not supported.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
