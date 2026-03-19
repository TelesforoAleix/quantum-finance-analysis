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
journal_or_venue: ''
methodology_tags:
- quantum-simulation
- amplitude-estimation
- variational
- Hamiltonian-simulation
- quantum-ML
paper_type: ''
quantum_advantage_claim: speculative
related_papers: []
relevance_phase1: high
relevance_phase3: high
source_type: preprint
source_type_confidence: high
step1_date: '2026-03-18T22:19:08.669710'
step1_model: Mistral-Large-3
step2_date: '2026-03-18T22:19:11.371383'
step2_model: Mistral-Large-3
step3_date: '2026-03-18T22:19:19.413671'
step3_model: Mistral-Large-3
step4_date: '2026-03-18T22:19:29.133784'
step4_model: Mistral-Large-3
step5_date: ''
step5_model: ''
step6_date: '2026-03-18T22:19:45.705497'
step6_model: Mistral-Large-3
steps_completed:
- 1
- 2
- 3
- 4
- 6
tags:
- topic/derivatives-pricing
- topic/asset-pricing
- topic/market-simulation
- method/quantum-simulation
- method/amplitude-estimation
- method/variational
- method/Hamiltonian-simulation
- method/quantum-ML
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
This preprint introduces quantum algorithms for simulating and solving stochastic differential equations (SDEs), which are critical in finance, chemistry, and climate science. The paper addresses the exponential computational cost of classical methods by leveraging quantum primitives like Hamiltonian simulation, quantum random number generation, and amplitude estimation. It demonstrates polynomial and super-polynomial speedups for linear, semilinear, and nonlinear SDEs, with applications to multi-asset pricing models, stochastic volatility, and molecular dynamics.
## Methodology
The paper presents a comprehensive framework for solving stochastic differential equations (SDEs) using quantum algorithms, targeting applications in quantitative finance, molecular dynamics, and other fields. The methodology combines Hamiltonian simulation for drift terms, quantum random number generation for noise increments, and quantum amplitude estimation for computing expectations. For linear and semilinear SDEs, the authors prove polynomial and super-polynomial speedups over classical methods, achieving accuracy ε in time ˜O(poly(d)polylog(1/ε)) compared to classical O(poly(d)/ε²). For nonlinear SDEs, variational quantum schemes with parameterized circuits are introduced, incorporating barren plateau mitigation strategies such as problem-informed ansätze, shallow circuits, layer-wise training, and local cost functions. The paper includes theoretical proofs for quantum speedups, resource quantification (qubits, gate depth, oracle calls), and numerical simulations on small-scale instances using Qiskit to demonstrate empirical speedups in accuracy for fixed runtime.

**Algorithms used:** Hamiltonian simulation, Quantum random number generation, Quantum amplitude estimation, Trotter-Suzuki decomposition, Linear combination of unitaries (LCU), Variational quantum eigensolver (implicit in variational schemes), Maximum-likelihood amplitude estimation
**Frameworks:** Qiskit

**Experimental setup:** Numerical simulations were conducted using Qiskit Terra 0.46 and Aer 0.15 on a classical backend with noise models calibrated to IBM heavy-hex devices. The experiments utilized basis gates {u3, cx} with average one- and two-qubit error rates of 10⁻⁴ and 10⁻³, respectively. Simulations were run on both statevector and noisy QASM simulators, with shot counts of 8192 per circuit. The setup included transpilation at optimization level 2 and layout restrictions to 27-qubit heavy-hex graphs. Small-scale instances of 2D Black-Scholes (10 qubits) and 3D Langevin dynamics were tested to validate theoretical speedups.

