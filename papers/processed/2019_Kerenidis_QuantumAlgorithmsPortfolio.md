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
step1_date: '2026-03-19T11:46:20.765928'
step1_model: Mistral-Large-3
step2_date: '2026-03-19T11:47:08.480155'
step2_model: Mistral-Large-3
step3_date: '2026-03-19T11:47:18.445692'
step3_model: Mistral-Large-3
step4_date: '2026-03-19T11:48:28.263397'
step4_model: Mistral-Large-3
step5_date: '2026-03-19T11:48:50.701536'
step5_model: Mistral-Large-3
step6_date: '2026-03-19T11:48:58.656083'
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
- method/HHL
- method/quantum-simulation
- method/variational
- idea/quantum-advantage
- idea/near-term-feasibility
- idea/hybrid-approach
title: Quantum Algorithms for Portfolio Optimization
topic_tags:
- portfolio-optimisation
year: 2019
zotero_key: ''
---

## Abstract summary
This paper presents the first quantum algorithm for solving the constrained portfolio optimization problem in financial services. The authors develop a quantum interior point method that extends classical approaches by incorporating quantum linear algebra techniques, achieving a polynomial speedup over classical algorithms under certain conditions. The work focuses on reducing the problem to second-order cone programming and demonstrates potential practical advantages through numerical experiments.
## Methodology
The paper presents a quantum algorithm for the constrained portfolio optimization problem, extending previous work that was limited to unconstrained problems. The methodology involves reducing the portfolio optimization problem to a Second Order Cone Program (SOCP), which generalizes both linear and quadratic programming. The quantum algorithm is based on a quantum interior point method (IPM) for SOCPs, leveraging quantum linear algebra techniques to solve the Newton linear systems arising in each iteration of the IPM. The algorithm uses quantum data structures, specifically Quantum Random Access Memory (QRAM), to store and manipulate matrices and vectors efficiently. The quantum short-step IPM is implemented by constructing block encodings for the Newton matrices, solving the linear systems using quantum linear system solvers, and performing quantum tomography to recover classical solutions. The paper also includes experimental results to analyze the performance and convergence of the quantum algorithm, comparing it with classical methods and examining problem-dependent parameters such as condition number and tomography precision.

**Algorithms used:** Quantum Interior Point Method (IPM), Quantum Linear System Solver
**Frameworks:** QRAM (Quantum Random Access Memory)

**Experimental setup:** The experimental setup involves simulating the quantum algorithm on classical hardware to solve instances of the portfolio optimization problem. The dataset used consists of historical stock prices for 50 companies from the S&P 500 over 100 days. The quantum algorithm's performance is analyzed by introducing Gaussian noise to simulate tomography precision. The experiments assess the duality gap, condition number of the Newton matrix, and the impact of tomography precision on the algorithm's convergence and runtime. The quantum algorithm is compared against classical IPM solvers in terms of iteration count and problem size scaling.

**Dataset:** Historical stock prices for 50 companies from the S&P 500 index, sampled over the first 100 days of a 9-year period (2007-2016). The dataset was subsampled from the cvxportfolio repository.
## Findings
- [supported] The paper presents the first quantum algorithm for constrained portfolio optimization, with a running time of eO(√r * n * κ * ζ / δ² * log(1/ϵ)), where r is the number of constraints, n is the number of assets, κ is the condition number, ζ is a parameter from the quantum linear system solver, and δ is the precision error.
- [supported] The quantum algorithm achieves a polynomial speedup over classical algorithms, which have a complexity of eO(n^ω * √r * log(1/ϵ)), where ω is the matrix multiplication exponent (theoretically ~2.373, but closer to 3 in practice).
- [supported] Experimental results suggest that for most instances, the quantum algorithm can achieve an O(n) speedup over classical algorithms, particularly when the number of assets (n) is large and the number of constraints (r) is small.
- [supported] The quantum algorithm reduces the constrained portfolio optimization problem to a Second Order Cone Program (SOCP) and uses a quantum interior point method (IPM) to solve it, ensuring feasibility and convergence properties similar to classical IPMs.
- [supported] The condition number κ of the Newton matrix does not grow significantly with problem size in practice, and the tomography precision δ scales roughly linearly with n, leading to an average-case complexity of O(n^2.387) for the quantum algorithm.
- [speculative] The authors suggest that quantum computers could offer significant speedups for large-scale portfolio optimization problems, but note that practical realization depends on advances in quantum hardware and closer collaboration between quantum algorithm and financial communities.
- [speculative] The paper claims that the quantum algorithm's performance is particularly suited for problems with a large number of assets and a small number of constraints, where the quantum advantage is maximized.

**Results summary:** The paper introduces a quantum algorithm for constrained portfolio optimization, leveraging a quantum interior point method for Second Order Cone Programs (SOCPs). The algorithm demonstrates a theoretical polynomial speedup over classical methods, with a running time of eO(√r * n * κ * ζ / δ² * log(1/ϵ)). Experimental simulations on real-world financial datasets suggest that the quantum algorithm can achieve an O(n) speedup for most instances, particularly when the number of assets is large and constraints are few. The condition number κ and tomography precision δ are shown to behave favorably in practice, leading to an average-case complexity of O(n^2.387). The results are derived from simulations, as the algorithm has not been tested on real quantum hardware.

