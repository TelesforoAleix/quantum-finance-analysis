---
aliases:
- Convergence to the ﬁxed-node limit in deep variational Monte Carlo
- Convergence xed node limit
authors:
- Z. Schätzle
- J. Hermann
- F. Noé
auto_detected: true
classification: ''
contradiction_flags: []
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
step1_date: '2026-03-25T15:55:53.619556'
step1_model: gpt-5.1
step2_date: '2026-03-25T15:55:58.055880'
step2_model: gpt-5.1
step3_date: '2026-03-25T15:56:37.751843'
step3_model: gpt-5.4
step4_date: '2026-03-25T15:57:21.325361'
step4_model: gpt-5.4
step5_date: '2026-03-25T15:57:45.077422'
step5_model: gpt-5.4
step6_date: '2026-03-25T15:57:51.318262'
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
title: Convergence to the ﬁxed-node limit in deep variational Monte Carlo
topic_tags: []
year: 2021
zotero_key: ''
---

## Abstract summary
The paper studies how deep neural-network-based variational quantum Monte Carlo (deep QMC), in particular PauliNet, converges toward the fixed-node limit as the network size and architecture complexity are increased. The authors disentangle different contributions to accuracy by examining restricted PauliNet variants that separately correct mean-field orbitals and add correlation via deep Jastrow factors, benchmarking on small molecules and model systems. They show that neural networks can effectively remove finite-basis Hartree–Fock errors, systematically approach fixed-node diffusion Monte Carlo energies, and, with backflow, improve nodal surfaces beyond the fixed-node approximation, especially illustrated on the water molecule.
## Methodology
This preprint presents an empirical computational study of deep variational quantum Monte Carlo (VMC) for electronic-structure problems, centered on the PauliNet neural-network wavefunction ansatz. The authors analyze convergence toward the fixed-node limit by systematically varying model expressiveness and isolating different ansatz components: a deep orbital-correction model, a deep many-body Jastrow factor, a mean-field Jastrow factor, and the full Slater-Jastrow-backflow-style PauliNet. The wavefunction is optimized under the standard VMC variational principle by minimizing the energy expectation value, estimated via Monte Carlo integration over electron configurations sampled from the squared wavefunction using Langevin sampling. Neural-network components are built from a graph-convolutional architecture acting on electron-nucleus and electron-electron distance graphs, with permutation-equivariant latent embeddings used to construct Jastrow and backflow terms. The study benchmarks performance on small molecular systems (H2, He, Be, LiH, H4, H2O), compares against Hartree-Fock (HF), complete-basis-set (CBS) limits, full configuration interaction (FCI), coupled-cluster references, and fixed-node diffusion Monte Carlo (FN-DMC)/DMC references, and includes an extensive hyperparameter grid search for H4 plus systematic scaling experiments on LiH and H2O. As a preprint, it should be treated as non-peer-reviewed.

**Algorithms used:** Variational Monte Carlo, Fixed-Node Diffusion Monte Carlo, Hartree-Fock, MCSCF, FCI, AdamW, Langevin sampling
**Frameworks:** DeepQMC, PySCF

**Experimental setup:** Numerical experiments were carried out with the DeepQMC Python package. The PauliNet ansatz uses a graph-convolutional neural network over fully connected electron-nucleus/electron-electron distance graphs. Optimization follows alternating Langevin sampling of electron configurations and stochastic gradient-based parameter updates. Default training used batch size 2000, 2000 walkers, AdamW optimizer, CyclicLR scheduler, learning-rate range 1e-4 to 1e-2, epoch size 100, 4 decorrelation sampling steps, and target acceptance 57%. Default architecture used 16 distance features, embedding dimension 128, 4 interaction layers, Jastrow network depth 3, filter network depth 1, and h/g network depths 2. System-specific training steps were 5000 for H4 and 10000 for H2, He, Be, and LiH; H2O training length is shown in a figure rather than a fixed table entry.

