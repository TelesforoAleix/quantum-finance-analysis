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
step1_date: '2026-03-19T11:57:26.288950'
step1_model: Mistral-Large-3
step2_date: '2026-03-19T11:57:33.525838'
step2_model: Mistral-Large-3
step3_date: '2026-03-19T11:58:24.730615'
step3_model: Mistral-Large-3
step4_date: '2026-03-19T11:58:43.694846'
step4_model: Mistral-Large-3
step5_date: '2026-03-19T11:59:03.093004'
step5_model: Mistral-Large-3
step6_date: '2026-03-19T11:59:32.113125'
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
This preprint presents rigorous bounds on the performance of shallow quantum circuits for approximating the ground state energy of local Hamiltonians on bounded-degree graphs. The authors introduce a family of quantum algorithms that improve the approximation ratio achieved by product states, leveraging the variance of the energy. The work extends these results to k-local Hamiltonians and entangled initial states, offering insights into the potential advantages of quantum computing for optimization problems in physics and computer science.
## Methodology
The paper presents a theoretical framework for improving approximation algorithms for bounded-degree local Hamiltonians, focusing on the task of approximating the ground state energy of two-local quantum Hamiltonians on bounded-degree graphs. The authors derive rigorous bounds on the performance of shallow quantum circuits in estimating the ground state energy. The methodology involves starting with an n-qubit product state and applying a variational family of shallow quantum circuits composed of nearest-neighbor commuting gates on the interaction graph. The improvement in energy is analyzed using the variance of the energy of the initial product state. The paper extends the results to k-local Hamiltonians and entangled initial states, and also explores the improvement of approximation ratios for random product states and states prepared by bounded-depth quantum circuits. Theoretical proofs and propositions are provided to establish the bounds and improvements.
## Findings
- [supported] For local Hamiltonians on bounded-degree graphs, the approximation ratio achieved by a product state can be improved by applying a shallow quantum circuit of depth d+1, assuming the variance of the energy satisfies Var_v(H) = Ω(|E|).
- [supported] The energy improvement is proportional to Var_v(H)^2 / (d^2 |E|), where Var_v(H) is the variance of the energy for the initial product state |v⟩.
- [supported] Theorem 1 provides a rigorous lower bound on the energy improvement: ⟨ψ|H|ψ⟩ ≥ ⟨v|H|v⟩ + Ω(Var_v(H)^2 / (d^2 |E|)), where |ψ⟩ is the state after applying the shallow quantum circuit.
- [supported] For locally optimal product states, the energy improvement bound tightens to ⟨ψ|H|ψ⟩ ≥ ⟨v|H|v⟩ + Ω(Var_v(H)^2 / (d |E|)).
- [supported] The results extend to k-local Hamiltonians and entangled initial states prepared by constant-depth quantum circuits, with energy improvement bounds adjusted for lightcone size and locality.
- [speculative] Quantum advantage for approximating ground state energies of local Hamiltonians may emerge due to the inefficiency of classical methods in capturing entanglement, but this remains unproven for general cases.
- [speculative] The authors suggest that shallow quantum circuits could provide a scalable approach for quantum optimization problems in near-term quantum devices, though empirical validation is lacking.
- [supported] For the quantum Max-Cut problem, the approximation ratio of any product state can be improved by a shallow quantum circuit, with the improvement scaling as Ω(r^4 / d), where r is the initial approximation ratio.
- [supported] For random product states on triangle-free graphs, the approximation ratio can be improved by Ω(1/√d) using shallow quantum circuits, matching the performance of known classical local algorithms.
- [speculative] The paper posits that shallow quantum circuits may offer advantages over product-state approximations for quantum optimization, but this claim is not empirically demonstrated on real hardware.

**Results summary:** The paper presents rigorous theoretical results on improving the approximation ratios for ground state energies of local Hamiltonians using shallow quantum circuits. The key contribution is a family of shallow quantum circuits that enhance the energy of product states by an amount proportional to the variance of the energy, scaled by the graph degree and number of edges. The results are extended to k-local Hamiltonians and entangled initial states, with bounds adjusted for circuit depth and lightcone size. Specific applications to the quantum Max-Cut problem and random product states on triangle-free graphs demonstrate improvements in approximation ratios. While the theoretical guarantees are strong, the paper does not provide empirical validation on real quantum hardware, leaving claims of quantum advantage speculative.

