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
journal_or_venue: Authorea Preprints
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
step1_date: '2026-03-20T01:01:04.330726'
step1_model: Mistral-Large-3
step2_date: '2026-03-20T01:01:07.588619'
step2_model: Mistral-Large-3
step3_date: '2026-03-20T01:01:22.247831'
step3_model: Mistral-Large-3
step4_date: '2026-03-20T01:01:32.279642'
step4_model: Mistral-Large-3
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
This preprint introduces a framework of quantum algorithms for simulating and solving stochastic differential equations (SDEs), which are critical in finance, chemistry, and climate science. The paper demonstrates how quantum computing techniques—such as Hamiltonian simulation, quantum random number generation, and amplitude estimation—can achieve polynomial and super-polynomial speedups over classical methods, particularly for high-dimensional systems. The work focuses on both linear and nonlinear SDEs, providing theoretical complexity bounds and practical resource estimates for applications like multi-asset option pricing and molecular dynamics.
## Methodology
The paper presents a theoretical and empirical framework for solving stochastic differential equations (SDEs) using quantum algorithms, targeting applications in finance, molecular dynamics, and climate science. The methodology combines Hamiltonian simulation for drift terms, quantum random number generation for noise increments, and quantum amplitude estimation for computing expectations. For linear and semilinear SDEs, the authors prove polynomial and super-polynomial speedups over classical methods, with complexity scaling as ˜O(poly(d)polylog(1/ε)) versus classical O(poly(d)/ε²). For nonlinear SDEs, variational quantum schemes with parameterized circuits are introduced, incorporating barren plateau mitigation strategies such as problem-informed ansätze, shallow circuits, and layer-wise training. The paper includes theoretical proofs for speedups in linear SDEs and Fokker-Planck PDEs, resource quantification (qubits, gate depth, oracle calls), and numerical simulations on small-scale instances using Qiskit to demonstrate empirical speedups.

**Algorithms used:** Hamiltonian simulation, Quantum random number generation, Quantum amplitude estimation, Trotter-Suzuki decomposition, Linear combination of unitaries (LCU), Variational quantum eigensolver (implicit in variational schemes), Maximum-likelihood amplitude estimation
**Frameworks:** Qiskit

**Experimental setup:** Numerical simulations were conducted using Qiskit Terra 0.46 and Aer 0.15 on classical backends with noise models calibrated to IBM heavy-hex devices. The experiments included small-scale instances of multi-asset Black-Scholes models (2D, 10 qubits) and Langevin dynamics for molecular coarse-graining (3D). Simulations were run on both statevector and noisy QASM simulators with shot counts of 8192 per circuit.

**Dataset:** The paper does not use external datasets but simulates synthetic financial and molecular dynamics scenarios, including multi-asset Black-Scholes models (e.g., basket options for two correlated assets) and Langevin dynamics for coarse-grained molecular systems (e.g., protein models with 3 beads).
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
Synthetic problem instances were used, including:
1. Multi-asset Black-Scholes: Parameters for drift (µ), volatility (σ), correlation matrix, maturity (T), and strike (K). Log-returns were discretized and encoded as quantum states.
2. Langevin dynamics: Coarse-grained coordinates (q) and velocities (v) for molecular systems, with parameters for potential energy (U), friction (γ), and temperature (kBT).
Preprocessing involved discretizing state spaces and encoding initial distributions as quantum states.

### Process
1. **Encoding**: Discretize state space and encode initial distributions as quantum states (amplitude encoding).
2. **Drift Simulation**: Use Hamiltonian simulation (Trotter-Suzuki or LCU) to evolve the drift term.
3. **Noise Generation**: Inject Gaussian noise increments via quantum random number generation.
4. **Amplitude Estimation**: Apply quantum amplitude estimation to compute expectations (e.g., option prices, hitting times). For variational schemes:
   - Design parameterized circuits with drift, noise, and mixer blocks.
   - Train using layer-wise optimization to minimize the difference between quantum and classical expectations.
   - Use local cost functions to mitigate barren plateaus.
5. **Execution**: Run circuits on Qiskit simulators (statevector or noisy QASM) with 8192 shots per circuit.
6. **Post-processing**: Estimate observables (e.g., option prices, rare event probabilities) and compute error metrics (bias, RMSE).

### Output
Outputs included:
1. Estimated financial metrics: Option prices (e.g., basket option prices for Black-Scholes), Sharpe ratios, or hitting times.
2. Molecular dynamics metrics: Rare event probabilities (e.g., barrier crossing in Langevin dynamics).
3. Error metrics: Bias (|quantum estimate - classical reference|), RMSE, and circuit metrics (depth, two-qubit gate count).
4. Speedup comparisons: Empirical speedups (e.g., 3x for Black-Scholes, 100x for Langevin) relative to classical Monte Carlo for fixed accuracy or runtime.

### Parameters
- qubits: 10-150 qubits (e.g., 10 qubits for 2D Black-Scholes, ~150 qubits for d=10 assets with ε=10⁻³, δx=10⁻²).
- circuit_depth: ˜O(poly(d) log(1/ε)) (e.g., polynomial in dimension and logarithmic in accuracy).
- shots: 8192
- time_steps: nt = ˜O(polylog(1/ε)) (e.g., O(log(1/ε)) for high-order integrators).
- optimizer: Layer-wise training for variational schemes (no specific classical optimizer named).
- learning_rate: Not specified.
- discretization: δx = Θ(ε/Lf) for spatial discretization, where Lf is the Lipschitz constant of the payoff function.
- noise_model: IBM heavy-hex device noise model (error rates: 10⁻⁴ for single-qubit gates, 10⁻³ for two-qubit gates).

### Hardware
Simulations were run on Qiskit Aer statevector and noisy QASM simulators. Noise models were calibrated to IBM heavy-hex devices (e.g., 27-qubit layouts). Transpilation was performed at optimization level 2 with basis gates {u3, cx}.

### Reproducibility
The paper provides sufficient theoretical detail for replication, including proofs, ansatz designs, and parameter choices. Numerical simulations were conducted using Qiskit, but the code is not explicitly linked or made available in the preprint. Data is synthetic, so no external datasets are required. The appendix includes detailed assumptions, discretization schemes, and proof sketches, enhancing reproducibility.
