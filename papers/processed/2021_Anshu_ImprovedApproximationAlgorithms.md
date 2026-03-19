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
- QAOA
- variational
- quantum-simulation
paper_type: ''
quantum_advantage_claim: speculative
related_papers: []
relevance_phase1: medium
relevance_phase3: not-yet-assessed
source_type: preprint
source_type_confidence: high
step1_date: '2026-03-18T22:59:39.492892'
step1_model: Mistral-Large-3
step2_date: '2026-03-18T22:59:41.933073'
step2_model: Mistral-Large-3
step3_date: '2026-03-18T23:00:16.343301'
step3_model: Mistral-Large-3
step4_date: '2026-03-18T23:01:23.660958'
step4_model: Mistral-Large-3
step5_date: '2026-03-18T23:01:34.081607'
step5_model: Mistral-Large-3
step6_date: '2026-03-18T23:02:27.130111'
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
- topic/derivatives-pricing
- method/QAOA
- method/variational
- method/quantum-simulation
- idea/quantum-advantage
- idea/near-term-feasibility
- idea/hybrid-approach
title: Improved approximation algorithms for bounded-degree local Hamiltonians
topic_tags:
- portfolio-optimisation
- risk-modelling
- derivatives-pricing
year: 2021
zotero_key: ''
---

## Abstract summary
This preprint presents rigorous algorithms to improve the approximation of ground state energies for local quantum Hamiltonians on bounded-degree graphs. The authors introduce shallow quantum circuits that enhance the performance of product-state approximations, demonstrating energy improvements proportional to the variance of the initial state. The work bridges quantum optimization challenges with classical approximation techniques, offering theoretical bounds for variational quantum algorithms in near-term quantum computing applications.
## Methodology
The paper presents a theoretical analysis of improved approximation algorithms for estimating the ground state energy of local Hamiltonians on bounded-degree graphs. The methodology focuses on deriving rigorous bounds on the performance of shallow quantum circuits in approximating the largest eigenvalue (or ground state energy) of two-local quantum Hamiltonians. The authors propose a variational family of states obtained by applying a quantum circuit composed of nearest-neighbor commuting gates to an initial product state. The key contribution is a theorem (Theorem 1) that guarantees an improvement in the approximation ratio of the energy for product states under specific variance conditions. The proof leverages a second theorem (Theorem 2) that bounds the energy improvement after applying the quantum circuit. The paper extends these results to k-local Hamiltonians and entangled initial states, as well as to random product states, demonstrating generalizations of known algorithms for classical constraint satisfaction problems. The analysis is theoretical, with no empirical experiments or hardware implementations described.

**Algorithms used:** QAOA
## Findings
- [supported] The paper presents a family of shallow quantum circuits that improve the approximation ratio of a given product state for the ground state energy of two-local Hamiltonians on bounded-degree graphs, with an energy improvement proportional to Varv(H)^2 / (d^2 |E|).
- [supported] Theorem 1 demonstrates that for a product state |v⟩ with variance Varv(H) = Ω(|E|), a depth-(d+1) quantum circuit can achieve an energy improvement of Ω(Varv(H)^2 / (d^2 |E|)).
- [supported] Theorem 2 provides a lower bound on the energy improvement using a variational quantum circuit, showing that ⟨ψ|H|ψ⟩ ≥ ⟨v|H|v⟩ + Ω(|E| α^2 / d), where α is defined in Eq. (5).
- [supported] The results extend to k-local Hamiltonians and entangled initial states, with Theorem 3 showing similar energy improvements for states prepared by bounded-depth quantum circuits.
- [speculative] The authors suggest that quantum computers may offer advantages for approximating ground state energies of local Hamiltonians, though the extent of quantum advantage for low-temperature properties remains unknown.
- [speculative] The paper posits that shallow quantum circuits could provide improvements over classical product-state approximations for quantum optimization problems, but notes that no general treatment of variational quantum algorithms' efficacy exists.
- [speculative] The authors claim that their algorithm generalizes the performance guarantees of known algorithms for bounded-occurrence classical constraint satisfaction problems when applied to random product states.
- [speculative] The paper suggests that their results could inform the development of new local Hamiltonian systems with the almost-linear NLTS (No Low-energy Trivial States) property.

**Results summary:** The paper rigorously analyzes the performance of shallow quantum circuits in approximating the ground state energy of local Hamiltonians on bounded-degree graphs. It introduces a method to improve the approximation ratio of product states using depth-(d+1) quantum circuits, achieving an energy gain proportional to the variance of the energy squared divided by the degree and number of edges. The results are extended to k-local Hamiltonians and states prepared by bounded-depth circuits, with theoretical guarantees provided for energy improvements. The work also explores applications to quantum Max-Cut and classical constraint satisfaction problems, demonstrating how shallow quantum circuits can enhance approximation ratios beyond classical product-state methods. However, the quantum advantage claims remain speculative, as the results are theoretical and not empirically validated on real hardware.

