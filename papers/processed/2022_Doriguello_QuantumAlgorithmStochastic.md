---
aliases:
- Quantum Algorithm for Stochastic Optimal Stopping Problems with Applications in
  Finance
- Quantum Algorithm Stochastic Optimal
authors:
- João F. Doriguello
- Alessandro Luongo
- Jinge Bao
- Patrick Rebentrost
- Miklos Santha
auto_detected: true
classification: ''
contradiction_flags: []
doi: 10.4230/LIPIcs.TQC.2022.2
evidence_type: ''
idea_tags:
- idea:quantum-advantage
- idea:near-term-feasibility
- idea:hybrid-approach
journal_or_venue: 17th Conference on the Theory of Quantum Computation, Communication
  and Cryptography (TQC 2022)
methodology_tags:
- amplitude-estimation
- quantum-simulation
- quantum-ML
paper_type: ''
quantum_advantage_claim: theoretical
related_papers: []
relevance_phase1: high
relevance_phase3: high
source_type: conference-paper
source_type_confidence: high
step1_date: '2026-03-19T12:16:02.836702'
step1_model: Mistral-Large-3
step2_date: '2026-03-19T12:17:08.766637'
step2_model: Mistral-Large-3
step3_date: '2026-03-19T12:17:19.126385'
step3_model: Mistral-Large-3
step4_date: '2026-03-19T12:17:30.952188'
step4_model: Mistral-Large-3
step5_date: '2026-03-19T12:17:53.710037'
step5_model: Mistral-Large-3
step6_date: '2026-03-19T12:18:15.728269'
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
- method/amplitude-estimation
- method/quantum-simulation
- method/quantum-ML
- idea/quantum-advantage
- idea/near-term-feasibility
- idea/hybrid-approach
title: Quantum Algorithm for Stochastic Optimal Stopping Problems with Applications
  in Finance
topic_tags:
- derivatives-pricing
- risk-modelling
year: 2022
zotero_key: ''
---

## Abstract summary
This paper introduces a quantum version of the least squares Monte Carlo (LSM) algorithm for solving stochastic optimal stopping problems, a key challenge in financial mathematics, particularly for pricing American options. The authors propose a quantum algorithm that leverages quantum access to stochastic processes and quantum techniques for Monte Carlo simulation to achieve a nearly quadratic speedup over the classical LSM algorithm. The work explores the interplay between function approximation and quantum algorithms, demonstrating potential applications in finance and beyond.
## Methodology
The paper presents a quantum algorithm for solving stochastic optimal stopping problems, specifically applied to financial contexts such as American option pricing. The methodology builds on the classical Least Squares Monte Carlo (LSM) algorithm, which approximates continuation values using linear least squares regression and Monte Carlo simulation. The quantum version leverages quantum access to stochastic processes and quantum circuits for computing optimal stopping times. The algorithm employs quantum techniques for Monte Carlo to achieve a nearly quadratic speedup in runtime compared to the classical LSM under mild assumptions. The quantum LSM algorithm recursively solves dynamic programming in superposition over all possible stochastic processes, using quantum subroutines for Monte Carlo to approximate expectation values. The approach involves constructing quantum circuits for computing stopping times and continuation values, with a focus on finite-dimensional linear approximation architectures. Error analysis and complexity considerations are detailed, showing the quantum algorithm's advantage in reducing the number of oracle calls quadratically relative to the classical counterpart.

**Algorithms used:** Quantum Least Squares Monte Carlo, Amplitude Estimation

**Experimental setup:** The quantum algorithm operates within the standard circuit model of quantum computation, utilizing fixed-point arithmetic for real numbers and assuming sufficient qubits for precision. Quantum sampling access to a Markov chain and quantum query access to functions (e.g., payoff and basis functions) are assumed. The experimental setup includes quantum oracles for input functions, quantum circuits for arithmetic operations, and controlled rotations. The algorithm is designed to run on a quantum computer with access to these quantum resources, and it leverages quantum subroutines for Monte Carlo (e.g., QMonteCarlo) to estimate expectation values efficiently.

