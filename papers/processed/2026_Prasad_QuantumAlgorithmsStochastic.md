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
step1_date: '2026-03-19T14:14:40.616559'
step1_model: Mistral-Large-3
step2_date: '2026-03-19T14:14:47.381442'
step2_model: Mistral-Large-3
step3_date: '2026-03-19T14:15:03.079729'
step3_model: Mistral-Large-3
step4_date: '2026-03-19T14:15:22.092424'
step4_model: Mistral-Large-3
step5_date: '2026-03-19T14:15:38.807368'
step5_model: Mistral-Large-3
step6_date: '2026-03-19T14:15:45.640775'
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
- topic/risk-modelling
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
- risk-modelling
- asset-pricing
- market-simulation
year: 2026
zotero_key: ''
---

## Abstract summary
This preprint introduces a framework of quantum algorithms designed to simulate and solve stochastic differential equations (SDEs) with improved computational scaling compared to classical methods. The paper targets high-dimensional systems common in finance, molecular dynamics, and climate science, where classical solvers face exponential cost growth. It combines Hamiltonian simulation, quantum random number generation, and amplitude estimation to achieve polynomial and super-polynomial speedups for estimating expectations, option prices, and rare event probabilities. The work also addresses nonlinear SDEs through variational quantum schemes, providing theoretical error bounds and practical resource estimates for near-term quantum hardware.
## Methodology
The paper presents a comprehensive framework for solving stochastic differential equations (SDEs) using quantum algorithms, targeting applications in finance, molecular dynamics, and other fields. The methodology combines Hamiltonian simulation for drift terms, quantum random number generation for noise increments, and quantum amplitude estimation for computing expectations. For linear and semilinear SDEs, the authors provide theoretical proofs demonstrating polynomial and super-polynomial speedups over classical methods, achieving complexity of ˜O(poly(d)polylog(1/ε)) versus classical O(poly(d)/ε²). For nonlinear SDEs, variational quantum schemes with parameterized circuits are introduced, incorporating a priori error bounds and strategies to mitigate barren plateaus. The paper includes concrete applications such as multi-asset Black-Scholes models, Heston stochastic volatility, and Langevin dynamics, with resource quantification for qubits, gate depth, and oracle calls. Numerical simulations are conducted using Qiskit to validate the theoretical speedups on small-scale instances, demonstrating empirical advantages in accuracy for fixed runtime.

**Algorithms used:** Hamiltonian simulation, Quantum Random Number Generation (QRNG), Quantum Amplitude Estimation, Trotter-Suzuki decomposition, Linear Combination of Unitaries (LCU), Variational Quantum Eigensolver (implicit in variational schemes), Schrödingerization method for Fokker-Planck PDEs
**Frameworks:** Qiskit

**Experimental setup:** Numerical simulations were performed using Qiskit Terra 0.46 and Aer 0.15 on classical backends with noise models calibrated to IBM heavy-hex devices. The experiments utilized basis gates {u3, cx} with average one- and two-qubit error rates of 10⁻⁴ and 10⁻³, respectively. Simulations were transpiled at optimization level 2 and restricted to 27-qubit heavy-hex graphs. Shot counts of 8192 per circuit were used for statistical estimation. Small-scale instances of 2D Black-Scholes (10 qubits) and 3D Langevin dynamics (3 beads) were tested, comparing quantum algorithm performance against classical Monte Carlo methods.

