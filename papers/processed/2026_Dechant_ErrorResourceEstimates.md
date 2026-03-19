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
relevance_phase1: medium
relevance_phase3: not-yet-assessed
source_type: preprint
source_type_confidence: high
step1_date: '2026-03-18T23:18:54.657242'
step1_model: Mistral-Large-3
step2_date: '2026-03-18T23:18:58.222235'
step2_model: Mistral-Large-3
step3_date: '2026-03-18T23:19:51.778393'
step3_model: Mistral-Large-3
step4_date: '2026-03-18T23:19:59.477877'
step4_model: Mistral-Large-3
step5_date: '2026-03-18T23:20:09.615552'
step5_model: Mistral-Large-3
step6_date: '2026-03-18T23:20:13.402749'
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
- method/variational
- method/VQE
- method/quantum-simulation
- idea/near-term-feasibility
- idea/hybrid-approach
title: Error and Resource Estimates of Variational Quantum Algorithms for Solving
  Differential Equations Based on Runge-Kutta Methods
topic_tags:
- derivatives-pricing
year: 2026
zotero_key: ''
---

## Abstract summary
This paper analyzes error sources and resource requirements for variational quantum algorithms (VQAs) that solve differential equations using Runge-Kutta methods (RKMs). The authors provide a rigorous framework to estimate errors—including truncation and shot noise—and determine the quantum resources needed to achieve target accuracy. The study compares different RKM orders to identify the most resource-efficient approaches for specific applications, such as option pricing via the Black-Scholes equation, offering practical guidance for optimizing hybrid quantum-classical algorithms in near-term quantum computing.
## Methodology
The paper presents a theoretical and analytical framework for evaluating error sources and resource requirements of variational quantum algorithms (VQAs) for solving differential equations (DEs) using Runge-Kutta methods (RKMs). The study focuses on hybrid quantum-classical approaches, where classical RKMs are combined with quantum computations to solve DEs, particularly in the context of near-term quantum devices. The authors derive analytical error and resource estimates for scenarios with and without shot noise, considering truncation errors in RKMs and shot noise in quantum measurements. The methodology involves formal error analysis, including the derivation of rigorous error bounds for the total error of the variational quantum algorithm, defined as the trace distance between the actual solution and the output of the algorithm. The paper applies this framework to two specific use cases: solving a 1D ordinary differential equation (ODE) classically and solving an option pricing linear partial differential equation (PDE) using the variational algorithm. The analysis highlights the trade-offs between the order of RKMs and resource requirements, demonstrating that higher-order RKMs can reduce resource demands depending on the problem parameters.

**Algorithms used:** Variational Quantum Eigensolver (VQE), Runge-Kutta Methods (RKMs)

**Experimental setup:** The analysis is theoretical and does not involve specific hardware or simulators. However, the paper discusses the application of the variational quantum algorithm on near-term quantum devices, considering shot noise and truncation errors. Numerical benchmarks are performed for a simple ODE (without shot noise) and an option pricing use case based on the Black-Scholes equation (with shot noise). The resource estimates are derived based on the number of quantum circuit evaluations required for the variational algorithm.

**Dataset:** The paper applies the methodology to two scenarios: (1) a simple 1D ordinary differential equation (ODE) solved classically, and (2) an option pricing problem described by the Black-Scholes partial differential equation (PDE). No explicit external datasets are mentioned; the data is generated through the numerical solution of these equations.
## Findings
- [supported] The paper provides rigorous error and resource estimates for variational quantum algorithms (VQAs) solving differential equations (DEs) using Runge-Kutta methods (RKMs), accounting for truncation errors and shot noise in quantum measurements.
- [supported] Higher-order RKMs (e.g., order 4 for a 1D ODE and order 2 for option pricing via the Black-Scholes equation) minimize the total number of quantum circuit evaluations required to achieve a target error.
- [supported] The total error of the variational quantum algorithm is defined as the trace distance between the actual solution and the output state, incorporating truncation errors from RKMs and shot noise errors from quantum measurements.
- [speculative] The authors suggest that higher-order RKMs may reduce resource requirements for other applications beyond the demonstrated use cases, depending on problem-specific parameters.
- [speculative] The framework provided could optimize quantum resources for solving DEs in other domains, such as quantum system simulations.
- [supported] The analysis excludes representation errors (due to Ansatz limitations) and hardware noise (e.g., gate infidelity, SPAM errors), assuming ideal conditions for these factors.
- [supported] The paper derives analytical error bounds and resource estimates for scenarios with and without shot noise, demonstrating that shot noise introduces an additional error scaling as O(1/N_meas^{1/2}).
- [speculative] The authors claim that their error and resource estimates are more comprehensive than prior works, as they integrate truncation errors and shot noise for direct comparisons between RKMs.

