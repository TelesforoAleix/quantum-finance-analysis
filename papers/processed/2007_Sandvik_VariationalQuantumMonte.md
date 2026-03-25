---
aliases:
- Variational quantum Monte Carlo simulations with tensor-network states
- Variational quantum Monte Carlo
authors:
- A. W. Sandvik
- G. Vidal
auto_detected: true
classification: ''
contradiction_flags:
- contradiction:classical-vs-quantum
doi: ''
evidence_type: ''
idea_tags: []
journal_or_venue: arXiv
methodology_tags:
- variational
- classical-simulation
paper_type: ''
quantum_advantage_claim: not-applicable
related_papers: []
relevance_phase1: low
relevance_phase3: low
source_type: preprint
source_type_confidence: high
step1_date: '2026-03-25T15:50:01.379779'
step1_model: gpt-5.1
step2_date: '2026-03-25T15:50:08.108635'
step2_model: gpt-5.1
step3_date: '2026-03-25T15:50:45.587770'
step3_model: gpt-5.4
step4_date: '2026-03-25T15:51:14.874217'
step4_model: gpt-5.4
step5_date: '2026-03-25T15:51:37.360809'
step5_model: gpt-5.4
step6_date: '2026-03-25T15:51:44.452013'
step6_model: gpt-5.4
steps_completed:
- 1
- 2
- 3
- 4
- 5
- 6
tags:
- method/variational
- method/classical-simulation
- contradiction/classical-vs-quantum
title: Variational quantum Monte Carlo simulations with tensor-network states
topic_tags: []
year: 2007
zotero_key: ''
---

## Abstract summary
The paper introduces a variational quantum Monte Carlo scheme that uses tensor-network states, specifically matrix product states, as the variational ansatz. The authors develop a stochastic optimization method to handle the large number of tensor parameters and demonstrate the approach on the critical transverse-field Ising chain with periodic boundary conditions. They show that this combination significantly reduces the computational scaling in the bond dimension compared to standard MPS/DMRG methods, while still allowing systematic improvement of ground-state properties by increasing the tensor dimension.
## Methodology
This preprint presents an empirical computational physics study proposing a variational quantum Monte Carlo (VQMC) method based on tensor-network states, specifically matrix product states (MPS), and evaluates it on the critical transverse-field Ising chain. The authors formulate the MPS wavefunction for a periodic, translationally invariant spin chain, sample spin configurations according to the squared wavefunction amplitude using Metropolis single-spin-flip updates, and estimate both the energy and its first derivatives with respect to MPS matrix elements from Monte Carlo averages. They then optimize the MPS parameters using a stochastic sign-based update rule with random bounded step sizes and a cooling schedule in which the maximum update size decays geometrically while the number of Monte Carlo sweeps and bins increases over optimization stages. Symmetry constraints are incorporated by using real symmetric matrices, enforcing equal eigenvalue spectra for the two spin-sector matrices after each update, and normalizing matrix elements. The method is benchmarked against the exact solution of the transverse Ising chain at criticality for system sizes up to 256 spins and bond dimensions up to 48, with results reported for energy and squared magnetization as functions of bond dimension and system size. As a preprint, it should be flagged as non-peer-reviewed.

**Algorithms used:** Variational Quantum Monte Carlo, Matrix Product States, Metropolis Monte Carlo, Stochastic optimization

**Experimental setup:** Numerical simulations of the transverse-field Ising chain at the critical point h = 1 were carried out using a variational quantum Monte Carlo scheme with matrix product state ansatzes under periodic boundary conditions. System sizes ranged up to N = 256 spins, and D x D MPS matrices were used with bond dimension D up to 48. The computational scaling of the proposed method is stated as O(ND^3). No quantum hardware or quantum software platform was used; this is a classical numerical simulation study.

