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
- contradiction:classical-vs-quantum
doi: 10.1145/3731599.3767550
evidence_type: ''
idea_tags:
- idea:quantum-advantage
- idea:near-term-feasibility
- idea:hybrid-approach
journal_or_venue: 'SC Workshops ''25: Workshops of the International Conference for
  High Performance Computing, Networking, Storage and Analysis'
methodology_tags:
- VQE
- variational
- classical-simulation
paper_type: ''
quantum_advantage_claim: theoretical
related_papers: []
relevance_phase1: medium
relevance_phase3: medium
source_type: conference-paper
source_type_confidence: high
step1_date: '2026-03-25T16:07:34.948238'
step1_model: gpt-5.1
step2_date: '2026-03-25T16:07:38.975369'
step2_model: gpt-5.1
step3_date: '2026-03-25T16:08:38.102371'
step3_model: gpt-5.4
step4_date: '2026-03-25T16:09:03.218158'
step4_model: gpt-5.4
step5_date: '2026-03-25T16:09:31.189046'
step5_model: gpt-5.4
step6_date: '2026-03-25T16:09:43.214321'
step6_model: gpt-5.4
steps_completed:
- 1
- 2
- 3
- 4
- 5
- 6
tags:
- topic/derivatives-pricing
- method/VQE
- method/variational
- method/classical-simulation
- idea/quantum-advantage
- idea/near-term-feasibility
- idea/hybrid-approach
- contradiction/scalability
- contradiction/classical-vs-quantum
title: A Practical Quantum Solver for Multidimensional Partial Differential Equations
topic_tags:
- derivatives-pricing
year: 2025
zotero_key: ''
---

