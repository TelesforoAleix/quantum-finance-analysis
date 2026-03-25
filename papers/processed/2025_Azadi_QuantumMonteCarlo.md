---
aliases:
- Quantum Monte Carlo study of the quasiparticle effective mass of the two-dimensional
  uniform electron liquid
- Quantum Monte Carlo study
authors:
- S. Azadi
- N. D. Drummond
- A. Principi
- R. V. Belosludov
- M. S. Bahramy
auto_detected: true
classification: ''
contradiction_flags: []
doi: 10.1103/3wjg-y6qk
evidence_type: ''
idea_tags: []
journal_or_venue: Physical Review B
methodology_tags: []
paper_type: ''
quantum_advantage_claim: not-applicable
related_papers: []
relevance_phase1: low
relevance_phase3: low
source_type: peer-reviewed-empirical
source_type_confidence: high
step1_date: '2026-03-25T16:06:32.766919'
step1_model: gpt-5.1
step2_date: '2026-03-25T16:06:37.769777'
step2_model: gpt-5.1
step3_date: '2026-03-25T16:07:02.768632'
step3_model: gpt-5.4
step4_date: '2026-03-25T16:07:45.840239'
step4_model: gpt-5.4
step5_date: '2026-03-25T16:08:21.730101'
step5_model: gpt-5.4
step6_date: '2026-03-25T16:08:29.147909'
step6_model: gpt-5.4
steps_completed:
- 1
- 2
- 3
- 4
- 5
- 6
tags: []
title: Quantum Monte Carlo study of the quasiparticle effective mass of the two-dimensional
  uniform electron liquid
topic_tags: []
year: 2025
zotero_key: ''
---

## Abstract summary
The paper uses variational and diffusion quantum Monte Carlo methods to compute energy bands and quasiparticle effective masses in paramagnetic and ferromagnetic two-dimensional uniform electron liquids over a range of densities. The authors systematically analyze sources of numerical error, including finite-size effects, trial wave function quality, backflow correlations, fitting procedures, and DMC time-step choice, and extrapolate to the thermodynamic limit. The work aims to clarify discrepancies with GW-based many-body perturbation results and to characterize how effective mass renormalization depends on density and spin polarization in 2D electron liquids.
## Methodology
The study is an empirical computational physics investigation using real-space quantum Monte Carlo to estimate quasiparticle energy bands and effective masses of the two-dimensional uniform electron liquid (2D-UEL) for both paramagnetic and ferromagnetic spin polarizations. The authors apply variational Monte Carlo (VMC) and diffusion Monte Carlo (DMC) with Slater-Jastrow (SJ) and Slater-Jastrow-backflow (SJB) trial wave functions, optimized via variance minimization followed by linear least-squares energy minimization in the CASINO package. Effective masses are obtained from single-particle excitation energies computed by adding or removing an electron at momentum k, constructing energy bands over more than 20 momentum points in the range 0 < k < 1.7kF, and fitting the resulting bands with Padé and quartic functions to extract the derivative at the Fermi wave vector. The methodology explicitly studies finite-size effects by simulating multiple electron counts and extrapolating m*(N) to the thermodynamic limit using power-law fits, while also testing sensitivity to backflow, wave-function reoptimization at each k, fitting form, and DMC time step. Results are compared against free-electron and Hartree-Fock bands, prior VMC/DMC and GW-based literature, and selected experimental effective-mass measurements.

**Algorithms used:** VMC, DMC
**Frameworks:** CASINO

**Experimental setup:** Real-space quantum Monte Carlo simulations were performed in finite hexagonal simulation cells with periodic boundary conditions and Bloch vector ks set to zero. Both VMC and DMC were used with SJ and SJB trial wave functions. Simulations covered density parameters rs = 1, 2, 3, 4, 5, and 10. System sizes were N = 146, 218, and 302 electrons for paramagnetic systems and N = 91, 139, and 151 for ferromagnetic systems. Energy bands were sampled at more than 20 momentum vectors over 0 < k < 1.7kF. DMC time-step sensitivity was examined using dt = 0.05 and 0.2 a.u. with 2560 walkers and 25,000 steps in one reported comparison. Calculations were run on the MASAMUNE-IMR supercomputer system.

