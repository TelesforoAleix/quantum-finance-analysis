---
aliases:
- 'Quantum speed-ups for solving semidefinite relaxations of

  polynomial optimization'
- Quantum speed ups solving
authors:
- Daniel Stilck França
- Ngoc Hoang Anh Mai
auto_detected: true
classification: ''
contradiction_flags:
- contradiction:scalability
doi: ''
evidence_type: ''
idea_tags:
- idea:quantum-advantage
- idea:near-term-feasibility
journal_or_venue: arXiv
methodology_tags:
- quantum-simulation
- variational
paper_type: ''
quantum_advantage_claim: speculative
related_papers: []
relevance_phase1: high
relevance_phase3: medium
source_type: preprint
source_type_confidence: high
step1_date: '2026-03-25T16:08:18.970743'
step1_model: gpt-5.1
step2_date: '2026-03-25T16:08:27.975775'
step2_model: gpt-5.1
step3_date: '2026-03-25T16:08:43.760943'
step3_model: gpt-5.4
step4_date: '2026-03-25T13:40:31.149691'
step4_model: gpt-5.1
step5_date: '2026-03-20T15:32:35.108765'
step5_model: Mistral-Large-3
step6_date: '2026-03-20T15:33:14.584349'
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
- topic/asset-pricing
- method/quantum-simulation
- method/variational
- idea/quantum-advantage
- idea/near-term-feasibility
- contradiction/scalability
title: 'Quantum speed-ups for solving semidefinite relaxations of

  polynomial optimization'
topic_tags:
- portfolio-optimisation
- risk-modelling
- asset-pricing
year: 2025
zotero_key: ''
---

## Abstract summary
The paper develops quantum algorithms, based on matrix multiplicative weights and block-encoding techniques, to approximately solve semidefinite programming relaxations (Lasserre/SOS and moment hierarchies) of polynomial optimization problems. It analyzes normalization, sparsity, and stability conditions under which these quantum SDP solvers achieve super-quadratic speedups in the problem dimension compared to classical interior-point methods, at the cost of worse dependence on precision. As a key application, the authors show how their framework yields improved asymptotic complexity for portfolio optimization problems formulated as polynomial optimization over the simplex or ball.
## Methodology
This preprint is a theoretical and algorithmic work that develops and analyzes quantum algorithms for approximating Lasserre / sum-of-squares (SOS) and moment semidefinite relaxations of polynomial optimization problems, with a specific application to portfolio optimization. The authors start from the standard SOS and moment SDP formulations of polynomial optimization (unconstrained, inequality-constrained, and simplex-constrained). They then systematically transform these SDPs into a standard form amenable to matrix multiplicative weights (MMW)–based quantum SDP solvers (Hamiltonian updates). Key steps include: (1) deriving coefficient-matching matrices B^(γ) and their constrained variants B_g^(γ) to express moment and localizing matrices as sparse linear combinations of basis matrices; (2) proving normalization and bounded/constant-trace properties via rescaling of objective and constraint polynomials, using moment-based inequalities and structural assumptions (e.g., solutions in ℓ1-balls, simplex constraints, or ball constraints); (3) constructing efficient block encodings of the sparse matrices B^(γ) and B_g^(γ) without QRAM, using reversible arithmetic and controlled-swap circuits with O(n log k) gates; (4) applying the quantum Hamiltonian updates algorithm (a quantum MMW SDP solver) combined with a classical binary search on the objective value to approximate the optimal SDP value, with rigorous complexity and accuracy bounds that depend on problem dimension n, relaxation order k, sparsity s_g, and precision ε; and (5) for portfolio optimization, mapping a normalized mean-variance quadratic program into a degree-2 polynomial optimization over the simplex, constructing a suitable Lebesgue measure on a small hyper-rectangle inside the feasible region to certify Assumption 2 (a lower bound on smallest eigenvalues of moment/localizing matrices), and then instantiating the general quantum SDP framework to obtain an O(n ε^-4 + sqrt(n) ε^-5) quantum runtime versus classical interior-point O(n^{ω+1} log(1/ε)). The methodology is entirely analytical: no numerical experiments are run; instead, the paper provides formal proofs of strong duality, finite convergence in some cases, trace bounds, dual norm bounds, and detailed asymptotic complexity comparisons between classical interior-point, classical MMW, and quantum MMW solvers.

