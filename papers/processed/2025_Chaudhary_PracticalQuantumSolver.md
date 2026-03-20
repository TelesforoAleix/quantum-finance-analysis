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
quantum_advantage_claim: theoretical
related_papers: []
relevance_phase1: high
relevance_phase3: high
source_type: conference-paper
source_type_confidence: high
step1_date: '2026-03-20T00:14:00.645829'
step1_model: Mistral-Large-3
step2_date: '2026-03-20T00:14:05.570801'
step2_model: Mistral-Large-3
step3_date: '2026-03-20T00:14:16.806859'
step3_model: Mistral-Large-3
step4_date: '2026-03-20T00:14:26.011521'
step4_model: Mistral-Large-3
step5_date: '2026-03-20T00:15:13.764321'
step5_model: Mistral-Large-3
step6_date: '2026-03-20T00:15:16.347457'
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
year: 2025
zotero_key: ''
---

## Abstract summary
This paper introduces a scalable and efficient quantum algorithm for solving multidimensional partial differential equations (PDEs), addressing limitations of existing variational quantum algorithms (VQAs) such as low accuracy and high execution times. The authors propose two algorithm variants leveraging finite-difference methods, classical-to-quantum encoding, and decomposition techniques, demonstrating improved performance on quantum simulators and real hardware for PDEs like Poisson, heat, Black-Scholes, and Navier-Stokes equations.
## Methodology
The paper presents a practical quantum solver for multidimensional partial differential equations (PDEs) with a focus on financial applications such as the Black-Scholes equation. The proposed methodology involves two variants of a quantum algorithm. Variant 1 combines the finite-difference method (FDM), classical-to-quantum (C2Q) encoding, and numerical instantiation, while Variant 2 employs FDM, C2Q encoding, and column-by-column decomposition (CCD). The PDEs are first discretized into linear systems using FDM, followed by preprocessing steps such as polar decomposition and singular value decomposition (SVD) to derive unitary matrices. These matrices are then encoded into quantum circuits using C2Q encoding. The quantum solver is validated on several PDEs, including Poisson, heat, Black-Scholes, and Navier-Stokes equations, demonstrating improved accuracy, scalability, and execution time compared to variational quantum algorithm (VQA)-based solvers. Experiments were conducted on both noise-free and noisy quantum simulators, as well as real quantum hardware (IBM's ibm_torino).
**Frameworks:** Qiskit, Berkeley Quantum Synthesis Toolkit (BQSKit)

**Experimental setup:** Experiments were performed using a computer cluster node equipped with a 48-core Intel Gold 6342 CPU, three NVIDIA A100 80 GB GPUs, and 256 GB of DDR4 RAM. The quantum simulations were conducted on noise-free (statevector simulator) and noisy (AerSimulator) simulators, as well as real quantum hardware (ibm_torino). The VQE-based experiments used the EfficientSU2 ansatz and the ADAM optimizer.

**Dataset:** The paper evaluates the proposed algorithm on several PDEs, including the Black-Scholes equation for option pricing. Parameters for the Black-Scholes equation include a risk-free rate of 4.3%, strike price of $100, share price range of 0 ≤ S ≤ $400, volatility of 20%, and maturity of 3 months. Other PDEs tested include Poisson, heat, and Navier-Stokes equations with predefined boundary and initial conditions.
## Findings
- [supported] The proposed quantum PDE solver algorithm (two variants: FDM + C2Q + numerical instantiation and FDM + C2Q + CCD) achieves higher accuracy, scalability, and faster execution times compared to VQA-based solvers on noise-free and noisy quantum simulators from IBM.
- [supported] The algorithm demonstrates promising results on real quantum hardware (ibm_torino), with Variant 1 performing better due to its depth optimization.
- [supported] The solver successfully addresses multidimensional Poisson, heat, Black-Scholes, and Navier-Stokes equations, showing close alignment with classical benchmarks and superior performance over VQE-based methods.
- [supported] Variant 1 of the proposed algorithm has a circuit depth complexity of O(N), where N = 2^n qubits, which is more efficient than Variant 2 (O(N^2)) and classical FFT-based solvers (O(N log N)).
- [speculative] The authors suggest that the proposed algorithm could offer a generalized quantum solution for PDEs across diverse domains, including finance and computational fluid dynamics, though this claim is not empirically validated for all possible PDEs.
- [speculative] Quantum advantage may emerge for solving high-dimensional PDEs due to the algorithm's scalability and reduced execution time, but this remains theoretical without direct comparison to state-of-the-art classical solvers on large-scale problems.

**Results summary:** The paper introduces a generalized quantum algorithm for solving multidimensional partial differential equations (PDEs) with two variants: Variant 1 (FDM + C2Q + numerical instantiation) and Variant 2 (FDM + C2Q + CCD). The algorithm was validated on Poisson, heat, Black-Scholes, and Navier-Stokes equations, demonstrating higher accuracy, scalability, and faster execution times compared to VQA-based solvers on both noise-free and noisy simulators. Results on real quantum hardware (ibm_torino) were promising, particularly for Variant 1 due to its depth optimization. The algorithm's circuit depth complexity (O(N) for Variant 1) suggests potential efficiency gains over classical methods, though empirical validation of quantum advantage is limited to simulations and small-scale hardware tests.

**Performance claims:**
- Higher accuracy than VQA-based solvers on noise-free and noisy simulators for Poisson, heat, Black-Scholes, and Navier-Stokes equations.
- Reduced total execution time compared to VQA-based solvers across all tested PDEs.
- Variant 1 achieves a circuit depth complexity of O(N), where N = 2^n qubits.
- Variant 2 achieves higher accuracy and scalability on simulators but with greater circuit depth (O(N^2)).
- Promising results on real quantum hardware (ibm_torino) for 4-qubit problems with 0.1M shots.
## Quantum advantage claim
**Classification:** theoretical

The paper claims a theoretical advantage based on the algorithm's scalability and reduced circuit depth complexity (O(N) for Variant 1) compared to classical FFT-based solvers (O(N log N)). However, quantum advantage is not empirically demonstrated on real hardware for large-scale problems, and results are primarily from simulations.
## Limitations
- Experiments conducted on quantum simulators and real hardware (IBM Torino) with limited qubit counts (up to 14 qubits), restricting scalability to larger problem sizes [inferred]
- Performance on real quantum hardware (ibm_torino) is significantly affected by noise, decoherence, and device-specific errors, leading to reduced accuracy compared to simulators
- Variant 2 of the proposed algorithm generates quantum circuits with higher depth (O(N²)), making it less suitable for NISQ devices compared to Variant 1 (O(N))
- Results for the VQE-based approach and Variant 1 are missing for some experiments (e.g., 2D Poisson equation) due to unrealistically high execution times
- Testing limited to specific case studies (Poisson, heat, Black-Scholes, and Navier-Stokes equations) without broader validation across other PDE types [inferred]
- Classical preprocessing steps (e.g., FDM, SVD, polar decomposition) may introduce approximations that affect overall solution accuracy [inferred]
- No explicit comparison with state-of-the-art classical PDE solvers (e.g., FFT-based methods) to benchmark quantum advantage [inferred]
- Page-limit constraints of the conference paper may have limited the depth of discussion on certain aspects (e.g., noise mitigation strategies) [inferred]
- Lack of detailed analysis on the impact of shot count (e.g., 1M vs. 256M shots) on solution accuracy and execution time [inferred]
- Assumption of zero boundary values (BVs) for some case studies (e.g., Poisson equation) may not generalize to real-world scenarios with non-zero BVs [inferred]
## Open questions
- How does the proposed algorithm perform on higher-dimensional PDEs (e.g., 5D or 6D) beyond the tested case studies?
- What is the trade-off between circuit depth and accuracy for Variant 1 and Variant 2 when scaling to larger qubit counts?
- How can noise mitigation techniques (e.g., error correction, dynamical decoupling) be integrated to improve performance on real quantum hardware?
- What are the computational limits of the proposed algorithm in terms of problem size (e.g., grid points) and qubit requirements?
- How does the algorithm compare to hybrid quantum-classical methods (e.g., quantum-assisted finite element methods) for solving PDEs?
- What is the impact of non-uniform grid spacing or adaptive meshing on the accuracy and scalability of the proposed method?
- Can the algorithm be extended to handle nonlinear PDEs or coupled systems of PDEs (e.g., fluid-structure interactions)?
- What are the implications of using different encoding schemes (e.g., amplitude encoding vs. C2Q) on the algorithm's performance?

**Future work:**
- Extend the algorithm to solve higher-dimensional PDEs (e.g., 5D or 6D) and validate its scalability
- Integrate noise mitigation techniques (e.g., error correction, dynamical decoupling) to improve performance on NISQ devices
- Benchmark the proposed algorithm against state-of-the-art classical PDE solvers (e.g., FFT-based methods) to quantify quantum advantage
- Explore hybrid quantum-classical approaches to combine the strengths of both paradigms for solving PDEs
- Investigate the use of adaptive meshing or non-uniform grid spacing to improve accuracy for complex geometries
- Apply the algorithm to nonlinear PDEs and coupled systems of PDEs (e.g., fluid-structure interactions)
- Optimize the classical preprocessing steps (e.g., FDM, SVD) to reduce computational overhead and improve accuracy
- Test the algorithm on a broader range of quantum hardware (e.g., trapped ions, photonic quantum computers) to assess platform-specific performance
- Develop a generalized framework for solving PDEs across diverse domains (e.g., finance, engineering, computational fluid dynamics)
- Explore the use of alternative encoding schemes (e.g., amplitude encoding) to reduce circuit depth and improve scalability
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

## Experiment details
### Input
{'Black-Scholes_equation': {'risk_free_rate': 0.043, 'strike_price': 100, 'share_price_range': [0, 400], 'volatility': 0.2, 'maturity': '3 months', 'preprocessing_steps': 'Discretization using FDM, polar decomposition, and SVD to derive unitary matrices.'}, 'Poisson_equation': {'source_function': 'f(x) = 10 for 1D, f(x,y) = xy for 2D, f(x,y,z) = xyz for 3D', 'distance': 1, 'boundary_values': 'Specified for each dimension (e.g., u(X-1) = -0.6, u(X_Nx) = -0.7 for 1D)'}, 'Heat_equation': {'initial_condition': '100°C for 2D and 3D', 'thermal_diffusivity': '0.97 cm²/s (Aluminum)', 'distance': '100 cm', 'time_duration': '10 minutes', 'boundary_values': '0°C'}, 'Navier-Stokes_equation': {'kinematic_viscosity': '10⁻⁶ m²/s (water)', 'domain_length': '1 m', 'pressure_gradient': '0.5 Pa/m', 'density': '1000 Kg/m³', 'external_force': '0.2 m/s²', 'initial_velocity_profile': '3 sin(πx) m/s'}}

### Process
1. Discretize the PDE into a linear system using FDM. 2. Preprocess the coefficient matrix using polar decomposition and SVD to obtain unitary matrices. 3. Encode classical data into quantum states using C2Q encoding. 4. Implement the unitary matrix as a quantum circuit using either numerical instantiation (Variant 1) or CCD (Variant 2). 5. Execute the quantum circuit on simulators or real quantum hardware. 6. Measure the output quantum state to obtain the solution vector. 7. Compare results against classical benchmarks and VQA-based solvers using RMSE and execution time metrics.

### Output
{'metrics_reported': ['RMSE error', 'total execution time'], 'comparison_baselines': ['Classical solvers', 'VQE-based solvers'], 'output_format': 'Solution profiles for each PDE, RMSE error plots, and execution time comparisons.'}

### Parameters
- qubit_count: Ranged from 4 to 14 qubits depending on the PDE and variant
- shots: Varied from 0.1M to 256M shots depending on the experiment
- simulator_types: ['Noise-free (statevector)', 'Noisy (AerSimulator)']
- hardware: ibm_torino for real quantum hardware experiments
- optimizer: ADAM for VQE-based experiments
- ansatz: EfficientSU2 for VQE-based experiments

### Hardware
{'simulator': 'Qiskit Aer statevector simulator (noise-free) and AerSimulator (noisy)', 'QPU_model': 'ibm_torino', 'cloud_provider': 'IBM Quantum', 'transpilation_settings': 'Depth-optimized circuits using BQSKit for numerical instantiation'}

### Reproducibility
The paper provides detailed experimental parameters and preprocessing steps. Code availability is not explicitly mentioned, but the methodology description is sufficient for replication. Data sources for financial parameters (e.g., risk-free rate, volatility) are cited.
