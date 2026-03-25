---
aliases:
- Quantum Monte Carlo study of Doppler broadening of positron annihilation radiation
  in semiconductors and insulators
- Quantum Monte Carlo study
authors:
- K. A. Simula
- J. Härkönen
- I. Zhelezova
- N. D. Drummond
- F. Tuomisto
- I. Makkonen
auto_detected: true
classification: ''
contradiction_flags: []
doi: 10.1103/PhysRevB.108.045201
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
step1_date: '2026-03-25T16:01:52.264368'
step1_model: gpt-5.1
step2_date: '2026-03-25T16:01:59.574232'
step2_model: gpt-5.1
step3_date: '2026-03-25T16:02:28.429089'
step3_model: gpt-5.4
step4_date: '2026-03-25T16:02:50.671170'
step4_model: gpt-5.4
step5_date: '2026-03-25T16:03:17.767921'
step5_model: gpt-5.4
step6_date: '2026-03-25T16:03:23.428167'
step6_model: gpt-5.4
steps_completed:
- 1
- 2
- 3
- 4
- 5
- 6
tags: []
title: Quantum Monte Carlo study of Doppler broadening of positron annihilation radiation
  in semiconductors and insulators
topic_tags: []
year: 2023
zotero_key: ''
---

## Abstract summary
The paper develops and applies a variational quantum Monte Carlo approach to compute annihilating electron–positron pair momentum densities and corresponding Doppler-broadened 511 keV spectra in semiconductors and insulators. Using materials such as Si, C, and AlN, the authors analyze finite-size, vibrational, and wavefunction-form effects, and then benchmark simulated Doppler spectra against high-resolution experimental data. They show that relatively small cells and simple wavefunctions suffice for accurate Doppler predictions, and that this QMC treatment of electron–positron correlations improves agreement with experiment compared to standard DFT-based enhancement-factor models.
## Methodology
This peer-reviewed empirical study develops and benchmarks a variational quantum Monte Carlo (VMC) workflow for computing annihilating-pair momentum densities (APMDs) and Doppler broadening spectra in crystalline semiconductors and insulators. The authors simulate periodic electron-positron systems with a single thermalized positron using VMC as implemented in the CASINO code, employing Slater-Jastrow (SJ) and Slater-Jastrow-backflow (SJB) trial wave functions. Single-particle electronic orbitals are first generated from density functional theory (DFT) calculations in QUANTUM ESPRESSO with the PBE functional, while the positron orbital is obtained from the authors' own positron package. The Jastrow factor is optimized by variance minimization and the Jastrow plus backflow parameters by energy minimization. Twisted boundary conditions and twist averaging over regular grids in the irreducible Brillouin-zone wedge are used to reduce finite-size effects and improve momentum resolution. The APMD is sampled in VMC with the Metropolis algorithm and then projected into one-dimensional Doppler spectra using tetrahedral interpolation and linear projection. Core-electron contributions, not included in the valence-only VMC due to pseudopotentials, are added from separate DFT-based calculations using state-dependent and state-independent enhancement models. The methodology includes convergence studies with respect to simulation-cell size and wave-function complexity, a DFT-based assessment of lattice-vibration effects in Si, and final benchmarking of computed Doppler spectra for Si and AlN against high-resolution experimental coincidence Doppler broadening measurements and against conventional DFT-based models.

**Algorithms used:** Variational Quantum Monte Carlo, Metropolis algorithm, Variance minimization, Energy minimization, Twist averaging, Delaunay tetrahedralization, Linear interpolation
**Frameworks:** CASINO, QUANTUM ESPRESSO, VASP

**Experimental setup:** Computational study using VMC simulations of periodic solids with one positron under periodic and twisted boundary conditions. VMC calculations were run in CASINO with SJ and SJB wave functions. Electronic orbitals were generated in QUANTUM ESPRESSO using PBE; additional DFT benchmark and vibrational calculations used VASP with PAW, LDA/GGA, and electron-positron enhancement models. Simulations used 16-, 54-, and 72-atom cells depending on material, momentum cutoff pcut = 7 a.u., and twist grids of 4x4x4 for C/Si and 4x4x5 for AlN. Experimental validation used published 2D coincidence Doppler broadening measurements for Si and AlN with HPGe detector resolutions of 0.92 keV and 0.90 keV FWHM, respectively.

