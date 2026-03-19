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
quantum_advantage_claim: speculative
related_papers: []
relevance_phase1: high
relevance_phase3: high
source_type: preprint
source_type_confidence: high
step1_date: '2026-03-18T22:31:55.453917'
step1_model: Mistral-Large-3
step2_date: '2026-03-18T22:31:57.076713'
step2_model: Mistral-Large-3
step3_date: '2026-03-18T22:32:04.861406'
step3_model: Mistral-Large-3
step4_date: '2026-03-18T22:33:03.457160'
step4_model: Mistral-Large-3
step5_date: '2026-03-18T22:33:13.772185'
step5_model: Mistral-Large-3
step6_date: '2026-03-18T22:33:18.445007'
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
This preprint proposes a method to reduce the number of qubits required for quantum Monte Carlo simulations in high-dimensional financial problems, such as credit risk measurement. The authors introduce a pseudo-random number generator (PRNG) implemented on a quantum circuit to sequentially generate random numbers, mimicking classical Monte Carlo techniques while preserving quantum speedup. The paper outlines the theoretical framework, provides a concrete implementation of a PRNG, and demonstrates its application to credit risk measurement and a simple multi-variable integration problem.
## Methodology
The paper proposes a method to reduce the number of qubits required for quantum Monte Carlo simulations in financial applications, such as credit risk measurement, by using a pseudo-random number generator (PRNG) implemented on a quantum circuit. The approach mimics classical Monte Carlo methods, where pseudo-random numbers are generated sequentially rather than allocating a quantum register per random number. The proposed method uses a permuted congruential generator (PCG) as the PRNG, which combines linear congruential generation with bit-string permutation. The quantum algorithm involves preparing a superposition of states, sequentially generating pseudo-random numbers, computing the integrand step-by-step, and estimating the average of sampled integrand values using quantum amplitude estimation. The paper also presents concrete implementations of the PCG on quantum circuits and applies the method to credit risk measurement and a simple multi-variable function integration, demonstrating results via simulation.

**Algorithms used:** Quantum Amplitude Estimation, Permuted Congruential Generator (PCG), Linear Congruential Generator (LCG)

**Experimental setup:** The experiments were conducted using a quantum simulator. The paper describes the implementation of the PCG on a quantum circuit, including modular arithmetic operations (addition, multiplication, exponentiation) and bit-string permutations (random rotation and xorshift). The quantum circuits for the proposed method and previous methods are outlined, with a focus on reducing qubit usage while maintaining quantum speedup.

**Dataset:** The paper applies the proposed method to credit risk measurement of a portfolio and a simple multi-variable trigonometric function integration for demonstrative purposes. Specific datasets are not explicitly named, but the credit risk measurement example assumes a large portfolio with up to O(10^6) obligors, requiring a corresponding number of random numbers for Monte Carlo simulation.
## Findings
- [supported] The proposed method reduces the required qubit number for quantum Monte Carlo simulations by using a pseudo-random number generator (PRNG) implemented on a quantum circuit, avoiding the need for a quantum register per random number.
- [supported] The quantum algorithm for Monte Carlo using PRNG achieves quadratic speedup (O(N⁻¹) error scaling) compared to classical Monte Carlo (O(N⁻¹/²) error scaling), where N is the number of computational steps.
- [supported] The paper demonstrates concrete implementation of a permuted congruential generator (PCG) as a PRNG on a quantum circuit, including modular arithmetic and permutation operations.
- [supported] Numerical results from a simulator show the feasibility of the proposed method for a simple multi-variable function integration and credit risk measurement.
- [speculative] The trade-off between qubit reduction and increased circuit depth may limit full qubit reduction in practice, but could be useful for adjusting calculations based on machine specifications.
- [speculative] The proposed method could enable large-scale Monte Carlo simulations on quantum computers with fewer qubits than previously required (e.g., O(10⁶) qubits for credit risk measurement).
- [speculative] The quantum advantage of the proposed method is expected to emerge for sufficiently large sample sizes (e.g., nsamp ≥ 20) where the error scales better than classical methods.

**Results summary:** The paper introduces a quantum algorithm for Monte Carlo simulation that reduces qubit requirements by using a pseudo-random number generator (PRNG) instead of allocating a quantum register per random number. The method achieves quadratic speedup in error scaling (O(N⁻¹)) compared to classical Monte Carlo (O(N⁻¹/²)), while maintaining the same statistical accuracy as classical sampling. The authors implement a permuted congruential generator (PCG) on a quantum circuit and demonstrate its application to credit risk measurement and a simple multi-variable function integration. However, the qubit reduction comes at the cost of increased circuit depth, creating a trade-off that may require optimization based on hardware capabilities. Numerical simulations support the feasibility of the approach, though no real hardware results are presented.

