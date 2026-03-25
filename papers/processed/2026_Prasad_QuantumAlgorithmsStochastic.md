---
aliases:
- 'Quantum Algorithms for Stochastic Differential Equations: Achieving Polynomial
  and Super-Polynomial Speedups for High-Dimensional Systems'
- Quantum Algorithms Stochastic Differential
authors:
- Yalla Jnan Devi Satya Prasad
auto_detected: true
classification: ''
contradiction_flags:
- contradiction:scalability
doi: 10.22541/au.176764501.12582212/v1
evidence_type: ''
idea_tags:
- idea:quantum-advantage
- idea:near-term-feasibility
- idea:hybrid-approach
journal_or_venue: Authorea Preprint
methodology_tags:
- HHL
- amplitude-estimation
- quantum-simulation
- variational
- quantum-ML
- classical-simulation
paper_type: ''
quantum_advantage_claim: speculative
related_papers: []
relevance_phase1: high
relevance_phase3: high
source_type: preprint
source_type_confidence: high
step1_date: '2026-03-25T16:15:37.946757'
step1_model: gpt-5.1
step2_date: '2026-03-25T16:15:42.197861'
step2_model: gpt-5.1
step3_date: '2026-03-25T16:16:28.105047'
step3_model: gpt-5.4
step4_date: '2026-03-25T16:17:00.464299'
step4_model: gpt-5.4
step5_date: '2026-03-20T01:01:49.424120'
step5_model: Mistral-Large-3
step6_date: '2026-03-20T01:01:52.350647'
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
- method/HHL
- method/amplitude-estimation
- method/quantum-simulation
- method/variational
- method/quantum-ML
- method/classical-simulation
- idea/quantum-advantage
- idea/near-term-feasibility
- idea/hybrid-approach
- contradiction/scalability
title: 'Quantum Algorithms for Stochastic Differential Equations: Achieving Polynomial
  and Super-Polynomial Speedups for High-Dimensional Systems'
topic_tags:
- derivatives-pricing
- asset-pricing
- market-simulation
year: 2026
zotero_key: ''
---

## Abstract summary
The paper proposes a set of quantum algorithms for simulating and solving stochastic differential equations (SDEs), targeting applications in areas such as quantitative finance, molecular dynamics, and climate science. It combines Hamiltonian simulation for drift, quantum random number generation for noise, and quantum amplitude estimation for expectations to obtain better scaling in dimension and accuracy than classical Monte Carlo and PDE-based methods, with formal complexity results for linear and semilinear SDEs. For nonlinear SDEs, it introduces variational quantum schemes with design choices aimed at avoiding barren plateaus, and illustrates the approach on multi-asset Black–Scholes, Heston volatility, and Langevin dynamics, including resource estimates and small-scale numerical simulations.
## Methodology
This preprint is primarily a theoretical-methods paper with a small empirical simulation component. It proposes a quantum framework for solving stochastic differential equations (SDEs) by combining amplitude-encoded state representations, Hamiltonian simulation for drift dynamics, quantum random number generation for stochastic noise increments, and quantum amplitude estimation for expectation estimation. For linear and semilinear SDEs, the paper develops complexity results under Lipschitz and boundedness assumptions, using time discretization, sparse/dense Hamiltonian simulation arguments, and query-complexity analysis to claim improved scaling over classical Monte Carlo and finite-difference PDE methods. For nonlinear SDEs, it introduces variational quantum schemes with problem-informed ansatz circuits, shallow depth, layer-wise training, and local cost functions to mitigate barren plateaus, together with an a priori error bound depending on parameter count and hardware noise. The paper analyzes finance-relevant models including multi-asset Black-Scholes and Heston, plus Langevin dynamics, and reports small-scale numerical simulations implemented in Qiskit on classical simulators with IBM-inspired noise models. These experiments compare quantum-estimated quantities such as option prices and rare-event probabilities against analytic Black-Scholes values or high-precision classical Monte Carlo / Brownian-dynamics references, using bias, RMSE, circuit depth, gate counts, runtime, and sample-efficiency as evaluation criteria. As a preprint, the work has not been peer reviewed.

