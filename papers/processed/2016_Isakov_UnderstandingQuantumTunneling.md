---
aliases:
- Understanding Quantum Tunneling through Quantum Monte Carlo Simulations
- Understanding Quantum Tunneling through
authors:
- Sergei V. Isakov
- Guglielmo Mazzola
- Vadim N. Smelyanskiy
- Zhang Jiang
- Sergio Boixo
- Hartmut Neven
- Matthias Troyer
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
- classical-simulation
- quantum-annealing
paper_type: ''
quantum_advantage_claim: speculative
related_papers:
- 2021_King_QuantumAdvantage
- 2022_Hauke_NonStoquasticHamiltonians
relevance_phase1: low
relevance_phase3: low
source_type: preprint
source_type_confidence: high
step1_date: '2026-03-25T15:50:03.204665'
step1_model: gpt-5.1
step2_date: '2026-03-25T15:50:10.763938'
step2_model: gpt-5.1
step3_date: '2026-03-25T15:50:57.942329'
step3_model: gpt-5.4
step4_date: '2026-03-25T15:51:28.839325'
step4_model: gpt-5.4
step5_date: '2026-03-25T15:51:54.557252'
step5_model: gpt-5.4
step6_date: '2026-03-25T15:52:07.758717'
step6_model: gpt-5.4
steps_completed:
- 1
- 2
- 3
- 4
- 5
- 6
tags:
- method/classical-simulation
- method/quantum-annealing
- idea/quantum-advantage
- idea/near-term-feasibility
- idea/hybrid-approach
- contradiction/classical-vs-quantum
- contradiction/scalability
title: Understanding Quantum Tunneling through Quantum Monte Carlo Simulations
topic_tags: []
year: 2015
zotero_key: ''
---

## Abstract summary
The paper analyzes how quantum Monte Carlo (QMC) simulations capture quantum tunneling processes that are relevant for quantum annealing, focusing on Ising ferromagnets and related models. By comparing tunneling rates and their scaling with system size, the authors show that standard path-integral QMC reproduces the same leading exponential dependence on the tunneling gap as incoherent quantum tunneling, and that projector-type QMC with open imaginary-time boundaries can achieve a quadratic speedup in this scaling. They also discuss conditions and model classes where this correspondence may break down, highlighting implications for when QMC can reliably predict quantum annealer performance.
## Methodology
This preprint combines theoretical analysis with numerical validation to study whether path-integral quantum Monte Carlo (QMC) reproduces the scaling of quantum tunneling rates relevant to quantum annealing. The authors develop an instanton-based semiclassical framework linking tunneling amplitudes and QMC escape rates via imaginary-time path integrals, Kramers escape theory, and saddle-point analysis of the free-energy functional. They then validate the theory numerically on two classes of systems: (1) a one-dimensional continuous-space double-well potential V(x)=lambda x^4-x^2, and (2) transverse-field Ising ferromagnets, including linear chains and fully connected clusters. For the spin systems, they perform path-integral Monte Carlo with both periodic imaginary-time boundary conditions (standard PIMC) and open boundary conditions (projector/path-integral ground state, PIGS), measuring average tunneling times as the number of Monte Carlo sweeps needed to generate a magnetization-reversing instanton configuration. They compare these measured tunneling times against exact-diagonalization estimates of the spectral gap, testing the predicted scaling xi proportional to 1/Delta^2 for periodic-boundary QMC and xi proportional to 1/Delta for open-boundary PIGS. The work is a preprint and is primarily a theoretical-plus-computational study rather than an application to financial data.

**Algorithms used:** Quantum Monte Carlo, Path-Integral Monte Carlo, PIGS, Path Integral Molecular Dynamics, Exact Diagonalization, WKB, Langevin dynamics, Metropolis Monte Carlo, Wolff algorithm, Swendsen-Wang algorithm

