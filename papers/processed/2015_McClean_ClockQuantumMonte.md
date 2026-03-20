---
aliases:
- 'Clock Quantum Monte Carlo: an imaginary-time method for real-time quantum dynamics'
- Clock Quantum Monte Carlo
authors:
- Jarrod R. McClean
- Alán Aspuru-Guzik
auto_detected: true
classification: ''
contradiction_flags: []
doi: 10.48550/arXiv.1410.1877
evidence_type: ''
idea_tags:
- idea:near-term-feasibility
- idea:hybrid-approach
journal_or_venue: arXiv
methodology_tags:
- quantum-simulation
- classical-simulation
paper_type: ''
quantum_advantage_claim: not-applicable
related_papers: []
relevance_phase1: medium
relevance_phase3: not-yet-assessed
source_type: peer-reviewed-theoretical
source_type_confidence: high
step1_date: '2026-03-19T22:45:39.335241'
step1_model: Mistral-Large-3
step2_date: '2026-03-19T22:45:41.939196'
step2_model: Mistral-Large-3
step3_date: '2026-03-19T22:45:54.048596'
step3_model: Mistral-Large-3
step4_date: '2026-03-19T22:46:01.370156'
step4_model: Mistral-Large-3
step5_date: '2026-03-19T22:46:11.806861'
step5_model: Mistral-Large-3
step6_date: '2026-03-19T22:46:16.340690'
step6_model: Mistral-Large-3
steps_completed:
- 1
- 2
- 3
- 4
- 5
- 6
tags:
- method/quantum-simulation
- method/classical-simulation
- idea/near-term-feasibility
- idea/hybrid-approach
title: 'Clock Quantum Monte Carlo: an imaginary-time method for real-time quantum
  dynamics'
topic_tags: []
year: 2014
zotero_key: ''
---

## Abstract summary
This paper introduces a novel method combining the Feynman-Kitaev Clock construction with Full Configuration Interaction Quantum Monte Carlo (FCIQMC) to simulate real-time quantum dynamics. The approach reformulates unitary quantum evolution as a ground-state eigenvalue problem, enabling the use of Monte Carlo techniques to mitigate the curse of dimensionality. The authors demonstrate the method's applicability through quantum circuit examples and propose techniques to reduce the dynamical sign problem via time-dependent basis rotations, while also highlighting its potential for parallel-in-time computation.
## Methodology
The paper presents a theoretical framework combining the Feynman-Kitaev Clock construction with the Full Configuration Interaction Quantum Monte Carlo (FCIQMC) method to address quantum dynamics problems. The Feynman-Kitaev Clock maps unitary quantum dynamics to a ground state eigenvalue problem of a Hermitian Hamiltonian, termed the Clock Hamiltonian. The authors adapt the FCIQMC method, originally designed for fermionic ground state problems, to simulate the real-time evolution of quantum systems by treating the Clock Hamiltonian. The methodology involves deriving the Clock Hamiltonian from a time-embedded discrete variational principle, applying the FCIQMC algorithm to this Hamiltonian, and analyzing the manifestation of the dynamical sign problem. The paper also introduces a technique to mitigate the sign problem through time-dependent basis rotations and explores the parallel-in-time scaling of the method for efficient computation on parallel architectures.

**Algorithms used:** FCIQMC (Full Configuration Interaction Quantum Monte Carlo)
## Findings
- [supported] The Feynman-Kitaev Clock construction maps general unitary quantum dynamics to a Hermitian ground state eigenvalue problem, enabling the application of quantum Monte Carlo methods to real-time quantum dynamics.
- [supported] The Full Configuration Interaction Quantum Monte Carlo (FCIQMC) method is adapted to the Clock Hamiltonian, providing a new technique for studying quantum dynamics problems with numerical examples from quantum circuits.
- [supported] The dynamical sign problem in quantum Monte Carlo simulations is mitigated through time-dependent basis rotations, reducing the number of walkers required for sign-coherent sampling in non-trivial quantum circuits.
- [supported] The Clock Quantum Monte Carlo method leverages parallelism in Monte Carlo techniques and time locality to achieve effective parallel-in-time simulation, with demonstrated parallel efficiencies of over 95% on 2 processors and 70% on 8 processors.
- [speculative] The severity of the sign problem depends on the form of quantum operations, with quasi-classical operations exhibiting less severe sign problems compared to non-quasi-classical rotations.
- [speculative] Basis rotations analogous to the interaction picture in quantum dynamics can mitigate the sign problem to an arbitrary extent, though finding optimal rotations may be as difficult as solving the quantum evolution problem exactly.
- [speculative] The critical number of walkers (nc) required for sign-coherent sampling may scale exponentially with system size and linearly with real-time, but could be much smaller for specific dynamical problems of interest.

