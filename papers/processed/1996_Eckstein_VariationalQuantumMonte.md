---
aliases:
- Variational quantum Monte Carlo ground state of GaAs
- Variational quantum Monte Carlo
authors:
- H. Eckstein
- W. Schattke
- M. Reigrotzki
- R. Redmer
auto_detected: true
classification: ''
contradiction_flags: []
doi: ''
evidence_type: ''
idea_tags: []
journal_or_venue: arXiv:mtrl-th/9607009
methodology_tags: []
paper_type: ''
quantum_advantage_claim: not-applicable
related_papers: []
relevance_phase1: low
relevance_phase3: low
source_type: preprint
source_type_confidence: high
step1_date: '2026-03-25T15:50:02.222895'
step1_model: gpt-5.1
step2_date: '2026-03-25T15:50:05.595237'
step2_model: gpt-5.1
step3_date: '2026-03-25T15:50:40.923023'
step3_model: gpt-5.4
step4_date: '2026-03-25T15:51:07.022759'
step4_model: gpt-5.4
step5_date: '2026-03-25T15:51:43.436950'
step5_model: gpt-5.4
step6_date: '2026-03-25T15:51:49.526442'
step6_model: gpt-5.4
steps_completed:
- 1
- 2
- 3
- 4
- 5
- 6
tags: []
title: Variational quantum Monte Carlo ground state of GaAs
topic_tags: []
year: 1996
zotero_key: ''
---

## Abstract summary
The paper applies variational quantum Monte Carlo methods to bulk GaAs to compute ground-state properties such as total energy, lattice constant, bulk modulus, and related quantities. The authors use pseudopotentials and a Jastrow-Slater wavefunction, compare their results with experiment and density functional calculations, and assess statistical accuracy and correlation effects. They argue that the method yields competitive accuracy for ground-state properties and provides an ab initio benchmark for density functional approaches.
## Methodology
This preprint is an empirical computational physics study that applies variational quantum Monte Carlo (VQMC) to estimate ground-state properties of bulk GaAs. The authors simulate a finite periodic supercell of the crystal with valence electrons only, using periodic boundary conditions and a Hamiltonian composed of kinetic, Coulomb, and local/nonlocal pseudopotential terms. Inner-shell electrons are replaced by generalized norm-conserving ab initio nonlocal pseudopotentials, and Coulomb interactions are evaluated with Ewald summation. The trial many-body wavefunction is a Slater-Jastrow ansatz consisting of separate spin-up and spin-down Slater determinants built from parametrized hybrid bond orbitals plus a Jastrow correlation factor with a cusp-condition-constrained parameterization. Expectation values are estimated by Monte Carlo sampling of |psi|^2, and wavefunction parameter optimization is performed by sampling several hundred parameter sets from a multidimensional Gaussian around a guessed minimum, fitting the resulting total energies with inverse-error weighting to a multidimensional quadratic surface, and then refining along the fitted minimum line with more simulation points. Convergence with system size is checked using 4- and 32-unit-cell supercells, though only the larger 32-unit-cell system with 256 electrons is reported in detail. The study also performs atomic calculations for Ga and As reference energies and Hartree-Fock calculations to extract correlation energies. Outputs include total energy versus lattice constant, equilibrium lattice constant, bulk modulus, cohesive energy, correlation energy, and charge distribution measures, with comparisons against experiment and density functional calculations (LDA and Becke-Perdew gradient-corrected results).

**Algorithms used:** Variational Quantum Monte Carlo, Hartree-Fock, Ewald summation, Sherman-Morrison-Woodbury formula

**Experimental setup:** Classical variational quantum Monte Carlo simulations of bulk GaAs using finite supercells with periodic boundary conditions. Systems of 4 and 32 GaAs unit cells were sampled for convergence testing; detailed results are reported for the 32-unit-cell system containing 256 valence electrons. The Hamiltonian includes kinetic, Coulomb, and local/nonlocal pseudopotential terms. Nonlocal pseudopotential angular integration is approximated on a four-point spherical grid exact for l <= 2.