**Dataset:** Synthetic/model data generated from the one-dimensional transverse-field Ising chain Hamiltonian at criticality (h = 1), with exact analytical results used as reference benchmarks.
## Experiment details
### Input
Input consists of the transverse-field Ising chain Hamiltonian H = -sum_i (sigma^z_i sigma^z_{i+1} + h sigma^x_i) at critical field h = 1, with periodic boundary conditions. Simulations were performed for chain lengths N = 16, 32, 64, 128, and 256. The variational ansatz used translationally invariant MPS with two real symmetric D x D matrices A(+1) and A(-1), with bond dimensions up to D = 48. Initial matrices were either random or seeded from converged runs at smaller D or smaller N. No external dataset was used.

### Process
1. Define a translationally invariant periodic-boundary MPS wavefunction with real symmetric matrices A(+1) and A(-1). 2. For a given spin configuration S, compute the wavefunction coefficient W(S) as the trace of the product of local matrices. 3. Sample spin configurations with probability proportional to W(S)^2 using sequential single-spin-flip Metropolis updates. 4. During sweeps, use stored left/right partial matrix products to efficiently evaluate acceptance ratios, diagonal observables, off-diagonal energy contributions, and derivatives of the energy with respect to matrix elements. 5. Aggregate Monte Carlo estimates over F spin-flip sweeps to form one simulation bin. 6. After each bin, update each independent matrix element using a stochastic sign-based rule a_ij^s <- a_ij^s - delta(k) * r_ij^s * sign(dE/da_ij^s), where r_ij^s is uniform in [0,1). 7. Decrease the maximum step size according to a cooling schedule delta(k) = delta0 * Q^k, typically with Q = 0.9-0.95; alternative power-law cooling is also discussed. 8. Increase the number of sweeps per bin and number of bins linearly with optimization stage k, using F = F0 k and G = G0 k. 9. After each parameter update, diagonalize A(+1) and A(-1), average their eigenvalues to enforce equal spectra, transform back, and normalize matrices so the largest absolute element equals 1. 10. Repeat until the energy stabilizes; practical optimization was sometimes improved by restarting from previously converged smaller-D or smaller-N solutions or by using multiple runs with decreasing initial step sizes. 11. Compare final variational energies and squared magnetizations against exact solutions.

### Output
Outputs include energy per site E/N, squared magnetization M^2, relative error in energy, relative error in squared magnetization, convergence trajectories versus optimization step k, and comparisons against exact analytical results for the critical transverse Ising chain. Statistical error bars are reported for magnetization and noted to be at most about 1e-8 in energy for the largest runs. Baseline comparison is the exact solution rather than another numerical heuristic.

### Parameters
- system_sizes: [16, 32, 64, 128, 256]
- bond_dimensions_max: 48
- boundary_conditions: periodic
- field_strength_h: 1
- cooling_schedule: delta(k) = delta0 * Q^k
- typical_Q: 0.9-0.95
- alternative_cooling_schedule: delta(k) = delta0 * k^-alpha, alpha in [1/2, 1]
- bin_sweeps_schedule: F = F0 * k
- bins_schedule: G = G0 * k
- example_parameters_fig1: {'D': 8, 'N': 16, 'delta0': 0.05, 'Q': 0.9, 'G0': 10, 'F0': 100}
- example_restart_parameters_fig1_inset: {'delta0': 0.005, 'G0': 5, 'F0': 50}
- largest_D_by_N_table: {'16': 12, '32': 16, '64': 20, '128': 32, '256': 48}

### Hardware
{'hardware_type': 'classical numerical simulation', 'simulator_or_qpu': 'not applicable', 'platform': 'not specified'}