**Dataset:** No external supervised dataset was used. Inputs are ab initio molecular systems and geometries for H2, He, Be, LiH, H4 (square and deformed rectangle), H2O, and non-interacting composite systems H2-H2 and LiH-H2. Baseline orbitals and determinant coefficients were initialized from standard quantum chemistry calculations such as HF or MCSCF in basis sets including 6-31G, 6-311G, cc-pVDZ, cc-pVTZ, cc-pVQZ, cc-pV5Z, TZP, and Roos-aug-DZ-ANO.
## Experiment details
### Input
Molecular electronic-structure test cases rather than tabular financial datasets. Systems include H2, He, Be, LiH, H4 square, H4 deformed rectangle, H2O, H2-H2, and LiH-H2. Explicit geometries are reported for LiH (Li at (0,0,0), H at (1.595,0,0) Å), H4 square (four H at ±0.635 Å in x/y plane), H4 deformed (x = ±0.900 Å, y = ±0.635 Å), and H2O (O at (0,0,0), H at (±0.75695, 0.58588, 0) Å). H2 dissociation was evaluated along a nuclear-distance curve, with one example at d = 1.4. Inputs were initialized from HF or MCSCF calculations in small and larger basis sets (e.g., 6-31G, 6-311G, TZP, Roos-aug-DZ-ANO, cc-pVXZ families), with cusp corrections applied where needed and no external data preprocessing in the machine-learning sense.

### Process
1. Construct PauliNet or restricted variants: (a) deep orbital correction, (b) deep many-body Jastrow factor, (c) mean-field Jastrow factor, or (d) full PauliNet with backflow. 2. Initialize determinant coefficients and orbitals from preceding HF or MCSCF calculations. 3. Build latent electron embeddings with a graph-convolutional neural network using electron-nucleus and electron-electron distances; enforce permutation equivariance/invariance for backflow and Jastrow terms. 4. Optimize the trial wavefunction by minimizing the VMC energy expectation value. 5. Approximate the expectation value by Monte Carlo integration over M sampled electron configurations drawn from |psi|^2 using Langevin sampling. 6. Update parameters with stochastic gradients using AdamW and CyclicLR. 7. For H4, perform a grid search over 864 hyperparameter combinations around default values, varying network depths, number of interactions, distance features, and embedding/kernel dimensions. 8. For LiH, systematically scale DNN width and number of interaction layers L to study convergence to the fixed-node limit; also evaluate dipole moments. 9. For H4 relative-energy experiments, run five independent optimizations per model and use the minimum-energy run to compute relative energies between geometries. 10. Compare VMC energies to HF, CBS estimates, FCI, coupled-cluster, and FN-DMC/DMC references; compute recovered correlation or fixed-node correlation percentages. No explicit convergence threshold is stated; training proceeds for a fixed number of steps and final energies are estimated from the end of optimization.

### Output
Outputs are total energies, recovered correlation energy percentages, recovered fixed-node correlation energy percentages, dipole moments, relative energy differences between geometries, and size-consistency comparisons. Results are benchmarked against HF baselines, extrapolated CBS limits, exact references for small systems, FCI in large basis sets, CCSD(T)-R12 dipole references, and FN-DMC/DMC literature references. Statistical uncertainty from Monte Carlo sampling is reported in parentheses for energies, and relative-energy accuracy is discussed in kcal/mol bands (e.g., within 1 or 2 kcal/mol of DMC reference).

### Parameters
- default_basis: 6-31G
- distance_features: 16
- embedding_dimension: 128
- interaction_layers_L: 4
- jastrow_network_depth: 3
- filter_network_depth_w: 1
- embedding_to_kernel_depth_h: 2
- kernel_to_embedding_depth_g: 2
- batch_size: 2000
- number_of_walkers: 2000
- training_steps: {'H4': 5000, 'H2': 10000, 'He': 10000, 'Be': 10000, 'LiH': 10000, 'H2O': 'see training curve figure; not fixed in table'}
- optimizer: AdamW
- learning_rate_scheduler: CyclicLR
- learning_rate_min: 0.0001
- learning_rate_max: 0.01
- clipping_window_q: 5
- epoch_size: 100
- decorrelation_sampling_steps: 4
- target_acceptance: 57%
- hyperparameter_scan_H4_models: 864
- independent_runs_for_H4_relative_energy: 5