**Experimental setup:** Numerical experiments were conducted entirely via classical simulation. For continuous-space tunneling, the authors used continuous-space path-integral QMC with both local Metropolis updates and global updates via path-integral molecular dynamics/Langevin dynamics. For spin systems, they mapped the transverse-field Ising model to a (D+1)-dimensional classical path-integral representation with P Trotter replicas/time slices, using both discrete-time simulations with P=128 and continuous-time QMC. Standard PIMC used periodic boundary conditions in imaginary time, while PIGS used open boundary conditions. Exact diagonalization was used to compute energy gaps for comparison.

**Dataset:** No external dataset was used. Inputs are synthetic physics models: a one-dimensional double-well potential V(x)=lambda x^4-x^2, transverse-field Ising ferromagnetic chains, fully connected Ising clusters, the Curie-Weiss/p-spin mean-field model, and a Grover-search Hamiltonian analyzed theoretically.
## Experiment details
### Input
Synthetic model instances only. Continuous-space case: double-well potential V(x)=lambda x^4-x^2 with lambda ranging from 0.05 to 0.20, mass m=1/2, temperature T=0.05, and P=64 replicas in the supplementary continuous-space experiments. Spin case: transverse-field Ising Hamiltonian H=-Gamma sum sigma_x - sum J_ij sigma_z sigma_z, with nearest-neighbor chain couplings J_ij=delta_{i,j+1}+delta_{i,j-1} and fully connected couplings J_ij=1/(2L). System sizes reported include fits over L=12 to 16 for PIMC and L=12 to 18 for PIGS; inverse temperatures include beta=8 in the main text for fully connected clusters and beta=16, 20, 24 in supplementary chain experiments; transverse fields include values such as Gamma=0.7 for temperature-scaling plots and Gamma in the range 0.6 to 0.8 in chain benchmarks. Simulations were initialized in fully polarized/metastable states: x_k=x_min in the right well for the double-well model and m(tau)=1 (all spins up) for Ising models.

### Process
1. Derive theoretical predictions for tunneling-rate scaling using instanton methods, imaginary-time path integrals, and Kramers escape arguments. 2. For the continuous-space double-well model, discretize the imaginary-time path integral with P replicas, initialize all replicas in one well, and sample trajectories using either local Metropolis updates (PIMC) or global Langevin/MD-based updates (PIMD). One Monte Carlo sweep consists of P local attempts in the local-update scheme. 3. Detect a tunneling event when 25% of replicas cross a threshold (for the double well, x < -x_min/2; for spin systems, at least 25% of replicas have magnetization m(tau)=-1). Record the first-passage time as the tunneling time xi. 4. For spin systems, perform path-integral QMC on the Trotterized transverse-field Ising model using either periodic imaginary-time boundary conditions (PIMC) or open boundary conditions (PIGS). Updates use variants of Wolff and Swendsen-Wang cluster methods local in space and extended along imaginary time; simulations were also run in the continuous-time limit. 5. Average tunneling times over runs and fit xi(L) to exponential forms a exp(bL). 6. Compute exact spectral gaps Delta(Gamma,L) by exact diagonalization and compare xi against 1/Delta^2 for periodic-boundary QMC and against 1/Delta for PIGS. 7. Examine temperature dependence, system-size scaling, and instanton-shape agreement between QMC trajectories and analytical instanton predictions.

### Output
Outputs are average QMC/PIGS tunneling times xi, exponential fit coefficients/exponents versus system size, temperature dependence of xi, and comparisons to exact-diagonalization gap-based baselines. Main reported metrics are scaling relationships: xi proportional to 1/Delta^2 for standard periodic-boundary QMC and xi proportional to 1/Delta for open-boundary PIGS, plus agreement of instanton shapes between simulation and theory. Baseline/comparison methods are exact diagonalization of the quantum Hamiltonian and analytical/WKB tunneling predictions.