**Dataset:** Ab initio simulated crystalline materials: diamond-structure C and Si, and wurtzite AlN. Experimental benchmark data consisted of Doppler broadening spectra from reference Si and AlN samples producing predominantly delocalized-state annihilations. Additional DFT-based vibrational sampling was performed for bulk Si.
## Experiment details
### Input
Materials studied were C, Si, and AlN in pristine periodic lattices. Main benchmark comparisons focused on Si and AlN. Simulation cells included 16-atom FCC cells for C and Si, 16-atom hexagonal cells for AlN, with larger comparison cells of 54 atoms for C and 72 atoms for AlN; electron counts reported include 64/216 electrons for C and 64/288 electrons for AlN. Electronic orbitals were obtained from DFT (QUANTUM ESPRESSO, PBE), positron orbitals from an in-house positron package, and norm-conserving nonlocal Dirac-Fock AREP pseudopotentials were used so VMC covered valence electrons only. Core-electron spectra were added from DFT models. For vibrational analysis, a 64-atom Si cell was used, with phonon-mode-based atomic displacements sampled at 0 K and 300 K. Experimental references were a (100)-oriented Si substrate measured along [110] and an AlN sample measured perpendicular to the c-axis, modeled along [1-210].

### Process
1. Generate single-particle electron orbitals from DFT in QUANTUM ESPRESSO using the PBE functional and obtain the positron orbital from the authors' positron package. 2. Construct SJ and SJB trial wave functions in CASINO from Slater determinants of Kohn-Sham orbitals multiplied by Jastrow factors; include backflow transformations for SJB. 3. Optimize the Jastrow factor by variance minimization, then optimize Jastrow and backflow parameters by energy minimization; Jastrow optimization was performed at the Gamma-point twist. 4. Run VMC with periodic boundary conditions and twisted boundary conditions for electrons, using regular twist grids in the irreducible Brillouin-zone wedge; no twist was applied to the positron (k = 0). 5. Sample the APMD using the Metropolis algorithm and the estimator given in the paper, including permutation over opposite-spin electron indices to reduce standard error. 6. Restrict momentum-grid values to |p_i| < pcut, using pcut = 7 a.u. and checking convergence down to about 5 a.u. 7. Convert 3D APMDs to 1D Doppler projections by Delaunay tetrahedralization followed by linear interpolation. 8. Normalize computed Doppler spectra to unit area and convolve them with the experimental resolution function before comparison with measurements. 9. Add core-electron contributions from separate DFT calculations using state-dependent or state-independent enhancement models and relative core intensity mu. 10. Perform convergence tests by comparing small and larger simulation cells and SJ versus SJB wave functions. 11. Assess lattice-vibration effects in Si using DFT by sampling phonon-induced atomic displacements in a 64-atom cell at 0 K and 300 K and recomputing APMDs. 12. Compare final VMC spectra against experimental Doppler spectra and against DFT-based state-dependent and state-independent model calculations.

### Output
Outputs are 3D annihilating-pair momentum densities and 1D Doppler broadening spectra along specified crystallographic directions. Reported evaluation criteria include agreement with experiment across low- and high-momentum regions, visual discrepancy/error-to-experiment plots, statistical error bars from twist-to-twist variation, convergence with respect to simulation-cell size and wave-function form, and qualitative/quantitative comparison of vibrational effects. Baselines include conventional DFT-based Doppler spectra using state-dependent and state-independent enhancement models within LDA/GGA frameworks, as well as comparison between SJ and SJB VMC and between small and larger simulation cells. Experimental comparisons use measured coincidence Doppler spectra for Si and AlN after convolution with detector resolution.

### Parameters
- simulation_method: VMC
- wave_functions: ['SJ', 'SJB']
- simulation_cells: {'C': [16, 54], 'Si': [16], 'AlN': [16, 72], 'Si_vibrations': [64]}
- electron_counts_reported: {'C': [64, 216], 'AlN': [64, 288]}
- twist_grids: {'C': '4x4x4', 'Si': '4x4x4', 'AlN': '4x4x5'}
- momentum_cutoff_au: 7
- converged_momentum_cutoff_au: 5
- electron_orbital_functional: PBE
- dft_functionals_for_benchmarks: {'Si': 'LDA', 'C': 'GGA/PBE', 'AlN': 'GGA/PBE'}
- core_models: ['state-dependent', 'state-independent']
- vibrational_temperatures_K: [0, 300]
- experimental_resolution_fwhm_keV: {'Si': 0.92, 'AlN': 0.9}