**Algorithms used:** Hamiltonian simulation, Quantum amplitude estimation, Maximum-likelihood amplitude estimation, Iterative amplitude estimation, LCU, Trotter-Suzuki decomposition, Schrödingerization, Variational quantum algorithm, Quantum random number generation
**Frameworks:** Qiskit, Qiskit Terra, Qiskit Aer, IBM Quantum

**Experimental setup:** Small-scale numerical simulations were performed in Qiskit on classical backends, including Aer statevector and noisy QASM simulation. The appendix states simulations used Qiskit Terra 0.46 and Aer 0.15 with noise models calibrated to IBM heavy-hex devices, basis gates {u3, cx}, transpilation optimization level 2, layout restricted to 27-qubit heavy-hex graphs, and 8192 shots per circuit. Reported examples include a 2D Black-Scholes basket option using 10 qubits and a Langevin coarse-grained model with 3 beads; the paper also mentions 2- to 4-asset Black-Scholes instances with 10-12 qubits.

**Dataset:** No external benchmark dataset is used. Inputs are synthetic/model-based financial and physical systems: multi-asset Black-Scholes basket option instances with specified drift, volatility, correlation matrix, maturity, and strike; a 2D Heston stochastic-volatility model; and coarse-grained Langevin dynamics / protein models. Reference values are obtained from analytic Black-Scholes pricing where available, or from high-precision classical Monte Carlo / Brownian-dynamics simulations.
## Findings
- [supported] For linear and semilinear SDEs with Lipschitz coefficients, quantum algorithms estimate relevant quantities (option prices, expected hitting times, moments) to accuracy ε in time ˜O(poly(d)polylog(1/ε)), versus classical O(poly(d)/ε²).
- [supported] Quantum simulation of the Fokker-Planck equation achieves accuracy ε in time ˜O(d · log(1/ε)), compared to classical finite-difference solvers at O(n^{d+1}_s).
- [supported] Numerical simulations on small instances (e.g., 2D Black-Scholes, 3D Langevin) demonstrate polynomial-to-super-polynomial empirical speedups in accuracy for fixed runtime.
- [speculative] Quantum advantage for SDE solving may emerge on near-term hardware for high-dimensional problems (d = 10-100) in finance and molecular dynamics.
- [speculative] Variational quantum schemes for nonlinear SDEs, with barren plateau mitigation, could scale polynomially in dimension while maintaining convergence.
- [speculative] Hybrid classical-quantum approaches (e.g., quantum noise sampling + classical PDE solvers) may reduce quantum resource requirements while preserving speedups.
- [supported] Resource requirements for d-dimensional SDEs: ~150 qubits for d=10, ε=10⁻³, and δx=10⁻² in finance applications.
- [speculative] Superpolynomial speedups in sampling rare events (e.g., Langevin dynamics) could be achieved via quantum parallelism.

**Results summary:** The preprint presents a family of quantum algorithms for simulating and solving stochastic differential equations (SDEs) with improved scaling over classical methods. For linear and semilinear SDEs, the authors prove polynomial and super-polynomial speedups in accuracy (˜O(poly(d)polylog(1/ε)) vs. classical O(poly(d)/ε²)), supported by theoretical complexity analyses and small-scale numerical simulations. Variational quantum schemes for nonlinear SDEs are proposed with a priori error bounds and barren plateau mitigation strategies. Applications to multi-asset Black-Scholes, Heston stochastic volatility, and Langevin dynamics demonstrate empirical speedups, though results are limited to simulations and small instances. Resource requirements (qubits, gate depth, oracle calls) are quantified, suggesting feasibility on near-term quantum hardware for specific problem sizes.

**Performance claims:**
- Quantum algorithm for linear SDEs: ˜O(poly(d)polylog(1/ε)) vs. classical O(poly(d)/ε²)
- Fokker-Planck PDE speedup: ˜O(d · log(1/ε)) vs. classical O(n^{d+1}_s)
- 2D Black-Scholes simulation: 3x speedup over classical Monte Carlo (10 qubits, simulated)
- 3D Langevin dynamics: ~100x speedup in rare event sampling (simulated)
- Heston model (2D): Quadratic speedup in accuracy (˜O(√(1/ε)) vs. classical O(1/ε²))
## Quantum advantage claim
**Classification:** speculative

