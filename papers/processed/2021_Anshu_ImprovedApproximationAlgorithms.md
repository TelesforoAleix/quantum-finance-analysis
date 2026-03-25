---
aliases:
- Improved approximation algorithms for bounded-degree local Hamiltonians
- Improved approximation algorithms bounded
authors:
- Anurag Anshu
- David Gosset
- Karen J. Morenz Korol
- Mehdi Soleimanifar
auto_detected: true
classification: ''
contradiction_flags:
- contradiction:classical-vs-quantum
doi: ''
evidence_type: ''
idea_tags:
- idea:quantum-advantage
- idea:near-term-feasibility
- idea:hybrid-approach
journal_or_venue: arXiv
methodology_tags:
- QAOA
- variational
paper_type: ''
quantum_advantage_claim: theoretical
related_papers: []
relevance_phase1: low
relevance_phase3: low
source_type: preprint
source_type_confidence: high
step1_date: '2026-03-25T15:52:14.262317'
step1_model: gpt-5.1
step2_date: '2026-03-25T15:52:20.996815'
step2_model: gpt-5.1
step3_date: '2026-03-25T15:52:34.401582'
step3_model: gpt-5.4
step4_date: '2026-03-25T15:52:59.196920'
step4_model: gpt-5.4
step5_date: '2026-03-25T15:53:23.626639'
step5_model: gpt-5.4
step6_date: '2026-03-25T15:53:34.216719'
step6_model: gpt-5.4
steps_completed:
- 1
- 2
- 3
- 4
- 5
- 6
tags:
- method/QAOA
- method/variational
- idea/quantum-advantage
- idea/near-term-feasibility
- idea/hybrid-approach
- contradiction/classical-vs-quantum
title: Improved approximation algorithms for bounded-degree local Hamiltonians
topic_tags: []
year: 2021
zotero_key: ''
---

## Abstract summary
The paper studies algorithms for approximating the ground state energy of bounded-degree local quantum Hamiltonians, focusing on two-local interactions and extending to k-local cases. The authors construct families of shallow quantum circuits that, when applied to an initial product state or other low-depth states, provably improve the achieved energy by an amount related to the variance of the Hamiltonian in that state. They also analyze performance on random product states and triangle-free graphs, connecting their quantum algorithms to and generalizing known classical approximation results for bounded-occurrence constraint satisfaction problems.
## Methodology
This arXiv preprint is primarily theoretical, though it presents constructive algorithmic results rather than empirical experiments. The paper develops and analyzes a family of shallow quantum circuits for improving the approximation ratio of an input state when estimating the ground-state or maximum eigenvalue of bounded-degree local Hamiltonians. The core methodology is a rigorous mathematical framework: starting from an n-qubit product state with known mean energy and variance under a 2-local Hamiltonian on a bounded-degree graph, the authors define a variational shallow circuit composed of commuting nearest-neighbor gates and prove lower bounds on the achievable energy improvement. The analysis derives explicit approximation guarantees in terms of the energy variance, graph degree, and number of edges, and extends to k-local Hamiltonians, bounded-depth input states, and random product-state initializations. The work uses theorem-proof style arguments, nested-commutator expansions, variance decompositions via Hamming-weight projectors, combinatorial counting of nonzero terms, and Haar-average calculations for randomized constructions. It also situates the proposed circuit family as a generalization of level-1 QAOA for classical 2-local Hamiltonians, but does not report numerical benchmarking, datasets, simulator runs, or hardware experiments. As a preprint, it should be flagged as non-peer-reviewed.