**Dataset:** The paper does not specify explicit datasets but focuses on synthetic financial models and molecular dynamics simulations. Applications include multi-asset Black-Scholes models (basket options with correlated geometric Brownian motion), Heston stochastic volatility models, and Langevin dynamics for coarse-grained molecular systems (e.g., protein models).
## Findings
- [speculative] Quantum algorithms for simulating and solving stochastic differential equations (SDEs) can achieve polynomial and super-polynomial speedups over classical methods for high-dimensional systems
- [supported] For linear and semilinear SDEs with Lipschitz coefficients, quantum algorithms can estimate relevant quantities (option prices, expected hitting times, moments) to accuracy ε in time ˜O(poly(d) polylog(1/ε)), versus classical O(poly(d)/ε²)
- [speculative] Quantum advantage may emerge for high-dimensional option pricing (d=10-100) and rare event sampling in molecular dynamics without requiring fault-tolerant quantum computers
- [supported] Numerical simulations on small instances (e.g., 2D Black-Scholes with 10 qubits) demonstrate polynomial-to-super-polynomial empirical speedups in accuracy for fixed runtime
- [speculative] Variational quantum schemes for nonlinear SDEs can avoid barren plateaus through problem-informed ansätze, shallow circuits, and layer-wise training
- [supported] Theorem 1 proves a quantum complexity of ˜O(poly(d) polylog(1/ε)) for estimating expectations in linear SDEs, compared to classical O(poly(d)/ε²)
- [supported] Theorem 2 shows quantum simulation of Fokker-Planck PDEs achieves accuracy ε in time ˜O(d·log(1/ε)), versus classical O(n^(d+1)) for spatial grid size n
- [speculative] Resource requirements for d=10 assets, ε=10⁻³, and δx=10⁻² are estimated at ~150 qubits, which may be feasible on near-term hardware with error mitigation
- [supported] Simulated quantum algorithms for 2D Black-Scholes show ~3x speedup over classical Monte Carlo for 0.1% accuracy, with estimated 10-20x speedup on real hardware
- [supported] Quantum simulation of Langevin dynamics for 3D coarse-grained systems shows ~100x speedup in sampling rare events due to superposition over trajectories
- [speculative] Hybrid classical-quantum approaches combining quantum noise sampling with classical PDE solvers could reduce quantum resource requirements while maintaining speedups

**Results summary:** The preprint presents a comprehensive quantum framework for solving SDEs, demonstrating theoretical polynomial and super-polynomial speedups over classical methods for linear, semilinear, and nonlinear SDEs. Key results include Theorem 1 (quantum complexity ˜O(poly(d) polylog(1/ε)) vs. classical O(poly(d)/ε²)) and Theorem 2 (Fokker-Planck PDE speedup via Schrödingerization). Numerical simulations on small-scale instances (2D Black-Scholes, 3D Langevin) show empirical speedups, though these are limited by simulation overhead. The work introduces variational schemes for nonlinear SDEs with barren plateau mitigation and quantifies resource requirements for financial and molecular dynamics applications. While theoretical advantages are rigorously proven, empirical validation remains preliminary and hardware-limited.

**Performance claims:**
- Quantum algorithm for linear SDEs: ˜O(poly(d) polylog(1/ε)) vs. classical O(poly(d)/ε²)
- Quantum Fokker-Planck PDE solver: ˜O(d·log(1/ε)) vs. classical O(n^(d+1))
- 2D Black-Scholes simulation: ~3x speedup over classical Monte Carlo for 0.1% accuracy (simulated)
- Estimated 10-20x speedup for 2D Black-Scholes on real hardware
- 3D Langevin dynamics: ~100x speedup in rare event sampling (simulated)
- Qubit requirement: ~150 qubits for d=10 assets, ε=10⁻³, δx=10⁻²
- Gate depth: ˜O(poly(d) log(1/ε)) for full SDE simulation
## Quantum advantage claim
**Classification:** speculative

