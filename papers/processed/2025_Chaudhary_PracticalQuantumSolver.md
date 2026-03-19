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
contradiction_flags:
- contradiction:scalability
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
step1_date: '2026-03-19T13:14:02.676933'
step1_model: Mistral-Large-3
step2_date: '2026-03-19T13:14:54.353482'
step2_model: Mistral-Large-3
step3_date: '2026-03-19T13:15:04.153528'
step3_model: Mistral-Large-3
step4_date: '2026-03-19T13:15:18.160796'
step4_model: Mistral-Large-3
step5_date: '2026-03-19T13:15:33.665281'
step5_model: Mistral-Large-3
step6_date: '2026-03-19T13:16:01.263958'
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
- topic/risk-modelling
- method/variational
- method/quantum-simulation
- method/classical-simulation
- idea/quantum-advantage
- idea/near-term-feasibility
- idea/hybrid-approach
- contradiction/scalability
title: A Practical Quantum Solver for Multidimensional Partial Differential Equations
topic_tags:
- derivatives-pricing
- asset-pricing
- risk-modelling
year: 2025
zotero_key: ''
---

## Abstract summary
This paper introduces a scalable and efficient quantum algorithm for solving multidimensional partial differential equations (PDEs), addressing limitations of existing variational quantum algorithms (VQAs) such as low accuracy and high execution times. The authors propose two variants of their algorithm, leveraging finite-difference methods, classical-to-quantum encoding, and decomposition techniques, and validate their approach on benchmark PDEs like Poisson, heat, Black-Scholes, and Navier-Stokes equations. The results demonstrate improved performance in accuracy, scalability, and execution time compared to VQA-based solvers on both simulators and real quantum hardware.
## Methodology
The paper proposes a generalized quantum algorithm for solving multidimensional partial differential equations (PDEs) with two variants. Variant 1 combines the finite-difference method (FDM), classical-to-quantum (C2Q) encoding, and numerical instantiation, while Variant 2 employs FDM, C2Q encoding, and column-by-column decomposition (CCD). The methodology involves discretizing PDEs into linear systems using FDM, preprocessing the coefficient matrix via polar decomposition to generate unitary matrices, and encoding classical data into quantum states using C2Q. The algorithm is validated through case studies on Poisson, heat, Black-Scholes, and Navier-Stokes equations. Experiments were conducted on noise-free and noisy quantum simulators (IBM's AerSimulator and statevector simulator) and real quantum hardware (IBM's ibm_torino). Performance metrics such as accuracy (RMSE), scalability, and execution time were compared against variational quantum algorithms (VQAs) like VQE.

**Algorithms used:** Finite-Difference Method (FDM), Classical-to-Quantum (C2Q) Encoding, Numerical Instantiation, Column-by-Column Decomposition (CCD), Singular Value Decomposition (SVD), Polar Decomposition
**Frameworks:** Qiskit, Berkeley Quantum Synthesis Toolkit (BQSKit)