### Hardware
N/A

### Reproducibility
Preprint. The paper names the DeepQMC package and provides substantial architectural and hyperparameter detail, plus open data availability via Figshare. PySCF is cited for some reference calculations. No explicit code repository for the exact experiment scripts is given in the excerpt, and hardware/runtime details are absent, but the methodological detail is fairly strong and partial replication appears feasible.
## Findings
- [supported] A deep neural-network orbital correction applied to Hartree–Fock baselines in a small 6-31G basis recovered at least 97% of the finite-basis-set error for H2, He, Be, LiH, and H4, reaching energies close to the mean-field complete-basis-set limit.
- [supported] For the two-electron nodeless systems H2 and He, the deep Jastrow factor achieved energies matching the exact references to five significant digits, recovering 99.97(3)% and 99.98(2)% of the correlation energy, respectively.
- [supported] Along the H2 dissociation curve, the deep Jastrow ansatz outperformed FCI in large cc-pVQZ/cc-pV5Z bases, reducing correlation-energy error by one to two orders of magnitude at compressed geometries and remaining more accurate at stretched geometries.
- [supported] Extensive hyperparameter scans on H4 and LiH showed that increasing model width and interaction depth systematically improves variational energies toward the fixed-node diffusion Monte Carlo limit for single-determinant Slater–Jastrow ansatzes.
- [supported] For LiH, sufficiently expressive deep Jastrow models reached energies within sampling error of the single-determinant FN-DMC benchmark and produced dipole moments converging toward coupled-cluster reference values.
- [supported] For two H4 geometries, both total and relative energies converged toward DMC references as model size increased; relative energies were within 2 kcal/mol of DMC for models with more than two interaction layers and within 1 kcal/mol for the largest-width models.
- [supported] Numerical tests on non-interacting H2-H2 and LiH-H2 systems indicate the deep Jastrow optimization is effectively size-consistent in practice, with combined-system energies closely matching sums of separately optimized subsystem energies.
- [supported] On H2O, the deep orbital correction recovered about 90% of the Hartree–Fock finite-basis-set error, while a mean-field Jastrow recovered only about half, suggesting that approaching the CBS limit significantly changes the nodal surface.
- [supported] For H2O with a single-determinant Slater–Jastrow ansatz in the Roos-aug-DZ-ANO basis, PauliNet recovered 97.2(1)% of the fixed-node correlation energy, improving previous single-determinant VMC Slater–Jastrow results by roughly half an order of magnitude.
- [supported] Combining deep orbital correction with a deep Jastrow factor on H2O starting from a small 6-311G Hartree–Fock baseline recovered 96.0(2)% of the fixed-node correlation energy relative to the Roos-aug-DZ-ANO benchmark.
- [supported] A single-determinant Slater–Jastrow–backflow version of full PauliNet on H2O achieved VMC energies below single-determinant DMC references, indicating that the backflow transformation improves the nodal surface and can overcome fixed-node limitations.
- [speculative] The authors argue that deep QMC offers a general and systematically improvable ansatz family whose accuracy can be increased by scaling trainable parameters without introducing new architectural components.
- [speculative] The paper suggests that the main long-term advantage of deep QMC over fixed-node DMC is the ability to go beyond the fixed-node approximation by learning improved nodal surfaces through many-body orbital transformations.