**Dataset:** No external dataset was used. Inputs are ab initio model-based simulations of bulk GaAs and isolated Ga and As atoms, with calculations performed across different lattice constants to determine equilibrium properties.
## Experiment details
### Input
Simulated physical system: bulk GaAs semiconductor in zinc-blende structure. Supercells of 4 and 32 unit cells were used for convergence checks; the main reported system is 32 unit cells with 256 valence electrons. Additional atomic simulations were performed for isolated Ga and As to obtain reference binding energies. Inputs include lattice constant values scanned around equilibrium, generalized norm-conserving ab initio pseudopotentials for Ga and As, and a parametrized Slater-Jastrow trial wavefunction with hybrid bond orbitals.

### Process
1. Define the periodic supercell Hamiltonian with kinetic, Coulomb, and local/nonlocal pseudopotential contributions. 2. Represent the many-body trial state as spin-up and spin-down Slater determinants multiplied by a Jastrow factor u(r)=A/r(1-exp(-r/F)), with F fixed by the cusp condition and orbital parameters beta, gamma, and zeta treated variationally. 3. Build Slater determinants from parametrized hybrid bond orbitals centered on As and Ga sites. 4. Sample expectation values by Monte Carlo using p=|psi|^2 and local estimators (B psi)/psi. 5. Evaluate Coulomb terms with Ewald summation and nonlocal pseudopotential projections using a four-point angular grid. 6. Update determinant ratios and related quantities numerically using the Sherman-Morrison-Woodbury formula. 7. Optimize wavefunction parameters by drawing several hundred parameter sets from a multidimensional Gaussian around an initial guessed minimum, computing total energies, and fitting them with reciprocal-error weighting to a multidimensional quadratic function. 8. If the fitted minimum lies within the sampled region, select a few parameter sets along the fitted minimum line and rerun them with increased numbers of simulation points for unbiased refinement. 9. Repeat calculations for different lattice constants to obtain the energy-volume curve, then fit a quadratic curve to determine equilibrium lattice constant and bulk modulus. 10. Perform Hartree-Fock calculations and compare with Jastrow-Slater results to estimate correlation energies; perform atomic calculations for Ga and As to derive cohesive quantities.

### Output
Reported outputs include total ground-state energy per unit cell, kinetic and potential energy components, correlation energy, cohesive energy, equilibrium lattice constant, bulk modulus, atomic total energies, ionization potentials, and charge partitioning over Voronoi polyhedra. Results are presented with statistical error bars from Monte Carlo sampling. Main comparisons are against experimental values and classical density functional theory baselines, specifically LDA and Becke-Perdew gradient-corrected calculations.

### Parameters
- unit_cells_tested: [4, 32]
- main_system_electrons: 256
- main_system_unit_cells: 32
- trial_wavefunction: Slater-Jastrow
- jastrow_form: u(r)=A/r(1-exp(-r/F))
- jastrow_parameters: {'A': 'variational', 'F': 'fixed by cusp condition'}
- orbital_parameters: ['beta', 'gamma_As', 'gamma_Ga', 'zeta_As_s', 'zeta_As_p', 'zeta_Ga_s', 'zeta_Ga_p']
- pseudopotential_type: generalized norm-conserving ab initio nonlocal pseudopotential
- nonlocal_integration_grid_points: 4
- optimization_strategy: multidimensional Gaussian sampling of several hundred parameter sets followed by weighted quadratic fit and refinement along minimum line

### Hardware
{'hardware_type': 'classical computation', 'quantum_hardware': 'none', 'simulator': 'Monte Carlo simulation on unspecified classical computing environment'}

