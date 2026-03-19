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
step1_date: '2026-03-19T11:39:26.103824'
step1_model: Mistral-Large-3
step2_date: '2026-03-19T11:39:34.113882'
step2_model: Mistral-Large-3
step3_date: '2026-03-19T11:39:49.805764'
step3_model: Mistral-Large-3
step4_date: '2026-03-19T11:41:25.539013'
step4_model: Mistral-Large-3
step5_date: '2026-03-19T11:41:44.436962'
step5_model: Mistral-Large-3
step6_date: '2026-03-19T11:41:52.864868'
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
This paper introduces a novel method combining the Feynman-Kitaev Clock construction with Full Configuration Interaction Quantum Monte Carlo (FCIQMC) to simulate real-time quantum dynamics. The approach reformulates unitary quantum evolution as a ground-state eigenvalue problem, enabling the use of Monte Carlo techniques to mitigate the curse of dimensionality. The authors demonstrate the method's applicability to quantum circuits and propose techniques to reduce the dynamical sign problem through time-dependent basis rotations, while also highlighting its potential for parallel-in-time simulations.
## Methodology
The paper presents a theoretical framework combining the Feynman-Kitaev Clock construction with the Full Configuration Interaction Quantum Monte Carlo (FCIQMC) method to address quantum dynamics problems. The Feynman-Kitaev Clock maps unitary quantum dynamics to a ground state eigenvalue problem of a Hermitian Hamiltonian, termed the Clock Hamiltonian. The FCIQMC method, originally designed for ground state electronic systems, is adapted to simulate the time evolution of quantum systems by treating the Clock Hamiltonian. The methodology involves deriving the Clock Hamiltonian from a time-embedded discrete variational principle, applying the FCIQMC algorithm to this Hamiltonian, and addressing the dynamical sign problem through stochastic sampling of walkers. The paper also introduces a technique to mitigate the sign problem using time-dependent basis rotations and explores the parallel-in-time scaling of the method for efficient computation on parallel architectures.

**Algorithms used:** Quantum Monte Carlo, Full Configuration Interaction Quantum Monte Carlo (FCIQMC)

**Experimental setup:** Numerical examples are provided using quantum circuits to demonstrate the methodology. The experimental setup involves simulating quantum dynamics on classical computers using the FCIQMC method adapted for the Clock Hamiltonian. The simulations include testing the impact of local rotations and controlled NOT (CNOT) gates on the sign problem and evaluating the parallel efficiency of the method on a Linux cluster with AMD Opteron 6376 processors.
## Findings
- [supported] The Feynman-Kitaev Clock construction maps general unitary quantum dynamics to a Hermitian ground state eigenvalue problem, enabling the use of quantum Monte Carlo methods for real-time quantum dynamics.
- [supported] The Full Configuration Interaction Quantum Monte Carlo (FCIQMC) method is adapted to the Clock Hamiltonian, providing a new technique for studying quantum dynamics problems with numerical examples from quantum circuits.
- [supported] The dynamical sign problem in quantum Monte Carlo simulations is mitigated through time-dependent basis rotations, reducing the number of walkers required for sign-coherent sampling.
- [supported] The Clock Quantum Monte Carlo method exhibits a sharp transition between sign-incoherent and sign-coherent sampling regimes, dependent on the number of walkers and the nature of the quantum circuit (e.g., rotation angles, entangling gates).
- [speculative] The method may allow efficient parallel-in-time simulation of quantum dynamics by leveraging the locality of time and the parallelism of Monte Carlo techniques, achieving high parallel efficiencies on commodity clusters.
- [speculative] The severity of the sign problem depends on the deviation of the quantum circuit from quasi-classical operations, with local rotations closer to quasi-classical requiring fewer walkers for coherent sampling.
- [speculative] The use of basis rotations (analogous to the interaction picture) can mitigate the sign problem even for circuits with entangling operations, though exact solutions may be as difficult as solving the quantum evolution itself.
- [supported] The Clock Hamiltonian is proven to be frustration-free, with a unique ground state separated from the first excited state by a gap of O(1/T²), where T is the number of discrete time steps.

**Results summary:** The paper introduces a novel method, Clock Quantum Monte Carlo, which combines the Feynman-Kitaev Clock construction with the FCIQMC algorithm to simulate real-time quantum dynamics as a ground state eigenvalue problem. The authors demonstrate the method's applicability to quantum circuits and show that it can mitigate the dynamical sign problem through time-dependent basis rotations. Numerical examples illustrate the transition to sign-coherent sampling and the impact of circuit structure on the severity of the sign problem. The method also enables efficient parallel-in-time simulations, achieving high parallel efficiencies. While the approach shows promise for quantum dynamics simulations, the sign problem remains a challenge for non-stoquastic or non-quasi-classical circuits.

