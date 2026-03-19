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
quantum_advantage_claim: speculative
related_papers:
- 2023_Holst_QuantumKnapsack
relevance_phase1: high
relevance_phase3: medium
source_type: peer-reviewed-empirical
source_type_confidence: high
step1_date: '2026-03-18T22:26:05.952926'
step1_model: Mistral-Large-3
step2_date: '2026-03-18T22:26:07.574513'
step2_model: Mistral-Large-3
step3_date: '2026-03-18T22:26:09.526683'
step3_model: Mistral-Large-3
step4_date: '2026-03-18T22:27:40.619278'
step4_model: Mistral-Large-3
step5_date: '2026-03-18T22:27:47.528237'
step5_model: Mistral-Large-3
step6_date: '2026-03-18T22:27:52.124669'
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
This paper explores the application of the Quantum Approximate Optimization Algorithm (QAOA) to financial portfolio optimization by reformulating it as a knapsack problem. The authors adapt QAOA to incorporate domain-specific investment constraints and expected returns from Markowitz analysis, evaluating the approach on both simulated and real quantum hardware. The study demonstrates how quantum computing methods can address complex decision-making challenges in financial services.
## Methodology
The paper presents an empirical study that applies the Quantum Approximate Optimization Algorithm (QAOA) to solve the financial portfolio optimization problem by reformulating it as a knapsack problem. The methodology involves mapping expected returns from Markowitz analysis into the knapsack formulation while incorporating domain-specific investment constraints. The study evaluates the QAOA-based approach using both simulated and real quantum devices. The feasibility oracle and mixer components of the QAOA framework are adapted from prior work, with modifications to tailor the algorithm for financial portfolio selection. The research demonstrates the practical application of QAOA in complex financial decision-making scenarios.

**Algorithms used:** QAOA

**Experimental setup:** Experiments were conducted using both quantum simulators and real quantum processing units (QPUs). Specific hardware details or simulators are not explicitly mentioned, but the study involves testing on actual quantum devices.

**Dataset:** Expected returns derived from Markowitz portfolio analysis, adapted into a knapsack problem formulation with financial constraints. Specific datasets (e.g., historical stock prices) are not detailed in the provided text.
## Findings
- [supported] The QAOA-based approach for portfolio optimization reformulates the problem as a knapsack problem, incorporating expected returns from Markowitz analysis and domain-specific investment constraints
- [supported] The method was evaluated using both simulated and real quantum devices, demonstrating practical applicability in financial decision problems
- [speculative] The novelty of the study lies in extending the QAOA framework to financial portfolio selection, though the core quantum circuit components (feasibility oracle and mixer) are adapted from prior work [2]
- [supported] The paper acknowledges similarities in mathematical derivation with reference [2], specifically in the design of the feasibility oracle and mixer components

**Results summary:** The paper presents an empirical evaluation of a QAOA-based approach for knapsack-formulated portfolio optimization in financial services. The authors adapt existing quantum circuit components (feasibility oracle and mixer) to incorporate Markowitz-style expected returns and investment constraints. The method is tested on both quantum simulators and real hardware, though the core quantum advantage claims remain unquantified. The work extends prior theoretical constructs to a practical financial domain but does not demonstrate a clear quantum advantage over classical methods.
## Quantum advantage claim
**Classification:** speculative

No explicit quantum advantage is demonstrated; results are derived from both simulation and real hardware, but no performance metrics (e.g., speedup, accuracy thresholds) are provided to substantiate a quantum advantage. The claim is based on theoretical extension of QAOA to financial problems rather than empirical superiority.
## Limitations
- Experiments conducted on limited qubit counts (not explicitly stated, but likely constrained by available quantum hardware) [inferred]
- Evaluation performed using both simulated and real quantum devices, but real hardware results may be affected by noise and decoherence [inferred]
- Portfolio optimization problem reformulated as a knapsack problem, which may not fully capture the complexity of real-world financial constraints [inferred]
- Reliance on prior work (Holst, 2023) for feasibility oracle and mixer components, limiting novelty in quantum circuit design
- No explicit comparison with state-of-the-art classical portfolio optimization methods to benchmark performance [inferred]
- Dataset size and diversity not specified, potentially limiting generalizability of results [inferred]
- Scalability to larger problem instances (e.g., >20 assets) not demonstrated [inferred]
- Reproducibility may be constrained by proprietary or undisclosed details of the real quantum hardware experiments [inferred]
## Open questions
- How does the QAOA-based approach perform on larger-scale portfolio optimization problems with more than 20 assets?
- What is the impact of quantum hardware noise and decoherence on the solution quality for real-world financial datasets?
- Can the knapsack-based reformulation effectively handle dynamic or multi-period portfolio optimization constraints?
- How does the proposed method compare to classical optimization techniques in terms of solution quality and computational efficiency?

**Future work:**
- Extend the QAOA framework to multi-period or dynamic portfolio optimization problems
- Test the algorithm on larger qubit counts and more diverse real-world financial datasets
- Incorporate noise mitigation techniques to improve performance on real quantum hardware
- Benchmark against state-of-the-art classical solvers to assess quantum advantage
- Explore hybrid quantum-classical approaches to enhance scalability and practical applicability
## Key ideas
- #idea:near-term-feasibility — QAOA is adapted for portfolio optimization using a knapsack reformulation, tested on both simulated and real quantum hardware, demonstrating practical applicability in financial decision-making
- #idea:hybrid-approach — The approach incorporates classical Markowitz analysis for expected returns and domain-specific constraints, suggesting a hybrid quantum-classical workflow
- #limitation:noise — Real hardware results may be degraded by noise and decoherence, though noise mitigation is proposed as future work
- #limitation:qubit-count — Scalability to larger problem instances (>20 assets) is not demonstrated, likely due to limited qubit counts
- #limitation:no-empirical-validation — No explicit quantum advantage is demonstrated; results lack performance benchmarks against classical methods
## Contradictions
<!-- Step 6 output — where this paper contradicts others -->

## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