**Dataset:** No external financial or benchmark dataset was used. The study uses simulated many-body electron-liquid systems defined by physical parameters: 2D uniform electron liquid at density range 1 <= rs <= 10, with paramagnetic and ferromagnetic spin configurations and multiple finite electron counts.
## Experiment details
### Input
Input consists of synthetic/physics-simulation configurations of the two-dimensional uniform electron liquid. Paramagnetic cases used N = 146, 218, 302 electrons; ferromagnetic cases used N = 91, 139, 151 electrons. Density parameters were rs = 1, 2, 3, 4, 5, 10. Momentum-space excitations were evaluated at more than 20 k points in 0 < k < 1.7kF. Trial wave functions included Slater-Jastrow and Slater-Jastrow-backflow forms, with Jastrow terms built from polynomial and plane-wave expansions in electron-electron separation and backflow represented by a polynomial in electron-electron distance. No conventional data preprocessing is applicable beyond wave-function optimization and finite-size setup choices.

### Process
1. Construct SJ and SJB trial wave functions for the 2D-UEL in finite hexagonal cells under periodic boundary conditions. 2. Optimize variational parameters using variance minimization followed by linear least-squares energy minimization in CASINO. 3. Compute ground-state total energy E0 with VMC and DMC. 4. For each momentum k, compute occupied and unoccupied single-particle excitation energies by removing or adding an electron: epsilon-(k) = E0 - E-(k) and epsilon+(k) = E+(k) - E0, while keeping simulation-cell volume fixed using adjusted rs' definitions for N-1 and N+1 systems. 5. Sample more than 20 momentum vectors over 0 < k < 1.7kF to build the energy band epsilon(k). 6. Fit the band using both Padé and quartic least-squares functions and extract the effective mass from m* = kF (d epsilon / dk)^(-1) at kF. 7. Repeat across densities, spin polarizations, and system sizes to assess finite-size effects. 8. Extrapolate m*(N) to the thermodynamic limit using m*(N) = cN^(-alpha) + m*(infinity), testing alpha values 2.0, 1.5, 1.0, 0.5, and 0.25, with alpha = 1.5 adopted for main analysis. 9. Perform sensitivity analyses for backflow inclusion, wave-function reoptimization at each k, fitting function choice, and DMC time step.

### Output
Primary outputs are quasiparticle energy bands and effective mass ratios m* for paramagnetic and ferromagnetic 2D-UEL across densities and system sizes. Reported outputs include fitted band curves, thermodynamic-limit extrapolated m* values with error bars, and qualitative trends versus density. Baseline and comparison references include free-electron and Hartree-Fock bands, VMC versus DMC agreement, SJ versus SJB trial-wave-function results, Padé versus quartic fitting, different DMC time steps, prior VMC/DMC literature, GW-based theoretical results, and selected experimental effective-mass measurements. Error bars and finite-size extrapolation behavior are central evaluation criteria.

### Parameters
- density_parameters_rs: [1, 2, 3, 4, 5, 10]
- paramagnetic_electron_counts: [146, 218, 302]
- ferromagnetic_electron_counts: [91, 139, 151]
- momentum_range: 0 < k < 1.7 kF
- momentum_points: >20
- trial_wavefunctions: ['Slater-Jastrow', 'Slater-Jastrow-backflow']
- wavefunction_optimization: ['variance minimization', 'linear least-squares energy minimization']
- fitting_functions: ['Pade: (a0 + a1 k + a2 k^2 + a3 k^3)/(1 + 2 a3 k)', 'quartic: a0 + a2 k^2 + a4 k^4']
- finite_size_extrapolation_form: m*(N) = c N^(-alpha) + m*(infinity)
- finite_size_alpha_tested: [2.0, 1.5, 1.0, 0.5, 0.25]
- main_alpha_used: 1.5
- dmc_time_steps_reported: [0.05, 0.2]
- walkers_reported: 2560
- steps_reported: 25000
- bloch_vector_ks: 0

