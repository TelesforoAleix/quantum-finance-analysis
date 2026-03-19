---
aliases:
- Quantum Algorithms for Portfolio Optimization
- Quantum Algorithms Portfolio Optimization
authors:
- Iordanis Kerenidis
- Anupam Prakash
- Dániel Szilágyi
auto_detected: true
classification: ''
contradiction_flags: []
doi: 10.1145/3318041.3355465
evidence_type: ''
idea_tags:
- idea:quantum-advantage
- idea:near-term-feasibility
- idea:hybrid-approach
journal_or_venue: 'AFT ''19: 1st ACM Conference on Advances in Financial Technologies'
methodology_tags:
- HHL
- quantum-simulation
- variational
paper_type: ''
quantum_advantage_claim: theoretical
related_papers: []
relevance_phase1: high
relevance_phase3: high
source_type: conference-paper
source_type_confidence: high
step1_date: '2026-03-18T23:13:14.013450'
step1_model: Mistral-Large-3
step2_date: '2026-03-18T23:13:16.938404'
step2_model: Mistral-Large-3
step3_date: '2026-03-18T23:13:22.977549'
step3_model: Mistral-Large-3
step4_date: '2026-03-18T23:13:34.754995'
step4_model: Mistral-Large-3
step5_date: '2026-03-18T23:13:44.264350'
step5_model: Mistral-Large-3
step6_date: '2026-03-18T23:13:49.125418'
step6_model: Mistral-Large-3
steps_completed:
- 1
- 2
- 3
- 4
- 5
- 6
tags:
- topic/portfolio-optimisation
- topic/risk-modelling
- method/HHL
- method/quantum-simulation
- method/variational
- idea/quantum-advantage
- idea/near-term-feasibility
- idea/hybrid-approach
title: Quantum Algorithms for Portfolio Optimization
topic_tags:
- portfolio-optimisation
- risk-modelling
year: 2019
zotero_key: ''
---

## Abstract summary
This paper presents the first quantum algorithm designed to solve the constrained portfolio optimization problem in financial services. The authors develop a quantum interior point method for second-order cone programs, achieving a polynomial speedup over classical algorithms while accommodating real-world constraints like budget and positivity. The work bridges quantum computing and mathematical finance, demonstrating potential practical advantages through theoretical analysis and experimental validation.
## Methodology
The paper presents a quantum algorithm for the constrained portfolio optimization problem by reducing it to a Second Order Cone Program (SOCP). The methodology involves formulating the portfolio optimization problem with positivity and budget constraints, then transforming it into an SOCP. The quantum algorithm employs a quantum short-step interior point method (IPM) to solve the SOCP. The approach leverages quantum linear algebra techniques, including block encoding of matrices and quantum linear system solvers, to achieve a polynomial speedup over classical algorithms. The algorithm iteratively solves Newton linear systems using quantum tomography to approximate solutions, ensuring convergence within a specified precision. Experimental results are provided to analyze problem-dependent parameters affecting the algorithm's running time and potential speedup over classical counterparts.

**Algorithms used:** Quantum Interior Point Method, Quantum Linear System Solver
**Frameworks:** QRAM (Quantum Random Access Memory)

**Experimental setup:** The quantum algorithm is theoretically analyzed and simulated using quantum linear algebra techniques. The experimental setup involves constructing block encodings for matrices using QRAM data structures, solving Newton linear systems via quantum linear system solvers, and performing quantum tomography to recover classical solutions. The simulations focus on bounding problem-dependent parameters such as the condition number of Newton matrices to evaluate the algorithm's efficiency and potential speedup.

**Dataset:** Historical prices of financial assets are used to compute the expected reward vector (µ) and the covariance matrix (Σ). The covariance matrix is derived from historical return data over T time epochs for m assets, enabling the formulation of the portfolio optimization problem.
## Findings
- [supported] The paper presents the first quantum algorithm for the constrained portfolio optimization problem, with a running time of e^O(n√r ζ κ / δ^2 log(1/ϵ)), where r is the number of constraints, n is the number of assets, ϵ is precision, and δ, κ, ζ are problem-dependent parameters.
- [supported] The quantum algorithm achieves a polynomial speedup over the best classical algorithms, which have a complexity of e^O(√rn^ω log(1/ϵ)), where ω is the matrix multiplication exponent (theoretically ~2.373, practically ~3).
- [speculative] Experiments suggest that for most instances, the quantum algorithm can potentially achieve an O(n) speedup over its classical counterpart.
- [supported] The quantum algorithm reduces the constrained portfolio optimization problem to Second Order Cone Programs (SOCP) and uses a quantum interior point method to solve it.
- [supported] The quantum algorithm ensures the duality gap reduces by a factor of 1 - α/√r per iteration, converging in O(√r log(n/ϵ)) iterations, similar to classical methods.
- [speculative] The quantum advantage is maximized when the number of assets (n) is large and the number of budget constraints (r) is small, as the condition number κ increases with the number of iterations.
- [supported] The quantum algorithm outputs a solution with an objective value within ϵr of the optimum and satisfies equality constraints to precision δ.
- [speculative] The paper claims that quantum computers could offer groundbreaking speedups in mathematical finance, though this requires more advanced hardware and collaboration between quantum algorithms and finance communities.

