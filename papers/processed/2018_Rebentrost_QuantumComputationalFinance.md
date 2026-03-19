---
aliases:
- 'Quantum computational ﬁnance: Monte Carlo pricing of ﬁnancial derivatives'
- Quantum computational nance Monte
authors:
- Patrick Rebentrost
- Brajesh Gupt
- Thomas R. Bromley
auto_detected: true
classification: ''
contradiction_flags: []
doi: 10.48550/arXiv.1805.00109
evidence_type: ''
idea_tags:
- idea:quantum-advantage
- idea:near-term-feasibility
journal_or_venue: arXiv
methodology_tags:
- amplitude-estimation
- grover
- quantum-simulation
- classical-simulation
paper_type: ''
quantum_advantage_claim: speculative
related_papers: []
relevance_phase1: high
relevance_phase3: high
source_type: preprint
source_type_confidence: high
step1_date: '2026-03-18T22:44:57.487757'
step1_model: Mistral-Large-3
step2_date: '2026-03-18T22:44:59.027665'
step2_model: Mistral-Large-3
step3_date: '2026-03-18T22:45:05.752506'
step3_model: Mistral-Large-3
step4_date: '2026-03-18T22:46:01.598398'
step4_model: Mistral-Large-3
step5_date: '2026-03-18T22:46:10.608614'
step5_model: Mistral-Large-3
step6_date: '2026-03-18T22:46:15.312341'
step6_model: Mistral-Large-3
steps_completed:
- 1
- 2
- 3
- 4
- 5
- 6
tags:
- topic/derivatives-pricing
- topic/risk-modelling
- method/amplitude-estimation
- method/grover
- method/quantum-simulation
- method/classical-simulation
- idea/quantum-advantage
- idea/near-term-feasibility
title: 'Quantum computational ﬁnance: Monte Carlo pricing of ﬁnancial derivatives'
topic_tags:
- derivatives-pricing
- risk-modelling
year: 2018
zotero_key: ''
---

## Abstract summary
This paper introduces a quantum algorithm for pricing financial derivatives using Monte Carlo methods, leveraging quantum superposition and amplitude estimation to achieve a quadratic speedup over classical approaches. The authors demonstrate how to encode probability distributions, payoff functions, and expectation values into quantum circuits, focusing on European and Asian call options as case studies. The work aims to establish a foundation for further exploration of quantum computing applications in financial modeling and risk management.
## Methodology
The paper presents a theoretical and algorithmic framework for quantum Monte Carlo pricing of financial derivatives, specifically European and Asian call options. The methodology involves encoding the probability distributions of financial asset prices into quantum superpositions, implementing payoff functions via quantum circuits, and extracting derivative prices through quantum measurements. The core quantum technique employed is amplitude estimation, which provides a quadratic speedup in the number of steps required to estimate the price with high confidence compared to classical Monte Carlo methods. The authors detail the preparation of log-normal distributions for asset prices, the discretization of Brownian motion, and the quantum circuit implementation of payoff functions. The quantum algorithm for Monte Carlo pricing is formalized using phase estimation and amplitude amplification, with theoretical proofs supporting the quadratic speedup. Numerical evidence from classical simulations is provided to validate the claimed speedup.

**Algorithms used:** Amplitude Estimation, Quantum Monte Carlo, Phase Estimation, Grover's Search

**Experimental setup:** The paper does not report experiments on actual quantum hardware. Instead, it relies on classical numerical simulations to validate the theoretical claims of quadratic speedup. The quantum circuits are described theoretically, including the preparation of quantum states representing discretized probability distributions (e.g., normal distribution for Brownian motion) and the implementation of payoff functions using reversible classical circuits adapted for quantum computation. The analysis assumes an ideal quantum computer with error-free operations.

**Dataset:** The paper uses synthetic financial data based on the Black-Scholes-Merton (BSM) model, including parameters such as initial stock price (S0), drift (α), volatility (σ), risk-free rate (r), strike price (K), and maturity date (T). The stochastic process for asset prices is modeled as geometric Brownian motion, with probability distributions derived analytically from the BSM framework. No real-world financial datasets are employed.
## Findings
- [speculative] The paper presents a quantum algorithm for Monte Carlo pricing of financial derivatives, leveraging amplitude estimation to achieve a quadratic speedup in the number of steps required for high-confidence price estimation compared to classical Monte Carlo methods
- [speculative] The quantum algorithm prepares relevant probability distributions in quantum superposition, implements payoff functions via quantum circuits, and extracts derivative prices through quantum measurements
- [supported] The amplitude estimation algorithm is shown to provide a quadratic speedup in estimating expectation values, reducing the error dependency from O(1/ϵ²) in classical Monte Carlo to O(1/ϵ) in the quantum approach
- [speculative] The quadratic speedup is argued to hold for pricing European and Asian call options, with resource estimates provided for these fundamental derivative types
- [supported] Classical numerical calculations are used to provide evidence that the quadratic speedup in pricing can be attained, though results are from simulation rather than real hardware
- [speculative] The authors suggest that the framework could be extended to more complex financial models and payoff functions beyond the Black-Scholes-Merton model