**Dataset:** The paper applies the algorithm to stochastic processes such as Brownian motion and geometric Brownian motion, which are common models in financial mathematics for asset price dynamics. While specific datasets are not explicitly mentioned, the methodology assumes quantum access to these stochastic processes and associated payoff functions, which are typically derived from financial market models.
## Findings
- [supported] The proposed quantum Least Squares Monte Carlo (LSM) algorithm achieves a nearly quadratic speedup in runtime compared to the classical LSM algorithm for stochastic optimal stopping problems under mild assumptions, including applications to American option pricing.
- [supported] The quantum algorithm demonstrates a time complexity of ˜O(T²m⁴/ϵ) compared to the classical algorithm's ˜O(Tm⁶/ϵ²), where T is the number of time steps, m is the number of expansion functions, and ϵ is the additive accuracy.
- [speculative] For continuation values that are n-times differentiable with n = Θ(log(5T/ϵ)/log log(5T/ϵ)), the quantum algorithm achieves ˜O(5T/ϵ) runtime, showing a quadratic improvement over the classical ˜O((5T/ϵ)²) runtime.
- [supported] The quantum LSM algorithm leverages quantum subroutines for Monte Carlo and dynamic programming in superposition, enabling recursive computation of stopping times and continuation values.
- [speculative] The quantum advantage may extend to other applications of LSM in finance, such as insurance, risk management, and optimization problems like quickest detection and sequential Bayesian hypothesis testing.
- [supported] For Brownian motion and geometric Brownian motion processes, the quantum algorithm's complexity simplifies due to the orthogonality of Hermite polynomials and the structure of Vandermonde matrices, respectively.
- [disputed] The exponential dependence on T in the final complexities is noted as potentially improvable, given the practical success of classical LSM algorithms in financial markets.

**Results summary:** The paper introduces a quantum LSM algorithm for stochastic optimal stopping problems, demonstrating a nearly quadratic speedup over the classical LSM algorithm. The quantum algorithm leverages quantum access to stochastic processes, quantum circuits for computing optimal stopping times, and quantum techniques for Monte Carlo. Under specific smoothness assumptions on continuation values, the quantum algorithm achieves a runtime of ˜O(5T/ϵ), compared to the classical ˜O((5T/ϵ)²). The algorithm is validated through theoretical analysis and case studies on Brownian motion and geometric Brownian motion processes, with potential applications extending to American option pricing and other financial and optimization problems.

**Performance claims:**
- Nearly quadratic speedup in runtime compared to classical LSM under mild assumptions
- Quantum algorithm time complexity: ˜O(T²m⁴/ϵ)
- Classical algorithm time complexity: ˜O(Tm⁶/ϵ²)
- For n-times differentiable continuation values, quantum runtime: ˜O(5T/ϵ)
- For n-times differentiable continuation values, classical runtime: ˜O((5T/ϵ)²)
## Quantum advantage claim
**Classification:** theoretical