**Results summary:** The paper introduces a quantum algorithm for constrained portfolio optimization, demonstrating a polynomial speedup over classical methods. The algorithm reduces the problem to Second Order Cone Programs (SOCP) and employs a quantum interior point method. The running time is e^O(n√r ζ κ / δ^2 log(1/ϵ)), compared to the classical e^O(√rn^ω log(1/ϵ)). Experimental results suggest potential O(n) speedups for real-world instances, though the quantum advantage is contingent on problem-specific parameters like the condition number κ. The algorithm converges in O(√r log(n/ϵ)) iterations, similar to classical methods, but leverages quantum linear algebra for efficiency. The findings are theoretical, with no empirical validation on real quantum hardware.

**Performance claims:**
- Running time: e^O(n√r ζ κ / δ^2 log(1/ϵ)) for the quantum algorithm
- Classical algorithm running time: e^O(√rn^ω log(1/ϵ))
- Potential O(n) speedup over classical methods for most instances
- Duality gap reduction factor: 1 - α/√r per iteration
- Convergence in O(√r log(n/ϵ)) iterations
- Objective value within ϵr of the optimum
- Equality constraints satisfied to precision δ
## Quantum advantage claim
**Classification:** theoretical

The paper claims a polynomial speedup over classical algorithms based on theoretical analysis and simulations. The advantage is not demonstrated on real quantum hardware and depends on problem-specific parameters like the condition number κ. The speedup is speculative for practical applications until validated empirically.
## Limitations
- The quantum algorithm's running time depends on problem-dependent parameters (δ, κ, ζ) related to the well-conditioning of intermediate solutions, which may not always be favorable in practice [inferred]
- The algorithm assumes the existence of a strictly feasible solution, which may not hold for all real-world portfolio optimization problems [inferred]
- The quantum algorithm's speedup is contingent on the condition number κ of the Newton matrices being bounded, which is not guaranteed for all problem instances
- The solution satisfies equality constraints only approximately to precision δ, which may not be sufficient for high-stakes financial applications [inferred]
- The quantum algorithm requires quantum linear system solvers and tomography, introducing errors that may affect solution feasibility and optimality
- The experiments bounding problem-dependent factors are not exhaustive and may not generalize to all real-world scenarios [inferred]
- The quantum algorithm's performance is particularly suited for cases where the number of assets (n) is large and the number of budget constraints (r) is small, limiting its applicability to problems with many constraints [inferred]
- The paper does not provide empirical validation on real quantum hardware, only theoretical and simulated results [inferred]
- The quantum algorithm's convergence rate is slower per iteration compared to the classical algorithm, though the asymptotic decay rate is the same [inferred]
- Page-limit constraints of the conference paper may have prevented a more detailed discussion of practical implementation challenges [inferred]
## Open questions
- How does the quantum algorithm perform on real-world financial datasets with noisy or incomplete historical price data?
- What is the impact of quantum hardware noise and decoherence on the algorithm's performance and solution quality?
- Can the algorithm be adapted to handle dynamic or time-varying portfolio optimization problems?
- How does the quantum algorithm compare to state-of-the-art classical solvers in terms of solution quality and runtime for large-scale problems?
- What are the specific values of the problem-dependent parameters (κ, ζ) for typical financial datasets, and how do they affect the algorithm's speedup?
- Can the algorithm be extended to handle more complex constraints, such as transaction costs or regulatory requirements?
- What is the minimum qubit count and coherence time required to achieve a practical speedup over classical methods?

**Future work:**
- Empirical validation of the algorithm on real quantum hardware to assess its practical performance
- Extension of the algorithm to handle dynamic portfolio optimization problems with time-varying constraints
- Development of noise mitigation techniques to improve the algorithm's robustness on near-term quantum devices
- Comparison of the quantum algorithm's performance with state-of-the-art classical solvers on large-scale financial datasets
- Exploration of hybrid quantum-classical approaches to leverage the strengths of both paradigms
- Investigation of the algorithm's applicability to other financial optimization problems, such as risk management or asset pricing
- Development of methods to reduce the impact of problem-dependent parameters on the algorithm's running time
## Key ideas
- #idea:quantum-advantage — Quantum interior point method achieves polynomial speedup (e^O(n√r ζ κ / δ^2 log(1/ϵ))) over classical algorithms (e^O(√rn^ω log(1/ϵ))) for constrained portfolio optimization
- #idea:near-term-feasibility — Algorithm is theoretically designed for NISQ-era applicability but requires bounded condition numbers and problem-specific parameters for practical speedup
- #idea:hybrid-approach — Quantum linear system solvers and tomography are used iteratively, suggesting potential for hybrid quantum-classical integration
- #limitation:qubit-count — Performance depends on large asset counts (n) and small constraint counts (r), limiting scalability for real-world problems
- #limitation:noise — Quantum tomography and linear system solvers introduce errors that may degrade solution feasibility and optimality
- #limitation:no-empirical-validation — Claims are theoretical/simulated; no validation on real quantum hardware
## Contradictions
<!-- Step 6 output — where this paper contradicts others -->

## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