The paper proves theoretical quantum speedups for SDE solving (polynomial and super-polynomial in dimension/accuracy) and demonstrates empirical speedups in simulations. However, all numerical results are from classical simulations of quantum algorithms, not real hardware. The claimed advantage is classified as speculative because: (1) hardware limitations (noise, qubit count) may prevent realization of theoretical speedups, (2) empirical validation is limited to small-scale instances, and (3) practical deployment on NISQ devices would require error mitigation not fully addressed in the preprint.
## Limitations
- Preprint status: The paper has not been peer-reviewed, which may affect the rigor and validity of the findings [inferred]
- Small-scale numerical simulations: Experiments were limited to small instances (e.g., 2D Black-Scholes with 10 qubits, 3D Langevin dynamics), which may not generalize to higher-dimensional systems
- Simulated quantum hardware: Results are based on Qiskit simulations with noise models, not real quantum hardware, limiting practical validation [inferred]
- Noise sensitivity: The paper acknowledges that current NISQ devices have high error rates (10^-3 to 10^-2 per gate), which could degrade performance for deep circuits (Depth > 1000) [inferred]
- Discretization assumptions: The theoretical results rely on state space truncation and discretization (e.g., hypercube [-R, R]^d with spacing δx), which may introduce bias or limit applicability to unbounded systems [inferred]
- Lipschitz and boundedness assumptions: The speedup proofs assume Lipschitz coefficients and bounded spectral norms for SDEs, which may not hold for all financial models (e.g., rough volatility models) [inferred]
- Variational ansatz limitations: The error bounds for variational schemes (Error_var = O(1/√p + hardware noise · L)) depend on trainable parameters and circuit depth, which may not scale well for large systems [inferred]
- Barren plateau mitigation: While the paper proposes layer-wise training and shallow circuits to avoid barren plateaus, empirical validation is limited to small-scale examples [inferred]
- Resource requirements: The paper estimates ~150 qubits for a 10-asset Black-Scholes model with ε=10^-3, which exceeds current quantum hardware capabilities [inferred]
- Oracle implementation: The theoretical complexity assumes efficient oracle implementations for drift and payoff functions, which may not be straightforward in practice [inferred]
- Hybrid approach reliance: The proposed hybrid classical-quantum approaches (e.g., quantum noise sampling + classical PDE solvers) may introduce integration challenges and overhead [inferred]
- Lack of comparison with state-of-the-art classical methods: The paper does not benchmark against advanced classical SDE solvers (e.g., multilevel Monte Carlo, quasi-Monte Carlo) [inferred]
## Open questions
- How do the proposed quantum algorithms perform on real quantum hardware with higher qubit counts and lower error rates?
- What is the impact of noise and decoherence on the accuracy of the quantum SDE solvers for larger problem instances?
- Can the variational schemes for nonlinear SDEs avoid barren plateaus in practice for high-dimensional systems (d > 100)?
- How do the quantum algorithms compare to state-of-the-art classical methods (e.g., multilevel Monte Carlo) in terms of runtime and accuracy for practical financial applications?
- What are the practical challenges in implementing the required oracles for drift and payoff functions on near-term quantum devices?
- How sensitive are the quantum speedups to violations of the Lipschitz and boundedness assumptions in real-world financial models?
- Can the proposed error mitigation techniques (e.g., selective quantum error correction) effectively reduce noise-induced errors in deep circuits?
- What are the trade-offs between circuit depth, qubit count, and accuracy for the variational quantum schemes?
- How do the quantum algorithms perform for SDEs with non-Gaussian noise or jumps (e.g., Lévy processes)?
- What is the minimum qubit count and gate fidelity required to achieve a practical advantage over classical methods for multi-asset option pricing?

**Future work:**
- Test the algorithms on real quantum hardware (e.g., IBM Eagle or Osprey processors) to validate performance under noise and decoherence
- Extend the framework to handle non-Lipschitz SDEs (e.g., rough volatility models) and non-Gaussian noise processes
- Develop more efficient oracle implementations for drift and payoff functions to reduce resource requirements
- Benchmark the quantum algorithms against advanced classical methods (e.g., multilevel Monte Carlo, quasi-Monte Carlo) for large-scale financial applications
- Explore hybrid quantum-classical approaches that combine quantum noise sampling with classical PDE solvers for drift terms
- Investigate the use of quantum error correction and error mitigation techniques to improve the robustness of the algorithms on NISQ devices
- Apply the quantum SDE framework to other domains (e.g., climate science, molecular dynamics) with high-dimensional systems
- Develop variational ansätze tailored to specific financial models (e.g., Heston, SABR) to improve trainability and avoid barren plateaus
- Optimize the circuit compilation and transpilation process to reduce gate depth and improve hardware compatibility
- Explore the use of quantum machine learning techniques to learn optimal ansätze for SDE simulation
## Key ideas
- #idea:quantum-advantage — Quantum algorithms achieve polynomial and super-polynomial speedups for solving stochastic differential equations (SDEs) in finance, with complexity ˜O(poly(d)polylog(1/ε)) vs. classical O(poly(d)/ε²).
- #idea:quantum-advantage — Quantum amplitude estimation and Hamiltonian simulation enable O(√1/ε) speedup in precision for multi-asset Black-Scholes and Heston stochastic volatility models.
- #idea:near-term-feasibility — Variational quantum schemes for nonlinear SDEs propose barren plateau mitigation strategies (e.g., problem-informed ansätze, shallow circuits) to enable NISQ-era applicability.
- #idea:hybrid-approach — Hybrid classical-quantum approaches combining quantum noise sampling with classical PDE solvers could reduce quantum resource requirements while maintaining speedups.
- #idea:quantum-advantage — Numerical simulations demonstrate 3x–100x speedups in accuracy for fixed runtime on small-scale financial models (e.g., 2D Black-Scholes, 3D Langevin dynamics).
## Contradictions
- #contradiction:scalability — The paper claims super-polynomial speedups for rare event sampling in Langevin dynamics, but these are disputed due to untested assumptions about noise resilience and state preparation fidelity on NISQ hardware. This contradicts prior work highlighting scalability challenges for high-dimensional problems.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
