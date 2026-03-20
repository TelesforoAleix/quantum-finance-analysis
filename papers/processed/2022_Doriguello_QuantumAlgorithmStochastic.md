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
contradiction_flags:
- contradiction:scalability
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
step1_date: '2026-03-19T23:15:49.594206'
step1_model: Mistral-Large-3
step2_date: '2026-03-19T23:15:53.404169'
step2_model: Mistral-Large-3
step3_date: '2026-03-19T23:15:57.486457'
step3_model: Mistral-Large-3
step4_date: '2026-03-19T23:16:43.106863'
step4_model: Mistral-Large-3
step5_date: '2026-03-19T23:16:51.064193'
step5_model: Mistral-Large-3
step6_date: '2026-03-19T23:17:38.004383'
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
- contradiction/scalability
title: Quantum Algorithm for Stochastic Optimal Stopping Problems with Applications
  in Finance
topic_tags:
- derivatives-pricing
- risk-modelling
year: 2022
zotero_key: ''
---

## Abstract summary
This paper introduces a quantum version of the least squares Monte Carlo (LSM) algorithm for solving stochastic optimal stopping problems, a key challenge in financial applications like American option pricing. The authors propose a quantum algorithm that leverages quantum access to stochastic processes and quantum techniques for Monte Carlo simulation, achieving nearly quadratic speedup over classical LSM under mild assumptions. The work explores the interplay between function approximation and quantum algorithms to enhance computational efficiency in financial modeling.
## Methodology
The paper presents a quantum algorithm for solving stochastic optimal stopping problems, with a specific application to American option pricing in finance. The methodology builds upon the classical least squares Monte Carlo (LSM) algorithm, which combines linear least square regression with Monte Carlo simulation to approximate solutions to optimal stopping problems. The quantum version leverages quantum access to stochastic processes, quantum circuits for computing optimal stopping times, and quantum techniques for Monte Carlo simulations. The algorithm achieves a nearly quadratic speedup in runtime compared to the classical LSM under mild assumptions. The approach involves dynamic programming to solve for optimal stopping times recursively, using quantum subroutines for Monte Carlo to estimate expectation values and quantum circuits to compute stopping times in superposition. The theoretical framework assumes a Markovian stochastic process and employs quantum oracles for sampling and function evaluation.

**Algorithms used:** Quantum Least Squares Monte Carlo, Amplitude Estimation
## Findings
- [supported] The proposed quantum Least Squares Monte Carlo (LSM) algorithm achieves a nearly quadratic speedup in runtime compared to the classical LSM algorithm for stochastic optimal stopping problems under mild assumptions.
- [supported] The quantum algorithm demonstrates a runtime complexity of ~O(T²m⁴/ϵ) compared to the classical algorithm's ~O(Tm⁶/ϵ²), where T is the number of time steps, m is the number of expansion functions, and ϵ is the additive accuracy.
- [supported] For American option pricing using Brownian motion or geometric Brownian motion processes, the quantum algorithm maintains a quadratic speedup over classical methods when continuation values are sufficiently smooth (n-times differentiable).
- [speculative] The quantum advantage may extend to other financial applications of LSM, such as insurance, risk management, and broader optimization problems like quickest detection and sequential Bayesian hypothesis testing.
- [speculative] The quadratic speedup could be practically significant for high-value financial instruments (e.g., American options) where additive precision requirements are stringent (e.g., ϵ ~ 10⁻¹¹).
- [supported] The quantum algorithm leverages quantum subroutines for Monte Carlo (e.g., amplitude estimation) and constructs unitaries to compute stopping times in superposition, enabling recursive dynamic programming in quantum parallel.
- [disputed] The exponential dependence on T (number of time steps) in the runtime complexity may be an artifact of loose error bounds, as classical LSM algorithms are widely used in practice without such limitations.

**Results summary:** The paper presents a quantum algorithm for stochastic optimal stopping problems, with a focus on financial applications like American option pricing. The quantum LSM algorithm achieves a nearly quadratic speedup in runtime compared to the classical LSM algorithm, reducing the complexity from ~O(Tm⁶/ϵ²) to ~O(T²m⁴/ϵ) under mild assumptions. The speedup is demonstrated through simulations and theoretical analysis, with specific case studies for Brownian motion and geometric Brownian motion processes. The algorithm leverages quantum access to stochastic processes, quantum circuits for computing stopping times, and quantum techniques for Monte Carlo. While the results are promising, the paper acknowledges potential limitations, such as the exponential dependence on T and the need for further analysis to assess practical applicability in real-world financial settings.

**Performance claims:**
- Nearly quadratic speedup in runtime compared to classical LSM (quantum: ~O(T²m⁴/ϵ) vs. classical: ~O(Tm⁶/ϵ²))
- For n-times differentiable continuation values, quantum runtime reduces to ~O((5T/ϵ)^(1+4d/n)) compared to classical ~O((5T/ϵ)^(2+6d/n))
- For Brownian motion, quantum runtime improves to ~O((5T/ϵ)^(1+7d/2n)) vs. classical ~O((5T/ϵ)^(2+4d/n))
- For geometric Brownian motion, quantum runtime is ~O((5T/ϵ)^(2/n) * (5T/ϵ)^(1+15d/2n)) vs. classical ~O((5T/ϵ)^(2/n) * (5T/ϵ)^(2+12d/n))
## Quantum advantage claim
**Classification:** theoretical