**Results summary:** The preprint introduces a quantum algorithm for Monte Carlo pricing of financial derivatives, focusing on European and Asian call options. The core contribution is the application of amplitude estimation to achieve a theoretical quadratic speedup in the number of computational steps required for accurate price estimation compared to classical Monte Carlo methods. The paper demonstrates how to encode financial probability distributions and payoff functions into quantum states and circuits. While the quadratic speedup is supported by classical numerical simulations, the results are not validated on real quantum hardware, and the practical realization of quantum advantage remains speculative.

**Performance claims:**
- Quadratic speedup in the number of steps for price estimation (O(1/ϵ) vs. O(1/ϵ²) in classical methods)
- Error reduction from O(λ²/(kϵ²)) in classical Monte Carlo to O(λ/ϵ) in the quantum algorithm for bounded-variance random variables
## Quantum advantage claim
**Classification:** speculative

The paper claims a theoretical quadratic speedup in Monte Carlo pricing via amplitude estimation, supported by classical numerical simulations. However, the advantage is not demonstrated on real quantum hardware, and the scalability to practical problem sizes remains unproven.
## Limitations
- The paper is a preprint and has not undergone peer review, which may affect the validity and reliability of the results [inferred]
- The quantum algorithm is demonstrated using classical numerical calculations rather than real quantum hardware, limiting empirical validation [inferred]
- The analysis is restricted to European and Asian call options, which are fundamental but do not cover the full spectrum of financial derivatives [inferred]
- The discretization of the probability density and the binary approximation of the payoff function introduce errors (O(2^-n)), which may affect accuracy for practical applications
- The quantum resource requirements (e.g., qubit count, circuit depth) are not explicitly quantified, making it difficult to assess scalability to real-world problems [inferred]
- The paper assumes ideal quantum operations without accounting for hardware noise, decoherence, or gate errors, which are critical in near-term quantum devices [inferred]
- The amplitude estimation algorithm requires controlled operations (e.g., Q^j), which may be challenging to implement on current quantum hardware [inferred]
- The analysis does not compare the proposed quantum algorithm with state-of-the-art classical Monte Carlo methods in terms of runtime or resource efficiency [inferred]
- The paper focuses on a single underlying asset (stock) and does not address multi-asset or correlated asset pricing, which are common in financial markets [inferred]
- The assumptions of the Black-Scholes-Merton model (e.g., constant volatility, no transaction costs) are simplistic and may not hold in real markets [inferred]
## Open questions
- How does the quantum algorithm perform on real quantum hardware with noise and limited qubit counts?
- What is the impact of discretization and function approximation errors on the accuracy of derivative pricing for more complex payoff functions?
- Can the quadratic speedup be maintained when extending the algorithm to multi-asset or path-dependent derivatives (e.g., American options)?
- How does the quantum algorithm compare to classical Monte Carlo methods in terms of runtime, resource requirements, and accuracy for large-scale problems?
- What are the practical limitations of implementing controlled operations (e.g., Q^j) on near-term quantum devices?
- How does the algorithm handle non-Gaussian or fat-tailed distributions, which are more realistic for financial markets?
- What noise mitigation techniques can be applied to improve the robustness of the algorithm on noisy intermediate-scale quantum (NISQ) devices?
- How does the algorithm scale with the number of qubits and circuit depth for real-world financial applications?

**Future work:**
- Implement and test the algorithm on real quantum hardware (e.g., IBM, Rigetti, or Xanadu devices)
- Extend the algorithm to more complex financial derivatives, such as American options or multi-asset options
- Investigate the impact of noise and decoherence on the algorithm's performance and develop error mitigation strategies
- Compare the quantum algorithm with state-of-the-art classical Monte Carlo methods in terms of runtime and resource efficiency
- Explore the use of quantum machine learning or hybrid quantum-classical approaches to improve the algorithm's applicability to real-world financial data
- Develop methods to handle non-Gaussian or fat-tailed distributions in the quantum Monte Carlo framework
- Quantify the quantum resource requirements (e.g., qubit count, gate depth) for practical financial applications
- Investigate the algorithm's performance under more realistic market assumptions, such as stochastic volatility or transaction costs
## Key ideas
- #idea:quantum-advantage — Amplitude estimation achieves quadratic speedup (O(1/ϵ) vs. O(1/ϵ²)) for Monte Carlo pricing of European and Asian call options
- #idea:near-term-feasibility — Theoretical framework for quantum Monte Carlo pricing is proposed, though validated only via classical simulation
- #limitation:no-empirical-validation — Quadratic speedup is supported by numerical simulations but not tested on real quantum hardware
- #limitation:noise — Assumes ideal quantum operations, ignoring hardware noise and decoherence in NISQ devices
- #limitation:data-encoding — Discretization and binary approximation of payoff functions introduce errors (O(2^-n))
- #idea:hybrid-approach — Potential future work includes hybrid quantum-classical approaches for real-world financial data
## Contradictions
<!-- Step 6 output — where this paper contradicts others -->

## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