### Reproducibility
Preprint. No code, software package, or computational environment details are provided. The methodological description is substantial and includes the wavefunction form, Hamiltonian terms, optimization strategy, and system sizes, but key implementation details such as exact Monte Carlo move scheme, number of samples, equilibration length, random-walk settings, and scanned lattice-constant grid are omitted, so full replication would be difficult.
## Findings
- [supported] Variational quantum Monte Carlo (VQMC) was applied to bulk GaAs using a 256-valence-electron supercell with nonlocal pseudopotentials and produced ground-state properties in satisfactory agreement with experiment.
- [supported] The calculated GaAs total energy per unit cell was -233.43 ± 0.09 eV, compared with an experimental reference of -233.04 ± 0.08 eV.
- [supported] The calculated GaAs lattice constant was 10.69 ± 0.1 a.u., in very close agreement with the experimental value of 10.6830 a.u.
- [supported] The calculated GaAs bulk modulus was 786 ± 100 kbar, somewhat higher than the experimental value of 756 kbar.
- [supported] The calculated cohesive energy of GaAs was -6.67 ± 0.09 eV per unit cell versus an experimental value of -4.9 ± 0.2 eV, with the authors attributing the discrepancy mainly to pseudopotential deficiencies in the atomic reference calculations.
- [supported] The correlation energy for GaAs near the ground-state density was estimated as -6.42 ± 0.2 eV per unit cell and showed no statistically significant dependence on lattice constant over the simulated range.
- [supported] A linear regression of the correlation energy versus density gave a slope of 0.9 ± 0.9 eV per rs, indicating no statistically significant trend.
- [supported] Atomic VQMC calculations yielded total energies of -58.000 ± 0.003 eV for Ga and -170.134 ± 0.007 eV for As, both lower than the experimental valence-electron reference energies.
- [supported] The first ionization potentials from the atomic calculations were 6.10 ± 0.02 eV for Ga and 10.38 ± 0.02 eV for As, compared with experimental values of 5.999 eV and 9.81 eV, respectively.
- [supported] Charge analysis based on Voronoi polyhedra suggested partial positive charge on both Ga and As sites and electron density extending into interstitial regions, with an additional bond charge accumulation of about 0.13 electron per occupied Ga-As bond.
- [speculative] The authors argue that VQMC is competitive with contemporary density functional methods for absolute ground-state quantities in simple solids.
- [speculative] The authors suggest that QMC calculations on simple systems could help assess and improve density-functional approximations.

**Results summary:** This preprint reports variational quantum Monte Carlo calculations for bulk GaAs using a 256-electron supercell and nonlocal pseudopotentials. The main reported results are a total energy of -233.43 ± 0.09 eV per unit cell, a lattice constant of 10.69 ± 0.1 a.u., and a bulk modulus of 786 ± 100 kbar. The total energy and lattice constant agree closely with experiment, while the bulk modulus is somewhat overestimated. The cohesive energy is more discrepant, which the authors attribute to errors in the pseudopotential-based atomic reference energies. Additional atomic calculations for Ga and As and a charge-partition analysis are presented. Overall, the paper provides empirical simulation evidence that VQMC can reproduce key ground-state properties of GaAs with accuracy comparable to strong density-functional calculations, but it makes no claim about quantum-computing-based speedup or advantage.

**Performance claims:**
- GaAs total energy: -233.43 ± 0.09 eV per unit cell vs experimental -233.04 ± 0.08 eV
- GaAs cohesive energy: -6.67 ± 0.09 eV per unit cell vs experimental -4.9 ± 0.2 eV
- GaAs lattice constant: 10.69 ± 0.1 a.u. vs experimental 10.6830 a.u.
- GaAs bulk modulus: 786 ± 100 kbar vs experimental 756 kbar
- Ga atomic total energy: -58.000 ± 0.003 eV vs experimental -57.21 eV
- As atomic total energy: -170.134 ± 0.007 eV vs experimental -169.554 eV
- Ga first ionization potential: 6.10 ± 0.02 eV vs experimental 5.999 eV
- As first ionization potential: 10.38 ± 0.02 eV vs experimental 9.81 eV
- GaAs correlation energy: -6.42 ± 0.2 eV per unit cell
- Correlation-energy slope vs rs: 0.9 ± 0.9 eV per rs
- Additional bond charge accumulation: 0.13 electron per occupied Ga-As bond
## Quantum advantage claim
**Classification:** not-applicable

