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
step1_date: '2026-03-19T22:49:53.907749'
step1_model: Mistral-Large-3
step2_date: '2026-03-19T22:49:58.333423'
step2_model: Mistral-Large-3
step3_date: '2026-03-19T22:51:42.874103'
step3_model: Mistral-Large-3
step4_date: '2026-03-19T22:51:49.547170'
step4_model: Mistral-Large-3
step5_date: '2026-03-19T22:52:55.821918'
step5_model: Mistral-Large-3
step6_date: '2026-03-19T22:52:59.667052'
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
This paper presents the first quantum algorithm for constrained portfolio optimization in financial services, addressing limitations of prior quantum approaches that could not handle positivity or budget constraints. The authors reduce the problem to second-order cone programming (SOCP) and apply a quantum interior point method, achieving a polynomial speedup over classical algorithms. The work explores theoretical and experimental performance, suggesting practical advantages for large-scale problems with complex constraints.
## Methodology
The paper presents a theoretical and algorithmic framework for solving the constrained portfolio optimization problem using quantum computing. The authors reduce the portfolio optimization problem to a Second Order Cone Program (SOCP) and then apply a quantum interior point method (IPM) to solve it. The quantum algorithm leverages quantum linear algebra techniques, specifically quantum linear system solvers, to achieve a polynomial speedup over classical algorithms. The methodology involves formulating the portfolio optimization problem with positivity and budget constraints, transforming it into an SOCP, and solving it using a quantum short-step interior point method. The paper also includes experimental simulations to analyze problem-dependent parameters such as condition number and tomography precision, demonstrating the potential for an O(n) speedup over classical methods for most instances.

**Algorithms used:** Quantum Interior Point Method, Quantum Linear System Solver

**Experimental setup:** The experimental simulations were conducted using a dataset of historical stock prices from the S&P 500 companies over a 9-year period (2007-2016), subsampled to 50 companies and 100 days. The quantum algorithm's performance was simulated by introducing Gaussian noise corresponding to tomography precision. The experiments aimed to bound problem-dependent factors like condition number and tomography precision, assessing their impact on the algorithm's running time.

**Dataset:** Historical stock prices from S&P 500 companies (2007-2016), subsampled to 50 companies and 100 days of data.
## Findings
- [supported] The paper presents the first quantum algorithm for constrained portfolio optimization, with a running time of e^O(n√r ζ κ / δ² log(1/ϵ)), where n is the number of assets, r is the number of constraints, and ζ, κ, δ are problem-dependent parameters.
- [supported] The quantum algorithm achieves a polynomial speedup over classical algorithms, which have a complexity of e^O(n^ω √r log(1/ϵ)) (ω ≈ 2.373 theoretically, closer to 3 in practice).
- [speculative] The authors suggest that for most instances, the quantum algorithm can achieve an O(n) speedup over classical counterparts, based on experimental observations.
- [supported] The algorithm reduces the constrained portfolio optimization problem to Second Order Cone Programs (SOCP) and uses a quantum interior point method for SOCPs, enabling the handling of positivity and budget constraints.
- [supported] Experimental results indicate that the condition number κ of the Newton matrix does not grow significantly with problem size, and the factor 1/δ² grows roughly linearly with n.
- [supported] The duality gap decreases multiplicatively by a factor of σ = (1 - α/√r) per iteration, with α close to the classical constant χ = 0.1, suggesting similar convergence rates for quantum and classical algorithms.
- [speculative] The paper claims that quantum computers could offer significant speedups for large-scale portfolio optimization problems where the number of assets n is large and the number of constraints r is small.
- [supported] The quantum algorithm ensures that the solution satisfies inequality constraints (x ≥ 0) and equality constraints to precision δ, with infeasibility bounded by δ ∥A∥.

**Results summary:** The paper introduces a quantum algorithm for constrained portfolio optimization, leveraging a quantum interior point method for Second Order Cone Programs (SOCP). The algorithm demonstrates a polynomial speedup over classical methods, with a theoretical running time of e^O(n√r ζ κ / δ² log(1/ϵ)). Experimental results suggest that the quantum algorithm can achieve an O(n) speedup for most problem instances, particularly when the number of assets is large and constraints are few. The condition number κ and tomography precision δ were observed to behave favorably, with κ not growing significantly with problem size and 1/δ² scaling linearly with n. The duality gap convergence rate is comparable to classical methods, indicating practical viability. The algorithm is notable for its ability to handle complex constraints like positivity and budget limits, which are common in real-world portfolio optimization.

**Performance claims:**
- Running time: e^O(n√r ζ κ / δ² log(1/ϵ)) for the quantum algorithm
- Classical algorithm complexity: e^O(n^ω √r log(1/ϵ)) (ω ≈ 2.373 theoretically, closer to 3 in practice)
- Observed O(n) speedup over classical algorithms for most instances
- Duality gap reduction by a factor of (1 - α/√r) per iteration, with α close to 0.1
- Condition number κ growth observed as O(1/ν^α) for α < 0.5 over T iterations
- 1/δ² grows roughly linearly with problem size n
## Quantum advantage claim
**Classification:** theoretical

