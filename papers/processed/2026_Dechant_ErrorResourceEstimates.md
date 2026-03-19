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
- classical-simulation
paper_type: ''
quantum_advantage_claim: speculative
related_papers: []
relevance_phase1: high
relevance_phase3: medium
source_type: preprint
source_type_confidence: high
step1_date: '2026-03-19T14:01:01.576140'
step1_model: Mistral-Large-3
step2_date: '2026-03-19T14:01:07.152630'
step2_model: Mistral-Large-3
step3_date: '2026-03-19T14:01:15.316104'
step3_model: Mistral-Large-3
step4_date: '2026-03-19T14:01:35.370729'
step4_model: Mistral-Large-3
step5_date: '2026-03-19T14:01:58.876861'
step5_model: Mistral-Large-3
step6_date: '2026-03-19T14:03:40.539462'
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
- method/classical-simulation
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
This preprint presents a rigorous error and resource analysis of variational quantum algorithms (VQAs) for solving differential equations using Runge-Kutta methods. The authors focus on quantifying error sources—such as shot noise in quantum measurements and truncation errors in classical numerical methods—and derive analytical estimates for the computational resources required to achieve specific target errors. The work applies these estimates to benchmark scenarios, including solving a 1D ordinary differential equation and pricing options via the Black-Scholes partial differential equation, demonstrating that higher-order Runge-Kutta methods can optimize quantum resource efficiency depending on the problem context.
## Methodology
The paper presents a theoretical and analytical framework for evaluating error and resource estimates of variational quantum algorithms (VQAs) used to solve differential equations (DEs) based on Runge-Kutta methods (RKMs). The study focuses on hybrid quantum-classical algorithms that integrate classical RKMs with quantum computations to solve DEs, particularly in the context of Noisy Intermediate-Scale Quantum (NISQ) devices. The methodology involves deriving analytical error bounds for the total error in solving DEs using RKMs, considering both truncation errors from the RKMs and shot noise errors from quantum measurements. The authors analyze the error propagation and resource requirements for achieving a specified target error, both in scenarios with and without shot noise. The variational quantum algorithm is applied to two specific use cases: solving a 1D ordinary differential equation (ODE) and pricing options via the Black-Scholes partial differential equation (PDE). The analysis provides a framework for optimizing quantum resources by selecting the most efficient RKM order for specific problems, thereby enhancing the efficiency and accuracy of quantum simulations of DEs.

**Algorithms used:** Variational Quantum Eigensolver (VQE), Runge-Kutta Methods (RKMs)

**Experimental setup:** The experimental analysis is conducted through numerical simulations rather than on actual quantum hardware. The setup involves estimating errors and resource requirements for solving differential equations using variational quantum algorithms combined with Runge-Kutta methods. The quantum circuits for evaluating matrix elements of the variational algorithm are simulated, accounting for shot noise in quantum measurements. The simulations focus on two scenarios: a simple 1D ODE and an option pricing problem modeled by the Black-Scholes PDE. The resource estimates are derived based on the number of quantum circuit evaluations required to achieve a specified target error.

**Dataset:** The paper applies the methodology to two specific financial and mathematical scenarios: (1) a simple 1D ordinary differential equation (ODE) for benchmarking without shot noise, and (2) an option pricing problem using the Black-Scholes partial differential equation (PDE), which is a linear PDE commonly used in financial services for pricing options.
## Findings
- [supported] The paper provides rigorous error and resource estimates for variational quantum algorithms (VQAs) solving differential equations (DEs) using Runge-Kutta methods (RKMs), accounting for truncation errors and shot noise in quantum measurements.
- [supported] Higher-order RKMs (e.g., order 4 for a 1D ODE and order 2 for option pricing via the Black-Scholes equation) minimize the total number of quantum circuit evaluations required to achieve a target error.
- [supported] The total error in VQAs for solving DEs is bounded by the sum of the parameter error (from RKM truncation and shot noise) and the representation error (from the quantum ansatz), with the former analyzed in detail.
- [speculative] The authors suggest that higher-order RKMs may outperform the Euler method in variational quantum algorithms for solving DEs, depending on problem-specific parameters, but this claim is not empirically validated on real hardware.
- [supported] The number of quantum circuit evaluations scales quadratically with the number of variational parameters (NV), highlighting a significant resource bottleneck for large-scale problems.
- [supported] The paper derives analytical bounds for the local truncation error (LTE) of RKMs, showing that the LTE scales as O(Δτ^(p+1)) for a p-th order RKM, where Δτ is the time step size.
- [speculative] Quantum advantage for solving DEs using VQAs is not demonstrated in this work; all results are based on simulations and theoretical error bounds, with no empirical validation on real quantum hardware.
- [supported] The shot noise error in quantum measurements scales as O(1/√N_meas), where N_meas is the number of measurements, and the paper provides a framework to minimize this error for a given target accuracy.
- [speculative] The authors claim that their framework can be applied to other use cases involving DEs, such as quantum simulations, but this is not empirically validated in the paper.

**Results summary:** The paper presents a comprehensive theoretical analysis of error sources and resource requirements for variational quantum algorithms (VQAs) solving differential equations (DEs) using Runge-Kutta methods (RKMs). The authors derive analytical error bounds for both truncation errors (from RKMs) and shot noise errors (from quantum measurements), demonstrating that higher-order RKMs can reduce the total number of quantum circuit evaluations needed to achieve a specified target error. Specifically, they show that for a 1D ordinary differential equation (ODE), a 4th-order RKM is most resource-efficient, while for option pricing via the Black-Scholes equation, a 2nd-order RKM is optimal. The paper also highlights the quadratic scaling of quantum circuit evaluations with the number of variational parameters, underscoring the resource-intensive nature of VQAs. While the analysis is rigorous and simulation-based, the work does not demonstrate quantum advantage on real hardware, and all claims of practical applicability remain speculative.