### Hardware
{'computational_type': 'Classical HPC clusters', 'software_environment': ['CASINO', 'QUANTUM ESPRESSO', 'VASP'], 'clusters': ['Mahti', 'Lumi'], 'qpu': None, 'simulator': None}

### Reproducibility
No code repository or executable workflow is provided in the excerpt. The paper gives substantial methodological detail on wave functions, software, cell sizes, twist grids, optimization strategy, momentum cutoff, and comparison procedure, which supports partial replication by experts. Input structures and experimental references are identifiable, but some implementation details and full parameter files are not included, so reproducibility is moderate rather than complete.
## Findings
- [supported] The paper presents a variational quantum Monte Carlo (VMC) method for simulating annihilating-pair momentum densities and Doppler broadening spectra in semiconductors and insulators, validated on Si and AlN against experiment.
- [supported] VMC predictions for Doppler broadening in Si and AlN agree better with experimental reference spectra than the compared DFT-based state-dependent and state-independent models.
- [supported] Small simulation cells were sufficient for converged Doppler broadening calculations: 16-atom cells produced spectra within error bars of larger-cell calculations (54 atoms for C and 72 atoms for AlN).
- [supported] Backflow corrections were not necessary for accurate Doppler broadening calculations; Slater-Jastrow and Slater-Jastrow-backflow results agreed within statistical error bars.
- [supported] Lattice vibrations had negligible effect on Si Doppler spectra; the largest discrepancy versus static-lattice results was less than 1% around 0.5 a.u., and effects at 0 K and 300 K were similar.
- [supported] In Si, VMC matched experiment within statistical error bars in the low-momentum region, while DFT-based models showed visibly worse agreement and lay outside the VMC statistical error bars.
- [supported] In AlN, VMC showed excellent agreement with experiment across the reported spectrum, while both DFT-based models deviated from experiment and from VMC.
- [supported] The results support the claim that explicit modeling of electron-electron and electron-positron correlations improves agreement with positron-annihilation experiments relative to conventional DFT-based approximations.
- [supported] For Si, the state-dependent DFT model agreed better at low momentum but overestimated high-momentum intensity, while the state-independent model performed better at higher momenta.
- [supported] For AlN, the state-independent core model gave better agreement with experiment than the state-dependent model in the high-momentum region.
- [speculative] The authors suggest the VMC/QMC workflow could be extended to metals, trapped positron states at open-volume defects, surfaces, interfaces, and large voidlike defects.
- [speculative] The authors argue that QMC can become a practical high-accuracy support tool for positron spectroscopies more broadly, beyond the benchmark systems studied here.

**Results summary:** This peer-reviewed empirical study develops and benchmarks a variational quantum Monte Carlo method for computing Doppler broadening spectra of positron annihilation in solids. Results were obtained from classical VMC simulations, not quantum-computing hardware. Using Si and AlN as benchmark materials, the authors show that relatively small simulation cells and simpler Slater-Jastrow wave functions are sufficient for converged Doppler spectra, with larger cells and backflow corrections producing results within statistical error bars. Vibrational effects in Si were found to be negligible, with the largest deviation from static-lattice spectra below 1%. When compared with experimental coincidence Doppler measurements, VMC spectra agreed better than conventional DFT-based state-dependent and state-independent enhancement models, especially in AlN where agreement was described as excellent. The paper concludes that explicit many-body treatment of electron-positron correlations is important for accurate modeling of positron-annihilation observables.

**Performance claims:**
- 16-atom simulation cells were sufficient for converged Doppler spectra, matching 54-atom cells in C and 72-atom cells in AlN within error bars
- Momentum cutoff pcut = 7 a.u. was used; Doppler spectra were found convergent with cutoffs as low as about 5 a.u.
- Twist grids used were 4x4x4 for C and Si and 4x4x5 for AlN
- In Si, the largest vibrational correction to the normalized Doppler spectrum was less than 1% around momentum 0.5 a.u.
- Experimental Doppler measurement resolution was 0.92 keV FWHM for Si and 0.90 keV FWHM for AlN
- Reliable theory-experiment comparison in Si was reported up to about p < 2.5 a.u., beyond which DFT-derived core spectra dominate and VMC statistical error becomes large
## Quantum advantage claim
**Classification:** not-applicable