**Algorithms used:** QAOA
## Findings
- [speculative] The paper proves that for 2-local Hamiltonians on bounded-degree graphs, a depth-(d+1) shallow quantum circuit can improve the energy of an input product state by an amount proportional to Var(H)^2/(d^2|E|), where Var(H) is the energy variance of the input state.
- [speculative] In the typical regime where the input product state has variance Var(H)=Omega(n), the resulting energy improvement is proportional to the number of edges, implying a constant additive improvement in approximation ratio on bounded-degree graphs.
- [speculative] For locally optimal product states, the improvement guarantee strengthens from Omega(Var(H)^2/(d^2|E|)) to Omega(Var(H)^2/(d|E|)).
- [speculative] The authors claim the general bound is essentially tight by constructing examples where the gap to the optimum is only O(Var(H)^2/(d^2|E|)).
- [speculative] The variational circuit family used generalizes level-1 QAOA for 2-local classical Hamiltonians to broader 2-local quantum Hamiltonians.
- [speculative] For the quantum Max-Cut Hamiltonian, any product state can be improved by a shallow quantum circuit, and an initial approximation ratio r is shown to improve to r + Omega(r^4/d).
- [speculative] The results extend beyond product states: for states prepared by a constant-depth circuit with maximum lightcone size l, the paper proves an energy improvement of Omega(Var(H)^2/(l^10 d^2 |E|)).
- [speculative] As a corollary, constant-depth states with Var(H)=Omega(|E|) cannot achieve approximation ratio arbitrarily close to 1 for these bounded-degree local Hamiltonian problems.
- [speculative] For random product-state initialization, the paper proves expected improvement over the random baseline of Omega(quad(H)^2/(d|E|)) on general bounded-degree graphs, where quad(H) measures the weight of two-qubit Pauli interaction terms.
- [speculative] For triangle-free graphs, the expected improvement from random product states strengthens to Omega(quad(H)/sqrt(d)).
- [speculative] The paper further claims that on triangle-free graphs, local classical algorithms can match the asymptotic Omega(1/sqrt(d)) scaling, so shallow quantum circuits are not necessary for that scaling, though they may still further improve the resulting product states.
- [speculative] The authors extend the framework to k-local Hamiltonians and derive a weaker general improvement bound scaling as Omega(Var(H)^2/(2^{O(k)} d^4 |E|)).
- [speculative] The paper argues that shallow quantum circuits can systematically outperform product-state methods for bounded-degree local Hamiltonian approximation under mild variance conditions, but it does not empirically demonstrate this on hardware or numerical benchmarks.

**Results summary:** This preprint presents theoretical performance guarantees for shallow quantum circuits applied to bounded-degree local Hamiltonian approximation. Starting from a product state, the authors prove that a depth-(d+1) circuit can increase the expected energy by Omega(Var(H)^2/(d^2|E|)), with a stronger Omega(Var(H)^2/(d|E|)) bound for locally optimal product states. They show the circuit family generalizes level-1 QAOA and apply the framework to quantum Max-Cut, where a product-state approximation ratio r improves to r + Omega(r^4/d). The paper also extends the analysis to constant-depth input states, random product-state initializations, triangle-free graphs, and k-local Hamiltonians. All results are theoretical derivations and proofs; there are no experimental or simulation-based empirical validations in the provided text, so any practical quantum advantage remains speculative.

**Performance claims:**
- Depth-(d+1) circuit achieves energy improvement Omega(Var(H)^2/(d^2|E|)) from a product-state input
- For locally optimal product states, improvement strengthens to Omega(Var(H)^2/(d|E|))
- Theorem 2 gives improvement Omega(|E| alpha^2 / d) for the commuting-gate variational circuit
- For quantum Max-Cut, an initial approximation ratio r improves to r + Omega(r^4/d)
- For constant-depth input states with maximum lightcone size l, improvement is Omega(Var(H)^2/(l^10 d^2 |E|))
- For random product states on general bounded-degree graphs, expected improvement is Omega(quad(H)^2/(d|E|))
- For triangle-free graphs, expected improvement is Omega(quad(H)/sqrt(d))
- For k-local Hamiltonians, derived improvement bound is Omega(Var(H)^2/(2^{O(k)} d^4 |E|))
## Quantum advantage claim
**Classification:** theoretical