The quantum advantage is claimed theoretically based on asymptotic runtime complexity improvements demonstrated through simulation. The advantage is not empirically validated on real quantum hardware, and the results depend on assumptions about the smoothness of continuation values and the structure of the underlying stochastic processes. The paper provides a rigorous error analysis and complexity bounds but does not include hardware-specific benchmarks.
## Limitations
- The algorithm assumes quantum access to a stochastic process, which may not be feasible with current quantum hardware [inferred]
- The proposed quantum LSM algorithm requires redoing all previous dynamic programming steps before progressing to the next time step, leading to O(T^2) time steps instead of O(T) in the classical version [inferred]
- The error analysis and final complexities depend on parameters that are implicitly tied to the underlying Markov chain, such as the minimum singular value of matrices At
- The algorithm's performance relies on smoothness assumptions of the continuation values (E[Zτt+1|Xt] ∈ C^n), which may not hold in all financial applications
- The quantum advantage is contingent on the continuation values being n-times differentiable for n = Θ(log(5T/ϵ)/log log(5T/ϵ)), a condition that may not be verifiable in practice [inferred]
- The analysis assumes fixed-point arithmetic with sufficient precision, which may introduce numerical errors in real quantum hardware implementations [inferred]
- The algorithm's runtime has an exponential dependence on T (number of time steps), which may limit practical applicability for long time horizons [inferred]
- The quantum algorithm assumes access to quantum controlled rotations with unit cost, which may not be realistic on near-term quantum devices [inferred]
- The complexity results for geometric Brownian motion are slightly weaker than the general case due to sensitivity of the minimum singular value bounds to the degree of chosen monomials
- The paper does not provide empirical validation of the quantum algorithm on real quantum hardware, limiting assessment of practical performance [inferred]
- The quantum LSM algorithm's advantage is demonstrated under idealized assumptions (e.g., negligible gate errors, perfect qubit coherence), which may not hold in NISQ-era devices [inferred]
## Open questions
- How does the quantum LSM algorithm perform on real quantum hardware with noise and limited qubit counts?
- What is the impact of decoherence and gate errors on the solution quality of the quantum algorithm?
- Can the exponential dependence on T (number of time steps) in the runtime be improved through tighter error bounds?
- How does the algorithm's performance compare to state-of-the-art classical methods for specific financial applications (e.g., American option pricing)?
- What are the practical challenges in implementing quantum sampling access to real-world financial stochastic processes?
- How sensitive is the algorithm's performance to the choice of approximation architecture (e.g., polynomials vs. Chebyshev interpolation)?
- Can the algorithm be extended to handle non-Markovian stochastic processes commonly encountered in finance?
- What are the implications of using quantum subroutines for inner product estimation when m (number of expansion functions) is large?
- How does the algorithm perform when the smoothness assumptions on continuation values are violated?
- What are the trade-offs between the precision parameters (ϵ, δ) and the runtime in practical implementations?

**Future work:**
- Empirical validation of the quantum LSM algorithm on real quantum hardware (e.g., IBM Eagle processor)
- Extension of the algorithm to multi-dimensional forward-backward stochastic differential equations
- Investigation of alternative quantum subroutines for Monte Carlo (e.g., multivariate Monte Carlo estimation) to improve performance
- Development of hybrid quantum-classical approaches to mitigate the O(T^2) time step limitation
- Application of the quantum LSM algorithm to other financial problems (e.g., insurance, risk management) and optimization problems outside finance
- Exploration of quantum algorithms for optimal stopping problems with non-Markovian processes
- Improvement of the error bounds to reduce the exponential dependence on T
- Integration of noise mitigation techniques to enhance performance on NISQ devices
- Comparison of the quantum LSM algorithm with classical methods for specific financial use cases (e.g., American option pricing)
- Development of quantum algorithms for dynamic programming and optimal control problems leveraging the interplay of function approximation and quantum Monte Carlo subroutines
## Key ideas
- #idea:quantum-advantage — Quantum LSM algorithm achieves nearly quadratic runtime speedup over classical LSM for stochastic optimal stopping problems (e.g., American option pricing) under theoretical assumptions, with complexity ~O(T²m⁴/ϵ) vs. classical ~O(Tm⁶/ϵ²)
- #idea:quantum-advantage — For n-times differentiable continuation values, quantum runtime improves to ~O(5T/ϵ) vs. classical ~O((5T/ϵ)²), demonstrating potential for significant speedup in smooth financial models
- #idea:near-term-feasibility — Algorithm leverages quantum access to stochastic processes and quantum Monte Carlo techniques, but feasibility on NISQ devices remains untested due to qubit and noise constraints
- #idea:hybrid-approach — Potential for hybrid quantum-classical implementations to address qubit limitations and noise, though not explicitly proposed in the paper
- #limitation:noise — Theoretical speedup does not account for noise/decoherence in near-term quantum hardware, which could degrade performance and limit practical applicability
- #limitation:data-encoding — Assumes efficient quantum sampling access to Markov chains and payoff functions, but practical encoding of financial data into quantum states remains a significant challenge
- #limitation:no-empirical-validation — Claims are purely theoretical; no empirical validation on real quantum hardware or real-world financial datasets, limiting confidence in real-world performance
- #limitation:qubit-count — Exponential dependence on T (time steps) and qubit requirements may render the algorithm impractical for large-scale financial problems on current hardware
## Contradictions
- #contradiction:scalability — The paper claims a quadratic speedup but acknowledges an exponential dependence on T (time steps) in runtime complexity, which contradicts the practical scalability of the algorithm for long time horizons. This aligns with concerns raised in other works (e.g., [2021_Rebentrost_QuantumAlgorithmsFinance]) about the feasibility of quantum advantage in real-world financial applications.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