### Parameters
- trotter_replicas: [64, 128]
- inverse_temperatures_beta: [8, 16, 20, 24]
- temperature_continuous_space: 0.05
- lambda_range_double_well: [0.05, 0.2]
- mass_double_well: 0.5
- transverse_field_values_reported: [0.6, 0.65, 0.7, 0.75, 0.8]
- system_size_fit_ranges: {'PIMC': 'L=12-16', 'PIGS': 'L=12-18'}
- tunneling_detection_threshold: 25% of replicas reversed/crossed threshold
- boundary_conditions: ['periodic imaginary-time boundary conditions', 'open imaginary-time boundary conditions']
- update_methods: ['local Metropolis updates', 'cluster updates based on Wolff/Swendsen-Wang variants', 'global Langevin/MD updates in continuous-space PIMD']

### Hardware
{'hardware_type': 'classical computation only', 'simulators': ['continuous-space path-integral QMC', 'discrete-time and continuous-time path-integral QMC', 'path-integral molecular dynamics', 'exact diagonalization'], 'qpu_used': False}

### Reproducibility
Preprint with substantial methodological detail and supplementary derivations/parameters, including model definitions, parameter ranges, update schemes, boundary conditions, and event-detection rules. No code repository is mentioned in the provided text. Reproducibility is moderate to good for an expert in computational physics, though some implementation details (e.g., number of independent runs, random seeds, exact stopping/statistical procedures) are not fully specified.
## Findings
- [supported] In quantum Monte Carlo (QMC) simulations of tunneling, the QMC tunneling/escape rate shows the same leading exponential scaling with system size as incoherent quantum tunneling, namely O(Δ^2), where Δ is the tunneling splitting.
- [supported] For a one-dimensional double-well potential, the average QMC tunneling time agrees closely with 1/Δ^2 over a wide range of time scales, based on simulation results.
- [supported] For transverse-field Ising ferromagnets (both fully connected clusters and linear chains), the measured average QMC tunneling time scales identically to 1/Δ^2 within reported error bars, based on QMC simulations compared with exact diagonalization.
- [supported] Using open instead of periodic boundary conditions in imaginary time (projector QMC / PIGS) changes the scaling of QMC tunneling time from 1/Δ^2 to 1/Δ, corresponding to a quadratic speedup of QMC relative to periodic-boundary QMC and incoherent tunneling in the studied models.
- [supported] The observed scaling behavior is interpreted through an instanton picture: periodic-boundary QMC tunneling is dominated by instanton–anti-instanton pairs, while open-boundary QMC requires only a single instanton.
- [supported] In the low-temperature regime for the studied Ising models, quantum tunneling becomes more efficient than thermally activated barrier crossing, whose contribution is suppressed by exp(-βE_barrier).
- [speculative] QMC simulations can be used as a quantitatively faithful predictor of quantum annealer performance for a broad class of tunneling problems with purely imaginary-time instantons.
- [speculative] The equivalence between QMC and quantum annealing tunneling scaling may fail in problems with topological obstructions, multidimensional tunneling with complex semiclassical action, or many-body delocalized phases where interference among exponentially many tunneling paths may matter.
- [speculative] Because QMC and QA have identical leading exponential scaling for the class of problems studied, these problems are unlikely to yield a scaling quantum advantage for physical quantum annealers over classical QMC.
- [speculative] Non-stoquastic Hamiltonians may offer a route beyond the studied regime because the sign problem can prevent a matching efficient QMC algorithm.
- [speculative] A physical quantum annealer may still be many orders of magnitude faster in wall-clock time than QMC despite identical asymptotic scaling, but this is not demonstrated in this paper.

**Results summary:** This preprint studies the relationship between quantum tunneling in quantum annealing and tunneling events observed in path-integral quantum Monte Carlo. Using simulations of a continuous double-well potential and transverse-field Ising ferromagnets, the authors report that standard QMC with periodic imaginary-time boundary conditions reproduces the same leading exponential scaling as incoherent tunneling, with tunneling time proportional to 1/Δ^2. They further show that projector/open-boundary QMC (PIGS) changes the scaling to 1/Δ, which they describe as a quadratic speedup for the classical simulation method. The paper argues, via an instanton framework, that QMC can predict QA performance for a class of barrier-tunneling problems, while also noting several possible obstructions where this correspondence may break down. Because this is a preprint and the broader predictive/generalization claims are theoretical rather than broadly empirically established, any quantum-advantage implications remain speculative.

