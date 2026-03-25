---
aliases:
- Corrections to ‘‘Enhancing Knapsack-Based Financial Portfolio Optimization Using
  Quantum Approximate Optimization Algorithm’’
- Corrections Enhancing Knapsack Based
authors:
- Chansreynich Huot
- Kimleang Kea
- Tae-Kyung Kim
- Youngsun Han
auto_detected: true
classification: ''
contradiction_flags:
- contradiction:classical-vs-quantum
- contradiction:scalability
doi: 10.1109/ACCESS.2025.3611744
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
- 2023_Holst_QAOAKnapsack
relevance_phase1: high
relevance_phase3: medium
source_type: peer-reviewed-theoretical
source_type_confidence: medium
step1_date: '2026-03-25T16:09:46.090888'
step1_model: gpt-5.1
step2_date: '2026-03-25T16:09:49.493442'
step2_model: gpt-5.1
step3_date: '2026-03-25T16:09:56.782015'
step3_model: gpt-5.4
step4_date: '2026-03-25T16:10:15.505074'
step4_model: gpt-5.4
step5_date: '2026-03-25T16:10:32.921827'
step5_model: gpt-5.4
step6_date: '2026-03-25T16:10:41.350293'
step6_model: gpt-5.4
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
- contradiction/classical-vs-quantum
- contradiction/scalability
title: Corrections to ‘‘Enhancing Knapsack-Based Financial Portfolio Optimization
  Using Quantum Approximate Optimization Algorithm’’
topic_tags:
- portfolio-optimisation
year: 2025
zotero_key: ''
---

## Abstract summary
This corrections note amends the earlier IEEE Access article on using QAOA for knapsack-based financial portfolio optimization by adding a previously omitted reference and clarifying methodological overlap. It explains how the original work builds on an existing bachelor’s thesis for specific quantum circuit components while extending the approach to financial portfolio selection, and updates the main text and code availability section accordingly.
## Methodology
This text is a correction notice rather than a full methods section, but it clarifies the methodological framing of the underlying study. The approach is a QAOA-based formulation of financial portfolio optimization by recasting the portfolio selection problem as a knapsack problem. Expected returns derived from Markowitz analysis are mapped into the knapsack objective, and domain-specific investment constraints are incorporated into the optimization model. The notice further states that parts of the quantum circuit design, specifically the feasibility oracle and mixer structure, follow prior constructions from Holst's thesis on QAOA for the knapsack problem, while the claimed contribution is the adaptation of that framework to financial portfolio selection. The paper is therefore best characterized as using a formal optimization reformulation grounded in Markowitz portfolio theory and constrained combinatorial optimization, with a quantum approximate optimization framework built on established knapsack-QAOA circuit components. No proofs, propositions, or formal derivations are provided in the correction text itself.

**Algorithms used:** QAOA, Markowitz portfolio optimization, Knapsack problem formulation
## Findings
- [speculative] This correction states that the original work reformulated financial portfolio optimization as a knapsack problem and applied QAOA to that formulation.
- [speculative] The authors claim the novelty of the original study lies in extending an existing QAOA knapsack framework to financial portfolio selection rather than introducing fundamentally new quantum circuit components.
- [speculative] The correction explicitly acknowledges that the feasibility oracle and mixer structure are consistent with prior constructions from Holst's 2023 thesis.
- [speculative] The paper claims to map expected returns from Markowitz analysis into a knapsack formulation and to incorporate domain-specific investment constraints.
- [speculative] The correction states that the method was evaluated on both simulated and real quantum devices, but provides no quantitative results in the correction text.
- [speculative] The authors argue that this adaptation illustrates practical applicability of QAOA-based methods to complex financial decision problems.

**Results summary:** This correction notice does not present new theoretical derivations, theorems, or quantitative results. Its main substantive claim is that the underlying 2024 paper applied QAOA to portfolio optimization by casting the problem as a knapsack problem, mapping Markowitz expected returns into that formulation, and adding investment constraints. The correction also clarifies that key circuit elements, specifically the feasibility oracle and mixer, were derived from prior work and that the claimed novelty is the financial-services application rather than the core QAOA construction. Although the text mentions evaluation on simulated and real quantum devices, it does not report metrics or evidence in the correction itself.
## Quantum advantage claim
**Classification:** speculative