The paper is about variational quantum Monte Carlo in computational condensed-matter physics, not quantum computing. It reports classical Monte Carlo simulation results and makes no quantum-computing advantage claim.
## Limitations
- Use of nonlocal pseudopotentials and the frozen-core approximation introduces uncertainty; the authors note that differences between calculated and experimental atomic energies/ionization potentials likely indicate pseudopotential error.
- Only valence electrons are simulated, so core-electron effects are not treated explicitly.
- Finite-size simulation of the solid is used; convergence was only tested with 4 and 32 unit cells, and reported results are for the larger finite system with 256 electrons.
- Periodic boundary conditions and supercell modeling may introduce finite-size and boundary-condition artifacts.
- The nonlocal pseudopotential projection integral is approximated by a four-point spherical grid that is exact only for angular momenta l <= 2.
- The bulk modulus is obtained slightly too high; the authors attribute this to the minimization procedure treating lattice constants farther from the minimum less accurately.
- The parameter optimization relies on a multidimensional quadratic fit and a straight minimum line in parameter space, which the authors acknowledge can yield nonminimum parameters far from the global minimum.
- Hartree-Fock minimization was more difficult because the Coulomb cusp leads to larger variance in the total energy.
- The lattice constant has a larger statistical uncertainty than the total energy, and the reported error is only an upper bound estimated from the fit.
- Cohesive energy is less accurate because atomic total energies for As and Ga are underestimated due to pseudopotential deficiencies in the atomic calculation.
- [inferred] The study is limited to a single material system (bulk GaAs), restricting generalizability to other semiconductors or financial/optimization contexts.
- [inferred] No systematic benchmark against alternative many-body methods beyond selected DFT comparisons is provided.
- [inferred] No detailed reproducibility information is given on random seeds, sampling length, computational cost, or implementation details sufficient for exact replication.
- [inferred] The work is a preprint and has not undergone peer review, so claims and methodology have not been independently validated through formal review.
- [inferred] The variational ansatz is relatively restricted (Slater-Jastrow with parametrized hybrid bonds), which may limit achievable accuracy compared with more flexible wave-function forms.
- [inferred] Statistical uncertainties are reported, but systematic errors from finite-size effects, pseudopotential choice, and ansatz bias are not comprehensively quantified.
## Open questions
- How large are the remaining finite-size errors after moving from 4 to 32 unit cells?
- To what extent do pseudopotential and frozen-core approximations affect the accuracy of cohesive energies and other derived properties?
- Would a more flexible variational wave function improve the bulk modulus and cohesive energy predictions?
- How robust is the optimization strategy based on quadratic fitting in higher-dimensional parameter spaces and for more complex solids?
- How well does the method scale to more complicated materials than GaAs, where DFT is commonly applied?
- What is the quantitative dependence of correlation energy on lattice constant or electron density beyond the statistically inconclusive trend reported here?
- [inferred] How would results compare with all-electron calculations or with different pseudopotential constructions?
- [inferred] Can the method deliver consistently superior accuracy to state-of-the-art DFT across a broader benchmark set of solids?

**Future work:**
- Use QMC calculations on simple solids to help select and adjust suitable density functionals for DFT.
- Apply the variational quantum Monte Carlo approach to more complicated solids beyond GaAs.
- Improve pseudopotential quality, especially for atomic reference calculations, to reduce errors in cohesive energies.
- Develop better minimization/optimization procedures that more accurately treat lattice constants away from the immediate vicinity of the minimum.
- [inferred] Perform more systematic finite-size scaling with larger supercells to quantify and reduce residual size effects.
- [inferred] Explore richer trial wave functions or improved Jastrow/orbital parametrizations to reduce variational bias.
- [inferred] Validate results with broader comparisons against other many-body electronic-structure methods and additional experimental observables.
- [inferred] Provide more detailed reproducibility information and independent validation, especially given the preprint status.
## Key ideas
- #contradiction:classical-vs-quantum — Despite the term 'variational quantum Monte Carlo,' the paper is a classical computational physics study on bulk GaAs and not a quantum computing paper relevant to finance
- #contradiction:classical-vs-quantum — The study makes no quantum advantage claim and uses no quantum hardware or quantum algorithms from the review taxonomy
## Contradictions
- The paper's terminology could be confused with quantum computing, but the extracted content explicitly states it is classical variational quantum Monte Carlo in condensed-matter physics, contradicting any interpretation that it provides evidence for quantum-computing superiority in finance-relevant tasks.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