## Abstract summary
The paper proposes a generalized quantum algorithm for solving multidimensional partial differential equations, with two variants that combine finite-difference discretisation, classical-to-quantum (C2Q) encoding, and either numerical instantiation or column-by-column decomposition of the resulting unitary. The authors validate the approach on Poisson, heat, Black–Scholes, and Navier–Stokes equations, comparing against variational quantum algorithm (VQA)–based solvers on simulators and real hardware. They report that their method achieves better accuracy, scalability, and execution time than VQA-based PDE solvers, including on noisy quantum devices.
## Methodology
This conference workshop paper proposes and empirically evaluates a generalized quantum PDE solver with two implementation variants for multidimensional partial differential equations. The methodology begins with classical preprocessing: each PDE is discretized using the finite difference method (FDM) into a linear system A u = b, then singular value decomposition (SVD) and polar decomposition are used to derive the matrices needed to construct a quantum solution procedure. The right-hand-side vector transformed by P^-1 is normalized and encoded into a quantum state using classical-to-quantum (C2Q) amplitude encoding. The solution state is then obtained by applying U†, where Variant 1 realizes U† through numerical instantiation of the unitary using BQSKit, and Variant 2 realizes U† using column-by-column decomposition (CCD). The measured output state is converted back into a classical approximation of the PDE solution vector. The approach is validated on four case studies: multidimensional Poisson equations, multidimensional heat equations, the Black-Scholes equation for option pricing, and a Navier-Stokes equation. The paper compares the proposed solver against a VQE-based PDE solver and classical solutions, evaluating accuracy, scalability, and total execution time on noise-free simulators, noisy simulators, and IBM quantum hardware. As a conference-paper, this appears to be a workshop paper (SC Workshops '25).

**Algorithms used:** FDM, C2Q, CCD, SVD, Polar decomposition, VQE
**Frameworks:** Qiskit, BQSKit, AerSimulator, MatrixOp, EfficientSU2

**Experimental setup:** Experiments were run at the University of Kansas on a cluster node with a 48-core Intel Gold 6342 CPU, three NVIDIA A100 80 GB GPUs (CUDA 11.7, PCIe 4.0), and 256 GB DDR4 RAM. Evaluation used IBM noise-free statevector simulation, noisy AerSimulator simulation, and real IBM quantum hardware (ibm_torino). The VQE baseline encoded discretized PDEs as Hamiltonians mapped to Pauli operators via MatrixOp, used an EfficientSU2 ansatz, and optimized with ADAM through Qiskit's VQE implementation.

**Dataset:** No external dataset is used. Inputs are synthetic/numerically defined PDE benchmark problems: 1D/2D/3D Poisson equations, 2D/3D heat equations, Black-Scholes option pricing instances, and 2D space-time Navier-Stokes equations, each generated from specified source terms, boundary conditions, initial conditions, and physical/financial parameters.
## Findings
- [supported] The paper proposes a generalized quantum PDE solver with two variants: Variant 1 uses finite-difference discretization, classical-to-quantum encoding, and numerical instantiation; Variant 2 uses finite-difference discretization, classical-to-quantum encoding, and column-by-column decomposition.
- [supported] The proposed solver was validated on multiple PDE classes including Poisson, heat, Black-Scholes, and Navier-Stokes equations, indicating cross-domain applicability that includes finance via the Black-Scholes equation.
- [supported] On noise-free and noisy IBM simulators, the proposed approach is reported to achieve higher accuracy, better scalability, and lower total execution time than the VQE-based PDE solver baseline.
- [supported] For 1D Poisson problems, the solution profiles from the proposed method closely match analytical solutions on both noise-free and noisy simulators, while the VQE-based approach shows visible errors in the solution profile.
- [supported] The authors report promising results on real IBM quantum hardware (ibm_torino), with Variant 1 performing better than Variant 2 on hardware because its circuits are more depth optimized.
- [supported] Some VQE baseline and Variant 1 runs for larger Poisson cases were omitted because execution times were unrealistically high, which the authors use as evidence of poorer practical scalability for the baseline.
- [supported] For 2D and 3D heat equations, the proposed method is reported to maintain higher accuracy and lower execution time than the VQE-based method on both noise-free and noisy simulators.
- [supported] For the Black-Scholes call option case, the proposed method is reported to produce solution profiles and RMSE behavior superior to the VQE-based approach, with larger-scale noisy simulation also demonstrated.
- [supported] For the 2D Navier-Stokes case, the proposed method is reported to outperform the VQE-based baseline in RMSE and total execution time on simulators.
- [speculative] The paper argues that Variant 1 has favorable asymptotic depth complexity O(N) versus O(N^2) for Variant 2 and O(N log N) for FFT-based classical PDE solvers, implying potential efficiency benefits for multidimensional PDEs, but this is a theoretical complexity claim rather than an end-to-end demonstrated runtime advantage over classical solvers.
- [speculative] The authors suggest the method is practical for NISQ-era devices because C2Q encoding and numerical instantiation can generate shallower circuits, but hardware validation is limited and does not establish broad practical utility at scale.

**Results summary:** This conference paper presents a generalized quantum algorithm for solving multidimensional PDEs and evaluates it on Poisson, heat, Black-Scholes, and Navier-Stokes equations. The method combines classical finite-difference discretization and preprocessing with quantum state preparation and unitary application, using either numerical instantiation (Variant 1) or column-by-column decomposition (Variant 2). Experiments were run on noise-free and noisy IBM simulators and, for a small case, on IBM real hardware. Across the reported case studies, the authors claim the proposed solver achieves better accuracy, scalability, and execution time than a VQE-based PDE solver baseline. For finance-relevant content, the Black-Scholes call option case is included and is reported to show better solution quality and RMSE than the VQE baseline. Real-hardware results are described as promising but limited, with Variant 1 favored due to lower circuit depth. The paper does not provide confidence intervals and most evidence is from simulation rather than large-scale real-hardware execution.

**Performance claims:**
- 1D Poisson evaluated on noise-free and noisy simulators with 8 qubits and 1M shots
- 1D Poisson evaluated on noisy simulator with 14 qubits and 1M shots
- 1D Poisson evaluated on real hardware (ibm_torino) with 4 qubits and 0.1M shots
- 2D Poisson demonstrated on noisy simulator with 14 qubits; classical reference shown for Nx = Ny = 128
- 2D heat equation demonstrated on noisy simulator with 14 qubits and 256M shots; classical reference shown for Nx = Nt = 128
- 3D heat equation demonstrated on noisy simulator with 12 qubits; classical reference shown for Nx = Ny = Nt = 16
- Black-Scholes call option demonstrated on noisy simulator with 4 qubits and 1M shots, and at larger scale with 14 qubits and 1M shots
- 2D Navier-Stokes demonstrated on noisy simulator with 14 qubits and 1M shots
- Variant 1 circuit depth complexity claimed as O(N), where N = 2^n
- Variant 2 circuit depth complexity claimed as O(N^2)
- FFT-based classical PDE solvers cited as having O(N log N) time complexity
## Quantum advantage claim
**Classification:** theoretical

The paper reports empirical improvements over a VQE-based quantum baseline on simulators and limited real hardware, but it does not demonstrate quantum advantage over classical PDE solvers in end-to-end runtime. Its strongest advantage claim is theoretical: Variant 1 is argued to have O(N) circuit depth versus O(N log N) for FFT-based classical solvers under the paper's complexity framing.
## Limitations
- Results on real quantum hardware are limited; the paper reports real-device results only for a 4-qubit 1D Poisson case on ibm_torino, with most evaluations conducted on simulators.
- Some benchmark results are missing because execution times were 'unrealistically high,' indicating practical runtime limitations for the compared methods and incomplete empirical coverage.
- Results for the Black-Scholes put option are omitted due to space constraints, limiting completeness of the financial-services evaluation.
- Real-hardware performance is significantly affected by short decoherence times and device-specific errors.
- Variant 2 generates higher-depth circuits than Variant 1, which reduces suitability for NISQ hardware despite better simulator-side scalability/accuracy tradeoffs.
- The approach relies on classical preprocessing steps such as FDM discretization, SVD, and polar decomposition before quantum execution, which may shift computational burden to the classical side.
- The method assumes the PDE can be discretized into a linear system and transformed through polar decomposition/SVD into forms suitable for unitary implementation.
- The case studies use simplified setups and boundary/initial conditions (e.g., zero boundary values in several PDEs, simplified Navier-Stokes flow assumptions), which may limit realism.
- For Navier-Stokes, the formulation is simplified by assuming velocity only in the x-direction, reducing generality for full fluid dynamics problems.
- [inferred] No comparison is provided against strong non-quantum production solvers beyond classical reference solutions, such as optimized FFT, multigrid, or specialized financial PDE solvers.
- [inferred] The scalability claims are demonstrated only up to modest qubit sizes (e.g., 12–14 qubits in several experiments), far below production-scale financial PDE instances.
- [inferred] The paper does not provide a full end-to-end resource analysis including state-preparation cost, measurement overhead, and classical preprocessing cost when assessing practical advantage.
- [inferred] Reproducibility may be limited because the paper does not include full implementation details, code, seeds, calibration snapshots, or exact hardware settings in the provided text.
- [inferred] The use of very large shot counts in some noisy simulations (e.g., 1M and 256M shots) may reduce practical feasibility and may not reflect realistic runtime/cost on hardware.
- [inferred] The conference-paper format and 10-page length likely constrain reporting of ablations, sensitivity analyses, and broader benchmark coverage.
## Open questions
- How well does the proposed solver perform on larger real quantum devices beyond the small 4-qubit hardware demonstration?
- Can the method maintain its reported accuracy and runtime advantages as the dimensionality and grid resolution of PDEs increase substantially?
- What is the true end-to-end computational advantage once classical preprocessing costs are included?
- How robust is the approach to different noise models, calibration drift, and hardware-specific error patterns on current quantum devices?
- For financial applications, how does the method perform on more realistic Black-Scholes variants, such as multi-asset, American-style, or stochastic-volatility models?
- Can the generalized framework handle nonlinear or more complex PDE systems without substantial loss of efficiency?
- What are the tradeoffs between Variant 1 and Variant 2 across different problem classes, hardware backends, and target accuracies?
- How does the method compare with state-of-the-art classical PDE solvers in wall-clock time, memory use, and accuracy on practically relevant instances?
- To what extent do the simplifying assumptions in the Navier-Stokes and boundary-condition setups affect the generality of the conclusions?
- What qubit counts and error rates are required before the proposed approach becomes practically competitive for production financial workloads?

**Future work:**
- Extend evaluation to larger and more complex PDE instances on real quantum hardware.
- Investigate techniques to mitigate hardware noise and decoherence effects, especially for deeper circuits and Variant 2.
- Expand the financial-services experiments beyond the reported call-option Black-Scholes case to include put options and more realistic derivatives pricing problems.
- Benchmark against stronger classical baselines such as FFT-based and other advanced PDE solvers.
- Optimize circuit synthesis further to reduce depth and improve NISQ suitability.
- Study the scalability of both variants at higher qubit counts and finer discretizations.
- Develop more complete resource analyses that include classical preprocessing, state preparation, and measurement overhead.
- Generalize the solver to broader classes of PDEs and less simplified physical/financial models.
- Provide fuller empirical and reproducibility artifacts, such as code and detailed experimental configurations.
- Explore hybrid strategies that choose between numerical instantiation and CCD depending on problem size, hardware constraints, and target accuracy.
## Key ideas
- #idea:hybrid-approach — The solver combines classical finite-difference discretisation, SVD/polar-decomposition preprocessing, and quantum state preparation/unitary application to solve PDE-derived linear systems.
- #idea:near-term-feasibility — The paper argues NISQ applicability by using shallower circuit constructions, and reports a limited 4-qubit real-hardware demonstration on IBM Torino.
- #idea:quantum-advantage — The authors claim better accuracy, scalability, and execution time than a VQE-based quantum PDE baseline across Poisson, heat, Black-Scholes, and Navier-Stokes examples.
- #idea:quantum-advantage — For the finance-relevant Black-Scholes call-option case, the proposed method reportedly yields better solution profiles and RMSE than the VQE baseline.
- #idea:quantum-advantage — A theoretical complexity claim is made that Variant 1 has O(N) circuit depth, positioned as potentially favorable relative to FFT-based classical PDE solvers with O(N log N).
## Contradictions
- The paper suggests scalability and potential efficiency benefits, but empirical evidence is limited to modest problem sizes (mostly 12–14 qubits on simulators and 4 qubits on hardware), which conflicts with broad claims about practical scaling to real financial PDE workloads.
- The paper frames a potential quantum advantage, but it does not show end-to-end superiority over strong classical PDE solvers; comparisons are mainly against a VQE-based quantum baseline and classical reference solutions rather than optimized non-quantum production methods.
- Near-term feasibility is claimed, yet the reliance on very large shot counts in simulation and the degradation on real hardware indicate that practical NISQ deployment remains unproven.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->

## Experiment details
### Input
Problem instances are generated from discretized PDEs rather than a conventional dataset. Poisson: 1D with f(x)=10, d=1, boundary values u_X-1=-0.6 and u_XNx=-0.7; 2D with f(x,y)=xy, d=1, zero boundary values; 3D with f(x,y,z)=xyz, d=1, zero boundary values. Heat: 2D with initial condition f(x,0)=100°C, thermal diffusivity 0.97 cm^2/s (aluminum), spatial extent 100 cm, duration 10 minutes, boundary values 0°C; 3D with initial condition f(x,y,0)=100°C, diffusivities sigma_x=sigma_y=0.97 cm^2/s, Xdiff=Ydiff=100 cm, duration 10 minutes, boundary values 0°C. Black-Scholes: risk-free rate r=4.3%, strike K=$100, stock price range 0<=S<=400, volatility sigma=20%, maturity 3 months, for call and put options. Navier-Stokes: kinematic viscosity nu=10^-6 m^2/s, domain length 1 m, pressure gradient 0.5 Pa/m, density 1000 kg/m^3, external force 0.2 m/s^2, initial velocity u(x,0)=3 sin(pi x) m/s. Grid sizes shown in results include examples such as Nx=Ny=128 for 2D Poisson, Nx=Nt=128 for 2D heat and Black-Scholes, Nx=Ny=Nt=16 for 3D heat, and qubit-scaled matrix sizes up to 14 qubits.

### Process
1. Discretize each PDE using finite difference method into a linear system A u = b. 2. Apply polar decomposition A = P U and SVD A = W Sigma V† to derive P^-1 and U†. 3. Compute the normalized transformed input vector P^-1 b / ||P^-1 b||. 4. Encode this vector into a quantum state using C2Q amplitude encoding. 5. Apply U† using one of two variants: Variant 1 uses numerical instantiation of the unitary with BQSKit; Variant 2 uses column-by-column decomposition. 6. Measure the output quantum state and reconstruct the classical solution vector u by rescaling the measured output. 7. Benchmark against a VQE-based solver, where the discretized PDE is encoded as a Hamiltonian, mapped to Pauli operators with MatrixOp, solved using an EfficientSU2 ansatz and ADAM optimizer via Qiskit's VQE class. 8. Run experiments on statevector simulator, noisy AerSimulator, and ibm_torino hardware. 9. Compare solution profiles, RMSE, scalability, and total execution time against classical and VQE baselines. Reported shot counts include 1M shots for several noisy Poisson and Black-Scholes runs, 0.1M shots on ibm_torino for a 4-qubit Poisson case, and 256M shots for a 14-qubit 2D heat simulation.

### Output
Outputs are PDE solution profiles/solution surfaces, RMSE error summaries, scalability observations in terms of qubit/problem size, and total execution time. Comparisons are made against classical analytical/numerical solutions and a VQE-based PDE solver. The paper reports that the proposed variants, especially Variant 1 on hardware and Variant 2 on simulators, generally achieve lower RMSE, better scalability, and lower execution time than the VQE baseline; some VQE and Variant 1 results are omitted for larger cases due to impractically high execution times.

### Parameters
- compute_node_cpu: 48-core Intel Gold 6342
- gpus: 3 x NVIDIA A100 80 GB
- ram: 256 GB DDR4 3200 MHz
- simulators: ['statevector simulator', 'AerSimulator']
- qpu: ibm_torino
- vqe_ansatz: EfficientSU2
- vqe_optimizer: ADAM
- reported_qubits: [4, 8, 12, 14]
- reported_shots: [100000, 1000000, 256000000]

### Hardware
Classical host environment: University of Kansas cluster node with Intel Gold 6342 CPU, 3 NVIDIA A100 80 GB GPUs, CUDA 11.7, and 256 GB RAM. Quantum environments: IBM statevector simulator (noise-free), Qiskit AerSimulator (noisy), and IBM Quantum real hardware ibm_torino. The paper mentions BQSKit for unitary synthesis/optimization but does not provide detailed transpilation settings, coupling maps, backend calibration dates, or noise model configuration.

### Reproducibility
No code repository or explicit artifact link is provided in the excerpt. The paper gives substantial methodological detail on the algorithmic pipeline, PDE parameter settings, hardware platforms, and some qubit/shot settings, but lacks full implementation details such as exact circuit synthesis settings, noise model parameters, transpilation configuration, and complete VQE hyperparameters. Replication is partially feasible but not fully straightforward.