The correction implies practical applicability of a QAOA-based approach and mentions testing on simulators and real hardware, but it provides no quantitative evidence or demonstrated advantage over classical methods in the text provided.
## Limitations
- This text is a correction notice rather than the full paper, so it provides very limited direct information about limitations, open questions, or future work.
- The correction states that key quantum circuit components, including the feasibility oracle and mixer structure, are consistent with prior constructions, limiting methodological novelty to the financial-domain adaptation rather than the core QAOA design.
- The paper required a post-publication correction to add a missing reference and clarify overlap in mathematical derivation with prior work, indicating incomplete attribution in the original publication.
- [inferred] As a peer-reviewed theoretical/method-focused work, the practical advantage over classical portfolio optimization methods is not established in this correction text.
- [inferred] The approach depends on reformulating portfolio optimization as a knapsack problem, which may require simplifying assumptions that do not capture the full Markowitz model or realistic market frictions.
- [inferred] Mapping expected returns from Markowitz analysis into a knapsack formulation may omit important financial features such as covariance structure, transaction costs, liquidity constraints, and multi-period dynamics.
- [inferred] Although the correction mentions evaluation on simulated and real quantum devices, no details are given here on hardware scale, noise effects, benchmark size, or reproducibility, limiting assessment of practical performance.
- [inferred] The gap between theoretical QAOA applicability and production-scale financial portfolio optimization remains unresolved, especially given likely qubit and circuit-depth constraints on current hardware.
## Open questions
- To what extent does the knapsack reformulation preserve the essential risk-return structure of portfolio optimization derived from Markowitz analysis?
- How much practical improvement, if any, does the QAOA-based method provide over state-of-the-art classical solvers for financial portfolio selection?
- How well does the method scale as the number of assets and investment constraints increases?
- What is the impact of real-device noise and limited circuit depth on solution quality for this portfolio optimization formulation?
- Which parts of the reported performance stem from the financial adaptation versus the previously known feasibility oracle and mixer construction?
- Can the approach handle more realistic portfolio settings, including covariance-aware risk modeling, transaction costs, cardinality constraints, and dynamic rebalancing?

**Future work:**
- Provide fuller empirical validation comparing the QAOA-based portfolio approach against strong classical optimization baselines.
- Investigate scalability on larger portfolio instances and more realistic financial datasets.
- Extend the formulation beyond a basic knapsack model to incorporate richer portfolio constraints and risk measures.
- Study the robustness of the method on real quantum hardware under noise, limited qubit counts, and depth constraints.
- Clarify and quantify the unique contribution of the financial-domain adaptation relative to prior QAOA knapsack constructions.
- Develop more practically relevant formulations for multi-period portfolio optimization and real-world investment decision support.
## Key ideas
- #idea:near-term-feasibility — Adapts an existing QAOA knapsack framework to financial portfolio optimisation and reports evaluation on simulators and real quantum devices, suggesting small-scale NISQ applicability.
- #idea:hybrid-approach — Uses classical Markowitz-derived expected returns and investment constraints, then encodes them into a knapsack-style optimisation problem for QAOA.
- #idea:near-term-feasibility — The claimed contribution is primarily the financial-domain adaptation rather than a new QAOA circuit design, with feasibility oracle and mixer inherited from prior work.
- #idea:hybrid-approach — Portfolio selection is simplified into a constrained combinatorial optimisation model, making it amenable to quantum optimisation workflows but at the cost of financial realism.
## Contradictions
- The paper implies practical applicability of QAOA for portfolio optimisation, but the correction text provides no quantitative evidence of superiority over classical solvers; this supports contradiction:classical-vs-quantum.
- The paper suggests relevance to financial decision problems, yet the open questions and limitations explicitly acknowledge unresolved scaling to realistic asset universes and constraints, supporting contradiction:scalability.
- Relative to prior knapsack-QAOA work such as 2023_Holst_QAOAKnapsack, the correction reduces the novelty claim from algorithmic innovation to domain adaptation, which weakens any implied broader quantum-performance claim.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->

## Experiment details
### Input
N/A

### Process
1. Reformulate the portfolio optimization problem as a knapsack problem. 2. Encode expected returns and constraints into the quantum circuit using feasibility oracles. 3. Apply the QAOA algorithm with parameterized quantum circuits. 4. Optimize the circuit parameters using classical optimization techniques. 5. Evaluate the performance on both simulators and real quantum devices.

### Output
Performance metrics related to portfolio optimization, such as solution quality and convergence behavior of the QAOA algorithm. Comparisons may be drawn against classical optimization baselines, though specific metrics are not detailed in the provided text.

### Parameters
N/A

### Hardware
Experiments conducted on both quantum simulators and real quantum devices (QPUs). Specific hardware models or providers are not mentioned in the provided text.

### Reproducibility
The paper references a Bachelor thesis that served as a foundation for certain quantum circuit components, suggesting partial reproducibility. However, the availability of code or datasets is not explicitly mentioned in the provided text, limiting a full reproducibility assessment.