**Results summary:** This preprint studies how deep variational Monte Carlo with PauliNet approaches the fixed-node limit as network size increases. Empirically, the authors show that neural-network orbital corrections can remove most Hartree–Fock basis-set error from small-basis baselines, and that deep Jastrow factors can achieve near-exact energies for nodeless two-electron systems. For four-electron systems (LiH and H4), larger and deeper Jastrow networks systematically improve energies toward fixed-node DMC benchmarks, with associated improvements in dipole moments and relative energies. The method also appears size-consistent in practical tests. On H2O, single-determinant Slater–Jastrow PauliNet substantially improves over prior VMC results, and the full single-determinant Slater–Jastrow–backflow PauliNet attains energies below single-determinant DMC references, which the authors interpret as evidence of improved nodal surfaces. Because this is a preprint and the claims concern quantum chemistry rather than quantum computing hardware, any broader advantage claims are best treated as method-level and not as demonstrated quantum-computing advantage.

**Performance claims:**
- At least 97% of finite-basis-set error recovered for H2, He, Be, LiH, and H4 using deep orbital correction from a 6-31G HF baseline
- H2 deep Jastrow energy: -1.17446(1) Eh vs exact -1.1744748 Eh; 99.97(3)% correlation energy recovered
- He deep Jastrow energy: -2.90372(1) Eh vs exact -2.9037247 Eh; 99.98(2)% correlation energy recovered
- For H2 dissociation, deep QMC reduced correlation-energy error by 1–2 orders of magnitude versus FCI at compressed geometries
- For H2-H2, combined and separate optimizations gave -2.34894(1) Eh and -2.34895(1) Eh vs exact -2.34895 Eh
- For LiH-H2, combined and separate optimizations gave -9.24394(7) Eh and -9.24405(7) Eh vs exact -9.24501 Eh
- For H2O, deep orbital correction recovered about 90% of HF finite-basis-set error
- For H2O, mean-field Jastrow recovered about half of the HF finite-basis-set error
- H2O single-determinant Slater–Jastrow PauliNet in 6-311G: VMC energy -76.3923(7) Eh; 91.2(2)% fixed-node correlation energy
- H2O deep orbital correction + Jastrow from 6-311G baseline: VMC energy -76.4096(7) Eh; 96.0(2)% fixed-node correlation energy
- H2O single-determinant Slater–Jastrow PauliNet in Roos-aug-DZ-ANO: VMC energy -76.4139(5) Eh; 97.2(1)% fixed-node correlation energy
- Previous H2O single-determinant Slater–Jastrow VMC references cited: 87.01(6)% and 73.5(3)% fixed-node correlation energy
- Full single-determinant PauliNet on H2O: -76.4252(3) Eh in 6-311G and -76.4281(3) Eh in Roos-aug-DZ-ANO, corresponding to 96.67(8)% and 97.38(8)% of total correlation energy
- Traditional comparison on H2O: single-determinant PauliNet SD-SJB -76.4281(3) Eh vs prior SD-SJB -76.4034(2) Eh; comparable to MD-SJ with 2316 determinants (-76.4259(6) Eh) and 7425 determinants (-76.4289(8) Eh)
## Quantum advantage claim
**Classification:** not-applicable