**Performance claims:**
- Running time of eO(√r * n * κ * ζ / δ² * log(1/ϵ)) for the quantum algorithm
- Classical algorithm complexity of eO(n^ω * √r * log(1/ϵ)), where ω ~ 3 in practice
- O(n) speedup over classical algorithms for most instances, based on experimental simulations
- Average-case complexity of O(n^2.387) for the quantum algorithm, compared to O(n^3.5) for classical methods
## Quantum advantage claim
**Classification:** theoretical

The paper claims a theoretical polynomial speedup over classical algorithms for constrained portfolio optimization, supported by experimental simulations. However, the results are not demonstrated on real quantum hardware, and the advantage is contingent on problem-specific parameters (e.g., condition number κ and tomography precision δ) behaving favorably in practice.
## Limitations
- The quantum algorithm's running time depends on problem-specific parameters (κ, ζ, δ) that may not be bounded in practice, limiting its theoretical speedup
- The algorithm assumes the existence of a strictly feasible solution, which may not always hold for real-world problems [inferred]
- Experiments were conducted on a small subset of data (50 companies, 100 days) and may not generalize to larger, more complex financial datasets [inferred]
- The quantum algorithm's performance is sensitive to the condition number (κ) of the Newton matrix, which could grow with problem size in practice
- Tomography errors in quantum state reconstruction lead to approximate solutions, unlike classical methods that provide exact solutions
- The quantum algorithm's speedup is only achievable if the number of budget constraints (r) is small compared to the number of assets (n), limiting applicability to highly constrained problems [inferred]
- The paper does not compare the quantum algorithm's performance with state-of-the-art classical solvers beyond asymptotic complexity analysis [inferred]
- The quantum algorithm requires QRAM data structures, which are not yet available in current quantum hardware [inferred]
- The experiments suggest that the 1/δ² term grows roughly linearly with problem size, potentially reducing the quantum speedup for large-scale problems
- The algorithm's convergence rate constant (α) is close to but still slower than the classical algorithm's constant (χ), leading to more iterations for the same precision [inferred]
## Open questions
- How does the quantum algorithm perform on real-world financial datasets with thousands of assets and complex constraints?
- What is the exact relationship between the condition number (κ) and problem size for practical portfolio optimization instances?
- Can the quantum algorithm be adapted to handle dynamic constraints that change over time in financial markets?
- How would noise in near-term quantum hardware affect the algorithm's performance and convergence?
- What is the minimum qubit count and coherence time required to achieve a practical speedup over classical methods?
- Can the quantum interior point method be extended to handle integer constraints for discrete portfolio optimization problems?
- How does the quantum algorithm compare with classical methods in terms of solution quality for the same computational budget?
- What are the implications of the tomography precision requirements for the algorithm's practical implementation?

**Future work:**
- Test the algorithm on larger, more diverse financial datasets to validate scalability claims
- Implement the algorithm on near-term quantum hardware to assess real-world performance
- Develop noise mitigation techniques tailored to the quantum interior point method
- Extend the algorithm to handle dynamic constraints and multi-period portfolio optimization
- Investigate hybrid quantum-classical approaches that combine the strengths of both paradigms
- Explore alternative quantum linear algebra techniques that may reduce the dependence on problem-specific parameters
- Develop methods to reduce the condition number (κ) of the Newton matrix for practical problems
- Compare the quantum algorithm's performance with state-of-the-art classical solvers on benchmark problems
- Investigate the algorithm's performance on other financial optimization problems beyond portfolio optimization
- Develop error bounds and robustness guarantees for the algorithm under hardware noise
## Key ideas
- #idea:quantum-advantage — Quantum interior point method achieves polynomial speedup (e^O(√r * n * κ * ζ / δ² * log(1/ϵ))) over classical algorithms (e^O(n^ω * √r * log(1/ϵ))) for constrained portfolio optimization
- #idea:near-term-feasibility — Algorithm is theoretically designed for NISQ-era applicability but requires bounded condition numbers and problem-specific parameters for practical speedup
- #idea:hybrid-approach — Quantum linear system solvers and tomography are used iteratively, suggesting potential for hybrid quantum-classical integration
- #limitation:qubit-count — Performance depends on large asset counts (n) and small constraint counts (r), limiting scalability for real-world problems
- #limitation:noise — Quantum tomography and linear system solvers introduce errors that may degrade solution feasibility and optimality
- #limitation:no-empirical-validation — Claims are theoretical/simulated; no validation on real quantum hardware
- #limitation:data-encoding — Requires QRAM for efficient data encoding, which is not yet available in current quantum hardware
## Contradictions
<!-- Step 6 output — where this paper contradicts others -->

## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