The paper claims polynomial and super-polynomial speedups for SDE solving, but these are primarily theoretical or demonstrated via classical simulations of quantum algorithms. Empirical results are limited to small-scale instances (e.g., 2-10 qubits), and no real hardware validation is provided. The advantage is classified as speculative due to the lack of large-scale or fault-tolerant hardware demonstrations.
## Limitations
- Preprint has not been peer-reviewed, which may affect the rigor and validity of the findings [inferred]
- Numerical simulations limited to small-scale instances (e.g., 2D Black-Scholes with 10 qubits), restricting generalizability to larger, real-world problems [inferred]
- Experiments conducted on Qiskit simulators with noise models, not on real quantum hardware, which may not fully capture hardware-specific limitations (e.g., gate errors, decoherence) [inferred]
- Resource requirements (e.g., ~150 qubits for d=10, ε=10⁻³) exceed current NISQ device capabilities, limiting practical applicability [inferred]
- Polynomial-depth circuits (˜O(poly(d) log(1/ε))) may still be too deep for current NISQ devices with high error rates (10⁻³ to 10⁻² per gate) [inferred]
- Assumes bounded spectral norm and Lipschitz coefficients for drift/diffusion terms, which may not hold for all real-world SDEs (e.g., rough volatility models) [inferred]
- State space truncation to a hypercube [−R, R]^d with R=poly(d, T) may introduce bias for heavy-tailed distributions or long time horizons [inferred]
- Variational quantum schemes for nonlinear SDEs rely on problem-informed ansätze, which may not be easily generalizable to arbitrary nonlinear systems [inferred]
- Barren plateau mitigation techniques (e.g., layer-wise training, local cost functions) are theoretically motivated but lack extensive empirical validation on real hardware [inferred]
- Amplitude estimation overhead (O(√(1/ε)) calls) may be prohibitive for very high precision (ε → 0) due to circuit depth and error accumulation [inferred]
- Noise generation via quantum RNG assumes idealized Gaussian noise, which may not account for hardware-specific noise distributions [inferred]
- Hybrid classical-quantum approaches (e.g., quantum noise sampling + classical PDE solvers) introduce additional complexity and potential integration challenges [inferred]
- Lack of comparison with state-of-the-art classical SDE solvers (e.g., adaptive time-stepping, multilevel Monte Carlo) to benchmark quantum advantage [inferred]
- Error bounds for variational schemes (Error_var = O(1/√p + hardware noise · L)) depend on hardware noise, which is not quantified in simulations [inferred]
- Discretization assumptions (e.g., δx = Θ(ε/Lf)) may not be feasible for high-dimensional systems due to memory constraints [inferred]
## Open questions
- How do the proposed quantum algorithms perform on real quantum hardware with current error rates and qubit counts?
- What is the impact of hardware noise (e.g., gate errors, decoherence) on the empirical speedups observed in simulations?
- Can the polynomial-to-super-polynomial speedups be maintained for larger problem instances (e.g., d > 20) on near-term devices?
- How do the variational quantum schemes for nonlinear SDEs compare to classical methods in terms of accuracy, robustness, and scalability?
- What are the trade-offs between circuit depth, qubit count, and accuracy for practical financial applications (e.g., option pricing with d=100)?
- How sensitive are the results to the choice of ansatz and training strategy for variational schemes?
- Can the proposed methods be extended to SDEs with non-Lipschitz coefficients or unbounded domains (e.g., rough volatility models)?
- What are the implications of state space truncation for long-time simulations (e.g., T >> 1) or heavy-tailed distributions?
- How do the quantum algorithms perform in the presence of correlated noise or crosstalk on real hardware?
- What are the minimal hardware requirements (e.g., qubit count, gate fidelity) to achieve a practical quantum advantage for SDE solving?
- How do the resource estimates (e.g., qubits, gate depth) scale for multi-period or path-dependent financial derivatives?
- Can the quantum speedups be combined with classical variance reduction techniques (e.g., importance sampling) to further improve performance?
- What are the limitations of amplitude estimation in the presence of hardware noise, and can alternative estimation techniques (e.g., iterative amplitude estimation) mitigate these?
- How do the proposed methods compare to other quantum approaches for SDEs (e.g., quantum PDE solvers, quantum Monte Carlo)?