The paper is about deep neural-network variational Monte Carlo for quantum chemistry, not quantum computing in financial services. It does not claim a quantum-computing advantage; reported gains are method-performance improvements versus classical quantum chemistry baselines and DMC/FCI references.
## Limitations
- The paper notes that there is currently little understanding of why deep neural-network wavefunctions work well and how individual components contribute to approximating the ground-state wavefunction and energy.
- Most of the analysis is conducted with restricted single-determinant Slater–Jastrow-type ansatzes possessing a mean-field nodal surface, so the study does not fully characterize the behavior of the unrestricted full PauliNet ansatz.
- The authors state that the restricted PauliNet variants are not intended to achieve best accuracy; best performance requires the full flexibility of PauliNet, limiting conclusions about ultimate achievable accuracy from the restricted experiments.
- For systems with nontrivial nodes, benchmarking the deep Jastrow factor requires FN-DMC references and reconstructed nodal surfaces, so conclusions depend on the quality and consistency of those external fixed-node benchmarks.
- The convergence results exhibit stochastic fluctuations due to both stochastic training and Monte Carlo sampling error.
- The authors explicitly note that the stochasticity of optimization complicates comparison of individual runs, especially for relative energies.
- The dipole moment convergence shows fluctuations, particularly for small models, indicating ambiguity from degenerate energy minima when the exact solution lies outside the variational subspace.
- The implemented PauliNet variant discussed in the size-consistency section is not exactly factorizable; exact size consistency is only argued to hold approximately in practice for the tested cases.
- The water-molecule experiments keep the graph-convolutional network size fixed while increasing system size, so the study does not fully explore scaling of architecture size with molecular complexity.
- The comparison of full PauliNet against traditional trial wavefunctions is explicitly described by the authors as not ultimate, since accuracy could be further improved by larger graph-convolutional networks or multiple determinants.
- A more thorough investigation of nodal-surface improvements and a benchmark of computational complexity are deferred to future work, leaving these aspects unresolved in the present paper.
- As a preprint, the work has not undergone peer review.
- [inferred] The study is limited to small benchmark molecules and model systems (H2, He, Be, LiH, H4, H2O), which constrains evidence for scalability to larger chemically relevant systems.
- [inferred] No wall-clock runtime, memory usage, or systematic computational-cost scaling analysis is provided, limiting assessment of practical efficiency versus conventional quantum chemistry methods.
- [inferred] The hyperparameter exploration is extensive only for selected small systems; robustness of chosen settings across broader chemical spaces is not established.
- [inferred] Results rely heavily on comparisons to prior literature references and selected basis sets rather than a uniform in-paper benchmark suite across all methods.
- [inferred] Although code/data availability is mentioned, reproducibility may still be sensitive to random seeds, optimization settings, and stochastic training dynamics.
## Open questions
- Why do deep neural-network wavefunctions such as PauliNet and related ansatzes achieve such high accuracy compared with traditional trial wavefunctions?
- How do the individual components of deep QMC ansatzes—Jastrow factor, orbital correction, backflow, and determinant expansion—each contribute to final accuracy?
- How systematically and efficiently can the full PauliNet ansatz improve the nodal surface beyond the fixed-node approximation?
- To what extent do larger graph-convolutional architectures or multideterminant expansions improve accuracy for larger molecules?
- How does optimization stochasticity scale with model size and system complexity, and how can it be reduced for more reliable comparisons?
- How robust are relative-energy predictions across geometries and systems when training noise and sampling noise are taken into account?
- What is the computational complexity of PauliNet relative to traditional VMC, FN-DMC, and standard quantum chemistry methods as system size grows?
- How well do the observed convergence trends generalize beyond the small molecules studied here to larger or more strongly correlated systems?
- Under what conditions does approximate size consistency of the non-factorizable PauliNet variant break down for heterogeneous composite systems?

**Future work:**
- Use the present analysis to guide future improvements of neural-network architectures in deep QMC.
- Investigate in more detail how the full PauliNet ansatz improves the nodal surface and overcomes fixed-node limitations.
- Conduct a more thorough benchmark of computational complexity for the full PauliNet ansatz.
- Explore larger graph-convolutional neural-network architectures to further improve accuracy.
- Introduce multiple determinants into PauliNet to improve accuracy beyond the single-determinant results shown here.
- Further investigate the stochasticity of optimization, particularly its impact on comparing individual runs and relative energies.
- [inferred] Extend benchmarking from small molecules to larger, more chemically and industrially relevant systems.
- [inferred] Develop more stable or reproducible training/optimization protocols to reduce variance across runs.
- [inferred] Perform broader empirical validation of scaling behavior, including runtime and memory benchmarks against classical baselines.
## Key ideas
- #idea:hybrid-approach — Uses neural-network-enhanced variational Monte Carlo (PauliNet) to improve electronic-structure accuracy, but this is outside financial-services quantum computing.
- #limitation:simulation-only — All results are from classical deep-QMC/VMC computations rather than execution on quantum hardware.
- #limitation:no-empirical-validation — No empirical validation on financial tasks or quantum-computing hardware; benchmarks are small-molecule quantum chemistry cases.
## Contradictions
<!-- Step 6 output — where this paper contradicts others -->

## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