**Results summary:** The paper introduces a novel method, Clock Quantum Monte Carlo, which combines the Feynman-Kitaev Clock construction with the FCIQMC technique to simulate real-time quantum dynamics as a ground state eigenvalue problem. The authors demonstrate the method's applicability to quantum circuits and show that time-dependent basis rotations can significantly mitigate the dynamical sign problem. Numerical examples illustrate the transition from sign-incoherent to sign-coherent sampling as the number of walkers increases. The method also exhibits strong parallel scaling properties, making it suitable for modern many-core computational architectures. While the method shows promise, the severity of the sign problem remains dependent on the nature of the quantum operations and system size.

**Performance claims:**
- Parallel efficiencies of over 95% with 2 processors and 70% with 8 processors for parallel-in-time simulations
- Reduction in the number of walkers required for sign-coherent sampling through time-dependent basis rotations, even for circuits with a high proportion of entangling operations
## Quantum advantage claim
**Classification:** not-applicable

The paper does not claim or demonstrate quantum advantage. It focuses on classical simulation techniques for quantum dynamics using quantum Monte Carlo methods, with no direct comparison to quantum hardware or claims of superiority over classical methods.
## Limitations
- The method relies on the Feynman-Kitaev Clock construction, which assumes a discrete-time evolution of quantum systems; continuous-time dynamics may not be accurately captured [inferred]
- The severity of the dynamical sign problem increases with system size and simulation duration, limiting scalability to larger quantum systems
- The number of walkers required to mitigate the sign problem (nc) may grow exponentially with system size, making simulations computationally intractable for large systems
- The method's performance is highly dependent on the choice of basis rotations to mitigate the sign problem, which may not always be straightforward or efficient to determine
- Numerical examples are limited to quantum circuits with local rotations and controlled NOT gates; performance on more complex or highly entangled circuits remains untested [inferred]
- The parallel-in-time scaling demonstration is limited to a basic MPI implementation on a commodity cluster; performance on large-scale HPC systems is not validated [inferred]
- The method assumes the ability to efficiently evaluate matrix elements of the system operators, which may not hold for all physical systems [inferred]
- The theoretical analysis of the sign problem is primarily focused on stoquastic or quasi-classical Hamiltonians, leaving gaps in understanding for more general cases [inferred]
## Open questions
- What are the precise conditions under which the dynamical sign problem can be efficiently mitigated for arbitrary quantum circuits?
- How does the critical number of walkers (nc) scale with system size and simulation time for non-stoquastic and non-quasi-classical Hamiltonians?
- Can more sophisticated basis rotation schemes be developed to further reduce the sign problem in complex quantum circuits?
- What is the impact of noise and decoherence on the performance of this method when applied to real quantum hardware?
- How does the method compare to other quantum Monte Carlo techniques for real-time dynamics in terms of accuracy and computational efficiency?
- What are the limitations of the parallel-in-time approach for systems with long-range interactions or non-local operations?
- Can the method be extended to open quantum systems, and if so, what are the associated computational costs?

**Future work:**
- Explore more advanced basis rotation schemes to mitigate the sign problem in complex quantum circuits
- Investigate the scalability of the method on large-scale HPC systems and optimize parallel-in-time implementations
- Apply the method to a broader range of quantum circuits, including those with high entanglement and non-local operations
- Extend the method to open quantum systems and study its performance in the presence of noise and decoherence
- Compare the method with other quantum Monte Carlo techniques for real-time dynamics to identify strengths and weaknesses
- Develop hybrid methods that combine this approach with other simulation techniques to improve efficiency and accuracy
- Study the theoretical and practical implications of the sign problem for larger system sizes and longer simulation times
## Key ideas
- #idea:near-term-feasibility — Clock Quantum Monte Carlo (CQMC) method combines Feynman-Kitaev Clock with FCIQMC to simulate real-time quantum dynamics, addressing the dynamical sign problem via time-dependent basis rotations
- #idea:hybrid-approach — Classical Monte Carlo techniques (FCIQMC) are adapted to simulate quantum dynamics, enabling parallel-in-time scaling for efficient computation on classical hardware
- #limitation:qubit-count — Scalability is limited by exponential growth in walkers (Nw) required for sign-coherent sampling in larger systems
- #limitation:noise — The method's reliance on Monte Carlo introduces statistical errors, and noise resilience on real quantum hardware remains untested
- #limitation:data-encoding — The Feynman-Kitaev Clock construction may not efficiently map all quantum dynamics problems, particularly for complex circuits
## Contradictions
<!-- Step 6 output — where this paper contradicts others -->

## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
