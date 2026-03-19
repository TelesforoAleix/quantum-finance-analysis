---
aliases:
- A Practical Quantum Solver for Multidimensional Partial Differential Equations
- Practical Quantum Solver Multidimensional
authors:
- Manu Chaudhary
- Kareem El-Araby
- Alvir Nobel
- Ishraq Islam
- Manish Singh
- Sunday Ogundele
- Kieran Egan
- Sneha Thomas
- Vincent Vordtriede
- Devon Bontrager
- Serom Kim
- Esam El-Araby
auto_detected: true
classification: ''
contradiction_flags: []
doi: 10.1145/3731599.3767550
evidence_type: ''
idea_tags:
- idea:quantum-advantage
- idea:near-term-feasibility
- idea:hybrid-approach
journal_or_venue: 'SC Workshops ''25: Workshops of the International Conference for
  High Performance Computing, Networking, Storage and Analysis'
methodology_tags:
- variational
- quantum-simulation
- classical-simulation
paper_type: ''
quantum_advantage_claim: speculative
related_papers: []
relevance_phase1: high
relevance_phase3: high
source_type: conference-paper
source_type_confidence: high
step1_date: '2026-03-18T23:28:32.009677'
step1_model: Mistral-Large-3
step2_date: '2026-03-18T23:28:34.920204'
step2_model: Mistral-Large-3
step3_date: '2026-03-18T23:28:42.749986'
step3_model: Mistral-Large-3
step4_date: '2026-03-18T23:28:50.190863'
step4_model: Mistral-Large-3
step5_date: '2026-03-18T23:29:01.076294'
step5_model: Mistral-Large-3
step6_date: '2026-03-18T23:29:04.928687'
step6_model: Mistral-Large-3
steps_completed:
- 1
- 2
- 3
- 4
- 5
- 6
tags:
- topic/derivatives-pricing
- topic/asset-pricing
- topic/market-simulation
- method/variational
- method/quantum-simulation
- method/classical-simulation
- idea/quantum-advantage
- idea/near-term-feasibility
- idea/hybrid-approach
title: A Practical Quantum Solver for Multidimensional Partial Differential Equations
topic_tags:
- derivatives-pricing
- asset-pricing
- market-simulation
year: 2025
zotero_key: ''
---

## Abstract summary
This paper introduces a scalable quantum algorithm for solving multidimensional partial differential equations (PDEs), addressing limitations of existing variational quantum algorithms (VQAs) such as low accuracy and high execution times. The authors propose two variants of their algorithm, combining finite-difference methods with classical-to-quantum encoding and either numerical instantiation or column-by-column decomposition, and validate their approach on practical PDEs like Black-Scholes and Navier-Stokes equations using both simulators and real quantum hardware.
## Methodology
The paper proposes an efficient and scalable quantum algorithm for solving multidimensional partial differential equations (PDEs) with applications in finance, engineering, and computational fluid dynamics. The methodology involves two variants of the algorithm: Variant 1 combines the finite-difference method (FDM), classical-to-quantum (C2Q) encoding, and numerical instantiation, while Variant 2 employs FDM, C2Q encoding, and column-by-column decomposition (CCD). The PDEs are first discretized into linear systems using FDM, followed by preprocessing steps such as polar decomposition and singular value decomposition (SVD) to generate unitary matrices for quantum computation. The algorithm is validated by solving Poisson, heat, Black-Scholes, and Navier-Stokes equations. Experiments are conducted on noise-free and noisy quantum simulators (IBM's AerSimulator) and real quantum hardware (IBM's ibm_torino). Performance is evaluated in terms of accuracy (RMSE), scalability, and execution time, with comparisons to variational quantum eigensolver (VQE)-based approaches.

**Algorithms used:** Finite Difference Method (FDM), Classical-to-Quantum (C2Q) Encoding, Numerical Instantiation, Column-by-Column Decomposition (CCD), Singular Value Decomposition (SVD), Polar Decomposition
**Frameworks:** Qiskit, Berkeley Quantum Synthesis Toolkit (BQSKit)