**Performance claims:**
- Quadratic speedup in error scaling (O(N⁻¹) vs. O(N⁻¹/²) for classical methods)
- Qubit reduction from O(N_ran) to O(n_PRN), where n_PRN is the bit length of the PRNG state (independent of the number of random numbers N_ran)
- Error convergence to the same order of magnitude as classical methods with 3 orders of magnitude fewer oracle calls (e.g., N_orac = 10³ vs. 10⁶ for nsamp = 20)
## Quantum advantage claim
**Classification:** speculative

The claimed quantum advantage (quadratic speedup) is theoretically supported by error scaling analysis and demonstrated via simulations, but not validated on real quantum hardware. The advantage is contingent on the trade-off between qubit reduction and circuit depth, which may limit practical applicability. No empirical evidence of advantage over classical methods is provided.
## Limitations
- Proposed method reduces qubit count but increases circuit depth, creating a trade-off that may limit practical applicability on near-term quantum devices [inferred]
- Assumes integrand can be computed sequentially in steps, which is not universally applicable to all financial Monte Carlo problems [inferred]
- Relies on pseudo-random number generators (PRNGs) with uniform distribution, requiring additional conversion gates for non-uniform distributions (e.g., normal distribution via Box-Muller method)
- Error analysis shows that the method's advantage diminishes when the statistical error (∆TrSm) dominates over estimation error (∆Est), particularly for small nsamp values
- Implementation of PRNG gates (PPRN and JPRN) requires modular arithmetic operations (addition, multiplication, exponentiation) that may be resource-intensive on current quantum hardware [inferred]
- Permutation operations (e.g., random rotation, xorshift) add complexity to the quantum circuit, potentially increasing noise susceptibility [inferred]
- Lack of empirical validation on real quantum hardware; all results are based on simulations
- [inferred] No comparison with state-of-the-art classical Monte Carlo methods in terms of runtime or accuracy
- [inferred] Potential statistical concerns with PRNG subsequences in high-dimensional spaces, though authors argue this is mitigated by large period PRNGs
- Preprint status means the work has not undergone peer review, which may affect methodological rigor or result interpretation [inferred]
## Open questions
- How does the proposed method perform on real quantum hardware with noise and decoherence effects?
- What is the optimal trade-off between qubit reduction and circuit depth for specific financial applications (e.g., credit risk measurement)?
- Can the method be extended to integrands that do not satisfy the sequential computation assumption?
- How do different PRNG implementations (e.g., PCG vs. Mersenne Twister) affect the accuracy and efficiency of the quantum Monte Carlo simulation?
- What is the impact of PRNG period length on the statistical properties of the Monte Carlo estimates, particularly for large Nran?
- How does the error scaling behave for integrands with different statistical properties (e.g., high variance vs. low variance)?
- Can noise mitigation techniques be effectively integrated into the proposed method to improve performance on NISQ devices?

**Future work:**
- Empirical validation of the proposed method on real quantum hardware (e.g., IBM or Rigetti processors)
- Development of hybrid quantum-classical approaches to balance qubit reduction and circuit depth
- Extension of the method to multi-period financial models (e.g., dynamic portfolio optimization)
- Investigation of alternative PRNGs or quantum random number generators to improve statistical properties
- Benchmarking against classical Monte Carlo methods to quantify quantum advantage in practical scenarios
- Exploration of noise-resilient implementations of modular arithmetic gates for PRNGs
- Application to other high-dimensional financial problems beyond credit risk measurement (e.g., derivative pricing, market risk analysis)
## Key ideas
- #idea:quantum-advantage — Proposes a quantum Monte Carlo method with quadratic speedup (O(N⁻¹) error scaling) compared to classical Monte Carlo (O(N⁻¹/²)), demonstrated via simulation for credit risk measurement and multi-variable integration.
- #idea:near-term-feasibility — Introduces a pseudo-random number generator (PRNG) on quantum circuits to reduce qubit requirements (O(n_PRN) vs. O(N_ran)), making large-scale simulations (e.g., O(10⁶) obligors) theoretically feasible on near-term devices.
- #idea:hybrid-approach — Suggests trade-offs between qubit reduction and circuit depth could be optimized via hybrid quantum-classical approaches, though not explicitly implemented.
- #limitation:qubit-count — Despite qubit reduction, the method's practicality is constrained by increased circuit depth and noise susceptibility on NISQ devices.
- #limitation:no-empirical-validation — All results are simulation-based; no real quantum hardware validation is provided, limiting claims of quantum advantage.
## Contradictions
<!-- Step 6 output — where this paper contradicts others -->

## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