**Results summary:** The paper presents a detailed error and resource analysis for variational quantum algorithms solving differential equations using Runge-Kutta methods. It derives rigorous bounds for truncation errors and shot noise, demonstrating that higher-order RKMs (order 4 for a 1D ODE and order 2 for option pricing) minimize the total number of quantum circuit evaluations required to achieve a specified target error. The analysis is validated through numerical benchmarks, including a simple ODE and the Black-Scholes equation for option pricing. While the results are supported by theoretical derivations and simulations, the paper acknowledges limitations such as the exclusion of representation errors and hardware noise, which are assumed to be negligible. The findings provide a framework for optimizing quantum resources in variational algorithms for DEs.

**Performance claims:**
- Order 4 RKM is most resource-efficient for solving a 1D ODE without shot noise.
- Order 2 RKM minimizes total quantum circuit evaluations for option pricing via the Black-Scholes equation.
- Shot noise error scales as O(1/N_meas^{1/2}) with the number of measurements N_meas.
- Total error (trace distance) is bounded by truncation and shot noise errors, with rigorous upper bounds derived.
## Quantum advantage claim
**Classification:** speculative

The paper does not demonstrate quantum advantage on real hardware. Claims of resource efficiency and error reduction are based on theoretical analysis and simulations, with no empirical validation of superiority over classical methods. The advantage is framed as potential rather than demonstrated.
## Limitations
- Analysis does not account for representation errors stemming from the chosen Ansatz state not being expressive enough
- Hardware noise (e.g., gate infidelity, bias, SPAM errors) is assumed to be negligible, which may not hold on NISQ devices
- Circuit error effects are not considered, potentially limiting real-world applicability
- Matrix A (Eq. 24) is assumed to be invertible; regularization techniques for non-invertible cases introduce additional errors not analyzed
- Error bounds derived are general and may overestimate true errors in practice, leading to overly conservative resource estimates
- Analysis focuses on linear differential equations (Eq. 10), limiting applicability to nonlinear DEs without further adaptation
- No empirical validation on real quantum hardware; results are based on theoretical error bounds and simulations
- Lack of peer review as the paper is a preprint [inferred]
- [inferred] No direct comparison with classical numerical methods for solving differential equations in terms of computational efficiency or accuracy
- [inferred] Limited exploration of Ansatz expressivity and its impact on solution quality for financial use cases (e.g., option pricing)
## Open questions
- How do representation errors and Ansatz expressivity affect the accuracy of variational quantum algorithms for solving differential equations in financial applications?
- What is the impact of hardware noise and gate infidelities on the performance of RKM-based variational quantum algorithms?
- How can the error bounds be tightened to reduce conservatism in resource estimates for practical applications?
- What are the trade-offs between higher-order RKMs and the increased quantum resource requirements for financial PDEs (e.g., Black-Scholes)?
- How does the algorithm perform for nonlinear differential equations relevant to financial modeling?
- What are the implications of non-invertible matrix A on the stability and accuracy of the variational algorithm?
- How do the resource requirements scale with problem size (e.g., number of assets in option pricing) on real quantum hardware?

**Future work:**
- Empirical validation of the algorithm on real quantum hardware (e.g., IBM or Rigetti processors) to assess noise resilience
- Extension of the analysis to include representation errors and hardware noise for more realistic error bounds
- Comparison with classical numerical methods (e.g., finite difference, Monte Carlo) to benchmark quantum advantage
- Adaptation of the framework for nonlinear differential equations in financial modeling (e.g., stochastic DEs)
- Development of adaptive RKM selection strategies based on problem-specific parameters to optimize resource efficiency
- Exploration of alternative Ansätze and their impact on solution quality for financial use cases
- Investigation of matrix regularization techniques to handle non-invertible cases in variational algorithms
- Application of the framework to other financial PDEs (e.g., Heston model, interest rate models)
## Key ideas
- #idea:near-term-feasibility — Framework provides error and resource estimates for variational quantum algorithms solving differential equations (e.g., Black-Scholes) on near-term devices
- #idea:hybrid-approach — Hybrid quantum-classical approach combines classical Runge-Kutta methods with quantum computations to optimize resource efficiency
- #idea:near-term-feasibility — Higher-order Runge-Kutta methods (e.g., order 4 for ODEs, order 2 for option pricing) minimize quantum circuit evaluations for target accuracy
- #limitation:noise — Excludes hardware noise and representation errors, assuming ideal conditions for theoretical analysis
- #limitation:no-empirical-validation — Theoretical claims lack empirical validation on real quantum hardware
## Contradictions
<!-- Step 6 output — where this paper contradicts others -->

## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