### Reproducibility
Preprint with substantial methodological detail, including equations for the estimator, derivatives, Metropolis sampling, and optimization schedule, plus several concrete hyperparameter examples. No code or repository is mentioned. Data are not needed beyond the model Hamiltonian and exact benchmark values. Replication appears feasible in principle for an expert, though some implementation details and stopping criteria are not fully standardized.
## Findings
- [supported] The paper demonstrates that tensor-network states, specifically matrix product states (MPS), can be used as variational ansatzes within a quantum Monte Carlo framework using stochastic optimization.
- [supported] For the critical transverse-field Ising chain with periodic boundary conditions, the proposed variational QMC-MPS method was applied to systems up to N = 256 spins with bond dimension D up to 48.
- [supported] The formal computational cost of the proposed MPS sampling scheme scales as N D^3 for periodic chains, compared with N D^5 for standard periodic-boundary MPS approaches and N D^6 for DMRG as stated by the authors.
- [supported] Numerical results for the critical transverse Ising chain show energies extremely close to exact values, with reported energy discrepancies as small as about 2.2e-7 per site for N = 256, indicating high variational accuracy.
- [supported] The squared magnetization also approaches exact results, though more slowly than the energy, and the authors report behavior consistent with requiring D to grow as a power of system size, roughly D ~ N^alpha with alpha in the range 0.5 to 1, to maintain fixed relative accuracy.
- [supported] Statistical errors in the reported energies are very small, at most about 1e-8 in the last digit shown, while residual discrepancies beyond statistical error are attributed by the authors to incomplete optimization rather than finite-D limitations.
- [supported] Using non-symmetric matrices with explicit symmetrization over reflected and spin-inverted configurations yields lower variational energy than the symmetric-matrix construction at the same D, but increases computational effort by about a factor of 4 and slows convergence somewhat.
- [speculative] The authors argue that similar reductions in scaling with tensor dimension should be possible for higher-dimensional tensor networks such as PEPS, but this is not empirically demonstrated in the paper.
- [speculative] The method is presented as a sign-problem-free and systematically refinable many-body approach through increasing tensor dimension D, but practical optimization difficulty for much larger D is acknowledged.

**Results summary:** This preprint introduces a variational quantum Monte Carlo method using tensor-network states, focusing on matrix product states for the critical transverse-field Ising chain with periodic boundary conditions. The authors combine Monte Carlo sampling over spin configurations with a stochastic optimization procedure based on first derivatives of the energy. In simulations up to 256 spins and bond dimension 48, the method reproduces exact benchmark energies and magnetizations with high accuracy. The main technical claim is a formal reduction in computational scaling for periodic MPS calculations from N D^5 to N D^3. The empirical evidence is entirely classical numerical simulation on a known spin model, not quantum hardware, and any broader scaling advantages for higher-dimensional tensor networks remain theoretical.

**Performance claims:**
- Simulations performed for system sizes up to N = 256 spins at criticality
- Bond dimensions up to D = 48
- Formal computational scaling of proposed periodic-chain MPS scheme: N D^3
- Authors state standard periodic MPS scaling as N D^5
- Authors state DMRG scaling for periodic systems as N D^6
- For PEPS, authors speculate scaling could be reduced from about D^12 to about D^6 via sampling
- N=16, D=12: E/N = -1.27528715 vs exact -1.27528715; M^2 = 0.52233(2) vs exact 0.522332
- N=32, D=16: E/N = -1.27375097 vs exact -1.27375102; M^2 = 0.44076(5) vs exact 0.440795
- N=64, D=20: E/N = -1.27336736 vs exact -1.27336739; M^2 = 0.37151(9) vs exact 0.371455
- N=128, D=32: E/N = -1.27327145 vs exact -1.27327150; M^2 = 0.3126(1) vs exact 0.312752
- N=256, D=48: E/N = -1.27324731 vs exact -1.27324753; M^2 = 0.2630(2) vs exact 0.263192
- Reported statistical errors of energies are at most about ±2 in the last digit shown (~1e-8)
- To maintain fixed relative accuracy in squared magnetization, authors estimate D scales roughly as N^alpha with alpha approximately 0.5 to 1
- Using non-symmetric matrices with explicit symmetrization increases computational effort by a factor of 4
## Quantum advantage claim
**Classification:** not-applicable