**Algorithms used:** Hamiltonian updates, Matrix Multiplicative Weights (MMW), Quantum Gibbs sampling (as a subroutine, via prior work), Quantum SDP solving (Brandão–Svore / van Apeldoorn–Gilyén style), Interior-point methods (classical, for comparison), Quantum interior-point methods (for comparison)
## Experiment details
<!-- Step 3 output — experiment replication details -->

## Findings
- [supported] The quantum algorithm based on matrix multiplicative weights achieves a runtime of O(n^k ε^{-4} + n^{k/2} ε^{-5}) for approximating Lasserre’s hierarchy values for polynomial optimization under specific conditions (e.g., optimal value attained within an ℓ1-ball or simplex constraints).
- [supported] For unconstrained polynomial optimization, the quantum algorithm achieves a runtime of O((n^{2k})^{1/2} + (1/ε) n^{k/2}) ε^{-4}) to approximate the optimal value with accuracy ε^{1-r}, where r is the radius of the ℓ1-ball containing the optimal solution.
- [supported] For inequality-constrained polynomial optimization, the quantum algorithm achieves a runtime of O(s_g (n^{2k}^{1/2} + (Σ_{i=0}^m n^{k-d_i})^{1/2} (1/ε)) ε^{-4}), where s_g bounds the sparsity of coefficient-matching matrices.
- [supported] The quantum algorithm for portfolio optimization achieves a runtime of O(n ε^{-4} + √n ε^{-5}), improving over the classical O(n^{ω+1} log(1/ε)) bound with ω ≈ 2.373.
- [speculative] The paper claims a super-quadratic speedup in problem dimension for computing Lasserre relaxations under the stated assumptions, but this is not empirically validated on real hardware.
- [speculative] The quantum advantage is argued to emerge from the ability to implement block encodings without QRAM, but this remains theoretical without empirical demonstration.
- [supported] The quantum algorithm demonstrates improved asymptotic performance for large-scale polynomial optimization problems compared to classical and quantum interior-point methods, despite worse dependence on the precision parameter ε.

**Results summary:** The paper presents quantum algorithms for solving semidefinite relaxations of polynomial optimization problems, leveraging the matrix multiplicative weights framework. Under specific structural assumptions (e.g., optimal solutions within an ℓ1-ball or simplex constraints), the quantum algorithms achieve runtime improvements over classical methods, with a super-quadratic speedup in problem dimension. For example, the quantum algorithm for portfolio optimization achieves O(n ε^{-4} + √n ε^{-5}) runtime, compared to the classical O(n^{ω+1} log(1/ε)). However, the claimed speedups are theoretical and rely on simulations, with no empirical validation on real quantum hardware. The algorithms also exhibit a polynomial dependence on the precision parameter ε, which is worse than the logarithmic dependence of classical interior-point methods.

**Performance claims:**
- O(n^k ε^{-4} + n^{k/2} ε^{-5}) runtime for approximating Lasserre’s hierarchy values
- O((n^{2k})^{1/2} + (1/ε) n^{k/2}) ε^{-4}) runtime for unconstrained polynomial optimization
- O(s_g (n^{2k}^{1/2} + (Σ_{i=0}^m n^{k-d_i})^{1/2} (1/ε)) ε^{-4}) runtime for inequality-constrained polynomial optimization
- O(n ε^{-4} + √n ε^{-5}) runtime for portfolio optimization
- Super-quadratic speedup in problem dimension compared to classical methods
## Quantum advantage claim
**Classification:** speculative

