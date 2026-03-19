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
quantum_advantage_claim: speculative
related_papers: []
relevance_phase1: medium
relevance_phase3: not-yet-assessed
source_type: preprint
source_type_confidence: high
step1_date: '2026-03-18T23:02:29.691024'
step1_model: Mistral-Large-3
step2_date: '2026-03-18T23:02:32.878339'
step2_model: Mistral-Large-3
step3_date: '2026-03-18T23:02:37.967349'
step3_model: Mistral-Large-3
step4_date: '2026-03-18T23:02:47.165698'
step4_model: Mistral-Large-3
step5_date: '2026-03-18T23:02:54.658885'
step5_model: Mistral-Large-3
step6_date: '2026-03-18T23:02:57.014920'
step6_model: Mistral-Large-3
steps_completed:
- 1
- 2
- 3
- 4
- 5
- 6
tags:
- topic/market-simulation
- topic/derivatives-pricing
- method/quantum-simulation
- method/classical-simulation
- idea/near-term-feasibility
- idea/hybrid-approach
title: 'Clock Quantum Monte Carlo: an imaginary-time method for real-time quantum
  dynamics'
topic_tags:
- market-simulation
- derivatives-pricing
year: 2014
zotero_key: ''
---

## Abstract summary
This paper introduces a novel method combining the Feynman-Kitaev Clock formalism with Full Configuration Interaction Quantum Monte Carlo (FCIQMC) to simulate real-time quantum dynamics. The approach reformulates quantum dynamics as a ground state eigenvalue problem, enabling the use of Monte Carlo techniques to mitigate the challenges of the dynamical sign problem. The authors demonstrate the method's applicability through numerical examples and propose techniques to improve its efficiency, including parallel-in-time simulation and time-dependent basis rotations.
## Methodology
The paper introduces a novel quantum Monte Carlo method termed 'Clock Quantum Monte Carlo' (CQMC) that combines the Feynman-Kitaev Clock construction with the Full Configuration Interaction Quantum Monte Carlo (FCIQMC) technique. The methodology involves mapping general unitary quantum dynamics to a Hermitian ground state eigenvalue problem using the Clock Hamiltonian. The FCIQMC algorithm is adapted to simulate the ground state of this Hamiltonian, enabling the study of real-time quantum dynamics through imaginary-time propagation. The approach addresses the dynamical sign problem inherent in quantum Monte Carlo methods by leveraging time-dependent basis rotations to mitigate sign incoherence. Numerical examples are provided using quantum circuits to demonstrate the efficacy of the method, including its parallel-in-time scaling capabilities for efficient computation on modern architectures.

**Algorithms used:** FCIQMC (Full Configuration Interaction Quantum Monte Carlo), Feynman-Kitaev Clock

**Experimental setup:** Numerical simulations were conducted using quantum circuits to test the Clock Quantum Monte Carlo method. The experiments involved local rotations and controlled-NOT (CNOT) gates applied to qubits initialized in the |0⟩ state. Simulations were performed on classical computational environments, with walkers represented as discrete system-time configurations. The method's performance was evaluated under varying numbers of walkers and rotation angles to assess sign coherence and convergence properties. Parallel-in-time scaling was demonstrated using domain decomposition in time for efficient communication between processes.
## Findings
- [supported] The Feynman-Kitaev Clock construction maps general unitary quantum dynamics to a Hermitian ground state eigenvalue problem, enabling the use of quantum Monte Carlo methods for real-time quantum simulations.
- [supported] The Clock Quantum Monte Carlo (Clock QMC) method combines the Feynman-Kitaev Clock with Full Configuration Interaction Quantum Monte Carlo (FCIQMC) to simulate quantum dynamics, with numerical examples provided for quantum circuits.
- [supported] The dynamical sign problem in quantum Monte Carlo simulations can be mitigated through time-dependent basis rotations, reducing the number of walkers required for sign-coherent sampling in non-stoquastic Hamiltonians.
- [supported] Numerical results show a sharp transition from sign-incoherent to sign-coherent sampling as the number of walkers increases, with the critical threshold (nc) depending on the system size and rotation angle.
- [supported] Parallel-in-time scaling is achieved by leveraging time-locality in the Clock Hamiltonian, enabling efficient domain decomposition and nearest-neighbor communication in parallel implementations.
- [speculative] The authors suggest that the Clock QMC method could be extended to more complex quantum circuits, though further testing is needed to determine the efficiency of basis rotation schemes for entangling operations.
- [speculative] The sign problem mitigation technique may reduce computational costs even for simulations with a high proportion of two-qubit entangling operations, as demonstrated in a controlled-NOT gate example.

**Results summary:** The paper introduces Clock Quantum Monte Carlo, a method that reformulates real-time quantum dynamics as a ground state eigenvalue problem using the Feynman-Kitaev Clock construction. This approach integrates FCIQMC to simulate quantum circuits, addressing the dynamical sign problem through time-dependent basis rotations. Numerical examples demonstrate the method's ability to achieve sign-coherent sampling and highlight a critical walker threshold (nc) for accurate simulations. The method also enables efficient parallel-in-time scaling, leveraging time-locality for domain decomposition. While the results are promising for certain quantum circuits, the authors note that further validation is needed for more complex systems.