This paper studies quantum Monte Carlo as a classical many-body simulation method for materials physics, not quantum computing. No quantum-computing advantage claim is made or evaluated.
## Limitations
- Scope is limited to semiconductors and insulators (C, Si, and AlN); metals are explicitly excluded because they require higher momentum resolution and larger computational effort.
- Experimental validation is only carried out for Si and AlN; diamond data were considered too noisy to support a meaningful benchmark.
- Core-electron contributions are not computed directly within VMC; they are added from separate DFT-based models, making the final spectra partly dependent on DFT approximations.
- The high-momentum region is less reliable because VMC statistical errors become large and the spectra are increasingly dominated by DFT-derived core contributions.
- Lattice-vibration analysis is performed only for bulk Si, so the conclusion that vibrations are insignificant is not directly validated for AlN or other materials.
- The vibrational treatment does not include anharmonic effects.
- Jastrow parameters were optimized only at the Gamma-point twist rather than independently for all twists.
- The benchmark set is small, limiting external validity and generalization to broader classes of materials or defect environments.
- [inferred] The study does not address scalability to production-scale simulations for large, defect-rich, or industrially relevant materials systems.
- [inferred] No reproducibility details such as full input decks, random seeds, or workflow artifacts are provided in the excerpt, which may hinder exact replication.
- [inferred] Results rely on pseudopotentials and frozen-core approximations, which may limit accuracy for materials where core or semicore states contribute more strongly.
- [inferred] The method is demonstrated on classical quantum Monte Carlo, not quantum computing hardware, so it does not provide evidence relevant to qubit noise, qubit-count constraints, or deployment on quantum devices.
## Open questions
- How well does the VMC approach perform for metals, where Fermi-surface features require much finer momentum resolution?
- Can the method accurately describe positrons trapped at open-volume defects, large voids, surfaces, or interfaces where nonlocal electron-positron correlations are important?
- Can the same QMC framework simultaneously and accurately describe both the electronic structure and trapped positron states in defect systems?
- How sensitive are the results to the DFT-based treatment of core annihilation, especially in the high-momentum region?
- Will the conclusion that small simulation cells and simple wave functions are sufficient remain valid for more complex materials and defected systems?
- What is the impact of anharmonic lattice vibrations and thermal expansion on Doppler spectra in materials beyond Si?
- How broadly do the observed improvements over DFT generalize across other semiconductors, insulators, and technologically relevant materials?

**Future work:**
- Extend the method to metals using larger simulation cells or denser twist grids to achieve the required momentum resolution.
- Apply QMC to positrons trapped at large voidlike defects.
- Study positron surface states and interface-related states where local or semilocal two-component DFT functionals fail.
- Test simultaneous QMC description of electronic structure and trapped positron states, motivated by work on the nitrogen-vacancy center in diamond.
- Apply QMC to both delocalized bulk positron states and trapped states at open-volume defects.
- Use QMC to support additional positron spectroscopies, including surface-sensitive techniques such as positron-annihilation-induced Auger spectroscopy.
- [inferred] Develop a fully QMC-based treatment of core-electron annihilation to reduce dependence on DFT corrections in the final spectra.
- [inferred] Validate the workflow on a broader and more diverse experimental benchmark set, including more materials and defect configurations.
## Key ideas
- #idea:hybrid-approach — Not applicable to the SLR scope: the paper studies classical variational quantum Monte Carlo for materials physics rather than quantum computing in finance.
- #contradiction:classical-vs-quantum — Despite the term 'quantum Monte Carlo,' the method is a classical HPC many-body simulation and provides no evidence about quantum algorithms for financial services.
## Contradictions
- The paper could be misread as quantum-computing research because of 'quantum Monte Carlo,' but it explicitly uses classical HPC clusters and no QPU; this contradicts any interpretation that it supports quantum superiority claims in finance-relevant quantum computing.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