**Performance claims:**
- Energy improvement of Ω(Varv(H)^2 / (d^2 |E|)) for product states using depth-(d+1) quantum circuits
- Energy improvement of Ω(|E| α^2 / d) using variational quantum circuits, where α is defined in Eq. (5)
- For quantum Max-Cut, approximation ratio improvement from r to r + Ω(r^4 / d) for product states
## Quantum advantage claim
**Classification:** speculative

The paper presents theoretical results suggesting that shallow quantum circuits can improve approximation ratios for ground state energy problems beyond classical product-state methods. However, these claims are speculative as they are not empirically demonstrated on real quantum hardware and rely on assumptions about variance and graph structure.
## Limitations
- The paper is a preprint and has not undergone peer review, which may affect the validity and robustness of the results [inferred]
- The results are primarily theoretical with rigorous bounds, but lack empirical validation on real quantum hardware [inferred]
- Assumes bounded-degree graphs for local Hamiltonians, limiting generalizability to arbitrary graph structures [inferred]
- The improvement in approximation ratio is proportional to Varv(H)^2 / (d^2 |E|), which may be small for certain Hamiltonians or initial states
- Condition (i) (Varv(H) = Ω(|E|)) is not satisfied for classical Hamiltonians where |v⟩ is a computational basis state, limiting applicability to purely classical optimization problems
- The optimality of the improvement (Eq. 2) is demonstrated only for specific Hamiltonians and product states, not universally [inferred]
- The quantum circuits used are shallow (depth d+1), but the energy improvement may not scale favorably for larger or more complex systems [inferred]
- The extension to k-local Hamiltonians is discussed in the supplemental material but not fully explored in the main text [inferred]
- The paper does not compare the proposed algorithm with state-of-the-art classical approximation methods for the same problems [inferred]
- The results for bounded-depth states (Theorem 3) require a non-constant-depth circuit U, which may limit practical implementation on near-term quantum devices [inferred]
- The improvement for random product states (Theorem 4) is probabilistic and may not guarantee consistent performance across all instances [inferred]
- The paper does not address noise or error mitigation techniques, which are critical for real-world quantum hardware [inferred]
## Open questions
- What are the ultimate limits of efficient quantum algorithms for approximating the ground state energy of local Hamiltonians?
- Can the quantum PCP conjecture provide stronger limitations on achievable approximation ratios for local Hamiltonians?
- How does the performance of shallow quantum circuits compare to deeper variational quantum algorithms for ground state preparation?
- Can the results be extended to Hamiltonians with unbounded-degree graphs or more complex interaction structures?
- What is the impact of noise and decoherence on the energy improvements achieved by the proposed shallow quantum circuits?
- Are there specific classes of Hamiltonians where the proposed algorithm fails to provide meaningful improvements?
- How can the algorithm be adapted to improve approximation ratios for classical optimization problems where Varv(H) = 0?
- Can the results be used to exhibit new local Hamiltonian systems with the almost-linear NLTS property?
- What are the trade-offs between circuit depth and approximation ratio improvement in practical implementations?
- How does the algorithm perform on real-world financial optimization problems, such as portfolio optimization or risk analysis?

**Future work:**
- Empirical validation of the proposed algorithms on real quantum hardware (e.g., IBM Eagle processor)
- Extension of the results to k-local Hamiltonians and more general interaction terms
- Comparison of the proposed quantum algorithms with state-of-the-art classical approximation methods
- Exploration of noise mitigation techniques to improve the robustness of the algorithm on near-term quantum devices
- Investigation of the algorithm's performance on specific financial optimization problems, such as portfolio optimization or option pricing
- Development of hybrid quantum-classical algorithms that combine the strengths of shallow quantum circuits and classical optimization techniques
- Study of the algorithm's scalability to larger systems and its applicability to industry-relevant problem sizes
- Extension of the results to entangled initial states beyond product states
- Exploration of the algorithm's potential to exhibit new local Hamiltonian systems with the almost-linear NLTS property
- Application of the algorithm to other domains, such as materials science or quantum chemistry, where ground state energy estimation is critical
## Key ideas
- #idea:quantum-advantage — Shallow quantum circuits improve approximation ratios for ground state energy problems beyond classical product-state methods, with potential applications in portfolio optimization and risk modelling
- #idea:near-term-feasibility — Theoretical bounds suggest near-term applicability of variational quantum algorithms for local Hamiltonian problems on bounded-degree graphs
- #idea:hybrid-approach — The paper bridges quantum optimization with classical approximation techniques, implying hybrid quantum-classical approaches for practical implementation
- #limitation:no-empirical-validation — Theoretical claims lack empirical validation on real quantum hardware, limiting direct applicability to financial use cases
- #limitation:qubit-count — Assumptions about bounded-degree graphs and shallow circuits may not scale to real-world financial problems requiring larger qubit counts
## Contradictions
<!-- Step 6 output — where this paper contradicts others -->

## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
