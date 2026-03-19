---
aliases:
- Quantum Algorithm for Stochastic Optimal Stopping Problems with Applications in
  Finance
- Quantum Algorithm Stochastic Optimal
authors:
- João F. Doriguello
- Alessandro Luongo
- Jinge Bao
- Patrick Rebentrost
- Miklos Santha
auto_detected: true
classification: ''
contradiction_flags: []
doi: 10.4230/LIPIcs.TQC.2022.2
evidence_type: ''
idea_tags:
- idea:quantum-advantage
- idea:near-term-feasibility
- idea:hybrid-approach
journal_or_venue: 17th Conference on the Theory of Quantum Computation, Communication
  and Cryptography (TQC 2022)
methodology_tags:
- amplitude-estimation
- quantum-simulation
- quantum-ML
- classical-simulation
paper_type: ''
quantum_advantage_claim: theoretical
related_papers: []
relevance_phase1: high
relevance_phase3: high
source_type: conference-paper
source_type_confidence: high
step1_date: '2026-03-18T23:36:58.688543'
step1_model: Mistral-Large-3
step2_date: '2026-03-18T23:37:49.570330'
step2_model: Mistral-Large-3
step3_date: '2026-03-18T23:38:56.037621'
step3_model: Mistral-Large-3
step4_date: '2026-03-18T23:39:04.324596'
step4_model: Mistral-Large-3
step5_date: '2026-03-18T23:39:10.263388'
step5_model: Mistral-Large-3
step6_date: '2026-03-18T23:39:58.573331'
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
- method/quantum-simulation
- method/quantum-ML
- method/classical-simulation
- idea/quantum-advantage
- idea/near-term-feasibility
- idea/hybrid-approach
title: Quantum Algorithm for Stochastic Optimal Stopping Problems with Applications
  in Finance
topic_tags:
- derivatives-pricing
- risk-modelling
year: 2022
zotero_key: ''
---

## Abstract summary
This paper introduces a quantum version of the least squares Monte Carlo (LSM) algorithm for solving stochastic optimal stopping problems, a key challenge in financial applications like American option pricing. The authors propose a quantum LSM framework that leverages quantum access to stochastic processes, quantum circuits for computing stopping times, and quantum Monte Carlo techniques. The work explores the interplay between function approximation and quantum speedups, demonstrating a nearly quadratic runtime improvement over classical LSM under certain assumptions.
## Methodology
The paper proposes a quantum version of the least squares Monte Carlo (LSM) algorithm for solving stochastic optimal stopping problems, with a focus on applications in finance such as American option pricing. The methodology involves developing a quantum algorithm that leverages quantum access to stochastic processes, quantum circuits for computing optimal stopping times, and quantum techniques for Monte Carlo simulations. The quantum LSM algorithm approximates continuation values using quantum states and linear function approximations, and it employs quantum Monte Carlo methods to estimate expectations. The theoretical framework is built on dynamic programming principles for optimal stopping times, recast into a quantum computational model. The quantum algorithm assumes quantum sampling access to Markov chains and quantum access to functions for payoffs and approximation architectures. The paper also assumes a quantum arithmetic model for fixed-point precision computations and access to quantum controlled rotations for Monte Carlo estimations.

**Experimental setup:** The quantum algorithm is designed within the standard circuit model of quantum computation. The experimental setup assumes quantum sampling access to a Markov chain (Definition 9) and quantum access to functions for payoffs and approximation architectures (Definition 10). The computational model includes a fixed-point arithmetic representation for real numbers (Definition 7) and assumes access to quantum controlled rotations (Definition 11). The quantum Monte Carlo algorithm (Theorem 13) is used for estimating expectation values. The paper does not specify the use of a particular quantum hardware or simulator but assumes idealized conditions for quantum operations.

**Dataset:** The paper discusses applications in finance, particularly American option pricing under stochastic processes like Brownian motion and geometric Brownian motion. While specific datasets are not explicitly mentioned, the methodology assumes access to stochastic processes and payoff functions typical in financial modeling, such as those derived from historical or simulated market data.
## Findings
- [supported] The proposed quantum least squares Monte Carlo (LSM) algorithm achieves a nearly quadratic speedup in runtime compared to the classical LSM algorithm under mild assumptions, specifically for stochastic optimal stopping problems such as American option pricing.
- [supported] The quantum algorithm leverages quantum access to stochastic processes, quantum circuits for computing optimal stopping times, and quantum techniques for Monte Carlo to approximate continuation values in the dynamic programming framework.
- [speculative] The quantum advantage is claimed to emerge from the interplay of function approximation and quantum algorithms for Monte Carlo, particularly through amplitude estimation and its generalizations.
- [supported] The algorithm is analyzed for cases involving Brownian motion and geometric Brownian motion processes, which are common in financial applications.
- [speculative] The authors suggest that the quantum LSM algorithm could be applied to other optimal stopping problems, such as the secretary problem, election timing, solvency estimation, and multi-armed bandit problems, though empirical validation is not provided.
- [speculative] The paper posits that the quantum algorithm may address computational challenges in the insurance sector, such as estimating Value at Risk (VaR) and life insurance contracts, but these claims are not empirically demonstrated in this work.

