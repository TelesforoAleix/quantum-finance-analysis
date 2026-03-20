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
contradiction_flags: []
doi: 10.48550/arXiv.2105.01193
evidence_type: ''
idea_tags:
- idea:quantum-advantage
- idea:near-term-feasibility
- idea:hybrid-approach
journal_or_venue: arXiv
methodology_tags:
- variational
- quantum-simulation
paper_type: ''
quantum_advantage_claim: speculative
related_papers: []
relevance_phase1: medium
relevance_phase3: not-yet-assessed
source_type: preprint
source_type_confidence: high
step1_date: '2026-03-19T23:01:30.285245'
step1_model: Mistral-Large-3
step2_date: '2026-03-19T23:02:33.590550'
step2_model: Mistral-Large-3
step3_date: '2026-03-19T23:02:39.604317'
step3_model: Mistral-Large-3
step4_date: '2026-03-19T23:02:50.931192'
step4_model: Mistral-Large-3
step5_date: '2026-03-19T23:03:01.935326'
step5_model: Mistral-Large-3
step6_date: '2026-03-19T23:03:06.600264'
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
- method/variational
- method/quantum-simulation
- idea/quantum-advantage
- idea/near-term-feasibility
- idea/hybrid-approach
title: Improved approximation algorithms for bounded-degree local Hamiltonians
topic_tags:
- portfolio-optimisation
- risk-modelling
year: 2021
zotero_key: ''
---

## Abstract summary
This preprint presents rigorous bounds on the performance of shallow quantum circuits for approximating the ground state energy of local Hamiltonians on bounded-degree graphs. The authors introduce a family of quantum algorithms that improve the approximation ratio achieved by product states, demonstrating that shallow circuits can systematically lower energy estimates proportional to the variance of the initial state. The work extends known results for classical constraint satisfaction problems to quantum settings and explores applications in quantum Max-Cut and other optimization tasks.
## Methodology
The paper presents a theoretical framework for improving the approximation ratios of product states in estimating the ground state energy of local Hamiltonians on bounded-degree graphs using shallow quantum circuits. The core methodology involves deriving rigorous bounds on the performance of these circuits. Specifically, the authors consider a Hamiltonian defined on a d-regular graph and use a variational family of states obtained by applying a quantum circuit composed of nearest-neighbor commuting gates to an initial product state. The improvement in energy is quantified through theorems that relate the variance of the Hamiltonian in the initial state to the achievable energy increase. The paper extends these results to k-local Hamiltonians and entangled initial states, and also explores improvements for random product states and bounded-depth states. The proofs rely on detailed mathematical derivations, including the use of commutator expansions, variance calculations, and properties of quantum circuits on triangle-free graphs.
## Findings
- [supported] The paper presents a family of shallow quantum circuits that improve the approximation ratio of product states for estimating the ground state energy of two-local quantum Hamiltonians on bounded-degree graphs, with an energy improvement proportional to Var^2/n, where Var is the variance of the energy of the initial product state.
- [supported] Theorem 1 demonstrates that given a product state |v⟩, a depth-(d+1) quantum circuit U can be efficiently computed such that the state |ψ⟩ = U|v⟩ achieves an energy improvement of Ω(Var_v(H)^2 / (d^2|E|)).
- [supported] The improvement is optimal in the sense that there exist Hamiltonians and product states where the energy difference from the maximum eigenvalue is bounded by O(Var_v(H)^2 / (d^2|E|)).
- [supported] For locally optimal product states, the energy improvement bound is strengthened to Ω(Var_v(H)^2 / (d|E|)).
- [supported] Theorem 2 provides a lower bound on the energy improvement after applying a variational quantum circuit V(θ) to a product state, with the improvement proportional to |E|α^2/d, where α is a parameter defined by the commutator of local Hamiltonian terms and Pauli operators.
- [supported] The results extend to k-local Hamiltonians and entangled initial states prepared by constant-depth quantum circuits, with energy improvements scaling similarly based on variance and graph properties.
- [speculative] The paper suggests that quantum computers may offer advantages for approximating ground state energies of local Hamiltonians, though the extent of quantum advantage for broader simulation tasks remains unknown.
- [speculative] The authors propose that their results could inform the development of new local Hamiltonian systems with the almost-linear No Low-energy Trivial States (NLTS) property.
- [speculative] The findings generalize known algorithms for bounded-occurrence classical constraint satisfaction problems, implying potential broader applicability of shallow quantum circuits in optimization.

**Results summary:** The paper rigorously analyzes the performance of shallow quantum circuits in approximating the ground state energy of local Hamiltonians on bounded-degree graphs. It introduces a method to improve the approximation ratio of product states using shallow quantum circuits, with energy improvements quantified by the variance of the initial state's energy. The results are supported by theorems demonstrating specific bounds on energy improvements, which are optimal under certain conditions. The work extends to k-local Hamiltonians and entangled initial states, and generalizes algorithms for classical constraint satisfaction problems. While the paper provides strong empirical and theoretical support for its claims, it acknowledges that the broader quantum advantage for simulation tasks remains speculative.