**Future work:**
- Test the algorithms on real quantum hardware (e.g., IBM Eagle, Google Sycamore) to validate empirical speedups and noise resilience
- Extend the framework to larger problem instances (e.g., d=50-100) and assess scalability on near-term devices
- Develop hybrid quantum-classical algorithms that combine quantum noise sampling with classical drift solvers to reduce quantum resource requirements
- Investigate adaptive ansatz designs for variational quantum schemes to improve trainability and accuracy for nonlinear SDEs
- Apply error mitigation techniques (e.g., zero-noise extrapolation, probabilistic error cancellation) to improve performance on NISQ devices
- Benchmark the quantum algorithms against state-of-the-art classical SDE solvers (e.g., multilevel Monte Carlo, adaptive time-stepping) for real-world financial and scientific applications
- Explore the use of quantum algorithms for path-dependent financial derivatives (e.g., Asian options, barrier options) and multi-period portfolio optimization
- Develop quantum algorithms for SDEs with non-Lipschitz coefficients or unbounded domains (e.g., rough volatility models, jump-diffusion processes)
- Investigate the integration of quantum SDE solvers with other quantum algorithms (e.g., quantum machine learning for parameter estimation)
- Extend the framework to stochastic partial differential equations (SPDEs) and high-dimensional PDEs in finance and physics
- Develop theoretical and empirical bounds for the impact of hardware noise on quantum speedups for SDE solving
- Explore the use of quantum error correction or fault-tolerant techniques to enable scalable SDE solving on future quantum computers
- Apply the proposed methods to other domains (e.g., climate science, molecular dynamics) and assess their practical value
- Develop open-source software tools and libraries for quantum SDE solving to facilitate adoption in industry and academia
## Key ideas
- #idea:quantum-advantage — Quantum algorithms achieve polynomial and super-polynomial speedups for solving SDEs in finance, with complexity ˜O(poly(d)polylog(1/ε)) vs. classical O(poly(d)/ε²).
- #idea:quantum-advantage — Quantum amplitude estimation and Hamiltonian simulation enable O(√1/ε) speedup in precision for multi-asset Black-Scholes and Heston models.
- #idea:near-term-feasibility — Variational quantum schemes for nonlinear SDEs propose barren plateau mitigation strategies (e.g., problem-informed ansätze) to enable NISQ-era applicability.
- #idea:hybrid-approach — Hybrid classical-quantum approaches (e.g., quantum noise sampling + classical PDE solvers) could reduce quantum resource requirements while preserving speedups.
- #idea:quantum-advantage — Numerical simulations demonstrate 3x–100x speedups in accuracy for fixed runtime on small-scale financial models (e.g., 2D Black-Scholes, 3D Langevin dynamics).
## Contradictions
- #contradiction:scalability — The paper claims super-polynomial speedups for rare event sampling in Langevin dynamics, but these are speculative due to untested assumptions about noise resilience and state preparation fidelity on NISQ hardware. This contradicts prior work (e.g., scalability challenges in high-dimensional problems).
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->

## Experiment details
### Input
Model-generated inputs rather than a fixed dataset. Black-Scholes experiments use 2- to 4-asset synthetic instances (including a 2D correlated basket option example), with problem parameters explicitly described as drift mu, volatility sigma, correlation matrix, maturity T, and strike K. State variables are encoded as discretized log-prices over bounded intervals [y_min, y_max], with l qubits per asset. Theoretical sections assume state-space truncation to [-R, R]^d and grid spacing delta_x chosen as Theta(epsilon / L_f). Langevin experiments use a coarse-grained molecular/protein model with 3 beads, encoding coordinates and velocities and evaluating barrier-crossing / hitting-time observables. No real market time series, sample count, or historical period is reported.