**Experimental setup:** Experiments were performed using a computer cluster node equipped with a 48-core Intel Gold 6342 CPU, three NVIDIA A100 80 GB GPUs (CUDA version 11.7), and 256 GB of DDR4 RAM. The proposed algorithm was evaluated on noise-free (statevector simulator) and noisy (AerSimulator) quantum simulators, as well as real quantum hardware (IBM's ibm_torino). VQE-based experiments utilized Qiskit's EfficientSU2 ansatz and the ADAM optimizer.

**Dataset:** The paper used synthetic datasets for various PDEs: (1) Poisson equation: source functions like f(x) = 10, f(x,y) = xy, and f(x,y,z) = xyz with boundary conditions; (2) Heat equation: initial conditions like f(x,0) = 100°C and thermal diffusivity values for aluminum; (3) Black-Scholes equation: parameters including risk-free rate (4.3%), strike price ($100), volatility (20%), and maturity (3 months); (4) Navier-Stokes equation: parameters such as kinematic viscosity (10^-6 m²/s), pressure gradient (0.5 Pa/m), and initial velocity profile (3 sin(πx) m/s).
## Findings
- [supported] The proposed quantum PDE solver algorithm (two variants: FDM + C2Q + numerical instantiation, and FDM + C2Q + CCD) achieves higher accuracy, scalability, and faster execution times compared to VQA-based solvers on noise-free and noisy quantum simulators from IBM.
- [supported] The algorithm was validated on multiple PDEs (Poisson, heat, Black-Scholes, Navier-Stokes) with results closely matching classical solvers and outperforming VQE-based approaches in accuracy and execution time.
- [supported] Variant 1 of the algorithm demonstrates better performance on real quantum hardware (ibm_torino) due to its depth-optimized circuits, while Variant 2 shows higher accuracy and scalability on simulators but generates deeper circuits.
- [supported] The proposed algorithm achieves lower RMSE errors across all tested PDEs (e.g., 1D/2D/3D Poisson, 2D/3D heat, Black-Scholes, Navier-Stokes) compared to VQE-based methods on both noise-free and noisy simulators.
- [supported] The algorithm scales to 14 qubits for 2D Poisson and heat equations on noisy simulators, with execution times significantly lower than VQE-based solvers.
- [speculative] Variant 1 of the algorithm may offer better depth complexity (O(N)) than classical FFT-based solvers (O(N log N)) for multidimensional PDEs, suggesting potential quantum advantage in specific scenarios.
- [speculative] The authors claim the algorithm is generalized for diverse PDEs, but empirical validation on real hardware is limited to small-scale problems (e.g., 4 qubits for 1D Poisson).
- [disputed] The paper claims superior performance over VQA-based solvers, but comparisons are primarily against VQE, which is only one type of VQA; other VQA variants (e.g., VQLS) may perform differently.

**Results summary:** The paper introduces a generalized quantum algorithm for solving multidimensional partial differential equations (PDEs) with two variants: Variant 1 (FDM + C2Q + numerical instantiation) and Variant 2 (FDM + C2Q + CCD). The algorithm was tested on Poisson, heat, Black-Scholes, and Navier-Stokes equations, demonstrating higher accuracy, scalability, and faster execution times compared to VQA-based solvers on both noise-free and noisy simulators. Results on real quantum hardware (ibm_torino) showed promising performance for Variant 1, though noise effects were significant. The algorithm's depth complexity (O(N) for Variant 1) is theoretically better than classical FFT-based solvers (O(N log N)), but empirical validation of quantum advantage remains limited to simulations and small-scale hardware tests.

**Performance claims:**
- Higher accuracy (lower RMSE) than VQE-based solvers for 1D/2D/3D Poisson, 2D/3D heat, Black-Scholes, and Navier-Stokes equations on noise-free and noisy simulators.
- Faster execution times compared to VQE-based solvers for all tested PDEs (e.g., 14-qubit 2D Poisson solved in significantly less time).
- Scalability up to 14 qubits for 2D Poisson and heat equations on noisy simulators.
- Depth complexity of O(N) for Variant 1, compared to O(N log N) for classical FFT-based solvers.
- Promising results on real quantum hardware (ibm_torino) for 4-qubit 1D Poisson with 0.1M shots.
## Quantum advantage claim
**Classification:** speculative

The paper suggests potential quantum advantage based on theoretical depth complexity (O(N) for Variant 1) and empirical performance on simulators. However, quantum advantage is not demonstrated on real hardware beyond small-scale tests (4 qubits), and claims rely on comparisons to specific VQA-based solvers (VQE) rather than broader classical or quantum alternatives. Results are primarily from simulations, with limited validation of scalability or noise resilience on NISQ devices.
## Limitations
- Low qubit count constraints limit scalability; experiments conducted with up to 14 qubits on simulators and 4 qubits on real hardware (ibm_torino)
- Performance on real quantum hardware (ibm_torino) is significantly affected by noise, decoherence, and device-specific errors
- Variant 2 of the proposed algorithm generates higher-depth circuits (O(N²)) compared to Variant 1 (O(N)), which may limit its practicality on NISQ devices
- Experiments primarily conducted on simulators (noise-free and noisy); real hardware validation is limited to small-scale tests (4 qubits)
- No direct comparison with state-of-the-art classical PDE solvers (e.g., FFT-based methods) to benchmark quantum advantage
- Assumption of zero boundary values (BVs) for Poisson, heat, and Navier-Stokes equations may not generalize to all real-world scenarios
- Black-Scholes equation tests limited to European-style options; no evaluation of American-style or exotic options
- [inferred] Lack of detailed analysis on the impact of quantum noise mitigation techniques (e.g., error correction, dynamical decoupling) on solution quality
- [inferred] Page-limit constraints of the conference paper may have omitted deeper discussions on failure cases or edge conditions
- [inferred] Reliance on specific quantum compilation tools (e.g., BQSKit, Qiskit) may limit reproducibility across different quantum hardware platforms
## Open questions
- How does the proposed algorithm perform on larger-scale problems (e.g., >20 qubits) requiring fault-tolerant quantum computing?
- What is the trade-off between circuit depth (Variant 1 vs. Variant 2) and solution accuracy on real NISQ devices?
- Can the algorithm be extended to handle non-zero or time-dependent boundary conditions for PDEs in financial applications?
- How does the algorithm compare to classical solvers (e.g., FFT-based methods) in terms of computational complexity and practical runtime for large-scale problems?
- What are the implications of quantum noise on the stability and convergence of the proposed PDE solver variants?
- Can the algorithm be generalized to solve other types of PDEs (e.g., hyperbolic, nonlinear) beyond the case studies presented?
- What is the minimum qubit coherence time required to achieve reliable results on real quantum hardware?

**Future work:**
- Extend the algorithm to larger qubit counts (e.g., 50+ qubits) and evaluate scalability on next-generation quantum hardware
- Incorporate noise mitigation techniques (e.g., error correction, dynamical decoupling) to improve performance on NISQ devices
- Benchmark the proposed algorithm against state-of-the-art classical PDE solvers to quantify quantum advantage
- Test the algorithm on a broader range of financial PDEs, including American-style options and multi-asset derivatives
- Explore hybrid quantum-classical approaches to handle non-zero boundary conditions and time-dependent problems
- Investigate the use of alternative quantum encoding techniques (e.g., amplitude amplification) to reduce circuit depth
- Validate the algorithm on additional real quantum hardware platforms (e.g., Rigetti, IonQ) to assess cross-platform reproducibility
- Develop a theoretical framework to analyze the convergence and stability of the proposed variants under quantum noise
- Apply the algorithm to real-world financial datasets (e.g., historical market data) to evaluate practical utility
## Key ideas
- #idea:quantum-advantage — Proposes a quantum PDE solver with theoretical depth complexity (O(N)) potentially outperforming classical FFT-based solvers (O(N log N)) for financial PDEs like Black-Scholes
- #idea:near-term-feasibility — Demonstrates feasibility on NISQ devices (IBM Torino) with 4 qubits, showing near-term applicability despite noise limitations
- #idea:hybrid-approach — Combines classical preprocessing (FDM, SVD, polar decomposition) with quantum computation to reduce qubit requirements and improve accuracy
- #limitation:qubit-count — Experiments limited to 14 qubits on simulators and 4 qubits on real hardware, insufficient for high-dimensional financial PDEs (e.g., multi-asset derivatives)
- #limitation:noise — Noise on real hardware (IBM Torino) significantly degrades performance, particularly for deeper circuits (Variant 2)
- #limitation:no-empirical-validation — Quantum advantage claims are speculative and lack direct comparison with state-of-the-art classical solvers (e.g., finite element methods)
## Contradictions
- #contradiction:scalability — Claims potential scalability to larger problems, but empirical validation is limited to 14 qubits on simulators and 4 qubits on real hardware, contradicting broader claims of quantum advantage for real-world financial applications
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