**Performance claims:**
- Parallel efficiencies of over 95% with 2 processors and 70% with 8 processors for fixed problem sizes using MPI implementation on a commodity cluster.
- Reduction in the number of walkers required for sign-coherent sampling when using local basis rotations, even for circuits with a high proportion of entangling operations (e.g., 8 controlled NOT gates).
- Sharp transition to sign-coherent sampling observed at a critical number of walkers (nc), which varies with rotation angles and circuit complexity.
## Quantum advantage claim
**Classification:** not-applicable

The paper does not claim or demonstrate quantum advantage in the context of quantum computing hardware. Instead, it focuses on classical simulation techniques for quantum dynamics using quantum Monte Carlo methods and their computational efficiency.
## Limitations
- The method relies on the Feynman-Kitaev Clock construction, which maps quantum dynamics to a ground state eigenvalue problem, but this mapping may not be efficient for all types of quantum systems [inferred]
- The dynamical sign problem remains a fundamental challenge, particularly for non-stoquastic Hamiltonians, and can severely limit the scalability of the method
- The number of walkers required to mitigate the sign problem (nc) can grow exponentially with system size and simulation time, making large-scale simulations computationally intractable
- The method assumes discrete time steps, which may not capture continuous-time dynamics accurately without sufficient refinement [inferred]
- Numerical examples are limited to quantum circuits and simple local rotations, lacking validation on more complex or physically realistic quantum systems
- The basis rotation technique for mitigating the sign problem requires preliminary computation, and finding optimal rotations may be as difficult as solving the original dynamics problem
- The parallel-in-time scaling demonstration is limited to a basic MPI implementation on a commodity cluster, and performance may degrade for more complex or larger systems [inferred]
- The method has not been empirically validated on real quantum hardware, limiting insights into practical performance under noise and decoherence [inferred]
- The theoretical analysis assumes ideal conditions (e.g., frustration-free Hamiltonians), which may not hold for many practical quantum systems [inferred]
## Open questions
- How does the severity of the dynamical sign problem scale with the complexity of the quantum circuit or physical system being simulated?
- What are the most effective strategies for selecting basis rotations to mitigate the sign problem in non-trivial quantum circuits?
- Can the method be extended to efficiently simulate open quantum systems or systems with non-unitary dynamics?
- What is the impact of noise and decoherence on the performance of this method when implemented on near-term quantum hardware?
- How does the critical number of walkers (nc) required for sign-coherent sampling vary across different types of quantum systems?
- Are there specific classes of quantum dynamics problems where this method outperforms classical Monte Carlo or other quantum simulation techniques?
- What are the trade-offs between the accuracy of the basis rotation scheme and the computational cost of finding optimal rotations?
- How does the parallel-in-time scaling perform for systems with long-range interactions or highly entangled states?

**Future work:**
- Extend the method to simulate more complex quantum circuits, including those with higher degrees of entanglement and non-local interactions
- Develop more efficient algorithms for finding basis rotations that mitigate the sign problem without requiring exact knowledge of the quantum evolution
- Apply the method to physically realistic quantum systems, such as molecular dynamics or condensed matter systems, to validate its practical utility
- Explore hybrid quantum-classical approaches that combine this method with near-term quantum hardware to overcome current limitations
- Investigate the use of machine learning techniques to optimize basis rotations and reduce the computational cost of mitigating the sign problem
- Benchmark the method against other quantum simulation techniques, such as tensor networks or variational quantum algorithms, to identify its relative strengths and weaknesses
- Study the impact of noise and error mitigation techniques on the performance of this method when implemented on real quantum devices
- Generalize the method to handle open quantum systems and non-unitary dynamics, broadening its applicability to a wider range of problems
## Key ideas
- #idea:near-term-feasibility — Clock Quantum Monte Carlo (CQMC) method combines Feynman-Kitaev Clock with FCIQMC to simulate real-time quantum dynamics, addressing the dynamical sign problem via time-dependent basis rotations
- #idea:hybrid-approach — Classical Monte Carlo techniques (FCIQMC) are adapted to simulate quantum dynamics, enabling parallel-in-time scaling for efficient computation on classical hardware
- #limitation:noise — The method's reliance on Monte Carlo introduces statistical errors, and noise resilience on real quantum hardware remains untested
- #limitation:qubit-count — Scalability is limited by exponential growth in walkers (Nw) required for sign-coherent sampling in larger systems
- #limitation:data-encoding — The Feynman-Kitaev Clock construction may not efficiently map all quantum dynamics problems, particularly for complex circuits
## Contradictions
<!-- Step 6 output — where this paper contradicts others -->

## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
