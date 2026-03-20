---
aliases:
- Error and Resource Estimates of Variational Quantum Algorithms for Solving Differential
  Equations Based on Runge-Kutta Methods
- Error Resource Estimates Variational
authors:
- David Dechant
- Liubov Markovich
- Vedran Dunjko
- Jordi Tura
auto_detected: true
classification: ''
contradiction_flags: []
doi: 10.48550/arXiv.2412.12262
evidence_type: ''
idea_tags:
- idea:near-term-feasibility
- idea:hybrid-approach
journal_or_venue: arXiv
methodology_tags:
- variational
- VQE
- quantum-simulation
paper_type: ''
quantum_advantage_claim: speculative
related_papers: []
relevance_phase1: high
relevance_phase3: high
source_type: preprint
source_type_confidence: high
step1_date: '2026-03-20T00:50:24.909852'
step1_model: Mistral-Large-3
step2_date: '2026-03-20T00:50:29.089660'
step2_model: Mistral-Large-3
step3_date: '2026-03-20T00:50:34.248718'
step3_model: Mistral-Large-3
step4_date: '2026-03-20T00:50:43.667881'
step4_model: Mistral-Large-3
step5_date: '2026-03-20T00:52:16.134374'
step5_model: Mistral-Large-3
step6_date: '2026-03-20T00:52:20.058519'
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
- method/VQE
- method/quantum-simulation
- idea/near-term-feasibility
- idea/hybrid-approach
title: Error and Resource Estimates of Variational Quantum Algorithms for Solving
  Differential Equations Based on Runge-Kutta Methods
topic_tags:
- derivatives-pricing
- asset-pricing
year: 2026
zotero_key: ''
---

## Abstract summary
This preprint presents a rigorous error and resource analysis of variational quantum algorithms (VQAs) for solving differential equations using Runge-Kutta methods. The authors focus on quantifying the trade-offs between truncation errors from classical numerical methods and shot noise from quantum measurements, providing analytical bounds for both. The work applies these estimates to practical scenarios, such as solving ordinary differential equations and option pricing via the Black-Scholes equation, to identify the most resource-efficient Runge-Kutta methods for specific problems. The findings offer a framework for optimizing quantum resource allocation in hybrid quantum-classical algorithms.
## Methodology
The paper presents a theoretical and analytical framework for evaluating error and resource estimates of variational quantum algorithms (VQAs) for solving differential equations (DEs) using Runge-Kutta methods (RKMs). The authors derive rigorous error bounds for the total error arising from solving DEs with RKMs, considering both truncation errors and shot noise in quantum measurements. The methodology involves mapping DEs to an imaginary-time Schrödinger equation and solving them using a variational quantum algorithm. The analysis focuses on two scenarios: solving a classical 1D ordinary differential equation (ODE) and solving an option pricing linear partial differential equation (PDE) using the Black-Scholes model. The paper provides analytical error and resource estimates for RKMs of different orders, both with and without shot noise, and validates these estimates through numerical simulations. The framework aims to optimize quantum resources by selecting the most efficient RKM order for specific problems.

**Algorithms used:** Variational Quantum Eigensolver (VQE), Runge-Kutta Methods (RKMs)
## Findings
- [supported] The paper provides rigorous error and resource estimates for variational quantum algorithms (VQAs) solving differential equations (DEs) using Runge-Kutta methods (RKMs), accounting for truncation errors and shot noise in quantum measurements.
- [supported] Higher-order RKMs (e.g., order 4 for a 1D ODE and order 2 for option pricing via the Black-Scholes equation) minimize the total number of quantum circuit evaluations required to achieve a target error.
- [supported] The total error in VQAs for solving DEs is bounded by the sum of the parameter error (from RKM approximations) and the representation error (from the quantum Ansatz), with the former analyzed in detail.
- [supported] The minimal number of RKM time steps and measurements per function evaluation is derived for both noiseless and shot-noise scenarios, providing a framework for optimizing quantum resource usage.
- [speculative] The authors suggest that higher-order RKMs may outperform lower-order methods (e.g., Euler) in variational quantum algorithms, depending on problem-specific parameters, but this claim is not empirically validated on real hardware.
- [speculative] Quantum advantage for solving DEs with VQAs is implied to be achievable with optimized RKMs, but the claim is defaulted to speculative due to the lack of empirical validation on real quantum devices.
- [supported] The paper demonstrates that the variational quantum algorithm can solve both ordinary and partial differential equations (e.g., Black-Scholes equation) by mapping them to imaginary-time Schrödinger equations.
- [supported] The total number of quantum circuit evaluations scales quadratically with the number of variational parameters (NV), highlighting the resource-intensive nature of VQAs for large-scale problems.

**Results summary:** The paper presents a comprehensive analysis of error sources and resource requirements for variational quantum algorithms (VQAs) solving differential equations (DEs) using Runge-Kutta methods (RKMs). It derives analytical error bounds for both noiseless and shot-noise scenarios, demonstrating that higher-order RKMs can minimize the total number of quantum circuit evaluations for specific target errors. The analysis is applied to two use cases: a 1D ordinary differential equation (ODE) and option pricing via the Black-Scholes partial differential equation (PDE). The results show that RKMs of order 4 and 2 are most resource-efficient for these cases, respectively. The paper also provides a framework for optimizing quantum resources, though all findings are based on simulations and theoretical estimates rather than real hardware experiments.