**Performance claims:**
- Energy improvement of Ω(Var_v(H)^2 / (d^2 |E|)) for product states on bounded-degree graphs
- Energy improvement of Ω(Var_v(H)^2 / (d |E|)) for locally optimal product states
- Approximation ratio improvement of Ω(r^4 / d) for the quantum Max-Cut problem
- Approximation ratio improvement of Ω(1/√d) for random product states on triangle-free graphs
## Quantum advantage claim
**Classification:** speculative

The paper argues theoretically that shallow quantum circuits could provide advantages over classical product-state approximations for quantum optimization problems, particularly in capturing entanglement. However, these claims are not empirically validated on real quantum hardware, and the results are derived from simulations and theoretical bounds. The extent of quantum advantage remains speculative, as classical methods may still compete effectively for the problem sizes and structures considered.
## Limitations
- The paper is a preprint and has not undergone peer review [inferred]
- The results are primarily theoretical with no empirical validation on real quantum hardware [inferred]
- Assumes bounded-degree graphs, limiting applicability to general graphs or real-world financial networks [inferred]
- The improvement in approximation ratio depends on the variance condition Var_v(H) = Ω(|E|), which may not hold for all product states [stated]
- The shallow quantum circuit depth depends on the graph degree (d+1), which may not scale well for high-degree graphs [stated]
- The optimality of the improvement (Eq. 2) is demonstrated only for specific Hamiltonians and product states [stated]
- The extension to k-local Hamiltonians shows a worse dependence on the degree (Ω(1/d^4)) compared to 2-local Hamiltonians (Ω(1/d^2)) [stated]
- The analysis assumes noiseless quantum operations, which is unrealistic for near-term quantum devices [inferred]
- The improvement strategy is limited to product states or bounded-depth states, excluding more complex entangled states [stated]
- The paper does not compare the proposed algorithm with state-of-the-art classical approximation methods for the same problems [inferred]
## Open questions
- What are the ultimate limits of efficient quantum algorithms for approximating ground state energies of local Hamiltonians?
- Can the quantum PCP conjecture provide stronger limitations on achievable approximation ratios for quantum optimization problems?
- How does the algorithm perform on graphs with higher degrees or more complex topologies beyond bounded-degree graphs?
- What is the impact of noise and decoherence on the performance of the proposed shallow quantum circuits?
- Can the improvement in approximation ratio be extended to more general families of quantum states beyond product states or bounded-depth states?
- How does the proposed algorithm compare with classical approximation algorithms for the same class of problems?
- Can the results be generalized to other types of Hamiltonians relevant to financial services, such as those modeling portfolio optimization or risk analysis?
- What are the implications of the almost-linear NLTS property for the approximation ratios achievable by shallow quantum circuits?
- How can the algorithm be adapted to handle the constraints and objectives specific to financial optimization problems?

**Future work:**
- Empirical validation of the algorithm on real quantum hardware
- Extension of the results to more general graph structures beyond bounded-degree graphs
- Investigation of noise mitigation techniques to improve performance on near-term quantum devices
- Comparison with state-of-the-art classical approximation algorithms for the same problems
- Exploration of the algorithm's applicability to financial optimization problems, such as portfolio optimization or risk analysis
- Development of hybrid quantum-classical algorithms that combine the strengths of both approaches
- Study of the impact of the quantum PCP conjecture on the limits of quantum approximation algorithms
- Generalization of the improvement strategy to more complex quantum states beyond product states or bounded-depth states
- Investigation of the almost-linear NLTS property in the context of local Hamiltonian systems
- Application of the algorithm to other scientific domains, such as materials science or quantum chemistry
## Key ideas
- #idea:quantum-advantage — Shallow quantum circuits improve approximation ratios for ground state energy problems beyond classical product-state methods, with potential applications in portfolio optimization and risk modelling
- #idea:near-term-feasibility — Theoretical bounds suggest near-term applicability of variational quantum algorithms for local Hamiltonian problems on bounded-degree graphs
- #idea:hybrid-approach — The paper bridges quantum optimization with classical approximation techniques, implying hybrid quantum-classical approaches for practical implementation
- #limitation:no-empirical-validation — Theoretical claims lack empirical validation on real quantum hardware, limiting direct applicability to financial use cases
- #limitation:qubit-count — Assumptions about bounded-degree graphs and shallow circuits may not scale to real-world financial problems requiring larger qubit counts
- #limitation:noise — The analysis assumes noiseless quantum operations, which is unrealistic for near-term quantum devices
## Contradictions
<!-- Step 6 output — where this paper contradicts others -->

## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