The paper provides rigorous theoretical guarantees that shallow quantum circuits can improve over product-state approximations for bounded-degree local Hamiltonians, but it does not empirically demonstrate quantum advantage on hardware or simulations. As a preprint, any broader advantage over classical methods remains speculative, especially since the paper also notes that classical local algorithms can match the asymptotic scaling in some triangle-free cases.
## Limitations
- Preprint status: the work had not undergone peer review at the time of posting
- The main guarantees are restricted to local Hamiltonians on bounded-degree graphs
- The core improvement result for product states requires two specific conditions: the initial state must be a product state and its energy variance must satisfy Var(H) = Omega(|E|)
- The method does not provide improvement in the purely classical setting when the input is a computational-basis eigenstate, since then the variance is zero
- The authors note that neither high variance alone nor product-state structure alone is sufficient to guarantee an additive-constant improvement in approximation ratio
- For general two-local Hamiltonians, improvement is only guaranteed when the mild-but-nonuniversal variance condition holds; the authors explicitly state this is expected for most but not all product states
- Theorem 3 extends to bounded-depth input states, but the constructed improving circuit U is not constant depth in that case
- The bounded-depth-state guarantee degrades polynomially with lightcone size, with an energy improvement scaling as Omega(Var(H)^2/(ell^10 d^2 |E|)), which may be weak in practice for larger ell
- The extension to k-local Hamiltonians yields a weaker dependence on degree, with Omega(1/d^4) scaling rather than the Omega(1/d^2) obtained for 2-local Hamiltonians
- The paper is primarily theoretical and does not include empirical validation on quantum hardware or numerical benchmarking against practical instances
- [inferred] No comparison is provided against state-of-the-art classical approximation or tensor-network methods on realistic problem instances
- [inferred] No analysis of robustness to hardware noise, gate errors, decoherence, or sampling error is given, limiting near-term implementation relevance
- [inferred] Although motivated by shallow circuits and near-term devices, the work does not quantify resource overheads such as measurement complexity, parameter-setting cost, or compilation constraints on actual hardware
- [inferred] The results concern generic local Hamiltonian approximation and are not specialized to financial-services use cases, so direct applicability to finance is unclear
## Open questions
- What are the ultimate limits of efficient quantum approximation algorithms for local Hamiltonians?
- How much advantage can shallow quantum circuits and variational quantum algorithms offer in general?
- Can the limitation on bounded-depth states be used to exhibit new local Hamiltonian systems with the almost-linear NLTS property?
- Can the k-local extension be improved to recover the stronger Omega(1/d^2) dependence on degree rather than Omega(1/d^4)?
- Under what broader conditions beyond product states and bounded-depth states can approximation ratios be systematically improved by shallow quantum circuits?
- [inferred] How tight are the theoretical lower bounds in practical regimes and for physically relevant Hamiltonian families?
- [inferred] Do the proposed improvements translate into meaningful advantages over classical methods on finite-size instances relevant to applications?
- [inferred] How implementable are the proposed circuits and parameter-selection procedures on NISQ hardware with connectivity and noise constraints?

**Future work:**
- Explore whether the bounded-depth-state limitation can be used to construct new local Hamiltonian systems with the almost-linear NLTS property
- Extend and refine the results for more general families of quantum states beyond product states
- Improve the k-local Hamiltonian analysis to recover Omega(1/d^2) scaling in the degree dependence
- Further study improvements starting from random product states and their relation to classical local algorithms
- [inferred] Provide empirical validation through simulations and experiments on quantum hardware
- [inferred] Benchmark against leading classical approximation algorithms and heuristics
- [inferred] Investigate noise-aware or hardware-efficient implementations of the proposed shallow circuits
- [inferred] Adapt the framework to structured application domains, including optimization problems arising in finance
## Key ideas
- #idea:quantum-advantage — The paper proves shallow variational quantum circuits can improve over product-state approximations for bounded-degree local Hamiltonians, generalizing level-1 QAOA beyond classical 2-local cases.
- #idea:near-term-feasibility — The focus on shallow circuits and bounded-degree interactions is framed as relevant to NISQ-style implementations, though only at a theoretical level.
- #idea:hybrid-approach — The construction is variational and naturally compatible with quantum-classical parameter optimization, even though no practical hybrid workflow is benchmarked.
- #idea:quantum-advantage — For quantum Max-Cut and related local Hamiltonian problems, the paper derives additive approximation improvements tied to input-state variance and graph structure.
## Contradictions
- The paper argues shallow quantum circuits can systematically improve over product-state methods, but it also states that on triangle-free graphs classical local algorithms can match the same asymptotic Omega(1/sqrt(d)) scaling, weakening any broad claim of quantum superiority.
- Although the work suggests near-term promise via shallow circuits, it provides no empirical validation and no noise analysis, so practical claims about outperforming classical methods on realistic instances remain unsubstantiated.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