The claimed quantum advantage is based on theoretical runtime improvements derived from simulations. The paper argues for a super-quadratic speedup in problem dimension under specific conditions, but these claims are not empirically validated on real quantum hardware. The advantage is contingent on assumptions like sparsity of input matrices and proper normalization, which may not hold in all practical scenarios.
## Limitations
- Assumptions required for quantum speedup (e.g., bounded-trace feasible region, sparsity of coefficient-matching matrices) may not hold for all polynomial optimization problems [inferred]
- Super-quadratic speedup is achieved at the cost of polynomial scaling in precision parameter ε⁻¹, which may limit practical applicability for high-precision requirements
- Quantum algorithm runtime depends on the maximum number of nonzero entries per row of coefficient-matching matrices (s_g), which could be large for dense problems [inferred]
- Exactness assumption (λ_k = f⋆) is required for some results, which may not hold for all problems or may be hard to verify
- Structural constraints (e.g., solution lying in ℓ₁-ball, simplex constraints) are necessary for accuracy guarantees, limiting generality
- Lack of empirical validation on real quantum hardware (preprint status) [inferred]
- No comparison with state-of-the-art classical solvers for specific financial applications like portfolio optimization [inferred]
- Block encoding constructions assume oracle access to polynomial coefficients, which may not be trivial to implement in practice [inferred]
- Results in Appendix B (more general cases) are less conclusive, indicating limitations in broader applicability [inferred]
- No noise mitigation techniques considered, which may affect performance on near-term quantum devices [inferred]
- Preprint status implies lack of peer review, which may affect reliability of claims [inferred]
## Open questions
- How does the quantum algorithm perform for problems where the exactness assumption (λ_k = f⋆) does not hold?
- What is the impact of decoherence and noise on the practical performance of these quantum algorithms?
- Can the quantum speedup be maintained when scaling to larger problem dimensions (n > 100) for financial applications?
- How do the quantum algorithms compare with classical methods for real-world financial datasets?
- What are the practical challenges in implementing block encodings for financial optimization problems?
- Can the polynomial dependence on ε⁻¹ be improved to make the algorithms more competitive with classical interior-point methods?
- How sensitive are the results to violations of the structural constraints (e.g., solution not lying in ℓ₁-ball)?
- What are the implications of the real radical property assumption for financial optimization problems?
- Can the algorithms be extended to handle inequality constraints more efficiently without exponential growth in problem size?

**Future work:**
- Test the quantum algorithms on real quantum hardware (e.g., IBM Eagle processor) to validate theoretical claims
- Extend the approach to multi-period portfolio optimization problems
- Investigate noise mitigation techniques to improve performance on near-term quantum devices
- Develop hybrid quantum-classical approaches to handle problems where exactness assumptions do not hold
- Compare the quantum algorithms with state-of-the-art classical solvers for specific financial applications
- Explore methods to reduce the polynomial dependence on ε⁻¹ in the runtime
- Investigate the applicability of the algorithms to other financial optimization problems (e.g., risk management, option pricing)
- Develop efficient implementations of block encodings for financial datasets
- Study the impact of problem structure (e.g., sparsity, constraint types) on quantum algorithm performance
- Extend the results to handle more general polynomial optimization problems without strict structural constraints
## Key ideas
- #idea:quantum-advantage — Quantum algorithm achieves O(n ε^{-4} + √n ε^{-5}) runtime for portfolio optimization, improving over classical O(n^{ω+1} log(1/ε)) bound with ω ≈ 2.373
- #idea:quantum-advantage — Claims super-quadratic speedup in problem dimension for Lasserre relaxations under specific structural assumptions (e.g., ℓ1-ball constraints)
- #idea:near-term-feasibility — Proposes matrix multiplicative weights framework for polynomial optimization, but acknowledges lack of empirical validation on real hardware
- #limitation:no-empirical-validation — Theoretical speedup claims are not backed by experiments on real quantum processors
- #limitation:noise — No noise mitigation techniques considered, which may degrade performance on near-term devices
- #limitation:data-encoding — Block encoding constructions assume oracle access to polynomial coefficients, posing practical implementation challenges
## Contradictions
- #contradiction:scalability — Claims super-quadratic speedup in problem dimension, but runtime exhibits polynomial dependence on ε⁻¹ (worse than classical logarithmic dependence), potentially limiting practical scalability for high-precision financial applications
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