**Performance claims:**
- For a 1D ODE, an RKM of order 4 minimizes the total number of quantum circuit evaluations.
- For option pricing via the Black-Scholes equation, an RKM of order 2 minimizes the total number of quantum circuit evaluations.
- The total error in VQAs is bounded by the sum of parameter error (from RKM approximations) and representation error (from the quantum Ansatz).
- The minimal number of RKM time steps (Nτ) and measurements per function evaluation (Nr) is derived for target errors in both noiseless and shot-noise scenarios.
- The total number of quantum circuit evaluations scales as O(NV^2), where NV is the number of variational parameters.
## Quantum advantage claim
**Classification:** speculative

The paper suggests that optimized RKMs in VQAs could lead to quantum advantage for solving DEs, but this claim is speculative as it is based on theoretical error and resource estimates without empirical validation on real quantum hardware. The analysis does not demonstrate a clear quantum advantage over classical methods.
## Limitations
- Lack of peer review as this is a preprint [inferred]
- Error analysis does not account for representation errors, which are specific to the chosen Ansatz and problem instance
- Hardware noise (e.g., gate infidelity, bias, SPAM errors) is assumed negligible, which may not hold on NISQ devices
- Assumes the matrix A (Eq. 24) is invertible; singular cases require regularization, introducing additional errors not analyzed
- Shot noise analysis relies on Gaussian approximations via the central limit theorem, which may not hold for small sample sizes
- Error bounds derived are upper bounds and may overestimate true errors, leading to overly conservative resource estimates
- Analysis excludes circuit errors (e.g., gate infidelities) and representation errors, limiting practical applicability
- Toy model for estimating condition numbers and norms (Sec. V.C) may not generalize to all variational quantum algorithms
- Lipschitz constant (Lfy) estimation is sensitive to Ansatz parameters and may vary significantly across problem instances
- Resource estimates (e.g., Ncirc) scale quadratically with the number of variational parameters (NV), limiting scalability
- Assumes Hamiltonian H is Hermitian; non-Hermitian cases require additional transformations or circuit evaluations, increasing complexity
- No empirical validation on real quantum hardware, only numerical simulations for specific ODEs and PDEs (e.g., Black-Scholes)
## Open questions
- How do representation errors (from limited Ansatz expressivity) quantitatively impact the total error (εtotal) in practical applications?
- What is the trade-off between higher-order Runge-Kutta methods (reducing truncation error) and increased quantum resource demands (e.g., circuit evaluations)?
- How do hardware noise sources (e.g., decoherence, gate errors) interact with shot noise and truncation errors in variational quantum algorithms?
- Can the condition number (κ(A)) and Lipschitz constant (Lfy) be bounded more tightly for specific Ansätze or problem classes?
- What are the implications of non-invertible matrices A in practice, and how do regularization techniques affect error bounds?
- How does the choice of norm (e.g., trace norm vs. Euclidean norm) influence error propagation and resource estimates?
- What is the minimal number of qubits required to achieve a practical advantage over classical methods for solving differential equations in finance?
- How do the error and resource estimates change for non-linear differential equations or stochastic differential equations?
- Can noise mitigation techniques (e.g., error mitigation, dynamical decoupling) reduce the impact of shot noise and hardware errors?
- What are the computational overheads of parallelizing circuit evaluations to reduce runtime, and how does this affect error bounds?

**Future work:**
- Empirical validation of error and resource estimates on real quantum hardware (e.g., IBM, Rigetti, or IonQ devices)
- Extension of analysis to include representation errors and circuit noise, providing more realistic error bounds
- Development of adaptive Runge-Kutta methods that dynamically adjust order (p) and step size (Δτ) to minimize resource usage
- Investigation of alternative numerical methods (e.g., linear multistep methods) for solving ODEs in variational quantum algorithms
- Application of the framework to other financial use cases (e.g., risk analysis, Monte Carlo simulations) beyond option pricing
- Exploration of hybrid quantum-classical approaches to mitigate shot noise and hardware errors (e.g., classical post-processing)
- Development of Ansätze tailored to specific differential equations (e.g., Black-Scholes) to reduce representation errors
- Analysis of the impact of non-Hermitian Hamiltonians on error bounds and resource requirements
- Benchmarking against state-of-the-art classical solvers (e.g., finite difference methods) to identify quantum advantage thresholds
- Extension of the framework to partial differential equations (PDEs) with higher dimensionality or non-linearities
- Optimization of variational parameters (e.g., NV, Nd) to balance expressivity and resource demands
- Integration of error mitigation techniques (e.g., zero-noise extrapolation) to improve solution accuracy on NISQ devices
## Key ideas
- #idea:near-term-feasibility — Framework provides error and resource estimates for variational quantum algorithms solving differential equations (e.g., Black-Scholes) on near-term devices, addressing NISQ-era applicability
- #idea:hybrid-approach — Hybrid quantum-classical approach combines classical Runge-Kutta methods with quantum computations to optimize resource efficiency for financial PDEs like Black-Scholes
- #idea:near-term-feasibility — Higher-order Runge-Kutta methods (e.g., order 4 for ODEs, order 2 for option pricing) minimize quantum circuit evaluations for target accuracy, improving practical feasibility
- #limitation:noise — Theoretical analysis excludes hardware noise and representation errors, assuming ideal conditions that may not hold on NISQ devices
- #limitation:no-empirical-validation — Claims about resource efficiency and error bounds lack empirical validation on real quantum hardware, limiting practical confidence
- #limitation:simulation-only — All results are derived from classical simulations, not real quantum processing units (QPUs), restricting real-world applicability
## Contradictions
<!-- Step 6 output — where this paper contradicts others -->

## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