**Performance claims:**
- Energy improvement of Ω(Var_v(H)^2 / (d^2|E|)) for product states using depth-(d+1) quantum circuits
- Energy improvement of Ω(Var_v(H)^2 / (d|E|)) for locally optimal product states
- Energy improvement of Ω(|E|α^2/d) for variational quantum circuits applied to product states
- Energy improvement of Ω(Var(H)^2 / (ℓ^10 d^2 |E|)) for states prepared by bounded-depth quantum circuits with maximum lightcone size ℓ
- Energy improvement of Ω(quad(H)^2 / (d|E|)) for random product states, and Ω(quad(H)/√d) for triangle-free graphs
## Quantum advantage claim
**Classification:** speculative

The paper suggests potential quantum advantages for approximating ground state energies of local Hamiltonians, particularly through the use of shallow quantum circuits to improve approximation ratios beyond classical product state methods. However, these claims are based on theoretical analysis and simulations, with no empirical demonstration on real quantum hardware. The broader quantum advantage for simulation tasks remains unproven and is noted as an open question.
## Limitations
- The paper is a preprint and has not undergone peer review [inferred]
- Assumes bounded-degree graphs for local Hamiltonians, limiting generalizability to arbitrary graph structures [inferred]
- Requires the variance condition Var_v(H) = Ω(|E|) for product states, which may not hold for all Hamiltonians [stated]
- The improvement in approximation ratio is proportional to Var_v(H)^2 / (d^2 |E|), which may be small for large graphs [stated]
- The algorithm's performance is rigorously analyzed only for two-local and k-local Hamiltonians, not for more general cases [stated]
- The quantum circuit depth scales with the degree (d + 1), which may limit practical implementation on near-term devices [inferred]
- The analysis assumes noiseless quantum operations, ignoring hardware noise and errors [inferred]
- The improvement bounds are asymptotic and may not translate to significant practical gains for small-scale problems [inferred]
- The paper does not provide empirical validation or benchmarking against classical methods [inferred]
- The extension to k-local Hamiltonians results in a worse dependence on the degree (Ω(1/d^4)) compared to two-local Hamiltonians (Ω(1/d^2)) [stated]
- The locally optimal product state condition is restrictive and may not be satisfied in many practical scenarios [inferred]
- The random product state improvement relies on triangle-free graphs, which may not be applicable to all problem instances [stated]
## Open questions
- What are the ultimate limits of efficient quantum approximation algorithms for local Hamiltonians beyond bounded-degree graphs?
- Can the quantum PCP conjecture provide stronger limitations on achievable approximation ratios for quantum optimization problems?
- How does the algorithm perform on real-world financial optimization problems with complex, non-regular graph structures?
- What is the impact of hardware noise and decoherence on the algorithm's performance in practical implementations?
- Can the improvement bounds be tightened for k-local Hamiltonians to match the Ω(1/d^2) scaling of two-local Hamiltonians?
- How does the algorithm compare to state-of-the-art classical approximation methods for specific problems like portfolio optimization?
- What are the implications of the almost-linear NLTS property for the approximation ratios achievable by shallow quantum circuits?
- Can the algorithm be extended to handle mixed states or noisy initial states in practical settings?
- What is the trade-off between circuit depth and approximation ratio improvement in near-term quantum devices?
- How does the variance condition Var_v(H) = Ω(|E|) influence the algorithm's applicability to real-world datasets?

**Future work:**
- Extend the results to more general graph structures beyond bounded-degree graphs
- Investigate the impact of noise and error mitigation techniques on the algorithm's performance
- Benchmark the algorithm against classical approximation methods for specific financial optimization problems
- Explore the connection between the algorithm's performance and the quantum PCP conjecture
- Develop hybrid quantum-classical algorithms that combine shallow quantum circuits with classical optimization techniques
- Test the algorithm on real quantum hardware to validate theoretical performance guarantees
- Improve the dependence on the degree for k-local Hamiltonians to achieve Ω(1/d^2) scaling
- Study the algorithm's performance on mixed states or noisy initial states relevant to practical applications
- Investigate the potential of the algorithm for multi-period portfolio optimization and other dynamic financial problems
- Explore the use of the algorithm in other domains such as materials science and quantum chemistry
- Develop methods to certify the approximation ratio achieved by the algorithm in practical settings
- Extend the analysis to include higher-depth quantum circuits and their impact on approximation ratios
## Key ideas
- #idea:quantum-advantage — Shallow quantum circuits improve approximation ratios for ground state energy problems beyond classical product-state methods, with potential applications in portfolio optimization and risk modelling via QUBO formulations or Hamiltonian-based approaches
- #idea:near-term-feasibility — Theoretical bounds suggest near-term applicability of variational quantum algorithms for local Hamiltonian problems on bounded-degree graphs, though scalability remains a challenge
- #idea:hybrid-approach — The paper bridges quantum optimization with classical approximation techniques, implying hybrid quantum-classical approaches for practical implementation in financial services
- #limitation:no-empirical-validation — Theoretical claims lack empirical validation on real quantum hardware, limiting direct applicability to financial use cases
- #limitation:qubit-count — Assumptions about bounded-degree graphs and shallow circuits may not scale to real-world financial problems requiring larger qubit counts
- #limitation:noise — The analysis assumes noiseless quantum operations, which is unrealistic for near-term quantum devices and could degrade performance in risk-modelling or portfolio-optimisation tasks
## Contradictions
<!-- Step 6 output — where this paper contradicts others -->

## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