This paper is about classical variational quantum Monte Carlo and tensor-network simulation methods in condensed matter physics, not quantum computing for financial services. It does not claim quantum computational advantage.
## Limitations
- The method is demonstrated only for the one-dimensional transverse-field Ising chain at the critical point, so validation is limited to a simple benchmark problem.
- The largest matrix dimension studied is D = 48, and the authors state that stochastic optimization will be difficult in practice for D much larger than this.
- For observables tied to long-distance physics, such as squared magnetization, achieving a fixed relative accuracy appears to require D to grow with system size as D ~ N^alpha, with alpha roughly 0.5-1, limiting scalability.
- For N > 16, remaining discrepancies beyond statistical errors are attributed by the authors to incomplete optimization rather than finite-D effects.
- The authors do not claim the cooling/optimization protocol is optimal, indicating possible inefficiency and sensitivity to hyperparameter choices.
- There may be additional non-obvious D-dependent convergence costs in the sampling and optimization schemes beyond the formal computational scaling.
- Using general non-symmetric matrices improves energy but increases computational effort by a factor of 4 and leads to slightly slower optimization convergence.
- Although the framework is said to be applicable to more generic tensor networks such as PEPS, the paper does not provide empirical demonstrations beyond MPS.
- The paper discusses potential scaling reductions for higher-dimensional tensor networks only formally; no numerical results are given for two-dimensional or higher-dimensional systems.
- [inferred] No comparison is provided against strong classical baselines beyond exact solutions and qualitative discussion of standard MPS/DMRG scaling, so practical advantage over existing optimized classical methods is not fully established.
- [inferred] Results are limited to a sign-problem-free model, leaving performance on harder frustrated or fermionic systems unresolved.
- [inferred] The approach relies on several symmetry assumptions or symmetry-enforcing procedures (real symmetric matrices, eigenvalue matching, explicit symmetrization), which may reduce generality for broader classes of systems.
- [inferred] As a preprint, the work lacks peer-review validation.
## Open questions
- How well does the variational QMC tensor-network approach perform for PEPS and other tensor networks in higher dimensions in practice, not just in formal scaling arguments?
- Can the stochastic optimization scheme be made reliable and efficient for matrix/tensor dimensions substantially larger than D = 48?
- What is the true D-dependence of convergence and optimization difficulty beyond the formal ND^3 cost?
- How does the method perform on more challenging systems, such as frustrated spin models or fermionic models that are difficult for conventional QMC?
- What is the best cooling schedule or stochastic optimization protocol for this class of tensor-network variational Monte Carlo problems?
- To what extent are the residual errors for larger N caused by optimization failure versus representational limitations of finite D?
- How does the method compare quantitatively with state-of-the-art deterministic MPS/DMRG implementations in runtime and accuracy for periodic systems?
- Can the need for D growing with system size for long-range observables be reduced through improved ansatz design or optimization?

**Future work:**
- Improve the cooling and stochastic optimization protocol to obtain better efficiency and convergence.
- Extend the approach from MPS to more generic tensor networks, especially PEPS.
- Investigate practical applications in higher-dimensional systems where reduced formal D-scaling could be especially valuable.
- Test the method on more difficult many-body problems, including systems with frustration or fermionic degrees of freedom.
- Study convergence properties and hidden D-dependent costs of sampling and optimization more systematically.
- Develop strategies to handle larger tensor dimensions beyond those explored in the paper.
- Explore alternative tensor parameterizations, including non-symmetric matrices or other symmetry treatments, to improve variational accuracy.
- [inferred] Benchmark against stronger classical tensor-network and variational methods to assess practical computational advantage.
- [inferred] Provide broader empirical validation on additional models and observables beyond the critical transverse Ising chain.
## Key ideas
- #contradiction:classical-vs-quantum — The paper studies a classical variational quantum Monte Carlo method with tensor-network states, not quantum computing for finance or quantum speedup
- #limitation:simulation-only — All results come from classical numerical simulation of the transverse-field Ising chain; no QPU, quantum software stack, or financial dataset is involved
- #contradiction:scalability — Although the paper reports improved formal scaling for periodic MPS calculations, empirical validation is limited to a benchmark spin model and modest bond dimensions, leaving broader scalability unresolved
## Contradictions
- The paper contradicts any interpretation of 'quantum advantage' because it explicitly presents a classical simulation method and states no quantum computational advantage claim.
- It also undercuts broad claims that improved formal scaling implies practical quantum relevance: the demonstrated gains are within classical tensor-network simulation on a condensed-matter benchmark, not on financial problems or quantum hardware.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
