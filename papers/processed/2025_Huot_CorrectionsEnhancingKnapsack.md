---
aliases:
- Enhancing Knapsack-Based Financial Portfolio Optimization Using Quantum Approximate
  Optimization Algorithm
- Enhancing Knapsack Based Financial
authors:
- Chansreynich Huot
- Kimleang Kea
- Tae-Kyung Kim
- Youngsun Han
auto_detected: true
classification: ''
contradiction_flags: []
doi: 10.1109/ACCESS.2024.3506981
evidence_type: ''
idea_tags:
- idea:near-term-feasibility
- idea:hybrid-approach
journal_or_venue: IEEE Access
methodology_tags:
- QAOA
- QUBO
paper_type: ''
quantum_advantage_claim: not-applicable
related_papers:
- 2023_Holst_QuantumPortfolio
relevance_phase1: high
relevance_phase3: medium
source_type: peer-reviewed-empirical
source_type_confidence: high
step1_date: '2026-03-19T13:36:44.878760'
step1_model: Mistral-Large-3
step2_date: '2026-03-19T13:36:57.359771'
step2_model: Mistral-Large-3
step3_date: '2026-03-19T13:37:16.538041'
step3_model: Mistral-Large-3
step4_date: '2026-03-19T13:37:22.815952'
step4_model: Mistral-Large-3
step5_date: '2026-03-19T13:37:30.010482'
step5_model: Mistral-Large-3
step6_date: '2026-03-19T13:37:33.782309'
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
- method/QAOA
- method/QUBO
- idea/near-term-feasibility
- idea/hybrid-approach
title: Enhancing Knapsack-Based Financial Portfolio Optimization Using Quantum Approximate
  Optimization Algorithm
topic_tags:
- portfolio-optimisation
year: 2024
zotero_key: ''
---

## Abstract summary
This paper explores the application of the Quantum Approximate Optimization Algorithm (QAOA) to financial portfolio optimization by reformulating the problem as a knapsack model. The authors adapt QAOA to incorporate financial constraints and expected returns from Markowitz analysis, demonstrating its practical use in portfolio selection. The study evaluates the approach on both simulated and real quantum hardware, highlighting its potential for solving complex financial decision-making problems.
## Methodology
The paper presents an empirical study that enhances financial portfolio optimization by reformulating it as a knapsack problem and solving it using the Quantum Approximate Optimization Algorithm (QAOA). The methodology involves mapping expected returns from Markowitz analysis to a knapsack formulation, incorporating domain-specific investment constraints, and evaluating the QAOA-based approach. The study adapts prior quantum circuit components, such as the feasibility oracle and mixer structure, to the financial domain. The research evaluates the proposed method using both simulated and real quantum devices to demonstrate its practical applicability in financial decision-making.

**Algorithms used:** QAOA

**Experimental setup:** Experiments were conducted using both simulated and real quantum processing units (QPUs). Specific hardware details or simulators are not explicitly mentioned, but the study involves practical implementation on quantum devices.

**Dataset:** The paper utilizes financial data derived from Markowitz portfolio analysis, including expected returns and investment constraints, though specific datasets (e.g., historical stock prices or indices) are not detailed.
## Findings
- [supported] The QAOA-based approach for portfolio optimization reformulates the problem as a knapsack problem and achieves measurable results on both simulated and real quantum devices
- [supported] The study maps expected returns from Markowitz analysis to the knapsack formulation and incorporates domain-specific investment constraints
- [supported] The feasibility oracle and mixer components of the QAOA framework were adapted from prior work [2], with extensions for financial portfolio selection
- [speculative] The adaptation of QAOA-based methods demonstrates potential for practical application in complex financial decision problems, though scalability to larger portfolios is not empirically validated

**Results summary:** The paper presents a QAOA-based method for solving portfolio optimization by reformulating it as a knapsack problem. The approach integrates Markowitz-based expected returns and investment constraints, evaluating performance on both quantum simulators and real hardware. While the core quantum circuit components are adapted from prior work, the novelty lies in extending the framework to financial portfolio selection. Results indicate feasibility but do not demonstrate quantum advantage over classical methods.
## Quantum advantage claim
**Classification:** not-applicable

The paper does not claim or demonstrate quantum advantage; results are focused on feasibility and adaptation of QAOA to financial problems without comparative performance metrics against classical methods.
## Limitations
- Experiments conducted on quantum devices with limited qubit counts, restricting the size of portfolio problems that can be solved [inferred]
- Reliance on synthetic or simplified financial data rather than real-world market data, limiting practical applicability [inferred]
- Potential hardware noise and decoherence effects not fully addressed in the evaluation, which may impact solution quality on real quantum devices [inferred]
- The study extends prior work (Holst, 2023) with similar quantum circuit components, which may limit the novelty of the approach [inferred]
- No explicit comparison with state-of-the-art classical portfolio optimization methods to benchmark performance [inferred]
- Reproducibility may be constrained by the use of proprietary or simulated quantum hardware [inferred]
- The correction acknowledges missing references, which could indicate gaps in the original literature review [inferred]
## Open questions
- How does the QAOA-based approach scale to larger portfolio sizes beyond the tested qubit constraints?
- What is the impact of quantum noise and error rates on the accuracy of portfolio optimization solutions?
- Can the method be adapted to handle dynamic or multi-period portfolio optimization problems?
- How does the performance of the quantum approach compare to classical solvers for real-world financial datasets?

**Future work:**
- Test the QAOA-based portfolio optimization on real quantum hardware with higher qubit counts (e.g., IBM Eagle or newer processors)
- Extend the framework to incorporate real-world financial data and constraints (e.g., transaction costs, regulatory limits)
- Investigate noise mitigation techniques to improve solution quality on noisy intermediate-scale quantum (NISQ) devices
- Compare the quantum approach with classical optimization methods to assess practical advantages
- Explore hybrid quantum-classical approaches to address scalability limitations
## Key ideas
- #idea:near-term-feasibility — QAOA is adapted for portfolio optimization via knapsack reformulation, tested on simulated and real quantum hardware, demonstrating practical applicability in financial decision-making
- #idea:hybrid-approach — Classical Markowitz analysis is integrated for expected returns and constraints, suggesting a hybrid quantum-classical workflow
- #limitation:qubit-count — Scalability to larger portfolios (>20 assets) is untested due to limited qubit counts
- #limitation:noise — Real hardware results may be degraded by noise and decoherence, with noise mitigation proposed as future work
- #limitation:no-empirical-validation — No quantum advantage is demonstrated; results lack benchmarks against classical methods
## Contradictions
<!-- Step 6 output — where this paper contradicts others -->

## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