**Results summary:** The paper introduces a quantum algorithm for stochastic optimal stopping problems, with a focus on financial applications like American option pricing. The authors demonstrate that their quantum least squares Monte Carlo (LSM) algorithm achieves a nearly quadratic speedup in runtime over the classical LSM algorithm, assuming quantum access to stochastic processes and quantum techniques for Monte Carlo. The algorithm is theoretically analyzed for Brownian motion and geometric Brownian motion processes, and its potential applications in other domains, such as insurance and decision-making problems, are discussed. However, the results are derived from theoretical analysis and simulations, with no empirical validation on real quantum hardware.

**Performance claims:**
- Nearly quadratic speedup in runtime compared to classical LSM under mild assumptions
- Applicability to American option pricing with Brownian motion and geometric Brownian motion processes
## Quantum advantage claim
**Classification:** theoretical

The quantum advantage is claimed based on theoretical analysis and simulations, with a nearly quadratic speedup in runtime. However, the results are not demonstrated on real quantum hardware, and the advantage is contingent on assumptions such as quantum access to stochastic processes and efficient quantum circuits for Monte Carlo.
## Limitations
- The proposed quantum LSM algorithm assumes quantum access to a stochastic process, which may not be feasible with current quantum hardware [inferred]
- The algorithm achieves a nearly quadratic speedup under mild assumptions, but these assumptions may not hold in real-world financial scenarios [inferred]
- The paper focuses on finite-dimensional linear approximation architectures, limiting the generality of the approach [inferred]
- The analysis does not account for noise and decoherence effects in near-term quantum devices, which could degrade performance [inferred]
- The quantum arithmetic model assumes sufficient qubits for fixed-point precision, which may not be available in practice [inferred]
- The Grover-Rudolph method for loading probability distributions is assumed, but its practical implementation remains challenging [inferred]
- The runtime analysis neglects the cost of arithmetic operations, which could be significant for complex financial functions [inferred]
- The algorithm is only analyzed for Brownian motion and geometric Brownian motion processes, not for more complex stochastic processes [inferred]
- The paper does not provide empirical validation on real quantum hardware, limiting insights into practical performance [inferred]
- Conference paper page limits may have constrained a more detailed discussion of implementation challenges [inferred]
## Open questions
- How does the quantum LSM algorithm perform under noisy intermediate-scale quantum (NISQ) conditions?
- What is the impact of decoherence and gate errors on the solution quality of the quantum algorithm?
- Can the quadratic speedup be maintained for higher-dimensional or more complex stochastic processes?
- How does the algorithm compare to state-of-the-art classical methods for American option pricing in terms of accuracy and runtime?
- What are the minimal qubit and gate requirements for practical applications of the quantum LSM algorithm?
- How can the quantum sampling access to Markov chains be efficiently implemented for real-world financial data?
- What is the trade-off between approximation accuracy and quantum resource requirements in the quantum LSM algorithm?

**Future work:**
- Empirical validation of the quantum LSM algorithm on real quantum hardware
- Extension of the algorithm to more complex stochastic processes beyond Brownian motion
- Development of noise mitigation techniques to improve performance on NISQ devices
- Comparison of the quantum LSM algorithm with classical methods on real-world financial datasets
- Investigation of alternative quantum input models for stochastic processes
- Exploration of hybrid quantum-classical approaches for optimal stopping problems
- Analysis of the algorithm's performance under different approximation architectures
- Resource estimation for practical implementation of the quantum LSM algorithm
## Key ideas
- #idea:quantum-advantage — Quantum LSM algorithm achieves nearly quadratic runtime speedup over classical LSM for stochastic optimal stopping problems (e.g., American option pricing) under theoretical assumptions
- #idea:near-term-feasibility — Algorithm assumes quantum access to stochastic processes and quantum Monte Carlo techniques, but feasibility on NISQ devices remains untested
- #idea:hybrid-approach — Potential for hybrid quantum-classical implementations to address qubit limitations and noise, though not explicitly proposed in the paper
- #limitation:noise — Theoretical speedup does not account for noise/decoherence in near-term quantum hardware, which could degrade performance
- #limitation:data-encoding — Assumes efficient quantum sampling access to Markov chains and payoff functions, but practical encoding of financial data remains challenging
- #limitation:no-empirical-validation — Claims are theoretical; no empirical validation on real quantum hardware or real-world financial datasets
## Contradictions
<!-- Step 6 output — where this paper contradicts others -->

## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