### Process
The experimental pipeline is described as follows: (1) specify SDE/model parameters such as drift, volatility, correlations, maturity, and payoff definition; (2) discretize time into n_t steps and encode the state distribution or discretized variables into qubit registers; (3) build an SDE simulation circuit U_SDE using drift blocks (Hamiltonian simulation or parameterized drift unitaries), noise-generation blocks approximating Gaussian increments, and mixing/entangling blocks for correlations; (4) append a payoff-encoding unitary U_f that maps the terminal state to an ancilla amplitude corresponding to the target observable; (5) run amplitude estimation, either standard Qiskit AmplitudeEstimation or a custom maximum-likelihood estimator, on Aer statevector or noisy QASM simulators; (6) for variational nonlinear-SDE settings, train shallow problem-informed ansatz circuits layer-wise using local cost functions of the form sum_i (E_quantum[f_i(X)] - E_classical[f_i(X)])^2; (7) repeat runs to estimate variance and RMSE; and (8) compare against analytic Black-Scholes prices, classical Monte Carlo, or Brownian-dynamics simulations using BAOAB for Langevin dynamics. The appendix reports 8192 shots per circuit. The main text also mentions 32 amplitude-estimation calls for the 2D Black-Scholes example. For theory, time stepping uses second-order weak schemes such as Milstein or high-order Runge-Kutta-type integrators, and Langevin ansatz construction references a Trotterized BAOAB splitting scheme.

### Output
Outputs include estimated option prices, expected values, rare-event probabilities, and hitting-time indicators. Evaluation metrics reported are bias relative to analytic or high-precision classical references, RMSE, variance from repeated runs, circuit depth, two-qubit gate count, runtime/wall-clock comparisons, and qualitative/quantitative speedup claims. Baselines include classical Monte Carlo for Black-Scholes and Heston, finite-difference PDE solvers in the theoretical comparison, and classical Brownian-dynamics simulations with BAOAB for Langevin dynamics. Example reported results include a 2D Black-Scholes case where classical Monte Carlo used 10,000 samples for 0.1% accuracy versus a simulated quantum approach with 32 amplitude-estimation calls, and claims that amplitude estimation reduces required samples by about an order of magnitude for fixed accuracy.

### Parameters
- qubits_reported: [10, '10-12', 150]
- shots: 8192
- basis_gates: ['u3', 'cx']
- transpilation_optimization_level: 2
- layout_constraint: 27-qubit heavy-hex graph
- noise_model_error_rates: {'one_qubit': 0.0001, 'two_qubit': 0.001}
- amplitude_estimation_calls_example: 32
- classical_monte_carlo_samples_example: 10000
- classical_langevin_trajectories_example: 100000
- ansatz_depth_scaling: L = O(log d)
- time_discretization: n_t time steps; theory discusses second-order weak schemes such as Milstein / high-order Runge-Kutta-type integrators
- state_space_discretization: grid spacing delta_x = Theta(epsilon / L_f), truncated domain [-R, R]^d
- black_scholes_register_encoding: l qubits per asset for discretized log-prices

### Hardware
No real QPU execution is reported. Simulations were run with Qiskit Terra 0.46 and Aer 0.15 on classical backends, including Aer statevector and noisy QASM simulators, using noise models calibrated to IBM heavy-hex devices. Basis gates were {u3, cx}; transpilation used optimization level 2 with layouts restricted to 27-qubit heavy-hex graphs. The paper discusses IBM Quantum / heavy-hex hardware characteristics and near-term feasibility but does not report execution on an actual IBM QPU.

### Reproducibility
Partial reproducibility only. The paper provides substantial methodological detail in the appendix, including circuit structure, encoding choices, simulator stack, shot count, transpilation settings, and evaluation metrics, but no code repository, scripts, or exact parameter files are provided. Inputs are mostly synthetic/model-based rather than external datasets, so data availability is not a major barrier. Replication of the general setup is plausible, but exact reproduction of all numerical claims would be difficult without code and fuller specification of instance parameters and implementation details. Preprint; not peer reviewed.
