---
aliases:
- Reduction of Qubits in Quantum Algorithm for Monte Carlo Simulation by Pseudo-random
  Number Generator
- Reduction Qubits Quantum Algorithm
authors:
- Koichi Miyamoto
- Kenji Shiohara
auto_detected: true
classification: ''
contradiction_flags: []
doi: 10.48550/arXiv.1911.12469
evidence_type: ''
idea_tags:
- idea:quantum-advantage
- idea:near-term-feasibility
- idea:hybrid-approach
journal_or_venue: arXiv
methodology_tags:
- amplitude-estimation
- quantum-simulation
- classical-simulation
paper_type: ''
quantum_advantage_claim: theoretical
related_papers: []
relevance_phase1: high
relevance_phase3: high
source_type: preprint
source_type_confidence: high
step1_date: '2026-03-19T11:55:09.554693'
step1_model: Mistral-Large-3
step2_date: '2026-03-19T11:55:16.287726'
step2_model: Mistral-Large-3
step3_date: '2026-03-19T11:55:40.248284'
step3_model: Mistral-Large-3
step4_date: '2026-03-19T11:56:07.554971'
step4_model: Mistral-Large-3
step5_date: '2026-03-19T11:56:32.464274'
step5_model: Mistral-Large-3
step6_date: '2026-03-19T11:57:17.578096'
step6_model: Mistral-Large-3
steps_completed:
- 1
- 2
- 3
- 4
- 5
- 6
tags:
- topic/risk-modelling
- topic/derivatives-pricing
- method/amplitude-estimation
- method/quantum-simulation
- method/classical-simulation
- idea/quantum-advantage
- idea/near-term-feasibility
- idea/hybrid-approach
title: Reduction of Qubits in Quantum Algorithm for Monte Carlo Simulation by Pseudo-random
  Number Generator
topic_tags:
- risk-modelling
- derivatives-pricing
year: 2020
zotero_key: ''
---

## Abstract summary
This preprint proposes a method to reduce the number of qubits required in quantum algorithms for Monte Carlo simulations, particularly in high-dimensional financial problems like credit risk measurement. The authors introduce a pseudo-random number generator (PRNG) implemented on a quantum circuit to sequentially generate random numbers, thereby avoiding the need for a quantum register per random number. The paper outlines the theoretical framework, provides concrete implementations of PRNGs, and demonstrates applications in credit risk measurement and simple multi-variable integration.
## Methodology
The paper proposes a method to reduce the number of qubits required for quantum Monte Carlo simulations in financial applications, particularly focusing on high-dimensional problems like credit risk measurement. The authors introduce a technique that uses a pseudo-random number generator (PRNG) implemented on a quantum circuit to sequentially generate random numbers, rather than allocating a separate quantum register for each random number. This approach mimics classical Monte Carlo methods where pseudo-random numbers are generated sequentially. The paper details the implementation of a permuted congruential generator (PCG) as the PRNG, which combines linear congruential methods with bit string permutations. The methodology involves creating superpositions of pseudo-random number sequences, sequentially computing the integrand values using these sequences, and estimating the average of these values through quantum amplitude estimation. The trade-off between qubit reduction and increased circuit depth is discussed, highlighting the practical implications for large-scale quantum Monte Carlo simulations.

**Algorithms used:** Quantum Amplitude Estimation, Permuted Congruential Generator (PCG), Linear Congruential Generator (LCG)

**Experimental setup:** The experimental setup involves simulations conducted using IBM's Qiskit quantum circuit simulator. The PRNG used is a linear congruential generator (LCG) with specific parameters (a=11, c=0, m=31) and a seed value of 1, producing 5-bit pseudo-random numbers. The demonstration focuses on a simple two-variable trigonometric function integration to validate the proposed method. The quantum circuit sequentially generates pseudo-random numbers, computes the integrand values, and estimates the integral average using amplitude estimation techniques.

**Dataset:** For the demonstration, a simple multi-variable trigonometric function (sin² of a sum of variables) is integrated over a defined range (θ = π/6). The method is also conceptually applied to credit risk measurement using the Merton model, which involves simulating default patterns of obligors based on normally distributed random variables, though no specific real-world dataset is used in the simulations.
## Findings
- [supported] The proposed method reduces the required number of qubits for quantum Monte Carlo simulations by using a pseudo-random number generator (PRNG) implemented on a quantum circuit, enabling sequential generation of random numbers instead of parallel allocation of quantum registers per random number.
- [supported] The quantum algorithm for Monte Carlo using PRNG achieves a quadratic speedup compared to classical Monte Carlo, with estimation error proportional to O(N^{-1}) versus O(N^{-1/2}) in classical methods.
- [supported] The trade-off for qubit reduction is increased circuit depth, which may limit practical implementation on near-term quantum hardware without error correction.
- [supported] The paper demonstrates a concrete implementation of a permuted congruential generator (PCG) as a PRNG on a quantum circuit, including modular arithmetic operations and bit permutation techniques like random rotation and xorshift.
- [supported] Application of the proposed method to credit risk measurement in the Merton model shows feasibility, though the circuit remains too large for current simulators or hardware.
- [supported] A proof-of-concept demonstration on a quantum circuit simulator for a simple multi-variable integration problem yields results close to the expected value, validating the approach.
- [speculative] Full qubit reduction may be impractical due to the increased circuit depth, but partial reduction (e.g., generating subsets of random numbers in parallel) could be a viable compromise for large-scale problems.
- [speculative] The method could be important for memory management in future large-scale quantum Monte Carlo simulations, even on quantum computers with large qubit counts.