**Performance claims:**
- For a 1D ODE, a 4th-order RKM minimizes the total number of quantum circuit evaluations.
- For option pricing via the Black-Scholes equation, a 2nd-order RKM minimizes the total number of quantum circuit evaluations.
- The shot noise error scales as O(1/√N_meas), where N_meas is the number of measurements.
- The total error in VQAs is bounded by the sum of parameter error (from RKM truncation and shot noise) and representation error (from the quantum ansatz).
- The number of quantum circuit evaluations scales quadratically with the number of variational parameters (NV).
## Quantum advantage claim
**Classification:** speculative

The paper does not demonstrate quantum advantage for solving differential equations using variational quantum algorithms. All results are derived from theoretical error bounds and simulations, with no empirical validation on real quantum hardware. The authors suggest potential efficiency gains from higher-order RKMs, but these claims are not supported by experimental evidence.
## Limitations
- Lack of peer review as this is a preprint [inferred]
- Error analysis does not account for representation errors, which are specific to the chosen Ansatz and problem instance
- Hardware noise (e.g., gate infidelity, SPAM errors) is assumed to be negligible, which may not hold on NISQ devices
- Assumes the matrix A (Eq. 24) is invertible; singular cases require regularization, introducing additional errors not analyzed
- Circuit errors (e.g., bias, gate infidelity) are disregarded, limiting applicability to real-world quantum hardware
- Analysis focuses on linear differential equations (Eq. 10), excluding non-linear or non-Hermitian cases without explicit transformations
- Resource estimates are based on upper bounds, which may be overly conservative in practice
- Shot noise analysis assumes Gaussian distribution of measurement errors, which may not capture all noise sources on NISQ devices
- Toy model used for estimating condition numbers and norms (Sec. V.C) may not generalize to all variational Ansätze
- Lipschitz constant (L_fy) estimation relies on a toy model, which may not reflect real-world variational algorithm behavior
- No empirical validation of the proposed framework on real quantum hardware or large-scale financial use cases (e.g., option pricing)
- Scalability to higher-dimensional problems (e.g., multi-asset portfolios) is not demonstrated beyond theoretical bounds
- Assumes parallel evaluation of circuits to reduce runtime, which may not be feasible on current quantum hardware
- Error bounds for regularization techniques (e.g., matrix inversion) are not quantified, limiting practical applicability
## Open questions
- How do representation errors (from limited Ansatz expressivity) impact the total error (ε_total) in real-world applications?
- What is the trade-off between higher-order Runge-Kutta methods (RKMs) and quantum resource requirements for non-linear differential equations?
- How does hardware noise (e.g., decoherence, gate errors) affect the performance of the proposed variational algorithm on NISQ devices?
- Can the framework be extended to non-Hermitian Hamiltonians without doubling the number of circuit evaluations?
- What is the minimal qubit count required to achieve a quantum advantage for financial differential equations (e.g., Black-Scholes)?
- How does the choice of Ansatz (e.g., hardware-efficient vs. problem-specific) influence the Lipschitz constant (L_fy) and resource estimates?
- What are the implications of shot noise for multi-period financial models (e.g., dynamic portfolio optimization)?
- How do the derived error bounds compare to empirical results on real quantum hardware for option pricing or other financial use cases?
- What is the impact of discretization errors when mapping partial differential equations (PDEs) to the variational algorithm?
- Can the proposed framework be adapted to stochastic differential equations (SDEs) without significant increases in resource requirements?
- How does the condition number of A scale with the number of variational parameters (N_V) for problem-specific Ansätze?
- What are the limitations of the toy model in capturing the behavior of real variational quantum circuits?

**Future work:**
- Validate the proposed error and resource estimates on real quantum hardware (e.g., IBM Quantum, Rigetti)
- Extend the analysis to non-linear differential equations and non-Hermitian Hamiltonians without doubling circuit evaluations
- Incorporate noise mitigation techniques (e.g., error mitigation, dynamical decoupling) to improve performance on NISQ devices
- Develop adaptive Runge-Kutta methods that dynamically adjust order (p) and stages (s) to minimize quantum resource usage
- Apply the framework to multi-period financial models (e.g., dynamic portfolio optimization, risk management)
- Benchmark the variational algorithm against state-of-the-art classical solvers (e.g., finite difference methods) for financial PDEs
- Explore the use of problem-specific Ansätze to reduce the Lipschitz constant (L_fy) and improve resource efficiency
- Investigate the impact of discretization methods (e.g., spectral methods, finite element) on the accuracy of the variational algorithm
- Develop hybrid quantum-classical algorithms that combine the proposed framework with classical post-processing for error correction
- Analyze the scalability of the framework to higher-dimensional problems (e.g., multi-asset portfolios, high-frequency trading models)
- Study the effects of hardware noise on the performance of the variational algorithm and propose noise-aware RKM selection strategies
- Extend the toy model to better capture the behavior of real variational quantum circuits and improve Lipschitz constant estimates
- Explore the use of alternative numerical methods (e.g., linear multistep methods) to reduce the number of quantum circuit evaluations
- Develop a software toolkit for automating the selection of optimal RKMs and Ansätze for financial differential equations
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