The quantum advantage is theoretically demonstrated through complexity analysis showing a nearly quadratic speedup in runtime for the quantum LSM algorithm compared to its classical counterpart. The advantage holds under specific assumptions, such as smoothness of continuation values and the use of quantum subroutines for Monte Carlo. However, the results are based on simulations and theoretical models, not real quantum hardware.
## Limitations
- The algorithm assumes quantum access to a stochastic process, which may not be feasible with current quantum hardware [inferred]
- The proposed quantum LSM algorithm requires redoing all previous dynamic programming steps before progressing to the next time step, leading to O(T^2) time steps instead of O(T) in the classical version
- The final complexities have an exponential dependence on T (number of time steps), which may limit practical applicability for large T [inferred]
- The error analysis assumes that the continuation values are n-times differentiable, which may not hold for all financial models
- The quantum algorithm's performance depends on parameters that implicitly depend on the underlying Markov chain, such as the minimum singular value of matrices A_t
- The paper assumes a fixed-point representation for real numbers with sufficient precision, which may not be practical on near-term quantum devices [inferred]
- The quantum arithmetic model assumes constant-time arithmetic operations, which may not reflect real quantum hardware constraints [inferred]
- The algorithm's advantage is demonstrated under specific smoothness conditions (n = Θ(log(5T/ϵ)/log log(5T/ϵ))), which may not be universally applicable
- The analysis does not account for error propagation and accumulation in quantum arithmetic operations, which could affect results on real hardware [inferred]
- The paper does not provide empirical validation of the quantum algorithm on real quantum hardware, only theoretical analysis
- The quantum algorithm's complexity includes polylogarithmic factors that may impact practical performance [inferred]
- The paper assumes quantum sampling access to Markov chains, which may be difficult to implement for complex financial models [inferred]
- The algorithm's performance for geometric Brownian motion is slightly weaker than the usual O(ϵ^{-1}) due to sensitivity of the minimum singular value of A_t to the degree q of chosen monomials
## Open questions
- How does the quantum algorithm perform on real quantum hardware with noise and limited qubit counts?
- What is the impact of decoherence and quantum noise on the solution quality of the quantum LSM algorithm?
- Can the exponential dependence on T be improved through tighter error bounds or alternative algorithmic approaches?
- How does the algorithm compare with state-of-the-art classical solvers for large-scale problems?
- What are the practical implications of the smoothness assumptions on continuation values for real-world financial applications?
- Can the quantum algorithm be modified to handle non-differentiable continuation values or other irregularities in financial models?
- How does the choice of expansion functions (e.g., polynomials vs. Chebyshev nodes) affect the algorithm's performance in practice?
- What are the trade-offs between the number of expansion functions (m) and the precision parameters in the quantum subroutines?
- Can the algorithm be extended to handle multi-dimensional optimal stopping problems more efficiently?
- What are the implications of using HHL-like algorithms for solving linear systems in the quantum LSM algorithm?
- How does the quantum algorithm perform in the presence of market frictions or transaction costs, which are common in real financial applications?
- Can the quantum LSM algorithm be adapted to solve other dynamic programming problems beyond finance?

**Future work:**
- Empirical validation of the quantum algorithm on real quantum hardware (e.g., IBM Eagle processor)
- Extension of the algorithm to handle multi-period and multi-dimensional optimal stopping problems
- Improvement of the error bounds to reduce the exponential dependence on T
- Development of noise mitigation techniques to enhance the algorithm's performance on near-term quantum devices
- Comparison of the quantum LSM algorithm with state-of-the-art classical solvers for large-scale problems
- Exploration of alternative quantum subroutines for Monte Carlo estimation to improve the algorithm's efficiency
- Investigation of the algorithm's performance under different smoothness conditions and expansion functions
- Adaptation of the algorithm to solve other dynamic programming problems in finance and beyond
- Integration of the quantum LSM algorithm with classical pre-processing and post-processing steps to optimize performance
- Development of hybrid quantum-classical approaches to leverage the strengths of both paradigms
- Application of the algorithm to real-world financial problems, such as American option pricing and risk management
- Exploration of the algorithm's potential for solving backward stochastic differential equations (BSDEs) and other related problems
## Key ideas
- #idea:quantum-advantage — Quantum LSM algorithm achieves nearly quadratic runtime speedup over classical LSM for stochastic optimal stopping problems (e.g., American option pricing) under theoretical assumptions, with complexity ˜O(T²m⁴/ϵ) vs. classical ˜O(Tm⁶/ϵ²)
- #idea:quantum-advantage — For n-times differentiable continuation values, quantum runtime improves to ˜O(5T/ϵ) vs. classical ˜O((5T/ϵ)²), demonstrating potential for significant speedup in smooth financial models
- #idea:near-term-feasibility — Algorithm leverages quantum access to stochastic processes and quantum Monte Carlo techniques, but feasibility on NISQ devices remains untested due to qubit and noise constraints
- #idea:hybrid-approach — Potential for hybrid quantum-classical implementations to address qubit limitations and noise, though not explicitly proposed in the paper
- #limitation:noise — Theoretical speedup does not account for noise/decoherence in near-term quantum hardware, which could degrade performance and limit practical applicability
- #limitation:data-encoding — Assumes efficient quantum sampling access to Markov chains and payoff functions, but practical encoding of financial data into quantum states remains a significant challenge
- #limitation:no-empirical-validation — Claims are purely theoretical; no empirical validation on real quantum hardware or real-world financial datasets, limiting confidence in real-world performance
## Contradictions
<!-- Step 6 output — where this paper contradicts others -->

## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