**Performance claims:**
- Sharp transition to sign-coherent sampling observed at a critical number of walkers (nc) for 11-qubit systems with local rotations.
- Time-dependent basis rotations reduce the number of walkers required for sign-coherent sampling by orders of magnitude in circuits with controlled-NOT gates.
- Parallel-in-time scaling demonstrated with nearest-neighbor communication, enabling efficient domain decomposition for large-scale simulations.
## Quantum advantage claim
**Classification:** speculative

The paper does not demonstrate quantum advantage on real hardware. Claims of potential efficiency gains are based on simulations and theoretical arguments, particularly the mitigation of the sign problem and parallel-in-time scaling. The authors suggest that the method could enable classical simulations of quantum dynamics beyond current capabilities, but this remains unvalidated empirically.
## Limitations
- The method relies on the Feynman-Kitaev Clock construction, which may not be applicable or efficient for all types of quantum dynamics problems [inferred]
- The sign problem remains a fundamental challenge, particularly for real-time dynamics, and can severely limit the scalability of the method
- The number of walkers (Nw) required to mitigate the sign problem and achieve accurate results (nc) can grow exponentially with system size and simulation time, making large-scale simulations intractable
- The method's performance is highly dependent on the choice of basis rotations {Bt}, and finding optimal or near-optimal rotations may be as difficult as solving the original quantum dynamics problem
- Numerical examples are limited to quantum circuits with relatively small system sizes (e.g., 11 qubits), and scalability to larger systems is not demonstrated
- The paper does not provide empirical validation on real quantum hardware, limiting insights into practical performance and noise resilience [inferred]
- The proposed basis rotation scheme for mitigating the sign problem is only tested on simple circuits with local rotations and CNOT gates; its efficacy for more complex circuits is unclear [inferred]
- The method assumes discrete time steps, which may not capture continuous-time dynamics accurately without sufficient refinement [inferred]
- Lack of peer review, as this is a preprint, may affect the robustness and generalizability of the findings [inferred]
- The parallel-in-time scaling is demonstrated theoretically, but empirical validation of scaling performance on large-scale parallel architectures is missing [inferred]
- The method's reliance on Monte Carlo techniques introduces statistical errors, and the paper does not thoroughly explore trade-offs between simulation time, walker count, and precision [inferred]
## Open questions
- How does the critical number of walkers (nc) scale with system size and simulation time for more complex quantum circuits beyond simple local rotations?
- What are the most effective strategies for choosing basis rotations {Bt} to mitigate the sign problem in general quantum circuits?
- Can the method be extended or adapted to handle open quantum systems or noise in quantum hardware effectively?
- What is the impact of decoherence and other noise sources on the accuracy and stability of the Clock Quantum Monte Carlo method when implemented on real quantum devices?
- How does the method compare to other quantum dynamics simulation techniques (e.g., tensor networks, variational quantum simulators) in terms of accuracy, scalability, and computational cost?
- What are the limitations of the parallel-in-time scaling approach when applied to very large numbers of time steps or highly entangled quantum systems?
- Can the method be generalized to simulate quantum dynamics in continuous time without discretization artifacts?

**Future work:**
- Empirical validation of the method on real quantum hardware to assess noise resilience and practical performance
- Extension of the basis rotation scheme to more complex quantum circuits, including those with multi-qubit gates and entanglement
- Investigation of hybrid approaches combining Clock Quantum Monte Carlo with other simulation techniques (e.g., tensor networks) to improve scalability
- Development of automated or heuristic methods for selecting optimal basis rotations {Bt} to minimize the sign problem
- Exploration of the method's applicability to open quantum systems and noisy intermediate-scale quantum (NISQ) devices
- Benchmarking the method against state-of-the-art classical and quantum simulation techniques for quantum dynamics
- Empirical study of parallel-in-time scaling on large-scale parallel architectures to validate theoretical predictions
- Extension of the method to continuous-time dynamics and assessment of discretization errors
## Key ideas
- #idea:near-term-feasibility — Clock Quantum Monte Carlo (CQMC) method combines Feynman-Kitaev Clock with FCIQMC to simulate real-time quantum dynamics, addressing the dynamical sign problem via time-dependent basis rotations
- #idea:hybrid-approach — Classical Monte Carlo techniques (FCIQMC) are adapted to simulate quantum dynamics, enabling parallel-in-time scaling for efficient computation
- #limitation:noise — The method's reliance on Monte Carlo introduces statistical errors, and noise resilience on real quantum hardware remains untested
- #limitation:qubit-count — Scalability is limited by exponential growth in walkers (Nw) required for sign-coherent sampling in larger systems
- #limitation:data-encoding — The Feynman-Kitaev Clock construction may not efficiently map all quantum dynamics problems, particularly for complex circuits
## Contradictions
<!-- Step 6 output — where this paper contradicts others -->

## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