**Performance claims:**
- QMC tunneling/escape rate scales as O(Δ^2) for the studied models.
- Open-boundary QMC / PIGS achieves tunneling-time scaling proportional to 1/Δ instead of 1/Δ^2, i.e. a quadratic speedup in the studied setting.
- For the double-well potential, agreement between average QMC tunneling time and 1/Δ^2 is reported over 5 orders of magnitude in 1/Δ^2.
- For ferromagnetic Ising chains, fitted PIMC exponents versus system size L are close to exact-diagonalization exponents for 1/Δ^2: at Γ=0.8, β=24, QMC exponent 0.541(4) vs ED 0.535(4); at Γ=0.75, β=24, 0.6697(14) vs 0.662(4); at Γ=0.7, β=24, 0.81(5) vs 0.799(4).
- For ferromagnetic Ising chains, fitted PIGS exponents versus system size L are close to exact-diagonalization exponents for 1/Δ: at Γ=0.8, β=24, QMC exponent 0.289(11) vs ED 0.268(2); at Γ=0.75, β=24, 0.350(9) vs 0.331(2); at Γ=0.7, β=24, 0.417(9) vs 0.400(2); at Γ=0.65, β=24, 0.482(18) vs 0.473(2); at Γ=0.6, β=24, 0.56(2) vs 0.553(2).
- Thermally activated transitions are stated to be suppressed as exp(-βE_barrier), with E_barrier ~ L/2 for fully connected clusters and E_barrier = 4 for a linear chain.
## Quantum advantage claim
**Classification:** speculative

The paper does not demonstrate quantum advantage; instead it argues that for the studied tunneling problems, classical QMC matches the leading exponential scaling of quantum annealing, implying no asymptotic scaling advantage there. Claims about where quantum annealing might outperform QMC (e.g., non-stoquastic Hamiltonians, interference-rich regimes, hardware speed) are theoretical or conjectural and not empirically demonstrated here.
## Limitations
- As a preprint, the work has not undergone peer review.
- The main equivalence result is stated to hold only for a broad class of models with purely imaginary-time instantons, limiting generality.
- The authors explicitly note possible obstructions where QMC may fail, including topological obstructions such as winding numbers of world lines.
- The authors note that an obstruction remains when the ground-state wavefunction and its square are concentrated on different supports, even if PIGS can sometimes alleviate this.
- The authors state that QMC may be less efficient for optimization problems involving tunneling to or from multidimensional minima.
- The authors explicitly note that when the semiclassical action under the barrier is not purely imaginary and has complex features such as caustics, non-integrability, and non-analyticity, it is unclear whether QMC can faithfully recover tunneling dynamics.
- The paper identifies many-body localization/delocalization regimes as unresolved cases where QA may benefit from interference among exponentially many tunneling paths, unlike QMC.
- The empirical validation is limited to simple benchmark systems: a 1D double-well potential, ferromagnetic Ising chains, and fully connected ferromagnetic clusters.
- System sizes studied numerically are small to moderate (e.g., fits over roughly L=12-18), which limits evidence for asymptotic scaling in larger practical instances.
- Comparisons to QA performance are largely based on scaling arguments and exact diagonalization of small systems rather than experiments on physical quantum annealers.
- The tunneling-time detection criterion uses an arbitrary threshold (25% of replicas reversed), which the authors say has small effect but still introduces a methodological choice.
- Some theoretical details are deferred to future work or supplementary/in-preparation material, reducing immediate reproducibility and completeness of the argument.
- [inferred] The study does not evaluate financially relevant optimization problems or realistic application instances, limiting direct applicability to financial services.
- [inferred] No comparison is provided against state-of-the-art classical optimization heuristics beyond QMC/PIGS, so broader classical competitiveness is not established.
- [inferred] The conclusions focus on leading exponential scaling and may understate important constant-factor and polynomial-overhead effects relevant in practice.
- [inferred] The analysis assumes idealized model structure and does not incorporate hardware noise, control errors, embedding overhead, or calibration issues of real annealers, despite discussing them qualitatively.
- [inferred] The work studies mostly stoquastic settings; its conclusions may not transfer to non-stoquastic Hamiltonians where QMC faces a sign problem.
## Open questions
- For which classes of tunneling problems does the equivalence between QMC tunneling time and QA tunneling rate continue to hold?
- Under what precise conditions do topological obstructions prevent efficient QMC simulation of tunneling?
- Can QMC faithfully reproduce tunneling dynamics in multidimensional minima where the under-barrier action is complex and affected by caustics, non-integrability, or non-analyticity?
- What happens in problems with many-body localization/delocalization transitions at finite transverse field?
- To what extent can QA exploit positive interference among exponentially many tunneling paths in ways that QMC cannot?
- When do open-boundary projector methods (PIGS) reliably achieve the observed quadratic speedup over periodic-boundary QMC?
- How predictive are QMC simulations of actual hardware QA performance once real-device effects are included?
- Can non-stoquastic Hamiltonians provide quantum speedup precisely because no matching efficient QMC algorithm exists?