**Experimental setup:** Experiments were performed on a computer cluster node equipped with a 48-core Intel Gold 6342 CPU, three NVIDIA A100 80 GB GPUs (CUDA version 11.7), and 256 GB of DDR4 RAM. The proposed algorithm was evaluated using noise-free (statevector simulator) and noisy (AerSimulator) quantum simulators, as well as real quantum hardware (IBM's ibm_torino). VQE-based experiments used the EfficientSU2 ansatz and the ADAM optimizer within Qiskit's VQE class.

**Dataset:** The paper uses synthetic datasets for solving PDEs, including: (1) Poisson equation with source functions (e.g., f(x) = 10 for 1D, f(x,y) = xy for 2D, f(x,y,z) = xyz for 3D) and boundary conditions; (2) Heat equation with initial conditions (e.g., 100°C) and thermal diffusivity values for aluminum; (3) Black-Scholes equation with parameters such as risk-free rate (4.3%), strike price ($100), volatility (20%), and maturity (3 months); (4) Navier-Stokes equation with parameters like kinematic viscosity (10^-6 m²/s), pressure gradient (0.5 Pa/m), and initial velocity profiles (e.g., 3 sin(πx) m/s).
## Findings
- [supported] The proposed quantum PDE solver algorithm (two variants: FDM + C2Q + numerical instantiation, and FDM + C2Q + column-by-column decomposition) achieves higher accuracy, scalability, and faster execution times compared to variational quantum algorithm (VQA)-based solvers on noise-free and noisy quantum simulators from IBM.
- [supported] The algorithm was validated on multiple PDEs, including Poisson, heat, Black-Scholes, and Navier-Stokes equations, demonstrating its generality across diverse domains such as finance, engineering, and computational fluid dynamics.
- [supported] On real quantum hardware (IBM Torino), the algorithm produced promising results, though noise effects were significant due to short decoherence times and device-specific errors.
- [supported] Variant 1 of the proposed algorithm (numerical instantiation) performed better on real quantum hardware than Variant 2 (column-by-column decomposition) due to its depth-optimized circuits.
- [supported] The algorithm reduced root mean square error (RMSE) compared to VQA-based approaches, particularly for higher qubit counts (e.g., 14 qubits for 2D Poisson and heat equations).
- [speculative] The authors suggest that the proposed algorithm could overcome the limitations of existing quantum PDE solvers (e.g., HHL and VQAs), which suffer from low accuracy, high execution times, and poor scalability on NISQ devices.
- [speculative] The paper implies potential quantum advantage for solving multidimensional PDEs, though this is not explicitly demonstrated on real hardware beyond small-scale tests (e.g., 4 qubits).
- [supported] Classical-to-quantum (C2Q) encoding used in the algorithm reduces quantum gate count by 50% compared to alternative amplitude encoding techniques, making it more suitable for NISQ devices.

**Results summary:** The paper introduces a generalized quantum algorithm for solving multidimensional partial differential equations (PDEs) with two variants: one combining finite-difference method (FDM), classical-to-quantum (C2Q) encoding, and numerical instantiation, and another using FDM, C2Q, and column-by-column decomposition (CCD). The algorithm was tested on Poisson, heat, Black-Scholes, and Navier-Stokes equations, demonstrating improved accuracy, scalability, and execution time compared to variational quantum algorithm (VQA)-based solvers. Results were validated on noise-free and noisy simulators, as well as real quantum hardware (IBM Torino), though noise effects limited performance on hardware. The algorithm outperformed VQA-based approaches in RMSE and execution time, particularly for higher qubit counts (e.g., 14 qubits).

**Performance claims:**
- Higher accuracy and scalability compared to VQA-based solvers on noise-free and noisy simulators
- Faster execution times than VQA-based solvers for multidimensional PDEs
- 50% reduction in quantum gate count using C2Q encoding compared to alternative amplitude encoding
- Successful validation on real quantum hardware (IBM Torino) for 4 qubits with 0.1M shots
- Lower RMSE error for 2D Poisson and heat equations at 14 qubits compared to VQA-based approaches
## Quantum advantage claim
**Classification:** speculative

The paper suggests potential quantum advantage for solving multidimensional PDEs more efficiently than classical methods, but this is not empirically demonstrated on real hardware beyond small-scale tests. Claims are primarily supported by simulations, and the authors acknowledge noise limitations on NISQ devices. The advantage is framed as theoretical and speculative for larger-scale problems.
## Limitations
- Low qubit count constraints limit scalability to higher-dimensional PDEs (e.g., experiments capped at 14 qubits)
- Performance on real quantum hardware (ibm_torino) degraded due to noise and short decoherence times, particularly for Variant 2
- Variant 2 generates higher-depth quantum circuits compared to Variant 1, increasing susceptibility to gate errors on NISQ devices
- Experiments primarily conducted on simulators (noise-free and noisy); real hardware results limited to 4 qubits and 0.1M shots
- No direct comparison with state-of-the-art classical PDE solvers (e.g., finite element methods) to benchmark quantum advantage
- [inferred] Assumes idealized boundary conditions (e.g., zero boundary values for Poisson/heat equations), which may not reflect real-world financial PDEs
- [inferred] Lack of error mitigation techniques (e.g., dynamical decoupling, zero-noise extrapolation) to address hardware noise
- [inferred] Limited exploration of non-Hermitian or ill-conditioned matrices, common in financial PDEs (e.g., Black-Scholes with stochastic volatility)
- [inferred] Page-limit constraints may have omitted details on hyperparameter tuning (e.g., optimizer choice for VQE comparisons)
- Classical preprocessing steps (e.g., SVD, polar decomposition) may introduce computational overhead, offsetting quantum speedup
## Open questions
- How does the proposed algorithm perform on larger qubit counts (e.g., 50+ qubits) for high-dimensional PDEs in finance?
- What is the impact of noise mitigation techniques on solution accuracy for real hardware implementations?
- Can the algorithm handle non-linear PDEs (e.g., Hamilton-Jacobi-Bellman equations) without linearization approximations?
- How does the algorithm compare to classical solvers (e.g., GPU-accelerated finite difference methods) in terms of wall-clock time and energy efficiency?
- What are the trade-offs between circuit depth (Variant 1 vs. Variant 2) and solution accuracy for specific financial PDEs (e.g., Black-Scholes with dividends)?
- How sensitive is the algorithm to input matrix sparsity and conditioning, particularly for ill-posed financial problems?
- Can the algorithm be extended to time-dependent PDEs with adaptive mesh refinement, a common requirement in quantitative finance?

**Future work:**
- Test the algorithm on larger-scale quantum hardware (e.g., IBM Heron or Google Sycamore processors) with 50+ qubits
- Incorporate error mitigation techniques (e.g., probabilistic error cancellation, symmetry verification) to improve real hardware performance
- Benchmark against classical solvers (e.g., PETSc, FEniCS) for specific financial PDEs to quantify quantum advantage
- Extend the algorithm to non-linear PDEs and stochastic PDEs relevant to finance (e.g., local volatility models, interest rate term structure)
- Optimize classical preprocessing steps (e.g., SVD, polar decomposition) to reduce overhead for large-scale problems
- Explore hybrid quantum-classical approaches (e.g., quantum-assisted multigrid methods) to improve scalability
- Investigate the algorithm's performance on PDEs with non-uniform grids or adaptive mesh refinement, critical for financial modeling
- Apply the solver to real-world financial datasets (e.g., market-implied volatility surfaces) to validate practical utility
## Key ideas
- #idea:quantum-advantage — Proposes a scalable quantum algorithm for solving multidimensional PDEs (e.g., Black-Scholes) with potential quantum advantage over classical methods, though not yet empirically demonstrated at scale
- #idea:near-term-feasibility — Demonstrates feasibility on NISQ devices (IBM Torino) with 4 qubits, showing promise for near-term applications despite noise limitations
- #idea:hybrid-approach — Combines classical preprocessing (FDM, SVD, polar decomposition) with quantum computation to reduce qubit requirements and improve accuracy
- #limitation:noise — Noise on real hardware (IBM Torino) significantly degrades performance, particularly for deeper circuits (Variant 2)
- #limitation:qubit-count — Experiments limited to 14 qubits, insufficient for high-dimensional financial PDEs (e.g., multi-asset Black-Scholes)
- #limitation:no-empirical-validation — Quantum advantage claims are speculative and lack direct comparison with state-of-the-art classical solvers (e.g., finite element methods)
## Contradictions
<!-- Step 6 output — where this paper contradicts others -->

## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