### Hardware
Simulations were performed on the MASAMUNE-IMR supercomputer system at the Center for Computational Materials Science, Institute for Materials Research. No quantum hardware or QPU was used; this is classical high-performance computing for QMC. The paper does not report simulator noise models or transpilation settings, as these are not applicable.

### Reproducibility
Data availability is explicitly stated: supporting data are openly available, though embargo periods may apply. A GitHub link is provided (https://github.com/arshamsam). The paper gives substantial methodological detail on wave functions, optimization, system sizes, densities, fitting procedures, and finite-size extrapolation, making replication plausible for researchers familiar with CASINO/QMC, though some implementation details may still rely on supplemental material and code/data access.
## Findings
- [supported] Using real-space VMC and DMC simulations, the paper finds that the effective mass of the paramagnetic 2D uniform electron liquid is very close to the bare mass at high density (rs = 1), with thermodynamic-limit estimates of 0.98(1) from VMC and 0.95(1) from DMC.
- [supported] For the paramagnetic 2D uniform electron liquid, the effective mass increases as rs increases over the studied density range 1 <= rs <= 10, with DMC thermodynamic-limit estimates of 0.95(1), 1.05(1), 1.06(1), 1.15(4), 1.10(3), and 1.25(5) for rs = 1, 2, 3, 4, 5, and 10 respectively (using the authors' preferred finite-size extrapolation exponent alpha = 1.5).
- [supported] For the ferromagnetic 2D uniform electron liquid, the effective mass decreases as density is reduced, with DMC thermodynamic-limit estimates of 0.87(1), 0.69(2), and 0.58(3) at rs = 1, 5, and 10 respectively (alpha = 1.5).
- [supported] VMC and DMC effective-mass estimates agree within error bars across the studied systems, indicating that well-optimized VMC can be a reliable lower-cost alternative to DMC for these excited-state calculations.
- [supported] Results are obtained from classical Monte Carlo simulation methods (VMC/DMC), not quantum-computing hardware or quantum algorithms.
- [supported] Backflow correlations in the trial wave function materially affect the inferred effective mass: for paramagnetic rs = 5, SJ-based VMC/DMC give m* < 1, whereas SJB-based VMC/DMC give m* > 1, implying that electron correlation treatment is crucial to the qualitative trend.
- [supported] Re-optimizing the wave function at each momentum k has negligible effect on DMC effective masses but slightly increases VMC effective masses.
- [supported] A quartic fit to the energy band gives slightly larger effective masses than a Padé fit and was judged to fit the data better.
- [supported] DMC time-step choice significantly affects extracted effective masses; the time-step error does not cancel in excitation-energy differences, and a smaller time step (0.05 a.u. vs 0.2 a.u. for rs = 5, N = 302) produced larger fitting uncertainty and a smaller m* with a larger error bar.
- [supported] Finite-size effects remain substantial and grow at lower density; extrapolated m* values at rs = 5 and 10 depend strongly on the assumed scaling exponent when alpha <= 0.5, so the thermodynamic-limit inference is sensitive to finite-size modeling.
- [speculative] The authors argue that the differing density dependence of m* in 2D versus 3D paramagnetic electron liquids is driven by competition between correlation and screening, with correlation enhancing m* in 2D while screening suppresses m* in 3D.
- [speculative] The paper notes that it remains an open question whether the finite-size QMC excitation methodology used away from the Fermi surface maps exactly onto true quasiparticle energies in the thermodynamic limit.

**Results summary:** This peer-reviewed empirical study uses classical variational and diffusion quantum Monte Carlo simulations to compute quasiparticle energy bands and effective masses for paramagnetic and ferromagnetic two-dimensional uniform electron liquids over 1 <= rs <= 10, using multiple finite system sizes and extrapolation to the thermodynamic limit. The main result is that the paramagnetic effective mass is essentially unrenormalized at high density (about 1 at rs = 1) and increases with rs, while the ferromagnetic effective mass decreases strongly as density is reduced. VMC and DMC agree within uncertainties, but the extracted values are sensitive to wave-function form, finite-size extrapolation, fitting function, and DMC time step. In particular, including backflow correlations changes the qualitative conclusion for paramagnetic rs = 5 from m* < 1 to m* > 1. The work is entirely simulation-based and does not involve quantum computing methods or demonstrate any quantum advantage.

**Performance claims:**
- Paramagnetic thermodynamic-limit m* at rs = 1: VMC 0.98(1), DMC 0.95(1) (alpha = 1.5 extrapolation)
- Paramagnetic DMC thermodynamic-limit m* (alpha = 1.5): rs = 1 -> 0.95(1), rs = 2 -> 1.05(1), rs = 3 -> 1.06(1), rs = 4 -> 1.15(4), rs = 5 -> 1.10(3), rs = 10 -> 1.25(5)
- Paramagnetic VMC thermodynamic-limit m* (alpha = 1.5): rs = 1 -> 0.98(1), rs = 2 -> 1.06(1), rs = 3 -> 1.12(1), rs = 4 -> 1.20(2), rs = 5 -> 1.22(3), rs = 10 -> 1.32(4)
- Ferromagnetic DMC thermodynamic-limit m* (alpha = 1.5): rs = 1 -> 0.87(1), rs = 5 -> 0.69(2), rs = 10 -> 0.58(3)
- Ferromagnetic VMC thermodynamic-limit m* (alpha = 1.5): rs = 1 -> 0.87(1), rs = 5 -> 0.69(2), rs = 10 -> 0.59(3)
- System sizes used: paramagnetic N = 146, 218, 302; ferromagnetic N = 91, 139, 151
- Momentum sampling: more than 20 k-points over 0 < k < 1.7 kF
- DMC time-step comparison discussed for rs = 5, N = 302: dt = 0.05 vs 0.2 a.u. with 2560 walkers and 25,000 steps
## Quantum advantage claim
**Classification:** not-applicable

The paper studies many-body electron systems using classical VMC/DMC quantum Monte Carlo simulation methods in condensed-matter physics. It does not evaluate quantum computing for finance, does not use quantum hardware, and makes no quantum advantage claim.
## Limitations
- Finite-size errors remain a major limitation; the authors state that one of the main sources of controversy in effective-mass calculations arises from finite-size errors and extrapolation to the thermodynamic limit.
- Thermodynamic-limit extrapolation relies on only three system sizes for each case, so the authors note that a chi-squared analysis does not provide meaningful information about fit quality.
- The inferred thermodynamic-limit effective mass depends strongly on the assumed finite-size scaling exponent when alpha <= 0.5, indicating sensitivity of conclusions to extrapolation assumptions.
- There is currently no theoretical framework, independent of simulation-specific technical details, for systematically analyzing finite-size effects on excitations in QMC calculations.
- The DMC time step has a crucial effect on the calculated energy band and effective mass; the authors explicitly find that time-step errors do not cancel in excitation-energy differences.
- Residual pathological behavior near the Fermi surface persists because QMC does not fully eliminate the Hartree-Fock pathology, making extraction of derivatives at k_F difficult.
- Excitations in finite systems are computed away from the Fermi surface because near-k_F behavior is problematic, which limits direct access to the quantity of primary interest.
- The exact connection between the finite-size single-particle excitation energies computed here and true quasiparticle energies or bandwidth is explicitly stated to remain unresolved.
- Quasiparticles are not exact eigenstates, so mapping exact finite-system many-body eigenstates to quasiparticle resonances is not guaranteed, especially far from the Fermi surface.
- Comparison with experiment is only qualitative because experimental 2D electron systems have finite width and disorder, unlike the ideal 2D uniform electron liquid studied here.
- The study is restricted to the metallic density range 1 <= r_s <= 10, so behavior outside this range is not established.
- Ferromagnetic calculations use relatively few and uneven system sizes (N = 91, 139, 151), which may limit robustness of finite-size extrapolation. [inferred]
- Only a limited number of densities and more than 20 momentum points up to 1.7k_F were sampled, which may miss subtler structure in the dispersion. [inferred]
- Results depend on trial-wave-function quality and nodal-surface choice; although backflow improves agreement, fixed-node bias may still remain. [inferred]
- The claim that VMC can be a reliable alternative to DMC for excited states may not generalize broadly because it depends on having a very well-optimized trial wave function. [inferred]
- No direct benchmarking against alternative state-of-the-art many-body numerical methods on the same setups is presented beyond literature comparison, limiting internal cross-validation. [inferred]
- Although data are said to be openly available, reproducibility may still depend on detailed optimization settings, random seeds, and implementation choices not fully specified in the main text. [inferred]
## Open questions
- Whether the effective-mass ratio m*/m is greater than or less than one in the density range 1 <= r_s <= 10 remains an open question in the broader literature, especially regarding discrepancies between approaches.
- Can the QMC methodology used here for finite-size occupied/unoccupied single-particle energies away from the Fermi surface be exactly connected to the true definition of quasiparticle energies or bandwidth?
- How should exact finite-system many-body eigenstates be reinterpreted in terms of quasiparticle resonances, particularly for states far from the Fermi surface with finite lifetime in the thermodynamic limit?
- What is the correct and simulation-independent finite-size scaling form for excitation properties and effective mass in QMC calculations?
- Why do QMC-based and Green's-function-based approaches still disagree for the effective mass, and which methodological assumptions are responsible for the discrepancy?
- How much residual fixed-node bias remains even with backflow-improved trial wave functions? [inferred]
- Would higher-level correlated trial states, such as full configuration interaction-inspired forms, materially change the low-density paramagnetic effective-mass trend? [inferred]
- How robust are the conclusions to alternative extrapolation strategies, larger system sizes, and denser momentum sampling? [inferred]

**Future work:**
- Further investigation is needed to resolve discrepancies between the Landau-mapping/QMC approach and GW-based calculations.
- Develop a careful reinterpretation and further extension of approaches based on Landau's Fermi-liquid framework to clarify disagreement with Green's-function formalism.
- Establish a more rigorous connection between finite-size QMC excitation energies and true quasiparticle energies or bandwidths.
- Develop a theoretical framework for systematically analyzing finite-size effects on excitations in QMC, independent of simulation-specific technical details.
- Use larger system sizes and improved thermodynamic-limit extrapolation to reduce finite-size uncertainty. [implied]
- Explore more accurate correlated wave functions beyond Slater-Jastrow-backflow, potentially including full configuration interaction-inspired improvements, especially at low density. [implied]
- Perform more systematic DMC time-step studies or extrapolation to zero time step for excitation energies to control bias in effective-mass estimates. [implied]
- Investigate states closer to and farther from the Fermi surface with methods that explicitly account for quasiparticle lifetime broadening. [implied]
- Extend comparisons with experiment using more realistic models that include finite-width and disorder effects present in actual 2D electron systems. [implied]
## Key ideas
- #contradiction:classical-vs-quantum — The paper uses classical VMC/DMC many-body simulation in condensed-matter physics and is not about quantum computing in finance.
- #contradiction:classical-vs-quantum — It explicitly makes no quantum advantage claim and uses no quantum hardware, QPU, or finance-related quantum algorithm.
- #limitation:simulation-only — All results come from classical high-performance computing simulations in CASINO on a supercomputer, not from quantum devices.
## Contradictions
- This paper falls outside the SLR scope: despite the phrase 'quantum Monte Carlo,' it studies classical computational physics rather than quantum computing for financial services.
- Any interpretation of this paper as evidence for quantum advantage would contradict its own explicit statement that no quantum-computing method or advantage claim is involved.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