**Dataset:** The paper does not use a specific external dataset but focuses on synthetic financial models and molecular dynamics simulations. Financial applications include multi-asset Black-Scholes models (geometric Brownian motion for correlated assets), Heston stochastic volatility models, and Langevin dynamics for molecular coarse-graining (e.g., protein coarse-grained models with 3 beads). The datasets are generated internally based on these models.
## Findings
- [supported] Quantum algorithms for linear and semilinear SDEs with Lipschitz coefficients achieve complexity ˜O(poly(d)polylog(1/ε)) for estimating expectations (e.g., option prices), compared to classical O(poly(d)/ε²).
- [supported] For the Fokker-Planck equation associated with SDEs, quantum simulation via Schrödingerization achieves accuracy ε in time ˜O(d · log(1/ε)), versus classical O(nd+1_s) for spatial grid size ns.
- [speculative] Variational quantum schemes for nonlinear SDEs can avoid barren plateaus using problem-informed ansätze, shallow circuits (L = O(log d)), and layer-wise training, with a priori error bounds scaling as O(1/√p + hardware noise · L).
- [supported] Numerical simulations on small-scale instances (e.g., 2D Black-Scholes, 3D Langevin) demonstrate polynomial-to-super-polynomial empirical speedups in accuracy for fixed runtime, with up to 100x speedup in sampling rare events.
- [speculative] Quantum advantage for SDE solving may emerge on near-term NISQ devices for high-dimensional problems (d = 10–100) in finance (e.g., multi-asset option pricing) and molecular dynamics (e.g., rare event sampling).
- [speculative] Hybrid classical-quantum approaches combining quantum noise sampling with classical PDE solvers could reduce quantum resource requirements while maintaining speedups.
- [supported] Resource requirements for d-dimensional SDEs with accuracy ε are quantified: ~150 qubits for d=10, ε=10⁻³, and gate depth ˜O(poly(d) log(1/ε)).
- [disputed] The claimed super-polynomial speedups for Langevin dynamics (exponential in rare event sampling) may be contested due to assumptions about noise resilience and state preparation fidelity on NISQ hardware.

**Results summary:** The preprint presents a quantum framework for solving stochastic differential equations (SDEs) with demonstrated polynomial and super-polynomial speedups over classical methods. For linear and semilinear SDEs, the authors prove quantum complexity advantages (˜O(poly(d)polylog(1/ε)) vs. classical O(poly(d)/ε²)) and validate these claims via numerical simulations on small-scale problems (e.g., 2D Black-Scholes, 3D Langevin dynamics). Variational schemes for nonlinear SDEs are proposed with theoretical error bounds and barren plateau mitigation strategies. While empirical results show promising speedups (e.g., 3x–100x in specific cases), the quantum advantage claims remain speculative for large-scale problems due to reliance on simulations and untested assumptions about NISQ hardware capabilities.

**Performance claims:**
- ˜O(poly(d)polylog(1/ε)) quantum complexity vs. classical O(poly(d)/ε²) for linear SDEs (Theorem 1)
- ˜O(d · log(1/ε)) quantum complexity for Fokker-Planck PDEs vs. classical O(nd+1_s)
- 3x speedup for 2D Black-Scholes (10 qubits) in simulated runtime vs. classical Monte Carlo
- 100x speedup in rare event sampling for 3D Langevin dynamics (superpolynomial)
- O(√1/ε) speedup in precision for multi-asset Black-Scholes, independent of dimension
- Quadratic speedup in accuracy for Heston stochastic volatility model (2D system)
## Quantum advantage claim
**Classification:** speculative

The paper claims polynomial and super-polynomial speedups for SDE solving, but these are primarily theoretical or demonstrated via classical simulations. Empirical results on small-scale problems (e.g., 2D/3D) show speedups, but the advantage is not validated on real quantum hardware. The super-polynomial claims for rare event sampling (e.g., Langevin dynamics) are particularly speculative due to noise and scalability challenges on NISQ devices.
## Limitations
<!-- Step 5 output — author-stated + [inferred] limitations -->

## Open questions
<!-- Step 5 output -->

## Key ideas
- #idea:quantum-advantage — Quantum algorithms achieve polynomial and super-polynomial speedups for solving stochastic differential equations (SDEs) in finance, with complexity ˜O(poly(d)polylog(1/ε)) vs. classical O(poly(d)/ε²).
- #idea:quantum-advantage — Quantum amplitude estimation and Hamiltonian simulation enable O(√1/ε) speedup in precision for multi-asset Black-Scholes and Heston stochastic volatility models.
- #idea:near-term-feasibility — Variational quantum schemes for nonlinear SDEs propose barren plateau mitigation strategies (e.g., problem-informed ansätze, shallow circuits) to enable NISQ-era applicability.
- #idea:hybrid-approach — Hybrid classical-quantum approaches combining quantum noise sampling with classical PDE solvers could reduce quantum resource requirements while maintaining speedups.
- #idea:quantum-advantage — Numerical simulations demonstrate 3x–100x speedups in accuracy for fixed runtime on small-scale financial models (e.g., 2D Black-Scholes, 3D Langevin dynamics).
## Contradictions
- #contradiction:scalability — The paper claims super-polynomial speedups for rare event sampling in Langevin dynamics, but these are disputed due to untested assumptions about noise resilience and state preparation fidelity on NISQ hardware. This contradicts prior work (e.g., on quantum Monte Carlo limitations) highlighting scalability challenges for high-dimensional problems.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