**Future work:**
- Explore the physical mechanisms behind the identified obstructions for QMC as starting points for studying potential quantum speedup.
- Investigate optimization problems and hardware that go beyond the class of problems analyzed here, where identical QMC/QA scaling precludes a scaling advantage.
- Study QA with non-stoquastic Hamiltonians, where the negative sign problem prevents a matching QMC algorithm.
- Further characterize the range of applicability of the instanton-based equivalence between QMC and QA.
- Examine problems with many-body localization/delocalization transitions and exponentially many tunneling paths.
- Develop a more complete theory of the equivalence between quantum-tunneling instantons and path-integral QMC instantons; the supplement notes that detailed calculations will be provided elsewhere.
- Test whether the observed PIGS advantage extends to broader classes of models and optimization landscapes.
- [inferred] Validate the claims on larger and more realistic problem instances, including application-relevant combinatorial optimization tasks.
- [inferred] Benchmark against physical quantum annealers and stronger classical baselines to assess practical rather than only asymptotic advantage.
- [inferred] Quantify finite-size, prefactor, and runtime-overhead effects beyond leading exponential scaling.
## Key ideas
- #idea:near-term-feasibility — Classical path-integral QMC reproduces the same leading exponential tunneling-time scaling as incoherent quantum annealing for the studied stoquastic tunneling models.
- #idea:hybrid-approach — Open-boundary projector QMC (PIGS) changes tunneling-time scaling from 1/Δ^2 to 1/Δ, yielding a quadratic speedup over standard periodic-boundary QMC in the tested models.
- #idea:quantum-advantage — The paper reframes quantum advantage as likely only in regimes where QMC fails, such as non-stoquastic Hamiltonians, topological obstructions, or interference-rich many-body tunneling.
- #contradiction:classical-vs-quantum — Rather than supporting generic QA superiority, the results suggest classical QMC can match QA’s asymptotic tunneling scaling on a broad studied class of problems.
- #contradiction:scalability — Claims about broad predictive power for QA are limited by validation only on small synthetic physics models and classical simulations, not large practical instances or hardware annealers.
## Contradictions
- The paper contradicts generic claims of quantum annealing superiority by showing that, for the studied stoquastic tunneling problems, classical QMC matches the same leading exponential scaling as QA and open-boundary PIGS can even improve the classical scaling. This stands in tension with stronger advantage claims such as 2021_King_QuantumAdvantage, while aligning with caveats that speedup may require non-stoquastic or QMC-obstructed regimes discussed in 2022_Hauke_NonStoquasticHamiltonians.
- The paper’s broader suggestion that QMC can predict QA performance is itself limited by small-system, synthetic-model evidence and absence of physical annealer experiments, creating a scalability contradiction between theoretical generalization and empirical scope.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