The quantum advantage is claimed based on theoretical complexity analysis and experimental simulations, showing a polynomial speedup over classical algorithms. The advantage is not demonstrated on real quantum hardware but is supported by numerical experiments and theoretical guarantees. The speedup is contingent on problem-dependent parameters like condition number κ and tomography precision δ, which were observed to behave favorably in simulations.
## Limitations
- Theoretical speedup assumes bounded condition number κ of the Newton matrices, which may not hold in all practical scenarios [inferred]
- Algorithm relies on quantum linear system solvers, which require efficient block encoding of matrices; constructing these encodings may be non-trivial for arbitrary financial datasets [inferred]
- Experiments limited to synthetic or subsampled real-world data (50 companies over 100 days), which may not generalize to full-scale financial datasets [inferred]
- Quantum algorithm's performance depends on problem-dependent parameters (δ, κ, ζ) that are not fully characterized for all portfolio optimization instances
- Tomography errors in quantum state reconstruction lead to approximate solutions, with equality constraints satisfied only to precision δ
- No empirical validation on real quantum hardware; experiments are classical simulations with added Gaussian noise to mimic tomography errors [inferred]
- Conference paper page limits may have constrained detailed discussion of failure cases or edge conditions [inferred]
- Algorithm assumes direct access to the square root of the covariance matrix (M), which may not be readily available in all financial datasets [inferred]
- Theoretical speedup is contingent on the number of constraints (r) being small relative to the number of assets (n), limiting applicability to highly constrained problems [inferred]
- No comparison with state-of-the-art classical solvers (e.g., commercial QP solvers) to benchmark practical speedups [inferred]
- Assumes existence of strictly feasible solutions for the SOCP formulation, which may not hold for all real-world portfolio problems [inferred]
## Open questions
- How does the quantum algorithm perform when the number of constraints (r) scales with the number of assets (n)?
- What is the impact of hardware noise and decoherence on the algorithm's convergence and solution quality on near-term quantum devices?
- Can the algorithm be adapted to handle dynamic or time-varying constraints (e.g., real-time portfolio rebalancing)?
- How do the problem-dependent parameters (κ, ζ, δ) behave for large-scale, real-world financial datasets?
- What are the trade-offs between tomography precision (δ) and the algorithm's runtime for practical applications?
- Can the quantum speedup be maintained when incorporating transaction costs or other real-world frictions?
- How does the algorithm compare to classical methods in terms of robustness to input data noise or missing data?
- What are the implications of the algorithm's approximate constraint satisfaction for regulatory compliance in financial applications?

**Future work:**
- Test the algorithm on real quantum hardware (e.g., IBM Eagle or future processors) to validate theoretical speedups
- Extend the algorithm to handle more complex constraints (e.g., transaction costs, regulatory limits, or multi-period optimization)
- Develop hybrid quantum-classical approaches to mitigate the impact of tomography errors and hardware noise
- Benchmark the algorithm against state-of-the-art classical solvers (e.g., MOSEK, ECOS) on large-scale financial datasets
- Investigate the algorithm's performance on other financial optimization problems (e.g., option pricing, risk management)
- Explore methods to reduce the dependence of runtime on problem-dependent parameters (κ, ζ, δ)
- Develop techniques to ensure strict feasibility of solutions for regulatory compliance
- Apply the algorithm to dynamic portfolio optimization problems with time-varying constraints
- Investigate the use of quantum data structures (e.g., QRAM) for real-time financial data processing
## Key ideas
- #idea:quantum-advantage — Quantum interior point method achieves polynomial speedup (e^O(√r * n * κ * ζ / δ² * log(1/ϵ))) over classical algorithms (e^O(n^ω * √r * log(1/ϵ))) for constrained portfolio optimization with positivity and budget constraints
- #idea:near-term-feasibility — Algorithm is theoretically designed for NISQ-era applicability but requires bounded condition numbers and problem-specific parameters (κ, δ, ζ) for practical speedup
- #idea:hybrid-approach — Quantum linear system solvers and tomography are used iteratively, suggesting potential for hybrid quantum-classical integration to mitigate data encoding and noise challenges
- #limitation:qubit-count — Performance depends on large asset counts (n) and small constraint counts (r), limiting scalability for highly constrained real-world problems
- #limitation:noise — Quantum tomography and linear system solvers introduce errors that may degrade solution feasibility (equality constraints satisfied only to precision δ) and optimality
- #limitation:no-empirical-validation — Claims are theoretical/simulated; no validation on real quantum hardware, only classical simulations with Gaussian noise
- #limitation:data-encoding — Requires QRAM for efficient data encoding, which is not yet available in current quantum hardware
## Contradictions
<!-- Step 6 output — where this paper contradicts others -->

## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->

## Experiment details
### Input
Subsampled dataset of 50 companies from the S&P 500, with historical stock prices for the first 100 days. The expected reward and risk were estimated from the data, and the covariance matrix was derived. The dataset was used to construct the constraint matrices for the SOCP formulation of the portfolio optimization problem.

### Process
1. Compute vector µ and matrix M from the dataset as per the portfolio optimization formulation. 2. Store the constraint matrix for the SOCP in Quantum Random Access Memory (QRAM). 3. For each iteration of the quantum interior point method: (a) Construct the block encoding for the Newton linear system matrix. (b) Estimate the norm of the Newton system solution. (c) Solve the Newton linear system using quantum linear algebra techniques and perform tomography to obtain classical estimates. (d) Update the solution and store it in QRAM. 4. After T iterations, output the solution to the portfolio optimization problem.

### Output
The solution to the constrained portfolio optimization problem, including the portfolio weights (x). The results were analyzed in terms of duality gap, condition number of the Newton matrix, and tomography precision. The output also included comparisons of the quantum algorithm's performance against classical methods, demonstrating potential speedups.

### Parameters
- iterations: O(√r log(n/ϵ))
- precision: ϵ (desired precision)
- tomography_precision: δ
- condition_number: κ (maximum condition number of the Newton matrix over iterations)
- parameter_zeta: ζ ≤ √n (parameter in quantum linear system solver)
- duality_gap_reduction_factor: σ = 1 - α/√r (α < 0.1)

### Hardware
N/A

### Reproducibility
N/A