**Results summary:** The paper introduces a method to reduce the qubit requirements for quantum Monte Carlo simulations by implementing a pseudo-random number generator (PRNG) on a quantum circuit. This approach enables sequential generation of random numbers, significantly lowering qubit usage compared to prior methods that allocate a quantum register per random number. The authors demonstrate that this method retains the quadratic speedup characteristic of quantum Monte Carlo while introducing a trade-off in increased circuit depth. Concrete implementations of PRNGs, such as the permuted congruential generator (PCG), are provided, along with applications to credit risk measurement and a simple integration problem. Simulation results validate the approach, though practical deployment on current hardware remains challenging due to circuit depth constraints.

**Performance claims:**
- Quadratic speedup in estimation error (O(N^{-1})) compared to classical Monte Carlo (O(N^{-1/2}))
- Reduction of qubit requirements from O(N_ran) to O(n_PRN), where n_PRN is the bit-length of the PRNG output
- Demonstrated integration result of 0.078391 on a quantum simulator, close to the exact average of 0.078394 for a simple multi-variable function
## Quantum advantage claim
**Classification:** theoretical

The paper claims a theoretical quantum advantage in the form of quadratic speedup for Monte Carlo simulations. However, this advantage is demonstrated only through simulations and theoretical analysis, not on real quantum hardware. The advantage is contingent on managing the trade-off between qubit reduction and increased circuit depth, which may limit practical implementation.
## Limitations
- Qubit reduction is a trade-off against increased circuit depth, which may make full reduction impractical on near-term quantum hardware due to error accumulation [inferred]
- The proposed method estimates the average of sampled integrand values (Esamp) rather than the exact expectation value (Etrue), introducing statistical error (ΔTrSm) similar to classical Monte Carlo
- The method assumes the integrand can be computed sequentially in steps, which is not universally applicable to all functions [inferred]
- Implementation relies on pseudo-random number generators (PRNGs) like PCG, whose statistical properties may not match true randomness, potentially affecting result quality [inferred]
- The paper demonstrates the method only on a small-scale problem (2-variable integral) using a simulator, lacking validation on real quantum hardware or larger-scale financial problems
- The period of the PRNG (e.g., 2^64 for PCG) may limit the number of samples (Nsamp) and random numbers (Nran) that can be generated without repetition [inferred]
- Concrete implementation details for converting uniform PRNs to desired distributions (e.g., normal) are assumed but not fully explored, which may introduce additional errors [inferred]
- Lack of peer review as this is a preprint, which may affect the robustness of claims and proposed methods [inferred]
- The analysis of computational load (Norac) assumes oracle calls dominate runtime, but does not account for overhead from PRNG implementation or error correction [inferred]
- The credit risk measurement example assumes a simplified Merton model and does not address practical complexities like varying exposure sizes or default correlations [inferred]
## Open questions
- How does the trade-off between qubit reduction and circuit depth impact practical performance on error-prone quantum hardware?
- What is the impact of PRNG statistical flaws on the accuracy of financial risk measures like VaR and CVaR?
- Can the method be extended to integrands that cannot be computed sequentially, and what are the implications for qubit count?
- How does the method perform when the number of samples (Nsamp) approaches the PRNG period, and what are the statistical consequences?
- What are the optimal PRNG parameters (e.g., PCG settings) for financial applications, and how do they affect speed and accuracy?
- How does the method compare to hybrid quantum-classical approaches for Monte Carlo simulation in terms of speed and resource requirements?
- What noise mitigation techniques are most effective for the deeper circuits resulting from qubit reduction?
- How does the method scale to problems requiring O(10^6) random numbers, such as large credit portfolios?

**Future work:**
- Test the proposed method on real quantum hardware to validate its performance and error resilience
- Extend the method to multi-period financial problems, such as dynamic portfolio optimization or path-dependent derivative pricing
- Develop and benchmark quantum circuits for converting uniform PRNs to non-uniform distributions (e.g., normal, log-normal) relevant to finance
- Explore hybrid quantum-classical approaches to balance qubit reduction with circuit depth constraints
- Investigate the use of alternative PRNGs or quantum random number generators to improve statistical properties
- Apply the method to larger-scale financial problems (e.g., credit portfolios with O(10^6) obligors) and compare results with classical Monte Carlo
- Study the impact of error correction and fault-tolerant gates on the method's practicality for deep circuits
- Develop adaptive strategies for adjusting the trade-off between qubit count and circuit depth based on problem size and hardware constraints
## Key ideas
- #idea:quantum-advantage — Proposes a quantum Monte Carlo method with quadratic speedup (O(N⁻¹) error scaling) compared to classical Monte Carlo (O(N⁻¹/²)), demonstrated via simulation for credit risk measurement and multi-variable integration.
- #idea:near-term-feasibility — Introduces a pseudo-random number generator (PRNG) on quantum circuits to reduce qubit requirements (O(n_PRN) vs. O(N_ran)), making large-scale simulations (e.g., O(10⁶) obligors) theoretically feasible on near-term devices.
- #idea:hybrid-approach — Suggests trade-offs between qubit reduction and circuit depth could be optimized via hybrid quantum-classical approaches, though not explicitly implemented.
- #limitation:qubit-count — Despite qubit reduction, the method's practicality is constrained by increased circuit depth and noise susceptibility on NISQ devices.
- #limitation:no-empirical-validation — All results are simulation-based; no real quantum hardware validation is provided, limiting claims of quantum advantage.
- #limitation:noise — Increased circuit depth due to qubit reduction may exacerbate noise-related errors on near-term quantum hardware.
- #limitation:data-encoding — Assumes seamless conversion of uniform PRNs to desired distributions (e.g., normal), but this may introduce additional errors or overhead.
## Contradictions
<!-- Step 6 output — where this paper contradicts others -->

## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
